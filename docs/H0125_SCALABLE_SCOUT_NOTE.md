# H=0.125 Scalable Scout Note

**Date:** 2026-04-06

**Status:** bounded no-go on the observed full-window rows; outside audit-ratified tier.
**Type:** no_go
**Primary runner:** [`scripts/h0125_scalable_scout.py`](../scripts/h0125_scalable_scout.py)
**Runner cache:** [`logs/runner-cache/h0125_scalable_scout.txt`](../logs/runner-cache/h0125_scalable_scout.txt)

This note records the shorter-axial-scale scout for the widened `h = 0.125`
dense `1/L^2 + h^2` bridge lane. It is narrower than the already-closed
full-window width-4 replay and asks whether shortening the axial scale opens
any genuinely wider or more scalable replay path worth keeping.

## Controls

- shorter-scale scout:
  - [`h0125_scalable_scout.py`](../scripts/h0125_scalable_scout.py)
  - `phys_l = 4`
  - `phys_w = 3`
  - `h = 0.125`
  - full window
  - `z_mass = 1.5, 2.0, 3.0`
- retained comparator already closed elsewhere:
  - [`lattice_3d_l2_wide_h0125_replay.txt`](../logs/runner-cache/lattice_3d_l2_wide_h0125_replay.txt)
  - `phys_l = 6`
  - `phys_w = 4`
  - full window
  - `alpha = 0.499`

## Observed Row

- `phys_l = 4`, `phys_w = 3`, full window:
  - `Born = 6.50e-15`
  - clean `k = 0`
  - `TOWARD` gravity `+0.005594`
  - `alpha = 0.501`, `0.501`, `0.502` across `z_mass = 1.5, 2.0, 3.0`

## Readout

The shorter axial scale did not produce a rescue signal in the observed
full-window row. The retained width-4 comparator stays pinned at
`alpha = 0.499`, while the shorter-scale `phys_l = 4`, `phys_w = 3` scout
only reaches `alpha = 0.501`, `0.501`, `0.502` across the tested masses.

That is a clean bounded no-go for the observed full-window rows. On this
executed `phys_l = 4`, `phys_w = 3`, three-mass slice, there is no rescue
signal for a genuinely wider or more scalable replay path; no untested family
or asymptotic statement is claimed.
