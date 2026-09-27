# Publication source and empirical-scope review

Scoped source-review outcome: **PASS for the supplied-snapshot empirical scope below**. No material source-lineage or empirical-claim defect remains in the reviewed note, runner and three data files. This is not an audit verdict, a calibration-optimizer verification, or independent proof of every mathematical/numerical result. The numerical reviewer owns the current implementation's decisive dynamical checks.

Reviewed base: `e37967e326c2bdb429bd3106d34158bd5420e9c0`; candidate branch `physics-loop/driven-squid-resonator-20260927`. Complete scientific note and runner were read; the JSON inputs/provenance were read completely and every measured signal/coordinate entry was checked against the exact prior reviewed source. Hashes below bind this coverage to the current candidate bytes.

## Measured lineage and prior-review reuse

The packaged frequency-offset axis is exactly equal to the prior `resonator_maps.npz` Fig.3f y axis, and every one of the twenty packaged 55-point signal columns and flux values is exactly equal to its corresponding original map column. The prior independent source review had reopened the author workbook and established exact equality of the entire data/x/y arrays. Its source workbook hash is unchanged (`68abbfae73aec3b91ccd6e140cc48cc3cd62e951624efd30283796c9bcd8a303`), and every available historical hash in current provenance matches. This permits reuse of the exact-source extraction review rather than repeating the same raw-slice checks.

The package contains genuine measured digitizer signal columns, not author theoretical curves or previously fitted center values. Column indices 10,30,...,390 are disjoint from the supplied 22 calibration indices. The reader is told these are interleaved measurements in an already viewed sweep, not blinded or statistically independent observations.

The published figure identifies MHz offsets from 7.6918 GHz. The runner's division by 1000 converts offsets to GHz correctly. The source-axis reference remains distinct from independently knowing the bare resonator frequency; the note explicitly preserves that caveat.

The earlier source review's outlier finding still applies: columns 50/250 have real dominant measured troughs close to the fitted centers. Two symmetric templates agree on their descriptive locations but do not eliminate unresolved mixtures or establish a microscopic single-transition label. The candidate keeps their large residuals, preparation/readout uncertainty and lack of statistical significance visible. No known source counterexample is suppressed.

## Supplied snapshots and empirical honesty

All two driven snapshots exactly match projections of the corresponding historical calibration rows, all six alignment snapshots exactly match historical rows, and the drive-reference snapshot matches a historical resonator-fit row. Thus the package neither invents parameters nor silently substitutes a refit. The current runner propagates these supplied snapshots; its numerical comparison is reproducible without claiming that it reconstructs the optimization or its exclusion history.

The note clearly states that raw calibration reconstruction, optimizer verification and parameter covariance are outside the packet. That is a valid narrowed scope. A later user wishing to validate calibration itself would need its raw calibration data, extraction and optimizer; no such validation should be inferred from executing this runner.

The six relative-axis alternatives use an older undriven calibration objective and were explored after observing evaluation discrepancies. Those facts are disclosed, and all six are propagated rather than selecting the best evaluation result. Their altered residuals are assumption sensitivity, not corrected predictions with independent empirical status.

The Rabi pulse settings are source measurements/settings, while the drive normalization uses this model's matrix element. The source-author derived 860 MHz amplitude is not imported as independent data. Finite-domain numerical anchors are named regression references, not experimental targets or proofs of general error bounds.

## Self-containment and current execution evidence

The scientific execution closure is the runner plus `inputs.json`, `measurements.json` and `provenance.json`, with ordinary NumPy/SciPy dependencies. There is no runtime import of another PR, local exploratory script, raw workbook, historical calibration output, or gitignored audit result. The declared input files and hash reads are accurate.

Both packaged scientific input hashes match. The paired current output `independent_publication_runner.json` gives nominal RMS values 36.452834893/37.235061957 kHz, shape-center sensitivity and both Floquet sizes as described. I inspected its structure and claim-relevant summaries for the source/scope conclusions, but did not independently rerun its eigensolver: another current reviewer supplied execution, and historical independent source evidence was reused only at matching identities.

The short module docstring says “no empirical fit” although the runner does fit empirical line shapes. The body and note repeatedly clarify “no calibration refit” and expressly describe the measurement-center fits, so this is a minor wording issue, not a material ambiguity in the scientific claim. Prefer “no circuit-parameter refit” when editing that header next.

The exact oscillator-displacement claim and its finite-basis implementation have a separate mathematical/numerical review boundary. This source review checks that they are not presented as proving preparation, dissipative readout or a framework-native prediction. The note passes that boundary: canonical rotor/oscillator dynamics, geometry and fitted circuit inputs remain imports; no framework axiom is changed or credited for deriving them.

## Remaining limits

No confidence intervals, calibrated experimental error budget, unique mechanism identification, all-model exclusion or native TOE confirmation follow. Same-sweep common errors and unknown state populations remain. The supplied review output is source readiness for this narrowly conditional artifact only; current-main integration and any later independent audit remain separate.

No editable prompts, skills, author source files or audit statuses were modified by this review.

## Source hashes

```text
444a419264f234435ff95ffb6668c58a0f51013fb2469c24b757993a0b6febff  docs/DRIVEN_SQUID_RESONATOR_COMPARISON_OPEN_GATE_NOTE_2026-09-27.md
27da3ab028375f10aa3c78549e5a6607917a70eabb894ff6620ca64153ad9c28  scripts/driven_squid_resonator_2026_09_27.py
baf26b54105765b5c3833f668a74273247df1cb13c06d016f1d9b0c4a4022bbc  data/driven_squid_resonator_2026_09_27/inputs.json
678a41d986c92b925b9f0661575c9ed0ec5c282558a6ed3db48102df80189e99  data/driven_squid_resonator_2026_09_27/measurements.json
92734babc2ae0840ecc74ca21991fd25b4e2943c28a7d281a4a3ca29f2bde712  data/driven_squid_resonator_2026_09_27/provenance.json
784f166e79dc447de840be6b9cbf7aef0525d08ca16257af984125102a66ba16  .claude/science/physics-loops/driven-squid-resonator-20260927/independent_publication_runner.json
```
