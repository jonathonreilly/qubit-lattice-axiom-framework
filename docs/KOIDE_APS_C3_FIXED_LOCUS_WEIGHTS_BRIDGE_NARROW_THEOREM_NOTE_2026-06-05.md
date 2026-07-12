# C₃ Body-Diagonal Fixed Locus and Local Inverse-Determinant Density

**Date:** 2026-06-05; exact supplier repair 2026-07-11
**Claim type:** positive_theorem
**Status authority:** audit verdict authority remains with the independent
audit lane.
**Primary runner:**
[`scripts/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.py`](../scripts/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.py)
**Cached runner output:**
[`logs/runner-cache/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.txt`](../logs/runner-cache/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.txt)

## Narrow claim

Take the proper cubic rotation by `2*pi/3` about the coordinate body diagonal
spanned by `(1,1,1)` in the `Z^3` lattice. This representative group element
supplies the finite calculation; physical-axis selection is a separate theorem
target. On its real two-dimensional normal plane, both nonidentity elements of
the generated `C_3` group have

```text
det_R(I-g|_N)=3.
```

Define the finite `C_3` inverse-normal-determinant density by

```text
L_C_3(N) = (1/3) sum_{k=1}^{2} 1/det_R(I-g^k|_N).
```

Then

```text
L_C_3(N) = (1/3)(1/3+1/3) = 2/9.
```

This is an exact local representation-theory statement. Physical
identification with a charged-lepton angle, eta invariant, global APS index,
probability, readout normalization, or registered-mass value belongs to
separate theorem domains.

## Framework input

The [current minimal-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the
`Z^3` lattice and its proper cubic rotations. The proof domain is the supplied
lattice rotation and standard exact linear algebra. Site, state, action,
matter-carrier, readout-context, charged-lepton-parameter, and physical
functional-selection claims have separate source rows. The finite average is
the mathematical functional defined and evaluated in this claim.

## Proof

### Body-diagonal rotation

In the ordered coordinate-axis basis, cyclic relabelling is

```text
P = [[0,0,1],
     [1,0,0],
     [0,1,0]].
```

It is orthogonal, has determinant one, and satisfies `P^3=I`. Rodrigues'
formula for angle `2*pi/3` about `(1,1,1)/sqrt(3)` evaluates exactly to `P`,
so this matrix is the proper cubic body-diagonal rotation rather than a
separately supplied operator.

Its characteristic polynomial in the convention `det(P-xI)` is

```text
1-x^3=(1-x)(1+x+x^2).
```

The fixed subspace is the body-diagonal line, because `rank(P-I)=2` and
`P(1,1,1)=(1,1,1)`. The real normal plane is therefore

```text
N={(u,v,w) in R^3 : u+v+w=0}.
```

### Real normal determinant

Use the exact normal-plane basis

```text
v1=(1,-1,0),   v2=(0,1,-1).
```

Writing `P[v1 v2]=[v1 v2] N` gives

```text
N = [[0,-1],
     [1,-1]],
```

up to the displayed basis convention. Its characteristic polynomial is
`x^2+x+1`, so the complexified normal eigenvalues are the conjugate pair

```text
omega=exp(2*pi*i/3),   omega_bar=omega^2.
```

The matrix trace of the normal action is `-1`. The relevant exact property is
that the real normal representation has the conjugate nontrivial characters
and determinant one.

For `k=1,2`, the normal action of `P^k` has the same conjugate eigenvalue set.
Consequently

```text
det_R(I-P^k|_N)
  =(1-omega)(1-omega_bar)
  =3.
```

The determinant is nonzero, so the normal contribution is well-defined for
both nonidentity group elements.

### Finite group average

Substitution into the stated finite average gives

```text
L_C_3(N)
  =(1/3) [det_R(I-P|_N)^(-1)+det_R(I-P^2|_N)^(-1)]
  =(1/3)(1/3+1/3)
  =2/9.
```

Reversing the generator exchanges `P` and `P^2`, so the value is independent
of orientation convention. The proof is constant over all supplied `r` and
`delta`; the result holds for every registered charged-lepton coordinate when
a downstream lane cites this local number within its stated boundary.

## Direct dependency surface

The citation graph matches the proof: the local theorem follows directly from
the Lattice axiom's proper cubic rotation and exact linear algebra. The
following are plain-text context handles with independent source rows:

- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`;
- `THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`;
- `FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md`;
- `FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md`;
- `HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md`;
- `KOIDE_RETAINED_WILSON_APS_SCALAR_ACTION_ON_RANK_TWO_MULTIPLICITY_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`;
- `S3_GENERAL_R_DERIVATION_NOTE.md`.

Their audit status is independent of this calculation.

## Theorem-domain boundary

The source proves the local representation and finite average above. Separate
theorem targets govern:

- physical single-summand readout;
- a map from the local number to a bare holonomy angle;
- `h`-unit normalization;
- global `Cl(3)/Z^3 -> PL S^3 x R` identification and APS applicability;
- action, K/CPT structure, matter statistics, generation labeling, mass,
  `r`, `delta`, probability rules, and observational values.

Axiom, primitive, import, comparator, and audit-authority surfaces are
unchanged. The row supplies the local number and is constant over AC(i),
AC(ii), and every registered value of `r`.

## Validation

The exact SymPy runner verifies:

1. orthogonality, orientation, and order of `P`;
2. equality with the Rodrigues body-diagonal rotation;
3. characteristic polynomial and fixed subspace;
4. an exact real normal-plane representation;
5. its conjugate complex weights and determinant-one property;
6. `det_R(I-P^k|_N)=3` for `k=1,2`;
7. the finite average `2/9`;
8. generator-reversal invariance;
9. absence of free parameters in the computed density; and
10. source-scope and citation-edge guards.

Expected result: `TOTAL: PASS=16, FAIL=0`.
