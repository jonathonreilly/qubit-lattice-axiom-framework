# DM Leptogenesis PMNS Transport Interval Witness

**Date:** 2026-04-16 (scope narrowed 2026-05-26; runner repaired 2026-05-27)
**Status:** bounded - imported transport interval witness only; the
interpolated equality point is a selector diagnostic, not a selected
physical source law
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
- interpolation along that parameterized family crosses
  `eta/eta_obs = 1`; the exact root is an intermediate-value diagnostic,
  not a retained prediction of the observed baryon ratio.

No physical selector law, full-stack closure, or sole-axiom derivation of the
off-seed source is claimed.

## Runner Repair (2026-05-27)

The raw PMNS projector-interface repair intentionally removed legacy transport
helpers from `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`.
That made this row's old transitive imports stale even though the intended
bounded interval witness only needs a narrow compatibility replay.

This revision makes the primary runner self-contained for the finite
compatibility layer:

- the canonical `CYCLE`, `canonical_h`, active packet diagonalization, and
  one-column transport functional are implemented directly in the primary
  runner;
- the runner imports only `scripts/dm_leptogenesis_exact_common.py` for the
  already-existing exact package constants, normalized transport grid, expansion
  profile, and washout profile; and
- the stale imports of the raw interface, active-projector reduction, and
  flavor-column theorem runners are removed from this row's executable surface.

This is a source-surface repair, not a new axiom or a selector law. The exact
`eta/eta_obs = 1` point remains an interpolated diagnostic against `ETA_OBS`,
so the auditable bounded content is the reproducible seed-to-overshoot interval
witness, not an independent physical prediction of the observed baryon ratio.

## Question

Does the imported PMNS-assisted transport functional contain a seed-to-overshoot
interval witness on the fixed `N_e` parameterized family?

## Bottom Line

Yes, as a bounded diagnostic.  On the imported fixed-seed family:

- the aligned seed benchmark gives
  `max_i eta_i / eta_obs = 0.719082664368` in the self-contained functional
  replay, matching the prior direct-transport benchmark
  `0.7190825360613422` within the runner tolerance;
- the sampled off-seed endpoint gives
  `max_i eta_i / eta_obs = 1.0522203130495849`; and
- the interpolated witness gives `max_i eta_i / eta_obs = 1`.

This is a constructive interval witness inside the imported transport setup.
It is not evidence that the framework physically selects that off-seed source,
and the exact equality at the interpolated root is not load-bearing claim
closure unless a separate selector theorem supplies that root or endpoint.

## Selector Firewall (2026-06-17)

The companion
[`DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md`](DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md)
records the source-side repair for the prior `audited_numerical_match`
verdict.  The repair separates three statements:

1. **Bounded interval support:** the imported transport functional is
   evaluable on the fixed seed family and has a seed endpoint below `1`
   and a sampled endpoint above `1`.
2. **Diagnostic crossing:** by continuity, a parameterized interpolation
   between those two endpoints has at least one root with
   `eta/eta_obs = 1`.
3. **Open selector:** the interval and root do not derive which off-seed
   source, interpolation parameter, or physical transport surface the
   framework selects.  A future theorem would have to supply that selector
   independently of the observed `ETA_OBS` comparator.

This parent row should therefore be read as bounded interval support plus a
selector firewall, not as a numerical match promoted by the exact root.

## Computed Witness

The sampled off-seed endpoint is:

- `x_opt = (0.0876587, 1.49144738, 0.11089392)`
- `y_opt = (0.29016988, 0.18598487, 0.44384525)`
- `delta_opt = -2.2327839107695158`

with best-column value:

```text
eta / eta_obs = 1.0522203130495849
```

The interpolated diagnostic crossing is:

- `lambda_* = 0.914106850348`
- `x_close = (0.128516, 1.411729, 0.149755)`
- `y_close = (0.291587, 0.196351, 0.432063)`
- `delta_* = -2.041003068182`

with:

```text
eta / eta_obs = 1
```

on the tested best flavor column.

This root is reported so the interval can be reproduced.  It is not a
physical selector and should not be cited as a framework prediction of
`eta_obs`.

## Out Of Scope

This row does not claim:

- transport extremality is the physical off-seed source selector;
- the interpolated value `lambda_*` is selected by the framework;
- the off-seed source is derived from the one-qubit operator algebra
  `M_2(ℂ) ≅ Cl(3,0)` on the `Z^3` spatial substrate;
- the imported fixed `N_e` surface is retained as a physical source surface by
  this row;
- full-stack DM/PMNS closure; or
- any promotion of the helper rows used by the runner.

## Command

```bash
python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py
```
