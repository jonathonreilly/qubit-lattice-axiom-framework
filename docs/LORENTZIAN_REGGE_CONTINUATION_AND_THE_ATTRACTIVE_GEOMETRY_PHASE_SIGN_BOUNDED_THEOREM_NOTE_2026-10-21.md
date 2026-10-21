---
claim_id: lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite deterministic diagnostics on the supplied Kuhn cubic and coned D4 Regge carriers, continued from Euclidean to Lorentzian signature: Schlaefli along the continuation, the per-cell match of the Lorentzian Regge second variation to (1/2) int sqrt(-g) R, and the static and wave responses for both signs of the geometry phase; no physical Newton constant, Planck identification, field equation beyond linear order or adoption of a law is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_2026_10_21.py
---

# Lorentzian Regge continuation and the attractive sign of the geometry phase

Claim type: bounded_theorem.
Primary runner: `scripts/lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. A Euclidean Regge action on the supplied carriers matches the Einstein-Hilbert action per cell. This note continues that action to Lorentzian signature and asks which sign of a geometry phase kappa S_L gives an attractive static response. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the carriers nor the sign.

## Continuation

The flat background g = diag(1,1,1,alpha e^{i phi}) is continued from phi = 0 to pi, with alpha = 0.6 and the tick as the fourth index. Along the way sqrt(det) becomes +i|.| on every simplex and the Schlaefli identity holds per simplex, with largest relative residual 3.0e-16 on the Kuhn cubic (15 edge classes, 50 hinge classes) and 3.7e-16 on the coned D4 (72 edge classes, 208 hinge classes). On hinges with a tick component the area is +i|A| and the deficit derivative is that of the real rotation angle, to 5.0e-8 and 5.6e-7. On spacelike hinges the deficit is i s times a rapidity deficit, with one sign s per wedge type. S_L, the continued action divided by i, is real.

## Per-cell match

For random metric perturbations and random timelike and spacelike wave vectors, the second variation of S_L divided by that of (1/2) int sqrt(-g) R is 1.00000 on both carriers, with imaginary parts below 2e-13. Continuing through phi = -pi gives the same Hessian to 2.4e-16. Flipping the sign of the spacelike-hinge part spoils the match, with ratios -1.243 and -3.362. The ratio stays 1.00000 at alpha = 1.7, 0.99 and 0.999, though single hinge coefficients grow toward the null limit alpha = 1, where relay steps are null and both carriers contain degenerate hinges.

## The sign

With the deposit's phase advance E per proper tick and the geometry entering the phase as sigma kappa S_L, sigma = -1 gives on both carriers a static h_00 k^2 equal to +E/kappa to within 3e-5, which is attraction. It also gives PPN gamma = 1 to within 3e-5, so light bends toward the source by 2(1+gamma) G E/b, and a transverse traceless wave action proportional to omega^2/alpha - k^2, positive in its kinetic term and vanishing on the light cone. sigma = +1 reverses all three: h_00 k^2 = -1.00003 and a negative kinetic term. Observed gravity is attractive, so the comparison selects sigma = -1.

On the coned D4 at sigma = -1, a position-space fit of h_00 on a 20^3 torus over 4 <= r <= 8 gives G = 0.03942 against 1/(8 pi) = 0.03979, with relative residual 0.047.

## Scope

Supplied: the carriers, flat lengths, the tick index, alpha = 0.6, the continuation direction, the squared-length metric reading, kappa, the torus, the fit radii and the pseudo-inverse cutoff. The relation G = a^2/(8 pi kappa) is conditional on kappa. No physical Newton constant, Planck identification or adoption of a law is established.
