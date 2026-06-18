## Summary

Source-side cycle-edge repair for `koide_q_reduced_carrier_physical_identification_obstruction_note_2026-06-12`.

The current audit queue reports a 2-node Koide Q-reduced cycle and says the obstruction note's citation back to `koide_q_reduced_observable_restriction_theorem_2026-04-22` should be informational/see-also, not load-bearing. This PR rewrites that parent reference as context-only claim-id text and removes the markdown dependency edge back to the parent note.

## Trace

- Loop handoff: `.claude/science/physics-loops/koide-q-reduced-cycle-edge-20260618/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/koide-q-reduced-cycle-edge-20260618/TRACE_GATE.md`
- Claim certificate: `.claude/science/physics-loops/koide-q-reduced-cycle-edge-20260618/CLAIM_STATUS_CERTIFICATE.md`
- Target blocker: `cycle_break_required` source-graph repair for the Koide Q-reduced 2-node cycle

## Boundaries

- No audit ledger, queue, dispatch, publication status, front-door, active-review, registry, or lane-board files edited.
- No audit-loop run.
- No audit verdict or effective status claimed.
- The physical charged-lepton reduced-carrier/readout theorem remains open.
- The `D_red = I_2` physical source-unit normalization remains open.

## Verification

- `python3 scripts/koide_q_reduced_cycle_edge_hygiene_2026_06_18.py` -> `TOTAL: PASS=10 FAIL=0`
- `python3 -m py_compile scripts/koide_q_reduced_cycle_edge_hygiene_2026_06_18.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/koide_q_reduced_cycle_edge_hygiene_2026_06_18.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/koide_q_reduced_cycle_edge_hygiene_2026_06_18.py`
- `git diff --check`
