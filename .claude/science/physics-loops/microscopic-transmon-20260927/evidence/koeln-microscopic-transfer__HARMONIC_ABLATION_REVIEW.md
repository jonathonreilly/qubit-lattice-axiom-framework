# Harmonic-envelope ablation review

2026-09-27. Bounded independent code/control and selected forward-spectrum check. No author Hamiltonian import, optimizer reproduction, higher-target read/comparison, or target-dependent case selection. No consequential implementation discrepancy found.

The complete ablation protocol, calibrator and input freeze were read. A full diff against calibrate_raw_transfer.py shows exactly three changes: manifest filename, addition of field_harmonics=False to the forward call, and output filename. Bounds, initial parameters, absolute Jacobian steps, optimizer options, objective and calibration observations are unchanged. All frozen hashes match. The unchanged model.py identity agrees with the previous spatial-average review.

Independent keyset checks find exactly twelve unique (case,initial_tau) entries in each family: raw_period_0.15/.22/.3 times None/.01/.1/.4, with identical calibration vectors and identical fixed alpha/Omega/G/psi. All return success. This does not assert gradient convergence or global optimality. All three cosine controls match their spatial counterparts within0.000384Hz over the saved means/dispersions. At tau=0 only m=1 contributes apart from a removable constant, so equality is the correct analytic control.

The physical spatial average multiplies the mth local harmonic by signed sinc(mB/Bnode). The ablation multiplies the entire local arm potential by sinc(B/Bnode), preserving its zero-field harmonic ratios. This is precisely the declared replacement. Changing m=0 as well is immaterial because the primary removes the potential diagonal constant. Neither construction uses absolute values of the sinc envelopes. Phase pi produces odd-harmonic arm subtraction and even-harmonic addition.

## Independent endpoint reconstruction

For raw_period_0.3, shape start.01, both frozen parameter rows were preserved in independent_ablation_snapshot.json. This case was preselected for the check from the lowest saved raw Ramsey calibration cost, not from higher-level agreement. The independent script directly averages the raw short-channel potential over each rectangular arm for the spatial model; for the ablation it evaluates u(phi+phase)*sinc(B/Bnode). Both normalize the local zero-field first harmonic independently by phase quadrature. It then projects onto charge plane waves and constructs the full charge tensor photon Hamiltonian with G(n−q)(a+a†), without the primary's device-eigenbasis truncation.

Both q=0/.5 endpoints are checked at N22/K12/grid4096/spatial64 and N28/K16/grid16384/spatial128. The first-three zero-photon excited gaps are assigned by isolated-device overlaps, with unique labels [0,1,3,5] and minimum fine weight above0.998326. The largest fine-versus-primary discrepancy over means/full dispersions is0.001039Hz, and the largest independent cutoff change is0.000931Hz. These are selected floating-point controls, not certified error intervals.

| Model | Fine mean f03 (GHz) | Fine full δ03 (GHz) |
|---|---:|---:|
| spatial | 14.669413488160 | 0.038256331211 |
| ablation | 14.669606129898 | 0.038235227083 |

Ablation minus spatial after each model's low-level recalibration is **192.641738kHz** in full f03 mean and **-21.104128kHz** in full endpoint δ03. Neither number is divided by three; any three-photon drive ordinate needs that explicit conversion. No measured higher target has been compared here.

The attribution is to the envelope replacement **together with its recalibration on the same low-level observations**. It is not a fixed-parameter derivative, a unique explanation of an empirical residual, or independent confirmation of rectangular microscopic geometry. Shared tau, equal current density/area ratio, fixed phase pi, fixed field nodes, cavity transfer, and endpoint-mean observation assumptions remain conditional. Selecting an ablation by exposed higher targets and calling it a blind prediction would exceed this evidence.

## Evidence identities

Independent script, selected snapshots, full endpoint diagnostics/results and log are retained. independent_ablation_controls.json preserves the twelve-pair keyset/calibration/cosine controls. Source SHA-256:

- `HARMONIC_ABLATION_PROTOCOL.md`: `25e6fd73b2debf7af248f525b95b91ae53bec138767b1e8668836b15a410c89a`
- `calibrate_harmonic_ablation.py`: `5d60418877130fb927f3855526ab1a6ff5b55c597087155f226d4ba3ac13287e`
- `HARMONIC_ABLATION_INPUTS.json`: `e2651bce29e6b9dd3a484daa61a7522bf033b14dd95ed779944e5b14c4eda731`
- `calibrate_raw_transfer.py`: `1d6b3e9221966b71d6fab7eacdf8ccb0a15a65d0d946a6793565f89ac0f2707c`
- `raw_transfer_fits.json`: `5b25bc09c09331c1683e6cb4b2aa62fdecd45f52bc9e7864a04dbedf8a672491`
- `harmonic_ablation_fits.json`: `fca3770298f91ed7cc158c811fba8fe44c567bd2b946111187f44a72fe60ee9d`
- `model.py`: `d9db69aa06122958dc81120c1518ef2e3148a01dfd46a2f1820e0d593eac8cf3`
- `independent_ablation_check.py`: `80c80a6ae3fdced88490d3e7244b5d487a1af75f280cb74b3d2b16aad1d929ed`
- `independent_ablation_snapshot.json`: `dbc91336f89ee006113b5b4420eaca69d281a558c3a3fc2366026ed5e2508b8e`
- `independent_ablation_results.json`: `3e9df2e7e2067c8800cb3267f3689fcb081d4474f1c32d6e19461094e8f007ea`
- `independent_ablation_check.log`: `7b2629b6023a364309de18f6f21ea5d5567be83e3d1c4cb98841f76552a77fa5`
- `independent_ablation_controls.json`: `1a0307d1a49dd96ade872718cc76703153f59f3ec769226e38b51de7c8786eac`
