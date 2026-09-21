---
claim_id: mobile_records_native_formation_euler_and_cubic_centering_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied seven-state immutable-record exchange model with fixed positive exchange floor and vacant-site formation beta/N times a fixed six-neighbor product of strictly positive weights: given a C2 interior reaction-current solution and o(N^3) initial relative entropy, the empirical profiles obey the stated Euler law. Its local reaction-adjoint constant and linear terms cancel after replacement, although the interacting finite-volume law is generally not product. Exact source algebra, a nonautonomous linear entropy-energy bound and an initial adjacent-covariance witness are included. In the separately specified constant-rate symmetric-stirring model with weights 1+j va dot vb and homogeneous isotropic initial law, the first two density Taylor coefficients vanish, the cubic coefficient is positive, and N times that coefficient has the displayed three-dimensional Green-function limit with a proved uniform punctured-torus heat bound. All Taylor claims extract coefficients at j=0 before the lattice limit; no uniform fixed-j remainder, native fluctuation theorem, driven-generator centering coefficient, axiom-selected clock, quantum realization or physical force law is asserted."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_immutable_context_exchange_acoustic_limits_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_native_formation_euler_and_cubic_centering_2026_09_21.py
---

# Native record formation: a conditional Euler law and a cubic correlation correction

**Date:** 2026-09-21  
**Type:** bounded_theorem  
**Status:** proposed_retained  
**Author support:** conditional-support; no independent audit verdict.

A site emptied by transport can form another permanent record. For the
specified neighbor-dependent formation rates, the macroscopic reaction law
can be justified without pretending that the actual interacting law stays
product. The same interactions produce a calculable density correction in
a separately controlled symmetric-stirring model. Together these results
identify a concrete obligation for a future formation fluctuation theorem.

The finite alphabet, exchange rule, formation hazard and Euler clock are
supplied model choices, not a derivation from [the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
Occupied labels are moved unchanged; formation acts only on vacancies.
No qubit realization, physical particle interpretation, continuum geometry
selection or theory-of-everything closure follows from this construction.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "Can neighbor-dependent formation after immutable-record transport be controlled beyond an exact-product assumption?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Control the fixed-coupling fluctuation centering and nonstationary replacement for the driven exchange generator."
conditional_surface_status: "Given smooth interior PDE, Euler theorem; exact formation algebra and linear energy; separately specified symmetric-stirring cubic Taylor coefficient and three-dimensional limit."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional proofs with separately reconstructed reaction cancellation, response hierarchy and uniform finite-volume heat estimate."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Part A uses the axis-balanced four-site-context exchange from the
[acoustic limit note](MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md).
Part B sets that drive to zero and uses constant symmetric stirring. The
third-order coefficient in Part B is not a coefficient for nonzero drive.
The two parts use their own equation numbers. Their smooth hydrodynamic and
perturbative limits have different hypotheses and cannot be interchanged.

## Part A. Neighbor-dependent formation on the Euler scale

### 1. Model and conditional theorem

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

### 2. Relative-entropy proof, with the new reaction step exposed

All estimates in the checked exchange Euler proof remain available with a
new constant in the absolute-entropy bound. Under the uniform seven-state
reference pi, the birth adjoint has at site x the value beta U_a when x has
label a, and -beta sum_a U_a when x is vacant. Thus

    R_N^*1 <= beta max(1,W_max)^6 N^3.

Stationarity of pi for exchanges and the same logarithmic inequality yield

    integral_0^T D_N(f_t)dt
      <= N^3[log 7+beta max(1,W_max)^6 T]/(N c_*).            (4)

Here f_t=dmu_t^N/dpi is the density relative to the uniform product and
D_N(f)=sum_e E_pi[(sqrt(f(eta^e))-sqrt(f(eta)))^2], the unweighted
swap square-difference form used in the checked proof. The finite count-sector
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

### 3. The W=1+j v dot v family and exact continuum reaction algebra

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
For beta>0 and j=1/2 the normalized gain is strictly decreasing before saturation when
0<rho<1. For j>1/2 it can begin increasing after rho>1/(2j), but its total
absolute amplification is bounded by exp[2j(1-rho0)] for positive j.
For beta>0, negative j damps the absolute uniform vector perturbation.
At beta=0 both uniform gains in (13) are identically one. None of this
proves the fate of finite perturbations or stochastic ordering.

At quadratic order, B_(r_i)=30 beta p0 j^2(g_i^2-|g|^2/3)+O(|g|^4).
The isotropic occupation slice is therefore not nonlinearly preserved by
these neighbor-dependent births, even though the quadratic exchange rule
preserves it when births are absent. This is another explicit reason to
retain all six fields rather than closing a two-field wave equation.

### 4. A bound for the actual time-dependent linear system

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

### 5. An exact finite-volume witness of nonproduct evolution

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

### 6. Limits, evidence and next obligations

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
`bcc3bc4ccdefc35df7fd42c8427b2fa7bd8350dab8a7471692ea169acd683c88`.
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
Part B supplies an independently reconstructed
perturbative test case, not a ready-made theorem for the driven wave model.

## Part B. A cubic density correction under symmetric stirring

### 1. Model, coefficients and exact unperturbed law

On the cubic torus of side N>=4, each nearest-neighbor bond swaps its two
unchanged states at microscopic rate kappa>0, independent of labels. There
are vacancy and six unit-axis labels. At a vacant x, label a forms at
microscopic rate (beta/N) product_{y~x}(1+j v_a dot v_y), |j|<1.
Work on macroscopic time, so the exchange generator has factor N and birth
intensity beta. Kappa,beta are fixed positive numbers. Initially the law is
product with vacancy v0 in (0,1) and each occupied probability (1-v0)/6.

At j=0 the evolving law is exactly product with

    v(t)=v0 exp(-lambda t), rho(t)=1-v(t), lambda=6 beta.

Finite state-space evolution is analytic in j for each fixed N,T. All series
coefficients here are coefficients of powers of j, without factorials. Let

    E_j n_x(t)=rho(t)+j m1_N(t)+j^2 m2_N(t)+j^3 m3_N(t)+...,
    E_j[v_i(x,t)v_k(y,t)]=j delta_ik C_N(y-x,t)+O_N(j^2), x!=y.

The global vector means vanish exactly by label inversion. The coefficient
C_N is independent of i by internal cubic symmetry. The O_N notation does
not assert a bound uniform in N. No conclusion about fixed nonzero j may be
obtained simply by replacing that notation with O(j^2).

### 2. First-order pair response closes exactly

Let D_N=torus\{0}, and let Delta_ref be the unit-rate lattice Laplacian on
that graph, with edges leading to the removed origin omitted. Write
b(r)=1_{r is a nearest neighbor of 0}. Then

    partial_t C_N=2 kappa N Delta_ref C_N+S(t)b,
    C_N(r,0)=0,       S(t)=4 beta rho(t)v(t)/3.             (1)

For stirring, moving either endpoint of a two-site product moves its
separation by one lattice step. Swapping the two marked endpoints leaves
their product unchanged, which explains the missing jumps to the origin.
Both endpoints give the factor 2 kappa N. At j=0 an independent uniform
birth has zero vector mean and its generator annihilates a two-site vector
product. Differentiating a birth across an adjacent marked pair gives
2 beta rho v/3 at each endpoint, hence S(t).

To expose the closure without a hidden moment truncation, introduce the
marked stirring generators H2 and H3 at unit bond rate. H2 tracks an
unordered pair of distinct vector-feature positions. H3 tracks those two
positions and a distinct vacancy-feature position. A swap between a vector
feature and the vacancy feature exchanges their positions; it is not blocked.
The projection of H3 onto the two vector positions is therefore exactly H2.

For fixed vector components i,k define, on distinct sites,

    Q_ik(y,z)=[j] E_j[v_i(y)v_k(z)],
    T_ik(x;y,z)=[j] E_j[1_(eta_x=0) v_i(y)v_k(z)].

At j=0 uniform births have zero vector drift and vacancy drift -lambda.
The first birth derivative of v_i(y) is
2 beta 1_(eta_y=0) sum_(w~y) v_i(w). At the unperturbed product, its pair
source survives only for w=z and gives 2 beta v rho delta_ik/3 at that
endpoint. The two endpoints give the full source S(t)delta_ik. With the
additional vacancy feature, w=x vanishes because vacancy times its vector
is zero; the remaining source acquires one factor v(t). Hence

    Q_ik' = kappa N H2 Q_ik + delta_ik S(t)1_(y~z),
    T_ik' = (kappa N H3-lambda)T_ik
                     +delta_ik v(t)S(t)1_(y~z).

Both initial data vanish. Since v'=-lambda v and H3 projects to H2,
v(t)Q_ik(y,z) solves the second finite linear system. Uniqueness proves

    [j] E_j[1_(eta_x=0) v_i(y)v_k(z)]
        =v(t) delta_ik C_N(z-y,t).                       (2)

This is an equality of first-order coefficients, not finite-j independence.
In relative coordinates, swapping adjacent selected endpoints reverses the
separation. The covariance and its source are even under r->-r, so this
reversal contributes zero. Equation (1) is the resulting reflected walk
on the even functions needed here.

### 3. The first density correction is cubic in the alignment parameter

Summing birth labels eliminates every odd power of j in the instantaneous
total birth intensity. Its second-order term is exactly

    [j^2] R_j n_x
      =2 beta 1_{eta_x=0}
           sum_{unordered distinct y,z in neighbors(x)} v_y dot v_z.

Every corresponding product expectation is zero at j=0. Therefore
m1_N=m2_N=0. Using (2), the third coefficient obeys

    m3_N'=-lambda m3_N+6 beta v(t)
          sum_{unordered y,z in neighbors(0)} C_N(z-y,t),
    m3_N(0)=0.                                           (3)

The factor 6 is 2 from the six-label second moment times 3 vector
components. No neighbor pair in this sum is adjacent to one another on the
cubic lattice. Stirring must propagate the initially nearest-neighbor pair
response to those separations. Consequently very-short-time and large-N
limits are not interchangeable.

For fixed finite N the semigroup in (1) is positive. Connectivity and S>0
give C_N(r,t)>0 and m3_N(t)>0 for t>0. This is a statement about the third
Taylor coefficient; it is not an all-j monotonicity theorem.

### 4. Three-dimensional large-N coefficient

Define the infinite-lattice Green function for the **unit-rate** Laplacian

    -Delta G=delta_0,
    G(r)=(2pi)^(-3) integral_[-pi,pi]^3
                exp(i k dot r)/[2 sum_i(1-cos k_i)] dk.

The integral is finite in dimension three. It is positive and tends to zero
at infinity. At a nearest neighbor, G(0)-G(e_i)=1/6. Removing the edge to
the origin therefore gives

    -Delta_ref [6G(r)]=b(r),       r!=0.                 (4)

Hence the integrated heat semigroup on the punctured infinite lattice
applied to b is 6G. For each fixed r!=0,t>0, (1) consequently predicts

    N C_N(r,t) -> [4 beta rho(t)v(t)/kappa] G(r).         (5)

The required passage can be made with a heat-kernel bound. The finite
punctured tori satisfy, with constants independent of N,

    (exp(u Delta_ref)b)(r) <= C[(1+u)^(-3/2)+N^(-3)].

The complete uniform bound is proved in Section 4a. It uses a bounded-energy
extension across the missing origin and a Fourier proof of the finite-volume
Nash inequality. No mixing-time assertion is imported.

After u=2 kappa N(t-s), the left side of (5) is

    (1/(2 kappa)) integral_0^(2 kappa Nt)
         S(t-u/(2 kappa N)) (exp(u Delta_ref^N)b)(r) du.

For fixed u the torus kernel converges to the infinite-graph kernel:
a finite number of jumps sees the same graph, and the remaining jump-count
tail is bounded by a Poisson tail. The integrated large-u tail is bounded
by C/sqrt(U)+C Nt/N^3, uniformly in N. Splitting at fixed U, then taking
N and U to infinity, proves (5). It also supplies a uniform bound for N C_N on fixed time
intervals, permitting dominated convergence in (3).

Among the fifteen unordered pairs of six neighbors, three have separation
2e_i and twelve have separation e_i+/-e_j. Put

    A_star=3G(2e_1)+12G(e_1+e_2)=15G(0)-3>0.             (6)

The second equality follows from the harmonic equation at e_1:
6G(e_1)=G(0)+G(2e_1)+4G(e_1+e_2), and G(e_1)=G(0)-1/6.
Equation (3) then gives the explicit coefficient

    N m3_N(t) -> D(t),
    D(t)=(24 beta^2 A_star/kappa)
          integral_0^t exp[-lambda(t-s)] rho(s)v(s)^2 ds
        =(4 beta A_star/kappa) v0^2 z
              [(1-z)-(v0/2)(1-z^2)],
    z=exp(-lambda t).                                    (7)

D(t)>0 for every t>0 and interior initial density. Kappa is fixed before
the large-N limit. The coefficient proportional to 1/kappa does not justify
taking kappa to zero, where the spatial spreading premise changes.

### 4a. Uniform heat estimate on the punctured tori

Use counting measure and Dirichlet energy

    E_D(f)=sum_{unoriented edges in D_N} |f(x)-f(y)|^2.

For N>=4 the six neighbors of the removed origin are distinct. Any two can
be joined inside D_N by a path of length at most four. Perpendicular
neighbors use their common diagonal intermediate vertex (length two).
Opposite neighbors use a different coordinate direction as a detour (length
four). These paths avoid the origin also on the N=4 torus.

Extend f to the full torus by F(0)=m, the average over the six neighbors,
and F=f elsewhere. The exact variance identity and path Cauchy-Schwarz give

    sum_y |f(y)-m|^2 = (1/6) sum_{y<z}|f(y)-f(z)|^2
                      <=10 E_D(f).

The last deliberately loose bound uses fifteen paths of length at most
four, with every edge used at most fifteen times. Consequently

    E_T(F)<=11 E_D(f),
    ||F||_1<=(7/6)||f||_1,
    ||f||_2^2<=||F||_2^2<=(7/6)||f||_2^2.                (8)

The L1 estimate uses |m|<=sum_neighbor|f|/6; the L2 estimate uses Jensen.
Both are valid for real or complex f.

Here is the finite-torus Nash estimate with a uniform constant:

    ||F||_2^(10/3)
      <=C [E_T(F)+N^(-2)||F||_2^2] ||F||_1^(4/3).        (9)

For completeness, use the orthonormal Fourier transform and representatives
k_i in [-N/2,N/2]. The eigenvalue is
4 sum_i sin^2(pi k_i/N), bounded below by c|k/N|^2.
For 1/N<=R<=1, the contribution of |k/N|<=R to Parseval is at most
C R^3 ||F||_1^2, since there are at most C(NR)^3 frequencies and each
squared Fourier coefficient is at most N^(-3)||F||_1^2. The complement
contributes at most C R^(-2) E_T(F). Optimizing R proves (9) when the
optimizer lies in [1/N,1]. At the lower endpoint the residual bound
||F||_2^2<=C N^(-3)||F||_1^2 is absorbed by the N^(-2) term in (9).
At the upper endpoint, use ||F||_2<=||F||_1 and the fact that the
optimizer exceeding one means E_T(F)>=c||F||_1^2. A zero function is
trivial; endpoint constants can be enlarged uniformly. Equivalently the
split gives

    ||F||_2^2 <= C E_T(F)^(3/5)||F||_1^(4/5)
                     +C N^(-3)||F||_1^2,

which implies (9) by separating which of its two terms is at least half
the left side. These arguments involve finite Fourier sums only.

Combining (8) and (9) transfers (9) to D_N, with E_D in place of E_T.
Let P_t=exp(t Delta_ref), f_t=P_t delta_x and y(t)=||f_t||_2^2.
Positivity and conservation give ||f_t||_1=1, and differentiation gives

    y'(t)=-2 E_D(f_t),
    E_D(f_t)>=c y(t)^(5/3)-N^(-2)y(t).                  (10)

If y>=C0 N^(-3) for a sufficiently large fixed C0, the last term is
absorbed into half the first, so y'<=-c1 y^(5/3). Also y is always
nonincreasing and y(0)=1. Integrating until this threshold is reached,
and then using monotonicity, yields

    y(t)<=C[(1+t)^(-3/2)+N^(-3)].                       (11)

The semigroup identity gives P_(2t)(x,x)=y(t). Cauchy-Schwarz applied
to P_t(x,y)=sum_z P_(t/2)(x,z)P_(t/2)(z,y) gives the same bound for every
x,y after changing C. Summing over the six neighbors proves the bound
used in (5). Constants do not depend on N, r or t.

For each fixed t and fixed vertices, the finite-torus kernels tend to
the infinite punctured-lattice kernel: uniformize at rate six, couple
steps until reaching a representative-box boundary, and use the tail
of a Poisson(6t) jump count. Thus (11) also implies the infinite-graph
bound C(1+t)^(-3/2). Its potential of b is finite.

It remains to justify its explicit value, rather than assume uniqueness
of an inverse on an infinite graph. W(r)=6G(r), r!=0, is bounded,
nonnegative, tends to zero at infinity and satisfies -Delta_ref W=b.
For this bounded generator, differentiation of P_t W gives exactly

    W-P_t W=integral_0^t P_s b ds.

On a fixed finite set, the heat bound makes P_t W tend to zero; outside
that set W is uniformly small. More explicitly, split the expectation
into the finite set and its complement, use a finite sum of kernel
bounds on the first and sup W on the second, then enlarge the set.
This proves P_t W(r)->0 and establishes integral_0^infinity P_s b ds=6G(r).
Together with the integrable tail estimate already given, this closes
the large-N proof of (5)-(7). The sealed independent reconstruction supplies its own marked-particle
closure and uniform finite-torus proof, with the same coefficient. Its
normalization uses the Green function for 2 Delta, exactly half of G here.

### 5. Fluctuation-scale implication and its exact limit

The zero Fourier mode at central-limit normalization has mean
N^(3/2)[E_j n_x(t)-rho(t)]. Its third Taylor coefficient is
N^(3/2)m3_N(t), which by (7) grows as sqrt(N) D(t).

Thus the first nonzero perturbative density response is negligible for the
Euler law but not for its naive fluctuation centering. This identifies a
specific deterministic correction to compute before claiming a native-birth
central-limit theorem centered at the product reaction solution.

It does **not**, by itself, disprove such a theorem for a fixed nonzero j:
that would require uniform control of higher Taylor coefficients or another
argument. It also does not establish the corresponding coefficient for the
nonreversible axis-balanced wave generator. The present calculation is a
controlled symmetric-stirring test case and a concrete next obligation for
the interacting formation lane.

### 6. Completed primary controls and remaining obligations

the archived author script `native_formation_centering_check.py` assembles the complete 2401-state
four-cycle generator and its 9604-state Taylor jet through order three,
separately from the punctured-relative-position response. On that cycle
use its two-neighbor formation footprint and its one neighbor pair; the
six internal labels and per-label beta are unchanged. At beta=.2,
kappa=.75,v0=.4, eight times through t=.7, the first two mean-density
coefficients vanish to below4e-17. All pair coefficients and the
vacancy-weighted pair projection agree to below1.1e-17; the third density
coefficient agrees to below4.8e-18 (final value .00163432385382513).
These are numerical matrix-exponential controls with exact integer-scaled
generator assembly, not exact arithmetic evaluation of the exponential.

A separate three-dimensional response computation at beta=.2,kappa=.75,
v0=.6 uses N=4,8,16,24,32,48,64 with no fitted coefficient. At t=1,
N m3_N rises from .02697975 at N=8 to .03322368 at N=64, versus the
Green-function target .03897323. The N=4 value is .04296748: the finite
size sequence is not globally monotone and must not be reported as such.
The Green quadrature gives G(0)=.2527310098587 and A_star=.79096514788;
its QUADPACK error estimate is not an interval certificate. All seven
cases and the full finite-cycle output are preserved, including that
small-torus deviation.

The independent report is the archived independent centering report, SHA
`24b168b662c0e6f72f1b2f95a6efe7fb3440eb5b5d57addf951020335fe05f4e`.
Seal SHA `cb26009a925ecd6861de994e57df67f904f906e5beac33aae6e6ed958b8a5d8e`
binds ten artifacts, three source dependencies and two instruction snapshots,
all verified. The complete report and checker have been read; eleven controls
include a separately assembled full cycle jet and finite-torus Poisson checks.
These checks do not replace the proof or constitute formal retention.

Next obligations: if seeking a fixed-j statement, control the remainder
uniformly in N. The driven exchange generator requires its own response
analysis. The present result supplies neither of those extra conclusions.

## Evidence, reproduction and open physical obligations

The adjacent packet
[mobile-record-native-formation-20260921](../.claude/science/mobile-record-native-formation-20260921/README.md)
contains byte-preserved independent reconstruction reports, their scripts,
all unsuccessful attempts and source seals. The two new reconstructions
were sealed before access to the author's native-formation sources; they
reuse explicitly identified earlier exchange proofs where applicable.
A final-source review separately checks the assembled publication argument.
These checks are mathematical evidence, not the independent audit verdict
required for effective retained status.

The canonical runner checks the reaction identities, the complete finite
four-cycle Taylor jet, the closed relative-walk response, selected finite
three-dimensional identities and the stated energy/source formulas. Numerical
matrix exponentials use tolerances; they are distinguished from exact symbolic
and rational controls. No finite numerical run proves the heat-kernel theorem.
The original seven-size response run and its unfitted Green target are retained
as supplemental evidence, including the nonmonotone N=4 case. A mutation mode
alters a load-bearing expression and must be rejected by an unchanged identity.

Reproduce from the repository root:

```bash
python3 scripts/mobile_records_native_formation_euler_and_cubic_centering_2026_09_21.py
python3 .claude/science/mobile-record-native-formation-20260921/verify_capsules.py
```

The next mathematical questions are uniform fixed-j remainder control and
fluctuation replacement for the actual driven process. The next physical
questions are why these labels, rate tensor, formation law and clock should
be selected. The result does not supply Gauss constraints, a physical force,
quantum dynamics, Lorentz invariance or gravity. No primitive registry,
editable prompt or audit verdict is changed.
