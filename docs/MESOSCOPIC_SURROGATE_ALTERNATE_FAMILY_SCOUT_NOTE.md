# Mesoscopic Surrogate Alternate-Family Scout Note

**Date:** 2026-04-04  
**Status:** support/meta planning index; not a theorem
**Type:** meta
**Claim type:** meta
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/mesoscopic_surrogate_alternate_family_scout.py`

## 2026-05-31 Audit Repair (support/meta scope)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The runner confirms the cited notes contain the expected frozen-evidence markers, but it does not compute or enforce an objective ranking for 'cheapest plausible next target'. The direct dependency packet also includes a persistent-inertial"*

with repair: *"missing_bridge_theorem: Add an explicit registered
ranking/priority criterion over the cited retained rows, or retag this note as
a support/meta planning index rather than a bounded theorem."*

Supplying a retained objective-ranking theorem would be substantive new work and
would not be justified by the current runner. This revision therefore takes the
auditor's support/meta path:

- **Load-bearing (in scope):** The runner verifies that the cited upstream
  notes (`MESOSCOPIC_SURROGATE_LOCALIZATION_FRONTIER_NOTE`,
  `MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE`, and
  `SAME_FAMILY_3D_CLOSURE_NOTE`) contain the expected frozen-evidence markers
  ruling out the `h=0.5` and 2D threshold lanes.
- **Non-load-bearing planning recommendation:** The positive ranking conclusion
  that the retained 3D `h=0.25` family is the "cheapest plausible next target"
  is an editorial planning recommendation. It is not derived from a registered
  objective ranking criterion and must not be cited as theorem content.

No new axiom, import, or retained bridge is introduced. The row is a
support/meta index over already-cited evidence, not a bounded theorem about the
priority ordering.

## Question

Which already-bounded non-Gate-B family is the cheapest plausible next target
for a more localized source object, if we want to beat the retained 3D
`h=0.5` mesoscopic-surrogate family?

## Frozen evidence

The current mesoscopic-surrogate lane already freezes three useful facts:

- the retained 3D `h=0.5` localization frontier does **not** reward sharp
  localization
  - the only numerical winners are degenerate point-like cases
  - once the family is meaningfully localized, `topN` remains the least-bad
    mesoscopic control
- the retained 2D support-threshold scan also does **not** show a sharp
  collapse
  - every scanned `topN` from `1` to `81` stayed stable
  - shrinking support is not the lever there
- the retained 3D `h=0.25` family is already the strongest bounded ordered
  family for the asymptotic bridge
  - same-family closure exists
  - the near-Newtonian finite-size bridge is much cleaner than the coarse
    `h=0.5` family

## Scout result (planning recommendation, not theorem content)

The cheapest already-bounded family that still plausibly has room for a more
localized source object to matter is:

- the retained 3D ordered-lattice family at `h = 0.25`

Why this family:

- it is already bounded on `main`
- it has the best retained continuum-like resolution among the mesoscopic
  ordered-lattice families
- the `h = 0.5` frontier is already closed as a degenerate-point-source lane
- the 2D lane is already closed as a no-threshold lane

## Recommendation

If we do another localization attempt, it should be:

- on the retained 3D `h = 0.25` family
- with non-degenerate localized shapes only
- with an explicit minimum support or capture floor so point-like winners are
  excluded by construction

Good candidate families:

- annular windows
- tapered ellipsoids
- compact Gaussians with enforced capture floor

## Extra cheap check

A later constrained compact-floor sweep on the retained 3D `h = 0.5`
family did not overturn the broad-source conclusion:

- compact Gaussian and tapered families can survive the floors
- but `topN` still remains the least-bad mesoscopic control on that family

So the extra cheap check reinforces the same recommendation:

- do not keep sweeping `h = 0.5`
- if localization is worth trying again, use the retained 3D `h = 0.25`
  family instead

## Safe read

The honest recommendation is:

- do **not** keep sweeping the 3D `h=0.5` frontier
- do **not** keep hunting a 2D threshold
- if a more localized source object is still worth trying, the retained 3D
  `h=0.25` family is the cheapest plausible target

If that family still cannot beat the broad mesoscopic control, the localization
lane should be frozen as a bounded negative result.

## Context references

These are context references for a planning index, not one-hop theorem
dependencies for a retained claim:

- [MESOSCOPIC_SURROGATE_LOCALIZATION_FRONTIER_NOTE.md](MESOSCOPIC_SURROGATE_LOCALIZATION_FRONTIER_NOTE.md) — retained 3D `h=0.5` localization frontier whose negative result motivates this scout.
- [MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md](MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md) — companion sweep evidence.
- [MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE.md](MESOSCOPIC_SURROGATE_THRESHOLD_2D_NOTE.md) — retained 2D support-threshold scan.
- [SAME_FAMILY_3D_CLOSURE_NOTE.md](SAME_FAMILY_3D_CLOSURE_NOTE.md) — retained 3D family closure referenced by the scout.
- [VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md](VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md) — asymptotic-regime bridge consulted as part of the alternate-family scan.
- [PERSISTENT_INERTIAL_RESPONSE_READINESS_NOTE.md](PERSISTENT_INERTIAL_RESPONSE_READINESS_NOTE.md) — readiness gate for the persistent inertial-response family this note evaluates as a candidate target.
