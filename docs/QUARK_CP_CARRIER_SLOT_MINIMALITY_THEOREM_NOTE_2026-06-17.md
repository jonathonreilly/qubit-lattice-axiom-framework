# Quark CP Carrier Slot Minimality Theorem

**Date:** 2026-06-17
**Claim type:** exact support theorem
**Status:** exact support, source-side proposal only; this is not an audit verdict.
**Primary runner:**
`scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py`

## Scope

This note repairs one structural gap in
[`QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md`](QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md).
The parent completion note uses one complex `1-3` carrier per quark sector,
`xi_u` and `xi_d`, and correctly says that the carrier values are fitted to
imported comparator targets rather than derived from framework primitives.

The result here is narrower and exact:

> On the fixed Schur-NNI tree with real `1-2` and `2-3` coefficients, the only
> Hermitian one-edge extension that creates a phase-gauge invariant carrier is
> the `1-3` closing edge. After the tree is gauge-fixed real, the `1-3` phase is
> the unique cycle phase. Because the matrix remains Hermitian, the determinant
> stays real; the slot itself introduces no continuous determinant phase.

This does not derive `xi_u` or `xi_d`. It does not derive quark comparator
targets, CKM magnitudes, the Jarlskog invariant, or a small-correction
interpretation. It only removes the slot-choice ansatz under the stated
fixed-tree/Hermitian one-edge boundary.

## Exact Algebra

Write the three-generation Hermitian support graph with vertices
`1,2,3`. Under a diagonal unitary rephasing

```text
M -> D^* M D,    D = diag(e^{i theta_1}, e^{i theta_2}, e^{i theta_3}),
```

an off-diagonal phase on edge `i-j` shifts by `theta_j - theta_i`. Therefore
the independent phase invariants are the cycle-space phases of the support
graph.

For the fixed Schur-NNI tree

```text
1 -- 2 -- 3
```

there are two edges and the connected vertex-rephasing rank is two. The phase
invariant dimension is therefore `2 - 2 = 0`; any phases on the `1-2` and `2-3`
tree edges are gauge.

On three vertices the only off-tree Hermitian edge is `1-3`. Adding it gives
the triangle. The phase invariant dimension becomes `3 - 2 = 1`, with invariant

```text
Phi = arg(M_12 M_23 M_31).
```

Gauge-fixing the tree real leaves exactly one residual phase on the `1-3`
coefficient, equal to `-Phi` in the runner's orientation. Thus, among
Hermitian one-edge extensions that preserve the fixed real Schur-NNI tree, the
complex `1-3` carrier is not an arbitrary slot choice: it is the unique closing
edge that can carry the cycle phase.

## Determinant Boundary

For a Hermitian three-by-three matrix with real diagonal entries and
off-diagonal magnitudes `x = |M_12|`, `y = |M_23|`, `z = |M_13|`, the determinant is

```text
abc - a y^2 - b z^2 - c x^2 + 2 x y z cos(Phi).
```

This expression is real for every cycle phase. The `1-3` carrier can change
the weak-sector cycle invariant, but Hermiticity prevents it from introducing a
continuous determinant phase by itself. That is the precise meaning of
"determinant-neutral" in this slot theorem.

## What This Repairs

The parent note listed four open load-bearing gaps. This note partially repairs
the second one:

```text
Derive why the determinant-neutral complex 1-3 carrier is the unique minimal
admissible CP-carrier slot beyond the Schur-NNI base.
```

The repaired statement is conditional on:

- preserving the real fixed Schur-NNI `1-2` and `2-3` tree coefficients;
- adding only one new Hermitian off-tree edge carrier;
- keeping the carrier determinant-phase neutral through Hermiticity.

Within that boundary, the slot is forced. Outside that boundary, other
extensions remain open: changing the fixed tree coefficients, adding more than
one carrier, using non-Hermitian completions, or deriving the fitted values
`xi_u`, `xi_d` from a deeper primitive.

## What Remains Open

This exact-support theorem does not close the parent row as a retained quark CP
derivation. The load-bearing numerical-match blockers remain:

1. derive the actual carrier coefficients `xi_u` and `xi_d`;
2. derive the relevant quark and CKM target readouts from framework primitives,
   or provide an independently audited bridge for them;
3. explain why the large fitted carrier magnitudes should be accepted as a
   framework-native completion rather than a non-perturbative bounded ansatz.

## Verification

Run:

```bash
python3 scripts/frontier_quark_cp_carrier_slot_minimality_2026_06_17.py
```

Expected summary:

```text
TOTAL: PASS=29 FAIL=0
```

The runner checks the incidence-rank count, the uniqueness of the off-tree
`1-3` edge, explicit random rephasing/gauge-fixing samples, the determinant
closed form, and source-boundary wording.
