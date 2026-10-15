# Focused initial-phase and chirped-operator correction confirmation

This addendum records a narrow correction check by `/root/orbit_inverse_check`. It is not a formal audit, landing review, retained-status decision, empirical acceptance, or a new review of author runner code. Scientific authorship remains with `/root`. The earlier reports and counterexamples are preserved unchanged.

## Final correction and source comparison

The complete byte-level text diff from `INITIAL_PHASE_ELIMINATION_v2.md` to v3 changes only the paragraph qualifying the minimum-variance contrast. It now calls the solution a **minimum-variance unit-response, nuisance-annihilating contrast** and requires zero-mean remaining physical and count errors, or removal of their known means, before calling the estimator unbiased. It explicitly gives the counterexample epsilon = delta*s + xi with E[xi] = 0 and Cov(xi) = I. For a unit-response contrast h, E[h*epsilon] = delta even though the covariance is unchanged. This resolves the qualification finding recorded against v2. The constrained variance minimization, C = I projector formula, nuisance constraints, and deterministic error bounds are unchanged.

The complete diff from `CHIRPED_COHERENT_PHASE_OPERATOR_v2.md` to v3 changes only its dependency pointer from the initial-phase v2 note to v3. It changes no formula or physical hypothesis. The earlier complete reads of both v2 sources plus these complete narrow diffs provide the final v3 source confirmation; the v3 snapshots match the final author source bytes exactly.

No additional mathematical run was necessary for these prose/reference changes. The independently implemented earlier checks remain applicable to the unchanged formulas. The author's reported new distribution example and 198/41 author controls are not counted as independent coverage here: their runner sources have not been imported, read, or rerun in this check.

## Preserved independent evidence and findings

The plasma check recorded 4,007 correlated mathematical controls with zero failed controls. The initial-phase/chirp check recorded 1,281 correlated exact controls with zero failed controls. These are finite synthetic controls supplementing the analytic checks, not independent experimental samples or a universal proof by enumeration. The unbiasedness wording problem was found by separate reasoning and an exact eight-point probability counterexample; the successful 1,281 controls did not establish an unconditional unbiasedness claim.

The original findings remain visible in immutable evidence:

- Time-varying carrier normalization cannot convert raw phase counts to normalized phase differences without the initial phase. The plasma v2 note uses fixed reference units, the full physical B matrix, the complete initial-state term, and endpoint phase-error terms.
- An observed-data operator-error bound plus a count-error bound at nominal weights is not generally valid. Initial-phase v2 and v3 use the true-family decomposition and a uniform bound on the relevant true-family count weights. The original exact error-2 versus nominal-bound-1 counterexample remains preserved.
- Covariance does not imply zero error mean. The exact independent distribution has covariance I, contrast bias 3/7 and variance 1/2. Initial-phase v3 now supplies the necessary mean qualification.
- The chirped note now points to the corrected initial-phase derivation. The earlier draft's obsolete dependency is preserved in its snapshot.

The plasma report also explicitly states the domain needed for its translated-interval Lipschitz bound: a bound across translated pairs, or a derivative bound on their connecting hull. Separate within-interval derivative bounds on disjoint intervals would not suffice.

## Scientific coverage and surviving premises

The checked algebra includes G = r + W*q0; annihilating contrasts and the unrestricted linear-state converse; count-covariance propagation with the correlations induced by cumulative counts; exact-family initial-state elimination; the joint operator/count error decomposition; the two-uplink chirped matrix; its inverse row and determinant; its equal-uplink-frequency singularity; and the rank-at-most-two initial-phase dependence under the specified common two-chirp model.

Initial phase is eliminated only for admissible contrasts of a supplied exact operator family. It is not derived, set to zero, or shown bounded. A truncated nonlinear family requires control of its remainder multiplied by the initial phase. A rank bound for each known history alone does not supply one contrast valid over all uncertain histories. A known or calibrated signature outside the full nuisance span remains necessary for an amplitude estimate.

The physical premises remain conditional: weak cold unmagnetized plasma response, common appropriate retarded rays, local-frequency separability, coherent carrier ratios, correct station-clock mapping, usable fixed references, first-order phase/Taylor approximations, and controlled residuals. Near equality of physical uplink frequencies can make the inverse ill-conditioned; algebraic nonzero determinant is not a measured uniform error bound. Supplied positive-definite endpoint covariance is a distinct premise; covariance induced only by cumulative counts may be singular. The synthetic three-link operators are not a physical calibration of Cassini, and the previously exposed X/X product does not become three carrier channels because multiple ground stations occur.

This check opens no raw observations, ancillary products, or reserved tracks. It establishes no gravity fit, empirical scalar-theory acceptance, complete physical link model, or derivation of all remaining physical assumptions. New parent-reported archive metadata and unpublished canonical consolidation are outside this addendum.

## Exact identity binding

Paths below are relative to the campaign's `physical_link/` directory. Every hash was rechecked when writing this addendum; the earlier reports, programs, result records, and final source snapshots are unchanged.

| Path | SHA-256 |
| --- | --- |
| `FINITE_COUNT_PLASMA_DERIVATION_v2.md` | `0bcb450acf7c42251b02b18d67254f1e0797736ce58b2f6922d2845d54418d72` |
| `INITIAL_PHASE_ELIMINATION_v3.md` | `557d8a5d2b125ddcbd50c66192766498ea9b2bff56f09b3165ed954cfac04fae` |
| `CHIRPED_COHERENT_PHASE_OPERATOR_v3.md` | `3bf1e74cb7ac6d7d5a2baf5c1a3d9638a38236e7ad8002312d2198f9c6c02449` |
| `independent_v1/REVIEW_FINITE_COUNT_PLASMA_v2.md` | `9290eee04f5e237ffdf6b16df1c85b408b0c7ed4bee12d2982eb677b40a9b553` |
| `independent_v1/REVIEW_INITIAL_PHASE_AND_CHIRP_v2.md` | `6837157d2ded9977029151184e6f2cf548f5546872579b7e4f7e1292b8b653f8` |
| `independent_v1/independent_plasma_checks_v1.py` | `f68bfc1ac1fb35a32dad47883556f9998f4c3f08495bba721641a38dbb4bd3ff` |
| `independent_v1/PLASMA_INDEPENDENT_RESULTS_v1.json` | `a487190d88c5ead22b423d0377f18e076460d646bdc91bb42ac54a82495da19b` |
| `independent_v1/independent_initial_phase_chirp_v1.py` | `f60366b98fd9d91856c226ee1a6020b29e37c236525ed0870a4827eb28bebdd8` |
| `independent_v1/INITIAL_PHASE_CHIRP_INDEPENDENT_RESULTS_v1.json` | `e36a9d092ad84793e10305b5445b014e2ba02c5438ef939e62ef3e7f2c237082` |
| `independent_v1/unbiasedness_counterexample_v1.py` | `3066deb7188d7c7641fd9ba3aff455a0afb561f0d32b57d2263625947531a3cb` |
| `independent_v1/UNBIASEDNESS_COUNTEREXAMPLE_v1.json` | `66739cca4883067bda19febb679e9b37a946cdd6a97854b6b7e4192cbe25c31e` |

Recorded at 2026-10-14T23:53:15.366953+00:00.
