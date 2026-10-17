# Larger-coupling scalar corroboration block — draft, unexecuted

Deliverables: `ARITHMETIC_BLOCK.py.txt` and this map. The text block is intended for insertion immediately before `check_arithmetic`'s return in the current canonical runner. It has four-space function-body indentation and uses the existing `F`, `lt`, `eq`, and local exact parameter variables J/E0. All new variables use `lc_`; original kap, T, geometry, historical checks and return metadata are untouched. Root may separately add larger-coupling metadata to the returned object. No import, compile, runner invocation, test, scientific computation or mutation run was performed here. In particular this draft has NO observed PASS count or execution receipt.

The only claimed purpose is corroborating scalar substitutions into separately checked analytical estimates. It cannot establish analyticity, root selection, physical reference planes, Green identities, positive spectral jump, completeness/synthesis, contour deformation, residual-spectrum accounting, or operator aggregation. Those remain source premises even if every row passes.

## Exact source identities

N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`; W is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree`.

| Source | SHA256 |
|---|---|
| N/LARGER_COUPLING_COMPOSITION.md | 3fd18e576fb394caea2b93272c4b430d782ec5c4663a9e961c8e3205d179952f |
| N/restricted_reference_moment/PROPOSAL.md | f76d55f9c51f582cf519bc025d5ae54e51d514023eaab7def6993c1cde782762 |
| N/restricted_reference_moment_check/REVIEW.md | e9ce634ae0b1981507e0e354ccc386c485fc1cbc5e4f0343fad7c7a439b6a686 |
| W/scripts/real_endpoint_autonomous_output_2026_10_17.py | cf1c78e122e0db0e5e3f1986c5f9ee8cdfe3b35453e26cd2e36b7b6851a8eb2a |
| W/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md, prior verified source | d3a48c35bf77a7ee5a084b949ff30573610282b97b88f3ad31bed3f5991894e9 |
| N/endpoint_background_regularity/PROPOSAL.md | 1229768dfdc065c6396a7f5d9ca0c8518f0862d8523a1dc9efed2ae9b3f6b64c |
| N/endpoint_background_regularity_check/REVIEW.md | c97208c7542cffffabc46f9445056332336126274d9d957fa7830be6c2538d77 |
| N/endpoint_coupling_interface_check/REVIEW.md | c89dbf5a567e4c2c38db93c3cc2ccba95456f0942073d94121ec87432594efc2 |
| N/endpoint_spectral_mass_check/REVIEW.md | eef72a0d61cb9ba79756fea1492aa507027a7b515b77e04c1230751cf47d4712 |
| N/complex_selfenergy_bridge/PROPOSAL.md | 0f627a4c3390ab007be46794b37a2daa21399dc61de7f23417e4082d2051e892 |
| N/complex_selfenergy_bridge_check/REVIEW.md | b46c9a561316415aac0d35344a4ada6ec0325c4fabef1e7f49a4e0fdf3c65c49 |
| N/schur_strip_interface/PROPOSAL.md | 16cc6ce85dd6bd40cf9ca6084274fd9b9d438134b39b35af21646a3af4f82a39 |
| N/schur_strip_interface_check/REVIEW.md | 11346d3c20ca4ae749b3c55750e8e0ec4144a9b4e9f82b3018c093f3a9516f18 |

The root composition and restricted proposal/check were read completely. The mass, background-regularity and coupling checks and complex bridge proposal were also read in full for this draft. Schur/source identities and derivations are reused from this reviewer's immediately preceding tasks. Table hashes explicitly read in this task or previously frozen are distinguished above where needed; integration must refresh all files before execution. The complex bridge check identity was freshly hashed, but its analytical conclusion was supplied by the composition rather than re-reviewed here. No W/Git/checkpoint/publication/prompt edits occurred.

## Check mapping and external premises

| Row prefix / group | Scalar content | Required analytical input not established by execution |
|---|---|---|
| `LC disk` | rho=1e-12; free gap .17; M16 Neumann inverse167; A/Tg derivatives; two-site response inverse2100; reflection and endpoint error constants | Exact free resolvent branches, M16 recurrence, physical two-site kernel and analytic disk continuation |
| `LC disk outgoing row squared` | sqrt(2)*41*(1+1.001)*exp(40rho)<130 | The review's added identity Tg_PP=Aopen*r_g*z²; extraction of the outgoing coefficient before taking a uniform off-axis norm |
| `LC disk reflected correction`, `endpoint correction` | 37/44 closed-power suppression and Cauchy scalar substitutions | Complete Pc Schur block, reference-plane distances and operator-valued Cauchy; a real-axis small value alone is insufficient |
| `LC background cancellation` through `regularity supplies` | H' four-term sum, phases42/90, R_bg'<12, g'<850, dG/dE<35000, ds/dE<36000 | Differentiation of the PRE-emitter half-sum, fixed projectors and full seven-coordinate product rule |
| `LC emitter`, `endpoint`, `real`, `outgoing`, `physical radius` | Positive onsite coefficients; restored diagonals; d_c<6; imaginary margin12kappa²; full-emitter factor; row floor; radius18 | Actual positive two-body installation, exact full Schur/Stone phases, local spectral synthesis at each positive coupling |
| `LC mass` and `actual/reference` | Inner cutoff d; comparison smallness; log argument<(8/3)^18; H<46; actual mass<4.85e-8; amplitude<.000221; reference deficit<4.54e-8 | Finite-interval exact density comparison lemma, normalized global actual/reference seed measures and no removed residual spectrum |
| `LC exponential rational lower proof` | 8/3<1+1+1/2+1/6+1/24=65/24 | Positive exponential series implies e>65/24. Monotonicity gives log(argument)<18. No transcendental function is evaluated |
| `LC bridge` | Disk scalar g<34, full norm<36, Cauchy oscillation<.000037, full Schur oscillation<.000038, resonant loss<6kappa² | Holomorphic G on every radius-rho disk, including endpoints; norm is maximum of orthogonal diagonal blocks; exact complementary emitter correction |
| `LC background source` / `strip` | Neumann .224; selected column; finite trace with factor8; X_bg<2e9; full Schur bottom/side inverses; C_b/C_s; localized<1e-7 | Positive single-open-channel jump on 896 coordinates; source continuation; complete C and uniformly convergent closed tails; both vertical cutoff edges |
| `LC strip ... aggregation expansion` | Exact rational identities for 6.6e21 bottom prefactor and 9.24e-8 side contribution | sqrt(2)<1.5 within parity; 2/sqrt(2pi)<1 accounts for both sides/length, without another column factor |
| `LC scalar` | Separate target/incoming strips, phase113, geometric-sum prefactor, fourth-power exponential remainder and squared normalization | Correct signs of Dref versus Dbar; pole-free domains; Fourier convention and finite negative-lattice sum; these scalar strips do not continue C |
| `LC restricted` | 145kappa pointwise bound; band width2sigma; .04205<.21²; delta<1.6e-6 | Exact complex reference amplitude including real resonance shift; restricted dk moment, not a whole-line Lorentzian moment |
| `LC complete` | Static expansion .000318243241; .000320/.001320 complete ceilings | In-band synthesis, all actual exterior mass, positive reference normalization, different aggregation of preparation versus orthogonal output errors |
| `LC finite` / `improvement` | M=50T; exponent margin9; transfer prefactor<.001; trace factors; ratios250000 | Canonical compensated compression and polynomial cancellation, distanceM+23, sinh(1)<6/5, same embedded infinite target and [T,2T] finite window |

All decimal constants enter via `F('...')`; powers and finite sums are exact integers/rationals. No binary floating-point literals are present. Fractions use ordinary division only when at least one operand is already a Fraction. No local definitions shadow historical kap/T. The pre-existing explicit raising `relation` helper remains effective under `python -O`; this block introduces no bare `assert` statements.

The block deliberately uses the conservative mass constant L=10^6 after checking36000<10^6, preserving the reviewed mass budget. It does not silently substitute the improved L into an unreviewed mass figure. Likewise it sums the reviewed rounded ceilings and retains a positive normalization term. No output count should be described as a new independent proof count.

## Suggested negative mutations (not performed)

Apply one mutation at a time to an isolated candidate copy, preserve its exact diff/source hash and streams, and require failure at the intended named row. These are suggested families, not claims of observed detection.

1. Change disk radius `lc_rho` from1e-12 to1e-5: the bare inverse/filter continuation envelopes should fail, exposing unsupported analytic-neighborhood enlargement.
2. Replace the outgoing row's130 ceiling with100: `LC disk outgoing row squared` should fail. This targets using a one-site row ceiling for a two-site row.
3. Change the endpoint closed-power exponent44 to24 in the actual bound expression: `LC disk endpoint correction input` should fail, exposing a lost propagation segment.
4. Remove the cancellation in the background derivative by replacing the bare `700*17e-6/lc_ad` term by `700/lc_ad`: `LC background cancellation derivative` should fail.
5. Replace the derivative's division by velocity with multiplication and also demand equality to the reviewed 34040 if testing Jacobian direction; the existing loose inequality alone cannot detect an erroneously smaller estimate. This needs an added anchored identity or a source-level mutation review, not a false claim of automatic detection.
6. Inflate lc_L to1e8: `LC actual exterior mass` should fail. Alternatively reduce the log exponent from18 to16: `LC mass logarithm argument` should fail.
7. Remove the real shift from the mass lemma in code: this may only make ceilings smaller and MUST NOT be claimed detectable by these upper-bound tests. Check the actual density-lemma formula via separate source review or anchor the shifted-denominator expression with a fixture.
8. Inflate lc_h to1e-17: the background strip inverse/Neumann rows should fail before accepting a wider strip. Explicit filter and background Neumann-hypothesis rows are included, so a negative inverse denominator cannot silently pass as a smaller upper bound.
9. Remove the full complementary correction or replace transpose by adjoint in an analytical Schur identity: scalar substitution tests cannot detect this identity error. Require the independent mathematical review; no PASS line certifies that algebra.
10. Change the localized side factor44 to22 or remove its1.5 aggregation: the anchored `LC strip side aggregation expansion` equality should fail. Change T downward by a factor10: the fixed bottom-exponent identity and/or localized bound should fail.
11. Enlarge the scalar outgoing h_o from delta/4 to delta: the sinh envelope explicitly retains 2J²*h_o/[kappa²*(1-h_o²)], so this change should fail its .501 ceiling. This tests crossing the reference pole.
12. Replace the restricted moment width2sigma by sigma: `LC restricted moment square coefficient` should fail. Dropping J from its amplitude denominator might only shrink a bound and needs a corresponding anchored formula/source check rather than reliance on lt.
13. Drop the preparation1.415 or outgoing factor2 in lc_static: `LC complete static arithmetic` should fail. Changing trace ceilings without their factor2 should fail the trace equalities.
14. Change M to10T: `LC finite output length` or the exponent-margin row should fail. A finite all-future claim cannot be tested by this finite-window scalar row; it must be rejected in prose review.

## Integration and exposure limits

Root should inspect the text, refresh parameter and source pins, add this dependency set to the runner/package manifest, then execute under a separately recorded bounded prelaunch plan. Preserve ordinary and -O streams, exact source/runtime identities, result outputs and mutation receipts. The draft has not been syntax-compiled or executed, so integration must not call it validated. Existing historical checks should remain unchanged; do not infer success of old or new code from this file's existence.

The component review premises are conditional on the supplied exact Hamiltonian/seed and inherited interval/calibration certificate. This block does not improve physical supply, calibration robustness, finite permanence, runtime optimality, audit status or source independence. No scientific program was run while preparing these two files.
