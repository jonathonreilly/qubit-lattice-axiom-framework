# Row 1111 serial GUIDE records

The scientific report is [gap-long-sheet-guide-astra.md](../../library/gap-long-sheet-guide-astra.md).
These computations guide or refute a numerical reading; they discharge no
proof step and grant no scientific status. No mass gap is claimed.

The source checkout is `2b67c749cc219d0051de7b26c2a62c77c3948266`.
The programs reuse row 1101's `su2_guarded.cpp` quaternion heat bath and
`analyze.py` jackknife/fit routines. Credit Creutz and Kennedy–Pendleton for
the updates, and Borisenko–Skala for the independent-sheet calibration.
The local model definitions come from `gap-bridge-vectors-max.md`,
L220–240 and L350–385. The report credits Sussman and Alpoge, with Claude
and Codex as authors of their text, for the bounded source readings.

* `gh_plan.json`, `p4_plan.json`, `face_plan.json`: couplings, sizes,
  starts, seeds, discarded cycles and record counts fixed before production.
* `sheets.cpp`: GH2 and P4 sampler, with E1/E4/E8/E16 and plaquette readouts.
* `face_sheets.cpp`: the same updates with E1/E8/E32/E64 readouts. This
  adaptation followed GH2 and preceded all face production.
* `batch.py`: serial process controller. It refreshes the machine lock,
  checks free memory, waits for each child exit, and hashes its records.
* `analyze.py`: fixed-window, binned-jackknife and autocorrelation analysis.
  `analyze_gh_frozen.py` and `analyze_p4_frozen.py` preserve the exact source
  versions hashed in those phases' analysis receipts.
* `verify.py`: separate complex-matrix evaluation of selected final
  configurations. This checks readouts, not equilibration or a theorem.
* Per-chain JSON and logs: arguments, timestamps, exit code, hashes and RSS.
  Small CSV copies hold energy/chi diagnostics and burn-in records.
* Per-phase summaries: selected and unresolved candidates, axis diagnostics
  and calibration. Full correlations, effective masses and rejected windows
  are in the hashed scratch detail files they name, with identical small
  `analysis_*.json` copies here. The manifest maps both locations.
* `manifest.json`: final inventory, source hashes, record locations,
  production-order verification and resource summary.
* `environment.json`, `record_checks.json`, `lock_release.json`: recorded
  software versions, packaging checks and the successful lock release.
  `artifact_inventory.json` hashes the final report and every packaged file
  except itself; its scope is packaging, not scientific verification.

Large raw observations and all configurations stay in
`/tmp/sa-gap-long-sheet-guide-astra.ioPBXO`. No raw record over 1 MB is
copied into this directory. Raw `.f32` layout is
`[sample, longitudinal_axis(0,1), channel(5), slice(L)]`, in native
little-endian float32. Each configuration is native float64 quaternions,
field-major with site index `x+L*y`; GH2 finite-coupling gauge links follow
the two Higgs fields. At the frozen endpoint no gauge links are stored.
The `.csv` columns are energy, chi0 and chi1. The spin susceptibility ratio
is used as a published calibration only for independent sheets; finite-GH2
spin chi0/chi1 are gauge-dependent and are not used as physical observables.

The two timing pilots are excluded. Their hashes are in the manifest.
Downloads remain in scratch, including the separate Borisenko–Skala folder
`/tmp/sa-gap-long-skala.YIk2wV`. Papers are not repository artifacts.

Compilation used `clang++ -O3 -std=c++17`, with outputs `sheets` and
`face_sheets` in the scratch directory. Production used one heat-bath plus
four over-relaxation sweeps per cycle. All five thread variables
(`OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`,
`VECLIB_MAXIMUM_THREADS`, `NUMEXPR_NUM_THREADS`) were 1. Actual nice was 20;
setting 10 was denied. The samplers stop above 2 GB peak RSS.

Execution order was GH2 sampling, GH2 verification/analysis, P4 sampling,
P4 verification/analysis, face sampling, face verification/analysis. The
machine lock uses holder `gap-long-sheet-guide-astra-2b67c749c`. The pinned
checkout lacks `automation_lock.py`; the main version was copied to scratch
and supplied through `PYTHONPATH`, without editing a repository helper.

For a new run, use a fresh empty scratch directory and a fresh output
directory. Adjust the explicit scratch and holder constants in `batch.py`,
compile the two programs there, and acquire the machine numeric lock before
running a plan. Preserve the original receipts and do not run a successor
sampler or an analysis process until the preceding numeric process exits.
The current controller refuses to overwrite completed chain receipts.
