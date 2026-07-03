# Gauge Vacuum Plaquette First-Sector Tail Underdetermination Live Packet

**Date:** 2026-04-19; live-source repair 2026-06-08
**Status:** bounded-support packet; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_2026_04_19.py)
**Primary runner cache:** [`logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_2026_04_19.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_2026_04_19.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_note_2026-04-19`.
The archived note failed audit because the declared exact runner was not
available to the restricted packet at the time of audit.

The runner is present on the current repo surface and its cache is fresh. This
note therefore asks re-audit to evaluate the executable finite
underdetermination packet, not the archived missing-runner surface.

## Live Claim

The runner constructs two finite factorized-class extensions:

- a zero extension;
- a positive decaying-tail extension.

It checks that both extensions agree exactly on the specified first-sector
packet and reproduce the same completed three-sample triple, while inducing
different Perron/Perron-Jacobi data for the same source operator `J`.

Current cached runner output records:

```text
retained packet gap zero-vs-tail = 0.000e+00
retained sample gaps zero/tail/pair = 1.777e-16 / 1.777e-16 / 0.000e+00
lambda zero/tail = 3.536529177387 / 3.537984551287
m1 zero/tail = 0.430754683575 / 0.431015307912
m2 zero/tail = 0.249382329102 / 0.249622183928
PASS=6 FAIL=0
```

The live finite certificate verifies:

- both extensions have the same specified first-sector packet;
- both reproduce the completed three-sample triple on the specified projection;
- the tail extension is nonnegative, conjugation-symmetric, and strictly
  positive on every outside-packet weight in the sampled box;
- both transfer operators are self-adjoint, conjugation-symmetric, and positive
  semidefinite on the truncated box;
- the Perron states are numerically unique and separated;
- the induced Perron moments and Jacobi coefficients differ while the specified
  packet is unchanged.

## Boundary

This packet supports only the finite underdetermination statement:

> The specified first-sector projection and completed three-sample triple do not
> determine the higher-tail Perron/Perron-Jacobi data inside the two explicit
> finite extensions constructed by the runner.

It does not claim a full Wilson-environment identification, a continuum gauge
theorem, or effective retained status before independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_TAIL_UNDERDETERMINATION_THEOREM_NOTE_2026-04-19.md`](../archive_unlanded/gauge-vacuum-plaquette-missing-runners-2026-04-30/GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_TAIL_UNDERDETERMINATION_THEOREM_NOTE_2026-04-19.md).
