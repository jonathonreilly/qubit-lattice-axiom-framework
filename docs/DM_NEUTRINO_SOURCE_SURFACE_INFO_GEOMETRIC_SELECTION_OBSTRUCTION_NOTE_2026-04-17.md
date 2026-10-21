# Scalar-baseline information geometry: local expansion and domain boundary

**Date:** 2026-04-17; calculation correction 2026-10-21
**Scope:** conditional local calculation; physical selector remains open
**Script:** `scripts/frontier_dm_neutrino_source_surface_info_geometric_selection_obstruction.py`

## Premises and retained calculation

Supply the real symmetric source `J = d T_delta + q T_q` from the
[active affine chart](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
and the reference baseline `D = m I_3`, `m > 0`.
The [Schur lemma](DM_NEUTRINO_SOURCE_SURFACE_SCHUR_SCALAR_BASELINE_THEOREM_NOTE_2026-04-17.md)
is conditional on commutation; it does not establish that the live affine
sheet has this baseline. Supply also the chosen
[chamber boundary](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md)
`d+q=E1=sqrt(8/3)`. Neither premise selects a physical source.

The generator identities are
`tr(T_delta^2)=tr(T_q^2)=6`, `tr(T_delta T_q)=0`, and
`tr(J^3)=6q(q^2-3d^2)`.
For `X=J/m` sufficiently small, compare precisely these four expressions:

- `F1=-log det(I+X)`;
- `F2=2 KL(N(0,H^-1) || N(0,(m I)^-1))`, `H=m I+J > 0`;
- `F3=-Hess(W)|_0[J,J]`, the curvature convention used here;
- `F4=tr(X^2)`.

For real Gaussians, the Fisher metric is `tr(X^2)/2`; therefore F3 is
**twice** that Gaussian Fisher quadratic, not its unqualified normalization.
No probability law is derived from the Grassmann generator by this notation.

Since `tr X=0`, expansion gives

```
F1 = (1/2) tr X^2 - (1/3) tr X^3 + O(||X||^4),
F2 = (1/2) tr X^2 - (2/3) tr X^3 + O(||X||^4),
F3 = F4 = tr X^2.
```

Thus the quadratic coefficients multiplying `(d^2+q^2)/m^2` are
`(3,3,6,6)`. In particular the F2 Hessian is `6 I_2/m^2`, not `18 I_2/m^2`.
The earlier coefficient 9 was a sign error, not a normalization convention.
The correct formula is

```
2 KL = tr(m H^-1) - 3 + log(det H/m^3).
```

Every displayed quadratic, as a polynomial extended to the boundary, has
its unique minimum at `d=q=E1/2=sqrt(6)/3`: differentiating
`d^2+(E1-d)^2` gives `4d-2E1`, with second derivative 4.
This says nothing about accuracy of the local expansion at that point.
It quantifies only the displayed family, not all information functionals.

## Why the former full Gaussian boundary comparison is invalid

At `m=1`, `tr(J^2)=6(d^2+q^2)>=3E1^2=8` on the entire boundary.
If `H=I+J` were positive definite, its three positive eigenvalues with
sum 3 would satisfy `tr(H^2)<9`; because `tr J=0`, this requires
`tr(J^2)<6`. These inequalities are incompatible. Therefore **no point
on that boundary defines the Gaussian covariance H^-1 at m=1**.

The previous runner used a minus sign before `log(abs(det H)/m^3)` and
compared grid minima outside this domain. Those minima and the claimed
full-order Gaussian obstruction are withdrawn. The corrected helper rejects
nonpositive eigenvalues and nonpositive baseline m. An absolute determinant
can define a different scalar response but cannot repair an invalid covariance.

The cubic coefficients above differ locally. That fact does not prove that
full functionals have different global minima. F4 is itself exactly quadratic
and retains the perpendicular-foot minimum. No universal impossibility of an
information-geometric selector follows.

## Open selection obligation and verification

The [observable principle](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md) supplies
responses to a given source. Identifying an extremum as the physical source
requires a separate justified selection rule. This note supplies none; it does
not rule out a future local or nonlocal derivation. The previously proposed
[minimum-information law](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md)
is not promoted by these calculations.

Run the named script for numerical trace and Hessian checks and domain rejection.
The companion `scripts/pmns_scoped_repair_regression_2026_10_21.py` independently
checks the scalar series and wrong-sign discriminator. PASS counts are execution
receipts, not scientific status. The former 26-check obstruction narrative is
superseded; no audit ledger or audit verdict is changed here.
