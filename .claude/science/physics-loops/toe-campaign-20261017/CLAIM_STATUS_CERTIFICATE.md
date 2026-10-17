# Claim status certificate

## C1
- Note: `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md`
- Runner: `scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py` (PASS=20)
- Current-surface status: bounded support, unaudited. Exact within the supplied
  hard-support stabilizer reading.
- Dependency classes: axioms (Lattice, Qubit); supplied model (stabilizer
  reading); declared choices (menu actions, Pauli conditions, star support).
- Mathematical inputs: declared four-action menu and the stated
  hopping-commutator statistics criterion; physical stabilizer and electron
  identifications remain open.
- Intended audit claim_type: bounded_theorem.
- Trace class: frontier_discovery.
- Independent check: a fresh-context agent with its own implementation
  (SU(2) lifts for signs, finite-box GF(2) linear algebra for mobility).
  Status: CONFIRMED all claims; it corrected the overall-sign statement, now fixed in the note.
- Independent audit: required before any retained use.

## C2
- Note: `docs/TWO_QUBIT_SITE_SOLDERED_SPIN_STABILIZER_RULES_THREE_DIMENSIONAL_CHARGE_MOTION_FLIPS_A_FREE_LOCAL_VARIABLE_BOUNDED_THEOREM_NOTE_2026-10-17.md`
- Runner: `scripts/two_qubit_site_soldered_spin_stabilizer_rules_charge_motion_flips_free_local_variable_2026_10_17.py` (PASS=17 with Singular)
- Current-surface status: bounded support, unaudited, exact within the
  supplied stabilizer reading. Two qubits per site is the declared M_4(C)
  enlargement.
- Independent check: confirmed. One classification statement was corrected
  (the E orbit); it is now checked by the runner.
- Intended claim_type: bounded_theorem. Trace: frontier_discovery.

## C3
- Note: `docs/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md`
- Runner: `scripts/three_axis_qubit_site_stabilizer_rules_soldering_and_three_dimensional_charge_mobility_2026_10_17.py` (PASS=10 with Singular)
- Status: bounded support, unaudited. Exact within the supplied model;
  Part B is also exact within the C4/C3 symmetry restriction.
- Independent check: Part A confirmed. Part B's counts confirmed. It found
  that the 23-, 31- and 187-orbit unions contain -1; the claims are now
  stated through the rank bound.

## C4
- Note: `docs/THREE_AXIS_QUBIT_SYMMETRIC_STABILIZER_RULES_FERMION_SEARCH_FINDS_NO_COHERENTLY_MOBILE_FERMION_BOUNDED_THEOREM_NOTE_2026-10-17.md`
- Runner: `scripts/three_axis_qubit_symmetric_stabilizer_rules_fermion_search_2026_10_17.py` (PASS=8)
- Status: bounded support, unaudited. Exact within the supplied model and
  the stated search restrictions.
- Independent check: confirmed all claims, with one count wording fixed.

## C6
- Note: `docs/BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md`
- Runner: `scripts/bksf_cubic_fermion_codes_rotation_orbits_2026_10_17.py` (PASS=8)
- Status: bounded support, unaudited. Exact for the stated family.
- Independent check: running.
- Intended claim_type: bounded_theorem. Trace: frontier_discovery. It fills
  the rotation-covariance gap recorded in the 2026-09-02 BKSF census note.
- Intended claim_type: bounded_theorem. Trace: frontier_discovery.
- Intended claim_type: bounded_theorem. Trace: frontier_discovery.
