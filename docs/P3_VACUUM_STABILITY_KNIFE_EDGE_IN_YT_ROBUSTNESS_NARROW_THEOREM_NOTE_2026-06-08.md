# P3 Vacuum Stability Is a Knife-Edge in y_t

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Type:** robustness and conditionality analysis of an existing prediction
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/p3_vacuum_stability_pressure_test_2026_06_08.py`](../scripts/p3_vacuum_stability_pressure_test_2026_06_08.py)
**Runner cache:**
[`logs/runner-cache/p3_vacuum_stability_pressure_test_2026_06_08.txt`](../logs/runner-cache/p3_vacuum_stability_pressure_test_2026_06_08.txt)

## Scope

This note pressure-tests the headline P3 vacuum-stability forecast in
[`HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md`](HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md).
The source forecast says the Higgs vacuum is absolutely stable because the
framework top Yukawa value

```text
y_t(v) = 0.918
```

is below the admitted SM stability comparator

```text
y_t,crit ~= 0.93  at m_H = 125.25 GeV.
```

The question here is narrower: is that binary statement robust under the
source note's own `+-3%` `y_t` systematic and open `y_t` Ward gate?

## Finding

The forecast is a central-value call, not a robust binary.

The framework band is

```text
y_t(v) = 0.918 +- 3% = [0.890, 0.946].
```

The stability comparator `y_t,crit ~= 0.93` lies inside that band. In the
source note's sigma convention, the boundary is only `0.44 sigma_sys` above the
central value, giving a Gaussian-tail diagnostic of about `33%` on the
metastable side. If the `+-3%` band is instead read as a hard interval, about
`29%` of the interval lies above the comparator. Either way, the
stable/metastable verdict flips inside the framework's stated `y_t` uncertainty.

Therefore P3 should not be advertised as "absolutely stable" in the robust
binary sense. The honest statement is:

> central-value stable; conditional beyond-SM `y_t` signature; not robust until
> the `y_t` gate is tightened below the margin to the stability boundary.

## Why This Is Still Useful

The note does not say the vacuum is metastable. The central value remains on the
stable side. The durable content is that the framework predicts a lower `y_t`
than the SM extraction used by the comparator lane; if that lower value becomes
retained with a smaller uncertainty, it would be a genuine beyond-SM stability
signature.

The runner's one-loop SM RGE integration is only a qualitative grounding check:
it confirms that the Higgs quartic sign is steeply sensitive to `y_t` in the
same neighborhood. The precise boundary is the literature comparator already
used by the P3 source note, not a newly derived framework value.

## Load-Bearing Inputs

- [`HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md`](HIGGS_VACUUM_STABILITY_NEW_PHYSICS_DISCRIMINATION_NOTE_2026-05-03.md)
  supplies the P3 forecast, `y_t(v) = 0.918`, the `+-3%` systematic, the
  `y_t,crit ~= 0.93` comparator, and the open `y_t` Ward gate.
- [`HIGGS_VACUUM_EXPLICIT_SYSTEMATIC_NOTE.md`](HIGGS_VACUUM_EXPLICIT_SYSTEMATIC_NOTE.md)
  records the inherited Higgs/vacuum systematic surface.

The imported comparator content is explicit: `m_H = 125.25 GeV`, the SM `y_t`
extraction, and the stability boundary near `0.93`. They are not derived here.

## What This Does Not Claim

- It does not derive `y_t(v)`.
- It does not derive the SM stability boundary.
- It does not derive `m_H`.
- It does not claim the vacuum is metastable.
- It does not dispute the source note's central-value discrimination framing.
- It does not add a new axiom, primitive, selector, fitted value, or audit
  verdict.

## Verification

```bash
python3 scripts/p3_vacuum_stability_pressure_test_2026_06_08.py
```

Expected result: `TOTAL: PASS=4 FAIL=0`.
