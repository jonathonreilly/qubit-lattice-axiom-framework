# Quark CP Carrier Completion Route: Exact Spectrum and Basis Obstruction

**Date:** 2026-04-18 (exact-obstruction revision 2026-07-12)
**Type:** no_go
**Status:** exact negative boundary for the current fitted-carrier promotion
route; independent audit is required before any effective-status change.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_quark_cp_carrier_spectrum_basis_obstruction.py`](../scripts/frontier_quark_cp_carrier_spectrum_basis_obstruction.py)
**Paired output:**
[`logs/2026-07-12-quark-cp-carrier-spectrum-basis-obstruction.txt`](../logs/2026-07-12-quark-cp-carrier-spectrum-basis-obstruction.txt)

## Claim

The old revision reported a bounded numerical fit obtained by optimizing two
complex `1-3` carrier coefficients, `xi_u` and `xi_d`, against imported quark
mass-ratio and CKM/J comparators. That positive fit cannot be promoted into a
first-principles derivation on the implemented surface. Two independent exact
obstructions intervene.

1. **Physical-spectrum obstruction.** The optimizer checks ratios of diagonal
   input labels, not ratios of the singular values of the completed mass
   matrices. For every non-diagonal Hermitian completion, those diagonal labels
   are not the physical singular spectrum. At the shipped fit point the actual
   up-sector singular-value ratios miss both quoted mass-ratio comparators.
2. **Weak-basis-coordinate obstruction.** A common weak-basis rotation of the
   up and down matrices preserves both singular spectra, the full CKM matrix
   (hence every CKM modulus and `J`), and both determinants, while changing the
   real-tree `1-3` matrix coordinates and the normalized quantities called
   `xi_u`, `xi_d`. Therefore those values are not weak-basis-invariant
   observables. Reading a particular pair requires an additional choice of
   weak-basis/texture representative.

Hermiticity supplies a related exact boundary: each determinant is real for
every complex `1-3` phase. The old zero-phase check therefore tests only a
discrete determinant-sign product on this ansatz; it is not an equation that
derives the carrier phases and is not a strong-CP derivation.

Non-load-bearing context: the companion
`QUARK_CP_CARRIER_SLOT_MINIMALITY_THEOREM_NOTE_2026-06-17.md` proves that the
`1-3` edge is the unique phase-carrying one-edge extension of the fixed real
tree. The fitted numerical values remain open in that companion. It does not
supply either obstruction proved here and is intentionally not a markdown
dependency of this revised row.

This is a no-go for promoting the **current fitted coordinates and current
diagonal-mass check**. It is not a no-go for quark CP violation, for a corrected
singular-spectrum fit, for a future framework-derived basis selector, or for a
different mass-matrix construction.

## Exact setup

Write either sector's Hermitian matrix as

```text
        [ a       x       z  ]
M   =   [ x       b       y  ],       a,b,c,x,y real; z complex,
        [ z*      y       c  ]
```

where the old runner uses positive diagonal labels and real `1-2`, `2-3`
tree edges. Physical masses are the singular values `sigma_1 <= sigma_2 <=
sigma_3` of `M`, equivalently the positive square roots of the eigenvalues of
`H = M M^dagger`.

## Theorem 1: diagonal labels are not the singular spectrum

For Hermitian `M`,

```text
sum_i sigma_i^2
  = tr(M M^dagger)
  = a^2 + b^2 + c^2 + 2 (x^2 + y^2 + |z|^2).
```

If any off-diagonal entry is nonzero, then

```text
sum_i sigma_i^2 > a^2 + b^2 + c^2.
```

Consequently the singular values cannot equal the positive diagonal labels
`(a,b,c)` as a multiset. The old runner adds nonzero `1-2`, `2-3`, and `1-3`
entries but passes its two “mass-ratio” checks using only the optimizer
variables placed on the diagonal. It never evaluates the corresponding
singular-value ratios.

At the fixed point printed in the old note,

```text
r_uc = 1.688494e-3,       r_ct = 7.400356e-3,
xi_u = 0.340735 - 0.063203 i,
xi_d = 0.078186 + 0.108371 i,
```

the up-sector matrix has singular values

```text
(2.3037522e-5, 4.2942791e-3, 1.0031416),
```

and therefore

```text
sigma_u/sigma_c = 5.3647007e-3,
sigma_c/sigma_t = 4.2808304e-3.
```

The imported comparators used by the optimizer are approximately
`1.6967793e-3` and `7.3767167e-3`. The shipped point is thus not a simultaneous
physical mass-ratio plus CKM/J fit.

This last statement is also certified without floating-point root finding.
Interpret the decimal point printed by the old note as exact rationals. Exact
sign evaluation of its algebraic characteristic polynomial isolates the three
Hermitian eigenvalues in the disjoint rational intervals

```text
lambda_1 in (-24/10^6, -23/10^6),
lambda_2 in (429/10^5, 430/10^5),
lambda_3 in (1003/1000, 1004/1000).
```

Their absolute values are ordered as the singular values, so

```text
23/4300 < sigma_u/sigma_c < 4/715,
429/100400 < sigma_c/sigma_t < 43/10030.
```

The first interval lies strictly above the first imported comparator and the
second lies strictly below the second comparator. The fitted and comparator
decimals remain explicit historical boundary data for this replay statement;
deleting that comparison leaves the load-bearing exact conclusion unchanged:
the old PASS checks never evaluated physical singular-value ratios, and
nonzero off-diagonal entries prevent the diagonal labels from being the
singular spectrum itself.

## Theorem 2: a shared observable-preserving orbit changes the carrier coordinates

Let `W` be any unitary matrix and transform both sectors by the same weak-basis
change,

```text
M_u' = W^dagger M_u W,
M_d' = W^dagger M_d W.
```

Then

```text
H_s' = M_s' M_s'^dagger = W^dagger H_s W,
det(M_s') = det(M_s),
```

so the two singular spectra and both determinants are unchanged. If `U_s`
diagonalizes `H_s`, then `U_s' = W^dagger U_s` diagonalizes `H_s'`, and

```text
V_CKM' = U_u'^dagger U_d' = U_u^dagger U_d = V_CKM.
```

Thus the complete observable target used by the old fit is constant on every
common weak-basis orbit.

The orbit remains inside the Hermitian triangle family with real tree edges.
Take the common real `1-3` rotation

```text
             [ cos(theta)    0    sin(theta) ]
R_13(theta)= [     0         1        0       ].
             [-sin(theta)    0    cos(theta) ]
```

Direct multiplication gives

```text
M_12' = cos(theta) x - sin(theta) y,
M_23' = sin(theta) x + cos(theta) y,

M_13' = sin(theta)cos(theta)(a-c)
        + cos(2 theta) Re(z) + i Im(z).
```

The tree edges remain real, but the `1-3` coordinate changes generically; at
`theta=0`,

```text
d Re(M_13')/d theta = a-c.
```

Both shipped sector matrices have `a != c`. The runner applies the same small
rotation to both matrices, re-expresses each transformed matrix in the same
real-tree normalization, and verifies that both `xi` coordinates change while
the spectra, CKM moduli, `J`, and determinants remain fixed to numerical
precision. The displayed algebra, not the numerical tolerance, is the
load-bearing proof.

Therefore `xi_u` and `xi_d` are coordinates on a selected texture/basis, not
weak-basis-invariant observables. A mathematical convention can define their
values on one gauge-fixed slice, and the optimizer may be isolated within that
slice; the orbit theorem does not claim otherwise. A first-principles physical
interpretation of the particular coordinates would additionally have to derive
why that texture representative and normalization are the physical readout.
Stipulating the old Schur-NNI slice defines coordinates but does not supply
that derivation.

## Theorem 3: Hermiticity makes the determinant phase check non-selecting

For the displayed matrix,

```text
det M = abc - a y^2 - b |z|^2 - c x^2 + 2xy Re(z).
```

This is real for every `Im(z)`. Hence Hermiticity alone restricts
`arg det M` to `0` or `pi` (away from a zero determinant). The old fit has two
negative sector determinants, so their product is positive and its phase is
zero. That check supplies no continuous carrier-phase equation. It also does
not address the anomalous chiral-rotation/readout content required for a
physical strong-CP statement.

## What the exact obstruction retires

The following route is closed:

```text
fit xi_u and xi_d to imported diagonal-mass/CKM targets
    -> reinterpret the fitted coordinates as framework-derived physical carriers
    -> promote the old full-quark completion claim.
```

The first arrow fails because the mass checks do not read the physical
singular spectrum. The second fails because the fitted `xi` values vary along
an exactly observable-preserving weak-basis orbit.

This does not deliver the audit-requested positive derivation of the
coefficients. It instead prunes and retypes the current promotion route by
exposing two earlier hidden conditions: a physical singular-spectrum readout
and a selected weak-basis/texture representative. The old diagonal-label
existence-of-fit arithmetic remains historical bounded context, but it is not
the claim proposed for audit by this revision.

## What remains open

A positive completion would have to supply all of the following independently:

1. a mass-matrix construction whose physical mass checks use singular values;
2. a framework-derived joint weak-basis/texture selector, or an invariant
   replacement for the coordinate pair `xi_u`, `xi_d`;
3. a framework-derived carrier normalization and readout map;
4. framework-derived quark mass ratios and CKM/J targets rather than
   observation/atlas values used as proof inputs;
5. a separate strong-CP determinant/readout bridge if a physical theta claim
   is intended.

A corrected numerical optimizer could address item 1 as bounded computation.
It would not by itself address items 2-5. No claim is made here that a
corrected physical-spectrum completion has no numerical solution.

## Assumption and import firewall

- The exact trace, orbit, CKM-covariance, and determinant identities use no
  observed mass, CKM, J, PDG, atlas, fitted selector, literature value, or
  scale convention.
- The historical fit values and comparators appear only to exhibit the old
  runner's concrete mismatch; deleting them leaves all three exact theorems
  intact.
- No new axiom, framework primitive, generation selector, readout rule, or
  dynamics is introduced.
- The fixed Hermitian three-generation triangle with real tree edges is the
  explicit domain. Non-Hermitian completions, different support graphs, and
  independently derived texture selectors are outside the no-go.

## Falsifier and reopening conditions

The narrow no-go would be evaded by a retained theorem that derives a unique
physical joint basis/texture and carrier normalization before the `xi`
coordinates are read, together with a runner that computes physical singular
mass ratios. An invariant carrier replacing `xi_s` would also define a
different route. Neither possibility contradicts this note because both add
exactly the structure whose absence the orbit exposes.

## Validation

Run:

```bash
python3 scripts/frontier_quark_cp_carrier_spectrum_basis_obstruction.py
```

The runner checks the symbolic Frobenius and determinant identities, the exact
real-tree rotation formulas, an exact rational similarity witness, the shipped
point's singular-spectrum mismatch, the common-orbit invariants, and the
change in both normalized carrier coordinates. The no-go-discipline N1-N8
record and review disposition live in
`.claude/science/physics-loops/quark-cp-carrier-derivation-20260712/` and are
not audit authority.
