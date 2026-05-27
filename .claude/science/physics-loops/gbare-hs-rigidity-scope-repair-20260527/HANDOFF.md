# Handoff

## What Changed

- Replaced the broad HS-rigidity source with a narrow R1-R3 bounded theorem.
- Added `scripts/frontier_g_bare_hs_rigidity_narrow.py`.
- Removed physical connection-equivalence, Wilson routing, and `g_bare = 1`
  closure from the row's binding surface.
- Re-ran the audit pipeline; the row is now queue-ready and unaudited.

## Verification

```text
python3 scripts/frontier_g_bare_hs_rigidity_narrow.py
python3 scripts/vocab_lint.py --report-only docs/G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

## Next Action

Independent audit should review whether the narrowed R1-R3 packet now closes as
bounded support. Downstream `g_bare = 1` uses must not cite this row alone.
