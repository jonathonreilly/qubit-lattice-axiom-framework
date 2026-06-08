# Gauge Vacuum Plaquette First-Sector Rank-One Factorized-Class Boundary Live Packet

**Date:** 2026-04-19; live-source repair 2026-06-08
**Status:** bounded-support packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_2026_04_19.py)
**Primary runner cache:** [`logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_2026_04_19.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_2026_04_19.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_note_2026-04-19`.
The archived note failed audit because the declared exact runner was not
available to the restricted packet at the time of audit.

The runner is present on the current repo surface and its cache is fresh. This
note therefore asks re-audit to evaluate the executable finite boundary packet,
not the archived missing-runner surface.

## Live Claim

Inside the first-sector finite packet, the runner constructs the completed
four-weight vector `v_min`, the specified sample triple `Z_min`, and an explicit
positive rank-one transfer `T_min` that propagates `e_0` to `v_min` at depth
three.

It then pulls `T_min` back through the Wilson half-slice multiplier
`M = exp(3J)`:

```text
D_back = M^{-1} T_min M^{-1}.
```

The live finite certificate verifies:

- `E_3 v_min = Z_min` to numerical precision;
- `T_min^3 e_0 = v_min` to numerical precision;
- the Wilson half-slice multiplier is invertible;
- the unique pullback `D_back` is self-adjoint and conjugation-symmetric but
  not diagonal;
- the positive conjugation-symmetric diagonal-family search reproduces the
  archived vector residual;
- the same best diagonal-family point still misses the three-sample target.

Current cached runner output records:

```text
||offdiag(D_back)||_F / ||.||_2 = 0.250338180104 / 0.188121379170
best vector/sample residuals    = 0.135462193873 / 0.228465894557
PASS=6 FAIL=0
```

## Boundary

This packet supports only the finite boundary statement:

> The explicit positive rank-one transfer realization of the first-sector
> `Z_min` target is not in the diagonal Wilson factorized-class subfamily
> `T = exp(3J) D exp(3J)` checked by the runner.

It does not claim a full Wilson-environment identification, a continuum gauge
theorem, or effective retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_RANK_ONE_FACTORIZED_CLASS_BOUNDARY_NOTE_2026-04-19.md`](../archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_RANK_ONE_FACTORIZED_CLASS_BOUNDARY_NOTE_2026-04-19.md).
