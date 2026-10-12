# Narrow independent inverse-implementation check

2026-10-12. This is a source and synthetic-control check, not a formal audit,
empirical fit, or disposition of the conditional gravity model. The author
retains the campaign and implementation. No author file, input, worker, or
automation was changed. No actual galaxy operator or empirical inverse fit
was executed by this reviewer.

## Disposition and exact scope

No material sign, unit, or linear-constraint error was found in the sources
below. The physical SI basis argument, fixed-source projection, exact D-family
condition, velocity-error rectangles, LP signs and scaling, external conversion,
solar coefficient scaling, and sampled-search implementation agree with the
frozen protocol. Independent synthetic checks pass.

This does not validate an actual fitted response. The direct and refined field,
new-response boundary, inward-force, and observation-readout obligations remain.
The author's old-response boundary receipt supplies a previously tested grid;
it does not establish the boundary error of every new response. The author has
separately stated that each fitted response will receive its own extended-domain
check. That evidence was pending at this checkpoint.

| Reviewed source | SHA-256 |
| --- | --- |
| FROZEN_DIRECT_INVERSE_PROTOCOL.md | `16ff2920797c5d5fb027a920f623b44983953b022931ef442194f6ac8b2a90ce` |
| direct_galaxy_response_operator.py | `fe1d5256bb1d867602b4c5c6f68a7c683db1f3ea485d9d85c572b3f8ffccfadb` |
| direct_shared_response_fit.py | `0f846de483a77c920761f214f6482fd125ec8206073d8226e71c082e499fc787` |
| direct_response_basis.py | `da0c24cdf104a79abc8bb796056e64d06dfb8c248fe39ca3de7325c629293f4f` |
| direct_qumond_disk.py | `701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00` |

Exact snapshots are preserved beside this report. The runtime snapshot manifest
records original and snapshot paths, hashes, and the observed control receipt.
All five original/snapshot hashes were checked before and after the synthetic
execution. The protocol freeze at 19:37:32 UTC is the author's declared ordering;
this review pins the resulting bytes and does not reconstruct past in-memory
execution. The local commit containing these subjects is `8e1ead28c9`, timestamp
2026-10-12T19:43:21Z. The author control receipt is timestamped 19:43:45Z and uses
the operator, protocol and solver hashes above.

## Independent mathematical checks

### Physical arguments and fixed-source projection

The code's field unit is `(km/s)^2/kpc`. Multiplication by
`ACC = 1e6 / 3.085677581491367e19` converts it to `m/s^2`. Both off-plane and
midplane basis calls use `ACC*hypot(U_R,U_z)`. Thus the fixed knots from
`1e-13` to `1e-8 m/s^2` act on the physical Newtonian-field norm. No redundant
`a0`, velocity unit, or radial-only norm enters those ramp calls.

For an axisymmetric vector mode, write

    A_r = a_l(r) P_l(c),
    A_theta = b_l(r) partial_theta P_l(c),
    H_l = (r^2 a_l)'/r^2 - l(l+1)b_l/r.

Solving the radial Poisson equation directly gives

    Phi_l = -[r^(-l-1) integral_0^r t^(l+2) H_l(t) dt
               + r^l integral_r^infinity t^(1-l) H_l(t) dt]/(2l+1).

Differentiate, then integrate the source terms by parts. The resulting radial
gradient equals `a_l` minus `l(l+1)/(2l+1)` times

    r^(-l-2) integral_0^r t^(l+1) [a_l+(l+1)b_l] dt
      + r^(l-1) integral_r^infinity t^(-l) [a_l-l b_l] dt.

The new operator uses precisely these combinations, angular normalizations,
midplane Legendre factors, and correction sign. Its linear columns retain the
reviewed upper-half-space sheet treatment and fixed source. Multiplying the
same fixed U by each ramp does not refit baryons or make K positive. Column
superposition follows from linearity of the Poisson boundary problem in its
vector input.

The LP baseline is the exact Newtonian midplane field. The implementation's
superposition control instead uses the numerically projected Newtonian field,
as it must for an internal linearity check. Their separately checked finite-grid
difference still has to be included when comparing the final LP force to a
direct projection. The two baselines are not asserted identical.

### Exact differential constraint

Let `d_j=log(A_(j+1)/A_j)` and `S_j=sum_(k>j) w_k`. Inside interval j,

    N = 1 + S_j + w_j log(A_(j+1)/A)/d_j,
    d(A N)/dA = 1 + S_j + w_j[b_j(A)-1/d_j].

For nonnegative `w_j`, the latter decreases across the interval, with upper-edge
infimum `1+S_j-w_j/d_j`. This gives exactly the code's row
`w_j/d_j - sum_(k>j)w_k <= 1`. The tails have positive constant response, and
`A N(A)` is continuous at the knots; slope jumps create no delta in its first
weak derivative. These inequalities therefore impose the stated global
nondecreasing radial differential response. They do not prove a relativistic
completion or positivity of every nonlocal disk radial component.

### Error rectangles and LP

Positive released velocities and scored radii give `A_i=V_i^2/R_i>0` in field
units. The lower velocity is clipped at zero before squaring. Released zero
errors are retained. For `g=g_N+K w`, dividing both rectangle inequalities by
`A_i` gives

    (K/A_i) w - t <= H_i/A_i - g_N/A_i,
    -(K/A_i) w - t <= g_N/A_i - L_i/A_i.

These are the implemented signs. All weights and t are nonnegative, and the
cap row is `sum w<=100`. The first LP minimizes t; the second minimizes total
weight under `t<=t_min+1e-8`. Reported candidates carry an explicit scaled
primal-residual check. The fitting statistic is a descriptive fractional
acceleration allowance, not a joint confidence level or a likelihood.

### External and solar conversion

At each sampled positive E, the two external rows impose
`g_min/E-1 <= sum w_j b_j(E) <= g_max/E-1`; the reported physical value is
`E[1+sum w_j b_j(E)]`. This changes with both E and the fitted response.
The necessary interval `[g_min/101,g_max]` follows from `1<=N<=101`, including
the M family if the physical-to-Newtonian map is not one-to-one.

The solar coefficient is evaluated anew as
`E^(3/2)/sqrt(GM_sun) * F(A_j/E,A_(j+1)/E)`. Its dimensions are `s^-2`.
Nonnegative weights and the positive kernel meet the negative lower solar
edge automatically; the upper inequality is scaled by `5.2e-27 s^-2`.
The spherical Galactic conversion and fixed external direction remain
additional premises, not exact nonspherical Milky Way results.

The scan samples the prescribed 129 logarithmic nodes, picks the three best
initial nodes using `(t_min,total_weight,E)`, and subdivides their adjacent
log intervals four times. It retains infeasible samples and returns the best
sampled member. It makes no continuous-E global-optimality claim.

## Independent executable evidence

`check_inverse_synthetic.py` computes expectations without author projection,
ramp, or solar-integral helpers; author functions are then invoked as subjects.
Synthetic NPZ files exercise the actual row reader through an in-memory path
substitution. No campaign velocity file is opened. The reviewed source bytes
are executed with original path semantics and Python bytecode writing disabled.

- A fresh non-gradient vector `A_r=r exp(-r)P_2(c), A_theta=0` is checked against
  adaptive quadrature of the differentiated source Green solution. Maximum
  absolute error decreases from `1.0944e-6` at 1536 radial nodes to `1.5503e-7`
  at 4096 nodes. Removing the Poisson correction produces absolute error
  `0.20759`. The initial coarse test failure and its exact script are preserved;
  the failed threshold concerned a force close to zero. The final receipt
  states the normalization floor explicitly rather than calling that metric an
  ordinary relative force error.
- Spherical SI ramp controls across four transition intervals agree within
  `3.69e-15` of the Newtonian force scale; synthetic superposition agrees within
  `7.37e-16` on that scale.
- Synthetic row-reader inputs produce `A=(9,2,.25)`, `L=(9,0,.0625)`,
  `H=(9,18,.5625)`, including zero error, a clipped negative lower velocity,
  and an excluded non-scored row.
- Three independently solved LP cases recover primary minima `0,1/3,0`,
  including a negative response column. The secondary weights match the
  analytically expected `1e-8` tolerance adjustments, with zero scaled primal
  violations. D-row slacks agree with independent upper-edge derivatives to
  `1.78e-15`, including just below, at, and above the last-interval bound.
- All 20 solar columns at each of three E values, including both envelope
  endpoints, agree with an independent 65-digit logarithmic quadrature of the
  square-root-difference kernel within `8.70e-16` relative error. The same
  probes check physical external and scaled solar row signs. These are 60
  synthetic coefficients, not fitted solar or galaxy results.
- A mocked analytic search recovers all 219 distinct nodes for three disjoint
  refinement neighborhoods and retains two infeasible samples. A wholly
  infeasible scan returns 129 samples and no candidate. Reference node locations
  agree to `3.45e-15` relative precision.

The combined check took 3.55 seconds with peak resident memory 118,194,176
bytes. CPU thread settings were fixed to one. The author's separate runtime
control receipt also reports passed sphere/Kuzmin controls; its largest Kuzmin
error is `7.7597e-5`, with its declared `0.003` limit. This review did not rerun
the actual-source operator construction or the author's field batch.

## Limits that must survive downstream interpretation

`force_positive` is a diagnostic flag, not an LP inequality. This is consistent
with the frozen relaxed rectangles, whose lower edges can become negative.
The separate synthetic `check_force_flag.py` confirms a legitimate LP optimum
`t=.4` can have a negative radial component: two allowed synthetic boxes and
signed columns yield forces approximately `(2.4,-.4)` and flag false. This is
not evidence of such a failure in an actual galaxy. A false flag must not be
turned into a physical circular-speed candidate or a conditional existence
claim; the direct candidate validation must retain that check.

Only the three declared original objects enter the inverse fit. The six exposed
extension objects are outside that fit, not blind data. Solar and external
measurements are constraints in the combined case, not new predictions.
Columns are not accompanied by certified uniform errors over the weight
simplex. A sampled failure or positive t cannot establish a universal exclusion.

The author's `DIRECT_KINEMATIC_READOUT_FINDING.md` is an additional interpretation
limit: converting the supplied rotation curves directly to `V^2/R` assumes a
circular-speed readout, especially consequential for UGC07577. Its astronomical
source-chain claim was not independently re-audited in this implementation
check. The present LP and synthetic results do not determine pressure support,
repair the observation map, or distinguish it from a gravity-model mismatch.

The final runtime review receipt pins this report, synthetic receipts, source
manifest, author controls, and the readout note. No formal audit lane or verdict
was invoked.
