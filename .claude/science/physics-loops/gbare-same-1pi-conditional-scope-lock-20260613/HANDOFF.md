# Handoff

Changed source packet:

- `docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md`
- `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py`

Science move:

- Changes the source title/scope from a pinning theorem to a conditional map
  plus residue-normalization obstruction.
- Adds a 2026-06-13 actual-surface scope lock.
- Adds runner checks that downstream rows may not cite this packet as an
  actual-surface theorem deriving `g_bare=1`.

Verification:

```bash
python3 -m py_compile scripts/frontier_gbare_same_1pi_admitted_residue_repair.py
python3 scripts/frontier_gbare_same_1pi_admitted_residue_repair.py
python3 scripts/cached_runner_output.py scripts/frontier_gbare_same_1pi_admitted_residue_repair.py --refresh --timeout-sec 120
python3 scripts/cached_runner_output.py scripts/frontier_gbare_same_1pi_admitted_residue_repair.py --check --timeout-sec 120
```

Expected runner result:

```text
PASS=50 FAIL=0
```

No audit ledger or publication-status file is edited.
