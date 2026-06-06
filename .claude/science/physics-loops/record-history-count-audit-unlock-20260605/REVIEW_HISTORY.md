# Review History

## Local review pass

Checklist:

- no `docs/audit/data` edits;
- no audit verdict application language;
- every candidate has a remaining gate;
- old P1 direct dependents are not auto-migrated;
- probability/instrument/dynamics rows are not promoted by finite history
  support.

Result:

- `python3 scripts/frontier_record_history_count_audit_unlock_scan_2026_06_05.py`
  -> `SCORECARD PASS=67 FAIL=0`
- `python3 -m py_compile scripts/frontier_record_history_count_audit_unlock_scan_2026_06_05.py`
- `git diff --check`
- wording scan prompted one table-label narrowing from status-like
  source-row language to `source-side theorem candidate`.
