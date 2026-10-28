# BFT_B: lane B of the background-field theorem (BFT-3 locality, BFT-4 branch-action class) — sessions 1-5, 2026-10-28

Owner of this file: BFT lane B. Writes only BFT_B.md, BFT_B_LOG.md, checks/bb*. Everything else read-only.
Target: REVIEW_S22.md Part 5, clauses **BFT-3** and **BFT-4**. Lane A (BFT_A.md) proves BFT-0/1/2; here they are
**named hypotheses**, used as stated in REVIEW_S22 Part 5 and never re-proved.

Inputs read before §1 was written (read-only): REVIEW_S22.md (all); PROOF.md [S18] N5-0/CT/N5-triv (l.5145-5243), [S19]
(l.5246-5540: N5-bg, N5-cov, AX, N5-an, CT♯, Theorem RW, RW-triv, N5-sf0, N5-sf_i), [S20] (l.5596-5935: U0, FPq, N5-an♭,
BR1, SC1, LOC, NAH1, N5-sf1, NAH-ind, (BG-unif)), [S21] (l.5955-6136: CURV-lin, CURV1, E3, NAH-unif), [S22]
(l.6159-6368: ENV, H-fac, HG1, LOC_1, CURV1_1, HG-ind, NAH-unif′, c38, TOWER-VAR, COMP); LINEAR_PACKAGE.md §1.3-1.4, §3.8,
§4 (N2-exp, N2-exp', Cor. 4.3, Lemma 4.4), §6.2 (KF, G♯_0-soft); SF.md §6.1 and §7.1 (Setting CE-exp, LOC-s, HULL,
Theorem CE-exp, CE-exp-𝒞, CE-exp^k with [RSF2-fix CEk-1/2]: (L-hol)_k NOT VIABLE, (L-loc)_k); FLOW.md §4 (SF-bg); RLARGE.md
§3.2 ((BG)_k, R_bg); HIST.md §14.2 (Lemma HF).

Status words (as in the ledger): PROVEN-HERE (complete argument written here), PROVEN as an implication (complete
argument from named hypotheses), ARGUED (a reason, not a proof), OPEN, [inference]. Nothing here is counted in the PROOF
tally; nothing here has been reviewed.

---

## 0. Conventions

- Levels, fields, F_j, 𝔉_k, Z^lift, S_k, U^(0), Π, h, C(U, V), 𝔠_∞, c_C, m_1, C_♭, r_♭, S_♭, α_*, ε_br: as in PROOF
  [S19]-[S22]. Left-trivialised complex coordinates of a level-k field: V = e^zV^r, V^r real, z = (z_y) ∈ (su(N)⊗C)^{links};
  ∂/∂V_k(y) := ∂/∂z_y (a block of N² - 1 complex partial derivatives; |·| the HS block norm of the multilinear form).
  **[RBB1-fix B1-3]** ∂/∂z_y is the *chart* derivative at e^zV^r. The left-trivialised derivative at V = e^zV^r differs from
  it by the local factor dexp_{z_y}^{±1} (depends on z_y alone; bounded on every domain used here), which changes the
  constants C_1, C_E of §2.2 by a factor ≤ (1 + O(ϱ))^n and nothing else.
- Distances: d_j = ℓ¹ torus distance of positions in level-j units; d := d_k when the target is BFT ("level-k units").
- **Trees.** For points x_0, …, x_n: 𝔱(x_0, …, x_n) := length of a minimal spanning tree (BFT's "tree"); 𝔱_S := length of a
  minimal Steiner tree (any connected graph of lattice paths containing the points, extra vertices allowed). Then
  ½𝔱 ≤ 𝔱_S ≤ 𝔱, and 𝔱_S ≤ Σ_{i≥1}d(x_0, x_i) ≤ n·max_i d(x_0, x_i) (the star is a connected graph).
  **[RBB1-fix BB-geo]** The star from x_0 is itself a *spanning* tree, so also **𝔱 ≤ n·max_i d(x_0, x_i)**, and for a pair
  version 𝔱(y_1, …, y_n) ≤ (n - 1)max_{i,j}d(y_i, y_j). Hence every "e^{-(μ/n)𝔱_S}" below may be read as "e^{-(μ/n)𝔱}" (BFT-3's
  minimal-spanning-tree form) with no factor 2 lost.
- Polymer norm of BFT-4: ||R||_𝒜 := Σ_{X∋0}sup_{𝒫}|R(X)|e^{m_0|X|}, X a connected set of level-k cubes of side M_c ≥ 1 (M_c
  fixed below), |X| its number of cubes, 𝒫 the BFT-2 polydisc.

---

## 1. Pre-stated lemmas (file created ≈04:53 UTC, 2026-10-28, right after a 04:52:52 UTC timestamp; before any proof in §2 and before the bb1 criteria, mtime 04:54:32 UTC) [post-hoc correction 05:07 UTC: an earlier header said "04:53-05:10", which was a guess; this section was written in one write at ≈04:53]

### 1.1 Abstract tools
- **Lemma BB-geo (trees).** (a) ½𝔱 ≤ 𝔱_S ≤ 𝔱. (b) For any finite tree τ whose leaves include x_0, …, x_n (internal vertices
  anywhere), Σ_{edges}d ≥ 𝔱_S(x_0, …, x_n). (c) Σ_{z}e^{-a d(x,z)} ≤ coth⁴(a/2) on every level torus (4 directions per
  position counted as in PROOF l.5252). *Planned: PROVEN-HERE (elementary).* **[RBB2-fix C2-1: (c) as written is the sum
  over positions z; for a sum over links (4 directions per position) the bound is 4coth⁴(a/2) (PROOF l.5252). Every use
  below in which the sum runs over links carries the factor 4 (§6.3 l.795 had it; §6.5 Step 1 did not and is corrected).]**
- **Lemma BB-C (Cauchy multi-point decay).** Let 𝒟 ⊂ C^{𝒴} be a polydisc of radius ϱ in every complex coordinate (around a
  point z_0), g: 𝒟 → C^q holomorphic, and suppose that at every point of 𝒟 and for every y, |∂g(x)/∂z_y| ≤ C_1e^{-μd(x,y)}
  (x a label of the component). Then at every point of the half polydisc, for n ≥ 1 and any y_1, …, y_n (repetitions
  allowed), |∂^ng(x)/∂z_{y_1}⋯∂z_{y_n}| ≤ C_1(n - 1)!(2/ϱ)^{n-1}e^{-μ max_id(x,y_i)} ≤ C_1(n - 1)!(2/ϱ)^{n-1}e^{-(μ/n)𝔱_S(x,y_1,…,y_n)}.
  The same with a pair: if |∂²G/∂z_y∂z_{y'}| ≤ C_2e^{-μd(y,y')} on 𝒟 for a scalar G, then for n ≥ 2
  |∂^nG/∂z_{y_1}⋯∂z_{y_n}| ≤ C_2(n - 2)!(2/ϱ)^{n-2}e^{-μ max_{i,j}d(y_i,y_j)} ≤ (…)e^{-(μ/(n-1))𝔱_S(y_1,…,y_n)}.
  *Planned: PROVEN-HERE.* (For su(N)⊗C-valued z_y read each z_y as N² - 1 complex coordinates; ϱ is per coordinate.)
- **Lemma BB-IFT (first derivatives of a critical point from a weighted inverse).** Abstract: Z(V) a holomorphic family of
  zeros of G(Z, V) = 0 in a fixed linear slice, ∂_ZG(Z(V), V) invertible with inverse 𝔊; if the V_y-source ∂_{V_y}G is
  supported within distance r_s of y with |·|_∞ ≤ S_1, and |𝔊|(x, x') ≤ G_0e^{-μd(x,x')} (block norms), then
  |∂Z(x)/∂V_y| ≤ G_0S_1n_se^{μr_s}e^{-μd(x,y)} (n_s the number of positions within r_s of y). *Planned: PROVEN-HERE.*
- **Lemma BB-MCT (multi-scale Combes-Thomas).** If an operator L = Σ_jL_j on a space with a **solid** norm (|K| ≤ |K'|
  entrywise ⇒ ||K|| ≤ ||K'||) has an inverse with ||L^{-1}|| ≤ G and the level-j parts have ranges r_j (level-k units) and
  absolute bounds || |L_j| || ≤ ℓ_j, then for every 1-Lipschitz f and m with m·Σ_jr_je^{mr_j}ℓ_j ≤ 1/(2G),
  ||e^{mf}L^{-1}e^{-mf}|| ≤ 2G. With r_j = r·L^{-(k-j)} and ℓ_j ≤ ℓ the condition is k-uniform. *Planned: PROVEN-HERE;
  the content is that the scale sum Σ_jL^{-(k-j)} converges. Its limitation (solid norms; COMP-F1) recorded in §2.*
- **Lemma BB-NL (BFT-0/1/2 do not imply BFT-3).** There is a family of functions satisfying the analytic hypotheses of
  BFT-0/2 (holomorphic, bounded on uniform polydiscs, gauge-invariant, extensive) whose first derivatives do not decay.
  *Planned: PROVEN-HERE (a toy); its point: locality needs a weighted linear estimate, not analyticity.*
  **[RBB1-fix B-NL-1] Retitled: "the analytic content of BFT-2 does not imply BFT-3".** The toy is not a critical point of
  𝔉_k. Correct reading: BFT-3 does not follow from BFT-0/1/2 *proven in unweighted norms (m = 0)*; it follows from them
  proven with exponential weights m > 0 (uniformly in the weight centre), via BB-IFT + BB-C (Proposition BB-3_k).

### 1.2 BFT-3 at level 1 (k = 1), from the ledger
- **Theorem BB-3_1 (BFT-3 at k = 1, every curvature-small background).** In the setting of Lemma BR1 (T ≥ T_0), with
  ϱ := min(α_*/8, r_♭/16) and ε_B ≤ ε_br the explicit threshold of §2.2: for every real V^r with ε_{V^r} ≤ ε_B/4 and every
  V = e^zV^r with |z_c| ≤ ϱ/2 (per coordinate), BR1's branch A*(V) ∈ ker h (h = h_{U^(0)(V)} is V-independent) obeys, for
  every n ≥ 1 and level-0 link b, level-1 links y_i,
    |∂^nA*(b)/∂z_{y_1}⋯∂z_{y_n}| ≤ C_1(n - 1)!(4/ϱ)^{n-1}e^{-(μ_1/n)𝔱_S(b,y_1,…,y_n)},  μ_1 := m_1/2 (level-0 units),
  and the same (with other constants) for the plaquette logs of U(V), for ρ(U(V), V), and, for n ≥ 2, for
  ∂^nE_1^br/∂z_{y_1}⋯∂z_{y_n} with e^{-(μ_1/(n-1))𝔱_S(y_1,…,y_n)}. In level-1 units the rate is ≥ Lμ_1/n - o(1).
  *Planned: PROVEN-HERE (⇐ N5-sf0 (b), N5-an♭, BR1 (i), (v), ENV, Lemma BB-C, BB-IFT).* At n = 1 the rate is μ_1 (no 1/n).
  For n ≤ 4 the BFT-3 statement with m_0 = Lμ_1/4 - O(1/L)·μ_1 in level-1 units follows. **[RBB2-fix R-1: the two rate
  phrasings above ("≥ Lμ_1/n - o(1)", "Lμ_1/4 - O(1/L)·μ_1") are superseded by the [RBB1-fix B1-2] replacement in §2.2
  (l.224-226 at session-2 numbering): rate exactly Lμ_1/n per level-1 unit with the constant factor e^{2dLμ_1n}, no o(1).]**
  **[RBB2-fix C2-3/D.4: the complex radius α_*/8 in ϱ (here and in §2.2 (F2), the definition of ϱ and proof step (1)) rests
  on BR1 (v)'s radius, which REVIEW_BFT_B_S2 D.4 finds unsupported by BR1's proof. Read throughout this file:
  ϱ := min(ϱ_B, r_♭/16), ϱ_B := ε_B/16 (≤ ϱ_br := ε_br/16), with ε_{V^r} ≤ ε_B/4 as stated. Reason for ε_B rather than
  ε_br: §2.2's contraction thresholds are in terms of ε_B, so the *complex* curvature of U^(0)(V) must be ≤ ε_B; with
  complex curvature ≤ (1 + c_B(ε_{V^r} + 4ϱ))(ε_{V^r} + 4ϱ) (BCH) and the complex continuation of Lemma U0 (iv) with factor
  c_ℂ ≤ 1.1 (Lemma U0-ℂ, §9), ε_{V^r} ≤ ε_B/4 and ϱ ≤ ε_B/16 give c_ℂ·(complex curvature) ≤ 0.6ε_B. The constants
  (4/ϱ)^{n-1}, (2/ϱ)^{n-1} change accordingly and stay ε-independent; no other step changes. The proposed restatement of
  BR1 (v) for PROOF's owner is in "FOR OTHER FILES (session 3)".]**

### 1.3 BFT-3 at general k
- **Proposition BB-3_k (BFT-3 ⇐ BFT-0/2 + a weighted inverse).** Name (H-𝔊_w)_k: at every point of the BFT-2 domain, the
  linearisation of 𝔉_k on S_k at Z(V_k) has an inverse 𝔊 whose response to any level-(k-1) source supported within the
  contour neighbourhood of a level-k link y, |s|_∞ ≤ 1, obeys |(𝔊s)(x)| ≤ G_0e^{-m d(x,y)} for every level-j link x
  (own units of level j, the slice representative). Then BFT-3 holds for n ≤ 4 with m_0 = m/4 (Cauchy route), and for
  ∂^nE_k^br, n ≤ 4, with m_0 = m/3 (one level: ENV). *Planned: PROVEN as an implication.*
  **[RBB1-fix B4-1/B4-2: (H-𝔊_w) restated; it is lane A's estimate]** "At Z(V_k) on S_k (the slice at the lift)" is withdrawn:
  by lane A's BA-2 (COMP-F2) the lift is not a centre in any BFT-admissible norm. (H-𝔊_w)_k is restated in lane A's (C-glob)
  centring (per-level covariant slice with Feynman terms, data in a global gauge on 𝒞_glob), and **(H-𝔊_w)_k := lane A's
  (H-lin^∇) with exponential weight m > 0, uniform in the weight centre y of f = d(·, y), plus (H-rem^∇) in the same
  weighted pair** (Neumann series from the trivial chain to Z(V)). The sub-item used is lane A's (G♯-res) (the top source
  s_y is a residual-type source s_{k-1}). The m = 0 → m > 0 step is this file's (H-op) (Combes-Thomas in the coarse-unit
  pair). Outside 𝒞_glob, (H-𝔊_w) inherits lane A's (UHL) + (SL-cov) through BA-11 patching. Nothing in (H-𝔊_w) is new
  relative to lane A: **the two lanes share one open linear estimate.**
- **Proposition BB-E1 (the E-part of BFT-3 is one-step).** ∂^nE_k^br/∂V_k^n involves only ∂^{n-1}U_{k-1}/∂V_k^{n-1}
  (ENV at level k - 1). *Planned: PROVEN-HERE (algebraic).* Consequence: BFT-3 for E_k^br ⇐ one-step locality of the
  level-(k-1) branch with level-(k-1) constants.
- **Failure mode B3-F1 (absolute composition of per-level tangents).** The per-level route to ∂U_j/∂V_k composes k - j
  one-step tangents; absolute row sums multiply. *Expected: OCCURS for the absolute estimate (Z_row ≈ 2.85 per level at
  level 0, c37 D2), not shown intrinsic.*
- **Failure mode B3-F2 (marginal level sum in ∂³E_k^br(1)).** By TOWER-VAR (d), ∂³E_k^br(1) is a sum over levels of local
  vertices on the composite linear legs; d = 4 power counting gives O(1) per level in level-k units, so an absolute bound
  grows ∝ k; a k-uniform C_0 needs the signed cancellation (non-running of the tree-level coupling). *Expected: OCCURS
  [inference]; the k-uniform n = 3, 4 part of BFT-3 for E is then a consequence of BFT-4, not an input to it.*
  **[RBB1-fix B3F2-1: this expectation is NOT ESTABLISHED and its dependency conclusion is withdrawn; see §2.3.]** The
  count treats the soft cubic vertex as generic; it is κ⟨r_l, ρ^{(2)}_l⟩ (residual-carrying), which lane A's centring
  (CEN2/BA-4, BA-6) makes irrelevant (L^{-(k-l)} per level, a geometric level sum). The k-uniform constant of the E-part
  at n ≤ 4 follows from BFT-1/2 by BB-E1 + Cauchy; decay follows from (H-𝔊_w). Not "a consequence of BFT-4".

### 1.4 BFT-4
- **Construction BB-loc (gauge-invariant localisation by lift-pinning).** For a set Y of level-k cubes (unions of level-1
  blocks at k = 1), the pinned branch value E_Y(V): the branch problem with the fluctuation restricted to Y (U = U^(0)(V)
  off Y); R(X) := Σ_{Y⊂X}(-1)^{|X∖Y|}[E_Y - E_∅]. Claims: (a) E^br = E_∅ + Σ_{X≠∅}R(X) exactly (Möbius); (b) each R(X)
  is gauge invariant and depends on V only on X^+ (a fixed fattening); (c) R(X) = 0 unless X^+-connected; (d) E_∅ =
  L^{d-2}S_W(V) at k = 1 (the lift's corner plaquettes). *Planned: (a)-(d) PROVEN-HERE at k = 1 (the pinned problems exist
  by BR1's proof on compressions); general k as an implication of BFT-0 on pinned composite problems.*
  **[RBB1-fix B-loc-2: the general-k clause is withdrawn.** Pinned to the composite lift, E_∅ = L^{k(d-2)}S_W(V_k) =
  L^{2k}S_W(V_k) (TOWER-VAR (b)), single-cube activities are O(L^{2k}), and by BA-2 the pinned composite problems have no
  centre in lane A's 𝔐^∇. BB-loc is restricted to the one-step use (level j → j + 1, pinned to the one-step lift).]
- **Lemma BB-mix ⇒ bound.** Name (BB-mix): the pinned densities have mixed differences of every order in distinct cubes
  bounded by K^{|X|}Σ_{trees}Πe^{-m d} (a sum over trees, geometric in |X|). Then ||R||_𝒜 ≤ C for m_0 < m - c(M_c).
  *Planned: PROVEN as an implication.* **[RBB1-fix B-mix-1: superseded 05:09 UTC (session 1): see §2.4, where (BB-mix) is
  per-cube smallness |R(X)| ≤ C_RK^{(|X|-n_0)_+}, K < e^{-m_0}/(80e); the tree-sum form above is withdrawn.]**
- **Proposition BB-mix-gap (why BFT-3's n ≤ 4 does not suffice).** The Möbius term R(X) is an |X|-th order mixed
  difference; first-order decay plus Cauchy gives only e^{-μ max d}, and the polymer sum of e^{-μ max d} diverges.
  *Planned: PROVEN-HERE (the divergence of the sum; the exact term).* **[RBB1-fix B-mix-1: superseded 05:09 UTC (session
  1): the divergence claim is false (polymers are *-connected; lattice animals grow only exponentially); see §2.4.]**
- **Lemma BB-env (the linearised classical step is a pull-back).** For E_{k+1}^br as a functional of the level-k action
  A_k = S_W + R_k: D_{R_k}E_{k+1}^br[δR](V) = δR(U_k(V)) (U_k(V) the branch for A_k). *Planned: PROVEN-HERE (envelope).*
- **Proposition BB-4-ind (per-level induction for BFT-4).** ||R_{k+1}||_𝒜 ≤ C_W + λ||R_k||_𝒜 + C_Q||R_k||_𝒜² ⇐ named
  one-step estimates; ⇒ sup_k||R_k||_𝒜 < ∞ and the optional strengthening when the map contracts. *Planned: PROVEN as an
  implication; its hypotheses OPEN and named exactly.*
- **Corollary BB-4c (Cauchy consequences of BFT-4).** BFT-4 + BFT-2 ⇒ C_♭^{(k)} ≤ C(||R_k||_𝒜), ∇R_k(1) = 0, (H-G) at
  every level with level-uniform constants (near/far split built in), hence (H-C⁺) for the per-level route without the
  θ-cascade CURV-F2″; and BFT-3's E-part for n ≤ 4. *Planned: PROVEN as an implication.*

### 1.5 Check bb1 (criteria in checks/bb1_criteria.md before the script)
The level-1 derivative decay at the trivial background in d = 4, L = 3: the branch tangent ∂U_0/∂V_1 in two
representatives (SC1's κC^0Q^T, BR1's J - C^0d^*ιd_1), their gauge equivalence, and the decay of ∂U_0/∂V_1 and of
∂²E_1^br = H_1 by coarse shell.

---

## 2. Proofs (appended in one write at 05:05 UTC, after §1, after the bb1 criteria and after bb1 A/B had run at 04:55-04:56 UTC)

### 2.1 Abstract tools

**Lemma BB-geo: PROVEN-HERE.** Define 𝔱_S(x_0, …, x_n) := inf over finite trees τ whose vertex set contains x_0, …, x_n of
Σ_{edges {u,v} of τ}d(u, v). (b) is then the definition. (a) 𝔱_S ≤ 𝔱 (an MST is such a tree). Given a tree τ, an Euler tour
of the doubled tree visits every vertex and has length 2Σd; deleting repeated and auxiliary vertices (triangle inequality)
leaves a path through x_0, …, x_n of length ≤ 2Σd, which is a spanning tree: 𝔱 ≤ 2𝔱_S. The star from x_0 is a tree, so
𝔱_S ≤ Σ_id(x_0, x_i) ≤ n·max_id(x_0, x_i). (c) is PROOF l.5252. ∎

**Lemma BB-C: PROVEN-HERE.** Fix w in the half polydisc; the polydisc of radius ϱ/2 about w (every coordinate) lies in 𝒟.
Choose i* with d(x, y_{i*}) = max_id(x, y_i) and put h := ∂g(x)/∂z_{y_{i*}}, holomorphic on 𝒟 with |h| ≤ C_1e^{-μd(x,y_{i*})}.
Derivatives commute, so ∂^ng(x)/∂z_{y_1}⋯∂z_{y_n} = ∂^αh with α the multi-index of the other n - 1 derivatives (|α| = n - 1).
Cauchy's inequality on the polydisc of radius ϱ/2 about w: |∂^αh(w)| ≤ α!·sup|h|·(2/ϱ)^{|α|} ≤ (n - 1)!(2/ϱ)^{n-1}C_1e^{-μd(x,y_{i*})}.
The star bound of BB-geo gives max_id(x, y_i) ≥ 𝔱_S/n. The pair version: choose (i*, j*) maximising d(y_i, y_j), put
h := ∂²G/∂z_{y_{i*}}∂z_{y_{j*}}, apply Cauchy to the remaining n - 2 derivatives, and use 𝔱_S(y_1, …, y_n) ≤ Σ_jd(y_{i*}, y_j)
≤ (n - 1)max_{i,j}d(y_i, y_j). ∎ (Block form: for z_y ∈ su(N)⊗C each ∂/∂z_y is N² - 1 coordinate derivatives; the bound holds
coordinatewise, and for the HS block norm of the n-linear form with an extra factor ≤ (N² - 1)^{n/2}.)

**Lemma BB-IFT: PROVEN-HERE.** Differentiating G(Z(V), V) = 0 in V_y: ∂_ZG·∂_{V_y}Z = -∂_{V_y}G, so ∂_{V_y}Z = -𝔊∂_{V_y}G
(both sides in the slice). Then |∂Z(x)/∂V_y| ≤ Σ_{x'}|𝔊|(x, x')|∂_{V_y}G(x')| ≤ G_0S_1Σ_{d(x',y)≤r_s}e^{-μd(x,x')} ≤
G_0S_1n_se^{μr_s}e^{-μd(x,y)} (d(x, x') ≥ d(x, y) - r_s). ∎

**Lemma BB-MCT: PROVEN-HERE.** L_f := e^{mf}Le^{-mf} = L + Δ, Δ = Σ_j(e^{mf}L_je^{-mf} - L_j), with entries
L_j(x, x')(e^{m(f(x)-f(x'))} - 1); L_j(x, x') ≠ 0 only for d(x, x') ≤ r_j and f is 1-Lipschitz, so |Δ| ≤ Σ_j(e^{mr_j} - 1)|L_j| ≤
Σ_jmr_je^{mr_j}|L_j| entrywise. Solidity gives ||Δ|| ≤ mΣ_jr_je^{mr_j}ℓ_j ≤ 1/(2G), so L_f = L(1 + L^{-1}Δ) with ||L^{-1}Δ|| ≤ ½,
||L_f^{-1}|| ≤ 2G, and L_f^{-1} = e^{mf}L^{-1}e^{-mf}. In the sup norm with f := d(·, y) this is a column decay bound
|(L^{-1}s)(x)| ≤ 2Ge^{mr_s}|s|_∞e^{-md(x,y)} for s supported within r_s of y. With r_j = rL^{-(k-j)}: Σ_jr_j ≤ rL/(L - 1). ∎
*Limitation (the exact loss, recorded as failure mode **B3-F3: OCCURS for solid norms**).* The hypothesis ||L^{-1}|| ≤ G with
G uniform in k is false for the composite operator in the solid norms where the commutator estimate is automatic: in
ℓ^∞ → ℓ^∞, ||𝓛^{-1}|| ≳ L^{2(k-1)} (SF §6.2, REVIEW_HIST_S4 S4-1; COMP-F1), and in own-units ℓ² the chain's gap is ≲ L^{-2(k-1)}
(test field: B_j the lift of a smooth level-(k-1) field, own-units size L^{-(k-1-j)}, Rayleigh quotient ≈ L^{-2(k-1)}). With
G ∝ L^{2k} the admissible m ∝ L^{-2k}: no uniform rate. In level-weighted ℓ² norms the diagonal weights commute with e^{mf}
(so the commutator bound survives), and the question becomes the uniform gap of the chain in a weighted ℓ²; at the trivial
background the back-substitution structure (§2.3) shows the column response is the composite lift, whose norm is
marginal (O(1) per level). In the non-solid pair (Hölder X_c, divergence-form Y; SF §33) the commutator [e^{mf}, L_j] is a
first-order operator that maps X_c → Y with norm O(mr_j) only if f is smoothed at scale L^{-(k-j)}: named **(H-op)**, OPEN.

**Lemma BB-NL: PROVEN-HERE.** On a level-k torus with n_P plaquettes take E(V) := n_P·φ(n_P^{-1}Σ_PRe tr(1 - V_P)) with φ
entire, φ(0) = 0, φ'(0) = 1. E is gauge invariant, holomorphic on every uniform polydisc in the left-trivialised coordinates,
extensive (|E| ≤ C n_P on the polydisc) and equals S_W at first order in the plaquette density. But ∂²E/∂z_y∂z_{y'} contains n_P^{-1}φ''·(∂_yS_W)(∂_{y'}S_W),
which is ≍ n_P^{-1} for every pair y, y' at the same order as the local term: no e^{-md(y,y')} bound with n_P-independent C
holds — and with E' := Σ_{blocks B}|B|φ(|B|^{-1}S_W|_B) over blocks of side ℓ (|B| plaquettes), the pair kernel is
≍ |B|^{-1} up to distance ℓ, so any decay bound C_0e^{-m_0d} forces ℓ ≲ log(C_0|B|)/m_0. So analyticity, boundedness on
polydiscs and gauge invariance do not imply BFT-3; locality must come from a weighted linear estimate on the actual
critical-point problem (BB-IFT, BB-MCT, §2.2-2.3). ∎ (The construction is a toy, not a branch action.)
**[RBB1-fix B-NL-1]** What is proven is that *the analytic content of BFT-2* does not imply BFT-3. BFT-0/1/2 proven by the
contraction in a norm with exponential weights m > 0 (BFT's 𝔐 has them) do give BFT-3 for n ≤ 4 (BB-IFT + BB-C; BB-3_k).

### 2.2 Theorem BB-3_1 (BFT-3 at k = 1): PROVEN-HERE

*Setting and constants.* Level 0 → 1 as in Lemma BR1, T ≥ T_0, κ_0 ∈ [κ_-, κ_+]. Facts used:
- (F1) The block-interior links of U^(0)(V) are 1 for every V (Lemma U0), so h_{U^(0)(V)} = h, Π_{U^(0)(V)} = Π and
  P_0 := P_res^{U^(0)(V)} (built from the block-interior transports M_U) do not depend on V; only D_0 = D_{U^(0)(V)} (through
  the crossing links) and f_V do. So BR1's A*(V) lives in the fixed space ker h.
- (F2) For V = e^zV^r with V^r real, ε_{V^r} ≤ ε_br/4 and |z_c| ≤ α_*/8 (HS), (U^(0)(V), V) ∈ 𝔑(α_*) and BR1's contraction
  holds with the same constants (Lemma BR1 (v)) **[RBB2-fix C2-3/D.4: with |z_c| ≤ ϱ_B := ε_B/16 in place of α_*/8 and
  ε_{V^r} ≤ ε_B/4; see §1.2]**; Theorem N5-sf0 (b) then gives |C_0|(b, b') ≤ c_Ce^{-m_1d(b,b')} for
  C_0 := C(U^(0)(V), V), and the entries of the gradient/Hessian of f_V and of D_0 are holomorphic with N5-an♭'s bounds on
  the polydisc of radius r_♭/2 in the local AX chart.
- Put ϱ := min(α_*/8, r_♭/16)/(N² - 1)^{1/2} (per complex coordinate of z_c; then |z_c|_HS ≤ min(α_*/8, r_♭/16)), μ_1 := m_1/2,
  c_N := 4coth⁴(m_1/4)c_C (≥ N_{μ_1}(|C_0|), BB-geo (c)), p_1 := N_{μ_1}(|Π|) + 1, r := 12𝔠_∞ε, and
    **ε_B := min{ε_br, 1/(48c_Np_1²e^{μ_1r_1}C_♭𝔠_∞)}** (so c_Np_1²e^{μ_1r_1}C_♭r ≤ ¼).
- r_g := r_1 + 3L + 2L (level-0 units): every entry of ∇f_V, of Hess f_V and of D_0 that depends on z_c is at level-0 distance
  ≤ r_g from the base of c (the variables of an entry lie in the blocks at coarse ℓ^∞ distance ≤ 2, Setting N5-bg; a coarse
  link enters through its L^{d-1} crossing links and its soft term); n_g := the number of level-0 links within r_g of a
  point (≤ 4(2r_g + 1)⁴).
- S_1 := sup over the domain of the block norm of ∂_{z_c}[Π(∇f_V(A) + D_0P_0D_0^*A)](b) at A = A*(V) (≤ (2S_♭/r_♭)(1 + 2(2d)^{1/2}r)
  ·(number of chart variables per entry), by N5-an♭'s Cauchy bound on its polydisc; explicit in S_♭, r_♭; not evaluated).

*Statement (as pre-stated, with the post-proof sharpening (4/ϱ) → (2/ϱ)).* For V = e^zV^r with ε_{V^r} ≤ ε_B/4 and
|z_c| ≤ ϱ/2 per coordinate, every n ≥ 1, level-0 link b and level-1 links y_1, …, y_n (coordinatewise derivatives):
  (i) **|∂A*(b)/∂z_y| ≤ C_1e^{-μ_1d_0(b,y)}, C_1 := 2c_C·S_1n_ge^{μ_1r_g}** (and at every point with |z_c| < ϱ);
  (ii) **|∂^nA*(b)/∂z_{y_1}⋯∂z_{y_n}| ≤ C_1(n - 1)!(2/ϱ)^{n-1}e^{-μ_1max_id_0(b,y_i)} ≤ C_1(n - 1)!(2/ϱ)^{n-1}e^{-(μ_1/n)𝔱_S}**;
  (iii) the same for every gauge-invariant local function of (U(V), V) at b of pattern radius r_p (plaquette logs, ρ_c),
       with C_1 → C_1^{loc}e^{μ_1r_p} and the pattern's Lipschitz constants;
  (iv) **for n ≥ 2: |∂^nE_1^br/∂z_{y_1}⋯∂z_{y_n}| ≤ C_E(n - 2)!(2/ϱ)^{n-2}e^{-μ_1max_{i,j}d_0(y_i,y_j)} ≤ (…)e^{-(μ_1/(n-1))𝔱_S}**,
       C_E := κ_0[c_π' + p_LC_1^{loc}]e^{μ_1(p_L+r_g)}; and |∇E_1^br| ≤ 24κ_0p_L𝔠_∞ε (HG1 (iv), real V; the complex bound by
       continuity of the same formula on the domain). **[RBB1-fix B1-3: "by continuity" → "by analytic continuation from
       real V" (the same formula, ENV, continues holomorphically from the totally real set).]**
In level-1 units d_0 ≥ L·d_1 - 2dL, so the rates are ≥ Lμ_1 - (2dLμ_1)/d_1 per level-1 unit, i.e. **m_0 = Lμ_1/n
asymptotically**, Lμ_1/4 for BFT-3's n ≤ 4 (E-part: Lμ_1/3). **[RBB1-fix B1-2: replace the previous sentence by:
e^{-μ_1𝔱^{(0)}} ≤ e^{2dLμ_1n}e^{-Lμ_1𝔱^{(1)}} (each of the n tree edges loses ≤ 2dL level-0 units), so the rate is Lμ_1/n per
level-1 unit with the constant factor e^{2dLμ_1n} ≈ 1; no "asymptotically".]** **[RBB1-fix scope]** Proven on tori T ≥ T_0
only; BFT's "every non-wrapping box with the boundary convention of N5-sf0" clause is not covered here.

*Proof.* (1) *Differentiability.* A*(z) is holomorphic in z on |z_c| < ϱ' := min(α_*/8, r_♭/16) (BR1 (v): uniform limit
of holomorphic iterates of a uniform contraction). **[RBB1-fix B1-4]** BR1 (v)'s domain is closed (|z_c| ≤ α_*/8) and the
iterates converge uniformly there, so holomorphy holds on a neighbourhood of every point with |z_c|_HS < α_*/8; the polydisc
𝒟 of step (5) is taken with per-coordinate radius ϱ(1 - δ), δ ∈ (0, 1) fixed (any δ; the constants change by (1 - δ)^{-(n-1)}),
so that 𝒟 lies in the open set where (1) gives holomorphy. (2) *The linearised operator and its inverse.* Differentiate the
fixed-point identity A* = Φ_z(A*), Φ_z(A) = A - C_0(z)Π[∇f_z(A) + D_0P_0D_0^*A], equivalently the equation 𝒢(A, z) :=
Π[∇f_z(A) + D_0P_0D_0^*A] = 0 on ker h (C_0Π is injective on the target, C_0ΠO_0 = 1 on ker h). ∂_A𝒢 = Π O_ch Π with
O_ch := Hess f_z(A*) + D_0P_0D_0^* = O_0 + Δ, O_0 := Hess f_z(0) + D_0P_0D_0^*, N_0(|Δ|) ≤ C_♭r and Δ of range r_1 (N5-an♭,
as in BR1's Lipschitz step: ||A*||_∞ ≤ r). On ker h, ΠO_chΠ = ΠO_0Π(1 + C_0ΠΔΠ), so 𝔊_ch := (ΠO_chΠ|_{ker h})^{-1} =
Σ_{n≥0}(-C_0ΠΔΠ)^nC_0, and N_{μ_1}(|C_0ΠΔΠ|) ≤ c_N·p_1²·e^{μ_1r_1}C_♭r ≤ ¼ (choice of ε_B; N_μ submultiplicative, and
N_{μ}(|Δ|) ≤ e^{μr_1}N_0(|Δ|) for range r_1). With M_μ(AB) ≤ N_μ(A)M_μ(B) (PROOF l.5250) and M_{μ_1}(C_0) ≤ c_C:
**|𝔊_ch|(b, b') ≤ (4/3)c_Ce^{-μ_1d(b,b')} ≤ 2c_Ce^{-μ_1d(b,b')}.** (3) *The source.* ∂_{z_c}𝒢(A, z) at fixed A: by (F1) only
f_z and D_0 depend on z; the dependence is through the crossing links of c (U^(0)_b = V_c there) and V_c in φ̂_c, so the
source is supported within r_g of c, with block norm ≤ S_1. (4) Lemma BB-IFT with G_0 = 2c_C, μ = μ_1: (i). The bound holds at
every point of |z_c| < ϱ' since steps (2)-(3) do. (5) (ii): Lemma BB-C with 𝒟 the polydisc of per-coordinate radius ϱ about
the real point (inside |z_c|_HS < ϱ'). (6) (iii): a local function q(U(V), V) at b reads the links of U(V) = e^{A*}U^(0)(V)
within r_p of b and V within r_p; its first z-derivative is a finite sum of (Lipschitz constant of q) × (∂A*/∂z_y or the
explicit z-dependence of U^(0), V), each ≤ const·e^{-μ_1(d_0(b,y) - r_p)}; then Lemma BB-C. (7) (iv): Lemma ENV (BR1 (ii) gives
criticality without fixing in every fine direction) gives ∇_cE_1^br(V) = -κ_0π(M̄_c(U(V))V_c^{-1}), a local function of U(V)
on the S4' contours of c (≤ p_L links each, within p_L of c) and of V_c; it is holomorphic in z (π continues as the traceless
part of (W - W^{-1})/2, PROOF l.6256), and its z_{y'}-derivative is bounded as in (6) by κ_0[c_π' + p_LC_1^{loc}]e^{μ_1(p_L+r_g)}·
e^{-μ_1d_0(c,y')} (c_π' the Lipschitz constant of π on the relevant set; the δ_{cy'} term included). Since ∂^nE_1^br/∂z_{y_1}⋯
∂z_{y_n} = ∂^{n-1}(∇_{y_1}E_1^br)/∂z_{y_2}⋯ (in any slot order), the pair version of Lemma BB-C applies with G := E_1^br. ∎

*What it is.* BFT-3 at k = 1 in full: every order n (not only n ≤ 4), every curvature-small real background and its
complex neighbourhood (not only V = 1), for the slice representative, the gauge-invariant local outputs and E_1^br, with
every constant traced to ledger constants (c_C, m_1, 𝔠_∞, C_♭, S_♭, r_♭, α_*). *What it is not.* Sharp: μ_1 = m_1/2 = 4.8·10⁻¹¹
(level-0 units; N5-w0's constants), so the proven rate is ≈ 10¹⁰ below the measured one (bb1: the n = 1 kernel decays at
≈ 1.7-2.4 per coarse ℓ^∞ shell, ℓ¹-weighted sums finite at μ = 0.5); and the Cauchy route divides the rate by n.
**[RBB1-fix B1-1: μ_1 was off by 2.** PROOF l.5471 gives m = 9.66·10⁻¹¹ (N5-w0) and m_1 = m/2 = 4.83·10⁻¹¹, so **μ_1 = m_1/2
≈ 2.4·10⁻¹¹** (level-0 units) and **Lμ_1 ≈ 7.2·10⁻¹¹ per level-1 unit**. The measured rate to compare with is the ℓ¹ one,
0.5-1 per level-1 unit (bb1 A3, B-bb1-2), so the gap is still ≈ 10¹⁰.] The
kernel-composition alternative (D²A* = -𝔊_ch[D³-vertex(DA*, DA*) + …], Steiner sums, BB-geo (b)) keeps the rate μ_1(1 - δ)
for every n ≤ 4 at the price of explicit vertex bounds; it is not written out here.

### 2.3 BFT-3 at general k

**Proposition BB-E1: PROVEN-HERE (algebraic).** [RBB1-fix BB-E1: E_{k-1}^br here is E^{cb} in Balaban's convention, lane A's
BA-9.] On the BFT-0 domain, E_k^br(V_k) = F_{k-1}(U_{k-1}(V_k), V_k) with U_{k-1}
critical for F_{k-1}(·, V_k) in every fine direction (BFT-0: the per-level tower), so Lemma ENV at level k - 1 gives
∇_yE_k^br(V_k) = -κ_{k-1}π(M̄^{(k-1)}_y(U_{k-1}(V_k))V_{k,y}^{-1}): a local function of U_{k-1} on the contours of y and of V_{k,y}.
Hence ∂^nE_k^br/∂V_k(y_1)⋯∂V_k(y_n) is a finite sum (Faà di Bruno) of products of derivatives of this local function with
∂^pU_{k-1}(x)/∂V_k(·)⋯ for p ≤ n - 1 and x on the contours of y_1. ∎ *Consequence:* the E-part of BFT-3 at level k needs only
the **one-step** derivatives ∂^pU_{k-1}/∂V_k^p, p ≤ 3, whose proof is Theorem BB-3_1's with the level-(k-1) operator in place of
the level-0 one: **BFT-3 (E-part, n ≤ 4) ⇐ (I_{k-1}) (a), (c) of NAH-ind with level-(k-1) constants** (CT♯/RW decay of the
level-(k-1) background covariance, analyticity of E_{k-1}^br on a uniform polydisc, its Hessian-Lipschitz constant), by the
proof of §2.2 verbatim. It is level-uniform exactly when those constants are, which Corollary BB-4c (§2.4) derives from
BFT-4 at level k - 1.

**Proposition BB-3_k: PROVEN as an implication.** Assume BFT-0, BFT-2 and (H-𝔊_w)_k (§1.3) at every point of the BFT-2
domain (with V_k real of curvature ≤ ε_0 and |z| ≤ r_ℂε_0: the polydisc is centred at each real point, of radius r_ℂε_0
independent of the point). Then for n ≤ 4, |∂^nU_j(x)/∂V_k(y_1)⋯∂V_k(y_n)| ≤ C_0e^{-(m/4)𝔱_S(x,y_1,…,y_n)} with
C_0 := G_0S_1n_se^{mr_s}·3!(2/(r_ℂε_0/(N² - 1)^{1/2}))³, and the same for ∂^nE_k^br with rate m/3. *Proof.* BFT-0 identifies
Z(V_k) with the per-level tower, so ∂Z/∂V_k(y) = -𝔊s_y with s_y := ∂_{V_k(y)}∇𝔉_k: only the top soft term
κ_{k-1}φ̂^{(k-1)}(M̄(U_{k-1}); V_k) depends on V_k(y), so s_y is a level-(k-1) source supported on the contour neighbourhood
of y, of size ≤ S_1 (BFT-1/2 bound the fields there). (H-𝔊_w) gives the n = 1 bound at every point of the domain;
BFT-2 gives holomorphy; Lemma BB-C gives n ≤ 4 with rate m/4 (star bound); Proposition BB-E1 + the pair version give the
E-part. ∎ *Remark (BFT-0/1/2 alone do not suffice):* Lemma BB-NL.
**[RBB1-fix B3k-1]** BB-C gives the bounds on the *half* polydisc: BFT-3 is obtained on |z| ≤ r_ℂε_0/2, i.e. with r_ℂ → r_ℂ/2
(or ε ≤ ε_0/2). The source bound S_1 on the complex domain is BFT-2's (BFT-1 holds on the complex ball). **[RBB1-fix
B4-1/B4-2]** (H-𝔊_w) is read as restated in §1.3: lane A's (H-lin^∇)_m + (H-rem^∇)_m in the (C-glob) centring; so on the
composite route BFT-3 (n ≤ 4, U_j and E parts) rests on exactly lane A's open items at m > 0: (G♯-res), (G♯_0-field^∇),
(LED-src), (G♯_0-fine-up), G♯_0-plain, (H-rem^∇), plus (H-op).

**What (H-𝔊_w) is, by back-substitution (PROVEN-HERE, algebraic).** Since the top source s_y lives at level k - 1 and the
tower is the per-level branch composition U_j = U_j(U_{j+1}(⋯U_{k-1}(V_k))), the chain rule gives
  **∂U_j/∂V_k = Ξ_{j←k}(V_k) := ζ_j∘ζ_{j+1}∘⋯∘ζ_{k-1}**, ζ_i := ∂U_i/∂U_{i+1} (the one-step tangents at the tower).
So (H-𝔊_w) is a uniform weighted bound for products of k - j one-step tangents, and the telescoping identity
  **Ξ_{j←k}(V) - Ξ^0_{j←k} = Σ_{i=j}^{k-1}Ξ_{j←i}(V)(ζ_i(V) - ζ_i^0)Ξ^0_{i+1←k}**
(Ξ^0 at V = 1; exact, Π a_i - Π b_i = Σ_i(Π_{<i}a)(a_i - b_i)(Π_{>i}b)) reduces it to: **(LEG_w)** the trivial composite
tangents Ξ^0_{i←k} (signed: the linear chain minimiser map B_k ↦ B_i in the slice) obey uniform pointwise bounds
C_Le^{-m d_k} and are bounded uniformly as operators in e^{±md}-weighted sup norms; and **(LOC-ζ)** in a local AX gauge
|ζ_i(V) - ζ_i^0|(x, x') ≤ C(level-i curvature within the box)e^{-m d_i(x,x')} + (far term e^{-mD}). Given BFT-1 with θ_w > 0,
the level-i curvature is ≤ C_0L^{-θ_w(k-i)}ε, so the sum over i converges: Σ_iL^{-θ_w(k-i)} ≤ 1/(1 - L^{-θ_w}). Status:
(LEG_w) **ARGUED** — for the gauge-invariant outputs it is PROVEN by LINEAR_PACKAGE (Theorem 4.2' (ii): the B_k-kernels of
r_i and f_0; Lemma 6.7 (KF): B_k ↦ f_l with |K| ≤ M_fe^{-m'd}, uniform in k, T, l); for the potentials themselves (an axial
representative from the curvature, path length ≤ 4L^{k-i} level-i units) it needs the curvature at level i to be
O(L^{-2(k-i)}) in own units with exponential weights (the weighted form of Proposition 3.3 BG-b-lin), not shown. (LOC-ζ)
at level 0 is Theorem BB-3_1's step (2) with Lemma LOC; at level i it is the same with (I_i) — level-uniform ⇐ BFT-4 at
level i (Corollary BB-4c).
**[RBB1-fix B3k-2/B3k-3; status of this paragraph]** (i) *Per-level alternative.* The telescoping route bounds ζ_i through the
per-level covariances at level i ((LOC-ζ) via (I_i)); it is the per-level (Balaban-type) alternative, outside BFT's
anti-circularity clause. The composite route is §1.3's restated (H-𝔊_w) = lane A's (H-lin^∇)_m. (ii) *Gronwall step.* The
telescoping has the non-trivial Ξ_{j←i}(V) on the left of each term; the reduction needs the iterated expansion
Ξ = Σ_{i_1<…<i_p}Ξ^0δ_{i_1}Ξ^0⋯δ_{i_p}Ξ^0 (δ_i := ζ_i(V) - ζ_i^0), which gives ||Ξ(V)|| ≤ C_Lexp(C_LΣ_i||δ_i||) in the weighted
operator norm provided ||Ξ^0_{a←b}|| ≤ C_L for **every** sub-chain a ≤ b: (LEG_w) is required for all sub-chains (a, b),
not only (i, k). (iii) *Gauge compatibility.* The local AX gauges used for (LOC-ζ) at the levels i must be compatible across
levels (block-constant at level i + 1); by lane A's (UHL) finding AX loses L^{k(1-α)} in the gradient for Hölder curvature
(fine for the sup bound on ζ_i, not for a chain-wide gauge). The gauge must be chosen once for the chain: lane A's global
gauge on 𝒞_glob, or (UHL) outside it. (iv) **[RBB1-fix B4-1] (LEG_w) is lane A's data-map row at m > 0**: the
configuration-level data map B_k ↦ x into 𝔐^∇ (BFT_A §3.11, "configuration-level (into 𝔐^∇): OPEN", with (G♯_0-field^∇));
the PROVEN half quoted above (LINEAR_PACKAGE 4.2' (ii), 6.7: gauge-invariant outputs) is that row's PROVEN half.

**Failure mode B3-F1: OCCURS for the absolute estimate.** Bounding Ξ_{j←k} by |ζ_j|⋯|ζ_{k-1}| (entrywise absolute values,
as in E3's recursion) multiplies row sums: Π_iN_0(|ζ_i|) with N_0(|ζ_0|) = Z_row = 2.849 (c37 D2; reproduced in bb1 A2:
2.848902 at T = 8, 2.866 at T = 10). So the absolute pointwise bound grows ≥ 2.85^{k-j} in level-j own units. It is not
shown intrinsic: the signed composite is the chain minimiser map, bounded uniformly by N2-lin for the gauge-invariant
outputs. **[RBB1-fix B3F1-1]** "grows ≥ 2.85^{k-j}" is withdrawn: for non-negative kernels N_0(|ζ_j|⋯|ζ_{k-1}|) lies between
Π(min row sums) and Π(max row sums); the rows differ over the 324 fine links per cell, and ζ_i for i ≥ 1 are different
operators (fine functional E_i^br + soft) whose row sums were not measured. Correct wording: **the absolute route's bound
is ≈ Π_iN_0(|ζ_i|), with N_0(|ζ_0|) = 2.85** (Z_row not T-converged at 1%: 2.849 at T = 8, 2.866 at T = 10).

**Failure mode B3-F2: OCCURS for the absolute estimate [power count, inference].** By TOWER-VAR (d), ∂³E_k^br(1) =
D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·] = Σ_{j<k}(level-j cubic vertex on the composite legs). In level-k units a level-j term carries
L^{4(k-j)} sites per unit volume, three legs of own-units size L^{-(k-j)} each (smooth spreading) and one derivative
(L^{-(k-j)}): O(1) per level, so the absolute sum is O(k). The level-uniform C_0 for the E-part at n = 3, 4 therefore
requires the signed cancellation — the per-level vertices telescope to the Wilson vertex up to irrelevant remainders
(c38 C: c_3 - c_2 ∝ s²; FLOW Lemma F-tree for the quadratic coefficient). This is BFT-4's content: Corollary BB-4c (iv)
derives the E-part of BFT-3 from BFT-4 by Cauchy, and c38 B's absolute-leg count N3^abs/N3 ≈ 22 at one level is the size
of what the absolute route loses per level.
**[RBB1-fix B3F2-1 (binding): B3-F2 is NOT ESTABLISHED; the dependency conclusion above is WITHDRAWN.]** (a) *The count is
incomplete.* By TOWER-VAR (c)-(d), φ̂ = ½|ρ|² + O(ρ⁴) and ρ = r + ρ^{(2)} + O(3), so the soft cubic vertex at level l is
κ⟨r_l, ρ^{(2)}_l⟩ (symmetrised): it carries the chain residual r_l (≲ L^{-2(k-1-l)} own on the composite legs; N2-lin,
lane A BA-3) and the S4' BCH commutator ρ^{(2)}_l, which lane A's CEN2 (BA-4) reduces to the leg oscillation on N(X, μ),
≲ L^{-3(k-l)} own on smooth legs (BA-6). The density is ≲ L^{-5(k-l)} per level-l site; L^{4(k-l)} sites per level-k unit
give **L^{-(k-l)} per level: a geometric level sum, irrelevant, not O(1)**. The Wilson cubic vertex lives at level 0 only.
The Lipschitz forms are not written (lane A's (H-rem^∇) is ARGUED for this reason): status "absolute generic bound O(k);
with the residual structure + CEN2, geometric [sizes PROVEN in BA-4/BA-6, unreviewed]". (b) *The dependency is wrong
independently of the count.* BB-E1 writes ∂^nE_k^br as derivatives of the local function ∇_yE = -κπ(M̄_y(U_{k-1})V_y^{-1}),
which BFT-1/2 make holomorphic and bounded (|π| ≲ soft fluctuation ≤ C_0ε) on the uniform polydisc; Cauchy gives
|∂^{n-1}∇_yE| ≤ (n - 1)!C(2/(r_ℂε_0))^{n-1} k-uniformly from BFT-1/2 alone, and decay from (H-𝔊_w) (BB-3_k). So **the
k-uniform constant ⇐ BFT-1/2 (Cauchy via BB-E1); decay ⇐ (H-𝔊_w)**. Corollary BB-4c (iv) remains a *second* derivation,
from BFT-4.

**FLOW's need (BFT-2/3 at z = 0, V_k = 1, orders ≤ 4), status.** n = 1 for the gauge-invariant outputs and n = 2 for E_k^br:
PROVEN (N2-exp' (ii), KF; H_k exponential, PROOF l.5204). n = 1 for the tower potentials: ⇐ (LEG_w) (ARGUED). n = 3, 4 for
E_k^br: by TOWER-VAR (d) explicit vertex × legs, each term exponentially local given (LEG_w), with the tree decay of
BB-geo (b) (the three legs meet at the vertex position: Σ_{legs}d ≥ 𝔱_S); the k-uniform constant is B3-F2's signed sum:
OPEN, ⊂ BFT-4. At k = 1: PROVEN (Theorem BB-3_1 at V = 1). **[RBB1-fix B3F2-1: "OPEN, ⊂ BFT-4" → "k-uniform constant ⇐
BFT-1/2 (Cauchy via BB-E1); decay ⇐ (H-𝔊_w) = lane A's (H-lin^∇)_m".]**

### 2.4 BFT-4

**Construction BB-loc at k = 1: (a)-(d) PROVEN-HERE.** Partition the level-1 torus into cubes Q of side M_c ≥ 3 level-1
blocks (T a multiple of M_c, or a product partition as in [R20-fix RW2-1]). For a set Y of cubes let Λ_Y := the level-0
links based in blocks of Y and H_Y := {A ∈ ker h : A_b = 0 for b ∉ Λ_Y}. Π is the identity on crossing links and acts within
blocks on interior links, so Λ_Y is Π-invariant and H_Y = Π-range ∩ ℓ²(Λ_Y). *Pinned branch.* Let K_Y := 1_YÕ(U^(0)(V), V)1_Y
(a compression; ≥ the same gap, and (RW1)/(RW2) hold for it with the same constants because compressions of compressions
are compressions, so Theorem N5-sf0 (b)'s bounds hold for C_{0,Y} := K_Y^{-1} - (1 - Π)1_Y, in particular N_0(|C_{0,Y}|) ≤ 𝔠_∞;
**[RBB1-fix B-loc-1]** RW's partition of Λ_Y is into the sets Ω_□ ∩ Λ_Y, which are not boxes, while Theorem RW is stated for
box partitions; its proof uses the partition only through (RW1)/(RW2) and the box-multiplicity counting, both inherited by
the intersections (CT♯ applies to the compressions (Õ(1, 1))_{Ω_□∩Λ_Y}, gap ≥ γ_0, D_m entrywise smaller)),
and Φ_Y(A) := A - C_{0,Y}1_YΠ[∇f_V(A) + D_0P_0D_0^*A] on H_Y. BR1's proof (Lipschitz ≤ 𝔠_∞C_♭r ≤ ½, ||Φ_Y(0)||_∞ ≤ 6𝔠_∞ε)
gives a unique fixed point A*_Y in the r-ball of H_Y, holomorphic on BR1 (v)'s complex neighbourhood **[RBB2-fix C2-3/D.4:
read |z_c| ≤ ϱ_br := ε_br/16 with ε_V ≤ ε_br/4 (complex curvature ≤ 0.6ε_br by the bound of §1.2's tag), not α_*/8]**. Put
  E_Y(V) := F(e^{A*_Y}U^(0)(V), V),  ΔE(Y) := E_Y - E_∅,  R(X) := Σ_{Y⊂X}(-1)^{|X∖Y|}ΔE(Y) (X ≠ ∅).
(a) A*_𝒬 = A* (Y = all cubes: H_𝒬 = ker h, K_𝒬 = Õ), so E_𝒬 = E_1^br; Möbius inversion (ΔE(∅) = 0) gives **E_1^br =
E_∅ + Σ_{∅≠X⊂𝒬}R(X)** exactly. (b) *Gauge invariance.* For a level-1 gauge G, U^(0)(GV) = ĜU^(0)(V) (U0 (iii)); R_Ĝ is
block-diagonal and preserves Λ_Y, ker h and the fixing (N5-cov); f_{GV}(R_ĜA) = f_V(A); so A*_Y(GV) = R_ĜA*_Y(V) and E_Y(GV) =
E_Y(V). *Support.* ΔE(Y) = Σ (densities touching supp A*_Y ⊂ Λ_Y)[value at e^{A*_Y}U^(0) - value at U^(0)], and A*_Y solves an
equation whose coefficients involve U^(0)(V) and V only within two blocks of Y (Setting N5-bg); so ΔE(Y), hence R(X), depends
on V only on X^+ := X ∪ (the cubes adjacent to X) (M_c ≥ 3). Being a gauge-invariant function on all fields that depends
only on V|_{X^+}, R(X) is a gauge-invariant function of V|_{X^+}. (c) *Polymers.* If X = X_1 ⊔ X_2 with no cube of X_1
adjacent (ℓ^∞ cube distance ≤ 1) to one of X_2, then for Y_i ⊂ X_i: Õ has range ≤ 1 block, so K_{Y_1∪Y_2} = K_{Y_1} ⊕ K_{Y_2},
the equation on H_{Y_1∪Y_2} splits (∇f_V, D_0P_0D_0^*, Π are of finite range ≤ 2 blocks < M_c), the fixed point is
A*_{Y_1} + A*_{Y_2}, and no density touches both supports: ΔE(Y_1 ∪ Y_2) = ΔE(Y_1) + ΔE(Y_2). The Möbius sum of an additive
function over a disconnected X vanishes. So **R(X) = 0 unless X is *-connected.** (d) At the lift, ρ_c = 0 (U0 (i)) so every
soft density vanishes, and the only non-trivial plaquettes are the L^{d-2} corner plaquettes per coarse plaquette (U0 (ii)):
**E_∅ = L^{d-2}S_W(V)**. Hence E_1^br = S_W + R_1 with R_1 := (L^{d-2} - 1)S_W + Σ_XR(X), a sum of gauge-invariant local
polymers (the S_W term split into single-plaquette polymers). ∎ *Remark.* The pinned values depend on the fixing
convention (the Lagrange step of BR1 (ii) needs the full space), but only through covariant choices; nothing above uses
criticality of A*_Y. ~~*General k:* the same construction for the composite problem with S_k-compressions, given BFT-0 on
the pinned composite problems (an implication; not written).~~ **[RBB1-fix B-loc-2: withdrawn.** Pinned to the *composite*
lift Z^lift off Y: (i) TOWER-VAR (b) (k-fold corners) gives E_∅ = L^{k(d-2)}S_W(V_k) = **L^{2k}S_W(V_k)**, single-cube
activities ΔE({Q}) ≈ (c - L^{2k})S_W|_Q = O(L^{2k}), so ||R_k||_𝒜 is not k-uniform for that decomposition (cancellations only
in the full Möbius sum); (ii) by BA-2 the pinned composite problems' centre is ≳ L^kε from the tower in every decaying
norm, so "BFT-0 on the pinned composite problems" is not available in lane A's 𝔐^∇. BB-loc is used only one step at a
time (level-k action → level k + 1, pinned to the one-step lift, factor L^{d-2} once). At k = 1 nothing changes: the
pinned problems are BR1's undecayed sup-norm contractions.]**

**Lemma BB-mix ⇒ bound: PROVEN as an implication** [post-proof correction 05:09 UTC: the first version of this item and of
BB-mix-gap below counted polymers as unconstrained subsets of a ball, which is wrong (R(X) = 0 unless X is *-connected),
and concluded a divergence that does not hold; both are rewritten here, and the pre-stated (BB-mix) of §1.4 is replaced by
the per-cube-smallness form]. Let c_an := 80e: the number of *-connected sets of n cubes containing a given cube is ≤ c_an^{n-1}
(connected subgraphs of a graph of degree Δ = 3⁴ - 1 = 80 containing a vertex; the standard bound (eΔ)^{n-1}). **(BB-mix)**:
|R(X)| ≤ C_RK^{(|X|-n_0)_+} on the polydisc, for some n_0 (compact clusters: the 2⁴ = 16 cubes around a common corner can all be
within one propagation length of a point, so no gain is expected below n_0 = 16) and **K < e^{-m_0}/c_an**. Then
||R||_𝒜 ≤ C_RΣ_{n≥1}c_an^{n-1}e^{m_0n}K^{(n-n_0)_+} < ∞. ∎ No decay with distance is needed beyond connectivity; what is needed
is **smallness per cube**. Its natural source is propagation across a cube: for a density at x to depend jointly on n cubes
when M_c ≫ 1/μ, at least (n - n_0) cube widths must be crossed, each costing e^{-μM_c}, so K ≈ Ce^{-μM_c} [inference] and
M_c ≳ (m_0 + log(Cc_an))/μ — at the proven μ = μ_1 ≈ 4.8·10⁻¹¹ (level-0 units) this is M_c ≳ 10¹¹·L^{-1} level-1 blocks, the
same order as CE-exp's M_min (SF §7.1: 3.2·10¹³ fine spacings). **[RBB1-fix B-mix-2 + B1-1: the gain is overstated by ≈ 2^d
in the exponent.** In a compact blob of n cubes a density's dependence tree can visit ≈ 2^d = 16 cubes per corner point,
so the Steiner length needed is ≳ (n/2^d - 1)M_c, not (n - n_0)M_c: the natural per-cube factor is **K ≈ Ce^{-μM_c/2^d}**,
and M_c ≳ 2^d(m_0 + log(Cc_an))/μ. With μ = μ_1 ≈ 2.4·10⁻¹¹ (B1-1) this is M_c ≳ 10¹³ level-0 spacings ([inference];
still of CE-exp's order, 3.2·10¹³, SF l.785, which uses μ = m_1).]**

**Proposition BB-mix-gap: (1) PROVEN-HERE; (2) ARGUED (route NO-GO) [RBB1-fix B-mix-3: (2) bounds the coercivity radius of
one interpolation family; it does not show that no holomorphic family with a large radius exists, so it is a route
failure, not a theorem. Also: Cauchy about points t ∈ [0, 1]^X has radius ϱ - 1, so the requirement reads "the radius about
[0, 1]^X must exceed 1/K", not "ϱ ≥ 1/K". A different family (bond weights, not masses) is the subject of session 2's §5.]** (1) R(X) is the |X|-th order mixed difference of
Y ↦ ΔE(Y) over the |X| cubes of X. BFT-3 bounds derivatives of order ≤ 4 in V; for |X| > 4 they do not bound R(X) (the
Möbius difference in field variables would need V-derivatives of order |X| in |X| distinct cubes; in pinning variables there
is no derivative relation at all). (2) The Cauchy route to (BB-mix) needs a holomorphic family g(t), t ∈ C^X, with
g(1_Y) = ΔE(Y) for all Y ⊂ X, bounded on the polydisc |t_Q| ≤ ϱ with ϱ ≥ 1/K > c_ane^{m_0} ≈ 218e^{m_0}; then R(X) =
∫_{[0,1]^X}∂^X_tg and Cauchy gives |R(X)| ≤ sup|g|·ϱ^{-|X|}. The natural family — the mass interpolation G_t(Ã) = f(T_tÃ) +
½Σ_Q(1 - t_Q²)γ|Ã_Q|² (T_t = t_Q on Λ_Q; t_Q = 0 pins A_Q = 0, t_Q = 1 is the free problem; for real t ∈ [0, 1] the Hessian
T_tHT_t + (1 - t²)γ ≥ min(γ_H, γ) on the slice) — stays coercive only for |Im t_Q| ≲ γ/(4(S + γ)), S := ||Hess f + fixing||:
ϱ - 1 ≈ 10⁻¹¹ with the proven γ', ≈ 4·10⁻⁴ with the measured gap 0.04 and S ≈ 25 (c35 C). **Exact loss: the condition
number S/γ of the fluctuation operator, against the required ϱ > 218e^{m_0}.** So neither BFT-3 nor this family gives BFT-4;
the smallness must come from the cube size (Lemma BB-mix ⇒ bound, last paragraph), i.e. from an all-order version of the
propagation estimate. ∎ The same holds for a Taylor-plus-remainder localisation (the order-4 remainder ∫D⁴E(tv)[v, v, v, v]
has coefficients depending on all of v, so it is not a polymer sum).

**Routes to (BB-mix) (OPEN; recorded with their exact obstacles).**
- *(R1) Balaban's s-weakened background.* Write BR1's fixed point as A = C_0N(A), N(A) := -Π(g + R_2(A)) (C_0ΠO_0 = 1 on ker h),
  and define A(s) := the fixed point of A ↦ C_0(s)N(A), C_0(s) the s-weakened inverse of Theorem RW (iv) (with (1 - Π)
  removed). For |s_□| ≤ s̄, s̄ε_R ≤ ½, C_0(s) obeys RW (ii) with s̄ε_R, so the contraction (and A(s)) exists uniformly and
  is holomorphic in s; A(1) = A*; and every walk step costs s̄ε_R, a small parameter once R is enlarged (RW remark RW-2:
  R ≥ R_* + (2/(aL))log(s̄/(2θ))). **Pitfall (proved):** the map A ↦ A - C_0(s)𝒢(A) must NOT be used: C_0(s) = P(1 - R(s))^{-1}
  is injective (P = (K + t)^{-1}(1 - R(1)) at t = 0 is invertible), so its fixed points are the zeros of 𝒢 for every s and
  carry no s-dependence. **Remaining obstacle (exact term):** at s = 0 off 𝒴 the equation A = C_0(s)N(A) still couples
  neighbouring boxes through N (N(A)|_□ reads A on □^+), so A(s) has exponentially decaying (factor ≤ ½ per box, the
  contraction constant), not finite-support, dependence on far boxes; a second interpolation of the nonlinear couplings is
  needed, and its smallness per box is 𝔠_∞C_♭r = O(ε), which must beat the box-entropy 3⁴.
- *(R2) Tree expansion of the pinned problem in distinct cubes.* The mixed derivatives in cube-pinning parameters expand
  (Faà di Bruno) into trees with propagators 𝔊 (decay e^{-μd}) and vertices D^p∇f. **Exact loss:** a vertex of degree p in
  sup-norm directions costs (p/ϱ)^p ≈ p!e^p/ϱ^p (Cauchy for a multilinear form in non-coordinate directions; attained by
  (Σz)^p-type densities), so the bound is Σ_τΠ_v(deg v)!(…), which the 1/(n - 1)! of the polymer count does not absorb for
  star-like trees. Per-cube smallness again comes only from propagation across a cube (e^{-μM_c}), which requires
  μM_c ≫ log(81·p!-factors).

**Lemma BB-env: PROVEN-HERE.** Let A_k = S_W + R be a level-k action with a non-degenerate (modulo the level-k fluctuation
gauge) critical branch U_k^{(R)}(V) of F^{(R)}(U, V) := A_k(U) + κ_kΣ_cφ̂_c(M̄_c(U); V), real-analytic in (R, V) along a
one-parameter family R + sδR (δR gauge invariant and local; IFT as in SC1/E3). Then
  **d/ds|_{s=0} E_{k+1}^br[R + sδR](V) = δR(U_k^{(R)}(V)),**
  **d²/ds²|_{s=0} E_{k+1}^br[R + sδR](V) = -⟨∇δR, C∇δR⟩(U_k^{(R)}(V))**,
C the gauge-fixed covariance at the branch (Setting N5-bg with A_k in place of S_W). *Proof.* E(s) = F_s(U(s), V) with
∂_UF_s(U(s), V) = 0 in every fine direction, so E'(s) = ∂_sF_s = δR(U(s)) (first claim at s = 0). Then E''(0) = ⟨∇δR(U), U'(0)⟩
with U'(0) determined, modulo gauge directions against which ∇δR is orthogonal (gauge invariance of δR), by Hess F·U'(0) =
-∇δR; Lemma SC1's representative argument gives U'(0) = -C∇δR. ∎ So the linearised classical step is the **pull-back along
the branch**, and its second-order term is the one-step (not composite) covariance between two gradients.

**Proposition BB-4-ind (per-level induction): PROVEN as an implication.** Suppose that for a norm |||·||| on gauge-invariant
polymer sums (any norm; ||·||_𝒜 is one candidate) and every level-k action S_W + R with |||R||| ≤ ρ_R:
- (O1) the one-step branch exists with the BR1/N5-sf0 conclusions, constants depending only on ρ_R;
- (O2) E_{k+1}^br[R] - S_W admits a polymer representation (BB-loc at level k with (BB-mix) constants depending only on
  ρ_R), with |||E_{k+1}^br[0] - S_W||| ≤ C_W (one step from pure Wilson, the same at every level since the step is the same
  function in own units with κ_k ∈ [κ_-, κ_+]);
- (O3) |||δR∘U_k^{(R)}|||_{loc} ≤ λ|||δR||| for every δR in the tangent space, λ < 1 (the pull-back of BB-env);
- (O4) |||second-order remainder||| ≤ C_Q|||R|||² (BB-env's second derivative with the one-step covariance).
Then |||R_{k+1}||| ≤ C_W + λ|||R_k||| + C_Q|||R_k|||², and if 4C_QC_W ≤ (1 - λ)² and C_W ≤ ρ_R(1 - λ)/2, induction from R_0 = 0
gives **sup_k|||R_k||| ≤ r_* := (1 - λ - ((1 - λ)² - 4C_QC_W)^{1/2})/(2C_Q) ≤ 2C_W/(1 - λ)**. If (O3)-(O4) hold in Lipschitz form
(differences), |||R_{k+1} - R_k||| ≤ (λ + 2C_Qr_*)|||R_k - R_{k-1}|||, which is the optional strengthening with BFT-4's
λ := λ + 2C_Qr_* < 1. ∎ (Fine print: C_W includes the change of κ_k with k only through the uniform range [κ_-, κ_+]; the
estimate is one step, so no composite covariance enters — the anti-circularity clause is respected.)
**[RBB1-fix B4i-1/B4i-2/B4i-3 (binding)]** (1) *Description.* The last clause is false as written: BFT's clause forbids the
per-level covariances C^{(j)} as Newton inverses and asks for one contraction for 𝔉_k in 𝔐; (O1) is exactly a per-level
Newton inverse. Correct: **BB-4-ind is the per-level (Balaban-type) architecture, an alternative to BFT's composite route;
it is non-circular if (O1)-(O4) are proven with constants depending only on ρ_R, but it is outside BFT's
anti-circularity clause.** (2) *Scale invariance.* On a polydisc of radius ρ in curvature coordinates C_W ≍ c·ρ² (R_1 is
O(1)·S_W) and C_Q ≍ 1/ρ² (Cauchy), so 4C_QC_W is a ρ-independent O(1) number: shrinking ε_0 cannot make 4C_QC_W ≤ (1 - λ)²
true, and with λ ≥ 1 (B4-F1) the condition fails outright in ||·||_𝒜. For the same reason (O1) is not perturbative in R
(Hess R_1 is O(1) relative to Hess S_W): it is the non-perturbative per-level N5 for actions E_k^br (NAH-unif/(I_k)).
(3) *Lipschitz strengthening.* Φ_k depends on k through κ_k: |||R_{k+1} - R_k||| ≤ Lip·|||R_k - R_{k-1}||| + |||Φ_k(R_{k-1}) -
Φ_{k-1}(R_{k-1})|||; the second term vanishes only for constant κ_k and is summable only if Σ_k|κ_{k+1} - κ_k| < ∞, which is
an added hypothesis of the strengthening. **Session 2 does not use BB-4-ind** (§5 runs on the composite route).

**Failure mode B4-F1: (O3) FAILS in the polydisc-sup norm ||·||_𝒜 at quadratic order [power count + Schwarz lemma;
inference for the attainment].** Let δR(X) = Σ_{p,p'∈X}K(p, p')F_pF_{p'} + O(F³) (curvature-adapted coordinates, ∇δR(1) = 0 by
Corollary BB-4c (ii)). On the branch, U_k(V) has fine curvature ≈ ε/L² for V of curvature ε (BFT-1 with θ_w = 2, smooth
regime). Schwarz's lemma on the polydisc of radius ρ gives |δR(X)(U_k(V))| ≤ sup_𝒫|δR(X)|(L^{-2}ε/ρ)², and a coarse polymer
collects ≈ L^4 fine polymers: total L^4·L^{-4} = 1. So λ ≥ 1 for the quadratic part in ||·||_𝒜 (the zeroth moment of K is
marginal: Σ_fineF_fKF_f ≈ K̂(0)Σ_coarse|F|²). The contraction exists only after (i) extracting the marginal part (the
coefficient of the unique dimension-4 invariant, fixed by the quadratic normalisation: FLOW Lemma F-tree, c38 C) and (ii)
measuring the remainder in a norm that sees smoothness (field-derivative weights; Brydges-Yau-type Taylor norms), where the
second-moment part gains L^{-2}. **So BFT-4 as stated (polydisc sup norm) is a correct target for the conclusion, but the
per-level induction must run in a stronger norm with a Loc-extraction; in ||·||_𝒜 itself the induction cannot close.**

**Corollary BB-4c (Cauchy consequences of BFT-4): PROVEN as an implication.** Assume BFT-4 at level i (E_i^br = S_W + R_i,
||R_i||_𝒜 ≤ C_0, rate m_0 per cube of side M_c, R_i translation-invariant) on BFT-2's polydisc: every e^zV^r with V^r real of
curvature ≤ ε_0 and |z_c| ≤ ρ_c := r_ℂε_0 (HS; per coordinate ρ_c/(N² - 1)^{1/2}). Let n_Q := 4M_c⁴ (links per cube).
- (i) **C_♭^{(i)} ≤ C_♭(S_W) + 6(N² - 1)^{3/2}ρ_c^{-3}n_Q²(2/(em_0))²C_0** at every real point of curvature ≤ ε_0 (the class on
  which C_♭ is used, when ε + 4r ≤ ε_0). *Proof.* Σ_{b',b''}|∂_b∂_{b'}∂_{b''}R_i| ≤ Σ_{X∋b}(n_Q|X|)²·3!((N² - 1)^{1/2}/ρ_c)³sup|R_i(X)|
  (Cauchy on the polydisc, coordinatewise) and |X|²e^{-m_0|X|} ≤ (2/(em_0))². **[RBB1-fix B4c-1]** R_i(X) depends on V on X^+,
  not X (BB-loc (b)): the derivative sum runs over links of X^+, (n_Q|X^+|)² ≤ (81n_Q|X|)², over polymers X with b ∈ X^+. So
  (i) holds with the extra factor 81² (equivalently, re-index the polymers by X^+ with m_0 → m_0/81). The same replacement
  ("X^+ containing" for "X containing") is made in (iii) and (iv).
- (ii) **∇R_i(1) = 0** (and ∇_FR_i(X)(0) = 0 in curvature coordinates on contractible X). *Proof.* Constant gauges g act by
  V_b ↦ gV_bg^{-1}, fix 1, and act on the left-trivialised gradient by Ad_g; so ∇_bR_i(1) is Ad-invariant, and su(N) has no
  non-zero Ad-invariant vector (∫Ad_gX dg = 0). On contractible X a flat field is gauge-trivial on X, so the same argument
  applies at every flat point. **[RBB1-fix B4c-2]** (iii)'s far term uses this for *-connected X whose X^+ has holes, where
  flat fields with non-trivial holonomy are not gauge-trivial. Replace "Taylor about a flat point" by: Taylor-expand about
  V = 1 in an AX gauge of X^+ (links ≤ 3·diam(X^+)·ε, Lemma AX), at a cost poly(|X|) absorbed by e^{-(m_0/2)|X|}, valid for
  |X| ≲ r_ℂε_0/ε; for larger |X| use plain Cauchy, C e^{-(m_0/2)|X|} ≤ e^{-c/ε} ≪ ε.
- (iii) **(H-G) at level i with level-uniform constants, with the near/far split built in.** For a level-(i+1) field W of
  curvature ε, its lift U^{(i)}(W) and the AX gauge of a box Λ of side ℓ (lift links ≤ α = 3ℓε ≤ ρ_c/2):
  ∇E_i^br(U^{(i)}(W)) = H_iJa + e_g with a := log(GW) the AX potential (so log of the lift = Ja exactly, U0), H_i :=
  Hess E_i^br(1), and |e_g(b)| ≤ e_g^W(b) + C_R(α + ε)ε (near: polymers X ∋ b with X^+ ⊂ Λ; Taylor to second order about 1 in the
  AX chart, C_R := 2(N² - 1)ρ_c^{-2}n_Q²(2/(em_0))²C_0 up to the chart factor) + C_Re^{-(m_0/2)dist(b,Λ^c)/M_c}ε (far: polymers
  leaving Λ, bounded by Lipschitz-in-curvature at flat points via (ii)), with e_g^W the Wilson part of CURV1 step (3).
  *Proof.* ∇S_W at the lift is CURV1 step (3) verbatim at level i (the lift is the same construction at every level). For
  the polymers: near ones by Taylor with ∇R(1) = 0 and Hess R(1) summed into H_i; far ones: |∇R_i(X)(V)| ≤
  C ε sup|R_i(X)|/ρ_c² at real V of curvature ≤ ε (Taylor in curvature coordinates about a flat point, (ii)), summed over
  X ∋ b, X ⊄ Λ, |X| ≥ dist/M_c.
- (iv) **The E-part of BFT-3, every n**: |∂^nE_i^br/∂z_{y_1}⋯∂z_{y_n}| ≤ [n!((N² - 1)^{1/2}/ρ_c)^ne^{m_0n/2}C_0 + (Wilson, finite
  range)]·e^{-(m_0/(8M_c))𝔱_S(y_1,…,y_n)}. *Proof.* Only polymers X containing the cubes of all y's contribute; a *-connected
  X containing them has |X| - 1 ≥ (cube ℓ^∞ Steiner length) ≥ 𝔱_S/(4M_c) - n; split e^{m_0|X|} = e^{(m_0/2)|X|}e^{(m_0/2)|X|} and
  Cauchy.
- (v) **Level-uniform (I_i), hence (H-C⁺) without CURV-F2″.** In a local AX gauge, Hess E_i^br(U) - Hess E_i^br(1) is bounded
  in N_m (m < m_0/M_c) by C(C_0, ρ_c, m_0, M_c)(α + e^{-m_0D/(2M_c)}) (Cauchy for the near polymers, tails for the far ones),
  so (NA-H_loc)_i holds with δ_H^{(i)} depending only on these and on the level-independent soft/slice constants
  (N5-an♭); with N5-triv's level-uniform γ_i, Proposition N5-sf_i's proof gives 𝔠_∞^{(i)}, m^{(i)}, c_K^{(i)}, A_in^{(i)},
  A_out^{(i)} level-uniform. CURV1 at level i + 1 then takes (H-G) from (iii) at its own θ (the far term is chosen by the box
  size at that level), so no θ' at level i is called for: **the θ-cascade CURV-F2″ (REVIEW_S22 S22-5) does not arise**, and
  the r-compounding (S22-4) does not arise either (g is bounded in curvature form by (iii)). With BFT-2 supplying (H-ℂ),
  **NAH-unif′'s hypotheses reduce to (H-K) + BFT-2 + BFT-4.** ∎ (All "level-uniform" statements here mean: functions of
  (C_0, ρ_c, m_0, M_c) and of level-independent ledger constants; none is evaluated.)

---

## 3. Check bb1 (criteria checks/bb1_criteria.md, mtime 04:54:32 UTC; script checks/bb1_decay.py written after it; run record below)

Run record (runner scratchpad bb/run_bb1.sh and bb/run_diag.sh: `until mkdir …/locks/numeric; do sleep 20; done`, wait for
load1 < 8 and memory free ≥ 25%, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l,
`rmdir` exactly once per acquisition, no trap, no `timeout`, python without -I). Two acquisitions:
- A 04:55:13-04:56:07 UTC (load1 3.00, free 40%), 54 s, peak footprint 582 MB; B 04:56:07-04:56:36, 29 s, 562 MB.
- post-hoc diagnostic 05:02:12-05:02:43 (load1 2.77, free 42%), 31 s, 616 MB. No process left running; lock released.

Results (checks/bb1A.out, bb1B.out, bb1diag.out):
- **A1 PASS.** max|d(a_S - a_B)| = 6.0e-15, max|Q(a_S - a_B)| = 7.5e-14 (max|a_B| = 1.000): the SC1 and BR1 representatives of
  ∂U_0/∂V_1 are gauge-equivalent on every fibre (T = 8).
- **A2 FAIL (criterion pre-registered).** Z_row = 2.848902 (c37: 2.848907, within 2e-6) but Z_col = 156.686797 against c37's
  156.078934 (0.39%). *Post-hoc diagnostic (bb1_diag.py, added after reading A2; not a criterion):* c37's own code path
  reproduces 156.078934 exactly, and the same float32 kernel summed in float64 gives 156.686796; with complex128 solves cast
  to complex64 the float32 path again gives 156.078934. So **c37 D2's Z_col is a float32 accumulation artefact; the value is
  156.6868** (Z_colZ_row² = 1271.7, not 1266.8; E3's soft coefficient (1 + Z_col)(1 + Z_row)² = 2.33·10³, unchanged at 2
  digits). The recorded verdict stays FAIL. **[RBB1-fix B-bb1-1]** Which combination: (1 + Z_col)(1 + Z_row)² goes 2327 → 2336;
  c37 D2's printed (1 + Z_col)max(1, Z_row)² goes 1274.9 → 1279.8; both change in the third digit only. Z_row and Z_col are not
  T-converged at 1% (T = 8 → 10: 2.849 → 2.866, 156.69 → 158.06).
- **A3 PASS.** Max-entry profiles by coarse ℓ^∞ shell (T = 10): a_S 2.48e-1, 1.04e-1, 3.71e-2, 1.77e-3, 6.89e-4, 8.24e-5;
  a_B 6.33e-1, 2.10e-1, 1.20e-2, 2.90e-3, 1.67e-4, 6.11e-5; H_1 7.05e-1, 1.04e-1, 1.20e-2, 1.50e-3, 2.37e-4, 7.95e-5. Local rates
  (r_2, r_3) = (3.04, 0.95), (1.42, 2.85), (2.08, 1.85); T = 8 vs 10 agree within 2.2% for s ≤ 3. Mean rates s = 1 → 4: 1.67
  (a_S), 2.38 (a_B), 2.03 (H_1) per coarse ℓ^∞ unit; the local rates oscillate with the cell geometry. Weighted row sums of
  a_S in coarse ℓ¹ distance (T = 10): N_0 = 2.87, N_{0.5} = 18.9, N_{1.0} = 5216 (dominated by the far shells), so the ℓ¹ rate
  is between 0.5 and ≈ 1, consistent with the located rate 0.98-1.04 (LINEAR_PACKAGE §4).
- **B (informational).** κ = 0.25: a_B rates 1.07, 2.76, 1.24, 2.08; H_1 1.93, 1.99, 1.69, 0.91 (located 0.50; the last shell is
  the antipodal one at T = 8). κ = 4: a_B 1.20, 3.28, 1.73, 2.58; H_1 1.87, 2.59, 2.54, 2.44 (located 2.46).
- *Reading (measured only).* At the trivial background the level-1 branch tangent and ∂²E_1^br decay exponentially and
  torus-stably, at O(1) rates per level-1 unit; Theorem BB-3_1's proven rate Lμ_1 ≈ 1.4·10⁻¹⁰ per level-1 unit is ≈ 10¹⁰
  below. **[RBB1-fix B-bb1-2 + B1-1]** The rates 1.7-2.4 are per coarse ℓ^∞ shell; in BFT's ℓ¹ distance the weighted sums
  (N_{0.5} = 18.9, N_{1.0} = 5216 at T = 10) place the measured rate at **≈ 0.5-1 per level-1 ℓ¹ unit**; the proven rate is
  **Lμ_1 ≈ 7.2·10⁻¹¹** (not 1.4·10⁻¹⁰): the gap is ≈ 10¹⁰. (A3's thresholds were met with margin only at r_3(a_S) = 0.945.) n = 3, 4 are not measured here: c38's cubic kernel lives on T ≤ 5, where shells stop at 2 (c38 D), too short to
  read a rate. Non-trivial backgrounds are not measured.

---

## 4. Outcome (written after §2-§3)

| Item | Status | Note |
|---|---|---|
| Lemma BB-geo | PROVEN-HERE | trees; ½𝔱 ≤ 𝔱_S ≤ 𝔱 |
| Lemma BB-C | PROVEN-HERE | first-order decay on a polydisc ⇒ n-th order, rate μ/n (max-distance form) |
| Lemma BB-IFT | PROVEN-HERE | n = 1 from a weighted inverse |
| Lemma BB-MCT | PROVEN-HERE (solid norms) | scale sum Σ L^{-(k-j)} converges; **B3-F3 OCCURS**: no uniform G in solid norms; (H-op) OPEN in the Hölder/divergence pair |
| Lemma BB-NL | PROVEN-HERE (as a toy) | [RBB1-fix B-NL-1] the analytic content of BFT-2 ⇏ BFT-3 (BFT-0/1/2 with m > 0 do give it) |
| **Theorem BB-3_1** | **PROVEN-HERE** | **BFT-3 at k = 1, all n, every curvature-small real V and its complex nbhd; U_0, gauge-invariant outputs, E_1^br; rate Lμ_1/n per level-1 unit** [RBB1-fix B1-1..4: Lμ_1 ≈ 7.2·10⁻¹¹; tori T ≥ T_0 only] |
| Proposition BB-E1 | PROVEN-HERE | E-part of BFT-3 is one-step (ENV) |
| Proposition BB-3_k | PROVEN as an implication | BFT-3 (n ≤ 4) ⇐ BFT-0/2 + (H-𝔊_w); (H-𝔊_w) = uniform weighted bounds on Ξ_{j←k} = ζ_j⋯ζ_{k-1} ⇐ (LEG_w) [ARGUED] + (LOC-ζ) + BFT-1 (θ_w > 0) |
| B3-F1 | OCCURS for the absolute estimate | [RBB1-fix B3F1-1] bound ≈ Π_iN_0(|ζ_i|), N_0(|ζ_0|) = 2.85 |
| B3-F2 | [RBB1-fix B3F2-1] NOT ESTABLISHED | residual-carrying soft cubic vertex + CEN2: geometric level sum; k-uniform constant ⇐ BFT-1/2 |
| FLOW's need (V = 1, n ≤ 4) | n = 1 (gauge-inv.), n = 2: PROVEN (ledger); n = 1 potentials ⇐ (LEG_w); n = 3, 4 k-uniform: [RBB1-fix B3F2-1] constant ⇐ BFT-1/2 (Cauchy via BB-E1), decay ⇐ (H-𝔊_w); k = 1: PROVEN |
| Construction BB-loc (k = 1) | PROVEN-HERE ((a)-(d)) | exact gauge-invariant polymer decomposition E_1^br = S_W + R_1, *-connected polymers on X^+ |
| BB-mix ⇒ ||R||_𝒜 bound | PROVEN as an implication | needs per-cube smallness K < e^{-m_0}/(80e) beyond compact clusters (corrected 05:09) |
| BB-mix-gap | (1) PROVEN-HERE; (2) [RBB1-fix B-mix-3] ARGUED (route NO-GO) | n ≤ 4 locality cannot give BFT-4; the mass-interpolation Cauchy route loses the condition number S/γ against the required radius 218e^{m_0} |
| (BB-mix) | OPEN | routes R1 (s-weakened A = C_0(s)N(A); pitfall proved; nonlinear chain coupling remains), R2 (vertex p! loss) |
| Lemma BB-env | PROVEN-HERE | linearised classical step = pull-back along the branch; 2nd order = one-step covariance |
| Proposition BB-4-ind | PROVEN as an implication (algebra) | [RBB1-fix B4i-1..3] per-level architecture, outside BFT's anti-circularity clause; closing condition scale-invariant (near-vacuous); strengthening needs Σ|κ_{k+1} - κ_k| < ∞ |
| B4-F1 | (O3) FAILS in ||·||_𝒜 [power count + Schwarz; inference] | λ ≥ 1 at quadratic order; needs Loc-extraction + a smoothness-sensitive norm |
| Corollary BB-4c | PROVEN as an implication [RBB1-fix B4c-1/2: X^+; AX-Taylor + large-|X| Cauchy] | BFT-4 ⇒ C_♭ uniform, ∇R(1) = 0, (H-G) uniform with near/far, BFT-3 E-part all n, (I_i) uniform, no θ-cascade; NAH-unif′ ⇐ (H-K) + BFT-2 + BFT-4 |
| bb1 | A1 PASS, A2 FAIL (c37 Z_col float32 artefact found), A3 PASS, B informational | |

**What BFT-3 and BFT-4 now rest on.**
- BFT-3: at k = 1, nothing beyond the ledger (Theorem BB-3_1). At general k: BFT-0/2 + (H-𝔊_w)_k (Proposition BB-3_k), with
  (H-𝔊_w) ⇐ (LEG_w) [ARGUED; PROVEN for gauge-invariant outputs by LINEAR_PACKAGE 4.2'/6.7] + (LOC-ζ)_i at every level (⇐ BFT-4
  at level i via Corollary BB-4c (v)) + BFT-1 with θ_w > 0. The E-part for n ≥ 3 is BFT-4 content (B3-F2; Corollary BB-4c (iv)).
- BFT-4: the decomposition exists and is exact, gauge-invariant and polymer-shaped (BB-loc, k = 1). The bound needs (BB-mix)
  (per-cube smallness of the Möbius differences, beyond compact clusters) — OPEN — and its level-uniformity needs the per-level induction
  BB-4-ind in a norm stronger than ||·||_𝒜 (B4-F1), with a Loc-extraction of the marginal coefficient (fixed at tree level:
  FLOW F-tree, c38 C).
- Logical order that avoids circularity: BFT-4_{i} ⇒ (I_i) uniform (BB-4c (v)) ⇒ (LOC-ζ)_i and one-step locality at level i
  (BB-3_1's proof at level i) ⇒ BFT-3 for E_{i+1} and the inputs of BB-loc/BB-mix at level i + 1 ⇒ BFT-4_{i+1} (BB-4-ind). Each
  arrow is one-step; no composite covariance is used as a Newton inverse.
- **[RBB1-fix, corrections to the three bullets above (binding; REVIEW_BFT_B_S1)]** (1) BFT-3 at general k: (H-𝔊_w)_k is
  lane A's (H-lin^∇)_m + (H-rem^∇)_m in the (C-glob) centring (B4-1/B4-2); the (LEG_w)/(LOC-ζ) telescoping is the per-level
  alternative (B3k-2/3). "The E-part for n ≥ 3 is BFT-4 content" is withdrawn (B3F2-1): its k-uniform constant comes from
  BFT-1/2 by Cauchy via BB-E1, its decay from (H-𝔊_w). (2) BFT-4: the last clause ("per-level induction BB-4-ind") describes
  the per-level architecture, which BFT's anti-circularity clause excludes (B4i-1); the composite-route form is §5 (session
  2). (3) The "logical order" paragraph is the per-level (Balaban-type) order; its first arrow uses per-level covariances as
  Newton inverses, so "no composite covariance is used as a Newton inverse" is true but is not BFT's clause, which asks for
  one composite contraction (B4i-1).

## FOR OTHER FILES (for their owners; not edited)
- **PROOF.md [S21] (H-C) bullet and c37 record (l.6102, l.6122):** c37 D2's Z_col = 156.08 is a float32 accumulation artefact;
  the value is 156.6868 (bb1 diag), Z_colZ_row² = 1271.7. No conclusion changes.
- **PROOF.md (BG-unif) (iii)/(iv) and REVIEW_S22 Part 5:** BFT-3 does not follow from BFT-0/1/2 (Lemma BB-NL); it needs the
  weighted inverse (H-𝔊_w). BFT-3's E-part at n ≥ 3 with a k-uniform constant is a consequence of BFT-4 (B3-F2, BB-4c (iv)),
  so the dependency is BFT-4 ⇒ BFT-3(E), not the converse; BFT-3 at n ≤ 4 cannot produce BFT-4 (BB-mix-gap).
- **BFT_A (lane A):** Proposition BB-3_k consumes (H-lin^∇) **with exponential weights e^{±md}** (BFT's 𝔐 includes them);
  in its unweighted form it does not give locality (BB-NL), and BB-MCT's commutator step is automatic only in solid norms
  (B3-F3). BFT-A's 𝒞_glob domain suffices for BB-C (a fixed-radius complex ball about each point).
- **SF.md (L-loc)_k:** BB-loc gives the gauge-invariant localisation at k = 1 exactly; the missing bound is (BB-mix), which
  is the precise form of "(L-loc) would follow from mixed-derivative decay … for ALL mixed derivatives" — with the addition
  that per-cube smallness (not only decay) is required (BB-mix ⇒ bound).
- **FLOW.md (SF-bg):** at k = 1 derivatives of every order are exponentially local at every curvature-small background
  (Theorem BB-3_1); for general k at V = 1, n = 3, 4 the k-uniform constant is ⊂ BFT-4 (B3-F2).
- **RLARGE.md (BG)_k:** the locality radius R_bg at level 1 is now a theorem (BB-3_1 (i), rate μ_1); for general k it is
  BB-3_k's (H-𝔊_w).
- **[RBB1-fix] corrections to FOR OTHER FILES.** PROOF (BG-unif)/REVIEW_S22 bullet: "BFT-3 does not follow from BFT-0/1/2" →
  "does not follow from BFT-0/1/2 proven in unweighted norms; it follows from them proven with m > 0" (B-NL-1); "BFT-4 ⇒
  BFT-3(E), not the converse" is withdrawn (B3F2-1). FLOW (SF-bg) bullet: "⊂ BFT-4 (B3-F2)" → "constant ⇐ BFT-1/2, decay ⇐
  (H-𝔊_w)". BFT_A bullet: (H-𝔊_w) *is* (H-lin^∇)_m + (H-rem^∇)_m, and (LEG_w) is lane A's configuration-level data-map row at
  m > 0 (B4-1/B4-2). RLARGE bullet: the rate is μ_1 ≈ 2.4·10⁻¹¹ level-0 units (B1-1).

---

# Session 2 (2026-10-28 UTC)

## 5. PRE-STATED (session 2) — statements only; written after Step 1's fixes (05:45:38 UTC) and before any session-2 proof, criteria file or script. Proofs follow in §6, later.

### 5.0 Setting and norms (definitions)
- Level-k fields on 𝒞_glob (lane A §1.2): V = e^B, B a level-k su(N)-valued link field in one global gauge, chart = left-
  trivialised log; at V^r = 1 the chart derivative ∂/∂z_y is ∂/∂B_y. 𝒫_ρ := {B ∈ (su(N)⊗C)^{links} : max_b|B_b| ≤ ρ}.
- For F holomorphic on 𝒫_ρ with F(0) = 0: Taylor kernels K_n^F(b_1, …, b_n) := ∂^nF/∂B_{b_1}⋯∂B_{b_n}(0) (symmetric; colour
  indices suppressed); F^{(n)}(B) := (1/n!)ΣK_n^F B⋯B. m_b := the midpoint of link b.
- **(SF-∞)_B (named hypothesis, as FLOW §4 (SF-∞)).** The kernels K_n^{E_k}, n ≤ 5, are torus-independent for T ≥ T_0 (an
  infinite-volume translation-covariant family on Z⁴); torus wrap terms are O(e^{-mT/2}) and are not tracked.
- Centred symbol: Ṽ_n^F(p_2, …, p_n) := Σ_{b_2,…,b_n}K_n^F(b_1; b_2, …, b_n)e^{-iΣ_{i≥2}p_i·(m_{b_i} - m_{b_1})} (b_1 fixed;
  p_1 := -Σ_{i≥2}p_i). Its degree-j Taylor part at p = 0 has **dimension n + j** (n fields, j derivatives).
- Norm: M_n^{(m)}(F) := sup_{b_1}Σ_{b_2…b_n}|K_n^F(b_1; …)|e^{m·max_i|m_{b_i} - m_{b_1}|}; G_∇(F; ρ) := sup_{B∈𝒫_ρ, b}|∂F/∂B_b(B)|;
  **𝒩_{m,ρ}(F) := Σ_{n=2}^5M_n^{(m)}(F) + G_∇(F; ρ)**; the Loc condition is **β[F] = 0** (β of L4a-Π / FLOW §3: the
  transverse mixed second moment of the Hessian kernel; β[S_W] = 1).
- Smooth test fields: A a C^6 su(N)-valued 1-form on R⁴ supported in {|x| ≤ R_A}, |∂^αA| ≤ a for |α| ≤ 6;
  f_{A,ℓ}(b) := ℓ^{-1}A_μ(m_b/ℓ) for b = (x, μ), ℓ ≥ 1.

### 5.1 BFT-4 in the marginal-extracted form (STEP 2)
- **Lemma BB-W (dimension lemma: gauge invariance + B_4 + β = 0 ⇒ no part of dimension ≤ 5).** Let F be holomorphic on
  𝒫_ρ, F(0) = 0, invariant under level-k lattice gauge transformations near 1, under level-k translations and under the
  hypercubic group B_4 (in particular total inversion), with M_n^{(m)}(F) < ∞ (n ≤ 5) for some m > 0, kernels as in (SF-∞)_B.
  If β[F] = 0, then for 2 ≤ n ≤ 5 every Taylor part of Ṽ_n^F at 0 of dimension ≤ 5 vanishes, i.e. the moments
  Σ_{b_2…b_n}K_n^F(b_1; …)Π_i(m_{b_i} - m_{b_1})^{α_i} vanish for Σ|α_i| ≤ 5 - n; and |Ṽ_n^F(p)| ≤ M_n^{(m)}(F)(|p|_∞/m')^{6-n} for
  real p, |p|_∞ < m' < m. Without β = 0, the same holds for F - β[F]S_W. *Planned: PROVEN-HERE* (L4a-Π for n = 2; the lattice
  Ward identity order by order for n = 3, 4, 5 with an algebraic transversality lemma; total inversion for odd dimension).
- **Lemma BB-sm (irrelevance on smooth fields).** Under the hypotheses of BB-W with β[F] = 0, for every smooth test field
  with a ≤ ρℓ/2: **|F(f_{A,ℓ})| ≤ C_sm(a, R_A, m, ρ)·𝒩_{m,ρ}(F)·ℓ^{-2}**, C_sm explicit (polynomial in a, R_A, 1/m, 1/ρ).
  *Planned: PROVEN-HERE* (vanishing moments + Taylor for n = 2…5; Cauchy in one complex variable for n ≥ 6).
- **Theorem BB-4♮ (BFT-4 with the marginal F² coefficient extracted; one composite contraction, no per-level route).**
  Hypotheses, each a statement about the depth-k composite problem at fixed k with constants uniform in k:
  (I1) Theorem BA's conclusion (BFT-0/1/2 on 𝒞_glob, holomorphic on the complex ball, BA-10) ⇐ lane A's (H-lin^∇)_m +
  (H-rem^∇)_m + (FP♯'), with ρ := ε_0 **[RBB2-fix B4N-1: 𝒫_{ε_0} is not inside BFT-2's domain (|Im B| = ε_0 occurs in
  𝒫_{ε_0}, while BFT-2 allows imaginary parts ≤ r_ℂε_0 with r_ℂ ≤ 1). Read ρ := r_ℂε_0/2 (then 𝒫_ρ ⊂ {e^ze^{B^r} : |B^r| ≤
  ε_0, |z| ≤ r_ℂε_0}: put B^r := Re B and z := log(e^Be^{-Re B}) = i Im B - ½[i Im B, Re B] + O(ρ³) (BCH), so
  |z| ≤ ρ(1 + Cρ) ≤ r_ℂε_0 for ε_0 small), or name BA-10's
  complex data ball 𝒫_{ε_0} explicitly as part of (I1). Only C_sm and C_♮ change (through ρ)]**; (I2) BB-3_k at V = 1 for
  the E-part up to n = 5 (decay rate m' > 0, constant C'), ⇐ (H-𝔊_w) = (I1)'s weighted estimate, BB-E1 and BB-C
  **[RBB2-fix B4N-r1: BB-3_k was stated for n ≤ 4; the E-part for n = 5 is BB-C's pair version applied to the Hessian pair
  decay on the polydisc, which gives every n ≥ 2]**; (I3) (SF-∞)_B; (I4) BA-9's identification (E_k^br := E_k^{cb},
  Balaban convention). Put **c_k := β[E_k^br]** and **R_k := E_k^br - c_kS_W**. Then:
  (a) **c_k = 1 for every k** (FLOW Lemma F-tree, with E_k^br's Hessian at 1 = the chain form H_k), and in any case
      |c_k| ≤ C·M_2^{(m')}(E_k^br);
  (b) **β[R_k] = 0 and sup_k𝒩_{m'/2,ρ}(R_k) ≤ C_♮ < ∞**, C_♮ a function of the constants in (I1)-(I2) only;
  (c) **(irrelevance, dimension ≥ 6)** |R_k(f_{A,ℓ})| ≤ C_smC_♮ℓ^{-2} uniformly in k, for every smooth test field with
      a ≤ ρℓ/2; and R_k's Taylor kernels of orders 2-5 have no part of dimension ≤ 5 (BB-W).
  *Planned: PROVEN as an implication.* The flow of c_k (here = 1 at tree level) is FLOW's business; BFT-4 needs only (b).
- **Check bb2 (k = 1, the quadratic part of (a)-(c) at the trivial background).** Criteria in checks/bb2_criteria.md before
  the script: β(t) := e^†H_1(tn)e/e^†H_W(tn)e → 1 and ||H_1(tn) - H_W(tn)|| = O(t⁴) (H_W := d1^†d1, the coarse Wilson symbol).

### 5.2 (BB-mix)_1 at k = 1 (STEP 3)
- **Proposition BB-mix-wall (BB-loc's Möbius activities).** For BB-loc's pinned Möbius activities, the propagation
  mechanism gives at best K ≈ Ce^{-μ_1M_c/2^d} [inference], and a proof needs an all-order *product-of-influences* bound
  for the |X|-fold pinning differences, named **(BB-prod)_1**: |Δ_{Q_1}⋯Δ_{Q_n}ρ_x| ≤ C^nn!Π_ie^{-μd(x,Q_i)}. *Planned: the
  wall named exactly; not proven.*
- **Construction BB-bond (bond-weighted walk family, k = 1).** Cubes of side M_c level-1 blocks, each partitioned into RW
  boxes of sides in [R, 2R), R + 2 ≤ M_c; bonds 𝔅 := pairs of *-adjacent cubes; s ∈ C^𝔅 (s_{QQ} := 1). Cube-pair weights on
  every inter-cube transfer of Theorem RW's walk expansion (P(s), R(s), K^{-1}(s) := P(s)(1 - R(s))^{-1}); the
  nonlinearity with arguments S_QA := Σ_{Q'}s_{QQ'}1_{Q'}A; Φ_s(A) := -K^{-1}(s)Π[g + ℛ^s(A)]; A(s) its fixed point;
  ΔE(s) := Σ_Dρ_D(S_{Q(D)}A(s); V) (densities minus their value at U^(0)(V), owner cube Q(D)).
- **Theorem BB-mix′_1 (per-cube smallness at k = 1 from bond analyticity).** For s̄ ≥ 2, R := R_* + ⌈(2/(aL))log(2s̄)⌉,
  M_c ≥ R + 2, T ≥ 4R + 6 a multiple of M_c, and ε ≤ ε_mix(s̄) (explicit in §6: BR1's thresholds at box size R, and
  ε ≤ 1/(24s̄⁴(𝔠_♮p_Π)²C_♭), ε ≤ r_♭/(24s̄²𝔠_♮p_Π)), for every real level-1 V with ε_V ≤ ε and its complex neighbourhood
  |z_c| ≤ α_*/8: (i) A(s) exists, is unique in the r_s-ball and holomorphic in (s, z) on |s_b| ≤ s̄; A(1) = A*(V);
  (ii) E_1^br = E_∅ + Σ_XR(X) exactly, with R(X) gauge invariant, a function of V|_{X^+}, zero unless X is *-connected;
  (iii) **|R(X)| ≤ C_RK^{|X|-1}, K := 2^{41}/(s̄ - 1)**, C_R explicit. Hence, for s̄ - 1 ≥ 2^{42}·80e·e^{m_0}, **||R||_𝒜 ≤
  2e^{m_0}C_R**, and with E_∅ = L^{d-2}S_W this is BFT-4's bound at k = 1. *Planned: PROVEN-HERE (given the ledger theorems
  N5-sf0 (b) at box size R, Theorem RW, N5-an♭, BR1, U0).* The polymers are not BB-loc's.
  **[RBB2-fix C2-3: the complex domain is |z_c| ≤ ϱ_mix := ε_mix(s̄)/16 (not α_*/8) and the real data obey ε_V ≤
  ε_mix(s̄)/2 (BR1 (v)'s hypothesis ε_V ≤ ε_br/4 was not carried by ε_mix, and its radius α_*/8 is unsupported; D.4).
  Reason for ε_mix/16 rather than REVIEW_BFT_B_S2's literal ε_br(R)/16: Step 2's contraction uses ||g||_∞ ≤ 6ε with ε ≤
  ε_mix, so the *complex* curvature of U^(0)(V) must be ≤ ε_mix (the reviewer's own parenthesis, "any fixed radius with
  complex curvature ≤ ε_mix"); with complex curvature ≤ (1 + c_B(ε_V + 4ϱ))(ε_V + 4ϱ) (BCH; Ad by real links preserves
  HS norms) and U0 (iv)'s gradient bound continued to complex V with a factor c_ℂ ≤ 1.1 (§9, Lemma U0-ℂ), ε_V ≤ ε_mix/2 and
  ϱ ≤ ε_mix/16 give 6c_ℂ(complex curvature) ≤ 6ε_mix. Since ε_mix ≤ ε_br(R) this radius is ≤ the reviewer's, and still
  ε-independent. BFT-2's polydisc |z| ≤ r_ℂε lies inside it for ε ≤ ε_mix/2 and r_ℂ ≤ 1/8 (BFT's r_ℂ ∈ (0, 1] is a free
  choice; per coordinate divide by (N² - 1)^{1/2} as in §2.2), so BFT-4 at k = 1 is unaffected.]** **[RBB2-fix C2-4: "C_R explicit" reads "C_R
  explicit in terms of N_Q, s̄, r_s and the density-analyticity constant c_ρ (Lemma N5-an♭-dens, §9; not computed)".]**
  **[RBB2-fix C2-2: status reads "PROVEN-HERE given Lemma N5-an♭-dens (routine; stated in §9, proved in §10)".]**
- **Proposition BB-mix-k (the wall at k ≥ 2).** Construction BB-bond at depth k on the composite route needs (W1) a
  walk/localised expansion of lane A's composite inverse 𝓛^{-1} with per-step factor ≪ 1/s̄ uniformly in k, named
  **(H-RW^∇)_k**, and (W2) cube weights compatible with 𝔐^∇ (sharp weights S_Q create cube-boundary jumps whose ∇^c and
  Hölder seminorms are not controlled; smooth weights need lane A's (COMM)-type commutator bounds). *Planned: ARGUED (wall
  named).*

## 6. Proofs (session 2; appended after §5 (05:49:21 UTC) and after bb2 ran (05:51:32-05:51:34 UTC))

### 6.1 Lemma BB-W: PROVEN-HERE
*Analyticity.* With |·| the ℓ¹ length and |Im p|_∞ ≤ η for every slot, |e^{-iΣp_i·Δ_i}| ≤ e^{ηΣ_i|Δ_i|} ≤ e^{(n-1)η max_i|Δ_i|}
(Δ_i := m_{b_i} - m_{b_1}), so Ṽ_n^F is holomorphic and bounded by M_n^{(m)}(F) on the polystrip |Im p_i|_∞ < m/(n - 1).
Translation invariance makes Ṽ_n independent of the base point of b_1 (it depends on b_1's direction and colour index only).
*Step 0.* F(0) = 0 and ∇F(0) = 0 (constant gauges fix 0 and act on the gradient by Ad; su(N) has no non-zero Ad-invariant
vector — FLOW Lemma F-Π (i)), so K_1 = 0.
*Step 1 (n = 2).* The Hessian kernel satisfies L4a-Π's hypotheses: (S) symmetry of a Hessian; (H) B_4 covariance; (G)
transversality (Hessian at 0 of a gauge-invariant functional); Σe^{δ|z|}|Π| < ∞ with δ = m; colour scalar by Ad-invariance.
L4a-Π's Π̃ is exactly the centred Ṽ_2 (Fourier transform in the difference of bond midpoints). Its claim: Π̃ = β(δs² - ss^T)
+ R, R = O(|p|⁴). With β[F] = 0, Ṽ_2 = O(|p|⁴): the parts of dimension 2, 3, 4, 5 vanish.
*Step 2 (parity).* Total inversion I about the midpoint c of b_1 maps a positively oriented link b to the positively
oriented link I(b) with midpoint 2c - m_b and the same axis, and the link variable to its inverse; since log(V^{-1}) = -log V
exactly, it acts linearly in the chart: (I*B)_b = -B_{I(b)}. Inversion about a link midpoint is a B_4 element composed with
a translation, so F∘I* = F and K_n(b_1, …, b_n) = (-1)^nK_n(Ib_1, …, Ib_n), Ib_1 = b_1. Relabelling b_i → Ib_i in the moment
μ_α := Σ_{b_2…b_n}K_n(b_1; …)Π_i(m_{b_i} - m_{b_1})^{α_i} gives μ_α = (-1)^{n+|α|}μ_α: **every part of odd dimension n + |α|
vanishes.**
*Step 3 (Ward identity).* For finitely supported λ: site → su(N), (g_t·B)_b := log(e^{tλ_x}e^{B_b}e^{-tλ_{x+μ}}) (b = (x, μ)) is
holomorphic near (t, B) = (0, 0), and F(g_t·B) = F(B). Differentiating at t = 0: Σ_b∂F/∂B_b(B)·δ_λB_b(B) = 0 with
δ_λB_b(B) = Σ_{r≥0}δ^{(r)}_b(B, λ), δ^{(r)}_b homogeneous of degree r in B_b (the same link only), linear in (λ_x, λ_{x+μ}), and
δ^{(0)}_b = λ_x - λ_{x+μ} = -(dλ)_b. The coefficient of B^{n-1}λ (n ≥ 3; K_1 = 0) is
  (★) (1/(n-1)!)Σ_bK_n[B^{n-1}, b](-dλ)_b + Σ_{m=2}^{n-1}(1/(m-1)!)Σ_bK_m[B^{m-1}, b]·δ^{(n-m)}_b(B, λ) = 0.
In Fourier variables on the hyperplane Σp = 0 (infinite volume by (SF-∞)_B; L4a-Π's phase bookkeeping: (dλ)^_ν =
is_ν(q)e^{iq_ν/2}λ̂, s_ν = 2sin(q_ν/2), and the midpoint phases are absorbed by centring) the first term is a non-zero
multiple of Σ_νs_ν(p_1)Ṽ_n^{ν…}(p), and the m-th term is Ṽ_m with one slot's momentum replaced by the sum of the momenta
of the n - m B's and λ merged at that link, times an analytic multiplier (from δ^{(n-m)}); substitution of sums of momenta is
linear, so its Taylor degree is ≥ that of Ṽ_m. **Induction on n:** assume Ṽ_m = O(|p|^{6-m}) for 2 ≤ m < n (true for m = 2,
Step 1). Then every m-term is O(|p|^{6-m}) ⊂ O(|p|^{7-n}), and for J ≤ 6 - n the degree-J part of (★) reads
  Σ_νp_{1,ν}Ṽ_n^{[J-1]ν…} - (1/24)Σ_νp_{1,ν}³Ṽ_n^{[J-3]ν…} + … = 0    (s_ν(p) = p_ν - p_ν³/24 + …, odd).
By the symmetry of K_n the same holds with any slot in place of slot 1.
- J = 1 (all n ≤ 5): Σ_νp_{1,ν}Ṽ^{[0]ν…} = 0 for all p_1 ⇒ the constant tensor Ṽ^{[0]} = 0 (take p_1 = e_ν). [dimension n]
- J = 2 (n ≤ 4): every slot is transverse at degree 1. **Algebraic lemma (A1):** a tensor V(p) linear in (p_1, …, p_n),
  Σp_i = 0, n ≥ 3, transverse in slots 1 and 2 vanishes. *Proof.* Eliminate p_1: V = Σ_{i≥2}p_{i,α}Y_i^{α ν_1 …}.
  Transversality in slot 1, -Σ_{i'}p_{i',ν_1}Σ_ip_{i,α}Y_i^{αν_1…} = 0 for independent p_2, …, p_n: the p_{i,α}p_{i,β} terms give
  Y_i antisymmetric in (α, ν_1); the p_{i,α}p_{i',β} terms (i ≠ i', available since n - 1 ≥ 2) give Y_i^{αβ} = -Y_{i'}^{βα} =
  Y_{i'}^{αβ}. So V = -p_{1,α}Y^{αν_1…}. Likewise (eliminating p_2) V = -p_{2,α}Z^{αν_2…}. For n ≥ 3, p_1 and p_2 are
  independent; setting p_2 = 0 gives p_{1,α}Y^{α…} = 0 for all p_1, so Y = 0 and V = 0. ∎ Hence Ṽ_n^{[1]} = 0 for n = 3, 4.
  [dimension n + 1]
- Parity (Step 2) removes Ṽ_3^{[2]} (dim 5), Ṽ_4^{[1]} (dim 5), Ṽ_5^{[0]} (dim 5).
So Ṽ_3 = O(|p|³), Ṽ_4 = O(|p|²), Ṽ_5 = O(|p|): **all parts of dimension ≤ 5 vanish for 2 ≤ n ≤ 5**, which closes the
induction and is the moment statement (vanishing Taylor coefficients ⇔ vanishing centred moments). *The bound.* For real p
with |p|_∞ = τ, ζ ↦ Ṽ_n(ζp/τ) is holomorphic on |ζ| < m/(n - 1), bounded by M_n^{(m)}, and vanishes to order 6 - n at 0;
Schwarz's lemma gives **|Ṽ_n(p)| ≤ M_n^{(m)}(F)(|p|_∞/m')^{6-n} for |p|_∞ < m' < m/(n - 1)** [post-proof correction of the
pre-stated range: m' < m/(n - 1), not m' < m]. *Last clause:* S_W is gauge invariant, B_4- and translation-invariant, of
finite range and entire in B, with β[S_W] = 1; so F - β[F]S_W satisfies the hypotheses with β = 0. ∎
*Reading.* The marginal (dimension-4) content of a gauge-invariant, B_4-invariant, exponentially local functional is one
number, β[F]: its quadratic part fixes the cubic and quartic dimension-4 parts through the Ward identity (here: they must
vanish when β = 0), and parity removes every odd dimension. This is the lattice form of "tr F² is the only dimension-4
invariant" (the θ-term is P-odd), with no continuum limit taken.

### 6.2 Lemma BB-sm: PROVEN-HERE
Let f := f_{A,ℓ} (assume R_A, ℓ ≥ 1). It is supported on links with |m_b| ≤ ℓR_A, at most N_s := 4(2ℓR_A + 2)⁴ ≤ 1024R_A⁴ℓ⁴
of them; ||f||_D ≤ a/ℓ ≤ ρ/2; and, as a function of the midpoint, |∂^αf_μ| ≤ aℓ^{-1-|α|} for |α| ≤ 6. F(f) = Σ_{n≥2}F^{(n)}(f)
(F(0) = 0, K_1 = 0; convergence below).
*Orders 2 ≤ n ≤ 5.* F^{(n)}(f) = (1/n!)Σ_{b_1}f(b_1)Σ_{b_2…b_n}K_n(b_1; …)g(m_{b_2}, …, m_{b_n}), g(y_2, …, y_n) := Π_{i≥2}f_{μ_i}(y_i);
only b_1 ∈ supp f contribute. Taylor-expand g about (m_{b_1}, …, m_{b_1}) to total order 5 - n. The polynomial part is killed
by BB-W's vanishing moments. The remainder is ≤ (Σ_i|Δ_i|)^{6-n}/(6 - n)!·max_{|α|=6-n}sup|∂^αg|, and since each variable y_i
belongs to one factor, ∂^αg = Π_i∂^{α_i}f_{μ_i}(y_i) ≤ a^{n-1}ℓ^{-(n-1)-(6-n)}. With (Σ_i|Δ_i|)^{6-n} ≤ (n - 1)^{6-n}max_i|Δ_i|^{6-n}
and x^je^{-mx} ≤ (j/(em))^j:
  |F^{(n)}(f)| ≤ c_na^nR_A⁴m^{-(6-n)}M_n^{(m)}(F)·ℓ^{-2},  c_n := 1024(n - 1)^{6-n}((6 - n)/e)^{6-n}/(n!(6 - n)!).
*Orders n ≥ 6.* w ↦ F(wf) is holomorphic for |w| < W := ρ/||f||_D (≥ 2), and F(wf) = ∫_0^1Σ_{b∈supp f}∂F/∂B_b(twf)wf(b)dt, so
|F(wf)| ≤ G_∇ρN_s on |w| = W(1 - δ), δ ↓ 0. Cauchy: |F^{(n)}(f)| ≤ G_∇ρN_sW^{-n}, and Σ_{n≥6} ≤ 2G_∇ρN_s(||f||_D/ρ)⁶ ≤
2048G_∇ρ^{-5}a⁶R_A⁴ℓ^{-2}. (The same Cauchy bound gives absolute convergence of the Taylor series at w = 1.) Summing,
  **|F(f_{A,ℓ})| ≤ C_sm𝒩_{m,ρ}(F)ℓ^{-2}, C_sm := R_A⁴·max{max_{2≤n≤5}c_na^nm^{-(6-n)}, 2048a⁶ρ^{-5}}.** ∎
*Reading.* "Dimension ≥ 6" is a theorem about F, not a choice of norm: n ≥ 6 fields cost ℓ^{-n}·ℓ⁴ automatically, and the
orders 2-5 cost ℓ^{-2} exactly because their dimension ≤ 5 parts vanish (BB-W). For S_W itself the same computation gives
O(1) (β = 1), the marginal term.

### 6.3 Theorem BB-4♮: PROVEN as an implication
*(a).* By (I4) and (I1), E_k^br(V) = 𝔉_k(Z(V); V) with Z(V) critical in every direction (NA-crit'), so the envelope theorem at
the nondegenerate trivial chain gives Hess E_k^br(0) = the Schur complement of Hess 𝔉_k(trivial chain) in the internal
variables, i.e. the linearised chain form H_k of LINEAR_PACKAGE Setting SC (FLOW Def F-strip states this for 𝒯_k; 𝔉_k with
φ̂ and FLOW's κk̃ have the same quadratic part at the trivial field (FLOW §3.1; lane A §1.1: "the same tree-level exponent")
— read, not re-derived here). Lemma F-tree: β[𝒯_k] = 1, i.e. β of H_k is 1. F-tree is stated for uniform κ; its induction
uses κ_k only through the term κ_k^{-1}P_⊥ of Ĝ_{k+1} = κ_k^{-1}P_⊥ + 𝒬(Ĝ_k), which is bounded and is killed by |ŝ(p)|² → 0
in (b), and through the K ≠ 0 alias terms, which are bounded by (a) — so it holds verbatim for κ_j ∈ [κ_-, κ_+] varying
with j [inference from reading FLOW l.251-267]. Hence **c_k = 1** (β[S_W] = β[𝒯_0] = 1). Independently of F-tree,
|c_k| = |Σ_zz_1z_2Π_12(z)| ≤ (2/(em'))²M_2^{(m')}(E_k^br) (L4a-Π's formula for β).
*(b).* β[R_k] = c_k - c_kβ[S_W] = 0. The moment norms: (I2) is BB-C's pair version before the tree conversion,
|K_n^{E_k}(b_1, …, b_n)| ≤ C'e^{-m' max_{i,j}d(b_i,b_j)} (2 ≤ n ≤ 5, at the real point V = 1, k-uniform: constant from BFT-1/2
by Cauchy, decay from (H-𝔊_w); B3F2-1), so with max_id(b_1, b_i) ≤ max_{i,j}d and e^{-(m'/2)max_i d} ≤ Π_{i≥2}e^{-(m'/(2(n-1)))d(b_1,b_i)},
  M_n^{(m'/2)}(E_k^br) ≤ C'e^{m'}(4coth⁴(m'/(4(n - 1))))^{n-1}   (BB-geo (c); midpoint vs link distance ≤ 1).
S_W has finite range, so M_n^{(m'/2)}(S_W) < ∞ explicitly. The gradient: by BB-E1 (ENV at the composite critical point, continued
analytically to complex B), ∇_yE_k^br(V) = -κ_{k-1}π(M̄_y(U_{k-1})V_y^{-1}); on 𝒫_ρ, (I1) with BA-3 gives |ρ_{k-1}| ≤ η + C_ρη² and
own-unit level-(k-1) link logs ≤ η (η := 2(1 + G_D)ρ), so |M̄_y(U_{k-1})V_y^{-1} - 1| ≤ C_Mη with C_M depending on (L, p_L)
(contour transports of p_L steps; NA-alg (a)-(b)) [sizes as in BA-3 and NA-alg; C_M not evaluated], and π is Lipschitz
near 1 (|π(W)| ≤ 4|W - 1| for |W - 1| ≤ ½). With the chart factor (1 + O(ρ)) (RBB1-fix B1-3): G_∇(E_k^br; ρ) ≤ 4κ_+C_Mη(1 + O(ρ)),
k-uniform; G_∇(S_W; ρ) ≤ 6 sup|∂s| < ∞. So **𝒩_{m'/2,ρ}(R_k) ≤ 𝒩(E_k^br) + |c_k|𝒩(S_W) =: C_♮**, a function of (C', m', G_D,
ρ, κ_+, L, N) only.
*(c).* R_k is holomorphic on 𝒫_ρ (E_k^br by (I1)/BA-10; S_W entire), R_k(0) = 0, gauge invariant (E_k^br by (I1)'s
identification; S_W), translation- and B_4-invariant (the composite problem is B_4-covariant: S4' family B_4-symmetric, blocks
centred, L odd; E_k^br does not depend on the fixing), with M_n^{(m'/2)} < ∞ and (SF-∞)_B. BB-W and BB-sm apply with F = R_k,
m = m'/2. ∎
*One contraction, no per-level route.* Every input is a property of the depth-k composite problem: Theorem BA (one Banach
contraction for 𝔉_k in 𝔐^∇, the composite 𝓛^{-1} as the only inverse), BB-3_k (IFT with the same inverse, then Cauchy),
BB-E1 (an identity at the composite critical point). No E_j^br with j < k is estimated, no per-level covariance is used as a
Newton inverse, and no induction in k is run; k enters only through the uniformity of (H-lin^∇)_m, (H-rem^∇)_m, (FP♯').
So B4-F1 (λ ≥ 1 in ||·||_𝒜) and B4i-2 (scale invariance of BB-4-ind's closing condition) do not arise: the marginal
coefficient is extracted (c_k = 1 at tree level, F-tree), not contracted.
*What it is.* **[RBB2-fix B4N-2: "in the right form" is withdrawn. Read: "a marginal-extracted Taylor-norm form of BFT-4
(necessary, and weaker than BFT-4: 𝒩 is a Taylor norm at V = 1 for n ≤ 5 plus one global gradient sup, and does not give
the sups of local pieces on polydiscs about non-trivial backgrounds that BFT-4's Cauchy consequences use); the polymer form
||·||_𝒜 remains BFT-4".]** The quantitative content of BFT-4 in the right form: E_k^br = c_kS_W + R_k with c_k = β[E_k^br] = 1 at tree level,
β[R_k] = 0, and R_k k-uniformly bounded in a norm in which it is irrelevant: no Taylor part of dimension ≤ 5, and
|R_k(f_{A,ℓ})| = O(ℓ^{-2}) on every smooth test field. *What it is not.* (1) Not a polymer representation (BFT-4's ||·||_𝒜):
that needs (BB-mix)_k (k = 1: §6.5; k ≥ 2: §6.6). (2) Only on 𝒞_glob (small data in one global gauge); generic
curvature-small backgrounds need lane A's (UHL), (SL-cov). (3) A Taylor norm at the trivial field plus an analytic sup on
𝒫_ρ; Hess-Lipschitz-type uses at non-trivial backgrounds (BB-4c (v)) are not re-derived from it. (4) The optional
strengthening (convergence of R_k in k) is not addressed. (5) Conditional on (I1)-(I4); (I1) is lane A's open estimate.
**[RBB2-fix B4N-r2]** It inherits lane A's (α, θ) window problem through (I1) and (I2) only (the plain level-l current rows
of (H-rem^∇) and the (Pl) slot of (H-lin^∇)); its own steps never use α, θ, θ_w or a Hölder component, so it transfers
unchanged to any repaired pair whose output norm dominates the sup of own-unit link logs and soft fluctuations and which
carries e^{±md} weights with m > 0 uniform in the centre; it does not survive a repair that reaches only m = 0.
(6) bb2 tests (a)-(c)'s quadratic part at k = 1 only, in the abelian fibre model.

### 6.4 Proposition BB-mix-wall: ARGUED (the wall for BB-loc's Möbius activities)
R(X) of BB-loc is the |X|-th mixed difference of Y ↦ ΔE(Y) in the pinning status of the cubes of X. Switching one cube's
pinning is an O(1) change of the field inside that cube, so no per-cube smallness can come from the switch itself; it can
come only from distance, i.e. from a bound **[RBB2-fix BMW-1: the previous sentence is narrowed. In absolute terms the
switch changes the fluctuation by ≤ r(ε) = 12𝔠_∞ε (small); it is O(1) only *relative to the fluctuation* (the pinned
and unpinned fluctuations in the cube are both O(ε) and differ by O(ε)). Small fields are exactly the source of smallness
§6.5 exploits through bond weights. What is meant: the hard pinning constraint has no known analytic interpolation of
radius ≫ 1 (the mass family has radius 1 + O(γ/S), BB-mix-gap (2)), so for BB-loc's Möbius polymers the only mechanism
identified is distance; read the rest of this paragraph with that qualification]** of the form **(BB-prod)_1: |Δ_{Q_1}⋯Δ_{Q_n}ρ_x| ≤ C^nn!Π_ie^{-μd(x,Q_i)}** for every
density ρ_x of the pinned problems. Given (BB-prod)_1 in this product form, Σ_id(x, Q_i) ≥ (n - 3^d)M_c from any x (at
most (2j + 1)^d cubes lie within distance jM_c of x), so K ≈ Ce^{-μM_c} beyond 81 cubes. What propagation (tree/walk)
expansions actually produce is a tree-type bound e^{-μ·(Steiner length)}, and the Steiner length through n cubes is only
≳ (n/2^d - 1)M_c, so the natural factor is K ≈ Ce^{-μM_c/2^d} (RBB1-fix B-mix-2) and M_c ≳ 2^d(m_0 + log(Cc_an))/μ_1 ≈ 10^{13}
level-0 spacings at μ_1 ≈ 2.4·10⁻¹¹ [inference]. (BB-prod)_1 is an
all-order statement: BB-3_1 controls V-derivatives, not pinning differences (BB-mix-gap (1)), and the mass-interpolation
Cauchy route fails (BB-mix-gap (2), a route NO-GO). It is not proven here. §6.5 replaces BB-loc's polymers by a
representation in which the needed smallness is proven.
**[Session-3 provenance note (RBB2-fix R-1).]** This paragraph was edited in place at ≈05:57 UTC on 2026-10-28 (session
2), after §6 was first appended at 05:56:20: the text from "Given (BB-prod)_1 in this product form" to "[inference]"
(the product-form count (n - 3^d)M_c versus the tree-type Steiner count (n/2^d - 1)M_c, which is what gives
K ≈ Ce^{-μM_c/2^d}) replaced an earlier wording of the same count. The edit is logged in BFT_B_LOG (session 2); the
earlier wording is not recoverable from the file.

### 6.5 Construction BB-bond and Theorem BB-mix′_1: PROVEN-HERE (k = 1)
*Setting at box size R.* Theorem N5-sf0's proof uses R only through the AX box side (4R + 5)L and T ≥ 4R + 6 (read: PROOF
l.5452-5467). So with ε_*(R) := α_*/(10p_L(4R + 5)L) and the class 𝔑_R(α_*) (gauges on Ω^+_□ for the R-partition), N5-sf0 (b)
holds with the same (γ', m, S'_m) and partition side R, and BR1 holds with ε_* → ε_*(R) in ε_br (=: ε_br(R)): the operator
C_0 = C(U^(0)(V), V) is the same, only its walk representation changes. RW-2: ε_R ≤ ½e^{-aL(R-R_*)/2}, so R := R_* +
⌈(2/(aL))log(2s̄)⌉ gives **s̄ε_R ≤ ¼**. Cubes: side M_c ≥ R + 2 level-1 blocks, T a multiple of M_c, each cube partitioned
into RW boxes of sides in [R, 2R) (a product partition refining the cube partition). 𝔅 := unordered pairs of *-adjacent cubes
(≤ 80 per cube); s ∈ C^𝔅, s_{QQ} := 1, s_{QQ'} := s_{{Q,Q'}}; 1_Q := projection on the level-0 links based in blocks of Q.
*Step 1 (the weighted walk operator).* With Theorem RW's G_□ := G_□(0), R_□ := R_□(0) for K := Õ(U^(0)(V), V):
  P(s) := Σ_□Σ_{Q'}s_{Q'Q(□)}1_{Q'}G_□1_□,  R(s) := Σ_□Σ_{Q'}s_{Q'Q(□)}1_{Q'}R_□,  K^{-1}(s) := P(s)Σ_{n≥0}R(s)^n.
Ranges: G_□1_□ has rows in Ω_□ (≤ R blocks from □) and R_□ rows within R + 1 blocks of □ (K has range ≤ 1 block), so
M_c ≥ R + 2 puts every row in Q(□) or a *-adjacent cube: every piece is either intra-cube (weight 1) or crosses one bond
(weight s_b). Bounds: entrywise |P(s)| ≤ s̄|P|, |R(s)| ≤ s̄Σ_□|R_□|; by (RW1) at t = 0, N_0(|P|) ≤ (2/γ')coth⁴(m/2) (each column
lies in one box; BB-geo (c)); by RW (i), N_0(|R(s)|) ≤ s̄ε_R ≤ ¼. Hence the series converges and
  **N_0(|K^{-1}(s)|) ≤ s̄𝔠_♮, 𝔠_♮ := 3coth⁴(m/2)/γ'**,
**[RBB2-fix C2-1: the column sum runs over links y, so N_0(|P|) ≤ (2/γ')·4coth⁴(m/2) = (8/γ')coth⁴(m/2) (PROOF l.5252;
RW's own proof has the same factor), and N_0(|K^{-1}(s)|) ≤ s̄N_0(|P|)/(1 - ¼) gives **𝔠_♮ := (32/3)coth⁴(m/2)/γ'**. Every
later 𝔠_♮ (𝔠_s, ε_mix, C_R) is read with this value; the thresholds keep their form.]**
K^{-1}(s) is holomorphic in (s, z) (polynomials in s, N5-sf0's analyticity in z, uniform convergence), and K^{-1}(1) = K^{-1}
(RW (i)). **Splitting (S1):** if the cubes are partitioned into classes and s_b = 0 for every bond between classes, then
K^{-1}(s)(x, y) = 0 for x, y in different classes (every term is a product of pieces; a chain of positions from y's class to
x's class contains a crossing piece of weight 0).
*Step 2 (the weighted fixed-point problem).* Π := Π_{U^(0)} (projection onto ker h; acts within blocks, so it commutes with
every 1_Q), p_Π := N_0(|Π|), g := ∇f_V(0) (||g||_∞ ≤ 6ε_V, Lemma U0 (iv)), ℛ(A) := ∇f_V(A) - g - Hess f_V(0)A,
S_QA := Σ_{Q'}s_{QQ'}1_{Q'}A, ℛ^s(A)(b) := ℛ(S_{Q(b)}A)(b), and
  Φ_s(A) := -K^{-1}(s)Π[g + ℛ^s(A)]  on ℓ^∞(level-0 links; su(N)⊗C).
Put 𝔠_s := max(s̄𝔠_♮p_Π, 𝔠_∞), r_s := 12𝔠_sε. For ||A||_∞, ||A'||_∞ ≤ r_s: ||S_QA||_∞ ≤ s̄r_s; if s̄r_s ≤ r_♭/2, N5-an♭ (in the
local AX gauge of each row, as in BR1) gives |ℛ^s(A)(b) - ℛ^s(A')(b)| ≤ C_♭s̄r_s·s̄||A - A'||_∞, so Lip(Φ_s) ≤ 𝔠_sC_♭s̄²r_s =
12𝔠_s²C_♭s̄²ε ≤ ½ and ||Φ_s(A)||_∞ ≤ 6𝔠_sε + r_s/2 = r_s provided
  **ε ≤ ε_mix(s̄) := min{ε_br(R), 1/(24𝔠_s²C_♭s̄²), r_♭/(24𝔠_ss̄)}**
[post-proof correction of the pre-stated explicit thresholds: 𝔠_s := max(s̄𝔠_♮p_Π, 𝔠_∞) replaces s̄𝔠_♮p_Π, so that r_s ≥ BR1's
r(ε); the form is unchanged]. Banach: a unique fixed point A(s) in the r_s-ball, holomorphic in (s, z) on |s_b| ≤ s̄ and BR1
(v)'s complex neighbourhood (uniform limit of holomorphic iterates). *At s ≡ 1:* S_Q = id and K^{-1}Π = C_0Π (C_0 =
K^{-1} - (1 - Π), (1 - Π)Π = 0); since C_0ΠO_0A = A on ker h (BR1's proof), BR1's map is A - C_0Π[∇f_V(A) + D_0P_0D_0^*A] =
-C_0Π[g + ℛ(A)] = Φ_1(A) on ker h; Φ_1 maps into ran(C_0Π) ⊂ ker h (Õ commutes with Π); BR1's A* lies in the r_s-ball
(r(ε) ≤ r_s) and is a fixed point of Φ_1, so **A(1) = A*(V)**. (i) is proven.
*Step 3 (splitting of the fixed point and of the energy).* Under the hypothesis of (S1), for A = ⊕_iA_i (A_i on the links of
class i): K^{-1}(s) and Π are block-diagonal over classes, g is data, and ℛ^s(A)(b) reads S_{Q(b)}A, which is supported in
the class of Q(b). So Φ_s = ⊕_iΦ_{s,i}, and A(s) = ⊕_iA_i(s) (the r_s-ball in sup norm is the product of the class balls).
Densities: F(U, V) = Σ_DD(U, V) over the level-0 plaquettes and the soft densities κ_0φ̂_c; Q(D) := the cube of the block of
D's base point; ρ_D(Ã) := D(e^{Ã}U^(0)(V), V) - D(U^(0)(V), V); ΔE(s) := Σ_Dρ_D(S_{Q(D)}A(s)). Then ΔE(1) = E_1^br - E_∅, and
under (S1)'s hypothesis ΔE(s) = Σ_iΔE_{C_i}(s), where for a cube set X, ΔE_X(s_X) := Σ_{Q(D)∈X}ρ_D(S_{Q(D)}A_X(s_X)) and A_X(s_X)
is the fixed point with all bonds leaving X set to 0 (it depends only on the bonds internal to X).
*Step 4 (cluster identity).* For a function holomorphic near [0, 1]^𝔅, iterating f(1) = f(0) + ∫_0^1f' over the bonds gives
ΔE(1) = Σ_{Γ⊂𝔅}∫_{[0,1]^Γ}∂^Γ_sΔE(s_Γ, 0_{𝔅∖Γ})ds_Γ. At s_{𝔅∖Γ} = 0 the classes are the connected components of the graph
(cubes, Γ), so ΔE = Σ_{components}ΔE_C; ∂^Γ annihilates every component term not depending on all bonds of Γ. Hence only
Γ = ∅ (giving Σ_QΔE_{{Q}}) and connected Γ survive, and
  **E_1^br = E_∅ + Σ_XR(X)**, R({Q}) := ΔE_{{Q}}, R(X) := Σ_{Γ connected, spanning X}∫_{[0,1]^Γ}∂^Γ_sΔE_X(s_Γ, 0)ds_Γ (|X| ≥ 2).
R(X) ≠ 0 only for X spanned by a connected Γ ⊂ 𝔅, i.e. *-connected X. *Gauge invariance:* for a level-1 gauge G,
U^(0)(GV) = ĜU^(0)(V) (U0 (iii)), K(GV) = R_ĜK(V)R_Ĝ^{-1} (N5-cov) with R_Ĝ block-diagonal, so the compressions, G_□, R_□ and
the cube projections are conjugated/commute and K^{-1}(s)(GV) = R_ĜK^{-1}(s)(V)R_Ĝ^{-1}; Π, g, ℛ are covariant (f_{GV}(R_ĜA) =
f_V(A)), S_Q commutes with R_Ĝ; by uniqueness A(s)(GV) = R_ĜA(s)(V); each ρ_D is invariant. So every ΔE_X(s), hence R(X), is
gauge invariant. *Support:* ΔE_X reads V through K's entries in pieces with an index within R + 1 blocks of X, through g, ℛ
(variables within 2 blocks of X's links) and the densities owned by X: **R(X) is a function of V|_{X^+}**. (ii) is proven.
*Step 5 (bounds).* Each density type is holomorphic on the polydisc of radius r_♭ in its local AX chart and bounded there
by some S_ρ (the proof of N5-an♭: finite compositions of entire functions and NA-alg's analytic X_0) [same proof as N5-an♭,
applied to the densities rather than to the gradient/Hessian entries; not separately reviewed]; Schwarz gives
|ρ_D(Ã)| ≤ c_ρ||Ã||_∞, c_ρ := 2S_ρn_1/r_♭, for ||Ã||_∞ ≤ r_♭/2 **[RBB2-fix C2-2: S_ρ and the density holomorphy are now
Lemma N5-an♭-dens (stated in §9, proved in §10); one-variable Schwarz along w ↦ ρ_D(wÃ) (|ρ_D| ≤ 2S_ρ, ρ_D(0) = 0) gives
the sharper c_ρ := 2S_ρ/r_♭, which is used from here on; n_1 is unnecessary]** **[RBB3-fix RS3-1: superseded by §10.5:
the constant is c_ρ = 4S_ρ/r_ρ with N5-an♭-dens's own radius r_ρ ≤ r_♭, and ε_mix(s̄) gains the two ε-independent thresholds
s̄r_s ≤ r_ρ/2 and 3(3L - 1)ε ≤ r_ρ/2; "2S_ρ/r_♭ used from here on" is withdrawn]**. With N_Q := the number of densities owned by a cube
(≤ 7(LM_c)⁴): sup_{|s|≤s̄}|ΔE_X(s)| ≤ |X|N_Qc_ρs̄r_s. Cauchy in the |Γ| distinct bond variables on polydiscs of radius s̄ - 1
about points of [0, 1]^Γ: |∂^Γ_sΔE_X| ≤ |X|N_Qc_ρs̄r_s(s̄ - 1)^{-|Γ|}. A connected Γ spanning X has |Γ| ≥ |X| - 1, and there are
≤ 2^{40|X|} subsets of the ≤ 40|X| bonds internal to X. With n := |X| ≤ 2^{n-1}:
  **|R(X)| ≤ C_RK^{|X|-1},  C_R := 2^{40}N_Qc_ρs̄r_s,  K := 2^{41}/(s̄ - 1)**
(also for |X| = 1). With c_an = 80e (session 1, confirmed by REVIEW_BFT_B_S1 D.3) and s̄ - 1 ≥ 2^{42}·80e·e^{m_0} (so
c_ane^{m_0}K ≤ ½): ||R||_𝒜 := sup_{Q_0}Σ_{X∋Q_0}sup|R(X)|e^{m_0|X|} ≤ C_Re^{m_0}Σ_{n≥1}2^{-(n-1)} = **2e^{m_0}C_R**. (iii) is proven.
With E_∅ = L^{d-2}S_W (BB-loc (d)): E_1^br = S_W + R_1, R_1 := (L^{d-2} - 1)S_W + Σ_XR(X), and the first term is a sum of
single-plaquette polymers bounded on the polydisc, so ||R_1||_𝒜 ≤ 2e^{m_0}C_R + 6(L^{d-2} - 1)M_c⁴e^{m_0}sup_𝒫|s| < ∞. ∎
*What it is.* **[RBB2-fix C2-3/C2-4: read "for each m_0 > 0, with ε_0 ≤ ε_mix(s̄(m_0))/2 (BFT's constants may depend on the
fixed choice m_0), on the complex neighbourhood |z_c| ≤ ϱ_mix = ε_mix(s̄)/16 of every real V with ε_V ≤ ε_mix/2" in place of
the next line's "every m_0 > 0, on BR1 (v)'s complex neighbourhood"; in Step 2 "BR1 (v)'s complex neighbourhood" reads the
same; the Banach argument is unchanged on the smaller domain.]** BFT-4's polymer bound at k = 1, every m_0 > 0, on BR1 (v)'s complex neighbourhood of every curvature-small real
V, with per-cube smallness K = 2^{41}/(s̄ - 1) coming from the **field size** (ε ≤ ε_mix(s̄) lets the fluctuation be
continued to bond weights |s| ≤ s̄ ≫ 1), not from the cube size (M_c = R + 2 suffices). It answers BB-mix-gap (2): the mass
family has radius 1 + O(γ/S); the bond family has radius s̄ because the inter-cube couplings it weights are either walk steps
(small: ε_R) or arguments of the nonlinearity (small: ε). *What it is not.* (1) k = 1 only. (2) Not BB-loc's polymers.
(3) Constants astronomically small: at N5-w0's numbers (m = 9.66·10⁻¹¹, a = m/2, R_* ≈ 1.7·10¹²), s̄ ≈ 10^{15}e^{m_0} needs
R - R_* ≈ (2/(aL))·log(2s̄) ≈ 5·10¹¹, and ε_mix ∝ s̄^{-4} — uniform, not evaluated. (4) c_ρ, C_M-type constants exist and are
not computed.

### 6.6 Proposition BB-mix-k: ARGUED (the wall at k ≥ 2)
At depth k on the composite route, Step 1 needs a localised expansion of the composite inverse 𝓛^{-1} (lane A's) whose
inter-cube pieces carry a factor ≪ 1/s̄, uniformly in k: **(H-RW^∇)_k** (lane A's (H-lin^∇) is a global inverse bound; its
weighted form at m > 0 gives decay e^{-mM_c} per cube crossing, which is small only for M_c ≫ log(s̄)/m and must then be
organised as a walk expansion in 𝔐^∇). Step 2 needs the cube weights S_Q to act boundedly in 𝔐^∇: sharp weights make
cube-boundary jumps of size ≤ (s̄ + 1)|x^c|, whose coarse gradient ∇^c is L^{k-j}-large at level j and whose Hölder seminorm is
not controlled, so smooth weights χ_Q (coarse gradient 1/M_c) are needed, with commutators [𝓛, χ_Q] bounded as in lane A's
(COMM) (BA-11/BA-12, whose plain-current rows are lane A's GAP F3). The per-level alternative (BB-bond at level j for the
one-step problem with action E_j^br) is the per-level architecture outside BFT's anti-circularity clause. Not proven.

## 7. Session-2 check record, outcome and notes for other files (written after §6)

**Check bb2** (criteria checks/bb2_criteria.md born 05:50:12 UTC; script checks/bb2_symbol.py born 05:50:30; output
checks/bb2.out 05:51:32-05:51:34). Runner scratchpad bb/run_bb2.sh: `until mkdir …/locks/numeric; do sleep 20; done`
(the lock was held by another session at 05:50:46; acquired 05:51:32), load1 5.68 < 8, memory free 50%, nice 10, thread
variables 1, PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l, python3 without -I, no `timeout`, no trap, `rmdir` once (05:51:34).
2.1 s wall, peak footprint 560 MB. No process left; no __pycache__ in checks/.
- **B2-1 PASS:** max||H_1d0c||/(||H_1||·||d0c||) = 1.1e-16 (κ = 1); Hermiticity defect 4.9e-13 (informational).
- **B2-2 PASS:** β - 1 at t = 0.4, 0.2, 0.1, 0.05, 0.025 (worst direction): -1.24e-1, -3.43e-2, -8.81e-3, -2.22e-3, -5.55e-4;
  max|β(0.025) - 1| = 5.55e-4 ≤ 1e-3; ratios |β(0.05) - 1|/|β(0.025) - 1| = 3.993 for all 8 (n, e) (O(t²)): **c_1 = 1**.
- **B2-3 PASS:** ρ(t) = max_n||H_1 - H_W||/t⁴ = 0.774, 0.857, 0.881, 0.887, 0.888; ratios 1.0069, 1.0017: **H_1 - H_W = O(|p|⁴)
  with c_1 := 1 fixed, not fitted** (the quadratic part of R_1 is dimension 6).
- Informational: κ = 0.25: max|β(0.025) - 1| = 2.4e-3 (would fail B2-2's 1e-3, but κ = 0.25 carries no verdict), ratios 3.971,
  ρ ratios 1.029, 1.007; κ = 4: 8.7e-5, ratios 3.999, ρ ratios 1.001, 1.000. The approach β → 1 is O(t²) at every κ tested,
  consistent with F-tree "for every κ".
- *Reading (measured only).* At k = 1, trivial background, abelian fibre model: the marginal coefficient of E_1^br's quadratic
  part is 1 and the remainder is O(p⁴), as Theorem BB-4♮ (a)-(c) and Lemma BB-W (n = 2) assert. Not measured: n ≥ 3 kernels,
  k ≥ 2, non-abelian structure, non-trivial backgrounds.

| Item (session 2) | Status | Note |
|---|---|---|
| 11 binding fixes of REVIEW_BFT_B_S1 | applied, tagged [RBB1-fix] | §0-§4 in place (41 tags) |
| Lemma BB-W (dimension lemma) | PROVEN-HERE | gauge invariance + B_4 + β = 0 ⇒ no Taylor part of dimension ≤ 5 at orders 2-5 (L4a-Π; Ward identity + (A1); parity); symbol range corrected to m' < m/(n - 1) |
| Lemma BB-sm | PROVEN-HERE | |F(f_{A,ℓ})| ≤ C_sm𝒩ℓ^{-2} |
| **Theorem BB-4♮** | **PROVEN as an implication** | E_k^br = c_kS_W + R_k, c_k = 1 (F-tree; κ_j-variation: inference from its proof), β[R_k] = 0, sup_k𝒩(R_k) ≤ C_♮, R_k irrelevant (dim ≥ 6, ℓ^{-2}); one composite contraction, no per-level route; ⇐ (H-lin^∇)_m + (H-rem^∇)_m + (FP♯') + (SF-∞)_B + BA-9; on 𝒞_glob; not a polymer norm |
| bb2 | PASS (B2-1, B2-2, B2-3) | c_1 = 1, H_1 - H_W = O(p⁴) at k = 1 |
| Proposition BB-mix-wall | ARGUED (wall named) | BB-loc's Möbius activities need (BB-prod)_1; propagation gives K ≈ Ce^{-μ_1M_c/2^d} |
| Construction BB-bond + **Theorem BB-mix′_1** | **PROVEN-HERE (k = 1)** | bond-weighted walk cluster expansion; K = 2^{41}/(s̄ - 1) from field size ε ≤ ε_mix(s̄); ||R||_𝒜 ≤ 2e^{m_0}C_R: BFT-4's polymer bound at k = 1 (unreviewed); thresholds corrected with 𝔠_s := max(s̄𝔠_♮p_Π, 𝔠_∞) |
| Proposition BB-mix-k | ARGUED (wall named) | k ≥ 2 needs (H-RW^∇)_k (localised composite inverse) and 𝔐^∇-compatible cube weights ((COMM)-type) |

**What BFT-4 now rests on (session 2).** At k = 1: the polymer bound is PROVEN-HERE (BB-mix′_1, from ledger theorems, with
one sub-claim — the density analyticity constant c_ρ — taken by the proof of N5-an♭). For every k on 𝒞_glob: the
marginal-extracted, irrelevance-norm form (Theorem BB-4♮) ⇐ lane A's shared estimate at m > 0 + (SF-∞)_B. The polymer form
at k ≥ 2: (H-RW^∇)_k + 𝔐^∇-compatible weights (BB-mix-k). Outside 𝒞_glob: lane A's (UHL), (SL-cov).

## FOR OTHER FILES (session 2; for their owners; not edited)
- **FLOW.md (F-tree):** Theorem BB-4♮ (a) uses F-tree with level-dependent κ_j; reading the proof, κ enters only through
  κ_k^{-1}P_⊥ and bounded alias terms, so the statement holds for κ_j ∈ [κ_-, κ_+] varying (FLOW's owner may wish to say so).
  bb2 measures c_1 = 1 with O(t²) approach at κ = 0.25, 1, 4. Lemma BB-W gives FLOW a lattice statement: once β[F] is
  extracted, a gauge-invariant B_4-invariant exponentially local functional has no dimension-≤ 5 part at orders ≤ 5.
- **REVIEW_S22 Part 5 / BFT-4:** **[RBB2-fix B4N-2 (applied 06:47 UTC, after §9; logged): "the right form of BFT-4 is"
  reads "a marginal-extracted Taylor-norm form of BFT-4 (necessary, weaker than ||·||_𝒜) is"; the polymer form ||·||_𝒜
  remains BFT-4.]** the right form of BFT-4 is E_k^br = c_kS_W + R_k with β[R_k] = 0 and R_k bounded in the
  irrelevance norm 𝒩 (Theorem BB-4♮); the polydisc-sup polymer norm is reachable at k = 1 (BB-mix′_1), and at k ≥ 2 its
  missing piece is (H-RW^∇)_k.
- **BFT_A (lane A):** Theorem BB-4♮ consumes (H-lin^∇)_m + (H-rem^∇)_m + (FP♯') through Theorem BA and BB-3_k only; the
  polymer form at k ≥ 2 would additionally need a walk/localised expansion of 𝓛^{-1} in 𝔐^∇, (H-RW^∇)_k.
- **SF.md (L-loc)_1:** BB-mix′_1 gives a gauge-invariant polymer representation at k = 1 with per-cube smallness from field
  size; (L-loc)'s "for ALL mixed derivatives" is replaced by bond analyticity with radius s̄.

---

# Session 3 (2026-10-28 UTC)

## 9. PRE-STATED (session 3) — statements only; appended after Step 1's [RBB2-fix] edits (stat 06:33:18 UTC, 111780 bytes) and before any session-3 proof, criteria file or script. Nothing in §9 cites a result of this session; lane A's estimates enter only as named hypotheses. Proofs follow in §10, later.

### 9.0 Setting W (definitions)
- **Spaces.** Depth k ≥ 1, coarse torus 𝕋 of side T (level-j side TL^{k-j}). X := ⊕_{j<k}(level-j su(N)-valued link fields),
  normed by lane A's 𝔐^∇ at m = 0 (BFT_A §1.4); Y := lane A's source representations y = (G_l, s_l, j_0, j_l) of the
  corrected pair (BFT_A §6 [RBA1-fix] and §7.2, whichever plain-current slot lane A finally fixes), with its norm ||·||_Y;
  π: Y → X*, ⟨y, x⟩ := Σ_l⟨G_l, dx_l⟩ + Σ_l⟨s_l, r_l(x)⟩ + ⟨j_0, x_0⟩ + Σ_{l≥1}⟨j_l, x_l⟩. 𝓛: X → X* is lane A's composite
  linearisation at the trivial chain (Hessian of 𝔉_k + Feynman terms at x = 0; BFT_A §3.9), 𝓑(u, x) := ⟨𝓛u, x⟩.
- **Positions.** Coarse coordinates z ∈ R⁴/TZ⁴; a component of a level-j form sits at the midpoint of its link/plaquette.
  supp u := the set of positions where some component of u is ≠ 0; S^{(a)} := {z : dist_∞(z, S) ≤ a}; |S| := coarse
  volume.
- **Local-sup norms.** A norm is *local-sup with radius r_N* if ||u|| = sup_zN_z(u) for seminorms N_z with N_z(u) = N_z(u')
  whenever u = u' on B_∞(z, r_N).
- **Cutoffs.** A cutoff of scale ℓ ≥ 1/2 is a C^{1,1} function φ: R⁴/TZ⁴ → [0, 1] with |∂_μφ| ≤ 1/ℓ, |∂_μ∂_νφ| ≤ 1/ℓ²
  (coarse derivatives, a.e.). It acts on X by (φx)_j(b) := φ(m_b)x_j(b) and on Y componentwise, (M_φy) := φ(position)·y.
  **[RBB3-fix RS3-4: cutoffs of every scale ℓ ≥ ¼ (χ_□ has scale ¼, §10.2); neither W-mult's proof nor any count uses
  ℓ ≥ ½; the same extension applies in clause (e) of §9.2.]**
- **Geometry.** Boxes □ of side R (coarse, R ≥ 8, corners on the coarse lattice), cubes Q of side M_c := 2R, T a multiple
  of M_c with T ≥ 2M_c; each box lies in one cube Q(□). N(Q) := Q and its *-adjacent cubes. Bonds 𝔅 := unordered pairs of
  *-adjacent cubes; s ∈ C^𝔅; s_{QQ} := 1, s_{QQ'} := s_{{Q,Q'}} for *-adjacent Q ≠ Q', **s_{QQ'} := 0 otherwise**.
- **Cutoff families.** χ_□ (Σ_□χ_□ ≡ 1, supp χ_□ ⊂ □^{(1)}, scale 1/2); ψ_□ (ψ_□ = 1 on □^{(R/2)}, supp ψ_□ ⊂ □^{(R)},
  scale R/4); η_Q (Σ_Qη_Q ≡ 1, supp η_Q ⊂ Q^{(2)}, scale 1).
- **Local tori and pieces.** 𝕋_□ := a coarse torus of side T_W := 3R + 12 and ι_□ a coarse-lattice translation embedding
  □^{(R + 6)} into it; 𝓛_□ := the depth-k composite operator on 𝕋_□. With the commutator covector C_ψ(u): x ↦ 𝓑(ψu, x) -
  𝓑(u, ψx) and its representation C^♯_ψ(u) ∈ Y from (W-comm):
    𝓖_□ := 𝓛_□^{-1}π,  P_□y := ψ_□·ι_□^*𝓖_□ι_{□*}(M_{χ_□}y),  R_□y := -ι_□^*C^♯_{ψ_□}(𝓖_□ι_{□*}M_{χ_□}y),
    P := Σ_□P_□,  R := Σ_□R_□.
- **Cube-weighted operators** (on cube-indexed vectors 𝐳 = (z_Q)_Q ∈ Y^{cubes}, 𝐀 = (A_Q)_Q ∈ X^{cubes}; |||𝐳||| :=
  sup_Q||z_Q||):
    (𝐈(s)𝐲)_Q := Σ_{Q''}s_{QQ''}y_{Q''},  (𝐑(s)𝐳)_{Q'} := Σ_□s_{Q'Q(□)}R_□z_{Q(□)},
    (𝐏(s)𝐳)_{Q'} := η_{Q'}·Σ_□s_{Q'Q(□)}P_□z_{Q(□)},  **𝐊(s) := 𝐏(s)(1 - 𝐑(s))^{-1}𝐈(s)**.
  𝐲 is *cube-supported* if supp y_Q ⊂ Q^{(2)} for every Q. Views: **S_Q𝐀 := Σ_{Q'}s_{QQ'}A_{Q'}**.

### 9.1 Named hypotheses (inputs; none is proven here)
- **(W-lin)** [lane A's (H-lin^∇) at m = 0, on every torus]: for every coarse torus 𝕋' of side ≥ T_W, 𝓛_{𝕋'} is invertible
  and ||𝓛_{𝕋'}^{-1}π||_{Y→X} ≤ G, uniformly in k and in the side. (Weighted form (W-lin)_m: the same for
  e^{mf}𝓛_{𝕋'}^{-1}πe^{-mf}, f 1-Lipschitz; this is lane A's m > 0 version used by BB-3_k.)
- **(W-comm)** [lane A's (COMM), BFT_A §3.10, on every torus]: for every cutoff ψ of scale ℓ ≥ 1 there is a linear map
  u ↦ C^♯_ψ(u) ∈ Y with πC^♯_ψ(u) = C_ψ(u), supp C^♯_ψ(u) ⊂ (supp ∂ψ)^{(3)}, depending on u only on (supp ∂ψ)^{(3)}, and
  ||C^♯_ψ(u)||_Y ≤ (C_c/ℓ)||u||_X, C_c k-uniform.
- **(W-loc)** [structure of 𝔉_k at the trivial chain]: (i) 𝓑(u, x) = 0 if dist_∞(supp u, supp x) > 3; 𝓑 is invariant under
  coarse-lattice translations, and 𝓑_𝕋(u, x) = 𝓑_{𝕋'}(ιu, ιx) whenever supp u ∪ supp x lies in a set whose 3-neighbourhood
  is mapped into 𝕋' by a coarse translation ι; (ii) ⟨y, x⟩ for y supported in S reads x only on S^{(3)}; (iii) Feynman
  form: 𝓛 acts on all of X (no hard slice constraint; if lane A keeps a hard block-local slice Π, cutoffs act as Πφ and
  [Π, φ] is part of (W-comm)); (iv) 𝓛, the cutoffs and the remainder below commute with constant gauges (Ad).
- **(f)** [lane A's (H-rem^∇), localised]: with g := NB (the data source, a residual-type source at level k - 1) and
  𝔑(x; B) := ∇(𝔉_k∘exp + ½||Γ·||²)(x) - 𝓛x - g as an element of Y: on the complex balls ||x||_X ≤ ρ_0, ||B||_D ≤ ε_0,
  ||𝔑(0; B)||_Y ≤ C_N||B||²_D and ||𝔑(x; B) - 𝔑(x'; B)||_Y ≤ C_N(||x|| + ||x'|| + ||B||_D)||x - x'||, 𝔑 holomorphic in (x, B);
  and **locality**: M_η𝔑(u; B) depends on u only on (supp η)^{(3)}.
- **(E3^∇)** [cubic density defects are level-summable]: write E := 𝔉_k∘exp + ½||Γ·||² = Σ_DD as a sum of local densities
  (level-0 plaquettes, level-j soft terms, Feynman terms), each reading u on a set of diameter ≤ 3 around its base position;
  𝒟_Q := the densities with base position in Q; 𝔇_D(u) := D(u) - D(0) - ½⟨∇D(0) + ∇D(u), u⟩ (the trapezoid defect). Then
  for ||u||_X ≤ ρ_3, ||B||_D ≤ ε_0 (complex): |Σ_{D∈𝒟_Q}𝔇_D(u; B)| ≤ C_3|Q^{(3)}|·||u||_X³, C_3 k-uniform.
- **(I-id)** [Theorem BA's conclusions, BFT_A §3.9, and BA-9]: for ||B||_D ≤ ε_0 the equation 𝓛x + g + 𝔑(x; B) = 0 has a
  unique solution x(B) in ||x||_X ≤ r_u; Γx(B) = 0 (NA-crit'); E_k^br(B) = 𝔉_k(x(B); B) (Balaban convention, BA-9).

### 9.2 (H-RW^∇)_k, stated precisely (the six clauses of REVIEW_BFT_B_S2 C.3, binding fix BMk-1)
**(H-RW^∇)_k** holds with constants (G_P, N_P, ε_W, 𝔠_W, C_M^X, C_M^Y) and a threshold R_W(s̄) if, for every s̄ ≥ 2 and
every R ≥ R_W(s̄), uniformly in k ≥ 1 and T:
- **(a) partition:** level-k cubes of side M_c = 2R, boxes of side R refining them; all levels' variables at a position are
  assigned to cubes and boxes through the cutoffs η_Q, χ_□ (smooth assignment; no sharp indicator acts on a field);
- **(b) decomposition:** 𝓛^{-1}π = P(1 - R)^{-1} = Σ_{n≥0}PR^n on Y, R = Σ_□R_□, where P_□ and R_□ read their input only on
  □^{(1)} ("column in □^{(1)}"), P_□ writes in □^{(R)} and R_□ writes in □^{(R+3)} ∖ □^{(R/2 - 3)};
- **(c) bounds (the replacement of "solid" absolute bounds):** ||P_□y||_X ≤ G_P||y||_Y, and for all scalars w_□ and inputs
  z_□: ||Σ_□w_□P_□z_□||_X ≤ N_PG_P·max|w_□|·max||z_□||_Y and **||Σ_□w_□R_□z_□||_Y ≤ ε_W·max|w_□|·max||z_□||_Y**, with
  **s̄ε_W ≤ ¼**; the operator is data-independent, so the bounds hold trivially for all data in 𝒞_glob(ε);
- **(d) holomorphy, s ≡ 1 identity, splitting:** 𝐊(s) is holomorphic (polynomial-then-uniform-limit) on |s_b| ≤ s̄ with
  |||𝐊(s)𝐲||| ≤ 𝔠_Ws̄²|||𝐲||| for cube-supported 𝐲; for cube-supported 𝐲, Σ_{Q'}(𝐊(1)𝐲)_{Q'} = 𝓛^{-1}πΣ_Qy_Q; and if the cubes
  are partitioned into classes and s_b = 0 on every bond between classes, (𝐊(s)𝐲)_{Q'} depends only on the y_Q and s_b with
  Q, b inside the class of Q';
- **(e) cube weights compatible with 𝔐^∇:** multiplication by every cutoff of scale ℓ ≥ 1/2 is bounded on X (C_M^X) and on Y
  (C_M^Y), k-uniformly; the s-weights act only as scalars on cube components; (W-comm) holds;
- **(f)** as in 9.1, applied to the views S_Q𝐀, which satisfy ||S_Q𝐀||_X ≤ 2^ds̄|||𝐀||| whenever supp A_{Q'} ⊂ Q'^{(2)} for all Q'.

### 9.3 Lemmas
- **Lemma W-ls (local-sup replaces solidity).** If ||·|| is local-sup with radius r_N and every ball B_∞(z, r_N) meets the
  supports of at most n of the u_i, then ||Σ_iw_iu_i|| ≤ n·max_i|w_i|·max_i||u_i||. Lane A's 𝔐^∇ (m = 0) and Y norms are
  local-sup with r_N = 3. *Planned: PROVEN-HERE (elementary).* **[RBB3-fix RW3-1: lane A's norms are sums of sups, hence
  only equivalent (factor t_X = 4, t_Y = 6) to local-sup norms; the lemma holds with the factor t; see §10.1.]**
- **Lemma W-cut (cutoff families exist).** The families χ_□, ψ_□, η_Q of 9.0 exist (products of one-dimensional C^{1,1}
  quadratic splines). *Planned: PROVEN-HERE.*
- **Lemma W-mult (cutoffs act boundedly on 𝔐^∇ and on Y).** For a cutoff φ of scale ℓ ≥ 1/2:
  ||φx||_X ≤ (1 + (12d + 3)/ℓ + 2/ℓ²)||x||_X =: C_M^X(ℓ)||x||_X and ||M_φy||_Y ≤ (1 + d/ℓ)||y||_Y =: C_M^Y(ℓ)||y||_Y.
  *Planned: PROVEN-HERE* (discrete product rule; the Campanato product rule Osc_2(fg; B) ≤ ||f||_∞Osc_2(g; B) +
  osc_∞(f; B)||g||_∞; the residual commutator through lane A's BL-2 (b) sup bound for Q; ℓ ≥ 1/2 makes the constants
  explicit).
- **Lemma W-pair (local pairing).** For y ∈ Y whose only non-zero component is a residual-type source s_l supported in S,
  and every x ∈ X: |⟨y, x⟩| ≤ 4ω_l^{-1}|S^{(3)}|·||y||_Y||x||_X. *Planned: PROVEN-HERE.*
- **Lemma N5-an♭-dens (RBB2-fix C2-2).** In the setting of Lemma N5-an♭ (PROOF l.5648-5659), every single density D of
  F(U, V) = S_W(U) + κ_0Σ_cφ̂_c(V; M̄_c(U)) (a level-0 plaquette term, or one soft term κ_0φ̂_c), as a function
  (A, u, B, v) ↦ D(e^Ae^uU, e^Be^vV) of the logs of its own variables, is holomorphic on the closed polydisc of radius r_♭
  and bounded there by some S_ρ < ∞ depending only on (N, L, κ_±) (finitely many types modulo translation). Hence
  |D(e^ÃU', V') - D(U', V')| ≤ (2S_ρ/r_♭)||Ã||_∞ for ||Ã||_∞ ≤ r_♭/2 at every (U', V') whose local AX-chart logs are ≤ r_♭/2.
  *Planned: PROVEN-HERE (routine: the proof of N5-an♭, applied to densities).*
- **Lemma U0-ℂ (U0 (iv) at complex V).** Let V = e^zV^r, V^r real, |z_c| ≤ ϱ ≤ 1/80 for every level-1 link c, and
  ε_{V^r} ≤ 1/40. Then (a) every level-1 plaquette has |log V_P| ≤ ε^ℂ_V := (ε_{V^r} + 4ϱ)(1 + 2(ε_{V^r} + 4ϱ)) (principal
  log, in sl(N, C)); (b) ||∇_AF(e^AU^(0)(V), V)|_{A=0}||_∞ ≤ 6c_ℂε^ℂ_V with c_ℂ := e^{6ϱ}(1 + (e^{6ϱ}ε^ℂ_V)²/5) ≤ 1.1.
  *Planned: PROVEN-HERE (BCH series bounds; analytic continuation of U0 (i) and of the stationarity of φ̂).*

### 9.4 Theorem RW^∇_k (the composite inverse is block-diagonally dominant in the box basis)
**Theorem RW^∇_k.** Assume (W-lin), (W-comm), (W-loc), k ≥ 1, R ≥ 8, M_c = 2R, T a multiple of M_c with T ≥ 2M_c **[RBB3-fix
RW3-3: R ≥ 13 (or T ≥ 3R + 14); product partitions for general T; see §10.7]** **[RBB3-fix RW3-4: Feynman form (W-loc) (iii)
assumed; hard-slice version: Theorem RW^∇_k-Π, §12.1]**. Then
**𝓛P = π(1 - R)** exactly, (b) holds, and (c)-(e) hold with
  G_P := C_M^X(R/4)·G·C_M^Y(1/2),  N_P := 4^d,  **ε_W := 5^d·(4C_c/R)·G·C_M^Y(1/2)**,  𝔠_W := (4/3)·2^d·N_P·C_M^X(1)·G_P,
  **R_W(s̄) := max{8, 16·5^d·C_c·G·C_M^Y(1/2)·s̄}**,
so (H-RW^∇)_k holds, uniformly in k and T. The per-step factor of the walk expansion 𝓛^{-1}π = Σ_ωT_ω (walks of boxes,
T_ω := P_{□_0}R_{□_1}⋯R_{□_n}) is ε_W = O(1/R), k-uniform. *Planned: PROVEN as an implication of (W-lin), (W-comm),
(W-loc).* **Remark (weighted form).** Under (W-lin)_m, ε_W gains the factor e^{-m(R/2 - 4)}, so R_W(s̄) = O(m^{-1}log s̄).
*Planned: PROVEN as an implication.* (Comparison: Theorem RW at level 0 uses sharp Dirichlet compressions and entrywise
(solid) block norms; RW^∇_k uses smooth cutoffs and local-sup norms, which is what the non-solid pair (𝔐^∇, Y) admits.)

### 9.5 Construction BB-bond_k and Theorem BB-mix_k (per-cube smallness at every k)
- **Construction BB-bond_k (multi-field bond family).** Data B in the complex ball 𝒫_ε := {||B||_D ≤ ε} of 𝒞_glob. On
  X^{cubes}: Φ_s(𝐀) := -𝐊(s)𝐲(𝐀), y_Q(𝐀) := M_{η_Q}[g + 𝔑(S_Q𝐀; B)]; 𝐀(s) its fixed point. Energy per cube:
    𝔈_Q(s) := ½⟨M_{η_Q}g, S_Q𝐀(s)⟩ + Σ_{D∈𝒟_Q}𝔇_D(S_Q𝐀(s); B),  ΔE(s) := Σ_Q𝔈_Q(s);
  for a cube set X, ΔE_X(s_X) := Σ_{Q∈X}𝔈_Q computed at the fixed point with every bond leaving X set to 0; R({Q}) :=
  ΔE_{{Q}}, R(X) := Σ_{Γ connected, spanning X}∫_{[0,1]^Γ}∂^Γ_sΔE_X(s_Γ, 0)ds_Γ (|X| ≥ 2), as in §6.5 Step 4.
- **Theorem BB-mix_k.** Assume (H-RW^∇)_k (a)-(e) with threshold R_W, (f), (E3^∇), (I-id), and write 𝔎 := 𝔠_Ws̄², σ := 2^ds̄,
  G_N := L^θκ_+ (so ||g||_Y ≤ G_N||B||_D). For s̄ ≥ 2, R ≥ max(R_W(s̄), 8), M_c = 2R, T a multiple of M_c (T ≥ 2M_c) and
    ε ≤ ε_mix,k(s̄) := min{ε_0, G_N/C_N, ρ_0/(4σ𝔎C_M^YG_N), ρ_3/(4σ𝔎C_M^YG_N), r_u/(2^{d+2}𝔎C_M^YG_N),
                         1/(2𝔎C_M^YC_Nσ(8σ𝔎C_M^YG_N + 1))},
  for every B ∈ 𝒫_ε (C_M^Y := C_M^Y(1)):
  (i) 𝐀(s) exists and is unique in |||𝐀||| ≤ r_s := 4𝔎C_M^YG_Nε, is holomorphic in (s, B) on |s_b| ≤ s̄, B ∈ 𝒫_ε, and
      Σ_{Q'}A_{Q'}(1) = x(B);
  (ii) **E_k^br(B) = E_∅(B) + Σ_XR(X) exactly**, E_∅(B) := 𝔉_k(0; B) (the trivial chain under the data: a sum of
      single-level-k-link terms), R(X) = 0 unless X is *-connected, R(X) a function of B on X^{(8)}, invariant under constant
      gauges and covariant under the translations that preserve the cube partition;
  (iii) **|R(X)| ≤ C_RK^{|X|-1}, K := 2^{41}/(s̄ - 1), C_R := 2^{40}C_E**, C_E := 2(M_c + 8)⁴C_M^YG_Nε·σr_s +
      C_3(M_c + 6)⁴(σr_s)³, uniformly in k and T. Hence for s̄ - 1 ≥ 2^{42}·80e·e^{m_0}: **||R||_𝒜 ≤ 2e^{m_0}C_R**,
      uniformly in k.
  *Planned: PROVEN as an implication.* **Not claimed:** that each R(X) is invariant under local gauge transformations
  (BFT-4's "gauge-invariant polymers"); named **(BB-gi)_k**, OPEN. **[RBB3-fix item 9: (BB-gi)_k is load-bearing (BFT-4 as
  stated, its Cauchy consequences at non-trivial backgrounds, EXISTENCE H-Bal-3(3a), HIST (C)'s glued main term). Restated in
  §12.2: on 𝒞_glob, (BB-gi)_k ⇐ (CovLift) + the session-3 hypotheses at the trivial chain (route GI-3 (a), Theorem
  BB-gi_k); off 𝒞_glob, Proposition GI-off ((CovLift) on boxes, axial/MSG frames for the sup half, (SL-cov), (I-id)).]**
  **[RBB3-fix RS3-6: covariance holds only under translations by multiples of M_c (the cube partition breaks unit
  translations); the sum E_k^br is translation invariant, which is all SF/BB-4♮ use.]**
- **Corollary BFT4-poly_k (BFT-4's polymer bound at every k, on 𝒞_glob, minus local gauge invariance of the pieces).**
  Under Theorem BB-mix_k's hypotheses: E_k^br = S_W + R_k with R_k := (E_∅ - S_W) + Σ_XR(X) a sum of local polymers and
  ||R_k||_𝒜 ≤ 2e^{m_0}C_R + C_∅, C_∅ := e^{m_0}(2M_c)⁴(6 sup_𝒫|s_p| + 4κ_+ sup_𝒫|φ̂_c(1; ·)|) (single-plaquette and
  single-link terms), uniformly in k; with Theorem BB-4♮, the marginal coefficient is c_k = β[E_k^br] = 1. *Planned:
  PROVEN as an implication.* **[RBB3-fix BP3-1 (binding, narrowed): the corollary is "the bounded-polymer clause of BFT-4 on
  𝒞_glob, without gauge-invariant pieces": E_k^br = S_W + R_k with R_k a k-uniformly bounded sum of local,
  constant-gauge-invariant polymers, NOT locally gauge invariant (E_∅ = κ_{k-1}Σ_cφ̂_c(V_c; 1) consists of single-link terms,
  tr V_c is not invariant under V_c ↦ g_xV_cg_y^{-1}, each of size O(κε²), the order of S_W per cell; exact invariance of
  E_k^br forces large cancellations between E_∅ and Σ_XR(X)); R_k is bounded, not small relative to S_W. c_k = 1 holds only
  under BB-4♮'s additional m > 0 inputs (lane A's (H-lin^∇)_m, (H-rem^∇)_m, (FP♯'), (SF-∞)_B, BA-9), which are not among
  BB-mix_k's hypotheses. The gauge-invariant version is Corollary BFT4-poly^gi_k (§12.2).]**
- **Corollary BB-Lloc_k ((H-RW^∇)_k ⇒ the classical part of SF's (L-loc)_k).** Under Theorem BB-mix_k's hypotheses, the
  branch-action (classical) part of SF's main-term density at stage k, as a function of its level-k argument on 𝒫_ε,
  splits as 𝓔^cl_{k,x} = Σ_{X∋x}𝓔_{x,X}, 𝓔_{x,X} := R(X)/|X|_cells (x a coarse cell of X), each piece depending on the
  argument on X^{(8)} only, holomorphic, and |𝓔_{x,X}| ≤ C_RK^{-1}e^{-κ_Ldiam_∞(X)}, **κ_L := log(1/K)/M_c**; this is SF
  (L-loc)_k's form (SF l.848-850) for the classical part, with polydisc 𝒫_ε. *Planned: PROVEN as an implication.* The
  fluctuation-integral parts of SF's 𝓔_k are not covered. **[RBB3-fix BL3-1 (binding): the per-piece bound
  C_RK^{-1}e^{-κ_Ldiam_∞X} discards the lattice-animal entropy (the number of *-connected X ∋ x of diameter D grows like
  exp(c(D/M_c)⁴)), so it is not summable over X. Corrected: |𝓔_{x,X}| ≤ C_RK^{-1/2}·K^{(|X|-1)/2}·e^{-(κ_L/2)diam_∞X}; then
  Σ_{X∋x}K^{(|X|-1)/2}(…) ≤ Σ_n(80eK^{1/2})^{n-1} converges for s̄ - 1 ≥ 2^{43}(80e)². Equivalently state the corollary as
  "(L-loc)_k with the polymer-norm bound ||R||_𝒜", which is what CE-exp-𝒞 consumes.]**
- **Remark ((SF-∞)_B from the walk expansion).** Walk terms that wrap the torus have ≥ T/(2R) steps, so the Taylor kernels
  of E_k^br at V = 1 on two tori T, T' ≥ T_0 agree up to O((s̄ε_W)^{T/(2R)}) [inference; planned ARGUED].

### 9.6 Failure modes (pre-stated)
- **RW∇-F1 (sharp Dirichlet boxes in 𝔐^∇).** Theorem RW's Dirichlet compressions, transplanted to the composite chain: the
  zero extension of a level-j Dirichlet solution has a jump of ∇^cx^c at the box boundary of the size of the boundary normal
  gradient, and the Campanato seminorm at scale ρ_j = L^{-(k-j)} turns it into L^{α(k-j)}×(jump). Expected: OCCURS
  [argued]; this is why 9.0 uses smooth cutoffs.
- **RW∇-F2 (local gauge invariance of the pieces).** The C-glob centring at the trivial chain is not covariant under
  non-constant gauges, so the bond-family pieces are not locally gauge invariant. Expected: OCCURS.
- **RW∇-F3 (naive energy bound grows with k).** On the 𝔐^∇ ball the soft energy at level l per coarse volume is O(η²)
  (the residual weight allows |r_l| ~ L^{-2(k-1-l)}η own on 4L^{4(k-1-l)} links), so a size bound of Σ_D[D(u) - D(0)] is
  O(kη²) per cube. Expected: OCCURS for that bound; 𝔈_Q is built from the data pairing and cubic trapezoid defects to avoid it.
- **RW∇-F4 (inherited).** (W-comm)'s plain level-l current rows are lane A's GAP 1 (BFT_A l.387-391); the theorems inherit
  it through (W-comm) and do not resolve it.

### 9.7 Check bb3 (criteria in checks/bb3_criteria.md, written after this section and before the script)
The algebra of Theorem RW^∇_k and Construction BB-bond_k on a model local operator (d = 2, one level, 𝓛 = -Δ + μ² on
scalar site fields, sup norms; boxes, cubes, cutoffs and local tori exactly as in 9.0 with R = 4): the parametrix identity
𝓛P = 1 - R; the Neumann series reproducing 𝓛^{-1}; the s ≡ 1 identity of (d); the class splitting of (d); the enlarged
nonlinear fixed point at s ≡ 1 versus the global one; the energy identity ΔE(1) = E(x) - E(0); and the energy splitting at
split s. Informational: the sup-norm of R as R grows. It tests no k-uniformity and no lane-A norm.

## 10. Proofs (session 3; appended after §9 (06:37:48 UTC) and after bb3 ran (06:42:01-06:42:03 UTC))

Post-proof corrections of pre-stated details are marked **[post-proof correction]** where they occur and collected in
§10.9; §9 is not edited.

### 10.1 Lemma W-ls: PROVEN-HERE
Fix z and let I_z := {i : supp u_i ∩ B_∞(z, r_N) ≠ ∅}, |I_z| ≤ n. On B_∞(z, r_N), Σ_iw_iu_i = Σ_{i∈I_z}w_iu_i, so
N_z(Σ_iw_iu_i) = N_z(Σ_{i∈I_z}w_iu_i) ≤ Σ_{i∈I_z}|w_i|N_z(u_i) ≤ n·max|w_i|·max||u_i||; take sup_z. Lane A's norms (m = 0):
every term of 𝔐^∇ (BFT_A §1.4) is a sup over positions of a quantity attached to a position z that reads x near z — x^c_j(z);
∇^cx^c_j(z) (one own step ≤ 1); the Campanato oscillation over boxes of side ρ ≤ 1 with a corner at z; the residual
r_j(x)(c), which reads x_j on the contours of c (within two level-(j+1) blocks, ≤ 2 coarse units) and x_{j+1}(c). Put N_z :=
the maximum over j of the sum of these quantities at z (with the Campanato sup restricted to boxes with corner z); then
||x||_𝔐 = sup_zN_z(x) up to the order of max and sup, which commute, and N_z reads x on B_∞(z, 3). The same for Y (sup
terms and Campanato terms, BFT_A §6/§7.2). ∎ *(Weights e^{m d(·,y_0)} multiply each local quantity by its weight at z;
the norms stay local-sup.)* This lemma is what replaces Theorem RW's entrywise ("solid") bounds: the s-weights below are
scalars on whole pieces, so the triangle inequality per position suffices; no entrywise absolute value is ever taken.
**[RBB3-fix RW3-1 (binding): the sentence "||x||_𝔐 = sup_zN_z(x) up to the order of max and sup, which commute" is false.
Lane A's norms are max over j of a SUM of sups (𝔐^∇: four terms ||x^c_j||_∞ + ||∇^cx^c_j||_∞ + [∇^cx^c_j]_α +
L^{k-1-j}||r^c_j||_∞; Y: (G) two terms, (P0) two terms, (R) and (Pl) one each), and sum and sup do not commute. Corrected
statement: with N_z as defined, ||x||' := sup_zN_z(x) is a local-sup norm (radius 3) and ||x||' ≤ ||x|| ≤ t||x||', t_X := 4
for 𝔐^∇, t_Y := 6 for Y (the summand counts). W-ls holds for ||·||' as proved; in lane A's norms it reads
||Σ_iw_iu_i|| ≤ t·n·max_i|w_i|·max_i||u_i||. Consequences (constants only; no statement changes form): every use of W-ls
gains t — N_P := t_X4^d; ε_W := t_Y5^d(4C_c/R)GC_M^Y(¼); R_W(s̄) := max{13, 16t_Y5^dC_cGC_M^Y(¼)s̄} (13 from RW3-3);
𝔠_W := (4/3)·t_Y2^d·t_X4^d·C_M^X(½)G_P; σ := t_X2^ds̄; the bound ||A||_X ≤ 2^dr_s of BB-mix_k (i) reads t_X2^dr_s ≤ r_u
(the threshold r_u/(2^{d+2}𝔎C_M^YG_N) of ε_mix,k gains 1/t_X); ε_mix,k inherits σ and 𝔎. Equivalently one may work
throughout in ||·||', with the equivalence constants t.]**

### 10.2 Lemma W-cut: PROVEN-HERE
Let σ(t) := 1 (t ≤ 0), 1 - 2t² (0 ≤ t ≤ ½), 2(1 - t)² (½ ≤ t ≤ 1), 0 (t ≥ 1): C^{1,1}, |σ'| ≤ 2, |σ''| ≤ 4, σ'(0) = σ'(1) = 0.
For an interval I of the circle and d_I(t) := dist(t, I):
- ψ_□(z) := Π_μσ((d_{□_μ}(z_μ) - R/2)/(R/2)): = 1 on □^{(R/2)}, = 0 off □^{(R)}, |∂_μψ| ≤ 4/R, |∂_μ∂_νψ| ≤ 16/R² (scale R/4).
  (d_I has kinks only on I, where σ(·) ≡ 1.)
- χ: w_I(t) := σ(d_I(t)) (1 on I, 0 at distance ≥ 1; C^{1,1} because σ'(0) = 0); for intervals of length R ≥ 2 partitioning
  the circle, 1 ≤ Σ_Jw_J ≤ 2, and near a common endpoint only two weights are non-trivial: χ_I := w_I/Σ_Jw_J has
  |χ_I'| = |σ'|/(1 + σ)² ≤ 2 and |χ_I''| ≤ |σ''| + 2σ'² ≤ 12; χ_□ := Π_μχ_{□_μ}(z_μ) has |∂_μχ| ≤ 2, |∂_μ∂_νχ| ≤ 12.
  **[post-proof correction: χ_□ has scale ¼ (|∂| ≤ 4, |∂²| ≤ 16), not ½ as pre-stated; every C_M^Y(½) attached to χ in §9
  reads C_M^Y(¼).]**
- η: w_Q(t) := σ(d_{Q_μ}(t)/2), normalised as for χ: |η'| ≤ 1, |η''| ≤ |σ''|/4 + 2(σ'/2)² ≤ 3, so η_Q has **scale ½
  [post-proof correction: pre-stated scale 1; C_M^X(1), C_M^Y(1) attached to η in §9 read C_M^X(½), C_M^Y(½)]**.
  supp η_Q ⊂ Q^{(2)}; since M_c = 2R ≥ 16 > 2·5, every B_∞(z, 3) meets Q^{(2)} for at most 2^d cubes Q. ∎

### 10.3 Lemma W-mult: PROVEN-HERE, with a corrected constant
Let φ be a cutoff of scale ℓ, x ∈ X, level j, coarse units, m = 0. With x_k := 0 in the residual of a displacement (the data
are not part of X):
- (1) ||(φx)^c_j||_∞ ≤ ||x^c_j||_∞.
- (2) ∇^c_ν(φx^c)(b) = φ(m_{b+e_ν})∇^c_νx^c(b) + h(b)x^c(b), h(b) := L^{k-j}[φ(m_{b+e_ν}) - φ(m_b)] = the average of ∂_νφ over the
  own step, so |h| ≤ 1/ℓ and ||∇^c(φx^c)||_∞ ≤ ||∇^cx^c||_∞ + ℓ^{-1}||x^c||_∞.
- (3) Campanato: for a box B of side ρ ∈ [ρ_j, 1] and functions f, g, Osc_2(fg; B) ≤ (avg_B|fg - f(z_0)avg_Bg|²)^{1/2} ≤
  ||f||_∞Osc_2(g; B) + osc_∞(f; B)||g||_∞. With f = φ(m_{·+e}): osc_∞ ≤ dρ/ℓ, so the first term costs ≤ [∇^cx^c]_α +
  (d/ℓ)||∇^cx^c||. With f = h: |h(b) - h(b')| ≤ |b - b'|_1/ℓ² ≤ dρ/ℓ², and Osc_2(x^c; B) ≤ osc_∞(x^c; B) ≤ dρ||∇^cx^c||_∞
  (a lattice path inside B has ≤ dρ/ρ_j own steps, each changing x^c by ρ_j|∇^cx^c|); so ρ^{-α}Osc_2(hx^c; B) ≤
  (d/ℓ)||∇^cx^c|| + (d/ℓ²)||x^c|| (ρ ≤ 1). Total: [∇^c(φx^c)]_α ≤ [∇^cx^c]_α + (2d/ℓ)||∇^cx^c|| + (d/ℓ²)||x^c||.
- (4) Residual: r_j(φx)(c) = φ(m_c)r_j(x)(c) + Σ_aw_{c,a}(φ(m_a) - φ(m_c))x_j(a), where (Q_jv)(c) = Σ_aw_{c,a}v(a). By lane A's
  BL-2 (b) (PROVEN there), ||(Q_jv)^c||_∞ ≤ 5||v^c||_∞, i.e. ||Q_jv||_∞ ≤ 5L||v||_∞ in own units, so Σ_a|w_{c,a}| ≤ 5L (the
  ∞→∞ norm of a scalar kernel is its maximal absolute row sum). The support of w_{c,·} lies in N(X, μ), whose midpoints are
  within own ℓ¹ distance 6L of m_c (BFT_A BA-12's bound; the slice part d∘h_j acts inside the blocks of c), i.e. within coarse
  ℓ¹ distance 6L·L^{-(k-j)}; so |φ(m_a) - φ(m_c)| ≤ 6L^{1-(k-j)}/ℓ and the commutator term is ≤ 30L²L^{-(k-j)}ℓ^{-1}·L^{-(k-j)}
  ||x^c_j||_∞ (own). The 𝔐^∇ residual term is L^{k-1-j}||r^c_j|| = L^{2(k-1-j)}||r_j||_own, so it changes by ≤ (30/ℓ)||x^c_j||_∞.
Summing (1)-(4) inside the max over j:
  **||φx||_X ≤ (1 + (2d + 31)/ℓ + d/ℓ²)||x||_X =: C_M^X(ℓ)||x||_X**
**[post-proof correction: the pre-stated constant was 1 + (12d + 3)/ℓ + 2/ℓ²; the ℓ^{-2} coefficient there (2) is below the
d = 4 obtained here; use the displayed C_M^X(ℓ).]** For Y, componentwise multiplication: sup terms do not grow; Campanato
terms ((G), (P0)) grow by ≤ (d/ℓ)·sup by the product rule of (3); the (R) and (Pl) terms are sup terms: **||M_φy||_Y ≤ (1 +
d/ℓ)||y||_Y = C_M^Y(ℓ)||y||_Y** (as pre-stated). ∎ *Note.* Both constants are k-independent: every own step of level j is
L^{-(k-j)} coarse units, and the coarse unit is the cutoff's scale; this is the cancellation that sharp cube weights lack
(BB-mix-k (W2): a sharp jump produces L^{k-j} in (2) and is not Hölder at scale ρ_j in (3)).

### 10.4 Lemma W-pair: PROVEN-HERE
Level-(l+1) links per coarse volume: 4L^{4(k-1-l)}; those with midpoint in S number ≤ 4L^{4(k-1-l)}|S^{(1)}|. For such c,
|s_l(c)| = L^{-(k-1-l)}|s^c_l(c)| ≤ ω_l^{-1}L^{-2(k-1-l)}||y||_Y and |r_l(x)(c)| = L^{-(k-1-l)}|r^c_l(c)| ≤ L^{-2(k-1-l)}||x||_X. The
HS pairing of the su(N) components is bounded by the product of norms. Hence |⟨y, x⟩| ≤ 4ω_l^{-1}|S^{(1)}|·||y||_Y||x||_X ≤
4ω_l^{-1}|S^{(3)}|·||y||·||x||. ∎ (For l = k - 1, ω_{k-1} = L^θ.)

### 10.5 Lemma N5-an♭-dens: PROVEN-HERE (routine), with radius r_ρ ≤ r_♭
**[post-proof correction: the radius is some r_ρ ∈ (0, r_♭], not necessarily r_♭ itself (N5-an♭ is an existence statement
for gradient/Hessian entries, and a single density is not such an entry; the same proof gives a radius for the densities,
which may be taken ≤ r_♭).]** *Proof.* (i) A plaquette density: Re tr(1 - U_p) on SU(N) equals N - ½(tr U_p + tr U_p^{-1}),
whose continuation is a polynomial in the entries of e^{±A}, e^{±u} for the four links: entire. (ii) A soft density
κ_0φ̂_c(V; M̄_c(U)) = κ_0[Re tr(W_0(M)^{-1}M) - Re tr(V^{-1}M)]: M̄_c is a polynomial in the link entries; W_0(M) = e^{X_0(M)}
with X_0 the fixed point of NA-alg (a)'s map, real-analytic in M where the transport logs are ≤ 1/20 (analytic implicit
function theorem, as in N5-an's proof); a real-analytic function near 0 continues holomorphically to a polydisc with a finite
sup. (iii) Up to translation by L there are finitely many density types, each with a fixed variable pattern, so one radius
r_ρ and one bound S_ρ serve all; shrinking a radius keeps holomorphy and the bound, so r_ρ ≤ r_♭ may be assumed. (iv) For
||Ã||_∞ ≤ r_ρ/2 at a point (U', V') whose local AX-chart logs are ≤ r_ρ/2, put f(w) := D(e^{wÃ}U', V') - D(U', V') for
|w| ≤ W := r_ρ/(2||Ã||_∞) (≥ 1): the arguments stay in the polydisc of radius r_ρ, so f is holomorphic, |f| ≤ 2S_ρ and f(0)
= 0; Schwarz gives |f(1)| ≤ 2S_ρ/W = (4S_ρ/r_ρ)||Ã||_∞. ∎ **[post-proof correction: the Schwarz constant is c_ρ = 4S_ρ/r_ρ (radius r_ρ/2
available for w, since the base point already uses up to r_ρ/2), not 2S_ρ/r_♭ as written in the C2-2 tag of §6.5; the
tag's "sharper" constant assumed the full radius r_ρ about the base point. Consequence for BB-mix′_1 (constants only):
c_ρ := 4S_ρ/r_ρ, and ε_mix(s̄) gains the two conditions s̄r_s ≤ r_ρ/2 (i.e. ε ≤ r_ρ/(24𝔠_ss̄)) and 3(3L - 1)ε ≤ r_ρ/2 (the
AX logs of the rows), both ε-independent thresholds.]**

### 10.6 Lemma U0-ℂ: PROVEN-HERE
(a) For P = (X, μ, ν), V_P is the ordered product of four factors e^{±z_c}V^{r,±1}_c. Moving every e^{±z} to the left
through the real (unitary) factors conjugates it by a unitary, which preserves HS norms: V_P = e^{w_1}e^{w_2}e^{w_3}e^{w_4}e^{Y_r}
with |w_i| ≤ ϱ and Y_r := log V^r_P (|Y_r| ≤ ε_{V^r}). Put S := 4ϱ + ε_{V^r} ≤ 1/20 + 1/40 = 3/40. Expanding the product,
|V_P - 1|_HS ≤ e^S - 1 ≤ S(1 + 0.53S) (submultiplicativity of HS on each monomial); log(1 + W) := Σ(-1)^{n+1}W^n/n converges
for |W|_HS < 1 with |log(1 + W)|_HS ≤ |W|/(1 - |W|); so |log V_P| ≤ S(1 + 0.53S)/(1 - S(1 + 0.53S)) ≤ S(1 + 2S) for S ≤ 0.18
(the inequality reduces to 0.47 ≥ 2.53S + 1.06S²) **[RBB3-fix RS3-2: read S ≤ 0.17; the reduced inequality fails at
S = 0.175; harmless, since S ≤ 3/40 here]**. tr log V_P ∈ 2πiZ (det V_P = 1) and |tr log| ≤ √N|log|_HS < 2π, so the log
is in sl(N, C); at z = 0 it is the principal log of V^r_P (uniqueness of small logs). (b) Lemma U0 (i)-(ii) are algebraic
and hold for SL(N, C) values (as U0 states). The soft term: the function (link logs of V) ↦ ∇_A[κ_0φ̂_c(V; M̄_c(e^AU^(0)(V)))]|_{A=0}
is real-analytic and vanishes identically on the real domain (U0 (iv)'s proof), hence its holomorphic continuation vanishes
identically on the connected complex neighbourhood. The Wilson term: the continuation of Re tr(1 - U_p) is N - ½(tr U_p +
tr U_p^{-1}); for b in p, U_p = P_1e^{A_b}U_bP_2 (or with U_b^{-1}e^{-A_b}), so the A_b-derivative in direction X is
-½tr(X(W - W^{-1})) with W := P_1^{-1}U_pP_1 = e^{Y}, Y = P_1^{-1}(log U_p)P_1. Non-corner plaquettes have U_p = 1 (U0 (ii))
and contribute 0. For a corner plaquette, P_1 is a product of ≤ 3 links of U^(0)(V), each 1 or e^{z}V^r with operator norms
of it and its inverse ≤ e^{ϱ}, so |Y|_HS ≤ e^{6ϱ}|log V_P| and |W - W^{-1}|_HS = |2 sinh Y|_HS ≤ 2|Y|(1 + |Y|²/5) (|Y| ≤ 1).
A link lies in 6 plaquettes: ||∇||_∞ ≤ 6e^{6ϱ}ε^ℂ_V(1 + (e^{6ϱ}ε^ℂ_V)²/5) = 6c_ℂε^ℂ_V, and for ϱ ≤ 1/80, ε^ℂ_V ≤ 0.087:
c_ℂ ≤ 1.0779·1.0018 ≤ 1.1. ∎ *Use.* With ε_{V^r} ≤ ε/4 and ϱ ≤ ε/16: S ≤ ε/2, so 6c_ℂε^ℂ_V ≤ 6·1.1·(ε/2)(1 + ε) ≤ 6·0.6ε
for ε ≤ 0.09; with ε_{V^r} ≤ ε/2, ϱ ≤ ε/16: S ≤ 3ε/4 and 6c_ℂε^ℂ_V ≤ 6·0.85ε **[RBB3-fix RS3-3: this second bound needs ε ≤ 0.02 (1.1·0.75(1 + 1.5ε) ≤ 0.85);
it holds for ε_mix]**. So BR1's contraction runs at complex V with
ε (the radius claims of the [RBB2-fix C2-3] tags in §1.2, §2.2, §3 and §5.2 are justified by this computation).

### 10.7 Theorem RW^∇_k: PROVEN as an implication of (W-lin), (W-comm), (W-loc)
**[post-proof correction: T_W := 3R + 14, not 3R + 12. The set □^{(R+6)} has ℓ^∞ side 3R + 12, and (W-loc) (i) needs it to
embed injectively into 𝕋_□ (on a torus of side exactly 3R + 12 its two boundary faces would be identified).]**
*Step 1 (parametrix identity 𝓛P = π(1 - R)).* Fix y ∈ Y and a box □; put y_□ := M_{χ_□}y (supported in □^{(1)}), ỹ := ι_*y_□ on
𝕋_□, u := 𝓖_□ỹ ∈ X(𝕋_□) ((W-lin) on 𝕋_□), so 𝓛_□u = πỹ; P_□y = ψ_□ι^*u. For x ∈ X(𝕋) let x' := x on □^{(R+3)} and 0 elsewhere
(a vector, no norm involved). Since supp(ψ_□ι^*u) ⊂ □^{(R)}, (W-loc) (i) gives 𝓑_𝕋(ψ_□ι^*u, x) = 𝓑_𝕋(ψ_□ι^*u, x'), and since both
arguments lie in □^{(R+3)}, whose 3-neighbourhood □^{(R+6)} embeds, = 𝓑_{𝕋_□}(ψ_□u, ιx'). By the definition of C_ψ on 𝕋_□:
  𝓑_{𝕋_□}(ψ_□u, ιx') = 𝓑_{𝕋_□}(u, ψ_□ιx') + ⟨C_{ψ_□}(u), ιx'⟩ = ⟨πỹ, ψ_□ιx'⟩ + ⟨C^♯_{ψ_□}(u), ιx'⟩.
The first pairing reads ψ_□ιx' only on □^{(4)} ((W-loc) (ii)), where ψ_□ = 1 (R/2 ≥ 4) and x' = x; translating back it is
⟨y_□, x⟩_𝕋. The second reads ιx' only on (supp ∂ψ_□)^{(3)} ⊂ □^{(R+3)}, where x' = x; it is ⟨ι^*C^♯_{ψ_□}(u), x⟩_𝕋 = -⟨R_□y, x⟩.
**[RBB3-fix RW3-2 (binding, justification): the previous sentence conflates two facts. The covector C_ψ(u) reads its
argument only on (supp ∂ψ)^{(3)} (Σu_aB_{ab}x_b(ψ_a - ψ_b) vanishes where ψ is locally constant); but the transfer to 𝕋 goes
through the representation, whose pairing reads x on (supp C^♯)^{(3)} ⊂ □^{(R+6)} ((W-loc) (ii)), where x' ≠ x. Correct
argument: put x'' := x on □^{(R+6)}, 0 elsewhere. Then ⟨ι^*C^♯_{ψ_□}(u), x⟩_𝕋 = ⟨C^♯_{ψ_□}(u), ιx''⟩_{𝕋_□} (pairing locality on the
embedded □^{(R+6)}, side 3R + 12 < T_W) = C_{ψ_□}(u)(ιx'') = C_{ψ_□}(u)(ιx') (x' = x'' on (supp ∂ψ_□)^{(3)} ⊂ □^{(R+3)}), which is
the second pairing above. This is what T_W = 3R + 14 is for.]**
**[RBB3-fix RW3-3 (binding, scope): Step 1 also needs □^{(R+6)} (side 3R + 12) to embed injectively in 𝕋, i.e. T ≥ 3R + 14. With
T a multiple of M_c = 2R and T ≥ 2M_c this holds for every such T iff R ≥ 13 (T = 4R needs 3R + 12 < 4R); the theorem's
"R ≥ 8" reads **R ≥ 13**, or else add T ≥ 3R + 14. Irrelevant in practice (R ≥ R_W ≫ 1). For BFT's class (every side T ≥ T_0)
replace "T a multiple of M_c" by product partitions: in each coordinate, cube sides in [M_c, 2M_c) and box sides in [R, 2R)
refining them (possible for every T ≥ 2M_c, as PROOF's R20-fix RW2-1); then local tori have side 4R + 14, the *-neighbour
count (3^d - 1 = 80) and the 2^d, 4^d, 5^d counts are unchanged (every side ≥ the old one), the distances in Step 5 use the
minimal sides and are unchanged, and the volume factors (M_c + 6)⁴ in C_E become (2M_c + 6)⁴.]**
**[RBB3-fix RW3-4 (binding, operator): this proof uses (W-loc) (iii), the Feynman form: 𝓛 acts on all of X, and x', x'',
ψι^*u, ψιx' (not in any slice) are fed to 𝓑 and to 𝓛_□u = πỹ. Lane A's present configuration-level operator is not of this
form: Theorem BA's hypotheses are at a "per-level covariant slice with Feynman terms on residual groups" (BFT_A l.206), and
LR-pot / Corollary FP are in the hard tent-axial slice S_tent (BFT_A l.893-896, l.934-939). The hard-slice version is
Theorem RW^∇_k-Π (§12.1, proved in §13); the mixed form is OPEN. Until lane A fixes its operator, (W-loc) (iii) is a
hypothesis lane A's present operator does not satisfy.]**
So 𝓛P_□y = π(M_{χ_□}y - R_□y), and Σ_□M_{χ_□}y = y (componentwise Σ_□χ_□ ≡ 1) gives **𝓛P = π(1 - R)**.
*Step 2 (supports; clause (b)).* P_□ and R_□ read y only through M_{χ_□}y, i.e. on □^{(1)}; P_□y ⊂ □^{(R)}; R_□y ⊂
(supp ∂ψ_□)^{(3)} ⊂ □^{(R+3)} ∖ □^{(R/2-3)} ((W-comm)).
*Step 3 (bounds; clause (c)).* Transport preserves local-sup norms of fields supported in □^{(R+3)}: for z with B(z, 3)
meeting the support, B(z, 3) ⊂ □^{(R+6)} lies in the embedded region, and lane A's local seminorms are defined by the same
formulas on both tori and are invariant under coarse translations (which preserve all level structures); elsewhere the
seminorm is 0. Hence, with W-mult, (W-lin), (W-comm):
  ||P_□y||_X ≤ C_M^X(R/4)·G·C_M^Y(¼)||y||_Y =: G_P||y||_Y,  ||R_□y||_Y ≤ (C_c/(R/4))·G·C_M^Y(¼)||y||_Y.
Counting (boxes of side R; R ≥ 8): a ball B_∞(z, 3) meets □^{(R+3)} for at most (⌈2(R + 6)/R⌉ + 1)^d ≤ 5^d boxes, and □^{(R)}
for at most (⌈2(R + 3)/R⌉ + 1)^d ≤ 4^d boxes. W-ls gives ||Σ_□w_□R_□z_□||_Y ≤ 5^d·max|w|·(4C_c/R)GC_M^Y(¼)·max||z_□|| =:
ε_W·max|w|·max||z_□|| and ||Σ_□w_□P_□z_□||_X ≤ 4^dG_P·max|w|·max||z_□|| **[RBB3-fix RW3-1: × t_Y and × t_X respectively (W-ls
is termwise, §10.1)]**. **[post-proof correction: ε_W := 5^d(4C_c/R)GC_M^Y(¼)
and G_P := C_M^X(R/4)GC_M^Y(¼) (χ has scale ¼, §10.2); R_W(s̄) := max{8, 16·5^dC_cGC_M^Y(¼)s̄}.]** For R ≥ R_W(s̄),
s̄ε_W ≤ ¼.
*Step 4 (the inverse).* ||R||_{Y→Y} ≤ ε_W < 1 (w ≡ 1, z_□ = y), so 1 - R is invertible and 𝓛P(1 - R)^{-1} = π. π is onto X*
(every covector is a plain current at each level, a component of Y), so 𝓛 is onto, hence invertible (dim X = dim X*), and
**𝓛^{-1}π = P(1 - R)^{-1} = Σ_{n≥0}PR^n = Σ_ωT_ω**, T_ω := P_{□_0}R_{□_1}⋯R_{□_n}, with ||PR^ny||_X ≤ 4^dG_Pε_W^n||y||_Y
(walks of length n, summed). (This uses (W-lin) only on the local tori 𝕋_□, not on 𝕋: the expansion constructs the inverse on any
torus of side ≥ 2M_c, and on Z⁴, from local-torus data alone.)
*Step 5 (clause (d)).* 𝐈(s), 𝐑(s), 𝐏(s) are linear in s. |||𝐑(s)𝐳||| ≤ s̄ε_W|||𝐳||| (Step 3 with w_□ = s_{Q'Q(□)}); so for
s̄ε_W ≤ ¼ the Neumann series of (1 - 𝐑(s))^{-1} converges uniformly on |s_b| ≤ s̄ with norm ≤ 4/3, and 𝐊(s) is holomorphic in
the interior and continuous up to the boundary. For cube-supported 𝐲, |||𝐈(s)𝐲||| ≤ 2^ds̄|||𝐲||| (W-ls with the 2^d count of
§10.2); |||𝐏(s)𝐳||| ≤ C_M^X(½)·4^dG_P·s̄|||𝐳||| (η has scale ½). So |||𝐊(s)𝐲||| ≤ 𝔠_Ws̄²|||𝐲||| with **𝔠_W := (4/3)2^d4^dC_M^X(½)G_P
[post-proof correction: C_M^X(½) in place of the pre-stated C_M^X(1)]**.
*The s ≡ 1 identity.* Non-adjacent distinct cubes are at ℓ^∞ distance ≥ M_c = 2R. Call 𝐳 *consistent with* z ∈ Y if
M_{χ_□}z_{Q(□)} = M_{χ_□}z for every box. (α) For cube-supported 𝐲, 𝐈(1)𝐲 is consistent with Y := Σ_Qy_Q: the y_{Q''} with
Q'' ∉ N(Q(□)) are supported in Q''^{(2)}, at distance ≥ 2R - 3 > 1 from □^{(1)}. (β) If 𝐳 is consistent with z, then
R_□z_{Q(□)} = R_□z and P_□z_{Q(□)} = P_□z (both read their input through M_{χ_□}); and M_{χ_{□'}}(𝐑(1)𝐳)_{Q(□')} =
M_{χ_{□'}}Σ_{□:Q(□)∈N(Q(□'))}R_□z = M_{χ_{□'}}Rz, because for Q(□) ∉ N(Q(□')) the support □^{(R+3)} of R_□z is at distance
≥ 2R - R - 4 > 1 from □'^{(1)}. So 𝐑(1)𝐳 is consistent with Rz; by induction and linearity Σ_{n≤N}𝐑(1)^n𝐈(1)𝐲 is consistent
with Σ_{n≤N}R^nY, and consistency passes to the limit. (γ) For 𝐳 consistent with z: Σ_{Q'}(𝐏(1)𝐳)_{Q'} = Σ_{Q'}η_{Q'}Σ_{□:Q(□)∈N(Q')}P_□z
= Σ_{Q'}η_{Q'}Pz = Pz, since for Q(□) ∉ N(Q') the support □^{(R)} of P_□z misses Q'^{(2)} (distance ≥ R - 2 > 0). Hence
**Σ_{Q'}(𝐊(1)𝐲)_{Q'} = P(1 - R)^{-1}Y = 𝓛^{-1}πΣ_Qy_Q**.
*Splitting.* If s_b = 0 on every bond between classes, every non-zero weight s_{QQ'} (including s_{QQ} = 1, and with s = 0 for
non-adjacent pairs) joins cubes of one class. 𝐈(s), 𝐑(s), 𝐏(s) then map the class-C components of their input to class-C
components, using only weights inside C; so does (1 - 𝐑(s))^{-1}; hence (𝐊(s)𝐲)_{Q'} depends only on the y_Q and s_b inside
the class of Q'.
*Clause (e)* is W-mult (§10.3) and the definition of 𝐈, 𝐑, 𝐏 (weights are scalars; no sharp indicator). ∎
*Reading: block-diagonal dominance.* In the box basis, the composite operator preconditioned by the local parametrix is
1 - R with ||R|| ≤ ε_W = O(C_cGC_M^Y/R): diagonal (the local inverses, (W-lin) on tori of side O(R)) dominant over the
off-diagonal transfers (commutators, (W-comm)), with a per-step factor < 1 that is k-uniform because G, C_c and C_M are.
This is the composite, multi-level analogue of Theorem RW (level 0, Dirichlet compressions, solid norms) and of the
level-1 walk expansions behind N5-sf1/NAH1; it needs no per-level covariance, so it sits inside BFT's anti-circularity
clause (one composite operator 𝓛; local inverses are 𝓛 on smaller tori).
*Remark (weighted form): PROVEN as an implication of (W-lin)_m and a localised (W-comm)* — the form ||C^♯_ψ(u)||_Y ≤
(C_c/ℓ)·sup_{z∈(supp∂ψ)^{(3)}}N^X_z(u), which is what "depending on u only on (supp ∂ψ)^{(3)}" gives when C_c is read as
a local constant **[this localised reading is an added hypothesis, not in §9's (W-comm)]**. Then with f := dist_∞(·, □^{(1)}),
f ≥ R/2 - 4 on (supp ∂ψ_□)^{(3)}, and N^X_z(u) ≤ e^{-m(f(z) - 3)}·(weighted seminorm), so ||R_□y||_Y ≤ (4C_c/R)G_m
C_M^Y(¼)e^{-m(R/2 - 7)}||y||_Y. Hence ε_W gains e^{-m(R/2 - 7)} and R_W(s̄) = O(m^{-1}log s̄). **[post-proof correction:
e^{-m(R/2-7)}, not e^{-m(R/2-4)}; the three units are the locality radius of N_z.]**

### 10.8 Construction BB-bond_k, Theorem BB-mix_k and the corollaries: PROVEN as implications
**[post-proof corrections, found while proving: (1) 𝔈_Q as pre-stated, ½⟨M_{η_Q}g, S_Q𝐀⟩ + Σ_{D∈𝒟_Q}𝔇_D(S_Q𝐀), sums at s ≡ 1 to
E(A) - E(0) - ½⟨𝔑(0; B), A⟩, not to E(A) - E(0): the trapezoid defect subtracts ½⟨∇D(0), u⟩ and ∇E(0; B) = g + 𝔑(0; B),
not g. The corrected definition is
  **𝔈_Q(s) := Σ_{D∈𝒟_Q}𝔉_D(S_Q𝐀(s)),  𝔉_D(u) := D(u) - D(0) - ½⟨∇D(u), u⟩ = ½⟨∇D(0), u⟩ + 𝔇_D(u)**,
and its bound needs Lemma W-grad0 below (added during the proof, not pre-stated); C_E's first term changes accordingly.
(2) (f)'s locality is needed in the data as well: M_η𝔑(u; B) depends on B only on (supp η)^{(3)} (the same structural
reason as in u: 𝔑 is built from local densities). (3) C_M^Y(1) → C_M^Y(½) (η has scale ½).]**
- **Lemma W-grad0 (added; PROVEN-HERE given lane A's Setting LIN identification of the linearised root map).** At the
  trivial chain, every density of E except the top-level soft densities κ_{k-1}φ̂_c(V_k; M̄_c(e^{x_{k-1}})) has zero gradient,
  and γ := Σ_D∇D(0; B) is the residual-type source s_{k-1}(c) = a_c(B), a_c(B) := the M-derivative of φ̂_c(V_c; M) at M = 1
  (left-trivialised), with |a_c(B)| ≤ (e^{|B_c|} - 1) ≤ 1.3|B_c| for |B_c| ≤ ½. Consequently, for every cube Q and u ∈ X,
  |Σ_{D∈𝒟_Q}⟨∇D(0; B), u⟩| ≤ 4·1.3||B||_D|Q^{(3)}|·||u||_X.
  *Proof.* Wilson densities at U_0 = 1: Re tr(1 - e^{q}) has zero gradient at q = 0 (Re tr X = 0 on su(N)). A soft density at
  level j < k - 1 at U_j = U_{j+1} = 1: φ = N^{-1}[Re tr(W_0(M)^{-1}M) - Re tr(V^{-1}M)] is stationary in M at M = W_0(M) = 1 = V
  (U0 (iv)'s argument) and its V-derivative at V = M = 1 is -N^{-1}Re tr(-X) = 0 (X ∈ su(N)). Feynman densities are
  quadratic. At the top level, x_{k-1} enters only through M = M̄_c(e^{x_{k-1}}) = exp(Qx_{k-1} + O(x²)) [Q the linearised S4' root
  map of lane A's Setting LIN, read], so ∂_xφ̂(V_c; M̄_c(e^x))|_0 = Q^Ta_c, with a_c(B)[δ] = Re tr(W_0(1)^{-1}δ) - Re tr(V_c^{-1}δ) =
  Re tr((1 - e^{-B_c})δ) (W_0 stationary, φ̂ = Nφ) and |1 - e^{-B_c}|_HS ≤ e^{|B_c|} - 1 **[RBB3-fix RS3-7: the holomorphic
  continuation of Re tr(V_c^{-1}δ) is ½tr((e^{-B} - e^{B})δ) = -tr(sinh(B)δ), not Re tr((1 - e^{-B})δ); the bound
  |sinh B| ≤ e^{|B|} - 1 ≤ 1.3|B| (|B| ≤ ½) is unchanged]**. Pairing with u: ⟨Q^Ta, u_{k-1}⟩ =
  ⟨a, r_{k-1}(u)⟩ (x_k := 0 for displacements), and Lemma W-pair at l = k - 1 with the support Q^{(2)} of the owned densities'
  sources (base in Q, contour radius ≤ 2) gives the bound with ||s^c||_∞ ≤ 1.3||B||_D (for l = k - 1, s^c = s). ∎
*Proof of Theorem BB-mix_k (with the corrections).* Write C_M^Y := C_M^Y(½).
- *(i) Fixed point.* Components of 𝐊(s)𝐳 are η_{Q'}·(…), so Φ_s maps into 𝐗_cs := {𝐀 : supp A_Q ⊂ Q^{(2)}}; on 𝐗_cs,
  ||S_Q𝐀||_X ≤ 2^ds̄|||𝐀||| = σ|||𝐀||| (W-ls, the 2^d count). 𝐲(𝐀) is cube-supported. With (f): |||Φ_s(0)||| ≤ 𝔎C_M^Y(G_Nε +
  C_Nε²) ≤ 2𝔎C_M^YG_Nε = r_s/2 (ε ≤ G_N/C_N); for 𝐀, 𝐀' in the r_s-ball (σr_s ≤ ρ_0), |||Φ_s(𝐀) - Φ_s(𝐀')||| ≤
  𝔎C_M^YC_N(2σr_s + ε)σ|||𝐀 - 𝐀'||| = 𝔎C_M^YC_Nσε(8σ𝔎C_M^YG_N + 1)|||𝐀 - 𝐀'||| ≤ ½|||𝐀 - 𝐀'||| by ε ≤ ε_mix,k. So Φ_s is a
  contraction of the r_s-ball (r_s/2 + r_s/2 ≤ r_s); its fixed point is unique there (any fixed point lies in 𝐗_cs), and,
  as a uniform limit of iterates holomorphic in (s, B) (𝐊 holomorphic in s, 𝔑 in (x, B)), holomorphic in the interior.
  *At s ≡ 1:* by (d), A := Σ_{Q'}A_{Q'} = -𝓛^{-1}πΣ_QM_{η_Q}[g + 𝔑(S_Q𝐀; B)]. M_{η_Q}𝔑(·; B) reads its argument on Q^{(5)}
  ((f) locality), where S_Q𝐀 = Σ_{Q'∈N(Q)}A_{Q'} = A (the A_{Q'} with Q' ∉ N(Q) live in Q'^{(2)}, at distance ≥ 2R - 7 > 0);
  so Σ_QM_{η_Q}𝔑(S_Q𝐀) = Σ_QM_{η_Q}𝔑(A) = 𝔑(A), Σ_QM_{η_Q}g = g, and 𝓛A + π(g + 𝔑(A; B)) = 0. ||A||_X ≤ 2^dr_s ≤ r_u, so A = x(B)
  by (I-id).
- *(ii) Exact decomposition.* At s ≡ 1, 𝔉_D(S_Q𝐀) = 𝔉_D(A) for D ∈ 𝒟_Q (D reads its argument within 3 of its base in Q,
  where S_Q𝐀 = A), so ΔE(1) = Σ_D[D(A) - D(0)] - ½⟨∇E(A), A⟩ = E(A) - E(0), since ∇E(A) = π(g + 𝓛A + 𝔑(A)) = 0. By (I-id),
  ΓA = 0, so E(A) = 𝔉_k(x(B); B) = E_k^br(B), and E(0) = 𝔉_k(0; B) =: E_∅(B) (at the trivial chain every density except the
  top-level soft ones is constant; E_∅ = κ_{k-1}Σ_cφ̂_c(V_c; 1), single-level-k-link terms). Splitting: if s vanishes on
  every bond between classes, Φ_s preserves class components (y_Q, Q ∈ C, reads S_Q𝐀, i.e. class-C components, and the
  shared data B; 𝐊(s) splits by (d)), so 𝐀(s) = ⊕_C𝐀_C(s_C), and ΔE(s) = Σ_CΔE_C(s_C) with ΔE_C = ΔE_X for X = C computed
  with the bonds leaving X set to 0. The cluster identity and *-connectivity follow verbatim as in §6.5 Step 4. Constant
  gauges: (W-loc) (iv) and uniqueness give 𝐀(s)(Ad_gB) = Ad_g𝐀(s)(B), and each D is invariant, so R(X) is invariant;
  translations by multiples of M_c preserve every construction. Support: through (f)'s locality in (u, B) and the densities,
  R(X) depends on B only on X^{(5)} ⊂ X^{(8)}.
- *(iii) Bounds.* For |s_b| < s̄ and Q ∈ X: ||S_Q𝐀|| ≤ σr_s ≤ min(ρ_0, ρ_3); W-grad0 and (E3^∇) give
  |𝔈_Q| ≤ ½·5.2ε(M_c + 6)⁴σr_s + C_3(M_c + 6)⁴(σr_s)³ =: C_E **[post-proof correction of the pre-stated C_E, whose first term
  used ||g||_Y and C_M^Y; the shape (polynomial in M_c, s̄, linear-times-cubic in ε) is unchanged]**, so sup|ΔE_X| ≤ |X|C_E.
  Cauchy in the |Γ| bond variables on polydiscs of radius s̄ - 1 (minus an arbitrarily small margin) about [0, 1]^Γ, |Γ| ≥
  |X| - 1, ≤ 2^{40|X|} subsets of the ≤ 40|X| internal bonds (d = 4: 80 *-neighbours), |X| ≤ 2^{|X|-1}:
  **|R(X)| ≤ 2^{40}C_E(2^{41}/(s̄ - 1))^{|X|-1} = C_RK^{|X|-1}**; with ≤ (80e)^{n-1} *-connected X ∋ Q_0 of size n and
  80e·e^{m_0}K ≤ ½: ||R||_𝒜 ≤ C_Re^{m_0}Σ_{n≥1}2^{-(n-1)} = **2e^{m_0}C_R**. Every constant is a function of (G, C_c, C_N, C_3, ρ_0,
  ρ_3, r_u, ε_0, L, κ_+, θ, d, s̄, m_0) only: k- and T-uniform. ∎
*Proof of Corollary BFT4-poly_k.* E_k^br = E_∅ + Σ_XR(X) by (ii); S_W(V_k) and E_∅ are sums of single-plaquette and
single-link functions, holomorphic and bounded on 𝒫_ε; assigning each to the cube of its base point makes R_k := (E_∅ - S_W)
+ Σ_XR(X) a polymer sum with ||R_k||_𝒜 ≤ 2e^{m_0}C_R + C_∅. With BB-4♮ (a), β[E_k^br] = 1 (for the same E_k^br, (I4) of BB-4♮
being (I-id)'s identification). The polydisc: 𝒫_ε is the C-glob complex data ball; BFT-2's polydisc lies in it after the
B4N-1 adjustment (ε → ε/2, r_ℂ ≤ 1/2). ∎ **[RBB3-fix BP3-1: what this proves is the narrowed corollary of §9.5's tag —
bounded, local, constant-gauge-invariant (not locally gauge-invariant) polymers, R_k of the order of S_W; the c_k = 1 clause
needs BB-4♮'s m > 0 inputs, which are additional hypotheses.]**
*Proof of Corollary BB-Lloc_k.* For *-connected X, diam_∞(X) ≤ M_c|X|, so K^{|X|-1} ≤ K^{-1}e^{-(log(1/K)/M_c)diam_∞(X)}; with
𝓔_{x,X} := R(X)/(|X|M_c⁴) for x a coarse cell of X, Σ_x𝓔_{x,X} = R(X) and |𝓔_{x,X}| ≤ C_RK^{-1}e^{-κ_Ldiam_∞(X)}; each piece is a
holomorphic function of the argument on X^{(8)} only. The single-link and single-plaquette terms are pieces of diameter ≤ 1.
This is SF (L-loc)_k's form for the classical (branch-action) density at stage k, with the uniform polydisc 𝒫_ε and κ_L =
log(1/K)/M_c in level-k units [identification of "classical part" as in REVIEW_BFT_B_S2 Part E; SF's 𝓔_k also contains
fluctuation-integral parts, which this does not touch]. ∎ **[RBB3-fix BL3-1: keep the factor K^{(|X|-1)/2}:
|𝓔_{x,X}| ≤ C_RK^{-1/2}K^{(|X|-1)/2}e^{-(κ_L/2)diam_∞X} (split K^{|X|-1} into two halves and use diam_∞X ≤ M_c|X| on one),
which is summable over X ∋ x for 80eK^{1/2} ≤ ½; see §9.5.]**
*Remark (SF-∞)_B: ARGUED.* Step 4 of §10.7 builds 𝓛^{-1} on Z⁴ and on every torus from the same local-torus pieces; a walk
contributing to a kernel entry on 𝕋 but not on Z⁴ must wrap, hence has ≥ T/(3R) steps; the Taylor kernels of E_k^br at
B = 0 are finite trees of 𝓛^{-1} and Taylor coefficients of 𝔑 (local), so torus and Z⁴ kernels differ by O((s̄ε_W)^{T/(3R)})
per tree, uniformly in k. Not written as a proof (the tree bookkeeping of the Taylor kernels is not done here).

### 10.9 Post-proof corrections (collected; §9 unchanged)
χ_□ has scale ¼ and η_Q scale ½ (§10.2); C_M^X(ℓ) = 1 + (2d + 31)/ℓ + d/ℓ² (§10.3); N5-an♭-dens has its own radius r_ρ ≤ r_♭
and c_ρ = 4S_ρ/r_ρ, with two added ε-independent thresholds in BB-mix′_1 (§10.5); T_W = 3R + 14 (§10.7); ε_W, G_P, R_W, 𝔠_W
with C_M^Y(¼), C_M^X(½) (§10.7); the weighted remark needs a localised (W-comm) and gains e^{-m(R/2 - 7)} (§10.7); 𝔈_Q is
Σ_{D∈𝒟_Q}𝔉_D(S_Q𝐀), with the added Lemma W-grad0, (f)'s locality also in B, C_M^Y(½), and the corrected C_E (§10.8). None
changes a theorem's form or status. **[RBB3-fix RS3-5: read "None changes a theorem's form; the hypotheses of BB-mix_k
((f) locality in B) and of the weighted remark (localised (W-comm)) are strengthened, and BB-bond_k's 𝔈_Q is redefined."]**

## 11. Session-3 check record, outcome and notes for other files (written after §10)

**Check bb3** (criteria checks/bb3_criteria.md born 06:39:49 UTC; script checks/bb3_walk.py born 06:41:47; output
checks/bb3.out 06:42:01-06:42:03). Runner scratchpad bb3/run_bb3.sh: `until mkdir …/locks/numeric 2>/dev/null; do sleep 20;
done` (free on arrival, acquired 06:42:01), load1 2.38 < 8, memory free 41%, nice 10, thread variables 1,
PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l, python3 without -I, no `timeout`, no trap, `rmdir` once (06:42:03). 2.38 s wall,
peak footprint 793 MB. No process left; no __pycache__ in checks/.
- **B3-1 PASS:** max|𝓛P - (I - R)| = 7.8e-16 (the parametrix identity, with 𝓛 applied on the 48² torus and R built from
  local-torus commutators, i.e. the embedding/locality step of §10.7 Step 1).
- **B3-2 PASS:** relative max|P(I - R)^{-1} - 𝓛^{-1}| = 4.8e-15; ||R||_∞ = 0.0524.
- **B3-3 PASS:** s ≡ 1 identity, relative error 1.3e-15 (8 Neumann steps).
- **B3-4 PASS:** class splitting at s_sp = 1.5: class-A outputs change by 0.0 under both perturbations; control (class B)
  changes by 1.48.
- **B3-5 PASS:** enlarged nonlinear fixed point at s ≡ 1 equals the global one to 2.4e-15.
- **B3-6 PASS:** ΔE(1) = -1.806905771205e-01 = E(x) - E(0) (printed relative difference 0.0).
- **B3-7 PASS:** energy splitting: class-A energy changes by 0.0 under both perturbations; control 3.8e-2.
- Informational: ||R||_∞ = 0.148, 0.041, 0.012 (μ² = 1; R = 4, 6, 8), 0.052, 0.0098, 0.0020 (μ² = 2): the model's walk
  factor falls with R faster than 1/R (R·||R||_∞ falls too), consistent with the weighted remark (exponential gain at m > 0).
- *Reading (measured only).* On a model local operator, the parametrix identity, the walk expansion of the inverse, the
  s ≡ 1 identity, the exact class splitting of the cube-weighted inverse, the multi-field nonlinear fixed point and the
  energy identity and splitting of Construction BB-bond_k hold to rounding. Not measured: anything about lane A's norms,
  k-uniformity, (W-comm)'s constant, the composite chain. Note: B3-6 tests the corrected 𝔈_Q (§10.8): the model has
  ∇E(0) = g exactly (𝔑(0) = 0), so it does not distinguish the pre-stated from the corrected definition; the correction is
  algebraic (§10.8 (1)).

| Item (session 3) | Status | Note |
|---|---|---|
| Binding fixes of REVIEW_BFT_B_S2 (R-1, B4N-1, B4N-2, BMW-1, C2-1, C2-2, C2-3, C2-4; non-binding B4N-r1, r2) | applied, tagged [RBB2-fix] | C2-3 radii set to ε_mix/16 (BB-mix′_1) and ε_B/16 (BB-3_1), smaller than the reviewer's literal ε_br/16, reason logged; the 05:57 §6.4 edit marked in §6.4 |
| Lemma N5-an♭-dens | PROVEN-HERE (routine) | own radius r_ρ ≤ r_♭, c_ρ = 4S_ρ/r_ρ; BB-mix′_1 gains two ε-independent thresholds |
| Lemma U0-ℂ | PROVEN-HERE | complex curvature ≤ S(1 + 2S), S = ε_{V^r} + 4ϱ; gradient ≤ 6c_ℂ·(complex curvature), c_ℂ ≤ 1.1; supports the BR1 (v) restatement |
| (H-RW^∇)_k | **stated precisely** (§9.2, clauses (a)-(f)) | binding fix BMk-1 |
| Lemmas W-ls, W-cut, W-mult, W-pair | PROVEN-HERE | local-sup norms replace solidity; cutoffs act k-uniformly on 𝔐^∇ and Y (constants corrected in §10.3) |
| **Theorem RW^∇_k** | **PROVEN as an implication** of (W-lin) [lane A's (H-lin^∇) on tori of side O(R)], (W-comm) [lane A's (COMM)], (W-loc) | 𝓛P = π(1 - R), ||R|| ≤ ε_W = 5^d(4C_c/R)GC_M^Y(¼), k-uniform: (H-RW^∇)_k (a)-(e); weighted remark: e^{-m(R/2-7)} gain under (W-lin)_m + localised (W-comm) **[RBB3-fix: constants × t (RW3-1, §10.1); scope R ≥ 13 or T ≥ 3R + 14, product partitions (RW3-3); Feynman form assumed, hard-slice version §12.1 (RW3-4); hypotheses not yet jointly satisfiable (RW3-5)]** |
| Lemma W-grad0 (added during proofs) | PROVEN-HERE (given Setting LIN's Q) | only the top-level soft densities have a gradient at the trivial chain: a residual-type source of size ≤ 1.3||B||_D |
| **Theorem BB-mix_k** | **PROVEN as an implication** of (H-RW^∇)_k + (f) + (E3^∇) + (I-id) | exact polymer decomposition at every k on 𝒞_glob; |R(X)| ≤ C_RK^{|X|-1}, K = 2^{41}/(s̄ - 1); ||R||_𝒜 ≤ 2e^{m_0}C_R, k-uniform; pieces constant-gauge invariant, **not** locally gauge invariant ((BB-gi)_k OPEN) |
| Corollary BFT4-poly_k | PROVEN as an implication | ~~BFT-4's polymer bound at every k on 𝒞_glob, minus local gauge invariance of the pieces~~ **[RBB3-fix BP3-1] the bounded-polymer clause of BFT-4 on 𝒞_glob without gauge-invariant pieces: R_k k-uniformly bounded, local, constant-gauge-invariant, not locally invariant (E_∅'s single-link terms, of the order of S_W); c_k = 1 only with BB-4♮'s m > 0 inputs** |
| Corollary BB-Lloc_k | PROVEN as an implication | (H-RW^∇)_k (+ (f), (E3^∇), (I-id)) ⇒ the classical (branch-action) part of SF's (L-loc)_k, κ_L = log(1/K)/M_c **[RBB3-fix BL3-1: per-piece bound with the factor K^{(|X|-1)/2} and rate κ_L/2, or the ||R||_𝒜 form]** |
| Remark (SF-∞)_B | ARGUED | wrapping walks ≥ T/(3R) steps |
| Failure modes | RW∇-F1 ARGUED (sharp Dirichlet boxes); RW∇-F2 OCCURS (no local gauge invariance in C-glob); RW∇-F3 OCCURS for the naive energy bound, avoided; RW∇-F4 inherited (lane A GAP 1) | |
| bb3 | PASS (B3-1..B3-7) | algebra on a model operator only |

**What BFT-4 rests on (after session 3).** At k = 1: the polymer bound (BB-mix′_1) from ledger theorems + Lemma
N5-an♭-dens, on the corrected complex domain. At every k on 𝒞_glob: the polymer bound (Corollary BFT4-poly_k) ⇐
(W-lin) + (W-comm) + (W-loc) + (f) + (E3^∇) + (I-id), i.e. lane A's shared estimate (H-lin^∇) **on local tori**, lane A's
(COMM) **including its GAP 1 plain-current rows**, lane A's (H-rem^∇) with locality, the cubic density bound (E3^∇)
(second-order part PROVEN in lane A's BA-6; third order ARGUED there), and Theorem BA's conclusions; plus Theorem BB-4♮ for
c_k = 1. Missing for BFT-4 as stated: **(BB-gi)_k** (locally gauge-invariant pieces) and everything outside 𝒞_glob (lane A's
(UHL), (SL-cov)). ~~The localisation wall of session 2 ("(H-RW^∇)_k") is now a theorem relative to lane A's linear inputs;
no new linear estimate is assumed beyond lane A's on smaller tori and its (COMM).~~ **[RBB3-fix RW3-5 (binding; the
overclaim is withdrawn): the localisation wall of session 2 ("(H-RW^∇)_k") is now an IMPLICATION of (W-lin), (W-comm),
(W-loc). Lane A has not established these jointly in one norm pair. Joint-satisfiability gaps: (GAP 1) (W-comm)'s plain
level-l commutator rows [A^T, ψ]A (BFT_A l.244, GAP 1 l.387-391) have size O(1/ℓ) per level and are representable in Y
only through a (Pl) slot, and BL-6 (b) (PROVEN) shows (H-lin^∇) FAILS with that slot as written for θ ≤ 1 - α; lane A's
repair (rough/smooth split, (G♯-rough) + (SB) for the BCH₂ rows) is NOT PROVEN (BFT_A §13.4, §13.7); [inference, from the
review] the commutator row may split like CR-1 into residual-type + (G♯-rough) parts, which would remove the (Pl) slot.
(LR-grad) (W-lin) is a configuration-level 𝔐^∇ bound (x^c, ∇^cx^c, [∇^cx^c]_α); lane A proves the gauge-invariant
outputs (BL-5 (a), Theorem W) and the potentials in S_tent (Corollary FP); the gradient half (LR-grad; lane A's LRL (b)
now) is OPEN. (Slice) (W-loc) (iii) must match lane A's operator (RW3-4; Theorem RW^∇_k-Π for the hard slice). So
RW^∇_k is a correct theorem whose hypothesis set has, today, no known model in one norm pair.]**
**[RBB3-fix (BB-mix_k at m = 0, mechanism): at m = 0 the per-cube smallness K = 2^{41}/(s̄ - 1) comes from CUBE SIZE, not
from field size: s̄ is bought by M_c = 2R ≥ 2R_W(s̄) ∝ t_Y5^dC_cGC_M^Y(¼)·s̄, so K ∝ C_cG/M_c polynomially, and
κ_L = log(1/K)/M_c ~ (log M_c)/M_c: k-uniform and fixed, but tiny (in BB-mix′_1 at k = 1 the smallness came from field
size at R = R_* + O(log s̄)). Any consumer with a rate threshold (SF (L-loc)_k's "κ_L in M-units ≈ κ_5M", SF l.850) needs
the weighted form: R_W = O(m^{-1}log s̄) and κ_L ≈ m/c, which requires (W-lin)_m and the localised (W-comm) (the weighted
remark of §10.7). Lane A's Theorem W proves the gauge-invariant half of (W-lin)_m; see also RW∇-F5 (§12.3).]**

## FOR OTHER FILES (session 3; for their owners; not edited)
- **PROOF.md, Lemma BR1 (v) (proposed edit, for the ledger owner; REVIEW_BFT_B_S2 D.4).** Proposed text: "(v) V ↦ A*(V)
  extends holomorphically to {e^zV : V real, ε_V ≤ ε_br/4, |z_c| ≤ ε_br/16} with ||A*||_∞ ≤ r(ε_br); E_1^br is holomorphic there.
  *Proof addition:* for such e^zV the lift's corner plaquettes have complex curvature ≤ S(1 + 2S), S := ε_V + 4|z| ≤ ε_br/2,
  and Lemma U0 (iv) continues to complex V with the factor c_ℂ ≤ 1.1 (BFT_B Lemma U0-ℂ, §10.6), so ||Φ(0)||_∞ ≤ 6𝔠_∞·0.6ε_br and
  the contraction of (i) runs with ε → 0.6ε_br; (U^(0)(V), V) ∈ 𝔑(α_*) since ε_br/16 ≪ α_*/8; the AX-chart condition of
  N5-an♭ holds with r_♭/6 + ε_br/16 ≤ r_♭/4." The present radius α_*/8 is not supported: at |z| ≈ α_*/8 the lift's gradient is
  O(α_*), and 12𝔠_∞²C_♭·O(α_*) ≤ ½ is not implied. **Other ledger users of the radius to check:** Theorem NAH1 (a)'s complex
  class {(e^zV, e^{z'}W) : |z|, |z'| ≤ α_*/8} (PROOF l.5775, citing BR1 (v)); the remark at l.5582; HG1's proof (l.5715) uses
  only real-analyticity (unaffected).
- **BFT_A (lane A).** Theorem RW^∇_k consumes (H-lin^∇) only on tori of coarse side 3R + 14 and lane A's (COMM) for smooth
  cutoffs of scale ≥ 1 (the commutator covector x ↦ 𝓑(ψu, x) - 𝓑(u, ψx), represented in Y, local, ≤ (C_c/ℓ)||u||); in return
  it builds 𝓛^{-1} on every torus and on Z⁴ as a convergent walk expansion with per-step factor O(C_cG/R). So lane A's global
  (H-lin^∇) on large tori would follow from the small-torus estimate + (COMM) (Step 4 of §10.7) — possibly useful for its
  uniformity-in-T bookkeeping. The plain-current rows of (COMM) (GAP 1) are the only part of (W-comm) not proven in lane A's
  sizes; RW^∇_k does not need the (Pl) slot of the source norm except through (COMM). Componentwise multiplication of
  source representations by smooth cutoffs is bounded (Lemma W-mult); covector multiplication w ↦ w(ψ·) is never used.
- **SF.md (L-loc)_k.** Corollary BB-Lloc_k gives the classical (branch-action) part of (L-loc)_k at every k on 𝒞_glob from
  (H-RW^∇)_k, with κ_L = log(1/K)/M_c, pieces holomorphic on the uniform data ball; the fluctuation-integral parts are not
  covered. At k = 1, BB-mix′_1 already gave it with gauge-invariant pieces on the curvature-small class. **[RBB3-fix BL3-1:
  in summable form, |𝓔_{x,X}| ≤ C_RK^{-1/2}K^{(|X|-1)/2}e^{-(κ_L/2)diam_∞X}, or as the ||R||_𝒜 bound; at m = 0 κ_L ~ log M_c/M_c
  is tiny, a usable rate needs the weighted form.]**
- **REVIEW_S22 Part 5 / BFT-4.** The polymer bound at every k is reduced (on 𝒞_glob) to lane A's linear inputs on local tori,
  (COMM), (H-rem^∇) with locality, (E3^∇) and Theorem BA; the clause "gauge-invariant polymers" is not obtained in the
  C-glob centring (RW∇-F2) and is named (BB-gi)_k. The session-2 line "the right form of BFT-4" is withdrawn (B4N-2).
  **[RBB3-fix BP3-1: read "the bounded-polymer clause of BFT-4 on 𝒞_glob at every k is reduced to … (the pieces are local
  and constant-gauge invariant, not locally gauge invariant; R_k contains E_∅ - S_W, of the order of S_W); c_k = 1 needs
  BB-4♮'s additional m > 0 inputs; the reduction is to hypotheses not yet jointly satisfiable (RW3-5)". The gauge-invariant
  form: §12.2 (Theorem BB-gi_k, Corollary BFT4-poly^gi_k).]**
- **FLOW.md.** The walk expansion of §10.7 is for the composite 𝓛 at the trivial chain; FLOW's single-level Ã(U) is a
  different operator (REVIEW_BFT_B_S2 Part E); no claim about FLOW's (L-loc)/(L-loc2) is made.

# Session 4 (2026-10-28 UTC)

## 12. PRE-STATED (session 4) — statements only; the FIRST edit of session 4 (appended before any [RBB3-fix] edit, before any session-4 proof, criteria file or script). Nothing in §12 cites a result of this session; lane A's estimates and (CovLift) enter only as named hypotheses. Proofs follow in §13, later.

### 12.0 Settings (definitions)
- **Setting Π (hard slice).** As Setting W (§9.0), except: S ⊂ X is a linear subspace (the slice) and Π: X → X a linear
  projection onto S, given on every torus 𝕋' of side ≥ T_0 by one local formula. 𝓑(u, x) := Hess_x𝔉_k(x; B = 0)|_{x=0}(u, x)
  on all of X (no Feynman term). 𝓛_S: S → S*, ⟨𝓛_Su, v⟩ := 𝓑(u, v); π_S: Y → S*, the restriction of π. 𝒢_0 := {Dλ} is the
  space of linearised composite (chain) gauge directions trivial at level k: λ a level-0 su(N)-valued function vanishing
  at the level-k sites, Dλ := (d ev^{(j)}λ)_{j<k} (F6 of HIST §20.0).
- **Setting GI (covariant centring).** Data V: level-k links (real, or complex in the BFT-2 sense). A *background* is a
  chain Z = (Z_0, …, Z_{k-1}) with Z_k := V. Expansion U = e^xZ link by link (left-trivialised at the base site of each
  link). E_Z(x; V) := 𝔉_k(e^xZ; V) + ½||D_Z^*x||², D_Z the linearised chain-gauge generator at Z (λ ↦ d/dt|_0(Z^{e^{tλ}})Z^{-1},
  λ trivial at level k), ^* for the Ad-invariant pairing (the *background Feynman* term; at Z = trivial chain it is the
  pure Feynman operator). 𝓛_Z := Hess E_Z(0), g_Z := ∇E_Z(0) and 𝔑_Z(x) := ∇E_Z(x) - 𝓛_Zx - g_Z, represented in Y. Chain
  gauges ĥ (level-0 functions acting via F6) act by Z ↦ Z^ĥ, x ↦ Ad_ĥx (Ad at the base site of each link), y ↦ Ad_ĥy.
- **Covariant local-sup norms 𝔐^∇_Z, Y_Z.** Lane A's local seminorms with every difference replaced by the Z-transported
  difference (∇^Z_νx(b) := (Ad_{Z_ν(y)}x(b + e_ν) - x(b))/(own step), b based at y, coarse normalisation as in 𝔐^∇), every
  Campanato oscillation taken of values transported to the box corner along fixed axial paths in Z, and every residual
  replaced by r^Z_j := the linearisation at Z of the root-map residual. N^Z_z reads x and Z on B_∞(z, 3).
- **Box frames.** For a box □ and a level-k region Ω ⊃ □, the *axial frame* g_Ω(V) := the complete axial gauge of V on the
  sites of Ω (fixed axis order, root := the lowest corner of □, g_Ω(V)(root) = 1); frame data b_Ω(V) := log V^{g_Ω(V)} on
  the links of Ω (principal log).

### 12.1 Hard slice: hypotheses, lemma, theorem (Step 1, binding fix RW3-4)
- **(W-Π)** [slice structure]: Π is local with radius r_Π (Πx at position z depends on x only on B_∞(z, r_Π)), commutes
  with coarse translations and constant gauges, Πx - x ∈ 𝒢_0 for every x, and for every cutoff φ of scale ℓ ≥ ¼ and every
  u ∈ S: ||Π(φu)||_X ≤ C_Π(ℓ)||u||_X with C_Π(ℓ) k-uniform. **[RBB4-fix RS4-6: "one local formula" includes that the
  local-torus embeddings ι are translations by coarse-lattice vectors, so level-k roots map to roots and the tents/root
  lattice to themselves.]**
- **(W-lin-Π)** [lane A's (H-lin^∇) in the hard slice, every torus]: for every torus 𝕋' of side ≥ T^Π_W, 𝓛_S is invertible
  and ||𝓛_S^{-1}π_S||_{Y→X} ≤ G_Π, uniformly in k and the side.
- (W-comm), (W-loc) (i), (ii), (iv) as in §9.1, for this 𝓑.
- **Lemma W-gauge0.** 𝓑(Dλ, x) = 0 for every x ∈ X and every Dλ ∈ 𝒢_0. *Planned: PROVEN-HERE* (invariance of 𝔉_k(·; B = 0)
  under chain gauges trivial at level k, and ∇𝔉_k(0; 0) = 0).
- **Theorem RW^∇_k-Π (hard-slice version of Theorem RW^∇_k).** Assume (W-Π), (W-lin-Π), (W-comm), (W-loc) (i), (ii), (iv),
  R ≥ max(8, 2r_Π + 8), M_c = 2R, local tori of side T^Π_W := 3R + 14 + 2r_Π, and a global torus side T ≥ max(2M_c, T^Π_W)
  (multiple of M_c, or product partitions as in [RBB3-fix RW3-3]) **[RBB4-fix RS4-1: with product partitions (box sides up
  to 2R) read T^Π_W := 4R + 14 + 2r_Π; 3R + 14 + 2r_Π stands for T a multiple of M_c]**. Put 𝓖^Π_□ := 𝓛_{S,𝕋_□}^{-1}π_S,
  P^Π_□y := Π(ψ_□·ι_□^*𝓖^Π_□ι_{□*}M_{χ_□}y),  R^Π_□y := -ι_□^*C^♯_{ψ_□}(𝓖^Π_□ι_{□*}M_{χ_□}y),  P^Π := Σ_□P^Π_□, R^Π := Σ_□R^Π_□.
  Then **𝓛_SP^Π = π_S(1 - R^Π)** exactly, P^Π maps into S, and clauses (b)-(e) of (H-RW^∇)_k hold with P^Π_□ writing in
  □^{(R + r_Π)} and G_P replaced by C_Π(R/4)·G_Π·C_M^Y(¼); hence 𝓛_S^{-1}π_S = P^Π(1 - R^Π)^{-1} = Σ_nP^Π(R^Π)^n.
  *Planned: PROVEN as an implication.*
- **Corollary BB-mix_k-Π.** Theorem BB-mix_k (i)-(iii) hold in the slice form (E := 𝔉_k∘exp on S; (f), (E3^∇), (I-id) read
  with ∇ the S-gradient and x(B) ∈ S), with (H-RW^∇)_k supplied by Theorem RW^∇_k-Π. *Planned: PROVEN as an implication.*
  **[RBB4-fix RS4-2: "∇ the S-gradient" reads: ∇ is the full X-gradient represented in Y (𝔈_Q pairs per-density full
  gradients with S_Q𝐀, whose cube components are not in S); π_S enters only through 𝓛_S^{-1}π_S; the ΔE(1) identity uses
  ⟨∇E(A), A⟩ = ⟨π_S∇E(A), A⟩ = 0 because A ∈ S.]**
- **Remark (mixed operator).** Lane A's Theorem BA hypothesis form "per-level covariant slice with Feynman terms on residual
  groups" (BFT_A l.206) is neither the pure Feynman form of (W-loc) (iii) nor the pure hard slice above: OPEN for RW^∇_k.

### 12.2 Covariant centring: (BB-gi)_k (STEP 2, binding fix 9 of REVIEW_BFT_B_S3, route GI-3 (a))
- **(BB-gi)_k** (definition): every polymer R(X) of the bond-family decomposition is a locally gauge-invariant function of
  V: R(X)(V^h) = R(X)(V) for every level-k gauge h (on the class where the construction is defined).
- **(CovLift)** [the new input; named, not proven]: a map V ↦ Z^sm(V), given on every torus by one local formula, with
  (i) *covariance with a cocycle*: for every level-k gauge h a chain gauge ĥ(h, V) restricting to h at level k, with
  Z^sm(V^h) = Z^sm(V)^{ĥ(h,V)}, ĥ(h_1h_2, V) = ĥ(h_1, V)ĥ(h_2, V^{h_1}), ĥ(c, V) = c for constant c; **[RBB7-fix RS7-8: with the convention (U^a)^b = U^{ba} used in 19.13 and 22.12 the cocycle reads ĥ(h_2h_1, V) = ĥ(h_2, V^{h_1})ĥ(h_1, V); Lemma CL-uniq makes it automatic in either convention. RS7-6 (a): for Z^off "every torus" means every torus of coarse side T ≥ 5]** (ii) *locality*:
  Z^sm(V) and ĥ(h, V) at position z depend on V (and h) only on B_∞(z, r_Z); (iii) commutation with coarse translations;
  (iv) *smallness in frames*: whenever V = e^b on a region Ω in some level-k gauge with ||b||_∞ ≤ ε_Z, then in the extended
  gauge the local 𝔐^∇ size of log Z^sm(V) on Ω^{(-r_Z)} is ≤ C_sm||b||_∞, and ||g_{Z^sm(V)}||_Y there is ≤ C_g||b||_∞;
  (v) holomorphic continuation to complex data e^zV^r with the same bounds on a polydisc.
- **Background hypotheses (covariant forms)** (W-lin)_Z, (W-comm)_Z, (f)_Z, (E3^∇)_Z, (I-id)_Z: the statements of §9.1 for
  𝓛_Z, g_Z, 𝔑_Z, E_Z in the norms 𝔐^∇_Z, Y_Z, on every torus, at the backgrounds Z = Z^sm(V) of the class considered.
- **Lemma GI-frame.** (a) g_Ω(V^h) = h^{-1}g_Ω(V)h(root) and b_Ω(V^h) = Ad_{h(root)^{-1}}b_Ω(V). (b) If ||1 - V_p|| ≤ ε for
  every plaquette p of V in Ω (ε small), then ||b_Ω(V)||_∞ ≤ C_F(Ω)ε with C_F(Ω) depending only on the side of Ω and d.
  *Planned: PROVEN-HERE* (lasso F4 and F1 of HIST §20.0, as in MSG's step (1)).
- **Lemma GI-norm.** (a) ||Ad_ĥx||_{𝔐^∇_{Z^ĥ}} = ||x||_{𝔐^∇_Z} and ||Ad_ĥy||_{Y_{Z^ĥ}} = ||y||_{Y_Z} exactly. (b) If Z = e^z on a
  region in some gauge with local 𝔐^∇ size of z ≤ δ ≤ δ_0, then there N^Z_w and N_w agree within factors 1 ± C_eqδ.
  *Planned:* (a) PROVEN-HERE; (b) PROVEN-HERE for the sup, gradient and Hölder terms, ARGUED for the residual term.
- **Lemma GI-pert (transfer from the trivial chain, 𝒞_glob).** If ||log Z||_X ≤ δ in the global gauge with δ small in
  terms of (G, C_N, ρ_0): (W-lin)_Z holds with G_Z ≤ 2G; (f)_Z holds on halved balls with doubled constants; (I-id)_Z holds
  (the same critical orbit); (W-comm)_Z holds up to the extra row C^δ_ψ(u)(x) := ⟨δ𝓛ψu, x⟩ - ⟨δ𝓛u, ψx⟩, δ𝓛 := 𝓛_Z - 𝓛,
  whose Y-representation needs covector multiplication (a GAP-1-type plain row); (E3^∇)_Z holds in the status of (E3^∇).
  *Planned: PROVEN as an implication* for (W-lin)_Z and (f)_Z; ARGUED for (I-id)_Z; the rest as stated.
- **Construction BB-bond_k^cov.** As Construction BB-bond_k (§9.5 with the §10.8 corrections), with background
  Z := Z^sm(V) and frame-transplanted local inverses: for each box □, Ω_□ := □^{(R + 6 + r_Z)}, g_□ := g_{Ω_□}(V),
  ĝ_□ := ĥ(g_□, V); on 𝕋_□ (side T^cov_W := 3R + 14 + 2r_Z **[RBB4-fix RS4-1: 4R + 14 + 2r_Z with product partitions]**) the data e^{b̃_□}, b̃_□ := ι_*b_{Ω_□}(V) on the embedded Ω_□ and 0
  elsewhere; 𝓛_□ := 𝓛_{Z^sm(e^{b̃_□})} on 𝕋_□; P_□ and R_□ as in §9.0 conjugated by the frame (P_□y := ψ_□Ad_{ĝ_□}ι^*𝓖_□ι_*
  Ad_{ĝ_□}^{-1}M_{χ_□}y, R_□ likewise, sign conventions fixed in §13); densities D(u; V) := the density at e^uZ^sm(V).
- **Theorem GI-cov.** In Construction BB-bond_k^cov, under (CovLift), (W-lin)_Z on the local tori, (W-comm)_Z,
  (W-loc) (i), (ii), (iv), (f)_Z with locality, (E3^∇)_Z and (I-id)_Z, for every level-k gauge h: P_□(V^h) =
  Ad_ĥP_□(V)Ad_ĥ^{-1}, R_□(V^h) = Ad_ĥR_□(V)Ad_ĥ^{-1} (ĥ := ĥ(h, V)), 𝐀(s)(V^h) = Ad_ĥ𝐀(s)(V), and 𝔈_Q, ΔE_X and R(X) are
  invariant; E^cov_∅(V) := E_{Z^sm(V)}(0; V) = 𝔉_k(Z^sm(V); V) is a sum of local gauge-invariant densities. The class on which
  the construction is defined is gauge invariant. *Planned: PROVEN as an implication.*
- **Theorem BB-gi_k (on 𝒞_glob).** Assume (CovLift) and the hypotheses of Theorem BB-mix_k at the trivial chain for the pure
  (background-)Feynman operator ((W-lin) on local tori, (W-comm) including GAP 1's plain rows and the δ𝓛-row of GI-pert,
  (W-loc), (f) with locality, (E3^∇), (I-id)). Then there is ε_gi > 0 (k- and T-uniform; depending on s̄, R and the
  constants) such that for ε ≤ ε_gi Theorem BB-mix_k's conclusions (i)-(iii) hold for Construction BB-bond_k^cov on
  𝒞_glob(ε) (and on its gauge saturation), and **(BB-gi)_k holds**. *Planned: PROVEN as an implication.* **Relative to
  Theorem BB-mix_k's hypothesis set, the one new input is (CovLift).**
- **Proposition GI-off (outside 𝒞_glob).** On BFT's class (every V with plaquettes ≤ ε on a torus of side ≥ T_0) the
  construction is defined and Theorem GI-cov applies, given (CovLift) (with (iv) used on boxes), the background hypotheses
  at Z^sm(V) on the local tori (from GI-pert in the box frames: Lemma GI-frame supplies the sup half of the frame, (CovLift)
  (iv) the 𝔐^∇ half), (SL-cov) read as "lane A's estimates hold for the background-Feynman operator", and the
  identification (I-id) off 𝒞_glob (lane A's BFT-0 there). *Planned: ARGUED.*
- **Corollary BFT4-poly^gi_k.** Under Theorem BB-gi_k: E_k^br = S_W + R^gi_k on 𝒞_glob(ε), R^gi_k := (E^cov_∅ - S_W) + Σ_XR(X),
  a k-uniformly bounded sum of local, locally gauge-invariant polymers, holomorphic on the polydisc; c_k = 1 under BB-4♮'s
  additional m > 0 inputs. *Planned: PROVEN as an implication.*
- **Proposition CovLift-status.** Which candidate constructions of (CovLift) fail and why, and which remain. *Planned:
  ARGUED.*

### 12.3 Failure modes (pre-stated)
- **GI-F1 (frame transplant non-covariant).** The root constant h(root) of Lemma GI-frame (a) is not absorbed. Expected: does
  NOT occur ((W-loc) (iv), constant-gauge covariance of the local problem).
- **GI-F2 (stabiliser ambiguity).** Without the cocycle in (CovLift) (i), ĝ_□ is fixed only up to the stabiliser of Z^sm(V),
  which need not commute with the local-torus inverse. Expected: OCCURS without the cocycle; removed by it.
  **[RBB5-fix RS5-1: GI-F2 cannot occur for any lift that is orbit-covariant at level 0 (Lemma CL-uniq, 16.11); the cocycle
  is automatic.]**
- **GI-F3 (finite-range frame interpolation).** Smooth interpolation of frame logs glued across overlapping frames is
  covariant only to first order (transition cocycle fails at second order). Expected: OCCURS [argued].
- **RWΠ-F1 (piecewise-linear tents).** Lane A's S_tent uses piecewise-linear tents χ_X; the slice correction d(Pλ) then has
  gradient jumps at tent kinks, so (W-Π)'s 𝔐^∇ multiplier bound fails at fine scales (the RW∇-F1 mechanism). Expected:
  OCCURS [argued]; C^{1,1} tents would be needed. **[RBB4-fix RS4-4: C^{2,α} tents, and an elliptic slice; see the 13.2
  remark's tag.]**
- **RW∇-F5 (no coarse mass).** For an operator that is massless at every scale (no residual-type coarse mass), the local
  inverse's potential sup grows with the box and ||R_□|| does not fall like 1/R. Expected: OCCURS in a model; lane A's
  uniform G at m = 0 relies on the top residual's coarse mass.

### 12.4 Check bb4 (criteria in checks/bb4_criteria.md, written after this section and before the script)
Three model families. (A) the m = 0 regime of RW^∇_k (reviewer's request): d = 2 scalar, 𝓛 = -Δ + (block-average
projector) (a coarse-scale mass mimicking the top residual, massless within blocks), against a massless control
(-Δ + a global mean penalty); single-box G_□ and ||R_□|| (sup norms) as R grows. (B) frame covariance (Theorem GI-cov's
mechanism, with the background given): d = 2 SU(2) fundamental covariant Laplacian plus mass and quartic term, axial box
frames, local tori; the parametrix identity, covariance of P_□, R_□ and invariance of the bond-family energies under
random gauges; control: frame-free transplant. (C) the hard slice (Theorem RW^∇_k-Π's algebra): d = 2 abelian 1-form model
with plaquette term, a root-to-root residual term and a tent slice; Π∘Π = Π, Lemma W-gauge0, the slice parametrix
identity on S, the walk inverse against the slice inverse; control: a plateau too small for Π's radius. No k-uniformity
and no lane-A norm is tested.

## 13. Proofs (session 4; appended after §12 (07:30:46 UTC), after Step 1 (07:33:17) and after bb4 ran (07:41:10-07:41:22))

Post-proof corrections of pre-stated details are marked **[post-proof correction]** where they occur; §12 is not edited.
They are: (1) Lemma GI-pert needs an added input (Mult-Y) (13.5), so Theorem BB-gi_k's "the one new input is (CovLift)"
reads "the new inputs are (CovLift) and (Mult-Y)" (13.7); (2) Theorem BB-gi_k's bound replaces Lemma W-grad0 by (CovLift)
(iv)'s source bound and a local pairing bound, ARGUED for the non-residual components (13.7); (3) Lemma GI-frame is proven
for unitary V, the complex case ARGUED (13.3); (4) GI-pert's (I-id)_Z is ARGUED, as pre-stated.

### 13.1 Lemma W-gauge0: PROVEN-HERE
Let F(x) := 𝔉_k(e^x·1; B = 0) (trivial chain below, trivial data). For a level-0 function λ vanishing at the level-k sites
let Ψ_t(x) := the chain displacement of (e^x·1)^{e^{tλ}} (F6: one level-0 gauge acting at every level through its values at
the level-j sites; trivial at level k, so the data are unchanged). Invariance: F(Ψ_t(x)) = F(x). Differentiate in t at 0:
⟨∇F(x), ξ(x)⟩ = 0, ξ(x) := ∂_tΨ_t(x)|_0, with ξ(0) = Dλ (at x = 0 the transformed chain is pure gauge, link b = (y, y') ↦
e^{-tλ(y)}e^{tλ(y')}, derivative λ(y') - λ(y) at each level). Differentiate in x at 0 in a direction v:
Hess F(0)(ξ(0), v) + ⟨∇F(0), Dξ(0)v⟩ = 0. By Lemma W-grad0 at B = 0 (a_c(0) = 0, all other densities stationary) ∇F(0) = 0,
so 𝓑(Dλ, v) = 0. ∎ (No Feynman term enters; with one, the conclusion fails, which is why RW^∇_k's Feynman form needed
(W-loc) (iii) instead.) bb4 C-2 measures 4.0e-16 in the abelian model.

### 13.2 Theorem RW^∇_k-Π: PROVEN as an implication of (W-Π), (W-lin-Π), (W-comm), (W-loc) (i), (ii), (iv)
*Step 1 (parametrix identity on S).* Fix y, □; y_□ := M_{χ_□}y (support □^{(1)}), ỹ := ι_*y_□, u := 𝓖^Π_□ỹ ∈ S(𝕋_□), so
𝓑_{𝕋_□}(u, w) = ⟨ỹ, w⟩ for every w ∈ S(𝕋_□). Let v ∈ S(𝕋), v' := v on □^{(R+3)}, 0 elsewhere.
(a) P^Π_□y - ψι^*u = Π(ψι^*u) - ψι^*u ∈ 𝒢_0(𝕋) ((W-Π)), so by Lemma W-gauge0 (first slot) 𝓑_𝕋(P^Π_□y, v) = 𝓑_𝕋(ψι^*u, v).
(b) supp(ψι^*u) ⊂ □^{(R)}, so by (W-loc) (i) and the embedding of □^{(R+6)}: = 𝓑_{𝕋_□}(ψu, ιv').
(c) = 𝓑_{𝕋_□}(u, ψιv') + C_ψ(u)(ιv').
(d) Π_□(ψιv') - ψιv' ∈ 𝒢_0(𝕋_□), so (W-gauge0, second slot; 𝓑 symmetric) 𝓑_{𝕋_□}(u, ψιv') = 𝓑_{𝕋_□}(u, Π_□(ψιv')) =
⟨ỹ, Π_□(ψιv')⟩, since Π_□(ψιv') ∈ S(𝕋_□) is an admissible test vector.
(e) ỹ is supported in ι□^{(1)} and the pairing reads within 3, so only Π_□(ψιv') on ι□^{(4)} enters. For z ∈ □^{(4)},
Π_□(ψιv')(z) depends on ψιv' on B(z, r_Π) ⊂ □^{(4 + r_Π)} ⊂ □^{(R/2)} (R ≥ 2r_Π + 8), where ψ = 1 and v' = v; by locality and
the common local formula (translation covariance), it equals ι(Πv)(z) = ιv(z) (v ∈ S). Hence (d) = ⟨y_□, v⟩.
(f) C_ψ(u)(ιv') = ⟨ι^*C^♯_{ψ_□}(u), v⟩ = -⟨R^Π_□y, v⟩ by the x''-argument of [RBB3-fix RW3-2].
Summing over □ (Σχ_□ = 1): 𝓑(P^Πy, v) = ⟨y - R^Πy, v⟩ for every v ∈ S, i.e. **𝓛_SP^Π = π_S(1 - R^Π)**; each P^Π_□y = Π(…) ∈ S.
*Step 2 (supports).* P^Π_□ reads y on □^{(1)} and writes in □^{(R + r_Π)} (Π(0) = 0 and locality); R^Π_□ as in §10.7.
*Step 3 (bounds).* By transport (□^{(R + r_Π + 3)} embeds: its side 3R + 2r_Π + 6 < T^Π_W **[RBB4-fix RS4-1: 4R + 2r_Π + 6
< 4R + 14 + 2r_Π for product partitions]**), ||P^Π_□y||_X = ||Π_□(ψu)||_{X(𝕋_□)} ≤
C_Π(R/4)||u|| ≤ C_Π(R/4)G_ΠC_M^Y(¼)||y||, and ||R^Π_□y||_Y ≤ (4C_c/R)G_ΠC_M^Y(¼)||y|| ((W-comm) on 𝕋_□, u ∈ S(𝕋_□) ⊂ X).
Counting: 2(R + r_Π + 3)/R < 3 for R ≥ 2r_Π + 8, so a ball B(z, 3) meets □^{(R + r_Π)} for ≤ 4^d boxes; with W-ls (factor t,
[RBB3-fix RW3-1]): ε^Π_W := t_Y5^d(4C_c/R)G_ΠC_M^Y(¼), G^Π_P := C_Π(R/4)G_ΠC_M^Y(¼), N_P := t_X4^d.
*Step 4 (inverse).* For s̄ε^Π_W ≤ ¼, 1 - R^Π is invertible and 𝓛_SP^Π(1 - R^Π)^{-1} = π_S. π_S is onto S* (π onto X*, and
restriction X* → S* onto), so 𝓛_S is onto, hence invertible (dim S = dim S*): **𝓛_S^{-1}π_S = P^Π(1 - R^Π)^{-1}**, with values
in S.
*Step 5 (clause (d)).* Verbatim as §10.7 Step 5; the only changed distance is (γ): P^Π_□z lies in □^{(R + r_Π)}, at distance
≥ 2R - (R + r_Π) - 2 > 0 from Q'^{(2)} for Q(□) ∉ N(Q') (R > r_Π + 2). Clause (e): W-mult and (W-Π). ∎
*Corollary BB-mix_k-Π: PROVEN as an implication.* In §10.8 only two steps use the operator form. (i) at s ≡ 1:
A := Σ_{Q'}A_{Q'} = -𝓛_S^{-1}π_SΣ_QM_{η_Q}[g + 𝔑(S_Q𝐀)] ∈ S, so ⟨𝓛A + g + 𝔑(A), v⟩ = 0 for v ∈ S: the slice-critical
equation; (I-id) in slice form gives A = x(B). (ii) ΔE(1) = E(A) - E(0) - ½⟨∇E(A), A⟩ and ⟨∇E(A), A⟩ = 0 because A ∈ S. The
cube components A_Q are not in S (η_Q multiplies), which no step uses. ∎ **[RBB4-fix RS4-2: throughout, ∇ = the full
X-gradient represented in Y; π_S appears only inside 𝓛_S^{-1}π_S; (ii) uses A ∈ S.]**
*Model check.* bb4 C-1..C-4 (tent slice, plaquette + root-to-root terms, Feynman-free): Π∘Π = Π exactly, W-gauge0 4.0e-16,
the slice identity 1.2e-15, P^Πy ∈ S to 2.2e-16, walk inverse = slice inverse to 2.7e-14; C-6: without Π the S-tested identity
still holds (1.1e-15; Step (a) needs Π only for the values) but P'z ∉ S (relative 9.9e-6). C-5 (pre-registered control) FAILED
as a prediction; diagnostic D1 (post hoc): the identity fails (6.9e-4) only for a plateau below Π's measured reach (1.5).
*Remark (RWΠ-F1: OCCURS [argued]).* For u ∈ S, Π(φu) - φu = d(Σ_Xχ_Xμ_X), μ_X(z) := -avg∫_{c_X→z}(φ(w) - φ(z))u_0(w), of coarse
size ≲ ||u||/ℓ. With lane A's piecewise-linear tents, dχ_X jumps across the root hyperplanes and the faces |z - c_X| = n; the
coarse gradient of (dχ_X)μ_X there is ≈ (jump)/ρ_0 ~ L^k·||u||/ℓ (Σ_Xdχ_X = 0 leaves the differences μ_X - μ_Y, generically
≠ 0). So (W-Π)'s multiplier bound fails in 𝔐^∇ for S_tent as written. **Repair (for lane A):** C^{1,1} tents
χ_X(z) := Π_νσ(|z_ν - c_{X,ν}|/n) (σ of Lemma W-cut; σ(t) + σ(1 - t) = 1 on [0, 1], σ'(0) = 0). The projection algebra uses
only Σ_Xχ_X = 1 and χ_X(c_Y) = δ_{XY}, both of which hold; whether LR-pot's constants survive is lane A's question.
**[RBB4-fix RS4-4 (binding): the repair above is INSUFFICIENT. (1) C^{2,α} tents are required (e.g. the quintic σ_5(t) =
1 - 10t³ + 15t⁴ - 6t⁵): in Π(φu) - φu the tents enter differentiated once, so ∇^c of the correction contains χ'', and C^{1,1}
tents have jumps in χ'' which cost ρ_0^{-α} = L^{αk} in the [∇^c·]_α term of 𝔐^∇. (2) S_tent fails (W-lin-Π) independently of
the tents, by lane A's LR-grad diagnosis (axial potentials lose up to L^{k(1-α)} in ∇^c), and plausibly (W-Π) itself by the
axial-strip-flux mechanism of REVIEW_BFT_B_S4 B.4 (the weight φ(w) - φ(z) on single (X, σ) fluxes). (3) Theorem RW^∇_k-Π
therefore awaits an elliptic slice (box-Coulomb gauge glued with C^{2,α} tents): see §15-§16 (S_E). (4) Kept: the projection
algebra and LR-pot survive smooth tents, with constants × sup|σ'|.]**

### 13.3 Lemma GI-frame: PROVEN-HERE (unitary V; the complex case ARGUED as in Lemma U0-ℂ (a))
(a) With V^g(x, y) := g(x)^{-1}V(x, y)g(y), the axial frame is g(x) = hol_V(γ_x)^{-1} (γ_x the axial path root → x; then V^g = 1
on tree links). hol_{V^h}(γ_x) = h(root)^{-1}hol_V(γ_x)h(x), so g_Ω(V^h)(x) = h(x)^{-1}g_Ω(V)(x)h(root), and
(V^h)^{g_Ω(V^h)} = h(root)^{-1}V^{g_Ω(V)}h(root); principal logs commute with conjugation. (b) In the frame a link b = (x, x + e_μ)
carries the holonomy of the loop γ_xbγ_{x+e_μ}^{-1}, spanned by a ladder of ≤ Σ_{ν>μ}|x_ν - root_ν| ≤ (d - 1)ℓ_Ω plaquettes
(ℓ_Ω the side of Ω; the count of MSG's step (1)). Lasso (F4): ||1 - V^g(b)|| ≤ (d - 1)ℓ_Ωε; (F1) for (d - 1)ℓ_Ωε ≤ ½:
**|b_Ω(V)| ≤ C_F(Ω)ε, C_F(Ω) := 1.011(d - 1)ℓ_Ω**. On 𝒞_glob (V = e^B, ||B||_∞ ≤ ε) every plaquette has ||1 - V_p|| ≤ 4ε (F2),
so ||b_Ω|| ≤ 4C_F(Ω)ε. ∎ For the frame regions of §12.2, ℓ_Ω = 3R + 12 + 2r_Z **[RBB4-fix RS4-1: ℓ_Ω ≤ 4R + 12 + 2r_Z
with product partitions]**: the frame sup half costs a factor O(R),
which a threshold ε ≤ ε_gi(R) absorbs (R is fixed before ε). MSG is not needed at level k; it supplies depth-uniform
chain-level frames if one wants frames for given chains (the fluctuation side).

### 13.4 Lemma GI-norm: (a) PROVEN-HERE; (b) PROVEN-HERE for sup/gradient/Hölder (crude constant), residual term ARGUED
(a) Under (Z, x) ↦ (Z^ĥ, Ad_ĥx) with (Ad_ĥx)(b) := Ad_{ĥ(y)^{-1}}x(b) for b based at y (so (e^xZ)^ĥ = e^{Ad_ĥx}Z^ĥ):
Ad_{Z^ĥ_ν(y)}(Ad_ĥx)(b + e_ν) = Ad_{ĥ(y)^{-1}}Ad_{Z_ν(y)}x(b + e_ν), so ∇^{Z^ĥ}(Ad_ĥx)(b) = Ad_{ĥ(y)^{-1}}∇^Zx(b); transported box
values all pick up Ad_{ĥ(corner)^{-1}}, so oscillations are unchanged; the root-map residual is root-covariant (S4', F6), so
r^{Z^ĥ}(Ad_ĥx) = Ad r^Z(x). HS norms are Ad-invariant. Sources: the same. (b) In a gauge with Z = e^z, |z^c| ≤ δ (coarse
units): ∇^{Z,c}x^c - ∇^cx^c = (Ad_{e^{z_ν}} - 1)x^c(b + e_ν)/ρ_j and ||Ad_{e^a} - 1|| ≤ e^{2|a|} - 1 ≤ 3|a| (|a| ≤ ½ **[RBB4-fix RS4-5:
read |a| ≤ ⅓; e^1 - 1 > 3/2 at |a| = ½; harmless since |a| ≤ δ_0 is small]**) with own-unit
|a| = ρ_j|z^c| give ≤ 3δ||x^c||_∞; transported box values differ from plain ones by ≤ 3dρδ|·|, and the multiplier
M := (Ad_{e^z} - 1)/ρ_j has ||M|| ≤ 3δ and osc_B(M) ≤ 3dρ·||∇^cz^c||_∞ ≤ 3dρδ (δ bounds the local 𝔐^∇ size of z, gradient
included); the Campanato product rule (§10.3 (3)) then
gives |N^Z_w - N_w| ≤ C_eqδ·N_w-type bounds with C_eq ≤ 12d + 6 for the sup, gradient and Hölder terms. The residual term
compares the linearised root map at Z with Q: (Dρ(Z) - Q)x is a BCH correction of relative own size O(ρ_jδ) per level;
its k-uniformity in the weight L^{k-1-j} is of the BA-6 type: ARGUED. ∎

### 13.5 Lemma GI-pert: PROVEN as an implication — **[post-proof correction: with an added input (Mult-Y)]**
In the global gauge on 𝒞_glob, Z = e^z, ||z||_X ≤ δ. Write β_z(x) := log(e^xe^z) link by link (analytic for small
arguments), J_z := Dβ_z(0), E(w) := 𝔉_k(e^w; V) + ½||Γw||² (trivial-chain Feynman form). Then E_Z(x) = E(β_z(x)) + F_Z(x),
F_Z(x) := ½||D_Z^*x||² - ½||Γβ_z(x)||², and
  𝓛_Z = J_z^T(𝓛 + D𝔑(z))J_z + ⟨∇E(z), D²β_z(0)[·, ·]⟩ + Hess F_Z(0),   g_Z = J_z^T∇E(z).
||D𝔑(z)||_{X→Y} ≤ C_N(2δ + ε) by (f); J_z - 1, D²β_z(0) and the Feynman difference are pointwise multipliers of 𝔐^∇-size
O(δ). On X such multipliers are bounded (1 + C_Xδ) by the product rule of Lemma W-mult (matrix coefficients; the residual
commutator as in §10.3 (4), ≤ 30·(coarse gradient of the coefficient)) — PROVEN-HERE in the same way.
**[RBB4-fix RS4-3 (binding): (1) the sup, gradient and Hölder parts of the X-multiplier bound are PROVEN-HERE as said; the
residual part is ARGUED, the same item as GI-norm (b)'s residual term: J_z acts levelwise, so the residual commutator
contains (J_{z_{j+1}} - Q_jJ_{z_j}Q_j-type)·x_{j+1}, a BCH comparison controlled only through r_j(z) and gradients at the weight
L^{k-1-j}. (2) The Feynman difference D_ZD_Z^* - J^TΓ^TΓJ is a second-order differential operator X → Y, not a pointwise
multiplier: its source "δ-coefficient × derivative of x" is of (G)/(Pl) type and is listed under (Mult-Y) below.]** **But the transposes
J^T act on sources:** ⟨y, J^{-1}x⟩ for a divergence-form component G is ⟨(J^{-1})^TG, dx⟩ + ⟨G, (dJ^{-1})∧x⟩, and for a
residual component ⟨s, r(J^{-1}x)⟩ = ⟨s, J'r(x)⟩ + ⟨s, [r, J^{-1}]x⟩; the second terms are plain level-l currents of
coarse size ≤ Cδ||y||_Y. Their representation in Y (and (W-lin) on them) is the input
- **(Mult-Y)** [GAP-1 family]: plain level-l currents of the form (coefficient field of 𝔐^∇-size δ) × (a Y-source) are
  represented in Y with norm ≤ C_Yδ||y||_Y, and (W-lin) holds on them. **[RBB4-fix RS4-3: (Mult-Y) also covers the
  Feynman-difference sources (δ-coefficient × derivative of x).]**
It is the same representability that (W-comm)'s plain commutator rows require (RW∇-F4; BL-6 (b) refutes the (Pl) slot
as written), so it holds in any norm pair in which (W-lin) + (W-comm) are jointly established for the plain rows of
"smooth coefficient × source" type; it is not implied by (W-comm) as literally stated (scalar cutoffs only). Given
(Mult-Y): 𝓛_Z^{-1}π = J_z^{-1}(𝓛 + D𝔑(z) + Δ_z)^{-1}(J_z^{-T}π) with ||𝓛^{-1}πΔ_z||, ||𝓛^{-1}πD𝔑(z)|| ≤ G(C_N(2δ + ε) + Cδ) ≤ ¼ for δ,
ε small, so **(W-lin)_Z with G_Z ≤ 2G(1 + C_Xδ)(1 + C_Yδ)** (Neumann series); (f)_Z: 𝔑_Z(x) = J(x)^T∇E(β_z(x)) - 𝓛_Zx - g_Z is
holomorphic with the (f) bounds on halved balls, constants ×2, by the same (Mult-Y); (W-comm)_Z: (W-comm) plus the
δ𝓛-row of §12.2 (covector multiplication; (Mult-Y)); (E3^∇)_Z: in (E3^∇)'s status (ARGUED). (I-id)_Z: Theorem BA's
solution x(B) and the critical point of E_Z near 0 lie on the same gauge orbit of critical points of 𝔉_k (the two Feynman
conditions Γ and D_Z^* select different representatives; local uniqueness modulo gauge is (FP♯')-type), so 𝔉_k agrees:
ARGUED. ∎

### 13.6 Theorem GI-cov: PROVEN as an implication
Conventions: Ad_ĝ as in 13.4 (on displacements and sources); P_□y := ψ_□·Ad_{ĝ_□}^{-1}ι^*𝓖_□ι_*Ad_{ĝ_□}M_{χ_□}y,
R_□y := -Ad_{ĝ_□}^{-1}ι^*C^♯_{ψ_□}(𝓖_□ι_*Ad_{ĝ_□}M_{χ_□}y), 𝓖_□ := 𝓛_□^{-1}π on 𝕋_□.
*Step 1 (the frame transplant is exact).* By (CovLift) (i) with h = g_□ (extended outside Ω_□ arbitrarily; by (ii) nothing
below depends on the extension), Z^sm(V)^{ĝ_□} = Z^sm(V^{g_□}); V^{g_□} = e^{b_{Ω_□}} on Ω_□ = □^{(R+6+r_Z)}; by (ii)-(iii)
Z^sm(V^{g_□}) = ι^*Z^sm(e^{b̃_□}) on □^{(R+6)}. So on □^{(R+6)} the global operator at Z^sm(V), read in the frame ĝ_□, coincides
with 𝓛_□ (densities read the background within 3): §10.7 Step 1 (with the RW3-2 x''-argument) applies verbatim in the frame
and gives 𝓛_{Z^sm(V)}P = π(1 - R). (T^cov_W = 3R + 14 + 2r_Z makes Ω_□ embed **[RBB4-fix RS4-1: 4R + 14 + 2r_Z for product
partitions, box sides < 2R]**.)
*Step 2 (covariance).* Let h be a level-k gauge, ĥ := ĥ(h, V), c := h(root_□). Lemma GI-frame (a): g_□(V^h) = h^{-1}g_□(V)c,
b_{Ω_□}(V^h) = Ad_{c^{-1}}b_{Ω_□}(V), hence b̃_□(V^h) = Ad_{c^{-1}}b̃_□(V), Z^sm(e^{b̃_□(V^h)}) = Z^sm(e^{b̃_□(V)})^c ((CovLift) (i),
ĥ(c, ·) = c) and 𝓛_□(V^h) = Ad_c^{-1}𝓛_□(V)Ad_c (constant-gauge covariance, (W-loc) (iv)). The cocycle gives
ĥ·ĝ_□(V^h) = ĥ(h·g_□(V^h), V) = ĥ(g_□(V)c, V) = ĝ_□(V)·ĥ(c, V^{g_□(V)}) = ĝ_□(V)c, i.e. the frame of V^h sees Ad_ĥ-transformed
objects exactly as the frame of V sees the originals, up to the constant c, which commutes through 𝓖_□. Hence
P_□(V^h) = Ad_ĥP_□(V)Ad_ĥ^{-1} and the same for R_□ (ψ_□, χ_□ scalar). **Without the cocycle** ĥĝ_□(V^h) and ĝ_□(V)c differ by an
element of the stabiliser of Z^sm(V), which need not extend to a stabiliser of the local-torus background: GI-F2 OCCURS
in that case, and the cocycle is what removes it. **[RBB5-fix RS5-1: GI-F2 cannot occur for any lift that is orbit-covariant
at level 0 (Lemma CL-uniq, 16.11): the two gauges agree at level-k sites and stabilise Z^sm(V), hence coincide; the cocycle
is automatic.]**
*Step 3 (fixed point and energies).* 𝐈(s), 𝐑(s), 𝐏(s) inherit the covariance (scalar weights), so 𝐊(s)(V^h) = Ad_ĥ𝐊(s)(V)Ad_ĥ^{-1}
componentwise; g_{Z^ĥ} = Ad_ĥg_Z and 𝔑_{Z^ĥ}(Ad_ĥx) = Ad_ĥ𝔑_Z(x) (E_Z is a sum of chain-gauge-invariant densities, including
the background-Feynman density ½|D_Z^*x|²(site), which is invariant under the joint action). So Φ_s(V^h) = Ad_ĥ∘Φ_s(V)∘Ad_ĥ^{-1};
the r_s-ball is defined in |||·|||_{𝔐^∇_Z}, which Ad_ĥ maps onto the ball at V^h (Lemma GI-norm (a)); uniqueness gives
**𝐀(s)(V^h) = Ad_ĥ𝐀(s)(V)**. Each density D(u; V) (at e^uZ^sm(V)) satisfies D(Ad_ĥu; V^h) = D(u; V), so 𝔉_D(S_Q𝐀), 𝔈_Q,
ΔE_X(s) and R(X) are invariant; E^cov_∅(V) = Σ_DD(0; V) with D(0; V) = density at Z^sm(V), invariant and depending on V within
3 + r_Z of its base. *The class* {V : (CovLift) (iv) and the background hypotheses hold at Z^sm(V) on 𝕋 and on the local
tori} is defined by covariant statements (Lemma GI-norm (a)), hence gauge invariant. ∎
*Model check.* bb4 B (SU(2) covariant Laplacian with mass and quartic term, background given, so (CovLift) is not
involved): B-1 parametrix identity 1.8e-15 (frame and frame-free, U and U^h); B-2 covariance of P_□, R_□ under a Haar-random
gauge 3.7e-15, 1.1e-14; B-3 walk inverse 1.6e-15; B-4 ΔE(s) invariant to 3.3e-16 (relative) at three random s and s ≡ 1, and
ΔE(1) = E(φ*) - E(0) to 6.0e-16; B-5 the two-cube polymer R(X) = -0.1707 invariant (defect 0). B-6 (pre-registered witness
for the frame-free transplant) FAILED as a prediction: the non-invariance was 2.1e-10 (ΔE) and 2.2e-12 (R(X)), below the
thresholds; diagnostic D2 (post hoc): it is 2.1e-10, 1.9e-5, 1.3e-2 at μ² = 1, 0.25, 0.05, while the frame version stays
≤ 2.1e-14. Reading: the gauge dependence of a frame-free transplant sits at the transplant cut (distance R + 6 from the box)
and reaches the pieces only through the decay of the local inverse from the cut, which is O(1) as the mass goes to 0; the
frame route removes it exactly.

### 13.7 Theorem BB-gi_k (on 𝒞_glob): PROVEN as an implication — **[post-proof correction: hypotheses include (Mult-Y)]**
Take ε ≤ ε_gi with ε_gi small enough that (1) 4C_F(Ω_□)ε ≤ ε_Z and C_sm·4C_F(Ω_□)ε ≤ δ_GI (the smallness at which GI-pert's
Neumann series converges with G_Z ≤ 2G(1 + C_Xδ)(1 + C_Yδ) and ε^Z_W ≤ 2ε_W, the δ𝓛-row included), on every local torus
(b̃_□ is sup-small on all of 𝕋_□: 0 off the embedded region) and on 𝕋 (C_smε ≤ δ_GI in the global gauge); (2) ε ≤ ε_mix,k(s̄)
with BB-mix_k's constants doubled. Then: Lemma GI-frame + (CovLift) (iv) give the 𝔐^∇-smallness of the backgrounds; GI-pert
(with (Mult-Y)) gives (W-lin)_Z on the local tori, (W-comm)_Z, (f)_Z, (E3^∇)_Z, (I-id)_Z; Theorem GI-cov Step 1 and the
proof of Theorem RW^∇_k (Steps 2-5 unchanged; bounds ×2) give (H-RW^∇)_k for Construction BB-bond_k^cov; the proof of Theorem
BB-mix_k (§10.8) runs verbatim with g_Z, 𝔑_Z, E_Z, except that Lemma W-grad0 (a trivial-chain statement) is replaced by
(CovLift) (iv)'s ||g_Z||_Y ≤ C_g·C_Fε and a local pairing bound |Σ_{D∈𝒟_Q}⟨∇D(0), u⟩| ≤ C_pair|Q^{(3)}|·||g_Z||_Y||u||_X (Lemma
W-pair for the residual components, PROVEN; for the (G), (P0), (Pl) components, the per-coarse-volume pairing count of lane
A's normalisations: ARGUED), giving C^cov_E := C_pairC_gC_Fε(M_c + 6)⁴σr_s + C_3(M_c + 6)⁴(σr_s)³ (×2⁴ with product
partitions); R(X) depends on V on X^{(8 + r_Z)}. Theorem GI-cov makes every R(X) locally gauge invariant, and the whole
statement holds on the gauge saturation of 𝒞_glob(ε). ∎ **[RBB6-fix RS6-4 (c): with (CovLift) = Z^{KΠ}, the extension to the
gauge saturation is by invariance: two 𝒞_glob(ε) representatives of one orbit differ by a gauge with O(ε) neighbouring root
differences, where KΠ's covariance applies (REVIEW_BFT_B_S6 D.7); the activities are defined on the saturation by
R(X)(V^h) := R(X)(V), and locality is inherited by the same argument.]**
**Relative to Theorem BB-mix_k's hypothesis set, the new inputs are (CovLift) (structural, OPEN) and (Mult-Y)
(representability, GAP-1 family) — not one, as pre-stated [post-proof correction].** **[RBB4-fix RS4-7 (binding): the
full input list is: BB-mix_k's hypotheses (pure background-Feynman form) + (CovLift) [OPEN] + (Mult-Y) [GAP-1 family, OPEN]
+ **(Pair-loc)** [the local pairing bound above: PROVEN for residual components (W-pair), ARGUED for (G), (P0), (Pl)] +
(I-id)_Z [ARGUED].]** The pure (background-)Feynman operator
is assumed (RW3-4); in the hard slice the same proof runs only with a background-covariant local slice, see 13.8.

### 13.8 Proposition GI-off (outside 𝒞_glob): ARGUED
On BFT's class (plaquettes ≤ ε, any torus side ≥ T_0; holonomies and torons allowed): (1) frames: Lemma GI-frame (b) gives
sup-small frame data on every Ω_□ from the curvature alone (no global gauge is used); (2) backgrounds: (CovLift) (iv) on
each Ω_□ gives the 𝔐^∇-smallness of Z^sm(V) in each frame; (3) the background hypotheses on the local tori follow from GI-pert
applied in each local torus's own global gauge (b̃_□ is sup-small on all of 𝕋_□), with (Mult-Y); (4) the global inverse is
built from the local tori alone (§10.7 Step 4), so global holonomies and torons do not enter the walk expansion; (5) the
fixed point exists and is unique in the covariant ball (13.6 Step 3); what is not available off 𝒞_glob is (I-id): that this
critical point is the one defining E_k^br (lane A's BFT-0 off 𝒞_glob; Balaban convention). **[RBB6-fix RS6-4 (d): the Karcher-glued
Z^{KΠ} (§18-§19) does not supply (CovLift) on this class: CL-F4 OCCURS (the corner normal forms differ by coarse transports);
the wall is named (KΠ-off); §22 gives the cut-off gluing Z^off for it (Theorem KΠ-off). [RBB7-fix RS7-1: planned at the time of this tag, Step 1 10:23; proof written 10:38]]** Also needed: (SL-cov), read as
"lane A's estimates hold for the background-Feynman operator ½||D_Z^*x||²" (covariant and local by construction), or, in a
slice, a background-covariant local slice (the tent construction with Z-transported path integrals, C^{1,1} tents; 13.2's
remark) **[RBB4-fix RS4-4: a background-covariant elliptic slice with C^{2,α} tents, i.e. S_E of §16 with Z-covariant
differences; not the tent-axial construction]**. Relation to lane A's package: (UHL)/LR-grad (lane A's LRL now) is one route to (CovLift) (iv) (lane A's ARGUED
"Z^sm = (UHL) on overlapping patches glued by BA-11"); MSG gives chain-level sup frames. So off 𝒞_glob, (BB-gi)_k and the
BFT-4 polymer bound reduce to (CovLift), (Mult-Y), (SL-cov) and (I-id) off 𝒞_glob [argued; not written as a proof].

### 13.9 Corollary BFT4-poly^gi_k: PROVEN as an implication (of Theorem BB-gi_k)
E_k^br = E^cov_∅ + Σ_XR(X) (Theorem BB-mix_k (ii) for the covariant construction). E^cov_∅ = Σ_DD(0; V) is a sum of local
gauge-invariant densities (13.6), S_W of gauge-invariant plaquettes; assigning each to the cube of its base point makes
R^gi_k := (E^cov_∅ - S_W) + Σ_XR(X) a polymer sum whose pieces are all locally gauge invariant, holomorphic on the polydisc
((CovLift) (v)), with ||R^gi_k||_𝒜 ≤ 2e^{m_0}C^cov_R + C^cov_∅, C^cov_R := 2^{40}C^cov_E, C^cov_∅ := e^{m_0}(2M_c)⁴·(number of
densities per coarse cell)·sup_𝒫|D(0; ·)| (finite by holomorphy on a polydisc), k-uniformly. R^gi_k is bounded, not claimed
small relative to S_W; c_k = 1 needs BB-4♮'s m > 0 inputs. ∎

### 13.10 Proposition CovLift-status: ARGUED
| candidate for Z^sm | covariant | local | 𝔐^∇-small | verdict |
|---|---|---|---|---|
| corner lift U^(0) (U0, TOWER-VAR (b)) | yes (block-constant ĥ) | finite range | no: L^{2(k-j)}ε (REVIEW_BFT_B_S3 Part E) | fails smallness |
| linear smooth lift exp(𝓘B) in a global gauge | constants only | finite range | yes | fails covariance (RW∇-F2 again) |
| frame-wise smooth interpolation, glued across overlaps | to first order | finite range | yes inside frames | GI-F3: transition cocycle exact only at first order (BCH); the O(ε²) mismatch is a jump, coarse gradient ~ L^{k-j}ε² [argued] |
| block-constant extension with covariant intra-block interpolation | yes | finite range | no: interface curvature O(ε) on fine plaquettes, coarse ~ L^{2(k-j)}ε [argued] | fails smallness |
| variational (minimiser of a covariant constrained functional, Balaban's U(V)) | yes (uniqueness) | exponentially, not finite range | needs BFT-1-type regularity | finite range needs the lift's own covariant localisation (Balaban: inductively over RG steps) |
| inductive single-level lift (MSG-like recursion, coarse sup contracting by 1/L) | if each step is | finite range | needs a C^{1,α}-consistent single-level step so constants do not multiply over levels | reduces (CovLift) to a single-level covariant C^{1,α} interpolation (CovLift_1); a Lüscher-type covariant interpolation with transition functions [from memory, CMP 85 (1982); not read] is smooth inside cells but, as far as known here, only continuous across faces |
(CovLift) is OPEN. The most concrete remaining routes: (CovLift_1) + induction; or the variational lift with an inductive
(over k) covariant localisation, which is Balaban's architecture and would make (CovLift) part of the induction rather than
an input.
**[RBB4-fix item 8: (a) seventh candidate (REVIEW_BFT_B_S4 Part E): corner lift + constrained covariant smoothing,
inductively per level — (R1) one-level covariant refinement Z_j := Φ(corner lift of Z_{j+1}), Φ finitely many steps of a
gauge-covariant smoothing descent constrained to M̄_c(Z_j) = Z_{j+1}; (R2) its linearisation a commuting subdivision pair
converging in C^{1,α} with level-uniform constants; (R3) MSG-type BCH absorption per level in C^{1,α}. Status OPEN; tested
and corrected in §16 (Lemma CL-blk: Φ commuting with all chain gauges keeps the corner lift's block-constant extension,
which (iv) excludes; a gauge-smoothing step is needed). (b) MSG's bound |log U^g_i(b)| ≤ C_Mε is in OWN units: in the
coarse units of 𝔐^∇ it allows L^{k-j}C_Mε; MSG gauges a given chain, is frame-dependent, and its Q1-Whitney reference field
is only Lipschitz across faces. (CovLift) is not a corollary of MSG plus smoothing.]** **[RBB5-fix RS5-9 (disclosure): the
words "tested and corrected in §16" in this tag were written at Step 1 of session 5 (08:26), before bb5 ran and before §16
existed; they are a forward reference. CL-blk itself was pre-stated in §15 (08:25:04).]**

## 14. Session-4 check record, outcome and notes for other files (written after §13)

**Check bb4** (criteria checks/bb4_criteria.md born 07:36:13 UTC; script checks/bb4_models.py born 07:39:19, final bytes
07:40:55; output checks/bb4.out 07:41:10-07:41:22). Runner scratchpad bb4/run_bb4.sh (lock free on arrival; load1 3.67;
memory free 38%; nice 10; thread variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3 without -I; no
`timeout`; no trap; `rmdir` once). 11.5 s wall, peak footprint 780 MB. No process left; no __pycache__ in checks/.
**Verdict: NOT ALL PASS (12/14).**
- **A-1 PASS** (m = 0 regime with coarse mass, sup norms): R·||R_□|| = 3.11, 0.605, 0.159, 0.0364, 0.0106 (R = 6..30);
  G_□ = 5.38 → 8.93 (bounded).
- **A-2 PASS** (prediction RW∇-F5 confirmed): without coarse mass G_□ = 12.1 → 157 (×13), ||R_□|| = 1.80, 1.07, 1.20, 1.26, 1.29
  (no 1/R decay), R·||R_□|| 10.8 → 38.6.
- **B-1..B-5 PASS** (13.6's model check). **B-6 FAIL** (prediction: magnitude too small; diagnostic D2).
- **C-1..C-4, C-6 PASS** (13.2's model check). **C-5 FAIL** (prediction: control plateau not below Π's reach; diagnostic D1).
- Post-hoc diagnostic checks/bb4_diag.py (written 07:44:49 after reading bb4.out; second lock acquisition 07:45:28-07:46:08;
  40.7 s; 146 MB): D1, D2 as quoted in 13.2 and 13.6. Not criteria; the verdict stays 12/14.
- *Reading (measured only).* (A) In a model where the only mass is a coarse-scale (block-average) term — lane A's top
  residual's role — the walk factor of RW^∇_k in unweighted sup norms falls faster than 1/R with G bounded; with no coarse
  mass G grows with the box and the factor stays O(1). So the O(1/R) law needs the uniform G, and in this model the uniform
  G comes from the coarse mass. (B) Frame-transplanted local inverses are exactly covariant and make the bond-family energies
  and a two-cube polymer exactly gauge invariant; a frame-free transplant is not, by an amount that grows as the mass falls.
  (C) The hard-slice parametrix identity and the walk inverse hold exactly in a Feynman-free abelian model with a tent slice.
  Not measured: lane A's norms, k-uniformity, (CovLift), (Mult-Y).

| Item (session 4) | Status | Note |
|---|---|---|
| Binding and cosmetic fixes of REVIEW_BFT_B_S3 (RW3-1..5, BP3-1, BL3-1, item 9, RS3-1..7, m = 0 mechanism) | applied, tagged [RBB3-fix] | W-ls termwise (t_X = 4, t_Y = 6); R ≥ 13 / product partitions; "now a theorem" withdrawn with the gap list |
| Lemma W-gauge0 | PROVEN-HERE | Hessian at the trivial chain annihilates 𝒢_0 (no Feynman term) |
| **Theorem RW^∇_k-Π** (hard slice) | **PROVEN as an implication** of (W-Π), (W-lin-Π), (W-comm), (W-loc) (i), (ii), (iv) | 𝓛_SP^Π = π_S(1 - R^Π), values in S; R ≥ 2r_Π + 8; local tori 3R + 14 + 2r_Π **[RBB4-fix RS4-1: 4R + 14 + 2r_Π with product partitions; RS4-2 gradient reading]** |
| Corollary BB-mix_k-Π | PROVEN as an implication | slice form of BB-mix_k |
| RWΠ-F1 | OCCURS [argued] for S_tent's piecewise-linear tents | repair: C^{1,1} σ-spline tents keep the projection algebra **[RBB4-fix RS4-4: insufficient — C^{2,α} tents needed (C^{1,1} fails [∇^c·]_α by L^{αk}); S_tent fails (W-lin-Π) by LR-grad and plausibly (W-Π) by the axial-flux mechanism; RW^∇_k-Π awaits an elliptic slice (§16: S_E)]** |
| Lemma GI-frame | PROVEN-HERE (unitary) | covariance up to the root constant; sup ≤ 1.011(d - 1)ℓ_Ω·(curvature) |
| Lemma GI-norm | (a) PROVEN-HERE; (b) PROVEN-HERE except the residual term (ARGUED) | covariant norms exactly invariant |
| Lemma GI-pert | PROVEN as an implication **with the added (Mult-Y)** [post-proof correction]; (I-id)_Z, (E3^∇)_Z ARGUED | transposed multipliers produce plain rows (GAP-1 family) |
| Theorem GI-cov | PROVEN as an implication | covariant construction ⇒ every R(X) locally gauge invariant, E^cov_∅ invariant local sum; cocycle removes GI-F2 **[RBB5-fix RS5-1: GI-F2 cannot occur for any lift orbit-covariant at level 0 (Lemma CL-uniq); the cocycle is automatic]** |
| **Theorem BB-gi_k** (on 𝒞_glob) | **PROVEN as an implication** of (CovLift) + (Mult-Y) + BB-mix_k's hypotheses (pure Feynman) | **(BB-gi)_k on 𝒞_glob and its gauge saturation; new inputs: (CovLift) [OPEN], (Mult-Y) [GAP-1 family]** **[RBB4-fix RS4-7: + (Pair-loc) [ARGUED for (G), (P0), (Pl)] + (I-id)_Z [ARGUED]]** |
| Proposition GI-off | ARGUED | off 𝒞_glob: (CovLift), (Mult-Y), (SL-cov), (I-id) off 𝒞_glob; frames need only the sup half **[RBB6-fix RS6-4 (d): Z^{KΠ} does not supply (CovLift) here (CL-F4 OCCURS, Karcher gluing undefined); named wall (KΠ-off), addressed in §22 by Z^off (Theorem KΠ-off) [RBB7-fix RS7-1: planned at the time of this tag, Step 1 10:23; proof written 10:38]]** |
| Corollary BFT4-poly^gi_k | PROVEN as an implication | BFT-4's bounded-polymer clause with locally gauge-invariant pieces, on 𝒞_glob |
| (CovLift) | **OPEN** | Proposition CovLift-status (ARGUED): six candidates; routes (CovLift_1) + induction, or Balaban's inductive variational lift |
| Failure modes | GI-F1 does not occur; GI-F2 occurs without the cocycle **[RBB5-fix RS5-1: cannot occur for any lift orbit-covariant at level 0 (Lemma CL-uniq); the cocycle is automatic]**; GI-F3 occurs [argued]; RWΠ-F1 occurs [argued]; RW∇-F5 occurs in a model (A-2) | |
| bb4 | 12/14: A-1, A-2, B-1..B-5, C-1..C-4, C-6 PASS; C-5, B-6 FAILED as predictions | diagnostics D1, D2 explain both; not repaired |

**What BFT-4 rests on (after session 4).** k = 1: BB-mix′_1 (gauge-invariant pieces, PROVEN). Every k on 𝒞_glob,
bounded polymers: Theorem BB-mix_k / BB-mix_k-Π ⇐ (W-lin), (W-comm), (W-loc) [or the slice versions], (f), (E3^∇), (I-id);
**with locally gauge-invariant pieces:** Theorem BB-gi_k ⇐ the same + (CovLift) + (Mult-Y). The hypothesis set is not
yet jointly satisfiable in one norm pair (RW3-5: GAP 1 vs BL-6 (b); LR-grad, which lane A's LRL is now attacking; the slice
form). Off 𝒞_glob: Proposition GI-off (ARGUED). c_k = 1: BB-4♮'s m > 0 inputs.

## FOR OTHER FILES (session 4; for their owners; not edited)
- **BFT_A (lane A).** (1) RW^∇_k exists in two exact forms: the Feynman form (§10.7) and the hard-slice form (Theorem
  RW^∇_k-Π, §13.2), whose only slice input is (W-Π): a local projection Π with Π - 1 ∈ 𝒢_0 and a k-uniform bound for
  Π(φu), u ∈ S. The mixed form (slice + Feynman terms on residual groups, Theorem BA's hypothesis form) is not covered.
  (2) S_tent's piecewise-linear tents violate (W-Π) in 𝔐^∇ at fine scales [argued, §13.2 remark]; C^{1,1} tents
  χ_X = Π_νσ(|z_ν - c_{X,ν}|/n) keep Π∘Π = Π and Π - 1 ∈ 𝒢_0 (only Σχ_X = 1, χ_X(c_Y) = δ_{XY} are used); worth checking in
  LR-pot / LRL (b)'s slice P_♯. **[RBB4-fix RS4-4: (2) is withdrawn as a repair — C^{2,α} tents are required, S_tent fails
  (W-lin-Π) by LR-grad and plausibly (W-Π) by the axial-flux mechanism; the slice for RW^∇_k-Π and for LRL (b) is the
  elliptic slice S_E of §15-§16.]** (3) Covariant centring (needed for gauge-invariant polymers) adds (Mult-Y): plain rows
  "smooth coefficient × source" from transposed multipliers; if lane A's repair of GAP 1 handles plain rows of that type
  generally, (Mult-Y) is covered. (4) bb4 (A): in a model whose only mass is a block-average term, G is bounded in
  unweighted sup norms and the walk factor falls faster than 1/R; with no coarse mass it does not fall — lane A's uniform G
  at m = 0 should be read as coming from the top residual.
- **REVIEW_S22 Part 5 / BFT-4.** The gauge-invariant bounded-polymer clause at every k on 𝒞_glob is reduced to (CovLift)
  [OPEN] + (Mult-Y) [GAP-1 family] + session 3's hypotheses (Theorem BB-gi_k, Corollary BFT4-poly^gi_k); off 𝒞_glob the
  reduction is ARGUED (Proposition GI-off).
- **HIST (MSG).** Theorem MSG is not needed for the level-k frames (axial frames on boxes of side O(R) suffice, at a cost
  O(R) absorbed by the threshold); MSG's role here would be chain-level frames on the fluctuation side. Corollary MSG-loc (as
  stated) is superseded by MSG-loc' in HIST itself; nothing here uses either.
- **SF.md (L-loc)_k.** With Theorem BB-gi_k the classical pieces of (L-loc)_k can be taken locally gauge invariant (given
  (CovLift), (Mult-Y)); the rate remark of [RBB3-fix] (κ_L ~ log M_c/M_c at m = 0) stands. **[RBB4-fix RS4-7: it stands
  for the unweighted form; the weighted form ((W-lin)_m with the top residual's coarse mass, localised (W-comm)) gives
  κ_L = O(m'_*), see Proposition RATE-m, §16.]** **[RBB4-fix RS4-7: Theorem BB-gi_k also needs (Pair-loc) [ARGUED] and
  (I-id)_Z [ARGUED].]**

# Session 5 (2026-10-28 UTC)

## 15. PRE-STATED (session 5) — statements only; the FIRST edit of session 5 (appended before any [RBB4-fix] edit, before any session-5 proof, criteria file or script). Nothing in §15 cites a result of this session; lane A's estimates enter only as named hypotheses. Proofs follow in §16, later. Exploratory reasoning while reading preceded this append (not recorded), so its only claim is file order.

### 15.0 Settings (definitions)
- **Setting EΠ (elliptic slice).** Setting LIN of BFT_A §7.1 at the trivial chain (su(N) componentwise in an orthonormal
  basis; every map below acts componentwise and real-linearly), d = 4, L ≥ 3 odd, n := L^k, coarse torus side T ≥ 5,
  α ∈ (0, 1) (lane A fixes α = ¼). For a level-k site X with level-0 root c_X:
  - Ñ_X := {level-0 sites z : |z_ν - c_{X,ν}|_T ≤ 2n for all ν} (coarse half-width 2), N_X := the same with n (half-width 1);
  - the **box-Coulomb gauge function** λ^E_X(x) := the unique level-0 function on Ñ_X with λ(c_X) = 0 minimising
    Σ_{b⊂Ñ_X}|x_0(b) + dλ(b)|² (b over level-0 links with both ends in Ñ_X; Neumann condition on ∂Ñ_X), and the
    **box-Coulomb potential** a_X := x_0 + dλ^E_X on the links of Ñ_X;
  - **quintic tents** σ_5(t) := 1 - 10t³ + 15t⁴ - 6t⁵ (0 ≤ t ≤ 1), σ_5(t) := 0 (t ≥ 1), χ^5_X(z) := Π_νσ_5(|z_ν - c_{X,ν}|_T/n);
  - Λ(x) := Σ_Xχ^5_Xλ^E_X(x) (each term extended by 0 off N_X); **Π_E x** := the composite gauge transform of x by λ_0 = Λ(x)
    (x_j ↦ x_j + d ev^{(j)}Λ(x), j < k); **S_E** := {x : Λ(x) = 0}.
- **Norms.** X := lane A's 𝔐^∇ (BFT_A §1.4; four terms per level, including [∇^cx^c_j]_α), m = 0 unless a weight is named;
  ||·||_inv, ||·||_D, ||·||_Y as in BFT_A §7.2 and §9.0 above. Level-0 local quantities on a set A:
  n_A(x) := sup_A|x^c_0| + sup_A|∇^cx^c_0| + [∇^cx^c_0]_{α;A} (Campanato over boxes inside A). For a level-l scalar or form H:
  ||H||_{C^{1,α}} := ||H^c||_∞ + ||∇^cH^c||_∞ + [∇^cH^c]_α (coarse units of its level).
- **Residual-gradient size.** N_res(x) := Σ_{0≤i≤k-2}||r_i(x)||_{C^{1,α}} (r_i a level-(i+1) 1-form, coarse units of level
  i + 1, no extra weight).
- **Gauge-optimal linear constant.** For a torus 𝕋': G_opt(𝕋') := sup_{y≠0}inf{||x||_X : 𝓛x = πy}/||y||_Y (𝓛 the Feynman-free
  Hessian 𝓑 of §12.0 at the trivial chain; πy annihilates 𝒢_0).
- **Root-to-root straight map** Q_ax: (Q_axv)(Y, μ) := the straight level-l line sum of v from the level-l root of Y to that
  of Y + e_μ (level l → l + 1); root-covariant (Q_ax d = d ev). Lane A's Q is the S4'-contour average (also root-covariant).
- **Construction CP (commuting tensor pair).** A 1D ternary-type (dilation L) interpolatory stationary scheme s on Z
  (finite mask, or exponentially decaying), roots at block centres (fine value at the root of block i equals c_i),
  reproducing constants; its derived scheme s^{[1]} on links, defined by Δ_fine∘s = s^{[1]}∘Δ_coarse. The d-dim pair:
  S_0 := s^{⊗d} on scalars; S_1 on μ-links := s^{[1]} in direction μ ⊗ s in the other directions. Linear lift
  Z^lin_j(B) := S_1^{k-j}B (level-k 1-form B), gauge extension ĥ^lin_j(μ) := S_0^{k-j}μ. φ := the basic limit function
  of s.
- **Corner lift (linear)** C: a level-(l+1) 1-form B is placed on every level-l link crossing the face between the blocks of
  Y and Y + e_μ, block-interior links 0 (the linearisation of Lemma U0's U^(0)); C_0 := the block-constant extension of
  scalars. **Φ-chain:** level by level, corner lift followed by N steps of the descent A ↦ A - τ P_c d*dA, P_c the
  orthogonal projection onto ker Q_ax (the linearised constrained covariant smoothing (R1) of REVIEW_BFT_B_S4 Part E).

### 15.1 Elliptic slice: statements (STEP 2)
- **Lemma EP-alg.** Π_E is a linear projection onto S_E; Π_Ex - x ∈ 𝒢_0 for every x; S_E ∩ 𝒢_0 = {0}; Π_E commutes with
  coarse-lattice translations and constant gauges; Π_Ex at a position z depends on x_0 only on B_∞(z, r_Π), r_Π := 4.
  *Planned: PROVEN-HERE* (uses only Σ_Xχ^5_X = 1, χ^5_X(c_Y) = δ_{XY} and λ^E_X(x + dμ) = λ^E_X(x) - μ + μ(c_X)).
- **Lemma EP-int (interior estimates on N_X; margin one coarse unit).** There is C_E = C_E(α, d, L), independent of k, T,
  such that for every x:
  (a) sup_{N_X}|∇^cλ^E_X| + sup_{N_X}|∇^c∇^cλ^E_X| + [∇^c∇^cλ^E_X]^∞_{α;N_X} ≤ C_E n_{Ñ_X}(x), and sup_{N_X}|λ^E_X| ≤ 4C_E n_{Ñ_X}(x);
  (b) for every level-0 function μ: sup_{N_X}|a^c_X| + sup_{N_X}|∇^ca^c_X| + [∇^ca^c_X]^∞_{α;N_X} ≤
  C_E(sup_{Ñ_X}|(x_0 + dμ)^c| + sup_{Ñ_X}|f_0| + [f_0]_{α;Ñ_X}).
  *Planned: PROVEN-HERE* given Lemma LES-div (PROOF [S15], reviewed), with a lattice Caccioppoli inequality and the L²
  projection property of λ^E_X (no box Gaffney inequality, no boundary regularity).
- **Lemma Q-hold.** For 0 ≤ a < b ≤ k and every level-a 1-form v: ||Q^{(a→b)}v||_{C^{1,α}} ≤ C_Q||v||_{C^{1,α}} with C_Q
  depending only on α (via BL-C), for lane A's Q (and for Q_ax, Q_str). *Planned: PROVEN-HERE* (BL-2 (b), translation
  covariance of h^{(a→b)}).
- **Theorem EP-bd ((W-Π) for S_E).** ||Π_Ev||_X ≤ C_Π||v||_X for every v ∈ X, C_Π = C_Π(α, d, L) k- and T-uniform. Hence
  (W-Π) of §12.1 holds for S_E with r_Π = 4 and C_Π(ℓ) := C_ΠC_M^X(ℓ). Weighted: ||Π_Ev||_{X,m} ≤ e^{4m}C_Π||v||_{X,m}.
  *Planned: PROVEN-HERE.*
- **Theorem EP-opt (slice optimality).** For every y ∈ Y and every x with 𝓛x = πy: 𝓛_{S_E}^{-1}π_{S_E}y = Π_Ex. Hence
  G_opt ≤ ||𝓛_{S_E}^{-1}π_{S_E}||_{Y→X} ≤ C_ΠG_opt on every torus: **(W-lin-Π) for S_E ⟺ (H-lin^∇) in some gauge**.
  *Planned: PROVEN-HERE.*
- **Theorem EP-rec (elliptic reconstruction).** For every configuration x (data x_k arbitrary; x_k := 0 for displacements):
  ||Π_Ex||_X ≤ C_rec(||x||_inv + ||x_k||_D + N_res(x)), C_rec k- and T-uniform; weighted with e^{c_rm}, c_r absolute.
  *Planned: PROVEN-HERE* given LES-div, lane A's Lemma Λ, Lemma LR-pot (both CONFIRMED in REVIEW_BFT_A_S3), BL-2, BL-C.
- **Corollary EP-lin.** (W-lin-Π) for S_E on every torus of side ≥ T^Π_W ⇐ **(H-inv+)**: every response x(y) (any
  representative) obeys ||x||_inv + N_res(x) ≤ G_+||y||_Y; then G_Π := C_recG_+. Conversely (W-lin-Π) for any slice gives
  ||x||_inv ≤ 2G_Π||y||_Y and max_i||r_i||_{C^{1,α}} ≤ C_QG_Π||y||_Y. *Planned: PROVEN as an implication.*
- **Corollary EP-LRL(b).** Lane A's LRL (b) (BFT_A l.1346-1349) holds with P_♯ := Π_E ⇐ Proposition W + **(Res-Hölder)_m**:
  N_res,m(y(B_k)) ≤ C||B_k||_{D,m} for the source-free data map. *Planned: PROVEN as an implication.*
  **[RBB5-fix RS5-3: for T ≥ 5 only (S_E needs Ñ_X to embed); LRL (b)'s cases T = 3, 4 are not covered and need a separate
  argument or LRL (b) restated for T ≥ 5. N_res,m := Σ_{0≤i≤k-2}||r_i||_{C^{1,α},m} with lane A's weight w(z) = e^{md(z,X_0)}
  inside the sup, gradient and Campanato terms (§18.0). RS5-4 (b): the weighted constant rests on EP-rec's weighted reach,
  ARGUED (16.6).]**
- **Theorem RW^∇_k-Π(E).** Theorem RW^∇_k-Π (§12.1, with [RBB4-fix RS4-1]) holds for S = S_E: r_Π = 4, R ≥ 16, local tori of
  side 4R + 22 (product partitions; 3R + 22 for T a multiple of M_c), G^Π_P := C_ΠC_M^X(R/4)G_ΠC_M^Y(¼), with (W-Π)
  supplied by EP-alg + EP-bd and (W-lin-Π) by Corollary EP-lin (or EP-opt); weighted form: ε_W gains e^{-m(R/2 - 9)}.
  *Planned: PROVEN as an implication.*
- **Proposition RATE-m (O(1) cluster rate).** Under the weighted (W-lin-Π)_m for S_E (0 < m < m'_*) and a localised (W-comm):
  R_W(s̄) ≤ 18 + (2/m)log(C_Ws̄) and κ_L ≥ m/c with c absolute; the mass is the top residual's (RW∇-F5, REVIEW_BFT_B_S4 Part F).
  *Planned: PROVEN as an implication.*

### 15.2 (CovLift): statements (STEP 3)
- **Lemma CL-uniq (the cocycle is automatic).** If Z is a chain on a connected region and G a chain gauge with Z^G = Z and
  G = 1 at one level-0 site, then G = 1 on the region. Hence for a lift with *orbit covariance* (Z^sm(V^h) = Z^sm(V)^G for some
  chain gauge G restricting to h at level k, and Z^sm(V^c) = Z^sm(V)^c) the extension ĥ(h, V) := G is unique, and the
  cocycle and ĥ(c, ·) = c of (CovLift) (i) hold. *Planned: PROVEN-HERE.*
- **Lemma CL-blk (block-constant extensions are excluded).** If a lift satisfies (CovLift) (i) and (iv) and its extension
  at V = 1, h ↦ ĥ(h, 1), is constant on level-k blocks at some level j < k, then (iv) fails at depth k - j ≥ 1 (the
  pure-gauge input 1^h gives an 𝔐^∇ size ≥ cL^{k-j}||b||_∞). In particular corner lift followed by any refinement commuting
  with all chain gauges fails (iv). *Planned: PROVEN-HERE.*
- **Proposition CL-lin (linearised (CovLift)).** If φ ∈ C^{2,α} with compact support (or exponential decay), the linear lift
  Z^lin of Construction CP satisfies: S_1d = dS_0, ev∘S_0 = 1 (linear orbit covariance with ĥ^lin, linear cocycle);
  Q_ax-consistency (Q_axS_1 = 1, so Q_ax-residuals vanish); finite range r_Z ≤ r_sL/(L - 1); translation covariance; and
  ||Z^lin(B)||_X ≤ C_sm||B||_∞ uniformly in k (with Q_ax residuals); with lane A's Q the residual term obeys
  L^{k-1-j}||r^c_j|| ≤ 2L²||f_j||_∞. *Planned: PROVEN-HERE* given the regularity of φ (a property of one finite mask; bb5
  measures it numerically, which is not a proof).
- **Proposition CL-Φ.** The Φ-chain is linearly covariant with the block-constant extension C_0 (so CL-blk applies to it);
  Z^Φ := Π_E∘(Φ-chain) is linearly orbit-covariant with a smooth extension, and its (iv)-bound reduces by EP-rec to a
  curvature bound ||f_j||_∞ + [f_j]_α ≤ C||B||_∞ and N_res ≤ C||B||_∞ for the Φ-chain. *Planned: PROVEN as an implication.*
- **Proposition CovLift-route.** (CovLift) on 𝒞_glob ⇐ (R1') an exactly orbit-covariant, finite-range one-level refinement
  whose linearisation at the trivial chain is a Construction CP pair with φ ∈ C^{2,α} (or Φ followed by a covariant elliptic
  normal form) + (R3) BCH absorption in C^{1,α}. *Planned: ARGUED* (the nonabelian construction is not given here).

### 15.3 Failure modes (pre-stated)
- **EP-F1** the lattice interior Schauder constant grows with k. Expected: does NOT occur (LES-div is scale-free).
- **EP-F2** the edge/corner singularities of the Neumann box reach the tent support. Expected: NOT (margin one coarse unit).
- **EP-F3** the transition functions λ^E_X - λ^E_Y lose a factor through root-to-root holonomy. Expected: NOT (Lemma Λ).
- **EP-F4** N_res is unbounded for responses (B5'-type obstruction moved into the residuals). Expected: OPEN (lane A).
- **CL-F1** corner lift + gauge-invariant smoothing fails (iv) through the gauge part. Expected: OCCURS (CL-blk).
- **CL-F2** the 4-point local ternary Lagrange mask is not C^{2,α}. Expected: OCCURS [guess]; 6- and 8-point: not [guess].
- **CL-F3** the Q1 (linear/Whitney) pair loses a factor L^{depth} in ∇^c. Expected: OCCURS.

### 15.4 Check bb5 (criteria in checks/bb5_criteria.md, written after this section and before the script)
d = 2 abelian, L = 3, coarse torus side 6, depths 1-5 from a random top 1-form (and a pure-gauge input), sup-normalised.
Pairs of Construction CP from 1D masks: linear (Q1/Whitney), Deslauriers-Dubuc-type ternary Lagrange 4-, 6-, 8-point,
periodic cubic-spline interpolation (global); plus the Φ-chain. Measured per depth in coarse units: sup, gradient sup, an
axis-shift Hölder proxy of the gradient (α = ¼), a C^{1,1} proxy, curvature sup and Hölder proxy. Identities: S_1d = dS_0,
ev∘S_0 = 1, Q_axS_1 = 1, Φ(dμ) = dC_0μ. Trend criteria only; no k-uniform constant is tested.

## 16. Proofs (session 5; appended after §15 (08:25:04 UTC), after Step 1 (08:25:3x-08:26:44) and after bb5 ran (08:28:31-08:28:34))

Post-proof corrections of pre-stated details are marked **[post-proof correction]** where they occur; §15 is not edited.
They are: (1) Lemma EP-int is proved on the larger box N'_X (half-width 3/2), which is what EP-rec uses; (2) the converse
constant in Corollary EP-lin is (C_Q + 1)G_Π, not C_QG_Π; (3) Lemma CL-blk: (iv) fails at every level j with
L^{2(k-j)} > C_sm (so it fails as a k-uniform statement), not at every depth ≥ 1; (4) Proposition CL-lin: with lane A's Q the
residual term is ≤ 2||f_j||_∞ (pre-stated 2L²||f_j||_∞), finite range only for finite masks (the cubic spline is
exponentially local); (5) Lemma CL-uniq has a consequence for GI-F2 (§12.3, §13.6), recorded in 16.11.
Conventions: level-0 own units; coarse ∇^cλ := n·(forward difference) for scalars, x^c_0 = nx_0, f_0 = n²dx_0 (BFT_A §1.3).
-Δ := d*d on scalars; on 1-forms the lattice identity -Δ = d*d + dd* holds componentwise on Z⁴.
**Campanato telescoping (standard; the argument of BL-C, localised).** If H is a lattice function on a region U and
U' ⊂ U with margin 1/4 (coarse), then for z, z' ∈ U' with |z - z'|_∞ ≤ 1: |H(z) - H(z')| ≤ C_T(α, d)([H]_{α;U} + sup_U|H|)|z - z'|^α_∞,
and |H(z) - avg_{Q_r(z)}H| ≤ C_Tr^α[H]_{α;U} for boxes Q_r(z) ⊂ U (nested boxes of side ratio ≤ 2 from Q_r(z) down to one site;
each step changes the average by ≤ 2^{d/2}Osc_2 ≤ 2^{d/2}ρ^α[H]_α; for |z - z'| ≤ 1/8 compare both points with one box of side
2|z - z'| containing them, otherwise use 2 sup). Conversely Osc_2(H; B) ≤ ρ^α[H]^∞_α. Below "C^{1,α}-bounds on a set" means
sup + gradient sup + pointwise Hölder of the gradient there, all coarse units.

### 16.1 Lemma EP-alg: PROVEN-HERE
(a) *Gauge shift.* For a level-0 μ, λ ↦ ν := λ + μ - μ(c_X) is a bijection of {λ(c_X) = 0} onto itself with
x_0 + dμ + dλ = x_0 + dν; so the minimiser for x + dμ is λ^E_X(x) - μ + μ(c_X) (uniqueness: Ñ_X is connected, the functional is
strictly convex modulo constants, and λ(c_X) = 0 fixes the constant). (b) *Tents.* σ_5(t) = 1 - p(t), p(t) := 10t³ - 15t⁴ + 6t⁵,
and p(1 - t) = 1 - p(t), so σ_5(t) + σ_5(1 - t) = 1 on [0, 1]; in one coordinate, a point between adjacent roots c, c + n has
weights σ_5(t), σ_5(1 - t) (t its coarse offset) and all other roots weight 0, so Σ_Xχ^5_X = 1 (product over ν);
χ^5_X(c_Y) = δ_{XY}. σ_5' = -30t²(1 - t)², σ_5'' = -60t(1 - t)(1 - 2t), σ_5''' = -60(1 - 6t + 6t²): σ_5' and σ_5'' vanish at 0 and 1, so
t ↦ σ_5(|t|) (extended by 0) is C^{2,1} with |σ_5'| ≤ 15/8, |σ_5''| ≤ 10/√3, |σ_5'''| ≤ 60. (c) Λ(c_Y) = λ^E_Y(c_Y) = 0 for every Y, so
ev^{(k)}Λ = 0 and Π_Ex - x = DΛ ∈ 𝒢_0. (d) For x' := Π_Ex = x + DΛ, (a) gives λ^E_X(x') = λ^E_X(x) - Λ + Λ(c_X) = λ^E_X(x) - Λ, so
Λ(x') = Σ_Xχ^5_X(λ^E_X(x) - Λ) = 0: Π_E maps into S_E and is the identity on S_E, so Π_E∘Π_E = Π_E. (e) For Dμ ∈ 𝒢_0 (μ = 0 at
level-k sites), λ^E_X(Dμ) = -μ + μ(c_X) = -μ, so Λ(Dμ) = -μ and Dμ ∈ S_E iff μ = 0. (f) Roots, boxes, tents and the order-free
minimisation are invariant under coarse-lattice translations; Π_E acts identically and linearly on each su(N) component in
an orthonormal basis, and a constant Ad is a constant orthogonal matrix on these components, so they commute. (g) Λ(z)
involves only X with |z - c_X|_∞ < 1, and λ^E_X reads x_0 on Ñ_X ⊂ B_∞(z, 3); (Π_Ex)_j at a level-j link reads Λ at its two end
roots (within ρ_j < 1): radius 4. T ≥ 5 makes Ñ_X (side 4 coarse plus one site) embed. ∎

### 16.2 Lemma EP-int: PROVEN-HERE (given LES-div), on N'_X := half-width 3/2 **[post-proof correction: proved on N'_X ⊃ N_X]**
Write Ñ := Ñ_X, λ := λ^E_X, v := x_0|_Ñ, a := v + dλ.
*Step 0 (projection).* a ⊥ {dν|_Ñ} in ℓ²(links of Ñ) (first variation), hence ||a||² + ||dλ||² = ||v||² and ||a|| ≤ ||v + dμ|| for every μ.
*Step 1 (equations).* At every site of Ñ all of whose 2d links lie in Ñ: (d*a)(z) = 0, i.e. -Δλ = Σ_a∂^-_ag_a with g := ∓v (sign
fixed by the d* convention). Differences commute with Δ and ∂^-, so u := ∂_bλ obeys -Δu = Σ_a∂^-_a(∓∂_bv_a) one site further in.
For a: da = dv on Ñ and d*a = 0 at interior sites, so componentwise -Δa_μ = (d*dv)_μ = Σ_ν∂^-_ν(±(dv)_{νμ}) at links whose
2-neighbourhood is interior: divergence form with g = ±dv, h = 0.
*Step 2 (lattice Caccioppoli; routine).* If -Δw = Σ_a∂^-_ag_a on Q_{2r}(z) (own side 2r ≥ 4), then for every constant c,
Σ_{Q_r}|∇w|² ≤ C_1(r^{-2}Σ_{Q_{2r}}|w - c|² + Σ_{Q_{2r}}|g - ḡ|²), C_1 absolute: test with η²(w - c), η = 1 on Q_r, supp η ⊂ Q_{2r-1},
|∇η| ≤ 2/r; summation by parts (ḡ drops out against a compactly supported test function); the discrete product rule
∇_a(η²w')(z) = η²(z + e_a)∇_aw'(z) + w'(z)∇_a(η²)(z), |∇_a(η²)| ≤ (η(z) + η(z + e_a))|∇η|, and Young's inequality.
*Step 3 (scales ≤ 1/8).* Fix z ∈ N'_X and the own box Q_R(z), R := n/4 (coarse 1/4; inside the interior of Ñ, margin ≥ n/4). In
coarse units put H := ∇^c∇^c_bλ = n²∇u, g^c := ∇^cv^c (= n²·own ∂v): LES-div (PROOF [S15]) is homogeneous of degree 2 + α under
this change of units, so for scales ρ ≤ R/4 (coarse 1/16) near z:
  ρ^{-α}Osc_2(H; Q_ρ) ≤ C_α[R_c^{-α}(avg_{Q_{R/4}}|H|²)^{1/2} + [∇^cv^c_0]_{α;Ñ}],  R_c = 1/4.
Caccioppoli (Step 2, w = u, c = 0) and Step 0: avg_{Q_{R/4}}|H|² ≤ C(R_c^{-2}avg_{Q_{R/2}}|∇^cλ|² + sup|∇^cv^c|²), and
avg_{Q_{R/2}}|∇^cλ|² ≤ (|Ñ|/|Q_{R/2}|)avg_Ñ|∇^cλ|² ≤ C_d avg_Ñ|v^c|² (∇^cλ = n dλ, v^c = nv, Σ|dλ|² ≤ Σ|v|²). Hence
[H]_{α; scales≤1/16, near N'_X} ≤ C n_Ñ(x).
*Step 4 (sups and all scales).* |H(z)| ≤ (avg_{Q_{R/4}(z)}|H|²)^{1/2} + C_TR_c^α[H]_α ≤ C n_Ñ(x) (telescoping); scales in (1/16, 1]:
ρ^{-α}Osc_2 ≤ 2·16^α sup|H|; pointwise Hölder by telescoping. |∇^cλ(z)| ≤ (avg_{Q}|∇^cλ|²)^{1/2} + (coarse ℓ¹ diameter of Q)·sup|H| ≤
C n_Ñ(x) (fine-step paths, each step changing ∇^cλ by ρ_0|H|); |λ| ≤ 4 sup|∇^cλ| on N_X (λ(c_X) = 0, ℓ¹ distance ≤ 4; ≤ 6 on N'_X).
*Step 5 (part (b)).* The same with u := a_μ, g = ±dv: Campanato of ∇^ca^c ≤ C[(avg|∇^ca^c|²)^{1/2} + [f_0]_α], Caccioppoli
avg|∇^ca^c|² ≤ C(avg_Ñ|a^c|² + sup|f_0|²), and avg_Ñ|a^c|² ≤ avg_Ñ|(v + dμ)^c|² (Step 0) for every μ; then Step 4 for a^c.
*Small k.* LES-div needs R ≥ 16, i.e. n ≥ 64. For the finitely many k with L^k < 64 the maps x_0|_Ñ ↦ λ|_{N'_X}, a|_{N'_X} are fixed
linear maps between finite-dimensional normed spaces (independent of T, the box being local): bounded by some C(L, k).
C_E := the maximum of these and the LES-div-based constant; it depends on (α, d, L) only. **EP-F1, EP-F2 do not occur:** no
boundary regularity is used (margin 1/2 coarse to ∂Ñ_X), and no box Gaffney inequality (Step 0 replaces it). ∎

### 16.3 Lemma Q-hold: PROVEN-HERE (C_Q ≤ 7C_T + 4)
Let s := L^{b-a}, ρ_a = L^{-(k-a)}, ρ_b = sρ_a. BL-2 (b) (PROVEN in BFT_A): Q^{(a→b)} = Q_str^{(a→b)} - d∘h^{(a→b)}, |h^{(a→b)}w| ≤ 2(s - 1)||w||_own.
*Straight part.* (Q_strv)(Y, μ) = s^{-3}Σ_{transverse}Σ_{i<s}v (own), so (Q_strv)^c = L^{k-b}·s·avg(v) = avg(v^c): a probability average of
v^c over s⁴ translates by offsets in [0, ρ_b)⁴. Its sup is ≤ ||v^c||; its level-b coarse gradient is the same average of the
difference quotients of v^c at step ρ_b, i.e. of averages of the fine ∇^cv^c (≤ ||∇^cv^c||); differences at distance δ of an
average of translates are averages of differences at distance δ, so [∇^c(Q_strv)^c]^∞_α ≤ [∇^cv^c]^∞_α, and Osc_2 ≤ ρ^α[·]^∞.
*Gauge part.* h^{(a→b)} = Σ_iev^{(i+1→b)}∘h_i∘Q_str^{(a→i)} is covariant under the level-b translations: (hv)(Y + e) = h(τ_ev)(Y), τ_e the
shift by s level-a steps. Fine own differences of v are ρ_a²∇^cv^c. So |(dhv)^c(Y, μ)| = L^{k-b}|h((τ_μ - 1)v)| ≤
ρ_b^{-1}·2s·sρ_a²||∇^cv^c|| = 2ρ_b||∇^cv^c||; its coarse gradient in direction ν is ρ_b^{-2}h((τ_ν - 1)(τ_μ - 1)v), and
|(τ_ν - 1)(τ_μ - 1)v| ≤ s·ρ_a²·ρ_b^α[∇^cv^c]^∞_α (s fine μ-differences, each differenced at distance ρ_b), so it is ≤ 2ρ_b^α[∇^cv^c]^∞_α;
its Campanato at scales ρ ≥ ρ_b is ≤ ρ^{-α}·2·sup ≤ 4[∇^cv^c]^∞_α. With [·]^∞ ≤ C_T([·]_α + sup):
||Q^{(a→b)}v||_{C^{1,α}} ≤ (7C_T + 4)||v||_{C^{1,α}}. The same holds for Q_str, and for Q_ax (one straight line: an average of
translates, no gauge part). ∎

### 16.4 Theorem EP-bd: PROVEN-HERE
Λ = Σ_Xχ^5_Xλ^E_X with at most 16 non-zero terms at each point (the corners of the coarse cell), each supported in N_X. By
16.1 (b) ||χ^5_X||_{C^{2,1}} ≤ C_χ (absolute, products of four σ_5-factors), and by EP-int (a) ||λ^E_X||_{C^{2,α}(N_X)} ≤ 6C_En_{Ñ_X}(v)
(sup, gradient, second differences and their pointwise Hölder). The discrete Leibniz rule for first and second differences
(shifted arguments) and the product rule for pointwise Hölder seminorms give ||Λ||_{C^{2,α}} := sup|∇^cΛ| + sup|∇^c∇^cΛ| +
[∇^c∇^cΛ]^∞_α ≤ 16·4C_χ·6C_E·sup_Xn_{Ñ_X}(v) ≤ C'||v||_X (n_{Ñ_X} ≤ the level-0 part of ||v||_X; Campanato inside Ñ_X ≤ global).
Level j: (d ev^{(j)}Λ)^c(b) = the difference quotient of Λ between the two end roots (step ρ_j), an average of fine ∇^cΛ;
its level-j gradient is an average over a ρ_j-grid of fine second difference quotients; its Hölder seminorm is bounded by
that of ∇^c∇^cΛ (averages of translates, as in 16.3). So ||(d ev^{(j)}Λ)_j||_{C^{1,α}} ≤ 2||Λ||_{C^{2,α}} for every j. Residuals:
r_i(Π_Ev) = r_i(v) (Q∘d = d∘ev; r_{k-1} also, since ev^{(k)}Λ = 0). Hence **||Π_Ev||_X ≤ (1 + 2·3C')||v||_X =: C_Π||v||_X** (the
factor 3 for the three C^{1,α} summands of 𝔐^∇ at each level), uniformly in k and T. Weighted: everything used at a link
lies within distance 4, so ||Π_Ev||_{X,m} ≤ e^{4m}C_Π||v||_{X,m}. With EP-alg and W-mult, (W-Π) holds for S_E with r_Π = 4 and
C_Π(ℓ) = C_ΠC_M^X(ℓ) (for every v, in fact; u ∈ S is not needed). **[RBB5-fix RS5-4 (c): EP-bd is a theorem about the
linear slice at the trivial chain; the background (Z-covariant, nonlinear) version needed by 13.8 / GI-off is (N1) of
CovLift-route, OPEN (session 6: §18.2, §19).]** ∎ **Contrast with S_tent:** the axial gauge function is
not bounded on C^{1,α} (LR-grad's L^{k(1-α)}), while the box-Coulomb gauge gains one derivative (Schauder) and the quintic
tents cost none.

### 16.5 Theorem EP-opt: PROVEN-HERE
*Kernel.* 𝓑(x, x) = ||dx_0||² + Σ_lκ_l||r_l(x)||² at the trivial chain (x_k := 0; componentwise). 𝓑(x, x) = 0 forces dx_0 = 0, so
x_0 = dλ_0 + h with h a constant 1-form, and r_l = 0 for all l, so 0 = x_k = Q^{(0→k)}x_0 = d ev^{(k)}λ_0 + L^kh (Q maps constants to L
times themselves, BL-2 (b)); d ev^{(k)}λ_0 has mean zero, so h = 0 and ev^{(k)}λ_0 is constant; subtracting it, x = Dλ_0 ∈ 𝒢_0.
Conversely 𝒢_0 ⊂ ker 𝓑 (Lemma W-gauge0). *Solvability.* πy annihilates 𝒢_0 (lane A's sources: ⟨G, d dλ⟩ = 0, r(Dλ) = 0, and
co-closed plain currents ⟨j, d ev λ⟩ = ⟨d*j, ev λ⟩ = 0), so 𝓛x = πy has solutions, unique modulo 𝒢_0. *Identification.* For a
solution x, Π_Ex ∈ S_E and Π_Ex - x ∈ 𝒢_0, so 𝓑(Π_Ex, w) = ⟨πy, w⟩ **[RBB5-fix RS5-2: ⟨πy, w⟩, not ⟨y, w⟩]** for every w, in particular w ∈ S_E. 𝓛_{S_E} is injective: if
u ∈ S_E and 𝓑(u, w) = 0 for w ∈ S_E, then for all w ∈ X (w - Π_Ew ∈ 𝒢_0 ⊂ ker), so u ∈ 𝒢_0 ∩ S_E = {0}. Hence
𝓛_{S_E}^{-1}π_{S_E}y = Π_Ex for every solution x, and ||Π_Ex|| ≤ C_Π inf_x||x|| ≤ C_ΠG_opt||y||; conversely Π_Ex is itself a
solution, so G_opt ≤ ||𝓛_{S_E}^{-1}π_{S_E}||. ∎ So **for S_E, (W-lin-Π) is exactly lane A's (H-lin^∇) in the best gauge**, up to
C_Π: the slice adds nothing and loses nothing.

### 16.6 Theorem EP-rec: PROVEN-HERE (given LES-div, Lemma Λ, LR-pot, BL-2, BL-3-free)
*Level 0.* For a μ-link b = (z, z + e_μ), from Σ_Xχ^5_X = 1 (as in BFT_A 13.12):
  (Π_Ex)_0(b) = Σ_Xχ^5_X(z + e_μ)a_X(b) + Σ_X(λ^E_X(z) - λ^E_*(z))dχ^5_X(b),
X_* any root with z ∈ N_*, using Σ_Xdχ^5_X(b) = 0. On a coarse cell K only its 16 corners carry tents; for z, z' at ∞-distance ≤ 1
the cells share a corner, which is taken as X_* for both, and every point used lies in N'_X ∩ N'_* for the X involved (if a
term's tent vanishes at one of the two points, compare instead with the point where the segment leaves supp χ^5_X: the term
and its first derivatives vanish there, and that point is within distance 1 of c_* and in N_X).
- a_X: EP-int (b) with μ := the tent-axial gauge function of S_tent, for which (x_0 + dμ) = (P_tentx)_0 and, by LR-pot (BFT_A
  13.12, CONFIRMED), sup|(P_tentx)^c_0| ≤ 155||f_0||_∞ + 8||x_k||_D + 40Σ_i||r^c_i||_∞. So ||a_X||_{C^{1,α}(N'_X)} ≤ C_E·A(x),
  A(x) := 156||f_0||_∞ + [f_0]_α + 8||x_k||_D + 40Σ_i||r^c_i||_∞.
- λ^E_X - λ^E_*: its coarse gradient is (a_X - a_*)^c (C^{1,α}-bounded by 2C_EA(x)); its value at c_* is λ^E_X(c_*) = Σ_π(a_X - x_0) along
  an axial path π from c_X to c_* made of ≤ 4 straight root-to-root segments (inside N'_X), so |λ^E_X(c_*)| ≤ 4sup|a^c_X| + 4max|Λ_root|,
  Λ_root lane A's root-to-root holonomy, and Lemma Λ (C_Λ = 10, CONFIRMED): |Λ_root| ≤ ||x_k||_D + 5Σ_i||r^c_i||_∞ + 10||f_0||_∞.
  **EP-F3 does not occur.** Hence ||λ^E_X - λ^E_*||_{C^{2,α}(N'_X∩N'_*)} ≤ C(A(x) + ||x_k||_D).
- Products with χ^5_X ∈ C^{2,1} and with (dχ^5_X)^c = ∇^cχ^5_X ∈ C^{1,1} (this is where C^{2,α} tents are needed), ≤ 16 terms:
  ||(Π_Ex)_0||_{C^{1,α}} ≤ C_0(||f_0||_∞ + [f_0]_α + ||x_k||_D + Σ_i||r^c_i||_∞) ≤ C_0'(||x||_inv + ||x_k||_D), using
  Σ_i||r^c_i||_∞ ≤ (L/(L - 1))||x||_inv (BFT_A 13.13).
*Levels j ≥ 1.* r_i(Π_Ex) = r_i(x), and x_{i+1} = Q_ix_i - r_i telescopes to (Π_Ex)_j = Q^{(0→j)}(Π_Ex)_0 - Σ_{i<j}Q^{(i+1→j)}r_i(x). Lemma Q-hold:
||(Π_Ex)_j||_{C^{1,α}} ≤ C_Q||(Π_Ex)_0||_{C^{1,α}} + C_QΣ_{i≤j-1}||r_i||_{C^{1,α}} ≤ C_QC_0'(||x||_inv + ||x_k||_D) + C_QN_res(x).
*Residual terms* of 𝔐^∇: L^{k-1-j}||r^c_j||_∞ ≤ ||x||_inv. Collecting: **||Π_Ex||_X ≤ C_rec(||x||_inv + ||x_k||_D + N_res(x))**,
C_rec := 3C_QC_0' + C_Q + 1, k- and T-uniform. *Weights:* every quantity used for a link at b lies within coarse distance 12
(LR-pot) + 8 (Q^{(0→j)}) + 4 (Π_E) of b, so the weighted form holds with c_r := 24 [crude]. **[RBB5-fix RS5-4 (a): this weighted constant rests on the reach of
LR-pot (≤ 12) and of Lemma Λ (≤ 8) per output point; lane A's texts state them (BFT_A 13.12 *Weights*, l.1144-1145; 13.11,
"all loops lie in B(X) ∪ B(X + e_μ)", l.1119) but they were not checked as proven in REVIEW_BFT_B_S5: ARGUED. RS5-4 (c):
EP-rec, like EP-bd, concerns the linear slice at the trivial chain; the Z-covariant (background) version is (N1).]** ∎ **Reading.** The gauge-variant part
of 𝔐^∇ is controlled in S_E by gauge-invariant quantities alone; the only extra one is N_res, which the B5' counterexample
(BFT_A [RBA3-fix] B5') shows cannot be dropped (a checkerboard residual r_{j-1} = dψ has ||x||_inv small and N_res large).
EP-F4 is therefore the remaining content, and it is gauge invariant.

### 16.7 Corollary EP-lin: PROVEN as an implication
By EP-opt, 𝓛_{S_E}^{-1}π_{S_E}y = Π_Ex(y) for any representative; by EP-rec with x_k = 0, ||Π_Ex(y)||_X ≤ C_rec(||x||_inv + N_res(x)) ≤
C_recG_+||y||_Y. Converse: for any slice and its solution x, ||x||_inv ≤ 2||x||_X ≤ 2G_Π||y|| (BFT_A §7.2) and
||r_i||_{C^{1,α}} ≤ ||Q_ix_i||_{C^{1,α}} + ||x_{i+1}||_{C^{1,α}} ≤ (C_Q + 1)G_Π||y|| **[post-proof correction: (C_Q + 1), not C_Q]**. ∎
(The converse bounds the max over i; N_res is a sum. For responses with geometric residual decay, BL-4 type, the two agree
up to a constant; in general the gap is the sum versus the max.)

### 16.8 Corollary EP-LRL(b): PROVEN as an implication
For the source-free data map y(B_k) (x_k = B_k), Π_E leaves B_k unchanged (ev^{(k)}Λ = 0) and is a projection with the
properties LRL (b) asks (EP-alg). Weighted EP-rec, Proposition W (BFT_A 13.9, PROVEN: ||y||_{inv,m} ≤ G_D(m)||B_k||_{D,m}) and
(Res-Hölder)_m give max_j[...]_m ≤ e^{c_rm}C_rec(G_D(m) + 1 + C)||B_k||_{D,m}. Residual-type sources enter through x = y - τ and
BL-3 as in Corollary FP. ∎ **So LRL (b) ⟸ (Res-Hölder)_m alone**; REVIEW_BFT_A_S4 Part 6 items 1 (slice), 2 (interior C^{1,α}),
3 (patching) and 5 (weights) are discharged here, and item 4 (level consistency) is exactly (Res-Hölder)_m plus Lemma Q-hold
(Q preserves C^{1,α}, PROVEN in 16.3). **[RBB5-fix RS5-3: the corollary holds for T ≥ 5 (Ñ_X must embed, 16.1 (g)); LRL (b)
is quantified over T ≥ 3, and T = 3, 4 are not covered (not finite-dimensional uniformly in k): a separate argument is
needed, or LRL (b) is restated for T ≥ 5. N_res,m is defined in §18.0 (weights e^{mf} inside the sup, gradient and Campanato
terms, f as in ||·||_{D,m}). RS5-4 (b): the weighted constant e^{c_rm} rests on the reach of LR-pot (≤ 12) and Lemma Λ
(≤ 8), ARGUED.]**

### 16.9 Theorem RW^∇_k-Π(E): PROVEN as an implication
Theorem RW^∇_k-Π (§13.2, with [RBB4-fix RS4-1, RS4-2, RS4-6]) uses (W-Π) only through: Πx - x ∈ 𝒢_0 (Steps (a), (d)); locality with
radius r_Π and one translation-covariant local formula on 𝕋 and on the local tori (Step (e)); P^Π_□ ∈ S (Step 1); the bound
C_Π(R/4) (Step 3). EP-alg and EP-bd supply all of them for S_E with r_Π = 4 (the tori embeddings are coarse-lattice translations,
which carry roots, Neumann boxes and tents to themselves). So R ≥ 2r_Π + 8 = 16, T^Π_W = 4R + 14 + 2r_Π = 4R + 22 (product partitions;
3R + 22 for T a multiple of M_c), G^Π_P = C_ΠC_M^X(R/4)G_ΠC_M^Y(¼), ε^Π_W = t_Y5^d(4C_c/R)G_ΠC_M^Y(¼), with (W-lin-Π) for S_E ⇐ (H-inv+)
(Corollary EP-lin) ⟺ (H-lin^∇) in the best gauge (EP-opt). *Weighted form.* With (W-lin-Π)_m (weights e^{mf}, f 1-Lipschitz):
in R^Π_□y = -ι^*C^♯_{ψ_□}(u), u := 𝓖^Π_□ι_*M_{χ_□}y, the input sits in □^{(1)} and C^♯ reads u on (supp ∂ψ_□)^{(3)}, at distance ≥ R/2 - 4;
with f := min(dist(·, □^{(1)}), R) and the local-sup reading radius 3, ||R^Π_□y||_Y ≤ e^{-m(R/2 - 7)}(4C_c/R)G_Π(m)C_M^Y(¼)||y||, so ε^Π_W
gains at least e^{-m(R/2 - 9)} (as pre-stated; Π_E enters only P^Π_□, at a cost e^{4m} in G^Π_P). ∎

### 16.10 Proposition RATE-m: PROVEN as an implication (of (W-lin-Π)_m for S_E, a localised (W-comm), and BB-mix_k-Π's other hypotheses)
Put C_W' := t_Y5^d·4C_cG_Π(m)C_M^Y(¼). By 16.9, s̄ε^Π_W ≤ ¼ as soon as e^{-m(R/2 - 9)} ≤ R/(4C_W's̄); since R ≥ 1 it suffices that
R ≥ 18 + (2/m)log(4C_W's̄): **R_W(s̄) ≤ max(16, 18 + (2/m)log(C_Ws̄)), C_W := 4C_W'**. For the rate, choose instead s̄ as large as the
walk expansion allows at given R: s̄(R) := Re^{m(R/2 - 9)}/(4C_W'). BB-mix_k's per-cube smallness K = 2^{41}/(s̄ - 1) then gives, with
M_c = 2R, κ_L := log(1/K)/M_c ≥ [m(R/2 - 9) + log(R/(2^{44}C_W'))]/(2R) **[RBB5-fix RS5-6: 2^{44}, not 2^{43} (s̄ - 1 ≥ s̄/2)]** ≥ m/8 for R ≥ R_0(m, C_W') — **an O(1) rate, κ_L ≥ m/8**, k- and
T-uniform, compared with κ_L ~ (log M_c)/M_c at m = 0 ([RBB3-fix] note). The price is the field-size threshold ε ≤ ε_mix,k(s̄(R))
(fixed once R is fixed, before ε). **[RBB5-fix RS5-6: ε_mix,k of Theorem BB-mix_k (l.1149-1150) is the minimum of ε_0, G_N/C_N,
ρ_0, ρ_3, r_u-terms and C_M^Y-terms, each k-uniform under the hypotheses; so it is k-uniform and is written ε_mix.]** The mass is the top residual's: the soft term κ_{k-1}|r_{k-1}|² is present at every RG step
with κ_{k-1} ∈ [κ_-, κ_+], so 0 < m < m'_* is k-uniformly available (RW∇-F5; REVIEW_BFT_B_S4 Part F); its gauge-invariant
half is Theorem W (PROVEN), its gauge-variant half reduces by EP-rec (weighted) to (Res-Hölder)_m-type bounds. ∎

### 16.11 Lemma CL-uniq: PROVEN-HERE. Consequence: **GI-F2 does not occur**
A chain gauge is a level-0 function G acting at level j through its values at level-j sites (F6). Z^G = Z at level 0 means
G(x)^{-1}Z_0(b)G(y) = Z_0(b) for each link b = (x, y), i.e. G(y) = Z_0(b)^{-1}G(x)Z_0(b); if G(x_0) = 1, induction along paths gives
G ≡ 1 on the connected region. If Z^sm(V)^G = Z^sm(V)^{G'} with G, G' both restricting to h at level k, then G^{-1}G' stabilises
Z^sm(V)^G and equals 1 at the level-k sites: G = G'. With ĥ(h, V) := that G: Z^sm(V)^{ĥ(h_1,V)ĥ(h_2,V^{h_1})} = Z^sm(V^{h_1})^{ĥ(h_2,V^{h_1})} =
Z^sm(V^{h_1h_2}), and the product restricts to h_1h_2, so it is ĥ(h_1h_2, V); Z^sm(V^c) = Z^sm(V)^c and uniqueness give ĥ(c, V) = c. The
same holds on any connected region containing a level-k site, which is the form GI-cov uses (frames on Ω_□). ∎
**[RBB5-fix RS5-8: conditions: orbit covariance exact at level 0 on the region where the identity is used (the r_Z-interior
of Ω_□), and that region connected through level-0 links and containing a level-k site; both hold for box regions.]**
*Consequence for §12.3 / §13.6 Step 2 (GI-F2).* There, ĥ·ĝ_□(V^h) and ĝ_□(V)c map Z^sm(V) to the same chain Z^sm(V^{g_□(V)c}) on the
frame region, and both restrict at level k to h·g_□(V^h) = g_□(V)c (Lemma GI-frame (a)); by uniqueness they are equal. So
**GI-F2 cannot occur for any orbit-covariant lift**: the stabiliser that matters is the one among chain gauges with fixed
level-k values, which is trivial even at flat or reducible backgrounds. (CovLift) (i) reduces to orbit covariance plus
constant covariance. This sharpens §13.6's sentence "Without the cocycle ... GI-F2 OCCURS" and REVIEW_BFT_B_S4 C.4's "genuine
requirement near reducible or flat backgrounds" [new here; for the reviewer to check].

### 16.12 Lemma CL-blk: PROVEN-HERE **[post-proof correction: (iv) fails at every level j with L^{2(k-j)} > C_sm]**
(iv) at b = 0 forces log Z^sm(1) = 0, i.e. Z^sm(1) = 1. Let h := e^μ (level-k, μ small, not constant), V := 1^h, V(Y, Y + e_μ) =
e^{-μ(Y)}e^{μ(Y+e_μ)} =: e^{b(Y,μ)} with b ≠ 0 small. By (i) and Lemma CL-uniq, Z^sm(V) = 1^{ĥ}, ĥ := ĥ(h, 1). If at level j ĥ is
constant on level-k blocks, it equals h(Y) on the block of Y (it restricts to h at the root). Then 1^ĥ at level j is 1 on
block-interior links and e^{b(Y,μ)} on the links crossing the face between the blocks of Y and Y + e_μ. In coarse units the
level-j log is L^{k-j}b(Y, μ) on those links and 0 on the adjacent interior links, so ||∇^cx^c_j||_∞ ≥ L^{2(k-j)}||b||_∞ (one own step
of coarse length L^{-(k-j)}), while (iv) demands ≤ C_sm||b||_∞. So (iv) fails at every level with L^{2(k-j)} > C_sm; a k-uniform
C_sm is impossible. **[RBB5-fix RS5-7: the sup term already gives ||x^c_j||_∞ ≥ L^{k-j}||b||_∞, so (iv) fails once
L^{k-j} > C_sm.]** *Corner lift + gauge-commuting refinement.* U^(0)(V^h) = U^(0)(V)^{Ĝ} with Ĝ block-constant (Lemma U0 (iii));
iterated over levels the extension is constant on level-k blocks at every level; any Φ with Φ(W^G) = Φ(W)^G for all chain gauges
preserves it, and by CL-uniq that block-constant G is the extension of Φ∘(corner lift). ∎ **CL-F1 OCCURS.** bb5 B5-5 (linear
model): Φ-chain(dμ) = d(C_0-chain μ) to 9.7e-17, and the gradient proxy grows ×729 = 3^{2·3} from depth 2 to 5 — exactly L^{2Δ}.
*Correction to REVIEW_BFT_B_S4 Part E (R1), for the reviewer:* "Φ commutes with all level-j gauges" must be dropped; the
one-level refinement must also smooth the gauge part, i.e. its extension at V = 1 must be a smooth interpolation of h
(linearised: an interpolatory S_0 with C^{2,α} limit), e.g. through an elliptic normal form (CL-Φ) or a commuting pair (CL-lin).

### 16.13 Proposition CL-lin: PROVEN-HERE given φ ∈ C^{2,α} (the mask property is not proven here)
(a) *Identities.* In one dimension, Δ_f∘s = s^{[1]}∘Δ_c by definition (on the torus: zero-mean part through a periodic potential,
constants refined to constants), and Σ_{r<L}(s^{[1]}d)(Li + r) = (sp)(L(i + 1)) - (sp)(Li) = p_{i+1} - p_i = d_i (interpolatory, roots at
block centres: here the root of block i is fine site Li). Tensor products: S_1d = dS_0 componentwise; ev∘S_0 = 1; Q_axS_1 = 1 (the
root-row transverse factors are the identity by interpolation). Iterating: Q_axZ^lin_j = Z^lin_{j+1}, so all Q_ax-residuals vanish.
(b) *Covariance (linear).* Z^lin(B + dμ) = Z^lin(B) + (d S_0^{k-j}μ)_j, and with λ_0 := S_0^kμ, ev^{(j)}λ_0 = S_0^{k-j}μ (interpolation), so the
change is the composite gauge direction Dλ_0 restricting to μ at level k; additivity is the linear cocycle; S_0c = c.
(c) *Range.* If s reads coarse values within r_s coarse steps, level j reads level j + 1 within r_sρ_{j+1}; composite
Σ_{i>j}r_sρ_i ≤ r_sL/(L - 1) (coarse). Finite for finite masks; exponential decay for the cubic spline **[post-proof correction:
finite range only for finite masks]**.
(d) *Bounds.* For an interpolatory stationary scheme, S_0^mc = f(L^{-m}·) on the fine lattice, f := Σ_ic_iφ(· - i) (values at the
level-m points are preserved by every further refinement). For links, with ψ(y) := Σ_{i≥1}φ'(y - i) (compactly supported since
Σ_iφ'(· - i) = 0; ψ ∈ C^{1,α} if φ ∈ C^{2,α}): (s^{[1]})^md at the fine link [z, z + ρ] equals ∫_z^{z+ρ}Σ_id_iψ(t - i)dt. In d dimensions
the μ-component of S_1^mB in coarse units is x^c(z) = Σ_iB_μ(i)·avg_{[z_μ,z_μ+ρ]}ψ(· - i_μ)·Π_{ν≠μ}φ(z_ν - i_ν) =: (K_ρB)(z), a C^{1,α} function of
z with ||K_ρB||_{C^{1,α}} ≤ C(φ, d)||B||_∞ uniformly in ρ ((2r_s)^d overlapping terms; averaging over an interval preserves the
bound). Its lattice values, difference quotients and their Hölder seminorms are bounded by the continuum ones. So
**||Z^lin(B)||_X ≤ 3C(φ, d)||B||_∞ uniformly in k** (Q_ax-residuals zero).
(e) *Lane A's Q.* Q - Q_ax kills exact forms (both root-covariant); for each S4' contour γ the loop γ - (straight leg) is spanned by
≤ 2L(L - 1) plaquettes (Lemma Λ's count), so |r_j|_own ≤ 2L(L - 1)max|dZ^lin_j|_own = 2L(L - 1)ρ_j²||f_j||_∞ and the 𝔐^∇ residual term
L^{k-1-j}||r^c_j|| = ρ_{j+1}^{-2}|r_j| ≤ 2((L - 1)/L)||f_j||_∞ ≤ 2||f_j||_∞ **[post-proof correction: 2, not 2L²]**. (Its C^{1,α} norm,
needed in N_res, is not bounded here.) ∎
*Status of the mask hypothesis.* For the periodic cubic spline, φ is the cardinal cubic spline (C^{2,1}, exponentially decaying)
[classical, from memory; not re-derived here]. For the ternary Lagrange masks bb5 measures (proxies, not proofs): DD4 not
C^{2,α} (gradient proxy grows ×1.9 from depth 3 to 5: **CL-F2 OCCURS** for DD4), DD6 and DD8 converge (×1.19-1.20, ×1.08-1.09,
with geometrically shrinking increments), their C^{1,1} proxy grows (they are not C³). A proof for DD6/DD8 is a finite
computation for one mask (a joint-spectral-radius bound on second differences of the derived scheme below L^{-(1+α)}), not done.
**[RBB5-fix RS5-10: done in REVIEW_BFT_B_S5 Part D (exact arithmetic, m-ary difference-scheme theorem) and reproduced by
lane B in checks/bb6m (planned at the time of this tag; session 6): DD8 ternary φ ∈ C^{2,β} with β ≥ 0.473 (PROVEN); DD6 β ≥ 0.267 (PROVEN; at most 0.320,
marginal at α = ¼); DD4 not C² (smoothness ≤ 1.817). **DD8 is adopted as the mask of CL-lin and of (N2).** bb5's DD6 pass
(1.193/1.200 against 1.25) is marginal on the proxy; admissibility is settled by the exact bound.]**

### 16.14 Proposition CL-Φ: PROVEN as an implication (linear model)
The descent increment τP_cd*dA is unchanged under A ↦ A + dν (d*d∘d = 0), and C dμ = d C_0μ, so Φ-chain(B + dμ) = Φ-chain(B) + d(C_0-chain μ):
linear covariance with the block-constant extension; CL-blk applies. For Z^Φ := Π_E∘(Φ-chain): by 16.1 (a), for λ_0 not vanishing at
level k, Λ(x + Dλ_0) = Λ(x) - λ_0 + I_χλ_0, I_χλ_0 := Σ_Xχ^5_Xλ_0(c_X), so Π_E(x + Dλ_0) = Π_Ex + D(I_χλ_0): Z^Φ(B + dμ) = Z^Φ(B) + D(I_χC_0^kμ),
and I_χC_0^kμ = Σ_Xχ^5_Xμ(X) is the quintic-tent interpolation of μ (smooth extension; CL-blk avoided). By EP-rec,
||Z^Φ(B)||_X ≤ C_rec(||Φ-chain(B)||_inv + ||B||_D + N_res(Φ-chain(B))). ∎ *Measured (bb5, informational):* for the Φ-chain with
N = 18, τ = 0.1, the curvature sup stays bounded (2.36 → 2.42) but its Hölder proxy grows like 3^{m/4} (5.53, 7.27, 9.55, 12.6, 16.5),
numerically the same as the Q1/Whitney curvature (5.53, 7.28, 9.58, 12.6, 16.6): this one-level descent leaves block-scale
piecewise-constant curvature, so the curvature hypothesis of CL-Φ FAILS for it (pre-stated guess "F1(5)/F1(3) ≤ 1.5": FAILED,
1.73). A refinement must read neighbouring coarse cells (as the 6- and 8-point masks do), not only its own block pair.

### 16.15 Proposition CovLift-route: ARGUED
On 𝒞_glob, (CovLift) follows from a nonabelian one-level refinement R_j: Z_{j+1} ↦ Z_j with (R1') exact orbit covariance with a
smooth extension (then the cocycle is automatic by CL-uniq), finite range, and linearisation at the trivial chain equal to a
CP pair with φ ∈ C^{2,α} (Proposition CL-lin), plus (R3) a level-uniform BCH absorption: the nonlinear defect of R_j is O(ε²) in
C^{1,α} and is not amplified by the linear iteration (the linear iterates are C^{1,α}-bounded by CL-lin, so an O(ε²) source per
level summed with the L^{-1} contraction of coarse units gives O(ε²) in total) [argued, not written]. A concrete candidate for
R_j: (1) the nonabelian box-Coulomb normal form (minimise Σ|log W^g|² over gauges g with g(c_X) = 1 on Ñ_X, glued by quintic tents in
exponential coordinates; locally unique near small fields by the implicit function theorem around EP-int, covariant under
constants) applied to (2) a gauge-invariant curvature subdivision whose linearisation is the CP pair's curvature map
(f ↦ dS_1B, reading neighbouring coarse cells). Items OPEN: (N1) the nonlinear EP-int; (N2) the covariant curvature subdivision;
(N3) (R3). Most robust alternative (unchanged): Balaban's variational lift, exponentially local, with the localisation inside
the induction. **(CovLift): OPEN.**

## 17. Session-5 check record, outcome and notes for other files (written after §16)

**Check bb5** (criteria checks/bb5_criteria.md born 08:27:06 UTC; script checks/bb5_lift.py born 08:28:06, final bytes 08:28:21
after one pre-run edit (the block-constant scalar extension's index offset fixed, a no-op conditional and an unused line
removed; no criterion touched); output checks/bb5.out 08:28:31-08:28:34). Runner scratchpad bb5/run_bb5.sh (lock free on
arrival; load1 3.31; memory free 40%; nice 10; thread variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3
without -I; no `timeout`; no trap; `rmdir` once). 2.85 s wall, peak RSS 521 MB. No process left; no __pycache__ in checks/.
**Verdict: ALL PASS (5/5).**
- **B5-1 PASS** identities: S_1d = dS_0 ≤ 2.2e-13, ev∘S_0 = 1 exactly, Q_axS_1 = 1 ≤ 8.5e-13 (relative); Φ-chain constraint ≤ 8.0e-16.
- **B5-2 PASS** (Q1/Whitney, CL-F3 OCCURS): gradient proxy P1 = 4.63, 13.9, 41.7, 125, 375 (×3 per level); ratio P1(5)/P1(2) = 27.
- **B5-3 PASS** (cubic-spline pair bounded): P(5)/P(3) = 1.000, 1.017, 1.018 (P0, P1, P2); C^{1,1} proxy also bounded (7.15 → 7.30).
- **B5-4 PASS**: DD6 (1.001, 1.193, 1.200) and DD8 (1.002, 1.079, 1.085) satisfy the condition; DD4 does not (1.003, 1.903, 2.308).
- **B5-5 PASS** (CL-blk mechanism): Φ-chain(dμ) = d(C_0-chain μ) to 9.7e-17; P1 = 11.8, 106, 957, 8.61e3, 7.75e4 (×9 per level),
  ratio 729.
- Informational: DD4 grows (guess CL-F2 confirmed); Φ-chain on random input: curvature Hölder proxy F1(5)/F1(3) = 1.73 (guess
  "≤ 1.5" FAILED), sup potentials grow ×3 per level (P0 = 3.27 → 268: the gauge part, CL-blk); C^{1,1} proxies of DD6/DD8 grow
  ×2.1/×1.6 per level (not C³).
- *Reading (measured only; proxies, d = 2, L = 3, depth ≤ 5).* Commuting tensor pairs from 6- and 8-point ternary interpolatory
  masks keep the coarse-unit C^{1,α} proxies (α = ¼) converging across depths, the 4-point one does not, the global cubic-spline
  pair is flat, and Q1/Whitney loses a factor 3 per level in the gradient. The corner lift followed by gauge-invariant
  constrained descent never smooths the gauge part (exact identity) and leaves Whitney-like piecewise-constant curvature.
  Not measured: lane A's exact norms, k > 5 levels, nonabelian effects, lane A's S4' Q.

| Item (session 5) | Status | Note |
|---|---|---|
| Binding and cosmetic fixes of REVIEW_BFT_B_S4 (RS4-1..RS4-7, item 8) | applied, tagged [RBB4-fix] | torus sides 4R + 14 + 2r; full-gradient reading; GI-pert residual ARGUED, Feynman difference in (Mult-Y); C^{2,α} tents + elliptic slice; (Pair-loc), (I-id)_Z listed; MSG own units |
| Lemma EP-alg | PROVEN-HERE | projection algebra of the box-Coulomb + quintic-tent slice; r_Π = 4 |
| Lemma EP-int | PROVEN-HERE (given LES-div) | interior C^{2,α} of the box-Coulomb gauge, k-uniform; no Gaffney, no boundary regularity |
| Lemma Q-hold | PROVEN-HERE | Q^{(a→b)} preserves coarse-unit C^{1,α} (C_Q ≤ 7C_T + 4) |
| **Theorem EP-bd** | **PROVEN-HERE** | **(W-Π) for S_E: Π_E bounded on 𝔐^∇, k-, T-uniform** |
| **Theorem EP-opt** | **PROVEN-HERE** | **(W-lin-Π) for S_E ⟺ (H-lin^∇) in the best gauge (within C_Π)** |
| **Theorem EP-rec** | **PROVEN-HERE** (given LES-div, Lemma Λ, LR-pot) | ||Π_Ex||_𝔐 ≤ C_rec(||x||_inv + ||x_k||_D + N_res(x)) for every configuration |
| Corollary EP-lin | PROVEN as an implication | (W-lin-Π) for S_E ⇐ (H-inv+) (gauge invariant); converse with max_i |
| Corollary EP-LRL(b) | PROVEN as an implication | lane A's LRL (b) ⇐ (Res-Hölder)_m alone (Prop W supplies the rest) **[RBB5-fix RS5-3: T ≥ 5 only; N_res,m defined in §18.0; RS5-4: weighted constant ARGUED]** |
| **Theorem RW^∇_k-Π(E)** | **PROVEN as an implication** | hard-slice RW^∇_k with an admissible slice: (W-Π) PROVEN; (W-lin-Π) ⇐ (H-inv+); R ≥ 16; tori 4R + 22 |
| Proposition RATE-m | PROVEN as an implication | κ_L ≥ m/8 (O(1) rate) from the top residual's coarse mass, under (W-lin-Π)_m + localised (W-comm) |
| Lemma CL-uniq | PROVEN-HERE | the cocycle of (CovLift) (i) is automatic; **GI-F2 cannot occur** (new; for review) |
| Lemma CL-blk | PROVEN-HERE | block-constant extensions violate (iv) by L^{2(k-j)}; corner lift + gauge-commuting smoothing fails (corrects REVIEW_BFT_B_S4's (R1)) |
| Proposition CL-lin | PROVEN-HERE given φ ∈ C^{2,α} | linearised (CovLift) (i)-(v) from a commuting tensor pair; ~~mask regularity measured (bb5), not proven~~ [struck: RBB6-fix RS6-9] **[RBB5-fix RS5-5: read "(i), (ii), (iii), (iv) first clause, (v) (linear)"; the C_g clause of (iv) holds at θ = 0 (or with Q_ax as the functional's Q), θ > 0 OPEN. RS5-10: mask regularity PROVEN by an exact finite computation (REVIEW_BFT_B_S5 Part D; a lane-B reproduction, checks/bb6m, planned at the time of this tag): DD8 ternary φ ∈ C^{2,β}, β ≥ 0.473; DD6 β ≥ 0.267 (marginal at α = ¼); DD4 not C². DD8 is the adopted mask]** |
| Proposition CL-Φ | PROVEN as an implication | Π_E as gauge normal form gives a smooth extension; the tested one-level descent fails its curvature-Hölder hypothesis |
| Proposition CovLift-route | ARGUED | (R1') + (R3); OPEN items (N1) nonlinear EP-int, (N2) covariant curvature subdivision, (N3) BCH absorption |
| (CovLift) | OPEN | linear level done (CL-lin); nonabelian exact covariance with smooth extension not constructed **[RBB5-fix RS5-10: linear level unconditional with DD8 (mask regularity PROVEN); minus the C_g clause at θ > 0 (RS5-5)]** |
| Failure modes | EP-F1, F2, F3 do not occur; EP-F4 OPEN (= (Res-Hölder)); CL-F1 OCCURS; CL-F2 OCCURS for DD4 (not DD6/DD8, numerically) **[RBB5-fix RS5-10: PROVEN exactly: DD4 not C², DD6/DD8 C^{2,α} at α = ¼]**; CL-F3 OCCURS | |
| bb5 | ALL PASS (5/5); one informational guess FAILED (Φ curvature Hölder) | |

**What the hard-slice RW^∇_k rests on now.** (W-Π): PROVEN for S_E. (W-lin-Π): ⟺ (H-lin^∇) in the best gauge ⟸ (H-inv+), a purely
gauge-invariant statement: lane A's ||x||_inv bounds (data + residual sources PROVEN, Theorem W; (CO-0), (CO-up) OPEN for the
other source classes) plus the residual-gradient size N_res of responses ((Res-Hölder), OPEN). (W-comm), (W-loc) (i), (ii), (iv):
as before (GAP 1 / BL-6 (b) for the plain rows).

## FOR OTHER FILES (session 5; for their owners; not edited)
- **BFT_A (lane A).** (1) Lane B now owns the slice: LRL (b)'s P_♯ should be Π_E (box-Coulomb gauge on half-width-2 Neumann boxes,
  glued by quintic tents; §15.0, §16.1-16.6). With it LRL (b) ⟸ (Res-Hölder)_m: N_res,m(y(B_k)) ≤ C||B_k||_{D,m} for the data map
  (Corollary EP-LRL(b)); REVIEW_BFT_A_S4 Part 6 items 1-3 and 5 are discharged, item 4 is (Res-Hölder) + Lemma Q-hold (PROVEN).
  (2) More generally (Theorem EP-rec) any gauge-invariant bound ||x||_inv + N_res(x) ≤ C||y|| for a response class gives the full
  𝔐^∇ bound in S_E; lane A may prove (H-lin^∇) in any convenient gauge (EP-opt) or gauge-invariantly. (3) S_tent is not needed
  for the gradient half; LR-pot and Lemma Λ are used as inputs of EP-rec.
- **REVIEW (next lane-B review).** New claims to check first: Lemma CL-uniq's consequence that GI-F2 cannot occur (16.11), and
  Lemma CL-blk's correction of REVIEW_BFT_B_S4 Part E (R1) (16.12).
- **SF.md (L-loc)_k.** With Proposition RATE-m the cluster rate is κ_L ≥ m/8 for 0 < m < m'_* (the top residual's coarse mass),
  under the weighted slice inputs; the unweighted κ_L ~ log M_c/M_c stands for the unweighted form.
- **HIST (MSG).** Unchanged: MSG's bound is in own units; (CovLift) is not an MSG corollary.

# Session 6 (2026-10-28 UTC)

## 18. PRE-STATED (session 6) — statements only; the FIRST edit of session 6 (appended before any [RBB5-fix] edit, before any session-6 proof, criteria file or script). Nothing in §18 cites a result of this session. Exploratory reasoning while reading preceded this append (not recorded), so its only claim is file order. Proofs follow in §19, later. Owner instruction: lane B owns (Res-Hölder) from this session; lane A does not work on it.

### 18.0 Settings (definitions)
- **Setting RH.** Setting LIN of BFT_A §7.1 at the trivial chain (componentwise in an orthonormal basis of su(N)), d = 4,
  L ≥ 3 odd, κ_l ∈ [κ_-, κ_+], κ̂ := κ_+/κ_-, 0 < α < θ < 1 unless stated (lane A fixes (α, θ) = (¼, ½), BFT_A §12.0).
  Sources y = (G_l (0 ≤ l < k), s_l (0 ≤ l < k), j_0, j_l (1 ≤ l < k)) with d*j_l = 0 for every l, entering E_src as in
  BFT_A §7.1 (and the pairing π of §9.0). x is any critical point of E_src (data x_k = B_k). Coarse units BFT_A §1.3
  (1-form x^c_j = L^{k-j}x_j, 2-form H^c = L^{2(k-j)}H, plain current j^c = L^{3(k-j)}j, r^c_j = L^{k-1-j}r_j).
- **Effective residual currents** ρ_l := κ_lr_l(x) - s_l (level-(l+1) 1-forms, 0 ≤ l ≤ k - 1). π_l(j) := ||j^c_l||_∞.
- **Residual sizes.** N_res(x) as in §15.0 (Σ_{0≤i≤k-2}||r_i||_{C^{1,α}}, Campanato [·]_α, level-(i+1) coarse units);
  N^∞_res the same with the pointwise [·]^∞_α; N^max_res := max_i instead of Σ_i.
- **Weighted residual size (fix RS5-3 (b)).** With lane A's weight w(z) := e^{m d(z,X_0)} (ℓ¹ coarse torus distance) and
  lane A's ||·||_{∞,m}, [·]_{α,m} (BFT_A §12.0): ||H||_{C^{1,α},m} := ||H^c||_{∞,m} + ||∇^cH^c||_{∞,m} + [∇^cH^c]_{α,m};
  **N_res,m(x) := Σ_{0≤i≤k-2}||r_i(x)||_{C^{1,α},m}**.
- **Nonabelian box functional.** For a level-0 SU(N) configuration U on the links of Ñ_X (§15.0) and g: Ñ_X → SU(N):
  Φ_{U,X}(g) := Σ_{b=(x,y)⊂Ñ_X}|log(g(x)U(b)g(y)^{-1})|² (principal log; Ad-invariant norm on su(N)). U^g(b) := g(x)U(b)g(y)^{-1}.
  𝒲_δ(U, X) := {g : g(c_X) = 1, max_{b⊂Ñ_X}n|log U^g(b)| ≤ δ}. ε_f(U, X) := max_{p⊂Ñ_X}n²|log U(∂p)| (gauge invariant).
  A critical point g ∈ 𝒲_δ is called a **box normal form**, g_X(U), and N_X(U) := U^{g_X(U)}.
- **(N1-G) [named import, not proven here]:** for the mean-zero Green function G_M of -Δ on a 4D lattice torus of side M,
  Σ_y|∇G_M(y)| ≤ C_GM, C_G absolute. (Implied by the bound |∂G(y)| ≤ C|y|^{-3} that BFT_A §3.7 (BA-7) imports, marked
  IMPORTED-NOT-YET-REVERIFIED there.) **[RBB6-fix RS6-6 (binding): no longer an import. Lemma N1G (§21.1, proof §22.2):
  Σ_y|∇_μG_M(y)| = M/4 exactly for M even (< M/4 for M odd), C_G = ¼, IMPORTED-AND-REVERIFIED from REVIEW_BFT_B_S6 D.4
  (reviewer's proof, re-verified line by line in §22.2; reproduced in checks/bb7g). [RBB7-fix RS7-1: planned at the time of this tag, Step 1 10:23; proof written 10:38] (proof replaced: REVIEW_BFT_B_S7 B.2)]**
- **Karcher mean [standard; cited (Karcher 1977), not re-derived].** For points p_1..p_q of SU(N) in a geodesic ball of
  radius r_K below the convexity radius of the bi-invariant metric and weights w_i ≥ 0, Σw_i = 1, the weighted Karcher
  mean M_w(p) is the unique minimiser of Σw_id(·, p_i)² in that ball; it is real-analytic in (p, w), M_w(apb) = aM_w(p)b
  for constants a, b, and M_w(p) = p_i if w_i = 1.
- **Construction KΠ (Karcher-glued elliptic normal form).** For U with box normal forms g_X(U) at every level-k site X:
  G(U)(z) := M_{χ^5(z)}({g_X(U)(z)}_{X: χ^5_X(z)>0}) (the ≤ 16 corners of z's coarse cell; tents χ^5 of §15.0);
  **Π^{NA}(U) := the composite gauge transform of U by G(U)** (all levels; G(U) = 1 at level-k roots); S^{NA} := {U : G(U) ≡ 1}.
- **Construction GC (gauge-commuting DD8 refinement).** s := the ternary Deslauriers-Dubuc 8-point (DD8) interpolatory
  scheme, φ its basic limit function; S_0, S_1 the commuting tensor pair of Construction CP (§15.0); C_0 the block-constant
  extension. Linear: R B := S_1B + dμ(B), μ(B)(z) := Σ_iΦ(z - i)·∫_{a(i→X(z))}B (Φ := φ^{⊗d} the S_0 kernel, the sum over
  level-(j+1) sites i, a(i→X) the coarse axial path from i to the block X(z) of z in a fixed coordinate order).
  Nonabelian (framed): for a level-j fine link b = (z, z') with z in block X and z' in block X' (X' = X or X + e_μ):
  R^{ax}(Z)(b) := exp(s^X(b))·Z(X, X') (Z(X, X) := 1), where s^X := the linearised value S_1A^X + dμ(A^X) at b with A^X
  the coarse configuration written in the axial frame at X, A^X(i, i + e_ν) := log(P_{X←i}Z(i, i + e_ν)P_{X←i+e_ν}^{-1}),
  P_{X←i} the product of Z along a(i→X) reversed (frame X ← frame i).

### 18.1 (Res-Hölder): statements (STEP 2)
- **Lemma RT (exact residual transport).** At every critical point of E_src: (a) d*ρ_l = 0 for 0 ≤ l ≤ k - 1; (b)
  ρ_{l-1} = (Q_{str,l})^Tρ_l - d*G_l - j_l for 1 ≤ l ≤ k - 1; (c) for 0 ≤ i ≤ k - 2:
  **r_i = κ_i^{-1}[s_i + (Q_str^{(i+1→k)})^Tρ_{k-1} - Σ_{l=i+1}^{k-1}(Q_str^{(i+1→l)})^T(d*G_l + j_l)]**.
  *Planned: PROVEN-HERE* (Euler-Lagrange equations; d*Q^T = ev^Td*; ev^T injective; Q^T = Q_str^T - h^Td*; IT-str).
- **Lemma TC (transported sizes; m := k - 1 - i ≥ 1).** In level-(i+1) coarse 1-form units:
  ||((Q_str^{(i+1→k)})^Tρ)^c||_∞ ≤ L^{-2m}||ρ||_∞ for level-k ρ; ||((Q_str^{(i+1→l)})^Tj)^c||_∞ ≤ L^{-2m}π_l(j) for a level-l
  current (i < l ≤ k - 1); π_l(d*G_l) ≤ 6L^{k-l}||G^c_l||_∞. Inverse estimate: for a level-(i+1) 1-form H,
  ||H||_{C^{1,α}} ≤ 5L^{(1+α)m}||H^c||_∞ (Campanato; 7 for the pointwise version). *Planned: PROVEN-HERE.*
- **Theorem RH ((Res-Hölder), m = 0).** For every critical point, uniformly in k ≥ 2, T ≥ 1 and in the level:
  N_res(x) ≤ (5/κ_-)[(κ_+||r^c_{k-1}||_∞ + ||s^c_{k-1}||_∞)/(L^{1-α} - 1) + L^{-θ}||s||_R/(L^{θ-α} - 1)
  + (1 - L^{-(1-α)})^{-1}Σ_{1≤l≤k-1}L^{-(1-α)(k-l)}(π_l(j_l) + 6L^{k-l}||G^c_l||_∞)].
  The same with 7 in place of 5 for N^∞_res. *Planned: PROVEN-HERE* (Lemma RT + Lemma TC; no LES, LES-div or Caccioppoli
  step is needed: the transport gains L^{-2} per level in coarse units against the inverse-estimate loss L^{1+α}, 2 > 1 + α
  in d = 4).
- **Corollary RH-inv.** For 0 < α < θ < 1 and every source class of 𝒴^∇ ((G), (R), (P0), (Pl-c), and rough plain currents in
  the F3 size N_l): N_res(x) ≤ C_1||x||_inv + C_2||y||, C_1, C_2 depending on (L, κ_±, α, θ) only. Hence **(H-inv+) ⟺ (H-inv)**
  (the gauge-invariant bound ||x||_inv ≤ G||y||_Y alone), and Corollary EP-lin gives (W-lin-Π) for S_E from (H-inv) alone.
  At α = θ: N^max_res obeys the same bound, while the sum N_res can grow like k (residual sources at all levels).
  *Planned: PROVEN as an implication; the α = θ example PROVEN-HERE.*
  **[RBB6-fix RS6-1 (binding), RS6-2; session 7, tag added to the pre-stated text, original words kept]** Scope: read "every
  level-wise co-closed Setting-LIN source class: (G), (R), the commutator rows (residual type by lane A's CR-1), BA-6's residual
  part, (P0), (Pl-c), rough plain currents, the co-closed BCH₂ rows and the co-closed completions d*W_l (as (G)-slot sources)" in
  place of "every source class of 𝒴^∇". **The non-co-closed BCH₂ remainder V_l (BFT_A §26.2) is outside Lemma RT** (Lemma RT (a)
  uses d*j_l = 0 at every level); its (Res-Hölder) is OPEN (lane A's (NC-Γ) target); candidate route: Lemma RT for
  composite-co-closed sources with the explicit funnel terms h_l^Td*ρ_l as additional level-l plain sources (REVIEW_BFT_B_S6 B.4,
  ARGUED there). Naming (RS6-8): Theorem RH is renamed **Theorem RHT** (lane A has a Lemma RH, BFT_A §23.8), Theorem RH_m →
  **RHT_m**; the corollaries keep their names.
- **Corollary RH-D (data map).** For the source-free data map: N_res(y(B_k)) ≤ (5κ̂/(L^{1-α} - 1))||r_{k-1}||_∞ ≤
  (20κ̂C_R/(L^{1-α} - 1))||B_k||_D (C_R of N2-lin). *Planned: PROVEN as an implication* (Theorem RH; LINEAR_PACKAGE Thm 3.8).
- **Theorem RH_m (weighted).** For 0 ≤ m: N_res,m(x) ≤ e^{c_wm}·[the right side of Theorem RH with weighted sup norms],
  c_w := 8 [crude]; for the data map, N_res,m(y(B_k)) ≤ e^{c_wm}(5κ̂/(L^{1-α} - 1))G_D(m)||B_k||_{D,m} for 0 ≤ m < m_*'
  (Proposition W). *Planned: PROVEN-HERE (supports of bounded coarse size) + PROVEN as an implication.*
- **Corollary LRL(b)-E.** With Corollary EP-LRL(b) (as fixed by RS5-3: T ≥ 5): lane A's LRL (b) holds for T ≥ 5 with
  P_♯ := Π_E and 0 ≤ m < m' < m_*'; its weighted constant rests on EP-rec's weighted reach (RS5-4, ARGUED). T = 3, 4: not
  claimed. *Planned: PROVEN as an implication.*

### 18.2 Nonabelian (CovLift): statements (STEP 3)
- **Lemma NF-crit.** g is a critical point of Φ_{U,X} on {g(c_X) = 1} iff (d*w)(z) = 0 at every site z of Ñ_X (Neumann
  divergence: links leaving Ñ_X omitted), w := log U^g. *Planned: PROVEN-HERE* (⟨w, φ(ad_w)ξ⟩ = ⟨w, ξ⟩).
- **Lemma NF-uniq (normal-form uniqueness).** There is δ_0 = δ_0(N) > 0, independent of n, k, T, such that for δ ≤ δ_0
  Φ_{U,X} has at most one critical point in 𝒲_δ(U, X). *Planned: PROVEN-HERE* (convexity of t ↦ Φ(e^{tξ}g_1) after a constant
  left shift that makes ξ mean-zero; Neumann box Poincaré ||η - η̄|| ≤ ((4n + 1)/2)||dη||).
- **Lemma NF-cov (exact covariance).** If g ∈ 𝒲_δ(U, X) is critical then, for every level-0 gauge h on Ñ_X (no smallness),
  h(c_X)gh^{-1} ∈ 𝒲_δ(U^h, X) is critical. Hence g_X(U^h) = h(c_X)g_X(U)h^{-1}, N_X(U^h) = Ad_{h(c_X)}N_X(U), and
  g_X(U^c) = cg_X(U)c^{-1} for constants c. *Planned: PROVEN-HERE.*
- **Lemma REF (exact reflection) and (N1-bd).** Neumann-co-closed 1-forms w on Ñ_X correspond (by even/odd reflection in
  all four directions) to reflection-odd co-closed mean-zero 1-forms w^R on the torus of side M = 2(4n + 1), with
  d(w^R) = (dw)^R and sup|w^R| = sup|w|. Hence **(N1-bd)**: sup_{Ñ_X}|w^c| ≤ C_B sup_{Ñ_X}|(dw)^c|, C_B := 60C_G.
  *Planned: PROVEN-HERE given (N1-G).*
- **Theorem NF-ex (existence).** There are ε_0, δ (depending on N, C_G only) such that if U = e^A on Ñ_X with
  max n|A| ≤ ε_0 then Φ_{U,X} has a critical point in 𝒲_δ(U, X) (unique by NF-uniq), and its w obeys
  max n|w| ≤ 2C_B(ε_f(U, X) + C_{BCH}ε_0²)... more precisely ≤ 2C_B·max_{t∈[0,1]}ε_f(e^{tA}, X).
  *Planned: PROVEN given (N1-G)* (continuation in t; IFT with the convexity Hessian bound; a priori bound from (N1-bd) and BCH).
- **Proposition KΠ.** On 𝒟(ε) := {U : U is gauge-equivalent on each Ñ_X to some e^A with max n|A| ≤ ε} (ε ≤ ε_0), and
  wherever the points {g_X(U)(z)} lie in a ball of radius r_K: Π^{NA} is well-defined, G(U)(c_Y) = 1, Π^{NA}∘Π^{NA} = Π^{NA};
  for every level-0 gauge h for which the points {h(c_X)g_X(U)(z)} also lie in such a ball (e.g. d(h(c_X), h(c_Y)) small for
  corners X, Y of one cell): **Π^{NA}(U^h) = Π^{NA}(U)^{ĥ}, ĥ(z) := M_{χ^5(z)}[h(c_X)g_X(U)(z)]·M_{χ^5(z)}[g_X(U)(z)]^{-1}**,
  ĥ(c_Y) = h(c_Y); constant covariance Π^{NA}(U^c) = Π^{NA}(U)^c; at U = 1, ĥ = M_{χ^5}[h(c_X)] (Karcher-tent interpolation of
  the root values, C^{2,1} in coarse units); Π^{NA} linearises at U = 1 to Π_E; range r_Π = 4. *Planned: PROVEN given NF-ex
  and the Karcher facts.*
- **Lemma GC-lin.** R of Construction GC is linear, local (range ≤ (r_s + d)L/(L - 1) coarse), with R(dν) = dC_0ν (linear
  orbit covariance with the block-constant extension), dRB = dS_1B (the DD8 curvature map), and Q_axRB = B.
  *Planned: PROVEN-HERE.*
- **Proposition AX-cov.** R^{ax} is exactly orbit-covariant with block-constant extension: R^{ax}(Z^h) = R^{ax}(Z)^{C_0h}
  (C_0h(z) := h(X(z))), constant-covariant, finite range, and its linearisation at the trivial chain is R. *Planned:
  PROVEN-HERE for covariance and range; linearisation ARGUED.*
- **Theorem CovLift-KΠ.** Z^{KΠ}(V) := Π^{NA}(R^{ax}_0∘…∘R^{ax}_{k-1}(V)) on 𝒞_glob(ε) satisfies (CovLift) (i) (exact orbit
  covariance with the smooth extension of Proposition KΠ; cocycle automatic, Lemma CL-uniq), (ii) finite range, (iii)
  translation covariance and constant covariance; (iv), (v) ⇐ **(N1-int)** (k-uniform interior C^{2,α} of the box normal
  forms, the nonlinear EP-int) + **(N2-bd)** (k-uniform C^{1,α} bounds of the iterated R^{ax}: BCH absorption (R3)).
  *Planned: PROVEN as an implication for (i)-(iii); (iv), (v) OPEN, the wall named.*

### 18.3 Failure modes (pre-stated)
- **RH-F1** ρ_l is not co-closed (the transport identity fails). Expected: does NOT occur.
- **RH-F2** the direct s-term blocks the sum N_res. Expected: occurs only at α = θ.
- **RH-F3** the transported term saturates the inverse estimate (gradient-Hölder ∝ L^{-(1-α)m}). [guess: occurs]
- **NF-F1** two box normal forms in 𝒲_δ. Expected: NOT. **NF-F2** a logarithmic boundary loss in (N1-bd). Expected: NOT
  (degree -1 after reflection). **NF-F3** the Karcher gluing breaks covariance. Expected: NOT on its domain.
- **CL-F4** the Karcher domain (small root differences of h) excludes gauges used by GI-cov (§13.6). Expected: OPEN.

### 18.4 Checks (criteria files written after this section and before the scripts)
- **bb6** (d = 4 abelian chain, L = 3, k = 2, coarse side T = 2; root-covariant Q := Q_str - d∘h with one axial order):
  identities of Lemma RT at a numerical critical point with all source classes; sizes of Lemma TC; depth scaling (m = 1-3)
  of the transported term with a random top ρ.
- **bb6m** (RS5-10): exact-arithmetic regularity of the ternary DD4/DD6/DD8 masks (||S_e^n||_∞ with e = 9a/σ³).
- **bb6n** (d = 2, SU(2)): box normal forms (critical equation, uniqueness from several starts, exact covariance under a
  large random h); KΠ on a coarse torus of side 5 (G = 1 at roots, idempotence, covariance formula).

## 19. Proofs (session 6; appended after §18 (09:20:07 UTC), after Step 1 (09:20:4x-09:22:01) and after bb6m, bb6n, bb6 ran (09:28:23-09:29:14))

Post-proof corrections of pre-stated details are marked **[post-proof correction]** where they occur; §18 is not edited.
They are: (1) Theorem RH_m: c_w = 12 (10 for the data map), not 8; (2) Theorem NF-ex also needs the coarse curvature to be
small along the path (max_t ε_f(e^{tA}, X) ≤ ε_0); sup-smallness alone does not give it; (3) Theorem CovLift-KΠ (i)-(iii) need,
for the existence of the box normal forms, the zeroth-order part (N2-0) of (N2-bd); (4) Proposition KΠ: the covariance
identity itself holds for every map U ↦ U^{G(U)} with G(U) = 1 at the level-k roots; the content is the root-value formula for
ĥ, idempotence and the smooth extension; (5) CL-F4 does not occur on 𝒞_glob; (6) Proposition AX-cov's linearisation is
PROVEN here (pre-stated ARGUED).

### 19.1 Lemma RT: PROVEN-HERE
*Euler-Lagrange equations.* For 1 ≤ l ≤ k - 1, x_l enters r_l = Q_lx_l - x_{l+1} and r_{l-1} = Q_{l-1}x_{l-1} - x_l, and the
sources ⟨G_l, dx_l⟩ + ⟨j_l, x_l⟩; so ∂E_src/∂x_l = Q_l^T(κ_lr_l - s_l) - (κ_{l-1}r_{l-1} - s_{l-1}) - d*G_l - j_l = 0, i.e.
ρ_{l-1} = Q_l^Tρ_l - d*G_l - j_l. At level 0: d*dx_0 + Q_0^Tρ_0 - d*G_0 - j_0 = 0.
*(a) Co-closedness.* Root covariance Q_ld = d ev (BFT_A §1.2) transposes to d*Q_l^T = ev^Td*. Applying d* to the level-0
equation (d*d* = 0, d*j_0 = 0) gives ev^T(d*ρ_0) = 0; ev^T places a level-1 function on the level-1 roots (distinct level-0
sites), so it is injective and d*ρ_0 = 0. If d*ρ_{l-1} = 0, d* of the level-l equation gives 0 = ev^Td*ρ_l - d*d*G_l - d*j_l =
ev^Td*ρ_l, so d*ρ_l = 0. Induction over l = 1, …, k - 1.
*(b)* Q_l^T = Q_{str,l}^T - h_l^Td* (transpose of BL-2 (b)'s one-step identity), so Q_l^Tρ_l = Q_{str,l}^Tρ_l on co-closed ρ_l.
*(c)* Iterate (b) from l = i + 1 to k - 1. Each source d*G_l + j_l is co-closed, so its composite transposes are the straight
ones (BL-2 (c)); r_i = (ρ_i + s_i)/κ_i. ∎ **RH-F1 does not occur.** (bb6 A2-A4: co-closedness 1.6e-12, 1.8e-11; funnel term
6.0e-12; transport formula with every source class 1.2e-12; control A5: the funnel term is 0.87·max|v| on a non-co-closed v.)

### 19.2 Lemma TC: PROVEN-HERE
BL-2 (c): on co-closed level-b currents, own |(Q_str^{(a→b)})^Tj| ≤ L^{-3(b-a)}||j||_own. For level-k ρ (own = coarse) and
a = i + 1: own ≤ L^{-3m}||ρ||, and level-(i+1) coarse 1-form units multiply by L^{k-1-i} = L^m: ≤ L^{-2m}||ρ||. For a level-l
current: own ≤ L^{-3(l-1-i)}L^{-3(k-l)}π_l(j) = L^{-3m}π_l(j), the same. A link lies in 2(d - 1) = 6 plaquettes, so
|d*G_l|_own ≤ 6L^{-2(k-l)}||G^c_l|| and π_l(d*G_l) ≤ 6L^{k-l}||G^c_l||. Inverse estimate (BL-2 (e) at level i + 1, ρ_{i+1} = L^{-m}):
||∇^cH^c|| ≤ 2L^m||H^c||, [∇^cH^c]_α ≤ L^{αm}||∇^cH^c||, so ||H||_{C^{1,α}} ≤ (1 + 2L^m + 2L^{(1+α)m})||H^c|| ≤ 5L^{(1+α)m}||H^c||;
pointwise, [·]^∞_α ≤ 2ρ^{-α}sup, giving 7. ∎ (bb6 A6 and B1: the bound L^{-2m} is attained (ratio 1.000 for m = 1, 2, 3); B2:
D_m/(2L^mS_m) = 0.925; B3: P_m/(2L^{αm}D_m) = 0.68-0.76.)

### 19.3 Theorem RH: PROVEN-HERE
By Lemma RT (c), subadditivity of ||·||_{C^{1,α}} and Lemma TC, for m = k - 1 - i ≥ 1:
  ||r_i||_{C^{1,α}} ≤ (5/κ_-)L^{(1+α)m}[||s^c_i|| + L^{-2m}||ρ_{k-1}|| + L^{-2m}Σ_{l=i+1}^{k-1}(π_l(j_l) + 6L^{k-l}||G^c_l||)].
- s-term: ||s^c_i|| ≤ L^{-θ(m+1)}L^{-m}||s||_R (ω^R_i = L^{θ(k-i)}), so the term is ≤ (5/κ_-)L^{-θ}L^{(α-θ)m}||s||_R; Σ_{m≥1}L^{(α-θ)m} =
  1/(L^{θ-α} - 1).
- Top term: (5/κ_-)L^{-(1-α)m}||ρ_{k-1}||, Σ_{m≥1} ≤ 1/(L^{1-α} - 1), and ||ρ_{k-1}|| ≤ κ_+||r^c_{k-1}|| + ||s^c_{k-1}|| (level k).
- Level-l sources enter r_i for i < l, i.e. m ≥ k - l: Σ_{m≥k-l}L^{-(1-α)m} = L^{-(1-α)(k-l)}/(1 - L^{-(1-α)}).
Summing over 0 ≤ i ≤ k - 2 gives the stated bound; 7 for N^∞_res. Nothing depends on k, T or the level beyond the displayed
geometric sums. ∎ **Reading.** No LES, LES-div, Caccioppoli or box-Neumann step is needed: below the top, every residual is the
transport of the top current plus the explicit sources of its own and higher levels; the transport gains L^{-2} per level in
coarse units (Q_str^T gains L^{-3} in own units), and the inverse estimate loses L^{1+α} < L². This is a d = 4 fact
(in d dimensions the gain is L^{-(d-2)}). bb6 B: the transported term saturates the inverse estimate up to a constant
(L^{(1-α)m}P_m/max|ρ| = 2.81, 2.52, 2.52 for m = 1, 2, 3; D_mL^m/max|ρ| = 1.85): **RH-F3 occurs [guess confirmed]**, harmlessly.

### 19.4 Corollary RH-inv: PROVEN as an implication; the α = θ example PROVEN-HERE
Bound each term of Theorem RH by the norms: ||r^c_{k-1}|| ≤ ||x||_inv; ||s^c_{k-1}|| ≤ L^{-θ}||s||_R; for (G) at l ≥ 1,
6L^{-(1-α)(k-l)}L^{k-l}||G^c_l|| ≤ 6L^{(α-θ)(k-l)}||G||_Y (ω_l = L^{θ(k-l)}), summable for α < θ; (Pl-c): π_l(j_l) ≤ L^{-θ(k-l)}||j||_{Pc};
rough plain currents w ∈ R_l: L^{-(1-α)(k-l)}π_l(w) = L^{-θ(k-l)}N_l(w); the BCH₂ rows R^B_l = 2κ_l⟨r_l, B(x_l, ·)⟩ at ||x||_𝔐 ≤ η
(own |r_l| ≤ L^{-2(k-1-l)}η, |x_l| ≤ L^{-(k-l)}η, |B| ≤ C_B') give π_l ≤ 2C_B'κ_+L²η², summable against L^{-(1-α)(k-l)}; (P0) j_0 and G_0 do not enter. **[RBB6-fix RS6-9: the BCH₂-row size in the preceding sentence is the in-place correction of 09:35:12 (session 6): a direct count replaced an imprecise SPD citation.] [RBB6-fix RS6-1 (binding): the BCH₂ rows enter here only when they are co-closed (lane A's scope, [RBA5-fix] U7); the co-closed completions d*W_l enter as (G)-slot sources (the (G) bound above); the non-co-closed remainder V_l (d*V_l = d*R^B_l, BFT_A §26.2) is outside Setting LIN and Lemma RT does not apply to it (its funnel terms are O(1), bb6 A5): (Res-Hölder) for its responses is OPEN. RS6-2: the commutator rows are residual-type sources (lane A's CR-1, ||s^C||_R ≤ κ_+L^θη²) and are covered by the s-term. RS6-8: C_B' is renamed C_bch here (it collides with C_B of 19.11).]** Hence
N_res(x) ≤ C_1||x||_inv + C_2||y||, C_1 := 5κ̂/(L^{1-α} - 1), C_2 explicit in (L, κ_-, α, θ). With (H-inv) (||x||_inv ≤ G||y||):
(H-inv+) holds with G_+ := (1 + C_1)G + C_2; the converse is trivial. **So Corollary EP-lin gives (W-lin-Π) for S_E from the
gauge-invariant (H-inv) alone, G_Π = C_rec((1 + C_1)G + C_2); the sum-versus-max gap of 16.7 is closed for α < θ.**
*α = θ.* T even, B_k = 0, at every level i ≤ k - 2 the checkerboard residual source s^c_i := a_i(-1)^{Σz}e_μ (level-(i+1) sites
z), a_i := L^{-θ(m+1)}L^{-m}, so ||s||_R = 1. Its coarse gradient alternates ±2L^ma_i, so on a box of two own steps
Osc_2 = 2L^ma_i and [∇^cs^c_i]_α ≥ 2^{1-α}L^{(1+α)m}a_i = 2^{1-α}L^{-θ}L^{(α-θ)m}. The other terms of r_i have
C^{1,α} ≤ (5/κ_-)L^{-(1-α)m}(κ_+G_R + L^{-θ}) (BL-5 (a): ||x||_inv ≤ G_R). At α = θ: ||r_i||_{C^{1,α}} ≥ κ_+^{-1}2^{1-α}L^{-θ} -
C'L^{-(1-α)m}, so N_res ≥ c(k - m_0) → ∞ while N^max_res stays bounded. ∎ **RH-F2 occurs exactly at α = θ.** Lane A's (¼, ½)
has α < θ.

### 19.5 Corollary RH-D: PROVEN as an implication
s = G = j = 0 in Theorem RH: N_res(y(B_k)) ≤ (5κ_+/κ_-)||r_{k-1}||/(L^{1-α} - 1), and ||r_{k-1}|| ≤ C_R sup|dB_k| ≤ 4C_R||B_k||_D
(LINEAR_PACKAGE Theorem 3.8, N2-lin). ∎ (L = 3, α = ¼: 5κ̂/(3^{3/4} - 1) = 3.91κ̂.)

### 19.6 Theorem RH_m: PROVEN-HERE **[post-proof correction: c_w = 12 (10 for the data map), not 8]**
Weights w(z) = e^{md(z,X_0)}, d the ℓ¹ coarse torus distance, w(z) ≤ e^{md(z,z')}w(z'). (Q_str^{(i+1→l)})^T at a fine μ-link b reads
level-l links whose blocks contain b - te_μ, t < L^{l-1-i} own steps: within ℓ¹ distance ≤ 5ρ_l ≤ 5. So every transported sup bound
holds weighted with e^{5m}. Inverse estimates: a coarse difference reads two points at distance ρ ≤ 1 (factor 1 + e^m ≤ 2e^m);
the weighted Campanato term w(z_B)ρ'^{-α}Osc_2(∇^cH; B) ≤ ρ'^{-α}e^{4m}||∇^cH||_{∞,m} (B of side ≤ 1, ℓ¹ diameter ≤ 4). So
||H||_{C^{1,α},m} ≤ 5e^{5m}L^{(1+α)t}||H||_{∞,m} **[RBB6-fix RS6-8: in 19.6 the depth k - 1 - i is written t (it was also written
m, colliding with the weight m); every L^{(·)m} in 19.6 that comes from Lemma TC or the inverse estimate reads L^{(·)t}, and every
e^{(·)m} is the weight]**. d*G_l reads plaquettes within distance 2. Collecting: the top and plain terms carry
e^{10m}, the G-terms e^{12m}, the s-terms e^{5m}: N_res,m ≤ e^{12m}·[Theorem RH with weighted norms]. For the data map only the top
term occurs: N_res,m(y(B_k)) ≤ e^{10m}(5κ̂/(L^{1-α} - 1))||r_{k-1}||_{∞,m} ≤ e^{10m}(5κ̂/(L^{1-α} - 1))G_D(m)||B_k||_{D,m}, using
Proposition W (BFT_A 13.9, PROVEN: the j = k - 1 residual component of ||y||_{inv,m} is ||r_{k-1}||_{∞,m}), 0 ≤ m < m_*'. ∎
This is **(Res-Hölder)_m for the data map: PROVEN** (as an implication of N2-lin / Theorem 6.8 (a) through Proposition W,
J-str and BL-2).

### 19.7 Corollary LRL(b)-E: PROVEN as an implication
Corollary EP-LRL(b) (16.8, with [RBB5-fix RS5-3]) states LRL (b) ⇐ (Res-Hölder)_m for T ≥ 5 with P_♯ = Π_E; Theorem RH_m supplies
(Res-Hölder)_m with C = e^{10m}5κ̂G_D(m)/(L^{1-α} - 1). Hence **lane A's LRL (b) holds for T ≥ 5, 0 ≤ m < m' < m_*'**, with
C_b = e^{c_rm}C_rec(G_D(m) + 1 + e^{10m}5κ̂G_D(m)/(L^{1-α} - 1)). Inputs: LES-div (PROOF, reviewed), Lemma Λ and Lemma LR-pot
(CONFIRMED), Proposition W, BL-2, BL-C, J-str, N2-lin; for m > 0 the factor e^{c_rm} rests on the ARGUED reach of LR-pot /
Lemma Λ (RS5-4). At m = 0 no reach statement is used. T = 3, 4: not covered. ∎ **[RBB6-fix RS6-3 (binding): T = 3, 4 are
covered by the periodic lift, Remark PL (§21.1, proof §22.1): LRL (b) holds for all T ≥ 3, C_b(T) ≤ e^{20m}C_b(2T) for T = 3, 4.
The exclusion was harmless for lane B's consumers in any case (local tori of side ≥ T^Π_W = 4R + 22 ≥ 86). [RBB7-fix RS7-1: planned at the time of this tag, Step 1 10:23; proof written 10:38] [RBB7-fix RS7-2: the constant e^{20m} of this tag is the correct one; §22.1's post-proof correction (1) is withdrawn (REVIEW_BFT_B_S7 B.1)]]**

### 19.8 Lemma NF-crit: PROVEN-HERE
For |w| small, d/ds log(e^we^{sY})|_0 = φ_1(ad_w)Y, φ_1(z) := z/(1 - e^{-z}) [the standard dexp^{-1} formula]. Since
e^{sξ}e^we^{-sη} = e^we^{s(e^{-ad_w}ξ - η) + O(s²)}, d/ds log(e^{sξ_x}W(b)e^{-sξ_y})|_0 = φ_2(ad_w)ξ_x - φ_1(ad_w)ξ_y, φ_2(z) := z/(e^z - 1).
ad_w is skew for the Ad-invariant inner product and ad_ww = 0, so ⟨w, φ(ad_w)ζ⟩ = ⟨φ(-ad_w)w, ζ⟩ = φ(0)⟨w, ζ⟩ = ⟨w, ζ⟩. Hence,
along g ↦ e^{sξ}g, dΦ/ds = 2Σ_{b=(x,y)}⟨w(b), ξ(x) - ξ(y)⟩ = -2Σ_z⟨ξ(z), (d*w)(z)⟩ (Neumann divergence). On {g(c_X) = 1} (ξ(c_X) = 0)
criticality is d*w = 0 at z ≠ c_X; Σ_z(d*w)(z) = 0 identically (each link once at each end), so also at c_X. ∎ **The nonabelian
box-Coulomb condition is exactly the linear Neumann condition d*log U^g = 0.** (bb6n N1: max|d*w| = 1.0e-12.)

### 19.9 Lemma NF-uniq: PROVEN-HERE
Let g_1, g_2 ∈ 𝒲_δ be critical, W_i := U^{g_i}, w_i := log W_i, max n|w_i| ≤ δ, κ := g_2g_1^{-1}. Then W_2(b) = κ(x)W_1(b)κ(y)^{-1}, so by
bi-invariance d(κ(x), κ(y)) ≤ |w_1(b)| + |w_2(b)| ≤ 2δ/n, and (ℓ¹ paths of length ≤ 8n from c_X, κ(c_X) = 1) d(κ(z), 1) ≤ 16δ.
*Shift.* The map ζ ↦ -avg_z log κ(z) - R(ζ), R(ζ) := avg_z[log(e^ζκ(z)) - ζ - log κ(z)] = O((|ζ| + 16δ)²) (BCH), maps
{|ζ| ≤ 40δ} into itself and contracts for δ ≤ δ_1(N); its fixed point gives a := e^ζ with avg_z log(aκ(z)) = 0. g_2' := ag_2 is
critical (Φ(ag) = Φ(g); U^{ag} = Ad_aU^g) with the same |w|; ξ := log(g_2'g_1^{-1}) is mean-zero, |ξ| ≤ 60δ, |dξ(b)| ≤ C_1·2δ/n
**[RBB6-fix RS6-8: this C_1 (the Lipschitz constant of log near 1) is renamed C_ℓ; C_1 is 19.4's constant. Likewise in §18-§19
Φ_{U,X} is the box functional and the S_0 kernel φ^{⊗d} of Construction GC is renamed Φ_0]**.
*Convexity.* g_t := e^{tξ}g_1, W_t(b) = e^{tξ_x}W_1(b)e^{-tξ_y}, max|log W_t| ≤ Cδ/n. f(t) := Φ(g_t) has f'(0) = f'(1) = 0 (g_1, g_2'
critical on the whole gauge group: d*w = 0 everywhere). f''(t) = Σ_b[2|D_b|² + 2⟨w_t(b), E_b⟩] with D_b = φ_2(ad_w)ξ_x - φ_1(ad_w)ξ_y,
|D_b - dξ(b)| ≤ C|w|(|ξ_x| + |ξ_y|), and E_b (the s²-coefficient ×2) = -[ξ_x, ξ_y] + O(|w||ξ|²) = [ξ_x, dξ(b)] + O(|w||ξ|²) (BCH at
w = 0: log(e^{sξ_x}e^{-sξ_y}) = s(ξ_x - ξ_y) - (s²/2)[ξ_x, ξ_y] + O(s³)). D_b is linear and E_b quadratic in ξ, with coefficients
depending on w only. By Cauchy-Schwarz, max|w_t| ≤ Cδ/n and the Neumann Poincaré inequality ||ξ|| ≤ ((4n + 1)/2)||dξ|| (path-graph
gap 4sin²(π/2S) ≥ 4/S², S = 4n + 1; tensor products; componentwise): f''(t) ≥ 2||dξ||² - C_2(δ + δ²)||dξ||² ≥ ||dξ||² for
δ ≤ δ_0(N). Since ∫_0^1f'' = 0, dξ = 0; ξ is constant and mean-zero, so ξ = 0, g_2' = g_1, and at c_X: a = 1, g_2 = g_1. ∎
All constants depend on N (BCH and analytic bounds on a small ball) and d only: the sup bound δ/n and the Poincaré factor n
cancel. **NF-F1 does not occur.** (bb6n N2: four starts agree to 3.2e-11.)

### 19.10 Lemma NF-cov: PROVEN-HERE
Φ_{U^h}(g') = Φ_U(g'h) and left variations correspond (e^{sξ}g' ↔ e^{sξ}g'h), so g' is critical for U^h iff g'h is critical for U.
With g' := h(c_X)gh^{-1}: g'h = h(c_X)g is critical (left-constant invariance), g'(c_X) = 1, and (U^h)^{g'} = Ad_{h(c_X)}U^g has the same
|log|, so g' ∈ 𝒲_δ(U^h). By NF-uniq it is the normal form. h ≡ c gives g_X(U^c) = cg_X(U)c^{-1}. ∎ No smallness of h is used.
(bb6n N3: Haar-random h, agreement 1.4e-11.)

### 19.11 Lemma REF and (N1-bd): PROVEN-HERE given (N1-G)
Local box coordinates {0, …, S - 1}⁴, S = 4n + 1; 𝕋_R := (Z/2SZ)⁴ with reflections ϱ_ν: z_ν ↦ -1 - z_ν. Each site of 𝕋_R is ϱ_Az for
a unique box site z and A ⊂ {1..4}. Scalars: f^R(ϱ_Az) := f(z). 1-forms: for μ ∉ A, w^R_μ(ϱ_Az) := w_μ(z); for μ ∈ A the link at ϱ_Az
is the reversed image of the box link (z - e_μ, z): w^R_μ(ϱ_Az) := -w_μ(z - e_μ); links crossing a reflection plane get 0. Then
(d(f^R) = (df)^R); the μ-component is odd under ϱ_μ, so it has mean zero; d*w^R at a site equals the box Neumann divergence at
its preimage (crossing links carry 0), so d*w^R = 0; dw^R = (dw)^R (a plaquette crossing the μ-plane has its two μ-links 0 and
its two transverse links equal), so sup|dw^R| = sup|dw|. On the torus, a co-closed mean-zero 1-form satisfies
w^R = Δ^{-1}(d*d + dd*)w^R = d*Δ^{-1}(dw^R) (componentwise lattice identity; harmonic 1-forms are constants, removed by mean zero).
Each component is a sum of ≤ 3 differences of G_M against a plaquette component, so by (N1-G) sup|w| ≤ 3C_GM sup|dw| ≤ 30C_Gn sup|dw|
(M = 2S ≤ 10n), i.e. **sup_Ñ|w^c| ≤ C_B sup_Ñ|(dw)^c|** with C_B := 60C_G (crude). ∎ **[RBB6-fix RS6-6: with Lemma N1G
(C_G = ¼, §22.2) this is PROVEN-HERE with no import: C_B ≤ 15 (in fact 30C_G = 7.5 suffices). Theorem NF-ex and Proposition KΠ
are then PROVEN (given only the cited Karcher facts for KΠ). [RBB7-fix RS7-1: planned at the time of this tag, Step 1 10:23; proof written 10:38]]** **NF-F2 does not occur:** the operator is d*Δ^{-1},
of degree -1, so the boundary-induced jumps of the reflected curvature cost nothing (a degree-0 operator would lose a logarithm).

### 19.12 Theorem NF-ex: PROVEN given (N1-G) **[post-proof correction: hypothesis also max_{t∈[0,1]}ε_f(e^{tA}, X) ≤ ε_0]**
**[RBB6-fix RS6-9: §18.2's pre-stated NF-ex contains a dangling "2C_B(ε_f(U, X) + C_{BCH}ε_0²)... more precisely"; the first
expression is withdrawn and the bound is the second one, max n|w| ≤ 2C_B·max_tε_f(e^{tA}, X) (annotated here; §18 not edited).
RS6-6: with Lemma N1G this theorem is PROVEN-HERE.]**
U_t := e^{tA}, ε_* := max_tε_f(U_t, X) ≤ ε_0 (e.g. max n²|dA| + C(max n|A|)² ≤ ε_0). *A priori bound.* At a critical point
g ∈ 𝒲_δ(U_t): d*w = 0 (NF-crit) and dw(p) = log W(∂p) - B_p with |B_p| ≤ C_3(max|w|)² (BCH) and |log W(∂p)| = |log U_t(∂p)|
(conjugation); (N1-bd) gives max n|w| ≤ C_B(ε_* + C_3δ·max n|w|), so with δ := min(δ_0, 1/(2C_BC_3)): max n|w| ≤ 2C_Bε_*. Require
2C_Bε_* ≤ δ/2. *Continuation.* 𝒯 := {t : Φ_{U_t} has a critical point in 𝒲_δ}. 0 ∈ 𝒯 (g = 1). Closed: compactness of SU(N)^{Ñ} and
continuity of the critical equation and of the closed condition. Open: at g_t (in 𝒲_{δ/2} by the a priori bound) the Hessian on
{ξ(c_X) = 0} is nondegenerate: constant directions lie in its kernel at a critical point (critical orbit {ag}), so
H(ξ) = H(ξ - ξ̄) ≥ ||dξ||² (19.9's quadratic estimate, valid for all ξ), and ξ(c_X) = 0, ξ ≠ 0 forces dξ ≠ 0; the finite-dimensional
implicit function theorem continues g_t, inside 𝒲_δ for nearby t. So 𝒯 = [0, 1]; uniqueness by NF-uniq. ∎ The normal form is
real-analytic in U (IFT); its holomorphic extension to complex U near real ones is ARGUED (nondegeneracy is open).
bb6n N6: with a rough random input (ε_f(U) = 2.0, outside the theorem's hypotheses) the normal forms still exist with
max n|w| = 0.243 (informational).

### 19.13 Proposition KΠ: PROVEN given NF-ex and the Karcher facts **[post-proof correction (4)]**
*Domain.* If U = (e^A)^k on Ñ_X with e^A as in NF-ex, g_X(U) := k(c_X)g_X(e^A)k^{-1} (well defined by NF-cov). For U = e^A small in one
level-0 gauge, d(g_X(y), g_X(x)) ≤ |w(b)| + |A(b)| along links, so d(g_X(z), 1) ≤ 8(2C_Bε_* + max n|A|) for z ∈ N_X: the ≤ 16 points
lie in a small ball. *Roots.* χ^5_X(c_Y) = δ_XY gives G(U)(c_Y) = g_Y(c_Y) = 1. *Root-value formula.* For a level-0 gauge k whose
points {k(c_X)g_X(U)(z)} lie in a Karcher ball: NF-cov and right-equivariance of M give G(U^k)(z) = M[k(c_X)g_X(U)(z)]·k(z)^{-1}, so
Π^{NA}(U^k) = U^{G(U^k)k} = Π^{NA}(U)^{ĥ}, **ĥ = M_{χ^5}[k(c_X)g_X(U)]·M_{χ^5}[g_X(U)]^{-1}**, ĥ(c_Y) = k(c_Y). The identity
Π(U^k) = Π(U)^{G(U^k)kG(U)^{-1}} holds for any U ↦ U^{G(U)} with G = 1 at roots; the content is that ĥ depends on k **only through its
root values** (and on U), whatever k does between roots. *Idempotence.* With k := G(U) (G = 1 at roots): G(U^G) = M[g_X(U)]G^{-1} = 1,
so Π^{NA}(Π^{NA}(U)) = Π^{NA}(U); S^{NA} is its image. *Constants:* k ≡ a gives ĥ = a. *Smooth extension.* At U = 1, g_X = 1 and
ĥ = M_{χ^5}[k(c_X)], the Karcher-tent interpolation of the root values: C^{2,1} in coarse units (χ^5 ∈ C^{2,1}, M real-analytic in
the weights on a ball), with norms ≲ max d(k(c_X), k(c_Y)) over corners of a cell. *Linearisation.* g = e^λ, U = e^{εa}: U^g = a - dλ
to first order, and d*(a - dλ) = 0 with λ(c_X) = 0 is λ = -λ^E_X(a); M linearises to the weighted average; so Π^{NA} linearises to
x ↦ x + DΛ = Π_E. *Range* 4 as in EP-alg. ∎ **NF-F3 does not occur.** **CL-F4 does not occur on 𝒞_glob:** if V and V^h are both in
𝒞_glob(ε), h(X) = V^h(X, Y)h(Y)V(X, Y)^{-1} gives d(h(X), h(Y)) ≤ 2ε for neighbours, so the Karcher condition holds for small ε.
**[RBB6-fix RS6-4 (binding): CL-F4 OCCURS on GI-off's class and for large gauges: Π^{NA} is defined only where neighbouring box
normal forms agree to O(ε) at the shared points (on GI-off's class the corner points g_X(U)(z) differ by the coarse transports;
REVIEW_BFT_B_S6 D.7). RS6-9: the domain 𝒟(ε) carries both NF-ex hypotheses, max n|A| ≤ ε and max_tε_f(e^{tA}, X) ≤ ε_0.]**
(bb6n N4: G(c_Y) = 1 to 3e-18; idempotence 3.0e-12; covariance with Haar-random h off the roots 5.6e-12; control N5: gluing in
exponential coordinates violates the root-value formula by 0.34.)

### 19.14 Lemma GC-lin: PROVEN-HERE
Σ_iΦ(z - i) = 1 (S_0 reproduces constants). (1) μ(dν)(z) = Σ_iΦ(z - i)(ν(X(z)) - ν(i)) = (C_0ν - S_0ν)(z), and S_1d = dS_0 (CL-lin (a)), so
R(dν) = dS_0ν + d(C_0 - S_0)ν = dC_0ν. (2) dRB = dS_1B (dd = 0). (3) ev μ(Y) = μ(c_Y) = Σ_iΦ(c_Y - i)∫_{a(i→Y)}B = ∫_{a(Y→Y)}B = 0
(interpolatory: Φ(c_Y - i) = δ_{iY}), so Q_axRB = Q_axS_1B + d ev μ = B. (4) μ reads B on axial paths of ≤ d(r_s + 1) coarse links from
the ≤ (2r_s)^d sites i in Φ's support; summed over levels, a geometric range. ∎ *Consequence at the linear level:* the R-chain and
the S_1-chain differ by composite gauge directions vanishing at the level-k roots (μ vanishes at roots and C_0 preserves that), so
Π_E∘(R-chain) = Π_E∘Z^lin, and ||Π_EZ^lin(B)||_X ≤ C_Π·3C(φ, d)||B||_∞ (EP-bd + CL-lin (d), DD8 regularity PROVEN): **the
linearisation of Z^{KΠ} satisfies (CovLift) (iv) first clause k-uniformly, with the tent-interpolation extension (CL-Φ).**

### 19.15 Proposition AX-cov: PROVEN-HERE **[post-proof correction (6): the linearisation is proven here]**
Under Z ↦ Z^h (level-(j+1) gauge h): P_{X←i} ↦ h(X)P_{X←i}h(i)^{-1}, so A^X ↦ Ad_{h(X)}A^X; s^X is linear in A^X, so exp(s^X(b)) ↦
h(X)exp(s^X(b))h(X)^{-1}; Z(X, X') ↦ h(X)Z(X, X')h(X')^{-1}. Hence R^{ax}(Z^h)(b) = h(X)R^{ax}(Z)(b)h(X')^{-1} = R^{ax}(Z)^{C_0h}(b) for
b = (z, z'), z ∈ X, z' ∈ X'. Constants: the same with h ≡ c. Range: A^X near X reads Z on the axial paths used by S_1 and μ. *Linearisation*
(Z = e^B; ψ_X(i) := ∫_{a(i→X)}B; A^X is B in the axial gauge at X, so ∫_{a(i→X)}A^X = 0, A^X = B + dψ_X up to the sign fixed by that
condition): inside block X, μ(A^X) = 0 and s^X = S_1A^X = S_1B + dS_0ψ_X = S_1B + dμ(B) (μ(B) = S_0ψ_X on block X). On a face link
from X to X' = X + e_μ: s^X(b) = S_1B(b) + S_0ψ_{X'}(z') - S_0ψ_X(z) + ψ_X(X'), and ψ_X(X') = -B(X, X') (the axial path from X' to X is
that link reversed), so s^X(b) + B(X, X') = RB(b). ∎ Iterating, R^{ax}_0∘…∘R^{ax}_{k-1}(V^h) = (…)(V)^K with K(z) := h(X_k(z)) (the
level-k block of z), a chain gauge restricting to h at level k.

### 19.16 Theorem CovLift-KΠ: PROVEN as an implication for (i)-(iii) **[post-proof correction (3): given (N2-0)]**; (iv), (v) OPEN
**(N2-0)** := for V ∈ 𝒞_glob(ε), the level-0 field of the R^{ax}-chain is, on every Ñ_X, gauge-equivalent to some e^A with
max n|A| ≤ ε_0 and max_tε_f(e^{tA}, X) ≤ ε_0 (k-uniformly; its linear version is CL-lin (d) for the S_1-chain, PROVEN).
**[RBB6-fix RS6-5 (binding): restated per level with quantifiers as (N2-0)_j, §21.0 (ε_1 = ε_1(L, φ, N, d), independent of k, T,
j; clauses (a) curvature, (b) axial stencil size at every level, (c) the level-0 box clause above); proof §22 (Theorem N2). [RBB7-fix RS7-1: planned at the time of this tag, Step 1 10:23; proof written 10:38]]**
Given (N1-G) and (N2-0): the box normal forms exist (NF-ex) and Π^{NA} is defined (KΠ). (i) By AX-cov the chain obeys
Z(V^h) = Z(V)^K, K(c_X) = h(X); by KΠ (Karcher condition: CL-F4 does not occur on 𝒞_glob), Z^{KΠ}(V^h) = Z^{KΠ}(V)^{ĥ},
ĥ = M_{χ^5}[h(X)g_X]·M_{χ^5}[g_X]^{-1}, which restricts to h at level k **[RBB6-fix RS6-4 (binding): for every level-k gauge h
with max_{X∼Y}d(h(X), h(Y)) ≤ cε (V, V^h ∈ 𝒞_glob(ε)); for large gauges the Karcher condition fails (CL-F4 OCCURS)]**; the cocycle and ĥ(c, ·) = c follow from Lemma CL-uniq;
at V = 1, ĥ is the Karcher-tent interpolation of h (smooth: the CL-blk obstruction is avoided). (ii) Finite range: R^{ax} (finite
DD8 mask, axial paths) and Π^{NA} (boxes of radius 3). (iii) Coarse translations act on masks, axial paths, boxes and tents
covariantly; constants by AX-cov and KΠ. ∎ *(iv), (v): OPEN.* **[RBB7-fix RS7-5: (N1-int) and (N2-bd) are to be read in local form (on Ω^{(-r)} given V^h = e^b on Ω, constants independent of V outside Ω): §24.2]** They need (N1-int) (k-uniform interior C^{2,α} of the box normal forms:
the nonlinear EP-int, a bootstrap of 16.2 with the BCH quadratic terms of 19.12 as divergence-form sources) and (N2-bd) (k-uniform
C^{1,α} bounds and residual sizes of the iterated R^{ax}: the BCH absorption (R3)); plus the C_g clause at θ > 0 (RS5-5). Their linear
parts are PROVEN (19.14).

## 20. Session-6 check record, outcome and notes for other files (written after §19)

**Checks** (criteria checks/bb6_criteria.md, bb6m_criteria.md, bb6n_criteria.md born 09:23:17 UTC; bb6_criteria.md's control A5
replaced at 09:25:02, before its script existed, because the original control (a non-co-closed j_1) has no critical point; scripts
checks/bb6m_mask.py born 09:25:33, bb6_transport.py 09:26:41 (one pre-run edit: CG iteration cap 30000 → 6000), bb6n_nf.py born
09:27:26, one pre-run edit 09:27:59 (principal SU(2) log without sign flip; unpinned descent normalised at c_X afterwards); no
criterion touched). Runner scratchpad bb6/run_bb6.sh: one lock acquisition 09:28:23-09:29:14 (load1 2.86, memory free 38%; nice 10;
thread variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3 without -I; no `timeout`; no trap; `rmdir` once). No process
left; no __pycache__ in checks/. (The lock directory seen at 09:32 was created at 09:32:18 by another worker.)
- **bb6m (RS5-10): ALL PASS.** 0.38 s, 95 MB. DD8: β_10 = 0.4732 (ρ_n < 1 from n = 2); DD6: β_10 = 0.2677; DD4: ρ_n = 1.2222 for all
  n ≤ 10 (no certificate); exact residue sums and σ³-divisibility; DD4 weights (-5, 60, 30, -4)/81. **Reproduces REVIEW_BFT_B_S5
  Part D's lower bounds exactly** (0.4732, 0.2677; DD6 at n = 7, 8: 0.2454, 0.2547).
- **bb6n: ALL PASS (N1-N5).** 45.1 s, 35 MB. N1 max|d*w| = 1.0e-12; N2 uniqueness 3.2e-11; N3 covariance under Haar-random h
  1.4e-11; N4 (a) 3.4e-18, (b) 3.0e-12, (c) 5.6e-12 and ĥ(c_Y) = h(c_Y) to 2.9e-17; N5 control: exponential-coordinate gluing
  deviates by 0.336. N6: n max|w| = 0.243, ε_f(U) = 2.02 (rough input), max|log ĥ| = 0.200 (= the root-value spread).
- **bb6: ALL PASS (A0-A6, B1-B3).** 5.8 s, 559 MB. A0 1.5e-15; A1 CG 172 iterations, residual 8.7e-14; A2 1.6e-12 / 1.8e-11;
  A3 6.0e-12; A4 1.2e-12; A5 control 0.87; A6 ratio 1.000; B1 S_mL^{2m}/max|ρ| = 1.0000 (m = 1, 2, 3); B2 0.925; B3 0.76, 0.68, 0.68;
  B4 [guess] holds (factor 1.118).
- *Reading (measured only).* The transport identity and the co-closedness hold at a numerical critical point with every source
  class; the funnel term is large off co-closed forms. The transported top term attains the coarse sup bound L^{-2m} and saturates
  the inverse estimate (gradient ∝ L^{-m}, gradient-Hölder ∝ L^{-(1-α)m}). In d = 2 SU(2) the box normal form is unique from several
  starts, exactly covariant under arbitrary gauges, and the Karcher-glued slice is idempotent with an extension that depends only
  on the gauge's root values; gluing in exponential coordinates does not have that property. Not measured: k ≥ 3 solves, d = 4
  nonabelian normal forms, the (N1-G) constant, nonlinear (iv) bounds.

| Item (session 6) | Status | Note |
|---|---|---|
| Binding and cosmetic fixes of REVIEW_BFT_B_S5 (RS5-1..RS5-10) | applied, tagged [RBB5-fix] | GI-F2 cannot occur; ⟨πy, w⟩; EP-LRL(b) T ≥ 5, N_res,m defined; weighted reach ARGUED; CL-lin "(i)-(iv) first clause, (v)"; 2^{44}; ε_mix k-uniform; CL-blk sup threshold; CL-uniq conditions; item-8 forward reference disclosed; DD8 adopted |
| Lemma RT | PROVEN-HERE | exact residual transport; ρ_l co-closed at every critical point |
| Lemma TC | PROVEN-HERE | transported coarse sups L^{-2m}; inverse estimate 5L^{(1+α)m} |
| **Theorem RH ((Res-Hölder), m = 0)** **[RBB6-fix RS6-8: = Theorem RHT; RH_m = RHT_m]** | **PROVEN-HERE** | N_res ≤ explicit gauge-invariant/source bound, k-, T-, level-uniform; no elliptic step needed (d = 4: 2 > 1 + α) |
| **Corollary RH-inv** | **PROVEN as an implication** | (H-inv+) ⟺ (H-inv) for α < θ; (W-lin-Π) for S_E ⇐ (H-inv) alone; α = θ: sum diverges (example) **[RBB6-fix RS6-1: on the level-wise co-closed Setting-LIN classes only (incl. commutator rows, co-closed BCH₂ rows, completions d*W_l); the non-co-closed BCH₂ remainder V_l is outside Lemma RT: OPEN]** |
| Corollary RH-D | PROVEN as an implication | data map: N_res ≤ 3.91κ̂·4C_R||B_k||_D (L = 3, α = ¼) |
| **Theorem RH_m** | **PROVEN-HERE** | weighted, c_w = 12 (10 for data) [post-proof correction]; (Res-Hölder)_m for the data map PROVEN |
| **Corollary LRL(b)-E** | **PROVEN as an implication** | **lane A's LRL (b) holds for T ≥ 5** with P_♯ = Π_E; m > 0 constant rests on ARGUED reach (RS5-4); T = 3, 4 not covered **[RBB6-fix RS6-3: T = 3, 4 by the periodic lift (Remark PL, §22.1): all T ≥ 3, C_b(T) ≤ e^{20m}C_b(2T)]** |
| Lemma NF-crit | PROVEN-HERE | nonabelian box-Coulomb condition ⟺ Neumann d*log U^g = 0 exactly |
| **Lemma NF-uniq** | **PROVEN-HERE** | nonabelian normal-form uniqueness in 𝒲_δ, δ_0(N) n-, k-, T-independent |
| Lemma NF-cov | PROVEN-HERE | g_X(U^h) = h(c_X)g_X(U)h^{-1} for every gauge h |
| Lemma REF, (N1-bd) | PROVEN-HERE given (N1-G) **[RBB6-fix RS6-6: PROVEN-HERE; (N1-G) = Lemma N1G, C_G = ¼]** | exact reflection to the doubled torus; degree -1 operator, no log loss |
| Theorem NF-ex | PROVEN given (N1-G) **[RBB6-fix RS6-6: PROVEN-HERE]** | existence by continuation; needs small coarse curvature [post-proof correction] **[RBB6-fix RS6-9: its domain 𝒟(ε) in KΠ carries both hypotheses: max n|A| ≤ ε and max_tε_f(e^{tA}, X) ≤ ε_0]** |
| Proposition KΠ | PROVEN given NF-ex + Karcher facts | nonabelian elliptic slice: idempotent, root-value extension formula, smooth extension, linearises to Π_E |
| Lemma GC-lin | PROVEN-HERE | gauge-commuting linear DD8 refinement; linearised Z^{KΠ} obeys (iv) first clause |
| Proposition AX-cov | PROVEN-HERE | framed nonabelian DD8 refinement, exactly orbit-covariant (block-constant extension); linearisation = GC |
| **Theorem CovLift-KΠ** | **(i)-(iii) PROVEN as an implication of (N1-G) + (N2-0); (iv), (v) OPEN** | wall: (N1-int) nonlinear interior Schauder of the normal forms; (N2-bd) BCH absorption (R3) for the iterated R^{ax}; C_g clause at θ > 0 **[RBB6-fix RS6-4 (binding): (i) holds for level-k gauges h with max_{X∼Y}d(h(X), h(Y)) ≤ cε (V, V^h ∈ 𝒞_glob(ε)), not for every level-k gauge; CL-F4 OCCURS off 𝒞_glob (GI-off's class) and for large gauges; the new wall (KΠ-off) is addressed in §22 (Theorem KΠ-off). RS6-5: (N2-0) restated per level with quantifiers, §21.0; RS6-6: (N1-G) = Lemma N1G]** |
| Failure modes | RH-F1 does not occur; RH-F2 occurs exactly at α = θ; RH-F3 occurs [guess confirmed], harmless; NF-F1, NF-F2, NF-F3 do not occur; CL-F4 does not occur on 𝒞_glob | **[RBB6-fix RS6-4: CL-F4 OCCURS off 𝒞_glob and for large gauges (REVIEW_BFT_B_S6 D.7)]** |
| bb6m, bb6n, bb6 | ALL PASS (3/3) | bb6m reproduces REVIEW_BFT_B_S5 Part D exactly |

**What the slice route rests on now.** (W-Π): PROVEN (S_E). (W-lin-Π) for S_E ⟺ (H-lin^∇) in the best gauge ⟸ **(H-inv) alone**
(lane A's gauge-invariant bound ||x||_inv ≤ G||y||_Y; the residual-gradient half is Theorem RH). LRL (b): PROVEN for T ≥ 5.
(CovLift): exact nonabelian covariance with smooth extension constructed (Z^{KΠ}), modulo (N1-G) and (N2-0); the quantitative
clauses (iv), (v) are the nonlinear bootstrap (N1-int) + (N2-bd). Largest levers now: (H-inv) for the remaining source classes
(lane A: (CO-0)/(CO-up) beyond the rough and carrier-decaying classes); (N2-bd) = (R3); a proof of (N1-G) on the framework.
**[RBB6-fix RS6-6: (N1-G) is now Lemma N1G (C_G = ¼, IMPORTED-AND-REVERIFIED from REVIEW_BFT_B_S6 D.4), not a lever. RS6-4: the
(CovLift) sentence holds on 𝒞_glob for small gauges only; off 𝒞_glob see §22 (Theorem KΠ-off).]**

## FOR OTHER FILES (session 6; for their owners; not edited)
- **BFT_A (lane A).** (1) (Res-Hölder) is proven (Theorem RH, RH_m): for α < θ the residual-gradient size of every response is
  bounded by ||x||_inv and the source norms; so LRL (b) holds for T ≥ 5 (Corollary LRL(b)-E) and the gauge-variant half of
  (H-lin^∇) needs nothing beyond (H-inv). (2) BFT_A's BL-5/B7' transport remark is the source-free case of Lemma RT; Lemma RT (c)
  adds the explicit plain and divergence-form sources. (3) (N1-G) is the BA-7 Green-function import; a framework proof of
  Σ|∇G_M| ≤ C_GM would also discharge (N1-bd). **[RBB6-fix RS6-1, RS6-6, RS6-8: (1) reads "for every level-wise co-closed
  Setting-LIN class (not the non-co-closed BCH₂ remainder V_l, whose (Res-Hölder) is OPEN)"; Theorem RH is Theorem RHT. (3): the
  ℓ¹ bound is proven (Lemma N1G, C_G = ¼, REVIEW_BFT_B_S6 D.4); lane A's pointwise BA-7 is not needed for (N1-bd).]**
- **REVIEW (next lane-B review).** Check first: Theorem RH's claim that no elliptic step is needed (19.3) and its α = θ example;
  Lemma NF-uniq's mean-zero shift and convexity estimate (19.9); Lemma REF's reflection of 1-forms (19.11); Proposition KΠ's
  root-value formula and post-proof correction (4) (19.13); AX-cov's linearisation signs (19.15).
- **HIST / SF.** Unchanged.

# Session 7 (2026-10-28 UTC)

## 21. PRE-STATED (session 7) — statements only; the FIRST edit of session 7 (appended before any [RBB6-fix] edit, before any session-7 proof, criteria file or script). Nothing in §21 cites a result of this session. Reading of REVIEW_BFT_B_S6, §18-§20, the log, BFT_B §12.2/13.7/13.8/16.13, HIST §20.2 and checks/bb5, bb6n preceded this append, with exploratory reasoning (not recorded); its only claim is file order. Proofs follow in §22, later. Lead decision (session 7): both BFT lanes use the elliptic slice S_E (§16) as the single gauge fixing.

### 21.0 Definitions
- **Coarse curvature per level.** For a chain (Z_0, …, Z_k), ρ_j := L^{-(k-j)}, and a level-j plaquette p:
  F_j(p) := ρ_j^{-2}log Z_j(∂p) (principal log, based at p's first corner), **f_j := max_p|F_j(p)|** (gauge invariant). f_k is the
  level-k plaquette size of V (own = coarse).
- **Axial stencil size.** For a level-(j+1) site X, A^X as in Construction GC (§18.0); a_{j+1} := max_X max_{stencil links}
  ρ_{j+1}^{-1}|A^X| (coarse 1-form units); D_ax := the maximal number of level-(j+1) plaquettes in the axial ladder spanning
  the loop a(i→X)·(i, i + e_ν)·a(i + e_ν→X)^{-1} over the stencil links (a finite number fixed by d and the DD8 support r_s).
- **The locally-small class** 𝒦(ε) := {V : f_k(V) ≤ ε} on any coarse torus (GI-off's class: no global gauge, holonomies, torons
  and nonzero topological charge allowed). 𝒞_glob(ε) ⊂ 𝒦(4ε + Cε²).
- **Composite refinement kernels.** S_2 := the 2-form refinement of the commuting tensor pair (dS_1 = S_2d; on μν-components
  s^{[1]} ⊗ s^{[1]} ⊗ s ⊗ s); W^{(t)}(p, P) := the matrix of S_2^{(t)} (level j + t → level j). **Λ_2 := sup_{t≥0}max_pΣ_P|W^{(t)}(p, P)|**,
  Λ_2^{(1)} := the t = 1 value; Λ_2' := sup_t of the Lipschitz constant of p ↦ W^{(t)}(p, ·) in ℓ¹, per level-j coarse step ρ_{j+t}.
- **(N2-0)_j (per level, with quantifiers; fix RS6-5).** There are ε_1 > 0 and C_N, C_ax, C_box < ∞ depending only on
  (L, φ, N, d), independent of k, T, j and of any global gauge, such that for every V ∈ 𝒦(ε_1) and every 0 ≤ j ≤ k:
  (a) f_j ≤ C_Nf_k; (b) a_{j+1} ≤ C_axρ_{j+1}f_k (j < k), so every principal log in R^{ax}_j is defined; (c) (j = 0) on every Ñ_X
  the level-0 field is, in the complete axial gauge of Ñ_X, e^A with n max|A| ≤ C_boxf_0 and max_{t∈[0,1]}ε_f(e^{tA}, X) ≤ f_0 + C_boxf_0².
  (N2-0) := (N2-0)_j for all j. Its j = 0 clause (c) is the input of NF-ex; (a), (b) are what R^{ax}_j needs at level j.
- **The C_g clause at θ > 0 (fix RS6-7).** (CovLift) (iv)'s ||g_Z||_Y ≤ C_g||b||_∞, residual component, written out: whenever
  V = e^b on Ω in some level-k gauge with ||b||_∞ ≤ ε_Z, then for Z := Z^sm(V) and every 0 ≤ l ≤ k - 1, on Ω^{(-r_Z)},
  **(C_g-θ)  κ_lL^{θ(k-l)}ρ_{l+1}^{-2}|r_l(Z)|_own ≤ C_g||b||_∞**, r_l(Z) the functional's level-l residual (lane A's S4' root map Q;
  linearised r_l = Q_lZ_l - Z_{l+1}). [ω^R_lL^{k-1-l}||r^c_l|| = L^{θ(k-l)}ρ_{l+1}^{-2}||r_l||_own, as in 16.13 (e).] The non-residual
  components of g_Z keep their θ = 0 status (RS5-5).
- **Cut-off geodesic interpolation.** r_inj := the injectivity radius of the bi-invariant metric of SU(N) (principal log analytic on
  d(1, c) < r_inj); 0 < r_1 < r_2 < r_inj; ψ ∈ C^∞, ψ = 1 on [0, r_1], ψ = 0 on [r_2, ∞). For a, b ∈ SU(N):
  m_0(a, b) := a, m_1(a, b) := b, and for 0 < w < 1: **m_w(a, b) := a·exp(wψ(d(a, b))log(a^{-1}b))**.
- **Construction KΠ-off (iterated cut-off gluing).** For a level-0 site z in the coarse cell with corners X_ε (ε ∈ {0, 1}^d
  relative to the lower corner) and offsets t_ν ∈ [0, 1): P^{(0)}_ε := g_{X_ε}(U)(z) (box normal forms, §18.0); for ν = 1, …, d,
  P^{(ν)}_{ε'} := m_{w_ν}(P^{(ν-1)}_{ε'|ε_ν=0}, P^{(ν-1)}_{ε'|ε_ν=1}) with w_ν := 1 - σ_5(t_ν) (ε' ranges over the remaining
  directions); **G^off(U)(z) := P^{(d)}**; Π^off(U) := the composite gauge transform of U by G^off(U); Z^off(V) :=
  Π^off(R^{ax}_0∘…∘R^{ax}_{k-1}(V)). 𝔪^geo := the same with ψ ≡ 1 (iterated geodesic interpolation, defined on clustered data).
- **Clustered.** U is r-clustered at z if d(g_X(U)(z), g_Y(U)(z)) ≤ r for all corners X, Y of z's cell.

### 21.1 Step 1 statements (RS6-3, RS6-6)
- **Remark PL (periodic lift, T = 3, 4).** For T ∈ {3, 4}, P_♯^{(T)} := descend∘Π_E^{(2T)}∘lift is a projection onto S_E-type
  representatives, and lane A's LRL (b) holds with C_b(T) ≤ e^{20m}C_b(2T). Hence Corollary LRL(b)-E holds for all T ≥ 3.
  *Planned: PROVEN-HERE (routine).*
- **Lemma N1G ((N1-G) with C_G = ¼).** Σ_y|∇_μG_M(y)| = M/4 for M even, < M/4 for M odd (4D lattice torus of side M,
  mean-zero Green function of -Δ). *Planned: IMPORTED-AND-REVERIFIED (REVIEW_BFT_B_S6 D.4: reflection lemma for the cycle heat
  kernel + the 1D Green function); reproduced in checks/bb7g.* **[RBB7-fix RS7-3: (proof replaced: REVIEW_BFT_B_S7 B.2)]** Consequence: C_B ≤ 15 in (N1-bd); NF-ex, KΠ and CovLift-KΠ no
  longer carry a named import.

### 21.2 Step 2 statements
- **Lemma S2K (composite kernels).** Λ_2, Λ_2' < ∞ for DD8 (φ ∈ C^{2,β}, β ≥ 0.473), uniformly in t. *Planned: PROVEN-HERE*
  (CL-lin (d)'s exact representation of S^{(t)} by averaged products of ψ and φ).
- **Lemma N2-step (one refinement step, in the axial frame).** If D_axf_{j+1} ≤ c_0(N) then a_{j+1} ≤ 1.02D_axρ_{j+1}f_{j+1}, and for
  every level-j plaquette p with first corner in the block of X: F_j(p) = Σ_Pw_{pP}Ad_{T_X(P)}F_{j+1}(P) + e_j(p), with w = the
  matrix of S_2 (one step), T_X(P) the transport from P's first corner to X along a(·→X), and |e_j(p)| ≤ C_eρ_{j+1}²f_{j+1}²,
  C_e = C_e(L, φ, N, d). *Planned: PROVEN-HERE.*
- **Theorem N2 ((N2-0) per level, k-uniform).** (N2-0)_j holds for every j with C_N := 2Λ_2. Moreover (N2-lip): for level-j
  plaquettes p, p' with |p - p'| ≤ 2ρ_{j+1} (coarse), |F_j(p) - Ad_{T}F_j(p')| ≤ C_Lρ_{j+1}(1 + (k - j)f_k)f_k (T the axial transport
  between them). *Planned: PROVEN-HERE* (Lemma N2-step, Lemma S2K, telescoping with thin-loop holonomies).
- **Corollary N2-cons.** On 𝒦(ε_1) (in particular on 𝒞_glob), the box normal forms of the R^{ax}-chain exist on every Ñ_X
  (NF-ex) and Theorem CovLift-KΠ (i)-(iii) holds on 𝒞_glob without the hypothesis (N2-0). *Planned: PROVEN as an implication.*
- **Lemma Γ0.** For lane A's linearised S4' root map Q and the straight-leg map Q_ax: Q - Q_ax = Γ∘d with Γ local (range one
  coarse link), and Γ(H) = 0 for every constant 2-form H. *Planned: PROVEN-HERE given the transverse-reflection symmetry (L1)
  of the S4' family (cited: HIST l.396, RLARGE L1).*
- **Proposition Cg-lin.** For the linear lift (R-chain, then Π_E), (C_g-θ) holds for every 0 ≤ θ ≤ 1 with C_g^lin =
  2L^θκ_+C(φ, d), k-uniformly. *Planned: PROVEN-HERE.*
- **Proposition Cg-NL.** For Z^{KΠ} on 𝒞_glob(ε) (and for Z^off on frame representatives, §21.3), (C_g-θ) holds for 0 < θ < 1
  with C_g = C(L, φ, N, d, θ). *Planned: PROVEN as an implication of Theorem N2 (N2-lip), Lemma Γ0 and the BCH form of lane A's
  nonlinear residual (root-covariant W_0∘M̄ with the S4' family).*
- **Design decision (C_g).** Keep lane A's Q; no Q_ax change in the functional (option (a)), no Q-consistent R∘(QR)^{-1}
  (option (b)) and no θ = 0 residual slot (option (c)). Justification: Lemma Γ0 (the S4' symmetry kills the first-order residual).

### 21.3 Step 3 statements ((KΠ-off))
- **Lemma CUT.** Each m_w is continuous on SU(N) × SU(N), bi-equivariant (m_w(cag, cbg) = c·m_w(a, b)·g for constants c, g),
  equal to the geodesic interpolation a·exp(w log(a^{-1}b)) (real-analytic) when d(a, b) ≤ r_1. G^off(U) is defined for every U
  whose box normal forms exist; G^off(U)(c_Y) = 1 at every level-k root; it is face-consistent (a site on a common face of two cells
  gets the same value from both); on r-clustered data with r ≤ r_1/2 it equals 𝔪^geo. *Planned: PROVEN-HERE.*
- **Theorem KΠ-off.** On 𝒦(ε) (ε ≤ ε_1): (a) G^off is root-normalised, continuous in U (real-analytic on the clustered set),
  local (range 4), translation covariant; (b) **root-value formula for every level-0 gauge k (no smallness):**
  Π^off(U^k) = Π^off(U)^{ĥ}, ĥ(z) := G^off-type gluing of {k(c_X)g_X(U)(z)} times G^off(U)(z)^{-1}; ĥ depends on k only through its
  root values, ĥ(c_Y) = k(c_Y), ĥ(c, ·) = c; (c) idempotence Π^off∘Π^off = Π^off; (d) on the clustered set it has Proposition KΠ's
  smooth extension (with 𝔪^geo for M) and linearises to Π_E at U = 1. Hence **(CovLift) (i)-(iii) hold for Z^off on 𝒦(ε) for every
  level-k gauge**, and (iv), (v) reduce to frame representatives (V^h clustered on Ω), where Z^off = 𝔪^geo-glued KΠ.
  *Planned: PROVEN-HERE for (a)-(c); (d) PROVEN as in Proposition KΠ with 𝔪^geo in place of M.*
- **Proposition TOP (where the topology sits).** (a) There is no continuous map μ: SU(N) × [0, 1] → SU(N) that is
  conjugation-equivariant with μ(c, 0) = c, μ(c, 1) = 1; hence no continuous bi-equivariant two-point mean with weights varying
  continuously over [0, 1] on all of SU(N)², and no covariant gluing that is continuous in a continuum cell variable on spread data.
  (b) Z^off evades (a) only because lattice weights are discrete: on spread representatives it has O(1) jumps next to roots. (c)
  These occur only where V is not small in the given gauge, where (CovLift) asks for no bound. (d) Fields in 𝒦(ε) with nonzero
  lattice topological charge are not in the gauge saturation of any 𝒞_glob(ε'), so (KΠ-off) is needed beyond large gauges.
  *Planned: (a)-(c) PROVEN-HERE; (d) cited (Lüscher 1982, from memory, not opened).*
- **Remark HOL.** (CovLift) (v) on spread representatives: ψ is not analytic, so Z^off is not holomorphic there; what GI-cov
  consumes (gauge-invariant local functionals, evaluated in frames) is holomorphic. *Planned: ARGUED.*

### 21.4 Failure modes (pre-stated)
- **N2-F1** the curvature recursion is not k-uniform (f_j/f_k grows with k - j). Expected: does NOT occur.
- **Cg-F1** with lane A's Q the weighted residual grows like L^{θ(k-l)}. Expected: does NOT occur (Γ0); OCCURS for an asymmetric
  root map (control).
- **KO-F1** G^off is discontinuous in U or not face-consistent. Expected: NOT. **KO-F2** the root-value formula or idempotence
  fails on spread data. Expected: NOT. **KO-F3** a topological obstruction to (CovLift) (i)-(iii) off 𝒞_glob. Expected: does NOT
  occur on the lattice; an obstruction to continuum smoothness on spread data OCCURS (Proposition TOP), harmless.

### 21.5 Checks (criteria files written after this section and before the scripts)
- **bb7g** (RS6-6): exact FFT on 4D tori, M ∈ {8, 12, 16, 24, 32, 48}: Σ|∇_1G_M| against M/4; cycle heat kernel unimodality;
  monotonicity of G_M in |y_1|; the 1D Green function formula.
- **bb7n** (d = 2, SU(2), L = 3, DD8): the nonabelian R^{ax}-chain from a random small top field, depths 1-3: f_j/f_k against depth
  (N2-F1), exact covariance of the curvature profile under a Haar-random level-k gauge; control: global-log refinement.
- **bb7c** (d = 2, abelian, DD8, depths 1-5): weighted residual L^{θ(k-l)}ρ_{l+1}^{-2}|r_l| of the S_1-chain for a symmetric
  S4'-type root map (bounded) and an asymmetric one (control: grows).
- **bb7k** (d = 2, SU(2)): G^off on spread data (Haar-random root gauges): root values, G_0-invariance, constant covariance,
  idempotence, root-value covariance, continuity along a gauge path, agreement with 𝔪^geo on clustered data; control: Karcher
  gluing on spread data depends on the start.

## 22. Proofs (session 7; appended after §21 (10:21:15 UTC), after Step 1 (10:22-10:23:36) and after bb7g, bb7c, bb7n, bb7k ran (10:34:18-10:35:23))

Post-proof corrections of pre-stated details are marked **[post-proof correction]**; §21 is not edited. They are: (1) Remark PL's
constant is e^{16m + 4m'} ≤ e^{20m'} (input weight m, output weight m') **[RBB7-fix RS7-2: withdrawn. LRL (b) uses the weight m on both sides (BFT_A l.1347-1349; m' is the kernel-decay exponent, not an output weight), so the pre-stated C_b(T) ≤ e^{(4T+4)m}C_b(2T) ≤ e^{20m}C_b(2T) stands (REVIEW_BFT_B_S7 B.1)]**; (2) (N2-lip) holds in the stronger form
C_Lρ_{j+1}(1 + f_k)f_k (no factor k - j); (3) Lemma CL-clu (new, stated and proven in 22.12) is needed: the R^{ax}-chain of a field
that is small in one level-k gauge is **not** small in one level-0 gauge (its face links carry the coarse links), so 19.13's
domain argument ("U = e^A small in one level-0 gauge") does not literally cover U = chain(V); CL-clu supplies the clustering of the
corner normal forms directly (this repairs 19.13's domain clause as applied in 19.16); (4) Proposition Cg-NL's BCH remainder is
ARGUED, not proven (lane A's nonlinear root map was not re-read this session); (5) the bb7k control K10 did not behave as
predicted (see 23).

### 22.1 Remark PL (periodic lift, T = 3, 4): PROVEN-HERE (routine) **[post-proof correction (1)]**
T ∈ {3, 4}, T' := 2T ∈ {6, 8} (≥ 5). lift: periodic extension of all-level configurations and data from 𝕋_T to 𝕋_{T'}; descend:
restriction to one fundamental domain; descend∘lift = 1, and lift∘descend = 1 on T-periodic configurations. (a) Every translation-
invariant local operator Op defined by one formula on both tori satisfies Op_{T'}∘lift = lift∘Op_T (periodisation). Hence a
critical point x of E_src on 𝕋_T lifts to a critical point of the lifted problem (same Euler-Lagrange formula), and Π_E^{(T')}
commutes with the coarse translations by Te_μ (EP-alg), so Π_E^{(T')}(lift x) is T-periodic. (b) P_♯ := descend∘Π_E^{(T')}∘lift
satisfies P_♯∘P_♯ = descend∘Π_E∘(lift∘descend)∘Π_E∘lift = descend∘Π_E∘Π_E∘lift = P_♯, and P_♯x - x is the descent of the periodic
composite gauge direction DΛ(lift x) (EP-alg's λ_0 = Λ is translation covariant), trivial at level k: P_♯ is an S_E-type gauge
projection on 𝕋_T. (c) Weights (w(z) = e^{m d(z, X_0)}, ℓ¹ coarse distance; X̃_0 a preimage of X_0): on 𝕋_{T'} each coordinate
distance exceeds the 𝕋_T one by at most T, so ||lift B||_{D,m} ≤ e^{4Tm}||B||_{D,m} ≤ e^{16m}||B||_{D,m}. On the output side, each
z ∈ 𝕋_T has a preimage z̃ with d_{T'}(z̃, X̃_0) = d_T(z, X_0) (minimal representatives); the difference and Campanato terms read
points within ℓ¹ distance 4 of z̃, costing at most e^{4m'} **[RBB7-fix RS7-2: read e^{4m}: the output weight is m]**. So LRL (b) on 𝕋_{T'} (Corollary LRL(b)-E, T' ≥ 5) gives LRL (b) on 𝕋_T
with C_b(T) ≤ e^{16m + 4m'}C_b(2T) ≤ e^{20m'}C_b(2T) **[RBB7-fix RS7-2: read C_b(T) ≤ e^{(4T+4)m}C_b(2T) ≤ e^{20m}C_b(2T), the pre-stated constant. Extension (REVIEW_BFT_B_S7 B.1, ARGUED-routine): the q-fold lift T' := qT ≥ 5 (q = 5 for T = 1, q = 3 for T = 2) gives LRL (b) for T = 1, 2 with cost e^{2qTm + 4m}]**. ∎ **Lane A's LRL (b) holds for all T ≥ 3** (with P_♯ = Π_E for T ≥ 5 and the lifted
P_♯ for T = 3, 4).

### 22.2 Lemma N1G: IMPORTED-AND-REVERIFIED (REVIEW_BFT_B_S6 D.4); reproduced in bb7g
Re-verified step by step. (1) -Δ on the 4D torus is the sum of four commuting 1D cycle Laplacians, so the continuous-time kernel
factorises, p_t(y) = Π_iq_t(y_i), and G_M = ∫_0^∞(p_t - M^{-4})dt (absolutely convergent for ∇G: the gap of -Δ is 2 - 2cos(2π/M)).
(2) *Reflection lemma.* For 0 ≤ x < M/2 - ½, reflect Z_M in the midpoint of the bond (x, x + 1) (y ↦ 2x + 1 - y; no fixed sites for
M even; it also fixes the antipodal bond midpoint). 0 and x + 1 lie on opposite arcs; a path from 0 to x + 1 enters x + 1's arc at a
first time; reflecting the path after that time is an injective, rate-preserving map onto paths from 0 to x. So q_t(x + 1) ≤ q_t(x).
**[RBB7-fix RS7-3 (binding): the path reflection above is not valid as written: reflecting after the first entry time deletes the
crossing jump (r(ω(τ)) = ω(τ-)), so the map is neither rate-preserving nor onto a path space of the same dimension. Replacement
(REVIEW_BFT_B_S7 B.2, PROVEN): for M even put u_t(x) := q_t(x) - q_t(x + 1), 0 ≤ x ≤ M/2 - 1. It obeys du/dt = u(x - 1) + u(x + 1) -
2u(x) with the antisymmetric ghost values u(-1) = -u(0), u(M/2) = -u(M/2 - 1) (symmetry of q_t), i.e. u' = Au with A Metzler
(non-negative off-diagonal entries), so e^{tA} ≥ 0 entrywise and u_0 = δ_{x,0} ≥ 0 gives u_t ≥ 0: q_t is non-increasing on
[0, M/2]. For M odd use x ≤ (M - 3)/2 with ghost u((M - 1)/2) = 0. Steps (3)-(5) are unchanged; Lemma N1G is PROVEN-HERE with
C_G = ¼ (no path argument needed).]**
(For M odd the same holds on [0, (M - 1)/2].) (3) Hence p_t(·, y') - M^{-4} and G_M(·, y') are symmetric and non-increasing in |y_1|,
and the total variation over the cycle gives Σ_{y_1}|∂_1G_M(y_1, y')| = 2(G_M(0, y') - G_M(M/2, y')). (4) g(y_1) := Σ_{y'}G_M(y_1, y')
solves the 1D problem -Δg = δ_0 - 1/M with mean zero; g(y) = -|y|/2 + y²/(2M) + c: at y ≠ 0, ±M/2 the linear part is harmonic and
-Δ(y²/2M) = -1/M; at 0, -Δg = 1 - 1/M; at M/2 (both neighbours at |y| = M/2 - 1), -Δg = -1/M (checked). So g(0) - g(M/2) = M/8.
(5) Σ_y|∇_1G_M| = 2(g(0) - g(M/2)) = M/4. For M odd: 2(g(0) - g((M - 1)/2)) = (M² - 1)/(4M) < M/4. ∎ **bb7g: ALL PASS** —
Σ|∇_1G_M| = 2, 3, 4, 6, 8, 12 for M = 8, 12, 16, 24, 32, 48 (deviation ≤ 3.6e-14); M = 9, 15: (M² - 1)/(4M) to 1.8e-15; cycle kernel
unimodal (worst 1.5e-15 relative); monotonicity in |y_1| (4.5e-17); transverse-sum formula (7.1e-15); max|y|³|∇G| = 0.1735
(flat in M). The values reproduce REVIEW_BFT_B_S6 D.4's. Consequence: (N1-bd) with C_B ≤ 15; Lemma REF, Theorem NF-ex, Proposition KΠ
carry no named import (KΠ: the Karcher facts remain cited).

### 22.3 Lemma S2K: PROVEN-HERE
By CL-lin (d), (s^{[1]})^t c at a fine link [z, z + ρ] equals ∫_z^{z+ρ}Σ_ic_iψ(u - i)du for every sequence c (ψ := Σ_{i≥1}φ'(· - i),
compactly supported, C^{1,β} since φ ∈ C^{2,β}), and s^tc(z) = Σ_ic_iφ(z - i). The μν-component of S_2^{(t)} is the tensor product
(s^{[1]})^t ⊗ (s^{[1]})^t ⊗ s^t ⊗ s^t, so in coarse 2-form units (S_2^{(t)}H)_{μν}(z) = Σ_iH_{μν}(i)·avg_{[z_μ, z_μ+ρ]}ψ(· - i_μ)·
avg_{[z_ν, z_ν+ρ]}ψ(· - i_ν)·Π_{κ≠μ,ν}φ(z_κ - i_κ) (z in units of the source spacing, ρ = L^{-t}). Averaging does not increase
sup_xΣ_i|·|, so **Λ_2 ≤ (sup_xΣ_i|ψ(x - i)|)²(sup_xΣ_i|φ(x - i)|)^{d-2} < ∞, uniformly in t**; the kernel is Lipschitz in z with
constant ≤ Λ_2' := 2(sup Σ|ψ'|)(sup Σ|ψ|)(sup Σ|φ|)^{d-2} + (d - 2)(sup Σ|ψ|)²(sup Σ|φ'|)(sup Σ|φ|)^{d-3}, per unit of source spacing. ∎

### 22.4 Lemma N2-step: PROVEN-HERE
Fix X (level j + 1) and work in the X-axial gauge g^X on the stencil (the union of the S_1/μ stencils of X and of its neighbours), extended
block-constantly to level j; this changes no holonomy based in X's block, since g^X(X) = 1.
(0) *Stencil size.* An axial-gauge link value is the holonomy of the loop a(i→X)·(i, i + e_ν)·a(i + e_ν→X)^{-1}, spanned by an axial
ladder of ≤ D_ax level-(j+1) plaquettes, so (lasso, HIST §20.0 F4 and F1, valid when the total is ≤ ½) own|A^X| ≤ 1.011D_axρ_{j+1}²f_{j+1},
i.e. a_{j+1} ≤ 1.02D_axρ_{j+1}f_{j+1}. In this gauge Z^X(X, X + e_ν) = 1 for every positive neighbour, and every coarse link among the
≤ 2^d blocks meeting a cell of X has own size ≤ 1.011·2D_axρ_{j+1}²f_{j+1}.
(1) *Links with tail in X* carry exp(s^X(b)), s^X = S_1A^X + dμ(A^X) (μ(A^X) = 0 on X's sites). *Links with tail in a neighbour X'*
carry, in this gauge, exp(Ad_{g^X(X')}s^{X'}(b)); and Ad_{g^X(X')}A^{X'} = (A^X)^H with H_i := g^X(X')g^{X'}(i)g^X(i)^{-1}, the holonomy
of a loop of ≤ D_ax plaquettes, own |log H| ≤ 1.011D_axρ_{j+1}²f_{j+1}. Writing (A^X)^H = A^X + dη + O(|η|·own|A^X|) with η fixed by the
vanishing of (A^X)^H on the X'-tree (η = ψ^X_{X'} + const, ψ^X_{X'}(i) := ∫_{a(i→X')}A^X), the X'-interior value S_1(A^X + dη) =
S_1A^X + dS_0ψ^X_{X'} = R(A^X) there (μ(A^X) = S_0ψ^X_{X'} on X'), and the face values s^X(b) are R(A^X)(b) by construction. So, up to
O(own|η|·own|A^X|), the level-j field near X is exp of the **linear** R(A^X) (in the X gauge, link by link).
(2) *Curvature.* For a level-j plaquette p near X: log hol(∂p) = (dRA^X)(p) + E_1, |E_1| ≤ C(own|s|)² + C·own|η|·own|A^X| (BCH, four links
of own size ≤ σ := C_sown|A^X|, C_s := Λ_1^{(1)} + Λ_0^{(1)}D_ax), and dRA^X = dS_1A^X = S_2dA^X (R - S_1 = dμ). For a level-(j+1)
plaquette P: dA^X(P) = (log hol of the X-gauge field around P) - E_2(P), |E_2| ≤ C(own|A^X|)², and that log hol equals
Ad_{g^X(i_P)}log hol(∂P) based at P's first corner i_P (gauge covariance of the holonomy). In coarse units (2-forms ×ρ^{-2}):
F_j(p) = Σ_Pw_{pP}Ad_{T_X(P)}F_{j+1}(P) + e_j(p), T_X(P) := g^X(i_P) (the axial transport from i_P to X), with
|e_j| ≤ ρ_j^{-2}(|E_1| + Λ_2^{(1)}|E_2|) ≤ C_eρ_{j+1}²f_{j+1}², C_e = C(N)·L²·(C_s² + D_ax + Λ_2^{(1)})·D_ax² (own|A^X| ≤ 1.011D_axρ_{j+1}²f_{j+1},
ρ_j = ρ_{j+1}/L). The smallness used (principal logs, BCH on a ball, lasso) is D_axf_{j+1} ≤ c_0(N). ∎

### 22.5 Theorem N2 ((N2-0) per level, k-uniform): PROVEN-HERE **[post-proof correction (2): (N2-lip) without the factor k - j]**
*Telescoping.* Fix a level j_0 and a level-j_0 plaquette q. For j ≥ j_0 let Φ_j := Σ_{p∈level j}W^{(j-j_0)}(q, p)Ad_{τ(q,p)}F_j(p), where
τ(q, p) is the transport along a reference path: from q's corner to x_j(q) (the level-j site of q's level-j block, through the
nested block sites x_{j_0+1}(q), …) and then the level-j axial path from x_j(q) to p's corner. Φ_{j_0} = F_{j_0}(q), and
|Φ_k| ≤ Λ_2f_k (Lemma S2K; Ad is an isometry). By Lemma N2-step at the step j + 1 → j and W^{(j+1-j_0)}(q, P) = Σ_pW^{(j-j_0)}(q, p)w_{pP}:
  Φ_j - Φ_{j+1} = Σ_pW^{(j-j_0)}(q, p)Ad_{τ(q,p)}e_j(p) + Σ_{p,P}W^{(j-j_0)}(q, p)w_{pP}[Ad_{τ(q,p)T(p,P)} - Ad_{τ(q,P)}]F_{j+1}(P),
with T(p, P) the transport of Lemma N2-step followed by the level-j path from c_X to p's corner. The bracket is controlled by the
holonomy of the loop x_j(q) → p → (via X) P → x_{j+1}(q) → x_j(q) (the common prefix q → x_j(q) cancels). All its points lie within
coarse distance C_rρ_{j+1} of q (supp W^{(j-j_0)}(q, ·) has radius ≤ r_sρ_jL/(L - 1); P is within (r_s + 2)ρ_{j+1} of p). Its
level-(j+1) segments are replaced by level-j root rows: the root-row product of R^{ax}(Z) equals the coarse link up to own
O(σ²) per link (the linear row sum of R vanishes, Q_axR = 1). The resulting level-j loop is spanned by ≤ C_A(L, d, r_s)
level-j plaquettes, so |log hol| ≤ 1.011C_Aρ_j²f_j + O(σ²) =: c_hρ_{j+1}²max(f_j, f_{j+1}). With ||Ad_g - Ad_{g'}|| ≤ 2|log g^{-1}g'|:
  |Φ_j - Φ_{j+1}| ≤ Λ_2[C_eρ_{j+1}²f_{j+1}² + 2c_hΛ_2^{(1)}ρ_{j+1}²max(f_j, f_{j+1})f_{j+1}].
*Induction downward in j_0.* Suppose f_j ≤ 2Λ_2f_k for all j > j_0 (true for j_0 = k - 1). A priori (one step, Lemma N2-step):
f_{j_0} ≤ Λ_2^{(1)}f_{j_0+1} + C_eρ²f_{j_0+1}² ≤ 3Λ_2^{(1)}Λ_2f_k, which makes the lasso totals small when ε_1 is small. Summing the
telescope (Σ_{j≥j_0}ρ_{j+1}² ≤ L²/(L² - 1)):
  f_{j_0} ≤ Λ_2f_k + Λ_2(L²/(L² - 1))[C_e(2Λ_2f_k)² + 2c_hΛ_2^{(1)}·3Λ_2^{(1)}Λ_2f_k·2Λ_2f_k] ≤ 2Λ_2f_k
as soon as f_k ≤ ε_1 := [Λ_2(L²/(L² - 1))(4C_eΛ_2 + 12c_h(Λ_2^{(1)})²Λ_2)]^{-1}·min(1, …) together with 2Λ_2D_axε_1 ≤ c_0 (Lemma N2-step's
smallness) and the lasso and BCH ball conditions. **This is (N2-0)_j (a) with C_N = 2Λ_2, for every j, with ε_1 = ε_1(L, φ, N, d)
independent of k, T, j and of any global gauge** (only f_k entered). (b) is Lemma N2-step (0): a_{j+1} ≤ 1.02D_axC_Nρ_{j+1}f_k =: C_axρ_{j+1}f_k.
(c) On Ñ_X (side 4n + 1) the complete axial gauge (root c_X, fixed order) gives each link the holonomy of a ladder of ≤ (d - 1)·4n
level-0 plaquettes of own size ≤ f_0/n²: n|A| ≤ 1.011·12f_0 ≤ 12.2f_0 (d = 4); and n²|dA(p)| ≤ n²|log U(∂p)| + C(n|A|)², while
n²|log e^{tA}(∂p)| ≤ tn²|dA(p)| + C(tn|A|)², so max_tε_f(e^{tA}, X) ≤ f_0 + C_boxf_0². ∎
*(N2-lip).* For p, p' at level j with |p - p'| ≤ 2ρ_{j+1}, compare the telescopes of p and p' (reference paths run parallel; the loop
between them has coarse length O(1) and width O(ρ_{j+1}), holonomy ≤ Cρ_{j+1}f_k): the top terms differ by ≤ Λ_2'·2ρ_{j+1}f_k + 2Λ_2Cρ_{j+1}f_k²
(Lipschitz kernel, Lemma S2K; ρ_k = 1); a level-j' error term contributes ≤ min(2Λ_2, Λ_2'·2ρ_{j+1}/ρ_{j'})·C_eρ_{j'+1}²(C_Nf_k)², whose
sum over j' ≥ j is ≤ Cρ_{j+1}f_k²; the frame-change terms likewise. So **|F_j(p) - Ad_TF_j(p')| ≤ C_Lρ_{j+1}(1 + f_k)f_k**. ∎
**N2-F1 does not occur.** **bb7n (d = 2, SU(2), DD8, depths 1-3): ALL PASS** — linear structure L0 exact (0, 2.5e-16); depth uniformity
R_1, R_2, R_3 = 1.2769, 1.3100, 1.3252 (increments shrinking ×0.46; the linear chain gives 1.2771, 1.3102, 1.3278); deviation from the
linear chain 0.0026·f_k; exact covariance of the curvature profile under a Haar-random level-k gauge 3.4e-16; the frame-free control
(global log of V^h) is off by 876·f_k. The axial stencil ratio own|A^X|/(ρ²f) rises 1.48 → 2.87 → 4.90 towards the 2D ladder bound
1.011·D_ax = 5.06 (D_ax = 5 for this stencil) as the field becomes smooth on the stencil. [Disclosed: the amplitude rescaling used
the unscaled field's plaquettes, so the runs have f_k = 0.26 and 0.52, not the 0.10 and 0.20 named in bb7n_criteria.md; the
criteria's thresholds are relative to f_k.]

### 22.6 Corollary N2-cons: PROVEN as an implication
For V ∈ 𝒦(ε_1) with C_box(C_Nε_1 + C_N²ε_1²) ≤ ε_0 and 12.2C_Nε_1 ≤ ε_0: Theorem N2 (c) gives NF-ex's hypotheses on every Ñ_X, so the box
normal forms of chain(V) exist (unique, Lemma NF-uniq), with no global gauge. 𝒞_glob(ε) ⊂ 𝒦(4ε + Cε²), so (N2-0) holds on 𝒞_glob(ε)
for small ε, and Theorem CovLift-KΠ (i)-(iii) holds on 𝒞_glob (small gauges, RS6-4) without the hypothesis (N2-0) and without (N1-G);
its Karcher domain for U = chain(V) is supplied by Lemma CL-clu (22.12) **[post-proof correction (3)]**. ∎

### 22.7 Lemma Γ0: PROVEN-HERE given the S4' reflection property (cited)
Q and Q_ax are root-covariant, so Q - Q_ax kills exact forms (16.13 (e)). For a coarse link c along μ, each S4' contour γ_{σ,y} of c and
the straight leg S_c share endpoints, and γ_{σ,y} - S_c bounds a ribbon of ≤ 2L(L - 1) level-j plaquettes in c's two endpoint blocks
(16.13 (e); HIST l.1036-1044). So (Q - Q_ax)B(c) = avg_{σ,y}Σ_{p∈ribbon}±dB(p) =: Γ(dB)(c), Γ local. For a constant 2-form H,
Γ(H)(c) = avg_{σ,y}Σ_{κ<λ}H_{κλ}A_{κλ}(γ_{σ,y} - S_c), A the signed projected areas. Every pair κ < λ contains an index ν ≠ μ; the
reflection x_ν ↦ 2(c_X)_ν - x_ν maps B(X), c and the S4' family of c to itself, pairing (σ, y) with (σ, y') (HIST l.396: property L1,
RLARGE) **[RBB7-fix RS7-8 (C.4): L1 is used for each transverse direction ν ≠ μ separately; lane A's linearised Q is the uniform S4' average avg_{σ,y} (BFT_A l.1112), so the uniform-weight assumption holds; bb7c's Q_sym is a model of the mechanism, not lane A's family]**, and reverses the orientation of every plane containing ν; so the average of A_{κλ} vanishes and Γ(H) = 0. ∎ (bb7c C1: the
symmetric S4'-type model gives 0.0 exactly on constant curvature; the asymmetric control gives 1.500.)

### 22.8 Proposition Cg-lin: PROVEN-HERE
Linear lift from level-k data b (V = e^b): the R-chain and the S_1-chain have the same residuals (R - S_1 = dμ with μ = 0 at the roots,
and Q is root-covariant), Π_E does not change residuals (composite-gauge invariance, REVIEW_BFT_B_S6 B.1), and Q_axS_1 = 1, so
r_l = (Q - Q_ax)S_1B_l = Γ(S_2^{(k-l)}db) (B_l the level-l field). Γ kills constants (Lemma Γ0), so
|r_l|_own ≤ 2L(L - 1)·max_{p,p'}|H(p) - H(p')|_own over Γ's stencil (diameter ≤ 2ρ_{l+1}), H := S_2^{(k-l)}db; by Lemma S2K the coarse
oscillation is ≤ 2Λ_2'ρ_{l+1}||db||_∞ ≤ 8Λ_2'ρ_{l+1}||b||_∞. Hence κ_lL^{θ(k-l)}ρ_{l+1}^{-2}|r_l|_own ≤ κ_+L^θρ_{l+1}^{-θ}·2L(L - 1)L^{-2}·8Λ_2'ρ_{l+1}||b||
≤ 16κ_+L^θΛ_2'ρ_{l+1}^{1-θ}||b||_∞ ≤ **C_g^lin||b||_∞, C_g^lin := 16κ_+L^θΛ_2', for every 0 ≤ θ ≤ 1, uniformly in k and l**. ∎
(The θ = 0 bound of 16.13 (e), 2||f_l||, did not use the symmetry; the gain ρ_{l+1}^{1-θ} is the symmetry.) **Cg-F1 does not occur.**
bb7c (d = 2 model, depth 5): symmetric map, θ = ½: the weighted residual decays from 1.247 (top step) to 0.270 (finest), ratio 0.22;
θ = 1: bounded (2.16 → 4.21, increments shrinking ×0.5); θ = 0: decays ≈ ×L^{-1} per level; asymmetric control: θ = 0 flat (≈ 1.23,
the 16.13 (e) marginal bound), θ = ½ grows ×1.73 = L^{½} per level (1.63 → 19.27): **Cg-F1 OCCURS for the asymmetric control, as
predicted.**

### 22.9 Proposition Cg-NL: PROVEN as an implication for the first-order term; the BCH remainder ARGUED **[post-proof correction (4)]**
Let V ∈ 𝒦(ε_1), V = e^b on Ω in some level-k gauge, ||b|| ≤ ε; by gauge covariance of the residuals (r_l(Z^g) = Ad r_l(Z) for composite
gauges, the root map being W_0∘M̄ with root-covariant S4' averages) compute in X-axial gauges. There the level-l field near c's blocks
is exp of the linear R(A^X) up to own O(ρ_{l+1}⁴f²) (22.4 (1)), so r_l(Z) = Γ(F_l in that gauge) + R_BCH, where the first term is the
linear residual of the frame field. Its size: by (N2-lip) (localised to Ω^{(-r)}: the telescope only reads V on Ω), the
oscillation of F_l over Γ's stencil is ≤ C_Lρ_{l+1}(1 + 4ε)4ε, so as in 22.8 the first-order term is ≤ 2(L - 1)L^{-1}C_Lρ_{l+1}(1 + 4ε)4ε in
the ρ_{l+1}^{-2}-weighted own units, and κ_lL^{θ(k-l)}× it is ≤ 8κ_+L^θC_Lρ_{l+1}^{1-θ}ε. R_BCH: the S4' transporters along ≤ 4L level-l
links of own size ≤ σ = O(ρ_{l+1}²ε) differ from exp of the line sums by own O(L²σ²) = O(ρ_{l+1}⁴ε²), and W_0 and the averaging are
analytic near 1 with BCH-quadratic corrections of the same order; weighted, κL^{θ(k-l)}ρ_{l+1}^{-2}O(ρ_{l+1}⁴ε²) = O(ρ_{l+1}^{2-θ}ε²) **[ARGUED: lane
A's nonlinear residual definition (BFT_A) was not re-read this session]**. So **(C_g-θ) holds for Z^{KΠ} on 𝒞_glob and for Z^off on
frame representatives for every 0 < θ < 1 (indeed θ ≤ 1), with C_g = 8κ_+L^θC_L + O(ε)**, given the ARGUED remainder. ∎

### 22.10 The C_g design decision: justified
Options (a) Q_ax in the functional (a lane-A change of BL-2 constants), (b) R∘(QR)^{-1} (exponential locality, an unverified
inverse) and (c) θ = 0 on the residual slot (a lane-A weighting change) are **not needed**: lane A's S4' root map already kills the
first-order residual (Lemma Γ0), so lane B's lift with lane A's Q satisfies (C_g-θ) for 0 < θ ≤ 1 linearly (Cg-lin, PROVEN) and
nonlinearly up to the ARGUED BCH remainder (Cg-NL). The clause is therefore written with lane A's own weights ω^R_l = L^{θ(k-l)}, and
no lane-A file needs to change. What this does not cover: the non-residual components of g_Z (status of RS5-5, θ = 0 analysis).

### 22.11 Lemma CUT: PROVEN-HERE
*Continuity.* On {d(a, b) < r_inj} the map (a, b) ↦ ψ(d(a, b))log(a^{-1}b) is continuous (log analytic there) **[RBB7-fix RS7-4 (binding; annotates §21.0's cut-off definition, §21 not edited): for N ≥ 3 the eigenvalue-principal log can leave su(N) inside the injectivity ball (angles (1.1π, -0.55π, -0.55π) in HS-angle normalisation, |X|² = 1.815π² < 2π² = r_inj², map to trace -2πi). "log" in m_w is therefore the inverse of exp on the ball B(0, r_inj) ⊂ su(N) (analytic there, conjugation-equivariant); equivalently one may require r_2 < π (HS-angle normalisation), where |θ_i| ≤ |X| < π makes the principal log traceless and equal to it. bb7k's SU(2) normalisation (d(1, -1) = π = r_inj) is unaffected]**; on {d(a, b) > r_2} it is 0;
the two open sets cover SU(N)² (r_2 < r_inj) and the definitions agree on the overlap. So m_w is continuous for each w ∈ (0, 1);
m_0, m_1 are projections. *Bi-equivariance.* (cag)^{-1}(cbg) = g^{-1}(a^{-1}b)g, d is bi-invariant and the principal log is
conjugation-equivariant, so m_w(cag, cbg) = cag·g^{-1}exp(wψ log(a^{-1}b))g = c·m_w(a, b)·g. *Root values.* At c_Y (lower corner Y,
t = 0) every w_ν = 0, so G^off(U)(c_Y) = g_Y(U)(c_Y) = 1. *Face consistency.* A site with t_ν = 0 in cell C has t_ν = 1 in C - e_ν; in
C - e_ν the interpolations along the axes before ν use the same corners and weights as C's ε_ν = 0 corners, the axis-ν step returns the
ε_ν = 1 branch (w = 1), and the later axes again coincide. *Clustered data.* If all corner points lie within r_1/2 of p_0 and
r_1/2 is below the convexity radius, every intermediate point stays in the convex ball B(p_0, r_1/2) (geodesic interpolation), so all
distances met are ≤ r_1, ψ = 1 throughout and G^off = 𝔪^geo. ∎ (bb7k K1 6.5e-19, K2 5.6e-17, K8 3.2e-18.)

### 22.12 Theorem KΠ-off: PROVEN-HERE ((a)-(c)); (d) PROVEN as in Proposition KΠ; with Lemma CL-clu
Let 𝔤[{p_X}] denote the iterated cut-off gluing of corner points (so G^off(U)(z) = 𝔤[{g_X(U)(z)}]).
(a) Defined on 𝒦(ε) (box normal forms exist, Corollary N2-cons), root-normalised (Lemma CUT); continuous in U (the normal forms are
real-analytic in U by NF-ex's IFT; m_w continuous), real-analytic where all corner data are r_1/2-clustered; range 4 (the corners of
z's cell and their boxes); translation covariant (one formula, fixed axis order; not rotation covariant, which (CovLift) does not ask). **[RBB7-fix RS7-6 (a): the boxes Ñ_X (coarse side 4 + 1/n) must embed, so Z^off is defined for coarse side T ≥ 5; "every torus" in (CovLift) is read as every torus with T ≥ 5 for Z^off (consumers use T ≥ 86). (b) The fixed axis order of 𝔪^geo and of R^{ax} breaks hypercubic covariance; (CovLift) asks only for translations, but the split of the polymer activities into a local part and a remainder is then not automatically hypercubic-symmetric, so the marginal-coupling extraction ((I-id)) symmetrises over the hypercubic group (or shows that no anisotropic Σc_{μν}tr F_{μν}² is generated). A note, not a new wall.]**
(b) For every level-0 gauge k: g_X(U^k) = k(c_X)g_X(U)k^{-1} (NF-cov, no smallness), so by right equivariance
G^off(U^k)(z) = 𝔤[{k(c_X)g_X(U)(z)}]·k(z)^{-1}, and with (U^a)^b = U^{ba}: Π^off(U^k) = U^{G^off(U^k)k} = Π^off(U)^{ĥ},
**ĥ = 𝔤[{k(c_X)g_X(U)}]·𝔤[{g_X(U)}]^{-1}**, which depends on k only through its root values; ĥ(c_Y) = k(c_Y) (root exactness);
k ≡ c gives ĥ = c (left equivariance by constants). (c) With k := G^off(U) (= 1 at the roots): G^off(Π^off(U)) = 𝔤[{g_X(U)}]G^off(U)^{-1} = 1.
(d) On clustered data G^off = 𝔪^geo: real-analytic, bi-equivariant, root-exact, so 19.13's root-value, idempotence and constant
arguments hold verbatim with 𝔪^geo for M; at U = 1, ĥ = 𝔪^geo[{k(c_X)}], the iterated geodesic interpolation of the root values with
σ_5 weights, C^{2,1} in coarse units across cell faces (σ_5', σ_5'' vanish at 0 and 1; each step is a smooth function of the previous
ones), with norms ≲ max d(k(c_X), k(c_Y)) over cells; linearisation: m_w(e^a, e^b) = e^{(1-w)a + wb} + O(2), so 𝔪^geo linearises to
Σ_Xχ^5_X(·) (σ_5(1 - t) = 1 - σ_5(t), product weights), and Π^off linearises to Π_E as in 19.13.
**Lemma CL-clu (new; PROVEN-HERE, constants not evaluated).** If V^h = e^b on Ω (level-k gauge h, ||b|| ≤ ε ≤ ε_1), the corner normal
forms of chain(V^h) at every site of Ω^{(-r)} are C_clε-clustered. **[RBB7-fix RS7-7 (binding): explicit hypotheses for CL-clu's use in Theorem KΠ-off (iv)-(v): C_clε ≤ r_1/2 and r_1/2 ≤ the convexity radius of SU(N); Ω contains the corner boxes Ñ_X of every cell meeting Ω^{(-r)}. C_cl contains the factor 16·25·4C_N (≈ 1600Λ_2), so ε is small; with Lemma GI-frame, C_F(Ω) depends on Ω's side, and ε is small relative to 1/C_F(Ω_□), consistent with BB-bond's boxes of fixed side.]** *Proof.* By Theorem N2 (c) and NF-ex, on Ñ_X the chain field is
U = (e^{A_X})^{k_X} with k_X the complete axial gauge of Ñ_X rooted at c_X, and g_X(U) = g_X(e^{A_X})k_X^{-1} with
|log g_X(e^{A_X})| ≤ 8(2C_Bε_* + 12.2f_0) on N_X (19.13's estimate, now for e^{A_X}). For corners X, Y of a cell, p_X(z)p_Y(z)^{-1} =
g_X(e^{A_X})(z)·k_X(z)^{-1}k_Y(z)·g_Y(e^{A_Y})(z)^{-1}; τ := k_Yk_X^{-1} maps e^{A_X} to e^{A_Y} on the overlap, so its neighbouring values
differ by ≤ own|A_X| + own|A_Y| ≤ 25f_0/n and it is within 16·25f_0 of the constant τ(c_X) = k_Y(c_X), the axial transport in U from c_X
to c_Y; that transport is the root-row product, which equals V^h(Y, X) = e^{-b(X,Y)} up to the BCH defect of the rows (22.5: own O(σ²)
per link, summed over the levels: O(ε²)). So d(p_X(z), p_Y(z)) ≤ ε + C(f_0 + ε_* + ε²) ≤ C_clε (f_0 ≤ C_N·4ε on Ω). ∎ This is the
clustering 19.13 needs for U = chain(V), V ∈ 𝒞_glob(ε) (with h = 1), and it shows that Z^off = the 𝔪^geo-glued construction on every
frame representative.
**Consequence: (CovLift) (i)-(iii) hold for Z^off(V) := Π^off(R^{ax}-chain(V)) on 𝒦(ε), for every level-k gauge h (no smallness):**
the chain is exactly covariant for all gauges (AX-cov; defined by Theorem N2 (b)), chain(V^h) = chain(V)^K with K(c_X) = h(X), and (b)
gives Z^off(V^h) = Z^off(V)^{ĥ}, ĥ restricting to h at level k; the cocycle and ĥ(c, ·) = c by Lemma CL-uniq; range: R^{ax} (finite DD8
mask, axial paths) plus 4; coarse translations act covariantly. **(iv) and (v) reduce to frame representatives:** if V^h = e^b on Ω,
Z^off(V^h) on Ω^{(-r)} is the 𝔪^geo-glued normal form (Lemma CL-clu), so (iv) for Z^off is (iv) for the clustered construction, i.e.
the same open items (N1-int) and (N2-bd) as on 𝒞_glob, plus (C_g-θ) (22.9) **[RBB7-fix RS7-5 (binding): literal only with (N1-int) and (N2-bd) in local form (on Ω^{(-r)} given V^h = e^b on Ω, ||b|| ≤ ε, constants independent of V outside Ω); the local forms are stated in §24.2 (Theorems N2-loc, N1-loc)]**. **Off 𝒞_glob the lift adds no wall beyond those of
𝒞_glob** (and Remark HOL for (v) on spread representatives). bb7k (spread data: corner spreads 1.39-2.76 at every site): K1 6.5e-19;
K2 5.6e-17; G_0-invariance (descents) 7.0e-11; constant covariance 2.5e-15; idempotence (descents) 7.2e-11; root-value covariance under a
Haar-random gauge 1.6e-15 with ĥ(c_Y) = k(c_Y) to 1.5e-16; continuity along a gauge path from clustered (0% of sites past r_1) to spread
(100%): output steps ≤ 8.2× the root steps; in the frame, Π^off(U_s)^{ĥ^{-1}} = Π^off(U0) to 4.7e-11 (coarse link size 0.224 there,
8.37 in the spread gauge). **KO-F1, KO-F2 do not occur.**

### 22.13 Proposition TOP: (a)-(c) PROVEN-HERE; (d) PROVEN given Lüscher's charge theorem (cited)
(a) A continuous m: SU(N)² × [0, 1] → SU(N) with m(a, b, 0) = a, m(a, b, 1) = b gives the homotopy μ(c, s) := m(c, 1, s) from id to the
constant 1, so SU(N) would be contractible; it is not (π_3(SU(N)) = Z, N ≥ 2). No equivariance is needed. Now take any G_0-invariant,
root-normalised gluing and the pure-gauge fields U = 1^k: by G_0-invariance Ĝ := G(1^k)k depends only on k's root values, and Ĝ has
the values k(c_X), k(c_Y) at the ends of an edge; if Ĝ restricted to the edge were continuous in (k(c_X), k(c_Y)) and in a continuum edge
variable, it would be such an m. **So a covariant slice that is continuous in a continuum cell variable on all data does not exist:
this is the topological content of CL-F4.** (b) On the lattice the edge variable is discrete, and only continuity in the data is
needed: Z^off has it, at the price of O(1) jumps on spread data (for d(a, b) ≥ r_2, m_w(a, b) = a for w < 1 and b at the root, so Ĝ jumps
next to the root). (c) Spread corner data occur only where V is not small in the given gauge (by Lemma CL-clu, frame representatives
are C_clε-clustered, and C_clε < r_1); (CovLift) asks no bound there (its (iv) is demanded in frames). (d) For admissible fields
(small plaquettes) Lüscher's construction (CMP 85 (1982) 39, cited from memory, not opened) defines an integer topological charge Q,
gauge invariant and continuous on the admissible class; t ↦ e^{tb} stays admissible for V = e^b ∈ 𝒞_glob, so Q = Q(1) = 0 on the gauge
saturation of 𝒞_glob, while 𝒦(ε) on large tori contains fields with Q ≠ 0 (discretised large instantons). **So (KΠ-off) is needed
beyond large gauges, and Z^off covers these fields** (it uses no global gauge). **KO-F3: no obstruction to (CovLift) (i)-(iii) on the
lattice; the continuum-smoothness obstruction OCCURS, harmlessly.** Remark on the Karcher mean: for antipodal a, b = -a in SU(2) every
weighted mean is non-unique (the minimisers of w s² + (1 - w)(π - s)² form a 2-sphere), so M of 19.13 has no continuous extension to all
data; this is the concrete CL-F4 (bb7k's control K10 used Haar spreads ≤ 2.76 < π and did not reach it, see 23).

### 22.14 Remark HOL: ARGUED
On spread representatives ψ is not analytic, so z ↦ Z^off(e^zV^r) is not holomorphic there. GI-cov and BB-gi_k consume the lift through
gauge-invariant local functionals (densities D(u; V), activities R(X)) and through the frame-transplanted backgrounds Z^sm(e^{b̃_□}) of
clustered data; a gauge-invariant local functional can be evaluated in a frame, where Z^off = the 𝔪^geo-glued construction is analytic
(Lemma CL-clu). So (v) is needed, and holds, on frame representatives only [ARGUED: GI-cov's proof (§13) not re-read line by line for
other uses of (v) in the given gauge].

## 23. Session-7 check record, outcome and notes for other files (written after §22)

**Checks** (criteria checks/bb7g_criteria.md, bb7c_criteria.md, bb7n_criteria.md, bb7k_criteria.md born 10:28:08 UTC; scripts
checks/bb7g_n1g.py 10:28:43, bb7c_resid.py 10:29:15, bb7n_chain.py 10:31:10 (one pre-run edit: a dead stub removed), bb7k_off.py
10:32:39 (one pre-run sed edit, which also reset its birth time: an `if False` expression replaced by its value); no criterion
touched). Runner scratchpad bb7/run_bb7.sh: one lock acquisition 10:34:18-10:35:23 (the lock was held by another worker at 10:32;
load1 3.03, memory free 36% on arrival, 34% after; nice 10; thread variables 1; PYTHONDONTWRITEBYTECODE=1; /usr/bin/time -l; python3
without -I; no `timeout`; no trap; `rmdir` once). No process left; no __pycache__ in checks/.
- **bb7g: ALL PASS (G1-G5).** 0.29 s, 289 MB. Σ|∇_1G_M| = M/4 to ≤ 3.6e-14 (M = 8-48); (M² - 1)/(4M) for M = 9, 15; unimodality,
  monotonicity and the 1D formula at float precision; max|y|³|∇G| = 0.1735. Reproduces REVIEW_BFT_B_S6 D.4.
- **bb7c: ALL PASS (C0-C4).** 0.40 s, 263 MB. **[RBB7-fix RS7-8: C3's threshold (max ≤ 2·top; measured 1.948) is tight; the θ = 1 profile converges to ≈ 4.3 against 4.32, so a depth-6 run could fail C3 without contradicting Cg-lin (REVIEW_BFT_B_S7 C.5)]** Root covariance 1.3e-16; Q_axS_1 = 1 to 7.7e-15; Γ0 exact (0.0; control 1.500); symmetric
  θ = ½ ratio 0.22; θ = 1 bounded (max/top 1.95); asymmetric control grows ×11.9 over four levels (×1.73 per level).
- **bb7n: ALL PASS (L0, N-a..N-d).** 0.82 s, 178 MB. **[RBB7-fix RS7-8: the reviewer's amplitude-corrected run (bisection to f_k = 0.1000, 0.2000; REVIEW_BFT_B_S7 E.3, scratchpad revBB7/bb7n_amp.py) ALL PASS: R_1, R_2, R_3 = 1.2769, 1.3100, 1.3272 at f_k = 0.10 (1.2768, 1.3100, 1.3261 at 0.20), deviation from the linear chain 0.0006·f_k, N-c 4.3e-16, stencil ratios 1.468, 2.859, 4.905 < 5.06. N-d's ungauged number (5.33·f_k at 0.26, 1.89·f_k at 0.10) is the O(|b|²) block-corner commutator missed by exp(linear refinement), not noise; the control remains valid]** Profiles in 22.5. Disclosure: f_k = 0.26 / 0.52 instead of the 0.10 / 0.20 named
  in the criteria (rescaling used the unscaled field); thresholds are relative to f_k.
- **bb7k: NOT ALL PASS (K1-K8 PASS, K10 FAIL).** 63.4 s, 35 MB. **[RBB7-fix RS7-8: the control K10 was mis-designed (Haar spreads ≤ 2.76 < π never reach the antipodal regime); the control actually demonstrating CL-F4 for the Karcher gluing is REVIEW_BFT_B_S7 E.2's near-antipodal probe (non-unique limits on antipodal pairs, an O(1) jump of the Karcher mean across the cut locus, 74/172 start disagreements), where the cut-off m_w stays continuous]** K1-K8 as in 22.11-22.12. **K10 (control) FAILED:** the Karcher gluing of
  the spread corner points (Haar-random root gauges; spreads 1.39-2.76) converged from both starts to the same point at every site
  (max disagreement 0.000, no non-convergence). The prediction "Karcher gluing on spread data depends on the start" was wrong for
  this sample: the spreads stay below the cut locus (π), where the iteration happened to be start-independent. CL-F4's actual failure
  needs near-antipodal corner data (22.13, last remark: there every weighted Karcher mean is non-unique, a 2-sphere of minimisers);
  this was not measured. The control's failure does not affect K1-K8, which test Z^off itself.
- *Reading (measured only).* The (N1-G) constant is exactly ¼. In the d = 2 model, the symmetric S4'-type root map's weighted residuals
  decay at θ = ½ and stay bounded at θ = 1, while an asymmetric map's grow like L^{θ} per level. The nonabelian framed DD8 chain's coarse
  curvature ratio converges with depth (1.277, 1.310, 1.325), tracks the linear chain to 0.3%, and is exactly gauge covariant. The cut-off
  gluing is root-exact, G_0-invariant, constant-covariant, idempotent and continuous on fully spread data. Not measured: d = 4 nonabelian
  chains, depth > 3, the nonlinear residuals (Cg-NL), near-antipodal Karcher failure, topological-charge configurations.

| Item (session 7) | Status | Note |
|---|---|---|
| Binding and cosmetic fixes of REVIEW_BFT_B_S6 (RS6-1..RS6-9) | applied, tagged [RBB6-fix] | co-closed scope of RH-inv, V_l OPEN; commutator rows; T = 3, 4 by lift; small-gauge scope of CovLift-KΠ (i), CL-F4 off 𝒞_glob, (KΠ-off) named; (N2-0) per level; (N1-G) = Lemma N1G; renames RHT, t, C_ℓ, Φ_0, C_bch; 09:35:12 correction marked; struck clause; "more precisely" annotated; A5 time |
| Remark PL (T = 3, 4) | PROVEN-HERE (routine) | C_b(T) ≤ e^{16m+4m'}C_b(2T) **[RBB7-fix RS7-2: e^{20m}C_b(2T), the pre-stated constant; T = 1, 2 by the q-fold lift, ARGUED-routine]**; **LRL (b) for all T ≥ 3** |
| Lemma N1G ((N1-G), C_G = ¼) | IMPORTED-AND-REVERIFIED (REVIEW_BFT_B_S6 D.4) | bb7g reproduces; (N1-bd), NF-ex, KΠ import-free |
| Lemma S2K | PROVEN-HERE | k-uniform ℓ¹ and Lipschitz bounds of the composite 2-form kernels (DD8) |
| Lemma N2-step | PROVEN-HERE | one framed refinement step: curvature = S_2 of transported curvature + O(ρ_{j+1}²f²) |
| **Theorem N2 ((N2-0) per level)** | **PROVEN-HERE** | f_j ≤ 2Λ_2f_k for all j, k-, T-, j-uniform, curvature-only (no global gauge); axial stencils small; box clause; (N2-lip) |
| Corollary N2-cons | PROVEN as an implication | box normal forms exist on 𝒦(ε_1); CovLift-KΠ (i)-(iii) on 𝒞_glob unconditional (small gauges) |
| Lemma Γ0 | PROVEN-HERE given the S4' reflection property L1 (cited) | S4' root map kills constant curvature |
| **(C_g-θ) written; Proposition Cg-lin** | **PROVEN-HERE** | linear lift: (C_g-θ) for all 0 ≤ θ ≤ 1, C_g^lin = 16κ_+L^θΛ_2' |
| Proposition Cg-NL | first-order term PROVEN as an implication; BCH remainder ARGUED | nonlinear (C_g-θ), 0 < θ ≤ 1 |
| C_g design decision | justified | keep lane A's Q and weights; options (a)-(c) not needed |
| Lemma CUT | PROVEN-HERE | continuous bi-equivariant cut-off interpolation; root-exact; face-consistent; = 𝔪^geo on clustered data |
| Lemma CL-clu | PROVEN-HERE (constants not evaluated) | frame representatives have C_clε-clustered corner data; repairs 19.13's domain clause for chain(V) |
| **Theorem KΠ-off** | **PROVEN-HERE ((a)-(c)); (d) as in KΠ** | **Z^off: (CovLift) (i)-(iii) on 𝒦(ε) for every level-k gauge; (iv), (v) reduce to frame representatives (the 𝒞_glob walls)** |
| Proposition TOP | (a)-(c) PROVEN-HERE; (d) given Lüscher's charge theorem (cited) | the obstruction is the non-contractibility of SU(N): it forbids continuum-smooth covariant gluing on spread data, not the lattice construction |
| Remark HOL | ARGUED | (v) needed and holding on frame representatives only |
| Failure modes | N2-F1 does not occur; Cg-F1 does not occur (OCCURS for the asymmetric control); KO-F1, KO-F2 do not occur; KO-F3: no lattice obstruction to (i)-(iii); continuum obstruction OCCURS, harmless | |
| bb7g, bb7c, bb7n, bb7k | 3 ALL PASS; bb7k NOT ALL PASS (control K10 failed; K1-K8 pass) | |

**What (KΠ-off) rests on now.** (CovLift) (i)-(iii) on the whole locally-small class 𝒦(ε) (holonomies, torons, nonzero topological
charge) for every gauge: Z^off, PROVEN modulo the cited Karcher-free facts (none: 𝔪^geo replaces the Karcher mean) and Lemma CL-uniq.
(iv): the same as on 𝒞_glob — (N1-int) (routine) and (N2-bd) (moderate; Theorem N2 is its zeroth order) — plus (C_g-θ) (linear PROVEN;
nonlinear BCH remainder ARGUED). (v): on frame representatives (Remark HOL, ARGUED). So **the "single gauge" requirement is replaced by
the covariant section Z^off**, and off 𝒞_glob no wall is added to the 𝒞_glob list **[RBB7-fix RS7-5: read "no wall is added, given the local forms of (N1-int) and (N2-bd)" (§24.2)]**. GI-off (13.8) still needs (Mult-Y), (SL-cov) and
(I-id) off 𝒞_glob (lane A's BFT-0 there); those are unchanged.

## FOR OTHER FILES (session 7; for their owners; not edited)
- **BFT_A (lane A).** (1) LRL (b) holds for all T ≥ 3 (Remark PL). (2) Lemma N1G proves the ℓ¹ form of BA-7 (Σ|∇G_M| = M/4); lane A's
  pointwise BA-7 import is untouched. (3) The (C_g-θ) clause needs no change to lane A's Q or weights: the S4' family's transverse
  reflection symmetry (L1) kills the first-order residual of any smooth refinement (Lemma Γ0); please confirm the uniform weighting
  of the S4' average used in BFT_A's linearised Q, which Lemma Γ0 assumes. **[RBB7-fix RS7-8: question withdrawn, answered by BFT_A l.1112 (uniform avg_{σ,y}; REVIEW_BFT_B_S7 C.4)]** (4) Theorem RH is now named Theorem RHT (your Lemma RH,
  §23.8, keeps its name). (5) The non-co-closed BCH₂ remainder V_l remains outside lane B's Lemma RT.
- **REVIEW (next lane-B review).** Check first: Lemma N2-step (22.4 (1): the X'-interior values against R(A^X)); the telescoping and
  absorption in Theorem N2 (22.5); Lemma Γ0's use of L1 (22.7); Lemma CL-clu (22.12) and its repair of 19.13's domain clause; Lemma
  CUT's face consistency and Theorem KΠ-off (b) (22.11-22.12); Proposition TOP (22.13); bb7k's failed control K10.
- **HIST / SF.** Theorem N2 is a curvature-only, depth-uniform statement for the framed DD8 chain (no per-level ε hypothesis as in
  HIST's MSG); MSG was not needed for (KΠ-off).

# Session 8 (2026-10-28 UTC)

## 24. PRE-STATED (session 8) — statements only; the FIRST edit of session 8 (appended before any [RBB7-fix] edit, before any session-8 proof, criteria file or script). Nothing in §24 cites a result of this session. Reading of REVIEW_BFT_B_S7 (all, binding), REVIEW_BFT_A_S7 (Parts 3-4: the Γ_E^T request), BFT_A §31.0-31.1, 33.1, 33.7, BFT_B §12.2, §15-§23 and BFT_B_LOG session 7 preceded this append, with exploratory reasoning (not recorded); its only claim is file order. Lane A's session-8 request was not yet written (BFT_A.md mod 10:26:38, BFT_A_LOG.md mod 10:26:52 at 11:10 UTC), so (GE-T) is stated in the form REVIEW_BFT_A_S7 Part 4 asks for (an ℓ¹ → ℓ¹ or ℓ^∞ → ℓ^∞ bound with explicit n-power, and locality, for Γ_E^T = Σ_X(λ^E_X)^Tχ^5_X). Proofs follow later in this file.

### 24.0 Definitions
- **Box data.** For a level-k site X: Ñ_X, N_X, N'_X (half-width 3/2), χ^5_X, λ^E_X as in §15.0 and 16.2; S := 4n + 1 (own side of
  Ñ_X); **M_n := 2S = 2(4n + 1)**, the side of the reflection torus 𝕋_R of Lemma REF (§18.2). d_X: level-0 functions on Ñ_X → 1-forms
  on the links with both ends in Ñ_X; d*_X := d_X^T (Neumann divergence); -Δ_X := d*_Xd_X. ⟨ψ⟩ := Σ_{Ñ_X}ψ. For neutral ψ
  (⟨ψ⟩ = 0), G_Xψ := any u with -Δ_Xu = ψ (d_Xu is unique). All maps act componentwise on su(N) (orthonormal basis); own units;
  ||·||_1, ||·||_∞ over all sites / links of the torus; transposes for the own ℓ² pairings.
- **Γ_E := Λ** (BFT_A §31.0): Γ_E(x) = Σ_Xχ^5_Xλ^E_X(x) (each term 0 off N_X), so Γ_E^Tφ = Σ_X(λ^E_X)^T(χ^5_Xφ) for level-0 functions φ.
- **Image fields.** For y ∈ Ñ_X, a^X_y := the function on Ñ_X obtained by restricting Σ_{y'}G_{M_n}(· - y') (y' over the 2^d
  reflection images of y in 𝕋_R; G_M the mean-zero Green function of -Δ on the d-dim torus of side M), and A^X_y := d_Xa^X_y.
- **Level-l sources (lane A's dual form, REVIEW_BFT_A_S7 Part 4).** A level-l current j (0 ≤ l < k), own sup ||j||_∞; s := L^l;
  D(j) := ev^{(l)T}d*j (a level-0 function on the level-l roots); Q_X(φ) := ⟨χ^5_X, φ⟩.
- **Frames (local form, RS7-5).** V ∈ 𝒦(ε_1) on a torus, Ω a coarse region, h a level-k gauge with V^h = e^b on Ω, ||b||_∞ ≤ ε;
  Ω^{(-r)} := {points at coarse distance ≥ r from the complement of Ω}; Z := chain(V^h) := R^{ax}_0∘…∘R^{ax}_{k-1}(V^h);
  Z^off := Π^off(Z) (Construction KΠ-off). Logarithms are the geodesic log (inverse of exp on the injectivity ball, into su(N)).
- **Covariant curvature difference.** For level-j plaquettes p, p' at coarse distance |p - p'| ≤ 1: τ(p, p') := the transport of Z
  along the level-j axial path (fixed coordinate order) from p's first corner to p''s; δF_j(p, p') := F_j(p) - Ad_{τ(p,p')}F_j(p')
  (it rotates by Ad of the gauge at p's corner, so |δF_j| is gauge invariant); [F_j]_{Lip;A} := sup{|δF_j(p, p')|/|p - p'| :
  p, p' ⊂ A, 0 < |p - p'| ≤ 1} (coarse level-j units).
- **Row defect.** For a level-(j+1) link (X, X') (j < k), d_j(X, X') := log((row product of Z_j from c_X to c_{X'})^{-1}Z_{j+1}(X, X'))
  (the straight level-j root row, Q_ax's path).

### 24.1 Step 2 statements: (GE-T) for lane A
- **Lemma GE-T (the box-Neumann adjoint Γ_E^T).** For every level-0 function φ and every level-k site X:
  (a) *Representation.* (λ^E_X)^Tψ = -d_XG_X(ψ - ⟨ψ⟩δ_{c_X}) on the links of Ñ_X (0 elsewhere); hence d*[(λ^E_X)^Tψ] =
  -(ψ - ⟨ψ⟩δ_{c_X}) on Ñ_X (Neumann divergence), and (λ^E_X)^Tψ = -Σ_wψ(w)A^X_w + ⟨ψ⟩A^X_{c_X}.
  (b) *Locality.* (Γ_E^Tφ)(b) depends on φ only on ∪{N_X : b ⊂ Ñ_X} ⊂ B_∞(b, 3) (coarse); supp Γ_E^Tφ ⊂ ∪{Ñ_X : χ^5_Xφ ≢ 0}.
  (c) *ℓ¹.* ||(λ^E_X)^Tψ||_1 ≤ M_n||ψ - ⟨ψ⟩δ_{c_X}||_1 ≤ 2M_n||ψ||_1, and **||Γ_E^Tφ||_1 ≤ 2M_n||φ||_1 = 4(4n + 1)||φ||_1**.
  (d) *Dual (sup-data) bound.* |λ^E_X(x)(z)| ≤ 2M_n max_{Ñ_X}|x_0| for z ∈ Ñ_X; hence ||Γ_Ex||_∞ ≤ 2M_n||x_0||_∞, i.e.
  ||Λ(x)||_∞ ≤ 20||x^c_0||_∞ in coarse units, with sup data only (contrast EP-int (a), which uses Hölder data).
  (e) *ℓ^∞.* C_∞ := sup over even M, y, μ of |∇_μG_M(y)| obeys C_∞ ≤ 2. ||(λ^E_X)^Tψ||_∞ ≤ (M_n/4)||ψ||_∞ + 2^dC_∞|⟨ψ⟩|,
  and ||Γ_E^Tφ||_∞ ≤ 5^d[(M_n/4)||φ||_∞ + 2^dC_∞max_X|Q_X(φ)|]. The second term (the pinned compensation charges ⟨χ^5_Xφ⟩ at
  the level-k roots) is the only one that is not O(n||φ||_∞).
  (f) *Lane A's level-l sources.* ||D(j)||_∞ ≤ 2d||j||_∞, ||D(j)||_1 ≤ 2||j||_1, and |Q_X(D(j))| ≤ (15/4)d2^d(n/s)^{d-1}||j||_∞
  (= 240L^{3(k-l)}||j||_∞ in d = 4). Hence ||Γ_E^TD(j)||_1 ≤ 4M_n||j||_1, and in sup Γ_E^TD(j) = B_j + P_j with
  ||P_j||_∞ ≤ 5^d2^dC_∞·240L^{3(k-l)}||j||_∞ (the root part) and ||B_j||_∞ ≤ 5^d(M_n/4)·2d||j||_∞ (the bulk part; n-power 1).
  *Sharper bulk bound [ARGUED, given the pointwise decay |∇G_M(y)| ≤ C|y|^{-3} (lane A's BA-7 import, not reverified here)]:*
  ||B_j||_∞ ≤ C(1 + L^{k-4l})||j||_∞ ≤ 2CL^{3(k-l)}||j||_∞. So the S_E correction Γ_E^TD(j) of a level-l source is, in sup,
  O(L^{3(k-l)}||j||_∞), concentrated near the level-k roots: the same order as (PW-i)'s dual bound.
  *Planned: (a)-(f) PROVEN-HERE except the marked ARGUED clause (inputs: 16.1, Lemma REF's reflection, Lemma N1G, and the
  monotonicity of G_M along coordinate lines from REVIEW_BFT_B_S7 B.2).*
- **Remark GE-T' (S_E against the 𝒩-optimal representative in ℓ¹).** Not claimed. At level 0, Π_E - 1 = d∘Λ, and on each box
  d_Xλ^E_X = -(the ℓ²(Ñ_X) projection onto gradients), a box Riesz projection whose ℓ¹ → ℓ¹ norm grows like log n [ARGUED: kernel
  |∇∇G| ~ |z|^{-4} in d = 4]. So an operator-norm comparison loses a factor 1 + log n = O(k); a k-uniform comparison has to use
  the structure of Y^p. *Planned: ARGUED (obstruction to the naive route); the comparison itself OPEN.*

### 24.2 Step 3 statements: local (N2-bd), local (N1-int), (CovLift) (iv)
- **Theorem N2-loc ((N2-bd) in local, gauge-invariant form).** There are ε_2 ≤ ε_1, r_N < ∞ and C_N', C_H, C_d depending only on
  (L, φ, N, d) (independent of k, T, j), such that if V ∈ 𝒦(ε_1) and V^h = e^b on Ω with ||b||_∞ ≤ ε ≤ ε_2, then on Ω^{(-r_N)},
  for every 0 ≤ j ≤ k: (a) f_j ≤ C_N'ε; (b) [F_j]_{Lip} ≤ C_Hε; (c) |d_j(X, X')|_own ≤ C_dρ_{j+1}⁴ε² (j < k); (d) all of this
  reads V^h only on Ω. *Planned: PROVEN-HERE* ((a) the Theorem-N2 telescope localised; (b) the same telescope with one common
  reference frame for p and p' and the Lipschitz kernel of Lemma S2K; (c) Lemma N2-step's axial frames). *Reading:* the chain is
  not C^{1,α}-small in any gauge (face links carry coarse links; linearly R(dν) = dC_0ν), so (a)-(c) is the part of (N2-bd) that
  the slice estimate consumes.
- **Theorem N1-loc ((N1-int) in local form: the nonlinear EP-int).** There are η_0 = η_0(N, d) > 0 and C_I = C_I(α, d, N, L)
  (k-, T-uniform) such that if U on Ñ_X has a box normal form with w := log U^{g_X(U)}, sup_{Ñ_X}|w^c| ≤ η ≤ η_0, then on N'_X:
  **sup|w^c| + sup|∇^cw^c| + [∇^cw^c]^∞_α ≤ C_I(η + f_0(Ñ_X) + [F_0]_{Lip;Ñ_X})** (curvatures of U; gauge invariant).
  *Planned: PROVEN-HERE given LES-div (PROOF [S15]) — the bootstrap of 16.2 with dw = (curvature of U^{g_X}) - B(w) as the
  divergence-form source, the BCH part B absorbed by an iteration in the distance to ∂Ñ_X (no boundary regularity).*
- **Corollary CL-iv ((CovLift) (iv), first clause, for Z^off in frames).** Under Theorem N2-loc's hypotheses with RS7-7's
  smallness (C_clε ≤ r_1/2 ≤ convexity radius), in the frame gauge: ||log Z^off_j||_{C^{1,α}} ≤ C_1ε on Ω^{(-r)} for every
  0 ≤ j ≤ k (sup, coarse gradient, pointwise Hölder of the gradient; level-j coarse units), r := r_N + 4 + (the RS7-7 box margin),
  C_1 k-, T-uniform; with Proposition Cg-NL at θ = 0 for the residual term, the local 𝔐^∇ size of log Z^off on Ω^{(-r)} is
  ≤ C_smε. *Planned: PROVEN as an implication* of Theorems N2-loc, N1-loc, NF-ex, Lemmas CL-clu and CUT (level 0: 𝔪^geo of the
  corner transition gauges κ_X := g_Xg_*^{-1}; levels j ≥ 1: the Q_ax-row recursion with the defects (c)); the residual term in
  Cg-NL's status (first order PROVEN, BCH remainder ARGUED). Not covered: the non-residual components of g_Z at θ > 0 (OPEN);
  (v) (Remark HOL, ARGUED).

### 24.3 Failure modes (pre-stated)
- **GE-F1** ||(λ^E_X)^T||_{1→1} grows faster than n (a corner/edge loss). Expected: NOT (reflection; degree -1 kernel).
- **GE-F2** the root part P_j exceeds O(L^{3(k-l)}||j||_∞). Expected: NOT.
- **GE-F3** the box Riesz projection is ℓ¹-bounded uniformly in n. Expected: NOT (log n) [guess].
- **N2L-F1** the covariant Lipschitz ratio [F_j]_{Lip}/f_k or the defect ratio ρ_{j+1}^{-4}|d_j|/f_k² grows with depth. Expected: NOT.
- **N1L-F1** the interior C^{1,α} constant of the nonlinear normal form grows with n. Expected: NOT.
- **N1L-F2** the BCH boundary layer reaches N'_X. Expected: NOT (margin ½ coarse).

### 24.4 Checks (criteria files written after this section and before the scripts)
- **bb8t** (d = 4, exact FFT on 𝕋_R, n = 2-6): the Neumann identity (a) and zero crossing flux; ||(λ^E_X)^Tδ_w||_1 against M_n||ρ||_1
  and its ratio to n; max|∇G_M| against 2; the ℓ^∞ bound (e) on random ψ; adjointness against an independent direct minimisation
  (n = 2); the Q_X bound (f) (combinatorial, n = 27, s = 1, 3, 9); controls: the pinned part's sup grows like n^d for ψ = 1_{N_X};
  the adjacent-dipole ℓ¹ norm grows like log n (GE-F3).
- **bb8n** (d = 2, SU(2), DD8, depths 1-3, bb7n's chain): [F_j]_{Lip}/f_k and ρ_{j+1}^{-4}|d_j|/f_k² against depth (N2L-F1);
  control: the non-covariant difference |F_j(p) - F_j(p')| in a Haar-random level-k gauge is O(f_k), not O(|p - p'|f_k).
- **bb8w** (d = 2, SU(2)): box normal forms of one smooth small-curvature coarse profile at n = 3, 9, 27: sup|w^c|, sup|∇^cw^c|
  and a Hölder proxy of ∇^cw^c on N'_X against n (N1L-F1); informational: the same on all of Ñ_X (boundary layer).

## 25. Proofs (session 8; appended after §24 (11:12:37 UTC), after Step 1 (11:13-11:15:04) and after bb8t, bb8n, bb8w (11:21:05-11:21:12) and the probe bb8n_defect (11:25:12-11:25:13) ran)

Post-proof corrections of pre-stated details are marked **[post-proof correction]**; §24 is not edited. They are: (1) Lemma GE-T
(f): the combinatorial sum is exact, Σ_{level-l links}|d ev χ^5_X| = 2d(n/s)^{d-1}, so |Q_X(D(j))| ≤ 2d(n/s)^{d-1}||j||_∞
(= 8L^{3(k-l)}||j||_∞ in d = 4, sharp), not only ≤ 240L^{3(k-l)}||j||_∞; (2) Lemma GE-T (c), (e) use Lemma N1G, which is a 4D
statement: (c), (e) are proven for d = 4 (the case needed); (3) **Theorem N2-loc (c) holds with C_d = 0: the root-row defect
vanishes identically** (the straight root row lies on the first branch of the axial tree and the interpolatory transverse weights
are δ, so R^{ax} puts exp(0) on the row's interior links and exp(0)·Z(X, X') on its face link); the pre-stated O(ρ⁴ε²) was an
over-estimate, and bb8n's criterion L-c, which assumed a nonzero second-order defect, failed for that reason (23-type record in
§26); (4) Lemma GE-T (e): the measured C_∞ is (1 - M^{-4})/8, attained at the nearest-neighbour link (informational; the proof gives
C_∞ ≤ 1.71).

### 25.1 Lemma GE-T: PROVEN-HERE ((a)-(f); d = 4 for (c), (e)); the sharper bulk bound ARGUED as marked
(a) λ := λ^E_X(x) minimises ||x_0 + d_Xλ||² on {λ(c_X) = 0}. The first variation in every direction ν (constants give 0) gives
d*_X(x_0 + d_Xλ) = 0, i.e. -Δ_Xλ = -d*_Xx_0; d*_Xx_0 is neutral (⟨1, d*_Xx_0⟩ = ⟨d_X1, x_0⟩ = 0). Hence λ = -(1 - 1δ_{c_X}^T)G_Xd*_Xx_0
(any choice of G_X on neutral functions; the projector fixes the constant). For ψ on Ñ_X, with ρ := ψ - ⟨ψ⟩δ_{c_X} (neutral):
⟨ψ, λ⟩ = -⟨ρ, G_Xd*_Xx_0⟩ = -⟨d_XG_Xρ, x_0⟩ (G_X symmetric on neutral functions, constants pair to 0 against neutral ones). So
(λ^E_X)^Tψ = -d_XG_Xρ, and d*_X(λ^E_X)^Tψ = -(-Δ_X)G_Xρ = -ρ. Images: by Lemma REF (19.11) the reflection torus 𝕋_R has each site
= ϱ_Az for a unique box site z and A ⊂ {1..4}; ρ^R(ϱ_Az) := ρ(z) is neutral, u := G_{M_n}ρ^R solves -Δu = ρ^R, and u is reflection-even
(G_M commutes with the reflections). At a box site z the torus neighbours outside the box are reflections of z itself, with equal
values of u, so (-Δu)(z) = (-Δ_Xu|_box)(z): u|_box solves the Neumann problem, and d_XG_Xρ = d_X(u|_box) = Σ_wρ(w)A^X_w (the uniform
backgrounds of G_M cancel since Σρ = 0). With ρ = ψ - ⟨ψ⟩δ_c: (λ^E_X)^Tψ = -Σ_wψ(w)A^X_w + ⟨ψ⟩A^X_{c_X}. Γ_E^Tφ = Σ_X(λ^E_X)^T(χ^5_Xφ)
is the transpose of Γ_E = Σ_Xχ^5_Xλ^E_X term by term. **bb8t T0** (|d*_XF - ρ| ≤ 1.2e-15, crossing flux ≤ 8e-16, n = 2-6) and **T4**
(adjointness against an independent CG solve of the normal equation, 1.7e-14).
(b) A term (λ^E_X)^T(χ^5_Xφ) is nonzero only if χ^5_Xφ ≢ 0, lives on the links of Ñ_X, and reads φ on supp χ^5_X ⊂ N_X; a link of Ñ_X
(|b - c_X|_∞ ≤ 2) and a point of N_X (|w - c_X|_∞ ≤ 1) are within coarse distance 3.
(c) (d = 4.) Each box link has 2^4 images in 𝕋_R carrying ±du (reflections are lattice automorphisms and u is even); each link crossing
a reflection plane is mapped to itself reversed by that reflection, so du = 0 there. Hence Σ_box|du| = 2^{-4}Σ_{𝕋_R}|du|. Per direction μ,
du_μ = Σ_yρ^R(y)∇_μG_M(· - y), so by Lemma N1G (M_n even): Σ_{𝕋_R}|du| ≤ Σ_y|ρ^R(y)|·Σ_μΣ_z|∇_μG_M(z)| = 2^4||ρ||_1·4·(M_n/4). So
**||(λ^E_X)^Tψ||_1 ≤ M_n||ρ||_1 ≤ 2M_n||ψ||_1**, and, χ^5 ≥ 0 with Σ_Xχ^5_X = 1: ||Γ_E^Tφ||_1 ≤ Σ_X2M_n||χ^5_Xφ||_1 = 2M_n||φ||_1. ∎(c)
**GE-F1 does not occur.** bb8t T1: ||F||_1 for point dipoles is ≤ 0.64·(2M_n) (corner, the worst; 63.41 against 100 at n = 6), and
max_w||F||_1/n = 10.66, 10.62, 10.60, 10.58, 10.57 for n = 2-6 (linear in n, slightly decreasing ratio).
(d) For z ∈ Ñ_X: λ^E_X(x)(z) = ⟨(λ^E_X)^Tδ_z, x_0⟩ ≤ ||(λ^E_X)^Tδ_z||_1max|x_0| ≤ M_n||δ_z - δ_{c_X}||_1max|x_0| = 2M_nmax_{Ñ_X}|x_0|;
then |Λ(x)(z)| ≤ Σ_Xχ^5_X(z)|λ^E_X(x)(z)| ≤ 2M_n||x_0||_∞, and 2M_n/n = 4(4n + 1)/n ≤ 20. bb8t T4: the extremal x = sign(-F) attains
λ(x)(corner) = ||F||_1 = 21.31 exactly (n = 2), below 2M_n = 36.
(e) (d = 4.) *C_∞.* The 4D torus kernel factorises (22.2 (1)), and by REVIEW_BFT_B_S7 B.2 (RS7-3) each cycle kernel q_t is symmetric
and non-increasing on [0, M/2]; so G_M(y) - G_M(y') = ∫_0^∞(p_t(y) - p_t(y'))dt is, along every coordinate line, symmetric and
non-increasing in |y_ν|, and G_M(0) = max G_M. For 0 ≤ y_μ < M/2: |∇_μG_M(y)| = G_M(y) - G_M(y + e_μ) ≤ Σ_{t<M/2}(G_M(y + te_μ) -
G_M(y + (t + 1)e_μ)) = G_M(y_⊥, 0) - G_M(y_⊥, M/2) ≤ max_y(G_M(0) - G_M(y)) (the other half by symmetry). By Fourier, with k_i = 2πm_i/M,
|m_i| ≤ M/2, λ(k) = Σ4sin²(k_i/2) ≥ (4/π²)|k|² = 16|m|²/M², and the shell count (2r + 1)⁴ - (2r - 1)⁴ = 64r³ + 16r (r = |m|_∞, |m|² ≥ r²):
G_M(0) - G_M(y) = M^{-4}Σ_{k≠0}(1 - cos k·y)/λ(k) ≤ 2M^{-4}Σ_{m≠0}M²/(16|m|²) ≤ (1/(8M²))Σ_{r=1}^{M/2}(64r + 16/r)
≤ (1/(8M²))[8M(M + 2) + 16(1 + ln(M/2))] = (M + 2)/M + 2(1 + ln(M/2))/M² ≤ 1.71 for every even M ≥ 4. So C_∞ ≤ 1.71 ≤ 2.
*Sup bound.* For a box link b = (z, z + e_μ): |Σ_wψ(w)A^X_w(b)| ≤ ||ψ||_∞Σ_wΣ_{w' images of w}|∇_μG_M(z - w')| = ||ψ||_∞Σ_{y∈𝕋_R}|∇_μG_M(z - y)|
= (M_n/4)||ψ||_∞ (Lemma N1G; the images of the box sites cover 𝕋_R once), and |A^X_{c_X}(b)| ≤ 2^4C_∞. So ||(λ^E_X)^Tψ||_∞ ≤ (M_n/4)||ψ||_∞ +
2^4C_∞|⟨ψ⟩|. A link b lies in Ñ_X for at most 5^4 roots X (per coordinate, at most five multiples of n within 2n of both ends), and
|χ^5_Xφ| ≤ |φ|: ||Γ_E^Tφ||_∞ ≤ 5^4[(M_n/4)||φ||_∞ + 2^4C_∞max_X|Q_X(φ)|]. ∎(e) bb8t T2: max|∇G_M| = 0.1250 for M = 18-50 [post-
proof correction (4)]; T3: the sup bound holds with ratio ≤ 0.004 on random ψ; C1: for ψ = 1_{N_X} the sup is (2n + 1)⁴·0.125 (the pinned
compensation charge |N_X| at c_X times |∇G| at the nearest link), i.e. **the second term of (e) is real and grows like n^d**.
(f) (d*j)(Y) is a signed sum of ≤ 2d link values, placed by ev^{(l)T} at Y's root (distinct roots), so ||D(j)||_∞ ≤ 2d||j||_∞ and
||D(j)||_1 ≤ 2||j||_1. Q_X(D(j)) = ⟨χ^5_X, ev^Td*j⟩ = ⟨d ev χ^5_X, j⟩, so |Q_X| ≤ ||j||_∞Σ_{level-l links}|d ev χ^5_X|. For a μ-link only the
μ-factor of χ^5_X changes: Σ_{links}|d ev χ^5_X| = Σ_μ(Σ_{y_μ∈sZ}|σ_5(|y_μ + s|/n) - σ_5(|y_μ|/n)|)·Π_{ν≠μ}Σ_{y_ν∈sZ}σ_5(|y_ν|/n). The first factor
is the total variation of t ↦ σ_5(|t|), = 2 (monotone on each side, from 0 to 1 and back); the second is n/s (the 1D partition of unity
σ_5(t) + σ_5(1 - t) = 1 summed over one period). So **Σ = 2d(n/s)^{d-1} exactly** and |Q_X(D(j))| ≤ 2d(n/s)^{d-1}||j||_∞ [post-proof
correction (1); the pre-stated (15/4)d2^d(n/s)^{d-1} also holds]. bb8t T5: ratio 8.0000 = 2d at n = 27, s = 1, 3, 9. Then (c) gives
||Γ_E^TD(j)||_1 ≤ 2M_n||D(j)||_1 ≤ 4M_n||j||_1, and (a), (e) give the split Γ_E^TD(j) = B_j + P_j, P_j := Σ_XQ_X(D(j))A^X_{c_X},
B_j := -Σ_XΣ_wχ^5_X(w)D(j)(w)A^X_w, with ||P_j||_∞ ≤ 5^4·2^4C_∞·8L^{3(k-l)}||j||_∞ and ||B_j||_∞ ≤ 5^4(M_n/4)·8||j||_∞. ∎(f)
*Sharper bulk bound (ARGUED, as marked in §24.1).* With |∇G_M(y)| ≤ C(1 + |y|)^{-3} (BA-7; bb7g measured max|y|³|∇G| = 0.1735, flat
in M), Σ_{w∈level-l roots, |w - b| ≤ 3n}|A^X_w(b)| ≤ 2^4C(C' + s^{-4}∫_s^{3n}r³r^{-3}dr) ≤ C''(1 + n/s⁴), and n/s⁴ = L^{k-4l} ≤ L^{3(k-l)}.
bb8t T6 (composite Γ_E^T on a coarse-side-5 torus, n = 3, l = 0, 81 boxes): identity D(S^E_0) = I_χ^TD to 1.5e-15, adjointness
5.6e-16, ||Γ_E^TD||_1 = 95.1 (bound 8570), sup 0.443 (bound 21215); sup|P| = 0.074, sup|B| = 0.442, max|Q_X| = 0.578.
**GE-F2 does not occur** (P_j ≤ C·L^{3(k-l)}||j||_∞ is proven; at l = 0 the bulk part dominates in the sample).
*What this gives lane A (the requested lemma, in usable form).* For a single-level source j at level l: the S_E correction
Γ_E^TD(j) is a level-0 1-form, supported within coarse distance 3 of supp j, with (i) ℓ¹ norm ≤ 4M_n||j||_1 (n-power 1; this is the
cost of one box-Neumann solve against a point charge: a dipole field |z|^{-3} summed to radius n); (ii) d*Γ_E^TD(j) = -D(j) + Σ_XQ_X
δ_{c_X} exactly, the residual charges Q_X = ⟨d ev χ^5_X, j⟩ sitting at the level-k roots with |Q_X| ≤ 8L^{3(k-l)}||j||_∞; (iii) sup ≤
C[n·||j||_∞ + L^{3(k-l)}||j||_∞] proven, C·L^{3(k-l)}||j||_∞ given BA-7. In the dual form of (PW-i) (||f^E_0[j]||_∞ ≤ C_PL^{3(k-l)}||j||_∞)
the correction is therefore of the same order as the target and localised at the roots; it cannot be dropped, and by (ii) its
composite divergence is exactly the root-charge field that makes S^E_0 composite-co-closed.

### 25.2 Remark GE-T': ARGUED (as pre-stated)
On Ñ_X, d_Xλ^E_X(x) = -P_grad x_0 (Step 0 of 16.2: the ℓ² projection onto gradients), and P_grad's row at a link b_0 = (z, z + e) is
d_XG_X(δ_{z+e} - δ_z), an adjacent dipole field (|∇∇G| ~ |y|^{-4}), whose ℓ¹ norm grows like log n. bb8t C2: ||F||_1 = 7.26, 8.30, 9.05,
9.63, 10.11 for n = 2-6, increments per log 2 of 2.59 and 2.62 (log growth; **GE-F3: OCCURS, as guessed**). So an operator-norm
comparison of Π_EY^p with the 𝒩-optimal representative loses 1 + log n = O(k); the k-uniform comparison is OPEN and needs Y^p's
structure (lane A's YH machinery). Note that (c) is not affected: (λ^E_X)^T pairs with a pinned point charge, never with an adjacent dipole
of the box itself.

### 25.3 Theorem N2-loc: PROVEN-HERE (constants not evaluated) **[post-proof correction (3): (c) with C_d = 0]**
Gauge: |δF_j|, f_j and |d_j| are gauge invariant (AX-cov: chain(V^h) = chain(V)^K with K block-constant at every level, and each of
the three quantities rotates by Ad of K at one point), so we work with chain(V^h), V^h = e^b on Ω. V ∈ 𝒦(ε_1) makes every principal log
of the chain defined and the global bounds of Theorem N2 available (used only for that).
(a) In 22.5 the telescope for a base plaquette q reads F_{j'} on supp W^{(j'-j_0)}(q, ·) (coarse radius ≤ r_sL/(L - 1)) and the chain
within C_rρ_{j'+1} of it; a level-j' chain value reads V within the chain's range (finite DD8 mask and axial paths, geometric in the
levels). Run 22.5's downward induction on the nested regions Ω_j := Ω^{(-r_j)}, r_j := (r_s + C_r + 2)Σ_{j'≥j}Lρ_{j'+1} ≤ r_N :=
(r_s + C_r + 2)L²/(L - 1), with f_k replaced by f_k(Ω) ≤ 4ε + Cε² =: ε'. Every estimate of 22.4-22.5 is pointwise in q with data in
the region, so f_j ≤ 2Λ_2ε' ≤ 10Λ_2ε =: C_N'ε on Ω^{(-r_N)} for ε ≤ ε_2.
(b) Fix j and level-j plaquettes p, p' ⊂ Ω^{(-r_N)} with coarse δ := |p - p'| ≤ 1. Use 22.5's reference transports τ(p, ·) for p,
and τ'(p', ·) := τ(p, p')^{-1}τ(p, ·) for p'. The telescope identity of 22.5 holds for any reference transports with τ(q, q) = 1 (each
increment is Lemma N2-step at one plaquette plus W^{(t+1)}(q, P) = Σ_pW^{(t)}(q, p)w_{pP}; no property of τ is used), and τ'(p', p') = 1.
Writing β_{j'}(p'') := Ad_{τ(p,p'')}e_{j'}(p'') + Σ_Pw_{p''P}(Ad_{τ(p,p'')T(p'',P)} - Ad_{τ(p,P)})F_{j'+1}(P), the increments are
I_{j'}(p) = Σ_{p''}W^{(j'-j)}(p, p'')β_{j'}(p'') and Ad_{τ(p,p')}I'_{j'}(p') = Σ_{p''}W^{(j'-j)}(p', p'')β_{j'}(p'') (the same β: one frame),
and the top terms are Σ_PW^{(k-j)}(·, P)Ad_{τ(p,P)}F_k(P). Hence
  δF_j(p, p') = Σ_P[W^{(k-j)}(p, P) - W^{(k-j)}(p', P)]Ad_{τ(p,P)}F_k(P) + Σ_{j'}Σ_{p''}[W^{(j'-j)}(p, p'') - W^{(j'-j)}(p', p'')]β_{j'}(p'').
Top: ≤ Λ_2'δf_k (Lemma S2K; source spacing ρ_k = 1). Level j' with ρ_{j'+1} ≥ δ: ||W(p, ·) - W(p', ·)||_1 ≤ Λ_2'δ/ρ_{j'}, and |β_{j'}| ≤
C_eρ_{j'+1}²f² + 2Λ_2^{(1)}c_h'ρ_{j'+1}²f² (the loop x_{j'}(p) → p'' → X → P → x_{j'+1}(p) → x_{j'}(p) has coarse diameter ≤ (C_r + 1)ρ_{j'+1},
as in 22.5; f := C_N'ε), contributing ≤ Λ_2'L(C_e + 2Λ_2^{(1)}c_h')δρ_{j'+1}f². Level j' with ρ_{j'+1} < δ: ||W(p, ·)||_1 + ||W(p', ·)||_1 ≤
2Λ_2, and for p'' near p' the loop consists of the level-j' axial path from x_{j'}(p) to p'' and the level-(j'+1) axial path from x_{j'+1}(p)
to P (same coordinate order, endpoints within C_rρ_{j'+1} of each other), closed by short segments; replacing its level-(j'+1) links by
level-j' root rows (exactly, by (c)) gives a level-j' loop bounding a ladder of width ≤ C_rρ_{j'+1} and length ≤ 4δ + C_rρ_{j'+1}, area
≤ C'ρ_{j'+1}δ, so (lasso, HIST §20.0 F4/F1; total ≤ ½ for small ε_2) |log hol| ≤ 1.011C'ρ_{j'+1}δf, and the contribution is
≤ 2Λ_2(C_e + 2.03Λ_2^{(1)}C')ρ_{j'+1}δf² (using ρ_{j'+1} < δ in the first term). Summing (Σ_{j'}ρ_{j'+1} ≤ L/(L - 1)):
|δF_j(p, p')| ≤ (Λ_2'f_k + C_2f²)δ ≤ C_Hεδ. ∎(b) **N2L-F1 does not occur** (bb8n L-a: Lip_m/f_k = 4.01, 5.70, 6.61 for m = 1, 2, 3, increments
shrinking ×0.54, the same at f_k = 0.05; L-b: |δF| gauge invariant to 4e-13; control: without the transport the ratio in a Haar gauge is
5.3, 16.9, 50.4, i.e. ∝ 1/|p - p'|).
(c) Let (X, X') be a level-(j+1) link, X' = X + e_μ, and b a level-j fine link on the straight row from c_X to c_{X'}. In X's axial frame
the row's coarse sites i = X + te_μ have axial paths a(i→X) along e_μ only (fixed coordinate order, only the μ-coordinate differs), so
A^X vanishes on every coarse μ-link of that line (tree links). (S_1A^X)(b) = s^{[1]} along μ (reading A^X(i, i + e_μ) on the line) ⊗ s in the
transverse directions at transverse offset 0, where the interpolatory scheme's weights are δ (reading only the line): so S_1A^X = 0 on the
row. μ(A^X) = 0 on X's sites (22.4 (1)), and at the face link's head c_{X'}: μ(A^X)(c_{X'}) = Σ_iΦ_0(c_{X'} - i)∫_{a(i→X)}A^X = ∫_{a(X'→X)}A^X
= 0 (Φ_0 interpolatory at roots; a tree path). So s^X = 0 on every row link, the interior row links carry exp(0) = 1 and the face link
exp(0)·Z_{j+1}(X, X'): **the row product equals Z_{j+1}(X, X') exactly, d_j ≡ 0** (nonabelian Q_axR^{ax} = 1). ∎(c) [This sharpens
22.5's "root-row product = coarse link up to own O(σ²)" and CL-clu's "O(ε²)": both errors are 0.] bb8n_defect: max own|d_j| ≤ 8.9e-17
(both amplitudes, ungauged and Haar-gauged; D-a PASS).
(d) By (a)-(c), every quantity at a point of Ω^{(-r_N)} reads V^h only within r_N. ∎

### 25.4 Theorem N1-loc: PROVEN-HERE given LES-div (PROOF [S15], reviewed)
Write Ñ := Ñ_X, w := log U^{g_X(U)}, coarse w^c = nw, sup_Ñ|w^c| ≤ η. *Equations.* NF-crit: d*_Xw = 0 at every site of Ñ. At links whose
2-neighbourhood lies in Ñ the componentwise identity -Δ = d*d + dd* gives -Δw_μ = (d*dw)_μ = Σ_ν∂^-_ν(±(dw)_{νμ}): divergence form with
g := ±dw, h = 0 (as for a in 16.2 Step 1). *Nonlinear source.* For a plaquette p ⊂ Ñ, log U^{g}(∂p) = dw(p) + B_p(w), B_p analytic in
the four link values with |B_p| ≤ C_3max_{∂p}|w|² and |B_p(w) - B_{p+e}(w)| ≤ C_3'max|w|·max_i|w(b_i + e) - w(b_i)|; and log U^g(∂p) =
Ad_{g(p)}F_0(p) =: F^N(p) (F_0 the principal log of U based at p's first corner, coarse units below). In coarse units G^c := n²dw =
F^{N,c} - B^c with |B^c| ≤ C_3η², Lip(B^c) ≤ C_3'η·sup|∇^cw^c| locally (one fine step changes B^c by ≤ n²C_3'(η/n)(|∇^cw^c|/n²) =
C_3'η|∇^cw^c|/n), and Lip(F^{N,c}) ≤ [F_0]_{Lip} + 8ηf_0 (F^N(p) - F^N(p') = Ad_{g(p)}δF_0(p, p') + (Ad_{τ^N} - 1)F^N(p'), τ^N the transport of
U^g along the axial path, |log τ^N| ≤ 4δn·η/n). On a box of coarse side ρ ≤ 1: ρ^{-α}Osc_2(G^c) ≤ ρ^{1-α}Lip(G^c) ≤ Lip(G^c).
*Interior estimate at one scale.* For z with coarse distance ≥ r to ∂Ñ (0 < r ≤ 1) and R_c := r/2, own R = nR_c ≥ 16: LES-div in the
form used in 16.2 Step 3/5 (homogeneous of degree 2 + α in coarse units), Caccioppoli (16.2 Step 2, c = 0) and Campanato telescoping give
  |∇^cw^c(z)| ≤ A_0(r^{-1}η + sup|G^c| + [F_0]_{Lip} + ηf_0) + A_1η·r·M(r/2),
  ρ^{-α}Osc_2(∇^cw^c; Q_ρ(z)) ≤ A_0(r^{-1-α}η + r^{-α}sup|G^c| + [F_0]_{Lip} + ηf_0) + A_1η·r^{1-α}M(r/2)  (ρ ≤ R/4),
with M(r) := sup{|∇^cw^c(y)| : dist(y, ∂Ñ) ≥ r} and A_0, A_1 = A(α, d, N): the B-part of [G^c] on Q_R(z) ⊂ {dist ≥ r/2} costs
C_3'η·M(r/2) times R_c^{1-α}. *Absorption by iteration in the distance.* Start at r_0 ∈ {1/4, 1/2} and iterate r_{i+1} = r_i/2 while
nr_{i+1} ≥ 32; at the last scale use the crude bound M(r) ≤ 2n·η (one fine step). With A_1η ≤ 1 and B := sup|G^c| + [F_0]_{Lip} + ηf_0:
  M(r_0) ≤ Σ_{i<m}(A_1η)^iΠ_{l<i}r_l·A_0(2^i r_0^{-1}η + B) + (A_1η)^mΠ_{l<m}r_l·2nη,
with Π_{l<i}r_l ≤ 2^{-i(i-1)/2}; the sum is ≤ 16A_0(4η + B), and the last term ≤ 2nη·2^{-m(m-1)/2} with n < 32·2^m/r_0 ≤ 128·2^m, which is ≤ 256η·2^{m - m(m-1)/2} ≤ 512η.
So M(1/4) ≤ C(η + f_0 + [F_0]_{Lip}) (sup|G^c| ≤ f_0 + C_3η²), and the Campanato bound at r = 1/2 with M(1/4) gives the Hölder term on
{dist ≥ 1/2}; Campanato-to-pointwise telescoping (16.2 conventions, margin ¼) gives [∇^cw^c]^∞_α on N'_X (dist ≥ ½). *Small k* (n < 64):
finitely many n, and |∇^cw^c| ≤ 2nη, [∇^cw^c]^∞_α ≤ 4n^{1+α}η: absorbed into C_I(L). Hence sup_{N'}|w^c| + sup_{N'}|∇^cw^c| +
[∇^cw^c]^∞_{α;N'} ≤ C_I(η + f_0 + [F_0]_{Lip}). ∎ **N1L-F1, N1L-F2 do not occur.** bb8w (d = 2, SU(2), n = 3, 9, 27, one coarse profile):
on N', A1 = 0.154, 0.164, 0.168; A2 = 0.147, 0.163, 0.178; A3 = 0.115, 0.147, 0.123 (flat; W1 PASS); ratio to (f_0 + Lip) 0.63-0.67; on the
whole box the Hölder proxy grows 0.168, 0.297, 0.466 (the boundary/corner layer, which N' excludes); the nonlinear part |w - a_lin|/|w| ≈
0.27 at amplitude 0.2 (so the test is not in the linear regime).

### 25.5 Corollary CL-iv: PROVEN as an implication (C^{1,α} terms); residual term in Cg-NL's status
Frame gauge (compute with V^h, V^h = e^b on Ω, ||b|| ≤ ε); hypotheses of N2-loc and RS7-7. Every Ñ_X used lies in Ω^{(-r_N)}.
*Level 0.* By 22.5 (c) and NF-ex the box normal forms exist with η_X := sup|w^c_X| ≤ 2C_B(f_0 + C_boxf_0²) ≤ Cε (N2-loc (a)), and N1-loc with
N2-loc (a), (b) at j = 0 gives ||w_X||_{C^{1,α}(N'_X)} ≤ Cε. Fix a cell and its lower corner X_*; for the corners X of the cells meeting
the unit ℓ^∞-neighbourhood of a point, κ_X := g_X(U)g_{X_*}(U)^{-1} on Ñ_X ∩ Ñ_* (pairs of points within distance 1 use one common corner, as
in 16.6). (i) N_X = N_*^{κ_X}, so for a link b = (y, y'): κ_X(y') = e^{-w_X(b)}κ_X(y)e^{w_*(b)}, i.e. with k := log κ_X, ∇^ck(b) =
ϕ_n(k(y), w^c_X(b), w^c_*(b)), ϕ_n(k, a, c) := n·[log(e^{-a/n}e^{k}e^{c/n}) - k] = c - a + O(|k|(|a| + |c|)) + O((|a| + |c|)²/n), analytic
uniformly in n. (ii) |k| ≤ C_clε (Lemma CL-clu). (iii) Discrete chain rule: ||k||_{C^{2,α}(N'_X∩N'_*)} ≤ C(C_clε + ||w_X||_{C^{1,α}} +
||w_*||_{C^{1,α}}) ≤ Cε. (iv) Lemma CUT (clustered: G^off = 𝔪^geo) and right equivariance: G(z) = 𝔪^geo[{κ_X(z)}]g_*(z), so
Z^off_0 = N_*^K, K := 𝔪^geo[{κ_X}] with weights w_ν = 1 - σ_5(t_ν); log K = Ψ({k_X}, w) with Ψ analytic near 0, Ψ(0, w) = 0, the weights
C^{2,1} in coarse units within cells and across faces (face consistency; σ_5', σ_5'' vanish at 0 and 1; 22.12 (d)); so ||log K||_{C^{2,α}} ≤ Cε.
(v) log Z^off_0(b) = log(K(y)e^{w_*(b)}K(y')^{-1}); in coarse units n·log(e^{κ}e^{w/n}e^{-κ'}) = Ad-type analytic function of (log K(y),
w^c_*(b), ∇^clog K(b)) with linear part w^c_* - ∇^clog K: ||log Z^off_0||_{C^{1,α}} ≤ C(||w_*||_{C^{1,α}} + ||log K||_{C^{2,α}}) ≤ C_0'ε.
*Levels j ≥ 1.* Z^off_j(b) = G(c_{b^-})Z_j(b)G(c_{b^+})^{-1} (G at level-j roots). For a level-(j+1) link (X, X'), inserting G^{-1}G at the
level-j roots of the straight row and using N2-loc (c) (d_j = 0): **Z^off_{j+1}(X, X') = the row product of Z^off_j from c_X to c_{X'}**,
exactly. With v_j := log Z^off_j: log(row) = Σ_iv_j(b_i) + β_j, and in level-(j+1) coarse units (Σ_iv_j(b_i))^c = avg_iv^c_j(b_i), an average
of L translates (sup, level-(j+1) gradient and Hölder do not increase: 16.3, Q_ax), while β_j (BCH of L near-parallel terms,
[v_i, v_{i'}] = [v_i, v_{i'} - v_i]) obeys ||β^c_j||_∞ ≤ 2L²ρ_j²||v^c_j||_∞||∇^cv^c_j||_∞ + (higher, same order), hence by the inverse estimate
(Lemma TC, step ρ_{j+1}) ||β_j||_{C^{1,α}} ≤ C_βρ_j^{1-α}||v_j||²_{C^{1,α}}. So ||v_{j+1}||_{C^{1,α}} ≤ ||v_j||_{C^{1,α}}(1 + C_βρ_j^{1-α}||v_j||_{C^{1,α}}),
and by induction from j = 0, sup_j||v_j||_{C^{1,α}} ≤ exp(2C_βC_0'εΣ_jρ_j^{1-α})C_0'ε ≤ 2C_0'ε =: C_1ε for ε small (Σ_jρ_j^{1-α} ≤
1/(1 - L^{-(1-α)})); regions shrink by Σρ_{j+1} ≤ L/(L - 1). (v_k = b, consistently.) The residual term L^{k-1-j}||r^c_j|| of 𝔐^∇ is
(C_g-θ) at θ = 0: Proposition Cg-NL (first order PROVEN, BCH remainder ARGUED). ∎ **So (CovLift) (iv), first clause, holds for Z^off
in frames, k- and T-uniformly: the sup/gradient/Hölder terms PROVEN as an implication (given LES-div), the residual term up to
Cg-NL's ARGUED remainder.** Not covered: the non-residual components of g_Z at θ > 0 (OPEN, RS5-5); (v) on frames (Remark HOL,
ARGUED); the step "log Z^off_0 analytic composition in C^{1,α}" and the BCH tail of β_j are routine discrete chain-rule estimates,
written at the level of 16.4 (not with explicit constants).

## 26. Session-8 check record, outcome and notes for other files (written after §25)

**Checks** (criteria checks/bb8t_criteria.md, bb8n_criteria.md, bb8w_criteria.md born 11:17:28 UTC; scripts checks/bb8t_get.py born
11:18:52 (one pre-run edit 11:19:08: a malformed mask-index line fixed and an unused variable removed; no criterion touched),
bb8n_lip.py and bb8w_nf.py after it). Runner scratchpad bb8/run_bb8.sh (lock `until mkdir …/locks/numeric`, load1 < 8 wait, nice 10,
thread variables 1, PYTHONDONTWRITEBYTECODE=1, /usr/bin/time -l, python3 without -I, no `timeout`, no trap, one `rmdir`): one
acquisition 11:21:05-11:21:12 (load1 2.42, memory free 32% before and after). Then, written after bb8n ran: checks/bb8n_defect_criteria.md
and bb8n_defect.py (born 11:25:00, criteria first, prediction written before the run), run bb8/run_bb8b.sh, one acquisition
11:25:12-11:25:13 (load1 2.89, memory free 37% → 33%). No process left; no __pycache__.
- **bb8t: ALL PASS (T0-T6, C1, C2).** 5.5 s, 650 MB. Numbers in 25.1-25.2.
- **bb8n: NOT ALL PASS (L-a, L-b, C PASS; L-c FAIL).** 1.7 s, 176 MB. L-c's scaling clause compared round-off: the root-row defect is
  identically 0 (Theorem N2-loc (c) with C_d = 0, 25.3; post-proof correction (3)); the pre-stated expectation of a nonzero
  second-order defect was wrong, the criterion was not retuned.
- **bb8n_defect (informational probe): D-a PASS** (max own|d_j| ≤ 8.9e-17). 1.0 s, 152 MB.
- **bb8w: ALL PASS (W0, W1).** 0.1 s compute, 66 MB. Numbers in 25.4.
- *Reading (measured only).* In d = 4 the box-Neumann adjoint costs exactly the predicted n-power: point-charge ℓ¹ norms ≈ 10.6n, the
  sup of the pinned part ≈ |N_X|/8, the adjacent dipole grows like 2.6·log₂-increments (log n). The framed DD8 chain's covariant
  curvature is Lipschitz with a depth-convergent constant, its root rows reproduce the coarse links exactly, and the d = 2 nonlinear
  box normal form has n-independent interior C^{1,α} proxies. Not measured: d = 4 nonabelian normal forms, Z^off's level-j C^{1,α}
  sizes, lane A's composite response to Γ_E^TD(j).

| Item (session 8) | Status | Note |
|---|---|---|
| Fixes of REVIEW_BFT_B_S7 (RS7-1..RS7-8) | applied, tagged [RBB7-fix] | forward references disclosed; e^{20m} restored; N1G step (2) replaced (Metzler); log on the injectivity ball / r_2 < π; local forms; T ≥ 5 and hypercubic note; CL-clu smallness explicit; cocycle convention; K10, bb7n, bb7c, C.4 notes |
| **Lemma GE-T (for lane A)** | **PROVEN-HERE** ((a)-(f); (c), (e) in d = 4); sharper bulk sup ARGUED (given BA-7) | Γ_E^T = box-Neumann adjoint: ℓ¹ ≤ 2M_n = 4(4n + 1) (n-power 1), local (range 3), d*Γ_E^TD = -D + ΣQ_Xδ_{c_X}, root charges |Q_X| ≤ 8L^{3(k-l)}||j||_∞ (exact sum), sup ≤ C(n + L^{3(k-l)})||j||_∞; dual sup-data bound ||Λ(x)||_∞ ≤ 20||x^c_0||_∞ |
| Remark GE-T' | ARGUED; comparison OPEN | operator-norm route loses log n (box Riesz projection; bb8t C2) |
| **Theorem N2-loc ((N2-bd), local, gauge-invariant)** | **PROVEN-HERE** (constants not evaluated) | local f_j ≤ C_N'ε; covariant Lipschitz curvature [F_j]_{Lip} ≤ C_Hε (all scales ≤ 1, all j, k-uniform); **root-row defects vanish identically** |
| **Theorem N1-loc ((N1-int), local)** | **PROVEN-HERE given LES-div** | nonlinear interior C^{1,α} of the box normal form by curvature sup + covariant Lipschitz; BCH absorbed by distance iteration |
| **Corollary CL-iv** | **PROVEN as an implication** (C^{1,α} terms); residual term: Cg-NL status | **(CovLift) (iv) first clause for Z^off in frames, k-, T-uniform**; levels j ≥ 1 by the exact row recursion |
| Step 4 ((Mult-Y) / GAP 1) | not attempted this session | |
| Failure modes | GE-F1, GE-F2, N2L-F1, N1L-F1, N1L-F2 do not occur; GE-F3 OCCURS (as guessed) | |
| bb8t, bb8w; bb8n; bb8n_defect | ALL PASS; NOT ALL PASS (L-c, criterion assumed a nonzero defect); probe PASS | |

**What (CovLift) rests on now.** (i)-(iii): Z^off on 𝒦(ε), every gauge, T ≥ 5 (session 7, CONFIRMED-WITH-FIX). (iv) first clause:
PROVEN as an implication in frames (Theorems N2-loc, N1-loc given LES-div, NF-ex, CL-clu, CUT), with the 𝔐^∇ residual term at Cg-NL's
status (first order PROVEN, BCH remainder ARGUED). Still OPEN in (iv): the non-residual components of g_Z at θ > 0 (RS5-5). (v):
frames, ARGUED (Remark HOL). Beyond (CovLift), BFT-4's gauge-invariant pieces still need (Mult-Y) (GAP-1 family), (Pair-loc) [ARGUED]
and (I-id)_Z [ARGUED, with the hypercubic symmetrisation note RS7-6 (b)].

## FOR OTHER FILES (session 8; for their owners; not edited)
- **BFT_A (lane A), the requested (GE-T).** Lemma GE-T (§24.1, proof 25.1) is the Γ_E^T lemma REVIEW_BFT_A_S7 Part 4 asks for. For a
  level-l source j: Γ_E^TD(j) is a level-0 1-form within coarse distance 3 of supp j; ||Γ_E^TD(j)||_1 ≤ 4M_n||j||_1 = 8(4n + 1)||j||_1;
  its composite divergence is exactly -D(j) + Σ_XQ_Xδ_{c_X} with Q_X = ⟨d ev χ^5_X, j⟩, |Q_X| ≤ 8L^{3(k-l)}||j||_∞ (d = 4, sharp); in sup,
  ≤ 5^4[(M_n/4)·8||j||_∞ (bulk) + 2^4C_∞·8L^{3(k-l)}||j||_∞ (roots)], and ≤ C·L^{3(k-l)}||j||_∞ given your BA-7.
  The root part is of the order of (PW-i)'s dual target and cannot be dropped. Also: ||Λ(x)||_∞ ≤ 20||x^c_0||_∞ with sup data only (25.1 (d)).
  The ℓ¹ comparison of S_E with the 𝒩-optimal representative is not supplied: the naive operator route loses log n (Remark GE-T', bb8t C2).
- **REVIEW (next lane-B review).** Check first: 25.1 (c) (the reflection count and Lemma N1G's use, d = 4), (e) (the monotonicity
  route to C_∞ ≤ 1.71); 25.3 (b) (one reference frame for p and p'; the case ρ_{j'+1} < δ and its ladder area) and (c) (the exact vanishing
  of the row defect: the axial tree contains the root rows; interpolatory transverse weights); 25.4 (the LES-div form used, the distance
  iteration and its last-scale term); 25.5 (the exact row recursion for levels j ≥ 1; the C^{2,α} of the transition gauges κ_X); bb8n's L-c
  failure and the post-run probe.
- **HIST / SF.** The nonabelian Q_ax-consistency of the framed DD8 chain is exact (row product = coarse link), not only to O(σ²).
