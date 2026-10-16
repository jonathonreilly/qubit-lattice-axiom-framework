# Focused canonical M7 source-consistency review v1

Reviewer: `/root/force_energy_bridge_check`. Lead scientific author: `/root`.
Review date: 2026-10-15. This is a scoped scientific source-consistency and adaptation review, not a formal audit verdict, retained-grade promotion, publication approval, or integrated-main validation.

## Outcome and complete-read scope

I found no remaining consequential discrepancy in the reviewed canonical mathematics, source adaptation, or recorded source/result binding. One wording defect was reported and repaired: section 8 called `329/(54 pi)` a norm although it is a **squared energy-dual norm**. The final note says that explicitly. No formula or program changed for that repair.

I read the complete canonical note and all four canonical Python files, including the complete observation kernels, quotient and variation suppliers, massive and curved comparisons, exact-Gram calculation, numerical controls, new analytic enclosure helper, and primary source/output binding. The complete note was first read at `c9b85c2ea8fbfea2fb314f2eb92c3dd61790ca2a149c04fcdb4675ad86a3a97f`, then after the constant-chi/physical-h clarification at `a8a1c3b16992722fcaa95b6b3dd11a42dc8b624b1c3298fbc93e1896cde0c8d9`. The subsequent EOF-only and squared-norm wording differences were inspected separately. Final section 2 through section 9 content was also read directly at the final identity. The four helper/runner sources were read completely; the primary's final EOF-only difference is AST-identical to the earlier source.

Final scientific source identities are:

| Worktree-relative source | SHA256 | Lines |
| --- | --- | ---: |
| `docs/SCALAR_MASS_CURVATURE_COUNT_BOUNDED_THEOREM_NOTE_2026-10-15.md` | `19898e25ef9ae34ee7949f7c688a46dda7c3160f41a69f4986acd9a7f1e998a3` | 536 |
| `scripts/scalar_mass_curvature_count_check.py` | `76e6defceabfee840a63df313cba4e2948f325f6f697c86f23d801a89129afe1` | 64 |
| `scripts/scalar_massive_response_controls.py` | `7213a1eb7d23a936d5388f46de0a355cd60e4dddd42b59f9d614be45d7b5814b` | 276 |
| `scripts/scalar_massive_refinement_controls.py` | `f3f5a8c4d560c7a4560662f7ec48ee9e811ee898eb39fda7ec64ef039620c512` | 123 |
| `scripts/scalar_curved_count_controls.py` | `03c45ca24da8b56157905852971238a96822508c38ffef889b850a76939bf4c0` | 288 |

These hashes, not a mutable branch label, define this review's source scope. The worktree is `/Users/jonBridger/.codex/worktrees/observations-backward-24h-20261014/New Axioms Lets Go`. All reviewer writes for this task are confined to its campaign `physical_bridge/independent_canonical_v1` directory. I made no canonical-source, Git, index, lock, state, observation-data, network, or publication changes and did not start another agent.

## Evidence classes and exposure

The following categories must remain distinct.

1. **My pre-author-source mass derivation and independent controls.** The frozen `independent_massive_v1/PRECHECK_v1.md` and `INDEPENDENT_REVIEW_v1.md` precede access to the author's new massive working implementation. They contain the common-real-energy-space derivation, the clock/force refinement, endpoint/BV accounting, exact radial constants, and 120 independent controls. Those controls were not rerun here. The subsequent `AUTHOR_SOURCE_COMPARISON_v1.md` contains 24 post-source comparisons and is not relabeled independent of author exposure.
2. **Other focused checkers' unchanged independent evidence.** I read their complete reports and the count/Gram prechecks listed below. Their curvature, mass-order, original count, and Gram computations are inherited evidence, not new derivations or executions by me. The curvature review's 209 checks preceded source exposure; its later 747 controls include a 605-point matrix grid and are post-source diagnostics, not 747 physical tests. The independent original-count/Gram review has 63 original-count controls and 10 separate Gram controls. I have not duplicated those routes.
3. **This canonical source consistency and adaptation examination.** Comparing the entire canonical arguments and helper formulas with the frozen independent and author working sources is necessarily post-exposure. Mathematical proof checking, AST comparison, and exact hash binding are valuable but are not new blind empirical tests.
4. **New focused post-exposure diagnostics.** My `canonical_consistency_controls_v1.py` ran 71 checks, all passing, without invoking the author's aggregate runners. They test source adaptation, the new enclosure function against a separate high-precision general-supplier calculation, boundary guards, printed table values, and finite-dimensional energy-normalization/composition fixtures. They are synthetic mathematical and software diagnostics. They provide no observational likelihood, fit, interval-certified PDE solution, or physical scalar detection.

The primary's 59 author aggregate checks are a fifth, separate recorded execution. I verified their final cache and products without rerunning that aggregate or counting it as independent evidence.

## Common real energy space and composition

The positive-frequency convention is internally consistent: real fields are obtained by explicitly adding the conjugate, with no additional `a(-k)=a(k)*` restriction. With `g=2 omega a`, the laboratory norm is `N_mu=4 integral omega^2 |a|^2 = integral |g|^2`. Thus the real Hilbert pairing is `Re integral g1* g2`, and the response kernel and Gram carry the displayed `(2 pi)^(-3/2)` and `(2 pi)^(-3)` factors. This is the same real normalization used in my frozen mass derivation. The use of a homogeneous-H1 representative at zero mass, or an explicitly canceled constant response column, is stated rather than silently identifying arbitrary constant representatives.

All worldline contributions enter the same response amplitude before its norm is taken. Cross terms are retained. Summing separate source norms is allowed only as an upper-bound step; it does not assign an independent field or energy budget to each observation location.

There are two different comparisons in the canonical composition. Let `J_mu` map the common real amplitude space to the initial data of the frozen positive-mass equation, and let `J_0` map it to massless initial data. Both are isometries in their respective energy norms. Let `B_V` and `B_mu` be the varying-potential and frozen operators acting on the **same massive chi initial data**. The relevant identity is

```
B_V J_mu - B_0 J_0
 = (B_V - B_mu) J_mu + (B_mu J_mu - B_0 J_0).
```

The first term is controlled by `epsilon_U`, and the second by `epsilon_mass`. They use the same transformed curved-reference response weights and one common initial epoch. Consequently the triangle inequality is legitimate. It would not be legitimate to identify massless and massive physical Cauchy data without the energy-space map, or to replace the derived curved count weights by an uncorrected flat count. The note explicitly avoids both substitutions. Independently recentering every vector row would also change the common mass-comparison map; the note requires a common origin and preserves that obligation.

For a compatible contrast and a justified projected error bound, the operator bound gives

```
max(0, |r|-e) <= (sqrt(G0)+epsilon_mass+epsilon_U) sqrt(N0).
```

The supplied initial physical energy satisfies `E_phys >= Q lambda_- N0`. Combining these statements yields equation (7) with **`Q lambda_-` in the numerator and no additional factor 1/2**. The earlier laboratory energy is `N0/2`; it is not the same physical normalization. If a known scalar/count coefficient has not been absorbed in the residual, its absolute square belongs in the denominator. Zero coupling or zero denominator demands feasibility handling, rather than division. Finite-dimensional random and eigenvector-attainment controls check this bookkeeping independently of the author's aggregate.

The energy in this result is the stated Einstein comoving excitation energy at the chosen initial slice. It is not a conserved de Sitter Killing energy, a Jordan-frame measurement already identified with an instrument, or a number obtained by substituting SI `G` into natural-unit formulas. No physical energy upper budget is derived.

## Positive-mass argument and its actual regularity domain

The canonical mass proof agrees with the independently frozen argument. For compact real `c_A` in L2 and zero-extended compact continuous `W_A` in W1,1 with `W_A'` in BV, the observation

```
O[h] = sum_A integral [c_A h - (1-|u_A|^2) W_A dot(grad h+u_A partial_t h)] dt
```

has the stated kernel. The `u partial_t h` term, its sign, and its `omega` dependence survive the adaptation. The paths are prescribed compact C3 timelike segments with a uniform speed margin `beta<1`. The force-weight regularity is stronger than bare H1; the note does not extend the explicit tail supplier to arbitrary H1 weights. L2 compact clocks need no extra BV condition, because the clock difference is handled separately.

The first force integration by parts uses the zero outer trace of W. The second is a Stieltjes/BV integration, so total variation includes both external and internal jumps of W'. The displayed quotient suppliers bound `b`, `b'`, and `b''` with the required speed margin, acceleration, and jerk. A sampled maximum would not establish these uniform suppliers; the analytic inequalities do.

The two radial integrals have constants `2-pi/2` and `pi/2-4/3`. The low/high split gives

```
epsilon_mu <= [C sqrt((2-pi/2) mu)
             +D sqrt((pi/2-4/3) mu^3)
             +2 mu sqrt(E V_F)]/(sqrt(2) pi).
```

The positive minimizing cutoff is `4 V_F/(E mu^2)`. For `E=0` or `V_F=0`, the all-cutoff bound is interpreted by its infimum; it does not require an invalid finite minimizer. At `mu=0` the operator difference is exactly zero. These are sufficient enclosures, not equality claims or best constants.

The sharpened clock estimate uses the combined numerator, with `C0=|sum integral c|`, and adds the first spacetime moment to D. Exact `C0=0` removes the generic square-root mass term. A small computed nonzero C0 does not imply exact cancellation. In the curved count example, cancellation is of a constant **comparison chi**. Constant physical h has `chi=a h` and need not cancel. Neither constant probe is asserted to be a finite-energy physical state or a massive KG solution. This was clarified in the canonical note before final freeze.

The separate mass-order counterexample is retained with the correct scope. Single-location spectral density domination does not establish a universal Loewner order for separated clock responses. The canonical smooth-bump localization argument supplies the existence claim. The finite-window cos-squared examples are described as finitely differentiable quadrature diagnostics, not C-infinity witnesses. The counterexample does not reject the particular coherent link or the scalar theory wholesale. I relied on the other checker's independent mass-order report and checked the canonical correspondence; I did not create a new mass-order experiment.

## Curvature, energy conversion, and varying-potential estimate

The supplied de Sitter chart has `a=(1-Ht)^(-1)` and `chi=a h`. Direct substitution changes the propagation potential to `(B-2)H^2/(1-Ht)^2`. Thus the frozen mass is `sqrt(B-2) H`, not `sqrt(B) H`. The transformed observation weights are `W/a` and `[c+(1-u^2) mathcalH W dot u]/a`. The induced clock term has the displayed positive sign. Curved reference clock/orbit weights must first be derived with the curved lapse; a field redefinition by itself does not supply them.

At the initial slice, the quadratic matrix in `(chi', mu0 chi)` is

```
[[1, -rB], [-rB, 1+3 rB^2]],  rB=1/sqrt(B-2).
```

Its eigenvalues are `1+3 rB^2/2 +/- sqrt(rB^2+9 rB^4/4)`. The determinant is positive, and the spatial-gradient coefficient 1 lies between the eigenvalues. This checks the orientation of the physical-energy inequality used in equation (7). The imported `B>12` is more than the positivity needed for this algebra, but it remains an explicit model premise and is not presented as a new derivation.

For the varying-potential comparison, the canonical variation-of-constants system has the correct opposite signs for the two amplitude derivatives and the same initial data as the frozen equation. Its matrix l1 norm is `|U|/omega`. Differentiating the oscillating coefficient matrix produces the additional `U0` term in the second-derivative bound. The positive-mass lower frequency allows the uniform Gronwall suppliers.

The branch force integration by parts requires

```
j_sigma = -(b_sigma dot W)',
r_sigma = (b_sigma+(1-u^2)u) dot W.
```

The second term in `r_sigma` must remain when treating individual amplitudes. Their summed amplitude derivatives cancel in the expression for the full field derivative; omitting this term branch by branch is not justified. The BV product rule gives the stated `C_F`. Its factor 2 conservatively allows separate branch suprema at different times.

The clock comparison is bounded by `RS C/omega^2`; the force comparison uses a low-momentum `RS D/omega` bound and a high-momentum `(C_F+V_F)/k^2` bound. The radial constants and optimized split give equation (4). `S=0`, vanishing force D, and the all-cutoff infimum are treated explicitly. These analytic bounds and density, not a finite collection of plane-wave probes, establish boundedness on the stated frozen energy completion. The separate curvature checker independently derived the field/energy transformations and checked the author's later BV/Gronwall argument; I read those complete reports and checked consistency of the canonical proof and implementation with them.

## Actual curved count and exact reference Gram

The curved count block derives weights from a recognizable supplied ideal coherent link. The linearized equations give `(a delta u)'=-alpha grad chi` and `eta'=alpha chi`, with position kernel `P(t)-P(s)` and `P=t-Ht^2/2`. There is no extra `d(s)` multiplying that position integrand. Fixed-receiver-proper-time null-event differentiation produces both the emission lapse and the receiver lapse ratio in equation (5). There is no ideal coherent spacecraft-clock term, but the spacecraft orbit force remains.

With `gamma=(-1,3,-3,1)` and `beta_i=d(t_i-2L) gamma_i`, the degree-two moment cancellations eliminate the stated initial longitudinal orbit and shared-clock columns of this exact reference. Transverse first-order coefficients vanish for this particular straight-line reference. Converting endpoint phase coefficients into adjacent counts requires the actual proper intervals `Delta_tau_i`. A conformal-time count substitution would alter the observable. The other checker's independent original nonlinear event/clock calculation addresses that issue directly; its source and frozen prechecks are cited below.

The resulting displayed kernels already act on chi. They must not receive an additional `1/a` factor. They have compact piecewise-constant clocks, continuous piecewise-quadratic force weights, and BV first derivatives, satisfying the mass-bound premises. Their exact integral clock cancellation is a response identity, not a choice of physical scalar history.

The exact polynomial

```
G0(H)=(646969 H^2-454020 H+98700)/(16200 pi)
```

is the **massless-propagation Gram of the curved count weights**. It is not the massive or varying-potential Gram. All path terms are summed at common arrival time before squaring. The interval-order changes at angular values `+/-2/3`, the prefactor `1/(4 pi)`, and the flat difference-channel limit are consistent with the separate independent event/interval derivation. I did not rebrand the author's exact polynomial evaluated inside its own control as independent evidence; the other checker's separately frozen pairwise-knot derivation and 10 controls provide that evidence.

The canonical analytic suppliers follow from the gamma step's L1 norm and total variation, both zero traces of F, and the nonnegative time support with `HT<1`. They yield `C<=9.6+4.8H`, `Wsum<=24`, `Wp<=16`, and `V_F<=32+16H`. The origin clock gives `D+M<=2TC+Wsum` and `E<=TWsum`. These are deliberately conservative bounds, not fitted values. My new 70-digit mpmath evaluation of the general supplier formulas independently reproduces all five new enclosure-helper rows and their printed rounding. In particular H=0.01 and H=0.05 fail to certify a small correction; that failure remains visible rather than being discarded.

Exact cancellation with a supplied reference does not imply uniform cancellation with an uncertain reference. The note correctly exposes the leakage `l^T(C-C_hat)theta`; without a bound on theta or exact equality of the operators, a small operator error does not eliminate arbitrary initial-state nuisance. Real trajectory, clock, hardware, and environmental uncertainty remain application obligations.

## Canonical source adaptation and new focused controls

I preserved the complete working/canonical source snapshots and adaptation diffs. The working source hashes are:

- `massive_response_controls_v1.py`: `226fbb6e5f4ef57359d1758a3fe99d5d212f357331ac2d05c1ce1ca3af74692f`.
- `massive_refinement_controls_v1.py`: `9674ee5a3ec50361df27f4a63e723931085b9cae2d1dbbbc7418fe8d77a7f451`.
- `curved_count_controls_v1.py`: `4a272c55ab3ba6a81b51bd3c1d33519a38cd13bd3b7d3a382c600baf43f79ae2`.

All 19 shared functions are AST-identical: ten massive, four refinement, and five curved. The existing scientific prefixes of all three runners are also AST-identical after accounting for `run` becoming `run_checks`, clearing local check arrays, and the added curved `extra_controls` call. The packaging now returns products to a primary runner rather than having helpers perform their previous local output writes. The primary binds the note and all four programs and declares the timeout. None of those changes alters an existing science formula.

The actual scientific addition in canonical packaging is `propagation_enclosure` and its `extra_controls` in the curved helper. I read both completely. My separate evaluation starts from the general stationary supplier formulas, uses high-precision arithmetic, and compares only the pure enclosure function, without invoking `run_checks`, aggregate numerical integrations, or exact-Gram helpers. The maximum observed absolute difference among the five rows was approximately `1.78e-15`. Domain guards reject nonpositive H, `B<=12`, the wrong fixture duration, and `HT>=1`.

The 71 post-exposure checks comprise 19 shared-function identities, three runner-prefix identities, five high-precision enclosure comparisons, a five-row count and five rounding checks, a check retaining the two nonsmall rows, five domain guards, 24 finite-Hilbert energy/composition diagnostics, three eigenvector equality controls, the primary's declared-input check, and four declared-timeout checks. All passed; no failed attempt was suppressed and no repair was needed for this reviewer program. Its SHA256 is `07fb81f63ae76d1017421b2ed582e93e583f5dd1b0a5447cb309959159af6c86`; results SHA256 is `b5fbb773af639eb81a86fb44964cf430e8012ff558e2a840a28f3433ff99ef87`.

## Final cache and exact evidence binding

The author's refreshed primary execution reports exit 0, empty stderr, fresh cache, 59 aggregate checks passed, and elapsed time `2.7399020195` seconds against a 180-second cap. I verified the recorded hashes against the actual final note, all four source files, and the three actual output products. I did not rerun this aggregate. The binding is preserved in `FINAL_CANONICAL_BINDING_v1.json`, SHA256 `9d8b88f64b032cacd8af0d8561fe4c5a6f5348798c5b4df7ae196a5c79fd730e`.

| Recorded artifact | SHA256 |
| --- | --- |
| Runtime `M7_CANONICAL_CACHE_v1.json` | `e4701c8c4a066b67dfb99f69b2054e60721a2e6a80a6a106894198b5d7267539` |
| `logs/runner-cache/scalar_mass_curvature_count_check.txt` | `3dc75e7dbcbc3c2f8bb7cc3f1876964fbef7cf66e6b408790fd26390fd9d5b17` |
| Output `summary.json` | `8d948d45a396844b154e7f2757331034d60a3480f0cc8b07eb231fe179e56c81` |
| `massive_response.json` (18 author checks) | `8ecd805a23ee6aa573a44353797b8bbec62fa48fc82cb8b2667963d344c6e8d8` |
| `mass_refinement.json` (13 author checks) | `a2f54a2a32e978c75c450fd01450a3c3f0f2f024b43cd9df401e7e4d488033bd` |
| `curved_count.json` (28 author checks) | `e155d3d66cce00c08cf9cae58ef7ada9d2546066369b37a1348297db5b8bb2dd` |

The cache input fingerprint is `d51eb7f4ac5f38c33ca4415aaba4a6e32c8574c786c353a46b7f3999cf735213`. All five current source hashes and all three product hashes agree. The products record zero empirical tests, fitted parameters, and physical-energy estimates, and no external scientific inputs. I read the author's ten recorded assertion-rejecting mutation cases but did not execute or independently reconstruct those mutation runs. They remain author evidence.

## Inherited report identities

The following reports were read completely and pinned in `INHERITED_EVIDENCE_IDENTITY_v1.json` (SHA256 `30e4e6b944234ea476b77cfee027fe391d3612f6fbc2b584a83bf197e9d7a59e`). Complete read means the report itself; it does not assert that every file named transitively in that report was reopened or rerun here.

| Path relative to physical_bridge | SHA256 |
| --- | --- |
| `independent_massive_v1/PRECHECK_v1.md` | `4e3e9e12ea953e60e3aaf7fd0fa110192e2a90cb5913e901e28c89e79e45719e` |
| `independent_massive_v1/INDEPENDENT_REVIEW_v1.md` | `8aa2145243f64e3d6b552ed00d08a923282cc7d8fe5f1558fabad91aa222f6d7` |
| `independent_massive_v1/AUTHOR_SOURCE_COMPARISON_v1.md` | `5e4c821f3341ec12cc78c94d9ddb6433d7c98929e075b7a1bad64a275034d6da` |
| `independent_curvature_v1/INDEPENDENT_REVIEW_v1.md` | `16f38d4bc178e5f3d28c7dee9383aa04e55ea87e3f2de940e91114cdc83e9070` |
| `independent_curvature_v1/AUTHOR_SOURCE_COMPARISON_v1.md` | `b9ffe5941a52b4f6176d591910a731ddc1a3a8c7a109b5f72cd52c0cb2ebb6af` |
| `independent_mass_order_v1/MASS_ORDER_REVIEW_v1.md` | `355fa24cbf0632a586139597b7505537d3c0783eb617f1035cdb42435478129e` |
| `independent_mass_order_v1/EQUILATERAL_CORRESPONDENCE_v1.md` | `ea0bcc1d87783f280594fa88137d433c2a4aeb473a3f781acff97b64cc6dbd2b` |
| `independent_mass_order_v1/CURVED_COUNT_PRECHECK_v1.md` | `21a052975ec0a87df00e8f9dd1e704f09d7ae755fc067dc276bc0f2a248d3619` |
| `independent_mass_order_v1/CURVED_GRAM_PRECHECK_v1.md` | `be7bd0f52840ac47c9f3671218fc3daf45dc24775314e0628263ea32bba9b907` |
| `independent_mass_order_v1/CURVED_COUNT_REVIEW_v1.md` | `91088f51b46e93a6483da137647e67c654e01902a735ecee63a73a6643087721` |

The original-count review independently differentiates the nonlinear conformal geodesic/proper-clock/null-event composition and reports maximum finite-difference comparison error about `9.7174e-8`. Its separate exact-Gram calculation reports numerical disagreement below `1.333e-15`. These numerical figures describe those specific synthetic fixtures; they do not provide a real-data error budget. Their report explicitly distinguishes independent precheck from later author-source correspondence, and this review preserves that distinction.

## Surviving imports, limits, and delivery boundary

The action/potential, stationary vacuum, positive kinetic coefficient Q, H, B, free-field linearization, background chart, prescribed trajectories, link model, clock calibration, scalar/count coupling, and observational interpretation remain supplied. The relation `B>12` and all absolute scales are not retired assumptions in this unit. The new derivations provide conditional operator control and an energy requirement, not a selector for actual initial data, a unique environmental history, an energy upper budget, or a TOE.

Arbitrary finite-energy initial data remain allowed in the declared completion. A minimum-energy compatible state is a mathematical extremum, not a state-selection principle. Nonlinear/sourced history, realistic environment, tensor/matter completion, calibration uncertainty, and physically justified residual/error values remain open. No raw observations were read, fitted, or held out during this review. Synthetic controls and exposed development reasoning are not independent empirical tests. The canonical note's proposed status and audit boundary are explicit; this report does not apply a formal verdict.

This report binds canonical source and recorded computation identities. It does not assert the eventual staged inventory or archive delivery identity. The author has stated that any immutable historical snapshots/diffs with whitespace will be preserved byte-for-byte in archives rather than rewritten. Any such archive mapping and final delivery binding must be checked separately against its frozen manifest; the present full source review remains unchanged.
