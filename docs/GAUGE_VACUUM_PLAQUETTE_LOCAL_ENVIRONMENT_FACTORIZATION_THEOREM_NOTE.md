# Gauge-Vacuum Plaquette Local Wilson Factor Finite Packet

**Date:** 2026-04-17 (scope-tightening re-frame: 2026-05-02);
2026-05-24 (scope repaired to a bounded finite local-factor packet).
**Type:** bounded_theorem
**Claim scope (post-2026-05-24 narrowing):** the load-bearing claim is only
the finite local Wilson coefficient packet checked by
`scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py`.
On the finite dominant-weight box `0 <= p,q <= NMAX`, at `beta = 6` and
`MODE_MAX = 80`, the runner computes normalized one-link Wilson character
coefficients
`a_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6))`, builds the finite diagonal
local packet
`D_6^loc = diag(a_(p,q)(6)^4)`, and checks the corresponding finite
source-sector package `exp(3J) D_6^loc exp(3J)` for the advertised algebraic
properties.
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane. The `bounded_theorem` label is a
source-side claim-boundary declaration, not an audit verdict.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py`
**Bounded coefficient companion:**
[`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)

This note does **not** claim the operator-level bridge that the temporal-gauge
mixed kernel on the actual marked-plaquette source sector factorizes into
exactly four nontrivial marked-link convolutions with only trivial-channel
scalars elsewhere. It also does not claim residual source-sector environment
data, physical `beta = 6` Perron/Jacobi data, analytic `P(6)`, or any
repo-wide plaquette repinning.

## Question

Can the local Wilson factor used in the plaquette source-sector package be
computed as an explicit finite coefficient packet, independent of the still
open residual-environment solve?

## Answer

Yes, on the bounded finite packet.

The runner computes normalized one-link Wilson character coefficients from the
canonical `SU(3)` Wilson integral:

`a_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6))`,

`c_(p,q)(6) = int_SU(3) chi_(p,q)(U) exp((6/3) Re tr U) dU`.

It then builds the finite local four-link packet

`D_6^loc chi_(p,q) = a_(p,q)(6)^4 chi_(p,q)`.

This is the finite local coefficient packet that downstream plaquette
source-sector notes may use. It does not by itself prove that the full actual
mixed-kernel compression on the marked plaquette sector equals this packet.

## Bounded Ingredient 1: computed one-link Wilson coefficients

On the finite box used by the runner, the coefficients are computed in-runner
by the Schur-Weyl Bessel-determinant identity. The bounded companion
cross-checks the same normalized Wilson coefficients against direct Weyl
integration on the Cartan torus with Vandermonde-squared measure.

The finite packet therefore has a bounded companion source for:

- positivity of the normalized finite coefficients;
- conjugation symmetry `a_(p,q)(6) = a_(q,p)(6)`;
- normalization `a_(0,0)(6) = 1`;
- the fourth-power local packet `a_(p,q)(6)^4`.

## Bounded Ingredient 2: finite local diagonal packet

The runner constructs

`D_6^loc = diag(a_(p,q)(6)^4)`

on the finite dominant-weight box. It checks that this packet is positive,
conjugation-symmetric, and normalized in the trivial channel.

The fourth power records the finite local plaquette-loop factor used by the
bounded source-sector packet. It is not a derivation of the actual
operator-level marked/non-marked mixed-kernel compression map.

## Bounded Ingredient 3: finite source-sector package

The runner constructs:

- the source recurrence `J` on the finite dominant-weight box;
- the marked half-slice multiplier `exp(3J)`;
- the diagonal local packet `D_6^loc`.

It then checks the finite package

`K_6^loc = exp(3J) D_6^loc exp(3J)`

for:

- self-adjointness;
- conjugation-swap symmetry;
- positivity of the finite diagonal local packet;
- a positive truncated Perron expectation.

These are finite packet checks. They do not prove that all non-marked
mixed-link factors in the actual Wilson source surface collapse to
trivial-channel scalars.

## Open Target: actual mixed-kernel compression bridge

The remaining theorem-grade target is still the operator-level bridge:

after temporal-gauge mixed-kernel factorization over the actual Wilson spatial
links, prove that restricting/compressing to the marked plaquette
class-function sector leaves exactly the four marked-link factors
`a_(p,q)(beta)^4` and no additional representation-dependent mixed-kernel
environment sequence.

To close that target, a future proof or runner must derive the actual
marked/non-marked compression map. The finite `D_6^loc` packet alone does not
establish it.

## What This Closes

- bounded computation of normalized one-link Wilson coefficients on the finite
  box;
- bounded construction of the fourth-power finite local packet
  `D_6^loc = diag(a_(p,q)(6)^4)`;
- bounded verification that the finite source-sector package remains
  self-adjoint, conjugation-symmetric, positivity-compatible on the
  truncation, and Perron positive.

## What This Does Not Close

- the actual temporal-gauge mixed-kernel compression bridge;
- proof that non-marked mixed-link factors in the actual source surface
  contribute only trivial-channel scalars;
- residual source-sector environment data at `beta = 6`;
- explicit `beta = 6` Perron moments after the full source-sector environment
  is included;
- analytic closure of canonical `P(6)`;
- repo-wide repinning of the canonical plaquette;
- status promotion of this note.

## Commands Run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py
```

Expected summary:

- `THEOREM PASS=4 SUPPORT=3 FAIL=0`

The theorem-grade checks are bounded to the finite packet:

- one-link Wilson coefficients are computed by the Bessel-determinant mode
  sum and normalized with `a_(0,0)(6) = 1`;
- trivial-channel scalar insertions do not change the normalized finite
  packet;
- `D_6^loc = diag(a_(p,q)(6)^4)` is positive and conjugation-symmetric on the
  finite source sector;
- `exp(3J) D_6^loc exp(3J)` is self-adjoint and conjugation-symmetric on the
  finite source sector.

## Audit Dependency Repair Links

This graph-bookkeeping section records the bounded inputs for the finite
packet. It does not promote this note, apply an audit verdict, or close the
actual mixed-kernel compression bridge.

- [gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
  has current pipeline-derived effective status `retained_bounded` and
  computes the same normalized one-link Wilson coefficients on a finite weight
  box by two independent methods.
- [gauge_vacuum_plaquette_transfer_operator_character_recurrence_note](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
  supplies the finite source recurrence `J` used in the packet runner.
- [gauge_vacuum_plaquette_source_sector_matrix_element_factorization_note](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
  supplies only the conditional source-sector matrix algebra and finite
  recurrence context for a separately supplied `M` and diagonal `D`. It does
  not derive a Wilson residual, a half-slice placement, or an actual
  mixed-kernel compression theorem.

The open bridge named by the earlier review history remains open at full
theorem scope: prove, or runner-certify, the actual temporal-gauge
mixed-kernel marked/non-marked compression map beyond construction of the
finite `D_6^loc` coefficient packet.
