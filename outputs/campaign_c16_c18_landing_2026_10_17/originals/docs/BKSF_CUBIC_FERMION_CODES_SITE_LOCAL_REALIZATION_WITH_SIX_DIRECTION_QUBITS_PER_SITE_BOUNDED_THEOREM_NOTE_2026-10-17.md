---
claim_id: bksf_cubic_fermion_codes_site_local_realization_with_six_direction_qubits_per_site_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied model: six qubits per site of Z^3, one per direction (half-edges); for an ordering of the six directions (the same at every site), generators B_v = Z on site v's six qubits, R_(v,a) = Z_(v,+a) Z_(v+e_a,-a), and plaquettes S_p = product of the four nearest-neighbour operators A_(v,a) = X_(v,+a) X_(v+e_a,-a) times Z on v's qubits ordered before +a times Z on (v+e_a)'s qubits ordered before -a. Exact: on the R code space this is the edge BKSF code of the companion notes (each edge carries one logical qubit, X = X X, Z = Z on either half), and the framework site rotation (permute sites and permute each site's six qubits as directions, Pauli labels unchanged) maps A_(v,a) of ordering o exactly to A of the rotated edge with the rotated ordering, and B and R to B and R. So the encoding intertwines the site action with the edge action. Checked (L = 4, all 60 codes; L = 6, one per orbit type): commuting, log2 code dimension 3, and the stabilizer of every code in O under the site action equals its stabilizer under the edge action (orbits 4, 6, 12). On-site Cliffords (checked for one code of each orbit type in the runner and for all 60 codes in exploration, both uniform sign sectors, L = 4): writing each site's six qubits in the code's own Jordan-Wigner order gives twelve local Majoranas mu_d = X_d Z_<d, nu_d = Y_d Z_<d with A_(v,a) = mu_{v,+a} mu_{v+e_a,-a} and Z_d = -i mu_d nu_d; a site rotation composed with an on-site signed permutation of these Majoranas maps the signed group to itself for every one of the 24 rotations, so with on-site Clifford actions each code is O-invariant and the minimal orbit four is a statement about the bare site action only. Consequently the statements of the BKSF orbit note and the bare-permutation note (fermionic charge, minimal orbit four, finite pair data and the conditional D3/single-C2 class inference under bare rotations, with D2 localization still open) hold verbatim for this site-local model with the bare site action. Not claimed: other site-local encodings, star-supported generators (the plaquette generators span four sites), dynamics, or any physical identification."
upstream_dependencies:
  - bksf_cubic_fermion_codes_are_not_rotation_invariant_minimal_orbit_four_bounded_theorem_note_2026-10-17
  - bksf_cubic_fermion_codes_bare_permutation_rotations_act_spinorially_on_the_fermion_bounded_theorem_note_2026-10-17
runner: scripts/bksf_cubic_fermion_codes_site_local_six_direction_qubit_realization_2026_10_17.py
---

# BKSF cubic fermion codes: a site-local realization with six direction qubits per site

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** SUPERSEDED for the emergent-electron lane by
`CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md`
and `CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`.
- **Why.** A fermion on the six direction positions sits on C4 axes, and so does one at the site. Under realizations that map terms to terms, its class is then trivial on C4, so this model cannot carry the spin-1/2 class.
- **What replaced it.** The lane now uses the 12 corners per site. Those notes also show that the qubit count per site is not physical for a fermion much larger than the grid.
- **What still stands.** The statements below remain valid bounded support for the stated encoding. Nothing is adopted.

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
4. **On-site Cliffords make every tested code cube-invariant (exact).**
   - Write each site's six qubits in the code's own Jordan–Wigner order.
     This gives twelve local Majoranas, mu_d = X_d Z_<d and
     nu_d = Y_d Z_<d.
   - In terms of them, A_(v,a) = mu_{v,+a} mu_{v+e_a,-a} and
     Z_d = -i mu_d nu_d. So B and R are products of local parities.
   - A site rotation composed with an on-site signed permutation of the
     twelve Majoranas maps every generator to plus or minus a generator.
   - The runner finds signs that preserve the signed group, for all 24
     rotations, in both uniform sectors, for one code of each orbit type
     (L = 4).
   - An exploration run extends this to all 60 codes, with every rotation
     and both sectors preserved (loop pack, c13,
     `majhalf_all60_L4.log`).
   - **Independent check: confirmed, and sharper.**
     - **No sign search is needed.** The sign-free choice always works:
       0 failures over 60 codes x 24 rotations x 2 sectors at L = 4 and
       L = 6, and over all 720 orderings at L = 4.
     - **An explicit form.** The map is U_R = V_R P_R, with V_R an
       on-site network of CZ gates, the same at every site, on the pairs
       of directions whose order differs between o and Ro.
     - **A genuine action.** Choices exist that form a genuine O action:
       an order-24 group with no fermion-parity twist needed.
     - **One code.** The 60 codes are a single code under on-site
       Cliffords: the CZ networks map any ordering's code to any other's.
     - **But a code-dependent action.** An action built from one ordering
       leaves only that ordering's code O-invariant.
     - **No six-qubit encoding needed.** In the edge model of the orbit
       note, the bare edge permutation followed by a vertex-centred CZ
       network also makes every code invariant. That network is local but
       not on-site, since edge qubits belong to no site.
   - So once on-site Clifford actions are allowed, the codes are
     O-invariant. "Minimal orbit four" is a statement about the bare site
     action only.
   - **Exploration: the sign-free action is spinless.** Take the sign-free
     choice mu_d -> mu_{Rd}, nu_d -> nu_{Rd}. It is a determinant-+1
     permutation of the twelve Majoranas, so it lifts to an action up to
     fermion parity.
     - Under it, plaquettes map to plaquettes exactly, so clean pair
       creators exist for every C2.
     - A clean pair test gives λ = -1, hence eta_f = +1, for all 3 axis
       C2 and all 6 edge C2. This was run for a D3 code and an order-4
       code, both sectors, L = 8 (loop pack, c13, `halfpair.log`).
     - So under this on-site action the same fermion that is spin-1/2-like
       under the bare action (companion note) is spinless. This matches
       the Majorana-per-direction code. The independent check reproduced
       this (λ = -1 for all 9 C2, every orbit type, both sectors), and
       recovered C8's +1 for the bare permutation as a calibration.
5. **Transfer.** The encoding is an isometry that intertwines the two
   actions. So the companion notes' statements hold for this site-local
   model with the bare site action:
   - a fermionic point charge;
   - no O-invariant code among these 60, with minimal orbit four;
   - the same finite pair data and conditional D3/single-C2 class inference under bare rotations, with D2 localization still open.

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

Files: `.claude/science/physics-loops/toe-campaign-20261017/c11_site_local/independent_check/` and, for
item 4, `.claude/science/physics-loops/toe-campaign-20261017/c13_onsite_clifford/independent_check/`.

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

Expected: `TOTAL: PASS=7 FAIL=0` (about three minutes).

## Load-bearing sources

- [BKSF orbit note](BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Bare-permutation note](BKSF_CUBIC_FERMION_CODES_BARE_PERMUTATION_ROTATIONS_ACT_SPINORIALLY_ON_THE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
