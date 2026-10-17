---
claim_id: corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the corner fermion of the companion corner-code note in the flux pattern square = plaquette = tube = pi, triangle = 0, with one-fermion Hamiltonian H = -t1 sum_onsite u c^dag c - t2 sum_links u c^dag c + i lambda sum over oriented triangles (gauge signs u), t1 = -1, lambda nonzero. Exact (fermion level): the site rotations act on crystal momentum by k -> R k + pi s_R (s_R from the projective symmetry group); H(R k + pi s_R) is unitarily equivalent to H(k); for this pattern exactly two momenta are fixed by all 24 rotations, k* and -k* = k* + (pi,pi,pi) (k* = (pi/2)(1,-1,1) in the runner's gauge; for tube flux 0 none is fixed). Numerical (12 x 12 Bloch bands; five parameter sets in the runner and 174 more in the independent check, t2 = +-0.05 to 2, |lambda| = 0.03 to 1.5): the searches found a lowest candidate that is a single 2-fold level at k* or -k*, the other lying higher by 2 sqrt2 min(|t2|, 2|lambda|); the hopping family has the antiunitary symmetry I K (site inversion times complex conjugation), which fixes every momentum and squares to -1, so every band is 2-fold; the effective-mass tensor at k* is isotropic (forced by the O-fixed momentum) and the cubic anisotropy is fourth order. On the L = 4 lattice (which contains k*) the lowest one-fermion level is this doublet and carries a two-dimensional spinorial irrep of the binary octahedral group under the twisted site rotations (E1/2 or E5/2 depending on the lift convention; the label flips with the sign of lambda). Long-wavelength theory: with I K, H_eff = [E0 + |dk|^2 / (2 m*) + O(|dk|^4)] I on an isolated doublet, conditional on the I K symmetry; scalar higher-order cubic anisotropy is allowed; O alone also allows an isotropic Weyl-form term alpha dk.sigma, which the exhibited translation- and U(1)-preserving perturbation generates; not every I K-breaking hop has a nonzero coefficient. Embedding (exact): the 48 local qubits form two free O-orbits and can be placed O-equivariantly on two free orbits of fine sites in a 5 x 5 x 5 block of a one-qubit-per-site lattice (the smallest site-centred cube that works), with 77 frozen spectators; the untwisted rotation is then a fine-site permutation about a block-centre site times on-block Clifford corrections (the spin-1/2 twist adds Clifford two-block gates), with term ranges up to 9 fine spacings. Not claimed: lambda = 0 (two valleys), the opposite sign sector (a quartet minimum), tube flux 0, generic I K-breaking dynamics beyond the stated Weyl term, a uniform one-qubit rule producing the blocks, or any physical identification."
upstream_dependencies:
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
runner: scripts/corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py
---

# The corner fermion at long wavelengths: one spin-1/2 doublet at a rotation-fixed momentum (nonrelativistic with I·K, Weyl-form terms allowed without); the 48-qubit sites embed in one-qubit-per-site blocks

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Items 1 and 5 are exact. Items 2 and 3 are numerical on the stated parameter sets. Item 4 is a symmetry argument from them. Nothing is adopted.

## Question

The owner proposed that the electron is much larger than the grid, possibly by many orders of magnitude. For such a fermion, what matters is its long-wavelength theory, not its lattice-scale details. Two questions follow.

1. **The long-wavelength theory.** Is it that of a single spin-1/2 particle? It could instead be spinless, or carry an extra internal label from several band minima.
2. **The qubit count.** The corner code uses 48 qubits per site. Can this be reconciled with one qubit per site of a finer grid?

## Result

1. **The rotations act on momentum by an affine map (exact).**
   - The projective symmetry group gives R T_a R^−1 = ±T_{Ra}. So a rotation maps crystal momentum k to Rk + π s_R.
   - For square = plaquette = tube = π, exactly two momenta are fixed by all 24 rotations: k* and −k* = k* + (π,π,π). In the runner's gauge, k* = (π/2)(1,−1,1); other gauges give another of the ±(π/2)(1,±1,±1).
   - The independent check verified H(Rk + πs_R) = W H(k) W^T directly, to 1.6e−16, for every rotation.
   - For tube flux 0 no momentum is fixed, so any band minimum would come in a star of at least two momenta.
2. **The band minimum is one isotropic doublet (Bloch bands, five parameter sets).**
   - The lowest candidate found by the stated searches is a single 2-fold level at k* (or at −k*, depending on the signs of t2 and λ).
     - The other fixed momentum lies higher, by 2√2 min(|t2|, 2|λ|).
     - The historical independent scan found the same lowest candidate in 174 further sets, and reported a second, higher local minimum for small |lambda|. These searches do not certify a unique local or global minimum.
     - It fails at λ = 0 (two valleys, four states), in the opposite sign sector t1 = +1 with triangle 0 (a G3/2 quartet), and for tube flux 0 (two valleys).
   - **Every band is 2-fold.** The cause is the antiunitary symmetry I·K, site inversion times complex conjugation, of this hopping family. It fixes every momentum and squares to −1.
     - It is not one of O, the translations or U(1).
     - Generic symmetry-allowed hops break it: for example 28 of 36 symmetrized second-neighbour hops.
   - The Hessian of the lowest band at k* is isotropic, to 1e−8. 1/m* = 0.043 at t2 = 0.1, λ = −0.5.
   - The cubic anisotropy enters at fourth order: the relative [111]−[100] difference is 5e−4 at |δk| = 0.1, and it scales as δk².
   - **Why the mass is isotropic.** It is forced by symmetry: k* is fixed by all of O, and an O-invariant symmetric 2-tensor is a multiple of the identity.
   - **Earlier statement corrected.** The companion corner-code note said that "the band minimum leaves the symmetric momenta". That came from a scan that tested only Γ and R. The minimum sits at the affine-fixed momentum k*.
3. **The doublet is spin-1/2 (L = 4 lattice, which contains k*).**
   - The lowest one-fermion level of the lattice is this doublet, at the same energy as the Bloch minimum.
   - Under the twisted site rotations it carries a two-dimensional spinorial irrep of the binary octahedral group.
     - With the runner's lift it is E1/2 for λ < 0 and E5/2 for λ > 0.
     - The other valid lift exchanges the labels. What is convention-free: a spinorial doublet whose label flips with λ, and whose spin vector transforms as a vector.
4. **Long-wavelength theory (symmetry argument from items 1–3; corrected by the independent check).**
   - **With I·K, the supplied family.**
     - A fermion wavepacket of size w ≫ a has H_eff = [E0 + |δk|²/(2m*) + O(|δk|⁴)] I within the isolated doublet. I·K forbids a Pauli-vector splitting at each momentum; it does not remove higher-order scalar dispersion or cubic anisotropy.
     - Lattice anisotropy enters at δk⁴, of relative size (a/w)².
     - Spin–orbit effects appear only in external fields, through the non-abelian Berry curvature of the 2-fold band. Its eigenvalues at k* are ±6e−4 a².
     - This is a nonrelativistic spin-1/2 particle.
   - **Without I·K.**
     - O alone allows an isotropic linear term α δk·σ at k*: a Weyl-form crossing.
     - The exhibited O-, translation- and U(1)-invariant perturbation has α = (2/3)δ. Here T denotes translations, not time reversal. Other I·K-breaking perturbations may have α=0; the author scan reports such examples. No generic Kramers protection is established.
     - For the leading isotropic quadratic-plus-Weyl approximation, the lower branch has a minimizing shell |δk| ≈ m*|α|; higher-order lattice terms can split it.
     - If α is nonzero, the linear term dominates sufficiently near the crossing. This local two-band expansion is not a relativistic spacetime theory, an identification with a neutrino, or a description of a wavepacket centered at the shifted ground minimum.
   - **In both cases** the doublet is spin-1/2, and the lattice rotations act on it as the restriction of SU(2).
5. **One qubit per fine site (exact).**
   - **The labels.** The 48 local qubits form two free orbits of labels under O: 24 on-site hop qubits and 24 link halves.
   - **The fine sites.** In a 5 × 5 × 5 block of a one-qubit-per-site lattice, the points (1,2,0) and (1,2,2) have disjoint free orbits.
   - **The placement.** Placing the labels equivariantly on these orbits is a bijection with p(R·l) = R·p(l), for all 24 rotations and all 48 labels.
   - **The spectators.** The other 77 fine sites form a union of orbits. They can be frozen by single-site terms.
   - **The consequences.**
     - The corner code's untwisted rotation about a site becomes the framework's own rotation about a block-centre fine site, which is a fine-site permutation, times the same on-block Clifford corrections.
     - The spin-1/2 twist adds exp(−iπR/4) gates across adjacent blocks. These are two-block Clifford gates: exp(-i pi P/4) maps Paulis to Paulis for Pauli P=R.
     - Term ranges reach 9 fine spacings.
     - 5 × 5 × 5 is the smallest site-centred cube that works: it has three free point orbits, and 3 × 3 × 3 has none.
     - Coarse translations become fine translations by 5.
     - Translations by one fine site are not symmetries of the embedded model.

## Scope of the discrete and symmetry evidence

For an affine-fixed momentum, the axis half-turn equations impose 2k_i = pi times an integer modulo 2pi. Thus the quarter-grid enumeration is complete for the fixed-point question; it is not a band-minimum search certificate. The primary band search uses a 16³ grid and 16 Nelder–Mead starts per parameter set and now reports convergence failures explicitly.

Independent coefficient-level control constructs inversion as a real signed matrix W with W²=-I and zero affine shift. For each Laurent shift d and each parameter component it verifies W conjugate(C[-d]) Wᵀ = C[d]. This is the algebraic I·K symmetry identity for all momenta of the supplied finite-range family, stronger than random spectral samples. It enforces paired bands and a scalar Hamiltonian in an isolated doublet, without enforcing exactly quadratic dispersion. Source/result: `outputs/campaign_c16_c18_landing_2026_10_17/independent_controls/antiunitary-control.py.txt` and `antiunitary-control.json` in that same directory. The independent Bloch control also exhibits two distinct local minima at t2=.3, lambda=.03; its source and result are preserved there. No global-band or physical-particle claim follows.

## How this bears on the lane (interpretation, not a claim)

- **Conditional long-wavelength description.** For an isolated spinorial doublet of the supplied hopping model, I·K gives scalar band dispersion with leading isotropic quadratic curvature. The numerical searches support the stated candidate minimum but do not certify global uniqueness. If an allowed perturbation supplies nonzero alpha, a Weyl-form term can appear locally near the crossing; this does not establish physical spin, Lorentz symmetry or a neutrino.
- **Embedding boundary.** The equivariant 48-label placement is an encoding into selected 5×5×5 blocks with 77 spectators, on-block Clifford corrections and two-block Clifford twist gates. It has range up to nine fine spacings and breaks unit fine translations. This does not make qubit count physically irrelevant or derive a uniform one-qubit nearest-neighbour rule. Whether such dynamics can produce the block structure remains open.
- **What is still supplied.**
  - The corner structure, the fluxes and the hopping.
  - The U(1)-twisted realization (number-conserving dynamics).
  - The I·K symmetry, for the nonrelativistic case.
  - There is no Dirac (massive relativistic) structure, and no electric charge beyond the conserved fermion number.

## Historical author check

The following reports submitted checks; their finite/numerical scope and the higher-local-minimum correction above control.

A fresh-context agent (same model family) wrote its own corner graph, gauge, PSG solve and 2O lifts. By brute force it found only four cycle classes, and these span the cycle space.
- **Items 1–3: confirmed.**
  - The minimum, gap, isotropy and anisotropy numbers reproduce.
  - The affine covariance holds to 1.6e−16.
  - The same lowest candidate was found in 174 further parameter sets; higher local minima occur in part of that scan, and global uniqueness is not certified.
- **Item 4: corrected (substantive).** The absence of spin–orbit coupling is due to I·K, not to O. O allows a Weyl-form term, which dominates at long wavelengths when I·K is broken. The note now states this.
- **Item 5: confirmed, with corrections.** The twisted action needs two-block gates; term ranges and the minimal block size are now stated.
- **Wording.** The gauge-free statement of k*, the lift convention, the failure regions, the numbering and the prior art are all fixed.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c18_large_fermion/independent_check/`.

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
- **Spin–orbit and degeneracy in band theory.**
  - Elliott, Phys. Rev. 96, 266 (1954).
  - Luttinger, Phys. Rev. 102, 1030 (1956).
- **Non-abelian Berry curvature of degenerate bands.**
  - Culcer, Yao and Niu, PRB 72, 085110 (2005).
  - Shindou and Imura, NPB 720, 399 (2005).
- **Kramers–Weyl and multifold fermions in chiral crystals.**
  - Chang et al., Nat. Mater. 17, 978 (2018).
  - Bradlyn et al., Science 353, aaf5037 (2016).
- **Spinorial structure from π-flux cubic hopping.** Staggered fermions: Kogut and Susskind (1975); Golterman and Smit (1984).
- **New here.**
  - The affine fixed momenta of the corner fermion.
  - The numerical evidence for an isolated spinorial doublet at the candidate minimum and its isotropic leading curvature.
  - The equivariant one-qubit-per-site block embedding of the 48-qubit site.

## No-Go Discipline Gate

- **N1 — routes.**
  - λ = 0 (two valleys).
  - The opposite sign sector (a quartet).
  - I·K-breaking dynamics (Weyl-form terms allowed).
  - Other flux patterns: tube 0 gives no fixed momentum.
  - Other hopping families.
  - Dynamics with fluctuating fluxes.
- **N2/N3 — scope.** Five parameter sets for the bands, and L = 4 for the irrep.
- **N4 — inputs.** The discrete affine and embedding calculations are finite controls. Parts 2 and 3 use floating-point Bloch spectra and characters. The long-wavelength statement is conditional on an isolated doublet and the specified symmetry; numerical searches are not global-minimum proofs.
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
