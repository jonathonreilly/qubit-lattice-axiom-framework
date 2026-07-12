# Gate B Connectivity Tolerance Note

**Date:** 2026-04-04  
**Type:** bounded_theorem
**Status:** bounded Gate B replay frozen on disk, not a dynamics theorem

## One-line read

Within this frozen finite replay, and under the supplied Gate B harness choices
recorded below, the replay supports two narrow diagnostic observations:

- the six-point fixed-connectivity jitter sweep is nonmonotonic and includes
  both positive and negative mean detector-window gains
- the architecture comparison also gives mixed outcomes, but it changes
  geometry and, for the K-NN case, connectivity together

Read strictly inside that finite harness, the replay does not isolate
connectivity as the cause of the mixed response and does not rank connectivity
against position noise as an intrinsic Gate B bottleneck. It motivates a
controlled comparison; it does **not** close Gate B.

## Primary artifact

- Script: [`scripts/gate_b_connectivity_tolerance.py`](../scripts/gate_b_connectivity_tolerance.py)
- Log: [`logs/2026-04-04-gate-b-connectivity-tolerance.txt`](../logs/2026-04-04-gate-b-connectivity-tolerance.txt)

## What was compared

The replay keeps the same valley-linear propagation law fixed and compares a
small architecture set:

- ordered lattice baseline
- jittered lattice with fixed connectivity
- templated growth with fixed-offset connectivity
- K-NN grown geometry
- snapped/grid-like connectivity

The main readout in this replay is a mass-side detector-window gain. The
`F~M` column in the log is a local response-slope probe, not a promoted
universal theorem.

## Frozen replay result

| architecture | toward | mean delta | local `F~M` |
|---|---:|---:|---:|
| ordered lattice | `66.7%` | `+0.000012` | `0.66` |
| jittered lattice | `75.0%` | `+0.000005` | `0.75` |
| templated growth | `27.8%` | `-0.000016` | `0.27` |
| K-NN grown | `55.6%` | `+0.000006` | `0.55` |
| snapped/grid-like | `58.3%` | `-0.000002` | `0.58` |

The jitter sweep on fixed connectivity is the cleanest tolerance check:

| jitter | toward | mean delta | local `F~M` |
|---|---:|---:|---:|
| `0.00` | `66.7%` | `+0.000012` | `0.66` |
| `0.10` | `55.6%` | `+0.000003` | `0.55` |
| `0.20` | `66.7%` | `+0.000009` | `0.67` |
| `0.30` | `47.2%` | `-0.000010` | `0.47` |
| `0.40` | `50.0%` | `-0.000003` | `0.50` |
| `0.50` | `75.0%` | `+0.000005` | `0.75` |

## Safe interpretation (finite replay only)

Read as frozen-replay observations under the supplied harness, not as general
theorems or a causal comparison:

- The fixed-connectivity sweep is nonmonotonic across the six sampled jitter
  values and its mean detector-window gain changes sign.
- The architecture rows do not isolate connectivity: coordinate geometry changes
  across the comparison, and the K-NN row changes connectivity as well.
- The highest sampled jitter point does not show a terminal collapse, but the
  six points do not establish a monotonic tolerance law.
- The local response-slope probe stays in a bounded linear-response band across
  the swept points; that is a row-local diagnostic, not a universal law.

## What this is not

- A solved Gate B dynamics theorem.
- A proof that any growth rule will work.
- A proof that the current `F~M` values are universal constants.
- A replacement for the existing bounded Gate B prototype notes.

## Why it matters

This finite replay sharpens the next diagnostic task:

- compare fixed and recomputed connectivity on the same coordinates
- compare coordinate perturbations while holding the connectivity graph fixed

Those controls are needed before interpreting connectivity as a bottleneck or
choosing a growth rule on that basis. This is a finite-replay signpost, not a
general theorem.

## Audit scope firewall (2026-07-12)

2026-07-12 audit scope: finite connectivity replay, not dynamics closure. This
note cites the frozen replay numbers only inside the stated finite Gate B
harness. The physical inputs behind those numbers remain supplied Gate-B data,
tracked here with the shared supplied-residue vocabulary of
`GATE_B_DYNAMICS_NOTE.md`:

- `GB-S1b-b`: the physical scalar source/boundary/regulator/normalization remains supplied.
- `GB-S2b`: the physical detector-window/TOWARD/`F~M` semantics remain supplied.
- `GB-S3b`: the physical selection/dynamical generation of the connectivity stencil remains supplied.

Because those inputs are supplied row-local premises rather than cited retained
authorities, this note does not derive a Gate B dynamics theorem, supplies no
physical gravity/readout bridge, and introduces no new axiom, approved primitive,
or audit-status change. The "connectivity is the current bottleneck" reading is a
question for a controlled comparison, not a result of this finite replay.
