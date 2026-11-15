# FLOW: the coupling flow (F) for the soft-kernel RG (lane C, opened 2026-10-27)

Scope. Lane C of the 4D Yang-Mills proof push: the nonperturbative coupling-flow theorem (node A5 / L4a-flow of
PROOF.md; hypothesis (F) of RLARGE.md §0 and §8.2; H-Bal-1 of agents/ym4d-existence/EXISTENCE.md) for the decision-4 RG
(S4' contour averaging, normalised soft gauge-covariant kernel; PROOF.md L5 [S9], Lemma D4-norm). This file is written
only by lane C. Status words as in PROOF.md: PROVEN-HERE, IMPORTED-AND-REVERIFIED, IMPORTED-NOT-YET-REVERIFIED, ARGUED,
OPEN, HYPOTHESIS ("given H" = a named hypothesis consumed from layer 1). Imported items are never load-bearing for a
PROVEN-HERE claim. Literature tags [read]/[read-skim]/[not-read] as in PROOF.md.

Inputs read for this file (read-only, by offset, 2026-10-27): PROOF.md L4 (L4a, L4a-flow, L4a-Π, L4b, L4c), L5 [S9]
(decision 4, D4-norm, GT-lat, R4D-lat), Theorem CE (statement), N5-triv block (Setting N5-0, Lemmas CT, N5-sl, N5-coer,
N5-loc), LF-count (l.4071-4100); RLARGE.md §0, §1, §1A, §3, §4 (GT-lat'), §8; LINEAR_PACKAGE.md §1; literature/NOTES.md
§9 (CMP 109); EXISTENCE.md H-Bal-1 (l.100-115).

File order. §0-§2 were written at 2026-10-27 23:04 UTC, before any derivation in §3 onward and before any check
criteria or script. §0-§2 are not edited after the derivations start; outcomes are pointers in §12, added afterwards.

---

## 0. Conventions fixed for this file

- **Levels** as RLARGE §0: level k = after k RG steps, k = 0 the bare lattice, k = K the unit lattice; d = 4, L ≥ 3 odd,
  G = SU(N), N ≥ 2. Everything at level k is in level-k units.
- **Coupling variable.** u_k := 1/g_k². Action normalisation of RLARGE §0: level-k Wilson term u_kΣ_p s(U_p),
  s(U) = 1 - N^{-1}Re tr U. So u = β_Wilson = 2N/g_std², where g_std is the coupling of (1/(4g_std²))∫F^aF^a with
  tr(T^aT^b) = δ^{ab}/2.
- **Lie coordinates.** V_b = exp(Σ_a B^a_b t_a), {t_a} a basis of su(N) orthonormal for ⟨X, Y⟩ := -(1/N)tr(XY)
  (so ||t_a||²_HS = N). In these coordinates s(e^X) = ½Σ_a(X^a)² + O(X⁴), i.e. the Hessian of Σ_ps(U_p) at U = 1 is, in
  each colour, the abelian plaquette form K (symbol δ_μν|ŝ|² - ŝ_μŝ_ν^*, ŝ_α = e^{ip_α} - 1).
- **The β-functional.** For a functional F of a level-k field, translation invariant (infinite volume), gauge
  invariant, B_4-covariant, C² at the trivial field with exponentially decaying Hessian, β[F] := Σ_z z_1z_2Π^F_12(z),
  Π^F the Hessian at V = 1 along one colour direction (all colours agree, §3). This is L4a-Π's β (CMP 109 (1.22)).
  β[Σ_ps(U_p)] = 1 (c17(A)). For a polymer family that is not B_4-symmetric, β is applied to its B_4-orbit sum.
- **Sign.** Density e^{-S}. If the step output S_{k+1} has marginal part (u_k - β_k)·Σs, then u_{k+1} = u_k - β_k; β_k > 0
  is asymptotic freedom (the coupling grows toward the IR). This is CMP 109 (0.18), 1/g_0² = 1/g_1² + β_1 [read, NOTES §9.3].
- **Standard coefficient.** b_0 = 11N/(48π²) (L4b, IMPORTED-AND-REVERIFIED); d(1/g_std²)/d ln μ = 2b_0 = 11N/(24π²).
  In our normalisation one RG step (μ → μ/L) at one loop shifts u by 2N·2b_0 log L = (11N²/(12π²)) log L
  =: β_0^std log L (≈ 0.0929N² log L; this is LF-count's "β'_B ≈ 4Nb_0" [PROOF l.4089, inference there]).
  **[RFL-fix normalisation wording, FN-1]** Exactly: β_0^std = 2N × 2b_0 with b_0 = 11N/(48π²) (the coefficient of
  β(g) = μ dg/dμ = −b_0g³), i.e. 2N × 11N/(24π²) = 11N²/(12π²); it is NOT 2N × b_0. Pointer: LF-count's β'_B line is now
  PROOF l.4114-4116 (the "l.4089" above is stale). **[RFL3-fix S3-4] "l.4114-4116" is itself wrong for the current
  PROOF bytes: the β'_B line is PROOF l.4162, inside Proposition LF-count (l.4144-4172).**

## 1. Target (pre-stated): Theorem FLOW

**Setting.** The exact soft chain of RLARGE §0 with bare coupling g_0 and kernels at κ/g_k² (κ > 0 fixed). At each
level the step output is written in renormalised form (Balaban's (0.28)-(0.29) form, CMP 109 [read]): tree part
u_k·𝒯_{k+1} with 𝒯 the u-stripped tree functional of the chain, plus polymers; the effective coupling of level k+1 is
defined by subtracting the marginal part of everything that is not tree-level (definition Def F-g, §3). The coupling
sequence (g_k) is then a deterministic function of (g_0, K, L, N, κ), defined as long as the per-level representation
exists.

**Theorem FLOW (target; all quantifiers).** There are constants β_0' > 0, R ≥ 0, C_ρ, γ_0 > 0 depending only on
(N, L, κ) and on the constants of the layer-1 hypotheses named below (never on K, the torus T, or the level k), such
that, given those hypotheses:

- **(F-1) One-loop coefficient.** The per-step one-loop coefficients b_k (g-independent numbers: the β-functional of the
  one-loop part of step k, §5) obey, for all 0 ≤ j ≤ n,
    |Σ_{k=j}^{n-1} b_k - β_0'(n - j) log L| ≤ R,
  with β_0' COMPUTED for the soft kernel (the polarisation-tensor route of L4a-Π applied to the Gaussian integration of
  the step), and compared with β_0^std of §0. Sub-target: b_k → b_∞ = β_0' log L as k → ∞, with a rate.
- **(F-2) Remainder.** The full per-step coupling shift β_k := u_k - u_{k+1} satisfies β_k = b_k + ρ_k with
    |ρ_k| ≤ C_ρg_k² + |δβ_k|  whenever g_0, …, g_k ∈ (0, γ_0],
  where C_ρ is explicit in the polymer norms of the step output (which polymer terms renormalise the coupling is listed;
  the B_4 averaging isolates the tr F² coefficient through L4a-Π / GT-lat'), and δβ_k are RLF's large-field coupling
  shifts, |δβ_k| ≤ g_k⁶ (RLF-0 / (W1-ret') (a)).
- **(F-3) Discrete flow.** For γ ∈ (0, γ_0] with C_ργ² ≤ ½β_0' log L, put β_± := β_0' ± C_ργ²/log L. If g_0, …, g_{n-1}
  ∈ (0, γ], then for all 0 ≤ j ≤ n:  β_-(n - j) log L - R ≤ u_j - u_n ≤ β_+(n - j) log L + R.
- **(F-4) Tuning (bare coupling).** Put g_1 := (γ^{-2} + R)^{-1/2}. For every K ≥ 1 and every g ∈ (0, g_1] there is a bare
  coupling g_0 = g_0(ε, g) ∈ (0, γ], ε = L^{-K}, with g_k ∈ (0, γ] for all k ≤ K and g_K = g; and then
    1/g² + β_-(K - k) log L - R ≤ 1/g_k² ≤ 1/g² + β_+(K - k) log L + R  for 0 ≤ k ≤ K.
  The constants γ, g_1, β_±, R are independent of K and of the torus side (uniformly in volume).

**Consumers.** (F-3)/(F-4) is the form RLARGE (F) and EXISTENCE H-Bal-1 consume, with the additive constant R stated
explicitly (whether R can be taken 0 is part of the outcome: §11).

**Hypotheses that may be consumed (each to be named as "given H" where used):**
- (SF) the small-field package at each level (RLARGE §8.2: (DF1)-(DF4) + the L4a-form contraction, nodes N2, N4, N5,
  N6), in the form of an analytic polymer representation of the step output, with a g-expansion of its non-tree part
  (to be stated precisely as (SF-g) in §4);
- (RLF) the per-level large-field coupling shift bound |δβ_k| ≤ g_k⁶ (RLARGE §1A (RLF-0) / §8.2 (W1-ret') (a));
- continuity of the step output in the coupling (for the shooting argument);
- an infinite-volume (translation-invariant) form of the polymer activities (for volume uniformity).

**Failure modes (each a valid outcome).** (FL-F1) the soft kernel renormalises the coupling at tree level (then u is
not the marginal coefficient of the tree action and the flow must be redefined); (FL-F2) the soft kernel's one-loop
coefficient differs from β_0^std (scheme dependence at one loop: possible a priori, since the soft kernel adds
normalisation factors 𝒩 at every level); (FL-F3) the remainder is not O(g²) in the polymer norms (e.g. earlier
renormalised polymers regenerate an O(1) marginal part when re-expressed at the next level); (FL-F4) the shooting
argument needs monotonicity or a continuity that the layer-1 hypotheses do not give.

## 2. Steps and checks (pre-stated)

1. **One-loop coefficient** from the Gaussian integration of the step (L4a-Π route): tree-level marginal coefficient of
   the soft step; one-loop telescoping over steps; the value of β_0' and its relation to β_0^std; the depth limit.
2. **Remainder bound** from the polymer representation: Cauchy bound of the β-functional by the polymer norm; which
   polymer terms renormalise the coupling; why earlier renormalised polymers do not regenerate a marginal part; the
   B_4 isolation of the tr F² coefficient (L4a-Π, GT-lat', D4-norm) and the identification of GT-lat''s c̄ with β.
3. **Discrete flow analysis and bare-coupling tuning** (elementary, written in full).

**Checks (criteria files before scripts; NUMERIC LOCK and machine limits as briefed):**
- f1: tree level of the soft step on the S4' root-map symbol (L = 3; several κ): transversality; marginal coefficient
  of the coarse tree form equals 1; the remainder is O(p⁴); alias components of the tree background.
- f2: a log-coefficient check for the soft kernel as an IR regulator (a channel of the one-loop computation where the
  universal coefficient is explicit), including κ-independence.
- f3: lattice universality of the remaining one-loop channel (sharpening L4b's c2(B), which was 0.94-1.10).
- f4: the discrete flow and the shooting argument on admissible synthetic remainders (an arithmetic check of (F-3),
  (F-4) and their constants).

---
# Derivations (written after §0-§2)

## 3. Definitions and the β-functional

**3.1 The u-stripped soft kernel (exact rewriting).** For a coarse link c write M := M̄_c(U) = WP (polar decomposition,
W ∈ U(N), P = (M^*M)^{1/2} ≥ 0; ||M||_op ≤ 1). Since Re tr P = tr P,
  1 - N^{-1}Re tr(V^{-1}M) = (1 - N^{-1}tr P) + k̃(V, M),   k̃(V, M) := N^{-1}Re tr((1 - V^{-1}W)P) ≥ 0,
(k̃ ≥ 0 because |Re tr(YP)| ≤ tr P for unitary Y), with k̃ = 0 iff V = W when P > 0. With X := W^{-1}V (Haar),
𝒩(M) = e^{-κu(1 - N^{-1}tr P)}𝒩'(P), 𝒩'(P) := ∫exp(-κu N^{-1}Re tr((1 - X)P))dX. Hence exactly
  -log k_c(V, U) = κu·k̃(V_c, M̄_c(U)) + log 𝒩'(P_c(U))   (u = 1/g_k² at step k).
The shrinkage term (1 - N^{-1}tr P) cancels identically ("only the distance from the polar part is charged",
LINEAR_PACKAGE §1.3, now as an exact identity). log 𝒩'(P) = -((N²-1)/2)log(κu) + O(1): it carries no power of u and is
part of the one-loop functional (§5).
**[RFL-fix §3.1, per HIST Lemma HF (HIST.md §14.2, read-only)]** The sentence "log 𝒩'(P) = -((N²-1)/2)log(κu) + O(1): it
carries no power of u" is correct for N = 2 only. For N ≥ 3 and det W ≠ 1, X = W⁻¹V ranges over the coset W⁻¹SU(N), on
which the exponent's minimum is d(M) := N⁻¹(tr P − Re tr(W_0⁻¹M)) > 0 (W_0 an SU(N) maximiser of Re tr(W'⁻¹M)), and
k̃(V, M) = φ_M(V) + d(M) (Lemma HF (i)); hence log 𝒩'(P) = −κu·d(M) + log∫exp(−κuφ_M(W_0X'))dX', which carries the power u
through −κu·d(M). The identity −log k_c = κu·k̃ + log 𝒩'(P) is exact and unchanged; what changes is the bookkeeping: the
exact tree exponent is κuφ (HIST's tower 𝓔_k), not κuk̃, and 𝒯_k ≥ 𝓔_k with equality for N = 2. Since 0 ≤ d(M) ≤ α²/(2N²)
(α = arg det M, Lemma HF (ii)) and d = O(y⁶) in the contour spreads (Lemma HF (iii)), d has no quadratic, cubic, quartic or
quintic part at the trivial field: every Hessian at 1 and every derivative of order ≤ 5 at 1 used in this file is the same
for 𝒯_k and 𝓔_k, so F-tree, F-bg, F-ren and all β-level statements below are unaffected (HIST: "β[𝓔_k] = 1").

**Def F-strip (the tree tower; uniform κ).** 𝒯_0(U) := Σ_ps(U_p); 𝒯_{k+1}(V) := min_U[𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U))]
(minimum over a compact group power; it exists). By induction 𝒯_k ≥ 0 = 𝒯_k(1), and 𝒯_k is gauge invariant, invariant
under coarse translations and B_4 (D4-norm (1): the S4' family is B_4-symmetric), and its Hessian at the trivial field is,
in each colour, the linearised chain form H_k of LINEAR_PACKAGE Setting SC with κ_i ≡ κ (envelope theorem at a minimum
that is nondegenerate on the gauge slice, N5-coer). Φ_{j←n} denotes the tree background map (the minimisers U_j, …, U_{n-1}
of the tower as functions of U_n = V; unique and smooth near the trivial field, given (SF-bg) of §4).

The kernel coupling in the stripped tower is the same κ at every level. This is the point of the renormalised form: at
step k the input is u_k𝒯_k + (renormalised terms) and the kernel is κu_k, so the ratio is κ at every level, and the
tree part of the output is u_k𝒯_{k+1}. (In bare normalisation the kernel stiffness relative to u_0 is κu_i/u_0 → 0 at
coarse levels, and loops are as large as the tree: the per-step renormalised form is necessary, as in CMP 109 (1.3).)

**Def F-g (effective coupling; CMP 109 (1.20)-(1.22) for the soft chain).** Suppose the level-(k+1) density is written,
in infinite volume and on the small-field domain, as e^{-S_{k+1}} with S_{k+1} = u_k𝒯_{k+1} + Γ_k + 𝒮_k, where Γ_k(V) is
the one-loop functional of step k (§5.1) and 𝒮_k collects all other field-dependent terms (each of the classes of
§6.1). Define
  u_{k+1} := u_k + β[Γ_k] + β[𝒮_k] (equivalently: u_{k+1} := β[S_{k+1}], since β[𝒯_{k+1}] = 1 by Lemma F-tree),
  β_k := u_k - u_{k+1},   and the renormalised remainder S_{k+1} - u_{k+1}𝒯_{k+1}, which has β = 0.
The β-functional is taken in infinite volume (CMP 109 takes Π "after the limit T^{(j+1)} → Z^d", NOTES §9.4 [read]), so
u_{k+1} does not depend on the torus: finite-volume differences are polymers of the representation, not couplings.

**Lemma F-Π (colour structure and a Cauchy bound for β): PROVEN-HERE.** Let {F(X)} be a translation-covariant family of
level-(k+1) polymers (X a *-connected union of M-cubes, d(X) ≥ |X| - 1 its tree length in M-units), each F(X) a function
of V|_X, analytic in the normalised Lie coordinates on the polydisc D_α(X) := {|B^a_b| ≤ α ∀b ⊂ X, a} (other links at 1),
with |F(X)| ≤ ||F||_{κ_p}e^{-κ_pd(X)} on D_α(X), and F := Σ_XF(X) gauge invariant. Then:
(i) the Hessian of F at V = 1 is δ_{ab} × (a real kernel Π^F) in colour;
(ii) Σ_z|z_1z_2||Π^F_12(z)| ≤ C_Π||F||_{κ_p}, C_Π := 64M⁶α^{-2}Σ_{n≥1}n³(6400e^{-κ_p})^{n-1}, finite for κ_p > log 6400 ≈ 8.76
(for κ_p ≥ 457, Theorem CE's requirement, the sum is ≤ 1 + 10^{-193}); in particular |β[F]| ≤ C_Π||F||_{κ_p}, and Π^F decays
exponentially, so L4a-Π applies to F when F is also B_4-covariant (or after the B_4 orbit sum).
*Proof.* (i) A constant gauge transformation h fixes V = 1 and acts on every tangent coordinate by Ad_h, so for each pair
of links (b, b') the Hessian block is an Ad-invariant bilinear form on su(N); su(N) is absolutely irreducible under Ad
(End_Ad = R, as in GT step 5 / GT-lat' (i)), so the block is a multiple of the invariant inner product, i.e. δ_{ab}Π(b, b')
in orthonormal coordinates. Gauge invariance also gives DF(1) = 0 (an Ad-invariant element of su(N)* vanishes).
(ii) Π^F_12(z) = Σ_{X ⊃ b_0, b_z}∂²F(X)/∂B^a_{b_0}∂B^a_{b_z}(0), b_0 = (0, e_1), b_z = (z, e_2) (distinct links). The
two-variable Cauchy estimate on the bidisc of radius α gives |∂²F(X)(0)| ≤ α^{-2}||F||e^{-κ_pd(X)}. A link lies in ≤ 16
M-cubes; the number of *-connected X with n cubes containing a given cube is ≤ 80^{2(n-1)} ((g3), as used in RLARGE
§8.4 (P1)); b_z ranges over ≤ 4M⁴n links of X; |z_1z_2| ≤ (Mn)²; d(X) ≥ n - 1. Summing,
Σ_z|z_1z_2||Π_12(z)| ≤ 16·4M⁶α^{-2}||F||Σ_nn³80^{2(n-1)}e^{-κ_p(n-1)}. ∎

**Lemma F-id (GT-lat' orbit coefficients are coupling shifts): PROVEN-HERE.** Let F_0 be a gauge-invariant local functional
(finite support, C² at 1), F := Σ_xτ_xF_0 its translation sum, B_4-covariant after the orbit sum, and Q_{F_0}(Φ) =
c̄Σ_{planes a}||Φ_a||²_HS its GT-lat' quadratic part (orbit-summed, GT-lat' (ii)). Then β[F] = 2N c̄ (per site of the lattice on
which F lives). *Proof.* In one colour the Hessian H_0 of F_0 at 1 is a gauge-invariant quadratic form of finite range, so
(lattice Poincaré lemma on a box, as in GT-lat step 1) H_0(A, A) = h_0(dA, dA) for a finite-range quadratic form h_0 on
plaquette variables. The translation sum has symbol Π̃(p) = ŝ^∧(p)^†ĥ(p)ŝ^∧(p), ĥ(0) = Σ over all pairs of the entries of
h_0 (per plane pair); after the B_4 orbit sum ĥ(0) = c·1 on Λ²R⁴ (absolute irreducibility, GT-lat' (ii)), and
ŝ^∧†(c·1)ŝ^∧ = c(δ|ŝ|² - ŝŝ^†), so β[F] = c. On GT's reference data 𝓛Φ (constant curvature φ in the plane 12, one colour,
d𝓛Φ = Φ exactly), H_0(𝓛Φ, 𝓛Φ) = h_0(Φ, Φ) = cφ² (sum of all entries of h_0 in the plane 12, which is the plane-12 entry of
ĥ(0)), and H_0(𝓛Φ, 𝓛Φ) = 2Q_{F_0}(Φ) = 2c̄||Φ_12||²_HS = 2c̄Nφ² (||t_a||²_HS = N, §0). So c = 2Nc̄. ∎
*Consequence.* RLARGE (RLF-0)'s δβ_k = (2N/L⁴)(1/6)Σ_{[S]}tr T_{[S]} is a shift of u_{k+1} in the normalisation of this file
(β = 2Nc̄, c̄ = (1/6)Σtr T; the factor L^{-4}, per-level-k-cube placements per level-(k+1) site, is RLARGE's and is not
re-derived here).

## 4. Hypotheses consumed from layer 1 (each "given H" where used)

- **(SF-bg)** [part of nodes A1-A3: the soft background field] The tree tower Φ_{j←n} and the functionals 𝒯_k are real
  analytic on a complex neighbourhood of the trivial field (in normalised Lie coordinates, uniformly in k), with
  exponentially local derivatives of every order ≤ 4 at the trivial field. (The second-order part, H_k exponentially local,
  is PROVEN-HERE upstream: N2-exp' (ii), as quoted in N5-loc; the higher orders are not.)
- **(SF-g)_k** [the L4a-form content of (SF)_k, RLARGE §8.2; Balaban's (2.13)-(2.15) structure, NOTES §9.5 [read]] In the
  representation of Def F-g, 𝒮_k = Σ_XẼ_k(X)∘Φ + Σ_XE^{≥2}_k(X) + 𝒮^{LF}_k + c_k, where: Ẽ_k are the renormalised level-k
  polymers (β[ΣẼ_k] = 0) evaluated at the tree background; E^{≥2}_k are level-(k+1) polymers as in Lemma F-Π with
  ||E^{≥2}_k||_{κ_p} ≤ E_2g_k² (the higher-loop terms of the fluctuation integral, the fluctuation corrections of the
  earlier polymers Ẽ_k, and the small-field cutoff tails, which are O(e^{-c/g²})); 𝒮^{LF}_k = (large-field returned terms)
  = -δβ_k𝒯_{k+1} + (remainders with β = 0) [RLARGE (RLF-2)]; c_k a c-number. Constants E_2, α, κ_p, M uniform in k, K, T,
  valid whenever g_0, …, g_k ∈ (0, γ_0].
  ~~[RFL-fix FR-2 (sign), first version, 01:0x UTC: "read 𝒮^{LF}_k = +δβ_k𝒯_{k+1}", following RLARGE v1 l.650]~~
  **[RFL3-fix S3-7, timestamps] "01:0x" and "01:3x" are not times. What the log records: the first version was applied in
  the 01:00-01:15 UTC fix pass and the correction in the 01:30-01:40 UTC K1/K4 window (FLOW_LOG session-3 entries); the
  exact minutes were not logged and are not recoverable from file metadata (FLOW.md has been rewritten since).**
  **[RFL-fix FR-2, re-derived 01:3x UTC on the lead's K1 note; CORRECTED] The sign as originally written, 𝒮^{LF}_k =
  −δβ_k𝒯_{k+1} + (β = 0), is the right one** for δβ_k as RLARGE defines it (R1 (iii) / R1^J add +δβΣs(U_p) to the LOG of the
  integrand, RLARGE v2 l.100-101; HIST (c4) [RH2-fix 9]). Derivation in this file's conventions (§0: density e^{-S}, u = β[S]):
  log(density) += δβ_kΣs ⇔ S_{k+1} −= δβ_kΣs; Σs = 𝒯_{k+1} + (Σs − 𝒯_{k+1}) with β[Σs] = β[𝒯_{k+1}] = 1 (c17(A), Lemma F-tree),
  so the second piece has β = 0; hence **β[𝒮^{LF}_k] = −δβ_k: the large-field shift ~~LOWERS u_{k+1}~~ shifts u_{k+1}
  by −δβ_k [RFL3-fix S3-7: it lowers u_{k+1} only when δβ_k > 0].** **[RFL3-fix S3-7, the level of Σs]** The display above
  takes Σs on the level-(k+1) field. If Σs is the level-k sum Σ_ps(U_k(p)), as HIST l.296 writes it, it enters S_{k+1}
  through the tree background as Σs∘Φ, and β[Σs∘Φ] = β[Σs] = 1 by Lemma F-ren (i) with β[Σs] = 1 (c17(A)), up to O(δβ_k·g²)
  loop corrections that belong to the E^{≥2} part of ρ_k; either way β[𝒮^{LF}_k] = −δβ_k. The first-version FR-2
  fix (and Prop. F-rem's proof and §6.1 (d), which wrote +δβ_k) followed RLARGE v1 l.650 ("1/g̃_{k+1}² = flow(1/g̃_k²) +
  δβ_k^{sea}"), which RLARGE v2 records as conflict K1 and abandons. Consequences (all checked): ρ_k = −β[ΣE^{≥2}_k] + δβ_k
  (Prop. F-rem, corrected below); |ρ_k| ≤ C_ΠE_2g_k² + |δβ_k| unchanged; (RLF-δ)_k is a bound on |δβ_k| only, unchanged; R,
  β_±, the e^{aR} factors of §19A and Theorems F-flow/F-tune use only |ρ_k|, unchanged. Def F-g's u_k already contains
  the δβ's (through β[𝒮_k]), so (F_R) of Theorem F-flow is a statement about RLARGE's shifted g̃_k, not about an unshifted flow.
- **(RLF-δ)** |δβ_k| ≤ g_k⁶ for g_k ≤ γ_0 (RLARGE §1A (RLF-0); in the induction (W1-ret')_k (a) gives
  |δβ_k^{sea}| ≤ Cg_k^{-6}e^{-a_♯/g_k²} ≤ g_k⁶). Only this per-level bound is used: no flow input.
  **[RFL-fix FI-1, FI-2 (B6); binding quantifier]** RLARGE §1A states RLF "for every … coupling sequence with g_K ≤ g_0
  obeying (F)" (RLARGE l.66-68, l.122-125); REVIEW_PLD_S1_S2 B6 shows that quantifier is false as stated (for sequences with
  β_+ < β_1 the level-k field is at strong coupling). This file does NOT consume that form. What is consumed is the
  requantified per-level form: **(RLF-δ)_k: along the chain's own coupling sequence (Def F-g), if g_0, …, g_k ∈ (0, γ_0] and
  (F_R) holds on [0, k] for that sequence, then |δβ_k| ≤ g_k⁶**; likewise (SF-g)_k is consumed along the chain's own sequence,
  given (F_R) on [0, k] only. The chain's own sequence has β_+ ≥ β_0^std = β_1 and β_- → β_1 as γ → 0 (Theorem F-flow), which
  is B6's admissible class. **Requirement on lane RLARGE (recorded, not discharged here):** its (I_k) → (I_{k+1}) induction
  must deliver (RLF-δ)_k and (SF-g)_k from (F_R) on [0, k] for the chain's own sequence, never from (F) on [0, K] or from g_K.
  Without that, Lemma F-ind's non-circularity (§9) is a statement about this file's constants only.
- **(SF-cont)** For each k, g_0 ↦ u_{k+1}(g_0) is continuous on 𝒜_k := {g_0: g_0, …, g_k ∈ (0, γ_0]} (Balaban: β_j is
  "smooth ... uniformly bounded on this interval together with all derivatives", CMP 109 p.264 [read, txt]).
- **(SF-∞)** The polymer activities of non-wrapping polymers are torus-independent (infinite-volume translation-covariant
  family); wrapping polymers are bounded in the same norm (so Def F-g's infinite-volume β is the coupling of every torus).
- **(UNIV-1L)** [OPEN, §5.5] There is R_0 < ∞ such that |Σ_{k<n}b_k - β_0^std n log L| ≤ R_0 for all n ≥ 0.
  [S2] Now Theorem UNIV (§18): PROVEN given (U-IR), (U-loc); the session-2 status is in §20.
  [RFL-fix] The quantifier "for all n" refers to the chain's own one-loop numbers b_k (g-independent); (UNIV-1L) is never
  asserted for "every sequence obeying (F)". (U-loc) is proven in §23 (session 3); (U-IR) is restated precisely in §18.

## 5. Step 1: the one-loop coefficient

### 5.1 The one-loop functional of a step
At step k, with input u𝒯_k (u = u_k) and kernel κu, the integrand in U = U_k is exp(-u[𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U))])·
Π_c𝒩'(P_c(U))^{-1} (§3.1), gauge fixed on the slice of FP-ab (N5-0) with Faddeev-Popov factor Δ_FP **[RFL7-fix S7-1] (Δ_FP(U_0) := |det χΓ|·det(hh^*)^{-1/2},
the exact factor of Lemma FP-exact (§52); NOT FP_U^{-1} of NA-FP (iii), which differs by the U_0-dependent det(Δ')^{1/2})**. Laplace expansion at the
tree minimiser U* = Φ_{k←k+1}(V) gives -log∫ = u𝒯_{k+1}(V) + Γ_k(V) + O(1/u) + c-numbers, with the one-loop functional
  Γ_k(V) := ½log det'[Hess_U(𝒯_k + κΣk̃(V, ·))(U*)]_{slice} - log Δ_FP(U*) + Σ_clog 𝒩'_1(P_c(U*)),
𝒩'_1(P) := the u-independent factor of the Gaussian approximation of 𝒩'(P) (𝒩'(P) = (2π/(κu))^{(N²-1)/2}𝒩'_1(P)(1 + O(1/u))).
b_k := -β[Γ_k] (given (SF-bg), Γ_k is gauge invariant, B_4- and translation-invariant, C² at 1, with exponentially local
Hessian: the Hessian is ½tr(𝒞H'') - ½tr(𝒞H'𝒞H') + (FP and 𝒩'_1 terms), 𝒞 the N5-triv covariance (Lemma CT bounds,
PROVEN-HERE upstream) and H', H'' the background derivatives of the fluctuation operator, exponentially local by (SF-bg)).
b_k is a g-independent number depending on (N, L, κ, k).

### 5.2 Lemma F-tree (the soft step does not renormalise the coupling at tree level): PROVEN-HERE
*Claim.* For every k ≥ 0, every κ > 0 and odd L ≥ 3: β[𝒯_k] = 1. Equivalently, in each colour the transverse inverse
symbol Ĝ_k := (Ĥ_k|_⊥)^{-1} (in level-k units) satisfies |ŝ(p)|²Ĝ_k(p) → P_⊥(n) as p = tn → 0, for every direction n.
*Proof.* Per coarse momentum p with aliases q_K = (p + 2πK)/L, K ∈ {0, …, L-1}⁴, the one-step tree form is the minimum of
½L⁴Σ_Ka_K^†Ĥ_k(q_K)a_K + (κ/2)|b - Σ_KQ̃_Ka_K|² (Q̃_K := e^{iq_K·o}Q̂_root(q_K); the L⁴ comes from Fourier normalisation,
f1). Root covariance Q_root∘d = d∘ev (LINEAR_PACKAGE §1.2; f1 (G): Q̂(q)ŝ(q) = ŝ(Lq) to 8e-15) means fine gradients map
to coarse gradients, so for transverse b the fine gradient components decouple (they can absorb any coarse-gradient part of
the residual at zero cost), and with Ĥ_k = Ĝ_k^{-1} invertible on fine transverse vectors at q ≠ 0:
  Ĝ_{k+1}(p) = κ^{-1}P_⊥(p) + 𝒬(Ĝ_k)(p),  𝒬(G)(p) := L^{-4}P_⊥(p)Σ_KQ̃_K(p)P_T(q_K)G(q_K)P_T(q_K)Q̃_K(p)^†P_⊥(p)
(the Gaussian/Schur formula; f1 (B) checks it against the direct pseudo-inverse formula, 6e-13). Induction hypothesis:
(a) Ĝ_k is bounded on {|q mod 2π| ≥ δ} for every δ > 0; (b) |ŝ(q)|²Ĝ_k(q) → P_⊥(n) as q = tn → 0. Base: Ĝ_0 = P_⊥/|ŝ|²
exactly. Step: in 𝒬(Ĝ_k)(p) the K ≠ 0 terms have q_K bounded away from 0 mod 2π for small p, so by (a) they are bounded;
the K = 0 term is L^{-4}P_⊥Q̃_0P_T(p/L)Ĝ_k(p/L)P_TQ̃_0^†P_⊥ with Q̃_0(p) → L·1 (the contour integral of a constant field
is L·A_μ; f1 (G)), |ŝ(p)|²/|ŝ(p/L)|² → L² and, by (b), |ŝ(p/L)|²Ĝ_k(p/L) → P_⊥(n). So |ŝ(p)|²Ĝ_{k+1}(p) → L^{-4}·L²·L²·P_⊥(n)
= P_⊥(n): (b) at k+1. (a) at k+1: a singularity of 𝒬(Ĝ_k)(p) needs some q_K ≡ 0, i.e. p ≡ 0. Finally 𝒯_{k+1} is gauge
invariant, B_4-covariant and has exponentially local Hessian (N2-exp' (ii), as quoted in N5-loc), so by L4a-Π
Ĥ_{k+1}|_⊥ = β|ŝ|²P_⊥ + O(p⁴), i.e. |ŝ|²Ĝ_{k+1} → P_⊥/β; hence β[𝒯_{k+1}] = 1. ∎
*Reading.* Failure mode FL-F1 does not occur: the tree action's marginal coefficient is the input coupling, for every κ,
every depth, and every L. κ (and the S4' structure) enter only the O(p⁴) part (f1 (C), (D)).

### 5.3 Lemma F-bg (the tree background is smooth: alias components are O(p³)): PROVEN-HERE
*Claim.* For transverse coarse b at momentum p, the minimiser's fine transverse components are
a_K = L^{-4}Ĝ_k(q_K)Q̃_K^†Ĝ_{k+1}(p)^{-1}b, and for K ≠ 0, ||ŝ(q_K)∧a_K|| = |ŝ(q_K)||a_K| ≤ C|p|³|b| as p → 0; the K = 0
component is a_0 = L^{-1}b(1 + O(p)) (the smooth interpolation).
*Proof.* Put r := P_⊥(b - Σ_KQ̃_Ka_K) (the transverse residual; the longitudinal one is absorbed by fine gradients).
Stationarity in a_K (transverse part): L⁴Ĥ_k(q_K)a_K = κP_T(q_K)Q̃_K^†r, so a_K = κL^{-4}Ĝ_k(q_K)Q̃_K^†r, hence
P_⊥Σ_KQ̃_Ka_K = κ𝒬(Ĝ_k)r and b = r + κ𝒬(Ĝ_k)r = κ(κ^{-1} + 𝒬(Ĝ_k))r = κĜ_{k+1}r, i.e. κr = Ĝ_{k+1}^{-1}b; this is the
displayed formula (P_T's implicit). Since κr ∈ range P_⊥, Q̃_K^†κr = (P_⊥Q̃_K)^†κr, and P_⊥Q̃_K =
P_⊥Q̃_str,K (Q_root = Q_str - d∘h and P_⊥ŝ = 0). Q̃_str,K is diagonal with entries Π_α(1D Dirichlet factors); for K ≠ 0 pick
α with K_α ≠ 0: the factor L^{-1}Σ_{y_α}e^{iq_α(y_α - o)} vanishes at p_α = 0 and is analytic, so ||Q̃_str,K|| ≤ C|p|.
Ĝ_k(q_K) is bounded (Lemma F-tree (a)) and ||Ĝ_{k+1}(p)^{-1}|| = O(|p|²) (Lemma F-tree). For transverse a,
|ŝ∧a| = |ŝ||a|. ∎ (f1 (E): c(0.02)/c(0.01) ∈ [7.46, 8.02].)

### 5.4 Lemma F-ren (renormalised terms stay renormalised under the tree background map): PROVEN-HERE
*Claim.* Let F be a functional of the level-j field, gauge invariant, B_4- and translation-invariant, C² at 1 with
exponentially local Hessian. Then for every n > j: (i) β[F∘Φ_{j←n}] = β[F]; in particular (ii) β[F] = 0 ⇒ β[F∘Φ] = 0, and
(iii) β[𝒯_j∘Φ_{j←n}] = 1.
*Proof.* One step suffices (Φ_{j←n} is a composition of one-step maps, each preserving the hypotheses: the linearised
one-step map is exponentially local by N2-exp, and gauge/B_4 covariance is inherited). DF(1) = 0 (Lemma F-Π (i)), so the
Hessian of F∘Φ at 1 is (DΦ)^THess F(DΦ); per coarse momentum its symbol is L^{-4}·L⁸Σ_Ka_K^†Π̂_F(q_K)a_K (the a_K of Lemma
F-bg as linear maps of b; the Fourier factors as in f1), where only transverse parts of a_K enter (Π̂_F is transverse by (G)).
F∘Φ is itself gauge invariant, translation invariant (coarse) and B_4-covariant with exponentially local Hessian, so
L4a-Π applies to it and β[F∘Φ] = lim_{t→0}e^†Π̂_{F∘Φ}(tn)e/|ŝ(tn)|² for any unit transverse e and direction n. In this
limit: the K ≠ 0 terms are O(p⁶) (Π̂_F(q_K) bounded, a_K = O(p³)); for K = 0, a_0 → L^{-1}b direction-wise (Lemma F-bg:
L^{-4}·(L²/|p|²)·L·|p|² = L^{-1}), and e'^†Π̂_F(p/L)e/|ŝ(p/L)|² → β[F]e'^†P_⊥(n)e (L4a-Π for F), with
|ŝ(p/L)|²/|ŝ(p)|² → L^{-2}. So the limit is L⁴·L^{-2}·L^{-2}·β[F] = β[F]: (i).
(iii): 𝒯_{j+1} = 𝒯_j∘Φ + κΣk̃∘(id, Φ), and the kernel term at the minimiser has quadratic part (κ/2)|r|² =
(1/(2κ))|Ĝ_{j+1}^{-1}b|² = O(p⁴)|b|², so β[𝒯_j∘Φ] = β[𝒯_{j+1}] = 1 (Lemma F-tree). ∎
*Reading.* Failure mode FL-F3's mechanism (an earlier renormalised polymer regenerates an O(1) marginal part at the next
level) does not occur at tree level: alias wiggles of the soft background are O(p³), so a zero-marginal functional stays
zero-marginal. Earlier polymers contribute to the next β only through fluctuations, at O(g²) (class (b) of §6.1).
~~[(i) with β[F] ≠ 0 is used only for F = 𝒯_j, where (iii) gives it independently of the Fourier normalisation.]~~
**[RFL-fix FR-1]** The struck bracket is false after session 2: Corollary U-red uses (i) with β ≠ 0 for F = Γ^{W0}_n. (i) is
nevertheless correct for every admissible F, by calibration rather than by trusting the factor L^{-4}·L⁸: the K = 0 limit
above is one and the same linear functional c·β[F] for every admissible F (the K ≠ 0 terms are O(p⁶) for every F), with a
universal factor c from the Fourier normalisation; applying it to F = 𝒯_j, for which (iii) gives β[𝒯_j∘Φ] = 1 = β[𝒯_j]
independently (kernel term O(p⁴), Lemma F-tree), forces c = 1.

### 5.5 Lemma F-tel (one-loop telescoping): PROVEN-HERE; Lemma F-split; Proposition F-1L (conditional on UNIV-1L)
**Lemma F-tel.** Let Γ_{j→n}(V) be the one-loop functional of the composite of steps j, …, n-1 at uniform u (the joint
integral over U_j, …, U_{n-1} with U_n = V, input u𝒯_j, kernels κu). Then exactly
  Γ_{j→n} = Σ_{k=j}^{n-1}Γ_k∘Φ_{k+1←n}, and hence β[Γ_{j→n}] = -Σ_{k=j}^{n-1}b_k.
*Proof.* f := 𝒯_j(U_j) + κΣ_kΣ_ck̃(U_{k+1}, M̄(U_k)). Minimising over U_j, then U_{j+1}, … gives min f = 𝒯_n(V), attained at
the tower U_k* = Φ_{k←n}(V) (Def F-strip). The joint Hessian at the tower (on the product of the per-level slices) is block
tridiagonal; eliminating U_j first, det H_joint = det H_{jj}·det S, and the Schur complement S equals the Hessian of the
partially minimised function 𝒯_{j+1}(U_{j+1}) + κΣ_{k>j}Σk̃ at the tower (second-order envelope identity
Hess(min_xf) = f_yy - f_yxf_xx^{-1}f_xy at a nondegenerate minimum). Induct on the number of levels. The FP and 𝒩'_1 factors
are per-level functions evaluated at the tower, hence additive. So Γ_{j→n} = ΣΓ_k∘Φ. Then β: Γ_k + b_k𝒯_{k+1} has β = 0, so
by Lemma F-ren (ii), (iii) β[Γ_k∘Φ] = -b_k. ∎
**[RFL-fix FT-1]** The last step applies Lemma F-ren to the per-step Γ_k, which needs Γ_k to be C² at 1 with an
exponentially local Hessian. That Hessian contains D³𝒯_k(1) and D⁴𝒯_k(1), i.e. D²Φ and D³Φ of the earlier tower: explicit
implicit-function compositions of the proven-local linear inverse with explicit vertex tensors, but NOT written. So the
identity "β[Γ_{j→n}] = −Σb_k" with the per-step b_k = −β[Γ_k] is given (SF-bg) at the trivial point (orders 3, 4); the
first identity Γ_{j→n} = ΣΓ_k∘Φ (exact, Laplace level) does not need it, and B_n := −β[Γ_{0→n}] (the composite route,
Lemma U-tad) does not need it either. **[S4] FT-1 is discharged by Lemma TOW (§31): the needed trivial-point data (D^{≤4}𝒯_k(1),
D^{≤2} of the one-step towers) are local at each k, so F-tel's second identity holds without (SF-bg).**
**Lemma F-split (where the soft normalisations go): [RFL-fix FS-1] WRONG as stated for SU(N) (it omits the drift term
Γ^dr); SUPERSEDED by Proposition U-dec, its β-level content surviving via Lemma U-pair; removed from the PROVEN-HERE count.
Original label (session 1): PROVEN-HERE (at the level of one-loop functionals).** [S2: exact only
for affine averaging maps; for SU(N) a drift term Γ^dr is missing, which has no marginal part: Proposition U-dec, Lemma
U-pair, §16.] Eliminate the
intermediate levels U_{j+1}, …, U_{n-1} first instead (fixed U_j, V). (1) The V-Hessian of κuk̃(V, M) at V = W equals κu times
the X-Hessian at X = 1 of N^{-1}Re tr((1 - X)P), which is the Gaussian form of 𝒩'(P): so each level's kernel is, at one-loop
order, a normalised Gaussian transition (its 𝒩'_1 factor is exactly its Gaussian normalisation). (2) A product of
normalised Gaussian transitions integrated over the intermediate levels is a normalised Gaussian in V with mean
𝔪(U_j) (the tree composite map) and covariance u^{-1}𝒞_comp(U_j) (Gaussian convolution, exact). Hence
  Γ_{j→n}(V) = [½log det'(Hess_{U_j}(𝒯_j + Ψ_comp(·; V)))_{slice} - log Δ_FP]_{U_j = Φ_{j←n}(V)} + ½log det 𝒞_comp(Φ_{j←n}(V)) + const,
Ψ_comp(U_j; V) := ½⟨V - 𝔪(U_j), 𝒞_comp(U_j)^{-1}(V - 𝔪(U_j))⟩ (to the order needed). So all per-level 𝒩'-terms are absorbed
into ONE term, ½log det 𝒞_comp, and the rest is the fine (level-j) fluctuation determinant with an IR term at scale L^{n-j}. ∎
**Proposition F-1L (the one-loop coefficient): given (UNIV-1L), PROVEN-HERE (arithmetic).** (F-1) holds with
β_0' = β_0^std = 11N²/(12π²) and R = 2R_0: Σ_{k=j}^{n-1}b_k = B_n - B_j (B_n := Σ_{k<n}b_k). If b_k converges, its limit is
b_∞ = β_0' log L (Cesàro). In the standard normalisation this is 2b_0 = 11N/(24π²) per unit log of the scale, the universal
one-loop coefficient: the soft kernel's scheme dependence (κ, S4', 𝒩) sits entirely in R_0 and in the depth corrections
b_k - b_∞. Numbers: β_0' = 0.37151 (SU(2)), 0.83590 (SU(3)), 0.092878N² in general; per step at L = 3: ×log 3 = 1.0986.
**(UNIV-1L): OPEN [P]; ARGUED reduction** (via Lemma F-split with j = 0):
- (U-b) the fine fluctuation determinant (Wilson background-field operator + gauge fixing + the IR term Hess Ψ_comp at
  scale ℓ = L^n) has β = -β_0^std log ℓ + O(1). Argued by the a_2 decomposition (L4b, IMPORTED-AND-REVERIFIED: (1/2)a_2^vec
  - a_2^gh = (11/12)C_AF^aF^a = [-(1/12) (Ω², diamagnetic) + 1 (E², paramagnetic)]C_AF^aF^a) and lattice universality of each
  channel's log: Ω² checked in f3 (slope 0.990 at m = 0.1/0.05, monotone convergence; sharpens c2(B)'s 0.94-1.10), E²
  checked in f2 with the soft kernel itself as the IR regulator (slope 1.001-1.005 at ℓ = 13/15 for κ_c ∈ {0.25, 1, 4, ∞},
  κ-spread 0.0035; the scheme dependence is in the constant, which varies 0.013-0.033). Not covered: the gauge-field lattice
  operator itself with the composite kernel, and the background dependence of Ψ_comp (power counting: its symbol is
  concentrated at |q| ≲ 1/ℓ, so its polarisation is O(1)).
- (U-c) β[½log det 𝒞_comp∘Φ] = O(1) uniformly in n. Argued: level-i noise reaches the level-n covariance through n - i
  applications of the averaging, each a contraction by ≤ L^{-2} on bounded symbols (Lemma F-depth, PROVEN for the linear
  map); the background dependence of level i's contribution is O(1)·F² per coarse site times L^{-2(n-i)}: a convergent
  geometric sum.
- Why scheme independence is expected at all (not a proof): a normalised kernel is a Markov transition, so the coarse
  theory at every level is a lattice gauge theory of the same (compact) family; two such block schemes for the same fine
  theory have Λ-parameters in a fixed ratio, so their couplings differ by O(1) in u. A per-level non-cancelling O(1) term
  (FL-F2) would make 1/g² of compact U(1) (b_0 = 0) run logarithmically under the soft chain, which the Coulomb-phase
  physics excludes [m; inference]. Lemma F-split is the mechanism: the per-level 𝒩-terms combine into ½log det 𝒞_comp,
  which is dominated by the last few levels.

### 5.6 Lemma F-depth (tree-level depth convergence, linear): PROVEN-HERE
*Claim.* ||Ĝ_{k+1} - Ĝ_k||_∞ ≤ λ'^k||Ĝ_1 - Ĝ_0||_∞ with λ' ≤ L^{-2}, and ||Ĝ_1 - Ĝ_0||_∞ < ∞; so the quadratic part of the
tree tower converges geometrically to a fixed point Ĝ_∞ = Ĝ_0 + Σ_k(Ĝ_{k+1} - Ĝ_k).
*Proof.* Δ_k := Ĝ_{k+1} - Ĝ_k obeys Δ_{k+1} = 𝒬(Δ_k) (the κ^{-1} terms cancel). 𝒬 is positivity preserving and, for Hermitian
-δ ≤ G ≤ δ, -δΛ ≤ 𝒬(G) ≤ δΛ with Λ := L^{-4}P_⊥(Σ_KQ̃_KQ̃_K^†)P_⊥ = L^{-4}P_⊥(Σ_KQ̃_str,KQ̃_str,K^†)P_⊥ (P_⊥ removes d∘h;
P_TGP_T ≤ δ). Q̃_str,K is diagonal, entries φ_μ(q_K), φ_μ(q) = Σ_wc_we^{iqw}; by Poisson summation over aliases,
Σ_K|φ_μ(q_K)|² = L⁴Σ_{r∈(Z/L)⁴}|Σ_{w≡r}c_we^{ipw/L}|² ≤ L⁴Σ_r(Σ_{w≡r}|c_w|)², and for the straight average every residue
class carries total weight L^{-4}·L (one block site per leg position j), so Σ_K|φ_μ|² ≤ L⁴·L⁴·L^{-6} = L²: Λ ≤ L^{-2}.
Boundedness of Δ_0 = κ^{-1}P_⊥ + 𝒬(Ĝ_0) - Ĝ_0: the K ≠ 0 terms are bounded; for K = 0, Q̃_str,0(p) = L·e^{iθ}Λ_p(1 + O(p²))
with Λ_p = diag(e^{ip_μ(L-1)/(2L)}) (the Dirichlet factors are real and even, the leg sum carries the phase), and
Λ_pŝ(p/L) has the same phases e^{ip_μ/2} as ŝ(p) and moduli ratio L^{-1}(1 + O(p²)), so P_⊥Λ_pP_T(p/L)Λ_p^†P_⊥ = P_⊥ + O(p²)
and |ŝ(p)|²/|ŝ(p/L)|² = L²(1 + O(p²)): the K = 0 term is P_⊥/|ŝ(p)|² + O(1). ∎ (f1 (F) as pre-registered measured the
unprojected L^{-4}max_pΣ_K||Q̃_K||² = 2.30 and FAILED its line (< 1/2): that quantity includes the d∘h gauge part, which P_⊥
removes and which is not the constant of this lemma. Post-hoc, labelled: λ' measured 0.1067 ≤ L^{-2} = 0.1111.)
*Not covered.* Convergence of b_k (the one-loop functional needs the nonlinear tower, (SF-bg)): ARGUED, OPEN [s-P].

### 5.7 The f3 integrand (as promised in f3_criteria, which cites it as §5.6; f4_criteria's "§8-§9" are §7-§8 here)
For φ^*M_Aφ = Σ|φ(x+e_μ) - e^{iA_{x,μ}}φ(x)|² + m²|φ|², ∂M/∂A_{x,μ}|_0 = V_{x,μ} := i(e_xe_{x+μ}^† - e_{x+μ}e_x^†), and
Π((x,1), (y,2)) = -tr(GV_{x,1}GV_{y,2}). In momentum space Π_12(z) = V^{-1}Σ_ke^{ikz}F(k) with F(k) as in f3_criteria (z = x - y),
so β = -∂_1∂_2F(0). Differentiating under the integral (g = 1/(ω + m²), ∂_αg = -2g²sin q_α, ∂_1∂_2g = 8g³sin q_1sin q_2):
  ∂_1∂_2F(0) = ∫[-32g⁴s_1²s_2² + 4g³s_1²cos q_2 + 4g³s_2²cos q_1 - g²cos q_1cos q_2] (s_α = sin q_α; odd parts dropped).
Continuum power counting of the four terms (angular averages q_1²q_2² → q⁴/24, q_α² → q²/4) gives
β ≈ (1/(6π²) - 1/(4π²) + 1/(8π²))log(1/m) = (1/(24π²))log(1/m), i.e. c_Γ = β/2 = (1/(48π²))log(1/m), the a_2 value. f3 checks
the formula against the exact position-space Hessian (5e-18) and a finite-difference Hessian of log det (1.5e-8), and the
analytic derivative against finite differences of F (8 digits).

## 6. Step 2: the remainder bound

### 6.1 Which terms renormalise the coupling
Classes of field-dependent terms in S_{k+1} beyond u_k𝒯_{k+1} (Def F-g, (SF-g)), and their contribution to u_{k+1} - u_k:
- (a) the one-loop functional Γ_k (fluctuation determinant, FP determinant, soft normalisation 𝒩'_1): -b_k, O(1),
  g-independent (§5);
- (b) the higher-order fluctuation terms (cubic² and quartic vertices, the fluctuation corrections of the earlier
  renormalised polymers, the small-field cutoff tails): β[ΣE^{≥2}_k], O(g_k²) by (SF-g) and Lemma F-Π;
- (c) the earlier renormalised polymers at the tree background: 0 (Lemma F-ren (ii));
- (d) the large-field returned terms: +δβ_k (RLF-0), their remainders 0 (irrelevant by (RLF-2)); **[RFL-fix FR-2, K1: read
  −δβ_k (the shift lowers u), §4]**
- (e) c-numbers (vacuum, including RLF's 𝒱^{LF}): 0;
- (f) wrapping polymers on the torus: not couplings (Def F-g is infinite-volume; (SF-∞)).
The tr F² coefficient is isolated by L4a-Π (the infinite-volume sum is gauge invariant, translation invariant and
B_4-covariant because the S4' family and the normalised kernel are, D4-norm (1)); for non-symmetric cluster families
(RLF's shapes S) by the B_4 orbit sum, GT-lat' (ii), with Lemma F-id converting c̄ into a coupling shift.

### 6.2 Proposition F-rem: given (SF-g)_k and (RLF-δ), PROVEN-HERE
*Claim.* If g_0, …, g_k ∈ (0, γ_0], then β_k = b_k + ρ_k with |ρ_k| ≤ C_ΠE_2g_k² + g_k⁶ ≤ C_ρg_k², C_ρ := C_ΠE_2 + 1 (g_k ≤ 1),
C_Π = 64M⁶α^{-2}Σ_nn³(6400e^{-κ_p})^{n-1} (Lemma F-Π).
*Proof.* u_{k+1} - u_k = β[Γ_k] + β[ΣẼ_k∘Φ] + β[ΣE^{≥2}_k] + β[𝒮^{LF}_k] = -b_k + 0 + β[ΣE^{≥2}_k] + δβ_k (definition of
b_k; Lemma F-ren (ii); (SF-g); (RLF-2), Lemma F-id). So ρ_k = -β[ΣE^{≥2}_k] - δβ_k, and **[RFL-fix FR-2, K1: with
(SF-g)'s sign the last term of the first sum is β[𝒮^{LF}_k] = −δβ_k, so ρ_k = −β[ΣE^{≥2}_k] + δβ_k; the bound below is
unchanged]**
|β[ΣE^{≥2}_k]| ≤ C_Π||E^{≥2}_k||_{κ_p} ≤ C_ΠE_2g_k² (Lemma F-Π (ii)); |δβ_k| ≤ g_k⁶ (RLF-δ). ∎

## 7. Step 3a: the discrete flow (Theorem F-flow)

**Theorem F-flow: given (UNIV-1L), (SF-g), (RLF-δ), PROVEN-HERE.** Let R := 2R_0, γ ∈ (0, γ_0] with C_ργ² ≤ ½β_0'log L, and
β_± := β_0' ± C_ργ²/log L (so β_0'/2 ≤ β_- ≤ β_0' ≤ β_+ ≤ 3β_0'/2). If g_0, …, g_{n-1} ∈ (0, γ], then for all 0 ≤ j ≤ n:
  β_-(n - j)log L - R ≤ u_j - u_n ≤ β_+(n - j)log L + R.
*Proof.* u_j - u_n = Σ_{k=j}^{n-1}β_k = (B_n - B_j) + Σ_{k=j}^{n-1}ρ_k. |B_n - B_j - β_0'(n - j)log L| ≤ 2R_0 (UNIV-1L twice).
|ρ_k| ≤ C_ρg_k² ≤ C_ργ² for j ≤ k ≤ n - 1 (Proposition F-rem needs only g_0, …, g_k ≤ γ ≤ γ_0). ∎
**Corollary F-ll (the two-loop-type refinement; arithmetic, PROVEN-HERE).** Under the same hypotheses, if u_n > R,
|u_j - u_n - β_0'(n - j)log L| ≤ R + C_ρΣ_{m=1}^{n-j}(u_n - R + β_-m log L)^{-1} ≤ R + C_ρ[(u_n - R)^{-1} +
(β_-log L)^{-1}log(1 + (n - j)β_-log L/(u_n - R))]: the deviation from the one-loop line grows only like log(n - j)
(the familiar log log of the two-loop running), not linearly. (Proof: g_k² = 1/u_k ≤ 1/(u_n - R + β_-(n - k)log L) by the
lower bound with j → k; compare the sum with an integral.)

## 8. Step 3b: bare-coupling tuning (Theorem F-tune)

**Theorem F-tune: given (UNIV-1L), (SF-g), (RLF-δ), (SF-cont), (SF-∞), PROVEN-HERE.** With γ, β_±, R as in Theorem F-flow
and g_1 := (γ^{-2} + R)^{-1/2}: for every K ≥ 1 and g ∈ (0, g_1] there is g_0 = g_0(ε, g) ∈ (0, γ] (ε = L^{-K}) with
g_k ∈ (0, γ] for 0 ≤ k ≤ K, g_K = g, and
  1/g² + β_-(K - k)log L - R ≤ 1/g_k² ≤ 1/g² + β_+(K - k)log L + R  (0 ≤ k ≤ K).
γ, g_1, β_±, R do not depend on K or on the torus. One may take g_0(ε, g) := the smallest such g_0 (it exists).
*Proof.* Write 𝒜 := {g_0 ∈ (0, γ]: g_k(g_0) ∈ (0, γ] for 0 ≤ k ≤ K}.
1. *Small bare couplings are admissible.* Let g_* := (γ^{-2} + β_+K log L + R)^{-1/2}. If g_0 ≤ g_* then by induction on k
   ≤ K: if g_0, …, g_k ≤ γ, Theorem F-flow on [0, k+1] (which uses only g_0, …, g_k ≤ γ) gives u_{k+1} ≥ u_0 - β_+(k+1)log L
   - R ≥ γ^{-2}, i.e. g_{k+1} ≤ γ. So (0, g_*] ⊂ 𝒜, and F(g_0) := u_K(g_0) ≥ g_0^{-2} - β_+K log L - R → ∞ as g_0 → 0.
2. *The first exit.* Let g_0^♯ := sup{s ∈ (0, γ]: (0, s] ⊂ 𝒜} (≥ g_* > 0). Induction on k ≤ K: g_0^♯ ∈ 𝒜_{k-1}(γ_0)
   (the domain of (SF-cont) for g_k) and every s < g_0^♯ is in 𝒜, so g_k(g_0^♯) = lim_{s↑g_0^♯}g_k(s) ≤ γ ≤ γ_0, i.e.
   g_0^♯ ∈ 𝒜_k(γ_0). Hence g_0^♯ ∈ 𝒜. Suppose g_0^♯ < γ and max_{k≤K}g_k(g_0^♯) < γ. Again by induction on k, for s in a
   small neighbourhood of g_0^♯ one has s ∈ 𝒜_{k-1}(γ_0) and, by continuity at g_0^♯, g_k(s) < γ; so a right-neighbourhood of
   g_0^♯ lies in 𝒜, contradicting the supremum. Hence g_{k*}(g_0^♯) = γ for some k* ≤ K (if g_0^♯ = γ, k* = 0).
3. *Value at the first exit.* Theorem F-flow on [k*, K] (valid: g_0, …, g_{K-1} ≤ γ at g_0^♯) gives
   u_K ≤ u_{k*} - β_-(K - k*)log L + R ≤ γ^{-2} + R = g_1^{-2} ≤ g^{-2}.
4. *Intermediate value.* F is continuous on (0, g_0^♯], F → ∞ at 0+, F(g_0^♯) ≤ g^{-2}: there is g_0 ∈ (0, g_0^♯] with
   F(g_0) = g^{-2}, and g_0 ∈ 𝒜. The zero set of F - g^{-2} in (0, g_0^♯] is closed and bounded away from 0 (step 1), so it
   has a smallest element.
5. *Bounds.* Theorem F-flow on [k, K] with u_K = g^{-2}. *Volume uniformity:* u_k is defined by the infinite-volume β (Def
   F-g, (SF-∞)), so the whole sequence, hence g_0(ε, g), is the same for every torus; the constants never involve K or T. ∎
*Not claimed.* Uniqueness of g_0 (would follow from ∂u_{k+1}/∂u_k > 0, i.e. |∂β_k/∂u_k| < 1, a C¹ form of (SF-cont)); not
needed. Positivity g_k > 0 is automatic (u_k ≥ γ^{-2}).
*Check f4* (synthetic admissible data with non-monotone, g_0-dependent remainders): (F-3) on 238 604 (j, n) pairs, 0
violations; tuning found 9/9 (K ∈ {10, 100, 1000}), tuned bounds 0 violations.

## 9. Lemma F-ind (no circularity with RLF and the small-field package): PROVEN-HERE (logic)
RLARGE's constants (n_♯ = ⌊4/(a_♯β_-)⌋, the sums (P1), (P2), (P5)) and possibly the (SF) constants (E_2, α, κ_p) depend on
the flow constants through the lower half of (F). Fix FIRST β_- := β_0'/2 and R := 2R_0 (numbers from the one-loop data
alone); then the layer-1 constants C_ρ = C_ρ(β_0'/2, 2R_0) are fixed; then γ := min{γ_0, (β_0'log L/(2C_ρ))^{1/2}}. Theorem F-flow
then returns the lower half with β_- ≥ β_0'/2 and the same R: the hypothesis used at level k (the flow on [0, k]) is
reproduced at level k + 1 with the same constants, and the per-level inputs (RLF-δ), (SF-g)_k use g_0, …, g_k ≤ γ only. The
induction over k closes; no constant is defined in terms of itself.
**[RFL-fix FI-1 (binding)]** The induction closes only if (SF-g)_k and (RLF-δ)_k at level k use the flow on [0, k] only,
along the chain's own sequence. RLF's statement (RLARGE §1A) involves g_K (Σ_k|δβ_k| ≤ Ce^{-a/g_K²}; LF-n with
1/g_i² ≥ 1/g_K² + …); this file consumes only the per-level |δβ_k| ≤ g_k⁶. That the per-level bound is derived in RLARGE's
(I_k) → (I_{k+1}) induction from (F_R) on [0, k] for the chain's own sequence is a REQUIREMENT ON LANE RLARGE (see §4), not
proven here. Lemma F-ind is PROVEN-HERE as a statement about the order of fixing this file's constants, conditional on it.

## 10. What the consumers get
- **RLARGE (F)** (§0): Theorem F-flow gives (F_R): β_-(k - j)log L - R ≤ u_j - u_k ≤ β_+(k - j)log L + R, i.e. (F) with an
  additive constant R = 2R_0. (F) as RLARGE writes it (R = 0) would need |B_n - B_j - β_0'(n - j)log L| small at
  n - j = 1, which the depth corrections b_k - b_∞ (O(1) at small k) do not give. **[RFL-fix FRR-2] The preceding
  sentence is false: RLARGE's β_± are free positive constants, and R = 0 needs only inf_k(b_k + ρ_k) > 0; superseded by
  Lemma F-R (i) (§19).** **[RFL-fix FI-2]** Any suggested (F_R) wording carries the quantifier "for the chain's own effective
  sequence (Def F-g)". Every consumer checked here tolerates R:
  LF-count's sums and RLARGE (P1), (P2) acquire factors e^{a_♯R} (or e^{(n+1)a_♯R} per n-cube term), and n_♯ (the
  asymptotic slope) is unchanged [inference; RLARGE not edited by this lane]. Suggested reading for the lead: replace (F) by
  (F_R) in RLARGE §0.
- **EXISTENCE H-Bal-1**: Theorem F-tune is H-Bal-1 for SU(N), every N ≥ 2, with the additive R, uniformly in the torus side
  M (by Def F-g's infinite-volume definition), conditional on (UNIV-1L) and the layer-1 hypotheses of §4. Its consequence
  used there (g_{m,K} in [(1/g² + β_+m log L + R)^{-1/2}, γ], K-independent) holds.
- **E8.3/E7.0 rate condition** (PROOF L4a-flow: β' < 6.1·2b_0 in the standard normalisation): β_+/(2N) = 2b_0 +
  C_ργ²/(2N log L) is below any c·2b_0 with c > 1 for γ small, given (UNIV-1L).

## 11. Outcomes against the pre-stated target (§1) and failure modes
- (F-1): the soft one-loop coefficient is β_0' = β_0^std = 11N²/(12π²) (our normalisation; 2b_0 = 11N/(24π²) standard),
  CONDITIONAL on (UNIV-1L) [OPEN, P], with the exact parts proven: tree level does not renormalise (F-tree, f1), the
  one-loop telescopes exactly (F-tel), renormalised terms stay renormalised (F-ren, F-bg), the per-level soft
  normalisations collapse into one covariance determinant (F-split), the linear tree tower converges at rate L^{-2}
  (F-depth). Channel checks f2 (E², with the soft kernel as regulator), f3 (Ω²). The rate of b_k → b_∞: OPEN (nonlinear).
- (F-2): PROVEN given (SF-g), (RLF-δ), with explicit C_ρ = C_ΠE_2 + 1.
- (F-3), (F-4): PROVEN given the above, (SF-cont), (SF-∞), with an additive constant R = 2R_0 (R = 0 is not obtained).
- FL-F1: does not occur (F-tree). FL-F2: excluded at the argued level (F-split + (U-c)); not proven. FL-F3: does not occur at
  tree level (F-ren); at loop level it is the O(g²) class (b), controlled by (SF-g). FL-F4: does not occur (no monotonicity
  needed; continuity is (SF-cont)).
- **Open items, weighted:** (UNIV-1L) [P] (a lattice one-loop computation for the soft composite: (U-b) gauge-field
  version of f2/f3 with the composite kernel; (U-c)); b_k → b_∞ with a rate [s-P]; (SF-g), (SF-bg), (SF-cont), (SF-∞) are
  layer-1 content (nodes A1-A4; (SF-g) is the L4a-form part of (SF), the polymer representation of the step output with its
  g-expansion) [P, shared with lane A]. Next check to design: f5, SU(2) one-loop β of one soft step on the S4' symbol at
  trivial background (Cartan-direction background, momentum space), to measure b_k at small depth and test (U-c) directly.

## 12. Checks (criteria before scripts; NUMERIC LOCK, nice 10, 1 thread; peaks ≤ 110 MB)
- **f1** (checks/f1_criteria.md, f1_tree_soft.py, f1_out.txt, f1_time.txt; 17 s) **[RFL-fix CK-1] provenance: NOT VERIFIABLE
  (the current f1_criteria.md bytes were re-created at 23:12:50 UTC, after the f1 script (23:09:26) and both f1 runs; the
  header's "23:07 UTC [file mtime]" is not the file's mtime; FLOW_LOG 2026-10-28 00:45 entry). f2-f4 criteria predate
  their scripts.**: G, A, B, C, D, E PASS; **F FAIL as
  pre-registered** (the unprojected quantity 2.30; see §5.6), post-hoc labelled λ' = 0.1067 ≤ L^{-2}. Marginal coefficient
  1 to Richardson ≤ 6e-7 for κ ∈ {0.25, 1, 4, 16} at L = 3 and κ = 1 at L = 5; remainder ratio 15.5-16.0 (O(p⁴)); alias
  curvature ratio 7.46-8.02 (O(p³)).
- **f2** (f2_criteria.md, f2_e2_soft.py, f2_out.txt, f2_time.txt; 22 s): A, E, B, C, D PASS. Slopes at (13, 15):
  1.0013, 1.0028, 1.0048, 1.0038 × 1/(8π²) for κ_c = 0.25, 1, 4, ∞; constants 0.033, 0.026, 0.020, 0.013.
- **f3** (f3_criteria.md, f3_omega2_lattice.py, f3_out.txt, f3_time.txt; 5 s): A, B, C, D PASS. Ω² slope × 48π²: 0.902,
  0.968, 0.990 along (0.4, 0.2), (0.2, 0.1), (0.1, 0.05).
- **f4** (f4_criteria.md, f4_flow_shoot.py, f4_out.txt, f4_time.txt; 2 s): A, B, C PASS (one pre-run fix of the shooting
  scan's exit handling, before the first run; logged).

## 13. Tally (FLOW.md items)
- **PROVEN-HERE (12; unreviewed):** Lemma F-Π, Lemma F-id, Lemma F-tree, Lemma F-bg, Lemma F-ren, Lemma F-tel, Lemma F-split,
  Lemma F-depth, Proposition F-rem [given (SF-g), (RLF-δ)], Theorem F-flow (+ Corollary F-ll) [given also (UNIV-1L)],
  Theorem F-tune [given also (SF-cont), (SF-∞)], Lemma F-ind. (Proposition F-1L is arithmetic given (UNIV-1L), not counted.)
- **IMPORTED-AND-REVERIFIED (used, upstream):** L4b (b_0, a_2 decomposition) — 1.
- **IMPORTED-NOT-YET-REVERIFIED:** none load-bearing (CMP 109's (1.22) definition and its "smooth" remark are used as
  motivation for Def F-g and (SF-cont), not as proof).
- **OPEN (2):** (UNIV-1L) [P] (reduction ARGUED: U-b, U-c); b_k → b_∞ with rate [s-P].
- **HYPOTHESES consumed (layer 1, named):** (SF-bg), (SF-g), (RLF-δ), (SF-cont), (SF-∞).

---
# Session 2 of lane C (opened 2026-10-27 23:38 UTC)

## 14. Session-2 targets (pre-stated 2026-10-27 23:39 UTC, before any session-2 derivation, criteria file or script)

Session-1 text (§0-§13) is not edited below except for pointer lines marked [S2]. Session-2 outcomes are in §20.

**Target T1 (UNIV-1L, §4).** Prove: there is R_0 < ∞ depending only on (N, L, κ) and named layer-1 constants with
|Σ_{k<n}b_k - β_0^std n log L| ≤ R_0 for all n, where b_k = -β[Γ_k] (§5.1). Pre-stated route:
- (R1) B_n := Σ_{k<n}b_k = -β[Γ_{0→n}] (Lemma F-tel); Γ_{0→n} in fine (level-0) units = the Wilson fluctuation
  determinant with the composite soft term Ψ_comp as IR term, plus ½log det 𝒞_comp∘Φ (Lemma F-split).
- (R2) Reduce the Hessian of Γ_{0→n} at V = 1 to a finite list of one-loop terms built from the trivial-background
  fluctuation covariance, the linear tree map DΦ, and the vertex tensors at the trivial point; show which inputs are
  needed (in particular whether the second-order tree map D²Φ enters).
- (R3) A residue lemma: the coefficient of log ℓ (ℓ = L^n) of a lattice integral whose integrand is (UV) the massless
  lattice integrand and (IR) cut off at |q| ~ 1/ℓ is the sphere integral of the leading homogeneous (degree -4) part of
  the massless lattice integrand; with explicit error terms.
- (R4) Show that every term containing a soft-kernel vertex, the composite covariance determinant, or the soft IR part
  of the propagator contributes O(1) (no log ℓ), uniformly in n; and identify the residue of the remaining (Wilson,
  Feynman-gauge) terms with the continuum one-loop coefficient through L4b.
- (R5) The normalisation conversion between 11N²/(12π²) per log L (u = 1/g_k² of RLARGE §0) and 2b_0 = 11N/(24π²)
  (L4b): the exact factor, with the place where each convention is defined.
**Target T2 ([s-P] of §5.6).** The convergence rate of b_k → b_∞ = β_0^std log L, as a corollary of T1's structure
(scaling form of the IR part), with the hypotheses it needs stated.
**Target T3 (the additive constant R).** A note, quoting the consumers' statements (read-only), on what each of RLARGE
(F), LF-count, RLARGE (P1)/(P2), n_♯ and EXISTENCE H-Bal-1 / X-NTAF needs from R.

**Failure modes (each a valid outcome).** (U-F1) D²Φ (the second-order tree map, (SF-bg) beyond order 2) enters b_k,
so UNIV-1L needs (SF-bg); (U-F2) a soft-kernel vertex term carries a log ℓ (the kernel's background dependence is not
IR-concentrated); (U-F3) the gauge fixing available on the composite (fine gauge transformations trivial on the coarse
sites) changes the leading homogeneous integrand; (U-F4) the composite covariance does not have the IR decay the residue
lemma needs (e.g. the S4' gauge parts spoil it); (U-F5) the normalisation conversion is not the factor 2N.

**Checks (criteria files before scripts; NUMERIC LOCK; nice 10; 1 thread).**
- f5: complex unit-charge lattice scalar in a U(1) background with a gauge-COVARIANT soft block kernel (path-averaged
  parallel transport to the block centre), kernel vertices included: (i) the log ℓ coefficient of β is the universal one,
  κ-independently; (ii) the part of β carried by diagrams with ≥ 1 kernel vertex has no log ℓ (tests R4/U-F2 directly);
  validation against a dense torus finite-difference Hessian and a Ward identity.
- f6 (if time): the rate of the slope convergence in f2/f5 data against T2's prediction.

---
# Session-2 derivations (written after §14)

## 15. Lemma F-norm (the normalisation conversion; target R5, failure mode U-F5): PROVEN-HERE

*Where each convention is defined.* (i) RLARGE §0 ("Action normalisation"): level-k Wilson term (1/g_k²)Σ_ps(U_p),
s(U) = 1 - N^{-1}Re tr U, Σ_p over unoriented plaquettes; FLOW §0 writes u_k := 1/g_k². (ii) PROOF L4b (l.1159-1170
**[RFL3-fix S3-4: stale; L4b is PROOF l.1207-1225, the continuum normalisation at l.1216-1217]**):
continuum S = (4g_std²)^{-1}∫Σ_{μ,ν}F^a_μνF^a_μν, F = F^aT^a with tr(T^aT^b) = δ^{ab}/2 (the generators of checks/c2_b0.py),
1/g_std²(μ) = 1/g_0² - (11/3)C_A(16π²)^{-1}ln(Λ²/μ²), i.e. d(1/g_std²)/d ln μ = 2b_0, b_0 = 11N/(48π²), C_A = N.
(iii) The lattice-continuum dictionary U_{x,μ} = exp(iaA^a_μ(x)T^a), U_p = exp(ia²F^a_μνT^a + O(a³)).
*Claim.* u = 2N/g_std² exactly (at the level of the marginal term). Hence one RG step (scale factor L) at one loop shifts
u by 2N·2b_0 log L = 4Nb_0 log L = (11N²/(12π²))log L = β_0^std log L. The two numbers in the brief differ by exactly the
factor 2N: 11N²/(12π²) = 2N × 11N/(24π²).
*Proof.* For hermitian X, 1 - N^{-1}Re tr e^{iX} = (2N)^{-1}tr X² + O(X⁴); with X = a²F^a_μνT^a, s(U_p) = a⁴F^a_μνF^a_μν/(4N)
+ O(a⁶) (no sum over the plane). Σ_p = Σ_xΣ_{μ<ν} = ½Σ_xΣ_{μ≠ν}, so uΣ_ps(U_p) = (u/(8N))Σ_xa⁴Σ_{μ,ν}F^aF^a →
(u/(8N))∫ΣF^aF^a. Equating with (4g_std²)^{-1}∫ΣF^aF^a gives u = 2N/g_std². The β-functional of FLOW §0 has
β[Σ_ps] = 1 (c17(A)), so b_k, β_k are in u-units, and a shift Δ(1/g_std²) = 2b_0 log L is Δu = 2N·2b_0 log L. ∎
*Cross-checks.* (a) LF-count (PROOF l.4106-4109 **[RFL3-fix S3-4: stale; now PROOF l.4162]**, read-only) uses Balaban's normalisation (1/g_B²)Σ[1 - Re tr U] with
tr 1 = 1, which is the same as (i) (normalised trace), and writes 1/g_B² = 2N/g_std², β'_B ≈ 2N·2b_0 = 4Nb_0 =
11N²/(12π²): the same factor. (b) The product aβ' is normalisation-independent: in standard units the instanton
a = 8π², β' = 2b_0 gives 8π²·11N/(24π²) = 11N/3; in u-units a = 8π²/(2N), β' = 11N²/(12π²) gives the same 11N/3 (LF-count's
instanton remark). (c) In FLOW's Lie coordinates (t_a orthonormal for -(1/N)tr(XY)), t_a = i√(2N)T^a, and s(e^X) =
½Σ(X^a)² is (i)'s Hessian. U-F5 does not occur.

## 16. The exact structure of the one-loop coefficient (target R2)

Setting: the joint integral of Lemma F-tel over U_0, …, U_{n-1} (U_n = V), stripped joint action f_V = 𝒯_0(U_0) +
κΣ_kΣ_ck̃(U_{k+1,c}, M̄_c(U_k)), the u-independent terms Σ_kΣ_clog𝒩'_1(P_c(U_k)), and on each level the legitimate fixing of
FP-ab / NA-FP (δ(h)e^{-½||P_resD^*·||²}, linear and colour-componentwise at the trivial background) with its FP factor.
𝔉(U, V) := (½log det' of the joint Hessian of f_V on the slices − log FP + Σlog𝒩'_1) evaluated at an arbitrary configuration
(U, V) near the trivial one; Γ_{0→n}(V) = 𝔉(Φ(V), V), Φ = (Φ_{0←n}, …, Φ_{n-1←n}) the tower.

**Lemma U-tad (tadpoles vanish; D²Φ does not enter β): PROVEN-HERE.** (i) Let F be C¹ near the trivial configuration of
a finite product of copies of SU(N) indexed by links (any levels), invariant under the diagonal global colour action
U_b ↦ hU_bh^{-1} (h ∈ SU(N) constant). Then DF(1) = 0. (ii) Consequently, for any C² global-colour-equivariant map Φ with
Φ(1) = 1 and any C² global-colour-invariant 𝔉: D²[𝔉(Φ(·), ·)](1)[v, v] = 𝔉_UU[DΦv, DΦv] + 2𝔉_UV[DΦv, v] + 𝔉_VV[v, v];
the term 𝔉_U(1, 1)[D²Φ(1)(v, v)] vanishes. [RFL-fix (minor)] "The Hessian at an arbitrary configuration" (Setting
above) is taken in an equivariant chart, e.g. exponential coordinates about each link value, U_b = U_b*e^{X_b}; constant
conjugation acts linearly (by Ad) on these coordinates, which is what (i) and (ii) use.
*Proof.* (i) The trivial configuration is fixed by the action, so DF(1) is an Ad-invariant element of ⊕_b su(N)*; each
component is an Ad-invariant vector of su(N) ≅ su(N)*, which is 0 (Ad is irreducible and nontrivial). (ii) The chain rule;
U ↦ 𝔉(U, 1) is global-colour invariant, so 𝔉_U(1, 1) = 0 by (i). ∎
*Application.* 𝒯_0 = Σs, k̃, the contour averages M̄ (constant conjugation commutes with parallel transport averages),
P = (M^*M)^{1/2}, 𝒩'_1 and the slice functionals are global-colour covariant, and the tower Φ is equivariant (uniqueness of
the minimiser near 1). So D²Γ_{0→n}(1) is built from: the linear tower DΦ (Lemma F-bg, exact linear formula), the
trivial-background joint covariance (Gaussian; N5-triv), and the third and fourth derivatives at the trivial point of
the EXPLICIT functions 𝒯_0 = Σs (Wilson), k̃∘(id, M̄), log𝒩'_1∘P∘M̄ and the FP factor. Since b_k = B_{k+1} - B_k (Lemma F-tel),
**every b_k is determined by Gaussian data and explicit vertex tensors; (SF-bg) beyond its proven second-order part is
not used. Failure mode U-F1 does not occur.** (In the per-step form b_k = -β[Γ_k] the third and fourth derivatives of the
tree tower 𝒯_k at 1 appear; they are themselves functions of the same explicit data, but the composite route never
needs them.)

**Proposition U-dec (composite decomposition; corrects Lemma F-split): PROVEN-HERE (at one-loop order, i.e. at the
Laplace level of the whole lane).** Let K_comp(V, U_0) := ∫Π_{0<k<n}dU_kΠ_{k<n}K_k(U_{k+1}, U_k) be the n-step
transition density (∫K_comp(V, U_0)dV = 1 exactly). At one-loop order -log K_comp(V, U_0) = uΨ(U_0; V) + Λ(U_0, V),
Ψ := min_{U_1,…,U_{n-1}}κΣk̃ (the tree composite exponent: Ψ ≥ 0, Ψ(U_0; 𝔪(U_0)) = 0, 𝔪 := the composite of the polar
averages W∘M̄), Λ its one-loop part. Then:
(i) (normalisation) Λ(U_0, 𝔪(U_0)) = ½log det(2π𝒞(U_0)/u), 𝒞(U_0) := (Hess_VΨ(U_0; ·)(𝔪(U_0)))^{-1};
(ii) Γ_{0→n}(V) = Γ^W(V) + Γ^cov(V) + Γ^dr(V) + const, with
  Γ^W(V) := [½log det'Hess_{U_0}(𝒯_0 + Ψ(·; V))|_slice − log Δ_FP]_{U_0 = Φ_0(V)},  Γ^cov := ½log det 𝒞∘Φ_0,
  Γ^dr(V) := Λ(Φ_0(V), V) − Λ(Φ_0(V), 𝔪(Φ_0(V))) = ⟨ω(Φ_0(V)), r(V)⟩ + O(|r|²),
r(V) := log(𝔪(Φ_0(V))^{-1}V) (the composite tree residual, linkwise) and ω(U_0) := ∂_VΛ(U_0, ·) at 𝔪(U_0) (in the frame of
𝔪(U_0));
(iii) for affine averaging maps (the abelian Gaussian case) Λ(U_0, ·) is constant, Γ^dr ≡ 0, and (ii) is Lemma F-split's
formula. For SU(N) the intermediate Hessian contains the terms (tree residual) × (second derivative of the averaging map),
so Λ depends on V and Γ^dr is present: **Lemma F-split, as stated in §5.5, omits Γ^dr [S2 correction]**; Lemma U-pair below
shows Γ^dr does not contribute to β, so F-split's use in §5.5 (the reduction (U-b), (U-c)) stands at the level of β.
*Proof.* (i) Laplace in V for ∫K_comp dV = 1 at order u⁰ (the Haar density in exponential coordinates is 1 + O(X²),
O(1/u) here). (ii) In F-tel's joint Hessian eliminate the intermediate levels at fixed (U_0, V): det H_joint =
det H_int·det S with S = Hess_{U_0}(𝒯_0 + Ψ(·; V)) (second-order envelope identity at the joint minimum, which is the tower);
½log det H_int + (the intermediate 𝒩'_1 terms) at the tower is Λ(Φ_0(V), V) by the definition of Λ (Laplace for the
intermediate integral at fixed (U_0, V); its tree point is the tower because the tower minimises jointly; with U_0 and V
fixed the intermediate integrand has no gauge degeneracy, since a gauge transformation of an intermediate level must also
act on U_0, so no intermediate slice or FP factor enters). Subtract and
add Λ(Φ_0, 𝔪(Φ_0)) and use (i). (iii) With affine means the intermediate Hessian is configuration independent. ∎

**Lemma U-pair (residual pairings have no marginal part): PROVEN-HERE.** Let ξ map fine configurations near 1 to
⊕_{level-n links c}su(N) (in the frame of 𝔪_c), C¹, with: (a) ξ(U^g) = ξ(U) for fine gauge transformations g with g = 1
at all level-n sites; (b) ξ(U^g)_c = Ad_{g(x_c)}ξ(U)_c for all g (x_c the base point of c); (c) ξ(1) = 0; (d) ℓZ⁴
translation covariance and B_4 covariance about level-n sites; (e) Dξ(1) has an exponentially decaying kernel in level-n
units. Let Q(v) := ⟨Dξ(1)[DΦ_0v], r(v)⟩ with r the linearised composite residual. Then the symbol of Q is O(|p|⁴); in
particular β[Q] = 0 (and Q contributes nothing to any marginal coefficient).
*Proof.* (1) For any fine 0-form λ and g_t = e^{tλ}: 1^{g_t} is a pure-gauge configuration and, by (b) and (c),
ξ(1^{g_t}) = Ad·ξ(1) = 0; differentiating at t = 0, Dξ(1)[dλ] = 0. So Dξ(1) vanishes on exact 1-forms and, by the lattice
Poincaré lemma (as in GT-lat step 1, with the locality (e)), Dξ(1)[a] = W[da] with W exponentially local.
(2) Symbols at level-n momentum p (F-ren's alias bookkeeping): the curvature of DΦ_0v is O(|p|) (Lemma F-bg: the K = 0
alias is the smooth interpolation, the aliases K ≠ 0 are O(|p|³)); r̂(p) = O(|p|²) (Lemma F-bg's κr = Ĝ^{-1}b, applied to the
composite with Ĝ_n^{-1} = O(|p|²)); Ŵ(p) is analytic. (3) Ŵ(0) = 0: at zero momentum the point inversion x ↦ -x about a
level-n site (an element of B_4, a symmetry by (d)) acts by +1 on constant curvatures (a plaquette goes to a plaquette with
both orientations reversed) and by -1 on constant link fields (orientation reversal); an intertwiner from a +1 to a -1
representation is 0. So Ŵ(p) = O(|p|) and the symbol of Q is O(|p|)·O(|p|)·O(|p|²) = O(|p|⁴). ∎
*Applications.* (1) ξ = ω: K_comp(V^{g_n}, U_0^g) = K_comp(V, U_0) (each kernel is covariant under the gauge
transformations of its two levels, D4-norm), so Λ inherits (a), (b); (c) by Lemma U-tad (i); (d) by the B_4 symmetry of
the nested S4' family (D4-norm (1); level-n sites are sites of every finer level for odd L). (e) is the hypothesis
(U-loc) of §18. Hence β[Γ^dr] = 0. (2) The r-linear part of Γ^W: Hess_{U_0}Ψ(U_0; V) = H^0(U_0) + ⟨r, ∂H(U_0)⟩ + O(r²) with
H^0(U_0) := Hess_{U_0}Ψ(U_0; V)|_{V = 𝔪(U_0)} = D𝔪^T𝒞^{-1}D𝔪 (the terms carrying V - 𝔪 vanish there), so
Γ^W = Γ^{W0}∘Φ_0 + ⟨ξ', r⟩ + O(r²), Γ^{W0}(U_0) := ½log det'(Hess𝒯_0 + D𝔪^T𝒞^{-1}D𝔪)(U_0)|_slice − log Δ_FP(U_0),
ξ' := ½tr[(Hess𝒯_0 + H^0)^{-1}∂H] (with the slice and FP pieces); ξ' satisfies (a)-(d) by the same covariance, so its pairing
with r has no marginal part. (3) O(r²) terms are O(|p|⁴). **[RFL-fix UP-1] (3) needs the O(|r|²) remainders of Γ^dr and
Γ^W to be bounded bilinear forms in r with exponentially local kernels (analytic symbols), so that their Hessian symbols are
O(p²)·O(1)·O(p²); this is now part of (U-loc') (§23: Λ_VV, Γ^W_rr), PROVEN there. [RFL-fix UP-2] Hypothesis (a) of the
lemma is not used in the proof (only (b), (c) enter step (1)); and "uniformly in n" in (U-loc) is not needed for
β[Q] = 0 at each n.**

**Corollary U-red (the reduced form of B_n): PROVEN-HERE given (U-loc).**
  B_n = −β[Γ^{W0}_n∘Φ_0] − β[Γ^cov_n],
where Γ^{W0}_n(U_0) = ½log det'(H_Wilson(U_0) + D𝔪_n(U_0)^T𝒞_n(U_0)^{-1}D𝔪_n(U_0))|_slice − log Δ_FP(U_0) is the one-loop
determinant of the Wilson background-field operator plus a gauge-covariant IR term (a "mass" for the block-averaged
component at scale ℓ = L^n), and Γ^cov_n = ½log det 𝒞_n∘Φ_0. Both Γ^{W0}_n and log det 𝒞_n are invariant under ALL fine
gauge transformations (H^0 and 𝒞 are conjugated by the level-n values of g), ℓZ⁴-periodic and B_4-symmetric. By
Lemma F-ren's alias argument (the K ≠ 0 aliases of DΦ_0v are O(|p|³) and the gauge-invariant kernel's cross terms
Π(q_0, q_K) are O(|q_0|)), β[F∘Φ_0] = β^fine[F̄] for such F (F̄ the ℓZ⁴-translation average, β^fine per fine site): **B_n is
the marginal coefficient of a gauge-invariant fine-lattice one-loop functional with an explicit, covariant IR term**. The
scalar-U(1) instance of exactly this functional (log det(M_A + κQ_A^†Q_A)) is check f5.

## 17. Lemma U-res (the log ℓ coefficient is a residue; target R3): PROVEN-HERE

Let BZ = [-π, π]⁴, dq := d⁴q/(2π)⁴. Let J_ℓ (ℓ ≥ 1) be integrable on BZ, J_* measurable on BZ∖{0}, and h continuous on
R⁴∖{0}, homogeneous of degree -4; put σ_h := (2π)^{-4}∮_{S³}h dσ. Suppose, with one constant A:
- (R-a) |J_ℓ(q) − J_*(q)| ≤ Aℓ^{-2}|q|^{-6} for q ∈ BZ, |q| ≥ 1/ℓ;
- (R-b) ∫_{|q|<1/ℓ}|J_ℓ|d⁴q ≤ A;
- (R-c) |J_*(q) − h(q)| ≤ A|q|^{-2} on BZ∖{0}, and sup_{S³}|h| ≤ A.
Then |∫_{BZ}J_ℓ dq − σ_h log ℓ| ≤ A(2π)^{-4}(1 + π² + 4π⁴ + 2π²log π + (2π)⁴π^{-4}) =: c_UA for all ℓ ≥ 1.
*Rate form.* If moreover J_ℓ(q) = J_*(q) − ℓ⁴φ_ℓ(ℓq) + E_ℓ(q) with ∫_{|Q|<1}|h − φ_∞|d⁴Q < ∞, |φ_∞(Q)| ≤ A|Q|^{-6} for
|Q| ≥ 1, ε_ℓ := ∫_{R⁴}|φ_ℓ − φ_∞|d⁴Q + ∫_{BZ}|E_ℓ|d⁴q, then ∫_{BZ}J_ℓ dq = σ_h log ℓ + c_∞ + O(Aℓ^{-2} + ε_ℓ), with
c_∞ := (2π)^{-4}[∫_{BZ}(J_* − h) + ∫_{|Q|<1}(h − φ_∞) + ∮h·log π + ∫_{BZ∖B_π}h − ∫_{|Q|≥1}φ_∞].
*Proof.* Split ∫_{BZ}J_ℓ = ∫_{|q|<1/ℓ}J_ℓ + ∫_{|q|≥1/ℓ}(J_ℓ − J_*) + ∫_{|q|≥1/ℓ}(J_* − h) + ∫_{|q|≥1/ℓ}h. The first is ≤ A; the
second ≤ Aℓ^{-2}·2π²∫_{1/ℓ}^∞r^{-3}dr = π²A; the third ≤ A·2π²∫_0^{2π}r dr = 4π⁴A; the fourth is ∮h·log(πℓ) + ∫_{BZ∖B_π}h,
and |∫_{BZ∖B_π}h| ≤ Aπ^{-4}(2π)⁴. Rate form: ∫_{BZ}(h(q) − ℓ⁴φ_∞(ℓq))d⁴q = ∫_{ℓBZ}(h − φ_∞)(Q)d⁴Q by Q = ℓq and the
homogeneity of h; split at |Q| = 1 and |Q| = πℓ; ∫_{ℓBZ∖B_{πℓ}}h = ∫_{BZ∖B_π}h; ∫_{|Q|≥1, Q∉ℓBZ}|φ_∞| ≤ A·2π²(πℓ)^{-2}/2. ∎
*Remarks.* (1) Only the leading homogeneous part of the massless integrand enters the coefficient of log ℓ; the IR
regulator (whatever it is) enters only through (R-a), (R-b), i.e. through the constant. This is the precise form of
"the coefficient of log L is a scheme-independent residue". (2) The p²-coefficient integrand depends on the loop
momentum routing; a change of routing changes J_* by a total derivative ∂_μ∂_νJ^{(0)} with J^{(0)} homogeneous of degree -2
at leading order, whose integral over 1/ℓ ≤ |q| ≤ π is a difference of two surface terms, each O(1): no log, so σ_h is
routing independent.

## 18. Theorem UNIV (UNIV-1L given (U-IR) and (U-loc)) and its inputs (target R4)

**Lemma U-Tay (the residue of the Wilson background-field Feynman integrand is the continuum one-loop coefficient):
PROVEN-HERE, with L4b (IMPORTED-AND-REVERIFIED).** Let J_* be the p²-coefficient integrand (analytic differentiation in
the external momentum as in §5.7/f3) of the massless one-loop polarisation of the Wilson action in background-covariant
Feynman gauge with adjoint FP ghosts, at the trivial background; let h be the integrand obtained by replacing every
lattice propagator 1/ω̂(q) and every vertex (a finite trigonometric polynomial) by its leading Taylor term. Then (R-c)
holds, and σ_h = −β_0^std/(log of the scale ratio), i.e. the coefficient of log ℓ in β of the IR-regulated functional is
−β_0^std = −11N²/(12π²) in u-units. **[RFL-fix UT-1] Read: σ_h = −β_0^std (u-units, per unit log ℓ), i.e. σ_h log ℓ =
−β_0^std n log L for ℓ = L^n; the phrase "/(log of the scale ratio)" is garbled and withdrawn.**
*Proof.* Each building block is (continuum leading term)·(1 + O(|q|²)) near q = 0 and bounded away from 0 on the rest of BZ
(ω̂(q) ≥ 4|q|²/π²); a finite sum of products of total degree −4 gives J_* = h + O(|q|^{-2}). The leading terms are the
continuum background-field Feynman-gauge rules (the Wilson action in a smooth background is the continuum action up to
O(a²) relative corrections, 1 − N^{-1}Re tr e^Y = ||Y||²_HS/(2N) + O(Y⁴), and the lattice covariant difference is D + O(a)),
so h is the continuum integrand of ½log det(−D²δ + 2i ad F) − log det(−D²). Apply Lemma U-res once more in the continuum
(UV cut by a proper-time or any regulator acting at |q| ≳ Λ, IR mass m) **[RFL-fix UT-2: Lemma U-res is a BZ lemma; what is
used here is the same four-piece split on R⁴, with the UV regulator in place of the BZ boundary: |q| < m, the IR-regulated
difference, J − h, and ∫_{m≤|q|≤Λ}h = ∮h·log(Λ/m), each piece bounded exactly as in U-res's proof]**: the coefficient of log(Λ/m) is σ_h·(the same sphere
integral). The heat-kernel computation (L4b: (½)a_2^vec − a_2^gh = (11/12)C_AF^aF^a, IMPORTED-AND-REVERIFIED, c2) gives that
coefficient as (11/12)C_A(16π²)^{-1}·2 per ∫F^aF^a per unit log(Λ/m), i.e. (×4, the tree term being (4g_std²)^{-1}∫F^aF^a)
2b_0 in 1/g_std² units, i.e. β_0^std in u-units
(Lemma F-norm). The sign: the one-loop term lowers the coefficient at the coarse scale (anti-screening). ∎

**Lemma U-cov-IR (IR decay of the composite fluctuation covariance, transverse sector): PROVEN-HERE.** In fine units, at
the trivial background, on transverse fields (P_⊥ at the coarse level), the fluctuation covariance of Γ^{W0}_n is, per fine
momentum class, C_n(q, q') = δ_{qq'}g(q) − ℓ^{-4}g(q)𝔪̂(q)^†Ĝ_n(P)^{-1}𝔪̂(q')g(q') (Woodbury; 𝔪̂ the composite average symbol,
Ĝ_n = 𝒞_n + ℓ^{-4}Σ_K𝔪̂Ĝ_0𝔪̂^† the level-n tree propagator, g = Ĝ_0), and
  |C_n(q, q) − g(q)| ≤ (π⁶/4)κℓ^{-4}|q|^{-6} for 0 < |q|, q ∈ BZ  (a relative correction ≤ π⁴κ(ℓ|q|)^{-4}).
*Proof.* Ĝ_n ≥ 𝒞_n ≥ κ^{-1}P_⊥ (Lemma F-tree's recursion: Ĝ_{k+1} = κ^{-1}P_⊥ + 𝒬(Ĝ_k), 𝒬 positivity preserving), so
||P_⊥Ĝ_n^{-1}P_⊥|| ≤ κ. P_⊥𝔪̂ = P_⊥𝔪̂_str (the composite of S4' averages is the composite straight average minus d∘h^{(n)}, by
Q_str∘d = d∘(ev + h∘d) and induction), and the composite straight average is the straight average over blocks of side ℓ
(the 1D Dirichlet sums telescope: Σ_{j<L}e^{iθj}·Σ_{j'<L}e^{iLθj'} = Σ_{m<L²}e^{iθm}), so |𝔪̂_μ(q)| ≤ ℓΠ_α|D_ℓ(q_α)|,
|D_ℓ(θ)| = |sin(ℓθ/2)/(ℓ sin(θ/2))| ≤ min(1, π/(ℓ|θ|)). With max_α|q_α| ≥ |q|/2: |𝔪̂(q)|² ≤ 4π²|q|^{-2}. And g(q) ≤ π²/(4|q|²).
So |C_n(q,q) − g(q)| ≤ ℓ^{-4}g²κ|𝔪̂|² ≤ ℓ^{-4}(π⁴/(16|q|⁴))κ·4π²|q|^{-2}. ∎ (The off-diagonal alias entries are bounded by
ℓ^{-4}κ|𝔪̂(q)||𝔪̂(q')|g(q)g(q'), the same estimate factor by factor; summing them against vertices uses Lemma F-depth's
alias sum Σ_K|𝔪̂_str(q_K)|² ≤ ℓ² (its Poisson-summation bound with L → ℓ). The longitudinal sector is not covered.)
**[RFL-fix UC-1] Status: CONFIRMED as stated (an undifferentiated bound). It does NOT give (R-a); the derivative form is
Lemma U-cov-IR' (§24), where the transverse sector is also defined exactly (it is slice independent, Lemma U-T⊥).**

**Hypotheses of Theorem UNIV (precise; each a statement about explicit trivial-background objects):**
- **(U-loc)** The first derivatives at the trivial point of ω and ξ' (Prop. U-dec, Lemma U-pair applications (1), (2)) have
  exponentially decaying kernels in level-n units, uniformly in n (the input (e) of Lemma U-pair). [Expected from N5-triv per level; not
  written.] **[RFL-fix UP-1, UP-2] Restated as (U-loc') in §23 (session 3): (i) uniformity in n is dropped (not needed
  for β[Q] = 0 at each n); (ii) the O(|r|²) remainders of Γ^dr and Γ^W are added (their kernels Λ_VV, Γ^W_rr must be
  exponentially local, so that their Hessian symbols are O(p²)·O(1)·O(p²)); (iii) ξ' is defined explicitly with its slice
  and FP pieces. (U-loc') is PROVEN in §23.**
- **(U-IR)** With J_n the ℓ-averaged p²-integrand of Γ^{W0}_n (fine units) and J_* of Lemma U-Tay: (a) (R-a) holds with a
  constant A_IR independent of n (it holds for the propagator by Lemma U-cov-IR; it must also hold for the terms with
  vertices of the covariant IR term D𝔪^T𝒞^{-1}D𝔪, and for the sparse block-centre/block-mean modifications of the
  Feynman gauge fixing that FP-ab's legitimate slice makes, which are finite rank per momentum class); (b) (R-b) with A_IR;
  (c) |β[Γ^cov_n]| ≤ A_cov uniformly in n. [Mechanism of (c): 𝒞_n = κ^{-1}(1 + Σ_{j≥1}A_jA_j^†), A_j the pushforward of
  level-(n−j) noise, ||A_jA_j^†|| ≤ L^{-2j} (Lemma F-depth's Λ ≤ L^{-2}); the background derivatives of A_j are bounded by the
  path lengths times the background, uniformly in j, so the second variation of log det 𝒞_n is ≤ CΣ_jL^{-2j}; ARGUED.]
  **[S4] §30: in the scalar U(1) instance (c) and (s2) are PROVEN in closed form (Proposition COV-sc); for the gauge chain
  the bracketed mechanism is false as stated: ||A_jA_j^†|| ≤ L^{-2j} fails on the coarse-gauge directions (Lemma COV-str (iv),
  ⟨v, 𝒞_nv⟩ ≥ (n/κ)||v||²); what remains is ~~(COV-NA)~~ **[RFL4-fix S4-4] (COV-GI) + (COV-⊥) (§35-§37): the bracketed
  L^{-2j} mechanism is true on the transverse sector P_⊥ (GS-1, GS-2), false only on G_n, where it is not needed.**
  **[RFL-fix UC-1, J_n definition, (a1)-(a4) split] The parenthetical "(it holds for the propagator by Lemma U-cov-IR)" in
  (a) is WITHDRAWN: Lemma U-cov-IR is an undifferentiated bound and does not give (R-a).** (R-a) bounds the p²-coefficient
  integrand, which contains first and second external-momentum derivatives of the propagator, and each q-derivative of the
  Dirichlet factors (and of the block-offset phases) costs a factor ~ℓ. What U-cov-IR gives is only |C_n(q, q) − g(q)| ≤
  (π⁶/4)κℓ^{-4}|q|^{-6} (no derivatives, transverse sector, diagonal alias entry). The derivative form is §24 (session 3).
  - **Definition of J_n (exact).** Γ^{W0}_n is ℓZ⁴-periodic. Its trivial-background Hessian at external fine momenta (k, −k)
    (modes ε_1e^{ikx} on 1-links, ε_2e^{−ikx} on 2-links; the translation average keeps only the K = 0 diagonal of the
    ℓZ⁴-periodic kernel) is T_12(k) = ∫_{BZ}dq/(2π)⁴ 𝒥_n(q; k), where 𝒥_n(q; k) is defined by: (i) the one-loop expression
    ½tr[C_nV_12] − ½tr[C_nV_2C_n'V_1] (C_n the slice-fixed fine covariance at the trivial background, C_n' the same at the
    shifted class, V the background vertices of the full fine operator O_n = H_Wilson + D𝔪_n^T𝒞_n^{-1}D𝔪_n + dP_resd*,
    including the vertices of the covariant IR term), minus the FP term's analogue; (ii) the trace is written per coarse
    momentum class P, with the alias sums over the ℓ⁴ fine aliases q_K of every internal index carried out inside the
    integrand; (iii) the integrand is assigned to the fine momentum q of the row index of the first C_n (cyclic start at
    vertex 1); (iv) routing: the external momentum enters at vertex 1 and leaves at vertex 2, the propagator from vertex 1
    to vertex 2 carries q, the other q + k. Then **J_n(q) := −∂_{k_1}∂_{k_2}𝒥_n(q; k)|_{k=0}** (analytic differentiation, as
    in f3/f5), and β^fine[Γ̄^{W0}_n] = ∫_{BZ}J_n dq/(2π)⁴. J_* is the same construction for the massless Wilson action in
    background-covariant Feynman gauge with adjoint FP ghosts (no aliases, no IR term). By Lemma U-res Remark (2) a change
    of routing moves J_n and J_* by surface terms with no log.
  - **(U-IR)(a) split.** (a) means (R-a) for J_n − J_*, and J_n − J_* = Σ_{i=1}^4 J^{(a_i)}_n with: (a1) the propagator
    part (every C_n replaced in turn by C_n − g, vertices those of J_*): transverse sector §24, PROVEN; longitudinal entries
    OPEN (§24.4); (a2) the IR-term vertices, the diagrams with ≥ 1 vertex of D𝔪_n^T𝒞_n^{-1}D𝔪_n: OPEN (f5/f5b/f6 test scalar
    instances); (a3) the slice modification, the residual-group fixing dP_resd* + δ(h^{(n)}) and its FP factor against the
    BF-Feynman dd* and ghost determinant: OPEN (§24.4 states the needed bound) **[RFL6-fix S6-1] RETIRED: after Lemma GH
    (§43) the slice enters only through the exact quotient, and Lemma FP-exact (§52) shows the tower's fixing with its
    Δ_FP(U_0) equals the S_0 quotient with no constant at every critical background satisfying (N); so "(a3) ≡ 0" there,
    and the comparison with BF-Feynman J_* defined here is superseded (the ghost is now G_gh, solved exactly)**; (a4) the longitudinal sector, the
    coarse-gauge modes (fine gradients dλ with ev λ ≠ 0, which carry only the IR term) and the transverse-longitudinal cross
    covariance: OPEN (§24.4). Each part must satisfy |J^{(a_i)}_n(q)| ≤ A_iℓ^{-2}|q|^{-6} for q ∈ BZ, |q| ≥ 1/ℓ, with A_i
    independent of n; then (a) holds with A_IR = ΣA_i. The word "sparse" above is replaced by this requirement.
    **[RFL3-fix S3-6] (1) Pointwise → integrated: per §24.3 (Lemma U-res') the requirement on each part is the integrated
    form ∫_{|q|≥1/ℓ}|J^{(a_i)}_n|d⁴q ≤ π²A_i with A_i independent of n; the pointwise bound above is sufficient, not needed.
    (2) No double count: the "longitudinal entries" of (a1) are the same diagrams as (a4) (P_LC^{ph}P_L, P_TC^{ph}P_L), so
    (a1) is now the transverse propagator part (a1⊥) only (PROVEN, Prop. U-a1⊥) and every longitudinal entry is in (a4).
    (3) What (a2) will need and §23 does not give: n-uniform locality of 𝒞_n and of the composite vertices. Lemma U-loc' is
    per n; (I3)'s gap κ/S_n degrades with n, so its Combes-Thomas rate m_n → 0. Session 4 (§30, Lemma COV-str (iv)) shows
    that 𝒞_n^{-1} has no n-uniform gap at all (⟨v, 𝒞_nv⟩ ≥ (n/κ)||v||² on coarse-gauge directions), so a proof of (a2) must
    work on the transverse compression (P_⊥𝒞_nP_⊥, as Lemma U-T⊥ does) or with the per-level structure, not with a uniform
    Combes-Thomas bound for 𝒞_n^{-1}.**
    **[RFL4-fix S4-4] Restated (binding, REVIEW_FLOW_S4 §5). (a2) := the IR-term vertices of the transverse inverse
    compression D𝔪^TP_⊥(P_⊥𝒞_nP_⊥)^+P_⊥D𝔪 (not of D𝔪^T𝒞_n^{-1}D𝔪); this removes S3-6 (3)'s demand for n-uniform locality of
    𝒞_n^{-1} (impossible by Lemma COV-str (iv)) and replaces it by n-uniform bounds on P_⊥𝒞_nP_⊥ (§37 at the trivial point
    and in the Cartan sector). (a4') := (a4) minus its coarse-gauge-mode block, which Lemma COV-GI (§36) absorbs exactly;
    what remains in (a4'): the transverse-longitudinal cross entries, the residual-slice longitudinal entries, and the
    𝒞-independent level-n determinants ½log det(D^*_{B_n}D_{B_n}) − ½log det(J^*J) of (COV-GI), taken together for IR
    safety. (c) := (c⊥) = (COV-⊥).**
- **(U-IR-s)** (for the rate only) the scaling form of Lemma U-res with ε_{ℓ_n} ≤ A_sθ^n for some θ < 1.
  **[RFL-fix (U-IR-s) precise] Restated:** there are n-independent J_* (as above), h (Lemma U-Tay) and a profile φ_∞ on R⁴
  with |φ_∞(Q)| ≤ A|Q|^{-6} for |Q| ≥ 1 and ∫_{|Q|<1}|h − φ_∞|d⁴Q < ∞, such that for every n (ℓ = L^n):
  (s1) J_n = J_* − ℓ⁴φ_ℓ(ℓq) + E_ℓ(q) on BZ, with the whole n-dependence in φ_ℓ − φ_∞ and E_ℓ, and
  ε_ℓ := ∫_{R⁴}|φ_ℓ − φ_∞|d⁴Q + ∫_{BZ}|E_ℓ|dq ≤ A_sθ^n;
  (s2) **a separate rate hypothesis for the covariance determinant:** there is c_cov with |β[Γ^cov_n] − c_cov| ≤ A_sθ^n.
  (s2) is needed because Γ^cov_n is not part of the J_n integral (Corollary U-red: B_n = −∫J_n − β[Γ^cov_n]); the session-2
  proof of Corollary UNIV-rate ("Γ^cov_n is included in φ_ℓ/E_ℓ") is wrong on this point.
  **[RFL5-fix S5-1] (s2) as stated above is the wrong statement and is REPLACED by (s2⊥).** After Lemma COV-GI (§36),
  β[Γ^cov_n] alone contains +½log det 𝒞^♭_G, whose n-behaviour is not controlled (λ_max(𝒞^♭_G) grows linearly in n in both
  f8 models). **(s2⊥)** there is c_⊥ with |β[½log det_⊥(P_⊥𝒞_nP_⊥)] − c_⊥| ≤ A_sθ^n, where in the root sectors
  ½log det_⊥(P_⊥𝒞_nP_⊥) = ½log det 𝒞_n − ½log det(D^*D) + ½log det(D^*𝒞_n^{-1}D) is read as one level-n group (REVIEW_FLOW_S5
  §2.2); Cartan sector: PROVEN (Proposition COV-⊥-C (c)). The 𝒞-independent determinants of (COV-GI) are assigned to the
  J side: with the orthogonal slice S_0 they combine EXACTLY (Lemma GH, §43) into the ghost group
  G_gh := ½log det(D^*_{B_n}D_{B_n}) − ½log det(D^*_{U_0}D_{U_0}), whose β is computed in closed form at constant Cartan
  curvature (Proposition GH-log, §44) and needs no rate hypothesis.

**Theorem UNIV: given (U-loc) and (U-IR), PROVEN-HERE.** For all n ≥ 0,
  |Σ_{k<n}b_k − β_0^std n log L| ≤ R_0 := c_U·A_IR + A_cov   (β_0^std = 11N²/(12π²)),
  **[RFL-fix notation] read R_0 := c_U·max(A_IR, A_Tay) + A_cov, as the next line says.**
with c_U the constant of Lemma U-res (with A := max(A_IR, A_Tay), A_Tay Lemma U-Tay's constant). This is (UNIV-1L).
*Proof.* Corollary U-red: B_n = −β^fine[Γ̄^{W0}_n] − β[Γ^cov_n]. β^fine[Γ̄^{W0}_n] = ∫_{BZ}J_n dq (the p²-coefficient as an
integral, f3's representation). (U-IR)(a), (b) and Lemma U-Tay give (R-a)-(R-c); Lemma U-res gives |β^fine[Γ̄^{W0}_n] −
σ_h log ℓ| ≤ c_UA with σ_h log ℓ = −β_0^std n log L (Lemma U-Tay, ℓ = L^n); (U-IR)(c) bounds the second term. ∎
**[RFL6-fix S6-4] The proof text just above (B_n = −β^fine[Γ̄^{W0}_n] − β[Γ^cov_n], with ∫J_n and (U-IR)(c)) is SUPERSEDED
by the re-split below and the binding J_n^⊥ definition that follows it; it is kept as the session-2 record only.**
**[RFL5-fix S5-1] Re-split for the regrouped functional (binding for any future write-up of the proof).** At the
critical backgrounds β needs (constant Cartan curvature; §36 Reading (b), conditional on (COV-GI-∞), which §45 supplies
at each fixed n given (L-loc)), Lemma COV-GI with the orthogonal slice S_0 and Lemma GH give
  Γ^{W0}_n + Γ^cov_n = G_⊥,n + G_gh,n,  G_⊥,n := ½log det_{ker D_0^*}(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥),
  G_gh,n := ½log det(D_n^*D_n) − ½log det(D_0^*D_0)  (D_0 := D_{U_0} fine, D_n := D_{B_n} level n),
and equivalently (Feynman form, §43 (iii)) Γ^{W0}_n + Γ^cov_n = ½log det_E(O^♯_n) − log det(D_0^*D_0) + ½log det(D_n^*D_n) +
½log det_⊥(P_⊥𝒞_nP_⊥), O^♯_n := H_W + D_0D_0^* + D𝔪^TΠD𝔪. So the UNIV proof reads B_n = −β^fine[G_⊥,n] − β^fine[G_gh,n],
and **J_n (l.769-781) is redefined** with O^♯_n in place of O_n = H_W + D𝔪^T𝒞^{-1}D𝔪 + dP_resd* (C_n := (O^♯_n)^{-1}, IR-term
vertices those of D𝔪^TΠD𝔪; the ghost loop is the full fine −log det(D_0^*D_0) and the level-n ghost ½log det(D_n^*D_n) enters
aliased), with the IR-singular parts grouped inside the integrand as G_⊥ and G_gh (each IR-safe, §44). The old split
"B_n = −∫J_n − β[Γ^cov_n]" stays correct as an identity but is not usable for a bound (its second term has no n-uniform
bound, by Lemma COV-str (iv)).
**[RFL6-fix S6-4] Binding definition (supersedes the J_n sentence just above).** G_gh,n is computed exactly (Proposition
GH-log) and is NOT part of any J-integrand. **J_n^⊥** is defined from G_⊥,n only, in the Feynman form
  G_⊥,n = [½log det_E O^♯_n − ½log det'Δ_0] + ½log det_⊥(P_⊥𝒞_nP_⊥),
where the bracket is ONE unit by definition: O^♯_n equals Δ_0 on Ran D_0 (§43 (v)), so it is massless there, and only the
difference with the ½log det'Δ_0 loop is IR safe. J_n^⊥(q) is the one-loop integrand of β^fine of the bracket (propagator
C_n = (O^♯_n)^{-1}, IR-term vertices those of D𝔪^TΠD𝔪, and the −½log det'Δ_0 loop subtracted inside the same integrand,
with the routing of Lemma U-res Remark (2)); the level-n group ½log det_⊥(P_⊥𝒞_nP_⊥) is handled with it (its IR safety in
the root sectors is OPEN and part of (s2⊥)). Then **B_n = −β^fine[G_⊥,n] − β^fine[G_gh,n] exactly**, with β^fine[G_gh,n] =
−(1/22)β_0^std log ℓ (Proposition GH-log, given G-mag (vi) **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]**; background-field Landau bookkeeping, §44 Reading (1)).
*Consequences.* With §5.5, Proposition F-1L, Theorem F-flow, Theorem F-tune, Lemma F-ind are now conditional on (U-IR),
(U-loc) (plus their previous layer-1 hypotheses) instead of on (UNIV-1L). U-F2 (a log in the kernel vertices) is excluded
for the residual-paired vertices (Lemma U-pair, all orders of the background map) and for the propagator's IR part
(Lemma U-cov-IR); for the covariant-IR-term vertices it is tested in f5/f5b (scalar U(1) instance). U-F3: the legitimate
slice (h, P_resD^*) is background Feynman gauge off a sparse set, so the leading integrand is the BF-Feynman one; the
sparse part sits in (U-IR)(a). U-F4: does not occur for the transverse straight part (Lemma U-cov-IR: the S4' gauge
parts are d-exact and drop out of P_⊥); the longitudinal sector is in (U-IR)(a).

## 19. The rate of b_k (target T2) and what it says about R

**Corollary UNIV-rate: [RFL-fix] session-2 status "PROVEN-HERE" WITHDRAWN: GAP** (the proof below used the imprecise
(U-IR-s) and the false step "Γ^cov_n is included in φ_ℓ/E_ℓ"; Γ^cov_n is not part of the J_n integral). **Repaired form
(arithmetic, not counted, unreviewed): given (U-loc), (U-IR) and the restated (U-IR-s) (s1)+(s2) of §18,** b_n = B_{n+1} − B_n
= −(∫J_{L^{n+1}} − ∫J_{L^n}) − (β[Γ^cov_{n+1}] − β[Γ^cov_n]); by U-res's rate form applied to (s1) at ℓ = L^{n+1}, L^n (c_∞
depends only on the n-independent J_*, h, φ_∞, so it cancels) and by (s2), |b_n − β_0^std log L| ≤ 2c_sA L^{-2n} + 4A_sθ^n.
Session-2 text follows unchanged:
**Corollary UNIV-rate (session 2): given (U-loc), (U-IR), (U-IR-s), PROVEN-HERE.** b_∞ = β_0^std log L and
|b_n − β_0^std log L| ≤ C_b(L^{-2n} + θ^n), C_b := 2(c_s A + A_s) (c_s from Lemma U-res's rate form).
*Proof.* b_n = B_{n+1} − B_n (Lemma F-tel); apply the rate form of Lemma U-res at ℓ = L^{n+1} and ℓ = L^n and subtract
(the constant c_∞ cancels; Γ^cov_n is included in φ_ℓ/E_ℓ). ∎
*Expected θ.* The composite objects in coarse units converge at the tree-tower rate L^{-2n} (Lemma F-depth, linear) and the
straight composite average converges to the continuum block average with O(ℓ^{-2}) corrections; so θ = L^{-2} is the
natural value [inference]. Data: f2's slopes approach 1 as ℓ^{-2} (|slope − 1|·ℓ_mid² ≈ 0.27, 0.27, 0.26, 0.25, 0.25 for
κ_c = 1 along (3,5), …, (13,15)), and f5b prints the same diagnostic. **[RFL-fix UR-1] Mislabelled: 0.27, 0.27, 0.26,
0.25, 0.25 are the κ_c = 0.25 values; for κ_c = 1 they are 0.60, 0.58, 0.56, 0.56, 0.55 (re-computed from f2_out in
session 3: pairs (5,7), …, (13,15)).** **[RFL-fix UR-2]** The data are consistent with O(ℓ^{-2}) as an upper rate; they do not show ℓ^{-2} (the
products are still falling in f5b).

**Lemma F-R (when can R be 0): PROVEN-HERE (arithmetic). [RFL-fix FRR-1] Only "if" directions are proven: the gap
0 < b_k ≤ C_ργ² is undecided, because ρ_k may have either sign. Correct reading: for some γ > 0, (F) with R = 0 holds IF
min_k b_k > 0 (given UNIV-rate — itself a GAP, §19 — a condition on b_0, …, b_{k_0−1}); it fails for small γ if some
b_k ≤ 0. In (ii) the quantifier order is: for each β_- > 0, failure once C_ργ² < β_- log L. In (iii) read "iff" as "if".** Under Proposition F-rem's hypotheses (|ρ_k| ≤ C_ργ²):
(i) if b_* := inf_kb_k > C_ργ², then (F) holds with R = 0 and β_- := (b_* − C_ργ²)/log L, β_+ := (sup_kb_k + C_ργ²)/log L;
(ii) if b_k ≤ 0 for some k, then for γ small (F) with R = 0 fails for the pair (j, n) = (k, k + 1) for every β_- > 0;
(iii) given Corollary UNIV-rate, b_k ≥ b_∞/2 for k ≥ k_0 := min{k: C_b(L^{-2k} + θ^k) ≤ b_∞/2}, so R = 0 holds (with
β_- ≥ min(b_∞/2, min_{k<k_0}b_k − C_ργ²)/log L) iff the finitely many numbers b_0, …, b_{k_0−1} exceed C_ργ²; and in any case the
additive constant needed for pairs j ≥ m is R_m ≤ C_bΣ_{k≥m}(L^{-2k} + θ^k) → 0: the deviation from the universal line sits
at the finest levels (k small), where the couplings are smallest.
*Proof.* (i) u_j − u_n = Σ_{k=j}^{n-1}(b_k + ρ_k) ∈ [(n − j)(b_* − C_ργ²), (n − j)(sup b + C_ργ²)]. (ii) u_k − u_{k+1} ≤ b_k + C_ργ²
≤ C_ργ² < β_- log L for γ small. (iii) Sum the rate bound. ∎

## 19A. Note on the additive constant R (target T3; consumers quoted read-only, nothing edited outside lane C)

What lane C delivers: (F_R) β_-(n − j)log L − R ≤ u_j − u_n ≤ β_+(n − j)log L + R (Theorem F-flow, R = 2R_0), with
β_± = β_0^std ± C_ργ²/log L; Lemma F-R: R = 0 iff (for small γ) every b_k > C_ργ², a condition on finitely many b_k given
Corollary UNIV-rate [RFL-fix FRR-1: "iff" → "if"; UNIV-rate is a GAP]; and in all cases the defect sits at the finest levels (R_m → 0 for pairs j ≥ m).

| consumer (file, place) | statement used (quoted) | needs from the flow | effect of R > 0 |
|---|---|---|---|
| RLARGE §0, hypothesis (F) | "β_-(k − j) log L ≤ 1/g_j² − 1/g_k² ≤ β_+(k − j) log L for 0 ≤ j ≤ k ≤ K" | the R = 0 two-sided form, all pairs | replace by (F_R); every place below |
| RLARGE §7.1 Lemma LF-n | "L^{4(K−i)}w_i^n ≤ C^ne^{−na/g_K²}L^{(4 − naβ_-)(K−i)}" (lower half substituted) | lower half | factor e^{naR}: C → Ce^{aR}; the convergence criterion naβ_- > 4 is unchanged |
| RLARGE §7.1, n_* = ⌊4/(a''β_-)⌋; §7.1 n_♯ = ⌊4/(a_♯β_-)⌋ | slope only | β_- | unchanged |
| RLARGE §6 Lemma RS ("RLF-F4 AVOIDED") and §7.1 [R-8] pricing | "priced unconditionally by the normalised soft kernel at the FINER coupling g_i (1/g_i² ≥ 1/g_{i+1}² under (F))"; "(Ce^{−a_RS/g_k²})^{n/c_RS} ≤ (Ce^{−a_RS/g_{k+1}²})^{n/c_RS}" | ONE-STEP monotonicity (F) at k − j = 1 | under (F_R) only 1/g_i² ≥ 1/g_{i+1}² − R: factor e^{a_RS R} per priced cube, absorbed in C; with Lemma F-R (iii) the monotonicity itself holds at all levels k ≥ k_0 |
| RLARGE §7.2 (iv) | "For these j, g_j ≤ g_K by (F)" | one-sided comparison | g_j² ≤ g_K²/(1 − Rg_K²) ≤ 2g_K² for g_K² ≤ 1/(2R) |
| RLARGE §8.4 (P1) | "Σ_kN_kΣ_{n>n_♯}80^{2(n−1)}(C_ℓe^{−a_♯/g_k²})^n ≤ C|T|e^{−(n_♯+1)a_♯/g_K²} for g_K ≤ g_0 (6400C_ℓe^{−a_♯/g_K²} ≤ ½)" | lower half (via LF-n) | C_ℓ → C_ℓe^{a_♯R}; g_0 smaller by an explicit R-dependent amount |
| RLARGE §8.4 (P2) | "Σ_k|δβ_k| ≤ C_*Σ_kg_k^{−6}e^{−a_♯/g_k²} ≤ C'e^{−a'''/g_K²}/(1 − L^{−a'''β_-})" | lower half | factor e^{a'''R} (and the polynomial g_k^{−6} ≤ (1/g_K² + β_-(K − k)log L + R)³) **[RFL-fix RN-2: read β_+ here; an upper bound on u_k = g_k^{-2} uses the upper half: g_k^{−6} ≤ (1/g_K² + β_+(K − k)log L + R)³]** |
| PLD.md Corollary PLD-fin (l.194) and its uses (l.199, l.208-209; l.392 with + R) **[RFL-fix RN-1, new row]** | "0 < g_0 ≤ g_1 ≤ … ≤ g_k (the order (F) gives)" | one-step monotonicity (exponents) and the upper half (prefactors) | the ordering is not implied by (F_R): replace 1/g_i² ≥ 1/g_k² in the exponents by 1/g_i² ≥ 1/g_k² − R (factor e^{a_kt²R} per term, absorbed in C at fixed k), or use it at levels with b_i > C_ργ²; the upper-half uses (prefactors at l.199; the comparison 1/g_{k-1}² ≤ 1/g_k² + β_+ log L at l.392) acquire + R, i.e. a factor e^{3κε_♮R} there |
| RLARGE §8.4 (P5) | "Theorem CE [S11] needs κ > 3κ_0 + 3, i.e. g_K² < a_♯/(8(3κ_0 + 3))" | g_K only | none |
| PROOF Prop. LF-count (l.4091-4102 **[RFL3-fix S3-4: stale; now l.4144-4172, the two quoted sentences at l.4151 and l.4153]**) | "Let g_k obey the upper half of (0.31), 1/g_k² ≤ 1/g² + β'(K − k) log L … C_K ≥ e^{−a/g²}Σ_{n=0}^K L^{(4 − aβ')n}"; "Conversely, if w_k ≤ e^{−a/g_k²} and the lower half of (0.31) holds with aβ > 4, then C_K ≤ e^{−a/g²}/(1 − L^{4−aβ})" | both halves, slopes decide | divergence: C_K ≥ e^{−a(1/g² + R)}Σ…, same criterion aβ' ≤ 4; convergence: factor e^{aR}. Its "[inference]" β'_B ≈ 4Nb_0 is now Lemma F-norm + Theorem UNIV (given (U-IR), (U-loc)) |
| EXISTENCE H-Bal-1 (l.130-140) | "1/g² + β(K − k) log L ≤ 1/g_k² ≤ 1/g² + β'(K − k) log L" with g_k ∈ (0, γ], g_K = g, γ, g_1, β, β' independent of M | two-sided, R = 0 form, M-uniform | Theorem F-tune gives it with −R / +R and M-uniformity (Def F-g, (SF-∞)) |
| EXISTENCE X-NTAF (l.788-799) | "(δ_*/2)/(1/g² + β'm log L) ≤ ω(1 − P_{p,m}) ≤ φ(G_m), G_m := (1/g² + βm log L)^{−1/2}" | both halves at each m | replace 1/g² + β'm log L by 1/g² + β'm log L + R and G_m by (1/g² + βm log L − R)^{−1/2} (positive: 1/g² ≥ γ^{−2} + R by F-tune's g ≤ g_1); X-NTAF-AF's m → ∞ statements unchanged |
| EXISTENCE X-ND / X-MONTEL (l.399, 418) | "g_{m,K} in a compact subinterval of (0, γ]"; "g_min the K-uniform lower bound of H-Bal-1" | a K-uniform lower bound | g_{m,K} ≥ (1/g² + β_+m log L + R)^{−1/2}: unchanged in kind |
| EXISTENCE X-NTAF-sharp, wall W-AF1 (l.57) | "the sharp coefficient c_blk g_m² with g_m² ~ 1/(2b_0 m log L)" | the universal slope | Theorem UNIV (given (U-IR), (U-loc)): u_m/(m log L) → β_0^std, i.e. 1/g_std,m² ~ 2b_0 m log L (Lemma F-norm); R is lower order |
| PROOF L4a-flow (l.1104-1105), E8.3/E7.0 | "They stay conditional on L4a-flow with β' < 6.1·2b_0" | the slope β_+ | β_+/(2N) = 2b_0 + C_ργ²/(2N log L): holds for γ small (given (U-IR), (U-loc)) |

Summary for the lead: no consumer needs R = 0. Two kinds of use exist: (1) slope uses (n_*, n_♯, LF-count's thresholds,
X-NTAF-AF, W-AF1, E8.3), which R does not touch; (2) constant-factor uses (LF-n, (P1), (P2), RS's one-step comparison,
§7.2 (iv), X-NTAF at fixed m), which acquire explicit factors e^{aR} absorbed into C and into the choice of g_0. The single
place that is literally false under (F_R) as written is RS's "1/g_i² ≥ 1/g_{i+1}² under (F)"; its repair is the e^{a_RS R}
factor (or Lemma F-R (iii) if the finitely many b_k with k < k_0 are positive).
**[RFL-fix RN-1] The preceding sentence is wrong twice over. (a) RS's one-step monotonicity is NOT IMPLIED by (F_R); it is
not false: u_i − u_{i+1} = b_i + ρ_i ≥ b_i − C_ργ², so it holds at every level with b_i > C_ργ². (b) It is not the single
place: RLARGE §7.2 (iv) ("For these j, g_j ≤ g_K by (F)", RLARGE l.482) and PLD.md Corollary PLD-fin ("0 < g_0 ≤ g_1 ≤ … ≤
g_k (the order (F) gives)", PLD.md l.194) assume the same ordering; both are repaired as in their rows (§7.2 (iv): g_j² ≤
g_K²/(1 − Rg_K²); PLD-fin: row below).** Suggested (F_R) wording carries the quantifier [RFL-fix FI-2]: "for the chain's own
effective sequence (Def F-g)". Suggested wording for RLARGE §0 (not
applied): "(F_R): β_-(k − j) log L − R ≤ 1/g_j² − 1/g_k² ≤ β_+(k − j) log L + R".

## 20. Session-2 outcomes against §14 (ADDED AFTER the derivations and checks)

**Checks.**
- **f5** (checks/f5_criteria.md, f5_cov_kernel.py, f5_out.txt, f5_time.txt; 863 s, peak 373 MB; NUMERIC LOCK): (A) FAIL
  as pre-registered (step 1e-4 is roundoff-limited: total 1.9e-5 relative; the M-only part 1.2e-6); POST-HOC labelled A'
  (step 1e-3): 2.3e-7, 4.2e-7. (A2) PASS (gauge invariance 2e-15). (B) PASS (Ward identity 6e-17 against a scale 1e-2; the
  M-only part alone violates it at 5%: the kernel vertices are needed for gauge invariance). (C) FAIL (midpoint quadrature
  n_P = 6 vs 10: 2%). (D) FAIL (k-step 7e-6 relative). (E) PASS: slopes × 48π² at (11, 13) = 0.9977, 0.9972, 0.9944 for
  κ_c = 0.25, 1, 4. (F) PASS: spread 0.0034. (G) PASS: kernel-vertex slopes × 48π² at (11, 13) = -0.0003, 0.0000, 0.0016.
- **f5b** (checks/f5b_criteria.md, f5b_quad.py, f5b_out.txt, f5b_time.txt; 641 s, peak 397 MB): written after f5's (C),
  (D) failures and before f5's (E)-(G) outcomes. (S) FAIL as pre-registered (symmetry defect 1.1e-12 against a 1e-12 line:
  roundoff; the symmetries hold). (C') FAIL for κ_c = 0.25 (2.3e-4) and κ_c = 1 (2.4e-5), PASS-level for κ_c = 4 (8e-7).
  (D') PASS (1.5e-7). (E') PASS: 0.9988, 0.9973, 0.9944. (F') PASS: 0.0044. (G') PASS: kernel-vertex slopes -0.0002, 0.0000,
  0.0016 at (11, 13), decreasing from (7, 9). The κ_c = 0.25 values of f5 were off by up to 9% [RFL-fix CK-2: up to 12.5%,
at ℓ = 3 (0.0039405 vs 0.0035032); ≈ 9.5% at ℓ = 5; the absolute offset is ℓ-independent, 4.34-4.38·10⁻⁴] (quadrature), but the
  slopes agree with f5b's to 0.001: the quadrature error is nearly ℓ-independent in coarse units.
- **Reading.** In the scalar-U(1) instance of Γ^{W0} (Corollary U-red), with a gauge-covariant block kernel at scale ℓ
  and all kernel vertices: the log ℓ coefficient is the universal 1/(48π²) to 0.3-0.6% at ℓ ≈ 12, κ-independently; the
  diagrams with ≥ 1 kernel vertex converge to κ-dependent constants (c^K(13) = -1.19e-4, -2.89e-4, -5.95e-4) and carry no
  log ℓ. Informational: |slope − 1|·ℓ_mid² → 0.168, 0.392, 0.804 (κ_c = 0.25, 1, 4), i.e. the ℓ^{-2} approach that
  Corollary UNIV-rate predicts with θ = L^{-2}. **[RFL-fix UR-2] Overstated: the products are still falling (κ_c = 1:
  0.541 → 0.392; κ_c = 4: 1.288 → 0.804); the data are consistent with O(ℓ^{-2}) as an upper rate, they do not show ℓ^{-2}.** Limits: one block of side ℓ, not the iterated S4' chain; abelian, scalar
  (Ω² channel only); 𝒞 constant (Γ^cov not tested).

**Targets.**
- **T1 (UNIV-1L): reduced, not discharged.** Theorem UNIV is PROVEN given (U-IR) and (U-loc), two precisely stated
  estimates on explicit trivial-background objects (§18). Proven unconditionally along the way: Lemma U-tad (D²Φ never
  enters: U-F1 does not occur), Proposition U-dec (with the correction that Lemma F-split omits a drift term Γ^dr for
  SU(N)), Lemma U-pair (every residual pairing, Γ^dr included, has no marginal part: the S4' family's point inversion kills
  the zero-momentum coupling), Lemma U-res (the coefficient of log ℓ is a residue of the massless integrand; any IR scheme
  only moves the constant), Lemma U-Tay (that residue is −β_0^std, via L4b), Lemma U-cov-IR (the composite propagator's IR
  part decays like (ℓ|q|)^{-4} in the transverse sector, S4' gauge parts drop out). U-F2: excluded for residual pairings
  and for the propagator, tested (not proven) for the covariant-IR-term vertices (f5/f5b). U-F3: the legitimate slice is
  BF-Feynman off a sparse set (in (U-IR)(a)). U-F4: does not occur in the transverse sector; longitudinal sector in (U-IR)(a).
- **T1 (R5) normalisation: PROVEN** (Lemma F-norm): 11N²/(12π²) per log L in u = 1/g_k² = 2N/g_std² units equals
  2N × 2b_0 = 2N × 11N/(24π²); U-F5 does not occur.
- **T2 (rate):** Corollary UNIV-rate, PROVEN given (U-IR-s) as well: |b_n − β_0^std log L| ≤ C_b(L^{-2n} + θ^n). Lemma F-R
  (arithmetic, PROVEN): R = 0 holds iff [RFL-fix FRR-1: read "if"] (for small γ) all b_k > C_ργ², which given the rate is a condition on finitely many
  b_k; otherwise R is needed only for pairs reaching the finest k_0 levels.
- **T3 (R note):** §19A. No consumer needs R = 0; RS's one-step monotonicity is the one statement that needs an explicit
  e^{a_RS R} repair (or Lemma F-R (iii)). [RFL-fix RN-1: "not implied", not "false"; and not the one statement: RLARGE
  §7.2 (iv) and PLD-fin (PLD.md l.194) assume the same ordering; §19A rows.]

**Open items after session 2 (weights).** (U-IR) [s-P]: (a) the covariant-IR-term vertex diagrams and the sparse
gauge-fixing modification and the longitudinal sector for SU(N) with the iterated S4' composite (the f5 mechanism, written
as bounds), (b), (c) the Γ^cov bound (mechanism written, ARGUED). (U-loc) [s]: exponential locality of Dω(1), Dξ'(1)
(from N5-triv per level). (U-IR-s) [s-P]: the scaling form. Layer-1 hypotheses of §4 unchanged. Next check to design: f6,
the iterated two-level covariant chain (ℓ = 9 = 3·3, composite paths through the intermediate centre, with the
background-dependent 𝒞) against the single-block f5b value at ℓ = 9, to test (U-IR)(c) and the composite structure.

## 21. Tally after session 2 (FLOW.md items; all unreviewed)
**[RFL-fix tally] Corrected by the review: 20 PROVEN-HERE (21 − Lemma F-split, which is WRONG as stated and superseded by
Proposition U-dec), every one conditional exactly as labelled; Corollary UNIV-rate is a GAP (not counted); Lemma F-R is
"if", not "iff". The (SF-bg) sentence below is narrowed by FT-1: (SF-bg) is not needed for B_n (composite route, U-tad);
it IS used (orders 3, 4 at the trivial point) for the per-step b_k = −β[Γ_k] of Def F-g / Prop. F-rem and for the identity
B_n = Σb_k via F-tel. Current tally: §28.** Session-2 text follows unchanged:
- **PROVEN-HERE (session 1: 12; session 2: +9 = 21):** session 2: Lemma F-norm, Lemma U-tad, Proposition U-dec, Lemma
  U-pair, Corollary U-red [given (U-loc)], Lemma U-res, Lemma U-Tay [with L4b], Lemma U-cov-IR, Theorem UNIV [given (U-IR),
  (U-loc)]; plus Corollary UNIV-rate [given also (U-IR-s)] and Lemma F-R (arithmetic) counted with Theorem UNIV.
- **Corrected:** Lemma F-split (§5.5) is exact only for affine averaging maps; the missing Γ^dr has no marginal part, so
  the uses of F-split stand at the level of β.
- **IMPORTED-AND-REVERIFIED (used):** L4b — 1 (unchanged).
- **OPEN:** (UNIV-1L) replaced by (U-IR) [s-P] and (U-loc) [s]; the rate needs (U-IR-s) [s-P].
- **HYPOTHESES consumed (layer 1, unchanged):** (SF-g), (RLF-δ), (SF-cont), (SF-∞); (SF-bg) is no longer needed for the
  one-loop coefficient (Lemma U-tad), only (as before) for Def F-strip's tower beyond second order elsewhere.

---
# Session 3 of lane C (opened 2026-10-28 00:46 UTC)

## 22. Session-3 targets (pre-stated 2026-10-28 01:00 UTC, before any session-3 derivation, criteria file or script)

Binding input: REVIEW_FLOW_S1_S2.md (hostile review of sessions 1-2). Every fix it requires is applied in place and
tagged **[RFL-fix]**; session-1/2 text is otherwise unchanged. Session-3 outcomes are in §27 (added afterwards).

**Target S3-1 ((U-loc), session-scale).** Prove (U-loc) as restated with fixes UP-1/UP-2: for each n, the four
trivial-background bilinear objects Dω(1), Dξ'(1) (first derivatives, fine → level-n links), Λ_VV := Hess_VΛ(1, ·)(1) and
Γ^W_rr := Hess_r Γ^W(1; ·)(0) (the O(r²) remainders of Prop. U-dec / Lemma U-pair, level-n → level-n) have exponentially
decaying kernels in level-n units, with ξ' defined explicitly including the slice and FP pieces. Pre-stated route: a
Bloch/Combes-Thomas algebra on the ℓZ⁴-periodic joint lattice (Lemma CT, infinite-lattice form), positivity of the
intermediate Hessian at fixed endpoints, of 𝒞_n, and of the composite-slice fine operator (Proposition PG^{(k)}), and the
finite range of the explicit vertex tensors. Uniformity in n is NOT targeted (UP-2: not needed for β[Q] = 0 at each n).
**Target S3-2 (U-cov-IR', the derivative form).** Momentum-derivative bounds |∂^α_q(C_n − g)| on the composite fluctuation
covariance with the ℓ-cost per derivative tracked, as needed for (R-a); prove it for the transverse sector (defined
exactly, including whether the slice enters it); state exactly what the longitudinal and slice parts need.
**Target S3-3 (f6, a falsification test).** The iterated two-level covariant chain (scalar U(1) instance of Γ^{W0} + Γ^cov
with composite paths through the intermediate centres and the background-dependent composite covariance) against the
single block, with a tighter kernel-vertex criterion than f5 (G), pre-registered: criteria file first, its `stat` copied
into FLOW_LOG before the script is written.

**Failure modes (each a valid outcome).** (S3-F1) the intermediate Hessian at fixed endpoints or the composite-slice
operator has no gap at some Bloch momentum (then (U-loc) fails at that n); (S3-F2) a q-derivative of C_n costs more than
one power of ℓ relative to C_n − g (then (R-a) fails at second order); (S3-F3) the slice changes the transverse-sector
covariance (then U-cov-IR is not slice-independent); (S3-F4) f6: the iterated kernel-vertex part, or the composite-
covariance part, shows a log ℓ, or the M-only part differs from the single block's at matched covariance.

---
# Session-3 derivations (written after §22)

## 23. (U-loc), session-scale (target S3-1): PROVEN-HERE

Throughout, n ≥ 1 is fixed, ℓ = L^n, and everything is at the trivial configuration in normalised exponential
coordinates about each link value (the equivariant chart of Lemma U-tad). By global-colour covariance every bilinear
object below is δ_{ab} × (a real kernel) (Ad is absolutely irreducible on su(N); the argument of Lemma F-Π (i)), so one
colour suffices. Per HIST Lemma HF (§3.1 fix) only derivatives of order ≤ 4 of k̃ (equivalently of φ_M: k̃ − φ_M = d(M) =
O(y⁶)) and of order ≤ 2 of the one-loop normalisation factor log 𝒩'_1 enter; so every statement holds verbatim for either
tower and for the HIST-corrected one-loop factor.

**23.1 Index sets, kernels.** 𝔛 := the disjoint union of the link sets of levels 0, …, n of the infinite lattice; a
level-k link sits at its base point, in level-n units (a point of L^{k−n}Z⁴); d := the ℓ¹ distance of base points in
level-n units. Z⁴ (level-n translations) acts on 𝔛 with finitely many orbits. For a kernel K on 𝔛_1 × 𝔛_2 put
N_m(K) := max{sup_xΣ_y|K(x, y)|e^{md(x,y)}, sup_yΣ_x|K(x, y)|e^{md(x,y)}} and D_m(K) := the same with e^{md} − 1. K is
*m-local* if N_m(K) < ∞, *local* if m-local for some m > 0. A *local vertex map* of order j is a j-linear map from fields
on 𝔜 to kernels on 𝔛 whose value on unit vectors e_{y_1}, …, e_{y_j} vanishes unless every argument and both kernel indices
lie within distance r of y_1 (some fixed r), with bounded entries.

**Lemma BL (the local algebra): PROVEN-HERE.**
(i) N_m(K_1K_2) ≤ N_m(K_1)N_m(K_2); if N_{m_0}(K) < ∞ and 0 < m ≤ m_0 then D_m(K) ≤ (m/m_0)N_{m_0}(K); pointwise
|K(x, y)| ≤ N_m(K)e^{−md(x,y)}.
(ii) (Combes-Thomas, infinite lattice) If K is symmetric, m_0-local and K ≥ γ > 0 on ℓ²(𝔛), then with
m := m_0·min{1, γ/(2N_{m_0}(K))}: |K^{-1}(x, y)| ≤ (2/γ)e^{−md(x,y)}, so K^{-1} is m''-local for every m'' < m.
(iii) If Π is an orthogonal projector with Π and 1 − Π local and ΠKΠ ≥ γ on ran Π (K symmetric, local), then
Π(ΠKΠ|_{ran Π})^{-1}Π is local.
(iv) If K is symmetric and local on ℓ²(𝔛_a ⊕ 𝔛_b) with K_bb ≥ γ_b > 0, then K_bb^{-1}K_ba and the Schur complement
K_aa − K_abK_bb^{-1}K_ba are local.
(v) If C_1, C_2 are local kernels on 𝔛 and V_1, V_2 local vertex maps of order 1 (from fields on 𝔜_1, 𝔜_2), V_12 of
order 2, then B(y_1, y_2) := tr(C_1V_1[e_{y_1}]C_2V_2[e_{y_2}]) and B'(y_1, y_2) := tr(C_1V_12[e_{y_1}, e_{y_2}]) are local;
compositions of local vertex maps with local linear maps in any argument are local vertex maps up to an exponentially
decaying tail (i.e. with the support condition replaced by an e^{−m·dist} bound), and (v) holds for those as well.
*Proof.* (i) e^{md(x,z)} ≤ e^{md(x,y)}e^{md(y,z)}; for t ≥ 0, e^{mt} − 1 ≤ (m/m_0)(e^{m_0t} − 1) (convexity of t ↦ e^{mt} in
m); the pointwise bound is one term of the row sum. (ii) Lemma CT's proof (PROOF [S18], for finite sets) with the weight
f_R := min{d(·, y_0), R} (1-Lipschitz and bounded, so E := e^{mf_R} and E^{-1} are bounded operators): the kernel of
EKE^{-1} − K is bounded by |K|(e^{md} − 1), so by the Schur test ||EKE^{-1} − K|| ≤ D_m(|K|) ≤ (m/m_0)N_{m_0}(K) ≤ γ/2, and
||K^{-1}|| ≤ 1/γ; hence EK^{-1}E^{-1} = (EKE^{-1})^{-1} has norm ≤ 2/γ and |K^{-1}(x, y_0)|e^{mf_R(x)} ≤ 2/γ; let R → ∞.
m''-locality: Σ_y e^{−(m − m'')d(x,y)} < ∞ because the number of points of 𝔛 at distance ≤ t from x is ≤ c(n)(1 + t)⁴.
(iii) K̃ := ΠKΠ + (1 − Π) is symmetric, local (by (i)) and ≥ min(γ, 1); K̃^{-1} = Π(ΠKΠ|)^{-1}Π + (1 − Π); apply (ii).
(iv) (ii) for K_bb, then (i). (v) |B(y_1, y_2)| ≤ v_1v_2Σ|C_1(x_1', x_2)||C_2(x_2', x_1)| over the ≤ c(n, r)⁴ index
quadruples within distance r of y_1 resp. y_2, and |C_i(x, x')| ≤ N_m(C_i)e^{−md(x,x')} ≤ N_m(C_i)e^{2mr}e^{−md(y_1,y_2)}
(triangle inequality); B' likewise with one kernel. Compositions: the support condition becomes an exponential tail by (i),
and the same estimate goes through with the tail summed by (i). ∎

**23.2 Inputs (each PROVEN, here or upstream).**
- **(I1) Vertex tensors.** The derivatives of order ≤ 4 at 1 of f_V := κΣ_{k<n}Σ_ck̃(U_{k+1,c}, M̄_c(U_k)), of Σ_ps(U_p), and
  of order ≤ 2 of the one-loop factors log𝒩'_1∘P∘M̄ are local vertex maps with r ≤ 2 (level-n units): each term involves
  the links of one plaquette or of one coarse link's contour support (two adjacent level-(k+1) blocks, PROOF N5-loc: range
  ≤ p_L in level-k units), and the functions are analytic near 1 with bounded derivatives. D(log𝒩'_1∘P∘M̄)(1) = 0
  (P = (M̄*M̄)^{1/2} = 1 + O(a²)).
- **(I2) The intermediate Hessian at fixed endpoints has a gap.** H_int := Hess_{(U_1,…,U_{n−1})}f_V at (U_0, V) = (1, 1)
  is, per colour, the form κΣ_{k=0}^{n−1}|a_{k+1} − Q_ka_k|² with a_0 = a_n = 0 (Q_k := DM̄(1) = Q_root at level k, in level
  units; the polar factor W has DW(1) = DM̄(1)). With q := sup_k||Q_k||_{ℓ²→ℓ²} ≤ (16p_L)^{1/2} (Schur test with N5-loc's
  column sums ≤ 16 and row sums ≤ p_L) and S_n := Σ_{m<n}q^{2m}: **H_int ≥ κ/((n − 1)S_n)**. *Proof.* Put r_j := a_{j+1} −
  Q_ja_j. Then a_k = Σ_{j<k}Q_{k−1}⋯Q_{j+1}r_j, so |a_k| ≤ Σ_{j<k}q^{k−1−j}|r_j| ≤ S_n^{1/2}(Σ_j|r_j|²)^{1/2} and
  Σ_{k=1}^{n−1}|a_k|² ≤ (n − 1)S_nΣ_{j=0}^{n−1}|r_j|². ∎ (No gauge zero mode: with U_0 and V fixed none remains, as in
  Prop. U-dec.) H_int is symmetric and local (finite range per level).
- **(I3) The composite covariance.** 𝒞_n^{-1} = Hess_VΨ(1; ·)(1) is the Schur complement of the Hessian of f_V in
  (intermediates, V) at U_0 = 1 onto V, hence local (BL (iv), (I2)); and **κ/S_n ≤ 𝒞_n^{-1} ≤ κ** (lower: b = Σ_jQ_{n−1}⋯
  Q_{j+1}r_j gives |b|² ≤ S_nΣ|r_j|²; upper: a_1 = … = a_{n−1} = 0). So 𝒞_n is local (BL (ii)).
- **(I4) The composite-slice fine operator has a gap.** O_n := d*d + Q^{(n)T}𝒞_n^{-1}Q^{(n)} + dP_resd* on
  H_0^{(n)} = ker h^{(n)} (Q^{(n)} = D𝔪_n(1), the composite root map; h^{(n)}, Λ_res the composite slice of FP-ab /
  Prop. PG^{(k)}). Since 𝒞_n^{-1} ≥ κ/S_n, O_n ≥ O_FP^{(n)}(κ/S_n) := d*d + (κ/S_n)Q^{(n)T}Q^{(n)} + dP_resd*, and
  Proposition PG^{(k)} (PROOF l.2915-2918, PROVEN-HERE upstream, uniformly in k and in the torus side T ≥ 2) gives
  **O_n ≥ γ_n := min{min(1, κ/S_n)/C_IT(L), 4} on H_0^{(n)}** on every torus (in PG's normalisation, a fixed rescaling at
  fixed n). Infinite volume: O_n and h^{(n)} are periodic and local; h^{(n)}(X) is supported in B(X) and is the translate of
  one vector w^{(n)} (IT-line (b)), so h^{(n)}h^{(n)T} = ||w^{(n)}||²·1 with w^{(n)} ≠ 0 (h^{(n)}(dλ) = Mλ − λ(c_X), IT-line
  (a)), the projector Π^{(n)} = 1 − h^{(n)T}h^{(n)}/||w^{(n)}||² onto H_0^{(n)} is local, and the Bloch fibres of Π O_nΠ are
  continuous in the Bloch momentum θ; a torus of side T realises the fibres at θ ∈ (2π/T)Z⁴, so the gap holds on a dense set
  of θ, hence for all θ, hence on ℓ²(𝔛_0). So the slice-fixed fine covariance C_n := Π(ΠO_nΠ|_{H_0})^{-1}Π is local
  (BL (iii)).
- **(I5) Linear towers.** The intermediate tower (U_0, V) ↦ U_int*(U_0, V) has DU_int*(1, 1) = −H_int^{-1}∂_{(U_0,V)}∇_{int}f,
  local (BL (iv)); its derivatives of order 2, 3 at (1, 1) are, by the implicit function theorem, −H_int^{-1} applied to
  finite sums of contractions of ∇^{≤4}f(1) with lower-order derivatives of the tower: local vertex maps with exponential
  tails (BL (v), induction on the order). The fine tower DΦ_0(1): b ↦ C_nQ^{(n)T}𝒞_n^{-1}b (the minimiser of the
  O_n-problem on H_0, which is a minimiser of the gauge-invariant problem: on its residual orbit a* + dΛ_res the term
  ½||P_resd*·||² attains 0, since P_resΔ_0 is invertible on Λ_res, N5-coer (1)) is local, and so is the linearised composite
  residual r_lin = (1 − Q^{(n)}DΦ_0(1))b.

**23.3 The objects (explicit definitions; the fix UP-1 and the definition of ξ').**
- Λ(U_0, V) = ½log det H_int(U_0, V) + Σ_{0<k<n}Σ_clog𝒩'_1(P_c(U_k*(U_0, V))) + (V-independent terms), H_int(U_0, V) the
  intermediate Hessian of f_V at the intermediate tower (Prop. U-dec (ii)). **Λ_VV := Hess_VΛ(1, ·)(1)**, and
  **Dω(1)[a] = ∂_U∂_VΛ(1, 1)[a, ·] + ∂²_VΛ(1, 1)[Q^{(n)}a, ·]** (chain rule through 𝔪, D𝔪(1) = Q^{(n)}; the change of frame of
  𝔪(U_0) multiplies ∂_VΛ(1, 1) = 0, Lemma U-tad (i)).
- 𝔊(U_0, r) := ½log det(Π_{U_0}O(U_0; r)Π_{U_0}|_{H_0(U_0)}) − log Δ_FP(U_0), with O(U_0; r) := Hess_{U_0}(𝒯_0 + Ψ(·; V))
  at the point U_0 for V := 𝔪(U_0)e^r (linkwise, frame of 𝔪(U_0)), plus the residual Feynman term D_{U_0}P_res^{U_0}D_{U_0}*;
  Π_{U_0}, H_0(U_0), P_res^{U_0}, Δ_FP(U_0) are those of the covariant slice χ_{U_0} = (h_{U_0}, P_res^{U_0}D_{U_0}*) of
  Proposition NA-FP (PROOF [S14]), analytic in U_0 near 1 (parallel transports along the funnel paths) **[RFL7-fix S7-1]
  (Δ_FP(U_0) := |det χ_{U_0}Γ_{U_0}|·det(h_{U_0}h_{U_0}^*)^{-1/2} (§52); NOT FP_U^{-1} of NA-FP (iii): the two differ by the
  U_0-dependent factor det(Γ^TΓ)^{1/2} = det(Δ')^{1/2}, of the size of β[G_gh])**. Γ^W(V) =
  𝔊(Φ_0(V), r(V)).
  **ξ'(U_0) := ∂_r𝔊(U_0, 0) = ½tr[𝒢(U_0)·∂_rO(U_0; 0)]**, 𝒢(U_0) := Π_{U_0}(Π_{U_0}O(U_0; 0)Π_{U_0}|)^{-1}Π_{U_0}. *The slice
  and FP pieces:* the slice data and Δ_FP depend on the background U_0 only, so they contribute nothing to ∂_r; they enter ξ'
  only through 𝒢 (and Dξ'(1) through D𝒢(1), which contains DΠ_{U_0}(1) and DP_res^{U_0}(1)).
  **Γ^W_rr := ∂²_r𝔊(1, 0) = ½tr[𝒢∂²_rO] − ½tr[𝒢∂_rO𝒢∂_rO]** (at U_0 = 1, r = 0), and Dξ'(1)[a] = ½tr[D𝒢(1)[a]∂_rO] +
  ½tr[𝒢∂_{U_0}∂_rO[a]], D𝒢(1)[a] = −𝒢(DO(1)[a])𝒢 + (terms linear in DΠ_{U_0}(1)[a], DP_res^{U_0}(1)[a]).
  The O(|r|²) remainders of Prop. U-dec / Lemma U-pair are the forms ½⟨r, Λ_VVr⟩ (of Γ^dr) and ½⟨r, Γ^W_rr r⟩ (of Γ^W).

**Lemma U-loc' ((U-loc) as needed, fixes UP-1/UP-2): PROVEN-HERE** [given upstream PROVEN-HERE: Lemma CT, FP-ab, IT-line,
PG^{(k)}, N5-loc's range counts, NA-FP; F-tree for nothing here]. For every n ≥ 1 there is m_n > 0 such that Dω(1),
Dξ'(1) (fine links → level-n links) and Λ_VV, Γ^W_rr (level-n × level-n) are m_n-local; so are DΦ_0(1) and r_lin. In
particular Lemma U-pair's hypothesis (e) holds for ξ = ω and ξ = ξ', and the O(|r|²) terms of Γ^dr and Γ^W have Hessian
symbols r̂^†Λ̂_VVr̂, r̂^†Γ̂^W_rr r̂ = O(p²)·O(1)·O(p²) = O(p⁴) (r̂ = O(p²), Lemma F-bg / U-pair (2)): no marginal part.
*Proof.* (a) Λ_VV, Dω(1): the second derivatives at (1, 1) of ½log det H_int are ½tr(H_int^{-1}∂²H_int) −
½tr(H_int^{-1}∂H_intH_int^{-1}∂H_int), where ∂H_int[x] = ∇³f(1)[(DU_int*x) ⊕ x, ·, ·]|_{int×int} and ∂²H_int[x, y] =
∇⁴f(1)[X, Y, ·, ·] + ∇³f(1)[D²U_int*(x, y), ·, ·] (X := DU_int*x ⊕ x): local vertex maps by (I1), (I5), contracted with the
local H_int^{-1} ((I2), BL (ii)); local by BL (v). The 𝒩'_1 terms contribute D²(log𝒩'_1∘P∘M̄)(1)[DU*x, DU*y] (the
first-derivative term vanishes by (I1)): local. Dω(1) is a sum of compositions of these with Q^{(n)}: local (BL (i)).
(b) Γ^W_rr, Dξ'(1): ∂_rO, ∂²_rO, ∂_{U_0}∂_rO at (1, 0) are derivatives of order ≤ 4 at the trivial point of the value
function Ψ(U_0; V) = min_{int}f, i.e. (envelope formula) finite sums of contractions of ∇^{≤4}f(1) with derivatives of order
≤ 3 of the intermediate tower: local vertex maps with tails ((I1), (I5)); 𝒢(1) = C_n is local ((I4)); DΠ_{U_0}(1) and
DP_res^{U_0}(1) are local (block-local analytic functions of the background, BL (i)-(iii) for (hh^T)^{-1}, P_res); so both
objects are local by BL (v). (c) DΦ_0(1), r_lin: (I5). m_n is the minimum of the finitely many rates. ∎
*What is not claimed.* Uniformity of m_n in n (not needed: Lemma U-pair concludes β[Q] = 0 at each n). The constants
degrade with n through S_n ≤ nq^{2n}; a uniform version would need the per-level structure (N5-triv's uniform rates) to be
propagated through the chain, which the β-level argument does not use.
**Consequence.** Corollary U-red holds without the hypothesis (U-loc): B_n = −β[Γ^{W0}_n∘Φ_0] − β[Γ^cov_n] is now PROVEN
(given its other inputs: Prop. U-dec at the Laplace level, Lemma U-pair, Lemma F-ren's alias argument with FR-1).
~~Theorem UNIV is conditional on (U-IR) only.~~ **[RFL3-fix S3-1] WRONG as stated, withdrawn.** Theorem UNIV bounds
Σ_{k<n}b_k (the per-step numbers of Def F-g / Prop. F-rem) through B_n, and the identity B_n = Σ_{k<n}b_k is F-tel's second
claim, which by FT-1 (§5.5) needs (SF-bg) at orders 3, 4 at the trivial point. Correct reading: Theorem UNIV is conditional
on (U-IR) and, for B_n = Σb_k (F-tel), on (SF-bg) at orders 3, 4 at the trivial point (or on the FT-1 tower lemma).
Session 4 (§31) addresses the second condition.

## 24. The derivative form of U-cov-IR (target S3-2)

Notation. One colour, fine units, trivial background, ℓ = L^n. Fine momenta q ∈ BZ = [−π, π]⁴; a coarse class P ∈ [−π, π]⁴
(level-n units) has the ℓ⁴ fine aliases q_K = Θ_K/ℓ, Θ_K := P + 2πK, K ∈ {−(ℓ−1)/2, …, (ℓ−1)/2}⁴; K = 0 is the *minimal
alias* (|q_0| = |P|/ℓ); for K ≠ 0, |Θ_K| ≥ π. ŝ_α(q) = e^{iq_α} − 1, ω̂ = |ŝ|² ≥ 4|q|²/π², P_T(q) := 1 − ŝŝ^†/|ŝ|²,
g(q) := P_T(q)/|ŝ(q)|² (the transverse part of the BF-Feynman propagator 1/ω̂), P_⊥(P) the coarse transverse projector,
𝔪̂(q) the composite S4' root-map symbol (fine 1-forms → level-n 1-forms), 𝔪̂_str its straight part (P_⊥𝔪̂ = P_⊥𝔪̂_str, U-cov-IR).

### 24.1 The transverse sector is exact and slice independent
**Lemma U-T⊥: PROVEN-HERE.** Let O^{gi}_n := d*d + Q^{(n)T}𝒞_n^{-1}Q^{(n)} (the gauge-invariant trivial-background
fluctuation form of Γ^{W0}_n) and let C_n be the covariance of the slice-fixed Gaussian δ(h^{(n)}(A))e^{−½||P_resd*A||²}
e^{−½⟨A, O^{gi}_nA⟩}dA (FP-ab's legitimate composite fixing). Let P_T be the orthogonal projector onto co-closed fine 1-forms
(ker d*). Then, ~~on every torus and~~ in infinite volume **and on twisted tori [RFL3-fix S3-5: on an untwisted torus the
class P = 0 contains the alias q = 0, where g(0) is undefined, and the constant 1-forms lie in ker d* and are carried by the
IR term alone; there the q = 0 block is separate, C^⊥ = (Q^TP_⊥(P_⊥𝒞_nP_⊥)^+P_⊥Q)^{-1} on constants, and the alias-block
formula below holds for the remaining entries; this is the same singularity that made f6's (V3) unevaluable]**,
  P_TC_nP_T = C^⊥_n := (P_T[d*d + Q_str^{(n)T}P_⊥(P_⊥𝒞_nP_⊥)^{+}P_⊥Q_str^{(n)}]P_T |_{ker d*})^{-1}P_T,
and per class, in alias-block form (Woodbury),
  **C^⊥_n(q_a, q_b) = δ_{ab}g(q_a) − ℓ^{-4}Y(q_a)^†Ĥ_n(P)Y(q_b),  Y(q) := 𝔪̂_str(q)g(q),**
where Ĥ_n(P) is the symbol of the level-n tree Hessian H_n (Def F-strip: the linearised chain form of Setting SC, κ_i ≡ κ),
i.e. Ĥ_n = (Ĝ_n|_⊥)^{-1} with Ĝ_n F-tree's transverse tree propagator. In particular the slice does not enter the transverse
sector (failure mode S3-F3 does not occur).
*Proof.* (1) Λ := {λ : λ(c_X) = 0 ∀X} acts freely by A ↦ A + dλ. O^{gi}_n annihilates dΛ (d dλ = 0; Q^{(n)}dλ = d_c ev λ = 0,
root covariance and IT-line (a)); for a co-closed source j, ⟨j, dλ⟩ = ⟨d*j, λ⟩ = 0. So I_j(A) := e^{−½⟨A,O^{gi}_nA⟩ + ⟨j,A⟩}
is Λ-invariant, and integrable on (dΛ)^⊥: a zero mode of O^{gi}_n has dA = 0 and Q^{(n)}A = 0, so A = dμ + c (c constant),
Q^{(n)}A = d_c ev μ + ℓc = 0 forces c = 0 (the coarse mean of d_c ev μ vanishes) and ev μ constant, i.e. A ∈ dΛ. Lemma FP-ab
gives ∫I_jδ(h)e^{−½||P_resd*A||²}dA = const·∫_{(dΛ)^⊥}I_j with a j-independent constant; hence the covariance of ⟨j, A⟩
for co-closed j is the same in both measures. (2) (dΛ)^⊥ = {d*A ∈ Λ^⊥ = span δ_{c_X}} = ker d* ⊕ d𝔐, 𝔐 := Δ^{-1}span{δ_{c_X}}
(mean zero), orthogonally; ev: 𝔐 → (coarse 0-forms)/constants is bijective (if ev μ is constant for μ = Δ^{-1}Σα_Xδ_{c_X},
Σα_X = 0, then ||dμ||² = Σα_Xμ(c_X) = 0). On A = A_T + dμ: ⟨A, O^{gi}_nA⟩ = ||dA_T||² + ⟨Q^{(n)}A_T + d_cν, 𝒞_n^{-1}(·)⟩,
ν := ev μ. Integrating ν (a linear change of variables with constant Jacobian) gives the A_T-marginal precision
||dA_T||² + min_ν⟨X + d_cν, 𝒞_n^{-1}(X + d_cν)⟩, X := Q^{(n)}A_T, and the minimum is ⟨P_⊥X, (P_⊥𝒞_nP_⊥)^+P_⊥X⟩ (the
inverse-compression identity for a positive form); P_⊥Q^{(n)} = P_⊥Q^{(n)}_str (U-cov-IR). (3) Woodbury per class:
(g^{-1} + ℓ^{-4}𝔪̂_str^†(P_⊥𝒞_nP_⊥)^{-1}𝔪̂_str)^{-1} = g − ℓ^{-4}g𝔪̂_str^†(P_⊥𝒞_nP_⊥ + ℓ^{-4}Σ_KP_⊥𝔪̂_strg𝔪̂_str^†P_⊥)^{-1}𝔪̂_strg on
the transverse ranges. The bracket is F-tree's Ĝ_n unrolled: P_⊥𝒞_nP_⊥ is the noise part of the recursion Ĝ_{k+1} =
κ^{-1}P_⊥ + 𝒬(Ĝ_k) (𝒞_n = κ^{-1}(1 + Σ_jA_jA_j^†) with A_j the push-forward through j averaging steps; longitudinal fields
are mapped to longitudinal fields, Q d = d ev, so P_⊥Q_k⋯Q_j = P_⊥Q_kP_TQ_{k−1}P_T⋯Q_j, which is the projected form of
𝒬), and the last term is the push-forward of Ĝ_0 = g. By F-tree's definition Ĝ_n = (Ĥ_n|_⊥)^{-1}, and Ĥ_n = P_⊥Ĥ_nP_⊥ (gauge
invariance of H_n). ∎

### 24.2 Factor bounds (uniform in n)
**Lemma DIR: PROVEN-HERE.** D_ℓ(θ) := ℓ^{-1}Σ_{|m|≤(ℓ−1)/2}e^{iθm}, m_ℓ(θ) := min{1, π/(ℓ|θ|)}. For |θ| ≤ π and j ≥ 0:
|∂^jD_ℓ(θ)| ≤ c_jℓ^jm_ℓ(θ). *Proof.* Always |∂^jD_ℓ| ≤ ((ℓ−1)/2)^j, which covers ℓ|θ| ≤ π. For ℓ|θ| > π use D_ℓ =
sin(ℓθ/2)/(ℓ sin(θ/2)) and Leibniz: |∂^i sin(ℓθ/2)| ≤ (ℓ/2)^i, and |∂^r csc(θ/2)| ≤ c_r|θ|^{-1-r} on 0 < |θ| ≤ π
(csc(θ/2) − 2/θ is analytic on |θ| < 2π); with |θ|^{-1} < ℓ/π each term is ≤ cℓ^{-1}|θ|^{-1}ℓ^j ≤ (c/π)ℓ^jm_ℓ(θ). ∎
**(F1)** ||∂^βg(q)|| ≤ c_β|q|^{-2-|β|} (q ∈ BZ∖0, |β| ≤ 2): g is a product of 1/ω̂ and the degree-0 projector, with
ω̂ ≥ 4|q|²/π².
**(F2)** 𝔪̂_str,μ(q) = e^{iq·v_μ}ℓΠ_αD_ℓ(q_α) with block offsets |v_μ|_∞ ≤ ℓ (the leg sum Σ_{j<ℓ}e^{iq_μj} = e^{iq_μ(ℓ−1)/2}ℓD_ℓ(q_μ),
the transverse average real and centred; the composite straight average is the straight average of side ℓ, U-cov-IR).
By Lemma DIR, ||∂^β𝔪̂_str(q)|| ≤ c_βℓ^{|β|}·ℓΠ_αm_ℓ(q_α), and ℓΠ_αm_ℓ(q_α) ≤ min{ℓ, 2π/|q|} (max_α|q_α| ≥ |q|/2).
Hence, with y(q) := ℓΠ_αm_ℓ(q_α)·π²/(4|q|²) ≥ ||Y(q)||/c: **||∂^βY(q)|| ≤ c_β(ℓ + |q|^{-1})^{|β|}y(q)**.
**(F3) Lemma H-sym: PROVEN-HERE (given N2-exp' (ii) as quoted in N5-loc, PROVEN-HERE upstream).** N5-loc's proof quotes
the infinite-lattice bound |H_n(b, b')| ≤ κMe^{−m'd(b,b')} (H_n = −κ(𝓡_n + 𝓡_n^T)/2, entries of 𝓡_n ≤ Me^{−m'|X|_1}),
uniformly in n. Then for |γ| ≤ 2, P ∈ [−π, π]⁴ and every n: **||∂^γĤ_n(P)|| ≤ A_H|P|^{2−|γ|}** and ||Ĥ_n(P)|| ≤ κ, with
A_H = A_H(κ, M, m') independent of n. *Proof.* Ĥ_n(z) = Σ_xH_n(0, x)e^{iz·x} is analytic on |Im z_α| < m' and bounded by
M_H := 4κM coth⁴(m'/4) on |Im z_α| ≤ m'/2. On real P, Ĥ_n(P) ≥ 0 and Ĥ_n(0) = 0 (L4a-Π with β[𝒯_n] = 1, Lemma F-tree:
Ĥ_n|_⊥ = |ŝ|²P_⊥ + O(P⁴); the longitudinal part vanishes by gauge invariance), so ∇Ĥ_n(0) = 0 (a PSD matrix function
vanishing at 0 has zero gradient there). Taylor's formula with Cauchy's estimate for the second derivatives on polydiscs
of radius m'/4 gives ||Ĥ_n(z)|| ≤ c M_Hm'^{-2}|z|² for |z| ≤ m'/4. For real |P| ≤ m'/8, Cauchy on the polydisc of radius
|P|/2 about P (inside |z| ≤ 2|P| ≤ m'/4) gives ||∂^γĤ_n(P)|| ≤ γ!(2/|P|)^{|γ|}cM_Hm'^{-2}(2|P|)²; for |P| ≥ m'/8, Cauchy on
radius m'/2 gives ||∂^γĤ_n(P)|| ≤ γ!(2/m')^{|γ|}M_H, which is ≤ c'|P|^{2−|γ|} on m'/8 ≤ |P| ≤ 2π. ||Ĥ_n|| ≤ κ: Ĝ_n ≥ κ^{-1}P_⊥
(U-cov-IR). ∎

### 24.3 Lemma U-cov-IR' and the transverse propagator part of (R-a)
**Lemma U-cov-IR' (derivative form; transverse sector): PROVEN-HERE.** Uniformly in n, for |α| ≤ 2:
(i) (diagonal) for q ∈ BZ with |q| ≥ 1/ℓ, D_n(q) := C^⊥_n(q, q) − g(q) obeys
  **||∂^α_qD_n(q)|| ≤ A_αℓ^{-4+|α|}|q|^{-6} = A_α(ℓ|q|)^{-4+|α|}|q|^{-2−|α|}:**
each q-derivative costs ~~exactly~~ **at most [RFL3-fix S3-7: an upper bound]** one factor ℓ (relative to the
undifferentiated correction; failure mode S3-F2 does not occur), and relative to |∂^αg| ~ |q|^{-2−|α|} the correction is ≤ A(ℓ|q|)^{-2} for |α| ≤ 2.
(ii) (all alias entries, at the shifted class) C^⊥_n(q_a + k, q_b + k) − δ_{ab}g(q_a + k) = −ℓ^{-4}Y(q_a + k)^†Ĥ_n(P + ℓk)
Y(q_b + k), with ||∂^β_kY(q + k)|_0|| ≤ c_β(ℓ + |q|^{-1})^{|β|}y(q) and ||∂^γ_k[Ĥ_n(P + ℓk)]_0|| ≤ A_Hℓ^{|γ|}|P|^{2−|γ|}.
*Proof.* (ii) is Lemma U-T⊥ at the class P + ℓk (the aliases of the shifted class are q_a + k) with (F2), (F3); note that
∂_k acts on Ĥ_n through P + ℓk, which is where the factor ℓ per derivative comes from. (i): D_n(q) = −ℓ^{-4}Y(q)^†Ĥ_n(ℓq)Y(q)
(P = ℓq mod 2π, Ĥ_n periodic); by Leibniz, (F2) with |q|^{-1} ≤ ℓ, and |∂^γ_q[Ĥ_n(ℓq)]| ≤ ℓ^{|γ|}sup|∂^γĤ_n| ≤ ℓ^{|γ|}A_H(2π)²
(or κ at γ = 0): ||∂^αD_n|| ≤ cℓ^{-4}ℓ^{|α|}y(q)² ≤ cℓ^{-4+|α|}(2π/|q|)²(π²/(4|q|²))². ∎
*Comparison with the review's suggested form.* UC-1 suggested |∂^α(C_n − g)| ≤ Cκℓ^{-4+|α|}|q|^{-6+|α|}. The proven bound
has |q|^{-6} instead: for |q| < 1 it is weaker by |q|^{-|α|}, and it is the true size (the q-derivative of the oscillating
factor sin(ℓq_α/2) is ℓ times the factor, not |q|^{-1} times). It suffices for (R-a) because of the degree count below.

**Lemma U-res' ((R-a) needed only in integrated form): PROVEN-HERE.** Lemma U-res and its rate form hold with (R-a)
replaced by (R-a_int): ∫_{BZ∩{|q|≥1/ℓ}}|J_ℓ − J_*|d⁴q ≤ π²A. *Proof.* U-res's proof uses (R-a) only to bound the second
piece ∫_{|q|≥1/ℓ}(J_ℓ − J_*) by π²A; the rate form does not use (R-a). ∎ **(U-IR)(a) is restated in this integrated form:
for each part, ∫_{|q|≥1/ℓ}|J^{(a_i)}_n|d⁴q ≤ π²A_i, A_i independent of n.** (Reason: the two-correction terms below carry
integrable singularities at the alias-resonance points q ∈ (2π/ℓ)Z⁴∖0 after two derivatives; a pointwise ℓ^{-2}|q|^{-6}
bound is not available from the factor bounds there [the singularity is an upper-bound feature; whether it is attained is
not decided].)

**Proposition U-a1⊥ (the transverse propagator part of (U-IR)(a)): PROVEN-HERE.** Let J^{(a1⊥)}_n be the J_n-construction
of §18 with J_*'s vertices (Wilson, background-covariant Feynman gauge, trivial background) and every gauge propagator
1/ω̂ replaced by 1/ω̂ + Δ^⊥_n, Δ^⊥_n := C^⊥_n − g (alias-block form, Lemma U-T⊥), minus J_*. Then, uniformly in n:
(1) the part with exactly one Δ^⊥_n obeys the pointwise bound |J^{(a1⊥,1)}_n(q)| ≤ A'ℓ^{-2}|q|^{-6} for |q| ≥ 1/ℓ;
(2) the part with two Δ^⊥_n obeys ∫_{BZ∩{|q|≥1/ℓ}}|J^{(a1⊥,2)}_n|dq ≤ A'' **[RFL3-fix S3-7: read d⁴q here, not §17's
dq = d⁴q/(2π)⁴; with dq the conversion below would be off by (2π)⁴, a constant only]**;
so (R-a_int) holds for J^{(a1⊥)}_n with A_{a1⊥} := A' + A''/π² (the constants depend on N, L, κ, M, m' only).
*Proof.* (0) Structure. J_*'s vertices and 1/ω̂ are diagonal in fine momentum. In the tadpole term ½tr[CV_12] and in a
bubble term with one Δ the alias index closes on Δ itself, so only the diagonal entries D_n(q_a) enter; the bubble with two
Δ's is Σ_{a,b}Δ(q_a, q_b)V_2(q_b)Δ'(q_b, q_a)V_1(q_a), folded to q = q_a (§18 convention (iii)). Vertex envelopes (trivial
background, momenta q and q + k): the one-gluon vertices are O(|q| + |k|) with bounded derivatives (|∂^jV(q)| ≤ c|q|^{1−j},
j ≤ 1; ≤ c for j = 2), the two-gluon vertex is O(1); J_*'s terms are products whose envelopes have total degree −4 (that is
why h has degree −4, Lemma U-Tay). (1) A one-Δ term is a J_* term with one factor ∂^βg (|β| ≤ 2) replaced by ∂^βD_n; by
Lemma U-cov-IR' (i) this multiplies the envelope by ≤ A(ℓ|q|)^{-4+|β|}·|q|^{-2−|β|}/|q|^{-2−|β|} ≤ A(ℓ|q|)^{-2}; the envelope
of the J_* term is ≤ c|q|^{-4}. (2) The class measure: ∫_{BZ}dq Σ_bF(q, q_b) = ∫_{[−π,π]⁴}dP ℓ^{-4}Σ_{a,b}F(q_a, q_b), and the
restriction |q| ≥ 1/ℓ keeps the a with |q_a| ≥ 1/ℓ (a = 0 only if |P| ≥ 1). Each two-Δ term, after −∂_{k_1}∂_{k_2} at k = 0
distributed by Leibniz over Ĥ_n(P), Ĥ_n(P + ℓk), Y(q_a), Y(q_a + k), Y(q_b), Y(q_b + k), V_1, V_2, is bounded by
ℓ^{-8}·(4ℓ(1 + |P|^{-1}))²·min{κ², A_H²|P|⁴}·c y(q_a)²|q_a|·y(q_b)²|q_b|: every k-derivative costs at most 4ℓ(1 + |P|^{-1})
relative to the undifferentiated envelope (on Ĥ_n: ℓ|P|^{-1} by (F3); on Y or V at q_b: ℓ + |q_b|^{-1} ≤ ℓ(1 + 2|P|^{-1}),
since |Θ_b| ≥ |P|/2 for every b; at q_a: ≤ 2ℓ). The alias sums: with m(Θ) := min{1, π/|Θ|} and ℓ|q_K| = |Θ_K|,
  Σ_by(q_b)²|q_b| = (π⁴/16)ℓ⁵Σ_bΠ_αm(Θ_{b,α})²|Θ_b|^{-3} ≤ (π⁴/16)ℓ⁵[|P|^{-3} + π^{-3}(1 + π²/4)⁴]
(the K = 0 term, plus |Θ_K| ≥ π and Σ_{K_α≠0}m(P_α + 2πK_α)² ≤ Σ_{j≠0}(2|j| − 1)^{-2} = π²/4 for K ≠ 0), and the same sum
over the a with |q_a| ≥ 1/ℓ is ≤ (π⁴/16)ℓ⁵[1 + π^{-3}(1 + π²/4)⁴] =: c_Yℓ⁵. Collecting the powers of ℓ (ℓ^{-4}·ℓ^{-8}·ℓ²·ℓ⁵·ℓ⁵ = 1):
  ∫_{|q|≥1/ℓ}|J^{(a1⊥,2)}_n| ≤ c∫_{[−π,π]⁴}dP (1 + |P|^{-1})²min{κ², A_H²|P|⁴}(1 + |P|^{-3}) < ∞,
the integrand being O(|P|^{-1}) at P → 0: integrable in d = 4, and n-independent. ∎
*Reading.* The transverse propagator part (a1⊥) of (U-IR)(a) is discharged, for every n, with the ℓ-cost per derivative
tracked: one-correction terms gain (ℓ|q|)^{-2} pointwise, two-correction terms are O(1) in the integrated norm. The
mechanism is the second-order vanishing of the level-n tree Hessian (Ĥ_n(P) = O(P²), from β[𝒯_n] = 1 and N2-exp''s strip
analyticity), which cancels the minimal-alias singularity g(q_0) ~ ℓ²/|P|².

### 24.4 What the longitudinal and slice parts need (exact statements; OPEN)
On H_0^{(n)} the slice-fixed Gaussian decouples (FP-ab's decomposition, N5-coer (1)): A = A^ph + dλ, λ ∈ Λ_res,
A^ph ∈ Phys^{(n)} = {h^{(n)}(A) = 0, d*A ∈ span(δ_{c_X}, 1_{B(X)})}, with form ||dA^ph||² + ⟨Q^{(n)}A^ph, 𝒞_n^{-1}Q^{(n)}A^ph⟩ +
||P_resΔ_0λ||². So C_n = C_n^{ph} ⊕ dT^{-2}d* (T := P_resΔ_0|_{Λ_res}), and C_n^{ph} = C^⊥_n + (the entries involving the
longitudinal part of A^ph: the coarse-gauge modes dμ, μ ∈ Δ^{-1}span(δ_{c_X}), and the block-mean modes, μ ∈ Δ^{-1}span(1_{B(X)})
cut by h^{(n)} = 0). Against J_*'s longitudinal propagator dΔ^{-2}d* (BF-Feynman) and its ghost determinant, (U-IR)(a)
needs, each in the integrated form (R-a_int) with n-independent constants:
- **(a3) residual-group part:** the diagrams of J_* with dΔ^{-2}d* replaced by dT^{-2}d* (Dirichlet at the level-n centres
  and zero block means, i.e. two block-local constraints per level-n block), together with −log Δ_FP of the composite slice
  against the BF ghost determinant −log det(−D²): ∫_{|q|≥1/ℓ}|J^{(a3)}_n| ≤ π²A_3. **[RFL6-fix S6-1] RETIRED (superseded by
  Lemma GH, §43, and Lemma FP-exact, §52: (a3) ≡ 0 at critical backgrounds; the ghost is G_gh, Proposition GH-log).**
- **(a4) coarse-gauge and block-mean modes and the cross covariance:** the diagrams of J_* with the longitudinal entries
  of C_n^{ph} (P_LC_n^{ph}P_L and P_TC_n^{ph}P_L) in place of the corresponding BF-Feynman entries:
  ∫_{|q|≥1/ℓ}|J^{(a4)}_n| ≤ π²A_4.
- **Structure available for both [inference, not proven]:** every one of these modifications is a block-local, finite-rank
  per class (≤ 2 per level-n block) constraint at scale ℓ, so each has the alias-block form −ℓ^{-4}Z^†(coarse symbol)Z of
  Lemma U-T⊥, with Z built from the block symbols of δ_{c_X} and 1_{B(X)}. The 1_{B(X)} symbol has the Dirichlet decay of
  (F2), so its part should follow the proof of Proposition U-a1⊥ verbatim; the δ_{c_X} symbol is FLAT across aliases (no
  Dirichlet decay), so its part needs a different mechanism: the 4D lattice Green's function at coinciding points is finite,
  which makes the point-constraint correction ~ℓ^{-4}g(q)g(q')/G(0), i.e. relative O(ℓ^{-4}|q|^{-2}) ≤ O((ℓ|q|)^{-2}ℓ^{-2}),
  but its derivative bounds and alias sums are not written. Also needed (not in (a)): (R-b) and (U-IR)(c), unchanged.

## 25. One-step comparison with an explicit e^{aR} factor (lead's K4 note; for HIST's g_k ≤ g_{k+1})

**Lemma F-mono: PROVEN-HERE (arithmetic; given the hypotheses of Theorem F-flow).** Along the chain's own sequence, if
g_0, …, g_k ∈ (0, γ] (γ as in Theorem F-flow), then
  (i) u_k − u_{k+1} ≥ β_- log L − R ≥ −R  (Theorem F-flow with (j, n) = (k, k + 1); R = 2R_0);
  (ii) hence g_k² ≤ g_{k+1}²/(1 − Rg_{k+1}²) ≤ 2g_{k+1}² whenever g_{k+1}² ≤ 1/(2R), and for every a > 0
       e^{−a/g_k²} ≤ e^{aR}e^{−a/g_{k+1}²},  and  ~~g_k^{-p} ≤ (g_{k+1}^{-2} + R)^{p/2}~~;
       **[RFL3-fix S3-2] the struck clause has its indices swapped and is WRONG as stated (it would say u_k − u_{k+1} ≤ R,
       which the lower half of (F_R) does not give; generically u_k − u_{k+1} ≈ β_0^std log L). Correct clauses, for p > 0:
       g_{k+1}^{-p} ≤ (g_k^{-2} + R)^{p/2} = g_k^{-p}(1 + Rg_k²)^{p/2}  (from (i): 1/g_{k+1}² ≤ 1/g_k² + R  (⋆)),
       and, if the other direction is wanted, g_k^{-p} ≤ (g_{k+1}^{-2} + β_+ log L + R)^{p/2}  (upper half of (F_R) at
       (k, k + 1)).**
  (iii) exact monotonicity u_k ≥ u_{k+1} (i.e. g_k ≤ g_{k+1}) holds at every level with b_k > C_ργ² (u_k − u_{k+1} = b_k + ρ_k
       ≥ b_k − C_ργ²); it is NOT implied by (F_R) in general (REVIEW RN-1), and its availability for all k ≥ k_0 rests on
       Corollary UNIV-rate, which is a GAP (§19).
*Proof.* (i) is the lower half of (F_R) at n − j = 1 and β_- > 0. (ii): 1/g_k² ≥ 1/g_{k+1}² − R; invert; exponentiate. (iii) is
Proposition F-rem. ∎
*Reading for HIST (CL^J, RS-lin, Theorem H-pos^J; K4).* Wherever g_k ≤ g_{k+1} is used only to compare e^{−a/g_k²} with
e^{−a/g_{k+1}²} or g_k^{-p} with g_{k+1}^{-p}, (ii) replaces it at the price e^{aR} (resp. ~~(1 + Rg_{k+1}²)^{p/2}~~ **[RFL4-fix S4-1] (1 + Rg_k²)^{p/2}**). Where it is used
as g_k ≤ min{1, √κ} from g_{k+1} ≤ min{1, √κ}, (ii) gives g_k ≤ √2·min{1, √κ} for g_{k+1}² ≤ 1/(2R), i.e. the threshold must be
taken smaller by √2 **[RFL4-fix S4-1] (needed only where g_k ≤ γ is not already assumed: F-mono's own hypothesis is g_0, …, g_k ≤ γ, so if γ ≤ min{1, √κ} it gives g_k ≤ min{1, √κ} directly and the √2 loss is unnecessary; which case HIST is in depends on HIST's γ, not checked here)**. ~~Whether HIST's uses are only of these kinds is for HIST's owner to confirm (not checked here).~~
**[RFL3-fix S3-2] Replaced by the use list.** HIST uses g_k ≤ g_{k+1} only in Proposition CL^J; H-pos^J and R1^J inherit it
through CL^J. HIST lines as read in session 4 (grep of g_{k+1}, read-only):

| # | HIST line | use (quoted in short) | inequality needed | covered by corrected F-mono? |
|---|---|---|---|---|
| H1 | l.235, CL^J (c) | "e c_N^{-1}(κ/g_{k+1}²)^{N²-1} ≤ e c_N^{-1}(κ/g_k²)^{N²-1} ((3.1); g_k ≤ g_{k+1})" | 1/g_{k+1}² ≤ C/g_k² | **COVERED** by the corrected clause with p = 2(N² − 1): factor (1 + Rg_k²)^{N²-1} ≤ 2^{N²-1} for g_k² ≤ 1/R, per factor; ≤ 8\|Y\| factors, so ≤ 2^{8(N²-1)} per cube, into C_J |
| H2 | l.244-247, CL^J (c) (iii) | exponent (κ/g_{k+1}²)·(3/2)[…] ≤ (3κ/2)[(1 + A_d)²ε°²/g_k² + p_L²r²] "(g_k ≤ g_{k+1})" | 1/g_{k+1}² ≤ 1/g_k² + R | **COVERED** by (⋆) (the exponential clause): an extra factor exp(−12κR[(1 + A_d)²(ε^J_loc)² + p_L²r²]) per cube (the reviewer's count), into C_J; a_J unchanged |
| H3 | l.253-254, CL^J (d) | "(1/g_{k+1}² ≤ 1/g_k²); U_{k+2}(c') enters one factor, ≤ κ/g_{k+1}²" | 1/g_{k+1}² ≤ C/g_k² | **COVERED** by the corrected clause with p = 2: κ/g_{k+1}² ≤ (1 + Rg_k²)κ/g_k² ≤ (1 + R)κ/g_k² for g_k ≤ 1, i.e. Λ^J_1 → (1 + R)Λ^J_1. **Not in the lead's K4 list; flagged for HIST's owner (FLOW_LOG)** |
| H4 | l.190 (Setting), l.349, l.767 | "g_k ≤ g_{k+1} ≤ min{1, √κ}" as a threshold for g_k | g_k ≤ min{1, √κ} from g_{k+1} ≤ … | **COVERED** by clause 1 of (ii): g_k ≤ √2 g_{k+1} for g_{k+1}² ≤ 1/(2R), so the Setting must read g_{k+1} ≤ min{1, √κ}/√2. **[RFL4-fix S4-1] If F-mono is applied with γ ≤ min{1, √κ}, its hypothesis g_k ≤ γ already gives g_k ≤ min{1, √κ} and no √2 is lost; the √2 form is for the case γ > min{1, √κ}** |
| H5 | l.349, H-pos^J (i) | constants "independent of k, K, T and g" | — | **COVERED**: after H1-H3 the constants depend on R as well, and stay independent of k, K, T and g |

So with the corrected clause all five uses are covered; under the uncorrected (struck) clause H1 and H3 were not. What
HIST's owner must still do (not done here; HIST is read-only for this lane): restate CL^J's Setting as "g_{k+1}^{-2} ≤
g_k^{-2} + R, g_k, g_{k+1} ≤ min{1, √κ}/√2" and carry the R-dependence of C_J and Λ^J_1. **[RFL3-fix tally] Lemma F-mono is
arithmetic on Theorem F-flow and is not counted separately (as for F-ll and F-R).**

## 26. f6 outcomes (ADDED AFTER the run; checks/f6_criteria.md, f6_iter_chain.py, f6_out.txt, f6_time.txt)
Run 02:08-02:44 UTC, 2170 s, peak 389 MB, NUMERIC LOCK, nice 10, 1 thread. Criteria written 01:18:41 UTC before the script
(stat in FLOW_LOG); two POST-HOC lines (V2', V3') added after a smoke test and before the official run, logged.
- **Validation.** (V1) PASS (A = 0 identity to 1.5e-16). **(V2) FAIL as pre-registered** (per-class total 1.2e-4; M-only
  1.8e-16): the per-class comparison was the wrong criterion: the joint (φ_0, φ_1) form and f5's integrated-out form assign
  the kernel terms that pass through the level-1 coordinate of class P − k1 to different classes (a class-shift term).
  (V2' POST-HOC) class sums on a shift-closed twisted torus: 8.6e-18. **(V3) NOT EVALUATED** (the untwisted torus has the
  q = 0 alias, where the class formula on 1/ω is singular); (V3' POST-HOC, twisted torus) Ward identity 1.5e-12 and 3.1e-12
  against scales 1.7e2, 4.0e2 (M-only alone violates it at ~1%). (V4) PASS 2.5e-14. (V5) PASS. (Q6) PASS 1.8e-5. (V1b) PASS
  1.0e-10.
- **Falsification lines: (G6) FAIL, (H6) FAIL, (C6) FAIL; (G6') NOT EVALUATED** (rule: projected ℓ = 21 time 6872 s > 3000 s).
  Slopes × 48π² over (9, 15), κ_c = 0.25 / 1 / 4: s_it^K = +0.0695 / +0.0691 / +0.0689; s^Δ = +0.0698 / +0.0691 / +0.0672;
  s^cov = +0.0701 (κ-independent). Totals: s_it = 1.069 / 1.066 / 1.061, single s_s = 0.999 / 0.997 / 0.994.
  Values: c^cov(9) = −1.3717e-4, c^cov(15) = −6.154e-5 (all κ_c); Δ^K(9) = −1.3656e-4, −1.3522e-4, −1.3192e-4; Δ^K(15) =
  −6.128e-5, −6.073e-5, −5.952e-5.
- **Per the pre-stated reading rule: the FAILs stand; f6 cannot separate a log from a transient with two ℓ values, and
  failure mode S3-F4 is NOT declared observed (G6' not evaluated).** POST-HOC reading, labelled: (i) the whole failing
  slope sits in the composite-covariance term c^cov (Γ^cov's scalar instance): Δ^K − c^cov = +6.2e-7, +1.95e-6, +5.2e-6 at
  ℓ = 9 and +2.6e-7, +8.1e-7, +2.0e-6 at ℓ = 15, i.e. the composite-path kernel vertices of the Γ^{W0} part change the
  single-block kernel-vertex part by ≤ 5e-6, with slope |·|×48π² ≤ 3e-3 (κ_c = 4) — inside the (G6) threshold; (ii) c^cov
  is shrinking in magnitude (−1.37e-4 → −6.15e-5; a power fit through two points gives |c^cov| ∝ L_2^{-1.6}), as the
  criteria anticipated for an O(L_2^{-2})-type transient in this (3, L_2) family, where the level-1 noise share of the
  composite covariance is 9/(9 + ℓ²); a log would make |c^cov| grow; but two points do not prove convergence. (iii) So f6
  neither falsifies nor supports (U-IR)(c) at the β-coefficient level; it does indicate that the kernel-vertex part of the
  scalar Γ^{W0} instance with composite paths stays at the single-block value. Next discriminating run: ℓ = 21 (needs a
  ~5× faster iterated algebra) or a three-level chain at fixed L = 3 for Γ^cov alone (level-1 algebra only, cheap).
- **[RFL3-fix S3-3] The criteria design was flawed, and ℓ = 21 must not be run under the original rule.** REVIEW_FLOW_S3 §6.2
  gives c^cov exactly, c^cov(L_2) = −(L_2² − 1)²/(576L_2⁴(L_2² + 1)): zero log coefficient, but finite-difference slopes
  s^cov(9, 15)·48π² = 0.0701 and s^cov(15, 21)·48π² = 0.0397. So the pre-registered (G6') would have FAILED at ℓ = 21 and, by
  the reading rule, would have declared S3-F4 OBSERVED for a term that provably has no log (a false positive); (C6) and
  (G6') could not PASS before ℓ ≈ 57. Post-hoc reading (ii) above is confirmed and sharpened. A labelled POST-HOC amendment
  A1 was appended to f6_criteria.md (session 4) and evaluated on the stored values (§32): the closed form matches f6's
  c^cov to the printed digits, and the residual parts c^K − c^cov, Δ^K − c^cov have |slope(9, 15)|·48π² ≤ 0.0030.

## 27. Session-3 outcomes against §22 (ADDED AFTER the derivations and checks)
- **Step 1 (fixes): DONE.** Every binding fix of REVIEW_FLOW_S1_S2 applied in place and tagged [RFL-fix] (FS-1, FI-1,
  FI-2/B6, UC-1, J_n definition, (a1)-(a4) split, (U-IR-s) restated with (s2) for Γ^cov, UNIV-rate marked GAP with a repaired
  arithmetic, UP-1, UP-2, FT-1, FR-1, FRR-1, FRR-2, RN-1 (incl. RLARGE §7.2 (iv) and PLD-fin l.194, new PLD row), RN-2, UT-1,
  UT-2, FR-2, CK-1 (FLOW_LOG appended correction; f1 provenance NOT VERIFIABLE, §12), CK-2, UR-1, UR-2, FN-1, normalisation
  wording, §3.1 per HIST Lemma HF). **[RFL3-fix S3-4] Overstated: FN-1 was only partly applied in session 3 (the l.577
  and §19A LF-count pointers and the l.566 L4b pointer were left stale); completed in session 4 against the current PROOF
  bytes (FLOW_LOG 03:38 UTC).** **FR-2 was first applied in the wrong direction and then corrected on the lead's K1
  note** (§4: the large-field shift LOWERS u; the original (SF-g) sign was right; F-rem's proof and §6.1 (d) annotated).
- **S3-1 (U-loc): PROVEN** as Lemma U-loc' (§23), at each n, with the O(r²) remainders and an explicit ξ' (slice and FP enter
  only through the slice-fixed covariance); not uniform in n (not needed). Corollary U-red is now unconditional on (U-loc).
  S3-F1 does not occur (gaps: intermediate Hessian ≥ κ/((n − 1)S_n), 𝒞_n^{-1} ≥ κ/S_n, composite-slice operator by PG^{(k)}).
- **S3-2 (derivative form): PROVEN for the transverse sector** (§24): the transverse sector is exact and slice independent
  (Lemma U-T⊥; S3-F3 does not occur); each q-derivative of C_n − g costs ~~exactly~~ at most [RFL3-fix S3-7] one factor ℓ (Lemma U-cov-IR'; S3-F2 does
  not occur), the true bound being ℓ^{-4+|α|}|q|^{-6}, not the review's suggested ℓ^{-4+|α|}|q|^{-6+|α|}; (R-a) is needed only
  in integrated form (Lemma U-res'), and the transverse propagator part (a1⊥) of (U-IR)(a) holds in that form uniformly in n
  (Proposition U-a1⊥; mechanism: Ĥ_n(P) = O(P²) uniformly in n). The longitudinal/slice parts (a3), (a4) are stated exactly
  (§24.4, OPEN), with the flat δ_{c_X} symbol named as the piece that needs a different mechanism.
- **S3-3 (f6): run; the three falsification lines FAIL; S3-F4 not declared** (§26; G6' not evaluated); the failing slope is
  entirely in the composite-covariance term, whose magnitude is decreasing.
- **Lead's K1/K4: K1 CORRECTED (sign re-derived), K4 SUPPLIED (Lemma F-mono, e^{aR} factor).**
- ~~**Theorem UNIV is now conditional on (U-IR) alone**~~ **[RFL3-fix S3-1] withdrawn: Theorem UNIV is conditional on
  (U-IR) and, for B_n = Σb_k (F-tel), on (SF-bg) at orders 3, 4 at the trivial point (FT-1), as the tally below already
  says**, with (U-IR)(a) in integrated form and its part (a1⊥) discharged;
  open: ~~(a1) longitudinal entries,~~ **[RFL3-fix S3-6: merged into (a4)]** (a2) IR-term vertices, (a3), (a4), (b), (c),
  and (U-IR-s) for the rate.

## 28. Tally after session 3 (FLOW.md items; session-3 items unreviewed)
- **PROVEN-HERE: 20 (sessions 1-2, as corrected by the review) + 6 (session 3) = 26.** Session 3: Lemma U-loc' (with Lemma
  BL counted with it), Lemma U-T⊥, Lemma U-cov-IR' (with Lemmas DIR, H-sym counted with it), Lemma U-res', Proposition U-a1⊥,
  Lemma F-mono (arithmetic). Each conditional exactly as labelled; upstream PROVEN-HERE inputs used: Lemma CT, FP-ab,
  IT-line, PG^{(k)}, N5-loc's counts and N2-exp' (ii) as quoted there, NA-FP, F-tree.
  **[RFL3-fix tally] Corrected by REVIEW_FLOW_S3: 24 PROVEN-HERE, not 26** (20 from sessions 1-2 + 4 from session 3: Lemma
  U-loc' with BL, Lemma U-T⊥ with fix S3-5, Lemma U-cov-IR' with DIR and H-sym, Proposition U-a1⊥). Not counted: Lemma
  U-res' (a one-line remark on Lemma U-res) and Lemma F-mono (arithmetic on Theorem F-flow, as F-ll and F-R; and it needed
  fix S3-2). WRONG as stated: Lemma F-split (unchanged) and the session-3 sentence "Theorem UNIV conditional on (U-IR) only"
  (S3-1). Current tally: the session-4 tally section.
- **GAP:** Corollary UNIV-rate (session-2 proof; a repaired arithmetic given the restated (U-IR-s), not counted).
- **WRONG as stated, superseded:** Lemma F-split (by Prop. U-dec).
- **IMPORTED-AND-REVERIFIED:** L4b — 1.
- **OPEN:** (U-IR) [(a1) longitudinal, (a2), (a3), (a4): s-P; (b), (c)]; (U-IR-s) [s-P]; finite-order locality of the tower at
  1 (FT-1, or keep (SF-bg) for the per-step b_k) [s]; the RLARGE requirement FI-1 (per-level (RLF-δ)_k, (SF-g)_k from (F_R) on
  [0, k] along the chain's own sequence) [cross-lane].
- **HYPOTHESES consumed (layer 1):** (SF-g), (RLF-δ), (SF-cont), (SF-∞); (SF-bg) at orders 3, 4 for the per-step b_k (FT-1).
- **Checks:** f6 (V2 FAIL as pre-registered, V3 NOT EVALUATED, two post-hoc lines; G6/H6/C6 FAIL, G6' NOT EVALUATED).

---
# Session 4 of lane C (opened 2026-10-28 03:30 UTC)

## 29. Session-4 targets (pre-stated 2026-10-28 03:40 UTC, before any session-4 derivation, criteria file or script)

Binding input: REVIEW_FLOW_S3.md. Its fixes S3-1..S3-7 are applied in place and tagged **[RFL3-fix]** (step 1); text of
sessions 1-3 is otherwise unchanged. Outcomes are in a later section, added afterwards.

**Target S4-2 ((U-IR)(c) and (s2): the composite-covariance determinant).** Prove |β[Γ^cov_n]| ≤ A_cov for all n and
|β[Γ^cov_n] − c_cov| ≤ A_sθ^n with θ < 1, using the per-block structure of the composite covariance. Pre-stated route:
(1) a structural lemma: at the point V = 𝔪(U_0) where 𝒞_n(U_0) is defined (Prop. U-dec (i)) every kernel term sits at its
zero, so the joint Hessian has no (residual) × (second derivative) terms, and 𝒞_n(U_0) is the marginal covariance of a
linear Gaussian chain whose maps and weights are evaluated at the tree composites; (2) the scalar U(1) instance of the
uniform chain (fixed L, levels 1..n, f6's covariant averages): 𝒞_n is diagonal on level-n sites, so β[Γ^cov_n] is a
single-block sum, to be computed in closed form for all n; (3) SU(N): reduce β to a Cartan (abelian) background and state
exactly what remains. The reviewer's prediction (convergence to c_cov ≠ 0 at an L^{-2}-geometric rate) is NOT assumed.
Check f7 (criteria file first; its stat into FLOW_LOG before the script): the uniform L = 3 scalar chain, n = 1..4, by
explicit fine-link path sums, against the closed form.
**Target S4-3 (FT-1).** Prove that the trivial-point Taylor data that F-tel's identity B_n = Σ_{k<n}b_k uses (the
derivatives of order ≤ 4 of 𝒯_k at 1 and of order ≤ 2 of the one-step towers Φ_{k←k+1}) are local at each k, so that the
per-step Γ_k has an exponentially local Hessian and Lemma F-ren applies without (SF-bg). Pre-stated route: §23 (I5)'s
implicit-function argument on the free-endpoint one-step problem, with the slice-fixed one-step inverse of Theorem N5-triv
(PROOF l.5181) and induction on k.

**Failure modes (each a valid outcome).** (S4-F1) in the scalar instance β[Γ^cov_n] grows with n or does not converge;
(S4-F2) the structural lemma fails (curvature terms survive at V = 𝔪(U_0)); (S4-F3) for SU(N) the composite covariance
has a non-contracting sector (noise that is not damped by L^{-2} per step) whose background dependence enters β at
second order, so that the scalar argument does not transfer; (S4-F4) the free-endpoint one-step problem has a gauge
degeneracy that the slice does not remove with a local inverse, or the induction loses locality.

---
# Session-4 derivations (written after §29)

## 30. The composite-covariance determinant (target S4-2)

Notation as in §23: n ≥ 1, ℓ = L^n, normalised exponential coordinates about each link value, one colour where a colour
is named. 𝔪_k(U_0) := the composite of k polar averages (𝔪_0 = id, 𝔪_{k+1} = W_♮∘M̄∘𝔪_k), where W_♮(M) is the zero of the
level's tree exponent in V: W_♮ = W (the polar part) for N = 2, and for N ≥ 3 the SU(N) maximiser W_0 of Re tr(V^{-1}M)
(HIST Lemma HF (i), read via §3.1's fix: k̃(V, M) = φ_M(V) + d(M), φ_M ≥ 0 with φ_M(W_0) = 0, d(M) independent of V).
W_♮ is analytic near M = 1 by the implicit function theorem (V ↦ Re tr(V^{-1}M) has a nondegenerate maximum on SU(N) at
V = 1 for M = 1: its Hessian there is −N^{-1}Re tr(Y²) = N^{-1}tr(Y^†Y) > 0). Let h(Z; M) := the level's tree exponent at
V = W_♮(M)e^{−Z} minus its minimum: h ≥ 0, h(0; M) = 0 and ∂_Zh(0; M) = 0 for all M near 1, and Π(M) := ∂²_Zh(0; M), a positive
form on su(N) (Π(1) = the metric of §0), analytic in M.

**Lemma COV-str (the composite covariance at the Laplace level): PROVEN-HERE.** For U_0 near 1 put B_k := 𝔪_k(U_0),
T_k := D(W_♮∘M̄)(B_k) (level-k tangent → level-(k+1) tangent, in the frames of B_k and B_{k+1}), and Π_{k+1} := ⊕_cΠ(M̄_c(B_k))
on level-(k+1) links. Then:
(i) the Hessian of f := κΣ_{k<n}Σ_ch(·) in (X_1, …, X_n) (U_k = B_ke^{X_k}, U_0 fixed, U_n = V) at X = 0 is exactly
  Σ_{k=0}^{n−1}κ⟨X_{k+1} − T_kX_k, Π_{k+1}(X_{k+1} − T_kX_k)⟩,  X_0 := 0;
no (tree residual) × (second derivative of the averaging map) term survives;
(ii) 𝒞_n(U_0) = κ^{-1}Σ_{j=1}^nA_jΠ_j^{-1}A_j^T with A_j := T_{n−1}⋯T_j (A_n := 1);
(iii) A_jΠ_j^{-1}A_j^T has finite range ≤ 2r_1L/(L − 1) in level-n units, r_1 := p_L/L + 1, for every j ≤ n, every n and every
U_0 near 1; in particular 𝒞_n(U_0) has finite range, uniformly in n;
(iv) (no n-uniform gap) at U_0 = 1, for every level-n site x and v := d_nδ_x (level-n units, one colour),
  ⟨v, 𝒞_nv⟩ ≥ (n/κ)||v||²,
so 𝒞_n^{-1} ≥ κ/S_n ((I3)) cannot be improved to an n-independent gap: the coarse-gauge directions carry a share of the
noise of every level that is not damped by the averaging.
*Proof.* (i) Each term is g_c(X) := h(Z_c(X); M̄_c(B_ke^{X_k})) with Z_c(X) defined by B_{k+1,c}e^{X_{k+1,c}} =
W_♮(M̄_c(B_ke^{X_k}))e^{−Z_c}; Z_c(0) = 0 because B_{k+1} = W_♮∘M̄(B_k), and DZ_c(0)X = −(X_{k+1} − T_kX_k)_c up to the sign
convention. Write g_c = h̃(Z, M). Since h̃(0; M) = 0 and ∂_Zh̃(0; M) = 0 for every M, all M-derivatives of h̃ and of ∂_Zh̃ vanish
at Z = 0; so in the second-order chain rule the terms ∂_Mh̃, ∂²_Mh̃, ∂_Z∂_Mh̃ and ∂_Zh̃·D²Z vanish, leaving
∂²_Zh̃(0; M̄_c(B_k))[DZ_c, DZ_c]. Sum over c and k. **[RFL4-fix S4-2a] Scope: f contains only h = k̃ − d. For N ≥ 3 the V-independent terms κd(M̄_c(U_k)) are also part of the order-u intermediate exponent; at a background near 1 their Hessian is O(|background|⁴) (d = O(y⁶), §3.1), so they do not touch the F² coefficient; they are not part of the chain form (i).** (ii) The form (i) is twice the negative log density of the linear Gaussian
chain X_{k+1} = T_kX_k + η_{k+1}, η_{k+1} ~ N(0, (κΠ_{k+1})^{-1}) independent, X_0 = 0 (Π_{k+1} > 0 near 1). Its Schur complement
onto X_n is the inverse of the covariance of X_n = Σ_jA_jη_j, and by Prop. U-dec (i) and the envelope identity of its proof,
Hess_VΨ(U_0; ·) at its minimiser V = 𝔪_n(U_0) is that Schur complement (the joint minimum over the intermediates at
V = 𝔪_n(U_0) is X = 0, where every h vanishes). So 𝒞_n = κ^{-1}Σ_jA_jΠ_j^{-1}A_j^T. (iii) T_k(c, b) ≠ 0 only if b lies in the
contour support of c, which spans two adjacent level-(k+1) blocks (N5-loc: range ≤ p_L in level-k units), so the base points
are within r_1 in level-(k+1) units; a chain of A_j moves ≤ Σ_{k=j}^{n−1}r_1L^{k+1−n} ≤ r_1L/(L − 1) in level-n units, and
A_jΠ_j^{-1}A_j^T doubles this (Π_j is block diagonal per link). This holds at every U_0 near 1, because T_k is the derivative
of a function of the links in the contour supports. **[RFL4-fix S4-2b] "Every U_0 near 1" is not an n-uniform neighbourhood: for a constant-F background the level-k curvature in level units is ≈ L^{2k}F, so B_k stays in W_♮'s analyticity domain for all k < n only for U_0 in a neighbourhood 𝒰_n of 1 that shrinks like |F| ≲ L^{-2n} in curvature. Read (i)-(iii) for U_0 ∈ 𝒰_n. This is harmless for β (a second derivative at F = 0 at each n); it matters for any non-perturbative use.** (iv) At U_0 = 1, T_k = Q_k (the S4' root map, level units), Π_j = 1, and
Q_kd_k = d_{k+1}ev_k (root covariance, LINEAR_PACKAGE §1.2, as used in Lemma F-tree; ev = evaluation at the block centres).
For odd L the level-n sites are sites of every level j, so ev^{(n−j)}δ_x^{(j)} = δ_x^{(n)} and A_ju = v for u := d_jδ_x^{(j)};
||u||² = ||v||² = 8 (2d links at x, values ±1). Cauchy-Schwarz: ⟨v, A_jA_j^Tv⟩ = ||A_j^Tv||² ≥ ⟨A_j^Tv, u⟩²/||u||² =
⟨v, A_ju⟩²/||u||² = ||v||². Sum over j = 1, …, n. ∎
*Reading.* (i)-(iii) answer the reviewer's open point (REVIEW_FLOW_S3 §9: "whether they keep the range finite"): at the
point V = 𝔪_n(U_0) where 𝒞_n is defined the background enters only through the linearised maps and the weights at the tree
composites, and the range stays finite at every background near 1 **[RFL5-fix S5-1: read "at every U_0 ∈ 𝒰_n", the
n-dependent neighbourhood of fix S4-2b]**. ~~(iv) is new and is a partial observation of failure mode
S4-F3: the gauge chain HAS a non-contracting sector (the pure-gauge noise, which the root covariance transports without
loss). Whether its background dependence enters β[Γ^cov_n] at second order is not decided here (below).~~
**[RFL4-fix S4-4] Corrected reading: (iv) is a true statement about 𝒞_n on the coarse-gauge directions G_n := D_{B_n}Λ_n,
and it is NOT an obstruction to UNIV. G_n is exactly the sector that cancels between Γ^{W0}_n and Γ^cov_n in B_n: the
coarse-gauge directions of the fine field (ev λ ≠ 0, not gauge-fixed by any slice) are zero modes of the Wilson Hessian
that carry only the IR term, and integrating them out removes 𝒞_n's G_n block exactly (Lemma COV-GI, §36). After that,
B_n depends on 𝒞_n only through P_⊥𝒞_nP_⊥, where the noise is damped (Proposition COV-⊥-C, §37). "S4-F3's first half
is observed" is withdrawn as a reading for B_n; it stays true as a statement about 𝒞_n alone.**

**Proposition COV-sc ((U-IR)(c) and (s2) in the scalar U(1) instance of the uniform chain, in closed form):
PROVEN-HERE.** Setting (f6's averages, extended to n levels; uniform κ in level units): fine Z⁴, complex unit-charge
scalar, U(1) background A on fine links; level-k sites L^kZ⁴ (odd L, nested centres); for k = 0, …, n − 1,
  (Q_k^Aφ_k)(y') := L^{-4}Σ_{y∈B_{k+1}(y')}(1/24)Σ_σexp(i∫_{σ: y→y'}A)φ_k(y),
σ the 24 coordinate orders of the axial path from y to y', run on fine links; the chain form
Σ_{k=0}^{n−1}κ_{k+1}Σ_{y'}|φ_{k+1}(y') − (Q_k^Aφ_k)(y')|² with κ_j := sL^{2j} (s > 0; f6's κ_1 = 9s at L = 3), φ_0 given;
Γ^cov_n(A) := log det 𝒞_n(A) (complex fields), 𝒞_n(A) := Σ_{j=1}^nκ_j^{-1}A_jA_j^† (A_j := Q_{n−1}^A⋯Q_j^A, A_n = 1; the
scalar form of Lemma COV-str (ii), where the averages are linear in φ, so (ii) is exact). Let c^cov_n be the coefficient of
F_{12}² per fine site in Γ^cov_n for a constant field strength F_{12} (one plane; f5/f6's c = β/2). Then for every n ≥ 1:
  **c^cov_n = c_∞[1 − L^{-2(n−1)}(1 + L^{-2n})/(1 + L^{-2})],   c_∞ := −(L² − 1)/(576(L⁴ + L² + 1)),**
independent of s. Hence, with θ := L^{-2}:
  **|c^cov_n| ≤ |c_∞| =: A_cov  and  |c^cov_n − c_∞| ≤ |c_∞|L^{-2(n−1)} = A_sθ^n,  A_s := L²|c_∞|;**
c^cov_n increases strictly in magnitude to c_∞ ≠ 0; c^cov_1 = 0. At L = 3: c_∞ = −1/6552 = −1.526252e-4, c^cov_2 =
−1.371742e-4 (= f6's ℓ = 9 value −0.00013717; at L = 3, n = 2 f6's chain IS this chain), c^cov_3 = −1.509270e-4, c^cov_4 =
−1.524367e-4.
*Proof.* (1) Diagonality (the per-block structure). Each level-k site has exactly one parent, so Q_k^A(y', y) ≠ 0 only for
y ∈ B_{k+1}(y'), and A_j(c, y) = Π_{k=j}^{n−1}Q_k^A(y_{k+1}, y_k) along the unique ancestor chain y = y_j → y_{j+1} → … → y_n = c,
or 0 if c is not the level-n ancestor of y. Hence A_jA_j^† is diagonal on level-n sites and
  𝒞_n(A)(c, c) = Σ_{j=1}^nκ_j^{-1}Σ_{y_j∈B(c)}Π_{k=j}^{n−1}L^{-8}|w_k(y_k)|²,  w_k(y_k) := (1/24)Σ_σexp(i∫_{σ: y_k→y_{k+1}}A),
so Γ^cov_n(A) = Σ_clog 𝒞_n(A)(c, c): a sum of single-block functions (exact, every A). (2) Constant F_{12} (gauge A_2(x) = F x_1
on links in direction 2, A_μ = 0 otherwise; |w_k| is gauge invariant). Along an axial path from y to y + d the phase is
F d_2·x_1(σ), with x_1(σ) = y_1 + d_1 if direction 1 precedes direction 2 in σ and x_1(σ) = y_1 otherwise (12 orders each). So
exactly |w_k|² = cos²(Fd_1d_2/2), d = y_{k+1} − y_k = L^km^{(k)}, m^{(k)} ∈ {−h, …, h}⁴ (h = (L − 1)/2) the offset of y_k in its
level-(k+1) block (level-k units). As y_j runs over B(c), the offsets m^{(j)}, …, m^{(n−1)} run independently over
{−h, …, h}⁴. Therefore the block sum factorises exactly:
  𝒞_n(c, c) = Σ_{j=1}^nκ_j^{-1}L^{-4(n−j)}Π_{k=j}^{n−1}N_k(F),  N_k(F) := L^{-4}Σ_{m∈{−h..h}⁴}cos²(FL^{2k}m_1m_2/2)  (all orders in F).
(3) Second order. N_k(F) = 1 − (F²/4)L^{4k}μ_2² + O(F⁴), μ_2 := L^{-1}Σ_{|m|≤h}m² = (L² − 1)/12. With κ_j = sL^{2j},
κ_j^{-1}L^{-4(n−j)} = s^{-1}L^{-4n}L^{2j}, so 𝒞_n(c, c) = 𝒞^0(1 − F²δ_n + O(F⁴)), 𝒞^0 = s^{-1}L^{-4n}Σ_{j=1}^nL^{2j} and
δ_n = (μ_2²/4)Σ_{j=1}^nL^{2j}Σ_{k=j}^{n−1}L^{4k}/Σ_{j=1}^nL^{2j}. Per block log 𝒞_n(c, c) = log 𝒞^0 − F²δ_n + O(F⁴); a block has
L^{4n} fine sites, so c^cov_n = −δ_nL^{-4n}. With x := L^{-2}, i := n − j, m := n − k:
  c^cov_n = −(μ_2²/4)·[Σ_{i=1}^{n−1}x^iΣ_{m=1}^ix^{2m}]/[Σ_{i=0}^{n−1}x^i].
(4) Summation. Σ_{m=1}^ix^{2m} = x²(1 − x^{2i})/(1 − x²), so the numerator is x²(1 − x²)^{-1}[(x − x^n)/(1 − x) − (x³ − x^{3n})/(1 − x³)]
and the denominator (1 − x^n)/(1 − x). As n → ∞, using x/(1 − x) − x³/(1 − x³) = x(1 + x)/(1 − x³):
c_∞ = −(μ_2²/4)x³/(1 − x³) = −(L² − 1)²/(576(L⁶ − 1)) = −(L² − 1)/(576(L⁴ + L² + 1)). For finite n the bracket is
x(1 + x)/(1 − x³) − x^n/(1 − x) + x^{3n}/(1 − x³); dividing,
  c^cov_n/c_∞ = [1 − x^{n−1}(1 + x + x²)/(1 + x) + x^{3n−1}/(1 + x)]/(1 − x^n) = 1 − x^{n−1}(1 + x^n)/(1 + x)
(the last step: the difference of the two sides times (1 − x^n)(1 + x) is x^n(1 + x) − x^{n−1}(1 + x + x²) + x^{3n−1} + x^{n−1}(1 + x^n)(1 − x^n) = 0).
At n = 1 the bracket is 0 and at n = 2 it is (1 − x³)/(1 + x), which reproduces REVIEW_FLOW_S3's closed form at L_2 = L.
(5) Bounds. 0 < x^{n−1}(1 + x^n)/(1 + x) ≤ 1, decreasing in n; so c^cov_n/c_∞ ∈ [0, 1), increasing, and |c^cov_n − c_∞| =
|c_∞|x^{n−1}(1 + x^n)/(1 + x) ≤ |c_∞|x^{n−1}. s cancels in δ_n. ∎
*Remarks.* (a) The block-factorised formula in (2) is exact in F, so Γ^cov_n of this instance is known non-perturbatively
for constant F; only its F² coefficient is used. (b) Mechanism: the level-(n − i) noise has share x^i/Σx^{i'} of the
variance, and the path-flux variance it picks up from the last m steps is ∝ x^{2m} relative to the level-n block (areas
scale like L^{2k}, per-fine-site normalisation divides by L^{4n}); both are geometric, so the double sum converges. This is
the reviewer's "share of the level-(n − j) noise is ~L^{-2j}", now exact. (c) In f6's family (L_1 = 3 fixed, L_2 growing)
the level-1 share is 1/(L_2² + 1) → 0, so c^cov → 0 there; in the uniform chain the shares are fixed in n and c^cov_n → c_∞ ≠ 0.
Both are bounded, neither has a log: failure mode S4-F1 does not occur in this instance.

**What this does and does not give for SU(N) ((U-IR)(c), (s2) stay OPEN for the gauge chain).**
- Given Lemma COV-str (i)-(iii), β[Γ^cov_n] is β of ½log det of a finite-range operator whose background dependence sits in
  T_k(B_k), Π_{k+1}(B_k) at the tree composites. Colour reduction (exact): by Lemma F-Π (i) β can be read along one Cartan
  direction; for a Cartan-valued U_0 every B_k is Cartan valued (M̄ of commuting transports is in the torus, and W_♮ of a
  torus element is in the torus by uniqueness), so 𝒞_n(U_0) commutes with the torus and splits into the Cartan sector and
  the root sectors ±α, each a U(1)-charged 1-form chain with the phases of the contour paths.
- The scalar proof used two facts: per-block diagonality (false for the gauge chain: S4' contours span two blocks; only
  finite range survives, (iii)) and the geometric damping of every level's noise share (false for the gauge chain by (iv):
  pure-gauge noise is not damped). The share identity that does survive: S_j := κ^{-1}Π_j^{-1/2}A_j^T𝒞_n^{-1}A_jΠ_j^{-1/2} obeys
  0 ≤ S_j ≤ 1 and Σ_jtr S_j = dim (level-n link space) (because 𝒞_n ≥ κ^{-1}A_jΠ_j^{-1}A_j^T and Σ_jκ^{-1}A_jΠ_j^{-1}A_j^T = 𝒞_n);
  so the δ²Π_j-terms of the second variation are bounded by sup|δ²Π_j| per unit share. The δT_k-terms are linear in the
  level-k fluctuation field (not in its curvature) term by term, and their cancellation to curvature order is a gauge
  statement that a bound must respect.
- ~~So the exact remaining statement for SU(N) is:~~ **[RFL4-fix S4-4] (COV-NA) below is the wrong target (it is stated
  on Γ^cov_n alone, over all directions) and is REPLACED by (COV-GI) + (COV-⊥) (§35-§37). It is kept, struck, for the
  record.** ~~**(COV-NA)** in the second variation of ½log det 𝒞_n at U_0 = 1 along a
  Cartan constant-curvature direction, the pure-gauge sector of each level's noise (the part transported without loss by
  (iv)) contributes a background-independent amount, or an amount bounded uniformly in n and convergent at a geometric
  rate. [inference, not proven: by covariance A_j(B)D_{B_j}λ = D_{B_n}ev λ at every B, so the undamped part lives on the
  level-n gauge directions D_{B_n}(·), whose n-growth (iv) enters log det as a background-independent log n per direction;
  but A_j^T does not preserve the gauge directions, so the sectors are not decoupled exactly.]~~
  **[RFL4-fix S4-4] The bracket is struck: the growth (iv) is p-dependent (reviewer's inference: 𝒞_n|_{G_n} ≈
  κ^{-1}(c_0 + nG(0)p²)) and its coefficient is background dependent, so "a background-independent log n per direction"
  is unsupported; "not decoupled exactly" is true for 𝒞_n but false for B_n (Lemma COV-GI).**
- **[RFL4-fix S4-4] Replacement statement.** (COV-GI) (Lemma, §36): Γ^{W0}_n + Γ^cov_n = ½log det'(H_W +
  D𝔪^TP_⊥(P_⊥𝒞_nP_⊥)^+P_⊥D𝔪)|_slice + ½log det_⊥(P_⊥𝒞_nP_⊥) + ½log det(D^*_{B_n}D_{B_n}) − ½log det(J^*J) − log Δ_FP
  + const, so all 𝒞_n-dependence of B_n is through P_⊥𝒞_nP_⊥. **[RFL5-fix S5-1] "+ const" means the U_0- and
  𝒞-independent normalisations (powers of 2π and the U_0-independent constants of Γ^{W0}_n, Γ^cov_n) dropped in §36's
  Setting (l.1720 at session 5); the identity (iii) between the displayed terms has no additive constant (§36 (iii)).** (COV-⊥) for SU(N): β of ½log det_⊥(P_⊥𝒞_nP_⊥) is
  bounded uniformly in n and converges geometrically (Cartan sector: Proposition COV-⊥-C, §37; root sectors OPEN).
  **Remark (kept, not used):** (U-IR)(c) on Γ^cov_n alone, over all directions, may be false (the G_n block of 𝒞_n^{-1}
  has an effective correlation length ~√n) [inference, not proven]; it is no longer a hypothesis of UNIV.

## 31. FT-1: the trivial-point tower data, at each level (target S4-3)

Setting: Def F-strip, uniform κ; the one-step problem at level k, F_k(U; V) := 𝒯_k(U) + κΣ_ck̃(V_c, M̄_c(U)) (for N ≥ 3 with
§3.1's bookkeeping: every derivative of order ≤ 5 at 1 is the same for 𝒯_k and HIST's 𝓔_k, so nothing below changes).
Residual group G_res := {level-k gauge transformations g with g = 1 at the level-(k+1) sites}: F_k(·; V) is G_res-invariant.
Tori of side T ≥ 2 (in level-(k+1) units) first; infinite volume at the end. Kernels and local vertex maps as in §23.1
(level-k units).

**Lemma TOW (finite-order locality of the tree tower at 1, each level): PROVEN-HERE** [given upstream PROVEN-HERE:
Theorem N5-triv (PROOF l.5181), Setting N5-0 (l.5116-5121), FP-ab and N5-coer (1) (the decomposition used in §24.4 and
(I5)), N2-exp' (ii) as quoted in N5-loc, NA-FP, Lemma BL]. For every k ≥ 0:
(a) D^m𝒯_k(1), m = 2, 3, 4, are local symmetric multilinear kernels (m = 2: H_k);
(b) near V = 1 the one-step tower Φ_{k←k+1} has an analytic representative V ↦ e^{X*(V)} with X*(V) in the linear slice
  Σ_lin := {X : h(X) = 0, P_resd*X = 0} (FP-ab's slice functionals at the trivial background), and DX*(1), D²X*(1) are local
  maps (with exponential tails);
(c) Γ_k (§5.1) is analytic near 1 on every torus, gauge invariant, coarse-translation invariant and B_4-covariant, with an
  exponentially local Hessian at 1. Hence Lemma F-ren applies to Γ_k, β[Γ_k∘Φ_{k+1←n}] = β[Γ_k] = −b_k, and **F-tel's second
  claim β[Γ_{j→n}] = −Σ_{k=j}^{n−1}b_k, in particular B_n = Σ_{k<n}b_k, holds without (SF-bg)**.
Constants and decay rates may depend on k (not claimed uniform); F-tel is used at each fixed n, so none is needed.
*Proof.* (1) The trivial-point Hessian on the slice has a local inverse, uniformly in k and T. Per colour (Lemma F-Π (i)),
Hess_UF_k(1; 1) = H_k + κQ_k^TQ_k (H_k = Hess𝒯_k(1), Def F-strip; κQ^TQ is the Hessian of the kernel term at its zero,
Lemma COV-str (i) with P = 1). Σ_lin ⊂ ker h, and on Σ_lin the form ⟨X, dP_resd*X⟩ = ||P_resd*X||² vanishes, so the
compression of H_k + κQ_k^TQ_k to Σ_lin equals the compression of N5-triv's O_k = H_k + κQ^TQ + dP_resd* (Setting N5-0).
Σ_lin = Phys (d*X ∈ Λ_res^⊥ = span(δ_{c_X}, 1_{B(X)}) iff P_resd*X = 0), and by FP-ab's decomposition on ker h (N5-coer (1),
as in §24.4) C_k = C_k^{ph} ⊕ dT_k^{-2}d*, T_k := P_resΔ_0|_{Λ_res}. So the inverse of the slice compression is
C_k^{ph} = C_k − dT_k^{-2}d*: C_k is local with gap γ_k uniformly in k, T (Theorem N5-triv (i)); T_k is block-local with gap
≥ 1 (N5-coer (1)), so T_k^{-1} is local (BL (iii)) and so is dT_k^{-2}d* (BL (i)).
(2) Slice theorem. The map (g, X) ↦ (e^X)^g, G_res × Σ_lin → configurations, has derivative (λ, X) ↦ X + dλ at (1, 0)
(λ ∈ Λ' := {λ : λ(c_X) = 0}). It is bijective: d is injective on Λ' (dλ = 0 ⇒ λ constant ⇒ λ = 0), and λ ↦ (h(dλ), P_resd*dλ) =
(Mλ, P_resΔ_0λ) (h(dλ) = Mλ − λ(c_X), IT-line (a)) is injective on Λ' (Mλ = 0 puts λ in Λ_res, where P_resΔ_0 is invertible)
between spaces of equal dimension (#blocks + dim Λ_res = dim Λ'), so ⊕_bsu(N) = Σ_lin ⊕ dΛ'. By the inverse function theorem
(finite dimension, each torus) every configuration near 1 is (e^X)^g with unique (g, X) near (1, 0), and
min_UF_k(U; V) = min_{X∈Σ_lin}F_k(e^X; V) near the orbit of 1.
(3) Global = local branch. On a torus, F_k(U; 1) = 0 iff 𝒯_k(U) = 0 and k̃(1, M̄(U)) = 0; by induction on k (𝒯_0 = Σs vanishes
~~exactly on~~ **[RFL4-fix S4-3] only on** flat configurations (the induction needs only "𝒯_k(U) = 0 ⇒ U flat"; the converse is not shown and not used); the composite of a flat configuration is flat with the same holonomies, and V = 1 has
trivial holonomy) this is the G_res-orbit of 1. By compactness, minimisers of F_k(·; V) converge to that orbit as V → 1, so
for V near 1 they lie in the chart of (2), where (4) gives a unique critical point.
(4) Implicit function theorem on Σ_lin. X*(V) solves ∇_{Σ}F_k(e^X; V) = 0 (the gradient along G_res-orbits vanishes by
invariance); the Jacobian at (0, 1) is the slice compression of (1), invertible with local inverse C_k^{ph}. So X* is analytic
near 1, DX*(1) = −C_k^{ph}∂_V∇F_k(1; 1) (Lemma F-bg's linear tree background), and D²X*(1) = −C_k^{ph}(∇³F_k(1; 1)[Y', Y', ·])
with Y' := (DX*(1), 1). These are compositions of the local C_k^{ph} with ∇^{≤3}F_k(1; 1), which are local vertex maps by the
induction hypothesis (a) at k and §23 (I1) for the kernel term; so they are local (BL (i), (v)).
(5) Value function. 𝒯_{k+1}(V) = F_k(e^{X*(V)}; V) near 1. At a nondegenerate minimum on Σ_lin: D𝒯_{k+1}(1) = 0,
D²𝒯_{k+1}(1) = ∇²F_k[Y', Y'], D³𝒯_{k+1}(1) = ∇³F_k[Y', Y', Y'] (the D²X* terms meet ∇²F_k[(·, 0), Y'], whose Σ-component is the
stationarity equation, so they vanish), D⁴𝒯_{k+1}(1) = ∇⁴F_k[Y'⁴] + 3∇³F_k[(D²X*, 0), Y', Y'] (symmetrised). Each is a
contraction of local vertex maps with the local maps of (4): local (BL (v)). This is (a) at k + 1; the base k = 0 is 𝒯_0 = Σs
(finite range). Induction gives (a), (b) for every k.
(6) Γ_k. Γ_k(V) = ½log det(Hess_UF_k at U*(V), compressed to the covariant slice at U*) − log Δ_FP(U*) + Σ_clog𝒩'_1(P_c(U*)),
U* = e^{X*(V)} (Γ_k is G_res-invariant in U*, so the representative does not matter). It is analytic near 1 on each torus
(log det of a positive matrix; NA-FP's slice is analytic in the background). Its Hessian at 1 is ½tr(C_kD²H[v, v]) −
½tr(C_kDH[v]C_kDH[v]) plus the slice/FP and 𝒩'_1 terms, with DH[v] = ∇³F_k(1; 1)[(DX*v, v), ·, ·] and D²H[v, v] =
∇⁴F_k(1; 1)[(DX*v, v)², ·, ·] + ∇³F_k(1; 1)[(D²X*(v, v), 0), ·, ·]; the first derivatives of log Δ_FP and log𝒩'_1∘P at 1 vanish
(Lemma U-tad (i); D(log𝒩'_1∘P∘M̄)(1) = 0, §23 (I1)), so those terms are D²(…)(1)[DX*v, DX*v]; the slice pieces enter through
D(projector)(1) and D(P_res^{U})(1), local as in Lemma U-loc' (b). All are local by (a), (b), (1) and BL (v). Gauge
invariance, translation and B_4 covariance: §5.1 (covariance of every ingredient). So F-ren (i), (ii), (iii) apply to Γ_k
(their hypotheses are exactly these), and F-tel's proof (§5.5) goes through with no use of (SF-bg).
(7) Infinite volume. The objects above are built from translation-covariant (ℓZ⁴-periodic) local kernels by products,
inverses (with a gap) and contractions; periodisation is a homomorphism of the corresponding ℓ¹ kernel algebras (and
commutes with inverses that exist in ℓ¹), so the torus Taylor kernels are the periodisations of infinite-lattice local
kernels, and the infinite-volume β of Def F-g is computed from the latter. ∎
*What is not claimed.* Uniformity in k of the vertex bounds for D³𝒯_k, D⁴𝒯_k and of the tower rates (each induction step
multiplies constants); analyticity of 𝒯_k on a complex neighbourhood uniform in k; the global (large-field) part of
(SF-bg). (SF-bg) as a whole stays a layer-1 hypothesis where the small-field package uses it (Def F-strip's tower near the
trivial field in the polymer representation (SF-g)); FT-1's use, the trivial-point Taylor data of order ≤ 4 behind
B_n = Σb_k, no longer needs it. **[RFL4-fix S4-3] Caveat: no per-step rate or bound may be taken from TOW's constants (for example a rate of b_k → b_∞ from the per-step route, or an analyticity domain uniform in k); TOW gives locality at each k, and F-tel is used only at each fixed n.**
**Consequence for Theorem UNIV.** With §23 (Corollary U-red without (U-loc)) and Lemma TOW (F-tel's identity without
(SF-bg)), Theorem UNIV is conditional on (U-IR) — parts (a2), (a3), (a4), (b), (c) — and on the upstream PROVEN-HERE items
named in §23 and here; fix S3-1's second condition is discharged. (U-IR)(c) is PROVEN in the scalar U(1) instance only
(Proposition COV-sc); for SU(N) it is ~~the statement (COV-NA) of §30~~ **[RFL4-fix S4-4] (COV-GI) + (COV-⊥) (§35-§37), with (a2)
and (a4) restated as in §18 ((a2) on the transverse inverse compression; (a4') = (a4) minus the coarse-gauge block).**

## 32. Session-4 checks (ADDED AFTER the runs)
Both under one NUMERIC LOCK acquisition (03:52:43-03:52:48 UTC), nice 10, 1 thread, load 4.2, memory free 48%.
- **f6c** (amendment A1 of checks/f6_criteria.md, POST-HOC and labelled, appended 03:42:34 UTC after f6's run; script
  checks/f6c_closed.py reads only f6_out.txt; output checks/f6c_out.txt). (A1-cov) PASS: |c^cov_f6 − c^cov_closed| ≤ 4.2e-9 at
  ℓ = 9, 15 (printed rounding 5e-9). (A1-G) PASS: residual kernel-vertex slopes (c_it^K − c^cov_closed) × 48π² over (9, 15) =
  −0.0006 / −0.0011 / −0.0013 (κ_c = 0.25 / 1 / 4). (A1-H) PASS: residual composite slopes (Δ^K − c^cov_closed) × 48π² =
  −0.0003 / −0.0011 / −0.0030. (A1-G') NOT EVALUATED (ℓ = 21 not run). Rounding bound on these slopes: 1.9e-5. Reading (per
  A1's rule): after the exactly known Γ^cov transient is removed, f6's remaining kernel-vertex and composite-path parts show
  no slope above 0.005 over (9, 15); two ℓ values cannot exclude a small log.
- **f7** (checks/f7_criteria.md written 03:48:00 UTC before the script; f7_cov_chain.py; f7_out.txt; f7_time.txt; 4.7 s, peak
  372 MB). The uniform scalar chain at L = 3, n = 1..4 (ℓ = 3, 9, 27, 81), by link-by-link path phases and explicit ancestor
  sums. (P1) PASS (c_1 = 0). (P4) PASS (a second gauge and a displaced block: identical). (P5) PASS (s-independent).
  (P2) PASS: c_2, c_3, c_4 = −1.371742112483e-4, −1.509269913477e-4, −1.524366977917e-4, equal to Proposition COV-sc's closed
  form to all 12 printed digits. (P3) PASS (c_2 equals f6's stored ℓ = 9 value to 4.2e-9). (F7) PASS: increment ratio
  |c_4 − c_3|/|c_3 − c_2| = 0.1098 (closed form: ≈ L^{-2}(1 + O(L^{-2}))), |c_4|/|c_∞| = 0.998765. Informational: the finite-ε
  route with exact complex means (no variance expansion) agrees to ≤ 3.1e-11. Reading (per the criteria's rule): the
  closed form and the bounded, L^{-2}-geometric convergence hold in THIS scalar instance; nothing about SU(N).
  **[RFL4-fix S4-4] Independence note: f7's brute route computes the path phases link by link and walks explicit ancestor
  chains, but it takes the diagonal formula for 𝒞_n(c, c) from proof step (1) of Proposition COV-sc; step (1)'s
  diagonality is therefore not tested independently by f7.**

## 33. Session-4 outcomes against §29 (ADDED AFTER the derivations and checks)
- **Step 1 (fixes): DONE.** S3-1..S3-7 applied in place, tagged [RFL3-fix]: S3-1 (both "UNIV conditional on (U-IR) only"
  sentences withdrawn), S3-2 (F-mono clause 3 corrected; HIST use table H1-H5: with the corrected clause all five uses are
  covered, H1 and H3 included; H3, not in the lead's K4 list, flagged for HIST's owner in FLOW_LOG), S3-3 (§26 record; f6
  amendment A1 appended and evaluated), S3-4 (FN-1 pointers; the review's own replacement numbers did not match the current
  PROOF bytes, and the verified lines are used, FLOW_LOG 03:38), S3-5, S3-6, S3-7; tally 26 → 24.
- **S4-2: PROVEN in the scalar U(1) instance; OPEN for SU(N), ~~with a new obstruction identified~~ [RFL4-fix S4-4: no new
  obstruction; the (iv) sector is an artefact of the split, removed by (COV-GI)].** Lemma COV-str: at the
  point where 𝒞_n is defined, the composite covariance is the marginal covariance of a linear Gaussian chain with maps and
  weights at the tree composites (no curvature terms; S4-F2 does not occur), of finite range uniformly in n at every
  background near 1 **[RFL5-fix S5-1: at every U_0 ∈ 𝒰_n]** (this answers the reviewer's open point); and (iv) 𝒞_n has eigenvalue ≥ n/κ on coarse-gauge
  directions (no n-uniform gap of 𝒞_n^{-1}; ~~S4-F3's first half is observed: the gauge chain has a non-contracting sector~~ **[RFL4-fix S4-4]
  a fact about 𝒞_n on G_n; the sector cancels in B_n (Lemma COV-GI, §36), so it is not an obstruction**).
  Proposition COV-sc: in the scalar U(1) uniform chain, c^cov_n = c_∞[1 − L^{-2(n−1)}(1 + L^{-2n})/(1 + L^{-2})], c_∞ =
  −(L² − 1)/(576(L⁴ + L² + 1)): (U-IR)(c) with A_cov = |c_∞| and (s2) with θ = L^{-2}, A_s = L²|c_∞|; S4-F1 does not occur;
  f7 confirms it to 12 digits at n ≤ 4. The reviewer's prediction (convergence to c_cov ≠ 0, L^{-2}-geometric) holds in that
  instance. For SU(N) the remaining statement is ~~(COV-NA) (§30): whether the undamped pure-gauge sector's background
  dependence enters β at second order~~ **[RFL4-fix S4-4] (COV-GI) + (COV-⊥) (§35-§37)**.
- **S4-3 (FT-1): PROVEN** (Lemma TOW, §31), at each level, not uniformly in k: the trivial-point tower data behind
  B_n = Σb_k are local, so F-tel's identity and Theorem UNIV no longer use (SF-bg). S4-F4 does not occur (the slice
  compression of N5-triv's operator has the local inverse C_k − dT_k^{-2}d*).
- **Theorem UNIV now:** conditional on (U-IR) parts (a2) (IR-term vertices), (a3) (residual-group slice), (a4) (longitudinal
  entries, including the former (a1)-longitudinal), (b), and (c) for SU(N) (= ~~(COV-NA)~~ **[RFL4-fix S4-4] (COV-GI) + (COV-⊥), with (a2), (a4) restated as in §18**); plus (U-IR-s) for the rate.
  Discharged: (a1⊥) (session 3), (U-loc) (session 3), FT-1 (session 4), (c) in the scalar instance (session 4).

## 34. Tally after session 4 (FLOW.md items; session-4 items unreviewed)
- **PROVEN-HERE: 24 (sessions 1-3, as corrected by REVIEW_FLOW_S3) + 3 (session 4) = 27.** Session 4: Lemma COV-str (with
  (iv)), Proposition COV-sc (scalar U(1) instance of (U-IR)(c), (s2)), Lemma TOW (FT-1). Each conditional exactly as
  labelled; upstream PROVEN-HERE inputs used: Theorem N5-triv, Setting N5-0, FP-ab / N5-coer (1), IT-line (a), N2-exp' (ii)
  as quoted in N5-loc, NA-FP, N5-loc's range counts, LINEAR_PACKAGE §1.2's root covariance; HIST Lemma HF for the N ≥ 3
  bookkeeping.
- **GAP:** Corollary UNIV-rate (session-2 proof; repaired arithmetic given (U-IR-s), not counted).
- **WRONG as stated, superseded:** Lemma F-split (by Prop. U-dec); the session-3 sentence "UNIV conditional on (U-IR)
  only" (withdrawn; now true for a different reason, §31); F-mono's clause 3 (corrected; F-mono not counted).
- **IMPORTED-AND-REVERIFIED:** L4b — 1.
- **OPEN:** (U-IR) (a2), (a3), (a4) [s-P]; (b) [s]; (c) for SU(N) = ~~(COV-NA)~~ **[RFL4-fix S4-4] (COV-GI) + (COV-⊥); (a2) on the
  transverse inverse compression, (a4') = (a4) minus the coarse-gauge block** [s-P]; (U-IR-s) (s1) [s-P] and (s2) for SU(N);
  the RLARGE requirement FI-1 [cross-lane]; HIST's restatement of CL^J's Setting (H1-H5) [cross-lane, HIST's owner].
- **HYPOTHESES consumed (layer 1):** (SF-g), (RLF-δ), (SF-cont), (SF-∞); (SF-bg) no longer for B_n = Σb_k (Lemma TOW), still
  wherever the small-field package uses the tower beyond the trivial-point Taylor data.
- **Checks:** f6c (POST-HOC amendment A1: A1-cov, A1-G, A1-H PASS; A1-G' NOT EVALUATED); f7 (P1-P5, F7 all PASS).

---
# Session 5 of lane C (opened 2026-10-28 04:22 UTC)

## 35. Session-5 targets (pre-stated 2026-10-28 04:23 UTC, before any session-5 derivation, criteria file or script)

Binding input: REVIEW_FLOW_S4.md. Its fixes S4-1..S4-4 are applied in place and tagged **[RFL4-fix]** (step 1); text of
sessions 1-4 is otherwise unchanged. Outcomes are in a later section, added afterwards.

**Target S5-1 (COV-GI).** State and prove the exact Gaussian identity of REVIEW_FLOW_S4 §2 (2): with S the slice tangent
space at U_0 (a linear complement of D_{U_0}Λ', Λ' the fine 0-forms vanishing at the level-n sites), H the Wilson Hessian
compressed to S, M := D𝔪_n(U_0)|_S, D := D_{B_n} on level-n 0-forms and J : Λ_n → S the coarse-gauge lift,
  ½log det_S(H + M^T𝒞^{-1}M) + ½log det 𝒞 = ½log det'_S(H + M^TΠM) + ½log det_⊥(P_⊥𝒞P_⊥) + ½log det(D^*D) − ½log det(J^*J),
  Π := 𝒞^{-1} − 𝒞^{-1}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1} = P_⊥(P_⊥𝒞P_⊥)^+P_⊥,
for every 𝒞 > 0. Pre-stated route: (1) MJ = D at every background (covariance of 𝔪); (2) HJ = 0 at the backgrounds where
it holds (to be determined: Wilson-critical backgrounds; for the Cartan sector of Cartan backgrounds possibly every
one); (3) the flat Gaussian integral over μ (the coarse-gauge coordinates), with its Jacobian det(J^*J)^{1/2};
(4) the quotient-marginal identity and the determinant identity det 𝒞 = det_⊥(P_⊥𝒞P_⊥)det(D^*D)/det(D^*𝒞^{-1}D);
(5) identify the cancelling pieces (the Schur complement of 𝒞 on Ran D, which carries Lemma COV-str (iv)'s growth)
exactly; (6) at general small-field backgrounds: the exact remainder when HJ ≠ 0, and what is needed to control it.
**Target S5-2 (COV-⊥, Cartan sector).** Using GS-1 / GS-2-type damping: n-uniform two-sided bounds on P_⊥𝒞_nP_⊥ at the
trivial point, and, in the Cartan sector of a constant Cartan background, (i) n-uniform operator bounds for |F| in an
n-dependent neighbourhood, (ii) the F²-coefficient c^⊥_n of ½log det_⊥(P_⊥𝒞_nP_⊥) per fine site bounded uniformly in n
and convergent at a geometric rate. Root sectors are not targeted.
**Check f8** (criteria file first, its stat into FLOW_LOG before the script): a small-torus U(1) gauge chain with a
gauge-covariant model averaging map (stated in the criteria), (A) (COV-GI) and the statement "B_n depends on 𝒞_n only
through P_⊥𝒞_nP_⊥" to round-off, with a control in which HJ ≠ 0 that must FAIL; (B) the n-uniform transverse damping
and the n-growth of the gauge Schur complement, n = 1..3.

**Failure modes (each a valid outcome).** (S5-F1) HJ ≠ 0 on the coarse-gauge lift at the backgrounds that β needs, so
(COV-GI) holds only with a remainder; (S5-F2) the slice does not admit the lift J (S ∩ (Dλ + D_{U_0}Λ') not a single
point); (S5-F3) in the Cartan sector the background converts gauge noise into transverse noise (δT_k d ≠ 0), or the
F²-coefficient of the transverse determinant grows with n; (S5-F4) f8 (A) fails beyond round-off.

---
# Session-5 derivations (written after §35)

## 36. The coarse-gauge Gaussian identity (target S5-1)

**Setting.** n ≥ 1, ℓ = L^n, odd L; one torus at a time (fine side a multiple of ℓ; infinite volume per level-n block at
the end, as in §31 (7)). Fine tangent space E := ⊕_{fine links}su(N) in normalised exponential coordinates about U_0
(U = U_0e^X), with the metric of §0; Λ := fine 0-forms (su(N)-valued); D_0 := D_{U_0} : Λ → E the infinitesimal gauge
action at U_0; ev : Λ → Λ_n evaluation at the level-n sites (sites of every level, odd L); Λ' := ker ev, the Lie algebra
of the composite residual group G_res^{(n)} = {g : g = 1 at the level-n sites} (𝔪_n(U^g) = 𝔪_n(U) for g ∈ G_res^{(n)}).
Level n: Y := ⊕_{level-n links}su(N) in the frame of B_n := 𝔪_n(U_0), D := D_{B_n} : Λ_n → Y, G := Ran D (the coarse-gauge
directions G_n of REVIEW_FLOW_S4), P_G, P_⊥ := 1 − P_G the orthogonal projectors (P_⊥ onto ker D^*), K_0 := ker D,
Λ_n^♮ := K_0^⊥, k := dim Λ_n^♮ = dim G, m := dim Y. M := D𝔪_n(U_0) : E → Y. H := Hess𝒯_0(U_0) (Wilson). 𝒞 : Y → Y any
positive operator (in the application 𝒞 = 𝒞_n(U_0)). The δ-slice form of Γ^{W0}_n: S ⊂ E is the slice tangent space at U_0
and Γ^{W0}_n(U_0) = ½log det_S(A) − log Δ_FP(U_0), A := (H + M^T𝒞^{-1}M)|_S (compression to S, orthonormal basis of S);
Γ^cov_n = ½log det 𝒞 (§16, Corollary U-red; constants independent of U_0 and 𝒞 dropped throughout).
Hypotheses: **(S)** E = S ⊕ D_0Λ' (direct sum); **(N)** A > 0 on S.
- (S) holds at U_0 = 1 on every torus for the linear slices used in this lane (TOW (2): ⊕su(N) = Σ_lin ⊕ dΛ' at one level;
  the composite residual slice has the same structure with Λ' = ker ev; for the slice S_0 := {X : (D_0^*X)(x) = 0 at every
  fine site x that is not a level-n site} it is the Dirichlet uniqueness of the lattice Laplacian off a nonempty set),
  and then on a torus-dependent neighbourhood of 1 by continuity (a direct sum stays direct under small perturbation).
  **[RFL5-fix S5-2] (S) holds at EVERY background, for the slice S_0 exactly: S_0 = (D_0Λ')^⊥, so E = S_0 ⊕ D_0Λ' is an
  orthogonal sum, and D_0 is injective on Λ' with a T-uniform gap (Lemma S-all, §42).**
- (N) at U_0 = 1, per colour: if X ∈ S and ⟨X, AX⟩ = 0 then dX = 0 and MX = 0; on a torus X = dλ + h (h harmonic), and
  M = D𝔪 maps exact forms to exact forms (Md = d_n ev) and constants to nonzero constants, so h = 0 and d_n ev λ = 0, i.e.
  ev λ is constant, λ ∈ const + Λ', X ∈ dΛ' ∩ S = {0} by (S). So (N) holds at 1, and near 1 by continuity.
  **[RFL5-fix S5-2] This is (N) at 1 by a kernel argument, with no gap, on a torus-dependent neighbourhood. (N) at U_f
  (constant Cartan curvature), uniformly in T, is what β needs (COV-GI-∞); it was OPEN at session 5; §45 (Lemma N-f)
  proves it for |f| ≤ ε_n at each fixed n, given (L-loc).**
- **The Feynman form of the residual fixing** (δ(h)e^{−½||P_resD^*·||²} on ker h, §16) differs from the δ-slice form by a
  𝒞-independent factor whenever HD_0Λ_res = 0 (it does at the backgrounds of (ii) below): on ker h = S_Σ ⊕ D_0Λ_res,
  MD_0Λ_res = 0 (by (1) below, ev Λ_res = 0) and the Feynman term vanishes on S_Σ together with its cross terms, so the
  Gaussian form is block diagonal and the D_0Λ_res block (Feynman term only) does not contain 𝒞.
  **[RFL5-fix S5-3] The factor is 𝒞-independent but U_0-dependent: it is part of (a3) and must be kept in β.**

**Lemma COV-GI (the coarse-gauge Gaussian identity): PROVEN-HERE** [given (S), (N); upstream: the composite covariance
𝔪_n(U^g) = 𝔪_n(U)^{ev g} (§30, l.1509 statement; D4-norm), Lemma U-tad's equivariant chart]. Define the coarse-gauge lift
J : Λ_n^♮ → S by: Jμ := the unique element of S ∩ (D_0λ + D_0Λ') for any λ ∈ Λ with ev λ = μ. Then:
(i) J is well defined, linear and injective, and **MJ = D on Λ_n^♮, at every U_0 satisfying (S), (N)**; moreover J(K_0) := 0
  is consistent, i.e. if μ ∈ K_0 and HJ = 0 then the element S ∩ (D_0λ + D_0Λ') is 0.
(ii) **HJ = 0** (as a map Λ_n^♮ → S, H compressed to S) in each of the cases: (a) U_0 is a critical point of 𝒯_0 (for example
  a Cartan-valued configuration with constant Cartan curvature in infinite volume, or on a torus with quantised flux);
  (b) U_0 is Cartan valued (any such configuration), restricted to the Cartan sector of J (μ Cartan valued), provided S is
  torus equivariant.
(iii) **(COV-GI)** If HJ = 0 then, for every 𝒞 > 0,
  ½log det_S(H + M^T𝒞^{-1}M) + ½log det 𝒞
    = ½log det'_S(H + M^TΠM) + ½log det_{ker D^*}(P_⊥𝒞P_⊥) + ½log det_{Λ_n^♮}(D^*D) − ½log det_{Λ_n^♮}(J^*J),
  Π := 𝒞^{-1} − 𝒞^{-1}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1} = P_⊥(P_⊥𝒞P_⊥|_{ker D^*})^{-1}P_⊥,
  with no additive constant; det' is the product of the nonzero eigenvalues, and the kernel of (H + M^TΠM)|_S is exactly
  J(Λ_n^♮). Subtracting log Δ_FP on both sides: **Γ^{W0}_n + Γ^cov_n = ½log det'_S(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥)
  + ½log det(D^*D) − ½log det(J^*J) − log Δ_FP, so the 𝒞_n-dependence of Γ^{W0}_n + Γ^cov_n is through P_⊥𝒞_nP_⊥ only.**
(iv) (the cancelling pieces) With 𝒞^♭_G := (P_G𝒞^{-1}P_G|_G)^{-1} (the Schur complement of 𝒞 on G, i.e. the conditional
  covariance of P_GY given P_⊥Y for Y ~ N(0, 𝒞)):
  ½log det_S(H + M^T𝒞^{-1}M) = −½log det_G𝒞^♭_G + ½log det(D^*D) + ½log det'_S(H + M^TΠM) − ½log det(J^*J),
  ½log det 𝒞 = +½log det_G𝒞^♭_G + ½log det_⊥(P_⊥𝒞P_⊥);
  the ±½log det_G𝒞^♭_G pieces cancel exactly. 𝒞^♭_G is the only place where the G-block of 𝒞 (Lemma COV-str (iv):
  ⟨v, 𝒞_nv⟩ ≥ (n/κ)||v||² for v = d_nδ_x ∈ G at U_0 = 1) enters either term; the reviewer's "±½log(n/κ) per coarse-gauge
  direction" is the size of these pieces [estimate, not proven here; f8 (B) measures 𝒞^♭_G in a model].
*Proof.* (1) Covariance. For λ ∈ Λ and g_t := e^{tλ}: 𝔪_n((U_0e^{X})^{g_t}) = 𝔪_n(U_0e^X)^{ev g_t}. In the equivariant
exponential charts (Lemma U-tad's [RFL-fix]) the derivative at t = 0, X = 0 reads MD_0λ = D(ev λ). This holds at every U_0
(no criticality used).
(2) J well defined. Let μ ∈ Λ_n; ev is onto, so pick λ with ev λ = μ. By (S), D_0λ = s + D_0ρ with unique s ∈ S, ρ' ∈ Λ'
(ρ := ρ') **[RFL5-fix S5-3: read "with unique s ∈ S and some ρ ∈ Λ' (D_0ρ ∈ D_0Λ' unique; only D_0ρ is used, so injectivity
of D_0 on Λ' is not needed here, though it holds, §42)"]**, and s ∈ S ∩ (D_0λ + D_0Λ'). If λ' also has ev λ' = μ then λ' − λ ∈ Λ', so D_0λ' ∈ D_0λ + D_0Λ' and the same s
results; uniqueness of the element of S ∩ (D_0λ + D_0Λ') is the directness of (S) (two elements differ by an element of
S ∩ D_0Λ' = {0}). Linearity: the decomposition of (S) is linear. By (1), MJμ = M(D_0λ − D_0ρ) = Dμ − D(ev ρ) = Dμ, since
ev ρ = 0. Injectivity on Λ_n^♮: Jμ = 0 ⇒ Dμ = MJμ = 0 ⇒ μ ∈ K_0 ∩ K_0^⊥ = {0}. For μ ∈ K_0: MJμ = 0; if also HJμ = 0
then ⟨Jμ, AJμ⟩ = 0, so Jμ = 0 by (N).
(3) HJ = 0, case (a). Let f(X) := 𝒯_0(U_0e^X). Gauge invariance: f(Φ_g(X)) = f(X), Φ_g the action of g in the chart. With
V_λ(X) := ∂_tΦ_{e^{tλ}}(X)|_{t=0} (so V_λ(0) = D_0λ): Df(X)[V_λ(X)] = 0 for all X near 0. Differentiate at X = 0 along Y:
D²f(0)[Y, D_0λ] + Df(0)[DV_λ(0)Y] = 0. At a critical point Df(0) = 0, so D²f(0)[Y, D_0λ] = 0 for all Y ∈ E, λ ∈ Λ. With
Jμ = D_0(λ − ρ): ⟨Y, HJμ⟩ = D²f(0)[Y, Jμ] = 0 for all Y ∈ S, i.e. HJ = 0. Constant Cartan curvature is critical: the
gradient of 𝒯_0 at a Cartan-valued U_0 is torus invariant, so its root components vanish (they lie in nontrivial weight
spaces); its Cartan components are those of the abelian Wilson action, ∝ d^T(sin of the plaquette angles), and d^T of a
constant 2-form vanishes (each link lies in the plaquettes of a plane in pairs of opposite incidence).
(4) HJ = 0, case (b). For U_0 and λ Cartan valued and X Cartan valued everything commutes: (U_0e^X)^{e^{tλ}} =
U_0e^{X + t dλ} linkwise, so V_λ(X) = dλ does not depend on X and DV_λ = 0; the identity of (3) gives D²f(0)[Y, dλ] = 0
for Cartan Y without criticality. For root-valued Y, D²f(0)[Y, dλ] = 0 because the Hessian at the torus-fixed point U_0 is
a torus-invariant bilinear form and Cartan (trivial weight) and root (nonzero weight) spaces are orthogonal for such
forms. With a torus-equivariant S, the Cartan part of J lies in the Cartan sector, and HJ = 0 there.
(5) The Gaussian representation. For X ∈ S, e^{−½⟨X, HX⟩}p_𝒞(MX) = (2π)^{-m/2}(det 𝒞)^{-1/2}e^{−½⟨X, AX⟩}, p_𝒞 the
N(0, 𝒞) density on Y. Hence, by (N),
  I(𝒞) := ∫_S dX e^{−½⟨X, HX⟩}p_𝒞(MX) = (2π)^{(dim S − m)/2}exp(−[½log det_SA + ½log det 𝒞])   (Lebesgue measure on S).
So the left side of (iii) is −log I(𝒞) + ((dim S − m)/2)log 2π.
(6) Coordinates and the Jacobian. Let S' := S ⊖ J(Λ_n^♮) (orthogonal complement inside S) and T(μ, X') := Jμ + X'
(Λ_n^♮ × S' → S, a linear bijection by (2)). Its Gram matrix is diag(J^*J, 1), so dX = det(J^*J)^{1/2}dμ dX'. Since HJ = 0 and
H is symmetric, ⟨Jμ + X', H(Jμ + X')⟩ = ⟨X', HX'⟩; by (2), M(Jμ + X') = MX' + Dμ. So
  I(𝒞) = det(J^*J)^{1/2}∫_{S'}dX' e^{−½⟨X', HX'⟩}q(MX'),   q(y) := ∫_{Λ_n^♮}dμ p_𝒞(y + Dμ).
The μ-integral is the flat integral over the coarse-gauge coordinates: in A these directions carry only the IR term
D^*𝒞^{-1}D (HJ = 0), which is what makes the integral Gaussian and exact.
(7) Quotient-marginal formula. Substitute w = Dμ ∈ G: D is a bijection Λ_n^♮ → G with dw = det(D^*D)^{1/2}dμ. So
q(y) = det(D^*D)^{-1/2}∫_G dw p_𝒞(P_⊥y + P_Gy + w) = det(D^*D)^{-1/2}∫_G dw p_𝒞(P_⊥y + w) = det(D^*D)^{-1/2}p^⊥(P_⊥y), where p^⊥
is the density on ker D^* of the marginal of P_⊥Y, Y ~ N(0, 𝒞), i.e. of N(0, 𝒞_⊥), 𝒞_⊥ := P_⊥𝒞P_⊥|_{ker D^*} (Fubini over
Y = ker D^* ⊕ G, orthogonal, so Lebesgue measure factorises). Explicitly
  q(y) = det(D^*D)^{-1/2}(2π)^{-(m−k)/2}(det 𝒞_⊥)^{-1/2}exp(−½⟨y, Π̃y⟩),   Π̃ := P_⊥𝒞_⊥^{-1}P_⊥.
(8) The two forms of Π agree. Put R := the orthogonal projector onto Ran(𝒞^{-1/2}D); then Π = 𝒞^{-1/2}(1 − R)𝒞^{-1/2}
(expand R = 𝒞^{-1/2}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1/2}). ΠD = 0, and Π is symmetric, so Ran Π ⊂ (Ran D)^⊥ = ker D^* and Π = P_⊥ΠP_⊥.
For w ∈ ker D^*: ⟨𝒞^{1/2}w, 𝒞^{-1/2}Dν⟩ = ⟨w, Dν⟩ = 0, so (1 − R)𝒞^{1/2}w = 𝒞^{1/2}w and Π𝒞w = w; since ΠP_G = 0,
ΠP_⊥𝒞P_⊥w = Π𝒞w − ΠP_G𝒞w = w. So Π restricted to ker D^* is the inverse of 𝒞_⊥, and Π = Π̃.
(9) Assemble. The X'-integral in (6) is Gaussian with form (H + M^TΠM)|_{S'}:
  I(𝒞) = det(J^*J)^{1/2}det(D^*D)^{-1/2}(2π)^{-(m−k)/2}(det 𝒞_⊥)^{-1/2}(2π)^{dim S'/2}det_{S'}(H + M^TΠM)^{-1/2},
provided (H + M^TΠM)|_{S'} > 0. It is: in the coordinates of (6), T^*AT = [[D^*𝒞^{-1}D, D^*𝒞^{-1}M'], [M'^T𝒞^{-1}D, (H + M^T𝒞^{-1}M)|_{S'}]]
(M' := M|_{S'}; the H-cross block vanishes as HJ = 0), positive by (N), and its Schur complement on S' is
(H + M^T𝒞^{-1}M − M^T𝒞^{-1}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1}M)|_{S'} = (H + M^TΠM)|_{S'} > 0. Since dim S' = dim S − k the powers of
2π match those of (5) exactly, and taking −log gives (iii) with det_{S'} in place of det'_S. Finally (H + M^TΠM)|_S
annihilates J(Λ_n^♮) (HJ = 0, ΠMJ = ΠD = 0) and is symmetric, so it maps S' to S' and is positive there: its kernel is
exactly J(Λ_n^♮) and det_{S'} = det'_S.
(10) The cancelling pieces (iv). Block-decompose Y = ker D^* ⊕ G. The Schur formula for 𝒞 > 0 gives det 𝒞 =
det 𝒞_⊥·det 𝒞^♭_G with 𝒞^♭_G = (P_G𝒞^{-1}P_G|_G)^{-1} (the inverse of a block of 𝒞^{-1} is the Schur complement of the other
block of 𝒞). Polar decomposition D = V(D^*D)^{1/2}, V : Λ_n^♮ → G unitary: D^*𝒞^{-1}D = (D^*D)^{1/2}V^*𝒞^{-1}V(D^*D)^{1/2}, so
det(D^*𝒞^{-1}D) = det(D^*D)/det 𝒞^♭_G. From (9), det(T^*AT) = det(D^*𝒞^{-1}D)·det_{S'}(H + M^TΠM) and det(T^*AT) =
det(J^*J)det_SA (the Gram factor of (6)). Taking ½log of these two lines gives the two displays of (iv); adding them
reproduces (iii), which is a second, purely algebraic proof of (iii). ∎

*Reading.* (a) (COV-GI) holds for EVERY positive 𝒞; it uses only MJ = D (covariance, every background), HJ = 0, (S) and
(N). Nothing about the chain structure of 𝒞_n enters, so Lemma COV-str (iv)'s n-growth on G cannot reach B_n: it sits
in 𝒞^♭_G, which cancels exactly. (b) Which backgrounds β needs. Corollary U-red's alias reading gives β[F∘Φ_0] = β^fine[F̄]
for the gauge-invariant fine functionals F = Γ^{W0}_n, Γ^cov_n, and FLOW reads β^fine as twice the F² coefficient at
constant curvature along one Cartan direction (Lemma F-Π (i); the convention of Proposition COV-sc and checks f5-f7). So
for β the identity is needed exactly at constant Cartan curvature, which is case (ii)(a); there it holds in all sectors.
**[RFL5-fix S5-2] Corrections. (1) The identification of β^fine with twice the f² coefficient along U_f = exp(H_1fa_Φ) is
Lemma F-id (l.173-182), extended from finite support to F's exponentially decaying Hessian kernel at fixed n via
Lemma F-Π (ii)'s moment bound; Lemma F-Π (i) only reduces to one colour direction. (2) The reduction is conditional on
(COV-GI-∞): COV-GI at U_f in infinite volume (per-site densities), or on flux-quantised tori uniformly in T, which needs
(N) at U_f with a T-uniform gap and a C² per-site density in f. FLOW (session 5) proves (S), (N) only near 1 per torus,
which does not contain U_f. (COV-GI-∞) was OPEN at session 5; §45 proves it at each fixed n for |f| ≤ ε_n, given (L-loc).
(3) In the root sectors the right-side terms of (iii) are individually IR-singular at f = 0 (massless charged
Laplacians, F² log F densities); only IR-safe groups have an f² coefficient (§44).**
At the tower point U_0 = Φ_0(V) itself (not needed by this reading) HJ ≠ 0 in general (see below). (c) In the Cartan
sector, case (ii)(b) gives (COV-GI) at every Cartan background, critical or not.

**What is not claimed / general small-field backgrounds (S5-F1 in part).** If HJ ≠ 0 the exact statement is
  ½log det_SA + ½log det 𝒞 = [(iii)'s right side with H replaced by H_♮] + ½log det_S(1 + A_♮^{-1}(H − H_♮)),
  H_♮ := (1 − Q)^TH(1 − Q), Q := the projection of S onto J(Λ_n^♮) along S', A_♮ := (H_♮ + M^T𝒞^{-1}M)|_S
(H_♮J = 0, so (iii) applies to H_♮; the formula is the multiplicativity of det) **[RFL5-fix S5-3: provided A_♮ > 0]**. The remainder is linear in HJ =
−D𝒯_0(U_0)[DV_λ(0)·] to first order, but it involves A_♮^{-1} on J(Λ_n^♮), i.e. (D^*𝒞^{-1}D)^{-1} = (D^*D)^{-1/2}V^*𝒞^♭_GV(D^*D)^{-1/2}:
the undamped G-block and a level-n inverse Laplacian (power-law, not exponentially local). So the reviewer's suggestion
to treat it as a Lemma U-pair pairing needs U-pair's hypothesis (e) (an exponentially decaying kernel at each n), which is
NOT available for this term as written. This is not needed for β under reading (b); it would be needed for any statement
of (COV-GI) at the tower point. OPEN. Not claimed: the infinite-volume form beyond per-block densities of each term; the
IR safety of ½log det(D^*D) − ½log det(J^*J) in root sectors (REVIEW_FLOW_S4 §2 (5)(a); OPEN, part of (a4')).

## 37. The transverse covariance in the Cartan sector (target S5-2)

Setting: Lemma COV-str's uniform chain (d = 4, odd L, uniform κ in level units, per colour where named), infinite volume
(or any torus of side T in level-n units; every statement below holds verbatim there). Noise at levels j = 1, …, n, X_0 = 0.
Q := the S4' root map at U_0 = 1 in level units (T_k(1) = Q, Π_j(1) = 1, COV-str (iv)); Q_str := the straight average.
P_⊥ := 1 − d(d^*d)^+d^* on level-n 1-forms (the Cartan-sector form of §36's P_⊥: on Cartan-valued fields at a Cartan
background D_B = d). Imported (EXISTENCE §14, PROVEN there, read-only): **GS-1** Q^m − Q_str^m = d∘λ_m (λ_m linear), and
**GS-2 (e)** ||Q_str^mQ_str^{mT}|| ≤ L^{-2m} (white noise of unit variance; s = L^m), hence ||Q_str^m|| ≤ L^{-m}.

**Proposition COV-⊥-C (n-uniform transverse damping; Cartan sector): PROVEN-HERE** [GS-1, GS-2 (e) (imported, EXISTENCE
§14), Lemma COV-str (i)-(iii) with fix S4-2]. 
(a) (trivial point, each colour) P_⊥𝒞_n(1)P_⊥ = κ^{-1}Σ_{m=0}^{n−1}P_⊥Q_str^mQ_str^{mT}P_⊥, hence, n-uniformly,
  κ^{-1}P_⊥ ≤ P_⊥𝒞_n(1)P_⊥ ≤ κ^{-1}(1 − L^{-2})^{-1}P_⊥,   0 ≤ P_⊥(𝒞_{n+1}(1) − 𝒞_n(1))P_⊥ ≤ κ^{-1}L^{-2n}P_⊥,
  where 𝒞_{n+1} − 𝒞_n is read in level-n units of the top level (the chain extended by one level of noise at the bottom),
  and P_⊥𝒞_n(1)P_⊥ → 𝒞^⊥_∞ in operator norm at rate κ^{-1}L^{-2n}/(1 − L^{-2}).
(b) (Cartan sector, constant Cartan curvature, operator bounds) Let U_f be a constant-curvature field with curvature
  fH_1 ⊗ e_1∧e_2 (H_1 a fixed unit Cartan element; Lemma F-Π (i) allows one direction), B_k := 𝔪_k(U_f), and 𝒞^𝔥_n(f) the
  restriction of 𝒞_n(U_f) to Cartan-valued level-n fields. There are ε_0 > 0 and c_±, independent of n, such that for
  |f| ≤ ε_0L^{-2n}: c_-κ^{-1}P_⊥ ≤ P_⊥𝒞^𝔥_n(f)P_⊥ ≤ c_+κ^{-1}P_⊥.
(c) (Cartan sector, the F² coefficient) Let c^⊥_n be the coefficient of f² per fine site in ½log det_{Ran P_⊥}(P_⊥𝒞^𝔥_n(f)P_⊥).
  There are A_⊥, A'_⊥ and c^⊥_∞, independent of n, with **|c^⊥_n| ≤ A_⊥ and |c^⊥_n − c^⊥_∞| ≤ A'_⊥L^{-2n}** (θ = L^{-2}).
*Proof.* (0) Three structural facts in the Cartan sector of a Cartan background.
 (C1) Cartan-valued backgrounds stay Cartan valued (§30's colour reduction), T_k maps Cartan-valued fields to Cartan-valued
  fields (torus equivariance), and on them D_{B_k} = d; covariance A_j(B)D_{B_j} = D_{B_n}ev^{(n−j)} (§30, l.1509) becomes
  **T_k(B_k)d = d ev for every Cartan B_k**. Hence P_⊥^{(k+1)}T_kP_G^{(k)} = 0 and, by induction,
  P_⊥A_j = (P_⊥T_{n−1}P_⊥)⋯(P_⊥T_jP_⊥)P_⊥ (the reviewer's §2 (3)); P_⊥ does not depend on the background.
 (C2) T_k|_𝔥 and Π_{k+1}|_𝔥 depend on B_k only through the fluxes of closed level-k loops. For commuting arguments,
  M̄_c(B_ke^X) = (Π_{σ_0}B_k)·Σ_σw_σe^{iΦ_σ}e^{⟨χ_σ, X⟩} (w_σ the contour weights, χ_σ the signed incidence of path σ, σ_0 a
  reference path, Φ_σ the Cartan flux of the closed loop σσ_0^{-1}), and W_♮(gM) = gW_♮(M) (Re tr(V^{-1}gM) =
  Re tr((g^{-1}V)^{-1}M), uniqueness of the maximiser), so B_{k+1}^{-1}W_♮(M̄(B_ke^X)) depends on B_k only through (Φ_σ);
  the same holds for Π. For U_f the level-k plaquette flux is constant, F_k = L^{2k}f + O(f³) (the linear part is the
  curvature of Q's image, dQ = dQ_str by GS-1, and the straight average of a constant-curvature field has curvature L²
  times as large in level units; the O(f³) is the nonlinearity of W_♮), and Stokes (abelian) gives every Φ_σ as F_k times
  a signed area. So T_k|_𝔥 = 𝒯(F_k), Π_{k+1}|_𝔥 = 𝒫(F_k) for FIXED analytic functions 𝒯, 𝒫 (the chain is uniform in level
  units), and 𝒯(φ)d = d ev for every φ (C1), so every Taylor coefficient of 𝒯 annihilates d.
 (C3) Evenness. Complex conjugation c(U) = Ū commutes with transports, averages, polar parts and W_♮ (Re tr(V̄^{-1}M̄) =
  Re tr(V^{-1}M)), so 𝔪_k(Ū_f) = conj(𝔪_k(U_f)), and Ū_f has curvature −f (take U_{−f} := Ū_f). On tangent vectors c acts by
  X ↦ X̄, which is −1 on 𝔥 (X = i·diag(x)); conjugating the linear map T_k by −1 leaves it unchanged. So 𝒯(−φ) = 𝒯(φ),
  𝒫(−φ) = 𝒫(φ): 𝒯(φ) = Q + φ²τ + O(φ⁴), 𝒫(φ) = 1 + φ²π + O(φ⁴), with τ, π finite-range kernels, ||τ||, ||π|| < ∞, and
  **τd = 0**. On a disc |φ| ≤ ε_1 (fixed): ||𝒯(φ) − Q|| ≤ c_Tφ², π_- ≤ 𝒫(φ) ≤ π_+ (π_± > 0), |F_{k+1} − L²F_k| ≤ c_3|F_k|³.
(a) At U_0 = 1, A_j = Q^{n−j} and Π_j = 1. GS-1 and P_⊥d = 0 give P_⊥Q^m = P_⊥Q_str^m. So P_⊥𝒞_nP_⊥ =
κ^{-1}Σ_{j=1}^nP_⊥Q_str^{n−j}(Q_str^{n−j})^TP_⊥; the m = 0 term is κ^{-1}P_⊥, every term is ≥ 0, and GS-2 (e) bounds the m-th
by κ^{-1}L^{-2m}P_⊥ (P_⊥XP_⊥ ≤ ||X||P_⊥ for X ≥ 0). Extending the chain by one level adds exactly the m = n term.
(b) Induction on k: if |f| ≤ ε_0L^{-2n} with ε_0 small, then |F_k| ≤ 2L^{2k}|f| ≤ 2ε_0L^{-2(n−k)} ≤ ε_1 for k < n (from
|F_{k+1}| ≤ L²|F_k|(1 + c_3F_k²) and Π_k(1 + c_3F_k²) ≤ exp(c_3ΣF_k²) ≤ 2). By (C1) and GS-2 (e),
||P_⊥T_kP_⊥|| ≤ ||P_⊥QP_⊥|| + ||T_k − Q|| ≤ L^{-1} + c_TF_k² = L^{-1}(1 + Lc_TF_k²), so
||P_⊥A_j|| ≤ L^{-(n−j)}exp(Lc_TΣ_kF_k²) ≤ L^{-(n−j)}e^{Lc_T·8ε_0²/(L⁴ − 1)} =: L^{-(n−j)}e_0 (Σ_{k<n}4L^{4k}f² ≤ 4ε_0²L^{-4n}L^{4n}/(L⁴ − 1)).
Hence P_⊥𝒞^𝔥_nP_⊥ ≤ κ^{-1}π_-^{-1}e_0²(1 − L^{-2})^{-1}P_⊥ =: c_+κ^{-1}P_⊥, and P_⊥𝒞^𝔥_nP_⊥ ≥ κ^{-1}P_⊥Π_n^{-1}P_⊥ ≥ π_+^{-1}κ^{-1}P_⊥ =: c_-κ^{-1}P_⊥
(the j = n term, A_n = 1; all terms ≥ 0).
(c) At each n, 𝒞^𝔥_n(f) is analytic in f (finite range at fixed n, COV-str (iii)) and even (C3), so 𝒞^𝔥_n(f) = 𝒞^0_n + f²𝒞^{(2)}_n
+ O(f⁴), and with K_n := (P_⊥𝒞^0_nP_⊥|_{Ran P_⊥})^{-1} (||K_n|| ≤ κ by (a)) the f² coefficient of ½log det(P_⊥𝒞P_⊥) is
½tr[K_nP_⊥𝒞^{(2)}_nP_⊥] (the first-order term of log det vanishes, there being no f-linear part). Expanding (COV-str (ii)) with
F_k² = L^{4k}f² + O(f⁴), A_j = Π_{k}T_k and Π_j^{-1} = 1 − F_{j−1}²π + O(f⁴):
  𝒞^{(2)}_n = κ^{-1}Σ_{j=1}^n[A^{(2)}_jQ^{(n−j)T} + Q^{n−j}A^{(2)T}_j − L^{4(j−1)}Q^{n−j}πQ^{(n−j)T}],  A^{(2)}_j = Σ_{k=j}^{n−1}L^{4k}Q^{n−1−k}τQ^{k−j}.
Sandwich with P_⊥: P_⊥Q^a = P_⊥Q_str^a (GS-1), τQ^b = τQ_str^b (GS-1 and τd = 0), Q^{(n−j)T}P_⊥ = (P_⊥Q_str^{n−j})^T. With
a := n − 1 − k, b := k − j (so n − j = a + b + 1), the operators
  X_{a,b} := P_⊥Q_str^aτQ_str^b(Q_str^{a+b+1})^TP_⊥,   Y_i := P_⊥Q_str^iπ(Q_str^i)^TP_⊥
act on level-n 1-forms and, in level-n units, depend only on (a, b), resp. i, not on n (uniform chain). Per level-n site
(tr_s; |tr_sZ| ≤ 4r||Z||, r = N − 1 the Cartan rank; **[RFL5-fix S5-3] this needs Z to commute with level-n translations,
which X_{a,b}, Y_i and K_n do: the Cartan-sector maps depend only on the translation-invariant fluxes, (C2)**) and dividing by L^{4n} for per fine site, using tr[KZ^T] = tr[KZ] for
symmetric K:
  c^⊥_n = Σ_{a,b≥0, a+b≤n−2}L^{−4−4a}κ^{-1}tr_s[K_nX_{a,b}] − ½Σ_{i=0}^{n−1}L^{−4−4i}κ^{-1}tr_s[K_nY_i].
GS-2 (e): ||X_{a,b}|| ≤ ||τ||L^{-a}L^{-b}L^{-(a+b+1)} = ||τ||L^{−2a−2b−1}, ||Y_i|| ≤ ||π||L^{-2i}. So with u_n(a, b) :=
κ^{-1}L^{2a+2b+1}tr_s[K_nX_{a,b}] and v_n(i) := κ^{-1}L^{2i}tr_s[K_nY_i] (|u_n| ≤ 4r||τ||, |v_n| ≤ 4r||π||):
  c^⊥_n = Σ_{a+b≤n−2}L^{−5−6a−2b}u_n(a, b) − ½Σ_{i<n}L^{−4−6i}v_n(i),
  |c^⊥_n| ≤ 4r||τ||L^{-5}/((1 − L^{-6})(1 − L^{-2})) + 2r||π||L^{-4}/(1 − L^{-6}) =: A_⊥.
Rate: K_∞ := (𝒞^⊥_∞)^{-1} exists (𝒞^⊥_∞ ≥ κ^{-1}P_⊥) and ||K_n − K_∞|| ≤ ||K_n||·||P_⊥(𝒞^0_∞ − 𝒞^0_n)P_⊥||·||K_∞|| ≤ κL^{-2n}/(1 − L^{-2})
by (a). So |u_n − u_∞| ≤ 4r||τ||L^{-2n}/(1 − L^{-2}), |v_n − v_∞| ≤ 4r||π||L^{-2n}/(1 − L^{-2}). Define c^⊥_∞ by the same series with
u_∞, v_∞ over all a, b, i ≥ 0. The difference is bounded by the u-, v-differences over the summed range plus the tails
Σ_{a+b≥n−1}L^{−5−6a−2b} ≤ L^{−3−2n}/((1 − L^{-4})(1 − L^{-2})) and Σ_{i≥n}L^{−4−6i} ≤ L^{−4−6n}/(1 − L^{-6}); each is ≤ const·L^{-2n}. ∎

*Reading.* (1) This is (COV-⊥) for the Cartan sector: after (COV-GI) the 𝒞_n-dependent part of B_n in the Cartan sector
is ½log det_⊥(P_⊥𝒞^𝔥_nP_⊥) (and the Cartan IR-term vertices, (a2)); its F² coefficient is bounded uniformly in n and
converges at the rate L^{-2n}, with the same double-geometric mechanism (area weight L^{4k}, damping L^{-2(n−j)}, per-site
normalisation L^{-4n}) as Proposition COV-sc. Failure mode S5-F3 does not occur: τd = 0 exactly, so the background never
converts gauge noise into transverse noise in the Cartan sector. (2) The neighbourhood in (b) shrinks like L^{-2n}
(fix S4-2b); (c) is a statement at f = 0 at each n and does not need (b). (3) Not claimed: the root sectors (there D_B
depends on the background, P_⊥(B) is nonlocal and background dependent, and the IR-safe form via d_B𝒞_nd_B^T of
REVIEW_FLOW_S4 §2 (5)(a) is needed: OPEN); the explicit values of ||τ||, ||π|| for the S4' contours (finite by finite
range; not computed); (a2) in its transverse form.
**[RFL5-fix S5-5] Scope. At a Cartan background the Cartan-sector fluctuations are neutral: the Cartan sector carries no
universal (log ℓ) content (its f-dependence is O(f²) and local: the cos-weights of H and the |m|-weights of Π). All of the
universal one-loop coefficient lives in the root sectors ±α (charge α(H_1)). COV-⊥-C is necessary bookkeeping; it is not
where β_0 sits. What UNIV for SU(N) still needs (REVIEW_FLOW_S5 §3.3): (R1) the GS-1 analogue in a root sector at a
Cartan background (only an estimate, PROOF l.2148-2150); (R2) diamagnetic damping of the straight part; (R3) the
magnetic symbol calculus for P_⊥(B) with an IR-safe regrouping of the COV-GI right side (the root-sector right-side terms
are individually IR-singular at f = 0, so (COV-⊥) must be stated for IR-safe groups); (R4) (a2) transverse form, (a3),
(a4'), (b), (s1)/(s2⊥), with the UNIV proof rebuilt for the regrouped operator. Session 6 (§41-§46) addresses (R3) and
part of (R4).**

## 38. Session-5 checks (ADDED AFTER the runs; checks/f8_criteria.md, f8_cov_gi.py, f8_out.txt, f8_time.txt; amendment A1: f8b_fullbox.py, f8b_out.txt, f8b_time.txt)
Criteria written 04:31:31 UTC before any f8 script (stat in FLOW_LOG); smoke test in the scratchpad, no change after it.
Official f8: one NUMERIC LOCK acquisition 04:36:21-04:37:00 UTC, nice 10, 1 thread, 38.9 s, peak 1.14 GB. Model 1 (the
pre-registered "staple" map, t ⊥ μ) is a gauge-covariant U(1) averaging map, NOT the S4' contours.
- **Part A (Lemma COV-GI), model 1: (A0)-(A4) PASS; the control FAILS as required.** Cases (d, T, n) = (2, 3, 1), (2, 3, 2),
  (3, 3, 1), (4, 2, 1) (dim S up to 3904), f = 0, 0.03, 0.07. MJ = D and HJ = 0 to ≤ 1.8e-15; LHS(𝒞_n) − LHS(P_⊥𝒞_nP_⊥ + P_G)
  and LHS(𝒞_n) − LHS((1 + G)𝒞_n(1 + G)^T) ≤ 4.5e-13 (LHS up to 3.9e3); (COV-GI) RHS − LHS ≤ 5.7e-13; the kernel of
  H + M^TΠM on S is exactly k-dimensional (≤ 3.7e-15 relative, next eigenvalue ≥ 1.6e-3); the two forms of Π agree to
  ≤ 1.3e-15; the f² coefficients per fine site of LHS with 𝒞_n and with P_⊥𝒞_nP_⊥ + P_G agree to 3.9e-11 and 2.9e-12. Control
  (H + 0.3·1, so HJ ≠ 0): the A1 difference is 1.6e-3, 0.81, 4.4e-3, 2.1e-3, so A1 discriminates. Informational (A4): the
  f² coefficients of ½log det 𝒞_n alone and of ½log det_S(H + M^T𝒞_n^{-1}M) alone are +0.735 / −0.682 ((2,3,2)) and
  +0.037 / −0.138 ((4,2,1)), against the sum 0.0529 / −0.1012: the two halves are individually much larger than the sum.
- **Part B, model 1: (B1) FAIL; (B2), (B3), (B4) PASS.** (B1)'s "model prediction" (P_⊥𝒞_n(0)P_⊥ a multiple of P_⊥) was
  wrong about model 1: its paths average over a μ-dependent set of transverse offsets, so Q_staple − Q_tr is a set of
  component-wise differences of DIFFERENT 0-forms, not d∘h, and P_⊥ does not remove it (FLOW_LOG 04:37). ~~In model 1 the
  transverse block is NOT n-uniformly bounded~~ **[RFL5-fix S5-4] In model 1 the GS-2 bound (1 − L^{-2})^{-1} fails by a
  factor > 3 at n = 3, and the increments are not L^{-2}-damped (ratio 0.81 vs 0.11); whether the block is n-uniformly
  bounded is not decided by n ≤ 3 (the data are equally consistent with slow convergence)**: its spectrum is [1, 1], [1.105, 2.397], [1.118, 3.524] at n = 1, 2, 3 (T = 2).
  (B2) ⟨v, 𝒞_nv⟩/(n||v||²) = 1, 1.77, 2.17 ≥ 1. (B3) λ_max(𝒞^♭_G) = 1, 4.65, 8.83 (r_G = 1.15): linear-type growth of the gauge
  Schur complement, as REVIEW_FLOW_S4 §2 (4) inferred. (B4) c^⊥_n = 2.836e-2, 1.956e-2, 1.799e-2 (ratio 0.179; Richardson
  consistency ≤ 1.2e-7). **[RFL5-fix S5-4] B4 passes in model 1, where B1 fails: a three-point geometric test of c^⊥_n
  is not diagnostic of n-uniform damping and is not cited as evidence for (COV-⊥) without the operator bound.**
- **Amendment A1 (POST-HOC, appended 04:37:52 UTC after the official run; f8b, NUMERIC LOCK 04:38:55-04:39:44): model 2,
  the full-box staple (t over the full box, μ-independent legs, so Q_2 = Q_box − d∘h̄ exactly, the structure GS-1 uses).**
  (A') A0-A4 PASS, control FAILS as required (same magnitudes). (B1'a) PASS: max|P_⊥(Q_2^m − Q_box^m)| ≤ 6.2e-16 (m = 1, 2),
  Q_box built independently. (B1'b) **FAIL as pre-stated**, but only on the increment test: ||P_⊥Q_box^mQ_box^{mT}P_⊥|| =
  L^{-2m} to 12 digits (GS-2 (e) attained), all spectra of P_⊥𝒞_n(0)P_⊥ lie in [1, 1.125] = [1, (1 − L^{-2})^{-1}]
  ([1.0453, 1.1111] at n = 2, [1.0495, 1.1235] at n = 3, T = 2; [1.0617, 1.1111] at T = 3, n = 2), and P_⊥(𝒞_3 − 𝒞_2)P_⊥ has
  λ_max = L^{-4} + 5.8e-14 (4.7e-12 relative; diagnostic FLOW_LOG 04:40), against a pre-stated tolerance of 1e-12 relative:
  a round-off-level excess at an attained bound. (B4') PASS: c^⊥_n = 2.836e-2, 2.616e-2, 2.594e-2 (ratio 0.098).
  Informational: λ_max(𝒞^♭_G) = 1, 6.44, 12.19 (linear growth); c_full = 3.70e-2, 2.61e-2, 2.58e-2.
- **Reading (per the rule; POST-HOC parts labelled).** (1) Lemma COV-GI holds to round-off in both U(1) models, in
  d = 2, 3, 4 **[RFL5-fix S5-4] (U(1): HJ = 0 and MJ = D hold identically there, so A0 is structural, a tautology, not a
test of criticality; the "f ≠ 0" cases are cos-weighted Hessians and phase-weighted maps, not flux-quantised
configurations)**, at f = 0 and f ≠ 0, and fails when HJ ≠ 0, as the lemma says it must. (2) The n-uniform transverse damping of
  Prop. COV-⊥-C (a) is observed in model 2 (which has the structure Q = Q_str − d∘h of GS-1 / LINEAR_PACKAGE §1.2) with the
  bound attained, and is ABSENT in model 1 (which lacks it). So that structure is load-bearing for (COV-⊥): COV-⊥-C's
  proof uses it through GS-1 for the S4' map, where it is PROVEN upstream; ~~a gauge-covariant averaging without it can have
  an undamped transverse block~~ **[RFL5-fix S5-4] in a gauge-covariant averaging without it the GS-2 bound fails and the
  increments are not L^{-2}-damped at n ≤ 3; boundedness in n is undecided. In general the requirement is that P_⊥QP_⊥ be
  contracting with summable powers (Q = Q_0 − d∘h with Q_0 damping is one way)**. (3) The gauge Schur complement grows linearly in n in both models while cancelling exactly
  in B_n. (4) Nothing about root sectors or the S4' contours themselves is tested.

## 39. Session-5 outcomes against §35 (ADDED AFTER the derivations and checks)
- **Step 1 (fixes): DONE.** S4-1..S4-4 applied in place, tagged [RFL4-fix] (20 tags): l.1266 index and the H4 / √2 note;
  COV-str (i) N ≥ 3 d-terms and (iii) n-dependent neighbourhood 𝒰_n; TOW (3) "only on" and the no-per-step-constants caveat;
  (COV-NA) and its bracket struck and replaced by (COV-GI) + (COV-⊥) with the remark kept; (a2), (a4') restated (§18);
  §30 Reading, §31 Consequence, §32 f7 independence note, §33 and §34 lines corrected.
- **S5-1 (COV-GI): PROVEN** (Lemma COV-GI, §36) on each torus given (S), (N), whenever HJ = 0: at Wilson-critical
  backgrounds (all sectors; in particular constant Cartan curvature, which is what β needs under Corollary U-red's
  alias reading), and in the Cartan sector at every Cartan background. The flat integral over the coarse-gauge
  coordinates, its Jacobian det(J^*J)^{1/2}, the quotient-marginal step, and the exact cancellation of ±½log det 𝒞^♭_G
  (the pieces that carry Lemma COV-str (iv)'s growth) are written out, with a second algebraic proof. S5-F2 does not
  occur ((S) gives the lift). **S5-F1 occurs in part:** at non-critical backgrounds (e.g. the tower point itself) the
  identity holds only with the remainder ½log det(1 + A_♮^{-1}(H − H_♮)), which involves (D^*𝒞^{-1}D)^{-1}; not needed for β
  under the alias reading; OPEN otherwise. f8 Part A confirms the identity to ≤ 5.7e-13 and the control fails.
- **S5-2 (COV-⊥, Cartan sector): PROVEN** (Proposition COV-⊥-C, §37), given GS-1 and GS-2 (e) (EXISTENCE §14, imported):
  n-uniform two-sided bounds at the trivial point and in the Cartan sector for |f| ≤ ε_0L^{-2n}; the f² coefficient c^⊥_n
  of the Cartan-sector transverse determinant is bounded uniformly in n and converges at rate L^{-2n}. S5-F3 does not
  occur (τd = 0). f8 (POST-HOC model 2) shows the mechanism with the bound attained; f8's pre-registered model 1 lacks
  the GS-1 structure and shows an undamped transverse block (B1 FAIL), which marks that structure as load-bearing.
- **Theorem UNIV now:** conditional on (U-IR) parts (a2) [IR-term vertices of the transverse inverse compression],
  (a3), (a4') [cross entries, residual-slice longitudinal entries, the 𝒞-independent determinants of (COV-GI) together],
  (b), (c⊥) in the root sectors; plus (U-IR-s) for the rate ((s2) is now discharged in the Cartan sector). Discharged in
  session 5: the coarse-gauge block of (a4) and the replacement of (c) by (c⊥) (COV-GI), (c⊥) and (s2) in the Cartan
  sector (COV-⊥-C).
  **[RFL5-fix S5-1, S5-2, S5-5] Must be added: (COV-GI-∞) (OPEN at session 5) as a hypothesis of the β-use of COV-GI;
  (s2⊥) in place of (s2); the IR-safe grouping of COV-GI's root-sector right side; the UNIV proof re-split for the
  regrouped operator (§18). The Cartan sector carries no universal log ℓ content: all of β_0 is in the root sectors,
  whose programme is (R1)-(R4) (§37 Reading, fix S5-5).**

## 40. Tally after session 5 (FLOW.md items; session-5 items unreviewed)
- **PROVEN-HERE: 27 (sessions 1-4, as confirmed by REVIEW_FLOW_S4) + 2 (session 5) = 29.** Session 5: Lemma COV-GI (given
  (S), (N), in the cases HJ = 0 of (ii)), Proposition COV-⊥-C (Cartan sector; given GS-1, GS-2 (e), imported from
  EXISTENCE §14, PROVEN there). Upstream inputs used: the composite covariance 𝔪(U^g) = 𝔪(U)^{ev g}, Lemma U-tad's chart,
  Lemma COV-str (i)-(iii), Corollary U-red's alias reading, TOW (2)'s slice structure.
- **GAP:** Corollary UNIV-rate (unchanged).
- **WRONG as stated, superseded:** Lemma F-split; the session-3 sentence; F-mono's clause 3 (corrected); (COV-NA) as a
  target (wrong target, replaced; it was never claimed PROVEN).
- **IMPORTED-AND-REVERIFIED:** L4b — 1. Imported from EXISTENCE (PROVEN there, not re-proven here): GS-1, GS-2 (e).
- **OPEN:** (U-IR) (a2) transverse form, (a3), (a4') [s-P]; (b) [s]; (c⊥) root sectors, including the IR-safe pairing of
  ½log det(D^*_BD_B) − ½log det(J^*J) [s-P]; (COV-GI) at non-critical backgrounds (remainder) [s]; (U-IR-s) (s1) [s-P] and (s2)
  in the root sectors; **[RFL5-fix S5-2] (COV-GI-∞) [s] (COV-GI at U_f in infinite volume / uniformly in T: (N) at U_f
  with a T-uniform gap, C² per-site density); (s2⊥) for the root sectors [s-P]; the IR-safe grouping of COV-GI's
  root-sector right side [s-P]. Scope annotations (REVIEW_FLOW_S5 tally): COV-GI is a per-torus identity whose β-use
  needs (COV-GI-∞); COV-⊥-C is the Cartan sector only, which carries no universal content;** the RLARGE requirement FI-1 [cross-lane]; HIST's restatement of CL^J's Setting [cross-lane].
- **Checks:** f8 (A0-A4 PASS, control FAILS as required; B1 FAIL, B2-B4 PASS); f8b (POST-HOC amendment A1: A'0-A'4 PASS,
  control FAILS as required, B1'a PASS, B1'b FAIL at round-off of an attained bound, B4' PASS).

---
# Session 6 of lane C (opened 2026-10-28 04:58 UTC)

## 41. Session-6 targets (pre-stated 2026-10-28 05:18 UTC, before any session-6 derivation, criteria file or script)

Binding input: REVIEW_FLOW_S5.md. Its fixes S5-1..S5-5 are applied in place and tagged **[RFL5-fix]** (step 1, done
before this section); text of sessions 1-5 is otherwise unchanged. Outcomes are in a later section, added afterwards.

Setting for all targets: G = SU(N), the constant Cartan background U_f = exp(H_1 f a_Φ) (H_1 a unit Cartan element, a_Φ a
linear potential of unit curvature in the plane 12), root α with charge q_α := α(H_1) (Σ_{α>0}q_α² is to be computed in
the metric of §0), fixed n ≥ 1, ℓ = L^n.
**Target S6-1 (IR-safe grouping in the root sectors).** Regroup the right side of (COV-GI) at U_f into groups each of
which has an f² coefficient (as lim_{f→0}(G(f) − G(0))/f²). Pre-stated route: choose the orthogonal slice S_0 = (D_0Λ')^⊥;
identify J^*J as a Schur complement of the fine covariant Laplacian and combine it with the slice Jacobian; pair the
level-n Laplacian with the fine one.
**Target S6-2 (magnetic calculus).** At constant Cartan curvature: (a) the per-site density of log det of the nearest-
neighbour charged Laplacian on Z⁴ (Harper/Hofstadter in the plane 12), its small-f expansion with the exact
coefficient of f² log(1/|f|); (b) a twisted-convolution (magnetic translation) calculus for covariant operators with
exponentially decaying kernels, giving analyticity in f of per-site densities of gapped operators; (c) (COV-GI-∞): (S) at
every background, and (N) at U_f with a T-uniform gap for |f| small at fixed n.
**Target S6-3 (the f² log ℓ coefficient in the root sectors).** Compute exactly the f² coefficient of each IR-safe group
that the calculus of S6-2 solves, uniformly in n; show the Cartan sector contributes no log ℓ; state exactly what remains
for the other groups, and the value they must contribute for the total to be the universal −β_0^std log ℓ (in u-units,
Δu = 2 × the f² coefficient per fine site).
**Check f9** (criteria file first, its stat into FLOW_LOG before any f9 script; jobs < 20 min, < 1 GB): on lattices with
constant Cartan curvature, (G) the scalar (ghost) pieces: the exact second-order heat-trace coefficient against a direct
lattice computation, the coefficient of f² log(1/|f|) and the ghost-group f² coefficient against the closed form for
ℓ = 3, 9; (V) the root-sector vector (Feynman) operator built from the SU(2) Wilson Hessian at a Cartan background:
criticality (the Feynman intertwining) to round-off, and its large-t heat-trace f² coefficient against the universal
continuum value; the Cartan block's coefficient against "no log".

**Failure modes (each a valid outcome).** (S6-F1) no grouping of the root-sector right side is IR-safe term by term
(the non-analytic f² log f parts do not cancel within groups); (S6-F2) the f² log(1/|f|) coefficient of the lattice
charged Laplacian differs from the continuum (Landau) value; (S6-F3) the ghost group's f² coefficient is not n-uniform
or not of the form const × log ℓ; (S6-F4) (N) at U_f fails or its gap is not T-uniform; (S6-F5) the lattice vector
heat-trace coefficient does not approach the continuum value (a lattice artefact surviving at large t).

---
# Session-6 derivations (written after §41)

Common setting. n ≥ 1, ℓ = L^n, odd L; fine lattice Z⁴ (or a torus of side a multiple of ℓ); level-n sites ℓZ⁴.
D_0 := D_{U_0} : Λ → E the fine covariant gradient, (D_0λ)_b = Ad(U_b^{-1})λ(x) − λ(x + μ) for b = (x, μ) in the chart
U = U_0e^X (the sign is immaterial below); Δ_0 := D_0^*D_0 on Λ (fine covariant Laplacian, adjoint); E' the orthogonal
projector of Λ onto Λ' = {ρ : ρ = 0 at the level-n sites}; Δ' := E'Δ_0E' on Λ' (Dirichlet Laplacian). U_f :=
exp(H_1 f a_Φ), H_1 = i·diag(h) unit for §0's metric ((1/N)Σh_i² = 1), a_Φ a linear potential of unit curvature in the
plane 12. For a root α = e_i − e_j put q_α := h_i − h_j; Ad(exp(H_1θ)) acts on the root vector E_ij by e^{iq_αθ}, so in
the root sector α the background is a U(1) field of flux q_αf per plaquette of the plane 12, and
**Σ_{α>0}q_α² = Σ_{i<j}(h_i − h_j)² = NΣh_i² − (Σh_i)² = N²** (SU(2): H_1 = iσ_3, q = 2). Per-site traces: τ(K) := K(x, x)
summed over the internal indices of one site (one cell for ℓZ⁴-covariant operators, then divided by ℓ⁴ for "per fine
site"). For a root pair ±α the real fields form one complex field, and ½log det over the real root-pair space equals
log det over the complex field; all root-sector densities below are complex (one per positive root).

## 42. (S) at every background (fix S5-2)

**Lemma S-all: PROVEN-HERE.** Let S_0 := {X ∈ E : (D_0^*X)(x) = 0 at every fine site x that is not a level-n site}. For
EVERY background U_0 (no smallness, no criticality):
(i) S_0 = (D_0Λ')^⊥, so E = S_0 ⊕ D_0Λ' (orthogonal): (S) holds;
(ii) ||D_0ρ||² ≥ γ_n||ρ||² for ρ ∈ Λ', γ_n := 1/(2ℓ⁵), on every torus of side a multiple of ℓ and in infinite volume
  (also for Bloch-twisted fields); in particular D_0 is injective on Λ' and Δ' ≥ γ_n;
(iii) for Cartan-valued U_0, S_0 is torus equivariant (the condition D_0^*X = 0 commutes with the torus action).
*Proof.* (i) ⟨X, D_0ρ⟩ = Σ_{x not level-n}⟨(D_0^*X)(x), ρ(x)⟩ vanishes for all ρ ∈ Λ' iff X ∈ S_0. (ii) Kato: Ad is
isometric, so |(D_0ρ)_b| ≥ ||ρ(x)| − |ρ(x + μ)||, hence ||D_0ρ||² ≥ ||d u||² with u := |ρ| ≥ 0, u = 0 on ℓZ⁴. Cover the
lattice by the disjoint blocks c + {−h_n, …, h_n}⁴ (h_n = (ℓ − 1)/2, c ∈ ℓZ⁴). For y in the block of c take the axial path
from c to y (directions in the order 1, 2, 3, 4), of length ≤ 4h_n < 2ℓ, inside the block; u(c) = 0 and Cauchy-Schwarz give
u(y)² ≤ 2ℓΣ_{e∈path(y)}(du)_e². Each edge lies on the paths of at most ℓ⁴ points of its block, and the edges of different
blocks are distinct, so ||u||² ≤ 2ℓ⁵||du||². Nothing here depends on the background or on T. (iii) Clear. ∎
*Consequence.* With S = S_0 the lift of Lemma COV-GI is the orthogonal projection Jμ = P_{S_0}D_0λ (any λ with ev λ = μ),
i.e. Jμ = D_0λ^har_μ with λ^har_μ := λ − ρ*, ρ* ∈ Λ' minimising ||D_0(λ − ρ)|| (the covariant harmonic extension of μ off the
level-n sites).

## 43. The slice Jacobian and the ghost group (target S6-1)

**Lemma GH (Landau regrouping of COV-GI): PROVEN-HERE** [given Lemma COV-GI, Lemma S-all]. Let U_0 be a critical point of
𝒯_0 satisfying (N) for S = S_0, and let 𝒮 be the Schur complement of Δ_0 onto the level-n sites (Λ = Λ_n ⊕ Λ', i.e.
𝒮 = Δ_{nn} − Δ_{n'}Δ'^{-1}Δ_{'n}, ⟨μ, 𝒮μ⟩ = min_{ρ∈Λ'}||D_0(λ_μ − ρ)||²). Then:
(i) J^*J = 𝒮|_{Λ_n^♮} and ker 𝒮 = K_0 (= ker D on Λ_n);
(ii) J(Λ_n^♮) = S_0 ∩ D_0Λ, D_0Λ = D_0Λ' ⊕ J(Λ_n^♮) (orthogonal), and S' := S_0 ⊖ J(Λ_n^♮) = ker D_0^*;
(iii) the exact slice Jacobian of S_0 is Δ_FP = det(Δ')^{1/2}: the Gram matrix of (s, ρ) ↦ s + D_0ρ (S_0 × Λ' → E) is
  diag(1, Δ'). At U_0 the form Q(X) := ⟨X, (H + M^T𝒞^{-1}M)X⟩ is invariant under X ↦ X + D_0ρ, ρ ∈ Λ' (HD_0 = 0 by COV-GI
  proof (3); MD_0ρ = D ev ρ = 0), so −log[∫_E dX e^{−Q/2}/∫_{Λ'}dρ] = ½log det_{S_0}A − ½log det Δ' + const, and every exact
  Faddeev-Popov representation of this quotient integral gives the same number up to a U_0-independent constant
  **[RFL6-fix S6-1] (the former parenthetical "a legitimate fixing differs … by its own U_0-dependent normalisation, which
  is (a3) bookkeeping" is DELETED: a U_0-dependent normalisation mismatch would shift β by O(β[G_gh]), e.g. using Δ_FP(1)
  for Δ_FP(U_0) would cancel all of β[G_gh]; the identity is used only for the exact quotient. That the tower's own fixing
  (h_U, P_res^UD_U^*) with its Δ_FP(U_0) IS an exact FP representation of this quotient, with no constant, is Lemma
  FP-exact, §52)**;
(iv) consequently, with constants independent of U_0 and 𝒞,
  Γ^{W0}_n + Γ^cov_n = ½log det_{ker D_0^*}(H + M^TΠM) + ½log det_⊥(P_⊥𝒞P_⊥) + ½log det_{Λ_n^♮}(D^*D) − ½log det_{Λ_n^♮}𝒮 − ½log det Δ',
  and when Δ_0 is invertible on Λ (no covariantly constant 0-forms; true in every root sector at f ∉ 2πZ/q_α),
  −½log det 𝒮 − ½log det Δ' = −½log det Δ_0, so
  **Γ^{W0}_n + Γ^cov_n = G_⊥,n + G_gh,n,  G_⊥,n := ½log det_{ker D_0^*}(H + M^TΠM) + ½log det_⊥(P_⊥𝒞_nP_⊥),
  G_gh,n := ½log det(D_n^*D_n) − ½log det(D_0^*D_0)**  (D_n := D_{B_n}, B_n = 𝔪_n(U_0));
  in general the last identity holds with det' and a factor depending only on the kernels (rank ≤ dim su(N)), which is
  invisible in per-site densities;
(v) (Feynman form) (H + M^TΠM)D_0 = 0, so on E = ker D_0^* ⊕ Ran D_0 the operator O^♯ := H + D_0D_0^* + M^TΠM is block
  diagonal and ½log det_{ker D_0^*}(H + M^TΠM) = ½log det_E O^♯ − ½log det'Δ_0; hence
  Γ^{W0}_n + Γ^cov_n = ½log det_E O^♯ − log det'(D_0^*D_0) + ½log det(D_n^*D_n) + ½log det_⊥(P_⊥𝒞_nP_⊥) (+ kernel factors).
*Proof.* (i) By §42's Consequence ||Jμ||² = ||D_0λ^har_μ||² = ⟨μ, 𝒮μ⟩ for every μ ∈ Λ_n, so J^*J = 𝒮 as forms on Λ_n (J
extended to Λ_n by the same formula). If μ ∈ K_0 then MJμ = Dμ = 0 and HJμ = 0 (critical), so ⟨Jμ, AJμ⟩ = 0 and Jμ = 0 by
(N): 𝒮μ = 0. Conversely 𝒮μ = 0 ⇒ Jμ = 0 ⇒ Dμ = MJμ = 0. (ii) S_0 ∩ D_0Λ = {D_0λ : E'Δ_0λ = 0} = {D_0λ^har_μ} = J(Λ_n) =
J(Λ_n^♮) (J(K_0) = 0 by (i)). D_0Λ' ⊂ D_0Λ and S_0 = (D_0Λ')^⊥ give the orthogonal splitting of D_0Λ; then
S' = (D_0Λ')^⊥ ∩ J(Λ_n^♮)^⊥ = (D_0Λ)^⊥ = ker D_0^*. (iii) The Gram computation is direct (S_0 ⊥ D_0Λ'). Invariance:
Q(X + D_0ρ) = Q(X) because (H + M^T𝒞^{-1}M)D_0ρ = 0 and the form is symmetric. Decomposing X = s + D_0ρ, dX =
det(Δ')^{1/2}ds dρ and the ρ-integral factors out. The FP statement is the standard identity for a Gaussian invariant under
a linear group action (each exact FP representation integrates the same invariant function over the same quotient).
(iv) COV-GI (iii) with S = S_0, det'_{S_0} = det_{S'} (COV-GI proof (9)), (i)-(iii) above. Schur: det Δ_0 = det Δ'·det 𝒮 when Δ_0
is invertible (then K_0 = 0 by (i), and Λ_n^♮ = Λ_n); a covariantly constant root-sector 0-form would have trivial holonomy
around a plaquette of the plane 12, which is e^{iq_αf}. (v) HD_0 = 0 (critical) and ΠMD_0λ = ΠD ev λ = 0; a symmetric operator
that kills Ran D_0 preserves ker D_0^*; D_0D_0^* vanishes on ker D_0^* and on Ran D_0 is unitarily equivalent to Δ_0 on
(ker D_0)^⊥. ∎
*Reading.* (1) The 𝒞-independent determinants of COV-GI combine exactly: −½log det(J^*J) − log Δ_FP = −½log det(D_0^*D_0), the
full fine (Landau-gauge) ghost determinant. What is left of them is the ghost group G_gh, a pairing of two nearest-
neighbour covariant Laplacians, the fine one at U_0 and the level-n one at B_n. This is a different (equivalent) grouping
from REVIEW_FLOW_S5 §2.2's suggestion (D^*D against J^*J = 𝒮), which leaves the gapped Dirichlet factor ½log det Δ' apart.
(2) S' = ker D_0^*: the "residual" determinant of COV-GI is the fine transverse (Landau-gauge) operator with the
transverse IR term. (3) (v) is the form in which J_n is redefined (§18, fix S5-1).

## 44. The ghost group at constant Cartan curvature: exact solution (targets S6-2 (a), S6-3)

**Lemma B-flux: PROVEN-HERE** [given §30's colour reduction, (C1)-(C3) of §37, B_4 covariance]. For |f| ≤ ε_0L^{-2n},
B_n = 𝔪_n(U_f) is Cartan valued and, in infinite volume, Cartan-gauge equivalent to the level-n constant-curvature field
with flux F_n in the plane 12 and no other flux, where F_n = F_n(f) is odd, analytic at fixed n, F_n(f) = ℓ²f + O_n(f³).
*Proof.* Cartan valued: §30. ℓZ⁴-translation of U_f is a Cartan gauge transform of U_f, and 𝔪_n is gauge and translation
covariant, so the (gauge-invariant) level-n plaquette fluxes of B_n are translation invariant. The reflection x_3 ↦ −x_3
about a level-n site maps U_f (in the gauge with only 2-links nontrivial, depending on x_1) to itself and reverses the
orientation of every plaquette in the planes 13, 23, 34; B_4 covariance of the S4' family then forces those fluxes to vanish;
x_4 ↦ −x_4 does the same for 14, 24. Abelian configurations on Z⁴ are determined up to gauge by their plaquette fluxes. F_n:
(C2) (F_{k+1} = L²F_k + O(F_k³), F_0 = f), and oddness from (C3). ∎
**[RFL6-fix S6-5] Per root.** For N ≥ 3 the Cartan-sector average acts entrywise on the diagonal phases, so beyond linear
order the level-n flux of B_n is diag(F_n(h_if)) (plus a common determinant phase), not F_n(f)H_1. The statement used
below is per root: root α sees the level-n flux **F_{n,α}(f) = q_αℓ²f + O_n(f³)** (odd, analytic at fixed n); for SU(2)
F_{n,α} = q_αF_n. Read q_αF_n as F_{n,α} in Proposition GH-log and its proof; nothing else changes (only the linear order
and the O_n(f³) remainder are used).

Let Δ_φ be the nearest-neighbour covariant Laplacian on Z⁴ for a complex field of charge 1 in a constant field of flux φ
in the plane 12, (Δ_φψ)(x) = Σ_{μ}[2ψ(x) − U_{x,μ}ψ(x + μ) − U^*_{x−μ,μ}ψ(x − μ)], and g(φ) := τ(log Δ_φ) (finite for every φ:
the 4D spectral measure gives log-integrable weight near 0). Let j_ν(t) := e^{−2t}I_ν(2t) (j_0 = the 1D heat kernel at 0) and
P(t) := j_0(t)⁴ = τ(e^{−tΔ_0}).

**Lemma G-mag (the charged Laplacian at constant field): (i)-(v) PROVEN-HERE; (vi) ARGUED, not counted.** **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]**
(i) (Feynman-Kac, exact) τ(e^{−tΔ_φ}) = P(t)E_t[cos φA], E_t the law of the continuous-time simple random walk bridge on Z⁴
  (rate 1 per neighbour) of duration t, A the signed algebraic area of its projection to the plane 12.
(ii) g(φ) − g(0) = Ψ(φ) := ∫_0^∞(dt/t)P(t)(1 − E_t cos φA) ≥ 0.
(iii) (exact second moment) P(t)E_t[A²] = m(t) := (t²/3)j_1(t)²j_0(t)², i.e. ∂²_φτ(e^{−tΔ_φ})|_0 = −m(t); in the plane alone,
  j_0²E^{(2)}_t[A²] = (t²/3)j_1².
(iv) E_t[A⁴] ≤ C_4t⁴ for t ≥ 1.
(v) ψ(φ) := Ψ(φ)/φ² = c_g log(1/|φ|) + c'(φ) with **c_g = 1/(96π²)** and sup_{0<|φ|≤1}|c'(φ)| < ∞. (This is the continuum
  (Landau) value: −D² in 4D has heat-trace density (16π²t²)^{-1}(Bt/sinh Bt), whose B²t² coefficient −1/6 gives c_g =
  (1/6)/(16π²); S6-F2 does not occur.)
(vi) c'(φ) → c'_0 as φ → 0. **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]** [ARGUED (superseded by §58): equivalent to E cos(φA_{s/φ}) → s/sinh s for each s > 0 (the invariance principle for
  the area of the lattice bridge: A_t = ∫x dy is a martingale for the free walk with bracket 2∫x²ds, so the martingale
  functional CLT gives (x/√t, y/√t, A/t) → (B¹, B², ∫B¹dB²) for the free walk; the bridge is absolutely continuous on
  [0, (1 − δ)t], and the last δt costs O(δ) by (iv)); then dominated convergence with the bounds of (v)'s proof. Not written
  out; f9 (G2) tests it numerically.]
*Proof.* (i) e^{−tΔ_φ} = e^{−8t}e^{tW}, W the transport-weighted hopping; e^{tW}(x, x) = Σ_kt^k/k!·Σ_{closed paths ω of k steps
at x}hol(ω), and e^{−8t}t^k/k! is the probability of a given k-step jump sequence of the walk in time t. For a constant
abelian field hol(ω) = e^{iφA(ω)} (lattice Stokes; in the gauge U_{x,2} = e^{iφx_1}, other links 1, the phase of a closed
path is φΣ_{2-steps}x_1Δx_2 = φA). A ↦ −A under the reflection x_1 ↦ −x_1, so the expectation is real. (ii) Spectrally,
log b − log a = ∫_0^∞(e^{−ta} − e^{−tb})dt/t; apply with Δ_0 + ε, Δ_φ + ε and let ε ↓ 0 (monotone convergence; the integrand
is ≥ 0 by (i) and is O(t^{-3}) at ∞, O(φ²t³) at 0). (iii) Write x = N_1^+ − N_1^-, y = N_2^+ − N_2^- (independent Poisson
processes of rate 1), A_t = ∫_0^tx(s−)dy(s), and compute E[A²; x_t = y_t = 0] (the plane factor; the directions 3, 4 give
j_0²). *Tilt lemma:* for a Poisson process N of rate 1 on [0, t] and F a polynomial in finitely many ∫h dN, E[z^{N_t}F] =
e^{(z−1)t}E^{(z)}[F], E^{(z)} the expectation for intensity z (for real z > 0 this is the Radon-Nikodym formula; both sides are
entire in z, the right one a polynomial times e^{(z−1)t} by Campbell's formula κ_r(∫h dN) = z∫h^r, so they agree at
z = e^{±iθ}). With 1{y_t = 0} = ∫_{−π}^{π}(dθ/2π)e^{iθy_t} and intensities e^{±iθ} for N_2^±: E^θ[A] = 2i sin θX_1,
Var^θA = 2cos θX_2 (X_r := ∫_0^tx_s^rds), so E_y[A²; y_t = 0 | x] = ∫(dθ/2π)e^{−2t(1−cos θ)}(2cos θX_2 − 4sin²θX_1²) =
2j_1(X_2 − X_1²/t), using ∫(dθ/2π)e^{−2t(1−cos θ)}sin²θ = e^{−2t}(I_0 − I_2)(2t)/2 = j_1/(2t). The same tilt for x (intensities
e^{±iψ}): E^ψ[x_s] = 2i sin ψ s, Cov^ψ(x_s, x_r) = 2cos ψ min(s, r), so E^ψ[X_2] = −(4/3)sin²ψt³ + cos ψt² and E^ψ[X_1²] =
−sin²ψt⁴ + (2/3)cos ψt³, hence E^ψ[X_2 − X_1²/t] = (t²/3)(cos ψ − t sin²ψ) and E[X_2 − X_1²/t; x_t = 0] = (t²/3)(j_1 − t·j_1/(2t))
= (t²/6)j_1. Multiply: (t²/3)j_1². Differentiation under E is licensed by |A| ≤ (number of jumps)². (iv) The same tilt for
the fourth moment: E^θ[A⁴] = κ_1⁴ + 6κ_1²κ_2 + 3κ_2² + 4κ_1κ_3 + κ_4 with κ_r = (e^{iθ} + (−1)^re^{−iθ})X_r; the θ-integrals obey
∫e^{−2t(1−cos θ)}|sin θ|^{2k}dθ ≤ C_kt^{−k}j_0 (Laplace), so E_y[A⁴; y_t = 0 | x] ≤ Cj_0[t^{-2}X_1⁴ + t^{-1}X_1²|X_2| + X_2² +
t^{-1}|X_1X_3| + |X_4|]. On [0, t/2] the x-bridge has density p_{t/2}(x_{t/2})/p_t(0) ≤ j_0(t/2)/j_0(t) ≤ 2 (t ≥ 1; p_s(x) ≤ p_s(0)
by Fourier positivity) against the free walk, and Doob's L^p inequality bounds the free walk's sup moments by C_pt^{p/2};
time reversal covers [t/2, t]. So E[|X_r|^k; bridge] ≤ C t^{k(1 + r/2)} and every term is ≤ Ct⁴. (v) Use x²/2 − x⁴/24 ≤ 1 − cos x ≤
x²/2 and split at t_1 := 1/|φ|. On [0, t_1]: (φ²/2)∫_0^{t_1}m(t)dt/t minus a remainder ≤ (φ⁴/24)∫_0^{t_1}P(t)E_tA⁴dt/t ≤
Cφ⁴(1 + t_1²) = O(φ²) (P(t) ≤ Ct^{-2}; for t ≤ 1, P·E A⁴ = O(t⁴)). By the Bessel asymptotics j_ν(t) = (4πt)^{-1/2}(1 + O(1/t)),
m(t) = 1/(48π²) + O(1/t) for t ≥ 1 and m(t) = O(t²) for t ≤ 1, so (φ²/2)∫_0^{t_1}m dt/t = (φ²/(96π²))log t_1 + O(φ²). On
[t_1, ∞): 0 ≤ ∫_{t_1}^∞2P(t)dt/t ≤ Cφ². ∎

**Proposition GH-log (the ghost group's f² coefficient, all n): PROVEN-HERE given G-mag (vi); unconditional part (b).** **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]**
Per fine site and per positive root α, in infinite volume, G_gh,n,α(f) = ℓ^{-4}g(q_αF_n) − g(q_αf) (Lemma B-flux: D_n is the
level-n nearest-neighbour Laplacian at flux q_αF_n, a level-n site carrying ℓ⁴ fine sites). Then:
(a) the f²log|f| parts cancel exactly: (G_gh,n,α(f) − G_gh,n,α(0))/f² = −2c_gq_α²log ℓ + q_α²[c'(q_αℓ²f) − c'(q_αf)] + O_n(f²log(1/|f|));
(b) (unconditional) every limit point of the left side as f → 0 lies within 2q_α²sup|c'| of −2c_gq_α²log ℓ, for every n;
(c) given (vi) **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]**, the f² coefficient exists and equals **−2c_gq_α²log ℓ = −(q_α²/(48π²))log ℓ exactly, for every n** (no
  n-dependent remainder: S6-F3 does not occur);
(d) summed over positive roots (Σq_α² = N²) and in u-units (Δu = 2 × the f² coefficient, Lemma F-id): **β^fine[G_gh,n] =
  −(N²/(24π²))log ℓ = −(1/22)·β_0^std log ℓ**;
(e) the Cartan sector contributes nothing: there D = d at every Cartan background, and G_gh's Cartan part does not depend
  on f.
*Proof.* (a) ℓ^{-4}Ψ(qF_n) − Ψ(qf) = q²f²[(F_n/(ℓ²f))²ψ(qF_n) − ψ(qf)]; F_n/(ℓ²f) = 1 + O_n(f²) and ψ(qF_n) − ψ(qℓ²f) =
O_n(f²log(1/|f|)) (ψ' = O(1/φ) from (v)'s representation); insert (v): ψ(qℓ²f) − ψ(qf) = c_g[log(1/(qℓ²|f|)) − log(1/(q|f|))] +
c'(qℓ²f) − c'(qf). (b), (c) from (a) and (v), (vi). (d) β_0^std = 11N²/(12π²) (§0), and 2·(1/48π²)/(11/(12π²)) = 1/22.
(e) §37 (C1). ∎
**[RFL6-fix S6-5] Remark ((b) suffices for UNIV).** Theorem UNIV is an O(1)-remainder statement, so the unconditional (b)
already gives what UNIV needs from G_gh: |β^fine[G_gh,n] + (1/22)β_0^std log ℓ| ≤ 4N²sup|c'| for every limit point, every n.
G-mag (vi) **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]** is needed only for "exactly, no remainder", for the existence of the coefficient as a limit, and for the
rate statements (UNIV-rate).
**[RFL6-fix S6-1] Scope.** (d) and the 1/22 / 21/22 split are statements about the δ-slice S_0 form of Γ^{W0}_n (Lemma GH).
They apply to the tower's own gauge fixing because (a3) ≡ 0 at critical backgrounds (Lemma FP-exact, §52, session 7,
unreviewed); before §52 they were conditional on it.
*Reading.* (1) This is the first root-sector piece of the universal coefficient computed exactly at finite n. Its share,
1/22, is the share of the Landau-gauge ghost in the continuum decomposition (heat-trace B²t² coefficients per q²: Landau
transverse vector R_V − R_S = 10/3 + 1/6 = 7/2, Landau ghost −R_S = 1/6, total 11/3; and (1/6)/(11/3) = 1/22).
**[RFL6-fix S6-5] Convention (REVIEW_FLOW_S6 §4.4).** The share is for background-field Landau-type (orthogonal-slice,
δ(D^*a)) bookkeeping: the δ-function Jacobian det(D^*D)^{-1/2} times the FP determinant det(D^*D) leaves a net ghost
−½log det_R(D^*D) = −log det_C(D^*D), i.e. −R_S = +1/6 per q², and the transverse part ½log det_⊥V = ½log det V − ½log det Δ
carries R_V − R_S = 7/2. In background-field Feynman bookkeeping, Γ = log det_C V − 2log det_C(−D²), i.e. R_V − 2R_S = 11/3,
the ghost share is (1/3)/(11/3) = **1/11** (the folklore "−1/3" is the diamagnetic total, vector orbital −2/3 plus ghost
+1/3, not the ghost alone). Only the total 11/3 is gauge invariant; the share is a convention. Here the Landau grouping is
the one forced by IR safety: the Feynman-type "ghost" ½log det D_n^*D_n − log det D_0^*D_0 would have f²log(1/f) coefficient
c_gq²(1 − 2) ≠ 0, so 1/11 never appears as an IR-safe group in this construction. G_gh is exactly Landau-type (its fine
piece is −½log det_R(D_0^*D_0), once complex per root), and G_⊥'s fine piece is the operator on ker D_0^* (Landau
transverse; in Feynman form ½log det O^♯ − ½log det'Δ_0, i.e. R_12 + R_S = R_V − R_S), so 1/22 and the 21/22 required of
G_⊥ are in the same convention and add to the invariant total. (2) The mechanism is exact scaling: the same lattice function g at the two levels, the level-n flux being
exactly ℓ² times the fine flux to first order; the IR singularities f²log f cancel identically and the log ℓ is the
scale ratio. No momentum-space residue estimate is needed for this group. (3) IR safety (target S6-1): G_gh is IR safe
(given (vi)); G_⊥ = (Γ^{W0}_n + Γ^cov_n) − G_gh is IR safe because the total has a C² density (§45). S6-F1 does not occur.
**[RFL6-fix S6-4] (3) is REPLACED by:** G_gh is IR safe given (vi) **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]** (without (vi), limit points within 2q²sup|c'|, (b)).
"G_⊥ := total − G_gh" is a definition; the content is that the explicit formula holds on the dense flux set (COV-GI-∞).
G_⊥'s fine term ½log det_{ker D_0^*}(H + M^TΠM) is IR safe directly (REVIEW_FLOW_S6 §3.2): in an orthonormal basis of S_0
adapted to S_0 = S' ⊕ J(Λ_n^♮), (H + M^TΠM)|_{S'} is the Schur complement onto S' of A = (H + M^T𝒞^{-1}M)|_{S_0} (this is
the content of COV-GI (iii)-(iv) in block form), and a Schur complement of A obeys ⟨x, A/A_{22}x⟩ = min_y⟨(x, y), A(x, y)⟩ ≥
λ_min(A)||x||² ≥ (c_n/2)||x||² (Lemma N-f); so it is the density of a gapped covariant operator, C² by Lemma MS. G_⊥'s level-n group
½log det_⊥(P_⊥𝒞_nP_⊥) = ½log det 𝒞_n − ½log det 𝒞^♭_G involves 𝒞^♭_G compressed to the non-local G = Ran D(B); its
density is not of MS type and **its IR safety in the root sectors is OPEN, part of (s2⊥)**.

## 45. Magnetic calculus, (N) at U_f, and (COV-GI-∞) (target S6-2 (b), (c))

**Lemma MS (covariant operators at constant Cartan curvature): PROVEN-HERE.** Let Γ := ℓZ⁴ and fix f. Magnetic
translations W_f(γ), γ ∈ Γ (translation by γ composed with the Cartan gauge transformation that restores U_f), act on E and
on all fine and level-n field spaces; on the root sector α they obey W(γ)W(γ') = e^{iq_αfγ∧γ'/2}W(γ + γ') in the symmetric
gauge about a level-n site (γ∧γ' := γ_1γ'_2 − γ_2γ'_1), on the Cartan sector they commute. Let K be an operator on
ℓ²(E) commuting with every W_f(γ) (every operator built covariantly from U_f by the constructions of this lane does: H, D_0,
E', M, 𝒞_n, Π, P_⊥, slices). Then:
(i) in the symmetric gauge K has the kernel K(γ + u, γ' + u') = e^{iq fγ∧γ'/2}κ(γ − γ')_{uu'} (u, u' cell indices, q the charge
  of the sector), κ : Γ → End(cell space), and products correspond to the twisted convolution
  (κ_1⋆_fκ_2)(γ) = Σ_{γ'}e^{iqfγ'∧γ/2}κ_1(γ')κ_2(γ − γ'); τ(K) = tr κ(0);
(ii) (Combes-Thomas, uniform in f) if K = K^* ≥ c > 0 and |κ(γ)| ≤ C_Ke^{−m|γ|}, then K^{-1} and log K have kernels bounded by
  C'e^{−m'|K-distance|} with m', C' depending only on (c, C_K, m) (the phases have modulus 1 and do not enter);
(iii) if moreover κ = κ_f depends on f in a C² way with |∂_f^jκ_f(γ)| ≤ C_Ke^{−m|γ|} (j ≤ 2) and K_f ≥ c on |f| ≤ f_1, then
  ρ(f) := τ(log K_f) is C² on |f| < f_1, and its derivatives are given by differentiating under the sums: every
  f-derivative of a twist produces a factor iqγ∧γ'/2 with |γ∧γ'| ≤ |γ||γ − γ'|, which the exponential decay of all factors
  absorbs;
(iv) (the β link) if K_f = K(U_f) for a covariant construction U ↦ K(U) whose cell density ρ_0(U) := (log K(U))_{00}
  (cell trace at the origin cell, symmetric gauge) has an exponentially decaying Hessian at U = 1, then
  ρ''(0) = D²ρ_0(1)[H_1a^sym, H_1a^sym] summed over translates, which is H_0(𝓛Φ, 𝓛Φ) in Lemma F-id with 𝓛Φ = H_1a^sym; hence
  twice the f² coefficient of ρ per fine site is β^fine (F-id, extended to exponentially decaying Hessian kernels by
  F-Π (ii)). **[RFL6-fix S6-3] The extension is now written: Lemma F-id-exp (§51), a homotopy (cone) Poincaré lemma with
  exponential weights; it replaces "extended … by F-Π (ii)".**
*Proof.* (i) Commutation with W(γ) gives K(γ + u, γ' + u') = (phase)·K(u, γ' − γ + u') with the phase of the cocycle; the
product rule is the composition of kernels with the cocycle identity. (ii) Conjugate by e^{η·x}: the conjugated K differs
from K by Σ_γ|κ(γ)|(e^{|η||γ|} − 1) ≤ c/2 for |η| ≤ η_0(C_K, m, c), so it is invertible with norm ≤ 2/c, which is the kernel
bound for K^{-1}; log K = ∫_0^∞[(1 + s)^{-1} − (K + s)^{-1}]ds with the same bound for each resolvent (gap c + s).
(iii) ρ'(f) = τ(K_f^{-1}∂_fK_f) and ρ'' are finite sums of cell traces of products of K_f^{-1} and of ∂_f^jK_f (j = 1, 2),
whose kernels are those of (ii) times polynomials in the cell coordinates of degree ≤ 2 per derivative; the traces at the
origin cell converge absolutely and uniformly in f, which licenses differentiation (dominated convergence). (iv) In the
symmetric gauge about the origin cell, U_f = exp(fH_1a^sym) exactly, so ρ(f) = ρ_0(exp(fH_1a^sym)); differentiate twice at 0
(DF(1) = 0 by Lemma U-tad (i)); the Hessian sum converges because a^sym grows linearly and the Hessian of ρ_0 decays
exponentially; this is the per-site evaluation on 𝓛Φ of F-id's proof. ∎

Define, for U in the small-curvature class 𝒦_n (configurations that are, on every ball of radius ρ_n larger than all ranges
of the level-n constructions, gauge equivalent to a configuration in fix S4-2b's 𝒰_n; U_f ∈ 𝒦_n for |f| ≤ ε_0L^{-2n}),
  Ã(U) := H(U) + M(U)^T𝒞_n(U)^{-1}M(U) + D_UE'D_U^*  on all of E.
**(L-loc)** There are C_n, m_n > 0 with |Ã(U)(b, b')| ≤ C_ne^{−m_nd(b,b')} and |∂_cÃ(U)(b, b')| ≤ C_ne^{−m_n(d(b,c) + d(c,b'))} for all
U ∈ 𝒦_n and links b, b', c (∂_c the derivative in the exponential chart at U_c; operator norms of su(N) blocks). [ARGUED:
H, D_U, E' are finite range and polynomial in the links; M = D𝔪_n and 𝒞_n are finite range and analytic on 𝒦_n (COV-str
(iii), read on 𝒦_n: the constructions are local, so analyticity is a local property); 𝒞_n ≥ κ^{-1}π_+^{-1} (the j = n term),
so 𝒞_n^{-1} is exponentially local by Combes-Thomas and ∂_c𝒞_n^{-1} = −𝒞_n^{-1}(∂_c𝒞_n)𝒞_n^{-1} with ∂_c𝒞_n supported near c.]
**[RFL6-fix S6-2] (L-loc) is too weak for its use** (Corollary COV-GI-∞ applies Lemma MS (iii), which needs j ≤ 2, and in
the symmetric gauge ∂_f²κ_f involves second link derivatives weighted by a^sym_c a^sym_{c'}). **Restated as (L-loc2):**
(L-loc) plus |∂_c∂_{c'}Ã(U)(b, b')| ≤ C_ne^{−m_n(d(b,c) + d(c,c') + d(c',b'))} for all U ∈ 𝒦_n and links b, b', c, c', and the
same three bounds for 𝒞_n(U) (and hence, by the resolvent identity, for 𝒞_n(U)^{-1} and Δ'(U)). [ARGUED, as (L-loc): the
argument above (finite range and polynomial for H, D_U, E'; finite range and analytic on 𝒦_n for M and 𝒞_n; Combes-Thomas
for 𝒞_n^{-1}; ∂_c∂_{c'}𝒞_n^{-1} = 𝒞_n^{-1}(∂_c𝒞_n)𝒞_n^{-1}(∂_{c'}𝒞_n)𝒞_n^{-1} + (c ↔ c') − 𝒞_n^{-1}(∂_c∂_{c'}𝒞_n)𝒞_n^{-1}, with ∂_c∂_{c'}𝒞_n
nonzero only for c, c' within the range of 𝒞_n) gives the second derivatives equally; a statement fix, not a new obstacle.]
Lemma N-f uses first derivatives only, so it holds given (L-loc); Corollary COV-GI-∞ needs (L-loc2).

**Lemma N-f ((N) at U_f with a T-uniform gap): PROVEN-HERE given (L-loc)** [Lemma S-all, COV-GI proof (3), the (N)
argument of §36].
(i) At critical U ∈ 𝒦_n, Ã(U) = A|_{S_0} ⊕ (D_UE'D_U^*)|_{D_UΛ'} for E = S_0 ⊕ D_UΛ', and the second block is ≥ γ_n (§42). So (N)
  for S_0 ⟺ Ã(U) > 0 on S_0.
(ii) Ã(1) ≥ c_n > 0 in infinite volume, hence on every torus of side a multiple of ℓ.
(iii) Ã(U_f) ≥ c_n − C'_n|f|^{2/3} in infinite volume and on every flux-quantised torus of side ≥ 4|f|^{-1/3} commensurate with
  ℓ, with C'_n depending only on (L-loc)'s constants. Hence for |f| ≤ ε_n := min{ε_0L^{-2n}, (c_n/(2C'_n))^{3/2}}, **(N)
  holds at U_f with gap ≥ c_n/2, uniformly in T** (S6-F4 does not occur at fixed n).
*Proof.* (i) A kills D_UΛ' at critical U (HD_U = 0, MD_Uρ = D ev ρ = 0) and is symmetric, so it maps into (D_UΛ')^⊥ = S_0;
D_UE'D_U^* kills S_0 = ker E'D_U^* and on D_Uρ gives ⟨D_Uρ, D_UE'D_U^*D_Uρ⟩ = ||Δ'ρ||² ≥ γ_n||D_Uρ||² (§42 (ii)).
(ii) Ã(1) is ℓZ⁴-periodic with an exponentially decaying kernel, so it is a direct integral of finite matrices Ã(θ) over
the Bloch torus θ ∈ [0, 2π)⁴, continuous in θ. Each Ã(θ) > 0: if ⟨X, Ã(θ)X⟩ = 0, write X = s + D_0ρ; then Δ'ρ = 0, so ρ = 0,
and ⟨s, Hs⟩ = 0 = ⟨Ms, 𝒞^{-1}Ms⟩. Per colour H = d^*d at 1, so s is closed: s = dλ + h with h a θ-twisted harmonic form
(h constant for θ = 0, h = 0 otherwise). Ms = d_n ev λ + Mh = 0. For θ ≠ 0, d_n ev λ = 0 with twisted boundary conditions
forces ev λ = 0; for θ = 0, FLOW's argument (M maps constants to nonzero constants) gives h = 0 and ev λ constant; in both
cases λ ∈ Λ' (+ const), s ∈ D_0Λ' ∩ S_0 = {0}. Compactness and continuity give c_n := min_θλ_min(Ã(θ)) > 0; a commensurate
torus samples finitely many θ. (iii) IMS localisation: a partition of unity Σ_jχ_j² = 1 by functions supported in balls B_j of
radius 2R about a grid of centres c_j (spacing R), with |χ_j(b) − χ_j(b')| ≤ Cd(b, b')/R and bounded overlap, gives
Ã = Σ_jχ_jÃχ_j + E_IMS, E_IMS(b, b') = −½Ã(b, b')Σ_j(χ_j(b) − χ_j(b'))², so ||E_IMS|| ≤ C_1/R² by (L-loc). For each j, gauge
covariance moves U_f to the symmetric gauge about c_j, U^{(1)} := exp(fH_1a^{sym,c_j}) with |a^{sym,c_j}_c| ≤ |c − c_j| + 1; the
family U^{(s)} := exp(sfH_1a^{sym,c_j}), s ∈ [0, 1], lies in 𝒦_n (constant curvature sf). For φ supported in B_j,
|⟨φ, (Ã(U^{(1)}) − Ã(1))φ⟩| ≤ |f|Σ_{b,b'∈B_j}|φ_b||φ_{b'}|∫_0^1ds Σ_c|∂_cÃ(U^{(s)})(b, b')|(|c − c_j| + 1), and with |c − c_j| ≤ 2R + d(b, c)
and (L-loc), Schur's test bounds this by C_2|f|(R + 1)||φ||². Hence ⟨χ_jψ, Ã(U_f)χ_jψ⟩ ≥ (c_n − C_2|f|(R + 1))||χ_jψ||²; summing,
Ã(U_f) ≥ c_n − C_2|f|(R + 1) − C_1R^{-2}; take R = |f|^{-1/3}. On a torus the same argument runs ball by ball (the balls embed
when the side is ≥ 4R), with (L-loc) on the torus. ∎

**Corollary COV-GI-∞: PROVEN-HERE given (L-loc) (and G-mag (vi) **[RFL8-fix S8-6: (vi) PROVEN-HERE, §58]** for the existence of the root-sector group
coefficients).** **[RFL6-fix S6-2] Read "given (L-loc2)" (the C² step through Lemma MS (iii) needs second derivatives) and
"MS (iv) with Lemma F-id-exp (§51)" throughout this corollary and its uses in §48-§49.** For each n and 0 < |f| ≤ ε_n with q_αℓ²f ∈ 2πQ for all α (a dense set), (S) and (N) hold at U_f
fibrewise in the Bloch decomposition with respect to a sublattice of commuting magnetic translations, with gaps γ_n and
c_n/2 independent of the fibre; Lemma COV-GI and Lemma GH hold fibrewise (they are finite-dimensional algebra, and every
operator involved commutes with the magnetic translations), so they hold between infinite-volume per-cell densities. The
left side, written as ½log det Ã − log det Δ' + ½log det 𝒞_n (by (i) of Lemma N-f and §43 (iii)), is a sum of densities of
gapped covariant operators satisfying Lemma MS (ii)-(iii): it is C² in f on |f| < ε_n, and twice its f² coefficient per
fine site is β^fine[Γ^{W0}_n + Γ^cov_n] (MS (iv)). On the right side G_gh,n is given by Proposition GH-log and
G_⊥,n = (left side) − G_gh,n. (Root-sector fibres of the massless Laplacians may have isolated zero modes; they are a null
set of the Bloch integral, and the identity holds with det' there.) Hence **the β-reduction of §36 Reading (b) is now
unconditional at each fixed n, given (L-loc2)** **[RFL7-fix S7-5: was "given (L-loc)"]**:
  β^fine[Γ^{W0}_n + Γ^cov_n] = 2(c^⊥_n + c^gh_n),  c^gh_n = −(N²/(48π²))log ℓ (all n),  c^⊥_n := the f² coefficient of G_⊥,n
(per fine site, summed over the root sectors; the Cartan sector contributes to c^⊥_n only through COV-⊥-C's bounded,
convergent c^⊥ and its Cartan Wilson part, neither of which has a log ℓ).
*Reading.* (1) What (COV-GI-∞) needed (REVIEW_FLOW_S5 §2.2) was (S) at U_f (§42), (N) at U_f with a T-uniform gap (Lemma
N-f, at |f| ≤ ε_n, an n-dependent window: harmless for β, which is a second derivative at f = 0 at each n, as fix S4-2b
already says), and a C² density with the F-id link (Lemma MS (iii)-(iv)). (2) Consistency with the Nielsen-Olesen
instability: H|_{ker D_0^*} at U_f has eigenvalues down to about −|q_αf| in the root sectors (the spin-aligned lowest Landau
level); Lemma N-f says the IR term lifts them as long as |f| ≲ c_n^{3/2}, so the f² coefficient sees no instability.

## 46. The transverse group: what it must give and what remains (target S6-3, remainder)

**Required value.** In the continuum (Landau-gauge bookkeeping, heat-trace units per q_α² per unit of 2log ℓ/(16π²)): the
Feynman vector −D²δ_μν + 2iq F_μν has heat-trace density (16π²t²)^{-1}(Bt/sinh Bt)(2 + 2cosh 2Bt), whose B²t² coefficient
is R_V = 4 − 2/3 = 10/3 (spin +4, orbital 4 × (−1/6)); the scalar has R_S = −1/6. Landau transverse = R_V − R_S = 7/2,
ghost (Landau, ½ of the real FP determinant, i.e. once complex) = −R_S = 1/6, total 11/3. Hence, for the total to be
universal, **c^⊥_n = −(21N²/(48π²))log ℓ + O(1), i.e. β^fine[G_⊥,n] = −(21/22)β_0^std log ℓ + O(1)**, with the Cartan sector
contributing O(1) **[RFL6-fix S6-1] (for the tower's own fixing, via (a3) ≡ 0, Lemma FP-exact §52)**. Equivalently, in the Feynman form (§43 (v)) the total root-sector log coefficient is set by the
plane-12 vector block alone: with K_F := H + D_0D_0^* at U_f, its components 3, 4 are scalars (the cross terms between the
plane 12 and the directions 3, 4, and within 34, cancel between H and D_0D_0^* because those planes are flat), so
R_V^{4D} = R_12 + 2R_S and R_V − 2R_S = R_12, whose continuum value is 2·(−1/6) + 4 = 11/3.

**What remains (OPEN, named).**
- **(V-heat)** Lattice universality of the vector heat trace: for K_F (SU(N) Wilson Hessian + D_0D_0^* at U_f, root sector α),
  R_12^lat(t) := [f² coefficient of the complex plane-12 heat trace]/(q_α²t²j_0(t)²) → 11/3 as t → ∞, at rate O(1/t). [The
  scalar analogue is Lemma G-mag (iii): R_S^lat(t) = −(1/6)(j_1/j_0)² → −1/6 exactly at rate O(1/t).] Route: the tilt method
  of G-mag (iii) with the spin term as a matrix weight on the walk; or a magnetic U-Tay. f9 (V) tests it numerically.
- **(V-IR)** The IR term and the level-n transverse covariance act on G_⊥ as a proper-time cutoff at t ≈ ℓ²:
  c^⊥_{n,α} = −(q_α²/(16π²))∫_1^{ℓ²}(R_12^lat(t) + R_S^lat(t))dt/t + O(1), uniformly in n (R_12 + R_S = R_V − R_S, the Landau
  transverse coefficient; with (V-heat) this is −(q_α²/(8π²))(7/2)log ℓ + O(1) = −(21q_α²/(48π²))log ℓ + O(1)). This is the remaining content of (R3) (the magnetic symbol calculus for P_⊥(B) on the
  transverse group only: P_⊥ = 1 − D(D^*D)^{-1}D^* is non-local, but inside G_⊥ it is paired with the transverse IR term) and
  of (U-IR) (a2), (a4') in transverse form. It needs (R1) (the root-sector GS-1 analogue: an estimate, not an identity,
  PROOF l.2148-2150) and (R2).
- (U-IR)(a3) (the slice's own normalisation against S_0's exact Jacobian), (b), (s1), (s2⊥) in the root sectors: unchanged.
  **[RFL6-fix S6-1] (a3) is not "unchanged": it is RETIRED and replaced by the statement "(a3) ≡ 0 at critical
  backgrounds" (exact FP of the tower slice), Lemma FP-exact (§52, session 7). (b), (s1), (s2⊥) in the root sectors stay
  OPEN; (s2⊥) includes the IR safety of the root-sector level-n ⊥ group (fix S6-4).**
*Reading.* After session 6 the root-sector problem is split into an exactly solved scalar part (share 1/22, every n) and a
vector part whose required value is pinned (21/22) and whose two inputs (V-heat), (V-IR) are stated on explicit operators.
The Cartan sector carries no log ℓ (§37 fix S5-5, §44 (e)).

## 47. Session-6 checks (ADDED AFTER the run; checks/f9_criteria.md, f9_root_sector.py, f9_out.txt, f9_time.txt)
Criteria written 05:27:55 UTC before any f9 script (stat in FLOW_LOG); smoke test in the scratchpad (reduced sizes), no
change after it. Official f9: one NUMERIC LOCK acquisition 05:32:23-05:32:39 UTC, nice 10, 1 thread, load 5.25, memory free
43%; 15.3 s, peak RSS 665 MB. **24/24 verdict lines PASS; both controls fail as required.**
- **G0 (Lemma GH), charge-1 tori 9² and 3⁴ with one flux quantum, ℓ = 3:** ||J^*J − 𝒮||/||𝒮|| ≤ 1.0e-15; |log det Δ_0 −
  log det Δ' − log det 𝒮| ≤ 5.6e-14; ||P_{S_0} − P_J − P_{ker D_0^*}|| ≤ 3.5e-15. Control (non-orthogonal slice): 1.6e-2,
  5.8e-3 (fails as required).
- **G1 (G-mag (iii)), 2D open box 81²:** the φ² coefficient of the diagonal heat kernel equals −(t²/6)j_1(t)² to ≤ 6.1e-8
  relative at t = 0.5, …, 16 (finite-difference Richardson; independent of the tilt derivation).
- **G2 (G-mag (v), (vi)), rational flux 2π/Q, Q = 16, …, 512:** slope of ψ against log(1/φ) over the three smallest φ:
  0.99685 c_g. c'(φ) = 1.4294e-3, 1.4092e-3, 1.3980e-3, 1.3921e-3, 1.3890e-3, 1.3874e-3; increments −2.0e-5, −1.1e-5,
  −5.9e-6, −3.1e-6, −1.6e-6 (ratios → 0.51, i.e. c'(φ) = c'_0 + O(φ), c'_0 ≈ 1.3859e-3 by a geometric tail). Accuracy
  (K-grid, du) ≤ 8e-15. This is numerical evidence for the ARGUED item (vi), not a proof.
- **G3 (Proposition GH-log):** ℓ = 3: Δ_3/(−2c_g log 3) − 1 = −1.6e-2, −8.8e-3, −4.6e-3 at Q' = 16, 32, 64 (decreasing like φ);
  ℓ = 9 (informational, level flux 2π/4 and 2π/8, not small): −2.8e-2, −1.7e-2.
- **V0 (SU(2) Wilson, 4D torus (6, 6, 3, 3), f = 2π/36):** gradient ≤ 1.0e-15 (U_f critical); max|HD_0| = 1.1e-15 against
  max|H| = 6 (HJ = 0 in all sectors, now tested in a non-abelian group, where it is not a tautology); K_FD_0 = D_0Δ_0 to
  1.8e-15; the Cartan-root block of H is 0; the §46 decomposition K_F = [K_12 ⊕ Δ^{(12)}] ⊗ 1 + 1 ⊗ Δ_34 holds to 8.9e-16 (3888
  dof). Control (f = 1.3 quanta, one defect plaquette): gradient and HD_0 both 1.22 (fail as required).
- **V1 (scalar calibration, 2D box 101², root block of the adjoint Laplacian, q = 2):** f² coefficient = −½q²(t²/3)j_1² to
  ≤ 2.7e-7 relative, t = 2, …, 24.
- **V2 ((V-heat)), same box, root block of K_12:** normalisation exact (4.4e-16). R_12(t) = 3.4742, 3.5463, 3.5786, 3.6091,
  3.6239, 3.6384, 3.6456, 3.6527 at t = 2, 3, 4, 6, 8, 12, 16, 24; fit R_∞ + a/t + b/t² on t ≥ 6: **R_∞ = 3.66662** (11/3 =
  3.66667; a = −0.332), on 4 ≤ t ≤ 16: 3.66649. Reported: R_V^{4D}(24) = 3.3263 (→ 10/3), (R_12 + R_S)(24) = 3.4895 (→ 7/2).
- **V4 (Cartan block):** R_C(t) = 0.137, …, 8.7e-4 at t = 2, …, 24, with t²R_C(t) ≈ 0.50-0.55 throughout: R_C ~ 1/(2t²), no
  constant, so no log ℓ from the Cartan sector.
- **Reading (per the rule).** (1) The PROVEN-HERE identities of §42-§44 (G0, G1, V1) and the SU(2) structure facts behind
  §46 (V0) hold to round-off; the controls fail. (2) G2a, G3a confirm Lemma G-mag (v) and Proposition GH-log
  numerically; G2b is consistent with (vi) at rate O(φ). (3) V2 is strong numerical evidence for (V-heat): the lattice
  plane-12 vector heat-trace coefficient approaches the universal 11/3 at rate O(1/t), so with the Feynman-form
  bookkeeping of §46 the total root-sector proper-time coefficient (R_V − 2R_S = R_12) is universal. It is evidence, not a
  proof, and it does not test (V-IR) (the IR term, the level-n covariance, the S4' contours are absent from V). (4) What
  f9 is: lattices with constant Cartan curvature (a 4D torus for V0; 2D boxes and infinite-volume Bloch sums for G1-G3,
  V1-V4, the reduction to 2D being exact by V0e and §46), not the full COV-GI right side on small 4D tori with the actual
  averaging maps; that is not feasible at < 1 GB for n ≥ 2 and is not claimed.

## 48. Session-6 outcomes against §41 (ADDED AFTER the derivations and checks)
- **Step 1 (fixes): DONE.** S5-1..S5-5 applied in place, tagged [RFL5-fix] (19 tags): (s2) → (s2⊥); UNIV proof re-split and
  J_n redefined with O^♯_n; two 𝒰_n qualifiers; "+ const" reconciled; (S) at every background; (N) at U_f; F-id cited for
  the β reduction; (COV-GI-∞) recorded as OPEN in §36, §39, §40 (and now supplied by §45, given (L-loc)); A0 tautological in
  U(1); "NOT n-uniformly bounded" narrowed (n ≤ 3, ratio 0.81); B4 non-diagnostic; the Cartan sector carries no universal
  log; (R1)-(R4) listed; the IR caution.
- **S6-1 (IR-safe grouping): DONE.** With the orthogonal slice S_0 (Lemma S-all: (S) at every background), the COV-GI
  ghost-like determinants combine exactly into the full fine Landau ghost (Lemma GH: J^*J = 𝒮, Δ_FP = det(Δ')^{1/2},
  S' = ker D_0^*), and the right side regroups as G_⊥ + G_gh. Both groups are IR safe (G_gh given (vi); G_⊥ because the
  total is C²). S6-F1 does not occur. **[RFL6-fix S6-4] Replace "G_⊥ because the total is C²" by: G_⊥'s fine term is a
  gapped covariant density (Schur complement ≥ λ_min(A) ≥ c_n/2, §44 Reading (3) as fixed); the level-n ⊥ group's IR
  safety in the root sectors is OPEN, part of (s2⊥). [RFL6-fix S6-1] The regrouping applies to the tower's fixing because
  (a3) ≡ 0 (Lemma FP-exact, §52).**
- **S6-2 (magnetic calculus): DONE in the scalar sector, structural elsewhere.** Lemma G-mag (exact Feynman-Kac area
  representation, the exact second moment (t²/3)j_1² by a Poisson tilt, c_g = 1/(96π²) = the Landau value; S6-F2 does not
  occur); Lemma MS (twisted convolution over ℓZ⁴, uniform Combes-Thomas, C² densities, the F-id link); Lemma N-f ((N) at
  U_f, gap c_n/2, uniformly in T, for |f| ≤ ε_n; S6-F4 does not occur at fixed n) and Corollary COV-GI-∞, given (L-loc).
- **S6-3 (the f² log ℓ coefficient): PARTIAL.** The ghost group is solved exactly for every n: β^fine[G_gh,n] =
  −(N²/(24π²))log ℓ = −(1/22)β_0^std log ℓ (given (vi); within 2N²sup|c'| unconditionally); S6-F3 does not occur. The Cartan
  sector contributes no log ℓ (D = d; f9 V4). The transverse group must give −(21/22)β_0^std log ℓ + O(1); its inputs are
  (V-heat) (f9 V2: R_∞ = 3.66662 against 11/3; S6-F5 not observed) and (V-IR), both OPEN. **[RFL6-fix S6-1] The 1/22 and
  21/22 statements hold for the tower's own fixing given (a3) ≡ 0, now Lemma FP-exact (§52, session 7, unreviewed).
  (V-heat): see Theorem V-heat (§53, session 7).**
- **Theorem UNIV now:** conditional on (U-IR) (a2) and (a4') in transverse form, which are now exactly (V-IR) for the
  group G_⊥ (the ghost part of (a4') is discharged by Proposition GH-log, and the coarse-gauge part by COV-GI), (a3), (b),
  and on (V-heat); plus (U-IR-s) (s1) and (s2⊥) in the root sectors for the rate; (COV-GI-∞) is discharged at each n
  given (L-loc) (ARGUED). Inputs (vi) and (L-loc) are ARGUED, not proven. **[RFL7-fix S7-5] SUPERSEDED: the UNIV condition
  list after session 7 is §55 as corrected there by [RFL7-fix S7-5], and after session 8 §62.**

## 49. Tally after session 6 (FLOW.md items; session-6 items unreviewed)
- **PROVEN-HERE: 29 (sessions 1-5, as confirmed by REVIEW_FLOW_S5) + 8 (session 6) = 37.** Session 6: Lemma S-all; Lemma
  GH (given COV-GI, (N)); Lemma B-flux; Lemma G-mag (i)-(v); Proposition GH-log ((b) unconditional, (c)-(d) given G-mag
  (vi)); Lemma MS; Lemma N-f (given (L-loc)); Corollary COV-GI-∞ (given (L-loc), and (vi) for the root-sector group
  coefficients). Upstream inputs used: Lemma COV-GI (iii) and its proof (3), (9); Lemma COV-str (iii) and fix S4-2b; §30's
  colour reduction; §37 (C1)-(C3); Lemma F-id, Lemma F-Π (ii), Lemma U-tad (i); B_4 covariance of the S4' family.
- **ARGUED, not counted:** G-mag (vi) (invariance principle for the bridge area; f9 G2b consistent); (L-loc) (exponential
  locality of Ã(U) on 𝒦_n).
- **GAP:** Corollary UNIV-rate (unchanged).
- **WRONG as stated, superseded:** Lemma F-split; the session-3 sentence; F-mono's clause 3 (corrected); (COV-NA) as a
  target; (s2) on β[Γ^cov_n] (replaced by (s2⊥), fix S5-1).
- **IMPORTED-AND-REVERIFIED:** L4b — 1. Imported from EXISTENCE (PROVEN there): GS-1, GS-2 (e).
- **OPEN:** (V-heat) [s] (strong numerical evidence, f9 V2); (V-IR) [s-P] (= the transverse-group content of (R3) and of
  (U-IR) (a2), (a4')); (R1) root-sector GS-1 analogue (an estimate, PROOF l.2148-2150) [s]; (R2) [s]; (U-IR) (a3) [s-P], (b)
  [s]; (U-IR-s) (s1) [s-P], (s2⊥) in the root sectors [s-P]; (COV-GI) at non-critical backgrounds (remainder) [s]; the
  RLARGE requirement FI-1 [cross-lane]; HIST's restatement of CL^J's Setting [cross-lane].
- **Checks:** f9 (G0, G1, G2-acc, G2a, G2b, G3a, V0a-V0e, V1, V2-norm, V2a, V2b, V4 PASS; G0-ctl, V0-ctl fail as required).
- **[RFL6-fix] Status after REVIEW_FLOW_S6 (binding; the session-7 tally is §56).** Confirmed: 37 PROVEN-HERE, with scope
  annotations: GH is an identity for the δ-slice S_0 form (its use for the tower needs (a3) ≡ 0: Lemma FP-exact, §52);
  GH-log (c), (d) given (vi), (a), (b), (e) unconditional; MS (iv) given the F-id extension (now Lemma F-id-exp, §51);
  N-f given (L-loc); COV-GI-∞ given (L-loc2) (not (L-loc)) and (vi). In the OPEN line above: (U-IR)(a3) is RETIRED in
  favour of "(a3) ≡ 0" (§52); add (L-loc2) [s] (ARGUED) and the IR safety of the root-sector level-n ⊥ group [s-P]
  (part of (s2⊥)).

---
## 50. Session-7 targets and PRE-STATED (session 7) lemmas (written 2026-10-28 ~06:00 UTC, before any session-7 proof, criteria file or script)

Binding input: REVIEW_FLOW_S6.md. Its fixes S6-1..S6-5 are applied in place and tagged **[RFL6-fix]** (step 1, done
before this section; 19 tagged lines). Outcomes are in a later section, added afterwards. Setting and notation of §41-§46.

**PRE-STATED (session 7).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Proofs follow in §51-§53; any change of a statement after this point is logged as such.

**(P1) Lemma F-id-exp (fix S6-3).** Let ρ_0 be a gauge-invariant C² function of the links of Z⁴ near U = 1, with Dρ_0(1) = 0
and a Hessian kernel h(b, b') := ∂_b∂_{b'}ρ_0(1) (one colour, after F-Π (i)) obeying Σ_{b,b'}|h(b, b')|e^{m(|b| + |b'|)} < ∞ for
some m > 0 (|b| the distance of b from the origin). Let F := Σ_xτ_xρ_0 (translation sum; B_4-covariant after the orbit
sum) and β[F] its p²-coefficient (Def. of §0). Then H_0 := D²ρ_0(1) extends to polynomially growing 1-forms, is invariant
under A ↦ A + dλ for polynomially growing λ, and H_0(A, A) = h_0(dA, dA) with a plaquette kernel h_0 obeying
Σ_{p,p'}|h_0(p, p')|e^{m'(|p| + |p'|)} < ∞ for every m' < m; consequently the conclusion of Lemma F-id holds:
H_0(𝓛Φ, 𝓛Φ) = β[F]·φ² for the constant-curvature reference field 𝓛Φ (curvature φ in the plane 12, after the B_4 orbit sum),
i.e. twice the f² coefficient of the per-site density is β.

**(P2) Lemma FP-exact (fix S6-1; "(a3) ≡ 0").** Let U_0 be a critical point of the level-n tower action at V = 𝔪_n(U_0)
(so that its Hessian Q at U_0 obeys QD_0ρ = 0 for ρ ∈ Λ'), with (N) for S_0 (Q > 0 on S_0). Let χ = (h, P_resD_0^*) be the
composite covariant slice of Proposition NA-FP at U_0 (h := h^{(n)}_{U_0} : E → su(N)^{N_c} onto; Λ_res := {λ ∈ Λ' :
M^{(n)}_{U_0}λ = 0}, P_res its orthogonal projector; Γ := D_0|_{Λ'}). Put O := Q + D_0P_resD_0^*, H_0 := ker h, Π its orthogonal
projector, and
  **Δ_FP(U_0) := |det(χΓ)|·det(hh^*)^{-1/2}**  (equivalently |det χΓ| when the slice is written as the Lebesgue δ(h(A))).
Then, with no additive constant,
  ½log det(ΠOΠ|_{H_0}) − log Δ_FP(U_0) = ½log det_{S_0}(Q|_{S_0}) − ½log det Δ',
so the tower's slice functional equals the δ-slice S_0 form of Lemma GH exactly; ΠOΠ > 0 on H_0 follows from (N); and
det(χΓ) = det(M_{U_0}|_{Λ'⊖Λ_res})·det(P_resΔ'P_res|_{Λ_res}). Hence (a3) ≡ 0 at every critical background satisfying (N),
in particular at U_f in every root sector for |f| ≤ ε_n, and Lemma GH / Proposition GH-log apply to the tower's fixing.
A U_0-independent normalisation (e.g. Δ_FP(1) in place of Δ_FP(U_0)) is NOT an exact representation.

**(P3) Theorem V-heat (target of REVIEW_FLOW_S6 §10.1).** Let K_12 be the plane-12 root-sector block of K_F = H + D_0D_0^*
at U_f (complex field, root α = e_i − e_j, charge q_α, root flux φ := q_αf per plaquette), and put ρ(t) := j_1(t)/j_0(t) =
I_1(2t)/I_0(2t), γ_α := (h_i² + h_j²)/(4q_α²). Then:
(i) (structure) K_12 = C_α(φ)c^*c + S_α(φ)𝒮 + D_0D_0^* with c the transported plaquette sum, 𝒮 the plaquette spin form
  (explicit in §53), C_α = ½(cos h_iΦ + cos h_jΦ), S_α = sin h_iΦ − sin h_jΦ (Φ := f), and criticality forces S_α = 2C_αtan(φ/2);
(ii) (exact) the φ² coefficient of τ tr e^{−tK_12} is Θ_2(t) = t²(j_0 + j_1)² + (t/2)j_0j_1 + 4γ_αt j_0(j_0 − j_1) − (t²/3)j_1², so
  **R_12^lat(t) = (1 + ρ)² − ρ²/3 + ρ/(2t) + 4γ_α(1 − ρ)/t**, and for SU(2) (γ = 1/8) **R_12^lat(t) = (1 + ρ)² − ρ²/3 + 1/(2t)**;
(iii) R_12^lat(t) = 11/3 − 1/(3t) + O(t^{-2}) for every root (the O(1/t) coefficient −1/3 does not depend on γ_α), so
  (V-heat) holds with rate O(1/t); with R_S^lat = −ρ²/6 (G-mag (iii)): R_V^{4D} = R_12 + 2R_S → 10/3 and R_12 + R_S → 7/2, each
  at rate O(1/t), in closed form.

**Target S7-4 (if time).** (V-IR) in a charged-scalar model with the real averaging maps (check f10 part B).
**Check f10** (criteria file first, its stat into FLOW_LOG before any f10 script; jobs < 20 min, < 1 GB): (A) Lemma FP-exact
on small 2D charged tori with the actual axial-path slice h_U, M_U at flux (both sides to round-off; control with Δ_FP(1));
(V) Theorem V-heat: the operator identity (i) against f9's SU(2) builder (imported read-only), and the closed form (ii)
against an independent direct heat-trace computation and against f9_out.txt's printed R_12, R_S values.

**Failure modes (each a valid outcome).** (S7-F1) the tower's Δ_FP as defined in PROOF (NA-FP) is not the exact factor
(a residual U_0-dependent normalisation survives); (S7-F2) the closed form disagrees with the direct lattice heat trace
(an error in the symbol of K_12 or in the Moyal expansion); (S7-F3) the extension F-id-exp fails (a boundary term survives
for exponentially decaying kernels).

---
# Session-7 proofs (written after §50)

## 51. Lemma F-id-exp (the F-id link for exponentially decaying Hessians; fix S6-3): PROVEN-HERE

Statement: (P1) of §50.
*Proof.* (1) *Extension and gauge invariance.* For polynomially growing A, A' (|A_b| ≤ C(1 + |b|)^k) the sum
H_0(A, A') = Σ_{b,b'}h(b, b')A_bA'_{b'} converges absolutely by the weighted ℓ¹ bound. For finitely supported λ, ρ_0(e^{sλ}·U) =
ρ_0(U) and Dρ_0(1) = 0 give Σ_bh(b, b')(dλ)_b = 0 for every b' (NA-inv at the critical point 1; take A' = δ_{b'}), hence
H_0(dλ, A') = 0 for every polynomially growing A'. For polynomially growing λ put λ_R := λ·1_{|x|≤R}: dλ_R = dλ on links with
both ends in the ball, so dλ − dλ_R is supported on links with |b| ≥ R − 1, where |(dλ − dλ_R)_b| ≤ C(1 + |b|)^k
**[RFL7-fix S7-4: the former "is O(R^{k}) there" was false as written (far links carry (1 + |b|)^k, not R^k); replaced by
the bound]**: |H_0(dλ − dλ_R, A')| ≤ Σ_{|b|≥R−1}Σ_{b'}|h(b, b')|C(1 + |b|)^k(1 + |b'|)^{k'} ≤ C_εe^{−(m−ε)(R−1)}Σ_{b,b'}|h(b, b')|e^{m(|b|+|b'|)}
→ 0 ((1 + |x|)^k ≤ C_εe^{ε|x|}, 0 < ε < m). So H_0(dλ, A') = 0 for polynomially growing λ, A'.
(2) *Cone homotopy.* For a 1-form A on Z⁴ let λ_A(y) := the sum of A along the axial path P(0 → y) (directions in the order
1, 2, 3, 4; backward links with sign −). For b = (x, x + e_μ), (A − dλ_A)_b is the circulation of A around the closed loop
P(0 → x) + b − P(0 → x + e_μ). The two axial paths coincide up to the point a := (x_1, …, x_μ, 0, …, 0) (resp. a + e_μ),
then run parallel in the directions μ + 1, …, 4 to x and to x + e_μ; so the loop bounds the ladder Σ(b) := {the plaquettes
spanned by e_μ and the steps of the segment a → x}, with |Σ(b)| ≤ |x|_1 ≤ 4|b| + 4 and every p ∈ Σ(b) at distance ≤ |b| + 2
from 0. Lattice Stokes: A = K̃dA + dλ_A with (K̃F)_b := Σ_{p∈Σ(b)}ε(b, p)F_p, ε ∈ {±1}, for every A (no growth condition), and
λ_A grows polynomially when A does.
(3) *Local plaquette form.* By (1) and (2), H_0(A, A) = H_0(K̃dA, K̃dA) =: h_0(dA, dA), h_0(p, p') := Σ_{b,b'}h(b, b')ε(b, p)ε(b', p')
(sums over Σ(b) ∋ p, Σ(b') ∋ p'), and Σ_{p,p'}|h_0(p, p')|e^{m'(|p|+|p'|)} ≤ e^{4m'}Σ_{b,b'}|h(b, b')|(4|b| + 4)(4|b'| + 4)e^{m'(|b|+|b'|)}
< ∞ for m' < m.
(4) *F-id's argument.* The Hessian kernel of F = Σ_xτ_xρ_0 at 1 is Π = Σ_xτ_xhτ_x^{-1}; by (3), ⟨A, ΠA⟩ = ⟨dA, Π_0dA⟩ for
finitely supported A, with Π_0 := Σ_xτ_xh_0τ_x^{-1} translation invariant and Σ_z|Π_0(z)|e^{m'|z|} < ∞ (|z| ≤ |p| + |p'|). So
Π̃(p) = ŝ^∧(p)^†ĥ(p)ŝ^∧(p) with ĥ analytic in a strip, ĥ(0)_{ab} = Σ_{p∈plane a, p'∈plane b}h_0(p, p') (absolutely convergent);
after the B_4 orbit sum ĥ(0) = c·1 on Λ²R⁴ (absolute irreducibility, GT-lat' (ii)), so β[F] = c exactly as in F-id
(ŝ^∧(p) = O(|p|) and ĥ(p) − ĥ(0) = O(|p|), so the p² coefficient is ŝ^∧†ĥ(0)ŝ^∧). On 𝓛Φ (polynomially growing, d𝓛Φ = Φ
constant in the plane 12): H_0(𝓛Φ, 𝓛Φ) = h_0(Φ, Φ) = φ²ĥ(0)_{12,12} = cφ² by (1)-(3). The colour factor (one colour → β = 2Nc̄)
is F-id's. ∎
*The hypothesis in MS (iv).* For ρ_0(U) = (log K(U))_{00} (origin-cell trace), log K = ∫_0^∞[(1 + s)^{-1} − (K + s)^{-1}]ds and
the second link derivatives of (K + s)^{-1} are sums of products (K + s)^{-1}(∂K)(K + s)^{-1}(∂K)(K + s)^{-1} and
(K + s)^{-1}(∂∂K)(K + s)^{-1}; under (L-loc2) and Lemma MS (ii) (gap c + s) their (0, 0) kernels are bounded by
C(c + s)^{-2}e^{−m(d(0,b) + d(b,b') + d(b',0))}, integrable in s; so |h(b, b')| ≤ Ce^{−m(|b|+|b'|)} and the weighted ℓ¹ bound holds
for every m'' < m. So MS (iv) holds given (L-loc2), with F-id-exp in place of "F-id extended by F-Π (ii)". **[RFL7-fix S7-4]
Differentiating ρ_0(exp(fH_1a^sym)) twice under the infinite link sum uses these second-derivative bounds uniformly on a
neighbourhood (U_f ∈ 𝒦_n), not only at U = 1; (L-loc2) supplies them on 𝒦_n, and Lemma MS (iii)'s dominated convergence
does the rest.**

## 52. Lemma FP-exact (the tower's fixing is an exact FP representation; (a3) ≡ 0; fix S6-1): PROVEN-HERE

Statement: (P2) of §50. [Upstream: Lemma FP-ab, Proposition NA-FP (ii) for the composite slice (PROOF l.2444-2460,
l.3046-3083, read-only), Lemma S-all, NA-inv / COV-GI proof (3).]
*Proof.* (1) *Invariance.* I(A) := e^{−½⟨A, QA⟩}. QD_0ρ = 0 for ρ ∈ Λ' (HD_0 = 0 at a critical point, NA-inv; MD_0ρ = D ev ρ = 0,
COV-GI proof (1)), and Q is symmetric, so I(A + Γρ) = I(A) with Γ := D_0|_{Λ'}. Γ is injective and (ΓΛ')^⊥ = S_0 (Lemma S-all
(i), (ii)), Γ^TΓ = E'D_0^*D_0E' = Δ', and ∫_{S_0}I = (2π)^{dim S_0/2}det_{S_0}(Q)^{−1/2} < ∞ by (N).
(2) *Admissibility.* χΓ is invertible: NA-FP (ii) for the composite slice (h(D_0λ) = M_{U_0}λ − λ(c) = M_{U_0}λ on Λ', by the
composite form of NA-FP (i); then the argument of NA-FP (ii)).
(3) *FP-ab* with χ_1 = h (target su(N)^{N_c}, dimension m_1) and χ_2 = P_resD_0^* (target Λ_res, dimension m_2 = dim Λ' − m_1):
  ∫_E I(A)δ(hA)e^{−½||P_resD_0^*A||²}dA = (2π)^{m_2/2}|det χΓ|^{−1}det(Δ')^{1/2}(2π)^{dim S_0/2}det_{S_0}(Q)^{−1/2}.
(4) *Coarea for the linear constraint.* h is onto, so E = H_0 ⊕ Ran h^* orthogonally; with A = A_0 + h^*y, dA = det(hh^*)^{1/2}dσ(A_0)dy
and δ(hA) = δ(hh^*y), whose y-integral is det(hh^*)^{−1}. So for g ≥ 0, ∫_Eg(A)δ(hA)dA = det(hh^*)^{−1/2}∫_{H_0}g dσ. With
g = e^{−½⟨A, OA⟩}, O = Q + D_0P_resD_0^*, the left side of (3) is det(hh^*)^{−1/2}∫_{H_0}e^{−½⟨A_0, ΠOΠA_0⟩}dσ. It is finite by (3),
so the symmetric form ΠOΠ|_{H_0} has no nonpositive direction (a nonpositive direction makes the Gaussian integral
infinite): ΠOΠ > 0 on H_0, and the integral is (2π)^{d_0/2}det(ΠOΠ|_{H_0})^{−1/2}, d_0 := dim E − m_1.
(5) *Logarithms.* Equating (3) and (4) and taking −log:
  ½log det(ΠOΠ|_{H_0}) + ½log det(hh^*) − log|det χΓ| = ½log det_{S_0}Q − ½log det Δ' + ½(d_0 − m_2 − dim S_0)log 2π,
and d_0 − m_2 − dim S_0 = dim E − m_1 − m_2 − (dim E − dim Λ') = 0. With Δ_FP(U_0) := |det χΓ|·det(hh^*)^{−1/2} this is (P2).
(6) *Factorisation.* On Λ' = (Λ' ⊖ Λ_res) ⊕ Λ_res and target su(N)^{N_c} ⊕ Λ_res, χΓλ = (M_{U_0}λ, P_resΔ'λ) (for λ ∈ Λ',
P_resD_0^*D_0λ = P_resE'Δ_0E'λ = P_resΔ'λ since Λ_res ⊂ Λ'), and M_{U_0} vanishes on Λ_res; the block matrix is lower
triangular, so det χΓ = det(M_{U_0}|_{Λ'⊖Λ_res})·det(P_resΔ'P_res|_{Λ_res}).
(7) *(a3) ≡ 0.* The tower's slice functional at U_0 is 𝔊(U_0, 0) = ½log det(Π_{U_0}O(U_0; 0)Π_{U_0}|_{H_0(U_0)}) − log Δ_FP(U_0)
(§23.3, the 𝔊 definition, l.1115-1121 at session 8 **[RFL7-fix S7-1: was "l.1100-1103", stale]**; the covariant slice of NA-FP), O(U_0; 0) the Hessian plus the residual Feynman term, i.e. O above. By (5) it
equals ½log det_{S_0}(A) − ½log det Δ' = the δ-slice S_0 form of Lemma GH (iii) (A = Q|_{S_0}, Δ_FP^{S_0} = det(Δ')^{1/2}),
with no constant. So the difference that (a3) was introduced to control is identically 0 on every torus where (N) holds.
At U_f (|f| ≤ ε_n, Lemma N-f) every operator here (h_{U_f}, M_{U_f}, P_res, D_0, Q) commutes with the magnetic translations
(they are built covariantly from U_f), so (5) holds fibrewise in the Bloch decomposition and hence between per-site
densities, exactly as in Corollary COV-GI-∞. ∎
*Reading.* (1) **Definition (binding).** The Δ_FP(U_0) of §23.3 (l.1115-1121 at session 8; **[RFL7-fix S7-1: was "l.1100-1103",
stale]**) and of Γ^{W0}_n is read as the exact factor of (P2). **[RFL7-fix S7-1] Δ_FP(U_0) := |det χΓ|·det(hh^*)^{-1/2} is NOT
FP_U^{-1} of NA-FP (iii): FP_U normalises to ∫_{S_0}I and differs by det(Γ^TΓ)^{1/2} = det(Δ')^{1/2}, a U_0-dependent factor of
the size of β[G_gh] (reading Δ_FP := FP_U^{-1} would leave a stray +½log det Δ', whose f² coefficient per complex root is
≈ +2c_gq_α²log ℓ, cancelling β[G_gh]). The tower's object is the Haar quotient ∫_E I/vol(G_res) (vol(G_res) independent of
U_0), which is what (P2) reproduces.** In detail,
|det χ_{U_0}Γ_{U_0}| in the Lebesgue-δ convention of NA-FP (iii) (where FP_U = (2π)^{m_2/2}|det χΓ|^{−1}det(Γ^TΓ)^{1/2}), times
det(hh^*)^{−1/2} when the slice is written as a determinant on H_0 with its induced metric. Both factors depend on U_0: hh^* and
M_{U_0} are block-local (one block per level-n site; the axial paths stay in the block) but carry the block holonomies, and
**[POST-HOC correction, 06:09 UTC, after f10 A5: "hh^* … carry the block holonomies" is too broad. In d = 2 every link of a
block is reached by axial paths along a single route (the earlier moves are in the one other direction), so the
coefficients of h have holonomy-independent moduli and det(hh^*) does not depend on f (f10 A5: −27.073393 at f and at 0);
in d ≥ 3 a link in direction μ can be reached by axial orders that differ in the order of the earlier directions, whose
transports differ by plaquette holonomies, so det(hh^*) can depend on U_0 there (not checked). det χΓ does depend on U_0
already in d = 2 (f10 A5: log|det χΓ| = 149.895, 149.729 at k = 1, 3 quanta against 150.082 at f = 0); M_{U_0}'s
coefficients do too (the two axial orders to a diagonal y differ by a plaquette holonomy); which factor of (6) carries the
shift was not separated. The lemma and its proof do not use these claims.]**
P_resΔ'P_res is the gapped Dirichlet/zero-block-mean Laplacian, whose f² coefficient per complex root is ≈ +2c_gq_α²log ℓ
(REVIEW_FLOW_S6 §3.1). So a U_0-independent normalisation would shift β at the size of β[G_gh] (S7-F1 would occur for such a
fixing); with the exact factor it does not. (2) The 1/22 (G_gh) and the required 21/22 (G_⊥) therefore hold for the tower's
own fixing, not only for the δ-slice S_0 form; their remaining conditions are those of Lemma GH, Proposition GH-log
(G-mag (vi) for exactness) and COV-GI-∞ ((L-loc2)). (3) Nothing here is perturbative in f or uses the size of the block: it is
linear Faddeev-Popov algebra at a critical background (the scope of NA-FP: the Gaussian level, linear orbits).

## 53. Theorem V-heat (the lattice vector heat-trace coefficient in closed form): PROVEN-HERE

Statement: (P3) of §50. Setting: Landau gauge (θ_{x,1} = 0, θ_{x,2} = Φx_1 with Φ := f, the Cartan angle per plaquette in
the plane 12), the left chart U_b = e^{X_b}U_b^0 (X_b transforms at the tail of b; the right chart of §36 is the link-wise
unitary change X ↦ Ad(U_b^{−1})X, which leaves spectra and the diagonal heat-kernel entries unchanged), and in the root
sector α the complex coordinate w of X with Ad(e^{θH_1}) acting as e^{iq_αθ}. Link fields are indexed by their tail site, so
operators on the plane-12 root block are 2 × 2 matrices over the algebra generated by u := (shift by e_1) and v :=
(e^{iφx_1}·shift by e_2), φ := q_αΦ (root flux); vu = e^{−iφ}uv. Put ε := e^{iφ}, s := e^{iφ/2}.

*Step 1 (structure, (i)).* For the plaquette p = (x; e_1, e_2) with links b_1 = (x, e_1), b_2 = (x + e_1, e_2), b_3 = (x + e_2, e_1),
b_4 = (x, e_2): e^{X_1}U_1e^{X_2}U_2U_3^{−1}e^{−X_3}U_4^{−1}e^{−X_4} = e^{Y_1}e^{Y_2}e^{Y_3}e^{Y_4}U_p^0 with Y_1 = X_1, Y_2 = Ad(U_1)X_2,
Y_3 = −Ad(U_1U_2U_3^{−1})X_3, Y_4 = −Ad(U_p^0)X_4, and by BCH = exp(R + ½Σ_{i<j}[Y_i, Y_j] + O(Y³))U_p^0, R := ΣY_i. For root-sector
fluctuations in the block (i, j) of root α: R is supported on the entries (i, j), (j, i), so tr(RU_p^0) = 0, R² = −ν|r|²(e_ii + e_jj)
and [Y_k, Y_l] = iν'Im(ȳ_ky_l)(e_ii − e_jj) (r := Σỹ_i, ỹ_i the complex coordinates of Y_i; ν, ν' > 0 normalisations); other root
sectors and the Cartan directions decouple at second order (tr(E_βE_γU^0) = 0 unless β + γ = 0; f9 V0d). With U_p^0 =
exp(ΦH_1) (entries e^{ia}, e^{ib} on the block, a = h_iΦ, b = h_jΦ, a − b = φ) and the Wilson term κ_N Re tr(1 − U_p):
  s_p^{(2)} = C̃(cos a + cos b)|r|² + S̃(sin a − sin b)Σ_{i<j}Im(ȳ_iy_j),
with constants C̃, S̃ independent of Φ. In operator form (y_1 = w_1, y_2 = uw_2, y_3 = −εvw_1, y_4 = −εw_2 in the Landau gauge),
s^{(2)} = ½⟨w, H w⟩ with
  H = C_αc^*c + S_α𝒮,  c := [1 − εv, u − ε],  𝒮 := Σ_{i<j}(Y_i^*Y_j − Y_j^*Y_i)/(2i),  Y_1 = [1, 0], Y_2 = [0, u], Y_3 = [−εv, 0], Y_4 = [0, −ε],
C_α = 2C̃·½(cos a + cos b), S_α = 2S̃(sin a − sin b). Explicitly 𝒮 = Σ/(2i) with Σ_11 = ε̄v^* − εv, Σ_22 = ε̄u − εu^*,
Σ_12 = u − ε + ε̄v^*u + v^*, Σ_21 = −Σ_12^*. D_0 = [1 − u; 1 − v] (D_0λ = λ(x) − Ad(U_b)λ(x + μ)). *Normalisation:* at Φ = 0,
H = c^*c = d^*d per colour (§0), so 2C̃ = 1. *Criticality:* cD_0 = (1 − ε)·1 (expand and use εvu = uv), so c^*cD_0 =
(1 − ε)c^* = ((1 − ε) + (1 − ε̄)v^*, (1 − ε)u^* + (1 − ε̄))^T, and (using vu = ε̄uv, u^*vu = ε̄v, v^{-1}uv = εu)
ΣD_0 = ((1 + ε̄)v^* − (1 + ε), (1 + ε̄) − (1 + ε)u^*)^T. So HD_0 = 0 (NA-inv at the critical U_f) holds iff, in both rows,
C_α(1 − ε) = (S_α/2i)(1 + ε) and C_α(1 − ε̄) = −(S_α/2i)(1 + ε̄), i.e. S_α/(2i) = C_α(1 − ε)/(1 + ε) = −iC_αtan(φ/2):
**S_α = 2C_αtan(φ/2)**. Since (sin a − sin b)/(cos a + cos b) = tan((a − b)/2) =
tan(φ/2), this forces 2S̃ = 1. Hence C_α = ½(cos h_iΦ + cos h_jΦ) = 1 − γ_αφ² + O(φ⁴) with γ_α = (h_i² + h_j²)/(4q_α²), S_α =
sin h_iΦ − sin h_jΦ = φ + O(φ³); SU(2) (H_1 = iσ_3, q = 2): C = cos(φ/2), S = 2sin(φ/2), γ = 1/8. K_12 = H + D_0D_0^*.

*Step 2 (Weyl symbols).* W(m, n) := e^{−iφmn/2}u^mv^n satisfies W(M)W(M') = e^{iφM∧M'/2}W(M + M') (M∧M' := mn' − nm'; from
v^nu^{m'} = e^{−iφnm'}u^{m'}v^n) and τ(W(M)) = δ_{M,0}. The Weyl symbol of Σâ(M)W(M) is a(k) = Σâ(M)e^{iM·k}; products go to
a ⋆ b = a·exp(−(iφ/2)(∂⃖_1∂⃗_2 − ∂⃖_2∂⃗_1))·b = ab − (iφ/2){a, b} − (φ²/8)(a_{11}b_{22} − 2a_{12}b_{12} + a_{22}b_{11}) + O(φ³)
(matrix order kept; M_j ↔ −i∂_j), and τ tr Op(a) = ∫tr a, ∫ := ∫_{[−π,π]²}dk/(2π)². Symbols: u^{±1} ↦ z_1^{±1}, v^{±1} ↦ z_2^{±1}
(z_j := e^{ik_j}), v^*u ↦ s z_1z̄_2, u^*v ↦ s̄ z̄_1z_2, uv^* ↦ s̄ z_1z̄_2, vu^* ↦ s z̄_1z_2. With ω := 4 − 2cos k_1 − 2cos k_2 this gives
  σ_11 = C_α(2 − 2cos(k_2 + φ)) − S_αsin(k_2 + φ) + 2 − 2cos k_1,  σ_22 = C_α(2 − 2cos(k_1 − φ)) + S_αsin(k_1 − φ) + 2 − 2cos k_2,
  σ_12 = (C_α − 1)A + (1 − ε) + (S_α/2i)B,  A := z_1 − ε − s̄z_1z̄_2 + z̄_2,  B := z_1 − ε + s̄z_1z̄_2 + z̄_2,  σ_21 = σ̄_12
(the c^*c and D_0D_0^* off-diagonal symbols add to (C_α − 1)A + 1 − ε). Expanding, **σ = ω·1 + φσ_1 + φ²σ_2 + O(φ³)** with
  σ_1 = [[sin k_2, −(i/2)(1 + z_1)(1 + z̄_2)], [(i/2)(1 + z̄_1)(1 + z_2), −sin k_1]],
  σ_2 = [[−2γ_α(1 − cos k_2), −¼z_1z̄_2 − γ_α(z_1 − 1)(1 − z̄_2)], [conj., −2γ_α(1 − cos k_1)]],
so tr σ_1² = sin²k_1 + sin²k_2 + 2(1 + cos k_1)(1 + cos k_2) (= 8 at k = 0: σ_1(0) has eigenvalues ±2, the continuum spin
coupling) and tr σ_2 = −2γ_α(2 − cos k_1 − cos k_2).

*Step 3 (exact second order of the star exponential).* Let 𝔄 := ℓ¹(Z², M_2; e^{|M|}) with the twisted convolution (a Banach
algebra for every real φ: the twist has modulus 1). σ_φ has finite support and is entire in φ, so E(t, φ) := Σ_m(−t)^mσ_φ^{⋆m}/m!
(the symbol of e^{−tK_12}) is entire in (t, φ) in 𝔄, solves ∂_tE = −σ_φ⋆_φE, E(0) = 1, and its φ-Taylor coefficients E^{(r)}(t) solve
the hierarchy obtained by differentiating at φ = 0 (the derivative form of ⋆ is the Fourier multiplier (M∧M')^r, dominated
by the weight). Because σ_0 = ω·1 is scalar:
  E^{(0)} = e^{−tω};  ∂_tE^{(1)} = −ωE^{(1)} − σ_1e^{−tω} + (i/2){ω, e^{−tω}}, and {ω, e^{−tω}} = 0, so E^{(1)} = −tσ_1e^{−tω};
  ∂_tE^{(2)} = −ωE^{(2)} − σ_1E^{(1)} − σ_2e^{−tω} + (i/2)({ω, E^{(1)}} + {σ_1, e^{−tω}}) + (1/8)P²(ω, e^{−tω}),
where {ω, E^{(1)}} = −t(ω_1∂_2σ_1 − ω_2∂_1σ_1)e^{−tω} = −{σ_1, e^{−tω}} (the t² terms cancel), so the bracket terms cancel, and
P²(ω, e^{−tω}) = [t²(ω_{11}ω_2² + ω_{22}ω_1²) − 2tω_{11}ω_{22}]e^{−tω} (ω_{12} = 0). The right side is e^{−tω}r(t) with r polynomial in t, so
  E^{(2)}(t) = e^{−tω}[(t²/2)σ_1² − tσ_2 + (1/8)((t³/3)(ω_{11}ω_2² + ω_{22}ω_1²) − t²ω_{11}ω_{22})·1].
*Calibration:* for the scalar Harper operator (σ_1 = σ_2 = 0) ∫ of the last bracket is (1/8)[(t³/3)(8j_1²/t) − 4t²j_1²] =
−(t²/6)j_1², which is Lemma G-mag (iii) (−½(t²/3)j_1² per complex scalar in the plane): the expansion reproduces the
independently proven scalar coefficient.
*Step 4 (integrals).* With the 1D moments ∫e^{−t(2−2cos k)}dk/2π = j_0, ∫…cos k = j_1, ∫…sin²k = (j_0 − j_2)/2 = j_1/(2t)
(I_0 − I_2 = (2/z)I_1 at z = 2t): ∫e^{−tω}tr σ_1² = j_0j_1/t + 2(j_0 + j_1)², ∫e^{−tω}tr σ_2 = −4γ_αj_0(j_0 − j_1), and the orbital part
gives 2 × (−(t²/6)j_1²). Hence
  Θ_2(t) = [φ²]τ tr e^{−tK_12} = t²(j_0 + j_1)² + (t/2)j_0j_1 + 4γ_αt j_0(j_0 − j_1) − (t²/3)j_1²,
and R_12^lat(t) := Θ_2/(t²j_0²) (the f² coefficient is q_α²Θ_2, so this is §46's normalisation) is (ii). SU(2): (t/2)j_0j_1 +
(t/2)j_0(j_0 − j_1) = (t/2)j_0², so R_12^lat = (1 + ρ)² − ρ²/3 + 1/(2t).
*Step 5 (asymptotics, (iii)).* I_1(z)/I_0(z) = 1 − 1/(2z) − 1/(8z²) + O(z^{−3}), so ρ = 1 − 1/(4t) + O(t^{−2}), (1 + ρ)² = 4 − 1/t + O(t^{−2}),
ρ²/3 = 1/3 − 1/(6t) + O(t^{−2}), ρ/(2t) = 1/(2t) + O(t^{−2}), 4γ_α(1 − ρ)/t = O(t^{−2}); so R_12^lat = 11/3 − (1/3)/t + O(t^{−2}) for every
γ_α, and |R_12^lat(t) − 11/3| ≤ C/t for t ≥ 1 (ρ ∈ (0, 1) is smooth). With R_S^lat = −ρ²/6 (G-mag (iii)): R_V^{4D} = R_12 + 2R_S =
(1 + ρ)² − (2/3)ρ² + … → 10/3 and R_12 + R_S = (1 + ρ)² − ρ²/2 + … → 7/2, both at rate O(1/t). ∎
*Reading.* (1) (V-heat) (§46) is now a theorem, in closed form, for every root of SU(N): the lattice plane-12 vector
coefficient is (1 + ρ)² (the spin coupling, ½∫e^{−tω}tr σ_1²/(j_0²), → 4) minus ρ²/3 (the two orbital components, each −ρ²/6, the
scalar G-mag value), plus an O(1/t) term from the lattice phases of the cross terms and C_α − 1. S6-F5 does not occur.
(2) The reviewer's fitted slope a ≈ −1/3 is the exact O(1/t) coefficient, and it is γ_α-independent. (3) What this does NOT
give: (V-IR), i.e. that the IR term and the level-n ⊥ group act on G_⊥ as a proper-time cutoff at t ≈ ℓ² with an
n-uniform error; it is unchanged and OPEN, and is now the single named input for the transverse 21/22 at the level of the
heat trace. (4) The derivation also confirms the structure behind f9 V0b-V0e: criticality is exactly the relation
S_α = 2C_αtan(φ/2).

## 54. Session-7 checks (ADDED AFTER the run; checks/f10_criteria.md, f10_fp_vheat.py, f10_out.txt, f10_time.txt)
Criteria written 06:04:51 UTC before any f10 script (stat in FLOW_LOG); smoke test in the scratchpad (B = 41, t ≤ 6), no
change after it. Official f10: one NUMERIC LOCK acquisition 06:08:39-06:08:43 UTC, nice 10, 1 thread, load 2.56, memory free
41%; 4.15 s, peak RSS 163 MB. **19/19 verdict lines PASS; all four controls fail as required.**
- **A (Lemma FP-exact), charge-1 torus 9², L = 3, NA-FP's axial-path slice, k = 1 and 3 flux quanta:** A0 (NA-FP (i) as
  implemented) 4.4e-16; σ_min(χΓ) = 0.275; **LHS − RHS = 2.3e-13 and 0.0** (LHS = 5.744664966585, 4.952623109279), no
  additive constant; factorisation of det χΓ to 2.3e-13; ΠOΠ > 0 on ker h (λ_min 0.046, 0.053). Control (Δ_FP(1) for Δ_FP(U_f)):
  mismatch 0.188 and 0.353 (fails as required). Reported: det(hh^*) is f-independent in 2D (see the post-hoc note in §52),
  log|det χΓ| moves by −0.188, −0.353.
- **V1 (Theorem V-heat (i)), SU(2):** f9's Wilson Hessian root block in the left chart equals Σ_p[C_pc_p^*c_p + S_p𝒮_p] to 6.7e-16
  (torus 9², one quantum) and 8.9e-16 (open box 11², f = 0.07); D_0 to 3.3e-16; the formula operator has H_CD_C = 6.0e-16 on
  the torus (criticality from S = 2C tan(φ/2)). Control S_p := 0: 7.7e-2, 7.0e-2 (fails as required).
- **V2 (closed form, SU(2)), direct heat trace of the formula operator (not f9's builder), box 101²:** max relative
  deviation from (1 + ρ)² − ρ²/3 + 1/(2t) is 1.9e-7 over t = 2, …, 24 (largest at t = 24: 3.6526655 against 3.6526661, the box
  edge entering).
- **V3 (closed form, γ = 1/4):** 2.6e-8. **V4:** f9_out.txt's printed R_12, R_S agree with the closed forms to 1.1e-6, 4.5e-7.
- **V5 (reported):** t(R_12 − 11/3) = −0.33396, −0.33340, −0.33334 at t = 10², 10³, 10⁴; R_12 + R_S = 3.4999750, R_V^{4D} =
  3.3333167 at t = 10⁴.
- **Reading.** (1) Lemma FP-exact holds to round-off in a non-trivial instance (actual NA-FP slice, flux, non-trivial M_U),
  with no constant, and the control shows that a U_0-independent normalisation is off at O(10^{-1}) here. (2) The SU(2)
  root-block structure of Theorem V-heat (i) is exactly f9's Wilson Hessian; the closed form (ii) matches a direct
  computation at 10^{-7} and f9's numbers at their printed precision. (3) Not tested: the SU(N ≥ 3) Wilson structure (i)
  (analytic only; V3 tests the Moyal step at γ ≠ 1/8 with the formula operator), the composite (n ≥ 2) slice in Part A,
  d = 4 in Part A, (V-IR).

## 55. Session-7 outcomes against §50 (ADDED AFTER the derivations and checks)
- **Step 1 (fixes): DONE.** S6-1..S6-5 applied in place, tagged [RFL6-fix] (19 tagged lines; S6-6 (R1), (R2) on T_k(B) and
  the operator form of (V-IR) not done this session).
- **(P1) Lemma F-id-exp: PROVEN** (§51; cone homotopy with exponential weights; the MS (iv) hypothesis checked given
  (L-loc2)). S7-F3 does not occur.
- **(P2) Lemma FP-exact: PROVEN** (§52; FP-ab + NA-FP (ii) + coarea; no constant; f10 A). **(a3) ≡ 0 at every critical
  background satisfying (N)**, in particular at U_f, |f| ≤ ε_n; the 1/22 and 21/22 statements now hold for the tower's own
  fixing. S7-F1 does not occur, given the binding reading of Δ_FP(U_0) (§52 Reading (1)).
- **(P3) Theorem V-heat: PROVEN in closed form** (§53): R_12^lat(t) = (1 + ρ)² − ρ²/3 + ρ/(2t) + 4γ_α(1 − ρ)/t, SU(2):
  (1 + ρ)² − ρ²/3 + 1/(2t); → 11/3 − 1/(3t) + O(t^{-2}) for every root. S7-F2 does not occur (f10 V1-V4). (V-heat) is
  discharged; S6-F5 is excluded.
- **Target S7-4 ((V-IR) in a charged-scalar model with the real averaging maps): NOT ATTEMPTED.** Reason: a faithful
  model needs the actual S4' root-sector maps T_k(B) and 𝒞_n at n = 1, 2 in 4D Bloch form; a toy block average would not
  test (V-IR), and the 2D analogue has a different (power, not log) proper-time structure. f10 has no Part B.
- **Theorem UNIV now:** conditional on (V-IR) for G_⊥ (the crux: the IR term and the level-n ⊥ group act as a proper-time
  cutoff at t ≈ ℓ² with an n-uniform error; it contains (R1), (R2), (R3) on G_⊥ and (a2), (a4') in transverse form), (s2⊥)
  including the IR safety of the root-sector level-n ⊥ group, (b), and (L-loc2) (ARGUED); plus (s1) and G-mag (vi) for the
  rate. (a3) and (V-heat) are discharged; the ghost share needs only GH-log (b) for UNIV's O(1) form.
  **[RFL7-fix S7-5] The list above is over-inclusive and is REPLACED by the minimal list (REVIEW_FLOW_S7 §6): Theorem UNIV
  (O(1) form) is conditional on (1) (V-IR) on G_⊥ (crux; operator-level, well-posed form: §57 (Q1)); (2) (L-loc2) (ARGUED);
  (3) G-mag (vi), or (V-IR) stated for limit points (§57 (Q1) does the latter; G-mag (vi) is attempted in §58).
  Means of proof of (V-IR), NOT separate hypotheses: (R1)-(R3) on G_⊥, (U-IR)(a2), (a4') in transverse form, (U-IR)(b) (a
  hypothesis only on the U-res route), and the IR safety of the root-sector level-n ⊥ group (needed only on a route that
  splits G_⊥ into its fine term and its level-n group). For UNIV-rate only: (s1), (s2⊥), and (vi) for exactness.**

## 56. Tally after session 7 (FLOW.md items; session-7 items unreviewed)
- **PROVEN-HERE: 37 (sessions 1-6, as confirmed by REVIEW_FLOW_S6, with its scope annotations) + 3 (session 7) = 40.**
  Session 7: Lemma F-id-exp; Lemma FP-exact (given NA-FP (ii) composite, FP-ab, S-all, (N)); Theorem V-heat (closed form;
  SU(N) structure (i) by the 2 × 2 block argument plus criticality). Upstream inputs used: Lemma FP-ab, Proposition NA-FP
  (i)-(ii) and its composite form (PROOF, read-only), Lemma S-all, NA-inv, COV-GI proof (1), (3), Lemma F-id, GT-lat' (ii),
  Lemma G-mag (iii), Lemma MS (ii).
- **Scope annotations now:** GH applies to the tower's fixing (FP-exact); MS (iv) given (L-loc2) via F-id-exp; N-f given
  (L-loc); COV-GI-∞ given (L-loc2) and (vi); GH-log (c), (d) given (vi).
- **ARGUED, not counted:** G-mag (vi); (L-loc2) (replaces (L-loc) where second derivatives are needed).
- **RETIRED:** (U-IR)(a3) as a bound against BF-Feynman J_* (superseded by "(a3) ≡ 0", Lemma FP-exact).
- **GAP:** Corollary UNIV-rate (unchanged). **WRONG as stated, superseded:** as in §49. **IMPORTED-AND-REVERIFIED:** L4b.
- **OPEN:** (V-IR) [s-P] (the crux; operator-level restatement S6-6 still to be written); (R1), (R2) on the root-sector maps
  [s]; (U-IR)(b) [s]; (U-IR-s) (s1) [s-P], (s2⊥) in the root sectors incl. IR safety of the level-n ⊥ group [s-P]; (COV-GI)
  at non-critical backgrounds [s]; FI-1 [cross-lane]; HIST's restatement of CL^J's Setting [cross-lane].
- **Checks:** f10 (A0-A4 ×2, V1 ×2, V2, V3, V4 PASS; A-ctl ×2, V1-ctl ×2 fail as required).

---
# Session 8 of lane C (opened 2026-10-28 06:25 UTC)

## 57. Session-8 targets and PRE-STATED (session 8) statements (written 2026-10-28 06:44 UTC, before any session-8 proof, criteria file or script)

Binding input: REVIEW_FLOW_S7.md. Its wording fixes S7-1, S7-4 and the S7-5 leftovers are applied in place, tagged
**[RFL7-fix]** (step 1, done before this section). S7-2 and S7-3 are answered here. Setting and notation of §41-§46 and
§53; root sector α, charge q_α, U_f, n ≥ 1, ℓ = L^n; densities per fine site; complex root coordinate, so log det_C =
½log det_R. For a function X(f) on the dense flux set 𝔉_n of Corollary COV-GI-∞, **[f²]_lim X** denotes the set of limit
points of (X(f) − X(0))/f² as f → 0 in 𝔉_n; when it is one point it is the f² coefficient [f²]X.

**PRE-STATED (session 8).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Each hypothesis is named in the statement; nothing below uses an ARGUED or OPEN item as if proven.
Proofs follow in §58-§60; any change of a statement after this point is logged as such.

**(Q1) (V-IR), well posed and at operator level (S7-2 second half, S7-3).** Put, for t > 0,
  θ_α(t) := [f²]{τ tr_C e^{−tK_F} − τ tr_C e^{−tΔ_0}}  (K_F = H + D_0D_0^* on 1-forms, Δ_0 = D_0^*D_0 on 0-forms, at U_f),
  𝔠_α(T) := −∫_0^T θ_α(t)dt/t,   𝔪_α(μ) := [f²]{log det_C(K_F + μ) − log det_C(Δ_0 + μ)}  (μ > 0).
(a) θ_α(t) = q_α²t²j_0(t)⁴(R_12^lat + R_S^lat)(t) exactly (the Landau transverse heat-trace coefficient), |θ_α(t)| ≤ C_θq_α²
  for all t > 0, and θ_α(t) = (7/2)q_α²/(16π²) + O(q_α²/t) for t ≥ 1.
(b) **Lemma VIR-eq.** For each μ ∈ (0, 1], 𝔪_α(μ) exists, equals −∫_0^∞e^{−μt}θ_α(t)dt/t, and |𝔪_α(μ) − 𝔠_α(1/μ)| ≤ A_0q_α²
  with A_0 absolute **[RFL8-fix S8-2: read "with A_0 depending only on N and H_1"]**. Moreover 𝔠_α(ℓ²) = −(21q_α²/(48π²))log ℓ + O(q_α²).
(c) **Well-posedness.** Given (L-loc2) (as a hypothesis): [f²]_lim G_⊥,n,α = c^tot_{n,α} − [f²]_lim G_gh,n,α, where
  c^tot_{n,α} := [f²](Γ^{W0}_n + Γ^cov_n)|_α exists (one number); by Proposition GH-log (b) the right side lies in the
  interval of radius 2q_α²sup|c'| about c^tot_{n,α} + 2c_gq_α²log ℓ. If G-mag (vi) holds it is one point, c^⊥_{n,α}.
(d) **(V-IR), binding form.** There is A, independent of n and α, such that for every n, every α and every
  c ∈ [f²]_lim G_⊥,n,α: |c − 𝔪_α(ℓ^{-2})| ≤ Aq_α² (equivalently, by (b), with 𝔠_α(ℓ²) in place of 𝔪_α(ℓ^{-2})). In words:
  on the f² coefficient, the IR term M^TΠM together with the level-n ⊥ group ½log det_⊥(P_⊥𝒞_nP_⊥) acts as a mass ℓ^{-2}
  (equivalently a proper-time cutoff at t = ℓ²) on the fine Feynman-form transverse operator, with an n-uniform error. With
  (b): (d) ⟹ every limit point equals −(21q_α²/(48π²))log ℓ + O(q_α²), i.e. β^fine[G_⊥,n] = −(21/22)β_0^std log ℓ + O(1).
  (d) is a STATEMENT (OPEN); (a)-(c) are lemmas.

**(Q2) (R1), (R2) on the root-sector maps T_k(B) (S7-2 first half).** Setting: B a Cartan level-k background of constant
level-k flux F (plane 12; any B with this flux is Cartan-gauge equivalent to it in infinite volume, Lemma B-flux's
argument), |q_αF| ≤ ε_1; T_k(B) := D(W_♮∘M̄)(B) restricted to the root sector α (complex linear by torus equivariance).
By the chain rule, T_k(B)X(c) = 𝔇_c[Σ_{σ,y}Σ_{b∈T^σ_y}ω_c(σ, y, b)X_b], with ω_c(σ, y, b) the unimodular linearised transport
phase of b along the contour T^σ_y = P^σ(c_X → y)S_yP^σ(c_Y → y + Le_μ)^† times the contour weight (1/24)L^{-4} and the sign of
the leg, and 𝔇_c the root block of DW_♮ at M̄_c(B) (frames of B, B' := W_♮∘M̄(B)). Split the b-sum by legs:
  T^str_k(B)X(c) := 𝔇_c[Σ_{σ,y}Σ_{b∈S_y}ω_cX_b] (straight leg),  h_k(B)X(X) := avg_σavg_{y∈B(X)}Σ_{b∈P^σ(c_X→y)}(transport phase to c_X)X_b
(the covariant slice functional; LINEAR_PACKAGE's h at B = 1), D^♭_{B'}λ(c) := Ad(B'_c)λ(Y) − λ(X) (c = (X, Y); D^♭_1 = d), and
**R_k(B) := T_k(B) − T^str_k(B) + D^♭_{B'}h_k(B)**. Then:
(R1) (estimate, root-sector GS-1 analogue) R_k(1) = 0 (this is Q_root = Q_str − d∘h); R_k(B) has the finite range of T_k,
  and ||R_k(B)|| ≤ C_R|q_αF| with C_R independent of k and of the level (uniform chain); and exactly
  T_k(B)D_B = D_{B'}ev (covariance, §30).
(R2) (diamagnetic damping) |T^str_k(B)(c, b)| ≤ r_*(F)^{-1}Q_str(c, b) entrywise, with r_*(F) := min_c(root-sector lower bound of
  𝔇_c^{-1}) ≥ 1 − c_W(q_αF)²; hence for a chain B_j, …, B_{n−1} of such backgrounds with fluxes F_j, …, F_{n−1}:
  ||T^str_{n−1}(B_{n−1})⋯T^str_j(B_j)|| ≤ Π_kr_*(F_k)^{-1}·L^{-(n−j)} (GS-2 (e)).
(R-damp) (consequence) For U_f with |f| ≤ ε_0L^{-2n} (ε_0 small, fixed): ||P_⊥(B_n)A_j(U_f)|| ≤ e_1L^{-(n−j)} and
  c_-κ^{-1}P_⊥ ≤ P_⊥𝒞_n(U_f)P_⊥ ≤ c_+κ^{-1}P_⊥ in every root sector, with e_1, c_± independent of n (the root-sector form of
  Proposition COV-⊥-C (b)).
  **[RFL8-fix S8-3] For N ≥ 3 read the flux in C_R, r_*(F), c_W and φ_k as |F| := max_i|h_iF| (resp. max_i|h_iF_k|): R_k and
  𝔇_c depend on all the diagonal fluxes h_iF, not on q_αF alone; C_R, c_W, r_* depend on N. For SU(2) this is q_αF up to the
  factor 1/2. No statement changes otherwise.**

**(Q3) Theorem G-mag (vi) (the area invariance principle; S7-3 first option).** In the setting of Lemma G-mag:
(a) (exact) for every θ ∈ R and t > 0, E_t[cos θA] = j_0(t)^{-1}E^{x-br}_t[∫_{−π}^{π}(dψ/2π)exp(−2∫_0^t(1 − cos(θx_s + ψ))ds)],
  E^{x-br}_t the law of the coordinate-1 bridge (continuous-time, jumps ±1 at rate 1 each, x_0 = x_t = 0);
(b) for every s ∈ R: lim_{t→∞}E_t[cos(sA/t)] = s/sinh s;
(c) c'(φ) → c'_0 as φ → 0, with
  c'_0 = ½κ_0 − (1/(16π²))∫_0^1(s²/6 − 1 + s/sinh s)s^{-3}ds + (1/(16π²))∫_1^∞(1 − s/sinh s)s^{-3}ds,
  κ_0 := ∫_0^1m(t)dt/t + ∫_1^∞(m(t) − 1/(48π²))dt/t,  m(t) = (t²/3)j_1(t)²j_0(t)².
  Consequently Proposition GH-log (c), (d) hold unconditionally, and the "(vi)" qualifiers of COV-GI-∞ and §56 drop.
  [Imported, to be re-verified on this walk in the proof: Donsker's invariance principle for the free walk.]

**(Q4) The scalar proxy (target of REVIEW_FLOW_S7 §9.1).** Complex unit-charge scalar on Z⁴ at the constant field of flux
f in the plane 12; Δ_f its covariant Laplacian (Lemma G-mag); the chain of Proposition COV-sc (Q_k^A: S4''s axial
transporters, 24 orders, to the level-(k+1) centres; κ_j = sL^{2j}); M_f := Q_{n−1}^A⋯Q_0^A (fine → level n); 𝒞_n(f) =
C_n(f)·1 (COV-sc (1)-(2)). Put
  G_S,n(f) := log det_C(Δ_f + C_n(f)^{-1}M_f^†M_f) + log det_C𝒞_n(f)  (per fine site),
the scalar analogue of Γ^{W0}_n + Γ^cov_n (no gauge group, no ghost). **Lemma S-red:**
(i) G_S,n is C² in f near 0 (every n; a gapped finite-range covariant density); c^S_n := [f²]G_S,n exists;
(ii) (exact, f ≠ 0) G_S,n(f) = g(f) + ℓ^{-4}τ_n log 𝒦_n(f), 𝒦_n(f) := C_n(f) + M_fΔ_f^{-1}M_f^† on level-n sites (τ_n per level
  site), g(φ) = τ log Δ_φ;
(iii) given Theorem G-mag (vi): c^S_n = 2c_g log ℓ + ρ_n, where ρ_n := lim_{F→0}F^{-2}[τ_n log 𝒦_n(F/ℓ²) + g(F) − (both at
  F = 0)] exists (F = ℓ²f is the level flux; the level-n quantity log 𝒦_n + log Δ^{(n)}_F ~~is IR safe~~ **[RFL8-fix S8-4: has
an F² limit ρ_n; that is all (iii) proves]**);
(iv) the scalar (V-IR), |c^S_n − 𝔠^S(ℓ²)| ≤ A_S for all n with 𝔠^S(T) := ½∫_0^Tm(t)dt/t, is equivalent to sup_n|ρ_n| < ∞
  (**statement (V-IR-S), OPEN**).

**Check f11** (criteria file first, its stat into FLOW_LOG before any f11 script; jobs < 20 min, < 1 GB, memory free
≥ 35%): (S) the scalar proxy at n = 1 (ℓ = 3) and n = 2 (ℓ = 9), L = 3, s = 4, with the real S4' axial transporters
(24 orders, reduced exactly to the plane 12 times a plain block average in 34; the reduction itself tested against a
direct 4D torus), magnetic Bloch decomposition at rational level flux, c^S_n by a polynomial fit in f²; **prediction
(V-IR-S at n ≤ 2): (c^S_2 − c^S_1)/(2c_g log 3) = 1 within 25%**, and the total is IR safe (fit-window stability) while
its piece g alone is not (control); (G) Theorem G-mag (vi)'s c'_0 by quadrature against f9's rational-flux sequence c'(φ)
(f9_out.txt; geometric extrapolation 1.38583e-3): **prediction |c'_0 − 1.38583e-3| ≤ 5e-6**.

**Failure modes (each a valid outcome).** (S8-F1) the area invariance principle fails or c'_0 disagrees with f9 (an error
in (Q3)); (S8-F2) the n-increment of c^S_n differs from 2c_g log 3 by more than 25% (the simple proper-time-cutoff picture
of (V-IR) fails already in the scalar proxy at n ≤ 2, or the n-dependent O(1) term is large); (S8-F3) the f² log f
part does not cancel in G_S,n (the IR term does not make the scalar total IR safe).

---
# Session-8 proofs (written after §57)

## 58. Theorem G-mag (vi) (the area invariance principle): PROVEN-HERE [one import, re-verified below]

Statement: (Q3) of §57. Notation of Lemma G-mag; p_s(k) := e^{−2s}I_k(2s) = ∫_{−π}^{π}(dθ/2π)e^{−2s(1−cos θ)}e^{ikθ} (the law of a
coordinate of the walk at time s), j_0(s) = p_s(0); m_∞ := 1/(48π²) = 2c_g.
*Proof.* (a) Under the 4D bridge law the four coordinates are independent one-dimensional bridges (the eight jump
directions are independent Poisson processes of rate 1 and the conditioning factorises), and A = ∫_0^tx(s−)dy(s) depends
only on (x, y). Fix the x-path (bounded, càdlàg). y = N^+ − N^- with N^± independent rate-1 Poisson processes independent
of x, so by Campbell's formula E[exp(i∫_0^t(θx_s + ψ)dy_s) | x] = exp(∫_0^t(e^{i(θx_s+ψ)} + e^{−i(θx_s+ψ)} − 2)ds) (x_{s−} = x_s at the
jump times of y a.s.: no common jumps). Insert 1{y_t = 0} = ∫_{−π}^{π}(dψ/2π)e^{iψy_t}, divide by P(y_t = 0) = j_0(t) (Fubini:
bounded integrands). The result is real and positive, so it is E_t[cos θA] (= E_t[e^{iθA}]).
(b) Put θ := s/t, ψ =: η/√t, X^t(u) := x_{tu}/√t (u ∈ [0, 1]). By (a),
  E_t[cos(sA/t)] = c_tE^{x-br}_t[Φ_t(X^t)],  Φ_t(X) := π^{−1/2}∫_{|η|≤π√t}dη exp(−2t∫_0^1(1 − cos((sX(u) + η)/√t))du),
c_t := π^{1/2}/(2π√t·j_0(t)) → 1 (j_0(t) = (4πt)^{−1/2}(1 + O(1/t))). Let b be a standard Brownian bridge and
Φ(X) := π^{−1/2}∫_Rdη exp(−∫_0^1(sX + η)²du) = exp(s²[(∫X)² − ∫X²]) (Gaussian η-integral), continuous on C[0, 1] in sup norm,
with values in (0, 1].
(b1) *Invariance principle for the x-bridge: X^t ⇒ √2 b in D[0, 1] (J1; the limit is continuous, so J1 and uniform
convergence agree on it).* IMPORTED: Donsker's theorem for the free walk (x is a Lévy process with Ex_1 = 0, Var x_1 = 2,
so x_{t·}/√t ⇒ √2W in D[0, 1]; hypotheses checked: independent stationary increments, finite variance). Re-verified on
this walk for the bridge: (1) for δ ∈ (0, ½), the bridge law restricted to [0, 1 − δ] has density ρ_t(X(1 − δ)) with respect
to the free law, ρ_t(z) := p_{δt}(z√t)/p_t(0); the local CLT for p_s (Laplace's method on the Fourier integral above:
sup_k|(4πs)^{1/2}p_s(k) − e^{−k²/(4s)}| → 0 as s → ∞) gives sup_z|ρ_t(z) − δ^{−1/2}e^{−z²/(4δ)}| → 0, which is the density of
√2 b on [0, 1 − δ] with respect to √2W; with free Donsker, E^{br}G(X^t|_{[0,1−δ]}) → E G(√2b|_{[0,1−δ]}) for bounded
continuous G (|E^{free}[Gρ_t] − E^{free}[Gρ]| ≤ ||G||sup|ρ_t − ρ|, and Gρ is bounded continuous). (2) Time reversal maps the
bridge to itself (jumps ±1 change sign, a symmetry), and on [0, δ] the bridge density with respect to the free walk is
≤ sup_kp_{(1−δ)t}(k)/p_t(0) ≤ p_{(1−δ)t}(0)/p_t(0) ≤ C (p_s(k) ≤ p_s(0) by Fourier positivity; δ ≤ ½), so Doob's inequality gives
E^{br}sup_{u∈[1−δ,1]}|X^t(u)|² ≤ 8Cδ and likewise P^{br}(sup_{u≤1}|X^t(u)| ≥ t^{1/8}) ≤ 2C·P^{free}(sup_{u≤1}|X^t| ≥ t^{1/8}) ≤ C'e^{−t^{1/8}}
(exponential martingale). (1)-(2) give finite-dimensional convergence and tightness, hence the claim. **[RFL8-fix S8-1]
The approximation step, in one sentence: (1) gives convergence of the restrictions to [0, 1 − δ] in D[0, 1 − δ] for every
δ, (2) makes the oscillation on [1 − δ, 1] small uniformly in t as δ → 0, and Billingsley (Convergence of Probability
Measures, 2nd ed., Thm 3.2: X^{t,δ} ⇒ X^δ, X^δ ⇒ X as δ → 0, and lim_δ limsup_t P(d(X^{t,δ}, X^t) ≥ η) = 0 give X^t ⇒ X) with
X^{t,δ} := X^t stopped at 1 − δ concludes.**
(b2) *The functional.* On G_t := {sup|X| ≤ t^{1/8}} put a(u) := (sX(u) + η)/√t. For |η| ≤ π√t − |s|t^{1/8}, |a| ≤ π, so
1 − cos a ≥ (2/π²)a² and the integrand is ≤ exp(−(4/π²)∫(sX + η)²) ≤ exp(−(4/π²)(η + s∫X)²) (Jensen), whose η-integral is
π^{3/2}/2 for every X; on the remaining strip (length ≤ 2|s|t^{1/8}) cos a ≤ −½ for t large and the contribution is ≤ Ct^{1/8}e^{−3t}.
So Φ_t ≤ C on G_t, while Φ_t ≤ 2π^{1/2}√t always and P^{br}(G_t^c) ≤ C'e^{−t^{1/8}}: E^{br}[Φ_t(X^t); G_t^c] → 0. By (b1) and
Skorokhod's representation (D[0, 1] with J1 is Polish) take X^t → X := √2b uniformly a.s.; for such a path, sup|X^t| and
∫X^t are bounded for large t, 2t(1 − cos a) = (sX^t + η)²(1 + O((sX^t + η)²/t)) → (sX + η)² pointwise in η, and the dominator
above is uniform; so Φ_t(X^t)1_{G_t} → Φ(X) a.s., boundedly. Hence E_t[cos(sA/t)] → EΦ(√2b) = E exp(−2s²∫_0^1(b − b̄)²du),
b̄ := ∫b. The demeaned bridge has Karhunen-Loève eigenvalues 1/(4π²k²), k ≥ 1, each of multiplicity 2 (Watson's U²; check:
Σ_k2/(4π²k²) = 1/12 = E∫(b − b̄)² = 1/6 − 1/12) **[RFL8-fix S8-1: proof in one line: b − b̄ has covariance G(u − v) =
1/12 − |u − v|/2 + (u − v)²/2, which is the Green's function of −d²/du² on the circle R/Z restricted to mean-zero functions
(G'' = −δ + 1 periodically, ∫G = 0); its eigenfunctions are cos 2πku, sin 2πku (k ≥ 1) with eigenvalue (2πk)^{-2}]**, so E e^{−λ∫(b−b̄)²} = Π_k(1 + λ/(2π²k²))^{−1}, and at λ = 2s² this is
Π_k(1 + s²/(π²k²))^{−1} = s/sinh s.
(c) By (b) and Lévy's continuity theorem, A/t ⇒ 𝒜 under E_t, E cos(s𝒜) = s/sinh s (so E𝒜² = 1/3, consistent with
(iii): E_tA²/t² = j_1²/(3j_0²) → 1/3). Let h(x) := x²/2 − 1 + cos x (0 ≤ h ≤ min(x²/2, x⁴/24)); (A/t)² is uniformly integrable
by (iv) (E_t(A/t)⁴ ≤ C_4, t ≥ 1), so E_th(sA/t) → E h(s𝒜) = s²/6 − 1 + s/sinh s. With T := 1/|φ| and 1 − cos x = x²/2 − h(x),
  ψ(φ) = ½∫_0^Tm(t)dt/t − I_2(φ) + I_3(φ),  I_2 := ∫_0^T(dt/t)P(t)φ^{−2}E_th(φA),  I_3 := ∫_T^∞(dt/t)P(t)φ^{−2}(1 − E_tcos φA).
First term: m(t) = m_∞ + O(1/t) (Bessel asymptotics, as in (v)), so ½∫_0^Tm dt/t = c_g log(1/|φ|) + ½κ_0 + O(|φ|), with κ_0 as in
(Q3) (absolutely convergent). I_2: the part t ≤ 1 is ≤ (φ²/24)∫_0^1P E_tA⁴dt/t = O(φ²); for t ≥ 1 substitute t = sT
(φA = s·A/t): the integrand becomes s^{−1}[(sT)²P(sT)]s^{−2}E_{sT}h(sA/t), with (sT)²P(sT) → 1/(16π²) (P = j_0⁴), bounded by
C s^{−3}min(s⁴C_4, …) ≤ C's on (0, 1] (h ≤ x⁴/24 and (iv)); dominated convergence gives I_2 → (16π²)^{−1}∫_0^1E h(s𝒜)s^{−3}ds.
I_3: the same substitution on [1, ∞), integrand ≤ 2Cs^{−3}, limit (16π²)^{−1}∫_1^∞(1 − s/sinh s)s^{−3}ds. Subtracting
c_g log(1/|φ|): c'(φ) → c'_0 as stated (ψ is even in φ). The consequences: in Proposition GH-log (a), c'(q_αℓ²f) − c'(q_αf) → 0,
so (c) and (d) hold without condition; COV-GI-∞'s root-sector group coefficients exist as numbers. ∎
*Reading.* (1) G-mag (vi) is now PROVEN-HERE (one import, Donsker for the free walk, with its hypotheses checked; the bridge
step, the area functional and the limit law are proved here). **[RFL8-fix S8-1] The standard facts used, listed: the
functional CLT for a Lévy process in D[0, 1] (Jacod-Shiryaev VII.3, or Donsker on the integer skeleton plus control between
integer times; this replaces "Donsker's theorem" as the name of the import; hypotheses: independent stationary increments,
mean 0, variance 2), Skorokhod's representation theorem (D[0, 1] with J1 is Polish), Lévy's continuity theorem, Billingsley
Thm 3.2 (the approximation step of (b1)), and the Karhunen-Loève spectrum of the demeaned Brownian bridge (proved in one
line in (b2)). All are textbook; none is specific to this lane.** The proof gives more than the limit: the exact Fourier
formula (a) reduces the area law of the planar bridge to a functional of ONE coordinate bridge, and the limit s/sinh s is
the Gaussian η-integral of Lévy's area formula. (2) c'_0 is explicit; f11 (G) compares it with f9's rational-flux
sequence (f9 G2). (3) The rate c'(φ) − c'_0 = O(φ) seen in f9 G2b is not proved here (it is a UNIV-rate input).

## 59. (V-IR) well posed, its mass/cutoff forms, and (R1), (R2), (R-damp): PROVEN-HERE (statement (Q1)(d) OPEN)

Statements: (Q1) (a)-(c), (Q2) of §57.
*Proof of (Q1)(a).* At critical U_f, K_FD_0 = D_0Δ_0 (§43 (v): HD_0 = 0), so K_F is block diagonal on ker D_0^* ⊕ Ran D_0, and on
Ran D_0 it is unitarily equivalent to Δ_0 on (ker D_0)^⊥; in a root sector at f ∉ 2πZ/q_α, ker Δ_0 is a null set of the Bloch
integral (§43 (iv)). So θ_α(t) = [f²]τ tr_{ker D_0^*}e^{−tH}. By §46 (exact decoupling of the components 3, 4, confirmed by
REVIEW_FLOW_S7 §3.3) and Theorem V-heat (ii), [f²]τ tr_Ce^{−tK_F} = q_α²j_0²·t²j_0²(R_12^lat + 2R_S^lat), and by G-mag (iii)
[f²]τ tr_Ce^{−tΔ_0} = q_α²t²j_0⁴R_S^lat; subtract. Bound: t²j_0⁴ ≤ min(t², C), |R_12^lat + R_S^lat| ≤ (1 + ρ)² + ρ²/2 + 1/2 + 4γ_α/t
(0 < ρ < 1, ρ/t ≤ 1), and t²j_0⁴·4γ_α/t ≤ 4γ_αmin(t, C/t); so |θ_α| ≤ C_θq_α² (γ_α ≤ max_ih_i²/(2q_α²) bounded at fixed N).
Large t: t²j_0⁴ = (16π²)^{−1} + O(1/t) and R_12 + R_S = 7/2 + O(1/t) (V-heat (iii)). ∎
*Proof of (Q1)(b) (Lemma VIR-eq).* (1) *Gap.* K_F,0 ≥ 0 and Δ_0 ≥ 0; both are finite range and polynomial in the links, so the
IMS argument of Lemma N-f (iii) (with Ã replaced by K_F, resp. Δ_0, whose (L-loc)-type bounds hold trivially by finite
range) gives K_F,f ≥ −C|f|^{2/3}, Δ_f ≥ 0. So for |f| ≤ f_μ := (μ/(4C))^{3/2}, K_F,f + μ ≥ 3μ/4 and Δ_f + μ ≥ μ. (2) *Existence.*
Both are gapped finite-range covariant operators, so Lemma MS (ii)-(iii) make their log-densities C² on |f| < f_μ; 𝔪_α(μ)
exists. (3) *Formula.* For K ≥ c > 0, τ[log(K + μ)] = −∫_0^∞(dt/t)(τ tr e^{−t(K+μ)} − e^{−t}τ tr 1) (spectral theorem). For the
semigroup, the Combes-Thomas conjugation e^{ηx}Ke^{−ηx} = K + ηB + O(η²) with B anti-Hermitian (K real symmetric in the
symmetric gauge up to the unimodular phases, finite range) gives |e^{−t(K_f+μ)}(x, y)| ≤ e^{−t(3μ/4 − C'η²)}e^{−η|x−y|}; take
C'η² = μ/4. Duhamel for ∂_f (in the symmetric gauge every f-derivative of the twist produces a factor iqγ∧γ'/2, absorbed by
the e^{−η|·|} moments) gives |∂_f^jτ tr e^{−t(K_f+μ)}| ≤ C_μ**t**(1 + t)^{2j}e^{−μt/2} (j = 1, 2), uniformly on |f| ≤ f_μ; the same
for Δ_f **[RFL8-fix S8-2: the factor t is the Duhamel factor: ∂_fe^{−tK} = −∫_0^te^{−(t−s)K}(∂_fK)e^{−sK}ds gives one factor t per
first derivative and (for j = 2) t² + t from the double Duhamel term and the ∂_f²K term, both ≤ t(1 + t) for the j = 2 bound]**.
So the f-derivatives may be taken under the t-integral (dominated convergence: the difference quotients of order ≤ 2 are
dominated, uniformly in |f| ≤ f_μ, by C_μt(1 + t)^4e^{−μt/2}, which is integrable against dt/t on (0, ∞)
**[RFL8-fix S8-2: replaces "near t = 0 the integrand's f² part is O(t), see (a)", a pointwise statement about the coefficient,
not the uniform domination needed]**), and 𝔪_α(μ) = −∫_0^∞e^{−μt}θ_α(t)dt/t. (4) *Comparison.* 𝔪_α(μ) − 𝔠_α(1/μ) = −∫_0^{1/μ}(e^{−μt} − 1)θ_αdt/t −
∫_{1/μ}^∞e^{−μt}θ_αdt/t, and with |θ_α| ≤ C_θq_α²: |…| ≤ C_θq_α²[∫_0^{1/μ}μ dt + ∫_1^∞e^{−u}du/u] =: A_0q_α² **[RFL8-fix S8-2:
A_0 = C_θ(1 + E_1(1)) depends on N and H_1 through γ_α (in C_θ), not "absolute"]**. (5) 𝔠_α(ℓ²) =
−∫_0^1θ_αdt/t − (7q_α²/(32π²))log ℓ² − ∫_1^{ℓ²}O(q_α²/t)dt/t = −(7q_α²/(16π²))log ℓ + O(q_α²) = −(21q_α²/(48π²))log ℓ + O(q_α²). ∎
*Proof of (Q1)(c)* **[RFL8-fix (tally): a REMARK (duplicate of COV-GI-∞ with GH-log (b)), not counted]**. Given (L-loc2), Corollary COV-GI-∞ makes the left side Γ^{W0}_n + Γ^cov_n a C² density at each n; all
operators involved commute with the torus action, so the density is a sum over the Cartan sector and the root sectors of
gapped covariant densities, each C² (the same argument per sector); so c^tot_{n,α} exists. G_⊥,n,α := (total)_α − G_gh,n,α
on 𝔉_n (definition; X(0) read as lim_{f→0}X(f), which exists for G_gh since g is continuous, hence for G_⊥). So
[f²]_lim G_⊥,n,α = c^tot_{n,α} − [f²]_lim G_gh,n,α, and GH-log (b) bounds the latter set. With §58, GH-log (c) applies and the set
is the point c^tot_{n,α} + 2c_gq_α²log ℓ. ∎
*Proof of (Q2).* (R1) At B = 1: the weights are the contour weights with leg signs, 𝔇_c = id (DW_♮(1) is the projection onto
su(N), and contour sums of an su(N) field lie in su(N)), so T_k(1) = Q_root (§37, l.1889), T^str_k(1) = Q_str, h_k(1) = h,
D^♭_1 = d, and R_k(1) = Q_root − Q_str + d∘h = 0 (LINEAR_PACKAGE §1.2). For general B fix c and use the Cartan gauge symmetric
about c_X (Cartan gauge transformations act on the root sector by unimodular phases and change neither ||R_k|| nor entry
moduli). In it the link angles on the contour support of c (diameter ≤ p_L + L in level-k units) are F times bounded
polynomials in the position, so the weights ω_c, the endpoint phases of T^σ_y(B), the transports in h_k and D^♭, and 𝔇_c
(analytic in M̄_c near 1, M̄_c analytic in the angles) are analytic in F on |q_αF| ≤ ε_1 with F-derivatives bounded by a
constant independent of c (magnetic-translation covariance: the configuration seen from c_X is the same for every c of a
given direction, up to the gauge phase) and of k (the chain is uniform in level units, and T_k depends on the level-k data
only). Hence |R_k(B)(c, b)| ≤ C|q_αF| **[RFL8-fix S8-3: ≤ C max_i|h_iF| for N ≥ 3]** on the finite support, and Schur's test gives ||R_k(B)|| ≤ C_R|q_αF|. Covariance: §30
(l.1509 at session 4), one step. (R2) For b ∈ S_y the weights ω_c(σ, y, b) are unimodular phases times (1/24)L^{−4}, and the
number of (σ, y) with b ∈ S_y is the multiplicity of b in Q_str's straight average, so |Σ_{(σ,y):b∈S_y}ω_c| ≤ Q_str(c, b). The root
block of DW_♮ at M̄_c: for N = 2, M̄_c = r_cW_c exactly (an average of SU(2) matrices is a nonnegative multiple of an SU(2)
matrix), W_♮(M) = M/(det M)^{1/2}, and the root block of DW_♮ is multiplication by r_c^{−1} (det M changes only at second
order in the root directions); r_c = |avg of the contour transporters| ≥ 1 − ½(q_αa_LF)² (a_L the largest contour area). For
N ≥ 3, at a Cartan M = diag(m_i) the maximiser of Re tr(V^{−1}M) is V = diag(e^{iψ_i}) with ψ_i = arg m_i − N^{−1}Σ_jarg m_j
**[RFL8-fix S8-3: up to O(|Σ_jarg m_j|) = O(F³); exact only when Σ_jarg m_j = 0 (Lagrange: r_isin(arg m_i − ψ_i) must be the
same for every i); the bound r'_i ≥ 1 − c_WF² below is unaffected]**, and in
the root direction (i, j) the second variation is ½|y|²(r'_i + r'_j), r'_i := Re(m_ie^{−iψ_i}), while the linear coupling to δM
has unimodular coefficients on δM_ij and δM_ji; so the root block of DW_♮ is bounded by 2/(r'_i + r'_j) applied to the common
weight sum. Each m_i is an average of unimodular phases of spread ≤ q_αa_L|F|, and Σ_iarg m_i = O(F³) (each transporter has
determinant 1 and arg of an average of e^{iθ} is the average of θ up to O(θ³)), so r'_i ≥ 1 − c_W(q_αF)². In both cases
|T^str_k(B)(c, b)| ≤ r_*(F)^{−1}Q_str(c, b). For products, |(XY)(a, c)| ≤ Σ_b|X(a, b)||Y(b, c)| and Q_str has a nonnegative kernel,
so |T^str_{n−1}⋯T^str_jv| ≤ Π_kr_*(F_k)^{−1}Q_str^{n−j}|v| pointwise, and ||Q_str^{n−j}|v||| ≤ L^{−(n−j)}||v|| (GS-2 (e) applied to the
real field |v|). (R-damp) By (R1)'s covariance, T_k(B_k) maps Ran D_{B_k} into Ran D_{B_{k+1}}, so P_⊥(B_{k+1})T_k = P_⊥(B_{k+1})T_kP_⊥(B_k)
and P_⊥(B_n)A_j = Π_k(P_⊥T_kP_⊥)·P_⊥(B_j); and P_⊥(B_{k+1})D^♭_{B_{k+1}} = 0, so P_⊥T_kP_⊥ = P_⊥(T^str_k + R_k)P_⊥ and
||P_⊥T_kP_⊥|| ≤ r_*(F_k)^{−1}L^{−1} + C_R|q_αF_k| **[RFL8-fix S8-3: read φ_k as max_i|h_iF_k| throughout this step for N ≥ 3]**. Per root, read q_αF_k as the root flux φ_k := F_{k,α} of B_k (Lemma B-flux
per root, [RFL6-fix S6-5]; φ_k = q_αF_k for SU(2)); the induction of §37 (b), applied to each diagonal phase, gives
|φ_k| ≤ 2L^{2k}|q_αf| for k < n when |f| ≤ ε_0L^{−2n}, so Σ_{k<n}|φ_k| ≤ 2q_αε_0/(L² − 1) and Σ_{k<n}φ_k² ≤ 4q_α²ε_0²/(L⁴ − 1); hence
||P_⊥A_j|| ≤ L^{−(n−j)}Π_k(r_*^{−1} + LC_R|φ_k|) ≤ e_1L^{−(n−j)}, e_1 := exp(2c_Wq_α²ε_0² + 2LC_Rq_αε_0/(L² − 1)) (for c_Wφ_k² ≤ ½). Then, with π_- ≤ Π_j ≤ π_+ (§30) and COV-str (ii),
κ^{−1}π_+^{−1}P_⊥ ≤ P_⊥𝒞_nP_⊥ = κ^{−1}Σ_j(P_⊥A_j)Π_j^{−1}(P_⊥A_j)^† ≤ κ^{−1}π_-^{−1}e_1²(1 − L^{−2})^{−1}P_⊥ (the j = n term, A_n = 1, for the
lower bound). ∎
*Reading.* (1) S7-3 is answered both ways: (V-IR) is now stated for limit points ((Q1)(c)-(d)), and G-mag (vi) is proven
(§58), so c^⊥_{n,α} exists as a number given (L-loc2). (2) S7-2 is answered: (R1), (R2) are written on the root-sector maps
T_k(B) and proven in their soft form (C_R, c_W not computed), and (V-IR) is an operator-level statement with an explicit
cutoff, in two equivalent forms (mass ℓ^{−2}, or proper time ℓ²) by Lemma VIR-eq. (3) (R-damp) is the root-sector analogue of
COV-⊥-C (b): the transverse noise of every level is damped geometrically, n-uniformly, in the root sectors. It gives
operator bounds on P_⊥𝒞_nP_⊥, not its f² coefficient, and P_⊥(B_n) is still non-local, so the level-n ⊥ group is not
thereby an MS-type density. (4) (R1)'s remainder is first order in F (not second as in the Cartan sector, where τd = 0);
(R-damp) survives because Σ_k|F_k| is a geometric sum dominated by its top term ε_0.

## 60. The scalar proxy: Lemma S-red: PROVEN-HERE ((V-IR-S) itself OPEN)

Statement: (Q4) of §57.
*Proof.* (i) M_f has range ≤ one level-n block and 𝒞_n = C_n(f)·1 with C_n(f) > 0 analytic (COV-sc (2)), so K_f := Δ_f +
C_n(f)^{−1}M_f^†M_f is finite range, analytic in f, and commutes with the magnetic translations of ℓZ⁴. Gap at f = 0: K_0 is
ℓZ⁴-periodic, so a direct integral of finite matrices K_0(θ), continuous in θ; if ⟨φ, K_0(θ)φ⟩ = 0 then Δ_0φ = 0 (φ constant,
θ = 0, or φ = 0) and M_0φ = 0, and M_0 maps a nonzero constant to a nonzero constant; so K_0 ≥ c_n > 0. The IMS argument of
Lemma N-f (iii) (finite range) gives K_f ≥ c_n/2 for |f| ≤ ε'_n. Lemma MS (ii)-(iii) give C² of τ log K_f; log C_n is analytic.
(ii) For 0 < |f| ≤ ε'_n, ~~Δ_f ≥ c(f) > 0 (Δ_f = Δ^{12}_f ⊗ 1 + 1 ⊗ Δ^{34}, and the 2D Harper operator at flux f ∉ 2πZ has a gap above
0; standard)~~ **[RFL8-fix S8-4: no Harper-gap import is needed: on each finite flux-quantised magnetic Bloch fibre, Δ_f(θ)ψ = 0
gives ⟨ψ, Δ_f(θ)ψ⟩ = Σ_b|ψ(x) − U_bψ(x + μ)|² = 0, so ψ is covariantly constant, hence |ψ| is constant and, if ψ ≠ 0, every
plaquette holonomy is trivial, which fails at f ∉ 2πZ; so ψ = 0 and each fibre matrix Δ_f(θ) is invertible, which is all
that (ii) uses]**, so on every flux-quantised magnetic Bloch fibre det(Δ + M^†C^{−1}M)·det C = det Δ·det(C + MΔ^{−1}M^†) (matrix
determinant lemma); integrating over the fibres gives (ii) between densities (ℓ^{−4} level sites per fine site).
(iii) G_S,n is continuous at 0 by (i), and g is continuous (g(φ) − g(0) = Ψ(φ) → 0), so Y(f) := ℓ^{−4}[τ_n log 𝒦_n(f) + g(ℓ²f)]
has a limit Y(0) as f → 0. By (ii),
  (G_S,n(f) − G_S,n(0))/f² = [ψ(f) − ψ(ℓ²f)] + (Y(f) − Y(0))/f²,  ψ(f) − ψ(ℓ²f) = 2c_g log ℓ + c'(f) − c'(ℓ²f),
and by Theorem G-mag (vi) (§58) c'(f) − c'(ℓ²f) → 0. The left side tends to c^S_n by (i); hence (Y(f) − Y(0))/f² → c^S_n −
2c_g log ℓ =: ρ_n. With F = ℓ²f, (Y(f) − Y(0))/f² = F^{−2}[τ_n log 𝒦_n(F/ℓ²) + g(F) − (F = 0)], as stated.
(iv) 𝔠^S(ℓ²) = ½∫_0^{ℓ²}m dt/t = 2c_g log ℓ + ½κ_0 + O(ℓ^{−2}) (m = m_∞ + O(1/t)), so c^S_n − 𝔠^S(ℓ²) = ρ_n − ½κ_0 + O(ℓ^{−2}). ∎
*Reading.* (1) The scalar (V-IR) is reduced exactly to the n-uniform boundedness of ρ_n, the F² coefficient of the IR-safe
LEVEL-n quantity log det(𝒦_nΔ^{(n)}_F): the block-averaged magnetic Green's function plus the noise, against the level-n
nearest-neighbour magnetic Laplacian. Its log ℓ part is EXACTLY 2c_g log ℓ (the same exact-scaling mechanism as
GH-log, with the opposite sign: here the fine operator is in the numerator). (2) Why ρ_n should be bounded (not proven):
at F = 0 the level-n symbol ℓ²𝒦̂_n(p)λ_n(p) converges uniformly as n → ∞ (block-spin Green's functions in level units:
ℓ²Σ_{m∈(Z/ℓ)⁴}|D_ℓ|²/λ((p + 2πm)/ℓ) → Σ_{m∈Z⁴}Π_μ|sin(p_μ/2)/((p_μ + 2πm_μ)/2)|²/|p + 2πm|²) and is bounded above and below; the F²
coefficient needs the magnetic (twisted) version of this convergence with two F-derivatives, for a symbol that is only
C^{1,1} at p = 0 (λ_n(p)/|p|² is not smooth there). That is the content of (V-IR-S), OPEN. (3) The vector root sector does
not reduce this way: the fine transverse operator H|_{ker D_0^*} at U_f has spectrum down to ≈ −|q_αf| (Nielsen-Olesen, §45
Reading (2)), so log det_{ker D_0^*}H has no real f-expansion and the matrix determinant lemma cannot split it off; this is
why (Q1)(d) is stated against the mass-regulated 𝔪_α(ℓ^{−2}), and the vector analogue of ρ_n (G_⊥ minus the mass-regulated
fine term) needs a comparison estimate (Duhamel in proper time, or the IR term as a mass bound), OPEN.
**[RFL8-fix S8-5] Scope: the obstruction is to the determinant-lemma split at finite constant f only. At U = 1 (two-point
form via MS (iv) and F-id-exp) all operators are nonnegative (H(1) = d^*d per colour, Ã(1) ≥ c_n, K_F(1) = d^*d + dd^*) and the
split is available; β is the f² germ at f → 0 with n fixed, where the Nielsen-Olesen modes at ≈ −|q_αf| ≥ −q_αε_0ℓ^{-2} are
dominated by the IR mass, so they never enter. See REVIEW_FLOW_S8 §7.3, and §64 (S5) for the vector two-point reduction.**

## 61. Session-8 check f11 (ADDED AFTER the run; checks/f11_criteria.md, f11_scalar_vir.py, f11_out.txt, f11_time.txt)
Criteria written 06:51:34 UTC before any f11 script (stat in FLOW_LOG); two disclosed pre-run script edits (fit-column
scaling; Part G quadrature repair after smoke test 1 gave nan), no criterion changed; smoke tests 1-2 in the scratchpad.
Official f11: one NUMERIC LOCK acquisition 06:55:52-07:02:17 UTC, nice 10, 1 thread, load 3.3, memory free 38%; 384.5 s,
peak RSS 695 MB. **15/15 verdict lines PASS; both controls fail as required.**
- **G (Theorem G-mag (vi)):** κ_0 = 6.154034e-4, I_a = 9.242186e-3, I_b = 0.1794995, **c'_0 = 1.385869e-3** against f9's
  geometric extrapolation 1.385834e-3 (|diff| 3.5e-8, threshold 5e-6); quadrature stable to 1.7e-15. Reported:
  (c'(φ) − c'_0)/φ = 1.109e-4, 1.186e-4, 1.234e-4, 1.261e-4, 1.278e-4, 1.286e-4 at Q = 16, …, 512 (one sign, tending to a
  constant: c'(φ) = c'_0 + O(φ), consistent with f9 G2b; the rate is not proved).
- **R (implementation):** the 2D reduction (two orders, 34 by aliases, determinant lemma) equals the direct 4D torus
  (6, 6, 3, 3) with all 24 S4' orders to 1.6e-15 (one order only: 3.6e-6, fails as required); gauge covariance |ΔG_S| = 0.0
  (bit-identical; no transport phases: 5.7e-3, fails as required); magnetic Bloch vs direct 2D torus 1.3e-14 (spectra),
  2.2e-16 (G_S); C_n against COV-sc's closed form, A_jA_j^† diagonal and constant, to round-off.
- **S (scalar proxy, s = 4, L = 3, level fluxes Φ = 2π/Q', Q' = 8, …, 32):** grids converged (≤ 1.6e-13); **the total is IR
  safe**: fitted f²log(1/f) coefficient 2.0e-8 (n = 1), 3.0e-8 (n = 2) against c_g = 1.055e-3, while its pieces g and E
  carry ±0.94 c_g (n = 1), ±0.85 c_g (n = 2) (finite-window values of the ±c_g of G-mag (v); equal and opposite to the
  printed digits); a1 stable to 3e-7 relative. **c^S_1 = 7.12343e-4, c^S_2 = 2.88549e-3; ρ_1 = −1.60667e-3, ρ_2 =
  −1.75254e-3; c^S_n − 𝔠^S(ℓ²) = −1.9439e-3, −2.0635e-3. Prediction S-VIR: (c^S_2 − c^S_1)/(2c_g log 3) = 0.9371**
  (threshold |· − 1| ≤ 0.25).
- **Reading.** (1) Theorem G-mag (vi)'s limit formula agrees with an independent rational-flux computation to 3.5e-8 out
  of 1.4e-3: S8-F1 does not occur. (2) In the scalar proxy with the real S4' axial transporters, the IR term and the
  level-n covariance make the total exactly IR safe (S8-F3 does not occur), and from n = 1 to n = 2 the f² coefficient
  grows by 0.937 × 2c_g log 3; the change of ρ_n, −1.46e-4, is 6% of the log step. This supports (V-IR-S) at n ≤ 2 (S8-F2
  does not occur); two levels cannot show n-uniformity, and ρ_n's convergence is not tested. (3) What f11 is: the scalar
  proxy (COV-sc's chain, f6's averages), not the vector root sector; no Wilson Hessian, no P_⊥, no gauge fixing.

## 62. Session-8 outcomes against §57 (ADDED AFTER the derivations and the check)
- **Step 1 (fixes): DONE.** S7-1, S7-4 and the S7-5 leftovers applied in place, tagged [RFL7-fix] (11 tag occurrences).
- **S7-2: DONE.** (R1), (R2) written on the root-sector maps T_k(B) and proven in soft form, with the Corollary (R-damp)
  (n-uniform transverse damping and c_-κ^{-1}P_⊥ ≤ P_⊥𝒞_n(U_f)P_⊥ ≤ c_+κ^{-1}P_⊥ in every root sector; C_R, c_W not computed).
  (V-IR) is written at operator level with an explicit cutoff, (Q1)(d), in mass form 𝔪_α(ℓ^{-2}) and proper-time form
  𝔠_α(ℓ²), equivalent by Lemma VIR-eq (PROVEN).
- **S7-3: DONE both ways.** (V-IR) is stated for limit points ((Q1)(c), PROVEN given (L-loc2)), and **Theorem G-mag (vi) is
  PROVEN** (§58; one import, Donsker for the free walk), so GH-log (c), (d) are unconditional and c^⊥_{n,α} exists as a
  number given (L-loc2). f11 G confirms c'_0.
- **Step 3 (f11): DONE**, 15/15; S-VIR ratio 0.937.
- **Step 4 (analytic (V-IR)):** scalar: Lemma S-red reduces (V-IR-S) exactly to sup_n|ρ_n| < ∞, ρ_n the F² coefficient of
  the IR-safe level-n quantity log det(𝒦_nΔ^{(n)}_F), with the log ℓ part exactly 2c_g log ℓ; the n-uniform bound on ρ_n is
  OPEN (it needs the magnetic, twice-F-differentiated form of the convergence of the block-spin Green's function in level
  units, for a symbol only C^{1,1} at p = 0). Vector root sector: NOT reduced; the determinant-lemma split is blocked by the
  Nielsen-Olesen negative modes of H|_{ker D_0^*}, so (V-IR) stays in the mass-regulated form (Q1)(d), OPEN.
  **[RFL8-fix S8-5] At finite constant f only; at U = 1 (two-point form via MS (iv) and F-id-exp) all operators are
  nonnegative and the split is available (REVIEW_FLOW_S8 §7.3; §64 (S5)).**
- **Theorem UNIV now (minimal list):** conditional on (V-IR) on G_⊥ in the form (Q1)(d) (crux, OPEN) and (L-loc2)
  (ARGUED). G-mag (vi) is no longer a condition. UNIV-rate additionally needs (s1), (s2⊥) and the rate of c'(φ) → c'_0.

## 63. Tally after session 8 (FLOW.md items; session-8 items unreviewed)
- **PROVEN-HERE: 40 (sessions 1-7, as confirmed by REVIEW_FLOW_S7, with its scope annotations) + 7 (session 8) = 47.**
  **[RFL8-fix (tally): 46, as corrected by REVIEW_FLOW_S8 §8. (Q1)(c) is a REMARK, not a counted item: it restates
  Corollary COV-GI-∞ (which already defines c^⊥_n as total − ghost) together with the one-line GH-log (b) radius. Scope
  annotations: G-mag (vi) uses textbook probabilistic facts (§58 Reading (1)); (R1), (R2), (R-damp) soft (constants not
  computed), N-dependent through max_i|h_i|; VIR-eq's A_0 depends on N and H_1; S-red (iii) uses §58.]**
  Session 8: Theorem G-mag (vi) (one import, re-verified hypotheses); Lemma VIR-eq with (Q1)(a); the well-posedness
  statement (Q1)(c) (given (L-loc2)); Lemma (R1) (soft; C_R not computed); Lemma (R2) (c_W not computed); Corollary
  (R-damp); Lemma S-red. Upstream inputs used: Lemma G-mag (i)-(v), Theorem V-heat, §46's decoupling, Lemma MS, Lemma N-f's
  IMS argument, COV-GI-∞, Proposition GH-log (b), Lemma COV-str, Proposition COV-sc, GS-2 (e), LINEAR_PACKAGE §1.2, §30
  covariance, Lemma B-flux (per root).
- **IMPORTED-AND-REVERIFIED:** L4b; Donsker's invariance principle for the free walk (§58 (b1)).
- **ARGUED, not counted:** (L-loc2). (G-mag (vi) moves from ARGUED to PROVEN-HERE.)
- **GAP:** Corollary UNIV-rate (unchanged). **RETIRED / WRONG as stated:** as in §56.
- **OPEN:** (V-IR) on G_⊥ in the form (Q1)(d) [s-P] (crux); (V-IR-S) (sup_n|ρ_n| < ∞) [s-P]; (L-loc2) to be proved [s];
  (s1) [s-P], (s2⊥) [s-P] (rate only); the rate of c'(φ) → c'_0 [s] (rate only); (COV-GI) at non-critical backgrounds [s];
  FI-1 [cross-lane]; HIST's restatement of CL^J's Setting [cross-lane].
- **Checks:** f11 (G-acc, G-c0, R1-R4, S-grid ×2, S-IR ×2, S-stab ×2, S-VIR PASS; R1-ctl, R2-ctl fail as required).

## 64. Session-9 targets and PRE-STATED (session 9) statements (written 2026-10-28 07:37 UTC, the first edit of session 9: before the [RFL8-fix] edits and before any session-9 proof, criteria file or script)

Binding input: REVIEW_FLOW_S8.md (tally 46; fixes S8-1..S8-6; the route of its §6 and §7.3; its next target §10). The
fixes S8-1..S8-6 are applied after this section, in place, tagged **[RFL8-fix]**. Notation of §57 (Q4) and §60.
Scalar proxy setting: fine Z⁴, complex unit-charge scalar, odd L, ℓ = L^n, κ_j = sL^{2j}; Q_k(U) the S4' axial averages of
Proposition COV-sc run on the fine links of an arbitrary U(1) configuration U; A_j(U) := Q_{n−1}(U)⋯Q_j(U) (A_n = 1),
M_U := A_0(U), **𝒞_n(U) := Σ_{j=1}^nκ_j^{-1}A_j(U)A_j(U)^†** (the covariant extension of COV-sc's 𝒞_n; at U_f it is C_n(f)·1),
  G_S,n(U) := τ log(Δ_U + M_U^†𝒞_n(U)^{-1}M_U) + ℓ^{-4}τ_n log 𝒞_n(U)  (per fine site; = §57 (Q4)'s G_S,n at U = U_f).
Plane-wave background U^{ε,p,ϑ}: U_{x,1} = exp(iε cos(px_2 + ϑ)), all other links 1; h_n(p) := [ε²]G_S,n(U^{ε,p,ϑ}) (per fine site).
For the vector sector: setting of §41-§46, §57 (Q1); Ã, Δ', E', D_U as in §45 (l.2331) and §41 (l.2107-2117).

**PRE-STATED (session 9).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Each hypothesis is named in the statement; nothing below uses an ARGUED or OPEN item as if proven.
Proofs follow in later sections; any change of a statement after this point is logged as such.

**(S1) Lemma S-2pt (the scalar proxy in two-point form at U = 1).** For every n ≥ 1:
(a) 𝒞_n(U) is diagonal on level-n sites for every U, and D𝒞_n(1) = 0 (first derivative at U = 1, every real direction);
(b) for 0 < |p| < π/ℓ, h_n(p) exists, does not depend on ϑ, and equals ¼∫dK/(2π)⁴ ℓ^{-4}[T_n(K, p) − I_n(K, p)], where T_n
  (tadpole) and I_n (bubble) are traces over the alias fibre of level momentum K (dimension ℓ⁴ + 1) of products of
  𝔐_0(K)^{-1}, 𝔐_0(K + ℓpe_2)^{-1} and the first- and second-order vertices at U = 1 of the extended matrix
  𝔐(U) := [[Δ_U, M_U^†], [M_U, −𝒞_n(U)]], and 𝔐_0(K)^{-1} is diagonal plus rank one on the fibre;
(c) h_n is real-analytic and even in p near 0, h_n(0) = 0, and **c^S_n = lim_{p→0}h_n(p)/(2 sin²(p/2))** (the F-id link of the
  proxy, through Lemma MS (iv) and Lemma F-id-exp).
**(S2) Proposition S-tel (exact decomposition of the proxy into RG steps).** Put Γ_0 := Δ_U^{-1}, Γ_{k+1} := Q_kΓ_kQ_k^† +
κ_{k+1}^{-1}1 and H_k := Γ_k^{-1} + κ_{k+1}Q_k^†Q_k (operators on level-k sites; at U = U_f with 0 < |f| small). Then:
(a) Γ_n = 𝒦_n := 𝒞_n + M Δ^{-1}M^† (§57 (Q4)), and G_S,n = Σ_{k=0}^{n−1}Φ_k with Φ_k := L^{-4k}τ_k log H_k − L^{-4(k+1)}log κ_{k+1}
  (per fine site); Φ_k does not depend on n;
(b) each H_k is a gapped, exponentially local, magnetic-translation covariant operator whose f-dependence satisfies the
  hypotheses of Lemma MS (iii) (and the Hessian hypothesis of MS (iv)), for |f| ≤ ε_k; Φ_k extends to f = 0 as a C² density;
(c) hence c^S_n = Σ_{k<n}φ_k with φ_k := [f²]Φ_k = c^S_{k+1} − c^S_k (c^S_0 := 0); in level-k units φ_k = [F²]𝔉(Γ̃_k, Q)(F) for
  one fixed functional 𝔉 (F = L^{2k}f the level-k flux), where Γ̃_k := L^{2k}Γ_k obeys the k-independent recursion
  Γ̃_{k+1} = L²Q(F)Γ̃_kQ(F)^† + s^{-1}1, Q(F) the level-unit S4' average at level flux F;
(d) consequently (V-IR-S) ⟺ sup_n|Σ_{k<n}(φ_k − 2c_g log L)| < ∞, and ρ_n = Σ_{k<n}(φ_k − 2c_g log L).
**(S3) Lemma S-fix (the level-unit two-point fixed point at U = 1).** Let γ_k(K) be the symbol of Γ̃_k at U = 1 (level-k
momentum K). Then |K̂|²γ_k → |K̂|²γ_* uniformly on the level Brillouin zone, together with K-derivatives of order ≤ 2 away
from K = 0, at rate CL^{-2k}, where γ_*(K) := Σ_{m∈Z⁴}Π_μ[sin(K_μ/2)/((K_μ + 2πm_μ)/2)]²/|K + 2πm|² + (s(1 − L^{-2}))^{-1} and
K̂_μ := 2 sin(K_μ/2); and the U = 1 symbol of L^{-2k}H_k is bounded above and below uniformly in k.
**(S4) Target theorem (V-IR-S) with a rate.** There are C_S < ∞ and θ < 1 with |φ_k − 2c_g log L| ≤ C_Sθ^k for all k; hence
ρ_n converges, sup_n|ρ_n| < ∞ and |ρ_n − ρ_∞| ≤ C_Sθ^n/(1 − θ). [Route: (S1)-(S3) and the geometric convergence, in level
units, of the first- and second-order vertex functions at U = 1 of Γ̃_k (equivalently of M_U, Δ_U and the alias sums in
level units). Any part that is not proved here is reported OPEN, with what it needs.]
**(S5) Lemma V-2pt (the vector root sector in two-point form at U = 1; REVIEW_FLOW_S8 §7.3 (V1)-(V3)).** Given (L-loc2)
(hypothesis), for every n and root α:
(a) 2c^tot_{n,α} equals the p² coefficient of the (12, 12) component of the U = 1 Hessian kernel of the root-α block of
  ½log det Ã − log det Δ' + ½log det 𝒞_n (MS (iv) with F-id-exp), and c^⊥_{n,α} = c^tot_{n,α} + 2c_gq_α²log ℓ (GH-log (c));
(b) for μ > 0, 2𝔪_α(μ) equals the same p² coefficient for log det_C(K_F + μ) − log det_C(Δ_0 + μ) at U = 1;
(c) with ρ^V_{n,α} := c^⊥_{n,α} − 𝔪_α(ℓ^{-2}): ρ^V_{n,α} is ½ × the p² coefficient of an explicit U = 1 one-loop kernel in
  which every propagator is the inverse of a nonnegative operator plus a strictly positive one (no negative mode enters),
  and (V-IR) in the form (Q1)(d) ⟺ sup_{n,α}q_α^{-2}|ρ^V_{n,α}| < ∞;
  **[RFL9-fix S9-5: "explicit" → the kernel is *defined* by the U = 1 Hessians; no fibre formula is written (unlike S-2pt
  (b)); "≥ c > 0" holds at each n with n-dependent constants, not level-uniformly: Δ'(1) has gap ≍ ℓ^{-4} in fine units, so
  the ghost must be removed exactly (GH-log (c), or (T5) of §73), never bounded, in an n-uniform route]**
(d) (the reviewer's check (V2), as a question with two admissible answers) either K̃(1) := H(1) + D E'D^*(1) is injective at
  every level momentum K ≠ 0, so the Woodbury reference K̃ is available, or it has zero modes there, and the reference is
  K_F(1) + μ with μ carried explicitly.
**(S6) Question (vector telescoping).** Does the vector total ½log det Ã − log det Δ' + ½log det 𝒞_n admit an exact
RG-step decomposition of the form (S2) (a), with n-independent step densities? Either answer is an outcome; a NO names
the term that breaks it.

**Check f12** (criteria file first, its stat into FLOW_LOG before any f12 script; jobs < 20 min, < 1 GB, memory free
≥ 35%): the scalar proxy at U = 1 in momentum space by (S1) (b)-(c), L = 3, s = 4, n = 1, 2, 3, 4. **Predictions:**
(a) reproduction of f11's c^S_1 = 7.12343e-4 and c^S_2 = 2.88549e-3 to ≤ 1e-8 absolute (an independent test of the F-id
link in the proxy and of f11); (b) **|ρ_3 − ρ_2| ≤ |ρ_2 − ρ_1|/3 = 4.9e-5** (REVIEW_FLOW_S8 §10 threshold: bounded with an
approach at least as fast as ℓ^{-1}, against a log drift ≈ 1.46e-4); reported: ρ_4, the increments, their ratios. (c) The
vector ρ^V_{n,α} for n = 1..3 if feasible within the budget; otherwise reported as not attempted.

**Failure modes (each a valid outcome).** (S9-F1) the U = 1 two-point value of c^S_n disagrees with f11 by more than 1e-8
(an error in (S1) or in f11); (S9-F2) |ρ_3 − ρ_2| > 4.9e-5 (no fast approach at n ≤ 3: the scalar (V-IR) picture is not
yet visible, or ρ_n drifts); (S9-F3) the increments of ρ_n do not shrink geometrically (against (S4)'s form).

---
# Session-9 proofs (written after §64 and the [RFL8-fix] edits)

## 65. Lemma S-2pt (the scalar proxy in two-point form at U = 1): PROVEN-HERE

Statement: §64 (S1). Fibre notation (level-n momentum K ∈ [−π, π]⁴, aliases k_m := (K + 2πm)/ℓ, m ∈ (Z/ℓ)⁴; fibre vectors
ψ_m := ℓ^{-2}φ̂(k_m), so the fibre inner product is unitary): Λ := diag λ(k_m), λ(k) = Σ_μ4 sin²(k_μ/2); block form factor
D(k) := ℓ^{-4}Σ_{j∈{−h..h}⁴}e^{ik·j} = Π_μD_1(k_μ) (h = (ℓ − 1)/2, the level-n block centred at its level site), and for
fine→level maps X with form factor x(k) (Xφ)^(K) = ℓ^{-2}Σ_mx(k_m)ψ_m, represented by the fibre column ℓ^{-2}x̄.
*Proof.* (a) Diagonality is COV-sc proof (1), which uses only that each level-j site has one level-n ancestor; it holds
for every U. The diagonal entries are Σ_jκ_j^{-1}Σ_{y_j}Π_kL^{-8}|w_k|², w_k the order average of the transport phases
e^{iθ_σ} along the step-k axial paths (θ_σ the line integral of A, U = e^{iA}); at A = 0, d|w_k|² = 2Re(w̄_k dw_k) =
2Re(i avg_σ dθ_σ) = 0 since dθ_σ is real. So D𝒞_n(1) = 0.
(b) By the Schur complement on the level block, det 𝔐(U) = det(−𝒞_n(U))·det(Δ_U + M_U^†𝒞_n(U)^{-1}M_U), so G_S,n = log|det 𝔐|
per fine site (exact on every torus of side a multiple of ℓ with antiperiodic boundary conditions, where Δ_U is invertible
for U near 1; the densities converge to the infinite-volume ones exponentially fast, the operators being gapped and of
finite range, Lemma MS (ii)). At U = 1, 𝔐_0(K) = [[Λ, v], [v^†, −C]] with v := ℓ^{-2}D̄, C := C_n(0) = Σ_jκ_j^{-1}L^{-4(n−j)}
(A_j(1)A_j(1)^† = L^{-4(n−j)}·1), and by block inversion with the Schur complement −(C + Ĝ), Ĝ(K) := v^†Λ^{-1}v,
  𝔐_0(K)^{-1} = (Λ^{-1} ⊕ 0) − α ξξ^†,  ξ := (Λ^{-1}v, −1),  α := (C + Ĝ)^{-1}
(diagonal plus rank one; Λ^{-1} has the single pole at K = 0, m = 0, where 𝔐_0^{-1} stays bounded: 𝔐_0(K) is invertible for
every K because M_0 maps the constant mode to a nonzero constant, S-red (i)). Write cos(px_2 + ϑ) = ½(e^{iϑ}e^{ipx_2} + c.c.).
Multiplication by e^{ipx_2} maps fibre K to fibre K' := K + ℓpe_2 with the same alias labels. The second-order expansion
log det(𝔐_0 + ε𝔐_1 + ε²𝔐_2) = log det 𝔐_0 + ε tr 𝔐_0^{-1}𝔐_1 + ε²[tr 𝔐_0^{-1}𝔐_2 − ½tr(𝔐_0^{-1}𝔐_1)²] + O(ε³), with
𝔐_1 = ½(e^{iϑ}A + e^{−iϑ}A^†) (A: fibre K → fibre K') and 𝔐_2 = ¼𝔚 + (parts of momentum ±2p). Every trace of a product of
ℓZ⁴-periodic operators with a total momentum q ≠ 0 mod 2πZ⁴/ℓ vanishes per site; for 0 < |p| < π/ℓ, 2p is not such a momentum,
so only ϑ-free terms survive: **h_n(p) = ¼∫dK/(2π)⁴ ℓ^{-4}[T_n − I_n]**, T_n := tr 𝔐_0(K)^{-1}𝔚(K), I_n := tr(𝔐_0(K)^{-1}A^†𝔐_0(K')^{-1}A),
and the first-order term vanishes (no zero-momentum part). The vertices, from the explicit construction (S4' averages: in
a background U_{x,1} = e^{ia(x_2)} the step-k phase is e^{iΔ_k a(x_2^*)} with Δ_k the leg in direction 1 and x_2^* the start
(resp. end) x_2-coordinate of the step for the 12 orders with 1 before 2 (resp. after); 34-legs carry no phase):
  A = [[Σ, μ_-], [μ^†, 0]] (the lower-right entry is −D𝒞_n(1)[·] = 0 by (a)), 𝔚 = [[W, ω], [ω^†, −c_2]],
Σ := diag 2 sin k_{m,1}, W := diag 2 cos k_{m,1} (from Δ_U), μ := ℓ^{-2}ū, μ_- := ℓ^{-2}conj(u(k_m + pe_2, −p)), ω := ℓ^{-2}m̄_2, where, with
balanced digits j_μ = Σ_{r<n}d_rL^r, δ_r(q) := (1 + 2cos(qL^r))/3 (so D_1 = Π_rδ_r), G_κ(q) := −(2/3)L^κ sin(qL^κ)Π_{r≠κ}δ_r(q),
F2_i(q; p) := Π_{r<i}δ_r(q)Π_{r≥i}δ_r(q + p):
  u(k, p) = Σ_{κ<n}G_κ(k_1)·½[F2_{κ+1} + F2_κ](k_2; p)·D_1(k_3)D_1(k_4)  (first order, coefficient of (ε/2)e^{iϑ}),
  m_2(k) = −Σ_κL^{2κ}(2/3)cos(k_1L^κ)Π_{r≠κ}δ_r(k_1)·D_1(k_2)D_1(k_3)D_1(k_4)
           + (2/9)Σ_{κ<κ'}L^{κ+κ'}sin(k_1L^κ)sin(k_1L^{κ'})Π_{r≠κ,κ'}δ_r(k_1)·Σ_{i∈{κ,κ+1}, i'∈{κ',κ'+1}}C_{ii'}(k_2)·D_1(k_3)D_1(k_4),
  C_{ii'}(q) := ½[Π_{r∉[i,i')}δ_r(q)Π_{r∈[i,i')}δ_r(q + p) + (p → −p)],
  c_2 = −Σ_{j=1}^nκ_j^{-1}L^{-4(n−j)}Σ_{κ=j}^{n−1}(4/9)L^{2κ}(1 − cos pL^κ)  (zero-mode, coefficient of ε²/4; from |w_κ|² = cos²(Δ_κ(a − a')/2)).
(m_2 is the zero-mode coefficient of ε²/4 of ℓ^{-4}Π_κw_κ: −½Σ_κΔ_κ²⟨a²⟩_κ − Σ_{κ<κ'}Δ_κΔ_{κ'}ā_κā_{κ'} with [a(x)a(y)]_0 = 2cos p(x − y);
at p = 0 it reduces to −j_1², the second order of e^{iaj_1}, as it must.) Inserting 𝔐_0^{-1} = D_0 − αξξ^† (D_0 := Λ^{-1} ⊕ 0):
  T_n = Σ_mW_m/λ_m − α[v^†Λ^{-1}WΛ^{-1}v − 2Re v^†Λ^{-1}ω − c_2],
  I_n = tr(Λ^{-1}ΣΛ'^{-1}Σ) − α'w^†Λ^{-1}w − αz^†Λ'^{-1}z + αα'|Ξ|²,
w := ΣΛ'^{-1}v' − μ, z := ΣΛ^{-1}v − μ_-, Ξ := ξ'^†Aξ = v'^†Λ'^{-1}ΣΛ^{-1}v − v'^†Λ'^{-1}μ_- − μ^†Λ^{-1}v (primes: fibre K'), using
tr(D_0A^†ξ'ξ'^†A) = ||D_0^{1/2}A^†ξ'||² and tr(ξξ^†A^†ξ'ξ'^†A) = |ξ'^†Aξ|². All entries are real (D_1, δ_r real; G_κ real).
Every fibre sum is of the form Σ_m Π_μx_μ(k_{m,μ})/(λ(k_m)^aλ(k_m + pe_2)^b), a + b ≤ 3, x_μ separable, as stated.
(c) G_S,n(U) is a covariant construction (U ↦ (Δ_U, M_U, 𝒞_n(U)), each covariant under U(1) gauge transformations, and
log|det 𝔐| invariant); K(U) := Δ_U + M_U^†𝒞_n(U)^{-1}M_U is finite range and polynomial/analytic in the links near 1, gapped
(K(1) ≥ c_n, S-red (i)), and 𝒞_n(U) is diagonal and ≥ κ_n^{-1}/2 near 1. So the origin-cell density has an exponentially
decaying Hessian at U = 1 (each second link derivative is a product of resolvents (K + s)^{-1} with finite-range
derivatives, Combes-Thomas; the hypothesis of MS (iv) as in §51). Lemma MS (iii)-(iv) (read for U(1) at unit charge: the
proofs use only covariance, the gap and the exponential decay) and Lemma F-id-exp give: the Hessian at U = 1 is
H_0(a, a) = h_0(da, da) with h_0 an exponentially decaying, ℓZ⁴-periodic quadratic form on plaquette variables, and
2c^S_n = H_0(𝓛Φ, 𝓛Φ)/(Vφ²) = ĥ(0) := the sum per fine site of all (12, 12) entries of h_0. For the plane wave, da has the single
component F_x = a_x − a_{x+e_2} = 2ε sin(p/2)sin(px_2 + p/2 + ϑ) in the plane 12, so (the umklapp cross terms vanish for
0 < |p| < π/ℓ, as in (b)) ½H_0(a, a)/V = ½ĥ(pe_2)·avg F² = ε²ĥ(pe_2)sin²(p/2), where ĥ(q) := the per-site sum of the (12, 12)
entries of h_0 weighted by cos q·(x − x'), analytic and even in q (exponential decay; reflection x_2 → −x_2). The first
derivative of G_S,n at 1 vanishes (Dρ_0(1) = 0: real symmetric K(1) and (a)). Hence h_n(p) = ĥ(pe_2)sin²(p/2): h_n is
real-analytic and even, h_n(0) = 0 (at p = 0 the background is a constant pure gauge), and h_n(p)/(2sin²(p/2)) = ĥ(pe_2)/2 →
ĥ(0)/2 = c^S_n. ∎
*Reading.* (1) This is the reviewer's route (REVIEW_FLOW_S8 §6 (1)): the f² coefficient of the gapped proxy is a one-loop
vacuum polarisation at U = 1, translation invariant on the level lattice; no magnetic Bloch decomposition, no Harper
spectrum. (2) The p = 0 integrand is a total K-derivative (constant A_1 is pure gauge), which f12 subtracts pointwise.
(3) In the proxy the noise covariance has no first-order vertex at U = 1 ((a)); only its zero-mode second-order vertex
c_2 (a number) enters.

## 66. Proposition S-tel (exact decomposition of the proxy into RG steps): PROVEN-HERE

Statement: §64 (S2).
*Proof.* (a) Unrolling the recursion, Γ_n = A_0Δ^{-1}A_0^† + Σ_{j=1}^nκ_j^{-1}A_jA_j^† = M Δ^{-1}M^† + 𝒞_n = 𝒦_n. On a flux-quantised
torus (or an antiperiodic one at U near 1) where Δ_U is invertible: for invertible Γ on level-k sites and Q: level k →
level k + 1, det(QΓQ^† + κ^{-1}1) = κ^{-N_{k+1}}det(1 + κQΓQ^†) = κ^{-N_{k+1}}det(1 + κΓQ^†Q) = κ^{-N_{k+1}}det Γ·det(Γ^{-1} + κQ^†Q)
(Sylvester), so log det Γ_{k+1} = log det Γ_k + log det H_k − N_{k+1}log κ_{k+1}. Summing from log det Γ_0 = −log det Δ and
using S-red (ii) (G_S,n = τ log Δ + ℓ^{-4}τ_n log 𝒦_n) gives G_S,n = Σ_{k<n}Φ_k per fine site (N_k/V = L^{-4k}). Γ_k, H_k are built
from Δ, Q_0, …, Q_k only, so Φ_k does not depend on n. In terms of inverses only: Γ_0^{-1} = Δ_U, H_k = Γ_k^{-1} + κ_{k+1}Q_k^†Q_k,
Γ_{k+1}^{-1} = κ_{k+1} − κ_{k+1}²Q_kH_k^{-1}Q_k^† (Woodbury), so all objects are defined whenever the H_k are invertible, also at
U = 1.
(b) *Variational form.* ⟨ψ, Γ_{k+1}^{-1}ψ⟩ = min_φ[⟨φ, Γ_k^{-1}φ⟩ + κ_{k+1}||ψ − Q_kφ||²] (the Schur complement of the nonnegative form
on (φ, ψ); the minimiser is H_k^{-1}κQ_k^†ψ). By induction Γ_k^{-1} ≥ 0 and, at U = 1, ker Γ_k^{-1} = constants (on the zero-momentum
fibre): true for Δ; if ⟨ψ, Γ_{k+1}^{-1}ψ⟩ = 0 the minimiser is in ker Γ_k^{-1} and ψ = Q_kφ is a constant, and constants are in the
kernel. *Gap at U = 1.* H_k(1) is level-(k+1)-periodic, a direct integral of L⁴ × L⁴ matrices continuous in the level-(k+1)
momentum (exponential locality, below); ⟨φ, H_k(1)φ⟩ = 0 forces φ constant and Q_kφ = 0, impossible for φ ≠ 0 (Q_k maps a
nonzero constant to a nonzero constant); compactness gives H_k(1) ≥ c_k > 0. *Locality.* H_0 is finite range; if H_k is
exponentially local with exponentially decaying first and second link derivatives ((L-loc2)-type bounds) and H_k ≥ c on a
neighbourhood, then H_k^{-1} is (Combes-Thomas, MS (ii)), hence so is Γ_{k+1}^{-1} = κ − κ²QH_k^{-1}Q^† (Q finite range, analytic in
the links), with ∂Γ_{k+1}^{-1} = −κ²[(∂Q)H_k^{-1}Q^† + QH_k^{-1}(∂Q^†) − QH_k^{-1}(∂H_k)H_k^{-1}Q^†] and the analogous second derivatives;
so H_{k+1} has the same bounds. *Gap at U_f.* The IMS argument of Lemma N-f (iii), whose inputs are exactly such kernel and
first-derivative bounds and the gap at U = 1, gives H_k(U_f) ≥ c_k/2 for |f| ≤ ε_k. With MS (ii)-(iii) each Φ_k is C² in f near
0; independently, Φ_k = G_S,k+1 − G_S,k on 0 < |f| < min(ε'_k, ε'_{k+1}), a difference of two C² functions (S-red (i)).
(c) φ_k := [f²]Φ_k = c^S_{k+1} − c^S_k by (a). Level-k units: the S4' paths of Q_j, j ≥ k, run between level-k centres
(coordinates in L^kZ), so at constant field their phases are e^{iF·(integers)} with F = L^{2k}f (Landau gauge), and the
level-unit Q_k is one fixed function Q(F). With Γ̃_k := L^{2k}Γ_k: Γ̃_{k+1} = L^{2(k+1)}(Q_kΓ_kQ_k^† + κ_{k+1}^{-1}) =
L²Q(F_k)Γ̃_kQ(F_k)^† + s^{-1}1 (κ_{k+1}^{-1}L^{2(k+1)} = s^{-1}), and L^{-2k}H_k = Γ̃_k^{-1} + sL²Q^†Q, so φ_k = [F²]τ_k log(Γ̃_k(F)^{-1} +
sL²Q(F)^†Q(F)) (per level-k site; the f² coefficient per fine site is L^{-4k}·L^{4k} times the F² coefficient per level site).
(d) S-red (iii): ρ_n = c^S_n − 2c_g n log L = Σ_{k<n}(φ_k − 2c_g log L); S-red (iv) gives the equivalence. ∎
*Reading.* (1) The proxy's level-n coefficient is a sum of n-independent step coefficients, each the F² coefficient of a
GAPPED level-k density (no IR problem in any single step). (V-IR-S) is the statement that ~~φ_k − 2c_g log L is summable~~
**[RFL9-fix S9-6: Σ_{k<n}(φ_k − 2c_g log L) has bounded partial sums ((S2) (d)); summability is (S4)]**.
(2) Γ̃_k is the level-k block-spin covariance with noise; its recursion is k-independent in level units, so the steps can
only differ through the initial condition Γ̃_0 = Δ^{-1} (the fine lattice) as seen through k block steps.

## 67. Lemma S-fix (the level-unit two-point fixed point at U = 1): PROVEN-HERE

Statement: §64 (S3).
*Proof.* At U = 1 (fibre notation of §65 with ℓ := L^k): γ_k(K) = L^{2k}[ℓ^{-4}Σ_m D(k_m)²/λ(k_m) + Σ_{j=1}^kκ_j^{-1}L^{-4(k−j)}] =
ℓ^{-2}Σ_mΠ_μD_1(k_{m,μ})²/λ(k_m) + s^{-1}Σ_{j=1}^kL^{-2(k−j)}. The second sum is s^{-1}(1 − L^{-2k})/(1 − L^{-2}). In the first, put
x_μ := K_μ + 2πm_μ with representatives |x_μ| ≤ πℓ; then D_1(k_{m,μ}) = sin(ℓk/2)/(ℓ sin(k/2)) = ±sin(K_μ/2)/(ℓ sin(x_μ/2ℓ)) and
λ(k_m) = Σ_μ4sin²(x_μ/2ℓ), so the m-th term equals t_m^{(ℓ)} := Π_μ[sin(K_μ/2)/s_ℓ(x_μ)]²/Σ_μ(2s_ℓ(x_μ))², s_ℓ(x) := ℓ sin(x/2ℓ).
For |x| ≤ πℓ: |x|/π ≤ |s_ℓ(x)| ≤ |x|/2 and |s_ℓ(x)/(x/2) − 1| ≤ x²/(24ℓ²). Hence t_m^{(ℓ)} → t_m^{(∞)} := Π_μ[sin(K_μ/2)/(x_μ/2)]²/|x|²,
with |t_m^{(ℓ)} − t_m^{(∞)}| ≤ C(max_μx_μ²/ℓ²)t̄_m ≤ Cℓ^{-2}Π_μmin(1, 4π²/x_μ²) (t̄_m a common dominator of both terms, using
max_μx_μ² ≤ |x|²), uniformly in K; the terms of γ_* with some |x_μ| > πℓ sum to O(ℓ^{-3}) (each decays as x_μ^{-4}). Since
Σ_{m∈Z⁴}Π_μmin(1, 4π²/x_μ²) < ∞ uniformly in K, |γ_k − γ_*| ≤ CL^{-2k} uniformly on the level Brillouin zone (the m = 0 term,
of size |K|^{-2}, has relative error O(|K|²ℓ^{-2}), hence absolute error O(ℓ^{-2})). Each term is analytic in K on a
neighbourhood of the closed zone except the m = 0 term at K = 0, and |K̂|²t_0^{(ℓ)} is analytic there; **[S10-corr (session-10 finding, not a reviewer fix): "|K̂|²t_0^{(ℓ)} is analytic there" is FALSE as written:
|K̂|²t_0^{(ℓ)} = Π_μ[sin(K_μ/2)/s_ℓ(K_μ)]²·Σ_μ4sin²(K_μ/2)/λ̃_ℓ(K), λ̃_ℓ(K) := Σ_μ(2s_ℓ(K_μ))², and the last ratio equals
1 − (1 − ℓ^{-2})Σ_μK_μ⁴/(12|K|²) + O(K⁴), which is C^{1,1} but not C² at K = 0 (the same holds for |K̂|²t_0^{(∞)}). What is
true and suffices: λ̃_ℓ(K)t_0^{(ℓ)} = Π_μ[sin(K_μ/2)/s_ℓ(K_μ)]² is analytic near K = 0. The statement (S3) claims derivative
convergence only away from K = 0, where the argument below is unaffected; the uniform (C⁰) statement is unaffected.]** the same dominated
bounds hold for the K-derivatives of order ≤ 2 of |K̂|²t_m^{(ℓ)} (each derivative of s_ℓ(x) differs from that of x/2 by a relative
O(x²/ℓ²)), which gives the C² statement at rate CL^{-2k}. *Bounds on L^{-2k}H_k(1).* For k ≥ 1, γ_k ≥ s^{-1} so γ_k^{-1} ≤ s, and
L^{-2k}H_k(1) = Γ̃_k^{-1} + sL²Q^†Q ≤ s + sL²||Q||² (k = 0: Δ ≤ 16); |γ_k^{-1} − γ_*^{-1}| ≤ |γ_k − γ_*|s² ≤ Cs²L^{-2k}, so the fibre
matrices of L^{-2k}H_k(1) converge uniformly to those of H̃_* := Γ̃_*^{-1} + sL²Q^†Q; H̃_* is fibrewise positive definite (the
argument of §66 (b): γ_*^{-1} vanishes only at K = 0, on constants, and Q maps constants to constants) and continuous on the
compact zone, so H̃_* ≥ c_* > 0; hence L^{-2k}H_k(1) ≥ c_*/2 for k ≥ k_0, and each of the finitely many k < k_0 is gapped by
§66 (b). ∎
*Reading.* The two-point data of the steps converge at rate L^{-2k}; the IR pole of γ_k is exactly |K|^{-2} at every k (D(0) =
1: the block average preserves the charge normalisation), which is why the step operators are uniformly gapped.

## 68. Target (S4): what is proved and what is OPEN

Statement: §64 (S4). **Status: OPEN** (analytic); f12 (§70) supports it at n ≤ 4 with θ ≈ L^{-2}.
*Proved here (reduction).* By §66, (S4) ⟺ the summability of φ_k − 2c_g log L, and by §65 each φ_k is the p² coefficient of a
U = 1 one-loop kernel built from the uniformly gapped step operators L^{-2k}H_k(1) (§67) and from the first- and
second-order plane-wave vertices of Γ̃_k^{-1} and Q in level units. For the plane wave U_{x,1} = e^{iε cos(px_2 + ϑ)} the
level-unit S4' averages Q_j (j ≥ k) see EXACTLY the level-unit plane wave of amplitude L^kε and momentum P := L^kp (the
direction-1 legs run at fixed x_2, so no Riemann-sum error enters). Hence (S4) follows from two statements:
- **(VC) (vertex convergence, OPEN):** the level-unit vertex data of Γ̃_k at U = 1 (symbol γ_k, and the plane-wave vertices
  γ_k^{(1)}(K; P), γ_k^{(2)}(K; P)), multiplied by the IR weights that make them bounded (|K̂|², |K̂||K̂ + P̂|·…), converge at a
  geometric rate θ^k, uniformly on a complex neighbourhood of the real (K, P) region. Given (VC), φ_k → φ_* with
  |φ_k − φ_*| ≤ C'θ^k, because the step kernel is an analytic function of these data on the uniformly gapped region (§67) and
  the P² coefficient is a Cauchy integral on a k-uniform disc.
- ~~**(IRR*) (the IR identification, OPEN):** φ_* = 2c_g log L. …~~ **[RFL9-fix S9-1: (IRR*) is REDUNDANT and RETIRED.** With
  x_n(P) := [ε̃²]τ_n log Γ̃_n^{-1}/(P²/2) (finite for P > 0) and x_0(p) := [ε²]τ log Δ_U/(p²/2), S-red (ii) along the plane wave
  gives x_n(ℓp) = x_0(p) − h_n(p)/(p²/2) exactly; with the fine IR expansion x_0(p) = 2c_g log(1/p) + a_0 + o(1) (Lemma
  FINE-IR, §74) and S-red (i), a_n := lim_{P→0}[x_n(P) − 2c_g log(1/P)] exists for every n and **ρ_n = a_0 − a_n,
  φ_k − 2c_g log L = a_k − a_{k+1}** exactly (Proposition IR-id, §75). The log coefficient 2c_g is forced at every level;
  no universality theorem for Γ̃_*^{-1} is needed. (V-IR-S) ⟺ **(UIR): sup_n|a_n| < ∞**; the rate form is a_n → a_* at θ^n.
  Numerically a_n − a_0 = −ρ_n → +1.76805e-3 (f12).]**
~~The proof of (VC) is an RG contraction for the affine recursion … not written here.~~ **[RFL9-fix S9-2: (VC) is not an
RG-contraction problem: S-tel (a) has solved the recursion (Γ̃_k = L^{2k}(M_UΔ_U^{-1}M_U^† + 𝒞_k(U)) in closed form), so the U = 1
plane-wave vertices of Γ̃_k are the explicit separable alias sums of §65 (b) at level k, and (VC) is S-fix's dominated
convergence applied to them. (VC) is to be stated on the vertex data of Γ̃_k^{-1} (equivalently, as done in §76, on γ_k, b_k,
w_k with the IR poles factored), which is regular at K = 0. The three real tasks: (i) alias summability with the
first-order form factors G_κ (one power of x_1 slower than D_1); (ii) the midpoint ℓ^{-2} rate; (iii) uniformity in k of
the IR expansion of x_k(P). All three are done in §76 (Theorem UIR-S).]**

## 69. Lemma V-2pt (vector root sector at U = 1) and the two questions (S5) (d), (S6)

Statement: §64 (S5), (S6).
*Proof of (S5) (a)-(c), given (L-loc2).* (a) The torus action block-diagonalises the total into Cartan and root blocks; the
root-α block, as a function of the Cartan background, is invariant under Cartan gauge transformations and is a gapped
covariant density at U_f (COV-GI-∞, Lemma N-f) whose cell density has an exponentially decaying Hessian at U = 1 (§51, "the
hypothesis in MS (iv)", given (L-loc2)). Lemma MS (iv) with F-id-exp then gives 2c^tot_{n,α} = H_0^α(𝓛Φ, 𝓛Φ)/(Vφ²), and the
plane-wave argument of §65 (c), run with the Cartan plane wave H_1 ε cos(px_2 + ϑ) on the 1-links, gives 2c^tot_{n,α} =
lim_{p→0}2h^α(p)/(2sin²(p/2)) with h^α the ε² coefficient of the root-α block: the (12, 12) p² coefficient of its U = 1 Hessian
kernel. c^⊥_{n,α} = c^tot_{n,α} + 2c_gq_α²log ℓ is GH-log (c) (unconditional since §58). (b) K_F + μ and Δ_0 + μ are finite range,
covariant, ≥ μ − C|f|^{2/3} (Lemma VIR-eq (1)), with exponentially decaying resolvent Hessians at U = 1; MS (iv) and F-id-exp
apply unconditionally. (c) Subtracting, ρ^V_{n,α} = lim_{p→0}[h^α(p) − h^α_𝔪(p)]/(2sin²(p/2)) + 2c_gq_α²log ℓ, h^α_𝔪 the ε² coefficient
of the root block of log det_C(K_F + ℓ^{-2}) − log det_C(Δ_0 + ℓ^{-2}). At U = 1 every propagator in these one-loop kernels is the
inverse of an operator ≥ c > 0: Ã(1) = d^*d + dE'd^* + M^T𝒞_n^{-1}M ≥ c_n (N-f (ii)), Δ'(1) = E'Δ_0E' > 0 on Λ' (a function vanishing at
the level sites with ⟨ρ, Δ_0ρ⟩ = 0 is constant, hence 0; fibrewise positivity and compactness give a gap **[RFL9-fix S9-5: a
gap c_n ≍ ℓ^{-4} in fine units (Rayleigh quotient of ρ = (g(0) − g)/g(0), g the cell Green's function: the 4D capacity of a
point), i.e. ≍ ℓ^{-2} → 0 in level units; Ã(1) ≥ c_n is likewise not shown level-uniform; these constants are n-dependent]**),
𝒞_n(1) ≥ κ^{-1}π_+^{-1},
K_F(1) + ℓ^{-2} ≥ ℓ^{-2}, Δ_0(1) + ℓ^{-2} ≥ ℓ^{-2}; no negative mode enters. Given (L-loc2) and §58, [f²]_lim G_⊥,n,α = {c^⊥_{n,α}}, so
(Q1)(d) reads |ρ^V_{n,α}| ≤ Aq_α² for all n, α: the stated equivalence. ∎
*(S5) (d): ANSWERED — K̃(1) has zero modes, exactly one per level momentum (per colour component), so ~~the Woodbury reference
must be K_F(1) + μ (or K̃(1) + μ) with μ carried explicitly~~* **[RFL9-fix S9-4: so the plain Woodbury about K̃ is
unavailable; the bordered Woodbury about the MASSLESS K_F(1) is exact (D^*K_F^{-1}D = 1 at U = 1; REVIEW_FLOW_S9 §6 (1);
Lemma V-bord, §77). The "must carry a mass" remark is WITHDRAWN.]** Proof. Per colour component at U = 1, K̃(1) = d^*d + dE'd^* with both
terms ≥ 0, so K̃(1)A = 0 ⟺ dA = 0 and E'd^*A = 0. On the fibre of a level momentum K ≠ 0 every alias k_m ≠ 0, so dA = 0 gives A = dλ
(Fourier Poincaré lemma: λ̂ = Â_μ/(e^{ik_μ} − 1) for any μ with k_μ ≠ 0). Then E'Δλ = 0, i.e. ν := Δλ is supported on the level-n
sites, and conversely every ν supported on the level sites (one dimension on the fibre) gives λ = Δ^{-1}ν (Δ invertible on the
fibre, K ≠ 0) and dλ ≠ 0 in the kernel. So ker K̃(1) on the fibre of K is span{dΔ^{-1}ν_K}, ν_K the level-site plane wave: these
are the residual gauge directions at the level sites, which E' does not fix and the IR term M^T𝒞_n^{-1}M lifts (Ã(1) ≥ c_n). ∎
*(S6): ANSWERED NO in the form (S2) (a)* **[RFL9-fix S9-4: narrowed — NO for the decomposition starting from Γ_0^{-1} = K̃_n
(with E'_n inside); not structural: E'_n is removable by the bordered Woodbury about K_F(1) and the Jacobi decimation of
the ghost, which give n-independent steps (REVIEW_FLOW_S9 §6; Lemma V-bord, Lemma V-Jac, Proposition V-tel, §77-§78); the
OPEN crux of that route is the off-shell defect H(U)D_U ≠ 0 along plane waves (§79)]**. The scalar decomposition starts from the n-independent Γ_0^{-1} = Δ. The vector analogue
would start from Γ_0^{-1} = K̃_n = H + D E'_n D^* (singular at U = 1 by (S5) (d), and depending on n through E'_n, the projector
that removes the level-n sites), and the total also carries −log det Δ'_n (Δ'_n = E'_nΔ_0E'_n); both depend on n, so the step
densities of that decomposition are not n-independent. The terms that break it: E'_n (in D E'_nD^* and in Δ'_n). [Route, not
claimed: Lemma FP-exact (§52) makes the total an exact FP representation of a gauge-invariant integral; a gauge fixing that
references every level (E'_k at step k) would give a decomposition of the (S2) form if the total is independent of the
choice of fixing within such a class. OPEN.]

## 70. Session-9 check f12 (ADDED AFTER the run; checks/f12_criteria.md, f12_proxy_2pt.py, f12_out.txt, f12_time.txt)
Criteria written 07:45:18 UTC before any f12 script (stat in FLOW_LOG); the script was not changed after its smoke test
(byte-identical copy). Official run: one NUMERIC LOCK acquisition, 07:54:08-07:54:12 UTC, nice 10, 1 thread, load 4.86,
memory free 46%; 3.8 s, peak RSS 375 MB. (A first official attempt at 07:51:00 started at 1-min load 8.53, above the
brief's load < 8; it is VOID: its output was set aside in the scratchpad and not used; a diff shows it identical to the
valid re-run's output apart from timing lines.) **14/14 verdict lines PASS.**
- **Implementation.** I1: the momentum-space formula of §65 against a direct 4D torus (6, 12, 6, 3) with all 24 S4' orders
  and an ε-fit of the exact log det: h = −7.828148246e-5 vs −7.828147578e-5, relative 8.5e-8 (threshold 1e-7). Reported:
  the n = 2 vertex form factors u, m_2 against the real-space block kernel (24 orders): 2.3e-11, 2.1e-9 relative. I2 (Ward):
  the unsubtracted p = 0 value is 1e-15 (n = 1), 1e-16 (n = 2), against thresholds 4e-10, 2e-10. I3: K grids 16⁴ vs 20⁴ agree to
  ≤ 2.9e-12 and the proper-time step halving changes ≤ 6.9e-12, n = 1..4. I4: p-fit stability ≤ 8.4e-13.
- **P-a (S9-F1 does not occur): c^S_1 = 7.1234243515e-4 (f11: 7.123425e-4, |diff| 6.5e-11), c^S_2 = 2.8854888648e-3 (f11:
  2.885494e-3, |diff| 5.1e-9).** The U = 1 two-point form reproduces f11's constant-field magnetic-Bloch computation.
- **c^S_3 = 5.1907041547e-3, c^S_4 = 7.5082020587e-3; ρ_1..ρ_4 = −1.6066720951e-3, −1.7525401957e-3, −1.7663394360e-3,
  −1.7678560623e-3. P-b (S9-F2 does not occur): ρ_3 − ρ_2 = −1.3799e-5 (threshold 4.9e-5).**
- **Increments (S9-F3 does not occur): ρ_{n+1} − ρ_n = −1.458681e-4, −1.379924e-5, −1.516626e-6; ratios 0.0946, 0.1099**
  (L^{-2} = 0.1111); φ_k − 2c_g log 3 = −1.6067e-3, −1.4587e-4, −1.3799e-5, −1.5166e-6 (k = 0..3).
- Scratchpad extension (not under the f12 criteria, reported only; flow9/ext56.py importing the f12 functions unchanged,
  one lock acquisition, 15 s, 598 MB): ρ_5 = −1.7680245243e-3, ρ_6 = −1.7680439484e-3; increments −1.6846e-7, −1.9424e-8
  (ratios 0.111, 0.115). **[RFL9-fix S9-3: ρ_6 and the ratio 0.115 are NOT converged: halving the proper-time step h_u changes c^S_6 by
  6.0e-10 > f12's I3 threshold 1e-10, and the 5→6 ratio spans 0.112-0.116 over (N_K, h_u) (REVIEW_FLOW_S9 §4.3); n = 5 is
  at the edge (9.7e-11). The 4→5 ratio is robust: 0.1111 (0.11103-0.11109). I1's 8.5e-8 is ε-fit truncation, not a formula
  error: a degree-5 fit on ε ∈ [0.01, 0.08] gives 9.2e-9, and the momentum side is stable to 4e-15 under h_u → h_u/3.]**
- **[RFL9-fix S9-7: provenance disclosures.** (1) The explicit vertex formulas of §65 (b) (u, m_2, c_2) were written at
  07:57-08:00 UTC, AFTER f12's script (07:49) and run (07:54); §64 (S1) (b) pre-fixed only their structure (traces over the
  alias fibre, diagonal plus rank one). For u and m_2 the written "derivation" is partly a description of the
  implementation; their independent support is f12's n = 2 real-space form-factor check (2.3e-11, 2.1e-9) and P-a against
  f11 (a different method). (2) c_2 vanishes at n = 1, so I1 does not test it, nor the multi-κ structure; they are covered
  by P-a at n = 2 and by the reviewer's hand derivation of c_2 (REVIEW_FLOW_S9 §2). (3) I2 was implemented as the direct
  unsubtracted h_n(0) test, not as "the fitted constant term in a fit with a free constant" of f12_criteria.md l.18 (a
  stronger and simpler test, but a wording deviation from the criteria).]**
- **Reading.** (1) Lemma S-2pt's F-id link holds in the proxy to 5e-9, and with it f11 is confirmed independently. (2) At
  n ≤ 4 (and n ≤ 5 in the extension **[RFL9-fix S9-3: n = 6 unconverged, see above]**) ρ_n converges geometrically with ratio ≈ L^{-2} = ℓ^{-2}-type approach, the fastest of
  REVIEW_FLOW_S8's three scenarios; ρ_∞ ≈ −1.76805e-3 (geometric tail), so c^S_n − 𝔠^S(ℓ²) → ρ_∞ − ½κ_0 ≈ −2.0758e-3. (3) This
  is evidence for (S4) with θ = L^{-2}, not a proof; (VC) and (IRR*) are OPEN **[RFL9-fix S9-1: (IRR*) retired; see §68]**. (4) The vector ρ^V_n was not attempted.

## 71. Session-9 outcomes against §64 (ADDED AFTER the derivations and the check)
- **Step 1 (fixes): DONE.** S8-1..S8-6 and the tally correction applied in place, tagged [RFL8-fix] (25 tag occurrences).
- **(S1) Lemma S-2pt: PROVEN** (§65; the scalar F-id link at U = 1, explicit fibre formula, D𝒞_n(1) = 0). f12 P-a confirms it.
- **(S2) Proposition S-tel: PROVEN** (§66): c^S_n = Σ_{k<n}φ_k with n-independent, gapped step densities;
  ρ_n = Σ_{k<n}(φ_k − 2c_g log L).
- **(S3) Lemma S-fix: PROVEN** (§67): level-unit two-point data converge at rate L^{-2k}; the steps are uniformly gapped.
- **(S4) (V-IR-S) with a rate: OPEN**, reduced (§68) to (VC) (geometric convergence of the level-unit vertex data, ~~an RG
  contraction for an affine recursion~~ **[RFL9-fix S9-2: explicit alias sums]**) and ~~(IRR*) (the IR log identification at
  the fixed point)~~ **[RFL9-fix S9-1: (IRR*) retired; (V-IR-S) ⟺ (UIR)]**. f12: geometric with
  ratio ≈ L^{-2} at n ≤ 4.
- **(S5) Lemma V-2pt (a)-(c): PROVEN given (L-loc2)** (§69): the vector root sector in two-point form at U = 1, all propagators
  strictly positive, (V-IR) ⟺ sup|ρ^V|/q² < ∞. **(d) ANSWERED:** K̃(1) has exactly one zero mode per level momentum (the
  level-site residual gauge directions dΔ^{-1}ν_K); ~~the reference must carry a mass~~ **[RFL9-fix S9-4: withdrawn; the
  bordered Woodbury about the massless K_F(1) is exact]**.
- **(S6) ANSWERED NO** in the form (S2) (a): E'_n (in D E'_nD^* and Δ'_n) makes the vector step densities n-dependent; a
  level-by-level fixing via FP-exact is a route, OPEN. **[RFL9-fix S9-4: NO only for the decomposition starting from K̃_n; E'_n is removable (bordered
  Woodbury + Jacobi ghost decimation + X_k recursion: n-independent steps, §77-§78); the off-shell defect is the OPEN crux of
  that route (§79)]**
- **Step 3 (f12): DONE**, 14/14; vector ρ^V_n not attempted.

## 72. Tally after session 9 (FLOW.md items; session-9 items unreviewed)
- **PROVEN-HERE: 46 (through session 8, as corrected by REVIEW_FLOW_S8) + 4 (session 9) = 50.** Session 9: Lemma S-2pt;
  Proposition S-tel; Lemma S-fix; Lemma V-2pt (given (L-loc2); including the K̃(1) zero-mode statement (d)). Upstream inputs
  used: Lemma MS (ii)-(iv), Lemma F-id-exp, S-red (i)-(iv), COV-sc proof (1), Lemma N-f (ii)-(iii) (IMS argument), GH-log (c),
  §58, COV-GI-∞, §51's MS (iv) hypothesis check, Lemma VIR-eq (1).
  **[RFL9-fix: scope annotations (REVIEW_FLOW_S9 §7): V-2pt (a)-(c) is counted conditional on (L-loc2), following the
  COV-GI-∞ precedent; its (d) consequence is narrowed by S9-4; S-2pt (b)'s u and m_2 are verified numerically (f12's n = 2
  real-space check), not by an independent derivation; the fine IR expansion of x_0 is a needed standard input (S9-1),
  proved in session 10 as Lemma FINE-IR (§74). Tally 50 as corrected by REVIEW_FLOW_S9.]**
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT (§58, renamed by [RFL8-fix S8-1]).
- **ARGUED, not counted:** (L-loc2).
- **OPEN:** (V-IR) on G_⊥ in the form (Q1)(d), equivalently sup|ρ^V_{n,α}|/q_α² < ∞ (§69) [s-P] (crux); (V-IR-S) via (VC) and
  (IRR*) (§68) [s-P]; a level-by-level fixing for the vector telescoping (§69) [s]; (L-loc2) to be proved [s]; (s1), (s2⊥)
  [s-P] (rate only); the rate of c'(φ) → c'_0 [s]; (COV-GI) at non-critical backgrounds [s]; FI-1 [cross-lane]; HIST's
  restatement of CL^J's Setting [cross-lane].
- **Checks:** f12 (I1, I2 ×2, I3 ×4, I4 ×4, P-a ×2, P-b PASS).

## 73. Session-10 targets and PRE-STATED (session 10) statements (written 2026-10-28 08:45 UTC, the first edit of session 10: before the [RFL9-fix] edits and before any session-10 proof, criteria file or script)

Binding input: REVIEW_FLOW_S9.md (tally 50 with its scope annotations; fixes S9-1..S9-7; the route of its §6; next target
§9). The fixes are applied after this section, in place, tagged **[RFL9-fix]**. Notation of §64-§68 (scalar proxy) and of
§41, §45, §57 (Q1), §69 (vector). Scalar definitions (plane wave U = U^{ε,p,ϑ} of §64; 0 < |p| < π/ℓ; P := ℓp; ε̃ := ℓε):
  x_0(p) := [ε²]τ log Δ_U/(p²/2)  (per fine site; any 0 < |p| < π),
  x_n(P) := [ε̃²]τ_n log Γ̃_n(U)^{-1}/(P²/2),  Γ̃_n(U) := ℓ²(𝒞_n(U) + M_UΔ_U^{-1}M_U^†)  (per level-n site; n ≥ 1).

**PRE-STATED (session 10).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Each hypothesis is named; nothing below uses an ARGUED or OPEN item as if proven. Any later change
of a statement is logged as such.

**(T1) Lemma FINE-IR.** x_0 is even and real-analytic on 0 < |p| < π, and x_0(p) = 2c_g log(1/p) + a_0 + O(p²log(1/p)) as
p → 0 (c_g = 1/(96π²)), with a_0 given by an explicit absolutely convergent integral.
**(T2) Proposition IR-id (REVIEW_FLOW_S9 S9-1, proven).** For n ≥ 1 and 0 < |P| < π, x_n(P) is finite and even, x_n(P) =
(2/P²)∫dK/(2π)⁴F_n(K, P) with F_n ∈ L¹ an explicit fibre integrand built from the §65 (b) form factors in level units, and
x_n(ℓp) = x_0(p) − h_n(p)/(p²/2) exactly. Hence a_n := lim_{P→0}[x_n(P) − 2c_g log(1/P)] exists for every n, ρ_n = a_0 − a_n,
and φ_k − 2c_g log L = a_k − a_{k+1}.
**(T3) Theorem UIR-S.** There are P_0 > 0 and C < ∞ with |x_n(P) − x_m(P)| ≤ C L^{-2min(n,m)} for all n, m ≥ 1 and
0 < |P| ≤ P_0. Consequently a_* := lim_n a_n exists, |a_n − a_*| ≤ CL^{-2n}, sup_n|ρ_n| < ∞ (that is (V-IR-S)), and (S4) holds
with θ = L^{-2}: |φ_k − 2c_g log L| ≤ 2CL^{-2k}. [Route: (VC) for the level-unit vertex data (γ_n, b_n, w_n) at U = 1 by
S-fix's dominated alias sums applied to the §65 (b) form factors; the Ward identity at P = 0; inversion parity. Any part
not proved is reported OPEN, with what it needs.]
**(T4) Lemma V-bord (bordered Woodbury, exact for every U at which K_F(U) := H(U) + D_UD_U^* is invertible; no criticality,
no mass).** Let ι be the isometric injection of the 0-forms on the level-n sites into Λ (so P_n := 1 − E' = ιι^*), g_U :=
ι^*Δ_U^{-1}ι, X_U := 𝒞_n(U) + M_UK_F^{-1}M_U^T, b_U := M_UK_F^{-1}D_Uι, δ_U := 1 − ι^*D_U^*K_F^{-1}D_Uι. Then
  det Ã(U) = det K_F·det 𝒞_n^{-1}·det X_U·det(δ_U + b_U^*X_U^{-1}b_U),   det Δ'(U) = det Δ_U·det g_U,
hence total_n(U) := ½log det Ã − log det Δ' + ½log det 𝒞_n = [½log det K_F − log det Δ_U] + ½log det X_U +
½log det(δ_U + b_U^*X_U^{-1}b_U) − log det g_U. (b) With E_U := H(U)D_U: δ_U = ι^*D_U^*K_F^{-1}E_UΔ_U^{-1}ι, and b_U =
D_ℓ^{𝔪(U)}g_U − M_UK_F^{-1}E_UΔ_U^{-1}ι (using M_UD_U = D_ℓ^{𝔪(U)}∘ι^*, the gauge covariance of 𝔪_n). At critical U (E_U = 0;
in particular U = 1, fibrewise at K ≠ 0): δ = 0, b = D_ℓg, and total_n = [½log det K_F − log det Δ_U] + ½log det X_U +
½log det(D_ℓ^*X_U^{-1}D_ℓ) = [½log det K_F − log det Δ_U] + ½log det_⊥X_U + ½log det(D_ℓ^*D_ℓ), det_⊥ the determinant of the
compression of X_U to (Ran D_ℓ)^⊥.
**(T5) Lemma V-Jac (ghost decimation).** For every U (Δ_U invertible) and every chain Λ = Λ_0 ⊃ Λ_1 ⊃ … ⊃ Λ_n of site sets, with
Δ^{(k)} := ((Δ_U^{-1})|_{Λ_k})^{-1}: log det(Δ_U|_{Λ_0∖Λ_n}) = Σ_{k<n}log det(Δ^{(k)}|_{Λ_k∖Λ_{k+1}}) exactly; the k-th term depends
only on Λ_0, …, Λ_{k+1}. For Λ_k the level-k sites, the left side is log det Δ'_n.
**(T6) Proposition V-tel.** For every U_0 near 1, with M = A_0 = T_{n−1}⋯T_0 (chain rule) and COV-str (ii): X_0 := K_F^{-1},
X_{k+1} := T_kX_kT_k^T + κ^{-1}Π_{k+1}^{-1} gives X_n = X_{U_0}; with H^V_k := X_k^{-1} + κT_k^TΠ_{k+1}T_k,
½log det K_F + ½log det X_n = ½Σ_{k<n}Φ^V_k, Φ^V_k := log det H^V_k − log det(κΠ_{k+1}) (n-independent steps). Hence, exactly,
total_n = −log det Δ_U + ½Σ_{k<n}Φ^V_k + ½log det 𝒢_n, 𝒢_n := g^{-1}(δ + b^*X_n^{-1}b)g^{-1} (at critical U: 𝒢_n = D_ℓ^*X_n^{-1}D_ℓ).
**(T7) The off-shell defect (the crux).** (a) For every U, E_U = H(U)D_U is linear in the gradient ∇S_W(U) (an explicit
formula), so E_U = 0 at critical U. Along the Cartan plane wave H_1ε cos(px_2 + ϑ) on the 1-links, E_U = εE_1 + O(ε³), and in
the root sector α, E_1 is (up to a fixed unit factor) q_α times multiplication by the linearised current J_1 = d^*da =
(2 − 2cos p)·a on the 1-links. **[RFL10-fix S10-1: "E_U = εE_1 + O(ε³)" is FALSE; the correct expansion is E_U = εp̂²Ê_1 +
ε²p̂²Ê_2 + O(ε³) (the O(ε) term of Ad(U_b^{-1}) = 1 − εa_b ad H_1 + … on the 1-links), see §79 (a); the pre-statement is left
as written and the correction is logged.]** (b) Hence the defect enters the ε² coefficient of total_n only through terms linear in E_1,
and its contribution to 2c^tot_{n,α} is 𝔡_{n,α} := lim_{p→0}(2 − 2cos p)𝔮_{n,α}(p)/(2sin²(p/2)) for an explicit one-loop
kernel 𝔮_{n,α} (if the limit exists). (c) Question: is 𝔡_{n,α} zero, O(ℓ^{-2}), or n-uniformly bounded? A proof of one, or the
exact wall, is an outcome.
**(T8) Target (vector (UIR)).** Given (L-loc2) and (T4)-(T7): (V-IR) in the form (Q1)(d) is reduced to named level-unit
statements for the X-part and the 𝒢-part (the vector analogue of (T3)) and to (T7) (c); what is proved and what is OPEN is
reported. Theorem UNIV for SU(N) is said to rest only on (L-loc2) ONLY if every other link is proved here.

**Check f13** (criteria file first, its stat into FLOW_LOG before any f13 script; jobs < 20 min, < 1 GB, memory free ≥ 35%,
load < 8 at start): (a) FINE-IR: x_0(q) by a two-dimensional proper-time quadrature (Bessel form), q ∈ [10^{-3}, 0.8]:
**predictions:** the log slope −dx_0/d log q equals 2c_g to ≤ 10^{-3} relative on q ∈ [10^{-3}, 10^{-2}]; the symmetrised form
agrees with the unsymmetrised one at q = 0.3, 0.6 to ≤ 10^{-9} relative; a_0 reported. (b) (VC)/(UIR): Y_n(P) := x_n(P) −
2c_g log(1/P), evaluated exactly as x_0(P/ℓ) − 2ℓ²h_n(P/ℓ)/P² − 2c_g log(1/P) (f12's h_n functions unchanged), n = 1..5, on a
P-grid in [0.05, 2.4]: **prediction:** sup_P|Y_n − Y_{n−1}| shrinks geometrically, each ratio for n = 3, 4, 5 ≤ 0.2 (the proof
predicts ≈ L^{-2}); quadrature step control (K grid, proper-time step) changes Y_n by ≤ 10^{-9}. (c) vector, finite-dimensional
(SU(2) root sector at Cartan backgrounds, torus 6 × 6 × 3 × 3, ℓ = 3, n = 1, straight-path decimation block map, 𝒞 = 1):
the identities of (T4) (a) to ≤ 10^{-9} relative at a flat twisted background and at a Cartan plane-wave background;
M D_U = D_ℓ∘ι^* to ≤ 10^{-12}; at the flat background δ and b − D_ℓg ≤ 10^{-7} (finite-difference Hessian); E_U/ε at p = 4π/6
against p = 2π/6 equal to the p̂² ratio 3 within 10^{-3}; (T5) on a two-step chain to ≤ 10^{-10}.

**Failure modes (each a valid outcome).** (S10-F1) the log slope of x_0 is not 2c_g; (S10-F2) some ratio > 0.2, or the
n-differences are not uniform in P (growing at small P); (S10-F3) a (T4) identity fails; (S10-F4) E_U is not O(εp̂²)
(the p̂² ratio fails).

---
# Session-10 proofs (written after §73 and the [RFL9-fix] edits)

## 74. Lemma FINE-IR (the fine scalar polarisation): PROVEN-HERE

Statement: §73 (T1).
*Proof.* (1) *Fibre formula.* In the background U_{x,1} = e^{ia(x_2)}, a = ε cos(px_2 + ϑ), Δ_U has the plane-wave vertices of
§65 (b) (first order Σ(k) = 2 sin k_1 between momenta k and k ± pe_2; ϑ-free second order ¼W, W = 2cos k_1). As in §65 (b)
(the ±2p parts vanish for 0 < |p| < π), [ε²]τ log Δ_U = ¼∫dk/(2π)⁴[W/λ − Σ²/(λλ_p)], λ_p := λ(k + pe_2). The integrand is in L¹:
near k = 0, W/λ ~ 2|k|^{-2}; near k = −pe_2, Σ² ~ k_1² ≤ |k + pe_2|². On the antiperiodic torus of side N with p ∈ 2πZ/N the
exact ε² density is the Riemann sum of this integrand on the half-shifted grid, which stays ≥ π/N away from both
singular points; the singular cells contribute O(N^{-2}) and the rest converges (midpoint rule, |∂²f| ≲ |k|^{-4}, error
O(N^{-2}log N)). So x_0(p) is this integral divided by p²/2, the infinite-volume density.
(2) *Ward rewrite.* ∂_{k_1}(Σ/λ) = W/λ − Σ(∂_1λ)/λ² = W/λ − Σ²/λ² (∂_1λ = 2 sin k_1). Σ/λ is periodic with |Σ/λ| ≲ |k|^{-1} and
∂_1(Σ/λ) ∈ L¹, so ∫∂_1(Σ/λ) = 0 (excise a ball B_r: the boundary term is O(r^{-1}r³) → 0). Hence ∫[W/λ − Σ²/(λλ_p)] =
∫Σ²(λ_p − λ)/(λ²λ_p) (each piece in L¹ at p ≠ 0). The measure-preserving map k ↦ −k − pe_2 exchanges λ and λ_p and fixes Σ², so the
integral equals ½∫Σ²(λ_p − λ)[1/(λ²λ_p) − 1/(λλ_p²)] = ½∫Σ²(λ_p − λ)²/(λ²λ_p²). With λ_p − λ = 4sin(k_2 + p/2)sin(p/2) and the
shift k_2 → k_2 − p/2:
  x_0(p) = (16sin²(p/2)/p²)·J(p),  J(p) := ∫dk/(2π)⁴ sin²k_1 sin²k_2/(λ_-²λ_+²) ≥ 0,  λ_± := λ(k ± (p/2)e_2).
x_0 is even (k_2 → −k_2). Real-analyticity on 0 < |p| < π: by 1/(λ_-²λ_+²) = ∫∫st e^{−sλ_- −tλ_+}ds dt and the factorisation over
directions, J(p) = ∫∫ds dt st e^{−8τ}·[I_1(2τ)/(2τ)]·½[I_0(2R) − cos2ψ I_2(2R)]·I_0(2τ)² (τ = s + t, R² = s² + t² + 2st cos p,
cos 2ψ = ((s² + t²)cos p + 2st)/R²); the integrand is analytic in p (I_0(2R) and I_2(2R)/R² are entire in R²) and, since
e^{−8τ}I_0(2τ)²I_ν(2τ)I_ν'(2R) ≲ τ^{-2}R^{-1/2}e^{−2(τ − R)} with τ − R = 2st(1 − cos p)/(τ + R), Re(1 − cos p) > 0 near any real
p_0 ≠ 0 gives locally uniform convergence for complex p near p_0.
(3) *Asymptotics.* Let B := {|k| ≤ 1}, f(k, p) := sin²k_1 sin²k_2/(λ_-λ_+)², c(k, p) := k_1²k_2²/(|k_-|²|k_+|²)², k_± := k ± (p/2)e_2.
(i) On T⁴∖B, λ_± ≥ c_0 > 0 for |p| ≤ 1, f is smooth and even in p: ∫_{T⁴∖B}f = ∫_{T⁴∖B}f(·, 0) + O(p²).
(ii) On B: |sin²y − y²| ≤ y⁴/3 and |λ(q)^{-2} − |q|^{-4}| ≤ C|q|^{-2} give |f − c| ≤ C[(k_1⁴k_2² + k_1²k_2⁴)/(|k_-|⁴|k_+|⁴) +
k_1²k_2²(|k_-|^{-2}|k_+|^{-4} + |k_-|^{-4}|k_+|^{-2})]. For |k| ≥ 2|p|: |k_±| ≥ |k|/2, so |f − c| ≤ C|k|^{-2}, and the same Leibniz
count gives |∂_p²(f − c)| ≤ C|k|^{-4}. For |k| ≤ 2|p|: k_1² ≤ |k_-||k_+| and k_2² ≤ 4p², so each term is bounded by
Cp^a|k_-|^{-b}|k_+|^{-b'} with b, b' ≤ 3 and a − b − b' = −2, whose integral over |k| ≤ 2|p| is O(p²) (scale k = pq; the singular
points q = ±e_2/2 are separated and each singularity is integrable in 4D). Evenness in p and the Taylor bound give
∫_{2|p|≤|k|≤1}(f − c)(k, p) = ∫_{2|p|≤|k|≤1}(f − c)(k, 0) + O(p²log(1/p)) = ∫_B(f − c)(k, 0) + O(p²log(1/p)).
(iii) ∫_Bc = (2π)^{-4}∫_{|q|≤1/p}q_1²q_2²/(|q_-|²|q_+|²)²d⁴q (k = pq, q_± = q ± e_2/2). Since |q_-|²|q_+|² = (|q|² + ¼)² − q_2²,
the integrand is q_1²q_2²|q|^{-8} + O(|q|^{-6}) for |q| ≥ 1 (no odd term), and the angular mean of n_1²n_2² over S³ is 1/24
(|S³| = 2π²), so ∫_Bc = (2π²/24)(2π)^{-4}log(1/p) + C_3 + O(p²) = log(1/p)/(192π²) + C_3 + O(p²).
With 16sin²(p/2)/p² = 4 + O(p²): x_0(p) = (4/(192π²))log(1/p) + a_0 + O(p²log(1/p)), 4/(192π²) = 1/(48π²) = 2c_g, and
  a_0 = 4[∫_{T⁴∖B}f(·, 0) + ∫_B(f(·, 0) − c(·, 0)) + C_3],  f(k, 0) = sin²k_1sin²k_2/λ⁴, c(k, 0) = k_1²k_2²/|k|⁸,
  C_3 := lim_{R→∞}[(2π)^{-4}∫_{|q|≤R}q_1²q_2²/(|q_-|²|q_+|²)²d⁴q − log R/(192π²)],
each piece absolutely convergent. ∎
*Reading.* The log coefficient of the massless fine scalar polarisation is 2c_g exactly, and the finite part a_0 exists;
this is the "standard input" REVIEW_FLOW_S9 asked for (S9-1), proven here with no import. f13 Part A: the log slope on
[10^{-3}, 10^{-2}] is 2c_g to 5.3e-6, the two forms agree to 2e-11, a_0 = 2.512968892e-3 (fit-window stable to 6e-13).

## 75. Proposition IR-id (the exact identity ρ_n = a_0 − a_n): PROVEN-HERE

Statement: §73 (T2).
*Level-unit dictionary* (U = 1, level-n fibre of the level momentum K, aliases x := K + 2πm with representatives |x_μ| ≤ πℓ,
fine momenta k_m = x/ℓ; primes: the fibre of K' := K + P, i.e. x' = x + Pe_2): d_m := D(k_m) = Π_μD_1(x_μ/ℓ) = Π_μ sin(x_μ/2)/s_ℓ(x_μ);
λ̃_m := ℓ²λ(k_m) = Σ_μ(2s_ℓ(x_μ))²; σ_m := ℓΣ(k_m) = 2ℓ sin(x_1/ℓ); ŵ_m := W(k_m) = 2cos(x_1/ℓ); ũ_m := ℓ^{-1}u(k_m; p), ũ^-_m :=
ℓ^{-1}u(k_m + pe_2; −p), ũ^{(−)}_m := ℓ^{-1}u(k_m − pe_2; p); m̃_m := ℓ^{-2}m_2(k_m); c_n := ℓ²C_n(0); c_2 as in §65 (b) (u, m_2, c_2 the
§65 (b) form factors). Then the symbol of Γ̃_n(1) is γ_n(K) = Σ_md_m²/λ̃_m + c_n, and, writing Γ̃_n(U) = γ_n + ε̃Γ̃_1 + ε̃²Γ̃_2 + O(ε̃³)
with Γ̃_1 = ½(e^{iϑ}B + e^{−iϑ}B^†) (B: fibre K → fibre K', symbol b_n) and ¼w_n the ϑ-free part of Γ̃_2 (expansion of
ℓ²(M_UΔ_U^{-1}M_U^† + 𝒞_n(U)) to second order; the second-order terms through an intermediate fibre K ± P combine into
YΛ^{-1}Y^†, Y := M_1 − MΛ^{-1}Δ_1, exactly; every power of ℓ cancels in level units):
  b_n(K; P) = −Σ_m[d'_mσ_md_m/(λ̃'_mλ̃_m) − d'_mũ^-_m/λ̃'_m − ũ_md_m/λ̃_m],
  w_n(K; P) = Σ_m[2d_mm̃_m/λ̃_m − d_m²ŵ_m/λ̃_m²] + c_2 + Σ_m(σ_md_m/λ̃_m − ũ^-_m)²/λ̃'_m + Σ_m(σ_md_m/λ̃_m − ũ^{(−)}_m)²/λ̃(x_m − Pe_2).
(This is the level part of f12's integrand, with the σ = − intermediate term written on the fibre K − P instead of after the
shift K → K − P that f12 uses; the integrals agree.) **[RFL10-fix S10-4: these explicit b_n, w_n were NOT numerically tested in
session 10; f13 Part B evaluates x_n through the identity (b) from f12's h_n, i.e. it tests the conclusion of UIR-S, not
(VC)'s vertex data. UIR-S uses b_n, w_n only through their structural classes (§76 Reading (2)), so this is a disclosure, not a
defect. Session 11 tests them directly: f14 (a), §91.]**
*Proof.* (a) As in §65 (b) (umklapp: 2P ∉ 2πZ⁴ for 0 < |P| < π), [ε̃²]τ_n log Γ̃_n = ¼∫dK/(2π)⁴[w_n/γ_n − b_n²/(γ_nγ_n')] (b_n real,
§65 (b)), so x_n(P) = (2/P²)∫dK/(2π)⁴F_n with F_n := −¼[w_n/γ_n − b_n²/(γ_nγ_n(K + P))]. Here γ_n ≥ c_n ≥ s^{-1} (n ≥ 1), and γ_n has
its only pole at K ≡ 0, ~ |K|^{-2}; b_n has poles of order ≤ 1 at K ≡ 0, −P; w_n of order ≤ 2 at K ≡ 0 and ≤ 1 at K ≡ ±P; so
F_n has singularities ≲ |K|^{-2}, |K ± P|^{-2} only, and the m ≠ 0 alias sums converge absolutely (§76 Lemma A). So F_n ∈ L¹, x_n
is finite, and the torus argument of §74 (1) (antiperiodic torus of side Nℓ, half-shifted level grid, aliases exact)
identifies the integral with the ε̃² density. Evenness in P: h_n is even (S-2pt (c)) and x_0 is even (§74), so x_n is
even by (b). (Pointwise, F_n(−K, −P) = F_n(K, P) from the parity of the form factors, Lemma VC (ii).)
(b) On the antiperiodic torus of side Nℓ (Δ_U invertible near U = 1; the covariant constructions see the seam as a flat
holonomy −1), the determinant identity log det(Δ + M^†𝒞^{-1}M) + log det 𝒞 = log det Δ + log det(𝒞 + MΔ^{-1}M^†) (S-red (ii)) holds
exactly along the plane-wave family for p ∈ (2π/(Nℓ))Z; its ε² coefficient per fine site reads h^{(N)}_n(p) = (p²/2)[x^{(N)}_0(p) −
x^{(N)}_n(ℓp)] with ℓ^{-4}[ε²]τ_n log Γ_n^{-1}/(p²/2) = [ε̃²]τ_n log Γ̃_n^{-1}/(P²/2) (Γ_n^{-1} = ℓ²Γ̃_n^{-1}, ε² = ℓ^{-2}ε̃², p² = ℓ^{-2}P²).
Each density converges as N → ∞ (h_n: smooth gapped integrand, f12; x_0 and x_n: (a) and §74 (1)), so x_n(ℓp) = x_0(p) −
h_n(p)/(p²/2) on a dense set of p ∈ (0, π/ℓ), hence everywhere there by continuity of the three sides.
(c) Put Π_n(p) := h_n(p)/(p²/2) = 2ĥ(pe_2)sin²(p/2)/p² → ĥ(0)/2 = c^S_n (§65 (c)). By (b) and Lemma FINE-IR, for P → 0:
x_n(P) − 2c_g log(1/P) = [x_0(P/ℓ) − 2c_g log(ℓ/P)] + 2c_g n log L − Π_n(P/ℓ) → a_0 + 2c_g n log L − c^S_n = a_0 − ρ_n (S-red (iii):
c^S_n = 2c_g log ℓ + ρ_n). So a_n exists and a_n = a_0 − ρ_n; with φ_k = c^S_{k+1} − c^S_k (S-tel (c)), φ_k − 2c_g log L = ρ_{k+1} − ρ_k =
a_k − a_{k+1}. ∎
*Reading.* (IRR*) is not needed: the log coefficient 2c_g of every level-n polarisation is FORCED by the finiteness of c^S_n
and the fine expansion. f13 Part B reports Y_n(0.05) − (a_0 − ρ_n) = 9.9e-8, 5.3e-8, 4.8e-8, 4.8e-8 (n = 1..4), the O(P²)
remainder at P = 0.05.

## 76. Theorem UIR-S ((UIR), hence (V-IR-S) and (S4) with θ = L^{-2}, for the scalar proxy): PROVEN-HERE

Statement: §73 (T3). Write ε_{nm} := L^{-2n} + L^{-2m}, r := |(K, P)|, ρ_0 := |K|, ρ_± := |K ± P| (K, P real, near 0).
**Lemma A (form-factor bounds).** For |Re x_μ| ≤ πℓ, |Im x_μ| ≤ δ_0 and |P| ≤ r_0 (fixed small δ_0, r_0), uniformly in n:
(A1) |D_1(x/ℓ)| = |sin(x/2)/s_ℓ(x)| ≤ C|sin(x/2)|/(1 + |x|); |s_ℓ(x)/(x/2) − 1| ≤ C|x|²/ℓ², and λ̃(x) := Σ(2s_ℓ(x_μ))² has Re λ̃ ≥ c|x|²
  − Cδ_0²; (A2) |σ| ≤ C|x_1|, |σ − 2x_1| ≤ C|x_1|³/ℓ², |ŵ| ≤ C, |ŵ − 2| ≤ C|x_1|²/ℓ²;
(A3) every partial digit product Π_{r∈I}δ_r(q) (I an interval of digits, possibly with q → q ± p on a sub-interval) is bounded by
  C, and in direction 2 the shifted products F2_i(x_2/ℓ; P/ℓ) obey |F2_i| ≤ C/(1 + |x_2|): writing F2_i = [sin A/sin A']·sin((x_2 +
  P)/2)/(ℓ sin(x_2/2ℓ)) with A := L^iq/2, A' := A + L^{i−n}P/2, either |sin A'| ≥ 2L^{i−n}|P|, and |sin A/sin A'| ≤ 3/2, or |sin A'| <
  2L^{i−n}|P|, and then |F2_i| ≤ |Π_{r<i}δ_r(q)| = |sin A|/|L^i sin(q/2)| ≤ C|P|/|x_2|;
(A4) |ũ| ≤ C(1 + log(1 + |x_1|))/(1 + |x_1|)·Π_{μ≥2}C/(1 + |x_μ|) and |m̃| ≤ C/(1 + |x_1|)·Π_{μ≥2}C/(1 + |x_μ|): the κ-th term of ũ is
  (2/3)L^{−1−j}|sin(L^{−1−j}x_1)|·|Π_{r<κ}δ_r|·|Π_{r>κ}δ_r| (j := n − 1 − κ) with |Π_{r>κ}δ_r| ≤ π/|x_1| for |x_1| ≤ πL^j and |Π_{r<κ}δ_r| ≤
  CL^{1+j}/|x_1| otherwise, so it is ≤ C min(L^{−2−2j}, 1/|x_1|) and the j-sum gives the bound; m̃ likewise with L^{−2−2j} in place
  of L^{−1−j}|sin|; **[RFL10-fix S10-3: the per-j bound is CL^{−1−j}min(L^{−1−j}, 1/|x_1|) for |x_1| ≤ πL^j, and C/|x_1| for
  |x_1| > πL^j (using |Π_{r<κ}δ_r| ≤ πL^{j+1}/|x_1|); the log in the stated bound comes from the second case, i.e. from the j
  with πL^j < |x_1|; the j-sum is ≤ C(1 + log(1 + |x_1|))/(1 + |x_1|) as stated]**;
(A5) (limits) d, σ, ŵ, ũ, m̃, c_n, c_2 converge as n → ∞ (s_ℓ(x) → x/2; the digit products to infinite products; the κ-sums to
  their j-series), each with error ≤ C(|x|²/ℓ²)·(its bound in (A1)-(A4)) + CL^{-2n}, uniformly on the same complex region.
*Proof.* Closed forms: Π_{r<i}δ_r(q) = sin(L^iq/2)/(L^i sin(q/2)), Π_{r≥i}δ_r(q) = sin(ℓq/2)/(L^{n−i}sin(L^iq/2)), and the tails of the
geometric j-series (L^{−1−j}|sin(L^{−1−j}x)| ≤ L^{−2−2j}|x|). The bounds follow by the case splits stated. ∎
**Lemma VC (level-unit vertex convergence at U = 1; S-fix's method on the explicit alias sums).** Let λ̃_n(K) := Σ_μ(2s_ℓ(K_μ))²
(the m = 0 alias, ℓ = L^n) and, on the complex polydisc 𝔻 := {|K_μ| < r_0, |P| < r_0},
  h_n := λ̃_n(K)γ_n(K),  β_n := λ̃_n(K)λ̃_n(K + P)b_n,  ω_n := λ̃_n(K)²λ̃_n(K + P)λ̃_n(K − P)w_n,  N_n := ω_n/h_n − β_n²λ̃_n(K − P)/(h_nh_n(K + P)).
Then (i) h_n, β_n, ω_n, N_n are analytic on 𝔻, bounded uniformly in n, |h_n| ≥ ½ there, h_n(0) = 1, and
  F_n = −N_n/(4λ̃_n(K)λ̃_n(K + P)λ̃_n(K − P))  on 𝔻 ∩ (real, K ∉ {0, ±P});
(ii) N_n is even under (K, P) ↦ (−K, −P), and its Taylor polynomial of degree ≤ 5 at 0 is n-INDEPENDENT:
  N_n = −2|K + P|²|K − P|² + 4K_1²|K + P|² + O(r⁶);
(iii) sup_𝔻|N_n − N_m| ≤ Cε_{nm}, and |λ̃_n − λ̃_m|(K) ≤ Cε_{nm}|K|⁴ on 𝔻;
(iv) on the real region Ω_out := {K ∈ [−π, π]⁴: |K| ≥ r_0/4}, |P| ≤ r_0/8: |∂^α_{K,P}(F_n − F_m)| ≤ Cε_{nm} for |α| ≤ 2.
*Proof.* (i) The m = 0 terms are explicit analytic functions times the poles 1/λ̃_n(K), 1/λ̃_n(K ± P) (orders as in §75 (a)),
which the prefactors remove; the m ≠ 0 terms have |x_m| ≥ 2π − 2r_0, hence λ̃(x_m), λ̃(x_m ± Pe_2) bounded away from 0 on 𝔻, and the
alias sums converge absolutely and uniformly by Lemma A: each term carries at least one factor 1/λ̃ (every term of Γ̃_n passes
through Δ^{-1} once). Term by term (the types d'σd/(λ̃'λ̃), d'ũ^-/λ̃', ũd/λ̃, d²ŵ/λ̃², dm̃/λ̃, (σd/λ̃ − ũ^±)²/λ̃^±), the
bounds (A1)-(A4) give Σ_m(1 + |x_m|²)|term_m| < ∞: e.g. the worst in direction 1, σ²d²/(λ̃²λ̃'), is ≲ Π_{μ≥2}(1 + |x_μ|)^{-2}|x|^{-6};
d'σd/(λ̃'λ̃) ≲ (1 + |x_1|)^{-1}Π_{μ≥2}(1 + |x_μ|)^{-2}|x|^{-4}; (ũ^±)²/λ̃^± ≲ log²(2 + |x_1|)(1 + |x_1|)^{-2}Π_{μ≥2}(1 + |x_μ|)^{-2}|x|^{-2}. h_n(0) = d_0(0)² = 1 since every other term carries λ̃_n(0) = 0; |h_n − 1| ≤
C|K|² gives |h_n| ≥ ½ on 𝔻 for r_0 small **[RFL10-fix S10-3: |h_n(K + P)| ≥ ½ and the analyticity of h_n(K ± P), λ̃_n(K ± P)
need K ± P ∈ 𝔻; all statements on 𝔻 below are read with K and P in the half-radius polydisc 𝔻_{1/2} := {|K_μ| < r_0/2,
|P| < r_0/2}, on which K ± P ∈ 𝔻; the Cauchy estimates of the proof of UIR-S then use 𝔻_{1/2}. (A5)'s uniformity "on the same
complex region" for the κ-series follows from the closed forms because L^{−1−j}Im x stays bounded; "F_n(K, P) → F_n(K, 0)
pointwise" (UIR-S (3)) is the continuity of the alias sums at P = 0 for K ≠ 0, true because the intermediate poles
1/λ̃(K ± P) are continuous there]**. The formula for F_n is algebra (w/γ = ω/(λ̃λ̃_+λ̃_-h), b²/(γγ_+) = β²/(λ̃λ̃_+hh_+)).
(ii) Parity: d, ŵ, m̃, λ̃ are even and σ, ũ odd under (x, P) ↦ (−x, −P) (G_κ is odd in k_1; δ_r even; m ↦ −m), so b_n is odd and γ_n,
w_n are even, hence N_n is even and has no Taylor terms of odd degree. Orders: d_0 = 1 + O(K²), σ_0 = 2K_1 + O(K³), ũ_0 = O(r)
(G_κ(0) = 0), λ̃_n = |K|² + O(K⁴), and the m ≠ 0 parts of γ_n, b_n, w_n are analytic on 𝔻. Hence h_n = 1 + O(r²), β_n = −2K_1 + O(r³)
(the ũ terms carry an extra λ̃: O(r³); the m ≠ 0 terms O(r⁴)), and ω_n = −2|K + P|²|K − P|² + 4K_1²(|K − P|² + |K + P|²) + O(r⁶)
(the m̃ term is O(r⁶), c_2 = O(P²) times λ̃²λ̃_+λ̃_- is O(r¹⁰), the ũ parts of the intermediate terms are O(r⁶), the m ≠ 0 parts
O(r⁸)). So N_n = ω_n − β_n²|K − P|² + O(r⁶) = −2|K + P|²|K − P|² + 4K_1²|K + P|² + O(r⁶). Every coefficient written is
n-independent; the n-dependence (s_ℓ, c_n, the κ-series, the m ≠ 0 aliases) enters only at degree ≥ 6 (degree 5 vanishes by
parity). [Check at P = 0: F_n = −N_n/(4|K|⁶) + … = ½(1/|K|² − 2K_1²/|K|⁴) = ½∂_1(K_1/|K|²) to leading order, the Ward total
derivative.]
(iii) By (A5) and dominated convergence on 𝔻 (S-fix's argument: the relative errors O(|x|²/ℓ²) are absorbed by the factor
|x|^{-2} that every alias term carries, so Σ_m|x_m|²|term_m| < ∞; the alias tail beyond |x_μ| > πℓ of the limit sums is ≤ Cℓ^{-2}
for the same reason), sup_𝔻|γ-, b-, w-data of n minus those of m|, after multiplication by the λ̃ prefactors, is ≤ Cε_{nm}; since
the prefactors themselves satisfy |λ̃_n − λ̃_m| ≤ Cε_{nm}|K|⁴ (s_ℓ(z) = (z/2)(1 − z²/(24ℓ²) + …)), N_n − N_m is ≤ Cε_{nm} on 𝔻.
(iv) On Ω_out all denominators are bounded below (γ_n ≥ s^{-1}; λ̃(x_m) ≥ c|x_m|² ≥ c' for every alias, the m = 0 one included,
since |K|, |K ± P| ≥ r_0/8), and the K- and P-derivatives of the alias terms obey the bounds of Lemma A with the same or better
decay (derivatives of s_ℓ-factors keep the relative O(|x|²/ℓ²) error; derivatives of 1/λ̃ decay faster); dominated convergence
gives the claim. ∎
*Proof of Theorem UIR-S.* Fix n, m ≥ 1, ε := ε_{nm}, D := F_n − F_m, and 0 < |P| ≤ P_0 := r_0/16.
(1) *Bounds near the IR.* By Lemma VC (ii)-(iii), N_n − N_m is analytic on 𝔻, ≤ Cε there, and vanishes to order 6 at 0 (its Taylor
polynomial of degree ≤ 5 is zero), so (Cauchy) |∂^α(N_n − N_m)| ≤ Cεr^{6−|α|} on a smaller real ball, |α| ≤ 2; and |∂^αN_m| ≤
Cr^{4−|α|}. On the real points, λ̃_n(q) ≥ c|q|², |∂^αλ̃_n(q)^{-1}| ≤ C|q|^{−2−|α|}, and |∂^α(λ̃_n(q)^{-1} − λ̃_m(q)^{-1})| ≤ Cε|q|^{−|α|} (by
(iii): the difference is (λ̃_m − λ̃_n)/(λ̃_nλ̃_m)). Writing D = −(N_n − N_m)/(4λ̃_nλ̃_n^+λ̃_n^-) − (N_m/4)[1/(λ̃_nλ̃_n^+λ̃_n^-) − 1/(λ̃_mλ̃_m^+λ̃_m^-)] and
telescoping the last bracket:
  (B1) |D(K, P)| ≤ Cε r⁶/(ρ_0²ρ_+²ρ_-²) for |K| ≤ r_0/4;
  (B2) |∂_t²D(K, t)| ≤ Cε|K|^{-2} for 2|P| ≤ |K| ≤ r_0/4 and |t| ≤ |P| (then ρ_±(t) ≥ |K|/2 and r ≤ 2|K|; each Leibniz term has
  degree −2); and |D(K, 0)| ≤ Cε there.
(2) *Away from the IR*, Lemma VC (iv) gives |D|, |∂_t²D| ≤ Cε on Ω_out.
(3) *Ward identity at P = 0 (each n).* The constant field U_{x,1} = e^{iε cos ϑ} is the pure gauge U^g, g(x) = e^{−iε cos ϑ x_1}; M_U, 𝒞_n(U),
Δ_U are covariant (COV-sc), so Γ̃_n(U^g) = g_levΓ̃_n(1)g_lev^{-1} with g_lev(X) = g(ℓX), i.e. the level symbol is shifted by ε̃cos ϑ in
K_1. Comparing with the plane-wave expansion at P = 0: b_n(K; 0) = ∂_1γ_n(K), w_n(K; 0) = ∂_1²γ_n(K) (the ϑ-free part of
½ε̃²cos²ϑ∂_1²γ_n is ¼ε̃²∂_1²γ_n). So F_n(K, 0) = −¼∂_1(∂_1γ_n/γ_n), with ∂_1γ_n/γ_n = O(|K|^{-1}) periodic and its derivative in L¹;
∫_{T⁴}F_n(K, 0)dK = 0 (excise B_r). F_n(K, P) → F_n(K, 0) pointwise as P → 0 (continuity of the alias sums).
(4) *The estimate.* Split T⁴ = {|K| < 2|P|} ∪ {|K| ≥ 2|P|}. By (B1) and scaling, ∫_{|K|<2|P|}|D(K, P)|dK ≤ CεP⁶·P^{4−6}·I_* = CεP⁴,
I_* := ∫_{|q|≤2}dq/(|q|²|q + e|²|q − e|²) < ∞. On |K| ≥ 2|P| the function t ↦ D(K, t), |t| ≤ |P|, is C² (its singular points are
avoided), so D(K, P) = D(K, 0) + P∂_tD(K, 0) + R(K, P) with |R| ≤ ½P²sup_{|t|≤|P|}|∂_t²D(K, t)|. Then:
∫_{|K|≥2|P|}D(K, 0) = −∫_{|K|<2|P|}D(K, 0) = O(εP⁴) by (3) for n and m; ∫_{|K|≥2|P|}∂_tD(K, 0) = 0 because D(−K, −t) = D(K, t)
(Lemma VC (ii) and the parity of F_n on all of T⁴) makes ∂_tD(·, 0) odd and the region is symmetric; ∫_{|K|≥2|P|}|R| ≤
½P²[∫_{|K|≤r_0/4}Cε|K|^{-2}dK + Cε] ≤ CεP². Hence |∫_{T⁴}D(K, P)dK| ≤ CεP², i.e.
  |x_n(P) − x_m(P)| = (2/P²)(2π)^{-4}|∫D| ≤ C L^{-2min(n,m)}·2,  0 < |P| ≤ P_0.
(5) *Conclusion.* By Proposition IR-id, a_n − a_m = lim_{P→0}(x_n(P) − x_m(P)), so |a_n − a_m| ≤ 2Cε_{nm}: (a_n) is Cauchy, a_* :=
lim a_n exists, |a_n − a_*| ≤ 2CL^{-2n}, and sup_n|a_n| < ∞ — **(UIR)**. Then ρ_n = a_0 − a_n converges, sup_n|ρ_n| < ∞ —
**(V-IR-S)** — with ρ_∞ = a_0 − a_* and |ρ_n − ρ_∞| ≤ 2CL^{-2n}; and |φ_k − 2c_g log L| = |a_k − a_{k+1}| ≤ 2C(L^{-2k} + L^{-2k-2}) — **(S4)
with θ = L^{-2}**. ∎
*Reading.* (1) The three tasks of REVIEW_FLOW_S9 §3.3 (4) are Lemma A (alias summability with the slower G_κ form factors:
1/|x_1| up to a log, enough because every alias term carries a 1/λ̃), Lemma VC (iii) (the ℓ^{-2} rate: the relative error
O(|x|²/ℓ²) of every form factor, absorbed by that 1/λ̃), and Lemma VC (ii) with the estimate (IR uniformity in n: N_n − N_m
vanishes to order 6, two orders more than N_n itself, because the leading minimal-coupling structure −2|K + P|²|K − P|² +
4K_1²|K + P|² is n-independent: d(0) = 1, σ → 2K_1, ŵ → 2 — the Ward/charge normalisation). (2) The proof uses the §65 (b) form
factors u, m_2, c_2 only through their structural classes (digit products and κ-series, parity, ũ(0) = 0), not through
their exact coefficients; S9-7's provenance caveat on u and m_2 therefore does not touch it. (3) Since λ̃_n, not |K̂|², is the
natural IR normaliser here, the [S10-corr] of §67 is what makes h_n analytic. (4) f13 Part B (pre-stated, 23/23 with Parts A, C):
Δ_n = max_P|Y_n − Y_{n−1}| = 1.4582e-4, 1.3794e-5, 1.5161e-6, 1.6829e-7 for n = 2..5 (ratios 0.0946, 0.1099, 0.1110 → L^{-2}), the
maximum always at the smallest P = 0.05, and |ΔY|(0.05) ≤ 2|ΔY|(0.4) (no growth toward the IR), with step control ≤ 2.4e-11:
the uniform-in-P geometric convergence that the proof asserts. **[RFL10-fix S10-4: f13 B computes x_n through the identity
(b) from f12's h_n, so it is a direct test of UIR-S's CONCLUSION, not of (VC)'s vertex data b_n, w_n; those are tested in
f14 (a).]**

## 77. Lemma V-bord (bordered Woodbury about the massless K_F): PROVEN-HERE

Statement: §73 (T4) (finite-dimensional: on tori where K_F(U) and Δ_U are invertible, or fibrewise at U = 1 for level momenta
K ≠ 0, per colour component; X_U invertible, which holds when K_F > 0 since then X_U ≥ 𝒞_n > 0).
*Proof.* (a) DE'D^* = DD^* − Dιι^*D^*, so Ã = K_F + M^T𝒞_n^{-1}M − Dιι^*D^* = K_F + B^*JB with B :=
(M; ι^*D^*) and J := diag(𝒞_n^{-1}, −1). The determinant form of Woodbury gives det Ã = det K_F·det J·det(J^{-1} + BK_F^{-1}B^*), and
J^{-1} + BK_F^{-1}B^* = [[X_U, b_U], [b_U^*, −1 + ι^*D^*K_F^{-1}Dι]] = [[X_U, b_U], [b_U^*, −δ_U]]. The Schur complement on X_U gives
det = det X_U·det(−δ_U − b_U^*X_U^{-1}b_U) = (−1)^{N_ℓ}det X_U·det(δ_U + b_U^*X_U^{-1}b_U), and det J = (−1)^{N_ℓ}det 𝒞_n^{-1} (N_ℓ := rank ι);
the signs cancel. The ghost identity is Jacobi's complementary-minor formula det(Δ_U|_{Λ'}) = det Δ_U·det((Δ_U^{-1})|_{Ran ι}). The
formula for total_n follows by adding logarithms. Equivalently (Woodbury), δ_U + b_U^*X_U^{-1}b_U = 1 − ι^*D^*A^{-1}Dι with A :=
K_F + M^T𝒞_n^{-1}M, i.e. det Ã = det A·det(1 − ι^*D^*A^{-1}Dι).
(b) Since DD^*D = DΔ_U, K_FD = DΔ_U + E_U, hence K_F^{-1}D = DΔ_U^{-1} − K_F^{-1}E_UΔ_U^{-1}. Then δ_U = 1 − ι^*D^*DΔ^{-1}ι +
ι^*D^*K_F^{-1}EΔ^{-1}ι = ι^*D^*K_F^{-1}E_UΔ_U^{-1}ι (D^*D = Δ_U, ι^*ι = 1), and b_U = M_UD_UΔ^{-1}ι − M_UK_F^{-1}E_UΔ^{-1}ι. Gauge
covariance of the block map, 𝔪_n(U^{e^{tλ}}) = 𝔪_n(U)^{e^{tλ}|_{level}}, differentiated at t = 0 in the exponential charts, is
M_UD_U = D_ℓ^{𝔪(U)}∘ι^* (for every U at which 𝔪_n is defined; the S4'/W_♮ constructions are covariant by construction), so
M_UD_UΔ^{-1}ι = D_ℓg_U. At critical U (E_U = 0): δ = 0 and b = D_ℓg; with g invertible, log det(b^*X^{-1}b) = 2log det g +
log det(D_ℓ^*X^{-1}D_ℓ) and the two log det g cancel. Finally, for injective D_ℓ, V := D_ℓ(D_ℓ^*D_ℓ)^{-1/2} is an isometry onto Ran D_ℓ,
det(D_ℓ^*X^{-1}D_ℓ) = det(D_ℓ^*D_ℓ)·det(V^*X^{-1}V), and Jacobi gives det(V^*X^{-1}V) = det_⊥X/det X. ∎
*Reading.* (1) REVIEW_FLOW_S9 §6 (1) is confirmed and extended: the identity holds for EVERY U (no criticality, no mass); the
whole off-shell content sits in the two defect terms, both linear in E_U = H(U)D_U. (2) At U = 1 and at critical backgrounds,
E'_n has disappeared: total_n = [½log det K_F − log det Δ_U]_fine + ½log det_⊥X_U + ½log det(D_ℓ^*D_ℓ), the last being the level-n
nearest-neighbour covariant Laplacian of the block field 𝔪_n(U). (3) f13 Part C (SU(2) root sector, torus 6 × 6 × 3 × 3, ℓ = 3,
straight-path decimation block map, 𝒞 = 1, finite-difference Wilson Hessian): the identity to 8e-15 (flat twisted) and 0
(plane wave), MD_U = D_ℓι^* to 2e-16, and at the flat background |δ| ≤ 6e-16, |b − D_ℓg| ≤ 4e-16. **[RFL10-fix S10-5: the
determinant identity (C1) holds for any matrices of compatible shapes, so it tests the implementation only; the lattice-gauge
content is MD_U = D_ℓι^* (C3, straight-path map, 𝒞 = 1, NOT the S4'/W_♮ map, for which it is proven by covariance but not
checked numerically) and the flat-background δ, b (C4). The words "exact on a real lattice gauge configuration, off-shell
included" (§81) overread C1.]**

## 78. Lemma V-Jac (ghost decimation) and Proposition V-tel (n-independent vector steps): PROVEN-HERE

Statements: §73 (T5), (T6).
*Proof of V-Jac.* For S ⊂ S' ⊂ Λ and invertible A on Λ, Jacobi gives det(A|_{Λ∖S}) = det A·det((A^{-1})|_S); applied to Λ_{k+1} ⊂ Λ_k
with A := Δ^{(k)} on Λ_k ((Δ^{(k)})^{-1} = (Δ_U^{-1})|_{Λ_k}, so ((Δ^{(k)})^{-1})|_{Λ_{k+1}} = (Δ^{(k+1)})^{-1}): det(Δ^{(k)}|_{Λ_k∖Λ_{k+1}}) =
det Δ^{(k)}/det Δ^{(k+1)}. The product over k < n telescopes to det Δ_U/det Δ^{(n)} = det(Δ_U|_{Λ∖Λ_n}) (Jacobi once more). The k-th
factor involves only Δ_U, Λ_k and Λ_{k+1}. ∎
*Remark (4D; why the decimated ghost is not used for n-uniform bounds).* At U = 1 the level-k symbol of (Δ^{(k)})^{-1} is
g_k(K) = ℓ_k^{-4}Σ_m1/λ(k_m) = ℓ_k^{-2}/λ̃(K) + g_{k,reg}(K), g_{k,reg} → G_{Z⁴}(0) (≈ 0.155, REVIEW_FLOW_S9 §5) as k → ∞: the
decimated Laplacian is dominated by the UV constant 1/G_{Z⁴}(0), and has no level-unit scaling limit (unlike the scalar step
data of §67). This is the same 4D capacity effect as Δ'(1)'s gap ≍ ℓ^{-4}. The ghost is solved exactly by GH-log (c); V-Jac is
recorded as the exact n-independent telescoping, not as a source of uniform bounds.
*Proof of V-tel.* With A^{(k)}_j := T_{k−1}⋯T_j (A^{(k)}_k := 1), COV-str (ii) at level k and M = A^{(k)}_0 (𝔪_k is the k-fold
composition of the one-step map, so D𝔪_k(U_0) = T_{k−1}⋯T_0 by the chain rule, B_j = 𝔪_j(U_0)) give X^{(k)} := 𝒞_k + MK_F^{-1}M^T =
A^{(k)}_0K_F^{-1}A^{(k)T}_0 + κ^{-1}Σ_{j=1}^kA^{(k)}_jΠ_j^{-1}A^{(k)T}_j; since A^{(k+1)}_j = T_kA^{(k)}_j (j ≤ k), X^{(k+1)} = T_kX^{(k)}T_k^T +
κ^{-1}Π_{k+1}^{-1}, X^{(0)} = K_F^{-1}. Sylvester: det(TXT^T + κ^{-1}Π^{-1}) = det(κΠ)^{-1}det(1 + κXT^TΠT) = det(κΠ)^{-1}det X·det(X^{-1} +
κT^TΠT), so log det X^{(k+1)} = log det X^{(k)} + log det H^V_k − log det(κΠ_{k+1}); sum from log det X^{(0)} = −log det K_F. With (T4):
total_n = [½log det K_F − log det Δ_U] + ½log det X_n + ½log det(δ + b^*X_n^{-1}b) − log det g = −log det Δ_U + ½Σ_{k<n}Φ^V_k +
½log det 𝒢_n, 𝒢_n := g^{-1}(δ + b^*X_n^{-1}b)g^{-1}. Each Φ^V_k is built from K_F, T_0, …, T_k, Π_1, …, Π_{k+1} only (n-independent). ∎
*Reading.* (1) The fine Feynman piece ½log det K_F cancels identically against the X-telescoping (as τ log Δ does in the
scalar S-tel); what remains is the fine ghost −log det Δ_U, the n-independent steps, and ONE level-n object 𝒢_n. (2) At
critical U, 𝒢_n = D_ℓ^*X_n^{-1}D_ℓ and ½log det X_n + ½log det 𝒢_n = ½log det_⊥X_n + ½log det(D_ℓ^*D_ℓ). (3) Gaps: H^V_0(1) =
K_F(1) + κT_0^TΠ_1T_0 and, for k ≥ 1, H^V_k(1) (X_k ≥ κ^{-1}Π_k^{-1}, so X_k^{-1} is bounded and vanishes only on the K = 0 constant
1-forms, which T_k does not annihilate) are fibrewise positive definite, hence gapped for each k (§66 (b) argument); a
k-uniform gap (a vector S-fix) is NOT proved here.

## 79. The off-shell defect (§73 (T7)): (a) PROVEN-HERE; (b) corrected; (c) OPEN — the wall named

*(a) Statement and proof.* For every U and every adjoint 0-form λ:
  (E_Uλ)_b = ½[Ad(U_b^{-1})λ(x) + λ(x + μ), J_b],  J_b := ∇_bS_W(U) ∈ su(N)  (b = (x, μ); exponential chart; ⟨A, B⟩ = −½tr AB).
Proof: gauge invariance gives ∇S(U)·V_λ(U) = 0 for all U, with V_λ(U)_b := Ad(U_b^{-1})λ(x) − λ(x + μ). Differentiate along U e^{sY}:
∂_s∂_tS(Ue^{sY}e^{tV}) = H(Y, V) + ½∇S·[Y, V] (from e^{sY}e^{tV} = e^{sY + tV + ½st[Y,V] + …}), and ∂_YV_λ = −[Y_b, Ad(U_b^{-1})λ(x)];
so ⟨Y, H V_λ⟩ = −∇S·(∂_YV_λ + ½[Y, V_λ]) = ½Σ_b⟨J_b, [Y_b, Ad(U_b^{-1})λ(x) + λ(x + μ)]⟩ = Σ_b⟨Y_b, ½[Ad(U_b^{-1})λ(x) + λ(x + μ), J_b]⟩ by
ad-invariance. So E_U is linear in the current J = ∇S_W, and E_U = 0 at critical U. At a Cartan background J is Cartan-valued
(torus invariance). Along the Cartan plane wave H_1ε cos(px_2 + ϑ) on the 1-links the plaquette angles are O(ε) and the Wilson
current is odd in them, so J = εJ_1 + O(ε³), with J_1 = c_N H_1·d^*da (c_N a fixed normalisation constant; for SU(2), S_W =
Σ_P(1 − cos θ_P) and J_b = Σ_{P∋b}±sin θ_P), and for a = cos(px_2 + ϑ)e_1: (d^*da)_1 = (2 − 2cos p)a_1, (d^*da)_μ = 0 (μ ≠ 1). Hence
E_U = εp̂²Ê + O(ε³) (p̂² := 2 − 2cos p), Ê the same commutator with J replaced by c_NH_1cos(px_2 + ϑ)e_1; in the root sector α,
[H_1, E_α] = iq_αE_α makes Ê the multiplication by (i/2)c_Nq_α cos(px_2 + ϑ) times the link-end average of λ on the 1-links. ∎
**[RFL10-fix S10-1] Correction (the formula above is exact; its expansion is not).** J = εJ_1 + O(ε³) is right, but the
coefficient Ad(U_b^{-1}) = exp(−εa_b ad H_1) on the 1-links has an O(ε) term, so
  E_U = εp̂²Ê_1 + ε²p̂²Ê_2 + O(ε³),  (Ê_1λ)_b = ½[λ(x) + λ(x + e_1), c_NH_1cos(px_2 + ϑ)],
  (Ê_2λ)_b = −½cos²(px_2 + ϑ)[[H_1, λ(x)], c_NH_1]  (on the 1-links; zero on the others).
In the root sector α, Ê_1 is −i c_Nq_α cos(px_2 + ϑ) times the link-end AVERAGE of λ (equivalently (−i/2)c_Nq_α cos(px_2 + ϑ)
times the link-end sum; the earlier "(i/2) × average" had the wrong factor, not load-bearing since c_N is free), and Ê_2 is
∝ c_Nq_α²cos²(px_2 + ϑ)λ(x), a multiplication operator with a nonzero zero-momentum part (½cos² → ¼). f13 C5 cannot see Ê_2
(it is also ∝ p̂², and its Frobenius overlap with Ê_1 vanishes); REVIEW_FLOW_S10 §4.2 measured ||E_2||/||E_1|| = 1.2247 and the
ε-ratio 2.000 with f13's own E_formula.
f13 Part C: E_U = H D_U agrees with the formula to 3e-15 (reported line), and ||E(4π/6)||/||E(2π/6)|| = 2.99999925 against the
p̂² ratio 3 (C5).
*(b) Corrected statement.* By (T4) (b) and (T6), exactly for every U:
  𝒢_n = (D_ℓ − η̃_U)^*X_n^{-1}(D_ℓ − η̃_U) + δ̃_U,  η̃_U := M_UK_F^{-1}E_U𝔥_U,  δ̃_U := 𝔥_U^*Δ_UD_U^*K_F^{-1}E_U𝔥_U,
where 𝔥_U := Δ_U^{-1}ιg_U^{-1} is the discrete harmonic extension from the level sites (Δ_U𝔥ν = 0 off the level sites, ι^*𝔥ν = ν;
𝔥^* = g^{-1}ι^*Δ^{-1}, so g^{-1}ι^* = 𝔥^*Δ). With E_U = εp̂²Ê + O(ε³), the ε² coefficient of ½log det 𝒢_n is its E = 0 part plus
p̂²𝔮_{1,n}(p) (Ê once, against one first-order vertex of D_ℓ^{𝔪(U)}, X_U, M_U, K_F, Δ_U or 𝔥_U) plus p̂⁴𝔮_{2,n}(p) (Ê twice: η̃^*X^{-1}η̃ and the
second-order term of the log). In the normalisation of §65 (c) (ε² coefficient = ĥ(pe_2)sin²(p/2), 2c = ĥ(0)), the defect adds
  𝔡_{n,α} := lim_{p→0}[4𝔮_{1,n}(p) + 16sin²(p/2)𝔮_{2,n}(p)]
to 2c^tot_{n,α}, if the limit exists. **[Correction to the pre-statement §73 (T7) (b), logged:** the quadratic Ê terms were
omitted there; they contribute iff 𝔮_{2,n}(p) ≳ p^{-2}.]
**[RFL10-fix S10-1] Further correction (logged as a second correction of §73 (T7) (b)):** the list above misses the ε² term
of E itself. With E_U = εp̂²Ê_1 + ε²p̂²Ê_2 + O(ε³) (§79 (a), corrected), the ε² coefficient of ½log det 𝒢_n has THREE defect
pieces: p̂²𝔮_{0,n}(p) (Ê_2 once, against U = 1 objects: 𝔮_{0,n} = ½tr(𝒢_0^{-1}d𝒢[Ê_2^{(0)}]), d𝒢[E] = 𝔥^*D^*E𝔥 −
2Re D_ℓ^*X^{-1}MK_F^{-1}E𝔥 at U = 1), p̂²𝔮_{1,n}(p) (Ê_1 once, against one first-order vertex) and p̂⁴𝔮_{2,n}(p) (Ê_1 twice), so
  𝔡_{n,α} := lim_{p→0}[4𝔮_{0,n}(p) + 4𝔮_{1,n}(p) + 16sin²(p/2)𝔮_{2,n}(p)].
No symmetry is known that kills 𝔮_{0,n}. (The normalisation 4𝔮_1 + 16sin²(p/2)𝔮_2 was right.) By §5 of REVIEW_FLOW_S10 and
§86 below, 𝔡_{n,α} is not needed: it is the plane-wave artifact c^pw[Δ_def], and c^cf[Δ_def] = 0.
*(c) Status: OPEN. The exact wall.* At U = 1, on the fibre of the level momentum K, the smooth (m = 0) component of 𝔥 applied to the
level plane wave has amplitude c_0(K) = (ℓ^{-2}/λ̃_n(K))/g(K) = 1/(1 + ℓ²λ̃_n(K)g_reg(K)), g_reg := ℓ^{-4}Σ_{m≠0}1/λ(k_m) → G_{Z⁴}(0)
(the Riemann sum of the fine Green's function at the origin); the remaining aliases carry the "spikes" of 𝔥 at the level
sites. So the defect involves TWO scales: the level scale |K| ~ 1, where c_0 ≈ (G_{Z⁴}(0)ℓ²|K|²)^{-1} and the defect terms are
suppressed by ℓ^{-2} relative to D_ℓ (size count, not a bound: with ε = ε̃/ℓ and p̂² ≈ P²/ℓ², the m = 0 part of η̃ is of order
ε̃P²ℓ^{-2}|K|^{-2}|K + P|^{-2} in level units for |K| ≫ ℓ^{-1}); and the
capacity scale |K| ~ ℓ^{-1} (fine momentum ℓ^{-2}, the scale of Δ'(1)'s ℓ^{-4} gap), where c_0 = O(1) and nothing is suppressed.
The p² coefficient needs p → 0 at FIXED n, i.e. it probes |K| ≲ P well below ℓ^{-1}. A size count of the dominant m = 0 terms
(ARGUED, not a proof) finds no small factor once |K| ≲ ℓ^{-1}: size estimates alone decide neither 𝔡_{n,α} = 0 nor
𝔡_{n,α} = O(ℓ^{-2}). **(DEF), the wall:** compute, or bound n-uniformly, lim_{p→0}[4𝔮_{1,n} + 16sin²(p/2)𝔮_{2,n}] with the crossover
function c_0(K) = 1/(1 + ℓ²λ̃_n(K)g_reg(K)) inside the defect bubbles — the two-scale analogue, for the defect, of what GH-log (c)
does exactly for the ghost. A route that may avoid it: an exact treatment of the ½log det(1 − ι^*D^*A^{-1}Dι) − log det g block
(§77 (a)) in the manner of GH-log (c), which handles precisely this capacity scale for Δ'. f13 Part C reports the defect sizes
at n = 1 (ε = 1e-3): max|δ| = 6.4e-6, 1.4e-5 and max|b − D_ℓg| = 5.6e-5, 1.4e-4 for p = 2π/6, 4π/6; these are finite-n data, not a
test of (DEF).
**[RFL10-fix S10-2] (DEF) is RETIRED as a wall (it is real as stated, but mis-aimed).** E_U ≡ 0 on the whole critical family
U_f (constant Cartan flux) that DEFINES c^tot_n := [f²]total_n(U_f) (MS (iv), F-id-exp, given (L-loc2)); so with Δ_def :=
total_n − T^c, T^c := −log det Δ_U + ½Σ_{k<n}Φ^V_k + ½log det(D_ℓ^*X_n^{-1}D_ℓ), Δ_def(U_f) ≡ 0 and the defect is a plane-wave
artifact. Exactly at each n, c^tot_n = ½Σ_{k<n}[f²]Φ^V_k(U_f) + γ_n, γ_n := [f²]Γ^crit_n(U_f), Γ^crit_n := −log det Δ_U +
½log det(D_ℓ^*X_n^{-1}D_ℓ). The replacement walls are **(GP)**: sup_n|γ_n + 2c_gq_α²log ℓ| < ∞ (γ_n minus its GH-log (c) log
part n-uniformly bounded), or equivalently **(DEF-F)**: the plaquette-reduced U = 1 Hessian kernel of Δ_def is continuous at
q = 0 in the (12, 12) channel, so that 𝔡_{n,α} = c^pw[Δ_def] = c^cf[Δ_def] = 0. Caution: X_U ≥ 𝒞_n FAILS at U_f, because
K_F(U_f) has the Nielsen-Olesen negative mode; at U_f the K_F^{-1} form of X_n must not be used, only V-tel's Woodbury form
(gapped steps H^V_k). Session 11 (§85-§86) shows that (GP) is NOT a ghost-only statement and gives the mechanism by which it
is expected to fail; the Landau split (§87) replaces it.

## 80. Target (T8) (vector (UIR)): OPEN, reduced

What is proved: total_n = −log det Δ_U + ½Σ_{k<n}Φ^V_k + ½log det 𝒢_n exactly for every U (§77-§78); at critical U, 𝒢_n = D_ℓ^*X_n^{-1}D_ℓ
and total_n = [½log det K_F − log det Δ_U]_fine + ½log det_⊥X_U + ½log det(D_ℓ^*D_ℓ). Given (L-loc2), Lemma V-2pt (§69) turns c^⊥_{n,α}
into the U = 1 plane-wave p² coefficient of this total. By the scalar template (§74-§76), (V-IR) in the form (Q1)(d) would
follow from three statements, NONE proved here:
- **(VFINE)** the fine IR expansions of the Feynman-gauge vector polarisation of ½log det K_F and of the ghost −log det Δ_U (root
  sector, charge q_α): §74's method applies (Ward rewrite, symmetrisation, continuum comparison) — not written;
- **(VC-V)** the level-unit convergence of the vertex data of X_U = A_0K_F^{-1}A_0^T + 𝒞_n (closed form, same alias structure as the
  scalar Γ̃_n, tensor form factors from T_k, Π_k) with the n-independence of the leading (degree-4) numerator — §76's method,
  not written; and the explicit level ghost ½log det(D_ℓ^*D_ℓ), whose level-unit polarisation is n-independent once the
  level background of 𝔪_n(U) is (a plane wave with a convergent form factor — to be checked for the S4'/W_♮ map);
- **(DEF)** §79 (c), the crux.
So **Theorem UNIV for SU(N) does NOT yet rest only on (L-loc2)**; it rests on (L-loc2), (VFINE), (VC-V) and (DEF), of which
(VFINE) and (VC-V) are of the type proved here for the scalar, and (DEF) is new.
**[RFL10-fix S10-2, S10-6] Restated list.** (DEF) → (GP) (or (DEF-F)), §79 (c). In (VC-V) the level ghost
½log det(D_ℓ^*X_n^{-1}D_ℓ) belongs to (GP), not to (VC-V); the X-part ½log det X_n is to be linked to the fine Feynman
polarisation through det A = det K_F·det 𝒞_n^{-1}·det X_n (exact for every U, no E), so it needs (VFINE) for K_F only and no
defect statement; (VFINE) for the ghost −log det Δ_U is a corollary of FINE-IR (ε → q_αε; §88). Hence the list after
REVIEW_FLOW_S10: (L-loc2), (VFINE-K), (VC-V) (tensor form factors of A_0, T_k, Π_k; vector IR-id; the plane-wave form factor of
𝔪_n for W_♮), (GP). **Session 11 (§86, Proposition G2-log): the X-part of this list is not n-uniform as stated** — X_n(1) has a
longitudinal level-unit symbol that grows like (log ℓ)/(8π²) for every covariant block map — and (VC-V) is replaced by (VC-L)
in the Landau split (§87, §89).

## 81. Session-10 check f13 (ADDED AFTER the run; checks/f13_criteria.md, f13_uir_vbord.py, f13_out.txt, f13_time.txt)
Criteria written 08:53:32 UTC before any f13 script (stat in FLOW_LOG); the script was not changed after its smoke test
(cmp-identical copy; the pre-smoke development fixes are listed in FLOW_LOG). Official run: one NUMERIC LOCK acquisition,
09:08:34-09:09:31 UTC, nice 10, 1 thread, load 4.57, memory free 49% (checked inside the lock before starting); 56.4 s, peak RSS
560 MB. **23/23 verdict lines PASS.**
- **Part A (FINE-IR, §74):** A1 step halving ≤ 4.1e-14 at every q used; A2 symmetrised = unsymmetrised form to 2.1e-11 (q = 0.3)
  and 7.3e-12 (q = 0.6); **A3: −dx_0/dlog q on [10^{-3}, 10^{-2}] = 2.1108467e-3 against 2c_g = 2.1108580e-3 (rel 5.3e-6).**
  Reported: **a_0 = 2.512968892e-3** (window change 5.8e-13).
- **Part B ((VC)/(UIR), §76):** B1 step control (K grid 16⁴ vs 12⁴ at n ≤ 4; h_u 0.15 vs 0.1 at n = 5) ≤ 2.4e-11; **Δ_n =
  max_P|Y_n − Y_{n−1}| = 1.4582e-4, 1.3794e-5, 1.5161e-6, 1.6829e-7 (n = 2..5), ratios 0.09460, 0.10991, 0.11100 (B2, ≤ 0.2;
  L^{-2} = 0.11111)**, each maximum at the smallest P (0.05), and |ΔY|(0.05) ≤ 2|ΔY|(0.4) for n = 3, 4, 5 (B3). Y_5(P) =
  4.28104e-3 … 4.38390e-3 on P ∈ [0.05, 2.4]. Reported: Y_n(0.05) − (a_0 − ρ_n) = 9.9e-8, 5.3e-8, 4.8e-8, 4.8e-8 (n = 1..4; the
  O(P²) remainder at P = 0.05, consistent with Y_n(0.1) − Y_n(0.05) ≈ 1.4e-7).
- **Part C (vector, §77-§79):** C1 the (T4) determinant identity to 7.7e-15 (flat twisted) and 0.0 (plane wave); C2 ghost
  Jacobi 1.8e-16; C3 MD_U = D_ℓι^T to 2.2e-16; C4 at flat |δ| = 5.6e-16, |b − D_ℓg| = 4.2e-16; **C5 ||E(4π/6)||/||E(2π/6)|| =
  2.99999925 (p̂² ratio 3)**; C6 two-step ghost decimation 2.3e-15. Reported: E_U = ½[Ad(U_b^{-1})λ(x) + λ(x + μ), ∇_bS] to 3.3e-15;
  defect sizes as in §79 (c).
- **Reading.** (1) FINE-IR's coefficient and the existence of a_0 are confirmed independently of the proof (S10-F1 does not
  occur). (2) The level-n polarisations converge geometrically at rate L^{-2}, uniformly in P down to P = 0.05, with no IR
  growth (S10-F2 does not occur): the direct test of (VC) REVIEW_FLOW_S9 asked for. (3) The bordered identity is exact on a
  real lattice gauge configuration, off-shell included (S10-F3 does not occur); the defect is O(εp̂²) as proven (S10-F4 does
  not occur). **[RFL10-fix S10-4, S10-5: in (2), "the direct test of (VC)" → "a direct test of UIR-S's conclusion" (x_n via
  the identity (b), not via (VC)'s b_n, w_n). In (3): C1, C2 and C6 are linear-algebra identities, valid for ANY symmetric
  H and any M, D of compatible shapes; they test the implementation, not lattice-gauge content. The lattice-gauge content of
  Part C is C3 (covariance, straight-path map only, 𝒞 = 1), C4 (the FD Hessian is gauge-degenerate at a flat background) and
  the E-formula match; "off-shell included" is struck as evidence. The Part C Hessian adds a Richardson step to the central
  differences of the criteria (stronger than stated). "The defect is O(εp̂²) as proven": C5 is consistent with the corrected
  E_U = εp̂²Ê_1 + ε²p̂²Ê_2 + O(ε³) (both terms ∝ p̂²), and cannot see Ê_2.]** (4) The scalar ρ_∞ = a_0 − a_* and a_* are not computed beyond what f12 gives (ρ_∞ ≈ −1.76805e-3).

## 82. Session-10 outcomes against §73 (ADDED AFTER the derivations and the check)
- **Step 1 (fixes): DONE.** S9-1..S9-7 and the scope annotations applied in place, tagged [RFL9-fix] (16 tag occurrences
  at the fix sites, l.3186-3463; further mentions only in §73, the §74 heading and here); one session-10 correction tagged [S10-corr] (§67).
- **(T1) Lemma FINE-IR: PROVEN** (§74), no import; f13 A confirms.
- **(T2) Proposition IR-id: PROVEN** (§75): ρ_n = a_0 − a_n and φ_k − 2c_g log L = a_k − a_{k+1} exactly; (IRR*) retired.
- **(T3) Theorem UIR-S: PROVEN** (§76, with Lemma A and Lemma VC): |x_n(P) − x_m(P)| ≤ CL^{-2min(n,m)} uniformly for 0 < |P| ≤ P_0;
  hence **(UIR), (V-IR-S) and (S4) with θ = L^{-2} are PROVEN for the scalar proxy.** f13 B confirms the uniform geometric
  convergence (ratio → 0.1110).
- **(T4) Lemma V-bord: PROVEN** (§77) for every U (stronger than pre-stated: no criticality needed for the identity itself);
  the "mass" remark of session 9 withdrawn. **(T5) Lemma V-Jac: PROVEN**; its level-unit scaling fails in 4D (remark).
  **(T6) Proposition V-tel: PROVEN** (§78): n-independent steps, the fine Feynman determinant cancels, one level-n object 𝒢_n
  remains; a k-uniform vector step gap is not proved.
- **(T7) (a) PROVEN** (§79: E_U = ½[Ad(U_b^{-1})λ(x) + λ(x + μ), J_b], E = εp̂²Ê + O(ε³)); **(b) corrected** (quadratic terms added);
  **(c) OPEN — the wall (DEF) is named:** the two-scale (capacity-scale) asymptotics of the defect bubbles through the
  harmonic extension 𝔥 = Δ^{-1}ιg^{-1}. **[RFL10-fix S10-1, S10-2: the expansion clause of (a) is FALSE (an ε²p̂²Ê_2 term;
  §79 (a) corrected); (b) misses the 𝔮_0 term (§79 (b) corrected); (DEF) is retired in favour of (GP)/(DEF-F) (§79 (c)).]**
- **(T8) vector (UIR): OPEN**, reduced to (VFINE), (VC-V), (DEF) (§80). Theorem UNIV for SU(N) does NOT yet rest only on
  (L-loc2).
- **Step 4 (f13): DONE**, 23/23.

## 83. Tally after session 10 (FLOW.md items; session-10 items unreviewed)
- **PROVEN-HERE: 50 (through session 9, as confirmed by REVIEW_FLOW_S9) + 9 (session 10) = 59.** Session 10: Lemma FINE-IR;
  Proposition IR-id; Lemma A; Lemma VC; Theorem UIR-S (which settles the previously OPEN (V-IR-S) and (S4)); Lemma V-bord;
  Lemma V-Jac; Proposition V-tel; §79 (a) (the defect formula). Upstream inputs used: S-red (i)-(iii), S-2pt (b)-(c) (form-factor
  classes and evenness), S-tel (c), COV-sc (covariance), COV-str (ii), GH-log (c) (cited, not used in a proof), §65 (b)'s form
  factors through their structural classes only (§76 Reading (2)).
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT (§58). No new import.
- **ARGUED, not counted:** (L-loc2); the size count of §79 (c).
- **[RFL10-fix S10-2, tally]** REVIEW_FLOW_S10 confirms 59 (57 under the stricter convention folding Lemma A and Lemma VC
  into UIR-S); §79 (a) counts for the exact formula only; (DEF) below is replaced by (GP)/(DEF-F).
- **OPEN:** (V-IR) on G_⊥ in the form (Q1)(d) [s-P] (crux), now reduced to (VFINE) [s], (VC-V) [s], (DEF) [s-P] (§80); (L-loc2)
  to be proved [s]; a k-uniform vector step gap (vector S-fix) [s]; (s1), (s2⊥) [s-P] (rate only); the rate of c'(φ) → c'_0 [s];
  (COV-GI) at non-critical backgrounds [s]; FI-1 [cross-lane]; HIST's restatement of CL^J's Setting [cross-lane].
- **Checks:** f13 (A1, A2 ×2, A3, B1 ×5, B2 ×3, B3 ×3, C1 ×2, C2, C3, C4 ×2, C5, C6 PASS).

## 84. Session-11 targets and PRE-STATED (session 11) statements (written 2026-10-28 ~09:56 UTC, the first edit of session 11: before the [RFL10-fix] edits and before any session-11 proof, criteria file or script)

Binding input: REVIEW_FLOW_S10.md (fixes S10-1..S10-6, applied after this section, in place, tagged **[RFL10-fix]**;
(DEF) replaced by (GP)/(DEF-F); (VFINE), (VC-V); tally 59). Notation of §73, §77-§79. "Critical" U: ∇S_W(U) = 0, so
E_U = 0 and H(U)D_U = 0. P_⊥ := the orthogonal projector onto ker D_U^*, H_⊥ := P_⊥H(U)P_⊥ on ker D_U^*; D_ℓ := D_ℓ^{𝔪(U)};
G2_U := ι^*Δ_U^{-2}ι (an operator on the level-n sites); Y_U := X_U − D_ℓG2_UD_ℓ^*; V := D_ℓ(D_ℓ^*D_ℓ)^{-1/2};
Γ^crit_n := −log det Δ_U + ½log det(D_ℓ^*X_U^{-1}D_ℓ), γ_n := [f²]Γ^crit_n(U_f) (REVIEW_FLOW_S10 §5.2-§5.3); G_gh,n as in
§43 (iv), in the counting of (T4). Level symbols at U = 1 in the level units of §75 (x_m := K + 2πm, λ̃(x) := Σ_μ(2s_ℓ(x_μ))²).

**PRE-STATED (session 11).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Each hypothesis is named; nothing below uses an ARGUED or OPEN item as if proven. Any later change
of a statement is logged as such.

**(U1) Lemma GP-L (Feynman/Landau recombination at critical backgrounds).** At every critical U at which Δ_U, H_⊥ (on
ker D_U^*) and Y_U are invertible and D_ℓ is injective: (a) K_F^{-1} = H_⊥^{-1}P_⊥ + D_UΔ_U^{-2}D_U^*, hence
Y_U = 𝒞_n + M_UH_⊥^{-1}P_⊥M_U^T; (b) with Z_U := D_ℓ^*Y_U^{-1}D_ℓ: D_ℓ^*X_U^{-1}D_ℓ = (Z_U^{-1} + G2_U)^{-1}, so
Γ^crit_n = −log det Δ_U − ½log det(G2_U + Z_U^{-1}); (c) ½log det X_U + ½log det(D_ℓ^*X_U^{-1}D_ℓ) = ½log det Y_U + ½log det Z_U;
(d) Γ^crit_n − G_gh,n = ½log det(V^*X_U^{-1}V) − ½log det Δ_U. Consequently γ_n = −2c_gq_α²log ℓ + γ'_n with
γ'_n := [f²](½log det(V^*X_U^{-1}V) − ½log det Δ_U)(U_f), which exists.
**(U2) Proposition G2-log (the longitudinal divergence at U = 1).** The level symbol of G2_1 is g2_n(K) = Σ_mλ̃(x_m)^{-2}, and
ḡ_n(K) := g2_n(K) − λ̃_n(K)^{-2} = (log ℓ)/(8π²) + r_n(K), where r_n converges uniformly on {r ≤ |K|, K ∈ [−π, π]⁴} for each
r > 0. Consequently, for EVERY block map with M_UD_U = D_ℓι^* (gauge covariance), the level symbol x_n(K) of X_n(1)
obeys ⟨D̂_ℓ(K), x_n(K)D̂_ℓ(K)⟩ ≥ |D̂_ℓ(K)|⁴g2_n(K): X_n(1) has no n-uniformly bounded level-unit symbol on Ran D_ℓ, and (VC-V)
in the form of §80 / REVIEW_FLOW_S10 §6 (n-uniform level-unit vertex data of X_n) fails at U = 1 already at zeroth order.
**(U3) Lemma L-tel (Landau telescoping; exact).** For every U at which the constructions of (T6) are defined and the
one-step covariance T_kD_ℓ^{(k)} = D_ℓ^{(k+1)}ι_k^* holds (ι_k: level-(k+1) sites into level-k sites): Y^{(0)} := K_F^{-1} −
D_UΔ_U^{-2}D_U^*, Y^{(k+1)} := T_kY^{(k)}T_k^T + κ^{-1}Π_{k+1}^{-1} gives Y^{(n)} = Y_U. At critical U (invertibility as in (U1)):
total_n = ½Σ_{k<n}Φ^L_k + Γ^L_n with Φ^L_0 := log det K_F − log det Δ_U + log det Y^{(1)} = log det_⊥(P_⊥(K_F + κT_0^TΠ_1T_0)P_⊥) −
log det(κΠ_1), Φ^L_k := log det Y^{(k+1)} − log det Y^{(k)} (k ≥ 1), Γ^L_n := −½log det Δ_U + ½log det(D_ℓ^*Y_U^{-1}D_ℓ) =
G_gh,n + ½log det W_U, W_U := V^*Y_U^{-1}V. At U = 1, Y^{(0)} = P_T/λ (P_T the fine transverse projector), so no alias term of
Y_n(1) contains the covariance-forced longitudinal part of M.
**(U4) Question (GP).** Is sup_n|γ'_n| < ∞ (equivalently (GP))? And its Landau analogue (GP-L): is sup_n|w_n| < ∞, w_n :=
[f²]½log det W_U(U_f)? Outcome: proof, disproof, or the mechanism, each with what it needs; an expectation not proved is
reported ARGUED.
**(U5) Corollary VFINE-gh.** In root sector α at the Cartan plane wave, [ε²] of the fine ghost τ log Δ_U is q_α²(p²/2)x_0(p)
(Lemma FINE-IR with ε → q_αε), so its log coefficient is 2c_gq_α² and its finite part q_α²a_0.
**(U6) Lemma FINE-IR-gen.** Let O(U) be fine operators (r × r symbols) with plane-wave expansion O = O_0 + εO_1 + ε²O_2 + …
such that (G1) O_0 is analytic on T⁴, O_0(k) > 0 for k ≠ 0 and O_0(k) = |k|²·1 + O(|k|⁴); O_1 (momentum transfer ±pe_2) and the
ϑ-free part of O_2 have analytic symbols; (G2) (Ward) at p = 0 the ε² density is the integral of a total k_1-derivative of a
periodic function with an L¹ derivative; (G3) the lowest-order homogeneous parts of O_0, O_1, O_2 at small (k, p) are those
of a continuum operator O^c whose second-order polarisation integrand is even under (k, p) ↦ (−k, −p). Then
x^O(p) := [ε²]τ log O/(p²/2) = 2C_O log(1/p) + a^O + o(1), with C_O the angular coefficient of the continuum integrand and a^O
an absolutely convergent integral. Application **(VFINE-K)**: given (CL-V) (the root-sector symbols of K_F(U) at the
Cartan plane wave obey (G1)-(G3) with O^c = −D²δ_{μν} + 2iq_αF_{μν} [RFL12-fix S12-6: superseded by −2iq_αF_{μν} with D = ∂ + iq_αa, §95], the classical continuum limit of the Wilson Hessian in
Feynman form), C_{K_F} = −20q_α²c_g (heat-trace ratio R_V/R_S = (10/3)/(−1/6)).
**(U7) (VC-L) (the Landau replacement of (VC-V)) and Proposition SP-div.** (VC-L): for a block map whose transverse form
factors obey the product decay of §76 Lemma A, the level-unit vertex data of Y_n (hence of W_n) at U = 1 converge at rate
L^{-2n}, uniformly on the polydisc after λ̃²-normalisation. Target: a proof or the exact obstruction. SP-div: for the
straight-path decimation map of f13, the transverse diagonal symbol of Y_n(1) at fixed K ≠ 0 grows like ℓ, so that map is not
admissible for (VC-L).
**(U8) Target (vector (UIR)).** The vector (UIR)/(V-IR) is reduced to named statements in the split of (U3); Theorem UNIV for
SU(N) is said to rest only on (L-loc2) ONLY if every other link is proved here.

**Check f14** (criteria file first, its stat into FLOW_LOG before any f14 script; jobs < 20 min, < 1 GB, memory free ≥ 35%,
load < 8 at start). (GP) at U_f by magnetic Bloch for n ≥ 2 is outside this budget (the vector fibre at ℓ = 9 has ≥ 10⁵
dimensions per Bloch momentum); it is replaced by (c). (a) **b_n, w_n (S10-4):** on the half-shifted level grid N⁴, P = 2πj/N,
the finite-torus identity mean_K ℓ^{-4}(T_n − I_n) = mean_K ℓ^{-4}Σ_m(W_m/λ_m − Σ_m²/(λ_mλ'_m)) + ℓ^{-2}mean_K[w_n/γ_n −
b_n²/(γ_nγ_n(K + P))] (T_n, I_n of §65 (b) by the f12 functions unchanged; b_n, w_n, γ_n by §75's formulas), n = 1, 2, 3, to
≤ 1e-10 relative; the Ward identities b_n(K; 0) = ∂_1γ_n(K), w_n(K; 0) = ∂_1²γ_n(K) to ≤ 1e-7 relative; a control with the sign
of the ũ^- term flipped must fail the identity. (b) **(U2):** ḡ_n(K) − ḡ_{n−1}(K) = log L/(8π²) to ≤ 5% for n = 4..7 at two K;
for the straight-path map, the alias symbol identity M_m·D̂(k_m) = D̂_ℓ(K) (≤ 1e-12) and the growth ratio of the transverse
diagonal symbol of Y_n(1) (prediction: within 10% of L at n ≥ 3). (c) **the mechanism of (U4), scalar model:**
P_n(U) := −log det Δ_U − ½log det G2_U; its level part y_n(P) := [ε̃²]τ_n log G2_U/(P²/2) by alias sums, tested at n = 1 against
a brute-force torus (≤ 1e-6 relative); D_n(P) := y_n(P) − y_{n−1}(P) at P = π/4, π/2, n = 2..6, classified "geometric" if
|D_n/D_{n−1}| ≤ 0.2 at n = 5 and 6 (both P), "slow" if |D_6/D_5| ≥ 0.5 (both P); ARGUED prediction: slow.

**Failure modes (each a valid outcome).** (S11-F1) an identity of (a) fails (a §75 formula is wrong); (S11-F2) the slope of
ḡ_n is not log L/(8π²); (S11-F3) (c) is geometric (the mechanism behind (U4) is then wrong); (S11-F4) the brute-force test
of (c) fails.

---
# Session-11 proofs (written after §84, the [RFL10-fix] edits and the f14 run)

## 85. Lemma GP-L (Feynman/Landau recombination at critical backgrounds): PROVEN-HERE

Statement: §84 (U1), with two clarifications logged as statement changes: (b) also assumes Z_U invertible (automatic when
Y_U > 0, e.g. at U = 1; at U_f, where H_⊥ has the Nielsen-Olesen negative mode, it is an assumption for each f); "log det" is
log|det| wherever an operator may be indefinite ((c), (d) need no extra hypothesis).
*Proof.* (a) At critical U, E_U = H(U)D_U = 0 (§79 (a)). H is symmetric, so Ran H ⊥ ker H ⊇ Ran D_U, i.e. H maps into
(Ran D_U)^⊥ = ker D_U^* and vanishes on Ran D_U. Hence, in E = ker D_U^* ⊕ Ran D_U (orthogonal), K_F = H + D_UD_U^* = H_⊥ ⊕
(D_UD_U^*)|_{Ran D_U}. Δ_U = D_U^*D_U invertible makes D_U injective, and (D_UD_U^*)·D_UΔ_U^{-2}D_U^* = D_UΔ_U^{-1}D_U^* is the
orthogonal projector onto Ran D_U, so ((D_UD_U^*)|_{Ran D_U})^{-1} = D_UΔ_U^{-2}D_U^* and K_F^{-1} = H_⊥^{-1}P_⊥ + D_UΔ_U^{-2}D_U^*.
Insert in X_U = 𝒞_n + M_UK_F^{-1}M_U^T and use M_UD_U = D_ℓι^* (gauge covariance of 𝔪_n, §77 (b)), so (M_UD_U)Δ_U^{-2}(M_UD_U)^* =
D_ℓ(ι^*Δ_U^{-2}ι)D_ℓ^* = D_ℓG2_UD_ℓ^*. Hence Y_U = X_U − D_ℓG2_UD_ℓ^* = 𝒞_n + M_UH_⊥^{-1}P_⊥M_U^T.
(b) G2_U = (Δ_U^{-1}ι)^*(Δ_U^{-1}ι) > 0 (ι injective). With X = Y + D_ℓG2D_ℓ^* (both X, Y invertible), Woodbury gives
X^{-1} = Y^{-1} − Y^{-1}D_ℓ(G2^{-1} + Z)^{-1}D_ℓ^*Y^{-1}, so D_ℓ^*X^{-1}D_ℓ = Z − Z(G2^{-1} + Z)^{-1}Z = Z(G2^{-1} + Z)^{-1}G2^{-1} =
[(1 + G2Z)Z^{-1}]^{-1} = (Z^{-1} + G2)^{-1}. Then Γ^crit_n = −log det Δ_U + ½log det(D_ℓ^*X^{-1}D_ℓ) = −log det Δ_U −
½log det(G2 + Z^{-1}).
(c) Sylvester: det X = det Y·det(1 + Y^{-1}D_ℓG2D_ℓ^*) = det Y·det(1 + G2Z), and D_ℓ^*X^{-1}D_ℓ = Z(1 + G2Z)^{-1} (the middle
expression in (b), which needs no Z^{-1}), so log det(D_ℓ^*X^{-1}D_ℓ) = log det Z − log det(1 + G2Z). Adding halves: the
log det(1 + G2Z) cancel.
(d) D_ℓ = VR, R := (D_ℓ^*D_ℓ)^{1/2}, so log det(D_ℓ^*X^{-1}D_ℓ) = log det(D_ℓ^*D_ℓ) + log det(V^*X^{-1}V). With G_gh,n =
½log det(D_ℓ^*D_ℓ) − ½log det Δ_U (§43 (iv)): Γ^crit_n − G_gh,n = −½log det Δ_U + ½log det(V^*X_U^{-1}V).
Consequence: γ_n exists (Γ^crit_n(U_f) = total_n − ½Σ_{k<n}Φ^V_k, with total_n C² in f (gapped) and each Φ^V_k C² for
|f| ≤ ε_k, REVIEW_FLOW_S10 §5.2 (ii)), and [f²]G_gh,n,α = −2c_gq_α²log ℓ exists (Proposition GH-log (c), unconditional since
§58); so γ'_n = γ_n − [f²]G_gh,n exists. ∎
*Reading.* (1) **Γ^crit_n is not a ghost-only pair.** Its level piece ½log det(D_ℓ^*X_n^{-1}D_ℓ) contains the full level-n
response X_n: by (b), the universal sampled object G2_U = ι^*Δ_U^{-2}ι (the Feynman-gauge gauge-parameter covariance at the
level sites) and the transverse response Z_U. So (GP) is the statement "γ'_n bounded", i.e. the longitudinal compression
of X_n^{-1} paired with HALF of the fine ghost (the Feynman excess over the Landau ghost). (2) By (c), at critical U every
appearance of G2 cancels between ½log det X_n and the level ghost: the critical total is the same expression with X_n
replaced by Y_n. That is the Landau split of §87.

## 86. Proposition G2-log, and the answer to (GP): G2-log PROVEN-HERE; (GP), a Feynman-split statement, expected false; irrelevant to c^tot_n (ARGUED, mechanism checked) [RFL11-fix S11-1: retitled]

Statement: §84 (U2), in a stronger form (logged): r_n converges uniformly on all of [−π, π]⁴.
*Proof.* (a) For a translation-invariant fine operator A with symbol Â, ι^*Aι has the level symbol ℓ^{-4}Σ_mÂ(k_m), k_m =
x_m/ℓ (Poisson summation; ι is the isometric injection of the level sites, no form factor). For A = Δ^{-2}, ℓ^{-4}λ(k_m)^{-2} =
λ̃(x_m)^{-2} (λ̃(x) = ℓ²λ(x/ℓ)), so g2_n(K) = Σ_mλ̃(x_m)^{-2}, and the m = 0 term is λ̃_n(K)^{-2} (K ∈ [−π, π]⁴ the representative).
(b) ḡ_n(K) = Σ_{m≠0}λ̃(x_m)^{-2}, every term with |x_m| ≥ π. Split λ(k)^{-2} = χ(k)|k|^{-4} + f_s(k), χ a smooth radial cutoff (1 on
|k| ≤ ½, 0 on |k| ≥ 1); f_s is smooth on T⁴∖{0} with |f_s(k)| ≤ C|k|^{-2}, |∂²f_s| ≤ C|k|^{-4}. (i) ℓ^{-4}Σ_{m≠0}f_s(k_m) is a
Riemann sum whose sample points are offset by K/ℓ from the cell centres (spacing 2π/ℓ, the cell of k_0 removed; **[RFL11-fix S11-4: not a midpoint sum; its O(h) term cancels because f_s is even and the removed cell is centred at 0]**) of an L¹ function with an integrable second-derivative bound
away from the cell of 0: it converges to ∫f_s dk/(2π)⁴, uniformly in K, with error ≤ Cℓ^{-2}log ℓ (the cells within distance
2π|m|/ℓ of 0 contribute ≤ ℓ^{-4}Σ_{|m|≤M}ℓ²/|x_m|² ≤ CM²ℓ^{-2}). (ii) ℓ^{-4}Σ_{m≠0}χ(k_m)|k_m|^{-4} = Σ_{m≠0}χ(x_m/ℓ)|x_m|^{-4}. Compare
each term with the average of g_ℓ(x) := χ(x/ℓ)|x|^{-4} over the cell x_m + [−π, π)⁴: the difference is ≤ C|x_m|^{-6} + Cℓ^{-2}|x_m|^{-4}
(second-order Taylor; the cell average kills the gradient term), summable over m ≠ 0 with sum → a K-dependent constant at
rate O(ℓ^{-2}log ℓ). The cell averages add up to (2π)^{-4}∫_{x ∉ C_0}g_ℓ(x)d⁴x, C_0 the cell of x_0 = K, = (2π)^{-4}[2π²(log ℓ +
c_χ) − ∫_{C_0∖B_π}|x|^{-4} + …] = (log ℓ)/(8π²) + c(K) + O(ℓ^{-2}) (2π²/(2π)⁴ = 1/(8π²)), c(K) continuous. Together:
ḡ_n(K) = (log ℓ)/(8π²) + r_n(K), r_n → r_∞ uniformly on [−π, π]⁴, |r_n − r_∞| ≤ Cℓ^{-2}log ℓ. **[RFL11-fix S11-4: for uniformity on all of [−π, π]⁴: when some |K_μ| → π a neighbouring alias cell touches x = 0, and both the second-order Taylor comparison and the complement formula for C_0 fail there. Treat the ≤ 2⁴ aliases with |x_m| < 2π separately: each such term λ̃(x_m)^{-2} is bounded and continuous in K on the set where it is kept (|x_m| ≥ π) and converges at rate O(ℓ^{-2}) (s_ℓ(x) = (x/2)(1 + O(x²/ℓ²))); apply the cell comparison to the remaining aliases, whose cells stay a fixed distance from 0. The alias set is the same for K and K − 2πe_μ, so ḡ_n is continuous on the torus and the convergence is uniform.]**
(c) At U = 1 (critical; H_⊥(1) = d^*d on ker d^*, positive fibrewise for K ≠ 0; 𝒞_n > 0), Lemma GP-L (a) gives the level symbol
x_n = y_n + D̂_ℓg2_nD̂_ℓ^† with y_n ≥ 0, for EVERY block map with M_UD_U = D_ℓι^*. So ⟨D̂_ℓ, x_nD̂_ℓ⟩ ≥ |D̂_ℓ|⁴g2_n ≥ |D̂_ℓ|⁴[(log ℓ)/(8π²)
+ r_n], which is unbounded in n at every K ≠ 0. ∎
*Reading.* (1) **(VC-V) as formulated in §80 / REVIEW_FLOW_S10 §6 (n-uniform level-unit vertex data of the Feynman X_n) is
FALSE at U = 1, at zeroth order, for every gauge-covariant block map.** The cause is the fine Feynman-gauge longitudinal
mode: its gauge parameter has covariance Δ^{-2}, which is log-correlated in 4D, and covariance forces its level-site samples
into X_n. This is a NARROW negative: it concerns the Feynman form of the X-telescoping only; the Landau form (§87) contains no
G2. (2) f14 B1: (ḡ_n − ḡ_{n−1})/(log L/(8π²)) = 0.99992, 0.99999, 1.00000, 1.00000 (n = 4..7, K_a) and 1.00091, 1.00010, 1.00001,
1.00000 (K_b); ḡ_7(K_a) = 0.10763. f14 B2: the inequality holds with margin ≥ 29% for the straight-path map.

**(GP), a Feynman-split statement, expected false; irrelevant to c^tot_n: the mechanism (ARGUED; not counted).** [RFL11-fix S11-1: retitled; see the tagged paragraph at the end of this section] By §85 (b), Γ^crit_n = P_n + Q_n with
P_n := −log det Δ_U − ½log det G2_U (= −½log det(Δ_U²|_{Λ'}) by Jacobi) and Q_n := −½log det(1 + G2_U^{-1}Z_U^{-1}). In level units
G2 ≈ λ̃^{-2} + ḡ_n with ḡ_n ≈ (log ℓ)/(8π²) at every K ≠ 0. Heuristic: log G2 = −2log λ̃ + log(1 + ḡλ̃²) and log(1 + ḡλ̃²) = log ḡ +
log(λ̃ + i ḡ^{-1/2}) + log(λ̃ − i ḡ^{-1/2}), two "massive" pieces with |mass²| = ḡ^{-1/2}, each of which has polarisation
c_g log(1/|mass²|) + O(1) = (c_g/2)log ḡ + O(1) per unit charge in the x-normalisation (massless: x = 2c_g log(1/p) =
c_g log(1/p²)); so the level polarisation y_n of log det G2 carries c_g log ḡ_n, and [f²]P_n + 2c_gq_α²log ℓ = −½c_gq_α²log ḡ_n + O(1) ≈ −½c_gq_α²log log ℓ + O(1).
Q_n is suppressed where ḡλ̃² ≫ 1 (G2^{-1} ≤ ḡ^{-1}), so it is not expected to cancel this. Hence **γ'_n is expected to grow
like −½c_gq_α²log log ℓ = −½c_gq_α²log n + O(1): (GP) as stated is expected to FAIL.** (It is compensated in c^tot_n by the
Feynman steps, ½Σ_{k<n}[f²]Φ^V_k ≈ … + ½c_gq_α²log n, i.e. the Feynman step coefficients converge like 1/k, not geometrically —
the same G2 enters X_k for every k.) **Check (f14 C, pre-stated; scalar model of the mechanism, plane-wave reading at
U = 1):** the brute-force torus confirms the level formula (C1: 8.4e-8, 1.1e-8); D_n(P) = y_n(P) − y_{n−1}(P) = 2.796e-4,
2.447e-4, 2.014e-4, 1.696e-4 (P = π/4, n = 3..6; P = π/2 the same to 1%), ratios 0.875, 0.823, 0.842 — NOT geometric (L^{-2} = 0.111),
step control ≤ 7.5e-6; and, as a post-run comparison not in the criteria, D_n/(c_g·log(ḡ_n/ḡ_{n−1})) at K_a = 0.977, 0.996,
0.9995 (n = 4, 5, 6) **[RFL11-fix S11-5: this agreement is specific to K_a; the same post-run ratio at K_b is 1.019, 1.031, 1.029 (REVIEW_FLOW_S11 §3.3). The K-free form (1/D_n − 1/D_{n−1})·c_g = 0.538, 0.927, 0.984 (n = 4, 5, 6; reviewer arithmetic on printed f14 numbers, 1/c_g = 96π²) → 1 supports D_n ≈ c_g/(n + n_0), i.e. y_n = c_g log n + const + o(1) with coefficient c_g at the few-% level; post-run, not in the criteria]** This tests the mechanism
for P_n in the plane-wave reading; γ'_n itself (constant field, with Q_n and the vector Z) is not computed.
**Lemma DEF-red (remark, PROVEN given F-id for each piece, not counted).** If the plane-wave and constant-field readings
agree for total_n (MS (iv) with F-id-exp, given (L-loc2)) and for each gapped step Φ^V_k (F-id-exp; exponentially decaying
Hessians from the gapped H^V_k, per k), then 𝔡_{n,α} = c^pw[Δ_def] = c^pw[Γ^crit_n] − γ_n: the defect is exactly the failure of
the exchange for the single massless object Γ^crit_n. (Proof: c^pw[total] = ½Σc^pw[Φ^V_k] + c^pw[Γ^crit] + c^pw[Δ_def] and
c^cf[total] = ½Σc^cf[Φ^V_k] + γ_n, since Δ_def(U_f) = 0.)
**[RFL11-fix S11-1] The log log ℓ is NOT in c^tot_n.** Exactly (GP-L (b), (c), L-tel, §87 Reading (3)), with 𝒦_n := [f²]½log det(1 + G2_UZ_U)(U_f): ½Σ_{k<n}(φ^V_k − φ^L_k) = +𝒦_n + [f²]½log det Δ_U and γ_n − γ^L_n = −𝒦_n − [f²]½log det Δ_U, so c^tot_n = ½Σφ^V_k + γ_n = ½Σφ^L_k + γ^L_n at each n. The G2 log-correlation (the object whose level polarisation drifts like c_g log ḡ_n) enters the Feynman steps as +𝒦_n and the Feynman remainder γ_n as −𝒦_n, and cancels identically. The total also has the manifestly G2-free form G_⊥,n + G_gh,n (l.839), and (forward reference, written 10:44-10:47 UTC before the session-12 proofs: see §96, Lemma T-tel [RFL12-fix S12-8]) the form ½Σφ^T_k − 2c_gq_α²log ℓ. It is NOT a contribution to β and does not threaten the standard one-loop running. The heat-kernel universality results (V-heat 11/3; ghost 1/22 + transverse 21/22) fix only the coefficient of log ℓ; they neither produce nor exclude a log log ℓ. The absence of every other non-standard term in c^tot_n is the content of the remaining vector (V-IR) items (§90, and session 12's revision).

## 87. Lemma L-tel (Landau telescoping): PROVEN-HERE

Statement: §84 (U3).
*Proof.* Write ι_{(k)} for the injection of the level-k sites into Λ, D^{(k)} := D_ℓ^{(k)} (D^{(0)} := D_U), G2^{(k)} := ι_{(k)}^*Δ_U^{-2}ι_{(k)}
(G2^{(0)} := Δ_U^{-2}), X^{(k)} as in V-tel (X^{(0)} = K_F^{-1}), Y^{(k)} := X^{(k)} − D^{(k)}G2^{(k)}D^{(k)*}. Since ι_{(k+1)} = ι_{(k)}ι_k,
ι_k^*G2^{(k)}ι_k = G2^{(k+1)}; with the one-step covariance T_kD^{(k)} = D^{(k+1)}ι_k^* (the argument of §77 (b) for the one-step map at
the level-k field 𝔪_k(U); k = 0 is §77 (b) itself), T_kD^{(k)}G2^{(k)}D^{(k)*}T_k^T = D^{(k+1)}G2^{(k+1)}D^{(k+1)*}. Subtracting it from
X^{(k+1)} = T_kX^{(k)}T_k^T + κ^{-1}Π_{k+1}^{-1} gives Y^{(k+1)} = T_kY^{(k)}T_k^T + κ^{-1}Π_{k+1}^{-1}; at k = n, Y^{(n)} = Y_U. Every U, no
criticality. At critical U: by (T4)'s critical form and Lemma GP-L (c), total_n = ½log det K_F − log det Δ_U + ½log det Y_n +
½log det(D_ℓ^*Y_n^{-1}D_ℓ); telescoping log det Y_n = log det Y^{(1)} + Σ_{1≤k<n}(log det Y^{(k+1)} − log det Y^{(k)}) gives
total_n = ½Σ_{k<n}Φ^L_k + Γ^L_n, and Γ^L_n = G_gh,n + ½log det W_U as in §85 (d). The form of Φ^L_0: at critical U,
log det K_F = log det_⊥H_⊥ + log det Δ_U (§85 (a); D_UD_U^* on Ran D_U is unitarily equivalent to Δ_U), and Y^{(0)} = H_⊥^{-1}P_⊥, so by
Sylvester det Y^{(1)} = det(κΠ_1)^{-1}det(1 + κH_⊥^{-1}P_⊥T_0^TΠ_1T_0); the last operator is block upper-triangular in
ker D_U^* ⊕ Ran D_U with diagonal blocks 1 + κH_⊥^{-1}P_⊥T_0^TΠ_1T_0P_⊥ and 1, so det Y^{(1)} = det_⊥(H_⊥ + κP_⊥T_0^TΠ_1T_0P_⊥)/
(det_⊥H_⊥·det κΠ_1), and Φ^L_0 = log det_⊥(P_⊥(K_F + κT_0^TΠ_1T_0)P_⊥) − log det(κΠ_1) (D_UD_U^* vanishes on ker D_U^*). At U = 1,
K_F(1) = d^*d + dd^* is the componentwise lattice Laplacian, symbol λ·1, and D̂D̂^† = λP_L, so Y^{(0)} = λ^{-1} − λ^{-2}D̂D̂^† = P_T/λ;
in Y_n(1) = 𝒞_n + Σ_mM_mP_T(k_m)M_m^†/λ(k_m) (fibre normalisation of §65) the covariance-forced component of M_m (the one
along D̂(k_m), fixed by M_mD̂(k_m) = D̂_ℓ(K)) is annihilated by P_T(k_m). ∎
*Reading.* (1) The Landau split moves the G2 log-correlation out of every term: the steps Φ^L_k are built from Y^{(k)}, whose
alias sums carry no forced 1/|x| longitudinal part, and the remainder Γ^L_n = G_gh,n + ½log det W_n consists of the exactly
solved ghost group and one level object W_n = V^*Y_n^{-1}V. (2) At U_f, Y^{(0)} = H_⊥^{-1}P_⊥ has the Nielsen-Olesen eigenvalue
≈ −1/(q_α f); as for X (REVIEW_FLOW_S10 §5.2), the Landau steps must then be used in the Woodbury form Φ^L_k = log det(Y_k^{-1} +
κT_k^TΠ_{k+1}T_k) − log det(κΠ_{k+1}) (k ≥ 1), with Y_k^{-1} continuous in f, and Φ^L_0 in the compressed form above.
(3) Φ^L_0 − Φ^V_0 = log det(D_U^*(H^V_0)^{-1}D_U) − log det Δ_U (Jacobi for the compression to ker D_U^*), a fine-scale,
IR-safe pair (H^V_0(0) is cubic-invariant on constant 1-forms), so the Landau and Feynman first steps differ by an
ℓ-independent fine object. Summed: ½Σ_{k<n}Φ^V_k = ½log det K_F + ½log det X_n (V-tel) and ½Σ_{k<n}Φ^L_k = ½log det K_F −
½log det Δ_U + ½log det Y_n, so ½Σ_{k<n}(Φ^V_k − Φ^L_k) = ½log det X_n − ½log det Y_n + ½log det Δ_U = ½log det(1 + G2_UZ_U) +
½log det Δ_U (§85 (c)), a level object containing G2: this is where the log log ℓ of §86 sits.

## 88. Corollary VFINE-gh and Lemma FINE-IR-gen: PROVEN-HERE; (VFINE-K) given (CL-V)

*Corollary VFINE-gh (§84 (U5)).* At the Cartan background U_{x,1} = exp(εcos(px_2 + ϑ)H_1), Ad(U_b^{-1}) acts on the root
component λ_α by e^{−iq_αa_b} ([H_1, E_α] = iq_αE_α), so Δ_U restricted to root sector α is the U(1) covariant Laplacian of §74
with a → q_αa (orientation conventions do not affect even orders). Hence [ε²] = q_α²·(p²/2)x_0(p): log coefficient 2c_gq_α²,
finite part q_α²a_0 (Lemma FINE-IR). ∎
*Lemma FINE-IR-gen (§84 (U6)), with two hypotheses made explicit (logged as statement changes):* (G1′) the lattice ε²
integrand f(k, p) (below) obeys f(−k, −p) = f(k, p); (G4) the family is invariant under the reflection x_2 ↦ −x_2 (which maps the
plane wave (p, ϑ) to (−p, −ϑ)), so the ϑ-free density is even in p. (Both hold for Δ_U, §74, and are standard lattice
symmetries of the Wilson Hessian at Cartan plane waves; they are not checked here for K_F.) **[RFL11-fix S11-3: both are AUTOMATIC, so they are not hypotheses. (G4): the plane wave εcos(px_2 + ϑ) with (p, ϑ) is the same field as with (−p, −ϑ), so f(k, −p) = f(k, p) pointwise (under p → −p the ± bubble terms swap, V_+^{(−p)} = V_−^{(p)} as momentum-transfer parts, and the explicit p-factors of the spin vertex transform consistently). (G1′): complex conjugation maps the root-α operator at background a to the root-(−α) operator, i.e. charge −q_α, equivalently ε → −ε, and maps k ↦ −k; f is the ε² coefficient, hence even in ε, and f is real pointwise (tr(O_0^{-1}Ô_2) is a trace of a product of two hermitian matrices, and the bubble is tr(AV_+^†BV_+) with A, B > 0); hence f(−k, p) = f(k, p), and with (G4) f(−k, −p) = f(k, p). This holds for Δ_U and for K_F = H + DD^* (the Wilson action and DD^* are C-covariant; E_α^† = E_{−α}). FINE-IR-gen therefore holds under (G1)-(G3) alone.]**
*Proof.* As in §65 (b), the ϑ-free ε² density is ∫dk/(2π)⁴f(k, p), f = tr(O_0^{-1}Ô_2) − ¼Σ_±tr(O_0(k)^{-1}V_∓(k)O_0(k ± pe_2)^{-1}V_±(k)),
Ô_2 the ϑ-free part of O_2 and V_± the two momentum-transfer parts of O_1 (±2p parts vanish for 0 < |p| < π). By (G1), (G3)
(O_0^{-1} ≲ |k|^{-2}, |V_±| ≲ |k| + |p|, |Ô_2| ≲ 1 near the singular points) f(·, p) ∈ L¹ with singularities ≲ |k|^{-2}, |k ± pe_2|^{-2}.
By (G2), x^O(p) = (2/p²)∫[f(k, p) − f(k, 0)]dk. (i) On T⁴∖B (B := {|k| ≤ 1}), O_0 ≥ c > 0, f is smooth in (k, p) for |p| ≤ ½ and even in p
(G4): ∫_{T⁴∖B}[f(k, p) − f(k, 0)] = O(p²). (ii) On B write f = f_c + (f − f_c), f_c the integrand of O^c (homogeneous of degree −2
jointly in (k, p)). By (G1), (G1′) and analyticity, the lattice corrections to the symbols are of relative order r² (r := |(k, p)|;
joint parity removes the relative order r), so f − f_c obeys the bounds of §74 (3) (ii) with one power of r to spare:
|f − f_c| ≲ r^{-2}·r²·(singular factors) and |∂_p²(f − f_c)| ≲ |k|^{-2} on 2|p| ≤ |k| ≤ 1; the region |k| ≤ 2|p| contributes O(p²) by
scaling (separated integrable singularities). So ∫_B[(f − f_c)(k, p) − (f − f_c)(k, 0)] = O(p²log(1/p)). (iii) ∫_B[f_c(k, p) − f_c(k, 0)]dk
= p²∫_{|q|≤1/|p|}[f_c(q, e_2) − f_c(q, 0)]d⁴q (k = |p|q, homogeneity; sign of p by (G4)). For |q| ≥ 1, f_c(q, e_2) − f_c(q, 0) =
c_1(q̂)|q|^{-3} + h(q̂)|q|^{-4} + c_3(q̂)|q|^{-5} + O(|q|^{-6}) **[RFL11-fix S11-6: the first-order term c_1(q̂)|q|^{-3} was omitted; c_1 is odd (joint parity gives ∂_pf_c(−q, 0) = −∂_pf_c(q, 0)), so ∫_{S³}c_1 = 0; pointwise it is the largest term; with it the conclusion x^O = 2C_O log(1/p) + a^O + o(1) stands]**, and ∫_{S³}c_3 = 0 (joint parity makes c_3(−q̂) = −c_3(q̂) at e_2 → −e_2, and (G4)
identifies the two). Hence (2π)^{-4}∫_{|q|≤1/|p|}[…] = C_O·log(1/p) + const + O(p), C_O := (2π)^{-4}∫_{S³}h, and x^O(p) = 2C_O log(1/p) +
a^O + O(p²log(1/p)) with a^O a sum of absolutely convergent integrals (as in §74 (3)). ∎
*(VFINE-K).* **[RFL11-fix S11-3: superseded by the tagged paragraph below; (G1′), (G4) are automatic]** Given (CL-V) and (G1′), (G4) for the root-sector symbols of K_F(U) at the Cartan plane wave, FINE-IR-gen gives
x^{K_F}(p) = 2C_{K_F}log(1/p) + a^{K_F} + o(1): the existence of the log coefficient and of the finite part is PROVEN given those
hypotheses. The VALUE C_{K_F} = −20q_α²c_g is the continuum angular integral of O^c = −D²δ_{μν} + 2iq_αF_{μν}; here it is
identified with the heat-trace ratio R_V/R_S = (10/3)/(−1/6) (§44 Reading (1); the B²t² coefficient of tr e^{−t(−D²δ + 2iF)} is
4·(−1/6) + 4 = 10/3) — ARGUED (the equality of the plane-wave angular coefficient and the constant-field heat-trace coefficient
for the continuum operator is the standard regulator-independence of the one-loop log; not re-derived here). (CL-V) itself
(the classical continuum limit of the lattice Wilson Hessian in the root sector, including its spin vertex) is OPEN as a
written statement (the explicit second-order plane-wave vertices of H(U) are not written anywhere yet).
**[RFL11-fix S11-3] The value of C_{K_F}, derived (replaces "ARGUED").** Continuum operator O^c = (−i∂ − qa)²δ_{μν} + 2iqF_{μν}, a = εcos(px_2)e_1, with the same tr log convention for the scalar and the vector (only the ratio matters). (1) Orbital and diamagnetic: the orbital part of O^c is diagonal in μν, so it gives exactly 4 × the scalar result, 4c_g. (2) Orbital × spin cross terms: the orbital vertex is ∝ δ_{μν} and the spin vertex ∝ A := E_{21} − E_{12}, with tr A = 0; they vanish. (3) Spin × spin: F is linear in a for an abelian background, so there is no second-order spin vertex; the e^{±ipx_2} parts of 2iqF are ∓εpA (hermitian partners), and tr(−A²) = 2; the spin ε² density is −p²Σ_±∫d⁴k/(2π)⁴[k²|k ± pe_2|²]^{-1}, whose log(1/p) coefficient is −p²·2/(8π²); so x_spin = −(1/(2π²))log(1/p), C_spin = −1/(4π²) = −24c_g (c_g = 1/(96π²)). Total: C_{K_F} = 4c_g − 24c_g = −20c_g, in agreement with the heat-trace ratio (10/3)/(−1/6) (whose arithmetic 4·(−1/6) + 4 = 10/3 is also right). Cross-checks: ½(−20) − 1 = −11 (the Feynman-form 11/3); ½(−20) − ½ = −21/2 and −½ (the 21/22 + 1/22 split of GH-log). Hence (VFINE-K) is PROVEN given (CL-V) alone, value included, and so is (VFINE-L) = (VFINE-K) − ½(VFINE-gh). (CL-V) is the session-12 target (W2).

## 89. (VC-L): OPEN; Proposition SP-div: PROVEN-HERE

*Proposition SP-div (§84 (U7)).* Straight-path map, U = 1: (M a)_{X,μ} = Σ_{j<ℓ}a_{ℓX+je_μ, μ}, row S_μ(k_m) with Poisson factor ℓ^{-4} **[RFL11-fix S11-2: was "fibre row ℓ^{-2}S_μ"]**, S_μ(k) =
Σ_{j<ℓ}e^{ik_μj}, diagonal in μ. Then the 11-symbol of Y_n(1) at fixed K with K_1 ≠ 0 is ≍ ℓ. *Proof.* Y_n = 𝒞_n + Σ_mℓ^{-4}S(k_m)P_T(k_m)S(k_m)^†/λ(k_m)
≥ 0 termwise. Lower bound: keep the aliases with m_1 = 0 and 1 ≤ |m_⊥| ≤ ℓ/4: there |S_1(k_m)|² = sin²(K_1/2)/sin²(K_1/2ℓ) ≥ cℓ²,
(P_T)_{11}(k_m) = 1 − 4sin²(K_1/2ℓ)/λ(k_m) ≥ ½ (since λ(k_m) ≥ c|m_⊥|²/ℓ² ≫ K_1²/ℓ²), λ(k_m) ≤ C|m_⊥|²/ℓ², so the sum is ≥
cΣ_{1≤|m_⊥|≤ℓ/4}|m_⊥|^{-2} ≥ c'ℓ (a 3D sum). Upper bound: |S_1|² ≤ min(ℓ², C/sin²(k_1/2)) and Σ_mℓ^{-4}|S_1|²/λ ≤ Cℓ by the same
count. ∎ f14 B3 **[RFL11-fix S11-2: f14 B2/B3 (criteria) measured the 11-symbol of the FEYNMAN X_n (x_{n,μμ} = ℓ^{-4}Σ_m|S_μ|²/λ, no P_T), while (U7) states Y_n; this deviation from the pre-statement was not logged in session 11. The reviewer's Y_11 (straight path, K_a) gives ρ_n/L = 0.838, 0.945, 0.983, 0.995, 0.998, 0.9996 (n = 2..7): the pre-stated (U7) prediction (within 10% of L at n ≥ 3) HOLDS for the pre-stated object Y; the X numbers and the FAIL line below stay as recorded]**: x_{n,11}(K_a) = 7.79, 21.4, 62.4, 185.2 (n = 3..6), ratios ρ_n = 2.392, 2.750, 2.910, 2.970 → L; **the pre-stated
10% prediction FAILS at n = 3 (ρ_3/L = 0.797) and holds at n = 4, 5, 6** (the approach is ρ_n ≈ L(1 − A/(Bℓ)); X − Y = |D̂_ℓ1|²g2 grows
only like log ℓ, so Y has the same linear growth). So the f13 map is not admissible for any level-unit vertex convergence:
(VC-V) and (VC-L) both need a map with transverse averaging (S4'/W_♮). **[RFL11-fix S11-7: our S4' map DOES average transversely: its U = 1 linearisation is Q_root = Q_str − d∘h, and Q_str has the product symbol S_μ(k_μ)Π_αD_ℓ(k_α) of 1D Dirichlet factors in all four directions (l.280, 737-739); no new map is needed. The admissible-map requirement reduces to the d∘h term of Q_root and the Lemma A-type product decay of the tensor form factors of T_k, Π_k. Session 12 (forward reference, written before those proofs: see §96, §98 [RFL12-fix S12-8]) shows that d∘h drops out of the level-transverse split exactly.]**
*(VC-L): OPEN.* What it needs, in order: (1) the vector form factors of the S4'/W_♮ map (1-form averages with transverse
decay); by L-tel the covariance-forced component is killed by P_T, so the remaining question is whether the transverse
components obey the product decay of §76 Lemma A; (2) the λ̃²-normalisation of the m = 0 alias (Y's m = 0 term is
(analytic)/λ̃² because of P_T = 1 − D̂D̂^†/λ), i.e. the scalar polydisc argument with one more pole order; (3) the Landau vector
IR-id: link the level polarisation of ½log det Y_n to the fine Landau transverse polarisation ½log det_⊥H through
det(H_⊥ + M^T𝒞^{-1}M)|_⊥ = det_⊥H_⊥·det𝒞^{-1}·det Y (critical U), the analogue of §75 (b); (4) the n-independence of the leading
(degree-4) numerator (charge normalisation: A_0(0) = 1 on constant 1-forms). (GP-L) (sup_n|w_n| < ∞) would follow from (VC-L)
applied to W_n, modulo the non-analyticity of V at K = 0 (use log det W_n = log det(D_ℓ^*Y_n^{-1}D_ℓ) − log det(D_ℓ^*D_ℓ), the last
exact by GH-log). **[RFL11-fix S11-7: (GP-L) is therefore not an independent item: (VC-L) stated for D_ℓ^*Y_n^{-1}D_ℓ contains it. Session 12 (Proposition LONG-n) shows that (VC-L) for Y_n, hence W_n, is false at zeroth order for every covariant map, and Lemma T-tel removes W_n from the split altogether.]**

## 90. Target (U8) (vector (UIR)): OPEN, re-reduced in the Landau split

At U_f (critical), by L-tel: c^tot_n = ½Σ_{k<n}φ^L_k + γ^L_n, φ^L_k := [f²]Φ^L_k(U_f) (Woodbury forms), γ^L_n = −2c_gq_α²log ℓ + w_n
(GH-log (c)). By the scalar template, the vector (UIR)/(V-IR) in the form (Q1)(d) would follow from:
- **(VFINE-L)** the fine Landau transverse polarisation of ½log det_⊥H = ½log det K_F − ½log det Δ_U: = (VFINE-K) − ½(VFINE-gh);
  PROVEN given (CL-V), (G1′), (G4) for the existence of the log and the finite part (§88); value ARGUED; **[RFL11-fix S11-3: (G1′), (G4) automatic; value derived (§88 tagged paragraph): PROVEN given (CL-V) alone, value included]**
- **(VC-L)** (§89) for the steps Φ^L_k and for W_n, with an admissible map and the Landau vector IR-id: OPEN;
- **(GP-L)** sup_n|w_n| < ∞: OPEN (follows from (VC-L) up to the V-non-analyticity); **[RFL11-fix S11-7: not a separate item; part of (VC-L) stated for D_ℓ^*Y_n^{-1}D_ℓ]**
- exchange (plane wave ↔ constant field) for the Landau pieces at U_f, with the Nielsen-Olesen mode handled by the Woodbury
  forms: OPEN **[RFL11-fix S11-7: including the plane-wave form factor of 𝔪_n (W_♮) (REVIEW_FLOW_S10 §11 item 3), which had dropped off this list]**; and (L-loc2).
(GP) and (VC-V) of REVIEW_FLOW_S10 are NOT on this list: in the Feynman split, (VC-V) is false at U = 1 (§86) and (GP) is
expected to fail by a log log ℓ that the Feynman steps compensate (§86, ARGUED, model-checked) **[RFL11-fix S11-1: the log log ℓ cancels exactly in c^tot_n (§86 tagged paragraph); it is not a contribution to β]**. So **Theorem UNIV for SU(N)
does NOT yet rest only on (L-loc2)**: it rests on (L-loc2), (CL-V) (+ (G1′), (G4)) for (VFINE-K), (VC-L) with an admissible
(transversely averaging) map, (GP-L), and the Landau exchange statements. **[RFL11-fix S11-3, S11-7: (G1′), (G4) drop (automatic); (GP-L) is part of (VC-L); our S4' qualifies at the Q_str level (the open part is its d∘h term and the product decay of T_k, Π_k); the exchange item includes the plane-wave form factor of 𝔪_n. Minimal list after REVIEW_FLOW_S11: (L-loc2); (CL-V); (VC-L) (Landau steps + D_ℓ^*Y^{-1}D_ℓ, for Q_root including d∘h, with the Landau vector IR-id); the Landau plane-wave/constant-field exchange at U_f (with the 𝔪_n form factor and the Nielsen-Olesen mode). Session 12 revises this list again (the level-transverse split).]**

## 91. Session-11 check f14 (ADDED AFTER the run; checks/f14_criteria.md, f14_gp_vlong.py, f14_out.txt, f14_time.txt)
Criteria written 10:01:43 UTC before any f14 script (stat in FLOW_LOG); the script (birth 10:04:46, mtime 10:05:00 UTC, md5
668777da…) was not changed after its smoke run (cmp-identical copy). Official run: one NUMERIC LOCK acquisition, 10:05:39-10:05:53
UTC, nice 10, 1 thread, load 2.53, memory free 39% (checked inside the lock before starting); 13.8 s, peak RSS 650 MB.
**35/37 verdict lines PASS; 2 FAIL (B3 n = 3; X0).**
- **Part A (b_n, w_n, S10-4): ALL PASS.** A1 the finite-torus identity with b_n, w_n, γ_n implemented from the TEXT of §75 against
  f12's T_n − I_n: rel 3.9e-16 … 7.1e-14 (n = 1..4, j = 1, 2; threshold 1e-10); A2 Ward identities b_n(K; 0) = ∂_1γ_n ≤ 8.0e-11 and
  w_n(K; 0) = ∂_1²γ_n ≤ 2.2e-8 (n = 1, 2, 3; threshold 1e-7); A3 control (sign of d'ũ^-/λ̃' flipped): rel 0.41 (fails, as required).
  **The explicit §75 formulas for b_n and w_n are confirmed, including the K − P intermediate fibre and the Ward
  normalisations ũ(P = 0) = ∂d, m̃ = ∂²d.**
- **Part B: B1 ALL PASS** (slope log L/(8π²) to ≤ 9.1e-4 at n = 4 and ≤ 1e-6 at n = 7; step control 8.3e-11); **B2 PASS** (margin
  ≥ 0.29); **B3: n = 3 FAIL** (ρ_3/L = 0.797), n = 4, 5, 6 PASS (0.917, 0.970, 0.990): the linear growth holds, the pre-stated
  onset was too early. **[RFL11-fix S11-2: B2/B3 measured the Feynman X_n, the criteria deviating (unlogged) from (U7)'s Y_n; on Y_n (reviewer) ρ_n/L = 0.945, 0.983, 0.995, 0.998 (n = 3..6): the pre-stated prediction holds for the pre-stated object. The FAIL line stays as recorded.]**
- **Part C: C1 PASS** (8.4e-8, 1.1e-8); **C2 step control PASS** (≤ 7.5e-6); **classification "slow" PASS** (r_6 = 0.842, 0.841;
  r_5 = 0.823, 0.821; geometric: no). **X0 FAIL** (2.5e-9 against 1e-12): a post-run diagnosis (scratchpad flow11/diag_x0.py,
  under the lock) locates the maximum relative difference at a kernel value 1.4e-303 (T = 3.6e7, e^{−T·min(A, B)} at the edge of
  the double range), where both implementations lose relative precision; the threshold was mis-specified for underflowing
  entries, which contribute nothing to any sum. C1's brute-force agreement (8e-8, limited by the finite differences) tests the
  extended kernels independently.
- **Reading.** (1) S10-4 is discharged: b_n, w_n are now numerically tested (S11-F1 does not occur). (2) Proposition G2-log's
  constant is confirmed (S11-F2 does not occur). (3) The mechanism behind (U4) is confirmed in the scalar model: the level
  polarisation of log det G2 drifts like c_g log ḡ_n ≈ c_g log log ℓ (S11-F3, S11-F4 do not occur) **[RFL11-fix S11-5: the 0.05% agreement is at K_a only (K_b: 1.019, 1.031, 1.029); the K-free (1/D_n − 1/D_{n−1})·c_g = 0.538, 0.927, 0.984 → 1. S11-1: the drift cancels exactly in c^tot_n]**. (4) SP-div holds
  asymptotically.

## 92. Session-11 outcomes against §84 (ADDED AFTER the derivations and the check)
- **Step 1 (fixes): DONE.** S10-1..S10-6 applied in place, tagged [RFL10-fix] (13 tag occurrences at the fix sites, l.3518-3926, in §73 (T7),
  §75, §76, §77, §79 (a)-(c), §80, §81, §82, §83; further mentions only in §84, the session-11 heading and here): the ε² defect term Ê_2 and the 𝔮_0 term; (DEF)
  retired for (GP)/(DEF-F); X_U ≥ 𝒞 fails at U_f; the per-j bound and the half-radius polydisc; b_n, w_n disclosure; C1, C2, C6
  are linear algebra; (VC-V)/(GP) restated.
- **(U1) Lemma GP-L: PROVEN** (§85; Z invertible added for (b)). Γ^crit_n is not a ghost-only pair.
- **(U2) Proposition G2-log: PROVEN** (§86, stronger: uniform on [−π, π]⁴). **(VC-V) as formulated is FALSE at U = 1** (narrow:
  Feynman form only). f14 B1 confirms the slope.
- **(U3) Lemma L-tel: PROVEN** (§87).
- **(U4) (GP): answered by a mechanism, not a proof:** (GP) is expected to FAIL by −½c_gq_α²log log ℓ (ARGUED; the mechanism is
  confirmed quantitatively in the scalar model by f14 C) **[RFL11-fix S11-1: a Feynman-split statement; the log log ℓ cancels exactly in c^tot_n and is not a contribution to β]**. (GP-L): OPEN. (DEF-F) reduced to the exchange for Γ^crit_n (remark).
- **(U5) VFINE-gh: PROVEN. (U6) FINE-IR-gen: PROVEN** under (G1)-(G4) ((G1′), (G4) added); **(VFINE-K): PROVEN given (CL-V), (G1′),
  (G4)** for existence; value −20q_α²c_g ARGUED **[RFL11-fix S11-3: (G1′), (G4) automatic; value derived: PROVEN given (CL-V) alone, value included]**.
- **(U7) SP-div: PROVEN** (f14 B3 prediction fails at n = 3 only). **(VC-L): OPEN**, needs listed (§89).
- **(U8): OPEN**, re-reduced (§90). Theorem UNIV for SU(N) does NOT yet rest only on (L-loc2).
- **Step 4 (f14): DONE**, 35/37 (two FAIL lines reported as such).

## 93. Tally after session 11 (FLOW.md items; session-11 items unreviewed)
- **PROVEN-HERE: 59 (through session 10, as confirmed by REVIEW_FLOW_S10; 57 under its stricter convention) + 6 (session 11)
  = 65.** Session 11: Lemma GP-L; Proposition G2-log; Lemma L-tel; Corollary VFINE-gh; Lemma FINE-IR-gen (under (G1)-(G4));
  Proposition SP-div. Upstream inputs used: §77 (b) covariance (and its one-step version), (T4) critical form, V-tel, §43 (iv),
  GH-log (c), FINE-IR, §65 (b) fibre conventions.
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT (§58). No new import.
- **ARGUED, not counted:** (L-loc2); the (GP) failure mechanism (−½c_gq_α²log log ℓ; model-checked by f14 C); the value
  C_{K_F} = −20q_α²c_g **[RFL11-fix S11-3: now derived, given (CL-V); S11-1: the log log ℓ cancels exactly in c^tot_n]**; Lemma DEF-red (a remark under F-id hypotheses).
- **OPEN:** (V-IR) on G_⊥ in the form (Q1)(d) [s-P] (crux), now reduced in the Landau split to (CL-V) (+ (G1′), (G4) **[RFL11-fix S11-3: automatic, dropped]**) [s], (VC-L)
  with an admissible map [s], (GP-L) [s], the Landau exchange statements at U_f [s] (§90); (L-loc2) [s]; (s1), (s2⊥) [s-P] (rate
  only); the rate of c'(φ) → c'_0 [s]; (COV-GI) at non-critical backgrounds [s]; FI-1 [cross-lane]; HIST's restatement of CL^J's
  Setting [cross-lane]. Retired: (DEF) (→ (GP)/(DEF-F), §79 (c)); (VC-V) in the Feynman form (false at U = 1, §86); (GP) as a
  target (expected false, §86).
- **Checks:** f14 (A1 ×8, A2 ×6, A3, B1 ×9, B2, B3 ×3, C1 ×2, C2 ×5 PASS; B3 n = 3 and X0 FAIL).

## 94. Session-12 targets and PRE-STATED (session 12) statements (written 2026-10-28 ~10:45 UTC, the first edit of session 12: before the [RFL11-fix] edits and before any session-12 proof, criteria file or script)

Binding input: REVIEW_FLOW_S11.md (fixes S11-1..S11-8, applied after this section, in place, tagged **[RFL11-fix]**; the
log log ℓ drift is a Feynman-split bookkeeping effect that cancels exactly in c^tot_n; (G1′), (G4) automatic; the value of
C_{K_F} derivable; S4' averages transversely at the Q_str level; the d∘h part of Q_root unchecked). Notation of §84-§89. At
level k, D^{(k)} := D_ℓ^{(k)} (D^{(0)} := D_U), P_k := the orthogonal projector onto ker D^{(k)*} (P_0 = P_⊥), log det_⊥ := log|det| on
the range of the projector named; Ỹ^{(k)} := P_kY^{(k)}P_k on ker D^{(k)*}, Ỹ_U := P_nY_UP_n. At U = 1 (level units of §75, one
colour, Π_j = 1): K a level momentum, x_m = K + 2πm, k_m = x_m/ℓ, ŝ(k)_μ := e^{ik_μ} − 1, λ = |ŝ|², D̂_ℓ(K)_μ := e^{iK_μ} − 1,
V := D̂_ℓ/|D̂_ℓ|, P_{T,ℓ}(K) := 1 − VV^†, D_r(θ) := r^{-1}Σ_{|s|≤(r−1)/2}e^{iθs}, S_μ^{(r)}(θ) := Σ_{j<r}e^{iθj}; the level symbol of a fine
operator A through a map M is ℓ^{-4}Σ_mM̂(k_m)Â(k_m)M̂(k_m)^†.

**PRE-STATED (session 12).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Each hypothesis is named; nothing below uses an ARGUED or OPEN item as if proven. Any later change
of a statement is logged as such.

**(W1) Step 1.** S11-1..S11-8 applied; the minimal UNIV list written (no (G1′), (G4); (GP-L) not a separate item; the plane-wave
form factor of 𝔪_n listed under the exchange item).
**(W2) Lemma CL-V (the root-sector Wilson Hessian at Cartan backgrounds and its classical continuum limit).** Let U_b =
exp(a_bH_1) (abelian, H_1 in the Cartan algebra, [H_1, E_α] = iq_αE_α, H_1 = i diag(h_1, …, h_N), α = e_i − e_j, h̄_α := (h_i + h_j)/2),
fluctuations U_be^{X_b}, and let φ_b be the E_α-coefficient of X_b. Then (a) the Hessian of S_W splits into root-pair sectors
and the Cartan sector (no cross terms); (b) in sector α, with H normalised by H(1) = d^*d,
  ⟨φ, H(U)φ⟩ = Σ_P cos(h̄_αF_P)[cos(q_αF_P/2)|w_P|² − 2sin(q_αF_P/2)Σ_{a<b}s_as_bIm(y_aȳ_b)],
where for P = (x; μ, ν) with links l_1 = (x, μ), l_2 = (x + e_μ, ν), l_3 = (x + e_ν, μ), l_4 = (x, ν), s = (+, +, −, −), F_P :=
a_1 + a_2 − a_3 − a_4, y_1 = e^{−iq_αa_2}φ_1, y_2 = φ_2, y_3 = φ_3, y_4 = e^{−iq_αa_3}φ_4 (up to a common phase), w_P := Σ_as_ay_a;
and the root-sector covariant gradient is (D_Uω)_{x,μ} = e^{−iq_αa_{x,μ}}ω(x) − ω(x + e_μ) (up to an overall sign);
(c) at the Cartan plane wave a_{x,1} = εcos(px_2 + ϑ) (other a = 0), the root-sector symbol of K_F(U) = H(U) + D_UD_U^* obeys
(G1)-(G3) of §84 (U6) with O^c = −D²δ_{μν} − 2iq_αF_{μν}, D = ∂ + iq_αa (equivalently §84's form with q_α → −q_α; the spin
coefficient |2| is the content) [RFL12-fix S12-6: the equivalence holds with D and F both flipping (q_α → −q_α in both); §84 (U6)'s
"+2iq_αF" (l.3976) is superseded by −2iq_αF with D = ∂ + iq_αa; the relative sign does not enter C_{K_F} (tr A = 0) and f15 A3 fixes it]; the factor cos(h̄_αF_P) and the F² terms enter only at homogeneous degree ≥ 2 above the
lowest. **Corollary VFINE-K-val:** C_{K_F} = −20q_α²c_g (orbital 4, cross 0, spin −24), so (VFINE-K) and (VFINE-L) are
PROVEN with their values, given nothing beyond Lemma CL-V and FINE-IR-gen.
**(W3) Lemma T-tel (level-transverse telescoping; exact).** For every U at which the constructions of (T6) are defined and the
one-step covariance T_kD^{(k)} = D^{(k+1)}ι_k^* holds: P_{k+1}T_k = P_{k+1}T_kP_k, and Ỹ^{(k+1)} = T̃_kỸ^{(k)}T̃_k^T + κ^{-1}P_{k+1}Π_{k+1}^{-1}P_{k+1}
with T̃_k := P_{k+1}T_kP_k, Ỹ^{(0)} = P_⊥Y^{(0)}P_⊥. At critical U (Δ_U, H_⊥, Y_U invertible, D_ℓ injective, Ỹ^{(k)} invertible on
ker D^{(k)*}): total_n = ½Σ_{k<n}Φ^T_k + G_gh,n EXACTLY, Φ^T_k := log det_⊥Ỹ^{(k+1)} − log det_⊥Ỹ^{(k)}, log det_⊥Ỹ^{(0)} = −log det_⊥H_⊥;
hence c^tot_n = ½Σ_{k<n}φ^T_k − 2c_gq_α²log ℓ with φ^T_k := [f²]Φ^T_k(U_f), and NO level remainder object (no W_n, no G2). Also
(determinant form of the T-split IR identity) ½log det_⊥H_⊥ + ½log det_⊥Ỹ_U = ½log det_⊥(P_n𝒞_nP_n) + ½log det_⊥(H_⊥ +
M̃^T(P_n𝒞_nP_n)^{-1}M̃), M̃ := P_nM_UP_⊥.
**(W4) Proposition LONG-n (the level-longitudinal block of Y_n is not n-uniform).** At U = 1, for EVERY block map with the
one-step covariance T_kd_k = d_{k+1}ev_k (ev ev^T = 1) and Π_j = 1, and every level momentum K ≠ 0:
⟨V, Ŷ_n(K)V⟩ ≥ ⟨V, 𝒞̂_n(K)V⟩ ≥ κ^{-1}[1 + (n − 1)|D̂_ℓ(K)|²/8]. Consequently the session-11 (VC-L) (§84 (U7): n-uniform level-unit
vertex data of Y_n, hence of W_n) is FALSE at U = 1 at zeroth order for every covariant map (narrow: the level-longitudinal
block only, which drops out of the total by (W3)). **[RFL12-fix S12-2: the FALSE verdict is PROVEN for Y_n only. For W_n = V^*Y_n^{-1}V,
Cauchy-Schwarz gives only the lower bound W_n ≥ 1/⟨V, Y_nV⟩. The W_n half follows from the Schur form W_n(K) = 1/(Y_VV −
Y_VTỸ^{-1}Y_TV) with ||Ỹ^{-1}|| ≤ κ (the j = n term) and Y_VT bounded (A_j = Q_str^{(L^i)} − d_n∘h^{(i)}: the cross terms are summable),
so W_n(K) ≤ 1/(κ^{-1}[1 + (n − 1)λ̃(K)/8] − C(K)) → 0, log det W_n ~ −log n; written out with the session-13 proofs (forward reference), not counted as a new item. The
bound uses the soft-chain form 𝒞_n = κ^{-1}ΣA_jA_j^T of COV-str (ii) (Π_j = 1): read 'every block map in the soft chain of COV-str'.]**
**(W5) Proposition VC-T0 (the T-split symbols at U = 1 converge geometrically, for the actual S4' linearisation including
d∘h).** (a) The composite linearisation of 𝔪_n at U = 1 is M = Q_str^{(ℓ)} − d_ℓ∘h^{(n)}, h^{(n)} = Σ_{j<n}ev∘h_j∘Q_str^{(L^j)}, with the
explicit symbol M̂_{μν}(k) = δ_{μν}S_μ^{(ℓ)}(k_μ)Π_αD_ℓ(k_α) − D̂_ℓ(K)_μĥ^{(n)}_ν(k), ĥ^{(n)}_ν(k) = Σ_{j<n}ĥ_{L,ν}(L^jk)S_ν^{(L^j)}(k_ν)Π_αD_{L^j}(k_α),
ĥ_{L,ν}(θ) = [(D_L(θ_ν) − 1)/(e^{iθ_ν} − 1)]·avg_σΠ_{β before ν in σ}D_L(θ_β) (common centring phase dropped). (b) P_{T,ℓ}M̂ = P_{T,ℓ}Q̂_str:
the d∘h term drops out of Ỹ_n EXACTLY. (c) The level symbol of Ỹ_n(1) is P_{T,ℓ}(K)[𝒞̃_n(K) + diag(x^{blk}_{n,μ}(K))]P_{T,ℓ}(K), x^{blk}_{n,μ}(K)
:= ℓ^{-4}Σ_m|S_μ^{(ℓ)}(k_{m,μ})|²Π_αD_ℓ(k_{m,α})²/λ(k_m), 𝒞̃_n := κ^{-1}Σ_{i<n}s_i (s_i the level symbol of Q_str^{(L^i)}Q_str^{(L^i)T}, n-independent,
||s_i|| ≤ L^{-2i}); and sup_{K∈[−π,π]⁴∖0}||Ỹ̂_n(K) − Ỹ̂_∞(K)|| ≤ CL^{-2n}.
**(W6) (ARGUED; checked by f15 B3).** For the actual map, the d∘h part adds to ⟨V, Ŷ_n(K)V⟩ a term growing like c_hn|D̂_ℓ(K)|²
(each scale j of h^{(n)} contributes an O(1) amount), c_h > 0.
**(W7) Target (vector (UIR)).** The vector (V-IR) is reduced in the T-split of (W3) to named statements (the plane-wave vertex
data of Ỹ_n, including the plane-wave form factor of 𝔪_n and the background dependence of P_k; the T-split exchange at U_f);
Theorem UNIV for SU(N) is said to rest only on (L-loc2) ONLY if every other link is proved here.

**Check f15** (criteria file first, its stat into FLOW_LOG before any f15 script; jobs < 20 min, < 1 GB, memory free ≥ 35%, load
< 8 at start). Part A ((W2)): (A1) the (W2) (b) quadratic form against the exact second derivative of S_W along U_be^{tX_b}
(product rule on the matrices; SU(2) and SU(3) with h̄_α ≠ 0) at the plane wave on a small torus, ≤ 1e-11 relative; root/root′
and root/Cartan cross terms ≤ 1e-12; (A2) D_U against the derivative of the gauge orbit ≤ 1e-8; (A3) the leading homogeneous
parts: the lattice +p transfer symbol of O_1 at (sk, sp) divided by s against the O^c symbol, relative error ≤ 0.03 at
s = 0.01 and decreasing with s, the degree-0 part of the ϑ-free O_2 against q_α²/2; control: the O^c symbol with spin
coefficient 1 in place of 2 must fail (relative error ≥ 0.2). Part B ((W4)-(W6), n = 1..5 or 6, three K incl. a small one):
(B0) the (W5) (a) closed form against direct contour sums of the S4' contours (one step) and against the product of one-step
symbols (n ≤ 4), ≤ 1e-11 (linear algebra); (B1) geometric convergence of the T-split symbol: ratios of successive sup
differences in [0.07, 0.16] at the two largest n, all K; (B2) the (W6) growth: successive increments of ⟨V, N̂_n[M]V⟩ (the
M H^{-1}M^T part) positive and constant within 10% at the two largest n; (B3) control: the straight single-path map's T-split
symbol must NOT converge (successive differences grow by ≥ 2).

**Failure modes (each a valid outcome).** (S12-F1) (A1) or (A2) fails (the (W2) formula is wrong); (S12-F2) (A3) fails (the
continuum limit is not O^c, or the spin coefficient is not 2); (S12-F3) (B0) fails (the S4' symbol is wrong); (S12-F4) (B1)
fails (VC-T0 false); (S12-F5) (B2) fails ((W6) wrong; does not affect (W3)-(W5)).

---
# Session-12 proofs (written after §94, the [RFL11-fix] edits and the f15 run)

## 95. Lemma CL-V (the root-sector Wilson Hessian at Cartan backgrounds; classical continuum limit): PROVEN-HERE; Corollary VFINE-K-val: PROVEN-HERE

Statement: §94 (W2). Normalisation: S_W = (β/N)Σ_PRe tr(1 − U_P); "Hessian" = d²/dt²S_W(U_be^{tX_b})|_{t=0}, which is the
Riemannian Hessian on the product of bi-invariant group manifolds (t ↦ U_be^{tX_b} are geodesics), and H is that Hessian
divided by 2β/N, so that H(1) = d^*d.
*Proof.* (a), (b). Write U_P = U_1U_2U_3^{-1}U_4^{-1} with U_a = B_ae^{tX_a}. Moving the B's to the left (e^{X}C = Ce^{Ad(C^{-1})X}):
U_P = B_Pe^{tY_1}e^{tY_2}e^{−tY_3}e^{−tY_4}, B_P = B_1B_2B_3^{-1}B_4^{-1} = exp(F_PH_1) (the B's commute), Y_1 = Ad(B_4B_3B_2^{-1})X_1,
Y_2 = Ad(B_4B_3)X_2, Y_3 = Ad(B_4B_3)X_3, Y_4 = Ad(B_4)X_4. Since Ad(exp(cH_1))e_{ij} = e^{iq_αc}e_{ij}, the e_{ij}-coefficients are
y_a = e^{iq_α(a_3 + a_4)}·(e^{−iq_αa_2}φ_1, φ_2, φ_3, e^{−iq_αa_3}φ_4), and the common phase drops out of everything below. BCH:
e^{tY_1}e^{tY_2}e^{−tY_3}e^{−tY_4} = exp(tW + ½t²Σ_{a<b}[s_aY_a, s_bY_b] + O(t³)), W := Σs_aY_a, so the t² coefficient of Re tr U_P is
Re tr B_P(½W² + ½Σ_{a<b}[s_aY_a, s_bY_b]). With X = φe_{ij} − φ̄e_{ji} (anti-hermitian) and B_P = diag(e^{ih_kF_P}): (i) only diagonal
products contribute to tr(B_P·): W² has diagonal part −|w|²(e_{ii} + e_{jj}), so Re tr(B_P½W²) = −½|w|²(cos h_iF + cos h_jF) =
−|w|²cos(h̄_αF)cos(q_αF/2); (ii) the diagonal part of [y_ae_{ij} − ȳ_ae_{ji}, y_be_{ij} − ȳ_be_{ji}] is −2iIm(y_aȳ_b)(e_{ii} − e_{jj}), and
Re[−i·Im(·)(e^{ih_iF} − e^{ih_jF})] = Im(y_aȳ_b)(sin h_iF − sin h_jF) = 2cos(h̄_αF)sin(q_αF/2)Im(y_aȳ_b). So the t² coefficient is
cos(h̄_αF_P)[−cos(q_αF_P/2)|w_P|² + 2sin(q_αF_P/2)Σ_{a<b}s_as_bIm(y_aȳ_b)], and d²/dt²S_W = (2β/N)·(the (W2) (b) summand). Cross terms:
a product or commutator of e_{ij}-type matrices from two different root pairs, or of a root matrix with a Cartan matrix, has zero
diagonal, so its trace against the diagonal B_P vanishes; hence the root pairs and the Cartan sector decouple at quadratic order
(at every abelian background, critical or not). D_U: the gauge orbit e^{tω(x)}U_{x,μ}e^{−tω(x+e_μ)} = U_{x,μ}e^{X(t)} has
X′(0) = Ad(U_{x,μ}^{-1})ω(x) − ω(x + e_μ), whose e_{ij}-coefficient is e^{−iq_αa_{x,μ}}ω(x) − ω(x + e_μ).
(c) At the plane wave only the links in direction 1 carry a, a_{x,1} = a(x_2) := εcos(px_2 + ϑ), so only plaquettes (x; 1, ν) see the
background, with a_1 = a(x), a_2 = 0, a_3 = a(x + e_ν), a_4 = 0, F_P = a(x) − a(x + e_ν) (nonzero only for ν = 2), and
w_P = φ_{x,1} + φ_{x+e_1,ν} − φ_{x+e_ν,1} − e^{−iq_αa(x+e_ν)}φ_{x,ν}; also (D_U^*φ)(x) = Σ_μ[e^{iq_αa_{x,μ}}φ_{x,μ} − φ_{x−e_μ,μ}].
(G1): at ε = 0, ⟨φ, Oφ⟩ = Σ|dφ|² + |d^*φ|², and d^*d + dd^* on 1-forms is the componentwise lattice Laplacian: O_0 = λ(k)·1, analytic,
> 0 for k ≠ 0, = |k|²1 + O(|k|⁴). Every coefficient of ⟨φ, Oφ⟩ is an entire function of the a-values (exponentials, cos, sin), so
O_1 (linear in a: momentum transfer ±pe_2 only) and the transfer-0 (ϑ-free) part of O_2 are trigonometric polynomials in k with
coefficients entire in p: analytic. (G2): at p = 0, a_{x,1} = c := εcos ϑ is pure gauge. With φ_{x,1} = e^{−iq_αcx_1}ψ_{x,1},
φ_{x,ν} = e^{−iq_αcx_1}e^{iq_αc}ψ_{x,ν} (ν ≥ 2), every w_P and every (D_U^*φ)(x) equals e^{−iq_αcx_1} times a fixed unimodular constant
times the corresponding U = 1 expression of ψ (direct check on the two formulas above), and F ≡ 0; so O(U_c) = GO(1)G^{-1} with G
unitary, i.e. the symbol is O_0(k + q_αce_1) conjugated by a constant diagonal unitary (sign of the shift by orientation). The ε²
density at p = 0 is therefore ¼q_α²∫∂_1²tr log O_0(k)dk/(2π)⁴, the integral of a total k_1-derivative of the periodic function
¼q_α²∂_1 tr log λ = q_α²∂_1λ/λ (O(|k|^{-1})), whose derivative O(|k|^{-2}) is L¹. (G3): expand at small (k, p). At first order in ε:
from |w_P|², 2Re(w̄_P^0·iq_αa(x + e_ν)φ_{x,ν}) (w^0 the U = 1 curl); from the spin term, −q_αF_P·J_P^0 (ν = 2 only; sin(q_αF/2) =
q_αF/2 + O(ε³), cos(h̄F) = 1 + O(ε²)); from the gauge term, 2Re(\overline{d^*φ}·iq_αa(x)φ_{x,1}). At leading homogeneous order
w^0_{1ν} → ∂_1φ_ν − ∂_νφ_1, a(x + e_ν) → a(x), F_P → −∂_2a_1 = F_{12}, d^*φ → ∂·φ (up to sign), and J^0 = Σ_{a<b}s_as_bIm(y_aȳ_b) with
y = (φ_1, φ_2, φ_1, φ_2) gives J^0 → Im(φ_1φ̄_2)(1 − 1 + 1 + 1) = 2Im(φ_1φ̄_2). These are the first-order parts of the continuum form
Q^c(φ) = ∫[Σ_{μ<ν}|D_μφ_ν − D_νφ_μ|² + |D·φ|² − 2q_αF_{12}Im(φ_1φ̄_2)], D = ∂ + iq_αa (indeed w_P → D_1φ_ν − D_νφ_1 since
φ_{x+e_1,ν} − e^{−iq_αa}φ_{x,ν} → (∂_1 + iq_αa_1)φ_ν). Weitzenböck (integrating by parts, D_μ^† = −D_μ, [D_μ, D_ν] = iq_αF_{μν}):
Σ_{μ<ν}|D_μφ_ν − D_νφ_μ|² + |D·φ|² = ⟨φ, −D²φ⟩ + Σ_{μν}⟨φ_ν, [D_μ, D_ν]φ_μ⟩ = ⟨φ, (−D² − iq_αF)φ⟩, and −2q_αF_{12}Im(φ_1φ̄_2) =
iq_αF_{12}(φ_1φ̄_2 − φ̄_1φ_2) = ⟨φ, −iq_αFφ⟩ (both spin contributions carry the same sign). So Q^c = ⟨φ, O^cφ⟩, O^c = −D²δ_{μν} −
2iq_αF_{μν}: the degree-1 part of O_1 is that of O^c, explicitly (O_1's +p part = (ε/2)e^{iϑ}Ṽ_+, pe_2 the transfer)
Ṽ_+^c(k, p) = 2q_αk_1·1 − 2q_αp(E_{12} − E_{21}). At second order the only degree-0 terms are |iq_αa(x + e_ν)φ_{x,ν}|² (ν ≥ 2) and
|iq_αa(x)φ_{x,1}|², i.e. q_α²a²·1, whose ϑ-free part is (q_α²/2)ε²·1, the diamagnetic term of O^c; every other ε² term has degree ≥ 1
(w^0 or F carries a derivative: 2Re(w̄^0(−q_α²a²/2)φ_ν), F·a·φφ from the phase in y_4, and F² from cos(q_αF/2), cos(h̄_αF), the
last of degree ≥ 2 above the lowest). The parity hypothesis of (G3) for the continuum integrand follows from complex conjugation
(charge −q_α, k ↦ −k) and (p, ϑ) ≡ (−p, −ϑ), as in the [RFL11-fix S11-3] note of §88. ∎
**Corollary VFINE-K-val.** By Lemma CL-V, (CL-V) holds; FINE-IR-gen (under (G1)-(G3) alone, [RFL11-fix S11-3]) gives
x^{K_F}(p) = 2C_{K_F}log(1/p) + a^{K_F} + o(1), and the continuum computation of the [RFL11-fix S11-3] paragraph of §88 (for O^c
in the form (−i∂ − qa)² + 2iqF, which is ours with q → −q in D and F together [RFL12-fix S12-6]; C ∝ q²) gives C_{K_F} = −20q_α²c_g. So (VFINE-K) is PROVEN with its
value, and (VFINE-L) = (VFINE-K) − ½(VFINE-gh) is PROVEN, value included (the 21/22 share of the GH-log
split, REVIEW_FLOW_S11 §4.4 cross-check), with a finite part. ∎
*Reading.* (1) SU(N), N ≥ 3: the factor cos(h̄_αF_P) (h̄_α ≠ 0 for a generic Cartan direction) is the only place where the root
sector is not literally a charged U(1) vector field; it enters at F², i.e. two degrees above the lowest, and does not touch
C_{K_F}. (2) f15 A1 (exact second derivative at ε = 0.7, no expansion): max rel 1.3e-16 (SU(2) and SU(3), all roots); cross terms
2.3e-16; dropping the spin term fails (1.0e-2) [RFL12-fix S12-7: a WEAK control: at this background the spin term is ≈ 1% of the Hessian;
the decisive spin test is A3c]; A2: D_U to 4.9e-11; A3: the lattice degree-1 symbol of O_1 against Ṽ_+^c at
s = 0.01: E1 = 3.2e-3 … 6.1e-3, halving with s (both roots, three directions); the spin-coefficient-1 control fails (E1 ≥ 0.50);
O_2's degree-0 part q_α²/2 to ≤ 3.8e-5.

## 96. Lemma T-tel (level-transverse telescoping): PROVEN-HERE

Statement: §94 (W3).
*Proof.* (i) T_kD^{(k)} = D^{(k+1)}ι_k^* says T_k maps Ran D^{(k)} into Ran D^{(k+1)}. 1 − P_k is the orthogonal projector onto
Ran D^{(k)} (= (ker D^{(k)*})^⊥, finite dimensions), so P_{k+1}T_k(1 − P_k) = 0, i.e. P_{k+1}T_k = P_{k+1}T_kP_k. Compressing the
Y-recursion of L-tel (valid at every U) with P_{k+1}: Ỹ^{(k+1)} = P_{k+1}T_kY^{(k)}T_k^TP_{k+1} + κ^{-1}P_{k+1}Π_{k+1}^{-1}P_{k+1} =
T̃_k(P_kY^{(k)}P_k)T̃_k^T + κ^{-1}P_{k+1}Π_{k+1}^{-1}P_{k+1}, a closed recursion on the transverse subspaces; Ỹ^{(n)} = P_nY_UP_n = Ỹ_U.
(ii) At critical U, by the proof of L-tel, total_n = ½log det K_F − log det Δ_U + ½log det Y_U + ½log det(D_ℓ^*Y_U^{-1}D_ℓ). With V an
orthonormal frame of Ran D_ℓ and D_ℓ = VR: log det(D_ℓ^*Y^{-1}D_ℓ) = log det(D_ℓ^*D_ℓ) + log det(V^*Y^{-1}V), and Jacobi's
complementary-minor identity det(V^*Y^{-1}V) = det_⊥(P_nYP_n)/det Y (Y invertible on E_ℓ = Ran V ⊕ ker D_ℓ^*). Hence
½log det Y_U + ½log det(D_ℓ^*Y_U^{-1}D_ℓ) = ½log det(D_ℓ^*D_ℓ) + ½log det_⊥Ỹ_U. With log det K_F = log det_⊥H_⊥ + log det Δ_U (§85 (a)) and
G_gh,n = ½log det(D_ℓ^*D_ℓ) − ½log det Δ_U: total_n = ½log det_⊥H_⊥ + G_gh,n + ½log det_⊥Ỹ_U. Ỹ^{(0)} = P_⊥Y^{(0)}P_⊥ = H_⊥^{-1}P_⊥ at
critical U (§85 (a)), so −log det_⊥Ỹ^{(0)} = log det_⊥H_⊥, and telescoping log det_⊥Ỹ_U − log det_⊥Ỹ^{(0)} = Σ_{k<n}Φ^T_k gives total_n =
½Σ_{k<n}Φ^T_k + G_gh,n. Taking [f²] at U_f and GH-log (c) ([f²]G_gh,n = −2c_gq_α²log ℓ exactly): c^tot_n = ½Σ_{k<n}φ^T_k − 2c_gq_α²log ℓ.
(iii) Determinant form of the IR identity: with A := P_n𝒞_nP_n (invertible on ker D_ℓ^*, since 𝒞_n > 0 near 1) and M̃ := P_nM_UP_⊥,
P_nM_UH_⊥^{-1}P_⊥M_U^TP_n = M̃H_⊥^{-1}M̃^T, so by Sylvester det_⊥(A + M̃H_⊥^{-1}M̃^T) = det_⊥A·det_⊥(H_⊥ + M̃^TA^{-1}M̃)/det_⊥H_⊥. ∎
*Reading.* (1) **The T-split has no level remainder**: the whole level-n object is in the steps, and the remainder is the exactly
solved ghost group. W_n and G2 do not occur; (GP-L) and (GP) are not needed. (2) For k ≥ 1, Φ^T_k − Φ^L_k = +log det(V_{k+1}^*Y^{(k+1)-1}V_{k+1})
− log det(V_k^*Y^{(k)-1}V_k) **[RFL12-fix S12-1: both signs corrected (they were reversed); by Jacobi log det_⊥Ỹ = log det Y +
log det(V^*Y^{-1}V); REVIEW_FLOW_S12 §0 confirms both sides numerically]** (Jacobi at levels k + 1 and k): the Landau steps of L-tel carry the level-LONGITUDINAL blocks, which are not
n-uniform (§97); the T-split removes them, exactly as L-tel removed G2 from the Feynman steps. (3) One-step form (Woodbury):
Φ^T_k = log det_⊥(Ỹ^{(k)-1} + κT̃_k^TΠ̃_{k+1}^{-1}T̃_k) + log det_⊥(κ^{-1}Π̃_{k+1}), Π̃_{k+1} := P_{k+1}Π_{k+1}^{-1}P_{k+1} on ker D^{(k+1)*}; at U_f
the Nielsen-Olesen mode sits in Ỹ^{(0)} = H_⊥^{-1}P_⊥, as in §87 Reading (2). (4) (iii) is the session-5/6 form G_⊥,n + G_gh,n (l.839)
read through Jacobi: the T-split IS that binding re-split, now with its telescoping and its exact one-step recursion.
**[RFL12-fix S12-3: notation. In l.839 read Π := P_n(P_n𝒞_nP_n)^{-1}P_n, and l.839's "P_⊥" as the LEVEL transverse projector P_n;
in §94-§96 P_⊥ = P_0 is the FINE projector. With that reading (iii) is l.839.]**

## 97. Proposition LONG-n (the level-longitudinal block of Y_n is not n-uniform): PROVEN-HERE

Statement: §94 (W4).
*Proof.* At U = 1, Y_n = 𝒞_n + M(P_T/λ)M^T ≥ 𝒞_n (§87), and 𝒞_n = κ^{-1}Σ_{j=1}^nA_jA_j^T (Lemma COV-str (ii), Π_j = 1), A_j the composite
of the one-step maps from level j to level n, A_n = 1; by induction A_jd_j = d_nev (ev: level j → level n, ev ev^T = 1). Fibre at a
level-n momentum K, i := n − j: the level-j fibre is spanned by the L^{4i} aliases κ_m = (K + 2πm)/L^i; A_j(K) = L^{-2i}[Â_j(κ_m)]_m,
d_j(K) = diag(ŝ(κ_m)) (one component per alias), ev(K) = L^{-2i}(1, …, 1), so ev(K)ev(K)^† = 1 and A_j(K)d_j(K) = D̂_ℓ(K)ev(K). For
ψ := ev(K)^†: |A_j(K)^†V|² ≥ |⟨A_j^†V, d_jψ⟩|²/|d_jψ|² = |⟨V, D̂_ℓ⟩|²/|d_jψ|² = |D̂_ℓ(K)|²/|d_jψ|², and |d_jψ|² = L^{-4i}Σ_mλ(κ_m) = Σ_μ
avg_m 4sin²((K_μ + 2πm_μ)/(2L^i)) = 8 for i ≥ 1 (each average is 2 − 2·avg cos = 2 over L^i ≥ 2 equally spaced points). The j = n term
is |V|² = 1. Summing: ⟨V, 𝒞̂_n(K)V⟩ ≥ κ^{-1}[1 + (n − 1)|D̂_ℓ(K)|²/8]. ∎
*Reading.* (1) **The session-11 (VC-L) (n-uniform level-unit vertex data of Y_n, hence W_n = V^*Y_n^{-1}V) is FALSE at U = 1 at zeroth
order, for EVERY covariant block map**: the coarse-gauge directions accumulate the noise of every level undamped (this is
COV-str (iv) in symbol form; it was overlooked in §84 (U7)). NARROW: it concerns the level-longitudinal block only, which drops
out of the total by Lemma T-tel. **[RFL12-fix S12-2: PROVEN for Y_n; the W_n clause by the Schur argument of the (W4) tag (forward reference to the session-13 proofs).]**
(2) f15 B4: κ⟨V, 𝒞̂_nV⟩ grows by 0.1225 per level at K_a (|D̂_ℓ|² = 0.757), 1.4743 at K_b (|D̂_ℓ|² = 9.12),
i.e. ≈ 0.162|D̂_ℓ|² per level, above the bound |D̂_ℓ|²/8 at every n ≤ 6 and K (K_c included).

## 98. Proposition VC-T0 (the T-split at U = 1 for the actual S4' linearisation, d∘h included): PROVEN-HERE; (W6): ARGUED, confirmed by f15 B2

Statement: §94 (W5).
*Proof.* (a) One step (side L, level-j units, block centre c = 0, y ∈ B := {−r..r}⁴, r = (L − 1)/2): on A_ν(x) = e^{ik·x}, an axial leg in
direction α from coordinate c_α to y_α at fixed other coordinates z contributes e^{ik·z}(e^{ik_αy_α} − e^{ik_αc_α})/(e^{ik_α} − 1) (both
orientations). For the order σ, the leg in σ_j has the coordinates σ_1..σ_{j−1} at y and the rest at c; averaging over y (avg_ye^{ik_βy_β}
= D_L(k_β)) gives, for the slice functional h, ĥ_ν(k) = [(D_L(k_ν) − 1)/(e^{ik_ν} − 1)]·avg_σΠ_{β before ν}D_L(k_β) = ĥ_{L,ν}(k), and
Q_str has the symbol δ_{μν}S_μ^{(L)}(k_μ)Π_αD_L(k_α); Q_root = Q_str − d∘h (LINEAR_PACKAGE §1.2) gives the one-step M̂_L. Composite: from
Q_str∘d = d∘(ev + h∘d) (LINEAR_PACKAGE §1.2), Q^{(k+1)} = Q_k∘Q^{(k)} = (Q_str,k − dh_k)(Q_str^{(k)} − dh^{(k)}) = Q_str^{(k+1)} − d[ev∘h^{(k)} +
h_k∘(Q^{(k)} + d∘h^{(k)})] = Q_str^{(k+1)} − d[ev∘h^{(k)} + h_k∘Q_str^{(k)}] (Lemma IT-str for the composite straight average), so h^{(n)} =
Σ_{j<n}ev∘h_j∘Q_str^{(L^j)}. The level-j field of a fine plane wave is a plane wave of momentum L^jk with amplitude Q̂_str^{(L^j)}(k), and
ev has symbol 1 (common centres, ℓ odd); this gives the (W5) (a) formula. Check: Σ_νĥ^{(n)}_ν(e^{ik_ν} − 1) telescopes to Π_αD_ℓ(k_α) − 1
(S^{(L^j)}_ν(k_ν)(e^{ik_ν} − 1) = e^{iL^jk_ν} − 1 and D_{L^{j+1}}(θ) = D_{L^j}(θ)D_L(L^jθ)), so M̂ŝ = D̂_ℓ (covariance). (b) P_{T,ℓ}D̂_ℓ = 0.
(c) Ỹ_n(1) = P_n𝒞_nP_n + P_nM(P_T/λ)M^TP_n. By (b), P_nM = P_nQ_str^{(ℓ)}, and Q̂_strŝ = D̂_ℓΠ_αD_ℓ, so P_{T,ℓ}Q̂_strP_TQ̂_str^†P_{T,ℓ} =
P_{T,ℓ}Q̂_strQ̂_str^†P_{T,ℓ} = P_{T,ℓ}diag(|S_μ|²Π_αD_ℓ²)P_{T,ℓ}: the M-part is P_{T,ℓ}diag(x^{blk}_{n,μ})P_{T,ℓ}. The same covariance at level j
(A_j = Q_str^{(L^i)} − d_n∘h^{(i)}) gives P_nA_jA_j^TP_n = P_nQ_str^{(L^i)}Q_str^{(L^i)T}P_n, so P_n𝒞_nP_n = κ^{-1}P_{T,ℓ}(Σ_{i<n}s_i)P_{T,ℓ}; s_i is
n-independent, and by the Schur test (row sums of Q_str^{(r)} = r, column sums = r^{-3}, r = L^i) ||s_i|| ≤ ||Q_str^{(r)}||² ≤ L^{-2i}.
Rate. Write term_ℓ(x) := ℓ^{-4}|S_μ(x_μ/ℓ)|²Π_αD_ℓ(x_α/ℓ)²/λ(x/ℓ), x = x_m with representatives |x_α| ≤ πℓ, and term_∞(x) :=
|e^{ix_μ} − 1|²x_μ^{-2}Π_α(sin(x_α/2)/(x_α/2))²/|x|². Since |sin y| ≥ 2|y|/π on |y| ≤ π/2: |S_μ(x/ℓ)|/ℓ ≤ min(1, π/|x_μ|), |D_ℓ(x/ℓ)| ≤
min(1, π/|x|), ℓ²λ(x/ℓ) ≥ (4/π²)|x|², so term_ℓ, term_∞ ≤ CΠ_αmin(1, π²/x_α²)/|x|²; and |S|², D_ℓ, ℓ²λ differ from their limits by the
relative factor 1 + O(|x|²/ℓ²) uniformly on |x_α| ≤ πℓ (ℓ sin(y/ℓ) = y(1 + O(y²/ℓ²)); only |S|² enters, so the first-order phase error
of S drops out). Hence |term_ℓ − term_∞| ≤ Cℓ^{-2}Π_αmin(1, π²/x_α²), summable over m ∈ Z⁴ uniformly in K (a product of 1D sums), and
the tail of the limit sum beyond |x_α| > πℓ is ≤ Cℓ^{-2} by the same bound. So |x^{blk}_{n,μ}(K) − x^{blk}_{∞,μ}(K)| ≤ Cℓ^{-2} uniformly on
[−π, π]⁴∖{0} (the m = 0 term included: |x|²·|x|^{-2} is bounded), P_{T,ℓ} is n-independent with norm 1, and ||Σ_{i≥n}s_i|| ≤ CL^{-2n}. ∎
*Reading.* (1) **The d∘h correction of S4' drops out of the T-split EXACTLY** (P_{T,ℓ}M̂ = P_{T,ℓ}Q̂_str), so the level-transverse
symbols are those of the product-Dirichlet straight average, and they converge geometrically at L^{-2}, uniformly down to K = 0
with no normalisation needed at zeroth order. **[RFL12-fix S12-5: "uniformly down to K = 0" applies to the DIFFERENCE
Ỹ̂_n − Ỹ̂_∞; the symbol itself is ~|K|^{-2} (the m = 0 term of x^{blk}).]** **[RFL12-fix S12-4: (b) is a U = 1 identity. At U ≠ 1, for
EVERY decomposition A_j(U) = Q_j(U) − D_n(U)h_j(U), P_n(U)A_jA_j^*P_n(U) = P_n(U)Q_jQ_j^*P_n(U) exactly, so the D_n(·)D_n^* growth never
enters the T-split, PROVIDED Q_j(U) has n-uniform, L^{-i}-summable ε-data ((T-a1)); with the U = 1 pairing D_n(1)h_j(1) the termwise
ε-expansion of P_n(U) carries a second-order term ~ n (pre-stated as §103 (X4) (d); proof to follow).]** (2) f15 B1: Δ_n = 2.30e-2, 2.56e-3, 2.84e-4, 3.16e-5, 3.51e-6 (K_a, n = 2..6), ratios
0.1113, 0.1111, 0.1111, 0.1111; K_b 0.1199 … 0.1112; K_c = (0.06, 0.04, 0.03, 0.02) 0.1111 throughout; ||s_i|| ratios 0.111; the
straight single-path control diverges (ratios 3.00). B0: the closed form against the S4' contour sums 6.0e-15, against the product
of one-step symbols 2.3e-14. (3) This is the ZEROTH-order part of the vector (VC) in the T-split; the plane-wave vertex data are
§99 (T-a).
*(W6) (ARGUED).* Each scale j of h^{(n)} = Σ_jev∘h_j∘Q_str^{(L^j)} is an O(1) level-j slice of the scale-L^j averaged field, so
⟨V, N̂_n[M]V⟩ gains c_h|D̂_ℓ|² per level. f15 B2 (pre-stated): δ_n/|D̂_ℓ|² = 2.2245e-4, 2.2531e-4, 2.2588e-4, 2.2594e-4 (n = 3..6) at K_a and
2.2373e-4, 2.2569e-4, 2.2592e-4, 2.2594e-4 at K_b: constant, positive, and the same at both K (c_h ≈ 2.259e-4). Map-specific; it adds to
the 𝒞_n growth of §97 in the longitudinal block and, like it, drops out of the T-split.

## 99. Target (W7) (vector (UIR)): OPEN, re-reduced in the level-transverse split; the minimal UNIV list

**Step-1 list (after REVIEW_FLOW_S11, the S11 fixes applied).** (L-loc2); (CL-V); (VC-L) for the Landau steps and D_ℓ^*Y_n^{-1}D_ℓ
(Q_root including d∘h, with the Landau vector IR-id); the Landau plane-wave/constant-field exchange at U_f (with the plane-wave
form factor of 𝔪_n and the Nielsen-Olesen mode). (G1′), (G4) dropped (automatic); (GP-L) inside (VC-L).
**Session-12 revision.** (CL-V) is PROVEN (§95), so (VFINE-K) and (VFINE-L) are PROVEN with their values. (VC-L) in the Landau form is
FALSE at zeroth order for every covariant map (§97); the right split is T-tel (§96), whose remainder is exactly G_gh,n, and whose
zeroth-order symbols converge at L^{-2} for the actual S4' map, d∘h included (§98). At U_f: c^tot_n = ½Σ_{k<n}φ^T_k − 2c_gq_α²log ℓ. By
the scalar template, the vector (UIR)/(V-IR) in the form (Q1)(d) would follow from:
- **(T-a) T-split vertex data:** the first- and second-order plane-wave vertex symbols of Ỹ_n converge in level units at rate
  L^{-2n} on the half-radius polydisc after λ̃-normalisation, with an n-independent leading (degree-4) numerator. Inputs: the
  plane-wave form factor of 𝔪_n (the ε-expansion of T_k(U) and Π_k(U), W_♮ for N ≥ 3); the background dependence of
  P_k(U) = 1 − D^{(k)}Δ_k^{-1}D^{(k)*} (a massless level Laplacian: its poles must be absorbed as in Lemma VC); H_⊥(U)^{-1}P_⊥ through
  M̃. OPEN. **[RFL12-fix S12-4: (T-a) is replaced by (T-a1) (the background linearisation T_k(U) in covariant-decomposition form
Q_k(U) := T_k(U) + D^{(k+1)}(U)h_k(U), first- and second-order plane-wave symbols n-uniform and L^{-i}-summable) and (T-a2) (the
ε-expansion of P_k(U) = 1 − D^{(k)}Δ_k^{-1}D^{(k)*}: first-order massless poles at K and K + P, normalisation λ̃(K)λ̃(K + P); P_{T,ℓ} is
non-analytic at K = 0, analyticity only for λ̃P_T = λ̃ − D̂D̂^†); see §103 (X4), (X5) (pre-stated; proofs follow).]** **[RFL12-fix S12-9: the plane-wave form
factor of 𝔪_n leaves this list: it is Lemma Cartan-𝔪 (§103 (X2), pre-stated; proof follows), exact for 𝔪^{S4'} and through second order for the chain map.]** (Zeroth order: PROVEN, §98; the transverse form factors are products of 1D Dirichlet factors, Lemma A applies.)
- **(T-b) T-split IR identity, polarisation form:** from the determinant form (§96 (iii), PROVEN) to x^T_n(ℓp) = x^⊥_0(p) − h^T_n(p)/(p²/2),
  which needs the plane-wave density of the gapped fine operator H_⊥ + M̃^T(P_n𝒞_nP_n)^{-1}M̃ (the vector analogue of S-red (ii) and
  §75 (b)). OPEN.
- **(T-c) T-split exchange at U_f** (plane wave ↔ constant field for the steps Φ^T_k, the NO mode in Ỹ^{(0)} via the Woodbury form
  of §96 Reading (3)). OPEN.
- **(L-loc2).** OPEN (ARGUED).
- Unchanged: (s1), (s2⊥) (rate); the rate of c'(φ) → c'_0; (COV-GI) at non-critical backgrounds (not needed on the critical-background
  route); FI-1; HIST's restatement of CL^J's Setting.
Not on the list any more: (VC-V) (false, §86), (GP) (Feynman-split statement, irrelevant to c^tot_n), (VC-L) for Y_n and (GP-L)
(Landau-split statements, false or unnecessary: §97, §96 [RFL12-fix S12-2: LONG-n proves the Y_n half; W_n by the Schur argument of the (W4) tag]), (G1′), (G4) (automatic), (CL-V) and the value of C_{K_F} (proven).
**So Theorem UNIV for SU(N) does NOT yet rest only on (L-loc2)**: it rests on (L-loc2), (T-a), (T-b), (T-c) and the unchanged
cross-lane and rate items.

## 100. Session-12 check f15 (ADDED AFTER the run; checks/f15_criteria.md, f15_cl_vct.py, f15_out.txt, f15_time.txt)
Criteria written 10:51:15 UTC before any f15 script (stat in FLOW_LOG); the script (birth = mtime 10:57:07 UTC, 24239 B, md5
e06c0c38c07bfcb1a1d3f6f2501e80fa) is a cmp-identical copy of the development file flow12/dev.py as smoke-run at 10:56:36-40 UTC and
was not changed afterwards. Official run: one NUMERIC LOCK acquisition, 10:58:16-10:58:55 UTC, nice 10, 1 thread, load 4.50,
memory free 38% (checked inside the lock before starting); 39.0 s, peak RSS 100 MB. **25/25 verdict lines PASS.**
- **Part A (CL-V): ALL PASS.** A1 2Q = exact second derivative, max rel 1.3e-16 (SU(2); SU(3), three roots with h̄ ≠ 0; ε = 0.7);
  A1x cross terms ≤ 2.3e-16; A1c control (spin term dropped) fails at 1.0e-2 [RFL12-fix S12-7: weak control, the spin term is ≈ 1% of the Hessian here; the
spin test is A3c]; A2 D_U ≤ 4.9e-11; A3 E1(s = 0.01) = 3.2e-3, 6.1e-3, 5.0e-3
  (three directions; identical for the two roots), each half of its s = 0.02 value; E2 ≤ 3.8e-5; O_0 = λ1 to 7e-19; A3c control
  (spin 1) E1 ≥ 0.496.
- **Part B: ALL PASS.** B0 closed form = contour sums (6.0e-15), = product of one-step symbols (2.3e-14), covariance (9.5e-16);
  B1 T-split ratios 0.1111-0.1114 at n = 5, 6 (K_a, K_b, K_c), s_i ratios in range, step control 1.2e-13; B2 increments constant
  (ratio 1.0003 at K_a, 1.0001 at K_b) and positive; B3 straight path diverges (ratio 3.00); B4 the LONG-n bound holds at all n ≤ 6, K.
- **Reading.** (1) S12-F1..F5 do not occur. (2) The explicit root Hessian is exact (not just to second order in the background), and
  its continuum limit has the spin coefficient 2: the value C_{K_F} = −20q_α²c_g rests on proven statements. (3) The actual S4' map is
  admissible for the T-split at zeroth order, with the predicted L^{-2} rate; the longitudinal growth exists in both of its
  predicted sources (𝒞_n: proven bound; d∘h: c_h ≈ 2.26e-4 per level).

## 101. Session-12 outcomes against §94 (ADDED AFTER the derivations and the check)
- **(W1) Step 1: DONE.** S11-1..S11-8 applied in place, tagged [RFL11-fix] (25 in-place replacements in §86, §88, §89, §90, §91,
  §92, §93; S11-2 and S11-8 also recorded in FLOW_LOG); the minimal UNIV list written (§99, step-1 list).
- **(W2) Lemma CL-V: PROVEN** (§95), with f15 A. **Corollary VFINE-K-val: PROVEN**: C_{K_F} = −20q_α²c_g; (VFINE-K), (VFINE-L) PROVEN
  with values.
- **(W3) Lemma T-tel: PROVEN** (§96): c^tot_n = ½Σφ^T_k − 2c_gq_α²log ℓ, no level remainder; determinant-form IR identity.
- **(W4) Proposition LONG-n: PROVEN** (§97): the session-11 (VC-L) for Y_n (and W_n [RFL12-fix S12-2: the W_n half by the Schur argument of the (W4) tag]) is FALSE at zeroth order for every covariant
  map (narrow: the longitudinal block, which drops out by T-tel).
- **(W5) Proposition VC-T0: PROVEN** (§98): d∘h drops out of the T-split exactly; rate L^{-2n}, uniform on [−π, π]⁴∖{0}.
- **(W6): ARGUED, confirmed** by f15 B2 (constant increments c_h|D̂_ℓ|², c_h ≈ 2.259e-4).
- **(W7): OPEN**, re-reduced (§99): Theorem UNIV for SU(N) does NOT yet rest only on (L-loc2); it rests on (L-loc2), (T-a) (including
  the plane-wave form factor of 𝔪_n), (T-b), (T-c) and the unchanged cross-lane and rate items. The plane-wave form factor of 𝔪_n
  and the Landau/T-split plane-wave/constant-field exchange were NOT proved in session 12.
- **Step 4 (f15): DONE**, 25/25.

## 102. Tally after session 12 (FLOW.md items; session-12 items unreviewed)
- **PROVEN-HERE: 65 (through session 11, as confirmed by REVIEW_FLOW_S11; 62 under its strict convention) + 5 (session 12) = 70**
  (strict: 62 + 4 = 66, with VFINE-K-val folded into CL-V). Session 12: Lemma CL-V; Corollary VFINE-K-val; Lemma T-tel; Proposition
  LONG-n; Proposition VC-T0. Upstream inputs used: Lemma COV-str (ii), (iv); LINEAR_PACKAGE §1.2 (Q_root = Q_str − d∘h, Q_str∘d =
  d∘(ev + h∘d)); Lemma IT-str; L-tel's Y-recursion and critical total; §85 (a); GH-log (c); FINE-IR-gen with the [RFL11-fix S11-3]
  automatic hypotheses.
- **IMPORTED-AND-REVERIFIED:** L4b; the Lévy-process functional CLT (§58). No new import (the continuum Weitzenböck identity and the
  BCH expansion are derived here; the continuum C_{K_F} is the derivation of REVIEW_FLOW_S11 §4.4, written in §88).
- **ARGUED, not counted:** (L-loc2); (W6) (the d∘h longitudinal growth; checked by f15 B2); the (GP) mechanism (a Feynman-split
  statement, irrelevant to c^tot_n); Lemma DEF-red (remark).
- **OPEN:** (V-IR) on G_⊥ in the form (Q1)(d) [s-P] (crux), now reduced in the T-split to (T-a) (vertex data, including the
  plane-wave form factor of 𝔪_n and the background dependence of P_k) [s], (T-b) [s], (T-c) [s] (§99); (L-loc2) [s]; (s1), (s2⊥)
  [s-P] (rate only); the rate of c'(φ) → c'_0 [s]; (COV-GI) at non-critical backgrounds [s]; FI-1 [cross-lane]; HIST's restatement
  of CL^J's Setting [cross-lane]. Retired: (VC-V) Feynman form (false); (GP), (GP-L) (not needed); (VC-L) for Y_n [RFL12-fix S12-2: Y_n proven; W_n via the (W4) tag] (false at zeroth
  order, §97).
- **Checks:** f15 (A1 ×2, A1x, A1c, A2, A3 ×3, A3c, B0 ×3, B1 ×8, B2 ×2, B3 ×2, B4 PASS).

## 103. Session-13 targets and PRE-STATED (session 13) statements (written 2026-10-28 ~11:35 UTC, the first edit of session 13: before the [RFL12-fix] edits and before any session-13 proof, criteria file or script)

Binding input: REVIEW_FLOW_S12.md (fixes S12-1..S12-9, applied after this section, in place, tagged **[RFL12-fix]**; T-tel
confirmed exact; LONG-n for Y_n only; VC-T0 at U = 1 only; away from U = 1 the D_n(·)D_n^* growth stays out of the T-split iff
the block-map linearisation at U is written as a covariant piece minus the level derivative OF A SLICE MAP PAIRED WITH THE
GRADIENT AT U). Notation of §94. In addition: the chain block map is 𝔪 = W_♮∘M̄ (§30: M̄_c the mean of the S4' contour
transporters T^σ_y, W_♮ the polar part for N = 2 and the SU(N) maximiser of Re tr(V^{-1}M) for N ≥ 3); 𝔪^{S4'} denotes the
log-averaged S4' map (PROOF.md S4'). A Cartan configuration is U_b = exp(a_bH_1) (one Cartan direction; H_1 = i diag(h_1, …, h_N),
Σh_k = 0); root α = e_i − e_j, q := q_α = h_i − h_j, φ_b := the E_α-coefficient of the fluctuation X_b (U_b → U_be^{X_b}). For a
lattice path γ with steps s (forward on link b, or backward on b): θ_γ := signed line sum of a along γ, θ_{>s} := the same over
the steps after s, and the TRANSPORTED LINE SUM ξ_γ(φ) := Σ_s e^{−iqθ_{>s}}ζ_s, ζ_s := φ_b (forward), −e^{iqa_b}φ_b (backward).
Root-sector covariant gradient (D_Uω)_{x,μ} := e^{−iqa_{x,μ}}ω(x) − ω(x + e_μ). Blocks {LX, …, LX + L − 1} with roots (centres)
c_X = LX + r, r = (L − 1)/2. avg_T := avg_{σ}avg_{y∈B(X)} over the S4' contours T = T^σ_y of the coarse link. λ̃(K) := |D̂_ℓ(K)|².

**PRE-STATED (session 13).** The statements below are fixed before their proofs are written (FLOW_LOG records the stat of
FLOW.md at this point). Each hypothesis is named; nothing below uses an ARGUED or OPEN item as if proven. Any later change of
a statement is logged as such.

**(X1) Step 1.** S12-1..S12-9 applied, tagged [RFL12-fix]; the plane-wave form factor of 𝔪_n leaves the wall list as (X2).
**(X2) Lemma Cartan-𝔪 (the background tower at Cartan configurations).** Let U be Cartan with every level-j composite (j < n) in
the domain (D' for 𝔪^{S4'}; for 𝔪, the neighbourhood of 1 on which W_♮ is the analytic local maximiser).
(a) 𝔪^{S4'}_n(U) = exp((Q_root^{(n)}a)H_1) EXACTLY, Q_root^{(n)} the abelian composite of §98 (a).
(b) 𝔪(U) is Cartan: on a coarse link, M̄ = diag(m_k), m_k := avg_Te^{ih_kθ_T}, and 𝔪(U) = diag(e^{iφ_k}) with φ the maximiser of
Σ_k|m_k|cos(φ_k − arg m_k) under Σφ_k = 0 (SU(2): φ_k = arg m_k); 𝔪 is odd under a ↦ −a; hence 𝔪_n(U) = exp((Q_root^{(n)}a)H_1 +
O(|a|³)): the linear part is exact and there is NO quadratic part. (The review's "exact" form holds for 𝔪^{S4'}; for the chain
map 𝔪 it holds through second order.)
(c) Plane wave a_{x,1} = εcos(px_2 + ϑ) (other a = 0): for 𝔪^{S4'} exactly, for 𝔪 up to O(ε³), the level-m background is
a^{(m)}_{X,1} = ε_mcos(L^mpX_2 + ϑ_m), other directions 0, with ε_m = ε sin(L^mp/2)/sin(p/2) and ϑ_m = ϑ + p(L^m − 1)/2 (the d∘h part
vanishes identically for this polarisation); with P := ℓp: ε_{n−i}/ε_n = ρ_i(P) := sin(PL^{-i}/2)/sin(P/2), ϑ_{n−i} − ϑ_n =
P(L^{-i} − 1)/2, independent of n; ρ_i ≤ (π/2)L^{-i} on 0 < |P| ≤ π; and ε_n/(εℓ) = (sin(P/2)/(P/2))(1 + O(P²/ℓ²)).
**(X3) Lemma Cartan-T (the exact root-sector linearisation at Cartan backgrounds).** At every Cartan U in the domain of (X2):
(a) chain map: (T(U)φ)(X, μ) = avg_T[N_Tξ_T(φ)]/avg_T[N̄_T], N_T := e^{iψ_i(T)} + e^{−iψ_j(T)}, N̄_T := e^{−iψ_i(T)} + e^{iψ_j(T)},
ψ_k(T) := h_kθ_T − φ_k (φ the W_♮ phases of the coarse link); for SU(2) (h = ±q/2): T(U)φ = avg_T[e^{iqθ_T/2}ξ_T]/avg_T[e^{iqθ_T/2}];
(b) S4' map: T^{S4'}(U)φ = e^{−iqδ̄}ξ_c + f(iqδ̄)avg_T[g(iqδ_T)(ξ_T − e^{−iqδ_T}ξ_c)], ξ_c := ξ_{S_c}, δ_T := θ_T − θ_{S_c}, δ̄ := avg_Tδ_T,
g(z) := z/(1 − e^{−z}), f := 1/g;
(c) covariance, exact: T(U)D_U = D_{U'}ev with U' the coarse Cartan background (root phase φ_i − φ_j, resp. q(θ_{S_c} + δ̄));
(d) both agree to first order: T(U)φ = avg_Tξ_T + (iq/2)Cov_T(θ_T, ξ_T) + O(|a|²); at U = 1 both are Q_root.
**(X4) Proposition SLICE-U (the covariant decomposition at U).** Hypothesis: one-step covariance T_kD^{(k)} = D^{(k+1)}ev at U
(true at Cartan U by (X3) (c)). For ANY maps h_k (level-k 1-forms → level-(k+1) gauge functions) put Q_k := T_k + D^{(k+1)}h_k.
(a) Composites: A^{(n←j)} = Q^{(n←j)} − D^{(n)}h^{(n←j)} with Q^{(n←j)} = Q_{n−1}⋯Q_j (plain product) and h^{(m+1←j)} = ev∘h^{(m←j)} +
h_m∘Q^{(m←j)}. Hence P_nA_j = P_nQ^{(n←j)}, P_nA_jΠ_j^{-1}A_j^*P_n = P_nQ^{(n←j)}Π_j^{-1}Q^{(n←j)*}P_n, and P_nM_U = P_nQ^{(n←0)}: the d∘h
analogue drops out of the whole T-split at every U (at U = 1 with h_k = −h this is §98 (b)).
(b) The transported slice h_{U,k}(φ)(X) := −avg_{σ,y}e^{iqθ_{P}}ξ_{P}(φ), P := P^σ(c_X → y), is local, analytic in the background,
and h_{1,k} = −h; Q_k(1) = Q_str,L.
(c) For the Cartan plane wave of (X2) (c), complex ε_n allowed, with level-(n−i) backgrounds of amplitude ε_nρ_i: ||Q_k|| ≤
L^{-1}exp(C_1|ε_nρ_{n−k}|) for |ε_n| ≤ R_1, C_1, R_1 > 0 depending only on (L, N, q) (operator norm on ℓ² of the level-k root-sector
1-forms, level units, uniform in the torus).
(d) The U = 1 bookkeeping lets the growth in. In the termwise ε-expansion of P_n(U)𝒞_n(U)P_n(U) (𝒞_n = κ^{-1}Σ_{j=1}^nA_jA_j^*,
Π_j = 1), the term ℒ_n := [ε]P_n·(1 − P_n^0)𝒞_n^0(1 − P_n^0)·[ε]P_n (superscript 0: U = 1) equals P_n^0D_1G_nD_1^*P_n^0, G_n :=
Δ_0^{-1}D_0^*𝒞_n^0D_0Δ_0^{-1}, D_1 := [ε]D^{(n)}(U), and ℒ_n ≥ κ^{-1}((n − 1)/8)·P_n^0D_1D_1^*P_n^0 (LONG-n). So ℒ_n grows linearly in n
wherever P_{T,ℓ}(K)D̂_1 ≠ 0, and the second-order T-split vertex is n-uniform (by (X5)) only through cancellations of ℒ_n against
the cross terms; the decomposition with D^{(n)}(U) organises them exactly. Also termwise first-order pieces such as
[ε]P_n·(1 − P_n^0)s_i^0P_n^0 decay only like L^{-i}, not L^{-2i}.
**(X5) Proposition VC-T1 ((T-a1) for the 𝒞-part: the level-transverse symbols at the Cartan plane wave converge at L^{-2n}).**
Hypotheses: SU(N), root α, the chain map 𝔪 (or 𝔪^{S4'}); (Π-loc) Π_{k+1}(U) = Π(M̄_c(B_k)) is a per-link multiplication operator
in the root sector, analytic in the background, Π(1) = 1; 𝒞_n(U) := κ^{-1}Σ_{j=1}^nA_jΠ_j^{-1}A_j^*. Let U be the Cartan plane wave of
(X2) (c), parametrised by the level-n linear amplitude ε_n (P, ϑ_n fixed). Then for r = 0, 1, 2:
(a) [ε_n^r](P_n𝒞_nP_n) = κ^{-1}Σ_{i=0}^{n−1}[ε_n^r](P s_i P), with P := P_n(U) and s_i := A^{(i)}Π^{-1}A^{(i)*} (the i-level composite at the
backgrounds of (X2) (c)) both n-INDEPENDENT;
(b) ||[ε_n^r](P s_i P)|| on the sectors below is ≤ C_r(K-sector)L^{-2i}, via P s_i P = P Q^{(i)}Π^{-1}Q^{(i)*}P and
||[ε_n^r]Q^{(i)}|| ≤ C'_rL^{-i} (C'_r = C'_r(L, N, q), uniform in P, ϑ_n and the torus);
(c) **Lemma P-poles ((T-a2) at orders 1 and 2).** On a level-n momentum sector {K + tP : t ∈ Z} avoiding 2πZ⁴, P_n(U) is
real-analytic in ε_n near 0; λ̃(K)λ̃(K + P)·[ε_n]P_n(K + P ← K) is a trigonometric polynomial in (K, P) (times e^{iϑ_n}), and
N_r(K)·[ε_n^r]P_n(K + sP ← K) is one for r ≤ 2, |s| ≤ r, N_r(K) := Π_{|t|≤r}λ̃(K + tP)^{r+1}; P_{T,ℓ} itself (r = 0) is bounded but
non-analytic at K = 0;
(d) hence sup_K Ñ_r(K)|[ε_n^r](P_n𝒞_nP_n)(K + sP, K) − [ε_n^r](P_∞𝒞_∞P_∞)(K + sP, K)| ≤ C_rL^{-2n}, Ñ_r := N_r², uniformly in K
(on sectors avoiding 0): the VC-T0 rate holds away from U = 1 for the 𝒞-part, λ̃-normalised, at first and second order.
The M-part P_nM_UH_⊥(U)^{-1}P_⊥M_U^*P_n = P_nQ^{(n←0)}H_⊥^{-1}P_⊥Q^{(n←0)*}P_n (by (X4) (a)) is NOT covered by (X5): its convergence
(T-a1-M) needs the fine H_⊥(U)^{-1} expansion and is filed with (T-b) (OPEN).
**(X6) Target.** The remaining UNIV list after (X2)-(X5).

**Check f16** (criteria file first, its stat into FLOW_LOG before any f16 script; jobs < 20 min, < 1 GB, memory free ≥ 35%, load
< 8 at start). Part A (4D, coarse side 3, fine side 9; SU(2) and SU(3) with h̄_α ≠ 0; Cartan plane wave): (A1) 𝔪^{S4'}(U) =
exp((Q_roota)H_1) ≤ 1e-12; the chain 𝔪(U) Cartan (off-diagonal ≤ 1e-13), odd in ε (≤ 1e-12 relative), its deviation from the
linear form cubic (ratio of deviations at ε and ε/2 in [7, 9]); (A2) the (X3) (a), (b) closed forms against central finite
differences of the nonlinear maps (random root-sector φ) ≤ 1e-7 relative; control: the chain map with the weights N_T/avg N̄_T
replaced by 1 fails (≥ 1e-3); (A3) (X3) (c) ≤ 1e-12; (X3) (d): the chain/S4' difference halves twice (ratio in [3, 5]) when ε
halves. Part B (SU(2), q = 1, chain map, Π = 1, κ = 1; levels b = n − 2 → n − 1 → n on level-n torus (3, 3, 2, 2); bottom background
a plane wave in direction 1 with momentum along 2, level-n momentum P = 2π/3, exact Cartan images above; coefficients [ε], [ε²]
by Richardson-extrapolated central differences; all norms on the level-n momentum sectors (K_1, K_3, K_4) ≠ 0): (B1)
A^{(2)} = Q^{(2)} − D^{(n)}h^{(2)} and P_n(U)A^{(i)} = P_n(U)Q^{(i)} (i = 1, 2) ≤ 1e-11, T(U)D = D'ev ≤ 1e-12; (B2) decay: for r = 1, 2,
c_r(i) := ||[ε^r](P s_iP)||, ratio c_r(2)/c_r(1) ≤ 0.25; ||[ε^r]Q^{(2)}||/||[ε^r]Q^{(1)}|| ≤ 0.5; (B3) control (U = 1 bookkeeping):
ℒ^{(i)} := [ε]P(1 − P^0)s_i^0(1 − P^0)[ε]P obeys ℒ^{(i)} − (1/8)P^0D_1D_1^*P^0 ≥ −1e-10 (i = 1, 2) and ||ℒ^{(2)}||/||ℒ^{(1)}|| ≥ 0.5
(no decay); (B4) Lemma P-poles at first order: λ̃(K)λ̃(K + P)[ε]P_n(K + P ← K) against its closed form ≤ 1e-7.

**Failure modes (each a valid outcome).** (S13-F1) (A1) fails (the tower is not as stated); (S13-F2) (A2) or (A3) fails (the
closed forms or the covariance are wrong); (S13-F3) (B1) fails (the decomposition algebra is wrong); (S13-F4) (B2) fails (no
L^{-2i} decay of the transverse coefficients: VC-T1 false or not visible at i ≤ 2); (S13-F5) (B3) fails (the leak bound or its
non-decay is wrong); (S13-F6) (B4) fails.

---
# Session-13 proofs (written after §103, the [RFL12-fix] edits and the f16 run)

## 104. Lemma Cartan-𝔪 (the background tower at Cartan configurations): PROVEN-HERE

Statement: §103 (X2).
*Proof.* (a) At a Cartan U every contour transporter is a product of commuting exponentials: T = exp(θ_TH_1), θ_T the signed
line sum. So S_c^{-1}T = exp(δ_TH_1), δ_T := θ_T − θ_{S_c}, with eigenvalues e^{ih_kδ_T}. On D' (||S_c^{-1}T − 1|| < 1) every
|h_kδ_T| < π/3 < π, so the principal log is δ_TH_1 and the S4' average is δ̄H_1. Hence U' = exp(θ_{S_c}H_1)exp(δ̄H_1) =
exp((avg_Tθ_T)H_1), and avg_Tθ_T = (Q_roota)(X, μ) by the definition of the root map (LINEAR_PACKAGE §1.2: the contour average
of line integrals). U' is again Cartan; induction on the level gives 𝔪^{S4'}_n(U) = exp((Q_root^{(n)}a)H_1).
(b) M̄ = avg_Texp(θ_TH_1) = diag(m_k). For t in the maximal torus 𝕋, Re tr((tVt^{-1})^{-1}tMt^{-1}) = Re tr(V^{-1}M), so the unique
local maximiser obeys W_♮(tMt^{-1}) = tW_♮(M)t^{-1}. M̄ commutes with 𝕋, so W_♮(M̄) lies in the centraliser of 𝕋 in SU(N), which is
𝕋: W_♮(M̄) = diag(e^{iφ_k}), Σφ_k ∈ 2πZ (φ → 0 as a → 0), and Re tr(diag(e^{−iφ_k})M̄) = Σ|m_k|cos(arg m_k − φ_k). Oddness: H_1 =
i·(real diagonal), so a ↦ −a sends U ↦ Ū, M̄ ↦ conj(M̄), and W_♮(M̄‾) = conj(W_♮(M̄)) (FLOW §30 (C3)); hence φ ↦ −φ. The
derivative of 𝔪 at 1 is Q_root (LINEAR_PACKAGE §1.2: both averagings share the linearisation), so on Cartan arguments
φ = h·(Q_roota) + O(|a|²), and oddness removes the O(|a|²) term. Induction: if 𝔪_j(U) = exp((Q_root^{(j)}a)H_1 + c_j(a)) with
c_j = O(|a|³), then 𝔪_{j+1} = exp(Q_root(Q_root^{(j)}a + c_j)H_1 + O(|a|³)) = exp((Q_root^{(j+1)}a)H_1 + O(|a|³)).
(c) For A_1(x) = e^{ipx_2} (other components 0), Q_str gives L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_1(y + je_1) = L·L^{-1}Σ_{|s|≤r}e^{ip(c_2+s)} =
(sin(Lp/2)/sin(p/2))e^{ip(LX_2 + r)}, only in direction 1. The slice functional vanishes: the only leg of P^σ(c_X → y) that sees
A_1 is the direction-1 leg, which contributes (y_1 − c_1)e^{ipx_2} with x_2 ∈ {c_2, y_2} fixed by σ and independent of y_1; the
average over y_1 ∈ c_1 + {−r..r} kills it. So Q_root = Q_str on this wave, and the image is a wave of the same type with amplitude
factor sin(Lp/2)/sin(p/2), momentum Lp and phase shift pr. Taking real parts and iterating (the factors telescope:
Π_{j<m}sin(L^{j+1}p/2)/sin(L^jp/2) = sin(L^mp/2)/sin(p/2), phases Σ_jL^jpr = p(L^m − 1)/2) gives (c) for 𝔪^{S4'} exactly, and for 𝔪
up to O(ε³) by (b). The ratios ρ_i and phase differences are as stated (substitute p = P/ℓ). |sin x| ≤ |x| and |sin(P/2)| ≥ |P|/π on
|P| ≤ π give ρ_i ≤ (π/2)L^{-i}. Finally ε_n/(εℓ) = sin(P/2)/(ℓ sin(P/2ℓ)), and ℓ sin(P/2ℓ) = (P/2)(1 + O(P²/ℓ²)). ∎
*Reading.* (1) REVIEW_FLOW_S12 §5 (1)'s "exact" form factor is exact for 𝔪^{S4'}. For the chain map 𝔪 = W_♮∘M̄ of FLOW it is exact
through second order, which is all the vertex data use. (2) f16 A1 checks this. 𝔪^{S4'} = exp(Q_root aH_1) to 4.4e-15 / 5.0e-15, and
the tower formula to 7.6e-15. The chain map is exactly diagonal and odd, with a deviation from linear that is cubic (ratios 8.06,
8.09). Part B checks the level-(n−1) image (2.6e-8 at ε = 0.04, consistent with ε³).

## 105. Lemma Cartan-T (the exact root-sector linearisation at Cartan backgrounds): PROVEN-HERE

Statement: §103 (X3).
*Proof.* Contour derivative. Write the contour as a product of steps V_s: V_s = U_b forward and U_b^{-1} backward. Then
U_b → U_be^{tX_b} sends V_s ↦ V_se^{tZ_s}, with Z_s = X_b (forward) and Z_s = −Ad(U_b)X_b (backward). So
ΠV_se^{tZ_s} = (ΠV_s)exp(tΣ_sAd(R_s^{-1})Z_s + O(t²)), R_s := the product after s. At Cartan U, Ad(exp(cH_1))e_{ij} = e^{iqc}e_{ij},
so the E_α-coefficient is ξ_T(φ).
(a) First order of M̄: M̄ + tE, with E_{ij} = avg_Te^{ih_iθ_T}ξ_T and E_{ji} = −avg_Te^{ih_jθ_T}ξ̄_T. W_♮ is analytic (§30, implicit
function theorem). Write W_♮(M̄ + tE) = W_0e^{tZ}, Z = ze_{ij} − z̄e_{ji} (the root sectors decouple by torus equivariance).
Stationarity says the anti-hermitian part of V^{-1}M is central. At first order its (ij) entry gives
e^{−iφ_i}E_{ij} − zr_j − e^{iφ_j}Ē_{ji} − zr̄_i = 0, with r_k := e^{−iφ_k}m_k = avg_Te^{iψ_k(T)}. This reads z·avg_TN̄_T = avg_TN_Tξ_T, and
avg N̄ → 2 as a → 0. For SU(2), h = ±q/2 and φ_2 = −φ_1 give N_T = 2e^{i(qθ_T/2 − φ_1)} and N̄_T = 2e^{−i(qθ_T/2 − φ_1)}; with
e^{iφ_1} = m_1/|m_1|, z = avg[e^{iqθ_T/2}ξ_T]/avg[e^{iqθ_T/2}].
(b) S_c(t)^{-1}T(t) = e^{−tξ_c}Ge^{tξ_T} = G·exp(t(ξ_T − Ad(G^{-1})ξ_c)) + O(t²), G = exp(δ_TH_1), whose E_α-part is ξ_T − e^{−iqδ_T}ξ_c.
From d/dt exp(Y + tW) = exp(Y)·((1 − e^{−ad_Y})/ad_Y)W one gets d/dt log(Ge^{tZ}) = g(ad_Y)Z, Y = δ_TH_1, and ad_Y = iqδ_T on E_α. So
X̄(t) = δ̄H_1 + tΞ, Ξ = avg_Tg(iqδ_T)(ξ_T − e^{−iqδ_T}ξ_c). Then U'(t) = S_ce^{tξ_c}exp(δ̄H_1 + tΞ) =
S_cexp(δ̄H_1)·exp(t e^{−iqδ̄}ξ_c)·exp(t f(iqδ̄)Ξ) + O(t²), which is (b).
(c) For φ = D_Uω the transported sum telescopes: ξ_γ(D_Uω) = e^{−iqθ_γ}ω(start) − ω(end).
  - Chain: N_Te^{−iqθ_T} = e^{−i(φ_i − φ_j)}N̄_T (direct, from ψ_i − qθ = ψ_j + φ_j − φ_i and −ψ_j − qθ = −ψ_i − φ_i + φ_j). So
    z = e^{−i(φ_i − φ_j)}ω(c_X) − ω(c_Y).
  - S4': ξ_T − e^{−iqδ_T}ξ_c = −(1 − e^{−iqδ_T})ω(c_Y), so the average of g(·)(·) is −iqδ̄ω(c_Y), and f(iqδ̄)(−iqδ̄ω_Y) =
    −(1 − e^{−iqδ̄})ω_Y. Adding e^{−iqδ̄}ξ_c gives e^{−iq(θ_{S_c} + δ̄)}ω(c_X) − ω(c_Y).
(d) Chain: φ_k = h_kavg θ + O(|a|³) by §104 (b). So ψ_k(T) = h_k(θ_T − θ̄) + O(|a|³), N_T = 2 + iq(θ_T − θ̄) + O(a²) and
avg N̄ = 2 + O(a²), giving z = avg ξ + (iq/2)Cov_T(θ, ξ) + O(a²). S4': expanding e^{−iqδ̄}, f, g, e^{−iqδ_T} to first order, the ξ_c
terms cancel, giving avg ξ + (iq/2)(avg[δξ] − δ̄avg ξ). The covariance is shift-invariant, so Cov(δ, ξ) = Cov(θ, ξ). ∎
*Reading.* f16 A2 (finite differences of the nonlinear maps, t = 1e-5): chain 2.4e-10, 2.7e-10, 2.8e-10; S4' 7.0e-10, 7.6e-10,
7.7e-10 (SU(2); SU(3) roots (1,2), (1,3) with h̄ ≠ 0). The naive average fails (7e-2 … 9e-2). A3: covariance to ≤ 2.6e-14; the
chain/S4' difference is second order (ratios 3.97, 4.03, 3.98).

## 106. Proposition SLICE-U (the covariant decomposition at U): PROVEN-HERE ((a)-(d)); one clause of (d) withdrawn

Statement: §103 (X4).
*Proof.* (a) Q_kD^{(k)} = T_kD^{(k)} + D^{(k+1)}h_kD^{(k)} = D^{(k+1)}(ev + h_kD^{(k)}). Induction on m, with A^{(m←j)} = Q^{(m)} − D^{(m)}h^{(m)}:
  A^{(m+1←j)} = (Q_m − D^{(m+1)}h_m)(Q^{(m)} − D^{(m)}h^{(m)})
  = Q_mQ^{(m)} − D^{(m+1)}[(ev + h_mD^{(m)})h^{(m)} + h_mQ^{(m)} − h_mD^{(m)}h^{(m)}]
  = Q_mQ^{(m)} − D^{(m+1)}[ev h^{(m)} + h_mQ^{(m)}].
P_nD^{(n)} = 0 gives the projected identities, and M_U = A^{(n←0)}.
(b) h_U is built from the paths P^σ(c_X → y), which lie in the box c_X + [−1, 1]⁴, so it is local. Its coefficients are
exponentials of line sums, so it is analytic. At U = 1 its coefficients are ±1 with the orientation, so h_{1,k} = −h. With
D_{U'}(1) = −d: Q_k(1) = Q_root + dh = Q_str (LINEAR_PACKAGE §1.2).
(c) Every entry of Q_k(U) − Q_str is an analytic function of the ≤ 648 background link values in the box of its coarse link, and
it vanishes at a = 0. Analyticity holds on a polydisc |a_b| ≤ η_0(L, N, q):
  - SU(2): the denominator avg e^{iqθ_T/2} stays ≥ 1/2 there, since contours have ≤ 11 steps;
  - SU(N): W_♮'s phases continue holomorphically by the implicit function theorem.
By the Schwarz lemma each entry is bounded by C_2η, η := max_box|a_b|.
  - The Schur test with the box incidence (row and column sums ≤ 648) gives ||Q_k − Q_str|| ≤ 648C_2η.
  - ||Q_str,L|| ≤ L^{-1} (Schur, nonnegative entries, §98).
  - For the plane wave, |a_b| ≤ |ε_nρ_{n−k}| for complex ε_n, since cos has a real argument.
So ||Q_k|| ≤ L^{-1} + C_3|ε_nρ| ≤ L^{-1}exp(LC_3|ε_nρ|). This is uniform in the torus (all constants are local).
(d) Differentiating P_n(U)D^{(n)}(U) = 0 gives [ε]P_n·D_0 = −P_n^0D_1. Since 1 − P_n^0 = D_0Δ_0^+D_0^*:
ℒ_n = [ε]P_nD_0Δ_0^+D_0^*𝒞_n^0D_0Δ_0^+D_0^*[ε]P_n = P_n^0D_1G_nD_1^*P_n^0 ([ε]P_n is hermitian).
G_n is diagonal in K with value ⟨D̂, 𝒞̂_n^0D̂⟩/λ̃² = ⟨V, 𝒞̂_n^0V⟩/λ̃ ≥ κ^{-1}[1 + (n − 1)λ̃/8]/λ̃ ≥ κ^{-1}(n − 1)/8 for K ∉ 2πZ⁴ (Proposition
LONG-n; its alias identity |d_jψ|² = 8 holds on every torus with L^i ≥ 2). On a sector avoiding 0, D_1^*P_n^0 maps into momenta
K ∓ P of the same sector. So ℒ_n ≥ κ^{-1}((n − 1)/8)P_n^0D_1D_1^*P_n^0.
Explicitly, P^0(K)D_1(K ← K ∓ P) = β_∓P_{T,ℓ}(K)e_1, |β_∓| = |q|·|[ε]ε_n|/2. So on the K-diagonal ℒ_n grows at least like
κ^{-1}((n − 1)/8)(q²|[ε]ε_n|²/2)(1 − |D̂_ℓ(K)_1|²/λ̃(K)), which is positive unless K ∥ e_1. By §107 the full second-order transverse
coefficient converges, so ℒ_n is cancelled by the cross terms of the termwise expansion. ∎
**Statement change (logged).** The last sentence of (X4) (d) ("termwise first-order pieces such as [ε]P_n(1 − P_n^0)s_i^0P_n^0 decay
only like L^{-i}") is WITHDRAWN. The proof gives only an upper bound O(L^{-i}), from one Q factor and one D_0h factor. f16 does not
show L^{-i} decay at i ≤ 2: on the official torus the piece vanishes (8e-16, 2e-14), and on the (3, 3, 2, 1) smoke torus it is
1.99e-2 → 2.46e-3 (ratio 0.12).
*Reading.*
(1) What is load-bearing is the gradient AT U in front of the slice. The slice functional itself can be any local analytic family
with h_{1,k} = −h. The transported slice, or a background-covariant box-Coulomb slice of the type of BFT_B's S_E (§15; S_E itself
is set at the trivial chain), both qualify. The covariant choice is what would give flux-type bounds at U_f (ARGUED, not used).
(2) f16 B1 checks A^{(2)} = Q^{(2)} − D^{(n)}h^{(2)} to 1.8e-14 and P(A^{(i)} − Q^{(i)}) to ≤ 9.5e-15, with covariance to 2.1e-14.
(3) f16 B3 / add-B3 checks the leak: ℒ^{(1)}, ℒ^{(2)} have norms 3.51 and 3.39 (ratio 0.966, no decay), and
ℒ − P^0D_1D_1^*P^0/8 ≥ −3e-16 at δ ≤ 0.002.
(4) With the U = 1 pairing, the data [ε]A^{(i)} = [ε]Q'^{(i)} do not decay (2.92 → 2.95). With the pairing at U, [ε]Q^{(i)} decays
(1.16 → 0.387).

## 107. Proposition VC-T1 ((T-a1) for the 𝒞-part at the Cartan plane wave) and Lemma P-poles ((T-a2), orders 1, 2): PROVEN-HERE

Statement: §103 (X5). Hypotheses: as stated. (Π-loc) is a named hypothesis, ARGUED: at diagonal M̄, Π(M̄) is torus-invariant,
hence diagonal in the roots.
*Proof.* (a) For r ≤ 2 the coefficients depend on the backgrounds only through their linear parts: by §104 (b) the quadratic part
vanishes, and by the chain rule a second-order Taylor coefficient sees b^{(1)} and b^{(2)} = 0 only. By §104 (c), in level-n
parametrisation the level-(n − i) background depends only on (i, ε_n, P, ϑ_n), and the level-(n − i) torus has side L^iT. The one-step
maps are the same at every level (the chain is uniform in level units, §30). P_n depends on the level-n background only. Hence
s_i and P are n-independent, and 𝒞_n is the sum over j = n − i, i = 0..n − 1.
(b) Q^{(i)} = Q_{n−1}⋯Q_{n−i}. By §106 (c), for complex |ε_n| ≤ R := η_0/2:
  ||Q^{(i)}(ε_n)|| ≤ L^{-i}exp(LC_3R Σ_{t≥1}ρ_t) ≤ L^{-i}exp(LC_3Rπ/(2(L − 1))).
  - Q^{(i)}(ε̄)^* is the holomorphic extension of Q^{(i)*}.
  - Π^{-1} is bounded and analytic, by (Π-loc).
  - Cauchy's estimate on |ε_n| = R gives ||[ε_n^r]Q^{(i)}|| ≤ C'_rL^{-i} and ||[ε_n^r](Q^{(i)}Π^{-1}Q^{(i)*})|| ≤ C''_rL^{-2i}, with
    C_r = C_r(L, N, q).
  - Since P s_iP = PQ^{(i)}Π^{-1}Q^{(i)*}P (§106 (a)), [ε^r](Ps_iP) = Σ_{r_1+r_2+r_3=r}[ε^{r_1}]P·[ε^{r_2}](QΠ^{-1}Q^*)·[ε^{r_3}]P.
(c) On a sector {K + tP} avoiding 2πZ⁴ (finite on the torus), Δ_0 ≥ μ_K := min_tλ̃(K + tP) > 0. Since Δ(ε) − Δ_0 = O(ε), Δ(ε) is
invertible and P is analytic for |ε| < cμ_K.
  - [ε^r]Δ^{-1} is a sum of products Δ_0^{-1}Δ_{r_1}Δ_0^{-1}⋯Δ_0^{-1}, with ≤ r + 1 diagonal factors 1/λ̃(K + tP), |t| ≤ r. D_r and Δ_r are
    trigonometric polynomials shifting momentum by ≤ rP (expand e^{−iqa}, a = ε_ncos(PX_2 + ϑ_n)).
  - Since P = 1 − DΔ^{-1}D^*, N_r·[ε^r]P is a trigonometric polynomial.
  - At first order only 1/λ̃(K) and 1/λ̃(K + P) occur, through the three terms D_1Δ_0^{-1}D_0^*, D_0Δ_0^{-1}D_1^* and
    D_0Δ_0^{-1}Δ_1Δ_0^{-1}D_0^*. The result is
    λ̃(K)λ̃(K+P)[ε]P(K+P←K) = −[βλ̃(K+P)e_1D̂(K)^† − βλ̃(K)D̂(K+P)e_1^T − Δ_1D̂(K+P)D̂(K)^†],
    with Δ_1 = β(D̂(K+P)_1‾ − D̂(K)_1), β := −iq[ε]ε_ne^{iϑ_n}/2 and D̂(K)_μ := 1 − e^{iK_μ}.
  - P_{T,ℓ} = P^0 has norm 1 but is non-analytic at K = 0.
(d) Each entry (K + sP, K) of the product in (b) is a finite sum over intermediate momenta K + tP, |t| ≤ r ≤ 2.
  - Each [ε^{r_1}]P factor, multiplied by its λ̃-factors (all at |t| ≤ 2), is a bounded trigonometric polynomial; P^0 entries are ≤ 1.
  - The products of the normalisations divide Ñ_r = N_r².
  - So Ñ_r(K)|[ε^r](Ps_iP)(K + sP, K)| ≤ C_rL^{-2i}, uniformly in K and in the torus.
  - Summing over i ≥ n gives sup_KÑ_r(K)|difference| ≤ C_rL^{-2n}. ∎
*Reading.*
(1) **The VC-T0 rate holds away from U = 1 for the 𝒞-part, at first and second order, λ̃-normalised and uniformly in K.** The
growth of LONG-n and (W6) is a D^{(n)}(·)D^{(n)*} term, and it is removed exactly by pairing the slice with D^{(n)}(U).
(2) The M-part (T-a1-M) is not covered. By §106 (a) it is P_nQ^{(n←0)}H_⊥(U)^{-1}P_⊥Q^{(n←0)*}P_n, which is d∘h-free at every U. Its
limit needs the fine H_⊥(U)^{-1} expansion, so it is filed with (T-b) (OPEN).
(3) The degree-4 leading numerator of the limit (the Lemma VC analogue for the vector) is not proved here. Name it (T-a3) (OPEN).
(4) f16 B2 (i = 1 → 2): transverse coefficients c_1 = 0.178 → 0.0188 (ratio 0.106) and c_2 = 0.628 → 0.0678 (ratio 0.108),
against L^{-2} = 0.111. [ε^r]Q^{(i)} ratios are 0.334 and 0.418, against L^{-1}(1 + ρ).
(5) f16 B4 (Lemma P-poles at first order): the finite-difference residual scales like δ⁴: 1.2e-3 (δ = 0.02), 1.2e-7 (0.002),
8.3e-10 (0.0005). The closed form is therefore exact, and the pre-stated δ was too coarse.

## 108. (W4) addendum: the W_n half of LONG-n (the [RFL12-fix S12-2] Schur argument)

At U = 1 and a level momentum K ≠ 0, write Y = Y_n(K) in the frame (V, ker D̂^†). Then (Y^{-1})_{VV} = 1/(Y_VV − Y_VTY_TT^{-1}Y_TV).
- Y_TT = Ỹ_n ≥ κ^{-1}P_n (the j = n term), so ||Y_TT^{-1}|| ≤ κ.
- In Y_VT = Σ_jV^*A_jA_j^*P_n + V^*M(P_T/λ)M^*P_n, the j-terms equal V^*(Q_str^{(L^i)} − d_n∘h^{(i)})Q_str^{(L^i)*}P_n. Their norms are
  ≤ L^{-2i} + ||h^{(i)}||L^{-i}, with ||h^{(i)}|| ≤ Σ_j||h_j||L^{-j} bounded. The M-term is finite at fixed K (x^{blk} ~ |K|^{-2}). So
  |Y_VT| ≤ C(K).
By LONG-n, W_n(K) = (Y^{-1})_{VV} ≤ 1/(κ^{-1}[1 + (n − 1)λ̃(K)/8] − κC(K)²) → 0, and log W_n(K) ≤ −log n + O_K(1). Together with
W_n ≥ 1/⟨V, YV⟩ this proves the W_n half. It is counted with LONG-n, not as a new item.

## 109. Session-13 check f16 (ADDED AFTER the run; checks/f16_criteria.md, f16_cartan_slice.py, f16_out.txt, f16_time.txt)

**Timeline and run conditions**
- Criteria written 11:39:15 UTC, before any f16 script (stat in FLOW_LOG).
- Three smoke runs, logged in FLOW_LOG:
  - one was interrupted by a session pause;
  - one hit an accumulator assertion and an instrument defect in B1;
  - one, on the (3, 3, 2, 1) torus, exceeded the 1 GB limit at 1.03 GB.
- Deviations decided before the official run:
  - Part B on the level-n torus (3, 3, 1, 1) instead of (3, 3, 2, 2), for memory;
  - two ADDENDUM passes, NOT pre-stated, at δ = 0.002 and 0.0005.
- Script: birth = mtime 11:54:59 UTC, 25561 B, md5 7c81a91bfff45189e025be6b22547cca.
- Official run: one NUMERIC LOCK acquisition, 11:55:17-11:56:22 UTC, load 3.03, memory free 38%, nice 10, 1 thread; 65.4 s,
  peak RSS 548 MB.

**Results: PRE-STATED verdicts 19/21 PASS; addendum 9/10 PASS.**
- **Part A: 16/16 PASS** (SU(2); SU(3), two roots).
- **Part B (δ = 0.02):**
  - B1, B2 (r = 1, 2): PASS.
  - **B3 FAIL** (λ_min −2.9e-9 against the pre-stated −1e-10).
  - **B4 FAIL** (1.2e-3 against 1e-7).
  - Both failures are finite-difference truncation. The level-n field is ≈ 7.5ε, so the step in the field is 0.15. The
    addendum shows it:
    - B3 passes at δ ≤ 0.002, at −3e-16;
    - B4 is 1.2e-7 at δ = 0.002, just over the 1e-7 threshold, so add1-B4 FAILs;
    - B4 is 8.3e-10 at δ = 0.0005, which PASSes;
    - the δ⁴ scaling identifies the residual as truncation.
  - B3's non-decay part (ratio 0.966 ≥ 0.5) passes at every δ.

**Reading.**
(1) S13-F1, F2, F3, F4 do not occur. The pre-stated F5 (B3) and F6 (B4) lines FAIL as recorded. The addendum attributes both to the
pre-stated finite-difference step, not to the statements.
(2) The level-transverse 𝒞 coefficients decay at ≈ L^{-2} per level at first and second order. The U = 1 bookkeeping term does not
decay.
(3) Limits:
  - only i ≤ 2;
  - one small torus (only sectors K_1 ≠ 0, no small K);
  - SU(2) only in Part B.

## 110. Session-13 outcomes, the remaining UNIV list, tally (ADDED AFTER the derivations and the check)

**Outcomes**
- (X1) DONE: S12-1..S12-9 applied, tagged [RFL12-fix].
- (X2) Lemma Cartan-𝔪: PROVEN.
- (X3) Lemma Cartan-T: PROVEN.
- (X4) Proposition SLICE-U: PROVEN (a)-(d), with the L^{-i} clause of (d) withdrawn.
- (X5) Proposition VC-T1 and Lemma P-poles: PROVEN, for the 𝒞-part, orders ≤ 2, given (Π-loc).

**Remaining items for the vector (UIR)/(V-IR)**
- (L-loc2) [ARGUED].
- (T-a1-M): the M-part convergence, filed with (T-b) [OPEN].
- (T-a3): the leading degree-4 numerator of the T-split limit [OPEN].
- (Π-loc) [ARGUED].
- (T-b) [OPEN].
- (T-c) [OPEN].
- Unchanged: the rate items (s1), (s2⊥) and c'(φ) → c'_0; (COV-GI) at non-critical backgrounds; FI-1; HIST's restatement of
  CL^J's Setting.
- Off the list now: the plane-wave form factor of 𝔪_n (§104) and the background dependence of P_k at orders 1, 2 (§107 (c)).

**Theorem UNIV for SU(N) does NOT yet rest only on (L-loc2).**

**Tally (session-13 items unreviewed)**
- PROVEN-HERE: 70 (confirmed by REVIEW_FLOW_S12; strict 66) + 5 = **75**: Cartan-𝔪, Cartan-T, SLICE-U, VC-T1, P-poles.
- Strict: 66 + 4 = **70**, with P-poles folded into VC-T1.
- IMPORTED-AND-REVERIFIED: unchanged (L4b; the Lévy CLT).
- ARGUED, not counted: (L-loc2); (W6); (Π-loc); the flux-type bound for the covariant slice at U_f; DEF-red.
- OPEN: (T-a1-M), (T-a3), (T-b), (T-c), (L-loc2) [s], and the rate and cross-lane items.
