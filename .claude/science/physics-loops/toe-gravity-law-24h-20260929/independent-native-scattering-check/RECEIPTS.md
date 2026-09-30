# Check receipt and reproduction

The precomparison was frozen at 2026-09-30T02:32:46.825006+00:00 before the author report, evidence or code was opened. Its hash remains `8ae4360ee69515a82b326af3a8ce576c5dd102cfff8ae9af900743f9d0e95574`. `PRECOMPARISON_BINDINGS.json` records the contract/operator inputs and the independence state. The later author report and evidence were read completely; no author implementation was read, imported or executed.

One sparse standard-library job was priced before launch at <=30 CPU seconds, <=120 wall seconds and <=150 MB. It ran once:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-native-scattering-check/check_occupations.py
```

It exited zero with no failed assertion. Python measured 6.8731107919011265 wall seconds, 6.768210999999999 CPU seconds and 33,292,288 bytes peak RSS. Tool wall time including startup was 8.6663515 seconds. The script installs a 30-second soft CPU limit and tests its wall bound during the core traversal. Its complete scientific output is preserved in `results.json`.

Deadline and STOP_REQUESTED were checked before work and at entry, with additional sentinel checks during the traversal. Deadline remains 2026-09-30T22:41:00.557005+00:00. No heavy job, dense torus or inverse matrix, unmanaged worker, source edit, commit or external mutation was used. Ordinary source hashing/binding is separate read-only bookkeeping, not a second mathematical compute job.

All physical-action coefficients are integer pairs `(mu,tau)` divided by twelve. The code first chooses an occupied unordered pair, reconstructs every actual local Q representation, applies each onsite or shifted pair term with hard-core exclusion, and accumulates literal occupation outputs. It does not assume pair-boson relations. Its momentum checks use integer Gaussian phases at quarter-period momenta; these are exact infinite-lattice Fourier evaluations, not aliased four-site torus calculations.

The job independently checks the abstract diagonal gap, all connected core shapes, the free collision hole and its physical image, the complete nine-component pair symbol, the two literal transition witnesses, the incoming E-channel defect, the closed-output norm and all physical core support/count claims. It did not recompute the previously checked bare quartic coefficient, evaluate a threshold Brillouin integral or invert S0/G_II. It did not compare the author's unpublished coefficient array entrywise or match its serialization digest. Reported counts and small expected values were known from the author proof when the independent code was written; the mathematical precomparison was already frozen.

All source hashes requested at freeze matched. The original author packet was unchanged during this check and required no correction. The final report specifies the limits of the threshold form and does not confer formal review/audit authority.
