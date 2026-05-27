# Gate B Grown-Geometry Joint Package Note

**Date:** 2026-04-05 (audit-narrowing refresh: 2026-05-10; cache
reconciliation refresh: 2026-05-27)
**Claim type:** bounded_theorem
**Status:** bounded support theorem for the runner-defined Born /
interference / decoherence numerical comparison between exact grid and grown
geometry on the declared `h = 0.5`, `drift = 0.2`, `restore = 0.7` row, with
`drift = 0.3`, `restore = 0.5` as a stress row, on four seeds.
**Script:** [`scripts/gate_b_grown_joint_package.py`](../scripts/gate_b_grown_joint_package.py)
(C-class runner)
**Runner cache:** [`logs/runner-cache/gate_b_grown_joint_package.txt`](../logs/runner-cache/gate_b_grown_joint_package.txt)

## Audit boundary

The independent audit verdict on this row is `audited_conditional`. The
2026-05-27 auditor found the only remaining local repair target to be stale
Born means in this note relative to the current SHA-pinned runner cache. This
refresh reconciles the frozen values to the cache without changing the runner
or expanding the claim.

The runner is non-print-only: it constructs the geometries, propagates
amplitudes, and computes Born / `d_TV` / MI / decoherence directly. The
bounded numerical comparison is supported by the current cache for that runner.

Current one-hop dependencies:

- [`docs/GATE_B_FARFIELD_NOTE.md`](GATE_B_FARFIELD_NOTE.md)
  (`claim_type: bounded_theorem`, `effective_status: retained_bounded`) —
  cited for the bounded far-field sign / `F ~ M` certificate on the same
  generated-geometry family, under runner-defined source, propagation, and
  readout ingredients only.
- [`docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
  (`claim_type: bounded_theorem`, `effective_status: retained_bounded`) —
  cited for the bounded distance-law fit on the same row. Retained-bounded,
  cross-confirmed.

This note's load-bearing claim is narrowed to the bounded numerical Born /
`d_TV` / MI / decoherence comparison on the declared scope. The broader
"package transfers as Gate B closure" reading is not part of this claim: this
note does not derive the grown-geometry rule, the source law, the propagation
kernel, the valley-linear action, or the physical-gravity readout from accepted
primitives.

## Artifact chain

- [`scripts/gate_b_grown_joint_package.py`](../scripts/gate_b_grown_joint_package.py)
- [`logs/runner-cache/gate_b_grown_joint_package.txt`](../logs/runner-cache/gate_b_grown_joint_package.txt)
  — current SHA-pinned audit-lane cache for the runner
- [`logs/2026-04-05-gate-b-grown-joint-package.txt`](../logs/2026-04-05-gate-b-grown-joint-package.txt)
  — historical frozen run superseded numerically by the current cache for
  audit packet construction

## Question

Do the non-gravity observables also transfer from the exact grid to the grown
geometry on the retained generated-geometry family?

This note freezes:

- Born
- `d_TV`
- `MI`
- CL-bath decoherence

on:

- exact grid
- grown geometry at `drift = 0.2`, `restore = 0.7`
- noisier grown geometry at `drift = 0.3`, `restore = 0.5` as a stress row

## Frozen result

The current SHA-pinned runner cache reports mean values across `4` seeds:

```text
geometry                 Born     d_TV       MI    Decoh
exact grid           2.06e-15    0.787    0.568    49.4%
grown drift=0.2      2.23e-15    0.811    0.569    49.4%
grown drift=0.3      2.63e-15    0.790    0.446    47.2%
```

The moderate-drift grown row stays extremely close to the exact grid:

- exact grid: Born `2.06e-15`, `d_TV = 0.787`, `MI = 0.568`,
  decoherence `49.4%`
- grown `drift = 0.2`, `restore = 0.7`: Born `2.23e-15`,
  `d_TV = 0.811`, `MI = 0.569`, decoherence `49.4%`

The noisier `drift = 0.3` stress row remains useful as a boundary read:

- Born `2.63e-15`
- `d_TV = 0.790`
- `MI = 0.446`
- decoherence `47.2%`

## Safe read

The honest bounded statement is:

- on the declared moderate-drift generated-geometry row, the non-gravity joint
  observables transfer well from the exact grid
- the moderate-drift row matches the exact grid almost exactly on Born, `MI`,
  and decoherence, and stays close on `d_TV`
- the noisier grown row shows that the transfer is not trivial under arbitrary
  growth noise: Born remains clean, while `MI` weakens first

This is exactly the kind of boundary skeptical readers need:

- one retained moderate-drift positive row
- one noisier stress row that degrades without collapsing everything at once

## Relation to Gate B (cross-references)

Read this with:

- [`docs/GATE_B_FARFIELD_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/GATE_B_FARFIELD_NOTE.md)
  (`audit_status: audited_conditional`) — far-field gravity sign / `F ~ M`
  bounded harness positive on the same generated-geometry family;
  one-hop dep of this note.
- [`docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
  (`effective_status: retained_bounded`) — bounded distance-law tail fit on
  the same row, cross-confirmed; one-hop dep of this note.

Together they support a *bounded numerical* package read on the moderate-drift
row:

- the far-field harness reports gravity sign / `F ~ M` (conditional on the
  runner-defined bounded ingredients in the upstream `gate_b_farfield_note`
  row)
- the distance-law fit on the bounded `z = 3..7` window is retained-bounded
- Born / `d_TV` / MI / decoherence stay close between exact grid and grown
  geometry on the four-seed comparison run by this runner

That is a bounded numerical observation on the declared scope, **not** a
"Gate B package transfer" closure. The remaining open step has two parts: how
broadly that comparison survives across the full generated-geometry family,
and the primitive-to-physical-gravity bridge for interpreting the far-field
readout physically. Both remain outside this note.
