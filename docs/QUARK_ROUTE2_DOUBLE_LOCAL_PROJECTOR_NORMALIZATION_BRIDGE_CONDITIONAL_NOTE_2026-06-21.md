# Exact Signed-Axis Projector Decomposition and Integer-Monomial Theorem

**Date:** 2026-06-21
**Type:** positive_theorem
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py`](../scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py)
**Cached log:**
[`logs/runner-cache/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.txt)
**Dependencies:** none. The carrier, group action, rational arguments, and
integer exponent below are definitions or universally quantified theorem
arguments, not framework premises.

## 1. Defined six-arm representation

Let

```text
Omega = {+x,-x,+y,-y,+z,-z},                 V = Q^Omega.
```

Define `B_3` to be the set of all `3 x 3` signed permutation matrices. It
acts on `Omega` by ordinary matrix multiplication and therefore on `V` by
permuting coordinates. Direct enumeration gives `3! 2^3 = 48` distinct group
elements: 24 have determinant `+1` and 24 have determinant `-1`. The runner
checks all products, inverses, signed-axis images, unique matrices, and all
`48^2` representation products exactly.

This is an explicitly defined finite representation. The labels `A1`, `E`,
and `T1` below are names for three displayed rational subspaces; they carry no
physical identification.

## 2. Exact orthogonal projectors

Let `R` exchange each signed axis with its antipode, let `S=(I+R)/2`, and
let `J` be the all-ones `6 x 6` matrix. Define

```text
P_A1 = J/6,                 P_E = S - P_A1,                 P_T1 = I - S.
```

Their images have the following mutually orthogonal bases:

```text
A1: (1,1,1,1,1,1),
 E: (1,1,-1,-1,0,0), (1,1,1,1,-2,-2),
T1: (1,-1,0,0,0,0), (0,0,1,-1,0,0), (0,0,0,0,1,-1).
```

The six basis vectors are linearly independent, so they span `V`. Direct
multiplication proves

```text
P_X^T = P_X,                P_X^2 = P_X,
P_X P_Y = 0  (X != Y),      P_A1 + P_E + P_T1 = I.
```

Thus these are the unique orthogonal projectors onto the three displayed
subspaces. They commute with every matrix in the defined `B_3` action. Their
exact ranks, traces, and diagonal entries are

| projector | rank | trace | every diagonal entry |
|---|---:|---:|---:|
| `P_A1` | `1` | `1` | `1/6` |
| `P_E` | `2` | `2` | `1/3` |
| `P_T1` | `3` | `3` | `1/2` |

No floating-point reconstruction is used: the runner stores every projector
entry as an exact `Fraction` and separately reconstructs the matrices from the
three orthogonal bases.

## 3. Integer-exponent monomial family

For supplied positive rationals `u,v` and any supplied integer `p`, define

```text
lambda_p(u,v) = (u/v)^p.
```

Negative exponents use the ordinary exact reciprocal power. In the formal
instance `u=1/3`, `v=1/2`, one has `u/v=2/3`, and

```text
lambda_p(1/3,1/2) = 9/4    if and only if    p = -2.
```

This is a statement over all integers, not a finite scan. Let `nu_2` be the
2-adic valuation on positive rationals. Equality would imply

```text
p = p nu_2(2/3) = nu_2(9/4) = -2,
```

because `nu_2(2/3)=1`. Conversely, direct exact exponentiation at `p=-2`
gives `(2/3)^-2=9/4`. The independent oracle repeats the proof with the
3-adic valuation: `nu_3(2/3)=-1` and `nu_3(9/4)=2`, again forcing `p=-2`.

The equivalence classifies one equation inside the defined monomial family.
It does not select an exponent for any application and does not turn that
integer into a law.

## 4. Supplied affine arithmetic

For supplied exact rationals `lambda,q,d`, define

```text
q' = lambda q,                       rho = d(q' - 1).
```

This is an identity by definition. For the exact worked example

```text
lambda=9/4, q=5/6, d=6  ->  q'=15/8, rho=21/4.
```

The example is rational arithmetic only. The theorem does not identify these
arguments with a physical quantity and does not predict a physical endpoint.

## 5. Exact scope and application boundary

The theorem proves only the following finite mathematical facts:

1. the displayed signed-axis matrices form a 48-element group and an exact
   six-point permutation representation;
2. the three displayed matrices are the orthogonal projectors onto the three
   displayed subspaces, with ranks and diagonal entries as stated;
3. the defined rational monomial equation has the unique integer solution
   `p=-2`; and
4. the displayed affine formulas evaluate exactly on supplied arguments.

It does not select an exponent, does not select a normalization, does not
identify a physical source or readout, and does not predict a physical
endpoint. In particular, it supplies no law relating physical channel values
to projector diagonals, no source or tensor functional, no center-shell
covariance, no normalization rule, and no interpretation of `q'` or `rho`.
Any application must state those additional premises separately.

The theorem is invariant under audit censuses, queues, ledgers, row counts,
and other repository metadata. Those inventories are not theorem arguments.

## 6. Falsification and reproducibility

The standard-library runner provides:

- a normal exact construction with full group/cardinality/closure checks,
  projector idempotence, orthogonality, ranks, traces, diagonal values, basis
  action, and two prime-valuation uniqueness certificates;
- an independently coded antipodal-pair action enumeration, orthogonal-basis
  projector oracle, integer numerator/denominator power oracle over 54 varied
  rational cases, and affine common-denominator oracle; and
- hostile mutations for projector perturbations, non-idempotence,
  nonorthogonality, wrong ranks/weights, group incompleteness, booleans,
  floats, subclasses, nonpositive inputs, malformed and scan-only uniqueness
  evidence, false endpoints, and physical source claims that assert exponent
  or normalization selection.

Every individual intentional-failure fixture and the aggregate exit nonzero.
Run:

```bash
python3 scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py
python3 scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py --independent
python3 scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py --hostile
python3 scripts/frontier_quark_route2_double_local_projector_normalization_bridge_2026_06_21.py --mode intentional-failure --fixture all
```

The cached log records the default normal run.

## 7. Consumer boundary

The fresh citation graph has no direct claim consumer of this note. A future
consumer may use only the exact finite identities above and must provide any
physical interpretation or selection rule as a separate premise.
