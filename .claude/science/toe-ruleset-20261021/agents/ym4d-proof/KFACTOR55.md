# KFACTOR55 — T56-4: trace the renormalisation-level factor

## PRE-STATED

UTC time: 2026-10-28 22:29:05 UTC. Written before reading the requested mathematical source passages or deriving an answer.

**OPEN — Question.** Does the source derivation actually contain a constant growing as 25(k−1), where does the level count first enter, and what precisely does that constant multiply? Does the stated scheme absorb it through a coupling-dependent threshold, decay between levels, or asymptotic-freedom running? If not, what is the narrowest sufficient repair for the affected estimate?

**OPEN — Discriminating outcomes.** KF-F1: the alleged factor is absent from the source argument. KF-F2: the estimate carries a level count times a fixed-size smallness parameter, leaving a genuine failure of the claimed uniform bound. KF-F3: the relevant smallness parameter is explicitly of order g_k², so that k g_k² is marginal under a separately justified running law. These alternatives may apply to different estimates; numerical similarity will not identify their hypotheses.

**OPEN — What would change my mind.** An explicit source identity tying the multiplying parameter to g_k², a proved bound on the sum of cross-level operator norms uniform in the number of levels, or a stated cutoff-dependent threshold with the downstream domain and induction checks would defeat a fixed-threshold diagnosis. Conversely, an unweighted sum over levels multiplying a fixed threshold, with no such source bridge, would defeat an asserted automatic absorption. A growing upper bound alone will not be called proof that the underlying operator must grow or that the Yang–Mills construction is impossible.

**CONDITIONAL — Scope and premises.** This is a source audit of T56-4 for the full R^4 OS0–OS3, non-free-theory target, without a mass-gap claim. All inherited PROVEN/REFUTED labels are unverified. PROVEN below will mean a complete local mathematical argument or a directly located textual fact, not validation of the entire programme. Physical asymptotic freedom, literature theorems, and source estimates not independently proved here remain named inputs. No git commands, no edits outside this file, no floating-point computations, and no retained-status changes are part of this handoff.

**PROVEN — Prior exposure record.** Before this pre-statement I read the user specification, the repository workflow, the scoped-worker procedure, and grep hits locating RTARGET §55 and its KF labels. I had not read the requested BFT_A/B, review, or PROOF mathematical passages. Source locations will use headings and search strings because line numbers drift.

## Analysis (incremental)

### 1. Source trail and the quantity being bounded

**PROVEN — Textual provenance.** The source facts below are located by headings and literal search strings, not by presumed stable line numbers. The local worktree is the source snapshot; its relationship to a remote revision was not checked because this assignment forbids git. The scoped-worker procedure is used only for this bounded handoff, without launching a campaign, reviewer, or landing workflow.

**PROVEN — Definitions in BFT_A §1.1–§1.4.** The depth-k composite functional is

\[
 \mathfrak F_k=S_W(U_0)+\sum_{l<k}\kappa_l\sum_c\widehat\phi_c(\overline M^{(l)}(U_l);U_{l+1}),
 \qquad U_l=e^{x_l},\quad U_k=V_k=e^{B_k}.
\]

The source explicitly identifies this as the tree-level exponent **at g = 1**, with N absorbed in the κ_l. It assumes κ_l in a fixed interval [κ_−,κ_+]. The g_j in the next sentence are **gauge transformations**, not running couplings. The relevant definitions are

\[
 x_l^c=L^{k-l}x_l,\quad j_l^c=L^{3(k-l)}j_l,\quad
 \pi_l(j_l)=\|j_l^c\|_\infty,\quad
 \|j\|_{Pc}=\max_{1\le l<k}L^{\theta(k-l)}\pi_l(j_l).
\]

The last formula is BFT_A §7.2, `(Pl-c)`, also used in BFT_B §19.4 and §35.4. Its exponential weight is a requirement on a source, not a decay theorem for that source.

**PROVEN — First level-count step, and the distinct earlier loss.** In BFT_A §3.6 `BA-6`, the older X_c norm produces a residual-source bound of order L^{θ(k−l)}η², or `Ω = Σ_lω_l^{-1} = k` when θ = 0. The proposed full-gradient norm supplies one extra power for that residual source, making its weighted size proportional to L^{−(1−θ)(k−l)}η². This fixes that particular estimate. The remaining plain-current estimate in the same paragraph is

\[
 |\kappa_l(\partial\rho_l^{(2)})^Tr_l|_{\rm own}
 \le 2\kappa_l p_LL^2L^{-3(k-l)}\eta^2.
\]

Multiplication by the defined current conversion L^{3(k−l)} gives

\[
 \pi_l\bigl(\kappa_l(\partial\rho_l^{(2)})^Tr_l\bigr)
 \le 2\kappa_+p_LL^2\eta^2. \tag{1}
\]

Thus the own-unit decay has **already been used up**. The initial table in §3.9 incorrectly calls this row geometric; the source's `GAP 1 (F3)` correction explicitly replaces that description by no level decay in plain-current coarse units. This is the earliest located origin of the surviving plain-current problem. The explicit summation diagnosis is `[RBA2-fix] B3`: the level-0 images cost at most (k−1)η². This predates the session-9/10 corollary and the later session-24/25 summaries.

**PROVEN — Two different commutators must be separated.** The patching term `[A^T, χ]A` in §3.10 is linear in the displacement: its displayed own-unit size is CL³L^{−3(k−l)}η/ℓ, hence its plain coarse size is CL³η/ℓ. It is not a quadratic η² row. The later B3 wording groups it with quadratic remainders; that wording cannot change its degree. Separately, §13.5 `Lemma CR-1` addresses the BCH commutator −[x_{l+1},Q_lx_l]/2, and writes its gradient pairing as a residual-type source s_l^C = (κ_l/2)[x_{l+1},r_l]. That algebra does not by itself repair the cutoff commutator `[A^T,χ]A`.

**CONDITIONAL — Precise surviving nonlinear row (named input: BFT_A Corollary NC and BFT_B §29.4).** The BCH₂ plain current is R_l^B(u)=2κ_l⟨r_l,B_l(x_l,u_l)⟩. The quoted local decomposition is R_l^B=d*W_l+V_l, with

\[
 \|W_l^c\|_\infty\le C L^{-(k-l)}\eta^2,
 \qquad \pi_l(V_l)\le A_V\eta^2,
 \qquad A_V:=2C_{NC}C_{bch}\kappa_+L^2. \tag{2}
\]

Here A_V abbreviates **the coefficient displayed in BFT_B §29.4**, not a newly verified bound for the NC decomposition. The W estimate has summable decay; the V estimate is explicitly `uniform in l`, with no decay. The source contains different formulas named C_NC; no identification between those formulas is needed for this diagnosis. No coupling appears in (1) or (2).

**PROVEN — Fixed field scale in the written theorem.** BFT_A §1.2 defines the data class by ∥B_k∥_D≤ε. In §3.9 `Theorem BA`, s=∥B_k∥_D, C_0=2(1+G_D), and ∥x∥_𝔐≤C_0s; its BFT-1 application sets η=C_0ε. Its displayed admissible ε_0 depends on ρ_0,G,G_D,C, all required to be k-independent. BFT_B §35.6 assumes ∥x∥_𝔐≤η≤η_0. These are deterministic geometric chart radii, with no stated identification η∼g_k or η²∼g_k². The multiplying quantity on this source path is η² (and, for a quadratic Lipschitz bound, η), rather than an established running-coupling factor.

### 2. Exact location of the summation in COF

**CONDITIONAL — Push-down assembly (named inputs: BFT_B Lemma DF-cc and Lemma FT).** Under (CC-0), D(S)=0 as a level-0 function, the source identities in §35.3–§35.4 are

\[
 C(j)=\sum_{l=0}^{k-1}(Q_{str}^{(0\to l)})^T\widehat j_l,
 \qquad \widehat j_l=j_l+h_l^T\psi_l,
\]
\[
 \pi_l(h_l^T\psi_l)\le 2d\sum_{t=0}^l L^{-3(l-t)}\pi_t(j_t). \tag{3}
\]

The first identity is an algebraic regrouping using total divergence zero, not smallness of the individual currents. The second estimate is the source's funnel bound; its proof is not promoted here merely because its heading says PROVEN.

**PROVEN — Push-down scale calculation.** For the straight average in BFT_A `BL-2 (c)`, a fine-link value of Q_str^Tv is L^{−4} times the sum of L coarse-link values. Thus ∥Q_str^Tv∥_own≤L^{−3}∥v∥_own. After l steps,

\[
 \pi_0((Q_{str}^{(0\to l)})^Tv)
 \le L^{3k}L^{-3l}\|v\|_{own}=\pi_l(v). \tag{4}
\]

There is **no remaining decay in l** in (4). In §35.4 `Proposition COF-size`, step 3, the triangle inequality is precisely

\[
 \pi_0(C(j))\le\sum_{l=0}^{k-1}\pi_l(\widehat j_l). \tag{5}
\]

**PROVEN — Summing the displayed inequalities.** For k≥2 let B=π_0(j_0), M=max_{1≤l<k}π_l(j_l), r=L^{−3}, and A_f=1+2d/(1−r). For k=1 set M=0; the upper-level family is empty and contributes nothing. Assuming (3)–(5), finite summation gives

\[
 \begin{aligned}
 \pi_0(C(j))
 &\le\sum_{l=0}^{k-1}\pi_l(j_l)
       +2d\sum_{l=0}^{k-1}\sum_{t=0}^{l}r^{l-t}\pi_t(j_t)\\
 &=\sum_{t=0}^{k-1}\pi_t(j_t)
       \left(1+2d\sum_{u=0}^{k-1-t}r^u\right)\\
 &\le A_f\sum_{t=0}^{k-1}\pi_t(j_t)
 \le A_f\bigl[B+(k-1)M\bigr]. \tag{6}
 \end{aligned}
\]

For d=4,L=3, A_f=1+8/(1−1/27)=121/13 exactly. Inserting (2) therefore costs at most (121/13)(k−1)A_Vη², plus the single level-0 term. This is a bound produced by these inequalities, not a lower bound on the actual response of V(x).

**PROVEN — The failed substitution.** The class-norm route requires ∥j∥_Pc. Formula (2) supplies only

\[
 \|V\|_{Pc}\le L^{\theta(k-1)}A_V\eta^2, \tag{7}
\]

not a k-independent O(η²) estimate. BFT_B §35.6 `Corollary COF-crit` substitutes (2) into §35.5 `Theorem COF` as if the weight in (7) were absent. Using (6) inside the proof improves the resulting exponential bound to a linear count, but does not remove that count. The inherited review's `≍` must be read as an upper-bound computation here: no matching lower bound for the actual nonlinear rows has been supplied.

**CONDITIONAL — Consequence for the curvature bound (named inputs: the remaining COF/YH/LES and residual estimates).** In §35.5(c), the binding term is n²⟨C(j),Y_0^p⟩, n=L^k. Its stated estimate is C_YNπ_0(C(j)): n²·n^{−3}·n=1, with no extra level factor gained. In contrast, the residual-pairing part has Σ_lL^{−2(k−l)}π_l(ĵ_l), a geometric sum. With (6), the displayed COF proof yields a curvature bound of the form [C_base+C_stack(k−1)]η², for constants independent of k and T **if its other named inputs hold**. The k-independent curvature assertion in `Theorem NCE` §36.5(i) is therefore unsupported by that substitution. §36.5(iv) itself says the factor k is untouched. Neither sentence establishes a lower bound on the true nonlinear curvature response.

### 3. Where the number “25” comes from, and what it does not prove

**PROVEN — Textual origin in the inspected sources.** The literal `25(k−1)` is in REVIEW_BFT_B_S9_S10, Part J, `S10-6`; it is not in BFT_A or BFT_B. That review obtains it by approximately optimizing the weighted estimate. Its source coefficient is

\[
 C_C(\theta)=A_f\left(1+\frac1{1-L^{-\theta}}\right),
 \qquad A_f=\frac{121}{13}\quad(d=4,L=3).
\]

Writing n=k−1≥1 and t=θ log L, the factor estimated by that maneuver is

\[
 F_n(t)=A_f e^{nt}\left(1+\frac1{1-e^{-t}}\right).
\]

**PROVEN — Symbolic derivation of its asymptotic size.** For t>0, 1−e^{−t}≤t and e^{nt}/t is minimized at t=1/n: its derivative has the sign of nt−1. Hence F_n(t)≥A_f e n. Conversely e^t≥1+t gives (1−e^{−t})^{−1}≤1+1/t, so F_n(1/n)≤A_f e(n+2). Therefore, if t can vary freely over positive values,

\[
 A_f e n\le\inf_{t>0}F_n(t)\le A_f e(n+2).
 \tag{8}
\]

The review's `≈25(k−1)` is the decimal description of the leading symbolic coefficient (121e/13)(k−1). It is not an exact constant of the Yang–Mills estimate, and it omits A_V and the other response constants. Formula (6) is already a better bound for the aggregation step, with coefficient 121/13 instead of 121e/13. No decimal evaluation is needed here.

**PROVEN — The optimization is not legal at fixed Hölder exponent for arbitrarily large k.** Theorem COF assumes 0<α<θ<1. Its α is fixed in a uniform theorem. The candidate θ=1/((k−1)log L) eventually violates θ>α. Indeed L^{θ(k−1)}≥L^{α(k−1)}, so the weighted-norm estimate itself stays exponential for fixed α. Allowing α to tend to zero changes the output norm and would require new control of all α-dependent constants. The linear O(k) replacement is obtained from the unweighted sum (6) inside the proof, **not** from a uniform optimization of the full COF theorem. This corrects the precision of S10-6 while preserving its principal missing-decay diagnosis.

**PROVEN — Sharpness of the summation map, not of the nonlinear curvature response.** Choose a fixed unit Lie-algebra component a in one link orientation, let j_0=0, and set j_l=L^{−3(k−l)}a constant on level-l links for every 1≤l<k. These currents have π_l=1 and d*j_l=0. The identity Q^T=Q_str^T−h^Td* in BFT_A `BL-2 (c)` reduces their push-down to the straight one. Its explicit formula used in (4) is an equality on constants. Thus

\[
 C(j)=(k-1)L^{-3k}a,\qquad \pi_0(C(j))=k-1.
\]

They satisfy (CC-0) because every level divergence vanishes. Consequently (CC-0) alone cannot turn the map from unweighted per-level sup bounds to π_0(C(j)) into a uniform map. This witness is **not** claimed to be an admissible BCH₂ remainder of a single background, or to force nonzero curvature: constant forcing can act in the zero-momentum sector. It proves only that a uniform aggregation estimate requires additional structure beyond these slot bounds and (CC-0).

### 4. Proposed absorption mechanisms

#### 4.1 Decay between levels

**PROVEN — Geometric convolution is not geometric decay to the top.** The kernel L^{−3(l−t)} in (3) has a bounded row sum, but for an input of size M on every level, its output is still of order M on every level. Summing those outputs is (6). Similarly, the own-unit L^{−3l} in (4) cancels the coarse-unit conversion exactly. Neither is an unspent L^{−δ(k−l)} gain.

**CONDITIONAL — Decay that does work for other pieces (named source inputs).** BFT_A Corollary NC's W part produces a response bounded level by level by C(k−l+1)²L^{−(1−α)(k−l)}η²; BFT_B COF's residual pairing produces L^{−2(k−l)}π_l(ĵ_l). Both sums converge for fixed 0<α<1. They do not price the remaining level-0 plain-current term. BFT_A §23.11 `Theorem CO-B` also displays a geometric sum for BCH₂ rows, but §23.12 explicitly restricts it to **level-wise co-closed BCH₂ rows**; the V_l in §29.4 are not assumed level-wise co-closed. Total (CC-0) does not supply that hypothesis.

**PROVEN — Three distinct source statements named SPD must not be conflated.** BFT_A `[RBA2-fix] B4` defines W2 as decay of the **smooth component of a split** carried from l to m. Section 13.6 `Proposition SPD` instead displays the carrier inequality

\[
 \bigl|Q_{str}^{(l\to m)}R_l^B\bigr|_{own}
 \le C_{SPD}\kappa_l L^{-3(k-l)}\eta^2. \tag{9}
\]

With its specified carrier normalization the coarse size is

\[
 L^{3(k-m)}L^{2(m-l)}L^{-3(k-l)}\eta^2
 =L^{-(m-l)}\eta^2. \tag{10}
\]

Equation (10) is exact exponent arithmetic, conditional on the carrier bound (9). It is different from the downward transport in (4). The source's `[RBA3-fix] B2'` expressly says W2 needs SPD **plus (SB)**, while (SB) is open. Section 13.7 identifies the gap: passing from the carrier to the recursive orthogonal split requires a sup-norm bound on a Gram inverse and Hodge projection. Treating the label “SPD: PROVEN” as that missing bridge would repeat an already recorded source error.

**CONDITIONAL — Alternative carrier route (named inputs: SPD and PW-ℓ¹).** BFT_A §33.7 `Proposition SR` shows how a direct dual estimate could avoid the orthogonal split: its per-level sup contribution is bounded by C(t+1)L^{−t/2}η², t=k−l. But its proof explicitly assumes both representative ℓ¹ control and an ℓ¹ gradient bound, called PW-ℓ¹; its scope is the sup output, with further work stated for Hölder control and off-critical iterates. This is a proposed repair mechanism, not an established absorption in COF-crit. The review's phrase “conditional on SPD” is therefore too short: the missing carrier-to-response bridge and its non-co-closed scope must also be named.

#### 4.2 A shrinking threshold and asymptotic-freedom running

**PROVEN — What the displayed contraction would require.** If a quadratic response R_k satisfies

\[
 \|R_k(x)\|\le Ck\|x\|^2,\qquad
 \|R_k(x)-R_k(y)\|\le Ck(\|x\|+\|y\|)\|x-y\|,
\]

then on a ball of radius η its Lipschitz bound is 2Ckη. Making that bound at most a fixed q<1 requires η≤q/(2Ck). Thus η=O(k^{−1/2}) bounds the **absolute quadratic error** kη², but does not control its ratio to the linear scale η or the contraction constant. For the same reason, merely replacing the radius by a coupling-sized radius is not automatically a contraction repair. This is an implication about the displayed quadratic estimate; it does not assert a necessary radius for a sharper, presently unwritten estimate.

**CONDITIONAL — AF comparison with explicit normalization.** Suppose, as a separate input, an ultraviolet-depth coupling g_[k] satisfies

\[
 g_{[k]}^{-2}=a+b\,k\log L+o(k),\qquad a\ge0,\quad b>0.
 \tag{AF}
\]

The bracketed index distinguishes this hypothetical UV depth from the source's coarsening index and its gauge transformations g_j. For fixed c>0 the algebra gives:

| Threshold in the actual x norm | Absolute stacked error kη_k² | Relative/Lipschitz scale kη_k |
|---|---|---|
| η_k=ε, fixed | kε² | kε |
| η_k=c g_[k] | tends to c²/(b log L) | grows as c√(k/(b log L)) |
| η_k=c g_[k]² | tends to 0 | tends to c/(b log L) |

All asymptotic entries in this table are **CONDITIONAL on (AF)**. A threshold g_[k] times an increasing logarithmic factor makes the middle row larger still. A g_[k]² threshold is only marginal for contraction: the limiting constant must actually be smaller than the needed smallness bound, and b and the other constants can depend on L. Increasing L has not been shown to improve their ratio.

**PROVEN — Restoring an overall coupling does not insert a missing g².** If the geometric action is S_g(x)=g^{−2}𝔉(x), its Hessian at zero is g^{−2}H and its gradient remainder is g^{−2}N(x). On the same invertible gauge-fixed space, their product in the Newton equation is (g^{−2}H)^{−1}g^{−2}N(x)=H^{−1}N(x). For x=gA the homogeneous quadratic term N_2 in the A equation instead has one power g: g^{−1}N_2(gA)=gN_2(A); higher-degree terms have their corresponding higher powers. Thus a convention change alone cannot turn the source's kη contraction loss into kg². A different running, renormalized estimate would need its own statement and proof.

**PROVEN — What the inspected text does and does not connect.** Neither BFT_A's chart/data assumptions nor BFT_B COF-crit connects η to a coupling. PROOF's `L4a-flow` paragraph explicitly distinguishes coarsening steps from UV resolution; its `L5` paragraph reports fixed ε_0 and ε_1 in certain variables and an alternative g_kε_1/γ_k normalization. These are **textual reports, not verified literature inputs in this note**. No theorem from Balaban is imported here, and no claim about his exact thresholds is inferred from those unreliable paraphrases. To use a coupling-dependent threshold in this lane one must first translate it into ∥x∥_𝔐 and check that the required backgrounds and fluctuation domains still lie in the resulting ball. That translation is absent from the traced corollary.

**PROVEN — A running value at each summation level is a different problem from k times one value.** Even assuming π_l(V_l)≤C g_{[k-l]}², one obtains Σ_{q=1}^{k−1}g_[q]², not (k−1)g_[k]². For the exact model g_[q]²=1/(a+bq log L), q≥1,

\[
 \frac{H_n}{a+b\log L}
 \le\sum_{q=1}^n\frac1{a+bq\log L}
 \le\frac{H_n}{b\log L},\qquad H_n=\sum_{q=1}^n\frac1q.
\]

The lower inequality follows from a+bq log L≤q(a+b log L); the upper from a+bq log L≥bq log L. H_n diverges: each block 2^{r−1}<q≤2^r contributes at least 1/2. Hence per-level AF factors of order 1/q alone are still nonsummable. The actual mapping of coupling indices to source levels is essential. This exact counterexample to an automatic summability argument is not a claim that the source's V_l have these sizes.

### 5. Comparison with CURV-F2″

**PROVEN — Source distinction.** In PROOF, search `[R22-fix S22-5] Failure mode CURV-F2″`. That passage concerns HG-ind's recursive first-order localization error, with

\[
 \theta_0=\theta\prod_j(16\kappa_j\mathfrak c_\infty^{(j+1)})^{-1}.
\]

Its θ is a **localization tolerance**, not COF's exponent in the source weight L^{θ(k−l)}. The paragraph connects θ_0 to a localization length ℓ_θ and then to a chart radius ε_θ. This is a different derivation from (5), although both can leave only a radius of order 1/k in their respective proof routes.

**CONDITIONAL — The 1/k deduction (named inputs: that cascade and its localization/radius bounds).** Suppose each amplification factor is at least A_*>1, a localization choice requires D≥(2/m_1)log(C/θ_0), ℓ_θ≥D, and ε_θ≤c/ℓ_θ, with fixed positive m_1,C,c. Then

\[
 \theta_0\le\theta A_*^{-k},\quad
 D\ge\frac{2}{m_1}\bigl(k\log A_*+\log(C/\theta)\bigr),\quad
 \varepsilon_\theta=O(k^{-1}).
\]

This checks the stated mechanism conditional on its premises. It does not verify the source's bounds on all amplification factors. It also does not show the best possible radius of the actual background problem is O(1/k). Shrinking a threshold to accommodate a defective route is a loss of the desired uniform domain; it is not evidence that an AF mechanism has absorbed that loss.

### 6. Minimal repair and its exact scope

**CONDITIONAL — A sufficient repair for the cited aggregation estimate (named inputs: COF's DF-cc/FT, YH/LES and residual bounds).** Work in COF's critical-point source setting, including (CC-0). Suppose the actual nonlinear rows satisfy, with constants independent of k,T,

\[
 \pi_0\!\left(\sum_{l=0}^{k-1}(Q^{(0\to l)})^TV_l(x)\right)
 \le C_J\eta^2,\qquad
 \max_l\pi_l(V_l(x))\le A_V\eta^2. \tag{J-unif}
\]

Then the binding COF sup term is bounded by C_YNC_Jη² under its quoted YH input. Equation (3) makes max_lπ_l(ĵ_l)≤A_fA_Vη². The residual part is therefore bounded by its geometric factor, and the local Hölder step §35.5(d) uses the first bound in (J-unif), plus the separately bounded top residual. Thus, conditional on the other COF inputs, (J-unif) removes **this** count from both the sup and Hölder parts. It is a direct, sufficient replacement for the failed use of the Pc norm, and allows signed cancellation instead of insisting that every V_l be small separately. It is not proved for the actual V_l here.

**PROVEN — A stronger but simpler sufficient input.** If for some fixed δ>0 the actual rows have π_l(V_l)≤A L^{−δ(k−l)}η², l≥1, and π_0(V_0)≤A_0η², then

\[
 \sum_{l=1}^{k-1}\pi_l(V_l)
 \le \frac{A}{L^\delta-1}\eta^2,
 \qquad
 \pi_0(C(V))\le A_f\left(A_0+\frac{A}{L^\delta-1}\right)\eta^2
\]

under (3)–(5). This proves (J-unif) as an implication. The corresponding difference estimate must hold for nonlinear iteration. A proof of W2 for the actual smooth components, together with a uniform response estimate for the rough components, is another possible implementation. The carrier inequality (9) alone is not that implementation.

**OPEN — Minimal substantive obligation.** Establish a uniform estimate for the combined current in (J-unif), or a uniform direct curvature pairing/local oscillation estimate that bypasses it, using the actual BCH/soft-row structure. The constant-current example only excludes a deduction from general unweighted slot sizes; it leaves this structural cancellation entirely possible. For the full construction, the extension needed is a uniform nonlinear **difference** estimate on the iteration domain, with the required source projection and gauge terms controlled away from critical points. A bound valid only at already-existing critical points supplies regularity, not their construction.

**CONDITIONAL — Immediate honest repair of the written corollary.** Retain only `[C_base+C_stack(k−1)]η²` for its curvature estimate, conditional on NC, DF-cc/FT, YH/LES and the other COF inputs. Preserve the separately summable pieces with their own hypotheses. For a fixed-depth contraction that uses the corresponding quadratic Lipschitz estimate, a radius η_k≤c/k is sufficient to control this contribution. It does not deliver the claimed common small-field domain as k→∞, and it does not remove the independent off-critical, background, large-field, OS, or non-freeness obligations.

**PROVEN — Why the count is upstream of the root-charge repairs in this proof.** Equation (6) was obtained after imposing (CC-0), so the root-charge term of COF-res is already zero. The unweighted V bounds still give the level sum. Supplying TENT-Q, NEUT-box or Y-sup^loc therefore cannot, simply by the displayed COF substitutions, repair the count. A new theorem involving those inputs could do more, but that would be a new estimate rather than the existing implication.

### Author checks

**PROVEN — Checks performed, completed 2026-10-28 22:38:26 UTC.** I reread the note and the binding COF sup/Hölder steps. A plain `python3 -I -B` calculation using only `fractions.Fraction` checked (6)'s finite double-sum regrouping and bound, and the constant-current equality, for L∈{3,5,9}, k∈{1,…,9}: 27 choices, all passed. The test used π_0=2/7, π_l=3/11 for l≥1 for the sum bound, and unit coarse constants for the sharpness identity; it also checked A_f(4,3)=121/13 exactly. These are arithmetic spot checks of the written general proofs, not a numerical proof of a source lemma. No source runner, floating-point computation, git command, external literature theorem, or edit outside this deliverable was used. The work has no independent fresh-context reviewer; its scientific source inputs remain conditional as labelled.

### 7. Ranked conclusion against the pre-stated failure modes

1. **PROVEN — KF-F2 is the source-level diagnosis.** The cited proof route pays a level count times the fixed geometric quantity η², and its quadratic Lipschitz bound would pay kη. The source does not establish k-uniformity on the fixed chart. This is a genuine non-uniformity of the available bound and a missing proof obligation, not a theorem that the actual nonlinear response diverges or that the full Yang–Mills target is impossible.
2. **PROVEN — KF-F1 is rejected for the level-count mechanism, with a numerical qualification.** The count is visible in BFT_A's plain-current scaling and B3, and in BFT_B COF-size step 3. The literal `25(k−1)` is a review-derived asymptotic prefactor, not an intrinsic or sharp source constant; the direct aggregation bound is (121/13)(k−1) times the row-size coefficient at d=4,L=3. The full response has further constants.
3. **CONDITIONAL — KF-F3 describes a possible additional normalization, not the cited theorem.** If the quantity multiplying k were independently proved to be g_[k]², (AF) would make kg_[k]² approach 1/(b log L), only marginally. No such identification is supplied for this row. Setting η∼g_[k] would make the absolute quadratic term marginal but still leave kη growing; summing actual per-level g_[q]² can also diverge logarithmically.

**OPEN — Least certain point.** Whether the actual non-co-closed BCH₂ remainder family, with its criticality/Ward identities and carrier cancellations, satisfies a direct uniform estimate that the slot-by-slot bounds miss. No lower-bound example for that nonlinear family or for its curvature response has been established here. This note does not independently validate the inherited NC, SPD, YH, COF or gauge-fixing lemmas, nor resolve the full R^4 OS0–OS3 and non-free-theory theorem.


---
**[LEAD] Note.** This Codex (gpt-6-astra, max) run COMPLETED before the owner's role split (Opus 5.5 does the work, Codex reviews). Step 4 is reassigned to an Opus 5.5 worker as primary, who forms a view independently and only then compares with this file. This file stands as a completed Codex analysis, unreviewed. (An earlier version of this note wrongly said the run was stopped.)
