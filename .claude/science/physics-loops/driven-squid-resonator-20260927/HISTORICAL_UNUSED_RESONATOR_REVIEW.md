# Independent unused-resonator review

The stored prediction freeze is intact, the 20 reserved columns are disjoint from the 22 calibration columns, and the two largest residuals survive independent direct charge–photon diagonalization. No consequential numerical error or state-label ambiguity was found at those two points. This supports the stated **conditional retrospective unused-center comparison**, not a statistical exclusion or a demonstrated physical readout prediction.

## Separation, extraction and units

I read the protocol, prediction/freezing script and manifest, extraction/comparison script and outputs, full-cavity script/helper and output, original calibration-column extractor, and necessary response helpers. The frozen manifest validates against all five listed current files, including the fitted candidates. The extraction script asserts these hashes before fitting. This preserves the declared prediction-before-extraction workflow at the source level and current identities; hashes alone are not an independently timestamped proof of historical execution order.

The zero-based reserved indices are 10,30,...,390 (20 columns). Calibration indices are 0,20,...,400 plus197 (22 columns). Their intersection is empty. “Column50” means zero-based array index50, hence spreadsheet column51 if counting from one. The original extraction smooths only each column's frequency vector for initialization and fits that column's unsmoothed data. It performs no flux smoothing and does not mix these reserved columns into calibration centers. Shared-map viewing and retrospective protocol selection remain disclosed limitations, not a blind holdout.

Predictions use fixed driven-calibration EC,J,asymmetry,G,offset and fixed Ω; no reserved center is read into that calculation. The measurement extraction objective uses only measured column values and shape/background parameters, not model predictions. Its reads of frozen predictions occur after the fits for comparison. Full-cavity evaluation is explicitly subsequent to extraction, with unchanged parameters; it is a numerical refinement, not a newly blind prediction freeze.

The source mesh spans −.2000000000004221 to .8799999999995478 in steps .02000000000013108. Under the recorded MHz ordinate convention, dividing by1000 correctly produces GHz shifts; multiplying GHz residuals by1e6 correctly produces kHz. These are frequency **offsets**, not absolute frequencies near7.69GHz. The fitted reference offset is included once. The archived published Fig.3 caption confirms spectroscopy around7.6918GHz but does not independently establish that scalar as the bare frequency. A fresh attempt to open the publisher figure and image failed during this check; the numeric workbook axes themselves do not encode a unit label. Thus the arithmetic conversion is verified conditional on the existing MHz-axis provenance, rather than a fresh visual verification of the original printed axis label. Do not upgrade the reference's physical status on this basis.

All40 shape fits report success and no active parameter bounds. The maximum Gaussian-versus-Lorentzian center difference is2.641536834kHz. Both use the same data, initialization and background family; this is a limited shape sensitivity, not a confidence bound. The20kHz source frequency grid step is likewise not a center uncertainty; sub-grid centers rely on the supplied line-shape interpolation. I did not independently reoptimize the measured line fits or test a broader extraction family.

## Independent full-cavity reconstruction

Preserved independent_unused_resonator_check.py constructs the scalar potential with phase quadrature, then diagonalizes a direct charge⊗photon Hamiltonian. It uses GnP; the author's undriven GnX construction is phase-equivalent. Both use n rather than n−ng in the interaction. The ng-dependent charging term is retained for both branches. Bare device-ground⊗zero/one-photon overlaps independently select distinct ground and cavity states. Charge/photon cutoffs (24,7) and (30,9) were computed. No author model or diagonalization helper is imported, and no parameter fit is run. Frozen parameters and measured center values are shared inputs, and author outputs were visible beforehand.

At the larger cutoff:

| ng | Zero-based column | Full shift (GHz), before offset | Residual after offset (kHz) | Cavity overlap weight |
|---|---:|---:|---:|---:|
|0|50|.000451916827143073|+108.148909088|.999273632|
|0|250|.000360796514816464|+114.806629917|.995118798|
|.5|50|.000451450693693012|+108.518609581|.999262128|
|.5|250|.000365594801467140|+120.440750511|.994831112|

The largest difference from the author's same physical full-cavity shifts at these four points is .000151Hz. Ground/cavity eigenvalue indices are(0,2) at column50 and(0,4) at column250; this change is expected from intervening device levels, not an off-by-one label error. Full numerical details and both cutoff runs are preserved in independent_unused_resonator_results.json. These are floating consistency controls, not rigorous infinite-domain enclosures.

## Near-resonance and interpretation

At column50, the nearest bare device transition is level2: cavity detuning −26.24MHz (ng0) or−25.57MHz (ng.5), with G|n02|/|detuning|≈.0207. At column250 the nearby level3 transition has detuning+30.43MHz or+29.69MHz and ratio≈.0726 or.0748. These are nearby poles of the perturbative formula, but the checked points are not singular. The full-cavity labels remain dominant and unique. The ground-state full-versus-perturbative correction is about−1.06kHz at column50 and−7.47/−7.93kHz at column250. It reduces, but does not remove, the large residuals. No ambiguity of these numerical labels explains the discrepancy.

The saved full-cavity RMS values over all20 columns are36.4528 and37.2351kHz, versus ground perturbative37.8060 and38.6883kHz. My independent diagonalization covers columns50/250 for both charge branches; the remaining points and full-sweep RMS are inspected author output, not a separate independent reconstruction. The preserved arithmetic and source review support their interpretation only at that scope.

A high overlap establishes a label within the supplied ground-state model, not experimental state preparation. Near-resonance sensitivity can amplify uncertainty in device parameters, reference frequency and assignment; no covariance or calibrated measurement error model is supplied. Moreover a cavity eigenenergy difference need not equal an observed mixed-state/dissipative signal extremum. The quoted residuals must retain those qualifications. The25mK calculation is a supplied canonical preparation alternative, not measured device temperature; its physical validity and thermal readout response were outside this review. Neither branch nor temperature was refitted or selected here.

No author source or other checkout was modified. Only this report and independent evidence were written.

## SHA-256 identities

- `UNUSED_RESONATOR_PROTOCOL.md`: `9d4893050f1d4d672448e9ce7ed6cb8ab6d483e261b2d79d8ed7156609d749db`

- `unused_resonator_predictions.py`: `13c3609f31adf93ba714be0a3123be8ed743d20beb46fb3db032dddc2547e03e`

- `unused_resonator_predictions.json`: `443238dce952a63af58637e81641e46c7cb3016e2a95215b817765abc872a540`

- `FROZEN_UNUSED_RESONATOR_PREDICTIONS.json`: `eb609a75d2b9777625c38c2498ee6dd678f7906244453baf1f3a37154947ea42`

- `unused_resonator_extract.py`: `807c4558b91673f4b40c443cc2e70fdfac89af15ab941788c9cfbc3ee75bec58`

- `unused_resonator_observations.json`: `72c17b6bc6bb867c0b4ff0d8fa40d4c7688892a8d38121e172d8ba101f672b9b`

- `unused_resonator_comparison.json`: `2690918503ad1e5126053d40e1839bbca16a2ee4f654e00ba5d1b104930d242e`

- `unused_resonator_full.py`: `6007c2aa04aed96a3dbed5bfd361ceedb28c743e3f009fd64b161e7c1c152edf`

- `unused_resonator_full.json`: `4922587f042c098fb4817ef056cb81329877253b5c8ddb2e41e5ce03f9880d42`

- `check_resonator_cavity.py`: `453545bcdf1d76abd7e8d36d6de8f748cb4e0850dd5d4ad677e32518ea7969e6`

- `thermal_resonator_probe.py`: `e73a8d39eb0a2a363e2dae4716e8cc05c847bd26a60336bfb6152681b54929c7`

- `extract_resonator_ridge.py`: `812505ed51d8a4ae705ab8b438e61291c36d9030eb67e3e30e4a8b2929282030`

- `resonator_ridge.json`: `ba85c89b104d8a7de8fb9091b1a7a14f42999cacbd245b4db102f8a4f4928318`

- `resonator_maps.npz`: `ee1e9b4cb7322d2fba09427db72c17a6c53e3b1f5fbb8cccdad387e0ca1ffb5f`

- `RESONATOR_MAP_PROVENANCE.json`: `e61b66841b55f1a2f6f8bd1b8c360cdfdccfbeedc9354367dbb293015ef52121`

- `source-figure3.xlsx`: `68abbfae73aec3b91ccd6e140cc48cc3cd62e951624efd30283796c9bcd8a303`

- `published-figure3-page.html`: `52b46e0e66beb99522bee9690a29352964260ba3931f69cf2a9d53f3cdc78b76`

- `driven_calibration.json`: `d93abfbda4c1f7af00d06a04bccf2b219df361f384dd99605b5f58e431e0ae64`

- `far_fit_exploratory.json`: `cf8f416eba6cd3e646e8bd5557ebd10f58f644968ffae6f10ee2e0e1c0dd3815`

- `independent_unused_resonator_check.py`: `f273e95a1a3155f4dc545849cd7b55f7114fa385025c07f3e07fd6ec246903af`

- `independent_unused_resonator_results.json`: `3ea5c220f93db9659e418e970cc93ebebec28c2a3aadc6e5fc43003934a3133a`

- `independent_unused_resonator_check.log`: `3ea5c220f93db9659e418e970cc93ebebec28c2a3aadc6e5fc43003934a3133a`
