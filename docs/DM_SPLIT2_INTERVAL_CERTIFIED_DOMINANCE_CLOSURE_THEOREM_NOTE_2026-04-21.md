# DM split-2 numerical two-box dominance support

**Date:** 2026-04-21; correction 2026-10-21
**Status:** support - structural or confirmatory support note
**Primary runner:** `scripts/frontier_dm_split2_interval_certified_dominance_closure_2026_04_21.py`

The legacy filename is retained for existing links. The runner provides
numerical support on two supplied boxes, not an interval certificate or a
proof of global carrier completeness. The former closure claim is withdrawn.

## Domain and exact mathematical ingredients

The supplied neighborhoods are

- `CAP_BOX`: `m in [-.145,-.14]`, `delta in [1.1835,1.1935]`, `slack in [.0145,.0245]`;
- `ENDPOINT_BOX`: `m in [-.145,-.14]`, `delta in [1.1839,1.1890]`, `slack in [0,.005]`.

The [affine chart](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md)
is `H=H_base+m T_m+delta T_delta+q T_q`. The
[half-plane coordinates](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md)
give `q=E1-delta+slack`. Therefore the tangent at fixed slack is
`T_delta-T_q`, whose eigenvalues are `-2,1-sqrt(3),1+sqrt(3)`.
Its norm is `1+sqrt(3)`, not `sqrt(3)`.

Weyl's theorem bounds the perturbation by

```
r = h_m + (1+sqrt(3))*h_delta + 2*h_slack.
```

For the two boxes, numerical evaluation gives respectively
`r=.0261602540378444` and `.0144667295593008`.
The earlier radii understated the bound by the delta half-width.
The resulting eigenvalue intervals remain disjoint in the numerical evaluation.
For simple eigenvalues the cofactor identity

```
P_ij = det(H_(i)-lambda_j I_2) / product_{k != j}(lambda_j-lambda_k)
```

is exact. It is a valid starting point for a future rigorous enclosure.

## Numerical evaluation and limits

The implementation propagates float endpoint intervals without outward rounding.
It evaluates the supplied one-variable transport functional
`F(P)=sum_alpha Psi(P_alpha)` through a discretized kernel and trapezoidal
integration. A bisection root of the sampled derivative supplies a candidate
peak; endpoint signs alone do not prove that it is the global kernel maximum.
The added `1e-15` padding is not a quadrature or roundoff error certificate.

With the corrected tangent, the rowwise upper **estimates** of `eta/eta_obs` are

- `CAP_BOX`: `(.774997112996, .888906090020, .907310059853)`;
- `ENDPOINT_BOX`: `(.762656546126, .867834797641, .900579176619)`.

The largest estimates leave margins about `.09269` and `.09942`. These are
encouraging local numerical results. They do not establish whole-box exclusion
until eigenvalue/cofactor rounding, integration error, and kernel supremum
control are certified. Even a future rigorous two-box result would require a
separate global coverage argument before implying branch completeness.

The [carrier-side conclusion](DM_NEUTRINO_SOURCE_SURFACE_CARRIER_SIDE_CONCLUSION_NOTE_2026-04-18.md)
records a tested reduction to two neighborhoods; its text does not provide that
global proof. The [dense-grid support](DM_SPLIT2_DENSE_GRID_LIPSCHITZ_DOMINANCE_SUPPORT_NOTE_2026-04-21.md)
likewise remains sampled support. Matching their text strings is not a proof gate.

## Reproduction and open obligations

Run the primary script and `scripts/pmns_scoped_repair_regression_2026_10_21.py`.
The latter independently checks the tangent eigenvalues and chart derivative.
The previous 17-PASS receipt is superseded; incidental packet thresholds and
literal closure/text checks have been removed rather than forced to pass.

Open obligations are certified arithmetic, kernel integration and supremum
control, and exhaustive reduction of the relevant carrier domain to these boxes.
No physical source selection, package-wide closure, or audit status follows.
