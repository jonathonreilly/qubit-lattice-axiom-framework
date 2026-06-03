# Massless Vector Null-Quotient Exact Linear Algebra Theorem

**Date:** 2026-06-03
**Type:** exact theorem
**Claim type:** exact-support
**Author-surface status:** exact-support; positive retained candidate for
independent audit.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict and does not update any audit ledger status.
**Primary runner:** [`scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py`](../scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py)
**Cached output:** [`logs/runner-cache/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.txt`](../logs/runner-cache/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.txt)

## Claim boundary

This note proves a pure finite-dimensional complex-linear-algebra identity.
It does not assert that the vector space is physical spacetime, that the
bilinear form is a framework-derived Lorentzian metric, that `k` is a physical
momentum, that `epsilon` is a field polarization, that `L_k(epsilon)=0` is a
Lorenz-gauge condition, or that the quotient is a physical photon/gluon/gauge
boson state space.

The physical QFT identifications remain outside this note. Those admissions
are still carried by
`MASSLESS_VECTOR_POLARIZATION_COUNT_FROM_LORENTZ_AND_GAUGE_BOUNDED_THEOREM_NOTE_2026-05-28.md`.
The purpose of the present note is only to retire the imported textbook
linear-algebra step by proving the quotient dimension natively as a theorem.

## Theorem

Let `V = C^4`, and let `eta` be the nondegenerate symmetric bilinear form with
matrix

```text
eta = diag(1, -1, -1, -1).
```

For a nonzero vector `k in V` satisfying the null condition
`eta(k, k) = 0`, define the linear functional

```text
L_k : V -> C,
L_k(epsilon) = eta(k, epsilon).
```

Then

```text
span_C{k} subset ker(L_k)
```

and the quotient has complex dimension

```text
dim_C(ker(L_k) / span_C{k}) = 2.
```

## Proof

Because `eta` is nondegenerate, the functional `L_k = eta(k, -)` is zero only
when `k = 0`. The theorem assumes `k != 0`, so `L_k` is a nonzero linear
functional from a four-dimensional complex vector space to `C`. Therefore
`rank(L_k) = 1`, and rank-nullity gives

```text
dim_C ker(L_k) = dim_C V - rank(L_k) = 4 - 1 = 3.
```

The null condition gives

```text
L_k(k) = eta(k, k) = 0.
```

Thus `k in ker(L_k)`. Since `k != 0`, the subspace `span_C{k}` is
one-dimensional and lies inside `ker(L_k)`. Therefore

```text
dim_C(ker(L_k) / span_C{k})
  = dim_C ker(L_k) - dim_C span_C{k}
  = 3 - 1
  = 2.
```

This proves the claim. No plane-wave decomposition, gauge orbit, gauge-fixing
choice, field equation, Standard Model inventory, observed value, fitted
constant, or literature theorem is used. The only hypotheses are the
four-dimensional complex vector space, the nondegenerate bilinear form, and a
nonzero null vector.

## Exact examples

The runner checks the theorem with exact rational arithmetic for several
nonzero null vectors in the displayed form:

```text
(1, 0, 0, 1)
(5, 3, 4, 0)
(13, 12, 0, 5)
(25, 7, 24, 0)
```

For each vector it verifies:

- `eta(k, k) = 0`;
- the row matrix for `L_k` has rank `1`;
- `dim ker(L_k) = 3`;
- `k` lies in `ker(L_k)`;
- `span_C{k}` has dimension `1`;
- `dim(ker(L_k) / span_C{k}) = 2`.

It also checks the massive/non-null contrast: if `eta(k, k) != 0`, then
`k` is not in `ker(L_k)`, so the quotient by `span_C{k}` is not the same
linear-algebra object.

## What this can close

If independent audit accepts this note, the algebraic core

```text
dim_C ker(k_mu epsilon^mu) / span{k^mu} = 2
```

can be cited as a one-hop exact theorem by the older massless-vector
polarization note. That moves the quotient identity itself out of textbook
import territory.

## What this does not close

This note does not close the physical massless-vector theorem by itself. In
particular it does not derive:

- physical Lorentzian spacetime from the framework;
- a free massless vector field;
- a plane-wave/Fourier decomposition;
- continuous gauge redundancy;
- Lorenz gauge or any other gauge slice;
- a photon, gluon, or gauge boson interpretation;
- an adjoint gauge-boson multiplicity;
- a contribution to a thermal `g_*` inventory.

Those are downstream bridge questions. This note supplies only the exact
linear-algebra quotient theorem that those bridge questions may consume.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
python3 scripts/cached_runner_output.py --refresh scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
python3 scripts/cached_runner_output.py --check-only scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
```

Expected result:

```text
SUMMARY: PASS=56 FAIL=0
VERDICT: EXACT-SUPPORT
```
