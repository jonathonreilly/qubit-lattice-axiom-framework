---
claim_id: mdtn_truncated_gauge_supporting_lemmas_lean_ready_note_2026-11-01
claim_type: supporting_lemmas
claim_scope: >
  Finite-dimensional Gauss-law and combinatorial lemmas for truncated (MDTN / Kogut-Susskind j_max = 1/2)
  SU(2) and SU(3) lattice gauge theory on finite graphs (L^3 open or periodic boxes). Unperturbed statements
  only: projector structure, invariant-space dimensions, support/girth of gauge-invariant states, and the
  spectrum of the excitation number N on the physical subspace. No dynamics, no perturbation theory, no
  spectral-gap bound under perturbation. Not the Clay Yang-Mills problem.
upstream_dependencies: []
supersedes_sections: ["MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31 §2 (Lemma 1), §3 (Lemma 2)"]
runner: scripts/mdtn_supporting_lemmas_check_2026_11_01.py
status: proposed (unaudited); status authority is the independent audit lane only
---

# Truncated gauge (MDTN) supporting lemmas: Gauss projectors, site singlets, girth (Lean-ready)

**Date:** 2026-11-01
**Type:** supporting lemmas (proposed; unaudited). Status authority: independent audit lane only.
**Runner:** `scripts/mdtn_supporting_lemmas_check_2026_11_01.py` →
`logs/runner-cache/mdtn_supporting_lemmas_check_2026_11_01.txt` (108/108 checks PASS; numpy 2.5.4, scipy 1.18.1).
Run from the repo root: `python3 scripts/mdtn_supporting_lemmas_check_2026_11_01.py > logs/runner-cache/mdtn_supporting_lemmas_check_2026_11_01.txt`.

**Scope.** This note replaces the proofs of Lemma 1 (§2) and Lemma 2 (§3) of
`MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md` with self-contained,
finite-dimensional versions and records where the old statements were wrong or underspecified (§7). It does **not**
touch the Lift Proposition, the Main Theorem, or any statement about the spectrum of H = Σ n_ℓ − δ Σ (U_P + U_P†) for
δ ≠ 0. Everything below concerns the operators G_s^a, P_s, n_ℓ, N and the gauge-covariant link operators only.

**Status legend.** **[R]** rigorous, complete finite-dimensional proof given here (linear algebra over C, finite
combinatorics). **[F]** finite check: the statement is proved by exhaustive exact or floating-point computation over a
stated finite range, logged in the runner. **[Cit]** standard theorem cited, not reproved here (repo policy: attribution
only until rebuilt). Each lemma lists which parts carry which tag.

---

## 1. Definitions (finite, explicit)

### 1.1 Graphs

**D-Γ.** An *oriented lattice graph* Γ = (V, E, src, tgt) is a finite set V of sites, a finite set E of links and maps
src, tgt : E → V with **src(ℓ) ≠ tgt(ℓ)** (no self-loops). Multiple links between two sites are allowed in the
definition (they occur for L = 2 periodic), but all graphs used for the lattice statements are simple. The underlying
simple graph Γ̄ has an edge {u, v} iff some link joins u and v. star(s) := {(ℓ, e) : e = 0 and src ℓ = s, or e = 1 and
tgt ℓ = s} (the *legs* at s); deg(s) = |star(s)|.

**Boxes.** Fix L₁, L₂, L₃ ≥ 1.
* *Open box* B(L₁,L₂,L₃): V = Π_μ {0, …, L_μ}, links (x, μ) from x to x + e_μ whenever x + e_μ ∈ V; plaquettes
  (x; μ < ν) with all four links present. (L₁ = L₂ = L₃ = L is the L^3 box of plaquette cells.)
* *Periodic box* T_L = (Z_L)^3, L ≥ 3: V = (Z_L)^3, links (x, μ) from x to x + e_μ mod L, 3L³ links, 3L³ plaquettes.
  Every site has deg = 6. (L ≤ 2 creates multi-links (L = 2) or self-loops (L = 1) and is excluded.)
* A plaquette P is the cyclic sequence of four (link, orientation) pairs
  P = ((x,μ),+), ((x+e_μ,ν),+), ((x+e_ν,μ),−), ((x,ν),−).

### 1.2 Truncated link Hilbert space

Let G = SU(d), d ∈ {2, 3}, with Hermitian generators T^a (d = 2: T^a = σ^a/2, a = 1..3; d = 3: T^a = λ^a/2, Gell-Mann,
a = 1..8). The link irrep set is 𝓡 = {0} ∪ 𝓡*, with 𝓡* = {1} (SU(2): 1 ≙ the doublet **2**) or 𝓡* = {1, 2} (SU(3):
1 ≙ **3**, 2 ≙ **3̄**). For every link

  H_ℓ = C|0⟩ ⊕ ⊕_{r ∈ 𝓡*} (C^d ⊗ C^d),   dim H_ℓ = 1 + |𝓡*| d² = 5 (SU(2)), 19 (SU(3)),

with basis |0⟩, |r; i, j⟩ (i, j = 1..d). Index i is the *start leg* (src ℓ), index j the *end leg* (tgt ℓ).
H(Γ) = ⊗_{ℓ∈E} H_ℓ. This is the ASQR / j_max = 1/2 truncation of the Peter–Weyl space ⊕_λ V_λ ⊗ V_λ*.

**Leg generators** (anti-Hermitian d×d matrices, the convention of
`scripts/mdtn_ed_part3_ks_gauge_invariant_2026_10_31.py`):

| leg | r = 1 (**2** or **3**) | r = 2 (**3̄**, SU(3) only) |
|---|---|---|
| start (e = 0), acts on i | ρ₀¹(a) = (−iT^a)^T = −i T^{a T} | ρ₀²(a) = iT^a |
| end (e = 1), acts on j | ρ₁¹(a) = iT^a | ρ₁²(a) = −i T^{a*} |

A^a_{ℓ,e} acts on H_ℓ as 0 on C|0⟩ and on the block r as ρ_0^r(a) ⊗ 1 (e = 0) or 1 ⊗ ρ_1^r(a) (e = 1).
Write X^a := iT^a (the fundamental anti-Hermitian generator) and X̄^a := (X^a)* = −iT^{a*}. Then ρ₁¹ = X, ρ₀² = X
("**fundamental-type legs**") and ρ₀¹ = X̄ (because T^{aT} = T^{a*}), ρ₁² = X̄ ("**antifundamental-type legs**").
For SU(2), X̄^a = σ² X^a σ², so both leg types are equivalent to the doublet.

**Gauss generators.** G_s^a := Σ_{(ℓ,e)∈star(s)} A^a_{ℓ,e} (each term tensored with the identity on all other link
factors). **Site Casimir** C_s := Σ_a (G_s^a)† G_s^a = −Σ_a (G_s^a)².

**Physical subspace.** H_phys := ⋂_{s∈V} ⋂_a ker G_s^a.

### 1.3 Gauss projector: three equivalent definitions

* **(D2, Lean-primary)** P_s := the orthogonal projector onto ker C_s.
* **(D1, Haar)** P_s^Haar := ∫_G dg W_s(g), where W_s(g) := ⊗_{(ℓ,e)∈star(s)} w_{ℓ,e}(g) ⊗ 1, and w_{ℓ,e}(g) acts on
  H_ℓ as 1 on |0⟩ and as ḡ ⊗ 1 / 1 ⊗ g (r = 1, start / end) or g ⊗ 1 / 1 ⊗ ḡ (r = 2, start / end).
  (Then d/dt w(e^{tX^a})|_{t=0} = A^a_{ℓ,e}.)
* **(D3, SU(2) finite group)** P_s^{2O} := (1/48) Σ_{g∈2O} W_s(g), 2O ⊂ SU(2) the binary octahedral group (unit
  quaternions ±1, ±i, ±j, ±k, (±1±i±j±k)/2, (±u ± v)/√2 for u ≠ v ∈ {1,i,j,k}; 48 elements).

### 1.4 Excitation number and bands

n_ℓ := 1 − |0⟩⟨0|_ℓ (projector onto the nontrivial irreps on ℓ; MDTN's E_ℓ), N := Σ_ℓ n_ℓ,
E_k := ker(N − k) (exactly k excited links), k = 0, …, |E|.

**Configurations.** A configuration is c ∈ 𝓡^E. H_c := ⊗_ℓ (C|0⟩ if c_ℓ = 0, else the c_ℓ-block of H_ℓ), so
H = ⊕_c H_c orthogonally and E_k = ⊕_{|supp c| = k} H_c. For SU(3) identify 𝓡 = {0, 1, 2} with Z_3; for SU(2) with Z_2.
The *boundary* ∂c ∈ Z_p^V (p = 2 or 3) is (∂c)(s) := Σ_{ℓ: tgt ℓ = s} c_ℓ − Σ_{ℓ: src ℓ = s} c_ℓ mod p.
Z_1(Γ; Z_p) := ker ∂ (the Z_p 1-cycles). For SU(2), c ∈ Z_1 iff every site has even degree in supp c.

**Site leg counts.** For c and a site s, let a_s(c) := number of fundamental-type excited legs at s
(end legs of r = 1 links, start legs of r = 2 links) and b_s(c) := number of antifundamental-type excited legs.
Then (∂c)(s) ≡ a_s − b_s (mod 3) for SU(3) and ≡ a_s + b_s (mod 2) for SU(2). The *site space* is
K_s(c) := (C^d)^{⊗(a_s + b_s)} with the generators Σ_legs ρ(a) acting; Inv_s(c) := ⋂_a ker of that sum.

**Combinatorial weights.** Cat(m) = (2m choose m)/(m + 1). For SU(3), w(a, b) := number of walks on dominant weights
(p, q) ∈ N² from (0,0) to (0,0) that take a steps of type **3**: (p,q) → (p+1,q), (p−1,q+1), (p,q−1), then b steps of
type **3̄**: (p,q) → (p,q+1), (p+1,q−1), (p−1,q), never leaving N². (w(a,b) = w(b,a) by conjugation symmetry.)

---

## 2. Gauss lemmas (projector structure)

**Lemma G1 (leg algebra) — [R].** For every link ℓ and a, b: (i) A^a_{ℓ,e} is anti-Hermitian and preserves each
irrep block of H_ℓ; (ii) [A^a_{ℓ,0}, A^b_{ℓ,1}] = 0; (iii) [A^a_{ℓ,e}, n_ℓ] = 0.
*Proof.* (i) ρ_e^r(a) is ±i times a Hermitian matrix (T^a, T^{aT}, T^{a*} are Hermitian); block-diagonal by
definition. (ii) On each block they are M ⊗ 1 and 1 ⊗ M′. (iii) n_ℓ is the identity on each nontrivial block and 0 on
C|0⟩, where A vanishes. ∎ (Runner C: residuals 0.)

**Lemma G2 (P_s is an orthogonal projector) — [R].** C_s is Hermitian positive semidefinite,
ker C_s = ⋂_a ker G_s^a, and P_s (D2) satisfies P_s† = P_s = P_s².
*Proof.* ⟨ψ, C_s ψ⟩ = Σ_a ‖G_s^a ψ‖² ≥ 0, so C_s ψ = 0 ⇔ all G_s^a ψ = 0. The orthogonal projector onto a subspace is
self-adjoint and idempotent. ∎ *Lean-friendly form:* P_s = q(C_s) where q is the Lagrange polynomial with q(0) = 1 and
q(μ) = 0 at the nonzero eigenvalues μ of C_s; hence every operator commuting with C_s commutes with P_s.

**Lemma G3 (locality) — [R].** Write H = H_{star(s)} ⊗ H_{rest}, where H_{star(s)} := ⊗_{ℓ ∋ s} H_ℓ. Then
P_s = p_s ⊗ 1_{rest}, with p_s the orthogonal projector onto ker c_s ⊂ H_{star(s)}, c_s := Σ_a (g_s^a)† g_s^a and
g_s^a the star-local Gauss generator. In particular P_s commutes with every operator acting only on links ∉ star(s).
*Proof.* G_s^a = g_s^a ⊗ 1, so C_s = c_s ⊗ 1 and ker(c_s ⊗ 1) = ker c_s ⊗ H_{rest}; the orthogonal projector onto
K ⊗ H′ is p_K ⊗ 1. ∎

**Lemma G4 (commutation) — [R].** For all s, t ∈ V and all a, b with s ≠ t: [G_s^a, G_t^b] = 0. Hence
[C_s, C_t] = 0 and [P_s, P_t] = 0 for all s, t.
*Proof.* Terms of G_s^a and G_t^b on different links act on different tensor factors. A link ℓ shared by s and t has
s and t at different ends (no self-loops), so the two terms are A^a_{ℓ,0}, A^b_{ℓ,1} or vice versa, which commute by
G1(ii). (Multi-links: each shared link is treated separately.) Then C_s, C_t commute, so P_s = q_s(C_s) and
P_t = q_t(C_t) commute (G2). ∎ *Note:* G_s^a and G_s^b at the same site do **not** commute; only kernels are used.

**Lemma G5 (physical projector) — [R].** P_phys := Π_{s∈V} P_s (any order) is the orthogonal projector onto
H_phys = ⋂_s ker C_s.
*Proof.* Product of commuting orthogonal projectors is an orthogonal projector (self-adjoint by commutation, idempotent
by commutation + idempotence) with range ⋂ ranges: if ψ ∈ ⋂ ran P_s then P_phys ψ = ψ; conversely
P_s P_phys = P_phys gives ran P_phys ⊆ ran P_s. ∎ Induction on |V| (Mathlib `IsStarProjection.mul`).

**Lemma G6 (commutation with N and with plaquette operators).**
(a) **[R]** If an operator O on H satisfies [O, G_s^a] = 0 for all a, then [O, C_s] = [O, P_s] = 0 and
[O†, G_s^a] = 0. In particular [P_s, n_ℓ] = [P_s, N] = 0, and N leaves H_phys and each H_phys ∩ E_k invariant.
(b) **(Cov) — [R] + [F].** Let Ũ^{xy}_ℓ (x, y = 1..d) be the truncated link operators of the part-3 runner
(SU(2): Ũ^{xy} = d^{−1/2}(δ_{xi}δ_{yj} creation 0 → 1 + ε_{xi}ε_{yj} annihilation 1 → 0); SU(3): creation 0 → **3**
and annihilation **3̄** → 0 with δδ/√3, fusion **3** → **3̄** with ε_{xik}ε_{yjl}/2). Then for every link
  [A^a_{ℓ,0}, Ũ^{xy}] = Σ_z (−iT^a)_{xz} Ũ^{zy},   [A^a_{ℓ,1}, Ũ^{xy}] = −Σ_z Ũ^{xz} (−iT^a)_{zy}.
(c) **[R] given (b).** For a plaquette (or any closed walk) P = (ℓ₁,σ₁), …, (ℓ_m,σ_m), with
X_k := Ũ_{ℓ_k} if σ_k = + and X_k := (Ũ_{ℓ_k})^{†T} (i.e. (X_k)^{xy} = (Ũ^{yx}_{ℓ_k})†) if σ_k = −, the operator
O_P := Σ_{x₁..x_m} X_1^{x₁x₂} X_2^{x₂x₃} ⋯ X_m^{x_m x₁} satisfies [G_s^a, O_P] = [G_s^a, O_P†] = 0 for all s, a; hence
[P_s, O_P] = [P_s, O_P†] = 0 and O_P + O_P† preserves H_phys.
*Proof.* (a) C_s is a polynomial in the G_s^a; P_s = q(C_s) (G2). G anti-Hermitian: ([G,O])† = O†G† − G†O† = [G, O†].
(b) Each transition tensor is built from δ and ε, which are SU(d)-invariant tensors (ε because det g = 1, i.e.
infinitesimally Tr T^a = 0); differentiating the invariance identity gives the two formulas. Runner C checks both
identities exactly (residual 0 in floating point, all a, x, y) for both groups. (c) Taking the adjoint of (b) shows that
the reversed matrix X_k obeys the same left/right rule (left factor −iT at the traversal start, right factor at the
traversal end). In the product, the right-multiplication by −(−iT) at the end of X_k and the left-multiplication by
(−iT) at the start of X_{k+1} act at the same site and cancel in Σ_{x_{k+1}}; the closing pair cancels under the trace.
Generators at sites not on P commute trivially. ∎ Runner D: ‖[G_s^a, Tr Ũ_P]‖_max = 0 on the full 625-dim (SU(2)) and
130321-dim (SU(3)) single-plaquette spaces.

**Lemma G7 (equivalence of definitions).**
(a) **[Cit]** For G = SU(d) (compact, connected) and the continuous unitary representation W_s,
P_s^Haar = P_s (D1 = D2): Haar averaging is the orthogonal projector onto the fixed vectors, and for a connected Lie
group the fixed vectors of a finite-dimensional representation are exactly the common kernel of the derived
Lie-algebra action. (The (≤) direction is elementary; (≥) uses that exp(su(d)) generates SU(d).)
(b) **[Cit] + [F]** For SU(2) and every site of degree ≤ 7 (all sites of T_L and of open boxes have degree ≤ 6),
P_s^{2O} = P_s. Reason: the invariant ring of 2O acting on C² has no nonconstant invariant of degree < 8 (Klein), so
V_j^{2O} = 0 for 1 ≤ j ≤ 3, while 2^{⊗k} with k ≤ 7 contains only spins j ≤ 7/2. Runner B: for k = 1..7 legs,
‖P^{2O} − P^{Lie}‖_max ≤ 2.0e-15; for k = 8 the 2O-average has rank 15 > Cat(4) = 14 (so D3 fails at 8 legs, as
predicted); and on the full 625-dim plaquette space (1/48) Σ_{2O} W_s(g) = P_s to 1.1e-16.
*Use:* D3 makes P_s a finite average, i.e. Mathlib's `Representation.averageMap` (`isProj_averageMap`) for SU(2).

---

## 3. Site-singlet lemmas

**Lemma S1 (parity / triality obstruction) — [R].** Inv(2^{⊗k}) = 0 for odd k (SU(2)); for SU(3),
Inv(3^{⊗a} ⊗ 3̄^{⊗b}) = 0 unless a ≡ b (mod 3).
*Proof.* An invariant vector is annihilated by every generator, in particular by the Cartan element. SU(2):
Σ_i T³_i is diagonal in the product basis with eigenvalues in (1/2)Z, ≡ k/2 mod 1, never 0 for odd k. SU(3): the
hypercharge Y = (2/√3)T⁸ = diag(1/3, 1/3, −2/3) acts on **3̄** as −Y; on the product basis its eigenvalues are
≡ (a − b)/3 mod 1, never 0 unless 3 | a − b. ∎ Runner A: minimum |eigenvalue| ≥ 1/2 (SU(2), k = 1,3,5,7) and ≥ 1/3
exactly when a ≢ b (SU(3), a + b ≤ 6).

**Lemma S2 (SU(2) Catalan count) — [Cit] + [F].** dim Inv(2^{⊗2m}) = Cat(m).
*Proof sketch.* Clebsch–Gordan V_j ⊗ V_{1/2} = V_{j+1/2} ⊕ V_{j−1/2} (j ≥ 1/2), V_0 ⊗ V_{1/2} = V_{1/2} [Cit];
iterating, the multiplicity of V_0 in 2^{⊗k} is the number of walks 0 → 0 of k ±1 steps on N, i.e. Dyck paths of
semilength m, counted by Cat(m) (Mathlib `DyckWord.card_dyckWord_semilength_eq_catalan`). Runner A: Lie-kernel
dimension = Weyl-integration value = walk count = Catalan for k = 0..8 (1,0,1,0,2,0,5,0,14), for both
all-start and alternating-end leg patterns.

**Lemma S3 (SU(3) walk count) — [Cit] + [F].** dim Inv(3^{⊗a} ⊗ 3̄^{⊗b}) = w(a, b) (§1.4), independent of the order
of the factors.
*Proof sketch.* Minuscule Pieri rule V_{(p,q)} ⊗ **3** = ⊕ of the dominant ones among V_{(p+1,q)}, V_{(p−1,q+1)},
V_{(p,q−1)} (and conjugately for **3̄**) [Cit]; iterate. Runner A, a + b ≤ 6: nonzero values
w(1,1) = 1, w(3,0) = w(0,3) = 1, w(2,2) = 2, w(1,4) = w(4,1) = 3, w(6,0) = w(0,6) = 5, w(3,3) = 6, all others 0;
Lie kernel = Weyl integration = w(a, b) in every case, for two leg-ordering patterns.

**Truncation-specific content of S1–S3.** These use that every excited leg carries the (anti)fundamental. With
j_max = 1 (adjoint links) S1 fails (the adjoint has zero triality and integer spin) and S2/S3 are replaced by other
counts. Only Schur's Inv(V_λ) = 0 for nontrivial irreducible λ (degree ≥ 2 on the support; used in the old note)
survives for every truncation.

---

## 4. Configuration and graph lemmas

**Lemma C1 (block decomposition) — [R].** Each G_s^a preserves every H_c. Hence H_phys = ⊕_c (H_phys ∩ H_c), and,
after regrouping the 2|supp c| leg factors of H_c ≅ ⊗_{ℓ∈supp c} (C^d ⊗ C^d) by sites,
H_phys ∩ H_c ≅ ⊗_{s∈V} Inv_s(c), so dim(H_phys ∩ H_c) = Π_s dim Inv_s(c).
*Proof.* A^a_{ℓ,e} preserves irrep blocks (G1). On H_c, G_s^a = (Σ_{legs at s} ρ) ⊗ 1 in the site-regrouped
factorisation ⊗_s K_s(c); the regrouping is a permutation of tensor factors (valid because no link has both ends at
one site). Common kernel of commuting families acting on different tensor factors: ⋂_s ker(c_s ⊗ 1) = ⊗_s ker c_s
(induction on the number of factors, using ker(M ⊗ 1) ∩ ker(1 ⊗ M′) = ker M ⊗ ker M′ for finite-dimensional spaces). ∎

**Lemma C2 (support lemma) — [R].** If H_phys ∩ H_c ≠ 0 then c ∈ Z_1(Γ; Z_p) (SU(2): supp c is an even subgraph;
SU(3): ∂c = 0 with 1 ≙ **3**, 2 ≙ **3̄**). In particular every site has degree 0 or ≥ 2 in supp c.
*Proof.* By C1 every Inv_s(c) ≠ 0; by S1 a_s + b_s is even (SU(2)) or a_s ≡ b_s (mod 3) (SU(3)); this is
(∂c)(s) = 0 (§1.4). A site with exactly one excited leg would have (∂c)(s) = ±1 ≠ 0. ∎ Runner E checks, by brute
force over all configurations, that the nonzero blocks are **exactly** the Z_p-cycles (SU(2): open 1×1, 2×1, 2×2,
3×2, 1×1×1, 2×1×1, periodic 3×3; SU(3): open 1×1, 2×1, 2×2, 1×1×1).

**Lemma C3 (girth of boxes) — [R].** (a) Open boxes B(L₁,L₂,L₃) (any L_μ ≥ 1 with at least one plaquette) and T_L
with L ≥ 4 are simple graphs of girth exactly 4. (b) T_3 has girth 3 (the loops x, x+e_μ, x+2e_μ). (c) Every 4-cycle
of an open box and of T_L with L ≥ 5 is the boundary of a plaquette, so #4-cycles = #plaquettes; in T_4 the 4-cycles
are the 3·4³ plaquettes plus the 3L² = 48 straight winding loops {x, x+e_μ, x+2e_μ, x+3e_μ}.
*Proof.* Simplicity: for L ≥ 3 the six steps ±e_μ are pairwise distinct and nonzero mod L, so there are no
self-loops and no two links join the same pair of sites (open boxes: trivially). A closed walk of m ≤ 4 unit steps ±e_μ has net
displacement Δ ∈ Z³ with |Δ_μ| ≤ m and Δ ≡ 0 (mod L) (periodic) or Δ = 0 (open). If m < L or the box is open, Δ = 0;
then m is even (the coordinate-sum parity flips each step), excluding m = 3, and for m = 4 the steps are
{+e_μ, −e_μ, +e_ν, −e_ν}; a cycle cannot backtrack, so μ ≠ ν and the walk traverses a plaquette boundary. If L = 4
and m = 4, additionally |Δ_μ| = 4 for one μ forces four equal steps: a straight winding loop (3 directions × L² lines).
For L = 3, m = 3 equal steps close. Plaquettes exist, so girth ≤ 4. ∎ Runner F: T_3 girth 3; T_4: girth 4, 240 =
192 + 48 four-cycles; T_5: 375 = 375; T_6: 648 = 648; open 2×3×4: 98 = 98; open 3×3×3: 108 = 108.

**Lemma C4 (girth lemma; spectrum of N on H_phys) — [R].** Let Γ be an oriented lattice graph whose underlying
graph is simple with girth g < ∞ (no self-loops). Then
(i) H_phys ∩ E_0 = C|0⟩, |0⟩ := ⊗_ℓ |0⟩_ℓ;
(ii) H_phys ∩ E_k = 0 for 1 ≤ k ≤ g − 1;
(iii) N commutes with P_phys and spec(N|_{H_phys}) ⊆ {0} ∪ {g, g+1, …, |E|}, the eigenvalue 0 is simple, and
g ∈ spec(N|_{H_phys});
(iv) for SU(2) on a bipartite Γ, spec(N|_{H_phys}) ⊆ 2N.
Specialisation: for open boxes and T_L, L ≥ 4: H_phys ∩ E_k = 0 for k = 1, 2, 3 and spec(N|phys) ⊆ {0} ∪ {4, …, |E|}.
*Proof.* (i) E_0 = H_{c=0} = C|0⟩ and all G_s^a vanish on it. (ii) By C1, H_phys ∩ E_k = ⊕_{|supp c| = k} H_phys ∩ H_c;
by C2 a nonzero summand has supp c ≠ ∅ with minimum degree ≥ 2, which contains a cycle (walk along unused links
until a vertex repeats), so k ≥ g. (iii) G6(a) gives [N, P_phys] = 0; N is diagonal in the H_c decomposition, so the
restriction has spectrum {k : H_phys ∩ E_k ≠ 0}; use (i), (ii), and C5(a) for attainment. (iv) An even subgraph is an
edge-disjoint union of cycles; in a bipartite graph cycles are even. ∎
**Truncation note.** (ii) uses only C2's "degree ≥ 2" (Schur), so it holds for any truncation; the sharp attainment
and dimension counts (C5) use S1–S3.

**Lemma C5 (exact dimensions) — [R] given S2, S3.**
(a) dim(H_phys ∩ E_g) = μ · #{g-cycles of Γ̄}, μ = 1 (SU(2)), μ = 2 (SU(3)).
(b) dim H_phys = Σ_{c ∈ Z_1(Γ;Z_p)} Π_{s∈V} ω_s(c), with ω_s(c) = Cat((a_s + b_s)/2) (SU(2)), w(a_s, b_s) (SU(3)).
(c) [Cit: rank of the incidence matrix over Z_p] |Z_1(Γ; Z_p)| = p^{|E| − |V| + #components}.
*Proof.* (a) A Z_p-cycle c with |supp c| = g has support containing a cycle of length ≥ g, hence equal to one cycle C,
all of whose vertices have degree 2. SU(2): c = 1_C, each vertex weight Cat(1) = 1. SU(3): ∂c = 0 at a degree-2 vertex
forces the flow to be consistent along C: c is one of the 2 nonzero multiples (a "3-flow" or a "3̄-flow") of the
oriented indicator of C, each vertex has (a_s, b_s) = (1, 1) and w(1,1) = 1. (b) C1 + C2 + S2/S3. ∎
Example: in T_4, dim(H_phys ∩ E_4) = 240 (SU(2)) and 480 (SU(3)), not 192/384: the 48 Polyakov-type winding loops
are gauge-invariant N = 4 states (C3(c)).
Runner E (numeric Lie-kernel products over all configurations vs (b), per N):
* SU(2) open 1×1: {0:1, 4:1} (total 2); 2×1: total 4; 2×2: {0:1, 4:4, 6:4, 8:9} (18); 3×2: {0:1, 4:6, 6:7, 8:24,
  10:25, 12:19} (82); cube 1×1×1: {0:1, 4:6, 6:16, 8:9} (32); 2×1×1: {0:1, 4:11, 6:36, 8:107, 10:244, 12:325, 14:80,
  16:64} (868); periodic 3×3 (girth 3): min N > 0 is 3.
* SU(3) open 1×1: {0:1, 4:2} (3); 2×1: {0:1, 4:4, 6:2, 7:2} (9); 2×2: total 99; cube: {0:1, 4:12, 6:32, 7:24, 8:72,
  9:64, 10:36, 12:2} (243); 2×1×1: total 47241 (cycles-only enumeration); periodic 3×3: min N > 0 is 3.
* In every girth-4 case, min{N > 0} = 4 and dim(H_phys ∩ E_4) = μ·#4-cycles. Totals agree with the independent
  gauge-invariant bases of the part-3 runner (SU(2): 2, 4, 18, 82, 32; SU(3): 3, 9).
* SU(3) admits odd N (e.g. N = 7 on 2×1, where all 7 links are excited and the two degree-3 sites carry
  (a, b) ∈ {(3, 0), (0, 3)}, i.e. ε-type "baryonic" vertices; also N = 7, 9 on the cube); SU(2) on bipartite graphs
  has only even N.

---

## 5. Full-space checks (runner D, definition D2)

Single plaquette, SU(2) (dim 625, dense): P_s² = P_s and P_s† = P_s (1.1e-16, 0); [P_s, P_t] = 0, [P_s, N] = 0,
[P_s, Tr Ũ_P] = 0 (≤ 5.6e-17); Π_s P_s equals the projector onto the common kernel of all Gauss generators (5.6e-16),
rank 2; P_s commutes with operators on links outside star(s); spec(N|phys) = {0, 4}.
Single plaquette, SU(3) (dim 130321, sparse): [G_s^a, G_t^b] = [G_s^a, N] = [G_s^a, Tr Ũ_P] = 0 exactly; the total
Gauss Casimir has a 3-dimensional kernel (next eigenvalue 8/3); spec(N|phys) = {0, 4, 4}; on star(s) ∪ star(t) for
adjacent s, t (3 links, dim 6859) P_s, P_t are self-adjoint idempotents that commute (≤ 5.1e-16).

**Runner honesty note.** The first run of the runner reported one FAIL: spec(N|phys) for the SU(3) plaquette came out as
[0, 4.04, 5.35]. Cause: `scipy.sparse.linalg.eigsh` (shift-invert) returned non-orthonormal vectors inside the
3-fold degenerate kernel. The runner now re-orthonormalises (QR) and checks ‖C_tot K‖ (5.9e-16) before restricting N;
the logged run is 108/108 PASS.

---

## 6. Lean formalisation map

Mathlib names in this table were checked by grepping `leanprover-community/mathlib4` master source on 2026-11-01, except `Matrix.kroneckerMap`-mixed-product lemma names, `PiTensorProduct`, `DirectSum`, `Submodule.iSup`, `Polynomial.aeval`, `MeasureTheory.Measure.haar`, `Matrix.specialUnitaryGroup`, `Equiv.Perm.sign` (well-known, not re-grepped). "Gap" means not in
Mathlib (to our knowledge) and must be built.

| Lemma | Lean statement shape | Mathlib ingredients | Gaps |
|---|---|---|---|
| Setup | `structure LatGraph (V E : Type) [Fintype V] [Fintype E] where src tgt : E → V; noLoop : ∀ e, src e ≠ tgt e`; `H := PiLp`/`TensorProduct` over `E`, or concretely `Matrix (E → LinkIdx) (E → LinkIdx) ℂ` with `LinkIdx := Fin 5 / Fin 19` | `Matrix.kroneckerMap`, `Matrix.kronecker`, `TensorProduct`, `PiTensorProduct` | Concrete Gell-Mann matrices; a usable finite `⊗_{e∈E}` of matrices (`PiTensorProduct` is abstract: practical route is `Matrix (E → Fin n)` with entrywise product formula) |
| G1 | `(A a e).IsHermitian` for `I • A`; `Commute (A a 0) (A b 1)`; `Commute (A a e) nOp` | `Matrix.IsHermitian`, `Matrix.kronecker` mixed-product lemmas | none (decidable over `ℚ(i)` or by `simp`) |
| G2 | `IsStarProjection (P s)` with `P s := (ker (C s)).starProjection` | `Submodule.starProjection`, `isSymmetricProjection_starProjection`, `isSelfAdjoint_starProjection`, `IsStarProjection` | ker(Σ A†A) = ⋂ ker A: short proof via inner products |
| G3 | `P s = Matrix.kronecker (p s) 1` after a reindexing equiv of `E → LinkIdx` | `Matrix.reindex`, kernel of `M ⊗ 1` | ker(M ⊗ₖ 1) = ker M ⊗ H′ for Kronecker matrices |
| G4 | `∀ s t, Commute (P s) (P t)` | `Commute`, polynomial functional calculus (`Polynomial.aeval`) | P = q(C) for Hermitian C (`Matrix.IsHermitian.spectral_theorem` in `Mathlib/Analysis/Matrix/Spectrum.lean` gives it) |
| G5 | `IsStarProjection (∏ s, P s)` and `range = ⨅ s, ker (C s)` | `IsStarProjection.mul` (needs `Commute`), `Finset.noncommProd` or `Finset.prod` in a commutative subalgebra | ordered product ↔ commuting family bookkeeping |
| G6 | `Commute O (G s a) → Commute O (P s)`; (Cov) as a matrix identity for each `x y` | `Commute` algebra; ε as `Matrix.det` expansion / `Equiv.Perm.sign` | ε-invariance identity Σ ε_{..} T = 0 for traceless T (finite check by `decide`/`norm_num` is feasible) |
| G7(a) | `∫ g, W s g ∂haar = P s` | `MeasureTheory.Measure.haar`, Bochner integral, `Representation.invariants` | SU(d) as a compact Lie group with Haar measure on operator-valued maps; fixed vectors = Lie kernel for connected groups. **Largest gap; avoid by using D2.** |
| G7(b) | `Representation.averageMap (2O) = P s` for `deg s ≤ 7` | `Representation.averageMap`, `isProj_averageMap`, `averageMap_invariant`, `Representation.invariants` | 2O as an explicit `Subgroup (Matrix.specialUnitaryGroup (Fin 2) ℂ)`; invariants equality is a finite rank computation (could be `decide`d over `ℚ(√2, i)`) |
| S1 | `Inv k = ⊥` for odd `k` | `Matrix.diagonal`, eigenvalues of Kronecker sums of diagonals | none |
| S2 | `finrank Inv (2m) = catalan m` | `catalan`, `catalan_eq_centralBinom_div`, `DyckWord.card_dyckWord_semilength_eq_catalan` | SU(2) Clebsch–Gordan (`V_j ⊗ V_{1/2}`): not in Mathlib. Workaround: prove dim via sl₂ highest-weight theory (Mathlib has `sl₂` triples, `IsSl2Triple`, but not the tensor decomposition), or restrict to `k ≤ 6` by computation |
| S3 | `finrank Inv a b = w a b` | — | SU(3) Pieri rule: gap. Workaround: finite computation for a + b ≤ 6 (all that T_L needs is a + b ≤ 6) |
| C1 | `H_phys = ⨆ c, H_phys ⊓ H_c`, `finrank (H_phys ⊓ H_c) = ∏ s, finrank (Inv s c)` | `DirectSum`, `Submodule.iSup`, `Module.finrank_tensorProduct`, `Matrix.reindex` | leg-to-site regrouping equiv `(E × Fin 2 → Fin d) ≃ (Σ s, star s → Fin d)` |
| C2 | `H_phys ⊓ H_c ≠ ⊥ → ∂ c = 0` | `ZMod p`, `Finset.sum` | none |
| C3 | `(torus L).girth = 4` for `L ≥ 4`; `(box ..).girth = 4`; 4-cycle classification | `SimpleGraph.girth`, `egirth`, `Walk.IsCycle.girth_le_length`, `three_le_girth`, `exists_girth_eq_length`, `IsBipartiteWith`, `SimpleGraph.boxProd`, `SimpleGraph.pathGraph` | girth of box products / torus; for fixed small L `decide` is possible |
| C4 | `∀ k, 0 < k → k < g → H_phys ⊓ E k = ⊥` | `Walk.IsCycle`, `IsAcyclic`, `isAcyclic_iff_forall_not_isCycle`, `IsTree.card_edgeFinset` (a forest has < |V| edges, so min-degree ≥ 2 ⇒ not acyclic) | "min degree ≥ 2 ⇒ contains a cycle" for a subgraph: short, via `IsAcyclic` + leaf existence (Mathlib has `IsTree` degree lemmas only partially) |
| C5 | counts | `Fintype.card`, `ZMod` linear algebra | cycle space dimension `|E| − |V| + c` over `ZMod p` (incidence-matrix rank): gap |

**Recommended Lean route.** Define P_s by D2 (`starProjection` of a kernel); never formalise Haar integration. Prove
G1–G6, C1, C2, C4 in full generality (pure linear algebra + graph theory). Discharge S1 by the Cartan argument;
replace S2/S3 by computation for the finitely many (a, b) with a + b ≤ 6 (site degree ≤ 6); prove C3 generally or
by `decide` per L. G7 is not needed for any statement in this note.

---

## 7. Corrections to the 2026-10-31 note (§2 Lemma 1, §3 Lemma 2)

1. **Lemma 1(b) underspecified.** "Every vertex of S has degree ≥ 2" is true but not the sharp statement. Correct
   statement: S = supp c is a Z_2-cycle (even subgraph) for SU(2) and c is a Z_3 1-cycle for SU(3) (Lemma C2). The
   girth conclusion needs only degree ≥ 2; the dimension counts and the spectrum of N need the cycle statement.
2. **Lemma 1(a) proof by citation of ballot numbers** is replaced by S1 (elementary Cartan proof of the vanishing,
   [R]) and S2 (Catalan count, [Cit] + [F] for k ≤ 8). The old note's numerical check covered k ≤ 6 only.
3. **Missing statement of the spectrum.** The old note proves H_phys ∩ E_k = 0 for k = 1, 2, 3 but never states the
   spectrum. Correct form: spec(N|phys) ⊆ {0} ∪ {4, …, |E|}, 0 simple, 4 attained (C4); it is **not** [4, ∞) and,
   for SU(3), contains odd values (7 on the cube); for SU(2) on bipartite graphs it is even.
4. **E_4 on T_4 is larger than "one state per plaquette."** For L = 4 the 48 straight winding loops are 4-cycles, so
   dim(H_phys ∩ E_4) = 240 (SU(2)) / 480 (SU(3)), not 192 / 384 (C3(c), C5(a)). For L ≥ 5 the count is 3L³ (SU(2)) /
   6L³ (SU(3)). Any later use of the E_4 band multiplicity at L = 4 must account for this (this note does not
   assess such uses).
5. **L ≥ 4 is sharp** (confirmed): T_3 has girth 3 and gauge-invariant N = 3 states (runner E, periodic 3×3: 6 for
   SU(2), 12 for SU(3)).
6. **§1 "star(s) = the 6 links"** holds only for T_L, L ≥ 3; open boxes have degree 2 to 6 (all lemmas here allow any
   degree; G7(b) needs degree ≤ 7).
7. **Lemma 2(i) defined P_s by Haar averaging** and used "Haar averaging gives the projector" without proof. The
   Lean-ready definition is D2 (kernel of the site Casimir), for which (i)–(iii) are proved by finite linear algebra
   (G2–G5); D1 = D2 is [Cit] (G7(a)), D3 = D2 for SU(2) is [Cit] + [F] (G7(b)).
8. **Lemma 2(ii) proof** ("left and right regular action") is correct in spirit but, in the truncated space, the
   actions are ρ_λ ⊗ 1 and 1 ⊗ ρ_λ* on each block V_λ ⊗ V_λ*; it also silently requires no self-loops (L ≥ 2) and
   that the truncation set is closed under the action (each block is a subrepresentation). Both are now explicit (G1, G4).
9. **Lemma 2(iv) rotation covariance underspecified.** Translations of T_L map links to links with orientation
   preserved and intertwine the W_s exactly. Proper cubic rotations reverse the orientation of some links; covariance
   then needs a link-reversal unitary R_ℓ implementing ψ(x) ↦ ψ(x⁻¹) on the truncated space (it exchanges the start and
   end legs and maps **3** ↔ **3̄** for SU(3); for SU(2) it uses the ε-identification 2̄ ≅ 2). The old statement
   omitted this map; its explicit matrix is not fixed here. Not used by any lemma here.
10. **Lemma 2(v) covariance of the plaquette term** was assumed, not shown, for the truncated operators (which are not
   unitary and not restrictions of the untruncated U). It is now G6(b, c): (Cov) holds because the transition tensors
   are δ/ε invariant tensors, verified exactly by the runner.

## 8. What this note does not do

No statement about the spectrum of H for δ ≠ 0, no cluster expansion, no BHM-type argument, no claim about the old
note's Lift Proposition or Main Theorem beyond flagging correction 4 for whoever audits them.
