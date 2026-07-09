# Collapse-Merger Toy Engine Validation -- Gravity's Loop Runs End To End In The Coupled Comparator

**Date:** 2026-07-08
**Type:** exact_support (machinery validation, no physics claim)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/collapse_merger_toy_engine_2026_07_08.py`](../scripts/collapse_merger_toy_engine_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/collapse_merger_toy_engine_2026_07_08.txt`](../logs/runner-cache/collapse_merger_toy_engine_2026_07_08.txt)

## Purpose

A coupled d = 1 comparator in which the season's derived loop runs end
to end: energy parcels fall along the crowding-set clock gradient,
deposit permanent records where they are active (capacity and
availability choked), and records suppress clocks. The fall bias,
parcel model, and kappa are DECLARED comparator couplings (sign and
class structure cited from #5076-#5081); nothing is derived here.

## Validated (supervisor-executed, TOTAL: ENGINE-VALID)

- Parcel conservation exact; record monotonicity exact.
- ATTRACTION SIGN: parcels drift toward a pre-recorded patch at
  z = 8.1 over 20 seeds; the no-record null is sub-sigma. Matter falls
  toward crowding in the coupled toy.
- Husk nucleation exactly where energy sits (fill 0.80 in 31 steps;
  parcel-free control exactly 0).
- Deposition self-chokes as fill grows (offered rate 0.60 -> 0.13 per
  step; both fitted slopes negative).
- Saturated blocks are dynamically excluding: zero interior parcels at
  every step, zero transmission, boundary pile-up profile printed.
- Same-seed determinism: full state hash identical.

Declared conventions (flags): fall bias p_R - p_L = clip(beta
(N_L - N_R)/2); blocked hops wait; formation displaces (not destroys)
parcels to the nearest open site, with a last-open refuge only at total
saturation; the deposition coupling is a rate, converted to a per-step
probability by the Poisson form 1 - exp(-kappa n (A/A0) dt).

## Boundaries

- d = 1 toy; validation only; collapse and merger measurements are the
  next blocks; no audit status.

## Changelog

- **2026-07-08.** Initial engine (worker: gpt-5.6-sol/max, first-draft
  pass), supervisor-reviewed and supervisor-executed.
- **2026-07-09 (supervisor).** Deposition changed from the bare product
  kappa n (A/A0) dt (a rate used directly as a Bernoulli probability,
  which exceeds one on bunched initial states -- both block02 runners
  failed closed on exactly this) to its Poisson conversion
  1 - exp(-rate dt). Identical in the small-rate regime the engine was
  validated in; well-defined at any occupancy. All six validation
  checks re-pass; determinism digests changed with the draw law
  (cache refreshed).
