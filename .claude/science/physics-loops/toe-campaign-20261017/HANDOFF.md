# Handoff — toe-campaign-20261017

Branch `claude/toe-campaign-12h-20261017`, cut from
`claude/toe-campaign-20261016-followup` (PR #9658). Window
2026-10-16T23:40Z – 2026-10-17T11:40Z. Lane: the electron as an emergent
excitation of neighbourhood conditions (owner's direction). Nothing here is
adopted; every result is unaudited bounded support with a declared model.

## Plain-language summary (for the owner)

- **C1: the simplest "neighbourhood conditions" cannot make a moving electron.**
  - Take each site's condition to be a quantum yes/no check on its six
    neighbours, of the kind used in quantum error-correcting codes, with
    the spin turning with space as the axioms' cubic symmetry requires.
    Then there is exactly one possible rule: Chamon's.
  - Its defects cannot move on their own (fractons). Pairs can slide only
    within special planes.
  - Without the spin turning with space, the rules are classical or
    trivial, and nothing fermionic appears.
  - This mirrors last campaign's result: one qubit per site is too little
    room both for a free moving electron and for one made of neighbourhood
    conditions in this simplest form.
- **C2: a second qubit per site frees the defects, but only by leaving a trail.**
  - With two qubits per site there are rules whose defects move in all three
    directions. One example has eight kinds of defect, labelled by the
    corners of a 2x2x2 block.
  - Every such move must flip a spare local variable, a free "memory"
    qubit, so each step writes a permanent mark into the neighbourhood.
  - Rules with no spare local variables have defects that do not move in 3D.
  - Reading (not claimed): a particle that leaves a which-path trail cannot
    interfere like an electron. Here, mobility costs extra stored
    information, not less.
- **Next:** conditions that are not Pauli checks, on one qubit per site (C3),
  then block rules (C4).

## Blocks

| Block | Note | Runner | Headline |
|---|---|---|---|
| C2 | `docs/TWO_QUBIT_SITE_CUBIC_COVARIANT_STABILIZER_RULES_THREE_DIMENSIONAL_DEFECT_MOTION_WRITES_A_LOCAL_RECORD_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/two_qubit_site_cubic_covariant_stabilizer_rules_three_dimensional_motion_writes_a_record_2026_10_17.py` (PASS=17) | Two qubits per site, spin soldered: record-free operators never move a charge in 3D, so rules without free local variables have no 3D-mobile defect; the example rule has 8 even-step-mobile charges whose moves flip a flavour variable. |
| C1 | `docs/ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md` | `scripts/cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17.py` (PASS=20) | Soldered: Chamon only, with fracton defects (no 3D mobility; planons in planes normal to body diagonals). Unsoldered: classical or cluster rules. No 3D-mobile fermionic defect in the class. |

## Open obligations
- C1 and C2 independent checks: done. C1 is fully confirmed (sign wording corrected). C2 is confirmed except one classification statement, which was corrected.
- C3 onwards in OPPORTUNITY_QUEUE.
- C2–C5 in OPPORTUNITY_QUEUE.

## Next decision
- Start C3: non-Pauli covariant commuting projectors on one qubit per site.
