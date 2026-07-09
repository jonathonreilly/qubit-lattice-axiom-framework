# Record Mobility Spot Probe -- What Motion Would Buy, What It Would Cost, Measured

**Date:** 2026-07-08
**Type:** exact_support (owner-requested exploratory probe; comparator
measurements only, no axiom change made or proposed)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/record_mobility_spot_probe_2026_07_08.py`](../scripts/record_mobility_spot_probe_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/record_mobility_spot_probe_2026_07_08.txt`](../logs/runner-cache/record_mobility_spot_probe_2026_07_08.txt)

## Question

If records could hop between sites (one-per-site exclusion kept), which
of the objections raised against mobility actually bite? Four measured
answers (probe conventions and their limits in the runner SPEC-NOTE;
the anchoring toy's K > L tension is declared -- its diffusion curve is
an abstract position stress test):

1. **Geometry anchoring survives source-following motion.** Causal-order
   consistency of the record configuration: `C = 0.961` after co-moving
   advection (gate `>= 0.95 x` baseline) -- records that share their
   source's displacement keep their causal relations. Diffusion, by
   contrast, degrades anchoring slowly and monotonically (half-life
   `> 200` hop steps, curve printed). The June-arc objection bites
   DIFFUSIVE mobility, not advective.
2. **The wake relocates with the source.** With a half-ring transit at
   calibrated partial fill: path suppression falls `0.237 -> 0.070`
   while the virgin half rises `0.070 -> 0.263`; relocation balance
   `0.87` (geometry-free gate `0.7-1.3`), crowding conserved exactly.
   Mobility does what its proposer said: crowding rides with the
   records. Residuals are understood (zone-width overhang, ring wrap,
   and exclusion drag -- at finite trail density co-moving records lag
   their source at the exclusion-limited speed).
3. **Saturated cores stay frozen; only boundaries peel.** One-per-site
   exclusion means a vacancy-free interior admits NO motion: strict
   layer-by-layer evaporation verified exactly (interior sites
   immobile until they become boundary; per-layer first-move times
   `1 / 33 / 131 / 259 / 282`). Mobility does NOT thaw the framework's
   horizon-flavored interiors -- it gives them surface evaporation.
4. **Frozen pockets thaw.** The strong-crowding termination phenomenon
   (open sites frozen by recorded neighborhoods) is erased by
   diffusion: `27.6` percent of frozen-open sites form after vacancies
   drift in, and terminal occupancy goes to `1.0` (vs `0.65` frozen).
   The frozen-pocket exhibit is a fixed-record result; mobility trades
   it for evaporation physics.

## Reading (probe-level, not a ruling)

Source-following mobility is cheaper than initially argued: geometry
anchoring and saturated-core physics survive it, and it performs its
advertised job on the wake. Its remaining costs are real but smaller
than claimed: the frozen-pocket phenomenon is lost, co-moving records
lag at the exclusion speed (a testable drag signature), and a motion
law would still be new supplied content. Separately, the same-day
saturation leg showed the FIXED-record wake self-regulates (sub-
geometric accumulation; aged wake reduces to convention), so mobility
is no longer NEEDED for Newtonian shape -- the choice between fixed
and mobile records is now a choice between two viable phenomenologies
(fixed: frozen pockets + transient scalar-memory wake; mobile:
evaporating cores + exclusion drag), not a rescue operation.

## Boundaries

- d = 1 comparator toys; the anchoring leg is an abstract stress test;
  no motion law is proposed; no axiom text is touched; sets no audit
  status.

## Changelog

- **2026-07-08.** Initial probe (owner-requested). Run 1's wake leg was
  unmeasurable by construction (full-ring path at saturating fill);
  corrected to half-ring transit at calibrated partial fill with the
  balance gate; documented here.
