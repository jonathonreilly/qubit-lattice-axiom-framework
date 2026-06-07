# Handoff

## What Changed

The exact idempotent-U(1) collapse is preserved and the broad ordering claim is
removed from the theorem surface.

The note now links one-hop authorities for:

- native finite generation algebra;
- generator-rephasing obstruction;
- chiral/anticommuting boundary.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/flavor_idempotent_u1_collapses_2026_05_30.py
git diff --check
git diff --name-only | rg '^docs/audit/' && exit 1 || true
```

## Next Science Target

`flavor_substrate_parent_separate_note_2026-05-30` is the nearest remaining
finite flavor repair candidate.
