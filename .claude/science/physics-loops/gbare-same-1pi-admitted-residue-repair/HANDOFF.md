# Handoff

## What changed

This block repairs the same-1PI `g_bare` row by removing the unqualified
theorem posture. The source now says the `g_bare = 1` solve is exact algebra
conditional on an explicit `H_unit`-residue completeness premise.

## Files

- `docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md`
- `scripts/frontier_gbare_same_1pi_admitted_residue_repair.py`
- `outputs/gbare_same_1pi_admitted_residue_repair_2026-05-25.txt`

## Verification

- `bash docs/audit/scripts/run_pipeline.sh`
- `PYTHONPATH=scripts python3 scripts/frontier_gbare_same_1pi_admitted_residue_repair.py`
- `python3 -m py_compile scripts/frontier_gbare_same_1pi_admitted_residue_repair.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md .claude/science/physics-loops/gbare-same-1pi-admitted-residue-repair/*.md`
- `git diff --check`

## Remaining blocker

The branch does not derive `H_unit`-residue completeness. If audit accepts
the rescope, the row should be judged only as narrowed conditional-support.
