# Handoff

## What changed

This branch adds a fifth exact route to the Koide `r=1/2` no-go note:
`C3`-compatible coefficient rephasing / doublet-basis calibration preserves
`|b|^2/a^2`, so it cannot force `r = 1/2`.

## Why it matters

The latest audit row for
`koide_r_half_not_symmetry_protected_dynamical_norm_balance_narrow_no_go_note_2026-06-04`
was conditional only because the no-go had four checked N1 routes. The audit
note explicitly requested a fifth route or a narrower rescope. This branch
adds the fifth route and keeps the broader dynamics/extra-structure openings
intact.

## Reviewer focus

- Confirm the new rephasing/doublet-basis route is genuinely distinct from the
  earlier unitary singlet/doublet swap route.
- Confirm the route is scoped to coefficient-channel phase/basis calibration
  and does not overclaim against dynamics, variational principles, nonunitary
  maps, or enlarged operator algebras.
- Confirm no audit/status surface was edited.

## Exact next action

Open review PR from `codex/koide-rhalf-fifth-route-20260618`.
