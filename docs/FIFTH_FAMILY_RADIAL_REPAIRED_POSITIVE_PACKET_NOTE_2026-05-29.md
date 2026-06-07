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
**Companion runner caches:**
[`logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt`](../logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt),
[`logs/runner-cache/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.txt`](../logs/runner-cache/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.txt),
[`logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt`](../logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt).
**Helper sources:**
[`scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py`](../scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py),
[`scripts/gate_b_no_restore_farfield.py`](../scripts/gate_b_no_restore_farfield.py).

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

## 2026-06-06 Primary-Runner Companion Packet Inlining Repair

The 2026-06-07 audit accepted the primary ten-row basin computation but left
the row conditional because the restricted packet did not include enough
verification for the load-bearing F~M transfer companion. The primary basin
runner now checks the companion packet inline. After recomputing the ten-row
basin surface, it verifies:

- the primary runner/cache, F~M transfer runner/cache, sweep runner/cache,
  failure-audit runner/cache, restored radial helper, and no-restore growth
  helper are linked from this note;
- the F~M transfer source is untruncated and contains the two sampled target
  rows, weak-field two-strength computation, logarithmic scaling exponent, and
  `ASSERTIONS: PASS` gate;
- the sweep and failure-audit companion sources are untruncated and contain
  the positive-row and sign-orientation-boundary assertions;
- the F~M, sweep, and failure-audit companion caches are SHA-fresh and
  clean-exit;
- the F~M cache reports `passed rows: 2/2` and
  `mean F~M among passes: 0.999439`;
- the sweep cache reports `passed rows: 2/3` with drift coverage
  `[0.05, 0.3]`;
- the failure-audit cache reports exactly one boundary row,
  `drift=0.20 seed=0`.

The primary runner reports:

```text
INLINE COMPANION PACKET: PASS=58 FAIL=0
```

This remains a packet-completeness repair for the finite bounded radial-shell
claim. It does not claim family-wide survival, continuum/asymptotic closure, a
physical mass-observable derivation, or audit-effective status.

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
