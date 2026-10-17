---
claim_id: bksf_cubic_fermion_codes_site_local_realization_with_six_direction_qubits_per_site_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: six qubits per site of Z^3, one per direction (half-edges); for an ordering of the six directions (the same at every site), generators B_v = Z on site v's six qubits, R_(v,a) = Z_(v,+a) Z_(v+e_a,-a), and plaquettes S_p = product of the four nearest-neighbour operators A_(v,a) = X_(v,+a) X_(v+e_a,-a) times Z on v's qubits ordered before +a times Z on (v+e_a)'s qubits ordered before -a. Exact: on the R code space this is the edge BKSF code of the companion notes (each edge carries one logical qubit, X = X X, Z = Z on either half), and the framework site rotation (permute sites and permute each site's six qubits as directions, Pauli labels unchanged) maps A_(v,a) of ordering o exactly to A of the rotated edge with the rotated ordering, and B and R to B and R. So the encoding intertwines the site action with the edge action. Checked (L = 4, all 60 codes; L = 6, one per orbit type): commuting, log2 code dimension 3, and the stabilizer of every code in O under the site action equals its stabilizer under the edge action (orbits 4, 6, 12). Consequently the statements of the BKSF orbit note and the bare-permutation note (fermionic charge, minimal orbit four, the spin-1/2 class under bare rotations) hold verbatim for this site-local model with the bare site action. Not claimed: other site-local encodings, star-supported generators (the plaquette generators span four sites), dynamics, or any physical identification."
upstream_dependencies:
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
  - bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
runner: scripts/bksf_cubic_fermion_codes_site_local_six_direction_qubit_realization_2026_10_17.py
---

# BKSF cubic fermion codes: a site-local realization with six direction qubits per site

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact for the stated encoding.
Nothing is adopted.

## Question

The two BKSF notes of this campaign put one qubit on each edge of Z^3 and
rotate edges about a vertex. They flag this as outside the framework's
site-local possibility domain: the Qubit axiom attaches qubits to sites,
and the Lattice axiom rotates about sites.

Can the same codes be realized site-locally, so that the framework's own
site rotation reproduces the edge rotation exactly?

## Result

1. **Encoding.** Give each site six qubits, one per direction (half-edges).
   - The pair stabilizer R_(v,a) = Z_(v,+a) Z_(v+e_a,-a) makes each edge
     carry one logical qubit, with X = X X and Z = Z on either half.
   - The BKSF operators become:
     - B_v = Z on site v's six qubits: one site;
     - the hop A_(v,a) = X_(v,+a) X_(v+e_a,-a) times Z on v's qubits
       ordered before +a, times Z on (v+e_a)'s qubits ordered before -a: a
       nearest-neighbour pair;
     - S_p, the product of the four A around a plaquette: four sites.
   - On the R code space, this is the edge code.
2. **Exact covariance.** The framework site rotation permutes the sites
   and permutes each site's six qubits as directions; Pauli labels are
   unchanged.
   - It maps A_(v,a) of ordering o exactly to A of the rotated edge with
     the rotated ordering.
   - It maps B to B and R to R.
   - So the encoding intertwines the site action with the edge action.
3. **Checks (runner).** All 60 codes, L = 4:
   - commuting, with log2 code dimension 3 (also 3 at L = 6 for one code
     of each orbit type);
   - each code's stabilizer in O under the site action equals its
     stabilizer under the edge action;
   - orbit sizes 4, 6 and 12.
4. **Transfer.** The encoding is an isometry that intertwines the two
   actions. So the companion notes' statements hold for this site-local
   model with the bare site action:
   - a fermionic point charge;
   - no O-invariant code among these 60, with minimal orbit four;
   - the spin-1/2 fractionalization class under bare rotations.

   Three qualifications:
   - **The charge.** B_v alone is not the gauge-invariant charge here. An
     X on a single half-edge flips B_v together with an R. The charge in a
     region is the product of B_v over the region times the product of R
     on the edges inside it.
   - **The realization.** As in the companion note, the class belongs to
     the bare site action.
     - The dressing W = prod_v exp(-i pi B_v / 4) is site-local.
     - Twisted along a Z2 character of the stabilizer, it gives other
       classes: the trivial class for D3 and single-C2 codes, but not for
       the order-4 codes.
   - **The scope.** "No O-invariant code" refers to the half-edge images
     of the 60 BKSF codes only, not to six-qubit-per-site codes in
     general.

## How this bears on the lane (interpretation, not a claim)

- **The edge caveat is removed.** The emergent fermion of these notes now
  lives in a model with qubits on the framework's sites. The framework's
  own rotation is a bare permutation of sites and of each site's
  direction-labelled qubits.
- **Two extensions remain.**
  - Six qubits per site is an enlargement of the Qubit axiom, as the three
    axis qubits of the companion notes are.
  - The plaquette generators span four sites, beyond the nearest-neighbour
    star.
- **Consistent with the earlier no-gos.** The campaign's star-supported
  searches found no coherently mobile fermion. Here the fermion appears
  once the conditions include plaquettes, a slightly larger neighbourhood.

## Independent check

A fresh-context agent (same model family) wrote its own code without first
reading the runner.
- **Items 1–3: confirmed.** It found dimension 3 at L = 6 for all 60 codes,
  and covariance on 3,317,760 edge checks.
- **Item 4: confirmed directly** in the half-edge model, with phases.
- **Wording.** It asked for the three qualifications above.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c11_site_local/independent_check/`.

## Premises

- **Axioms used.** Lattice (Z^3, unit translations, proper cubic rotations
  about sites).
- **Supplied model.** The encoding above. Qubit is read as six
  direction-labelled qubits per site, a declared enlargement.
- **Declared choices.** The same ordering at every site; unsoldered Pauli
  labels.

## Relation to prior work

- BKSF: Bravyi and Kitaev, Ann. Phys. 298, 210 (2002).
- Generalized superfast encodings with qubits attached to vertices: Setia,
  Bravyi, Mezzacapo and Whitfield, PRR 1, 033033 (2019).
  - That encoding uses d/2 qubits per vertex: three per site here, half as
    many as the present encoding.
  - In it a site rotation permutes the local Majoranas, which is in
    general an on-site Clifford, not a bare qubit permutation.
  - The repetition encoding of edge qubits into half-edges is elementary.
- **New here.** The observation that the framework's site rotation acts
  exactly as the edge rotation for this encoding, so that the campaign's
  BKSF results transfer to a site-local model.

## No-Go Discipline Gate

- **N1 — routes around the claim.** Other site-local encodings, such as
  the generalized superfast encoding with three qubits per site, may have
  different symmetry. They are not treated.
- **N2/N3 — scope.** One encoding of one family.
- **N4 — inputs.** Exact GF(2) checks. The transfer in item 4 is the
  intertwining identity of item 2.
  - The runner tests the unsigned structure only.
  - The independent check tested the signed statements directly in the
    half-edge model:
    - T-junction -1 in all 60 codes;
    - sign sectors as in the edge model;
    - pair test +1 for all 108 pairs, with either sign of R;
    - control -1.
- **N5 — wording.** "Site-local" means qubits on sites. It does not mean
  star-supported generators.
- **N6/N7 — strongest objection.** The six qubits per site and the
  plaquette range are enlargements. Both are stated.
- **N8 — earlier claims.** Removes the "qubits on edges, not sites" caveat
  of the two BKSF notes. Nothing else changes.

## Verification

```bash
python3 scripts/bksf_cubic_fermion_codes_site_local_six_direction_qubit_realization_2026_10_17.py
```

Expected: `TOTAL: PASS=6 FAIL=0` (about one minute).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Bare-permutation note](BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
