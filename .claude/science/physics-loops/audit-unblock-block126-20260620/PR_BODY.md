## Summary

Refreshes the canonical runner cache for
`scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py`
and carries the deterministic audit-support regeneration needed for strict-lint cleanliness.

On `origin/main`, the cache recorded `status: ok` but did not preserve useful stdout. This PR
recomputes the cache through `scripts/precompute_audit_runners.py` and records the full transcript:
`PASS = 46`, `FAIL = 0`, under the runner's declared `1800` second timeout.

The audit pipeline regeneration updates queue/ledger/effective-status support surfaces from
current source state. No audit worker was run and no verdict was hand-applied.

## Boundary

This PR does not audit the claim, apply a verdict, or assert retained/proposed-retained status.
It does not hand-edit audit ledgers, queues, publication matrices, lane registries, active review
queues, or repo-wide status boards.

The target row remains unaudited and not ready because these dependencies remain unresolved:

- `neutrino_dirac_z3_support_trichotomy_note`
- `dm_neutrino_dirac_bridge_theorem_note_2026-04-15`

## Artifacts

- `logs/runner-cache/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.txt`
- `docs/audit/data/audit_ledger.json`
- `docs/audit/data/audit_queue.json`
- `docs/audit/data/audit_packet_script_deps.json`
- rendered audit/publication effective-status surfaces from `docs/audit/scripts/run_pipeline.sh`
- `logs/runner-cache/audit_packet_script_deps.txt`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-block126-20260620/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py --check-only --push-mode none --allow-non-main` -> `fresh: 1`, all relevant caches fresh
- `bash docs/audit/scripts/run_pipeline.sh` -> pipeline complete; lint stage `OK: no errors`
- `python3 scripts/audit_packet_script_deps.py | tee logs/runner-cache/audit_packet_script_deps.txt` -> exit 0
- `python3 docs/audit/scripts/audit_lint.py --strict` -> `OK: no errors` with notices only
- `python3 -m py_compile scripts/precompute_audit_runners.py scripts/runner_cache.py scripts/frontier_dm_neutrino_source_surface_perturbative_uniqueness_theorem.py` -> OK
- `git diff --check` -> OK
