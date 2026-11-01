v1

## User Profile

- Develops ANSYS Workbench/Fluent microchannel cooling studies and values reproducible, organized simulation artifacts.
- Explores ANN/NSGA-II surrogate optimization for microchannel and non-uniform-heat-source cold-plate design, including mechanism-based biomimetic vascular networks.
- Investigates recent aerogel-based electronic heat dissipation and the applicability boundary of chitosan-aerogel evaporation research.
- Produces microchannel research/group-meeting PPTs with an evidence-backed narrative and authentic CAD/CFD visuals. [ad-hoc note]
- Uses Codex and explicitly wants suitable installed skills considered before work begins. [ad-hoc note]

## User preferences

- Before future work, inspect available installed skills and use one only when it genuinely suits the request; do not invoke an unrelated skill merely because it is installed. [ad-hoc note]
- When modeling information is incomplete, “如果我的提问信息不全及时指出，我会提供更多信息” -> identify missing variables, ranges, constraints, boundary conditions, and output definitions before finalizing a plan.
- For biomimetic cooling claims, distinguish a tree-shaped optimized structure from a validated biological/transport mechanism and testable contribution.
- For ANSYS microchannel work, save artifacts on D drive: primary root `D:\Codex\2026-09-11\x`, final outputs `D:\Codex\2026-09-11\x\outputs`; avoid new C-drive results except an active-task compatibility file. [ad-hoc note]
- Archive reproducible milestones in `D:\Codex\Microchannel_Fluent_Archive` as sequential `V...` folders with complete `README.md`; keep shared evidence in `00_References` and exclude disposable intermediates. [ad-hoc note]
- Before advising on microchannel papers or simulation design, search retained project memory and relevant available threads; if old thread text is unavailable, say so and use retained memory plus supplied files. [ad-hoc note]
- For microchannel research/group-meeting PPTs, default to “研究背景→研究现状→研究内容→未来计划” using the latest supplied template; for a small edit, change only the requested portion. [ad-hoc note]
- Build research background from the original paper's introduction with PDF page numbers/evidence status; explain uniformity through hotspots, spatial temperature difference, reliability, and thermal stress rather than listing metrics. [ad-hoc note]
- Use actual SolidWorks/ANSYS API exports for model views (overall plus local hierarchy); never replace them with AI/redrawn outlines, distinguish structure views from simulation contours, and do not use computer use without approval. [ad-hoc note]
- For electronic-cooling literature, start with “近年 + 电子器件 + 强化散热”; keep sustained heat rejection distinct from insulation or short-term phase-change buffering.
- Do not equate solar-interfacial evaporation results with electronic evaporative cooling; state “机制可借鉴、应用尚未直接验证” unless direct device-cooling evidence exists.

## General Tips

- Small CFD datasets: fit scaling only on training folds, compare simple baselines, and treat 100 samples as initial evidence rather than a guaranteed high-accuracy ANN dataset.
- Do not equate “biomimetic” with novelty: compare against conventional and branching baselines under identical constraints, then test manufacturability, compute cost, and heat-map transfer.
- For microchannel Fluent runs, use 3D double precision and 4 solver processes unless a live license check supports more; save/update Workbench Setup and Solution, and use Fluent/CFD-Post to update Results when required. [ad-hoc note]
- If PDF text extraction fails with `UnicodeEncodeError: 'gbk' codec can't encode character`, configure stdout as UTF-8.
- When source pages block access (403/429/CAPTCHA), cross-check DOI with accessible abstracts/open full text and label conclusions that were not PDF-verified.
- For the user's microchannel slide rules, consult `C:\Users\PC\.codex\skills\pptx\SKILL.md` and its `references\user-research-presentation-rules.md`. [ad-hoc note]

## What's in Memory

### C:\Users\PC\.codex\.chatgpt-projects\g-p-6aa249ca204c8191af9f8af6ee519c78 / research literature

#### 2026-10-28

- Aerogel electronic cooling and chitosan evaporative-cooling literature: aerogel, electronic cooling, thermal interface material, chitosan aerogel, evaporative cooling, MXene, capillary transport
  - desc: Search first for recent aerogels that strengthen electronic-device heat dissipation, or for whether chitosan-aerogel evaporation work transfers to chip cooling.
  - learnings: Separate aerogel-derived TIM/heat-sink evidence from porous insulation; chitosan examples support capillary/porosity mechanisms but not direct chip-cooling claims.

### D:\Codex\2026-09-11\x / microchannel project

#### 2026-10-23

- Microchannel research and group-meeting PPT production: 研究背景→研究现状→研究内容→未来计划, 原论文前言, PDF页码, 鱼鳍论文Fig.1, SolidWorks API, ANSYS API, computer use
  - desc: Search first when drafting or narrowly revising this user's microchannel research/group-meeting deck; these are personal, template-aware slide rules. [ad-hoc note]
  - learnings: Ground the background in original-paper evidence, connect uniformity to hotspots/reliability/thermal stress, and use authentic CAD exports for overall-plus-local structure views. [ad-hoc note]

#### 2026-09-16

- Manifold-jet paper context and open pin-fin study design: Wu et al., 10.1038/s41928-025-01449-4, Li et al., 10.1016/j.applthermaleng.2026.132654, open pin-fin layer, equal-pumping-power, ANN, NSGA-II
  - desc: Search first for the retained reference platform, fish-fin comparison, density-gradient pin-fin layer, or novelty framing; extension-derived context. [ad-hoc note]
  - learnings: Reusing manifold/jet/heater/boundaries is a control choice; fairly compare open-array flow redistribution and density law. [ad-hoc note]

### D:\data\ANN / microchannel research design

#### 2026-10-09

- ANN/NSGA-II surrogate and biomimetic vascular-manifold research design: MLPRegressor, lbfgs, 80 development samples, 20 independent test samples, topology optimization, OpenCCO
  - desc: Search first for small-sample CFD surrogate plans, fish-fin ANN/NSGA-II paper facts, demand-driven vascular manifold novelty, or synthetic-vascular-network algorithms; cwd=`D:\data\ANN`.
  - learnings: Define variables and constraints before ANN settings; use a three-method comparison before spending the 100-case CFD budget, and treat thermal-demand-to-flow mapping as a hypothesis.

### Older Memory Topics

#### C:\Users\PC\.codex\skills / cross-task Codex workflow

- Codex installed-skill selection: prioritize suitable installed skills, grill-me, grilling, C:\Users\PC\.codex\skills
  - desc: Search first when deciding whether a new task needs an installed skill; covers suitable-skill selection and plan/design interview helpers. [ad-hoc note]
  - learnings: Check the catalog first, read only a genuinely relevant skill, and do not treat installation as a mandate. [ad-hoc note]

#### D:\Codex\2026-09-11\x / D:\Codex\Microchannel_Fluent_Archive

- ANSYS microchannel Fluent project storage, archive, and Workbench cases: D:\Codex\2026-09-11\x, D:\Codex\Microchannel_Fluent_Archive, V1_, 3D double precision, 4 solver processes
  - desc: Use for storage, `README.md` archive rules, shared-Geometry multi-case Workbench layouts, or Fluent launch/cell-update defaults; extension-derived and checkout-specific. [ad-hoc note]
