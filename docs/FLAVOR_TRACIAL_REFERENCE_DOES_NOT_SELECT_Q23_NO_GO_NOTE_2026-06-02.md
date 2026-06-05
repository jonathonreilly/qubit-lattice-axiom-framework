# Flavor Tracial Reference Does Not Select Q=2/3 No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Runner:** `scripts/flavor_tracial_reference_does_not_select_q23_no_go_2026_06_02.py`

This note tests a narrow value-route question: can the tracial/product/modular
reference route select the equal-block generation measure that gives `Q=2/3`?
It cannot. In the finite `Z_3` generation carrier, the tracial reference reads
central blocks by dimension, giving weights `(1,2)` and `Q=1`. The equal-block
read `(1,1)` gives `Q=2/3`, but it is a separate non-tracial state or sector
selector.

The framework baseline is
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). Lattice and
Quantum supply the finite carrier and matrix algebra used in the runner. Record
does not supply Born weights, a generation reference state, or a block-measure
choice.

## Result

For the real generation algebra `R[Z_3] = R (+) C`, the two central blocks have
real dimensions `1` and `2`. The Koide line checked by the runner is

```text
Q = 1/3 + (2/3) r.
```

Two measures sit on that line:

```text
dimension/tracial block weight (1,2) -> r = 1   -> Q = 1
equal real-block weight        (1,1) -> r = 1/2 -> Q = 2/3
```

The tracial state on the three-dimensional generation carrier is `rho = I_3/3`.
Its central-block state weights are

```text
Tr(rho e0) : Tr(rho e1) = 1/3 : 2/3 = 1 : 2.
```

The Tomita/KMS check for the trace is also trivial: the modular operator is
`Delta = 1`, so there is no non-trivial reweighting. Product/locality-style
factorization leaves the same generation-block weight for every tested region
size. These are all the same tracial route seen from different handles.

The equal-block state is admissible as a positive, `C_3`-invariant, unit-trace
matrix state, but it is not the trace. The runner exhibits it as a finite-gap
non-tracial density. That makes it a live chiral/sector/reference-state selector
target, not a consequence of the tracial route.

## Scope

This is not evidence against `Q=2/3`, and it does not choose the physical flavor
sector. It only says the tracial/product/modular route lands on the `Q=1`
dimension read and cannot be reused as the selector for the `Q=2/3` equal-block
read.

The `Q=2/3` route remains open through a chiral sector, non-tracial reference
state, finite-gap dynamics, or owner-approved block-measure admission.

## No-Go Discipline Gate

This gate applies only to the route above: deriving the `Q=2/3` equal-block
weight from a tracial/product/modular reference.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Tracial state route | Use `rho = I_3/3` to select the generation block weight. | It gives `(1,2)`, not `(1,1)`. |
| Modular route | Use KMS/Tomita flow to reweight the two blocks. | The trace has `Delta = 1`; no reweighting occurs. |
| Product/locality route | Let region factorization change the block count. | The tested product trace leaves `(1,2)` at every region size. |
| Positivity route | Use reflected or transfer positivity to rank `(1,2)` against `(1,1)`. | The tested positivity matrices are compatible with both candidate points. |
| Equal-block state route | Exhibit `(1,1)` directly. | It works as a separate non-tracial state, not as the trace. |
| Finite-gap route | Use a non-trivial Gibbs/reference gap to reach `(1,1)`. | This is a possible future selector, but it is extra input. |

### N2 - Wall Independence

The collapsed wall is a single reference-state/sector choice. Traciality,
trivial modular flow, and product factorization are not independent selectors;
they are different reads of the same tracial state.

### N3 - Hidden-Wall Scan

"Trace" means the finite matrix trace. "Modular" means the Tomita operator of
that trace. "Equal-block" means a different positive state on the same carrier.
No Record axiom, Born rule, chiral operator, or finite-temperature dynamics is
hidden inside the tracial route.

### N4 - Residual Matching

The residual is the generation-block reference choice: dimension count `(1,2)`
versus equal-block count `(1,1)`. It is not the algebraic existence of either
state and not the general Koide line.

### N5 - Rhetoric Audit

"Does not select" is scoped to the tracial/product/modular route. It does not
say `Q=2/3` is impossible, inconsistent, or disfavored as a chiral-sector value.

### N6 - Partial-Closure Path Scan

A chiral-sector theorem, a non-tracial reference-state derivation, a finite-gap
dynamics, or an explicit block-measure admission could still select `(1,1)`.
This note leaves those paths open.

### N7 - Steelman

A hostile reviewer can argue that the physical charged-lepton reference need not
be the trace. That is correct and is exactly the residual: a physical non-tracial
or chiral reference could select `(1,1)`. The tracial route still does not.

### N8 - Cross-Cycle Echo

Flavor notes repeatedly separate form/readout gates from value/weight gates.
This note keeps that split: the tracial reference is a clean comparator, while
the physical `Q=2/3` selector remains a separate sector or reference-state task.

**Gate result:** pass for the tracial-reference route only.

## Validation

The runner checks finite-matrix facts:

- `C^3 = I` and the central projectors have ranks `1` and `2`;
- the Koide line is `Q = 1/3 + (2/3)r`;
- the tracial state gives block weights `(1,2)` and `Q=1`;
- the equal-block state gives `(1,1)` and is non-tracial;
- the Tomita operator for the trace has trivial modular flow;
- a finite-gap non-tracial witness can reach `(1,1)`;
- the tested positivity matrices are compatible with both candidate weights;
- product-trace factorization leaves the generation-block weight unchanged.
