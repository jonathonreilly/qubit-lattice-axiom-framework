# Review History

- Self-review pass: no `docs/audit/data` files or audit ledger files are
  edited; the source note keeps bounded reduced-shell scope and says the row is
  not promoted.
- Verification pass:
  `python3 scripts/frontier_one_parameter_reduced_shell_law.py` -> `PASS=7
  FAIL=0 TOTAL=7`.
- Verification pass:
  `python3 scripts/frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17.py`
  -> `PASS=10 FAIL=0 TOTAL=10`.
