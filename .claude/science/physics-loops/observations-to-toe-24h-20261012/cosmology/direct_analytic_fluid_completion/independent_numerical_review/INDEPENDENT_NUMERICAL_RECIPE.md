# Independent numerical recipe

This stage checks the frozen first implementation of the already reviewed
handwritten three-field candidate. The parent source is not imported as an
independent oracle. Its stored outputs are the objects compared; modified
source copies are executed only for negative sensitivity tests.

## Frozen input and complete row coverage

Before numerical checks, the reviewer copied all eight present top-level
source/context files and twelve first-execution evidence files. The twenty
paths and exact bytes are recorded in `INPUT_FREEZE_v1.json`. The seven inputs
declared by the parent freeze have matching hashes in that freeze, the final
result, the parent source snapshots, the current source and the independent
snapshots. The upstream radiation result used for the photon normalization is
separately frozen and hash-checked. Its central thermal calibration value is
used only to check the declared import, not to create a new observational test.

The full parent runner, fixtures, calibration roles, freeze and execution
record were read. Every result row is consumed by independent code:

- 72 off-trajectory fixtures: three a values, four nu values, six states;
- 25 free-mode rows: five squared masses and five times;
- 12 tracking families, each with both refinements and all twelve sites;
- 48 disturbed histories, each with both author formulations at all 61 sites;
- all 1492 original check records, including their numeric arrays and recorded
  tolerance arithmetic.

The original proof and its two narrow corrections remain bound to the exact
previous review identities. That proof is reused as proof only; it does not
substitute for this implementation and numerical comparison.

## High-precision canonical force reconstruction

Let pi_i=K_ii v_i denote canonical momentum per volume, excluding the cosmic
volume factor. The finite-dimensional energy is

  E(q,pi,sigma,r)=sum_i pi_i^2/(2K_ii(q))+V(q)+sigma+r,
  H=sqrt(2E/3).

At fixed momenta and fluid densities, differentiate E with respect to the
three coordinates. The momentum equation and field velocity are

  dot pi_i=-3H pi_i-partial_i E-alpha_i sigma,
  dot q_i=pi_i/K_ii.

The potential and kinetic contributions to partial_i E are computed by
70-digit `mpmath.diff`; no explicit connection or parent force helper is used.
Differentiating K separately gives

  dot v_i=[dot pi_i-v_i sum_j(partial_j K_ii)v_j]/K_ii.

The independent N acceleration follows from the proper-time transformation

  p_i'=dot v_i/H^2-v_i dot H/H^3,
  dot H=-sum_i K_ii v_i^2-sigma-4r/3.

These values are compared to both recorded implementations of all 72 force
fixtures. The same calculation independently supplies H, H_J, K, V, the
potential gradient, metric derivatives, full N state and conservation rates.
The energy derivative is evaluated as

  dot E=(partial_q E).v+v.dot pi+dot sigma+dot r.

Its residual against -3H(T+sigma+4r/3) is checked at high precision before
rounding results to binary64 for comparison. The independent normalized force
discrepancy max|difference|/max(1,|reference|) is 6.67e-16 or smaller.

## Independent free-mode calculation

For q''+3q'+m^2 q=0 in dimensionless H_v time, write q(t)=sum c_n t^n.
Starting from c_0=0.2 and c_1=-0.1, use

  c_(n+2)=-[3(n+1)c_(n+1)+m^2 c_n]/[(n+2)(n+1)].

The reviewer sums 402 coefficients at 80 decimal digits. This route uses
neither the parent's hyperbolic/trigonometric formulas nor its matrix
exponential. It covers nu=1/4,1,9/4,4 and the y squared mass 2, including the
critical repeated root. The last retained term has magnitude at most
1.21e-254 on the frozen time sites; the largest difference from the recorded
mode is 1.39e-16. These are free linear modes, not a replacement for the
nonlinear or matter-forced system.

## Independent histories: conserved fluid numbers

The alternative nonlinear integrator evolves canonical momenta in Einstein N.
Dust number conservation and radiation conservation eliminate their two
differential equations analytically:

  sigma(N,u)=sigma_0 exp[-3(N-N_0)+sqrt(a)(u-u_0)],
  r(N)=r_0 exp[-4(N-N_0)].

At fixed N, including this sigma in E makes its coordinate derivative supply
the scalar matter force automatically. The six field equations are

  q'=K^{-1}pi/H,
  pi'=-3pi-(partial_q E)_pi,N/H.

There is no Christoffel evaluation and no integrated density variable. H comes
from the energy in momentum variables, with no division by 3-Kp^2. This is
a different dynamical representation from both the parent's N acceleration
system and its proper-time momentum system. The independent integration uses
Radau, whereas the parent uses DOP853 and RK45. Solver settings and comparison
tolerances were saved in `NUMERICAL_REVIEW_PLAN_v1.json` before execution.

### Long tracking interval

The interval starts at N=-ln(1+10^6) and ends at N=6. To keep the large early
fields and momenta numerically conditioned, use positive reference scales

  e_x=x0 exp(-3N/2), e_y=y0 exp(-2N),
  Dbar=1+c(e_x^2+e_y^2), Hbar=H_v sqrt(Dbar), c=2(1+a)/3.

The evolved coordinates are Q=(u,x/e_x,y/e_y). Momentums are scaled by

  L=(Hbar, A_x Hbar e_x/Dbar, A_y Hbar e_y/Dbar),
  P=pi/L, A_x=4a/9, A_y=a/3.

The time-dependent coordinate transformation is invertible for every finite
site. Its derivative uses

  dln Dbar/dN=-c(3e_x^2+4e_y^2)/Dbar,
  dln L/dN=(dln Dbar/2,-dln Dbar/2-3/2,-dln Dbar/2-2).

The actual D, kinetic energy, potential and H are evaluated from all six
evolving variables. They are not replaced by reference values. In particular,
the complete combined u force is evaluated in the stable but algebraically
general form

  H_v^2 u(4x^2+nu)
  +sqrt(a)H_v^2 e_x^2[expm1(sqrt(a)u)-(Q_x-1)(Q_x+1)].

Expanding the bracket gives sqrt(a)(sigma-H_v^2 x^2), so this expression
does not set u=0 or project x onto its target. Nonzero u, arbitrary Q_x and
independent momenta retain all their dynamics. The exact trajectory has
constant scaled coordinates and correspondingly very small roundoff error
in this representation; the separate off-trajectory force and disturbed-history
checks are essential for sensitivity beyond that special orbit.

Radau uses rtol=3e-11, atol=3e-13 and max_step=0.04. All twelve independent
tracking solutions are compared at all twelve sites against the exact target
and both stored author refinements, using the author's already frozen
atol=2e-8 and rtol=2e-7. No tolerance was relaxed after execution. The
maximum state discrepancy against either author refinement is 3.30e-10,
or 0.001441 of the allowed tolerance.

### Disturbed histories

For each of the 48 disturbed cases, introduce vacuum-normalized coordinates

  X=(u,w_x x,w_y y), w_x=2sqrt(a)/3, w_y=sqrt(a/3),
  P=(pi_u,pi_x/w_x,pi_y/w_y).

Then

  T=P_u^2+D(P_x^2+P_y^2),
  D=1+[3(1+a)/(2a)]X_x^2+[2(1+a)/a]X_y^2.

The momentum force is obtained from this Hamiltonian, including the coordinate
dependence of the analytically conserved dust density. A seventh variable
integrates dt/dN=1/H, providing an independent proper-time quadrature. Radau
uses rtol=3e-11, atol=3e-14 and max_step=0.04 on 0<=N<=12.

At all 61 sites of every case, the independent fields, N velocities and
densities are compared against both parent formulations. The proper times and
energies are also compared. The parent tolerances remain unchanged. The
largest state differences are 1.08e-12 against the parent N formulation and
6.35e-12 against its proper-time formulation; the largest proper-time
difference is 2.10e-12. The independent energy decreases within precision and
stays above the vacuum floor. Finite-interval agreement is not a numerical
proof of the separate infinite-time attractor theorem.

## Actual source-copy omission tests

Four copies of the frozen parent source each receive one narrow deliberate
change. Their full sources, exact diffs, fixtures, results and exit statuses
are preserved under `negative_mutations/`. Only the parent's 792
off-trajectory controls are executed for each mutant; the author code is used
as a subject for sensitivity testing, not as independent positive evidence.

| Omission | Failed controls | Affected family |
| --- | ---: | --- |
| Numerical connection acceleration | 60 | Full off-trajectory KG |
| Dust mass exchange | 48 | Full off-trajectory conservation |
| Scalar matter force | 48 | Full off-trajectory KG |
| u(4x^2+nu) restoring force | 60 | Full off-trajectory KG |

Every mutant exits 1 with actual numeric assertion failures and no exception
substitution. The last omission is deliberately invisible on the exact u=0
trajectory, but is exposed by all 60 nonvacuum off-trajectory fixtures. Zero
or zero-dust fixtures appropriately do not detect terms that vanish there.
This demonstrates sensitivity to the requested omissions in the frozen
implementation; it does not claim exhaustive mutation coverage.

## Calibration and scope

The fixture Omega_gamma=5.046740289227271e-5 is byte-for-byte the exposed
central thermal import from the pinned radiation result. H0=70 km/s/Mpc,
m=0.3, the photon temperature and the G_N=(1+a)G_* normalization bridge are
supplied assumptions or calibration inputs. In H0=1 numerical units,

  H_v^2=1-m-Omega_gamma,
  sigma_0=3m/[2(1+a)], r_0=3Omega_gamma/[2(1+a)].

The declared bridge makes these expansion fractions consistent with that
import convention. This check does not establish local measurement viability
of the new action, neutrino physics, a cosmological-constant mechanism,
independent observational fit, or finite-history selection.
