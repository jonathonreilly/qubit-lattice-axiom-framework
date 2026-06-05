# Massless Vector Null Quotient Exact Linear Algebra Theorem

**Date:** 2026-06-03
**Claim type:** positive_theorem
**Claim scope:** pure finite-dimensional complex linear algebra: for `V = C^4` with nondegenerate symmetric bilinear form `eta = diag(1,-1,-1,-1)` and nonzero null vector `k`, the quotient `ker(L_k) / span_C{k}` has complex dimension `2`, where `L_k(epsilon) = eta(k, epsilon)`; no physical spacetime, momentum, gauge, Lorenz-slice, photon, gluon, or gauge-boson interpretation is asserted.
**Primary runner:** [`scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py`](../scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py)
(SUMMARY: PASS=55 FAIL=0).

This note sets no audit verdict and proposes no physical QFT bridge. It only
proves the abstract quotient dimension that a separate physical note may cite
after independent review.

---

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

and

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

No plane-wave decomposition, gauge orbit, gauge-fixing choice, field equation,
Standard Model inventory, observed value, fitted constant, or literature theorem
is used.

## Exact Runner Coverage

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

It also checks the non-null contrast: if `eta(k, k) != 0`, then `k` is not in
`ker(L_k)`, so the quotient by `span_C{k}` is not this theorem's object.

## Boundary

This theorem does not assert that:

- `V` is physical spacetime;
- `eta` is a framework-derived Lorentzian metric;
- `k` is physical momentum;
- `epsilon` is a field polarization;
- `L_k(epsilon)=0` is a Lorenz-gauge condition;
- quotienting by `span_C{k}` is a physical gauge orbit;
- the quotient is a physical photon, gluon, or gauge-boson state space;
- a downstream thermal `g_*` inventory is changed.

Those are separate physical bridge questions. This note proves only the
linear-algebra quotient dimension.

## No-Go Discipline Gate

**Status:** PASS for the boundary claims only. The theorem is positive; the
N1-N8 gate applies to the negative-sounding boundary statements above. The
closed claim is the abstract quotient equality, not any physical massless-vector
count.

### N1 - Alternative Route Enumeration

| route | what it would attempt | outcome | marker |
|---|---|---|---|
| Rank-nullity without quotient | Derive the value `2` from `ker(L_k)` alone. | A nonzero functional on `C^4` has a 3-dimensional kernel; the value `2` appears only after quotienting by `span_C{k}`. | ATTEMPTED |
| Drop the null condition | Use the same quotient when `eta(k,k) != 0`. | Then `L_k(k) != 0`, so `span_C{k}` is not a subspace of `ker(L_k)` and the displayed quotient is not the same object. | ATTEMPTED |
| Degenerate form route | Allow `eta` to be degenerate. | Degeneracy can make `L_k` zero for nonzero `k`, changing the rank-nullity count; nondegeneracy is an explicit hypothesis. | ATTEMPTED |
| Real-scalar read | Reinterpret the count over `R`. | The theorem asserts `dim_C`; a real-dimensional count is a different statement. | ATTEMPTED |
| Physical-gauge read | Treat `k`, `epsilon`, and the quotient as physical momentum, polarization, and gauge orbit. | The boundary section explicitly refuses those identifications; they require separate physical bridge work. | ATTEMPTED |

### N2 - Wall-Independence Audit

There is one collapsed wall for the equality: a nonzero null vector in a
nondegenerate four-dimensional complex bilinear space gives both
`rank(L_k)=1` and `k in ker(L_k)`. The two numerical subtractions are not
independent premises; they are consequences of the stated hypotheses.

### N3 - Hidden-Wall Scan

The load-bearing inputs are exhausted by the theorem statement: `V=C^4`,
nondegenerate `eta`, `k != 0`, and `eta(k,k)=0`. No spacetime metric,
momentum, gauge group, field equation, particle inventory, or empirical input is
used.

### N4 - Residual Matching

The residual addressed here is only the abstract quotient dimension
`dim_C(ker L_k / span_C{k}) = 2`. It matches the algebraic sub-step isolated by
the existing physical massless-vector note, but it does not match that note's
physical context residuals: Lorentzian spacetime, plane waves, gauge orbit, and
Lorenz-gauge interpretation remain outside this theorem.

### N5 - Rhetoric Audit

"Null" means the algebraic equation `eta(k,k)=0`, not physical lightlike
momentum. "Exact" means exact finite-dimensional linear algebra and exact
rational runner checks, not exact physical closure. "Not the same object" in
the non-null contrast means only that `span_C{k}` no longer lies in `ker(L_k)`;
it is not a claim that non-null vector fields have no polarization count.

### N6 - Partial-Closure Path Scan

The physical bridge can still be supplied by separate work: deriving a
Lorentzian metric, a field equation, a gauge orbit, a gauge slice, and a
particle interpretation would bypass this boundary because it would add the
physical structures this note intentionally omits. None of those paths is
called a new axiom here.

### N7 - Steelman

A hostile reviewer could argue that writing `diag(1,-1,-1,-1)` quietly imports
Lorentzian physics. The proof does not use physical Lorentzian structure; it
uses only nondegeneracy and the existence of a nonzero isotropic vector. The
displayed form is a convenient representative for the exact checks. That
steelman prevents any physical reading of the theorem, but it does not break the
abstract equality.

### N8 - Cross-Cycle Echo

The overclaim pattern to avoid is proving one algebraic witness and then
declaring a physical bridge solved. This note avoids that pattern by proving
only the quotient dimension and naming every omitted physical identification.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/massless_vector_null_quotient_exact_linear_algebra_2026_06_03.py
```

Expected result:

```text
SUMMARY: PASS=55 FAIL=0
VERDICT: EXACT-LINEAR-ALGEBRA
```
