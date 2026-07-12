# Local Activity Bound And Finite Toy Witnesses Conditional On A Record-Opportunity Bridge

**Date:** 2026-07-08
**Type:** bounded_theorem
**Primary runner:**
[`scripts/activity_energy_bound_witnesses_2026_07_08.py`](../scripts/activity_energy_bound_witnesses_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/activity_energy_bound_witnesses_2026_07_08.txt`](../logs/runner-cache/activity_energy_bound_witnesses_2026_07_08.txt)

## Exact Bound

For a normalized finite-dimensional state `rho`, a Hamiltonian
`H = sum_X h_X`, and a region `R`, define

```text
a_R = || Tr_(R^c)(-i[H,rho]) ||_1.
```

Terms disjoint from `R` vanish after the partial trace. Contractivity,
the triangle inequality, and
`||[h_X,rho]||_1 <= 2 ||h_X|| ||rho||_1` give

```text
a_R <= 2 sum_(X intersects R) ||h_X||.
```

This is a spectral/operator-norm activity bound. It bounds local reduced-state
change by the scale of Hamiltonian terms touching the region. It does not say
that a nonzero energy expectation forces nonzero activity.

## Finite Toy Witnesses

The runner also records bounded numerical witnesses on declared one-dimensional
comparators.

- One selected stationary eigenstate has numerically zero reduced-state
  activity while retaining nonzero local energy expectation.
- A localized fixed-particle basis state has zero activity in the sampled far
  region at the tested initial time.
- A separately prepared Gaussian packet is evolved, and its activity/energy
  profiles are compared at the declared sample times.
- A moving one-particle packet has bond-activity and absolute bond-energy
  profiles with the printed overlaps and centroid separations.
- A dense three-site local-term model independently checks the norm bound on
  random states, and a one-particle chain supplies the empty-region and moving
  packet diagnostics.

These are toy witnesses, not a general energy-to-registration theorem.

## Explicit Bridge Premise

Any use of the activity proxy as a record-formation opportunity additionally
supplies the comparator premise `AO`: interpret the declared activity
observable as an opportunity proxy. `AO` is explicitly supplied here; this
note and runner do not attempt to derive it, a formation rule, a registration
threshold, or a deposition probability.

## Boundaries

- The exact inequality is finite-dimensional and uses the declared local-term
  decomposition.
- The profile comparisons use unthresholded bond-activity and absolute
  apportioned bond-energy arrays, with full-profile overlaps and centroids at
  finite sample times. They are diagnostics, not identities.
- The dense three-site model and one-particle chain, including their terms,
  preparation choices, sizes, mass, and finite times, are supplied.
- No gravity conclusion or physical sourcing law is made.

## Dependencies

None. The operator inequality and toy comparators are self-contained; the
optional record-opportunity reading uses the explicitly supplied `AO` premise
rather than a derived dependency.
