# Latest clock/source PR: read boundary and two scope observations

2026-09-21. Read-only catch-up, not an independent review of the complete PR.
PR 8568 at fb5252af7da4c9deb561c18af0495b27c7e6f7a3 was inspected after the
final repository fetch. The complete 181-line theorem note was read at
SHA-256 3312767452cc25192d50c075d439babc4bc4e353abc10e72932b9d9cab4dbd5f.
Its runner, refuter and broader evidence were not executed or fully reviewed.
No change, comment or verdict was sent to that PR.

The note supplies a positive site clock, a differentiable homogeneous
nearest-neighbor rule and an added scale-covariance premise. Its first-order
argument is sound at that scope: proper cubic transitivity makes the six
uniform-point derivatives equal; homogeneity and normalization make each
1/6. A nearest-neighbor Laplacian follows in the linearized log-clock law.
The absence of a time metric in the axioms is motivation for the supplied
premise, not its derivation. No result from this PR is used as a premise in
the mobile-record campaign.

Two distinctions should be resolved before building a dynamical source claim
on the narrative. These observations do not replace a full source/code review.

1. **Exact superposition needs the linear completion.** T2 explicitly allows
   nonlinear scale-covariant means. For the arithmetic mean, neighbor rates
   exp(a), exp(-a),1,1,1,1 and no local multiplier give

       u_x - average(u_neighbors) = log[(cosh(a)+2)/3],

   which is nonzero for a!=0. Thus the exact log-clock Laplace law and exact
   arbitrary-strength superposition are not consequences of the entire C1-C3
   class. They hold for an expressly chosen linear log-clock completion
   (for example the geometric mean), or to the declared perturbative order.
   The frontmatter does restrict T3/T4 to the linear law, but the result-up-front
   and T4's transition from first order to exact arbitrary-density additivity
   need that qualification kept visible. On a torus a source of nonzero sum
   has no solution; projecting it to zero sum is a modification of the source
   prescription, not a solution of the unchanged non-neutral equation.

2. **Residence bias differs from conditional velocity drift.** The displayed
   symmetric departure-site rates w_x/6 give the stated invariant law
   proportional to 1/w_x on a finite connected torus. However the instantaneous
   conditional mean lifted displacement is exactly

       sum_i [(w_x/6)e_i+(w_x/6)(-e_i)] = 0.

   An unwrapped walk is a martingale for bounded positive rates. In a continuum
   description the density law can contain a gradient-dependent probability
   flux through Delta(w rho); that does not make the particle's conditional
   mean velocity proportional to grad(w). The note's sentence that its mean
   velocity follows the gradient needs this distinction. Accumulation in
   slow-clock regions is consistent with zero conditional drift and is not
   an inertial force.

The short author check `latest_clock_scope_check.py` verifies the local
nonlinear residual and the separate stationary-law/zero-drift identities.
It does not confer independent-review status on these catch-up observations.
