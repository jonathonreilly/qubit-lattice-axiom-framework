# Handoff

Branch: `physics-loop/observable-p2-det-boundary-20260607`

Target:
`observable_principle_p2_det_realization_bridge_conditional_on_fermionic_frame_narrow_theorem_note_2026-05-28`

This block retargets the row to bounded finite determinant/relabeling support.
The runner now verifies:

- the note carries the 2026-06-07 boundary retargeting;
- the unproved physical-frame premises remain outside the direct proof load;
- Berezin determinant, staggered positivity, and relabeling invariance all pass.

Verification:

```text
python3 scripts/audit_companion_p2_det_realization_bridge_conditional_2026_05_28.py
SCORECARD: PASS=35 FAIL=0
```

Reviewer extraction target: keep the finite determinant/relabeling packet if
accepted; do not extract it as full observable-principle P2 realization.
