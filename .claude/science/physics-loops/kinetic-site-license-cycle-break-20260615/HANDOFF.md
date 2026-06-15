# Handoff

## Scope

This block repairs source-graph cycles, not science verdicts. On current
`origin/main`, the generated cycle inventory reports three cycles. The first
uses the edge from
`kinetic_isotropy_from_strict_license_chiral_quantization_bounded_theorem_note_2026-06-09`
to
`site_license_tick_dichotomy_all_periods_bounded_theorem_note_2026-06-11`.
After that non-authority edge is removed, the remaining two cycles share the
kinetic/tick-unitarity candidate edge and the tick-unitarity note's reverse
context/consumer edges.

## Source-side change

The kinetic note had two markdown links to the all-period site-license note:

- one in the 2026-06-15 premise-discharge candidate list;
- one in the dependency/consequence map.

Those references are downstream candidate-consumer pointers. They are not
load-bearing authorities for the kinetic note. This PR changes that
site-license note reference to plain filename text and records why the graph
edge should point the other way when the all-period note consumes the kinetic
monomial/winding-budget lemma.

The tick-unitarity note also linked back to the kinetic block and staggered
dichotomy while describing context and downstream consumers. Its actual
finite-dimensional characterization depends on the CPT identity surface and
the channel envelope, not on those consumer notes. This PR converts those
context/consumer references to plain filename text.

## Audit boundary

This PR does not edit audit verdicts, seed status, effective status, generated
audit data, or runner caches. Diagnostic generated files are restored before
commit.

## Validation

- `python3 docs/audit/scripts/build_citation_graph.py`: wrote diagnostic graph, 3452 nodes, 12962 edges.
- `python3 docs/audit/scripts/build_cycle_inventory.py`: `cycles: 0`.
- `jq '{cycle_count, cycles}' docs/audit/data/cycle_inventory.json`: `{ "cycle_count": 0, "cycles": [] }`.
- `python3 docs/audit/scripts/audit_lint.py`: OK, no errors; graph-cycle notice gone, only pre-existing notices remain.
- `git diff --check`: clean.
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main`: 0 runners under consideration, all relevant caches fresh.

Generated `docs/audit/data/citation_graph.json` and
`docs/audit/data/cycle_inventory.json` were restored before commit.
