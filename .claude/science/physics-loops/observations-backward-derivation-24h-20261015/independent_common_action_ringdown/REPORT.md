# Independent common-action ringdown check

No material mathematical or implementation defect found in the declared single quadratic hidden-mode, reciprocal kinetic/Rayleigh class. This is a focused conditional mathematics/code check, not an empirical validation, novelty certification, formal audit or publication approval.

## Binding and execution

Complete note read and independent derivation recorded in derivation_before_code.md before reading the full runner. Complete published controls subsequently read. Final rehash confirms the following exact sources unchanged:

- COMMON_ACTION_RINGDOWN_v1.md: `61c46a1ae94f20de40fe0d8fd484f350ff9325bfd433afd0913f48a689685750`
- check_common_action_ringdown_v2.py: `b8123f4b9aa3da98a453d9cf43621d4830334f5051941d09716103ff9132fee8`
- COMMON_ACTION_RINGDOWN_CONTROLS_v2.json: `68c550d5fa4bb230e813d2b649f2a9f2108d7330693c0fa32541266eb46eda8c`

Independent check.py passed 268 checks; the author runner passed all 62 controls and its parsed complete JSON matched the frozen controls exactly. Full stdout and stderr, comparison and execution_receipts.json are retained. Both runs used Python -B and explicit 120-second subprocess limits. No computational failure occurred. The separately inspected v1/v2 diff is exactly simplification before testing residue free symbols; it changes symbolic bookkeeping rather than the residue identity. The diff command returned its normal difference exit status 1; author_v1_v2.diff preserves the difference. Historical author v1 evidence was not modified.

## Independent evidence

The held-force Euler-Lagrange derivation verifies the negative tau' velocity-square term, reciprocal G/nu/k cross operators, and h=tau O'|c|². The complex pole residue gives Kspec=|N(lambda)|²/tau; f=N(lambda)c then proves Kspec*h/|f|²=O'. The half factor relating f to real cosine/sine amplitudes is essential and correctly implemented. Degenerate zero O' is permitted and yields h=0; it does not require division by h.

Nine independent parameter sets cover negative, zero and positive O'. A separate matrix-exponential simulator generated force histories; a complex exponential least-squares fit extracted coefficients. Contour integration extracted residues without the author's rational-residue formula. A separate variable-projection rational fit recovered poles directly from synthetic frequency records. Output-only quadratic defects and cubic closure failures were independently reproduced. Positive and negative work-preserving affine coordinate/force scales were checked. Actual undamped basis rank loss and symbolic observable-pole cancellation supplement the author's brief exclusion controls.

Two hundred random correlated complex perturbations exercised both deterministic error envelopes with true-value bounds. The midpoint Lipschitz factor follows from integrating distance to a midpoint and is sharp for piecewise tent profiles. All error and covariance formulas agree with the derivation. Ordered integration bounds use positive interval widths; coordinate/timing/interpolation certificates remain separate obligations.

## Scope and practical limits

The implementation genuinely fits the monic quadratic dynamic-response denominator and quartic numerator from complex frequency data; it does not feed the extractor hidden generator parameters. It then fits the six force modes using the extracted pole. Three development and three distinct reserved synthetic environments/preparations are explicitly named. They share a chosen generator and a frozen extractor; this is numerical separation, not empirical validation or evidence that the class is uniquely selected.

The reported dynamic fit condition numbers span approximately 8,274 to 71,283; ringdown conditions are about 5.75 to 6.14. Successful noiseless fits do not certify finite-band/noisy pole identification. The note explicitly acknowledges this. Neither the extraction code nor these tests supplies a general robust estimator or missing uncertainty certificate. The synthetic extractor is not a production guarded API for blind or out-of-class inputs.

The mathematical exclusions matter: Gamma>0 and omega>0, isolated observable pole N(lambda)!=0, nonzero ringdown excitation, and a calibrated rest-equilibrium dynamic stiffness (force/displacement). Arbitrary ringdown initial state is eliminated only in the ratio; it does not remove the separate rest-state requirement of the linear probe. Near zero damping, cancellation or small f makes extraction ill-conditioned. More modes, nonlinear hidden kinetics/restoring forces, external hidden drives, uncertain readout distortion and environment-dependent clocks are outside the exact statement.

Common reciprocal structure is assumed, not inferred from a single successful identity. Quadratic output distortion can violate the relation with unchanged linear response; cubic output changes full closure while leaving the selected exact coefficients unchanged. Finite observations or this one identity do not prove sufficiency. Physical normalization, generalized-force calibration and prior-art/novelty boundaries are stated honestly. External prior-art papers were not re-reviewed in this narrow local mathematical check.
