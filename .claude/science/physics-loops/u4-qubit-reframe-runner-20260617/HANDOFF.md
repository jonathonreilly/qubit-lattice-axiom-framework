# Handoff

This PR unlocks the critical U4 qubit-reframe row:

- `claim_id`: `u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20`
- queue on `origin/main`: critical, `runner_path: null`,
  `transitive_descendants: 1057`, load 16.047
- runner: `scripts/frontier_u4_qubit_reframe_closure.py`
- result: PASS=15 FAIL=0

The note now cites the current `MINIMAL_AXIOMS_2026-06-05.md` Quantum axiom as
the load-bearing framework source. The runner proves the Pauli/M2(C)/Cl(3,0)
local carrier directly with matrix units and real-span rank.

No audit result, audit ledger row, publication table, active review queue,
front-door status file, canonical harness, lane registry, or lane status board
is edited. Independent audit remains required.

Verification to rerun:

```bash
python3 scripts/frontier_u4_qubit_reframe_closure.py
python3 scripts/cached_runner_output.py scripts/frontier_u4_qubit_reframe_closure.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_u4_qubit_reframe_closure.py --check-only
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/frontier_u4_qubit_reframe_closure.py scripts/cached_runner_output.py docs/audit/scripts/build_citation_graph.py
```

