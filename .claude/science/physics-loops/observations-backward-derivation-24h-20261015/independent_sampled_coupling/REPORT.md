# Focused sampled-coupling inverse check

PASS within the stated passive single-response class and identifiable sampled-data contract. No new material mathematical or code-source defect found. Complete v2 note and correction note were read, independent derivation saved before code inspection, and complete runner/output then read. The parent v2 inverse is the identical same-session checked source; its calibration/anchoring restrictions remain in force. Exact frozen binding:

- SAMPLED_COUPLING_INVERSE_v2.md: f353fa17d30ae96e286d12379b5393daefae58816198323c12001de65251b2f7
- check_sampled_coupling_inverse_v2.py: 7305a8f7daef0d7598bdd288b4e6f4298e6c708e91250a0628f329ce25a95823
- SAMPLED_COUPLING_CONTROLS_v2.json: 1301bf184592aba51a55f9cfaa9203b01711866940a6ece03e05ccb701f8114b
- SAMPLED_COUPLING_CORRECTION_v1.md: f43f5b1d1e30be898de953a2281f8d37e66ebf4962fea5d0a20aff26a2d338c1
- COUPLING_RECONSTRUCTION_v2.md: 42498cb335c85568c2358981f8563e9958f8994c61adcf6562cc1fcff9d7c909

## Decisive conclusions

Cayley-Hamilton on the affine sampled state proves the third-order force recurrence and second-order difference recurrence, including Jordan/repeated poles. The two-row determinant and Cramer formulas have the correct signs. Three pre-pulse and three settled post-pulse samples determine the baseline and backward-extrapolated regular pulse-end force for p>0. They do not require a common hidden preparation between runs. The pre-time-zero sample must be a left-limit clamp reading and the reconstructed pulse-end force a right-limit regular clamp reading; derivative impulses and unsettled instruments remain excluded.

The energy proof establishes nonnegative J_end for every positive stiffness and nonnegative damping, strictly positive for positive damping and any positive duration. Undamped full-period pulses can vanish. Continuous frequency aliases preserve sampled coefficients but do not determine the step magnitude; nonzero anchor plus the assumed passive class suffices for its positive sign. A late-time force cannot replace extrapolated pulse end in that argument. Neither a fitted recurrence nor nonzero anchor proves the actual passive class.

Arbitrary C1 nonpolynomial coupling functions are covered mathematically: the temporal recurrence depends only on constant-clamp values, and the parent normalized shape/converse does not impose a polynomial. Independent checks use a=b/constant proportional to exp(q), not a polynomial. Finite grid measurements still cannot determine a continuum function without additional regularity/approximation control. The unknown overall J/tau scale and hidden normalization remain unresolved.

Critical and overdamped regimes are covered both by the general proof and actual controls. Independent checks use elementary homogeneous bases and numerical IVP integration rather than the author's augmented matrix exponentials. Repeated discrete poles do not invalidate Cayley-Hamilton. Degenerate sample ranks are not invertible: steady, single-exponential or aliased records can fail even when the pulse response is nonzero. An independent undamped half-period example has rank one and positive J_end. The note correctly labels rank failure inconclusive and requires measured rank/conditioning margins; there is no universal inverse for every initial state.

The measurement norm, calibration Neumann bound and corrected coefficient-error bound are valid under their stated denominator/segment constraints. The v2 p derivative correctly includes -s*F2/p² and yields (2+2S)/pmin². The mean-value argument requires p>=pmin and |s|<=S on the full interpolation segment. Combining coefficient error on true bounded samples with force error at estimated coefficients is legitimate. Uncertain timing, pulse shape, model drift and physical force sign are not included. The original v1 control failures remain separately bound in v1_failure_binding.json; the symbolic-structure comparison issue and genuine sensitivity-term omission were corrected, not erased.

## Independent evidence

275 assertions passed: analytic sampled-basis recurrence checks, six-sample reconstruction from direct piecewise IVPs in undamped/critical/overdamped regimes with nonpolynomial couplings, positive pulse integrals, degenerate half-period rank, and all 64 force-sign corners with four coefficient-error corners. The full author v2 JSON reproduced exactly, including versions: 33 passing controls, zero failures. Actual commands, 120-second subprocess bounds, elapsed times and return codes are preserved in check_receipt.json and reproduction_receipt.json; full stdout/stderr and results are adjacent. No independent failure or timeout occurred. All frozen sources were rehashed unchanged.

These are exact derivations and synthetic numerical checks, not empirical validation, framework premise adoption, unique continuous-frequency identification or a complete action derivation. No author sources, canonical files, git/PR state or audit authority were changed, and no network was used.
