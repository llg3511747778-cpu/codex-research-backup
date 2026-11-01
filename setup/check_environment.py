#!/usr/bin/env python3
"""Read-only environment checks. No software install, authentication, or solver launch."""
import importlib.util,json,pathlib,platform,shutil,sys
modules=['numpy','pandas','matplotlib','scipy','h5py','pypdf','docx','pptx','openpyxl']
print(json.dumps({'os':platform.system(),'architecture':platform.machine(),'python':sys.version,'tools':{x:shutil.which(x) for x in ['git','node','python3','pdftoppm','pandoc']},'python_modules':{x:bool(importlib.util.find_spec(x)) for x in modules},'skills_directory':str(pathlib.Path.home()/'.agents/skills'),'windows_solver_automation':'Run on the compatible Windows host; not validated on macOS.'},ensure_ascii=False,indent=2))
