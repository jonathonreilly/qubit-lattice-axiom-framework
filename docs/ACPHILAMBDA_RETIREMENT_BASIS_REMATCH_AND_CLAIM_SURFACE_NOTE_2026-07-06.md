# AC_phi_lambda Historical Retirement Re-Match — Current Obligation Surface

**Original date:** 2026-07-06

**Current correction:** 2026-07-11

**Claim type:** meta

**Premise weight:** none
**Primary runner:** [`scripts/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.py`](../scripts/acphilambda_retirement_basis_rematch_claim_surface_2026_07_06.py)

## Current result

The 2026-07-05 governance disposition is historical only. It does not supply
or retire any physics dependency. The current exact AC surface is:

| Atom | Current status |
|---|---|
| matter-action occupancy statistical grain | [open derivation obligation](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md) |
| R-eta h-class/h-unit physical readout | [open derivation obligation](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md) |

Both carry zero premise weight. The general staggered-Dirac gate keeps its own
ordinary ledger status and is no longer overloaded as a supplied premise id.

Theta's gauge-side disposition is unchanged. Its mass-side composition remains
conditional on both the occupancy-grain obligation and the independent
quark-determinant cross-sector readout obligation; removing the governance-only
channel exposes rather than supplies that second bridge.

## Downstream boundary

Any result consuming either AC atom remains conditional or
`retained_pending_chain` until a retained theorem closes that exact obligation.
In particular, neither obligation supplies `r=1/2`, `Q=2/3`, `delta=2/9`, a
charged-lepton mass, a species map, a mixing angle, or a probability rule.

This meta note changes no audit verdict. The audit pipeline owns all graph and
publication regrading.
