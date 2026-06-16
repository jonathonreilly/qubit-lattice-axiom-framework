# Grown Transfer Basin Targeted Repair Note

**Date:** 2026-06-04
**Status:** bounded-support repair packet; independent audit required before any effective status change
**Primary runner:** [`scripts/GROWN_TRANSFER_BASIN_TARGETED.py`](../scripts/GROWN_TRANSFER_BASIN_TARGETED.py)

## Scope

This note repairs the executable support surface for the legacy
`grown_transfer_basin_note` blocker. It does not unarchive the old note, edit
the audit ledger, or assert an audit-ratified status. It supplies a current,
SHA-pinned runner packet for re-audit.

The primary runner imports the sweep runner that computes the row predicates,
so audit packet construction can expose the full executable chain without
making the broader sweep the audited claim.

The grown-geometry helper is the same finite packet registered in
[`GATE_B_GROWN_JOINT_PACKAGE_NOTE.md`](GATE_B_GROWN_JOINT_PACKAGE_NOTE.md);
this repair changes only the downstream basin predicate and the declared
finite `PW` scope.

## Post-audit compute repair (2026-06-15)

The 2026-06-15 audit caught that the note and sweep declared `PW = 8`
while `scripts/gate_b_grown_joint_package.py::grow()` closed over its
retained module default `PW = 10`. This repair uses the audit-suggested
low-blast-radius path: the finite packet is respecified to the actually
computed helper geometry, `PW = 10`, without changing the retained helper
row. The targeted runner imports the same constants from the sweep and
prints them in the cache header. The executable packet now computes the
declared finite claim at `PW = 10`.

The same audit also requested that the complex-action predicate prove an
actual away sign at `gamma = 0.5`, not just a non-positive toward count.
The repaired row now records the mean `gamma = 0.5` deflection and the
per-seed away count. `complex_action_survives(row)` requires
`away_count(gamma=0.5) == 3/3` and mean `gamma=0.5` deflection `< 0`,
in addition to the prior near-linearity checks.

The repaired claim is finite and narrow:

- fixed `H = 0.5`, `K = 5.0`, `BETA = 0.8`, `NL = 25`, `PW = 10`
- seeds `0, 1, 2`
- drifts `0.15, 0.20, 0.25`
- restores `0.60, 0.70, 0.80`
- signed-source and complex-action predicates must hold on the same row

No family-wide growth rule, graph-ladder transfer theorem, or physical
geometry-generic claim is asserted here.

## Predicate Repair

The stale targeted checker treated complex-action survival as
`abs(action_gamma0) < 1e-12`. That was the wrong criterion for this row family:
the complex-action row is meant to preserve the `TOWARD -> AWAY` crossover plus
weak-field near-linearity, not zero deflection at `gamma = 0`.

The current runners now share the same predicate functions:

- `signed_source_survives(row)` requires zero-source and neutral controls,
  a nonzero signed-source response, and charge exponent within `0.05` of `1`.
- `complex_action_survives(row)` requires `action_toward == (positive, zero)`
  at `gamma = 0` and `gamma = 0.5`, `away_count(gamma=0.5) == 3/3`,
  mean `gamma=0.5` deflection `< 0`, and `F0 > 0.99`, `F05 > 0.99`.
- the safe read reports the same-row intersection, not separate row counts.

## Current Runner Packet

- [`scripts/grown_transfer_basin_live_packet.py`](../scripts/grown_transfer_basin_live_packet.py)
  is the cache-backed live packet verifier (`PASS=5 FAIL=0`). It checks the current note
  wording and the fresh cached stdout for the two slow replay runners below,
  while explicitly keeping the scope at finite-row support rather than a
  graph-ladder theorem.
- [`scripts/GROWN_TRANSFER_BASIN_SWEEP.py`](../scripts/GROWN_TRANSFER_BASIN_SWEEP.py)
- [`scripts/GROWN_TRANSFER_BASIN_TARGETED.py`](../scripts/GROWN_TRANSFER_BASIN_TARGETED.py)
- [`logs/runner-cache/GROWN_TRANSFER_BASIN_SWEEP.txt`](../logs/runner-cache/GROWN_TRANSFER_BASIN_SWEEP.txt)
- [`logs/runner-cache/GROWN_TRANSFER_BASIN_TARGETED.txt`](../logs/runner-cache/GROWN_TRANSFER_BASIN_TARGETED.txt)

Both runners declare long audit timeouts because the 3-seed propagation replay
is slow enough to timeout under the legacy 120-second default.

Both runner caches were regenerated after the `PW` reconciliation and
away-sign predicate repair.

## Results

The full 3x3 sweep now exits cleanly:

```text
SAFE READ
  signed-source survivors: 9/9
  complex-action survivors: 9/9
  same-row survivors: 9/9
  narrow basin has rows surviving both observables
```

The four-row targeted checker also exits cleanly:

```text
SAFE READ
  nearby rows surviving both observables: 4/4
  the prior grown-row positives survive on a narrow nearby basin
```

The row values are not imported constants. They are recomputed by
`_score_row(drift, restore)`, which builds the grown geometry through
`scripts/gate_b_grown_joint_package.py`, propagates the signed-source and
complex-action amplitudes, and then applies the shared row predicates.

## Boundaries

This packet is not a verdict-grade claim. It is bounded support for re-audit
of the narrow grown-transfer basin after the executable criterion mismatch has
been repaired.

Remaining audit questions:

- whether the cited grown-geometry helper dependency is acceptable for this
  bounded row packet;
- whether the finite row grid is the right audited scope;
- whether the old archived note should remain archived while this repaired
  packet becomes the live source.
