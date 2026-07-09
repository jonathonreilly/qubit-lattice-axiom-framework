# Two Frozen Stars Merge By Bridging -- Husks Never Move, The Between-Region Ossifies First

**Date:** 2026-07-08 (measured 2026-07-09)
**Type:** bounded comparator measurement (no derivation)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/merger_bridging_2026_07_08.py`](../scripts/merger_bridging_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/merger_bridging_2026_07_08.txt`](../logs/runner-cache/merger_bridging_2026_07_08.txt)
**Engine / frozen-star conventions:**
[`scripts/collapse_merger_toy_engine_2026_07_08.py`](../scripts/collapse_merger_toy_engine_2026_07_08.py),
[`scripts/collapse_frozen_star_2026_07_08.py`](../scripts/collapse_frozen_star_2026_07_08.py)

## Claim scope

Two-star merger in the coupled d = 1 comparator, run to
TOTAL: MERGER-BY-BRIDGING (all six checks, exit 0). Two 150-parcel
Gaussian blobs (sigma 8) at separation 60 on the 400-site ring,
kappa = 0.001, T = 6000, seed 20260708. Comparator phenomenology of the
declared toy; no derivation; no audit status.

## What the run exhibits

1. **Husks never translate (exact).** Each star's husk, anchored at its
   density-peak component and tracked by containment continuity, passes
   a site-set superset assertion at every step through the merge: a
   husk only gains sites; nothing it holds is ever lost or shifted.
   This is record permanence doing the work the area theorem does in
   GR, and it is exact, not statistical.
2. **Merger completes by bridging, the only channel available.** The
   clock well is nearest-neighbor, so distant husks exert no attraction
   on each other, and records cannot move: the merger junction must be
   deposited. Measured: the two husks become one connected component at
   t_bridge = 3720, the junction interval between their facing surfaces
   is fully recorded at the bridge step, and both far flanks are 100%
   open at that moment -- the between-region saturates first. This is
   the pair-of-pants picture from the 2026-07-09 merger thought-pass,
   now as numbers.
3. **Area analog (exact gate).** Total record count is monotone
   (asserted every step), and the merged husk mass (140) is >= the sum
   of the two pre-merger husk masses (51 + 88): husk area never
   decreases through a merger.
4. **The exterior survives.** Exterior open fraction 0.507 at T -- a
   merger inside an intact universe, not the saturation endgame.
5. **Memory imprint exhibited.** The far-exterior quarters (>= 30 sites
   from any pre-merger husk surface) carry a SPARSE permanent record
   shell at T (fill 0.207, gate <= 0.3) with a permanent clock
   suppression of 0.635 at the 9 record-adjacent far sites, and those
   records never clear (asserted). Post-bridge outward marker flux is
   small (3 crossings) -- at this kappa the imprint is laid mostly by
   diffusing shell leakage over the run, not by a burst; reported as
   measured.

## The identity lesson (measured, then declared)

The first draft reused the frozen-star block's husk selector (largest
blob-overlapping component, re-run every snapshot) for identity over
time. Measured result: it flickers between fragments early (first
violation t = 12) and aliases both stars onto one component late
(t = 2950), corrupting the channel and area gates while the underlying
records behave perfectly. The corrected convention -- anchor at the
peak component, track by containment continuity -- is exact because
records are permanent, so components only merge and never split. The
per-snapshot selector remains correct for what block02 used it for
(end-state anatomy); it is unsuitable for identity, and the runner's
SPEC-NOTE declares both facts.

## Boundaries

- d = 1 comparator with supplied couplings; separation, blob masses,
  and kappa are declared devices. The "radiated burst" leg of the
  original spec did not occur at this kappa (no significant
  bridge-epoch outward flux); the memory shell here is leakage-laid and
  the note claims exactly that. A burst-driven memory leg would need a
  driven release, which would be a new declared device.

## Changelog

- **2026-07-09.** Worker draft (gpt-5.6-sol/max) delivered the full
  protocol with an honest PARTIAL and a precise diagnosis of the
  selector-identity failure (its own SPEC-NOTE documented the aliasing
  it measured). Supervisor patch: anchored containment-continuity
  identity (one iteration); all six checks pass unchanged in
  definition except the identity convention, which is declared above.
