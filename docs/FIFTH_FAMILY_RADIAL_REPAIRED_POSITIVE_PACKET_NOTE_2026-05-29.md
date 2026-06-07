# Fifth Family Radial Repaired Positive Packet

**Date:** 2026-05-29
**Status:** bounded-support positive packet; proposed for independent audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/FIFTH_FAMILY_RADIAL_BASIN.py`](../scripts/FIFTH_FAMILY_RADIAL_BASIN.py)
**Primary runner cache:** [`logs/runner-cache/FIFTH_FAMILY_RADIAL_BASIN.txt`](../logs/runner-cache/FIFTH_FAMILY_RADIAL_BASIN.txt)
records `status: ok` under the runner-declared audit timeout.
**Companion runners:**
[`scripts/FIFTH_FAMILY_RADIAL_SWEEP.py`](../scripts/FIFTH_FAMILY_RADIAL_SWEEP.py),
[`scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py`](../scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py),
[`scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py`](../scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py).
The primary basin runner intentionally imports these companion runners so the
audit packet builder's static helper-graph resolver includes their source files
in the restricted packet. Its cache also prints a companion packet manifest with
source and cache SHA-256 hashes for each companion.

## Purpose

This packet repairs the stale-helper blocker on the archived fifth-family
radial rows without broadening their scope. The repaired claim is finite and
sampled:

- the radial-shell helper API used by the fifth-family scripts is restored in
  `scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py`;
- the live basin runner recomputes ten `(drift, seed)` rows from the
  no-restore grown slice;
- the primary basin runner declares `AUDIT_TIMEOUT_SEC = 300`, because the
  full ten-row replay can exceed the legacy 120 second audit window under
  contention even though it completes without changing the scientific packet;
- four rows pass exact zero-source, exact neutral-cancellation, sign-
  orientation, and weak-charge exponent gates;
- the two historically cited positive rows also pass the dedicated F~M
  transfer runner;
- the drift `0.20`, seed `0` row remains a sign-orientation boundary, not a
  control leak.

No new axiom, observed target value, fitted selector, or external comparator is
introduced by this repair. The result is a current executable finite packet,
not a family-wide theorem and not a physical mass-observable derivation.

## Repaired API Surface

The stale failure came from importing underscore-prefixed helper names from a
star-import compatibility shim. The repair makes
`CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py` explicitly export the old radial
helper API:

- `Family`
- `_build_radial_shell_connectivity`
- `_measure_family`
- `_field_from_sources`
- `_centroid_z`
- `_propagate`
- `_mean`
- `SOURCE_Z`
- `SOURCE_STRENGTH`

The restored radial builder uses ordinary y/z radial shells around each
layer's center, one parity-neighbor shell, and the same nearest-node edge
floor as the historical fifth-family radial packet.

## Live Runner Results

The repaired `FIFTH_FAMILY_RADIAL_BASIN.py` runner checks
`drifts = [0.05, 0.10, 0.20, 0.30, 0.40]` and `seeds = [0, 1]`.

Positive rows:

- `drift = 0.05`, `seed = 0`
- `drift = 0.10`, `seed = 0`
- `drift = 0.30`, `seed = 0`
- `drift = 0.30`, `seed = 1`

The live basin summary is:

```text
passed rows: 4/10
drift coverage: [0.05, 0.1, 0.3]
mean exponent among passes: 0.999495
ASSERTIONS: PASS
```

The repaired `FIFTH_FAMILY_RADIAL_SWEEP.py` runner replays the historical
three-row packet. It confirms the two cited positive rows and the interior
boundary row:

```text
passed rows: 2/3
drift coverage: [0.05, 0.3]
mean exponent among passes: 0.999439
ASSERTIONS: PASS
```

The repaired `FIFTH_FAMILY_RADIAL_FM_TRANSFER.py` runner checks the two cited
positive rows:

```text
passed rows: 2/2
mean F~M among passes: 0.999439
ASSERTIONS: PASS
```

The repaired `FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py` runner confirms that the
interior row `drift = 0.20`, `seed = 0` is a sign-orientation miss:

```text
failing rows: 1
drift=0.20 seed=0 plus=-2.028e-06 minus=+2.028e-06 exp=1.000
ASSERTIONS: PASS
```

The primary basin runner's `COMPANION PACKET MANIFEST` pins the companion
sources and caches, including the F~M transfer source/cache named by the audit
repair note. This packet-surface repair is purely runner-manifest hygiene; it
does not widen the bounded positive claim.

## Claim Boundary

This packet supports only the following bounded positive claim:

> In the live no-restore grown-slice harness, the repaired radial-shell
> fifth-family connectivity rule has four sampled rows satisfying the declared
> finite controls and sign-orientation gates, and the two historically cited
> positive rows satisfy the dedicated F~M transfer check.

It does not claim:

- family-wide radial-shell survival;
- a continuum, asymptotic, or architecture-universal theorem;
- a physical mass-observable derivation;
- a retained status before independent audit.

Independent audit should treat this as a re-audit target for a narrow finite
positive packet that repairs the old stale-helper failure.
