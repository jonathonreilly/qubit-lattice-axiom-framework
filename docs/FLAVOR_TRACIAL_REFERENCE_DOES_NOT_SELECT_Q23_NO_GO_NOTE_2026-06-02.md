# Flavor Tracial Reference Does Not Select `Q=2/3` No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "the tracial/product/modular reference selects the equal-block `Q=2/3` measure".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_tracial_reference_does_not_select_q23_no_go_2026_06_02.py` (SCORECARD PASS=39).

## Closed Packet

This note assumes the finite `R[Z_3]=R(+)C` generation carrier and the displayed
Koide line/readout

```text
Q = 1/3 + (2/3) r.
```

Under that assumed carrier/readout surface, the tracial/product/modular route
does not select the equal-block measure that gives `Q=2/3`. It reads the two
central blocks by dimension, giving block weights `(1,2)`, hence `r=1` and
`Q=1`.

The packet does not derive that carrier, the physical flavor-sector
identification, or the physical mass readout from baseline axioms. Those are
open bridge questions outside this no-go.

## Direct Checks

1. **Central projectors close.** The cyclic generator satisfies `C^3=I`; the
   central projectors `e0=(I+C+C^2)/3` and `e1=I-e0` have ranks `1` and `2`.

2. **The two measure points are distinct.** On the displayed Koide line,
   dimension/tracial block weighting `(1,2)` gives `r=1`, `Q=1`; equal-block
   weighting `(1,1)` gives `r=1/2`, `Q=2/3`.

3. **The tracial state selects `(1,2)`.** For `rho=I_3/3`,
   `Tr(rho e0):Tr(rho e1)=1/3:2/3=1:2`.

4. **The equal-block state is admissible but non-tracial.** The runner exhibits
   a positive, `C3`-invariant, unit-trace state with equal block masses. It is a
   separate state, not the trace.

5. **Modular/product/positivity handles do not turn trace into equal-block.**
   The trace has trivial Tomita modular flow, product trace leaves the same
   generation-block ratio, and the tested reflection-positivity matrices are
   compatible with both candidate weights.

## Scope

This is not evidence against `Q=2/3`, and it does not choose the physical
flavor sector. It says only that the tracial/product/modular route, on the
assumed finite carrier/readout surface, lands on the dimension read and cannot
be reused as the selector for the equal-block read.

The `Q=2/3` route remains open through a chiral sector, non-tracial reference
state, finite-gap dynamics, or explicit block-measure admission.

## No-Go Discipline Gate

The no-go applies only to deriving the `Q=2/3` equal-block weight from a
tracial/product/modular reference.

Alternative routes remain open:

| Route | Status in this packet |
| --- | --- |
| Tracial state route | Gives `(1,2)`, not `(1,1)`. |
| Modular route | The trace has `Delta=1`; no reweighting occurs. |
| Product/locality route | Product trace leaves `(1,2)` at every tested region size. |
| Positivity route | Tested positivity matrices are compatible with both candidate points. |
| Equal-block state route | Works as a separate non-tracial state, not as the trace. |
| Finite-gap route | Possible future selector, but extra input. |

## Provenance

- The runner checks finite-matrix facts, the Koide-line arithmetic, tracial and
  equal-block states, trivial trace modular flow, product-trace factorization,
  and positivity agnosticism.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
