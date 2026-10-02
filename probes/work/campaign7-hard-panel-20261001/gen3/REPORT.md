I've done the synthesis. Nothing was run and no files were written. The report follows.

---

# Synthesis report: three light chiral generations from the coin carrier (Lanes B and C)

**Provenance.** Everything here is derived by hand.

**Read on origin/main `0485dc0738`:**
- The axioms memo. Its Lattice clause gives "standard translations, and proper cubic rotations about each site", with no inversion.
- `SPIN10_SYMMETRIC_ATOMIC_GAPS_…_2026-09-14`, §1. This gives the refined q = 32 atom, the quartic Ω = Σ_a B_aB_a, and the decomposition 16⊗16 = 10 ⊕ 120 ⊕ 126.
- `WHAT_CAN_GAP_THE_WALK_…_2026-09-22`, T1. Corner orbits under proper rotations have sizes 1, 1, 3, 3, and any translation-invariant coin symbol is a scalar at a corner.
- The claim scope of `SCALAR_HOP_…_2026-09-22`.
- Lane B and Lane C reports, in full.

**Literature.** Abstracts or search summaries fetched this session, never used as premises:
- Golterman–Shamir, arXiv:2603.15985;
- Wang–Wen, arXiv:1809.11171;
- García-Etxebarria–Montero, arXiv:1808.00009;
- Wang–Wen–Witten, arXiv:1810.00844 (search summary only).

**Labels.** EXACT (proof given here), CHECKED (finite hand evaluation), ARGUED (reasoning, not verified), LIT (fetched literature), [S] (supplied piece).

**Notation.**
- c_j = cos k_j, σ_j = sin²(k_j/2) = (1−c_j)/2, γ_j = cos²(k_j/2) = (1+c_j)/2.
- Node n ∈ {0,1}³ sits at πn and has handedness (−1)^{|n|}. Following Lane B, L = {e_a, 111} and R = {000, ē_a}.
- Λ = {e_a} is the light triplet, M = {ē_a} is the mirror triplet, and 000, 111 are the singlets.

## 1. The problem

**Carrier [S].** The coin carrier ⊗ C^{N_int}, with an exact on-site group G_int.

**Target.** The infrared content is exactly 3 × (R_int, L) at Λ. The five other nodes are gapped without breaking G_int. The three copies are degenerate by symmetry, not by tuning.

## 2. Q1: the composite

### 2.1 Unit-cube composites

**Walsh form (EXACT).** Take Ψ_c = Σ_{y∈{0,1}³} w(y) ψ_{c+y}. Its form factor at corner πn is the Walsh transform W(n) = Σ_y w(y)(−1)^{n·y}, so any eight corner values can be realised.

**Rotation content (EXACT).** Cube-centre rotations act on the eight vertices with permutation character (8, 2, 0, 0, 0). So 8 = A1 ⊕ T1 ⊕ T2 ⊕ A2, sorted by Walsh weight 0, 1, 2, 3.

**A T2 triplet isolates the mirror.** Φ^{(m)}_c = Σ_y (−1)^{y_j+y_l} ψ_{c+y}, with {j,l,m} = {1,2,3}, has W = 8δ_{n,ē_m}. It singles out ē_m exactly at the corners.

**Lemma B (EXACT): unit cubes vanish only linearly at light nodes.**
- A unit-cube form factor F is multi-affine in z_j = e^{ik_j}.
- At e_a, the derivative along z_l (l ≠ a) is ∂F/∂z_l = (W(e_a) − W(e_a + e_l))/2 = −W(ē_m)/2.
- So any cube composite that is nonzero on ē_m vanishes only linearly at the two light nodes adjacent to ē_m.

**General bound (EXACT).** A degree-R trigonometric polynomial has at most 2R zeros counted with multiplicity. So with reach R per axis, the vanishing order at a light node, in the direction of an adjacent gapped node, is at most 2R.

**Adjacency (EXACT).** Every light node e_a is at Hamming distance 1 from 000, ē_b and ē_c. This adjacency is unavoidable in the triplet synthesis.

### 2.2 Construction (EXACT)

**Corner indicators.** I_n(k) = Π_j [n_j σ_j + (1−n_j) γ_j]. They satisfy I_n(πn′) = δ_{nn′} and Σ_n I_n ≡ 1.

**Stencil.** β_n(y) = 2^{−3−|y|₀} (−1)^{n·y} on y ∈ {−1,0,1}³, where |y|₀ counts nonzero components. The composite is Φ^{[n]}_x = Σ_y β_n(y) ψ_{x+y}.

**Three A1 scalars:**
- **Mirror indicator.** 𝔅 = Σ_m I_{ē_m} = (3 − Σc − Σ_{j<l} c_jc_l + 3c₁c₂c₃)/8.
  - It is 0 on weights 0, 1 and 3, and 1 on weight 2.
  - Near πe_a + q it is (|q|² − q_a²)/4.
- **Gapped-set indicator.** 𝔊 = 1 − Σ_a I_{e_a} = (5 − Σc + Σcc + 3ccc)/8.
  - It vanishes at exactly the three light corners and nowhere else on T³. (Proof: 𝔊 = 0 forces I_000 = I_111 = I_{ē_m} = 0, which leaves only (π,0,0) and its permutations.)
  - It equals 1 on the five other corners.
  - Near light nodes it is |q|²/4, isotropic.
  - Stencil weights: 5/8 at 0; −1/16 on the 6 nearest neighbours; 1/32 on the 12 face diagonals; 3/64 on the 8 body diagonals. These sum to 1 (CHECKED).
- **Handedness indicator.** I_E = (1 + c₁c₂c₃)/2. It is 1 on R nodes and 0 on L nodes.

**Vanishing orders at e_a + q (reach 1):**

| Indicator | Order at e_a + q |
|---|---|
| I_000 | q_a²/4 |
| I_{ē_b}, I_{ē_c} | quadratic (q_c²/4, q_b²/4), toward the adjacent mirror |
| I_111 | q_b²q_c²/16 |
| I_{ē_a} | q⁶/64 |

### 2.3 Symmetry checks (EXACT)

- **Reality.** β_n is real and even, so I_n is real and even.
- **Rotations.** The composite is site-centred, so a proper rotation R sends Φ^{[n]}_x to U_R Φ^{[Rn]}_{Rx} and permutes the I_n within a weight.
- **Translations and Hermiticity.** H_int = Σ_x F(Φ_x, Φ_x†), with F a fixed local even polynomial, is invariant under all translations, odd ones included. It is O-invariant if F is a spin-SU(2) singlet, Hermitian if F = F†, and G_int-invariant if F is.

### 2.4 The brief's b(k) (EXACT)

- Σ_{j<l} sin(k_j/2) sin(k_l/2) is not 2π-periodic.
- Its lattice realisation is the plaquette composite Σ_{j<l} (1−T_j)(1−T_l)ψ. Its symbol is −4Σ e^{i(k_j+k_l)/2} s_j s_l.
- That symbol has modulus 4 at weight 2 and 12 at the 111 singlet, and vanishes only linearly at light nodes (Lemma B).
- It is rotation-covariant only up to translations and signs.
- 𝔅 and 𝔊 replace it.

### 2.5 Interaction [S]

- The composite has 2 × 16 = 32 components per site.
- Use the landed quartic Ω = Σ_a B_aB_a, with B_a = Φᵀ ε CΓ_a Φ. The landed note shows Ω is nonzero, a Spin(10) and spin singlet, changes fermion number by 4, and reduces number rotations to the Z₄ centre.
- Take H_int = g Σ_x [Ω(Ψ^𝔊_x) + h.c.] + λ Σ_x C₂(Ψ^𝔊_x), or the per-node version with Φ^{[n]}.
- The charge-4 part is required (§4).
- **Locality.** The support is the 3×3×3 block, graph reach 3. That is beyond nearest neighbour [S].

## 3. Q2: translations, degeneracy, and where the brief's route fails

### 3.1 Corner zero-mode lemma (EXACT)

- Suppose H_int depends on ψ only through composites whose form factors vanish at k₀. Then ψ_{k₀} anticommutes with every Φ_x and Φ_x†, so [H_int, ψ_{k₀}] = 0.
- Hence [H, ψ_{k₀}] = −E_c ψ_{k₀}, where E_c is the scalar corner value of the one-body symbol (landed T1). For the coin, E_c = a0 + 2a.
- So on every even torus and at every coupling, the 3 × 32 light-corner modes are exact eigen-operators.

**Corollary (EXACT, diagrammatic).** Every leg of an H_int vertex carries a form factor, so the self-energy factorises: Σ(k) = I(k)† Σ̃ I(k) = O(q⁴).
- So there is no O(q) renormalisation of mass or velocity at the light nodes. The NN coin's isotropic velocity v (Lane B, D2) survives.
- This needs Σ̃ to be regular near the light corners (ARGUED). That regularity is the symmetric-mass-generation (SMG) condition itself.

### 3.2 Mackey (EXACT)

H_int preserves Z³ ⋊ O, so Lane B's D3 applies unchanged:
- light ⊗ spin ⊗ 16 is irreducible under (Z³ ⋊ O*) × Spin(10);
- the three copies are exactly degenerate, related by C₃, and distinguished by translation characters.

### 3.3 Lemma C: every quadratic gap pairs a light node (EXACT)

This is the decisive failure of the brief's route.
- A translation-breaking bilinear at momentum πb couples n to n ⊕ b. It is a Dirac mass only when |b| is odd.
- For odd |b|, e_a ⊕ b is never light and always has opposite handedness:
  - b = e_a gives 000;
  - b = e_c gives ē_d;
  - b = 111 gives ē_a.
- So any staggering that gaps something quadratically makes a light–gapped Dirac mass symmetry-allowed.
- **Lane B's term.** ε(α + β Σ cos cos) takes two independent invariant values at the corners: M_s on weights 0 and 3, M_t on weights 1 and 2 (an ε Σ cos 2k_j term just adds to α).
  - M_t = α − β = 0 is a codimension-1 tuning.
  - No symmetry protects it: ε·1 is invariant under even translations, O, G_int and time reversal.
- **Lane C.** f = Σ C_jC_l − 3 has the same tuned constant.
- By 3.1 the tuned value is stable within the form-factor model class, but not against generic local terms.

### 3.4 Variant T: keep all translations

**Lemma D (EXACT).** With Z³ and Spin(10):
- inter-node bilinears are forbidden by momentum;
- intra-node pairing is forbidden, because 16⊗16 = 10 + 120 + 126 has no singlet (landed);
- the intra-node one-body symbol is scalar at a corner (landed T1).

So the corner energy E_c is the one relevant symmetric deformation at the light nodes.

**Lemma E (EXACT).** E_c (the A1 hoppings a0 and a) cannot be forbidden by any operation built from translations, proper rotations, the sublattice sign, time reversal T and particle-hole C.
- For the σ·sin term to survive while the identity term flips sign, det(spin map) · det(momentum map) must equal −1.
- A proper rotation always gives +1.
- Lattice CP (particle-hole × site inversion, with iσ_y) does forbid a0 and a. But inversion is not an axiom symmetry.

**Consequence.**
- Variant T carries exactly one tuning, E_c = 0, or a supplied improper CP. The tuning is stable by 3.1.
- If E_c ≠ 0, the light nodes acquire Fermi surfaces of radius |E_c|/v.
- The gapped nodes' offsets (−4a, +4a, −8a) are harmless while they stay below the gap.

### 3.5 What would lift the degeneracy (EXACT representation theory)

- **Cell blocking.** Blocked composites (2Z³) make every corner character trivial.
  - V₆ then splits as E_{1/2} ⊕ G_{3/2} under O* alone.
  - Light–gapped bilinears become allowed.
- **Spontaneous order (ARGUED risk).** A density wave at odd b acts like 3.3. At b = e_c it splits copy c from the other two (O → D₄).

### 3.6 Mean-field control (EXACT, symmetry-broken comparator)

- Condense the 10-channel along one direction. CΓ_a is unitary, so all 16 Takagi values equal 1.
- Each channel's Bogoliubov–de Gennes (BdG) block is σ·s τ_z + Δ𝔊² τ_x, with E² = v²|s|² + Δ²𝔊⁴.
- The five gapped corners have gap |Δ|. The light nodes keep E ≈ v|q| + Δ²q⁷/(512v).
- So the form factor isolates the gapped set at mean-field level. Whether the symmetric phase exists is the open question.

## 4. Q3: anomaly bookkeeping

All anomalies are written in left-handed language; Σq³ is counted with fermion-number charge q = 1.

| Set | Content | U(1)_F Σq³ | Spin(10) perturbative | ν mod 16 (centre Z₄) |
|---|---|---|---|---|
| Light Λ | 3×16 | +48 | 0 | 0 |
| Mirror M | 3×16̄ | −48 | 0 | 0 |
| 000 / 111 | 16̄ / 16 | ∓16 | 0 | 0 |
| Gapped set, Variant T | M + 000 + 111 | −48 | 0 | 0 |

**General content.**
- **EXACT:** for any per-corner representation R, the mirror's perturbative anomalies are exactly −3A(R), and the light triplet's are +3A(R).
- The 000/111 pair cancels within itself (perturbatively, and in the Z₁₆ count ν).
- The gapped set therefore carries minus the light anomaly. Symmetric gapping requires A(R) = 0, using standard anomaly matching (ARGUED).

**Z₁₆ (LIT classification, EXACT arithmetic).**
- The gapped set has ν = −3ν(R) mod 16. Since 3 is invertible mod 16, this vanishes iff ν(R) ≡ 0.
- The three generations do not help cancel anything.
- 16 per corner passes. 15 per corner (the Standard Model without ν_R) gives 45 ≡ 13 and fails if the relevant Z₄ is kept.

**U(1)_F must be broken to Z₄ (EXACT).** Its anomaly on the gapped set is −48 ≠ 0. The landed Ω does this breaking.

**Translations kept (Variant T).** The translation T₁₁₁ acts as handedness (EXACT), so mirror ≅ conj(light) ⊗ χ₁₁₁. Per-node anomaly freedom is therefore the operative condition:
- The 16 of Spin(10) is anomaly-free; the Wang–Wen–Witten summary says the spinor GUT is "completely anomaly-free" (LIT).
- Each structure z·T_v carries whole 16s, so ν ∈ 16Z (EXACT).
- Mod-2 counts are even: 4 zero modes in the minimal instanton via 16 → (2,1,4) + (1,2,4̄), and even Â (ARGUED).
- Lane C's set (1, 5, −7, −8, 9) passes the perturbative test per node. Global anomalies for Spin × U(1) beyond the perturbative ones are not verified (ARGUED).

## 5. Q4: residual symmetry

- **Exact symmetries.**
  - Spin(10), on-site and so gaugeable;
  - Z³;
  - O*;
  - optionally CP [S];
  - U(1)_F reduced to the Z₄ centre.
- **Copy index.** No continuous symmetry acts on it. Its image of (Z³ ⋊ O) is B₃ = Z₂³ ⋊ S₃ (order 48) acting as signed permutations (EXACT). By Schur, any lattice-symmetric generation mass matrix is proportional to 1₃ (EXACT).
- **Would-be protectors of the mirror:**
  - Sublattice particle-hole C·S maps light to mirror (EXACT). It is broken, since 𝔊(k+Π) ≠ 𝔊(k).
  - All seven species-exchange maps n ↦ n ⊕ b move the light set (Lane B lemma), so all are broken.
  - U(1)_F is broken.
  - No other protector is known (ARGUED).

## 6. Q5: supplied pieces and what the axioms give

**What the axioms give.**
- Z³ translations and proper rotations. This is exactly the group the Mackey protection uses.
- The corner orbits 1, 1, 3, 3 (landed T1). Hence (EXACT): if the light set is a single orbit with more than one element, its size is 3 = d.
- One qubit per site.
- The nearest-neighbour admissibility rule. It yields no Hamiltonian, but it makes the light velocity isotropic if H₀ is kept at nearest-neighbour range.
- The Record axiom is unused.

**Supplied, exhaustively:**
1. Fermionic modes: 2 × 16 = 32 complex modes per site (32 or 64 qubits per block cell).
2. Spin(10) and its action on the modes.
3. The continuous-time Hamiltonian H₀ and the choice E_c = 0, or an improper CP.
4. The composites (3×3×3 support).
5. Ω, C₂ and the strong couplings g, λ.
6. The choice of gapped set, which fixes the count. With O-invariant form factors the count is 1, 3 or 4 (EXACT); the plain handedness split I_E gives 4.
7. Variant E only: the staggered mass with α = β.

## 7. Routes, ranked, and failure modes

**Routes:**
1. **Variant T.** Full translations; SMG on the five gapped nodes via 𝔊; 16 per corner; one tuning. Bilinear protection is symmetry-based (EXACT).
2. **Variant E.** Lane B's ε-mass plus 𝔅. Two tunings, and the light–mirror Dirac mass is symmetry-allowed (3.3).
3. **Handedness split I_E.** Four light generations. Simplest, but the count is 4.
4. **Lane C.** One generation. Its SMG vertex vanishes to order q⁶ at reach 1, but the explicit ε-coupling already makes the overall coupling order q².

**Failure modes, worst first (ARGUED unless marked):**
- **(a) Golterman–Shamir.** Per their abstract (LIT): if the mirror zeros are "kinematical", then under conditions for Nielsen-Ninomiya on a constructed one-particle Hamiltonian the spectrum "must be vector-like". The landed atom's zero is of the kinematical (c, b) Dirac form, G⁻¹ = z + Δ_f σ_x. That makes this the live risk.
- **(b) Golterman–Petcher–Rivas-type binding.** Gapped-sector three-fermion composites with the light quantum numbers exist (EXACT: for example {ē_b, ē_c, 111}).
- **(c) The interaction must be strong.** Composites with vanishing form factors cannot be canonical, because {Φ_x, Φ_x′†} = δ requires |β̃| ≡ 1 (EXACT). So no product-atom limit exists; the strong-coupling problem is non-commuting.
- **(d) Spontaneous density waves (§3.5).**
- **(e) The count of 3 is a choice (§6).**

## 8. Q6: decisive computations (spec only)

**C0. Done on paper here.**
- The indicator table and polynomials (§2.2).
- The zero-mode lemma (§3.1).
- The BdG control (§3.6).
- The anomaly table (§4).
- On the L = 2 torus the problem factorises exactly into eight corner problems (EXACT). Choosing landed-atom coefficients gives each gapped corner a unique Spin(10)-singlet ground state with a gap (landed). This is a 0-D check only.

**C1. Exact free-fermion regression (seconds).**
- Evaluate I_n, 𝔅 and 𝔊 on a grid.
- Verify [ψ_{πe_a}, H] = 0 on a 2⁸-site Fock space with N_int = 1 and any quartic in Φ.
- Expected: exact results. Any deviation is an algebra error.

**C2. Decisive interacting test: a 1+1-D adjacency analog.**
- **Setup.** Lane C's 3450 chain: light at k = 0, mirror at π. This is one-axis adjacency, the same as e_a to ē_b.
- **Composite variants.** Bond composite (linear); σ(k) = sin²(k/2) (quadratic, matching §2.2); σ² (quartic).
- **Run.** DMRG, local dimension 16, L = 64–128, U from 0 up to a few bandwidths. Use antiperiodic boundary conditions to sidestep the exact k = 0 zero modes, or use those modes as a check.
- **Measurements.** Central charge c, gaps at 0 and π, light velocity, the light–composite correlator, and the zero-frequency inverse propagator as a test for kinematical zeros.

| Outcome | Meaning |
|---|---|
| c = 2, gap at π only, velocity unrenormalized | Adjacency is survivable; move to a 3-D QMC sign-structure check |
| c < 2, or the light mode is paired | Golterman–Petcher–Rivas failure at that reach; Variant T fails at reach 1 |
| c = 4 | Interaction irrelevant; raise the coupling |
| Gapped, but the mirror zeros fit a local (ψ, b) Hamiltonian | Golterman–Shamir conditions are likely met; the result is vector-like |

**C3. 3-D.** Exact diagonalization is infeasible beyond L = 2. The next step is a check of whether the 10-Yukawa formulation is sign-free (ARGUED); it is not for the 8 GB machine.

---

**10-line summary**
1. [EXACT] Unit-cube composites split by weight as A1 ⊕ T1 ⊕ T2 ⊕ A2. The T2 triplet isolates each ē_m exactly, but vanishes only linearly at light nodes (Lemma B). With reach R the bound is order 2R, because every e_a is adjacent to 000, ē_b and ē_c.
2. [EXACT] Site-centred indicators I_n = Π(σ or γ) on 3×3×3 stencils. 𝔅 = (3−Σc−Σcc+3ccc)/8 isolates the mirror triplet. 𝔊 = (5−Σc+Σcc+3ccc)/8 vanishes exactly at the light corners, as |q|²/4. Both are O-invariant, invariant under every translation, real and Hermitian.
3. [EXACT] Corner zero-mode lemma: with form-factor interactions, [H, ψ_{πe_a}] = −E_c ψ_{πe_a} at every coupling. The light self-energy is O(q⁴), so velocity and mass are not renormalized there.
4. [EXACT] Lemma C: every quadratic staggered gap pairs each light node with an opposite-handed gapped node. In Lane B's ε-route, α = β is a symmetry-unprotected codimension-1 tuning; Lane C's constant −3 is the same.
5. [EXACT] Variant T, which keeps all translations, forbids every light bilinear except the corner energy E_c. Mackey degeneracy of the three copies holds under (Z³ ⋊ O*) × Spin(10).
6. [EXACT] E_c cannot be forbidden by translations, proper rotations, the sublattice sign, time reversal or particle-hole. It needs an improper CP that the axioms do not supply, or one tuning.
7. [EXACT + LIT] The gapped set's anomaly is −3A(R) and ν = −3ν(R) mod 16, so the condition is per corner. One 16 of Spin(10) per corner passes, while 15 per corner fails with Z₄ kept. U(1)_F must break to Z₄, which the landed Ω does.
8. [EXACT] There is no continuous copy symmetry. The copy group is B₃ (order 48), so symmetric generation masses are proportional to 1₃. C·S and all species-exchange maps are broken by 𝔊.
9. [ARGUED/LIT] Live risks are Golterman–Shamir kinematical zeros (the landed atom's zero has that form), Golterman–Petcher–Rivas binding, non-canonical composites, density waves, and the count (1, 3 or 4) being a choice. That 3 = d is EXACT once the light set is a single orbit with more than one element.
10. [SPEC] Decisive next run: the 1+1-D 3450 DMRG with composites of order 1, 2 and 4 (adjacent geometry), plus a test of the zero-frequency inverse propagator for kinematical zeros. The 3-D interacting test cannot be done by exact diagonalization.

Sources: [arXiv:2603.15985](https://arxiv.org/abs/2603.15985), [arXiv:1809.11171](https://arxiv.org/abs/1809.11171), [arXiv:1808.00009](https://arxiv.org/abs/1808.00009), [arXiv:1810.00844](https://arxiv.org/pdf/1810.00844), [arXiv:1305.1045](https://arxiv.org/abs/1305.1045)