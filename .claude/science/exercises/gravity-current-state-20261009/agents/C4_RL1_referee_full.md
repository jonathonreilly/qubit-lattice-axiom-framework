# C4 lane RL, probe RL1: independent referee

## VERDICT: NOT CONFIRMED

The worker's bounded `FAIL` is not established under the fixed readings.  The
mean failures for Johnston massless/mass-perturbative sums, admissible
volume/count-weighted one-hop kernels, the original BD inverse, and a universal
scalar density repair of a thin Ricci lens are sound after the corrections
below.  The stable generalized-operator class remains inconclusive: the
resolved scan has three distinct numerical candidates (six antipodally
duplicated rows), while the step from its positive shared-path ladder to the
full small-epsilon variance is neither a bound nor a theorem.  The physical
claim extrapolates from epsilon=1 to roughly 7e-64 and translates point-to-point
kernel noise rather than the fixed-source Fano observable of E1-prime-b.  This
violates the no-long-extrapolation rule and leaves the fixed `FAIL` clause
unsatisfied (`TESTS.md:5-9,1576-1583`; `RL1_report.md:164-175,194-212`).  The
correct lane reading is **INCONCLUSIVE, leaning FAIL**.

## Findings

### 1. (a) Johnston multi-hop cone coefficient: confirmed with one algebraic correction

At `b=0`, Johnston's four-dimensional expression is exactly `aL`, so the
refereed G-L result applies (`RL1_report.md:63-65`).  The finite-density Mecke
factorization is also correct: on a fixed chain, all consecutive open order
intervals are pairwise disjoint, inserted chain points lie on interval
boundaries rather than inside another hop, and Slivnyak leaves independent
Poisson restrictions.  Hence the expected `k`-hop kernel is the convolution
power stated at `RL1_report.md:67-71`.

Two normalized four-dimensional direct kernels convolve to a step, not another
delta: in flat space

`G0*G0 = theta(t-r)/(8*pi)`.

The independent normalization check is at `RL1_referee_checks.py:57-60`.
Smooth curved cone amplitudes change the finite jump but not its distributional
order.  This does not conflict with continuum Hadamard transport: changing a
wave operator's principal part introduces derivative insertions that can act
on cone distributions; Johnston's scalar hop convolution has no such
insertions.  Thus longer fixed-coupling hops alter the tail and not the direct
coefficient.

The multiplier in `RL1_report.md:77` is misstated.  After writing the normalized
one-hop mean as `G_rho = a E[L]`, the `k`-hop coefficient is
`(b rho)^(k-1)=(-m^2)^(k-1)`, not `(ab rho)^(k-1)`.  The correction leaves the
massless result and the no-new-delta conclusion unchanged.  It does not cover
nonperturbative density-dependent resummations, which correctly belong to
class (c) (`RL1_report.md:79-81`).

### 2. (b) Weighted one-hop links: confirmed with scope correction

For a cone kernel `a_w F(rho V)` with an integrable, nonzero flat cone moment,
the substitution `s' = sqrt(nu) s` gives exactly the factor `nu^(-1/2)` at
needle order (`RL1_report.md:48-57`).  Division by the GR direct coefficient
therefore gives `(nu Delta)^(-1/2)`.  The phrase "any function of the interval
count" must be restricted to kernels possessing that nonzero normalizable
direct moment; zero-moment combinations such as a local BD kernel are not
one-hop direct kernels of this class.

I reran the deterministic conformal calculation.  All five displayed weights
converge to 0.4857/0.4858 for the central lens and 0.5426 for the quarter lens,
as recorded at `RL1_G_conformal_lens_readouts.out:3-18`.  The code normalizes by
the corresponding flat result, so the comparison does not hide a shared
normalization (`RL1_G_conformal_lens_readouts.py:40-59`).

### 3. (c) Mean inverse identity and the original BD mode: identity and mode confirmed; curved-locality claim narrowed

The surprising identity is exact in the appropriate Palm-kernel sense, not as
an unrestricted identity for arbitrary fixed-dimensional random matrices.  For
strictly retarded `N` with deterministic nonzero diagonal, the inverse is a
finite Neumann series in each finite realization.  Mecke turns each ordered
chain into `rho^(k-1)` times a continuum chain integral; disjoint consecutive
intervals then factor their count weights.  Term by term this is precisely the
Neumann series of the mean Palm integral operator.  Bounded regions and the
finite-layer coefficients give the needed absolute integrability.  This
justifies `RL1_report.md:85-95` under its stated hypotheses.

The claim that curved far-cone terms vanish is not proved in general by the
moment rescaling alone.  What is established here is the leading regular-tube
needle cancellation plus a particular conformal-lens quadrature
(`RL1_report.md:97-106`; `RL1_G_conformal_lens_readouts.out:9-20`).  Indeed the
report correctly admits that no curved inverse was solved and that the stable
inverse's `sqrt(Delta)` mean is only suggested (`RL1_report.md:104-106`).

The original 4D BD instability is solid.  An independent adaptive integral,
not the worker's Gauss rule, gives

`z = 0.3755983314 +/- 5.0522386540 i`,

with residual below 2e-16; in the squared variable this is
`Z=z^2=-25.38404131 +/- 3.79522482 i`
(`RL1_referee_checks.py:14-33`).  This reproduces `RL1_report.md:110-124` and is
consistent with Aslanbeigi-Saravani-Sorkin's finding of precisely two unstable
zeros for the minimal continuum-averaged 4D operator.  Their paper described
the result as strong numerical evidence rather than an analytic theorem.  The
Poisson-thinning rescaling of the mean is exact, so the smeared BD mean remains
unstable at rate `0.3756/ell_k`.

### 4. (c-prime) Stability scan, noise law, and physical bound: not sufficient for FAIL

The F4b winding count is reproducible for the candidate rows in both stated
boxes, so it is fair to call them stable *to the tested resolution*.  It is not
a global certificate: `Re z < 0.003` is untested and the large-|z| exclusion is
only an unquantified asymptotic argument (`RL1_report.md:130-147`;
`RL1_F4b_rescan_resolved.py:1-6,18-22`).

The selector also tests `sum(ns) == 0` instead of requiring each box count to
vanish (`RL1_F4b_rescan_resolved.py:37-41`).  That could admit cancellation of
numerically spurious positive and negative windings.  It does not change the
six saved rows in this run, which the output places in the `(0,0)` bin, but the
negative histogram entries at `RL1_F4b_rescan_resolved.out:3` show why the
implementation is not a general stability certificate.

There are three distinct candidate operators, not six.  The L=6 grid samples
the full coefficient-nullspace sphere, and normalization by `f0` identifies
antipodes (`RL1_F4b_rescan_resolved.py:30-36`).  The saved rows pair as
`(0,3)`, `(1,4)`, `(2,5)` to relative differences of only
`4.4e-8`--`1.2e-7` (`RL1_referee_checks.py:36-44`).  Thus "six of 7320" counts
duplicated parameter points; mathematically it is three candidates among about
3541 projective grid directions.

The diagonal shared-path ladder and its small-epsilon root are correctly
computed (`RL1_F5_stable_members.py:23-42`), but the inference at
`RL1_report.md:151` is invalid: a positive diagonal subseries of `E[H^2]` is
not a lower bound on either `E[H^2]` or `Var(H)` when the off-diagonal path-pair
terms have signs and the mean square is subtracted.  The epsilon=1 Monte Carlo
shows only that cancellation is modest over `T=3..9`; the endpoint sample falls
to 25 realizations (`RL1_C_stable6b_4d.out:1-7`).  The report itself labels the
ladder-to-variance step at small epsilon merely "SUGGESTED"
(`RL1_report.md:164-168`).

There is also an observable mismatch.  The simulated source has center and
width proportional to `T`, including width `0.07T`
(`RL1_C_bd_inverse_mc.py:58-68`), whereas E1-prime-b controls a fixed regular
source with `D >> s >> ell` (`E1p_b_referee.md:140-154`).  The physical
translation uses the point-to-point `H` ladder, not a uniform bound for that
source-driven Fano factor (`RL1_I_translate.py:1-10`).

Conditional on the unproved identification, the arithmetic is correct:

`lambda_sd = (2/2.8446) ell_k^3/ell_P^2 = 0.7031 ell_k^3/ell_P^2`,

giving `2.691e12 m` at `ell_k=1e-19 m` and
`ell_k >= 2.255e-15 m` for one standard-deviation e-fold over 1 Gpc
(`RL1_referee_checks.py:47-54`).  Correct arithmetic cannot turn the missing
variance theorem and roughly 63-decade epsilon extrapolation into a FAIL; the
fixed rule expressly forbids that (`TESTS.md:5-9`).

### 5. (d) Metric-aware scalar density: first-order obstruction confirmed, numerical "best" narrowed

The first-order repair condition at `RL1_report.md:177-183` follows from the
inhomogeneous Poisson void exponent.  For a nonzero thin Ricci lens at `u=0`,
the required weighted transform is quartic in the two endpoint offsets, while
the transform of a lens-supported scalar has only the three moments shown at
`RL1_H_density.py:14-23`.  Therefore no single scalar field repairs all
outside-endpoint pairs.

The result does not actually require assuming compact support.  If

`F_eta(y,x)=integral_y^x (u-y)(x-u) eta(u) du`, then
`d_x^2 F_eta=(x-y)eta(x)`.  The target implied by `-ln(nu Delta)` obeys
`d_x^2 F_req/(x-y)=R*y`, which cannot be a function of `x` alone for every
past endpoint (`RL1_referee_checks.py:63-71`).  A single positive-strength
thin Ricci lens is an NEC member and suffices to exclude a universal scalar
repair for the class.

The reproduced 0.769--0.786 residuals are only the least-squares optimum over
the three ray moments and the sampled endpoint grid
(`RL1_H_density.py:10-25`; `RL1_H_density.out:1-3`).  They should not be called
the optimum over every possible four-dimensional, nonlocal, or
endpoint-dependent density prescription.  This scope correction does not
weaken the exact first-order obstruction to one scalar density field.

## Strongest correct statement

For regular pre-caustic scalar propagation, the massless 4D Johnston sum is
exactly the one-hop link kernel, fixed-coupling extra scalar hops add tails but
no direct-cone delta, and every normalizable one-hop kernel whose Palm mean is
only a function of `rho V` retains the wrong direct coefficient
`nu^(-1/2)/(2*pi)`.  The Palm-kernel identity equating the mean retarded inverse
to the inverse mean operator is exact for deterministic-diagonal,
count-dependent retarded operators; the original 4D BD mean nevertheless has
the confirmed unstable pair `z=0.375598+/-5.052239i`.  A universal scalar
density cannot repair the one-hop coefficient even at first order for a thin
net-focusing Ricci lens.  The resolved L=6 scan leaves three distinct
numerically stable candidates, but neither their curved `sqrt(Delta)` mean nor
their physical small-epsilon, fixed-source variance is established; the
shared-path ladder gives only a conditional `ell_k >= 2.25e-15 m` translation.
Accordingly RL1 is **INCONCLUSIVE, leaning FAIL**, bounded to the stated scalar
readout classes—not a confirmed bounded FAIL and not a no-go for other
order-only readouts.
