# Microcausality Jmax Wilson-Surface Repair Handoff

## Target

Audit row:

```text
microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09
```

Prior audit blocker:

```text
Re-audit after fixing the plaquette normalization in F2/J_max and supplying a retained bridge from the cited action carriers to the diagonal Wilson surface.
```

## What This PR Repairs

- Fixes the Wilson plaquette contribution in F2 from `2 beta / N_c` per face to `2 beta` per face.
- Updates the conservative `d=4`, `beta=6`, `r_W=1` action-density bound from `J_max <= |m| + 30` to `J_max <= |m| + 78`.
- Adds explicit bounded source support for the canonical Wilson surface:
  - `docs/WILSON_REAL_POSITIVE_MEASURE_BOUNDED_PREMISE_BRIDGE_NOTE_2026-06-03.md`
  - `docs/WILSON_ACTION_SURFACE_SELECTOR_REAL_POSITIVE_THEOREM_NOTE_2026-05-25.md`
  - `docs/CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md`
- Adds an F0 runner manifest guard so the runner fails if the note reverts to the stale `2 beta / N_c` theorem formula.

## Honest Boundary

This PR does not claim the Wilson-surface packet is retained. It supplies source-visible bounded support and fixes the actual normalization error. If the reviewer/auditor requires a retained bridge specifically, the next dependency to audit is the Wilson-surface source packet itself.

## Verification

```text
python3 scripts/microcausality_finite_range_h_bridge_2026_05_09.py
python3 scripts/cached_runner_output.py scripts/microcausality_finite_range_h_bridge_2026_05_09.py
python3 -m py_compile scripts/microcausality_finite_range_h_bridge_2026_05_09.py
```

Latest runner result: `PASS=5, FAIL=0`.

