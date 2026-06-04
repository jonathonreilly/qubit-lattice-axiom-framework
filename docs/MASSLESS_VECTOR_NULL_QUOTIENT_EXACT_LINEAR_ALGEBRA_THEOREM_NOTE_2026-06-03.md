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

## No-go discipline gate (N1-N8)

**Status:** PASS for the exact-support scope only. This note is primarily a
positive exact identity (`dim_C(ker L_k / span_C{k}) = 2`), but it carries
several boundary-foreclosure statements that require the no-go discipline:
the word "null" in the hypothesis and title, the "exact"/"exact-support"
framing, the explicit "What this does not close" foreclosure list, and the
massive/non-null contrast ("if `eta(k, k) != 0` ... not the same linear-algebra
object"). The claim being asserted is the single quotient-dimension equality
for a nonzero null vector in `(C^4, eta)`; the foreclosures only deny that
this equality on its own supplies any physical or non-null content. Nothing
here is a no-go against the physical photon count, against the massive-vector
count, or against any bridge derivation.

### N1 - Alternative route enumeration

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Rank-nullity route | Derive `dim ker(L_k) = 2` directly (skip the `span{k}` quotient). | `L_k` is a single nonzero functional, so `rank = 1` and `dim ker = 3`; the value `2` is only reached after quotienting by `span{k}`, which needs `k in ker(L_k)` (the null condition). | ATTEMPTED |
| Drop-the-null-condition route | Get the same quotient `ker(L_k)/span{k} = 2` without `eta(k,k)=0`. | If `eta(k,k) != 0` then `L_k(k) = eta(k,k) != 0`, so `k notin ker(L_k)` and `span{k}` is not a subspace of the kernel; the displayed quotient is then not even defined the same way (this is exactly the massive/non-null contrast the runner checks). | ATTEMPTED |
| Degenerate-form route | Allow `eta` degenerate so `L_k` can be the zero functional. | A degenerate `eta` can make `rank(L_k) = 0` and `dim ker = 4`, breaking the `4 - 1 - 1 = 2` count; nondegeneracy of `eta` is an explicit hypothesis, not assumed silently. | ATTEMPTED |
| Real-scalar route | Reinterpret the components as real `R^4` / `R^8` to change the dimension count. | The theorem is stated and proved over `C`; `dim_C` is the asserted object. A real reading is a different (out-of-scope) count and is not what this note claims. | ATTEMPTED |
| Physical-import route | Read `k` as momentum, `epsilon` as polarization, the quotient as a photon state space, and call the `2` a derived physical polarization count. | The Claim boundary explicitly refuses every physical identification; those admissions stay in the 2026-05-28 bounded note. This note closes only the abstract quotient dimension. | ATTEMPTED |

### N2 - Wall-independence audit

The collapsed wall set for the exact equality has a single wall: the
nonzero null vector `k` in a nondegenerate `(C^4, eta)` forces
`rank(L_k) = 1` and `k in ker(L_k)`, so `dim_C(ker L_k / span{k}) = 3 - 1 = 2`.
The two visible reductions (the `-1` from `rank(L_k)` and the `-1` from
`span{k}`) are not two independent retained walls; they are two consequences
of the same hypothesis pair (`eta` nondegenerate, `k != 0`, `eta(k,k) = 0`).
The only thing that could change the count is changing those hypotheses
(degenerate `eta`, `k = 0`, or non-null `k`) — each of which moves the claim
to a different, explicitly out-of-scope object rather than refuting this one.

### N3 - Hidden-wall scan

The words "null", "exact", "exact-support", and "quotient" are not used as
hidden retained inputs for the result. The explicit load-bearing inputs are
exactly four and all appear in the Theorem statement: (i) the four-dimensional
complex vector space `V = C^4`; (ii) the nondegenerate symmetric bilinear form
`eta = diag(1,-1,-1,-1)`; (iii) a nonzero vector `k`; (iv) the null condition
`eta(k, k) = 0`. No spacetime metric, no momentum, no gauge group, no
plane-wave structure, and no Standard Model inventory is consumed — the Claim
boundary disclaims each of these by name.

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `MASSLESS_VECTOR_POLARIZATION_COUNT_FROM_LORENTZ_AND_GAUGE_BOUNDED_THEOREM_NOTE_2026-05-28.md` (audit-repair target) | The textbook-imported linear-algebra quotient step `4 - 1 - 1 = 2` inside the bounded physical theorem. | The same quotient dimension, proved natively as `dim_C(ker L_k / span{k}) = 2`. | yes |
| The bounded note's AC1-AC5 physical admissions (Lorentzian signature, gauge orbit, Lorenz gauge) | The physical QFT identification of the abstract structure. | NOT attacked here; this note explicitly leaves AC1-AC5 with the bounded note. | no |
| The parent g_star proof-walk premise P2 | The per-massless-vector polarization count as an unattributed admission. | NOT load-bearing here; this note reaches only the abstract `2`, not the physical polarization count. | no |

The non-matching witnesses are listed only to mark scope; they are not used
as load-bearing support for this exact identity.

### N5 - Rhetoric audit

"Null" is scoped to the algebraic condition `eta(k, k) = 0` on a vector in
`(C^4, eta)`, not to a physical null/light-like momentum. "Exact" and
"exact-support" are scoped to the use of exact rational arithmetic in the
runner and to the status-lane claim type, not to any assertion that this is
the *only* route to the count `2` (the bounded note's Wigner little-group path
reaches the same `2` independently). The massive/non-null contrast ("not the
same linear-algebra object") is scoped to the displayed `span{k}`-quotient
construction when `k notin ker(L_k)`; it is not a claim that no count exists in
the non-null case (the standard non-null count is `4 - 1 = 3`, owned by the
bounded note's R8). Read over-broadly — as "this forecloses the physical photon
count" or "no non-null analysis is possible" — the claim would be wrong; that
reading is disclaimed.

### N6 - Partial-closure path scan

Open non-axiom partial-closure paths remain for everything this note declines
to derive: a framework derivation of the Lorentzian signature, of the
continuous gauge orbit, of the Lorenz-gauge slice, and of the physical
photon/gluon identification are all live downstream bridge questions. This note
calls none of them a new axiom; it only supplies the abstract quotient theorem
that such a bridge may one-hop consume. The abstract-to-physical bridge is a
positive open task, not a closure.

### N7 - Steelman

The strongest objection is that the displayed count `2` looks like it depends
on the specific signature `diag(1,-1,-1,-1)`, so a reader might claim the
theorem secretly imports Lorentzian physics. It does not: the proof uses only
(a) nondegeneracy of `eta` (to force `rank(L_k) = 1`) and (b) the null
condition `eta(k,k) = 0` (to force `k in ker(L_k)`). Any nondegenerate
symmetric form on `C^4` admitting a nonzero isotropic vector gives the same
`3 - 1 = 2`; over `C` every nondegenerate symmetric bilinear form of dimension
`>= 2` admits such a vector, so the displayed signature is a representative,
not a hidden physical premise. The steelman blocks any claim that the count is
signature-derived physics; it does not break the scoped algebraic equality.

### N8 - Cross-cycle echo

The repo's recurrent overclaim failure mode is to verify one representative
witness (here, one specific null vector such as `(1,0,0,1)`, or one signature
convention) and then declare a whole physical lane closed. This note avoids
that echo two ways: the runner checks the identity across multiple distinct
null vectors and the massive/non-null contrast rather than a single case, and
the Claim boundary plus "What this does not close" keep the claim pinned to the
abstract quotient dimension, explicitly refusing every physical lane closure.
The exact-support claim is the linear-algebra equality only; no
photon-count, massive-vector, or bridge lane is foreclosed.

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
