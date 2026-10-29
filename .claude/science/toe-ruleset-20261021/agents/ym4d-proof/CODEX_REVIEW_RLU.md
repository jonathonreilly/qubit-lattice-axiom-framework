## PRE-STATED — independent hostile review

Recorded 2026-10-29 00:50:07 UTC, before independent calculations or verdicts. Target: `RLARGE_U55.md`. Prior exposure: the user's six attack requests and a locating-string search of the target, including its advertised conclusions and errata. This is not a blind preregistration.

Scope: review the on-disk mathematical arguments and evidence, with no git operations and no writes outside this report. All large-file reads use targeted searches and sed ranges. Arithmetic will use integers and rational numbers only; logarithms will have explicit rational remainder bounds. Existing script PASS lines will not substitute for independent derivations.

Attack criteria:

1. W-cb♯: reconstruct both sides of the new split from TE, RS (R1), PM and KQ; check strictness, domains, normalizations, exponent minima, and all four exact R² values. Attempt to evade the claimed CL obstruction by varying ε_loc within CL's actual proof constraints. A failed preferred choice alone does not prove impossibility.
2. FI-1: check quantifiers and endpoints of the IVT map, uniformity over trial kernels and consistent pasts, recursive existence, and the exact counterexample. Distinguish sufficient contraction assumptions from necessary uniqueness conditions.
3. U1: trace the return exponent to PLD's actual theorem/hypotheses, distinguish an attainable exponent from a supremum, test its binding entry, and derive the complete DX′ comparison including monotonicity assumptions.
4. Margins: recompute using rational logarithm intervals, expose every benchmark input, and test the missing exp(38417 B_0). A benchmark at unproved constants is not a certified live margin.
5. DAG: inspect edges, omitted dependencies and source quantifiers; challenge the proposed θ-first order and K/T uniformity. A finite encoded graph cannot certify completeness of its mathematical dependency model.
6. Controls: inspect ru55_3's defective control and ru55_3b's replacement; independently test the asserted analytic enclosure and wrong-normalization rejection.

Verdicts will be CONFIRMED, NOT-VERIFIED or REFUTED, each with a file and locating string. CONFIRMED conditional implications retain all their hypotheses. The report will end with exactly what may be banked; no scientific audit status will be changed.

## Independent result

Reviewer: Codex, independent of the target's authorship. The target identifies its author as `claude-opus-5-5`. This report concerns the supplied worktree snapshot, not a main-branch or audit-status certification. The user's no-git/single-output instructions control over the review skill's branch/integration procedures.

Let `L = .claude/science/toe-ruleset-20261021/agents/ym4d-proof`; all file references below are relative to L. Target read: all 609 lines of `RLARGE_U55.md`, including E1–E9. Its SHA-256, checked at 00:59 UTC via `sed -n '1,609p' ... | shasum -a 256`, is `14132d95e9336bc71d41e1e3fc6b219e251967460934255ffe4e92643fe8bb88`.

**The useful new mathematics survives: W-cb♯ removes (TC) under HW's stated geometric reading, and FI-1 proves per-level existence under its explicitly strengthened hypotheses. The claimed live numerical conclusions and some dependency conclusions do not survive at their advertised strength.**

| Claim and locating string | Verdict | Scope of result |
|---|---|---|
| `RLARGE_U55.md §2.2`, `Lemma W-cb♯` | **CONFIRMED** | Conditional on (CLS-min), HW's window geometry, and its inherited level/domain conditions; no (TC). |
| `§2.1`, `no ε_loc repairs it`; `ru55-U3a` | **CONFIRMED** | The stated CL estimates cannot certify a positive exponent and (TC) simultaneously on the specified live branch; all four R_TC² values are exact. |
| `§2.3`, `(third entry)/R²`; `ru55-U3d` | **CONFIRMED** | Exact on the four frozen grid points; the third entry is the minimum before and after the split. Not a formula for arbitrary κ and saturated thresholds. |
| `§3.2`, `Theorem FI-1 (per-level existence)` | **CONFIRMED** | The IVT implication, including the new γ restriction. Actual node-A (A-unif)/(A-cont) remain **NOT-VERIFIED**. |
| `§3.3`, `(A-Lip)` | **CONFIRMED** | Sufficient for unique, continuous per-level solutions, with joint continuity and the other FLOW hypotheses retained. |
| `§8`, `Uniqueness ... needs (A-Lip)` | **REFUTED** | Contraction is not necessary for uniqueness. The counterexample establishes failure of continuity-only guarantees, not necessity of (A-Lip). |
| `§1.1`, `a_ret ... (SC2)'s exponent`; `PLD.md`, `Proposition W1R` | **CONFIRMED** | The returned counterterm estimate preserves (SC2)'s exponent. |
| `§1.1`, `a_ret^{PLD} is a supremum, not a value` | **NOT-VERIFIED** | PLD supplies component prices and explicitly permits a fixed loss in the unproved expansion. The proposed endpoint requires an additional quantitative expansion premise. |
| `ru55-U1c`, `(β) entry ... binds` | **CONFIRMED** | Exact Gaussian benchmark on **12**, not 24, parameter triples; no control of the omitted fluctuation correction is supplied. |
| `§1.3`, `(L618-δ)` | **CONFIRMED** | Algebraic endpoint test for the sufficient bound, subject to its monotonicity premise and use of the actual counterterm prefactor. Nonbinding at the live constants remains **NOT-VERIFIED**. |
| `ru55-U1f`, `+61.034`, `+58.238`, `+56.318` | **CONFIRMED** | Rationally enclosed benchmark computations, with all the omitted parameters identified below. |
| `§7 row 11`, the replacement figures as a `live margin` | **NOT-VERIFIED** | These are still conditional benchmarks. The missing exp(38417 B_0) is real, but setting B_0=1 does not evaluate the live route. |
| `ru55-U1e`, `(RLF-δ)'s ceiling is the lowest of RLF's own ceilings` | **REFUTED** | Already false in the target's own fallback scenario: HIST gives 5.203…×10⁻⁹⁶, below all four displayed return ceilings. |
| `ru55-U3f`, `no cycle and no K- or T-growth ... for the encoded graph` | **CONFIRMED** | No new strict SCC or strong growth source; the full graph retains its old SCCs and weak-uniformity obligations. |
| `§1.5`, `θ := min{θ_cap, a_A°/a_bad}` | **CONFIRMED** | Removes the literal 2-cycle when a_A° is positive and independently fixed; the route's moment/probability hypotheses are not thereby proved. |
| `§2.3`, `Unchanged ... a_ret`; `ru55-U3e`, `W-cb♯ does not` reach a_ret | **REFUTED** | As an unconditional dependency assertion once the admitted n_♯→(SC)_k edge is included. The candidate component-price formula stays fixed; the actual cutoff-indexed output need not. |
| `§4 Disclosures`, defective K4; `checks/ru55_3b_lncheck.py`, L1/L3/L4 | **CONFIRMED** | The truncation diagnosis and corrected window checks are correct. Independent rational computation certifies the numerical log bounds. |
| `checks/ru55_3b_criteria.md`, `L2 (independent route)` | **REFUTED** | L2 reconstructs exactly the same interval by exactly the same decomposition. It is not independent evidence. |

## 1. W-cb♯ and the CL incompatibility

**CONFIRMED — the deterministic lemma.** Sources: `HW.md`, `Lemma TE (tower-energy splitting)` and `Lemma W-cb`; `RLARGE.md`, `Lemma RS`, `(R1) Ribbon bound`; `HIST.md`, `Lemma PM`, `Lemma KQ`, and `η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }`.

Write R_TC for the threshold ratio, reserving R for FLOW's slack. Set t=ε_loc/2 and

\[
\eta_* = \min\{\eta_q,t/((16N+3)A_d)\}.
\]

On a coarse-link mismatch, choose that link c and let η_c be the maximum fine-plaquette norm over its two endpoint blocks **including plaquettes straddling their interface**. RS's ribbon rectangles lie in that union. HW expressly places these endpoint blocks inside N₁(Q), so those plaquettes are among the nonnegative energy terms in X_Q^cb.

* If η_c≥η_*, TE(ii) gives an energy contribution at least c_pr min{η_*²,t_pr²}. At k=0 use (B), with c_pr≤1/(2N), as in HW's original lemma.
* If η_c<η_*, put δ=‖M̄_c−S_c‖. Then δ≤A_dη_c<A_dη_*≤δ₀, so PM is applicable and gives ‖W₀−S_c‖≤3δ, ‖M̄_c−W₀‖≤4δ. With x=‖V_c−W₀‖,

\[
x>t-3\delta>\frac{16N}{16N+3}t\ge\max\{16N\delta,t/2\}.
\]

The last inequality uses δ<t/(16N+3) and 32N≥16N+3, valid for N≥2. KQ(lower) consequently gives

\[
\phi_c\ge x^2/(2N)-4\delta x\ge x^2/(4N)\ge t^2/(16N)=\varepsilon_{\rm loc}^2/(64N).
\]

The original fine-plaquette collar failure is priced at t, and original nonquietness is priced at η_q≥η_*. These cases cover the event. Taking their minimum proves exactly the displayed a_cb♯. TE(iii) supplies the unchanged upper bound. The boundary η_c=η_* belongs to the first case, so there is no strict-inequality gap. No new moment or probability estimate was used.

The inheritance matters: this is not a proof of (CLS-min), of the unstated joint rule σ_Q^J, or of the collar moments/(REL). `RLARGE.md §3.6`, `This family is a separate open row (10f)`, and §2.2, `σ^J_Q is still not stated`, remain operative. The collar version of Theorem HW is still conditional on its own moment, overlap, and law hypotheses. The assertion that W-cb♯ removes **the (TC) sub-obligation** is bankable; closure of the collar route is not.

**CONFIRMED — exact arithmetic and loss.** On d=4, L=3, A_d=9, n_P=1296, ε₁≤256Nδ₀, and N b₁≥4,

\[
b_1=1296+1200\kappa,\quad
\varepsilon_{\rm loc}^2=\varepsilon_1^2/(4Nb_1),\quad
\eta_q=\varepsilon_1/(256NA_d),\quad
R_{\rm TC}^2=(16N+3)^2b_1/(4096N).
\]

All calculations below used rational squares, with no numerical square roots:

| N | κ | R_TC² | a_cb♯/a_bad |
|---|---|---|---|
| 2 | 1 | 47775/128 | 1/7925299200 |
| 2 | 1/4 | 488775/2048 | 1/5067619200 |
| 3 | 1 | 33813/64 | 1/25241269248 |
| 3 | 1/4 | 345933/1024 | 1/16139850048 |

At the frozen c_pr=1/1797760 and ε₁<t_pr, both the old and new third entries are strictly smaller than their other entries at these four points. Therefore

\[
a_{\rm cb}^{\sharp}=c_{\rm pr}\eta_*^2
=\frac{c_{\rm pr}\eta_q^2}{R_{\rm TC}^2}
=\frac{a_{\rm cb}}{R_{\rm TC}^2},\qquad a_D^\sharp=a_{\rm cb}^\sharp.
\]

For general parameters the bankable statement is the minimum formula. In particular η_* = η_q/max{1,R_TC}, and a very small κ can make the unchanged kernel entry bind. The blanket equality in `RLARGE_U55.md §8`, `a_cb♯ = a_cb/R² exactly`, must carry its frozen-grid/minimum qualifications.

**CONFIRMED — incompatibility within the actual CL estimate.** Source: `RLARGE.md`, `Proposition CL`, proof `(c) Numerator` / `Denominator`. The numerator supplies ε₁²/(2N) per cube and the denominator estimate spends b₁ε_loc². The stated CL exponent requires ε_loc²≤ε₁²/(4Nb₁). Even merely preserving a positive coefficient with those estimates requires ε_loc²<ε₁²/(2Nb₁). But (TC) requires

\[
\varepsilon_{\rm loc}^2\ge
\left(\frac{16N+3}{128N}\right)^2\varepsilon_1^2.
\]

The ratio of this required squared threshold to the largest strictly admissible squared threshold in the relaxed estimate is R_TC²/2. It is respectively 47775/256, 488775/4096, 33813/128, 345933/2048, all greater than 1. Replacing b₁ by its plaquette part 1296 still leaves a contradiction at N=2,3. Thus changing ε_loc alone cannot repair these estimates. This is not a no-go for every sharper denominator argument, changed collar definition, or the capped η_q branch outside the stated live regime.

For the alternative change of the shared quietness threshold, I also verified `(η_*/2)²/(ε_loc^J/C_♭)²` equals respectively 976125049/158505984, 976125049/101352384, 24403126225/8413756416, 24403126225/5379950016, all >1; C_♭=199. Hence the displayed minimum in `HIST.md`, `Lemma 7.2-0^J`, keeps its second entry on this grid. The lemma's additional chart-ball constant C_♮^J is still required. Under the hypothetical joint threshold ε_loc^J/2 the two squared ratios are exactly 754875625/8192 and 534267075/4096; this arithmetic does not define σ_Q^J.

## 2. FI-1: existence, selection, and what the counterexample proves

**CONFIRMED — per-level conditional existence.** Locators: `RLARGE_U55.md §3.1–§3.2`, `x := u_{k+1}^{ker}` / `Theorem FI-1`; `HIST.md §4`, `w^J_B`; `RLARGE.md §4.4`, `Option A`; `FLOW.md`, `Theorem F-flow`.

The two-kernel formula w_B^J reads K_k and K_{k+1}, while later normalized kernels integrate to 1 in the earlier marginal. With the stipulated stage representation, the next trial parameter is one scalar x. Set ℓ=β₀′log L>0. UNIV-1L supplies |b_k−ℓ|≤R; A-unif and the γ restriction supply |ρ_k(x)|≤ℓ/2. Consequently

\[
\Phi_k(X_k)\subset
[u_k-3\ell/2-R,\ u_k+R-\ell/2]\subset X_k.
\]

The new restriction u_k≥γ⁻²≥x_lo+R+3ℓ/2 puts the whole trial interval above x_lo. Thus the left endpoint has Φ_k(x)−x≥0, the right endpoint has Φ_k(x)−x≤−ℓ/2<0, and A-cont gives a zero. The bound on ρ_k at that zero gives F_R on the extended interval by the same finite sum as F-flow. It does not require knowing the next effective coupling before solving the equation.

There is a useful noncircular finite-sequence version of the target's weakly worded `Corollary (sequence)`: for any finite K, take

\[
u_0\ge\gamma^{-2}+\beta_+K\log L+R.
\]

After each IVT step, F_R gives u_{k+1}≥u₀−β₊(k+1)log L−R≥γ⁻², so another step is admissible. This proves existence through K under the same uniform assumptions. It does not give an infinite weak-coupling trajectory from a fixed finite u₀.

**NOT-VERIFIED — discharge for the actual YM stage.** A-unif must be a bound for **every trial x in X_k**, for every admitted past, with constants fixed before choosing x. FLOW's bounds along the chain's own sequence are not that statement. The bracket alone does not prove such a uniform stage estimate or continuity of the sea expansion. The source correctly names A-unif/A-cont; calling U4/K11 `SUPERSEDED` must mean replacement by these explicit open hypotheses, not that they have been established. No K/T dependence is introduced by the interval argument if R, β₀′, C_ρ and γ are already uniform. Their uniformity and (SF-∞) do not follow from IVT.

**CONFIRMED — contraction gives uniqueness and continuous selection.** Locators: `RLARGE_U55.md §3.3`, `(A-Lip)`; `FLOW.md`, `(SF-cont)` and `Theorem F-tune`. Φ is a q-contraction on the complete interval, so the fixed point is unique. Joint continuity in the past gives continuous dependence. A clean proof with the moving intervals is: for pasts p_n→p, their fixed points stay in a common compact interval; any subsequential limit belongs to X_k(p) and is a fixed point by joint continuity; uniqueness makes every such limit x*(p). Induct on k. FLOW takes the one-loop b_k to be g-independent; if one generalizes b_k to depend on the past, continuity of that dependence must also be imposed. Retain F-tune's other hypotheses, particularly (SF-∞). A-an's stated uniform complex-disc bound implies q≤1/2 by Cauchy's estimate, but no such bound for the full stage output has been proved here.

**CONFIRMED — continuity and a small remainder do not guarantee uniqueness or a continuous smallest-root selection.** Locators: `checks/ru55_4_fi1.py`, `ymin_steep`; `RLARGE_U55.md §4 Disclosures (2)`. Let clip_a(y)=max{−a,min{a,y}} and h(y)=2clip_a(y). The equation y=h(y)+s has three solutions at s=0: −2a,0,2a. Its smallest root equals s−2a for s<a, equals −a at s=a, and equals s+2a for s>a. Thus its one-sided jump at s=a is 4a, not merely a large finite difference at two sampled points.

The published F4 samples use ε=3/1000, a=1/1000, d=1/10⁶ and s=a+d. Their bound is ε+d, so the original sample is outside its exact preregistered ε-budget. The target discloses this correctly. I independently checked the proposed repair, without modifying the original check: set

\[
a=(\varepsilon-d)/3=2999/3000000,
\quad s\in[a-d,a+d].
\]

Then 2a+max|s|=ε exactly; the two sampled smallest roots are −1501/1500000 and 3/1000, separated by 6001/1500000>ε. Taking ρ=−h−s gives the promised uniform budget and the same discontinuity mechanism. This is an exact, repairable defect in the recorded control, not a counterexample to the IVT theorem.

**REFUTED — necessity of (A-Lip).** Locator: `RLARGE_U55.md §8`, `Uniqueness, and hence F-tune ... needs (A-Lip)`. With the opposite sign, ρ(x)=2clip_a(x−m), the fixed-point equation x=m−ρ(x) has the unique solution x=m: y+2clip_a(y) is strictly increasing and vanishes only at 0. Its local Lipschitz constant is 2, so A-Lip fails. This fits FI-1's scalar hypotheses at arbitrary admitted ℓ,R,b,u: take m=u−b and a=min{ℓ/8,C_ρ/(4u)}>0. The center m is at least ℓ/2 above X's lower endpoint and at least ℓ below its upper endpoint, because |b−ℓ|≤R. Also |ρ|≤2a≤C_ρ/(2u), and Φ(X) lies in [m−2a,m+2a]⊂X. Dependence on u is continuous. Thus even the uniform smallness budget and self-map condition do not make contraction necessary. This is a counterexample to the asserted logical necessity, not a proposed YM remainder. The correct statement is **A-Lip is one sufficient condition; A-cont alone is insufficient for a uniqueness/selection theorem**. The proposed Browder continuation alternative remains **NOT-VERIFIED**; the target itself does not write that proof.

## 3. U1: the return exponent and the DX′ test

**CONFIRMED — identification and domain.** Locators: `PLD.md §9.4`, `(SC2)` / `Proposition W1R`; `PLD.md §16.8`, `[RPLD4-fix CC-2]`; `RLARGE.md §1.2`, `(RLF-0)` / `[v3-δ]`. W1R bounds the counterterms by C′g_k^{−6−p(SC)}exp(−a/g_k²), with a the (SC2) exponent. Both are extracted at V=1, on the chart. The off-chart Proposition CC does not refute this chart estimate. The SC expansion and the other W1R hypotheses remain hypotheses.

**CONFIRMED — component-price formula; NOT-VERIFIED — its promotion to the supplied SC supremum.** The exact PLD locator is `a_ret on the chart (the explicit formula; per-cube prices PROVEN as cited, the expansion (SC)_k itself still HYPOTHESIS)` and, immediately after the displayed minimum, `per cube; (SC)_k's cluster expansion may lose a fixed factor`. Define the candidate component-price minimum by

\[
A=\min\{\kappa\varepsilon_1^2/(2048N),\,
49\eta_q^2/(1024\sigma_{\rm fl}^2),\,
\kappa\varepsilon_{\rm loc}^2/(64N)\}.
\]

If one additionally proves a uniform polymer estimate of the form (C exp(−Au))^{|X|}, with the requisite derivative/locality bounds and with only subexponential or fixed prefactors lost in the expansion, then any fixed a′<A can absorb those losses by reducing the coupling ceiling. That conditional reasoning in the target is sound. But **PLD does not supply that quantitative expansion theorem**. A fixed multiplicative loss in the exponent is explicitly allowed there. Neither an expansion retaining every a′<A nor attainment of A follows from the stated (SC)_k hypothesis. Also an upper bound based on A does not establish that the true optimal decay rate cannot be larger. Thus A is a proposed endpoint of a particular proof estimate, not an independently established optimal or attained SC exponent. The target's phrase `conditional on (SC)_k being proven that way` must be retained whenever using its supremum language.

The chart restriction is also essential: the β-price requires r_ch≤L²η_q/(4C_I), the near-trivial curvature bound, and (SG^fl)_k. A level-k bound on σ_fl and the O(α_*) correction in `σ_fl² = 16(1 + O(α_*))/λ_min` are not discharged by this review. The appearance of (SG^fl)_k and restricted (BG)_k on the numerical a_ret path is **CONFIRMED**, contrary to reading RLARGE rows 7–8 as excluding them from that path.

For the **Gaussian benchmark** σ_fl²=16/λ_min, the β entry is exactly

\[
A_\beta/\varepsilon_1^2
=\frac{49\lambda_{\min}}{2^{30}N^2 A_d^2}.
\]

I compared it, as a rational number, against κ/(2048N) and κ/(256N²b₁) for N∈{2,3}, κ∈{1,1/4}, λ_min∈{317/100000,423/100000,66/10¹¹}. It is strictly the smallest at all **2·2·3=12** triples. At λ_min=317/100000:

| N | A_β/ε₁² | A_β/a_bad, at c_pr=1/1797760 |
|---|---|---|
| 2 | 15533/34789235097600000 | 43632197/54358179840000 |
| 3 | 15533/78275778969600000 | 43632197/122305904640000 |

These are arithmetic evaluations of frozen parameters; in particular the N=3 row does not establish the SU(N) moment hypotheses. With ε₁=67/10⁴¹ and N=2, the rational price lies in `[2.004287728, 2.004287729] × 10⁻⁹¹`. The target's binding-entry arithmetic is correct, its `24 grid points` count is not.

**CONFIRMED — a sufficiently small return ceiling exists for every fixed a_ret>0.** Locator: `RLARGE_U55.md §1.2`, with erratum E1. For C>0 and P=12+p(SC)≥12, put

\[
\phi(t)=a_{\rm ret}t-(P/2)\log t-\log C,\qquad t=g^{-2}.
\]

Since log t<√t, φ(t)≥ψ(√t), where ψ(s)=a_ret s²−(P/2)s−log⁺C. Its positive root is the stated s₀; ψ(s)≥0 for every s≥s₀. Thus g≤1/s₀ suffices, independently of the mistaken monotonicity sentence corrected by E1. No decimal evaluation of a_ret is needed for this existence implication. Uniformity in K,T holds only if the input a_ret,C,P are uniform.

**CONFIRMED — (L618-δ) as a conditional comparison; NOT-VERIFIED — nonbinding at live inputs.** Locators: `RLARGE_U55.md §1.3`, `(L618-δ)`; `RLARGE.md`, `RLF's own ceilings do not bind`; `SF.md`, `C_Ω := C + 3(N² − 1)/2`.

Let d_DX=25/10¹⁵³ and t_DX=C_Ω/d_DX. Requiring the **sufficient counterterm estimate** to imply |δβ|≤g⁶ throughout 0<g²≤d_DX/C_Ω is exactly

\[
\phi\bigl(\max\{t_{\rm DX},P/(2a_{\rm ret})\}\bigr)\ge0.
\]

On the monotone branch t_DX≥P/(2a_ret), this reduces to precisely

\[
\log C+\frac{12+p({\rm SC})}{2}\log\frac{C_\Omega}{d_{\rm DX}}
\le a_{\rm ret}\frac{C_\Omega}{d_{\rm DX}}.\tag{L618-δ}
\]

There are three qualifications to preserve:

1. C here must be the **derived RLF/W1R counterterm prefactor C′**, including extraction and derivative constants. W1R displays C′, not literal equality to SC2's raw C. Calling it an inequality on SC's constants means all these derived constants must be bounded too. SF's C inside C_Ω is a different constant.
2. It tests a sufficient majorant. Failure does not prove that the actual δβ exceeds g⁶. Conversely existence of some positive a_ret does not prove nonbinding at the fixed DX ceiling.
3. The monotonicity premise and actual positive exponent remain part of the test. For example a_ret=d_DX, P=18, C=C_Ω=1 makes φ(t_DX)=1−9 log(1/d_DX)<0 despite modest prefactors. A fixed positive exponent alone is not a magnitude comparison.

At the proposed Gaussian endpoint A above and C_Ω=1, independently certified rational intervals give

\[
\log t_{\rm DX}\in[349.076643403,349.076643404],\quad
A t_{\rm DX}\in[8.017150915,8.017150916]\,10^{60},
\]

and the maximum P at log C=0 is in `[4.593347086,4.593347087] × 10⁵⁸`. The joint benchmark (P,log C)=(10⁵⁸,10⁶⁰) satisfies the inequality and monotonicity; (10⁶²,0) fails the inequality. These checks confirm the advertised envelope at its stated inputs. They do not bound the actual constants or the rate lost in SC. C_Ω=1 is a comparison normalization, not SF's actual N=2 value: for nonnegative TILT C, SF already gives C_Ω≥9/2. Increasing C_Ω helps on the monotone branch; this does not settle the other missing inputs.

## 4. Exact margins: numerical agreement, incorrect live ranking

**CONFIRMED — the missing exponential factor.** Locators: `HW.md`, `6400C_ℓe^{aR}e^{38417B_0}e^{-a/g_K²} ≤ ½`; `RLARGE_U55.md §1.6` / `ru55-U1f`; `RLARGE.md`, `g_K² ≲ a/10²`. The actual sufficient HIST condition is

\[
g_K^2\le\frac{a}{\log12800+\log C_\ell+aR+38417B_0}.
\]

It is not a/100. The missing exp(38417B₀) becomes an additive **38417B₀** in the denominator; it is not a multiplicative correction to a.

For the target's benchmark, take ε₁=67/10⁴¹, c_pr=1/1797760, N=2, Gaussian λ_min=317/100000, C_Ω=1, B₀=1, log C_fc=0, aR=0, and log C_ℓ=324 log(4/3). This gives

\[
D\in[38519.666191924,38519.666191925].
\]

Every endpoint in the following tables is a rational decimal, rounded **outwards**, not a floating-point display:

| HIST input θ | Certified g_H² interval | Certified log₁₀(g_H²/d_DX) interval |
|---|---|---|
| 1/24, route-(iii) limiting benchmark | [2.700997210,2.700997211] × 10⁻⁹¹ | [61.033584126,61.033584127] |
| 1/15000, route-(iv) cap benchmark | [4.321595536,4.321595537] × 10⁻⁹⁴ | [58.237704109,58.237704110] |
| A/a_bad, route-(ii) fallback benchmark | [5.203284262,5.203284263] × 10⁻⁹⁶ | [56.318337543,56.318337544] |

With denominator 100 instead, θ=1/24 gives `[63.619266641,63.619266642]`, so the old +63.619 arithmetic is also reproduced. The corrections +61.03/+58.24/+56.32 are numerically correct **at these frozen benchmark inputs**.

For the return ceiling, solving A t−(P/2)log t−log C=0 on its increasing branch gives:

| p(SC) | log C | Certified g_δ² interval | Certified log₁₀(g_δ²/d_DX) interval |
|---|---|---|---|
| 6 | 0 | [1.029038100,1.029038101] × 10⁻⁹⁴ | [57.614491446,57.614491447] |
| 6 | 50 | [1.003167836,1.003167837] × 10⁻⁹⁴ | [57.603433590,57.603433591] |
| 12 | 0 | [7.707492563,7.707492564] × 10⁻⁹⁵ | [57.488973105,57.488973106] |
| 12 | 50 | [7.561437388,7.561437389] × 10⁻⁹⁵ | [57.480664351,57.480664352] |
| 702 | 100000 | [1.120505198,1.120505199] × 10⁻⁹⁶ | [55.651473867,55.651473868] |

The final row is illustrative, as the target says. All rows evaluate **A**, not a proved attained a_ret. Calling the first four “approximately +57.5” is an acceptable shorthand for their displayed range; it is not a measured or established live margin.

**REFUTED — the route-independent binding claim.** Locators: `RLARGE_U55.md`, `ru55-U1e`, `(RLF-δ)'s ceiling is the lowest of RLF's own ceilings`; `ru55-U1f`, `the binding RLF ceiling is (RLF-δ)'s`; §8 item 2. Within the target's own inputs, the fallback HIST ceiling is at most 5.203284263×10⁻⁹⁶, whereas the smallest of its four sample return ceilings is at least 7.561437388×10⁻⁹⁵. Thus **HIST is lower on that fallback route**. For the first two θ benchmarks and those same four SC examples, δ is lower. With the illustrative (702,100000), δ is lower even on the fallback route. The ranking depends on the route and the actual SC constants.

There is a second source-level reason not to call B₀=1 “live.” `HW.md §32`, `Constants against the record`, already carries a c_f-dependent HIST/REL ceiling below the recorded return ceiling. Its subsequent §35.7, `The constants after §35.2–§35.6`, gives c_f=C_sh·81·c_+, with C_sh=81 and c_+=c_A+17c_U for the ring. At that section's c_A=0,c_U=1, c_f=111537; its unchanged-HIST comparison explicitly uses B₀=c_f+2, not 1. These exact formulas suffice to show that the target's B₀=1 comparison does not evaluate that recorded route. The review does not certify the ring/CRC theorem by quoting its illustrative decimal outputs.

**NOT-VERIFIED — any of these numbers as the final live margin.** One still needs the admissible θ (strict CAP inequalities exclude the supremum itself), a proved a_A, a proved positive returned exponent after SC, its C′ and p, the fluctuation correction, the applicable C_fc/C_ℓ, B₀, R, and actual C_Ω. Positive missing log C_fc and aR lower the displayed HIST values; actual C_Ω adds log₁₀C_Ω to the margin at a fixed numerator ceiling. The target discloses several omissions, but disclosure does not turn an evaluated benchmark into the programme's binding margin. Its `Every ru55_3 verdict therefore stands` is valid for the corrected numerical computations, not these stronger interpretations.

## 5. Dependency check: what is acyclic, and what still moves

**CONFIRMED — the encoded strict-graph result.** Locators: `checks/ru55_2_variants.py`, `v1`, `v3`, `v4`, `v5`, `v6`; `checks/dag55_2_dag.py`, `STRICT_EXCLUDE = {"implicit", "fixedpoint"}`. I loaded the inert graph data and variant constructors under `python3 -I -B`, but used an independent reachability implementation: components were computed by mutual transitive reachability, not the author's Tarjan checker. Results:

| Variant | Nontrivial strict SCCs | Full-graph SCC sizes |
|---|---|---|
| V0 | none | 4,12 |
| V1, W-cb♯ | none | 4,12 |
| V2, shared quietness change | none | 4,12 |
| V3, literal θ→a_A | {a_A,θ} | 4,12 |
| V4, θ-first order | none | 4,11 |
| V5, FI-1 γ condition | none | 4,12 |
| V6, combined | none | 4,11 |

The strong live growth seeds remain C_fun and V_LF. Neither strongly taints η_*, while the weak uniformity seed does: ε_N5,unif→ε_loc→η_*. A deliberately inserted a_cb→η_* back-edge created the expected strict SCC; starting a growth tag at η_* reached g₀. These were independent structural controls. W-cb♯ adds no K or T factor to its explicit local formulas. It does not prove level-uniform ε₁, eliminate existing growth elsewhere, or erase the full graph's implicit/fixed-point components.

**CONFIRMED — the algebraic θ repair, conditionally on an independently available price.** Locator: `RLARGE_U55.md §1.5`. For positive θ-free a_A° and a_bad, first choose a fixed admissible θ_cap strictly below the relevant moment cap, then set

\[
\theta=\min\{\theta_{\rm cap},a_A^\circ/a_{\rm bad}\},\quad
a_A=\min\{a_A^\circ,6\theta a_{\rm bad}\},\quad
a=\theta a_{\rm bad}.
\]

Both entries defining a_A are ≥θa_bad. This supplies a forward order and removes the need to read θ back from that a_A. For the explicit route-(iii) formula, a_A°=λκε₁²/256 is indeed independent of θ. The κ≥256θc_pr/λ comparison and threshold 1/84270 at θ=1/24, λ=1/2 are exact. If routes (i)/(ii) use a_ns or a_cd, their positivity, applicable law class and availability before θ must be supplied; a name without an explicit θ argument is not a uniformity theorem. Their moment hypotheses remain open, and this review does not independently re-audit the target's imported claim that (CEM^COL) is false as quantified.

**CONFIRMED — the reported cutoff SCC calculation; REFUTED — the claimed absence of a forward path to a_ret.** Locators: `checks/ru55_2b_dag.py`, `add_cut` / `a_ret -> theta`; `PLD.md §9.0`, `𝒢_x := Σ_{N≤n_♯}Σ_{S∋x}𝓖^{(N)}_S/|S|`; `RLARGE_U55.md`, `ru55-U1i` / `ru55-U3e`.

Adding n_♯→SC_k produces the reported 14-node cutoff SCC in W0 and W6. Removing the route-(ii) fallback edge a_ret→θ yields the reported 12-node SCC in W8; θ and a_ret are outside it. But the forward paths in that same W8 graph are

\[
\eta_*\to a_{\rm cb}\to a_D\to a\to n_\sharp\to({\rm SC})_k\to a_{\rm ret},
\]

and

\[
\eta_*\to a_{\rm cb}\to a_D\to a\to n_\sharp\to({\rm SC})_k
\to C_{p,\mathrm{RLF0}}\to\gamma_0.
\]

Thus **being outside the cutoff SCC is not being independent of the cutoff**. The target itself permits the order `n_♯, then (SC)_k at that cutoff, then a_ret(n_♯) > 0`, yet elsewhere declares a_ret unchanged and cites V1's lack of descendants as evidence. The latter V1 calculation omitted the very edge subsequently admitted in ru55_2b.

Precisely what stays unchanged is η_q, ε_loc, and the candidate **component-price expression A**. If collars are actually included so that a_D→a is active, the cutoff and the actual SC outputs can move. A pre-proved cutoff-uniform SC estimate with the same constants could prevent that change; none is supplied. In the bad-only route, the collar a_D→a edge is inactive, so this particular propagation is absent. Do not merge these two route scopes. The remaining cutoff SCC also still contains SC_k and node-A constants after θ's literal 2-cycle is removed.

## 6. Controls and exact-arithmetic provenance

**CONFIRMED — K4's defect was correctly disclosed.** Locators: `checks/ru55_3_u1.py`, `K4: contains`; `checks/ru55_3_out.txt`, `CONTROLS: NOT all as designed`; `RLARGE_U55.md §4`, `Disclosures`. The check asks whether an interval of width 4/10⁴⁵ containing log 10 also contains the exact rational 2302585092994045684/10¹⁸. It should not. My independent enclosure gives

\[
\log10-2302585092994045684/10^{18}
\in[1.799145468436420,1.799145468436421]\,10^{-20}.
\]

The source's displayed `2.30258509299404590109` is produced by its explicit float formatting and is not a rigorous decimal endpoint. The underlying Fraction interval is correct; no float is used by its mathematical gate expressions. The original check did **not** satisfy its own all-controls rule, and exit 0 is not a mathematical PASS.

**CONFIRMED — ru55_3b's L1, L3 and shifted L4; REFUTED — independence of L2.** Locators: `checks/ru55_3b_lncheck.py`, `alt = (3 * l2[0] + l54[0]`; `checks/ru55_3_u1.py`, `ln_enc`. That function already evaluates log 10 by reducing 10=2³·(5/4). It evaluates log 2 as LN2 plus the zero interval for log 1. Therefore L2's alternative interval equals the original interval **exactly, endpoint for endpoint**; I checked the equality using Fractions. A shared multiplication of both by 1001/1000 still passes this agreement test, although L1 rejects it. L1/L3 are useful external decimal-window checks, and L4 checks rejection of the specified 10⁻²⁰ shift. They do not alone certify all log arguments or the mathematical inputs to the margin claims.

The author's analytic remainder formula is nevertheless correct: for m∈[1,2], z=(m−1)/(m+1), the omitted part of 2Σ_{j=0}^{n−1}z^{2j+1}/(2j+1) is between 0 and 2z^{2n+1}/((2n+1)(1−z²)); its floor/ceiling operations and signed k·LN2 addition enclose the result. I separately used a different series and direct evaluation of log 10, rather than that decomposition:

\[
\log x=\sum_{j=1}^n\frac{w^j}{j}+R_n,
\quad w=1-1/x,\quad
0\le R_n\le\frac{w^{n+1}}{(n+1)(1-w)},\quad x\ge1.
\]

With an integer grid S=10⁸⁰, each power, term and tail was rounded down/up separately. I used n=2000 directly at x=10, n=300 at x=2 and at reduced arguments in [1,2). Other positive arguments were reduced by exact powers of 2, reversing the interval endpoints when multiplying by a negative power index. Division used all four rational endpoint quotients. No binary floats, Decimal approximations, numerical exp, or numerical log were used in the independent computations.

The independently obtained intervals, contained in the author's Fraction intervals, include

\[
\log10\in[2.30258509299404568401799145468436420760110148862877,
2.30258509299404568401799145468436420760110148862878],
\]

\[
\log2\in[0.69314718055994530941723212145817656807550013436025,
0.69314718055994530941723212145817656807550013436026].
\]

The interval core actually executed in memory was:

```python
from fractions import Fraction as F
S = 10**80

def ceilq(q):
    return -((-q.numerator) // q.denominator)

def log_series(x, n):
    x = F(x)
    assert x >= 1
    w = (x - 1) / x
    z = w * S
    lo, hi = z.numerator // z.denominator, ceilq(z)
    sl = sh = 0
    for j in range(1, n + 1):
        sl += lo // j
        sh += (hi + j - 1) // j
        a, b = lo * w, hi * w
        lo = a.numerator // a.denominator
        hi = ceilq(b)
    tail = ceilq(F(hi, n + 1) / (1 - w))
    return F(sl, S), F(sh + tail, S)
```

For each return-ceiling row I bracketed t in [10⁹⁰,10⁹⁸], verified strict negative/positive φ signs with the rational log intervals, and performed 120 integer midpoint bisections. The final bracket is above P/(2A), so the root is unique there and inversion yields the g² interval. All final decimal endpoints above were rounded outwards by integer division. The exact R_TC²/price comparisons and the repaired F4 witness used Fractions throughout. Graph data were checked with integer/set operations and independent reachability. All independent executions completed successfully; no runner files, caches, or output logs were written. The author's scripts containing float displays were not run through their main functions.

Final snapshot check: 2026-10-29 01:10 UTC; `RLARGE_U55.md` remains 609 lines with the same SHA-256 above. This review wrote only `CODEX_REVIEW_RLU.md`; no git operations or source edits were performed.

## Exactly what may be banked

1. **The W-cb♯ conditional deterministic energy bound**, with HW's explicit geometry, (CLS-min), k=0 normalization and level-size conditions. It removes (TC) from that bound. The four R_TC² values, the grid-specific third-entry loss by exactly R_TC², and the incompatibility of (TC) with the existing CL denominator estimate are exact. Other collar-route obligations remain open.
2. **The FI-1 conditional per-level IVT theorem**, and finite-K recursive existence after a sufficiently small bare-coupling choice, given uniform estimates on every trial kernel parameter, continuity, UNIV-1L and the stated γ restrictions. **A-Lip suffices** for unique continuous selection; the corrected saturation example proves that continuity alone does not guarantee it. A-Lip is not necessary. No actual stage regularity or torus-uniform tuning hypothesis is discharged here.
3. **The identification a_ret=(SC2)'s exponent**, the chart-domain distinction, the candidate component-price formula and its Gaussian binding-entry arithmetic, and the exact conditional (L618-δ) comparison. No supplied SC supremum, attained return rate, bounded live prefactor, or live DX nonbinding conclusion is established.
4. **The rational benchmark margin intervals in §4 and the missing exp(38417B₀)**. They replace the old arithmetic only at their declared inputs. No universal ranking of HIST versus (RLF-δ), and no final live margin, may be banked.
5. **The explicit θ-first algebraic order and the absence of new strict-graph cycles or explicit K/T factors from W-cb♯/FI-1**, under fixed uniform inputs. The cutoff and fixed-point SCCs, weak-uniformity obligations, and possible forward dependence n_♯→SC→a_ret remain. The corrected log computations are certified independently; ru55_3b's L2 is not an independent control.
