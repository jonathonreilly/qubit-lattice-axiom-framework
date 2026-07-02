# Gauge-Vacuum Plaquette First-Sector Minimal-Bulk Completion Packet Theorem

**Date:** 2026-04-19 (source parent added 2026-06-12)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set
ledger or effective status.
**Primary runner:** `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_packet_theorem_2026_04_19.py`

## Claim

On the explicitly narrowed zero-extension/witness surface supplied by the
first-sector minimal-bulk completion principle note, the canonical
factorized-class zero extension produces one explicit Wilson/Perron
first-layer packet.

Let `rho_ret` be the first-sector retained packet consumed by the local
runner helpers, and let `rho_0` be its coefficient-order zero extension to
the dominant-weight box. Assemble

```text
T_sel = exp(beta J / 2) D_loc diag(rho_0) exp(beta J / 2).
```

The runner constructs `T_sel`, extracts its Perron state, and verifies that
the first Jacobi layer and first Hankel moments satisfy

```text
alpha0 = m1,
beta1^2 = m2 - m1^2,
beta1 > 0.
```

For the current runner inputs the selected packet is

```text
alpha0 = 0.430754683575...
beta1  = 0.252651403480...
m1     = 0.430754683575...
m2     = 0.249382329102...
```

This is a bounded packet theorem on the zero-extension witness branch. It
does not assert that the framework-point Wilson environment packet is
physically selected by this branch.

## What Is Proved Here

The paired runner verifies:

- `rho_0` gives finite `m1, m2` with `m2 > m1^2`;
- the assembled transfer operator is self-adjoint to machine precision;
- the transfer operator is conjugation-symmetric on the truncated
  dominant-weight box;
- the Perron state is conjugation-symmetric;
- the first Jacobi layer is equivalent to the first Hankel packet by
  `alpha0 = m1` and `beta1^2 = m2 - m1^2`.

These are direct computations on the framework's in-tree packet and
factorized-transfer helpers. They are not imported from textbook or
external mathematical authority.

## Boundaries

This note does not prove universal Loewner-minimality for all admissible
tails. The sibling minimal-bulk completion principle note records that as an
open derivation gap.

This note does not add an axiom, selector law, or physical postulate.

This note does not prove that the zero-extension branch is the actual
framework-point Wilson environment packet.

This note does not close the historical earliest-feeding-DM-boundary premise.
The child first-Hankel-to-DM-boundary note has already narrowed its
load-bearing claim to algebraic first-Jacobi/first-Hankel equivalence on the
realized packet.

This note does not promote the child decoration row. The audit lane owns any
effective-status change.

## Dependencies

- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_PRINCIPLE_THEOREM_NOTE_2026-04-19.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_PRINCIPLE_THEOREM_NOTE_2026-04-19.md)
  for the narrowed runner-tested zero-extension/witness surface and for the
  explicit statement that universal Loewner-minimality remains open.
- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_ZERO_EXTENSION_FACTORIZED_CLASS_THEOREM_NOTE_2026-04-19.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_ZERO_EXTENSION_FACTORIZED_CLASS_THEOREM_NOTE_2026-04-19.md)
  for the explicit factorized-class zero-extension construction and local
  factor diagonal used by the runner.

The current audit status of these dependencies is tracked only by
`docs/audit/AUDIT_LEDGER.md`.

Context (not load-bearing for this parent note): the downstream decoration
consumer
`GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_FIRST_HANKEL_TO_DM_BOUNDARY_NOTE_2026-04-19.md`
uses the first-Jacobi/first-Hankel equivalence on this packet.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_packet_theorem_2026_04_19.py
```

Expected:

```text
PASS=5 FAIL=0
```

For the downstream algebraic decoration check, run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_first_hankel_to_dm_boundary_2026_04_19.py
```

Expected:

```text
PASS=4 FAIL=0
```
