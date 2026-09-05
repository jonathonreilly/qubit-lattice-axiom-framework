# Artifact plan

## Canonical claim

Claim ID: native_edge_record_local_cycle_transport_and_ledger_bounded_theorem_note_2026-09-05  
Claim type: bounded_theorem  
Current surface: conditional-support  
Audit: unset; the independent audit lane owns any verdict.

| Surface | Role |
|---|---|
| docs/NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md | Finite theorem/support note and scope boundary |
| scripts/native_edge_record_local_cycle_transport_2026_09_05.py | Primary native-edge runner |
| scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py | Independent fixed-N CAR checker |
| logs/runner-cache/native_edge_record_local_cycle_transport_2026_09_05.txt | Source-pinned primary receipt |
| logs/runner-cache/native_edge_record_local_cycle_transport_independent_check_2026_09_05.txt | Source-pinned checker receipt |
| .claude/science/physics-loops/record-matter-block06-local-cycle-20260905/ | Loop packet and handoff |

## Canonical commands

~~~text
python3 scripts/native_edge_record_local_cycle_transport_2026_09_05.py
python3 scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py
python3 scripts/cached_runner_output.py --refresh scripts/native_edge_record_local_cycle_transport_2026_09_05.py
python3 scripts/cached_runner_output.py --refresh scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py
python3 -m py_compile scripts/native_edge_record_local_cycle_transport_2026_09_05.py scripts/native_edge_record_local_cycle_transport_independent_check_2026_09_05.py
git diff --check
~~~

The primary cache also fingerprints its imported native-edge parent source
through AUDIT_INPUT_PATHS. The checker has no source imports beyond standard
scientific libraries.

No generated audit ledger, queue, status, or verdict is authored by this
block. If the citation graph is regenerated because the new note is a graph
node, only the generated citation manifest may co-land; it is inventory, not
authority.

