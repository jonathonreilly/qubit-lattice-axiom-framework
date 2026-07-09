# The Registration Yield kappa(theta) Measured -- Baseline-Subtracted Registration, The Recurrence Floor, And A Non-Empty Sparsity Window

**Date:** 2026-07-08
**Type:** bounded_theorem (measured comparator legs with declared proxies)
**Claim type:** bounded_theorem
**Claim scope:** On the gauged comparator (N = 12, g in {0.6, 1.0}, two
strictly local unitary kicks), the deposition-per-activity function
kappa(theta) = (first-registrations per site) / (integrated bond
activity) is measured under declared proxies: registration = upward
crossing of the EXCESS distinguishability (1 - bond purity, minus the
per-bond interacting-ground-state baseline 0.27-0.49) through a
threshold theta; one registration per site (the axiom-shaped counter);
re-arm crossings reported as coherent-recurrence context. Results:
kappa falls with threshold (median log-log exponent -0.81); the
registration cascade is transient-complete above the threshold floor
(theta >= 0.2) while below it a closed coherent ring produces late
first-crossings indefinitely (no quiescence exists -- the yield is
well-defined only above a floor, itself a finding); and the
DEPOSITION-SPARSE WINDOW IS NON-EMPTY: for theta >= 0.2 the translated
fill-per-dwell falls below the campaign-6 wake bound 0.3 in comparator
units. Reading: the phenomenology constraint is satisfiable exactly
when registration is a genuinely thresholded (measurement-grade)
event. The registration threshold is not axiomatic; kappa is a
per-transient yield (driven steady-state rate = named follow-up); the
QD bridge remains a named premise. Sets no audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/deposition_per_activity_kappa_2026_07_08.py`](../scripts/deposition_per_activity_kappa_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt`](../logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt)

## Boundaries

- Declared proxies only (purity-based distinguishability, bond
  activity); crossings are sampled and convention-dependent (both
  conventions printed); comparator units; no formation rule chosen;
  no gravity claim.
- Supervisor-executed result: `TOTAL KAPPA-MEASURED failed=none`
  (checks: stationary control exact zero; locality of early events
  exact; monotone kappa(theta); sparse-window-theta >= 0.2).

## Changelog

- **2026-07-08.** Worker draft (gpt-5.6-sol/max) honestly failed itself
  on absolute thresholds (GS entanglement baseline); supervisor added
  baseline subtraction, fixed a cross-check ordering bug in the first
  patch, reframed the stationarity gate to per-transient yield with the
  once-per-site counter, and located the recurrence floor. Five
  documented iterations, supervisor-executed.
