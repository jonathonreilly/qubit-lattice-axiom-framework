# K-Z SU(3) beta=6 Reproduction Contract Firewall

Date: 2026-06-06

Status: no-go

actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This artifact prunes invalid K-Z beta=6 reproduction routes; it does not produce a new beta=6 bracket."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Summary

This block builds on the K-Z convention split:

```text
SU(3), Wilson beta=6  ->  paper coordinate lambda = N^2 / beta = 1.5.
```

It adds a sharper firewall for the remaining K-Z external-lift blocker. A
repo-owned finite `SU(3)`, Wilson `beta=6` reproduction cannot be accepted if
it only supplies support, Hausdorff, Hankel, Wilson-loop Gram, and
area-style inequalities. Those constraints admit the endpoint witness

```text
P = R = Q = 1,
all moments and cross-correlators = 1,
```

so the upper bound remains the trivial support endpoint. The missing
load-bearing ingredient is beta-coupled source information: either primary
source data/table extraction at `lambda=1.5`, or explicit
Migdal-Makeenko / Schwinger-Dyson loop equations in a repo-owned SDP
reproduction.

## Runner

Runner:

```text
scripts/frontier_kz_beta6_reproduction_contract_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_kz_beta6_reproduction_contract_2026_06_06.txt
```

The runner checks three things:

1. The coordinate contract: equating the paper coefficient `N/(2 lambda)` to
   standard Wilson `beta/(2N)` gives `lambda=N^2/beta`, hence `lambda=1.5`
   for `N=3`, `beta=6`.
2. The support-only SDP firewall: the endpoint witness `P=R=Q=1` satisfies
   the support interval, plaquette Hankel PSD, shifted Hausdorff PSD,
   Wilson-loop Gram PSD, area-style inequalities, and the admitted lower
   bound `p1 >= 0.4225`.
3. The reproduction contract: the old `W_lift ~= 0.05` shortcut fails, and a
   support-only SDP at the correct coordinate still fails unless it includes
   beta-coupled loop equations or primary source data.

## Contract

An acceptable future K-Z beta=6 source package must satisfy one of two routes.

### Primary Source-Data Route

- Target the finite `SU(3)`, Wilson `beta=6` coordinate, i.e. source-paper
  `lambda=1.5` under the action convention above.
- Use primary table/source data, not only an image-vector extraction.
- Record extraction method, uncertainties, outward rounding, and raw cached
  source artifact.
- Explicitly distinguish the prior image-derived `lambda=3.0` width from the
  `lambda=1.5` target.

### Repo-Owned SDP Route

- Target `N=3`, Wilson `beta=6`, paper coordinate `lambda=1.5`.
- State the truncation/cutoff, Wilson-loop basis, normalization, and objective.
- Include beta-coupled Migdal-Makeenko / Schwinger-Dyson loop equations or an
  equivalent beta-coupled source constraint.
- Report positivity constraints, solver/version, tolerances, primal and dual
  residuals, raw solver output, and outward-rounded final interval.
- Keep figure-derived values as comparators unless backed by source data.

## No-Go Boundary

This block prunes exactly these routes:

```text
old W_lift ~= 0.05 -> finite SU(3), Wilson beta=6 source bracket
support-only SDP constraints -> nontrivial finite SU(3), Wilson beta=6 upper bound
```

It does not rule out a primary source-data extraction at `lambda=1.5`, and it
does not rule out a repo-owned SDP that adds beta-coupled loop equations.

## Claim Boundary

This is negative route pruning plus an acceptance contract. It does not
certify a finite `SU(3)`, Wilson `beta=6` bracket, does not close the
K-Z external-lift gate, and does not promote the gauge-scalar parent chain.
The next positive K-Z route must supply primary source data or the missing
beta-coupled loop-equation machinery.
