# Geometry Lane Head-to-Head Note — Four-Configuration Runner Table (Binding)

**Date:** 2026-04-02 (scope narrowed 2026-05-17 per audited_conditional `scope_too_broad` repair: binding scope is the finite four-configuration runner table; top-lane-selection and same-readout-implementation interpretation requires explicit audited dependency edges)
**Status:** bounded finite four-configuration runner table only;
top-lane-selection / same-readout-implementation interpretation is
out-of-binding-scope without explicit audited dependency edges.
**Primary runner:** `scripts/geometry_lane_head_to_head.py`

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"split the clean bounded
core as a finite four-configuration runner table, or add explicit
audited dependency edges for the top-lane selection and same-readout
implementation."*

This revision takes the splitting option. The binding evidence of
this note is exactly the **finite four-configuration runner table**
from `scripts/geometry_lane_head_to_head.py` on the declared 16
matched-seed grid (`npl = 25`, `y_range = 12`).

The broader "top-lane selection" interpretation (i.e. promoting one
lane as the head-to-head winner) and the "same-readout
implementation" claim across geometry lanes are **demoted to
out-of-binding-scope**. Promoting either requires explicit audited
dependency edges for (a) the lane-selection criterion and (b) the
shared-readout implementation across all compared lanes. Neither
dependency surface is supplied here.


## Setup

This note compares the best bounded hard-geometry lanes on exactly the
same seeds and the same readout:

- `16` matched seeds
- `npl = 25`
- `y_range = 12`
- `connect_radius = 3.0`
- `N = 25, 40, 60, 80, 100`
- readout: `pur_min` under layer normalization, plus gravity mean and
  `g/SE`

Compared lanes:

1. imposed modular gap = 2
2. imposed modular gap = 4
3. central-band removal `|y-center| < 1`
4. central-band removal `|y-center| < 2`

Source log:
[logs/2026-04-02-geometry-lane-head-to-head.txt](/Users/jonreilly/Projects/Physics/logs/2026-04-02-geometry-lane-head-to-head.txt)

## Results

| N | Best decoherence | Best joint coexistence | Notes |
|---|---|---|---|
| 25 | modular gap=2 (`pur_min 0.619`) | modular gap=4 or gap=2 | modular remains strongest at small `N` |
| 40 | central `|y|<1/2` (`pur_min ~0.735`) | central `|y|<2` (`g/SE +2.0`) | central-band clearly wins here |
| 60 | modular gap=4 (`pur_min 0.769`) | modular gap=4 (`g/SE +1.9`) | best matched modular pocket |
| 80 | modular gap=2 (`pur_min 0.852`) | central `|y|<1` (`g/SE +2.6`) | decoherence vs gravity tradeoff |
| 100 | central `|y|<2` (`pur_min 0.876`) | central-band slightly cleaner | modular gap=2 gravity turns negative |

Removal fractions are modest and stable:

- `|y-center| < 1`: about `8.5-8.6%`
- `|y-center| < 2`: about `16.2-17.2%`

## Safe interpretation

There is **no single universal winner** across the whole matched sweep.

What is established:

- imposed modular gaps are still the strongest decoherence lane at the
  smallest `N`
- central-band removal is a real competing hard-geometry lane
- central-band removal often gives cleaner positive gravity than the
  imposed modular gaps at larger `N`
- by `N=100`, central-band removal is the better balanced lane in this
  matched comparison

What is not established:

- that central-band removal dominates modular gaps at all `N`
- that any one bounded hard-geometry lane has already solved the
  asymptotic problem

## Practical conclusion

The repo should keep **both** of these as top bounded geometry lanes:

1. **imposed modular gap + layer norm**
   - strongest small-`N` decoherence
2. **simple central-band removal + layer norm**
   - simpler hard-geometry rule
   - competitive through `N=100`
   - often cleaner on the gravity side

The next clean discriminator is not another broad sweep. It is a
same-family gravity-law cleanup on the best `N=80-100` pockets from
both lanes.

---

**Re-queued for re-audit 2026-05-17:** previous `unaudited` verdict cited packet incompleteness (missing helper-script imports from the restricted packet). The audit pipeline now populates `helper_runner_paths` per [PR #1371](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1371) so the next audit pass receives the complete packet. Helpers now declared: ``. The current re-queue is mechanical — no science content changes — and is documented here so the hash drift is explicit.
