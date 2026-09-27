# Portable preparation-transfer implementation handoff

Author implementation, not independent scientific validation. Only assigned primary/data paths were written in the publication checkout; independent helper is the source agent's implementation. No note/pack/git/PR/pipeline/cache actions. Parent confirmed Echo outputs for integration before target import. This supersedes the initial Ramsey-only execution logs; old logs preserved.

Primary: scripts/preparation_transfer_2026_09_27.py. All scientific/runtime data are under data/preparation_transfer_2026_09_27; helper is explicitly imported and declared. Literal AUDIT_INPUT_PATHS covers all included input files; AUDIT_TIMEOUT_SEC=600. No HDF5 dependency, network, external absolute-path runtime read, or optimizer run. Historical author scripts are inert .txt evidence; their original freeze receipts describe the earlier external workflow, not a fresh prospective experiment. Provenance pins upstream NPZ/source HDF identities, copied source protocols, rates, original frozen predictions/evaluations and DOI https://doi.org/10.5281/zenodo.10728469.

Compact NPZ files copy raw_IQ, stored time and gate axes verbatim from calibration_readout.npz, target_observations.npz and echo/target_observations.npz. No precomputed population arrays enter the portable science. Boolean genuine masks are indices<197/<380/<246; references are the final three stored records, source-defined and checked. No clipping. All three full-rate and three sequential returns survive; calibration cost alone defines each original selected start. All twelve Echo swap/no-swap curves survive.

Primary reconstructs affine readout and stable closed-form populations. Imported helper independently uses QR readout and SI-second matrix exponentials at all calibration/Ramsey/Echo times for every applicable return, plus zero/degenerate/swap toy controls. Saved costs, whole frozen curves and descriptive residual arithmetic are regression anchors, explicitly not empirical-proximity success thresholds. Full calibration is 36,051 correlated population coordinates; Ramsey is 11,780 Pexc comparisons per return; Echo is 15,006 per curve.

The output preserves Ramsey RMS about1.6593pp(full)/1.6735pp(sequential), no-decay5.1642pp, AND Echo failure: full swap about15.851pp versus no-swap13.387pp, sequential swap16.255pp. No target fit, rescaling, chosen factor-of-two conversion or model selection by this comparison. Markov/preparation/stationarity/instantaneous-pulse/readout/total-delay assumptions remain conditional; classical population equations give the same results. No coherence/native-TOE/no-go/measurement-precision claim. Optimizer messages/optimalities/Jacobian singular values are supplied, not independently regenerated.

Verification: primary executed with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 and PYTHONHASHSEED=1,913: both exit0,224 numerical/integrity checks, exact stdout bytes identical. All six --mutation identity|units|initialprep|readout|membership|swap runs exit1 at natural failed checks. These are full raw logs, not runner caches: portable_final_seed1.log, portable_final_seed913.log, portable_final_<mutation>.log; PORTABLE_CHECKS.json records outcomes. Stdout SHA256 5e2a3df58c7a28a9e785720ec43ad097f2ee71ac20a570b19115d231f76881e8. Primary source fully reread after Echo integration; runtime passed. Final-source independent review, source rate/pulse interpretation closure, note/pack integration and mechanical gates remain parent responsibilities. No final cache created.

Reproduce from checkout root: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/preparation_transfer_2026_09_27.py`; append `--mutation <family>` for expected nonzero controls.

## Exact source identities

- `scripts/preparation_transfer_2026_09_27.py`: `436445c0a6e7b7cc0980e90e8b3339abf252732ee070b8850ffab7aecaf31616`
- `scripts/preparation_transfer_independent_2026_09_27.py`: `bce339d01716f2b66f28033fda48f8e301279cafffe6efaf79763b40888e5aa8`
- `data/preparation_transfer_2026_09_27/CALIBRATION_INPUTS.json`: `0f946dea6e3703caa139f723097543fe715e517d4b8fa42b2024480f0f131a1e`
- `data/preparation_transfer_2026_09_27/FROZEN_TARGET_PREDICTIONS.json`: `8c553e09364b31b609d1ae4eeea1bce40976cff97fc4ee7f7eddeb565c9d0ada`
- `data/preparation_transfer_2026_09_27/NO_DECAY_CONTROL.json`: `449895e8828bb3dc95df679bf146d6b91d2250b4edd5ebbcb9f4ff0e36e8951d`
- `data/preparation_transfer_2026_09_27/PREDICTION_FREEZE.json`: `32c15912a752e9b01d3f88aeea123d0329f39782f3adf8be58b1d36638faac3c`
- `data/preparation_transfer_2026_09_27/PROTOCOL.md`: `266dd151a66f6ff32e68cc7e27a7945b33243383b208d2f01cf87f10f09e0c2a`
- `data/preparation_transfer_2026_09_27/SEQUENTIAL_CONTROL_INPUTS.json`: `4059d9891249c8ccd2155fe65ed8948a34fb24e602487bc0f222d672719549b8`
- `data/preparation_transfer_2026_09_27/SEQUENTIAL_CONTROL_PROTOCOL.md`: `27dc3e0d360a5a2d971670da492d7bb2d03a757b9c7586b5ff93cf47eb629dcb`
- `data/preparation_transfer_2026_09_27/SEQUENTIAL_EVALUATION.json`: `d4416c779fd56ff0ec1c8f6969b1409c309dcb075c5ecdfd43d23cd94867a70d`
- `data/preparation_transfer_2026_09_27/SEQUENTIAL_FROZEN_PREDICTIONS.json`: `d071e4452f1ff5b5457f123c06513d2f034f1a2db6275d305c21c8a2891b2cd9`
- `data/preparation_transfer_2026_09_27/SEQUENTIAL_PREDICTION_FREEZE.json`: `d079df7cba8d873ede58faec6e6affe3f6d4511f63c716d6369ce3771dc290eb`
- `data/preparation_transfer_2026_09_27/SOURCE_ELIGIBILITY.json`: `fddd57b7f96d660eb4cf702b661f15d179aa305b6b808362def7e703efe4a9c2`
- `data/preparation_transfer_2026_09_27/SOURCE_ELIGIBILITY.md`: `4be8a24840229c2b918d547a8ecbc0d789d2a3b5e3e9849a71df97497e02b0c5`
- `data/preparation_transfer_2026_09_27/SOURCE_IDENTITIES.json`: `891747e3ae3a2184efbdab5e1f309428bb305072dfe863ebe58e9272545ec324`
- `data/preparation_transfer_2026_09_27/TARGET_ACCESS_RELEASE.json`: `84a0720d8c56dbb014488a5986f8c7e843178fc762146ef8250988812e12e144`
- `data/preparation_transfer_2026_09_27/calibration_fits.json`: `0f288cb27f611627ea8e93e8bdbd6c7f49853ec8277a964095739b06208731c4`
- `data/preparation_transfer_2026_09_27/calibration_raw.npz`: `fec875c2159324ac9c00ff4185305d79fa3533609d99953827bf6745ad67b740`
- `data/preparation_transfer_2026_09_27/echo_FROZEN_PREDICTIONS.json`: `79ebaf70e119f046bca6277a3d412040a5362c8d0b187f2302ac9d980862895d`
- `data/preparation_transfer_2026_09_27/echo_PREDICTION_FREEZE.json`: `5dd773d59c04a6157e16dbbe1b9f833793c1eca32c4e9e62d7e1635c351ce573`
- `data/preparation_transfer_2026_09_27/echo_PROTOCOL.md`: `310284303c2fbec736d2b0713e8115cbaeb550f68211b1e162cc006a54201eb0`
- `data/preparation_transfer_2026_09_27/echo_SOURCE_ELIGIBILITY.json`: `92010cb66e515b4e93a7e275882fb85c5dc7baf4c5e9bac0c851cc2431c1066e`
- `data/preparation_transfer_2026_09_27/echo_SOURCE_ELIGIBILITY.md`: `32e6a598dd4b81f19c6fc025863b4ddf15c9fc67e76d3fd325cf0c75eab8361c`
- `data/preparation_transfer_2026_09_27/echo_SOURCE_IDENTITIES.json`: `98d89d668d170a620af5f394362dff5044b9a0a167aee3bc3692f7bbea8478f0`
- `data/preparation_transfer_2026_09_27/echo_TARGET_ACCESS_RELEASE.json`: `64e1bec34f6c303a94620e7ce9f334fe8d317708d204d533e2367a9f65fe15a6`
- `data/preparation_transfer_2026_09_27/echo_evaluation.json`: `881a59e1821cba7e1a437d48174e38817726d4009ce2f27268f9ac31f49612ad`
- `data/preparation_transfer_2026_09_27/echo_raw.npz`: `fa38ac8b685cfc54bc8da685885ea2ea760a895d182159a265b3e84a39d3f0f8`
- `data/preparation_transfer_2026_09_27/evaluation.json`: `d4e04739275b20e94fd5c246e835bb1a59b1eb7420a53d9d2357c02e16b7e45d`
- `data/preparation_transfer_2026_09_27/historical_calibrate_and_freeze.txt`: `1ce03afda05c3c03fcf8607bafdf93f2f875f009e8d11d9b501ea780b8b30bd6`
- `data/preparation_transfer_2026_09_27/historical_echo_evaluate_frozen.txt`: `90b47fc34ee331a2d7045062122d05f11aa2bb5121c95ead53b3ffe9f2e80b6d`
- `data/preparation_transfer_2026_09_27/historical_echo_freeze_predictions.txt`: `5aad02df6e0424de6d2626317525b9eb9fd3be0a8e80dcff02d3be6dbb0bf84f`
- `data/preparation_transfer_2026_09_27/historical_evaluate_frozen.txt`: `7d942aa90a7a1f0c032bc0fe2fc6569b499739c7783615657a24883ce7a5ba9f`
- `data/preparation_transfer_2026_09_27/historical_sequential_control.txt`: `ca701a5cd31298ded93f73b31cb4d222c34f59c3cd106953a1778687830dc25c`
- `data/preparation_transfer_2026_09_27/provenance.json`: `2775422eac8bf64bddb794e005c089bd456da17c64b103f353b021709eefbb0c`
- `data/preparation_transfer_2026_09_27/ramsey_raw.npz`: `94d8b1d44f6cc7e7ea960e6947a9831f8190c8dfd1d80d5e90a3f45ec309bbc8`
- `data/preparation_transfer_2026_09_27/sequential_control_fits.json`: `9e2a8aa1348ea346fc8b6ccd11928f3ace3870d6d1e38792ee5d8cdeea30f0d6`
