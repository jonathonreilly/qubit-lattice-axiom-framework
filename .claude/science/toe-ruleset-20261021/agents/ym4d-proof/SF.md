# SF: lane F of the 4D YM proof push. The small-field package (SF^J)_k (node A) split into narrow lemmas (session 1, 2026-10-28)

**Scope.** RLARGE v2 §4.2 row 3 names **(SF^J)_k** (node A1-A4, weight P×3-4, OPEN) as the small-field step at stage k. This
file splits it into narrow lemmas, pre-states each one (§2, written before any proof in §3), proves what it can, and names
every hypothesis consumed with its owner file. Write access: SF.md, SF_LOG.md, checks/s*. Everything else read-only. No
commit, PR, push, CL or axiom edit. No tally change in PROOF.md (the ledger owner decides). Status words as in PROOF.md:
PROVEN-HERE (counted or not, said each time), CONDITIONAL (implication proven, hypotheses named), ARGUED, OPEN, HYPOTHESIS.
Imported items are never load-bearing for a PROVEN-HERE claim.

**Inputs read (read-only; md5 at 01:39 UTC, 2026-10-28, while other agents were editing):** PROOF.md 6e7f856c… (header
l.1-60; Theorem CE + Lemmas CE-geo, TG, CE-geo' l.1807-1980, l.2217-2240; Setting N5-bg, Lemmas N5-cov, AX, N5-an, CT♯,
Theorem RW, Corollary RW-triv, Theorem N5-sf0, Proposition N5-sf_i l.5199-5420; grep hits for NA-crit, NA-inv, NA-IFT,
B-NA-red, N2-lin, N2-exp, NAH1, NAH-ind); RLARGE.md 24a73553… (§0-§1, §4, §6-§8 in full; §2-§3 headings); RLARGE_INTEGRATION_LOG.md
4dbddafe…; HIST.md 253bb29f… (§8, §14.0-§14.1, §20 in full); PLD.md 4db9b142… (§9.3-§9.4, §15.2); FLOW.md f3d4165f… (§4 SF
clauses l.180-230); REVIEW_S20.md d7828b1f… (bottom line, (BG-unif) template, repair route (R-a)/(R-b)); REVIEW_S15_CONVERGENCE.md
5b0d4a48… (node A DAG). **Session 21 (the one-level curvature lemma, REVIEW_S20 route (R-a)) has NOT landed in PROOF.md**
at read time (RTARGET §46 pre-stated; c37 criteria and script exist, no PROOF [S21] block): it is not consumed here.

---

## 0. Conventions (RLARGE v2 §0; additions)
- Levels, Λ_k, L ≥ 3 odd, d = 4, G = SU(N), u_k = 1/g_k², s(U) = 1 - N⁻¹Re tr U, the chain, χ_Q, ε_1, (F_R): RLARGE v2 §0.
- Stage k integrates U_k given U_{k+1} (HIST §2, RLARGE §2.1). At stage 0 the U_0-integrand is
  **e^{-u_0Σ_ps(U_0(p))}·Π_ce^{-κu_0φ_{M̄_c(U_0)}(U_1(c))}/n_c(M̄_c(U_0)),  n_c(M) := ∫_{SU(N)}e^{-κu_0φ_M(W)}dW** (HIST (3.0)),
  so the kernel normalisation is part of the stage-0 U_0-integrand (it is HIST GAP S2-3's term at k = 0).
- Setting N5-bg (PROOF l.5199): O(U, V), Π_U = 1 - h_U^T(h_Uh_U^T)^{-1}h_U (orthogonal, block-diagonal), Õ = Π_UOΠ_U + (1 - Π_U),
  C = Õ^{-1} - (1 - Π_U), 𝒞 = Õ^{-1/2} - (1 - Π_U); Õ(b, b') = 0 unless the blocks of b, b' are at coarse ℓ^∞ distance ≤ 1
  (range r_K = 1 block at level 0). Theorem RW's objects G_□(t), R_□(t), P(t), T_ω(t), Ω_□, K^{-1}(s; t), 𝒞(s) (PROOF l.5282).
  Put **𝒞^Π(s) := 𝒞(s) - (1 - Π_U)** (so 𝒞^Π(1) = 𝒞).
- Setting CE (PROOF l.1808): unit cubes of a d = 4 torus, polymers = *-connected (touching) sets of cubes, d(X) the
  touching-tree length; κ_0 = 16 log 12800 ≈ 151.3, K_0 = e^{κ_0}/6400 (the [S11] constants, Lemma CE-geo'); |X| ≤ 16(1 + d(X)).
  **X^+** := the set of cubes whose closed cube meets the closed cube of some element of X (the *-neighbourhood; X ⊂ X^+).
- White noise: Z = (Z_b)_b, Z_b ∈ su(N) ≅ R^{N²-1} (orthonormal basis for **the Frobenius structure ⟨A, B⟩ := -tr AB, |A|² =
  |A|²_HS = -tr A²** [RSF1-fix SF-J-2: was "⟨A, B⟩ = -2tr AB or any fixed Euclidean structure"; one structure is fixed because the
  constants N/9, N/270 of SF-J and the √N of SF-A2^0 are for it; under -2tr AB they would read N/18, N/1080 and the white-noise
  normalisation would change by √2]; constants below are for the HS norm |·|), μ_wn(dZ) := Π_bΠ_a(2π)^{-1/2}e^{-z_{b,a}²/2}dz_{b,a}. Z(x) := (Z_b)_{b based at x} ∈
  R^n, **n := 4(N² - 1)**.

---

## 1. The package (SF^J)_k split into clauses (statement map; every clause with owner and status)

(SF^J)_k (RLARGE v2 §4.2 row 3; HIST §8 H-3) is: the small-field step that integrates U_k on Λ_k(𝔥) against the (I_k^E)'
density with polymers in (U_k, U_{k+1}, U_{k+2}), outputting two-field polymers in (U_{k+1}, U_{k+2}) on Λ_{k+1} in the
(I_{k+1}^E)' form, with level-uniform thresholds [v2-C], and the clauses (SG^fl)_k, (SF-irr)_{k+1}, (RLF-5)'s width. Split:

| clause | content | owner of the statement | status before this file |
|---|---|---|---|
| **A1** background | A1.0 level-0 → 1 critical branch U(V) (BR1/NAH1); A1.k level-k tower uniform in k ((BG-unif)); A1.loc the tower on Λ_k(𝔥) only (large-field complement); A1.thr thresholds compatible with ε_1 | PROOF [S20], B-NA; REVIEW_S20 template; HIST (I_k^E)' (a3)-(a4); RLARGE §0 [v2-C] | A1.0 PROVEN [S20]; A1.k OPEN (named, not precise); A1.loc not stated; A1.thr named |
| **A2** Gaussian + remainder | N5 at the level-k background; the exact split of the stage-k integrand into a Gaussian (covariance C/u_k) times local analytic activities: Haar Jacobian, action Taylor remainder, kernel normalisation, Faddeev-Popov part; fluctuation cut | PROOF N5-sf0, N5-sf_i, NA-FP; HIST GAP S2-3 | N5-sf0 PROVEN; level ≥ 1 ⇐ (NA-H_loc); the rest not stated |
| **A3** cluster expansion | the remainder's expansion by Theorem CE after the RW decoupling; CE's hypotheses re-verified | PROOF Theorem CE, Theorem RW (iv); PLD (SC)_k | CE, RW PROVEN; their composition not written |
| **A4** reproduction | (I_{k+1}^E)' at level k+1 with the same constants: blocking of polymers, extraction/contraction ((SF-irr)), coupling flow ((SF-g)), (SG^fl)_{k+1}, (BG)_{k+1}, (RLF-5) width, (SF-last) at k = K | HIST §20.3; PLD §9.3, §15.2; FLOW §4; RLARGE §4.2 | all HYPOTHESIS/OPEN |

---

## 2. Pre-stated lemmas (written 2026-10-28 01:39-01:44 UTC, after reading the inputs above and after unwritten
exploratory reasoning, BEFORE any proof in §3 and before the s1 criteria; not edited after §3 starts except for the
dated annotations marked [post-proof])

### A1 (background)
- **Lemma SF-thr (operator-norm cut ⇒ N5's log class).** For every N ≥ 2 and U ∈ SU(N) with ||1 - U||_op ≤ ε ≤ ε^thr_N :=
  min{½, 2π/(1.011N)·(1 - 10⁻⁶)}: the principal logarithm log U lies in su(N), |log U|_op ≤ 1.011ε and |log U|_HS ≤ 1.011√N·ε.
  Consequently, if ε_1 ≤ min{ε^thr_N, ε_N5/(1.011√N)} then every cut-good plaquette (χ-good, ||1 - U_p||_op < ε_1) satisfies the
  plaquette clause |log U_p|_HS ≤ ε_N5 of N5-sf0 (a) [ε_N5 = ε_* at level 0]. *Planned status: PROVEN-HERE (not counted).*
  **[RSF1-fix SF-thr-1/2, 2026-10-28 session 2] Reading of "Consequently".** The lemma is a NORM CONVERSION for whichever field is
  cut. N5-sf0 (a)'s plaquette clause is a clause on the BACKGROUND U of (U, V) (PROOF l.5398-5399); χ_Q (RLARGE l.55) acts on the
  integrated field. The chain that puts the background in 𝔑(α_*) is: cut on V = U_{k+1} ⇒ (SF-thr) |log V_P|_HS ≤ 1.011√Nε_1 ⇒
  (BR1 (iii) at level 0, or Lemma CURV1 / Proposition NAH-unif at level j) the curvature and soft fluctuation of the background
  U(V) are ≤ (K̄ + θ)η and (K̄_ρ + θ + C_θη)η (PROOF l.6048) ⇒ N5-sf0 (a) / N5-sf_j. χ_Q covers cube-INTERIOR plaquettes only; the
  inter-cube plaquettes enter through the EVENT of [v2-E8] (RLARGE l.75-79), not through χ_Q. The other thresholds of [v2-C]:
  ε_loc ≤ ε_1/4 (RLARGE l.681), so the conversion applies a fortiori wherever ε_loc bounds operator-norm plaquette defects;
  ε^J_loc is assumed to have the same form (not checked in this session). [RSF2-fix SF-thr-2: not checked in session 3 either;
  it is kept as an explicit ASSUMPTION of Lemma SF-thr's "Consequently" for the ε^J_loc threshold (definition HIST §4-§5).]
- **Corollary SF-thr-k.** Under (BG-unif) (A1.k below) the choice ε_1 := min{ε^thr_N, min(ε_BG, ε_*/C_BG)/(1.011√N)} is
  independent of k, K, T and makes the [v2-C] compatibility hold at every level for the plaquette clause. The soft-fluctuation
  clause |ρ_c| ≤ ε is NOT implied by any cut and stays a kernel-mismatch event (Lemma KN / RS branch (i)). *Planned:
  CONDITIONAL ⇐ (BG-unif).* **[RSF1-fix SF-thr-k-2: the preceding sentence is WITHDRAWN as stated.** For the background (the
  object N5 is about) the soft clause IS implied by the curvature of V: BR1 (iii) |ρ_c(U(V), V)| ≤ 3p_Lr(ε) (PROOF l.5637) and
  NAH-unif's ρ ≤ (K̄_ρ + θ + C_θη)η. Correct statement: the INTEGRATED field's soft fluctuation ρ(U_k, U_{k+1}) is not controlled by
  any plaquette cut; it is the kernel-mismatch event (RLARGE §3.1); the background's ρ is controlled by V's curvature.]
- **(BG-unif) [HYPOTHESIS, P; statement adopted verbatim in substance from REVIEW_S20 Part 2's template, owner PROOF (B-NA)].**
  There are ε_BG > 0, C_BG < ∞, m_BG > 0, T_BG depending only on (N, L, κ_±) such that for every k ≥ 1, every torus with level-k
  side ≥ T_BG and every level-k field V_k (and its complex neighbourhood of radius ε) with own-units plaquette logs and level-k
  soft fluctuations ≤ ε ≤ ε_BG [RSF1-fix BG-1: the template (REVIEW_S20 l.331-332) says "level-(k+1) soft fluctuations"; the
  template's wording is restored: read "level-(k+1) soft fluctuations" here. ~~After PROOF [S21], clauses (i)-(iii) follow from
  CURV1 + NAH-unif under (H-K) + (H-C)~~ **[RSF2-fix BG-1: that sentence overstated NAH-unif. Correct reading against PROOF
  [S21]-[S22]: (i) (curvature and ρ of the tower) ⇐ CURV1 + Proposition NAH-unif′ under (H-K), (H-C⁺), (H-ℂ), with (H-G) derived
  (Lemma HG-ind, [S22]); (ii) (holomorphy with the same bound) IS (H-ℂ), so it is not a conclusion; (iii) (exponential tower
  response |∂U_j/∂V_k|) is not supplied by NAH-unif or NAH-unif′ at all.]**; clause (iv) is exactly what remains as (H-C) (now
  (H-C⁺), PROOF [S22] CURV-F2′) for the per-level route], there is a tower U_{k-1}, …, U_0 with U_j a critical point of F_j(·, U_{j+1}) (U_k := V_k), unique
  in the composite slice ball of sup-radius C_BGε about the composite lift, such that for every j < k: (i) plaquette logs of U_j
  and soft fluctuations ρ(U_j, U_{j+1}) ≤ C_BGε; (ii) U_j holomorphic in V_k on the neighbourhood with the same bound; (iii)
  |∂U_j(x)/∂V_k(y)| ≤ C_BGe^{-m_BGd_j(x,y)}; (iv) the N_0-Lipschitz constants of Hess E_j^br in the chart at the lift ≤ C_BG.
  **No-circularity clause (REVIEW_S20 (d)):** the proof may not use the per-level covariances C^{(j)} as Newton inverses.
- **(BG-loc) [OPEN; new name; s to P].** (BG-unif) with "every level-k field V_k small on the torus" replaced by "V_k small on
  Λ_k(𝔥) ∪ collar", the tower defined on the cone over Λ_k(𝔥) with the exterior links frozen (Dirichlet data from the history),
  the same conclusions inside, and the dependence on the frozen exterior exponentially small (rate m_BG) at distance r from
  Ω^c_k. *Why named:* N5-sf0 (a) and the (BG-unif) template are global-smallness statements (every plaquette of the torus),
  while (SF^J)_k acts on Λ_k(𝔥) only; this is HIST GAP S2-1's background analogue.
  **[RSF1-fix BG-loc-1: (BG-loc) is DROPPED as a name.** As written it is not well posed (no boundary convention for terms
  straddling the frozen exterior; "cone over Λ_k(𝔥)" undefined in SF; no form of the exterior dependence). Its content is
  Theorem A5 (A)-(C) of HIST §25.5 on the full-cone term set 𝒞^♭(Λ_k), which IS a boundary convention: (i) ⇐ A5 (A) (real
  regularity via AE-red), (ii) ⇐ A5 (B) (holomorphic branches), (iii) ⇐ A5 (B)'s kernel decay. So (BG-loc) is a CONSEQUENCE of
  A5's hypotheses (an implication, not an identity), and those hypotheses are now (a5-G♯) + (R♯) + (a5-U) + (a3-q) + (MS-Sob)
  (§6.2, §7.2 of this file).]

### A2 (Gaussian + remainder)
- **Lemma SF-J (the Haar Jacobian is an ultralocal analytic single-link activity).** For A ∈ su(N) with ||A||_op < π and any
  U_0 ∈ SU(N), the Haar probability measure in the coordinates U = e^AU_0 is dU = c_N·j(A)dA (dA Lebesgue for the HS structure,
  c_N > 0 a constant), with
    j(A) = det((1 - e^{-ad A})/ad A) = Π_{a<b}(sinh(w_ab)/w_ab)²,  w_ab := (λ_a - λ_b)/2,
  λ_a the eigenvalues of A; j > 0 on {||A||_op < π}. log j extends holomorphically to {A ∈ su(N)⊗C : ||A||_op < π} and, for
  ||A||_op ≤ π/2: **|log j(A)| ≤ (N/9)|A|²_HS**, and log j(A) = (N/12)tr(A²) + R_4(A) with |R_4(A)| ≤ C_J|A|⁴_HS (explicit C_J).
  *Planned status: PROVEN-HERE (counted).*
- **Lemma SF-cut (per-site fluctuation cut).** Let μ = Π_xμ_x be any product probability measure on the white-noise field with
  μ_x the standard Gaussian on R^n (n = 4(N² - 1)), p > 0, χ_x := 1{|Z(x)| ≤ p}. Then (a) for every bounded measurable F,
  ∫Fdμ = Σ_{Q⊂sites}[Π_{x∉Q}μ_x(χ_x)][Π_{x∈Q}μ_x(1 - χ_x)]∫Fdν_Q, ν_Q := Π_{x∉Q}(χ_xμ_x/μ_x(χ_x))·Π_{x∈Q}((1 - χ_x)μ_x/μ_x(1 - χ_x)),
  each ν_Q a product probability measure; (b) μ_x(1 - χ_x) ≤ 2^{n/2}e^{-p²/4}; (c) on supp ν_∅, |Z_b| ≤ p for every link b. *Planned:
  PROVEN-HERE (not counted; elementary).*
- **Lemma SF-T0 (stage-0 action remainder: local, analytic, cubic).** There are r_T ∈ (0, 1/8], S_T < ∞ depending only on
  (N, L, κ_±) such that: for every real background (U, V), every term τ of the stage-0 action (a plaquette s(U_p), or a kernel
  term φ_{M̄_c(U)}(V_c)) with variable pattern P_τ, and every real gauge g on a box containing P_τ with |log(gU)_b|,
  |log(gV)_c| ≤ r_T/4 on P_τ, the function A ↦ τ(e^AU; V) (A_b ∈ su(N)⊗C, b ∈ P_τ) is holomorphic on {max_{b∈P_τ}|A_b| < r_T/4},
  bounded there by S_T, and its third-order Taylor remainder obeys
    |τ(e^AU) - τ(U) - Dτ(U)·A - ½D²τ(U)(A, A)| ≤ 16S_T(4ρ/r_T)³,  ρ := max_{b∈P_τ}|A_b| ≤ r_T/8.
  If (U, V) is a critical point of the full stage-0 action (BR1: U = U(V)), Σ_τDτ(U)·A = 0 for every A (all directions).
  *Planned status: PROVEN-HERE (existence of constants, as N5-an; counted).*
- **(SF-N) [OPEN; s].** The kernel normalisation ν(M) := log n_c(M) + (N² - 1)/2·log(κu_0/(2π)) (u_0-subtracted) is, on a complex
  neighbourhood of {M = W_0(M)e^{-ρ}: |ρ| small} of g-independent radius, holomorphic, bounded uniformly in u_0 ≥ u_min, with
  a u_0-uniform expansion ν = ν_0(M) + O(1/u_0). (The Laplace method gives it formally; not proven here.)
  **[RSF1-fix SF-N-1: (SF-N) is LARGELY DISCHARGED by HIST §25.4 Lemma NORM-an** (PROVEN-HERE [S4-D] in HIST, counted there,
  reviewed by REVIEW_HIST_S4 (strategic verdict 2: real and reusable) [RSF2-fix, wording]): on D_c(y_0), uniformly in u ≥ 1/(2κ), log𝒩^ℂ_c = log𝒩_0 + 𝔫_c with 𝒩_0 a
  c-number and 𝔫_c holomorphic, |𝔫_c| ≤ 2C_Nθ, θ = 18.4y²(2 + 2c_N). SF's u_0-subtraction differs from log𝒩_0 by a u-uniform
  c-number. **What remains, exactly:** (i) the domain match, stated as **(SF-N♮)** in §6.3 (the complexified fields reached in the
  fluctuation integral lie in D_c(y_0), with a linear spread bound y ≤ y_bg + c_y max|A_b|); (ii) the 1/u_0 expansion
  ν = ν_0 + O(1/u_0), which no statement of SF uses (kept only as a note, not as an item). The c-number sign: -log𝒩_c contributes
  +((N² - 1)/2)log(κu_k) + const (REVIEW_HIST_S4 N-6), consistent with SF's subtraction.]
  *Proven part planned:*
  **Lemma SF-N0:** n_c(aMb⁻¹) = n_c(M) for a, b ∈ SU(N), so log n_c(M̄_c(U)) is gauge invariant and depends on U only through
  the contour pattern of c. *PROVEN-HERE (not counted).*
- **(FP-loc) [OPEN; s to P; = PROOF's FP_U(V) item, REVIEW_S15 A2].** The exact gauge-fixed representation of the stage-k
  integral on the small-field chart, beyond the Hessian level of NA-FP: Faddeev-Popov determinant and the D_UP_resD_U^T
  insertion as a local analytic polymer in A, with the uniqueness of the slice intersection on the chart.
- **(N5-reg)_k [OPEN; s].** N5 (gap, decay, RW expansion) for the stage-k operator on Λ_k(𝔥) with the large-field exterior
  frozen, uniformly in 𝔥. (N5-sf0 is stated for backgrounds small on the whole torus.)
- **Proposition SF-A2^0 (stage 0, Gaussian + local remainder).** Let (U(V), V) be the real critical branch of BR1, in N5-sf0's
  class 𝔑(α_*), and assume (FP-loc) at stage 0 and (SF-N). Then on the fluctuation-cut domain (supp ν_∅ of SF-cut with
  p = p(g)) the stage-0 U_0-integrand, in the coordinates U_0 = e^{A}U(V), A = g_0𝒞Z, equals
  e^{-u_0S^{(0)}(U(V);V)}·n-terms·(normalised white noise)·exp(Σ_τV_τ + Σ_blog j(A_b) + FP-terms), where each V_τ depends on Z only
  through A on P_τ and |u_0V_τ| ≤ 16S_T(4g_0N_0(|𝒞|)p/r_T)³/g_0² ≤ 1024S_TN_0(|𝒞|)³p³g_0/r_T³ whenever 8N_0(|𝒞|)g_0p ≤ r_T.
  *Planned: CONDITIONAL ⇐ (FP-loc), (SF-N) (the action and Jacobian parts PROVEN-HERE via SF-T0, SF-J, SF-WN, SF-cut).*
  [RSF1-fix SF-A2-3: status now CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮) (the NORM-an domain match); see §3.2.]

### A3 (cluster expansion after the RW decoupling; re-verification of Theorem CE's hypotheses)
- **Lemma SF-WN (white-noise representation).** For every real (U, V) ∈ 𝔑(α_*) (N5-sf0) the law of 𝒞(U, V)Z under μ_wn is the
  centred Gaussian with covariance C(U, V), supported on ran Π_U = ker h_U (the slice). Under μ_wn the field Z is a product,
  ultralocal (site-by-site independent, identically distributed) probability measure. *Planned: PROVEN-HERE ⇐ N5-sf0 (not
  counted).*
- **Lemma SF-DC (dependence sets of the s-weakened field).** Setting of Theorem RW with K = Õ(U, V) and the finite-range
  property Õ(b, b') = 0 unless blocks at coarse distance ≤ r_K (level 0: r_K = 1). Let s ∈ C^𝒫 with |s_□| ≤ s̄, s̄ε_R < 1, and
  𝒴 ⊂ 𝒫 with s_□ = 0 for □ ∉ 𝒴. Call □, □' **linked** if their coarse ℓ^∞ distance is ≤ R + r_K; let 𝒴_1, …, 𝒴_q be the linked
  components of 𝒴; 𝒴_α^+ := 𝒴_α ∪ {□ : □ linked to some element of 𝒴_α}; Ω(𝒮) := ∪_{□∈𝒮}Ω_□. Then for every t ≥ 0:
  (a) for □' ∉ 𝒴: K^{-1}(s; t)1_{□'} = G_{□'}(t)1_{□'}, and its entries (x, y), y ∈ □', vanish unless x ∈ Ω_{□'};
  (b) for □' ∈ 𝒴_α: K^{-1}(s; t)(x, y) = 0 for y ∈ □' unless x ∈ Ω(𝒴_α^+);
  (c) hence, for every link x, (𝒞^Π(s)Z)(x) depends on Z only through Z on the boxes of
    D(x) := {□' ∉ 𝒴 : x ∈ Ω_{□'}} ∪ ∪{𝒴_α : x ∈ Ω(𝒴_α^+)}  (and on x's own block, via 1 - Π_U, which is block-diagonal);
  (d) if no 𝒴_α has x ∈ Ω(𝒴_α^+), every box of D(x) contains a block at coarse distance ≤ R from x's block, so D(x) lies within
  coarse ℓ^∞ distance < 3R of x's block.
  *Planned: PROVEN-HERE ⇐ Theorem RW (counted).*
- **(OP-loc)_k [OPEN; new name; s to P].** At stage k ≥ 1 the operator Õ_k (Hessian of the (I_k^E)' main term + kernel term +
  slice) is not finite range (its main-term part is exponentially local only, N2-exp). Needed: a decomposition Õ_k = Σ_XÕ_{k,X}
  into local pieces with exponential decay in d(X), and an interpolation in a second family of weakening parameters that makes
  Lemma SF-DC's finite-range input available; or an RW variant for exponentially local K with the same decoupling. *Reason
  named:* without it SF-DC (c)-(d) fails at k ≥ 1 even off 𝒴: a column y ∈ 𝒴 reaches every x through one long-range entry of K.
  **[RSF1-fix OP-1/2/3.** (1) "even off 𝒴" is WITHDRAWN: SF-DC (a) uses only R(s)1_{□'} = 0 for □' ∉ 𝒴, which holds at any range
  of K, so off-𝒴 columns stay local (REVIEW_SF_S1 R2). The real failure: every x's dependence set D(x) contains every
  𝒴-component (exponentially weak, non-zero), a statement about the polymer connectivity of the joint s-expansion. (2) What is
  proven is "SF-DC's support propagation needs finite range": necessity OF THIS ROUTE only, not of the problem (Theorem RW needs
  only (RW2)). (3) At k ≥ 1 the main-term densities are themselves only exponentially local (HIST Theorem A5 (C)), so any
  localisation item must cover the activities as well as Õ_k. ~~**Session 2 retires (OP-loc)_k:**~~ Theorem CE-exp (§7.1) needs
  neither finite range nor a second interpolation of K; its operator input is N_μ(|𝒞_k|) < ∞ (N5's ℓ¹ conclusion), and its
  activity input is the weighted-polydisc holomorphy (L-hol)_k.] **[RSF2-fix CEk-1: only the OPERATOR half of (OP-loc)_k is
  retired** (the operator enters CE-exp only through N_μ(|𝒞_k|)). The ACTIVITY half (REVIEW_SF_S1 OP-3) is not: (L-hol)_k is NOT
  VIABLE AS STATED (§7.1, CE-exp^k) and is replaced by **(L-loc)_k**, the localisation of the main-term densities into strictly local
  pieces on FIXED-radius polydiscs.]
- **Lemma SF-geo (collar tree bound).** In Setting CE, for every polymer X: X^+ is a polymer, d(X^+) ≤ d(X) + 17|X|, hence
  **d(X^+) ≤ 273d(X) + 272**. *Planned: PROVEN-HERE ⇐ CE-geo' (not counted).*
- **Corollary CE^+ (Theorem CE for collar-dependent activities).** In Setting CE, let H(X, Φ) depend on Φ|_{X^+} only and
  satisfy |H(X, Φ)| ≤ H_0e^{-κd(X)} on supp μ. Put κ' := κ/273 - 16 log 2 and H'_0 := 2^{16}e^{272κ/273}H_0. If κ' > 3κ_0 + 3
  and H'_0 ≤ c_0(κ') (Theorem CE's c_0, [S11] form), then ∫exp(Σ_XH(X))dμ = exp(Σ_YH#(Y)) with H#(Y) depending only on
  {H(X) : X^+ ⊂ Y}, H#(Y) = 0 unless Y is a polymer, and |H#(Y)| ≤ C_1H'_0e^{-(κ'-3κ_0-3)d(Y)}. (κ' > 3κ_0 + 3 ⟺ κ > 273(3κ_0 + 3 +
  16 log 2) ≈ 1.278·10⁵.) *Planned: PROVEN-HERE ⇐ Theorem CE [S11 constants] + SF-geo (counted).*
- **Lemma SF-s (s-interpolation with Cauchy bounds; standard).** Let 𝒫 be finite, s̄ > 1, F holomorphic on a neighbourhood of
  {|s_□| ≤ s̄ ∀□}. Then F(1, …, 1) = Σ_{𝒴⊂𝒫}∫_{[0,1]^𝒴}(∂^𝒴F)(σ_𝒴, 0_{𝒫∖𝒴})dσ_𝒴 and |(∂^𝒴F)(σ_𝒴, 0)| ≤ sup|F|·(s̄ - 1)^{-|𝒴|} for
  σ_𝒴 ∈ [0, 1]^𝒴. *Planned: PROVEN (standard; not counted).*
- **Proposition SF-V (re-verification of Theorem CE's hypotheses after the RW decoupling).** Items, each with its status:
  (V1) product + ultralocal measure: holds for Z (SF-WN), not for A; CE must be run in white-noise variables. [RSF1-fix V-1:
  Theorem CE as stated (product measure) requires Z-variables. A symmetric-decoupling covariance (C(s) built from s-products of
  localised pieces) would allow a correlated-Gaussian CE variant; RW's P(1 - R(s))^{-1} does not supply one, since it is not
  symmetric for s ∉ {0, 1}^𝒫 (PROOF l.5339-5344). In the RW scheme the white-noise representation is forced, not chosen.]
  (V2) "H(X) depends on Φ|_X only": fails in Z-variables; at level 0, off the s-support, it holds in collar form with CE cubes
  of fine side M ≥ (3R + 1)L (SF-DC (d)), and CE^+ covers the collar.
  (V3) at s ≡ 1 the Z-dependence of A is global (𝒞 has infinite range): the s-interpolation (SF-s) is needed; near 𝒴 the
  dependence is component-wide (SF-DC (b)), which is the joint s-Mayer step **(CE-s)** [named; ARGUED, standard in kind].
  [Session-2 note: "required" is narrowed to "required on the RW s-interpolation route". Theorem CE-exp (§7.1) localises the
  Z-dependence by per-site interpolation on the cut measure instead, with no s-walks.]
  (V4) at stage k ≥ 1 (V2) fails without (OP-loc)_k.
  (V5) "bound on supp μ": the Gaussian has unbounded support and the polymer remainders grow polynomially in Z, so CE's
  sup hypothesis fails for μ_wn; the per-site cut of SF-cut restores a product measure with bounded support (ν_Q), the cut
  complement being a fluctuation large field (RLARGE branch (ii), (SG^fl)).
  (V6) complex activities, real measure: CE needs no Remark CE-cx (the measure ν_Q is real); complex s and complex
  backgrounds enter only the activities.
  (V7) constants: CE^+'s κ > 1.278·10⁵ in M-units with N5-sf0's proven rate m_1 forces M ≥ 1.278·10⁵/m_1 fine spacings; with
  N5-w0's m_1 = 4.83·10⁻¹¹ that is ≈ 2.6·10¹⁵ ≫ (3R_* + 1)L ≈ 1.5·10¹³, so the decay requirement, not the collar, sets M.
  (V8) Remark RW-2: the Cauchy gain of SF-s needs s̄ ≫ 1, i.e. R > R_* (s̄ε_R ≤ θ).
  *Planned: PROVEN-HERE as a verdict (each item proven by the lemmas cited or by inspection of Theorem CE's statement); not
  counted.*
- **Proposition SF-A3^0 (stage-0 cluster expansion of the remainder).** Under Proposition SF-A2^0's hypotheses and (CE-s), for
  g_0 ≤ g_A3 (explicit in terms of S_T, r_T, N5-sf0's constants and c_0): log∫(stage-0 remainder)dν = Σ_YH#(Y) over polymers of
  M-cubes, with |H#(Y)| ≤ C g_0p³e^{-κ''d(Y)}, κ'' > 3κ_0 + 3, and the cut complement priced separately. *Planned: ARGUED (the
  composition through (CE-s) is not written).*

### A4 (reproduction)
- **Lemma SF-blk (blocking preserves polymer decay).** Let level-k CE cubes (side M in level-k units) be grouped into
  level-(k+1) CE cubes (L⁴ level-k cubes each, side M in level-(k+1) units). For a level-k polymer X let X̄ be the set of
  level-(k+1) cubes containing a cube of X. If |E(X)| ≤ E_0e^{-κd_k(X)} for every level-k polymer X, with κ ≥ κ_0L/(L - 1) + 1,
  then Ē(Y) := Σ_{X: X̄=Y}E(X) obeys
    |Ē(Y)| ≤ 16L⁴K_0E_0·e^{-(κL - κ_0L - 1)d_{k+1}(Y)}  for every level-(k+1) polymer Y,
  and in particular, for d_{k+1}(Y) ≥ 1, |Ē(Y)|e^{κd_{k+1}(Y)} ≤ 16L⁴K_0E_0e^{-(κ(L-1) - κ_0L - 1)}, which is ≤ E_0 iff
  κ ≥ (κ_0L + 1 + log(16L⁴K_0))/(L - 1) (≈ 302.4 at L = 3). *Planned: PROVEN-HERE ⇐ CE-geo' (counted).* (The polymers with
  d < 1 — the small sets carrying the relevant parts — are NOT contracted by blocking; they need the extraction of
  (W1-ret'^J)/(SF-irr).)
- **(SF-irr)_{k+1}, (SF-g)_k, (SG^fl)_k, (BG)_k, (RLF-5) width, (SF-last), (I_k^E)' (a3)-(a4)**: carried as HYPOTHESIS with their
  owners (PLD §9.3, FLOW §4, PLD §15.2, PLD §15.2, RLARGE §1.2, RLARGE §4.2, HIST §20.3). Not attacked in this session.
- **Theorem (SF^J)_k (target; OPEN)** = A1 + A2 + A3 + A4 above at every k with constants independent of k, K, T, 𝔥.

---

# 3. Proofs (written from 01:45 UTC, after §2)

## 3.1 A1

**Lemma SF-thr: PROVEN-HERE (not counted).** *Proof.* Let e^{iθ_j} (|θ_j| ≤ π) be the eigenvalues of U. Then
|1 - e^{iθ_j}| = 2|sin(θ_j/2)| ≤ ||1 - U||_op ≤ ε ≤ ½, and |θ_j| = 2arcsin(|1 - e^{iθ_j}|/2) ≤ 1.0108|1 - e^{iθ_j}| (2arcsin(x/2)/x
is increasing on (0, ½] with value 1.010721… at x = ½ [post-check correction, 02:08 UTC: was "1.0107", copied from HIST §20.0 (F1),
which is low in the 5th digit (s1 E4); every bound used is 1.011, unaffected]). det U = 1 gives Σθ_j ∈ 2πZ, and |Σθ_j| ≤ 1.011Nε < 2π by
ε < 2π/(1.011N); so Σθ_j = 0 and log U := W diag(iθ_j)W^† (U = W diag(e^{iθ_j})W^†) is traceless anti-Hermitian, i.e. in su(N),
and it is the principal log. |log U|_op = max|θ_j| ≤ 1.011ε, |log U|_HS = (Σθ_j²)^{1/2} ≤ 1.011√Nε. The consequence is
the case ε = ε_1. ∎ (Lemma TL of PLD §15.1 gives the tracelessness under ε_1 < 2sin(π/N); the present bound is the
quantitative form N5's class needs.)

**Corollary SF-thr-k: CONDITIONAL ⇐ (N5-unif)** [post-proof restatement, 01:46 UTC; the pre-stated "⇐ (BG-unif)" is
replaced because the step (BG-unif) ⇒ level-uniform N5 is REVIEW_S20's sentence "Then (I_i) holds with ε_i ≡ min(ε_BG,
ε_*/C_BG) … uniformly in i", stated there without proof: ARGUED]. *(N5-unif):* N5 (Corollary N5-sf1's conclusions) holds at
every level k with one plaquette threshold ε_N5 > 0 independent of k, K, T. *Proof.* Lemma SF-thr with ε_N5 in place of
ε_*. ∎ Chain: (N5-unif) ⇐[ARGUED, REVIEW_S20 Part 2] (BG-unif) + Proposition NAH-ind's other inputs ((MIN_i), the region
form (b), m^{(i+1)} ≤ Lm_1^{(i)}/2). The soft clause |ρ_c| ≤ ε_N5 is not implied by any plaquette cut: it stays a
kernel-mismatch event (RLARGE §3.1, PROVEN branch).
**[RSF1-fix SF-thr-k-1/2, session 2.] Chain replaced:** (N5-unif) ⇐ [PROVEN implication, PROOF [S21] Proposition NAH-unif,
l.6036-6054, not counted, unreviewed] (H-K) + (H-C). (H-K) is measured with margin ≈ 10 at levels 0-1 (c37: K_p^♯ = 0.062,
0.103; not certified); (H-C) is OPEN (Lemma E3's recursion compounds by ≈ 1.3·10³ per level, PROOF l.6064-6066); (BG-unif) (iv)
via the composite contraction (REVIEW_S20 (R-b)) is the alternative route to (H-C). The implication (BG-unif) ⇒ (N5-unif) is
kept as ARGUED only as that (R-b) route. The last sentence above is withdrawn as stated: it holds for the INTEGRATED field's
soft fluctuation (kernel-mismatch event); the BACKGROUND's soft fluctuation is bounded by V's curvature (BR1 (iii), NAH-unif).
Corollary SF-thr-k's status: CONDITIONAL ⇐ (N5-unif) ⇐ (H-K) + (H-C).
**[RSF2-fix SF-thr-k (stale after PROOF [R21-fix S21-5] and [S22]).** The chain above is replaced by PROOF's current text:
Proposition NAH-unif is "GAP as stated" (PROOF l.6070); its corrected form is **Proposition NAH-unif′** ([S22], PROVEN as an
implication, not counted): (N5-unif) ⇐ **(H-K) + (H-C⁺) + (H-ℂ)**, with (H-G) DERIVED (Lemma HG-ind: CURV1_i (ρ) ⇒ (H-G)_{i+1}; HG1
at level 1). Status of the three (PROOF l.6093-6108, l.6238-6259): (H-K) measured, K_p^♯ ≈ 0.11-0.13 at level 0 on closed inputs,
margin ≈ 8, two rows, not certified (the "margin ≈ 10" and "K_p^♯ = 0.062, 0.103" above are withdrawn); (H-C⁺) (level-uniform
C_θ^{(i)}, C_θ^{ρ,(i)} besides the (H-C) constants) is NOT delivered by the per-level route in sup norms (failure mode CURV-F2′
occurs: ≥ 100 per level); (H-ℂ) OPEN. The composite alternative is Proposition COMP ⇐ (CL-0)-(CL-3), with COMP-F1 occurring for
sup-curvature norms and (CL-cl) OPEN. **Corollary SF-thr-k: CONDITIONAL ⇐ (N5-unif) ⇐ (H-K) + (H-C⁺) + (H-ℂ).**]

**(BG-unif), (BG-loc): not attacked** (statements in §2). Remark on (BG-loc): N5-sf0's proof is local (RW's compressions to
the boxes Ω_□ and Lemma AX on non-wrapping boxes), so the N5 half of a region version needs only a boundary convention for
the boxes meeting Ω^c_k; the background half (the tower with frozen exterior) is the substantive part [inference].

## 3.2 A2

**Lemma SF-J: PROVEN-HERE (counted).** *Proof.* (1) *Density.* For A, B ∈ su(N), Duhamel's formula gives
d/dt e^{A+tB}|_{t=0} = ∫_0^1e^{(1-σ)A}Be^{σA}dσ = e^A∫_0^1e^{-σ ad A}Bdσ = e^A·f(ad A)B, f(z) := (1 - e^{-z})/z (entire, f(0) = 1).
So in the left trivialisation d exp_A = f(ad A), and the pull-back of the bi-invariant volume form under A ↦ e^AU_0 (right
invariance removes U_0) is |det f(ad A)|dA up to a constant c_N. (2) *Chart* [post-proof correction, 01:52 UTC: the first
version claimed "a diffeomorphism onto a set of full Haar measure"; that is true for N = 2 only]. On D_N := {A ∈ su(N):
||A||_op < π} the map A ↦ e^A is injective (if ||A||, ||B|| < π and e^A = e^B, the principal logs agree: A = B), and with (3)
below det f(ad A) ≠ 0 there, so it is a diffeomorphism onto the open set E_N := exp(D_N) = {U : -1 ∉ spec U, principal log
traceless}. E_N ⊃ {U : ||1 - U||_op ≤ ε^thr_N} (Lemma SF-thr). For N = 2 every principal log of an SU(2) element without
eigenvalue -1 is traceless (angles ±θ), so E_2 has full Haar measure. For N ≥ 3 it does NOT: U ∈ SU(3) with eigen-angles
(5π/6, 5π/6, π/3) has principal log of trace 2πi, and since that trace is continuous with values in 2πiZ, a neighbourhood of U
misses E_3 (positive measure). So the chart identity ∫_Bf dU = c_N∫_{log B}f(e^AU_0)j(A)dA holds for Borel B ⊂ E_NU_0, in
particular for every B inside the small-fluctuation set {||1 - UU_0⁻¹||_op ≤ ε^thr_N}; it is a statement about the
small-fluctuation region only. [RSF1-fix SF-J-1: this correction is specific to the chart D_N = {||A||_op < π} and is NOT a
property of the exponential chart. On D'_N := {A ∈ su(N) : spread of the eigen-angles < 2π} the exponential map covers a
Haar-full set for every N (Lemma SF-J', §7.3, PROVEN-HERE). Measured Haar fraction of E_N = exp(D_N): 0.975 (SU(3)), 0.948
(SU(4)) (REVIEW_SF_S1 R3: 0.9753, 0.9476; s2 D1-D2 re-measure). SF uses D_N because its BOUNDS live there (SF-J (5)-(6) need
||A||_op ≤ π/2; SF-T0 needs ρ ≤ r_T/8); the complement is priced as a fluctuation large field either way, so no conclusion of SF
changes.] (3) *Product formula.* On gl(N, C), ad A = A ⊗ 1 - 1 ⊗ A^T has eigenvalues λ_a - λ_b (a, b = 1, …, N, λ the
eigenvalues of A, with algebraic multiplicity; Jordan form). sl(N, C) = su(N)⊗C is invariant and gl = sl ⊕ C·1 with
ad A(1) = 0, so on sl(N, C) the eigenvalues are the same list minus one zero. f(0) = 1, hence
det f(ad A|_sl) = Π_{a≠b}f(λ_a - λ_b) = Π_{a<b}f(z_ab)f(-z_ab), z_ab := λ_a - λ_b, and f(z)f(-z) = (2cosh z - 2)/z² =
(sinh(z/2)/(z/2))². So j(A) = Π_{a<b}(sinh w_ab/w_ab)², w_ab = z_ab/2. For A ∈ su(N), λ_a = iθ_a, w_ab = i(θ_a - θ_b)/2, and
sinh w/w = sin(μ/2)/(μ/2) (μ := θ_a - θ_b, |μ| < 2π when ||A||_op < π), so every factor is > 0 and j = |det f(ad A)| > 0.
(4) *Holomorphic log.* ℓ(z) := log(sinh(z/2)/(z/2)) (branch with ℓ(0) = 0) is holomorphic on |z| < 2π, where sinh(z/2)/(z/2) has
no zero. log f(z) = -z/2 + ℓ(z) there. For ||A||_op < π the spectral radius of ad A is ≤ 2||A||_op < 2π, so
L(A) := tr ℓ(ad A) (holomorphic functional calculus on gl; the N zero eigenvalues contribute ℓ(0) = 0) is holomorphic in A,
L(A) = Σ_{a≠b}ℓ(z_ab), and e^{L(A)} = e^{tr(log f)(ad A) + tr(ad A)/2} = det f(ad A) because tr ad A = 0. So log j := L.
(5) *Bound.* For |w| ≤ π/2: sinh w/w = Π_{n≥1}(1 + ζ_n), ζ_n := w²/(n²π²), |ζ_n| ≤ 1/(4n²) ≤ ¼. The series Σ_nLog(1 + ζ_n)
(principal logs) converges uniformly to a continuous logarithm of sinh w/w vanishing at 0, hence equals ℓ(2w). With
|Log(1 + ζ)| ≤ |ζ|/(1 - |ζ|) ≤ (4/3)|ζ|: |ℓ(2w)| ≤ (4/3)|w|²Σ_n1/(n²π²) = (2/9)|w|². If ||A||_op ≤ π/2 then |w_ab| = |λ_a - λ_b|/2 ≤
||A||_op ≤ π/2 and |L(A)| ≤ Σ_{a≠b}(2/9)|z_ab|²/4 = (1/18)Σ_{a,b}|λ_a - λ_b|² = (1/18)(2NΣ_a|λ_a|² - 2|Σ_aλ_a|²) =
(N/9)Σ_a|λ_a|² ≤ (N/9)|A|²_HS (tr A = 0; Schur's inequality Σ|λ_a|² ≤ ||A||²_F). (6) *Quadratic part.* Σ_nζ_n = w²/6, so
ℓ(2w) - w²/6 = Σ_n(Log(1 + ζ_n) - ζ_n), |Log(1 + ζ) - ζ| ≤ |ζ|²/(2(1 - |ζ|)) ≤ (2/3)|ζ|², giving |ℓ(z) - z²/24| ≤
(2/3)|w|⁴Σ_n(nπ)^{-4} = |w|⁴/135 = |z|⁴/2160 (|z| ≤ π). Σ_{a≠b}z_ab²/24 = (2NΣλ_a² - 2(Σλ_a)²)/24 = (N/12)tr(A²). So
L(A) = (N/12)tr(A²) + R_4(A), |R_4| ≤ (1/2160)Σ_{a≠b}|z_ab|⁴ ≤ (1/2160)(4||A||²_op)(2N|A|²_HS) ≤ **(N/270)|A|⁴_HS** (C_J = N/270). ∎
*Reading.* In the stage-k chart U_b = e^{A_b}U_b^bg the Jacobian is Π_bj(A_b): a single-link (ultralocal) activity, holomorphic,
real-positive on real points, of size (N/9)|A_b|² = O(g²|Z|²) with A = O(g). Its quadratic part (N/12)tr A_b² = -(N/12)|A_b|²_HS is a
link-mass term of order g² relative to the Gaussian; it is gauge-covariant under the fluctuation group (Ad-invariant per link).
(Check s1 B verifies the product formula, the bound and C_J numerically.)

**Lemma SF-cut: PROVEN-HERE (not counted).** *Proof.* (a) Π_x(χ_x + (1 - χ_x)) = Σ_QΠ_{x∈Q}(1 - χ_x)Π_{x∉Q}χ_x pointwise (finite
product); integrate F times each term against the product measure and divide by the (positive) normalisations; each ν_Q is
a product of probability measures. (b) Chernoff: μ_x(|Z(x)|² > p²) ≤ e^{-p²/4}E e^{|Z(x)|²/4} = e^{-p²/4}(1 - ½)^{-n/2}. (c) |Z_b|
≤ |Z(x)| for b based at x. ∎ (Check s1 C compares (b) with the exact χ²_n tail.)

**Lemma SF-T0: PROVEN-HERE (existence of constants, as Lemma N5-an; counted).** *Proof.* (1) *Term types.* Up to translation
by L and the B_4 action there are finitely many term types (plaquettes; the kernel terms of one coarse link c, whose variables
are V_c and the fine links of the S4' contours of c, a fixed pattern of ≤ p_L links per contour in two blocks). For each type,
τ̂(u, v) := the term as a function of the logs (u_b, v_c) of its variables is real-analytic on a neighbourhood of 0: the
plaquette term N⁻¹Re tr(1 - e^{u_1}e^{u_2}e^{-u_3}e^{-u_4}) is entire in (u, ū) and real-analytic in the real coordinates; the
kernel term φ_{M̄}(V) = N⁻¹[Re tr(W_0(M̄)⁻¹M̄) - Re tr(V⁻¹M̄)] is real-analytic near 0 because M̄ is a polynomial in the link
entries and W_0(M̄) = e^{X_0(M̄)} with X_0 real-analytic in M̄ near 1 (NA-alg (a): fixed point of a real-analytic contraction,
analytic implicit function theorem; the argument of Lemma N5-an's proof, PROOF l.5258-5261). A real-analytic function on a
neighbourhood of 0 in R^q continues holomorphically to a complex polydisc around 0 with finite sup on a smaller closed polydisc.
Take r_T ≤ 1/8 below every such radius and S_T := the max of the sups over the closed polydiscs of radius r_T (finitely many
types). (2) *Gauge.* Each term is gauge invariant (S_W, and φ(gV; g·M) = φ(V; M) with M̄_c(gU) = g(c_X)M̄_c(U)g(c_Y)⁻¹, Lemma N5-cov's
proof). For a real gauge g, (g·e^AU)_b = e^{Ad_{g(x)}A_b}(gU)_b and |Ad_{g(x)}A_b| = |A_b|. (3) *Composition.* With |u_b| :=
|log(gU)_b| ≤ r_T/4 and |A_b| < r_T/4: |A_b| + |u_b| < r_T/2 ≤ 1/16, and for |X| + |Y| ≤ ¼ the BCH logarithm satisfies
|log(e^Xe^Y)| ≤ 2(|X| + |Y|) (||e^Xe^Y - 1|| ≤ e^{|X|+|Y|} - 1, |log(1 + W)| ≤ |W|/(1 - ||W||); op or HS norm) and is holomorphic
in (X, Y). So A ↦ log(e^{Ad A_b}(gU)_b) maps {max|A_b| < r_T/4} holomorphically into the polydisc of radius r_T, and
A ↦ τ(e^AU; V) = τ̂(log(e^{Ad A}(gU)), log(gV)) is holomorphic there, bounded by S_T. (4) *Remainder.* Fix A with ρ := max|A_b|
≤ r_T/8, put a := A/ρ and G(ζ) := τ(e^{ζa}U; V), holomorphic and bounded by S_T on |ζ| < r' := r_T/4. G(ρ) = τ(e^AU),
ρG'(0) = Dτ(U)·A, ρ²G''(0)/2 = ½D²τ(U)(A, A) (the derivatives along t ↦ e^{tA}U, the left-trivialised Hessian of Setting
N5-bg). Cauchy: |G^{(j)}(0)/j!| ≤ S_T/r'^j, so |G(ρ) - Σ_{j≤2}G^{(j)}(0)ρ^j/j!| ≤ S_T(ρ/r')³/(1 - ρ/r') ≤ 2S_T(4ρ/r_T)³ (ρ/r' ≤ ½),
which is ≤ the pre-stated 16S_T(4ρ/r_T)³. (5) *Criticality.* Σ_ττ = N⁻¹F(·, V), F := S_W + κ_kerΣ_cφ̂_c [RSF1-fix SF-T0-1: the kernel strength, Setting N5-bg's κ_0 ∈
[κ_-, κ_+], is renamed κ_ker throughout SF; κ_0 means only CE's 16 log 12800] (BR1's functional,
PROOF [S20] l.5543; S_W = NΣs, φ̂ = Nφ). BR1 (ii) (NA-crit with Lagrange multipliers) makes U(V) a critical point of F(·, V)
in every direction, so Σ_τDτ(U(V))·A = N⁻¹d/dt F(e^{tA}U(V), V)|_0 = 0 for every A. ∎
*What is not done:* r_T, S_T are not computed (as in N5-an); the hypothesis "a gauge with logs ≤ r_T/4 on each pattern" holds for
(U(V), V) when the BR1 background is curvature-small enough, by BR1 (iii) and Lemma AX on the pattern's box (10p_Lℓε' ≤ r_T/4).

**Lemma SF-N0: PROVEN-HERE (not counted).** *Proof.* Re tr(V⁻¹aMb⁻¹) = Re tr((a⁻¹Vb)⁻¹M), and
W_0(aMb⁻¹) = aW_0(M)b⁻¹ (the maximiser set is mapped bijectively), so φ_{aMb⁻¹}(V) = φ_M(a⁻¹Vb); the substitution V ↦ aVb⁻¹
preserves Haar measure, so n_c(aMb⁻¹) = n_c(M). With M̄_c(gU) = g(c_X)M̄_c(U)g(c_Y)⁻¹, log n_c(M̄_c(·)) is gauge invariant; it
depends on U only through M̄_c(U), i.e. on the contour links of c. ∎ (SF-N)'s analytic content is not attacked.

**Proposition SF-A2^0: CONDITIONAL ⇐ (FP-loc)_0, (SF-N)** [post-proof correction, 01:46 UTC: the pre-stated bound omitted
the normalisation factor √N of A; the corrected form is below]. *Statement as proven.* Let (U(V), V) be the BR1 critical
branch, real, in 𝔑(α_*), with a gauge of logs ≤ r_T/4 on every term pattern (Lemma SF-T0's hypothesis). Write U_0 = e^{A}U(V)
link by link (chart of SF-J (2)). Then, exactly,
  ∫F(U_0)Π_bdU_0(b) = c_N^{#b}∫F(e^AU(V))Π_bj(A_b)dA  (every F ∈ L¹ supported where ||1 - U_0(b)U(V)_b⁻¹||_op ≤ ε^thr_N ∀b;
  [post-proof correction, 01:52 UTC: was "every F ∈ L¹"; the complement is a fluctuation large field, priced elsewhere]),
and the stage-0 action splits as u_0S^{(0)}(e^AU(V); V) = u_0S^{(0)}(U(V); V) + (u_0/2N)⟨A, H A⟩ + Σ_τu_0V_τ(A), H the Hessian of F(·, V)
at U(V) (no linear term: SF-T0 (5)), V_τ the cubic remainders. On the slice with the gauge-fixing insertion of Setting N5-bg
(O = H + D_UP_resD_U^T; this is the step that needs (FP-loc)), the Gaussian factor is that of A = g_0√N·𝒞Z, Z white noise
(SF-WN, with covariance Ng_0²C = (N/u_0)C [RSF1-fix SF-A2-2; was "C/u_0·N"]). On supp ν_∅ (SF-cut with cut p): |A_b| ≤ g_0√N·N_0(|𝒞|)p for every b, and, whenever
8√N·N_0(|𝒞|)g_0p ≤ r_T,
  |u_0V_τ(A)| ≤ 2S_T(4g_0√NN_0(|𝒞|)p/r_T)³/g_0² = 128S_TN^{3/2}N_0(|𝒞|)³p³g_0/r_T³,  |log j(A_b)| ≤ (N²/9)g_0²N_0(|𝒞|)²p².
*Proof.* The chart identity: SF-J (1)-(2) per link (product of charts, on the support stated). The split: SF-T0 (4)-(5), summed over τ
(finitely many terms on a finite torus). |A_b| ≤ g_0√NΣ_{b'}|𝒞|(b, b')|Z_{b'}| ≤ g_0√NN_0(|𝒞|)p (block norms; SF-cut (c)). The
bounds: SF-T0 (4) with ρ = g_0√NN_0(|𝒞|)p ≤ r_T/8, and SF-J (5) (|A_b|_HS² ≤ g_0²N·N_0²p², and ||A_b||_op ≤ r_T/8 ≤ π/2). ∎
*Conditional part.* The kernel normalisations -Σ_clog n_c(M̄_c(e^AU(V))) are a gauge-invariant local function of A (SF-N0) whose
analytic bounds are (SF-N); their linear term in A does NOT vanish at U(V) (U(V) is critical for F, not for F + Σlog n_c) and is
of order g_0p per coarse link: a source term the cluster expansion must carry. **[RSF1-fix SF-A2-1: the size is overstated.**
By NORM-an, log n_c = c-number + 𝔫_c with |𝔫_c| = O(y²) holomorphic; Lemma SF-src (§7.3, PROVEN-HERE ⇐ NORM-an + (SF-N♮)) gives
|𝔫_c(e^AU(V)) - 𝔫_c(U(V))| ≤ 8K_𝔫c_yy_bgρ + 9K_𝔫c_y²ρ² with ρ = max|A_b| ≤ g_0√NN_0(|𝒞|)p: the linear source is
O(y_bg·g_0√NN_0(|𝒞|)p) per coarse link, proportional to the background's contour spread y_bg, and it VANISHES at flat backgrounds
(consistent with EXISTENCE Proposition NA-3; REVIEW_SF_S1 R5 measures it linear in the spread). It is u-independent; no u_0
enhancement.] The FP determinant and the D_UP_resD_U^T
insertion beyond the Hessian level are (FP-loc). N_0(|𝒞|) is N5-sf0 (b)'s ℓ¹ bound (finite; astronomically large at the
evaluated constants (RW (ii)'s 8coth⁴(a/2)/(√γ'(1 - ε_R)) with a ≈ 5·10⁻¹¹, or RW-ℓ²'s sup-norm form), so the smallness
condition g_0p ≤ r_T/(8√NN_0(|𝒞|)) is a g-independent but extreme threshold).

## 3.3 A3

**Lemma SF-WN: PROVEN-HERE ⇐ Theorem N5-sf0 (not counted).** *Proof.* For real (U, V) ∈ 𝔑(α_*), N5-sf0 (b) gives Õ > 0 real
symmetric; Π_U is an orthogonal projection (Π_U^T = Π_U = Π_U², from its formula) commuting with Õ (Õ = Π_UOΠ_U + (1 - Π_U)), and
Õ = 1 on ran(1 - Π_U). So Õ^{-1/2} (positive square root) is symmetric, commutes with Π_U, and equals 1 on ran(1 - Π_U). Hence
𝒞 = Õ^{-1/2} - (1 - Π_U) = Π_UÕ^{-1/2}Π_U is symmetric with range in ran Π_U = ker h_U, and 𝒞𝒞^T = 𝒞² = Π_UÕ^{-1}Π_U = Õ^{-1} - (1 - Π_U) = C.
A linear image of a standard Gaussian vector is the centred Gaussian with covariance 𝒞𝒞^T. μ_wn is a product over links and
Lie-algebra components of identical standard normals by definition. ∎ For complex s, 𝒞^Π(s)Z is a complex linear image of
real white noise: the measure stays μ_wn (real, product); only the integrand becomes complex.

**Lemma SF-DC: PROVEN-HERE ⇐ Theorem RW (counted).** *Proof.* Notation of Theorem RW: G_□(t) = (K_{Ω_□} + t)^{-1} extended by
zero (entries vanish unless both indices are in Ω_□), R_□(t) = -1_{Ω_□^c}KG_□(t)1_□, P(t) = Σ_□G_□(t)1_□, R(s; t) := Σ_□s_□R_□(t),
K^{-1}(s; t) = P(t)Σ_{n≥0}R(s; t)^n (convergent: N_0(Σ|s_□||R_□|) ≤ s̄ε_R < 1, RW (iv)).
(a) R_□1_{□'} = R_□1_□1_{□'} = 0 for □ ≠ □', so R(s)1_{□'} = s_{□'}R_{□'}1_{□'} = 0 for □' ∉ 𝒴; then K^{-1}(s; t)1_{□'} = P1_{□'} =
G_{□'}1_{□'}, whose entries vanish unless x ∈ Ω_{□'}. (This is RW (iv)'s decoupling.)
(b) *Support propagation.* If v is supported in the links of a box □, then G_□v is supported in Ω_□ (blocks at distance ≤ R
from □), KG_□v in the blocks at distance ≤ R + r_K from □ (finite range), and R_□v = -1_{Ω_□^c}KG_□v in blocks at distance
∈ (R, R + r_K]; every box meeting that set is linked to □. Fix y ∈ □' ∈ 𝒴_α and let 𝒮_n be the set of boxes meeting
supp R(s)^ne_y. Induction: 𝒮_0 = {□'}; R(s)^{n+1}e_y = Σ_{□∈𝒮_n∩𝒴}s_□R_□1_□R(s)^ne_y, so every box of 𝒮_{n+1} is linked to an
element of 𝒮_n ∩ 𝒴. If (inductively) 𝒮_n ∩ 𝒴 ⊂ 𝒴_α, then 𝒮_{n+1} ⊂ 𝒴_α^+ and 𝒮_{n+1} ∩ 𝒴 ⊂ 𝒴_α (a box of 𝒴 linked to 𝒴_α is in the
component 𝒴_α). Finally Pw = Σ_□G_□1_□w is supported in ∪{Ω_□ : □ meets supp w}, so K^{-1}(s; t)e_y is supported in
Ω(∪_n𝒮_n) ⊂ Ω(𝒴_α^+).
(c) 𝒞^Π(s) = π⁻¹∫_0^∞t^{-1/2}K^{-1}(s; t)dt - (1 - Π_U) entrywise (RW (iv) defines 𝒞(s) this way; the integral converges absolutely
entry by entry, RW (iii)-(iv) bounds), so an entry that vanishes for every t vanishes after integration; 1 - Π_U is block-
diagonal (Setting N5-bg). (𝒞^Π(s)Z)(x) = Σ_y𝒞^Π(s)(x, y)Z_y, and by (a), (b) the y with a non-zero entry lie in a box □' ∉ 𝒴 with
x ∈ Ω_{□'}, or in a box of some 𝒴_α with x ∈ Ω(𝒴_α^+), or in x's block.
(d) If x ∉ Ω(𝒴_α^+) for every α, then D(x) = {□' ∉ 𝒴 : x ∈ Ω_{□'}}, and x ∈ Ω_{□'} means a block of □' is at coarse distance ≤ R
from x's block; □' has side < 2R, so each of its blocks is at distance ≤ R + 2R - 1 < 3R. x's own block: its box □(x) ∉ 𝒴 (else
x ∈ Ω_{□(x)} ⊂ Ω(𝒴^+)) and x ∈ Ω_{□(x)}, so it is in D(x) already. ∎
*Consequence for CE cubes (level 0).* Take CE cubes of fine side M ≥ 3RL + L. A site within fine ℓ^∞ distance < 3RL + L ≤ M of a
site x lies in an M-cube touching x's M-cube. So for any function H(X; 𝒞^Π(s)Z) of the field on a union X of M-cubes all of whose
links obey (d)'s hypothesis, H depends on Z only on X^+. (Check s1 A verifies (a)-(d) as exact zero patterns in a d = 2
model.)

**(OP-loc)_k: OPEN (named).** *Why (b) fails at k ≥ 1 without it (PROVEN-HERE, elementary).* (b)'s support propagation used
K(x, z) = 0 beyond r_K blocks. If K has a non-zero entry K(x, z) with z ∈ Ω_□, □ ∈ 𝒴, and x at arbitrary distance (exponentially
small but non-zero, as for the level-k main-term Hessian, N2-exp), then R_□e_y has a non-zero component at x and P maps it into
Ω_{□(x)}: (𝒞^Π(s)Z)(x) depends on Z_y. So the dependence sets are not finite at any distance, and CE^+'s collar hypothesis fails.

**Lemma SF-geo: PROVEN-HERE ⇐ CE-geo' (not counted).** *Proof.* X^+ is connected (each added cube touches X). Two closed lattice
cubes Q = k + [-½, ½]⁴, Q' = k' + [-½, ½]⁴ that meet have Q ∩ Q' = Π_i(intervals), each factor either [k_i - ½, k_i + ½] (k'_i = k_i)
or a single endpoint k_i ± ½; choosing an endpoint in each full factor gives a vertex of Q in Q'. So every cube of X^+ touching
Q ∈ X contains a vertex of Q. Let τ be a connected union of segments of length ℓ meeting every closed cube of X. For each
Q ∈ X pick p_Q ∈ τ ∩ Q, a segment from p_Q to a vertex v_Q of Q (inside the convex Q, length ≤ diam Q = 2), and an edge path
through all 16 vertices of Q starting at v_Q (the reflected 4-bit Gray code translated by v_Q: a Hamiltonian path of 15 unit
edges; the hypercube graph is vertex-transitive). The union τ' is connected, has length ≤ ℓ + 17|X|, and meets every closed
cube of X^+. Infimum over τ: d(X^+) ≤ d(X) + 17|X| ≤ d(X) + 17·16(1 + d(X)) = 273d(X) + 272 (CE-geo': |X| ≤ 16(1 + d(X))). ∎
(Check s1 D verifies the Gray path and the vertex property.)

**Corollary CE^+: PROVEN-HERE ⇐ Theorem CE ([S11] constants) + SF-geo (counted).** *Proof.* exp(Σ_XH(X)) = exp(Σ_YH'(Y)),
H'(Y) := Σ_{X: X^+=Y}H(X) (regroup the finite sum). H'(Y) depends on Φ|_Y only; H'(Y) = 0 unless Y = X^+ for a polymer X, hence
unless Y is a polymer. By SF-geo, d(X) ≥ (d(Y) - 272)/273 when X^+ = Y, and the X with X^+ = Y are subsets of Y, at most
2^{|Y|} ≤ 2^{16(1+d(Y))} of them (CE-geo'). So on supp μ, |H'(Y)| ≤ 2^{16}e^{16log2·d(Y)}·H_0e^{272κ/273}e^{-κd(Y)/273} = H'_0e^{-κ'd(Y)}.
Theorem CE applied to H' (hypotheses κ' > 3κ_0 + 3, H'_0 ≤ c_0(κ')) gives the conclusion; H#(Y) depends on {H'(Y') : Y' ⊂ Y} =
{H(X) : X^+ ⊂ Y}. ∎ κ' > 3κ_0 + 3 ⟺ κ > 273(3κ_0 + 3 + 16log 2) = 1.2779·10⁵ (s1 E).
*Remark (cost).* The rate loss 1/273 and the factor e^{272κ/273} in H'_0 are the price of using CE as a black box; re-running CE's
Step 2 with "X_i^+ disjoint" would be sharper ~~but is not needed for an existence statement~~. **[RSF2-fix CEk-2: the second
half is WITHDRAWN.** The 1/273 rate loss and the e^{272κ'} norm factor BLOCK ITERATION: at L = 3, L(κ_c - 3κ_0 - 3 - κ_0) - 1 <
273(κ_c + 16 log 2) + 1296W for every κ_c (REVIEW_SF_S2 B-6), so CE^+/CE-exp cannot be composed across levels. The collar-native
re-proof is Theorem CE-col (§10.3), which removes both.]

**Lemma SF-s: PROVEN (standard; not counted).** *Proof.* One variable: h(1) = h(0) + ∫_0^1h'(σ)dσ for h holomorphic near [0, 1].
Apply it in each of the finitely many variables in turn (Fubini; everything continuous on a compact set) and expand the
product of the |𝒫| two-term sums: the term indexed by 𝒴 carries ∫_0^1∂_{s_□}dσ_□ for □ ∈ 𝒴 and s_□ = 0 for □ ∉ 𝒴. Cauchy's
estimate on the polydisc of radius s̄ - 1 about (σ_𝒴, 0) in the 𝒴-coordinates (contained in the domain, |σ_□| + s̄ - 1 ≤ s̄)
gives |∂^𝒴F| ≤ sup|F|·(s̄ - 1)^{-|𝒴|}. ∎ (Applied to G(s) := ∫F(𝒞^Π(s)Z)dν(Z): G is holomorphic on |s_□| < s̄ whenever s̄ε_R < 1
(RW (iv), entries holomorphic and uniformly bounded) and F is holomorphic and bounded on the set of complex fields reached
from supp ν; differentiation under ∫dν is legitimate because supp ν_∅ is compact and the integrand is jointly continuous.)

**Proposition SF-V (re-verification of Theorem CE's hypotheses after the RW decoupling): PROVEN-HERE as a verdict (not
counted).** Theorem CE's hypotheses (PROOF l.1825-1830, l.1868-1871): (H1) fields on sites, μ = Π_xμ_x a product probability
measure; (H2) H(X, Φ) depends on Φ|_X only; (H3) |H(X, Φ)| ≤ H_0e^{-κd(X)} on supp μ with κ > 3κ_0 + 3 ≈ 457 and H_0 ≤ c_0(κ).
- (V1) (H1) holds for Z (SF-WN; sites = fine sites x, Φ(x) = Z(x) ∈ R^n), and fails for the fluctuation field A (correlated
  Gaussian, covariance C with infinite range). **So CE is applied in white-noise variables.** ✓ proven.
- (V2) (H2) in Z-variables: fails for s ≡ 1; holds in the collar form "depends on Φ|_{X^+}" at level 0 off the s-support with
  CE cubes M ≥ (3R + 1)L (SF-DC (d) and its consequence); CE^+ (proven) covers the collar. ✓ proven.
- (V3) The global Z-dependence at s ≡ 1 forces the s-interpolation (SF-s); near 𝒴 the dependence is component-wide (SF-DC (b),
  (c)); a single CE run therefore cannot be applied term by term in 𝒴: the joint step **(CE-s)** — sum over 𝒴 and Mayer
  expansion of the integrand together, polymers = connected unions of 𝒴-components (with their Ω^+) and CE^+ polymers — is
  required. [ARGUED, standard in kind (Balaban; Dimock II-III [not read this session]); not written.]
- (V4) At stage k ≥ 1, (V2) fails without (OP-loc)_k (§3.3 above, elementary).
- (V5) (H3) "on supp μ": supp μ_wn = all of R^{n·#sites}; the cubic remainders V_τ grow like |Z|³ and log j like |Z|², so no
  finite H_0 exists under μ_wn: CE's Step 1 (|e^z - 1| ≤ 2|z| for |z| ≤ log 2) fails. Under ν_Q (SF-cut) the support is bounded on
  Q^c and the measure is still a product (H1 ✓). The cut complement Q ≠ ∅ is a fluctuation large field with weight
  ≤ (2^{n/2}e^{-p²/4})^{|Q|} (SF-cut (b)), to be priced as RLARGE §3.2 branch (ii) [(SG^fl)]; and the Q-sites still carry
  unbounded Z, so the polymers touching Q need a separate (large-fluctuation) bound — named, part of (CE-s). ✓ proven
  (failure and repair route); the repair's completion is (CE-s).
- (V6) CE is used with a REAL product measure (ν_Q); complexity sits in the activities (complex s, complex backgrounds), which CE
  allows ("complex allowed"). Remark CE-cx is not needed. ✓ by inspection.
- (V7) Constants. CE^+ needs κ > 1.278·10⁵ in M-units. An activity decaying like e^{-m_1·(fine distance)} has, in M-units,
  rate ≤ m_1M (one M-unit of tree length spans ≤ M fine spacings in sup distance [inference: the precise conversion between
  the activities' decay and d(X) is part of (CE-s)]). With N5-w0's m_1 = m/2 = 4.83·10⁻¹¹ (PROOF l.5404): M ≥ 1.278·10⁵/m_1 ≈
  2.65·10¹⁵ fine spacings, against the collar requirement (3R_* + 1)L ≈ 1.5·10¹³ (R_* ≈ 1.7·10¹²): the decay requirement sets M.
  Then H'_0 ≤ c_0(κ') needs the per-M-cube activity ≲ e^{-2κ'-272κ/273}, i.e. g_0p³ (Prop. SF-A2^0) times M⁴ ≈ 5·10⁶¹ below
  e^{-1.3·10⁵}-type numbers: g-independent but extreme. (s1 E.) [RSF1-fix V-2: the M ≳ 2.6·10¹⁵ requirement comes from the
  WALK (𝒴-generated) activities of (CE-s). Activities supported on one M-cube plus collar (all of SF-A2^0's local terms) have
  H(X) = 0 for d(X) > 0, so they satisfy |H| ≤ H_0e^{-κd} for every κ. So (V7) is a statement about (CE-s)'s 𝒴-activities, and the
  [inference] tag stays. Session 2: in Theorem CE-exp (§7.1) the decay of the field map is used through the site-interpolation,
  which needs μM ≥ 3κ' + 4 log M + 8 with κ' ≈ 469, not κ > 1.278·10⁵; s2 C2 records M_min.]
- (V8) SF-s's Cauchy gain (s̄ - 1)^{-|𝒴|} must beat the walk combinatorics; with N5-sf0's R_* only s̄ < 2 (ε_R ≤ ½), so R must be
  enlarged (Remark RW-2): R ≥ R_* + (2/(aL))log(s̄/(2θ)). ✓ by inspection of RW (iv). [RSF1-fix V8 note: Theorem N5-sf0 (b) is
  stated for R = R_*; using R > R_* needs RW's hypotheses at the larger R (they hold: ε_R decreases in R) and T ≥ 4R + 6 in place
  of T_0 = 4R_* + 6. Theorem CE-exp (§7.1) does not use the s-interpolation, so (V8) is needed only on the (CE-s) route.]
∎

**Proposition SF-A3^0: ARGUED (not counted).** The route: SF-cut (per-site cut, sum over Q) → SF-s in the walk parameters
(R enlarged per V8) → for each (Q, 𝒴), SF-DC makes the integrand a function of Z that is collar-local away from 𝒴 ∪ Q → (CE-s):
joint Mayer expansion with polymers built from 𝒴-components, Q-components and CE^+ polymers → CE^+ on the result. The
activity bounds: SF-A2^0's cubic and Jacobian bounds (O(g_0p³) and O(g_0²p²) per term), (s̄ - 1)^{-1} per 𝒴-box, 2^{n/2}e^{-p²/4} per
Q-site, and the walk-decay e^{-m_1d}. With p = p(g_0) → ∞ slowly and g_0p³ → 0 every factor is small; κ'' > 3κ_0 + 3 after M is
fixed as in V7. Not written: (CE-s) itself; the source term of (SF-N); (FP-loc); the polymers touching Q.
[RSF1-fix, session 2: the source term is O(y_bg·g_0p) (Fix SF-A2-1), no worse than the Jacobian term at small curvature. The
cut-good (Q = ∅) part of SF-A3^0 is now Corollary CE-exp^0 (§7.1), CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮), by a different route (site
interpolation, no s-walks); the Q ≠ ∅ part is (CE-Q).]

## 3.4 A4

**Lemma SF-blk: PROVEN-HERE ⇐ CE-geo' (g4'), (g5') (counted).** *Proof.* (1) For a level-k polymer X, X̄ is a level-(k+1)
polymer and **d_{k+1}(X̄) ≤ d_k(X)/L**: a connected union of segments τ meeting every closed level-k cube of X also meets every
closed level-(k+1) cube of X̄ (each contains a cube of X), and its length in level-(k+1) units is (length in level-k units)/L;
X̄ is connected because τ is. (2) Split e^{-κd_k(X)} = e^{-κ_0d_k(X)}e^{-(κ-κ_0)d_k(X)} ≤ e^{-κ_0d_k(X)}e^{-(κ-κ_0)Ld_{k+1}(Y)} for X̄ = Y
(κ ≥ κ_0). Every X with X̄ = Y contains one of the L⁴|Y| level-k cubes of Y, so by (g4') at level k,
Σ_{X: X̄=Y}e^{-κ_0d_k(X)} ≤ L⁴|Y|K_0 ≤ 16L⁴K_0(1 + d_{k+1}(Y)) ≤ 16L⁴K_0e^{d_{k+1}(Y)} ((g5'), 1 + d ≤ e^d). Hence
|Ē(Y)| ≤ 16L⁴K_0E_0e^{-((κ-κ_0)L-1)d_{k+1}(Y)}. (3) For d_{k+1}(Y) ≥ 1 and κ(L - 1) - κ_0L - 1 ≥ 0:
|Ē(Y)|e^{κd(Y)} ≤ 16L⁴K_0E_0e^{-(κ(L-1)-κ_0L-1)d(Y)} ≤ 16L⁴K_0E_0e^{-(κ(L-1)-κ_0L-1)}, ≤ E_0 iff κ ≥ (κ_0L + 1 + log(16L⁴K_0))/(L - 1).
∎ (The pre-stated hypothesis κ ≥ κ_0L/(L - 1) + 1 is stronger than the κ ≥ κ_0 used in (2); harmless.) At L = 3: rate
reproduction (κ - κ_0)L - 1 ≥ κ ⟺ κ ≥ 227.5; contraction for d ≥ 1 ⟺ κ ≥ 302.4 (s1 E); Theorem CE's κ > 457 is above both, so a
CE-admissible rate is reproduced and the large polymers (d ≥ 1) contract under blocking. *What it does not give:* polymers with
d_{k+1}(Y) < 1 (sets of cubes with a common point and short trees) are not contracted; their relevant parts must be extracted
(β = 0 renormalisation, (SF-irr), W1R) — the genuinely A4 part. Also not given: the fluctuation integral between levels (A2-A3),
which is what turns level-k polymers in U_k into level-(k+1) polymers in U_{k+1}.

**A4 remainder (not attacked):** (SF-irr)_{k+1}, (SF-g)_k, (SG^fl)_k, (BG)_k, (RLF-5) width, (SF-last), (I_k^E)' (a3)-(a4): HYPOTHESIS
with owners as in §2.

---

# 4. Outcome: lemma list, statuses, and what (SF^J)_k now rests on (written after §3)
[Session-2 note: §4.1, §4.3 are the session-1 record; their statuses are superseded by §8 (session-2 outcome), which applies
REVIEW_SF_S1's fixes. §4.2's first bullet is rewritten per RSF1-fix SF-J-1.]

## 4.1 Lemma list (this file; all unreviewed)
| item | clause | status | consumes (owner) |
|---|---|---|---|
| Lemma SF-thr | A1 | **PROVEN-HERE** (not counted) | HIST §20.0 (F1) (elementary) |
| Corollary SF-thr-k | A1 | **CONDITIONAL** ⇐ (N5-unif) | (N5-unif) ⇐[ARGUED, REVIEW_S20] (BG-unif) + NAH-ind inputs (PROOF) |
| (BG-unif) precise | A1 | HYPOTHESIS [P] (template REVIEW_S20, adopted with the no-circularity clause) | PROOF B-NA |
| (BG-loc) | A1 | **OPEN, new name** [s to P] | — |
| Lemma SF-J | A2 | **PROVEN-HERE** (counted) | none (Duhamel, functional calculus) |
| Lemma SF-cut | A2 | **PROVEN-HERE** (not counted) | none |
| Lemma SF-T0 | A2 | **PROVEN-HERE** (existence of constants; counted) | NA-alg (a) analyticity as in N5-an's proof; BR1 (ii) (PROOF [S20]) |
| Lemma SF-N0 | A2 | **PROVEN-HERE** (not counted) | none |
| (SF-N) | A2 | OPEN [s] (kernel normalisation: analytic, u-uniform; its linear term is a source) | HIST GAP S2-3 |
| (FP-loc)_k | A2 | OPEN [s to P] (= PROOF's FP_U(V)) | PROOF NA-FP |
| (N5-reg)_k | A2 | **OPEN, new name** [s] | PROOF N5-sf0 |
| Proposition SF-A2^0 | A2, stage 0 | **CONDITIONAL** ⇐ (FP-loc)_0, (SF-N) | N5-sf0, BR1, SF-T0, SF-J, SF-WN, SF-cut |
| Lemma SF-WN | A3 | **PROVEN-HERE** ⇐ N5-sf0 (not counted) | PROOF N5-sf0 |
| Lemma SF-DC | A3 | **PROVEN-HERE** ⇐ Theorem RW (counted) | PROOF Theorem RW, Setting N5-bg (range 1 block) |
| (OP-loc)_k | A3 | **OPEN, new name** [s to P]; its necessity PROVEN-HERE (elementary) | — |
| Lemma SF-geo | A3 | **PROVEN-HERE** ⇐ CE-geo' (not counted) | PROOF CE-geo' |
| Corollary CE^+ | A3 | **PROVEN-HERE** ⇐ Theorem CE [S11] (counted) | PROOF Theorem CE, CE-geo' |
| Lemma SF-s | A3 | PROVEN (standard; not counted) | none |
| Proposition SF-V | A3 | **PROVEN-HERE as a verdict** (not counted) | the above; Theorem CE's statement; RW (iv) |
| (CE-s) | A3 | ARGUED (standard in kind; not written) [s to P] | — |
| Proposition SF-A3^0 | A3, stage 0 | **ARGUED** | SF-A2^0, SF-V, (CE-s) |
| Lemma SF-blk | A4 | **PROVEN-HERE** ⇐ CE-geo' (counted) | PROOF CE-geo' (g4'), (g5') |
| (SF-irr), (SF-g), (SG^fl), (BG), (RLF-5) width, (SF-last), (I_k^E)' (a3)-(a4) | A4 | HYPOTHESIS (not attacked) | PLD, FLOW, RLARGE, HIST |

**Tally of this file:** PROVEN-HERE 11 (counted 5: SF-J, SF-T0, SF-DC, CE^+, SF-blk; not counted 6: SF-thr, SF-cut, SF-N0, SF-WN,
SF-geo, SF-V) + 1 standard (SF-s); CONDITIONAL 2 (SF-thr-k, SF-A2^0); ARGUED 2 ((CE-s), SF-A3^0); OPEN/HYPOTHESIS: new names
(BG-loc), (N5-reg)_k, (OP-loc)_k; carried (BG-unif), (SF-N), (FP-loc), and the A4 hypotheses. No item of RLARGE §4.2 is
discharged; row 3 is split and partly reduced.

## 4.2 Corrections made while proving (all marked [post-proof] in §2-§3)
- SF-J (2) [RSF1-fix SF-J-1, rewritten in session 2]: the chart D_N = {||A||_op < π} covers only a proper subset of SU(N) for
  N ≥ 3 (explicit SU(3) counterexample; measured Haar fractions 0.975 (SU(3)), 0.948 (SU(4))); the spread chart D'_N covers a
  Haar-full set for every N (Lemma SF-J', §7.3); SF uses D_N because its bounds live there. SF-A2^0's chart identity is stated on
  the small-fluctuation support, which is where its bounds hold; the complement is a fluctuation large field either way.
- SF-A2^0: a missing factor √N in A = g_0√N𝒞Z; and the kernel normalisation carries a NON-vanishing linear term (a source),
  since U(V) is critical for F, not for F + Σlog n_c. [RSF2-fix, stale text: its size is O(y_bg)·|A| and it is zero at flat
  backgrounds (Lemma SF-src, §7.3).]
- SF-thr-k: re-based on (N5-unif); the step (BG-unif) ⇒ (N5-unif) is REVIEW_S20's unproven sentence (ARGUED).

## 4.3 What (SF^J)_k now rests on (stage-0 → general k)
**At stage 0** the A1 background is PROVEN (BR1/NAH1, PROOF [S20]); A2 is reduced to **(FP-loc)_0 + (SF-N)** (everything else in
the Gaussian/remainder split is proven: SF-J, SF-T0, SF-cut, SF-WN with N5-sf0); A3 is reduced to **(CE-s)** (the hypotheses
of Theorem CE are re-verified item by item in SF-V: product/ultralocal in white-noise variables ✓, collar locality ✓ via SF-DC +
CE^+, sup bound ✓ only after the per-site cut, complex activities ✓); A4's large-polymer half is proven (SF-blk), its
small-polymer half is (SF-irr)/(W1-ret'^J).
**At stage k ≥ 1** add: **(BG-unif)** (or (N5-unif)) for level-uniform thresholds (Corollary SF-thr-k); **(BG-loc)** and
**(N5-reg)_k** (region forms: the history has a large-field exterior); **(OP-loc)_k** (the stage-k operator is not finite range, so
SF-DC's input fails — a new necessary item found here) [RSF2-fix, stale text: necessary on the RW route only; its operator half
is retired by CE-exp, its activity half is (L-loc)_k (§8.1)]; **(I_k^E)' (a3)-(a4)** for the main term's locality (SF-T0's analogue at
level k needs a local main term); (FP-loc)_k, (SF-N) at coupling u_k.
**Constants (SF-V (V7)):** with N5-sf0's proven rates the CE scale is M ≳ 2.6·10¹⁵ fine spacings and the per-cube activity must be
below e^{-O(10⁵)}: g-independent, so an existence statement for g_0 small is not obstructed, but every constant is extreme;
sharper N5 rates (c37-type work) would move them. **[RSF3-fix stale-M (REVIEW_SF_S3 Part A 11(a)):** "g-independent" was false for
session 3's Theorem CE-Q, whose (M-Q) μM ≥ 2(j_max + 1)log 2 made M grow like log(1/g_0). Session 4's Theorem CE-Q-col (§13.1)
drops (M-Q) (shell-dependent halos, Fix Q4), so M is g-independent again under (M-W3) alone; the sentence holds for CE-Q-col,
not for the session-3 form.]

## 4.4 Hypotheses consumed, by item, with owner
SF-thr: none. SF-thr-k: (N5-unif) [PROOF/REVIEW_S20]. SF-J, SF-cut, SF-N0, SF-s: none. SF-T0: NA-alg (a) + N5-an's analyticity
argument [PROOF S14/S19], BR1 (ii) [PROOF S20]. SF-WN: N5-sf0 [PROOF S19]. SF-DC: Theorem RW, Setting N5-bg's range [PROOF S19].
SF-geo, SF-blk: CE-geo' [PROOF S11]. CE^+: Theorem CE [PROOF S10/S11]. SF-A2^0: + (FP-loc)_0 [PROOF FP_U], (SF-N) [HIST S2-3].
SF-A3^0: + (CE-s) [this file]. No imported (literature) item is load-bearing for any PROVEN-HERE claim; Balaban/Dimock II-III
are named for (CE-s) only as the standard form [not read this session].

---

# 5. Check s1 (criteria checks/s1_criteria.md, final mtime 01:49:54 UTC, before the script; script checks/s1_sf.py; output
checks/s1_out.txt; record checks/s1_time.txt; first run kept as s1_out_firstrun.txt / s1_time_firstrun.txt)
- **Run 1** (01:56:18-01:56:29 UTC, numeric lock, load 2.9, 36% free, nice 10, BLAS threads 1, 11 s, peak RSS 285 MB): the
  reporting was DEFECTIVE: `rec` tested `ok is True` on numpy booleans, so most passing criteria printed "FAIL" while the
  OVERALL line (testing `is False`) printed "PASS". Neither label is usable; the printed numbers are correct.
- **Post-run fix 1 (disclosed, 01:57 UTC):** `ok = bool(ok)` in `rec`; no criterion, threshold or computation changed.
- **Run 2** (02:50:08-02:50:19 UTC, lock, load 2.3, 43% free, 11 s, 302 MB): every number identical to run 1.
  **OVERALL: FAIL as pre-registered (E4).** A0-A6, B1-B5, C1, D1-D2, E1-E3 PASS.
  - A (SF-DC): off-Ω and off-Ω(𝒴^+) entries exactly 0.0 at t = 0, 1, 10; reach beyond Ω_□ up to 6.3·10⁻⁴ (non-vacuous); the
    quadrature square root matches K^{-1/2} to 8.8·10⁻¹⁵; 𝒞(s) outside the predicted D(x) exactly 0.0; one long-range entry
    (1e-3) makes a 𝒴-column reach outside Ω(𝒴^+) (9.1·10⁻⁶): the (OP-loc) failure mode is real.
  - B (SF-J): product formula to 3.4·10⁻¹⁵ (N = 2, 3, 4, complex A); bound ratios 0.76 (N/9 bound), 0.39 (C_J = N/270), 0.82
    (scalar (2/9)); Haar SU(2) KS 0.0014.
  - C1: tail ratio ≤ 0.16. D1-D2 PASS. E1-E3 reproduce 1.2777·10⁵, 227.47 / 302.33, 2.646·10¹⁵, 1.53·10¹³, 4.93·10⁶¹.
  - **E4 FAIL:** max 2arcsin(x/2)/x on (0, ½] = 1.010721 > 1.0107. The constant 1.0107 (copied from HIST §20.0 (F1)) is low in the
    5th digit. SF-thr's proof was corrected to 1.0108 (02:08 UTC); every bound actually used (1.011) is unaffected. HIST (F1)
    carries the same 5th-digit slip (read-only here; flagged for its owner; its uses are 1.011 as well).

---

# SESSION 2 (2026-10-28 UTC). Inputs read before 03:45 UTC: REVIEW_SF_S1.md (BINDING; in full), SF.md, SF_LOG.md,
REVIEW_HIST_S4.md (S4-1, S4-2, binding fixes, strategic verdict; the coordinator's correction routes STEP 3 through it),
HIST.md 468e9f03… (§25.4 NORM-an, §25.5 (a5-G)/(a5-U)/(a3-q)/(R♯_∞)/Theorem A5, §25.6, l.1768-1778, l.1185), PROOF.md 490aaf34…
(Theorem CE l.1831-1915; Lemma CT♯, Theorem RW, Corollary RW-triv, Theorem N5-sf0 l.5296-5406; B-NA-red, (G♯), (R♯), BNA-F1-F3
l.3140-3199; [S15] l.126-153, (R♯_ω) l.3477-3491; [S21] NAH-unif and N5 status l.6036-6099), RTARGET.md §33-§35 (l.572-633),
RLARGE.md l.49-80, l.681; PLD.md l.1110-1120. md5 at 03:45: SF.md (before this block) 88402e0b…, REVIEW_SF_S1 319d65c3…, REVIEW_HIST_S4 bc0a9da0…, PLD 4db9b142…, RLARGE 24a73553…, RTARGET e9af331a….

## 6. Pre-stated targets, session 2 (appended to this file at 03:45:30 UTC, 2026-10-28, BEFORE any session-2 proof and before the s2 criteria)

### 6.1 STEP 2: one cluster-expansion lemma for exponentially local operators and activities
*Idea fixed before writing (exploratory, unwritten):* after the per-site cut (SF-cut) the white noise has a product measure with
bounded support; on such a measure the Z-dependence of an activity can be localised by interpolating EACH SITE's variable
(s_y Z_y, s_y ∈ [0, 1]) and Taylor-expanding to first order in each far site, with Cauchy gains from analyticity in s_y on a disc
whose radius grows exponentially with the distance. This needs only an exponential ℓ¹ bound on the field map (N_μ(|𝒞|) < ∞) and
analyticity of the activity on a weighted polydisc. It does not use the RW s-interpolation or finite range.

**Setting CE-exp.** Setting CE (PROOF l.1832) with CE cubes of fine side M ≥ 1 (unit cubes after scaling; [S11] constants κ_0 =
16 log 12800, K_0, c_0(·), C_1). Λ := the fine sites (M⁴ per CE cube), q(y) the CE cube of the site y. Each site carries
Z_y ∈ R^n. ν = Π_yν_y is a product probability measure with supp ν_y ⊂ {|Z_y| ≤ p}. X^+ as in §0. δ(y, X) := the fine ℓ^∞
torus distance from y to the set of sites of ∪X; n(y, X) := the ℓ^∞ cube-index torus distance from q(y) to X^+. For s ∈ C^Λ,
(s·Z)_y := s_yZ_y; 1_S·Z := Z on S, 0 off S. For a polymer X:
  𝔻_X(μ) := {s ∈ C^Λ : s_y = 1 for every site y of ∪X^+, |s_y| < 1 + e^{μδ(y,X)} otherwise}.
**Hypothesis (H-exp)(κ, h_0, μ).** For every polymer X there is a function Φ_X on complex fields such that, for every Z ∈ supp ν,
s ↦ Φ_X(s·Z) is defined and holomorphic on 𝔻_X(μ), with |Φ_X(s·Z)| ≤ h_0e^{-κd(X)} there, and Z ↦ Φ_X(s·Z) is measurable.
Put F_X(Z) := Φ_X(Z) (s ≡ 1).

- **Lemma LOC-s (site-interpolation localisation).** Under (H-exp), for every polymer X and Z ∈ supp ν,
    F_X(Z) = Σ_{S⊂Λ∖∪X^+}F_{X,S}(Z),  F_{X,S}(Z) := Σ_{T⊂S}(-1)^{|S∖T|}Φ_X(1_{∪X^+∪T}·Z),
  F_{X,S} depends on Z only through Z on (∪X^+) ∪ S, and |F_{X,S}(Z)| ≤ h_0e^{-κd(X)}Π_{y∈S}e^{-μδ(y,X)} with δ(y, X) > M·n(y, X)
  and n(y, X) ≥ 1 for y ∉ ∪X^+. *Planned: PROVEN-HERE (counted).*
- **Lemma HULL.** For a polymer X and a finite S ⊂ Λ∖∪X^+ there is a polymer Y(X, S) (a fixed rule) with X^+ ⊂ Y(X, S),
  q(y) ∈ Y(X, S) for y ∈ S, and **d(Y(X, S)) ≤ 273d(X) + 272 + Σ_{y∈S}(2n(y, X) + 1)**. *Planned: PROVEN-HERE (not counted).*
- **Theorem CE-exp (= the (CE-s)^exp of REVIEW_SF_S1 Part E, in site-interpolation form).** Let κ_c > 3κ_0 + 3, κ' := κ_c + 16 log 2,
    W := M⁴e^{κ'}Σ_{n≥1}(2n + 1)⁴e^{-(μM - 2κ')n}  (finite iff μM > 2κ').
  Under (H-exp)(κ, h_0, μ) with κ ≥ 273κ' + 1296W and **H'_0 := 2^{16}e^{272κ' + 1296W}h_0 ≤ c_0(κ_c)**:
    ∫exp(Σ_XF_X)dν = exp(Σ_YF#(Y)),  F#(Y) = 0 unless Y is a polymer,  |F#(Y)| ≤ C_1H'_0e^{-(κ_c - 3κ_0 - 3)d(Y)},
  and F#(Y) depends only on the pieces F_{X,S} with Y(X, S) ⊂ Y. **Sufficient explicit condition:** μM ≥ 3κ' + 4 log M + 8
  implies W ≤ w_8 := Σ_{n≥1}(2n + 1)⁴e^{-8n} (≈ 0.0272). *Planned: PROVEN-HERE ⇐ Theorem CE [S11], SF-geo, CE-geo' (counted).*
- **Corollary CE-exp-𝒞 (fields that are exponentially local images of the white noise).** Let 𝒞 be a linear map with block
  kernel (A_b = Σ_y𝒞(b, y)Z_y), x(b) the base site of b, d a distance with d(b, y) ≥ ℓ^∞(x(b), y), and
  N_μ(|𝒞|) := sup_bΣ_y|𝒞(b, y)|e^{μd(b,y)} < ∞. If for every polymer X the function H_X is holomorphic on the weighted polydisc
  𝒫_X(ρ, μ) := {A : |A_b| < ρe^{μδ(x(b),X)} for every b} with |H_X| ≤ h_0e^{-κd(X)} there, and 2pN_μ(|𝒞|) ≤ ρ, then
  Φ_X(Z) := H_X(𝒞Z) satisfies (H-exp)(κ, h_0, μ). (Strictly local H_X, depending on A_b for x(b) ∈ ∪X only, need the bound on
  {max_{x(b)∈∪X}|A_b| < ρ} only.) *Planned: PROVEN-HERE (not counted).*
- **Corollary CE-exp^0 (stage 0, the cut-good term).** In Proposition SF-A2^0's setting with 𝒞 = 𝒞(U(V), V) of N5-sf0 (b),
  μ := m_1, d the distance of N5-sf0 (~~provided it dominates the fine ℓ^∞ distance~~ [RSF2-fix CE0-1: it does; d is the ℓ¹
  torus distance of positions, PROOF Setting N5-0 l.5155, and ℓ¹ ≥ ℓ^∞]), M chosen by the sufficient condition of
  Theorem CE-exp, and activities H_X := the sum of the terms u_0V_τ, log j(A_b), and 𝔫_c(e^AU(V)) - 𝔫_c(U(V)) whose variables lie in
  the cubes of X (each term assigned to the polymer of the cubes containing its pattern; a pattern of fine diameter < M gives
  d(X) = 0, |X| ≤ 16): the ν_∅ term of SF-cut, ∫exp(Σ_XH_X(g_0√N𝒞Z))dν_∅, has Theorem CE-exp's form for g_0 ≤ g_CE (explicit
  in terms of S_T, r_T, N_{m_1}(|𝒞|), p, M, the 𝔫_c constants and c_0(κ_c)). *Planned: CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮), where
  (SF-N♮) is the remaining domain-match clause of (SF-N) (stated in §6.3).*
- **Corollary CE-exp^k (k ≥ 1; replaces (OP-loc)_k).** The same at stage k with 𝒞 = 𝒞_k (the level-k fluctuation operator's square
  root) and the level-k activities, under: (i) N_μ(|𝒞_k|) < ∞ uniformly (N5-sf_k's ℓ¹ conclusion; level-uniform ⇐ (N5-unif));
  (ii) **(L-hol)_k**: the level-k activities (the Taylor remainders of the main-term densities 𝓔^{an}_{k,x}, the Jacobian, the
  kernel normalisation) are holomorphic and bounded on weighted polydiscs 𝒫_X(ρ_k, μ_k); (iii) (FP-loc)_k, (N5-reg)_k.
  *Planned: CONDITIONAL ⇐ (i)-(iii).* (OP-loc)_k is then retired: no finite-range or localisation input on the operator is used.
  [RSF2-fix CEk-1/2: only the operator half is retired; (ii) is replaced by (L-loc)_k; the inherited activities and (CE-col) are
  added; see the corrected statement at the end of CE-exp^k's proof, §7.1.]
- **(CE-Q) [named, OPEN].** The cut-complement terms Q ≠ ∅ of SF-cut: the Q-sites carry unbounded Z. Failure expected in Theorem
  CE-exp's form: the field reached on X from a large Z_y at a near site leaves the analyticity domain, so a large-fluctuation
  region around Q must be excised (RLARGE §3.2 branch (ii), (SG^fl)), not expanded.

### 6.2 STEP 3: (a5-G) restated in the §33 pair; (a5-U) and (a3-q) on R_{3ε_1}
[Coordinator correction, received during session 2, applied before any STEP-3 writing: per REVIEW_HIST_S4 S4-1 the sup-norm
(a5-G) is FALSE at the trivial chain (||𝓛⁻¹||_{ℓ^∞→ℓ^∞} ≳ L^{2(k-1)}, BNA-F2); it is not attempted.]
- **(a5-G♯) [restated; OPEN; = B-NA's (G♯) at non-trivial chains].** There are G, G_D, G_w, G_{D,w} < ∞, m_G > 0, θ ∈ (0, 1],
  depth-uniform, such that at every real critical chain ψ^r of E^♭(·; U), U ∈ R_{3ε_1}(Λ_k), in a per-level covariant slice through
  ψ^r with Feynman terms on the residual groups, the slice Hessian 𝓛 and data map N obey (G♯) in RTARGET §33's pair: X = X_c
  (Hölder version), Y = the divergence-form source norm with ω_0 = 1, ω_l = L^{θ(k-l)}, D = the level-k sup norm ||·||_{D,m},
  weights e^{±md(·,·)} (0 ≤ m ≤ m_G) in the coarse-position distance of §33 (level-k ancestor distance), and (FP♯') on the
  X_c-ball of radius ρ_0. [RSF2-fix G♯-1/G♯-2: d is §33's "ℓ¹ torus distance between coarse positions L^{l-k}·(base point)"
  (RTARGET §33), not "level-k ancestor distance" (they agree to O(1)); the ± weight pair e^{∓md} is B-NA-red's (PROOF B-NA-red),
  §33 defines only w = e^{+md}.]
- **(R♯) at ψ^r [OPEN; PROOF/N2 owner]:** (R♯_ω) of PROOF l.3479 with the trivial chain replaced by ψ^r.
- **(a5-U) [restated on R_{3ε_1}; OPEN].** For real U ∈ R_{3ε_1}(Λ_k), the minimiser of E^♭(·; U) over the chain variables read by
  𝒞^♭-terms is unique modulo chain gauges trivial at the level-k sites (REVIEW_HIST_S4 M-1, M-2).
- **(a3-q) [restated on R_{3ε_1}; OPEN; lane D].** HIST l.1669 with δ ≤ δ_3 and real U ∈ R_δ(Λ_k), used at δ = 3ε_1.
- **Lemma BS (base set).** If U ∈ R_{2ε_1}(Λ_k) is real, Z real with ||Z_b|| ≤ s for all b, s ≤ min{ε_1/5, 0.01}, then Ue^Z ∈
  R_{3ε_1}(Λ_k). *Planned: PROVEN-HERE (elementary; not counted).* Consequence: with ε_1 ≤ δ_a/3 and s_5 ≤ ε_1/5, Theorem A5's
  openness step stays inside the domain of (a5-U), (a3-q).
- **Lemma G-pert (the B-NA pair is stable under X_c-small backgrounds).** Assume (G♯) at the trivial chain in the §33 pair
  (constants G, G_D and weighted G_w, G_{D,w}; this is (G♯_0-field)) and (R♯_ω) at the trivial chain with the Lipschitz form
  ||D_x𝔑(x; B)||_{X→Y} ≤ C_R(2||x||_X + ||B||_D), ||D_B𝔑(x; B)||_{D→Y} ≤ C_R(||x||_X + ||B||_D) (also weighted, C_{R,w}) on
  ||x||_X + ||B||_D ≤ ρ_0. Then at every chain x^r of the trivial slice with data B^r and t := ||x^r||_X + ||B^r||_D ≤
  min{ρ_0, 1/(4GC_R), 1/(4G_wC_{R,w})}, the Hessian 𝓛(x^r) := 𝓛 + D_x𝔑(x^r; B^r) and N(x^r) := N + D_B𝔑(x^r; B^r) obey (G♯) with
  constants 2G, 2(G_D + Gt C_R)… (exact forms in the proof), weighted likewise. *Planned: PROVEN-HERE (implication; not counted).*
- **(G♯-patch) [named, OPEN].** For U ∈ R_{3ε_1}(Λ_k) on large Λ_k no global gauge makes the data ||B_k||_D small (curvature is
  small, holonomies accumulate; BNA-F4). (a5-G♯) at such ψ^r needs a patching of the local (G♯)'s (each patch gauge-equivalent
  to an X_c-small chain by MSG-type gauges) into a global inverse in the §33 pair: the Schauder-norm analogue of N5-sf0's proof
  (local gauges g_□ on Ω^+_□, CT♯, Theorem RW).
  **[RSF2-fix GPa-1: precise statement.]** **(G♯-patch):** there are G', G'_D, G'_w, G'_{D,w} < ∞ and m'_G > 0, independent of k, K, T,
  depending only on the trivial-chain constants of (G♯_0-field), (R♯_ω) and on (C_R, ρ_0), such that for every real
  U ∈ R_{3ε_1}(Λ_k) and every ε_R-regular real critical chain ψ^r of E^♭(·; U), the slice Hessian 𝓛(ψ^r) and data map N(ψ^r) in the
  per-level covariant slice through ψ^r (Feynman terms on the residual groups) obey (G♯) in RTARGET §33's pair (X = X_c Hölder,
  Y = divergence-form with ω, D = ||·||_{D,m}) with these constants, unweighted and with weights e^{±m d}, 0 ≤ m ≤ m'_G.
  *What it is:* (a5-G♯) minus B-NA-red's small-gauge class, i.e. the non-abelian local-gauge patching in Schauder norms. This is
  the B-NA wall itself (REVIEW_HIST_S4 strategic 3), not a new sub-item of it.
- **(MIN-reg) [named, OPEN].** Every minimiser of E^♭(·; U), U ∈ R_{3ε_1}(Λ_k), is, after a chain gauge trivial at level k, in the
  per-level slice through any other minimiser and within X_c-distance r_U (below) of it. (Linear case: the minimiser is unique and
  N2-exp bounds its coarse-unit curvature by the data [inference].) [RSF2-fix, (MIN-reg) re-homed: it is the global half of
  (a5-U) renamed (U-red = a-priori closeness + local uniqueness). Owner: **lane D** (with (a5-U), (a3-q)); lane F does not attack
  it. The "(Linear case …)" sentence belongs to lane D's (a3-q) linear-case target. Note in SF_LOG session 3; HIST not edited.]
- **Proposition U-red.** (a5-U) on R_{3ε_1} ⇐ (a5-G♯) + (R♯) at one minimiser ψ^r + (MIN-reg) with r_U := min{ρ_0, 1/(4GC)}
  (C the (R♯) constant at ψ^r). *Planned: PROVEN-HERE (implication; not counted).*
- **What the restated A5 then rests on (planned reading):** (a5-G♯) + (R♯) are B-NA's wall at non-trivial chains; ~~by G-pert they
  reduce to the trivial-chain items (G♯_0-field), (R♯_ω), (FP♯') plus (G♯-patch) and (MIN-reg). A5 adds no wall beyond B-NA's
  (REVIEW_HIST_S4 strategic verdict 3) except (MIN-reg) and (G♯-patch), which are named here.~~ [RSF2-fix GP-1/GP-2: reading
  withdrawn. Correct reading: (a5-G♯) on B-NA-red's class (chains X_c-small in one global gauge, ||B_k||_D ≤ ε_0), stated in the
  TRIVIAL slice at x^r, ⇐ (G♯_0-field) + (R♯_ω) + (FP♯') (Lemma G-pert, which is NA-IFT's Neumann step and adds no case beyond
  B-NA-red). For every U ∈ R_{3ε_1}(Λ_k) without a globally small gauge (BNA-F4), (a5-G♯) IS (G♯-patch), and that is the whole
  difficulty. (MIN-reg) is lane D's.]

### 6.3 STEP 1 targets (the binding fixes) — applied in place in §2-§5, each tagged [RSF1-fix]; the new items:
- **Lemma SF-J' (the spread chart covers full Haar measure for every N).** D'_N := {A ∈ su(N) : max_{a,b}|θ_a - θ_b| < 2π} (θ the
  eigen-angles of A/i). Every U ∈ SU(N) with N distinct eigenvalues has exactly one logarithm in D'_N; exp restricted to the
  preimage of that (Haar-full) set is a diffeomorphism; j > 0 and log j holomorphic on D'_N; hence ∫f dU = c_N∫_{D'_N}f(e^AU_0)j(A)dA
  for every f ∈ L¹ and every N. *Planned: PROVEN-HERE (not counted).*
- **Lemma SF-src (size of the kernel-normalisation source).** Under (SF-N♮) below, |𝔫_c(e^AU) - 𝔫_c(U)| ≤ 8K_𝔫c_yy_bgρ + 9K_𝔫c_y²ρ²
  for max_b|A_b| ≤ ρ, K_𝔫 := 36.8C_N(2 + 2c_N) (NORM-an's constants), y_bg the background contour spread of c. *Planned: PROVEN-HERE
  ⇐ NORM-an + (SF-N♮) (not counted).*
- **(SF-N♮) [OPEN; s; what remains of (SF-N)].** There are r_𝔫 > 0, c_y < ∞ (g-independent) such that for every background in
  the class used and every coarse link c: the complexified fields e^AU with max_{b in c's contours}|A_b| ≤ r_𝔫 lie in NORM-an's
  D_c(y_0), and their contour spread obeys y(e^AU) ≤ y_bg + c_y max|A_b|, with y_bg/c_y ≤ r_𝔫.

---

## 7. Session-2 proofs (written from 03:53 UTC, after §6 and after the s2 criteria; s2 ran 03:52:08-03:52:17 UTC)

### 7.1 STEP 2: Theorem CE-exp and its corollaries

**Lemma LOC-s: PROVEN-HERE (counted).** *Proof.* Fix X and Z ∈ supp ν; let F := Λ∖∪X^+ (finite) and g(s_F) := Φ_X(s·Z) with s_y = 1
on ∪X^+; g is holomorphic on 𝔻 := Π_{y∈F}{|s_y| < 1 + e^{μδ(y,X)}} ⊃ [0, 1]^F. For T ⊂ F write g(1_T) for g at the indicator of T;
g(1_T) = Φ_X(1_{∪X^+∪T}·Z). (1) *Identity.* Σ_{S⊂F}Σ_{T⊂S}(-1)^{|S∖T|}g(1_T) = Σ_{T⊂F}g(1_T)Σ_{S: T⊂S⊂F}(-1)^{|S∖T|} = g(1_F) = F_X(Z)
(the inner sum is 1 if T = F and 0 otherwise). (2) *Locality.* Every g(1_T) with T ⊂ S reads Z only on ∪X^+ ∪ T ⊂ ∪X^+ ∪ S.
(3) *Bound.* Iterating h(1) - h(0) = ∫_0^1h'(σ)dσ in each variable of S (variables of F∖S held at 0) gives
F_{X,S} = ∫_{[0,1]^S}(∂^Sg)(σ_S, 0_{F∖S})dσ_S. At s⁰ = (σ_S, 0), the closed polydisc Π_{y∈S}{|s_y - σ_y| ≤ r_y}, r_y < e^{μδ(y,X)}, lies in 𝔻
(|σ_y| + r_y < 1 + e^{μδ}); Cauchy's formula for the mixed first derivative in |S| variables gives |∂^Sg(s⁰)| ≤ sup_𝔻|g|·Π_yr_y^{-1};
let r_y ↑ e^{μδ(y,X)}. (4) *Distance.* y ∉ ∪X^+ means q(y) ∉ X^+, so n := n(y, X) ≥ 1. If a cube Q of X had ℓ^∞ cube-index distance
j ≤ n from q(y): j = 1 puts q(y) in X^+; for j ≥ 2, stepping once from Q towards q(y) in every differing coordinate gives a cube of
X^+ at distance j - 1 < n, contradicting the definition of n. So every cube of X is at index distance ≥ n + 1 from q(y); two sites
whose cubes are at index distance j in some coordinate differ there by ≥ (j - 1)M + 1 fine spacings (also on the torus), so
δ(y, X) ≥ nM + 1 > nM. ∎

**Lemma HULL: PROVEN-HERE (not counted).** *Proof.* Let τ be a connected union of segments in ∪X^+ meeting every closed cube of X^+,
of length ≤ d(X^+) + η (η > 0 arbitrary); d(X^+) ≤ 273d(X) + 272 (Lemma SF-geo). For y ∈ S let Q'_y be the lexicographically first
cube of X^+ at index distance n_y := n(y, X) from q(y), and work in the lift in which the index displacement Δ ∈ Z⁴ from q(y) to Q'_y
has |Δ|_∞ = n_y. Let σ_y be the segment from the centre of q(y) to the centre of Q'_y (Euclidean length |Δ|_2 ≤ 2|Δ|_∞ = 2n_y, d = 4),
and γ_y ⊂ Q'_y a segment from the centre of Q'_y to a point of τ ∩ Q'_y (length ≤ the half-diagonal, 1). Put Y(X, S) := X^+ ∪ {cubes
whose closed cube meets some σ_y}. Then τ' := τ ∪ ∪_y(σ_y ∪ γ_y) is connected (each σ_y ∪ γ_y is connected and meets τ), lies in
∪Y(X, S) (σ_y lies in the union of the closed cubes it meets; γ_y ⊂ Q'_y), and meets every closed cube of Y(X, S). Hence ∪Y(X, S) is
connected (a union of closed cubes each meeting the connected set τ' contained in the union), q(y) ∈ Y(X, S) (σ_y starts at its
centre), and d(Y(X, S)) ≤ length(τ') ≤ d(X^+) + η + Σ_y(2n_y + 1). Let η → 0. ∎ (s2 B1-B3: the construction on a 7⁴ torus of cubes
with M = 2, 200 random trials: Y *-connected and containing every q(y); added length ≤ Σ(2n_y + 1), equality attained when all four
|Δ_i| = n_y; min(δ - Mn) = 1, as the proof's +1 predicts.)

**Theorem CE-exp: PROVEN-HERE ⇐ Theorem CE [S11 constants], Lemma SF-geo, Lemma CE-geo' (counted).** *Proof.* Step 1 (localise and
regroup). By Lemma LOC-s, Σ_XF_X = Σ_XΣ_SF_{X,S} (finite sums). Put H'(Y) := Σ_{(X,S): Y(X,S)=Y}F_{X,S}. Each piece reads Z only on
∪X^+ ∪ S ⊂ ∪Y(X, S) (q(y) ∈ Y(X, S)), so H'(Y) depends on Z|_Y only, and H'(Y) = 0 unless Y is a polymer (Lemma HULL). Step 2
(bound). Y(X, S) = Y forces X ⊂ X^+ ⊂ Y; dropping every other constraint and using Lemma HULL and Lemma LOC-s (δ > Mn):
  e^{κ'd(Y)}|H'(Y)| ≤ h_0e^{272κ'}Σ_{X⊂Y}e^{-(κ - 273κ')d(X)}Σ_{S⊂Λ∖∪X^+}Π_{y∈S}w_y,  w_y := e^{κ'}e^{-(μM - 2κ')n(y,X)}.
Σ_SΠ_{y∈S}w_y = Π_y(1 + w_y) ≤ exp(Σ_yw_y). The sites with n(y, X) = n lie in cubes at index distance ≤ n from some cube of X^+, at
most |X^+|(2n + 1)⁴ cubes of M⁴ sites, so Σ_yw_y ≤ |X^+|W; |X^+| ≤ 81|X| ≤ 1296(1 + d(X)) (each cube has 3⁴ cubes within index distance 1;
CE-geo' |X| ≤ 16(1 + d(X))). With κ ≥ 273κ' + 1296W every exponent -(κ - 273κ' - 1296W)d(X) is ≤ 0, and there are ≤ 2^{|Y|} ≤
2^{16}e^{16 log 2·d(Y)} sets X ⊂ Y (CE-geo'). So |H'(Y)| ≤ 2^{16}e^{272κ'+1296W}h_0·e^{-(κ' - 16 log 2)d(Y)} = H'_0e^{-κ_cd(Y)} on supp ν.
Step 3. Setting CE holds for (ν, H'): fields on sites, ν a product probability measure, H'(Y) complex, measurable, reading Z on Y
only, bounded on supp ν. Theorem CE ([S11] form: κ_c > 3κ_0 + 3, H'_0 ≤ c_0(κ_c)) gives the conclusion, with F#(Y) depending only on
{H'(Y') : Y' ⊂ Y}, i.e. on the pieces with Y(X, S) ⊂ Y. *Sufficient condition.* If μM - 2κ' ≥ κ' + 4 log M + 8 then for n ≥ 1,
M⁴e^{κ'}e^{-(μM-2κ')n} ≤ e^{-8n}e^{-(κ' + 4 log M)(n-1)} ≤ e^{-8n}, so W ≤ w_8. ∎
*Numbers (s2 C, κ_c := 3κ_0 + 4):* κ_0 = 151.3152, κ_c = 457.9456, κ' = 469.0360, w_8 = 0.02724, so the polymer-decay requirement on the
input activities is κ ≥ 273κ' + 1296w_8 = 1.2808·10⁵ (met by every activity supported on d(X) = 0 polymers, for which κ is free).
With μ = m_1 = 4.83·10⁻¹¹ the sufficient condition holds from **M_min = 3.187·10¹³ fine spacings** (μM_min = 1539.5; directly summed
W(M_min) = 0.02717 ≤ w_8). This replaces SF-V (V7)'s M ≳ 2.6·10¹⁵ (which came from the walk activities of the (CE-s) route) by a
value 83 times smaller. The smallness condition H'_0 ≤ c_0(κ_c) still carries the factor e^{272κ'} ≈ e^{1.28·10⁵} from SF-geo's
crude d(X^+) ≤ 273d(X) + 272: g-independent, extreme, and an existence statement [RSF2-fix CEk-2: and, with the rate loss 1/273,
it BLOCKS ITERATION across levels; Corollary CE-exp-col (§10.3) removes the e^{272κ'} factor and the rate factor]. *Remark (what this route does not use):* no
finite range of the operator, no random-walk s-interpolation (SF-DC, SF-s, Theorem RW (iv)), no symmetric decoupling; only the
bounded support of the cut white noise, analyticity in the per-site scalings, and an exponential ℓ¹ bound of the field map.
(s2 A1-A4, d = 1 toy with a kernel that has no zero entry: Σ_SF_S = Φ exactly (0.0), F_S unchanged under re-drawing Z off
B ∪ S (0.0), |F_S| ≤ h·Πe^{-μδ} with max ratio 0.076, non-vacuous (1.8·10⁻² for S ≠ ∅, 3.0·10⁻³ at |S| ≥ 3).)
[RSF2-fix, check design: five s2 criteria are TAUTOLOGIES of the construction and carry no evidence: **A1** (Möbius inversion is
an identity), **A2** (the pieces do not read off-set Z by construction), **B2** (|Δ|_2 ≤ 2|Δ|_∞ in d = 4), **D3's window count**
(K + j + Nm = 0 has exactly one solution j ∈ {0, …, N - 1} for every integer K, blind to the eigenvalue structure), **E2**
(arithmetic). s2's 14/14 is 9 informative passes (A3-A4, B1, B3, C1-C2, D1-D2, D3's reconstruction, E1). The s3 criteria
include an edge test of the Cauchy bound (s3 A).]

**Corollary CE-exp-𝒞: PROVEN-HERE (not counted).** *Proof.* For Z ∈ supp ν and s ∈ 𝔻_X(μ), A := 𝒞(s·Z) has
|A_b| ≤ Σ_y|𝒞(b, y)||s_y||Z_y| with |s_y| < 1 + e^{μδ(y,X)} ≤ 2e^{μδ(y,X)} (and |s_y| = 1 on ∪X^+), |Z_y| ≤ p, and
δ(y, X) ≤ ℓ^∞(y, x(b)) + δ(x(b), X) ≤ d(b, y) + δ(x(b), X). So |A_b| ≤ 2pe^{μδ(x(b),X)}Σ_y|𝒞(b, y)|e^{μd(b,y)} ≤ 2pN_μ(|𝒞|)e^{μδ(x(b),X)},
strictly below ρe^{μδ(x(b),X)} unless A_b = 0 (then trivially). A is linear in s, so Φ_X(s·Z) = H_X(𝒞(s·Z)) is holomorphic on 𝔻_X(μ)
and bounded by h_0e^{-κd(X)}. For strictly local H_X only b with x(b) ∈ ∪X enter, where δ(x(b), X) = 0. ∎

**Corollary CE-exp^0: CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮) (not counted).** *Statement as proven.* In Proposition SF-A2^0's setting
(real BR1 background (U(V), V) ∈ 𝔑(α_*), gauge logs ≤ r_T/4 on every term pattern), let 𝒞 := 𝒞(U(V), V), μ := m_1 ~~, and assume the
distance d of N5-sf0 dominates the fine ℓ^∞ distance between base sites [not checked in PROOF's text in this session]~~
[RSF2-fix CE0-1: caveat deleted; d is the ℓ¹ torus distance of positions (PROOF l.5155) ≥ ℓ^∞, and N5-sf0 (b)'s ℓ¹ bound holds for
every m'' ≤ m_1]. Take M ≥
max{M_min(μ), 2L + 1} (M_min as above), so every term pattern (fine diameter ≤ 2L) lies in cubes whose indices take two consecutive
values per coordinate: its polymer X(τ) has d(X(τ)) = 0, |X(τ)| ≤ 16. Put ρ' := 2g_0√NpN_{m_1}(|𝒞|) and require
**ρ' ≤ min{r_T/8, r_𝔫/2}**. Let H_X := Σ_{X(τ)=X}[u_0V_τ + log j(A_b) + (𝔫_c(e^AU(V)) - 𝔫_c(U(V)))] (A = g_0√N𝒞Z; the three term types
of SF-A2^0 with the source of SF-src), n_* the maximal number of terms of all types whose first pattern site is a given site.
Then (H-exp)(κ, h_0, m_1) holds for every κ with
  **h_0 := 16M⁴n_*·max{128S_T(2√NpN_{m_1}(|𝒞|))³g_0/r_T³, (N/9)ρ'², 8K_𝔫c_yy_bgρ' + 9K_𝔫c_y²ρ'²}**,
and for g_0 so small that 2^{16}e^{272κ'+1296w_8}h_0 ≤ c_0(κ_c), the cut-good term ∫exp(Σ_XH_X(g_0√N𝒞Z))dν_∅ equals
exp(Σ_YF#(Y)) with |F#(Y)| ≤ C_1H'_0e^{-(κ_c-3κ_0-3)d(Y)}. *Proof.* Corollary CE-exp-𝒞 with the kernel g_0√N𝒞 (strictly local
H_X): on the polydisc reached, max_b|A_b| < ρ'. On it: SF-T0 (4) (complex A allowed) bounds |u_0V_τ| ≤ 2S_T(4ρ'/r_T)³/g_0²; SF-J (5)
bounds |log j(A_b)| ≤ (N/9)ρ'² (||A_b||_op ≤ |A_b| ≤ r_T/8 ≤ π/2); Lemma SF-src bounds the source. The count: a term with X(τ) = X has
its first pattern site in one of the ≤ 16 cubes of X, ≤ 16M⁴n_* terms. H_X = 0 unless d(X) = 0, so |H_X| ≤ h_0e^{-κd(X)} for every κ;
take κ := 273κ' + 1296w_8. Theorem CE-exp. Every entry of h_0 is O(g_0) at fixed (p, M) (ρ' ∝ g_0; y_bg ≤ ε fixed), so g_CE > 0. ∎
*Conditional part:* (FP-loc)_0 is what makes the stage-0 integrand exactly "white-noise Gaussian × exp(Σ_XH_X) × c-numbers" on the
slice (SF-A2^0); (SF-N♮) is SF-src's hypothesis. *Not covered:* the cut-complement terms Q ≠ ∅ ((CE-Q)).
[RSF2-fix CE0-2/CQ-1, scope: the integrand contains the chart indicator 1_D(𝒞Z); on supp ν_∅ it is ≡ 1 (ρ' ≤ r_T/8), on Q ≠ ∅ terms it is
a NON-LOCAL function of Z, and outside the chart the integrand is the Haar integrand, not a Gaussian one. Session 3: on the band
(§10.1, Theorem CE-Q) 1_D ≡ 1 again; beyond it, (CE-Q^∞), the pricing is in U-variables. After Lemma SF-N♮ (§10.2) the status of
this corollary is CONDITIONAL ⇐ (FP-loc)_0 (+ the background clause gauge logs ≤ α_𝔫).]

**Corollary CE-exp^k: CONDITIONAL ⇐ (i) N_μ(|𝒞_k|) < ∞ [N5-sf_k's ℓ¹ conclusion, level-uniform ⇐ (N5-unif)], (ii) (L-hol)_k,
(iii) (FP-loc)_k, (N5-reg)_k, and the criticality of the level-k background for the full level-k action (the analogue of SF-T0 (5),
part of (I_k^E)''/(BG)_k) (not counted).** *Proof.* As CE-exp^0 with one change: a main-term density 𝓔_{k,x} is not strictly local.
Assign its cubic Taylor remainder R_x to X := {q(x)} (d(X) = 0). If (L-hol)_k gives 𝓔_{k,x}(e^AU) holomorphic and ≤ S_k on the weighted
polydisc 𝒫_{{x}}(ρ_k, μ_k) := {|A_b| < ρ_ke^{μ_kℓ^∞(x(b),x)}}, then for A ∈ 𝒫_{{x}}(ρ, μ_k), ρ ≤ ρ_k/2, the one-variable Cauchy bound on
ζ ↦ 𝓔_{k,x}(e^{ζA}U) (holomorphic for |ζ| < ρ_k/ρ ≥ 2) gives |R_x(A)| ≤ 2S_k(ρ/ρ_k)³. Since δ(x(b), X) ≤ ℓ^∞(x(b), x),
𝒫_X(ρ, μ_k) ⊂ 𝒫_{{x}}(ρ, μ_k), and Corollary CE-exp-𝒞 (weighted form, μ ≤ μ_k, 2g_k√NpN_μ(|𝒞_k|) ≤ ρ) gives (H-exp). The linear term
vanishes by (the criticality hypothesis); the quadratic term is in the Gaussian. ∎ ~~**So (OP-loc)_k is retired**~~: the operator enters
only through N_μ(|𝒞_k|) < ∞, which N5 already provides; the locality content moves to (L-hol)_k, an ACTIVITY statement (weighted
analyticity of the level-k main-term densities). ~~*Where (L-hol)_k would come from [inference]:* Theorem A5 (B) run in the
weighted space with weight e^{-μ_kd(·, x)} (growing data allowed), i.e. the weighted constants G_w, G_{D,w} of (G♯) with the weight
sign reversed; this is inside the B-NA wall (§7.2).~~
**[RSF2-fix CEk-1 + CEk-2 (binding, REVIEW_SF_S2 B-6).**
(1) *(L-hol)_k is NOT VIABLE AS STATED.* It asks 𝓔_{k,x}(e^AU) to be holomorphic and ≤ S_k for |A_b| < ρ_ke^{μ_kℓ^∞(x(b),x)} at ALL b.
𝓔_{k,x} is an energy density of the critical chain of E^♭(·; U) (HIST A5), which exists only on small-field domains (R_δ, 𝔇_{ε,α}).
At a link at distance d the polydisc allows |A_b| ≍ ρ_ke^{μ_kd} ≫ 1, where no critical chain exists and the density is undefined.
Exponential decay of the DERIVATIVE (A5 (C)) is weaker: f(A) = Σ_ye^{-κ|y|}log(1 + A_y) decays in that sense and is holomorphic on no
growing polydisc. The [inference] on A5 (B) "with growing data" is withdrawn: A5 (B) contracts in level-k sup-norm polydiscs.
**Replacement (L-loc)_k [OPEN; inside the B-NA wall]:** 𝓔_{k,x} = Σ_{R∋x}𝓔_{x,R}, with 𝓔_{x,R} depending on A on R only, holomorphic
and ≤ S_ke^{-κ_Ld(R)} on the UNIFORM polydisc max_{b∈R}|A_b| < ρ_k. Each piece is then strictly local and CE-exp-𝒞's strictly-local
branch applies with X ⊃ R (κ_L in M-units ≈ κ_5M). (L-loc)_k would follow from mixed-derivative decay of 𝓔 on a uniform polydisc
(A5 (C) for ALL mixed derivatives, not only the first), which sits behind (a5-G♯) and (G♯-patch).
(2) *Missing inherited activities; the rate does not survive iteration.* At stage k the integrand also carries the inherited
level-k polymer activities of (I_k^E)', of finite rate κ_in in M-units. CE-exp requires κ_in ≥ 273κ' + 1296W and returns rate
κ_c - 3κ_0 - 3; SF-blk turns that into L(κ_c - 3κ_0 - 3 - κ_0) - 1 < 273(κ_c + 16 log 2) + 1296W for every κ_c at L = 3, and the norm
requirement e^{-272κ'}c_0 is not reproduced either. The loss is entirely SF-geo's multiplicative d(X^+) ≤ 273d(X) + 272 (HULL's
far-site part is additive). New OPEN name **(CE-col)** (Theorem CE with collar-native linking), attacked in §10.3. **Corrected
statement:** CE-exp^k is CONDITIONAL ⇐ (i) N_μ(|𝒞_k|) < ∞ [⇐ (N5-unif)], (ii) **(L-loc)_k**, (iii) (FP-loc)_k, (N5-reg)_k,
criticality, (iv) the inherited activities as additional (H-exp) inputs, and (v) **(CE-col)** for any composition across
levels. As stated in session 2 (three activity types only) it is NOT the stage-k expansion.]

**(CE-Q): OPEN (named).** Reason recorded (inference, not proven): for a Q-site y with |Z_y| = λp, λ ≫ 1, the site-interpolation
needs a Cauchy radius e^{μδ(y,X)}/λ ≥ 1, i.e. δ(y, X) ≥ (log λ)/μ; nearer activities see a field of size ∝ λ, outside the
analyticity domain. So the region of radius ≈ (log λ)/m_1 around each large Q-site is a fluctuation large-field region to be
excised and priced ((SG^fl), RLARGE §3.2 branch (ii)), with the Q-weight 2^{n/2}e^{-λ²p²/4} (SF-cut (b), shell form) paying the
region's polymer cost; the cut-good complement is then Corollary CE-exp^0 on a region.

### 7.2 STEP 3: (a5-G♯), (a5-U), (a3-q) restated; what is proven

**Restatement (applied).** (a5-G) of HIST §25.5 is replaced by (a5-G♯) of §6.2, for the reason of REVIEW_HIST_S4 S4-1 (the sup-norm
inverse grows like L^{2(k-1)} at the trivial chain: BNA-F2). (a5-U) and (a3-q) are stated on R_{3ε_1}, and Theorem A5 is to be read
with ε_1 ≤ δ_a/3 (so δ = 3ε_1 in A5 (A): E ≤ 9C_3ε_1² ≤ η_AE and residuals ≤ 3C_♮√C_3ε_1 ≤ ε_R) and **s_5 ≤ min{ε_1/5, 0.01}** (Lemma BS).
These are proposed edits for HIST's owner (lane D), recorded here; SF does not edit HIST.

**Lemma BS: PROVEN-HERE (not counted; elementary).** *Proof.* Let p be a level-k plaquette with links b_1, …, b_4 (orientations ±).
U'_p = Π_i(U_{b_i}e^{Z_{b_i}})^{±1}. Replace the factors one at a time; all factors are unitary, so
||U'_p - U_p|| ≤ Σ_i||e^{±Z_{b_i}} - 1|| ≤ 4(e^s - 1) (||e^W - 1|| ≤ e^{||W||} - 1). Hence ||1 - U'_p|| ≤ 2ε_1 + 4(e^s - 1) ≤ 2ε_1 + 4.05s
(e^s - 1 ≤ se^s ≤ 1.0102s for s ≤ 0.01) ≤ 2ε_1 + 0.81ε_1 < 3ε_1. ∎ The real points of P_{s_5}(U) are Ue^X with X ∈ su(N), ||X|| ≤ s_5
(HIST l.1552), so they lie in R_{3ε_1}: the openness step of A5 (B) stays where (a5-U), (a3-q) hold. (s2 E1-E2: 10⁴ random SU(2),
SU(3) plaquettes with ||1 - U_p|| ≤ 0.2 and ||Z|| ≤ 0.01: the bound is never exceeded, max slack -1.5·10⁻²; 4(e^{0.01} - 1) = 0.040201.)

**Lemma G-pert: PROVEN-HERE (implication; not counted).** *Statement as proven.* Hypotheses as pre-stated (§6.2). Then for
t := ||x^r||_X + ||B^r||_D ≤ min{ρ_0, 1/(4GC_R), 1/(4G_wC_{R,w})}:
  ||𝓛(x^r)^{-1}||_{Y→X} ≤ 2G,  ||𝓛(x^r)^{-1}N(x^r)||_{D→X} ≤ 2(G_D + GC_Rt),  and weighted: 2G_w, 2(G_{D,w} + G_wC_{R,w}t).
*Proof.* ∇(E_NA∘exp + ½||Γ_gf·||²)(x) = 𝓛x + NB + 𝔑(x; B) on the trivial-background per-level slice (B-NA-red's definition of 𝔑), so
the slice Hessian at x^r is 𝓛(x^r) = 𝓛 + D_x𝔑(x^r; B^r) and the data map is N(x^r) = N + D_B𝔑(x^r; B^r). ||𝓛^{-1}D_x𝔑(x^r; B^r)||_{X→X}
≤ G·C_R(2||x^r|| + ||B^r||) ≤ 2GC_Rt ≤ ½, so 𝓛(x^r) = 𝓛(1 + 𝓛^{-1}D_x𝔑) is invertible with 𝓛(x^r)^{-1} = (1 + 𝓛^{-1}D_x𝔑)^{-1}𝓛^{-1}
and norm ≤ 2G; 𝓛(x^r)^{-1}N(x^r) = (1 + 𝓛^{-1}D_x𝔑)^{-1}(𝓛^{-1}N + 𝓛^{-1}D_B𝔑), norm ≤ 2(G_D + GC_Rt). The weighted bounds are the same
computation in the weighted norms. ∎ *Reading.* At every chain that is X_c-small around the trivial chain in one global gauge
(B-NA-red's class of data, ||B_k||_D ≤ ε_0), (a5-G♯) follows from the trivial-chain items (G♯_0-field) + (R♯_ω) (+ (FP♯') on the
ball)~~: no new wall~~. **[RSF2-fix GP-1/GP-2 (scope).** (GP-1) G-pert bounds the Hessian of E_NA∘exp + ½||Γ_gf·||² in the TRIVIAL
slice at x^r, not the Hessian in "a per-level covariant slice through ψ^r" as (a5-G♯) is stated; the two are different gauge-fixed
operators (re-centred slice functional and Feynman term; moved residual groups). So G-pert gives (a5-G♯) only if (a5-G♯) is
stated at X_c-small chains in the trivial slice (the natural choice, where NA-IFT works), or with a slice-change lemma (the two
slice Hessians at a critical chain conjugate by a gauge-chart change bounded in the §33 pair), not proven. (GP-2) Its hypothesis
t ≥ ||B^r||_D small means the data are small in ONE global gauge: exactly B-NA-red's class. G-pert is NA-IFT's Neumann step and
reaches no background that B-NA-red does not already handle; the generic background (BNA-F4) is (G♯-patch).] *Remark (re-centred remainder).* If (R♯_ω)'s quadratic bound holds on the COMPLEX ball of radius ρ_0, the
re-centred remainder 𝔑_r(y; B') := 𝔑(x^r + y; B^r + B') - 𝔑(x^r; B^r) - D𝔑(x^r; B^r)(y, B') obeys, for t ≤ ρ_0/4 and ||y|| + ||B'|| ≤ ρ_0/4,
||𝔑_r(y; B')|| ≤ (8/3)C_R(||y|| + ||B'||)² (one-variable Cauchy on ζ ↦ 𝔑(x^r + ζy; B^r + ζB'), radius ≥ 3, sup ≤ C_Rρ_0²); the matching
Lipschitz bound is the same argument for D𝔑 (not written). So "(R♯) at ψ^r" is a consequence of a complex-ball form of (R♯_ω).

**Proposition U-red: PROVEN-HERE (implication; not counted).** [Post-proof precision, written 03:54 UTC with the proof: (MIN-reg)'s gauge must be the
COMPLETE one, h = 0 AND Γ_gf = 0 on the residual groups (reachable on the ball by (FP♯')); the pre-stated "in the per-level slice"
is read that way.] *Proof.* Let U ∈ R_{3ε_1} be real, ψ^r a minimiser of E^♭(·; U) (attained, HIST (a') (1)), and ψ' any minimiser. By
(MIN-reg), after a chain gauge trivial at level k, ψ' = ψ^re^{x'} with x' in the complete gauge through ψ^r and ||x'||_{X_c} ≤ r_U.
A minimiser on the boundaryless manifold SU(N)^{links} at which E^♭ is smooth is critical in every direction; with Γ_gf(x') = 0 the
Feynman term's gradient DΓ_gf^TΓ_gf(x') vanishes, so x' is a zero of the slice gradient 𝓛_rx + 𝔑_r(x; 0) (data fixed: B-increment 0),
i.e. a fixed point of Φ(x) := -𝓛_r^{-1}𝔑_r(x; 0). So is x = 0 (ψ^r itself). On ||x||_{X_c} ≤ r_U, Lip(Φ) ≤ GC(2r_U) ≤ ½ (NA-IFT's
Lipschitz bound with s = 0). Two fixed points of a contraction on a convex set coincide: x' = 0, so ψ' is gauge-equivalent to ψ^r by a
chain gauge trivial at level k. ∎ *Reading.* (a5-U) is reduced to the B-NA items at ψ^r plus (MIN-reg), a quantitative a-priori
statement (any two minimisers are X_c-close after gauge). (MIN-reg) is not implied by AE-red's own-unit bounds: own-unit
regularity ε_R at level 0 is coarse-unit size L^{2k}ε_R in the X_c norm (§33's units), so it says nothing about X_c-closeness.

**Status of STEP 3 (the wall, named).** The restated A5 rests on: (G♯_0-field) [trivial-background multi-scale Schauder bound; PROOF:
soft half PROVEN [S15], fine half ⇐ (LED-src) OPEN, plus G♯_0-plain, G♯_0-fine-up and the per-level abelian multi-level gap, all
OPEN], (R♯_ω) [stated, argued, PROOF l.3477-3491], (FP♯') on the ball, **(G♯-patch)** [new name: patching local (G♯)'s across MSG
cells for backgrounds with no globally small gauge], **(MIN-reg)** [new name], (a3-q) on R_{3ε_1}, (MS-Sob). This IS the B-NA wall
((G♯) + (R♯), (R♯) OPEN) plus two named items; (a5-G♯) is not attacked further here. (BG-loc)'s content is A5 (A)-(C) under these.

### 7.3 STEP 1 new items

**Lemma SF-J': PROVEN-HERE (not counted).** *Proof.* (1) *Uniqueness.* Let U have distinct eigenvalues e^{iφ_a}, φ_a ∈ [0, 2π). If
A ∈ D'_N and e^A = U, A commutes with U, so A preserves U's one-dimensional eigenspaces: A = W diag(iθ_a)W^† in U's eigenbasis, with
θ_a ∈ φ_a + 2πZ, Σθ_a = 0 (A ∈ su(N)), spread < 2π. With c := min_aθ_a, every θ_a is the representative of φ_a in [c, c + 2π). For
c ∈ R let S(c) := Σ_a(the representative of φ_a in [c, c + 2π)). S is a non-decreasing step function, constant between consecutive
points of {φ_a} + 2πZ, rising by exactly 2π at each (eigenvalues distinct), with S(c + 2π) = S(c) + 2πN; det U = 1 gives S(c) ∈ 2πZ.
So S takes the value 0 on exactly one constancy interval, and on it the representatives are one fixed set {θ_a}. Hence exactly
one A ∈ D'_N has e^A = U (the θ's determine A via W), and this A exists (the representatives on that interval have spread < 2π and
sum 0). (2) *Chart.* U_dist := {U with N distinct eigenvalues} has full Haar measure (its complement is the zero set of the
discriminant of the characteristic polynomial, a proper real-analytic subset). D''_N := exp^{-1}(U_dist) ∩ D'_N = {A ∈ D'_N with
distinct eigen-angles} (spread < 2π: θ_a - θ_b ∈ 2πZ forces θ_a = θ_b), whose complement in D'_N is Lebesgue-null. exp: D''_N → U_dist
is a bijection by (1), smooth, with Jacobian j(A) = Π_{a<b}(sin(μ_ab/2)/(μ_ab/2))² > 0 (SF-J (3); |μ_ab| = |θ_a - θ_b| < 2π), hence a
diffeomorphism (inverse function theorem). log j is holomorphic near D'_N (spectral radius of ad A = spread < 2π; SF-J (4)). The
change of variables gives ∫f dU = c_N∫_{D'_N}f(e^AU_0)j(A)dA for every f ∈ L¹, every N. ∎ (s2 D: in 4·10⁴ Haar samples per N = 3, 4 and
10⁴ for N = 2, 5, exactly one spread-< 2π traceless log every time, reconstruction error 3.1·10⁻¹⁵; the Haar fraction of exp(D_N) is
0.9752 (SU(3)), 0.9486 (SU(4)), 0.9257 (SU(5)), 1.0000 (SU(2)).)

**Lemma SF-src: PROVEN-HERE ⇐ NORM-an + (SF-N♮) (not counted).** (SF-N♮) is read as: e^AU ∈ D_c(y_bg + c_y max|A_b|) with
C_Nθ ≤ ½ there, for max|A_b| ≤ r_𝔫, and y_bg/c_y ≤ r_𝔫. *Proof.* Fix A with max|A_b| = ρ ≤ r_𝔫/2, a := A/ρ, φ(ζ) := 𝔫_c(e^{ζa}U),
holomorphic on |ζ| < r_𝔫 (NORM-an's holomorphy on D_c). Put R := max{y_bg/c_y, 2ρ} ≤ r_𝔫. On |ζ| ≤ R, |φ| ≤ K_𝔫(y_bg + c_yR)² (NORM-an:
|𝔫_c| ≤ 2C_Nθ = K_𝔫y²). For |ζ| ≤ R/2, |φ'(ζ)| ≤ 2sup_{|ζ'|≤R}|φ|/R; ρ ≤ R/2, so |φ(ρ) - φ(0)| ≤ 2ρK_𝔫(y_bg + c_yR)²/R. If R = y_bg/c_y
this is 8K_𝔫c_yy_bgρ; if R = 2ρ > y_bg/c_y it is ≤ K_𝔫(3c_yρ)² = 9K_𝔫c_y²ρ². ∎ At y_bg = 0 the linear term vanishes.
[RSF2-fix src-1/src-2: (1) when R = r_𝔫 the closed disc touches the boundary of the holomorphy disc; Lemma SF-N♮ (§10.2) gives
holomorphy on |ζ| < 2r_𝔫, so the closed disc |ζ| ≤ R ≤ r_𝔫 is strictly inside and the proof stands as written. (2) The bound is
the MAX of the two cases, max{8K_𝔫c_yy_bgρ, 9K_𝔫c_y²ρ²}; the sum is valid but weaker.]

## 8. Session-2 outcome (written after §7)

### 8.1 Status list after the binding fixes and session 2 (all unreviewed)
| item | status | change in session 2 |
|---|---|---|
| SF-J | PROVEN-HERE (counted) | Fix SF-J-1/2 applied (chart-specific correction; Frobenius structure fixed) |
| **SF-J'** | **PROVEN-HERE** (not counted) | new: spread chart, Haar-full for every N |
| SF-T0 | PROVEN-HERE (counted) | κ_0 → κ_ker (Fix SF-T0-1) |
| SF-DC, CE^+, SF-blk | PROVEN-HERE (counted) | unchanged; SF-DC/SF-s no longer on the main CE route |
| SF-thr, SF-cut, SF-N0, SF-WN, SF-geo, SF-V | PROVEN-HERE (not counted) | Fixes SF-thr-1/2, V-1, V-2, V8 note applied |
| SF-s | standard | unchanged |
| SF-thr-k | CONDITIONAL ⇐ (N5-unif) ⇐[PROOF S21 NAH-unif, implication] (H-K) + (H-C) [RSF2-fix: ⇐ [S22] NAH-unif′: (H-K) + (H-C⁺) + (H-ℂ); (H-G) derived by HG-ind] | re-based; soft-clause sentence withdrawn for the background |
| SF-A2^0 | CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮) | source size O(y_bg·g_0√NN_0p); covariance Ng_0²C |
| **SF-src** | **PROVEN-HERE ⇐ NORM-an + (SF-N♮)** (not counted) | new |
| **LOC-s** | **PROVEN-HERE** (counted) | new |
| **HULL** | **PROVEN-HERE** (not counted) | new |
| **Theorem CE-exp** | **PROVEN-HERE ⇐ Theorem CE, SF-geo, CE-geo'** (counted) | new: (CE-s)^exp in site-interpolation form |
| **CE-exp-𝒞** | **PROVEN-HERE** (not counted) | new |
| **CE-exp^0** | **CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮)** | new; replaces SF-A3^0's cut-good part (was ARGUED) |
| **CE-exp^k** | **CONDITIONAL ⇐ N_μ(|𝒞_k|) < ∞, (L-hol)_k, (FP-loc)_k, (N5-reg)_k, criticality** [RSF2-fix: (L-hol)_k NOT VIABLE AS STATED → (L-loc)_k; + inherited activities + (CE-col)] | new; ~~retires (OP-loc)_k~~ retires its operator half only |
| **Lemma BS** | **PROVEN-HERE** (not counted) | new (base-set fix S4-2) |
| **Lemma G-pert** | **PROVEN-HERE (implication)** (not counted) [RSF2-fix: trivial-slice Hessian at x^r, B-NA-red's class only; its "Reading" withdrawn] | new |
| **Proposition U-red** | **PROVEN-HERE (implication)** (not counted) | new |
| (CE-s) | ARGUED; now an alternative route, not needed by CE-exp | — |
| SF-A3^0 | ARGUED for its Q ≠ ∅ part only; cut-good part = CE-exp^0 | narrowed |
| (BG-loc) | DROPPED (ill-posed; its content = A5 (A)-(C)) | Fix BG-loc-1 |
| (OP-loc)_k | ~~RETIRED (replaced by (L-hol)_k inside CE-exp^k)~~ [RSF2-fix] operator half RETIRED; activity half = (L-loc)_k, OPEN | Fixes OP-1/2/3, then retired |
| (SF-N) | reduced to (SF-N♮) (domain match) | Fix SF-N-1 |
| OPEN names now: (SF-N♮), (FP-loc)_k, (N5-reg)_k, (L-hol)_k, (CE-Q), (a5-G♯) [B-NA], (R♯) at ψ^r [B-NA], (G♯-patch), (MIN-reg), (a5-U), (a3-q) on R_{3ε_1} | | |

**Tally of this file after session 2:** PROVEN-HERE 20 + 1 standard (SF-s): counted 7 (SF-J, SF-T0, SF-DC, CE^+, SF-blk,
LOC-s, CE-exp); not counted 13 (SF-thr, SF-cut, SF-N0, SF-WN, SF-geo, SF-V, SF-J', SF-src, HULL, CE-exp-𝒞, BS, and the
implications G-pert, U-red). CONDITIONAL 4 (SF-thr-k, SF-A2^0,
CE-exp^0, CE-exp^k); ARGUED 2 ((CE-s) as an alternative, SF-A3^0's Q ≠ ∅ part). No RLARGE §4.2 row is discharged; no PROOF.md tally
change is proposed (the ledger owner decides). Row 3's stage-0 A3 part is reduced from ARGUED to CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮)
for the cut-good term.

### 8.2 What (SF^J)_k now rests on
- **Stage 0:** A1 PROVEN (BR1/NAH1); A2 ⇐ (FP-loc)_0 + (SF-N♮); A3 cut-good term ⇐ the same (CE-exp^0); A3 cut-complement ⇐ (CE-Q);
  A4 large polymers PROVEN (SF-blk), small polymers ⇐ (SF-irr).
- **Stage k ≥ 1:** add (N5-unif) ⇐ (H-K) + (H-C) [RSF2-fix: + (H-C⁺) + (H-ℂ), (H-G) derived; PROOF S22] [thresholds and N_μ(|𝒞_k|)]; (L-hol)_k [RSF2-fix: → (L-loc)_k; + the inherited activities and (CE-col)] [activity analyticity, inside the B-NA wall];
  (N5-reg)_k; (FP-loc)_k; the main term's A5 hypotheses (a5-G♯) + (R♯) [B-NA], (G♯-patch), (MIN-reg), (a5-U), (a3-q), (MS-Sob).
- **Constants:** CE scale M ≥ 3.19·10¹³ fine spacings with N5-w0's m_1 (was 2.6·10¹⁵ on the walk route); H'_0 ≤ c_0(κ_c) with an
  e^{272κ'} factor from SF-geo's crude collar bound: existence only. [RSF3-fix stale-M: this M is g-independent; session 3's
  CE-Q added (M-Q), which made M ∝ log(1/g_0); Theorem CE-Q-col (§13.1) removes (M-Q), so M stays g-independent (condition (M-W3),
  (μ/2)M ≥ 5κ' + 4 log M + 8, on the CE-col route).]

### 8.3 Proposed edits for other owners (SF edits none of these files)
- **PLD l.1114-1117 (owner PLD):** "covariance g_0²C(𝔟(V), V) … up to the normalisation constant of the action (a factor depending
  only on N)": the factor is N (stage-0 exponent (u_0/N)(S_W + κΣφ̂), so the covariance is Ng_0²C); σ_fl² gains a factor N. Harmless
  (only finiteness is used); make it explicit.
- **HIST l.1772 (owner HIST):** "c' := 1.0107√N" is used as an upper-bound constant in y'_η and (Z2); 4arcsin(¼) = 1.010721 > 1.0107,
  so set c' := 1.011√N (all smallness conditions have slack; no conclusion changes). HIST l.1185 (F1) parenthetical: "≤ 1.0107" →
  "≤ 1.0108".
- **HIST §25.5 (owner HIST/lane D):** (a5-G) → (a5-G♯) (§6.2); (a5-U), (a3-q) on R_{3ε_1}; ε_1 ≤ δ_a/3; s_5 ≤ min{ε_1/5, 0.01} (Lemma
  BS); HIST l.1731-1733 add: 𝔫_c's linear fluctuation term is O(y_bg)·|A| (Lemma SF-src).
- PROOF l.701, l.3811 displays "= 1.0107" → "1.01072" (display only).

---

# SESSION 3 (2026-10-28 UTC). Inputs read before 04:25 UTC: REVIEW_SF_S2.md (BINDING; in full; md5 e0f0e111…), SF.md (ab0199f0…),
SF_LOG.md, PROOF.md 4a7bbccc… (Theorem CE + Lemmas CE-geo, TG, CE-geo' l.1857-2028, l.2264-2290; Setting N5-0 l.5149-5155
(d = the ℓ¹ torus distance of positions); [S21] Proposition NAH-unif with the [R21-fix] block l.6069-6136; [S22] block l.6140-6368:
Lemmas ENV, HG1, LOC_1, HG-ind, Corollaries H-fac, CURV1_1, failure mode CURV-F2′, Proposition NAH-unif′, c38, Lemma TOWER-VAR,
Proposition COMP, COMP-F1, (CL-cl), N5 node status [S22]), HIST.md 468e9f03… (§25.1 TERM-an (ii)-(iii) l.1555-1580, §25.4 NORM-an
l.1628-1642), REVIEW_HIST_S4 M-3 (l.276-278), PROOF l.3459 (p_L := 5L - 4).

## 9. Pre-stated targets, session 3 (appended at 04:26 UTC, 2026-10-28, BEFORE any session-3 proof and before the s3 criteria)

### 9.1 STEP 2: (CE-Q), the cut-complement terms
*Idea fixed before writing (exploratory, unwritten):* do not excise a radius-(log λ)/m_1 region in Z. Instead split each site's
noise into dyadic shells and keep the large-noise sites' activities unexpanded. Then (i) the shadow radius (j + 1)log 2/μ of a
shell-j site fits inside one CE cube once μM ≳ 2(j + 1)log 2, (ii) the field a shell-j site produces stays in the analyticity
polydisc for 2^j ≲ 1/(g_0p), and on that band the chart indicator is identically 1, and (iii) the Gaussian tail e^{-4^jp²/4} of the
shell beats the action-remainder cost, which by Hölder with the ℓ¹ row and column norms of 𝒞 is ≲ g_08^jp³ per large site with no
M⁴ factor. Steps 3-4 of Theorem CE (the hard-core part) are then used as a black box on integrated activities.

**Setting CE-Q.** Corollary CE-exp^0's setting and notation (𝒞 := 𝒞(U(V), V), μ := m_1, ρ' := 2g_0√NpN_μ(|𝒞|), h_0, n_*), with
N_0 := N_0(|𝒞|) ≤ N_μ := N_μ(|𝒞|) (link kernel), and the integration measure μ_wn itself (no cut). Shells: for a site y,
j_y := -1 if |Z_y| ≤ p, j_y := j ≥ 0 if 2^jp < |Z_y| ≤ 2^{j+1}p. Q(Z) := {y : j_y ≥ 0}. **Band:** j_y ≤ j_max for every y, where
j_max := the largest j ≥ 0 with (B1) ρ' + g_0√NN_02^{j+1}p ≤ ρ_* := min{r_T/8, r_𝔫/2} and (B2) C_3g_02^jp ≤ 1/16, given also
(B3) C_2g_0² ≤ 1/16, C_1g_0 ≤ 1/16, p ≥ 1. [RSF3-fix (Part A 11(b), Q3, Q5): the proof uses **(B1′)** 2ρ' + g_0√NN_02^{j+1}p ≤ ρ_*
(§10.1 Step 2), not (B1); (B3) reads **p ≥ 2** (Σ_{j≥0}e^{-4^jp²/16} ≤ 2e^{-p²/16} fails at p = 1); and the band constants are renamed
**C_1^Q, C_2^Q, C_3^Q** (they clash with Theorem CE's prefactor C_1 = 2κ_0B).] The constants C_1, C_2, C_3 (explicit in S_T, r_T, N, N_0, n_b, n'_c, K_𝔫, c_y, y_bg; n_b :=
the maximal number of action terms whose pattern contains a given link, n'_c := the maximal number of coarse links whose contours
contain a given link) are fixed in the proof. **Deep set:** 𝔇 := {Z : some j_y > j_max}.
- **Lemma LOC-s′ (refined Cauchy domain).** In Lemma LOC-s, |F_{X,S}| ≤ sup|g|·Π_{y∈S}r_y^{-1} with the sup over the set
  {s : s = 1 on ∪X^+; |s_y - σ_y| ≤ r_y for y ∈ S, some σ ∈ [0, 1]^S; s_y = 0 for y ∉ ∪X^+ ∪ S}, for any radii r_y > 0 for which g is
  holomorphic on a neighbourhood of that set. *Planned: PROVEN-HERE (not counted).*
- **Lemma QC (the large-site cost).** For σ_b := g_0√NΣ_{y∈Q}|𝒞(b, y)|2^{j_y+1}p (the field of the large sites at real s = 1):
  Σ_bσ_b³ ≤ 4N_0³Σ_{y∈Q}t_y³, Σ_bσ_b² ≤ 4N_0²Σ_yt_y², Σ_bσ_b ≤ 4N_0Σ_yt_y, t_y := g_0√N2^{j_y+1}p. *Planned: PROVEN-HERE (not counted).*
- **Theorem CE-Q (band).** Assume CE-exp^0's hypotheses ((FP-loc)_0, (SF-N♮), the background class), (B1)-(B3), and
  **(M-Q)** μM ≥ 2(j_max + 1)log 2, **(M-W)** (μ/2)M ≥ 3κ' + 4 log M + 8 (κ' := κ_c + 16 log 2). Then on supp μ_wn ∖ 𝔇 the chart
  indicator is 1 and
    ∫_{𝔇^c}exp(Σ_XH_X(g_0√N𝒞Z))dμ_wn(Z) = μ_1(good)^{|Λ|}·exp(Σ_𝒵𝓗_𝒵),  |𝓗_𝒵| ≤ C_1Ĥ_0e^{-(κ_c - 3κ_0 - 3)d(𝒵)},
  where μ_1(good) := μ_wn,y(|Z_y| ≤ p), the sum runs over polymers 𝒵, 𝓗_𝒵 depends only on Z on 𝒵, and
  Ĥ_0 := max{H'_0, 16e²M⁴η̂/C_K}, H'_0 := 2^{16}e^{272κ' + 1296w_8}h_0, η̂ := e^{274κ̂}Γ·4·2^{n/2}e^{-p²/16}·2, κ̂ := κ_c - κ_0,
  Γ := exp(546·11⁴κ̂ + 13⁴w_8); provided κ_c > 3κ_0 + 3, Ĥ_0 ≤ c_0(κ_c), and e^{2κ̂}C_KH'_0K_0 + M⁴η̂ ≤ 1/16. That is: the
  cut-complement terms with every noise variable below 2^{j_max+1}p form, together with the cut-good term, ONE convergent polymer
  gas with the decay rate of CE-exp^0. *Planned: CONDITIONAL ⇐ (FP-loc)_0 + (SF-N♮) (the same hypotheses as CE-exp^0); the
  analytic part PROVEN-HERE ⇐ Theorem CE (Steps 1, 3-4), LOC-s′, QC, HULL, SF-geo, CE-geo' (counted).*
  **[RSF3-fix (Part A 11(c)): the constants of this pre-statement (Γ with 11⁴, 13⁴; the η̂ display; "the decay rate of CE-exp^0";
  the condition Ĥ_0 ≤ c_0(κ_c)) are SUPERSEDED by §10.1's "Statement as proven" (as corrected there by Fixes Q1, Q2) and, for the
  iterable form, by Theorem CE-Q-col (§12.1, §13.1).]**
- **(CE-Q^∞) [named, OPEN].** The deep set 𝔇: its μ_wn-mass is ≤ |Λ|·2^{n/2}e^{-4^{j_max+1}p²/4} with 4^{j_max+1}p² ≥ a_*/g_0² (a_*
  explicit), but there the field leaves the analyticity polydisc (and possibly the chart), so the Gaussian-Haar integrand has no
  Z-local bound. It must be priced in U-variables (RLARGE §3.2 branch (ii)). Expected failure if attempted in Z: the remainder
  u_0V_τ is O(1/g_0²) at |A_b| = O(1), comparable to the Gaussian exponent, so no Gaussian domination holds without a local
  coercivity bound of the true action.
  [RSF3-fix C-1..C-5 (Part C): the displayed bound is the μ_wn-MASS of 𝔇, not its contribution (e^{ΣH} can be e^{O(1/g_0²)} on 𝔇);
  𝔇 as written depends on the gauge-direction noise (1 - Π_U)Z, which 𝒞 kills; the |Λ| is a union bound, not a per-site
  extraction; and "price it in branch (ii)" is circular as it stands (branch (ii)'s (SG^fl) lists SF's cluster expansion as an
  input). Restated in §12.2 (pre-statement) and §13.2 (what is proven).]

### 9.2 STEP 3: (SF-N♮), the domain match with NORM-an
- **Lemma SF-N♮ (natural form).** Let |·| be the HS norm (or the operator norm) on gl(N, ℂ), C_N, c_N NORM-an's constants, and
    y_♭ := min{1/40, [36.8(2 + 2c_N)max(1, C_N)]^{-1/2}},  c_y := 2.2p_L,  r_𝔫 := y_♭/(3c_y),  α_𝔫 := y_♭/(3c_y).
  Let U be a real background and c a coarse link such that some real gauge has link logs ≤ α_𝔫 on the links of S_c and of all
  contours T_j of c. Then y_bg := max_j|log(S_c⁻¹T_j)| ≤ c_yr_𝔫, and for every complex A with a := max_{b in S_c, T_j}|A_b| ≤ 2r_𝔫 the
  field e^AU lies in D_c(y_♭) ⊂ D_c(1/20), with y(e^AU) ≤ y_bg + c_ya ≤ y_♭, θ := 18.4y²(2 + 2c_N) ≤ ½ and C_Nθ ≤ ½ there.
  *Planned: PROVEN-HERE (not counted).* Consequences: SF-src holds for ρ ≤ r_𝔫/2 with the closed disc |ζ| ≤ R ≤ r_𝔫 strictly inside
  the holomorphy disc |ζ| < 2r_𝔫 (Fix src-1); CE-exp^0, SF-A2^0 and Theorem CE-Q become CONDITIONAL ⇐ (FP-loc)_0 alone, with the
  background-class clause "gauge logs ≤ α_𝔫 on each contour pattern" added. [RSF3-fix SN-2: "alone" is withdrawn. The background
  clause **(BGC) gauge logs ≤ min{r_T/4, α_𝔫} on every term pattern and every coarse link's contour pattern** is an explicit
  HYPOTHESIS of the background class wherever (FP-loc)_0 is cited below; its derivation from BR1 (iii) + Lemma AX (10p_Lℓε' ≤ α_𝔫)
  is a bracketed remark, not a written step.]

### 9.3 STEP 4: (CE-col), Theorem CE with collar-native linking
- **Setting CE-col.** Setting CE. For a set c of cubes, c^+ as in §0, c^{(2)} := the cubes at ℓ^∞ index distance ≤ 2 from c. c is
  **2-connected** if it is connected under "index distance ≤ 2". **d^+(c)** := the infimum of the lengths of connected finite unions of
  segments contained in ∪c^+ that meet every closed cube of c. Activities H(X, Φ) for polymers X depend on Φ|_{X^+} only.
  a' := log(2·624²), κ̃_0 := 16a' (≈ 217.05), K̃_0 := e^{κ̃_0}/624², C_K := 32eK_0, B̃ := 625C_Ke^{κ̃_0}K̃_0, C̃_1 := 2κ̃_0B̃.
- **Lemma GEO-col.** (a) |c| ≤ 16(1 + d^+(c)) for every c with d^+(c) < ∞; (b) if c_1, …, c_n are sets with d^+(c_i) < ∞ and a tree on
  {1, …, n} with c_i^+ ∩ c_j^+ ≠ ∅ along its edges, then d^+(∪c_i) ≤ Σ_id^+(c_i) + 6(n - 1); for polymers X_i, d^+(X_i) ≤ d(X_i);
  (c) Σ_{c ∋ □, 2-connected}e^{-κ̃_0d^+(c)} ≤ K̃_0; (d) c^+ ∩ Z^+ ≠ ∅ implies c ∩ Z^{(2)} ≠ ∅, |Z^{(2)}| ≤ 625|Z|; (e) d^+(c) =
  inf{d(Y') : Y' a polymer, c ⊂ Y' ⊂ c^+}. *Planned: PROVEN-HERE (not counted).*
- **Theorem CE-col.** In Setting CE-col suppose |H(X, Φ)| ≤ H_0e^{-κd(X)} on supp μ for every polymer X, with
  **κ > κ_0 + 2κ̃_0 + 3** (≈ 588.4) and **H_0 ≤ c̃_0(κ) := min{log 2, (32K_0)^{-1}e^{-6(κ-κ_0)}, (8B̃)^{-1}e^{-6(κ-κ_0-2κ̃_0-2)}}**.
  Then ∫exp(Σ_XH(X))dμ = exp(Σ_YH#(Y)), the sum over 2-connected sets Y, with H#(Y) depending only on Φ|_{Y^+} and on
  {H(X) : X ⊂ Y}, and **|H#(Y)| ≤ C̃_1H_0e^{-(κ - κ_0 - 2κ̃_0 - 3)d^+(Y)}**. Re-indexed to polymers (Lemma GEO-col (e)), the output is a
  polymer activity of rate κ - κ_0 - 2κ̃_0 - 3 - 16 log 2 with prefactor 2^{16}e^{κ}C̃_1H_0: the loss is ADDITIVE, with no factor
  1/273. *Planned: PROVEN-HERE ⇐ Theorem CE's proof (Steps 1-4 re-run), Lemma TG, CE-geo' (g1'), (g4'), (g5') (counted).*
- **Corollary CE-exp-col.** Theorem CE-exp with Theorem CE-col in place of Theorem CE and the collar-free hull Y_0(X, S) (X plus the
  cubes met by the segments σ_y to the nearest cube of X): with W_3 := M⁴e^{3κ'}Σ_{n≥1}(2n + 1)⁴e^{-(μM-2κ')n} and κ' := κ_c + 16 log 2,
  under (H-exp)(κ, h_0, μ) with κ ≥ κ' + 1296W_3, **H''_0 := 2^{16}e^{1296W_3}h_0 ≤ c̃_0(κ_c)** and κ_c > κ_0 + 2κ̃_0 + 3, the
  conclusion of Theorem CE-col holds with rate κ_c - κ_0 - 2κ̃_0 - 3 in d^+ and prefactor C̃_1H''_0. No e^{272κ'} factor. Sufficient:
  μM ≥ 5κ' + 4 log M + 8 ⇒ W_3 ≤ w_8. *Planned: PROVEN-HERE (counted with CE-col? no: not counted, a corollary).*
- **Proposition RATE (the rate survives iteration at L = 3).** With SF-blk, the composite level map κ_in ↦ (output rate of
  CE-exp-col, re-indexed, blocked) reproduces the input requirement κ ≥ κ_c + 16 log 2 + 1296W_3 iff κ_c ≥ κ_c^* (explicit, ≈ 1.15·10³
  at L = 3), whereas the CE^+/HULL route (factor 273) reproduces it for no κ_c. *Planned: PROVEN-HERE (arithmetic; not counted).*
  What it does not give: the NORM reproduction of the small polymers (d < 1), which stays (SF-irr).

## 10. Session-3 proofs (written from 04:34 UTC, after §9, after the STEP-1 [RSF2-fix] edits and after s3 ran 04:33:31-04:33:35 UTC)

### 10.1 STEP 2: (CE-Q)

**Lemma LOC-s′: PROVEN-HERE (not counted).** *Proof.* Lemma LOC-s's step (3) writes F_{X,S} = ∫_{[0,1]^S}(∂^Sg)(σ_S, 0_{F∖S})dσ_S.
The derivative is taken in the S-variables only, at a point whose F∖S-coordinates are 0. Cauchy's formula for the mixed first
derivative on the closed polydisc Π_{y∈S}{|s_y - σ_y| ≤ r_y} (F∖S-coordinates fixed at 0, ∪X^+-coordinates fixed at 1) gives
|∂^Sg(σ_S, 0)| ≤ sup|g|·Π_{y∈S}r_y^{-1}, the sup over exactly the stated set. ∎ (s3 A: a function with a pole 10⁻³ outside the
refined domain; bound never violated in 791 sets, max ratio 1.08·10⁻⁴; for some S the UNREFINED polydisc contains the pole, so
the refinement is load-bearing.) *Use.* Far sites outside ∪X^+ ∪ S contribute NOTHING to the field in the bound, and every site
may carry its own radius.

**Lemma QC: PROVEN-HERE (not counted).** Write a_{by} := |𝒞(b, y)| := the operator norm of the block (𝒞(b, b'))_{b' based at y},
so a_{by} ≤ Σ_{b' at y}|𝒞(b, b')|, Σ_ya_{by} ≤ N_0 (link row sums) and Σ_ba_{by} ≤ Σ_{b' at y}Σ_b|𝒞(b', b)| ≤ 4N_0 (𝒞 symmetric, SF-WN;
4 links per site in d = 4). σ_b = Σ_ya_{by}t_y. *Proof.* Hölder with the probability-like weights a_{by}/Σ_{y'}a_{by'}:
(Σ_ya_{by}t_y)^k ≤ (Σ_ya_{by})^{k-1}Σ_ya_{by}t_y^k ≤ N_0^{k-1}Σ_ya_{by}t_y^k (k = 1, 2, 3); sum over b and use the column bound. ∎
(s3 B: never violated in 400 random trials; linear ratio up to 0.79, cubic up to 3.2·10⁻².)

**Theorem CE-Q (band): analytic part PROVEN-HERE ⇐ Theorem CE (Step 1, and Steps 3-4 as a hard-core lemma), LOC-s′, QC, HULL,
SF-geo, CE-geo' (counted); as a statement about the stage-0 integral CONDITIONAL ⇐ (FP-loc)_0 + the background clause (after
§10.2, (SF-N♮) is proven).** [Post-proof precision, written with the proof: the shell structure is a function of Z, so no
separate label measure is needed; the "μ_1(good)^{|Λ|}" prefactor and the definition of Ĥ_0 are as below, which corrects the
garbled η̂ display of §9.1.]
*Constants.* T(ρ) := max{2S_T(4ρ/r_T)³/g_0², (N/9)ρ², 8K_𝔫c_yy_bgρ + 9K_𝔫c_y²ρ²} (the three term-type bounds; T(ρ') = h_0/(16M⁴n_*));
C_3 := 16384S_Tn_bN_0³N^{3/2}/r_T³, C_2 := (32/9)N²N_0² + 288K_𝔫c_y²n'_cN_0²N, C_1 := 64K_𝔫c_yy_bgn'_cN_0√N.
[RSF3-fix Q3: read these three as **C_3^Q, C_2^Q, C_1^Q** throughout §10.1 (Step 3, (B2)-(B3), a_*); the unadorned C_1 in Step 6
and in the "Statement as proven" is Theorem CE's prefactor 2κ_0B.]
*Step 0 (the field on the band; the chart).* For Z ∉ 𝔇 and real s = 1, |A_b| ≤ g_0√NΣ_ya_{by}|Z_y| ≤ g_0√NN_02^{j_max+1}p ≤ ρ_*
((B1′) below). So ||1 - e^{A_b}||_op ≤ e^{1/64} - 1 (ρ_* ≤ r_T/8 ≤ 1/64) < ε^thr_N for every b: **1_D ≡ 1 on supp μ_wn ∖ 𝔇** (this disposes of CE0-2/CQ-1's
non-local indicator on the band).
[Disclosure: Steps 1-6 were first written 04:34-04:36 UTC with three in-line post-proof corrections (the choice of κ̂, the
parametrisation of the rate in Steps 3-4, and the radius of U_α, whose first value R̄_α^{(5)} does not make the component structure
readable inside clusters). At 04:37-04:38 UTC they were rewritten into the clean form below; the three corrections are kept and marked
(c1)-(c3). No other change.]
*Step 1 (structure).* Fix Z ∉ 𝔇; Q := Q(Z), R := the cubes containing a site of Q. Two cubes of R are *R-linked* if their index distance
is ≤ 7; R̄_α are the R-linked components, Q_α := Q ∩ (sites of R̄_α), W_α := R̄_α^{(2)}, **U_α := R̄_α^{(7)} (c3)** (a polymer: boxes of
radius 7 around cubes at distance ≤ 7 overlap); |U_α| ≤ 15⁴|Q_α|, |U_α^+| ≤ 17⁴|Q_α|, d(U_α) ≤ 2(|U_α| - 1) ≤ 2·15⁴|Q_α| (spanning
tree of the touching graph, centre-to-centre segments of length ≤ 2 inside the two closed cubes). A term polymer X (d(X) = 0,
CE-exp^0) is **large** if X^+ ∩ R ≠ ∅, else **small**; a large X lies in W_α for exactly one α. *Readability:* whether a site is a
Q-site is read on that site; the R-linked class of a Q-site of R̄_α is decided by Z on R̄_α^{(7)} = U_α; whether X is large is decided
on X^+. So every structural fact used for a member below is read on that member's own set.
*Step 2 (localisation).* G_α := exp(Σ_{X large in W_α}H_X(g_0√N𝒞Z)). Apply LOC-s′ to G_α with "X^+" := U_α^+, radii r_y := e^{μδ(y,U_α)}
(good y) and r_y := 2^{-(j_y+1)}e^{μδ(y,U_α)} (y ∈ Q, y ∉ U_α^+): G_α = Σ_SG_{α,S}, G_{α,S} reading Z on U_α^+ ∪ S. On the refined domain,
at b ∈ W_α: own large sites (s = 1) give σ^α_b := g_0√NΣ_{y∈Q_α}a_{by}2^{j_y+1}p; good sites of U_α^+ give ≤ g_0√NpN_0 ≤ ρ'/2; large sites
of other components inside U_α^+ (s = 1) lie at index distance ≥ 8 - 2 = 6 from W_α, fine distance ≥ 5M + 1, and give ≤
g_0√N2^{j_max+1}pe^{-5μM}Σ_ya_{by}e^{μd(b,y)} ≤ ρ'/2 (2^{j_max+1} ≤ e^{μM} by (M-Q)); S-sites give ≤ g_0√NΣ_ya_{by}(1 + r_y)|Z_y| ≤
g_0√NΣ_ya_{by}2e^{μδ(y,U_α)}p ≤ ρ' (for y ∈ Q, (1 + r_y)2^{j_y+1} ≤ 2^{j_y+1} + e^{μδ} ≤ 2e^{μδ} since δ ≥ M + 1; δ(y, U_α) ≤ d(b, y));
all other sites are 0 (LOC-s′). So |A_b| ≤ 2ρ' + σ^α_b ≤ ρ_* by **(B1′) 2ρ' + g_0√NN_02^{j_max+1}p ≤ ρ_*** (replaces (B1)). Each small X:
LOC-s′ with the same radius rule relative to X; X^+ has no Q-site, so the field on X is ≤ ρ' (+ the far large sites, which enter only
through S); a Q-site in S costs r_y^{-1} = 2^{j_y+1}e^{-μδ(y,X)} ≤ e^{-μδ(y,X)/2} (μδ ≥ μM ≥ 2(j_y + 1)log 2 by (M-Q)) and a good one
e^{-μδ} ≤ e^{-μδ/2}. So the small pieces obey LOC-s's bound with μ/2 in place of μ, and CE-exp's Steps 1-2 (W(μ/2) ≤ w_8 by (M-W))
give H'(Y) := Σ_{(X,S): X small, Y(X,S)=Y}F_{X,S}, reading Z on Y, |H'(Y)| ≤ H'_0e^{-κ_cd(Y)} on supp μ_wn ∖ 𝔇.
*Step 3 (the cost of a large component).* On G_α's refined domain |log G_α| ≤ Σ_{τ in W_α}T_τ(2ρ' + σ^α_τ), σ^α_τ := max_{b∈P_τ}σ^α_b.
With (u + v)^k ≤ 2^{k-1}(u^k + v^k), max ≤ sum over the pattern, and Lemma QC for the own sites:
  baseline ≤ 4·8·#{terms in W_α}·T(ρ') ≤ 32|W_α|M⁴n_*T(ρ') = 2|W_α|h_0 ≤ 1250h_0|Q_α|  (|W_α| ≤ 5⁴|R̄_α| ≤ 625|Q_α|);
  cubic ≤ 4·128S_Tr_T^{-3}g_0^{-2}·n_bΣ_b(σ^α_b)³ ≤ 512S_Tn_br_T^{-3}g_0^{-2}·4N_0³Σ_{y∈Q_α}t_y³ = Σ_{y∈Q_α}C_3g_08^{j_y}p³;
  Jacobian ≤ (2N/9)Σ_b(σ^α_b)² ≤ (8N/9)N_0²Σ_yt_y²;  source ≤ Σ_c[8K_𝔫c_yy_bgσ^α_c + 18K_𝔫c_y²(σ^α_c)²] ≤ 4n'_cN_0Σ_y(8K_𝔫c_yy_bgt_y + 18K_𝔫c_y²N_0t_y²);
with t_y = g_0√N2^{j_y+1}p this is ≤ Σ_{y∈Q_α}c(j_y), c(j) := C_3g_08^jp³ + C_2g_0²4^jp² + C_1g_02^jp, and by (B2)-(B3) and 2^jp ≥ 1,
c(j) ≤ (3/16)4^jp² for 0 ≤ j ≤ j_max. So |G_{α,S}| ≤ Π_{y∈Q_α}e^{(3/16)4^{j_y}p² + 1250h_0}·Π_{y∈S}e^{-μδ(y,U_α)/2}.
*Step 4 (clusters).* Mayer-expand the small part (Theorem CE, Step 1): exp(Σ_YH'(Y)) = Σ_{disjoint {Z_i}}Π_iK(Z_i), K(Z) reading Z on Z,
|K(Z)| ≤ C_KH'_0e^{-κ_1d(Z)}, κ_1 := κ_c - κ_0 - 2 (a pointwise bound, valid on supp μ_wn ∖ 𝔇). Put Ŷ_{α,S} := Y(U_α, S) (Lemma HULL with
the polymer U_α: Ŷ ⊃ U_α^+, q(y) ∈ Ŷ for y ∈ S, d(Ŷ) ≤ 273d(U_α) + 272 + Σ_{y∈S}(2n(y,U_α) + 1)). Expanding Π_αΣ_S, the integrand on 𝔇^c
is a sum over choices ((S_α)_α, {Z_i}); in each choice the members Ŷ_{α,S_α}, Z_i form an overlap graph (the Z_i pairwise disjoint);
its connected components ("clusters") have pairwise disjoint unions 𝒵; every member reads Z only on its own set; two components
α, β whose U-collars meet a common Q-site are in the same cluster. Every Q-site lies in some U_α ⊂ Ŷ_α, so the sites outside all
clusters are good. By Step 1's readability,
  e^{ΣH}1_{𝔇^c} = Σ_{disjoint {𝒵_k}}Π_kΨ(𝒵_k)·Π_{y∉∪𝒵_k}1[|Z_y| ≤ p],
Ψ(𝒵) := Σ over connected member data with union 𝒵, the structure (Q ∩ 𝒵, its R-linked classes, which X are large) computed from Z on
𝒵, times 1_{𝔇^c} on 𝒵 and the indicator that every Q-site of 𝒵 is in a class whose U-collar lies in 𝒵. Ψ(𝒵) reads Z on 𝒵 only, and
μ_wn is a product over sites, so
  ∫_{𝔇^c}e^{ΣH}dμ_wn = μ_1(good)^{|Λ|}·P(z),  z(𝒵) := μ_1(good)^{-#sites(𝒵)}∫Ψ(𝒵)dμ_wn|_𝒵,
P the hard-core polynomial of Theorem CE's Step 2 (families of pairwise disjoint 𝒵).
*Step 5 (activity bounds).* Pure clusters (no Q-site): z(𝒵) = ∫K(𝒵)dν_∅, |z| ≤ C_KH'_0e^{-κ_1d(𝒵)}. Mixed clusters: **(c1) κ̂ := κ_1 - κ_0
= κ_c - 2κ_0 - 2.** Along a spanning tree of the member graph d(𝒵) ≤ Σ_md(m) + 2(n - 1) (CE-geo (g2)), so Π_me^{-κ̂d(m)} ≤
e^{-κ̂d(𝒵)}e^{-2κ̂}Π_me^{2κ̂}. K-members: e^{2κ̂}e^{κ̂d(Z)}|K(Z)| ≤ e^{2κ̂}C_KH'_0e^{-κ_0d(Z)}; the sum over disjoint families of subsets of 𝒵
is ≤ Π_{Z⊂𝒵}(1 + e^{2κ̂}C_KH'_0e^{-κ_0d(Z)}) ≤ exp(e^{2κ̂}C_KH'_0K_0|𝒵|) (CE-geo' (g5')). G-members: e^{κ̂d(Ŷ)}|G_{α,S}| ≤
e^{κ̂(546·15⁴|Q_α| + 272)}Π_{y∈Q_α}e^{(3/16)4^{j_y}p²+1250h_0}·Π_{y∈S}e^{κ̂(2n_y+1)}e^{-μMn_y/2} (δ > Mn_y); the S-sum is ≤ exp(|U_α^+|W̃),
W̃ := M⁴e^{κ̂}Σ_n(2n + 1)⁴e^{-(μM/2-2κ̂)n} ≤ w_8 by (M-W) (κ̂ < κ'). So Σ_Se^{2κ̂}e^{κ̂d(Ŷ_{α,S})}|G_{α,S}| ≤ e^{274κ̂}Π_{y∈Q_α}Γe^{(3/16)4^{j_y}p²+1250h_0},
**Γ := exp(546·15⁴κ̂ + 17⁴w_8)**; charge e^{274κ̂} to one Q-site of α (|components| ≤ |Q|). Integrating over the shells (SF-cut (b) at the
lower edge 2^jp; μ_1(good) ≥ ½ for p² ≥ 4(n log 2 + 2)), each Q-site carries ≤ Σ_{0≤j≤j_max}2·2^{n/2}e^{-4^jp²/4}e^{(3/16)4^jp²}Γe^{1250h_0}
≤ 4Γe^{1250h_0}2^{n/2}e^{-p²/16} =: η (s3 D4 checks the shell sum); put η̂ := e^{274κ̂}η. Summing over non-empty Q ⊂ sites(𝒵)
(M⁴|𝒵| sites): Π(1 + η̂) - 1 ≤ M⁴|𝒵|η̂e^{M⁴|𝒵|η̂}. With |𝒵| ≤ 16(1 + d(𝒵)) ≤ 16e^{d(𝒵)} and c_* := e^{2κ̂}C_KH'_0K_0 + M⁴η̂ ≤ 1/16:
  |z(𝒵)| ≤ e^{-κ̂d(𝒵)}·e^{c_*·16(1+d)}·16e^{d}M⁴η̂ ≤ 16eM⁴η̂·e^{-(κ̂-2)d(𝒵)}.
*Step 6 (hard-core expansion).* Theorem CE's Steps 3-4 use the activities only through |z_Y| ≤ C_KH_0e^{-κ_1(κ)d(Y)} (κ_1(κ) := κ - κ_0 - 2)
on the closed polydisc ("𝓗 converges absolutely and uniformly on the closed polydisc 𝔻", Step 3; "uniformly on 𝔻", Step 4), with
κ > 3κ_0 + 3 and the third condition on H_0. **(c2)** Both cluster types obey |z| ≤ C_KĤ_0e^{-(κ_c-2κ_0-4)d} (κ_1 ≥ κ̂ - 2 = κ_c - 2κ_0 - 4),
Ĥ_0 := max{H'_0, 16eM⁴η̂/C_K}. Apply Steps 3-4 with κ := κ_c - κ_0 - 2 (so κ_1(κ) = κ_c - 2κ_0 - 4): P(z) = exp(Σ_𝒵𝓗_𝒵),
|𝓗_𝒵| ≤ C_1Ĥ_0e^{-(κ_c-4κ_0-5)d(𝒵)}, 𝓗_𝒵 depending on z(𝒵'), 𝒵' ⊂ 𝒵, hence on Z on 𝒵. ∎
[RSF3-fix Q2: z(𝒵) is the SUM of its pure part (configurations with Q ∩ 𝒵 = ∅) and its mixed part, so |z(𝒵)| ≤ C_KH'_0e^{-κ_1d} +
16eM⁴η̂e^{-(κ̂-2)d} ≤ 2C_KĤ_0e^{-(κ_c-2κ_0-4)d}: read **Ĥ_0 := 2max{H'_0, 16eM⁴η̂/C_K}** in Step 6 and below (harmless).
RSF3-fix Q1: Step 4's pointwise Mayer expansion of the small part is Theorem CE's Step 1 at rate κ_c and needs **H'_0 ≤ log 2 and
H'_0 ≤ (32K_0)^{-1}e^{-2(κ_c-κ_0)}**, i.e. H'_0 ≤ c_0(κ_c)'s first two entries; neither Ĥ_0 ≤ c_0(κ_c - κ_0 - 2) (weaker by e^{2κ_0+4}
in the second entry) nor c_* ≤ 1/16 implies it. It is added to the statement below.]
**Statement as proven (replaces §9.1's constants).** Under (FP-loc)_0, the background clause (gauge logs ≤ min{r_T/4, α_𝔫} on every
pattern), (B1′), (B2)-(B3) [with p ≥ 2, RSF3-fix Q5], (M-Q), (M-W), κ_c > 4κ_0 + 5, c_* ≤ 1/16, **H'_0 ≤ c_0(κ_c) [RSF3-fix Q1]** and
Ĥ_0 ≤ c_0(κ_c - κ_0 - 2) [Ĥ_0 with the factor 2 of RSF3-fix Q2]:
  **∫_{𝔇^c}exp(Σ_XH_X(g_0√N𝒞Z))dμ_wn = μ_1(good)^{|Λ|}exp(Σ_𝒵𝓗_𝒵),  |𝓗_𝒵| ≤ C_1Ĥ_0e^{-(κ_c-4κ_0-5)d(𝒵)}.**
The rate is CE-exp^0's κ_c - 3κ_0 - 3 minus (κ_0 + 2) (one more Mayer layer): the same decay up to an additive constant, not the
identical number. Every smallness condition is met for g_0 small at fixed p ≥ p_0 (η̂M⁴ ≤ 1/32 fixes p_0, depending on M only through
log M), since h_0, H'_0 = O(g_0M⁴p³) and 2^{j_max} ≳ 1/(g_0p); (M-Q) then needs M ≳ 2log_2(1/(g_0p))log 2/μ, logarithmic in 1/g_0.
**[RSF3-fix (route note): this theorem is built on Theorem CE, Theorem CE-exp and Lemma HULL, i.e. on the 273-loss route (the
546 = 2·273 in Γ, the e^{272κ'} in H'_0). It cannot be iterated across levels (REVIEW_SF_S3 D-4). Its (M-Q) makes M g-dependent.
Both defects are removed in Theorem CE-Q-col (§12.1 pre-stated, §13.1 proven), which supersedes this theorem for every use beyond
stage 0.]**

**(CE-Q^∞): OPEN (named; the exact wall).** 𝔇's mass: μ_wn(𝔇) ≤ |Λ|2^{n/2}e^{-4^{j_max+1}p²/4} and, from the definition of j_max,
2^{j_max+1} ≥ min{1/(16C_3g_0p), ρ_*/(4√NN_0g_0p)} (the floor costs one factor 2; (B1′) with ρ' ≤ ρ_*/4), so 4^{j_max+1}p² ≥ a_*/g_0² with a_* :=
min{(16C_3)^{-2}, (ρ_*/(4√NN_0))²} [C_3 = C_3^Q, RSF3-fix Q3]. On 𝔇 the field |A_b| at real s may exceed ρ_* [RSF3-fix Q6: the
garbled "some field |A_b| ≥ ... can exceed ρ_*" replaced]: the activities leave their analyticity polydisc, the
chart indicator may vanish, and the integrand is the Haar integrand, not a Gaussian one. A Z-local bound would need a local
coercivity of the true action (S(e^AU) - S(U) ≥ δ·(Hessian quadratic) on the chart, localised), which is not available; the
pricing is in U-variables (RLARGE §3.2 branch (ii)). **Status of (CE-Q) after session 3:** the band part is PROVEN (Theorem CE-Q,
conditional only on CE-exp^0's hypotheses); the deep part is (CE-Q^∞), of μ_wn-weight ≤ |Λ|2^{n/2}e^{-a_*/(4g_0²)}, OPEN.
[RSF3-fix C-2: "μ_wn-weight" means μ_wn-MASS of 𝔇, not the contribution of 𝔇 to the integral; the pricing sentence above
("in U-variables, RLARGE §3.2 branch (ii)") is withdrawn as stated (circular, Part C 5); restated in §12.2/§13.2.]
*Cost recorded:* (M-Q) makes M grow like log(1/g_0)/μ (2^{j_max} ∝ 1/(g_0p)); every smallness condition carries M⁴ only
polynomially (h_0 ∝ g_0M⁴p³), so g_0M⁴p³ → 0 still holds, but M is no longer g-independent. [RSF3-fix: superseded by CE-Q-col
(§13.1), where (M-Q) is dropped and M is g-independent.]

### 10.2 STEP 3: Lemma SF-N♮

**Lemma SF-N♮: PROVEN-HERE (not counted).** *Proof.* (1) *Gauge.* For a real gauge h, |log(h S⁻¹T_j h⁻¹)| = |log(S⁻¹T_j)| (log commutes
with unitary conjugation; |·| unitarily invariant), and (h·e^AU)_b = e^{Ad_{h}A_b}(hU)_b with |Ad_hA_b| = |A_b|; so work in the gauge with
link logs ≤ α_𝔫. (2) *Loop factorisation.* S⁻¹T_j = Π_{i=1}^ℓF_i with ℓ ≤ L + p_L ≤ 2p_L factors F_i = U_{b_i}^{ε_i}. Replace U_b by e^{A_b}U_b.
With P_i := F_1⋯F_i (real, unitary): e^{A}U appended to P_i gives e^{Ad_{P_i}A}P_iU, and (e^AU)⁻¹ = U⁻¹e^{-A} gives e^{-Ad_{P_iU⁻¹}A}P_iU⁻¹;
by induction the perturbed loop is E·Λ_j, Λ_j := S⁻¹T_j, E := e^{Ã_1}⋯e^{Ã_ℓ}, |Ã_i| = |A_{b_i}| ≤ a. (3) *Bounds.* For a submultiplicative norm,
|Π_i(1 + W_i) - 1| ≤ Π_i(1 + |W_i|) - 1 (expand; no identity term survives), so with W_i := e^{Ã_i} - 1, |W_i| ≤ e^{a} - 1: |E - 1| ≤ e^{ℓa} - 1.
At a = 0 and links e^{X_b}, |X_b| ≤ α_𝔫, the same argument (Λ_j itself is a product of ℓ factors e^{±X}) gives |Λ_j - 1| ≤ e^{ℓα_𝔫} - 1 and,
by (4) with Y = 0, y_bg = |log Λ_j| ≤ 1.04ℓα_𝔫 ≤ 2.2p_Lα_𝔫 = c_yr_𝔫 (α_𝔫 = r_𝔫). (4) *Log.* log(1 + W) := Σ_k(-1)^{k+1}W^k/k is holomorphic on
|W| < 1 with ||D log(1 + W)|| ≤ Σ_k|W|^{k-1} = 1/(1 - |W|) (||D(W^k)|| ≤ k|W|^{k-1}). Put W_0 := Λ_j - 1, W' := EΛ_j - 1; then W' - W_0 =
(E - 1)Λ_j, |W' - W_0| ≤ |E - 1| (|BΛ| ≤ |B| for unitary Λ, both norms), and the segment [W_0, W'] lies in the ball of radius w :=
|W_0| + |E - 1|. With y_bg ≤ c_yr_𝔫 = y_♭/3 ≤ 1/120 and ℓa ≤ 2p_L·2r_𝔫 = 4y_♭/(6.6) ≤ 0.0152: |W_0| ≤ e^{1/120} - 1 ≤ 0.00837, |E - 1| ≤
e^{0.0152} - 1 ≤ 0.0154, w ≤ 0.0238, so |log(EΛ_j) - log Λ_j| ≤ |E - 1|/(1 - w) ≤ ℓa·e^{0.0152}/0.9762 ≤ 1.04ℓa ≤ 2.08p_La ≤ c_ya.
[RSF3-fix SN-1: the rounded chain "ℓa·e^{0.0152}/0.9762 ≤ 1.04ℓa" is false as printed (1.0400**3**). With the unrounded values
ℓa ≤ 4/(40·6.6) = 0.0151515…, |W_0| ≤ e^{1/120} - 1 = 0.0083682…, w ≤ 0.0083682 + (e^{0.0151515} - 1) = 0.0236350…, and
|E - 1| ≤ ℓa·e^{ℓa}: |E - 1|/(1 - w) ≤ ℓa·e^{0.0151515}/0.9763650 = **1.03984ℓa ≤ 1.04ℓa** (s4 C6). The lemma stands as stated.]
(For the a = 0 case in (3) replace (E, Λ_j) by (Λ_j, 1).) Hence y(e^AU) ≤ y_bg + c_ya ≤ y_♭/3 + 2y_♭/3 = y_♭ ≤ 1/40 < 1/20: e^AU ∈ D_c(y_♭).
(5) *NORM-an's hypotheses there.* θ = 18.4y²(2 + 2c_N) ≤ 18.4(2 + 2c_N)y_♭² ≤ ½·(1/max(1, C_N)) by the choice of y_♭; so θ ≤ ½ and C_Nθ ≤ ½.
NORM-an (ii) also needs κu ≥ ½ (u = u_0 ≥ 1/(2κ)), a coupling condition, unchanged. ∎ (s3 C: SU(2), SU(3), 22-factor loops, 2400
samples: y - y_bg ≤ 0.909c_ya (= ℓa/(c_ya) at the aligned samples, which attain y - y_bg = ℓa exactly); y_bg ≤ 2.2p_Lα always.)
*Consequences (applied).* SF-src holds as proven with ρ ≤ r_𝔫/2, and its closed disc |ζ| ≤ R ≤ r_𝔫 lies inside the holomorphy disc
|ζ| < 2r_𝔫 (Fix src-1 discharged). **CE-exp^0, SF-A2^0 and Theorem CE-Q: CONDITIONAL ⇐ (FP-loc)_0** (with the background clause
"gauge logs ≤ α_𝔫 on every coarse link's contour pattern", a smallness condition met by BR1 backgrounds at small curvature via
Lemma AX, 10p_Lℓε' ≤ α_𝔫 [as in SF-T0's closing remark]). The 1/u_0 expansion of (SF-N) (ii) is used by no statement of SF and stays a
note.

### 10.3 STEP 4: Theorem CE-col

**Lemma GEO-col: PROVEN-HERE (not counted).** (a) A connected union of segments of length ℓ meeting every closed cube of c meets ≥ |c|
cubes, and CE-geo' (g1') bounds the number it meets by 16(1 + ℓ) (its proof uses only connectedness and length). (b) Take near-optimal
trees τ_i ⊂ ∪c_i^+ meeting every cube of c_i. For an edge {i, j}: a cube Q ∈ c_i^+ ∩ c_j^+ touches some a ∈ c_i and b' ∈ c_j; join a point
of τ_i ∩ a to a point of a ∩ Q, then to a point of Q ∩ b', then to a point of b' ∩ τ_j, by three segments inside the convex closed cubes
a, Q, b' (length ≤ 2 each). The union is connected, lies in ∪(∪c_i)^+, meets every cube of ∪c_i; length ≤ Σ(d^+(c_i) + η) + 6(n - 1).
d^+(X) ≤ d(X) since ∪X ⊂ ∪X^+. (c) If c^+ is connected then c is 2-connected (two cubes of c whose collars share a cube are at index
distance ≤ 2), and conversely the cores arising below are 2-connected by construction. The graph "index distance ≤ 2" has degree
≤ 5⁴ - 1 = 624; a depth-first closed walk of length 2(m - 1) determines a 2-connected set of m cubes containing □: ≤ 624^{2(m-1)}
of them; so Σ_{c∋□}e^{-a'|c|} ≤ e^{-a'}Σ_{m≥0}(624²e^{-a'})^m = 2e^{-a'} = 1/624², and by (a) e^{-κ̃_0d^+(c)} ≤ e^{κ̃_0}e^{-a'|c|}. (d) A cube
Q ∈ c^+ ∩ Z^+ touches a ∈ c and z ∈ Z, so a is within index distance 2 of z. |Z^{(2)}| ≤ 5⁴|Z|. (e) "≤": a polymer Y' ⊂ c^+ ⊃ c has trees
in ∪Y' ⊂ ∪c^+ meeting all of Y' ⊃ c. "≥": for a tree τ ⊂ ∪c^+ meeting all cubes of c, Y' := the cubes of c^+ whose closed cube meets τ
contains c, is *-connected (closed cubes meeting the connected τ ⊂ ∪Y'), and τ meets every cube of Y' and lies in ∪Y'. ∎

**Theorem CE-col: PROVEN-HERE ⇐ Theorem CE's proof re-run, Lemma TG, CE-geo' (counted).** *Proof.* Step 1 (Mayer, collar linking).
Π_X(1 + f_X), f_X := e^{H(X)} - 1. Call X, X' linked if X^+ ∩ X'^+ ≠ ∅. Grouping a collection of distinct polymers by linked-connected
components gives Π_X(1 + f_X) = Σ_{families of cores {c_j}, pairwise c_i^+ ∩ c_j^+ = ∅}Π_jK(c_j), K(c) := Σ_n(1/n!)Σ_{distinct, linked-connected
(X_1..X_n), ∪X_i = c}Πf_{X_i} (unique decomposition; (∪X_i)^+ = ∪X_i^+, so different components have disjoint supports). K(c) reads Φ on
c^+. With κ' := κ - κ_0 and GEO-col (b) (d^+(X_i) ≤ d(X_i)): Π_ie^{-κd(X_i)} ≤ e^{-κ'(d^+(c) - 6(n-1))}Π_ie^{-κ_0d(X_i)}; drop every constraint
but X_i ⊂ c and use (g5'): |K(c)| ≤ e^{-κ'd^+(c)}e^{-6κ'}(e^u - 1) ≤ e^{-κ'd^+(c)}2H_0K_0|c|e^u, u := 2H_0K_0e^{6κ'}|c|. The second condition
on H_0 gives u ≤ |c|/16 ≤ 1 + d^+(c) (GEO-col (a)); so |K(c)| ≤ C_KH_0e^{-κ_1d^+(c)}, κ_1 := κ - κ_0 - 2, C_K = 32eK_0, as in [S11].
Step 2. Disjoint supports carry independent fields: Ξ = P(K#), P(z) := Σ_{families with pairwise disjoint supports}Πz_c.
Step 3. The exponential-formula identity exp(𝓗) = P of Theorem CE's Step 3 holds for any symmetric, reflexive incompatibility
relation (the ζ-product expansion, the grouping into connected components of the incompatibility graph and the exponential formula
use nothing else); here incompatibility is c^+ ∩ c'^+ ≠ ∅, and ρ^T is that graph's (Lemma TG, a statement about any connected graph).
Step 4. As in Theorem CE with three changes: (g2) → GEO-col (b) (constant 6), the relaxed constraint c_j ∩ c_{p(j)} ≠ ∅ → c_j^+ ∩ c_{p(j)}^+ ≠ ∅,
whose sum is over c_j meeting c_{p(j)}^{(2)} (GEO-col (d)), and (g4')-(g5') → GEO-col (a), (c). With κ_3 := κ_1 - 2κ̃_0:
Π_ie^{-κ_1d^+(c_i)} ≤ e^{-κ_3(d^+(Y) - 6(n-1))}Π_ie^{-2κ̃_0d^+(c_i)}; leaves inwards, Σ_{c: c ∩ Z^{(2)} ≠ ∅}e^{-2κ̃_0d^+(c)}|c|^m ≤
m!e^{κ̃_0}Σe^{-κ̃_0d^+(c)} ≤ m!e^{κ̃_0}K̃_0·625|Z| (|c| ≤ 16(1 + d^+) ≤ κ̃_0(1 + d^+)); the root gives ≤ d_1!e^{κ̃_0}K̃_0|Y|. With Cayley's degree
formula as in Theorem CE: (1/n!)Σ|ρ^T|Πr_{c_i} ≤ κ̃_0B̃H_0(4B̃H_0e^{6κ_3})^{n-1}e^{-(κ_3-1)d^+(Y)} (|Y| ≤ κ̃_0e^{d^+(Y)}); n = 1 likewise.
The third condition on H_0 is 4B̃H_0e^{6κ_3} ≤ ½; summing over n, |H#(Y)| ≤ 2κ̃_0B̃H_0e^{-(κ_3-1)d^+(Y)}, κ_3 - 1 = κ - κ_0 - 2κ̃_0 - 3 > 0 by
hypothesis. H#(Y) involves K#(c_i), c_i ⊂ Y, hence H(X) with X ⊂ Y, and it vanishes unless the incompatibility graph is connected,
i.e. unless Y is 2-connected; it reads Φ on Y^+. *Re-indexing.* By GEO-col (e) choose for each Y a polymer Y'(Y), Y ⊂ Y' ⊂ Y^+, with
d(Y') ≤ d^+(Y) + 1; at most 2^{|Y'|} ≤ 2^{16(1+d(Y'))} sets Y map to one Y' (Y ⊂ Y' ⊂ Y^+ ⊂ Y'^+ … Y ⊂ Y'); so
Σ_{Y: Y'(Y)=Y'}|H#(Y)| ≤ 2^{16}e^{r}C̃_1H_0e^{-(r - 16 log 2)d(Y')}, r := κ - κ_0 - 2κ̃_0 - 3, and the re-indexed activity reads Φ on Y'^+. ∎
*What changed against CE^+.* The collar enters the LINKING (constant 6 per edge, 625 per neighbourhood), never the size: d^+ is measured
on the cores and no d(X^+) appears. The 1/273 and e^{272κ'} of SF-geo are gone.

**Corollary CE-exp-col: PROVEN-HERE (not counted).** *Proof.* Lemma LOC-s as before; collar-free hull Y_0(X, S): for y ∈ S let Q'_y be a
cube of X at index distance n(y, X) + 1 from q(y) (Lemma LOC-s (4)), σ_y the centre-to-centre segment (length ≤ 2(n_y + 1)), γ_y ⊂ Q'_y to a
point of a near-optimal tree of X (length ≤ 1); Y_0 := X ∪ {cubes met by some σ_y}: a polymer containing q(y), d(Y_0) ≤ d(X) + Σ_y(2n_y + 3)
(HULL's argument with X in place of X^+). F_{X,S} reads ∪X^+ ∪ S ⊂ ∪Y_0^+. Regroup H''(Y_0) := Σ_{Y_0(X,S)=Y_0}F_{X,S} (reads Y_0^+). As in
CE-exp Step 2: e^{κ'd(Y_0)}|H''(Y_0)| ≤ h_0Σ_{X⊂Y_0}e^{-(κ-κ')d(X)}Π_{y}(1 + e^{κ'(2n_y+3)}e^{-μMn_y}) ≤ h_0Σ_{X⊂Y_0}e^{-(κ-κ'-1296W_3)d(X)}e^{1296W_3}
(Σ_yw_y ≤ |X^+|W_3, |X^+| ≤ 1296(1 + d(X)), e^{κ'(2n+3)} ≤ e^{3κ'}e^{2κ'n}); with κ ≥ κ' + 1296W_3 and 2^{|Y_0|} ≤ 2^{16}e^{16 log 2·d(Y_0)}:
|H''(Y_0)| ≤ H''_0e^{-κ_cd(Y_0)}. Theorem CE-col applies (H'' depends on the field on Y_0^+). Sufficient condition: as in CE-exp, with
e^{3κ'} in place of e^{κ'}: μM - 2κ' ≥ 3κ' + 4 log M + 8 ⇒ W_3 ≤ w_8. ∎ The input requirement is κ ≥ κ_c + 16 log 2 + 1296W_3
(≈ κ_c + 46.4), against 273κ' + 1296W (≈ 1.28·10⁵) for CE-exp; H''_0 has no e^{272κ'}.

**Proposition RATE: PROVEN-HERE (arithmetic; not counted).** Feed CE-exp-col's output (rate r = κ_c - κ_0 - 2κ̃_0 - 3 in d^+), re-indexed
(rate r - 16 log 2 in d), into SF-blk (rate L(κ - κ_0) - 1 for input κ ≥ κ_0): the next stage's input rate is 3(κ_c - 2κ_0 - 2κ̃_0 - 3 -
16 log 2) - 1, and the next CE-exp-col needs κ_c + 16 log 2 + 1296W_3. With W_3 ≤ w_8 this holds iff κ_c ≥ κ_c^* = 1149.92 (s3 D2). The
273 route: 3(κ_c - 4κ_0 - 3) - 1 < 273(κ_c + 16 log 2) + 1296w_8 for every κ_c ≥ 3κ_0 + 3 (s3 D3; algebraically, the left side
grows with slope 3 and the right with slope 273, and it already holds at κ_c = 3κ_0 + 3). ∎ **So (CE-col) is PROVEN in the rate
sense:** the decay rate survives iteration at L = 3. (Bookkeeping of rates only: that the blocked inherited activities are again (H-exp) inputs of the next
stage, i.e. holomorphic in the next stage's site scalings with the stated bounds, is item (iv) of CE-exp^k and is not shown here.) *Not given:* the norm reproduction of the small polymers (d < 1), which SF-blk
does not contract and which stays (SF-irr); and the norm of the d ≥ 1 part is reproduced by SF-blk only if C̃_1H''_02^{16}e^{r}·16L⁴K_0
e^{-(κ(L-1)-κ_0L-1)} ≤ (next input norm), a condition on c̃_0 that is not checked here.
[RSF3-fix RT-1: "decay rate survives" above means the RATE only. The d ≥ 1 NORM, re-derived in §13.3 (s4 C3-C4): in the displayed
same-rate form it closes from κ_c ≥ 1853.49 (REVIEW_SF_S3's ≈ 1854 reproduced); measured in the next stage's input class (rate
κ_c + 16 log 2 + 1296W_3, the iteration condition) from κ_c ≥ 2499.39. d < 1 is (SF-irr).] [RSF4-fix RT-1 citations: the
iteration thresholds are **2499.39 (CE-col) / 2938.18 (CE-Q-col)**; 1853.49 (≈ 1854) is the same-rate form only and is not to be
cited as an iteration threshold (REVIEW_SF_S4 B-6, fix 8).]

## 11. Session-3 outcome (written after §10)

### 11.1 Status changes
| item | status | note |
|---|---|---|
| Lemma LOC-s′ | PROVEN-HERE (not counted) | refined Cauchy domain; s3 A edge test |
| Lemma QC | PROVEN-HERE (not counted) | Hölder with ℓ¹ row/column norms; s3 B |
| **Theorem CE-Q (band)** | analytic part **PROVEN-HERE (counted)**; CONDITIONAL ⇐ (FP-loc)_0 as a statement on the stage-0 integral | rate κ_c - 4κ_0 - 5; M ∝ log(1/g_0) [RSF3-fix: + Fixes Q1, Q2; 273 route, not iterable; + (BGC); superseded by CE-Q-col §13.1] |
| (CE-Q^∞) | **OPEN, new name** | deep shells, weight ≤ \|Λ\|2^{n/2}e^{-a_*/(4g_0²)}; U-variable pricing [RSF3-fix C-2: μ_wn-MASS, not contribution; the branch-(ii) handoff withdrawn; restated §12.2/§13.2] |
| **Lemma SF-N♮** | **PROVEN-HERE** (not counted); (SF-N♮) discharged | c_y = 2.2p_L; s3 C |
| CE-exp^0, SF-A2^0 | CONDITIONAL ⇐ (FP-loc)_0 (+ background clause α_𝔫) [RSF3-fix SN-2: + (BGC), an explicit hypothesis] | was ⇐ (FP-loc)_0 + (SF-N♮) |
| Lemma GEO-col | PROVEN-HERE (not counted) | |
| **Theorem CE-col** | **PROVEN-HERE (counted)** | (CE-col) discharged in the rate sense |
| Corollary CE-exp-col | PROVEN-HERE (not counted) | no e^{272κ'}; input κ ≥ κ_c + 46.4 |
| Proposition RATE | PROVEN-HERE (arithmetic; not counted) | κ_c^* = 1149.9 at L = 3 [RSF3-fix RT-1: rate only; d ≥ 1 norm from 2499.4, §13.3] |
| CE-exp^k | CONDITIONAL ⇐ N_μ(\|𝒞_k\|), **(L-loc)_k**, (FP-loc)_k, (N5-reg)_k, criticality, inherited activities; composition via CE-exp-col | (L-hol)_k NOT VIABLE AS STATED |
| SF-thr-k | CONDITIONAL ⇐ (N5-unif) ⇐ (H-K) + (H-C⁺) + (H-ℂ) | PROOF [S22] |
| (MIN-reg) | lane D | re-homed |
| (G♯-patch) | OPEN, precisely stated; = the B-NA wall | GPa-1 |

**Tally of this file after session 3:** PROVEN-HERE 26 + 1 standard: counted 9 (SF-J, SF-T0, SF-DC, CE^+, SF-blk, LOC-s, CE-exp, CE-Q
(analytic part), CE-col); not counted 17 (SF-thr, SF-cut, SF-N0, SF-WN, SF-geo, SF-V, SF-J', SF-src, HULL, CE-exp-𝒞, BS, G-pert, U-red,
LOC-s′, QC, SF-N♮, GEO-col) + CE-exp-col and RATE (corollary/arithmetic, listed but not added to the count). CONDITIONAL 5 (SF-thr-k,
SF-A2^0, CE-exp^0, CE-exp^k, CE-Q as a statement on the integral). ARGUED 2 ((CE-s), SF-A3^0's deep part now = (CE-Q^∞)).
[RSF3-fix tally (Part F): **ARGUED 1** ((CE-s)). SF-A3^0's Q ≠ ∅ part is band = CE-Q (CONDITIONAL) + deep = (CE-Q^∞) (OPEN), and is
not ARGUED; it is not listed twice. CE-Q is counted only with Fix Q1. CONDITIONAL items cite (FP-loc)_0 + (BGC).] OPEN names:
(FP-loc)_k, (N5-reg)_k, (L-loc)_k, (CE-Q^∞), (a5-G♯)/(G♯-patch) [B-NA], (R♯) at ψ^r [B-NA], (SF-irr) and the A4 items; lane D: (MIN-reg),
(a5-U), (a3-q). Discharged this session: (SF-N♮), (CE-col) (rate). No RLARGE §4.2 row is discharged; no PROOF.md tally change proposed.

### 11.2 What (SF^J)_0 now rests on
Stage 0: A1 PROVEN (BR1/NAH1); A2 ⇐ (FP-loc)_0; A3 cut-good + band ⇐ (FP-loc)_0 (CE-exp^0, CE-Q); A3 deep shells ⇐ (CE-Q^∞) (U-variable
large field, weight e^{-O(1/g_0²)} per site) [RSF3-fix SN-2, C-2: every "⇐ (FP-loc)_0" here is "⇐ (FP-loc)_0 + (BGC)"; "weight
e^{-O(1/g_0²)} per site" is the μ_wn-MASS per deep site, not a contribution bound; see §13.2]; A4 large polymers PROVEN (SF-blk), small ⇐ (SF-irr). Across levels the cluster expansion
now composes in rate (CE-col); the k ≥ 1 activity input is (L-loc)_k (B-NA wall).

### 11.3 Check s3 (criteria checks/s3_criteria.md 04:29:22 UTC, md5 0fdc251a…, before the script; script checks/s3_sf.py; output
checks/s3_out.txt; record checks/s3_time.txt). One run under the numeric lock 04:33:31-04:33:35 UTC (load 3.34; nice 10; BLAS threads 1;
3.3 s; peak RSS 80 MB). **OVERALL PASS 13/13.** Evidential: A1-A3, B1-B3, C1-C3 (9); arithmetic: D1-D4 (4). [RSF3-fix check design
(Part E): LOW-POWER, recorded as such: A3 (automatic once ρ_S saturates S), B1-B2 (Hölder's inequality, a theorem), C3 (ratio 1 by the
commuting construction: sharpness, not correctness); A1 has slack ≈ 10⁴, so it is not an edge test. Informative: A1 (weakly), C1, C2.] Margins: A2's
non-vacuity 1.08·10⁻⁴ against the 10⁻⁴ threshold (thin: the Cauchy bound with a 10⁻³ pole margin is loose by ≈ 10⁴); C1's worst
ratio 0.909 = ℓ/c_y (the aligned loops attain ℓa exactly, so c_y has 10% slack); B3 0.787 / 3.2·10⁻².

---

# SESSION 4 (2026-10-28 UTC). Inputs read before 05:14 UTC: REVIEW_SF_S3.md (BINDING; in full; md5 fbf4d6d6…), SF.md (63503687…,
= SF_LOG's session-3 final), SF_LOG.md (464a785c…), PROOF.md 4a7bbccc… (Theorem CE + Lemmas CE-geo, TG l.1857-1960; CE-geo' + new
constants l.2264-2295; Proposition NA-FP l.3040-3075 (h_U, M_U, Λ := {λ : λ(c_X) = 0}, Λ_res^U, χ_U); Setting N5-bg l.5255-5275),
RLARGE.md 24a73553… (§3.1-§3.4 l.290-380, branch (ii) l.310-331, branch (iii) inputs l.345-360). STEP-1 fixes were applied in place
05:14-05:19 UTC, each tagged [RSF3-fix] (RT-1's numbers are written after s4 ran; see §13.3).

## 12. Pre-stated targets, session 4 (appended at 05:20 UTC, 2026-10-28, BEFORE any session-4 proof and before the s4 criteria)

### 12.1 STEP 2: Theorem CE-Q-col (shell-dependent halos; the CE-col route)
*Idea fixed before writing (exploratory, unwritten):* (i) replace (M-Q) by a halo whose cube radius grows with the shell index,
ℓ_j ≍ 1 + 4(j + 1)log 2/(μM), so every far-site Cauchy cost 2^{j+1}e^{-μδ} ≤ e^{-μδ/2} holds by geometry, not by a g-dependent M;
(ii) the extra polymer cost per shell-j site is e^{O(κ̂ℓ_j⁴)}, beaten by the shell's Gaussian e^{-4^jp²/16} uniformly in j; (iii) run
the small pieces through CE-exp-col (collar-free hull Y_0, no 273), the Mayer step through CE-col Step 1 (collar linking, 2-connected
cores), the large components through the collar-free hull Y_0(U_α, S), and the final hard-core step through CE-col Steps 3-4. The
member-linking constant 6 (GEO-col (b)) replaces 2, and the K-members need e^{-κ̃_0d^+} (2-connected cores), so the extra rate loss
over CE-exp-col is κ̃_0 + 2, not κ_0 + 2.

**Setting CE-Q-col.** Setting CE-col and Corollary CE-exp-col's setting at stage 0 (𝒞 := 𝒞(U(V), V), μ := m_1, ρ' := 2g_0√NpN_μ(|𝒞|),
h_0, n_* as in CE-exp^0), CE cubes of fine side M with **(M-W3) (μ/2)M ≥ 5κ' + 4 log M + 8** (κ' := κ_c + 16 log 2) and M ≥ 2L + 1.
Shells j_y, Q, the band j_y ≤ j_max with (B1′), (B2), (B3) (p ≥ 2; constants C_1^Q, C_2^Q, C_3^Q) and 𝔇 as in §9.1/§10.1.
**Halo:** ℓ_j := ⌈4(j + 1)log 2/(μM)⌉ (≥ 1), H_y := the cubes at ℓ^∞ index distance ≤ ℓ_{j_y} - 1 from q(y) (y ∈ Q), R := ∪_{y∈Q}H_y.
R-linking at index distance ≤ 7, classes R̄_α, Q_α := {y ∈ Q : H_y ⊂ R̄_α}, W_α := R̄_α^{(2)}, U_α := R̄_α^{(7)}. A term polymer X is
large iff X^+ ∩ R ≠ ∅. κ̂ := κ_c - κ_0 - κ̃_0 - 2. Γ_j := exp(2κ̂(2ℓ_j + 13)⁴ + w_8(2ℓ_j + 15)⁴ + 2h_0(2ℓ_j + 3)⁴).
- **Lemma HALO (geometry).** (a) X small, y ∈ Q: n(y, X) ≥ ℓ_{j_y}. (b) y ∈ Q_β, β ≠ α, y ∉ ∪U_α^+: n(y, U_α) ≥ max{1, ℓ_{j_y} - 1} ≥ ℓ_{j_y}/2.
  (c) y ∈ Q_β, β ≠ α, q(y) ∈ U_α^+: index distance(q(y), W_α) ≥ ℓ_{j_y} + 5. (d) |W_α| ≤ Σ_{y∈Q_α}(2ℓ_{j_y} + 3)⁴, |U_α| ≤ Σ(2ℓ_{j_y} + 13)⁴,
  |U_α^+| ≤ Σ(2ℓ_{j_y} + 15)⁴; U_α is a polymer with d(U_α) ≤ 2(|U_α| - 1). (e) A large X lies in W_α for exactly one α. (f) In (a)-(c),
  μ·(fine distance) ≥ 2(j_y + 1)log 2, so 2^{j_y+1}e^{-μδ} ≤ e^{-μδ/2}. *Planned: PROVEN-HERE (not counted).* *Expected failure mode if
  mis-derived:* with 2 log 2 in place of 4 log 2 in ℓ_j, (b) gives only n ≥ ℓ_j - 1 and the cost fails by one cube (s4 A's negative
  control).
- **Lemma SH (shell-collar cost).** Under (M-W3), κ' ≥ 470, h_0 ≤ 1 and p ≥ 2: Γ_je^{-4^jp²/16} ≤ Γ_0e^{-p²/16}e^{-(4^j-1)p²/32} for
  every j ≥ 0, hence Σ_{j≥0}Γ_je^{-4^jp²/16} ≤ 2Γ_0e^{-p²/16}, uniformly in the upper limit (j_max or ∞). *Planned: PROVEN-HERE (not
  counted).*
- **Theorem CE-Q-col (band, collar-native, M g-independent).** Assume (FP-loc)_0 + (BGC), (B1′), (B2), (B3) with p ≥ 2, (M-W3),
  M ≥ 2L + 1, **κ_c > κ_0 + 3κ̃_0 + 5** (≈ 808.5 [RSF4-fix CQ-1: **807.46** = 151.315 + 651.142 + 5; s5 F3]), **H''_0 := 2^{16}e^{1296w_8}h_0 ≤ c̃_0(κ_c)**, and, with
  η̂ := 2^{n/2+2}e^{6κ̂}Γ_0e^{-p²/16} and **Ĥ_0 := 2max{H''_0, 16eM⁴η̂/C_K}**: **c_*^col := e^{6κ̂}C_KH''_0K̃_0 + M⁴η̂ ≤ 1/16** and
  **Ĥ_0 ≤ (8B̃)^{-1}e^{-6(κ_c-κ_0-3κ̃_0-4)}**. Then the chart indicator is 1 on supp μ_wn ∖ 𝔇 and
    ∫_{𝔇^c}exp(Σ_XH_X(g_0√N𝒞Z))dμ_wn = μ_1(good)^{|Λ|}·exp(Σ_𝒴𝓗_𝒴),  |𝓗_𝒴| ≤ C̃_1Ĥ_0e^{-(κ_c-κ_0-3κ̃_0-5)d^+(𝒴)},
  the sum over 2-connected sets 𝒴, 𝓗_𝒴 a function of the background through {z(𝒵) : 𝒵 ⊂ 𝒴} only. Re-indexed to polymers
  (GEO-col (e)): rate r_Q - 16 log 2, r_Q := κ_c - κ_0 - 3κ̃_0 - 5, prefactor 2^{16}e^{r_Q}C̃_1Ĥ_0. **(M-Q) is not assumed**; M and the p_0
  fixed by M⁴η̂ ≤ 1/32 are g-independent; 2^{j_max} ≍ 1/(g_0p) enters only through the band edge. *Planned: analytic part PROVEN-HERE
  ⇐ Theorem CE-col (Steps 1, 3-4), CE-exp-col, GEO-col, LOC-s′, LOC-s (4), QC, HALO, SH (counted); as a statement on the stage-0
  integral CONDITIONAL ⇐ (FP-loc)_0 + (BGC).*
- **Corollary RATE-Q (L = 3).** Rate reproduction for CE-Q-col (output re-indexed, blocked by SF-blk, against the next input
  requirement κ_c + 16 log 2 + 1296W_3) iff κ_c ≥ κ_c^{Q*} := (6κ_0 + 9κ̃_0 + 16 + 64 log 2 + 1296w_8)/2 (≈ 1478.5 expected). The d ≥ 1
  norm threshold is computed in s4 C. *Planned: PROVEN-HERE (arithmetic; not counted).*

### 12.2 STEP 3: (SL-coer), the restated (CE-Q^∞), and the circularity check
*Idea fixed before writing (exploratory, unwritten):* (i) integrate the gauge-direction noise out first and put the shells on
v := Π_UZ, block by block; (ii) a deep block forces a large slice field nearby (Õ^{1/2} is exponentially local); (iii) local slice
coercivity is provable in the amplitude range of SF-T0; it must be in operator form (a localised positive quadratic form in v),
because per-block Hölder conversions lose N_0²; tilting the product Gaussian by a localised positive form costs only a local
determinant, which is what makes per-site extraction possible; (iv) the reviewer's wording "large slice fluctuation ⇒ plaquette or
kernel defect" is expected to FAIL along residual-gauge directions of ker h_U (Λ_res is not fixed by h_U, only by the Feynman term);
the correct target includes the Feynman energy.
- **Lemma GD (gauge directions).** The stage-0 integrand depends on Z only through v := Π_UZ; under μ_wn the blocks' v_B ∈ ran Π_U|_B
  are independent standard Gaussians (dimension n_B ≤ 4L⁴(N² - 1)), independent of (1 - Π_U)Z. Integrating (1 - Π_U)Z out, Theorem
  CE-Q-col and the band/deep split hold verbatim with blocks as sites (n → n_B, M⁴ sites per cube → (M/L)⁴ blocks, a_{by} →
  a_{bB} := ||𝒞(b, B)||, N_0 → N_r := sup_bΣ_Ba_{bB}) when L | M. The deep set 𝔇_Π := {∃B: |v_B| > 2^{j_max+1}p} is a function of A
  (v = Õ^{1/2}A/(g_0√N)). *Planned: PROVEN-HERE (not counted).*
- **Lemma DL (deep localisation).** N_μ(|Õ^{1/2}|) ≤ N_μ(|Õ|)·(N_μ(|𝒞|) + N_μ(|1 - Π_U|)) < ∞, and if |v_B| ≥ t then some link b has
  |A_b| ≥ g_0√N t e^{μd(b,B)}/N_μ(|Õ^{1/2}|). *Planned: PROVEN-HERE (not counted).*
- **Lemma SLc (small-amplitude local slice coercivity, operator form).** For a set Ω of links, T(Ω) the action terms with pattern in Ω,
  real A = g_0√N𝒞v with ρ_Ω := max_{b∈Ω^+}|A_b| ≤ r_T/8: Σ_{τ∈T(Ω)}|u_0V_τ(A)| ≤ θ(ρ_Ω)⟨v, K_Ωv⟩, with K_Ω := 𝒞1_ΩΠ… (explicit in the
  proof) positive, ||K_Ω|| ≤ 1, tr K_Ω ≤ (explicit)·|Ω|, and θ(ρ) := C_coer·ρ, C_coer explicit in S_T, r_T, n_b, N, ||C||. Valid in
  all slice directions, residual-gauge ones included. *Planned: PROVEN-HERE (not counted).*
- **Lemma TILT (local Gaussian tilt).** For a symmetric K ≥ 0 with ||K|| ≤ 1 and tr K < ∞, θ ∈ [0, 1) and an event E:
  ∫_Ee^{θ⟨v,Kv⟩/2}dγ(v) ≤ exp((1 + θ)tr K/(2(1 - θ)))·sup_{v∈E}e^{-(1-θ)⟨v,Kv⟩/4}. *Planned: PROVEN-HERE (elementary; not counted).*
- **Proposition RES (the reviewer's (SL-coer) wording fails in residual-gauge directions).** There is a g-independent r_res > 0 and a
  real-analytic family {A(λ) : λ ∈ 𝒩} ⊂ ker h_U, 𝒩 a submanifold of Λ of dimension dim Λ_res^U through 0, with |A(λ)| ≍ |λ| and
  e^{A(λ)}U an exact gauge transform of U by a gauge trivial at the block centres: every plaquette norm and every kernel term of
  e^{A(λ)}U equals that of U. So "large slice field near x ⇒ plaquette ≥ τ or kernel mismatch ≥ ε near x" is false on ker h_U.
  *Planned: PROVEN-HERE (a negative; not counted).*
- **(SL-coer′) [named; expected OPEN; the wall].** The corrected target (precise form in §13.2): large slice field near b ⇒ a plaquette
  or kernel defect near b, OR a local Feynman-energy excess ||P_res^UD_U^*A||²_{near b} ≥ c_Fa_1², with, in the second case, an
  operator-form integrand bound as in Lemma SLc. Expected wall: a quantitative local Gribov-freeness of the full gauge fixing
  χ_U = (h_U, P_res^UD_U^*) on the chart, i.e. the "uniqueness of the slice intersection on the chart" clause of (FP-loc)_0, localised.
- **Proposition DX (per-site extraction).** CONDITIONAL ⇐ (SL-coer′) + (FP-loc)_0 + (BGC): every deep block B lies within a
  g-independent distance R_* of either a U-variable defect at a threshold ε' (priced per defect at stage 0 by Wilson positivity
  s(W) ≥ ||1 - W||²_op/(2N) or by RLARGE branch (i)) or of a Feynman-energy excess (priced per site by Lemma TILT), each defect serving
  ≤ (2R_* + 1)⁴ blocks; hence a per-deep-block factor e^{-a'/g_0²} with a' explicit, multiplicative over far-apart blocks, in place of
  the |Λ| union bound. The large-field normalisation bookkeeping (the Gaussian/Haar normalisation of the removed region) is named, not
  written.
- **Circularity check (to be written in §13.2):** which items consume (SG^fl)_0, and a non-circular order.

## 13. Session-4 proofs (written 05:28-05:31 UTC, appended 05:31 UTC; after §12, after the s4 criteria (05:22:00 UTC) and after s4 ran 05:25:24-05:25:32 UTC; post-append corrections 05:32-05:35 UTC are marked [post-proof])

### 13.1 STEP 2: Theorem CE-Q-col

**Lemma HALO: PROVEN-HERE (not counted).** *Proof.* Index distances are ℓ^∞ on the torus of cubes. That metric is geodesic for
the cube graph with ℓ^∞-adjacency, so dist(c, S^{(r)}) = max{dist(c, S) - r, 0}. (a) X small means X^+ ∩ R = ∅. H_y ⊂ R is the box of
radius ℓ - 1 about q(y) (ℓ := ℓ_{j_y}), so every cube of X^+ is at distance ≥ ℓ from q(y), i.e. n(y, X) ≥ ℓ. (b) Let y ∈ Q_β, β ≠ α,
and D := dist(q(y), R̄_α), attained at c ∈ R̄_α. If D ≤ ℓ - 1 then c ∈ H_y ⊂ R̄_β, which is impossible (classes are disjoint). Otherwise,
step from q(y) towards c along an ℓ^∞ geodesic ℓ - 1 times. This gives c' ∈ H_y ⊂ R̄_β with dist(c', c) = D - ℓ + 1. Cubes of
different classes are not linked, so D - ℓ + 1 ≥ 8, i.e. **D ≥ ℓ + 7**. If q(y) ∉ U_α^+ = R̄_α^{(8)}, then n(y, U_α) = D - 8 ≥ ℓ - 1, and
n ≥ 1. Finally max{1, ℓ - 1} ≥ ℓ/2. (c) If q(y) ∈ U_α^+, D ≥ ℓ + 7 still holds, so dist(q(y), W_α) = D - 2 ≥ ℓ + 5. (d) R̄_α = ∪_{y∈Q_α}H_y.
So W_α = ∪q(y)^{(ℓ_y+1)}, U_α = ∪q(y)^{(ℓ_y+6)} and U_α^+ = ∪q(y)^{(ℓ_y+7)}, with boxes of sides 2ℓ_y + 3, 2ℓ_y + 13, 2ℓ_y + 15. U_α is
*-connected: each box is connected, and two halos at distance ≤ 7 have each other's nearest cube inside the radius-7 dilation.
d(U_α) ≤ 2(|U_α| - 1) is CE-Q's spanning-tree bound (REVIEW_SF_S3 B-2). (e) If X^+ meets c ∈ R̄_α, some x ∈ X has dist(x, c) ≤ 1. X has
index diameter ≤ 1, so X ⊂ R̄_α^{(2)} = W_α. If X^+ also met c' ∈ R̄_β, then dist(c, c') ≤ 1 + 1 + 1 ≤ 7, so the two cubes would be
linked: a contradiction. (f) LOC-s (4): δ(y, ·) > M·n. In (a), μδ > μMℓ_j ≥ 4(j + 1)log 2. In (b), μδ > μMℓ_j/2 ≥ 2(j + 1)log 2. In (c), the
fine distance from y to the sites of W_α is ≥ (ℓ_j + 4)M + 1, so μδ > 4(j + 1)log 2 + 4μM. In every case 2^{j+1}e^{-μδ} ≤ e^{-μδ/2}. ∎
(s4 A, criteria first. d = 2 and 3 tori, 70 random trials, random ℓ ∈ {1, …, 4}: 0 violations of (a)-(e), with 4124 pairs in (b), 3036
of them with ℓ ≥ 2, and 42 pairs in (c). **Negative control A7:** the stronger claim n(y, U_α) ≥ ℓ, which a halo built with 2 log 2 in
place of 4 log 2 would need, is violated 139 times. So the ℓ/2 weakening in (b), and hence the factor 4 in ℓ_j, is load-bearing.) [RSF4-fix HALO-b: (b) is
**tight**: REVIEW_SF_S4 B-1's independent d = 2 run found 32 of 878 pairs with n(y, U_α) = ℓ - 1 exactly. So 4 log 2 (not 2 log 2)
is NEEDED in ℓ_j, not merely sufficient for this proof.]

**Lemma SH: PROVEN-HERE (not counted).** *Proof.* Put L_j := log Γ_j - log Γ_0 and c_Γ := 2κ̂ + w_8 + 2h_0 ≤ 2κ' + 3 ≤ 3κ'. If ℓ_j = 1,
then L_j = 0 ≤ (4^j - 1)p²/32. If ℓ_j ≥ 2, then 4(j + 1)log 2 > μM, so j + 1 > J_M := μM/(4 log 2). (M-W3) gives μM ≥ 10κ' + 16, so
J_M ≥ 3.6κ' and j ≥ 3.6κ' - 1 ≥ max{25, c_Γ} (κ' ≥ κ_c > 808). Also ℓ_j ≤ 1 + (j + 1)/J_M ≤ 2(j + 1), so 2ℓ_j + 15 ≤ 4j + 19 ≤ 23j and
L_j ≤ c_Γ(23j)⁴ ≤ 2.8·10⁵j⁵. For p ≥ 2 and j ≥ 1, (4^j - 1)p²/32 ≥ 4^j/16, and 4^j ≥ 4.5·10⁶j⁵ for j ≥ 25 (4^j/j⁵ increases for j ≥ 4;
4^{25}/25⁵ = 1.15·10⁸). So L_j ≤ (4^j - 1)p²/32 for every j, which is the pointwise claim:
Γ_je^{-4^jp²/16} = Γ_0e^{-p²/16}e^{L_j - (4^j-1)p²/16} ≤ Γ_0e^{-p²/16}e^{-(4^j-1)p²/32}. Summing, using p ≥ 2:
Σ_{j≥0} ≤ Γ_0e^{-p²/16}(1 + Σ_{j≥1}e^{-(4^j-1)/8}) = 1.841·Γ_0e^{-p²/16} ≤ 2Γ_0e^{-p²/16} (s4 C7: 0.841024). ∎ (s4 B: a grid of 4 κ_c ×
3 μM × 4 p × 2 h_0, j up to 3J_M + 10, so ℓ_j ≥ 2 is reached at every grid point. Pointwise inequality: 0 violations. Shell-sum ratio:
max 1.4959 ≤ 2.)

**Theorem CE-Q-col: analytic part PROVEN-HERE ⇐ Theorem CE-col (Steps 1, 3-4), Corollary CE-exp-col, Lemma GEO-col, LOC-s′,
LOC-s (4), QC, HALO, SH (counted). As a statement on the stage-0 integral: CONDITIONAL ⇐ (FP-loc)_0 + (BGC).**
[Post-proof precision, written with the proof: the shell integration uses μ_1(good) ≥ ½, which needs **p² ≥ 4(n log 2 + 2)** (the
session-3 condition); (B3)'s p ≥ 2 does not imply it. It is added to the hypotheses. It is implied by p ≥ p_0 (s4 C8:
p_0 ≈ 4.2·10⁴). [RSF4-fix CQ-1: 4.24·10⁴ is p_0 at the RATE threshold κ_c = 1478.5. The band iterates in norm only from
κ_c ≥ 2938.18, where **p_0 ≈ 6.45·10⁴** (REVIEW_SF_S4 B-5, independently re-derived there); to leading order p_0 ≈ √(32·15⁴κ̂). Both are
g-independent.]]
*Step 0 (chart).* As in §10.1: on supp μ_wn ∖ 𝔇 the field at real s = 1 is ≤ ρ_* ≤ r_T/8, so 1_D ≡ 1.
*Step 1 (structure, readability).* Setting CE-Q-col's Q, H_y, R, R̄_α, Q_α, W_α, U_α, and large/small. Whether a site is a Q-site, and its
shell, is read on that site. The halo of a Q-site of class α lies in R̄_α ⊂ U_α. Every other structural fact used for a member is
decided inside the cluster that contains it (consistency, Step 4).
*Step 2 (localisation; no (M-Q)).* Large components: G_α := exp(Σ_{X large in W_α}H_X). Apply LOC-s′ with "X^+" := U_α^+ and radii
r_y := e^{μδ(y,U_α)} (good y) or 2^{-(j_y+1)}e^{μδ(y,U_α)} (y ∈ Q, q(y) ∉ U_α^+). At b ∈ W_α on the refined domain:
- the class's own Q-sites (s = 1) contribute σ^α_b;
- good sites of U_α^+ contribute ≤ ρ'/2;
- Q-sites of other classes with q(y) ∈ U_α^+ (s = 1) contribute ≤ g_0√NpΣ_ya_{by}e^{μd(b,y)}·2^{j_y+1}e^{-μ(ℓ_{j_y}+4)M} ≤ g_0√NpN_μe^{-4μM}
  ≤ ρ'/2, by HALO (c) (2^{j+1}e^{-μMℓ_j} ≤ 2^{-3(j+1)});
- S-sites contribute ≤ g_0√NΣ_ya_{by}(1 + r_y)|Z_y| ≤ ρ', since (1 + r_y)2^{j_y+1} ≤ 2e^{μδ} by HALO (b), (f).
So |A_b| ≤ 2ρ' + σ^α_b ≤ ρ_* by (B1′). An S-site costs r_y^{-1} ≤ e^{-μδ(y,U_α)/2}.
Small X: LOC-s′ with X^+. X^+ contains no Q-site, so the field is ≤ ρ', and a Q-site in S costs ≤ e^{-μδ/2} by HALO (a), (f). So
|F_{X,S}| ≤ h_0Π_{y∈S}e^{-μδ(y,X)/2}, which is LOC-s's bound at rate μ/2. Corollary CE-exp-col's regrouping on the collar-free hull
Y_0(X, S) gives H''(Y_0) := Σ_{X small, Y_0(X,S)=Y_0}F_{X,S}, which reads Z on ∪Y_0^+. Since d(X) = 0, |X^+| ≤ 1296 and
e^{κ'd(Y_0)} ≤ Π_ye^{κ'(2n_y+3)}, so e^{κ'd(Y_0)}|H''(Y_0)| ≤ h_02^{|Y_0|}e^{1296W_3(μ/2)}. Hence |H''(Y_0)| ≤ H''_0e^{-κ_cd(Y_0)} with
H''_0 = 2^{16}e^{1296w_8}h_0, because (M-W3) is CE-exp-col's sufficient condition at rate μ/2.
*Step 3 (cost of a large component).* As §10.1 Step 3, with |W_α| ≤ Σ_{y∈Q_α}(2ℓ_{j_y} + 3)⁴ (HALO (d)). The baseline is
≤ 2h_0Σ_{y∈Q_α}(2ℓ_{j_y} + 3)⁴. The cubic, Jacobian and source terms are ≤ Σ_{y∈Q_α}c(j_y) by QC, with c(j) ≤ (3/16)4^jp² under (B2)-(B3). So
|G_{α,S}| ≤ Π_{y∈Q_α}e^{(3/16)4^{j_y}p² + 2h_0(2ℓ_{j_y}+3)⁴}·Π_{y∈S}e^{-μδ(y,U_α)/2}.
*Step 4 (Mayer step and clusters, collar form).*
- Pointwise on supp μ_wn ∖ 𝔇, Theorem CE-col's Step 1 at rate κ_c applies to exp(Σ_{Y_0}H''(Y_0)). It needs H''_0 ≤ log 2 and
  H''_0 ≤ (32K_0)^{-1}e^{-6(κ_c-κ_0)}: the Fix-Q1 analogue, contained in H''_0 ≤ c̃_0(κ_c). The result is a sum over families of
  2-connected cores c with pairwise disjoint collars of ΠK(c). Each K(c) reads Z on c^+, and |K(c)| ≤ C_KH''_0e^{-κ_1d^+(c)}, κ_1 = κ_c - κ_0 - 2.
- G-members: Ŷ_{α,S} := Y_0(U_α, S), CE-exp-col's collar-free hull with the polymer U_α. It satisfies U_α ⊂ Ŷ, q(y) ∈ Ŷ (y ∈ S), and
  d(Ŷ) ≤ d(U_α) + Σ_{y∈S}(2n(y, U_α) + 3). G_{α,S} reads Z on U_α^+ ∪ S ⊂ ∪Ŷ^+.
- Members are linked when their collars meet. Clusters are the linked components, and distinct clusters have disjoint collars.
- Ψ(𝒵) := the sum over cluster data with union 𝒵: the Q-structure computed from Z on 𝒵^+, the S_α and the cores. Ψ carries 1_{𝔇^c} on
  𝒵^+, the good-indicator of every site of 𝒵^+ that is not a Q-site of 𝒵, and the consistency indicator (every Q-site of 𝒵 lies in a
  class with U_α ⊂ 𝒵).
- **Claim:** e^{ΣH}1_{𝔇^c} = Σ_{families {𝒵_k} with pairwise disjoint collars}Π_kΨ(𝒵_k)·Π_{y∉∪𝒵_k^+}1[|Z_y| ≤ p].
  - (⇒) Every term of Π_αΣ_SG_{α,S}·Σ_{cores}ΠK groups uniquely into clusters, and members of different clusters are not linked.
    Every Q-site y lies in U_β ⊂ Ŷ_β. If y lay in 𝒵^+ but in another cluster 𝒵', then 𝒵' ∩ 𝒵^+ ≠ ∅ and the collars would meet. So
    the sites of 𝒵^+ that are not Q-sites of 𝒵 are good, and so are the sites outside ∪𝒵_k^+.
  - (⇐) In a family with non-zero product, every Q-site lies in ∪𝒵_k. A class computed inside 𝒵_k has U ⊂ 𝒵_k. A halo cube of 𝒵_{k'},
    k' ≠ k, within distance 7 of it would lie in U ⊂ 𝒵_k, contradicting 𝒵_k ∩ 𝒵_{k'} = ∅. So the computed classes are the true ones.
    Smallness of X ⊂ 𝒵_k (X^+ ⊂ 𝒵_k^+) is decided by R ∩ 𝒵_k^+, which is the computed R(𝒵_k) ∩ 𝒵_k^+ (other clusters' halos lie in
    their own sets, disjoint from 𝒵_k^+).
  So every term occurs exactly once.
- Ψ(𝒵) reads Z on 𝒵^+ and μ_wn is a product, so ∫_{𝔇^c}e^{ΣH}dμ_wn = μ_1(good)^{|Λ|}P(z), with
  z(𝒵) := μ_1(good)^{-#sites(𝒵^+)}∫Ψ(𝒵)dμ_wn|_{𝒵^+}. P is CE-col's hard-core polynomial (families with pairwise disjoint collars).
*Step 5 (activity bounds).* 𝒵 is 2-connected: members are 2-connected, and linked members have cubes at index distance ≤ 2.
- Pure part (no Q-site in 𝒵): a single core, since cores are pairwise collar-disjoint. It is bounded by C_KH''_0e^{-κ_1d^+(𝒵)}.
- Mixed part. Take a spanning tree of the member graph. By GEO-col (b), d^+(𝒵) ≤ Σ_md^+(m) + 6(n - 1), so
  Π_me^{-κ̂d^+(m)} ≤ e^{-κ̂d^+(𝒵)}Π_me^{6κ̂}, with **κ̂ := κ_1 - κ̃_0**.
  - Cores: e^{6κ̂}e^{κ̂d^+(c)}|K(c)| ≤ e^{6κ̂}C_KH''_0e^{-κ̃_0d^+(c)}. Summed over families of 2-connected cores in 𝒵, this is
    ≤ exp(e^{6κ̂}C_KH''_0K̃_0|𝒵|) (GEO-col (c), summed over the cubes of 𝒵).
  - G-members: d^+(Ŷ) ≤ d(Ŷ) (GEO-col (b)) ≤ d(U_α) + Σ_{y∈S}(2n_y + 3), with d(U_α) ≤ 2Σ_{y∈Q_α}(2ℓ_{j_y} + 13)⁴ (HALO (d)). The S-sum is
    Σ_SΠ_{y∈S}e^{κ̂(2n_y+3)}e^{-μδ(y,U_α)/2} ≤ exp(|U_α^+|W̃_3). Here δ > Mn (LOC-s (4) with X := U_α), there are ≤ |U_α^+|(2n + 1)⁴M⁴
    sites at cube distance n, and W̃_3 := M⁴e^{3κ̂}Σ_n(2n + 1)⁴e^{-(μM/2-2κ̂)n} ≤ W_3(μ/2) ≤ w_8 (κ̂ < κ'). So
    Σ_Se^{6κ̂}e^{κ̂d^+(Ŷ_{α,S})}|G_{α,S}| ≤ e^{6κ̂}Π_{y∈Q_α}Γ_{j_y}e^{(3/16)4^{j_y}p²}. Charge e^{6κ̂} to one Q-site of α.
  - Shell integration (SF-cut (b) at the lower edge 2^jp; μ_1(good) ≥ ½): each Q-site carries
    ≤ Σ_{j=0}^{j_max}2^{n/2+1}e^{6κ̂}Γ_je^{-4^jp²/4 + (3/16)4^jp²} ≤ 2^{n/2+2}e^{6κ̂}Γ_0e^{-p²/16} = η̂ (Lemma SH).
  - Summing over non-empty Q ⊂ sites(𝒵) gives ≤ M⁴|𝒵|η̂e^{M⁴|𝒵|η̂}. With |𝒵| ≤ 16(1 + d^+(𝒵)) ≤ 16e^{d^+} (GEO-col (a)) and
    c_*^col ≤ 1/16, the mixed part is ≤ 16eM⁴η̂e^{-(κ̂-2)d^+(𝒵)}.
- Sum of the two (the Fix-Q2 form): |z(𝒵)| ≤ C_KĤ_0e^{-(κ̂-2)d^+(𝒵)}, Ĥ_0 = 2max{H''_0, 16eM⁴η̂/C_K} (κ_1 ≥ κ̂ - 2).
*Step 6 (hard-core step).* Theorem CE-col's Steps 3-4 use the activities only through |z_c| ≤ C_KH_0e^{-κ_1(κ)d^+(c)} on 2-connected c, the
collar incompatibility, and the third entry of c̃_0. Take κ_1(κ) := κ - κ_0 - 2 := κ̂ - 2, i.e. κ := κ_c - κ̃_0 - 2. Their hypotheses are then
κ > κ_0 + 2κ̃_0 + 3 ⟺ **κ_c > κ_0 + 3κ̃_0 + 5** and **Ĥ_0 ≤ (8B̃)^{-1}e^{-6(κ_c-κ_0-3κ̃_0-4)}**. Output: P(z) = exp(Σ_𝒴𝓗_𝒴), with
|𝓗_𝒴| ≤ C̃_1Ĥ_0e^{-(κ-κ_0-2κ̃_0-3)d^+(𝒴)} = C̃_1Ĥ_0e^{-(κ_c-κ_0-3κ̃_0-5)d^+(𝒴)}. 𝓗_𝒴 depends on {z(𝒵) : 𝒵 ⊂ 𝒴}. Re-index as in
CE-col (GEO-col (e)). ∎
**Statement as proven.** Hypotheses: (FP-loc)_0, (BGC), (B1′), (B2), (B3) with p ≥ 2, **p² ≥ 4(n log 2 + 2)**, (M-W3), M ≥ 2L + 1,
κ_c > κ_0 + 3κ̃_0 + 5, H''_0 ≤ c̃_0(κ_c), c_*^col ≤ 1/16, and Ĥ_0 ≤ (8B̃)^{-1}e^{-6(κ_c-κ_0-3κ̃_0-4)}. Under them:
  **∫_{𝔇^c}exp(Σ_XH_X(g_0√N𝒞Z))dμ_wn = μ_1(good)^{|Λ|}exp(Σ_𝒴𝓗_𝒴),  |𝓗_𝒴| ≤ C̃_1Ĥ_0e^{-(κ_c-κ_0-3κ̃_0-5)d^+(𝒴)}.**
*g-dependence.* M is fixed by (M-W3), which involves only κ'. p_0 is fixed by M⁴η̂ ≤ min{1/32, C_K(8B̃)^{-1}e^{-6(κ_c-κ_0-3κ̃_0-4)}/(32e)}
(M, κ̂, n only). Both are g-independent. The remaining conditions hold for g_0 small, since h_0 = O(g_0M⁴p³), and 2^{j_max} ≍ 1/(g_0p) is
only the band edge. This settles REVIEW_SF_S3 B-7: SF-blk/RATE, FLOW F-Π (C_Π ∝ M⁶), RLARGE/HIST (I_k^E)(b), g_CE and p_0 keep
g-independent constants on this route. (s4 C8: at κ_c = 1478.5, M_W3 = 3.14·10¹⁴ and p_0 ≈ 4.24·10⁴ from M⁴η̂ ≤ 1/32 [RSF4-fix CQ-1: ≈ 6.45·10⁴ at the norm-closing
κ_c = 2938.2, which is the κ_c actually used], against 7.2-7.7·10⁵ for
session-3's CE-Q.) **CE-Q-col is in CE-col's locality class, so it composes (in rate) across levels; it supersedes Theorem CE-Q.**
What it does not give: (SF-irr); the inherited activities as (H-exp) inputs (item (iv)); and the deep set (§13.2).

**Corollary RATE-Q: PROVEN-HERE (arithmetic; not counted).** Output rate r_Q = κ_c - κ_0 - 3κ̃_0 - 5 in d^+, re-indexed r_Q - 16 log 2,
blocked (SF-blk, L = 3): 3(κ_c - 2κ_0 - 3κ̃_0 - 5 - 16 log 2) - 1. This is ≥ the next input requirement κ_c + 16 log 2 + 1296W_3 iff
κ_c ≥ κ_c^{Q*} = (6κ_0 + 9κ̃_0 + 16 + 64 log 2 + 1296w_8)/2 = **1478.49** (s4 C5). The rise over CE-col's 1149.92 is 3(κ̃_0 + 2)/2 = 328.6.
(REVIEW_SF_S3 D-4 estimated ≈ 230 from a κ_0 + 2 loss; the loss is κ̃_0 + 2 because the K-members are 2-connected cores, which are
counted with κ̃_0.) Norm thresholds: §13.3.

### 13.2 STEP 3: (SL-coer), the restated (CE-Q^∞), and the circularity check

**Lemma GD: PROVEN-HERE (not counted).** *Proof.* 𝒞 = Π_UÕ^{-1/2}Π_U (SF-WN), so A = g_0√N𝒞Z = g_0√N𝒞Π_UZ. The integrand (the activities
of A and the chart indicator of A) is therefore a function of v := Π_UZ. Π_U is an orthogonal projection and block-diagonal,
Π_U = ⊕_BΠ_B. Under μ_wn the block vectors Z_B are independent standard Gaussians, and Z_B = Π_BZ_B + (1 - Π_B)Z_B is an orthogonal
splitting into independent standard Gaussians on ran Π_B and its complement. So ∫F(Π_UZ)dμ_wn = ∫F(v)Π_Bdγ_B(v_B).
The proofs of SF-cut, LOC-s, LOC-s′, QC, HULL, CE-exp-col, HALO, SH and CE-Q-col use only three things: a product probability
measure over "sites" with the tail bound P(|v_B| > t) ≤ 2^{n_B/2}e^{-t²/4} (SF-cut (b)'s Chernoff step in dimension n_B); a field map
A_b = Σ_B𝒞(b, B)v_B with a_{bB} := ||𝒞(b, B)||_op, row sums ≤ N_r and column sums ≤ N_c; and site counts per cube. With blocks as sites
(L | M) these hold with n → n_B ≤ 4L⁴(N² - 1), M⁴ → (M/L)⁴, N_r ≤ N_0 (Σ_Ba_{bB} ≤ Σ_ya_{by}) and QC's column bound 4N_0 → N_c ≤ 4L⁴N_0
(a_{bB} ≤ Σ_{y∈B}a_{by}). On ran Π_U, Õ commutes with Π_U and Õ^{1/2}𝒞 = Π_U, so **v = Õ^{1/2}A/(g_0√N)**. The deep set
𝔇_Π := {∃B : |v_B| > 2^{j_max+1}p} is therefore a function of the slice field A: Fix C-1 is applied. ∎
[RSF4-fix GD-1: "hold verbatim" is withdrawn; the constants change (all stay g-independent). With blocks as sites (L | M):
(i) QC's column bound 4N_0 → N_c ≤ 4L⁴N_0, so **C_3^{Q,B} ≤ L⁴C_3^Q, C_2^{Q,B} ≤ L⁴C_2^Q, C_1^{Q,B} ≤ L⁴C_1^Q** (each is one column sum times
powers of the row sum N_r ≤ N_0); (ii) n → **n_B ≤ 4L⁴(N² - 1)** in SF-cut (b), in η̂_B := 2^{n_B/2+2}e^{6κ̂}Γ_0e^{-p²/16} and in the
shell condition **p² ≥ 4(n_B log 2 + 2)**; (iii) M⁴ sites per cube → **(M/L)⁴ blocks per cube** in c_*^col, Ĥ_0 and the Q-sum (Step 5),
with L | M; (iv) (B1′)-(B3) read 2ρ' + g_0√NN_r2^{j+1}p ≤ ρ_*, C_3^{Q,B}g_02^jp ≤ 1/16, C_2^{Q,B}g_0² ≤ 1/16, C_1^{Q,B}g_0 ≤ 1/16, p ≥ 2,
and a_*^B := min{(16C_3^{Q,B})^{-2}, (ρ_*/(4√NN_r))²}. Γ_j is a count of cubes and is unchanged. REVIEW_SF_S4 B-4 checked that
p² ≥ 4(n_B log 2 + 2) still holds at p_0 (n_B = 2592 for N = 3).]

**Lemma DL: PROVEN-HERE (not counted).** *Proof.* N_μ(K) := sup_bΣ_{b'}|K(b, b')|e^{μd(b,b')} is submultiplicative (triangle inequality).
Õ^{1/2} = Õ·Õ^{-1/2} with Õ^{-1/2} = 𝒞 + (1 - Π_U) (Setting N5-bg). So N_μ(|Õ^{1/2}|) ≤ N_μ(|Õ|)(N_μ(|𝒞|) + N_μ(|1 - Π_U|)), which is finite:
Õ has range r_1 = 8L - 4 and bounded entries, and 1 - Π_U is block-diagonal. Õ^{1/2} is symmetric, so
g_0√N|v_B| ≤ Σ_b||Õ^{1/2}(B, b)|| |A_b| ≤ N_μ(|Õ^{1/2}|)·max_b|A_b|e^{-μd(b,B)}, and the max is attained. ∎
*Consequence.* A deep block forces |A_b| ≥ a_deep e^{μd(b,B)} at some b, with a_deep := min{√N/(16C_3^Q), ρ_*/(4N_r)}/N_μ(|Õ^{1/2}|) [RSF4-fix
DL-1: |v_B| is a norm over the 4L⁴ links of B, so the B-row sum is ≤ 4L⁴e^{μ·diam B}N_μ(|Õ^{1/2}|); read **a_deep := min{√N/(16C_3^{Q,B}),
ρ_*/(4N_r)}/(4L⁴e^{μ·diam B}N_μ(|Õ^{1/2}|))**, still g-independent], a
g-independent number (from §10.1's lower bound on 2^{j_max+1}). On the chart (|A_b| < π√N) this b lies within fine distance
R_DL := μ^{-1}log(π√N/a_deep) of B [RSF4-fix DL-1: on SF-A2^0's chart ||1 - e^{A_b}|| ≤ ε^thr_N ≤ ½, so |A_b| ≤ 1.011√N/2 and
R_DL := μ^{-1}log(1.011√N/(2a_deep)); on session 5's shrunk chart (§16) |A_b| ≤ r_sol and R_sh := μ^{-1}log(r_sol/a_sh)]. **This is the reviewer's "translation" (Part C 4): a deep block is a localised large slice field.**

**Lemma SLc: PROVEN-HERE (not counted).** *Statement as proven.* Let Ω be a set of links, T(Ω) the action terms whose pattern lies in
Ω, ρ_Ω := max_{b∈Ω}|A_b| ≤ ρ_* = min{r_T/8, r_𝔫/2} [post-proof: was "≤ r_T/8"; SF-src needs ρ ≤ r_𝔫/2] for the real slice field A = g_0√N𝒞v, and let 𝔫-terms be those whose contour lies in Ω. Put
K_Ω := 𝒞1_Ω𝒞/||C||. Then K_Ω ≥ 0, ||K_Ω|| ≤ 1, tr K_Ω ≤ (N² - 1)|Ω|, and
  Σ_{τ∈T(Ω)}|u_0V_τ(A)| + Σ_{b∈Ω}|log j(A_b)| + Σ_c|𝔫_c(e^AU) - 𝔫_c(U)| ≤ (C_coerρ_Ω + C'g_0²)⟨v, K_Ωv⟩ + 8K_𝔫c_yy_bgρ_Ω·#{c},
  C_coer := 1024S_Tn_bN||C||/r_T³,  C' := (N²/9 + 9K_𝔫c_y²n'_cN)||C||.
This holds in every slice direction, residual-gauge directions included.
*Proof.* SF-T0 (4): |V_τ| ≤ 16S_T(4ρ_τ/r_T)³ ≤ 1024S_Tr_T^{-3}ρ_ΩΣ_{b∈P_τ}|A_b|². Each link lies in ≤ n_b patterns, so
Σ_τ|u_0V_τ| ≤ g_0^{-2}·1024S_Tn_br_T^{-3}ρ_Ω|1_ΩA|². |1_ΩA|² = g_0²N⟨v, 𝒞1_Ω𝒞v⟩ = g_0²N||C||⟨v, K_Ωv⟩ (𝒞 symmetric). ||K_Ω|| ≤ ||𝒞||²/||C|| = 1
(C = 𝒞², SF-WN), and tr K_Ω = Σ_{b∈Ω}tr C(b, b)/||C|| ≤ (N² - 1)|Ω|. SF-J (5): |log j(A_b)| ≤ (N/9)|A_b|². SF-src: the ρ² part is
≤ 9K_𝔫c_y²Σ_{b∈contour}|A_b|². Both are proportional to g_0²N||C||⟨v, K_Ωv⟩ (with n'_c contours per link). The linear source part is
≤ 8K_𝔫c_yy_bgρ_Ω per coarse link. ∎ *Why operator form.* The per-block Hölder conversion of QC (|A_b|² ≤ g_0²NN_rΣ_Ba_{bB}|v_B|²) would
replace ||C|| by N_rN_c, i.e. lose ≈ N_0². The operator form loses only ||C||.

**Lemma TILT: PROVEN-HERE (not counted; elementary).** *Proof.* Put θ'' := (1 + θ)/2. Then
e^{θ⟨v,Kv⟩/2}e^{-|v|²/2} = e^{-⟨v,(1-θ''K)v⟩/2}e^{-(θ''-θ)⟨v,Kv⟩/2}, and θ'' - θ = (1 - θ)/2. On E bound the second factor by its sup, and
integrate the first: det(1 - θ''K)^{-1/2} = exp(-½Σlog(1 - θ''k_i)) ≤ exp(½·(θ''/(1 - θ''))·tr K) = exp((1 + θ)tr K/(2(1 - θ))), using
-log(1 - x) ≤ x/(1 - x) and 0 ≤ k_i ≤ 1. ∎ (s4 D1: 20 random K, 4 θ, 3 events, no violation, max ratio 0.344. The plain Monte Carlo
estimate has infinite variance at θ = 0.9 for eigenvalues near 1. The exact-tilt reference (sampling the tilted Gaussian) gives the
same maximum, 0.344.)
*Corollary SLc-X (small-amplitude per-site factor; PROVEN-HERE as an inequality, not counted).* Suppose that on an event E the real
slice field on Ω stays ≤ a ≤ ρ_* with θ := 2(C_coera + C'g_0²) < 1 [post-proof: the factor 2 converts SLc's θ(ρ)⟨v,Kv⟩ into TILT's
θ⟨v,Kv⟩/2], and that some b_0 ∈ Ω has |A_{b_0}| ≥ a_0. Then
⟨v, K_Ωv⟩ ≥ |A_{b_0}|²/(g_0²N||C||) on E, and by SLc and TILT the Ω-terms contribute at most
  ∫_E|e^{Σ_{Ω-terms}H}|dγ ≤ exp((1 + θ)(N² - 1)|Ω|/(2(1 - θ)) + 8K_𝔫c_yy_bga·#{c})·e^{-(1-θ)a_0²/(4g_0²N||C||)}:
**an exponentially small factor per site, with a local (not |Λ|) prefactor.** With a_0 = a_deep (DL), this is the reviewer's
per-site extraction, in the amplitude range a ≤ min{ρ_*, a_θ}, a_θ := (1 - 4C'g_0²)/(4C_coer) (so θ ≤ ½) [post-proof: was
(1 - C'g_0²)/(2C_coer), which gives θ > 1 in TILT's convention]. The event "field on Ω ≤ a" is not a product event in
v. Inserting this absolute bound into the polymer expansion, with the deep region as polymer support and the band expansion off it,
is bookkeeping not written here: **(DX-loc)** [OPEN; same class as the large-field normalisation bookkeeping (H-w)].

**Proposition RES: PROVEN-HERE (a negative; not counted).** *Proof.* Define F: Λ → su(N)^{N_c} by F(λ) := h_U(A(λ)), where
A(λ)_b := log(e^{λ(x)}U_be^{-λ(y)}U_b^{-1}) (principal log), b = (x, y). It is real-analytic on {max|λ| < (log 2)/2}, since
||e^{λ(x)}U_be^{-λ(y)}U_b^{-1} - 1|| ≤ e^{2max|λ|} - 1 < 1 there. F(0) = 0. d/dt A(tλ)_b|_0 = λ(x) - Ad(U_b)λ(y) = -(D_Uλ)_b, so
DF(0) = -h_U∘D_U|_Λ = -M_U (NA-FP (i), and λ(c) = 0 on Λ). This is onto su(N)^{N_c}, with kernel Λ_res^U (NA-FP (ii)). By the
real-analytic submersion theorem, 𝒩 := F^{-1}(0) ∩ {|λ| < r_res} is a real-analytic submanifold of dimension
dim Λ_res^U = dim Λ - (N² - 1)N_c > 0, tangent to Λ_res^U, for some r_res > 0 fixed by the background class (g-independent).
For λ ∈ 𝒩: A(λ) ∈ ker h_U and e^{A(λ)_b}U_b = g(x)U_bg(y)^{-1} with g := e^λ, g(c_X) = 1. So (e^AU)_p = g(x_p)U_pg(x_p)^{-1}, every plaquette
norm and S_W are unchanged, and M̄_c(e^AU) = g(c_X)M̄_c(U)g(c_Y)^{-1} = M̄_c(U) (SF-T0 (2)), so every kernel term and every n_c is
unchanged. D_U is injective on Λ (NA-FP (ii)), so |A(λ)| ≥ c_D|λ|/2 for small λ. ∎
(s4 D2: SU(2), 4×4 sites, blocks of side 2, one axial ordering (NA-FP's ℓ_P, for which (i) holds by the same telescoping). 5 of 5
Gauss-Newton projections converge to |h(A(λ))| ≤ 6·10⁻¹⁷ with max_b|A_b| = 0.35-0.50, reconstruction error ≤ 4.5·10⁻¹⁶, and plaquette-norm
change ≤ 3.3·10⁻¹⁶. Control D3: generic directions of ker h of the same size change plaquette norms by 0.36-0.51.)
*Consequence.* REVIEW_SF_S3's (SL-coer) wording, "large slice fluctuation near x ⇒ plaquette ≥ τ or kernel mismatch ≥ ε near x", is
**false on ker h_U**. ker h_U fixes only the block-mean gauge; the residual gauge Λ_res^U is weighted by the Feynman term
½||P_res^UD_U^*A||² of O, not removed. Along 𝒩, ΔS ≡ 0, so the only suppression is the Feynman Gaussian. In white-noise variables
e^{ΣH} = e^{u_0H(A,A)/2}·(Jacobian, 𝔫 ratio), with H(A, A) = H(q, q) = O(|λ|⁴), since H·D_Uλ = 0 at a critical background (NA-inv) and
A = -D_Uλ + q, q = O(λ²). So any correct (SL-coer) must count the Feynman energy.
[RSF4-fix RES-1 (cosmetic): read e^{u_0H(A,A)/(2N)} (SF-A2^0's (u_0/2N) normalisation). RES-2 (relation to (FP-loc), REVIEW_SF_S4 C-5):
RES does NOT contradict (FP-loc)_0's "uniqueness of the slice intersection". NA-FP's fixing χ_U = (h_U, P_res^UD_U^*) imposes h_U = 0 as a
δ-constraint and **averages** the residual part with the 't Hooft weight e^{-(u_0/2N)||P_res^UD_U^*A||²} (PROOF l.3062-3063); the residual
gauge is averaged, NOT fixed. Uniqueness therefore means: for each ω the orbit meets {h_U = 0, P_res^UD_U^*A = ω} once in the chart, i.e.
λ ↦ P_res^UD_U^*A(λ) is injective along RES's residual orbit 𝒩. A failure of (F) near b_0 means that this map is nearly non-injective
(small Feynman energy at large A): a **soft-gauge Gribov copy**. This is a Gribov-type uniqueness issue of the slice, sitting in
(FP-loc)_0's nonlinear uniqueness clause. Session 5 (§16.1, Propositions FP-uniq, FP-sh) proves that clause on a shrunk chart.]

**(SL-coer′) [OPEN; named; the wall. Stage-0 form].** There are g-independent a_1 ≤ a_deep, τ_c, ε_c, c_F > 0, θ_1 < 1 and R_c < ∞
with the following property. Take a real background with (BGC), a real A ∈ ker h_U in (FP-loc)_0's chart, and a link b_0 with
|A_{b_0}| ≥ a_1. Let Ω := the links within fine distance R_c of b_0. Then at least one of:
- **(P)** a plaquette p ⊂ Ω has ||1 - (e^AU)_p||_op ≥ τ_c, or a coarse link with contour in Ω has kernel mismatch ≥ ε_c;
- **(F)** there is a symmetric K ≥ 0 with ||K|| ≤ 1, tr K ≤ C|Ω|, exponentially localised at Ω, such that the real part of the sum
  of the Ω-terms of ΣH is ≤ θ_1⟨v, Kv⟩/2 + C|Ω| and ⟨v, Kv⟩ ≥ c_Fa_1²/g_0².
*What is proven of it:* (F) holds with K = K_Ω, θ_1 = ½ and c_F = 1/(N||C||) whenever max_Ω|A| ≤ min{ρ_*, a_θ} (Lemma SLc,
Corollary SLc-X). Proposition RES shows (P) alone is false, so (F)
is needed.
*Why it is the wall:* (P) ∨ (F) fails exactly when, near b_0, e^AU is a large-amplitude gauge copy of U (no local defect) whose
Feynman energy does not grow with A: a local Gribov copy of the complete gauge fixing χ_U = (h_U, P_res^UD_U^*) inside the chart. Its
absence is the "uniqueness of the slice intersection on the chart" clause of (FP-loc)_0, here required quantitatively and locally,
plus large-amplitude rigidity of the physical directions (a single-scale analogue of HIST's (MSG)).
*Owners:* PROOF NA-FP / (FP-loc) for the gauge part; lane F for the statement. *Weight:* s to P (it is (FP-loc)_0's nonlinear core).
[RSF4-fix SC-1..SC-3 (REVIEW_SF_S4 C-6): **SC-1** in (F), K must be fixed BEFORE v is integrated: read "there is K" as "K belongs to a
family 𝒦(b_0, Ω) fixed in advance, determined by local data, of cardinality ≤ e^{C|Ω|}" (the union over the family costs a local factor), or
K := K_Ω. **SC-2** "the Ω-terms of ΣH" excludes the terms whose pattern straddles ∂Ω; those go to (DX-loc). **SC-3** the chart in this
statement is SF-A2^0's link-wise chart ||1 - U_0U(V)^{-1}||_op ≤ ε^thr_N (≈ ½). On that ½-chart the statement is a moderate-amplitude
Gribov statement that may be false (the reviewer's risk judgement); it is NOT attacked in this form. Session 5 replaces it by Theorem
SLC-sh on the shrunk chart (§16.1), which is PROVEN.]

**Proposition DX (per-site extraction of the deep set): CONDITIONAL ⇐ (SL-coer′) + (FP-loc)_0 + (BGC) (not counted); the
insertion into the expansion is (DX-loc), OPEN.** *Statement as proven.* Let R_* := R_DL + R_c. On the chart, every deep block B lies
within fine distance R_* of either
- (P) a U-variable defect at threshold (τ_c, ε_c), or
- (F) a region Ω with ⟨v, K v⟩ ≥ c_Fa_1²/g_0² and the (F)-bound.
Each defect or region serves at most (2R_* + 1)⁴ blocks. The per-defect factors at stage 0 are:
- a plaquette defect: Wilson positivity, s(W) = N⁻¹Σ_a(1 - cos θ_a) ≥ ||1 - W||²_op/(2N) (exact: ||1 - W||²_op = max_a2(1 - cos θ_a)), so
  the bare integrand carries e^{-u_0τ_c²/(2N)}, up to the background's s(U_p) ≤ ε_bg²/2; **[RSF4-fix DX-1: this line is WRONG as written.**
  Wilson positivity bounds e^{-u_0S(U_0)} absolutely; the expansion's normalisation carries the background action e^{-u_0S(U)} of the
  whole removed region, so the ratio is ≤ e^{-u_0s(p_def) + u_0Σ_{p∈removed}s(U_p)}: the subtraction runs over EVERY plaquette of the
  removed region, here ≳ (2R_DL)⁴ ≳ 10⁴² cubes (1/μ ≈ 2·10¹⁰), not over one plaquette; the same holds for the kernel terms. So
  "τ_c²/(2N) - ε_bg²/2" must read "τ_c²/(2N) - Σ_{removed}s(U_p)", which is negative unless ε_bg ≲ 10⁻²¹τ_c, and (BGC) does not give
  that. The (P)/kernel exponent of a' below is therefore **ARGUED, not proven**. Re-done in session 5: Lemma DX-rel (bounded holes,
  §16.2) and Proposition DX′ (no defect in the deep part at all, §16.1).]**
- a kernel mismatch [RSF4-fix DX-2: the citation "RLARGE branch (i) (PROVEN)" is wrong at stage 0. Branch (i) is a conditional
  probability of V given U with its in-history caveat H-4 ARGUED; stage 0 integrates U_0 at fixed V, so what is needed is the POINTWISE
  kernel-factor bound, which is elementary: Lemma KF (§16.2). The text that follows is kept for the record]: the kernel factor's
  positivity as priced by RLARGE branch (i) (Lemma RS (R3)-(R4); PROVEN, with its in-history
  caveat H-4), e^{-a_ker(ε_c)/g_0²}, a_ker(ε_c) := branch (i)'s exponent at mismatch threshold ε_c (κε_c²/(4N) by RS's ε_1/8 ↔
  κε_1²/(256N)), up to its polynomial prefactor [post-proof: an exponent first written κε_c²/(256N) used the wrong threshold
  conversion; the stage-0 U_0-integrand form of this pricing is part of (DX-loc)];
- an (F)-region: Lemma TILT, e^{-(1-θ_1)c_Fa_1²/(4g_0²)}e^{O(|Ω|)}.
So each deep block carries ≤ e^{-a'/g_0²}, with
  a' := min{τ_c²/(2N) - ε_bg²/2, a_ker(ε_c), (1 - θ_1)c_Fa_1²/4}/(2R_* + 1)⁴ (minus o(1) from the prefactors),
multiplicative over blocks at mutual distance > 2R_*. This replaces session 3's |Λ|-union bound and "mass, not contribution".
*Proof of the inclusion.* For a deep B, Lemma DL and the chart give b_0 within R_DL of B with |A_{b_0}| ≥ a_deep ≥ a_1. Apply (SL-coer′)
at b_0. The multiplicity bound counts blocks within R_* of a point. The factors are the cited bounds. ∎
[RSF4-fix DX-1/DX-2, status: what is proven of DX as stated is the INCLUSION plus the (F)-factor (TILT is a white-noise bound relative
to the Gaussian; the background action cancels). The (P)/kernel exponent of a' is ARGUED (DX-1). Superseded by Proposition DX′ (§16.1).]
*Not written:* (DX-loc), i.e. the deep regions as polymer supports inside CE-Q-col's expansion of the complement, including the
Gaussian/Haar normalisation of the removed region (the e^{B_0}-per-boundary-cube class, (H-w)).
**Restated (CE-Q^∞) after session 4:** = Proposition DX (CONDITIONAL ⇐ (SL-coer′)) + (DX-loc) (OPEN bookkeeping). The wall is
(SL-coer′), i.e. (FP-loc)_0's nonlinear uniqueness clause, localised.

**Circularity check (RLARGE l.319-322) and a non-circular order.**
- *The circle as handed over in session 3.* Branch (ii) ⇐ (SG^fl)_0. (SG^fl)_0 ⇐ "(SF)_0's cluster expansion" (RLARGE l.320-321), which
  includes (CE-Q^∞). Session 3 sent (CE-Q^∞) to branch (ii). That is circular, and **the session-3 note "(CE-Q^∞) → RLARGE §3.2 branch
  (ii) owner" is withdrawn.**
- *Non-circular order (stage 0):*
  - (O1) Theorem CE-Q-col (band) ⇐ (FP-loc)_0 + (BGC). No (SG^fl), no branch.
  - (O2) Proposition DX ⇐ (SL-coer′) + (FP-loc)_0 + (BGC) + RLARGE branch (i) (PROVEN) + bare Wilson positivity + Lemma TILT, plus
    (DX-loc). No (SG^fl), no branch (ii). [RSF4-fix DX-2: delete "RLARGE branch (i) (PROVEN)" from this list; read "the pointwise
    kernel-factor bound (Lemma KF)". RSF4-fix D-1: add **(CH-c)**, the chart complement of SF-A2^0 l.362 ("a fluctuation large field,
    priced elsewhere"), which is branch (ii)'s domain and is assigned NOWHERE in this list; sending it to branch (ii) reopens the circle.
    Restated (CE-Q^∞) = DX + (DX-loc) + (CH-c). Session 5 assigns (CH-c) in §16.3. RSF4-fix D-2: **(DX-loc) may use only (H-w)'s
    B_0-per-cube normalisation parts (a)-(c) (HIST l.536-541: Lemma TD, the E_0 polymer bound, the normalisation mismatch); it may NOT
    use (H-w)'s unreturned-weight sources, which list (PLD) = branches (ii)+(iii) under v2 (HIST l.535-536)**, else the loop returns
    through HIST.]
  - (O3) (SG^fl)_0 ⇐ (O1) + (O2) + N5-sf0 + (G0-1)-(G0-4) (PLD §15.4). [RSF4-fix D-3: add (I_0^E) (the bare representation), (BG)_0
    (background locality, an SF/N2 item) and threshold compatibility (RLARGE l.320-322); none of them consumes branch (ii).]
  - (O4) Branch (ii) at level 1 ⇐ (SG^fl)_0.
  Nothing in (O1)-(O2) consumes (O3)-(O4).
- *Stage k ≥ 1:* (O2_k) prices (P)-defects by RLARGE branch (iii), i.e. CLS-sf in cone form, in place of bare positivity. CLS-sf ⇐ CLS-red ⇐
  (AE) ⇐ (MSG) + (MS-Sob) (RLARGE l.345-353); none of these consumes (SG^fl). (SL-coer′)_k and (FP-loc)_k replace their stage-0
  forms. The order stays non-circular.
- *Threshold note.* τ_c and ε_c join [v2-C]'s threshold list (RLARGE §0). Defects in [τ_c, ε_1) lie inside RLARGE's small-field set, and
  (O2) prices them in-step. [RSF4-fix: "(O2) prices them in-step" was not written anywhere: it is the unassigned region (CH-c). Session 5
  (§16.3) instead imposes (TH-ch) ε_1 ≤ τ_c, which empties [τ_c, ε_1).]
- [RSF4-fix (B-5 minor): at k ≥ 1 the fine halo radius ≈ 4(j + 1)log 2/μ + M ≈ 5.7·10¹⁰(j + 1) meets the torus constraint T_k for the
  last levels (REVIEW_SF_S3 B-7 item 6); recorded in the torus-size caveat.]
- **Owner note for RLARGE (proposed edit, RLARGE not edited by lane F):** read (SG^fl)_k's input "(SF)_k's cluster expansion" as
  "CE-Q-col (band) + Proposition DX (deep part, priced without branch (ii))".

### 13.3 STEP 1 item RT-1: the d ≥ 1 norm thresholds (re-derived; s4 C3-C5)
SF §10.3's displayed condition measures the blocked d ≥ 1 activity at the OUTPUT rate κ = r - 16 log 2. That is SF-blk (3) with the same
κ in and out. In that form the d ≥ 1 norm closes from **κ_c ≥ 1853.49** (s4 C3). The log ratio is +703.57 at 1149.92, so REVIEW_SF_S3's
≈ 1854 and +703.6 are reproduced. [RSF4-fix: this same-rate value is NOT the iteration threshold; cite 2499.39 / 2938.18.]
But the iteration feeds the next stage, and CE-exp-col requires input rate κ_in ≥ κ_c + 16 log 2 + 1296W_3, which is above the output
rate. Measured in the next stage's input class, the exponent is (κ - κ_0)L - 1 - κ_in. The d ≥ 1 norm then closes from
**κ_c ≥ 2499.39** (s4 C4). The difference, κ_0 + 2κ̃_0 + 3 + 32 log 2 + 1296w_8 = 645.90, is κ_in - κ. The rate exponent there is
+2698.9 ≥ 0. **The iteration condition is the second one**; the first is SF-blk's contraction at a fixed rate, which the next
stage cannot accept.
For CE-Q-col (H''_0-dominated Ĥ_0, factor 2 included): rate from **1478.49**; d ≥ 1 norm from **2938.18** (next-input form; 2073.23 in the
displayed form) (s4 C5). Requiring "blocked old part ≤ ½ of the allowed input norm" (so that fresh terms fit) adds log 2 = 0.69 to each
threshold. When the η̂ part dominates Ĥ_0, the band's fresh contribution is a p_0 condition (g-independent), not a κ_c condition.
**RT-1 applied:** Proposition RATE reads "the RATE closes from κ_c ≥ 1149.92; the d ≥ 1 NORM closes from κ_c ≥ 2499.4 (1853.5 in SF's
displayed same-rate form); d < 1 is (SF-irr)". §9.3, §10.3 and §11.1 say "rate" where they said "decay survives".

## 14. Session-4 outcome (written after §13)

### 14.1 Status changes
| item | status | note |
|---|---|---|
| [RSF3-fix] STEP 1 | applied | stale M (2 places), (B1′), §9.1 superseded, Q1, Q2, Q3, Q5, Q6, SN-1, SN-2 ((BGC) explicit), C-1..C-5 wording, 273-route note, RT-1 (§13.3), tally ARGUED 1, s3 low-power labels |
| Lemma HALO | PROVEN-HERE (not counted) | s4 A, with a negative control |
| Lemma SH | PROVEN-HERE (not counted) | s4 B |
| **Theorem CE-Q-col** | analytic part **PROVEN-HERE (counted)**; CONDITIONAL ⇐ (FP-loc)_0 + (BGC) on the integral | **M g-independent**; CE-col route; rate κ_c - κ_0 - 3κ̃_0 - 5; supersedes CE-Q |
| Corollary RATE-Q | PROVEN-HERE (arithmetic; not counted) | κ_c^{Q*} = 1478.49; norm 2938.2 |
| Lemma GD | PROVEN-HERE (not counted) | Fix C-1; shells on Π_UZ per block |
| Lemma DL | PROVEN-HERE (not counted) | deep block ⇒ localised slice field |
| Lemma SLc (+ Corollary SLc-X) | PROVEN-HERE (not counted) | small-amplitude local coercivity, operator form; per-site factor |
| Lemma TILT | PROVEN-HERE (not counted) | s4 D1 |
| **Proposition RES** | **PROVEN-HERE (negative; not counted)** | the reviewer's (SL-coer) wording is false on ker h_U; s4 D2/D3 |
| **(SL-coer′)** | **OPEN, new name; the wall** | = (FP-loc)_0's uniqueness clause, localised + large-amplitude rigidity |
| Proposition DX | CONDITIONAL ⇐ (SL-coer′) + (FP-loc)_0 + (BGC) | per-deep-block e^{-a'/g_0²}; replaces the \|Λ\| union bound |
| (DX-loc) | OPEN, new name (bookkeeping, (H-w) class) | deep regions as polymer supports |
| (CE-Q^∞) | restated = DX + (DX-loc); wall (SL-coer′) | branch-(ii) handoff withdrawn (circular) |
| Proposition RATE | PROVEN-HERE (arithmetic), corrected wording | rate 1149.92; d ≥ 1 norm 2499.4 (RT-1) |

**Tally of this file after session 4 (unreviewed):**
- PROVEN-HERE 34 + 1 standard.
  - Counted 10: SF-J, SF-T0, SF-DC, CE^+, SF-blk, LOC-s, CE-exp, CE-Q (analytic part, with Fix Q1), CE-col, CE-Q-col (analytic part).
  - Not counted 24: the 17 of session 3, plus HALO, SH, GD, DL, SLc, TILT, RES. Corollaries and arithmetic CE-exp-col, RATE, RATE-Q and
    SLc-X are listed, not added.
- CONDITIONAL 7: SF-thr-k; SF-A2^0, CE-exp^0, CE-Q and CE-Q-col as statements on the integral (⇐ (FP-loc)_0 + (BGC)); CE-exp^k; DX.
- ARGUED 1: (CE-s).
- OPEN names:
  - (FP-loc)_k, (N5-reg)_k, (L-loc)_k [B-NA];
  - **(SL-coer′)**, **(DX-loc)**;
  - (CE-col)'s item (iv);
  - (SF-irr) and the A4 items;
  - (a5-G♯)/(G♯-patch), (R♯) at ψ^r [B-NA];
  - lane D: (MIN-reg), (a5-U), (a3-q).
- Discharged this session: the "CE-Q-col" OPEN item (a CE-col version of CE-Q); REVIEW_SF_S3 B-7 (M g-dependence).
- Withdrawn: (SL-coer) in REVIEW_SF_S3's wording (false, RES); the session-3 handoff of (CE-Q^∞) to branch (ii).
- No RLARGE §4.2 row is discharged. No PROOF.md tally change is proposed.
- [RSF4-fix, tally per REVIEW_SF_S4 Part F: DX is CONDITIONAL only as the inclusion + the (F)-factor; DX's (P)/kernel exponent a' is
  ARGUED (DX-1), so ARGUED 2 ((CE-s); DX's a'). GD, DL are CONFIRMED-WITH-FIX (constants restated in place). New OPEN names recorded:
  **(CH-c)** (the chart complement of SF-A2^0 l.362; branch (ii)'s domain; unassigned after session 4) and **(DX-rel)** (relative pricing of
  a defect by its local excess over the background). (DX-loc) is restricted by D-2 (no (H-w) weight sources).]

### 14.2 What (SF^J)_0 now rests on
- **A2:** ⇐ (FP-loc)_0 + (BGC).
- **A3 band:** ⇐ (FP-loc)_0 + (BGC) (CE-exp^0, CE-Q-col), with g-independent M and p_0.
- **A3 deep:** ⇐ (SL-coer′) + (DX-loc), priced per site without branch (ii). Both sit inside (FP-loc)_0's nonlinear gauge-fixing
  content, plus the (H-w)-class bookkeeping.
- **A4:** large polymers PROVEN (SF-blk); d ≥ 1 norm closes from κ_c ≈ 2.5·10³ (2.94·10³ with the band); small polymers ⇐ (SF-irr).
- **Across levels:** the band expansion now composes in rate (CE-Q-col, from κ_c ≥ 1478.5). The k ≥ 1 activity input is (L-loc)_k (B-NA
  wall), plus item (iv).

### 14.3 Check s4
Criteria checks/s4_criteria.md: born 05:22:00 UTC (md5 06c44d6a…), before the script (born 05:24:27 UTC). Script checks/s4_sf.py
(md5 fa1fcd37…). Output checks/s4_out.txt (md5 1cd744d2…). Record checks/s4_time.txt.
One run under the numeric lock, 05:25:24-05:25:32 UTC: load 5.87, nice 10, BLAS threads 1, 7.5 s, peak RSS 257 MB, exit 0, one rmdir.
**OVERALL PASS 21/21.**
- Evidential: A1-A5, A7 (negative control, found 139 violations of the stronger claim), B1-B2, D1-D2.
- Non-vacuity: A6, B3.
- Control: D3.
- Arithmetic: C1-C8.
- Low-power, recorded:
  - D1 tests an elementary inequality, and its plain Monte Carlo has infinite variance at θ = 0.9; the exact-tilt reference agrees.
  - D2's plaquette identity is construction-level; its evidential part is the existence of non-small zeros of h∘A.
  - C4 and C5 are formulas evaluated, not checks of the iteration logic.

# SESSION 5 (2026-10-28 UTC). Inputs read before 06:11 UTC: REVIEW_SF_S4.md (BINDING; in full; md5 1b9d442f…), SF.md (e6835ab9…,
= SF_LOG's session-4 final), SF_LOG.md (931bca87…), HIST.md 468e9f03… (§20.0-§20.2: (F1)-(F6), Theorem MSG, Corollaries MSG-loc′ and
MSG-loc, l.1182-1306; (H-w) l.526-541), PROOF.md 4a7bbccc… (Lemma FP-ab + application l.2443-2492; Proposition PG^{(k)} l.2969-2985;
NA-alg, NA-crit, NA-inv, Proposition NA-FP l.2995-3084; Setting N5-bg, Lemma N5-cov l.5255-5284), RLARGE.md 24a73553… (l.300-332),
PLD.md (§15.2 l.966-1024, §15.4 l.1104-1146).

## 15. PRE-STATED (session 5) (appended at 06:15 UTC, 2026-10-28, BEFORE any session-5 proof, before the [RSF4-fix] edits and before the s5 criteria)

### 15.0 Conventions for §15-§17
Stage 0; real background U := U(V) (BR1) with (BGC); V fixed; U_0 the integrated fine field. 𝒢_V := {g : sites → SU(N), g(c_X) = 1 ∀X},
acting by (g·U_0)_b := g(x)U_{0,b}g(y)^{-1}, b = (x, y); the integrand is 𝒢_V-invariant. Left-trivialised field A_b := log(U_{0,b}U_b^{-1})
(principal log). |·| is the HS norm, ||·|| the operator norm; |A|_∞ := max_b|A_b|; for a site field λ, ||λ||_{B∞} := max_X(Σ_{x∈B(X)}|λ(x)|²)^{1/2}.
h := (L - 1)/2; A_d := (d - 1)L(L - 1)/2 (HIST MSG); (F1)-(F5) = HIST §20.0. hol_W(γ) := the ordered product of the link variables of W
along γ (W(x→x') = W_b forward, W_b^{-1} backward); γ_x := the block-internal axial path (order 0, …, d - 1) from c_X to x ∈ B(X).
**Event E_good(τ):** (E1) ||1 - U_{0,p}|| ≤ τ for every fine plaquette p; (E2) ||V_c - W_0(M̄_c(U_0))|| ≤ τ for every coarse link c.
ε_bg := the maximum of the same two quantities for the background U (finite under BR1 (iii); a smallness hypothesis below).
[RSF5-fix CH-3 (scope): E_good presupposes a V-EVENT, and ε_bg must be LOCAL. V is cut only on level-1 cube interiors, so level-1
inter-cube plaquettes of V can be rough (the level-(k+1) [v2-E8] event, about the N5 background); near such a V-plaquette U(V) is not
ε_bg-small and FP-sh's hypothesis ε_bg ≤ τ_c/2 fails there. So **(SF)_0 is stated on a V-event 𝒱^sf(Λ′)** (every level-1 plaquette of V
on Λ′ is < ε_1; this matches (SG^fl)'s domain, PLD l.1144-1146), with **ε_bg := the max over Λ′ only**. The rough-V complement is
RLARGE's level-1 defect pricing, not SF's (CH-c). The localised GF-dec / FP-uniq on Λ′ (and a local form of BR1, whose (i) is stated
with the global ε_V) go into (DX-loc), next to the frozen-hole complement already there.]

### 15.1 STEP 2: the reviewer's reduction of (SL-coer′) (REVIEW_SF_S4 C-6), made precise
*Idea fixed before writing (exploratory, unwritten):* (i) MSG's one-step construction with the background U in place of the interpolated
reference exp(Ia) is block-local and keeps g(c_X) = 1, so it is already an element of 𝒢_V; it needs no box at all, only the block pair of
each link: this is the one-scale case of MSG; (ii) χ_UΓ is block-diagonal except for the residual Laplacian G_res := P_resD_U^*D_UP_res,
whose gap follows from λ(c_X) = 0 alone (telescoping along axial paths), for every background; a Neumann series then gives exponential
decay with an explicit rate; (iii) a sup-norm contraction then gives existence AND uniqueness of the χ_U-representative near the axial one;
(iv) the 't Hooft average must be truncated per block (an exact change of the gauge-fixing weight), otherwise large ω has no nearby zero;
the truncation costs only a c-number and is invisible on the band; (v) on the resulting chart every deep block is priced by SLc + TILT
relative to the white-noise reference, so no defect and no background action enters DX; defects appear only in the complement of
E_good, which is a union of LOCAL events with bounded holes.
- **Lemma MSG_0 (one-scale, block-local small-field gauge; the stage-0 case of Theorem MSG).** Let τ satisfy (S0): (4A_d + 4)τ ≤ ½,
  18.8NA_d²τ ≤ 1 (MSG's (S2)) and 1.011√NA_dτ ≤ 1/20. Put **g_ax(x) := hol_U(γ_x)^{-1}hol_{U_0}(γ_x)** (x ∈ B(X)); g_ax ∈ 𝒢_V, and on B(X)
  it depends only on U_0 and U on B(X). Let b = (x, y), x ∈ B(X), y ∈ B(Y). If (E1) holds at level τ for U_0 and for U on every plaquette
  of B(X) ∪ B(Y), and, when X ≠ Y, (E2) holds at level τ for U_0 and for U at c = (X, Y), then
    ||(g_ax·U_0)_b - U_b|| ≤ 2A_dτ (X = Y),  ≤ (4A_d + 4)τ (X ≠ Y);  hence |A^0_b|_op ≤ C_0τ, C_0 := 1.011(4A_d + 4),
  A^0 := log((g_ax·U_0)U^{-1}) (the axial representative). A^0 is a function of the 𝒢_V-orbit of U_0 only. (d = 4, L = 3: C_0 = 40.44.)
  *Planned: PROVEN-HERE ⇐ Theorem MSG steps (2)-(4) [HIST, PROVEN], (F1), (F4), RS (R1), NA-alg (a) (a specialisation; not counted).*
  *Expected failure mode if mis-derived:* a root not at c_X (g(c_X) ≠ 1) leaves 𝒢_V; a global axial gauge makes C_0 grow with the box.
- **Lemma W-Lip (Lipschitz bound of the kernel centre).** If the background's contour spreads at c are ≤ 1/40 and |A|_∞ ≤ ρ with
  2√N(6L - 4)ρ ≤ 1/40, then ||W_0(M̄_c(e^AU)) - W_0(M̄_c(U))|| ≤ C_Wρ, C_W := L + 3.8√N(6L - 4). *Planned: PROVEN-HERE ⇐ NA-alg (a)'s
  contraction (not counted).*
- **Lemma GF-dec (explicit inverse of χ_UΓ; exponential locality; every real background).** (a) M_U is block-diagonal and
  σ_min(M_U|_{Λ_X}) ≥ L^{-d}, so M_U^+ := M_U^T(M_UM_U^T)^{-1} is block-diagonal with ||M_U^+|| ≤ L^d; Λ_res^U = ⊕_XΛ_{res,X} and P_res^U is
  block-diagonal. (b) **||D_Uλ||² ≥ c_D||λ||² on Λ, c_D := 1/(dhL^d)**, and ||D_U||² ≤ 4d. (c) G_res := P_res^UD_U^*D_UP_res^U on Λ_res^U has
  spectrum in [c_D, 4d] and block range 1, hence **||G_res^{-1}(X, Y)|| ≤ q^{|X-Y|_∞}/c_D**, q := (4d - c_D)/(4d + c_D), m_FP := -log q.
  (d) **(χ_UΓ)^{-1}(η, ω) = M_U^+η + G_res^{-1}(ω - P_res^UD_U^*D_UM_U^+η)** (Γ := D_U|_Λ; χ_UΓλ = (M_Uλ, P_res^UD_U^*D_Uλ) by NA-FP (i)).
  (e) **G_∞ := sup_XΣ_Y||(χ_UΓ)^{-1}(X, Y)|| ≤ L^d + c_D^{-1}S_d(q)(1 + 4d·3^dL^d)**, S_d(q) := Σ_{D≥0}((2D + 1)^d - (2D - 1)_+^d)q^D.
  Every constant is background-independent (no smallness of U is used). *Planned: PROVEN-HERE ⇐ NA-FP (i)-(ii) (not counted).*
  *Expected failure mode:* if the gap of G_res needed U ≈ 1, c_D would carry an ε_bg-dependence; the telescoping in (b) should avoid it.
- **Lemma BCH-L (explicit BCH remainder).** g(X, Y, Z) := log(e^Xe^Ye^Z) - X - Y - Z. For P = (X, Y, Z), P′ with ℓ¹ operator size
  ≤ r ≤ s_1 := 0.3: ||g(P) - g(P′)|| ≤ c_gr·|P - P′|_{ℓ¹}, c_g := G(0.6)/0.09, G(s) := s - log(2 - e^s) (c_g ≈ 25.9); in HS norms the
  constant is c′_g := √Nc_g. *Planned: PROVEN-HERE (Cauchy + Schwarz; not counted).*
- **Proposition FP-uniq (the χ_U-representative: existence and uniqueness, sup-norm, volume-independent).** Put X_∞ := 2dL^{d/2},
  q_∞ := G_∞X_∞. Let U_0 have axial representative with |A^0|_∞ ≤ s_0 (HS), ω ∈ Λ_res^U with ||ω||_{B∞} ≤ ζ, and r > 0 with
  (I1) 2c′_gq_∞(s_0 + 2r) ≤ ½, (I2) 2G_∞(X_∞s_0 + ζ) ≤ r, (I3) s_0 + 2r ≤ 0.3. Then λ ↦ Φ_ω(λ) := χ_U(log((e^λ·(g_ax·U_0))U^{-1})) - (0, ω)
  has exactly one zero λ_* in {λ ∈ Λ : ||λ||_{B∞} ≤ r}; ||λ_*||_{B∞} ≤ r_* := 2G_∞(X_∞s_0 + ζ), and the representative A_* obeys
  |A_*|_∞ ≤ r_sol := (s_0 + 2r_*)(1 + c′_g(s_0 + 2r)). If also (I4) 1.011√NL^{d/2}dh(r_sol + s_0) ≤ r and dh(r_sol + s_0) ≤ ½, then every
  A′ on the 𝒢_V-orbit with h_U(A′) = 0, P_res^UD_U^*A′ = ω and |A′|_∞ ≤ r_sol equals A_*. *Planned: PROVEN-HERE ⇐ GF-dec, BCH-L, MSG_0
  (not counted).*
- **Proposition FP-sh (exact gauge-fixed representation on E_good; the uniqueness clause of (FP-loc)_0 on the shrunk chart).** Let
  τ_c > 0 with (S0) and ε_bg ≤ τ_c/2, s_0 := √NC_0τ_c, and ζ, r with (I1)-(I4). Let γ̃ := Π_Xγ̃_X, γ̃_X the centred Gaussian on Λ_{res,X} of
  covariance (N/u_0)1 conditioned on |ω_X| ≤ ζ. For every measurable 𝒢_V-invariant I ≥ 0 supported in E_good(τ_c):
    ∫IΠ_bdU_0(b) = c_N^{#b}∫I(e^AU)Π_bj(A_b)·1{|A|_∞ ≤ r_sol}·Δ(A)·δ(h_U(A))·γ̃(P_res^UD_U^*A)dA,
  Δ(A) := |det(χ_U∘𝔇_A)|, 𝔇_A := d/dλ|_{λ=0} log((e^λ·e^AU)U^{-1}) (𝔇_0 = -Γ), and γ̃(P_resD^*A) = Z_ζ^{-1}e^{-(u_0/2N)||P_resD_U^*A||²}Π_X1{|(P_resD_U^*A)_X| ≤ ζ},
  Z_ζ a c-number, Z_ζ = Π_X(1 - p_X)·(Gaussian normalisation), p_X ≤ 2^{m_X/2}e^{-u_0ζ²/(4N)}. No Gribov copy enters. *Planned: PROVEN-HERE ⇐
  FP-uniq + Haar invariance + Fubini (not counted).* What then remains of (FP-loc)_0 on E_good is **(FP-det)**: log(Δ(A)/Δ(0)) is a local
  analytic polymer function of A on {|A|_∞ ≤ r_sol} with decay rate m_FP [named; expected ARGUED: a walk expansion of tr log(1 + K),
  K := (χ_UΓ)^{-1}χ_U(𝔇_A - 𝔇_0), with GF-dec's decay].
- **Theorem SLC-sh ((SL-coer′) on the shrunk chart).** If r_sol ≤ min{ρ_*, a_θ}, then for every real slice field A with |A|_∞ ≤ r_sol,
  every link b_0 and every fixed set Ω ∋ b_0, (F) holds with **K := K_{Ω^+} fixed before v** (Ω^+ := Ω ∪ the links of every action term,
  Jacobian and contour pattern meeting Ω), θ_1 := 2(C_coer r_sol + C′g_0²) ≤ ½ and c_F := 1/(N||C||); (P) is not needed. This meets SC-1
  (K fixed in advance), SC-2 (straddling terms are inside Ω^+) and SC-3 (the chart is |A|_∞ ≤ r_sol, stated). *Planned: PROVEN-HERE ⇐
  SLc, SLc-X (not counted).*
- **Proposition DX′ (per-deep-block extraction on the shrunk chart; corrected pricing).** Re-tune the band edge with ρ_* replaced by
  ρ_band := min{ρ_*, τ_c/(2C_W), s_0/(√NX_∞)} (so the band lies in E_good(τ_c), in {|A|_∞ ≤ r_sol} and in the support of γ̃). Then every deep
  block B lies within fine distance R_sh := μ^{-1}log(r_sol/a_sh) of a link with |A_b| ≥ a_sh, a_sh := (a_deep with ρ_* → ρ_band and the
  DL-1 factor), and for every fixed deep pattern 𝔅 the deep part carries
    ≤ exp(C_Ω|Ω(𝔅)|)·e^{-|𝔅|a′/g_0²},  a′ := a_sh²/(8N||C||m_sh), m_sh := (2R_sh/L + 3)^d,
  Ω(𝔅) := the fixed R_sh-neighbourhood of 𝔅, C_Ω explicit (TILT's determinant and SLc's linear source). **No plaquette or kernel defect and
  no background action enters a′** (the bound is relative to the white-noise reference). Defects are priced only on E_good^c ((CH-c),
  §15.2), with BOUNDED holes. *Planned: CONDITIONAL ⇐ FP-sh + (FP-det) + (BGC) + (TH-ch) (inclusion and factor PROVEN-HERE; the
  insertion is (DX-loc)).*
- **Lemma KF (pointwise kernel factor; DX-2).** For M = S·Σ_jw_je^{Y_j} (S ∈ SU(N), |Y_j| ≤ y ≤ 1/20, w_j ≥ 0, Σw_j = 1) and V ∈ SU(N):
  **φ(V; M) ≥ ||V - W_0(M)||²/(4N) - 1354.3y⁴** and φ(V; M) ≤ ||V - W_0(M)||; hence n_c(M) := ∫e^{-u_0κ_0φ(V;M)}dV ≥ e^{-1}c′_N(u_0κ_0)^{-(N²-1)}
  (c′_N > 0 depending only on N). *Planned: PROVEN-HERE ⇐ NA-alg (a), SF-J (not counted).*
- **Lemma DX-rel (relative pricing of a defect hole; DX-1 corrected).** Let D ≠ ∅ be a set of defects (plaquettes with ||1 - U_{0,p}|| > τ_c;
  coarse links c with mismatch > τ_c whose block pair has all plaquettes ≤ τ_c), and R(D) the fine links of the blocks within coarse
  ℓ^∞ distance 1 of the blocks carrying D (the hole; ≤ n_R|D| links, n_R := d·3^dL^d). The U_0-integrand on R(D), divided by its background
  value, is ≤ Π_{δ∈D}e^{-u_0a_δ}·exp(u_0Σ_{p∈𝒫(R(D))}s(U_p))·(C_Ku_0^{N²-1})^{#𝒦(R(D))}, a_p := τ_c²/(2N), a_c := κ_0(τ_c²/(4N) - 1354.3y_c⁴),
  with the subtraction over the plaquettes 𝒫(R(D)) of the BOUNDED hole only (≤ n_1|D| plaquettes, n_1 := 2(d - 1)n_R, each s(U_p) ≤ ε_bg²/2).
  Under **(TH-bg)** n_1ε_bg² ≤ min{a_p, a_c}: per defect ≤ e^{-u_0min{a_p,a_c}/2}(C_Ku_0^{N²-1})^{n_K}. The Gaussian/FP normalisation of the hole
  and the factorisation across ∂R(D) are (DX-loc), which uses only (H-w)'s normalisation parts (a)-(c) (REVIEW_SF_S4 D-2). *Planned:
  PROVEN-HERE as an inequality of the hole integrand (not counted).*

### 15.2 STEP 3: (CH-c), its assignment, and the exact dependency order
- **(CH-c) (session-5 form).** The stage-0 integration domain minus E_good(τ_c). (SF-A2^0's ½-chart is replaced by FP-sh.)
- **(TH-ch) (threshold compatibility; added to [v2-C]'s list).** ε_1 ≤ τ_c and every RLARGE stage-0 small-field threshold (the cube-interior
  plaquette cut ε_1; the soft-residual / kernel-mismatch threshold of (G0-3)) is ≤ τ_c; with (TH-bg) and ε_bg ≤ τ_c/2.
- **Proposition CH-assign.** Under (TH-ch), (CH-c) meets RLARGE's stage-0 small-field set only through the inter-cube [v2-E8] event and the
  ∂Λ(𝔥)-adjacent plaquettes. So (CH-c) consists of RLARGE level-0 large-field events: cut-bad cubes (the history), the [v2-E8] event,
  above-threshold kernel mismatches (branch (i); at stage 0 the pointwise bound KF, DX-2). **None of it lies in branch (ii)'s domain**
  (fluctuation plaquette defects at τ ≤ ε_1 inside cut-good regions, where E_good holds). If some small-field threshold exceeds τ_c, the
  defects in (τ_c, threshold] are in-step and are priced by DX-rel, NOT by branch (ii): pricing them by branch (ii) is circular, because
  (SG^fl)_0 is an expectation over the whole cut-good fixed-V law, which contains them. *Planned: PROVEN-HERE (set inclusion + the
  circularity argument; not counted).* *Expected failure mode:* if (TH-ch) were incompatible with (TH-bg) or with FP-uniq's radius chain,
  the band (τ_c, ε_1] could not be emptied; s5 F checks that the chain is consistent.
  [RSF5-fix CH-1/CH-2/TH-1 (pre-statement record kept; the corrected forms are in §16.3 and govern): the routing "[v2-E8] event → RLARGE"
  and "∂Λ(𝔥)-adjacent plaquettes → HIST boundary terms" is WITHDRAWN (REVIEW_SF_S5 D-2, D-3); (TH-ch) is strengthened to TH-1's min
  (§16.3); (CH-c) is CONDITIONAL, not assigned.]
- **Dependency order (to be written in §16.3, exact):** O0 background/thresholds → O1 MSG_0, GF-dec, BCH-L, FP-uniq, FP-sh (⇐ (FP-det)) →
  O2 CE-Q-col (band, re-tuned) → O3 DX′ + (DX-loc) → O4 (CH-c) (RLARGE large-field events; DX-rel for any in-step band) → O5 (SG^fl)_0 →
  O6 branch (ii). Nothing in O0-O4 consumes O5-O6.

## 16. Session-5 proofs (written from 06:27 UTC; after §15 (06:15:49 UTC), after the s5 criteria (06:16:32 UTC), after the single s5 run (06:21:27-06:21:43 UTC) and after the [RSF4-fix] edits (06:22-06:24 UTC); corrections made while proving are marked [post-proof])

### 16.1 STEP 2: the shrunk-chart reduction

**Lemma MSG_0: PROVEN-HERE (a specialisation of Theorem MSG; not counted).** *Proof.* (1) γ_{c_X} is empty, so g_ax(c_X) = 1 and
g_ax ∈ 𝒢_V; γ_x ⊂ B(X), so g_ax on B(X) reads only U_0, U on B(X). (2) For any W and gauge g, hol_{g·W}(γ : z → z′) = g(z)hol_W(γ)g(z′)^{-1}.
With π := γ_xbγ_y^{-1} (a path c_X → c_Y): (g_ax·U_0)_b = hol_U(γ_x)^{-1}hol_{U_0}(γ_x)U_{0,b}hol_{U_0}(γ_y)^{-1}hol_U(γ_y) = hol_U(γ_x)^{-1}hol_{U_0}(π)hol_U(γ_y),
and U_b = hol_U(γ_x)^{-1}hol_U(π)hol_U(γ_y). Unitary invariance gives **||(g_ax·U_0)_b - U_b|| = ||hol_{U_0}(π) - hol_U(π)||**. This is MSG step (2)
with the reference field exp(Ia) replaced by the background U (and MSG's convention U^g = g^†Ug transposed to ours). (3) X = Y: π is a
closed loop at c_X spanned by a ladder of ≤ Σ_{ν>μ}|x_ν - c_ν| ≤ (d - 1)h ≤ A_d plaquettes of B(X) (MSG step (3)). (F4) gives
||1 - hol_W(π)|| ≤ A_dτ for W = U_0 and W = U, so the difference is ≤ 2A_dτ. (4) X ≠ Y: MSG step (4) verbatim, for W = U_0 and W = U
separately: deforming π to the centre segment S_c costs a ladder of ≤ (d - 1)hL = A_d plaquettes in B(X) ∪ B(Y), so ||hol_W(π) - hol_W(S_c)||
≤ A_dτ; and ||hol_W(S_c) - V_c|| ≤ ||hol_W(S_c) - M̄_c(W)|| + ||M̄_c(W) - W_0(M̄_c(W))|| + ||W_0(M̄_c(W)) - V_c|| ≤ A_dτ + 18.4y² + τ ≤ (A_d + 2)τ, by RS (R1)
(each contour differs from S_c by a ribbon of ≤ A_d plaquettes in B(X) ∪ B(Y)), NA-alg (a) with y := 1.011√NA_dτ ≤ 1/20, and (E2); (S2)
gives 18.4y² ≤ τ. Hence ||hol_{U_0}(π) - hol_U(π)|| ≤ 2A_dτ + 2(A_d + 2)τ = (4A_d + 4)τ. (5) ||1 - (g_ax·U_0)_bU_b^{-1}|| = ||(g_ax·U_0)_b - U_b||
≤ ½ by (S0), so (F1) gives |A^0_b|_op ≤ 1.011(4A_d + 4)τ = C_0τ. (6) For g′ ∈ 𝒢_V, hol_{g′·U_0}(γ_x) = hol_{U_0}(γ_x)g′(x)^{-1} (g′(c_X) = 1), so
g_ax(g′·U_0) = g_ax(U_0)g′^{-1} pointwise and g_ax(g′·U_0)·(g′·U_0) = g_ax(U_0)·U_0: A^0 is a function of the orbit. ∎
*Reading.* No box is used: the "bounded box" of REVIEW_SF_S4 C-6 is the block pair B(X) ∪ B(Y) of each link, and the recursion over
levels (MSG step (6)) is not needed at one scale. The gauge is the one-step MSG gauge with the background as reference; this is why it
stays in 𝒢_V and why C_0 does not grow with the volume. (s5 A, criteria first: d = 2 (4×4 blocks) and d = 3 (2×2×2 blocks), SU(2),
amplitudes 10⁻³-2·10⁻²: A1 intra-block bound 0/1440 violations, max ratio 0.221; A2 the ladder part of step (4) 0/1440, max ratio 0.839;
A3 identity (2) to 5·10⁻¹⁶; A4 locality exact (0.0, 20 trials); A5 orbit invariance to 1.8·10⁻¹⁵; **negative control A7:** with the root
at a block corner (g(c_X) ≠ 1) the orbit invariance fails by 1.93. The RS (R1)/NA-alg part of step (4) is cited, not tested.)

**Lemma W-Lip: PROVEN-HERE (not counted).** *Proof.* Write M̄_c(W) = hol_W(S_c)·m(W), m(W) := avg_jhol_W(S_c)^{-1}hol_W(T_j) = avg_je^{Y_j(W)},
and use the left covariance W_0(Sm) = SW_0(m) (S ∈ SU(N): Re tr(W^{-1}Sm) = Re tr((S^{-1}W)^{-1}m)). With W′ := e^AU: S_c has L links and every
contour ≤ 5L - 4 links (PROOF l.3469), and ||hol_{W′}(γ) - hol_U(γ)|| ≤ (#links)·max_b||e^{A_b} - 1|| ≤ (#links)ρ. So ||hol_{W′}(S_c) - hol_U(S_c)|| ≤ Lρ
and, by (F3) (both loops within ½ of 1), |Y_j(W′) - Y_j(U)|_op ≤ 2(6L - 4)ρ, i.e. δ := max_j|Y_j(W′) - Y_j(U)|_HS ≤ 2√N(6L - 4)ρ ≤ 1/40, so both
spreads are ≤ y′ := 1/20. In NA-alg (a)'s fixed-point form X = Φ_Y(X) := Ȳ + Π(K_Y(X)), K_Y = R_X + E_Y + (R_X - X)(Ȳ + E_Y), on B := {|X| ≤ 3y′}:
|E_Y - E_{Y′}| ≤ (e^{y′} - 1)δ ≤ 0.052δ, |R_X - X| ≤ 5.23y′² + 3y′ ≤ 0.163, so |Φ_Y(X) - Φ_{Y′}(X)| ≤ 1.052·1.163δ ≤ 1.224δ; Lip(Φ_Y) ≤ 4.5y′ ≤ 0.23. The two
fixed points obey |X_0 - X_0′| ≤ 0.23|X_0 - X_0′| + 1.224δ, so |X_0 - X_0′| ≤ 1.59δ, and ||e^{X_0′} - e^{X_0}|| ≤ e^{0.15}·1.59δ ≤ 1.86δ. Altogether
||W_0(M̄_c(W′)) - W_0(M̄_c(U))|| ≤ Lρ + 1.86·2√N(6L - 4)ρ ≤ C_Wρ, C_W = L + 3.8√N(6L - 4) (d = 4 independent; L = 3, N = 3: 95.15). ∎

**Lemma GF-dec: PROVEN-HERE (not counted).** *Proof.* (a) M_Uλ(X) averages Ad(T^σ)λ(y) over y ∈ B(X) and axial paths inside the box B(X),
so it reads λ on B(X) only: M_U = ⊕_XM_X, hence Λ_res^U = ⊕_Xker M_X and P_res^U = ⊕_XP_X. For y = c_X + e_μ every axial path is the single
link b, so M_X(vδ_y) = L^{-d}Ad(U_b)v (NA-FP (ii)'s proof). For w ∈ su(N), with v := Ad(U_b)^{-1}w: |M_X^Tw| ≥ ⟨w, M_X(vδ_y)⟩/|v| = L^{-d}|w|.
So M_XM_X^T ≥ L^{-2d} and ||M_X^+|| ≤ L^d. (b) For λ ∈ Λ and y ∈ B(X) take one axial path P: c_X → y, |P| ≤ dh. NA-FP (i)'s telescoping gives
ℓ_P(D_Uλ) = Ad(T_P)λ(y) - λ(c_X) = Ad(T_P)λ(y), and |ℓ_P(A)| ≤ Σ_{b∈P}|A_b| (Ad is an isometry). So |λ(y)|² ≤ dhΣ_{b∈P}|(D_Uλ)_b|². Each
block-internal link lies on at most L^d of these paths, so Σ_{y∈B(X)}|λ(y)|² ≤ dhL^dΣ_{b⊂B(X)}|(D_Uλ)_b|²; summing over X, **||λ||² ≤ dhL^d||D_Uλ||²**.
And ||D_Uλ||² ≤ Σ_b2(|λ(x)|² + |λ(y)|²) = 4d||λ||². Nothing about U is used. (c) For λ ∈ Λ_res^U ⊂ Λ, ⟨λ, G_resλ⟩ = ||D_Uλ||² ∈ [c_D, 4d]·||λ||², and
G_res maps Λ_res^U to itself. P_res^U is block-diagonal and D_U^*D_U couples only nearest-neighbour sites, so G_res(X, Y) = 0 for |X - Y|_∞ > 1.
With c := (c_D + 4d)/2, ||1 - G_res/c|| ≤ q on Λ_res^U, G_res^{-1} = c^{-1}Σ_{n≥0}(1 - G_res/c)^n, and the n-th term has block range ≤ n. So
||G_res^{-1}(X, Y)|| ≤ c^{-1}Σ_{n≥|X-Y|}q^n = q^{|X-Y|}/(c(1 - q)) = q^{|X-Y|}/c_D. (d) Let λ_0 := M_U^+η ∈ Λ and λ_r := G_res^{-1}(ω - P_resD_U^*D_Uλ_0) ∈ Λ_res^U.
Then M_U(λ_0 + λ_r) = η (M_Uλ_r = 0) and P_resD_U^*D_U(λ_0 + λ_r) = P_resD_U^*D_Uλ_0 + G_resλ_r = ω. By NA-FP (i) and λ(c) = 0, χ_UΓ = (M_U, P_resD_U^*D_U)
on Λ; it is injective with matching dimensions (NA-FP (ii)), so this is its inverse. (e) The η-column of (χ_UΓ)^{-1}(X, ·) is M_X^+δ_{XY} plus
-G_res^{-1}P_resD_U^*D_UM_U^+, whose block row sum is ≤ (c_D^{-1}Σ_Zq^{|X-Z|})·3^d·4d·L^d (range 1, ≤ 3^d neighbours, entries ≤ ||D_U^*D_U|| ≤ 4d,
||M^+|| ≤ L^d); the ω-column has row sum ≤ c_D^{-1}Σ_Zq^{|X-Z|}; and Σ_Zq^{|X-Z|_∞} ≤ S_d(q). So G_∞ ≤ L^d + c_D^{-1}S_d(q)(1 + 4d·3^dL^d). ∎
*Numbers (s5 F1, ARITHMETIC; d = 4, L = 3):* c_D = 1/324 = 3.086·10⁻³, q = 0.999614, **m_FP = 3.858·10⁻⁴ per block**, S_4(q) = 1.733·10¹⁶,
**G_∞ ≤ 5.90·10²³**, X_∞ = 72. (s5 B, criteria first, d = 2, SU(2) adjoint, 5×5 and 4×4 blocks, backgrounds U = 1, Haar-random
(not small) and smooth: B1 λ_min(Γ^TΓ)/c_D = 7.9-14.8; B2 ||D_U||² ≤ 8.000; B3 σ_min(M_X)L^d = 2.06-2.83, off-block entries exactly 0; B4
max ||G_res^{-1}(X, Y)||c_D/q^{|X-Y|} = 0.026-0.035; B5 the inverse formula to 3·10⁻¹⁵, and h_U(D_Uλ) = M_Uλ to 4·10⁻¹⁶. B6 (report): the
measured decay is 1.0-2.1 per block against the bound's m_FP = 1.39·10⁻² at d = 2: the bound is very conservative.)
*Reading.* The gap comes from λ(c_X) = 0 (a Dirichlet point per block), not from Λ_res's mean-zero condition and not from smallness of
the background. So the residual-gauge inverse is exponentially local for EVERY background; this is the "N5/FP_U-type item" of
REVIEW_SF_S4 C-6 (2)-(3), at one scale, without any assumption.

**Lemma BCH-L: PROVEN-HERE (not counted).** *Proof.* For complex X, Y, Z with |X| + |Y| + |Z| ≤ 0.6 (operator norms),
||e^Xe^Ye^Z - 1|| ≤ e^{0.6} - 1 = 0.822 < 1, so log(e^Xe^Ye^Z) is given by the convergent series and |g| ≤ -log(2 - e^{0.6}) + 0.6 = G(0.6) = 2.327. g is
analytic there, g(0) = 0 and Dg(0) = 0. For Q with ℓ¹-size ≤ s_1 = 0.3 and a direction H of ℓ¹-size 1, u ↦ g(Q + uH) is analytic on
|u| ≤ s_1 and bounded by G(0.6), so |Dg(Q)H| ≤ G(0.6)/s_1 (Cauchy). For P of size ≤ s_1, t ↦ Dg(tP/|P|)H is analytic on |t| ≤ s_1, vanishes at
t = 0 and is bounded by G(0.6)/s_1, so (Schwarz) |Dg(P)H| ≤ G(0.6)|P|/s_1² = c_g|P|. Integrate along the segment from P′ to P (it stays in the
ball of radius r): ||g(P) - g(P′)|| ≤ c_gr|P - P′|. HS: ||·||_HS ≤ √N||·|| and |·|_op ≤ |·|_HS give c′_g = √Nc_g. ∎ (c_g = 25.85. s5 C1: 2080
pairs in su(2), su(3), r ∈ {10⁻³, 10⁻², 0.1, 0.3}: 0 violations; C2: the measured ratio is ≤ 0.546.)

**Proposition FP-uniq: PROVEN-HERE (not counted).** *Proof.* (1) Since e^{λ(x)}(g_ax·U_0)_be^{-λ(y)}U_b^{-1} = e^{λ(x)}e^{A^0_b}e^{-Ad(U_b)λ(y)},
  A(λ)_b = A^0_b - (D_Uλ)_b + R(λ)_b,  R(λ)_b := g(λ(x), A^0_b, -Ad(U_b)λ(y)),
because g(0, A^0_b, 0) = 0. Hence Φ_ω(λ) = χ_U(A^0) - (0, ω) - χ_UΓλ + χ_U(R(λ)), and Φ_ω(λ) = 0 ⟺ λ = T(λ) := (χ_UΓ)^{-1}[χ_U(A^0) - (0, ω) + χ_U(R(λ))]
(T maps into Λ). (2) Norms: |h_U(A)(X)| ≤ dh|A|_∞ (each ℓ_P has ≤ dh terms) and |(P_res^UD_U^*A)_X| ≤ |D_U^*A|_{ℓ²(B(X))} ≤ L^{d/2}·2d|A|_∞; so
both components of χ_U(A) at X are ≤ X_∞|A|_∞, and by GF-dec (e) ||(χ_UΓ)^{-1}(η, ω)||_{B∞} ≤ G_∞max_Ymax{|η_Y|, |ω_Y|}. (3) For λ, λ′ in the ball
B_r := {||λ||_{B∞} ≤ r}: ||λ||_∞ ≤ r, each triple has ℓ¹-size ≤ s_0 + 2r ≤ 0.3 (I3), and Ad is an isometry, so by BCH-L
|R(λ)_b - R(λ′)_b| ≤ 2c′_g(s_0 + 2r)||λ - λ′||_∞. So Lip(T) ≤ G_∞X_∞·2c′_g(s_0 + 2r) ≤ ½ (I1), and ||T(λ)|| ≤ ||T(0)|| + ½r ≤ G_∞(X_∞s_0 + ζ) + ½r ≤ r
(I2). Banach's fixed-point theorem: exactly one zero λ_* in B_r, with ||λ_*|| ≤ ||T(0)|| + ½||λ_*||, i.e. ||λ_*||_{B∞} ≤ r_*. (4)
|A_*|_∞ ≤ s_0 + 2r_* + 2c′_g(s_0 + 2r)r_* ≤ r_sol. (5) Uniqueness in A: let A′ be as stated, e^{A′}U = g′·(g_ax·U_0), g′ ∈ 𝒢_V. Then
g′(y) = U_b^{-1}e^{-A′_b}g′(x)e^{A^0_b}U_b along every link, so ||1 - g′(y)|| ≤ ||1 - g′(x)|| + |A′_b| + |A^0_b| ((F2); unitary products). Along γ_y
from c_X, where g′ = 1: ||1 - g′(y)|| ≤ dh(r_sol + s_0) ≤ ½. [post-proof: the principal log of g′(y) is in su(N) when ||1 - g′(y)|| ≤ ε^thr_N
(SF-thr), which is ½ for N ≤ 12; for larger N read the hypothesis as dh(r_sol + s_0) ≤ ε^thr_N.] (F1): |log g′(y)|_HS ≤ √N·1.011dh(r_sol + s_0).
So λ′ := log g′ ∈ Λ, e^{λ′} = g′, and ||λ′||_{B∞} ≤ 1.011√NL^{d/2}dh(r_sol + s_0) ≤ r (I4). λ′ is a zero of Φ_ω in B_r, so λ′ = λ_* and A′ = A_*. ∎
*The chain is consistent (s5 F2, ARITHMETIC; d = 4, L = 3, N = 3; ζ the 't Hooft truncation radius, s_0 := ζ/X_∞, r := 509.4·G_∞ζ):*
**ζ = 2.19·10⁻⁵⁵, s_0 = 3.04·10⁻⁵⁷, r_* = 5.16·10⁻³¹, r_sol = 1.03·10⁻³⁰, τ_c := s_0/(√NC_0) = 4.34·10⁻⁵⁹**, and (I1)-(I4), (S0) hold. These are
g-independent and volume-independent, and astronomically small. They are driven by the crude G_∞ (s5 B6 measures the decay ~10²
times faster than m_FP at d = 2), not by any g-dependence.
[RSF5-fix FP-uniq tightness: the chain is TIGHT at this point: (I1) evaluates to 0.4995 (bound ½) and (I4)/r = 0.990 (bound 1)
(REVIEW_SF_S5 B-5, independent mpmath re-derivation). The optimum over ρ := r/(G_∞ζ) is ζ_max = 2.209·10⁻⁵⁵ at ρ ≈ 505 (τ_c = 4.38·10⁻⁵⁹), a 1%
change. Scaling: ζ ≈ 1/(4032c′_gX_∞G_∞²), so every threshold of the chain is ∝ G_∞^{-2}. Session 6 (§18-§19) sharpens G_∞.]
(s5 D, criteria first, d = 2, SU(2), 4×4 blocks, smooth background: D1 Newton from λ = 0 converges to residual ≤ 1.5·10⁻¹⁴ with
||λ_*||_{B∞} = 1.04·10⁻³ and 1.46·10⁻² for s_0 = 10⁻³, 10⁻², against the bound 0.20 and 2.0 (measured G = 7.79); D2 ten starts per case inside
the ball all converge to the same zero, to 3.5·10⁻¹³. **D3 FAILED as pre-registered:** from 12 starts of size O(1), no Newton run
converged within 60 iterations, so s5 exhibits no far Gribov copy; far zeros of h_U∘A at max|A| = 0.35-0.50 are s4 D2's. FP-uniq's proof
does not use D3.)
[RSF5-fix D3: D3 is recorded as a **failed positive control that does not test the proof**. It shows only that the copy-finder (Newton
from O(1) starts, principal-log discontinuity, a backtracking that accepts a step at t ≈ 10⁻⁴) is too weak; it says nothing for or
against far copies. FP-uniq and FP-sh never assume their absence (FP-sh is exact even if copies exist). Its one cost is evidential:
**D2's "same zero from 10 in-ball starts" has no demonstrated sensitivity**, and D2's starts lie in a ball where the contraction already
forces uniqueness, so D2 is low-power. A real control would relax a gauge functional along random 𝒢_V-orbits under the χ_U
constraint (REVIEW_SF_S5 B-7); not done.]

**Proposition FP-sh: PROVEN-HERE (not counted).** [post-proof correction: the displayed identity carries the c-number c_N^{-n_Λ}
(n_Λ := the number of non-centre sites) from the Haar density of 𝒢_V; it is absorbed in the normalisation.] *Proof.* (0) E_good(τ_c) is
𝒢_V-invariant: plaquettes are conjugated, and M̄_c(g·U_0) = g(c_X)M̄_c(U_0)g(c_Y)^{-1} = M̄_c(U_0). For U_0 ∈ E_good, both U_0 and U satisfy (E1)-(E2) at
level τ_c (ε_bg ≤ τ_c/2), so MSG_0 holds at every link: |A^0|_∞ ≤ √NC_0τ_c = s_0. (1) For ω ∈ supp γ̃ (so ||ω||_{B∞} ≤ ζ), FP-uniq gives exactly one
zero g_* = e^{λ_*}g_ax(U_0) of Φ^{U_0}_ω(g) := χ_U(log((g·U_0)U^{-1})) - (0, ω) in 𝒩(U_0) := {e^λg_ax(U_0) : ||λ||_{B∞} ≤ r}. It is non-degenerate: the
derivative is -χ_UΓ(1 - DT(λ_*)) with ||DT|| ≤ ½. In the chart g = e^μg_* the Haar measure of 𝒢_V is Π_x c_Nj(μ(x))dμ(x) (SF-J at each non-centre
site; right invariance). So J(U_0, ω) := ∫_{𝒢_V}1_{𝒩(U_0)}(g)δ(Φ^{U_0}_ω(g))dg = c_N^{n_Λ}/Δ(A_*), A_* := log((g_*·U_0)U^{-1}), Δ(A) := |det(χ_U∘𝔇_A)|.
(2) Covariance: by MSG_0 (6), 𝒩(g′·U_0) = 𝒩(U_0)g′^{-1} and Φ^{g′·U_0}_ω(hg′^{-1}) = Φ^{U_0}_ω(h); right invariance of dg gives J(g′·U_0, ω) = J(U_0, ω).
(3) Fix ω. For I as stated, ∫I = ∫I(U_0)J(U_0, ω)^{-1}∫_{𝒢_V}1_{𝒩(U_0)}(g)δ(Φ^{U_0}_ω(g))dg dU_0. By Tonelli, and the substitution U_0 → g^{-1}·U_0 at fixed g
(the link Haar measures are invariant under U ↦ aUb^{-1}; I, E_good and J are invariant), the integrand becomes
I(U_0)J(U_0, ω)^{-1}1_{𝒩(U_0)}(1)δ(Φ^{U_0}_ω(1)), by (2) with g′ = g^{-1}, h = 1. It no longer depends on g, and ∫dg = 1. So
∫I = ∫I(U_0)J(U_0, ω)^{-1}1_{𝒩(U_0)}(1)δ(χ_U(A) - (0, ω))dU_0, A := log(U_0U^{-1}). (4) On E_good: if 1 ∈ 𝒩(U_0) and Φ(1) = 0, then 1 = g_*, A = A_* and
|A|_∞ ≤ r_sol. Conversely, if Φ(1) = 0 and |A|_∞ ≤ r_sol, then A = A_* by FP-uniq (5), so 1 = g_* ∈ 𝒩(U_0). Hence 1_{𝒩(U_0)}(1)δ(…) = 1{|A|_∞ ≤ r_sol}δ(…),
and J^{-1} = c_N^{-n_Λ}Δ(A). (5) Average over ω with γ̃: ∫γ̃(ω)δ(χ_U(A) - (0, ω))dω = δ(h_U(A))γ̃(P_res^UD_U^*A). On {|A|_∞ ≤ r_sol}, SF-J gives
Π_bdU_0(b) = c_N^{#b}Π_bj(A_b)dA. γ̃_X = γ_X1{|ω_X| ≤ ζ}/(1 - p_X) with γ_X ∝ e^{-(u_0/2N)|ω_X|²}; SF-cut (b)'s Chernoff step, rescaled by √(N/u_0),
gives p_X ≤ 2^{m_X/2}e^{-u_0ζ²/(4N)}. ∎
*What this settles.* (i) Only the zero in 𝒩(U_0) is ever counted, so **no Gribov copy enters, exactly**, on E_good(τ_c): the uniqueness
clause of (FP-loc)_0 is PROVEN on the shrunk chart {|A|_∞ ≤ r_sol}. (ii) Any probability weight on ω gives an exact identity (as in FP-ab).
The truncated weight equals SF's 't Hooft weight times a c-number Z_ζ^{-1} wherever |(P_resD^*A)_X| ≤ ζ, which holds on |A|_∞ ≤ ζ/X_∞ ⊃ band. So the
D_UP_resD_U^T insertion of Setting N5-bg is exact; it is quadratic in A and has no nonlinear part. (iii) What remains of (FP-loc)_0 on
E_good is **(FP-det)**. *(FP-det), ARGUED:* χ_U𝔇_A = -χ_UΓ(1 - K), K := (χ_UΓ)^{-1}χ_U(𝔇_A + Γ). (𝔇_A + Γ)λ at b reads λ(x), λ(y), A_b, and its norm is
≤ 2c′_g|A_b|·|λ| (BCH-L's derivative bound). So ||K||_{B∞→B∞} ≤ 2c′_gq_∞r_sol ≤ ½, and log(Δ(A)/Δ(0)) = Re tr log(1 - K) = -ReΣ_ntr K^n/n. Writing
K = Σ_bK_b and using GF-dec's decay at rate m_FP, the trace expands into connected polymers with exponential decay: a walk expansion
of the RW type, not written. Analyticity in A on the complex chart follows from the same bounds. Owner: PROOF NA-FP / (FP-loc), with
lane F.
[RSF5-fix, non-binding notes. **FS-1:** "the truncation is invisible" (p_X ≤ ½) needs u_0ζ² ≥ 4N(m_X/2 + 1)ln 2, m_X = (L^d - 2)(N² - 1) = 632,
i.e. g_0² ≤ 1.8·10⁻¹¹³ (g_0 ≤ 4.3·10⁻⁵⁷) at session-5's ζ; the band window of DX′-2 (g_0 ≲ 5·10⁻⁶⁷) implies it. The exact identity does not
need it (Z_ζ is a c-number either way). **FS-2:** the chart {|A|_∞ ≤ r_sol} is LARGER than E_good: it contains fields with plaquettes up
to ≈ 4r_sol ≫ τ_c, so 1_{E_good}(e^AU) is a nontrivial, non-convex cut inside the chart. DX′ handles this (TILT takes an arbitrary event
E_𝔅 ⊂ E_good ∩ chart) and the band lies inside E_good (DX′ (a)). **FD-1 (an (M-W)-type hypothesis of (FP-det)):** the polymers of
(FP-det) decay at rate m_FP per L-block with prefactor G_∞, while CE-Q-col's norm needs rate κ_c ≈ 2.9·10³ per M-cube; this is
compatible only if **m_FP·M/L ≥ κ_c + log G_∞ + O(1)**. With session-5's m_FP = 3.858·10⁻⁴ it holds at M = M_W3 and fails at M ≲ 10⁸;
session 6 (§19) replaces m_FP and G_∞.]

**Theorem SLC-sh: PROVEN-HERE for the action, Jacobian and 𝔫 terms (not counted); the FP-det terms' local bound is part of (FP-det).**
*Proof.* |A|_∞ ≤ r_sol ≤ ρ_*, so Lemma SLc applies on Ω′ := Ω^+, where every term whose pattern meets Ω has its pattern:
  Σ_{τ∈T(Ω^+)}|u_0V_τ| + Σ_{b∈Ω^+}|log j(A_b)| + Σ_c|𝔫_c(e^AU) - 𝔫_c(U)| ≤ (C_coer r_sol + C′g_0²)⟨v, K_{Ω^+}v⟩ + 8K_𝔫c_yy_bgr_sol·n′_c|Ω^+|.
θ_1 := 2(C_coer r_sol + C′g_0²) ≤ 2(C_coer a_θ + C′g_0²) = ½ (a_θ = (1 - 4C′g_0²)/(4C_coer)). ⟨v, K_{Ω^+}v⟩ = |1_{Ω^+}A|²/(g_0²N||C||) ≥ |A_{b_0}|²/(g_0²N||C||), so
c_F = 1/(N||C||). K_{Ω^+} = 𝒞1_{Ω^+}𝒞/||C|| depends on Ω only (SC-1). It has ||K|| ≤ 1, tr K ≤ (N² - 1)|Ω^+|, and it is exponentially localised
(𝒞 decays at m_1). Straddling terms lie in T(Ω^+) (SC-2). The chart is stated (SC-3). The FP-det terms contribute ≤ C_FPr_sol|Ω^+| once (FP-det)
holds (linear in |A|, like SLc's source term). ∎ *Reading.* On the shrunk chart, (SL-coer′) holds with (F) for every b_0, and (P) is not
needed. The Gribov content of REVIEW_SF_S4's wall is gone: FP-sh shows that no copy is in the chart, and SLc needs no gauge input.

**Proposition DX′: inclusion and per-block factor PROVEN-HERE; CONDITIONAL ⇐ (FP-det) + (BGC) as a statement on the integral (not
counted); the insertion is (DX-loc), OPEN.** [post-proof: the pre-stated condition list included (TH-ch); DX′ does not use it, only FP-sh's
ε_bg ≤ τ_c/2.] *Proof.* (a) *Band re-tuned.* CE-Q-col uses ρ_* only as an upper bound for the field (Step 0, (B1′), SF-T0/SF-src domains), so
it holds verbatim with ρ_* → ρ_band (stronger hypotheses, g-independent constants). On the band |A|_∞ ≤ ρ_band, and then:
- plaquettes: ||1 - (e^AU)_p|| ≤ ε_bg + 4ρ_band ≤ τ_c/2 + 2τ_c/C_W ≤ τ_c;
- mismatch: ≤ ε_bg + C_Wρ_band ≤ τ_c, by W-Lip (the background spreads are ≤ y_bg ≤ c_yr_𝔫 ≤ y_♭ ≤ 1/40 by (BGC) and SF-N♮, and 2√N(6L - 4)ρ_band ≤ 1/40);
- |A|_∞ ≤ ρ_band ≤ r_sol, and |(P_resD^*A)_X| ≤ X_∞ρ_band ≤ ζ.
So the band lies in E_good ∩ {|A|_∞ ≤ r_sol} and in the support of γ̃, and its integrand is CE-Q-col's integrand times the (FP-det) polymers.
(b) *Inclusion.* On E_good ∩ chart, Lemma DL (with DL-1 and ρ_band) gives, for every deep block B, a link b with |A_b| ≥ a_she^{μd(b,B)}.
Since |A_b| ≤ r_sol, d(b, B) ≤ R_sh. (c) Fix a deep pattern 𝔅, put Ω(𝔅) := ∪_{B∈𝔅}{b : d(b, B) ≤ R_sh} and E_𝔅 := {deep set = 𝔅} ∩ chart. A link
lies within R_sh of at most m_sh blocks, so on E_𝔅, ⟨v, K_{Ω^+}v⟩ ≥ |𝔅|a_sh²/(m_shg_0²N||C||). (d) TILT with this fixed K, θ = θ_1 ≤ ½ (SLC-sh) and
E = E_𝔅: ∫_{E_𝔅}|exp(Σ_{Ω^+-terms}H)|dγ ≤ e^{C|Ω^+|}·exp((1 + θ_1)tr K/(2(1 - θ_1)))·sup_{E_𝔅}e^{-(1-θ_1)⟨v,Kv⟩/4} ≤ e^{C_Ω|Ω^+|}e^{-|𝔅|a′/g_0²}, with
C_Ω := C + 3(N² - 1)/2 and a′ = a_sh²/(8N||C||m_sh). (e) dγ is the white-noise reference, in which SF-A2^0 and FP-sh have already factored out
e^{-u_0S(U)} exactly. So **no background action and no defect enters a′: DX-1 does not arise.** ∎
*Size, recorded honestly.* R_sh = μ^{-1}log(r_sol/a_sh) ≳ 2·10¹⁰·log(10³⁰), so |Ω_B| ≳ 10⁴⁸ links and m_sh is comparable. The factor
e^{C_Ω|Ω_B|}e^{-a′/g_0²} is < 1 only for g_0² below a g-independent but astronomically small number. These are TILT's determinant and the
counting, pure numbers; they are not an action leak.
[RSF5-fix DX′-1: **the coupling ceiling DX′ implies, evaluated** (session-5 constants; scratch arithmetic sf6/arith1, reproduced in s6 F1).
Write N′ := N_r·N_μ(|Õ^{1/2}|) (finite, not evaluated) and f := 1 + ln N′/77.75.
- ρ_band = τ_c/(2C_W) = 2.280·10⁻⁶¹ (C_W = 95.145). The ρ_band entry of a_sh binds unless C_3^{Q,B} ≳ 10⁶⁰: a_sh = ρ_band/(16L⁴N′) = 1.759·10⁻⁶⁴/N′
  (e^{μ·diam B} = 1 + O(10⁻⁹)).
- R_sh = μ^{-1}ln(r_sol/a_sh) = 1.610·10¹²·f fine spacings (μ = m_1 = 4.83·10⁻¹¹); m_sh = (2R_sh/L + 3)⁴ = 1.327·10⁴⁸f⁴;
  |Ω_B| ≤ 4(2R_sh + L)⁴ = 4.30·10⁵⁰f⁴.
- ||C|| ≤ 1/λ_min. With Proposition RW-ℓ²'s λ_min ≥ 6.6·10⁻¹⁰: a′ = 6.42·10⁻¹⁸⁷/(N′²f⁴). With N5-sf0 (b)'s product-rule 7·10⁻⁸²: a′ = 6.80·10⁻²⁵⁹/(N′²f⁴).
- Per deep block the factor is e^{C_Ω|Ω_B|}e^{-a′/g_0²}; summing over patterns needs a′/g_0² ≥ C_Ω|Ω_B| + 1, so
  **g_0² ≤ g_{DX′}² ≈ 1.49·10⁻²³⁷/(C_ΩN′²f⁸)** (RW-ℓ² gap) or **≈ 1.58·10⁻³⁰⁹/(C_ΩN′²f⁸)** (product-rule gap).
- DX-rel's hole normalisation (REVIEW_SF_S5 DR-1: ≈ u_0^{(N²-1)n_R/2} per defect, with KF's (C_Ku_0^{N²-1})^{n_K}) is beaten by e^{-u_0a_p/2},
  a_p = τ_c²/(2N) = 3.14·10⁻¹¹⁸, only for u_0 ≥ (2P/a_p)ln u_0, P := (N² - 1)(n_K + n_R/2) = 339968: **g_0² ≲ 1.6·10⁻¹²⁶** (C_K and the
  pattern entropy ignored; they lower it by O(1) factors in the exponent).
  [RSF6-fix A-1/A-2 (non-binding): DX-rel prices each defect at min{a_p, a_c}, and a_c ≈ κ_sτ_c²/(4N) (KF) is below a_p for κ_s < 2; the
  ceiling is ≈ linear in a, so read **g_0² ≲ (min{a_p, a_c}/a_p)·1.6·10⁻¹²⁶** (≈ 0.8·10⁻¹²⁶ at κ_s = 1). "Lower it by O(1) factors in the
  exponent" reads "change it by an O(1) factor in u_0 (log terms)".]
- These two ceilings, the band window (DX′-2) and the truncation invisibility (FS-1 below) all enter O0's **g_*** (min of all).
  Scaling: ρ_band, a_p ∝ τ_c ∝ G_∞^{-2}, so g_{DX′}², the hole ceiling and the band window scale as G_∞^{-4} up to logarithms.]
[RSF5-fix DX′-2: **the re-tuned band hypotheses**, written out (they were left implicit in "stronger hypotheses"). With ρ_* → ρ_band in
GD-1 (iv): **(B1′) 2ρ′ + g_0√NN_r2^{j+1}p ≤ ρ_band** (ρ′ = 2g_0√NpN_μ(|𝒞|)); (B2′)-(B3′) unchanged (they carry no ρ_*); hence
**j_max := max{j : 2ρ′ + g_0√NN_r2^{j+1}p ≤ ρ_band}**, **a_*^B := min{(16C_3^{Q,B})^{-2}, (ρ_band/(4√NN_r))²} = 1.08·10⁻¹²³/N_r²** (ρ_band entry
binding), and the band's g_0-window at j = 0, p = p_0 = 6.45·10⁴: **g_0 ≤ ρ_band/(4√Np_0·max{N_r, 2N_μ(|𝒞|)}) ≈ 5.1·10⁻⁶⁷/max{N_r, 2N_μ}**. a_deep's
ρ_* → ρ_band and DL-1 factor are as in a_sh above.]
**Restated (CE-Q^∞) after session 5:** = DX′ (deep part on the chart; CONDITIONAL ⇐ (FP-det) + (BGC)) + (DX-loc) + (CH-c) (§16.3). The
session-4 wall (SL-coer′) on the ½-chart is not needed and is not attacked.

### 16.2 STEP 2 (pricing lemmas): Lemmas KF and DX-rel
**Lemma KF: PROVEN-HERE (not counted).** [post-proof notation: write κ_s for the soft-kernel coupling (Setting N5-bg's κ_0 ∈ [κ_-, κ_+]),
to avoid a clash with CE's κ_0 = 151.3; n_c(M) := ∫e^{-u_0κ_sφ(V;M)}dV.] *Proof.* By left covariance (φ(V; SM) = φ(S^{-1}V; M), W_0(SM) = SW_0(M)) take
S = 1. With X := V^{-1}W_0 unitary and G := W_0^{-1}M = H + iθ1 (NA-alg (a): ||H - 1|| ≤ 18.4y²; |θ| ≤ ||G - 1|| ≤ 18.4y², since iθ1 is the
anti-Hermitian part of G - 1): Nφ = Re tr((1 - X)G) = Re tr(1 - X) + Re tr((1 - X)(H - 1)) + θΣ_asin θ_a. Here Re tr(1 - X) = ½Σ_a|1 - x_a|², the
middle term is ≤ ||H - 1||Σ_a|1 - x_a| in absolute value (1 - X is normal), and |sin θ_a| ≤ |1 - x_a|. So Nφ ≥ Σ_a(½t_a² - 36.8y²t_a) (t_a := |1 - x_a|) ≥
Σ_a(¼t_a² - (36.8y²)²) ≥ ¼||1 - X||² - 1354.3Ny⁴, and ||1 - X|| = ||V - W_0||. Upper: Nφ ≤ ||G||·Σ_at_a ≤ N||V - W_0|| (||G|| ≤ ||M|| ≤ 1). Then
n_c ≥ ∫_{||V-W_0||≤r}e^{-u_0κ_sr}dV with r := 1/(u_0κ_s) ≤ 1. W_0exp{|A|_op ≤ r} lies in that ball (F2), and its Haar measure is
c_N∫_{|A|_op≤r}j(A)dA ≥ c_N(5/6)^{N(N-1)}v_{N²-1}r^{N²-1} (SF-J: j = Π(sin w′/w′)² ≥ (5/6)^{N(N-1)} for |w′| ≤ 1; the HS ball lies inside the op ball). So
n_c ≥ e^{-1}c′_N(u_0κ_s)^{-(N²-1)}, c′_N := c_N(5/6)^{N(N-1)}v_{N²-1}. ∎ (s5 E, criteria first: SU(2), SU(3), 4200 samples, y up to 1/20: E1 0
violations; E2 0 violations; E3 (report): the uncorrected bound without the y⁴ term was never violated either, so the correction is
not seen in the samples.)

**Lemma DX-rel: PROVEN-HERE as an inequality of the hole integrand (not counted).** [post-proof correction: the reference also carries
the background KERNEL values of the hole's coarse links. So (TH-bg) reads **ε_bg²(n_1/2 + 1.03κ_sn_K) ≤ ½min{a_p, a_c}**, with n_K := d·3^d (coarse
links per hole per defect). The pre-stated "n_1ε_bg² ≤ min{a_p, a_c}" omitted them. Second post-proof correction (hole size): a
plaquette defect can have its vertices in up to 2^d blocks, so the hole per defect is the ≤ 4^d blocks within coarse distance 1 of them:
read **n_R := d·4^dL^d, n_1 := 2(d - 1)n_R, n_K := d·4^d** (d = 4, L = 3: 82944 links, 497664 plaquettes, 1024 coarse links; s5 F1 printed the
3^d values 26244 / 157464, which undercount). The a_p entry of (TH-bg) then needs ε_bg ≤ τ_c/√(2Nn_1) = 2.51·10⁻⁶² (hand arithmetic from s5 F2's
τ_c; F2's printed 4.46·10⁻⁶² used the 3^d count).] *Proof.* On R(D) the stage-0 integrand is
Π_{p∈𝒫(R)}e^{-u_0s(U_{0,p})}·Π_{c∈𝒦(R)}e^{-u_0κ_sφ_c(U_0)}/n_c(M̄_c(U_0)), with s, φ ≥ 0. Numerator:
- every factor is ≤ 1, except 1/n_c ≤ e(u_0κ_s)^{N²-1}/c′_N (KF);
- each defect plaquette gives e^{-u_0s} ≤ e^{-u_0τ_c²/(2N)} (s(W) ≥ ||1 - W||²/(2N));
- each defect coarse link has its block-pair plaquettes ≤ τ_c, so its contour spread is y_c ≤ 1.011√NA_dτ_c ≤ 1/20 (each contour loop is spanned
  by ≤ A_d plaquettes, as in MSG step (4)), and KF gives e^{-u_0κ_sφ_c} ≤ e^{-u_0a_c}.
The defects are distinct objects, so these factors multiply. Reference: the background values of the same factors are e^{-u_0s(U_p)} with
s(U_p) ≤ ||1 - U_p||²/2 ≤ ε_bg²/2 (s(W) = (2N)^{-1}Σ_a|1 - e^{iθ_a}|²), and e^{-u_0κ_sφ_c(U)}/n_c(M̄_c(U)), with φ_c(U) ≤ 1.03ε_bg² (NA-alg (b): |ρ| ≤ 1.011√Nε_bg,
φ ≤ |ρ|²/N) and 1/n_c(U) ≥ 1 (n_c ≤ 1). So the ratio is ≤ Π_δe^{-u_0a_δ}·exp(u_0|D|ε_bg²(n_1/2 + 1.03κ_sn_K))·(C_Ku_0^{N²-1})^{n_K|D|}, C_K := eκ_s^{N²-1}/c′_N,
and under the corrected (TH-bg) this is ≤ Π_δe^{-u_0a_δ/2}(C_Ku_0^{N²-1})^{n_K}. ∎
*What it corrects.* DX-1's subtraction now runs over the plaquettes and coarse links of a BOUNDED hole: n_1 = 497664 plaquettes and n_K = 1024
coarse links per defect (d = 4, L = 3; 4^d-block holes, post-proof), not ≳ 10⁴² cubes. The hole is bounded because MSG_0 at a link reads only its block pair, so
a defect spoils the axial representative only on the blocks within coarse distance 1. With τ_c from s5 F2, the a_p entry alone needs
ε_bg ≤ 2.51·10⁻⁶² (4^d holes; F2's 4.46·10⁻⁶² is the 3^d count). *Not written:* the Gaussian/FP normalisation of the hole in the reference (polynomial in g_0 per link: (2πNg_0²)^{dim/2}
and det^{-1/2}, FP_U), and the factorisation of the reference across ∂R(D). This is **(DX-loc)**. It may use only (H-w)'s normalisation parts
(a)-(c), not its weight sources (REVIEW_SF_S4 D-2), and the rest of FP-uniq on the complement of a frozen hole (GF-dec restricted to the
non-hole blocks keeps the gap c_D and the decay).
[RSF5-fix, non-binding DR-1: outside the hole the GAUGE-FIXED field is a nonlocal function of the data, through (χ_UΓ)^{-1} (range ≈ 1/m_FP
blocks, prefactor G_∞). So "factorisation across ∂R(D)" in (DX-loc) is a decay statement at rate m_FP, not an exact factorisation, and
FD-1 applies there too. The hole's Gaussian normalisation costs ≈ u_0^{(N²-1)n_R/2} per defect; it is beaten by e^{-u_0a/2} only below the
DX-rel ceiling of DX′-1.]

### 16.3 STEP 3: (CH-c), its assignment, and the exact dependency order
**Proposition CH-assign: PROVEN-HERE (a set inclusion + the circularity argument; not counted).** *Proof.* (i) Take a stage-0
configuration in RLARGE's small-field set (cut-good: every cube-interior plaquette has ||1 - U_{0,p}|| < ε_1; soft residual / kernel
mismatch below threshold). Exclude the inter-cube [v2-E8] event and the plaquettes adjacent to ∂Λ(𝔥), which are HIST boundary terms
(e^{B_0} per boundary cube). Under (TH-ch), (E1) holds at every remaining plaquette (ε_1 ≤ τ_c) and (E2) at every coarse link (|ρ_c| ≤ ε ⇒
||V_c - W_0|| ≤ ε by (F2), with ε ≤ τ_c). So the configuration is in E_good(τ_c). Hence (CH-c) consists of: cut-bad cubes (the level-0 large-field
history, RLARGE's structure, not SF's), the [v2-E8] event, above-threshold kernel mismatches (branch (i); at stage 0 the pointwise
bound KF, which carries no H-4 caveat), and boundary terms. (ii) Branch (ii)'s domain (PLD-desc, RLARGE l.312-318) is: plaquettes with
||1 - U_p|| ≥ τ, τ ∈ (0, ε_1], on A ⊂ 𝒫°(𝔥), under the cut-good law with V ∈ 𝒱^sf(A). Those plaquettes are < ε_1 ≤ τ_c, so these
configurations satisfy (E1) there. They lie in E_good, i.e. in the chart, not in (CH-c). **So branch (ii) prices no part of (CH-c).** It
is a consumer of the in-chart expansion, never a supplier to it. (iii) If (TH-ch) is dropped and some small-field threshold t exceeds
τ_c, then the defects in (τ_c, t] are in (CH-c) ∩ small-field set. (SG^fl)_0 is the expectation E_{μ^+}[exp(tΣ⟨u, Y⟩) | V] over the whole cut-good
fixed-V law μ_V ∝ 1_cut e^{-S_W/g_0²}K_0 (PLD l.1109, l.985-990), so its derivation ((G0-2): the (SF)_0 expansion of that law) must already price
those configurations. Pricing them by branch (ii) ⇐ (SG^fl)_0 is therefore circular. DX-rel prices them with no (SG^fl) input. ∎
*Answer to the STEP-3 question as posed.* "(CH-c) priced by branch (ii) without circularity, since (SG^fl)_0 follows from CE-Q-col + DX":
the premise needs one correction. (SG^fl)_0 follows from CE-Q-col + DX′ only TOGETHER WITH the pricing of (CH-c) ∩ small-field set.
That set is empty under (TH-ch) (modulo [v2-E8] and boundary terms), and in-step priced by DX-rel otherwise. So the order is
non-circular because (CH-c) never goes to branch (ii), not because branch (ii) comes later.
[RSF5-fix CH-1 (binding; the routing in (i) and in the paragraph above is corrected). RLARGE's χ_Q reads cube-INTERIOR plaquettes only
and is never changed (RLARGE l.55-56), so at stage 0 the inter-cube fine plaquettes are uncut in μ^+, and those above τ_c lie in
supp μ^+ ∩ (CH-c), away from A. RLARGE prices its "[v2-E8] event" as (D-c), "priced as (D-b)" (RLARGE l.258-260), and (D-b) via §3.4's split
at η_♭′ "priced as above (branches (ii)/(iii))" (l.367-368). Routing it there closes the circle (SG^fl)_0 ⇐ (SF)_0 ⇐ (α) ⇐ RLARGE (D-c)/(D-b)
⇐ branch (ii) ⇐ (SG^fl)_0, which is exactly what (iii) forbids; branch (iii) (CLS-sf, ARGUED) is built for coherent backgrounds, not single
rough plaquettes. **Corrected routing: at stage 0, EVERY fine plaquette > τ_c (cube-interior or inter-cube) and EVERY coarse-link
mismatch > τ_c is priced in-step by DX-rel + (DX-loc)** (Wilson/kernel positivity relative to the background on a bounded hole), never
via RLARGE (D-c)/(D-b) → §3.4 → branches (ii)/(iii). "The [v2-E8] event" in (i), in O4 and in the RLARGE owner note reads "DX-rel-priced
defects". The cut-bad-cube history (outside Λ(𝔥); bare R1 by Wilson positivity, RLARGE App. A) is unchanged.]
[RSF5-fix CH-2 (binding). "∂Λ(𝔥)-adjacent plaquettes are HIST boundary terms (e^{B_0} per boundary cube)" in (i) is the reading that
REVIEW_PLD_S3 SG-1 withdrew: **e^{B_0} is a cost, not a suppression**. This family is RLARGE (D-d) = **E10, OPEN** (RLARGE l.261-265: it needs
its own e^{-a/g²}; neither route is written). DX-rel prices the interior side of such a defect only if its hole does not meet ∂Λ(𝔥); a
hole that meets the history boundary needs E10. (CH-c) inherits E10.]
[RSF5-fix status. Proposition CH-assign stays PROVEN-HERE **as the set inclusion of (i) (with the families (α) inter-cube plaquettes
> τ_c, (β) ∂Λ(𝔥)-adjacent defects, (γ) mismatches > τ_c, and the cut-bad history) and the circularity argument (iii)**. Its routing sentence
is withdrawn. **(CH-c) is CONDITIONAL ⇐ DX-rel (PROVEN inequality) + (DX-loc) [OPEN] + RLARGE E10 [OPEN] + the CH-3 V-scope (𝒱^sf(Λ′),
local ε_bg)**. It is NOT "assigned / discharged".]
*Consistency of (TH-ch).* s5 F2: with τ_c = 4.34·10⁻⁵⁹ the radius chain (I1)-(I4), (S0) holds. Then (TH-ch) asks ε_1 ≤ τ_c and every stage-0
small-field threshold ≤ τ_c. ε_1 is a free g-independent threshold of [v2-C]; lowering it changes only g-independent constants in RLARGE's
large-field exponents (∝ ε_1²). ε_bg ≲ C_bgε_1 is BR1 (iii)'s background bound (a bracketed remark, as in SN-2, not a written step).
[RSF5-fix TH-1 (binding). (TH-ch) as stated (ε_1 ≤ τ_c) is too weak: it does not carry (TH-bg). The binding stage-0 threshold condition is
  **(TH-ch′) ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}**, with every RLARGE stage-0 small-field threshold (incl. ε_*) ≤ τ_c,
where ε_bg^{(TH-bg)} is the largest ε_bg allowed by the corrected (TH-bg) ε_bg²(n_1/2 + 1.03κ_sn_K) ≤ ½min{a_p, a_c} (a_p entry alone:
τ_c/√(2Nn_1) = 2.511·10⁻⁶²; the κ_s entry lowers it), and **C_bg** is read off BR1 (iii) (PROOF l.5668): |log U(V)_p| ≤ (1 + 48𝔠_∞)ε_V and
|ρ_c| ≤ 3p_Lr(ε_V) = 36p_L𝔠_∞ε_V, with ε_V ≤ 1.011√Nε_1 ((F1); ε_V is |log|_HS, ε_1 an op-norm cut), so
  **C_bg := 1.011√N·max{1 + 48𝔠_∞, 36p_L𝔠_∞} = 1.39·10⁴⁰** (𝔠_∞ ≈ 2.0·10³⁷ at N5-w0's constants, PROOF l.5859, N = 2 there; p_L = 11).
At session-5 constants: **ε_1 ≤ 1.81·10⁻¹⁰² (the ε_bg^{(TH-bg)}/C_bg entry binds)**, not 4.3·10⁻⁵⁹. With the product-rule 𝔠_∞ ≈ 1.3·10⁵³ it is
≈ 2.8·10⁻¹¹⁸. s5 F2's "consistency" covers (I1)-(I4), (S0) only, not (TH-bg) against BR1. (BR1 is stated with the global ε_V; under CH-3
the local form is part of (DX-loc).)
[RSF6-fix TH-2 (binding). (TH-ch′) omits BR1's own domain: BR1 holds only for ε_V ≤ ε ≤ ε_br, ε_br := min{ε_*/(1 + 36p_L𝔠_∞),
1/(24𝔠_∞²C_♭), r_♭/(24𝔠_∞), r_♭/(18(3L - 1)), 1/(1728𝔠_∞K_FP)} (PROOF l.5663). The binding stage-0 threshold condition is
  **(TH-ch″) := (TH-ch′) ∧ ε_1 ≤ ε_br/(1.011√N)** (and every RLARGE stage-0 small-field threshold, incl. ε_*, ≤ τ_c as before).
At PROOF's 𝔠_∞ = 2.0·10³⁷ the second entry of ε_br is 1.04·10⁻⁷⁶/C_♭ and the others are larger (given C_Δ ≤ C_♭, PROOF l.5659), so
**ε_1 ≤ 5.95·10⁻⁷⁷/C_♭** (N = 3). C_♭ := 4S_♭n_1/r_♭ (Lemma N5-an♭) exists and is not evaluated (PROOF l.6052); it is carried
symbolically. (TH-ch′) alone is not admissible.]
**Derived-constant consequences, recorded honestly** (scaling each source's own reference value at ε_1 = 0.5; scratch arithmetic
sf6/arith1, reproduced in s6 F1; at ε_1 = 1.81·10⁻¹⁰²):
| item (source) | scaling | at ε_1 = 0.5 (as quoted) | at ε_1 = 1.81·10⁻¹⁰² |
|---|---|---|---|
| RLARGE n_* = ⌊4/(a″β_-)⌋, a″ < ε_1²/(4N) | ε_1^{-2} | 382 / 255 (SU(2)/SU(3)) | **2.9·10²⁰⁵ / 1.9·10²⁰⁵** |
| HIST n_♯, joint route (η_q linear) | ε_1^{-2} | 5·10¹¹-4·10¹⁵ | 4·10²¹⁴-3·10²¹⁸ |
| HIST n_♯, RS route (η_1 quadratic) | ε_1^{-4} | 4·10¹³-3·10¹⁷ | 2·10⁴¹⁹-2·10⁴²³ |
| RLARGE η_1 = min{ε_1/18, ε_1²/(4608N)} | ε_1² | 2.7·10⁻⁵ (N = 2) | 2.4·10⁻²⁰⁸ (N = 3); a_RS ∝ η_1² ≈ 6·10⁻⁴¹⁶ |
| HW a_bad = c_pr·min{ε_1², t_pr²} | ε_1² | min-branch | ≈ 1.7·10⁻²¹⁰ |
| RLF torus / final-levels caveat | log_L(n_*^{1/4}) | O(1) levels | **≈ 108 final levels** |
All are finite, g-independent and K-independent: no lane needs ε_1 bounded below (REVIEW_SF_S5 Part E). Every lane's ε_1 = 0.5 numerics
are "illustrative, not admissible under (TH-ch′)". Session 6 (§19) re-evaluates this table after sharpening G_∞; C_bg then dominates.]

**Exact dependency order at stage 0 (each item lists everything it consumes):**
- **O0** (thresholds and background):
  - choose ζ (s5 F2), then s_0 = ζ/X_∞ and τ_c = s_0/(√NC_0), then ε_1 ≤ τ_c and RLARGE's stage-0 thresholds ≤ τ_c (TH-ch), then ε_bg from BR1 (iii)
    with ε_bg ≤ τ_c/2 and the corrected (TH-bg);
  - background: BR1/NAH1 (PROOF [S20]) + (BGC).
- **O1** (gauge fixing on E_good): MSG_0 [⇐ HIST MSG steps (2)-(4), (F1)-(F5), RS (R1), NA-alg (a)], W-Lip, GF-dec [⇐ NA-FP (i)-(ii)], BCH-L,
  FP-uniq, FP-sh. All PROVEN, session 5. Output: (FP-loc)_0 on E_good ⇐ (FP-det) [ARGUED].
- **O2** (band): CE-Q-col with ρ_band (analytic part PROVEN) ⇐ O1 + (BGC) + its own hypotheses (§13.1).
- **O3** (deep part on the chart): DX′ ⇐ O1 + SLc + TILT + DL (PROVEN). The insertion is (DX-loc) [OPEN; (H-w)(a)-(c) only].
- **O4** ((CH-c)): CH-assign (PROVEN). The large-field events are RLARGE level-0 items (history / [v2-E8] / branch (i) in its pointwise
  stage-0 form KF). Any in-step defect band is priced by DX-rel (PROVEN inequality) + (DX-loc).
  [RSF5-fix CH-1/CH-2: **corrected O4** ⇐ CH-assign's inclusion (PROVEN) + DX-rel (PROVEN inequality) for every fine plaquette > τ_c and
  every mismatch > τ_c (inter-cube included) + (DX-loc) [OPEN] + RLARGE E10 [OPEN] for holes meeting ∂Λ(𝔥) + the bare-level history
  (cut-bad cubes, outside Λ(𝔥), bare R1 by Wilson positivity, RLARGE App. A) + the CH-3 V-scope. No (SG^fl)_0, no branch (ii), no (H-w)
  weight source. **O0-O6 is non-circular only in this corrected form**; as written in session 5 (O4 citing RLARGE [v2-E8] and "boundary
  terms") it routed through branch (ii) and relied on an OPEN family. O0 reads (TH-ch′) of TH-1 in place of "ε_1 ≤ τ_c".]
- **O5**: (SG^fl)_0 ⇐ O2 + O3 + O4 + N5-sf0 + (G0-1)-(G0-4) + (I_0^E) + (BG)_0 + (TH) (PLD §15.4; D-3).
- **O6**: branch (ii) at level 0 (PLD-desc) ⇐ (SG^fl)_0. It is consumed by RLARGE's level-1 step.
- Check: O0-O4 consume no (SG^fl)_0, no branch (ii) and no (H-w) weight source. O4 uses branch (i) only in KF's pointwise form.
- k ≥ 1: MSG_0 and DX-rel transpose with level-k blocks. GF-dec at level k needs the block-diagonality of the composite M^{(k)}_U
  (NA-FP composite slice), which is not checked here: **(GF-dec)_k** [OPEN, new name]. Branch (iii) stays ARGUED, so (O3_k), (O4_k) are at
  most ARGUED.
- **Owner note for RLARGE (proposed; RLARGE is not edited by lane F):** read (SG^fl)_k's input "(SF)_k's cluster expansion" as
  "CE-Q-col (band, ρ_band) + DX′ + (DX-loc) + (CH-c) as assigned by CH-assign". Add τ_c and (TH-ch) to [v2-C]'s threshold list.
  [RSF5-fix: read "(CH-c) as assigned by CH-assign" as "(CH-c), CONDITIONAL ⇐ DX-rel + (DX-loc) + E10 + CH-3 scope"; read (TH-ch) as
  (TH-ch′). **Second owner note for RLARGE (proposed, not edited):** at stage 0, §3.4's plaquette leg above τ_c for (D-b)/(D-c) is DX-rel
  (in-step), not branches (ii)/(iii); (D-d)/E10 is now on lane F's path.]

## 17. Session-5 outcome (written after §16)

### 17.1 Status changes
| item | status | note |
|---|---|---|
| [RSF4-fix] STEP 1 | applied | RT-1 citations, CQ-1 (807.46; p_0 ≈ 6.45·10⁴), HALO-b tight, GD-1, DL-1, RES-1/2, SC-1..3, DX-1, DX-2, D-1..D-3, threshold note, halo-vs-torus caveat, §14 tally line |
| Lemma MSG_0 | PROVEN-HERE (not counted) | one-scale, block-local case of HIST MSG; s5 A with a negative control |
| Lemma W-Lip | PROVEN-HERE (not counted) | C_W = L + 3.8√N(6L - 4) |
| **Lemma GF-dec** | **PROVEN-HERE (not counted)** | (χ_UΓ)^{-1} explicit; gap c_D from λ(c_X) = 0 for EVERY background; decay m_FP; s5 B |
| Lemma BCH-L | PROVEN-HERE (not counted) | c_g = 25.85; s5 C |
| **Proposition FP-uniq** | **PROVEN-HERE (not counted)** | sup-norm IFT; existence + uniqueness, volume-independent; s5 D1-D2 (D3 control FAILED, recorded) |
| **Proposition FP-sh** | **PROVEN-HERE (not counted)** | exact gauge-fixed representation on E_good with a truncated 't Hooft weight; no Gribov copy enters |
| (FP-det) | ARGUED, new name | the only remaining part of (FP-loc)_0 on E_good |
| **Theorem SLC-sh** | **PROVEN-HERE (not counted)** (FP-det terms via (FP-det)) | (SL-coer′) on the shrunk chart; SC-1..SC-3 met; (P) not needed |
| Proposition DX′ | CONDITIONAL ⇐ (FP-det) + (BGC) (inclusion and factor PROVEN) | a′ = a_sh²/(8N‖C‖m_sh); no defect, no background action; supersedes DX |
| Lemma KF | PROVEN-HERE (not counted) | DX-2's pointwise kernel bound; s5 E |
| **Lemma DX-rel** | **PROVEN-HERE (inequality; not counted)** | bounded holes (n_1 = 497664 plaquettes per defect, 4^d blocks), corrected (TH-bg) |
| **Proposition CH-assign** | **PROVEN-HERE (not counted)** | (CH-c) is in no part branch (ii)'s; under (TH-ch) it is RLARGE level-0 large-field events |
| (SL-coer′) on the ½-chart | not attacked; superseded | SLC-sh |
| Proposition DX (session 4) | superseded by DX′ | its a′ stays ARGUED (DX-1) |
| (CH-c), (DX-rel) | assigned / PROVEN (as above) | session-4 OPEN names discharged as stated |
| [RSF5-fix] Proposition CH-assign | PROVEN-HERE only as the set inclusion + the circularity argument (iii) | routing sentence withdrawn (CH-1, CH-2) |
| [RSF5-fix] (CH-c) | **CONDITIONAL ⇐ DX-rel + (DX-loc) + RLARGE E10 + CH-3 V-scope** | "assigned" withdrawn from "Discharged"; RLARGE E10 now on lane F's path |
| [RSF5-fix] (TH-ch) | replaced by (TH-ch′) (TH-1) | ε_1 ≤ min{τ_c, τ_c/(2C_bg), ε_bg^{(TH-bg)}/C_bg}; C_bg = 1.39·10⁴⁰ |
| (DX-loc) | OPEN | restricted by D-2; now also carries FP-uniq on the complement of a frozen hole |
| (GF-dec)_k | OPEN, new name | composite-slice block-diagonality at k ≥ 1 |

**Tally of this file after session 5 (unreviewed):**
- **PROVEN-HERE 44 + 1 standard.**
  - Counted 10: unchanged.
  - Not counted 34: session 4's 24, plus MSG_0, W-Lip, GF-dec, BCH-L, FP-uniq, FP-sh, SLC-sh, KF, DX-rel, CH-assign.
- **CONDITIONAL 7:**
  - SF-thr-k; CE-exp^k;
  - SF-A2^0, CE-exp^0, CE-Q and CE-Q-col as statements on the integral. These are now ⇐ (FP-det) + (BGC) + the O0 thresholds on E_good,
    through FP-sh, in place of ⇐ (FP-loc)_0 + (BGC);
  - DX′ (replaces DX).
- **ARGUED 3:** (CE-s); DX's a′ (session 4, superseded); (FP-det).
- **OPEN names:** (DX-loc); (GF-dec)_k; (FP-loc)_k, (N5-reg)_k, (L-loc)_k [B-NA]; (CE-col)'s item (iv); (SF-irr) and the A4 items; (a5-G♯)/(G♯-patch),
  (R♯) at ψ^r [B-NA]; lane D: (MIN-reg), (a5-U), (a3-q).
- **Discharged this session:**
  - (SL-coer′) as the wall, by reformulation (SLC-sh);
  - the uniqueness clause of (FP-loc)_0 on the shrunk chart (FP-uniq, FP-sh);
  - ~~(CH-c) assigned (CH-assign);~~ [RSF5-fix: withdrawn; (CH-c) is CONDITIONAL, see the table]
  - (DX-rel) (bounded-hole pricing);
  - DX-1, DX-2, SC-1..SC-3, D-1..D-3.
- No RLARGE §4.2 row is discharged. No PROOF.md tally change is proposed. The owner of PROOF NA-FP may want FP-uniq/FP-sh as the stage-0
  nonlinear complement of NA-FP (iii).

### 17.2 What (SF^J)_0 now rests on
- **A2 (gauge-fixed representation):** ⇐ (FP-det) [ARGUED] + (BGC) + the O0 thresholds, on E_good. The uniqueness clause is PROVEN.
- **A3 band:** CE-Q-col with ρ_band, g-independent M and p_0 (p_0 ≈ 6.45·10⁴ at κ_c = 2938.2).
- **A3 deep:** DX′ (per-block factor, relative to white noise) + (DX-loc).
- **A3 out-of-chart:** (CH-c) per CH-assign: RLARGE level-0 large-field events; any in-step band goes to DX-rel + (DX-loc). No branch (ii).
  [RSF5-fix: (CH-c) ⇐ DX-rel for every plaquette/mismatch > τ_c (inter-cube included) + (DX-loc) + RLARGE E10 + the CH-3 V-scope;
  CONDITIONAL. Reviewer-corrected tally after session 5: PROVEN-HERE 44 + 1 standard; CONDITIONAL 8 (SF's 7 + (CH-c)); ARGUED 3;
  OPEN names + RLARGE E10; (FP-det) carries FD-1.]
- **A4:** unchanged (rate from 1149.92 / 1478.49; d ≥ 1 norm from 2499.39 / 2938.18; d < 1 is (SF-irr)).
- **Price paid:** every threshold is astronomically small (τ_c ≈ 4·10⁻⁵⁹, ρ_band ≈ 2·10⁻⁶¹, ε_bg ≲ 2.5·10⁻⁶²), so the "g_0 small enough"
  conditions are extreme. All of this comes from the crude ℓ^∞ bound G_∞ ≈ 6·10²³ (s5 B6: the true decay is far faster). It is
  g-independent and volume-independent.

### 17.3 Check s5
- Provenance. Criteria checks/s5_criteria.md born 06:16:32 UTC (md5 ad0e4d71…), before the script (born 06:19:23 UTC). Script
  checks/s5_sf.py (md5 6edaee23…). Output checks/s5_out.txt (md5 b9a1f55d…). Record checks/s5_time.txt.
- Run. One run under the numeric lock, 06:21:27-06:21:43 UTC: load 3.74, nice 10, BLAS threads 1, 15.4 s, peak RSS 114 MB, exit 0, one
  rmdir.
- **OVERALL FAIL 19/20: D3 FAILED as pre-registered.** D3 was the control meant to exhibit far Gribov copies by Newton from O(1)
  starts; none of the 12 runs converged. No proof uses D3. [RSF5-fix D3: a failed positive control that does not test the proof; D2
  therefore has no demonstrated sensitivity (see §16.1).]
- Evidential: A1-A2, B1, B3-B4, C1, D1-D2, E1-E2. Exact identities / locality: A3-A5, B5. Negative control: A7 (passed: a corner root
  breaks orbit invariance). Non-vacuity: A6. Arithmetic: F1-F3. Reports: B6, C2, E3.
- Low power, recorded:
  - A2 tests only the ladder part of MSG step (4); the RS (R1)/NA-alg part is cited.
  - E3 shows that the y⁴ correction of KF is never needed in the samples.
  - B is at d = 2 only (d = 4 sizes are out of the memory budget for dense inverses).

# SESSION 6 (2026-10-28 UTC). Inputs read before 06:59 UTC: REVIEW_SF_S5.md (BINDING; in full; md5 4449034c…), SF.md (83843fef…, =
SF_LOG's session-5 final), SF_LOG.md (fa3a8d57…), RLARGE.md 24a73553… (l.50-80, 250-268, 360-372), PROOF.md 4a7bbccc… (Lemma FPq
l.5630-5640; Lemma BR1 l.5661-5700; 𝔠_∞ l.5600-5606 and l.5859; N5-sf0's gap l.5414-5420), HIST.md 468e9f03… ((F1)-(F6), l.1182-1196).
The [RSF5-fix] STEP-1 edits (07:09-07:15 UTC) precede this section.

## 18. PRE-STATED (session 6) (appended at ≈07:16 UTC, 2026-10-28, BEFORE any session-6 proof and before the s6 criteria; cites only PROVEN items)

### 18.0 Conventions for §18-§20
§15.0's conventions (stage 0, background U, 𝒢_V, Λ := {λ : sites → su(N), λ(c_X) = 0}, Λ_res^U := Λ ∩ ker M_U, P_res^U, D_U, Γ := D_U|_Λ,
χ_UΓλ = (M_Uλ, P_res^UD_U^*D_Uλ) (NA-FP (i)), d = 4, L = 3 unless stated). Block-kernel operators A = (A(X, Y)) between block-ℓ² spaces;
**|||A||| := sup_XΣ_Y||A(X, Y)||** (operator norms of the blocks). For a map of the input (η, ω): **|||A|||_sp := sup_XΣ_Y(||A_η(X, Y)|| +
||A_ω(X, Y)||)**. Then ||Ax||_{B∞} ≤ |||A|||·||x||_{B∞}, |||AB||| ≤ |||A|||·|||B|||, and ||A(η, ω)||_{B∞} ≤ |||A|||_sp·max_Ymax{|η_Y|, |ω_Y|}.
**G_∞(U)** := the least G with ||(χ_UΓ)^{-1}(η, ω)||_{B∞} ≤ G·max_Ymax{|η_Y|, |ω_Y|} for all η ∈ su(N)^{blocks}, ω ∈ Λ_res^U. This is the only property
of G_∞ that FP-uniq's proof uses (its step (2)); GF-dec (e)'s number 5.8954·10²³ is an upper bound for it. The volume is a torus of n_T
blocks per side.

### 18.1 STEP 2: a sharp bound for G_∞ (every threshold of §16 is ∝ G_∞^{-2})
*Idea fixed before writing (from the exploratory scratch runs logged in SF_LOG at 07:02-07:06; they are not evidence):* GF-dec (e)
loses three times: (1) c_D = 1/(dhL^d) = 1/324, while Kato's inequality |D_Uλ| ≥ |d|λ|| gives the scalar Dirichlet gap 0.0852 (PROOF
Lemma FPq (i), PROVEN); (2) the Neumann rate ≈ c_D/(4d), while a Chebyshev polynomial gives ≈ 2√(c_D/(4d)); (3) entrywise ℓ^∞-shell sums
in d = 4 with ||M^+|| ≤ L^d. (1)-(2) give an every-background bound ~10¹⁰. For the background actually used (plaquettes tiny), the
operator is, block by block in a local axial gauge, a tiny perturbation of the U = 1 operator, which is scalar ⊗ 1 and translation
invariant; there an explicit finite-range approximate inverse with a certified residual gives a bound of order 10¹-10². A bordered
(saddle-point) form makes the target space independent of U and every matrix entry an integer.
- **Lemma CD (Kato gap, every background).** For every background U and every λ ∈ Λ: ||D_Uλ||² ≥ c_D^K||λ||², **c_D^K := 2663/31250 = 0.085216**. Hence
  G_res := P_res^UD_U^*D_UP_res^U on Λ_res^U has spectrum in [c_D^K, 4d]. *Planned: PROVEN (citation) ⇐ PROOF Lemma FPq (i) [S20, PROVEN];
  s6 A1 re-certifies 2663/31250 independently (exact rational LDLᵀ). Not counted.*
- **Lemma CHEB (Chebyshev decay; any block-range-1 positive operator).** Let G be self-adjoint on ⊕_X H_X with spectrum in [a, b], 0 < a < b,
  and G(X, Y) = 0 for |X - Y|_∞ > 1. Put σ := (b + a)/(b - a), θ := arccosh σ, T_D the Chebyshev polynomial. Then ||G^{-1}(X, Y)|| ≤ 1/a, and for
  D := |X - Y|_∞ ≥ 1, **||G^{-1}(X, Y)|| ≤ 1/(aT_D(σ)) ≤ (2/a)e^{-θD}**. *Planned: PROVEN-HERE (elementary; not counted).*
- **Lemma RINV (block-local right inverse of M_U; every background).** With T_s the transport of the single link between c_X and c_X + s
  used by M_U (s over the 2d unit vectors ±e_μ), **R_Uη := Σ_X Σ_s (L^d/(2d)) Ad(T_s)^{-1}η_X δ_{c_X+s}** satisfies M_UR_U = 1, R_U is
  block-diagonal with ||R_U(X, X)|| = L^d/√(2d), and |||P_res^UD_U^*D_UR_U||| ≤ **c_R := (L^d/(2d))(√(8d³ + 8d(d - 1)) + 2d)** (= 330.66 at d = 4, L = 3).
  *Planned: PROVEN-HERE ⇐ GF-dec (a) (not counted).*
- **Proposition GF-A (every background; explicit).** For every background U:
    **G_∞(U) ≤ G^A := L^d/√(2d) + Γ_1(1 + c_R)**,  Γ_1 := (c_D^K)^{-1}[1 + Σ_{D≥1}N_D/T_D(σ)],  N_D := (2D + 1)^d - (2D - 1)^d,
  with a = c_D^K, b = 4d; and ||(χ_UΓ)^{-1}(X, Y)|| ≤ (1 + c_R)(c_D^K)^{-1}·2e^{-θ(|X-Y|_∞-1)} + L^d/√(2d)·δ_{XY} for all X, Y, i.e. decay rate
  **m_FP^A := θ** per block. The same holds verbatim on the complement of any frozen set of blocks (Lemma FH below). *Planned: PROVEN-HERE
  ⇐ CD, CHEB, RINV, GF-dec (d) with R_U in place of M_U^+ (not counted).* Numbers by s6 A4. *Expected failure mode:* a wrong count in c_R
  (the geometry of D^*D near c_X at L = 3); s6 A3 measures |||P_resD^*DR||| at d = 2.
- **Lemma KKT (bordered form; every background).** Put M′_U := L^dM_U and 𝒦_U(λ, μ) := (P_ΛD_U^*D_Uλ - M′_U^{T}μ, M′_Uλ) on Λ ⊕ su(N)^{blocks}. Then 𝒦_U
  is invertible, and **(χ_UΓ)^{-1}(η, ω) = P_λ𝒦_U^{-1}(ω, L^dη)** for every ω ∈ Λ_res^U. At U = 1, 𝒦_1 = 𝒦^{sc} ⊗ 1_{su(N)} with 𝒦^{sc} a
  translation-invariant block kernel of range 1 whose entries lie in {0, ±1, 2d}. 𝒦 is covariant: 𝒦_{g·U} = Ad(g)𝒦_UAd(g)^{-1} for every
  gauge g (acting on (λ, μ) through g at sites and at block centres). *Planned: PROVEN-HERE ⇐ NA-FP (i)-(ii), GF-dec (a), Lemma CD (not counted).*
- **Lemma BOXG (local axial gauge on a box).** Let B be a box of fine sites with a centre site c, max_{x∈B}|x_ν - c_ν| ≤ h_B, and let every
  plaquette p ⊂ B have ||1 - U_p|| ≤ ε. With γ_x the axial path (order 0, …, d - 1) from c to x and g(x) := hol_U(γ_x), every link b ⊂ B
  obeys **||(g·U)_b - 1|| ≤ (d - 1)h_Bε**. *Planned: PROVEN-HERE ⇐ MSG_0 proof steps (2)-(3) with the reference field 1, and (F4) (not counted).*
- **Proposition GF-B (computer-assisted; locally small backgrounds).** Fix R_t := 5 and w > 0. Let K̃ be the finite-range scalar kernel
  of s6 B (the inverse of 𝒦^{sc} on the torus of 2R_t + 1 blocks, restricted to |Z|_∞ ≤ R_t; at the representatives 0 ≤ Z_1 ≤ … ≤ Z_4 ≤ R_t it
  is a fixed array of floating-point (dyadic) numbers, and elsewhere it is DEFINED by the hyperoctahedral relabelling K̃(Z)[a, b] :=
  K̃(r(Z))[π_Z(a), π_Z(b)]). Let E := 𝒦^{sc}K̃ - 1 (computed for every |Z|_∞ ≤ R_t + 1; E = 0 beyond), W := diag(1_Λ, w) on the equation space,
  D := diag(1, L^d) on the input (ω, η), and let s6 B certify (floating point with a priori rounding bounds, Higham's γ_n) upper bounds
  k_0 ≥ |||P_λK̃D|||_sp, k_1 ≥ |||P_λK̃W^{-1}|||, k_3 ≥ |||K̃W^{-1}|||, k_4 ≥ |||K̃D|||_sp, e_1 ≥ |||WEW^{-1}|||, e_2 ≥ |||WED|||_sp. Let the torus have
  n_T ≥ 2R_t + 3 blocks per side and let every fine plaquette in every box of blocks within ℓ^∞-distance R_t + 1 of a block have
  ||1 - U_p|| ≤ ε. Put δ := (d - 1)(L(R_t + 1) + h)ε and c_Δ(w) := (2d + 1)·4d + 2dh√(L^d - 1)(1 + w). If e_1 + c_Δδk_3 < 1, then
    **G_∞(U) ≤ G^♯(δ) := k_0 + k_1(e_2 + c_Δδk_4)/(1 - e_1 - c_Δδk_3).**
  *Planned: PROVEN-HERE ⇐ KKT, BOXG, (F2)-type bound ||Ad(V) - 1|| ≤ 2||V - 1||, and s6 B's certified numbers (computer-assisted; not
  counted).* Pre-registered expectation (s6 criteria): e_1 < ½ and G^♯(0) ≤ 10³. *Expected failure mode:* e_1 ≥ 1 at R_t = 5 (truncation
  too short); then R_t is raised and the run is reported as a second run.
- **Corollary CHAIN-6 (the radius chain with the sharpened G_∞).** FP-uniq, FP-sh, MSG_0 and DX-rel hold verbatim with G_∞ replaced by any
  upper bound for G_∞(U). With G^♯ (locally small backgrounds, as in GF-B) the chain (I1)-(I4), (S0) is re-solved in s6 C, giving new
  ζ, s_0, r_*, r_sol, τ_c, ρ_band and the (TH-bg) ceiling; with G^A likewise. *Planned: PROVEN-HERE (substitution + arithmetic; not counted).*
  The smallness hypothesis of GF-B (ε ≤ the GF-B threshold) is implied by FP-sh's ε_bg ≤ τ_c/2 once τ_c is below it (checked in s6 C).

### 18.2 STEP 3: (DX-loc) and (GF-dec)_k
- **Lemma FH (frozen holes; every background).** For a set 𝔥 of blocks let Λ^𝔥 := {λ ∈ Λ : λ = 0 on every block of 𝔥}, Λ_res^{U,𝔥} := Λ^𝔥 ∩ Λ_res^U,
  and (χ_UΓ)^𝔥 := (M_U, P^𝔥_resD_U^*D_U) on Λ^𝔥 (P^𝔥_res the orthogonal projection onto Λ_res^{U,𝔥}; equations only on blocks ∉ 𝔥). Then
  (χ_UΓ)^𝔥 is invertible, and Lemma CD, CHEB, RINV and Proposition GF-A hold for it verbatim, with the same constants, for every 𝔥 and
  every background. *Planned: PROVEN-HERE (not counted).*
- **(DX-loc), decomposed.** (DX-loc) = (DX-loc-1) the frozen-hole gauge fixing on the complement of the holes and of the rough-V set
  (FP-uniq/FP-sh with (χ_UΓ)^𝔥), (DX-loc-2) the hole normalisation relative to the reference, (DX-loc-3) the decoupling across ∂R(D) (a
  decay statement, DR-1), (DX-loc-4) a local form of BR1 (CH-3) [RSF6-fix FP-2: the "rough-V set" belongs to (DX-loc-4), not to
  (DX-loc-1): on ∂Λ′ the background U(V) is defined only through a local BR1]. Session 6 proves FH (the every-background part of (DX-loc-1)), states which
  constant enters (DX-loc-1) and names the rest. *Expected outcome:* (DX-loc-1) holds with G^A in place of G^♯ (FH), and a G^♯-type bound
  for frozen holes is a separate certificate (named (GF-B^𝔥)); (DX-loc-2)-(DX-loc-4) are named, not proven.
- **(GF-dec)_k (k ≥ 1).** Not attempted beyond a remark: Lemmas CD, CHEB, RINV use only (a) λ(c_X) = 0 at the block centres, (b) a
  block-diagonal M with a single-link right inverse, (c) range-1 D^*D. At k ≥ 1 the open input is (b) for NA-FP's composite slice.

## 19. Session-6 proofs (written from 07:27 UTC; after §18 (07:16:13 UTC), after the s6 criteria (07:18:35 UTC) and after the single s6 run (07:23:55-07:24:28 UTC); corrections made while proving are marked [post-proof])

### 19.1 STEP 2, every-background tier

**Lemma CD: PROVEN (citation; not counted).** PROOF Lemma FPq (i) [S20, PROVEN]: |(D_Uλ)_b| = |Ad(U_b)λ(y) - λ(x)| ≥ ||λ(y)| - |λ(x)||
(Ad orthogonal), so ||D_Uλ||² ≥ Σ_{b intra-block}(f(y) - f(x))² for the scalar f := |λ|, which vanishes at every block centre; the
block-internal Neumann Laplacian with a Dirichlet point at the centre has lowest eigenvalue ≥ 2663/31250. Nothing about U is used.
For λ ∈ Λ_res^U ⊂ Λ, ⟨λ, G_resλ⟩ = ||D_Uλ||² ∈ [c_D^K, 4d]||λ||² (the upper bound as in GF-dec (b)). ∎ (s6 A1, exact: the Fraction LDLᵀ of
H - (2663/31250)·1 (80×80) has all pivots > 0, the smallest 1.12·10⁻⁴; A1n: at c = 0.0853 a pivot < 0 appears. Float λ_min(H) = 0.0852175382.
This re-certifies PROOF's c36 number independently. The gain over GF-dec (b)'s 1/324 is a factor 27.6: the telescoping along one
axial path wastes the other paths.)

**Lemma CHEB: PROVEN-HERE (not counted).** *Proof.* ||G^{-1}|| ≤ 1/a gives the first bound. Let D ≥ 1, t(x) := (b + a - 2x)/(b - a) (so t maps
[a, b] onto [-1, 1] and t(0) = σ > 1) and p(x) := (1 - T_D(t(x))/T_D(σ))/x. The numerator is a polynomial of degree D vanishing at x = 0, so
p is a polynomial of degree D - 1. G has block range 1, so G^k(X, Y) = 0 for |X - Y|_∞ > k, hence p(G)(X, Y) = 0 for |X - Y|_∞ = D. Then,
with P_X the orthogonal projection onto H_X, ||G^{-1}(X, Y)|| = ||P_X(G^{-1} - p(G))P_Y|| ≤ sup_{x∈[a,b]}|1/x - p(x)| = sup|T_D(t(x))|/(xT_D(σ)) ≤
1/(aT_D(σ)) (spectral theorem; |T_D| ≤ 1 on [-1, 1]). Finally T_D(σ) = cosh(Dθ) ≥ ½e^{Dθ}. ∎ (s6 A2, d = 2, 6×6 blocks, U = 1, two
Haar backgrounds and a smooth one: spectrum of G_res within [a, 8] (A2b); ||G_res^{-1}(X, Y)||aT_D(σ) ≤ 0.28 for every pair; negative control
A2n: the claimed rate 10θ is violated (ratio up to 3.1·10³).) *Reading.* This is Demko-Moss-Smith's argument; the rate is θ ≈ 2√(a/b)
instead of the Neumann a/b.

**Lemma RINV: PROVEN-HERE (not counted).** *Proof.* For y = c_X + s every axial path from c_X to y is the single link, so M_U(vδ_y) =
L^{-d}Ad(T_s)v (GF-dec (a)'s computation). Hence M_UR_Uη = Σ_sL^{-d}(L^d/(2d))η_X = η_X, and R_Uη_X ∈ Λ (c_X + s ≠ c_X). ||R_U(X, X)η||² =
2d(L^d/(2d))²|η|². For c_R take λ := R_Uη supported in B(Y), |λ(c + s)| = a := (L^d/(2d))|η|. (D_U^*D_Uλ)(z) = 2dλ(z) - Σ_{z′~z}Ad(·)λ(z′) (the
diagonal of D_U^*D_U is exactly 2d·1). The sites c + s are pairwise non-adjacent, so the value at c + s has norm 2da. The centre is
removed by P_Λ. A site c + s + s′ (s′ ≠ ±s; 2d(d - 1) of them, all in B(Y) since L ≥ 3) touches two support sites: norm ≤ 2a. A site
c + 2s touches one: norm ≤ a; at L = 3 it lies in B(Y + s). All other values vanish. P_res^U is block-diagonal with norm 1. So
||(P_resD^*DR)(Y, Y)|| ≤ (L^d/(2d))√(2d(2d)² + 4·2d(d - 1)) and ||(P_resD^*DR)(Y + s, Y)|| ≤ L^d/(2d); a row of blocks Z meets the
columns Y = Z and Y = Z - s; the sum is ≤ c_R. ∎ (s6 A3, d = 2, four backgrounds: ||MR - 1|| ≤ 6.7·10⁻¹⁶, ||R(X, X)|| = 4.5 exactly,
measured |||P_resD^*DR||| = 0.92-0.945·c_R(2): the count is tight.)

**Proposition GF-A: PROVEN-HERE (not counted).** *Proof.* GF-dec (d)'s proof uses of M_U^+ only that it is a right inverse with values
in Λ; so (χ_UΓ)^{-1}(η, ω) = R_Uη + G_res^{-1}(ω - P_res^UD_U^*D_UR_Uη) (RINV). With Γ_1 ≥ |||G_res^{-1}||| (CD + CHEB: at most N_D blocks at
distance D) the η-columns have row sum ≤ L^d/√(2d) + Γ_1c_R and the ω-columns ≤ Γ_1. The entry bound: ||K(X, Y)|| ≤ δ_{XY}L^d/√(2d) +
g(D) + Σ_{|Z-Y|≤1}g(|X - Z|)||(P_resD^*DR)(Z, Y)|| with g(D′) ≤ (2/a)e^{-θD′} and |X - Z| ≥ D - 1; the column sums of P_resD^*DR are ≤ c_R by the
same count. ∎ *Numbers (s6 A4, mpmath, 60 digits; the tail beyond D = 20000 is bounded explicitly and is < 10⁻³⁰⁰ of Γ_1):* σ = 1.01070904,
**θ = m_FP^A = 0.146219 per block** (session 5: 3.858·10⁻⁴), Γ_1 = 1.951447·10⁷, c_R = 330.6588, **G^A = 6.472145·10⁹** (session 5:
5.8954·10²³; factor 9.11·10¹³). Every constant is background-independent and N-independent.

### 19.2 STEP 2, locally small backgrounds

**Lemma KKT: PROVEN-HERE (not counted).** *Proof.* Injectivity: if P_ΛD_U^*D_Uλ = M′_U^Tμ and M′_Uλ = 0, then λ ∈ Λ_res^U and ||D_Uλ||² =
⟨λ, P_ΛD^*Dλ⟩ = ⟨M′λ, μ⟩ = 0, so λ = 0 (CD); then M′^Tμ = 0, so μ = 0 (σ_min(M_X) ≥ L^{-d}, GF-dec (a)). Finite dimension gives invertibility.
If 𝒦_U(λ, μ) = (ω, L^dη) with ω ∈ Λ_res^U, then M_Uλ = η, and applying P_res^U (P_resP_Λ = P_res; ran M′^T = Λ ⊖ Λ_res^U, so P_resM′^T = 0)
gives P_res^UD_U^*D_Uλ = ω; so χ_UΓλ = (η, ω) and λ = (χ_UΓ)^{-1}(η, ω) (NA-FP (ii)). At U = 1 every Ad is 1, D^*D has diagonal 2d and
off-diagonal -1, and M′_1λ(X) = Σ_{y∈B(X)}λ(y), so 𝒦_1 = 𝒦^{sc} ⊗ 1 with entries in {0, ±1, 2d}. Covariance: (D_{g·U}λ)_b = Ad(g(x))(D_U(Ad(g)^{-1}λ))_b
and the axial transports of g·U are g(c_X)Tg(y)^{-1}, so M′_{g·U} = Ad(g(c_·))M′_UAd(g)^{-1}; Λ is preserved. ∎

**Lemma BOXG: PROVEN-HERE (not counted).** *Proof.* hol_{g·W}(γ: z → z′) = g(z)hol_W(γ)g(z′)^{-1}, so with g(x) = hol_U(γ_x),
(g·U)_b = hol_U(γ_xbγ_y^{-1}) (MSG_0 step (2) with the reference field 1). The closed loop γ_xbγ_y^{-1} is spanned by a ladder of
Σ_{ν>μ}|x_ν - c_ν| ≤ (d - 1)h_B plaquettes inside the box spanned by c, x, y ⊂ B (MSG_0 step (3)). (F4) gives the bound. ∎

**Proposition GF-B: PROVEN-HERE, computer-assisted (not counted).** *Proof.* (1) *U = 1.* E is supported in |Z|_∞ ≤ R_t + 1 (𝒦^{sc} has
range 1, K̃ range R_t), so on a torus with n_T ≥ 2R_t + 3 the translates do not overlap and 𝒦_1K̃ = 1 + E holds there exactly. (2) *Gauge
per column.* For a block Y let B_Y be the fine box of the blocks within ℓ^∞-distance R_t + 1 of Y (centre c_Y, h_B = L(R_t + 1) + h; it
does not wrap since n_T ≥ 2R_t + 3) and g^{(Y)} its BOXG gauge (extended by 1 outside B_Y): every link of B_Y has ||(g^{(Y)}·U)_b - 1|| ≤ δ.
Let 𝔊^{(Y)} be the orthogonal map acting by Ad(g^{(Y)}) at sites and at block centres, and define K̃_U(X, Y) := (𝔊_X^{(Y)})^{-1}(K̃(X - Y) ⊗ 1)𝔊_Y^{(Y)}.
By KKT's covariance, (𝒦_UK̃_U)(X, Y) = (𝔊_X^{(Y)})^{-1}[δ_{XY} + E(X - Y) + (Δ^{(Y)}K̃(· - Y))(X)]𝔊_Y^{(Y)}, Δ^{(Y)} := 𝒦_{g^{(Y)}·U} - 𝒦_1, and only
entries of Δ^{(Y)} between blocks of the box enter (the Laplacian couplings between blocks at distance ≤ R_t and ≤ R_t + 1 from Y, and the
block-diagonal M′, M′^T at distance ≤ R_t). (3) *Size of Δ.* ||Ad(V) - 1|| ≤ 2||V - 1|| (Ad(V)X - X = (V - 1)XV^{-1} + X(V^{-1} - 1)). Laplacian
part: entries -(Ad(·) - 1) of norm ≤ 2δ, ≤ 2d per row and column, so each block entry is ≤ 4dδ and a row meets 2d + 1 blocks. M′ part: an
axial transport has ≤ dh links, so ||T - 1|| ≤ dhδ, each site entry of M′_{gU} - M′_1 is ≤ 2dhδ and the (1 × (L^d - 1)) row has norm
≤ 2dh√(L^d - 1)δ; the same for the column -M′^T. With W on the equation space: |||WΔ^{(·)}||| ≤ c_Δ(w)δ. [RSF6-fix GB-1: "|||WΔ^{(·)}|||" is
not a defined object, since Δ^{(Y)} depends on the column Y. What is used: the entry bound b(X, Z) := (the bounds just derived for
||WΔ^{(Y)}(X, Z)W^{-1}||, nonzero only for |X - Z|_∞ ≤ 1) holds for EVERY Y whose box contains X and Z, i.e. it is uniform in Y, and
sup_XΣ_Zb(X, Z) ≤ c_Δ(w)δ. Hence sup_XΣ_Y||Σ_ZWΔ^{(Y)}(X, Z)K̃(Z - Y)W^{-1}|| ≤ sup_XΣ_Zb(X, Z)·sup_ZΣ_Y||K̃(Z - Y)W^{-1}|| ≤ c_Δ(w)δk_3,
and the same with D in place of W^{-1} (k_4). This is the only property of Δ^{(·)} that step (4) uses.] (4) *Neumann.* With E_U :=
𝒦_UK̃_U - 1, all block norms are 𝔊-invariant, so |||WE_UW^{-1}||| ≤ e_1 + c_Δδk_3 =: ε_W < 1 and |||WE_UD|||_sp ≤ e_2 + c_Δδk_4. Then
𝒦_UK̃_UW^{-1} = W^{-1}(1 + WE_UW^{-1}) is invertible, 𝒦_U^{-1} = K̃_U - K̃_UW^{-1}(1 + WE_UW^{-1})^{-1}WE_U (|||·||| is submultiplicative, so the
Neumann series converges), and with KKT, G_∞(U) ≤ |||P_λ𝒦_U^{-1}D|||_sp ≤ k_0 + k_1(e_2 + c_Δδk_4)/(1 - ε_W) (ω ∈ Λ_res^U ⊂ Λ only lowers the norm). (5)
*The certificate (s6 B2).* K̃ at the 126 representatives is a fixed float array (exact dyadic numbers), so its norms are exact
numbers, bounded by min{Frobenius, √(||BᵀB||_∞)} of B = |K̃| with rounding margins; K̃(Z) for other Z is a row/column permutation of a
representative, so the Z-sums are orbit-size multiples. E(Z) was computed for all 28561 blocks |Z|_∞ ≤ 6: the products by entries of
𝒦^{sc} ∈ {0, ±1, 8} are exact, so the only rounding is in sums of ≤ 730 terms, bounded entrywise by γ_730·(|𝒦^{sc}||K̃|) (Higham; any
summation order of classical dgemm); norms of B = |E| + that bound as above; every sum inflated by (1 + 10⁻⁹), which dominates the
accumulated relative rounding (≤ 10⁻¹⁰). ∎
*The certified numbers (s6 B2, w = 1000):* k_0 = 36.826073, k_1 = 3.272490, k_3 = 3.307759, k_4 = 37.577884, e_1 = 3.3377·10⁻³, e_2 = 6.6078·10⁻²,
**G^♯(0) = 37.043038** (w = 1: 37.057157). Residual: max entry bound 9.3·10⁻⁷, at the truncation shells only (inner |Z| ≤ 4: 1.9·10⁻¹³).
*Uniform form (hand arithmetic from the certified w = 1 numbers, c_Δ(1) = 287.108):* **for every background whose plaquettes are ≤ 10⁻⁶ on
every R_t + 1 box, G_∞(U) ≤ 39.36** (δ = 5.7·10⁻⁵, ε_W = 0.0612). At ε ≤ τ_c/2 (C1 below) δ = 3.1·10⁻¹³ and G_∞(U) ≤ 37.04304.
*Tightness (B3):* the float estimate of the U = 1 value is G_est = 35.7303, so G^♯(0)/G_est = 1.037. *End-to-end test (B4, d = 2, the same
construction):* on a 13×13-block torus with a Haar-random gauge times links within ≈ 2·10⁻⁶ of 1 (plaquettes ≤ 4.7·10⁻⁶), the measured
G_∞(U) = 8.689587 ≤ G^♯(δ) = 9.2278 (w = 1); |G_meas(U) - G_meas(1)| = 5·10⁻⁸ relative (B4b); in the original gauge the entries of 𝒦_U and
𝒦_1 differ by up to 2.0 (B4c), so BOXG's gauge is load-bearing; at a rough Haar background G_meas = 11.97 (B4n, hypothesis violated).
*Scope.* d = 4, L = 3, every N (the U = 1 operator is scalar ⊗ 1_{su(N)}, the perturbation constants are N-free); tori of n_T ≥ 13 blocks
(stage 0 has far more); only a LOCAL plaquette bound is used (compatible with CH-3's V-scope). A frozen hole is NOT covered (§19.3).
[RSF6-fix GB-2 (non-binding): "only a LOCAL plaquette bound is used" overstates it. G_∞(U) is a sup over all blocks, so the hypothesis
(plaquettes ≤ ε on every R_t + 1 box) is needed on EVERY box of the torus. On 𝒱^sf(Λ′) with rough V outside Λ′, GF-B does not apply as
stated; that needs a boundary version, of the (GF-B^𝔥) type. Independent confirmation (REVIEW_SF_S6 C-3, the reviewer's own BLAS-free code
with directed rounding): G^♯(0) ≤ 36.5473 (≤ 38.37 at plaquettes ≤ 10⁻⁶, w = 1), consistent with SF's 37.0430; SF's number is kept.]

**Corollary CHAIN-6: PROVEN-HERE (not counted).** *Proof.* FP-uniq's proof uses G_∞ only through its step (2), i.e. through the defining
inequality of G_∞(U); FP-sh, MSG_0 and DX-rel use it only through τ_c. Substitute an upper bound and re-solve the arithmetic. ∎
*Numbers (s6 C, mpmath 60 digits, operating point 0.99ζ_max, ρ = 504.5; N = 3):*
| quantity | session 5 (G = 5.8954·10²³) | **G^A = 6.4721·10⁹ (every background, frozen holes too)** | **G^♯ = 37.0430 (locally small, no hole)** |
|---|---|---|---|
| ζ | 2.188·10⁻⁵⁵ | 1.816·10⁻²⁷ | 5.545·10⁻¹¹ |
| r_* / r_sol | 5.16·10⁻³¹ / 1.03·10⁻³⁰ | 4.70·10⁻¹⁷ / 9.40·10⁻¹⁷ | 8.22·10⁻⁹ / 1.64·10⁻⁸ |
| **τ_c** | 4.34·10⁻⁵⁹ | **3.602·10⁻³¹** | **1.0995·10⁻¹⁴** |
| ρ_band | 2.28·10⁻⁶¹ | 1.89·10⁻³³ | 5.78·10⁻¹⁷ |
| ε_bg^{(TH-bg)} (a_p entry) | 2.51·10⁻⁶² | 2.08·10⁻³⁴ | 6.36·10⁻¹⁸ |
| (TH-ch′) ε_1 ≤ (C_bg = 1.39·10⁴⁰) | 1.81·10⁻¹⁰² | **1.50·10⁻⁷⁴** | **4.59·10⁻⁵⁸** |
(I1) = 0.4950 and (I4)/r ≈ 0.9997 at both operating points; (S0) holds; at ε = τ_c/2 GF-B's hypothesis holds with ε_W = 3.34·10⁻³ (C1).
~~**The ε_1 ceiling is now set by C_bg = 1.39·10⁴⁰ (BR1 (iii)), not by G_∞:** τ_c/(2C_bg) and ε_bg^{(TH-bg)}/C_bg are both ∝ 1/C_bg.~~
[RSF6-fix TH-2 (binding): the sentence above and the (TH-ch′) row of this table are WRONG as ε_1 ceilings. BR1 itself holds only for
ε_V ≤ ε ≤ ε_br (PROOF l.5663-5664), and ε_br ∋ 1/(24𝔠_∞²C_♭) = 1.04·10⁻⁷⁶/C_♭ at 𝔠_∞ = 2.0·10³⁷. With ε_V ≤ 1.011√Nε_1 this gives
**ε_1 ≤ ε_br/(1.011√N) ≤ 5.95·10⁻⁷⁷/C_♭** (N = 3), C_♭ (Lemma N5-an♭) not evaluated. It binds below the τ^A entry 1.50·10⁻⁷⁴ unless
C_♭ ≲ 4·10⁻³, and below the τ^♯ entry 4.59·10⁻⁵⁸ unless C_♭ ≲ 10⁻¹⁹; the row is read as "≤ min{this row, 5.95·10⁻⁷⁷/C_♭}". Both ε_1
entries are 𝔠_∞-driven (∝ 𝔠_∞^{-1} via C_bg, ∝ 𝔠_∞^{-2} via ε_br); G_∞ and τ_c do not set ε_1. See (TH-ch″) in §16.3 and the corrected
§19.4.]

### 19.3 STEP 3: frozen holes and (DX-loc)

**Lemma FH: PROVEN-HERE (not counted).** *Proof.* Λ^𝔥 ⊂ Λ, so CD holds on it (the Kato bound is block by block) and ⟨λ, G^𝔥_resλ⟩ =
||D_Uλ||² ∈ [c_D^K, 4d]||λ||² on Λ_res^{U,𝔥}. G^𝔥_res is the compression of D_U^*D_U, so it has block range 1. M_U is block-diagonal, so
Λ_res^{U,𝔥} = ⊕_{X∉𝔥}Λ_{res,X} and R_U restricted to blocks ∉ 𝔥 is a right inverse; RINV's count only decreases (some neighbours are frozen).
Invertibility and the formula of GF-A follow as before (injectivity from CD; matching dimensions block by block). ∎ (s6 D1, d = 2,
three frozen blocks, U = 1 and Haar: spectrum within [a, 8], CHEB ratio ≤ 0.28. D2 (report): at U = 1 the frozen hole changes the
measured G_∞ from 8.4551 to 8.4574.)
[RSF6-fix FP-1 (binding): the heading and statement struck through below are WRONG as written (with g = 1 on hole sites the boundary
links are not small); they are replaced by the two-step statement that follows them, which is what the [post-proof] correction proves.]
~~**Corollary FP^𝔥 ((DX-loc-1) with G^A): PROVEN-HERE (verbatim transposition; not counted).** Let 𝔥 be the hole blocks (DX-rel's R(D):
the blocks within coarse distance 1 of the defect-carrying blocks) and 𝒢_V^𝔥 := {g ∈ 𝒢_V : g = 1 on the sites of 𝔥}. FP-uniq and FP-sh hold
with 𝒢_V^𝔥, χ_U^𝔥 (equations on blocks ∉ 𝔥), Λ^𝔥 and G_∞ := G^A, at τ_c := τ^A.~~
**Corollary FP^𝔥 ((DX-loc-1) for fluctuation holes, with G^A), restated [RSF6-fix FP-1]: PROVEN-HERE in this two-step form (not counted).**
Let 𝔥 be the hole blocks (DX-rel's R(D): the blocks within coarse distance 1 of the defect-carrying blocks), and let U(V) exist globally
(BR1 with the global ε_V; FP-2 below). (i) Fix the gauge at the sites of every hole block by the exact block-internal complete axial
gauge ((g·U_0)_b = U_b on the axial tree of B(Y), g(c_Y) = 1; Jacobian 1, no Gribov copy). (ii) On the rest, FP-sh^𝔥: FP-uniq and FP-sh
hold with 𝒢_V^𝔥 := {g ∈ 𝒢_V : g = 1 on the sites of 𝔥}, (χ_UΓ)^𝔥 (equations on blocks ∉ 𝔥; Lemma FH), Λ^𝔥 (measured from the axially
fixed hole blocks) and G_∞ := G^A, at τ_c := τ^A. [RSF6-fix FP-2 (binding, scope): this covers the fluctuation holes R(D) when U(V)
exists globally. It does NOT cover the rough-V boundary ∂Λ′ of CH-3, where U(V) itself is defined only via (DX-loc-4).] *Proof (of the
struck statement, kept for the record; the valid proof is the [post-proof] two-step argument after it).* The changes: every link with a block pair not
both in 𝔥 has both blocks free of defects (a non-hole block has no defect-carrying neighbour), so MSG_0 holds on it; the linearisation
of Φ^𝔥 is -(χ_UΓ)^𝔥 (FH); the hole links are integrated with their Haar measure, untouched by 𝒢_V^𝔥; the rest of both proofs is unchanged. ∎
[post-proof correction (found on re-reading; the statement above is incomplete as written). With g = 1 on the hole sites, the base
point g_ax^∁ (= g_ax off 𝔥, 1 on 𝔥) gives (g_ax^∁·U_0)_b = g_ax(x)U_{0,b} on a link b from a non-hole block X to a hole block Y, which is NOT
small in general. Corrected construction: **first fix the gauge at the sites of every hole block by the block-internal complete axial
gauge** ((g·U_0)_b = U_b on the axial tree of B(Y), g(c_Y) = 1): this is exact (each tree link is in bijection with one gauge variable,
Jacobian 1, no Gribov copy), its solution is MSG_0's g_ax restricted to B(Y), and it involves only links inside B(Y). The remaining
integrand is invariant under 𝒢_V^𝔥 (tree links of B(Y) have both ends in B(Y)). After it, g_ax = 1 on hole sites, so on a boundary link
the base point is MSG_0's axial representative; the hole block Y adjacent to a non-hole block carries no defect (else X would be in 𝔥),
so MSG_0 bounds A^0_b. Then FP-sh^𝔥 with 𝒢_V^𝔥 as above. The statement holds for this two-step fixing; λ = 0 on 𝔥 is measured from the
axially fixed hole blocks, which is FH's frozen set.]
**Consequence for τ_c (recorded honestly).** E_good itself (no defect anywhere) may use τ^♯ (GF-B). But (CH-c)'s complement charts
are frozen-hole charts at the same threshold, and they are covered only with G^A. Defining defects at τ^A everywhere is consistent
(E_good(τ^A) ⊂ E_good(τ^♯)'s domain of validity). So **the PROVEN admissible stage-0 threshold is τ_c = τ^A = 3.60·10⁻³¹**, and **τ_c = τ^♯ =
1.10·10⁻¹⁴ ⇐ (GF-B^𝔥)** [OPEN, new name: a G^♯-type certificate for (χ_UΓ)^𝔥 uniform over hole shapes; D2's 0.03% change is evidence
that it holds with nearly the same constant, not a proof]. A route to (GF-B^𝔥): an approximate inverse with a boundary layer at the hole
(the extra residual is the hop into frozen blocks, of size ≈ Σ_{Z≠0}||K̃(Z)|| on face sites, O(1) as is), or a Schur complement over the hole.
**(DX-loc), the rest named:**
- (DX-loc-2) the hole normalisation relative to the reference: ARGUED. Upper: the hole integral over Haar (volume 1) is ≤ the sup of
  the integrand ≤ DX-rel's price × the background value. Lower: the in-chart reference on the hole links is ≥ the background value ×
  (c_Nu_0^{-1/2})^{(N²-1)|R|}e^{-C|R|}, because the background is critical for the full stage-0 integrand (BR1 (ii)), so there is no linear term
  and |A_b| ≤ u_0^{-1/2} costs O(1) per link. Ratio per defect ≤ e^{-u_0a/2}(Cu_0)^{(N²-1)n_R/2}: this is the DX-rel ceiling of DX′-1. The
  gauge-fixing Jacobian on the hole boundary is not written. [RSF6-fix E-3 (nit): the ball's Haar volume is (c_Nu_0^{-(N²-1)/2})^{|R|},
  not (c_Nu_0^{-1/2})^{(N²-1)|R|}.]
- (DX-loc-3) decoupling across ∂R(D): ~~the covariance part is in hand~~ [RSF6-fix E-4: read "CHEB applies (positivity + finite range
  r_1; rate not evaluated); not a counted item"] (the compression of Õ to the non-hole links has spectrum in
  [λ_min(Õ), ||Õ||] and range r_1, so CHEB gives decay uniform in the hole shape, at rate ≈ 2√(λ_min/||Õ||)/r_1, not evaluated); the FP part is
  (FP-det)^𝔥 [ARGUED, as (FP-det), now with FH's rate m_FP^A = 0.1462]; the polymer decoupling of the reference across ∂R(D) itself is
  OPEN (a decay statement, DR-1).
- (DX-loc-4) a local form of BR1 (its (i) is a global contraction in ε_V): OPEN.
- (GF-B^𝔥): OPEN (above).
**(GF-dec)_k, k ≥ 1:** not attempted. CD, CHEB, RINV use only (a) λ = 0 at the block centres, (b) a block-diagonal M with a single-link
right inverse, (c) a range-1 D^*D. At k ≥ 1 the open input is (b) for NA-FP's composite slice M^{(k)}_U; the name stays OPEN.

### 19.4 Derived constants after session 6 ((TH-ch′); s6 C; scaling each source's own reference value)
| item | session 5 + TH-1 (ε_1 = 1.81·10⁻¹⁰²) | **τ^A, PROVEN (ε_1 = 1.50·10⁻⁷⁴)** | τ^♯ ⇐ (GF-B^𝔥) (ε_1 = 4.59·10⁻⁵⁸) |
|---|---|---|---|
| RLARGE n_* (SU(2)/SU(3)) | 2.9·10²⁰⁵ / 1.9·10²⁰⁵ | **4.2·10¹⁴⁹ / 2.8·10¹⁴⁹** | 4.5·10¹¹⁶ / 3.0·10¹¹⁶ |
| HIST n_♯ joint route | 4·10²¹⁴-3·10²¹⁸ | 5.5·10¹⁵⁸-4.4·10¹⁶² | 5.9·10¹²⁵-4.8·10¹²⁹ |
| HIST n_♯ RS route | 2·10⁴¹⁹-2·10⁴²³ | ≈ 5·10³⁰⁷-4·10³¹¹ [post-proof: s6 printed "inf" for the upper end, a float overflow in a REPORT line; ≈ 3·10¹⁷·(0.5/ε_1)⁴ by hand] | 5.6·10²⁴¹-4.2·10²⁴⁵ |
| HW a_bad | 1.7·10⁻²¹⁰ | 1.2·10⁻¹⁵⁴ | 1.1·10⁻¹²¹ |
| final levels under the torus caveat | ≈ 108 | ≈ 78 | ≈ 61 |
| g_{DX′}²·C_ΩN′²f⁸ (RW-ℓ² / product-rule gap) | 1.5·10⁻²³⁷ / 1.6·10⁻³⁰⁹ | 7.3·10⁻¹⁸⁰ / 7.8·10⁻²⁵² | 5.1·10⁻¹⁴⁵ / 5.4·10⁻²¹⁷ |
| DX-rel hole ceiling g_0² | 1.6·10⁻¹²⁶ | 2.0·10⁻⁷⁰ | 3.5·10⁻³⁷ |
| FS-1 truncation g_0² | 1.8·10⁻¹¹³ | 1.3·10⁻⁵⁷ | 1.2·10⁻²⁴ |
| band window g_0·max{N_r, 2N_μ} | 5.1·10⁻⁶⁷ | 4.2·10⁻³⁹ | 1.3·10⁻²² |
| a_*^B·N_r² | 1.1·10⁻¹²³ | 7.5·10⁻⁶⁸ | 7.0·10⁻³⁵ |
| FD-1: M/L ≥ (κ_c + log pref + 1)/m_FP | fails at M ≲ 10⁸ | **M ≥ 6.05·10⁴ fine spacings** (m_FP^A = 0.1462, pref 7.8·10³) | same |
The binding coupling ceiling g_* is DX′'s (≈ 10⁻⁹⁰ in g_0 at τ^A with RW-ℓ²'s gap, before the unevaluated N′, C_Ω). All are finite,
g-independent and K-independent. ~~The two remaining levers are now C_bg (BR1 (iii)'s 𝔠_∞ ≈ 2·10³⁷) for ε_1, and (GF-B^𝔥) for τ_c.~~
[RSF6-fix TH-2 (binding). The ε_1 columns of this table (ε_1 = 1.50·10⁻⁷⁴, resp. 4.59·10⁻⁵⁸) are NOT admissible: (TH-ch″) adds
ε_1 ≤ ε_br/(1.011√N) = 5.95·10⁻⁷⁷/C_♭ (N = 3), which binds in BOTH columns (unless C_♭ ≲ 4·10⁻³, resp. ≲ 10⁻¹⁹). The ε_1-driven rows
are therefore the same in both columns; at C_♭ = 1 (scaling each source's reference value, as above; the s7 F check reproduces the
arithmetic):
| ε_1-driven item | scaling | at ε_1 = 5.95·10⁻⁷⁷/C_♭, C_♭ = 1 (both τ columns) |
|---|---|---|
| RLARGE n_* (SU(2)/SU(3)) | ε_1^{-2} | 2.7·10¹⁵⁴ / 1.8·10¹⁵⁴ (× C_♭²) |
| HIST n_♯ joint route | ε_1^{-2} | 3.5·10¹⁶³-2.8·10¹⁶⁷ |
| HIST n_♯ RS route | ε_1^{-4} | 2.0·10³¹⁷-1.5·10³²¹ |
| HW a_bad | ε_1² | 1.8·10⁻¹⁵⁹ (× C_♭^{-2}) |
| final levels under the torus caveat | log_3(n_*^{1/4}) | ≈ 81 |
The τ_c-driven rows (g_{DX′}², hole ceiling, FS-1, band window, a_*^B) are unchanged and keep their two columns. **The levers:**
𝔠_∞ (and C_♭) drive ε_1 (∝ 𝔠_∞^{-2}C_♭^{-1} through ε_br, ∝ 𝔠_∞^{-1} through C_bg); (GF-B^𝔥) drives only the τ_c rows (ρ_band, the DX′,
hole and FS-1 ceilings, the band window), not ε_1. Session 7 (§22) certifies a sharp 𝔠_∞.]

## 20. Session-6 outcome (written after §19)

### 20.1 Status changes
| item | status | note |
|---|---|---|
| [RSF5-fix] STEP 1 | applied (20 tags) | FP-uniq tightness; D3 failed positive control (D2 without demonstrated sensitivity); DX′-1 (ceilings evaluated); DX′-2 (re-tuned (B1′), j_max, a_*^B, window); FS-1, FS-2, FD-1, DR-1; CH-1 (DX-rel for every plaquette/mismatch > τ_c, inter-cube included); CH-2 (E10 OPEN; e^{B_0} a cost); CH-3 (𝒱^sf(Λ′), local ε_bg); TH-1 ((TH-ch′), C_bg = 1.39·10⁴⁰); O4 corrected; (CH-c) CONDITIONAL |
| Lemma CD | PROVEN (citation, re-certified exactly; not counted) | c_D^K = 2663/31250, 27.6× GF-dec (b) |
| Lemma CHEB | PROVEN-HERE (not counted) | Chebyshev decay, rate arccosh((b + a)/(b - a)) |
| Lemma RINV | PROVEN-HERE (not counted) | block-local right inverse; c_R = 330.66 (tight to 0.95 at d = 2) |
| **Proposition GF-A** | **PROVEN-HERE (not counted)** | **G_∞ ≤ 6.47·10⁹, m_FP^A = 0.1462 per block, every background, frozen holes too** |
| Lemma KKT | PROVEN-HERE (not counted) | bordered form; integer entries at U = 1; covariance |
| Lemma BOXG | PROVEN-HERE (not counted) | local axial gauge, ||(g·U)_b - 1|| ≤ (d - 1)h_Bε |
| **Proposition GF-B** | **PROVEN-HERE, computer-assisted (not counted)** | **G_∞ ≤ 37.0430 (≤ 39.36 for local plaquettes ≤ 10⁻⁶); tori ≥ 13 blocks; no hole** |
| Corollary CHAIN-6 | PROVEN-HERE (not counted) | τ^A = 3.60·10⁻³¹, τ^♯ = 1.10·10⁻¹⁴ |
| Lemma FH, Corollary FP^𝔥 | PROVEN-HERE (not counted) | (DX-loc-1) with G^A [RSF6-fix FP-1/FP-2: FP^𝔥 in its two-step form; fluctuation holes R(D) only, U(V) global] |
| (GF-B^𝔥) | OPEN, new name | needed for τ_c = τ^♯ on (CH-c)'s charts |
| (DX-loc) | OPEN, decomposed | (DX-loc-1) ~~PROVEN with G^A~~ [RSF6-fix FP-2: for fluctuation holes R(D), PROVEN with G^A; the ∂Λ′ part ⇐ (DX-loc-4)]; (DX-loc-2) ARGUED; (DX-loc-3) covariance decay in hand, FP part ARGUED, decoupling OPEN; (DX-loc-4) OPEN |
| (FP-det) | ARGUED (unchanged) | FD-1 now holds from M ≥ 6.05·10⁴ with m_FP^A |
| (GF-dec)_k | OPEN (unchanged) | input (b) at k ≥ 1 |

**Tally of this file after session 6 (unreviewed; base = REVIEW_SF_S5's corrected tally):**
- ~~**PROVEN-HERE 54 + 1 standard.** Counted 10: unchanged. Not counted 44: session 5's 34, plus CHEB, RINV, GF-A, KKT, BOXG, GF-B
  (computer-assisted), CHAIN-6, FH, FP^𝔥, and CD (a citation, re-certified).~~ [RSF6-fix tally: **PROVEN-HERE 53 + 1 standard.** Counted
  10: unchanged. Not counted 43: session 5's 34, plus CHEB, RINV, GF-A, KKT, BOXG, GF-B (computer-assisted), CHAIN-6, FH, FP^𝔥 (two-step
  form, FP-1/FP-2). **Lemma CD is a PROVEN citation** (PROOF FPq (i)), re-certified, not PROVEN-HERE.]
- **CONDITIONAL 8:** SF-thr-k; CE-exp^k; SF-A2^0, CE-exp^0, CE-Q, CE-Q-col (statements on the integral, ⇐ (FP-det) + (BGC) + O0's thresholds);
  DX′ (⇐ (FP-det) + (BGC)); (CH-c) (⇐ DX-rel + (DX-loc) + RLARGE E10 + CH-3 scope).
- **ARGUED 4:** (CE-s); session-4 DX's a′ (superseded); (FP-det); (DX-loc-2).
- **OPEN names:** (DX-loc) (now = (DX-loc-3)'s decoupling + (DX-loc-4) + (GF-B^𝔥) for τ^♯); (GF-B^𝔥) new; (GF-dec)_k; RLARGE E10 (on lane F's path);
  (FP-loc)_k, (N5-reg)_k, (L-loc)_k [B-NA]; (CE-col)'s item (iv); (SF-irr) and the A4 items; (a5-G♯)/(G♯-patch), (R♯) at ψ^r [B-NA]; lane D:
  (MIN-reg), (a5-U), (a3-q).
- **Discharged this session:** RSF5 fixes CH-1, CH-2, CH-3, TH-1, DX′-1, DX′-2 (binding) and the non-binding notes; the "constants, not
  logic" risk of REVIEW_SF_S5 Part H is reduced by 44 orders in τ_c at locally small backgrounds [RSF6-fix: ⇐ (GF-B^𝔥); not on the
  proven path] and by 28 orders unconditionally.
- No RLARGE §4.2 row is discharged. No PROOF.md tally change is proposed.

### 20.2 What (SF^J)_0 now rests on
- A2 (gauge fixing): ⇐ (FP-det) [ARGUED] + (BGC) + O0's thresholds, on E_good; uniqueness PROVEN; G_∞ now PROVEN at 6.47·10⁹ (every
  background, frozen holes) and 37.04 (locally small, no hole).
- A3 band / deep: CE-Q-col with ρ_band (re-tuned, DX′-2) + DX′ + (DX-loc).
- A3 out-of-chart: (CH-c), CONDITIONAL ⇐ DX-rel + (DX-loc) + E10 + CH-3 scope. No branch (ii).
- Thresholds: τ_c = 3.60·10⁻³¹ PROVEN admissible; 1.10·10⁻¹⁴ ⇐ (GF-B^𝔥); ~~ε_1 ≤ 1.50·10⁻⁷⁴ (resp. 4.59·10⁻⁵⁸), set by C_bg.~~
  [RSF6-fix TH-2: ε_1 ≤ min{1.50·10⁻⁷⁴, 5.95·10⁻⁷⁷/C_♭} under (TH-ch″) (BR1's domain ε_V ≤ ε_br), in both τ columns; set by 𝔠_∞ and
  C_♭, not by C_bg alone and not by τ_c. Session 7 (§22) replaces 𝔠_∞.]

### 20.3 Check s6
- Provenance: criteria checks/s6_criteria.md born 07:18:35 UTC (md5 3964da2e…), before the script (born 07:21:58 UTC; pre-run desk
  fixes to 07:23:48, logged; no run had happened). Output checks/s6_out.txt (md5 7e123ac5…), record checks/s6_time.txt.
- Run: one run under the numeric lock, 07:23:55-07:24:28 UTC: load 2.13, nice 10, BLAS threads 1, 32.4 s, peak RSS 776 MB, exit 0, one
  rmdir.
- **OVERALL PASS 17/17.**
- Rigorous (proof inputs): A1 (exact), A4 (mpmath), B2 (floats with a priori bounds), C1-C2, F1 (arithmetic). Evidential: A2, A2b, A3,
  B1, B3, B4, B4b, D1. Negative controls: A1n, A2n, B4c. Reports: B4n, D2, C3, FD-1.
- Low power / caveats, recorded: A2-A3, B4, D1 are at d = 2 (d = 4 dense inverses exceed the memory budget); B2's rigour assumes classical
  dgemm summation (any order); the s6 "inf" in a REPORT line is a float overflow (§19.4).

# SESSION 7 (2026-10-28 UTC). Inputs read before 07:57 UTC: REVIEW_SF_S6.md (BINDING; in full; md5 cd663df8…), SF.md (62079998…, =
SF_LOG's session-6 final), SF_LOG.md (82083e0a…), PROOF.md 4a7bbccc… (Setting N5-0 l.5149-5158, N5-sl, N5-coer, N5-triv l.5169-5236,
Setting N5-bg l.5255-5272, N5-cov, AX, N5-an l.5274-5318, N5-sf0 l.5415-5481, N5-w0 l.5498-5524, RW-ℓ² l.5555-5588, 𝔠_∞ l.5596-5606,
U0, FPq, N5-an♭, BR1 l.5608-5704, l.5852-5870, CURV1 l.6000-6052), checks/c36_nah1.py part C (read only), the reviewer's
revSF6/indep_cert.py (read only).

## 21. PRE-STATED (session 7) (appended at 07:57:19 UTC, 2026-10-28, BEFORE any session-7 proof, before the [RSF6-fix] edits and before the s7 criteria; statements only)

### 21.0 Conventions for §21-§23
Setting N5-bg at level 0 (PROOF l.5255), d = 4, L = 3, κ_0 = 1 (the case in which PROOF evaluates its level-0 constants), N ≥ 2 any.
Õ_0 is PROOF's scalar trivial-background operator (Õ(1, 1) = Õ_0 ⊗ 1_{su(N)}); it acts on ℓ²(links of Z⁴) (or of a torus), commutes with
block translations, and has block range 1: Õ_0 = (A(Z))_Z, A(Z) the 324 × 324 matrix between the links based in block X + Z and in block
X, Z ∈ {-1, 0, 1}⁴. Its entries are rationals (PROOF N5-w0, c36 C). Π, 1 - Π, C_0 := Õ_0^{-1} - (1 - Π) as in PROOF (l.5260-5261). For a
kernel K on links, N_m(K) := sup_bΣ_{b'}|K|(b, b')e^{md(b,b')} with d the ℓ¹ distance of link base points (PROOF Setting N5-0), |K|(b, b') the
block norm (scalar case: |entry|). "Certified" means: exact rationals, or floating point with a priori rounding bounds (Higham γ_n) and
upward-rounded sums, as in GF-B (§19.2) and the reviewer's indep_cert.py. R_t (truncation radius, in blocks) and the weights m are chosen
after this section by exploratory runs that are logged and are not evidence.

### 21.1 STEP 1 (binding fixes of REVIEW_SF_S6 F-3; applied in place, tagged [RSF6-fix])
TH-2 ((TH-ch″) with BR1's domain ε_V ≤ ε_br; C_♭ carried; §19.4 ε_1-driven rows recomputed; l.2477, l.2537, l.2577 corrected), FP-1
(FP^𝔥 restated in its two-step form), FP-2 ((DX-loc-1) scoped to fluctuation holes; ∂Λ′ ⇐ (DX-loc-4)), GB-1 (the Y-uniform entry bound
behind |||WΔ^{(·)}K̃W^{-1}|||), tally (CD a citation; 53 + 1); non-binding A-1 (hole ceiling with min{a_p, a_c}), A-2, GB-2, E-3, E-4, the
"44 orders" sentence, the reviewer's independent G^♯(0) recorded.

### 21.2 STEP 2: a certificate for the level-0 sup-norm covariance constant 𝔠_∞ (the (𝔠_∞-cert) of REVIEW_SF_S6 Part D)
*Idea fixed before any session-7 computation:* PROOF's 𝔠_∞ is a walk-expansion bound driven by the proven rate (≈ 10⁻¹⁰). At the trivial
background Õ_0 is translation invariant and scalar ⊗ 1; a finite-range approximate inverse K̃ with a certified residual E bounds N_m(Õ_0^{-1})
directly (GF-B's method, with Õ_0 in place of 𝒦^{sc}). The step to backgrounds in N5-sf0's class 𝔑(α_*) needs no new analytic constant:
N5-sf0 defines α_* so that C_Δα_* ≤ γ_0/2, and N5-an's entrywise deviation bound is uniform in the gauge column (the GB-1 lesson).
- **Lemma HO (hyperoctahedral covariance).** For every element g of the hyperoctahedral group of Z⁴ fixing a block centre (axis permutations
  and reflections through the centre), the induced signed permutation P_g of links (a reflected link is reversed; reversal flips the sign of
  A_b at U = 1) satisfies A(gZ) = P_gA(Z)P_g^T for all Z, and the same for Π. *Planned: PROVEN-HERE, computer-assisted (exact rationals,
  s7 A); not counted.* *Expected failure mode:* the S4′ contour average or the slice average is not reflection symmetric; then the
  certificate is run without the symmetry reduction over the subgroup that is exact, or on all offsets.
- **Proposition CI-0 (certificate at the trivial background; computer-assisted).** Let K̃ = (K̃(Z))_{|Z|_∞≤R_t} be a fixed array of
  floating-point numbers at the hyperoctahedral representatives (defined elsewhere by K̃(gZ) := P_gK̃(Z)P_g^T), E := Õ_0K̃ - 1 on Z⁴ (supported in
  |Z|_∞ ≤ R_t + 1), and let s7 B certify upper bounds k_m ≥ N_m(|K̃|), k′_m ≥ N_m(|K̃ - (1 - Π)|), e_m ≥ N_m(|E|). If e_m < 1, then Õ_0 is invertible on
  ℓ²(links of Z⁴) and on every torus of T ≥ 2R_t + 3 blocks, and
    **N_m(|Õ_0^{-1}|) ≤ k_m/(1 - e_m),  N_m(|C_0|) ≤ 𝔠_m^♮ := k′_m + k_me_m/(1 - e_m),  λ_min(Õ_0) ≥ (1 - e_0)/k_0,  |C_0(b, b′)| ≤ 𝔠_m^♮e^{-md(b,b′)}.**
  *Planned: PROVEN-HERE ⇐ Lemma HO, the Schur test and s7 B's certified numbers (computer-assisted; not counted).* *Expected failure mode:*
  e_0 ≥ 1 at the affordable R_t (the decay of Õ_0^{-1} per block is slower than that of (χ_UΓ)^{-1}); then the run is reported as failed and a
  larger R_t is a second, separately reported run.
- **Proposition CI-bg (every background of 𝔑(α_*), real or complex).** Let δ := C_Δα_* (≤ γ_0/2 by N5-sf0's definition of α_*). If
  e_0 + δk_0 < 1, then for every (U, V) ∈ 𝔑(α_*) on a torus T ≥ max(T_0, 2R_t + 3):
    **N_0(|C(U, V)|) ≤ 𝔠_∞^♯ := k′_0 + δ + k_0(e_0 + δk_0)/(1 - e_0 - δk_0),**
  for real (U, V) λ_min(Õ(U, V)) ≥ (1 - e_0 - δk_0)/k_0, and the weighted form holds with δ → e^{mr_1}δ (r_1 = 8L - 4) in the e-terms.
  *Planned: PROVEN-HERE ⇐ CI-0, N5-cov, N5-an (entrywise form), N5-sf0 (a)'s gauges g_□ on Ω^+_□, the column-wise gauge of GF-B (2)
  (not counted).*
- **Corollary CI-BR1.** PROOF's 𝔠_∞ may be replaced by 𝔠_∞^♯ in Lemma BR1, Theorem NAH1 at level 0 and Lemma CURV1 (each uses 𝔠_∞ only as
  an upper bound for N_0(|C|) at backgrounds of 𝔑(α_*)); this is checked use by use. *Planned: PROVEN-HERE (substitution; not counted);
  scope κ_0 = 1, L = 3, d = 4, as PROOF's evaluated numbers.* Then C_bg, ε_br's 𝔠_∞-entries, (TH-ch″)'s ε_1 ceiling and the §19.4 rows are
  re-evaluated (arithmetic). C_♭ is evaluated only if a complete explicit bound for N5-an♭'s (r_♭, S_♭) can be written; otherwise it is
  carried symbolically and the missing input is named.
- **Lemma CHEB-f (decay of f(G) for f analytic on a Bernstein ellipse; citation + two lines).** For G as in Lemma CHEB with spectrum in
  [a, b] and f analytic with |f| ≤ M_ρ inside the Bernstein ellipse E_ρ of [a, b] (ρ > 1): ||f(G)(X, Y)|| ≤ 2M_ρρ^{-(D-1)}/(ρ - 1) for
  D = |X - Y|_∞ ≥ 1. Applied to f(x) = x^{±1/2} with the certified [a, b] it gives a rate for 𝒞 and Õ^{1/2} (the inputs of DL / DX′-1).
  *Planned: PROVEN (citation: Chebyshev truncation error for analytic functions, Trefethen ATAP Thm 8.2) + PROVEN-HERE application (not
  counted).*
- *DX′ re-evaluation.* With ||C|| ≤ 1/λ_min certified and the CHEB-f rate, DX′-1's ceiling is recomputed (arithmetic; N′, C_Ω stay symbolic).

### 21.3 STEP 3 (if time): (GF-B^𝔥)
- **(GF-B^𝔥), target statement.** For every frozen set 𝔥 and every background as in GF-B, G_∞^𝔥(U) := G_∞ of (χ_UΓ)^𝔥 is bounded by a
  certified constant of GF-B type, uniform in the shape of 𝔥. *Planned route:* an approximate inverse K̃^𝔥 equal to K̃ away from 𝔥, with the
  residual of the hop into frozen blocks bounded uniformly in the shape. *Expected outcome:* attempted only if STEP 2 finishes; otherwise it
  stays OPEN and is not touched.

## 22. Session-7 proofs (written from 08:25 UTC; after §21 (07:57:19 UTC), after the [RSF6-fix] edits (to 08:03:20 UTC), after the s7 criteria (08:12:41 UTC) and after the single s7 run (08:18:31-08:24:29 UTC))

### 22.1 Lemma HO: PROVEN-HERE, computer-assisted (not counted)
*Proof.* The group is generated by an axis transposition, a 4-cycle and one reflection through the block-0 centre; covariance under
generators gives it for the group. For each generator, every exact row of Õ_0 (and of 1 - Π) was mapped and compared entry by entry in
Fractions (s7 A2): 0 mismatches. A reflected link is reversed (field sign -1) and, for a μ-link with u_μ = 2, its base point moves to the
neighbouring block; the check uses the link-level map, so this shift is included. ∎ *Control A2n:* a reflection through a plane that is
not a block centre gives 490902 mismatches. The 324 link types fall into 8 orbits (sizes 64, 96, 32, 48, 48, 8, 24, 4; s7 A3).

### 22.2 Proposition CI-0: PROVEN-HERE, computer-assisted (not counted)
*Definitions.* For each of the 8 canonical types c, K̃(·, (0, c)) is the float column of the inverse of Õ_0 on the 12⁴-block torus, restricted
to the links whose midpoint is within ℓ^∞ distance 16.5 (= 3R + 3/2, R = 5) of the block-0 centre, and then made EXACTLY Stab(c)-invariant
by copying, on each Stab(c)-orbit, the value at the orbit's least index (with the field sign). Every other column is DEFINED from these
by the group and block translations. So K̃ is a fixed array of dyadic numbers, exactly covariant; its accuracy affects only the size of
E := Õ_0K̃ - 1, never the validity. Metric: midpoint ℓ¹ distance d_mid (group invariant; |d_mid - d_base| ≤ 1).
*Proof.* (1) *Covariance reduces row sums to 8 columns.* E and K̃ are covariant (HO + definition). For a column type j with h(j) = c (h in
the group), Σ_Z|X((Z, i), (0, j))| = Σ_Z|X((Z, π_h(i)), (0, c))|, since h maps the type-i links bijectively onto the type-π_h(i) links. So
the row sum of type i is Σ_jS_{c(j)}[π_{h_j}(i)], with S_c[i] the type-i mass of column c. The same holds with the weights e^{md_mid}.
(2) *Enclosure.* fl(Õ_0K̃) is computed by BLAS (81 block products and their sum, ≤ 81·324 terms per entry). Then |fl - Õ_fK̃| ≤ γ_n|Õ_f||K̃|
for any summation order of classical dgemm. Also |Õ_f - Õ_0| ≤ u|Õ_0| (correctly rounded conversion of the exact rationals), and the
identity entry adds u|·|. The type sums of |Õ_f||K̃| are computed exactly in structure: with a_ij := Σ_Y|A_f(Y)[i, j]| and v_j := the
type-j mass of |K̃|, and e^{md_mid} ≤ e^{mD_A}e^{md_mid(z′)} (D_A = 10, the coupling range in d_mid), the type sums are ≤ e^{mD_A}Σ_ja_ijv_j.
Every sum is rounded upward. (3) *Periodisation.* On a torus of T ≥ 3 blocks, Õ_T, K̃_T and E_T are the periodisations, Õ_TK̃_T = 1 + E_T,
and N_m(|X_T|) ≤ N_m(|X|), because the torus distance is ≤ the Z⁴ distance. (4) *Neumann.* N_m is submultiplicative (d_mid is a metric).
If e_m < 1, then Õ_T^{-1} = K̃_T(1 + E_T)^{-1} (a right inverse in finite dimension), N_m(|Õ_T^{-1}|) ≤ k_m/(1 - e_m), and
C_0 = Õ^{-1} - (1 - Π) = (K̃ - (1 - Π)) - K̃(1 + E)^{-1}E. (5) *Gap.* Õ^{-1} is symmetric, so the Schur test gives ||Õ^{-1}|| ≤ N_0(|Õ^{-1}|).
Compressions of Õ_0 have the same lower bound (Rayleigh). ∎
*The certified numbers (s7 B2, midpoint metric):*
| m | k_m (≥ N_m(|K̃|)) | k′_m (≥ N_m(|K̃ - (1 - Π)|)) | e_m (≥ N_m(|E|)) |
|---|---|---|---|
| 0 | 132.842054 | 132.842054 | 0.4381436 |
| 0.005 | 137.95304 | 137.95304 | 0.5056699 |
| 0.01 | 143.33145 | 143.33145 | 0.5843553 |
| 0.02 | 154.96851 | 154.96851 | 0.7835355 |
| 0.03 | 167.92862 | 167.92862 | 1.0567 (fails) |
- **N_0(|Õ_0^{-1}|) ≤ 236.434158, N_0(|C_0|) ≤ 𝔠_0^♮ = 236.434158, λ_min(Õ_0) ≥ 4.229507·10⁻³**, on every torus T ≥ 3 blocks (and compressions).
- The k′_m column equals k_m to the printed digits: the row maximum sits at a type whose (1 - Π) entries do not lower it.
- *Rate:* N_{0.02}^{mid}(|C_0|) ≤ 715.9 (C1 at the background, below). So |C_0(b, b′)| ≤ 730.4e^{-0.02d_base(b,b′)}.
- *Validation:*
  - B2x: 320 entries of E (the 20 largest and 20 random ones per column) were recomputed in exact rationals. Each lies within its rounding
    radius (worst ratio 2.2·10⁻³). This tests the BLAS assumption on samples.
  - B1: canonicalisation changes the float columns by ≤ 2.0·10⁻¹⁶.
  - B4: the float N_0 of the full 12-torus inverse is 132.94 ≤ 236.43, and the float λ_min = 0.039849 ≥ 4.23·10⁻³.
  - B5n: at R = 2 the residual column total is 6.74, against 0.242 at R = 5.
- *Tightness:* certified/float N_0 = 1.78. The certified gap is 9.4× below the measured one, because the Schur bound ||·|| ≤ N_0 is loose.

### 22.3 Proposition CI-bg: PROVEN-HERE (not counted)
**Statement as proven.** For every (U, V) ∈ 𝔑(α_*) (N5-sf0; real or complex) on a torus T ≥ T_0 (any N, κ_0 = 1):
**N_0(|C(U, V)|) ≤ 𝔠_∞^♯ := k′_0 + δ + k_0(e_0 + δk_0)/(1 - e_0 - δk_0) = 236.434602** (δ = γ_0/2 = 7.94·10⁻⁹). For real (U, V),
**λ_min(Õ(U, V)) ≥ (1 - e_0 - δk_0)/k_0 = 4.229499·10⁻³**. With weights, **N_{0.02}^{mid}(|C(U, V)|) ≤ 715.91**, and
N_{0.01}^{mid} ≤ 344.84, N_{0.005}^{mid} ≤ 279.07.
*Proof.*
(1) *The column gauge.* Fix a column block Y. Let □ ∋ Y and g := g_□, the real gauge of 𝔑(α_*) on Ω^+_□. Every entry that enters
column Y lies within coarse distance R + 5 = 10 ≤ R_* + 3 of Y. These are the entries Õ_U(b, z) with z in K̃'s support plus Õ's range,
together with their variables (2 more blocks). In this gauge every link and coarse link of that region is ≤ α_* (in log).
(2) *The deviation.* By N5-cov, Õ_U(·, z)R_z^{-1} = R^{-1}Õ(gU, gV)(·, z). By N5-an (entrywise), ||Õ(gU, gV)(b, z) - Õ_0(b, z)|| ≤ (2S_*/r_*)α_*.
This bound is the same for every Y; it is the GB-1 point. Row b has ≤ n_1 nonzero z, so sup_bΣ_zsup_Y|Δ^{(Y)}|(b, z) ≤ C_Δα_* ≤ γ_0/2 = δ.
The last inequality is N5-sf0's definition of α_* (C_Δα_* ≤ (γ_0/2 - 𝔇_0(m))e^{-mr_1}). The same holds for Π_U.
(3) *Neumann.* Put K̃_U(·, b′) := R^{-1}(K̃(·, b′) ⊗ 1)R_{b′}, column by column. Its block norms are those of K̃. Then E_U := Õ_UK̃_U - 1 has
N_0(|E_U|) ≤ e_0 + δk_0. Finish as in CI-0 (4), with K̃_U - (1 - Π_U) costing ≤ k′_0 + δ.
(4) *Gap and weights.* Real backgrounds: the Schur test. Weights: N_m(|Δ|) ≤ e^{m(r_1+1)}δ in d_mid. ∎
*κ-window (A4: q = N_0(|ΠQ^TQΠ|) = 161215/985608 = 0.16357, exact):* Õ(κ) = Õ(1) + (κ - 1)ΠQ^TQΠ. So CI-0 and CI-bg hold with
e_0 → e_0 + |κ - 1|qk_0. In particular **𝔠_∞ stays finite for |κ - 1| ≤ 2.6·10⁻²**. The C1 line prints the half-margin window 1.29·10⁻².
Scope: κ_0 near 1, not all of [κ_-, κ_+].

### 22.4 Corollary CI-BR1: PROVEN-HERE (substitution; not counted)
PROOF uses the level-0 𝔠_∞ only as an upper bound for N_0(|C|) at backgrounds of 𝔑(α_*). The uses checked are:
- BR1's proof (C_0 at (U^(0)(V), V) ∈ 𝔑(α_*), real; (v) complex);
- NAH1's ∂_VU = -CF_AB at (U(V), V) ∈ 𝔑(α_*) (BR1 (iii));
- CURV1 (l.6028);
- HG1 (iv) (the level-0 C).

So **𝔠_∞ := 𝔠_∞^♯ = 236.4346** is admissible there, at κ_0 = 1 (and in the κ-window), L = 3, d = 4, every N. The level-1 𝔠_∞^{(1)} is not covered.
*Consequences (s7 C3; N = 3, p_L = 11, K_FP = 514.5):*
| quantity | PROOF constants | with 𝔠_∞^♯ |
|---|---|---|
| 𝔠_∞ | 2.0·10³⁷ | **236.43** |
| C_bg = 1.011√N·max{1 + 48𝔠, 36p_L𝔠} | 1.39·10⁴⁰ | **1.640·10⁵** |
| ε_br: ε_*/(1 + 36p_L𝔠_∞) (PROOF ε_* = 1.7·10⁻²⁴/C_Δ) | ≈ 2·10⁻⁶⁴/C_Δ | 1.82·10⁻²⁹/C_Δ |
| ε_br: 1/(24𝔠_∞²C_♭) | 1.04·10⁻⁷⁶/C_♭ | **7.45·10⁻⁷/C_♭** |
| ε_br: r_♭/(24𝔠_∞), r_♭/144, 1/(1728𝔠_∞K_FP) | 2·10⁻³⁹r_♭, r_♭/144, 3·10⁻⁴¹ | 1.76·10⁻⁴r_♭, r_♭/144, 4.76·10⁻⁹ |
| **(TH-ch″) ε_1 at τ^A** | ≤ 5.95·10⁻⁷⁷/C_♭ | **≤ min{1.27·10⁻³⁹, 1.04·10⁻²⁹/C_Δ, 4.26·10⁻⁷/C_♭, 1.0·10⁻⁴r_♭, 2.7·10⁻⁹}** |
| (TH-ch″) ε_1 at τ^♯ ⇐ (GF-B^𝔥) | same | min{3.88·10⁻²³, 1.04·10⁻²⁹/C_Δ, …} |
- *Reading.* At τ^A the (TH-ch′) entry ε_bg^{(TH-bg)}/C_bg = 1.27·10⁻³⁹ binds, unless C_Δ ≳ 8·10⁹ or C_♭ ≳ 3·10³². That is 37 orders above
  session 6's 5.95·10⁻⁷⁷/C_♭.
- With PROOF's current ε_*, the C_Δ entry can bind. C_Δ = 2S_*n_1/r_* is unevaluated and ≥ 2n_1/r_* ≳ 10⁷ S_*.
- At τ^♯ the C_Δ entry (1.04·10⁻²⁹/C_Δ) binds for every C_Δ ≳ 3·10⁻⁷. So τ^♯ buys nothing for ε_1 until ε_* is sharpened (22.6).
- *C_♭:* not evaluated. Evaluating it needs explicit (r_♭, S_♭) for Lemma N5-an♭. Those in turn need explicit bounds on the holomorphic
  continuation of the soft term (NA-alg (a)'s fixed point X_0(M)) and of (h_Uh_U^T)^{-1}, (M_UP_ΛM_U^T)^{-1} on a polydisc. This is named
  **(C_♭-eval)** [OPEN, new name]. After this session C_♭ binds only if C_♭ ≳ 3·10³².

### 22.5 Lemma CHEB-f: PROVEN (citation) + PROVEN-HERE application (not counted)
**The bound.** Let G be self-adjoint with block range 1 and spectrum in [a, b], and let f be analytic in the open Bernstein ellipse E_ρ of
[a, b] with |f| ≤ M_ρ there. The Chebyshev truncation of degree D - 1 has sup error ≤ 2M_ρρ^{-(D-1)}/(ρ - 1) (Trefethen, ATAP Thm 8.2,
mapped to [a, b]), and it vanishes on block pairs at distance D. So ||f(G)(X, Y)|| ≤ 2M_ρρ^{-(D-1)}/(ρ - 1).
**The ellipse.** For f = x^{±1/2} the ellipse must avoid (-∞, 0], which means ρ < ρ_0 := σ + √(σ² - 1). On E_ρ, the nearest point to 0 is
the left vertex x_L = (a + b)/2 - (b - a)(ρ + ρ^{-1})/4. *Proof:* the distance² is quadratic in cos t with leading coefficient
((b - a)/2)² > 0 and vertex at s* ≤ -1, since (a + b)A/2 ≥ ((b - a)/2)². The farthest point is x_R. ∎
**Application (s7 C2).** Inputs: a = 4.229499·10⁻³ (CI-bg, real backgrounds), b = N_0(|Õ_0|) + δ = 25.47602, block range 1 (Setting N5-bg),
and base-point ℓ¹ distance ≤ 12D + 8 at block distance D. Take ρ = ρ_0^{1/2} and μ := ln ρ/24 = **5.369·10⁻⁴ per fine unit** (θ = ln ρ_0 =
0.02577 per block). Then **N_μ(|Õ^{1/2}|) ≤ 5.72·10¹⁶** and N_μ(|Õ^{-1/2}|) ≤ 2.01·10¹⁷, explicit, against N5-sf0's m_1 = 4.83·10⁻¹¹ with
N′ unevaluated.

### 22.6 Proposed re-evaluation of N5-sf0 (for PROOF's owner; s7 C4)
N5-sf0 uses γ_0 = 1.587·10⁻⁸ only as a lower bound for the compressions (Õ(1, 1))_Ω. CI-0 gives λ_min(Õ_0) ≥ 4.229507·10⁻³ on every
torus, and compressions inherit it. Rerun on PROOF's chain:
- the control with γ_0 reproduces m = 9.66·10⁻¹¹, R_* = 1.72·10¹², T_0 = 6.89·10¹² and ε_* = 1.745·10⁻²⁴/C_Δ;
- with the certified gap: **m = 2.57·10⁻⁵, R_* = 3.23·10⁶, T_0 = 1.29·10⁷, ε_* = 2.48·10⁻¹³/C_Δ** (×1.4·10¹¹).

The ε_br entry then becomes 2.6·10⁻¹⁸/C_Δ, and (TH-ch″)'s C_Δ entry becomes 1.5·10⁻¹⁸/C_Δ. This does not bind at τ^A unless C_Δ ≳ 10²¹;
at τ^♯ ⇐ (GF-B^𝔥) it binds unless C_Δ ≲ 4·10⁴. Status: a proposed substitution in a PROVEN theorem, to be made by PROOF's owner. SF
records it as PROVEN-HERE (substitution) and does not count it.

### 22.7 DX′-1 and the derived rows, re-evaluated (s7 C5, C6; arithmetic)
**DX′-1** (τ^A column, N_r = 1, C_Ω symbolic). The control reproduces 1.49·10⁻²³⁷.
| inputs | g_{DX′}²·C_Ω |
|---|---|
| (i) RW-ℓ²'s gap, m_1 | 7.3·10⁻¹⁸⁰ |
| (ii) ‖C‖ ≤ 1/λ_min (CI-bg) | **4.7·10⁻¹⁷³** |
| (iii) + CHEB-f's μ and its explicit N_μ(|Õ^{1/2}|) | **2.5·10⁻¹⁵²** (R_sh = 1.57·10⁵, m_sh = 1.2·10²⁰, |Ω_B| = 3.9·10²²) |

The gain is 28 orders, not REVIEW_SF_S6's estimated ≈ 70. a_sh ∝ 1/N_μ(|Õ^{1/2}|) enters squared, and the CHEB-f rate is ≈ 2√(a/b)/24 per
fine unit, so R_sh stays ≈ 10⁵. The binding coupling ceiling is now g_0 ≲ 1.6·10⁻⁷⁶/√C_Ω (from g_0² ≈ 2.5·10⁻¹⁵²). The hole ceiling,
FS-1 and the band window are τ_c-driven and unchanged.

**ε_1-driven rows** at the certified 𝔠_∞^♯ (C_♭ = C_Δ = 1, r_♭ = 1/220, the proposed ε_*; illustrative in the unevaluated constants):
- ε_1 = 1.27·10⁻³⁹;
- RLARGE n_* = 5.9·10⁷⁹ (SU(2)), against 2.7·10¹⁵⁴ after TH-2;
- ≈ 42 final levels (against 81);
- HW a_bad = 8.4·10⁻⁸⁵.

The TH-2 table of §19.4 is reproduced: 1.0417·10⁻⁷⁶, 5.9486·10⁻⁷⁷, 2.70·10¹⁵⁴/1.80·10¹⁵⁴, 3.5·10¹⁶³-2.8·10¹⁶⁷, a_bad 1.84·10⁻¹⁵⁹, 80.9 levels.
s7 printed "inf" for the RS row, a float overflow in a REPORT line; by hand it is 2.0·10³¹⁷-1.5·10³²¹.

### 22.8 STEP 3: (GF-B^𝔥) not attempted (time); it stays OPEN. After TH-2 and 22.4 it moves τ_c-driven rows only; at τ^♯ ε_1 needs ε_* sharpened first (22.6).

## 23. Session-7 outcome (written after §22)

### 23.1 Status changes
| item | status | note |
|---|---|---|
| [RSF6-fix] STEP 1 | applied (18 tags) | TH-2 ((TH-ch″)), FP-1, FP-2, GB-1, tally 53 + 1, non-binding notes |
| Lemma HO | PROVEN-HERE, computer-assisted (not counted) | exact; 8 orbits |
| **Proposition CI-0** | **PROVEN-HERE, computer-assisted (not counted)** | N_0(|C_0|) ≤ 236.43, λ_min(Õ_0) ≥ 4.23·10⁻³ (γ_0 = 1.59·10⁻⁸), rate 0.02 |
| **Proposition CI-bg** | **PROVEN-HERE (not counted)** | **𝔠_∞^♯ = 236.4346 on 𝔑(α_*)**, against 2.0·10³⁷; κ-window |κ - 1| ≤ 2.6·10⁻² |
| Corollary CI-BR1 | PROVEN-HERE (substitution; not counted) | C_bg 1.64·10⁵; ε_1 ≤ 1.27·10⁻³⁹ at τ^A modulo C_Δ, C_♭ |
| Lemma CHEB-f | PROVEN (citation) + PROVEN-HERE application | μ = 5.37·10⁻⁴, N_μ(|Õ^{1/2}|) ≤ 5.7·10¹⁶ |
| N5-sf0 re-evaluation | PROVEN-HERE as a substitution, proposed to PROOF | ε_* = 2.48·10⁻¹³/C_Δ, R_* = 3.2·10⁶ |
| DX′-1 ceiling | re-evaluated | g_0² ≲ 2.5·10⁻¹⁵²/C_Ω (was 7.3·10⁻¹⁸⁰ at τ^A) |
| (C_♭-eval) | OPEN, new name | explicit (r_♭, S_♭) of N5-an♭ |
| (GF-B^𝔥) | OPEN (not attempted) | |

**Tally (unreviewed; base = REVIEW_SF_S6's 53 + 1):** **PROVEN-HERE 58 + 1 standard** (counted 10; not counted 48 = 43 + HO, CI-0
(computer-assisted), CI-bg, CI-BR1, CHEB-f's application). CONDITIONAL 8, ARGUED 4, unchanged. OPEN names: §20.1's list, plus (C_♭-eval).
No RLARGE §4.2 row is discharged; no PROOF.md tally change is proposed. PROOF constant changes are proposed in SF_LOG.

### 23.2 Check s7
- Provenance:
  - criteria checks/s7_criteria.md born 08:12:41 UTC (md5 06238199…);
  - script checks/s7_sf.py born 08:16:53 UTC; desk fixes to 08:18:03 before any run (md5 05c1d69e…);
  - one run under the numeric lock, 08:18:31-08:24:29 UTC: load 2.77, free 46%, nice 10, BLAS threads 1, 358 s, exit 0, one rmdir;
  - output checks/s7_out.txt (md5 c97d39df…), record checks/s7_time.txt.
- **OVERALL PASS 17/17.** Rigorous: A1, A2, A3 (exact), B2, B3 (certified floats), C1-C6 (arithmetic). Validation: B2x (exact samples),
  B1, B4. Negative controls: A2n, B5n.
- Caveats:
  - Peak RSS was 867 MiB (909 MB) < 1 GB, but the peak memory footprint was 1.18 GB, over 1 GB on that measure.
  - The exploratory sf7/ex2 peaked at 1.36 GB RSS / 2.24 GB footprint (SF_LOG).
  - B2 assumes classical dgemm for the γ_n bound; the B2x samples support it.
  - Scope κ_0 = 1 (± window), L = 3, d = 4.
