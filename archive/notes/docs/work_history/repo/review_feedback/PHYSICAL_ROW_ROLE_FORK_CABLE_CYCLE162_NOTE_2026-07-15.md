# Physical row-role fork cable — Cycle 162

Status: parked constructive result on the single bare-metal compiler PR.

## Question

Can the retained nearest-neighbor law move and fork every physical five-bit
Pauli-row record through empty lattice space without adding a coordinate,
orientation, row value, or scheduling choice to the supplied state?

This is the first exact interface left by Cycle 161. The pivot controller can
now derive its two remote selector records from the three physical input rows,
but the selected row payloads still have to travel from their producers to the
selector-specific copy branches and then onward to common outputs.

## Result

Yes, as a finite compiler extension of the retained candidate law.

The same local straight/turn cable context used by the earlier case-role cable
works unchanged for all 32 physical row roles. The only new table entries are
the row-role outputs for those already-retained structural contexts:

- 32 row roles;
- two canonical local shapes per role: straight and turn;
- 64 canonical rows;
- 1,536 proper-cubic raw rows;
- zero overlap with the retained 89,708-row law;
- zero deterministic conflict;
- 91,244 total raw rows after the merge.

The exhaustive graph test covers all 32 row roles in all 24 proper-cubic
orientations: 768 apparatus graphs. Each graph has 36 reachable schedule
states, 60 canonical edges, one terminal history class, maximum frontier two,
and no wrong, dead, parasitic, or port write. The common source enables exactly
the two first branch writes. Deleting that source suppresses both branches for
all 32 row values.

## Bare-metal reading

This is transport, not new foundation content. A row is already a record in the
onsite alphabet. In the retained guide/frame neighborhood, an adjacent open
site can acquire the same row record. Repeating the same local relation moves
the information; exposing two adjacent destinations forks it. The row value is
not decoded, re-encoded, selected, or supplied again along the route.

Nothing in this result says that records occur, assigns occurrence weights,
defines a clock, or alters permanence. It therefore supplies no reason to edit
Admissibility, Record, a primitive, the registry, or policy.

## TOE-lane consequence

Cycle 162 closes a compiler plumbing gap shared by the quantum/matter lanes:
the physical tableau rows produced or consumed by the commutator, multiplier,
and pivot controller can now be transported and causally forked by one local,
covariant mechanism. This is necessary for an end-to-end physical pivot, but it
does not by itself complete that pivot.

The next constructive composition is exact:

1. fork and route the physical inputs `g1`, `g2`, and `P`;
2. feed routed `g2` and `g1` to the retained commuting-row multiplier;
3. route its physical `g2*g1` output;
4. let the two derived lane selectors choose the appropriate two row payloads;
5. converge each selected payload to its common recurrent output port.

Cycle 161's no-go checklist remains controlling for any proposed negative
claim about that residual. This note makes no such claim: retained constructive
routes remain and are the next target.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_row_role_transport_cycle162_2026_07_15.py
```
