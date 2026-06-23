# Quark Route-2 Adjoint-Singlet Normalization No-Go

**Date:** 2026-06-22
**Type:** no-go / invariant-form normalization obstruction packet
**Actual current-surface status:** no-go for SU(3) invariance alone fixing the Route-2 adjoint/singlet normalization
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_adjoint_singlet_normalization_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_adjoint_singlet_normalization_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_adjoint_singlet_normalization_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_adjoint_singlet_normalization_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Question

Block116 proves that the orientation-free linear contraction on a symmetric
`sl_3` adjoint Hessian is unique up to scale. Could SU(3) invariance of the
full color source already fix that scale relative to the disconnected identity
line and therefore force the normalized `8/9` selector?

## Result

No. For the full color source representation

```text
End(C^3) = 1 + adjoint,
```

the invariant symmetric contraction space is two-dimensional:

```text
Hom_SU3(Sym^2(1 + adjoint), 1) = 2.
```

The two independent contractions are:

```text
singlet identity-line contraction,
adjoint inverse-Killing contraction.
```

There is no invariant cross term because:

```text
Hom_SU3(adjoint, 1) = 0.
```

So invariance separates the disconnected identity line from the connected
adjoint block, but it does not choose their relative coefficient.

If the singlet and adjoint coefficients are `alpha` and `beta`, the normalized
connected fraction is:

```text
R(alpha,beta) = 8 beta / (alpha + 8 beta).
```

Only the additional normalization `alpha = beta` gives:

```text
R = 8/9,   kappa = 0.
```

Other SU(3)-invariant choices are allowed by representation theory alone, for
example:

```text
R(1,2) = 16/17,
R(2,1) = 4/5.
```

Therefore Block116 removes a hidden color-orientation selector, but it does not
remove the need for a Route-2 coefficient/source normalization theorem.

## Missing Primitive

The precise missing primitive is:

```text
Route-2 adjoint/singlet coefficient normalization theorem:

after constructing the same-source covariant adjoint multi-record family and
typing the physical E/T readout as D_A D_B log Z, prove that the identity-line
and adjoint inverse-Killing contractions are normalized with equal unit weight
for the physical Route-2 source/readout.
```

This primitive is separate from the orientation-free contraction theorem. It is
also separate from endpoint-value reversal: no endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=54, FAIL=0
```
