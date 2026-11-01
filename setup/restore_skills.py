#!/usr/bin/env python3
"""Validate a private skill archive and install selected skills without running them."""
import argparse, datetime, hashlib, io, json, os, pathlib, re, shutil, sys, unicodedata, zipfile

REPO = pathlib.Path(__file__).resolve().parents[1]
RESEARCH = {'pdf','pptx','docx','xlsx','matplotlib','scientific-visualization','scientific-writing','scientific-critical-thinking','scientific-brainstorming','literature-review','citation-management','research-lookup','nature-paper-card','nature-reader','paper-lookup','markdown-mermaid-writing','scikit-learn','pymoo','statistical-analysis','uncertainty-and-units'}

def validated_archive():
    snap=json.loads((REPO/'inventory/snapshot.json').read_text(encoding='utf8'))
    manifest=json.loads((REPO/'inventory/skills-files.json').read_text(encoding='utf8'))
    direct=REPO/'archives/skills.zip'
    if direct.exists():data=direct.read_bytes()
    else:
        parts=json.loads((REPO/'archives/skills-parts.json').read_text(encoding='utf8'))
        blocks=[]
        for part in parts:
            f=REPO/part['path'];b=f.read_bytes()
            if len(b)!=part['bytes'] or hashlib.sha256(b).hexdigest()!=part['sha256']:raise ValueError('Archive part mismatch: '+str(f))
            blocks.append(b)
        data=b''.join(blocks)
    if hashlib.sha256(data).hexdigest()!=snap['skills_archive_sha256']:raise ValueError('Archive SHA-256 mismatch')
    z=zipfile.ZipFile(io.BytesIO(data))
    expected={a['path']:a for a in manifest}
    names={a.filename for a in z.infolist() if not a.is_dir()}
    if names!=set(expected):raise ValueError('Archive file list mismatch')
    collision={}
    for n in names:
        p=pathlib.PurePosixPath(n)
        if p.is_absolute() or '..' in p.parts or '\\' in n or not p.parts or p.parts[0]!='skills':raise ValueError('Unsafe archive path')
        key=unicodedata.normalize('NFD',n).casefold()
        if key in collision and collision[key]!=n:raise ValueError('macOS filename collision: '+n)
        collision[key]=n
        b=z.read(n);e=expected[n]
        if len(b)!=e['bytes'] or hashlib.sha256(b).hexdigest()!=e['sha256']:raise ValueError('File SHA-256 mismatch: '+n)
    return z

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',action='store_true',help='Validate only; do not write user files')
    ap.add_argument('--profile',choices=['research','all'],default='research')
    ap.add_argument('--target',type=pathlib.Path,default=pathlib.Path.home()/'.agents/skills')
    ap.add_argument('--replace',action='store_true',help='Back up conflicting skill folders before replacing')
    args=ap.parse_args()
    z=validated_archive()
    inventory=json.loads((REPO/'inventory/skills.json').read_text(encoding='utf8'))
    # This package stores Windows-only workflows for reference, but never installs them on Mac.
    blocked={a['path'].split('/')[0] for a in inventory if a['platform']=='windows_only'}
    selected={a['path'].split('/')[0] for a in inventory if a['path'].split('/')[0] not in blocked and (args.profile=='all' or a['name'] in RESEARCH)}
    result={'archive_verified':True,'platform':sys.platform,'target':str(args.target),'profile':args.profile,'selected_folders':len(selected),'windows_only_not_installed':sorted(blocked),'installed':[],'already_identical':[],'conflicts_skipped':[],'check_only':args.check}
    if args.check:
        print(json.dumps(result,ensure_ascii=False,indent=2));return
    target=args.target.expanduser().resolve();target.mkdir(parents=True,exist_ok=True)
    backup=target.parent/'skill-backups'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    for name in sorted(selected):
        dst=target/name
        if dst.is_symlink():result['conflicts_skipped'].append(name+' (symlink)');continue
        prefix='skills/'+name+'/'
        members=[n for n in z.namelist() if n.startswith(prefix) and not n.endswith('/')]
        if dst.exists():
            if all((dst/n[len(prefix):]).is_file() and (dst/n[len(prefix):]).read_bytes()==z.read(n) for n in members):
                result['already_identical'].append(name);continue
            if not args.replace:result['conflicts_skipped'].append(name);continue
            backup.mkdir(parents=True,exist_ok=True);shutil.copytree(dst,backup/name)
            # A reviewed backup exists; remove only this resolved skill folder inside target.
            if dst.resolve().parent!=target:raise ValueError('Unsafe replacement target')
            shutil.rmtree(dst)
        for n in members:
            f=dst/n[len(prefix):];f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(z.read(n))
            if f.suffix in ['.sh','.py']:f.chmod(f.stat().st_mode | 0o100)
        result['installed'].append(name)
    if backup.exists():result['previous_skills_backup']=str(backup)
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
