# Author sequential-channel control

Post hoc author computation,2026-09-27. The parent had already evaluated the target; this control author did not read any target amplitude, population, I/Q or evaluation output. Protocol/code/input manifest were frozen before fitting. All sequential target predictions were frozen before comparison. Original three-rate sources and freeze are unchanged.

Same61×197×3 calibration population objective, fixed initial|2>, equal raw weights, no clipping/offset/preparation fitting. Setting k20=0 leaves fitted k10,k21. All three declared starts return success=true by ftol with no active bounds. Results are preserved without target-driven selection:

| Start | k10 (/µs) | k21 (/µs) | Cost | Optimality |
|---|---:|---:|---:|---:|
| [0.05, 0.1] | 0.077281345236 | 0.117629252779 | 18.772920956380 | 0.00476563 |
| [0.2, 0.2] | 0.077281346561 | 0.117629256196 | 18.772920956379 | 0.00284211 |
| [1, 0.1] | 0.077281347325 | 0.117629250826 | 18.772920956381 | 0.00493373 |

Minimum calibration cost is the[.2,.2] start, by numerical-scale differences. All three prediction arrays are retained for all380 frozen target times and apply to all31 gates. The target times/gates were read only from the original frozen prediction file. Predictions assume initialhalf1/half2 and within12-pulse invariance of Pexc. Target observations were not accessed and no target residual was computed.

Calibration population RMS is.03227173136, versus the original three-rate.03151154765; cost18.77292095638 versus17.89891836386. This descriptive change includes matched recalibration, not removal of a channel at fixed rates. It is not a likelihood-ratio test, statistical evidence that direct2→0 decay is necessary, or exclusion of all sequential preparation/readout models. Shared source/reference/preparation/stationarity conditions and equal-channel weighting limitations persist.

New2-parameter Jacobian singular values are approximately387.752 and188.097, condition2.06145 in the declared inverse-microsecond parameter coordinates. Existing three-rate singular values are approximately542.668,209.591,109.102, condition4.97397. All three returns of each model are recorded in SEQUENTIAL_IDENTIFICATION.json; no parameter units are changed. These indicate local numerical sensitivity at the supplied solutions, not global identifiability or calibrated rate errors. Full-model optimalities remain.000219… .001566; sequential.002842… .004934, all above gtol1e−10 despite ftol termination. Start agreement is not an uncertainty interval.

Stable closed-form predictions were author-crosschecked with a separate3×3 population-generator exponential at every calibration/target time for each sequential return; maximum discrepancy is below2e−14. This is an author formula check, not independent audit coverage. No nonlinear fit after target access and no optimizer retuning were performed.

Evidence: sequential_control.py/log; SEQUENTIAL_CONTROL_PROTOCOL.md/INPUTS.json; sequential_control_fits.json; SEQUENTIAL_FROZEN_PREDICTIONS.json; SEQUENTIAL_IDENTIFICATION.json; SEQUENTIAL_PREDICTION_FREEZE.json. Exact SHA-256:

- `SEQUENTIAL_CONTROL_PROTOCOL.md`: `27dc3e0d360a5a2d971670da492d7bb2d03a757b9c7586b5ff93cf47eb629dcb`
- `sequential_control.py`: `ca701a5cd31298ded93f73b31cb4d222c34f59c3cd106953a1778687830dc25c`
- `SEQUENTIAL_CONTROL_INPUTS.json`: `4059d9891249c8ccd2155fe65ed8948a34fb24e602487bc0f222d672719549b8`
- `sequential_control_fits.json`: `9e2a8aa1348ea346fc8b6ccd11928f3ace3870d6d1e38792ee5d8cdeea30f0d6`
- `SEQUENTIAL_FROZEN_PREDICTIONS.json`: `d071e4452f1ff5b5457f123c06513d2f034f1a2db6275d305c21c8a2891b2cd9`
- `SEQUENTIAL_IDENTIFICATION.json`: `11d2519b9e42023fdaf12bb5a4d0f3c3839b9aa9dea71509e473c7c68509111f`
- `SEQUENTIAL_PREDICTION_FREEZE.json`: `d079df7cba8d873ede58faec6e6affe3f6d4511f63c716d6369ce3771dc290eb`
- `sequential_control.log`: `37371b379de2d4abf4f323d5ab228a8b3b4c2b7ac668c5b0fbb1ca4e29c5c216`
