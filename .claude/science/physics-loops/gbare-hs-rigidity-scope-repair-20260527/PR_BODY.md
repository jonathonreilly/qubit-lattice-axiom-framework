## Summary

Repairs `g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07` by narrowing
it to the audited-clean core candidate: R1-R3 Hilbert-Schmidt trace-Casimir
rigidity.

The old note also made R4/R5 claims about physical connection equivalence and
Wilson coefficient routing. Those are now explicitly non-binding and require
separate retained-grade bridge theorems.

## Audit Surface

- Target row: `g_bare_hilbert_schmidt_rigidity_theorem_note_2026-05-07`
- New runner: `scripts/frontier_g_bare_hs_rigidity_narrow.py`
- After pipeline: `audit_status=unaudited`, `effective_status=unaudited`,
  `ready=true`
- No new axiom, Wilson matching convention, physical selector, or `g_bare=1`
  promotion.

## Verification

```text
python3 scripts/frontier_g_bare_hs_rigidity_narrow.py
python3 scripts/vocab_lint.py --report-only docs/G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```
