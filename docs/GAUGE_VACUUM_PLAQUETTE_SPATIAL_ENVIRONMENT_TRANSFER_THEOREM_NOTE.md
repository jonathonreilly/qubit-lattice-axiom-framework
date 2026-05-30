# Gauge-Vacuum Plaquette Spatial Environment Transfer Finite Witness Packet

**Date:** 2026-04-17; 2026-05-24 (scope repaired to finite witness packet).
**Type:** bounded_theorem
**Claim scope (post-2026-05-24 narrowing):** the load-bearing claim is only
the finite class-sector witness constructed and checked by
`scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py`.
On the finite dominant-weight box `0 <= p,q <= NMAX`, with `NMAX = 5`,
`ETA = 0.32`, and `DEPTH = 3`, the runner constructs one explicit positive
self-adjoint conjugation-symmetric transfer witness

`S_packet = exp(ETA J) D_packet exp(ETA J)`,

one positive conjugation-symmetric boundary vector

`eta_packet = exp(ETA J / 2) e_(0,0)`,

and the finite boundary-amplitude sequence

`z_packet = S_packet^DEPTH eta_packet`.

It verifies positivity to floating tolerance, conjugation-swap symmetry,
normalization of `rho_packet = z_packet / z_packet_(0,0)`, and positive
truncated Perron overlap/readout. This is a bounded finite witness packet, not
a proof of the actual unmarked spatial Wilson environment.
**Status authority:** independent audit lane only. The `bounded_theorem` label
is a source-side claim-boundary declaration, not an audit verdict.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py`

This note does **not** claim the full untruncated spatial-environment
boundary-amplitude identity

`z_(p,q)^env(beta) = <chi_(p,q), (S_beta^env)^(L_perp-1) eta_beta>`.

It also does not claim the actual Wilson environment transfer operator, the
physical `beta = 6` matrix elements, explicit `rho_(p,q)(6)` values, full
Perron/boundary data, analytic `P(6)`, or repo-wide plaquette repinning.

## Question

Can the spatial-environment lane at least exhibit, on a bounded class-sector
packet, the transfer-amplitude structure that the full Wilson-environment
theorem would need?

## Answer

Yes, as a finite witness packet.

The runner builds an explicit positive self-adjoint transfer witness on the
truncated `SU(3)` dominant-weight class sector. It then constructs a
conjugation-symmetric boundary vector and verifies that the resulting finite
sequence is a normalized boundary-amplitude sequence of that witness.

This demonstrates the finite transfer-amplitude pattern. It does not identify
that witness with the actual unmarked spatial Wilson environment.

## Bounded Ingredient 1: finite transfer witness

Let `J` be the finite six-neighbor class-sector recurrence on the
dominant-weight box. The runner constructs

`S_packet = exp(ETA J) D_packet exp(ETA J)`,

where `D_packet` is a positive diagonal damping packet. On the finite box,
the runner checks that `S_packet` is:

- self-adjoint to numerical tolerance,
- conjugation-swap symmetric,
- positive definite.

## Bounded Ingredient 2: finite boundary-amplitude sequence

The runner also constructs

`eta_packet = exp(ETA J / 2) e_(0,0)`,

and then computes

`z_packet = S_packet^DEPTH eta_packet`.

It verifies that:

- `eta_packet` is nonnegative to floating tolerance and
  conjugation-symmetric;
- `z_packet` is positive and conjugation-symmetric;
- `rho_packet = z_packet / z_packet_(0,0)` is normalized at the trivial
  channel and nonnegative;
- the finite Perron vector has positive overlap with the boundary-amplitude
  sequence.

The prior cached failure for the marked-rim boundary state was a
roundoff-scale component about `-1.3e-16`; the runner now treats
nonnegativity at a `1e-14` tolerance and reports the tolerance explicitly.

## Open Target: actual Wilson environment transfer theorem

The theorem-grade target remains open:

`z_(p,q)^env(beta) = <chi_(p,q), (S_beta^env)^(L_perp-1) eta_beta>`

for the actual unmarked spatial Wilson environment, with the actual transfer
operator and boundary state. Closing that target requires a proof or runner for
the full untruncated Wilson environment, not a finite constructed witness.

## What This Closes

- bounded construction of one finite positive self-adjoint class-sector
  transfer witness;
- bounded construction of a finite boundary-amplitude sequence from that
  witness;
- repair of the floating-tolerance boundary positivity runner failure;
- a precise finite target for independent audit.

## What This Does Not Close

- the actual unmarked spatial Wilson environment transfer operator;
- the full boundary-amplitude identity for `Z_beta^env`;
- explicit physical `beta = 6` coefficients `rho_(p,q)(6)`;
- full Perron moments or boundary state of the Wilson environment;
- analytic closure of canonical `P(6)`;
- repo-wide repinning of the canonical plaquette.

## Commands Run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_spatial_environment_transfer.py
```

Expected summary:

- `THEOREM PASS=4 SUPPORT=3 FAIL=0`

The theorem-grade checks are bounded to the finite witness packet:

- `S_packet` is positive, self-adjoint, and conjugation-symmetric on the
  finite class sector;
- `eta_packet` is nonnegative to tolerance and conjugation-symmetric;
- `z_packet` is a positive boundary-amplitude sequence of `S_packet`;
- `rho_packet` is a normalized nonnegative finite sequence, not a free
  asserted list.

## Audit Dependency Repair Links

This graph-bookkeeping section records the bounded upstream packet that limits
the honest scope of this row. It does not promote this note, apply an audit
verdict, or close the full Wilson-environment transfer theorem.

- [gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  supplies the upstream finite tensor-word packet. This row uses it only as
  bounded support for the finite transfer-witness pattern, not as authority for
  the full untruncated Wilson-environment identity. Any effective dependency
  status is pipeline-derived, not asserted here.

The missing bridge named by the prior conditional audit remains open at full
theorem scope: prove the full untruncated spatial-environment boundary
amplitude identity for the actual Wilson environment.
