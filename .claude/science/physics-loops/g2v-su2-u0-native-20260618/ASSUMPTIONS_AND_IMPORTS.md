# Assumptions And Imports

## Allowed Inputs

- Native SU(2) class-angle parametrization with Haar density
  `sin(theta)^2 dtheta`.
- Wilson one-plaquette weight `exp(beta cos(theta))`.
- Parent anchor-supplied `beta_W = 16`.
- Standard modified Bessel function identity used as a cross-check
  against direct quadrature.

## Retired Import

- The parent row no longer needs a row-local literature numerical
  interval for `u0(SU2) in [0.96, 0.98]`.

## Still Open

- Full thermodynamic SU(2) gauge-field continuum/non-perturbative
  matching is not derived here.
- Effective retained status is not set by this branch; independent audit
  remains required.
