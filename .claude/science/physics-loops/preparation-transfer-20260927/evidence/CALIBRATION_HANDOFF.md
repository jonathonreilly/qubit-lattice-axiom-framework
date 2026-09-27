# Author calibration and prediction-freeze handoff

This is the explicitly authorized author computation, not an independent audit. Source eligibility was read before execution. Only calibration raw I/Q and target x0/x1 axes were accessed; target I/Q/populations and QOI/fitted parameters were not opened. Stop point: all predictions are frozen; no target evaluation performed.

All61 gates ×197 genuine T1 delays ×3 affine populations were fitted with fixed initial|2>, three canonical nonnegative downward rates, bounds0…10/us, no offset/rescaling/clipping. Raw reference indices197–199 are retained separately; source semantics are pinned in SOURCE_ELIGIBILITY.md/json. All target predictions cover380 genuine times, apply shared rates to all31 target gates and use initialhalf|1>/half|2>. A final ideal within12 unitary preserves Pexc; cross-acquisition stationarity, preparation/reference fidelity and pulse loss remain conditional.

Three declared starts return success=true by ftol, all with cost17.89891836386 and population RMS.03151154765. Selected lowest cost is start[1,.1,1], with rates[k10,k21,k20]=[.07126916243144915,.11124121007542162,.008397699651499876]/us. Costs differ only at numerical precision; all three outcomes and all three full target predictions remain preserved. No target information participates in choosing the minimum. Optimalities.0004565,.0015662,.0002195 exceed gtol1e−10, so no gradient-convergence claim. No active bounds. Supplied Jacobian singular values are approximately542.668,209.591,109.102, much better separated locally than the earlier shared-Pexc-only fit, but not a global identifiability or uncertainty proof.

The author check compares the stable divided-difference formulas with a separate3×3 population-generator exponential at every calibration and target time for each rate return. Maximum difference1.163e−14. This is explicitly an author numerical check, not independent reviewer certification. Equal weights across all three populations are a defined least-squares objective, not independent noise channels; affine populations sum to1 and share reference covariance. The finite rate domain and source/preparation assumptions remain open empirical conditions.

Artifacts: calibrate_and_freeze.py; CALIBRATION_INPUTS.json (created before execution); calibration_readout.npz (raw reference data, populations and membership); calibration_fits.json (all outcomes/status/Jacobian singular values); AUTHOR_FORMULA_CHECK.json; FROZEN_TARGET_PREDICTIONS.json (all three full arrays); PREDICTION_FREEZE.json (exact snapshot hashes, target_signal_access=false); calibration.log. Existing upstream source files were not modified.

Exact output hashes:

- `calibrate_and_freeze.py`: `1ce03afda05c3c03fcf8607bafdf93f2f875f009e8d11d9b501ea780b8b30bd6`
- `CALIBRATION_INPUTS.json`: `0f946dea6e3703caa139f723097543fe715e517d4b8fa42b2024480f0f131a1e`
- `calibration_readout.npz`: `23295ed8ed45ca24bac0dca882390d4cd7b5af746969a8a80875b6b1eb1092d9`
- `calibration_fits.json`: `0f288cb27f611627ea8e93e8bdbd6c7f49853ec8277a964095739b06208731c4`
- `AUTHOR_FORMULA_CHECK.json`: `313971f69182ec10547bc39354b4309d9c4d840c5abdb30e4462faf684c26899`
- `FROZEN_TARGET_PREDICTIONS.json`: `8c553e09364b31b609d1ae4eeea1bce40976cff97fc4ee7f7eddeb565c9d0ada`
- `PREDICTION_FREEZE.json`: `32c15912a752e9b01d3f88aeea123d0329f39782f3adf8be58b1d36638faac3c`
- `calibration.log`: `8752c3accc85ba5c3d9f32d1339556904b2d3d65cdaf21e624bd31a554f05223`
