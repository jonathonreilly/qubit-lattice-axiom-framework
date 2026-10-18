---
claim_id: corner_fermion_odd_filling_is_forced_gapless_by_anticommuting_gauge_dressed_c2_lifts_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied model only: the corner fermion of the companion notes (12 corner modes per site of Z^3; flux square = plaquette = tube = pi, triangle = 0; translation-invariant gauge), number-conserving, with the gauge-dressed (PSG) lifts G_g|v,c> = (-1)^(lam_g.v + tau_g(c)) |g v, g c> of O_h about site 0. (T1, exact) For each of the 12 commuting pairs (a, b) of distinct proper C2 rotations, G_a G_b = -G_b G_a on the whole one-particle space l^2(Z^3) (x) C^12 (global, not only at one momentum). (T2, exact) For every translation-invariant one-particle Hamiltonian with summable hopping commuting with G_a and G_b, every level of the Bloch Hamiltonian H(k) is even-degenerate at each momentum fixed by both affine maps k -> R k + pi s_R; these include +-k* (k* = (pi/2, -pi/2, pi/2), the only momenta fixed by all 24 rotations) and, for the axis Klein group D2, exactly the 8 points (+-pi/2)^3. (T3, exact) Hence, if the symmetry subgroup S contains a commuting C2 pair, E_nu(k*) = E_{nu+1}(k*) for every odd filling nu per site: no symmetric band insulator (gapped Slater ground state) exists at odd nu. (T4, numerically certified witnesses) A gapped symmetric band insulator exists at nu = 2 with translations + the 24 dressed rotations, and at nu = 1 with translations + dressed C2x only; the dressed site irreps are [2,2,4,4] under O and [4,4,4] under O_h. (T5, exact finite size) On odd-L tori with U(1) twist theta = +-k* all 24 dressed rotations are symmetries (theta = 0: the 21 shifted rotations fail), the C2 lifts still anticommute, and their vacuum-fixing Fock lifts obey Gamma_a Gamma_b = (-1)^N Gamma_b Gamma_a, so every level in an odd-N sector of any number-conserving Hamiltonian commuting with them is even-degenerate. (T6, conditional) Under the stated hypothesis that a symmetric short-range-entangled gapped phase has a unique gapped ground state on large odd tori with twist theta = +-k*, no such phase exists at odd nu. (T7) In the doubled-cell class 'dressed O_h about site 0 + even translations' free-fermion levels at the folded k* come in multiples of 4 (numerical evidence), while an entangled O_h-covariant two-fermion pair state on the even sublattice gives an exactly symmetric atomic (product) insulator at nu = 1: that obstruction is free-fermion only. This class is not the A2-staggered-mass group. Not covered: antiunitary symmetries, superconducting (U(1)-breaking) states, translation breaking beyond the doubled-cell class, symmetry-broken or topologically ordered gapped states, other flux patterns, the qubit-code realisation, any physical identification."
upstream_dependencies:
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
  - scale_ladder_cross_rung_invariants_corner_fermion_bounded_theorem_note_2026-10-18
  - corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_odd_filling_forced_gapless_anticommuting_c2_lifts_2026_10_18.py
---

# Corner-fermion odd filling is forced gapless by anticommuting gauge-dressed C2 lifts

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact statements T1–T3 and T5 with proofs and finite exact certificates; T4 and the free-fermion part of T7 are numerical witnesses or numerical evidence; T6 is conditional on a named hypothesis. Nothing is adopted.
**Provenance:** drafted by a same-model-family worker; checked by a fresh-context same-model-family agent. Neither is an independent human reviewer. Campaign block B7 of the scale-ladder campaign (2026-10-18).

## Question

The corner fermion carries gauge-dressed (projective) cube rotations. Does that projectivity constrain which fillings per site can host a symmetric insulator, in the manner of a Lieb–Schultz–Mattis (LSM) or band-filling constraint? Which symmetries are actually needed, and does the constraint survive interactions?

## Result

**Setting.** One-particle space ℓ²(Z³) ⊗ C¹², a mode |v, c⟩ for each site v and corner c. The supplied flux pattern is square = plaquette = tube = π and triangle = 0, in the translation-invariant gauge u of the cross-rung note. For each g in O_h about site 0, the PSG lift of the corner-code note has the form

  G_g |v, c⟩ = (−1)^(λ_g·v + τ_g(c)) |g v, g c⟩,

with λ_g ∈ GF(2)³ and τ_g ∈ GF(2)¹². The runner checks this form for all 48 elements against the repo's own PSG solve on the L = 4 torus. It follows that G_g T_e G_g⁻¹ = (−1)^(λ_g·e) T_{g e}. In momentum space G_g maps the Bloch fibre at k onto the fibre at g k + π s_g, with s_g = g λ_g mod 2, by one k-independent 12 × 12 signed permutation U_g:

  U_g H(k) U_gᵀ = H(g k + π s_g),  H(k) = Σ_d h_d e^{−i k·d}.

Exactly 21 of the 24 proper rotations have s_g ≠ 0. Number conservation is assumed throughout. A *filling* ν is the number of fermions per site, 0 ≤ ν ≤ 12.

1. **T1: global anticommutation (exact).** Take a commuting pair (a, b) of distinct proper C2 rotations. There are 12 such pairs: the 3 axis pairs, the 6 pairs of an axis C2 with a perpendicular face-diagonal C2, and the 3 pairs of perpendicular face diagonals. For each pair,

   G_a G_b = − G_b G_a  on all of ℓ²(Z³) ⊗ C¹².

   *Proof.* By composition, G_a G_b |v, c⟩ = (−1)^((λ_b + R_bᵀλ_a)·v) (U_a U_b)_{(R_aR_b c), c} |R_aR_b v, R_aR_b c⟩, and similarly for G_b G_a, with R_aR_b = R_bR_a. The runner checks exactly, in integer arithmetic for all 12 pairs, that λ_b + R_bᵀλ_a ≡ λ_a + R_aᵀλ_b (mod 2). So the site-dependent signs agree. It also checks that U_aU_b = −U_bU_a exactly. The sign is therefore −1 on every basis vector. ∎ The anticommutation is a property of the operators, not of a momentum. k* matters only because it is fixed by both affine maps (T2). On the L = 4 torus the 768 × 768 operators anticommute as well.

2. **T2: even levels at doubly fixed momenta (exact).** Let H be translation invariant with Σ_d ‖h_d‖ < ∞ and commute with G_a and G_b for a commuting C2 pair. Let k be fixed (mod 2π) by both maps k ↦ R k + π s_R, R ∈ {R_a, R_b}. Then every eigenvalue of H(k) has even multiplicity.

   *Proof.* U_a and U_b commute with H(k) and preserve each eigenspace E. Their restrictions A and B are invertible with AB = −BA, so det(A)det(B) = (−1)^{dim E} det(B)det(A), and dim E is even. ∎

   Which momenta: the doubly fixed set of a commuting C2 pair consists of points with coordinates in (π/2)Z. It therefore lies on the N = 24 grid, and the runner's enumeration is exhaustive.
   - **O:** the only momenta fixed by all 24 rotations are ±k*, with k* = (π/2, −π/2, π/2). Every subgroup therefore has k* among its doubly fixed points.
   - **Axis Klein group D2 = {E, C2x, C2y, C2z}:** exactly the 8 points (±π/2)³.

3. **T3: odd filling is forced gapless for free fermions (exact).** Let the symmetry subgroup S ⊂ O_h contain a commuting C2 pair. This holds for O, T, D4, the axis D2 and D2′ = {E, C2z, C2(xy), C2(x−y)}. Let H be as in T2 and symmetric under translations and G_S. For every odd ν,

   E_ν(k*) = E_{ν+1}(k*),  hence  inf_k E_{ν+1}(k) − sup_k E_ν(k) ≤ 0.

   So no symmetric band insulator, meaning a gapped Slater ground state at ν per site, exists at odd ν. *Proof.* By T2 the level counts below any gap at k* are partial sums of even multiplicities, and so are even. ∎ For D2 the same holds at each of the 8 points (±π/2)³.

4. **T4: the constraint is sharp and minimal (numerically certified witnesses).**
   - **ν = 2** with translations and the 24 dressed rotations: an on-site −P, with P projecting onto a 2-dim site irrep, plus a small symmetric range-1 hopping. Its global gap is certified ≥ 0.58 by a grid of N = 48 and a Lipschitz bound (grid gap 0.74).
   - **ν = 1** with translations and dressed C2x only, where no commuting pair exists: certified gap ≥ 0.71.
   - **Site irreps of the dressed site operators:** dimensions [2, 2, 4, 4] under O and [4, 4, 4] under O_h. Hence no O_h-symmetric on-site Slater state has N ≡ 2 (mod 4).

   "Certified" means grid eigenvalues computed in floating point plus a rigorous Lipschitz covering argument. It does not mean interval arithmetic.

5. **T5: exact finite-size many-body statement.** Take an L × L × L torus with L odd and U(1) twist θ, using the quasi-periodic convention ψ(w + L n) = e^{iθ·n} ψ(w). The operators are restricted from the infinite lattice.
   - **Which rotations survive.** A dressed rotation preserves the twist iff R θ + π L R λ_R ≡ θ. For odd L this is the affine fixed-point condition, so with θ = ±k* all 24 rotations are unitary symmetries of every symmetric one-particle Hamiltonian. The runner checks L = 1 and 3, θ = ±k*, with the twisted spectrum equal to the union of H(k) over L k ≡ θ. With θ = 0 (L = 3), exactly the 21 shifted rotations fail.
   - **Anticommutation.** By T1, G_a G_b = −G_b G_a holds on the twisted one-particle space.
   - **Fock lift.** The vacuum-fixing Fock lift Γ, defined by Γ c†_i Γ⁻¹ = Σ_j U_{ji} c†_j and Γ|0⟩ = |0⟩, is multiplicative: Γ(X)Γ(Y) = Γ(XY), and Γ(−1) = (−1)^N. Hence

     Γ(G_a) Γ(G_b) = (−1)^N Γ(G_b) Γ(G_a).

     The runner checks this exactly on the 4096-state Fock space at L = 1.
   - **Consequence.** Every level in an odd-N sector of any number-conserving Hamiltonian commuting with Γ(G_a) and Γ(G_b), interacting or not, is even-degenerate. That is the det argument of T2 applied to the sector. With L odd and ν odd, N = ν L³ is odd.
   - **Interacting check.** At L = 1, generic interacting symmetric sector Hamiltonians at N = 3 and 5 have only even levels, while the N = 2 or 4 sectors have simple levels.
   - **Twisted restriction.** For one-body terms, the twisted restriction of an infinite-lattice symmetric Hamiltonian is shown to commute with the lifts. For interacting terms this is the standard twisted-boundary construction for ranges below L/2, and is not separately verified here.

6. **T6: conditional many-body LSM-type statement.**
   - **Hypothesis H_SRE.** A gapped, symmetric, short-range-entangled (SRE) phase of a finite-range, number-conserving Hamiltonian invariant under translations and G_S, with S containing a commuting C2 pair, has a unique gapped ground state on all sufficiently large odd-L tori with twist θ = k* (or −k*), in the N = ν L³ sector.
   - **Conclusion.** Under H_SRE, no such phase exists at odd ν, by T5.
   - **Status of H_SRE.** It is the standard insensitivity-to-twist hypothesis of flux-insertion arguments. It is a named premise here and is not proved for this model.
   - **What T6 leaves open.** It does not exclude gapped states that break the symmetry or carry topological order. It does not show that any symmetric gapped state occurs at even ν with interactions; even ν has symmetric product states (campaign evidence, below).

7. **T7: the doubled-cell class.** The class is K_dc = ⟨the 48 dressed O_h operators about site 0, the even translations (x + y + z even)⟩. The odd translations are broken, and O_h preserves the parity of x + y + z.
   - **Free fermions (numerical evidence).** For random K_dc-symmetric Hamiltonians on the L = 4 torus, every level of the folded 24-state fibre at k* (k* and −k* fold together) has multiplicity divisible by 4. So 2ν ≡ 2 (mod 4) fermions per doubled cell, that is odd ν, admits no Slater band insulator. The reason is that the dressed O_h class has only 4-dimensional constituents there. The runner checks multiplicities, not a full irrep proof on the folded fibre.
   - **Many-body (exact).** On U ⊗ U the two-fermion site space Λ²C¹² (66 dimensions) is a linear O_h representation. It contains a state ψ transforming by the improper-sign character χ. The coefficient rank of ψ is 12, so it is not a Slater determinant.
     - **Covariance.** The pair operators P_v† = ½ Σ ψ_ab c†_{v,a} c†_{v,b} satisfy G_g P_v† G_g⁻¹ = χ_g P_{gv}†, because the sign (−1)^{λ_g·v} enters squared. They also satisfy T_t P_v† T_t⁻¹ = P_{v+t}†.
     - **The state.** Hence ∏_{v even} P_v†|0⟩ is K_dc-symmetric as a ray. It is a product of on-site states, so it is atomic and SRE. It is the unique ground state of the commuting-projector Hamiltonian Σ_{v even}(1 − |ψ⟩⟨ψ|_v) + Σ_{v odd} N_v, with gap 1 and ν = 1.
     - **Consequence.** In K_dc the odd-ν obstruction is free-fermion only.
   - **Scope.** K_dc is **not** the symmetry group of the A2-staggered-mass model of the Dirac-pair note. That group contains the w1-odd rotations composed with an odd translation, the 24 rotations about a cube centre. The runner checks that the integer translation of (R, c − Rc) has parity w1(R). The independent check found that in that group a free cube-centre doublet exists at ν = 1, so there is no free-fermion obstruction there either.

## How this bears on the lane (interpretation, not a claim)

- **Origin of the constraint.** The gauge dressing of the corner fermion makes commuting C2 rotations anticommute. This is the same algebraic mechanism that gives Kramers-like even degeneracies in double groups. In this model the projectivity comes from the Z2 flux pattern through the PSG, not from a supplied spin.
- **Free fermions versus interactions.**
  - Under translations plus any commuting C2 pair, a symmetric band insulator at odd filling is impossible.
  - With interactions the same conclusion follows only under H_SRE.
  - In the doubled-cell class it fails outright.
- **Which fillings are affected.** The runner Weyl model's node sits at an odd filling (campaign evidence, below), so that filling is among the forced-gapless ones for free fermions. This is a statement about the supplied Hamiltonian only.

## Premises

- **Axioms used.** Lattice (Z³, unit translations, cube rotations about sites).
- **Supplied.**
  - The corner model, its flux pattern and the translation-invariant gauge.
  - Number conservation.
  - The choice of symmetry class: translations plus a subgroup S of the dressed O_h, or K_dc.
  - Summable hopping.
  - For T6, hypothesis H_SRE.
- **Standard facts used.**
  - Bloch decomposition.
  - The determinant argument for anticommuting invertible operators.
  - Multiplicativity of the vacuum-fixing Fock lift of one-particle unitaries.
  - The Lipschitz continuity of sorted eigenvalues (Weyl's inequality).

## Relation to prior work

- **Free-fermion part.** T2–T3 is textbook double-group or projective little-group theory: projective representations of the little group force even band degeneracies and therefore even fillings for band insulators (e.g. Bradley and Cracknell, *The Mathematical Theory of Symmetry in Solids*, 1972). The projectivity here comes from a gauge PSG (Wen, PRB 65, 165113 (2002)).
- **Method precedent only.** Watanabe, Po, Vishwanath and Zaletel, PNAS 112, 14551 (2015), give filling constraints for nonsymmorphic crystals. They assume time-reversal symmetry, which is absent here, so the paper is a method precedent, not a source of this result.
- **Interacting precedents.**
  - Oshikawa, PRL 84, 1535 (2000): flux insertion.
  - Po, Watanabe, Jian and Zaletel (2017; arXiv:1703.06882): lattice homotopy.
  - Else and Thorngren (2020; arXiv:1907.08204): topological theory of LSM constraints.
  - These are stated for spin or bosonic systems. The fermionic (−1)^N twisted-torus version in T5–T6 is an adaptation of them, not a quotation.
- **Block-state counting.** Song, Huang, Fu and Hermele (PRX 2017), and Huang, Song, Huang and Hermele (PRB 2017). The campaign's block-state count agrees with the parity result; it is not re-run here.
- **New here.**
  - The origin of the projective class in the corner-fermion gauge PSG.
  - The explicit twist θ = ±k* that makes all 24 dressed rotations symmetries of odd tori.
  - The minimal-symmetry statement (any commuting C2 pair suffices, a single C2 does not).
  - The free-fermion versus many-body split in the named doubled-cell class.
- Citations are recalled from memory; bibliographic details were not re-verified in this session.

## No-Go Discipline Gate

- **N1 — routes not covered.**
  - Antiunitary symmetries.
  - Superconducting (U(1)-breaking) states.
  - Translation breaking other than K_dc, including the A2-staggered mass, which doubles the cell differently.
  - Symmetry-broken or topologically ordered gapped states.
  - Other flux patterns.
  - The qubit-code realisation.
- **N2/N3 — scope.**
  - The exact negative statement (T3) is quantified over all translation-invariant, number-conserving, summable-hopping one-particle Hamiltonians symmetric under translations and G_S with S ⊇ a commuting C2 pair.
  - The many-body exclusion (T6) is conditional on H_SRE.
  - The K_dc free-fermion quartets are numerical evidence.
- **N4 — inputs.**
  - T1 and the fixed-point sets are exact finite certificates in integer arithmetic.
  - The degeneracy checks use floating-point diagonalisation of random symmetric Hamiltonians.
  - Gap certificates are floating-point grids plus a rigorous Lipschitz bound.
- **N5 — wording.** "Gapless" means the free-fermion single-particle gap closes at k* (T3), or that odd-N levels are degenerate on twisted odd tori (T5). It does not assert a Fermi surface or a specific low-energy theory. "Global anticommutation" means as operators on the whole one-particle space.
- **N6/N7 — strongest objections.**
  - H_SRE is assumed, not proved.
  - The doubled-cell example shows that a free-fermion obstruction can disappear with interactions, so free-fermion statements must not be read as many-body ones.
  - K_dc must not be conflated with the A2-mass group.
- **N8 — earlier claims.** Uses the corner-code PSG and the cross-rung affine action. Changes neither.

## Independent check

A fresh-context agent of the same model family checked the campaign findings. It is not an independent human reviewer. It rebuilt the model without importing the repo model or the campaign model, using its own GF(2) gauge solve and a brute-force PSG over all 2¹⁵ (λ, τ) per O_h element. Files: `.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check/` (REPORT.md, chk_*.py and logs).

- **Confirmed.**
  - The anticommutation of commuting-C2 lifts.
  - Odd filling forced gapless.
  - The ν = 2 insulator (gap ≥ 0.737 in its own construction) and the C2x-only ν = 1 insulator (≥ 0.717).
  - Site irreps [2, 2, 4, 4] and [4, 4, 4].
  - The twisted odd-L torus: 24/24 rotations at θ = ±k* for L = 1, 3, 5; 3/24 at θ = 0.
  - The exact (−1)^N Fock relation.
  - The doubled-cell pair state.
- **Corrections applied here.**
  - The anticommutation is global, not "at k*". The role of k* is only that it is doubly fixed, and under D2 all 8 points (±π/2)³ are forced even.
  - The doubled-cell class is named explicitly, with the scoping remark that it is not the A2-staggered-mass group.
  - The many-body result is stated as conditional on H_SRE.
  - Prior art is rewritten: Watanabe–Po–Vishwanath–Zaletel 2015 is a method precedent only (it assumes TRS); the interacting precedents are Po–Watanabe–Jian–Zaletel 2017 and Else–Thorngren 2020; block-state counting is credited to Song–Huang–Fu–Hermele and Huang–Song–Huang–Hermele; the free-fermion part is textbook; the fermionic (−1)^N version is an adaptation.
- **Not re-checked by the check.** The runner-point node filling, the Wyckoff table and the ν = 4–10 gaps.

**Campaign evidence not re-run by this runner** (scripts in `.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_corner_LSM/`, all ending FAIL = 0):
- Certified insulators at every even ν = 2…10.
- O_h insulators at ν = 2, 6, 10 from cube-centre Wannier doublets.
- ν = 1 insulators with C4z, C3[111] or C2(xy) alone.
- The Wyckoff projective-class table (1a, 1b, 3c, 3d nontrivial).
- Block-state counting.
- Symmetric product states with commuting-projector parents at every even ν.
- The runner Weyl model's node filling ν = 1 (bands 1–2 touching at k*; ν = 2 not forced, since bands 2 and 3 overlap by 0.015).

## Verification

```bash
python3 scripts/corner_fermion_odd_filling_forced_gapless_anticommuting_c2_lifts_2026_10_18.py
```

Expected: `TOTAL: PASS=25 FAIL=0` (about 6–7 minutes; the L = 1 Fock sectors and the doubled-cell symmetrisation dominate).

## Load-bearing sources

- [Corner-code note (PSG class)](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Cross-rung note (affine action, k*)](SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md)
- [Dirac-pair note (A2-staggered mass group)](CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_AND_PSEUDOSCALAR_DIRAC_MASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
