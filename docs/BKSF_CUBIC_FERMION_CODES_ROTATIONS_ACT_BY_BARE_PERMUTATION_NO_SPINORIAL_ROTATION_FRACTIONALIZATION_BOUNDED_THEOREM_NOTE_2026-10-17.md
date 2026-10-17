---
claim_id: bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_no_spinorial_rotation_fractionalization_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the 60 translation-invariant BKSF stabilizer codes on the cubic lattice (one qubit per edge of Z^3, one ordering of the six edge directions at every vertex) of the companion orbit note, with signed plaquette generators, one sign per plaquette orientation (8 translation-invariant sign sectors). Exact on the L = 4 torus (Pauli algebra with phases): all 8 sectors of all 60 codes are valid (-1 is not in the signed group); exactly two sectors are mapped to themselves by the bare qubit permutation of every stabilizing rotation of every code, and in them the point charge moved by the edge operators sees flux 0, respectively pi, through every plaquette; in each of the 6 mixed sectors some code has a stabilizing rotation whose bare permutation needs a sign correction. Proved from this: in the zero-flux and pi-flux sectors, a stabilizing rotation R of order n is realized by the bare permutation U_R with U_R^n = 1, its restriction to any R-invariant region has n-th power 1, and so the symmetry-fractionalization phase eta_f(R^n) of the fermion at an R-fixed vertex is +1; replacing U_R by U_R V with V any product of stabilizer generators does not change this. In particular C2^2 = +1 on the fermion: it is not spinorial under the lattice rotations. Not claimed: other realizations of the symmetry (non-Pauli or non-stabilizer dressings), sign patterns that are not translation-invariant, the mixed sectors, other encodings, dynamics, the continuum limit, or any physical identification (electron, spin)."
upstream_dependencies:
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
runner: scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py
---

# BKSF cubic fermion codes: lattice rotations act by bare permutation, so the fermion is not spinorial under them

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. The computations are exact on the
L = 4 torus for the stated family; the fractionalization statement is
proved from them. Nothing is adopted.

## Question

The companion orbit note showed that each translation-invariant BKSF code
carries a fermionic point charge and is fixed by a subgroup of the cubic
rotations (at most D3). An electron is a spin-1/2 fermion: a rotation by
2 pi acts on it as -1. On a lattice the analogous question is symmetry
fractionalization: does a rotation R of order n, acting on a fermion that
sits at a vertex fixed by R, have R^n = -1 relative to the vacuum? For
example, C2^2 = -1 would make the fermion spinorial under C2.

Two things decide this. First, the plaquette generators carry signs (flux
sectors), so we must ask which signed codes the rotation preserves. Second,
the rotation might need a Pauli sign correction F on top of the qubit
permutation P; then U = F P and U^n can be a nontrivial string operator that
anticommutes with the fermion's hopping legs.

## Result

1. **Sign sectors (exact, L = 4).** Give the plaquette generator normal to
   axis c the sign (-1)^{s_c}. All 8 translation-invariant sectors
   s = (s_x, s_y, s_z) of all 60 codes are valid stabilizer groups.
2. **Flux (exact).** Compare the hop product A(v,b) A(v+b,a) A(v+a,b) A(v,a)
   around a plaquette with the signed plaquette generator.
   - In one sector, (0,0,0) in the runner's convention, it equals the
     generator: the charge sees flux 0 through every plaquette.
   - In the sector (1,1,1) it equals minus the generator: flux pi through
     every plaquette.
3. **Rotations act by bare permutation (exact).** In these two sectors,
   every rotation in the stabilizer of every code (D3, the order-4 group or
   a single C2, by orbit type) maps every signed generator, under the bare
   qubit permutation, to an element of the same signed group. No sign
   correction is needed. So R is realized by U_R = P_R, and U_R^n = 1.
4. **Control (exact).** In each of the 6 mixed sectors, 44 of the 60 codes
   have a stabilizing rotation whose bare permutation does not preserve the
   signed group. So the test in item 3 can fail.
5. **No spinorial fractionalization (proof).**
   - Let R fix the vertex x0 and let D be any R-invariant region around x0.
     U_R restricted to D is a permutation of the qubits in D, so its n-th
     power is the identity.
   - The fractionalization phase eta_f(R^n) of a fermion at x0 is the phase
     of this local n-th power on the fermion state relative to the vacuum.
     It is therefore +1.
   - Dressing U_R by a product V of stabilizer generators changes the local
     n-th power by V V^R ... V^{R^{n-1}}. On a fermion at x0 only the vertex
     generator B_{x0} detects the charge, and since R fixes x0 its exponent
     in this product is n times its exponent in V. Plaquette generators
     commute with the edge operators, so they do not detect the charge.
   - For C2 (n = 2) this exponent is even, so the phase stays +1. For the
     C3 of the D3 codes, a phase is in any case removable: H^2(Z3, Z2) = 0.
   - So C2^2 = +1 on the fermion: it is not spinorial under the lattice
     rotations. The class eta_f(C2, C2) is gauge-invariant here, because
     f x f = 1 forces the gauge phase nu_f(C2) to be +-1.

## How this bears on the lane (interpretation, not a claim)

- **The electron's spin does not come from the microscopic rotations
  here.** In this family, a fermion that respects the lattice rotations
  carries integer lattice angular momentum. A spin-1/2 would have to be
  emergent.
- **The pi-flux sector is rotation-symmetric.** In it, the charge hopping
  with the edge operators sees pi flux on every plaquette. That
  single-particle problem is the Kogut–Susskind staggered-fermion hopping
  problem.
  - Its low-energy limit is two four-component Dirac fermions ("tastes").
  - Lattice rotations act on spin times taste, a product that is integer
    (1/2 x 1/2 = 0 + 1). This matches item 5.
- **The resulting picture.** A cubic-covariant lattice fermion that becomes
  a Dirac spin-1/2 at low energy, with spin locked to an internal taste
  label. Wen's string-net programme uses pi-flux fermions of this kind as
  emergent massless fermions. The new content here is the rotation-action
  computation in the cubic BKSF family, not the staggered physics.
- **Not computed.**
  - The projected hopping Hamiltonian is a dynamics choice, outside the
    axioms.
  - Gap stability and the continuum limit are not computed.
  - Whether the taste count interacts with the four-species minimum of the
    orbit note is open.

## Premises

- **Axioms used.** Lattice (Z^3, proper cubic rotations).
- **Supplied model.** The BKSF codes of the companion orbit note, with
  signed plaquette generators. As there, the qubits sit on edges, not on
  sites.
- **Declared choices.**
  - Translation-invariant signs.
  - Realizations of the symmetry of the form P_R times a Pauli.
  - Fractionalization at R-fixed vertices.

## Relation to prior work

- BKSF: Bravyi and Kitaev, Ann. Phys. 298, 210 (2002). Statistics criterion:
  Levin and Wen, PRB 67, 245316 (2003).
- Symmetry fractionalization and its gauge freedom: Barkeshli, Bonderson,
  Cheng and Wang, PRB 100, 115147 (2019).
- Staggered fermions: Kogut and Susskind, PRD 11, 395 (1975); Golterman and
  Smit, Nucl. Phys. B245, 61 (1984); Golterman, lecture notes
  arXiv:2406.02906. Symmetries of Hamiltonian staggered fermions, including
  lattice rotations: Catterall, Pradhan and Samlodia, arXiv:2501.10862.
- Emergent massless fermions from pi-flux string nets: Wen, PRD 68, 065003
  (2003).
- **New here.**
  - The sign-sector analysis of the rotation action on the cubic BKSF
    family.
  - The resulting fractionalization statement for its fermion.

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - Not covered: realizations of R with non-Pauli dressings, sign patterns
    that are not translation-invariant (for example, flux patterns with
    larger unit cells), the mixed sectors (there a sign correction exists
    and could fractionalize), other encodings, and stacks with couplings.
- **N2/N3 — scope.** One family, two sectors, one fractionalization class.
- **N4 — inputs.** Exact Pauli algebra with phases on the L = 4 torus. The
  generators are translation-invariant and the support is local, so the
  sign comparison is a local identity; L = 4 is the torus used throughout
  the companion note.
- **N5 — wording.** "Not spinorial" means eta_f(C2, C2) = +1. It does not
  exclude an emergent spin-1/2 under an emergent rotation group.
- **N6/N7 — strongest objection.** The answer could depend on the chosen
  realization of the symmetry. Item 5 handles dressing by stabilizers, and
  the fusion argument fixes the gauge freedom. A local Pauli dressing must
  commute with every generator, and the local Paulis that do are stabilizer
  products. Nonlocal dressings (logical strings or membranes) and non-Pauli
  dressings are not treated.
- **N8 — earlier claims.** Consistent with the orbit note. It answers the
  spin question that note left open.

## Verification

```bash
python3 scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py
```

Expected: `TOTAL: PASS=5 FAIL=0` (about one minute).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
