---
claim_id: corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the corner fermion of the companion notes, flux square = plaquette = tube = pi, triangle = 0, translation-invariant gauge, L = 4 torus, one-fermion Hamiltonian H = -t1 sum_onsite u c^dag c - t2 sum_links u c^dag c + delta X (+ m M), number-conserving. Finite numerical evidence from group averaging and diagonalization, with conditional representation arguments: (1) the one-fermion terms of range <= 1 site that are invariant under the 24 site rotations, the site inversion and the translations and odd under complex conjugation have sampled numerical rank 9 from fourteen averaged seeds; completeness of this space is not established; (2) with one such term X (t1 = -1, t2 = 0.2, delta = 0.05) the lowest levels at the two rotation-fixed momenta k* and -k* are degenerate doublets (inversion), each splitting linearly with one velocity in all directions (spread 1e-10), with Berry flux -1 and +1 through small spheres: an opposite-chirality Weyl pair; (3) selection rule: conditional on the stated distinct valley irreps, every rotation-invariant staggered (momentum Q = (pi,pi,pi)) on-site term has zero first-order projected matrix elements in the four-state node space, because the doublets at k* and -k* carry E1/2 and E5/2 (they differ by the pseudoscalar character A2), so a first-order projected invariant mass is excluded; finite-strength and higher-order effects remain outside this selection argument; (4) an imaginary A2 staggered on-site term (ten sampled seeds have rank 5; three tested real seeds give zero; no completeness or universal real-term claim) splits the node space into two doublets at E_N -+ m_D with the projected first-order m_D linear in its strength, and the folded Bloch Hamiltonian agrees numerically with the real-space spectrum; its finite near-node comparison with +-sqrt(v^2 dk^2 + m_D^2) is gap-dominated corroboration, not an exact dispersion theorem; (5) the massless node states form E1/2 + E5/2 under the twisted site rotations and each massive doublet is the irreducible spin-1/2 representation of the binary tetrahedral group; (6) the massive Hamiltonian is invariant under the rotations of T about a site, under the w1-odd rotations composed with an odd translation (together the 24 rotations about a cube centre) and under the even translations, while w1-odd rotations about a site alone are broken. Not claimed: that the Dirac point is the global low-energy feature (for the stated parameters other parts of the band come closer), a filled Dirac vacuum, the qubit-level construction of X and M (by the BKSF dictionary they are even fermion operators, encodable as Paulis, but this is not built here), a mechanism that generates the pseudoscalar mass, electric charge, or any physical identification."
upstream_dependencies:
  - corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_2026_10_17.py
---

# Corner-model Weyl-pair evidence and a supplied pseudoscalar mass candidate

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Numerical support for the supplied model on the L = 4 torus; conditional selection-rule argument. Nothing is adopted.

## Question

The companion note finds a numerical candidate for an isolated spinorial minimum in a supplied corner Hamiltonian. Inversion-times-conjugation symmetry I·K excludes a linear splitting in the protected doublet. Breaking that symmetry permits, but does not force, a nonzero Weyl coefficient.

A massive Dirac fermion is a closer analogue of the electron. Can the corner model produce one: a four-component spin-1/2 particle with dispersion E = ±√(v²k² + m²)? What does it cost?

## Result

1. **Weyl pair.**
   - **The allowed terms.** One-fermion terms that respect all 24 site rotations, the site inversion and the translations, are odd under complex conjugation and have range ≤ 1 site, have sampled numerical rank 9 from fourteen averaged seeds; completeness of this space is not established.
   - **The pair.** With one such term (t1 = −1, t2 = 0.2, strength 0.05), the rotation-fixed momenta k* and −k* host degenerate doublets.
     - Each doublet splits linearly with a single velocity, so the cone is isotropic.
     - The Berry fluxes are −1 and +1.
     - So this is a massless Dirac pair: two Weyl nodes of opposite chirality.
2. **The cube rotations protect it.**
   - The doublets at k* and −k* carry E1/2 and E5/2. These differ by the pseudoscalar character A2, the sign of the direction permutation.
   - Conditional on the numerically reconstructed distinct valley irreps, Schur’s lemma makes every rotation-invariant inter-valley intertwiner zero. Momentum Q = k* − (−k*) eliminates same-valley blocks, so staggered on-site terms have zero first-order projection to the four node states.
   - This forbids a first-order projected mass in the specified node space; finite-strength band rearrangements and higher-order effective terms require separate analysis.
   - The w1-odd rotations (C4 and the edge C2) act on the four node states like a chiral transformation. This plays the role of the shift symmetries of staggered fermions.
3. **A pseudoscalar mass makes it massive.**
   - **Which terms work.** The exhibited imaginary staggered on-site term that transforms as A2 (ten sampled seeds have numerical rank 5, a lower bound) splits the node space into two doublets at E_N ∓ m_D, with the projected first-order m_D linear in its strength. The three sampled real A2 seeds have zero projected mass. This is not an exhaustive statement about every real term. Other A2 terms can lie in the kernel of projection; membership in the sampled span alone does not guarantee a nonzero mass.
   - **The dispersion.** The folded Bloch Hamiltonian reproduces the real-space spectrum numerically. A finite small-momentum comparison uses the corrected Weyl velocity v (without an extra factor of one half). Total-energy agreement near a nonzero gap is only corroboration: it can hide an incorrect kinetic coefficient and does not prove an exact Dirac dispersion or uniform remainder.
   - **Leading joint limit.** Projection to the isolated four-node subspace gives numerical kinetic matrices K_i and a mass matrix M_0 with {K_i,K_j}=2v²δ_ij I, M_0²=c²I and {K_i,M_0}=0, with v≈0.10959552 and c≈1.40405896. These imply the projected leading spectrum E_N±sqrt(v²|q|²+c²m²). The finite Laurent Hamiltonian is analytic and the node quartet is spectrally separated, so perturbation theory permits O(|q|²+|qm|+m²) corrections; no certified uniform numerical remainder bound is supplied. The runner checks the matrix relations numerically and three joint shrinkage samples. The old extra factor of one half in the velocity was erroneous and is corrected.
4. **Its components are spin-1/2.**
   - The massless node states form E1/2 + E5/2 under the twisted site rotations.
   - Each massive doublet is the irreducible spin-1/2 representation of the binary tetrahedral group 2T.
5. **The massive model keeps a full cube group.**
   - **Kept:**
     - the rotations of T about a site;
     - the w1-odd rotations composed with an odd translation. For c=(1/2,1/2,1/2), the actual cube-centred rotation is (R,c−Rc). Its integer translation has parity w1(R), so it differs from the tested fixed odd translation by a preserved even translation. Together with T, these give the 24 rotations about that centre;
     - the even translations.
   - **Broken:** the w1-odd rotations about a site alone.

## How this bears on the lane (interpretation, not a claim)

- **A supplied four-band candidate.** The numerical node-space evidence motivates a leading-order Dirac description of the two valleys. This is a model analogy, not an electron, a derived relativistic vacuum, or an exact lattice dispersion. Velocity and mass strength are supplied parameters.
- **The mass breaks a chiral-like symmetry.** In this model it requires breaking the site-centred cube rotations down to T. The full cube group survives about cube centres.
  - This has the shape of chiral symmetry breaking: the w1-odd rotations act as the chiral transformation, and the mass is the pseudoscalar order parameter.
  - Whether the mass can arise spontaneously, for example from interactions, is open.
- **Not shown.**
  - That the Dirac point is the global low-energy feature, so that filling the lower bands gives a clean Dirac vacuum.
    - At the stated parameters the lower band rises 0.16 above the node energy, and bands 0 and 1 touch at 24 further Weyl points (independent check).
    - **Author search.** Optimization over the sampled 9-dimensional span (t2 ≥ 0.05, fixed Weyl velocity, |coefficients| ≤ 3) found no ideal node: the best excess on a 24^3 grid was 0.05. Unbounded searches exploited coarse grids.
    - **Independent search.** About 1,800 random sets plus optimization found no clean gapped vacuum. The best case has a positive gap of only 0.22–0.46 of 2 m_D, because of extra Weyl touchings.
    - Longer-range terms are untested.
    - Logs: loop pack, `c19_dirac/`.
  - The qubit construction of the new terms.
  - Charge.

## Independent check

A fresh-context agent (same model family) wrote its own code, then reran the author's runner version (17/17). Its findings bear on the claims above as follows.
- **Selection rule: confirmed and broader.**
  - With exact signed-orbit counting at ranges up to |sh|_1 ≤ 2, the inter-node coupling of every rotation-invariant staggered term is ≤ 8.6e−16.
  - It also holds without translation symmetry: with averaging over the 24 site rotations only, the coupling is ≤ 3.3e−14. That is Schur's lemma for the site rotations.
  - Real A2 masses vanish at all ranges tested.
- **Weyl pair: confirmed** over 40 random parameter sets.
  - The velocity (0.027–0.147) and the sign of the chirality depend on X.
  - The doublet is the lowest level only for t1 = −1 with modest strength (17 of 40).
- **Massive Dirac.**
  - Mass space rank 5, and m_D exactly linear in the mass strength.
  - An isotropic scalar term c δk² (c = 0.0275) accompanies the Dirac form.
  - A generic mass breaks site inversion. Its 5-dimensional span has 3 inversion-even and 2 inversion-odd directions, so the phase is axion-like.
- **Cube-centre group.**
  - The composed operations were verified geometrically to be rotations about a cube centre.
  - The fermion is in the spin-1/2 class under them: two perpendicular half-turns anticommute.
  - Each massive doublet is a spinorial irrep of the double cover of this group.
- **Global structure.** No clean Dirac vacuum was found; see "Not shown".

Files: `.claude/science/physics-loops/toe-campaign-20261017/c19_dirac/independent_check/` (REPORT.txt; the refined numbers in `globalband_*.log` predate a sign fix, so use the grid numbers there and the `verify*` and `touch*` logs).

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
- **Weyl nodes coupled by a density wave, with an axion phase.** Wang and Zhang, PRB 87, 161107(R) (2013).
- **Zero- and finite-momentum pairing in Weyl semimetals.** Cho, Bardarson, Lu and Moore, PRB 86, 214514 (2012).
- **The pinning here is different.** It comes from a two-dimensional projective irrep at an affine-fixed momentum. It is not the time-reversal Kramers–Weyl mechanism.
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
  - A number-violating (Majorana) mass.
    - The independent check found that under the twisted action a momentum-Q pairing invariant under all 24 twisted rotations (on-site, sampled rank 5) gaps each Weyl node. So the protection in item 2 requires number conservation.
    - Under the untwisted action, only momentum-0 inter-node pairing is allowed, and it leaves the nodes gapless.
    - These findings come from the check's own code and are not built into the runner.
  - Longer-range masses.
  - Other flux patterns.
- **N2/N3 — scope.** One flux pattern, L = 4, and one generic choice of X and M from each space.
- **N4 — inputs.** Floating-point group averaging and diagonalization; sampled ranks are lower bounds, not complete dimension classifications.
- **N5 — wording.** "Dirac candidate" refers to the proposed leading-order four-band description of the opposite-chirality pair; the full lattice spectrum contains higher-order corrections. "Spin-1/2" means the irreps stated.
- **N6/N7 — strongest objections.**
  - The mass breaks the site rotations to T.
  - The Dirac point is not shown to be the global low-energy feature.
  - The terms are supplied.
- **N8 — earlier claims.** Extends the long-wavelength note. It does not change it.

## Verification

```bash
python3 scripts/corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_2026_10_17.py
```

Expected: `TOTAL: PASS=19 FAIL=0` (about two minutes).

## Load-bearing sources

- [Long-wavelength note](CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Corner-code note](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
