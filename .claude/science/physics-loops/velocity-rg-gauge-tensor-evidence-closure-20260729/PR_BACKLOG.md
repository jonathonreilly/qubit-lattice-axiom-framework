# PR Backlog

PR creation is deferred because the managed worktree cannot write the shared
Git metadata (`FETCH_HEAD` failed with `Operation not permitted`) and network
delivery is unavailable. The user-provided `claude/science-fix/...` branch is
the orchestrator's explicit override of the generic `physics-loop/...` branch
namespace. The science-fix orchestrator may recover with:

```bash
git add docs/VELOCITY_RG_GAUGE_TENSOR_WTI_XI_AFFINE_DRAG_EXACT_SUPPORT_NOTE_2026-07-17.md \
  scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py \
  scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_independent_recheck_2026_07_29.py \
  logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.txt \
  logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_independent_recheck_2026_07_29.txt \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/APPROACH_REGISTRY.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/ARTIFACT_PLAN.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/ASSUMPTIONS_AND_IMPORTS.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/CLAIM_STATUS_CERTIFICATE.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/GOAL.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/HANDOFF.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/LITERATURE_BRIDGES.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/NO_GO_DISCIPLINE_CHECKLIST.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/NO_GO_LEDGER.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/OPPORTUNITY_QUEUE.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/PR_BACKLOG.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/PR_BODY.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/REVIEW_HISTORY.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/ROUTE_PORTFOLIO.md \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/STATE.yaml \
  .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/TRACE_GATE.md
git commit -m "fix(velocity-rg): supply complete independent runner evidence"
git push -u origin HEAD
gh pr create --base main --title "[physics-loop] velocity-rg gauge tensor bounded theorem evidence closure" --body-file .claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/PR_BODY.md
```
