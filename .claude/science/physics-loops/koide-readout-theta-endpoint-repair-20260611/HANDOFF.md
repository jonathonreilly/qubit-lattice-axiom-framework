# Handoff

This block targets the audited-conditional Koide readout demarcation row.

Changed source packet:

- `docs/KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md` now distinguishes
  `t=0` single-pole collapse from `t=1` physical unit residues in the
  `Z=(1,t,t)` family.
- `scripts/frontier_koide_readout_lane_demarcation_2026_05_30.py` now asserts
  the endpoint behavior explicitly:
  `Z=(1,1,1)` is theta-independent but keeps `r` free, `Z=(1,0,0)` is collapse
  with `Q=1`, and `Z=(1,1/2,1/2)` remains theta-dependent.
- `logs/runner-cache/frontier_koide_readout_lane_demarcation_2026_05_30.txt`
  is refreshed through the repo cache utility and reports `PASS=13 FAIL=0`.

Reviewer focus:

- Confirm that the t=1 unit-residue branch is not misread as selecting
  `r=1/2`.
- Confirm that the t=0 collapse branch is not treated as a valid three-mass
  selector.
- Confirm that no generated audit data or ledger verdict file is included.

Remaining status:

Independent audit owns any effective status change.
