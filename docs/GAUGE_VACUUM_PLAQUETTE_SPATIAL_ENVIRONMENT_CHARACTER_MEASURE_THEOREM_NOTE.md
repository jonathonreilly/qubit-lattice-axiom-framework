# Gauge-Vacuum Plaquette Spatial Environment Character-Measure Finite Packet

**Date:** 2026-04-17 (witness-source repair 2026-05-16);
2026-05-24 (scope repaired to a bounded finite character-measure packet).
**Type:** bounded_theorem
**Claim scope (post-2026-05-24 narrowing):** the load-bearing claim is only
the finite character-measure coefficient packet checked by
`scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py`.
On the finite dominant-weight box `0 <= p,q <= NMAX`, at `beta = 6` and
`MODE_MAX = 80`, the runner computes normalized single-link Wilson character
coefficients
`rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6))`, verifies that the prior
hand-picked witness has been replaced, and packages the resulting finite
coefficient sequence as a normalized central boundary-character packet
`Z_6^packet`.
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane. The `bounded_theorem` label is a
source-side claim-boundary declaration, not an audit verdict.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py`
**Bounded coefficient companion:**
[`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)

This note does **not** claim that the stripped residual source-sector operator
equals normalized convolution by the actual unmarked spatial Wilson
environment boundary class function. It also does not claim all-weight
closure, the full multi-link unmarked spatial-environment tensor-transfer
operator, explicit `beta = 6` Perron/Jacobi data, analytic `P(6)`, or any
repo-wide plaquette repinning.

## Question

After the finite Wilson coefficient table is computed, can the coefficient
slot formerly represented by an arbitrary positive witness be packaged as an
explicit finite normalized central character-measure packet?

## Answer

Yes, on the bounded finite packet.

The runner computes the finite coefficients from the canonical normalized
single-link `SU(3)` Wilson character integral:

`rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6))`,

`c_(p,q)(6) = int_SU(3) chi_(p,q)(U) exp((6/3) Re tr U) dU`.

Those coefficients are the same finite-box Wilson coefficients checked by the
bounded companion row. The current note uses them only as the finite
diagonal packet `C_(Z_6^packet)` inserted into the source-sector package

`exp(3J) D_6^loc C_(Z_6^packet) exp(3J)`.

This replaces the prior arbitrary witness sequence on the finite box. It does
not prove that `Z_6^packet` is the actual boundary class function
`Z_6^env(W)` of the full unmarked spatial Wilson environment, and it does not
prove that the stripped residual operator is exactly
`C_(Z_6^packet)`.

## Bounded Ingredient 1: computed finite Wilson coefficients

On the finite box used by the runner, the coefficients are computed in-runner
by the Schur-Weyl Bessel-determinant identity. The bounded companion
cross-checks the same coefficients against direct Weyl integration on the
Cartan torus with Vandermonde-squared measure.

The finite packet therefore has a bounded companion source for:

- positivity of the normalized finite coefficients;
- conjugation symmetry `rho_(p,q)(6) = rho_(q,p)(6)`;
- normalization `rho_(0,0)(6) = 1`;
- replacement of the retired hand-picked witness sequence
  `exp(-0.24 (p+q) - 0.08 (p-q)^2)`.

## Bounded Ingredient 2: finite central character-measure packaging

The runner packages the finite coefficient sequence as

`Z_6^packet(W) = z_(0,0)^packet sum d_(p,q) rho_(p,q)(6) chi_(p,q)(W)`.

The normalized convolution packet acts diagonally on the finite
class-function basis:

`C_(Z_6^packet) chi_(p,q) = rho_(p,q)(6) chi_(p,q)`.

This is a finite algebraic packaging statement. It is not an identification
of `Z_6^packet` with the full unmarked spatial Wilson environment boundary
function.

## Bounded Ingredient 3: finite source-sector package

The runner constructs the finite matrices:

- the source recurrence `J` on the finite dominant-weight box;
- the marked half-slice multiplier `exp(3J)`;
- the diagonal local factor `D_6^loc`;
- the diagonal character-measure packet `C_(Z_6^packet)`.

It then checks the finite package

`K_6^packet = exp(3J) D_6^loc C_(Z_6^packet) exp(3J)`

for:

- self-adjointness;
- conjugation-swap symmetry;
- normalized coefficient consistency;
- positive finite coefficients;
- a positive truncated Perron expectation.

These are finite packet checks. They do not prove the all-weight operator
identity named by the earlier parent theorem wording.

## Open Target: actual character-measure identification

The remaining theorem-grade target is still:

`R_beta^actual = C_(Z_beta^env)`,

where `Z_beta^env(W)` is the actual boundary class function obtained by
integrating the full unmarked spatial Wilson environment with the marked
plaquette boundary holonomy held fixed.

To close that target, a future proof or runner must derive the equality for
the actual stripped residual source-sector operator, not merely insert the
finite single-link Wilson coefficient packet. It must also handle all-weight
support, the full spatial-environment tensor-transfer/Perron construction,
and the boundary readout at `beta = 6`.

## What This Closes

- bounded replacement of the prior arbitrary positive witness on the finite
  coefficient packet;
- bounded construction of a finite normalized central character-measure packet
  from computed single-link Wilson coefficients;
- bounded verification that the finite source-sector package remains
  self-adjoint, conjugation-symmetric, positivity-compatible on the
  truncation, and Perron positive.

## What This Does Not Close

- equality of the stripped residual source-sector operator with normalized
  convolution by the actual unmarked spatial Wilson environment boundary
  class function;
- identification of the finite single-link packet with the full multi-link
  unmarked spatial Wilson environment;
- all-weight closure beyond the finite dominant-weight box;
- full unmarked spatial Wilson environment tensor-transfer/Perron data;
- explicit `beta = 6` Perron moments or Jacobi coefficients;
- analytic closure of canonical `P(6)`;
- repo-wide repinning of the canonical plaquette;
- status promotion of this note.

## Commands Run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.py
```

Expected summary:

- `THEOREM PASS=6 SUPPORT=3 FAIL=0`

The theorem-grade checks are bounded to the finite packet:

- `J` is self-adjoint and conjugation-symmetric on the finite source sector;
- the finite packet equals the computed normalized single-link Wilson
  coefficients;
- the finite packet is distinct from the retired arbitrary witness sequence;
- the packet is positive and conjugation-symmetric on the truncation;
- the finite coefficients can be packaged as one normalized central
  boundary-character packet;
- `exp(3J) D_6^loc C_(Z_6^packet) exp(3J)` is self-adjoint and
  conjugation-symmetric on the finite source sector.

## Audit Dependency Repair Links

This graph-bookkeeping section records the explicit bounded inputs for the
finite packet. It does not promote this note, apply an audit verdict, or close
the full residual-environment / character-measure identification theorem.

- [gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
  has current pipeline-derived effective status `retained_bounded` and
  computes the bounded normalized single-link Wilson coefficients on a finite
  weight box by two independent methods. This is the load-bearing coefficient
  authority for the finite packet used here.
- [gauge_vacuum_plaquette_local_environment_factorization_theorem_note](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md)
  supplies the bounded finite `D_6^loc` packet used in
  `exp(3J) D_6^loc C_(Z_6^packet) exp(3J)`.
- [gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification_narrow_theorem_note_2026-05-17](GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md)
  supplies the source-side all-weight **formal diagonal-convolution**
  bridge for the stripped residual eigenvalue sequence. It supports the
  Peter-Weyl dictionary part of the character-measure identification:
  a diagonal residual sequence can be written as unnormalized formal
  convolution by a central sequence. It does not compute the actual
  beta=6 unmarked spatial Wilson environment coefficients, prove
  normalized `kappa_(0,0)=1`, or identify the finite single-link packet
  with the full multi-link environment.

The actual residual-environment equality row remains a future sibling target,
not a dependency of this finite packet. This note does not import a stronger
actual-environment equality from that row.

The open bridge named by the earlier review history remains open at full
theorem scope: prove, or runner-certify, that the stripped residual
source-sector operator equals normalized convolution by the actual compressed
unmarked spatial Wilson environment boundary character, beyond insertion of
the finite single-link coefficient packet. After the all-weight formal bridge
above, the remaining physical bridge is the independent derivation of the
environment coefficient sequence from the unmarked DOF integral /
tensor-transfer construction, not the formal Peter-Weyl diagonal-convolution
dictionary itself.
