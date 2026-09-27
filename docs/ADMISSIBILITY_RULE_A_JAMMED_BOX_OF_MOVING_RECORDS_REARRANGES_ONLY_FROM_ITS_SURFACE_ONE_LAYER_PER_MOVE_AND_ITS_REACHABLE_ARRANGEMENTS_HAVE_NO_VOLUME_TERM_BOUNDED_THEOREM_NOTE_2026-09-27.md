---
claim_id: admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_one_layer_per_move_and_its_reachable_arrangements_have_no_volume_term_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 39's pair-weight transit as landed (a bond with exactly one occupied end is visited, and the record moves to the empty end with positive probability), for the full L x L x L box of aligned records in empty space, with no formation, counting arrangements first reached after T single moves: (T1) a record at graph distance d from the outside can first leave its site at move d and not earlier, so the movable set grows by one layer per move; (T2) N_1 = 6L^2 and N_2 = 18L^4 + 33L^2 - 24L for every L >= 2, of which C(6L^2, 2) - 12L have two displaced records and 36L^2 - 12L have one; (T3) the arrangements with T displaced records are exactly the sets of T outward moves by distinct surface records, numbering [x^T](1+x)^(6(L-2)^2)(1+2x)^(12(L-2))(1+3x)^8, and N_T = (6L^2)^T/T! + O(L^(2T-2)) with no L^(2T-1) term. A harvest of probe #8992 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9349, Grok). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_2026_09_27.py
---

# A jammed box of moving records rearranges only from its surface, one layer per move, and its reachable arrangements have no volume term

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 39's transit as landed; a harvest of probe #8992, confirmed by an other-family referee in #9349; nothing adopted or registered; unaudited)

This note works within block 39 as landed on main (records that move to empty neighbouring sites with positive probability) and counts how a jammed box of aligned records can rearrange; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 127 (landed) counted what a jammed box of moving records loses in one move: `6L²` bonds to the outside. This note, a harvest of a probe result another model family has confirmed, counts what the box can become in more moves.

- **T1: one layer per move.** A record at distance `d` from the outside can first move at move `d`, and not before. So the jam loosens one layer at a time.
- **T2: two moves, exactly.** The arrangements first reached after two moves number `18L⁴ + 33L² − 24L`.
- **T3: every number of moves, at leading order.** The arrangements first reached after `T` moves number `(6L²)^T/T! + O(L^{2T−2})`: the surface's one-move count to the `T`-th power, over `T!`. There is no term of order `L^{2T−1}`, and no volume term.

In plain terms: a solid block of records can only change at its skin. Each move peels at most one more layer, and the ways the block can have changed after a few moves are essentially the ways of choosing which surface records stepped outward.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-27.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The transit and the jammed box are supplied clauses. Nothing is adopted.
- **Block 39 (landed on main).** Pair-weight transit: "A bond with exactly one occupied end is visited" (quoted, A3). The record moves to the empty end with positive probability. So an arrangement is reachable in `T` moves iff `T` single moves of records to empty neighbouring sites produce it.
- **The jammed box.** The full `L × L × L` box of aligned records in empty space. Records carry equal contents, so an arrangement is its set of occupied sites. There is no formation.

## Domain qualifications

- Boxes only. Faceted shapes, where one outside site touches several surface sites, change the leading coefficient.
- Reachability in moves; in continuous time any finite sequence of moves has positive probability in any positive time.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — one layer per move

*Statement.* Let `δ₀(x)` be the graph distance from `x` to the outside. A record at `x` can first leave its site at move `δ₀(x)`, and not earlier. The sites vacated within `t` moves are exactly those with `δ₀ ≤ t`.

*Proof.*
- One move changes the empty set by one site, so the distance from `x` to the nearest empty site falls by at most 1 per move. A record moves only when that distance is 1.
- Conversely, walk a vacancy inward along a shortest path.
- The runner checks the vacated sets exactly for `L = 2, 3, 4` (`t ≤ 3`) and `L = 5` (`t ≤ 2`) (B1). ∎

## Theorem T2 — two moves, exactly

*Statement.* For every `L ≥ 2`, `N₁ = 6L²` and `N₂ = 18L⁴ + 33L² − 24L`. Of the two-move arrangements, `C(6L², 2) − 12L` have two displaced records and `36L² − 12L` have one.

*Proof.*
- **Two displaced records.** Each move must take an unmoved surface record outward. Each outside site touches one box site, so the targets determine the movers. The count is `C(6L², 2) − Σ_r C(m_r, 2) = C(6L², 2) − 12L`, with `m_r = 1, 2, 3` outward moves for face, edge and corner records.
- **One displaced record.** It is decided within distance 3 of the mover. For `L ≥ 7` the count is therefore a polynomial of degree at most 2 in `L`, and the values at `L = 7, 8, 9` fix it as `36L² − 12L`.
- The runner enumerates all arrangements exactly for `L = 2` to `9` (C1). ∎

## Theorem T3 — every number of moves, at leading order

*Statement.*
- The arrangements with `T` displaced records are exactly the sets of `T` outward moves by distinct surface records. They number `[x^T](1 + x)^{6(L−2)²}(1 + 2x)^{12(L−2)}(1 + 3x)⁸`: face, edge and corner records.
- All other arrangements first reached at move `T` number `O(L^{2T−2})`.
- Hence `N_T = (6L²)^T/T! + O(L^{2T−2})`, with no `L^{2T−1}` term.

*Proof.*
- As in T2, each of the `T` moves takes a new surface record outward. The coefficient counts the choices, at most one outward move per record.
- The other arrangements have at most `T − 1` displaced records, and there are `O(L^{2(T−1)})` of them.
- The runner checks the three-displaced count against the coefficient for `L = 2, 3, 4` (all arrangements at move 3: 4184, 38394, 189128). It also checks, for `T = 1` to `5`, that the coefficient is a polynomial of degree `2T` in `L` with leading term `6^T L^{2T}/T!` and no `L^{2T−1}` term (D1). ∎

## What this settles and what it does not

- **Settled.** Within block 39's transit, a jammed box changes only at its surface. The count of what it can become in `T` moves has no volume term at any order computed.
- **For landed block 127.** This extends its one-move count to every number of moves.
- **Not settled.**
  - Faceted shapes.
  - The exact polynomial for three moves.
  - Formation.
  - The dynamics' weights; only reachability is counted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 127 as landed: the one-move census of a jammed box; the task moving-jammed-clusters (a): arrangements reachable in T > 1 moves"
source_of_blocker_text: probes task J:derive:moving-jammed-clusters
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "faceted shapes; the exact three-move polynomial; weights of the dynamics"
conditional_surface_status: "exact counts for the box under block 39's transit, reachability only"
hypothetical_axiom_status: "the transit and the jammed box are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.** Block 39 (landed): the transit. Block 127 (landed): the one-move census and the box's evaporation per bond, a harvest of attempt a2 of the same task.
- **Probes.**
  - #8992, worker `w-macbookpro9927a-j4ba6`, Claude Opus 5.5, the supervisor's own model family, found T1–T3.
  - #9349, worker `w-macbookpro90c72-j6adb`, `grok-4.6`, another model family, refereed #8992 with its own checker. It confirmed `6L²`, `18L⁴ + 33L² − 24L` for `L = 2..5`, the split, the depth law, the three-move counts for `L = 2, 3, 4`, and the generating function's leading behaviour.
- **In the literature.** Counting reachable configurations of exclusion processes from a jammed state is combinatorics of the standard kind. No result is imported.
- **New here.**
  - The harvest.
  - A new exact runner with its own enumeration, which extends the two-move check to `L = 9`.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: what a jammed box can become in `T` moves. The obligations are:
- (O1) the premises (A3);
- (O2) the depth law (B1);
- (O3) two moves (C1);
- (O4) every number of moves at leading order (D1).

## No-Go Discipline Gate

The note's negative sentence: no record deeper than `t` in the box can have moved within `t` moves.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A shortcut through the interior.* The distance to the nearest vacancy falls by at most 1 per move (T1). ATTEMPTED.
2. *Interior moves add volume terms.* They are `O(L^{2T−2})` (T3). ATTEMPTED.

Scope left open: faceted shapes; the dynamics' weights.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The box, the aligned contents and reachability in moves are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 39 (landed) | the transit | yes (quoted, A3) |
| block 127 (landed) | the one-move census | placement |
| probe #8992 and referee #9349 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "one layer per move; `N₂` exactly; `N_T` at leading order" | executed: single moves | executed: the depth law for `L` up to 5 | executed: the two-move census to `L = 9` | executed: three moves to `L = 4`; the generating function to `T = 5` | not executed: faceted shapes; formation |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Only counts, no physics."
  - *Reply:* The count shows the jam's changes live on its surface at every order computed. That is the fact block 127's evaporation rate needs beyond one move.

### N8 — Cross-cycle echo
- Block 127: one move.
- This note: every number of moves, at leading order.

## Falsifiers

- An arrangement first reached in two moves outside the stated count for some `L ≥ 2`.
- A record at distance `d` that moves before move `d`.

## Boundaries and non-claims

- The box; aligned contents; reachability only.
- The transit and the box are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 39 (landed), quoted. Block 127 (landed), placed.
- Named standard imports, at definition level:
  - breadth-first enumeration;
  - generating functions;
  - exact integer and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - Probe #8992 (Claude Opus 5.5) was refereed by #9349 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner with its own enumeration.
- **Before writing.** Origin was re-fetched. Block 39 was read as landed. The own prior-art check covered memory (block 127 harvested a2 of this task), the held branches, open PRs and main.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_2026_09_27.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
