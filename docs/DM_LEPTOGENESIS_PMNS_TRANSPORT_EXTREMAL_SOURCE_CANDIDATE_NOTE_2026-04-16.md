# DM Leptogenesis PMNS Transport Interval Witness

**Date:** 2026-04-16 (scope narrowed 2026-05-26)
**Status:** bounded - imported transport interval witness only
**Status authority:** independent audit lane only
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py`

## Scope Narrowing (2026-05-26)

The prior audit row was `audited_conditional` because this note treated
transport extremality as a candidate physical selector law for the off-seed
`5`-real source.  The restricted packet did not provide retained-grade
authority for the fixed `N_e` surface, the imported transport/kernel helpers,
or a bridge from transport extremality to a physical source selector.

This revision removes that selector claim.  The binding content is only the
bounded interval witness computed by the runner:

- the imported transport functional evaluates the aligned seed endpoint below
  `eta/eta_obs = 1`;
- the same imported functional evaluates a sampled off-seed endpoint above
  `eta/eta_obs = 1`; and
- interpolation along that parameterized family yields a point with
  `eta/eta_obs = 1`.

No physical selector law, full-stack closure, or sole-axiom derivation of the
off-seed source is claimed.

## Question

Does the imported PMNS-assisted transport functional contain a seed-to-overshoot
interval witness on the fixed `N_e` parameterized family?

## Bottom Line

Yes, as a bounded diagnostic.  On the imported fixed-seed family:

- the aligned seed benchmark gives
  `max_i eta_i / eta_obs = 0.7190825360613422`;
- the sampled off-seed endpoint gives
  `max_i eta_i / eta_obs = 1.0522203130495849`; and
- the interpolated witness gives `max_i eta_i / eta_obs = 1`.

This is a constructive witness inside the imported transport setup.  It is not
evidence that the framework physically selects that off-seed source.

## Computed Witness

The sampled off-seed endpoint is:

- `x_opt = (0.0876587, 1.49144738, 0.11089392)`
- `y_opt = (0.29016988, 0.18598487, 0.44384525)`
- `delta_opt = -2.2327839107695158`

with best-column value:

```text
eta / eta_obs = 1.0522203130495849
```

The interpolated closure witness is:

- `lambda_* = 0.914106850348`
- `x_close = (0.128516, 1.411729, 0.149755)`
- `y_close = (0.291587, 0.196351, 0.432063)`
- `delta_* = -2.041003068182`

with:

```text
eta / eta_obs = 1
```

on the tested best flavor column.

## Out Of Scope

This row does not claim:

- transport extremality is the physical off-seed source selector;
- the off-seed source is derived from `Cl(3)` on `Z^3`;
- the imported fixed `N_e` surface is retained as a physical source surface by
  this row;
- full-stack DM/PMNS closure; or
- any promotion of the helper rows used by the runner.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
```
