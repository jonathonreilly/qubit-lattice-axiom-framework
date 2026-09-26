# Primary derivation: population-normalized orientation in the growing process

2026-09-20. Working author result. The separate pre-source mathematical check agrees with the initial derivative and exact generator identities; later-time statements retain the qualifications below.
This is a supplied finite stochastic model, with no physical rate selection or
new axiom. Parent source: PR #8545 at 689941783bea870e08458e079ddb208257d0083d.

## Exact moment identities at arbitrary configurations

Let G be a finite simple graph with V sites. A site is vacant (0) or has an
immutable content a in a six-element menu. Positive symmetric W has row sum 6,
and weights involving a vacancy are 1. A vacancy hop preserves the full content
multiset. Content a is born at vacant x at rate epsilon U_x(a), where
U_x(a)=product over occupied neighbors y of W(a,s_y). Put
N=sum_x 1_(s_x!=0), M_chi=sum_(occupied x) chi(s_x). For every configuration,

```
L N       = epsilon sum_(vacant x) sum_a U_x(a),
L M_chi   = epsilon sum_(vacant x) sum_a chi(a) U_x(a),
L M_chi^2 = epsilon sum_(vacant x) sum_a [2 M_chi chi(a)+chi(a)^2] U_x(a).
```

All motion contributions vanish exactly. These are instantaneous generator
identities, not a closure of expectations. For unit six-axis vectors, summing
over components gives L |M|^2=epsilon sum_x,a [2 M dot v_a+1] U_x(a).

For W(a,b)=1+j v_a dot v_b, a vector component has the explicit birth term
`epsilon (1-n_x)[product_y(1+j m_i(y))-product_y(1-j m_i(y))]`.
The occupancy source is epsilon (1-n_x) times the sum of the corresponding
plus and minus products over the three axes. These polynomials retain every
neighbor correlation. In particular the vacancy indicator cannot be dropped.

## Exact initial response under an independently sampled initial law

Assume G is z-regular. Let chi be a nonzero centered eigenfunction:
`sum_a chi(a)=0`, `W chi=theta chi`, `nu=(1/6)sum_a chi(a)^2>0`.
At each site independently put

```
Pr(0)=1-rho,
Pr(a)=rho/6 + h chi(a)/(6 nu),
```

where 0<rho<1 and h is in a sufficiently small two-sided interval to make all
probabilities nonnegative. The mean content per site is h. A neighbor's mean
factor for a prospective birth of a is

```
1-rho + sum_b W(a,b)[rho/6+h chi(b)/(6 nu)]
 = 1 + h theta chi(a)/(6 nu).
```

The central vacancy and z distinct neighbor states are independent initially.
Therefore at t=0,

```
d E[N]/dt / V = epsilon(1-rho) sum_a [1+h theta chi(a)/(6nu)]^z,
d E[M_chi]/dt / V
 = epsilon(1-rho) sum_a chi(a)[1+h theta chi(a)/(6nu)]^z.
```

At h=0 the density slope is 6 epsilon(1-rho), and its derivative with respect
to h vanishes. The h derivative of the content slope is
`epsilon(1-rho) z theta`. Motion cannot change either total observable, so
no equilibrium approximation or motion-gap assumption is present here.

Write rho(t,h)=E[N_t]/V, m(t,h)=E[M_chi(t)]/V, and
`chi_response(t)=partial_h m(t,h)|_(h=0)`, so chi_response(0)=1.
The gain in **the ratio of expectations** m/rho relative to its initial
linear response 1/rho is

```
G(t)=rho partial_h [m(t,h)/rho(t,h)] evaluated at h=0,
G(0)=1,
G'(0)=epsilon(1-rho)[z theta-6/rho].
```

For the content-symmetric equal/opposite/orthogonal family used in the simulations, the unbiased mean remains zero and the density has zero first derivative under the vector perturbation, so G(t)=rho chi_response(t)/rho(t,0) at all times. A general symmetric row-six matrix need not preserve a centered unperturbed ensemble at later times; that simplification is not claimed for arbitrary W. The derivative of the denominator is essential. This quantity is not
E[M_chi/N], which needs a convention at N=0 and has a different derivative.
For the cubic z=6 j=1/2 vector sector theta=1, G'(0) is strictly negative
at every 0<rho<1, although chi_response'(0)>0. This is an initial-response
statement only; it neither excludes subsequent correlation-driven ordering
nor establishes a finite-density closed field equation. At rho=1 all sites
are occupied and the specified finite system has no allowed moves or births.
At rho=0 the per-record normalization and this response parameterization are
undefined; that case is not covered by the displayed gain formula.

For normalized raw weights (p,q,r), theta_v=6(p-q)/(p+q+4r). The local
feedback changes sign in this initial normalized test at z rho theta_v=6.
For a separately stipulated seven-outcome self-consistency map with vacancy
weight one, content activity chosen for density rho, and neutral W, a content
perturbation passes to each neighbor with eigenvalue rho theta_v/6. Thus its
uniform-mode linear stability boundary has the same algebraic condition.
This is a correspondence between derivatives of two supplied constructions,
not equivalence of their laws, evolution or nonlinear phases. PR #8548 uses
that other construction; no theorem from it is needed for the derivation here.

## Product-law comparison, explicitly not a proved evolution

If independent one-site distributions are imposed as a closure at all times,
linearization around the uniform content law gives

```
rho_dot=6 epsilon(1-rho),
m_dot=epsilon(1-rho) z theta m,
m(rho)/m(rho0)=exp[z theta (rho-rho0)/6],
G_closure(rho)=rho0/rho exp[z theta (rho-rho0)/6].
```

The absolute gain is bounded over rho0<=rho<=1. When theta<=6/z,
`d log G_closure/d rho=z theta/6-1/rho<=0`, so the imposed product closure
predicts decreasing orientation per record. This conclusion applies to the
closure, not automatically to the interacting stochastic process. The new
finite generator and trajectory calculations compare them rather than silently
using the closure as a theorem.

## Exact W=1 calibration

With constant pair weights, the entire homogeneous independent site law stays
independent: symmetric vacancy swaps preserve any homogeneous product law,
and independent six-content births map the product family to the product
family with `Pr(0,t)=(1-rho0)exp(-6epsilon t)` and
`Pr(a,t)=Pr(a,0)+(rho(t)-rho0)/6`. This family solves the finite forward
Kolmogorov equation, whose solution is unique.

Consequently chi_response(t)=1, G(t)=rho0/rho(t), and for the unbiased vector
menu every Fourier structure factor divided by the expected record count is
exactly one. At arbitrary j these are controls, not assumed identities.

## Decisive computation and current status

`growing_exact.py` assembles every transition of all 7^4 configurations on the
four-cycle, using complete global weights for hop acceptance and a sparse
matrix exponential. It checks the moment identities against the full generator,
the initial response derivatives, and the W=1 time-dependent controls.

`growing_sim.py` uses independent local-weight ratios and a dynamic Fenwick
birth-hazard sampler; edge proposals form a rate-|E| Poisson process, with null
hops retained. Its clock is continuous physical model time, reported as
`tau=6epsilon t`. The small-window calibration passed its declared sanity gate;
the exact outputs, raw per-trajectory summaries and comparisons are preserved.
For unbiased independent initial records, the exact likelihood-score identity
is chi_response(t)=E[M_i(t) M_i(0)]/(V rho0 nu). For the six-axis vector menu,
isotropy permits averaging the three components; the implemented control
variate is `1+E[(M(t)-M(0)) dot M(0)]/(V rho0)`.


## Independent-check outcome and retained normalization distinction

`independent_initial_response/REPORT.md` and `SEAL.json` were produced before
primary-source access. The checker uses perturbation P(a)=rho(1+h chi(a))/6,
which rescales the primary h by rho nu; its relative response formulas agree.
It also derives an exact finite-size formula for E[M/N] (zero when empty),
including the covariance with the birth hazard. A four-cycle example with
rho=3/4 and W=1+(4/5)chi chi^T, chi=(1,1,1,-1,-1,-1), has opposite initial
signs for the two ratio conventions. This reinforces keeping our observable
explicit. The general-W limitation on later centering is carried above.
The primary author subsequently rederived the independent second-moment and
random-ratio results using initial-law differentiation and conditional
hypergeometric neighbor counts. They remain supplementary here; a publication
relying on them must carry the full argument and observable convention.
