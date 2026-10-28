# YM4D existence from UV stability: a conditional lemma DAG (sessions 1-2, 2026-10-27)

Lane: layer 2 of the 4D Yang-Mills construction. Layer 1 (UV stability, Balaban's RG) is the sister lane
`../ym4d-proof/` (read-only here; cited as **P**, with P's lemma names). Nothing here is a PR, a CL entry or an axiom
edit. Literature tags are in NOTES.md. The session record is in LOG.md.

**Status legend** (same as P):
- **PROVEN-HERE**: the complete argument is written in this file. "PROVEN-HERE | H" means it is a proven implication
  from the named hypothesis H.
- **IMPORTED-AND-REVERIFIED**: exact source; the load-bearing step re-derived or re-checked on our setting.
- **IMPORTED-NOT-YET-REVERIFIED**: a named obligation. It never supports a PROVEN claim except as an explicit hypothesis.
- **OPEN**: the missing estimate is stated.
- **ARGUED**: a heuristic or perturbative reason, uncounted.
- **STANDARD**: a textbook theorem of analysis/topology used as a tool (Banach-Alaoglu, Riesz, Montel, Minlos,
  continuous mapping theorem, uniqueness of positive roots). Uncounted; named where used.

---

## 0. Summary

**Main finding (structural).** The theorem Balaban published, Z-stability (H-Bal-2 below), is not used anywhere in
the conditional theorem. Every non-soft conclusion uses instead the *inductive content* of his proof: the
representation of the **law of the block variables at a physical scale** (H-Bal-3), plus the coupling flow
(H-Bal-1). What compactness gives for free, and what each extra hypothesis buys:

| Part | Delivered | From |
|---|---|---|
| (a) subsequential continuum limits, finite volume | **YES**: a single limit state ω on a separable commutative C*-algebra containing every block observable (all resolutions, all L-adic shifts) and every flowed lattice Wilson loop; consistent across resolutions | compactness alone (X-ALG, X-CONS), with the **continuous** block map X-S4c |
| (b) OS structure | **RP** for every L-adic block-boundary plane, **L-adic translations**, hypercubic symmetry, gauge invariance; on R×T³: OS Hilbert space, positive contraction semigroup T(s) = T(2)^{s/2}, **Hamiltonian H ≥ 0 on (ker T)^⊥** | lattice RP (Osterwalder-Seiler, re-verified) + compactness (X-RP, X-OS) |
| (b) not delivered | time continuity (ker T = 0), rotation invariance (OS1), OS0 for local fields | need H-cont, H-rot, H-src (OPEN; not in Balaban). Session 2: ker T ⊥ everything supported off the plane (X-KER); two-grid laws = one resolution's law + one two-grid step (X-2GRID); estimate proven in the free Gaussian model (X-CONT-G); interacting case ⇐ H-corr + H-lin (ARGUED). Sources: separated-support correlations of the action density bounded **| H-Bal-loc** (X-SRC-CT, X-SRC-RED) |
| (c) non-triviality | **weak form YES | H-Bal-3**: at every resolution the limit block law is neither flat nor Haar, and on small fields it has a density of Balaban's form with an analytic effective action; Taylor coefficients of order n are O(g^n) | X-ND, X-MONTEL, X-CAUCHY |
| (c) asymptotic freedom (session 2) | **two-sided, volume-uniform**: (δ_*/2)/(1/g² + β'm log L) ≤ ω(1 - P_{p,m}) ≤ φ(G_m), so block plaquettes approach the free value logarithmically in the scale (not dilation invariant, no power law) | X-NTAF, X-NTAF-AF **| H-Bal-1, H-Bal-3L, H-Bal-3T** (§10.1) |
| (c) not delivered | non-Gaussianity (connected 4-point ≠ 0); the sharp coefficient c_blk g_m² with g_m² ~ 1/(2b_0 m log L) | OPEN (X-NT2; X-NTAF-sharp: walls W-AF1 flow coefficient, W-AF2 = H-corr) |
| (d) infinite volume | limit points exist with all of (b)'s soft structure; non-degeneracy **| H-Bal-3G** (volume-uniform Gibbs/finite-energy form) | X-IV, X-IVND |
| (d) not delivered | uniqueness, clustering (OS4), mass gap, rotation invariance via universality | OPEN (IR; need a gap or cluster expansion) |

**Tally (session 2): PROVEN-HERE 24 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 7 (hypotheses H-Bal-1, -2,
-3, -3G, -3L, -3T, -loc) / OPEN 11.** (Session 1: 16 / 1 / 4 / 9.) Itemised in §6. Session-2 work is §9 (pre-stated
targets) and §10 (results); the reader's trust list is §10.4.

---

## 1. Setting (fixed)

- **ES1 (lattice).** L odd (CMP 109 (0.1) takes L odd and large; P transcribes "> 11"). K ∈ N, ε = L^{-K}.
  Physical units: the resolution-0 (unit) lattice has spacing 1. Fine torus Λ_K = (εZ / ℓZ)^4 with ℓ = 4L^M
  (time side ℓ_0 may differ, also a multiple of 4; P's convention [S4]). Resolution-m coarse lattice
  Λ_m = (L^{-m}Z / ℓZ)^4 for 0 ≤ m ≤ K. **For fixed m and fixed ℓ, Λ_m is a finite lattice independent of K.**
  Balaban's step index is k = K - m (k counts steps from the fine lattice; CMP 109 p.255-256).
- **ES2 (measure).** G = SU(N), N ≥ 2. μ_K = Z_K^{-1} exp(-(2N/g_0²) Σ_p (1 - N^{-1} Re tr U_p)) Π_b dU_b (Haar).
  Config space Ω_K = G^{links(Λ_K)}, compact.
- **ES3 (tuning).** g_0 = g_0(ε, g), the bare coupling of H-Bal-1 with renormalised coupling g at the unit scale.
  (Not P's S5' renormalisation condition; the tuning is part of the hypothesis.)
- **ES4 (block map).** The continuous averaging map S4c of Lemma X-S4c, iterated: V^(m)_K := A^{K-m}(U) ∈
  C_m := G^{links(Λ_m)}. On small fields it equals P's S4' and Balaban's (0.4) with diagonal pairing (P, B-avg,
  check c17(B)). Shifted grids: for a ∈ D := ∪_m L^{-m}Z^4 (the L-adic translations), V^(m)_{K,a} is the same map on
  the grid translated by a (defined for K ≥ m(a), the level of a).
- **ES5 (observables).**
  - **O^blk** (block observables): f(V^(m)_{K,a}|_X), f ∈ C(C_m(X)) gauge-invariant under coarse gauge
    transformations, X a finite union of resolution-m blocks. Includes Wilson loops *of the block variables*
    ("smoothed Wilson loops" in the sense of Magnen-Rivasseau-Sénéor, NOTES §2).
  - **O^flow** (flowed lattice Wilson loops): W_{t,γ}(U) = N^{-1} Re tr Hol_{V_τ(U)}(γ), γ a closed loop of the
    resolution-m coarse graph (refined to fine straight segments), V_τ the Wilson flow (Lüscher (1.4), NOTES §4) at
    lattice flow time τ = t/ε², t ∈ Q_{>0} physical.
  - **O^raw** (raw lattice Wilson loops of physical size): excluded, see X-RAW.
  - **Unbounded fields** (smeared composites, flowed energy density): only in §4 (OS0).
- **ES6 = Lemma X-PLANES (reflections; PROVEN-HERE).** P_m := {x_μ = (j + ½)L^{-m}} (resolution-m block-boundary hyperplanes; link mid-planes of
  every finer lattice). Since L is odd, (j + ½)L^{-m} = ((jL + (L-1)/2) + ½)L^{-m-1}, so **P_m ⊂ P_{m+1}**;
  P := ∪_m P_m is dense in each coordinate.

---

## 2. The hypothesis H-Bal (exact form used; every quantifier explicit)

Sources: CMP 109 [read by P, NOTES §1 here]; CMP 102, 116, 119, 122 I-II [not-read; abstracts/Crossref only].
Everything below is **[unverified-exact-statement]** except where marked as transcribed from CMP 109.

**H-Bal-1 (coupling flow). IMPORTED-NOT-YET-REVERIFIED.** (CMP 109 Theorem 2 and (0.31), transcribed by P; stated
for SU(2), "superficial" for SU(N); its proof is deferred by Balaban to "a separate paper".)
There are γ > 0, g_1 > 0 and 0 < β ≤ β' such that for every g ∈ (0, g_1] and every K ≥ 0 there is a bare coupling
g_0(ε, g) for which the effective couplings satisfy g_k ∈ (0, γ] for k = 0, ..., K, g_K = g, and
1/g² + β(K - k) log L ≤ 1/g_k² ≤ 1/g² + β'(K - k) log L.
- Consequence used below: at a fixed physical resolution m (k = K - m), g_{m,K} := g_{K-m} lies in
  [(1/g² + β' m log L)^{-1/2}, γ], a compact subinterval of (0, γ], **independent of K**.

**H-Bal-2 (UV stability of Z). IMPORTED-NOT-YET-REVERIFIED.** (CMP 122 II, per its OSTI abstract "completing the
proof of the ultraviolet stability of four-dimensional pure gauge field theories" [read-abs, via P].)
For g ≤ g_1 and g_0 = g_0(ε, g): there are E_± = E_±(g, L, N) < ∞, **independent of K and of M**, such that
e^{-E_-|T|} ≤ Z_K / 𝒩_K ≤ e^{E_+|T|}, |T| = ℓ^4 the physical volume, 𝒩_K an explicit normalisation (products of
the Gaussian and Faddeev-Popov normalisations of the steps (0.17); exact form unverified).
- Quantifier status: CMP 109 (0.1) allows the torus side 2L^m (any m) in unit-lattice units, so nothing in the
  small-field theorem restricts the physical volume (P, L6 [S6]); whether the full theorem is uniform in M is
  unverified.

**H-Bal-3 (block-variable laws at every scale; the inductive content). IMPORTED-NOT-YET-REVERIFIED.**
(Small-field form: CMP 109 Theorems 1/3, (0.22)-(0.29), (1.18), transcribed by P; its inductive step is completed in
CMP 116 [not-read]. Large-field part: the R-operation of CMP 122 I-II [abstracts only]. Background field: CMP 102
Theorem 1 [second-hand].) Fix m and put k = K - m, η = L^{-k}. Let ν_{K,m} be the law of V^(m)_K on C_m (finite
dimensional), ρ_{K,m} its density with respect to Haar measure on C_m, and
R_m(ε_0) := {V ∈ C_m : |V(∂p') - 1| < ε_0 for every coarse plaquette p'} (Balaban's coarse regularity condition,
CMP 109 p.259). There are ε_0, E_0, κ > 0, α > 0, η_0 ∈ (0,1) and C_A < ∞, **independent of K**, such that for all
K ≥ m:
- **(3a) small-field density.** On R_m(ε_0):
  ρ_{K,m}(V) = 𝒵_{K,m}^{-1} exp(-(1/g_{m,K}²) A^η(U_k(V)) + E_{K,m}(V)) (1 + R_{K,m}(V)),
  where U_k(V) is the regular background minimiser (CMP 102), E_{K,m} = Σ_X E_{K,m}(X) over polymers X (connected
  unions of coarse M-cubes) with E_{K,m}(X) gauge invariant; V ↦ A^η(U_k(V)) and every E_{K,m}(X) extend
  holomorphically to a complex neighbourhood R^c_m of R_m(ε_0) (fixed in coarse units; it contains, in a coarse
  axial or Landau gauge, all V = exp(iX)·V_flat with complex ||X||_∞ < α), with
  |E_{K,m}(X)| ≤ E_0 e^{-κ d(X)} (CMP 109 (1.18): no positive power of the coupling) and |A^η(U_k(V))| ≤ C_A |Λ_m|
  on R^c_m; R_{K,m} is the contribution of large-field histories at finer scales after the R-operation, with
  sup_{R_m(ε_0)} |R_{K,m}| ≤ 1/2.
- **(3b) large-field mass.** ν_{K,m}(C_m \ R_m(ε_0)) ≤ η_0.

**H-Bal-3G (volume-uniform Gibbs form; needed only for (d)). IMPORTED-NOT-YET-REVERIFIED** (no source states it; it is
what a Balaban-type representation with local polymers should give, and it is the content of P's E8* at depth k).
For every finite set Y of coarse links there are a non-empty open set O_Y ⊂ G^Y of regular local configurations and
c_Y > 0, **independent of K and M**, such that, outside an event of ν_{K,m}-probability ≤ η_0 |Y|, the conditional
density of V^(m)|_Y given V^(m)|_{Y^c} is ≥ c_Y on O_Y; and the Peierls bound
ν_{K,m}(|V(∂p'_i) - 1| ≥ ε_0 for i = 1..r) ≤ η_0^r for coarse plaquettes at mutual distance ≥ R_0.

**What H-Bal does not contain** (each named because a part of the theorem needs it):
- **H-src**: bounds on generating functionals with sources (unbounded fields), §4.
- **H-cont**: comparison of block variables on grids shifted by small a, uniformly in K, §4.
- **H-rot**: comparison of differently oriented lattices / universality, §4.
- **H-uniq**: uniqueness / decay of correlations in infinite volume, §5.

---

## 3. The soft layer and the (a), (b), (c) conclusions

### X-S4c. A continuous, gauge- and lattice-covariant block map with Balaban's small-field form exists. PROVEN-HERE
**Statement.** Fix 0 < r_0 < r_1 < 2π/N and a smooth φ: [0,∞) → [0,1] with φ = 1 on [0, r_0], φ = 0 on [r_1, ∞).
Put ψ(X) := φ(||X||_op) X on su(N), and λ(Z) := ψ(log Z) for Z ∈ SU(N) with no eigenvalue -1 (principal log),
λ(Z) := 0 otherwise. Define (notation of P's S4')
U'(X, X + e_μ) := S_{c_X} exp( (1/d!) Σ_σ L^{-d} Σ_{y∈B(X)} λ(S_{c_X}^{-1} T^σ_y) ).
Then: (i) λ: SU(N) → su(N) is continuous, so U' is a continuous function of the fine links; (ii) U' ∈ SU(N);
(iii) U' is gauge covariant; (iv) U' is covariant under block-aligned reflections and axis permutations; (v) U'
equals S4' (hence Balaban's (0.4) with diagonal pairing) whenever every ||log(S^{-1}T^σ_y)||_op ≤ r_0; (vi) it is
local (uses only links of B(X) ∪ B(X + e_μ) and the crossing links), as P's L0.
**Proof.** (i) The set C = {Z : -1 ∈ spec Z} is closed and conjugation invariant; on its complement the principal log
is continuous, so λ is continuous there. If Z_n → Z ∈ C with Z_n ∉ C, some eigenphase of Z_n tends to ±π, so
||log Z_n||_op > r_1 eventually and λ(Z_n) = 0 = λ(Z). Hence λ is continuous everywhere.
(ii) If λ(Z) ≠ 0 then ||log Z||_op < r_1 < 2π/N, so the eigenphases θ_j lie in (-2π/N, 2π/N); Σθ_j ∈ 2πZ and
|Σθ_j| < 2π force Σθ_j = 0: log Z, hence λ(Z), is traceless anti-Hermitian. An average of such is such, so the
exponential is in SU(N).
(iii) Under a fine gauge transformation h, S_{c_X} ↦ h(c_X)S h(c_Y)^{-1}, T^σ_y ↦ h(c_X)T^σ_y h(c_Y)^{-1}, so every
S^{-1}T ↦ h(c_Y)S^{-1}T h(c_Y)^{-1}. The principal log is conjugation equivariant off C, C is conjugation invariant,
and ||·||_op is unitarily invariant, so λ is conjugation equivariant and U' ↦ h(c_X)U'h(c_Y)^{-1}.
(iv) P's L9a' reversal computation uses only log(Z^{-1}) = -log Z and conjugation equivariance. Off C,
log(Z^{-1}) = -log Z (eigenphases negate inside (-π, π)); ψ is odd; Z^{-1} ∈ C iff Z ∈ C. So λ(Z^{-1}) = -λ(Z)
everywhere and the computation goes through verbatim. Axis permutations: P's S4' re-check (order set and reference are
permutation invariant) uses no property of log. (v), (vi): immediate. ∎
- **Consequence.** With S4c, every block observable at every resolution and every shift is a **continuous** function
  on Ω_K, and A: C_{m+1} → C_m is continuous. **P's branch-set discontinuity (S4'' with the odd branch rule) is a
  choice, not a necessity**, and the "price" P records under S5' (E8* needed to pass A through limits) disappears.
- **Caveat (load-bearing for H-Bal-3).** Balaban's papers define the averaging on regular configurations; which
  everywhere-defined extension his large-field analysis uses is [not-read]. H-Bal-3 is assumed **for S4c**. Since S4c
  agrees with (0.4) on regular configurations, only the large-field bookkeeping (CMP 122) could depend on the choice.

### X-ALG. A single limit state exists on a separable algebra of all block and flowed observables. PROVEN-HERE
**Statement.** Let I be the countable index set of generators (m, a, X, f) (f from a countable dense subset of the
gauge-invariant part of C(C_m(X)), a ∈ D) and (t, γ) (t ∈ Q_{>0}, γ a coarse lattice loop). For each K let π_K(i) ∈
C(Ω_K) be the corresponding observable (and the constant 1 for the finitely many K below the level of i). Let 𝔄 be
the C*-subalgebra of the ℓ^∞-product Π_K C(Ω_K) generated by the sequences (π_K(i))_K. Then 𝔄 is a separable,
unital, commutative C*-algebra; ω_K(F) := E_{μ_K}[F_K] are states on 𝔄; and there is a subsequence K_j with
ω_{K_j} → ω weak-*, for a state ω. By Gelfand duality, ω is a Radon probability measure on the compact metrizable
space 𝒳 := Spec 𝔄 (the "continuum configuration space").
**Proof.** Polynomials with rational complex coefficients in the generators are countable and dense, so 𝔄 is separable.
ω_K is positive and ω_K(1) = 1. The state space of a separable unital C*-algebra is weak-* compact (Banach-Alaoglu) and
metrizable (separability), hence sequentially compact [STANDARD]. ∎
- Every element of 𝔄 has well-defined Schwinger "functions": ω(F_1⋯F_n) = lim_j E_{K_j}[F_{1,K_j}⋯F_{n,K_j}]. This is
  part **(a)** for bounded gauge-invariant observables, in finite volume, with **no hypothesis at all**.
- Content-free alone (P's L7a remark stands): ω could be degenerate. (c) is where content enters.

### X-CONS. The limit is consistent across resolutions; the block laws form a projective family. PROVEN-HERE
**Statement.** For f ∈ C(C_m) let F_f := (f ∘ V^(m)_K)_K ∈ 𝔄. f ↦ F_f is a *-homomorphism C(C_m) → 𝔄; let
p_m: 𝒳 → C_m be its dual map and ν_{*,m} := (p_m)_*ω. Then A ∘ p_{m+1} = p_m and A_*ν_{*,m+1} = ν_{*,m}.
**Proof.** f∘A ∈ C(C_{m+1}) by X-S4c, and (f∘A)∘V^(m+1)_K = f∘V^(m)_K as functions on Ω_K for all K ≥ m+1, so
F_{f∘A} = F_f in 𝔄 (they differ in finitely many components only through the convention below the level; ω, a limit
of the ω_K, does not see finitely many components). Dualising gives A∘p_{m+1} = p_m and the push-forward identity. ∎
- **Comparison with P (L7a, §0 finding 1, S5' "Price").** P states that without E8* the per-resolution limits need not
  be consistent. That is true for the discontinuous S4''. With S4c, consistency is automatic. Even with S4'', the
  *state* ω on 𝔄 is automatically consistent (F_f is one element, whatever level represents it); only its
  representation by measures on C_{m+1} can fail, by the continuous mapping theorem exactly on ν_{*,m+1}(Disc A) > 0.
  So **E8* is not needed for existence of a consistent limit state**; it is a regularity statement.

### X-SYM. Symmetries of ω. PROVEN-HERE (using P's covariance computations, re-checked in X-S4c)
**Statement.** ω is invariant under the L-adic translations a ∈ D (mod ℓ), under the hypercubic group about a
resolution-0 block centre (on a torus with equal sides; on R×T³ the spatial hypercubic group and time reflections),
and every element of 𝔄 is gauge invariant (by construction).
**Proof.** μ_K is invariant under εZ^4 translations and the lattice hypercubic group. A translation by a ∈ L^{-m'}Z^4,
K ≥ m', maps the generator (m, b, X, f) to (m, a + b, X, f) and flowed loops to translated flowed loops (the flow
commutes with lattice symmetries, X-FLOW). Hypercubic covariance of S4c is X-S4c (iv). Hence ω_K∘α = ω_K for these
automorphisms α of 𝔄 for all large K, and the identity passes to the weak-* limit. ∎

### X-LRP. Lattice reflection positivity of the Wilson action, for bounded measurable functions. IMPORTED-AND-REVERIFIED
**Statement.** For a fine link mid-plane Π of Λ_K (and its antipodal plane), with θ the reflection and 𝔉_+ the bounded
measurable functions of the links strictly on the positive side, ω_K(θ(F)^* F) ≥ 0 for F ∈ 𝔉_+, when β ≥ 0.
**Source.** Osterwalder-Seiler, Ann. Phys. 110 (1978) [not-read here]; re-derived in P, L9a (scope extended to bounded
measurable F in [R4-fix]); mixed reflection L9a-m; exact Z2 check c4.
**Re-verification (this session).** I re-read P's proof (P l.4249-4266 at session 15): gauge-fix the crossing links to
1 by a positive-side gauge transformation; e^{-S} = e^{A_+}θ(e^{A_+}) Π_{crossing p} exp((β/N) Re tr(W_pθ(W_p)^†));
expand the crossing factors into Σ_α c_α G_α θ(Ḡ_α) with c_α ≥ 0; Haar factorises; θ preserves Haar. The argument
uses no continuity of F, so it covers 𝔉_+. Correct. On the torus, ℓ_0/2 = 2L^M ∈ εZ, and Π ∈ P_0 implies the antipodal
plane Π + ℓ_0/2 ∈ P_0 ⊂ P_K: both are link mid-planes, as required.

### X-RP. Reflection positivity of ω for every plane in P. PROVEN-HERE | X-LRP
**Statement.** For Π ∈ P and 𝔄_+(Π) the C*-subalgebra generated by the block generators all of whose blocks lie on the
positive side of Π (all resolutions and all shifts), ω(θ(F)^*F) ≥ 0 for F ∈ 𝔄_+(Π).
**Proof.** Let Π ∈ P_{m_0}. For K ≥ m_0 and K above the levels of the finitely many generators in F, every block
generator in F is a function of fine links in blocks on the positive side (locality, X-S4c (vi)), so F_K ∈ 𝔉_+;
θ maps grids shifted by a to grids shifted by θ_lin a, so θ(F)_K = θ(F_K). Hence ω_K(θ(F)^*F) ≥ 0 by X-LRP, and
the inequality is preserved by the weak-* limit. Elements of 𝔄_+ are norm limits of such polynomials. ∎
- **Flowed observables are not in 𝔄_+** (X-FLOW-NL); RP is not asserted for them.

### X-FLOW. Flowed lattice Wilson loops are bounded continuous gauge-invariant observables. PROVEN-HERE
**Statement.** The Wilson flow V_τ(U) exists for all τ ∈ R, is smooth in (τ, U), commutes with gauge transformations
and lattice symmetries; W_{t,γ} ∈ C(Ω_K), |W_{t,γ}| ≤ 1, gauge invariant.
**Proof.** The flow is the gradient flow of a smooth function on the compact manifold Ω_K; a smooth vector field on a
compact manifold is complete and its flow is smooth (Lüscher states the same, NOTES §4 [read]). The Wilson action is
gauge and lattice-symmetry invariant, so the gradient vector field is equivariant, and by uniqueness of solutions the
flow commutes with these actions. The holonomy is a continuous function of V_τ; its normalised trace is bounded by 1
and gauge invariant (closed loop). ∎

### X-FLOW-NL. At every positive flow time a flowed loop depends on links arbitrarily far away. PROVEN-HERE (+ check x1)
**Statement.** Around the flat configuration U = 1, the first variation of the flowed curvature F(τ) with respect to a
fine link b is Σ_{p'} K_τ(p - p')(dδA_b)(p') componentwise, with K_τ(x) = e^{-8τ} Π_{i=1}^4 I_{x_i}(2τ) > 0 (I_n the
modified Bessel function); it is non-zero for links b at any distance. Hence for a coarse loop γ, the second variation
∂²W_{t,γ}/∂A_b∂A_b at U = 1 is non-zero for links b arbitrarily far from γ, and W_{t,γ} is not a function of the links
in any half-space not containing all of them.
**Proof.** U = 1 is a stationary point of the flow, so the derivative of V_τ at U = 1 is the linearised flow
Ȧ = -d^*dA (lattice units). For F = dA: Ḟ = -dd^*F = -Δ_2 F (since dF = 0, Δ_2F = dd^*F). On the cubical lattice the
Hodge Laplacian on 2-forms acts componentwise as the scalar lattice Laplacian (check x1 A2: exact, side 4 and 5), whose
heat kernel is the stated product of Bessel functions, strictly positive. The response of a plaquette (μν) to a link b in
direction ν at transverse offset x is K_τ(x) - K_τ(x - e_μ) up to sign; since n ↦ I_n(z) is strictly decreasing for
n ≥ 0 and z > 0, this is non-zero for x_μ ≥ 1. W = 1 - (1/2N)tr(Φ_γ²) + O(Φ³) with Φ_γ the (linear-order) flux, so the
second variation is -(1/N)·(response)² ≠ 0. Check x1 B2: response 2.96e-5 (τ = 0.5), 1.62e-4 (τ = 2) for a link at
distance 2 in every coordinate on side 5. ∎
- Physical reading: in physical units the kernel width is of order √t; the dependence is Gaussian-small beyond √t but never
  zero; exact RP for flowed fields is therefore not available, and approximate RP needs a locality estimate (H-loc, §4).

### X-OS. OS reconstruction on R×T³: a Hamiltonian H ≥ 0 exists on (ker T)^⊥ with no estimate. PROVEN-HERE | X-RP, X-SYM
**Setting.** Take the time side ℓ_0 → ∞ jointly with K → ∞ (X-IV below, with the spatial torus fixed). Let Π_0 ∈ P_0
be a time plane, θ its reflection, τ_s time translation, 𝔄_+ as in X-RP. On 𝔄_+ put ⟨F, G⟩ := ω(θ(F)^*G); let H_ω be
the Hilbert completion modulo null vectors, Ω the class of 1. For s ∈ 2D_+ := {2jL^{-m} : j ≥ 1, m ≥ 0}
define T(s)[F] := [τ_s F].
**Statement.** (i) T(s) is a well-defined self-adjoint contraction with T(s) ≥ 0, T(s)T(s') = T(s + s'), T(s)Ω = Ω.
(ii) T(s) = T(2)^{s/2} for all s ∈ 2D_+ (functional calculus). (iii) With 𝒦 := ker T(2) = ker T(s) for every s,
H := -½ log T(2) is a self-adjoint operator ≥ 0 on 𝒦^⊥ with HΩ = 0, T(s) = e^{-sH} ⊕ 0 on 𝒦^⊥ ⊕ 𝒦, and
s ↦ e^{-sH} extends to a strongly continuous semigroup on 𝒦^⊥ for real s ≥ 0. (iv) 𝒦 = {0} iff the time-continuity
condition holds: lim_{s→0, s∈2D} ω(θ(F)^*τ_sF) = ω(θ(F)^*F) for every F ∈ 𝔄_+.
**Proof.** (i) τ_s maps 𝔄_+ into 𝔄_+ (s > 0; shifted grids are generators). θτ_s = τ_{-s}θ and τ-invariance of ω give
⟨F, T(s)G⟩ = ⟨T(s)F, G⟩ and ⟨T(s)F, T(s)F⟩ = ⟨F, T(2s)F⟩. Positivity: ⟨F, T(s)F⟩ = ω(τ_{-s/2}θ(F)^* τ_{s/2}F) =
ω(θ'(G)^*G) with G = τ_{s/2}F and θ' the reflection in Π_0 + s/2. For s = 2jL^{-m}, s/2 = jL^{-m}, and
Π_0 + s/2 ∈ P_m by X-PLANES [Π_0 = i + ½, and i + ½ + jL^{-m} = ((i + ½)L^m + j)L^{-m} with
(i + ½)L^m = iL^m + (L^m - 1)/2 + ½, L^m - 1 even]; G lies on its positive side; X-RP gives ≥ 0. Contraction: by
Cauchy-Schwarz iterated, ⟨F, T(s)F⟩ ≤ ⟨F, F⟩^{1-2^{-n}} ⟨F, T(2^n s)F⟩^{2^{-n}} ≤ ⟨F, F⟩^{1-2^{-n}}||F||_∞^{2^{1-n}} →
⟨F, F⟩, using |ω(·)| ≤ ||·||. Null vectors map to null vectors by Cauchy-Schwarz, so T(s) is well defined; it is
bounded, symmetric and positive on a dense set, hence self-adjoint positive with ||T(s)|| ≤ 1. The semigroup law and
T(s)Ω = Ω are immediate. (ii) T(2L^{-m}) ≥ 0 and T(2L^{-m})^{L^m} = T(2); positive operators have unique positive roots
[STANDARD], so T(2L^{-m}) = T(2)^{L^{-m}} and T(2jL^{-m}) = T(2)^{jL^{-m}}. (iii) Functional calculus for the positive
contraction T(2): ker T(2)^r = ker T(2) for r > 0; on 𝒦^⊥, T(2) is injective with spectrum in (0, 1], so log T(2) is
self-adjoint ≤ 0; e^{-sH} = T(2)^{s/2} is strongly continuous on 𝒦^⊥ by dominated convergence in the spectral
representation. (iv) T(s) → P_{𝒦^⊥} strongly as s → 0 (spectral theorem), so ⟨F, T(s)F⟩ → ||P_{𝒦^⊥}F||²; this equals
||F||² for all F in a dense set iff 𝒦 = {0}. ∎
- **Meaning.** The OS Hilbert space and a positive Hamiltonian exist for **every** limit point, from RP alone. The
  only OS-structural estimate on the time axis is (iv): **H-cont-time** (OPEN, X-CONT).
- On the torus (finite ℓ_0) the same holds with the usual finite-temperature restrictions (supports in
  (0, ℓ_0/2)); not written out.

### X-IV. Infinite-volume limit points exist with all soft structure. PROVEN-HERE
**Statement.** Along any sequence (K_j, ℓ_j) → (∞, ∞) (ℓ_j ∈ 4L^N), there is a subsequence and a state ω on the
quasi-local algebra 𝔄^loc (generators supported in bounded regions of R^4, defined on all tori large enough) with:
X-CONS, X-SYM (D-translations of R^4, hypercubic group), X-RP for all planes in P, and X-OS on R^4.
**Proof.** Same as X-ALG with the countable generator set of bounded support; each generator is defined for all large
j; X-CONS, X-SYM, X-RP pass to the limit as before (for X-RP, a bounded-support F lies in the positive slab for ℓ_j
large). ∎ (This is P's L8a/L8b/L8c in the state formulation.)

### X-ND. Non-triviality, weak form: the limit block laws are neither flat nor Haar. PROVEN-HERE | H-Bal-1, H-Bal-3 (finite volume)
**Statement.** For every m and every limit point: (i) on int R_m(ε_0), ν_{*,m} ≥ c_m · Haar with c_m > 0;
(ii) ν_{*,m}(closure of R_m(ε_0)) ≥ 1 - η_0; hence (iii) ν_{*,m} gives zero mass to no non-empty open subset of
int R_m(ε_0), so it is not supported on the flat configurations (a Haar-null closed set), and (iv) ν_{*,m} ≠ Haar
whenever 1 - η_0 > Haar(R̄_m(ε_0)) (true for small ε_0: a single coarse plaquette is Haar distributed under Haar
measure, so Haar(R̄_m) ≤ Haar{|W - 1| ≤ ε_0} = O(ε_0^{N²-1})).
**Proof.** By (3a), on R := R_m(ε_0): ρ_K = 𝒵_K^{-1} w_K e^{E_K}(1 + R_K) with w_K := exp(-(1/g_{m,K}²)A^η(U_k(V))).
Put Ē := E_0 Σ_X e^{-κd(X)} over polymers in the finite torus (< ∞, at most C_κ E_0 |Λ_m|). Then
e^{-Ē}/2 ≤ e^{E_K}(1 + R_K) ≤ 3e^{Ē}/2 and e^{-C_A|Λ_m|/g_{min}²} ≤ w_K ≤ e^{C_A|Λ_m|/g_{min}²} with g_min the K-uniform
lower bound of H-Bal-1 (A^η is real on real configurations; the modulus bound of (3a) is used). Put
c' := ½e^{-Ē - C_A|Λ_m|/g_min²} and c'' := (3/2)e^{Ē + C_A|Λ_m|/g_min²}, so c' ≤ w_K e^{E_K}(1 + R_K) ≤ c'' on R.
Normalisation: 1 ≥ ν_K(R) = 𝒵_K^{-1}∫_R w_K e^{E_K}(1 + R_K) dHaar ≥ 𝒵_K^{-1} c' Haar(R), so
𝒵_K^{-1} ≤ (c' Haar(R))^{-1}; and ν_K(R) ≥ 1 - η_0 gives 𝒵_K^{-1} ≥ (1 - η_0)/(c'' Haar(R)). Hence
ρ_K ≥ c_m := c'(1 - η_0)/(c'' Haar(R)) > 0 on R, uniformly in K. For continuous f ≥ 0 supported in int R, ∫f dν_{*} = lim ∫ f ρ_K dHaar ≥ c_m ∫ f dHaar; Riesz on
the open set int R gives (i). (ii) is the Portmanteau inequality for the closed set R̄. (iii), (iv) follow. ∎
- H-Bal-2 is not used. The constants degrade like e^{-C|Λ_m|} with the number of coarse cells: this is a
  finite-volume statement at each fixed m; X-IVND is the volume-uniform version.

### X-MONTEL. The limit block law has a density of Balaban's form with an analytic effective action. PROVEN-HERE | H-Bal-1, H-Bal-3
**Statement.** Along a further subsequence, g_{m,K} → g_{m,*} ∈ (0, γ], and E_{K,m}(X) → E_{*,m}(X),
A^η(U_k(·)) → 𝒜_*(·) locally uniformly on R^c_m, holomorphically, with |E_{*,m}(X)| ≤ E_0 e^{-κd(X)}; and on
int R_m(ε_0), dν_{*,m}/dHaar = 𝒵_*^{-1} exp(-(1/g_{m,*}²)𝒜_* + E_{*,m}) (1 + R_*) with R_* a weak-* limit point of the
R_{K,m} (|R_*| ≤ 1/2 a.e.).
**Proof.** H-Bal-1 gives g_{m,K} in a compact subinterval of (0, γ]. In finite volume there are finitely many polymers;
each E_{K,m}(X) and A^η(U_k(·)) is holomorphic on R^c_m and bounded uniformly in K, so Montel's theorem (several
complex variables) [STANDARD] gives locally uniformly convergent subsequences with holomorphic limits; the bounds pass
to the limit. The R_{K,m} are bounded by 1/2 in L^∞, so a further subsequence converges weak-* in L^∞(Haar|_R);
𝒵_K converges along a subsequence by the bounds in X-ND. For continuous f supported in int R, ∫ f ρ_K dHaar converges
to the integral against the stated limit (uniform convergence times weak-* convergence). ∎
- This is the precise sense in which "the effective action on the unit lattice remains bounded, and the existence of a
  UV limit for gauge-invariant observables such as smoothed Wilson loops follows by compactness, without uniqueness"
  (Magnen-Rivasseau-Sénéor's description of Balaban's result, NOTES §2 [read]).

### X-CAUCHY. In the limit effective action, the order-n Taylor term in the rescaled field is O(g^n). PROVEN-HERE | H-Bal-3
**Statement.** In a coarse gauge where V = exp(iX)V_flat and R^c_m ⊃ {||X||_∞ < α}, write X = g_{m,*}B. For every
polymer X_0, the homogeneous degree-n Taylor term T_n of B ↦ E_{*,m}(X_0; exp(ig B)V_flat) satisfies
|T_n(B)| ≤ E_0 e^{-κd(X_0)} (g||B||_∞/α)^n.
**Proof.** For fixed real B ≠ 0, f(z) := E_{*,m}(X_0; exp(izgB/||B||_∞)V_flat) is holomorphic for |z| < α/g and bounded by
E_0e^{-κd(X_0)}; T_n(B) = f^{(n)}(0)||B||_∞^n/n!, and Cauchy's estimate on |z| = r < α/g, r → α/g, gives the bound. ∎
- **Reading.** The effective-action corrections perturb the Gaussian quadratic form ½⟨B, QB⟩ by relative O(g²) and
  contribute O(g⁴) to quartic vertices, while the explicit term (1/g²)𝒜_* contributes cubic vertices O(g) and quartic
  O(g²). This is the structure X-NT2 needs.

### X-NT2. Non-triviality, strong form: the limit is not Gaussian. OPEN (reduced)
**Statement (target).** For some m, small g and some coarse loops (or linearised block fields), the connected 4-point
cumulant of the rescaled linearised block field B = g^{-1}Π_0 log V^(m) under ν_{*,m} is c g² + O(g³) with c ≠ 0
determined by the tree-level vertices of (1/g²)𝒜_*.
**Reduction.** Given X-MONTEL and X-CAUCHY, what is missing is a finite-dimensional Laplace-method lemma (LAP) for the
integral over C_m with density ∝ exp(-(1/g²)𝒜_* + E_*), uniformly in the large-field remainder (3b) and on a torus
whose flat connections are not isolated (commuting holonomies: the moduli must be integrated, not expanded). Also
needed: the cubic coefficient of 𝒜_* is the non-abelian YM vertex smeared by the block constraint, which requires the
second-order expansion of the background minimiser (CMP 102 [not-read]).

### X-NTAF. Non-triviality via asymptotic freedom: the block laws approach flat logarithmically as m → ∞. (Session 1: OPEN; session 2: PROVEN-HERE in two-sided form, §10.1)
**Statement (target).** For a coarse plaquette p at resolution m, c_1 g_{m,*}² ≤ ∫ (1 - N^{-1}Re tr V_p) dν_{*,m} ≤
c_2 g_{m,*}², with g_{m,*}² ≍ 1/(m log L) by H-Bal-1. A massless Gaussian field gives m-independent block laws, a
massive one m-independent laws as m → ∞, so this excludes free fields with canonical scaling.
**Needs.** H-Bal-3G (finite-volume constants e^{±C|Λ_m|} grow with m and are useless here) plus a one-link Laplace lemma
(LAP-1) for the conditional law of a coarse link given a regular environment.

### X-IVND. Infinite-volume non-degeneracy. PROVEN-HERE | H-Bal-3G
**Statement.** Under H-Bal-3G, every infinite-volume limit point (X-IV) has marginals on any finite coarse link set Y
with ν_{*,m}|_Y ≥ c_Y(1 - η_0|Y|)·Haar on O_Y, and ν_{*,m}(r given coarse plaquettes at mutual distance ≥ R_0 are all irregular) ≤ η_0^r. Hence the infinite-volume limit is not flat and not Haar, uniformly in the volume.
**Proof.** For continuous f ≥ 0 supported in O_Y: E_K[f(V_Y)] = E_K[E_K[f(V_Y) | V_{Y^c}]] ≥ c_Y (∫ f dHaar)
(1 - η_0|Y|), uniformly in K and M; pass to the limit. The Peierls bound is a bound on the probability of a closed set
of coarse configurations; Portmanteau for closed sets passes it to the limit. ∎

### X-RAW. Raw lattice Wilson loops of fixed physical size degenerate. ARGUED (uncounted)
At one loop, a straight lattice line of physical length ℓ_γ costs exp(-c g_0² C_F ℓ_γ/ε) (lattice self-energy;
c involves the 3D lattice Green's function at the origin), with g_0² ≍ 1/(2b_0 log(1/ε)); so ⟨W_γ⟩ → 0 like
exp(-c' ℓ_γ/(ε log(1/ε))), with extra cusp factors at every lattice corner. Chatterjee's Problem 5.2 (NOTES §3 [read])
formulates the continuum limit of raw loops *with* a divergent perimeter subtraction c(β)(R + T). Raw loops are
therefore excluded from 𝔄; the block loops (O^blk) and flowed loops (O^flow) replace them. Not proven here.

---

## 4. What needs more than stability: OS0, time continuity, rotations, sources

### X-MOM. Exponential-moment bounds imply convergent Schwinger functions, distributional bounds and OS0. PROVEN-HERE (implication)
**Hypothesis H-src(Φ).** Φ_K(f) are real random variables on Ω_K, linear in f ∈ 𝒯 (a separable space of test
functions with a continuous norm N, e.g. C^∞(T^4) with N(f) = ||f||_{L^1} + ||f||_{L^p}), and there are C, c_0 > 0 with
E_K[exp Φ_K(f)] ≤ exp(C N(f)) for all K and all f with N(f) ≤ c_0.
**Statement.** Then (i) E_K|Φ_K(f)|^n ≤ 2e^{Cc_0} n! (N(f)/c_0)^n for all f, n, K; (ii) along a subsequence, all
S^K_n(f_1, ..., f_n) := E_K[Φ_K(f_1)⋯Φ_K(f_n)] converge, for all n and all f_i ∈ 𝒯, to multilinear S_n with
|S_n(f_1..f_n)| ≤ 2e^{Cc_0} n! c_0^{-n} Π N(f_i); for 𝒯 = C^∞(T^4) each S_n is a distribution on T^{4n} (kernel
theorem); (iii) the limits are the moments of a probability measure on 𝒯' (Minlos, 𝒯 nuclear), with
E[e^{Φ(f)}] ≤ e^{CN(f)} (OS0 in the Glimm-Jaffe exponential form); (iv) if moreover each Φ_K(f) with f supported in a
positive half-space is measurable with respect to the positive-half links, the limit is reflection positive on the
polynomial algebra and on exponentials.
**Proof.** (i) For N(f) ≤ c_0 put h := c_0 f/N(f): E e^{±Φ(h)} ≤ e^{Cc_0}, so E e^{|Φ(h)|} ≤ 2e^{Cc_0}, and
|x|^n/n! ≤ e^{|x|} gives E|Φ(h)|^n ≤ 2e^{Cc_0}n!; scale back by linearity (any f). (ii) Hölder gives the multilinear
bound for S^K_n. For f_i in a countable dense 𝒟 ⊂ 𝒯 the S^K_n are bounded, so a diagonal subsequence converges for
all finite tuples from 𝒟; the uniform multilinear bound gives |S^K_n(f) - S^K_n(f')| ≤ C_n Σ_i N(f_i - f'_i)Π_{j≠i}
max(N(f_j), N(f'_j)), so convergence extends to all of 𝒯, with the same bound. Continuity in N (continuous on C^∞)
plus multilinearity gives distributions by the Schwartz kernel theorem [STANDARD]. (iii) Moments with n!c^n growth
determine the finite-dimensional laws, which therefore converge weakly (tightness from (i), method of moments);
|1 - E e^{iΦ(f)}| ≤ E|Φ(f)| ≤ C'N(f) gives continuity of the characteristic functional, and Minlos [STANDARD] gives the
measure on 𝒯'. e^{Φ_K(f)} is uniformly integrable when N(2f) ≤ c_0 (bounded second moment by H-src), so the exponential
bound passes to the limit (for N(f) ≤ c_0/2; the constant is unchanged); general f by the form of the bound is not
claimed. (iv) Each RP inequality for polynomials is a finite combination of moments, which converge; exponentials are
limits of polynomials in L² by (i). ∎

### X-SRC-GAP. H-src is not in Balaban, and the obvious fields violate its naive form. OPEN (the gap), with ARGUED sub-points (session 2: separated-support form reduced, §10.3)
- **Bounded block fields** satisfy H-src trivially at fixed resolution (|Φ| ≤ C(m)N(f)); the content of OS0 is the
  limit m → ∞ (point-like fields), where the constants must not grow.
- **Local composite fields of dimension 4** (the lattice action density Σ_p f(x_p)β_0 w_p, i.e. tr F² smeared at
  the lattice scale): ARGUED, its variance diverges like ε^{-4}∫f² (conditional on all other links, the
  single-link action has O(1) equipartition fluctuations, and there are ε^{-4} independent such links per unit
  volume), so H-src in exponential form fails. For dimension-4 composites the Schwinger functions must be bounded at
  **non-coincident** supports and extended (H-src', OPEN): this is a statement about generating functionals with
  local counterterm polynomials in the sources, i.e. **UV stability with a position-dependent bare coupling g_0(x)**
  (a source for tr F² is a variation of the coupling) with explicit counterterms. Balaban's machinery is local, so this
  is a natural extension; it is not in the published papers.
- **Flowed fields at fixed t > 0** (energy density E_t(x)): perturbatively finite with no further renormalisation
  (Lüscher-Weisz, NOTES §4 [read]); H-src(E_t) is plausible but OPEN, and it needs fine-scale control (the flow
  reaches the cutoff scale), i.e. H-Bal-3 at every scale, not just at m.
- **Statement of H-src-flow (OPEN):** for each t > 0 there are C_t, c_t with E_K[exp(Σ_x ε^4 f(x)(E_t(x) - ⟨E_t⟩_K))]
  ≤ exp(C_t N(f)) for N(f) ≤ c_t, uniformly in K. With X-MOM it gives OS0 for flowed fields at fixed t; RP for them
  still needs H-loc.

### X-ARP. Approximate RP for approximately local observables. PROVEN-HERE (implication)
**Statement.** If F ∈ L²(ω) (e.g. a flowed observable, via X-ALG) and G ∈ 𝔄_+ with ||F - G||_{L²(ω)} ≤ δ and
||θF - θG||_{L²(ω)} ≤ δ, then ω(θ(F)^*F) ≥ -2δ||G||_{L²(ω)} - δ².
**Proof.** ω(θ(F)^*F) = ω(θ(G)^*G) + ω(θ(F - G)^*G) + ω(θ(F)^*(F - G)); the first is ≥ 0 by X-RP; Cauchy-Schwarz bounds
the others. ∎
- **H-loc (OPEN):** for a flowed loop at distance d from Π, inf_{G∈𝔄_+} ||W_{t,γ} - G||_{L²(ω)} ≤ C e^{-c d²/t},
  uniformly along the subsequence. X-FLOW-NL shows exact locality fails, so H-loc is the needed estimate. With H-loc,
  flowed and block observables generate a common RP structure in the limit t → 0 at fixed distance (P's route γ2).

### X-CONT. Time (and space) continuity: ker T = 0. OPEN (session 2 reductions: X-KER, X-2GRID, X-CONT-G, §10.2)
**Statement H-cont (needed).** There are γ > 0 and C such that for every block observable F ∈ O_m(X) with Lipschitz
constant 1 and every a ∈ D with |a| ≤ L^{-m}: |E_K[F(V^(m)_{K,a})] - E_K[F(V^(m)_{K,0})]| ≤ C|X|_m (L^m|a|)^γ,
uniformly in K (P's E9.1). Joint version for products. By X-OS (iv), H-cont implies 𝒦 = {0}, i.e. the Hamiltonian on
all of H_ω, and with X-SYM, exact R^4 translation invariance of the limit (P's L9b(β)).
**Why it is not soft and not in H-Bal-3 at one scale.** V^(m)_{K,a} and V^(m)_{K,0} are averages over blocks that
differ in a boundary layer of physical width |a|; comparing them needs control of the fine fields at all scales between
|a| and L^{-m} *in the same configuration*. H-Bal-3 at each scale separately gives the law of each block variable, not
the joint law of two grids. Large-field regions at fine scales are dense (P, E8.3), so the estimate must use the
R-operation's resummation, not their absence.

### X-ROT. Euclidean invariance (OS1). OPEN
On the torus false by geometry. On R^4: averaging limit points over SO(4) destroys RP (P, remark R9.1). Needs either
H-rot (orientation independence of the limit, a universality statement requiring E7-type convergence and, in infinite
volume, probably H-uniq) or the two-family route (rotation-covariant flowed fields + H-loc). Hypercubic symmetry allows
dimension-6 rotation-breaking operators (e.g. Σ_μ tr(D_μF_μν)²), so rotation invariance requires that their
coefficients vanish in the limit: a rate statement (cutoff effects O(ε^κ)), not a compactness statement.

---

## 5. Infinite volume: what needs a gap or a cluster expansion

### X-IR. Uniqueness, clustering (OS4), mass gap. OPEN
- **Not needed for existence of limit points** (X-IV) or for RP, L-adic translations, hypercubic symmetry, the OS
  Hilbert space and H ≥ 0 on 𝒦^⊥ (X-OS).
- **Needed for:** uniqueness of the state (independence of the subsequence and of the torus shapes); clustering OS4
  (and hence the vacuum's uniqueness in H_ω); the mass gap; the universality route to rotation invariance; and any
  identification of the limit with "the" YM theory.
- **Why H-Bal does not reach it.** At the unit scale g = g_K is small but the coarse theory on the unit lattice is a
  weakly coupled lattice gauge theory in a large volume, whose own RG flows to strong coupling at larger scales.
  Balaban stops at the unit scale; H-Bal-2's bulk bounds e^{±E|T|} are crude at that scale and say nothing about decay.
  H-Bal-3G gives volume-uniform *local* bounds (X-IVND), not decay of correlations.
- Remark: OS4 for a translation-invariant RP limit point can in principle be sought by ergodic decomposition; whether
  RP survives it is [unverified] (P, L9d).

---

## 6. DAG and tally (updated session 2)

```
(a) X-ALG ⇐ X-S4c (continuity) ; X-CONS ⇐ X-S4c, X-ALG ; X-FLOW
(b) X-RP ⇐ X-LRP [IMP-REV], X-S4c(iv,vi), X-ALG ; X-SYM ⇐ X-S4c, X-FLOW ; X-OS ⇐ X-RP, X-SYM, X-IV(time)
    time continuity: 𝒦 = {0} ⇐ H-bl ⇐ H-cont-time (X-KER) ; X-2GRID (exact) ;
        H-cont ⇐ H-corr + H-lin [OPEN; implication ARGUED] ; free Gaussian model: X-CONT-G (proven)
    OS1: X-ROT [OPEN] ⇐ H-rot or (X-ARP + H-loc [OPEN])
    OS0 (fields): X-MOM [implication] ⇐ H-src-flow / H-src' [OPEN, X-SRC-GAP]
        separated supports: X-SRC-CT ⇐ H-src' ⇐ H-Bal-loc (X-SRC-RED) ; diagonal: H-src'-diag [OPEN]
(c) X-ND ⇐ H-Bal-1, H-Bal-3 ; X-MONTEL ⇐ H-Bal-1, H-Bal-3 ; X-CAUCHY ⇐ X-MONTEL
    X-NT2 [OPEN] ⇐ X-MONTEL, X-CAUCHY, LAP (moduli)
    LAP-1 ⇐ H-Bal-3L, C2 ; X-NTAF, X-NTAF-AF ⇐ H-Bal-1, LAP-1, H-Bal-3T ; X-WIL ⇐ LAP-1 (exact for Wilson)
    X-NTAF-sharp [OPEN] ⇐ W-AF1 (flow coefficient) + W-AF2 (= H-corr)
(d) X-IV ; X-IVND ⇐ H-Bal-3G ; X-IR [OPEN]
H-Bal-2 : used by no node.
```

| Status | Count | Items |
|---|---|---|
| PROVEN-HERE | 24 | session 1 (16): X-S4c, X-ALG, X-CONS, X-SYM, X-RP, X-FLOW, X-FLOW-NL, X-OS, X-IV, X-ARP, X-MOM, X-ND, X-MONTEL, X-CAUCHY, X-IVND, X-PLANES. Session 2 (8): LAP-1 (with C2), X-NTAF (with corollary X-NTAF-AF), X-WIL, X-KER, X-2GRID, X-CONT-G, X-SRC-CT, X-SRC-RED |
| IMPORTED-AND-REVERIFIED | 1 | X-LRP (Osterwalder-Seiler lattice RP, via P's re-derivation, re-read here) |
| IMPORTED-NOT-YET-REVERIFIED | 7 | hypotheses H-Bal-1, H-Bal-2, H-Bal-3, H-Bal-3G; session 2: H-Bal-3L, H-Bal-3T, H-Bal-loc (no source states the last four) |
| OPEN | 11 | X-NT2 (with LAP), X-NTAF-sharp (W-AF1, W-AF2), H-src-flow, H-src'-diag (contact terms), H-loc, H-cont (X-CONT; reduced), H-corr, H-lin, X-ROT, X-IR (uniqueness/OS4/gap), the S4c-compatibility of CMP 122's large-field bookkeeping |
| ARGUED (uncounted) | 6 | X-RAW; the ε^{-4} variance of the action density; H-corr + H-lin ⇒ H-cont; H-Bal-3L/3T as the local content of H-Bal-3 (Dimock analogue); the bare additive coupling shift as the source of the RG-invariant g_0²F²; the leading coefficient c_blk |

Conditional items: X-ND, X-MONTEL, X-CAUCHY, X-IVND | H-Bal-3/3G; LAP-1, X-NTAF | H-Bal-1/3L/3T; X-SRC-RED | H-Bal-loc.
Implications from OPEN hypotheses: X-MOM, X-ARP, X-SRC-CT. Unconditional: X-WIL, X-KER, X-2GRID, X-CONT-G (free model).
Session 1 counted X-NTAF as OPEN; it is now PROVEN-HERE in the two-sided form and its sharp form is the OPEN
X-NTAF-sharp. Session 1's OPEN "H-src' (composites)" is split into X-SRC-RED (proven | H-Bal-loc) and H-src'-diag (OPEN).
Nothing has been reviewed independently yet.

**Check x1** (checks/x1_criteria.md written before checks/x1_hodge_flow.py): A1-A3 exact (0.0 differences on sides 4
and 5); B1 min heat-kernel entry 1.14e-5 (τ = 0.5), 1.04e-3 (τ = 2); B2 far-link responses 2.96e-5, 1.62e-4. PASS.
0.5 s, 67 MB, one process, nice 10, threads 1. Run as `python3` without -I (numpy is in the user site); the script reads
no external files.

**Check x2** (checks/x2_criteria.md written before checks/x2_lap_gauss.py): A (LAP-1 in the exact 2D SU(2) Wilson model)
PASS; B (Gaussian two-grid variances, exact Fourier symbol) PASS; all pre-registered expectations met (A3, B3 a-c).
0.6 s wall, 162 MB peak, nice 10, threads 1, load 1.7, memory free 37%. Run as `python3` without -I (same reason as x1).

---

## 7. Relation to layer 1 (P) — which parts of H-Bal P re-derives

- **H-Bal-1 (flow):** P L4a is IMPORTED-NOT-YET-REVERIFIED; P re-derived the polarisation-tensor structure that
  defines β_j (L4a-Π, check c17(A)) and one-loop data from the D4 kernel. The flow bounds (0.31) themselves: not
  re-derived.
- **H-Bal-2 (Z-stability):** P L6 IMPORTED-NOT-YET-REVERIFIED.
- **H-Bal-3 (block laws):** P's ingredients — background field (L2, reduced via B-NA-red), propagators (L3s proven in
  a weaker scalar form; L3g imported), polymer expansion (Theorem CE, a d = 4 re-proof of Dimock's abstract theorem),
  the linear abelian package (N2-lin, N2-exp, PG, PG^(k), FP-ab, G♯_0-soft, F-df_0), the isolated-cube R-step
  (R4D-iso). **Caution:** under P's decision 4 these are proven for P's *soft* (Gaussian-constraint) kernel, not
  Balaban's δ-function constraint (0.17); they are analogues of H-Bal-3's ingredients, not re-derivations of H-Bal-3.
  H-Bal-3(3b)/3G ↔ P's E8* (fixed-depth cases proven, general OPEN) and L6loc.
- **Soft layer overlap:** P's L7a, L8a, L8b, L8c, L9a, L9a', L9a-m are the measure-form versions of X-ALG, X-IV,
  X-SYM, X-RP, X-LRP. New here: the continuous block map X-S4c (removing P's need for E8* for consistency),
  the state formulation X-CONS, the transfer-operator lemma X-OS, the flowed-observable lemmas, and the
  hypothesis-to-conclusion map of §0.

---

## 8. Next targets (updated session 2; recommended order)

1. **H-corr in the simplest non-trivial setting.** Prove the ℓ²-domination E|⟨χ, F^{(n)}⟩|² ≤ C||χ||² for the block
   curvature of the compact U(1) (Villain or Wilson) model at weak coupling in a small-field event, where the composite
   averaging is exactly linear on regular configurations (fluxes add); this would give H-cont there via X-2GRID and the
   proof of X-CONT-G, and test whether H-corr is the right interface to P's N5.
2. **H-bl directly.** X-KER needs only boundary-layer insensitivity; test whether H-bl follows from H-Bal-3L-type local
   bounds plus X-CONT-G-type counting without a full two-point bound.
3. **X-NTAF-sharp, W-AF2 side:** a Gaussian comparison for the single block-plaquette law in the small-field region,
   given H-Bal-3G; W-AF1 waits for Balaban's flow theorem.
4. **H-src'-diag:** identify the contact-term structure of ΔΨ as the supports merge (counterterm polynomials in h and
   its derivatives up to dimension 4).
5. **Review:** an independent read of §10 (LAP-1, X-KER, X-2GRID, X-CONT-G, X-SRC-RED) before any of it is used.

---

## 9. Session 2 (2026-10-27): pre-stated targets (written before any proof below)

Norm convention for this section: |·| is the Hilbert-Schmidt norm on N×N matrices, so for U ∈ SU(N)
**1 - N^{-1}Re tr U = |U - 1|²/(2N)** exactly (|U - 1|² = Σ_j |e^{iθ_j} - 1|² = Σ_j 4 sin²(θ_j/2)). Regularity sets
R_m(ε) use this norm.

**T1 (X-NTAF, target).** For a coarse plaquette p at resolution m, under hypotheses to be stated in local form
(one-link density ratios on a local regular event, and a per-plaquette tail bound), prove
c_- g_{m,K}² ≤ E_{K}[1 - N^{-1}Re tr V^{(m)}_p] ≤ c_+ g_{m,K}² p(g_{m,K})² uniformly in K and in the volume, with
explicit c_±, and pass it to every limit point; then read off the asymptotic-freedom signature through H-Bal-1. If the
sharp form (coefficient (N²-1)/(8N)-type and the 2b_0 rate) is not reachable, name the wall.

**T2 (H-cont, target).** (i) Reduce ker T = 0 to a condition weaker than translation continuity, if one exists.
(ii) Prove an exact identity reducing the two-grid comparison at sub-block shift s = jL^{-n} to the law of ONE
resolution n and a single averaging step applied on two grids offset by j/L of a block. (iii) Prove the resulting
estimate in the free abelian Gaussian model with the linearised S4' averaging (layer-1 linear package), uniformly in the
cutoff and the volume. (iv) Say what the interacting case needs.

**T3 (H-src, target).** State H-src for the action density as UV stability with a position-dependent bare coupling, in a
form where the divergent local counterterms drop out exactly; prove that it bounds the connected Schwinger functions of
the action density at separated supports; reduce it to a multiscale local polymer representation of log Z.

**T4.** A section "What a reader needs to trust".

Check x2 criteria are in checks/x2_criteria.md (written before checks/x2_*.py).

---

## 10. Session 2 results

### 10.1 T1: asymptotic-freedom form of non-triviality

Notation. For a coarse link b of Λ_m and u ∈ SU(N), T_{b,u}: C_m → C_m multiplies V_b on the left by u and fixes every
other link; it preserves Haar measure on C_m. For a coarse plaquette p with b ∈ ∂p, oriented to start with b,
V_p = V_bY with Y independent of V_b, so (T_{b,u}V)_p = uV_p. P_p := N^{-1}Re tr V_p, so 1 - P_p = |V_p - 1|²/(2N).

**H-Bal-3L (one-link density ratios on a local regular event). IMPORTED-NOT-YET-REVERIFIED** (no source states it in
this form). There are α ∈ (0, 1], A_1, E_1 < ∞ and η_L ∈ [0, 1/4], **independent of K and of the volume**, such that
for every m, every K ≥ m and every coarse link b: ν_{K,m} has a density ρ w.r.t. Haar on C_m, and there is a Borel set
G_b ⊂ C_m with ν_{K,m}(C_m \ G_b) ≤ η_L such that for every V ∈ G_b, ρ(V) > 0, and for every X ∈ su(N) with |X| = 1 and
real |s| < α:
  ρ(T_{b,e^{sX}}V)/ρ(V) = q(s) exp(-(1/g_{m,K}²) a(s) + e(s)),
with q(s) ∈ [1/3, 3], and a, e (depending on V, b, X) real on real s, extending holomorphically to the complex disc
|s| < α, with a(0) = e(0) = 0, |a| ≤ A_1 and |e| ≤ E_1 there.
- *Relation to H-Bal-3 (ARGUED, uncounted).* In finite volume, with G_b = R_m(ε_0/2), α ≤ ε_0/2, (3a) gives the ratio
  with q = (1 + R(T V))/(1 + R(V)) ∈ [1/3, 3] (|R| ≤ 1/2), a(s) = A^η(U_k(T V)) - A^η(U_k(V)), e(s) = E(T V) - E(V).
  Volume-uniform bounds on these one-link increments need the dependence of the background U_k(V) and of the polymers on
  V_b to decay away from b (CMP 102 Proposition 9, (190) [via P NOTES §9.7]); a volume-uniform local G_b needs the
  large-field R-operation to localise (CMP 122 [not-read]). This is the one-link content of H-Bal-3G.

**H-Bal-3T (per-plaquette tail). IMPORTED-NOT-YET-REVERIFIED.** There is p_* > 1/2 such that, with
p(x) := (log(1/x))^{p_*}, for every coarse plaquette p, every m and K ≥ m, uniformly in the volume:
ν_{K,m}(|V_p - 1| ≥ g_{m,K} p(g_{m,K})) ≤ g_{m,K}².
- *Source analogue (ARGUED).* Dimock's φ⁴_3 large-field split uses thresholds p_k = (-log λ_k)^p on rescaled fields
  with a factor e^{-O(1)p_k²} per large-field cube (Dimock II, eqs. 9-12 [via P NOTES §2]); e^{-c p²} ≤ x² for small x
  when 2p_* > 1. The YM transposition (field = g × rescaled field) is [unverified].

**Lemma C2 (second difference from a holomorphic bound). PROVEN-HERE.** If f is holomorphic on |z| < α, f(0) = 0 and
|f| ≤ A there, then |f(s) + f(-s)| ≤ (8/3)A s²/α² for real |s| ≤ α/2.
*Proof.* f(s) + f(-s) = 2Σ_{k≥1}c_{2k}s^{2k} with |c_n| ≤ A/α^n (Cauchy), so |f(s) + f(-s)| ≤ 2A x/(1 - x) with
x = (s/α)² ≤ 1/4, and 2x/(1 - x) ≤ (8/3)x. ∎

**Lemma LAP-1 (one-link anti-concentration). PROVEN-HERE | H-Bal-3L.** Put C_* := (4/3)(A_1 + γ²E_1)/α². If
g := g_{m,K} ≤ α/2 and 0 < r ≤ 1/(2π), then for every coarse plaquette p:
  ν_{K,m}(|V_p - 1| < r g) ≤ η_L + 3π r e^{C_*}.
*Proof.* Fix b ∈ ∂p and X ∈ su(N), |X| = 1. Let ρ_0 := rg and S := G_b ∩ {|V_p - 1| < ρ_0}.
(1) *Pair inequality.* For V ∈ S and real |s| ≤ g (so |s| ≤ α/2), H-Bal-3L and Lemma C2 give
ρ(T_{e^{sX}}V)ρ(T_{e^{-sX}}V)/ρ(V)² = q(s)q(-s)exp(-(a(s) + a(-s))/g² + e(s) + e(-s)) ≥ (1/9)exp(-(8/3)(A_1/g² + E_1)s²/α²),
so by AM-GM ρ(T_{e^{sX}}V) + ρ(T_{e^{-sX}}V) ≥ 2c ρ(V) with c := (1/3)e^{-C_*} (using s² ≤ g², g ≤ γ). Haar invariance of
T gives ν(T_uS) = ∫_S ρ(T_uV)dV, hence ν(T_{e^{sX}}S) + ν(T_{e^{-sX}}S) ≥ 2c ν(S).
(2) *Disjointness.* If W ∈ T_uS ∩ T_{u'}S then W_p = uV_p = u'V'_p with V, V' ∈ S, and by unitary invariance of |·|,
|u - u'| ≤ |1 - V_p| + |V'_p - 1| < 2ρ_0. So T_uS and T_{u'}S are disjoint when |u - u'| ≥ 2ρ_0.
(3) *A packing on one one-parameter subgroup.* Let iθ_k be the eigenvalues of X (Σθ_k² = 1, |θ_k| ≤ 1). For real
|σ| ≤ π, |e^{σX} - 1|² = Σ_k 4 sin²(σθ_k/2) ≥ (4/π²)σ². Put t := πρ_0, J := ⌊1/(πr)⌋ ≥ 1/(2πr), u_i := e^{itX} for
0 < |i| ≤ J. Then |i - i'|t ≤ 2Jt ≤ 2g ≤ π, so |u_i - u_{i'}| = |e^{(i-i')tX} - 1| ≥ (2/π)|i - i'|t ≥ 2ρ_0 for i ≠ i', and
every |it| ≤ Jt ≤ g. By (2) the 2J sets T_{u_i}S are disjoint, so 1 ≥ Σ_{i=1}^J [ν(T_{u_i}S) + ν(T_{u_{-i}}S)] ≥ 2Jc ν(S).
Hence ν(S) ≤ 1/(2Jc) ≤ πr/c = 3πr e^{C_*}, and ν(|V_p - 1| < ρ_0) ≤ ν(S) + ν(G_b^c). ∎

**Theorem X-NTAF (two-sided asymptotic-freedom bound). PROVEN-HERE | H-Bal-1, H-Bal-3L, H-Bal-3T.**
Put δ_* := e^{-2C_*}/(288π²N). Assume γ ≤ min(α/2, e^{-p_*}). Then for every m, every coarse plaquette p of Λ_m, and
every limit point ω (finite volume, X-ALG, or infinite volume, X-IV), writing P_{p,m} := N^{-1}Re tr V^{(m)}_p:
  (δ_*/2) / (1/g² + β' m log L) ≤ ω(1 - P_{p,m}) ≤ φ(G_m),  G_m := (1/g² + β m log L)^{-1/2},
  φ(x) := x²(p(x)²/(2N) + 2).
The same two bounds hold for E_K[1 - P_{p,m}] at every K ≥ m, uniformly in K and in the volume.
*Proof.* Lower: with r_* := e^{-C_*}/(12π) (≤ 1/(2π)) and δ_* = r_*²/(2N), {1 - P_p < δ_*g²} = {|V_p - 1| < r_*g}; LAP-1
gives probability ≤ η_L + 1/4 ≤ 1/2, so E_K[1 - P_p] ≥ (δ_*/2)g_{m,K}² ≥ (δ_*/2)/(1/g² + β'm log L) by H-Bal-1.
Upper: on {|V_p - 1| < g_{m,K}p(g_{m,K})}, 1 - P_p < g²p(g)²/(2N); elsewhere 1 - P_p ≤ 2, on probability ≤ g² (H-Bal-3T).
So E_K[1 - P_p] ≤ φ(g_{m,K}). φ is increasing on (0, e^{-p_*}] (d/dx[x² log(1/x)^{2p_*}] = 2x log(1/x)^{2p_*-1}(log(1/x) - p_*)),
and g_{m,K} ≤ G_m by H-Bal-1. 1 - P_{p,m} is a block generator (bounded, continuous, gauge invariant), so ω(1 - P_{p,m})
is the limit of E_{K_j}[1 - P_{p,m}] along the defining subsequence, and both bounds pass. ∎

**Corollary X-NTAF-AF (the asymptotic-freedom signature). PROVEN-HERE | same.** As m → ∞ at fixed g:
  δ_*/(2β' log L) ≤ liminf m·ω(1 - P_{p,m}),  ω(1 - P_{p,m}) ≤ (1 + o(1)) (½ log m)^{2p_*}/(2Nβ m log L).
So the block plaquette at physical scale μ = L^m tends to its free (flat) value 1 and the deviation decays
**logarithmically in μ** (between 1/log μ and (log log μ)^{2p_*}/log μ). Consequences: (i) in infinite volume the
projective family (ν_{*,m})_m is not dilation invariant (a dilation-invariant family has m-independent ω(1 - P_{p,m}), but ω(1 - P_{p,0}) > 0
and ω(1 - P_{p,m}) → 0); (ii) no power-law approach ω(1 - P_{p,m}) ≤ C L^{-θm}, θ > 0, is possible (lower bound);
(iii) at every finite resolution the limit is not flat. This excludes massless free fields with canonical scaling
(m-independent block laws) and any theory whose block plaquettes approach the free value with a power (anomalous
dimension) — both by statements about the constructed state, not about perturbation theory.

**Corollary X-WIL (unconditional instance). PROVEN-HERE.** For the Wilson SU(N) lattice gauge theory in any dimension d
on any finite periodic lattice with β = 2N/g² and g ≤ 1/2: 1 - ⟨P_p⟩ ≥ δ_W g²/2 with δ_W := e^{-2C_W}/(288π²N),
C_W := (16/3)(d - 1)√N(e - 1).
*Proof.* Density exp(-(1/g²)Σ_p|U_p - 1|²) with respect to Haar, so H-Bal-3L holds with G_b = everything, η_L = 0, q ≡ 1,
e ≡ 0, α = 1, and a(s) = Σ_{p∋b}(|e^{sX}U'_p - 1|² - |U'_p - 1|²) (each plaquette rotated, and inverted if needed, to begin
with b; |W - 1| = |W^{-1} - 1| and is conjugation invariant). For real s, |W - 1|² = 2N - tr W - tr W^*; the holomorphic
extension of each term is -tr((e^{sX} - 1)U') - tr(U'^*(e^{-sX} - 1)), of modulus ≤ 2√N|e^{sX} - 1| ≤ 2√N(e^{|s|} - 1),
and there are 2(d - 1) plaquettes per link, so A_1 = 4(d - 1)√N(e - 1). Apply LAP-1 and the lower half of X-NTAF at
fixed g (no H-Bal-1 needed). ∎ (Constants are far from sharp: check x2 A.)

**Check x2 A (criteria first, PASS).** 2D open-boundary SU(2) Wilson model (plaquettes i.i.d.), where H-Bal-3L holds
exactly with A_1 = 9.72, C_* = 12.96, δ_* = 9.7e-16. A1, A2: the lemma's bounds hold at g = 0.05-0.5 (trivially, the
constants being lossy). A3 (expectation): E[1 - P]/g² = 0.37494 at g = 0.05 against the Gaussian value 3/8. A4: the
core pair inequality ν(T_uS) ≥ c_s ν(S) holds in all 12 cases; the measured ratio is 0.37-0.94 against c_s = 2e-6 to 0.44.

**X-NTAF-sharp (OPEN; the wall named).** Target: ω(1 - P_{p,m}) = c_blk g_m²(1 + o(1)) with g_m² ~ 1/(2b_0 m log L)
and c_blk := (N² - 1)κ_blk/(4N), κ_blk := lim_r ||Π_ex ψ^{(r)}||² the Gaussian block-plaquette constant of §10.2
(0.105 at depth 3 on a coarse 2⁴ torus, check x2 B2; finite-volume, informational). Two separate walls:
- **W-AF1 (flow coefficient):** β = β' = 2b_0 log L + o(1) in H-Bal-1. CMP 109 Theorem 2 gives only some 0 < β ≤ β',
  with the proof deferred by Balaban (P NOTES §9.4; "no statement β_j → 2b_0 log L appears in CMP 109").
- **W-AF2 (= H-corr, §10.2):** a Gaussian comparison for block observables in the small-field region, uniform in the
  depth: it would replace p(g)² by O(1) in the upper bound and give the coefficient c_blk. LAP-1 uses only one-link
  density ratios; the upper bound needs the joint fluctuation of the whole block, which is a correlation-function
  statement (Dimock III: "can be adapted to treat correlation functions as well", not done [via P]).

### 10.2 T2: time continuity (ker T = 0)

**Lemma X-KER (the kernel sees only the reflection plane). PROVEN-HERE | X-OS.** In the setting of X-OS, let
𝔄_{++}(d) ⊂ 𝔄_+ be the C*-subalgebra generated by the block generators all of whose blocks lie in {x_0 ≥ Π_0 + d},
d ∈ 2D_+, and 𝔄_{++} := ∪_d 𝔄_{++}(d). Then [𝔄_{++}] ⊂ 𝒦^⊥. Hence: (i) 𝒦 = {0} iff [𝔄_{++}] is dense in H_ω; (ii) it
suffices (**H-bl**, boundary-layer approximation) that every element F of the *-algebra generated by the block
generators of 𝔄_+ be an L²(ω)-limit of elements of 𝔄_{++}; (iii) H-cont-time (L²(ω)-continuity of time translations on generators) implies H-bl.
*Proof.* For G ∈ 𝔄_{++}(d) and s := d: τ_{-s}G ∈ 𝔄_+ (its blocks are translated by -s ∈ D and stay on the positive side;
translated generators are generators), and T(s)[τ_{-s}G] = [G]. So [G] ∈ Ran T(s). T(s) is bounded self-adjoint with
ker T(s) = 𝒦 (X-OS (iii)), so closure(Ran T(s)) = 𝒦^⊥. (i) follows. (ii): ||[F] - [G]||²_OS = ω(θ(F - G)^*(F - G)) ≤
||θ(F - G)||_{L²(ω)}||F - G||_{L²(ω)} = ||F - G||²_{L²(ω)} (θ preserves ω), so L²-approximation gives OS-approximation
and [F] ∈ 𝒦^⊥ for every such F; these F are norm-dense in 𝔄_+, hence [·]-dense in H_ω. (iii): τ_sF ∈ 𝔄_{++}(s) for F ∈ 𝔄_+. ∎
- H-bl involves no translation: it asks that block observables touching Π_0 be insensitive, in L²(ω), to the block
  variables in a thin layer at Π_0. It is weaker than H-cont-time.

**Lemma X-2GRID (two-grid comparison = one resolution's law + one two-grid step). PROVEN-HERE.** Let n > m, K ≥ n,
s = jL^{-n}e (e a coordinate vector, j ∈ Z), and let W := V^{(n)}_{K,0} ~ ν_{K,n}. Then (i) V^{(r)}_{K,s} = V^{(r)}_{K,0}
for every r ≥ n (as functions on Ω_K); (ii) after identifying the s-translated resolution-r lattice (r < n) with Λ_r
by translation, V^{(n-1)}_{K,s} = A(τ_{-j}W) where (τ_{-j}W)(b) := W(b + je), and V^{(m)}_{K,s} = A^{n-1-m}(A(τ_{-j}W));
(iii) therefore for every block generator F = f(V^{(m)}|_X):
  F(V^{(m)}_{K,s}) - F(V^{(m)}_{K,0}) = Φ(A(τ_{-j}W)) - Φ(A(W)),  Φ := f ∘ A^{n-1-m}(·)|_X,
and the joint law of (V^{(m)}_{K,0}|_X, V^{(m)}_{K,s}|_X) is the push-forward of the single-resolution law ν_{K,n} under
the deterministic map W ↦ (Φ̃(A(W)), Φ̃(A(τ_{-j}W))), Φ̃ := A^{n-1-m}(·)|_X.
*Proof.* (i) For r ≥ n, s ∈ L^{-r}Z^4, so the s-translated tilings at all resolutions ≥ r coincide with the standard ones
(the tiling by cubes of side L^{-r'} is invariant under translations in L^{-r'}Z^4 ⊃ L^{-r}Z^4), and the block maps are
defined by the tilings. (ii) The s-translated resolution-(n-1) tiling is the standard one translated by j resolution-n
sites; the averaging formula is translation covariant, so its output on the translated blocks equals A applied to the
translated input. Coarser levels: the s-translated hierarchy is the translate of the standard one. (iii) is (i)-(ii). ∎
- **Reading.** "Uniform control of joint laws on two grids" is a statement about the law of ONE resolution n, tested on
  functions of the form Φ∘A∘τ_{-j} - Φ∘A. The two hierarchies differ in exactly one averaging step, on two grids offset by
  j/L of a block. With X-KER and X-OS, 𝒦 = {0} ⇐ for every m, f, X: sup_K E_{ν_{K,n}}|Φ(A(τ_{-j}W)) - Φ(A(W))|² → 0 as
  n → ∞ with j = 2 (s_n = 2L^{-n} ∈ 2D_+).

**Lemma X-CONT-G (the two-grid estimate in the free abelian Gaussian model). PROVEN-HERE.**
Setting: fine torus (Z/nZ)^4 in fine units; the field strength F = dA of the noncompact abelian model with action
(β/2)||dA||², i.e. the Gaussian measure on 2-forms with covariance β^{-1}Π_ex (Π_ex the orthogonal projector onto exact
2-forms); the linearised S4' averaging (P's Q_root) iterated r times; block side ℓ := L^r ≤ n/2. For a level-r plaquette P
(plane μν) let F^{(r)}_s(P) be the curvature of the level-r block field on the grid translated by s ∈ Z^4 (fine units).
(i) (composite flux) F^{(r)}_0(P) = ⟨ψ_P, F⟩ with ψ_P := ℓ^{-4}Σ_{y∈B(P)} 1_{Sq_y}, Sq_y the straight ℓ × ℓ square of fine
plaquettes in the μν plane with corner y, B(P) the level-r block of the base point of P (side ℓ); F^{(r)}_s(P) = ⟨τ_sψ_P, F⟩.
(ii) For s = je_a, 0 ≤ j ≤ ℓ, w := j/ℓ: E|F^{(r)}_s(P) - F^{(r)}_0(P)|² ≤ (4/β)w if a ∉ {μ, ν}, ≤ (4/β)w² if a ∈ {μ, ν}.
(iii) E|F^{(r)}_0(P)|² ≤ 1/β (scale invariance), uniformly in r, n.
*Proof.* (i) One step is P's Lemma 2.2(i) (LINEAR_PACKAGE §2), re-derived here: in dA'(P) = A'(X, μ) + A'(X + e_μ, ν)
- A'(X + e_ν, μ) - A'(X, ν), pair the four contour averages by the common (σ, offset u = y - LX); the axial legs at the
shared roots cancel, leaving the boundary of the straight L × L square at LX + u; averaging over (σ, u) gives
avg_{u}Φ_A(sq_{LX+u}). Induction: if the level-q curvature is avg_{y∈B_q}Φ_A(Sq^{(q)}_y), then the level-(q+1) curvature is
avg_{y'}Σ_{P' ∈ sq'_{y'}} avg_{u}Φ_A(Sq^{(q)}_{c_{P'} + u}) = avg_{y', u}Φ_A(Sq^{(q+1)}_{L^q y' + u}) (fluxes add; the
squares with a common offset u tile the big square), and (y', u) ↦ L^q y' + u is a bijection onto B_{q+1}. Translation
covariance of the linear map gives the shifted statement. (ii) Var⟨φ, F⟩ = β^{-1}||Π_exφ||² ≤ β^{-1}||φ||². With
(B + s) \ B and B \ (B + s) slabs of jℓ³ sites, τ_sψ - ψ = w(ψ_top - ψ_bot), ψ_slab := (jℓ³)^{-1}Σ_{y∈slab}1_{Sq_y}, so
||τ_sψ - ψ||² ≤ 4w² max||ψ_slab||² and ||ψ_slab||² ≤ ||ψ_slab||_∞||ψ_slab||_1 with ||ψ_slab||_1 = ℓ². A plaquette p lies
in Sq_y only if y agrees with p in the two directions transverse to the plane and lies in an ℓ × ℓ window in the plane:
if a ∉ {μ, ν} the slab condition fixes one transverse coordinate, so the count is ≤ ℓ² and ||ψ_slab||_∞ ≤ 1/(jℓ),
||ψ_slab||² ≤ ℓ/j, giving 4w²ℓ/j = 4w; if a ∈ {μ, ν} the count is ≤ jℓ, ||ψ_slab||_∞ ≤ ℓ^{-2}, ||ψ_slab||² ≤ 1, giving 4w².
(iii) ||ψ||² ≤ ||ψ||_∞||ψ||_1 ≤ ℓ^{-2}·ℓ². ∎
- Consequence: for f Lipschitz (constant Λ) in the block curvatures of finitely many coarse plaquettes X,
  E|f(F_s|_X) - f(F_0|_X)|² ≤ Λ²|X|(4/β)w: H-cont with exponent 1/2 (in L²) in this model, uniformly in the cutoff and the
  volume. (RP of this model is not re-derived here; only the estimate is claimed.)

**Check x2 B (criteria first, PASS).** Exact variances from the Fourier symbol of Π_ex at L = 3, r = 1, 2, 3 (fine sides
6, 18, 54), both orientations, all j: B1 holds with max V/(4w) ≤ 0.093; B2 ||Π_exψ||² = 0.144, 0.109, 0.105. B3 (all
expectations met): (a) the **one-step** discrepancy (r = 1, j = 1) is 42% (perpendicular shift) and 67% (in-plane) of the
plaquette variance itself; (b) at fixed j = 1, V falls by a factor ≈ 9 per level (V ∝ w², sharper than the proven 4w);
(c) at fixed w = 1/3, V(r = 3)/V(r = 2) = 0.94, 0.95 (cutoff independence).

**Finding (from X-2GRID + x2 B3).** The single two-grid step is NOT small in any per-plaquette norm: offsetting one
averaging step by j/L of a block changes the next-level plaquettes by O(1) of their own fluctuation. Smallness appears
only after composing with the remaining n - 1 - m averaging steps, through cancellation (a difference of translates of
one smooth composite test form). So H-cont cannot be reduced to a single-step bound in a norm on single-step outputs;
the reducible form is X-2GRID's: a single-resolution law tested on composite functions.

**What the interacting case needs (OPEN; implication ARGUED).**
- **H-corr (two-point domination of block curvature, every resolution).** Uniformly in K ≥ n, n and the volume, for the
  level-n block plaquette logarithms 𝔉^{(n)} parallel-transported to a common coarse root (small-field gauge) and every
  test 2-form χ: E_{ν_{K,n}}|⟨χ, 𝔉^{(n)}⟩|² ≤ C_c g_n²||χ||²_{ℓ²}, on the small-field event.
- **H-lin (linearisation of the composite averaging).** The level-m block plaquette log of A^{n-m}(W) (either grid) equals
  the transported linear average ⟨ψ, 𝔉^{(n)}⟩ up to an error o(1) in L²(ν_{K,n}) as n → ∞, uniformly in K.
- ARGUED: H-corr + H-lin ⇒ H-cont-time, by X-2GRID and the proof of X-CONT-G (which uses only ||Π_exφ|| ≤ ||φ||, i.e.
  exactly an ℓ²-domination, so β^{-1} → C_c g_n²). Then 𝒦 = {0} by X-KER.
- **Why the single-step small-field statement is not provable with the current layer-1 package.** In Balaban's step
  (CMP 109 (2.13) [via P NOTES §9.5]) the δ-constraint fixes A(W) on one grid; the other grid's A(τ_{-j}W) is an
  unconstrained functional of the fluctuation field, and its law needs the fluctuation covariance C^{(k)} =
  (C*Δ^{(k)}C)^{-1} at general backgrounds (Balaban CMP 99 propagators [not-read]; P's node N5, OPEN). P's linear package
  controls background-response kernels (B_k ↦ r, f_0; exponentially local, N2-exp), not that covariance
  (LINEAR_PACKAGE §9 "Not the fluctuation covariance"). H-corr is the same correlation input as W-AF2: one wall.

### 10.3 T3: sources for the action density

Put Y_K(h) := -Σ_p h(x_p)|U_p - 1|² (x_p the plaquette centre, h real, bounded, Borel). Then
E_K[e^{zY_K(h)}] = Z_K[1/g_0² + zh]/Z_K[1/g_0²], the ratio of Wilson partition functions with the **position-dependent
bare inverse coupling** 1/g_0(x)² = 1/g_0² + zh(x) (density exp(-Σ_p (1/g_0(x_p)²)|U_p - 1|²)). An additive O(1) shift of
1/g_0² is, to leading order, the same shift of the renormalised 1/g² (∂(1/g_0²)/∂(1/g²) → 1 under H-Bal-1-type flows;
ARGUED), so this is the source conjugate to the RG-invariant combination g_0²tr F²_can (ARGUED; at separated points
⟨g_0²F²(x) g_0²F²(y)⟩_c ~ g(|x - y|)⁴/|x - y|⁸, finite and non-zero).

**H-src' (n, δ, r_0): stability with a position-dependent coupling, separated supports** (hypothesis form; implied by
H-Bal-loc, Lemma X-SRC-RED below; n ≥ 2).
For real h_1, ..., h_n with |h_i| ≤ 1 and pairwise distances of supports ≥ δ > 0, put
Ψ_K(z) := log E_K[exp(Σ_i z_iY_K(h_i))], z ∈ C^n. Require: E_K[exp Σ z_iY_K(h_i)] ≠ 0 on the polydisc D := {|z_i| < r_0},
and the inclusion-exclusion
  ΔΨ_K(z) := Σ_{S⊂{1..n}} (-1)^{n-|S|} Ψ_K(z_S)  (z_S: z_i for i ∈ S, 0 otherwise)
obeys |ΔΨ_K| ≤ C_s on D, uniformly in K.

**Lemma X-SRC-CT (counterterms drop out; connected functions at separated points). PROVEN-HERE (implication).**
Under H-src'(n, δ, r_0): (i) every functional of the form Σ_x c_K(x; η|_{B(x,ρ)}) with ρ < δ/2 (a local counterterm of
range < δ/2 in the coupling field η = Σz_ih_i) contributes 0 to ΔΨ_K; (ii) the joint cumulant (connected n-point
function) of Y_K(h_1), ..., Y_K(h_n) obeys |κ_K(Y_K(h_1), ..., Y_K(h_n))| ≤ C_s r_0^{-n}, uniformly in K; (iii) along a
subsequence these cumulants converge for every tuple from a countable family of such (h_i).
*Proof.* (i) A ball of radius ρ < δ/2 meets at most one supp h_i, so each term depends on at most one z_i; for a function
independent of z_i the terms S and S ∪ {i} cancel in pairs. (ii) Ψ_K is analytic on D (finite-dimensional integral,
non-vanishing). κ_K = ∂^nΨ_K/∂z_1⋯∂z_n(0) = ∂^nΔΨ_K/∂z_1⋯∂z_n(0), since every other term of ΔΨ_K is independent of some
z_i; Cauchy's estimate on polydiscs of radii → r_0 gives the bound. (iii) Bounded sequences in C, diagonal argument. ∎
- H-src' says nothing at coincident points: the diagonal contact terms (needed for OS0 in the X-MOM sense and for
  distributions on all of T^{4n}) are **H-src'-diag, OPEN**.

**H-Bal-loc (multiscale local representation of log Z with a coupling field). IMPORTED-NOT-YET-REVERIFIED** (no source
states it; it is what Balaban's induction with a position-dependent coupling should give). In finite physical volume |T|,
for every complex coupling field η with ||η||_∞ < r_0:
  log Z_K[1/g_0² + η] - log Z_K[1/g_0²] = CT_K[η] + Σ_{r=1}^{K} Σ_{X∈𝒫_r} a_{K,r}(X; η) + R_K[η],
where 𝒫_r is the set of polymers (connected unions of cubes of physical side ML^{-r}), a_{K,r}(X; η) depends only on η|_X
with |a_{K,r}(X; η)| ≤ a_0e^{-κ d_r(X)} (d_r = tree length in units of the cube side), κ ≥ 2κ_0 (P's κ_0 ≈ 151.3), CT_K is
a local counterterm of range ρ_K ≤ ML^{-K}·O(1), and |R_K[η]| ≤ C_IR (the unit-scale remainder), all uniformly in K.

**Lemma X-SRC-RED. PROVEN-HERE | H-Bal-loc.** H-Bal-loc implies H-src'(n, δ, r_0) for every n ≥ 2, δ (with K large enough
that ρ_K < δ/2), with
  C_s ≤ 2^n [ a_0 K_0 e^{4(κ-κ_0)} |T| M^{-4} Σ_{r≥1} L^{4r} e^{-(κ-κ_0)δL^r/M} + C_IR ]   (n ≥ 2),
K_0 = e^{κ_0}/6400 the polymer-sum constant of P's Theorem CE ((g4): Σ_{X∋□}e^{-κ_0 d(X)} ≤ K_0, with Lemma CE-geo').
*Proof.* Ψ_K(z_S) = log Z_K[1/g_0² + Σ_{i∈S}z_ih_i] - log Z_K[1/g_0²] (disjoint supports: ||Σz_ih_i||_∞ < r_0). In ΔΨ_K:
CT_K drops by X-SRC-CT (i); a polymer term a(X; ·) not meeting some supp h_i is independent of that z_i and drops;
the R_K terms contribute ≤ 2^n C_IR (2^n terms, each |R_K[η_S]| ≤ C_IR). A polymer meeting
supp h_1 and supp h_2 contains a connected union of segments joining two cubes at distance ≥ δ - 4ML^{-r} (cube diameter
2ML^{-r} in d = 4), so d_r(X) ≥ δL^r/M - 4. The cubes of resolution r number ≤ |T|L^{4r}/M^4. Hence
Σ_{X meets all supports}|a(X)| ≤ |T|L^{4r}M^{-4} a_0 e^{-(κ-κ_0)(δL^r/M - 4)} Σ_{X∋□}e^{-κ_0 d(X)}, and (g4) bounds the last sum
by K_0. Each surviving polymer appears in 2^n terms of ΔΨ. Sum over r. ∎
- **Reading.** "UV stability with a position-dependent coupling" in this form gives K-uniform bounds on all connected
  correlations of the action density at separated supports; the divergent self-energies of each coupling defect (the
  ε^{-4} pieces of X-SRC-GAP) are local and cancel exactly in ΔΨ. Balaban's published theorems (constant coupling,
  Z only) do not contain H-Bal-loc.

### 10.4 What a reader needs to trust

The conditional existence theorem (§0 table, §10) rests on the following, and on nothing else.
1. **Standard analysis** (named where used): Banach-Alaoglu and metrizability of the state space of a separable C*-algebra;
   Gelfand duality; Riesz representation; Portmanteau; Montel in several variables; Cauchy estimates; the spectral theorem
   and uniqueness of positive roots of positive operators; Minlos and the Schwartz kernel theorem (only for X-MOM).
2. **Lattice reflection positivity of the Wilson action** (Osterwalder-Seiler; re-derived in P and re-read here).
3. **H-Bal-1** (coupling flow): bare couplings g_0(ε, g) exist with 1/g² + β m log L ≤ 1/g_{m,K}² ≤ 1/g² + β' m log L and
   g_{m,K} ≤ γ, for some 0 < β ≤ β'. Used only for (c).
4. **H-Bal-3** (finite volume, each fixed resolution m): on regular block configurations the block law has a density
   𝒵^{-1}exp(-(1/g²)𝒜 + E)(1 + R) with 𝒜, E bounded and analytic on a fixed complex neighbourhood, |R| ≤ 1/2, and the
   irregular configurations have probability ≤ η_0 < 1. Used for (c) weak form (X-ND, X-MONTEL, X-CAUCHY).
5. **Local, volume-uniform versions** (needed only for infinite volume and for the asymptotic-freedom bound):
   H-Bal-3G (conditional densities and Peierls bound), H-Bal-3L (one-link density ratios with holomorphic increments on a
   local regular event of probability ≥ 3/4), H-Bal-3T (P(|V_p - 1| ≥ g p(g)) ≤ g²).
6. **For sources:** H-Bal-loc (multiscale local representation of log Z with a complex coupling field).
Not used anywhere: **H-Bal-2** (Balaban's published Z-stability bound). Unconditional (no hypothesis beyond 1-2): part (a)
(a consistent limit state on all block and flowed observables, finite and infinite volume), RP for all L-adic planes,
L-adic translation and hypercubic invariance, the OS Hilbert space with H ≥ 0 on 𝒦^⊥, X-KER, X-2GRID, X-WIL. Not
delivered under any of the above: 𝒦 = {0} (needs H-corr + H-lin, OPEN), rotation invariance, OS0 at coincident points,
uniqueness, clustering, mass gap. Status of items 3-6: IMPORTED-NOT-YET-REVERIFIED; items 5-6 are not stated in any
source and are this lane's formulations of what Balaban's inductive bounds should contain.
