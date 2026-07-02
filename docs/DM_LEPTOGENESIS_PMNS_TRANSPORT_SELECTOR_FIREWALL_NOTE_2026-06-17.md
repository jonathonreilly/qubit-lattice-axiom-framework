# DM Leptogenesis PMNS Transport Selector Firewall

**Date:** 2026-06-17
**Claim type:** no_go
**Status:** source-side selector firewall; independent audit owns effective
status.
**Primary runner:**
[`scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py`](../scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py)

## Claim

The parent transport note
`DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md`
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

## No-Go Discipline Gate

This gate is source-side scope control, not an audit verdict. The negative
claim is only that the current intermediate-value root is not by itself a
physical selector law.

**N1 -- Alternative routes.** Five attacks were checked. (1) Interval
bracketing: it proves a crossing, not selection. (2) Continuity: it proves
existence of at least one root, not which source is physical. (3) The sampled
off-seed endpoint: it is an imported endpoint, not a derived selector. (4)
Using `ETA_OBS` to choose `lambda_*`: this is the hidden empirical selector
forbidden above. (5) A future independent endpoint, lambda, or source-law
theorem: this remains open and is outside the firewall.

**N2 -- Wall independence.** There is one collapsed wall: a selector theorem
is missing. The interval arithmetic and target crossing do not create separate
physical-selection authorities.

**N3 -- Hidden-wall scan.** The load-bearing hidden risks are exactly the
observed comparator, the sampled endpoint, and the interpolation parameter.
All three are named as non-authorities unless separately derived.

**N4 -- Residual matching.** The parent residual is the old numerical-match
reading of `eta/eta_obs = 1`. This note attacks only that selector residual;
it does not attack the parent interval-evaluation arithmetic.

**N5 -- Rhetoric audit.** "No selector" means no selector in this source
packet. It does not mean no future DM/leptogenesis selector can exist.

**N6 -- Partial-closure path scan.** The legitimate closure path is explicit:
derive the endpoint, `lambda_*`, a source law, or a same-surface baryon-ratio
mechanism without using `ETA_OBS` as a hidden target.

**N7 -- Steelman.** A stronger transport principle could make the sampled
off-seed endpoint or the same interpolation parameter natural before looking
at `ETA_OBS`. That would be a real positive repair; it is not present here.

**N8 -- Cross-cycle echo.** This matches the repo's recurring numerical-match
firewall pattern: an exact hit against an observed comparator remains
diagnostic until a framework-native selector chooses the target surface.

## Verification

Run:

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_transport_selector_firewall_2026_06_17.py
```

Expected result:

```text
PASS=12 FAIL=0
```
