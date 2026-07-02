# DM Live Constants Canonical Edge Certificate

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** bounded support theorem / dependency-edge certificate
**Status:** bounded support only
**Source runner:** [`scripts/frontier_dm_live_constants_canonical_edge_2026_06_18.py`](../scripts/frontier_dm_live_constants_canonical_edge_2026_06_18.py)
**Runner cache:** [`logs/runner-cache/frontier_dm_live_constants_canonical_edge_2026_06_18.txt`](../logs/runner-cache/frontier_dm_live_constants_canonical_edge_2026_06_18.txt)

## Scope

This note supplies a narrow source-side certificate for the live-constant
edge used by the same-surface DM thermal bounding helper packet. It verifies
that the helper constants currently used by the DM thermal layer are the same
canonical arithmetic quantities exposed by
[`CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md`](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md)
and by `scripts/canonical_plaquette_surface.py`, plus explicit eta/Omega
bookkeeping for the observed comparison constants.

This is not a DM closure theorem. It is a bounded support certificate for one
piece of the parent blocker:

```text
live-DM plaquette / eta-omega constants
```

It does not close the separate packet-completeness / selector premise.
Independent audit owns any effective status, dependency registration, or
verdict change.

## Certified Edges

The runner checks the following equalities directly from source helpers:

```text
P                     = 0.593400000000000
u_0                   = P^(1/4) = 0.877681381198684
alpha_bare            = 1/(4 pi) = 0.079577471545948
alpha_LM              = alpha_bare/u_0 = 0.090667836017286
alpha_s(v)            = alpha_bare/u_0^2 = 0.103303816122267
DM ALPHA_LO           = alpha_LM
DM ALPHA_HI           = -log(1 - (pi^2/3) alpha_bare)/(pi^2/3)
```

The live DM helper `scripts/dm_leptogenesis_exact_common.py` carries
`PLAQ_MC`, `u0`, `alpha_bare`, and `ALPHA_LM`; the thermal helper carries
`ALPHA_LO` and `ALPHA_HI`. This certificate makes those identifications
visible and runner-checked rather than relying on an opaque hard-coded
constant packet.

## Eta/Omega Bookkeeping

The observed comparison constants remain observed inputs, not framework
derivations:

```text
ETA_OBS       = 6.12e-10
OMEGA_DM_OBS  = 0.268
H_PARAM       = 0.674
Omega_b h^2   = 3.6515e-3 * (ETA_OBS / 1e-10)
Omega_b       = (Omega_b h^2) / H_PARAM^2
Omega_DM/Omega_b = 5.447934280745940
```

The runner checks this arithmetic and a falsifier: perturbing `ETA_OBS`
changes `Omega_b`, so the observed value is load-bearing bookkeeping and is
not silently derived from the framework.

## Firewalls

- No new axiom or primitive premise is introduced.
- This note does not derive `CANONICAL_PLAQUETTE = 0.5934`.
- This note does not derive `ETA_OBS` or `OMEGA_DM_OBS`.
- This note does not close packet-completeness or selector authority.
- This note does not change an audit ledger, audit verdict, or effective
  status.
- Downstream DM closure still inherits the parent plaquette scope and the
  observed-comparator scope recorded here.

## Downstream Use

The parent trace target
`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md`
may cite this note only as a bounded support certificate for the live constants
edge. The remaining hard blocker is the selector / packet-completeness premise,
plus any independent audit decision on whether this source-side certificate is
sufficient as a one-hop authority for the constants edge.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_live_constants_canonical_edge_2026_06_18.py
```

The expected result is `FAIL=0`.
