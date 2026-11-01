# 正80%凸0.5/0.6/0.7：本轮用户请求的有限排队任务

用户2026-10-29要求补凸0.4—0.8中间案例。已按0.5、0.6、0.7三个单胞及基准流量500/1000共6工况准备。当前仅离线程序、参数和新目录；建模、网格和求解均尚未开始。详见新增凸曲率案例与比较方案.md、scope.json、cases.json。

正式盘当前为F，不能使用历史E路径。原始公共CAD只读，临时依赖修复发生在本任务私有stage；保护文件哈希有清单。原生C#编译通过仍不等于模型几何验收。

## 顺序与真实状态

1. Whole_StraightSaw_Diagnostics_20261028原有整条诊断继续。
2. FlowSweep_15_20_20261029原24工况继续，必须全部原生回写验收且控制器退出。
3. 本根orchestrate.py随后运行run_preprocessing.py：SolidWorks五体原生/独立引用/体积互补→共享拓扑→约4M流体加密网格→独立Fluent质量、正体积、heat/symmetry/域/界面检查→原Workbench双Setup保存重开。
4. prepare_solver.py仅在全部前处理凭据齐全后生成solve/jobs.json，复制对应的新500 native CASE。
5. solve/pipeline.py串行执行三例500→对应已验收500温启动1000，原生回写两分支并从原Solution重开。

只使用同一个native_solver_memory_slot；已有原生程序正在忙时不重复命令。新增queue是有限工作链，无新增周期automation。检查进度先读根progress/process.json；模型、网格和求解的实际状态在各子目录。出现异常保留匹配恢复场，禁止盲目重跑整个stage。

## 关键防误操作

- solve/worker.py从已验证P80_Derivatives1000 worker复制，只修正新映射案例的phase audit mesh路径为input_500.cas.h5，并加入Tmax漂移指标。
- warm_source的fluid.ip/solid.ip复用原线性正80%500原生导出，WARM_SOURCE_REUSED.json校验哈希；不重复启动Fluent导出。新网格不能读取旧DAT。
- 第二相插值沿用已验证的read_data('ok', filename)调用；检查全部T/P/U/V/W有限且映射热场、速度非零，物理/方法/控制不变。插值只是初值，不是收敛。
- SIMPLE、二阶、当前材料/入口/出口/温度梯度限制保留。第1/2/8齿和最宽90 μm保持，新建3/6不能擅自扩流量或新增几何切割。
- 保存必须完成命令、核对CASE/DAT和原生步数才可退出。末100及重开100、分相与外部守恒共同验收。1500保护步数未通过必须人工看真实趋势，不能硬宣布合格。
- 未写回场不清理。只有6份原Workbench native登记和原路径Solution重开字段/残差/网格来源全部一致，Setup/Solution实际/显示UpToDate才完成。
- 两个热负荷分别分析；优先看σA/Tmean/Δp折中以及热点真实坐标，不预设0.6最优。真实流体体积不等，必须报告。
- 不关闭用户程序。不使用未经批准computer use。不新增周期检查。


## 2026-10-30T10:43:39.938092+08:00 用户批准：写回同时提前三个案例前处理（优先于旧串行交接）
- P807/P808/P809即正80%凸0.5/0.6/0.7：三个实际CAD均完成五体体积/互补、独立部件引用、原F路径保存重开，CAD_ALL_ACCEPTED.json和三份installed_cad凭据齐全。原公共CAD哈希保护。旧build_error.json为10:25缺少part子目录依赖的旧失败，已经修复；parallel_cad2最新成功，23312已退出，任务专属SolidWorks已正常关闭。
- early_mesh_preprocessing.py有限进程已启动94636（以early_mesh_process.json创建时间为准），不启动Fluent、不占Fluent共享锁。当前P807已进入原生ANSYS Meshing生成，后续顺序P808/P809；每次新启动至少14GiB可用内存，Meshing两线程。
- 原始orchestrate.py仍等待前24工况原生交付，这只约束独立Fluent审计/工况赋予/求解；不再阻止上述纯CAD/Meshing提前处理。run_preprocessing.py已加入等待现有early_mesh凭据逻辑，之后跳过已完成CAD和原生网格，不重复生成。
- 网格生成/原生重开不等于验收：独立Fluent正体积、OQ>=.055、3.6-4.4M、五域流固、界面、完整heat/symmetry验收仍必需，且与旧登记共享同一Fluent内存槽。之后原生双Setup保存重开；全部前处理通过才做授权的基准流量500/1000。
- FlowSweep前24计算全通过，但原生写回在修复第一例登记。Single自动重开问题已通过固定Double解决，第一例T/P/U/V/W及全部残差数组逐项完全相同。随后Windows260字符复制限制在原工程交换前中断；当前修复仅复制/哈希使用扩展路径，旧incoming/rollback保留为.failed_in500_1038/.failed_rb500_1038，无源场丢失。当前delivery_resume_process/process及delivery_resume2日志权威，24812恢复。已有通过的Double stage用原receipt复用，仍重新比对源数组及所有安装门槛。
- 不启动第二份Fluent、不重复C#CAD/Workbench网格；已有加载、生成、复制、登记不得重叠命令。正式盘F，未交付恢复场保留。


### 2026-10-30T10:46:01.287782+08:00 Live parallel milestone
P807 convex0.5 native mesh and Mesh database reopen passed: 3759942 cells, native minimum orthogonal quality 0.2007787083; independent Fluent audit still pending, not final mesh acceptance. P808 waiting for 14GiB startup margin while original Solution reopen consumes RAM; P809 follows automatically. FlowSweep first500 Double fields/residuals, mesh and effective physics exact, installed to F; finalize_originals running, do not declare green yet. Existing automation-2 update returned Automation does not exist; no replacement automation created. Finite delivery and mesh controllers remain active.


## 2026-10-30T13:28:19.578067+08:00 500 all12 delivered; inherited1000 Mesh source repaired, queue resumed
All12 new-flow500 original native deliveries verified, ALL_500_NATIVE_REGISTERED exists. Original24 computation receipts remain complete. At12:27 first1000 verify_install correctly blocked FluentImportable MasterSources inherited from the baseline original FLU1; this was not a numerical failure or lost field. Independent native staging-only probe component.Reset->Mesh.TransferData->Mesh.Update passed, actual saved MasterSources exclusively SimulationGeneratedMesh, protected delivered500 branch all hashes unchanged. Root registration_precision_patch now injects native target-only connection repair before restoring accepted1000 settings/DAT, never reads CASE into Setup, no initialization/iterations; installer additionally verifies stage500 branch hashes BEFORE swapping original pair. First unconnected staging tokens/comparison retained under failed_independent_1000_link so fresh completion and exact source array comparisons are required. Current76708 delivery_resume3 process/logs authority; older delivery_resume2 error is resolved history.12/24 delivered as of this check, not yet1000 green. P807/P808/P809 all native meshes generated and saved/reopened (3.76M,3.75M,3.76M; OQ .201/.209/.203), independent Fluent/conditions wait same shared slot after24delivery. Old P80 rootprogress was stale: trust actual case receipts and early_mesh_state. No second Fluent, no source cleanup.


### 2026-10-30T13:30:06.017418+08:00 Idempotent native link repair resume
Current authoritative controller PID57416, delivery_resume4 logs/process creation;76708 delivery_resume3 stopped before Fluent because first probe had already created the mesh transfer, so attempting TransferData again correctly reported existing connection. Fix now reads actual staged object graph, binds target source to actual SYS Mesh GUID, and skips transfer only when that exact source already exists. Bad inherited branches still use native target Reset/TransferData/Mesh.Update in D staging before accepted settings/DAT restore. First case TARGET_LINK_STATE confirms sole SimulationGeneratedMesh with correct GUID, fresh NATIVE_TARGET_MESH_RELINKED and OPEN_STAGED_SETUP observed. No new source iterations or initialization.12 original500 deliveries complete;1000 exact fields and original green still pending. Older error files not authority.


## 2026-10-30T13:55:57.868102+08:00 User asks multi-case writeback: two offline lanes plus serialized native field
Authoritative controller73092/delivery_resume5; parallel_offline_preparation.py64940 two Python lanes, process creation records authoritative. Two laterG0 cases already offline-prepared, continuing remaining cases; no extra Fluent. Each phase has offline_preparation.lock, native prepare joins it and reuses only case/data hash-bound PREPARED. --offline-only exits before launch_fluent, native source audit/settings restoration still mandatory. This overlaps copy/numeric hash/finite fields with native writeback while preserving one large native field. Do not duplicate prepare jobs.
At13:41 previous delivery_resume4 stopped on Z0Q2p0x1000 exact raw mesh hash: source675102 nodes vs native675108, changed8 dataset representations, all cell field/residual arrays exact. Investigated full geometry:29zones exact oriented triangle corner coordinates, original cell0/cell1 IDs, all physical coordinate set with ZERO tolerance, geometric wall-shadow pair and owner cell match, other raw datasets identical. New audit_mesh_representation.py now additionally requires reciprocal shadows and correct target zones; current production proof passed. Only explicitly bounded representation differences allowed, never changed geometry or cell mapping. Installer first tries unchanged exact raw hash; mismatch requires full exact geometric cell/zone proof, saved MESH_REPRESENTATION_EXACT_PROOF and comparison method, not blanket hash suppression. Native source physics and500branch original/staging hashes still strict. First1000 case native delivered;second resumes cached exact source/stage under this independently verified proof. Continue original Solution readback, do not claim green before receipts. Current counts500=12,1000=1. All three P80 new native meshes generated, independent checks await shared slot.


## 2026-10-30T14:24:13.400158+08:00 Finite queue restart after unexplained process exits
At14:22 actual PIDs73092(native),64940(two offline lanes),26208 predecessor66620(curvature orchestrator) and their children had exited without traceback; no native Fluent/Workbench remained. Native receipts still13/24 (all12x500 plus first1000), offline6 later cases fully prepared. Z0Q2p0x1000 interrupted during incoming copy: original pair exists, no INSTALLED, rollback empty, so atomic swap had NOT begun. Retained incomplete incoming and empty rollback as .interrupted_in1000_1422/.interrupted_rb1000_1422 inside that same original folder. Pending offline staging directories with NO PREPARED receipt retained under interrupted_staging_1422, avoiding reuse of a partially copied project. No files deleted, no source fields modified, no physical solving/reinitialization. Recovery script resumed native99004 (delivery_resume6), offline10480(parallel_offline_resume1422), curvatureorchestrator26208(orchestrate_resume1422). Creation-time process records authoritative; existing locks and native gates unchanged. Currently active and no new error. Keep single native field, two offline lanes. Automation had previously been absent/deleted; no new scheduled task created.


## 2026-10-30T14:41:36.585192+08:00 User requests serial writeback again
SERIAL_WRITEBACK_ONLY.json now forbids any new parallel offline preparation. Previous two-lane offline work had already finished all10 pending-case preparations and exited at14:28; no live parallel job required termination. parallel_offline_preparation.py has a serial-policy startup guard; recovery launcher respects it and no longer restarts parallel lanes. Existing verified prepared copies retained and reused. Current native delivery controller99004 is already strictly one case at a time, and remains untouched: save/install/original Solution exact field and residual reopen before next case. Actual delivered now15/24 (50012 +10003), current G0uniformQ2x1000 prepare. Keep this serial policy in all future retries.


## 2026-10-30T14:45:33.169721+08:00 User authorizes deferring failed writebacks and moving to next
Keep strictly serial native delivery. SKIP_FAILED_CASE_POLICY.json and finite continue_after_case_failure.py supervisor88568 now monitor existing controller99004 without interrupting its active save/reopen. If a case fails, confirm owned children idle/exited, retain candidate/source/logs; only exact PID+creation captured descendants may be closed after180s grace, never unrelated user apps. Verify original pair exists or restore an unambiguously missing member from its exact rollback before continuing. Mark SKIPPED_WRITEBACK_BY_USER_POLICY with failure stage/evidence and accepted_delivery=false; PENDING_WRITEBACK_FAILURES lists all deferred cases. Generator now skips only explicitly deferred cases and preserves all other validation gates. After failure watcher restarts remaining serial queue (no parallel prep) and stops after finite pass. A pass with skips creates WRITEBACK_PASS_FINISHED_WITH_SKIPS, NOT COMPLETE, never green or all-delivered; new solve prerequisites stay unchanged until failed native deliveries reviewed. Current loaded controller retains old stop behavior, but supervisor takes over its exit and resumes others within same finite task. No current native command or source field modified by installing policy.
