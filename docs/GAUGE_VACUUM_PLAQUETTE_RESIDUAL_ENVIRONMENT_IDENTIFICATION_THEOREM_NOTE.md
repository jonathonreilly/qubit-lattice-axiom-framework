# Gauge-Vacuum Plaquette Residual Environment Finite Coefficient Packet

**Date:** 2026-04-17 (residual-env structural identification);
2026-05-16 (witness replaced by computed Wilson coefficients on finite box);
2026-05-23 (scope repaired to a bounded finite coefficient packet).
**Type:** bounded_theorem
**Claim scope (post-2026-05-23 narrowing):** the load-bearing claim is only
the finite source-sector coefficient packet checked by
`scripts/frontier_gauge_vacuum_plaquette_residual_environment_identification.py`.
On the finite dominant-weight box `0 <= p,q <= NMAX`, at `beta = 6` and
`MODE_MAX = 80`, the runner constructs a diagonal finite coefficient factor
from computed normalized single-link Wilson character coefficients
`rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6))`, verifies that the prior
hand-picked witness has been replaced, and checks the corresponding finite
source-sector packaging
`exp(3J) D_6^loc R_6^packet exp(3J)` for self-adjointness,
conjugation-swap symmetry, positivity improving entries, and positive
truncated Perron readout.
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane. The `bounded_theorem` label is a
source-side claim-boundary declaration, not an audit verdict.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_residual_environment_identification.py`
**Bounded coefficient companion:**
[`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)

This note does **not** claim that the stripped residual source-sector operator
equals the compressed unmarked spatial Wilson environment. It also does not
claim all-weight closure, a full unmarked spatial-environment tensor-transfer
operator, explicit `beta = 6` Perron/Jacobi data, analytic `P(6)`, or any
repo-wide plaquette repinning.

## Question

After the marked half-slice factor and the normalized mixed-kernel local factor
are separated, can the finite coefficient slot used for the remaining
source-sector package be computed rather than supplied as a generic positive
witness?

## Answer

Yes, on the bounded finite coefficient packet.

The runner computes the finite coefficients from the canonical normalized
single-link `SU(3)` Wilson character integral:

`rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6))`,

`c_(p,q)(6) = int_SU(3) chi_(p,q)(U) exp((6/3) Re tr U) dU`.

Those coefficients are the same finite-box Wilson coefficients checked by the
retained bounded companion row. The current note uses them only as the finite
diagonal packet `R_6^packet` inserted into the source-sector package

`exp(3J) D_6^loc R_6^packet exp(3J)`.

This replaces the prior arbitrary witness sequence on the finite box. It does
not prove that `R_6^packet` is the actual compressed unmarked spatial
environment operator.

## Bounded Ingredient 1: computed finite Wilson coefficients

On the finite box used by the runner, the coefficients are computed in-runner
by the Schur-Weyl Bessel-determinant identity. The retained bounded companion
cross-checks the same coefficients against direct Weyl integration on the
Cartan torus with Vandermonde-squared measure.

The finite packet therefore has a retained bounded source for:

- positivity of the normalized finite coefficients,
- conjugation symmetry `rho_(p,q)(6) = rho_(q,p)(6)`,
- normalization `rho_(0,0)(6) = 1`,
- replacement of the retired hand-picked witness sequence.

## Bounded Ingredient 2: finite source-sector packaging

The runner constructs the finite matrices:

- the source recurrence `J` on the finite dominant-weight box,
- the marked half-slice multiplier `exp(3J)`,
- the diagonal local factor `D_6^loc`,
- the computed diagonal packet `R_6^packet`.

It then checks the finite package

`K_6^packet = exp(3J) D_6^loc R_6^packet exp(3J)`

for:

- self-adjointness,
- conjugation-swap symmetry,
- positive matrix entries on the truncation,
- a positive truncated Perron expectation.

These are finite packet checks. They do not prove the all-weight operator
identity named by the earlier parent theorem wording.

## Open Target: actual residual environment identification

The remaining theorem-grade target is still:

`R_beta^actual = compressed unmarked spatial Wilson environment`,

after stripping the marked half-slice factors and the normalized local
mixed-kernel factor from the source-sector transfer law.

To close that target, a future proof or runner must derive the equality for the
actual stripped residual operator, not merely insert the finite Wilson
coefficient packet. It must also handle all-weight support, the full
spatial-environment tensor-transfer/Perron construction, and the boundary
readout at `beta = 6`.

## What This Closes

- bounded replacement of the prior arbitrary positive witness on the finite
  coefficient packet;
- bounded construction of a finite diagonal source-sector packet from computed
  Wilson coefficients;
- bounded verification that the finite package remains self-adjoint,
  conjugation-symmetric, positivity improving on the truncation, and Perron
  positive.

## What This Does Not Close

- equality of the stripped residual source-sector operator with the compressed
  unmarked spatial Wilson environment;
- all-weight closure beyond the finite dominant-weight box;
- full unmarked spatial Wilson environment tensor-transfer/Perron data;
- explicit `beta = 6` Perron moments or Jacobi coefficients;
- analytic closure of canonical `P(6)`;
- repo-wide repinning of the canonical plaquette.

## Commands Run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_residual_environment_identification.py
```

Expected summary:

- `THEOREM PASS=6 SUPPORT=3 FAIL=0`

The theorem-grade checks are bounded to the finite packet:

- `J` is self-adjoint and conjugation-symmetric on the finite source sector;
- `exp(3J)` is positive and self-adjoint;
- `D_6^loc` is explicit, positive, diagonal, and conjugation-symmetric;
- `R_6^packet` is built from computed normalized Wilson coefficients, not the
  prior witness;
- `R_6^packet` acts diagonally with eigenvalues `rho_(p,q)(6)` on the finite
  class-function basis;
- `exp(3J) D_6^loc R_6^packet exp(3J)` is self-adjoint,
  conjugation-symmetric, and positivity improving on the finite source sector.

## Audit Dependency Repair Links

This graph-bookkeeping section records the explicit retained bounded input for
the finite packet. It does not promote this note, apply an audit verdict, or
close the full residual-environment identification theorem.

- [gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
  has current pipeline-derived effective status `retained_bounded` and
  computes the bounded normalized single-link Wilson coefficients on a finite
  weight box by two independent methods. This is the load-bearing coefficient
  authority for the finite packet used here.
- [gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md)
  supplies the source-side all-weight **formal diagonal-convolution**
  bridge for the stripped residual eigenvalue sequence:
  `R_beta^env chi_(p,q) = (1/lambda_env) C_(Z_beta^env) chi_(p,q)`.
  This is structural support only. It does not compute the beta=6
  coefficient sequence from the full unmarked spatial Wilson integral, does
  not assert normalized `kappa_(0,0)=1` closure, and does not promote this
  parent row.

The open bridge named by the prior conditional audit remains open at full
theorem scope: prove, or runner-certify, that the stripped residual
source-sector operator equals the compressed unmarked spatial Wilson
environment beyond the finite inserted coefficient table. After the
all-weight formal bridge above, the remaining physical bridge is the
independent derivation of the environment coefficient sequence from the
unmarked DOF integral / tensor-transfer construction, not the formal
Peter-Weyl diagonal-convolution dictionary itself.
