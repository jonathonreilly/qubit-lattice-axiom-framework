# Gate B Far-Field Cached Harness Certificate

**Date:** 2026-04-05; narrowed 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded cached-output certificate for the runner-defined h=0.5
far-field rows. This is not a physical Gate B bridge theorem.
**Runner:** [`scripts/gate_b_farfield_harness.py`](../scripts/gate_b_farfield_harness.py)

## Purpose

The prior row mixed a valid long-run numerical harness result with bridge
language about physical gravity. This repair keeps only the finite auditable
certificate:

```text
h = 0.5
W = 8
NL = 25
seeds = 12
z_masses = [3, 4, 5]
drift/restore rows = (0.3,0.5), (0.2,0.7), (0.1,0.9), exact grid
```

The cached harness output reports `36/36` TOWARD and `F~M = 1.00` on every
declared row.

## Bounded Claim

In the committed cache
`logs/runner-cache/gate_b_farfield_harness.txt`, the far-field harness reports:

| Row | TOWARD | F~M |
|---|---:|---:|
| `drift=0.3,rest=0.5` | `36/36` | `1.00` |
| `drift=0.2,rest=0.7` | `36/36` | `1.00` |
| `drift=0.1,rest=0.9` | `36/36` | `1.00` |
| `exact grid` | `36/36` | `1.00` |

The runner for this row parses that cache and verifies the declared scope,
row count, TOWARD counts, and slope values.

## Boundary

This row does not claim:

- that the growth rule is derived from accepted primitives;
- that the source law is derived from accepted primitives;
- that the propagation kernel or valley-linear action is derived from
  accepted primitives;
- that TOWARD/F~M is the physical gravity readout;
- clean Gate B far-field closure;
- a physical gravity or attraction theorem;
- any new axiom or audit verdict.

The primitive-to-physical-gravity bridge is separate science work. This row is
only a bounded cached numerical certificate for the runner-defined scenario.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gate_b_farfield_harness.py
```
