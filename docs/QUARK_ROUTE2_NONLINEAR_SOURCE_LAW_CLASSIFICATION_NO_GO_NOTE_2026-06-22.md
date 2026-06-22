# Quark Route-2 Nonlinear Source-Law Classification No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for the broad nonlinear same-domain shortcut
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_nonlinear_source_law_classification_no_go_2026_06_22.py`

Actual current-surface status: no-go for the broad nonlinear same-domain shortcut.

## Scope

This block follows the finite Schur-polynomial no-go and the direct
inverse-square dualization stretch attempt:

- [`QUARK_ROUTE2_FINITE_SCHUR_LAW_P2_GATE_NO_GO_NOTE_2026-06-21.md`](QUARK_ROUTE2_FINITE_SCHUR_LAW_P2_GATE_NO_GO_NOTE_2026-06-21.md)
- [`QUARK_ROUTE2_DIRECT_INVERSE_SQUARE_DUALIZATION_STRETCH_NO_GO_NOTE_2026-06-22.md`](QUARK_ROUTE2_DIRECT_INVERSE_SQUARE_DUALIZATION_STRETCH_NO_GO_NOTE_2026-06-22.md)

It asks whether a broader nonlinear same-domain weight law can force the
Route-2 endpoint without adding the two-sided unit-dual premise or fitting the
endpoint.

This is not an audit verdict. It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Target

The same-domain weights are

```text
w_E = 1/3
w_T = 1/2
```

and the endpoint requires

```text
q_E/q_T = 9/4.
```

For a pure power law

```text
q_X proportional to w_X^-p
```

the target is equivalent to `p = 2`.

## Nonlinear Classification

The runner checks four broader law families.

| Family | Result |
|---|---|
| Multiplicative power laws | Exact covariance permits every exponent `p`; target inversion selects `p=2` but this imports `q_E/q_T=9/4`. |
| Two-bin monomials `w^a(1-w)^b` | Exact integer solve gives the unique target solution `(a,b)=(-2,0)`, i.e. inverse-square again. |
| Reciprocal / complement / odds controls | Natural nonlinear controls miss the target unless they collapse to `w^-2`. |
| Free-coefficient nonlinear interpolation | Can fit `9/4`, but only by choosing coefficients after the target equation is imposed. |

The two-bin monomial result is useful because it rules out a common escape.
Equivalently, the tested two-bin monomials do not provide a second mechanism:
adding a complement factor `(1-w)^b` does not create a new target mechanism.
The target equations force `b=0` and `a=-2`.

## Boundary

The pruned shortcut is:

```text
broad nonlinear same-domain law class => endpoint ratio
```

without an independent exponent or coefficient selector.

The remaining positive target is unchanged but sharper:

```text
derive inverse-square as a physical source/readout theorem,
derive two unit canonical-dual charges,
or provide a new same-domain nonlinear principle whose coefficients are fixed
without using q_E/q_T=9/4.
```

This note does not rule out future nonlinear laws. It rules out using the
tested nonlinear grammars as if they already derive the endpoint.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonlinear_source_law_classification_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=53, FAIL=0
```
