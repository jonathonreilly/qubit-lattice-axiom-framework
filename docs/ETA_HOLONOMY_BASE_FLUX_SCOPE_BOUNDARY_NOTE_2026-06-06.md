# eta Holonomy Base-Flux Scope Boundary

**Date:** 2026-06-06
**Claim type:** exact-support with a scoped negative boundary
**Runner:** [`scripts/frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.py`](../scripts/frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.py)
**Cached output:** [`logs/runner-cache/frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.txt`](../logs/runner-cache/frontier_eta_holonomy_base_flux_scope_boundary_2026_06_06.txt)
(`SCORECARD: PASS=18 FAIL=0`)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch lands the narrower base-connection area-flux theorem requested by the active review queue. It does not prove the missing UD_2 homotopy bridge and does not ask for any retained-grade status change."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope

The active review queue records a gap for closed PR #2207:
`ETA_PHASE_HOLONOMY_AREA_FLUX_NOT_BRAID_INVARIANT_NARROW_NO_GO_NOTE_2026-05-29.md`
claimed that the staggered `eta`-phase holonomy is not a braid invariant. The
review finding says the useful exact spin-diagonalization and `Z_2` area-flux
calculation were not enough to support the no-go conclusion, because the PR
asserted two unproved topological steps:

- the compared detour swaps are the same element of `B_2(Z^3)`;
- a one-token plaquette loop is null-homotopic in `UD_2(Z^3)`.

This note takes the salvage option named in that queue entry: land only the
narrower base-connection area-flux theorem and leave the `UD_2` homotopy bridge
open.

## Exact Base Theorem

Let the three spatial staggered phases be

```text
eta_1(x) = 1
eta_2(x) = (-1)^x1
eta_3(x) = (-1)^(x1+x2)
```

and let

```text
T(x) = sigma_1^x1 sigma_2^x2 sigma_3^x3 .
```

The runner verifies exactly on `3^3` and `4^3` blocks that

```text
T(x)^dag sigma_mu T(x + e_mu) = eta_mu(x) I_2 .
```

So the staggered phases are a scalar `Z_2` connection in the spin-diagonal
frame. Its coordinate plaquette curvature is uniformly `-1`:

```text
F_{mu,nu}(x) =
  eta_mu(x) eta_nu(x + e_mu) eta_mu(x + e_nu) eta_nu(x)
  = -1 .
```

The same curvature survives a deterministic `Z_2` gauge transformation in the
runner. Rectangular base loops in each coordinate plane then obey

```text
Hol(rectangle a x b) = (-1)^(a b).
```

In particular a `1 x 1` base loop has holonomy `-1`, while a `1 x 2` base loop
has holonomy `+1`.

## Boundary Against the Closed-PR No-Go

The runner does not assert that the two detour swaps compared by PR #2207 are
the same braid class. That is precisely the missing bridge. The current exact
result is weaker and cleaner:

- eta holonomy is a base-graph area-flux computation;
- different base areas can carry different eta holonomies;
- a nearest-neighbor `Z^3` site graph treated as a graph is a 1-complex and
  supplies no plaquette 2-cell by itself;
- therefore a geometric square is not automatically a null-homotopy in
  `UD_2(Z^3)`.

If a later theorem proves that two different-area exchange loops represent the
same element of `B_2(Z^3)`, then this base area law becomes an obstruction to
using eta holonomy as a braid-class character. This branch does not supply that
theorem.

## Claim-State Movement

This partially closes the active review queue item by preserving the exact
calculation from PR #2207 in a form that no longer overclaims the topology.
The remaining open blocker is specific:

```text
Prove or cite a retained-grade bridge identifying the relevant detour swaps in
UD_2(Z^3), or keep the eta result scoped to base-connection area flux.
```

No new axiom, selector, Koide/generation dial setting, or retained-grade status
proposal is introduced here.
