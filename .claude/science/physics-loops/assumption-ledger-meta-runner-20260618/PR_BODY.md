## Summary

Registers and hardens the existing meta-firewall runner for the critical
`assumption_derivation_ledger` row.

Current `origin/main` has `docs/ASSUMPTION_DERIVATION_LEDGER.md`,
`scripts/assumption_derivation_ledger_meta_check.py`, and a runner cache, but
the audit ledger row still has `runner_path: null`. This PR makes the source
registration explicit and strengthens the runner so the row has mechanical
evidence for its metadata-only boundary.

## Trace gate

- trace_class: methodology
- target_claim_id: `assumption_derivation_ledger`
- reachability: supports audit handling by providing an explicit primary runner
- artifact_role: runner_certificate
- handoff: `.claude/science/physics-loops/assumption-ledger-meta-runner-20260618/HANDOFF.md`
- certificate: `.claude/science/physics-loops/assumption-ledger-meta-runner-20260618/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `python3 scripts/assumption_derivation_ledger_meta_check.py` -> `PASS=16 FAIL=0`
- `python3 scripts/cached_runner_output.py scripts/assumption_derivation_ledger_meta_check.py`
- `python3 -m py_compile scripts/assumption_derivation_ledger_meta_check.py`
- `git diff --cached --check`
- forbidden audit/status path guard clean

## Discipline

No audit result, ledger JSON, queue, publication effective-status, front-door
status, lane registry, or active-review queue files are edited. No ingredient
row is promoted/demoted/retained/bounded by this PR, and no new axiom is
introduced.
