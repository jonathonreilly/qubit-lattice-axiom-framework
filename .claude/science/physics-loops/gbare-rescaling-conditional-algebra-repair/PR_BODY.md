# Summary

Repairs `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` by taking
the audit-specified narrowing path: conditional Gram/beta scaling over
scoped Wilson matching.

The note no longer claims Wilson matching retention, Wilson action-surface
uniqueness, global rescaling-freedom removal, or downstream `g_bare`
retention. The only load-bearing retained dependency is now
`cl3_color_automorphism_theorem`.

# Verification

```bash
python3 -m py_compile scripts/frontier_g_bare_rescaling_conditional_algebra_check.py
bash docs/audit/scripts/run_pipeline.sh
python3 scripts/frontier_g_bare_rescaling_conditional_algebra_check.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md scripts/frontier_g_bare_rescaling_conditional_algebra_check.py .claude/science/physics-loops/gbare-rescaling-conditional-algebra-repair
git diff --check
```

# Post-Pipeline Queue State

The repaired row is `unaudited` / `awaiting_audit`, ready in the audit
queue, critical, and has `criticality_rank: 3`. Direct deps:
`cl3_color_automorphism_theorem`.

The pipeline conservatively invalidated eight downstream rows that had relied
on the prior stronger effective status; this PR does not re-promote them.

# Status Boundary

No audit verdict is applied here. This is a source repair and audit-queue
handoff only.
