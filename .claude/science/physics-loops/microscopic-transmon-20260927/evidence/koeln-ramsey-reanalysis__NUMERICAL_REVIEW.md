# Independent raw-Ramsey residual review

2026-09-27. Bounded reconstruction of all three saved raw-calibration fits. Read complete protocol, source CODE_REVIEW.md, fitter and manifest. No author import, nonlinear optimizer, spectroscopy/03 target read, or model-selection-by-higher-target agreement. No consequential residual, unit-conversion, projection, or sign defect was found in the checked calculation.

## Independent reconstruction

The script reads the original HDF5 x0/x1/y0/y1, lexicographically sorts gate and delay, and reconstructs the 31×267×2 array independently of the fitter's grouping loop. Every saved time/gate coordinate matches. All 16,554 normalized residual entries per fit are recomputed from its 66 nonlinear parameters and 31 sets of 5×2 linear coefficients; the complete arrays are retained in independent_residual_arrays.npz. The manifest and raw-file hashes match.

Unlike the fitter's MHz/µs trigonometric expressions, reconstruction uses Hz/seconds complex exponentials. For each branch, transition=reference+c*1e6±split*1e6*cos(...)/2 and oscillation=artificial+reference−transition. The real/imaginary parts of exp[(-1/T2+i2pi*oscillation)t] yield the damped cosine/sine design. Thus the detuning sign, 2pi, time conversion and full-splitting factor are correct. The observed oscillation ranges in these saved fits are approximately1.517–1.628MHz; no crossing through zero occurs. This verifies the declared convention, while the independent source review remains the dependency establishing the instrument's reference/artificial-detuning interpretation.

A separate reduced-QR least-squares projection checks the saved coefficients, rather than repeating the author's SVD-based lstsq. The maximum relative normal-equation defect ||Aᵀ(Ac−y)||/(||A|| ||y||) is7.59e−13. The largest saved-vs-QR reconstructed signal difference is1.50e−7 in raw ordinate units, negligible relative to the residual RMS below. Maximum per-gate RMS discrepancy is9.17e−10 raw units and maximum condition-number discrepancy is9.37e−9. Tiny differences include roundoff from forming transition frequencies around5.24GHz before subtraction, whereas the author evaluates detunings directly. These differences do not affect any conclusion here.

| Initial period (V) | Returned period (V) | Center (Hz) | Full splitting (Hz) | Reconstructed cost | Raw RMS |
|---|---:|---:|---:|---:|---:|
| 0.15 | 0.139883500 | 5241117888.938410 | 57633.708827 | 7.116222647984 | 365.684337 |
| 0.22 | 0.216409412 | 5241114370.692266 | 110010.059408 | 6.689207149983 | 354.543003 |
| 0.3 | 0.214475489 | 5241114788.554434 | 110154.482197 | 6.680081116212 | 354.301070 |

Maximum absolute discrepancy from the saved half-squared normalized residual cost is4.24e−12. HDF5 labels the ordinates as volts, but their numerical ranges are approximately I1652…11654 and Q−20809…−15550. RMS is reported in the stored raw ordinate units without claiming a calibrated physical voltage scale. The single global standard deviation rescales both channels and all times; this is not a per-sample noise model or chi-square.

## What the preference establishes

Within this declared phenomenological residual objective and these three returned solutions, starts.22 and.30 yield lower raw residual cost than start.15. The lowest saved cost is the.30-start return, followed closely by.22; their centers differ by about418Hz, while their periods and fitted decay patterns differ. This is raw-calibration-only preference among saved candidates, not proof of the true charge period, a global optimum, statistical confidence, or validation of either earlier source pipeline. Branch exchange/phase ambiguity and arbitrary channel/branch sine/cosine coefficients remain as described in CODE_REVIEW.md.

All three terminate by ftol, with reported optimalities.003160,.001377,.000882, above the declared gtol1e−6. Thus cost termination must not be described as satisfying the gradient tolerance. The.30-start solution has a decay approximately49.999586µs near the50µs upper bound. Maximum design condition numbers are120.54,17.61,13.00 respectively; these selected endpoint matrices have full rank, but finite conditioning at returned points does not establish smoothness through branch coalescence or uncertainty control. Independent QR confirms the linear projection only; the nonlinear search, its finite-difference Jacobian and basin completeness were not reproduced.

The model assumes one stationary sinusoidal gate map, a common center, two exponential decays per gate and time-independent per-channel offsets. Flexible I/Q coefficients are not a derivation of parity preparation/readout. Drift, hysteresis, nonexponential decay, additional components and correlated instrument errors remain possible model limitations. This check concerns measurement extraction, not the underlying quantum theory or higher-level transfer performance.

## Evidence identities

`independent_residual_check.py`, its log, JSON diagnostics and full compressed residual arrays are retained beside this report. No author files were modified. SHA-256:

- `PROTOCOL.md`: `18ad028a3c7e28e237329ddc0adcacf64795171e51e409a20047066b252fb127`
- `CODE_REVIEW.md`: `2b679278db92e2788d86e6ef736371dea27f698fef32065a673ae3faad8b709f`
- `INPUTS.json`: `1f39d242da12b60d6cf80068f95616ec4bb6a874e9af3887525728b63cbd6179`
- `fit_raw.py`: `9b475e7e88395cd2cfcdfdc9905bc306718272a6ad442639e3d8338a6665f259`
- `fits.json`: `4bab159078275824642eec59d4ce02415438419fedeed62f82795eeb64c1b5eb`
- `independent_residual_check.py`: `b904e7010ac8819dfb8db5c2975d2a52102b99296c5ef14b2eb4fc77954f9a39`
- `independent_residual_arrays.npz`: `df9262efcb973303191995b30c8391dc8179bec249aa31aad0a63f0f6087f3af`
- `../koeln-energy-addition/source/Krause2024_Quasiparticle/Data/quantify_datasets/20220729/20220729-074423-596-6dd5d0-Ramsey oscillation 01 vs Gate at 5.2411 GHz/dataset.hdf5`: `b48d9620e77a4eb0d47550ea405531908ca9514525c022df6d99ebba4c31e6cc`
- `independent_residual_results.json`: `e1e6a15764d9a8c100e68146a78ba16c6b558323e4485f49ad26cf48f5f89d86`
- `independent_residual_check.log`: `37dc1844581121bdcc55873f3a4c934e2450a2429ef15d460f3214b0c4e5d322`
