# g_bare Constraint Surface Firewall

## Target

- Claim: `g_bare_constraint_vs_convention_theorem_note_2026-05-03`
- Source: `docs/G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`
- Runner: `scripts/frontier_g_bare_constraint_surface_check.py`

## Change

This branch repairs the one uncovered `audited_conditional` row on latest
`origin/main` by strengthening the source boundary instead of pretending the
missing Wilson input has been derived. The note now states the actual
current-surface status as conditional support, names the two scoped inputs
that remain load-bearing, and forbids downstream use as a retained derivation
of Wilson matching, the Wilson action form, the beta surface, or the broader
`g_bare` derivation.

The paired runner now checks those firewall markers before running the exact
Fraction arithmetic:

```text
CN + WM + beta=6 + N_c=3 => g_bare^2 = 1.
```

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_g_bare_constraint_surface_check.py`
- `git diff --check`
- `python3 scripts/precompute_audit_runners.py --check-only --pr-diff origin/main --allow-non-main --push-mode none`

## Remaining Blocker

The scientific blocker is real and unchanged: a separate theorem-grade source
must supply Wilson matching and/or the `beta = 6` surface from accepted
framework inputs before this lane can be promoted beyond conditional support.
This PR does not edit audit results, queue files, or generated effective-status
surfaces.
