# Task Group: Aerogel electronic cooling and chitosan evaporative-cooling literature

scope: Recent-literature screening for aerogels that strengthen electronic-device heat dissipation, and for chitosan aerogels whose evaporation mechanisms may or may not transfer to electronics cooling.
applies_to: cwd=C:\Users\PC\.codex\.chatgpt-projects\g-p-6aa249ca204c8191af9f8af6ee519c78; reuse_rule=reuse the screening criteria and evidence boundaries for related literature questions; re-verify paper-level claims and current coverage before treating the list as exhaustive.

## Task 1: 筛选近几年面向电子器件、能够强化散热的气凝胶研究, success

### rollout_summary_files

- rollout_summaries/2026-10-28T02-10-14-CWTU-aerogel_electronics_heat_dissipation_chitosan_evaporation.md (cwd=C:\Users\PC\.codex\.chatgpt-projects\g-p-6aa249ca204c8191af9f8af6ee519c78, rollout_path=\\?\C:\Users\PC\.codex\sessions\2026\10\28\rollout-2026-10-28T10-10-14-01a18045-b688-7b83-8867-8742b7bf3242.jsonl, updated_at=2026-10-28T06:37:15+00:00, thread_id=01a18045-b688-7b83-8867-8742b7bf3242)

### keywords

- aerogel, electronic cooling, graphene aerogel, thermal interface material, heat sink, thermal resistance, BNNS/PVA, 10.1016/j.applthermaleng.2024.125325, 10.3390/ma16237419, 10.1038/s41467-025-65983-7

## Task 2: 查找壳聚糖气凝胶用于蒸发强化的近年研究，并判断其对电子器件蒸发冷却的相关性, success

### rollout_summary_files

- rollout_summaries/2026-10-28T02-10-14-CWTU-aerogel_electronics_heat_dissipation_chitosan_evaporation.md (cwd=C:\Users\PC\.codex\.chatgpt-projects\g-p-6aa249ca204c8191af9f8af6ee519c78, rollout_path=\\?\C:\Users\PC\.codex\sessions\2026\10\28\rollout-2026-10-28T10-10-14-01a18045-b688-7b83-8867-8742b7bf3242.jsonl, updated_at=2026-10-28T06:37:15+00:00, thread_id=01a18045-b688-7b83-8867-8742b7bf3242)

### keywords

- chitosan aerogel, evaporative cooling, solar interfacial evaporation, MXene, capillary transport, dry-out time, 10.1002/advs.202505944, 10.1039/D4SE00617H, 10.1021/acssuschemeng.2c06472, 10.1016/j.desal.2024.117333

## User preferences

- When screening this literature, the user narrowed the request to “近几年的”“用于电子器件的”“最好还是有利于强化散热” -> begin with that retrieval contract; exclude generic insulation, building, and battery-safety papers unless explicitly requested. [Task 1]
- The user cares about sustained heat rejection, not merely insulation or short-term phase-change buffering -> distinguish 导热、均热、TIM、对流/液冷耦合、持续散热 from insulation and transient thermal buffering. [Task 1]
- In an electronic-cooling context, the user asked whether chitosan aerogels are used for evaporation enhancement -> search solar interfacial evaporation and electronic evaporative cooling as separate evidence chains, then state their boundary explicitly. [Task 2]

## Reusable knowledge

- For aerogel-enabled electronic cooling, ask whether the design lowers total device-to-coolant thermal resistance at the same heat load and pump/fan power; compare maximum temperature, total/contact thermal resistance, pressure drop, thickness-direction conduction, and electrical insulation. Loose aerogels are often insulators; credible cooling examples more often use aerogel-derived dense TIM films, oriented conductive networks, or aerogel-integrated heat sinks. [Task 1]
- `10.1016/j.applthermaleng.2024.125325` is a 2025 topology-optimized graphene-aerogel forced-air heat-sink study; its reported approximately 28.4% thermal-resistance reduction and at-least-14% solid-volume reduction are numerical results, not experimental validation. `10.3390/ma16237419` reports a hot-pressed graphene-aerogel-derived TIM film with approximately 740/42.5 W·m⁻¹·K⁻¹ in-plane/through-plane conductivity, not a pristine porous aerogel. `10.1016/j.compositesa.2025.108802` uses an aerogel template to organize an electrically insulating BNNS/PVA conductive network; check through-thickness conductivity separately. [Task 1]
- `10.1038/s41467-025-65983-7` (AlN aerogel thermo-cooler) supports vertical channels, capillary liquid supply, and phase-change heat rejection as mechanisms, but its extreme-environment setting is not direct chip-cooling validation. [Task 1]
- Current chitosan-aerogel examples are chiefly solar interfacial evaporation/desalination rather than chip evaporative cooling: MXene/natural-fiber directed pores (`10.1002/advs.202505944`), MXene/chitosan wet-stability and capillary supply (`10.1039/D4SE00617H`), WS₂/chitosan oriented microchannels (`10.1021/acssuschemeng.2c06472`), and a hydrophilic-shell/hydrophobic-core structure (`10.1016/j.desal.2024.117333`). Treat them as supply/porosity design references, not electronic-cooling performance evidence. [Task 2]
- To substantiate electronic evaporative cooling with a chitosan aerogel, measure device temperature, imposed heat flux/evaporative latent heat, total thermal resistance, wet-state heat transfer, liquid-supply stability, dry-out time, vapor removal, and controls including a bare surface and conventional porous wick. [Task 2]

## Failures and how to do differently

- Symptom: search returns insulation, radiative cooling, or battery thermal-runaway work -> cause: the query does not encode “近年 + 电子器件 + 强化散热” -> fix: set that screening contract before gathering papers, and label any peripheral material explicitly. [Task 1]
- Symptom: a source page yields 403, 429, or CAPTCHA -> cause: publisher access barriers -> fix: cross-check DOI with PubMed, open full text, or reliable abstracts; say when conclusions are based only on accessible abstracts rather than PDF-level experimental detail. [Task 1]
- Symptom: solar-evaporation flux is presented as chip heat-removal capability -> cause: conflating different heat inputs, area definitions, and environments -> fix: retain “机制可借鉴、应用尚未直接验证”; use an electronic heat source with controlled heat load, humidity, airflow, liquid feed, and wick controls for a direct test. [Task 2]
- Symptom: a proposed chitosan wick improves capillarity but degrades cooling -> cause: ignored tradeoffs between pore size/capillary force versus flow resistance, low conductivity versus heat delivery to the evaporation interface, and hydrophilicity versus parasitic heat loss to bulk liquid -> fix: evaluate these coupled tradeoffs rather than optimizing evaporation rate alone. [Task 2]

# Task Group: Microchannel research and group-meeting PPT production

scope: User-specific rules for microchannel research/group-meeting slide decks: four-part narrative, evidence-backed background, CAD/CFD visuals, and tightly scoped revisions.
applies_to: cwd=D:\Codex\2026-09-11\x and future microchannel research/group-meeting presentations; reuse_rule=apply only to this user's microchannel research slides, using the latest supplied PPT template/layout and the installed pptx skill reference; do not generalize these rules to unrelated presentations.

## Task 1: Preserve research-PPT background, structure-display, and edit-boundary rules

### rollout_summary_files

- No rollout summary on disk; authoritative extension note: extensions/ad_hoc/notes/20261023-180000-research-ppt-background-and-cad-views.md (cwd=D:\Codex\2026-09-11\x, rollout_path=not available, updated_at=2026-10-23T18:00:00, extension-derived evidence) [ad-hoc note]

### keywords

- 研究背景→研究现状→研究内容→未来计划, PPT母版, 原论文前言, PDF页码, 均温性, 局部热点, 空间温差, PEC, 鱼鳍论文Fig.1, SolidWorks API, ANSYS API, 原生结构图, 仿真场图, computer use

## User preferences

- When creating a microchannel research/group-meeting PPT, the user specified the default structure “研究背景→研究现状→研究内容→未来计划” and wants the latest supplied PPT template and layout followed. For a small requested revision, change only the specified portion; do not introduce a broad new framework. [Task 1] [ad-hoc note]
- Before writing research background, read the relevant original paper's introduction; trace the argument from application need to the specific problem, and record PDF page numbers and evidence status. [Task 1] [ad-hoc note]
- When temperature uniformity is a goal, explain the connection among local hotspots, spatial temperature difference, reliability, and thermal stress; do not merely list metrics. Put PEC and similar performance coefficients on the actual evaluation slide, and avoid excessive small text at lower left. [Task 1] [ad-hoc note]
- For structure display, show both overall and local views, following the fish-fin paper Fig. 1 hierarchy “整体—单胞—流道”. Export model views through the actual SolidWorks/ANSYS software API; do not substitute AI-generated images or redrawn outlines, and distinguish native structure images from simulation contour plots. [Task 1] [ad-hoc note]
- The user explicitly does not permit unapproved use of computer use. [Task 1] [ad-hoc note]

## Reusable knowledge

- Related skill: `C:\Users\PC\.codex\skills\pptx\SKILL.md`; its `references\user-research-presentation-rules.md` is the detailed executable reference for these personal presentation rules. [Task 1] [ad-hoc note]

## Failures and how to do differently

- Symptom: a microchannel slide deck has generic background, AI/redrawn model imagery, or an overhauled layout after a narrow edit request -> cause: the user-specific evidence, visual-source, and edit-scope rules were not applied -> fix: consult the latest provided template plus the pptx reference, document original-paper evidence/page status, export CAD views from SolidWorks/ANSYS, and limit edits to the requested part. [Task 1] [ad-hoc note]

# Task Group: ANN/NSGA-II surrogate and biomimetic vascular-manifold research design

scope: Small-sample CFD surrogate planning, fish-fin paper method extraction, and mechanism-based novelty testing for non-uniform-heat-source vascular manifolds.
applies_to: cwd=D:\data\ANN; reuse_rule=reuse for related microchannel CFD, ANN, NSGA-II, and vascular-network design questions; do not transfer numerical settings or biological assumptions to another cold-plate geometry without defining its variables, constraints, and physics.

## Task 1: Plan a small-sample ANN surrogate model from CFD samples, partial

### rollout_summary_files

- rollout_summaries/2026-09-15T03-49-51-aVgx-ann_nsga2_biomimetic_vascular_manifold_planning.md (cwd=D:\data\ANN, rollout_path=\\?\C:\Users\PC\.codex\sessions\2026\09\15\rollout-2026-09-15T11-49-51-01a0a32f-76c2-70f0-8520-56e97fdcbaa5.jsonl, updated_at=2026-10-09T14:41:03+00:00, thread_id=01a0a32f-76c2-70f0-8520-56e97fdcbaa5, partial because variables/ranges were not supplied)

### keywords

- small-sample ANN, CFD-generated data, MLPRegressor, lbfgs, Latin-hypercube sampling, training-fold-only scaling, temperature, pressure drop

## Task 2: Extract the fish-fin microchannel ANN + NSGA-II method, success

### rollout_summary_files

- rollout_summaries/2026-09-15T03-49-51-aVgx-ann_nsga2_biomimetic_vascular_manifold_planning.md (cwd=D:\data\ANN, rollout_path=\\?\C:\Users\PC\.codex\sessions\2026\09\15\rollout-2026-09-15T11-49-51-01a0a32f-76c2-70f0-8520-56e97fdcbaa5.jsonl, updated_at=2026-10-09T14:41:03+00:00, thread_id=01a0a32f-76c2-70f0-8520-56e97fdcbaa5)

### keywords

- Biomimetic fish-fin microchannels for energy-efficient manifold liquid cooling, 200 CFD cases, 5 inputs, pressure drop, area-normalized thermal resistance, NSGA-II population 100, WT, WF, WW, theta, UnicodeEncodeError gbk

## Task 3: Assess a demand-driven vascular manifold for a non-uniform heat source, partial

### rollout_summary_files

- rollout_summaries/2026-09-15T03-49-51-aVgx-ann_nsga2_biomimetic_vascular_manifold_planning.md (cwd=D:\data\ANN, rollout_path=\\?\C:\Users\PC\.codex\sessions\2026\09\15\rollout-2026-09-15T11-49-51-01a0a32f-76c2-70f0-8520-56e97fdcbaa5.jsonl, updated_at=2026-10-09T14:41:03+00:00, thread_id=01a0a32f-76c2-70f0-8520-56e97fdcbaa5, use before committing the 100-case CFD budget)

### keywords

- non-uniform heat source, fixed hotspot, vascular manifold, topology optimization, supply-return manifold, regular lower microchannels, fixed total flow, 100 CFD cases, manufacturability, transferability

## Task 4: Review recent synthetic vascular-network generation methods, success

### rollout_summary_files

- rollout_summaries/2026-09-15T03-49-51-aVgx-ann_nsga2_biomimetic_vascular_manifold_planning.md (cwd=D:\data\ANN, rollout_path=\\?\C:\Users\PC\.codex\sessions\2026\09\15\rollout-2026-09-15T11-49-51-01a0a32f-76c2-70f0-8520-56e97fdcbaa5.jsonl, updated_at=2026-10-09T14:41:03+00:00, thread_id=01a0a32f-76c2-70f0-8520-56e97fdcbaa5)

### keywords

- CCO, OpenCCO, supply-demand generation, tissue growth, cDCGAN, LFDO-CCO, Murray law, 10.1007/s10237-023-01703-8, 10.1111/micc.12854, 10.1126/science.adj6152

## User preferences

- When modeling details are incomplete, the user said “如果我的提问信息不全及时指出，我会提供更多信息” -> identify missing variables, ranges, constraints, fixed boundary conditions, and output definitions before finalizing an ANN/optimization plan. [Task 1]
- When proposing biomimetic cold-plate research, the user challenged whether “a tree-like structure plus optimization” really tells a vascular-network story -> distinguish visual resemblance from a validated biological/transport mechanism and a testable contribution. [Task 3]

## Reusable knowledge

- For small tabular CFD datasets, use feasible-space Latin-hypercube or comparable space-filling sampling; a starting plan is about 80 development samples, 20 independent test samples, cross-validation inside development data, a small `MLPRegressor` tested with `lbfgs`, simple regression baselines, and preprocessing fitted only on training folds. Treat 100 samples as an initial dataset, not a guaranteed high-accuracy ANN dataset. [Task 1]
- The fish-fin paper workflow is CFD-generated data -> ANN surrogate -> NSGA-II Pareto search -> CFD verification. It reports 200 initial CFD cases, 5 inputs, and two outputs (pressure drop and area-normalized thermal resistance); the fifth input being flow rate was inferred rather than explicitly enumerated. Training R² values were 0.993 and 0.986; validation relative errors 1.51% and 8.10%; test relative errors 1.52% and 6.56%. Its population size 100 is the NSGA-II initial population, not the CFD sample count. [Task 2]
- For the selected fish-fin geometry, `WT=20 μm`, `WF=25 μm`, `WW=20 μm`, and `θ=60°`; the 8 μm fillet was a separate later analysis. The paper does not fully disclose ANN architecture, split proportions, training algorithm, NSGA-II generation count, or exact relative-error definition. Preserve those as unknowns. [Task 2]
- Model the complete supply -> heat-exchanger microchannels -> return path. With an asymmetric heat source, do not assume uniform channel flow or symmetry. Compare conventional manifold, unmodified branching manifold, and heat-source-matched branching manifold under identical geometry, material, flow, and manufacturing constraints; use maximum temperature, pressure drop or pumping power, and temperature uniformity, then rerun CFD after dimensions are rounded. [Task 3]
- A stronger vascular-manifold contribution needs demonstrable advantage over topology optimization: repeatable cross-heat-source transfer, lower design/computation cost, guaranteed connected/manufacturable networks, or a validated rule linking heat-demand distribution to flow allocation. [Task 3]
- Demand-driven growth is the most transferable synthetic-vasculature mechanism: local demand guides territory growth, terminal creation, branch size, and work/maintenance cost. Treat mapping thermal demand to cooling demand as a new engineering hypothesis; account for lateral conduction, fluid temperature rise, return-path resistance, rectangular-channel hydraulics, and manufacturing constraints. [Task 4]

## Failures and how to do differently

- Symptom: an ANN plan specifies architecture or sampling ranges without a parameter list -> cause: geometry, operating ranges, constraints, and precise temperature/pressure-drop definitions are missing -> fix: request those inputs first and state uncertainty instead of promising that 100 samples are enough. [Task 1]
- Symptom: PDF extraction fails on Windows with `UnicodeEncodeError: 'gbk' codec can't encode character` -> cause: console output encoding -> fix: configure Python stdout with `sys.stdout.reconfigure(encoding='utf-8')` before printing extracted text. [Task 2]
- Symptom: “biomimetic” is asserted as novelty under fixed heat source, fixed flow, and ordinary temperature/pressure objectives -> cause: demand-driven branch generation plus optimization is mathematically close to constrained topology optimization -> fix: before allocating 100 CFD samples, run a small three-method comparison measuring performance, design cost, manufacturability, shifted-hotspot transfer, and the vascular rule's effect. [Task 3]

# Task Group: Microchannel manifold-jet paper context and open pin-fin study design

scope: Prior literature, retained design choices, and novelty framing for the user's manifold-jet microchannel cooling study; use before advising on paper comparisons, simulation design, or optimization claims.
applies_to: cwd=D:\Codex\2026-09-11\x and future microchannel project conversations; reuse_rule=use as retained project context, but search project memory and available thread history first; if prior thread text is unavailable, say so and rely on retained memory plus user-provided files.

## Task 1: Retain jet-manifold references and proposed open pin-fin study framing

### rollout_summary_files

- No rollout summary on disk; authoritative extension note: extensions/ad_hoc/notes/20260916-120000-jet-manifold-paper-context.md (cwd=D:\Codex\2026-09-11\x, rollout_path=not available, updated_at=2026-09-16T12:00:00, extension-derived evidence)

### keywords

- jet-enhanced manifold microchannels, Wu et al., 10.1038/s41928-025-01449-4, tapered manifold, intermediate jet plate, 3 mm by 3 mm uniform heater, fish-fin microchannels, Li et al., 10.1016/j.applthermaleng.2026.132654, open pin-fin layer, 50 micrometre-wide channels, 50 micrometre-thick sidewalls, ANN, NSGA-II, equal-pin-volume, equal-pumping-power

## User preferences

- For future conversations in the microchannel project, first search project memory for prior discussions and decisions about relevant papers and simulation design; if thread-history tools are available, review the relevant project threads before advising. If old thread text is unavailable, state that plainly and use retained memory plus files the user provides. [Task 1]

## Reusable knowledge

- The retained project reference context identifies Wu et al., “Jet-enhanced manifold microchannels for cooling electronics up to a heat flux of 3,000 W cm-2,” Nature Electronics 8 (2025) 810-817, DOI `10.1038/s41928-025-01449-4`: tapered manifold, intermediate jet plate, lower straight or sawtooth microchannel layer, and a 3 mm by 3 mm uniform heater. [Task 1]
- The follow-on reference is recorded as Li et al., “Biomimetic fish-fin microchannels for energy-efficient manifold liquid cooling,” Applied Thermal Engineering 304 (2026) 132654, DOI `10.1016/j.applthermaleng.2026.132654`; it reuses a similar manifold-jet platform and changes the lower heat-transfer layer to fish-fin microchannels. [Task 1]
- The proposed study keeps the reference manifold, jet plate, chip heat-source area, and boundary conditions, while replacing continuous 50 micrometre-wide channels and 50 micrometre-thick sidewalls with an open pin-fin layer. The proposed design space includes cold-to-hot-side pin-fin density gradients and may use ANN plus NSGA-II. [Task 1]
- Frame novelty around the open-array flow-redistribution mechanism, density-distribution law, fair equal-pin-volume/equal-pumping-power comparisons, and applicability limits. Reusing the cited manifold and boundary conditions is an experimental/control choice, not itself a novelty defect. [Task 1]

## Failures and how to do differently

- Symptom: advice implies that prior project decisions or relevant paper discussion are available when they are not -> cause: assuming old thread text can be retrieved -> fix: search project memory and available thread history first; otherwise explicitly state the limit and ask for/proceed from supplied files. [Task 1]
- Symptom: novelty is rejected merely because the manifold, jet plate, heater area, or boundary conditions match a reference -> cause: treating controls/platform reuse as the claimed contribution -> fix: assess the new open-array flow redistribution, density-gradient law, fair comparison basis, and limits instead. [Task 1]

# Task Group: Codex installed-skill selection

scope: Selecting installed Codex skills for a new task; use this preference before deciding whether a skill applies, not as a mandate to invoke a skill.
applies_to: cwd=C:\Users\PC\.codex\skills and all Codex tasks; reuse_rule=check the available installed-skill catalog first, then read and apply only instructions for skills genuinely suited to the request; the user's request and current authorization remain controlling.

## Task 1: Prefer suitable installed skills for future work

### rollout_summary_files

- No rollout summary on disk; authoritative extension note: extensions/ad_hoc/notes/20260913-092100-prefer-installed-skills.md (cwd=C:\Users\PC\.codex\skills; rollout_path=not available; updated_at=2026-09-13; extension-derived evidence)

### keywords

- prioritize suitable installed skills, C:\Users\PC\.codex\skills, grill-me, grilling, mattpocock/skills, plan/design interviews

## User preferences

- When beginning future work, the user explicitly instructed to prioritize suitable installed skills -> inspect the installed-skill catalog first and use a skill when it genuinely fits the task; do not invoke an unrelated skill merely because it is installed. [Task 1]

## Reusable knowledge

- `grill-me` and its companion `grilling`, installed from `mattpocock/skills` under `C:\Users\PC\.codex\skills\skills\productivity\`, support user-requested plan/design interviews. Their presence does not require grilling for every task. [Task 1]
- Read a selected skill's instructions before applying it. Existing user instructions and authorization boundaries remain controlling. [Task 1]

## Failures and how to do differently

- Symptom: a task is routed through an irrelevant interview or workflow skill -> cause: treating installation as an instruction to invoke the skill -> fix: first assess fit to the user's request; skip unrelated skills and proceed under the user's current authorization. [Task 1]

# Task Group: ANSYS microchannel Fluent project storage, archive, and Workbench cases

scope: Future ANSYS Workbench/Meshing/Fluent microchannel runs: storage locations, reproducible milestone archives, multi-case Workbench layout, and solver launch defaults. This block is based on authoritative ad-hoc notes, not rollout summaries.
applies_to: cwd=D:\Codex\2026-09-11\x and D:\Codex\Microchannel_Fluent_Archive; reuse_rule=reuse for the user's future microchannel ANSYS/Fluent work unless a later live license check or explicit user direction supersedes a path, archive convention, or solver setting.

## Task 1: Preserve the microchannel simulation data location and archive convention

### rollout_summary_files

- No rollout summary on disk; authoritative extension notes: extensions/ad_hoc/notes/20260912-0825-save-simulation-data-on-d-drive.md and extensions/ad_hoc/notes/20260912-0840-microchannel-version-archive.md (cwd=D:\Codex\2026-09-11\x; rollout_path=not available; updated_at=2026-09-12; extension-derived evidence)

### keywords

- D:\Codex\2026-09-11\x, D:\Codex\2026-09-11\x\outputs, D:\Codex\Microchannel_Fluent_Archive, V1_, README.md, 00_References, ANSYS Workbench, Fluent case/data

## Task 2: Configure multi-case Workbench systems and Fluent launch defaults

### rollout_summary_files

- No rollout summary on disk; authoritative extension note: extensions/ad_hoc/notes/20260912-0900-workbench-multicase-fluent-launch.md (cwd=D:\Codex\2026-09-11\x; rollout_path=not available; updated_at=2026-09-12; extension-derived evidence)

### keywords

- shared Geometry, ANSYS Meshing, independently named Fluent systems, 3D double precision, 4 solver processes, Workbench Setup, Solution cells, CFD-Post, .cas.h5, .dat.h5

## User preferences

- For future microchannel simulations, the user explicitly requested that “ANSYS Workbench, Meshing, Fluent case/data, reports, and related simulation artifacts be saved on the D drive going forward” -> use `D:\Codex\2026-09-11\x` as the primary project root and `D:\Codex\2026-09-11\x\outputs` for final artifacts; use the C-drive Codex workspace only for a temporary compatibility file required by the active desktop task. [Task 1]
- The microchannel archive is rooted at `D:\Codex\Microchannel_Fluent_Archive` -> retain reproducible milestones as sequential `V1_...`, `V2_...`, `V3_...` folders and keep common literature/parameter evidence in `00_References`. [Task 1]
- For different flow rates, heat fluxes, or other boundary-condition cases, use one shared Geometry and ANSYS Meshing upstream in Workbench, then branch into independently named Fluent systems. [Task 2]

## Reusable knowledge

- Each archive version folder must have a `README.md` covering purpose, boundary conditions, changes from the prior version, results, file layout, and unresolved limitations. Do not retain failed launches, wrong-boundary cases, transient video-frame caches, or other disposable intermediates in this archive. [Task 1]
- The saved Workbench project must contain Fluent setup and solution state, rather than only standalone `.cas.h5` and `.dat.h5` files outside Workbench. [Task 2]
- Launch Fluent in 3D double precision with the highest effective local process count allowed by the installed license. The observed limit is 4-way parallel, so use 4 solver processes unless a later live check confirms a higher limit. Ensure Workbench Setup and Solution cells are updated/saved; update Results through Fluent/CFD-Post when a completed Results cell is required. [Task 2]

## Failures and how to do differently

- Symptom: a run is saved only as external `.cas.h5`/`.dat.h5` files or the Workbench system appears incomplete -> cause: Fluent setup/solution and cell states were not saved/updated in Workbench -> fix: save the Fluent state in the Workbench project, update Setup and Solution, and use Fluent/CFD-Post to update Results when needed. [Task 2]
- Symptom: archive contains clutter or cannot explain a milestone -> cause: disposable intermediates were retained or the version folder lacks a complete `README.md` -> fix: keep only reproducible milestones in sequential `V...` folders, document the required fields, and place shared evidence in `00_References`. [Task 1]
