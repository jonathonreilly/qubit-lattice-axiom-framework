# DM Leptogenesis PMNS Fixed-Chart Hermitian Block Parity Theorem

**Date:** 2026-04-16; fixed-chart parity repair 2026-05-25
**Status:** bounded-support formal matrix algebra. No reduced `N_e` surface
authority, favored-column closure, eta normalization, relative-action selector,
KKT branch classification, or stationary-branch minimality is part of the
binding theorem.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_dm_pmns_he_parity_repair.py`
**Status authority:** independent audit lane only.

## Actual claim

Let `x_1,x_2,x_3,y_1,y_2,y_3` be real coordinates and let `delta` be a real
phase. Define the supplied fixed-chart matrix

```text
Y(delta) =
[[x1,          y1, 0],
 [0,           x2, y2],
 [y3 exp(i delta), 0, x3]].
```

Set

```text
H_e(delta) = Y(delta) Y(delta)^dagger.
```

Then

```text
H_e(delta) =
[[x1^2+y1^2,              x2 y1,        x1 y3 exp(-i delta)],
 [x2 y1,                  x2^2+y2^2,    x3 y2],
 [x1 y3 exp(i delta),     x3 y2,        x3^2+y3^2]].
```

Moreover,

```text
H_e(-delta) = conjugate(H_e(delta)).
```

Therefore every scalar readout invariant under entrywise complex conjugation
of this Hermitian block is even in `delta`; for example, the trace, trace
square, determinant, characteristic polynomial coefficients, eigenvalue
multiset, and Frobenius norm are unchanged under `delta -> -delta`.

That fixed-chart Hermitian-block formula and conjugation parity are the entire
repaired theorem.

## Why This Repair Is Narrow

The prior judicial audit accepted the displayed `H_e` formula and
`delta -> -delta` parity as algebraic, but kept the row conditional because
the selector conclusion imported helper machinery: reduced `N_e` surface
authority, seed averages, favored-column closure functional, eta normalization,
and relative-action/KKT branch selection.

This repair withdraws that selector conclusion from the binding claim. It
preserves only the matrix-algebra theorem that closes from the supplied
fixed-chart definition of `Y(delta)`.

The prior sampled KKT/action-gap diagnostic is intentionally not part of this
binding row. If that sampled diagnostic is needed downstream, it should be
rebuilt as a separate runner-backed bounded diagnostic with its own assumptions
and audit queue entry.

## Theorem

**Theorem.** For the supplied fixed-chart matrix `Y(delta)` above,
`H_e(delta)=Y(delta)Y(delta)^dagger` has the displayed entries and satisfies
`H_e(-delta)=conjugate(H_e(delta))`.

**Proof.** Multiplying `Y(delta)` by its adjoint gives:

```text
H11 = x1^2 + y1^2
H22 = x2^2 + y2^2
H33 = x3^2 + y3^2
H12 = x2 y1
H23 = x3 y2
H13 = x1 y3 exp(-i delta)
H31 = x1 y3 exp(i delta).
```

The only phase-dependent entries are `H13` and `H31`, and replacing
`delta` by `-delta` swaps `exp(i delta)` with `exp(-i delta)`. Since all
`x_i,y_i` are real, this is exactly entrywise complex conjugation of the
Hermitian block. Any scalar function unchanged by entrywise conjugation is
therefore even in `delta` on this supplied chart. QED.

## What This Row Does Not Claim

- It does not derive the fixed `N_e` reduced surface from the framework.
- It does not derive seed averages, favored-column closure, eta normalization,
  or a PMNS value law.
- It does not define or derive a relative-action selector.
- It does not classify stationary KKT branches or prove branch minimality.
- It does not compute a leptogenesis abundance or select a physical PMNS
  column.
- It does not add an axiom or apply an audit verdict.

The bridge from this fixed-chart parity algebra to the full PMNS-assisted
leptogenesis selector remains a separate open science problem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_he_parity_repair.py
```

Expected result:

```text
DM/PMNS fixed-chart Hermitian-block parity repair
TOTAL: PASS=33 FAIL=0
```
