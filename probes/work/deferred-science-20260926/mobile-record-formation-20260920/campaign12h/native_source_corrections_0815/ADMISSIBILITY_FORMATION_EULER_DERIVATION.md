# Neighbor-dependent formation on the immutable-wave Euler scale

2026-09-21. Conditional theorem with a sealed independent reconstruction
(`independent_admissibility_euler/REPORT.md`); no independent audit or retained
status claimed. This extends the checked smooth-profile proof to the previously supplied multiplicative
neighbor birth rule. It is not an adoption or derivation of a physical clock.
The four-site exchange generator is the axis-balanced construction in
`AXIS_BALANCED_CONTEXT_EXCHANGE_DERIVATION.md`. Full occupied labels remain
immutable under every exchange and formation event.

## 1. Model and conditional theorem

Let Lambda_N=(Z/NZ)^3, with N sufficiently large that the six nearest neighbors
of a site and every four-site exchange footprint are distinct. States are
vacancy 0 and the six unit-axis contents a. Fix a strictly positive finite
6 by 6 matrix W and extend W(a,0)=1. At a vacant site x, form label a at rate

    (beta/N) U_a(x,eta),
    U_a(x,eta)=product_(y: |y-x|=1) W(a,eta_y),

on microscopic time. Exchange rates are fixed, bounded, have a positive
floor for all unequal endpoint swaps, and preserve every homogeneous product
law as proved for the axis-balanced construction. On Euler time the generator
is N L_N+R_N, where the birth rate is beta U_a. Beta>=0 and W do not depend on N.
Formation does not remove or rewrite an existing label; it uses a vacancy.

Given that a birth occurs at x, its conditional content odds are U_a/sum_b U_b.
These are the selected multiplicative neighbor odds studied earlier in this
campaign. This identifies the conditional distribution for this model; the
total hazard beta sum_a U_a and the Euler scaling remain supplied choices.
The finite six-content alphabet and its interpretation also remain supplied.

For six occupied product probabilities p, define p0=1-sum_a p_a and

    m_a(p)=p0+sum_b p_b W(a,b),
    B_a(p)=beta p0 m_a(p)^6.                                  (1)

The smooth-profile limit is

    partial_t p_a+sum_i partial_i J_a^i(p)=B_a(p),             (2)

with the exact exchange current J from the axis-balanced construction.
Assume a C^2 periodic solution on [0,T], all seven probabilities at least
eta>0, and initial relative entropy o(N^3) against its sampled product profile.
Then

    sup_(t<=T) H(mu_t^N|nu_t^N)/N^3 -> 0.                    (3)

In particular the empirical species profiles converge weakly in probability
at each fixed time. There is no assertion that mu_t^N is an exact product,
no fluctuation theorem, no global smooth solution claim, and no interchange
with t->infinity, beta->infinity, or a simplex boundary.

## 2. Relative-entropy proof, with the new reaction step exposed

All estimates in the checked exchange Euler proof remain available with a
new constant in the absolute-entropy bound. Under the uniform seven-state
reference pi, the birth adjoint has at site x the value beta U_a when x has
label a, and -beta sum_a U_a when x is vacant. Thus

    R_N^*1 <= beta max(1,W_max)^6 N^3.

Stationarity of pi for exchanges and the same logarithmic inequality yield

    integral_0^T D_N(sqrt(f_t))dt
      <= N^3[log 7+beta max(1,W_max)^6 T]/(N c_*).            (4)

Here D_N denotes the same unweighted swap square-difference form as in the
checked proof, with its convention fixed there. The finite count-sector
Poincare comparison and marginal Hellinger bound depend only on (4), the
positive exchange floor, and count-sector connectivity. Births need not
preserve a count sector. They therefore still give one-block replacement
for any fixed bounded local observable, including the seven-site birth
footprint. Product versus without-replacement means differ by O(1/M),
and canonical variances of averaged translates are O(1/M), uniformly over
count vectors. Smooth profile coefficients vary by O(l/N) over a block.

The nontrivial question is the adjoint reaction term in the entropy relative
to the evolving inhomogeneous product nu_t. Write theta_a=log(p_a/p0).
Since U_a(x,eta) does not depend on eta_x, its contribution is exactly

    V_x(eta;p_x)=beta sum_a U_a(x,eta)
       [1_(eta_x=a) p0_x/p_(a,x)-1_(eta_x=0)].              (5)

Uniform positivity of the reference p bounds all coefficients and their
first two derivatives. Averaging (5) under a homogeneous product q gives

    Vbar(q;p)=beta sum_a [q_a p0/pa-q0] m_a(q)^6.           (6)

At q=p, the square bracket is zero term by term. Therefore

    Vbar(p;p)=0,
    D_q Vbar(p;p).delta q
      = sum_a beta m_a(p)^6[(p0/pa) delta q_a+sum_b delta q_b]
      = [H(p) B(p)].delta q,                               (7)

where H=diag(1/pa)+(1/p0)11^T is the categorical entropy Hessian.
The derivative of m_a(q)^6 makes no first-order contribution because its
prefactor vanishes at q=p. Consequently

    |Vbar(q;p)-[H(p)B(p)].(q-p)| <= C |q-p|^2              (8)

uniformly for every probability vector q and every reference p in the
fixed interior compact set. The polynomial is smooth on the whole simplex;
q itself need not be interior.

The reaction component of partial_t log(dnu_t/dpi) is exactly
[H(p_x)B(p_x)].(xi_x-p_x). Its one-block replacement cancels the linear
term in (7). Equation (8) leaves the SAME quadratic block deviation already
controlled in the exchange proof by product concentration, block coloring
and the entropy inequality. The transport component still cancels through
H A_i=A_i^T H. The integrated residual is bounded by

    H_N(t)/N^3 <= H_N(0)/N^3 + C integral_0^t H_N(s)/N^3 ds
                   + C_T/l+C_T/sqrt(M)+C_T/M+o_N(1),             (9)

where N first tends to infinity at fixed block size l and M=(2l+1)^3.
The O(1/l) term allows removal of boundary anchors so all seven-site
observables lie inside their canonical blocks. Then l tends to infinity.
Gronwall proves (3), conditional on the stated
smooth interior solution. Product concentration plus the binary-event
entropy inequality gives the fixed-time empirical consequence.

The central distinction from uniform births is important: (5) is not
pointwise equal to the reference-law time derivative. It is its first-order
local-equilibrium projection that cancels. Treating the exact finite-N law
as product would be an unjustified shortcut.

## 3. The W=1+j v dot v family and exact continuum reaction algebra

Take -1<j<1 so every W entry is strictly positive, with
W(a,b)=1+j v_a.v_b. Let g_i=sum_a p_a v_(a,i), rho=sum_a p_a,
q_i=p_(+i)+p_(-i), r_i=q_i-rho/3, and p0=1-rho. Since vacancy has zero vector,

    m_(+i)=1+j g_i,   m_(-i)=1-j g_i.

Thus (1) supplies the exact reaction terms in the continuum equation:

    B_rho=beta p0 [6+30j^2 |g|^2+30j^4 sum_i g_i^4
                                      +2j^6 sum_i g_i^6],
    B_(g_i)=beta p0 [12j g_i+40j^3 g_i^3+12j^5 g_i^5],
    B_(q_i)=beta p0 [2+30j^2 g_i^2+30j^4 g_i^4+2j^6 g_i^6],
    B_(r_i)=B_(q_i)-B_rho/3.                               (10)

These are continuum reaction coefficients justified by (3), not exact
finite-time expectations of the interacting microscopic process.
At g=0, q_i=rho/3 the homogeneous continuum solution obeys

    rho(t)=1-(1-rho0)e^(-6 beta t).                         (11)

Linearization of the full reaction-current system along (11) gives

    delta rho_t+2alpha rho p0 div delta g=-6 beta delta rho,
    delta g_t+(2alpha rho/3) grad delta rho=lambda(t) delta g,
    delta r_i,t=0,     lambda(t)=12 beta j p0(t).           (12)

For a frozen time and wave vector K, the longitudinal characteristic roots
are

    z_+/-=(lambda-6beta)/2
          +/- sqrt((lambda+6beta)^2/4-c_s(t)^2 |K|^2),

while the two transverse vector eigenvalues are lambda and the two
quadrupole eigenvalues are zero. A frozen coefficient spectrum is not a
solution of this time-dependent problem and is not a stability theorem.
The linear acoustic principal symbol remains isotropic at every density.

For a spatially uniform infinitesimal polarization, (12) integrates exactly:

    delta g(t)=delta g(0) exp[2j(rho(t)-rho0)],
    (delta g(t)/rho(t))/(delta g(0)/rho0)
       =rho0/rho(t) exp[2j(rho(t)-rho0)].                   (13)

This is linear response about the continuum background, for each component.
It is a ratio of continuum fields, not an expectation of a random ratio.
For j=1/2 the normalized gain is strictly decreasing before saturation when
0<rho<1. For j>1/2 it can begin increasing after rho>1/(2j), but its total
absolute amplification is bounded by exp[2j(1-rho0)] for positive j.
Negative j damps the absolute uniform vector perturbation. None of this
proves the fate of finite perturbations or stochastic ordering.

At quadratic order, B_(r_i)=30 beta p0 j^2(g_i^2-|g|^2/3)+O(|g|^4).
The isotropic occupation slice is therefore not nonlinearly preserved by
these neighbor-dependent births, even though the quadratic exchange rule
preserves it when births are absent. This is another explicit reason to
retain all six fields rather than closing a two-field wave equation.

## 4. A bound for the actual time-dependent linear system

The independent reconstruction also supplies a bound beyond the frozen-time
spectrum. For each Fourier mode of (12), define the positive entropy energy

    E=E_rho+E_g+E_r,
    E_rho=|delta rho|^2/[rho(1-rho)],
    E_g=(3/rho)|delta g|^2,
    E_r=(3/rho)sum_i |delta r_i|^2,   sum_i delta r_i=0.

Write Lambda=6beta and mu=12beta j(1-rho). Differentiating both the fields
and their time-dependent weights gives the exact identity

    E' = -(Lambda/rho) E_rho
         +[2mu-Lambda(1-rho)/rho] E_g
         -[Lambda(1-rho)/rho] E_r.                         (14)

Indeed the density/vector transport terms cancel because their weighted
coefficients are both 2alpha. The quadrupoles are static in (12), but their
entropy weights still change. Using rho'=Lambda(1-rho) yields

    E(t)<=E(0) exp(integral_(rho0)^rho(t) [4j-1/s]_+ ds)
          <=E(0) exp[4 max(j,0)(1-rho0)].                  (15)

This is uniform in the Fourier wave vector and finite for all t. For j<=1/4
the energy is nonincreasing. For j>1/4 and rho>rho_star=max(rho0,1/(4j)),
the integral in (15) equals
4j(rho-rho_star)-log(rho/rho_star); it is zero before that threshold.
A growing vector amplitude can coexist with this weighted-energy statement.
This bound concerns the linearized continuum system only, not nonlinear
stability or a microscopic central-limit theorem.

## 5. An exact finite-volume witness of nonproduct evolution

At a homogeneous orbit-isotropic product with density rho in (0,1), let
x,y be adjacent distinct sites and select one vector component i. Product
exchange balance contributes zero to the initial derivative, while births
give exactly

    d/dt Cov(v_i(x),v_i(y))|_(t=0)
       =4 beta j rho(1-rho)/3.                            (16)

For a birth at x, the other five neighbor factors average to one. The
remaining product expectation is
E[v_i(y)(1+j v_a.v_y)]=j rho v_(a,i)/3, and summing v_(a,i)^2 over the six
labels gives two. Thus that endpoint contributes2 beta j rho(1-rho)/3;
the other endpoint is equal. Individual vector means and their initial
derivatives vanish by label inversion, so this is connected covariance.
At beta=1/3,j=1/2,rho=1/2 it is1/18. This is an initial-time identity for
the finite microscopic process on macroscopic time, not an assumed
mean-field factorization at later times. It shows explicitly why the exact
product fluctuation argument requires new work for these births.

## 6. Limits, evidence and next obligations

The conditional theorem establishes a connection to the declared neighbor-dependent
odds without selecting the clock or making a quantum interpretation. It
also does not turn the acoustic sector into gravity or Lorentz symmetry.
The hydrodynamic proof permits bounded fixed W and beta, with fixed positive
exchange floor and an interior smooth reference solution. The formation
scale beta/N is essential for this reaction contribution on Euler time.

For j!=0 the exact microscopic law is generally not product after births.
The stationary and exactly-growing-product fluctuation proofs cannot simply
be reused. A central-limit statement here requires a stronger nonstationary
replacement argument and control of the fluctuation law, not just (3).
The formation martingale's formal covariance beta p0 I at the isotropic
background is only a candidate coefficient until that proof is supplied.

The separate reconstruction read only the declared generator and its own
previous sealed exchange proof before sealing. Its report SHA is
`dddec2c24051a77ff46e5c333e4a63c269ddb4b1739f60ba8543b8b0fcde023c`;
pre-source seal SHA is
`bcc3bc4ccdefc35df7fd42c8427b2fa7bd8350dab8a747169acd683c88`.
All ten listed artifacts and nine dependencies were verified, and the full
report and checker read. Eleven exact groups and four numerical controls
include all924 six-neighbor count sectors, general nonsymmetric positive W,
the seven-site score derivatives, full six-field source algebra, (14)-(16),
and a time-dependent ODE comparison. The checker corrected an initially
mislabeled biased raw pair derivative to a connected covariance and retained
the first script/log; the balanced value1/18 is unchanged. These evidence
counts do not substitute for the arguments or constitute formal retention.

Next: control correlation-induced finite-size centering and replacement at
fluctuation scale. The separate symmetric-stirring calculation in
`NATIVE_FORMATION_THIRD_ORDER_CENTERING_DERIVATION.md` supplies a primary
perturbative test case, not a ready-made theorem for the driven wave model.
