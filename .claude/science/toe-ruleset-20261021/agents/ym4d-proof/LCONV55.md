Reviewer model: claude-opus-5-5

# LCONV55 — Is the multiscale small-field chain convex? (node A residual (LC°))

UTC start: 2026-10-29T01:21:17Z
Author: Opus 5.5 worker (claude-opus-5-5). Append-only. No git. Writes only this file and `checks/lc55_*`.

## PRE-STATED (written before any derivation)

Targets:
- T1 (multiscale claim). Decide whether the lowest Hessian eigenvalue of the gauge-fixed soft-scheme
  chain action, on the MULTISCALE small-field region (smallness at every level), is bounded below by
  c * (free Laplacian) with c > 0 uniform in k and T. Identify which constraint (level, threshold)
  removes the lattice Nielsen-Olesen (NO) negative mode, and whether the lane's actual thresholds
  (epsilon_1 et al., in the order SMALLNESS_DAG.md gives) are small enough.
- T2 (coordinates). Decide whether convexity (LC-2') is provable in the exponential/axial coordinates
  of the small-field core, or whether background-covariant coordinates around the critical tower
  (BFT-0/1/2 on C_glob, GV55.md) do better.
- T3 (LC-3'). State the large-field Peierls bound node A needs and what RLARGE / HW / PLD supply.
- T4. If convexity fails on node A's region, give the smallest modification of the region or of the
  tilt that restores it, and check whether node A's consumers tolerate it.

What would count as a refutation of the multiscale claim ("smallness at every level restores convexity"):
- an explicit configuration inside the multiscale small-field region (all levels' constraints satisfied
  at the lane's thresholds) with a Hessian direction of negative Rayleigh quotient, or a Rayleigh quotient
  that is not bounded below by a positive constant times the free Laplacian uniformly in k, T;
- or an exact scaling argument that the NO threshold is not crossed by the constraints at any level
  (i.e. the constraint at every level permits a background strength above the NO threshold for some
  mode the constraint does not control).
What would count as CONFIRMING it: an exact (rational/symbolic) lower bound on the Hessian quadratic
form, valid on the whole multiscale region at the lane's thresholds, with the constraint that does the
work identified; plus a designed-FAIL control (a configuration that violates exactly that constraint)
in which the negative mode reappears.
A precise statement of what is missing counts as a first-class result if neither can be settled.


## RESUMED 2026-10-29T02:45:53Z

Resumed by claude-opus-5-5 (same model ID as the first line; no extra model line needed). State found on disk: the
previous run left only the model line, title, UTC start and the PRE-STATED block (35 lines); no derivation, no
findings and no `checks/lc55_*` files exist. So there is no unreviewed draft step to re-verify; errata section
reserved below in case later findings need it. Work continues from the PRE-STATED targets T1-T4.

## Errata (reserved; append-only)
(none yet)

## 0. Inputs read, Codex verdicts used, method (written 2026-10-29 ≈03:35Z, before any criteria file or exact check)

**Read (files as on disk 02:45-03:35Z; located by string).** The brief (`queue/go_LCONV55.md`, all) and REVIEW_BRIEF_55.md
(all). CODEX_REVIEW_NRES.md (all 478 lines; complete: it ends with "Exactly what may be banked"). CODEX_REVIEW_NODEA.md, its
"Exactly what may be banked" section. NODEA_RES55.md (all 574 lines). NODEA55.md l.1-130 (setting, A.1-A.2). SMALLNESS_DAG.md §1
and Appendix A rows `eps1`, `eta_q`, `eps_loc`, `a_bad`. RLARGE.md §0 ("Indicators", "Thresholds", "The exact chain"), §2.1-§2.4
("Bad and collar-bad cubes"), §3.3 ("(SDP)^A_θ"). HIST.md §0 ("The chain measure"), §3 ("φ_M(V) := N⁻¹[Re tr(W_0⁻¹M) − Re
tr(V⁻¹M)]", (3.0), Lemma PM, Lemma KQ), "Quietness" (l.197). PLD.md "M̄_c(U) := |Γ_c|^{-1}Σ_{(σ,y)}T^σ_y(U)" (§17.3), "ε_V =
max||log(V_cS_c(U)^{-1})||", "𝔄(U_0, …, U_K) := u_0Σ_ps(U_0(p))". PROOF.md §1 "S4 Averaging (L1)" and "S4' [S3] Order-averaged
averaging". GV55.md §0-§3 ("Theorem BFT-E (assembly)", §3.3 "What Theorem BFT-E does not give"). HW.md §0 and §6 ("local coupling
response"). Corpus (third-party, read as data; cited by id + equation, never copied): 1108.1335 eqs. (193)-(196) and Lemma 34
eq. (378); 1212.5562 Definitions 3.2 and 3.5; 2204.08252 §1.2 eqs. (11)-(12), §1.4 eq. (19), Theorem 1, eq. (100).
**Not read:** BFT_A/B, FLOW, SF, EXISTENCE, PLD/HW beyond the strings above. No claim below rests on an unread file.

**Codex verdicts used, and whether I agree.**
| Codex item (CODEX_REVIEW_NRES, "Exactly what may be banked") | Codex verdict | mine |
|---|---|---|
| 5: non-convexity of the specified finite Wilson patches at plaquette norms 2/√17, 2/√65; "Arbitrarily small thresholds, multiscale convexity, and the full normalized-chain conclusion are NOT-VERIFIED" | CONFIRMED / NOT-VERIFIED | **agree** on both halves; §B uses the witnesses' geometry (constant field, fixed boundary, critical point), not their thresholds |
| 2: BL-TILT under its complete H-convexity, D1-D4, positive-normalizer hypotheses (repaired convex-domain proof) | CONFIRMED | **agree**; used only as the consumer that (LC-1′) was meant to feed |
| §2.3 "plain log-concavity alone is insufficient … quantitative H-convexity, D1-D2, the strict domination margin, mean zero, convex support and the local rank bound" | NOT-VERIFIED as actual-chain application | **agree**; this file shows the first of those hypotheses fails on the lane's region |
| 6: Proposition NU as a finite-volume implication; "NU-ii/LC-3′ equivalence NOT-VERIFIED" | CONFIRMED / NOT-VERIFIED | **agree**; used in §F |
| §3 colour invariance gives mean zero only in an equivariant chart for the complete invariant law; "Fixing arbitrary boundary fields … destroys global conjugation invariance of each conditional law" | CONFIRMED with qualification | **agree**; relevant to (LC-1′)'s conditional form, §F |
CODEX_REVIEW_NODEA item 5 (Gaussian convex-core theorem): agree; not re-derived here.

**Method and an exploration disclosure.** Before writing any criteria file I ran float-only exploratory scripts in my scratchpad
(`.../scratchpad/lc55_explore/stripe_float*.py`, `box_float.py`, `box_exp_float.py`; outside the repository) to locate candidate
configurations. **No verdict below rests on them.** Every number used as evidence comes from a `checks/lc55_*` script run after
its criteria file was written, in exact rational arithmetic (plain python `fractions`; rigorous rational intervals where an
angle is not rational-parametrised). Floats appear in those scripts only to *propose* a direction, which is then rounded to
rationals and certified exactly.

*[Timestamp correction: "§0 … written ≈03:35Z" was an estimate; `date -u` printed 03:32:32Z right after that append.]*

---

## A. The chain's Hessian along "following" directions reduces to the bare Wilson Hessian (Lemma FOL): PROVEN-HERE

**Objects (verbatim sources).** Chain potential 𝔄(U_0, …, U_K) := u_0Σ_ps(U_0(p)) + Σ_{m<K}κu_mΦ_m(U_m, U_{m+1}),
Φ_m(U, V) = Σ_cφ_{M̄_c(U)}(V_c) (PLD "𝔄(U_0, …, U_K) :="; HW §0); φ_M(V) := N⁻¹[Re tr(W_0⁻¹M) − Re tr(V⁻¹M)] ≥ 0 with W_0(M) a
maximiser of W ↦ Re tr(W⁻¹M) (HIST §3); M̄_c(U) := |Γ_c|⁻¹Σ_{(σ,y)}T^σ_y(U), the arithmetic mean of the S4′ transporters (PLD
§17.3; PROOF §1 "S4′"). The chain density is W = e^{−𝔄}·Π_{m,c}𝒩_m(M̄_c(U_m))⁻¹, 𝒩_m(M) := ∫e^{−κu_mφ_M}dV (HIST (3.0)). In a
chart with Lebesgue coordinates the potential of the chain is 𝔄 + Σlog𝒩_m(M̄_c(U_m)) + (chart Jacobians).

**Definition (following set).** 𝓕 := {(U_0, …, U_K) : U_{m+1}(c) = W_0(M̄_c(U_m)) for every m < K and every level-(m+1) link c},
taken on the open set where every M̄_c is within δ_0 = min{1/(640N), 2/N³} of SU(N), so that W_0 is unique and real-analytic
there (Lemma PM: the maximiser is within 3δ of S; for SU(2), M̄ is a positive multiple of a unit quaternion and W_0(M̄) = M̄/|M̄|).
A tangent vector τ = (τ_0, τ_1, …) at p ∈ 𝓕 is a *following direction* if τ_{m+1} = D(W_0∘M̄)_p(τ_m) for every m.

**Lemma FOL.** Let p ∈ 𝓕 and τ a following direction at p. In any C² chart in which each level's links are coordinates, and
along any C² curve γ with γ(0) = p, γ′(0) = τ,
  (i) d²/dt² [Σ_mκu_mΦ_m(γ_m(t), γ_{m+1}(t))]|_{t=0} = 0;
  (ii) hence d²/dt²(𝔄∘γ)|_0 = u_0·d²/dt² S(γ_0(t))|_0 with S := Σ_ps(U_0(p)), and the chain potential's second derivative along γ
       equals that plus the second derivative of Σlog𝒩_m(M̄_c(γ_m(t))) + (chart Jacobians), neither of which carries a factor u_m.
*Proof.* Fix m, c and put g(U_m, U_{m+1}) := φ_{M̄_c(U_m)}(U_{m+1}(c)). g ≥ 0, g is C² near p, and g = 0 on 𝓕 (φ_M(W_0(M)) = 0).
A C² function with a minimum value at p has ∇g(p) = 0, so its second derivative along any C² curve through p is the
chart-independent quadratic form Hess g(p)[γ′(0), γ′(0)] (the term ⟨∇g(p), γ″(0)⟩ vanishes). 𝓕 is locally the graph of the
real-analytic map U_m ↦ W_0(M̄(U_m)), hence a C² submanifold, and τ ∈ T_p𝓕 by definition; taking a curve inside 𝓕 with tangent
τ shows Hess g(p)[τ, τ] = 0. Sum over m, c. (ii) is (i) plus the definition of 𝔄. ∎
*Reading.* Along following directions the kernels contribute **no curvature at all**; the only u-carrying curvature is the bare
Wilson term u_0S at the finest level. So any lower bound "H ≥ (1 − δ)M" for the chain on a region containing a point p ∈ 𝓕 must
already hold, along following directions, for **u_0·Hess S(U_0) + O(1)**. In particular, if Hess S at p's level-0 field has a
direction τ_0 with Hess S[τ_0, τ_0] ≤ −c|τ_0|², then the chain potential at p has a direction with second derivative
≤ −u_0c|τ_0|² + C_𝒩|τ|², where C_𝒩 bounds the u-free terms (normalisers, Jacobians) and |τ|² ≤ C_D|τ_0|² (C_D bounds the
linearised blocking, a fixed geometric constant); this is **negative as soon as u_0c > C_𝒩C_D**. Since H ≥ (1 − δ)M ≥ 0 is
violated by any negative direction, no δ < 1 survives. *(C_𝒩 and C_D are fixed functions of N, L, κ, independent of u; I do not
evaluate them. The lane's quantifier order chooses every threshold before g_0 (SMALLNESS_DAG §7: "… → ε_1 → … → g_0"), so
u_0 = 1/g_0² can be taken as large as needed at fixed thresholds; RLARGE §0 even records the requirement "g² ≪ ε_1²·10⁻¹³".)*
*Status.* Elementary; PROVEN-HERE. It is the step that turns any non-convexity of the bare Wilson action on the level-0
projection of the region into a non-convexity of the **chain** on the region.

---

## B. The Nielsen–Olesen (constant-field) mode IS killed by the multiscale cut — at the level whose blocks fit the mode

**The witnesses being tested.** NODEA_RES55's G5 (Codex NRES item 5, CONFIRMED) are **constant-field critical points of a
fixed-boundary patch**: U_1(x) = w^{x_2}-type Landau gauge, every plaquette e^{iασ_3}, α = 2arctan τ with τ = 1/4, 1/8; plaquette
norms 2/√17, 2/√65; negative Rayleigh quotients −1.07, −0.52. At a critical point the Hessian's inertia is chart-independent,
so these are genuine non-convexities of the bare action; Lemma FOL turns them into non-convexities of the chain.

**B1. Coarse angle of a constant field: L²α per level, exactly (PROVEN-HERE, elementary).** Let U be abelian (values in the
σ_3-torus) with constant plaquette angle α on a region containing the blocks in question. Lattice translations act on U as gauge
transformations (constant field), the S4′ family Γ_c is translation-covariant, and M̄_c and W_0 are gauge-covariant (PLD §17.3:
"U_{k-1} and the kernel centres transform by the same h(x_e)·h(y_e)^{-1}"). Hence the following field V = W_0(M̄(U)) is again
abelian and translation-invariant up to gauge, i.e. a constant field, and its plaquette phase is
arg(M̄_1) + arg(M̄_2) − arg(M̄_3) − arg(M̄_4) for the four sides. Write arg M̄_c = (phase of the straight centre transporter
S_{c_X}) + κ_c, where κ_c := arg(mean_{σ,y} e^{i(φ^σ_y − φ_{S})}) depends only on the direction of c by translation covariance (the
loop c_X → y → y+Le_μ → c_Y → c_X encloses a flux that is the same for parallel links of a constant field). The κ's of opposite
sides cancel, and the four straight centre transporters enclose the L×L square of block centres: **coarse angle = L²α (mod 2π)**.
Iterating, the level-j following field has angle L^{2j}α as long as no wrap occurs, and none occurs while L^{2j}α < 2π − (it is
reached from below in steps of ×L² starting under the level-(j−1) threshold).

**B2. Which constraint kills it, and with what margin (ARGUED: B1 exact + a numerical NO threshold).** In a float exploration
(disclosed, §0; `no_const.py`) the fixed-collar n×n constant-field patch first acquires a negative gauge-horizontal Riemannian
eigenvalue at **n²α ≈ 3.2 (α = 0.2, n = 4), 3.6 (α = 0.1, n = 6), 3.2 (α = 0.05, n = 8)** — the familiar continuum statement
that the NO mode needs a flux of order one through its support (magnetic length ≲ patch size). If the patch lies in the
multiscale small-field region, every level-j plaquette formed inside it has angle L^{2j}α below the level-j threshold t_j
(t_j ≤ η_q ≤ ε_1/(2L²), RLARGE §0 / HIST "Quietness"). Take j* := the largest j with 2L^j ≤ n (two level-j blocks per side fit);
then n < 2L^{j*+1} and **n²α < 4L²·L^{2j*}α < 4L²t_{j*}**. So **the level-j* cut (blocks of side L^{j*} ≈ n/L ≈ the magnetic
length up to a factor L) kills the constant-field NO mode whenever 4L²t < c_0 ≈ 3** — i.e. t ≲ 0.09 at L = 3. The lane's
thresholds (ε_1 ≲ 6.7·10⁻⁴⁰, RLARGE §0 "Current ε_1 ceiling"; t ≤ η_q ≤ ε_1/(256NA_d)) satisfy this by ~40 orders; even the
"illustrative" ε_1 = 0.5 gives η_q ≤ 0.028 and 4·9·0.028 ≈ 1.0 < 3. The G5 witnesses themselves are outside the lane's region
twice over: their fine plaquettes (0.485, 0.248) exceed ε_1 by 40 orders, and their blocked plaquettes exceed their fine ones
(Codex NRES §4.2: blocked norms² 2.60, 3.24).
*What is not proven.* A positivity theorem "constant-field patch with flux < c_0 ⇒ horizontal Hessian ≥ 0" is not written (only
the numerical threshold); B2 is therefore ARGUED. It is also beside the main point, because §C shows that **the NO mechanism is
not the only source of negative curvature**, and the other source is invisible to every coarse level.
*Verdict on NODEA_RES55's specific argument* ("the curvature seen by a mode of size ℓ is ≲ ε_1/ℓ² against a free Hessian ≍
1/ℓ²", §3.4 table): **CONFIRMED as to the constant-field (first-order, net-flux) mechanism** (B1 exact, B2 ARGUED); its conclusion
"H-convexity with δ = O(ε_1) … to hold there" is **REFUTED** in §C — the estimate controls only the first-order term in the
background, and first order is not where the negative curvature comes from.

---

## C. The stripe: a coarse-invisible configuration at which the chain is not convex (the multiscale claim is REFUTED)

### C0. The configuration
**Stripe S(P, β)** (d = 4, SU(2); P odd, P | L): every link is the identity except U_2(x) = exp(i a(x_1 mod P) σ_3), with the
centred antisymmetric pattern a(c) = 0 at c = (P−1)/2, a(c−1) = +β, a(c+1) = −β, a = 0 elsewhere (P = 3: (β, 0, −β)), and
β = 2arctan τ (τ rational, so everything is exact). Plaquette angles θ(x_1) = a(x_1+1) − a(x_1) ∈ {0, ±β, ±2β}: a fine-scale
field of size β whose flux through every aligned L-block is **exactly zero**. Physically: alternating sheets of chromomagnetic
flux one or two lattice spacings wide, invisible to every blocking.

### C1. It lies in the multiscale small-field region with every coarse level exactly trivial (check lc55_1: PASS)
`checks/lc55_1_criteria.md` (md5 c035cba8…, written 03:39:00Z before the script) → `checks/lc55_1_region.py` (706e03a1…) →
`checks/lc55_1_out.txt` (16 s, exit 0). For L ∈ {3, 5}, τ ∈ {1/10, 1/1000}, on the fine torus of side 2L: every S4′ transporter
T^σ_y (all 24 axis orders, all L⁴ points, one coarse link per direction plus a translated spot check) lies in the σ_3-torus;
**every kernel centre M̄_c is a positive real scalar** (r_c = 1 for μ ≠ 2; e.g. r_c = 2733299/3090903 for μ = 2 at L = 3,
τ = 1/10), so W_0(M̄_c) = 1; **every straight centre transporter S_{c_X} = 1**. Hence the following level-1 field is the identity
on every link, so is every coarser following field (transporters of the identity field are the identity), every coarse
plaquette is 1 and every mismatch ‖V_c − W_0(M̄_c)‖ and ‖V_c − S_c(U)‖ vanishes. Level-0 record: 2 − tr U_p ∈ {0, 4τ²/(1+τ²),
16τ²/(1+τ²)²}, i.e. ‖1 − U_p‖_op ≤ 2 sin β. **Controls fired:** C1a (pattern (β, 0, 0): M̄ for μ = 2 has σ_3-part
580060/3090903 ≠ 0) and C1b (period 2 at L = 3: centres not scalar and 16 coarse plaquettes with 2 − tr V_P > 0).
**Membership (CONFIRMED, exact + the analytic induction):** the stripe is defect-free at every level as soon as
2 sin β < min{η_q, ε_loc/2} (level-0 quietness and collar thresholds, RLARGE §0, HIST "Quietness"); every coarse condition holds
with equality-free margin (all coarse plaquettes and mismatches are exactly 0). **No coarse threshold, however small, excludes
it.** For the region with general odd L use P = L (or P = 3 when 3 | L).

### C2. The gauge-quotient (Riemannian) Hessian of the bare action is negative there, at second order in β, for every small β
### (check lc55_2: all gates PASS)
`checks/lc55_2_criteria.md` (28edda0b…, 03:39:00Z) → `checks/lc55_2_propose.py` (825da121…; numpy, **proposals only**) →
`checks/lc55_2_proposals.txt` → `checks/lc55_2_certify.py` (86ad8059…; plain python `fractions`) → `checks/lc55_2_out.txt`
(8.7 s, exit 0, stderr empty).
*What is computed.* The Riemannian Hessian of S = Σ_p(1 − ½tr U_p) for the bi-invariant metric (second derivative along the
geodesics U_ℓ e^{itv·σ}), restricted to **horizontal** vectors (orthogonal to every gauge-orbit direction ξ(λ)_ℓ =
Ad_{U_ℓ⁻¹}λ(x) − λ(y), λ on non-collar sites). This is the Hessian of the action **on the gauge quotient** — chart-free and
slice-free: for a Riemannian submersion the quotient Hessian of an invariant function is the total-space Hessian on horizontal
lifts, with no gradient correction. It is the quantity any Riemannian Brascamp–Lieb / Bakry–Émery argument, and any
background-covariant normal-coordinate chart at the point, would use.
- **G2a (reduced torus, every 0 < τ ≤ 1/10; P ∈ {3, 5, 7}): PASS.** On x_2-independent, x_1-periodic modes the horizontal space
  is parametrised exactly (dim 3P + 1, every basis vector exactly horizontal); the quadratic form is an exact polynomial matrix
  in τ; exact degenerate perturbation theory on the 6-dimensional toron kernel (K^TQ_1K = 0 exactly) gives a horizontal vector
  p(τ) = p⁽⁰⁾ + τp⁽¹⁾ with **N(τ) = −704τ² + O(τ³) (P = 3), −640τ² + O(τ³) (P = 5, 7)**, the O(τ³) tail bounded at τ_0 = 1/10
  by less than |n_2|: **the quotient Hessian has a negative direction at every τ ∈ (0, 1/10]**, i.e. at every β ≤ 0.199, in
  particular below every threshold the lane can choose. Leading Rayleigh quotients: **RQ = −(88/3)τ² + O(τ³) ≈ −7.33β²
  (P = 3), −16τ² ≈ −4.0β² (P = 5), −(80/7)τ² ≈ −2.86β² (P = 7)** (β ≈ 2τ; these are certified values of one direction, upper
  bounds on the lowest eigenvalue). The direct t-expansion of the combined vector equals pᵀQ̂p exactly.
- **G2b (bounded-in-three-directions "cylinder" region: collar at x_1 ∈ {0, n}, x_2 periodic, x_3, x_4 boxed by the envelope
  f(x) = x(n_⊥+1−x)): PASS** at all four pre-registered instances: (τ, n, n_⊥) = (1/10, 9, 16): RQ_4D ≈ −0.1123; (1/10, 60, 12):
  −0.1702; (1/50, 9, 80): −0.003337; (1/50, 240, 80): −0.008512 (each = exact RQ_cyl + exact 2S_1/S_0; horizontality exact by
  construction). The n = 9 mode is the transporter across the slab (constant charged v_1 wall to wall) dressed by the stripe;
  the n = 60, 240 modes approach the bulk (torus) value.
- **G2c (box: collar on all four sides of a 12×12 plaquette square in (x_1, x_2), x_3, x_4 boxed by the envelope; τ = 1/10,
  n_⊥ = 16): PASS**, RQ_4D ≈ −0.1337 (the float proposal had 181 nonzero residual entries — detector fires — and its exact
  horizontal projection, obtained by solving the 363×363 vertical normal equations over Q, has residual exactly 0).
- **G2-sep: PASS** — on a full 4D instance (n = 4, x_2-period 2, n_⊥ = 3, τ = 1/10, all six plaquette orientations) the 4D
  Hessian equals T_2(S_0²·Hess_cyl + 2S_0S_1|w|²) exactly, |v|²_4D = T_2S_0²|w|², and the 4D horizontality residual is exactly 0.
- **G2-agree: PASS** — for every certified vector the t-expansion with quaternions equals the per-plaquette assembled form
  computed with 2×2 complex matrices over Q(i) (a different representation and a different organisation), exactly.
- **Controls (all as designed):** C2a (τ = 0, trivial background): Hess ≥ 0 every time; C2b (σ_3-components only): Hess ≥ 0 every
  time; C2c: the horizontality detector fires on perturbed / unprojected vectors and reads exactly 0 on certified ones.

**Lemma SEP (the transverse lift; PROVEN-HERE, and checked exactly by G2-sep).** Let w be a mode on the (x_1, x_2)-geometry with
v_3 = v_4 = 0 and background trivial in the 3, 4 directions, and v := w ⊗ f(x_3) ⊗ f(x_4) with f vanishing on the transverse
collar. In the Riemannian chart: (12)-plaquettes at (x_3, x_4) carry f(x_3)²f(x_4)²·Hess_2D(w); a (13)-plaquette is
U_1(x)U_1(x+e_3)⁻¹ = e^{it(f(x_3)−f(x_3+1))w_1·σ} (one direction in su(2), commuting exponents), contributing |w_1|²(Δf)²; a (23)-
plaquette is G e^{it(f−f′)w_2·σ}G⁻¹, contributing |w_2|²(Δf)²; (14), (24) likewise; (34) none. So Hess_4D(v) = S_0²Hess_2D(w) +
2S_0S_1|w|², |v|² = S_0²|w|², and since ξ(λ) has its 3, 4 components paired with v_3 = v_4 = 0, v is horizontal iff w is,
slice by slice. ∎ With f(x) = x(n_⊥+1−x), 2S_1/S_0 = 2/29 (n_⊥ = 16), 2/17 (12), 10/3281 (80): it scales like 20/n_⊥².

### C3. In the exponential/axial coordinates (the chart (LC-2′) names) the failure is FIRST order in β (check lc55_3: PASS)
`checks/lc55_3_criteria.md` (76a41be6…, 03:39:00Z) → `checks/lc55_3_propose.py` (4a74135a…; numpy, proposals only) →
`checks/lc55_3_proposals.txt` → `checks/lc55_3_certify.py` (80da13ae…; plain python, rigorous rational intervals) →
`checks/lc55_3_out.txt` (36 s, exit 0, stderr empty).
Chart: U_ℓ = exp(i(A_ℓ + v_ℓ)·σ), stripe A_2 = a(x_1 mod 3)σ_3 with **rational** β ∈ {1/5, 1/20}; the second-order expansion of
exp(iX·σ) = F(|X|²) + i·Gf(|X|²)X·σ is enclosed through F(s) = Σ(−s)^k/(2k)!, Gf(s) = Σ(−s)^k/(2k+1)! and their s-derivatives
(exact partial sums + rigorous tails). Slice: axial along x_4 on a box with collar — the collar's bottom face fixes the residual
gauge, so the slice is exactly {v_4 = 0} and (v_1, v_2) are unconstrained in the bulk. Region: 6×6-plaquette (x_1, x_2) box
with collar, lifted transversally (**Lemma SEP-exp**: in this chart the (13), (14) plaquettes give |w_1|²(Δf)² exactly and the
(23), (24) plaquettes give |c(w_2)|²(Δf)² with c(w) = the first-order coefficient of exp(i(A+tw))exp(−iA) conjugated, |c(w)| ≤ |w|
because the derivative of exp is an average of isometries; hence Hess_4D ≤ S_0²Hess_2D + 2S_0S_1|w|²).
**Results (G3 PASS):** RQ_2D = **−0.50301** (β = 1/5) and **−0.097981** (β = 1/20), i.e. ≈ −2.5β and −1.96β — **linear in β**;
with the lift, RQ_4D ≤ **−0.3854** (n_⊥ = 12) and **−0.06603** (n_⊥ = 24). The closed-form link series and an independent
matrix-power-series derivation (exact Gaussian-rational 2×2 matrices, rigorous tail) give overlapping intervals (widths below
10⁻¹²). Control C3a (β = 0, same vectors): Hess = +0.6807, +0.04421 ≥ 0, as designed.
**Why first order.** At a non-critical point the second derivative of a gauge-invariant function along a gauge orbit, in a chart
where the orbits are curved, equals −⟨∇S, γ″⟩ (γ the orbit through p in the chart): first order in |∇S| = O(β). The axial-4
slice removes no (v_1, v_2)-plane gauge-like direction in the bulk (they leave the slice only through the transverse envelope),
and the linear model's precision M on such directions is only the envelope cost O(n_⊥⁻²). So in these coordinates
H ≥ (1 − δ)M fails at the stripe already with margin O(u_0β), on regions only ~β^{−1/2} wide transversally.
**Verdict on "convexity of the small-field core in the chosen coordinates" as the route to (LC°):** the exponential/axial chart
is the **worst** choice tested — it turns a second-order (chart-free) obstruction into a first-order one.

### C4. A uniform family down to every threshold, on a region with a collar (check lc55_4 / lc55_4b: PASS)
`checks/lc55_4_criteria.md` (479a48c9…, 03:52:51Z) → `checks/lc55_4_cyl_family.py` → `checks/lc55_4_out.txt` (3.4 s, exit 0);
corrected control: `checks/lc55_4b_criteria.md` (59916c71…, written after lc55_4 ran, before its script) →
`checks/lc55_4b_cyl_family_ctrl.py` (8282d618…) → `checks/lc55_4b_out.txt`.
Region Ω_τ: collar at x_1 ∈ {0, 9}, x_2 periodic, x_3, x_4 ∈ [0, n_⊥(τ)+1] with collar faces; stripe P = 3.
- The 27-dimensional horizontal space (recursion basis) carries an exact polynomial quadratic form; **ker Q̂(0) = the three
  wall-to-wall holonomy directions** (constant w_1 across the slab); K^TQ̂_1K = 0 exactly; the effective second-order form on K
  is **diag(−144, −144, 0)** (the two charged holonomies are negative, the neutral one is flat).
- Certified p(τ): **N(τ) = −2592τ² + O(τ³)**, tail at 1/10 equal to 141.39 < 2592, so **RQ_cyl(τ) ≤ −c_*τ² on (0, 1/10] with
  c_* = 2269084551038400/247334195090033 ≈ 9.174** (κ = |n_2| − tail, divided by (1 + 1/100)²·D_max).
- **Exact identity** 2S_1/S_0 = 20/((n_⊥+1)² + 1) (checked n_⊥ = 1…200; closed form: S_0 = N(N⁴−1)/30, S_1 = (N−1)N(N+1)/3,
  N = n_⊥ + 1). With **n_⊥(τ) := ⌈√(40/(c_*τ²))⌉** one gets **RQ_4D ≤ −c_*τ²/2 < 0**. Values: n_⊥ = 21 (τ = 1/10), 105 (1/50),
  2089 (1/1000), **2.088·10⁴⁴ (τ = 10⁻⁴⁴, below the lane's ε_1 ≲ 6.7·10⁻⁴⁰)**.
- G4-agree: the polynomial, the quaternion t-expansion and the 2×2-complex assembled form agree exactly at τ ∈ {1/10, 1/50,
  1/1000}; certified residuals exactly 0. C4a (τ = 0): Hess = 0 ≥ 0; C4b (σ_3 parts): Hess = 0 ≥ 0.
- **Control disclosure.** lc55_4's C4c perturbed w_2 at x = 4, a site with a = 0 where Ad_G − 1 = 0, so the perturbed vector was
  itself exactly horizontal and the detector correctly read 0: the control could not fire (my design error; its summary line
  "ctrl4 FAIL" stands in the record). The corrected control (lc55_4b: perturb w_1(4), and w_2 at the +β site) **fired** on
  both, and lc55_4b reproduces every lc55_4 number exactly (n_2 = −2592, same c_*). A first lc55_4 run was killed by me at
  ≈04:00Z: its n_⊥ search had a mis-scaled initial guess (√2 too large) and was decrementing one step at a time at τ = 10⁻⁴⁴;
  its partial output is kept as `checks/lc55_4_out_run1_killed.txt`; the rerun uses the criteria's own closed formula.
**Reading.** For every τ ∈ (0, 1/10] there is a region with a collar — 9 wide, periodic in one direction, and ~2/τ wide in the
two others — and an exactly gauge-horizontal level-0 direction along which the Riemannian Hessian of the bare action is
≤ −(c_*/2)τ²|v|². Nothing in the family depends on a threshold: **it reaches below every ε_1 the lane can choose.** This
closes the gap Codex NRES §4.3 named ("A uniform family reaching arbitrarily small ε₁ would require an error-controlled scaling
and boundary construction"), for this mechanism and this region shape.

### C5. Assembly: (LC-1′) is FALSE on the lane's multiscale small-field region; the multiscale claim is REFUTED
**Theorem NC (non-convexity of the chain on its defect-free event).** Fix N = 2, any odd L ≥ 3 with 3 | L (P = 3; for other L
the same with P = L, exact here for P ∈ {5, 7} on the torus, G2a), any admissible thresholds (ε_1, ε_loc, η_q, …), and τ ∈
(0, 1/10] with 2 sin β < min{η_q, ε_loc/2} (β = 2arctan τ). Let p_τ be the following tower over the stripe S(3, β) (all coarse
fields = 1). Then:
(i) p_τ lies in the interior of the event "no defect at any level" on the region Ω_τ of C4, and the collar datum is small-field
    (C1, lc55_1).
(ii) In any gauge-fixed chart obtained by fixing the level-0 gauge with a slice whose tangent at p_τ is the level-0 horizontal
    space and whose second fundamental form at p_τ vanishes (e.g. the background-Coulomb linear slice in normal coordinates at
    p_τ), coarse levels free, the chain potential has, along the following direction 𝔇(v) of the C4 vector v, second derivative
    **≤ −u_0(c_*/2)τ²|v|² + C_𝒩C_D|v|²** (Lemma FOL + C4; the slice's Euclidean Hessian at p_τ equals the Riemannian one on
    T_pΣ because II_Σ(p_τ) = 0). In the exponential/axial chart, at β ∈ {1/5, 1/20}, the same holds with −0.3854u_0, −0.06603u_0
    in place of −u_0(c_*/2)τ² on boxes (C3).
(iii) Hence, as soon as u_0τ² > 2C_𝒩C_D/c_* (in the lane: thresholds are fixed before g_0, and RLARGE §0 records the
    requirement g² ≪ ε_1²·10⁻¹³, so u_0β² is astronomically large at any admissible β ~ η_q), **the chain conditioned on the
    defect-free event is not H-convex for any H ≥ 0 in these charts, so no δ < 1 makes H_Ω ≥ (1 − δ)·(model precision) true.**
**Status:** (i), the exact level-0 certificate and the lift: PROVEN (exact checks). (ii) for the stated slice class:
PROVEN-HERE (Lemma FOL is elementary; C_𝒩, C_D are fixed u-independent constants — normaliser −(3/2)log r_c + O(1/(κur)) and
blocking derivative — not evaluated). Not claimed: impossibility in **every** Euclidean chart (at a non-critical point a chart
with second derivative ≳ β along ∇S can change the sign of the Hessian locally; such a chart must be adapted to each
configuration's fine structure, and "(1 − δ)·model precision" would then refer to that chart). The **joint**-quotient version
(horizontality for the chain's own metric, which weights blocked components) differs from (ii) by a gauge shift of the level-0
vector driven by the coarse divergence of the blocked mode, O(|∇f|) = O(τ/K) when n_⊥ = K/τ; its effect, O(u_0βτ/K), is
negligible for K large: ARGUED, not computed.
**Verdicts.**
- NODEA_RES55 §3.4 table, "on the multiscale small-field core … H-convexity with δ = O(ε_1) is **ARGUED** to hold there", and
  its nr-19 / nr-15 / §7 item 4 ("the multiscale constraint plausibly does"): **REFUTED.** Correct statement: on the
  multiscale small-field region the chain has negative curvature of size ≈ u_0β² (chart-free, gauge-quotient sense) and
  ≈ u_0β (exponential/axial coordinates) at coarse-invisible fine-scale configurations, for every threshold.
- **(LC-1′) as stated (uniformly in Ω, on the defect-free event, H_Ω ≥ (1 − δ)·model precision): REFUTED** (Theorem NC).
- NODEA_RES55 nr-18 (G5 at 0.485, 0.248): **CONFIRMED** (agree Codex NRES item 5); its "below ε_1: ARGUED (scaling)" for the
  constant-field mechanism: the scaling is moot, because the multiscale cut excludes that mechanism (§B) — the obstruction that
  does reach below ε_1 is a different one (C2-C4).
- NODEA_RES55 nr-20 "(LC°) ⇒ (LCR°)" as an implication: unaffected (CONFIRMED by Codex via BL-TILT); its premise (LC-1′) is false.

---

## D. Task 1 answered: the lowest eigenvalue, the constraint that "kills", and the lane's thresholds

**D1. The mechanism (second order, coarse-invisible).** At the stripe the first-order term vanishes on the soft (toron /
holonomy) directions — exactly (K^TQ̂_1K = 0 in G2a and G4) — because the stripe has zero net flux through every aligned block.
That is the term NODEA_RES55's "ε_1/ℓ² against 1/ℓ²" estimate controls, and it does vanish. The negative curvature is the
**second-order** term: the charged components of a slow mode are mixed by the fine-scale field with fast modes, and the
spin-coupling (magnetic-moment) contribution outweighs the diamagnetic one. A continuum reading [ARGUED; the lattice statement
is the exact check]: for an abelian field B(x_1) with zero mean, χ″ = B and A_2 = χ′, the aligned-helicity charged mode
ψ = e^{−χ} is an exact zero mode of Π_+ = (p_1 − A_1) + i(p_2 − A_2), it is background-Coulomb (D·v = 0, hence horizontal), and
⟨ψ, (−D² − 2B)ψ⟩ = −∫B e^{−2χ} = −2∫|χ′|²e^{−2χ} < 0 — strictly negative for every nonzero B, with no net flux at any scale.
This is the same paramagnetic-over-diamagnetic dominance of the spin-1 charged modes that underlies asymptotic freedom.
**Exact sizes (certified directions; upper bounds on the lowest eigenvalue).** Bulk (reduced torus, P = 3): RQ ≤ −(88/3)τ² + O(τ³)
≈ −7.33β²; P = 5: −4.0β²; P = 7: −2.86β². Cylinder of width 9: RQ_cyl ≤ −9.17τ² ≈ −2.3β² on (0, 1/10] (float exploration of
the true lowest eigenvalue there: −4.0β²). Exponential/axial chart: ≈ −2β to −2.5β.
**Answer to "bounded below by a positive constant times the free Laplacian, uniformly in k and T?": NO.** For every admissible
threshold set the chain's Hessian has a negative direction on the defect-free event, as soon as the fine torus side exceeds the
region size (≈ 2.1/(√c_* τ) ≈ 0.7/τ transversally): i.e. for **every UV cutoff K ≥ K_0(τ)**, every T, every column level k.
The failure sits in the UV limit the lane needs.

**D2. Which constraint does what.**
| mechanism | needs | killed by | lane's margin |
|---|---|---|---|
| constant-field Nielsen–Olesen (NODEA_RES55's G5) | flux ≳ c_0 ≈ 3 through the mode's support | the level-j* cut, L^{j*} ≈ n/L (§B) | ~40 orders (4L²t ≪ 3) |
| stripe / toron paramagnetic mode (this file) | any nonzero fine-scale field with zero coarse flux | **no level** | — |
| exponential-chart near-gauge mode | any non-critical point | no level | — |
The stripe's size is bounded only by the **level-0** cut (2 sin β < min{η_q, ε_loc/2}); its curvature deficit is ≈ u_0·c·β², and
the lane's quantifier order (thresholds before g_0; RLARGE §0 "g² ≪ ε_1²·10⁻¹³") makes u_0β² ≫ 1 at every admissible β ≳ g_0.
**Are the lane's thresholds small enough? Irrelevant to the stripe:** making ε_1 smaller shrinks β but leaves u_0β² large
(g_0 is chosen afterwards). Only a level-0 threshold at the fluctuation scale, t_0 ≲ g_0, would tame it — see §G for why that
is not an option.

---

## E. Task 2 answered: choice of coordinates

**E1. Exponential/axial (the coordinates (LC-2′) names): fails at first order (C3).** At a non-critical point the orbit curvature
of the exponential chart contributes −⟨∇S, γ″⟩ = O(|∇S|) on gauge-like directions, and an axial slice keeps (v_1, v_2)-plane
gauge-like directions in the bulk with model precision only O(n_⊥⁻²). Exact: RQ ≤ −0.385, −0.066 at β = 1/5, 1/20.
**E2. Background-covariant (normal) coordinates.** Normal coordinates centred **at the configuration** give the Riemannian
Hessian there; on horizontal vectors that is the gauge-quotient Hessian, which C2/C4 show is negative at the stripe (second order).
So the background-covariant choice improves the order (β instead of β... β² instead of β) but **not the sign**.
**E3. Coordinates around the critical tower (BFT-0/1/2 on 𝒞_glob, GV55 §3).** GV55's Theorem BFT-E (an implication pending a
Codex check of Proposition GV-E; not re-derived here) gives a unique slice critical point x* in 𝔅 = {x ∈ Ker Γ : ‖x‖_(σ) ≤ C_0s},
with level-j plaquette logs ≤ L^{−2(k−j)}(2η + 9η²) (BFT-1). Two facts decide its use for (LC-2′):
- *At* the tower, positivity of the fluctuation operator on the slice is the expected (Balaban-type) statement — in the corpus it
  is obtained one RG step at a time with the blocking term pinning slow modes (1108.1335 eq. (378): a lower bound by
  c_0(−Δ + L⁻²) once the a_kQ^TQ-type term is present), and the background is the unique minimiser in a space of configurations
  smooth at the current scale (2204.08252 eq. (19) and Theorem 1; positivity at the minimiser, eq. (100)). The non-quadratic
  remainder is handled by a cluster expansion (2204.08252 eqs. (11)-(12)), **not** by convexity. [m-free: these are citations
  of where the mechanism is stated; nothing here rests on them.]
- *Away* from the tower — and the chain's defect-free event is far larger than 𝔅: at level 0 it allows plaquettes up to ~η_q,
  while 𝔅 allows L^{−2k}η — coordinates centred at the tower see the stripe as a fluctuation x − x* whose Hessian is the
  exponential-chart one at x (E1), and normal coordinates at x give E2. Either way negative.
**Verdict (task 2).** No coordinate choice among those proposed makes (LC-1′)/(LC-2′) provable on the lane's region, because the
Riemannian gauge-quotient Hessian — the best any covariant chart can see — is negative there. Convexity is available only (a) on
the BFT ball around the tower (ARGUED from BFT-1 + one-step positivity; it is not where the chain's mass is), and (b) for the
**one-step conditional** laws (§G2).

---

## F. Task 3: (LC-3′) — the large-field Peierls bound needed, and what RLARGE / HW / PLD give

**F1. The statement needed (with quantifiers; NODEA_RES55 §3.4 correction + Proposition NU, restated in the tilted law).**
(LC-3′)^tilt: there are a > 0, C < ∞, c_sh < ∞, independent of g ≤ g_0, K, T, k and the cutoff n_♯, such that for every datum of
(CEM°)_k, every λ ∈ [0, λ̄] and every finite set Y of (level, cube) pairs,
  μ_{R,λ}(Y ⊂ 𝒟) ≤ Π_{(j,x)∈Y} C e^{−a u_j} · exp(c_sh · shadow sums),   μ_{R,λ} ∝ e^{λ𝔞^col_A}μ_R,
together with a forcing estimate — the tilted mean of 𝔞^col_A given the large-field data is ≤ B_0|A| + Σ_{(j,x)∈𝒟}ρ_A(j,x)·(size),
Σρ_A·(C e^{−a u}) ≤ b|A| (NU-i / NU-iii form; NODEA55 C.2 (v)'s r⁻⁸ power count is ARGUED). By Proposition NU (Codex NRES item 6:
CONFIRMED as an implication) these give an n_♯-free moment. Agreeing with Codex NRES §5.1: (NU-ii) and a first-moment bound on a
forced action are **different** inputs; NODEA_RES55's "equivalently (LC-3′)" is NOT-VERIFIED.
**F2. What the lane has (located by string; statuses as filed).**
| item | status | what it gives |
|---|---|---|
| RLARGE §3.3 "(SDP)^A_θ [OPEN, P; node A]: … μ(S ⊂ D_k) ≤ (C_Ae^{-a_Au_k})^{\|S\|}·exp(c_A·shadow sums)", μ ∈ ℛ_𝔥^↑ ∪ {μ_{R(𝔥)}} | OPEN (node A's own output; "never derived from (SDP)^A at level k − 1"; Lemma LOOP-const: not by column induction inside ∫W·1_𝔥) | the **untilted** version of (LC-3′)'s probability half |
| HW Lemma TE (ii) / Lemma W-bad: "ℰ_P(V) ≥ c_pr·min{\|\|1 - V_P\|\|²_op, t_pr²}" | CONDITIONAL ⇐ (CLS-min) (level 0 PROVEN-HERE by inequality (B)) | the **energy** half of a Peierls estimate (a defect forces cone energy ≥ c_prε_1²) |
| HW Lemma KS / KS-chain, (M-i) | PROVEN (SU(2)) | exact kernel-mismatch moments (the top term of the column action) |
| HW Theorem HW^cap, Lemma REL-seq | CONDITIONAL (implications proven) | prices of **unreturned** (history) defects in Z(𝔥)/Z(R(𝔥)); not a probability bound under the tilted constrained law |
| PLD Lemma DLR / Theorem W-FREE | PROVEN-HERE (PLD; not re-derived) | column conditional independence one level down — a reduction, not a bound |
| NODEA_RES55 Proposition NU | implication CONFIRMED (Codex) | n_♯-uniformity ⟸ (NU-i)+(NU-ii)+(NU-iii); inputs OPEN |
**F3. Missing, precisely.** (a) (SDP)^A itself (OPEN). (b) Its **tilted** extension: by DOM′ the tilt e^{λ𝔞^col_A} is a local
lowering of the coupling on A's column to ≥ (1 − λ̄)u, so (LC-3′)^tilt is (SDP)^A for an **inhomogeneous-coupling** chain,
uniformly over coupling patterns in [(1 − λ̄)u, u] supported on columns. (c) The forcing decay (ARGUED). None of the three is
supplied by RLARGE / HW / PLD.
**F4. What §C changes.** With (LC-1′) false, (LC-3′) no longer completes (LCR°) through BL-TILT. It remains necessary — in the
(SDP)^A / (NU-ii) form — for every route, including the one in §G3.

---

## G. Task 4: the smallest modification, and whether node A's consumers tolerate it

**G1. Shrinking the region does not work: the convexity window and the Peierls window are disjoint (ARGUED-structural; the
convexity side is exact).** Any region containing every configuration with level-0 plaquettes ≤ t_0 and trivial coarse data
contains stripes with 2 sin β ≈ t_0, where Theorem NC gives curvature ≈ −u_0c t_0² (c ≈ 2-7 by C2-C4) against O(1) positive terms
(Ricci of SU(2) = 2 per link in the bi-invariant metric, normalisers, chart Jacobians). Convexity therefore needs u_0t_0² ≲ O(1),
i.e. a threshold at the **fluctuation scale** t_0 ≲ g_0 (and t_j ≲ g_j at level j, by stripes in the level-j field realised by
smooth finer fields). A Peierls bound needs the opposite: a defect is rare only if u_j·t_j² ≫ 1 (HW W-bad's window c_pr t², price
e^{−a u_j} with a ∝ t²; RLARGE §0's a_bad = c_pr·min{ε_1², t_pr²} with u_kε_1² astronomically large). **Up to O(1) factors the
two windows are disjoint**: no threshold choice gives both a convex small-field region and rare large fields. Not tolerated by
any consumer.
**G2. What IS convex: one-step conditional laws (ARGUED).** Given the other levels, the level-j field (j ≥ 1) sees
κu_{j−1}Φ_{j−1} + κu_jΦ_j + normalisers; near the kernel centres the first term has Hessian ≈ κu_{j−1}r_c (HIST Lemma KQ's
two-sided quadratic bounds) and dominates. For level 0 given level 1, the kernel term κu_0Φ_0 pins exactly the block-averaged
(slow) directions in which the stripe deficit lives (toron / holonomy directions have nonzero block averages): deficit ≈ u_0cβ²
against ≈ κu_0, with β ≤ ε_1 ≪ √κ. This is Balaban's one-step positivity (1108.1335 eq. (378)). **Joint convexity fails;
one-step conditional convexity holds.** Consumer tolerance: BL-TILT on a conditional law gives a conditional tilted-mean bound
with a forced charge; iterating level by level degrades the rate λ ↦ λ/(1 − λ) per level (NODEA_RES55 §3.6 (c2); HW (HW-F5)).
(CEM°) / (LCR°) need k-uniform constants, so **not tolerated as is**.
**G3. The modification the consumers can tolerate (recommended restatement of node A's residual).**
  (LCR°) ⟸ [one-step conditional positivity on the multiscale small-field region (G2)] + [a cluster expansion of the
  non-quadratic terms **with an inhomogeneous coupling** — the tilt as the coupling (1 − λ)u on A's column, via DOM′; HW §6
  "local coupling response … ARGUED: it needs node A's cluster expansion with an inhomogeneous coupling"] + [(LC-3′)^tilt, F1].
This is the structure of Balaban's method as the corpus states it: positivity one step at a time at the background, the rest by
cluster expansion (2204.08252 eqs. (11)-(12)). **It is a larger obligation than (LC°), not a smaller one: the global-convexity
shortcut does not exist on the region node A uses.** (CEM°)'s consumers (Corollary E2-RED°, CRC-2T°, CRC-HW°) see only the
moment bound, so they are unaffected by which route proves it.
**G4. What survives of BL-TILT.** (a) Everything Codex banked: the theorem, BL-1–BL-4 in the convex-core models. (b) Its
application to **one-step conditional** laws inside an RG step (G2). (c) Not: its application to the chain on the defect-free
event (Theorem NC).

---

## H. Errata to this file (append-only; found on proof-reading at ≈04:12Z; nothing above is edited)
- **LE1 (§E, E2).** "improves the order (β instead of β... β² instead of β)" is a garbled self-correction. Read: normal coordinates
  at the configuration improve the order of the failure from **β (exponential/axial) to β² (Riemannian)**, but not its sign.
- **LE2 (§D, D1).** "region size (≈ 2.1/(√c_* τ) ≈ 0.7/τ transversally)" is wrong arithmetic. Correct: n_⊥(τ) = ⌈√(40/(c_*τ²))⌉
  ≈ √(40/9.174)/τ ≈ **2.09/τ** transversally (lc55_4_out.txt: 21, 105, 2089 at τ = 1/10, 1/50, 1/1000). No conclusion changes.
- **LE3 (§C2, G2a; checks/lc55_2_out.txt log line).** The script prints "(polynomial identity of degree <= 8 checked at 3 points +
  closure assertion)". Three evaluations do not prove a polynomial identity. Correct status: each basis vector is horizontal **for
  all τ by construction** — w_1 is defined by the recursion R(x) = 0 for x = 1…P−1, with (Ad_G − 1)w_2 computed through the exact
  identities (1+τ²)²(Ad_{G(β)} − 1)u = Ĝ_+(0,u)Ĝ_+^† − (1+τ²)²u and Ad_{G(−β)}Ad_{G(β)} = id, and (Ad_G − 1)σ_3 = 0; the closure
  R(0) = 0 is asserted as an exact polynomial identity. The 3-point evaluation only checks that the implementation of these
  formulas agrees with the generic Ad (and the certified vectors' residuals are separately exactly 0 at τ = 1/10). Same for lc55_4.
- **LE4 (§C2, §E).** "any Riemannian Brascamp–Lieb / Bakry–Émery argument" refers to manifold versions of those inequalities
  (Hess V + Ric on a weighted Riemannian manifold, convex boundary) [m: from memory, e.g. Kolesnikov–Milman; not re-read]. Nothing
  here depends on the exact statement: the point is only that such arguments see the Riemannian Hessian, which C2/C4 show negative.

---

## I. Summary table (every claim of this file and every prior claim it re-judges)

| id | claim | verdict / status | where |
|---|---|---|---|
| lc-01 | Lemma FOL: along following directions the kernels contribute no curvature; chain Hessian = u_0·Hess S(U_0) + u-free terms | **PROVEN-HERE** (elementary) | §A |
| lc-02 | B1: coarse angle of a constant abelian field is L²α per level (S4′, translation/gauge covariance) | **PROVEN-HERE** (elementary) | §B |
| lc-03 | B2: the constant-field NO mode needs flux ≳ c_0 ≈ 3; the level-j* cut excludes it when 4L²t < c_0; lane's margin ~40 orders | **ARGUED** (B1 exact + numerical threshold; no positivity theorem written) | §B |
| lc-04 | NODEA_RES55 §3.4 "curvature seen by a mode of size ℓ is ≲ ε_1/ℓ²" (first-order, net-flux mechanism) | **CONFIRMED** as to that mechanism | §B, §D1 |
| lc-05 | stripe S(P, β): every coarse following field exactly trivial, all mismatches 0, level-0 plaquettes ≤ 2 sin β (L = 3, 5; τ = 1/10, 1/1000) | **PROVEN** (exact, lc55_1; controls fired) | §C1 |
| lc-06 | quotient (Riemannian, horizontal) Hessian at the stripe negative for **every** τ ∈ (0, 1/10], P = 3, 5, 7 (reduced torus) | **PROVEN** (exact PT, lc55_2 G2a) | §C2 |
| lc-07 | same on bounded-in-3-directions cylinders (4 instances) and on a box bounded in all 4 directions (τ = 1/10) | **PROVEN** (exact, G2b, G2c) | §C2 |
| lc-08 | Lemma SEP (exact transverse lift; horizontality preserved) | **PROVEN-HERE** + exact check G2-sep | §C2 |
| lc-09 | exponential/axial chart: negative at FIRST order (β = 1/5, 1/20; RQ_4D ≤ −0.385, −0.066) | **PROVEN** (rigorous intervals, lc55_3, two link-series paths) | §C3 |
| lc-10 | first-order mechanism in the exponential chart for every small β (orbit curvature × gradient) | **ARGUED** | §C3, §E1 |
| lc-11 | Lemma SEP-exp (lift inequality in the exponential chart) | **PROVEN-HERE** | §C3 |
| lc-12 | uniform family to every threshold on a collared region (width 9, x_2 periodic, ~2.09/τ transversally): RQ_4D ≤ −c_*τ²/2, c_* ≈ 9.174, all τ ∈ (0, 1/10] incl. 10⁻⁴⁴ | **PROVEN** (exact, lc55_4; corrected control lc55_4b fired) | §C4 |
| lc-13 | Theorem NC: the chain is not H-convex on its defect-free event, for any H ≥ 0, in level-0-normal horizontal slices and in exponential/axial charts, once u_0τ² > 2C_𝒩C_D/c_* | **PROVEN-HERE** for the stated chart classes (C_𝒩, C_D u-free, not evaluated) | §C5 |
| lc-14 | joint-quotient (chain-metric) version of lc-13 | **ARGUED** (correction O(u_0βτ/K)) | §C5 |
| lc-15 | NODEA_RES55 nr-19 / §3.4 "H-convexity with δ = O(ε_1) … on the multiscale small-field core" / nr-15 (multiscale half) / §7 item 4 | **REFUTED** (lc-12, lc-13) | §C5 |
| lc-16 | (LC-1′) as stated (uniform in Ω, defect-free event, H_Ω ≥ (1 − δ)·model precision) | **REFUTED** | §C5 |
| lc-17 | NODEA_RES55 nr-18 (G5 at 0.485, 0.248) | **CONFIRMED** (agree Codex NRES item 5); its below-ε_1 extrapolation is moot (§B) | §C5 |
| lc-18 | lowest eigenvalue NOT ≥ c·(free) uniformly in k, T: negative for every K ≥ K_0(τ), every T, every k | **PROVEN** (from lc-12, lc-13) | §D1 |
| lc-19 | the stripe/toron mode is killed by no level; only the level-0 cut bounds its size | **PROVEN** (lc-05 + lc-12) | §D2 |
| lc-20 | continuum reading: e^{−χ} is a Π_+ zero mode with ⟨ψ, (−D² − 2B)ψ⟩ = −2∫|χ′|²e^{−2χ} < 0 for zero-net-flux B | **ARGUED** (continuum; not used for any verdict) | §D1 |
| lc-21 | coordinates: exponential/axial worst (O(β)); covariant normal improves order to β², not sign; BFT-ball convexity only near the tower | lc-09/lc-06 **PROVEN**; BFT-ball positivity **ARGUED** (GV55's BFT-E not re-derived here) | §E |
| lc-22 | (LC-3′)^tilt stated; lane supplies (SDP)^A (OPEN), W-bad energy windows (CONDITIONAL), KS (PROVEN), DLR (as filed); missing: (SDP)^A, its inhomogeneous-coupling extension, forcing decay | statement + inventory | §F |
| lc-23 | NODEA_RES55 "(NU-ii) … equivalently (LC-3′)" | **NOT-VERIFIED** (agree Codex NRES §5.1) | §F1 |
| lc-24 | G1: convexity window (u t² ≲ 1) and Peierls window (u t² ≫ 1) disjoint up to O(1) | **ARGUED** (convexity side exact) | §G1 |
| lc-25 | G2: one-step conditional laws are convex on the region | **ARGUED** | §G2 |
| lc-26 | G3: recommended restatement of node A's residual (one-step positivity + inhomogeneous-coupling cluster expansion + (LC-3′)^tilt) | recommendation | §G3 |

**Counts.** Prior claims re-judged: **CONFIRMED 2** (lc-04 as to mechanism, lc-17); **REFUTED 2** (lc-15, lc-16);
**NOT-VERIFIED 1** (lc-23). New: **PROVEN (exact checks) 7** (lc-05, -06, -07, -09, -12, -18, -19); **PROVEN-HERE 5** (lc-01, -02,
-08, -11, -13 for its chart classes); **ARGUED 7** (lc-03, -10, -14, -20, -21's BFT part, -24, -25).
**Checks** (criteria first; exact; every control reported): lc55_1 PASS (C1a, C1b fired); lc55_2 all 20 gates PASS (C2a-c as
designed); lc55_3 PASS (C3a as designed); lc55_4 G4 PASS, G4-agree PASS, its C4c mis-designed (disclosed), corrected in lc55_4b
(fired). Floats only in `*_propose.py` and the scratchpad exploration (disclosed, §0).

---

## FOR THE LEAD

1. **The multiscale claim is false.** On the region node A uses (no defect at any level, at any thresholds), the chain is not
   convex: a fine-scale "stripe" of chromomagnetic flux (plaquettes ≤ 2 sin β, zero flux through every aligned block, so **every
   coarse field is exactly the identity**) has a gauge-horizontal direction along which the bare action's Riemannian Hessian is
   ≤ −(c_*/2)τ²|v|² (c_* ≈ 9.17, τ = tan(β/2)), exactly, for every τ ≤ 1/10 — down to 10⁻⁴⁴, below every ε_1 the lane can pick —
   on a collared region ~2.09/τ wide (lc55_4). Lemma FOL lifts this to the chain (kernels add no curvature along following
   directions), so (LC-1′) fails once u_0τ² ≫ 1, which the lane's order of constants guarantees. In the exponential/axial chart
   (LC-2′)'s coordinates) it fails already at first order in β (lc55_3).
2. **Which constraint kills the Nielsen–Olesen mode:** the level-j* cut with L^{j*} ≈ the mode size, needing 4L²t < c_0 ≈ 3;
   the lane's thresholds pass by ~40 orders (§B, ARGUED). **But the NO mode is not the obstruction**: the stripe's negative
   curvature is second order, comes from the spin coupling of charged modes (paramagnetic beats diamagnetic), lives in
   toron/holonomy directions, and **no level's constraint sees it**. Smaller thresholds do not help: they shrink β, and g_0 is
   chosen after them.
3. **Coordinates:** exponential/axial is the worst choice (first order). Background-covariant normal coordinates improve the order
   to β² but not the sign, and coordinates around the critical tower only help inside the BFT ball, which is not where the chain's
   mass is (§E).
4. **(LC-3′):** stated with quantifiers in the tilted law (§F1). The lane has its untilted probability half only as an OPEN item
   ((SDP)^A, RLARGE §3.3) and its energy half conditionally (HW Lemma W-bad). Missing: (SDP)^A, its inhomogeneous-coupling form,
   and the forcing decay.
5. **Modification:** shrinking the region cannot work — convexity needs thresholds at the fluctuation scale (u t² ≲ 1), Peierls
   needs u t² ≫ 1 (§G1). What is true is **one-step conditional convexity** (§G2, ARGUED), which BL-TILT can use only inside an RG
   step. The consumer-compatible restatement of node A's residual (§G3) is: one-step positivity + a cluster expansion with an
   inhomogeneous coupling (HW §6's "local coupling response") + (LC-3′)^tilt. That is a **larger** obligation than (LC°).
6. **What PROOF.md / HANDOFF should change.** HANDOFF's node-A item should **not** read "(LCR°) ⟸ (LC°) = (LC-1′) multiscale
   small-field convexity + …" (NODEA_RES55 FOR THE LEAD item 6): (LC-1′) is refuted. Replace by: *"(LCR°) via one-step
   conditional positivity + inhomogeneous-coupling small-field cluster expansion + (SDP)^A in tilted form; global convexity of
   the chain on the defect-free event is false (LCONV55 Theorem NC: coarse-invisible stripes, second order in the field; first
   order in exponential/axial coordinates)."* BL-TILT stays banked as Codex banked it (convex-core models), with its scope noted
   as "not applicable to the chain on the defect-free event". NODEA_RES55 nr-19 / nr-15 (multiscale half) / §7 item 4 should not
   be quoted. No counted HW/PLD/RLARGE theorem changes.
7. **Codex verdicts used:** CODEX_REVIEW_NRES items 2, 5, 6 and §2.3/§3/§5.1 — **agree** with every one; this file supplies, for
   item 5's NOT-VERIFIED "multiscale convexity", a **negative** answer, and for its "uniform family reaching arbitrarily small
   ε₁", an exact family (for the stripe mechanism, on a collared region periodic in one direction; on a region bounded in all
   four directions only at τ = 1/10 exactly). CODEX_REVIEW_NODEA item 5: agree (not re-derived).

Files written: `LCONV55.md`; `checks/lc55_1_criteria.md`, `lc55_1_region.py`, `lc55_1_out.txt`, `lc55_1_err.txt`;
`checks/lc55_2_criteria.md`, `lc55_2_propose.py`, `lc55_2_proposals.txt`, `lc55_2_certify.py`, `lc55_2_out.txt`,
`lc55_2_err.txt`; `checks/lc55_3_criteria.md`, `lc55_3_propose.py`, `lc55_3_proposals.txt`, `lc55_3_certify.py`,
`lc55_3_out.txt`, `lc55_3_err.txt`; `checks/lc55_4_criteria.md`, `lc55_4_cyl_family.py`, `lc55_4_out.txt`, `lc55_4_err.txt`,
`lc55_4_out_run1_killed.txt`; `checks/lc55_4b_criteria.md`, `lc55_4b_cyl_family_ctrl.py`, `lc55_4b_out.txt`, `lc55_4b_err.txt`.
No git command was run.

---
*[Appended 2026-10-29 ≈04:15Z on a final proof-read.]*
- **LE5 (§C5, Theorem NC (ii)).** The chart class must also require the coordinates **on** Σ to be normal at p_τ (vanishing
  Christoffel symbols there), as in the example given ("the background-Coulomb linear slice in normal coordinates at p_τ").
  For other coordinates on the same slice the Euclidean Hessian at p_τ differs from the Riemannian one by ⟨∇_ΣS, Γ(p_τ)⟩, which is
  nonzero because the stripe is not a critical point. The exponential/axial statement in (ii) is a separate, explicit chart and is
  unaffected. No other conclusion changes.
- **Pointer.** The "## Errata (reserved; append-only)" stub near the top of this file was written at resume time and says "(none
  yet)"; the errata are LE1-LE5 in §H and here.

Closing provenance: deliverable final at `date -u` below. Model: claude-opus-5-5. No git command was run.
Thu Oct 29 04:13:23 UTC 2026
*[Timestamp correction: the "≈04:15Z" in the last appended block was an estimate; the `date -u` line above (04:13:23Z) is the actual time.]*
