# Source-Resolved Propagating Green Pocket

**Date:** 2026-04-05  
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** bounded-support exact-lattice same-site-memory positive packet;
proposed for independent audit, not audit-ratified.
**Primary runner:**
[`scripts/source_resolved_propagating_green_pocket.py`](../scripts/source_resolved_propagating_green_pocket.py)

This note freezes the smallest exact-lattice same-site-memory harness that
could still be compared directly against the static Green control and
the instantaneous `1/r` comparator.

## Setup

- exact 3D lattice: `h = 0.5`, `W = 3`, `L = 20`
- source cluster: clipped cross5 local cluster, leaving 4 in-bounds nodes
- source ladder: `s = {0.001, 0.002, 0.004, 0.008}`
- same-site memory field: Green-like layer recurrence with `mix = 0.9`
- control comparison: instantaneous `1/r` field and static source-resolved Green field

## Hard gates

The asserted exact-lattice run passes all requested gates:

- exact zero-source reduction: `0.0`
- all-TOWARD on the source ladder: `4/4`
- dynamic `F~M`: `1.00`
- mean `|dynamic/instantaneous|`: `1.420`
- mean `|dynamic/static Green|`: `1.149`

## Frozen values

| `s` | instantaneous shift | static Green shift | propagating shift | `prop/inst` | `prop/green` |
|---:|---:|---:|---:|---:|---:|
| `0.001` | `+1.713544e-03` | `+2.139974e-03` | `+2.460113e-03` | `1.436` | `1.150` |
| `0.002` | `+3.440703e-03` | `+4.279368e-03` | `+4.919670e-03` | `1.430` | `1.150` |
| `0.004` | `+6.936763e-03` | `+8.557987e-03` | `+9.837774e-03` | `1.418` | `1.150` |
| `0.008` | `+1.410179e-02` | `+1.712572e-02` | `+1.967434e-02` | `1.395` | `1.149` |

The instantaneous, static Green, and propagating responses all keep the same
weak-field sign and preserve linear mass scaling on this exact-lattice family.

## Causal observable

The same-site memory field is not identical to the static Green control:

- mean `prop - green = +1.197212e-03`

That is the smallest checked layer-memory observable in this pocket. It is
nontrivial, but it remains bounded and does not claim transverse transport, a
finite-speed field equation, or a full self-consistent GR sector.

## Safe read

This is a bounded exact-lattice positive:

- the same-site memory field keeps the weak-field `TOWARD` sign
- it preserves the Newtonian mass-scaling class on the tested source ladder
- it stays within the requested amplitude ratio band
- it is distinguishable from the static Green control by a small layer-memory
  offset

What it is **not**:

- a full self-consistent propagating-field theory
- a genuine transverse transport or finite-speed field model
- a horizon / black-hole result
- a claim that the generated geometry sector is closed
- audit-ratified status before independent audit

## Current assertion readout

The registered runner now asserts the finite packet:

```text
zero-source dynamic shift: +0.000000e+00
instantaneous F~M exponent: 1.01
static Green F~M exponent: 1.00
propagating Green F~M exponent: 1.00
TOWARD rows: 4/4
mean |prop/inst| ratio: 1.420
mean |prop/green| ratio: 1.149
causal memory observable (prop - green): +1.197212e-03
ASSERTIONS: PASS
```

## Audit dependency repair links

This graph-bookkeeping section records the one load-bearing upstream authority
used by the runner. It does not promote this note or change the audited claim
scope.

- [minimal_source_driven_field_probe_note](MINIMAL_SOURCE_DRIVEN_FIELD_PROBE_NOTE.md)

The exact-Green sibling `SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md` is useful
context, but it is not a load-bearing authority for this packet: the registered
runner constructs its own static Green control before comparing it to the
same-site memory field.
