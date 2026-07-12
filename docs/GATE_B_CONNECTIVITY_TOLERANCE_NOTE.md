# Gate B Connectivity Tolerance Note

**Date:** 2026-04-04  
**Status:** bounded Gate B replay frozen on disk, not a dynamics theorem

## One-line read

Within this frozen finite replay, and under the supplied Gate B harness choices
recorded below, the replay supports a narrow bounded reading:

- on this fixed connectivity backbone, the swept position noise is tolerated
- once connectivity is recomputed from geometry, the sampled response becomes mixed

Read strictly inside that finite harness, connectivity structure — not position
noise — is where the sampled response first becomes mixed. That is a
finite-replay observation under the supplied choices, not a derived theorem that
connectivity is intrinsically the Gate B bottleneck, and it does **not** close
Gate B.

## Primary artifact

- Script: [`scripts/gate_b_connectivity_tolerance.py`](/Users/jonreilly/Projects/Physics/scripts/gate_b_connectivity_tolerance.py)
- Log: [`logs/2026-04-04-gate-b-connectivity-tolerance.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-gate-b-connectivity-tolerance.txt)

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
theorems:

- On this fixed connectivity backbone, the sampled response survives the swept
  position noise.
- Geometry-recomputed connectivity is where the sampled response first becomes
  mixed in this replay.
- The response does not show a cliff at jitter `0.5`; it degrades gradually
  across the swept points.
- The local response-slope probe stays in a bounded linear-response band across
  the swept points rather than collapsing.

## What this is not

- A solved Gate B dynamics theorem.
- A proof that any growth rule will work.
- A proof that the current `F~M` values are universal constants.
- A replacement for the existing bounded Gate B prototype notes.

## Why it matters

Within this finite replay the remaining Gate B gap looks sharper:

- across the swept points, position noise is not what mixes the response first
- recomputed connectivity is

Read as a finite-replay signpost and not a general theorem, the next growth rule
to try is not “more jitter tolerance” but a rule that produces structured
connectivity without turning the graph into a hand-imposed lattice.

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
physical gravity/readout bridge, and introduces no new axiom, Tier-A admission,
or audit-status change. The "connectivity is the current bottleneck" reading is a
finite-replay observation under those supplied choices, not a general theorem.
