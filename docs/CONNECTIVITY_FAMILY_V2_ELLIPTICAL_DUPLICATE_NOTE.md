# Connectivity Family V2 Elliptical Duplicate Note

**Date:** 2026-04-06; cache-aligned row inventory 2026-06-18; runner-output
accounting refresh 2026-06-20
**Claim type:** bounded_theorem
**Status:** bounded diagnostic duplicate of the parent sign-portability gate;
the parity-tapered elliptical-shell sweep is not an independent
tier-ratifiable family.

**Status authority:** independent audit lane only. This note records no audit
verdict and asserts no grade; the effective status is set exclusively by the
independent audit lane on `origin/main`.

## Artifact Chain

- Primary runner:
  [`scripts/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.py`](../scripts/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.py)
- Runner cache:
  [`logs/runner-cache/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.txt`](../logs/runner-cache/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.txt)
- Parent invariant:
  [`docs/SIGN_PORTABILITY_INVARIANT_NOTE.md`](SIGN_PORTABILITY_INVARIANT_NOTE.md)
- Helper source:
  [`scripts/gate_b_no_restore_farfield.py`](../scripts/gate_b_no_restore_farfield.py)

## Question

Does a parity-tapered elliptical-shell connectivity rule on the no-restore
grown slice produce a second independent sign-law family beyond the parent
sign-portability gate?

## Current Cached Sweep

The current evidence surface is the cached 45-row runner sweep, not the older
targeted-slice inventory. The runner configuration is:

```text
h = 0.5
NL = 25
drifts = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
seeds = [0, 1, 2, 3, 4]
source_z = 3.0
source_strength = 5.0e-05
field_power = 1
min_edges = 5
shell_count = 8
```

The old `drift = 0.02, seed = 0` targeted row is not part of this current
runner/cache packet and is not used by this note.

## Checked Row Inventory

| drift | passing seeds | failing seeds | pass count |
| ---: | --- | --- | ---: |
| `0.00` | `0, 1, 2, 3, 4` | none | `5/5` |
| `0.05` | `0, 2, 3` | `1, 4` | `3/5` |
| `0.10` | `0, 2` | `1, 3, 4` | `2/5` |
| `0.15` | `2` | `0, 1, 3, 4` | `1/5` |
| `0.20` | `2, 3` | `0, 1, 4` | `2/5` |
| `0.25` | `0, 2, 3` | `1, 4` | `3/5` |
| `0.30` | `0, 1, 2, 3` | `4` | `4/5` |
| `0.40` | `2, 3, 4` | `0, 1` | `3/5` |
| `0.50` | `1, 4` | `0, 2, 3` | `2/5` |

Total: `25/45` rows pass the runner gate. This matches the runner's verbatim
`SAFE READ` summary line `passed rows: 25/45` in the SHA-pinned cache.

The passing rows retain the runner's exact-control packet:

- exact zero-source baseline;
- exact neutral same-point cancellation;
- plus/minus antisymmetry with the accepted sign orientation;
- weak-field double-source exponent near unit slope.

The cache reports mean passing exponent `0.999826`, matching the runner's
verbatim `SAFE READ` line `mean exponent among passes: 0.999826`. Rows that
fail do so by the sign-orientation condition, not by loss of the exact zero or
neutral controls.

## Safe Read

The elliptical-shell rule reproduces the parent sign-law gate on many finite
rows, but the pass set is patchy across seeds and drifts. That is useful as a
basin-width and sign-orientation diagnostic. It is not evidence for a new
independent connectivity family.

The source conclusion is therefore a duplicate-boundary claim:

- the control surface is real in the cached finite sweep;
- the unit-slope weak-field response is real on the passing rows;
- the failed rows mark a sign-orientation boundary;
- the result stays inside the parent sign-portability gate and does not add a
  new order parameter.

## Boundary

This note does not claim:

- a new retained or tier-ratifiable connectivity family;
- a universal sign-portability theorem;
- an independent order parameter beyond the parent sign-portability gate;
- row evidence outside the current cached 45-row sweep;
- any new audit verdict.

## Final Verdict

The parity-tapered elliptical-shell sweep is a bounded finite diagnostic
duplicate of the parent sign-portability gate. It records a `25/45`
cache-backed pass surface and a sign-orientation boundary, not a second
independent retained family.

## Repair: runner-output accounting refresh (2026-06-20)

This repair refreshes the reported rows/pass accounting against the current
SHA-pinned cached sweep and records why the older drift=0.02 targeted row is
not part of this packet. No runner computation and no derived value were
changed; only the note's reported accounting was synced to the runner's
current cached output.

Quote-anchored accounting:

- Pass total — before: `Total: 25/45 rows pass the runner gate.`; after:
  unchanged at `25/45`, now anchored to the runner's verbatim `SAFE READ` line
  `passed rows: 25/45`.
- Mean passing exponent — before: `mean passing exponent 0.999826`; after:
  unchanged at `0.999826`, now anchored to the runner's verbatim `SAFE READ`
  line `mean exponent among passes: 0.999826`.
- Per-drift inventory — before: the `Checked Row Inventory` table; after:
  unchanged, re-verified row-for-row against the current SHA-pinned cache
  (per `(drift, seed)` `YES`/`no` flags). All nine drift rows and their
  passing/failing seed sets match the current cache exactly.

Verbatim runner `SAFE READ` summary block reproduced from the current
SHA-pinned cache:

```text
SAFE READ
  passed rows: 25/45
  drift coverage: [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5]
  mean exponent among passes: 0.999826
  this family reproduces the portable sign-law fixed point on a narrow slice
  it does not broaden the retained family set
```

Drift=0.02 certificate (second audit branch): not applicable. The current
runner's `DRIFTS` list is
`[0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]`; it does not contain
`0.02`, so the runner computes no drift=0.02 row and the SHA-pinned cache
contains no such row. The honest refresh is therefore the current-cache row
set above. The old `drift = 0.02, seed = 0` targeted row remains out of this
packet (see `Current Cached Sweep`).
