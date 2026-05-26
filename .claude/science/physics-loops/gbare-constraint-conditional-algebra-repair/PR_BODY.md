# Summary

Repairs `g_bare_constraint_vs_convention_theorem_note_2026-05-03` by taking
the audit-specified narrowing path:

```text
CN + WM + beta=6 + N_c=3 => g_bare^2 = 1
```

The note no longer claims beta pinning, Wilson action-surface uniqueness,
no-external-scale closure, or downstream `g_bare` retention. The only
load-bearing retained dependency is now `cl3_color_automorphism_theorem`.

# Verification

```bash
python3 -m py_compile scripts/frontier_g_bare_constraint_surface_check.py
bash docs/audit/scripts/run_pipeline.sh
python3 scripts/frontier_g_bare_constraint_surface_check.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md scripts/frontier_g_bare_constraint_surface_check.py .claude/science/physics-loops/gbare-constraint-conditional-algebra-repair
git diff --check
```

# Post-Pipeline Queue State

The repaired row is `unaudited` / `awaiting_audit`, ready in the audit
queue, critical, and has `criticality_rank: 3`. Direct deps:
`cl3_color_automorphism_theorem`.

The pipeline conservatively invalidated five downstream rows that had relied
on the prior stronger effective status; this PR does not re-promote them.

# Status Boundary

No audit verdict is applied here. This is a source repair and audit-queue
handoff only.
