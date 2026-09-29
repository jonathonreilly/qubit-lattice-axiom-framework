---
claim_id: the_owners_frozen_box_reading_under_nearest_neighbour_formation_rules_a_sealed_box_freezes_into_one_state_or_into_a_number_of_states_growing_with_its_volume_not_its_area_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "A supplied formalisation, not adopted, of the owner's reading (records form where the neighbourhood allows; a sealed box's record count rises until frozen; frozen = black hole). Sealed L^d boxes of Z^d (d = 2, 3); at most one record per site; records permanent; an empty site may form a record iff its number k of recorded nearest neighbours lies in an allowed set A; monotone growth; frozen when no empty site has k in A; entropy ln N with N the number of distinct frozen configurations reachable from the empty box. (A) Upward-closed rules (A = {m, ..., 2d}): the frozen state from any start is unique (checked for every m on 5^2 and 3^3 boxes with random starts and orders); from the empty box it is the full box if 0 is in A, else the empty box. (B) Crowding rules (A = {0, ..., m}, m < 2d): reachable iff the recorded set is m-degenerate, frozen iff every empty site has more than m recorded neighbours; exact counts on 2D boxes L = 2..5 and 3D boxes L = 2, 3 show ln N per site roughly constant (2D m = 0, 1: change < 0.03 between L = 4 and 5) and ln N per boundary unit growing with L for every m tested. (C) With the lattice at the Planck length (the scale primitive) and a black hole whose horizon area equals the box's surface (S_BH = 6 L^2/4 in 3D), a frozen box with ln N ~ c L^3 exceeds S_BH beyond L* = 1.5/c, a few lattice spacings (c = 0.23 to 0.48 at L = 3). Pre-registered outcome FAIL. Not shown: rules that are neither crowding nor upward-closed; sizes beyond those enumerated; stochastic weights; any quantum dynamics; boundary-entanglement entropy (main's area-law lane)."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
runner: scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py
---

# The owner's frozen-box reading: under nearest-neighbour formation rules a sealed box freezes into one state, or into a number of states growing with its volume, not its area

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** exact enumeration on small boxes; pre-registered; unaudited.
Independent checks are recorded below.

## In one paragraph

The owner's reading, recorded in this PR and not adopted:
- records form where their neighbourhood allows;
- in a sealed box the number of records rises until nothing more can form;
- a box frozen that way is a black hole.

A black hole has a definite entropy, the count of its possible inner
states, and that entropy grows with the area of its surface, not with its
volume.

This probe counts the ways a sealed box can end up frozen, under the
simplest neighbourhood rules. Two cases cover every rule tested:
- If more recorded neighbours never stop a record forming, the box always
  ends in the same frozen state: one state, entropy zero.
- If crowding stops records forming, the number of frozen states grows with
  the volume.

Neither grows with the surface. With the lattice at the Planck length, a
frozen box of the second kind larger than a few lattice spacings would
carry more entropy than a black hole of its size could.

So under these rules the reading needs something extra to match a black
hole's entropy. For example, the frozen interior could be fixed by the
surface. Or the relevant entropy could be something other than the count of
frozen interiors.

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (the reading survives this test)** if some tested rule gives
  ln N growing like the boundary, L^(d−1).
- **FAIL** if every tested rule gives a unique frozen state or ln N growing
  like the volume, L^d.
- Also recorded: upward-closed rules give a unique frozen state.

**Outcome: FAIL.**

## Prior art

On main:
- **The black-hole entropy lane:** the area-law notes, the conditional
  Bekenstein-bound theorem, and the finite-lattice BH-entropy companion
  (an open gate). It studies entanglement entropy across a boundary, which
  follows an area law. That is a different quantity from the count of
  frozen interiors, and this note does not test it.
- **The scale primitive:** the lattice spacing is the Planck length.

Of this PR:
- probe 7, on the record count under a unitary wave;
- the owner's reading, recorded in the map;
- the gravity-lane panel's condensed-matter lens, which proposed this test.

External, reference only: random sequential adsorption; bootstrap
percolation, which is order-independent; the known exponential growth of
the number of maximal independent sets of grid graphs.

## Premises (supplied)

- **Box.** A sealed L^d box of Z^d, with d = 2 or 3. Neighbours outside the
  box count as unrecorded.
- **Records.** At most one per site, and permanent.
- **Formation rule.** An empty site may form a record iff its number k of
  recorded nearest neighbours lies in an allowed set A. This is the
  Admissibility wording "odds set by nearest-neighbour conditions", with the
  odds reduced to allowed or not.
- **Frozen.** No empty site has k in A.
- **Entropy.** ln N, where N is the number of distinct frozen configurations
  reachable from the empty box.

## A — upward-closed rules: one frozen state (check A)

- If A = {m, …, 2d}, then more recorded neighbours never forbid a record.
  Growth is then a closure, and its end state does not depend on the order
  of events. This is bootstrap percolation.
- Checked for every m on 5² and 3³ boxes, from 6 random starts with 5
  random orders each.
- From the empty box, the end state is the full box if 0 ∈ A, and the empty
  box otherwise. The entropy is 0.

## B — crowding rules: counts grow with the volume (check B)

With A = {0, …, m} and m < 2d (a record forms only if at most m neighbours
are recorded):
- a configuration is reachable iff its recorded set can be peeled away
  site by site, each site having at most m recorded neighbours when removed
  (m-degenerate);
- it is frozen iff every empty site has more than m recorded neighbours.

Exact counts, by backtracking:

| d | m | N for L = 2, 3, 4, 5 (2D) or L = 2, 3 (3D) | ln N per site | ln N per boundary unit |
| --- | --- | --- | --- | --- |
| 2 | 0 | 2, 10, 42, 358 | 0.17, 0.26, 0.23, 0.24 | 0.35, 0.77, 0.93, 1.18 |
| 2 | 1 | 6, 57, 1699, 144205 | 0.45, 0.45, 0.47, 0.48 | 0.90, 1.35, 1.86, 2.38 |
| 2 | 2 | 1, 17, 305, 22398 | 0, 0.31, 0.36, 0.40 | 0, 0.94, 1.43, 2.00 |
| 2 | 3 | 1, 2, 7, 63 | 0, 0.08, 0.12, 0.17 | 0, 0.23, 0.49, 0.83 |
| 3 | 0 | 6, 496 | 0.22, 0.23 | 0.45, 0.69 |
| 3 | 1 | 40, 379531 | 0.46, 0.48 | 0.92, 1.43 |
| 3 | 2 | 34, 413615 | 0.44, 0.48 | 0.88, 1.44 |
| 3 | 3 | 1, 12274 | 0, 0.35 | 0, 1.05 |
| 3 | 4 | 1, 65 | 0, 0.15 | 0, 0.46 |
| 3 | 5 | 1, 2 | 0, 0.03 | 0, 0.08 |

- The entropy per site settles, while the entropy per boundary unit keeps
  growing, in every row where the sizes resolve it.
- Rules with larger m freeze late, so on these small boxes the boundary
  suppresses their counts. Their per-site entropy is still rising at the
  largest size.

## C — against a black hole of the box's size (check C)

- Put the lattice at the Planck length (the scale primitive). Take a black
  hole whose horizon area equals the box's surface, so S_BH = 6L²/4 in 3D.
- A frozen box with ln N ≈ cL³ exceeds S_BH beyond L* = 1.5/c.
- At L = 3, c is 0.23, 0.48 and 0.48 for m = 0, 1 and 2, giving L* ≈ 6.5,
  3.2 and 3.1 lattice spacings.
- A different choice of the comparison black hole changes L* by an O(1)
  factor, not the conclusion.

## What this means

Under the nearest-neighbour formation rules tested, a sealed box that
freezes has either no freedom (one frozen state) or freedom in its bulk (a
number of frozen states growing with its volume). A black hole's entropy
grows with its area. So "frozen box = black hole" does not follow from
these rules.

For it to hold, one of these is needed:
- the frozen interior is fixed by the surface (only surface choices are
  free);
- the black-hole entropy is a different quantity, such as the entanglement
  across the surface, which is what main's area-law lane studies;
- the rules are of a kind not tested here.

This is the owner's reading; nothing is adopted. The test only says what
the reading would need in order to meet black-hole entropy.

## No-Go Discipline Gate

The bounded negative claim: for the tested rule families and sizes, no rule
gives a frozen-state count growing with the boundary.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *An upward-closed rule with many frozen states.* ATTEMPTED (A): the
     closure is unique. Fails.
  2. *A crowding rule whose count grows with the boundary.* ATTEMPTED (B:
     every m < 2d in 2D and 3D). The counts grow with the volume. Fails at
     the enumerated sizes.
  3. *Boundary-dominated counts at larger m.* ATTEMPTED (B): the per-boundary
     entropy grows with L for every m. Fails at the enumerated sizes.
  4. *A different comparison black hole.* ATTEMPTED (C): only L* moves.
  5. *Seeds or other starting states.* ATTEMPTED (A) for upward-closed
     rules: unique from any start. Not tested for crowding rules from
     non-empty starts.

  **Open routes:**
  - (i) rules neither crowding nor upward-closed;
  - (ii) larger sizes;
  - (iii) stochastic weights and quantum dynamics;
  - (iv) boundary-entanglement entropy.
- **N2 — pairwise table, with directions.**
  - W1: nearest-neighbour count rules.
  - W2: monotone, permanent records.
  - W3: counting reachable frozen configurations as the entropy.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: count rules can allow removal | no: monotone rules need not be count rules | independent |
  | W1, W3 | no | no | independent |
  | W2, W3 | no | no: W3 is an identification choice | independent |

- **N3 — hidden-wall scan.**
  - "sealed": explicit (outside counts as unrecorded).
  - "entropy = ln N": explicit, as W3.
  - "Planck length": the scale primitive, a registered units conversion.
- **N4 — residual matching.**

  | Citation | Residual attacked | Status here | Match |
  | --- | --- | --- | --- |
  | docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md, "What This Declares" | the lattice spacing in Planck units | used in C | yes |

- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "volume, not area" | each counted configuration checked | the rule at every site, including the boundary | not applicable | all boxes enumerated | not executed beyond the enumerated sizes |

- **N6 — primitive scan.** The scale primitive is used as a units
  conversion only. No other primitive is invoked.
- **N7 — steelman, in a hostile reviewer's voice.** "The owner's reading
  may mean that a black hole's entropy is the information across its
  surface, not the number of possible frozen interiors. Main's area-law
  lane studies exactly that. The count here would then be the wrong
  quantity. Also, larger m freezes late, and small boxes cannot settle the
  scaling for m ≥ 2." Partly convincing. So the claim is restricted to the
  count of frozen interiors at the enumerated sizes.
- **N8 — cross-cycle echo.**
  - Probe 7 (a record count that never falls never rises): about a unitary
    wave, not formation rules. It is not a wall here.
  - Main's area-law lane: a different quantity, not tested.
- **Outcome.** PASS as scoped. The pre-registered outcome is FAIL.

## Independent checks

Pending.

## Reproduction

`python3 scripts/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.py`
prints 3 checks, the N5 lines and TOTAL, in about 2 minutes. The canonical
cache is at
logs/runner-cache/the_owners_frozen_box_reading_counts_of_frozen_record_configurations_2026_09_29.txt.
