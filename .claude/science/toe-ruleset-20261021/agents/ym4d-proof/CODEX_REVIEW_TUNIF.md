# Independent hostile review of TUNIF.md

## PRE-STATED

UTC registration: 2026-10-28 21:50:28 UTC. Written before reading the target or deriving any result.

Scope: TUNIF §U0–§U9; permitted tu1/tu1b check records; NLOC §L5/§L7; NORMS §N4/§N7. At most two additional source files will be used, and identified. No git commands, no edits outside this deliverable, no numerical computation except exact arithmetic in plain Python. Source locations will be obtained by string search, with observed line numbers recorded.

Pre-stated targets and refutation criteria:

1. TU-0/TU-1/TU-2/TU-3: reconstruct the twisted difference algebra and boundary conditions. Refutation: a closed admissible analytic 2-form without the asserted primitive; a residual term in the spread correction; a norm loss larger than the advertised bound; or cancellation by a zero divisor in the actual coefficient space. Distinguish analytic families from individual momentum fibers, particularly resonant fibers.
2. Quantifier Q3: reconstruct what m=0 and m>0 norms imply and identify the consumer's actual norm. Refutation: a quantifier mismatch, an invalid implication from a supremum bound, or an asserted necessity unsupported by the consumer.
3. N-loc-b to N-loc-b': count the constant mode's mass in the specified measure and scaling, and trace the repair into the permitted consumer text. Refutation: incorrect mass or scale, or a consumer needing an unrepaired hypothesis.
4. Checks: rebuild what A/B/C/D/E and the replacement D can decide. Refutation: a falsely excused failure, vacuous/tautological gate, or a control that cannot distinguish the claimed defect. A printed PASS is not verification.
5. Scope: trace d=4, trivial background, abelian/linearised hypotheses through the claimed N1-15 transfer. Refutation: use outside those hypotheses without a separate argument.
6. Across all targets: identify symbol meanings by source location, inspect changing constants and quantifiers, and verify any load-bearing numerical or line citation against the allowed sources.

Review verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Findings are appended as the review proceeds; provisional statements will be explicitly revised if later evidence changes them.

## Findings (incremental)

### F1 — TU-0/TU-1/TU-2/TU-3 survive the isolated-fiber attack

**Verdict: CONFIRMED for TU-0/TU-1/TU-2 and the intended 2π-periodic analytic-family version of TU-3; claim status: PROVEN with that explicit domain.** The literal omission of periodicity from TU-3 is addressed in F10; this qualification supersedes any broader reading of this initial finding. Attachments: `TUNIF.md:259–275` (twisted difference and TU-0), `283–290` (TU-1), `296–308` (TU-2), `317–339` (TU-3). This does not yet validate TU-4/TU-5/TU-6's consumer bridge.

Independent reconstruction: along a line write `a=σg/(z−1)`. The function `a+Σ_{i<u}g(i)` has difference `g(u)` at interior sites, while its seam difference is `(z−1)a−Σ_{i<ℓ−1}g(i)=g(ℓ−1)`. The homogeneous equation forces a line-constant value with `(z−1)a=0`. Operators in distinct coordinates commute, including the seam factors.

For the division estimate, put `w=a+ib`, `|a|≤π/2`, `|b|≤η′`. Rotating the integral by `e^{−ia/2}` gives real part at least `e^{−η′}∫_0^1 cos(a(t−1/2))dt ≥ (2/π)e^{−η′}`. Thus `|e^{iw}−1|≥(2/π)e^{−η′}|w|`; Cauchy's estimate bounds `|g(w)|≤|w|G/(η−η′)`. For `π/2≤|a|≤π`, `Re e^{iw}≤0` gives denominator at least 1. Periodicity and vanishing on the entire hyperplane `p_mu=0` remove every zero. This reconstructs the advertised κ bound.

Apply the first line sum to closedness at `p_1=0`: `D_beta Ω_gamma=D_gamma Ω_beta`. Apply the second at `p_2=0`: `D_gamma Φ=0`. Each remaining transverse cell line makes Φ constant in its cell coordinate and gives `(e^{ip_gamma}−1)Φ=0`. Here Φ is still analytic in the remaining variables, including a free `p_gamma` for some `gamma≥3`. On the open set `e^{ip_gamma}≠1`, Φ=0, hence by continuation Φ=0 everywhere. The finite cell index makes this a componentwise argument in a free module of analytic functions. Evaluation at `p_gamma=0` first would invalidate cancellation, but that is not the stated proof. At all-resonant momentum a constant nonzero plaquette is a closed non-exact fiber field; it is not the restriction of a closed analytic family of the required kind. Thus it is not a counterexample to TU-2 or TU-3.

For the spread correction, the line solve gives `D_beta μ=Ω_beta` first away from `z_2=1`, then everywhere analytically. Set `b_1=−μ/ℓ`, extending it independently of `u_1` and `p_1`. This is an admissible cell 1-form; a twisted difference is an operator, not an extra condition requiring the coordinate values themselves to be quasi-periodic. Its transverse derivative is exactly `−Ω_beta/ℓ`, bounded by G on the original strip. Consequently `G_beta=F_1beta−Ω_beta/ℓ` is bounded by 2G on the original strip, even though μ's bound was obtained only on the smaller strip. Its line sum vanishes at `p_1=0`; one more division therefore uses the original η, not a second strip loss. The remaining curl error is annihilated by D_1 and vanishes by analytic continuation. The estimates are `|μ|≤(1+κ)ℓ²G`, `|b_1|≤(1+κ)ℓG`, and `|b_beta|≤2(1+κ)ℓG`. No extra power of ℓ is hidden in this argument.

**Boundary of this confirmation:** admissibility as a cell 1-form is not admissibility as a nested chain reparametrisation fixing all level-k roots. The latter is a separate obligation in TU-6 and is reviewed below.

### F2 — The original tu1-D criterion is satisfiable; the stated excuse is false

**Verdict: REFUTED** for “unsatisfiable by the truth / cannot PASS”; **CONFIRMED** for the recorded seed-777 FAIL and the repaired finite-sample inequality. Attachments: `TUNIF.md:541–551,649–651`; `checks/tu1_criteria.md:37–42`; `checks/tu1b_criteria.md:8–18`; `checks/tu1_twisted.py:264–284`; `checks/tu1b_pole.py:12–24`.

Four sample values `10^-1,...,10^-4` span three decades. A pure pole `A/ε`, A>0, grows by **exactly 1000**, satisfying the original **≥1000**, not violating it. For `A/ε+B`, with positive endpoint values, the ratio is `(10000A+B)/(10A+B)`: below 1000 if B>0, equal if B=0, above if B<0. The existence of a pole alone cannot decide which case holds.

An exact input of the actual construction makes this decisive, not merely a toy scalar objection. Set ℓ=3,d=4, `a_1(u)=1_{u_1=2}`, all other components zero, and `F=D∧a`. Use the script's transverse twists `(z_2,z_3,z_4)=(5/4,3/7,7/5)` and `z_1=1+ε`. Then `F_1beta=−ν_beta·1_{u_1=2}·1_{u_beta=2}`, Ω_beta=`−ν_beta·1_{u_beta=2}`, μ=−1. The corrected solution has `b_1=1/3`, `b_beta=(u_1/3)ν_beta·1_{u_beta=2}` and **max|b|=8/21**, independent of ε. Omitting b_1 gives **max|b|=4/(7ε)**. Thus the four uncorrected maxima are **40/7, 400/7, 4000/7, 40000/7**; growth **1000**, corrected variation **1**, and the original gate **passes**. Exact Python evaluation with the existing functions reproduced these values and zero corrected residuals. No floats or file writes were used by that check.

For the actual seed 777, exact recomputation gives corrected max **158/15** at all six values. The uncorrected maxima are `(1200,11433,113763,1137063,11370063,113700063)/7`, equivalently **1137/(70ε)+9**. Original growth is **379021/400 = 947.5525**, so the recorded 947.6 and FAIL are correct rounded reports. The repair's successive ratios are `3811/400`, `37921/3811`, `379021/37921`, `3790021/379021`, `37900021/3790021`; they satisfy its rational thresholds 9 and 99/10. The mathematical phenomenon is intact, but the correct explanation is **an over-demanding threshold for this pole plus its positive regular part**, not a gate unsatisfiable by a true pole.

The replacement gate also does not characterize a simple pole: the implementation only checks lower bounds on ratios. A double pole has successive ratios **100**, which satisfy every uncorrected-side inequality at `tu1b_pole.py:23`. “Must approach 10” in the criteria is not implemented as convergence, monotonicity toward 10, or even an upper bound. The observed sequence is consistent with a simple pole (and the exact formula above establishes one for these samples); the gate itself cannot exclude higher-order poles. Claim status of the gate's asserted diagnostic sufficiency: **GAP**.

### F3 — The m=0 consumer is real; the m>0 argument does not follow from a sup bound alone

**Verdict: CONFIRMED** for the need to control unrestricted configuration legs for the named N_0 consumer; **REFUTED** for the general “sup bound alone” inference; **NOT-VERIFIED** for a replacement proof for this particular chain at every m>0. Attachments: `TUNIF.md:158–187,196–211,588–590`; `NORMS.md:331–332,422–431`; `PROOF.md:5885–5887,5918–5922,6058–6059`.

For a scalar row M, `Σ_y|M_xy|=sup_{|Y|∞≤1}|Σ_y M_xy Y_y|`, by choosing each Y_y to align the sign. A decay constraint `|Y_y|≤e^{−m d(y,x)}` excludes that global sign pattern. For example `M_xy=1` has unweighted row mass T^d but decay-restricted row action bounded by `Σ_{Z^d}e^{−m|y|_1}`. Thus a bound only for the stated m>0 test class cannot furnish the BR1 N_0 bound. BR1 explicitly uses N_0 at the cited current lines. NAH1's later weighted estimates still import N_0 bounds for local Hessian factors; the positive operator weight there is not permission to replace those factors with a decay-restricted trilinear test norm. In block/color spaces the scalar sign identity needs the corresponding finite-dimensional norm comparison; exact equality of block-norm row sums is not automatic.

However, the factors `e^{−m d(p,x)}` in TUNIF's vertex sum concern the **responses at the vertex p**, whereas the decay restriction is imposed on the **coarse input**. An unweighted `∞→∞` bound does not transport that decay. Counterexample: on a T^d-site torus let `(RY)(p)=Y(x)` for every p. Then `||R||∞→∞=1`, uniformly in T, while the unit decay-admissible input Y=δ_x has RY identically 1. The local cubic `V(X,Y,W)=Σ_p(RX)(p)(RY)(p)(RW)(p)` equals T^d on three such inputs. The claimed leftover decaying factor cannot be inferred from sup bounds. This refutes that inference, not the Yang–Mills chain theorem by itself. A weighted response estimate, or another use of locality/cancellation, is required; NORMS's second N-loc estimate at 423 is exactly an extra weighted input-to-output property.

The m>0 theorem would be a meaningful weaker/easier theorem if its weighted transport hypotheses were proved, not a vacuous statement. The target's main T-UNIF statement is explicitly at m=0, so no hidden m>0 substitution was found in that statement. Full identification with the original N^F-2 definition remains outside the permitted NORMS sections.

### F4 — Mean subtraction loses a factor; harmonic mass uses an upper bound as equality

**Verdict: REFUTED** for the displayed mean-subtraction arithmetic and the equality for one-link harmonic mass; **CONFIRMED** for volume cancellation in the harmonic-mode budget, conditional on the stated harmonic response. Attachments: `TUNIF.md:365,378–392,578–579`.

Write n=k−j. A single unit coarse link in orientation v has mean vector `c_k=T^{−d}e_v`; if its harmonic response is `c_j=L^{−n}c_k`, summing over the **one occupied orientation** gives exactly `T^dL^{dn} L^{−n}T^{−d}=L^{(d−1)n}`. Summing the maximum component over all d orientations yields the conservative upper bound **d L^{(d−1)n}**, not equality for this δ_x. This harmless factor-d overcount leaves the T-free conclusion intact. The harmonic response formula itself relies on Q preserving the mean sector and on orthogonality in the chain form, not just on `Q(const c)=Lc`; its full chain derivation is not supplied by the allowed sections.

The subtraction of the constructed primitive's mean has a different missing factor. Line 392 assumes `|mean b|≤𝔠_0L^{−k}c_{η′}T^{−d}`. Multiplying by the number `dT^dL^{dk}` of level-0 links gives **d𝔠_0c_{η′}L^{(d−1)k}**, not the stated **dc_{η′}L^{(d−1)k}**. The lost factor is **𝔠_0**; at transported levels the direct Q estimate also brings its 𝔮_0 when applicable. Using only the stated envelope and harmonic bound, a safe level-0 estimate for `b−mean b+c_harm,0` is **d(2𝔠_0c_{η′}+1)L^{(d−1)k}**. This is a sufficient triangle bound, not a lower bound or a claim of optimality. The file gives no inequality allowing the omitted 𝔠_0 to be replaced by 1, and M in 𝔠_0 is a free imported bound. Its displayed all-level 𝔠_L therefore is not established by this arithmetic.

Symbol check: `TUNIF.md:365` and `578` both define **𝔠_0=4(d−1)(1+κ)M**. There is no factor-two discrepancy between them. The error above is the omission of the entire 𝔠_0 in the mass calculation.

### F5 — tu1-E passes the very concentrated correction it claims to exclude

**Verdict: REFUTED** for “this is the clause that would have caught” U-F2; **CONFIRMED** for the narrow purpose of control C; **NOT-VERIFIED** for independent computational coverage of analytic continuation. Attachments: `TUNIF.md:535–540,554–556`; `checks/tu1_criteria.md:24–46`; `checks/tu1_twisted.py:189–244,255–258`.

I replaced only the spread correction with `b_1=−μ·1_{u_1=0}`, recomputed the remaining components by the same line solve, and kept the script's original seed and exact sequence of generated inputs. These are exactly the three instances judged by tu1-E:

| Instance | ℓ,d | concentrated max∣b∣ | exact max∣F∣ | max∣b∣/(ℓ max∣F∣) | E's ≤100 gate | curl discrepancies |
|---|---|---|---|---|---|---|
| A1 | 3,4 | 72/5 | 43/2 | 48/215 | passes | 0 |
| A5 | 9,4 | 629/15 | 28 | 629/3780 | passes | 0 |
| A7 | 5,3 | 253/14 | 1401/70 | 253/1401 | passes | 0 |

These are new exact rational checks, not rounded values copied from the output. The concentrated version is the precise failure mode identified in TU-3 at 341–345. The finite bracket cannot certify one power rather than two: a ratio proportional to ℓ remains below 100 at all sampled ℓ≤9. Even the observed decrease in the original ratios is not an exponent test, since different random fields were used at different sizes. E is executable and can reject sufficiently large errors; it does not discriminate the advertised scaling defect on its present inputs.

A is a genuine equation test: it constructs b by integration and then differentiates it, rather than defining F to equal the output derivative. Its use of the same D primitive for generating F and checking b creates shared-implementation risk, reduced here by the separate derivation in F1. B is a telescoping identity on its exact inputs, so it can find indexing errors but cannot test the analytic-domain/non-zero-divisor step. This limitation is honestly disclosed at `tu1_criteria.md:30–32`; C does not upgrade B to a test of that step.

For C, the perturbation is a unit 12-plaquette at the origin. Its 123 closedness component contains `D_3δ`, nonzero already at the origin, and its double line sum is exactly 1. Linearity makes the curl residual of the perturbation independent of the random exact part. A separate coordinate-by-coordinate evaluation of the curl, without using the script's Dmu/residual functions for this evaluation, gave **12 discrepancies with worst 21/5** at ℓ=3,d=4, and **10 with worst 3** at ℓ=5,d=3; max Φ=1 in each. C therefore controls detection of this non-closed input and a nonzero obstruction. It says nothing about root admissibility, the infinite-lattice strip bound, or the scaling exponent.

None of the tested twist vectors lies wholly in the theorem's `η≤1/10` strip: every vector retains, for example, `z_3=3/7`, whereas `e^{−1/10}>9/10>3/7`. They remain useful algebra tests. E also compares against max|F| at a single twist, not the supremum G on the entire strip used by TU-3. A failure of this pointwise numerical inequality would not by itself refute the strip theorem. The construction code divides by ν_1 and ν_2 explicitly and never evaluates either exact zero; continuation to the resonances is established by F1's proof, not by these runs.

### F6 — The chain bridge is not the cell theorem; a precise conditional repair

**Verdict: NOT-VERIFIED** for TU-5/TU-6 as a fully checked discharge of (N-loc), with their displayed constants; claim status: **CONDITIONAL**, with a **GAP** in the supplied all-level budget. Attachments: `TUNIF.md:110–127,377–405,441–468,580–583,641–644`; `NORMS.md:382–432`; `NLOC.md:544–546`.

There are three logically distinct steps: (a) reconstruct a local fine primitive from its curvature; (b) transport it with the same residuals to a chain with both row and column bounds; (c) restore the exact top datum by a nested root-compatible gauge change. F1 establishes (a), given the analytic input. It does not alone establish (b) or (c).

The root correction is **repairable without assuming that the gauge scalar μ itself is local**. Here is the missing operator estimate. Let s=L^{k−j}. Multilinearly interpolate a coarse scalar μ on each s-cell. Across a fine edge in direction α, the interpolated difference is `s^{-1}` times a convex combination of the parallel coarse differences `(d_k μ)_α` at that cell's transverse corners. Thus the gradient interpolation H_j obeys

`||H_j h||∞ ≤ s^{-1}||h||∞`, and `||H_j h||1 ≤ s^{d−1}||h||1` for `h=d_kμ`.

For the second estimate, sum the nonnegative transverse hat weights: in each transverse direction their sum for one coarse node is s; in the longitudinal direction s fine edges each contribute 1/s. The product is exactly s^{d−1}. The formula uses coarse **differences**, not absolute values of a possibly nonlocal μ. Nested grids preserve the interpolation at all roots.

Consequently, if a single preliminary chain map R_j already satisfies `||R_j||∞→∞≤A s^{-1}` and `||R_j||1→1≤B s^{d−1}`, uniformly in j,k,T, and `I−R_k` is exact, then

`R'_j=R_j+H_j(I−R_k)`

has top value I, both bounds with **A'=2A+1, B'=2B+1**, and the same uniformity. Its difference from the original chain is a gauge function vanishing at the top roots, provided the harmonic modes were matched first. This independently confirms the *mechanism* of TUNIF's root correction. It does **not** justify carrying the uncorrected explicit constants through unchanged. TUNIF's “adds a term of the same form” leaves that contribution out of its displayed numerical budget.

What remains unverified in the supplied chain transfer:

- I-A as restated at 110–117 supplies f_0 and r_{k−1}. TU-5 at 383–387 uses **all** r_i with their depth factors and local transports. The needed `κ̂ C_R L^{−(d−1)(k−1−i)}` estimate appears in `NORMS.md:395–398`, where it explicitly relies on that file's (I4). It is not re-derived in TUNIF's list (I-A)–(I-E). Both the scaled residual input and its compatibility with the particular Q must be supplied to certify (b). A uniform ∞→∞ estimate on Q^j alone does not specify its column mass or spatial support.
- The mean sector needs the chain's actual mean-preserving property, not merely its action on constants. For example the two-site map `(y_1,y_2)↦(y_1,y_1)` preserves constants but does not preserve the mean. This is not a counterexample to Setting SC; it pinpoints the missing hypothesis in the stated harmonic argument. The separate missing 𝔠_0 in F4 must also be repaired or avoided by an independently proved stronger mean identity.
- The 1.17 transport correction in §U9 does not account for these mean and root terms. It only addresses the displacement of supports by Q.

For consumer compatibility, `NORMS.md:423` still states two exponential estimates, including a weighted input-to-output estimate. A nonzero constant tail does not satisfy those literal estimates: the rank-one mean map P has `Pδ_x=T^{−d}`, row and column norms both 1, but `T^{−d}≤C e^{−η T/2}` fails for sufficiently large T for every fixed C,η>0. Thus (N-loc-b′) is sufficient for the **unweighted row/column budgets after they are proved**, but is not the original exponential hypothesis. NLOC §L7 identifies the potential ℓ¹ mass as the relevant missing object, which supports this restricted repair. The complete proof of Theorem N1-15 is in NORMS §N6, outside the user's allowed sections; every use of (N-loc) there cannot be certified from §N4/§N7 alone. The request to close all named (N-loc) rows is therefore premature on this review's evidence.

### F7 — The claimed preregistration chronology contradicts the recorded run times

**Verdict: NOT-VERIFIED** for preregistration; **CONFIRMED** for the internal timestamp contradiction. Attachments: `checks/tu1_criteria.md:3`, `checks/tu1b_criteria.md:3`, `TUNIF.md:524,668–671`.

The first criterion says it was written at **21:33 UTC**, before the script existed. TUNIF's run record places tu1 at **21:31:33–21:31:35 UTC**. The replacement criterion says **21:36 UTC**, while the run record places tu1b at **21:32:18 UTC**. These cannot all be the actual event times with the claimed ordering. The existing documents do not decide whether a timestamp is wrong or the criteria were written after the runs. No accusation about intent or invented replacement time is justified; preregistration is unverified until an independent chronology is supplied.

**Verdict: REFUTED** for the labels “four decades” and “six decades.” Attachments: `checks/tu1_out.txt:64`, `checks/tu1b_pole.py:3,22`, `TUNIF.md:549`. Four points from 10^-1 to 10^-4 span **3 decades**; six points from 10^-1 to 10^-6 span **5 decades**, with respectively 3 and 5 adjacent ratios. TUNIF correctly repairs the first interval count in its prose, but repeats the second error.

**Verdict: REFUTED** for “fractions only” if applied to the D verdict arithmetic. Attachments: `TUNIF.md:525–526`; `checks/tu1_twisted.py:275–284`; `checks/tu1b_pole.py:17–23`. The fields and residuals use exact rationals, but both D gates convert maxima to float before computing ratios and comparing thresholds. F2's rational replay establishes the same outcomes for these instances; floating-point rounding did not cause the original FAIL. A/B/E use the exact stored rational quantities.

### F8 — Drifted PROOF citations; explicit physics scope is retained

**Verdict: REFUTED** for the line citations; **CONFIRMED** for the cited statements at the relocated strings. Attachments: `TUNIF.md:218–219`.

- “Lemma BR1 opens ‘Let T ≥ T_0’ (PROOF l.5842)” now points to Lemma U0's exact-lift assertion. The matching BR1 statement is at **PROOF.md:5892**.
- “C_♭ := 4S_♭n_1/r_♭ … (l.5835–5840)” now points into a coupling-window discussion and the beginning of U0. The formula and finite-variable argument are at **PROOF.md:5885–5890**.

These are observed current locations found by string search, not a uniform offset assumption. The cited material at PROOF 6110–6135 really concerns level induction/background uniformity; it does not establish the new TU-6 transfer. No inference from an audit ledger was used.

**Verdict: CONFIRMED** for preservation of the stated d=4, trivial-background, abelian/linearised caveats in the target's main statement and handoffs. Attachments: `TUNIF.md:104–106,165–168,433–440,562–563,641–644,676–679`; `NORMS.md:671–673`. The file explicitly declines to discharge the small-field (H-C) Hessian Lipschitz bound or (N-bg). TU-3 itself is a scalar/linear cochain theorem valid for d≥3; it does not furnish a nonlinear background theorem. The final “unconditional” sentence retains the physics scope but still overstates closure of the bridge identified in F6.

The scale exponents can be checked without a ledger: at d=4, `(θ_w^c,θ_w^r,θ_A)=(2,3,1)` gives Wilson exponent `4−2−2=0` and soft exponent `4−3−2=−1`, hence A_soft=1/L. Summing the soft terms gives **L^3/(L−1)**. The number **13.5=27/2** at `TUNIF.md:397,405` is correct only for **L=3**, not for the entire odd-L≥3 range in §U1; for L=5 the same series is **125/4=31.25**. **Verdict: REFUTED** for reading 13.5 as the evaluated series for all stated L; **CONFIRMED** at the standing L=3 specialization. This is an L-quantifier repair, not evidence against k- or T-uniform convergence.

### F9 — Symbol, quantifier, and unchecked-import register

**Verdict: CONFIRMED** for the following distinct meanings; no comparisons between them were accepted without identifying the object.

| Symbol | Source and meaning | Review consequence |
|---|---|---|
| κ(η,η′) | TUNIF 285: analytic division loss | Used only with its strip arguments in F1 |
| κ=1 / κ_± | TUNIF 115–116,410: coupling parameters | Not the division loss; setting the coupling to 1 does not set κ(η,η′)=1 |
| κ̂ C_R | TUNIF 378; NORMS 395–398: residual-transport coefficient | All-level depth/locality statement not supplied by I-A alone |
| μ in TU-3 | TUNIF 320–321: transverse primitive of Ω, size O(ℓ²G) | Spread by 1/ℓ in the cell |
| μ in admissibility correction | TUNIF 402–403,465: coarse scalar with d_kμ=I−R_k | Different object; F6 estimates its interpolated gradient |
| m | TUNIF 180–187: test-norm weight | m=0 is the claimed consumer norm |
| m_*′,η′ and c_{η′} | TUNIF 110–127,365,379: analytic/decay rates and a geometric sum | η′ stays strictly below the available strip; c_{η′} is finite independently of the test weight m=0 |
| T | TUNIF 102–103: coarse torus side; 159: also a trilinear form name | Volume counting always uses the former |

The two additional source files used beyond the named target/check artifacts and allowed NLOC/NORMS sections were **docs/ai_methodology/SCIENCE_WORKFLOW.md** (operating rules) and **PROOF.md** (string searches and bounded consumer/citation ranges only). No snapshots, audit ledgers, git metadata, or other lane sources were read. Check scripts were inspected as the expressly requested tu1/tu1b check artifacts. No full PROOF read, numerical package, background job, or write outside this deliverable was used.

**NOT-VERIFIED imports and exclusions:** LINEAR_PACKAGE's claimed strip bound uniform in k and the fine offset u, its periodisation statement, the actual Setting SC residual/mean identities, NQ_CHECK's result, the full NORMS §N6 proof, and the other consumers in BFT_B/EXISTENCE were not independently established under this read scope. In particular the comparison prices and crossover in §U4.7 are not certified here: the quoted GREENT formula was not supplied, and the “located rate” is explicitly not a proven strip. The §U6 claims involving BFT_B and representative changes likewise receive no independent confirmation from this review. Named imports are premises, not evidence supplied by their PROVEN labels.

### F10 — TU-3's displayed construction needs an explicit periodicity hypothesis

**Verdict: REFUTED** for analyticity of the displayed construction under the literal “closed and analytic on S_η” hypotheses alone; **CONFIRMED** for the intended periodic-symbol version proved in F1. Claim status: **PROVEN after adding 2π-periodicity**, not a refutation of the Fourier-symbol application. Attachments: `TUNIF.md:283–287` explicitly assumes periodicity in TU-1, but `296–300,317–324` do not state it for F. This is a quantifier/domain omission, not a zero-divisor failure.

Here is an exact bounded analytic counterexample to the formula as literally quantified. Let d≥3, choose any allowed ℓ, and put `a_1(u;p)=f(p_1)=e^{ip_1/2}`, `a_beta=0` for beta≥2, independent of all cell coordinates. Then

`F_1beta=−f(p_1)ν_beta·1_{u_beta=ℓ−1}`, and `F_beta,gamma=0`.

This is exact, hence closed, analytic on the entire strip, and bounded there by `e^{η/2}(1+e^η)`. Its Ω_beta is `−ℓν_beta·1_{u_beta=ℓ−1}`, so the TU-3 formulas give μ=−ℓ and b_1=1. The remaining line solve is

`b_beta=(u_1+ℓ/ν_1)·(1−e^{ip_1/2})ν_beta·1_{u_beta=ℓ−1}`.

At `p_1=2π`, ν_1=0 but `1−e^{ip_1/2}=2`; for any transverse ν_beta≠0 this has a genuine pole. The advertised b is therefore not analytic on S_η′ even though F meets the literal written hypotheses. At p_1=0 the ratio is removable: its limit is −1/2. What fails is extending that cancellation to the other resonances without periodicity.

A coarse Fourier symbol is naturally periodic, so this example is excluded by the intended application. The repair is to state **F is 2π-periodic in the momentum coordinates**, or explicitly work on the complexified momentum torus. With that repair, the cancellation at all resonances and the one-power bound are exactly those rebuilt in F1. The report does not use this wording defect to claim that the physical T-uniformity statement is false.

## Summary table

| Finding | Review verdict | Claim status / consequence |
|---|---|---|
| F1: TU-0/TU-1/TU-2 and periodic TU-3, including resonances and spread | CONFIRMED | PROVEN for periodic analytic families; not arbitrary isolated fibers |
| F10: TU-3 construction under analytic-only literal hypotheses | REFUTED | Add periodicity; an exact nonperiodic family produces a pole at p_1=2π |
| F2: tu1-D “cannot pass” diagnosis | REFUTED | Original gate passes an explicit exact closed input; original seed FAIL is legitimate |
| F2: repaired D as a simple-pole discriminator | REFUTED | Lower-bound gate also accepts a double pole; observed seed formula is a simple pole |
| F3: m=0 matches the named N_0 consumer | CONFIRMED | Global input patterns must be controlled |
| F3: m>0 follows from an unweighted sup bound alone | REFUTED | Weighted response transport is missing from that inference |
| F4: constant-mode budget | REFUTED in its stated arithmetic | Actual one-orientation mass is one budget unit; subtraction loses 𝔠_0 |
| F5: E would catch the concentrated two-power construction | REFUTED | All three concentrated mutations pass E exactly |
| F5: C detects its advertised non-closed perturbation | CONFIRMED | Exact counts 12/10, worst 21/5 and 3, Φ=1 |
| F6: root correction's scale/volume mechanism | CONFIRMED conditionally | Explicit repaired operator bounds A'=2A+1, B'=2B+1 |
| F6: full TU-5/TU-6 / closure of every (N-loc) consumer | NOT-VERIFIED | CONDITIONAL; GAP in the all-level, same-representative budget and consumer audit |
| F7: preregistration chronology | NOT-VERIFIED | Recorded times contradict the claimed order |
| F7: decade counts / fractions-only D gates | REFUTED | 3 and 5 decades; D decisions used floats, independently reproduced exactly |
| F8: PROOF line citations | REFUTED | BR1 relocated to 5892; C_♭ argument to 5885–5890 |
| F8: d=4 / trivial / abelian-linearised scope | CONFIRMED | No discharge of (N-bg) or the background (H-C) clause |
| F8: 13.5 with unrestricted odd L | REFUTED | Correct series L³/(L−1), 13.5 only at L=3 |

**Disposition:** retain TU-3 with explicit momentum periodicity as an independently reconstructed analytic-cell theorem. Do not propagate “T-UNIF / N-loc closed, conditional on N-Q alone” on this review. The all-level chain estimate needs its exact residual/mean premises, corrected constants, and the consumer substitution written out for one common admissible representative. None of the findings is a counterexample to the existence of a T-uniform representative; the strongest positive claim is **NOT-VERIFIED**, not declared false.

**Most dangerous unverified point:** the passage from the analytic fine curvature primitive to a single root-fixed chain representative with simultaneous row and column bounds, using the actual all-level residual and mean identities. TU-3 and the existing check suite do not certify that passage.

Review completed: 2026-10-28 22:09:33 UTC.

## Stdout summary

```text
VERDICTS: TU-0/1/2 and periodic TU-3 CONFIRMED; analytic-only TU-3 formula REFUTED; full TU-5/6 T-UNIF NOT-VERIFIED / CONDITIONAL (chain-transfer GAP).
REFUTED GATES: tu1-D can pass (exact growth 1000, corrected variation 1); tu1b's lower-bound gate accepts ratio 100 from a double pole. Concentrated tu1-E ratios 48/215, 629/3780, 253/1401 all pass.
CORRECTIONS: one-link harmonic mass d*L^((d-1)n) -> L^((d-1)n); constructed-mean budget d*c_eta*L^((d-1)k) -> d*c_0*c_eta*L^((d-1)k). Four/six sample points span 3/5 decades. The soft sum is L^3/(L-1): 13.5 at L=3, 125/4 at L=5. PROOF citations 5842 -> 5892 and 5835-5840 -> 5885-5890.
OTHER REFUTATIONS: m>0 does not follow from unweighted sup control alone; D verdict arithmetic used floats; literal TU-3 needs periodicity (otherwise its formula has a pole at p_1=2*pi).
MOST DANGEROUS UNVERIFIED: simultaneous row/column bounds for the same root-fixed chain after all-level residual transport and harmonic matching.
```
