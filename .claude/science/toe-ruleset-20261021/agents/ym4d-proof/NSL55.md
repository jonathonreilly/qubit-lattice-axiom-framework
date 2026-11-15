Reviewer model: claude-opus-5-5

# NSL55 — the nonlinear S_E slice-attainment lemma (NSL) at every depth, and BFT-0's identification clause at the trivial background

Worker file. Author: Opus 5.5 (claude-opus-5-5). Append-only. No git.
Started (UTC): 2026-10-29 01:21:07 (from `date -u` at session start).

## PRE-STATED (written before any derivation)

### Targets
- **T1 (statement).** State (NSL)_j precisely, for every depth 1 ≤ j ≤ k: the field space (depth-j composite fields
  x = (x_0, …, x_{j−1}) at the trivial background, data in 𝒞_glob), the gauge group acting (composite gauges, and which of
  them: trivial at the level-j roots, i.e. the group whose Lie algebra is Λ_* at depth j), the norm and ball radius, the
  conclusion (existence of g with Λ^{(j)}(x^g) = 0, uniqueness of such g in a small ball, analyticity of x ↦ g(x), and
  ‖x^g‖ ≤ C‖x‖), with every constant independent of k, T and j.
- **T2 (linear step).** Identify the derivative at (x, ξ) = (0, 0) of the slice map ξ ↦ Λ^{(j)}(x^{e^ξ}) and prove it is
  invertible on the right space with a bound uniform in k, T, j, from banked S_E results (EP-alg (e) Λ(Dμ) = −μ, EP-bd,
  EP-rec, Codex GSHARP item 1), then the derivative at general small x (Faddeev-Popov-type operator) by perturbation.
- **T3 (nonlinear step).** Control the nonlinear remainder of x ↦ x^{e^ξ} in the norms the consumer uses (𝔐^∇ and the
  σ-weighted 𝔐^{(σ)}: potentials θ_A = 1, coarse C^{1,α}, residual weight 2 + σ), and conclude (NSL)_j by the implicit
  function theorem (or a contraction), uniformly in k, T, j.
- **T4 (identification clause).** Use (NSL) to show that the composite critical point at depth k, restricted to depth j,
  is (gauge-equivalent to) the unique slice critical point at depth j, so that Z(V_k) is the per-level tower and
  E_k^br(V_k) = 𝔉_k(Z(V_k); V_k); decide whether E^cb = E^br is needed and, if so, whether it is available.
- **T5 (honest gap statement).** If any of T1-T4 fails, state exactly what is missing (a first-class result).

### What would count as a refutation
- **R1 (linear).** The linearised slice map is not invertible on the space carrying the depth-j gauge directions, or its
  inverse bound grows with k, T or j (e.g. a depth-dependent loss in the pinned-gauge norm ‖Ξξ‖_{𝔐^∇}).
- **R2 (norm class).** A gauge transformation ξ with ‖Ξξ‖ ≤ ε moves a point of the σ-ball out of the σ-weighted class
  (e.g. the residual weight 2 + σ is not preserved under x ↦ x^{e^ξ}, or the coarse Hölder term is not), so the IFT cannot
  be closed in the norm the consumer needs.
- **R3 (identification).** The depth-k critical point restricted to depth j is NOT a critical point of the depth-j
  functional F_j(·, U_j) (e.g. the composite functional does not split level by level at fixed U_j), or it is not in the
  depth-j small ball, or gauge-equivalence at depth j changes the level-j field U_j itself (so that "unique modulo depth-j
  gauges" does not identify the tower).
- **R4 (envelope / energy).** The identity E_k^br(V_k) = 𝔉_k(Z(V_k); V_k) needs more than gauge-invariant values (e.g.
  a derivative identity that holds only in the per-level slice), or needs E^cb = E^br and that identification is not
  available on 𝒞_glob.
- **R5 (premise).** GV55's rank argument for "BA-9 step (i) fails for S_E" is wrong (e.g. Λ^{(j)} is not the object the
  depth-j slice uses), in which case (NSL) is not needed at all.

### Method
Read (by string, bounded ranges): GV55 §3.3; BFT_A §3.8-§3.9 (BA-9, BA-10), §31 (Γ_E, Lemma GE, Proposition SM); BFT_B
§15-§16 (EP-alg, EP-opt, EP-rec, EP-bd); REVIEW_S22 Part 5 "Statement (BFT)"; PROOF.md "(FP♯')" and "[S26-BANKED]";
KFACTOR_OFF55 §3.4 "Scope", §6.3; CODEX_REVIEW_GSHARP item 1, CODEX_REVIEW_KOFF §4.3 and banked item 5; CODEX_REVIEW_GV if
it appears. Any numeric check gets `checks/ns55_*_criteria.md` with pre-registered PASS/FAIL before the script; exact
rational arithmetic in plain python only.

---

## §0. Read record, provenance, symbols pinned (appended 2026-10-29 ≈01:56Z)

**Read (bounded ranges, located by string):** REVIEW_BRIEF_55 (scratchpad); **GV55.md in full** (568 lines); REVIEW_S22
"Statement (BFT)" (l.387-440) and fix S22-6 (l.312-330, l.483); BFT_A §1 (l.18-47), lemma heads BA-1…BA-12 (l.49-97), §3.8
"BA-9" and §3.9 "Theorem BA" (l.187-231), §28.9 "Lemma FG", §31.0-§31.3 (l.2752-2842); BFT_B §15.0-§15.1 (l.2016-2087), §16
preamble and §16.1-§16.6 (l.2126-2260); KFACTOR_OFF55 §1.1-§1.4, §3.4 incl. "Scope", §4.1-§4.6, §6; CODEX_REVIEW_KOFF §4.3,
§5.3 and "Exactly what may be banked"; CODEX_REVIEW_GSHARP §1, §2.5, §5, §7-§8 and banked list; CODEX_REVIEW_HIGHER l.1-140
and banked list; PROOF.md header (l.1-45), "Lemma TOWER-VAR", "Proposition COMP" + "[R22-fix S22-6", "Lemma BR1", "Lemma
NA-alg", "Decision 4: the RG kernel"; REVIEW_BFT_A_S1 l.22-32, Part 7 (l.302-335), F8 and tally (l.404-416); REVIEW_S13_S14
l.174 ("Lemma NA-alg … CONFIRMED-WITH-FIX"); GSHARP55 §5.5.
**CODEX_REVIEW_GV.md** did not exist at 01:21Z; it appeared with mtime 01:36Z and I read it in full (429 lines, complete:
ends with "Exactly what may be banked", items 1-6) at ≈01:48Z — **after** my §1 witness, its sign proof and the rank
finding had been derived and checked (ns55_1 criteria written 01:47:19Z, run 01:47:43Z). Its §5 reaches the same two
conclusions by a different witness; see §1.4.
**Drift:** none of consequence. GV55 cites REVIEW_S22 "l.385-435" for BFT-0; the statement is at l.387-408.

**Symbols pinned (systemic defect 1).**
- **j** = depth (1 ≤ j ≤ k); i, l = levels. **n_j := L^j** (fine steps per depth-j coarse unit); **h_i := L^{i−j}** (own step of
  level i in depth-j coarse units; h_i ≤ 1/L for i < j).
- **Λ^{(j)}** = the depth-j slice functional: BFT_B §15.0's Λ = Σ_Xχ^5_Xλ^E_X with n replaced by n_j (boxes Ñ_X of depth-j coarse
  half-width 2 about the level-j roots). Λ^{(k)} = Γ_E = GV55's "Λ"; at depth k with T ∈ {3, 4}, Λ^{(T)} := Γ^{(T)} of
  Proposition SM. **Not** BFT_A §13.11's "Lemma Λ" (root-to-root holonomy) and not the spaces Λ_0, Λ_*.
- **Λ_*^{(j)}** := su(N)-valued level-0 functions vanishing at every level-j root (KFACTOR_OFF55's Λ_* is j = k).
- **𝒢^{(j)}** := depth-j composite gauges trivial at level j: g on level-0 sites, g = 1 at level-j roots, acting on level
  i < j through g_i := ev^{(i)}g (BFT_A §1.1: g_i(c_X) = g_{i+1}(X)). 𝒢^{(j)} ⊂ 𝒢^{(j+1)} (level-(j+1) roots are level-j roots).
- **Gauge action** (BFT_A §31.0 convention, K_0 = −Ξ): (x^g)_i(b) := log(g_i(b^−)e^{x_i(b)}g_i(b^+)^{−1}); left action,
  (x^g)^{g′} = x^{g′g}. **Ξμ** := (dμ, d ev^{(1)}μ, …); Π_E x = x + ΞΛ(x).
- **I_j u** := Σ_Xχ^{5,(j)}_X u(c^{(j)}_X), the level-j quintic-tent interpolation of root values; p(t) := 10t³ − 15t⁴ + 6t⁵,
  σ_5 = 1 − p.
- **‖·‖_{(σ),j}** = KFACTOR_OFF55 §1.2's 𝔐^{(σ)} at depth j, top residual r_{j−1} = Qx_{j−1} − x_j with the datum x_j
  (differences in the homogeneous-data norm, Codex KOFF §5.3). Level-i part: ‖x^c_i‖_{1,α;i} + L^{(1+σ)(j−1−i)}‖r^c_i‖_∞ with
  ‖f‖_{1,α;i} := ‖f‖_∞ + max_ν‖∇_νf‖_∞ + max_ν[∇_νf]_α (∇_ν = difference quotient at step h_i, coarse units).
- **‖ξ‖_♮** := ‖ξ‖_∞ + ‖∇^cξ‖_∞ + ‖∇^c∇^cξ‖_∞ + [∇^c∇^cξ]^∞_α (level 0, depth-j coarse units) = EP-bd's ‖·‖_{C^{2,α}} plus the
  sup term. On Λ_*^{(j)} it is equivalent to GV55's ‖Ξξ‖_{𝔐} (Lemma A (d)).
- **n_0(v)** := ‖v^c_0‖_∞ + ‖∇^cv^c_0‖_∞ + [∇^cv^c_0]_α (level-0 part of 𝔐, no residual). **η(x)** := max_{i<j}(‖x^c_i‖_∞ +
  ‖∇^cx^c_i‖_∞) + ‖x_j‖_D (sup/gradient size incl. the datum; no Hölder, no residual).
- **ρ_l** := log(V^{−1}W_0) (NA-alg (b); V = U_{l+1}(c), W_0 the SU(N) maximiser for M̄_c(U_l)); **r_l** := Q_lx_l − x_{l+1};
  **Δ_l := ρ_l − r_l**.
- **C_0, ε_0** = Theorem K^{(σ)} / BFT-E's (KFACTOR_OFF55 §4.5; Codex KOFF §5.3). New local names introduced here and used
  nowhere else in the lane: **C_Λ, C_alg, K_G, C_Δ, η_1, ρ_N, a_N, r_N, C_N, r_u, ε_u, ε_ID**.
- **E^cb_j(W)** := 𝔉_j(Z_j(W); W) (BA-9's composite branch value); **E^br_j** = PROOF's per-level branch value (TOWER-VAR (a);
  BR1 at level 1).

---

## §1. The premise (R5): GV55's rank proof is wrong, its conclusion is right

### 1.1 The rank inequality is reversed — REFUTED
GV55 §3.3 (locating "Proof (rank count)"): "If Ker Λ^{(k)} ⊂ Ker Λ^{(j)} then rank Λ^{(j)} ≤ rank Λ^{(k)} = N_0 − N_k <
N_0 − N_j for j < k — impossible." The task brief repeats it ("rank Λ^{(j)} = N_0 − N_j > N_0 − N_k for j < k").
With N_i = (TL^{k−i})^4 (BFT_A §1.1: level-i side TL^{k−i}), N_j > N_k for j < k, so **N_0 − N_j < N_0 − N_k**. The ranks per
Lie-algebra component are indeed N_0 − N_j and N_0 − N_k (image in Λ_*^{(i)}, onto by Λ^{(i)}Ξ = −1 there), but kernel
inclusion would imply rank Λ^{(j)} ≤ rank Λ^{(k)}, which is **true**: no contradiction, so the rank count proves nothing.
(ns55_1 C6 prints the exact counts, e.g. (L, j, k, T) = (3, 1, 2, 3): 524880 < 531360.)

### 1.2 Proposition W (constant-data witness) — PROVEN-HERE (exact; ns55_1)
Fix τ ∈ su(N), |τ| = 1, h ∈ ℝ, and the constant real datum **B_k := hτe_1** (in 𝒞_glob(|h|)). Put c := L^{−k}hτ.
- (a) The constant chain x̄_i := L^{i−k}hτe_1 (i < k) is a global minimiser of 𝔉_k∘exp(·; B_k), value 0.
- (b) Its S_E^{(k)} representative is x̂ := x̄^{e^{ζτ}}, ζ := L^{−k}h(z_1 − I_k[z_1]) ∈ Λ_*^{(k)} (scalar), with
  x̂_0 = c·e_1 − d(ζτ) and Λ^{(k)}(x̂_0) = 0; ‖x̂‖_{(σ),k} ≤ C|h|.
- (c) For every 1 ≤ j < k: **Λ^{(j)}(x̂_0) = −c·(1 − I_j)(I_k[z_1])**, and at the fine site c_X + e_1 next to any level-k root
  its value is **−c·n_k[p(1/n_k) − p(n_j/n_k)p(1/n_j)] ≠ 0**.
- (d) For |h| small, x̂ is the depth-k slice critical point x* of Theorem BFT-E (Corollary K-U, §4.1). So **the actual slice
  critical point for constant data does not restrict into S_E^{(j)}**, at every depth j < k, for arbitrarily small data.

*Proof.* (a) 𝔉_k ≥ 0: Wilson terms are ≥ 0 and φ = N^{−1}[Re tr(W_0^{−1}M) − Re tr(V^{−1}M)] ≥ 0 because W_0 maximises
Re tr(W^{−1}M) (NA-alg (a)). At x̄ every plaquette holonomy is 1 (e^{aτ}·1·e^{−aτ}·1 for (1,ν)-plaquettes, 1 otherwise). Every
S4′ contour of a coarse link c runs from root c_X to root c_Y (PROOF "Decision 4": M̄_c → g(c_X)M̄_cg(c_Y)^{−1}); its transporter
is a product of commuting factors e^{±aτ} (direction-1 links) and 1's, equal to e^{(net 1-displacement)aτ}: e^{Laτ} for c in
direction 1, 1 otherwise. So M̄_c = W_0 = V and ρ = φ = 0 everywhere; 𝔉_k(x̄) = 0.
(b) In the single direction τ everything commutes, so the gauge action is exactly linear: log(e^{ζ(b^−)τ}e^{aτ}e^{−ζ(b^+)τ}) =
(a − dζ(b))τ, i.e. x̄^{e^{ζτ}} = x̄ − Ξ(ζτ). On a box Ñ_X (no wrap, T_k ≥ 5) the field c e_1 is exact, so the pinned box
minimiser is λ^E_X(c e_1) = −c(z_1 − c_{X,1}) with minimum 0; Σ_Xχ_X = 1 gives **Λ^{(k)}(c e_1) = −c(z_1 − I_k z_1)** (torus
displacements; the function z_1 − I_kz_1 = Σ_Xχ_X(z)(z_1 − c_{X,1}) is periodic and vanishes at level-k roots). EP-alg (e)
(Λ(dμ) = −μ on Λ_*): Λ^{(k)}(x̂_0) = −c(z_1 − I_kz_1) + ζτ = 0. Norm: x̂^c_i = hτe_1 − (Ξζτ)^c_i, ζ is h times a fixed C^{2,1}
function of the coarse coordinate (t − p(t) on each cell), residuals vanish; so ‖x̂‖_{(σ),k} ≤ C|h|. (For T ∈ {3, 4} the same
after periodic lifting, Proposition SM.)
(c) EP-alg (a) at depth j: Λ^{(j)}(v + dν) = Λ^{(j)}(v) − ν + I_jν. With v = c e_1, ν = −ζτ = −c(z_1 − I_kz_1):
Λ^{(j)}(x̂_0) = −c(z_1 − I_jz_1) + c(z_1 − I_kz_1) − cI_j(z_1 − I_kz_1) = −c(I_kz_1 − I_jI_kz_1). Tensor tents reduce I_k, I_j on
functions of z_1 to 1D quintic interpolation (Σ_{X_ν}σ_5 = 1 in each other coordinate). On a level-k cell, I_kz_1 = c_{X,1} +
n_kp((z_1 − c_{X,1})/n_k); level-k roots are level-j roots; so at z_1 = c_{X,1} + 1 the defect is
ψ(1) := n_kp(1/n_k) − n_kp(n_j/n_k)p(1/n_j). Writing p(t) = t³q(t), q(t) = 10 − 15t + 6t²: ψ(1) = n_k^{−2}[q(1/n_k) −
q(n_j/n_k)q(1/n_j)]. x ↦ q(1/x) is increasing on x ≥ 1 (derivative 15/x² − 12/x³ > 0), n_j ≥ 3 and n_k/n_j ≥ 3, so
q(n_j/n_k)q(1/n_j) ≥ q(1/3)² = 289/9 > 10 > q(1/n_k): **ψ(1) < 0**. Exact values (ns55_1 C3): (L, j, k) = (3,1,2): −640/2187;
(3,1,3) and (3,2,3): −9280/177147; (5,1,2): −5376/78125; (7,1,2): −129600/5764801; (3,1,4): −95680/14348907.
(d) ‖x̂‖_{(σ),k} ≤ C|h| ≤ r_u and x̂ is a full critical point in S_E^{(k)}, so Corollary K-U applies. ∎

### 1.3 Reading
The obstruction is that quintic tents neither reproduce linear functions (I_kz_1 ≠ z_1) nor commute with subdivision. ns55_1
C5 (designed control): with hat tents p_lin(t) = t the same code gives ψ ≡ 0 (hat tents are not C^{2,1} and are not an
admissible replacement in EP-bd; this only shows the check discriminates). A restriction-compatible depth-j condition does
exist — Γ′_j := (1 − I_j)∘Λ^{(k)} has Γ′_jΞ = −1 on Λ_*^{(j)} (I_jμ = 0 there) and Γ′_j(x*_0) = 0 for every depth-k slice point —
but its boxes have depth-j coarse size 4L^{k−j}, no depth-uniform (GV) is available for it, and it is not used below.

### 1.4 Comparison with CODEX_REVIEW_GV §5 (read after 1.1-1.2 were derived)
Codex GV §5.1 REFUTES the same inequality (its exact example (L, k, j, T) = (3, 2, 1, 5): ranks 4050000 < 4100000) — **agree**.
Codex GV §5.2 gives an independent witness x_0 = dμ, μ = I_2u (one-coordinate root data), with Λ^{(1)}(dμ)(1) = −640/19683 —
**agree**; it is the same function up to normalisation: on the cell μ = 1 − g/n_k with g(m) = n_kp(m/n_k), so
(1 − I_1)μ = −ψ/n_k and −640/19683 = (1/9)·(−640/2187) = ψ(1)/n_k at (3, 1, 2). Two derivations from different starting
fields (an exact gradient there; a flat field with holonomy here, which is moreover the true nonlinear slice critical point)
give the same exact number. Codex GV §5.3 ("The witness is not a counterexample to identification modulo gauges … NSL is one
sufficient route") — **agree**; (NSL) below is a sufficient repair, not shown to be necessary.

---

## §2. (NSL) stated (target T1)

**Setting N (depth j).** d = 4, N ≥ 2, L ≥ 3 odd, 0 < α < σ ≤ 1, 1 ≤ j ≤ k, T ≥ 3, trivial background, m = 0. Depth-j
configurations x = (x_0, …, x_{j−1}) with a real top datum x_j = B (level-j su(N) 1-form); coarse torus side T_j := TL^{k−j}
(≥ 9 for j < k). Slice S_E^{(j)} := Ker Λ^{(j)} (T_j ≥ 5), or S_E^{(T)} := Ker Λ^{(T)} when j = k and T ∈ {3, 4}. Gauge group
𝒢^{(j)} (§0). Hölder seminorms are pointwise ([·]^∞_α over pairs at coarse ℓ^∞-distance ≤ 1); the Campanato version of 𝔐 is
equivalent (Osc_2(H; B) ≤ ρ^α[H]^∞_α and [H]^∞_α ≤ C_T([H]_α + sup|H|), BFT_B §16 preamble), so every statement below holds
for either after multiplying constants by (1 + C_T).

> **Theorem NSL (nonlinear S_E slice attainment at every depth). PROVEN-HERE (§3), given the banked inputs listed in §3.0.**
> There are r_N > 0, ρ_N > 0 and C_N < ∞ depending only on (N, L, α) — **not on k, T or j** — such that for every real
> depth-j configuration x with ‖x‖_{(σ),j} ≤ r_N:
> - **(a) existence and uniqueness.** There is exactly one ξ = ξ(x) ∈ Λ_*^{(j)} with ‖ξ‖_♮ ≤ ρ_N and Λ^{(j)}((x^{e^ξ})_0) = 0
>   (i.e. x^{e^ξ} ∈ S_E^{(j)}); e^{ξ} ∈ 𝒢^{(j)}.
> - **(b) size.** ‖ξ(x)‖_♮ ≤ 2C_Λ·n_0(x) ≤ 2C_Λ‖x‖_{(σ),j}.
> - **(c) the slice representative.** (x^{e^ξ})_j = x_j (datum unchanged) and ‖x^{e^ξ}‖_{(σ),j} ≤ C_N‖x‖_{(σ),j}.
> - **(d) analyticity.** x ↦ ξ(x) is real-analytic and extends holomorphically (complexified real coordinates) to a polydisc of
>   fixed radius, with (a)-(b) there up to a factor 2.
> - **(e) consistency.** ξ(x) = 0 iff x ∈ S_E^{(j)}.
> - **(f) Faddeev-Popov operator.** M_FP(x) := Λ^{(j)}∘K_x restricted to Λ_*^{(j)} (K_x the infinitesimal composite gauge
>   action at x, BFT_A §31.0; level-0 component) satisfies M_FP(0) = 1 and ‖M_FP(x)^{−1}‖_{♮→♮} ≤ 2.
> (a), (b), (d)-(f) need only n_0(x) ≤ a_N (no residual control); the residual weight enters only (c).

Remarks. (1) The constants do not depend on σ either: σ ≤ 1 is used only through L^{(σ−1)q} ≤ 1 (Lemma D). (2) (f) is Lemma CD
(ii)'s nonlinear Faddeev-Popov hypothesis ("Γ_EK_x is a bijection") on Λ_*; since K_x(constant c) = [c, x] ≠ 0 for nonabelian
x ≠ 0, the pinned space Λ_* (not "Λ_0/const") is its correct domain at x ≠ 0. K^{(σ)} does not use Lemma CD (ii) (CCP (d)
replaced it), so (f) is a by-product. (3) GV55's sketch used ‖ξ‖_♮ := ‖Ξξ‖_{𝔐^∇}; by Lemma A (d) the two norms are equivalent
on Λ_*^{(j)} (‖Ξξ‖ ≤ ‖ξ‖_♮ ≤ 3‖Ξξ‖).

---

## §3. Proof of Theorem NSL (targets T2, T3)

### 3.0 Inputs and their status
- EP-alg (a), (c), (e) and EP-bd's C^{2,α} bound of Λ (BFT_B §16.1, §16.4): **Codex GSHARP banked item 1 and §1, §2.5**
  ("Caccioppoli and LES-div thus control λ in C^{2,α} on the tent support by the local C^{1,α} norm of x_0"), lane CONFIRMED
  (REVIEW_BFT_B_S5); descended slices: Proposition SM, Codex GSHARP §2.5, Codex GV item 3. Named package input inherited:
  LES-div (LINEAR_PACKAGE Lemma 3.2″), as for EP-bd.
- NA-alg (a)-(b) (PROOF; REVIEW_S13_S14 "CONFIRMED-WITH-FIX (domain of (b))"); BA-4, BA-5 (REVIEW_BFT_A_S1: CONFIRMED);
  local analytic constants, â₂ = avg B₂, S4′ centering, β(X, w) vanishing on both axes, |ρ − r| ≤ Cε_l³η² on the 𝔐-ball:
  **Codex HIGHER banked item 1** (and Codex KOFF §4.3 (1)).
- S4′ contours with common root endpoints, M̄_c → g(c_X)M̄_cg(c_Y)^{−1} (PROOF "Decision 4: the RG kernel").
- The BCH series (absolute convergence in any Banach algebra for small arguments). No other input.

### 3.1 Lemma A (the slice functional at depth j) — banked, restated
For 1 ≤ j ≤ k (T_j ≥ 5; or Λ^{(T)} at j = k, T ∈ {3, 4}):
- (a) Λ^{(j)} is real-linear, reads x_0 only, and takes values in Λ_*^{(j)} (EP-alg (c): Λ(c_Y) = λ^E_Y(c_Y) = 0).
- (b) Λ^{(j)}(v + dμ) = Λ^{(j)}(v) − μ + I_jμ for every level-0 μ; in particular **Λ^{(j)}(dμ) = −μ for μ ∈ Λ_*^{(j)}**
  (EP-alg (a), (e): λ^E_X(x + dμ) = λ^E_X(x) − μ + μ(c_X), Σχ = 1).
- (c) **‖Λ^{(j)}(v)‖_♮ ≤ C_Λ n_0(v)**, C_Λ = C_Λ(α, d, L). (EP-bd's proof: ‖Λ‖_{C^{2,α}} ≤ 16·4C_χ·6C_E·sup_X n_{Ñ_X}(v), and
  n_{Ñ_X}(v) ≤ n_0(v): **only the level-0 C^{1,α} norm of v enters**; plus ‖Λ‖_∞ ≤ 2‖∇^cΛ‖_∞, since Λ vanishes at the level-j
  roots and every fine site is joined to one by ≤ 2(n_j − 1) fine steps. C_E covers the finitely many depths with n_j < 64,
  BFT_B §16.2 "Small k".)
- (d) For μ ∈ Λ_*^{(j)} and every level i < j: **‖(Ξμ)^c_i‖_{1,α;i} ≤ ‖μ‖_♮ and r_i(Ξμ) = 0** (i ≤ j − 1). [(Ξμ)^c_i at a
  level-i link is the average of the fine ∇^cμ along its L^i fine steps; its level-i difference quotients are averages of fine
  second difference quotients; Hölder seminorms of averages of translates are bounded by those of the averaged function
  (BFT_B §16.3-16.4). Residuals: Q_i∘d∘ev^{(i)} = d∘ev^{(i+1)} (root covariance), and r_{j−1}(Ξμ) = d ev^{(j)}μ = 0.] Hence
  ‖Ξμ‖_{(σ),j} ≤ ‖μ‖_♮ ≤ 3‖Ξμ‖_{(σ),j}.

### 3.2 Lemma B (the nonlinear gauge action in coarse units) — PROVEN-HERE
Let **F(u, a, β) := log(e^u e^a e^{−u−β}) − a + β**. For ξ ∈ Λ_*^{(j)}, a level i < j and a level-i link b put
u_i(b) := ξ(b_i^−) (ξ at the base root), β_i := (Ξξ)^c_i. Since ξ_i(b^+) = ξ_i(b^−) + (dξ_i)(b), x_i = h_ix^c_i and
dξ_i = h_iβ_i:
  **(B0) (x^{e^ξ})^c_i = x^c_i − β_i + G_{h_i}(u_i, x^c_i, β_i),  G_h(u, a, β) := h^{−1}F(u, ha, hβ).**
*Structure of F.* F vanishes whenever two of its arguments vanish: F(u, 0, 0) = log 1 = 0, F(0, a, 0) = 0, F(0, 0, β) =
log e^{−β} + β = 0. Hence in its (absolutely convergent) noncommutative power series every word with nonzero coefficient has
degree ≥ 2, contains at least two distinct letters, and contains u or β; every word without u contains both a and β; the
degree-2 part is [u, a] − ½[u, β] − ½[a, β]. (ns55_2 verifies all five statements exactly in the free algebra to degree 4,
with a designed-FAIL control.) Consequently the coefficients of G_h are c_wh^{n_a(w)+n_β(w)−1} with n_a + n_β ≥ 1 (pure-u
words have zero coefficient), so **|coefficient| ≤ |c_w| for every 0 < h ≤ 1: G_h is controlled uniformly in h**.
*Norm.* ‖·‖_{1,α;i} on level-i link functions (M_N(ℂ)-valued, Hilbert-Schmidt) is a Banach algebra up to C_alg ≤ 8: with
A, A′, A″ the three parts for f and B, B′, B″ for g, ∇(fg) = (∇f)·g(·+h e_ν) + f·∇g and [g]^∞_α ≤ 4‖∇g‖_∞ at scales ≤ 1
(lattice path of ≤ 4|b − b′|_∞/h steps) give ‖fg‖ ≤ AB + A′B + AB′ + A″B + 8A′B′ + AB″ ≤ 8‖f‖‖g‖.
*Majorant.* With ‖·‖′ := C_alg‖·‖ (submultiplicative) and ‖u‖′, ‖a‖′, ‖β‖′ ≤ R: Σ_w|c_w|R^{|w|} ≤ m(R) := −log(2 − e^{4R}) + 2R
(majorant of log(1 + Y), Y = e^ue^ae^{−u−β} − 1, ‖Y‖′ ≤ e^{4R} − 1 < 1). For a word with letters s ∈ {u, β} and t ≠ s,
‖w(X)‖′ ≤ ‖X_s‖′‖X_t‖′R^{|w|−2}; telescoping w(X) − w(X′) puts the difference in one slot and, in an a-slot, keeps a u- or
β-letter elsewhere. Hence, for **max(‖u‖, ‖a‖, ‖β‖) ≤ R_0 := 1/(20C_alg)** and 0 < h ≤ 1:
  **(B1) ‖G_h(u, a, β)‖ ≤ K_G(‖u‖ + ‖β‖)(‖u‖ + ‖a‖ + ‖β‖),**
  **(B2) ‖G_h(u,a,β) − G_h(u′,a′,β′)‖ ≤ K_G[(‖u‖+‖β‖+‖u′‖+‖β′‖)‖a − a′‖ + (‖u‖+‖a‖+‖β‖+‖u′‖+‖a′‖+‖β′‖)(‖u−u′‖+‖β−β′‖)],**
with **K_G an absolute constant** (crudely K_G ≤ 2C_alg·max(m(1/20)·20², 2m(1/10)·10²) ≤ 1.5·10³, using
|w|(1/20)^{|w|−2} ≤ 2(1/10)^{|w|−2}; no value of K_G is load-bearing).
*Inputs to (B1)-(B2).* ‖u_i‖_{1,α;i} ≤ ‖ξ‖_∞ + ‖∇^cξ‖_∞ + 4‖∇^c∇^cξ‖_∞ ≤ 4‖ξ‖_♮ (level-i difference quotients of ξ are averages of
fine ones; Lipschitz ⇒ Hölder at scales ≤ 1); ‖β_i‖_{1,α;i} ≤ ‖ξ‖_♮ (Lemma A (d)); ‖x^c_i‖_{1,α;i} ≤ ‖x‖_{(σ),j}. Hence, if
4‖ξ‖_♮, ‖x^c_i‖_{1,α;i} ≤ R_0:
  **(B1′) ‖(x^{e^ξ})^c_i − x^c_i + (Ξξ)^c_i‖_{1,α;i} ≤ 5K_G‖ξ‖_♮(5‖ξ‖_♮ + ‖x^c_i‖_{1,α;i}),**
  **(B2′) ‖[(x^{e^ξ})^c_i + (Ξξ)^c_i] − [(x^{e^{ξ′}})^c_i + (Ξξ′)^c_i]‖_{1,α;i} ≤ 5K_G(10ρ + 2‖x^c_i‖_{1,α;i})‖ξ − ξ′‖_♮**
  (‖ξ‖_♮, ‖ξ′‖_♮ ≤ ρ ≤ R_0/4).
**Uniformity:** nothing here depends on h_i ∈ (0, 1/L], on the level i, on the depth j, on k or on T. ∎

### 3.3 Lemma E (slice attainment = a contraction at level 0) — PROVEN-HERE
Let a := n_0(x). By (B0) at i = 0 and Lemma A (b), for ξ ∈ Λ_*^{(j)}:
  Λ^{(j)}((x^{e^ξ})_0) = Λ^{(j)}(x_0) + ξ + Λ^{(j)}(R_0(x, ξ)),  R_0(x, ξ) := (x^{e^ξ})_0 − x_0 + dξ  (R^c_0 = G_{h_0}(u_0, x^c_0, β_0)).
So **x^{e^ξ} ∈ S_E^{(j)} ⟺ ξ = Ψ_x(ξ) := −Λ^{(j)}(x_0) − Λ^{(j)}(R_0(x, ξ))**, and Ψ_x maps into Λ_*^{(j)} (Lemma A (a)). Only
level-0 quantities enter. Lemma A (c) with (B1′), (B2′) at i = 0 gives, for ‖ξ‖_♮, ‖ξ′‖_♮ ≤ ρ ≤ R_0/4 and a ≤ R_0:
  ‖Ψ_x(ξ)‖_♮ ≤ C_Λ[a + 5K_G‖ξ‖_♮(5‖ξ‖_♮ + a)],   ‖Ψ_x(ξ) − Ψ_x(ξ′)‖_♮ ≤ 5C_ΛK_G(10ρ + 2a)‖ξ − ξ′‖_♮.
Put **ρ_N := min(R_0/4, 1/(200C_ΛK_G))** and **a_N := min(R_0, ρ_N/(2C_Λ), 1/(40C_ΛK_G), 1/(10C_ΛK_G(10C_Λ + 1)))**. For
a ≤ a_N:
- on {‖ξ‖_♮ ≤ ρ_N}, Lip(Ψ_x) ≤ 50C_ΛK_Gρ_N + 10C_ΛK_Ga ≤ ¼ + ¼ = ½, so **Ψ_x has at most one fixed point there** (no self-map
  needed);
- on {‖ξ‖_♮ ≤ ρ_a}, ρ_a := 2C_Λa ≤ ρ_N: ‖Ψ_x(ξ)‖_♮ ≤ C_Λa + 5C_ΛK_Gρ_a(5ρ_a + a) ≤ 2C_Λa (the last condition in a_N), so Ψ_x
  maps this ball into itself with Lip ≤ ½ and **has a fixed point ξ(x) with ‖ξ(x)‖_♮ ≤ 2C_Λa**.
This is (a)-(b). (e): Ψ_x(0) = −Λ^{(j)}(x_0) since R_0(x, 0) = 0; so 0 is the fixed point iff Λ^{(j)}(x_0) = 0. (d): Ψ_x(ξ) is
given by a convergent series in (x_0, ξ); all bounds hold for complexified arguments with R_0 halved; the iterates Ψ_x^n(0)
are holomorphic in x and converge uniformly (as in BA-10), so ξ(x) is holomorphic, real on real x. (f): K_xμ =
d/dt|_{t=0}x^{e^{tμ}}, so by (B0) Λ^{(j)}(K_xμ) = μ + Λ^{(j)}(∂_ξR_0(x, 0)μ), and (B2′) with ξ′ = 0, ξ = tμ, t → 0 gives
‖Λ^{(j)}(∂_ξR_0(x, 0)μ)‖_♮ ≤ 10C_ΛK_Ga‖μ‖_♮ ≤ ¼‖μ‖_♮; so M_FP(x) = 1 + (operator of norm ≤ ¼). ∎
**The linearisation** (task step 2) is thus the identity at the trivial background (Λ^{(j)}K_0 = −Λ^{(j)}Ξ = 1 on Λ_*^{(j)}, Lemma
A (b)), and the Faddeev-Popov operator at small x is a ¼-perturbation of it in ‖·‖_♮; **no Schauder estimate beyond EP-bd is
needed, because Λ^{(j)} gains the derivative that the remainder costs** (C^{1,α} → C^{2,α}).

### 3.4 Lemma C (soft fluctuation versus linear residual, residual kept explicit) — PROVEN-HERE from Codex HIGHER item 1
There are η_1 > 0 and C_Δ < ∞, depending only on (N, L), such that for every depth-j configuration y with η(y) ≤ η_1, every
0 ≤ l < j and every level-(l+1) link c (own units, h_l = L^{l−j}):
  **|Δ_l(y)(c)| = |ρ_l(y)(c) − r_l(y)(c)| ≤ C_Δ[h_l³η(y)² + h_lη(y)|r_l(y)(c)|].**
*Proof.* (Codex HIGHER §2's derivation, with the residual term not replaced by its 𝔐-ball value.) W_0 = e^{X_0}, X_0 = Q_ly_l + â,
where â is the averaged second-order BCH part plus the analytic tail: â₂ = avg B₂ (Codex HIGHER §2), |avg B₂| ≤ ½p_L(p_L −
1)δ(2|ȳ| + δ) (BA-4) with δ ≤ 5Lh_l²η(y) (gradient part of η) and |ȳ| ≤ h_lη(y) (sup part); the tail is O(h_l³η(y)³) (≤ p_L =
5L − 4 letters per contour, each O(h_lη(y)); uniform local analytic constants, Codex HIGHER item 1). So |â| ≤ C_ah_l³η(y)².
Let ŵ := X_0 − y_{l+1}(c) = r_l(y) + â. Then ρ = log(e^{−y_{l+1}}e^{X_0}) = log(e^{−X_0+ŵ}e^{X_0}) = ŵ + β(X_0, ŵ),
β(X, w) := log(e^{−X+w}e^X) − w, which vanishes on {X = 0} and on {w = 0}, hence |β(X, w)| ≤ C_β|X||w| on a fixed polydisc.
With |X_0| ≤ 2p_Lh_lη(y) and |ŵ| ≤ |r_l(y)| + |â| (both small: |r_l(y)| ≤ (p_L + L)h_lη(y) a priori):
|ρ − r| ≤ |â| + C_β|X_0|(|r| + |â|) ≤ C_Δ[h_l³η² + h_lη|r|]. Only the sup and gradient parts of y were used. ∎
On the 𝔐-ball (|r_l| ≤ h_l²η) this returns Codex KOFF (1) / Codex HIGHER's |ρ − r| ≤ Ch_l³η²; for a gauge transform x^g the
residual is the unknown, which is why it is kept explicit.

### 3.5 Lemma D (residuals of a gauge transform) — PROVEN-HERE
Let x be a real depth-j configuration and g = e^ξ ∈ 𝒢^{(j)} with η(x), η(x^g) ≤ η_2 := min(η_1, 1/(2C_Δ)). Then for every
l < j:
  **L^{(1+σ)(j−1−l)}‖r^c_l(x^g)‖_∞ ≤ 3L^{(1+σ)(j−1−l)}‖r^c_l(x)‖_∞ + 2C_ΔL^{−3}(η(x)² + η(x^g)²).**
*Proof.* **Exact covariance.** For a coarse link c = (X, Y) at level l + 1 all S4′ contours run c_X → c_Y, so M̄_c(U^g) =
g(c_X)M̄_c(U)g(c_Y)^{−1} (PROOF "Decision 4"); Re tr(W^{−1}g(c_X)Mg(c_Y)^{−1}) = Re tr((g(c_X)^{−1}Wg(c_Y))^{−1}M) and the
maximiser is unique (NA-alg (a)), so W_0 ↦ g(c_X)W_0g(c_Y)^{−1}; composite compatibility gives V = U_{l+1}(c) ↦
g(c_X)Vg(c_Y)^{−1}. Hence V^{−1}W_0 ↦ g(c_Y)(V^{−1}W_0)g(c_Y)^{−1} and **ρ_l(U^g)(c) = Ad(g(c_Y))ρ_l(U)(c)** (principal log;
for l = j − 1, g(c_Y) = 1). Therefore
  r_l(x^g) = ρ_l(x^g) − Δ_l(x^g) = Ad(g(c_Y))[r_l(x) + Δ_l(x)] − Δ_l(x^g),
and Ad(g(c_Y)) is an isometry. Lemma C for x and for x^g, then absorption (C_Δh_lη(x^g) ≤ ½):
|r_l(x^g)| ≤ 3|r_l(x)| + 2C_Δh_l³(η(x)² + η(x^g)²). Multiply by L^{(2+σ)(j−1−l)} (the own-unit form of the weight):
L^{(2+σ)(j−1−l)}h_l³ = L^{(σ−1)(j−1−l)−3} ≤ L^{−3} because σ ≤ 1. ∎
This is the step GV55's sketch stated as "the nonlinear soft fluctuation is exactly gauge-covariant … so ‖r(x^g)‖ stays
σ-weighted (L^{(2+σ)q}h³ ≤ L^{−3})" — **CONFIRMED**, with Lemma C supplying the bound Codex KOFF (1) only states on the σ-ball.

### 3.6 Conclusion of the proof
Let ‖x‖ := ‖x‖_{(σ),j} ≤ r_N and ξ := ξ(x) (Lemma E; n_0(x) ≤ ‖x‖ ≤ a_N). (b): ‖ξ‖_♮ ≤ 2C_Λ‖x‖. Datum: ev^{(j)}ξ = 0.
Non-residual part, every level i < j, by (B0), Lemma A (d) and (B1′):
  ‖(x^{e^ξ})^c_i‖_{1,α;i} ≤ ‖x^c_i‖_{1,α;i} + 2C_Λ‖x‖ + 10C_ΛK_G‖x‖(10C_Λ + 1)‖x‖ ≤ ‖x^c_i‖_{1,α;i} + 3C_Λ‖x‖,
for ‖x‖ ≤ 1/(10K_G(10C_Λ + 1)). Hence η(x^{e^ξ}) ≤ η(x) + 3C_Λ‖x‖, and η(x) ≤ 7‖x‖ (the datum: |x_j| ≤ |Q_{j−1}x_{j−1}| +
|r_{j−1}| ≤ (p_L/L + 1)‖x‖ ≤ 6‖x‖), so both are ≤ η_2 when ‖x‖ ≤ η_2/(7 + 3C_Λ). Residual part: Lemma D. Adding, at each level
  ‖(x^{e^ξ})^c_i‖_{1,α;i} + L^{(1+σ)(j−1−i)}‖r^c_i(x^{e^ξ})‖_∞ ≤ 3[‖x^c_i‖_{1,α;i} + L^{(1+σ)(j−1−i)}‖r^c_i(x)‖_∞] + 3C_Λ‖x‖
    + 2C_ΔL^{−3}(49 + (7 + 3C_Λ)²)‖x‖² ≤ (4 + 3C_Λ)‖x‖,
once also ‖x‖ ≤ L³/(2C_Δ(49 + (7 + 3C_Λ)²)). So **(c) holds with C_N := 4 + 3C_Λ** and
**r_N := min(a_N, η_2/(7 + 3C_Λ), 1/(10K_G(10C_Λ + 1)), L³/(2C_Δ(49 + (7 + 3C_Λ)²)))**. Every constant is a function of
(N, L, α) through C_Λ (EP-bd), K_G (absolute), C_Δ, η_1 (NA-alg/HIGHER local constants): **uniform in k, T, j (and σ)**. ∎

---

## RESUMED 2026-10-29 02:58:01 UTC

Resumed run, same model (**claude-opus-5-5**, verbatim from my system prompt; it matches the first line, so no extra model line
is added). The draft above (§0-§3.6, ending at the `---` after §3.6) was written by the stopped run and is UNREVIEWED. Nothing
above this heading is edited; corrections go to the errata section below.

### Resume pre-statement (written before any new derivation; statements only)
- **Still to do.** (R-a) Re-verify every step of §1-§3 that the rest builds on (Lemma A, Lemma B, Lemma E, Lemma C, Lemma D,
  §3.6, Proposition W). (R-b) Supply the fixed-radius uniqueness statement that §1.2 (d) cites as "Corollary K-U, §4.1" — **no
  §4.1 exists in the draft; the citation was a forward reference** — or record (d) as unsupported. (R-c) Target T4: the
  identification clause. (R-d) Decide whether E^cb = E^br is needed, and for whom. (R-e) Summary table, counts, Codex verdicts.
- **What would refute the T4 conclusion I expect** (restriction ≅ depth-j slice point modulo 𝒢^{(j)}; per-level criticality and
  value recursion for E^cb; uniqueness modulo level-j gauges trivial at level-(j+1) roots in an explicit level-j ball):
  (i) the restricted, gauge-fixed point lies outside every region where depth-j critical-point uniqueness is available
  (Codex GV §5.3's warning: the depth-j datum may be much smaller than L^{−(k−j)}s, so the C_0·s_j ball is the wrong region);
  (ii) the envelope identity needs per-level slice preservation (not only gauge-invariant values); (iii) the uniqueness region
  for the per-level statement is not a ball in the level-j variable alone; (iv) E^cb_j is not gauge-invariant under the group
  the uniqueness is taken modulo.
- **Inputs I will not build on:** anything Codex GV REFUTES (GV55's rank inequality / rank proof; the "≤ 16 cells" small-torus
  citation extension). The PROOF header's paraphrase "(NSL) is genuinely needed" is the lead's; Codex GV §5.3 says only that the
  direct restriction argument fails and NSL is one sufficient route — I use Codex's wording.

## §R. Re-verification of the draft's §1-§3 (resumed run, ≈03:05-03:40Z)

Same model family as the draft's author, so this is a re-derivation, **not** an independent cross-family check. Every item
below I re-derived from the cited source text (located by string, read this session: BFT_B "Setting EΠ (elliptic slice)",
"16.1 Lemma EP-alg", "16.2 Lemma EP-int", "16.4 Theorem EP-bd"; BFT_A "1.1 The composite problem" … "1.4 The pair",
"3.1 BA-1", "3.4 BA-4", "3.5 BA-5", "3.8 BA-9", "3.9 Theorem BA"; KFACTOR_OFF55 "1.1"-"1.3", "3.4 Proposition CCP",
"4.5 Theorem K"; CODEX_REVIEW_KOFF §1, §4.3, §5.3 and banked list; CODEX_REVIEW_GSHARP l.225 and banked item 1;
CODEX_REVIEW_HIGHER banked item 1; PROOF "Lemma U0", "Lemma BR1", "Lemma TOWER-VAR", "Proposition COMP", "(BG-unif), precise
statement"; REVIEW_S22 "Statement (BFT)").
I also re-ran both existing checks unchanged (`python3 -I checks/ns55_1_witness.py`, `python3 -I checks/ns55_2_bch.py`): both
print `OVERALL: PASS` with the recorded values. (ns55_1 prints floats only as labels; every verdict there is a Fraction test.)

| Draft item | What I re-derived | Verdict |
|---|---|---|
| §1.1 rank inequality reversed | N_i = (TL^{k−i})^4 ⇒ N_0 − N_j < N_0 − N_k for j < k; kernel inclusion implies the TRUE inequality | **CONFIRMED** (agrees with Codex GV §5.1) |
| §1.2 (a) x̄ is a global minimiser | S_W ≥ 0 with every plaquette = 1 at x̄; every S4′ transporter is e^{(net 1-displacement)aτ} (commuting factors), so M̄_c = V(c) ∈ SU(N); Re tr(W^{−1}V) ≤ N with equality iff W = V, so W_0 = V, ρ = φ = 0 | **CONFIRMED** |
| §1.2 (b) S_E^{(k)} representative | abelian direction ⇒ x̄^{e^{ζτ}} = x̄ − Ξ(ζτ) exactly (F ≡ 0 on commuting arguments); λ^E_X(ce_1) = −c(z_1 − c_{X,1}) (exact on the box, BFT_B Setting EΠ); EP-alg (e); ζ = h(t − p(t)) per cell is C^{2,1}-periodic (φ := t − p(t): φ(0) = φ(1) = 0, φ′(0) = φ′(1) = 1, φ″(0) = φ″(1) = 0), residuals r_i(x̂) = 0 (Q(ae_1) = Lae_1, root covariance) | **CONFIRMED** |
| §1.2 (c) the defect formula and sign | EP-alg (a) at depth j; 1D reduction (other coordinates sit on root coordinates, tents give δ's); ψ(1) = n_k^{−2}[q(1/n_k) − q(n_j/n_k)q(1/n_j)], q decreasing on [0, 1/3], q(1/3) = 17/3, so the bracket ≤ 10 − 289/9 < 0 | **CONFIRMED** |
| §1.2 (d) "x̂ is the slice critical point" | needs a uniqueness statement in a ball **not** of radius C_0s (‖x̂‖ ≤ C_W|h| with an explicit C_W not compared to C_0). The draft cites "Corollary K-U, §4.1", which **does not exist in the draft** | **NOT-VERIFIED as drafted** (dangling forward reference, Erratum E1); **CONFIRMED** once §4.1 below (Corollary K-U) is supplied |
| §1.4 comparison with Codex GV §5 | −640/19683 = ψ(1)/n_k at (3,1,2) | **CONFIRMED** |
| §3.1 Lemma A (a)-(d) | (a) χ_X(c_Y) = δ_{XY}, pin; (b) EP-alg (a) + Σχ = 1; (c) EP-int (a)/EP-bd give the C^{2,α} bound from the **local level-0** C^{1,α} norm only (also Codex GSHARP l.225), sup by ≤ 2(n_j − 1) fine steps to a root; (d) (Ξμ)^c_i = average of ∇^cμ over n_i fine steps, its difference quotient an average of ∇^c∇^cμ, Hölder of averages of translates, Q∘d = d∘ev | **CONFIRMED** |
| §3.2 Lemma B | (B0) (x^g)_i = a − β′ + F(u, a, β′), β′ = h_iβ_i; F vanishes when two arguments vanish ⇒ the five word properties (also ns55_2); pure-u words vanish ⇒ G_h's coefficients carry h^{n_a+n_β−1}, n_a + n_β ≥ 1; C_alg ≤ 8 (product rule + [g]^∞_α ≤ 4‖∇g‖_∞ by lattice paths); majorant −log(2 − e^{4R}) + 2R; telescoping keeps a u/β letter when the difference sits in an a-slot; e^{0.4} < 2 | **CONFIRMED** (K_G ≤ 1.5·10³ re-checked: 8·400·m(1/20) ≈ 1.1·10³, 8·200·m(1/10) ≈ 1.4·10³; not load-bearing) |
| §3.3 Lemma E (a)-(f) | slice equation ⟺ ξ = Ψ_x(ξ); Lip ≤ ¼ + ¼ on the ρ_N-ball; self-map of the 2C_Λa-ball under the a_N conditions; M_FP = 1 + E, ‖E‖ ≤ 10C_ΛK_Ga ≤ ¼ | **CONFIRMED** |
| §3.4 Lemma C | X_0 = Q_ly_l + â, |â| ≤ C_ah_l³η² (BA-4 with δ ≤ 5Lh_l²η, |x̄| ≤ h_lη; BA-5; analytic tail; Codex HIGHER item 1's uniform local constants); ρ = ŵ + β(X_0, ŵ), β vanishing on both axes; only sup and gradient of y enter | **CONFIRMED** |
| §3.5 Lemma D | M̄_c(U^g) = g(c_X)M̄_cg(c_Y)^{−1} (all S4′ contours run c_X → c_Y, PROOF "Decision 4"/Lemma U0's proof), unique maximiser ⇒ W_0 covariant; composite compatibility for V; ρ_l(U^g) = Ad(g(c_Y))ρ_l(U); absorption; L^{(2+σ)(j−1−l)}h_l³ = L^{(σ−1)(j−1−l)−3} ≤ L^{−3} | **CONFIRMED** |
| §3.6 conclusion, Theorem NSL (a)-(f) | the bookkeeping of (c) (datum: |x_j| ≤ (p_L/L + 1)‖x‖ ≤ 6‖x‖; C_N = 4 + 3C_Λ; r_N's four conditions) | **CONFIRMED** (as an implication of EP-int/EP-bd [Codex GSHARP item 1] and the uniform local analytic constants [Codex HIGHER item 1]) |

**Two precisions (not errors).** (i) GV55 §3.3 says the restricted Campanato term scales "by ≤ L^{−(2−α)(k−j)}". Depth-j
distances are L^{k−j} times depth-k ones, so the factor is in fact ≤ L^{−(2+α)(k−j)}; GV55's bound is weaker and still true. Only
the potential term's L^{−(k−j)} matters below. (ii) Going **up** one depth (used in §4.3 (I3)), the depth-(j+1) Hölder seminorm
also sees pairs at depth-j distance in (1, L], which the depth-j seminorm does not; they are bounded by 2·sup. Hence the up-going
factor is ≤ 3L³, not L^{2+σ} (Lemma SC (b) below).

---

## §4. T4 — BFT-0's identification clause from (NSL) (written ≈03:40-04:30Z)

### 4.0 Symbols, objects, inputs
**Symbols pinned for §4-§5 (systemic defect 1; see Erratum E2 — several names the draft called "new" are not).**
C_Λ := the draft's Lemma A (c) constant (**not** Lemma Λ's C_Λ = 10, BFT_A "13.11 Lemma Λ"). C_Δ, η_1, η_2 := the draft's
Lemma C/D constants (**not** the analyticity constant C_Δ of PROOF "Lemma BR1", written **C_Δ^{BR1}** below, and not PROOF's three
η_1's). R_B := 1/(20C_alg), the draft's Lemma B radius (the draft writes it R_0, which it also uses for the level-0 remainder
R_0(x, ξ) of Lemma E). r_N, C_N, ρ_N := Theorem NSL's (the same objects GV55 §3.3 calls (NSL)_j's r_N, C_N). **r_u, ε_u, ε_ID**
:= the constants defined in 4.1 and 4.3 below (**not** BA-9's / Theorem BA's r_u in BFT_A §2-§3.9 and BFT_B l.1083, and not the
lane's ε_u of TUNIF/NORMS). G, K, η_*, C_0, ε_0, r_ℂ, C_cc := 2d(59/100)L^{d−1} := Codex KOFF §5.3's bookkeeping constants of
the corrected Theorem K^{(σ)}, with G discharged by Proposition GV-E (Codex GV item 2).

**Norms.** ‖·‖_{(σ),j} := the draft's depth-j norm (pointwise Hölder); ‖·‖^{C}_{(σ),j} := the same with RTARGET §33's Campanato
seminorm (the norm of KFACTOR_OFF55 §1.2, Codex KOFF and BFT-E). ‖·‖^C ≤ ‖·‖ ≤ (1 + C_T)‖·‖^C (BFT_B §16 preamble), and
**C_0′ := (1 + C_T)C_0**. For a level-j 1-form w and a level-(j+1) datum v, the **top norm at depth j + 1**
‖w‖_{T;v} := ‖w^c‖_∞ + ‖∇^cw^c‖_∞ + [∇^cw^c]^∞_α + ‖Qw − v‖_∞ (depth-(j+1) coarse units, w^c = Lw) is the level-j part of
‖·‖_{(σ),j+1} (weight L^{(1+σ)·0} = 1 on the top residual).

**Objects (Balaban's convention, BA-9).** For j ≥ 1 and a real level-j 1-form w (global gauge) with ‖w‖_D ≤ ε_u:
- **Z_j(w)** := the depth-j point of Theorem BFT-E with datum w, on the same fine torus (level-j coarse side T_j := TL^{k−j};
  slice Λ^{(j)} if T_j ≥ 5, the descended Γ^{(T)} if T_j ∈ {3, 4}, which happens only at j = k);
- **E^cb_j(w)** := 𝔉_j(exp Z_j(w); e^w); **E^cb_0** := S_W;
- **F^cb_j(w, v)** := E^cb_j(w) + κ_jΣ_cφ̂_c(M̄^{(j)}_c(e^w); e^v) (j ≥ 0; F^cb_0(·, v) = 𝔉_1(·; v));
- **U^cb_j(v)** := (Z_{j+1}(v))_j, the level-j component of the depth-(j+1) point (j ≥ 0);
- **𝒢^{rt}_j** := {ev^{(j)}g : g ∈ 𝒢^{(j+1)}} = the level-j gauges equal to 1 at the level-(j+1) roots (every such h extends to a
  level-0 g with g = 1 at the level-(j+1) roots). These are exactly the gauges under which w ↦ F_j(w, v) is invariant at fixed v.

**Inputs and status.**
- (In-1) **Theorem BFT-E at every depth** (GV55 §3.1; **Codex GV item 4: CONFIRMED** as an implication, holomorphy of the point
  and of its composite critical value included), in the bookkeeping of **Codex KOFF §5.3** (C_0 = max(2, 4G); ε_0 below
  η_*/(C_0 + 1), C_0/[4GK(C_0 + 1)²], 1/[2GK(2C_0 + 1)], 1/[2C_ccC_0]) and its source estimate
  N^{(σ)}(S̃(x) − S̃(x′)) ≤ K(η + η′ + s)‖x − x′‖^C_{(σ)} on ‖x‖^C, ‖x′‖^C ≤ η ≤ η_* (Codex KOFF banked items 3, 5).
  Constants independent of k and T; **the same constants at every depth j** because BFT-E holds for every k ≥ 1 and every
  T ≥ 3 and the depth-j problem is the depth-"k := j" problem on a torus of side T_j ≥ 3.
- (In-2) **CCP (d)** (Codex KOFF item 2: CONFIRMED): a full critical point x̄ ∈ Ker Γ with max_i‖x̄^c_i‖_∞ < 1/C_cc is a fixed point
  of Φ̃_Γ (the converse direction needs no analytic radius).
- (In-3) **Theorem NSL** (§2-§3; re-verified in §R; **no Codex check yet**).
- (In-4) **BA-1** and **composite gauge invariance of 𝔉_j** (both re-derived here). S_W is gauge invariant. For compatible
  (g_i, g_{i+1}) (g_i(c_X) = g_{i+1}(X)): M̄_c(U_i^{g_i}) = g_i(c_X)M̄_c(U_i)g_i(c_Y)^{−1} (all S4′ contours run c_X → c_Y; PROOF
  "Decision 4", Lemma U0's proof), U_{i+1}^{g_{i+1}}(c) = g_i(c_X)U_{i+1}(c)g_i(c_Y)^{−1}, and φ̂(gMg′^{−1}; gVg′^{−1}) = φ̂(M; V)
  (W_0(gMg′^{−1}) = gW_0(M)g′^{−1} by uniqueness of the maximiser; both traces are invariant). Hence 𝔉_j(U^g; W^{g_j}) = 𝔉_j(U; W)
  for every composite gauge, and **for g ∈ 𝒢^{(j)} (g_j = 1): 𝔉_j(U^g; W) = 𝔉_j(U; W) for every datum W** (the top soft term sees
  g_{j−1} only at level-j roots, where g = 1). The gauge action is a local real-analytic diffeomorphism of the log chart, so it
  maps full critical points to full critical points.

### 4.1 Corollary K-U (slice uniqueness in a ball of fixed radius, at every depth) — PROVEN-HERE (from In-1, In-2)
Put **r_u := min(η_*, 1/(8GK), 1/(2C_cc))** and **ε_u := min(ε_0, 1/(4GK), r_u/C_0, r_ℂε_0/2)**. For every depth k ≥ 1, every
T ≥ 3 and every real B with s := ‖B‖_D ≤ ε_u, **x*(B) is the only full critical point of F := 𝔉_k∘exp(·; B) in
{x ∈ Ker Γ : ‖x‖^C_{(σ)} ≤ r_u}**, whatever the size of s inside (0, ε_u].
*Proof.* x* lies there: ‖x*‖^C ≤ C_0s ≤ r_u. A full critical point x̄ ∈ Ker Γ with ‖x̄‖^C ≤ r_u has max_i‖x̄^c_i‖_∞ ≤ r_u ≤
1/(2C_cc) < 1/C_cc, so it is a fixed point of Φ̃_Γ (In-2). For x, x′ in the r_u-ball of Ker Γ, S̃(x) − S̃(x′) is cc (CCP (a))
with zero datum, so ‖Φ̃_Γ(x) − Φ̃_Γ(x′)‖^C ≤ G·K(2r_u + s)‖x − x′‖^C ≤ (¼ + ¼)‖x − x′‖^C. Two fixed points in the ball coincide. ∎
*Reading.* This is the statement Codex GV §5.3 asks for ("uniqueness of any two fixed points in a sufficiently small
fixed-radius slice neighborhood, independently of the datum's exact size"). It also **supplies the "Corollary K-U, §4.1" that
the draft's §1.2 (d) cites**: ‖x̂‖^C_{(σ),k} ≤ C_W|h| with C_W explicit (ζ = h(t − p(t)) per cell), so for |h| ≤ min(ε_u, r_u/C_W)
the constant-data witness x̂ is x*(hτe_1), and Proposition W (d) holds.

### 4.2 Lemma SC (changing depth) — PROVEN-HERE (elementary)
(a) **Down.** For 1 ≤ j < k and a depth-k configuration x (datum B_k), the depth-j configuration x_{<j} := (x_0, …, x_{j−1}) with
datum x_j obeys ‖x_{<j}‖_{(σ),j} ≤ L^{−(k−j)}‖x‖_{(σ),k} (also for ‖·‖^C), and ‖x_j‖_D ≤ L^{−(k−j)}‖x‖_{(σ),k}.
(b) **Up.** For a depth-j configuration y with datum w and a level-(j+1) datum v: ‖(y, w)‖_{(σ),j+1} ≤ max(3L³‖y‖_{(σ),j}, ‖w‖_{T;v}).
(c) **Sup comparison.** L‖w‖_D ≤ ‖w‖_{T;v} ≤ 20L³‖w‖_D + ‖v‖_D.
*Proof.* (a) x^{c,j}_i = L^{−(k−j)}x^{c,k}_i; the own step L^{i−j} of level i in depth-j units equals L^{k−j}·L^{i−k}, so
∇^{c,j} = L^{−(k−j)}∇^{c,k} and the gradient term scales by L^{−2(k−j)}; depth-j distances are L^{k−j} times depth-k ones and
depth-j pairs at distance ≤ 1 are depth-k pairs at distance ≤ L^{−(k−j)}, so the Hölder term scales by ≤ L^{−(2+α)(k−j)}
(Campanato: boxes of depth-j radius ρ are boxes of depth-k radius L^{−(k−j)}ρ inside the depth-k range); weighted residuals:
L^{(2+σ)(j−1−i)}·own|r_i| = L^{−(2+σ)(k−j)}·L^{(2+σ)(k−1−i)}·own|r_i|, and the depth-j top residual Qx_{j−1} − x_j **is** the depth-k
residual r_{j−1}. Datum: own|x_j| = L^{−(k−j)}|x^{c,k}_j|. (b) The inverse factors with k − j = 1 (L, L², L^{2+α}, L^{2+σ}), plus the
depth-(j+1) Hölder pairs at depth-j distance in (1, L], bounded by 2·sup·L^α; per level ≤ L + L² + L^{2+α}·3 ≤ 3L³ times the depth-j
part; the depth-j top residual Qy_{j−1} − w becomes the level-(j−1) residual at depth j + 1 (weight L^{2+σ} ≤ L³); level j is
‖w‖_{T;v} by definition. (c) w^c = Lw; ∇^cw^c = L²·(difference) ≤ 2L²‖w‖_D; [∇^cw^c]^∞_α ≤ 4‖∇^c∇^cw^c‖_∞ ≤ 16L³‖w‖_D (lattice
paths, as in Lemma B); ‖Qw − v‖_∞ ≤ p_L‖w‖_D + ‖v‖_D; L + 2L² + 16L³ + p_L ≤ 20L³ for L ≥ 3. ∎

### 4.3 Theorem ID — PROVEN-HERE as an implication of In-1 … In-4
**Constants** (all independent of k, T and j):
- **ε_ID** := min(ε_u, Lr_N/C_0′, Lr_u/(C_NC_0′), Lε_u/C_0);
- **r_B** := min(Lε_u/6, r_N/(3L²C_0′), r_u/(3L²C_NC_0′), 1/(30K_G), η_2/9, L³/(324C_Δ)), and **ρ_h := r_B**;
- **ε_lev** := min(ε_ID, r_B/C_0′, r_B/2); **ρ_lev** := r_B/(40L³); **ε_tow** := ε_lev/C_0.
Write **𝔹_j(v)** := {w real level-j 1-form : ‖w‖_{T;v} ≤ r_B}. By Lemma SC (c), **𝔹_j(v) ⊇ {w : ‖w‖_D ≤ ρ_lev}** whenever
‖v‖_D ≤ r_B/2: a sup ball of fixed radius about the trivial field, in the global gauge.

> **Theorem ID (BFT-0's identification clause at the trivial background, Balaban's convention).** Setting of Theorem BFT-E
> (d = 4, N ≥ 2, odd L ≥ 3, κ_l ∈ [κ_−, κ_+], 0 < α < σ ≤ 1, θ₀ ∈ (α, σ], θ₀ < 1, 𝒞_glob, trivial centring, m = 0, coarse torus side
> T ≥ 3, every k ≥ 1). With the constants above:
> - **(I1) restriction.** For k ≥ 2, real B_k with s := ‖B_k‖_D ≤ ε_ID, x* := Z_k(B_k), and 1 ≤ j < k: there is ξ_j ∈ Λ_*^{(j)},
>   ‖ξ_j‖_♮ ≤ 2C_ΛC_0′L^{−(k−j)}s, unique in {‖ξ‖_♮ ≤ ρ_N}, with **(x*_{<j})^{e^{ξ_j}} = Z_j(x*_j)**: the composite point, cut at
>   depth j, is the depth-j composite point of its own level-j component, modulo one small gauge trivial at the level-j roots.
> - **(I2) per-level criticality and value.** For j ≥ 0 and real v (level j + 1) with ‖v‖_D ≤ ε_lev: **U^cb_j(v) is a critical
>   point of w ↦ F^cb_j(w, v)**, and **E^cb_{j+1}(v) = F^cb_j(U^cb_j(v), v)**.
> - **(I3) per-level uniqueness, modulo the level's gauge group.** For the same (j, v): U^cb_j(v) ∈ 𝔹_j(v); **every real critical
>   point w of F^cb_j(·, v) in 𝔹_j(v) is w = (U^cb_j(v))^h with h ∈ 𝒢^{rt}_j**; conversely, for ξ ∈ Λ_*^{(j+1)} with ‖ξ‖_♮ ≤ ρ_h,
>   (U^cb_j(v))^{ev^{(j)}e^ξ} is again a critical point of F^cb_j(·, v), with the same value F^cb_j = E^cb_{j+1}(v).
> - **(I4) the tower.** For real B_k with s ≤ ε_tow, U_j := e^{x*_j} (U_k := V_k = e^{B_k}) and every 0 ≤ j < k: U_j is a critical
>   point of F^cb_j(·, U_{j+1}) lying in 𝔹_j(x*_{j+1}), where every critical point is gauge-equivalent to it under 𝒢^{rt}_j; and
>   **E^cb_{j+1}(x*_{j+1}) = F^cb_j(U_j, U_{j+1})**, so that, telescoped, **E^cb_k(B_k) = 𝔉_k(exp x*; V_k) = S_W(U_0) +
>   Σ_{j<k}κ_jΣ_cφ̂_c(M̄^{(j)}_c(U_j); U_{j+1})**.
>
> With E^br := E^cb (Balaban's convention, BA-9) this is REVIEW_S22's BFT-0 second bullet ("each U_j is the unique critical
> point of F_j(·, U_{j+1}) in its level-j ball … and E_k^br(V_k) = 𝔉_k(Z(V_k); V_k)"), with "unique" read modulo 𝒢^{rt}_j — the
> invariance group of F_j(·, U_{j+1}) — and "its level-j ball" = 𝔹_j(x*_{j+1}) ⊇ the own-units sup ball of radius ρ_lev,
> uniformly in k, T and j, for tori (T ≥ 3), real data in 𝒞_glob(ε_tow). Together with BFT-E's holomorphy of the composite
> value, **BFT-2's literal branch-action clause also holds in this convention** (E_k^br := E^cb_k = 𝔉_k(x*(B_k); B_k)).

*Proof.* **(I1).** By BA-1, x*_{<j} (datum x*_j) is a full critical point of 𝔉_j∘exp(·; x*_j). By Lemma SC (a),
‖x*_{<j}‖_{(σ),j} ≤ L^{−(k−j)}(1 + C_T)‖x*‖^C_{(σ),k} ≤ L^{−(k−j)}C_0′s ≤ C_0′s/L ≤ r_N. Theorem NSL (a)-(c) gives ξ_j (unique in the
ρ_N-ball; size by NSL (b)) with z := (x*_{<j})^{e^{ξ_j}} ∈ S_E^{(j)} and ‖z‖^C_{(σ),j} ≤ ‖z‖_{(σ),j} ≤ C_NC_0′s/L ≤ r_u; z is a full
critical point of 𝔉_j∘exp(·; x*_j) (In-4: e^{ξ_j} ∈ 𝒢^{(j)} fixes the datum and is a symmetry); the datum has
‖x*_j‖_D ≤ C_0s/L ≤ ε_u (Lemma SC (a), Campanato version). Corollary K-U at depth j: z = Z_j(x*_j).
**(I2).** j = 0: F^cb_0(·, v) = 𝔉_1(·; v), U^cb_0(v) = Z_1(v), a full critical point, and E^cb_1(v) = 𝔉_1(Z_1(v); v) by
definition. j ≥ 1: apply (I1) to the depth-(j+1) problem with datum v ("k := j + 1"; ‖v‖_D ≤ ε_ID): with y := Z_{j+1}(v) and
w_0 := y_j = U^cb_j(v), there is ξ ∈ Λ_*^{(j)} with (y_{<j})^{e^ξ} = Z_j(w_0); ‖w_0‖_D ≤ C_0‖v‖_D/L ≤ ε_u, so E^cb_j is
real-analytic near w_0 (BFT-2 at depth j; ε_u ≤ r_ℂε_0/2). *Envelope:* Z_j(w) is a full critical point of 𝔉_j(·; w) and Z_j is
C¹, so dE^cb_j(w) = ∂_w𝔉_j(Y; w)|_{Y = Z_j(w)}. At w = w_0, Y = (y_{<j})^{e^ξ} and by In-4 𝔉_j((y_{<j})^{e^ξ}; w) = 𝔉_j(y_{<j}; w)
**for every w**, so ∂_w agrees: dE^cb_j(w_0) = ∂_w𝔉_j(y_{<j}; w)|_{w_0}. Hence d_wF^cb_j(w_0, v) = ∂_{x_j}𝔉_{j+1}(y; v) = 0 (BA-1: the
x_j-derivative of 𝔉_{j+1} is that of 𝔉_j(·; x_j) + κ_jΣφ̂(x_j; v); y is a full critical point). *Value:* E^cb_{j+1}(v) =
𝔉_{j+1}(y; v) = 𝔉_j(y_{<j}; w_0) + κ_jΣφ̂(w_0; v) = 𝔉_j(Z_j(w_0); w_0) + κ_jΣφ̂(w_0; v) = F^cb_j(w_0, v) (BA-1, In-4).
**(I3).** *Membership:* ‖U^cb_j(v)‖_{T;v} ≤ ‖Z_{j+1}(v)‖_{(σ),j+1} ≤ C_0′‖v‖_D ≤ r_B. *Uniqueness:* let w ∈ 𝔹_j(v) be critical for
F^cb_j(·, v). For j ≥ 1: ‖w‖_D ≤ r_B/L ≤ ε_u (Lemma SC (c)), so Z_j(w) exists; the depth-(j+1) configuration Y := (Z_j(w), w) with
datum v is a **full** critical point of 𝔉_{j+1}(·; v) (lower components: Z_j(w) is critical for 𝔉_j(·; w); top component: by
the envelope identity ∂_w𝔉_{j+1}(Z_j(w), w; v) = d_wF^cb_j(w, v) = 0). By Lemma SC (b) and BFT-E at depth j,
‖Y‖_{(σ),j+1} ≤ max(3L³C_0′‖w‖_D, ‖w‖_{T;v}) ≤ 3L²C_0′‖w‖_{T;v} ≤ 3L²C_0′r_B ≤ r_N. NSL at depth j + 1 gives g = e^{ξ′} ∈ 𝒢^{(j+1)}
with Y^g ∈ S_E^{(j+1)} (or Ker Γ^{(T)} if j + 1 = k, T ≤ 4) and ‖Y^g‖^C ≤ C_N·3L²C_0′r_B ≤ r_u; Y^g is a full critical point (In-4)
and ‖v‖_D ≤ ε_u, so Corollary K-U at depth j + 1 gives Y^g = Z_{j+1}(v); reading the level-j component, w^{ev^{(j)}g} = U^cb_j(v),
i.e. w = (U^cb_j(v))^h, h := (ev^{(j)}g)^{−1} ∈ 𝒢^{rt}_j. For j = 0 the same with Y := (w) and no Z_0. *Converse:* x := Z_{j+1}(v),
‖x‖_{(σ),j+1} ≤ C_0′‖v‖_D ≤ r_B ≤ R_B; ξ ∈ Λ_*^{(j+1)}, ‖ξ‖_♮ ≤ ρ_h = r_B ≤ R_B/4. x^{e^ξ} is a full critical point of 𝔉_{j+1}(·; v)
with the same value (In-4; the datum is fixed). Its norm, by (B0), Lemma A (d), (B1′) (5K_G(5ρ_h + r_B) ≤ 30K_Gr_B ≤ 1) and Lemma D
(η(x) ≤ 7r_B, η(x^{e^ξ}) ≤ 9r_B ≤ η_2): ‖x^{e^ξ}‖_{(σ),j+1} ≤ 3r_B + 2ρ_h + 4C_ΔL^{−3}(9r_B)² ≤ 6r_B. For j = 0 we are done (x^{e^ξ}
is then the point itself). For j ≥ 1 cut at depth j: by Lemma SC (a) the cut has ‖·‖_{(σ),j} ≤ 6r_B/L ≤ r_N and datum
w′ := (U^cb_j(v))^{ev^{(j)}e^ξ} with ‖w′‖_D ≤ 6r_B/L ≤ ε_u; NSL at depth j then K-U at depth j (C_N·6r_B/L ≤ r_u) identify the cut,
modulo 𝒢^{(j)}, with Z_j(w′); the envelope argument of (I2), verbatim, gives d_wF^cb_j(w′, v) = ∂_{x_j}𝔉_{j+1}(x^{e^ξ}; v) = 0 and
F^cb_j(w′, v) = 𝔉_{j+1}(x^{e^ξ}; v) = 𝔉_{j+1}(x; v) = E^cb_{j+1}(v).
**(I4).** ‖x*_{j+1}‖_D ≤ C_0s ≤ ε_lev for j + 1 < k (Lemma SC (a)), and = s ≤ ε_lev for j + 1 = k. *Criticality and value:* for
j + 1 = k they are (I2) with v = B_k and U^cb_{k−1}(B_k) = x*_{k−1}; for j + 1 < k, (I1) at depth j + 1 gives
(x*_{≤j})^{e^{ξ_{j+1}}} = Z_{j+1}(x*_{j+1}), and the computation of (I2) with y := x*_{≤j} (a full critical point of 𝔉_{j+1}(·; x*_{j+1})
by BA-1) gives d_wF^cb_j(x*_j, x*_{j+1}) = ∂_{x_j}𝔉_k(x*; B_k) = 0 and E^cb_{j+1}(x*_{j+1}) = 𝔉_{j+1}(x*_{≤j}; x*_{j+1}) = F^cb_j(x*_j,
x*_{j+1}). *Ball:* ‖x*_j‖_{T;x*_{j+1}} ≤ L^{−(k−j−1)}‖x*‖_{(σ),k} ≤ C_0′s ≤ r_B. *Gauge-equivalence:* (x*_j)^{ev^{(j)}e^{ξ_{j+1}}} =
U^cb_j(x*_{j+1}), so every critical point in the ball, being ≅ U^cb_j(x*_{j+1}) by (I3), is ≅ U_j. *Telescoping:* BA-1 / TOWER-VAR's
definition of 𝔉_k; E^cb_k(B_k) = 𝔉_k(Z_k(B_k); B_k) by definition. ∎

### 4.4 Remarks on Theorem ID
1. **Where (NSL) is used, and where it is not.** (I1) and (I3) use NSL at depth j or j + 1 to move a full critical point that is
   **not** in the depth's own slice (the witness of §1.2 shows it is not, in general) into that slice, inside the fixed radius r_u
   of Corollary K-U. The envelope step (I2) uses a **derivative** identity, not only values: ∂_w𝔉_j(Y^g; w) = ∂_w𝔉_j(Y; w) for
   g ∈ 𝒢^{(j)}, which holds because such g fix the datum level and 𝔉_j is invariant for **every** datum (In-4). GV55 §3.3's sketch
   ("the envelope step uses only values") is right in substance; this is the precise form.
2. **Codex GV §5.3's ball objection is met** by Corollary K-U plus the choice ε_ID ≤ Lr_u/(C_NC_0′): membership is in the
   **fixed** radius r_u, never in the datum-dependent C_0‖x*_j‖_D ball (which can be far smaller than L^{−(k−j)}s).
3. **The witness, revisited.** For B_k = hτe_1 everything lies in the abelian direction τ, the gauge action is affine
   (F ≡ 0 on commuting arguments), Lemma E's map is constant, and (I1)'s gauge is explicit:
   **ξ_j = −Λ^{(j)}(x̂_0) = L^{−k}h(1 − I_j)(I_k[z_1])·τ ≠ 0** — Codex GV §5.3's "root-pinned gauge I_j ev_j μ − μ", up to sign and
   normalisation.
4. **Uniformity.** No constant above depends on k, T or j: every input (BFT-E, K-U, NSL, Lemma SC) is uniform, and E^cb_j is
   defined at each depth **directly** by BFT-E on the fixed domain {‖w‖_D ≤ ε_u}; the recursion (I2) is a derived identity, so
   nothing shrinks from level to level. (Contrast §5.3.)
5. **Not covered:** complex data in (I1)/(I3)/(I4) (BFT-0's clause is for real V_k; BFT-2 is covered by BFT-E); non-wrapping boxes
   (REVIEW_S22's BFT also asks for them; GV55 §3.3 item 3); data off 𝒞_glob / non-trivial backgrounds; any global (non-local)
   uniqueness of the type (MIN_1). Uniqueness is local: in 𝔹_j(v), modulo 𝒢^{rt}_j.

*Clarification to (I2)-(I3).* The depth-(j+1) problem there is posed on any torus whose level-(j+1) coarse side is ≥ 3 (inside a
depth-k problem: T_{j+1} = TL^{k−j−1}); the constants do not see which.

---

## §5. Is E^cb = E^br needed? (target T4, second half; written ≈04:30-04:55Z)

### 5.1 Two readings of "E^br" in REVIEW_S22's clause
REVIEW_S22 "Statement (BFT)" takes "F_j = E_j^br + κ_jΣ_cφ̂_c and 𝔉_k as in PROOF [S20]-[S22] (TOWER-VAR)".
- **(R-B) Balaban's convention:** the per-level branch actions are *defined* as the composite ones, E^br_j := E^cb_j (BA-9's
  stated convention; REVIEW_S22 fix S22-6's "Alternative"; KFACTOR_OFF55 §1.3 "(CL-4) = BA-9 in Balaban's convention").
- **(R-P) PROOF's per-level branch:** E^br_1(V) := F(U(V), V) with U(V) Lemma BR1's critical branch (unique in BR1's sup ball of
  radius r(ε) = 12𝔠_∞ε about the lift U^{(0)}(V), in BR1's slice ker h_{U^{(0)}}), and E^br_{j+1} from BR1 run at level j on
  F^br_j = E^br_j + κ_jφ̂ — which PROOF has only under the per-level hypotheses (I_j) of NAH-ind, with radii shrinking per level
  (PROOF "(BG-unif), precise statement": "replacing BR1's ε_{i+1} ≤ ε_i/(1 + 36p_L𝔠_∞^{(i)}) and the C_♭^{(i+1)} recursion").

### 5.2 Reading (R-B): not needed — Theorem ID is the clause
In (R-B) the identity E^cb = E^br is a definition, and Theorem ID (I2)-(I4) is the content the clause asks for: the per-level
recursion E_{j+1}(v) = F_j(U_j(v), v) with U_j(v) critical, unique modulo 𝒢^{rt}_j in a level-uniform level-j ball, and the
telescoped identity E_k(V_k) = 𝔉_k(Z(V_k); V_k). BFT-2's literal branch-action version holds too: E^cb_k(B_k) = 𝔉_k(x*(B_k); B_k)
is holomorphic on BFT-E's polydisc (Codex GV item 4). So **in (R-B), E^cb = E^br is not an open input** and Codex GV item 4's
"Identification with E_k^br … remains NOT-VERIFIED" is discharged by Theorem ID **subject to a Codex check of Theorem NSL and
Theorem ID**.

### 5.3 Reading (R-P), level 1: Proposition E1 — PROVEN-HERE as an implication (of BR1 (i)-(ii) and Theorem ID (I3) at j = 0)
Let the level-1 coarse side be ≥ max(3, T_0) (T_0: BR1's torus threshold), κ_0 the coupling at which BR1 is run, and V = e^v real
in the global gauge with ‖v‖_D ≤ **ε_E1** := min(ε_br/4, ε_lev, r_B/2, ρ_lev/(48𝔠_∞ + 1)) (ε_br, 𝔠_∞ BR1's; their values involve
BR1's named not-computed inputs C_♭, C_Δ^{BR1}, r_♭ — only finiteness is used). Then **BR1's U(V) is gauge-equivalent under
𝒢^{(1)} to Z_1(v), and E_1^br(V) = E_1^cb(v).**
*Proof.* Plaquette holonomies are products of four link factors, so ε_V := max_P|log V_P| ≤ 4‖v‖_D (bi-invariant distance,
|log W| = d(W, 1) near 1; as in BA-2's proof); run BR1 with ε := 4‖v‖_D ≤ ε_br. BR1 (i)-(ii): U(V) = e^{A*}U^{(0)}(V),
‖A*‖_∞ ≤ 48𝔠_∞‖v‖_D, and U(V) is a critical point of F(·, V) = 𝔉_1(·; V) **without fixing**. In the global gauge U^{(0)}(V) has links
1 or V_c (Lemma U0), so x := log U(V) has ‖x‖_D ≤ (48𝔠_∞ + 1)‖v‖_D ≤ ρ_lev, i.e. x ∈ 𝔹_0(v) (Lemma SC (c), ‖v‖_D ≤ r_B/2).
F^cb_0(·, v) = 𝔉_1(·; v), so Theorem ID (I3) at j = 0 gives x = (Z_1(v))^h, h ∈ 𝒢^{rt}_0 = 𝒢^{(1)}, and E_1^br(V) = 𝔉_1(e^x; V) =
𝔉_1(exp Z_1(v); V) = E_1^cb(v) (In-4). ∎
This is the one place where two **different** slices meet (BR1's axial-type ker h_{U^{(0)}} and S_E^{(1)}), and NSL is what
connects them. Level-1 results proven for BR1's branch (PROOF [S20]: NAH1, BR1 (iii), the c36 checks) therefore hold for E_1^cb on
𝒞_glob(ε_E1), which is level 1 of the (R-B) tower.

### 5.4 Reading (R-P), levels j ≥ 2: a conditional transfer, not uniform
**Proposition E-ind — PROVEN-HERE as a conditional implication.** Fix j ≥ 1 and δ > 0. Suppose PROOF's level-j construction
supplies, for real v with ‖v‖_D ≤ δ: a function E^br_j with E^br_j = E^cb_j on a neighbourhood of every point used below, and a
critical point U^br_j(v) of F^br_j(·, v) := E^br_j + κ_jΣφ̂(·; e^v) with ‖log U^br_j(v)‖_D ≤ ρ_lev; and E^br_{j+1}(v) :=
F^br_j(U^br_j(v), v). Then **E^br_{j+1}(v) = E^cb_{j+1}(v) for ‖v‖_D ≤ min(δ, ε_lev, r_B/2).**
*Proof.* w := log U^br_j(v) ∈ 𝔹_j(v) is a critical point of F^cb_j(·, v) (the two functions agree near w). As in the proof of (I3),
(Z_j(w), w) is a full critical point of 𝔉_{j+1}(·; v), gauge-equivalent under 𝒢^{(j+1)} to Z_{j+1}(v); so E^br_{j+1}(v) = F^cb_j(w, v) =
𝔉_{j+1}(Z_j(w), w; v) = 𝔉_{j+1}(Z_{j+1}(v); v) = E^cb_{j+1}(v). ∎
*Why this does not give (R-P) uniformly.* The hypotheses are PROOF's per-level ones: E^br_j must exist and agree with E^cb_j on a
domain containing the level-j branch points, and BR1 at level j has radii that shrink per level (ε_{i+1} ≤ ε_i/(1 + 36p_L𝔠_∞^{(i)}),
PROOF "(BG-unif), precise statement"). Iterating E-ind therefore gives E^br_j = E^cb_j on balls whose radii depend on j. A
level-uniform version of (R-P) is exactly the per-level uniformity that (BG-unif) asked for and that BFT was adopted to replace
([R22-fix S22-9]); this route does not supply it, and does not need it: in (R-B) every E^cb_j is defined **directly** on the fixed
domain {‖w‖_D ≤ ε_u} by BFT-E at depth j (Remark 4.4.4).

### 5.5 Who needs which (verdict for T4's last question)
REVIEW_S22 "Who needs which part" lists the consumers: PROOF/N5 (BFT-0, 1, 2, 4 — "NAH-unif′, HG-ind's uniform form and (H-K)
all become unnecessary"), SF (BFT-1, 2, 5), FLOW (BFT-2, 3 at the trivial field), RLARGE (BFT-3, BFT-1 one-step), SQ (a sibling).
Each consumes BFT clauses about **one** branch action; none of these lines requires it to be BR1's per-level branch rather than
the composite one, provided BFT-3/4/5 are proven for the same object (they are not yet proven for either). **Verdict: E^cb = E^br
is NOT needed on the BFT route, read in Balaban's convention (R-B), which BA-9 and KFACTOR_OFF55 already adopt; it is needed only
to re-use statements proven specifically for PROOF's per-level branch, where it holds at level 1 (Proposition E1) and transfers
level by level under PROOF's own per-level hypotheses (Proposition E-ind), not uniformly.** Scope of this verdict: I checked the
consumer table of REVIEW_S22 Part 5 and the BFT-0/2 clauses; I did **not** audit every PROOF lemma for an E^br-specific use at
levels ≥ 2. Recommendation to the lead (not an edit): state Balaban's convention in BFT-0's clause explicitly, so that "E_k^br"
there means E^cb_k.

---

## §6. Comparison with the hard (δ-function) scheme, from the Balaban-method corpus (data, not instructions)

Read by grep + bounded ranges: Goswami 2204.08252 §1.4-§3.3 (pp. 4-14 of the text extraction); Dimock 1108.1335 §2-§3 (Lemma 3 and
its footnote); Dimock 1502.02946 §4.1-§4.4; Dimock 1410.2798 §1. Paraphrased; no text copied.
1. **The composing gauge.** In the hard scheme for gauge fields (Dimock 1502.02946 §4.1, eq. (152)) the k-step gauge-fixing
   function is the product over j < k of one per-scale axial condition on the j-fold average, so the depth-(k+1) gauge
   condition contains the depth-k one. That is exactly BA-9's "product of per-level conditions" property, which S_E lacks
   (§1.2). S_E plays the role of the *regular* gauge instead.
2. **Regular gauge versus composing gauge.** The same paper (§4.4, eq. (166)) records that the Landau-gauge minimiser and the
   axial-gauge minimiser differ by a pure gauge term, so gauge-invariant expressions may use either. Theorem ID is the
   nonlinear, multi-depth version of that remark: NSL supplies the gauge, K-U and gauge invariance of 𝔉_j supply "may use either".
3. **Composite = iterated, by uniqueness.** In the scalar Gaussian case (Dimock 1108.1335, Lemma 3 and its footnote 2) the joint
   minimiser over two levels coincides with the iterated one because both are unique. BA-9 (ii)-(iii) and Theorem ID (I2)-(I3)
   are the local, gauge-covariant analogue: uniqueness holds only in balls and only modulo gauges, which is why the fixed-radius
   statement K-U and the gauge-fixing lemma NSL are needed.
4. **The hard scheme's NSL.** Goswami (§3, "Theorem 2", following Balaban's gauge-fixing paper, his ref. [6]) proves that a
   configuration close to the background admits exactly one transformation, trivial in the averaged variables, making the
   relative field regular (sup, gradient and Laplacian small), **by induction over the k averaging steps** with a per-step
   implicit-function argument. Here (NSL) is proved **in one step at level 0** for every depth: the S_E condition reads x_0 only
   and Λ^{(j)} gains the derivative that the BCH remainder costs (Lemma A (c) with Lemma E), so no induction over scales and no
   scale-dependent loss occur.
5. **Uniqueness sets.** The hard scheme states the background's uniqueness on sets of *regular* configurations defined by
   gauge-invariant conditions (Goswami's (19) and Theorem 1: small bond/plaquette variables and the averaging constraint), so
   restriction to fewer steps is automatically compatible. Here uniqueness is stated in a slice ball (K-U), which is not
   restriction-compatible; NSL is the price. Codex GV §5.3's "direct gauge-invariant uniqueness argument" is the hard scheme's
   form of the statement; I did not pursue it.

---

**Precision to §6 items 4-5 (after re-reading Goswami §3.2, his (40)-(44)).** In the sigma model the "mapping transformations"
are the model's **global** symmetries, re-expressed relative to the background U_0 (his (41)-(42)), with the condition that their
k-step average be the identity (his (43)); the local-gauge original is Balaban's gauge-fixing paper (Goswami's ref. [6], cited
there for "Proposition 5"). Item 4's comparison is therefore with the structure of the argument (one transformation, fixed by an
averaged condition, found by induction over the k steps), not with a local gauge statement in that paper. Item 5's
"symmetry-invariant conditions" are, in Goswami's (19), smallness of the bond variables ∂U(b) − 1 and of δU (invariant under the
global symmetry); in Balaban's gauge theory the analogous conditions are on plaquettes.

---

## §7. Errata to the draft (§0-§3.6 above the RESUMED heading; the draft text is not edited)

- **E1 (dangling forward reference; load-bearing for one clause).** §1.2 (d) and its proof cite "Corollary K-U, §4.1" and a
  radius "r_u"; neither existed when the draft stopped (it ends at §3.6). As drafted, Proposition W (d) ("x̂ **is** the slice
  critical point") was unsupported: membership of x̂ in BFT-E's ball {‖x‖^C ≤ C_0|h|} would need C_W ≤ C_0, which nobody checked.
  **Repair:** Corollary K-U (§4.1 of this file, written after the RESUMED heading) is the fixed-radius uniqueness statement the
  draft meant; with it W (d) holds for |h| ≤ min(ε_u, r_u/C_W). Proposition W (a)-(c) — the non-preservation itself — never
  depended on (d) **for the conclusion "S_E^{(k)} points do not in general restrict into S_E^{(j)}"**: (a)-(c) exhibit an
  S_E^{(k)} point (a gauge transform of a critical point) with Λ^{(j)} ≠ 0. (d) only adds "and it is the BFT-E point".
- **E2 (systemic defect 1: the "new local names" claim is false).** §0 says "New local names introduced here and used nowhere
  else in the lane: C_Λ, C_alg, K_G, C_Δ, η_1, ρ_N, a_N, r_N, C_N, r_u, ε_u, ε_ID". A grep of $L/*.md shows: **C_Λ** = Lemma Λ's
  root-to-root constant C_Λ = 10 (BFT_A "13.11 Lemma Λ", BFT_B l.2243, GSHARP55 l.451) — a different object; **C_Δ** = the
  analyticity constant of PROOF's Lemma BR1 / N5-an ("a C_Δ evaluation, the binding one") — different, and live in §5.3 of this
  file (written C_Δ^{BR1} there); **η_1** is already three symbols in PROOF (l.102); **a_N** (PLD), **r_u** (BA-9 and Theorem BA,
  BFT_A; BFT_B l.1083), **ε_u** (TUNIF, NORMS, PROOF) are other objects; **r_N, C_N** are GV55's names for the same (NSL) object
  (consistent) and other files' names for other objects. Genuinely new: C_alg, K_G, ρ_N, ε_ID. Also inside the draft **R_0**
  names both Lemma B's radius 1/(20C_alg) and Lemma E's level-0 remainder R_0(x, ξ). No derivation is affected (each use is
  local and typed); read with the pins of §4.0.
- **Not errata (checked):** the draft's §0 drift note (REVIEW_S22 BFT-0 at l.387-408) is right; the draft's §1.4 timing note
  (Codex GV read after §1.1-1.2 were derived) is consistent with the check timestamps it cites; the "Campanato ≤ L^{−(2−α)(k−j)}"
  wording appears in GV55, not in the draft.

---

## §8. Findings, claim by claim

**Reviewed claims (prior files and the unreviewed draft).**
1. **GV55 §3.3 rank inequality and rank proof** ("Proof (rank count)"): **REFUTED.** Correct statement: N_0 − N_j < N_0 − N_k for
   j < k (N_i = (TL^{k−i})^4), so kernel inclusion implies a true inequality and the count proves nothing. Correct reason for
   non-preservation: quintic tents neither reproduce linear functions nor commute with subdivision (§1.2-§1.3). Agrees with
   Codex GV §5.1.
2. **GV55 §3.3 conclusion** ("a depth-k slice point restricted to depth j is in general not in the depth-j slice"):
   **CONFIRMED** (draft §1.2 (a)-(c), re-derived; Codex GV §5.2's independent witness gives the same exact number).
3. **GV55 §3.3 "(NSL) … OPEN; ARGUED-standard" and its IFT sketch:** the sketch's load-bearing steps — derivative at 0 is the
   identity on Λ_*; residuals controlled by exact covariance ρ(U^g) = Ad(g)ρ(U) plus |ρ − r| ≤ Ch³η² — **CONFIRMED**; the two
   missing pieces (BCH remainder in coarse units uniformly in the step h — Lemma B; |ρ − r| with the residual kept explicit, since
   for x^g the residual is the unknown — Lemma C) are supplied by the draft and re-verified. Status of (NSL): **PROVEN-HERE**
   (Theorem NSL), awaiting Codex.
4. **GV55 §3.3 "Given (NSL)_j, BA-9 goes through modulo depth-j gauges … hence to Z_j(U_j)":** **CONFIRMED with a repair** — the
   uniqueness region must be a ball of fixed radius (Corollary K-U), not the datum-dependent ball (Codex GV §5.3), and the
   envelope step uses a derivative identity valid because 𝒢^{(j)} fixes the datum level (Remark 4.4.1).
5. **GV55 §3.3 restriction scaling** ("potentials … L^{−(k−j)} … Campanato term by ≤ L^{−(2−α)(k−j)} … residual … L^{−(2+σ)(k−j)}"):
   **CONFIRMED** (Lemma SC (a)); the Campanato factor is in fact ≤ L^{−(2+α)(k−j)} (stronger; GV55's is true).
6. **GV55 §3.3 "Inherited on top of that, unchanged: E_j^{cb} = PROOF's E_j^{br}"** as an open input: **CONFIRMED as scoped** —
   it is open in reading (R-P) beyond level 1 (and true at level 1, Proposition E1), and **not an input at all** in reading
   (R-B), which BA-9 and KFACTOR_OFF55 adopt (§5).
7. **Draft §1.1:** CONFIRMED. 8. **Draft Proposition W (a)-(c):** CONFIRMED. 9. **Draft Proposition W (d):** CONFIRMED only
   with §4.1 (Erratum E1). 10. **Draft §1.3 remark (Γ′_j := (1 − I_j)Λ^{(k)}):** CONFIRMED (Γ′_jΞ = −1 on Λ_*^{(j)} since level-k
   roots are level-j roots; Γ′_j vanishes on S_E^{(k)}); not load-bearing. 11. **Draft §1.4:** CONFIRMED.
12.-17. **Draft Lemmas A, B, E, C, D and Theorem NSL (a)-(f):** CONFIRMED as implications of EP-int/EP-bd (Codex GSHARP item 1,
   l.225) and the uniform local analytic constants (Codex HIGHER item 1, §2), with LES-div as inherited named input (§R table).
18. **Draft §0 "new local names … used nowhere else in the lane":** **REFUTED** (Erratum E2; correct list of collisions there).
19. **Checks ns55_1 and ns55_2:** CONFIRMED (re-run, unchanged output; ns55_1's C5 and ns55_2's D6 are designed controls that fire
   as designed, so both checks could have failed).

**New results of this resumed run (PROVEN-HERE, unreviewed; not counted as CONFIRMED).**
- N1 **Corollary K-U** (§4.1): slice uniqueness in a fixed-radius ball, every depth — an immediate consequence of Codex-confirmed
  CCP (d) and Codex KOFF §5.3's source estimate.
- N2 **Lemma SC** (§4.2): norms under change of depth.
- N3 **Theorem ID** (§4.3): BFT-0's identification clause at the trivial background on 𝒞_glob, tori T ≥ 3, real data, in
  Balaban's convention, uniformly in k, T, j: (I1) restriction ≅ depth-j point; (I2) per-level criticality and value recursion;
  (I3) per-level uniqueness modulo 𝒢^{rt}_j in a fixed level-j ball (⊇ a fixed own-units sup ball); (I4) the tower and the
  telescoped identity E^cb_k(V_k) = 𝔉_k(Z(V_k); V_k).
- N4 **Proposition E1** (§5.3): E_1^br = E_1^cb on 𝒞_glob(ε_E1), given BR1 (i)-(ii).
- N5 **Proposition E-ind** (§5.4): level-by-level transfer under PROOF's per-level hypotheses; not uniform.
- N6 **Verdict on E^cb = E^br** (§5.5): not needed on the BFT route in Balaban's convention; needed only to re-use statements proven
  for PROOF's per-level branch (holds at level 1).

### 8.1 Summary table

| # | Claim (file, locating string) | Kind | Verdict |
|---|---|---|---|
| 1 | GV55 §3.3 "Proof (rank count)" | prior | **REFUTED** |
| 2 | GV55 §3.3 "in general **not** in the depth-j slice" | prior | CONFIRMED |
| 3 | GV55 §3.3 "(NSL)_j … ARGUED-standard" sketch | prior | CONFIRMED (sketch); (NSL) now PROVEN-HERE (N/A to count) |
| 4 | GV55 §3.3 "Given (NSL)_j, BA-9 goes through modulo depth-j gauges" | prior | CONFIRMED with repair (K-U; derivative form) |
| 5 | GV55 §3.3 restriction scaling factors | prior | CONFIRMED (Campanato factor stronger than stated) |
| 6 | GV55 §3.3 "E_j^{cb} = PROOF's E_j^{br}" as inherited open item | prior | CONFIRMED as scoped (open in (R-P) only) |
| 7 | NSL55 §1.1 rank inequality reversed | draft | CONFIRMED |
| 8 | NSL55 §1.2 Proposition W (a)-(c) | draft | CONFIRMED |
| 9 | NSL55 §1.2 Proposition W (d) | draft | CONFIRMED with §4.1 (Erratum E1) |
| 10 | NSL55 §1.3 Γ′_j remark | draft | CONFIRMED (not load-bearing) |
| 11 | NSL55 §1.4 comparison with Codex GV §5 | draft | CONFIRMED |
| 12 | NSL55 §3.1 Lemma A | draft | CONFIRMED |
| 13 | NSL55 §3.2 Lemma B | draft | CONFIRMED |
| 14 | NSL55 §3.3 Lemma E | draft | CONFIRMED |
| 15 | NSL55 §3.4 Lemma C | draft | CONFIRMED |
| 16 | NSL55 §3.5 Lemma D | draft | CONFIRMED |
| 17 | NSL55 §2/§3.6 Theorem NSL (a)-(f) | draft | CONFIRMED (as implication) |
| 18 | NSL55 §0 "used nowhere else in the lane" | draft | **REFUTED** (E2) |
| 19 | checks ns55_1, ns55_2 | draft | CONFIRMED (re-run) |
| N1 | Corollary K-U | new | PROVEN-HERE |
| N2 | Lemma SC | new | PROVEN-HERE |
| N3 | Theorem ID (I1)-(I4) | new | PROVEN-HERE (implication) |
| N4 | Proposition E1 | new | PROVEN-HERE (implication of BR1) |
| N5 | Proposition E-ind | new | PROVEN-HERE (conditional) |
| N6 | E^cb = E^br not needed in (R-B) | new | finding (scope stated in §5.5) |

**Counts (reviewed claims 1-19): CONFIRMED 17, NOT-VERIFIED 0, REFUTED 2.** (Item 9 is counted CONFIRMED only because §4.1 now
exists; as drafted it was NOT-VERIFIED.) New results N1-N6 are not counted.

---

## §9. Codex verdicts used — agree or disagree (files as on disk at 02:58-04:55Z; each ends with its "Exactly what may be banked")

- **CODEX_REVIEW_GV** item 2 (GV-E): used as an input through BFT-E; not re-derived here — **agree** (no reason to doubt; scope
  respected). Item 3 (Γ_E = Λ, ΓΞ = −1 on root-pinned gauges, descended slices): re-derived from EP-alg and the lifting argument —
  **agree**. Item 4 (corrected contraction; "Identification with E_k^br … NOT-VERIFIED"): **agree** at the time; Theorem ID now
  supplies the identification in Balaban's convention (pending Codex), and §5 shows the literal-E^br reading is open only beyond
  level 1. Item 5 (rank proof REFUTED, witness CONFIRMED, NSL NOT-VERIFIED, "no impossibility claimed"): **agree** with all
  parts. §5.3 (fixed-radius uniqueness needed; NSL one sufficient route): **agree** — Corollary K-U implements exactly its fix.
  I **disagree** only with the lead's paraphrase in PROOF's [S26-BANKED] line, "(NSL) is genuinely needed": Codex says the direct
  restriction argument fails and NSL is a sufficient repair; necessity is not shown (by Codex, the draft or me).
- **CODEX_REVIEW_KOFF** item 2 (CCP (a)-(d)): the critical ⇒ fixed-point direction re-derived — **agree**. Items 3, 5 and §5.3
  (corrected K^{(σ)}, source bounds K(η + η′ + s), bookkeeping): used as inputs — **agree**.
- **CODEX_REVIEW_GSHARP** item 1 and its §2.5 paragraph (EP-bd: "Caccioppoli and LES-div thus control λ in C^{2,α} … by the local
  C^{1,α} norm of x_0"): this is Lemma A (c)'s input — **agree** (read BFT_B §16.2/16.4 against it).
- **CODEX_REVIEW_HIGHER** item 1 and §2 (X_0 = Qx + â, â₂ = avg B₂, |â| ≤ Cε_l³η², β vanishing on both axes): Lemma C is exactly this
  chain with the residual kept explicit — **agree**.

---

## §4.5 Addendum to §4.4 (written after §9): the recursion (I2) for complex data — PROVEN-HERE (short)
On a complex polydisc 𝒫 := {v : |v|_∞ ≤ ε′} with ε′ ≤ ε_lev small enough that BFT-E's complex contraction applies at depth j + 1
and keeps U^cb_j(v) inside the complex polydisc on which BFT-2 at depth j makes Z_j and E^cb_j holomorphic (Codex KOFF §5.3:
complexified contraction "after reducing ε₀ by another fixed factor"; Codex GV item 4), the maps
v ↦ E^cb_{j+1}(v) − F^cb_j(U^cb_j(v), v) and v ↦ d_wF^cb_j(U^cb_j(v), v) are holomorphic (φ̂ is holomorphic near the identity by
Codex KOFF §4.3's local completion) and vanish on the real points of 𝒫 by (I2); hence they vanish on 𝒫. So **the per-level value
recursion and criticality of (I2) hold for complex data** on a k-, T-, j-independent polydisc. Uniqueness (I3) remains a real
statement, as in REVIEW_S22's clause.

---

## §10. For the lead: precise status, what is missing, what should change (nothing here is banked; Codex first)

### 10.1 Status after this file
- **(NSL) at every depth: PROVEN-HERE** (Theorem NSL, §2-§3; re-verified §R): uniform in k, T, j (and σ); existence and uniqueness
  of the gauge in a ♮-ball, size 2C_Λ·n_0(x), (σ)-norm bound C_N = 4 + 3C_Λ, analyticity, Faddeev-Popov operator a ¼-perturbation
  of the identity. The linearisation the task asks about is **the identity** (Λ^{(j)}K_0 = −Λ^{(j)}Ξ = 1 on Λ_*^{(j)}), and no
  Schauder estimate beyond EP-bd is needed because Λ^{(j)} gains the derivative the BCH remainder costs.
- **BFT-0's identification clause: PROVEN-HERE as an implication, in Balaban's convention** (Theorem ID, §4.3), at the trivial
  background on 𝒞_glob, m = 0, tori T ≥ 3, real data, uniformly in k, T and j; the recursion also for complex data (§4.5).
- **E^cb = E^br: not needed** on the BFT route read in Balaban's convention; **true at level 1** for PROOF's BR1 branch
  (Proposition E1); level-by-level only under PROOF's own per-level hypotheses beyond (Proposition E-ind) — not uniform, not
  delivered, not needed (§5.5, with its stated audit scope).

### 10.2 Precisely what is still missing for BFT-0 (first-class statement)
1. A **Codex check** of Theorem NSL (§2-§3), Corollary K-U, Lemma SC, Theorem ID, Propositions E1/E-ind.
2. **Boxes:** REVIEW_S22's BFT also asks for every non-wrapping box with N5-sf0's boundary convention; BFT-E, NSL and ID are
   proved for tori only.
3. **Off 𝒞_glob / non-trivial backgrounds:** NSL's proof uses the trivial-chain slice Λ^{(j)} and its trivial-background C^{2,α}
   bound (EP-bd); a background version needs the background-covariant slice estimate (lane B's (N1)), OPEN, plus BFT-E itself off
   𝒞_glob (HANDOFF row "BFT off 𝒞_glob").
4. **The literal reading (R-P)** of "E^br" beyond level 1 (only if some consumer insists on PROOF's per-level branch).
5. Inherited, unchanged: every named lane-A input of BFT-E (LES-div, the C2-COF package, TR∞, GV-E's inputs).

### 10.3 What should change (the lead edits)
- **HANDOFF, row "BFT-0 identification"** ("slice form banked; the nonlinear slice lemma (NSL) open"): → "(NSL) and the
  identification clause PROVEN-HERE in Balaban's convention at the trivial background on 𝒞_glob, tori, real data (NSL55 Theorem NSL,
  Theorem ID); awaiting Codex. Open: boxes; off 𝒞_glob; the per-level-branch reading of E^br beyond level 1 (not needed)."
- **HANDOFF, row "BFT-3"** ("per-level identification … open") and **BFT34_55** ("BFT-0's per-level identification additionally
  needs GV55's (NSL)_j"; "the per-level identification ((NSL)_j) remain[s] OPEN"), **CODEX_REVIEW_BFT34** ("It proves neither the
  per-level tower identification …"): the identification premise is what Theorem ID (I4) supplies on 𝒞_glob at the trivial
  background, pending Codex. (Derivative bounds of BFT-3 are statements about the composite components in the S_E^{(k)} slice; the
  per-level representatives differ from them by the small gauges of (I1), which this file does not differentiate.)
- **PROOF [S26-BANKED] line** "(NSL) is genuinely needed": reword to Codex GV's own statement — the direct restriction argument
  fails (exact witness) and (NSL) is a sufficient repair — and, after Codex, record NSL55's results.
- **PROOF clause table row "| BFT-0/1/2 | OPEN on 𝒞_glob"**: after a Codex check, BFT-0 (both bullets, Balaban's convention),
  BFT-1 and BFT-2 hold on 𝒞_glob at the trivial background, m = 0, T ≥ 3, as implications of the named lane-A inputs; boxes and
  off-𝒞_glob stay OPEN.
- **REVIEW_S22's BFT-0 clause** should state Balaban's convention explicitly (E_k^br := 𝔉_k(Z(V_k); V_k)), as BA-9, KFACTOR_OFF55
  §1.3 and BFT34_55 l.106 already do.
- **Tally:** no change (lane-level results; the [S26-BANKED] header says such results do not move the 105-item tally).
- **Symbols:** C_Λ, C_Δ, η_1, r_u, ε_u, a_N, R_0 collide with lane symbols (Erratum E2); any quotation of NSL55 should carry the
  pins of §4.0.

### 10.4 Check record
No new numeric check was needed: every new step (§4-§5) is analytic, and no number in them changed a decision. The two existing
checks were re-run unchanged (§R). Files written by this resumed run: this file only (append-only below the RESUMED heading).

### 10.5 Correction to my own timestamps (resumed run; Erratum E3)
The time ranges I wrote in the headings of §R ("≈03:05-03:40Z"), §4 ("≈03:40-04:30Z"), §5 ("≈04:30-04:55Z") and §9 ("files as on
disk at 02:58-04:55Z") were estimates typed before reading the clock, and they are **wrong**. `date -u` gave 02:58:01 at the
RESUMED heading and **03:16:42** right after §10.4 was appended: everything from §R to §10.4 was written between 02:58:01 and
03:16:42 UTC (the derivations behind it were done in the same session before and between those appends). The Codex files I used
were read as they were on disk in that window (CODEX_REVIEW_GV.md mtime 01:36Z; the others earlier).
File times (macOS local = UTC−4): CODEX_REVIEW_GV 01:36:34Z, CODEX_REVIEW_HIGHER 01:23:37Z, CODEX_REVIEW_KOFF 01:10:45Z,
CODEX_REVIEW_GSHARP 00:52:28Z. Note for the lead: GV55 §0 recorded CODEX_REVIEW_KOFF's mtime as 01:06:39Z; the file on disk is
later (01:10:45Z). I used the file as it is now (its §1, §4.3, §5.3 and banked list); I did not diff it against GV55's reading.

### 10.6 Two more items found on re-reading (appended after §10.5; `date -u` 03:18:53 before ns55_3's criteria were written)
- **Erratum E4 (draft §3.2, Lemma B, non-load-bearing arithmetic).** The draft displays "K_G ≤ 2C_alg·max(m(1/20)·20²,
  2m(1/10)·10²) ≤ 1.5·10³". With C_alg = 8 the displayed expression is **≥ 2806 > 1.5·10³**, so the displayed chain is false.
  The derivation (majorant per word, one telescoped slot, |w|(1/20)^{|w|−2} ≤ 2(1/10)^{|w|−2}) gives **K_G ≤ C_alg·max(400·m(1/20),
  200·m(1/10)) ≤ 1403.1** — the "≤ 1.5·10³" is right for this expression, the extra factor 2 in the display is spurious.
  Exact rational check **ns55_3** (criteria `checks/ns55_3_criteria.md` written 03:18:53Z before `checks/ns55_3_kg.py`; output
  `checks/ns55_3_out.txt`): m(1/20) ∈ [0.3502613, 0.3502614], m(1/10) ∈ [0.8769288, 0.8769289] (rational brackets, width < 10^{−6});
  A (draft expression > 1500) PASS, B (re-derived < 1500) PASS; controls K1 (undefined at R = 9/50, where e^{0.72} > 2) and K3
  (exp/log consistency) fire as designed; OVERALL PASS. Only finiteness of K_G is used anywhere (thresholds r_N, a_N, r_B), so
  no conclusion changes.
- **Precision to §5.3's last sentence.** "Level-1 results proven for BR1's branch … therefore hold for E_1^cb" is meant for
  statements about the **function** E_1^br on the open overlap 𝒞_glob(ε_E1) (its values and derivatives there) and for
  **gauge-invariant** statements about the point U(V) (BR1 (iii): curvature and soft-fluctuation sizes, non-degeneracy modulo
  𝒢_V), which pass to Z_1(v) because the two points are 𝒢^{(1)}-equivalent. The c36 checks are finite numerical evidence for
  particular models and configurations; they are not "transferred" by Proposition E1 in any stronger sense.
- **Outcome of the resume pre-statement's refutation tests.** (i) ball membership: met by K-U (fixed radius r_u) — not refuted;
  (ii) the envelope identity needs only 𝒢^{(j)}-invariance of 𝔉_j for every datum (In-4), not slice preservation — not refuted;
  (iii) the per-level uniqueness region 𝔹_j(v) is a ball in the level-j variable w (for fixed v) and contains a fixed own-units
  sup ball — not refuted; (iv) invariance of F^cb_j(·, v) along the 𝒢^{rt}_j-orbit of U^cb_j(v) for small gauges is (I3)'s
  converse — not refuted. (Invariance at every point of 𝔹_j(v) is not claimed and not needed.)

### 10.7 Counts, final (supersedes the count line under §8.1)
Reviewed claims 1-19 of §8.1 plus **20: draft §3.2 "K_G ≤ 2C_alg·max(…) ≤ 1.5·10³" — REFUTED as displayed (E4; correct constant
≤ 1403.1, non-load-bearing)**: **CONFIRMED 17, NOT-VERIFIED 0, REFUTED 3** (items 1, 18, 20). New results N1-N6 not counted.
*Correction to §10.4.* One numeric check was added after §10.4 was written: **ns55_3** (§10.6; criteria before script). Files
written by this resumed run: `NSL55.md` (append-only below the RESUMED heading) and `checks/ns55_3_criteria.md`,
`checks/ns55_3_kg.py`, `checks/ns55_3_out.txt`. No other file was written; no git.

*Addendum to §6 item 3 (corpus, read after §10.7).* The same "joint minimiser = iterated minimiser" identity appears in Dimock II
(1212.5562, Lemma 2.3, with small-field regions Ω) and Dimock III (1304.0705, Appendix A, eqs. (227)-(230)): in each, minimising
the two-level functional jointly in (fine field, intermediate field) gives the iterated minimiser, with the composite minimiser
re-expressed through the intermediate one. These are quadratic (scalar, Gaussian) problems with global uniqueness and no gauge
group, so they support §6 item 3's analogy and nothing more; I found no gauge-field statement in Dimock I-III.
