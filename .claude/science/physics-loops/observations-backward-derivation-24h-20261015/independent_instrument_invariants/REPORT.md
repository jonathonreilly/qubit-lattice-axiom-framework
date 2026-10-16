# Focused block11 independent check

PASS within the stated finite real linear-network assumptions. No material mathematical or implementation defect found. This is a source-bound independent check, not an audit verdict, empirical test, novelty determination, or apparatus validation.

Complete note read and independent derivation saved in derivation_before_code.md before reading author code. Complete runner and published control JSON then read. Exact frozen hashes:

- NETWORK_EVOLUTION_BLOCK11_v1.md: bf8cf17be938e5598f28a998089490976e6418a7a6089de8b371b3aa1cd0c2f2
- probe_instrument_invariants_v1.py: 931ffe69ac5dcbed771a59ce34458c81883867af8893fc935775b99cca0c803a
- INSTRUMENT_INVARIANTS_CONTROLS_v1.json: 96f96fdb9b5f72e7a184d3a7002168ec4c8307ac7e5e37108ff6affaddbf3b4e

The derivation confirms the fractional-linear composition and four-setting polynomial, including constant responses and repeated settings; deterministic correlated-error certificate; within-pair cancellation of homogeneous initial data; sharp energy-mismatch certificate; and exact polynomial-force convolution leading order and remainder. Prior block09/10 response and impulse results remain conditional inputs, checked previously and reconstructed in the preceding canonical report. No new framework axiom is inferred.

Useful four-setting tests need finite responses at all settings, distinct commands and nonconstant response. Their polynomial remains true but uninformative in degenerate cases. Arbitrary setting-specific calibration can manufacture agreement; even a common projective control calibration passes, so the test does not identify affine calibration or rank-one physics. Error radii and command precision remain externally certified. An instrument common across settings at each frequency does not provide a time-domain impulse-response calibration.

Preparation cancellation requires the same K, initial state, signed linear source and readout within a pair. States may differ between pairs. The mismatch bound assumes real readout and SPD K, as inherited from the finite real-network setup; for a complex readout the quadratic norm would need conjugation. It is not an estimator of unobserved energy. The bound includes zero mismatch and is attained with zero velocity mismatch and displacement proportional to K inverse times c.

The finite-pulse statement requires finite accessible d, admissible Ktheta and exactly f(t)=fr*t^r/r! on the stated causal interval. At fr=0 or theta=0 the displayed coefficient vanishes; an inaccessible direction gives identical responses and has no finite d. Additional forcing terms and instrument filtering require their own bounds. The cosh remainder follows monotonically from the impulse remainder under the positive convolution-weight bound, not from empirical fitting. No light-cone, detector-record, Born-law or microscopic-network conclusion follows.

Independent executable check.py uses a projective-graph determinant, a nonprojective counterexample, an exact anisotropic energy-bound saturator, and direct polynomial antiderivative sums rather than the author's beta-integral implementation. It reproduced the complete author JSON exactly: nine passing families. Total independent assertions: 47. Both outer calculation and runner had explicit 120-second subprocess limits; receipts record actual commands, elapsed times and return codes. All completed successfully; no failure or timeout occurred. Stdout and stderr are preserved. All frozen source hashes were rechecked unchanged. No canonical or author files were modified.

The note explicitly acknowledges cross-ratio prior art. This check verifies the mathematical identity directly; it does not claim independent inspection of the referenced metrology paper or its experiments. The open physical assumptions are accurately distinguished from the algebraically eliminated absolute calibration and zero-state requirements.
