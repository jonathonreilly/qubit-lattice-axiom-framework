---
claim_id: corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the corner fermion of the companion corner-code note, in the flux pattern square = plaquette = tube = pi, triangle = 0, with one-fermion Hamiltonian H = -t1 sum_onsite u c^dag c - t2 sum_links u c^dag c + i lambda sum over oriented triangles (gauge signs u). Exact (fermion level): the site rotations act on crystal momentum by k -> R k + pi s_R (s_R from the projective symmetry group); for this pattern exactly two momenta are fixed by all 24 rotations, k* = (pi/2)(1,-1,1) and -k* (for tube flux 0 no momentum is fixed). Numerical (Bloch bands, 12 x 12, a dense grid plus local minimization, five parameter sets with t1 = -1, |t2| in [0.1, 0.3], |lambda| in [0.3, 0.5]): the global band minimum is a single 2-fold level at k* or -k* (the other lies higher by 2.8 t2 for these sets); every band is 2-fold degenerate at every momentum tested; the Hessian of the lowest band at k* is isotropic (eigenvalue spread below 1e-8; 1/m* = 0.043 at t2 = 0.1, lambda = -0.5); the cubic anisotropy of the dispersion appears at fourth order (relative [111]-[100] difference 5e-4 at |dk| = 0.1, scaling as dk^2). On the L = 4 lattice, which contains k*, the lowest one-fermion level is this doublet, and under the twisted site rotations it carries the two-dimensional spinorial irrep E1/2 (lambda < 0) or E5/2 (lambda > 0) of the binary octahedral group. Hence, by the standard symmetry argument, the low-energy theory of a fermion wavepacket much larger than the lattice spacing is H_eff = E0 + |dk|^2 / 2 m* acting on a spin-1/2 doublet, with cubic corrections of relative order (a/w)^2 for a packet of size w. Embedding (exact): the 48 local qubits of a site form two free O-orbits of labels and can be placed O-equivariantly on two free orbits of fine sites in a 5 x 5 x 5 block of a one-qubit-per-site lattice, with the 77 other fine sites as frozen spectators; the corner code's rotation about a site is then the framework's rotation about a block-centre fine site (a fine-site permutation) times the same on-block Clifford corrections, and coarse translations are fine translations by 5. Not claimed: that a one-qubit-per-site rule invariant under unit fine translations produces this structure; dynamics beyond the free one-fermion problem in a static flux background; the size of the gaps relative to any physical scale; or any physical identification."
upstream_dependencies:
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py
---

# The corner fermion seen at long wavelengths is one isotropic spin-1/2 doublet; the 48-qubit sites embed in one-qubit-per-site blocks

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Parts 1 and 4 are exact. Parts 2 and 3 are numerical on the stated parameter sets. Nothing is adopted.

## Question

The owner proposed that the electron is much larger than the grid, possibly by many orders of magnitude. For such a fermion, what matters is its long-wavelength theory, not its lattice-scale details. Two questions follow.

1. **The long-wavelength theory.** Is it that of a single spin-1/2 particle? It could instead be spinless, or carry an extra internal label from several band minima.
2. **The qubit count.** The corner code uses 48 qubits per site. Can this be reconciled with one qubit per site of a finer grid?

## Result

1. **The rotations act on momentum by an affine map (exact).**
   - The projective symmetry group gives R T_a R^−1 = ±T_{Ra}. So a rotation maps crystal momentum k to Rk + π s_R.
   - For square = plaquette = tube = π, exactly two momenta are fixed by all 24 rotations: k* = (π/2)(1,−1,1) and −k*.
   - For tube flux 0 no momentum is fixed, so any band minimum would come in a star of at least two momenta.
2. **The band minimum is one isotropic doublet (Bloch bands, five parameter sets).**
   - The global minimum is a single 2-fold level at k* (or at −k*, depending on the signs of t2 and λ). The other fixed momentum lies higher, by 2.8 t2 for these sets.
   - Every band is 2-fold degenerate at every momentum tested.
   - The Hessian of the lowest band at k* is isotropic, to 1e−8. 1/m* = 0.043 at t2 = 0.1, λ = −0.5.
   - The cubic anisotropy enters at fourth order: the relative [111]−[100] difference is 5e−4 at |δk| = 0.1, and it scales as δk².
   - **Why the mass is isotropic.** It is forced by symmetry: k* is fixed by all of O, and an O-invariant symmetric 2-tensor is a multiple of the identity.
   - **Earlier statement corrected.** The companion corner-code note said that "the band minimum leaves the symmetric momenta". That came from a scan that tested only Γ and R. The minimum sits at the affine-fixed momentum k*.
3. **The doublet is spin-1/2 (L = 4 lattice, which contains k*).**
   - The lowest one-fermion level of the lattice is this doublet, at the same energy as the Bloch minimum.
   - Under the twisted site rotations it carries a two-dimensional spinorial irrep of the binary octahedral group: E1/2 for λ < 0, E5/2 for λ > 0.
4. **Long-wavelength theory (symmetry argument from items 1–3).**
   - A fermion wavepacket of size w much larger than the spacing a has
     H_eff = E0 + |δk|² / 2m*.
   - It acts on a doublet that transforms as spin-1/2. At this order spin and orbital motion decouple, so the long-wavelength rotation group is SU(2)_spin × SO(3)_orbit.
   - The lattice enters only through quartic anisotropy and spin–orbit terms, of relative size (a/w)².
5. **One qubit per fine site (exact).**
   - **The labels.** The 48 local qubits form two free orbits of labels under O: 24 on-site hop qubits and 24 link halves.
   - **The fine sites.** In a 5 × 5 × 5 block of a one-qubit-per-site lattice, the points (1,2,0) and (1,2,2) have disjoint free orbits.
   - **The placement.** Placing the labels equivariantly on these orbits is a bijection with p(R·l) = R·p(l), for all 24 rotations and all 48 labels.
   - **The spectators.** The other 77 fine sites form a union of orbits. They can be frozen by single-site terms.
   - **The consequences.**
     - The corner code's rotation about a site becomes the framework's own rotation about a block-centre fine site, which is a fine-site permutation, times the same on-block Clifford corrections.
     - Coarse translations become fine translations by 5.
     - Translations by one fine site are not symmetries of the embedded model.

## How this bears on the lane (interpretation, not a claim)

- **A large spin-1/2 particle.** If the grid is much finer than the fermion, as the owner proposes, the corner fermion looks at long wavelengths like a single spin-1/2 particle with an isotropic mass.
  - It is not spinless, and it has no extra valley label.
  - Lattice details are suppressed by (a/w)². For a lattice spacing many orders of magnitude below the particle's size, this is negligible.
- **Spin survives the large size.** The spin-1/2 is fixed at the lattice scale, by the doublet's irrep at k*. The large size does not wash it out; it only removes the cubic anisotropy.
- **The qubit count is not physical at long wavelengths.** Embedding shows that 48 qubits per site is the same as one qubit per fine site with 5 × 5 × 5 blocks. The real open question has moved: can a uniform one-qubit rule produce this block structure by itself, for example by spontaneously breaking fine translations?
- **What is still supplied.**
  - The corner structure, the fluxes and the hopping.
  - The U(1)-twisted realization (number-conserving dynamics).
  - A nonrelativistic particle. There is no Dirac structure, and no electric charge beyond the conserved fermion number.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations about sites); one qubit per site for item 5.
- **Supplied.**
  - The corner model, flux pattern and one-fermion Hamiltonian stated above. The qubit realization of the companion note passes its 18 checks for this flux pattern too (loop pack, `runner_qubits_L4_flux1011.log`).
  - The twisted realization of the companion note.
  - A static flux background. The one-fermion problem is exact there, because the loop terms commute with the hops.
- **Standard facts used.**
  - Bloch's theorem with projective translations.
  - Invariant tensors of O.
  - k·p perturbation theory around a symmetric minimum.

## Relation to prior work

- **Projective symmetry groups and momentum-shifted rotations.** Wen, PRB 65, 165113 (2002).
- **Magnetic space groups** are standard.
- **Doubled bands from combined inversion and time reversal** are standard (the Kramers-type degeneracy found here).
- **Spinorial structure from π-flux cubic hopping.** Staggered fermions: Kogut and Susskind (1975); Golterman and Smit (1984).
- **New here.**
  - The affine fixed momenta of the corner fermion.
  - The verification that its band minimum is a single isotropic spin-1/2 doublet there.
  - The equivariant one-qubit-per-site block embedding of the 48-qubit site.

## No-Go Discipline Gate

- **N1 — routes.**
  - Other flux patterns: tube 0 gives no fixed momentum.
  - Other hopping families.
  - Dynamics with fluctuating fluxes.
- **N2/N3 — scope.** Five parameter sets for the bands, and L = 4 for the irrep.
- **N4 — inputs.** Part 1 and Part 4 are exact. Parts 2 and 3 use floating-point Bloch spectra and characters. The long-wavelength statement is a symmetry argument from them.
- **N5 — wording.** "Spin-1/2 doublet" means the E1/2 or E5/2 irrep under the stated, twisted realization. "Large" means a wavepacket size w ≫ a.
- **N6/N7 — strongest objections.**
  - The construction is supplied, not derived from the framework's axioms.
  - The embedding breaks unit fine translations explicitly.
  - The particle is nonrelativistic.
- **N8 — earlier claims.** Corrects the companion note's statement about the band minimum.

## Verification

```bash
python3 scripts/corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py
```

Expected: `TOTAL: PASS=12 FAIL=0` (about 25 seconds). It reuses the definitions of the corner PSG runner.

## Load-bearing sources

- [Corner-code note](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
