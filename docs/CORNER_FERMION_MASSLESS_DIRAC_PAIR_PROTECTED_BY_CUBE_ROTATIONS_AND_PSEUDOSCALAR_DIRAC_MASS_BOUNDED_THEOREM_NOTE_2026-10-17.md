---
claim_id: corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the corner fermion of the companion notes, flux square = plaquette = tube = pi, triangle = 0, translation-invariant gauge, L = 4 torus, one-fermion Hamiltonian H = -t1 sum_onsite u c^dag c - t2 sum_links u c^dag c + delta X (+ m M), number-conserving. Exact up to floating point (finite group averaging and diagonalization): (1) the one-fermion terms of range <= 1 site that are invariant under the 24 site rotations, the site inversion and the translations and odd under complex conjugation form a 9-dimensional space; (2) with one such term X (t1 = -1, t2 = 0.2, delta = 0.05) the lowest levels at the two rotation-fixed momenta k* and -k* are degenerate doublets (inversion), each splitting linearly with one velocity in all directions (spread 1e-10), with Berry flux -1 and +1 through small spheres: an opposite-chirality Weyl pair; (3) selection rule: every rotation-invariant staggered (momentum Q = (pi,pi,pi)) on-site term has zero matrix elements in the four-state node space, because the doublets at k* and -k* carry E1/2 and E5/2 (they differ by the pseudoscalar character A2), so no rotation-invariant, number-conserving term of this kind gives a Dirac mass; (4) an imaginary A2 staggered on-site term (a 5-dimensional space; real ones give zero) splits the node space into two doublets at E_N -+ m_D with m_D linear in its strength, and the folded Bloch Hamiltonian (checked against the real-space spectrum) gives E - E_N = +-sqrt(v^2 dk^2 + m_D^2) near k*, isotropic to 5e-4; (5) the massless node states form E1/2 + E5/2 under the twisted site rotations and each massive doublet is the irreducible spin-1/2 representation of the binary tetrahedral group; (6) the massive Hamiltonian is invariant under the rotations of T about a site, under the w1-odd rotations composed with an odd translation (together the 24 rotations about a cube centre) and under the even translations, while w1-odd rotations about a site alone are broken. Not claimed: that the Dirac point is the global low-energy feature (for the stated parameters other parts of the band come closer), a filled Dirac vacuum, the qubit-level construction of X and M (by the BKSF dictionary they are even fermion operators, encodable as Paulis, but this is not built here), a mechanism that generates the pseudoscalar mass, electric charge, or any physical identification."
upstream_dependencies:
  - corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_2026_10_17.py
---

# The corner fermion: a massless Dirac pair protected by the cube rotations, and a pseudoscalar Dirac mass

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact up to floating point for the supplied model on the L = 4 torus. Nothing is adopted.

## Question

The long-wavelength note found that the large corner fermion is a single spin-1/2 doublet. With the inversion-times-conjugation symmetry I·K it is nonrelativistic; without it, it is a Weyl fermion.

A massive Dirac fermion is a closer analogue of the electron. Can the corner model produce one: a four-component spin-1/2 particle with dispersion E = ±√(v²k² + m²)? What does it cost?

## Result

1. **Weyl pair.**
   - **The allowed terms.** One-fermion terms that respect all 24 site rotations, the site inversion and the translations, are odd under complex conjugation and have range ≤ 1 site, form a 9-dimensional space.
   - **The pair.** With one such term (t1 = −1, t2 = 0.2, strength 0.05), the rotation-fixed momenta k* and −k* host degenerate doublets.
     - Each doublet splits linearly with a single velocity, so the cone is isotropic.
     - The Berry fluxes are −1 and +1.
     - So this is a massless Dirac pair: two Weyl nodes of opposite chirality.
2. **The cube rotations protect it.**
   - The doublets at k* and −k* carry E1/2 and E5/2. These differ by the pseudoscalar character A2, the sign of the direction permutation.
   - Every rotation-invariant staggered term (momentum Q = k* − (−k*)) therefore has zero matrix elements in the four-state node space.
   - So no rotation-invariant, number-conserving term of this kind gives a Dirac mass.
   - The w1-odd rotations (C4 and the edge C2) act on the four node states like a chiral transformation. This plays the role of the shift symmetries of staggered fermions.
3. **A pseudoscalar mass makes it massive.**
   - **Which terms work.** An imaginary staggered on-site term that transforms as A2 (a 5-dimensional space) splits the node space into two doublets at E_N ∓ m_D, with m_D linear in its strength. Real A2 terms give no mass.
   - **The dispersion.** The folded Bloch Hamiltonian reproduces the real-space spectrum exactly. Near k* it gives E − E_N = ±√(v²δk² + m_D²), the same in every direction to 5e−4: a massive Dirac fermion.
4. **Its components are spin-1/2.**
   - The massless node states form E1/2 + E5/2 under the twisted site rotations.
   - Each massive doublet is the irreducible spin-1/2 representation of the binary tetrahedral group 2T.
5. **The massive model keeps a full cube group.**
   - **Kept:**
     - the rotations of T about a site;
     - the w1-odd rotations composed with an odd translation. Together with T, these are the 24 rotations about a cube centre;
     - the even translations.
   - **Broken:** the w1-odd rotations about a site alone.

## How this bears on the lane (interpretation, not a claim)

- **A four-component spin-1/2 particle.** The corner model now produces a massive, isotropic Dirac particle at long wavelengths. Its components are spin ⊗ valley, with the valleys k* and −k*.
  - This is the structure of the electron's Dirac equation, minus charge.
  - The lattice fixes the spin. The mass m_D and the velocity v are free parameters.
- **The mass breaks a chiral-like symmetry.** In this model it requires breaking the site-centred cube rotations down to T. The full cube group survives about cube centres.
  - This has the shape of chiral symmetry breaking: the w1-odd rotations act as the chiral transformation, and the mass is the pseudoscalar order parameter.
  - Whether the mass can arise spontaneously, for example from interactions, is open.
- **Not shown.**
  - That the Dirac point is the global low-energy feature, so that filling the lower bands gives a clean Dirac vacuum.
    - An optimization over the 9-dimensional space was run (exploration, loop pack `c19_dirac/ideal3.log`), with t2 ≥ 0.05, Weyl velocity fixed to 0.05 and |coefficients| ≤ 3.
    - It found no ideal node: the best excess on a 24^3 grid was 0.05. Unbounded searches exploit coarse grids.
    - Longer-range terms are untested.
  - The qubit construction of the new terms.
  - Charge.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations about sites).
- **Supplied.**
  - The corner model and flux pattern.
  - The hopping, the conjugation-odd term X and the pseudoscalar mass M.
  - Number conservation, and the twisted realization of the companion notes, for the spin labels.
- **Standard facts used.**
  - Weyl node chirality as a Berry flux.
  - Selection rules for invariant operators.
  - The Dirac form of two coupled opposite-chirality Weyl nodes.

## Relation to prior work

- **Fermion doubling, and Weyl pairs coupled into Dirac fermions.**
  - Nielsen and Ninomiya, NPB 185, 20 (1981).
- **Staggered fermions: shift symmetries acting as γ5 × taste, and the staggered mass.**
  - Kogut and Susskind, PRD 11, 395 (1975).
  - Golterman and Smit, NPB 245, 61 (1984).
- **Kramers–Weyl and multifold fermions in chiral crystals.**
  - Chang et al., Nat. Mater. 17, 978 (2018).
  - Bradlyn et al., Science 353, aaf5037 (2016).
- **New here.**
  - The corner model's Weyl pair at the affine-fixed momenta.
  - The selection rule from the E1/2 / E5/2 labels.
  - The identification of the w1-odd rotations as the protecting chiral-like symmetry.
  - The pseudoscalar mass, with the symmetry of the massive model.

## No-Go Discipline Gate

- **N1 — routes.**
  - A number-violating (Majorana) mass, which the twisted action also allows in A2 form.
  - Longer-range masses.
  - Other flux patterns.
- **N2/N3 — scope.** One flux pattern, L = 4, and one generic choice of X and M from each space.
- **N4 — inputs.** Exact group averaging and diagonalization, in floating point.
- **N5 — wording.** "Dirac fermion" means the four-band spectrum ±√(v²k² + m²) of an opposite-chirality Weyl pair coupled by a mass. "Spin-1/2" means the irreps stated.
- **N6/N7 — strongest objections.**
  - The mass breaks the site rotations to T.
  - The Dirac point is not shown to be the global low-energy feature.
  - The terms are supplied.
- **N8 — earlier claims.** Extends the long-wavelength note. It does not change it.

## Verification

```bash
python3 scripts/corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_2026_10_17.py
```

Expected: `TOTAL: PASS=17 FAIL=0` (about two minutes).

## Load-bearing sources

- [Long-wavelength note](CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Corner-code note](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
