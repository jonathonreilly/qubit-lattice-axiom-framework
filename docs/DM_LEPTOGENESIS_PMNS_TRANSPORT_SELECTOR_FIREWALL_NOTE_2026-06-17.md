# DM Leptogenesis PMNS Transport Selector Firewall

**Date:** 2026-06-17
**Claim type:** no_go
**Status:** source-side selector firewall; independent audit owns effective
status.
**Primary runner:**
[`scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py`](../scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py)

## Claim

The parent transport note
[`DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md`](DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md)
contains a real bounded interval witness: on the imported PMNS-assisted
transport functional, the aligned seed endpoint lies below
`eta/eta_obs = 1`, while a sampled off-seed endpoint lies above `1`.
Continuity then gives an interpolated root with `eta/eta_obs = 1`.

This note proves the source-side firewall:

> The existence of such an interpolated root is not a physical selector law.
> Unless an independent framework theorem selects the off-seed endpoint or the
> interpolation parameter, the equality point is a diagnostic crossing against
> the observed `ETA_OBS` comparator, not a retained prediction.

## Minimal Premises

Allowed:

1. the parent runner's two computed endpoint values,
   `f(0) = 0.719082664368` and `f(1) = 1.0522203130495849`, as replayed
   outputs of the imported transport functional;
2. continuity of the straight-line interpolation used by the parent runner;
3. elementary real-variable algebra.

Forbidden proof inputs:

1. treating `ETA_OBS` as a selected framework output;
2. choosing the interpolation root because it equals the observed comparator;
3. importing a physical source selector for the five-real off-seed family;
4. promoting transport extremality to a retained selector.

## Theorem

Let `f` be the parent runner's scalar diagnostic along a supplied
one-parameter interpolation between the aligned seed source and an off-seed
source.  If `f(0) < 1 < f(1)`, continuity implies at least one
`lambda_* in (0,1)` with `f(lambda_*) = 1`.

That statement is interval arithmetic.  It does not determine which endpoint
or which parameter value is physically selected.  Indeed, for the same seed
value `f(0)`, any sufficiently high supplied endpoint `b > 1` gives a
different linear crossing

```text
lambda_b = (1 - f(0)) / (b - f(0)).
```

Thus the equality `f(lambda_b) = 1` follows from how the target level is
chosen, not from a source-selection theorem.

## Consequence For The Parent Row

The parent row should be audited, if re-opened, as:

- bounded support for an imported transport interval witness;
- exact support for the diagnostic crossing calculation; and
- a no-go/firewall against citing the crossing root as a physical selector.

It should not be cited as:

- a retained derivation of `eta_obs`;
- a derivation of the off-seed five-real source;
- a proof that transport extremality selects the physical source; or
- a full-stack DM/PMNS closure.

## What Remains Open

A positive closure repair would require an independent theorem deriving one of
the following without using the observed `ETA_OBS` comparator as a hidden
selector:

1. the off-seed endpoint itself;
2. the interpolation parameter `lambda_*`;
3. a physical transport/source law that picks the same point; or
4. a different same-surface baryon-ratio mechanism.

This firewall does not rule those routes out.  It only prevents the current
intermediate-value root from being treated as that missing selector.

## Verification

Run:

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py
```

Expected result:

```text
PASS=12 FAIL=0
```
