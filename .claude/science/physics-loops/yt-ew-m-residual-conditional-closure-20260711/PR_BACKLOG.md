# PR Backlog

PR creation is delegated to the enclosing `claude/science-fix/*` integration
loop that created this disposable worktree. The science block is not pushed to
`main`; the local handoff records the exact re-audit action.

Recovery commands for the enclosing integration loop:

```bash
git status --short
git add docs/YT_EW_M_RESIDUAL_NOTE_2026-05-02.md \
  docs/EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md \
  scripts/yt_ew_m_residual_channel_check.py \
  scripts/frontier_ew_current_matching_rule_no_go.py \
  outputs/yt_ew_m_residual_channel_check_2026-05-02.txt \
  docs/audit/data/yt_ew_m_residual_reaudit_queue_2026-07-11.json \
  .claude/science/physics-loops/yt-ew-m-residual-conditional-closure-20260711
git commit -m "physics: narrow EW residual to scalar propagator no-go"
git push -u origin HEAD
gh pr create --base main --head claude/science-fix/yt_ew_m_residual_note_2026-05-02-343895ca \
  --title "[physics-loop] yt-ew-m-residual no-go scope repair" \
  --body-file .claude/science/physics-loops/yt-ew-m-residual-conditional-closure-20260711/HANDOFF.md
```
