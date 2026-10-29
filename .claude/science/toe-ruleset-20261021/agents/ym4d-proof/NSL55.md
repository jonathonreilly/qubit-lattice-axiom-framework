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
