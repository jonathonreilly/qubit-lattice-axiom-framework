# Gauge-Vacuum Plaquette First-Sector First-Hankel to DM Boundary

**Date:** 2026-04-19  
**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_gauge_vacuum_plaquette_first_sector_first_hankel_to_dm_boundary_2026_04_19.py`

## 2026-05-24 narrowing — load-bearing claim restricted

The previous audit on this row returned `audited_conditional` with re-audit
guidance:

> other: provide a retained derivation or runner that constructs the boundary
> map and proves first-Hankel minimality without text checks of the contested
> premise.

This revision narrows the **load-bearing claim** of this row to the
**algebraic equivalence on the canonical Wilson-side realization only**: on
the canonical minimal-bulk-completion branch's selected first-layer packet,
the first Jacobi layer `(alpha0, beta1)` and the first Hankel packet
`(m1, m2)` are equivalent via the exact identities

  `alpha0 = m1`,  `beta1^2 = m2 - m1^2`,

with `beta1 > 0` (positive Perron eigenvalue, conjugation-symmetric Perron
state, factorized transfer operator). This is exact linear algebra on the
already-constructed packet from the sibling
[`minimal-bulk-completion packet theorem`](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_PACKET_THEOREM_NOTE_2026-04-19.md)
and is closed inside the runner.

The previous load-bearing statement

> the earliest Wilson-side scalar packet feeding [the DM] boundary is exactly
> the first Hankel packet `(m1, m2)`

is **demoted to a non-load-bearing conditional corollary** for this row's
audit scope: it depends on an "earliest-feeding-boundary" premise that this
note does not derive from a retained authority and is not closed by the
runner. It is preserved below for historical traceability only.

## Bottom line (load-bearing, 2026-05-24)

On the canonical Wilson-side packet selected by the
minimal-bulk-completion branch, the first Jacobi layer `(alpha0, beta1)` and
the first Hankel packet `(m1, m2)` are equivalent via `alpha0 = m1` and
`beta1^2 = m2 - m1^2`, with `beta1 > 0`. This is an exact algebraic identity
on the realized packet.

## Bottom line (non-load-bearing historical context)

The remarks below are **not** load-bearing for this row and depend on
imports that are not closed here. They are preserved so the historical
framing remains traceable.

The nilpotent-chain packet-to-DM boundary already closes the downstream
local interface once the actual Wilson/PF packet is supplied.

The historical framing was: the earliest Wilson-side scalar packet feeding
that interface is the first Hankel packet `(m1,m2)`, equivalently the first
Jacobi layer `(alpha0,beta1)`, and the current stack still leaves that
packet open on the live route. Under that framing the quantitative DM seam
now starts exactly at the first-Hankel layer of `K_6^env` after identity-rim
reduction.

The "earliest-feeding-boundary" identification is **not derived** in this
note and is explicitly **not** part of the load-bearing claim of this row
per the 2026-05-24 narrowing.

## What the runner checks

The runner now drops text checks of the contested premise. It exercises the
canonical Wilson-side packet from the sibling
[`minimal-bulk-completion packet theorem`](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_PACKET_THEOREM_NOTE_2026-04-19.md)
and verifies the algebraic equivalence numerically:

1. one canonical realization on the minimal-bulk-completion branch is
   produced (finite `m1, m2` with `m2 > m1^2`);
2. the produced packet is well-defined: positive Perron eigenvalue,
   conjugation-symmetric Perron state, symmetric (factorized) transfer
   operator, `beta1 > 0`, `m2 - m1^2 > 0`;
3. the first Jacobi layer / first Hankel packet equivalence holds to
   machine precision:
   - `|alpha0 - m1| < 1e-12`,
   - `|beta1 - sqrt(m2 - m1^2)| < 1e-12`.

A successful run prints `PASS=<n> FAIL=0`.

## Commands run

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_first_hankel_to_dm_boundary_2026_04_19.py
```

Expected summary (load-bearing-only checks):

- `PASS=4 FAIL=0`
