# Kappa Translated -- Trail Density, Body Mobility, And Ossification In One Comparator

**Date:** 2026-07-08 (measured 2026-07-09)
**Type:** bounded comparator measurement (no derivation)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/ossification_mobility_translation_2026_07_08.py`](../scripts/ossification_mobility_translation_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/ossification_mobility_translation_2026_07_08.txt`](../logs/runner-cache/ossification_mobility_translation_2026_07_08.txt)
**Engine:**
[`scripts/collapse_merger_toy_engine_2026_07_08.py`](../scripts/collapse_merger_toy_engine_2026_07_08.py)
(Poisson deposition form per its changelog)
**Kappa provenance:** the deposition-per-activity function measured in
[`docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md`](DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md)
(cited for meaning only; values here are a comparator sweep).

## Claim scope

Block02 of the deposition-constant campaign: kappa swept over five
decades (1e-6 .. 1e-2) in the coupled toy, translated into the two
phenomenological handles -- the moving-body trail and the
collapsed-body ossification -- with the joint sparse window printed.
TOTAL: WINDOW-MAPPED (exit 0). Declared comparator; comparator units;
no derivation; no audit status.

## Measured (seed 20260708; Leg A means over 5 spawned seeds)

| kappa | trail fill d | mobility m | ossification o |
|-------|--------------|------------|----------------|
| 1e-6  | 0.0000       | 0.997      | 0.016          |
| 1e-5  | 0.0071       | 0.658      | 0.024          |
| 1e-4  | 0.119        | 0.190      | 0.200          |
| 1e-3  | 0.641        | 0.079      | 0.375          |
| 1e-2  | 1.000        | 0.167 (ratchet) | 0.769     |

- Leg A: 120-parcel sigma-6 blob driven by a declared +0.15 p_R wind
  across a 200-site horizon (667 steps); d = record fill on the swept
  corridor, m = capped maximum forward centroid progress / 200.
- Leg B: same blob, no wind, T = 4000; o = husk / (husk + parcels).

## The four gated statements

1. **Monotone handles.** Trail fill and ossification are monotone
   nondecreasing in kappa (5/5 order statistics each).
2. **The mobile-sparse window is non-empty.** At kappa = 1e-6 the body
   crosses the full horizon essentially freely (m = 0.997) and paints
   no trail (d = 0.0000): a mobile, sparse-depositing body exists.
3. **The fossil-anchor regime is real.** At kappa = 1e-3 mobility is
   gone (m = 0.079): heavy deposition anchors bodies. The window
   statement has teeth on both sides.
4. **Mobility forces sparsity.** The largest kappa that leaves a body
   mobile (m >= 0.8: kappa_mob = 1e-6) sits FOUR DECADES below the
   smallest kappa that ossifies a stationary body within the run
   (o >= 0.5: kappa_oss = 1e-2). In this comparator, any body that
   moves is automatically a sparse depositor -- the comparator-level
   version of the season's deposition-sparsity premise, now exhibited
   rather than assumed (compare the P-DEPOSITION-SPARSE weakening in
   the season synthesis).

## Two transport modes (declared)

A single record is a TOTAL barrier on a line, so coherent transport
survives only while the body's own core has deposited nothing; the
pinning scale is therefore the d = 1 extreme, and in d >= 2 open-site
bypass would widen the mobile window. At kappa = 1e-2 the centroid
moves again (m = 0.167, trail fill 1.0, ring husk saturates): this is a
deposit-displace ratchet -- formation relocates parcels to the nearest
open site -- not coherent mobility. It is flagged RATCHET, excluded
from the window by its own trail fill, and excluded from the
monotonicity gates (which run on d and o only, for exactly this
declared reason). The ratchet is the same boundary-peeling mechanic the
frozen-star block sees at husk surfaces.

## Boundaries

- Comparator units throughout: kappa here is the toy's per-parcel rate,
  not the theta-sweep kappa of block01 (that mapping is cited for
  meaning, not numerically bridged). The wind, blob mass, and horizon
  are supplied devices; the window edges scale with them (trail fill
  per site ~ 1 - exp(-kappa Np / v)), so the four-decade separation,
  not the absolute edges, is the load-bearing number.
- Anchoring time in Leg B (first 500-step +/-2 confinement) is reported
  only; a stationary undriven blob trivially anchors at low kappa.

## Changelog

- **2026-07-09.** Worker draft (gpt-5.6-sol/max) failed closed on the
  engine's bare-product deposition probability (root-caused and fixed
  in the engine -- Poisson conversion) and, honestly, on its own gates:
  the spec's sweep (1e-3 .. 1e-1) sat entirely above the mobile window,
  and at high kappa the ratchet mode produced m > 1 and non-monotone
  mobility. Supervisor rewrite: sweep extended down to 1e-6, Leg A
  averaged over 5 seeds, mobility capped at the horizon and measured as
  maximum forward progress, monotonicity gated on trail/ossification
  only with the two-mode structure declared, and the
  mobility-forces-sparsity separation gate added (it is the physics
  payoff of the sweep). Verdict trichotomy WINDOW-MAPPED /
  WINDOW-NOT-EXHIBITED / MACHINERY-FAIL so a physics miss cannot
  masquerade as machinery failure.
