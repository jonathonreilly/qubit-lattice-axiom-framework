# Finite-stencil tensor response on the trivial cubic scalar-irrep support segment

**Status:** bounded support; candidate bounded theorem pending milestone review
and independent audit. The endpoint secant is a bounded approximation on the
declared grid, not an exact affine support law.
**Date:** 2026-04-14 (original prototype); 2026-07-12 (source-step-free
finite-operator repair).
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/frontier_s3_time_tensor_primitive_prototype.py`](../scripts/frontier_s3_time_tensor_primitive_prototype.py)
(`PASS=11`, `FAIL=0`).
**Runner cache:**
[`logs/runner-cache/frontier_s3_time_tensor_primitive_prototype.txt`](../logs/runner-cache/frontier_s3_time_tensor_primitive_prototype.txt).
**Implementation helpers:**
[`quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py`](../scripts/quark_route2_endpoint_step_free_active_branch_slopes_bounded_2026_06_12.py)
and
[`quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py`](../scripts/quark_route2_t_balance_exact_algebraic_value_bounded_2026_06_12.py).

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "fixed finite-operator computation with explicit conditions, endpoint values, and an eleven-point residual bound"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Bounded theorem domain

Fix the following finite-operator conditions. They define the theorem domain;
they are not supplied by the framework axioms.

- a `15^3` cubic box with zero Dirichlet boundary and `13^3` interior;
- the nearest-neighbor negative Laplacian and seven Green columns on the
  center-plus-six-arms star;
- the `R=4` exterior projector and `(3,3,0)` anisotropic orbit functional;
- `scipy.ndimage.map_coordinates(order=3, mode="nearest", prefilter=True)`;
- the static conformal metric
  `g_00=-[(1-phi)/(1+phi)]^2`, `g_ii=(1+phi)^4`;
- centered coordinate step `h=1/25`;
- probes `(0,4.25,0,0)`,
  `(0.3,4.25/sqrt(2),4.25/sqrt(2),0)`, and
  `(0.6,4.25/sqrt(3),4.25/sqrt(3),4.25/sqrt(3))`;
- the maximum absolute spatial trace-free Einstein component as readout;
- NumPy `2.4.1`, SciPy `1.17.0`, and mpmath `1.3.0` for the frozen replay.

The high-precision interpolation emulation uses edge padding `PAD=12`, a
rational tridiagonal spline-coefficient solve, and cubic B-spline weights. The
runner pins SHA-256 fingerprints of both implementation helpers.

The trivial cubic scalar irrep is denoted below by the established runner token
`A1`. `E_x` and `T1x` are the tangent directions fixed by the proper cubic
quarter-turn about the `+x` probe axis. “Route 2” is only the legacy program
label for this construction.

On the unit-charge scalar segment

`q_x = x e0 + (1-x) s_unit`, `x = 0,1/10,...,1`,

the fixed operator satisfies these bounded statements:

1. `delta_A1(q_x)=x/6` by exact finite-lattice algebra.
2. The negative `probe0:xx` entry is the unique maximum on the eleven-point
   grid, with minimum gap `1.208546819918e-05`.
3. Stabilizer-dark tangent responses `E_perp,T1y,T1z` are below `8.7e-17` in
   the replay, while the `E_x,T1x` responses are nonzero.
4. The common shell normalization and endpoint coefficients are computed
   without a source-amplitude finite difference.
5. The endpoint secant residual is below `5e-9` in E and `1.1e-8` in T on the
   grid.
6. Two numerical implementations give positive midpoint defects above `4e-9`
   and `1e-8`. This is a bounded numerical non-affinity witness, not an
   interval-certified exact nonzero theorem.

No fitted source family, observation, literature value, reported endpoint
target, or imported decimal normalization is load-bearing.

## Exact finite-operator reduction

Let

`s_unit=(1/6) sum_arms e_arm`, `d=e0-s_unit`.

The center row of the nearest-neighbor negative Laplacian gives

`d = H[(1/6) delta_center]`.

Therefore

`Gd=(1/6) delta_center`,

`q_delta=s_unit+6 delta d`,

`phi_delta=phi_shell+delta delta_center`, `0<=delta<=1/6`.

This derives `delta_A1(q_delta)=delta`. It also shows that the two raw lattice
fields differ only at the center.

The `R=4` exterior projector kills that center spike. Its total shell charge
and anisotropic orbit functional are consequently constant on the scalar
segment. The finite sine-sum replay computes

`A_aniso = 0.0814354029959012027063775747854140534`

at shell, midpoint, and center, with 90-digit anchor drift below `2e-91`; the
total shell charge equals `Q=1` with drift below `3e-89`. These extra digits
identify the high-precision replay, not physical precision.

## Analytic source derivative

For a support tangent `v`, set `phi_v=Gv`. At every coordinate-stencil sample,

`D_v g_00 = 4(1-phi)/(1+phi)^3 phi_v`,

`D_v g_ii = 4(1+phi)^3 phi_v`.

The runner applies

`D_v(g^-1)=-g^-1(D_v g)g^-1`

and the product rule through the centered Christoffel, Ricci, Einstein, and
trace-free constructions. This removes the former `epsilon=0.005`
source-amplitude difference from the load-bearing calculation.

Let `F(q)` be the active `probe0:xx` entry. It is negative at every declared
grid point, so on the checked branch

`beta_v(q)=D_v|F(q)|=-D_vF(q)`.

The reported finite response is

`Theta_R^(0)(q)=(beta_Ex(q)/A_aniso,beta_T1x(q)/A_aniso)`.

Naming the pair is secondary. The load-bearing result is its explicit
derivative, normalization, active-branch, endpoint, and residual computation.

## Stabilizer-selected tangent channels

The proper cubic quarter-turn about the `+x` probe axis fixes `E_x` and `T1x`.
It sends `E_perp` to its negative and rotates the `T1y,T1z` plane without a
fixed vector. Because the scalar background and active `xx` entry are fixed by
this stabilizer, their linear response annihilates the complementary tangent
space. The runner also finds

`max(|gamma_Eperp|,|gamma_T1y|,|gamma_T1z|)<8.7e-17`

at shell, midpoint, and center. This selects the two tangent channels for the
fixed readout; it does not establish a unique physical GR bright pair.

## Endpoint values and affine secant

The source-step-free sparse replay gives

`Theta_R^(0)(e0)=(-3.772329630900e-04,+3.359952161280e-04)`,

`Theta_R^(0)(s_unit)=(-2.010571753887e-04,+4.031967438104e-04)`,

`Theta_R^(0)(q_mid)=(-2.891402561310e-04,+3.696066929060e-04)`.

The 60- and 90-digit helper evaluations differ below `1.5e-62`; the
sparse-double analytic derivative differs below `2.6e-15`. A separate central
source-amplitude finite difference reproduces the values within `1.5e-10`.

The endpoint secant is

`gamma_E^sec(delta)=-2.010571753887e-04-1.057054726208e-03 delta`,

`gamma_T^sec(delta)=+4.031967438104e-04-4.032091660945e-04 delta`.

Its eleven-point maximum residual is `4.813108758989e-09` in E and
`1.071293969295e-08` in T. At `delta_A1=1/12`,

`R_E=gamma_E(mid)-[gamma_E(shell)+gamma_E(center)]/2`

`=+4.813108344220e-09`,

`R_T=gamma_T(mid)-[gamma_T(shell)+gamma_T(center)]/2`

`=+1.071293674114e-08`.

These values rule out affinity at the stated numerical tolerances. Exact
algebraic non-affinity remains open without a validated error enclosure.

## Interpolation boundary and physical firewall

The identity `G(e0-s_unit)=delta_center/6` makes the exterior raw lattice
fields identical. On the `probe0` curvature-stencil samples, local linear
interpolation sees their difference only at `2.1e-18`, whereas the frozen cubic
prefilter replay produces a tail as large as `4.322e-04`.

Thus the observed scalar-segment dependence at the shell-adjacent readout is
interpolation-contract dependent in this replay. The cubic contract supports
the bounded finite computation, but this note does not derive it as a physical
support-to-shell map.

The note does not claim an interpolation-independent or continuum endpoint,
an exact affine law, a unique physical tensor primitive, support-to-slice
coupling, or GR closure.

For compatibility with downstream boundary checks, the broader physical gaps
are also recorded in the older vocabulary:

- Outside the fixed algorithm, This note **does not**
derive the named inputs themselves on an interpolation-independent surface.
- Open physical phrases: exact reduced anisotropic shell amplitude; bridge theorem identifying the support-block pair.
- This note still does **not** close an exact endpoint coefficient theorem on
  an interpolation-independent or continuum surface.

## Historical repair boundary

The historical review objected that the prototype was a renaming with no
inspectable endpoint, normalization, or affine-residual computation. The new
runner computes those quantities, makes the naming secondary, and exposes the
interpolation condition. This closes the quoted artifact blocker for review of
the bounded fixed-operator claim. Independent audit and dependency closure
determine any retained-grade effective status.
