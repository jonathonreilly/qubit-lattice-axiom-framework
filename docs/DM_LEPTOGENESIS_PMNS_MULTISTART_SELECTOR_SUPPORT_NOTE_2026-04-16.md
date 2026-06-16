# DM Leptogenesis PMNS Multistart Runner Diagnostic

**Status:** bounded - runner diagnostic only on the tested multistart sample
**Status authority:** independent audit lane only
**Claim type:** bounded_theorem
**Date:** 2026-04-16 (scope narrowed 2026-05-24 per audited_conditional `scope_too_broad` repair)
**Script:** `scripts/frontier_dm_leptogenesis_pmns_multistart_selector_support.py`
**Claim boundary:** runner-defined constrained optimization diagnostic only.

**2026-06-16 source-language repair:** the fixed `N_e` seed surface,
transport/readout normalization, and `eta/eta_obs` readout used here are
runner-defined inputs of this sampled diagnostic. This row does not derive
them from Tier-A premises and does not cite them as retained bridge coverage.

## Scope narrowing (2026-05-24 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair instruction: *"provide a retained certified-global reduced-surface
branch enumeration/selector theorem, or narrow the claim to the runner
diagnostic only."*

This revision takes the narrowing option. The binding evidence of this
note is exactly the **sampled multistart runner diagnostic** as
reported by the cached stdout of
`scripts/frontier_dm_leptogenesis_pmns_multistart_selector_support.py`:
on the tested multistart starts on the runner-defined fixed `N_e` seed
surface, the constrained scan reports one low-action diagnostic branch
(separated from a high-action branch by a finite action gap on the
sampled starts). The note does **not** claim certified-global branch
enumeration, theorem-grade global selector authority, or
branch-uniqueness beyond what the sampled starts cover. The
certified-global enumeration/selector theorem alternative repair path
is deferred to future work and is **not** part of this row's binding
scope.

## Question

After the relative-action stationarity runner support, one caveat still remained:

- the sampled runner surface gave a seed-relative bosonic action diagnostic;
- the PMNS-assisted `N_e` closure source was the **lowest-action branch**
  among sampled stationary closure branches in that runner packet.

Could that last branch-global caveat now be removed on the refreshed DM
branch?

## Bottom line (narrowed)

The current broad multistart scan gives a runner diagnostic on the
tested starts: the sampled multistart constrained scan recovers one
low-action PMNS-assisted `N_e` branch on the runner-defined fixed seed
surface. This is a runner-level diagnostic only; it is **not** a
certified-global branch enumeration nor a theorem-grade selector
result.

On the sampled multistart starts, broad enumeration of exact closure
starts on the runner-defined fixed `N_e` seed surface yields two dominant
stationary closure branches recovered by the runner:

1. a low-action branch
2. a high-action branch

These are separated by a finite action gap on the sampled starts.

Later strengthened reduced-surface support on the same branch reveals one
additional higher-action stationary branch beyond this broad multistart pair.
That stronger support does not change the favored low-action branch
recovered here on the sampled starts; it only sharpens the recovered
branch count on the reduced surface (with the same narrow-diagnostic
caveat).

On the sampled multistart starts, the broad scan isolates the same
low-action branch already seen in the later reduced-surface support
pass. That branch gives, on the tested starts:

- runner-normalized `eta / eta_obs = 1` on the imposed closure surface

## Stationary branches

The low-action branch is

- `x = (0.471675, 0.553811, 0.664514)`
- `y = (0.208063, 0.464383, 0.247554)`
- `delta ~ 0`
- `S_rel = 0.240906701369`
- `eta / eta_obs = (1.0, 0.75917896, 0.48458840)`

The high-action branch is

- `x = (0.790189, 0.406763, 0.493049)`
- `y = (0.586185, 0.167566, 0.166248)`
- `delta ~ 0`
- `S_rel = 1.110657539...`
- `eta / eta_obs = (1.0, 0.94763529, 0.95876001)`

So the action gap is finite and large:

- `ΔS > 0.5`

On the sampled multistart starts, the low-action branch is the
lower-action branch among the dominant pair recovered by the runner; the
later reduced-surface support pass recovers the same branch as the
lowest-action branch in a three-branch set on its sampled surface. No
global-selector or certified-enumeration content is claimed here.

## Status

This is a **runner diagnostic only**, not live closure authority and
not a certified-global selector:

- it is a broad multistart constrained scan on the runner-defined fixed `N_e` seed
  surface
- on the sampled starts, it recovers a low-action and high-action
  stationary pair with a large action gap
- it is a sampled-multistart diagnostic on the tested starts only
- it is not, by itself, a theorem-grade global selector and does not
  certify global enumeration of stationary branches

## Numerical consequence (on the sampled multistart starts)

Relative to the old one-flavor runner diagnostic miss

- `eta_obs / eta = 5.297004933778`

the low-action branch recovered on the tested starts gives

- runner-normalized `eta / eta_obs = 1`

So the old `5.3x` runner diagnostic miss is gone on the low-action branch
among the sampled starts. This is a runner diagnostic on the tested starts
only, not a framework-native readout theorem.

## Scope

This note is binding only as a **sampled-multistart runner
diagnostic**. The later reduced-surface support pass is stronger on the
same branch set on its tested surface; neither pass is theorem-grade
and neither closes certified-global enumeration or global selector
authority.

## Bounded out-of-scope / open future work

Per the 2026-05-24 narrowing, the following are explicitly **not**
part of this row's binding scope:

- Any certified-global reduced-surface branch enumeration claim
  (covering all admissible stationary closure branches on the reduced
  surface, not just those recovered on the sampled multistart starts).
- Any theorem-grade global selector closure beyond the sampled-starts
  diagnostic recorded here.
- Branch-uniqueness or branch-completeness outside the sampled starts
  the runner actually tests.

A retained certified-global branch enumeration / selector theorem
(the alternative repair path the auditor offered) is deferred to
future work. Until it lands, the binding claim is the
sampled-multistart runner diagnostic only.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_multistart_selector_support.py
```
