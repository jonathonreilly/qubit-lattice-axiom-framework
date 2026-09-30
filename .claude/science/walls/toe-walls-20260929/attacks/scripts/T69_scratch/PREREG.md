# T69 pre-registration (written before any number below was computed)

Wall: T69 = L14-W10 (what sources gravity, with what absolute strength) + L02-W7
(the log-det / readout bridge lost its footing when Record additivity went).

Best route under test (R2, "the readout is the action"): use the filled sea's
ground-state energy E_-[u] (the zero-temperature limit of the log-det readout) as the
generating functional. Then the source is dE_-/du (b55 T1, exact) and the field's own
stiffness is the sea's gradient response. If that response is a positive, isotropic,
walk-independent number, the absolute strength (K) is derived for the lapse sector.
If it is zero, negative, or depends on the supplied walk's UV shape, K is supplied.

## Model (all from landed notes, nothing new)
- 3D walker H = sum_a sigma_a sin(k_a)  (b54 identity frame, 8 species), coupling
  H_w = phi H phi, phi = exp(u/2), u = eps cos(q.x) (b53-b55, b76 defs).
- Sea = every negative level filled (b76 E_-).
- a2(q) = coefficient of eps^2 in E_-/site.  c0 = E_-/site at u=0.
- Clock stiffness kappa := 4 (a2(q) - a2(0)) / |q|^2_lat  as q -> 0
  (b76 / b130 convention: Pi(q) = c0/4 + (kappa/4)|q|^2 + ...).

## Sanity gates (if any fails, no physics reading is taken)
- G0: the k-space (BZ-sum) formula for a2(q) equals exact diagonalisation on a
  3D antiperiodic torus (L=6, q = 2pi/6 x-hat and 2pi/3 x-hat) to relative 1e-7 (the ED noise floor with eps = 0.004; threshold fixed before the run).
- G1: the same formula in 1D (H = sigma_3 sin k) gives c0 = -2/pi and kappa = 1/(3 pi)
  (the free-sea values quoted in b130) to 1e-4 as q -> 0.

## Main readings (3D)
- K1 (declared input check): kappa_3D within 5% of the declared 0.095 (b76 T4, rounded).
  Otherwise the declared input is off and is reported as such.
- K2 (sign): kappa > 0 needed for an attractive, stable induced stiffness.
  kappa <= 0 -> the sea cannot supply the strength (and the sign problem T71 bites).
- K3 (isotropy, bug detector): kappa along x-hat and along (1,1,1) agree to 2%
  (a rank-2 cubic tensor is isotropic at O(q^2)).
- K4 (universality): repeat with the reach-two family
  s(k) = (1-mu) sin k + mu sin(2k)/2  (same IR theory, speed 1, other UV shape),
  mu in {0, 0.25, 0.4}.
    * spread of kappa(mu) < 10%  -> kappa looks walk-independent: the readout route
      is a live way to DERIVE the lapse-sector strength (outcome would lean PASSED
      for the strength half).
    * spread > 30%              -> kappa is a property of the supplied walk's UV shape:
      the strength is supplied, not derived (outcome stays PRICED at the walk/K).
    * 10-30%                    -> ambiguous, reported as such.
- K5 (continuum-covariance expectation, reading only): for a static lapse a
  covariantly regulated Dirac sea has no O(q^2) term (sqrt(g) R = -2 lap N is a total
  derivative). A nonzero lattice kappa is then a non-covariant cutoff-scale number,
  not Einstein-Hilbert's 1/(16 pi G).

## What each outcome would move
- K2 pass, K4 universal: strength half of T69 (and part of T70) has an in-model
  computed value; wall moves.
- K2 pass, K4 walk-dependent: strength is a property of the supplied walk; T69 priced.
- K2 fail: sea cannot supply stiffness; T69/T71 priced at the supplied bare term.
