# Gate B Grown-Geometry Joint Package Note

**Date:** 2026-04-05 (audit-narrowing refresh: 2026-05-10;
runner-cache reconciliation: 2026-05-27)
**Type:** bounded_theorem
**Status:** bounded Born / interference / decoherence numerical comparison
between exact grid and grown geometry on the declared `h = 0.5`,
`drift = 0.2`, `restore = 0.7` row, with `drift = 0.3`, `restore = 0.5` as
a stress row, on four seeds.
**Status authority:** independent audit lane only.
**Script:** [`scripts/gate_b_grown_joint_package.py`](../scripts/gate_b_grown_joint_package.py)
**Runner cache:** [`logs/runner-cache/gate_b_grown_joint_package.txt`](../logs/runner-cache/gate_b_grown_joint_package.txt)

## Audit boundary (2026-05-27)

The prior independent audit verdict was `audited_conditional` because this
source note's runner-cache artifact and dependency-status prose drifted from
the live runner and ledger. This refresh does not apply an audit verdict. It
only reconciles the source note to the current locally replayed runner and
current dependency metadata so the independent audit lane can re-audit the
same bounded scope.

The runner is non-print-only: it constructs the geometries, propagates
amplitudes, and computes Born / `d_TV` / MI / decoherence directly. The
bounded numerical comparison is the runner-cache certificate, not the
historical frozen log.

The current one-hop dependencies are:

- [`GATE_B_FARFIELD_NOTE.md`](GATE_B_FARFIELD_NOTE.md)
  (`claim_type: bounded_theorem`, `effective_status: retained_bounded`) —
  cited for the bounded far-field gravity sign / `F ~ M` finite harness on
  the same generated-geometry family.
- [`GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
  (`claim_type: bounded_theorem`, `effective_status: retained_bounded`) —
  cited for the bounded distance-law fit on the same row. Retained-bounded,
  cross-confirmed.

This note's load-bearing claim is narrowed to the bounded numerical Born /
`d_TV` / MI / decoherence comparison on the declared scope. The broader
"package transfers as Gate B closure" reading remains out of scope even
though the two cited finite-harness dependencies are retained-bounded.

## Artifact chain

- [`scripts/gate_b_grown_joint_package.py`](../scripts/gate_b_grown_joint_package.py)
- [`logs/runner-cache/gate_b_grown_joint_package.txt`](../logs/runner-cache/gate_b_grown_joint_package.txt)
- [`logs/2026-04-05-gate-b-grown-joint-package.txt`](../logs/2026-04-05-gate-b-grown-joint-package.txt)
  is retained as a historical run log only; the runner cache is the current
  audit artifact.

## Question

Do the non-gravity observables also transfer from the exact grid to the grown
geometry on the declared generated-geometry family?

This note freezes:

- Born
- `d_TV`
- `MI`
- CL-bath decoherence

on:

- exact grid
- grown geometry at `drift = 0.2`, `restore = 0.7`
- noisier grown geometry at `drift = 0.3`, `restore = 0.5` as a stress row

## Current runner-cache result

The current local runner replay reports mean values across `4` seeds.

The declared moderate-drift grown row stays extremely close to the exact grid:

- exact grid: Born `2.12e-15`, `d_TV = 0.787`, `MI = 0.568`,
  decoherence `49.4%`
- grown `drift = 0.2`, `restore = 0.7`: Born `2.19e-15`,
  `d_TV = 0.811`, `MI = 0.569`, decoherence `49.4%`

The noisier `drift = 0.3` stress row remains useful as a boundary read:

- Born `2.45e-15`
- `d_TV = 0.790`
- `MI = 0.446`
- decoherence `47.2%`

The refreshed runner has a source-note replay self-check pinned to the values
above, with a relative Born tolerance for platform-level libm cancellation
drift and tight absolute tolerances on `d_TV`, MI, and decoherence.

## Safe read

The honest bounded statement is:

- on the declared moderate-drift generated-geometry row, the non-gravity joint
  observables transfer well from the exact grid
- the moderate-drift row matches the exact grid almost exactly on Born, `MI`,
  and decoherence, and stays close on `d_TV`
- the noisier grown row shows that the transfer is not trivial under arbitrary
  growth noise: Born remains clean, while `MI` weakens first

This is exactly the kind of boundary skeptical readers need:

- one declared moderate-drift positive row
- one noisier stress row that degrades without collapsing everything at once

## Relation to Gate B (cross-references)

Read this with:

- [`GATE_B_FARFIELD_NOTE.md`](GATE_B_FARFIELD_NOTE.md)
  (`effective_status: retained_bounded`) — far-field gravity sign / `F ~ M`
  bounded harness positive on the same generated-geometry family; one-hop dep
  of this note.
- [`GATE_B_GROWN_DISTANCE_LAW_NOTE.md`](GATE_B_GROWN_DISTANCE_LAW_NOTE.md)
  (`effective_status: retained_bounded`) — bounded distance-law tail fit on
  the same row, cross-confirmed; one-hop dep of this note.

Together they support a *bounded numerical* package read on the moderate-drift
row:

- the far-field harness reports gravity sign / `F ~ M` on its bounded finite
  harness scope
- the distance-law fit on the bounded `z = 3..7` window is retained-bounded
- Born / `d_TV` / MI / decoherence stay close between exact grid and grown
  geometry on the four-seed comparison run by this runner

That is a bounded numerical observation on the declared scope, **not** a
"Gate B package transfer" closure. The remaining open step has two parts:
how broadly that comparison survives across the full generated-geometry
family, *and* the upstream primitive-to-physical-gravity bridge that the
farfield dep is itself flagged on. Both are recorded as deferred to the
upstream rows.
