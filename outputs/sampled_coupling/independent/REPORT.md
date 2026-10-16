# Focused final-source integration check

PASS within the explicitly conditional passive clamped-response and anchored inverse class. No material mathematical or helper/source mismatch found. This is a focused final-source check, not an audit verdict, empirical validation, complete repository integration review or shared landing gate.

## Complete source binding

Read the complete integrated note, complete primary runner, complete normally imported helper and complete primary cache. Exact hashes frozen before checking:

- docs/SAMPLED_COUPLING_RECONSTRUCTION_NOTE_2026-10-16.md: 6e28e5afcba4c2557570ae2527c71f9ed1cf5a947c20005fa00e3f345c5da0e5
- scripts/sampled_coupling_inverse.py: 500e86a6e7df075b785aafc9946965da70a20da4c70d0f1328eb0af4df4a8c20
- scripts/sampled_coupling_math.py: 0d27f68e63d050de220e9b7b984429733ae8bcab9bcb6d68736dee28328ef6af
- logs/runner-cache/sampled_coupling_inverse.txt: dff97ceb18267c504d7f74e979bbaf416b2315eb3fef2a01aad20e02907099cd

The integrated source was checked directly rather than inheriting a prior PASS. It preserves the sampled recurrence, corrected p derivative, increasing-limits shape-error bound, parent pulse factorization and reciprocal-potential theorem. The primary imports exactly the checked helper and records both note/helper integrity inputs. The entire mathematical argument is supplied in the note; historical campaign outputs and external references are not executable or logical proof dependencies. The prior-art read claims and external sources were not independently re-investigated here.

## Proof and interaction check

A held-coordinate force has constant affine oscillator forcing. Its augmented sampled map has characteristic polynomial (z-1)(z²-sz+p), so the displayed recurrence and first-difference Cramer inverse hold even for repeated/Jordan poles. Measured rank and conditioning are required. The three pre-pulse samples propagate the same-run baseline forward, while the three settled post-pulse samples propagate actual regular force backward through positive p. Their difference removes arbitrary hidden homogeneous preparation without requiring identical starts across trials. The two endpoint readings have the correct left/right-limit conventions; force impulses, hidden derivative coupling and unsettled readout remain excluded. Small p is explicitly unstable for noisy inversion.

Variation of constants gives D=-J a(x)[b(y)-b(x)]/tau. The homogeneous displacement solution with initial (1,0) obeys dissipating positive energy, so J=(1-z(Delta))/Omega2 is nonnegative, strictly positive under positive damping, and zero only at undamped complete periods. A nonzero anchor therefore selects positive J in the admitted class without choosing a continuous frequency branch. This says nothing about positivity at arbitrary late lags; the source retains that restriction. Critical/overdamped and aliased underdamped regimes are genuinely included, whereas rank-degenerate data remain inconclusive.

Column subtraction gives E=-J a(x)[b(y)-b(z0)]/tau and normalizes A,B by the nonzero anchor. The surface converse additionally uses D(x,x)=0 and the definition of E; it is not a complete realization theorem. Finite samples cannot fix nonpolynomial continuum shapes or count hidden modes. The algebra is valid for C1 nonpolynomial couplings, including zeros away from the anchor.

Mixed potential derivatives require a=lambda b-prime in the positive constant-diagonal-mass completion. Constructing U and V proves sufficiency only for the stated force core; damping is Rayleigh dissipation and the moving-coordinate kinetic law/global stability remain separate. The normalized shape relation gives lambda=a_r/(d kappa), with E0*kappa=-J a_r²/(tau lambda). This proves the sign criterion without assuming a_r,d positive. Independent tests deliberately use a negative anchor-row coupling and a zero of a. Common positive gain preserves the condition; arbitrary setting-dependent or unknown-sign gain does not. No physical action is selected.

The six-sample force bound is exactly the sum of absolute linear weights. The calibration bound is a square-system Neumann inverse estimate, not a universal least-squares guarantee. The corrected derivative includes -s F2/p², and the coefficient bound requires the entire uncertainty segment to retain p>=pmin and |s|<=S. Ratio error requires a certified nonzero-anchor margin. Shape error uses nonnegative segment integrals while the signal integral remains oriented. The integrated pulse-shape discussion correctly requires propagation of errors at the actual six observation times, rather than substituting a later force into the pulse-end formula. Uncertain time, pulses, parameters, gain and model drift remain separate obligations.

## Helper and execution evidence

check.py probes the actual final helper against independent expressions: nonpolynomial normalized surfaces, positive/negative lambda, a zero of feedback coupling, elementary critical/overdamped/oscillatory calibration bases, all 32 correlated sample-error corners in each regime, symbolic gradients, ratio corners, reversed-endpoint shape errors and sharp six-weight read noise. It checks ten invalid finite-domain inverse/bound inputs raise. These routines are finite-input algebra helpers; exact nonzero-anchor and nonsingular guards do not by themselves certify conditioning, continuum rank-one structure or a valid physical oscillator. The source explicitly requires those further checks, and response_surface correctly returns diagnostics even for a nonfactorized comparison matrix.

135 independent assertions passed. Full primary output reproduced exactly against the frozen cache, including all 44 controls, version metadata and source integrity hashes. No computational failure or timeout occurred. Both independent computation and primary subprocess were bounded to 120 seconds; commands, cwd, elapsed times and return codes are preserved in check_receipt.json and reproduction_receipt.json. Full stdout/stderr and results.json are adjacent. Python bytecode writes were disabled. All frozen source/cache hashes were rechecked unchanged.

No author source, git/PR state or audit authority was modified. Scratch mutations, publication metadata, repository-wide source preservation and combined landing validation are outside this report until separately inspected. Synthetic controls do not establish a physical coordinate/force bridge, a measured coupling, absolute hidden scales, quantum records or a gravitational action.
