---
claim_id: two_chirality_split_step_mass_gaps_every_cone_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite zone scans of a supplied two-chirality split-step cell on Z^3 with a same-site and a staggered chirality mass: cone sets, the gap over the zone and the light band; no matter content, one-qubit realization, exact cubic covariance or physical mass values."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/two_chirality_split_step_mass_gaps_every_cone_2026_10_21.py
---

# Two mass terms gap every cone of a split-step cell

Claim type: bounded_theorem.
Primary runner: `scripts/two_chirality_split_step_mass_gaps_every_cone_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, leaves the tick update and the mass of each species open. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither. This note examines a supplied cell with two chirality components at each site.

## The supplied cell

- **The L component** runs the split-step walk U_L(k) = S_z S_y S_x, with S_i = cos k_i - i sigma_i sin k_i.
- **The R component** runs the momentum-reversed walk U_L(-k).
- **Each tick** first applies the chirality mass exp(-i m(x) beta), where beta exchanges L and R and m(x) = m + M (-1)^(x+y+z).

## Cones

Each walk has eight zero-quasi-energy cones on a 40^3 grid. L and R share four momenta, where their chiralities are opposite: k = 0 and the three momenta pi times (1,1,0) and its permutations. The other four L cones, at (pi/2)(1,1,1) and its images, are absent from R.

A same-site mass couples only equal momenta, so with M = 0 those four L cones stay at zero quasi-energy. The staggered term multiplies by (-1)^(x+y+z), which shifts momentum by Q = pi(1,1,1). Q carries the four unshared L cones onto the four unshared R cones.

## Gap and light band

With both terms the minimum |quasi-energy| on a 25^3 zone grid equals the same-site mass. That held for m = .05 with M = .5, and for m = .02 with M = 1. The light band near k = 0 follows sqrt(m^2 + cos(M)^2 k^2) to within 1.5 percent along three directions for |k| up to 2m. The staggered term thus sets the scale of the former doublers and slows the light band uniformly.

## Scope

The two components per site, the substep order, the momentum-reversed R walk and the two mass terms are supplied. The light band has four copies at k = 0 and its three images, one for each sublattice class. No matter content, one-qubit realization, exact cubic covariance or physical mass values are established.
