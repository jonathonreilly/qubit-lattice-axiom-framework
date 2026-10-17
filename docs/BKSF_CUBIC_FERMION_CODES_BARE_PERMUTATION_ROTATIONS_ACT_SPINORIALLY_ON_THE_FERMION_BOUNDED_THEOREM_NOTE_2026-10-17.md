---
claim_id: bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: the 60 translation-invariant BKSF stabilizer codes on the cubic lattice (one qubit per edge of Z^3, one ordering of the six edge directions at every vertex) of the companion orbit note, with signed plaquette generators, one sign per plaquette orientation (8 translation-invariant sign sectors). Exact on the L = 4 torus (Pauli algebra with phases): all 8 sectors of all 60 codes are valid; in two sectors the hop product of a fixed ordering's edge operators around every plaquette is +, respectively -, the signed generator (flux 0 and flux pi; this labels the sectors); every rotation in each code's stabilizer maps the signed group of those two sectors to itself as a bare qubit permutation P_R, while in each of the 6 mixed sectors 44 codes have a stabilizing rotation that needs a sign correction. Pair test, exact: for 72 of the 108 (code, C2) pairs (all three edge C2 of every D3 code, one edge C2 of each order-4 code, the edge C2 of 24 of the 36 single-C2 codes) there is an ordering whose plaquette span P_R preserves, and in both sectors the state with fermions at x and Rx has P_R-eigenvalue +1 relative to the vacuum for every tested off-axis x (control: +1 for the bosonic toric-code charge). With exchange sign -1 this gives eta_f(C2, C2) = -1 under P_R: the bare permutation acts on the emergent fermion spinorially, C2^2 = (-1)^F. The realization P_R W with W = prod_v exp(-i pi B_v / 4) (a function of the stabilizers, constant on the code space) gives +1, so the class belongs to the realization, not to the code alone. Not claimed: the 36 remaining pairs, C3 (no Z2 class), sign patterns that are not translation-invariant, the mixed sectors, other encodings, dynamics, the continuum limit, or any physical identification (electron, spin)."
upstream_dependencies:
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
runner: scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py
---

# BKSF cubic fermion codes: bare-permutation rotations act spinorially on the fermion

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact on the L = 4 torus for the
stated family; an independent check reproduced it at L = 6. Nothing is
adopted.

## Question

The companion orbit note showed two things about the translation-invariant
BKSF codes:
- each carries a fermionic point charge;
- each is fixed by a subgroup of the cubic rotations: D3, a group of order
  4, or a single C2.

An electron is a spin-1/2 fermion: a 2 pi rotation acts on it as -1. The
lattice version of this question is symmetry fractionalization. For a C2 in
the code's stabilizer, is eta_f(C2, C2) = -1, i.e. does C2^2 act on the
fermion as fermion parity?

The answer depends on how the rotation is realized on the qubits. The
framework's Lattice axiom lets rotations act by moving sites, so the natural
realization is the bare qubit permutation P_R. This note asks the question
for P_R.

## Result

1. **Sign sectors (exact).** Give the plaquette generator normal to axis c
   the sign (-1)^{s_c}. All 8 translation-invariant sectors of all 60 codes
   are valid stabilizer groups.
2. **Flux labels.** For a fixed ordering, the hop product
   A(v,b) A(v+b,a) A(v+a,b) A(v,a) around a plaquette is plus or minus the
   generator. So one uniform sector is the flux-0 sector and one is the
   flux-pi sector; this is a labelling, true by construction.
3. **Bare permutations (exact).** In the flux-0 and flux-pi sectors, every
   rotation in each code's stabilizer maps the signed group to itself as a
   bare qubit permutation P_R, with no sign correction.
   - As a control, in each of the 6 mixed sectors, 44 codes have a
     stabilizing rotation whose bare permutation needs a correction.
   - The independent check gives the reason: P_R A^o_e P_R^-1 = A^{Ro}_{Re}
     exactly, and the two uniform signed groups do not depend on which
     ordering in the class is used.
4. **Pair test (exact).** Let R be a C2 in the code's stabilizer and x an
   off-axis vertex. Let S be the product of a fixed ordering's edge
   operators along a path from x to Rx.
   - Then P_R S|vac> = S (S^dagger S^R) P_R|vac>. The product S^dagger S^R
     is plus or minus an element of the signed group, and lambda is that
     sign. So lambda is the eigenvalue of P_R on the pair state relative
     to the vacuum.
   - This needs an ordering o in the class whose plaquette span is
     preserved by P_R. Such an ordering exists for 72 of the 108
     (code, C2) pairs:
     - all three edge C2 of each D3 code;
     - one edge C2 of each order-4 code;
     - the edge C2 of 24 of the 36 single-C2 codes.
   - For the remaining 36 pairs, P_R maps bare hops to flux-dressed hops
     for every ordering, and lambda is not determined here.
   - In all 72 pairs, in both sectors and for every tested x, lambda = +1.
   - Control: in the untwisted toric code (bosonic charge), lambda = +1.
5. **Spinorial action (from 4).** For a pair swapped by C2,
   lambda = theta_f eta_f(C2, C2).
   - The independent check calibrated this relation: a boson gives +1, a
     boson in pi background flux gives -1 for axes through perpendicular
     plaquettes (the Aharonov–Bohm effect), and a scalar fermion with
     c_v -> c_{Rv} gives -1.
   - With theta_f = -1 it gives eta_f(C2, C2) = -1 under P_R. So C2^2 acts
     on the emergent fermion as (-1)^F, the spin-1/2 behaviour.
   - The independent check also derived this from the Majorana form: P_R
     maps A_e to plus or minus A_{Re} B_tail B_head (times plaquettes), so
     the encoded fermion goes as c_v -> -i s_v c_{Rv}.
6. **The class belongs to the realization.**
   - Let W = prod_v exp(-i pi B_v / 4). It is a function of the
     stabilizers, so it is constant on the code space. On a state with
     n fermions it contributes a relative phase e^{i pi n / 2}.
   - P_R W is therefore also a realization of R, and it flips lambda, so
     eta_f = +1. It is the scalar rotation c_v -> c_{Rv}.
   - Within one realization, dressing by stabilizer products cannot change
     the class: f x f = 1 fixes the gauge freedom to nu_f = +-1, and
     (F P_R)^2 is constant for a Pauli dressing F that respects the group
     law.

## How this bears on the lane (interpretation, not a claim)

- **Spin from moving sites.** If the framework's rotations act on the
  qubits by moving them, with no extra local unitary, then in these codes
  the emergent fermion is spinorial. A half-turn applied twice gives the
  fermion parity, as for a spin-1/2 particle. Here the lattice supplies the
  "electron spin" sign without any spin degree of freedom being put in.
- **Two caveats.**
  - The dressed realization P_R W gives the scalar answer. Which one is
    physical depends on the dynamics.
    - The bare permutation is not a symmetry of Majorana hopping
      sum t_e A_e built from one ordering's edge operators; P_R W is.
    - With number-conserving hopping both are symmetries, and they differ
      by e^{i pi N / 2}.
    - So the spinorial answer is tied to the bare-permutation reading of
      the Lattice axiom, not forced by the code.
  - The hop system of a fixed ordering is less symmetric than the code.
    - For every ordering of a D3 code, P_R preserves span(S^o) only for the
      identity and one edge C2.
    - Even there, P_R maps a hop to a hop times the endpoint vertex terms.
    - A follow-up search (loop pack, c9) finds D3-invariant flux
      conventions of the form S^o_p times corner vertex terms. Whether they
      support D3-symmetric clean hops is open.
- **Pi-flux sector.** For complex (number-conserving) hopping with pi flux
  per plaquette, the low-energy theory is the Kogut–Susskind staggered
  fermion: two four-component Dirac tastes. The independent check confirms
  2 nodes, each with 4 linearly crossing bands. For the Majorana hopping
  sum A_e, the two nodes are particle-hole partners: one Dirac fermion.

## Independent check

A fresh-context agent (same model family) wrote its own code without
reading the runner. Its verdicts:
- **Items 1–4: confirmed**, at L = 4 and L = 6.
- **Earlier wording: refuted, and corrected here.** It refuted the earlier
  version of this note, which claimed eta_f(C2, C2) = +1 under P_R by
  restricting P_R to a region around the fixed vertex. That restriction
  breaks the generators straddling the region's boundary, so it is not a
  valid localization of the symmetry.
- **The current claim.** Its pair test (with calibrations), its Majorana
  derivation and the W-dressing result are the basis of items 4–6. This
  note's runner reproduces the pair test with independent code.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c8_rotation_action/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, proper cubic rotations about a vertex).
- **Supplied model.** The BKSF codes of the companion orbit note, with
  signed plaquette generators. The qubits sit on edges, not on sites.
- **Declared choices.**
  - Translation-invariant signs.
  - The bare-permutation realization of the rotations.
  - The relation lambda = theta_f eta_f, calibrated as above.

## Relation to prior work

- BKSF: Bravyi and Kitaev, Ann. Phys. 298, 210 (2002). Statistics: Levin and
  Wen, PRB 67, 245316 (2003).
- Symmetry fractionalization and its gauge freedom: Barkeshli, Bonderson,
  Cheng and Wang, PRB 100, 115147 (2019). This is a 2+1D framework, used here
  for point particles.
- Staggered fermions: Kogut and Susskind, PRD 11, 395 (1975); Susskind,
  PRD 16, 3031 (1977); Golterman and Smit, Nucl. Phys. B245, 61 (1984);
  Golterman, lecture notes arXiv:2406.02906. Symmetries of Hamiltonian
  staggered fermions, including a twisted rotation group: Catterall,
  Pradhan and Samlodia, PRD 113, 014504 (2026), arXiv:2501.10862.
- Emergent fermions from string nets: Wen, PRD 68, 065003 (2003).
- **New here.**
  - The sign-sector and pair-test analysis of the bare-permutation rotation
    action in the cubic BKSF family.
  - The finding that this action is spinorial, while a stabilizer-function
    dressing makes it scalar.

## No-Go Discipline Gate

- **N1 — routes around the claim.** Not covered:
  - the 36 pairs with no span-preserving ordering;
  - realizations other than P_R and P_R W;
  - sign patterns that are not translation-invariant;
  - the mixed sectors;
  - other encodings;
  - stacks.
- **N2/N3 — scope.** One family, two sectors, one Z2 class per covered
  (code, C2) pair.
- **N4 — inputs.** Exact Pauli algebra with phases on the L = 4 torus. The
  pair paths lie within a box of side 2 around the origin, so the loops
  S^dagger S^R are contractible. The relation lambda = theta_f eta_f is an
  input, calibrated by the independent check.
- **N5 — wording.** "Spinorial" means eta_f(C2, C2) = -1 for the stated
  realization. It does not mean an emergent SU(2) spin.
- **N6/N7 — strongest objection.** The class depends on the realization.
  This is stated in item 6, and the interpretation does not treat the
  spinorial answer as forced.
- **N8 — earlier claims.** This replaces this note's own first version,
  which had the opposite sign. It is consistent with the orbit note.

## Verification

```bash
python3 scripts/bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17.py
```

Expected: `TOTAL: PASS=7 FAIL=0` (about 1.5 minutes).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
