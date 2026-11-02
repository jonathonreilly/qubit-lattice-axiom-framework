# Independent review of the geometric half-arc correction

**Disposition: LAND at the affected source scope.** No unresolved defect was found in the correction to OSLEAF55's finite site-reflection domain or HRP's corresponding RP export. The original endpoint-only statement is false at temporal extent two; the corrected geometric statement has the paired-half proof below. This is a source review, not an audit, whole-packet certification, or a Yang–Mills construction. **Full four-dimensional Yang–Mills existence and the physical continuum mass gap remain OPEN.**

## Scope, source history and independence

One fresh review pass covered the coordinator's correction in [OSLEAF55.md](OSLEAF55.md):292–315 and [HRP.md](HRP.md):554–566, 619, with the actual definitions, paired-half proof and RP consumers. The complete current HRP text was read. The exact OSLEAF/context ranges, purposes and source hashes are in the [actual-read manifest](checks/review_hrp_half_arc_read_manifest.json). Reading a larger range does not certify its unrelated claims.

The original source is recoverable at commit `295b508bea2c65bf548172f3190e32f7f7eaf6cf`, which was also the unchanged worktree HEAD throughout this review. The [captured exact diff](checks/review_hrp_half_arc_source.diff) contains the entire two-file correction; its SHA-256 is `d201dd63434e062639dc8255a8f8ba02e6d7f969385b7d2a9a53dc93f9270a2b`. No source text outside those two files differed from that baseline among the read scientific contexts. The two new author correction records were read in full, with their hashes independently checked; neither is treated as a reviewer verdict.

| Source | Original SHA-256 at the baseline | Corrected SHA-256 reviewed |
|---|---|---|
| OSLEAF55.md | `7ba9423f52e7da40f5bf2a44dd4fb49d477405bb70cf5b41de3c0482bf2e0df0` | `7f73bedc795e9356f65651a0d39b1fd3e8300fb460846cf84a45f0c5307f0c1c` |
| HRP.md | `f1f991dea8062bfc7176a68cc639beacd848d4fb9cdd0bd4917198e39dac51b5` | `d3a53ef3b29d09c774b1a836603ca731eeadb580127d3928dbbcd5dbe343699e` |

The original discovery remains [REVIEW2_HRP.md](REVIEW2_HRP.md), finding 1, SHA-256 `095a038fb111b456d63c0262b968aaa7b3d08bede58ce34ab214320cda972278`. Its earlier source verdict is historical. I knew the reported counterexample and proposed correction from the task brief and inspected that finding, but independently reconstructed the edge classification, conditional integral and observable transfer rather than inferring correctness from prior reviews. I did not author the correction. This is a fresh restricted-input Codex context, with same-family independence relative to the Codex correction author; no cross-family independence is claimed. The coordinator requested Astra/max. This tool context does not independently attest the backend model identifier or reasoning setting, so that configuration is recorded as requested, not measured.

Methodology was selected from the observed local `origin/main` commit `01589af3faf806b736c42dc2f3bd625e9edead9f`, using the repository workflow, applicable review-loop lenses and physics-loop proof/premise guidance, together with [PROCESS_LIGHT.md](PROCESS_LIGHT.md). No fetch was performed and no newer remote state is claimed. The complete local main delta from `ca2bc7ddf64790da96cd43d42017d000fbfe4808` lists seven anomaly/GR/runner-related files, with no affected source or methodology path. This review does not certify those unrelated changes or substitute for the coordinator's integration checks.

## Finding and independent proof

**Prior BUG, resolved: endpoint membership on the two-edge temporal circle.** At temporal extent `2a`, the positive temporal edge `e_0` goes from `0` to `a` along the chosen arc and the distinct positive edge `e_1` goes from `a` to `2a=0` along the other arc. Site reflection sends `e_0` to the inverse traversal of `e_1` and conversely. Thus

```text
(rho U)_0 = U_1^{-1},       (rho U)_1 = U_0^{-1},
F(U) = Re Tr U_0 - Re Tr U_1,
F(rho U) = -F(U),          Q(F,F) = -E[F^2].
```

For every `N >= 2`, take `U_0=I` and `U_1=diag(-1,-1,1,...,1)` in `SU(N)`: `F=4`. Continuity gives an open neighborhood where `F^2>0`. Product Haar has positive mass on that neighborhood, and every finite real Wilson action gives a continuous strictly positive density. Hence `E[F^2]>0`; the displayed form is strictly negative for all the finite reflection-symmetric Wilson models stated in the correction. No numerical toy group or zero-coupling inference is needed. The observable need not be gauge invariant because the original claim covered all functions of the admitted links. At extent two that original endpoint rule admits both arcs and hence admits this bounded real `F`.

**Required correction, now present:** select one closed geometric temporal arc and distinguish parallel periodic edges even when their endpoint names agree. OSLEAF55:294–297 now does this, and HRP:554–558, 619 qualifies its consumer export. There are no remaining required fixes at this scope.

For the corrected theorem put `R/a=2m`, `m>=1`, and label temporal bases by integers modulo `2m`. Positive-half temporal bases are `0,...,m-1`; reflection reverses orientation and sends a base `k` to `2m-1-k`, exactly the negative family `m,...,2m-1`. Spatial links at layers `1,...,m-1` pair with layers `2m-1,...,m+1`. Spatial links at layers `0` and `m` are individually fixed, with their orientation unchanged. Let `W` collect the spatial links on **both** fixed slices, and `X_+`, `X_-` the remaining two disjoint edge families.

Every spatial plaquette is in one layer. Every temporal plaquette has its temporal interval in one of the two closed arcs: its base is in one of the two disjoint temporal-base sets above. Therefore no elementary plaquette couples the two open halves. Reflection preserves fixed-plane plaquettes pointwise and pairs the other plaquettes, allowing orientation reversal and cyclic rebasing of the Wilson word. Real trace is invariant under both operations. With paired finite real coefficients,

```text
S(U) = S_0(W) + H(W,X_+) + H(W,rho X_-).
```

The finite product-Haar law factors in these three edge families. Reflection permutes the negative variables onto positive ones, possibly inverting them, preserving Haar. For bounded measurable `A(W,X_+)`, Fubini is legitimate since the finite compact-domain density is bounded, and therefore

```text
Z Q(A,A) = integral dW exp(-S_0(W))
           * | integral dX_+ A(W,X_+) exp(-H(W,X_+)) |^2 >= 0.
```

This is the OSLEAF55 displayed proof with half of `S_0` assigned to each half-action. The boundary factor appears exactly once after squaring. No gauge fixing, gauge-invariance restriction, trivial temporal holonomy, or character-positivity argument is required. In particular, a sign assumption on the real site-contained couplings is unnecessary. For `m=1`, `W` contains all spatial links, `X_+` contains one temporal arc and `X_-` the other: the same factorization still holds. Inverse orientations identify a traversal of one edge with its inverse; they never identify these distinct periodic arcs. Spatial extents of two cause no exception because their geometric edges likewise remain distinct. This verifies every even temporal size allowed by the affected statement.

## Observable map and actual consumers

The independent support check used the actual clover formula in [ROTDEF.md](ROTDEF.md):112–121, rather than its locality slogan. Each of the four plaquettes with corner `x` in a coordinate plane has every link in the coordinate box of radius `a` about `x`; in particular its time projection is in `[t_x-a,t_x+a]`. Reflection permutes this plaquette set, possibly reversing Wilson-loop orientation. It therefore gives exactly `e_a(rho U,x)=e_a(U,theta x)`. Reflection invariance of the Wilson measure pairs the real centering, and the stated real positive `Z(a)` preserves covariance. At every fixed cutoff the clover and every finite lattice polynomial are bounded; no cutoff-uniform bound follows from that fact.

In OSLEAF55 D8 and the RP-lat use, compact positive-time multi-tests lie in `(B_{R/4})^n` and `a<=tau_F`. For every nonconstant component the earliest time is positive and at least `a`, while each insertion has `t<R/4`. Thus `a<R/4`, and every clover time interval lies in `[0,R/2]`, including the possibility of tangential boundary links. The far periodic cut is therefore handled as well as the cut at zero. The constant component is harmless. For a fixed compact test on an exhausting sequence, these inequalities hold eventually; `a_j->0` and `R_j>=R_0>0` also force `R_j/a_j->infinity`. The extent-two counterexample cannot become an admissible clover half-observable through this support map.

OSLEAF55's `Theta` on observables/test functions is linear and the star supplies conjugation; HRP's observable `Theta` is antilinear. With real clover variables,

```text
Theta_HRP A_F = conjugate(A_F(rho U)) = A_{R(F^*)}(U),
sum_(n,m) S^(a,R)_(n+m)(R(F_n^*) tensor F_m) = Q(A_F,A_F).
```

Reversing the test arguments in `F_n^*` only permutes commuting lattice field factors. There is exactly one complex conjugation. No kernel, centering prescription, normalization, or soft-field interpretation changes in this correction. HRP:272–291 and ROTDEF:300–308 keep the zero-source bare Wilson marginal by integrating the pointwise normalized kernels from the last level backwards; this transfers the bare-clover form without asserting RP for the whole auxiliary joint law.

I checked the affected continuum implication in full at HRP:481–581; OSLEAF55 D2–D8, Lemmas P/DENSE, RP-lat, CLOSURE-sep(d), CONTRACT-sep's RP step, and errata E2/E8/E9; and the BRIDGE(iii) consumer at OSLEAF55:868–891. Reflected negative ordered times and positive ordered times keep every pairing off coincidences. On a **supplied common sequence** the finite sum of these convergent pairings inherits positivity. A continuous limiting functional and density of compact ordered tests then extend the form to the restricted positive space. Flatness at the ordering-cone boundary absorbs every derivative of the small-gap cutoffs; the independent argument uses fixed insertion orders and does not supply any Yang–Mills growth estimate. At fixed `R`, OSLEAF55 erratum E2 restricts the conclusion to the stated cap-supported subspace, and erratum E8 keeps the sphere finite-RP input separate from RP-lat.

The actual literal consumers were also read: PANEL_P1:54–65, ASSEMBLY55:137–181, and CODEX_REVIEW_P4:246–263. They require convergence of the intended products on a common algebra; restricted off-diagonal distributional convergence alone does not establish those ordinary moments. HRP:559–566, 757, 763, 781–801 preserves that distinction and keeps invariance, radius-uniform control and diagonal compatibility explicit. Its quoted historical “banked” wording grants no new status. The correction changes no continuum convergence hypothesis and does not construct a trajectory, sphere state, reconstruction, non-freeness witness, or positive physical spectral threshold.

## Coverage, preservation and limits

The [read manifest](checks/review_hrp_half_arc_read_manifest.json), SHA-256 `987813bfabea7007d40cd055fadc61a48f68ab219eaf1b773e0bf387393d5936`, is the exact source/range record. The [history manifest](checks/review_hrp_half_arc_history.json), SHA-256 `723c94bb670b7856e76f045e11b2abe6c40a013032c381b263e465e1e3933d67`, verifies that 61 tracked `hrp_*`, `ol55_*`, HRP log and HRP review files remain byte-identical to the baseline. Their numerical criteria, successful or failed outputs and previous review texts remain immutable. This is a preservation check, not re-execution or renewed certification of those numerical claims.

Applicable lens outcomes: the finite domain and paired-half proof are **CLOSED at the stated supplied-regulator scope**; continuum RP transfer is **CONDITIONAL** on the displayed convergence/domain hypotheses; inputs and normalization conventions are disclosed. The standard Wilson model, independent Haar and finite paired real action are supplied mathematical data, with no claimed derivation from the framework axioms or registered primitives. No empirical target, fitted value or new physical premise enters. This counterexample corrects one finite-domain assertion and makes no no-go claim about a construction route or the full theory. Reconstruction, sphere-cell/topology claims, quantitative EXT/TP/growth/UV estimates and the entire older proof packet were not re-certified. The surrounding multiscale program credits Balaban and Dimock; no literature theorem is used to discharge this correction.

One affected-source iteration; one pre-existing bug verified as fixed; zero new blocking findings; zero source fixes by this reviewer. Checks performed were analytic derivation, exact diff/source identity checks and historical-byte preservation. Numerical experiments, broad tests, audit workers, ledger/status mutations, PR operations, Git fetch/checkout/staging/commits and combined integration validation were not performed. The coordinator owns the final integration/publication gates; this verdict grants only affected-source readiness. No retained/audit status is assigned. Frozen report and manifests must be re-opened for an affected source, premise, observable-domain or convergence-contract change; unrelated main movement calls for the coordinator's separate freshness check.

VERDICT: LAND
