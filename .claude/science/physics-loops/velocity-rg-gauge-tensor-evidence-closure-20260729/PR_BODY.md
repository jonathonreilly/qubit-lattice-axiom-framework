# Velocity-RG gauge-tensor evidence closure

Closes only the quoted runner-artifact repair target for the bounded finite
reconstruction. It does not supply a carrier, target-surface, continuum,
pole-speed, or RG-coefficient bridge.

## Evidence

- [Trace gate](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/.claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/TRACE_GATE.md) and [claim certificate](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/.claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/CLAIM_STATUS_CERTIFICATE.md)
- [Source note](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/docs/VELOCITY_RG_GAUGE_TENSOR_WTI_XI_AFFINE_DRAG_EXACT_SUPPORT_NOTE_2026-07-17.md)
- [Primary runner](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py) and [complete cache](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.txt)
- [Independent scalar-trace runner](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_independent_recheck_2026_07_29.py) and [standalone cache](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_independent_recheck_2026_07_29.txt)
- [Assumptions and imports](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/.claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/ASSUMPTIONS_AND_IMPORTS.md), [No-Go Discipline](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/.claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/NO_GO_DISCIPLINE_CHECKLIST.md), and [review history](../blob/claude/science-fix/velocity_rg_gauge_tensor_wti_xi_affine_drag_exact_support_no-6a58fc6a/.claude/science/physics-loops/velocity-rg-gauge-tensor-evidence-closure-20260729/REVIEW_HISTORY.md)

## Checks

- Primary live/cache: independent math `PASS=7 FAIL=0`, ordered V1--V7
  `PASS=25 FAIL=0`; complete stdout `3773` characters.
- Standalone independent live/cache: `PASS=10 FAIL=0`.
- Source `29795 < 30000`, primary/helper source below `40000`, and all packet
  roles contain no clipping marker.
- Vocabulary lint, Python compilation, cache freshness, `git diff --check`,
  strict audit lint, full pipeline rehearsal, and repo invariants pass.

Local review disposition: `PASS WITH BOUNDED CLAIMS`. Independent audit is
still required; this PR does not set or predict a verdict.
