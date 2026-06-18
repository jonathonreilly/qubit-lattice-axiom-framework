# Summary

Repairs the source-side citation-hygiene blocker for
`koide_q_delta_linking_relation_theorem_note_2026-04-20`.

This does not audit, retag, or promote the row. It adds a citation firewall to
the formal Q-Delta note and extends the paired runner to scan direct source
citations for stale uses as a Koide selector, Berry/radian bridge, PDG
comparator, or charged-lepton offset theorem.

# Trace Gate

- Target: `koide_q_delta_linking_relation_theorem_note_2026-04-20`
- Current main audit status: `audited_renaming`
- Audit blocker addressed: second auditor requested citation-use recheck
- Artifact role: runner certificate plus source citation cleanup
- Independent audit still required before any status change

# Verification

```bash
python3 scripts/frontier_koide_q_delta_formal_ratio_repair.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_q_delta_formal_ratio_repair.py
python3 -m py_compile scripts/frontier_koide_q_delta_formal_ratio_repair.py scripts/frontier_koide_q_delta_linking_relation.py
git diff --check
```

Runner result: `PASS=106 FAIL=0`.

# Guardrails

- No audit ledger or queue edits.
- No effective-status output edits.
- No retained/promoted status claim.
