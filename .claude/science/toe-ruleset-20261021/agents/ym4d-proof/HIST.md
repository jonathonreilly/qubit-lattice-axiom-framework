# HIST: lane D of the 4D YM proof push. The effective action at bad cubes (H-pos) and the multi-scale history bookkeeping (HIST) (session 19, 2026-10-27)

Scope. Constructive UV stability of 4D lattice SU(N) Yang-Mills, soft-kernel RG of decision 4 (S4' contour averaging,
normalised soft gauge-covariant kernel; PROOF.md L5 [S9], Lemma D4-norm). This file opens two named hypotheses of
RLARGE.md §8.2: **(H-pos)** and **(HIST)**. It does not edit PROOF.md, RTARGET.md, LOG.md, RLARGE.md, FLOW.md or
agents/ym4d-existence/. Its log is HIST_LOG.md; its checks are checks/h*.

Status words as in PROOF.md: PROVEN-HERE (counted or not, said each time), CONDITIONAL (an implication proven, its
hypotheses named), ARGUED, OPEN, HYPOTHESIS. "Given H" marks every hypothesis a statement consumes. Literature tags:
[read], [read-skim], [read-abs], [not-read]. Balaban CMP 122 (the large-field papers) is [not-read]; nothing here is
attributed to it. Imported items are never load-bearing for a PROVEN-HERE claim.

Inputs read this session (read-only): RLARGE.md in full (§0-§14); REVIEW_S16_S17.md l.350-550 (the inductive-step gaps
G1-G4, fix R-7b, the strategic verdict); PROOF.md by offset: R4D-iso and its 4D cut/positivity paragraph (l.1290-1400),
decision 4 / D4-norm / GT-lat / R4D-lat / BG-sum / W1-size' / (DF) / W1-LD-cond (l.1520-1760), Setting CE / CE-geo /
Lemma TG / Theorem CE (l.1766-1880), CE-geo' (l.2163-2196), LF-count (l.4071-4128); LINEAR_PACKAGE.md §2 (Lemmas 2.2,
2.7, Theorem 2.6); literature/NOTES.md §2-§4, §10 (Dimock II Theorem 3.1 and Remark 3; Dimock III Lemmas 11-13, 20;
Dimock QED Lemma 23; the OSTI abstracts of CMP 122).

File order. §0-§1 were written at **2026-10-27 23:08 UTC**, after reading the inputs and after exploratory reasoning in
this session, and BEFORE any written derivation (§2 onward) and before any h-check criteria file. §0-§1 are not edited
after the derivations start; outcomes are pointers in §10, added afterwards.

**Session 2 of lane D (opened 2026-10-28 00:03 UTC).** Binding input: REVIEW_HIST_S1.md (fixes H-1..H-12, the WRONG
sentence of §2, (D1-c)'s wider reach, the strategic verdict); also read: REVIEW_S18_S19.md l.1-140 (R1 and TS
CONFIRMED-WITH-FIX, F1, F2, G5); FLOW.md §0, §3, §5.1-§5.4, §5.6 (Def F-strip, Lemma F-tree, F-bg, F-ren, F-depth;
read-only); LINEAR_PACKAGE.md §1.2-§1.3, §2 (Lemmas 2.2-2.5, 2.7, Theorem 2.6), §3 (Lemma 3.1, Theorem 3.8); PROOF.md
by offset: Lemma NA-alg (l.2914-2949), A1-NA / Lemma A1-NA(1) / Corollary A1-NA(k) (l.3953-4090); RLARGE.md §8.1-§8.2
(l.566-612). The twelve fixes are applied in place to §2-§12 and tagged **[RH1-fix H-n]**; nothing else in §0-§12 is
changed. Session-2 work is in §13 onward (pre-stated targets in §13, written before §14-§16 and before any h5 file).

---

## 0. Conventions (RLARGE §0, with additions)

- Levels k = 0 (bare) … K; U_k the level-k field on Λ_k; d = 4; L ≥ 3 odd; G = SU(N), N ≥ 2. A level-k **cube** is a
  level-k block (L⁴ level-k sites = one level-(k+1) site); level-k cubes are indexed by level-(k+1) sites, and the
  level-(k+1) cube containing the level-k cube z is **π(z) := ⌊z/L⌋** (componentwise; RLARGE §0 nesting, X ↦ LX + o).
- s(U) := 1 - N⁻¹Re tr U; inequality (B): s(U) = ||1 - U||²_HS/(2N) ≥ ||1 - U||²_op/(2N).
- **The chain measure.** W(U_0, …, U_K) := e^{-S_0(U_0)}Π_{i<K}K_i(U_{i+1}, U_i), S_0 = Wilson at g_0, K_i = Π_c k^{(i)}_c,
  k^{(i)}_c(V, U) = exp(-(κ/g_i²)[1 - N⁻¹Re tr(V⁻¹M̄_c(U))])/𝒩_i(M̄_c(U)) (D4-norm). ∫K_i dU_{i+1} = 1, so
  Z_K = ∫W = ∫e^{-S_k}dU_k for every k, where e^{-S_k} is the level-k marginal of W.
- Small-field indicator χ_Q(U_k) := Π_{p⊂int Q}1{||1 - U_k(p)||_op < ε_1}, ζ_Q := 1 - χ_Q (RLARGE §0).
- Flow hypothesis (F) (RLARGE §0): β_-(k - j)log L ≤ 1/g_j² - 1/g_k² ≤ β_+(k - j)log L, 0 < β_- ≤ β_+.
- RLARGE's names are used unchanged: Proposition CL, Lemma RS, Theorem R1 (with Lemma 7.2-0), Theorem TS, Lemma GT-lat',
  a'', a_♯, n_*, n_♯, (H-ch), (G1), (SF), (PLD), (W1-ret'), (H-Mayer), (H-pos), (HIST), (SF-last), (P1)-(P5).

## 1. Pre-stated targets (2026-10-27 23:08 UTC)

### Target D1: (H-pos), the effective action at bad cubes
Three forms, in decreasing strength; each with all quantifiers.
- **(D1-c) RLARGE's form (§8.2).** For every k ≤ K the representation (I_k) holds on bad level-k cubes too: e^{-S_k} =
  e^{𝒱_k}Σ_𝔥 1_𝔥 exp(-(1/g̃_k²)Σs(U_p) + ΣE_k(X)) ℒ_𝔥 for EVERY U_k, with Σ_{X∋Q}sup|E_k(X)| ≤ E_0 per cube and C³ bounds,
  E_0 independent of g, k, K, T.
- **(D1-b) Pointwise stability (the brief's form).** There are c > 0, C, q, independent of g, k, K, T, such that for every
  level k ≥ 1, every set R of level-k cubes and every level-k configuration U, S_k(U) - inf{S_k(U') : U' = U off int R}
  ≥ (c/g_k²)Σ_{P⊂int R} s(U(P))·1{||1 - U(P)|| ≥ ε_1} - C|R|log(1/g_k), with the soft kernel.
- **(D1-a) Conditional (frozen-activity) form, the form CL and R1 consume.** There are a > 0, C, q independent of g, k,
  K, T such that for every k, every *-connected set Y of level-k cubes and every frozen exterior datum D whose collar
  parameter is small (to be made precise), the frozen activity r_Y(D) := (weight of "all Q ∈ Y bad")/(weight of "all
  Q ∈ Y good"), computed with the exact level-k integrand, obeys r_Y(D) ≤ (Cg_k^{-q}e^{-a/g_k²})^{|Y|}, together with
  CL (d)-(e) (C³ bounds, gauge and B_4 covariance), so that Theorem R1 holds at level k.
- **Routes (both to be tried).** (R-a) the brief's: Wilson positivity at level 0, propagated through soft steps with the
  normalised kernel's positivity, inequality (B), Lemma RS and Dimock's per-level extraction (NOTES §3 Lemma 13, §4
  Lemma 23). (R-b) the review's alternative (REVIEW_S16_S17 fix R-7b): run CL at level k on the joint
  (U_{k-1}, U_k, U_{k+1}) integrand, RS-style, so that no effective action is evaluated at a bad cube.
- **Success:** a PROVEN-HERE statement that RLF-step can use in place of (H-pos) (either D1-a proven at every level, or
  a proof that RLF-step does not need (H-pos)), with constants uniform in k; or, for each of D1-a/b/c not proven, the
  exact wall (a precise statement) with its weight.
- **Failure modes (each a valid named outcome).** (HP-F1) the per-step constants degrade (geometrically in the depth),
  as for E8*-ob; (HP-F2) the bound needs regularity of the large field itself; (HP-F3) the bound needs small-field
  (fluctuation) statements at large fields, where no background exists; (HP-F4) a stated form is false or not
  implied by the inputs.
- **Not success:** a bound whose constants grow with k; a bound at a fixed depth only; a bound for isolated cubes only.

### Target D2: (HIST), the multi-scale history bookkeeping
- **Definitions to give.** A history 𝔥 (which level-k cubes are new unreturned large-field cubes at which level k), its
  nested large-field regions Ω^c_k(𝔥) and small-field regions Λ_k(𝔥) at every level (Λ_{k+1} inside the coarsening of
  Λ_k), the collars, and the admissibility conditions; the RS ordering of RLARGE R-9 (level-(k+1) indicators inserted
  before U_k is integrated) made explicit.
- **Theorem HIST-sum (target).** Name precisely a hypothesis (H-w) on the history weights (per unreturned configuration
  𝒟 at level j: (C_ℓe^{-a/g_j²})^{|𝒟|}; boundary terms ≤ e^{B_0} per cube, as Dimock II (217)-(218) [read]). Prove: for
  every K, every torus T and every coupling sequence obeying (F), with g_K ≤ g_0, Σ_{𝔥≠∅}Z(𝔥) ≤ Z^{sf}(exp(C|T|e^{-(n+1)a/g_K²})
  - 1) for an explicit integer threshold n (g-, K-, T-independent), uniformly in K: the K-level extension of (P1)/(RLF-3).
  The entropy of histories (choice of regions at every level, persistence of the regions to later levels, boundary terms)
  must be counted against e^{-a/g_k²} with g_k flowing logarithmically (LF-count / Lemma LF-n arithmetic).
- **Extensions.** Theorem TS (two scales, frozen) and (P1)-(P5) to K levels, each with its status.
- **Failure modes.** (HI-F1) the collar width (hence the per-level entropy) grows with the cutoff n_c, so that no
  consistent threshold exists; (HI-F2) the per-level entropy is not beaten by the logarithmic flow; (HI-F3) boundary
  terms of nested regions accumulate non-summably over levels; (HI-F4) (P4) is not implied by the bookkeeping alone.
- **Not success:** a two-level statement only; a threshold that depends on K or g; an unstated hypothesis.

### Checks (criteria files first, then scripts)
- **h1** the kernel-maximiser perturbation and the two-sided quadratic bounds of the normalised kernel exponent (SU(2),
  SU(3)), if D1 route (R-b) or (R-a) uses them;
- **h2** a one-step S4' instance (d = 4, L = 3, SU(2)) of any explicit chain configuration used to bound what route (R-a)
  can give;
- **h3** the shadow geometry of nested regions (projection and collar sizes) on explicit *-connected sets in d = 4;
- **h4** the threshold arithmetic (informational).

---
# Derivations (written after §0-§1)

## 2. The exact multi-level structure of the soft chain (definition-level and elementary)

**Lemma TD (top-down normalisation; elementary, not counted).** For every k < K and every bounded measurable F of
(U_0, …, U_{k+1}), ∫W·F = ∫e^{-S_0(U_0)}Π_{i≤k}K_i(U_{i+1}, U_i)·F dU_0⋯dU_{k+1}. Hence, under the probability measure W/Z_K,
the conditional law of U_{k+1} given (U_0, …, U_k) is K_k(·, U_k) = Π_ck^{(k)}_c(·; M̄_c(U_k)): **given U_k, the level-(k+1)
links are independent, link c with density k^{(k)}_c(·; M̄_c(U_k)).**
*Proof.* Integrate U_K, U_{K-1}, …, U_{k+2} in this order; each ∫K_i(U_{i+1}, U_i)dU_{i+1} = 1 (D4-norm). ∎
(With history indicators at levels ≥ k + 2 inserted the conditional law changes; TD is used only for the plain chain
measure, or after those indicators are bounded by 1.)

**The stage-k integrand (definition).** Stage k is the RG step that integrates U_k. In the RS ordering of RLARGE (R-9) the
level-(k+1) large-field indicators are inserted at stage k, before U_k is integrated. All factors of the integrand that
involve level-(k+1) links are then explicit:
  J_k := G_k(U_{≤k}, U_{k+1})·K_k(U_{k+1}, U_k)·K_{k+1}(U_{k+2}, U_{k+1})·F_k(U_{≥k+2}),
where G_k > 0 collects the level-k density e^{-S_k(U_k)} (or, before U_{k-1} is integrated, its unintegrated form) and
every factor produced at earlier stages, and F_k > 0 is everything above level k + 1 (the future). Z_K = ∫J_k. F_k does not
depend on U_{k+1}. ~~G_k depends on U_{k+1} only through factors produced at stage k - 1 near returned level-k defects~~
**[RH1-fix H-1: that sentence was WRONG.]** G_k depends on U_{k+1} **globally**: stage k - 1 rewrites the level-k bad
cubes as Z_∅⟨Ξ^J_{k-1}⟩_cut with Ξ^J_{k-1} = Σ_BΠr^J_{Y_i}, and every r^J_Y (for every cluster Y, good samples included)
reads U_{k+1} on C(Y); every level-(k+1) link has an endpoint block, so Ξ^J_{k-1} depends on all of U_{k+1}. After R1^J
exponentiates it (log Ξ^J_{k-1} = c-number + δβ^J_{k-1}Σs(U_{k-1}) + Σ_xℛ^J_x), the δβ term reads only U_{k-1}, but every
remainder ℛ^J_x, at every cube x, and every re-extracted polymer of (W1-ret'^J)_{k-1} reads U_{k+1} (on C(Y) for the
clusters Y of x's box). The statement holds only for a single term Z_B of the unexponentiated sum, a form the induction
does not keep. Call J_k **explicit near B** (a set of level-(k+1) cubes) if G_k does not depend on the links int(B). After
stage k - 1 this fails for every B; CL^J (a)-(b) apply only after the whole-lattice Mayer expansion (H-Mayer^J)_k of §8,
which writes G_k's U_{k+1}-dependent factor e^{Σ_xρ_x} as a polymer gas of small two-field activities.

## 3. Kernel positivity, sharpened (the normalised kernel near its maximum)

Notation. For M ∈ M_N(C) with ||M||_op ≤ 1 let W_0(M) be a maximiser of W ↦ Re tr(W⁻¹M) on SU(N) (exists by compactness)
and φ_M(V) := N⁻¹[Re tr(W_0⁻¹M) - Re tr(V⁻¹M)] ≥ 0 (independent of the choice of maximiser). Then
  k_c(V; M) = e^{-(κ/g²)φ_M(V)} / ∫e^{-(κ/g²)φ_M}dV  (exactly: the factor e^{-(κ/g²)[1 - N⁻¹Re tr W_0⁻¹M]} cancels with 𝒩). (3.0)

**Lemma PM (maximiser perturbation): PROVEN-HERE [S19-D].** Let S ∈ SU(N), M ∈ M_N(C), ||M - S||_op ≤ δ ≤ δ_0 :=
min{1/(640N), 2/N³}. Then every maximiser satisfies ||W_0(M) - S||_op ≤ 3δ, and ||M - W_0(M)||_op ≤ 4δ.
*Proof.* (1) *Square-root bound.* Re tr(W_0⁻¹M) ≥ Re tr(S⁻¹M), and |Re tr(X(M - S))| ≤ Nδ for unitary X. So
Re tr(W_0⁻¹S) ≥ N - 2Nδ, i.e. s(W_0⁻¹S) ≤ 2δ, and by (B) ||W_0 - S||²_op ≤ 2N·2δ: ||W' - 1||_op ≤ 2√(Nδ), W' := S⁻¹W_0.
(2) *Logarithm.* The eigenvalues e^{iθ_j} of W' (|θ_j| ≤ π) obey |θ_j| ≤ (π/2)|e^{iθ_j} - 1| ≤ π√(Nδ). Since det W' = 1,
Σθ_j ∈ 2πZ, and |Σθ_j| ≤ πN√(Nδ) < 2π because δ < 4/N³. So Σθ_j = 0 and Y := the principal logarithm of W' lies in su(N),
with ||Y||_op = max|θ_j| ≤ π√(Nδ) ≤ 1/8 because δ ≤ 1/(64π²N).
(3) *Stationarity.* For X ∈ su(N), d/dt Re tr((W_0e^{tX})⁻¹M)|_0 = -Re tr(XW_0⁻¹M) = 0. With the real inner product
⟨A, B⟩ = Re tr(A*B) and P the orthogonal projection onto su(N) (P(Z) = (Z - Z*)/2 - N⁻¹tr((Z - Z*)/2)·1, ||P(Z)||_op ≤
2||Z||_op), this says P(W_0⁻¹M) = 0. Write W_0⁻¹M = e^{-Y}(1 + E), E := S⁻¹M - 1, ||E|| ≤ δ, and e^{-Y}(1 + E) = 1 - Y + R,
R := (e^{-Y} - 1 + Y) + e^{-Y}E. P(1) = 0 and P(Y) = Y, so Y = P(R), and ||R|| ≤ (e^{||Y||} - 1 - ||Y||) + δ ≤
½e^{1/8}||Y||² + δ ≤ 0.567||Y||² + δ (e^{-Y} is unitary). Hence ||Y|| ≤ 1.134||Y||² + 2δ ≤ 0.142||Y|| + 2δ, so ||Y|| ≤ 2.34δ.
(4) ||W_0 - S|| = ||e^Y - 1|| ≤ max|θ_j| = ||Y|| ≤ 3δ, and ||M - W_0|| ≤ ||M - S|| + ||S - W_0|| ≤ 4δ. ∎
*Remark.* Step (1) alone gives only 2√(Nδ); RLARGE's Lemma RS compared V with S directly, which costs a LINEAR δ in the
kernel exponent and forces η_1 ∝ ε_1² (RLARGE §11 item 7). PM is what makes the threshold linear (Lemma RS-lin)
**[RH1-fix H-9] for ε_1 ≤ 256Nδ_0 (= 0.4 for N = 2 and for N = 3) only**; above that the ε_1-independent cap δ_0/A_d of
η_q binds.

**Lemma KQ (two-sided quadratic bounds near the maximum): PROVEN-HERE [S19-D] (counted with PM).** Let ||M||_op ≤ 1,
W_0 = W_0(M), x := ||V - W_0||_op. Then
- (lower) φ_M(V) ≥ x²/(2N) - x·||M - W_0||_op;
- (upper) if x ≤ 1/(4N), then φ_M(V) ≤ (π²/4)x² ≤ 2.5x²;
- (global) φ_M(V) ≤ x (D4-norm (2)), so ∫e^{-(κ/g²)φ_M} ≥ e^{-1}c_N(g²/κ)^{N²-1} for g² ≤ κ, and by (3.0)
  e^{-(κ/g²)φ_M(V)} ≤ k_c(V; M) ≤ e c_N^{-1}(κ/g²)^{N²-1}e^{-(κ/g²)φ_M(V)}.                                    (3.1)
*Proof.* Put A := W_0⁻¹M, U := V⁻¹W_0. Then φ = N⁻¹Re tr((1 - U)A) = s(U) + N⁻¹Re tr((1 - U)(A - 1)). (B) gives
s(U) ≥ ||1 - U||²/(2N) = x²/(2N); |N⁻¹tr(XZ)| ≤ ||X||_op||Z||_op, and ||A - 1|| = ||M - W_0||. (Upper) V = W_0e^X with X the
principal logarithm of W_0⁻¹V; its eigen-angles are ≤ (π/2)x ≤ π/(8N), so their sum is 0 and X ∈ su(N), ||X|| ≤ (π/2)x ≤ 1.
Stationarity (PM step 3) kills the first-order term: φ = N⁻¹Re tr((1 - e^{-X} - X)A) ≤ ||1 - e^{-X} - X|| ≤ e^{||X||} - 1 - ||X||
≤ ||X||² (||X|| ≤ 1). (Global) |N⁻¹tr((W_0⁻¹ - V⁻¹)M)| ≤ ||V - W_0||; the Haar ball of radius g²/κ ≤ 1 about W_0 has mass
≥ c_N(g²/κ)^{N²-1} and there φ ≤ g²/κ. ∎

**Lemma RS-lin (one-step re-seeding with a LINEAR threshold; linear for ε_1 ≤ 256Nδ_0 [RH2-fix N-2]): PROVEN-HERE [S19-D].** Setting of Lemma RS (RLARGE §6), step
i → i + 1, A_d := (d - 1)L(L - 1)/2. Put
  **η_q := min{ ε_1/(2L²), ε_1/(256NA_d), δ_0/A_d }.**
Let c be a level-(i+1) link whose two endpoint blocks carry only level-i plaquettes with ||1 - U_i(p)|| < η_q, and δ :=
||M̄_c - S_c|| (≤ A_dη_q by RS (R1)). Then:
- (a) ||W_0(M̄_c) - S_c|| ≤ 3A_dη_q ≤ 3ε_1/(256N);
- (b) on {||V_c - S_c|| ≥ ε_1/8}: k^{(i)}_c(V_c) ≤ e c_N^{-1}(κ/g_i²)^{N²-1}e^{-κε_1²/(1024Ng_i²)};
- (c) (dichotomy, as RS (R3)) if a level-(i+1) plaquette P has ||1 - V_P|| ≥ ε_1 and all level-i plaquettes of U_4(P) are
  < η_q, some c ∈ ∂P has ||V_c - S_c|| ≥ ε_1/8.
*Proof.* (a) PM with δ ≤ A_dη_q ≤ δ_0. (b) x = ||V - W_0|| ≥ ε_1/8 - 3δ ≥ ε_1/16, and ||M̄ - W_0|| ≤ 4δ ≤ 4A_dη_q ≤
ε_1/(64N) ≤ x/(4N). KQ (lower): φ ≥ x(x/(2N) - x/(4N)) = x²/(4N) ≥ ε_1²/(1024N); then (3.1). (c) RS (R2): ||1 - V_P|| ≤ L²η +
Σ_{c∈∂P}||V_c - S_c|| < ε_1/2 + Σ, so Σ > ε_1/2. ∎
*Constants (d = 4, L = 3, A_4 = 9).* η_q = min{ε_1/18, ε_1/(2304N), δ_0/9}. At N = 2, ε_1 = 0.5: η_q = min{0.028, 1.09·10⁻⁴,
8.7·10⁻⁵} = 8.7·10⁻⁵ (RLARGE's η_1 = 2.7·10⁻⁵); for ε_1 → 0, η_q/η_1 = 2/ε_1 (linear vs quadratic). The kernel exponent
is κε_1²/(1024N) (RS: κε_1²/(256N)); the factor 4 is the price of comparing with W_0 instead of S.
**[RH1-fix H-9]** η_q is linear in ε_1 only while ε_1/(256NA_d) ≤ δ_0/A_d, i.e. ε_1 ≤ 256Nδ_0 (0.4 at N = 2, 3). At the
quoted ε_1 = 0.5 the cap δ_0/A_d binds, and the gain over RLARGE there is the factor 3.2 in η (8.7·10⁻⁵ against 2.7·10⁻⁵),
not linearity. The binding exponent of the joint route is the plaquette branch a_η/81 ∝ η_q² (h4); most of h4's 80-fold
reduction of n_♯ comes from c_RS = 81 against 5⁴ = 625, and the rest from η_q² against η_1².

## 4. Proposition CL^J (frozen activities of the JOINT stage-k integrand): PROVEN-HERE [S19-D]

*Setting.* Stage k ≥ 0 (§2), g_k ≤ g_{k+1} ≤ min{1, √κ}. Level-(k+1) cubes Q; int(B) := the level-(k+1) links with both
ends in one cube of B; C(B) := the level-(k+2) links with an endpoint block in B (≤ 8|B|); R_k(Q) := the level-k region of
Q (the L⁴ level-k blocks of the sites of Q, with all level-k links between them; L⁸ level-k sites). A frozen datum D
consists of U_k (all), U_{k+1} on the links outside int(B), and U_{k+2} (all). Put
  w^J_B(U_{int B}; D) := Π_{c∈int B}k^{(k)}_c(U_{k+1}(c); M̄_c(U_k))·Π_{c'∈C(B)}k^{(k+1)}_{c'}(U_{k+2}(c'); M̄_{c'}(U_{k+1})),
  Num^J_B := ∫Π_{Q∈B}ζ_Q w^J_B dU_{int B},  Den^J_B := ∫Π_{Q∈B}χ_Q w^J_B dU_{int B},  r^J_B := Num^J_B/Den^J_B.
No effective action appears: e^{-S_k}, e^{-S_{k+1}} and all earlier-stage factors are either data or absent.
**Quietness.** η_k(Q) := max{||1 - U_k(p)||_op : p a level-k plaquette with all vertices in R_k(Q)}; Q is **quiet** if
η_k(Q) < η_q (§3).
**Joint completion parameter.** For a cluster Y and a choice W_0 = (W_0(M̄_c(U_k)))_{c∈int Y} of maximisers, let Ũ := D's
U_{k+1} off int(Y) and W_0 on int(Y), and
  ε^J_♭(D; Y) := min over the choices of [max_{p⊂N_1(Y)}||1 - Ũ_p||_op + max_{c'∈C(Y)}||U_{k+2}(c') - S_{c'}(Ũ)||_op],
p over the level-(k+1) plaquettes with all vertices in the sites of N_1(Y), S_{c'} the straight level-(k+1) transporter
between the block centres of c' (the maximiser set is compact; the minimum is attained).
*Constants.* n_ℓ := 4L³(L - 1); p_L := 5L - 4; r := min{ε_1/32, 1/(4N)};
  a_J := κε_1²/(2048N),  p_J := (N² - 1)(n_ℓ + 18),  ε^J_loc := ε_1/(157(1 + A_d)√N),  Λ^J_1 := 8κ(2 + C_𝒩),
  C_J := n_ℓ(ec_N^{-1})⁹κ^{9(N²-1)}·[c_Nr^{N²-1}e^{-3κr²}]^{-n_ℓ}·e^{12κp_L²r²}.

*Claims.*
- (a) **Exact Fubini identity.** If J_k is explicit near B, then Z_B := ∫Π_{Q∈B}ζ_QΠ_{Q∉B}χ_Q J_k = Z_∅⟨r^J_B⟩_cut, where
  ⟨·⟩_cut is the probability measure ∝ Π_{all Q}χ_Q J_k and r^J_B is evaluated on the sample's data outside int(B).
- (b) **Factorisation.** If Y_1, …, Y_m are the *-components of B, r^J_B = Π_ir^J_{Y_i}.
- (c) **Size, per cube uniform, any cluster size.** If every Q ∈ Y is quiet and ε^J_♭(D; Y) ≤ ε^J_loc, then
    r^J_Y(D) ≤ (C_Jg_k^{-p_J}e^{-a_J/g_k²})^{|Y|}.
- (d) **Derivatives.** In local Lie coordinates z_1, …, z_q (q ≤ 3) of the data, |∂_{z_1}⋯∂_{z_q}r^J_Y| ≤ B_q(Λ^J_1/g_k²)^q r^J_Y.
- (e) **Invariance.** r^J_Y is invariant under chain gauge transformations (an arbitrary level-k gauge transformation,
  acting on the level-(k+1) and level-(k+2) links through its restriction to block centres), and covariant under
  translations and under B_4 about the centre of any level-(k+1) cube: r^J_{RY}(R·D) = r^J_Y(D).

*Proof.* (a) The factors of J_k involving int(B) links are exactly w^J_B: each level-(k+1) link c enters K_k only through
its own factor k^{(k)}_c; it enters K_{k+1} only through the factors of the level-(k+2) links whose contours contain it,
whose endpoint blocks contain c's endpoints (RLARGE §5 (d), CL-1), i.e. c' ∈ C(B); F_k does not involve level-(k+1) links;
G_k does not involve int(B) (explicit near B). The indicators χ_Q, Q ∉ B, involve only links interior to Q. Then RLARGE's
CL (a) argument verbatim: integrating Π_{all}χ J_k over int(B) gives (Π_{Q∉B}χ_Q)(J_k/w^J_B)Den^J_B, so Z_B =
∫Π_{all}χ_Q J_k·r^J_B = Z_∅⟨r^J_B⟩_cut. Den^J_B > 0 **[RH1-fix H-6]**: on the configuration U_{k+1} ≡ 1 on int(B) every
plaquette interior to a cube of B equals 1 (all its links are interior links), so Π_{Q∈B}χ_Q = 1 on a neighbourhood of it
(the indicators are of open conditions), and the integrand w^J_B is continuous and strictly positive; so Den^J_B > 0 for
every datum D (no quietness needed; the earlier "continuity at the maximisers" was not a proof, since without quietness
the maximisers need not make Q good). ∎
(b) For *-separated Y, Y': int(Y) ∩ int(Y') = ∅; a level-(k+2) link's two endpoint blocks are face-adjacent, so no c' lies in
C(Y) ∩ C(Y'); each k^{(k)}_c involves one integrated link. So w^J_B = Πw^J_{Y_i} in disjoint variables, and the indicators
factorise. ∎
(c) *Numerator.* Let Q ∈ Y. If ζ_Q = 1, some plaquette P interior to Q has ||1 - U_{k+1}(P)|| ≥ ε_1; P's four corners are
sites of Q, so U_4(P) ⊂ R_k(Q) and all its level-k plaquettes are < η_q (quiet). RS-lin (c): some c ∈ ∂P ⊂ int(Q) has
m_c := 1{||U_{k+1}(c) - S_c|| ≥ ε_1/8} = 1. So Π_{Q∈Y}ζ_Q ≤ Π_{Q∈Y}Σ_{c∈int Q}m_c. Bound every factor of C(Y) by its sup,
e c_N^{-1}(κ/g_{k+1}²)^{N²-1} ≤ e c_N^{-1}(κ/g_k²)^{N²-1} ((3.1); g_k ≤ g_{k+1}). Expand the product over the choices (c_Q):
the int(Y) links then appear only through Π_ck^{(k)}_c, a product of probability densities in distinct variables, so each
choice integrates to Π_Q∫m_{c_Q}k^{(k)}_{c_Q} ≤ Π_Q e c_N^{-1}(κ/g_k²)^{N²-1}e^{-κε_1²/(1024Ng_k²)} (RS-lin (b); every c ∈ int Q has
both endpoint blocks in R_k(Q)). With |C(Y)| ≤ 8|Y| and n_ℓ choices per cube:
  Num^J_Y ≤ [n_ℓ(ec_N^{-1})⁹(κ/g_k²)^{9(N²-1)}e^{-κε_1²/(1024Ng_k²)}]^{|Y|}.
*Denominator.* Fix W_0 attaining ε° := ε^J_♭(D; Y) ≤ ε^J_loc, and the caps 𝒞 := {||U_{k+1}(c) - W_0(c)|| ≤ rg_k, c ∈ int Y}.
On 𝒞: (i) every χ_Q = 1: for P interior to Q, ||1 - U_{k+1}(P)|| ≤ ||1 - S_P|| + Σ_{c∈∂P}(||U(c) - W_0(c)|| + ||W_0(c) - S_c||) ≤
L²η_q + 4rg_k + 12A_dη_q ≤ ε_1/2 + ε_1/8 + 3ε_1/128 < ε_1 (RS (R2), RS-lin (a)). (ii) k^{(k)}_c ≥ e^{-(κ/g_k²)φ} ≥ e^{-(κ/g_k²)2.5r²g_k²}
≥ e^{-3κr²} ((3.1), KQ (upper); rg_k ≤ 1/(4N)). (iii) For c' ∈ C(Y), by 𝒩 ≤ 1 and the linearity remark of D4-norm,
k^{(k+1)}_{c'} ≥ exp(-(κ/g_{k+1}²)·mean_{σ,y}½||U_{k+2}(c') - T^σ_y(U)||²); and ||U_{k+2}(c') - T^σ_y(U)|| ≤ ||U_{k+2}(c') - S_{c'}(Ũ)|| +
||S_{c'}(Ũ) - T^σ_y(Ũ)|| + ||T^σ_y(Ũ) - T^σ_y(U)|| ≤ ε° + A_dε° + p_Lrg_k (ribbon bound RS (R1) for Ũ, whose plaquettes in the
two endpoint blocks of c' lie in N_1(Y); contours have ≤ p_L links, and U, Ũ differ by ≤ rg_k on int(Y) links). With
(x + y)² ≤ 3(…): exponent ≤ (3κ/2)[(1 + A_d)²ε°²/g_k² + p_L²r²] (g_k ≤ g_{k+1}). (iv) Haar caps: ≥ c_N(rg_k)^{N²-1} per link.
So Den^J_Y ≥ [c_N(rg_k)^{N²-1}e^{-3κr²}]^{n_ℓ|Y|}·exp(-12κ|Y|[(1 + A_d)²ε°²/g_k² + p_L²r²]).
*Ratio.* 12(1 + A_d)²ε°² ≤ 12ε_1²/(157²N) ≤ ε_1²/(2048N), so the exponent per cube is ≥ κε_1²/(1024N) - κε_1²/(2048N) = a_J; the
powers of g_k are g_k^{-18(N²-1)}·g_k^{-(N²-1)n_ℓ} = g_k^{-p_J}. ∎
(d) As RLARGE CL (d) with Λ_1 replaced by Λ^J_1 (no Wilson term): a U_k data link lies in contours of ≤ 8 level-(k+1)
links (CL-1), at most twice per contour, so it enters ≤ 8 factors k^{(k)}_c with first derivative of the exponent ≤ 2κ/g_k²
and of log 𝒩 ≤ κC_𝒩/g_k² (D4-norm (3)); a U_{k+1} data link enters ≤ 8 factors of C(Y) with the same bounds at g_{k+1} ≤ …
(1/g_{k+1}² ≤ 1/g_k²); U_{k+2}(c') enters one factor, ≤ κ/g_{k+1}². The indicators do not depend on D; derivatives of the
ratio of two positive integrals with D-independent indicators are joint cumulants of bounded variables (R4D-iso step 3). ∎
(e) A chain gauge transformation h changes M̄_c(U_k) → h(x_c)M̄_ch(y_c)⁻¹ (D4-norm's covariance) and the level-(k+1)/(k+2)
links accordingly; change variables U_{int Y} → h·U_{int Y} (Haar invariance); the indicators are gauge invariant. The
lattices are nested with centred blocks (L odd), so B_4 about a level-(k+1) cube centre maps each level's lattice, blocks,
S4' families (L1) and cubes to themselves; RLARGE CL (e). ∎

*Remark (what changed against Proposition CL).* CL integrates the level-j links against e^{-S_j}·K_j and so needs the
level-j action at the bad cube; CL^J integrates the level-(k+1) links against K_k·K_{k+1} with U_k frozen. The positivity
that CL takes from the Wilson term (B) is supplied by the normalised kernel K_k (RS-lin), whose level-(k+1) "action" is
explicit at every level. The non-locality of S_k (its polymers, functions of the frozen U_k) is frozen with U_k, so for
THOSE factors CL^J (b) is exact. **[RH1-fix H-1]** This is false for the U_{k+1}-dependent part of G_k: every stage-(k-1)
remainder ℛ^J_x and every re-extracted polymer of (W1-ret'^J)_{k-1} reads level-(k+1) links, at every cube (§2). So
**RLARGE's gap G1 is reduced, not removed**: it becomes the whole-lattice Mayer expansion of SMALL two-field activities
(H-Mayer^J)_k of §8 (activities ≲ e^{-a''_J/g_{k-1}²} per cube, against RLARGE's O(E_0) polymers), not a step local to
returned defects.

## 5. Theorem R1^J (one stage, frozen) and its region-restricted form: PROVEN-HERE [S19-D]

**Lemma GT-lat'' (multi-level data): PROVEN-HERE (counted with R1^J).** GT-lat' (RLARGE §4) holds verbatim when C is any
finite set of straight lattice segments between sites of B̂ (of any lengths; in R1^J: the level-(k+1) links, length L,
and the level-(k+2) links, length L², in level-k units), with ε_V := max_{c∈C}||log(V_cS_c⁻¹)||_op, S_c the straight
level-k transporter. For (ii), C is B_4-invariant about the box centre.
*Proof.* GT-lat' uses of a coarse link c only: (1) in tree gauge S_c = hol(π_xcπ_{x'}⁻¹), a closed loop in B̂ bounding a
lattice surface of ≤ A(R_0) plaquettes (true for every closed lattice loop in the box, whose 2-complex is simply
connected), hence ||log S_c|| ≤ Cε_2 and the BCH estimates; (2) constant gauge transformations act by Ad on every tree
coordinate; (3) B_4 maps straight segments to straight segments (for (ii)). None uses the length L. ∎

**Theorem R1^J.** RLARGE Theorem R1 (§7.2 (i)-(iv)) holds at every stage k for the gas Ξ^J(D) := Σ_BΠ_ir^J_{Y_i}(D) of
level-(k+1) clusters, with the substitutions:
| R1 (level j, bare form) | R1^J (stage k, joint) |
|---|---|
| integrated level-j links; data D = (level-j links off int B, level-(j+1) links) | integrated level-(k+1) links; data D = (U_k, U_{k+1} off int B, U_{k+2}) |
| Proposition CL (c)-(e); Lemma 7.2-0 | Proposition CL^J (c)-(e); Lemma 7.2-0^J below |
| box radius R_* = (n_c + 2)L (level-j units) | R^J_* := (n_c + 2)L² (level-k units, about level-(k+1) cube centres) |
| (H-ch): ε_2 + ε_V ≤ ε_♮ | (H-ch)^J: ε_2(U_k) + ε_V ≤ ε^J_♮, ε_V over the level-(k+1) and level-(k+2) links of the box |
| GT-lat' | GT-lat'' |
| (G1) with θ = 2(C_rg^{-p_r}e^{-a_1/g²})^{1/16}, a_1 = ε_1²/(4N) - a'' | (G1)^J: θ^J := 2(C_Jg_k^{-p_J}e^{-a^J_1/g_k²})^{1/16} ≤ C_Kc_0(κ)e^{-2κ_1}, a^J_1 := a_J - a''_J, a''_J ∈ (0, a_J) (κ, κ_1 here are Theorem CE's decay parameters, as in RLARGE §7.2, not the kernel constant) |
| n_* = ⌊4/(a''β_-)⌋, cutoff n_c ≥ n_* | n^J_* := ⌊4/(a''_Jβ_-)⌋, cutoff n_c ≥ n^J_* |
| B_x: level-j plaquettes based in block x (6L⁴); δβ_j := (2N/L⁴)c̄_1 | B_x: level-k plaquettes based in R_k(x) (6L⁸); **δβ^J_k := (2N/L⁸)c̄_1, a shift of the level-k Wilson coupling** |
| torus side T_j ≥ W := 2n_c + 5 | T_{k+1} ≥ W (level-(k+1) torus side in cubes) |
Explicitly: under (H-ch)^J on every box and (G1)^J, with N_{k+1} the number of level-(k+1) cubes and T_{k+1} ≥ W,
  log Ξ^J(D) = N_{k+1}c̄^J_0(g_k) + δβ^J_kΣ_ps(U_k(p)) + Σ_xℛ^J_x(D),
  |c̄^J_0| ≤ 2κ_0Bc_0K_0e^{-a''_J/g_k²},  |δβ^J_k| ≤ C^J_*g_k^{-6}e^{-a''_J/g_k²},
  |ℛ^J_x| ≤ C^J_*g_k^{-6}e^{-a''_J/g_k²}𝔯_x(D) + 2κ_0Bc_0K_0e^{-a''_J(n_c+1)/g_k²},
c̄^J_0, δβ^J_k field-independent infinite-volume numbers depending only on (g_k, g_{k+1}, L, N, κ, ε_1, a''_J, n_c); and the
torus-wrap statement (iv) with these constants.
**Lemma 7.2-0^J.** (H-ch)^J on the box of every cube with ε^J_♮ ≤ min{η_q/2, ε^J_loc/C_♭}, C_♭ := L² + 1 + (12 + 3L)A_d,
implies: every Q is quiet, and ε^J_♭(D; Y) ≤ C_♭ε^J_♮ ≤ ε^J_loc for every Y.
*Proof.* ||1 - U_k(p)|| ≤ ||P̂_p|| ≤ ε_2 < η_q. For c ∈ int(Y), RS-lin (a) gives ||W_0(c) - S_c|| ≤ 3A_dε_2; for other level-(k+1)
links ||U_{k+1}(c) - S_c|| ≤ ε_V; so every level-(k+1) link of Ũ in the region is within 3A_d(ε_2 + ε_V) of S_c. RS (R2) for Ũ:
||1 - Ũ_p|| ≤ L²ε_2 + 12A_d(ε_2 + ε_V). For c': S^{(k+1)}_{c'}(Ũ) is the product of the L links of Ũ along c', and the straight
level-k transporter S^{(k)}_{c'} is the product of their S_c; telescoping, ||S^{(k+1)}_{c'}(Ũ) - S^{(k)}_{c'}|| ≤ 3LA_d(ε_2 + ε_V), and
||U_{k+2}(c') - S^{(k)}_{c'}|| ≤ ε_V. Sum. ∎ [As in RLARGE's S18 note, ε^J_♮ must also be small enough (a constant C_♮) that the
whole chart ball of GT-lat'' obeys CL^J (c)'s hypotheses.] **[RH1-fix H-7, = REVIEW_S18_S19 F1 carried over]** Such a
constant exists: on the chart ball, ε^J_♭(·; Y) and the quietness parameter are Lipschitz in the tree coordinates, with a
constant C'(R^J_*) (finitely many links, each a smooth function of the coordinates; ε^J_♭ is a minimum over a compact set of
such functions, hence Lipschitz with the same constant), so C^J_♮ := max{C_♭, C'(R^J_*)C(R^J_*)} works, C(R^J_*) the
chart-ball radius factor of GT-lat''.
*Proof of R1^J.* RLARGE's proof of R1 (i)-(iv) uses of the activities exactly: CL (b) (hard core = disjointness), CL (c) for
every cluster (via Lemma 7.2-0; the grading r' = e^{a''|Y|/g²}r), CL (d) (K_F of GT-lat'), CL (e) (gauge invariance; the
B_4 permutation of the tuple family about x), locality (r_Y depends on D only near Y), the Wilson identification on B_x,
and the Z⁴ embedding for T ≥ W. Each is supplied by the right-hand column: CL^J (b)-(e), Lemma 7.2-0^J, GT-lat''; locality:
r^J_Y depends on D only through U_k on R_k(N_1(Y)), U_{k+1} on N_1(Y) and U_{k+2} on C(Y), all within level-k distance
n_cL² + (L² - 1)/2 + L² < R^J_* of the centre of any x ∈ S when S ∋ x is *-connected with |S| ≤ n_c; the identification
Σ_{p∈B_x}s(U_k(p)) = (L⁸/(2N))Σ_a||Φ_{x,a}||² + O(L⁸(ε_2ε_3 + ε_2³)) (L⁸ base points per plane in R_k(x)); the box spans
2n_c + 5 = W level-(k+1) cubes per direction. The CE step is unchanged (statements about the polynomial P(z) on the
polydisc). ∎
**[RH1-fix H-7] Status of the inherited input.** RLARGE's R1 proof (S18 repair) and Theorem TS are CONFIRMED-WITH-FIX by
REVIEW_S18_S19 (fixes F1, F2, constants-level); F1 is carried over in Lemma 7.2-0^J above. R1^J inherits a reviewed input,
not an unreviewed one.

**Corollary R1_Λ (region-restricted gas, cluster cutoff): PROVEN-HERE (counted with R1^J).** Let Λ' be a set of
level-(k+1) cubes and n_♯ ≥ n_c an integer; let the gas contain only clusters Y ⊂ Λ' with |Y| ≤ n_♯ (activities set to 0
otherwise). Put Λ'^{in} := {x ∈ Λ' : every cube meeting the box of x is in Λ'}. If (H-ch)^J holds on the boxes of all
x ∈ Λ'^{in} and CL^J (c)'s hypotheses hold for every Y ⊂ Λ' (e.g. (H-ch)^J on the box of every cube of Λ'), then
  log Ξ^J_{Λ'} = |Λ'^{in}|c̄^J_0 + δβ^J_kΣ_{p∈B(Λ'^{in})}s(U_k(p)) + Σ_{x∈Λ'^{in}}ℛ^J_x + Σ_{x∈Λ'∖Λ'^{in}}ℛ^∂_x,  |ℛ^∂_x| ≤ 2κ_0Bc_0K_0e^{-a''_J/g_k²},
with the SAME numbers c̄^J_0, δβ^J_k as R1^J. *Proof.* Zero activities are allowed in CE's polydisc, so (i) holds for the
restricted gas. For x ∈ Λ'^{in} every *-connected S ∋ x with |S| ≤ n_c lies in the box ⊂ Λ', and every cluster of a tuple
with support S has size ≤ n_c ≤ n_♯; so 𝓖^{(N)}_S is the unrestricted function and (ii)-(iii) apply verbatim at x. For the
other x put ℛ^∂_x := Σ_NΣ_{S∋x}𝓖^{(N)}_S/|S| (nothing extracted) and bound it by (i). ∎
**[RH1-fix H-7] R1_Λ is the local-hypothesis R1 ("R1-loc") that REVIEW_S18_S19 G5 asks for, in the joint form,** with
Λ' := the cubes whose boxes satisfy (H-ch)^J (a sample-dependent set). A sample-dependent Λ' is harmless: for x ∈ Λ'^{in}
the functions 𝓖_S with S ∋ x, |S| ≤ n_c, do not depend on Λ' (every such S lies in the box of x ⊂ Λ'), and the Taylor step
of R1 (ii)-(iii) acts on the smooth r^J_Y, not on an indicator-truncated activity; the (H-ch)^J indicator is constant on
the chart ball by the C^J_♮ line of Lemma 7.2-0^J. **Cost (stated).** No δβ^J_k is extracted on the extraction collar
(cubes of Λ' ∖ Λ'^{in}) of every collar-bad cube **inside** Λ_{k+1} (these are scattered in the sea with density
e^{-c/g²}), not only near Ω^c: the missing shift costs ≤ (2w_* + 1)⁴·12L⁸|δβ^J_k| per collar-bad cube **[RH2-fix N-1: 12L⁸, not 6L⁸]** (w_* ~ n_c box
half-width in cubes; 6L⁸ level-k plaquettes per cube, each with s ≤ 2), i.e. ≲ C(n_♯)C^J_*g_k^{-6}e^{-a''_J/g_k²} per collar-bad cube (the
review's estimate 10⁵n_♯⁴ for the combinatorial factor), small for g ≤ g_0(n_♯). It is listed with the other costs of
(W1-ret'^J) in §8.

## 6. Outcome D1: what replaces (H-pos)

**Theorem H-pos^J (the frozen R-operation at every effective level without an effective action at bad cubes):
PROVEN-HERE [S19-D] (corollary of CL^J and R1^J; not counted separately).** For every stage k ≥ 0 with g_k ≤ g_{k+1} ≤
min{1, √κ}:
- (i) the level-(k+1) R-operation is an exact rewriting of the stage-k integrand (CL^J (a)-(b)), and its frozen activities
  obey CL^J (c)-(e) with constants (C_J, p_J, a_J, Λ^J_1) independent of k, K, T and g: **form (D1-a) holds at every level,
  in the joint form**;
- (ii) under (H-ch)^J and (G1)^J, Theorem R1^J (and R1_Λ) holds at stage k with stage-independent constants;
- (iii) neither uses S_{k+1}, nor S_k anywhere except as the weight of the frozen datum U_k, which under the cut measure is a
  level-k small-field configuration (every level-k cube of Λ_k is good, the bad ones having been rewritten at stage k - 1).
  After the stage-k rewriting the cut measure has χ_Q = 1 on every level-(k+1) cube outside the history, so integrating
  U_k is needed ONLY on the level-(k+1) small-field domain. **[RH1-fix H-3: wording]** It does not produce a function
  e^{-S_{k+1}(U_{k+1})} there: after stage k the integrand carries ℛ^J and re-extracted polymers in (U_k, U_{k+1}, U_{k+2}),
  so integrating U_k produces a JOINT density of (U_{k+1}, U_{k+2}) on Λ_{k+1}. The small-field step needed is
  **(SF^J)_k: integrate U_k against a level-k density with polymers in three levels (U_k, U_{k+1}, U_{k+2}) and output
  two-field polymers in (U_{k+1}, U_{k+2})** (named in §8). In Balaban/Dimock this is routine for fine-coarse polymers
  [inference; not-read for the YM case], but RLARGE's (SF)_k is stated for a level-k density only.
**Consequence for RLARGE's induction (a proposal for the lead; RLARGE.md is not edited here).** In Proposition RLF-step,
(I_k) is needed only on Λ_k, and **[RH1-fix H-10] (H-pos)_k is not needed by CL^J/R1^J; its content is RELOCATED, not
removed** — the large-field cost of level-(k+1) defects is now carried by the kernel (RS-lin, CL^J (c): proven), by
(PLD-q)_k [s given SF], by (W1-ret'^J)(c) [s to P] and by (H-w) [P] — provided: the level-(k+1) R-operation is run at
stage k on J_k (the RS ordering), the cutoff and threshold are those of §7, and the following are accepted as the costs:
- the coupling shift δβ^J_k multiplies the LEVEL-k Wilson action (it is added before U_k is integrated); **[RH1-fix H-2]**
  against the chain-energy main term of (I_k^E) (§13-§14) it is read as δβ^J_k·𝓔_k(U_k) + δβ^J_k(Σs - 𝓔_k), a coupling
  shift plus a small polymer (§14.3);
- the returned remainders are polymers in (U_k, U_{k+1}, U_{k+2}) **[RH1-fix H-1] at every cube, not only near returned
  defects** (after U_k is integrated: in (U_{k+1}, U_{k+2}), via (SF^J)_k);
- non-quiet level-(k+1) cubes (a level-k plaquette in [η_q, ε_1) below them) violate (H-ch)^J (ε_2 ≥ η_q > ε^J_♮), so they are
  collar-bad cubes in RLARGE §1A's sense; they are priced in the sea by (PLD)_k (i) at threshold η_q (Lemma RS-joint, §7)
  and returned or not through (W1-ret'), exactly as RLARGE's collar-bad cubes;
- the stage-(k-1) factors that depend on level-(k+1) links need a Mayer step, (H-Mayer^J) (§8), which replaces RLARGE's
  (H-Mayer). **[RH1-fix H-1]** These factors are ALL stage-(k-1) remainders and re-extracted polymers that read level-(k+1)
  links, at every cube of the lattice, so (H-Mayer^J) is a whole-lattice Mayer expansion; it is weaker than RLARGE's
  (H-Mayer) only in that its activities are small (≲ e^{-a''_J/g_{k-1}²} per cube), not O(E_0);
- the extraction-collar cost of R1_Λ around collar-bad cubes inside Λ_{k+1} (§5, [RH1-fix H-7]).

**Proposition CF (constant-curvature chain: the ceiling of route (R-a)): PROVEN-HERE [S19-D] (not counted; it bounds a
method).** d = 4, L ≥ 3 odd, SU(2) (any SU(N) via the block embedding), on Z⁴. Fix k ≥ 1 and θ ∈ (0, π/6]. Let U_0 be the
abelian constant-curvature field U_0(x, 1) = e^{-iF_0x_2σ_3/2}, U_0(x, 2) = e^{iF_0x_1σ_3/2}, U_0(x, 3) = U_0(x, 4) = 1, F_0 :=
θL^{-2k}, and U_{i+1}(c) := W_0(M̄_c(U_i)) for i < k (the kernel's maximiser on every coarse link). Then for every i ≤ k:
- (1) for every level-(i+1) link c, M̄_c(U_i) = m_{i,c}S_c(U_i) with m_{i,c} ∈ (0, 1], so W_0 = S_c(U_i) uniquely and the
  normalised kernel exponent φ vanishes on every link at every step (each k^{(i)}_c is at its maximum);
- (2) U_i is a constant-curvature abelian field with (1,2)-plaquette e^{iθL^{-2(k-i)}σ_3} (other planes 1), up to constant
  flat phases; hence ||1 - U_i(p)||_op ≤ θL^{-2(k-i)} for i < k, while ||1 - U_k(P)||_op = 2sin(θ/2) =: ε (ε ≤ 0.52);
- (3) its bare Wilson action per level-k site is L^{4k}(1 - cos(θL^{-2k})) ∈ [θ²/2 - θ⁴L^{-4k}/24, θ²/2].
*Proof.* (1) For constant curvature F in the (1,2)-planes, a closed lattice loop has holonomy e^{iFA_{12}σ_3}, A_{12} the
signed area of its projection onto the (1,2)-plane (Stokes; abelian). T^σ_yS_c⁻¹ is the holonomy of the RS ribbon loop
(RLARGE §6 (R1) proof), whose |A_{12}| ≤ A_d(L) (≤ (d - 1)(L - 1)/2 off-axis steps, each a 1 × L rectangle). If c is along e_3
or e_4, γ and γ + Le_μ have the same (1,2)-projection, traversed oppositely, so A_{12} = 0 and T = S_c. If c is along e_1
(e_2 alike), the reflection x_2 ↦ 2(c_X)_2 - x_2 maps B(X), c and the S4' family of c to themselves (the order σ is
unchanged; L1) and reverses (1,2)-orientation: it pairs (σ, y) with (σ, y') and A ↦ -A. So M̄_c = mean(e^{iFAσ_3})S_c =
mean(cos FA)·S_c, and |F|A_d(L) ≤ θL^{-2}·(3/2)L(L - 1) < 3θ/2 ≤ π/4 for i ≤ k - 1 gives m ∈ (0, 1]. Re tr(W⁻¹mS) = m Re tr(W⁻¹S) ≤ 2m
with equality iff W = S. (2) Straight transporters from LX + o along e_1: Π_{t<L}e^{-iF(LX_2 + o)σ_3/2} = e^{-i(L²F)X_2σ_3/2}e^{-iFLoσ_3/2};
along e_2 similarly; along e_3, e_4: 1. So U_{i+1} is the symmetric-gauge field of curvature L²F times constant phases per
direction, which cancel in every closed loop; (1) applies again at level i + 1. Induct. 2 sin(t/2) ≤ t. (3) There are
L^{4k} level-0 sites per level-k site, each with one (1,2)-plaquette of angle θL^{-2k}; 1 - cos t ∈ [t²/2 - t⁴/24, t²/2]. ∎
**Reading.** A level-k plaquette of size ε arises with zero kernel mismatch at every step and with every finer plaquette
≤ 1.05εL^{-2(k-j)} (θ ≤ 1.05ε), while the configuration costs ≈ θ²/(2g_0²) per level-k site in the bare action. Any bound
that prices "U_k(P) bad" through kernel mismatches and sup-thresholds t_j of level-j plaquettes therefore needs
t_j ≤ 1.05εL^{-2(k-j)}, and its Peierls exponent t_j²/g_j² ≤ 1.1ε²L^{-4(k-j)}(1/g_k² + β_+(k - j)log L) → 0 as k - j → ∞: **route
(R-a) meets (HP-F1) beyond depth O(log(1/g_k)/log L)** (the depth E8*-ob found for E8*). **[RH1-fix H-8: scope]** This
holds for bounds that price a bad level-k plaquette through O(1) kernel mismatches or O(1) level-j plaquettes per level
above sup-thresholds t_j, i.e. for the sup-threshold (iterated-dichotomy) form of (R-a). It does NOT exclude bounds that
aggregate ≳ L^{4(k-j)} level-j plaquettes per level (many-plaquette Peierls counts, action sums): for those the CF cost
L^{4(k-j)}t_j²/g_j² ≈ θ²/g_j² does not decay, so CF's cost is visible to them; Dimock-style per-level extraction uses
action sums and is not covered by this reading. Proposition CF is also the explicit reason why RS must never be iterated
(RLARGE §6).

**Wall for (D1-b): (CLS-NA), classical large-field stability of the chain energy [OPEN; P].** Tree-level chain energy
E_k(U_k) := inf_{U_0,…,U_{k-1}}[Σ_ps(U_0(p)) + κΣ_{i<k}Σ_cφ_{M̄_c(U_i)}(U_{i+1}(c))] (couplings equalised). (CLS-NA): there are
c_cl, s_1 > 0, independent of k, such that E_k(U_k) ≥ c_clΣ_{P∈𝒫}min{s(U_k(P)), s_1} for every set 𝒫 of level-k plaquettes with
pairwise disjoint shadows. **[RH1-fix H-11: "shadow" defined]** Here the shadow is DOWNWARD (not §7.1's upward Σ): the
**footprint** of a level-k plaquette P is ft(P) := the set of level-0 sites in the level-0 descendants of P's four
corner sites, enlarged by a level-0 collar of width 1 (i.e. W_P^{(0)} of §15.1 with a 1-collar; the level-0 descendants of every
W_P^{(i)}, i < k, equal W_P^{(0)} **[RH2-fix N-3]**); "pairwise disjoint shadows" means pairwise disjoint footprints. **Its linear
abelian case is PROVEN:** LINEAR_PACKAGE Lemma 2.7 (E-low), E_k(B_k) ≥ c_E||dB_k||²
uniformly in k and T [read]. The non-abelian large-field case is open: the abelian proof averages fluxes linearly, and for
large SU(N) fields the polar part of an average of transporters is not controlled by the average of the transporters'
deviations (the obstruction is the nonlinearity of M̄ ↦ W_0(M̄) far from S, where Lemma PM does not apply). (D1-b) needs
(CLS-NA) together with a bound on the fluctuation integral around large-field configurations, where no background field
exists (HP-F3). [Laplace link, ARGUED: at fixed k, g²(S_k(U) - S_k(U')) → E_k(U) - E_k(U') as g → 0, since the 𝒩 and
Haar-cap factors are O(log(1/g)).] **Status of (D1-b): OPEN [P]; not needed by RLF-step (Theorem H-pos^J).**

**(D1-c), RLARGE's (H-pos) in per-cube-bounded form: ARGUED to be false at tree level (HP-F4).** If (I_k) held for every U_k
with Σ_{X∋Q}sup|E_k(X)| ≤ E_0 per cube, then by the Laplace link g²(S_k(U) - S_k(1)) → λΣ_Ps(U(P)) on every configuration
supported in a fixed region, i.e. E_k(U) = λΣ_Ps(U(P)) for all U (λ := lim g²/g̃_k², the same for all U). At U = e^{itB}
(t → 0) this forces the linearised chain energy to be λ||dB||²/2 (up to normalisation): a multiple of ||dB_k||². It is not:
c31 E2 (LINEAR_PACKAGE Lemma 2.7's check, [read: checks/c31E.out]) gives E_1/||dB_1||² = 0.0574, 0.0585, 0.0582 on three random
data and 0.0408 on a single mode (T = 3, κ = 1). With t of order ε_1 (a bad cube) and g → 0 the mismatch is ≍ t²/g² per
cube, unbounded. **So (H-pos) as written in RLARGE §8.2 should be replaced, not proven;** Theorem H-pos^J replaces it.
~~[inference, for the SF lane, not acted on] The same computation at fields of size g …~~ **[RH1-fix H-2: the argument
reaches further, and is acted on.]** The configurations e^{itB} with g ≪ t < ε_1 are SMALL-FIELD (every plaquette < ε_1).
On them the mismatch between the coarse Wilson action and the chain energy is ≍ t²/g² per cube, unbounded on RLARGE's
g-independent ε_1-domain. Hence, by the same Laplace-link argument (ARGUED):
- **(I_k) on Λ_k in RLARGE §8.1's form** (main term (1/g̃_k²)Σs(U_p) + polymers with a g-independent per-cube bound) is
  ARGUED FALSE as well; RLF-step^J step 5 and H-pos^J (iii) assumed it;
- the per-cube bound Σ_{X∋x}|E_m(X)| ≤ E_0 that §7.5 (P4) and §7.4 (H-w)(b) consumed, read for the coarse-Wilson form,
  is the same object and falls with it.
- **Named requirement (I_k^E)** (stated precisely in §14): on Λ_k the main term of (I_k)/(SF)_k is the soft-chain classical
  energy, u_k𝓔_k(U_k) (𝓔_k := E_k above, with β[𝓔_k] = 1 by FLOW Lemma F-tree, §14.2), plus polymers bounded per cube in a
  background-field norm, as in Balaban's and Dimock's effective actions [inference for the YM case]. Two layers replace
  RLARGE's per-cube form: for the R-operation, CL^J/R1^J (no action at bad cubes is needed); for the representation,
  (I_k^E). (P4) and (H-w)(b) are re-based on (I_k^E) (§7.4-§7.5), and the "one coupling shift" reading of (RLF-0) is
  restated against 𝓔_k (§14.3).

## 7. Target D2: the multi-scale history

### 7.1 Definitions
- **Projection, collar, shadow.** For a set A of level-k cubes: π(A) := {π(z) : z ∈ A} (level-(k+1) cubes); N_ρ(A) := the
  cubes at sup-distance ≤ ρ from A; **Σ(A) := N_1(π(A))** (the one-step shadow: projection plus a collar of width 1). For
  a level-j set A and m ≥ 0, sh_{j+m}(A) := Σ^m(A). Σ distributes over unions (π and N_1 do).
- **History.** 𝔥 = (𝒰_0, …, 𝒰_{K-1}), 𝒰_k a set of level-k cubes (the NEW unreturned large-field cubes of level k). With
  Ω^c_{-1} := ∅ and, for k ≥ 0,
    Ω^c_k(𝔥) := ∪_{j≤k}sh_k(𝒰_j)  (the level-k large-field region),  Λ_k(𝔥) := all level-k cubes ∖ Ω^c_k (small-field region),
  𝔥 is **admissible** if (A1) every *-component of 𝒰_k has more than n_♯ cubes, and (A2) 𝒰_k ∩ Σ(Ω^c_{k-1}) = ∅ (new regions
  arise only in the current small-field region). 𝒰_k is decided at stage k - 1 (by the level-k R-operation on J_{k-1};
  𝒰_0 by the bare R1 of RLARGE §7.2, whose level-0 action is Wilson's).
- **Returned configurations are not part of the history:** at each stage the components with ≤ n_♯ cubes inside
  Λ^{pre}_{k+1} := all level-(k+1) cubes ∖ Σ(Ω^c_k), *-separated from 𝒰_{k+1}, form the gas of R1_Λ (§5) and are exponentiated.
  **[RH1-fix H-11]** Small defect configurations touching Σ(Ω^c_k) read collar data (level-k data under N_1(Y)) that were
  never R-operated; if those data are bad, the configurations are collar-bad and go to (W1-ret'^J) (two thresholds, as in
  RLARGE §1A).
- **RS ordering (RLARGE R-9), made explicit.** Stage k inserts the level-(k+1) indicators into J_k, decides 𝒰_{k+1}, runs
  the level-(k+1) R-operation on J_k (§4-§5), and only then integrates U_k (the small-field step, (SF)_k).

**Lemma H-nest (nesting; elementary, counted with H-geo).** (i) Σ(Ω^c_k) ⊂ Ω^c_{k+1}; equivalently the small-field regions
decrease: if Q ∈ Λ_{k+1} then N_1(Q) ∩ π(Ω^c_k) = ∅. (ii) **Collar property.** If Y ⊂ Λ_{k+1} then every level-k cube under
N_1(Y) lies in Λ_k: every level-k datum that a stage-k activity r^J_Y reads (CL^J: U_k on R_k(N_1(Y))) lies over the
level-k small-field region. (iii) **Columns.** For a level-i cube x, {m ≥ i : π^{m-i}(x) ∈ Λ_m} is an interval [i, m(x)]
(possibly empty).
*Proof.* (i) Ω^c_{k+1} ⊇ ∪_{j≤k}Σ(sh_k(𝒰_j)) = Σ(Ω^c_k). (ii) Q ∉ Σ(Ω^c_k) = N_1(π(Ω^c_k)) means N_1(Q) ∩ π(Ω^c_k) = ∅; a level-k
cube z under N_1(Y) has π(z) ∈ N_1(Y), so z ∉ Ω^c_k. (iii) If π^{m-i}(x) ∈ Λ_m and π^{m-1-i}(x) ∈ Ω^c_{m-1}, then π^{m-i}(x) ∈
π(Ω^c_{m-1}) ⊂ Σ(Ω^c_{m-1}) ⊂ Ω^c_m, a contradiction. ∎
*Remark (why width 1, not the box width).* CL^J (c) reads data only on N_1(Y) (and below it), so the ACTIVITY collar has
width 1. R1's Taylor extraction reads the box of radius R^J_* ∝ n_c; cubes of Λ_{k+1} whose box meets Ω^c are simply not
extracted (R1_Λ: ℛ^∂_x, bounded by 2κ_0Bc_0K_0e^{-a''_J/g_k²}). **Putting the extraction collar into the shadow would make
the shadow's per-level size grow like n_c⁴, while the threshold n_♯ must beat that size (Theorem HIST-sum): failure mode
(HI-F1) would then be met. It is avoided by separating the two collars.**

### 7.2 Geometry of shadows
**Lemma H-geo: PROVEN-HERE [S19-D].** L ≥ 3. Let 𝒟 be a *-connected set of n level-j cubes and m ≥ 1. Then
- (i) sh_{j+m}(𝒟) ⊂ N_3(π^m(𝒟));
- (ii) |π^m(𝒟)| ≤ min{n, 16 + 32(n - 1)L^{-m}};
- (iii) |sh_{j+m}(𝒟)| ≤ 2401(16 + 32(n - 1)L^{-m});
- (iv) Σ_{m=0}^{M}|sh_{j+m}(𝒟)| ≤ 38417n + 38416M for every M ≥ 0.
*Proof.* (i) Induction on m ≥ 0 for the claim sh_{j+m}(𝒟) ⊂ N_3(π^m𝒟) (m = 0 trivial). For integers u, v,
|⌊u/L⌋ - ⌊v/L⌋| ≤ ⌊|u - v|/L⌋ + 1, so π(N_3(B)) ⊂ N_{⌊3/L⌋+1}(π(B)) ⊂ N_2(π(B)) (L ≥ 3), and N_1(N_2(·)) = N_3(·).
(ii) Put level-j cube z ↔ the closed unit cube z + [-½, ½]⁴; then a level-(j+m) cube Z is the closed box
[L^mZ - ½, L^mZ + L^m - ½]⁴. Join the centres of 𝒟 along a spanning tree of its *-adjacency graph: a connected union τ of
n - 1 segments of Euclidean length ≤ 2 (centre differences in {-1, 0, 1}⁴), through every centre, so τ meets the box of every
cube of π^m(𝒟). Scaled by L^{-m}, the boxes are the closed unit cubes of a translate of Z⁴ and τ has length ≤ 2(n - 1)L^{-m};
Lemma CE-geo' (g1') [PROOF L5 [S11], PROVEN-HERE] in d = 4 (2^d = 16, 2^{d-1}√d = 16; its proof is translation invariant)
gives ≤ 16 + 32(n - 1)L^{-m}. (iii) |N_3(A)| ≤ 7⁴|A|. (iv) The m = 0 term is n; Σ_{m≥1}2401·32(n - 1)L^{-m} =
76832(n - 1)/(L - 1) ≤ 38416(n - 1); and 2401·16 = 38416 per level. ∎
*Reading.* A defect never disappears from the history: its shadow keeps at least one cube at every later level (it is
"persistent"), but its size settles at ≤ 2401·16 cubes per level, independent of n and of the cutoff (Lemma H-geo (iii)).

### 7.3 Joint pricing of the two RS branches (RLARGE's c_RS, ARGUED there)
**Lemma RS-joint: CONDITIONAL [S19-D] (proven ⇐ (PLD-q)_k).** Hypothesis **(PLD-q)_k** (the multi-point (PLD)_k (i) of RLARGE
§8.2 at threshold η_q, under the level-k marginal of the chain measure): for every set 𝒫 of level-k plaquettes with
pairwise disjoint 1-neighbourhoods, P(||1 - U_k(p)||_op ≥ η_q ∀p ∈ 𝒫) ≤ (C_ηe^{-a_η/g_k²})^{|𝒫|}. Then, under W/Z_K, for every finite
set A of level-(k+1) cubes, with m_k := 6L⁸ and ε_ker := e c_N^{-1}(κ/g_k²)^{N²-1}e^{-κε_1²/(1024Ng_k²)},
  P(ζ_Q = 1 ∀Q ∈ A) ≤ ε_RS^{|A|},  ε_RS := n_ℓε_ker + (m_kC_ηe^{-a_η/g_k²})^{1/81}  (when m_kC_ηe^{-a_η/g_k²} ≤ 1).
So the RS-generated level-(k+1) defects cost **exponent ≥ min{κε_1²/(1024N), a_η/81} per cube: c_RS = 81** (RLARGE §7.1 had
c_RS = 5⁴, ARGUED).
*Proof.* ζ_Q ≤ q_Qζ_Q + (1 - q_Q), q_Q the quietness indicator of Q (a function of U_k). Expand Π_{Q∈A}: a sum over splits
A = A_1 ⊔ A_2 of E[Π_{A_2}(1 - q_Q)·Π_{A_1}q_Q·P(ζ_Q = 1 ∀Q ∈ A_1 | U_{≤k})] (Lemma TD). On q_Q = 1, ζ_Q ≤ Σ_{c∈int Q}m_c (RS-lin
(c)); the links of distinct Q are distinct and, given U_k, independent with densities k^{(k)}_c (TD); so the conditional
probability is ≤ (n_ℓε_ker)^{|A_1|} (RS-lin (b)). Next, the level-k regions R_k(Q) of two cubes that are not *-adjacent are at
level-k sup-distance ≥ L² + 1 ≥ 10, so plaquettes chosen in them have disjoint 1-neighbourhoods. A greedy choice gives
A'_2 ⊂ A_2, pairwise non-*-adjacent, |A'_2| ≥ |A_2|/81. Bound Π_{A_2}(1 - q_Q) ≤ Π_{A'_2}(1 - q_Q) ≤ Π_{Q∈A'_2}Σ_{p∈R_k(Q)}1{||1 - U_k(p)|| ≥ η_q},
expand (≤ m_k terms per cube), and apply (PLD-q) to each term: ≤ (m_kC_ηe^{-a_η/g_k²})^{|A'_2|} ≤ (m_kC_ηe^{-a_η/g_k²})^{|A_2|/81}. Sum
over splits: (x + y)^{|A|}. ∎
(With history indicators present, (PLD-q) is needed in RLARGE's form, under the all-cut measure of (I_k) on Λ_k; that is
how RLARGE states (PLD).) **[RH1-fix H-4]** The **in-history form** of the lemma is ARGUED, not proven: in the induction
the conditional law of U_{k+1} given U_{≤k} is not K_k(·, U_k) but is tilted by G_k's U_{k+1}-dependent factor e^{Σ_xρ_x}
(§2, H-1). Under (H-Mayer^J)_k the tilt is bounded by e^{Σ|ρ|} ≤ e^{C|A|e^{-a''_J/g²}}-type factors per cube, which is
plausibly harmless (it multiplies ε_RS by 1 + O(e^{-a''_J/g²})), but the step "conditional law of the int(Q) links ≤ e^{Σ|ρ|}
× Π k^{(k)}_c" is not written. The proven statement is the plain-chain-measure one above.

### 7.4 The weight hypothesis and the summation theorem
**Hypothesis (H-w) (the analytic content of the history representation; given H) [P].** There are constants C_ℓ ≥ 1,
B_0 ≥ 0 and a > 0, independent of K, T, the history and of the cutoff n_♯ (for g_K ≤ g_0(n_♯)), and a number Z^{sf}_K > 0
(the small-field reference of RLARGE (RLF-4)), such that Z_K = Σ_{𝔥 admissible}Z(𝔥) with every Z(𝔥) ≥ 0, and for every
admissible 𝔥
  Z(𝔥) ≤ Z^{sf}_K·Π_{j<K}Π_{𝒟 ∈ comp(𝒰_j)}(C_ℓe^{-a/g_j²})^{|𝒟|}·exp(B_0Σ_{k<K}|Ω^c_k(𝔥)|).
(Charging B_0 to every cube of every large-field region at every level, not only to the transition cubes Λ_{k-1} ∖ Λ_k
of Dimock II (218), makes (H-w) WEAKER than the Dimock form; the theorem below needs only this.) Where each factor comes
from, ARGUED (not written; §8): the unreturned weights from (W1-ret')(c) in the joint form (CL^J (c) for quiet,
collar-good cubes, (PLD) for the collar-bad and non-quiet ones, Lemma RS-joint for RS-generated ones, W1-size' to pass
from frozen to sea bounds); the B_0 per cube from (a) the variables above large-field regions, integrated top-down with
∫K dV = 1 (Lemma TD, exact), (b) the small-field polymers that meet Ω^c_k, Σ_{X∩A≠∅}|E_k(X)| ≤ E_0|A| — **[RH1-fix H-2]
re-based: E_k are the polymers of (I_k^E) (§14.1 (b)), the remainder after the chain-energy main term u_k𝓔_k, NOT the
remainder after the coarse Wilson action (which is not per-cube bounded, §6)**, (c) the per-cube normalisation mismatch
with Z^{sf} on Ω^c_k ((SF)'s bulk bound), (d) the unextracted tuple terms ℛ^∂ and the vacuum and coupling-shift
corrections near Ω^c (R1_Λ; ≤ C(n_♯)e^{-a''/g_k²} per cube, ≤ 1 for g ≤ g_0(n_♯)).
**[RH1-fix H-11: fragility of (c)]** Item (c) assumes the per-cube, per-level normalisation mismatch with Z^{sf} is O(1).
For the exact soft chain this is plausible, because ∫K = 1 makes the per-step normalisations trivial; but a log(1/g) per
cube per level here would make c_B g-dependent and n_H infinite (failure mode (HI-F2)). It is the one place where the
g-independence of the threshold is fragile [inference].

**Theorem HIST-sum (the K-level history sum): CONDITIONAL [S19-D] (proven ⇐ (H-w) + (F), lower half).** Assume (H-w) and
1/g_j² - 1/g_K² ≥ β_-(K - j)log L (0 ≤ j ≤ K). Put
  **c_B := 38416B_0/log L,  n_H := ⌊(4 + c_B)/(aβ_-)⌋,  γ_H := (n_H + 1)aβ_- - 4 - c_B > 0,**
and suppose **n_♯ ≥ n_H** and 6400C_ℓe^{38417B_0}e^{-a/g_K²} ≤ ½. Then, for every K and every torus T (N_j = L^{4(K-1-j)}|T|),
  Σ_{𝔥≠∅}Z(𝔥) ≤ Z^{sf}_K·(exp(C_H|T|e^{-(n_♯+1)a/g_K²}) - 1),  C_H := 2·6400^{n_♯}(C_ℓe^{38417B_0})^{n_♯+1}/(1 - L^{-γ_H}),
uniformly in K; and Z(∅) ≤ Z_K ≤ Z^{sf}_K exp(C_H|T|e^{-(n_♯+1)a/g_K²}) (positivity for the lower bound).
*Proof.* (1) *Injectivity.* 𝔥 ↦ the set s(𝔥) := {(j, 𝒟) : 𝒟 a *-component of 𝒰_j} is injective. (2) *Product bound.* By
Σ-distributivity Ω^c_k = ∪_{(j,𝒟)∈s(𝔥), j≤k}sh_k(𝒟), so Σ_k|Ω^c_k| ≤ Σ_{(j,𝒟)}Σ_{k=j}^{K-1}|sh_k(𝒟)| ≤ Σ_{(j,𝒟)}[38417|𝒟| + 38416(K - 1 - j)]
(Lemma H-geo (iv)). Hence Z(𝔥) ≤ Z^{sf}_KΠ_{(j,𝒟)∈s(𝔥)}v(j, 𝒟), v(j, 𝒟) := (C'_ℓe^{-a/g_j²})^{|𝒟|}e^{38416B_0(K-1-j)}, C'_ℓ := C_ℓe^{38417B_0}.
(3) *Drop the constraints.* All v ≥ 0, so summing over ALL finite sets s of pairs (j, 𝒟) (𝒟 *-connected, |𝒟| > n_♯) gives an
upper bound: Σ_𝔥Z(𝔥) ≤ Z^{sf}_KΠ_{(j,𝒟)}(1 + v(j, 𝒟)) ≤ Z^{sf}_K exp(Σ_{(j,𝒟)}v). (4) *Count.* #{𝒟 ∋ □, |𝒟| = n} ≤ 80^{2(n-1)} = 6400^{n-1}
((g3), PROOF L5 [S10]); so Σ_{(j,𝒟)}v ≤ Σ_jN_jΣ_{n>n_♯}6400^{n-1}(C'_ℓ)^ne^{-na/g_j²}e^{38416B_0(K-1-j)}. (5) *Flow.* e^{-na/g_j²} ≤
e^{-na/g_K²}L^{-naβ_-(K-j)} ≤ e^{-na/g_K²}L^{-naβ_-(K-1-j)}. With m := K - 1 - j, the j-sum is |T|Σ_{m≥0}L^{-m(naβ_- - 4 - c_B)} ≤
|T|/(1 - L^{-γ_H}) for every n ≥ n_H + 1, in particular for n > n_♯. (6) *n-sum.* Σ_{n>n_♯}6400^{n-1}(C'_ℓe^{-a/g_K²})^n ≤
(2/6400)(6400C'_ℓe^{-a/g_K²})^{n_♯+1}. (7) Z(∅) is the term 𝔥 = ∅ and every term is ≥ 0. ∎
**Corrections to RLARGE that this forces (reported, RLARGE not edited).**
- **Threshold.** RLARGE §1A item 1 sets n_♯ := ⌊4/(a_♯β_-)⌋. With persistent shadows and boundary factors e^{B_0} per cube,
  the per-level entropy of one unreturned configuration is e^{38416B_0}, independent of n; n_♯ must be ≥ n_H =
  ⌊(4 + 38416B_0/log L)/(a_♯β_-)⌋, which reduces to RLARGE's value when B_0 = 0. This is a finite, g-, K- and
  T-independent integer **only because the collar has width 1 and the shadow size is cutoff-independent** (Lemma H-geo
  (iii); §7.1 Remark). (HI-F1) and (HI-F2) are AVOIDED, with this threshold.
- **(RLF-3)** holds in the form of Theorem HIST-sum (exponent (n_♯ + 1)a, any n_♯ ≥ n_H), given (H-w) and (F).
- **The logarithmic flow is load-bearing.** The persistent per-level factors are beaten only by L^{-naβ_-} per level; with
  β_- = 0 (no running, or the upper half of (F) only) the m-sum diverges for every n. Lemma LF-n's arithmetic is used
  exactly once per (level, configuration) pair.

### 7.5 (P1)-(P5) over K levels
- **(P1) = Theorem HIST-sum** (CONDITIONAL on (H-w), (F)); it supersedes RLARGE (P1), which did not count the persistence of
  the regions (no B_0 term) and so used n_♯ = ⌊4/(a_♯β_-)⌋.
- **(P2) Coupling shifts (arithmetic, PROVEN given the per-stage bounds).** With the joint route, stage k shifts the
  level-k coupling by δβ_k with |δβ_k| ≤ C^J_*g_k^{-6}e^{-a''_J/g_k²} (R1^J; the sea-averaged value under (W1-ret'^J) obeys the
  same form): Σ_k|δβ_k| ≤ C'e^{-a'''/g_K²}/(1 - L^{-a'''β_-}) for every a''' < a''_J, exactly as RLARGE (P2). The extraction
  is done on Λ^{in} only (R1_Λ); the missing shift on the extraction collar is a boundary term ≤ |δβ_k|·12L⁸·#(collar cubes) **[RH2-fix N-1]**,
  ≤ 1 per cube of Ω^c for g ≤ g_0(n_♯), part of B_0 (d) (and, around collar-bad cubes inside Λ_{k+1}, a sea cost listed under
  (W1-ret'^J), [RH1-fix H-7]). **[RH1-fix H-2]** "Coupling shift" is read against the chain-energy main term of (I_k^E):
  δβ_kΣs(U_k) = δβ_k𝓔_k(U_k) + δβ_k(Σs - 𝓔_k); the first is the shift u_k → u_k + δβ_k of the β-functional coupling
  (β[Σs] = β[𝓔_k] = 1), the second is a polymer with β = 0 and per-cube size ≤ |δβ_k|·O(1) (§14.3). The arithmetic above is
  unchanged.
- **(P3) Vacuum (arithmetic, PROVEN).** The field- AND history-independent constant is 𝒱^{LF}_K := Σ_kN_{k+1}c̄_0(g_k) (all
  cubes, all levels); the history-dependent difference -Σ_k#(Ω^c_{k+1} ∪ extraction collar)·c̄_0 is ≤ C(n_♯)e^{-a''/g_k²} ≤ 1 per
  cube of Ω^c, part of B_0 (d). So (RLF-1)'s c-number is unchanged and does not depend on the history.
- **(P4) Consistency of the nesting: [RH1-fix H-2] ARGUED (was "CONDITIONAL"); its naive form FAILS.** The polymer bound it
  consumes, read in the coarse-Wilson form of RLARGE's (SF)/(I_k), is ARGUED false on the ε_1-domain (§6). Its hypothesis is
  re-based below on the polymers of (I_k^E) (§14.1 (b)); whether the re-based implication is promoted is for review.
  **Lemma P4-div (arithmetic, PROVEN-HERE, not counted).** Under the upper half of (F), if the frozen remainders of
  level-k cubes are bounded only by δ_k ≥ ce^{-a/g_k²} per cube (as R1's sea bound |ℛ_x| ≤ C_*g_k^{-4}e^{-a''/g_k²} is), then the
  naive bound on the remainders accumulated under ONE level-m cube, Σ_{k<m}L^{4(m-k)}δ_k ≥ ce^{-a/g_m²}Σ_{n=1}^{m}L^{(4-aβ_+)n},
  diverges as m → ∞ whenever aβ_+ ≤ 4, i.e. for every exponent a ≤ a_♯ in the regime of RLARGE §7.1 (a_♯β ≪ 4).
  *Proof.* 1/g_k² ≤ 1/g_m² + β_+(m - k)log L. ∎ So "remainders inside a later unreturned region cost e^{B_0} per cube"
  (RLARGE (P4)) cannot come from bookkeeping; it holds if the returned remainders are admissible small-field polymers
  ((W1-ret')(b)) contracted by the small-field step, whose polymers E_m obey Σ_{X∋x}|E_m(X)| ≤ E_0 (**[RH1-fix H-2] the
  polymers of (I_m^E), §14.1 (b)**): then the polymers meeting a new region A cost ≤ e^{E_0|A|}, i.e. B_0 ≥ E_0. **(P4) is
  ARGUED (re-based on (I_k^E)(b) and (W1-ret')(b)); (HI-F4) is MET for the bookkeeping-only version** (RLARGE already marks
  (P4) ARGUED).
- **(P5)** unchanged (RLARGE §8.4; arithmetic PROVEN; composition needs (SF-last)).

### 7.6 Theorem TS_K (all levels, frozen exterior): PROVEN-HERE [S19-D], **[RH1-fix H-5] an uncounted corollary** (its new ingredients are H-nest (iii), counted with H-geo, and R1_Λ, counted with R1^J); given TS, which REVIEW_S18_S19 CONFIRMED-WITH-FIX
*Setting.* A frozen admissible history 𝔥 and frozen data at every level, in the frozen model of Theorem TS (RLARGE §7.3:
inner integrands of bare form at each level). **[RH1-fix H-5]** ~~the same proof works with R1^J~~: that is ARGUED only (BG-b
would have to cover the level-(i+2) links); TS_K is stated and proven in the bare form only.
Cutoff n_c ≥ n_*; w_i := C_*g_i^{-6}e^{-a''/g_i²}; box half-width in cubes w_* := ⌈R_*/L⌉ + 1. At each level i, the gas of
R1_Λ on Λ' := Λ_i ∖ N_1(𝒰_i) with cluster cutoff n_♯ ≥ n_c. Assume:
- (R1)_i: (H-ch) and (G1) on the boxes of every cube of Λ_i, and g_i² < a''/3;
- **top cubes:** Δ is a top cube of level m if Δ ∈ Λ_m and either m = K - 1 or π(Δ) ∈ Ω^c_{m+1}; for each top cube Δ, BG-b
  relative to level m on **[RH1-fix H-5] Δ^{in}_{*,n} := the cubes meeting B̂_*(x) for x ∈ 𝒬_n(Δ) ∩ Λ_i^{in}** (TS's (b1),
  (b2) with constants M_2 ≤ ε_TS, M_3). (TS's own Δ_{*,n}, all cubes within R_*/L + 1 of 𝒬_n(Δ), contains large-field cubes
  near Ω^c, where (b1) ε_2 + ε_V ≤ M_2σ_n² cannot hold; TS's proof uses (b1)-(b2) only on the boxes of the extracted x, and
  the overlap count is unchanged.)
*Claim.*
  Σ_iΣ_{x∈Λ_i^{in}}|ℛ_x| ≤ Σ_{m<K}#top_m·C_TS[w_m(3M_2M_3 + M_2³/(1 - L^{-2})) + e^{-a''(n_c+1)/g_m²}/(1 - L^{4-(n_c+1)a''β_-})],
with #top_{K-1} ≤ |T| and #top_m ≤ L⁴|Ω^c_{m+1}| for m < K - 1; and Σ_iΣ_{x∈Λ_i∖Λ_i^{in}}|ℛ^∂_x| ≤ 2κ_0Bc_0K_0Σ_i(2w_* + 1)⁴|Ω^c_i ∪ N_1(𝒰_i)|e^{-a''/g_i²}.
*Proof.* By Lemma H-nest (iii) every x ∈ Λ_i has a unique top ancestor Δ(x) := π^{m(x)-i}(x) (top: either m(x) = K - 1 or
π(Δ(x)) ∉ Λ_{m(x)+1}), and x ∈ 𝒬_{m(x)-i}(Δ(x)). Theorem TS (TS-b) with k - 1 := m and j := 0 bounds the sum over all inner
levels and all x ∈ ∪_n𝒬_n(Δ) of |ℛ_x| by the bracket; its proof bounds each |ℛ_x| separately (R1 (iii)) and sums, so restricting
to x ∈ Λ^{in} only lowers the left side. Top cubes of level m < K - 1 are children of cubes of Ω^c_{m+1} (L⁴ each). A cube
x ∈ Λ_i ∖ Λ_i^{in} has a box meeting Ω^c_i ∪ N_1(𝒰_i), so it lies within w_* cubes of that set; R1_Λ bounds each ℛ^∂_x. ∎
*Reading.* The |T|-extensive part is the top level's, C|T|w_{K-1}(…): the frozen shadow of (RLF-2)'s per-cell summation over
all levels at once. Every other term is attached to the history (≤ C(n_c) per cube of Ω^c, absorbed in B_0 for g small). As
for TS, this is the frozen-background shadow; the fluctuating version is (W1-ret')'s re-extraction (RLARGE §7.2 Reading).

## 8. The inductive step after lanes D1-D2 (a proposal for the lead; RLARGE.md not edited)

**Named hypotheses, restated for the joint route.**
- **(H-Mayer^J)_k [s given (W1-ret'^J)_{k-1}] (replaces RLARGE's (H-Mayer)). [RH1-fix H-1: restated; global.]** Let
  e^{Σ_xρ_x} be G_k's U_{k+1}-dependent factor, where ρ_x := every stage-(k-1) remainder ℛ^J_x (R1^J/R1_Λ) and every
  re-extracted polymer of (W1-ret'^J)_{k-1}, after the stage-(k-1) sea average, that reads level-(k+1) links — at EVERY cube
  x of the lattice (§2). Hypothesis: these are polymer activities ρ(X) in (U_k, U_{k+1}) (two-field), C³ in the data, with
    |ρ(X)| ≤ (Ce^{-a''_J/g_{k-1}²})^{#cubes(X)}e^{-κ'd(X)},  κ' > 3κ_0 + 3,
  so that the Mayer expansion e^{Σρ} = Σ_{families}Π(e^{ρ(X)} - 1) over the WHOLE lattice, jointly with the level-(k+1)
  clusters of CL^J, is a polymer gas of connected unions to which Theorem CE steps 3-4 apply, and the frozen activities of
  its components keep CL^J (c)-(e) up to factors 1 + O(e^{-a''_J/g²}) per cube. It is still weaker than RLARGE's (H-Mayer)
  (small activities against O(E_0) ones), and [s given (W1-ret'^J)] is a fair weight; it is not local to returned defects.
- **(W1-ret'^J)_k [s to P] (RLARGE's (W1-ret') with CL^J's activities).** As RLARGE §8.2, with r_Y replaced by r^J_Y, (H-ch) by
  (H-ch)^J, the sea average taken over U_k under the stage-k cut measure, and the non-quiet cubes counted as collar-bad;
  output: c̄^{J,sea}_0, δβ^{J,sea}_k (a shift of the level-k coupling), returned remainders that are admissible polymers
  in (U_{k+1}, U_{k+2}) after U_k is integrated, and unreturned weights (C_ℓe^{-a_♯/g_k²})^{n(𝒟)}. **[RH1-fix H-7] Costs
  listed:** the missing δβ^J_k on the extraction collars of collar-bad cubes inside Λ_{k+1} (R1_Λ, §5: ≲ C(n_♯)C^J_*g_k^{-6}
  e^{-a''_J/g_k²} per collar-bad cube); the unextracted ℛ^∂ near Ω^c; the non-quiet cubes as collar-bad.
- **(PLD)_k [s given SF]** as RLARGE, including (PLD-q)_k at threshold η_q (Lemma RS-joint); **[RH1-fix H-2]** under the
  measure of (I_k^E), its Peierls exponent at threshold η_q needs the small-field classical stability CLS-sf (§15).
- **(H-w) [P]** (§7.4), in place of the analytic half of RLARGE's (HIST); the combinatorial half is Theorem HIST-sum.
- **[RH1-fix H-3] (SF^J)_k [P, new in kind]:** the small-field step integrating U_k against a level-k density with polymers
  in (U_k, U_{k+1}, U_{k+2}), outputting two-field polymers in (U_{k+1}, U_{k+2}) on Λ_{k+1}, with (SF)_k's bounds.
- **[RH1-fix H-2] (I_k^E) [HYPOTHESIS, new in kind]:** the representation on Λ_k with main term u_k𝓔_k (chain energy),
  §14.1; it replaces the coarse-Wilson form of (I_k) on Λ_k.
- Unchanged: (F) [P], (SF)_k [P×3-4] (now required to output the (I_{k+1}^E) form), (SF-last) [s given SF].
- **Not needed by CL^J/R1^J:** (H-pos)_k; **[RH1-fix H-10]** its content is relocated (§6), not removed; RLARGE's form is
  ARGUED false (§6).

**Proposition RLF-step^J: [RH1-fix H-1, H-3, H-4] ARGUED (was "CONDITIONAL"; a proof sketch with the gaps H-1, H-3, H-4
and the requirement H-2 now NAMED, steps 3, 5, 7 being hypotheses).**
(I_k^E) on Λ_k + (F) + (SF^J)_k + (PLD)_k + (W1-ret'^J)_k + (H-Mayer^J)_k ⇒ (I_{k+1}^E) on Λ_{k+1}; with (H-w) and Theorem
HIST-sum for the assembly over k. Named gaps: **H-1** step 1 needs (H-Mayer^J)_k in the global form above; **H-3** step 5
needs (SF^J)_k (three-level polymers in, two-field polymers out); **H-4** step 4 uses Lemma RS-joint in its in-history
(tilted) form, ARGUED; **H-2** steps 5, 7 use the representation (I_k^E), not RLARGE's coarse-Wilson (I_k).
1. *Exact.* Stage k: insert the level-(k+1) indicators into J_k (RS ordering); the whole-lattice Mayer step of
   (H-Mayer^J)_k for G_k's level-(k+1) dependence [H-1], then CL^J (a)-(b) on the components: ⟨Ξ^J⟩_cut with the joint frozen
   gas, pointwise in the sea sample U_k.
2. *Frozen R-step.* R1_Λ (PROVEN) on the quiet, collar-good part, cutoff n_c = n_♯ ≥ max{n^J_*, n_H}: c-numbers, δβ^J_k on the
   level-k Wilson action, remainders ℛ^J (of order 𝔯 = O(g²) in a sea sample, RLARGE §7.2 Reading), unextracted ℛ^∂ near Ω^c.
3. *Sea average and re-extraction:* (W1-ret'^J)_k (a)-(b), including collar-bad and non-quiet cubes.
4. *Unreturned configurations:* (W1-ret'^J)_k (c); RS-generated defects priced by Lemma RS-joint (⇐ (PLD-q)_k; in-history
   form ARGUED [H-4]).
5. *Small-field step:* (SF^J)_k [H-3] integrates U_k on Λ_k against the (I_k^E) density [H-2] with the shifted coupling
   (read as in §14.3); by Theorem H-pos^J (iii) it is needed only on Λ_{k+1}, and it outputs a two-field density there.
6. *Nesting:* Lemma H-nest (PROVEN); the next stage's activities read only Λ_{k+1} data (collar property).
7. *Assembly over k:* (H-w), then Theorem HIST-sum (CONDITIONAL-proven) gives (RLF-3) with n_♯ ≥ n_H; (P2), (P3) arithmetic;
   (P4) ARGUED (re-based on (I_k^E)(b) and (W1-ret')(b)); (P5) with (SF-last).
**What lane D removed from RLF-step's hypotheses:** the need for (H-pos) in CL/R1 (its content relocated, [RH1-fix H-10]);
the frozen-stage part of (H-Mayer) (G1), the rest REDUCED to (H-Mayer^J) [H-1]; the combinatorial part of (HIST); RLARGE's
ARGUED c_RS (now Lemma RS-joint, c_RS = 81, ⇐ (PLD-q)). **What it added [RH1-fix H-12]:** two hypotheses NEW IN KIND —
(SF^J)_k (the effective densities become two-field) and (I_k^E) (the main term changes from the coarse Wilson action to the
chain energy); (W1-ret'^J) and (H-Mayer^J) as RLARGE's hypotheses with the joint activities ((H-Mayer^J) global); a
corrected threshold n_♯ ≥ n_H.

## 9. Checks h1-h4 (criteria first: checks/h*_criteria.md; scripts checks/h1_kernel_max.py, h2_constfield.py, h3_shadow.py, h4_threshold.py; records checks/h*_time.txt, h*_out.txt)
All four PASS, first and only runs (laptop, one job at a time under the numeric lock, nice 10, BLAS threads 1, load ≤ 3.9,
37-38% free, peak RSS ≤ 42 MB). Disclosures: HIST_LOG.md.
- **h1 (PM, KQ, RS-lin; SU(2), SU(3)): PASS.** P1: max ||W_0 - S||/δ = 1.000 (N = 2), 1.012 (N = 3) against the proven 3; max
  ||M - W_0||/δ ≤ 1.072 against 4. P2 (informational): the ratio stays ≤ 1 up to δ = 0.3, so δ_0 is a property of the proof,
  not of the maximiser. G: no random W beats the computed maximiser. K1-K3 PASS; max φ/x² = 0.50 (N = 2), 0.33 (N = 3) against
  2.5 (≈ 1/N is the true constant). R: min φ·1024N/ε_1² = 15.5 (N = 2), 11.8 (N = 3) against 1: RS-lin (b)'s exponent is
  ≈ 12-16 times conservative. Scope: random and anti-Hermitian-adversarial instances; not a proof of the constants.
- **h2 (Proposition CF, one S4' step, d = 4, L = 3, SU(2)): PASS** for F = 0.01, 0.03, 0.058: M̄_c = m_cS_c to ≤ 4.7·10⁻¹⁵
  (m_c = 0.9997, 0.9973, 0.9899), W_0 = S_c to ≤ 4.7·10⁻¹⁵, φ(S_c) ≤ 2.2·10⁻¹⁶, coarse plaquette = exp(iL²Fσ_3) to ≤ 7.3·10⁻¹⁵,
  transverse contours = S exactly; gauge control ≤ 6.4·10⁻¹⁴; negative control (random 0.02 perturbation) 4.6·10⁻²
  (discriminates). Scope: one step; the induction over levels is the written proof.
- **h3 (Lemma H-geo, H-nest (iii)): PASS** (L = 3, 5; 63 random *-connected sets per L with n ≤ 300, 24 adversarial lines;
  20 random histories). Max |π^m|/(16 + 32(n - 1)L^{-m}) = 0.20; max |sh_m|/bound = 0.0067; **the persistent shadow of one cube
  is 81 cubes at m = 1 and 256 = 4⁴ at every m ≥ 2** (the proven per-level bound 38416 is ≈ 150 times loose; a sharper count,
  not needed, would lower c_B).
- **h4 (threshold arithmetic, informational, [inference] one-loop rate): I1 PASS.** With crude constants a_♯ is limited by
  the plaquette branch a_η/81 (≈ 2·10⁻¹¹ at N = 2, ε_1 = 0.5) and n_♯ ≈ 5·10¹¹ (B_0 = 0) to 4·10¹⁵ (B_0 = 1) on the joint route,
  vs 4·10¹³ to 3·10¹⁷ with RLARGE's RS constants: finite, g- and K-independent, and properties of the bounds.

## 10. Outcomes against the pre-stated targets (§1) (ADDED AFTER the derivations; pointers only)
- **D1 (H-pos).**
  - **(D1-a): MET, in the joint form, at every level, uniformly in k** (Proposition CL^J, Theorem R1^J with R1_Λ; Theorem
    H-pos^J; frozen, under quietness and the ε^J_♭ hypothesis). **[RH1-fix H-10]** The pre-stated success item "a proof
    that RLF-step does not need (H-pos)" is **ARGUED, not met as a proof**: Theorem H-pos^J (iii) plus the RS ordering give
    a sketch with hypotheses and the gaps H-1 (global (H-Mayer^J)), H-3 ((SF^J)), H-4 (in-history RS-joint), and the
    requirement H-2 ((I_k^E)); (H-pos)'s content is relocated to the kernel, (PLD-q), (W1-ret'^J)(c) and (H-w), with the
    costs listed in §6.
  - **(D1-b): NOT MET. OPEN [P].** Route (R-a) (the brief's) was executed as far as it goes: one step is sharp and now has a
    LINEAR threshold (Lemmas PM, KQ, RS-lin; linear for ε_1 ≤ 0.4 only, [RH1-fix H-9]); iterated, its sup-threshold form
    meets (HP-F1) beyond depth O(log(1/g)/log L), and Proposition CF shows this is the method, not the bound (zero kernel
    mismatch at every step, finer plaquettes ≤ 1.05εL^{-2(k-j)}); aggregating bounds are not excluded [RH1-fix H-8]. Exact wall:
    (CLS-NA) (non-abelian large-field classical stability of the chain energy, whose linear abelian case is LINEAR_PACKAGE
    E-low) plus a fluctuation bound at large fields (HP-F3).
  - **(D1-c): (HP-F4), ARGUED false at tree level** (Laplace link + c31 E2's non-constant ratio E_1/||dB_1||²). RLARGE's (H-pos)
    should be replaced (by Theorem H-pos^J), not proven. **[RH1-fix H-2]** The same argument reaches the small-field domain:
    RLARGE's coarse-Wilson (I_k) on Λ_k and the per-cube E_0 consumed by (P4) and (H-w)(b) are ARGUED false in that form;
    replaced by the requirement (I_k^E) (§14).
- **D2 (HIST).**
  - Definitions: MET (§7.1: histories, shadows Σ = N_1∘π, nested regions, admissibility, the RS ordering; Lemma H-nest).
  - **Theorem HIST-sum: MET as a CONDITIONAL theorem** (⇐ (H-w) + the lower half of (F)), uniformly in K, with the explicit
    threshold n_H = ⌊(4 + 38416B_0/log L)/(aβ_-)⌋ and the entropy counted (persistence of every region to level K; ≤ 38416
    shadow cubes per level per region, observed 256 in h3). (HI-F1) AVOIDED by separating the width-1 activity collar from
    the Taylor-extraction collar; (HI-F2) AVOIDED by the logarithmic flow (load-bearing; fails for β_- = 0; fragile at
    (H-w)(c), [RH1-fix H-11]); (HI-F3) AVOIDED (the boundary entropy per level is absorbed into the threshold); **(HI-F4) MET
    for the bookkeeping-only (P4)** (Lemma P4-div), so **[RH1-fix H-2] (P4) is ARGUED** (re-based on (I_k^E)(b) and
    (W1-ret')(b)).
  - Extensions: Theorem TS_K (all levels, frozen, bare form) PROVEN-HERE given TS (CONFIRMED-WITH-FIX in REVIEW_S18_S19), an
    uncounted corollary [RH1-fix H-5]; (P1) = HIST-sum; (P2), (P3) arithmetic PROVEN with the history and extraction-collar
    corrections absorbed into B_0; (P5) unchanged.
  - Not met: the analytic content (H-w) itself (OPEN [P]; decomposed, ARGUED, into (W1-ret'^J)(c), (SF^J), (I_k^E), Lemma TD).
- **Corrections reported to the lead (RLARGE not edited):** n_♯ ≥ n_H (not ⌊4/(a_♯β_-)⌋); (H-pos) not needed by CL/R1, its
  content relocated; (H-Mayer) REDUCED to the global small-activity (H-Mayer^J) [RH1-fix H-1]; c_RS = 81 ⇐ (PLD-q) (was 5⁴,
  ARGUED); (P4) ARGUED; **[RH1-fix H-2] (I_k)'s main term on Λ_k must be the chain energy, (I_k^E), not the coarse Wilson
  action** (no longer "[inference] … if (SF) needs E_k small").

## 11. Lemma DAG and tally of this file (session-1 items, after the [RH1-fix] corrections; session-2 items in §17)
```
D4-norm, RS (R1)(R2) ──► PM ──► KQ ──► RS-lin ──► CL^J ──► Lemma 7.2-0^J ─┐
                                                   │                       ├─► R1^J ──► R1_Λ (= G5's R1-loc) ──► H-pos^J (iii) ──► RLF-step^J [ARGUED: gaps H-1, H-3, H-4; needs (I_k^E)]
GT-lat' ──► GT-lat'' ──────────────────────────────┼───────────────────────┘                                          ▲
Theorem CE, R1 proof [S18; CONFIRMED-WITH-FIX] ────┘                                                                  │
RS-lin + TD + (PLD-q) ──► RS-joint [CONDITIONAL; in-history form ARGUED] ─────────────────────────────────────────────┤
CE-geo' ──► H-geo ◄── H-nest;   H-geo + (g3) + (H-w) + (F)_- ──► HIST-sum [CONDITIONAL] ──► (RLF-3), n_♯ ≥ n_H
TS [S18; CONFIRMED-WITH-FIX] + R1_Λ + H-nest ──► TS_K [uncounted];   (F)_+ ──► P4-div ──► (P4) [ARGUED]
Proposition CF ──► sup-threshold route (R-a) meets (HP-F1);  E-low (linear) ──► (CLS-NA) [OPEN] ──► (D1-b) [OPEN]
```
- **[RH1-fix H-12] Corrected tally of §0-§12 (REVIEW_HIST_S1): 5 PROVEN-HERE / 2 CONDITIONAL / 6 ARGUED / 3 OPEN** (claimed
  in session 1: 6 / 4 / 4 / 3).
- **PROVEN-HERE [S19-D], counted (5):** Lemma PM (with KQ); Lemma RS-lin; Proposition CL^J; Theorem R1^J (with GT-lat'',
  Lemma 7.2-0^J, Corollary R1_Λ); Lemma H-geo (with H-nest). All five CONFIRMED (CL^J, R1^J WITH-FIX) by REVIEW_HIST_S1. R1^J's
  inherited R1 proof is CONFIRMED-WITH-FIX by REVIEW_S18_S19 (the stale "[S18-repair, unreviewed]" label is dropped).
- **PROVEN-HERE, not counted:** Lemma TD (elementary); Proposition CF (bounds a method); Theorem H-pos^J (corollary of CL^J,
  R1^J); **Theorem TS_K (corollary; [RH1-fix H-5])**; Lemma P4-div, (P2), (P3) (arithmetic).
- **CONDITIONAL (implication proven, hypotheses named) (2):** Lemma RS-joint (⇐ (PLD-q), plain chain measure); Theorem
  HIST-sum (⇐ (H-w), (F)_-).
- **ARGUED (6):** (D1-c) false at tree level (broadened to the ε_1-domain, H-2); the Laplace link; the decomposition of (H-w)
  into named hypotheses; (H-Mayer^J) [s] (global form, H-1); (P4) (H-2); Proposition RLF-step^J (gaps H-1, H-3, H-4; H-2).
- **OPEN (named walls) (3):** (CLS-NA) [P]; (D1-b) [P]; (H-w) [P].
- **0 GAP, 0 WRONG among counted items** (REVIEW_HIST_S1); the one WRONG uncounted sentence (§2) is struck through and
  corrected.
- No change is made to the PROOF.md tally; if the lead places these in PROOF.md, the main-path count rises by 5, not 6.

## 12. Hypotheses consumed ("given H"), by statement
- **R1^J, R1_Λ:** (H-ch)^J and (G1)^J on the stated boxes; g_k ≤ g_{k+1} ≤ min{1, √κ}; T_{k+1} ≥ W (else the wrap term). Ledger
  inputs used as proven: D4-norm, Lemma RS (R1)-(R2), Theorem CE with CE-geo' and Lemma TG, GT-lat', RLARGE's R1 proof
  (CONFIRMED-WITH-FIX, REVIEW_S18_S19).
- **CL^J, PM, KQ, RS-lin:** none beyond the stated parameter ranges (quietness and the joint collar are hypotheses of the
  statement, not of the lemma). CL^J (a) needs "J_k explicit near B", which after stage k - 1 holds only after
  (H-Mayer^J)_k [RH1-fix H-1].
- **RS-joint:** (PLD-q)_k (plain chain measure); in-history form additionally the tilt bound of H-4 (ARGUED).
- **HIST-sum:** (H-w); the lower half of (F); n_♯ ≥ n_H; 6400C_ℓe^{38417B_0}e^{-a/g_K²} ≤ ½.
- **TS_K:** TS's hypotheses at every top cube ((b1), (b2) relative to the top level, on Δ^{in}_{*,n} [RH1-fix H-5]), (R1)_i on
  the boxes of Λ_i, the coupling window g_i² < a''/3, n_c ≥ n_*.
- **(P4):** (I_m^E)(b)'s per-cube polymer bound and (W1-ret')(b) [RH1-fix H-2]. **P4-div:** the upper half of (F).
- **Theorem H-pos^J / RLF-step^J:** (F), (SF^J)_k, (I_k^E), (PLD)_k incl. (PLD-q)_k, (W1-ret'^J)_k, (H-Mayer^J)_k (global),
  (H-w), (SF-last).
- **Not load-bearing for any PROVEN-HERE item:** LINEAR_PACKAGE E-low and the c31 E2 numbers (used for the linear case of
  (CLS-NA) and for the ARGUED (D1-c) item only); Dimock II (217)-(218) [read-skim] (the model for (H-w)'s B_0); CMP 122
  [not-read].

---
# Session 2 of lane D (2026-10-28)

## 13. Session-2 pre-stated targets (written 2026-10-28 00:07 UTC, after reading the session-2 inputs and after exploratory reasoning, BEFORE any written session-2 derivation (§14 onward) and before any h5 criteria file or script; not edited after the derivations start)

### Target S2: the chain-energy form (I_k^E)
- **State precisely** the representation of the level-k density on the small-field region Λ_k(𝔥) with main term
  u_k𝓔_k(U_k), u_k := 1/g_k² the β-functional coupling (FLOW Def F-g) and 𝓔_k the soft chain classical energy of the
  block data (tree tower, equalised kernel coupling κ), plus a polymer remainder with stated bounds (per-cube sup bound on
  the ε_1-domain, decay, C³, gauge/B_4 covariance, renormalisation condition), in the two-field form that (SF^J) outputs.
- **Consistency checks (each with its status):** (c1) with FLOW Lemma F-tree (β[𝒯_k] = 1, read-only): the main term's
  coupling is u_k, and HIST's 𝓔_k (φ-form, SU(N) maximiser) and FLOW's 𝒯_k (k̃-form, polar part) are compared exactly;
  (c2) with LINEAR_PACKAGE E-low and N2-E: the quadratic part of 𝓔_k is two-sided equivalent to the coarse Wilson
  quadratic form, uniformly in k; (c3) with (D1-c): the Laplace-link obstruction disappears by construction, and the
  coarse-Wilson mismatch is a β = 0 term of sup size u_k·O(t²), i.e. exactly what may NOT be put into a per-cube-bounded
  polymer; (c4) the coupling-shift reading of R1^J's δβ^J_k against 𝓔_k; (c5) the recursion: the stage-k exponent
  u_k[𝓔_k(U_k) + κΣφ] has tree-level minimum u_k𝓔_{k+1}, so (I_k^E) is self-reproducing at tree level.
- **Success:** a precise hypothesis statement (I_k^E) with every quantifier, the five consistency items each PROVEN,
  ARGUED or found inconsistent (an inconsistency is a valid outcome, to be reported to the FLOW lane if it is FLOW's).
- **Not success:** a statement whose polymer bound is not per-cube g-independent on the ε_1-domain, or that silently
  changes the coupling definition.

### Target S3: the small-field part of (CLS-NA), "CLS-sf"
- **Statement to prove (pre-stated form).** There are c_sf > 0 and ε_sf > 0, independent of k, K, T and g, such that for
  every k ≥ 1, every level-k field V whose level-k plaquettes all satisfy ||1 - V_P||_op < ε_sf, and every chain
  (U_0, …, U_{k-1}, V) [or: the infimum over chains, E_k(V)], E(chain) ≥ c_sf·Σ_P s(V_P), with the equalised-coupling chain
  energy E = Σ_ps(U_0(p)) + κΣ_iΣ_cφ_{M̄_c(U_i)}(U_{i+1}(c)). Inputs allowed: A1-NA(1)/(k), NA-alg, PM/KQ, E-low and N2-E
  (as proven in the ledger), Lemma 3.1/Theorem 3.8 of LINEAR_PACKAGE.
- **Route (pre-stated).** (i) A local (cone) form of the linear lower bound, proven in real space, so that the nonabelian
  comparison can be done cone by cone; (ii) an ε-regularity induction on the cone energy (small cone energy ⇒ every
  plaquette and residual in the cone small, at every level), reducing the nonabelian statement to an analytic estimate in
  the regime where every level is small; (iii) that estimate by link-level linearisation, using that averaging errors are
  LINK-level (their transport to level k decays like L^{-m} per depth m) while plaquette-level errors propagate marginally.
- **Success:** CLS-sf PROVEN-HERE uniformly in depth; or a PROVEN reduction of CLS-sf to a precisely stated wall, with the
  wall's linear case proven and the exact place where depth-uniformity is lost identified.
- **Failure modes.** (CS-F1) the constant degrades geometrically in depth (as HP-F1); (CS-F2) the argument needs a global
  small gauge (not available on the torus or for large-scale smooth fields); (CS-F3) the nonlinear errors are summable
  only for depth-decaying (smooth) chains; (CS-F4) the statement is false.
- **Not success:** a one-step bound iterated; a bound for smooth backgrounds only presented as general.

### Check h5 (criteria first: checks/h5_criteria.md, then the script)
- **h5 A** the real-space inequalities of the local linear bound (exact composite-average identity; the two counting
  bounds; the cone inequality on random and adversarial linear chains, d = 4, L = 3, depths 1 and 2).
- **h5 B** the HIST/FLOW comparison of (c1): d(M) := N⁻¹(tr P - max_{W∈SU(N)}Re tr(W⁻¹M)) ≥ 0 is V-independent, vanishes
  for SU(2), and its order in the spread y of an average of near-identity SU(3) matrices.

# Session-2 derivations (written after §13)

## 14. Step 2: the chain-energy form (I_k^E) of the representation on Λ_k

### 14.0 The tree tower (definition, and one elementary identity)
For a level-i field U and a level-(i+1) field V put Φ_i(U, V) := Σ_cφ_{M̄_c(U)}(V_c) (φ of (3.0); the kernel exponent with
the SU(N) maximiser). **𝓔_0 := Σ_ps(U_p), 𝓔_{i+1}(V) := min_U[𝓔_i(U) + κΦ_i(U, V)]** (minimum over a compact group power;
it exists). *Identity (elementary, PROVEN-HERE, not counted):* 𝓔_k = E_k of §6, i.e. 𝓔_k(V) = inf over chains
(U_0, …, U_{k-1}, V) of the equalised chain energy E(chain) := Σ_ps(U_0(p)) + κΣ_{i<k}Φ_i(U_i, U_{i+1}). *Proof.* Split the
infimum: inf_{U_0,…,U_{k-1}} = inf_{U_{k-1}}inf_{U_0,…,U_{k-2}}, and induct. ∎ 𝓔_k ≥ 0 = 𝓔_k(1), gauge invariant, coarse
translation and B_4 invariant (D4-norm (1)).

### 14.1 Hypothesis (I_k^E) [HYPOTHESIS, P; new in kind; the form (SF)_k must output] (precise statement) **[RH2-fix: this statement has three GAPs, S2-1 (a), S2-2 (b), S2-3 (d), marked below; the repaired statement is (I_k^E)' of §20.3]**
For every k ≤ K, every admissible history 𝔥 and every level-k configuration U with 1_𝔥(U) = 1, on the small-field region
Λ_k = Λ_k(𝔥):
  e^{-S_k(U)}|_{𝔥} = e^{𝒱_k}·exp(-u_kΣ_{x∈Λ_k}𝓔_{k,x}(U) - Σ_{X⊂Λ_k}E_k(X; U))·ℒ_𝔥(U),
with the following, all constants (E_0, κ_p, α_E, C_ℓ, B_0) independent of g, k, K, T and 𝔥:
- **(a) Main term.** u_k := 1/g_k² is the β-functional coupling of FLOW Def F-g (u_k = β[S_k] in infinite volume on the
  small-field domain), NOT a coarse-Wilson coupling. 𝓔_{k,x} is the local density of the tower over the level-k cube x:
  the energy terms (level-0 plaquettes, kernel terms) of the tree minimiser chain Φ_{·←k}(U) lying over x, defined on the
  small-field domain by (SF-bg) (FLOW §4: the tower minimiser is unique, real-analytic and exponentially local there), so
  that Σ_x𝓔_{k,x} = 𝓔_k whenever U is small-field on the whole torus; 0 ≤ 𝓔_{k,x}(U) ≤ C_𝓔 for U small-field near x.
  **[GAP S2-1]** The tower minimiser is global: on a U that is small-field only on Λ_k it reads U on Ω^c_k, where (SF-bg) gives
  neither uniqueness nor analyticity, so 𝓔_{k,x}, x ∈ Λ_k, is undefined exactly where (I_k^E) is needed (the local main term
  needs global smallness); the assignment of straddling terms is unspecified.
- **(b) Polymers.** X ranges over *-connected unions of level-k cubes in Λ_k; E_k(X; ·) depends on U|_X only, is real
  analytic on the complex polydisc 𝔇_α(X) := {|B^a_b| ≤ α_E in normalised Lie coordinates of a local gauge on X} with
  α_E ≥ c·ε_1 (a g-INDEPENDENT radius: the whole ε_1-domain), gauge invariant, translation and B_4 covariant (orbit sums),
  **[GAP S2-2]** a single-gauge polydisc on X does NOT contain the ε_1-domain when X contains an m × m square with
  m > 4α_E/ε_1 (Stokes: flux ≈ m²ε_1 ≤ 4m·max|B|), so the sup bound misses the actual configurations on large polymers;
  and
    Σ_{X∋x}sup_{𝔇_α(X)}|E_k(X; U) - E_k(X; 1)|·e^{κ_pd(X)} ≤ E_0  (per cube x),   β[Σ_XE_k(X)] = 0 (renormalisation).
  E_0 is bounded but NOT small: the field-dependent one-loop functionals Γ_j (FLOW §5.1), accumulated over j < k with their
  irrelevant parts contracted, are O(1)·(field)² per cube; the higher-loop and returned large-field terms are O(g_k²) and
  O(e^{-a_♯/g_k²}) (FLOW (SF-g), (RLF-δ)). C³ bounds in the data follow by Cauchy on 𝔇_α.
- **(c) Large-field factor** ℒ_𝔥 as RLARGE §8.1 (unchanged), carried in the history representation of §7.
- **(d) Two-field form (the (SF^J) interface).** At stage k, before U_k is integrated, the joint integrand of (U_k, U_{k+1})
  on Λ_k × Λ_{k+1} has main term **u_k[Σ_x𝓔_{k,x}(U_k) + κΦ_k(U_k, U_{k+1})]** (the kernel K_k has stiffness κ/g_k² = κu_k
  exactly, (3.0)), plus the polymers of (b), the R1^J remainders ℛ^J_x and re-extracted polymers (functions of
  (U_k, U_{k+1}, U_{k+2})) and the coupling-shift polymer of §14.3, each obeying (b)'s bound with E_0 for the first and
  ≲ C^J_*g_k^{-6}e^{-a''_J/g_k²} per cube for the others. **[GAP S2-3]** The kernel normalisation
  -Σ_clog∫e^{-κu_kφ_{M̄_c(U_k)}} (a field-dependent function of U_k, O(1) per link with a quadratic part, not β-free; it
  feeds Γ_k's 𝒩'_1 term and u_{k+1} in (c5)) is missing from this list.
- (I_0^E) holds: 𝓔_0 = Σs, E_0 ≡ 0, u_0 = 1/g_0² (the bare action is exactly the main term).
**What it replaces.** RLARGE §8.1's (I_k) on Λ_k (main term (1/g̃_k²)Σs(U_p)), which §6 [RH1-fix H-2] argues false on the
ε_1-domain. (I_k^E) is the analogue of Balaban's and Dimock's effective actions, whose main term is the action of the
background (minimiser) field [inference for the soft chain; CMP 122 not read].

### 14.2 Consistency checks (each with its status)
**(c1) With FLOW Lemma F-tree: the coupling of the main term is u_k.**
- **Lemma HF (HIST's φ-tower against FLOW's k̃-tower): PROVEN-HERE [S2-D] (counted).** Let ||M||_op ≤ 1, M invertible,
  M = WP its polar decomposition (W ∈ U(N), P > 0), W_0 an SU(N) maximiser of Re tr(W'⁻¹M), and k̃(V, M) :=
  N⁻¹Re tr((1 - V⁻¹W)P) (FLOW §3.1). Then
  (i) k̃(V, M) = φ_M(V) + d(M) for every V ∈ SU(N), with d(M) := N⁻¹(tr P - Re tr(W_0⁻¹M)) ≥ 0 independent of V;
  (ii) 0 ≤ d(M) ≤ (tr P/N)(1 - cos(α/N)) ≤ α²/(2N²), α := arg det M ∈ (-π, π]; in particular d ≡ 0 for N = 2 **when M is a non-negative combination of SU(2) elements** (every
  M̄_c is; false for a general 2 × 2 contraction) **[RH2-fix 8]**;
  (iii) if M = Σ_jw_je^{Y_j} (w_j ≥ 0, Σw_j = 1, Y_j ∈ su(N), |Y_j|_HS ≤ y ≤ 1/20), then |α| ≤ 1.05(4.8√N + 7)y³, so
  d(M) ≤ [1.05(4.8√N + 7)]²y⁶/(2N²) (≤ 14.4y⁶ at N = 3).
  *Proof.* (i) V⁻¹WP = V⁻¹M, so k̃ - φ = N⁻¹[tr P - Re tr(V⁻¹M) - Re tr(W_0⁻¹M) + Re tr(V⁻¹M)] = d(M); and Re tr(YP) ≤ tr P
  for unitary Y gives d ≥ 0. (ii) det M = det W·det P with det P > 0, so det W = e^{iα}; W_1 := We^{-iα/N} ∈ SU(N) and
  Re tr(W_1⁻¹M) = Re(e^{iα/N}tr P) = cos(α/N)tr P ≤ Re tr(W_0⁻¹M); tr P ≤ N because ||M|| ≤ 1; 1 - cos t ≤ t²/2. For N = 2,
  M is a non-negative multiple of an SU(2) element (sums of SU(2) matrices are real multiples of SU(2) matrices, the
  quaternion structure), so det M ≥ 0 and α = 0. (iii) NA-alg (a) (PROOF l.2914-2941): W_0 = e^{X_0}, |X_0| ≤ y + 9.2y² ≤ 3y,
  and G := W_0⁻¹M = H + iθ·1, H Hermitian, ||H - 1|| ≤ 18.4y², θ ∈ R. Since det W_0 = 1, α = arg det G = Σ_jarg(h_j + iθ),
  h_j ∈ [1 - 18.4y², 1] the eigenvalues of H, so |α| ≤ N|θ|/(1 - 18.4y²) ≤ 1.05N|θ|. And Nθ = Im tr G. With NA-alg's
  notation G = e^{-X_0}M = 1 + (Ȳ - X_0) + K(X_0), K = R_X + E + (R_X - X)(Ȳ + E): tr(Ȳ - X_0) = 0; Im tr R_X = Im Σ_{m≥3 odd}
  tr((-X)^m)/m! (tr X² is real for anti-Hermitian X), |·| ≤ √N(sinh|X| - |X|) ≤ 1.01√N|X|³/6 ≤ 4.6√Ny³; likewise
  |Im tr E| ≤ 0.17√Ny³; Im tr(XȲ) = 0 (tr of a product of two anti-Hermitian matrices is real), so |Im tr((R_X - X)(Ȳ + E))|
  ≤ |R_X||Ȳ + E| + |X||E| ≤ 5.23y²·1.03y + 3y·0.53y² ≤ 7y³ (|tr(AB)| ≤ |A|_HS|B|_HS). Sum: |Nθ| ≤ (4.8√N + 7)y³. ∎
- **Consequence (PROVEN-HERE given F-tree, not counted separately).** Termwise k̃ ≥ φ, so 𝒯_k ≥ 𝓔_k (FLOW's tower 𝒯_k of
  Def F-strip, written with k̃), with equality for N = 2; for N ≥ 3, 𝒯_k(V) ≤ 𝓔_k(V) + κΣ_{i,c}d(M̄_c(U*_i)) at 𝓔_k's minimiser
  chain U*, a sextic-order term in the contour spreads. φ and k̃ have the same quadratic part at the trivial field (d = O(y⁶)),
  so 𝓔_k and 𝒯_k have the same Hessian at 1, the linearised chain form H_k of LINEAR_PACKAGE Setting SC (κ_i ≡ κ); Lemma
  F-tree is a statement about H_k (its symbol Ĝ_k), so **β[𝓔_k] = 1**: the main term u_k𝓔_k has coupling exactly u_k, and the
  tree step does not renormalise it. [F-tree is FLOW's PROVEN-HERE, unreviewed; used read-only.]
- **Report to the FLOW lane (FLOW.md not edited).** FLOW §3.1 writes -log k_c = κu·k̃ + log 𝒩'(P) with 𝒩'(P) = ∫exp(-κuN⁻¹
  Re tr((1 - X)P))dX, X = W⁻¹V, and states "log 𝒩'(P) = -((N²-1)/2)log(κu) + O(1): it carries no power of u". For N ≥ 3 and
  det W ≠ 1, X ranges over the coset W⁻¹SU(N), on which the minimum of the exponent is d(M) > 0, so by Lemma HF (i)
  log 𝒩'(P) = -κu·d(M) + log∫e^{-κuφ}, i.e. it carries the term -κu·d(M). The identity itself is exact and equals (3.0);
  only the "no power of u" sentence is off, by a sextic term with β = 0. Tree-level conclusions (F-tree, F-bg, F-ren) are
  unaffected, since d has no quadratic part. The exact tree exponent is κuφ (SU(N) maximiser), i.e. the tower 𝓔_k, not 𝒯_k.
  **[RH2-fix 10] Strengthening (proposed edit for FLOW; FLOW.md not edited).** FLOW §5.1 puts Π_c𝒩'(P_c(U))⁻¹ into the
  U-integrand as an O(1) factor and Σ_clog𝒩'_1 into Γ_k as "the u-independent factor". For N ≥ 3 that factor contains
  e^{+κu·d(M̄_c(U))}, a function of the integration variable with coefficient u. On the ε_1-domain contour spreads reach
  A_dε_1 and d reaches α²/(2N²), which is O(1) there (not one-loop-sized): **κu·d is O(u) per link on the
  ε_1-domain**, not per-cube bounded, and it shifts the tree minimiser from 𝒯's to 𝓔's. So it is a β = 0 tree term of the
  (c3) kind, which must stay in the main term: **FLOW's tower must be φ-based (𝓔_k, SU(N) maximiser) wherever per-cube
  polymer bounds ((SF-g)) are claimed.** Proposed FLOW text: "§3.1: 𝒩' depends on det W; log 𝒩' = -κu·d(M) + log∫e^{-κuφ}.
  Replace k̃ by φ in Def F-strip and §5.1 (or move κu·d into the tower). β, F-tree, F-bg and F-ren are unchanged, since
  d = O(y⁶)."
  (h5 B: d ≡ 0 for SU(2) to 4.4·10⁻¹⁶; d ≥ -4.4·10⁻¹⁶; the k̃ - φ - d identity to 2.1·10⁻¹⁵; and d/[(trP/N)α²/(2N²)] = 1.0000
  in the median at y = 0.08: the bound (ii) is essentially attained. The pre-registered y⁶ slope test B3
  FAILED, see §16.)
**(c2) With LINEAR_PACKAGE E-low and N2-E: two-sided equivalence of the quadratic parts (PROVEN, citing the ledger).** In
FLOW's normalised coordinates (s(e^X) = ½Σ_a(X^a)² + O(X⁴)) the quadratic part of Σs(V_P) is ½||dB_k||² per colour and that
of 𝓔_k is E_k(B_k) of Setting SC (κ_i ≡ κ). Lemma 2.7 and Theorem 2.6: c_E||dB_k||² ≤ E_k(B_k) ≤ C_E(1 + κ)||dB_k||², uniformly in
k and T. So the main term is equivalent to the coarse Wilson action at quadratic order within the fixed factors
[2c_E, 2C_E(1 + κ)] = [0.0081, 4.8·10⁸] (κ = 1, L = 3), but NOT equal to it: c31 E2's ratios 0.0574-0.0585 (random data) and
0.0408 (one mode) differ (§6). §15.2 adds the local (cone) form of the lower bound.
**(c3) With (D1-c) (ARGUED, as the Laplace link).** At fixed k, g²(S_k(U) - S_k(U')) → 𝓔_k(U) - 𝓔_k(U') (Laplace link) and
u_k/u_0 → 1. (I_k^E)'s main term reproduces this limit exactly, and its field-dependent remainder is O(1) per cube (the
one-loop determinant ratio; the O(log(1/g)) Gaussian normalisations are c-numbers), so the (D1-c) obstruction does not arise.
The coarse-Wilson form fails because u_k(𝓔_k - Σs) has β = 0 (both have β = 1 by (c1)) but sup size ≍ u_kt² per cube at fields
of size t: it is a "renormalised remainder" in FLOW's sense (Def F-g) that is not per-cube bounded. **FLOW's renormalised
remainder and (D1-c) agree: the β = 0 tree part must stay in the main term, not in a per-cube-bounded polymer.**
**(c4) The coupling shift of R1^J against 𝓔_k (PROVEN, arithmetic, given (a)'s per-cube bound C_𝓔).** R1^J adds
δβ^J_kΣ_{p}s(U_k(p)) to the level-k exponent before U_k is integrated. Write δβ^J_kΣs = δβ^J_k·Σ_x𝓔_{k,x} + δβ^J_k(Σs - Σ_x𝓔_{k,x}).
The first term is the coupling shift u_k → u_k - δβ^J_k of the main term (adding +δβΣs to log e^{-S} lowers u_k)
**[RH2-fix 9: sign]** (β[Σs] = β[𝓔_k] = 1; FLOW Lemma F-id's "β = 2Nc̄"
reading is unchanged). The second has β = 0 and per level-(k+1) cube size ≤ |δβ^J_k|(12L⁸ + L⁴C_𝓔) ≤ C·C^J_*g_k^{-6}e^{-a''_J/g_k²}
(6L⁸ level-k plaquettes per cube, s ≤ 2): a small polymer of the class (d). §7.5 (P2)'s arithmetic is unchanged.
**(c5) Self-reproduction at tree level (PROVEN, elementary).** By §14.0, min_{U_k}[𝓔_k(U_k) + κΦ_k(U_k, V)] = 𝓔_{k+1}(V). So the
main term of (d) has tree-level minimum u_k𝓔_{k+1}(U_{k+1}): integrating U_k by the Laplace method gives u_k𝓔_{k+1} + Γ_k + …,
and Def F-g's u_{k+1} = u_k + β[Γ_k] + β[𝒮_k] turns it into u_{k+1}𝓔_{k+1} + (renormalised remainder): (I_{k+1}^E)'s form, with
the renormalised one-loop remainder in E_{k+1}. The ratio kernel-stiffness/action-coupling is κ at every level, as FLOW §3
requires.

### 14.3 What (I_k^E) changes downstream (pointers; status changes made in §7-§8 under [RH1-fix H-2])
- **CL^J, R1^J, R1_Λ, HIST-sum: untouched.** U_k is frozen in CL^J and the main term never enters it; R1^J uses only CL^J's
  activities; HIST-sum uses only (H-w).
- **(PLD-q)_k:** its Peierls exponent at threshold η_q under the (I_k^E) measure needs a classical lower bound
  u_k𝓔_k(U) ≥ u_kc_sf·η_q²-type per bad plaquette, uniformly in depth: this is CLS-sf (§15). The fluctuation part needs
  (b)'s E_0 per cube against u_kc_sfη_q² (fine for g small, since E_0 is g-independent).
- **(P4), (H-w)(b):** their per-cube E_0 is (b)'s; (P4) stays ARGUED pending review.
- **(SF)_k/(SF^J)_k:** must output (I_{k+1}^E), including (a)'s localisation of the tower on Λ_{k+1}.

## 15. Step 3: the small-field part of (CLS-NA)

### 15.1 Cones
Fix a level-k plaquette P with corner sites X, X + e_μ, X + e_ν, X + e_μ + e_ν. For i ≤ k let **W_P^{(i)}** be the set of
level-i sites descending from P's corners (the level-i sites of the four level-k blocks of the corners; a box of
2L^{k-i} × 2L^{k-i} × L^{k-i} × L^{k-i} level-i sites). The **cone** 𝒞(P) is the set of energy terms of the chain whose
vertices all lie in the W_P^{(·)}: the level-0 plaquettes with four vertices in W_P^{(0)}, and the kernel terms φ_c of the
level-(i+1) links c with both endpoints in W_P^{(i+1)} (0 ≤ i < k; for i + 1 = k these are P's four links). E_𝒞(P) := the
sum of these terms (s for plaquettes, κφ for kernel terms). Since S4' contours of c stay in c's two endpoint blocks,
M̄_c(U_i) depends only on level-i links inside W_P^{(i)} for such c.
- **Nesting.** If p is a level-i plaquette with vertices in W_P^{(i)}, then W_p^{(j)} ⊂ W_P^{(j)} for j ≤ i, so 𝒞(p) ⊂ 𝒞(P) and
  E_𝒞(p) ≤ E_𝒞(P).
- **[RH2-fix S2-4] Standing hypothesis: the level-k torus has side ≥ 3** (as A1-NA(1), [R56-fix]), so the four corner blocks
  are distinct and no cone wraps; "uniformly in T" below means "for every T with level-k side ≥ 3".
- **Overlap.** A term lies in 𝒞(P) iff the set A of level-k ancestors of its vertices is contained in P's corner set; a site
  is a corner of 24 level-k plaquettes (d = 4), so each term lies in ≤ 24 cones and **Σ_PE_𝒞(P) ≤ 24E(chain)**.

### 15.2 Lemma E-loc (the cone form of the linear lower bound): PROVEN-HERE [S2-D] (counted)
*Setting.* The linearised soft chain of LINEAR_PACKAGE Setting SC: real (or su(N)-valued, HS norms) level-i link fields
B_i, B_{i+1} = QB_i - r_i (Q the linearised S4' root map), 0 ≤ i < k, κ_- ≤ κ_i, and
E^{lin}_𝒞(P) := ½Σ_{p∈𝒞(P)}|dB_0(p)|² + Σ_i(κ_i/2)Σ_{c∈𝒞(P)}|r_i(c)|². *Claim.* For EVERY chain (not only minimisers) and every
level-k plaquette P,
  **|dB_k(P)|² ≤ C_loc·E^{lin}_𝒞(P),  C_loc := ((2L - 1)/(L - 1))·max{2, 16/κ_-}**  (= 40 at L = 3, κ ≡ 1),
uniformly in k and in every T of level-k side ≥ 3 [RH2-fix S2-4]. Hence ||dB_k||² ≤ 24C_loc·E(chain), i.e. **E_k(B_k) ≥ ||dB_k||²/(24C_loc)**: an independent real-space
proof of E-low's form (constant 1/960 ≈ 0.00104 at κ ≡ 1, L = 3, against Lemma 2.7's c_E = 0.004069), with the sup form
"every coarse plaquette is controlled by the energy of its own cone", which the Fourier proof does not give.
*Proof.* (1) *Representation.* B_k = Q^kB_0 - Σ_{i<k}Q^{k-1-i}r_i. Root covariance and Q = Q_str - d∘h (LINEAR_PACKAGE §1.2)
give d∘Q = d∘Q_str; and Q_str∘d = d∘avg (the straight average of a gradient is the gradient of the block average:
n^{-4}Σ_yΣ_{j<n}(f(y + (j+1)e_μ) - f(y + je_μ)) = n^{-4}Σ_y(f(y + ne_μ) - f(y))). By induction d∘Q^m = d∘Q_str^m = d∘Q_str^{(L^m)} (the
composite of m straight averages is the straight average of side L^m, LINEAR_PACKAGE Lemma 2.4). (2) *The square formula.*
For a link field A and n = L^m, d(Q_str^{(n)}A)(P) = n^{-4}Σ_{y∈B_n(X)}∮_{∂sq_y}A, sq_y the n × n square at y in P's plane: the four
coarse links of P are n^{-4}Σ_y of the four legs, and B(X + e_μ) = B(X) + ne_μ pairs the legs into the boundary of sq_y (h5 A1).
(3) *Main term.* ∮_{∂sq_y}B_0 = Σ_{p∈sq_y}dB_0(p), so |∮|² ≤ n²Σ_{p∈sq_y}|dB_0(p)|² (Cauchy-Schwarz, n² plaquettes). A plaquette p
of P's plane lies in sq_y for ≤ n² of the n⁴ points y ∈ B_n(X) (h5 A2). So |d(Q^kB_0)(P)|² ≤ n^{-4}Σ_y|∮_y|² ≤ n^{-4}·n²·n²·
Σ_{p∈R_0(P)}|dB_0(p)|² =: a², R_0(P) := ∪_ysq_y, whose plaquettes have vertices in W_P^{(0)}. (4) *Residual terms.* For r_i, a
level-(i+1) field, transported by m := k - 1 - i steps (n = L^m in level-(i+1) units): |∮_{∂sq_y}r_i|² ≤ 4nΣ_{c∈∂sq_y}|r_i(c)|²
(4n links), and a link c lies on ∂sq_y for ≤ 2n points y (its transverse coordinates are fixed, one in-plane coordinate has n
choices, the other 2; h5 A2). So |d(Q^mr_i)(P)|² ≤ n^{-4}·4n·2n·Σ_{c∈R'_i(P)}|r_i(c)|² = 8L^{-2m}ρ_m², ρ_m² := Σ_{c∈R'_i(P)}|r_i(c)|²,
with R'_i(P) := ∪_y∂sq_y ⊂ links with both endpoints in W_P^{(i+1)}. (5) *Sum.* |dB_k(P)| ≤ a + Σ_{m≥0}√8L^{-m}ρ_m, and by
Cauchy-Schwarz with weights 1 and L^{-m}, (a + Σ_mb_m)² ≤ (1 + Σ_mL^{-m})(a² + Σ_mL^mb_m²) = ((2L - 1)/(L - 1))(a² + 8Σ_mL^{-m}ρ_m²).
Finally a² ≤ 2·(½Σ_{𝒞}|dB_0|²) and 8L^{-m}ρ_m² ≤ (16/κ_i)·(κ_i/2)ρ_m². (6) *Global.* Sum over P with the overlap 24 (§15.1). ∎
(h5 A3: max ratio |dB_k(P)|²/E_C(P) = 3.81 over random chains with residual scale up to 10, 0.72 / 0.56 for constant flux
(k = 1, 2; predicted 2n²/(2n - 1)² = 0.72 at n = 3), 0.41 after random-search ascent, against C_loc = 40.)
*Reading.* The main term is controlled without any sign cancellation (ℓ¹ Stokes then Cauchy-Schwarz), and each residual
is a LINK-level source whose effect on a level-k plaquette decays like L^{-m} in depth m (its flux through a big square is
a boundary circulation, 4n links, spread over n⁴ positions). Both mechanisms have exact non-abelian counterparts:
||1 - hol(∂S)|| ≤ Σ_{p∈S}||1 - U_p|| (lasso decomposition and unitarity) and ||hol(γ) - hol(γ')|| ≤ Σ||U_c - U'_c|| over the
changed links. What does not carry over verbatim is step (1), the linear representation through the composite average.

### 15.3 Hypothesis (AE) (multiscale linearisation in the every-level-small regime) [OPEN; P] **[RH2-fix: a LOCAL perturbative-regime strengthening of (CLS-NA), constant any depth-uniform; not a weakening of (CLS-NA)]**
**[RH2-fix S2-5, S2-7] Restated form (binding; the original is kept below, struck as the operative statement).** There are
ε_AE > 0 and C'_AE < ∞, independent of k, K and T (level-k side ≥ 3), such that (i)-(ii) below with ε ≤ ε_AE imply
**U_k(P) = e^X with X ∈ su(N), |X|²_HS ≤ C'_AE·E_𝒞(P)** (hence s(U_k(P)) ≤ |X|²_HS/(2N)). No principal log of U_k(P) is
used, and any depth-uniform C'_AE suffices. Logically (AE) ⇒ (CLS-NA) (Theorem CLS-red) but (CLS-NA) ⇏ (AE): (AE) is a
local, pointwise strengthening restricted to the perturbative regime. *Original (superseded) wording:*
There are ε_AE > 0 and C_AE < ∞, independent of k, K, T, such that for every k ≥ 1, every chain (U_0, …, U_k) and every
level-k plaquette P, if for some ε ≤ ε_AE
- (i) every level-i plaquette p with vertices in W_P^{(i)} (0 ≤ i < k) has |log U_i(p)|_HS ≤ ε (principal logarithm), and
- (ii) every level-(i+1) link c with endpoints in W_P^{(i+1)} (0 ≤ i < k) has ||U_{i+1}(c) - W_0(M̄_c(U_i))||_op ≤ ε,
then **|log U_k(P)|²_HS ≤ (1 + C_AEε)·N·C_loc·E_𝒞(P)**, E_𝒞 the NON-ABELIAN cone energy (s and κφ terms).
*Status.* Its linear case (abelian linear chain; C_AE = 0, no ε restriction; s(e^X) ↦ |X|²/(2N), φ ↦ |r|²/(2N)) is Lemma
E-loc (in HS norms: |dB_k(P)|²_HS ≤ C_loc[½Σ|dB_0|²_HS + Σ(κ_i/2)|r_i|²_HS] = C_loc·N·E^{lin}). The non-abelian statement is OPEN;
§15.5 says exactly where depth-uniformity is at stake.

### 15.4 Theorem CLS-red ((AE) ⇒ (CLS-NA), uniformly in depth): CONDITIONAL [S2-D] (implication proven ⇐ (AE))
*Claim.* Assume (AE). Put C_* := 2N·C_loc **[RH2-fix S2-5: with the restated (AE), C_* := max{C'_AE, 2N(1 + φ²/6)} and η_E is
chosen after C_*; the steps below are unchanged with (1 + C_AEε)NC_loc replaced by C'_AE, and (δ) reads s ≤ (C'_AE/(2N))E_𝒞]**, and let η_E > 0 be so small (depending only on N, L, κ, C_AE, ε_AE **[RH3-fix N-4: read C'_AE, ε_AE, η_AE; and choose η_E ≤ η_AE, so that (AE)'s energy cap (iii) of §20.3 holds wherever step γ applies (AE)]**) that
ε := max{√(C_*η_E), c_0√(2Nη_E), √(4Nη_E/κ)} satisfies ε ≤ ε_AE, C_AEε ≤ 1, (c'A'ε) ≤ 1/20 and 73.6N(c'A'ε)² ≤ ε, where
c' := 4arcsin(¼)·√N (op-to-HS log conversion, A1-NA(1) step 1 and its [R56-fix]), c_0 := 4arcsin(¼) and A' := 2A_d
(two ribbons of RS (R1): each contour T^σ_y differs from the straight centre transporter S_c by the holonomy of a ribbon of
≤ A_d level-i plaquettes, the bound CL^J (c) (iii) uses). Then for every k, every chain and every level-k plaquette P:
- (ε-regularity) if E_𝒞(P) < η_E, then |log U_k(P)|²_HS ≤ C_*E_𝒞(P);
- (CLS-NA, strong form) **s(U_k(P)) ≤ max{C_loc, 2/η_E}·E_𝒞(P)**, hence
  **E(chain) ≥ c_cl·Σ_Ps(U_k(P)),  c_cl := 1/(24·max{C_loc, 2/η_E}),**
  **[RH3-fix N-4] With the restated (AE) these two displays read s(U_k(P)) ≤ max{C'_AE/(2N), 2/η_E}·E_𝒞(P) = C_cone·E_𝒞(P) and
  c_cl := 1/(24·C_cone), C_cone := max{C'_AE/(2N), 2/η_E} (§20.3 (B)); the max{C_loc, 2/η_E} form is the superseded (AE)'s.**
  for EVERY level-k field U_k (no small-field restriction, no disjointness condition, no min{·, s_1}), and in particular
  𝓔_k(V) ≥ c_clΣ_Ps(V_P): CLS-sf, with c_sf = c_cl and any ε_sf.
*Proof.* Induction on the level i of the plaquette, for the ε-regularity statement (all chains at once). *i = 0:* E_𝒞(p) ≥ s(U_0(p))
(p ∈ 𝒞(p)); if s < η_E then ||1 - U_0(p)||²_HS = 2Ns < 2Nη_E, so ||1 - U_0(p)||_op ≤ √(2Nη_E) ≤ ½ and |log U_0(p)|²_HS ≤ (1 + φ²/6)
·2N·s(U_0(p)) ≤ C_*E_𝒞(p) (A1-NA(1) step 6; C_loc > 4, so C_* > 8N ≥ 2N(1 + φ²/6)). *Step i → k:* let E_𝒞(P) < η_E. (α) Every level-i plaquette p in the cone
(i < k) has E_𝒞(p) ≤ E_𝒞(P) < η_E (nesting), so by induction |log U_i(p)|_HS ≤ √(C_*η_E) ≤ ε (for i = 0 directly). (β) Every
residual in the cone is small: let c be a level-(i+1) link of the cone, T_j its S4' contour transporters (in W_P^{(i)}). For two
contours T_1, T_j, T_1⁻¹T_j = (T_1⁻¹S_c)(S_c⁻¹T_j) is a product of two ribbon holonomies over ≤ A' level-i plaquettes, all in
the cone (**[RH2-fix S2-6]** the S4' contours T^σ_y of c use axial moves inside one endpoint block and one straight leg
between the two blocks, S_c is straight between the centres, and the RS (R1) ribbons are 1 × L rectangles at the off-axis
steps; all lie in the coordinate box formed by c's two endpoint blocks, which lies in W_P^{(i)}), so ||1 - T_1⁻¹T_j||_op ≤ A'ε (lasso decomposition and unitarity) and |Y_j|_HS := |log(T_1⁻¹T_j)|_HS ≤ c'A'ε =: y ≤ 1/20.
NA-alg (a) applied to T_1⁻¹M̄_c = avg_je^{Y_j} (W_0 is left-covariant: W_0(T_1⁻¹M̄) = T_1⁻¹W_0(M̄)) gives ||M̄_c - W_0(M̄_c)||_op =
||G - 1||_op ≤ |Ȳ - X_0| + |K(X_0)| ≤ 18.4y² (NA-alg (a), proof of the G-bound). KQ (lower) with x := ||U_{i+1}(c) - W_0||_op: φ_c ≥ x²/(2N) - 18.4y²x. Either x ≤ 73.6Ny² ≤ ε, or
φ_c ≥ x²/(4N), and κφ_c ≤ E_𝒞(P) < η_E gives x ≤ √(4Nη_E/κ) ≤ ε. (γ) So (AE)'s hypotheses hold with this ε, and (AE) gives
|log U_k(P)|²_HS ≤ (1 + C_AEε)NC_locE_𝒞(P) ≤ C_*E_𝒞(P). This proves ε-regularity at level k. (δ) CLS: if E_𝒞(P) < η_E,
s(U_k(P)) ≤ |log U_k(P)|²_HS/(2N) (1 - cos θ ≤ θ²/2) ≤ C_locE_𝒞(P); otherwise s ≤ 2 ≤ (2/η_E)E_𝒞(P). Sum over P with the
overlap 24 (§15.1). ∎
*Remarks.* (1) The induction never iterates a per-level constant: the constant C_* is re-derived at each level from (AE)
and the cone energy, which is an AGGREGATING quantity (all L^{4(k-i)} level-i terms under P), so Proposition CF's method
limit does not apply ([RH1-fix H-8]); CF itself is consistent (its energy per level-k site ≈ θ²/2 ≈ s(V_P)). (2) The
large-field case of (CLS-NA) is not harder than its small-field core: small cone energy forces every level of the cone into
the regime of (AE) (steps α-β), and large cone energy pays for itself because s ≤ 2. (3) Only the classical (tree-level)
statement is reduced; (D1-b) still needs the fluctuation bound at large fields (HP-F3), and (D1-b) is still not consumed
by RLF-step^J.

### 15.5 Where (AE) stands, and where depth-uniformity is at stake
- **What carries over (argued at constants level, not written as a proof).** In a gauge on the cone in which every link
  variable is small, write a_i := log U_i (links). The chain relation is a_{i+1} = Qa_i + e_i - ρ_i, where ρ_i is the residual
  (|ρ_i|² ≲ 4Nφ + (73.6Ny²)², step β above) and e_i collects the BCH errors along contours and the averaging error of NA-alg (a)
  (|X_0 - Ȳ| ≤ 9.2y²): e_i is a LINK-level source, quadratic in local link sizes. Lemma E-loc's steps (1)-(5) then apply
  verbatim to the linear recursion with sources ρ_i - e_i, and link-level sources at depth m enter with the decaying weight
  √8L^{-m}; plaquette-level errors appear only twice (level-0 plaquettes vs da_0, and the top plaquette vs Σ_{c∈∂P}a_k(c)).
- **(CS-F2) is the wall: the gauge.** The cone is a box of side ~2L^k level-0 sites. In complete axial gauge (A1-NA(1) step 2)
  link variables grow with the distance and the coarse links concentrate on block faces, so the inherited link sizes add up
  over the levels (Σ_j of local sizes), and the linearisation is not uniform in k. What is needed is an **interpolation
  gauge** [MSG, inference]: at each level i, a gauge (fixed at block centres by level i + 1) with
  |a_i(b) - I(a_{i+1})(b)| ≤ C_M·(local level-i plaquette and residual sizes near b), I the interpolation of coarse links with
  |I(a)| ≤ (C_I/L)|a|, C_I² < L; and then a **multi-scale ℓ⁴ (Sobolev-type) bound** [MS-Sob, inference] for the resulting link
  field, Σ_b|a_0(b)|⁴ ≲ C_S·E_𝒞(P)² (the lattice analogue of ||A||_{L⁴} ≤ C||F||_{L²} in Coulomb gauge; scale invariant in
  d = 4), which is what controls the level-0 plaquette BCH errors (which propagate MARGINALLY, without decay). With (MSG) and
  (MS-Sob), the link-level errors cost Σ_m(m + 1)²C_I^{2m}L^{-m}·ε√E_𝒞, summable for C_I² < L, and (AE) would follow with
  C_AE = C(N, L, κ, C_M, C_I, C_S). Neither (MSG) nor (MS-Sob) is proven here; both are of the kind Balaban's small-field gauge
  fixing supplies (CMP 95-99) [not-read for this statement].
- **Where uniformity is lost in the obvious alternative.** Per-step plaquette bookkeeping (A1-NA(1)(b) iterated, as in
  Corollary A1-NA(k)) has the factor Π_j(1 + C_6φ_j), uniform only when Σ_jφ_j < ∞ (true on the L1e domain and for the
  linear minimiser, whose level-i curvatures are ≲ L^{-2(k-i)}sup|dB_k| by LINEAR_PACKAGE Theorem 3.8; false for general
  small-field chains): failure mode (CS-F3). It also cannot handle residuals uniformly even linearly (a residual's curvature
  dr is not small; its decay appears only through the link-level transport of step (4)). The cone/link-level route avoids
  both; the gauge is what remains.

## 16. Check h5 (criteria first: checks/h5_criteria.md 00:08:33 UTC; script checks/h5_cone_and_dM.py; records h5_time.txt, h5_out.txt)
First and only run (00:21:39-00:21:41 UTC, under the numeric lock, nice 10, BLAS threads 1, load 3.25, 39% free, 1.7 s,
peak RSS 148 MB). **OVERALL: FAIL as pre-registered (B3); A1, A2, A3, B1, B2, B4 PASS.**
- **A1 PASS.** Q_str^{(3)}∘Q_str^{(3)} = Q_str^{(9)} to 8.6·10⁻¹⁷ (relative); d(Q^{(n)}A)(P) = block average of square fluxes to
  1.2·10⁻¹⁶ (n = 3, 9): step (2) of Lemma E-loc.
- **A2 PASS.** Plaquette multiplicity exactly n² (9, 81); link multiplicity n (3, 9), below the proof's 2n (the proof's
  count is generous by 2: a link is on the "bottom" or the "top" edge, not both, for a given y).
- **A3 PASS.** max |dB_k(P)|²/E_C(P) = 3.81 (k = 1, residual scale 10), 0.06 at k = 2 for the same scale (the L^{-m} decay
  is visible), 0.720 and 0.561 for constant flux (0.720 = 2n²/(2n - 1)² predicted at n = 3), 0.41 after random-search ascent;
  all ≤ C_loc = 40. A4 (info): global ratio ≤ 1.99 against 480.
- **B1, B2, B4 PASS.** SU(2): d ≤ 4.4·10⁻¹⁶ (exactly 0 up to rounding); d ≥ -4.4·10⁻¹⁶; k̃ - φ - d = 0 to 2.1·10⁻¹⁵.
  Maximiser check: no competitor beat W_0 (max F(competitor) - F(W_0) = -5·10⁻¹³; 200 near and far competitors).
- **B3 FAIL (pre-registered).** Median slope of log d against log y = 5.37 (prediction band [5.5, 6.5]), with only 20 of
  50 samples having d > 0 at all four y (range 2.72-6.28). Diagnosis (post hoc, labelled; h5b below): at y = 0.02 the
  predicted d ≲ 14.4y⁶ ≈ 9·10⁻¹⁰ is in practice ~10⁻¹⁴-10⁻¹⁶, at the rounding floor of tr P - Re tr(W_0⁻¹M) ≈ 3, so the
  smallest-y point drags the fit; the criterion did not account for the noise floor. The FAIL stands as recorded.
- **B5 (info).** d/[(tr P/N)α²/(2N²)] has median 1.0000 (range 0-1.019 at y = 0.08), so Lemma HF (ii)'s bound is essentially
  an equality for these averages. A ratio above 1 would contradict the rigorous bound (ii), so the 1.019 can only be
  numerical [inference: the outliers are samples with small α, where d is at the rounding floor; not separately tested].
- **h5b (POST HOC diagnostic, written after B3 failed; not a criterion change; checks/h5b_diag.py, h5b_out.txt).** Run 00:32:03 UTC under the lock (load 3.32, 33% free, 0.1 s, 57 MB). |α| = |arg det M| scales as y^3.000
  (median; range 2.999-3.004; max |α|/y³ = 0.010 at y ≤ 0.04, far below Lemma HF (iii)'s bound 16.1 at N = 3); d scales as
  y^5.99 on y = 0.04-0.16 (47/50 samples with d > 0) and y^6.000 on y = 0.08-0.32 (50/50; range 5.84-6.17). So the O(y⁶)
  behaviour of Lemma HF (iii) is seen once the rounding floor is excluded; this is a post-hoc reading and does not
  reverse the recorded B3 FAIL.

## 17. Outcomes against the session-2 targets (§13) (ADDED AFTER the derivations; pointers only)
- **[RH2-fix] Target S2 ((I_k^E)): MET-WITH-FIX (REVIEW_HIST_S2), not MET: GAPs S2-1, S2-2, S2-3; repaired in §20.3.** *Original line:* MET. Precise statement §14.1 (a)-(d). (c1) PROVEN: Lemma HF (HIST's φ-tower and FLOW's k̃-tower
  agree exactly for SU(2) and up to a sextic, β-neutral term for N ≥ 3), hence β[𝓔_k] = 1 given F-tree; an imprecision in
  FLOW §3.1 found and reported (log 𝒩' carries -κu·d(M) for N ≥ 3; harmless at tree level). (c2) PROVEN (E-low, N2-E;
  local form E-loc). (c3) ARGUED (Laplace link). (c4) PROVEN (arithmetic, given (a)'s per-cube bound). (c5) PROVEN
  (elementary).
- **Target S3 (CLS-sf): NOT MET as a proof; MET in the alternative success form.** A PROVEN reduction (Theorem CLS-red):
  CLS-sf, and in fact (CLS-NA) for every field in the strong form E ≥ c_clΣ_Ps(V_P), follows uniformly in depth from one
  precisely stated small-field wall (AE); (AE)'s linear case is Lemma E-loc (PROVEN-HERE); the place where depth-uniformity
  is at stake is identified: the gauge on the cone (CS-F2), with the interpolation gauge (MSG) and a multi-scale ℓ⁴ bound
  (MS-Sob) as the two named ingredients [inference]. Failure modes: (CS-F1) AVOIDED (no per-level constant is iterated);
  (CS-F2) MET by (AE) as the wall; (CS-F3) MET by the per-step plaquette route only (§15.5); (CS-F4) not observed.
- **Status change of a session-1 wall:** (CLS-NA) [OPEN] → CONDITIONAL ⇐ (AE) (Theorem CLS-red); the OPEN wall is now (AE),
  a small-field (every level small) statement. **[RH2-fix 11]** (CLS-NA) is reduced to the LOCAL small-field statement (AE);
  (AE) is a local strengthening restricted to the perturbative regime, not a weakening or a smaller instance of (CLS-NA). This revises REVIEW_HIST_S1's strategic reading that the large-field case is
  off-limits [it remains off the main path; only its classical part is reduced]: given the cone/ε-regularity structure the
  large-field case is not harder than (AE).

## 18. Tally (session 2) and hypotheses consumed
- **Session-2 items.** PROVEN-HERE, counted (2): Lemma HF (§14.2); Lemma E-loc (§15.2). PROVEN-HERE, not counted: the tower
  identity §14.0; β[𝓔_k] = 1 (corollary of HF + F-tree); (c4) arithmetic; (c5). CONDITIONAL (1): Theorem CLS-red (⇐ (AE)).
  HYPOTHESIS (1): (I_k^E) [P] **[RH2-fix: with GAPs S2-1..S2-3 in the statement; see §20.3]**. OPEN (1): (AE) [P], the LOCAL
  small-field strengthening to which (CLS-NA) is reduced [RH2-fix 11]. [inference, not counted]: (MSG), (MS-Sob) and the §15.5 sketch
  (AE) ⇐ (MSG) + (MS-Sob).
- **Whole file after session 2 (unreviewed for session-2 items): 7 PROVEN-HERE / 3 CONDITIONAL / 6 ARGUED / 3 OPEN + 1
  HYPOTHESIS**: PROVEN-HERE PM, RS-lin, CL^J, R1^J, H-geo, HF, E-loc; CONDITIONAL RS-joint, HIST-sum, CLS-red; ARGUED as §11;
  OPEN (AE), (D1-b), (H-w) ((CLS-NA) moves to CONDITIONAL ⇐ (AE)); HYPOTHESIS (I_k^E).
- **Hypotheses consumed.** Lemma HF: NA-alg (a) (PROOF, PROVEN-HERE) for (iii); none for (i)-(ii). β[𝓔_k] = 1: FLOW Lemma
  F-tree (FLOW's PROVEN-HERE, unreviewed) and N5-coer as FLOW uses it. Lemma E-loc: LINEAR_PACKAGE §1.2 (Q = Q_str - d∘h, root
  covariance) and Lemma 2.4 (IT-str), both ledger PROVEN. Theorem CLS-red: (AE); NA-alg (a), KQ (lower), RS (R1)'s ribbon
  bound, A1-NA(1) steps 1 and 6. (c4): (I_k^E)(a)'s bound C_𝓔. (I_k^E) itself: (SF-bg) of FLOW §4.
- No change is made to the PROOF.md tally; nothing outside HIST.md, HIST_LOG.md, checks/h* was edited.

# Session 3 of lane D (2026-10-28)

## 19. Session-3 pre-stated targets (written 2026-10-28 01:00 UTC, after STEP 1's [RH2-fix] edits and after exploratory reasoning, BEFORE any written session-3 derivation (§20 onward) and before any h6 criteria file or script; not edited after the derivations start)

### Target S4: the multi-scale small-field gauge theorem (MSG)
- **Statement to prove (pre-stated form).** Let k ≥ 1, (U_0, …, U_k) a chain, P a level-k plaquette with cone 𝒞(P) (§15.1,
  level-k side ≥ 3). Suppose, for some ε ≤ ε_M: (i) every level-i plaquette p with vertices in W_P^{(i)}, 0 ≤ i ≤ k - 1,
  has ||1 - U_i(p)||_op ≤ ε; (ii) every level-(i+1) link c with endpoints in W_P^{(i+1)}, 0 ≤ i ≤ k - 1, has
  ||U_{i+1}(c) - W_0(M̄_c(U_i))||_op ≤ ε. Then there is a chain gauge (one level-0 gauge function on W_P^{(0)}, acting on
  U_i through its values at the level-i sites, which is the gauge freedom of the soft chain) in which every link b of every
  level i ≤ k in the cone has |log U_i^g(b)|_op ≤ C_M·ε, with C_M = C_M(N, L, d) and ε_M = ε_M(N, L, d) independent of k,
  K, T; and a local form in which ε is replaced by the local sizes at each level, weighted by L^{-(j-i)} for level j ≥ i.
- **Route (pre-stated).** Top level k - 1: complete axial gauge on the bounded box W_P^{(k-1)} (2L × 2L × L × L sites).
  Downward step i + 1 → i: build a reference fine field V = exp(I a_{i+1}) from the gauge-fixed coarse logs by a
  d-commuting interpolation I (lowest-order cubical Whitney forms, clamped outside the hull of the block centres) with
  |Ia| ≤ max|a|/L, and gauge-fix U_i to V along block-internal axial paths from the centres. The contraction 1/L per level
  is what makes the constant depth-uniform; the obstruction to avoid is the additive accumulation of the axial gauge
  (CS-F2).
- **Success:** MSG PROVEN-HERE with explicit constants. **Not success:** a constant growing in k, or a proof that uses a
  global small gauge on the cone (excluded by Stokes when only the level-0 data is small).

### Target S5: re-derive (AE), CLS-red and (I_k^E) on top of MSG
- (AE): reduce it to MSG plus a precisely stated remainder (the ℓ⁴ / square-function control of the marginal level-0 BCH
  errors), or prove it; state exactly what MSG does and does not supply.
- (I_k^E): repair GAPs S2-1 (localised main term without global smallness), S2-2 (a gauge-covariant domain containing the
  ε_1-domain on large polymers), S2-3 (kernel normalisation listed). Say where MSG is used and where it is not needed.
- CLS-red and CLS-sf: restate in the **cone-local (pointwise per cone) form**, usable defect by defect, with RLARGE's
  threshold η_1 = min{ε_1/(2L²), ε_1²/(512N·A_d(L))} (lead's note), and update statuses.
- **Not success:** an (AE) "proof" that iterates a per-level constant, or a repaired (I_k^E) whose domain still needs one
  gauge on large polymers.

### Check h6 (criteria first: checks/h6_criteria.md, then the script)
- **h6 A** (d = 4, SU(2), L = 3, depth 2, κ = 1): the non-abelian cone ratio R_NA := |log U_2(P)|²_HS / E_𝒞(P) on random
  and adversarial ε-small chains, against the linearised ratio R_lin on the same Lie data and against the linear constant
  N·C_loc = 80; R_NA/R_lin → 1 as the field scale t → 0, with an O(t) deviation.
- **h6 B** (same setting): the MSG gauge built as in the route; measured max|log U_i^g|/ε at levels 0, 1, 2; the exact
  identities used (hol_V(S_c) = e^{a_c}, |Ia| ≤ max|a|/L, gauge invariance of plaquettes and kernel terms).
- **h6 C** (d = 2, SU(2), L = 3, depths 1-5): depth-uniformity of the MSG constant, against complete axial gauge on the
  level-0 cone box.

# Session-3 derivations (written after §19)

## 20. Step 2: the multi-scale small-field gauge (MSG), and what it repairs

### 20.0 Elementary facts (op norm ||·||; |log U| the op norm of the principal log; all standard, PROVEN, not counted)
- (F1) U unitary, ||1 - U|| ≤ ½ ⇒ |log U| ≤ 1.011||1 - U|| (eigen-angles: |θ| = 2arcsin(|1 - e^{iθ}|/2), 2arcsin(x/2)/x ≤ 1.0107).
- (F2) X anti-Hermitian ⇒ ||1 - e^X|| ≤ |X|.
- (F3) X, Y unitary with ||1 - X||, ||1 - Y|| ≤ ½ ⇒ |log X - log Y| ≤ 2||X - Y|| (log(1 - Z) = -Σ_nZ^n/n on the convex ball
  ||Z|| ≤ ½; the derivative of Z^n/n has norm ≤ ||Z||^{n-1}; Σ_n2^{-(n-1)} = 2).
- (F4) Lasso: a closed loop spanned by a plaquette surface S has ||1 - hol|| ≤ Σ_{p∈S}||1 - U_p|| (product of conjugates of
  plaquette holonomies; ||1 - AB|| ≤ ||1 - A|| + ||1 - B|| for unitaries).
- (F5) x_1, …, x_m anti-Hermitian, s := Σ|x_j| ⇒ ||e^{x_1}⋯e^{x_m} - e^{x_1+⋯+x_m}|| ≤ 2(e^s - 1 - s) ≤ s²e^s (the two series agree
  in orders 0, 1; each order-n part has norm ≤ s^n/n!).
- (F6) Chain gauge freedom. M̄_c(U_i) transforms by the gauge at the two ROOTS c_X, c_Y (S4' is root covariant), so the soft
  chain is invariant under one level-0 gauge function g acting on U_i through its values at the level-i sites (the iterated
  block centres). A chain gauge is therefore built top-down: fix g at the level-(k-1) sites, then extend to the remaining
  level-(k-2) sites, …, then to all level-0 sites.

### 20.1 The interpolation I (lowest-order cubical Whitney forms, clamped)
Let the level-(i+1) box have coarse sites X (block centres c_X = LX + h in level-i units, h := (L - 1)/2) and let a be a
Lie-algebra-valued 1-form on its links. Let W(a) be the lowest-order cubical Whitney (Q1-Nédélec) 1-form of a on the hull of
the centres: on a coarse cell, W(a)_μ(ξ) = Σ_{e∥μ in the cell}a_e·Π_{ν≠μ}λ^e_ν(ξ_ν), λ the 1-d linear hats (so W(a)_μ is a convex
combination of the cell's 2^{d-1} μ-edges, constant in ξ_μ); outside the hull use the pull-back r^*W(a) by the coordinatewise
clamping r. For a level-i link b put **(Ia)(b) := ∫_bW(a)** (b has length 1/L in coarse units and lies in one cell along its
own direction, since centres are level-i sites). Then (PROVEN, standard properties of Whitney forms, not counted):
- (W1) |(Ia)(b)| ≤ L⁻¹max{|a_e| : e a coarse edge of the cell of b} (convexity of the norm). **C_I = 1.**
- (W2) On every coarse edge, W(a) restricted to the edge is a_e dξ_μ, so the L fine links of the straight centre segment S_c
  each carry a_c/L: Σ_{b∈S_c}(Ia)(b) = a_c, and the factors commute.
- (W3) d∘W = W_2∘d (Whitney forms commute with d; so does r^*), and W_2(f) on a cell is a convex combination of the cell's
  (μ,ν)-plaquette values in the (μ,ν) component (zero in a clamped direction). Stokes on each level-i plaquette p:
  (d Ia)(p) = ∫_pW_2(da), so **|(dIa)(p)| ≤ L⁻²max{|da(P')| : P' a coarse plaquette of the cell of p}.**
For the non-abelian reference field put V(b) := exp((Ia)(b)).

### 20.2 Theorem MSG (multi-scale small-field gauge on a cone): PROVEN-HERE [S3-D] (counted)
*Setting.* d ≥ 2, L ≥ 3 odd, N ≥ 2; k ≥ 1; a chain (U_0, …, U_k); P a level-k plaquette; the cone boxes W_P^{(i)} of §15.1
(level-k side ≥ 3). Constants: A_d := (d - 1)L(L - 1)/2, A_ax := (2L - 1) + (d - 2)(L - 1), B := 2A_d + 2 + 2.02A_d/L²,
**C_* := max{1.011A_ax, 2BL/(L - 1)}, C_M := max{C_*, 1.011(1.011L·A_ax + 2A_d + 1)}** (d = 4, L = 3: A_d = 9, A_ax = 9, B = 22.0,
C_* = 66.1, C_M = 66.1).
**[RH3-fix S3-1]** A_ax = (2L - 1) + (d - 2)(L - 1) (= 9) holds only when the top-level axial order starts with one of P's two
plane directions; the construction below is restated with that order. For an arbitrary fixed order (e.g. 0, …, d - 1 with P
in a plane not containing axis 0) put A_ax := 2(2L - 1) + (d - 3)(L - 1) (= 12 at d = 4, L = 3). Either way C_* = max{1.011A_ax,
2BL/(L - 1)} = 66.1 (1.011·12 = 12.1 < 66.06), and C_M's second entry becomes 1.011(1.011·3·12 + 19) = 56.0 < 66.1, so
**C_M = 66.1 is unchanged**; (S1) reads A_axε ≤ ½ (12ε ≤ ½ in the second form).
*Hypotheses,* for some ε ≤ ε_M (ε_M = ε_M(N, L, d) > 0 fixed by (S1)-(S4) below):
- (i) ||1 - U_i(p)|| ≤ ε for every level-i plaquette p with vertices in W_P^{(i)}, 0 ≤ i ≤ k - 1;
- (ii) ||U_{i+1}(c) - W_0(M̄_c(U_i))|| ≤ ε for every level-(i+1) link c with endpoints in W_P^{(i+1)}, 0 ≤ i ≤ k - 1.
*Claim.* There is a chain gauge g (F6) such that every link b of every level i ≤ k with endpoints in W_P^{(i)} satisfies
  **|log U_i^g(b)| ≤ C_M·ε,** with C_M and ε_M independent of k, K, T.
*Construction.* Level k - 1: complete axial gauge on the box W_P^{(k-1)} (order 0, 1, …, d - 1, root at a corner **[RH3-fix S3-1:
axes relabelled so that P's two plane directions come first; otherwise use A_ax = 12 as above]**). Step
i + 1 → i (i = k - 2, …, 0), given g on the level-(i+1) sites with a := log U_{i+1}^g on the level-(i+1) cone links: let V :=
exp(Ia) (§20.1) on the level-i box; for a level-i site x in the block of X let γ_x be the axial path (order 0, …, d - 1) from
c_X to x inside the block, and put **g(x) := hol_U(γ_x)^†·g(c_X)·hol_V(γ_x)** (so g(c_X) is unchanged, and
hol_{U^g}(γ_x) = hol_V(γ_x)).
*Proof.* Write U^g(b) = g(x)^†U(b)g(y) for b = (x, y) and α_{i+1} := max|a| at level i + 1.
(1) *Top level.* In complete axial gauge a link b = (x, x + e_μ) carries the holonomy of the loop γ_xbγ_{x+e_μ}⁻¹, spanned by the
ladder of Σ_{ν>μ}x_ν ≤ A_ax plaquettes (box sides 2L, 2L, L, …, L at level k - 1). (F4), (i), (F1): |a_{k-1}(b)| ≤ 1.011A_axε
(S1: A_axε ≤ ½).
(2) *Algebra of one step.* With A := hol_V(γ_x)^†, B' := hol_V(γ_y): U^g(b) = A·[g(c_X)^†hol_U(γ_xbγ_y⁻¹)g(c_{X'})]·B' and
V(b) = A·hol_V(γ_xbγ_y⁻¹)·B', X' the block of y. Hence **||U^g(b) - V(b)|| = ||g(c_X)^†hol_U(π)g(c_{X'}) - hol_V(π)||,
π := γ_xbγ_y⁻¹** (unitary invariance).
(3) *Intra-block links* (X' = X, π a closed loop at c_X). γ_x and γ_y share the moves along axes < μ, differ by one step along
μ, then run parallel: π is spanned by a ladder of ≤ Σ_{ν>μ}|x_ν - c_ν| ≤ (d - 1)h ≤ A_d plaquettes, all in the block. So
||U^g(b) - V(b)|| ≤ ||1 - hol_U(π)|| + ||1 - hol_V(π)|| ≤ A_dε + A_d·max_p||1 - V(p)||.
(4) *Inter-block links* (x on the +μ face of X, y = x + e_μ in X' = X + e_μ =: Y; c the level-(i+1) link (X, Y); the -μ face
is the mirror case). In
coordinates relative to c_X, π = P_<(t)·μ^h·P_>(t)·μ·P_>(t)⁻¹·μ^h·P_<(t)⁻¹ (t the transverse offset, P_≶ the moves along axes ≶ μ).
Deforming P_>μP_>⁻¹ → μ costs a ladder of Σ_{ν>μ}|t_ν| plaquettes and P_<μ^LP_<⁻¹ → μ^L = S_c a ladder of LΣ_{ν<μ}|t_ν|; in all ≤
(d - 1)hL = A_d plaquettes in X ∪ Y. So ||hol_U(π) - hol_U(S_c)|| ≤ A_dε and ||hol_V(π) - hol_V(S_c)|| ≤ A_d·max_p||1 - V(p)||. Next,
hol_V(S_c) = e^{a_c} exactly (W2), and g(c_X)^†U_{i+1}(c)g(c_Y) = e^{a_c}. Finally ||hol_U(S_c) - U_{i+1}(c)|| ≤ ||S_c - M̄_c|| +
||M̄_c - W_0(M̄_c)|| + ||W_0(M̄_c) - U_{i+1}(c)|| ≤ A_dε + 18.4y² + ε, by RS (R1) (each S4' contour differs from S_c by a ribbon of
≤ A_d level-i plaquettes in X ∪ Y, §15.4 step β's sentence), NA-alg (a) applied to S_c⁻¹M̄_c = avg_je^{Y_j}, |Y_j|_HS ≤ y :=
1.011√N·A_dε ≤ 1/20 (left covariance of W_0), and (ii). Under (S2): 18.8NA_d²ε ≤ 1, 18.4y² ≤ ε. So
||U^g(b) - V(b)|| ≤ (2A_d + 2)ε + A_d·max_p||1 - V(p)||.
(5) *Curvature of V.* For a level-i plaquette p, hol_V(p) = e^{v_1}e^{v_2}e^{-v_3}e^{-v_4} with |v_j| ≤ α_{i+1}/L (W1), so by (F5) and
(W3) ||1 - hol_V(p)|| ≤ |(dIa)(p)| + 16α²L⁻²e^{4α/L} ≤ L⁻²[max|da(P')| + 16α²e^{4α}]. For a level-(i+1) cone plaquette P'
(i + 1 ≤ k - 1, so (i) applies), (F5) gives ||e^{da(P')} - U^g_{i+1}(P')|| ≤ 16α²e^{4α}, so ||1 - e^{da(P')}|| ≤ ε + 16α²e^{4α} ≤ ½ and
(|da| ≤ 4α < π) |da(P')| ≤ 1.011(ε + 16α²e^{4α}). Hence **||1 - hol_V(p)|| ≤ L⁻²(1.011ε + 33α²e^{4α}) ≤ 2.02ε/L²** under (S3):
33C_*²ε·e^{4C_*ε} ≤ 1 with α ≤ C_*ε.
(6) *Recursion.* (3)-(5): ||U^g(b) - V(b)|| ≤ Bε. (F3) with ||1 - V(b)|| ≤ α/L and ||1 - U^g(b)|| ≤ α/L + Bε ≤ ½ (S4:
C_*ε/L + Bε ≤ ½): **|a_i(b)| ≤ α_{i+1}/L + 2Bε.** The inherited term enters with coefficient exactly 1/L (W1, F3): this is
the contraction. If α_{i+1} ≤ C_*ε then α_i ≤ C_*ε/L + 2Bε ≤ C_*ε since C_* ≥ 2BL/(L - 1); with (1) as the start,
α_i ≤ C_*ε for 0 ≤ i ≤ k - 1, by induction downward, with the SAME C_* at every level.
(7) *Level k.* For the four links of P: g(c_X)^†U_k(c)g(c_Y) differs from hol_{U^g_{k-1}}(S_c) by ≤ (A_d + 18.4y²/ε + 1)ε ≤ (2A_d + 1)ε
(as in (4)), and ||1 - hol_{U^g_{k-1}}(S_c)|| ≤ L·1.011A_axε by (1), (F2); (F1) gives |a_k| ≤ 1.011(1.011LA_ax + 2A_d + 1)ε ≤ C_Mε.
The plaquettes, kernel terms and residuals are gauge invariant (F6), so (i)-(ii) are unchanged by g. ∎
*Reading.* (CS-F2) is avoided because no gauge is ever chosen on a region whose size grows with depth: the axial gauge is
used on one bounded box (level k - 1) and inside single blocks; across levels the coarse links are SPREAD over the L fine
links of each centre segment (C_I = 1), so the inherited size contracts by 1/L per level, and the per-level cost 2Bε is
a geometric series. The complete axial gauge on the level-0 box instead ADDS the coarse sizes over the levels (h6 C3:
its constant grows 1.5 → 10.2 over depths 1-5 while MSG's stays ≤ 1.8 on the same chains). ε_M is small but fixed
(d = 4, L = 3, N = 2: (S3) is the binding condition, ε_M ≈ 7·10⁻⁶); it is a depth-independent threshold, which is all
CLS-red needs, since CLS-red's η_E is chosen after the constants.
**[RH3-fix, literature pointer 9]** Structurally the closest analogue of MSG is CMP 109 (1.15)-(1.16) (text l.574-590 [read
this session]): Balaban constructs U_n(V) "in the axial gauges" on nested maximal domains Ω_n, with per-scale plaquette bounds
of the form |dU_n - 1| < α_0ξ² (and a J_n bound) on the domain with two boundary layers removed; his input conditions (1.14)
(OCR text: |dU - 1| < α_0ξ, |J| < γ_0 on X) include a sup smoothness condition on J, stronger than MSG's per-level ε
hypothesis.
*Comparison [read-skim: CMP 109 §1, p.260, text l.486-530].* Balaban's background-field regularity is stated through
plaquette variables of the minimiser on the finest lattice (|J| < ε_0, J built from η⁻²·Im of the plaquettes), with the
gauge-fixed fields controlled by the papers [12]-[15] (not read). MSG is our own depth-uniform gauge statement for the soft
chain; Uhlenbeck's small-curvature Coulomb gauge (CMP 83 (1982)) is the continuum template [not-read; no open exposition
consulted this session].

**[RH3-fix S3-2] GAP: Corollary MSG-loc as stated below is NOT proven** (REVIEW_HIST_S3). Step (5)'s quadratic BCH term
33α²e^{4α} was converted into ≤ 1.01ε using α ≤ C_*ε and (S3) with the GLOBAL ε; in the local iteration it is
33α_{cell}(b)²e^{4α}, with α_cell(b) the INHERITED level-(i+1) link size on b's coarse cell, which is not bounded by the local
source ε̂_i(b). **Corollary MSG-loc' (the proven local form; PROVEN-HERE, counted with MSG):** under MSG's hypotheses, for every
level-i cone link b (i ≤ k - 2),
  |a_i(b)| ≤ L⁻¹max_{nearby c}|a_{i+1}(c)| + 2B'ε̂_i(b) + c_q·α_cell(b)²,
  B' := 2A_d + 2 + 1.011A_d/L² (= 21.0), c_q := 2·33A_de^{4C_*ε}/L² (≈ 66 at d = 4, L = 3),
(steps (3)-(6) verbatim, with (5) kept as L⁻²(1.011ε̂ + 33α_cell²e^{4α}) and (F3)'s factor 2; the step-(4) term 18.4y² ≤ ε̂ is
genuinely local since y ∝ ε̂). Iterated, |a_i(b)| ≤ Σ_{j=i}^{k-2}L^{-(j-i)}[2B'ε̂_j + c_qα_{cell,j}²] + L^{-(k-1-i)}1.011A_axε̂_{k-1}. **The
global ε absorbs the quadratic term only in the sup form (MSG itself); in ℓ⁴ (MS-Sob, §20.3) the per-level source
c_qα_{cell,j}² is the non-abelian, d = 4-marginal part of the multi-scale problem**: for a smooth top-scale field
(α_j ≍ θL^{-(k-j)} on ≍ L^{4(k-j)} blocks) it contributes ≍ θ⁴ per level, i.e. k-fold in Σ_jΣ_{level j}α_j⁴. Its control belongs to
(SQ-dev) (§20.3 (A) [RH3-fix S3-4]), not to MSG. Absorbing it instead (α² ≤ C_*εα) changes the contraction to L⁻¹ + c_qC_*ε, which
is not depth-uniform in MS-HLS. *Superseded statement (kept for the record):*
**Corollary MSG-loc (local form): [was: PROVEN-HERE [S3-D] (counted with MSG; same proof)].** Under the hypotheses of MSG (global ε
only in the smallness conditions), for every level-i cone link b,
  |a_i(b)| ≤ Σ_{j=i}^{k-2}L^{-(j-i)}·2B·ε̂_j(b) + L^{-(k-1-i)}·1.011A_ax·ε̂_{k-1},
where ε̂_j(b) is the maximum of the sizes in (i) at levels j, j + 1 and in (ii) at level j + 1 over the level-j and level-(j+1)
objects within level-(j+1) distance 2 of b's level-(j+1) ancestor, and ε̂_{k-1} the maximum over the level-(k-1) box. *Proof.*
Steps (3)-(6) use only the plaquettes, residuals and coarse links of the block pair of b and of the coarse cells touching it;
iterate (6) in the form |a_i(b)| ≤ L⁻¹max_{nearby c}|a_{i+1}(c)| + 2Bε̂_i(b). The neighbourhoods do not grow: a radius r_j in
level-j units becomes ≤ (r_j + 2)/L + 1 ≤ 2 at level j + 1. ∎

### 20.3 What MSG repairs, item by item
**(A) (AE): the gauge part is done; the remainder is a scale-invariant ℓ⁴ bound.**
- **Lemma MS-HLS (multi-scale Hardy-Littlewood-Sobolev bound): PROVEN-HERE [S3-D] (counted).** Let x_j ≥ 0 be functions on
  the level-j blocks of a box (0 ≤ j ≤ J), g_j(b) := L^{-j}x_j(block_j(b)) on level-0 links, h_j := Σ_{level-j blocks}x_j². Then
    **Σ_b(Σ_jg_j(b))⁴ ≤ 24d·S_L·(Σ_jh_j)²,  S_L := Σ_{m≥0}(m + 1)²L^{-m} = (1 + L⁻¹)/(1 - L⁻¹)³** (= 4.5 at L = 3).
  *Proof.* Expand the fourth power over ordered quadruples j_1 ≤ j_2 ≤ j_3 ≤ j_4 (multiplicity ≤ 24). Cauchy-Schwarz:
  Σ_bg_{j_1}g_{j_2}g_{j_3}g_{j_4} ≤ ||g_{j_1}||_2||g_{j_2}||_2||g_{j_3}||_∞||g_{j_4}||_∞, with ||g_j||²_2 = d·L^{4j}·L^{-2j}h_j (d links per
  site, L^{4j} sites per block) and ||g_j||_∞ ≤ L^{-j}√h_j. The product is ≤ d·L^{j_1+j_2-j_3-j_4}√(h_{j_1}h_{j_2}h_{j_3}h_{j_4}) ≤
  d·L^{-m}H√(h_{j_1}h_{j_4}), m := j_4 - j_1, H := Σh. At most (m + 1)² pairs (j_2, j_3) lie between, and Σ_j√(h_jh_{j+m}) ≤ H. ∎
  It is exactly scale invariant (L^{-j} link size against L^{4j} links), so it loses nothing in depth: the discrete
  analogue of ||I_1f||_{L⁴} ≲ ||f||_{L²} in d = 4.
  **[RH3-fix S3-3] The lemma is stated for d = 4** ("L^{4j} sites per block"). In general d a block has L^{dj} sites and the
  product acquires L^{(d-4)(j_1+j_2)/2}, so it is scale invariant only at d = 4, the critical case it is for. *Application
  constants:* MSG-loc's ε̂_j is a maximum over a radius-2 neighbourhood of b's level-(j+1) ancestor (converting Σ(max over the
  neighbourhood)² to Σ(local)² costs 5^d = 625), and indexing x_j on level-(j+1) blocks costs L^d in ||g_j||²_2; both are
  depth-uniform and go into C_Q (the formula C_S = 24dS_L(2B)⁴C_Q² below omitted them).
- **(MS-Sob) [OPEN; P].** In the MSG gauge, for each level i < k: Σ_{level-i cone links}|a_i(b)|⁴_HS ≤ C_S·E_𝒞(P)², C_S
  depth-uniform.
- **[RH3-fix S3-4] Re-labelled: MS-Sob ⇐ MSG-loc-dev [OPEN] + MS-HLS [PROVEN] + (SQ-dev) [OPEN]: ARGUED** (the HLS step proven;
  the deviation localisation only sketched in the next bullets). **MSG-loc-dev** (the deviation-source localisation of the
  gauge, OPEN): |a_i(b) - (Ia_{i+1})(b)| ≤ C·(local deviation sizes + residuals + (deviation × size) terms), the sources being
  those of the corrected (SQ) below; MSG's steps (3)-(4) bound hol_U(π) - hol_V(π) through plaquette SIZES (lasso) and the RS
  ribbons of step (4) are curvature-sized, so MSG does not give it. **(SQ-dev)** := the corrected (SQ) below, including the
  quadratic BCH sources c_qα_{cell}² of MSG-loc' [RH3-fix S3-2]. The OPEN wall is the single item "(SQ-dev) incl. MSG-loc-dev".
  The curvature-source implication below is kept only as a remark: **valid but vacuous, its premise is false** (next bullet).
  *Original (superseded) bullet:*
- **MS-Sob ⇐ MSG-loc + MS-HLS + (SQ): [was CONDITIONAL [S3-D]; now a vacuous remark, RH3-fix S3-4] (implication PROVEN).** MSG-loc bounds |a_i| by Σ_jg_j with
  x_j = 2Bε̂_j; MS-HLS gives Σ|a_i|⁴ ≤ 24dS_L(2B)⁴(Σ_jh_j)² (the top term is one more j); so (MS-Sob) holds with
  C_S = 24dS_L(2B)⁴C_Q² as soon as
  **(SQ) [OPEN; P] (square-function bound):** Σ_{j≥i}Σ_{level-j blocks}x̂_j² ≤ C_Q·E_𝒞(P), with x̂_j the local SOURCE sizes of
  MSG-loc. ∎
- **(SQ) is false with curvature sources (a k-fold loss), true-in-kind only with deviation sources** [the example is
  PROVEN-HERE, elementary; the corrected (SQ) is OPEN]. For a field smooth at the top scale with top curvature θ, every level
  j carries Σ_{level-j cone plaquettes}|log U_j(p)|² ≈ c·θ² (flux θL^{-2(k-j)} on ≍ L^{4(k-j)} plaquettes) while E_𝒞(P) ≍ θ²:
  with ε̂_j = local plaquette sizes, Σ_jh_j ≍ kθ² ≍ k·E. This is the d = 4 marginality of §15.5 in its sharpest form. In MSG's
  proof the sources that actually enter are the DEVIATIONS: in step (3)-(4), hol_U(π) - hol_V(π) is controlled by
  Σ_{p∈S}(log U^g_i(p) - log V(p)) plus terms quadratic in link sizes, and log V(p) ≈ L⁻²·W_2(log U_{i+1}) is the interpolated
  coarse curvature. The correct (SQ) has x̂_j := local sizes of [log U_j^g(p) - L⁻²W_2(log U^g_{j+1})(p)] + residuals + α·(local
  link deviations), and its linear case is a Littlewood-Paley square-function estimate for the pair (Q_2, I_2) (block
  plaquette average and its Whitney interpolation; (1 - I_2Q_2) kills constants, so Σ_j|ψ(L^jξ)|² ≤ C on the symbol side)
  [ARGUED, not proven here].
- **(AE)'s restatement with the energy cap** (harmless for CLS-red, whose step γ applies (AE) only when E_𝒞(P) < η_E): add
  hypothesis (iii) E_𝒞(P) ≤ η_AE.
- **(AE) ⇐ MSG + (MS-Sob): ARGUED [S3-D]** (proof written at the level of every error term; constants C_e, C' named, not
  all computed). In the MSG gauge (|a_i| ≤ C_Mε):
  (1) exact linear recursion a_{i+1} = Qa_i + e_i - ρ̃_i on cone links, ρ̃_i := -log(W_0(M̄_c)⁻¹U_{i+1}(c)) the residual log, e_i the
  error; (2) |e_i(c)| ≤ C_e(m_i(c)² + m_i(c)|ρ̃_i(c)|), m_i(c) := max|a_i| over the contour links of c, from (F5)+(F3) on each
  contour, NA-alg (a) about 1 (|X_0 - Ȳ| ≤ 9.2y²) and the first BCH commutator of log(W_0e^{-ρ̃}); (3) E-loc's steps (1)-(5) are
  linear identities and apply verbatim to a_k = Q^ka_0 + ΣQ^{k-1-i}(e_i - ρ̃_i); (4) level 0: da_0(p) = log U_0^g(p) + R_p,
  |R_p| ≤ C·m_0(p)², and the averaged square fluxes give |n⁻⁴Σ_yΣ_{p∈sq_y}R_p| ≤ n⁻²Σ_{R_0}|R_p| ≤ 2C(Σ_{cone}|a_0|⁴)^{1/2} ≤
  2C√C_S·E (|R_0| ≤ 4n⁴); (5) depth m sources: |d(Q^me_i)(P)| ≤ √8L^{-m}||e_i||_{ℓ²(R'_i)} ≤ √8L^{-m}C(√C_S·E + C_Mε√(Σρ̃²)), summable;
  (6) residuals: |ρ̃_c| ≤ √(4Nφ_c) + 73.6Ny² (KQ dichotomy, §15.4 β), the y² part joining (2); (7) top: |log U_k^g(P) -
  da_k(P)| ≤ C·m_k² and, by MSG-loc at level k and (AE) at depth k - 1 for the bounded set of level-(k-1) plaquettes and
  residuals that bound a_k, m_k ≤ C√E_𝒞(P) (induction on depth; the inherited constant enters multiplied by ε). Collecting:
  |log U_k(P)|_HS ≤ √(C_locN·E)(1 + Cε) + C(√C_S·√η_AE + ε)√E, i.e. **(AE) with C'_AE := 2C_locN** for ε, η_AE small. (The
  linear constant C_locN = 80 at N = 2; h6 A: R_NA ≤ 16.0005 on the coherent adversarial chain, whose linear value is 16.)
- **[RH3-fix S3-4] Net status of (AE) (corrected):** OPEN. (AE) ⇐[ARGUED; promoted to PROVEN-conditional in §26] MSG [PROVEN] +
  (MS-Sob); (MS-Sob) ⇐[ARGUED] MSG-loc-dev [OPEN] + MS-HLS [PROVEN] + (SQ-dev) [OPEN]. The wall is "the square function of the
  deviations" TOGETHER WITH the deviation localisation of the gauge (one wall). *Original line:*
- **Net status of (AE):** OPEN, reduced: (AE) ⇐[ARGUED] MSG [PROVEN] + (MS-Sob) ⇐[PROVEN] (SQ) [OPEN]. The wall has moved
  from "the gauge on the cone" (CS-F2) to "the scale-invariant square function of the deviations" (SQ), the genuinely
  d = 4-critical step.

**(B) CLS-red and the cone-local CLS-sf (lead's note).**
- CLS-red stands as CONDITIONAL ⇐ (AE) (restated (AE), §15.3/§15.4 [RH2-fix]). Its conclusion is already pointwise per cone.
- **Corollary CLS-cone (cone-local CLS-sf, per defect): CONDITIONAL [S3-D] ⇐ (AE).** Put C_cone := max{C'_AE/(2N), 2/η_E}
  (CLS-red's constants; depth-uniform). For every k ≤ K, every chain, every level-k field and every level-k plaquette P:
    **s(U_k(P)) ≤ C_cone·E_𝒞(P).**
  (a) *Level-k defect* (RLARGE (R3)'s ||1 - V_P|| ≥ ε_1): since s(V) = ||1 - V||²_HS/(2N) ≥ ||1 - V||²/(2N),
     **E_𝒞(P) ≥ ε_1²/(2N·C_cone).**
  (b) *RLARGE's fine threshold* η_1 = min{ε_1/(2L²), ε_1²/(512N·A_d(L))} (= min{ε_1/18, ε_1²/(4608N)} at d = 4, L = 3): any level-i
     plaquette p (1 ≤ i ≤ k) of the chain with ||1 - U_i(p)|| ≥ η_1 has **E_𝒞(p) ≥ η_1²/(2N·C_cone)**, its cone 𝒞(p) ⊂ 𝒞(P) for
     p inside W_P^{(i)} (nesting); at i = 0, E_𝒞(p) ≥ s(U_0(p)) ≥ η_1²/(2N) directly (the (R5) branch).
  (c) *Defect by defect.* For any set D of level-k plaquettes and any set T of chain terms containing ∪_{P∈D}𝒞(P), the
     terms of T have energy ≥ (1/24)Σ_{P∈D}E_𝒞(P) ≥ |D|·ε_1²/(48N·C_cone) on (a)-defects (overlap ≤ 24, §15.1). The price is
     paid by the cone's own terms, at every depth, so it can be entered into ℒ_𝔥 defect by defect.
     **[RH3-fix S3-5] Scope: "defect by defect" is proven only for defects at ONE level.** Cones of plaquettes at different
     levels nest, so a chain term lies in ≤ 24 cones at EACH level. Stated forms:
     - (c1) *single level:* D ⊂ level-k plaquettes: Σ_{T} ≥ (1/24)Σ_{P∈D}E_𝒞(P) (as above);
     - (c2) *one-step re-seeding (RLARGE (R3)'s branch "a level-(k-1) plaquette p ⊂ U_4(P) with ||1 - U_p|| ≥ η_1"):* the map
       P ↦ p is ≤ 24-to-1 (P must have p's block among its corners), so the finer-cone charges cost a factor 24·24 = 576:
       Σ_T ≥ (1/576)Σ_{P∈D}E_𝒞(p(P));
     - (c3) *multi-level:* a defect set spread over k levels gets only (24k)⁻¹ unless the selection makes the cones disjoint
       (one price per footprint, as §7.2's disjoint shadows do); without that, the price is k-fold diluted.
     **Size of the price (remark).** ε_AE ≤ ε_M ≈ 7·10⁻⁶ forces η_E ≤ η_AE ≲ ε_M²/C'_AE (§26: ≈ 3·10⁻¹³), so **C_cone ≥ 2/η_E ≳
     10¹²** and the per-defect price u_kε_1²/(2NC_cone) is ≳ u_kε_1²·10⁻¹³ only: depth-uniform, enough for a proof, but RLARGE must
     then take g² ≪ ε_1²·10⁻¹³ wherever this price has to beat per-defect entropy (to be recorded by RLARGE when it consumes
     CLS-cone; RLARGE.md not edited).
  For the minimiser chain (𝓔_k, 𝓔^Λ_k below) this is CLS-sf in cone form: 𝓔^Λ_k(V) ≥ (1/24)Σ_{P: 𝒞(P)⊂𝒞(Λ)}E_𝒞(P) ≥
  (1/(24C_cone))Σs(V_P). *Proof.* CLS-red (δ) is the displayed inequality; (a)-(c) are the conversions stated. ∎

**(C) (I_k^E) repaired: (I_k^E)' [HYPOTHESIS, P].** As §14.1 with (a), (b), (d) replaced as follows ((c) unchanged).
- **(a') Localised main term, defined without global smallness.** 𝒞(Λ_k) := the chain terms all of whose vertices have
  level-k ancestors in Λ_k (free boundary); **𝓔^Λ_k(U) := inf{Σ_{terms∈𝒞(Λ_k)} : chains with level-k field U on Λ_k}**; main
  term u_k𝓔^Λ_k(U). *Elementary facts (PROVEN-HERE, not counted):* (1) defined and attained for every U (a continuous function
  on a compact group power), depends only on U on the links of Λ_k, gauge invariant, coarse translation/B_4 covariant; for
  Λ_k = the torus it is 𝓔_k; (2) superadditivity: Λ ∩ Λ' = ∅ ⇒ 𝓔^{Λ∪Λ'} ≥ 𝓔^Λ + 𝓔^{Λ'} (disjoint term sets; straddling terms
  ≥ 0 dropped), in particular 𝓔_k ≥ 𝓔^{Λ_k}_k + 𝓔^{Ω^c_k}_k; (3) CLS-cone applies inside Λ_k (CONDITIONAL ⇐ (AE)); (4) (c5)
  in localised form: if the level-k descendants of Λ_{k+1} lie in Λ_k, then min_{U_k}[𝓔^{Λ_k}_k(U_k) + κΦ_k^{Λ_{k+1}}(U_k, V)] ≥
  𝓔^{Λ_{k+1}}_{k+1}(V) (drop the terms outside 𝒞(Λ_{k+1})), with equality for the global tower; the defect is supported on the
  terms over Λ_k ∖ desc(Λ_{k+1}). *Term-to-cube assignment:* each term goes to the level-k cube of the level-k ancestor of its
  lexicographically first vertex; 𝓔^Λ_{k,x} := the assigned terms of a minimiser chosen by a measurable selection (the
  argmin correspondence is compact-valued and upper hemicontinuous; Kuratowski-Ryll-Nardzewski). *Hypothesis items
  (not proven):* (a3) 0 ≤ 𝓔^Λ_{k,x} ≤ C_𝓔 for U small-field near x (needs an upper-bound construction below a level-k
  small field); (a4) β[𝓔^Λ_k] = 1 in the bulk and the boundary defect of (2)/(4) is supported within distance R_b of Ω^c_k
  up to e^{-κ_pR} tails, so that it is carried by the boundary factor (B_0, ℒ_𝔥; RLARGE §8.1), NOT by the bulk polymers
  (by (c3), a β = 0 tree term may not enter a per-cube-bounded polymer) [ARGUED: needs (SF-bg) in local form; MSG is the
  depth-uniform chart gauge in which FLOW's near-trivial (SF-bg) can be applied on the cone over each bounded level-k chart,
  once the minimiser chain there is every-level ε-small (ε-regularity, CLS-red steps α-β, ⇐ (AE))]. (c4) is unchanged with
  𝓔^Λ: δβΣs = δβ𝓔^Λ_k + δβ(Σs - 𝓔^Λ_k), the first the coupling shift u_k → u_k - δβ (given (a4)), the second ≤
  |δβ|(12L⁸ + L⁴C_𝓔) per cube (given (a3)).
- **[RH3-fix S3-6] (a') has a hole: it is an infimum over REAL chains, so it has no analytic continuation, and its measurable
  per-cube selection is not even continuous where minimisers are non-unique; (b') needs the polymers, hence the main term,
  analytic on 𝔇_α. Repaired by item (a5) and the analytic main term of §25.**
- **[RH3-fix S3-7] Notation error in (b') below: "U = V_be^{iZ_b}, Z_b ∈ i·su(N) (Hermitian traceless)" is UNITARY (iZ_b is
  anti-Hermitian), so as written 𝔇_α(X) has no complex points. Read U = V_be^{H_b}, H_b ∈ i·su(N) Hermitian traceless
  (equivalently e^{iZ_b} with Z_b ∈ su(N)); facts (1)-(4) hold verbatim with this reading (fact (4) already uses it). The
  corrected domain, with its chart (sl(N, ℂ)) form, is (b'') of §25.**
- **(b') Gauge-covariant domain containing the ε_1-domain on every polymer.** 𝔇_α(X) := {U = (V_be^{iZ_b})_{b⊂X} : V ∈ SU(N)^X
  with ||1 - V_p|| ≤ 2ε_1 for every level-k plaquette p ⊂ X; Z_b ∈ i·su(N) (Hermitian traceless), |Z_b| ≤ α_E}. *Elementary
  facts (PROVEN-HERE, not counted):* (1) (V, Z) ↦ Ve^{iZ} is the polar decomposition, a real-analytic diffeomorphism
  SU(N) × i·su(N) → SL(N, ℂ) (Cartan; standard), so 𝔇_α(X) is a complex thickening of a real set; (2) gauge covariant:
  g_xVe^{iZ}g_y⁻¹ = (g_xVg_y⁻¹)·e^{ig_yZg_y⁻¹}, and |Z| and the plaquette condition are invariant; (3) its real points include
  the whole ε_1-domain on X **for every polymer, of any size**: no gauge is chosen, so Stokes (GAP S2-2) does not apply;
  (4) Cauchy estimates: at a real U in the ε_1-domain and real directions Y_b ∈ su(N), the polydisc {(U_be^{w_bY_b}) : |w_b| ≤ r}
  lies in 𝔇_α(X) when r·max|Y_b| ≤ min{α_E, ε_1/4}, because U_be^{(s+it)Y_b} = (U_be^{sY_b})e^{itY_b} exactly (Y_b commutes with
  itself) and a real change of the four links of a plaquette by ≤ r|Y| moves it by ≤ 4r|Y| ≤ ε_1. So C³ bounds of the
  polymers at real points of the ε_1-domain follow from the sup over 𝔇_α(X) with radius ≍ min{α_E, ε_1}, uniformly in |X|.
  (b) is restated with this 𝔇_α(X). On a bounded chart in axial gauge, 𝔇_α and the chart polydisc contain each other up to
  constant factors in the radii [ARGUED, via (1)]; this is the form in which Balaban extends his effective-action terms to
  G^c-valued "regular" configurations (CMP 109 p.261, text l.523-530 [read-skim]; the conditions (3.35)-(3.38) of his [13]
  not read). MSG is NOT needed for (b'): it concerns the level-k field only.
- **(d') Two-field form, completed (GAP S2-3).** Add to (d)'s list: the kernel normalisation -Σ_clog∫e^{-κu_kφ_{M̄_c(U_k)}}, a
  function of U_k, (b')-class with E_0, not β-free; it feeds Γ_k's 𝒩'_1 term and hence u_{k+1} in (c5). **[RH3-fix, review
  Priority 5 note]** Its field-independent part, -((N² - 1)/2)log(κu_k) per link, is a c-number and goes to 𝒱_k, so E_0 stays
  g-independent.
- **Status.** (I_k^E)' is a HYPOTHESIS with its three statement GAPs repaired at the statement level; its new hypothesis items
  are (a3), (a4) (localised tower: upper bound and boundary locality). Target S5's "not success" clause (a domain that needs
  one gauge on large polymers) is avoided by (b').

## 21. Check h6 (criteria first: checks/h6_criteria.md 01:01:44 UTC; script checks/h6_msg_cone.py; records h6_out.txt, h6_time.txt)
Pre-run (disclosed): two crash fixes to the script (directions with no cone links at level k; a safe max on empty arrays)
and one smoke run of a REDUCED scratch copy (3 samples, 3 t values, d = 2 depths ≤ 2; scratchpad h6smoke/, 01:13:01 UTC);
no criterion edited. Official run 01:13:48-01:16:21 UTC under the numeric lock (load 3.6, 39% free, nice 10, BLAS threads 1,
153 s, peak RSS 729 MB). **OVERALL: FAIL as pre-registered (A2, A3); A1, B1, B2, B3, C1, C2, C3 PASS.**
- **A1 PASS.** R_NA ≤ 80 everywhere; max R_NA = 16.0005 (coherent top residuals; linear value exactly 16 = 8N), 0.057
  (smooth), 0.035 (residuals), ≈ 0 (noise: aggregate cone energy).
- **A2 FAIL, A3 FAIL (one sample).** Smooth seed 2: D(0.0025) = 0.216, D(t) non-monotone (slope -0.31). All other nine
  samples PASS both (slopes 0.77-1.58; coherent: slope 2.00). The failing sample has a near-cancelling top flux (R_lin =
  6.6·10⁻⁴), so the RELATIVE deviation |R_NA/R_lin - 1| is a ratio of an O(t) correction to a small number; the criterion
  did not anticipate this.
- **B1, B2, B3 PASS.** The MSG gauge leaves every s and φ invariant to ≤ 9.2·10⁻¹⁵ (the chain-gauge structure F6);
  hol_V(S_c) = e^{a_c} to 3.3·10⁻¹⁶ and |Ia| ≤ max|a|/L (W1, W2); **max C_meas = 3.53** over all samples and t (proof's C_M =
  66.1, criterion 450). Per level at t = 0.01 (the nine non-coherent samples): max|log U_0^g|/ε ∈ [0.54, 1.46], level 1 ∈ [1.14, 2.31], level 2 ∈ [0.31, 3.42];
  max|a_0| - max|a_1|/L ≤ 1.08ε (the measured per-step cost, against the proof's 2B = 44).
- **C1, C2, C3 PASS (d = 2, depths 1-5).** max C_meas: 8.03 (k = 1), 8.43 (k = 2), 8.60, 8.65, 8.66 (k = 5): depth-uniform
  (the maximum is the smooth family's top-level axial links; the noise family stays in [1.0, 1.8]). Complete axial gauge on
  the level-0 box, noise family: 1.51/1.36 (k = 1) → 9.03/10.18 (k = 5), ratio to MSG 5.5 and 6.7 at k = 5: the additive growth
  MSG avoids.
- **h6b (POST HOC diagnostic, written after A2/A3 failed; not a criterion change; checks/h6b_diag.py, h6b_out.txt).** Run
  01:16:56 UTC under the lock (17 s, 642 MB). Smooth seeds 1-3, t = 10⁻⁴ … 10⁻²: the ADDITIVE error |log U_2(P) - dB_2(P)|_HS/√E
  scales as t^{1.017}, t^{0.998}, t^{1.005} with constants 0.64, 1.34, 2.65 (stable to 3 digits over two decades); for seed 2,
  D_rel → 0 linearly (9.3·10⁻³ at t = 10⁻⁴). So the failure is the near-cancellation artefact of the relative criterion; the
  additive error, which is the form (AE)'s proof uses (|X| ≤ |dB| + Cε√E), is linear in the field scale. Post hoc reading;
  the A2/A3 FAIL stands as recorded.

## 22. Outcomes against the session-3 targets (§19) (ADDED AFTER the derivations; pointers only)
- **Target S4 (MSG): MET.** Theorem MSG PROVEN-HERE with explicit constants (C_M = 66.1, d = 4, L = 3), depth-uniform; local
  form MSG-loc. No global small gauge is used. Checked (h6 B, C; measured constants 3.5 at d = 4 depth 2 and ≤ 8.7 at d = 2
  depths 1-5, flat in depth).
- **Target S5: MET in the reduction form.** (AE): OPEN, reduced to (SQ) via (AE) ⇐[ARGUED] MSG + (MS-Sob) ⇐[PROVEN, with the
  new Lemma MS-HLS] (SQ); the curvature-source (SQ) is shown false by a factor k, so the correct remainder is the deviation
  square function. (I_k^E)': GAPs S2-1, S2-2, S2-3 repaired at the statement level; MSG is used for (a4) (chart gauge for the
  localised tower) and not needed for (b'). CLS-red restated; Corollary CLS-cone gives CLS-sf in cone-local, per-defect form
  with RLARGE's η_1 (lead's note). "Not success" clauses: avoided (no per-level constant iterated; no single gauge on large
  polymers).
- **h6: OVERALL FAIL as pre-registered (A2/A3, one near-cancelling sample)**; the post-hoc h6b reading is labelled.
- **[RH3-fix S3-1..S3-4] Corrected (REVIEW_HIST_S3):** S4 MET with S3-1 (axial order / A_ax = 12; C_M unchanged); MSG-loc GAP,
  MSG-loc' (with c_qα²) proven; S5 MET in reduction form with fixes, except that the chain to (SQ) is ARGUED, not proven:
  (MS-Sob) ⇐[ARGUED] MSG-loc-dev [OPEN] + MS-HLS + (SQ-dev) [OPEN].

## 23. Tally (session 3) and hypotheses consumed
- **Session-3 items.** PROVEN-HERE, counted (2): Theorem MSG (with Corollary MSG-loc); Lemma MS-HLS. CONDITIONAL (2):
  MS-Sob ⇐ (SQ); Corollary CLS-cone ⇐ (AE). ARGUED (1): (AE) ⇐ MSG + (MS-Sob). OPEN, new (1): (SQ) [P]. HYPOTHESIS: (I_k^E)'
  replaces (I_k^E) (statement GAPs repaired; new items (a3), (a4)). PROVEN-HERE, not counted: §20.0 facts; Whitney (W1)-(W3);
  (a') (1), (2), (4); (b') (1)-(4); the k-fold counterexample to curvature-source (SQ).
- **Whole file after session 3 (unreviewed for session-3 items): 9 PROVEN-HERE / 5 CONDITIONAL / 7 ARGUED / 4 OPEN + 1
  HYPOTHESIS.** PROVEN-HERE: PM, RS-lin, CL^J, R1^J, H-geo, HF, E-loc, MSG, MS-HLS. CONDITIONAL: RS-joint, HIST-sum, CLS-red,
  MS-Sob⇐SQ, CLS-cone. OPEN: (AE) (reduced to (SQ)), (SQ), (D1-b), (H-w). HYPOTHESIS: (I_k^E)'.
- **[RH3-fix S3-4] Corrected tally (REVIEW_HIST_S3; supersedes the two bullets above).** Session 3: **2 PROVEN-HERE** (MSG with
  MSG-loc'; MS-HLS) **/ 1 CONDITIONAL** (CLS-cone ⇐ (AE)) **/ 2 ARGUED** ((AE) ⇐ MSG + MS-Sob; MS-Sob ⇐ MSG-loc-dev + MS-HLS +
  SQ-dev) **/ 1 OPEN** ((SQ-dev) incl. MSG-loc-dev) **+ HYPOTHESIS** (I_k^E)' (replaces). **Whole file after session 3: 9
  PROVEN-HERE / 4 CONDITIONAL / 8 ARGUED / 4 OPEN + 1 HYPOTHESIS.** CONDITIONAL: RS-joint, HIST-sum, CLS-red, CLS-cone. OPEN:
  (AE), (SQ-dev), (D1-b), (H-w). (The curvature-source "MS-Sob ⇐ (SQ)" is a vacuous remark, not counted.)
- **Hypotheses consumed.** MSG: RS (R1) ribbon bound (RLARGE, A_d), NA-alg (a) (PROOF), S4' root covariance (LINEAR_PACKAGE
  §1.2); Whitney-form commutation (standard). MS-HLS: none. MS-Sob ⇐ (SQ): MSG-loc, MS-HLS. (AE) ⇐ MSG + MS-Sob: E-loc, KQ,
  NA-alg (a), A1-NA(1) step 6, (AE) at lower depth (induction). CLS-cone: CLS-red ⇐ (AE). (I_k^E)': (SF-bg) local form for
  (a4); polar decomposition (standard) for (b').
- Proposed edit for FLOW (not made): §14.2 [RH2-fix 10]. No change to PROOF.md; nothing outside HIST.md, HIST_LOG.md,
  checks/h* edited. No commits, PRs, pushes.

# Session 4 of lane D (2026-10-28)

## 24. Session-4 pre-stated targets (written 2026-10-28 01:52 UTC, after STEP 1's [RH3-fix] edits and after exploratory reasoning, BEFORE any written session-4 derivation (§25 onward) and before any h7 criteria file or script; not edited after the derivations start)

### Target S6: an analytic main term and a genuine complex domain for (I_k^E) ("(I_k^E)''")
- **(a5) to deliver.** Replace the real infimum 𝓔^Λ_k on the small-field part by an object that is holomorphic on the
  complex domain: the critical value of the holomorphically continued chain energy at a critical chain obtained by the
  implicit function theorem (NA-IFT; analyticity inputs in the style of N5-an), in MSG-type / left-trivialised charts.
  Pieces to prove or reduce: (1) every chain energy term (s and κφ, φ built with the SU(N) maximiser W_0) has an explicit
  holomorphic continuation on a chart-free, gauge-covariant complex domain, with explicit bounds; (2) the critical value is
  gauge invariant, independent of the base point used, and holomorphic with a depth-uniform radius, given a precisely stated
  linear-analytic input; (3) on real small fields it equals the infimum 𝓔^Λ_k, with every hypothesis named.
- **Domain to deliver.** U = V e^{H} (H Hermitian traceless) in chart-free form, and the sl(N, ℂ) chart form U = U^r e^{Z},
  Z = X + iY ∈ sl(N, ℂ), |Y| small (a genuine polydisc around real points, in left-trivialised or MSG coordinates), with the
  two forms compared by explicit constants.
- **Consistency to check.** Lemma HF (the φ- vs k̃-towers) on the complex domain; FLOW Lemma F-tree / β[𝓔_k] = 1 (unchanged by
  the redefinition?); RLARGE v2 (RLF-5) and Conflict K7 (one gauge-covariant complex domain; width).
- **Success:** (I_k^E)'' stated, with (a5) either proven or reduced to named hypotheses whose class is identified (which
  PROOF/FLOW node owns each). **Not success:** an "analytic main term" whose radius depends on depth or polymer size, or an
  agreement claim with an unnamed uniqueness step.

### Target S7: (AE) ⇐ MSG + (MS-Sob), written fully
- Promote the §20.3 ARGUED chain to a PROVEN implication conditional on (MS-Sob) (stated precisely, as a hypothesis on the
  canonical MSG gauge), with every error term bounded, the depth induction written, and the closing inequality explicit:
  √(C_locN)(1 + δ) + C√η_AE ≤ √C'_AE with C'_AE = 2C_locN fixed BEFORE η_AE is chosen. Record ε_AE, η_AE, C_cone numerically.
- **Not success:** a constant that is iterated per level, or a use of MSG-loc (GAP) beyond a bounded box.

### Check h7 (criteria first: checks/h7_criteria.md, then the script)
- **h7 A** (SU(2), SU(3)): the holomorphic continuation of NA-alg (a)'s fixed point and of φ on complex data: agreement with
  the real construction on real data, the complex stationarity identity, the bound |X_0 - Ȳ| ≤ 9.2y² at complex data, and
  holomorphy (complex-linear finite differences).
- **h7 B:** the polar/chart comparison (|H| against |Y| for U = e^{X+iY}).
- **h7 C:** the arithmetic of §26's constants (closing inequality, η_AE, C_cone), computed from the displayed formulas.

# Session-4 derivations (written after §24)

## 25. Step 2: (I_k^E)'', an analytic main term on a genuine complex domain

### 25.0 Notation
sl(N, ℂ) = su(N) ⊕ i·su(N); for Z ∈ sl(N, ℂ), X := (Z - Z*)/2 ∈ su(N) and iY := (Z + Z*)/2 ∈ i·su(N) are its real and
imaginary parts (Z = X + iY), ||X||, ||Y|| ≤ ||Z||. ||·|| is the operator norm, |·| the HS norm. Only SU(N) gauges act. For a set
X of level-k links: R_ε(X) := {V ∈ SU(N)^X : ||1 - V_p|| ≤ ε for every level-k plaquette p ⊂ X} (gauge invariant); the
left-trivialised polydisc about a real U^r is **P_r(U^r) := {(U^r_be^{Z_b})_b : Z_b ∈ sl(N, ℂ), ||Z_b|| ≤ r}**; the polar domain
([RH3-fix S3-7] reading) is **𝔇_{ε,α}(X) := {(V_be^{H_b})_b : V ∈ R_ε(X), H_b ∈ i·su(N), ||H_b|| ≤ α}.** The real points of
P_r(U^r) (r ≤ 1/8) are exactly {U^re^{X} : X ∈ su(N)^X, ||X_b|| ≤ r} (e^Z unitary and ||Z|| ≤ 1/8 force Z ∈ su(N)).

### 25.1 Lemma TERM-an (the chain energy terms continue holomorphically to a chart-free domain): PROVEN-HERE [S4-D] (counted)
**(i) Plaquette term.** s^ℂ(U) := 1 - (tr U + tr U⁻¹)/(2N) is entire on SL(N, ℂ), equals s on SU(N) (U⁻¹ = U*), and is invariant
under conjugation; on P_r about a real plaquette, |s^ℂ| ≤ 1 + e^{4r}.
**(ii) Maximiser.** Let Y_1, …, Y_m ∈ sl(N, ℂ), |Y_j| ≤ y ≤ 1/20, w_j ≥ 0, Σw_j = 1, Ȳ := Σw_jY_j, M := Σw_je^{Y_j}, M̌ := Σw_je^{-Y_j},
and for X ∈ sl(N, ℂ): K(X) := e^{-X}M - 1 - (Ȳ - X), Ǩ(X) := M̌e^{X} - 1 - (X - Ȳ), Π_0(Z) := Z - N⁻¹tr(Z)·1,
  **Φ^ℂ(X) := Ȳ + Π_0(½(K(X) - Ǩ(X))).**
Then Φ^ℂ maps B^ℂ := {X ∈ sl(N, ℂ) : |X| ≤ 3y} into itself with Lip ≤ 4.5y ≤ 0.23; its fixed point X_0^ℂ(Y) is holomorphic in
(Y_j) on {|Y_j| < 1/20}; |X_0^ℂ - Ȳ| ≤ 9.2y²; with G := e^{-X_0}M, Ǧ := M̌e^{X_0} it solves the holomorphic stationarity
**Π_0(G - Ǧ) = 0**, and |G - 1|, |Ǧ - 1| ≤ 18.4y², |(G - 1) + (Ǧ - 1)| = |K + Ǩ| ≤ 18.3y²; for Y_j ∈ su(N), X_0^ℂ is NA-alg (a)'s X_0
(W_0 = e^{X_0} the unique SU(N) maximiser of Re tr(W⁻¹M)).
**(iii) Kernel term.** Let c be a level-(i+1) link, S := S_c its straight centre transporter, T_j (weights w_j) its S4' contour
transporters, all products of (possibly complex) chain links. On D_c(y_0) := {|log(S⁻¹T_j)| ≤ y_0 ∀j} (y_0 ≤ 1/20, log the
series) put Y_j := log(S⁻¹T_j) (traceless: det = 1 and |tr Y_j| < 2π), A := Σw_je^{Y_j} = S⁻¹M̄_c, Ǎ := Σw_je^{-Y_j},
W_0^ℂ := Se^{X_0^ℂ(Y)} ∈ SL(N, ℂ), and for V ∈ SL(N, ℂ), V' := S⁻¹V,
  **φ^ℂ_c(V) := (1/2N)[tr(e^{-X_0}A) + tr(Ǎe^{X_0}) - tr(V'⁻¹A) - tr(ǍV')].**
It is holomorphic in (links, V) on D_c(y_0) × SL(N, ℂ), entire in V, equal to φ_{M̄_c}(V) on real chains, and invariant under
SU(N) chain gauges (F6). Two expansions hold, with y := max_j|Y_j|:
- (local) for V = W_0^ℂe^{-ρ}, ρ ∈ sl(N, ℂ): **|φ^ℂ_c(V) + tr(ρ²)/(2N)| ≤ 4.6y²|ρ|²/N + e^{4y+|ρ|}|ρ|³/(6√N);**
- (global Haar-shift form) for V'' ∈ SU(N): **φ^ℂ_c(W_0^ℂV'') = s(V'') + Δ(V''), |Δ(V'')| ≤ θ·s(V''), θ := 18.4y²(2 + 2c_N),**
  c_N := max{π³/24, N/r_N²}, r_N := min{1, 4/√N} (c_2 = 2, c_3 = 3).
*Proof.* (i) is immediate. (ii) *Expansion.* e^{-X}M = (1 - X + R_X)(1 + Ȳ + E) = 1 + (Ȳ - X) + K(X) with K = R_X + E + (R_X - X)(Ȳ + E)
(NA-alg's identity), and M̌e^{X} = (1 - Ȳ + Ě)(1 + X + Ř_X) = 1 + (X - Ȳ) + Ǩ(X) with Ǩ = Ř_X + Ě + (Ě - Ȳ)(X + Ř_X), Ř_X :=
e^X - 1 - X, Ě := Σw_j(e^{-Y_j} - 1 + Y_j). NA-alg (a)'s norm bounds use only submultiplicativity of |·| and the exponential
series, so they hold verbatim for complex arguments: on B^ℂ, |R_X|, |Ř_X| ≤ 5.23y², |E|, |Ě| ≤ 0.53y², |K|, |Ǩ| ≤ 9.11y², and the
Lipschitz bounds (e^{3y} - 1 ≤ 3.24y; (1 + 3.24y)(1.03y)) give Lip(K), Lip(Ǩ) ≤ 4.5y. Π_0 is the HS-orthogonal projection onto
traceless matrices (norm 1), so |Φ^ℂ(X) - Ȳ| ≤ ½(|K| + |Ǩ|) ≤ 9.11y², |Φ^ℂ(X)| ≤ y + 9.2y² ≤ 3y, Lip(Φ^ℂ) ≤ 4.5y ≤ 0.23. Banach's
fixed point theorem on B^ℂ. *Holomorphy:* the iterates (Φ^ℂ)^n(Ȳ) are holomorphic in (Y_j) and converge uniformly (rate 0.23),
so the limit is holomorphic (Weierstrass). *Stationarity:* ½(G - Ǧ) = (Ȳ - X_0) + ½(K - Ǩ) and Ȳ - X_0 is traceless, so the
fixed-point equation is Π_0(½(G - Ǧ)) = 0. |G - 1| ≤ |Ȳ - X_0| + |K| ≤ 18.4y²; G + Ǧ - 2 = K + Ǩ. *Real case:* for Y_j, X ∈ su(N),
(e^{-X}M)* = M̌e^{X}, so Ǩ = K* and ½(K - Ǩ) - N⁻¹tr(½(K - Ǩ)) = Π(K) (NA-alg's projection onto su(N)): Φ^ℂ = Φ on su(N); Φ maps
the real ball into itself, and the fixed point in B^ℂ is unique, so X_0^ℂ = X_0. (iii) *Holomorphy/reality:* compositions of
(ii) with products of links. For a real chain, φ_{M̄_c}(V) = N⁻¹[Re tr(W_0⁻¹M̄) - Re tr(V⁻¹M̄)] with W_0(M̄) = SW_0(A) (left
covariance) = Se^{X_0}, and Re tr Z = ½(tr Z + tr Z*) with (e^{-X_0}A)* = Ǎe^{X_0}, (V'⁻¹A)* = ǍV'. *Gauge:* under g, S⁻¹T_j and
V' are conjugated by g(c_Y) (they are loops / transports based at c_Y), Y_j and X_0 likewise (uniqueness), traces invariant.
*Local expansion:* tr(V'⁻¹A) = tr(e^{ρ}G), tr(ǍV') = tr(Ǧe^{-ρ}), so φ^ℂ = -(1/2N)[tr((e^ρ - 1)G) + tr(Ǧ(e^{-ρ} - 1))]. Order 1:
-(1/2N)tr(ρ(G - Ǧ)) = 0, because G - Ǧ = N⁻¹tr(G - Ǧ)·1 (stationarity) and tr ρ = 0. Order 2: -(1/4N)tr(ρ²(G + Ǧ)) =
-tr(ρ²)/(2N) - (1/4N)tr(ρ²(K + Ǩ)), and |tr(ρ²(K + Ǩ))| ≤ |ρ|²·18.22y². Orders ≥ 3: ≤ (1/2N)Σ_{m≥3}(|ρ|^m/m!)(|G| + |Ǧ|) with
|G|, |Ǧ| ≤ √N·e^{|X_0|+y} ≤ √Ne^{4y}, and e^r - 1 - r - r²/2 ≤ r³e^r/6. *Global form:* with D := 1 - V'' and Γ := G - 1, Γ̌ := Ǧ - 1
= Γ - c·1 (stationarity, c := N⁻¹tr(G - Ǧ)):
  φ^ℂ(W_0^ℂV'') = (1/2N)[tr(2 - V'' - V''⁻¹) + tr(D*Γ) + tr(Γ̌D)] = s(V'') + (1/2N)[tr(Γ(D + D*)) - c·tr D],
and D + D* = DD* for unitary V'', so |tr(ΓDD*)| ≤ ||Γ||·|D|² = ||Γ||·2N·s(V''). For tr D: Re tr D = N·s; if |D| < r_N, every
|1 - e^{iθ_j}| < 1 (so |θ_j| < π/3) and Σ|θ_j| ≤ (π/2)√N|D| < 2π, hence Σθ_j = 0 and |Im tr V''| = |Σ(sin θ_j - θ_j)| ≤
Σ|θ_j|³/6 ≤ (π/18)Σθ_j² ≤ (π³/72)|D|²; if |D| ≥ r_N, |Im tr V''| ≤ N ≤ (N/r_N²)|D|². So |tr D| ≤ N(1 + 2c_N)s, and |c| ≤ ||Γ|| +
||Γ̌||, which gives |Δ| ≤ s[||Γ|| + (1 + 2c_N)(||Γ|| + ||Γ̌||)/2] ≤ 18.4y²(2 + 2c_N)s. ∎

### 25.2 Lemma POL (polar and chart forms of the complex domain): PROVEN-HERE [S4-D] (not counted; elementary)
(i) For X, Y ∈ su(N) with ||X||, ||Y|| ≤ 1/8: e^{X+iY} = Ve^{H} with V ∈ SU(N), H ∈ i·su(N) (Hermitian traceless),
**||H|| ≤ 4.19||Y||, ||V - e^{X}|| ≤ 9.2||Y||** (the proof gives 7.6).
(ii) **Chart polydiscs lie in the polar domain:** for U^r ∈ R_ε(X) and r ≤ 1/8, P_r(U^r) ⊂ 𝔇_{ε+41r, 4.19r}(X). Conversely
𝔇_{ε,α}(X) ⊂ ∪_{V∈R_ε(X)}P_α(V) (Ve^{H} = Ve^{Z} with Z = H).
(iii) **MSG / log charts:** if U^r_b = e^{a_b} with ||a_b|| ≤ 1/8 (e.g. in an MSG gauge, ||a_b|| ≤ C_Mε), then the log polydisc
{(e^{w_b}) : w_b ∈ sl(N, ℂ), ||w_b - a_b|| ≤ r} ⊂ P_{1.27r}(U^r) for r ≤ 1/16. So, in a local MSG gauge, the domain contains a genuine
product of discs in the Lie coordinates w_b, of radius r ≍ min{α_E, ε_1}, around every real point.
*Proof.* (i) G(X', Y') := ½log(e^{-X'+iY'}e^{X'+iY'}) (series) is holomorphic for complex X', Y' with ||X'||, ||Y'|| ≤ 1/8, since the
argument is within e^{1/2} - 1 = 0.6487 of 1; there ||G|| ≤ ½(-log(1 - 0.6487)) = 0.5231. For real X, Y, (e^{X+iY})* = e^{-X+iY}, so
the argument is A*A > 0 (A := e^{X+iY}) and H := G(X, Y) is its Hermitian log; V := Ae^{-H} is unitary; det A = e^{tr(X+iY)} = 1 and
e^{2tr H} = |det A|² = 1, so tr H = 0 and det V = 1. G(X, 0) = 0, so Schwarz's lemma for ζ ↦ G(X, ζY/(8||Y||)) (|ζ| ≤ 1; for
Banach-valued maps via norming functionals) gives ||H|| ≤ 0.5231·8||Y|| = 4.185||Y||. V - e^X = (A - e^X)e^{-H} + e^X(e^{-H} - 1);
||A - e^X|| ≤ e^{||X||}(e^{||Y||} - 1) ≤ 1.207||Y||, ||e^{-H}|| ≤ e^{0.5231} = 1.687, ||e^X|| = 1, ||e^{-H} - 1|| ≤ 1.314||H|| ≤ 5.50||Y||:
total ≤ 7.54||Y||. (ii) U^r_be^{Z_b} = (U^r_bV_b)e^{H_b} by (i) (||X_b||, ||Y_b|| ≤ ||Z_b|| ≤ r), ||H_b|| ≤ 4.19r, ||U^r_bV_b - U^r_b|| ≤
||V_b - e^{X_b}|| + ||e^{X_b} - 1|| ≤ 10.2r, so each plaquette moves by ≤ 40.8r. (iii) e^{-a}e^{w} - 1 = e^{-a}(e^w - e^a) has norm ≤
e^{||a||}(e^r - 1) ≤ 1.171r ≤ 0.074 (||e^{-a}|| = 1), and ||log(1 + W)|| ≤ ||W||/(1 - ||W||) ≤ 1.27r. ∎

### 25.3 Lemma EXT (gluing holomorphic continuations along the real domain): PROVEN-HERE [S4-D] (not counted; standard)
Let r ≤ 1/8, 𝒰 ⊂ SU(N)^X a set of real base points, f a function on the real set ∪_{U∈𝒰}(real points of P_r(U)), and for each
U ∈ 𝒰 let F_U be holomorphic on P_r(U) with F_U = f on the real points of P_r(U). Then **F(W) := F_U(W) for W ∈ P_{r/4}(U) is well
defined and holomorphic on ∪_{U∈𝒰}P_{r/4}(U).**
*Proof.* If W ∈ P_{r/4}(U_1) ∩ P_{r/4}(U_2), then U_1⁻¹U_2 = e^{Z_1}e^{-Z_2} linkwise is unitary with ||e^{Z_1}e^{-Z_2} - 1|| ≤
e^{r/2} - 1 ≤ 0.516r, so U_2 = U_1e^{X_{12}}, X_{12} ∈ su(N), ||X_{12}|| ≤ 0.522r (F1). For ||Z|| ≤ r/4, U_2e^{Z} = U_1e^{Z'} with
||e^{X_{12}}e^{Z} - 1|| ≤ e^{0.772r} - 1 ≤ 0.81r ≤ 0.101 and ||Z'|| ≤ 0.81r/0.899 ≤ 0.9r: P_{r/4}(U_2) ⊂ P_r(U_1). P_{r/4}(U_2) is
connected (image of a convex set), F_{U_1} and F_{U_2} are holomorphic on it and agree on its real points, an open subset of the
maximal totally real submanifold SU(N)^X (in the coordinates Z the real points are an open set of su(N)^X, and
su(N)^X ⊗ ℂ = sl(N, ℂ)^X); the identity theorem gives F_{U_1} = F_{U_2} on P_{r/4}(U_2) ∋ W. ∎

### 25.4 Lemma NORM-an (the kernel normalisation has a g-independent complex width): PROVEN-HERE [S4-D] (counted)
(i) **Haar shift.** If f is entire on SL(N, ℂ), then ∫_{SU(N)}f(AV)dV = ∫_{SU(N)}f(V)dV for every A ∈ SL(N, ℂ).
(ii) Let c be as in TERM-an (iii), on D_c(y_0), with θ = 18.4y²(2 + 2c_N) ≤ ½, and κu ≥ ½. Then
  **𝒩^ℂ_c := ∫_{SU(N)}e^{-κuφ^ℂ_c(V)}dV satisfies |𝒩^ℂ_c/𝒩_0 - 1| ≤ C_Nθ,  𝒩_0 := ∫_{SU(N)}e^{-κu·s(V)}dV** (a c-number),
with C_N < ∞ depending only on N (exists; not computed). If C_Nθ ≤ ½, then log𝒩^ℂ_c = log𝒩_0 + 𝔫_c with 𝔫_c holomorphic on
D_c(y_0) and **|𝔫_c| ≤ 2C_Nθ = O(y²), uniformly in u ≥ 1/(2κ), i.e. uniformly in g.**
*Proof.* (i) J(A) := ∫f(AV)dV is holomorphic on SL(N, ℂ) (differentiation under the integral; compact domain), and J(A) = J(1)
for A ∈ SU(N) (Haar invariance). SU(N) is a maximal totally real submanifold of the connected complex manifold SL(N, ℂ), so
J ≡ J(1). (ii) V ↦ e^{-κuφ^ℂ_c(V)} is entire on SL(N, ℂ) (V⁻¹ is polynomial for det V = 1), so by (i) with A := W_0^ℂ and TERM-an
(iii) (global form), 𝒩^ℂ_c = ∫e^{-κu(s + Δ)}dV''. |e^{-κuΔ} - 1| ≤ κuθs·e^{κuθs}, so |𝒩^ℂ_c - 𝒩_0| ≤ θ∫κus·e^{-κu(1-θ)s} ≤
θ(2/(e(1 - θ)))Z(κu(1 - θ)/2), Z(λ) := ∫e^{-λs}dV (te^{-at} ≤ (2/(ea))e^{-at/2}). *Ratio bound:* v(t) := Haar{s ≤ t} is continuous,
positive for t > 0, v(t) ~ c_vt^{D/2} as t → 0 (D := N² - 1; s ≈ |X|²/(2N) in exponential coordinates, smooth Haar density), and
v ≡ 1 for t ≥ 2; so c_-t^{D/2} ≤ v(t) ≤ c_+t^{D/2} on (0, 2] and v(t) ≤ c'_+t^{D/2} for all t > 0. Then Z(Λ) ≥ e⁻¹v(1/Λ) ≥
e⁻¹c_-Λ^{-D/2} (Λ ≥ ½) and Z(λ) = ∫_0^∞λe^{-λt}v(t)dt ≤ c'_+Γ(D/2 + 1)λ^{-D/2}, so Z(λ)/Z(Λ) ≤ C^Z_N(Λ/λ)^{D/2},
C^Z_N := ec'_+Γ(D/2 + 1)/c_-. With Λ = κu, λ = κu(1 - θ)/2 ≥ κu/4: C_N := (4/e)·4^{D/2}C^Z_N for θ ≤ ½. Holomorphy of 𝒩^ℂ_c:
differentiation under the integral; |log(1 + w)| ≤ 2|w| for |w| ≤ ½. ∎
*Reading.* The obstruction to a g-independent width ("the Gaussian scale is g/√κ") is removed by moving the integration
contour to the complex maximiser W_0^ℂ, which (i) makes exact; after the shift the integrand is s(V'')(1 + O(y²)), with no
linear term (stationarity). This is the standard device of shifting to the complex background, here exact on a compact group.
[inference, not proven:] the same shift applies to the sea average of any ENTIRE function of the fine field under the
normalised kernel, so the width O(g/√κ) of PLD §9.4 (l.497-503, ARGUED there) is caused by the non-analytic large-field
indicators inside the frozen activity, not by the kernel.

### 25.5 The analytic main term (item (a5)) and its hypotheses
**Term set.** 𝒞^♭(Λ_k) := ∪{𝒞(P) : P a level-k plaquette with its four corners in Λ_k} (full cones only). 𝒞(Λ_k) ∖ 𝒞^♭(Λ_k)
consists of terms over the outer level-k layer of Λ_k (terms ≥ 0); they join (a4)'s boundary defect. Every chain variable of a
𝒞^♭-term lies in a cone box W_P^{(i)} (§15.1), where MSG applies. E^♭(ψ; U) := Σ_{𝒞^♭(Λ_k)}(s, κφ terms) for a chain ψ on the
descendants with top field U; E^{♭,ℂ} the same sum with TERM-an's s^ℂ, φ^ℂ; **𝓔^♭_k(U) := inf_ψE^♭(ψ; U)** (attained, as (a') (1)).
**Regular chains.** A real chain ψ with top U is *ε_R-regular* if, in every full cone 𝒞(P) ⊂ 𝒞^♭(Λ_k), every level-i plaquette
(0 ≤ i ≤ k) with vertices in W_P^{(i)} and every residual of a cone link is ≤ ε_R (op norm), with C_Mε_R·p_L ≤ 1/8 (so all contour
spreads y ≤ y_0 in MSG gauges, TERM-an applies, and E^♭ is real-analytic near ψ).
**Hypothesis items (precise; not proven here).**
- **(a5-G) [OPEN; P; owner: the small-field package (lane F; PROOF node N2's (G♯) and N5's background operators)]** There are
  ε_R > 0, G, G_D, G_w, G_{D,w} < ∞, κ_5 > 0, depth-uniform (independent of k, K, T, Λ_k, 𝔥), such that at every ε_R-regular real
  critical chain ψ^r with top U, in left-trivialised coordinates ψ = ψ^re^{X}, U' = Ue^{Z} and with a chain-gauge slice through
  ψ^r (chain gauges trivial at the level-k sites) carrying a Feynman term: the slice Hessian 𝓛 of E^♭ and the data map N obey
  ||𝓛⁻¹||_{ℓ^∞→ℓ^∞} ≤ G, ||𝓛⁻¹N||_{ℓ^∞→ℓ^∞} ≤ G_D, the same with weights e^{±κ_5d(·, b_0)} (constants G_w, G_{D,w}), and the
  combined map 𝔉 of B-NA-red's (FP♯') is onto at every point of the slice ball ||X||_∞ ≤ r_T/2 (r_T of (R♯_∞) below). (At
  ψ^r = trivial chain this is PROOF's (G♯) at U = 1 in sup norms.)
- **(a5-U) [OPEN; lane D; classical]** For real U ∈ R_{2ε_1}(Λ_k) the minimiser of E^♭(·; U) is unique modulo chain gauge.
  (Near the trivial field this is the uniqueness clause of FLOW's (SF-bg).)
- **(a3-q) [OPEN; lane D; classical; replaces (a3)]** There are C_3, δ_3 > 0, depth-uniform, such that for real U ∈ R_δ(Λ_k),
  δ ≤ δ_3, every minimiser ψ* of E^♭(·; U) has **E_𝒞(P)(ψ*) ≤ C_3δ²** for every full cone 𝒞(P) ⊂ 𝒞^♭(Λ_k). (It implies (a3) on
  R_δ: a cube's assigned terms lie in ≤ 24 nearby cones, so 0 ≤ 𝓔_{k,x} ≤ 24C_3δ². Its linear case is plausibly a corollary of
  the curvature decay of the linear minimiser, LINEAR_PACKAGE Theorem 3.8 as quoted in §15.5 [inference; not checked].)

**Lemma (R♯_∞) (the nonlinear remainder in sup norms): PROVEN-HERE (not counted; Cauchy estimates).** At an ε_R-regular real
chain, every term of E^{♭,ℂ} depends on ≤ n_T := 1 + 2dL^d + L^{d-1} link variables (a kernel term reads V and the level-i links of c's two
endpoint blocks and between them; a plaquette term reads 4), every variable lies in ≤ m_T terms
(m_T depends only on (L, d)), and by TERM-an each term is holomorphic and bounded by some S_T < ∞ depending only on (N, L, d) (e.g. 1 + e^{1/2} for s^ℂ and 2e^{4y_0+1/2} for φ^ℂ) on the
product polydisc {||X_b||, ||Z_b|| ≤ r_T}, r_T := y_0/(8p_L). Cauchy's estimates bound its second and third derivatives per
pair/triple of variables by 2S_T/r_T² and 6S_T/r_T³; summing over the ≤ m_T terms through a link, 𝔑(X; Z) := ∇_XE^{♭,ℂ} - 𝓛X - NZ
obeys NA-IFT's two bounds in ℓ^∞ (and in the weighted ℓ^∞ norms, the weights changing by ≤ e^{κ_5n_T} inside a term) with
C := 3m_Tn_T²S_T/r_T³, on ||X||_∞, ||Z||_∞ ≤ r_T/2. ∎

**Theorem A5 (the analytic main term): CONDITIONAL [S4-D] ⇐ (a5-G) + (a5-U) + (a3-q) + (MS-Sob) (the last through Theorem
AE-red, §26).** Let ε_1 ≤ ½δ_a, δ_a := min{δ_3, √(η_AE/C_3), ε_R/(C_♮√C_3), ε_R} (C_♮, η_AE of §26). Put ρ_1 := min{r_T/2, 1/(4GC)} and s_5 :=
min{ρ_1/(4(1 + G_D)), 1/(16GC(1 + G_D)²), 1/(10G_wC_w(1 + G_D))} (NA-IFT with (R♯_∞)'s C; on the slice ball ||X||_∞ ≤ ρ_1 the
fixed-point map has Lipschitz constant ≤ GC(2ρ_1 + s_5) < 1, so critical chains there are unique). Then:
- (A) *Real regularity.* For real U ∈ R_{2ε_1}(Λ_k), every minimiser ψ* of E^♭(·; U) is ε_R-regular and is a critical chain.
- (B) *Local branches.* For such U there is a holomorphic map Z ↦ Ψ_U(Z) = ψ*e^{X(Z)} (||Z||_∞ ≤ s_5) of critical chains with top
  field Ue^{Z}, X(0) = 0, |∂X(b)/∂Z(b')| ≤ (2G_{D,w} + 6G_wC_w(1 + G_D)s_5)e^{-κ_5d(b,b')}; F_U(Ue^{Z}) := E^{♭,ℂ}(Ψ_U(Z); Ue^{Z}) is
  holomorphic on P_{s_5}(U), and **F_U = 𝓔^♭_k on the real points of P_{s_5}(U).**
- (C) *Glued main term.* **𝓔^{an}_k := the gluing of the F_U (Lemma EXT) is holomorphic on ∪_{U∈R_{2ε_1}}P_{s_5/4}(U) ⊃
  𝔇_{2ε_1, s_5/4}(Λ_k), equals 𝓔^♭_k on R_{2ε_1}(Λ_k), and is SU(N)-gauge invariant.** Its local densities 𝓔^{an}_{k,x} (the
  𝒞^♭-terms assigned to x by the lexicographic rule of (a'), evaluated on the branches) are well defined, holomorphic, equal on
  real points to the assigned terms of THE minimiser (no measurable selection on Λ_k), and exponentially local:
  |∂𝓔^{an}_{k,x}/∂Z(b')| ≤ C·e^{-κ_5d(x,b')}.
- (D) (*Unconditional part.*) For any real chain ψ with top U, E^♭(ψ; U) ≥ 𝓔^♭_k(U); in particular every real critical value
  dominates the infimum, so the CLS-cone lower bounds (§20.3 (B)) hold for 𝓔^{an}_k wherever it is a real critical value.
*Proof.* (A) By (a3-q) with δ = 2ε_1 ≤ δ_a, every full cone has E_𝒞(P)(ψ*) ≤ 4C_3ε_1² ≤ η_AE. Theorem AE-red (§26) and its
size clause give, on every full cone, all plaquettes of levels ≤ k and all residuals ≤ C_♮√(4C_3)ε_1 ≤ ε_R (level-k plaquettes of
U are ≤ 2ε_1 ≤ ε_R directly). On the open set of ε_R-regular chains E^♭ is real-analytic in the chain variables (TERM-an), and ψ*
minimises over the boundaryless manifold SU(N)^{links}, so ∇E^♭(ψ*) = 0. (B) (a5-G), (R♯_∞) and NA-IFT, run in the complex
Banach space ℓ^∞(links; sl(N, ℂ)) (its proof is verbatim; the contraction is holomorphic in (X, Z), so the fixed point is
holomorphic in Z, as in TERM-an (ii)); the slice solution is critical in all directions by NA-crit' ((FP♯') in (a5-G)). *F_U = 𝓔^♭
on real points:* let O be the set of real Z (||Z||_∞ ≤ s_5, a connected set) at which Ψ_U(Z) is a minimiser for Ue^{Z}. 0 ∈ O.
O is closed: minimisers are closed under limits (continuity of E^♭) and Ψ_U is continuous. O is open: at Z_1 ∈ O, the
minimiser for Ue^{Z} is unique modulo gauge (a5-U), so its gauge orbit depends continuously on Z (Berge on the compact quotient);
for Z near Z_1 a gauge representative lies in the slice within the uniqueness ball ||X||_∞ ≤ ρ_1 (it is near Ψ_U(Z_1),
which lies strictly inside, ||X(Z_1)||_∞ ≤ 2(1 + G_D)s_5 ≤ ρ_1/2, and the slice is transversal there by (FP♯') on the ball;
local slice theorem, non-uniform, at fixed k and T); by (A) it is a critical
chain, so it equals Ψ_U(Z): Z ∈ O. Hence O is everything, and F_U = E^♭(minimiser) = 𝓔^♭_k there. (C) Lemma EXT with r = s_5,
f = 𝓔^♭_k. ⊃ 𝔇: Ue^{H} ∈ P_{s_5/4}(U) for ||H|| ≤ s_5/4. Gauge invariance: W ↦ 𝓔^{an}(W^g) - 𝓔^{an}(W) is holomorphic on each
P_{s_5/4}(U) (W^g ∈ P_{s_5/4}(U^g); R_{2ε_1} is gauge invariant) and vanishes at real points. Densities: two branches through W
agree, after a gauge, at real points (unique minimiser; terms gauge invariant), hence on the connected overlap by the
identity theorem. Locality from (B)'s kernel decay (finite-range terms). (D) is the definition of an infimum. ∎
*What is and is not proven.* Proven here: TERM-an, NORM-an, POL, EXT, (R♯_∞), the implication of Theorem A5, (D). Not proven:
(a5-G) (the uniform linear-analytic input, the multi-level background version of PROOF's (G♯): lane F / node N2), (a5-U), (a3-q)
(classical, lane D), (MS-Sob) (lane G's (SQ-dev) family). **The radius s_5 is depth- and polymer-size-independent given (a5-G):
the polydiscs are sup-norm (product) polydiscs and every constant is per link.** Target S6's "not success" clauses are avoided.

### 25.6 (I_k^E)'' (restated hypothesis) [HYPOTHESIS, P]
As §14.1 / §20.3 (C) with:
- **(a'') Main term** u_k𝓔^{an}_k(U) on Λ_k (Theorem A5 (C)); real points: 𝓔^{an}_k = 𝓔^♭_k (the localised infimum over full
  cones); densities 𝓔^{an}_{k,x} as in A5 (C). The term set is 𝒞^♭(Λ_k); the outer-layer terms 𝒞(Λ_k) ∖ 𝒞^♭(Λ_k), the
  superadditivity and (c5) defects of (a') (2), (4) (which hold verbatim for 𝒞^♭) go to (a4)'s boundary factor. The
  inf/measurable-selection definition is used only for Ω^c_k-adjacent bookkeeping, never on the small-field region.
- **(b'') Polymers** E_k(X; ·) holomorphic on **𝔇_{2ε_1,α_E}(X) = {V_be^{H_b} : V ∈ R_{2ε_1}(X), H_b Hermitian traceless, ||H_b||
  ≤ α_E}** (S3-7 corrected), α_E ≤ s_5/4 g-independent, with (b)'s bound. By POL (ii), 𝔇 contains every chart polydisc P_r(U^r),
  U^r ∈ R_{ε_1}(X), r ≤ min{α_E/4.19, ε_1/41}, and in local MSG gauges a log polydisc of radius r/1.27 (POL (iii)): Cauchy
  estimates at real points of the ε_1-domain hold with radius ≍ min{α_E, ε_1}, uniformly in |X|, k.
- (c) unchanged.
- **(d'') Two-field form** u_k[𝓔^{an}_k(U_k) + κΦ^{♭,ℂ}_k(U_k, U_{k+1})] (φ^ℂ of TERM-an (iii)) + polymers + R1^J remainders +
  coupling-shift polymer + **the kernel normalisation -Σ_clog𝒩^ℂ_c = -Σ_clog𝒩_0 - Σ_c𝔫_c (NORM-an: c-number plus a holomorphic
  per-link term |𝔫_c| ≤ 2C_Nθ = O(y²), on a g-independent width).**
- **Hypothesis items:** (a3-q) (replaces (a3)); (a4) (unchanged; now also carries the outer-layer terms); **(a5) := (a5-G) +
  (a5-U)** (with (a3-q) and (MS-Sob) it yields Theorem A5).

### 25.7 Consistency checks
- **(c1'') Lemma HF on the complex domain (PROVEN, elementary).** With P^ℂ := (ǍA)^{1/2} (series; ǍA near 1), k̃^ℂ(V) :=
  (1/2N)[2tr P^ℂ - tr(V'⁻¹A) - tr(ǍV')] and d^ℂ := (1/2N)[2tr P^ℂ - tr(e^{-X_0}A) - tr(Ǎe^{X_0})], the identity **k̃^ℂ = φ^ℂ + d^ℂ**
  holds identically (algebra), so HF (i) continues. d^ℂ is holomorphic in (Y_j); on real data d ≤ 14.4y⁶ (HF (iii), N = 3; similar
  for every N), so its Taylor polynomials of degree < 6 vanish on su(N)^m, hence identically, and the order-6 Schwarz lemma gives
  |d^ℂ| ≤ D_0(y/y_0)⁶ (D_0 := sup over |Y_j| ≤ y_0 ≤ 2e^{4y_0} + 2e^{y_0}). For N = 2, d^ℂ ≡ 0 (identity theorem). So the φ-tower
  stays the right main term on the complex domain, and FLOW's k̃-tower differs from it there by the same sextic, β-neutral term
  ([RH2-fix 10] unchanged).
- **(c2'') FLOW F-tree, β[𝓔_k] = 1.** β is the coupling of the infinite-volume quadratic part at the trivial field. There
  𝓔^{an}_k = 𝓔^♭_k = the tower (given (a5-U) near 1, i.e. (SF-bg)'s uniqueness), and the restriction to 𝒞^♭ changes only
  boundary terms. So β[𝓔^{an}_k] = 1 in the bulk, unchanged; the IFT branch through the trivial chain at U = 1 is the trivial
  chain, and the Hessian of the critical value is the Schur complement, i.e. H_k (Setting SC), as F-tree uses.
- **(c3'') RLARGE v2 (RLF-5) and Conflict K7.** (b'') is one gauge-covariant complex domain on the ε_1-domain, chart-free, with
  genuine polydiscs in every chart (POL): it is the object K7 asks for. Widths: the main term (⇐ Theorem A5's hypotheses), the
  chain terms (TERM-an) and the kernel normalisation (NORM-an, unconditional) have a g-INDEPENDENT width. The returned
  large-field remainders of (RLF-5) have width O(g/√κ) per PLD l.497-503 (ARGUED there). **Integration item for the lead
  (RLARGE.md not edited):** (I_k^E)''(b'') needs either (RLF-5) at width α_E for the remainders that enter E_k, or a second polymer
  class at width O(g/√κ) whose e^{-a_♯/g²} size pays the g^{-3} loss of C³ Cauchy bounds [inference]; by NORM-an's reading the
  width loss sits in the non-analytic indicators, which is where (RLF-5) should look.
- **(c5'') Self-reproduction in critical-value form (PROVEN, elementary).** If Ψ(U_k) is a critical chain with top U_k and U_k*
  is a critical point of U_k ↦ 𝓔^{an}_k(U_k) + κΦ^♭_k(U_k, V), then (Ψ(U_k*), U_k*) is a critical chain of the level-(k+1) problem
  with top V (chain rule: ∂_{U_k}[E^♭(Ψ(U_k); U_k)] = ∂_{U_k}E^♭ at ∂_ψE^♭ = 0). With (a5-U) at level k + 1 and (A), its value is
  𝓔^{an}_{k+1}(V) when it is the minimiser; so (c5) holds with critical values, and the localised inequality ≥ of (a') (4) is
  unchanged. The Laplace step of (SF^J) needs the critical point to be the global minimiser of the real exponent: that is where
  Theorem A5 (B)'s agreement is consumed (the pricing (CLS-cone) needs only (D)).

## 26. Step 3: Theorem AE-red ((AE) ⇐ MSG + (MS-Sob)), written fully

**(MS-Sob) (precise form consumed) [OPEN; P; lane G's (SQ-dev) family].** There are C_S < ∞ and ε_S ∈ (0, ε_M], depth-uniform,
such that for every k ≥ 1, every chain and every level-k plaquette P (level-k side ≥ 3) satisfying MSG's hypotheses (i)-(ii)
with some ε ≤ ε_S, the link logs a_i := log U^g_i of the MSG gauge g (§20.2, axial order with P's plane first, [RH3-fix S3-1])
satisfy **Σ_{b level-i, endpoints in W_P^{(i)}}|a_i(b)|⁴ ≤ C_S·E_𝒞(P)²** for every 0 ≤ i ≤ k - 1 (HS norms). (The MSG gauge is a
construction, independent of ε; ε enters only its bounds.)

**Constants.** κ_i ≡ κ; A_d = (d - 1)L(L - 1)/2, A' := 2A_d, p_L := 5L - 4 (contour length), C_loc := ((2L - 1)/(L - 1))max{2, 16/κ},
**C'_AE := 2C_locN (fixed first)**, c' := 1.0107√N, C'' := max{2N, C'_AE}, **C_♮ := max{√C'', √(4N/κ)}**, C_M = 66.1 (MSG),
  C_e := max{2√Np_L²e^{1/8} + 9.4Np_L² + 36.8N^{3/2}p_L²e^{1/4}, 4√Ne^{1/4}},  K_R := 64√8·√N·e^{1/2},
  **C_2 := K_R√C_S + √8(L/(L - 1))C_e[√(2dC_S) + 1.011√N·C_♮√(2.4N/κ)] + 32√Ne^{1/2}C_M²C_♮².**
**Smallness conditions on η_AE** (ε̃_η := C_♮√η_AE, y'_η := c'A'√(C''η_AE), y_M := 1.011√Np_LC_Mε̃_η, r_η := 1.011√Nε̃_η,
θ_η := 1.011√(2Nη_AE)):
- (Z1) ε̃_η ≤ ε_S (so MSG and (MS-Sob) apply);
- (Z2) y'_η ≤ 1/20, 2A_d√(C''η_AE) ≤ ½, and 73.6N(c'A')²C''√η_AE ≤ √C'';
- (Z3) p_LC_Mε̃_η ≤ 1/8, 3y_M + r_η ≤ 1/4, y_M ≤ 1/20;
- (Z4) 1 + δ_η ≤ 1.2, δ_η := max{θ_η²/(12 - θ_η²), (18.4y'_η² + (2√N/3)e^{r_η}r_η)/(1 - 18.4y'_η² - (2√N/3)e^{r_η}r_η)};
- (Z5) (closing inequality) **√(1.2·C_locN) + C_2√η_AE ≤ √(2C_locN) = √C'_AE.**
Every condition involves only (N, L, d, κ, C_S, ε_S) and constants fixed before η_AE; C'_AE does not depend on η_AE.

**Theorem AE-red: CONDITIONAL [S4-D] (implication PROVEN) ⇐ MSG [PROVEN] + (MS-Sob).** Let η_AE satisfy (Z1)-(Z5). For every
k ≥ 1, every chain (U_0, …, U_k) and every level-k plaquette P (level-k side ≥ 3) with **E_𝒞(P) ≤ η_AE**:
  **U_k(P) = e^X, X ∈ su(N), |X|²_HS ≤ C'_AE·E_𝒞(P) = 2C_locN·E_𝒞(P).**
*Size clause.* Moreover every level-i plaquette p (0 ≤ i ≤ k - 1) with vertices in W_P^{(i)} has ||1 - U_i(p)|| ≤ √C''·√E and
every residual of a cone link has ||U_{i+1}(c) - W_0(M̄_c)|| ≤ C_♮√E, E := E_𝒞(P).
In particular (AE) in its restated form (§15.3, §20.3: (i)-(iii)) holds with C'_AE = 2C_locN, any ε_AE, and this η_AE: hypotheses
(i)-(ii) are implied by (iii).
*Proof.* Strong induction on k; write E := E_𝒞(P). The claim for depth < k is used only for plaquettes p in P's cone.
**(1) Sizes.** (a) Level 0: ||1 - U_0(p)||² ≤ |1 - U_0(p)|²_HS = 2Ns(U_0(p)) ≤ 2NE (s(U_0(p)) is a term of 𝒞(P)). (b) Level
1 ≤ i ≤ k - 1: 𝒞(p) ⊂ 𝒞(P) (nesting, §15.1), so E_𝒞(p) ≤ E ≤ η_AE and the induction hypothesis gives U_i(p) = e^{X_p},
||1 - U_i(p)|| ≤ |X_p|_op ≤ |X_p|_HS ≤ √(C'_AE·E) (F2). So every plaquette size in the cone (levels < k) is ≤ √C''√E. (c)
Residuals: for a level-(i+1) cone link c (0 ≤ i ≤ k - 1; i = k - 1 includes P's four links, whose kernel terms are in 𝒞(P)), the
S4' contours T_j satisfy ||1 - T_1⁻¹T_j|| ≤ A'·√C''√E ≤ ½ (§15.4 β: two ribbons of ≤ A_d cone plaquettes; lasso), so
|Y_j|_HS := |log(T_1⁻¹T_j)| ≤ c'A'√C''√E ≤ y'_η ≤ 1/20 (Z2), and NA-alg (a) gives ||M̄_c - W_0|| ≤ 18.4y'²; KQ (lower) with
x := ||U_{i+1}(c) - W_0||: either x ≤ 73.6Ny'² ≤ 73.6N(c'A')²C''√η_AE·√E ≤ √C''√E (Z2), or φ_c ≥ x²/(4N) and κφ_c ≤ E gives
x ≤ √(4N/κ)√E. So all sizes are ≤ **ε̃ := C_♮√E ≤ ε̃_η ≤ ε_S ≤ ε_M** (Z1).
**(2) Gauge.** MSG with ε̃ (its hypotheses (i)-(ii) are (1)): in the MSG gauge g every cone link of every level i ≤ k has
|a_i(b)|_op ≤ C_Mε̃; (MS-Sob) applies with ε̃: Σ_{level i}|a_i|⁴ ≤ C_SE² (0 ≤ i ≤ k - 1). Plaquettes, kernel terms and residuals
are gauge invariant (F6). Put m_i(c) := max{||a_i(b)|| : b on a contour of c}, m_0(p) := max_{b∈∂p}||a_0(b)|| (op norms, ≤ C_Mε̃,
so (Z3) gives p_Lm_i ≤ 1/8 and 4m_0 ≤ 1/8); inside the ℓ⁴ sums below they are bounded by the HS maxima.
**(3) Exact recursion.** For a level-(i+1) cone link c: U^g_{i+1}(c) = W_0(M̄_c(U^g_i))e^{-ρ̃_c}, ρ̃_c := -log(W_0⁻¹U^g_{i+1}(c))
(principal; ||ρ̃_c|| ≤ 1.011ε̃, |ρ̃_c|_HS ≤ r_η), and W_0(M̄_c(U^g_i)) = e^{X_0(c)} with M̄_c(U^g_i) = Σ_jw_je^{Y_j}, Y_j := log T_j
(MSG gauge; |Y_j|_HS ≤ y_c := 1.011√Np_Lm_i(c) ≤ y_M ≤ 1/20 (Z3)). Define (Qa_i)(c) := Σ_jw_jΣ_{b∈T_j}±a_i(b) (the linearised S4'
map, LINEAR_PACKAGE's Q) and e_i(c) := a_{i+1}(c) - (Qa_i)(c) + ρ̃_c. Then exactly
  **a_{i+1} = Qa_i + e_i - ρ̃_i on cone links,** and e_i(c) = Σ_jw_j[Y_j - Σ_{T_j}±a_i] + [X_0 - Ȳ] + [log(e^{X_0}e^{-ρ̃}) - X_0 + ρ̃].
**(4) The error e_i.** (F5) and (F3) (both sides within ½ of 1): |Y_j - Σ_{T_j}±a_i|_op ≤ 2(p_Lm)²e^{p_Lm}, HS ≤ √N times that;
NA-alg (a): |X_0 - Ȳ|_HS ≤ 9.2y_c²; (F5) with two factors and (F3): |log(e^{X_0}e^{-ρ̃}) - X_0 + ρ̃|_op ≤ 2t²e^t ≤ 4(9y_c² +
||ρ̃||²)e^t, t := |X_0| + ||ρ̃|| ≤ 3y_c + r_η ≤ 1/4 (Z3). With y_c² ≤ 1.0221Np_L²m², this gives
  **|e_i(c)|_HS ≤ C_e(m_i(c)² + |ρ̃_c|²_HS).**
Each level-i link b lies on contours of ≤ 2d level-(i+1) links c (the S4' contours of c = (X, Y) use axial moves inside one endpoint
block and one straight leg between the two blocks, §15.4 β; a link inside block X serves only the 2d links at X, a crossing link
only the link it parallels), so Σ_cm_i(c)⁴ ≤ 2d·Σ_{level i}|a_i|⁴ ≤ 2dC_SE². And Σ_c|ρ̃_c|⁴ ≤ r_η²Σ_c|ρ̃_c|², with, by NA-alg (b) (base
T_1; ||ρ̃|| < 2π/N), |ρ̃_c|² ≤ 2N(1 + δ_η)φ_c (the ρ-coefficient of φ is ≥ (1/(2N))(1 - 18.4y'² - (2√N/3)e^{|ρ|}|ρ|)). Minkowski:
  **||e_i||_{ℓ²(R'_i(P))} ≤ C_e[√(2dC_S)·E + r√(2.4N/κ)·√E],  r := 1.011√Nε̃ ≤ r_η** (Σ_{R'_i}κφ ≤ E; 1 + δ_η ≤ 1.2 by (Z4)).
**(5) Unrolling and the top plaquette.** U^g_k(P) = e^{a_k(c_1)}e^{a_k(c_2)}e^{-a_k(c_3)}e^{-a_k(c_4)} (c_j ∈ ∂P), so with m_k := max_{∂P}|a_k|
≤ C_Mε̃ and 4m_k ≤ 1/8: log U^g_k(P) = da_k(P) + R_top, |R_top|_HS ≤ √N·2(4m_k)²e^{4m_k} ≤ 32√Ne^{1/2}C_M²C_♮²·E. Unrolling (3)
along the cone (contours stay in endpoint blocks, so every link the recursion reaches is a cone link):
  a_k = Q^ka_0 + Σ_{i<k}Q^{k-1-i}(e_i - ρ̃_i) on ∂P, hence da_k(P) = d(Q^ka_0)(P) + Σ_{m=0}^{k-1}d(Q^m(e_i - ρ̃_i))(P), i = k - 1 - m.
E-loc's steps (1)-(4) are linear identities for Q and apply verbatim (on cone data):
- d(Q^ka_0)(P) = n⁻⁴Σ_{y∈B_n(X)}Σ_{p∈sq_y}da_0(p), n = L^k, and da_0(p) = log U^g_0(p) - R_p with |R_p|_HS ≤ 32√Ne^{1/2}m_0(p)².
  *Linear part:* A := |n⁻⁴Σ_yΣ_{p∈sq_y}log U^g_0(p)|_HS ≤ (Σ_{p∈R_0}|log U_0(p)|²_HS)^{1/2} (E-loc step (3); gauge-invariant norm), and
  |log U_0(p)|²_HS ≤ 2Ns(U_0(p))/(1 - θ²/12) ≤ 2N(1 + δ_η)s(U_0(p)) (1 - cos t ≥ (t²/2)(1 - t²/12); angles ≤ θ_η).
  *Remainder:* a level-0 plaquette lies in ≤ n² squares sq_y (E-loc (3)), so T_R := n⁻⁴Σ_yΣ_{p∈sq_y}|R_p| ≤ n⁻²Σ_{R_0}|R_p| ≤
  32√Ne^{1/2}n⁻²Σ_{R_0}m_0(p)²; each in-plane link bounds ≤ 2 plaquettes of R_0 and |L(R_0)| ≤ 8n⁴, |R_0| ≤ 4n⁴, so Σ_{R_0}m_0² ≤
  2Σ_{L(R_0)}|a_0|² ≤ 2√8n²(Σ|a_0|⁴)^{1/2} ≤ 2√8n²√C_S·E. Hence **T_R ≤ K_R√C_S·E.**
- For each depth m, E-loc step (4): |d(Q^mf)(P)|_HS ≤ √8L^{-m}||f||_{ℓ²(R'_i(P))}. With f = ρ̃_i: b_m := √8L^{-m}ρ_m, ρ_m² :=
  Σ_{R'_i}|ρ̃|² ≤ 2N(1 + δ_η)Σ_{R'_i}φ. With f = e_i: Σ_m√8L^{-m}||e_i|| ≤ √8(L/(L - 1))·max_i||e_i||.
**(6) Collecting.** By E-loc step (5) (Cauchy-Schwarz with weights 1, L^{-m}): (A + Σ_mb_m)² ≤ ((2L - 1)/(L - 1))(A² + 8Σ_mL^{-m}ρ_m²) ≤
((2L - 1)/(L - 1))·N(1 + δ_η)·max{2, 16/κ}·[Σ_{R_0}s + κΣ_iΣ_{R'_i}φ] ≤ C_locN(1 + δ_η)·E (R_0 and the R'_i are disjoint sets of cone
terms). Therefore
  |X|_HS = |log U^g_k(P)|_HS ≤ √(C_locN(1 + δ_η)E) + T_R + √8(L/(L - 1))max_i||e_i|| + |R_top|
        ≤ √(1.2C_locN)·√E + [K_R√C_S·E + √8(L/(L - 1))C_e(√(2dC_S)E + r√(2.4N/κ)√E) + 32√Ne^{1/2}C_M²C_♮²E].
Every bracketed term is ≤ (const)·√η_AE·√E, since E ≤ √η_AE·√E and r√E = 1.011√NC_♮E ≤ 1.011√NC_♮√η_AE√E (r is evaluated
at the actual E: r = 1.011√NC_♮√E); the constants sum to C_2. So |X|_HS ≤ (√(1.2C_locN) + C_2√η_AE)√E ≤ √C'_AE·√E by
(Z5). X := g(X_P)·log U^g_k(P)·g(X_P)⁻¹ ∈ su(N) (P based at its corner X_P) has U_k(P) = e^X and the same HS norm. This proves the
claim at depth k with the SAME C'_AE, closing the induction; the size clause is (1). ∎
*Reading.* (i) No per-level constant is iterated: the induction re-derives C'_AE at each depth from a FIXED target 2C_locN,
and the depth-(k - 1) input enters only through the sizes in (1), which are then multiplied by √η_AE in (6) (the reviewer's point
(i)). (ii) MSG-loc (GAP) is not used: only MSG's sup bound (global ε̃) and (MS-Sob). (iii) The top term 32√Ne^{1/2}C_M²C_♮² dominates
C_2 (≈ 5·10⁷ at N = 2, L = 3, κ = 1); it is the price of bounding the top-level BCH term by sup sizes. (iv) The theorem shows that
(AE)'s hypotheses (i)-(ii) are consequences of (iii): (AE) is exactly the ε-regularity statement of CLS-red, and CLS-red's steps
α-β are subsumed. **Status: (AE) moves from OPEN to CONDITIONAL ⇐ (MS-Sob); the OPEN wall is (MS-Sob) ⇐[ARGUED] MSG-loc-dev +
MS-HLS + (SQ-dev).**
*Consequences for CLS-red / CLS-cone.* Take η_E := η_AE (N-4): C_cone = max{C'_AE/(2N), 2/η_AE} = 2/η_AE. (Z1) alone forces
η_AE ≤ ε_S²/C'' ≤ ε_M²/C'_AE ≈ (6.9·10⁻⁶)²/160 ≈ 3·10⁻¹³ (N = 2, L = 3, κ = 1), and (Z5) is smaller still (h7 C reports the numbers):
**C_cone ≳ 10¹²-10¹⁵**, depth-uniform.

## 27. Check h7 (criteria first: checks/h7_criteria.md 01:57:46 UTC; script checks/h7_term_an.py 02:08:39 UTC; records h7_out.txt, h7_time.txt)
First and only run (lock taken 02:50:02, released 02:50:04 UTC by one rmdir after waiting for another holder; load 2.39, 45%
free, nice 10, BLAS threads 1; 2.3 s, peak RSS 155 MB). No smoke run, no script edit after the run, no criterion edited.
**OVERALL: FAIL as pre-registered (A3); A1, A2, A4, B1, B2, C1, C2 PASS; soft A5 within limits.**
- **A1 PASS.** Real data: X_0^ℂ anti-Hermitian and traceless to 1.5·10⁻¹⁷, equal to NA-alg's real fixed point to 7.8·10⁻¹⁸, and
  no ascent direction or Haar sample beats W_0 (gap 0). ≤ 7 iterations.
- **A2 PASS.** Complex data: holomorphic stationarity residual ≤ 2.4·10⁻¹⁶; |X_0 - Ȳ| far below 9.2y² (printed ratio 0.000 at 3
  digits); |X_0|/(3y) ≤ 0.316.
- **A3 FAIL.** The holomorphic cases pass (CR defect of X_0^ℂ ≤ 5.0·10⁻⁹, of φ^ℂ ≤ 4.3·10⁻⁴ against the 10⁻³ limit), but the
  pre-registered CONTROL did not fail: the real-projection map applied to complex data gave CR defects 3.9·10⁻⁶ … 4.0·10⁻³ (median
  3.4·10⁻⁴), below the required 0.1. [inference, post hoc, no new run:] its non-holomorphic part enters only through Π(K) with
  |K| ≤ 9.2y² and a derivative O(y) relative to the leading Ȳ (y = 0.02), so the control is nearly holomorphic at this scale and
  the criterion did not discriminate. The holomorphy claim rests on the proof (uniform limits of holomorphic iterates), not on
  A3. The FAIL stands.
- **A4 PASS.** φ^ℂ = real φ to 4.7·10⁻¹⁶; local expansion at ≤ 1.0% of TERM-an (iii)'s bound; global Haar-shift form |Δ| ≤
  0.0011·θs (θ's bound is loose by ~10³).
- **A5 (soft).** Haar shift of the normalisation: |I_1 - I_2|/|I_2| = 3.9·10⁻⁴ (κu = 20), 1.5·10⁻³ (κu = 80), within MC limits;
  |I_2/I_0 - 1| = 1.8·10⁻⁵ at both κu (θ = 0.025): no growth with κu, as NORM-an predicts.
- **B1, B2 PASS.** det V = 1, tr H = 0 to 1.3·10⁻¹⁵; max ||H||/||Y|| = 1.000 (bound 4.19), max ||V - e^X||/||Y|| = 0.005 (bound
  9.2). B3: ||H - iY|| ≤ 1.0·(||X||||Y|| + ||Y||²).
- **C1, C2 PASS.** At (N, L, d, κ) = (2, 3, 4, 1): C_loc = 40, C'_AE = 160, C_♮ = 12.65, C_e = 1.88·10⁴, C_2 = 5.5·10⁷ (C_S = 1) to
  7.8·10⁷ (C_S = 10⁴), ε_M = 6.93·10⁻⁶ (A_ax = 12), **η_AE = 1.8·10⁻¹⁵ (C_S ≤ 10²) / 8.9·10⁻¹⁶ (C_S = 10⁴), closing 12.14 ≤ 12.65,
  C_cone = 1.1-2.3·10¹⁵.** N = 3: C'_AE = 240, η_AE = 4.4-8.9·10⁻¹⁶, C_cone = 2.3-4.5·10¹⁵. (Z5) binds, not (Z1).

## 28. Outcomes against the session-4 targets (§24) (ADDED AFTER the derivations; pointers only)
- **Target S6: MET in the reduction form.** (I_k^E)'' stated (§25.6). New PROVEN: TERM-an (every chain energy term and the SU(N)
  maximiser continue holomorphically to a chart-free, gauge-covariant domain, explicit bounds), NORM-an (the kernel
  normalisation is analytic on a g-INDEPENDENT width, by an exact Haar shift to the complex maximiser), POL (polar ⇄ chart ⇄
  MSG-log polydiscs, explicit constants), EXT, (R♯_∞). Theorem A5 (analytic main term: holomorphic on 𝔇_{2ε_1, s_5/4}, equal
  to the localised infimum on real small fields, gauge invariant, local densities without measurable selection):
  CONDITIONAL ⇐ (a5-G) [lane F / node N2 class], (a5-U), (a3-q) [lane D, classical], (MS-Sob). The radius is depth- and
  polymer-size-independent given (a5-G). Domain fixed (S3-7). Consistency (c1'') HF, (c2'') F-tree, (c3'') RLF-5/K7 (one
  integration item on widths), (c5'') recorded. "Not success" clauses avoided.
- **Target S7: MET.** Theorem AE-red: (AE) ⇐ MSG + (MS-Sob), PROVEN as an implication, every term bounded, induction and the
  closing inequality explicit (C'_AE = 2C_locN fixed first). It also shows (AE)'s (i)-(ii) follow from the energy cap (iii).
- **h7: OVERALL FAIL as pre-registered (A3: the control did not discriminate);** the rest PASS.

## 29. Tally (session 4) and hypotheses consumed
- **Session-4 items (unreviewed).** PROVEN-HERE, counted (2): Lemma TERM-an; Lemma NORM-an. CONDITIONAL (2): Theorem AE-red
  (⇐ MS-Sob; replaces the ARGUED "(AE) ⇐ MSG + MS-Sob"); Theorem A5 (⇐ (a5-G), (a5-U), (a3-q), MS-Sob). PROVEN, not counted:
  POL, EXT, (R♯_∞), A5 (D), (c1''), (c5''). HYPOTHESIS: (I_k^E)'' replaces (I_k^E)' (items (a3-q), (a4), (a5) = (a5-G) + (a5-U)).
  Status change: (AE) OPEN → CONDITIONAL ⇐ (MS-Sob); (MS-Sob) becomes the named OPEN wall in its place.
- **Whole file after session 4: 11 PROVEN-HERE / 6 CONDITIONAL / 7 ARGUED / 4 OPEN + 1 HYPOTHESIS.** PROVEN-HERE: PM, RS-lin, CL^J,
  R1^J, H-geo, HF, E-loc, MSG, MS-HLS, TERM-an, NORM-an. CONDITIONAL: RS-joint, HIST-sum, CLS-red, CLS-cone, AE-red, A5. OPEN:
  (MS-Sob), (SQ-dev) incl. MSG-loc-dev, (D1-b), (H-w). HYPOTHESIS: (I_k^E)''.
- **Hypotheses consumed.** TERM-an: NA-alg (a) (its proof, run on complex data). NORM-an: TERM-an. Theorem A5: (a5-G), (a5-U),
  (a3-q), Theorem AE-red, NA-IFT (complex version, same proof), NA-crit' ((FP♯') in (a5-G)), MSG. Theorem AE-red: MSG, (MS-Sob),
  E-loc steps (1)-(5), NA-alg (a)-(b), KQ (lower), RS (R1) ribbons (§15.4 β), (F1)-(F5).
- No change to PROOF.md, RLARGE.md, FLOW.md; integration item (c3'') for the lead. Nothing outside HIST.md, HIST_LOG.md,
  checks/h* edited. No commits, PRs, pushes, CL or axiom edits.
