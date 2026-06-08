# Fifth Family Complex Companion Live Packet

**Date:** 2026-04-06; live-source repair 2026-06-08
**Status:** bounded-support positive packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py`](../scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py)
**Primary runner cache:** [`logs/runner-cache/FIFTH_FAMILY_COMPLEX_TARGETED.txt`](../logs/runner-cache/FIFTH_FAMILY_COMPLEX_TARGETED.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`fifth_family_complex_note`. The archived note failed because the live runner
was then broken by a helper import mismatch and the radial-shell base family was
not current. The helper API now resolves, the base radial packet is current, and
the runner has an explicit assertion gate.

Base packet:
[`FIFTH_FAMILY_RADIAL_NOTE.md`](FIFTH_FAMILY_RADIAL_NOTE.md).

Boundary companion:
[`FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md`](FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md).

## Live Claim

In the radial-shell fifth-family slice, the complex-action targeted runner
finds exactly one anchor row passing the Born/F~M gates and the
`TOWARD -> AWAY` crossover gate:

- `drift = 0.20`, `seed = 0`

Current cached runner output:

```text
anchor rows passing exact gamma=0 + Born/F~M gates: 1
anchor rows with TOWARD -> AWAY crossover: 1
the radial-shell fifth-family slice carries a narrow complex-action companion
ASSERTIONS: PASS
```

The anchor row is narrow: the runner also prints the sampled outer rows and
does not promote the complex companion to a family-wide statement.

## Boundary

This note claims only a sampled complex-action companion on the named
radial-shell anchor row. It does not claim complex-action selectivity across the
whole fifth-family slice, a continuum theorem, a physical mass observable, or
retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_COMPLEX_NOTE.md`](../archive_unlanded/fifth-family-stale-runners-2026-04-30/FIFTH_FAMILY_COMPLEX_NOTE.md).
