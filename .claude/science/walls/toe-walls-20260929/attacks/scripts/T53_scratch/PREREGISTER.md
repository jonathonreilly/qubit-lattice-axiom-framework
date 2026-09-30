# T53 pre-registration (written before any T53 script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as supervisor; same-family checks).
Chart, constants, PERM=(2,1,0) copied from repo
`scripts/frontier_pmns_theta23_upper_octant_chamber_closure_prediction.py:104-158`.
Comparators (NuFIT-6.1) are ONLY the repo-quoted numbers in
`scripts/audit_companion_pmns_dcp_nufit6_comparator_refresh_exact.py`
(s12^2 in [0.2893,0.3295], s13^2 in [0.02070,0.02420], s23^2 best 0.470, 3sigma [0.432,0.587]/[0.435,0.584],
dCP best 207/212, 3sigma [114,405]/[125,365]). No other data used.

## Claim under test
L10-W6 says the forecast rests on ONE bit (gamma -> -gamma). Hypothesis H2: it rests on TWO
independent discrete labels: (a) sign of gamma (complex conjugation of H) and (b) the row pairing
sigma_hier (mu<->tau swap: (2,1,0) vs (2,0,1)). The "upper octant" is the (b) label, not a chamber
property; the DM lane's "upper-octant selector" (docs/DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md)
applies a threshold computed with PERM=(2,1,0) hard-coded to the (2,0,1) labelling (circular).

## Test A: four sheets S(gamma=+-0.5, sigma in {(2,1,0),(2,0,1)})
Algebraic predictions (must hold to 1e-9 at every chart point tested):
 A1 s12^2, s13^2 identical on all four sheets at a fixed (m,delta,q).
 A2 s23^2(201) = 1 - s23^2(210) exactly.
 A3 sin(dCP) flips under gamma flip and flips under the sigma swap; unchanged under both.
 A4 cos(dCP) unchanged under gamma flip.
Unknown a priori (computed): cos(dCP) under the sigma swap, hence dCP on each sheet.
PASS (H2 supported): A1-A3 hold AND the four sheets realize all four (sign J, octant) combinations.
FAIL (H2 refuted; wall stands as one bit): any of A1-A3 fails at 1e-9, or fewer than 4 combos.
Data reading: for each sheet, does the Basin-1 chamber-boundary preimage of the NuFIT-6.1 rectangle land
inside the repo-quoted 3sigma ranges of BOTH dCP and s23^2? Is there a sheet with sin dCP<0 AND s23^2<0.5?

## Test B: circularity of the "upper-octant selector"
Fit (m,delta,q) to targets under each labelling with the repo's own solver approach.
 B1 sigma=(2,0,1) with target s23^2 = 0.455 (mirror of 0.545) has a chamber-interior root
    (q+delta > sqrt(8/3)), and it is the SAME (m,delta,q) as sigma=(2,1,0) with target 0.545.
 B2 sigma=(2,0,1) with target s23^2 = 0.470 (NuFIT-6.1 best fit) has NO chamber-interior root
    at (0.307,0.0218) (mirror of 0.530 < 0.541).
 B3 chamber-threshold surface for the (2,0,1) labelling is 1 - t(s12^2,s13^2); the excluded band
    around maximal mixing is (1-t, t) for both labellings.
PASS (circularity shown): B1 and B2 hold. FAIL: B1 has no interior root (then (2,0,1) truly excluded).

## Test C: sheet-invariant content over the NuFIT-6.1 rectangle (float, NOT the interval certificate)
On the chamber boundary q = sqrt(8/3)-delta, Basin 1: over a 9x9 grid of the rectangle compute
 range of |sin dCP|, of dCP (sheet A), threshold t and the gap (1-t, t).
Reading: label-free forecast = {|sin dCP| in [lo,hi], |s23^2-1/2| >= g}. Compare with repo-quoted NuFIT-6.1 3sigma.
Refutation of the label-free forecast (pre-registered): |sin dCP|<0.95 inside 3sigma, or s23^2 inside (1-t,t) at >3sigma.
Also record whether the float band over the 6.1 rectangle stays inside [251.86,270.00] (the 06-08 note's "expected" stability).
