# Local milestone decision

OPEN — combine the exact theorem, quantitative extension and scoped Lean
evidence in one reviewable main-based milestone.

The complete mathematical sources, controls and raw outputs were read before
this decision. The existing campaign PRs concern supplied stochastic transport
or the excluded walk's scattering and memory dynamics. They do not prove the
cross-species-only collision-invariant classification. The historical C1
proposal explicitly left that step open. This result supplies a common energy
and momentum coefficient from regular AB collisions, with no AA or BB identity.
The proof retains labels and equal velocities, covers the exceptional skew-line
configurations, and states the measure and current conditions separately.

The quantitative extension adds a usable error interface. Merely perturbing
the initial four-cycle would leave unbounded constants near exceptional lines.
The full proof controls both tubes and identifies the additional anchor
conditioning needed for a uniform estimate over arbitrary label sets. It then
tracks the units of wedge errors, intrinsic path lengths and the separate
derivative assumptions for approximate current rigidity. A continuous thin-image
counterexample and an oscillatory-charge example preserve the limits of those
conclusions. These are substantive additions to the exact theorem, so both
are packaged together rather than issued as successive corollary PRs.

The Lean component verifies six universal finite-geometry steps with explicit
scope and preserved failed development history. It does not replace the
analytic proof or formalize the stability inequalities. Distinct source reviews,
complete controls and whole-primary mutations support the milestone's review
value; PASS counts and source-author replay are not independent mathematics.
The OPEN decision does not assign retained status or adopt a physical law.
Actual collision selection, current identification, scale-dependent conditioning
and approximation errors remain application obligations. The next campaign
work attacks those interfaces while this regular PR remains available for review.
