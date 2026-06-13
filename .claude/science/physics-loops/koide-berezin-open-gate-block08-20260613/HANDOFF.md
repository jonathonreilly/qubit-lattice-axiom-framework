# Handoff

This PR repairs the high-criticality open-gate row
`koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04`.

The original note stays honest: it still does not derive `r = 1/2`, adopt
orbit-occupancy, or make a mass prediction. The update adds the downstream
source state that was missing from the row:

- the K/CPT orbit quotient equals the `R (+) C` complex-slot quotient;
- the Record axiom declines weighting/occupancy supply;
- two exact models satisfy the checked current surface and differ only by the
  occupancy/slot-degree rule;
- the live residual is now the explicit occupancy atom, not an unstructured
  "Berezin might select det_C" gate.

Artifacts:

- `docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`
- `scripts/berezin_detc_detr_fork_2026_06_04.py`
- `logs/runner-cache/berezin_detc_detr_fork_2026_06_04.txt`
- `.claude/science/physics-loops/koide-berezin-open-gate-block08-20260613/`

Verification:

```bash
python3 scripts/berezin_detc_detr_fork_2026_06_04.py
python3 scripts/precompute_audit_runners.py --allow-non-main --push-mode=none --force --concurrency=1 --runners scripts/berezin_detc_detr_fork_2026_06_04.py
python3 scripts/precompute_audit_runners.py --allow-non-main --check-only --push-mode=none --runners scripts/berezin_detc_detr_fork_2026_06_04.py
git diff --check
git diff --name-only -- docs/audit docs/repo/FRONT_DOOR_STATUS.md
```

Runner result: `SCORECARD: PASS=36 FAIL=0`.

No audit ledger, active queue, front-door status, publication matrix, or
authority surface is edited by this PR.
