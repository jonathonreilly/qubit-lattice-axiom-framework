# Collapse In The Coupled Toy -- The Frozen-Star Anatomy As Numbers

**Date:** 2026-07-08 (measured 2026-07-09)
**Type:** bounded comparator measurement (no derivation)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/collapse_frozen_star_2026_07_08.py`](../scripts/collapse_frozen_star_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/collapse_frozen_star_2026_07_08.txt`](../logs/runner-cache/collapse_frozen_star_2026_07_08.txt)
**Engine:**
[`scripts/collapse_merger_toy_engine_2026_07_08.py`](../scripts/collapse_merger_toy_engine_2026_07_08.py)
(validated in the block01 note; Poisson deposition form per its changelog)

## Claim scope

Single-blob collapse in the coupled d = 1 comparator, run to
TOTAL: FROZEN-STAR-EXHIBITED (all six checks, exit 0). A Gaussian energy
blob (300 parcels, sigma 10) on the 400-site ring, kappa in
{0.00025, 0.001}, T = 3000, seed 20260708. Everything here is
comparator-unit phenomenology of the declared toy; no derivation, no
audit status.

## What the run exhibits

1. **The self-formed husk gravitates (the collapse feedback link).**
   Two-phase probe: the blob self-forms its husk under the true dynamics
   (kappa = 0.001, t = 1000), then deposition is frozen (hop-only, so no
   cage can form) and a uniform 300-parcel probe bath runs 300 steps.
   Net accepted hop flux toward the record set at its distance-2 entry
   ring: active +323.3 vs beta = 0 control +1.2, paired over 10 seeds,
   z = +9.5. The structure the blob built pulls fresh energy in; without
   the fall bias the same structure pulls nothing.
2. **Husk growth is monotone and peak-anchored.** H(t) non-decreasing
   exactly at both kappas; at kappa = 0.001 the selected husk (136 of
   146 records in one connected component) contains the initial density
   peak. At kappa = 0.00025 nucleation is fragmented (24 small cages,
   largest 10 sites, off-peak) -- the proto-star regime, reported not
   gated.
3. **Capacity caps the core (no singularity).** Record density never
   exceeds one per site (exact assert), and no single site condenses the
   supply (max site occupancy 211 of 300 parcels at kappa = 0.001,
   gate 240 = 0.8 Np). The pile is a boundary shell, not a divergence.
4. **The exterior clock freezes as the husk grows.** Boundary-ring clock
   trend negative at z = -8.9 (kappa 0.001) and z = -43.8 (kappa
   0.00025), asymptoting toward the availability floor.
5. **Frozen-star anatomy.** At T = 3000, kappa = 0.001: husk 136 sites,
   bound shell 278/300 parcels (0.927) within 3 sites of the husk
   surface, unbound (>10 from the husk) 7/300 (0.023), exterior open
   fraction 0.635. The star is a record husk plus a bound
   unrecorded-energy shell, with an intact exterior.
6. **Ossification law, two regimes.** Supply-starved (kappa = 0.00025,
   parcels leak from the fragmented proto-star): growth decelerates
   (late d2 < 0). Capture-fed (kappa = 0.001): growth continues and
   ACCELERATES (late-time power fit alpha = 1.47; infall concentrates
   the boundary pile, raising the deposition offer). The pre-run
   expectation "ossification decelerates" (from the 2026-07-09 merger
   thought-pass) holds in the starved regime only; the capture-fed
   correction is a finding of this block, not a gate relaxation --
   deceleration is not claimed where the toy shows acceleration.

## Regime and design choices (declared)

- **Record-mediated gravity has no pre-nucleation channel.** With no
  records there is no clock gradient; a fresh blob diffuses first. The
  spec's original "contract before husk formation" Jeans gate was
  physically impossible in this engine and was replaced by the two-phase
  probe above.
- **Caging confound.** At matched kappa, every end-state occupancy or
  concentration statistic fails to separate fall-bias-on from
  fall-bias-off in d = 1: records form where parcels are in both legs,
  and unbiased 1-d diffusion is recurrent, so even beta = 0 cages
  coalesce (measured: husk-share z < 1.5 at t in {1000, 3000}). The
  kappa = 0 probe phase is what isolates the pull. This is a real d = 1
  limitation of occupancy statistics, documented so later blocks do not
  rediscover it.
- **Star-with-exterior budget.** kappa in {0.005, 0.02} (the spec's
  first choice) saturates the entire ring by t <= 2000 -- the
  global-saturation endgame, not a star. The budget was cut to keep the
  exterior open (gate >= 0.30; measured 0.635 / 0.863).
- Capture and escape are measured from the husk surface; a fixed
  ring-centre radius sits inside a grown husk and misreads the bound
  shell as escape.

## Boundaries

- d = 1 comparator with supplied couplings; the fall bias, kappa, and
  parcel model are declared devices. Merger (two blobs, bridging, the
  husk-monotonicity area analog, the radiated memory imprint) is the
  next block.

## Changelog

- **2026-07-09.** Worker draft (gpt-5.6-sol/max) failed closed on the
  engine's bare-product deposition probability exceeding one for the
  bunched blob -- correct behavior, root cause in the engine; fixed
  there (Poisson conversion, engine note changelog). Supervisor then
  revised the spec's checks against the measured physics across five
  runs: (1) budget cut to the star-with-exterior regime
  (kappa {0.005, 0.02} -> {0.00025, 0.001}, T 6000 -> 3000, exterior
  gate added); (2) impossible pre-nucleation Jeans gate replaced by the
  two-phase self-formed-husk probe, after fixed-radius tail, husk-share,
  and occupancy-capture statistics all proved caging-confounded
  (z = +1.3 / +0.95 / +1.7); the decisive form is the engine's own
  cumulative entry-ring flux statistic (z = +9.5); (3) peak-containment
  gated at the anatomy kappa only (low-kappa fragmentation reported);
  (4) no-condensation gate replaces the arbitrary 60-parcel pile gate;
  (5) ossification law split into starved/capture-fed regimes as
  measured. All revisions are visible in the runner's SPEC-NOTE.
