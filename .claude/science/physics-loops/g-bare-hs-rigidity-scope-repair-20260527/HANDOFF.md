# Handoff

This block repairs a critical conditional g_bare row by narrowing it to the
audit-supported R1-R3 Hilbert-Schmidt trace/Casimir rigidity theorem.

What changed:

- `claim_type` is now `bounded_theorem`.
- R4 physical connection-coordinate equivalence was removed from the binding
  theorem and marked as out of scope.
- R5 Wilson coefficient routing was removed from the binding theorem and marked
  as out of scope.
- The companion `g_bare = 1` constraint-vs-convention row is explicitly not
  closed by this note.
- Pipeline artifacts queue the row as `unaudited`, `ready: true`.

Reviewer checks:

```bash
python3 scripts/cached_runner_output.py --check-only --tail-chars 1200 scripts/frontier_g_bare_audit_residual_closure.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md .claude/science/physics-loops/g-bare-hs-rigidity-scope-repair-20260527
bash docs/audit/scripts/pre_commit_audit_check.sh
```
