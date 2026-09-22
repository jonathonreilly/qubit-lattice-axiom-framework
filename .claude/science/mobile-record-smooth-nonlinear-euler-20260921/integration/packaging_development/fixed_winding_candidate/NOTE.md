---
claim_id: mobile_records_smooth_nonlinear_euler_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the specified permanent-color exchange process on a fixed winding matching, any strictly positive periodic C3 solution of the derived fourteen-color conservation law governs the Euler-time process over its smooth interval when the initial relative entropy per pair vanishes. This is a conditional hydrodynamic limit with supplied rates and preparation, not a birth-selected state, moving-geometry theorem or quantum TOE."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_moving_geometry_color_waves_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_smooth_nonlinear_euler_2026_09_21.py
---

# Smooth nonlinear evolution of permanent mobile record colors

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

The existing local exchange process for permanent record pairs supports a
finite-amplitude, fourteen-color conservation law over each stipulated smooth
time interval. This is not a derivation from the
[minimal record axioms](MINIMAL_AXIOMS_2026-06-29.md). The stochastic rates,
Euler clock scaling, fixed winding matching and inhomogeneous preparation
are specified assumptions.

The result strengthens the earlier initial-drift and stationary fluctuation
calculations in one concrete direction. Let K=N^3/2 and let p(t,x) be a fixed
periodic C3 solution, bounded away from the probability-simplex boundary.
If H(mu_N(0)|nu_N(0))=o(K), then the actual law satisfies
sup_t H(mu_N(t)|nu_N(t))/K ->0, with uniform-time weak empirical convergence
to p. The proof controls correlations by entropy dissipation and conditional
finite-block mixing. It does not assert a product law at later times or
convergence of the whole microscopic distribution in total variation.

The full nonlinear flux is
F_a=gamma p_a[e_a cross Y+X cross b_a-2 X cross Y].
Its exact thirteen-moment representation includes six vector components and
seven additional moments. The convex entropy sum p log p symmetrizes the
Jacobian on the simplex tangent. At anisotropic rest states the vector
sector generally has two distinct polarization speeds. Equal speeds on
three axes force isotropic second moments when gamma is nonzero. A hidden
cubic moment can remain invisible to that linear optical diagnostic.

The three source arguments follow in full. Original pending-review status
sentences are historical; the sealed reports define the completed selective
check coverage. Formal retention remains unaudited.

## I. Nonlinear flux, entropy and anisotropic optical diagnostics

**Status:** proposed exact flux/PDE identities with author controls and
independent check pending. **Date:** 2026-09-21.

This returns to the existing permanent-color routed process. Its homogeneous
product-law current is exact. Applying that current to a spatially varying
local-equilibrium profile gives a candidate thirteen-component conservation
law. The calculations below prove algebraic properties of that candidate;
they do not establish its inhomogeneous hydrodynamic limit from the
microscopic process. The earlier stationary Gaussian Euler theorem is a
different, smaller-amplitude result.

### 1. Exact homogeneous current and the candidate conservation law

Use the same six axis colors A, with e=+/-e_i,b=0, and eight cube colors B,
with e=0,b in {+/-1}^3. For strictly positive probabilities p_a summing to
one, put X=sum_a p_a e_a and Y=sum_a p_a b_a. Take gamma!=0 when discussing
propagating speeds; the algebraic flux identities also hold at gamma=0.
The current already derived in
`DIMER_ROUTED_RECORD_TRANSPORT.md` is

    F_a(p)=gamma p_a[e_a cross Y+X cross b_a-2 X cross Y]. (1)

All spatial components use this same vector formula; sum_a F_a=0. The
candidate continuum equation is

    partial_t p_a + div F_a(p)=0.                    (2)

No assumption that arbitrary microscopic profiles remain product measures
is made. A proof of local replacement, control of entropy, and a smooth-time
hydrodynamic limit for the routed process would still be required to identify
(2) with a microscopic limit. Shocks or positive-density fluctuations are
not covered by the stationary linear theorem.

### 2. A complete moment representation

Define D_i=sum_A p_a e_(a,i)^2, so rho_A=sum_i D_i and rho_B=1-rho_A.
For i<j set Z_ij=sum_B p_a b_i b_j, and w=sum_B p_a b_1 b_2 b_3. Along
with the six means X,Y, the three D_i, three Z_ij and w are thirteen
independent real coordinates on the probability simplex. The exact inverse is

    p_(A,i,sigma)=(D_i+sigma X_i)/2,
    p_(B,b)=[rho_B+b.Y+sum_(i<j) b_i b_j Z_ij
                         +b_1 b_2 b_3 w]/8.        (3)

Positivity means precisely that all fourteen numerators in (3) are positive.
No closure approximation is used to obtain these coordinates. Set the
symmetric matrix M_B by (M_B)_ii=rho_B and (M_B)_ij=Z_ij for i!=j, and let
r=(Z_23,Z_13,Z_12). For each variable below its vector flux is exactly

    F_(D_i)=gamma[X_i e_i cross Y-2D_i X cross Y],
    F_(X_i)=gamma[D_i e_i cross Y-2X_i X cross Y],
    F_(Y_i)=gamma[X cross (M_B e_i)-2Y_i X cross Y],
    F_(Z_ij)=gamma[X cross (Y_j e_i+Y_i e_j+w e_k)
                                      -2Z_ij X cross Y],
    F_w=gamma[X cross r-2w X cross Y],               (4)

where k is the third index in the Z_ij line. In particular,

    F_(rho_A)=gamma(1-2rho_A)X cross Y.              (5)

Thus the seven additional population coordinates cannot generally be held
fixed in a finite-amplitude version of the wave equations. At an orbit-
isotropic rest profile X=Y=Z=w=0, D and Z have quadratic sources in
the vector fields; w is driven through the generated Z variables at the next
order. This order statement concerns that background, not arbitrary w or Z.

### 3. Convex entropy and real characteristic speeds

For a spatial direction n define a real symmetric fourteen-by-fourteen
matrix

    K^(n)_ab=n.[e_a cross b_b+e_b cross b_a].

Let v=Kp, M=p^T Kp, eta(p)=sum_a p_a log p_a. The directional flux from
(1) is gamma[diag(p)Kp-pM]. On the tangent space sum_a u_a=0 its Jacobian is
the restriction of

    A=gamma[diag(v-M)+diag(p)K-2p v^T].             (6)

The Hessian of eta is diag(1/p_a). For tangent vectors u,z,

    u^T Hess(eta) A z
       =gamma u^T[diag((v-M)/p)+K]z,                (7)

because the last term contains u^T 1=0. The right matrix is symmetric, and
the restricted entropy Hessian is positive definite for p_a>0. Hence every
directional Jacobian on the thirteen-dimensional simplex tangent space is
similar to a real symmetric matrix: all characteristic speeds are real and
the principal part is symmetrizable. This is an algebraic property on the
interior simplex, not a proof of global smooth solutions or shock selection.

An entropy flux can also be written explicitly. For each spatial component,
or equivalently after contraction with n, set

    q_eta^(n)=gamma[sum_a p_a log p_a (Kp)_a
                       -eta M-M/2].               (8)

Differentiating (8) along a tangent variation gives
grad eta dot A times that variation. Therefore every smooth interior
solution of (2) obeys partial_t eta+div q_eta=0. The minus-M/2 term is
necessary. Convexity and symmetrization do not imply that the microscopic
entropy production or a nonsmooth entropy solution has already been derived.

### 4. Rest profiles and a precise birefringence test

At a constant rest profile X=Y=0, let D=diag(D_1,D_2,D_3) and B=M_B.
Strictly positive color probabilities make D and B positive definite. The
six vector perturbations close linearly:

    X_dot=gamma D curl Y,
    Y_dot=-gamma B curl X.                          (9)

They conserve the positive quadratic integral
[X^T D^-1 X+Y^T B^-1 Y]/2. Their conserved divergence combinations are
div(D^-1 X) and div(B^-1 Y); assigning the unweighted divergences the same
role would generally be wrong at anisotropic rest profiles.

For a wavevector along e_1, the two squared propagation speeds are

    c_+/-^2 = (gamma^2/2)[rho_B(D_2+D_3)
       +/- sqrt(rho_B^2(D_2-D_3)^2+4D_2D_3 Z_23^2)]. (10)

This follows by restricting -D[e_1 cross]B[e_1 cross] to its transverse
two-by-two matrix. Analogous formulas hold cyclically. Positivity implies
both speeds are positive. Their equality on this axis holds exactly when
D_2=D_3 and Z_23=0. Equality on all three coordinate axes consequently holds
exactly when

    D=(rho_A/3)I,              B=rho_B I.            (11)

Under (11) the two speeds agree in every direction, with
c=|gamma|sqrt(rho_A rho_B/3), as in the stationary wave theorem. This is
an exact criterion within the stated rest-profile family; it is not a
theorem against different record laws, other encodings or general metrics.

For a concrete positive profile take D_i=1/7, rho_B=4/7, Z_23=1/14 and
Z_12=Z_13=w=0. Equation (3) gives positive probabilities. Along e_1 the two
squared speeds are gamma^2/14 and 9gamma^2/98, whereas the e_2 and e_3 axes
have coincident squared speeds 4gamma^2/49. Thus positive homogeneous
stationarity alone does not select the common isotropic optical branch.

Conversely, a nonzero w with X=Y=Z=0 and D_i=rho_A/3 does not alter (9).
For example w=1/14 at rho_A=3/7,rho_B=4/7 is still strictly positive and has
the same six-vector linear optical spectrum as w=0. It changes higher color
moments and other components of the full population response. Optical
isotropy of these six means is therefore not full isotropy of the color law.

### 5. Use in the campaign

Equations (3)-(8) provide a finite, explicit nonlinear continuation of the
exact homogeneous current, with a strictly convex entropy and real
characteristic speeds. Equations (10)-(11) supply a diagnostic for which
rest populations retain the common two-polarization branch. They make
finite-amplitude feedback and anisotropy testable without assigning a
gravitational interpretation to every coefficient change.

The missing microscopic inhomogeneous-limit proof is explicit. No quantum
generator, Born readout, matter coupling, spacetime metric, or TOE follows
from this candidate PDE. The useful next test is whether the actual routed
process follows these nonlinear currents for controlled slowly varying
profiles before shocks, and which preparation/dynamics select the required
background and perturbation regime.

## II. The exact microscopic initial derivative

**Status:** proposed conditional initial-time theorem; controls and independent
check pending. **Date:** 2026-09-21. **Dependencies:** the actual routed rates
in `DIMER_ROUTED_RECORD_TRANSPORT.md` and the flux definitions in
`DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md`.

Fix an even torus side N>=8 with the winding matching from every black site
u to the white site u+e_1. All records remain permanent, pair colors are
immutable, and only the existing routed color-exchange dynamics is used.
Take k0>|gamma|. At time zero draw independent colors at black anchors with
probabilities p(u/N), where p is a fixed C^3 periodic profile in the interior
of the fourteen-color simplex. This is a supplied inhomogeneous preparation;
it is not asserted to be produced by the earlier birth law.

For a direction delta in {+/-e_i}, the owner route has displacement

    a_delta=delta-e_1.

The +e_1 route is fixed and has no exchange. For the five other directions,
the four distinct contexts are at u-a_delta,u,u+a_delta,u+2a_delta. Let their
probabilities be p_l,p_u,p_w,p_r. Set

    S_delta(a,b)=(gamma/2)delta.[e_a cross b_b+e_b cross b_a],
    s=S_delta(p_l+p_r),
    mu_u=p_u.s,        mu_w=p_w.s.

The actual channel rate is k0/2+h/4, where
h=S(l,a)+S(a,r)-S(l,b)-S(b,r). Summing over the four independent initial
colors gives the **exact** expected outgoing color-current vector

    J_delta^N(u)
      =(k0/2)(p_u-p_w)
        +(1/4)[(p_u+p_w) elementwise s
                         -p_u mu_w-p_w mu_u].       (1)

Its fourteen entries count color moving from u toward its route successor;
their sum is zero. This calculation uses independence only at time zero.
It does not replace later joint laws by products.

All current sums below run over the five nonfixed directions. The final
tensor identity can also include +e_1 because its displacement is zero.

For I_(u,a) the indicator that anchor u carries color a, the Markov generator
therefore gives exactly

    d/dt E I_(u,a)(t)|_(t=0)
       =sum_delta [J_delta^N(u-a_delta)-J_delta^N(u)]_a. (2)

Incoming and outgoing routes are counted once, with their actual half-rate
normalization. At a homogeneous p, (1) reduces to

    J_delta(p)=F_delta(p)/2,

where F_delta=delta.F and F is equation(1) of the nonlinear-flux note.
Although this homogeneous current has zero divergence, its profile derivative
is nontrivial.

For the smooth profile, (1) is a polynomial in a fixed finite stencil of p.
Taylor expansion, including its first spatial derivative, gives uniformly

    J_delta^N(x)=F_delta(p(x))/2+N^-1 R_delta^N(x),
    sup_N ||R_delta^N||_(C^1) < infinity.            (3)

The symmetric k0 term is included in R; no large-scale diffusion term is
silently identified with zero at finite N. Bounds depend on the fixed
profile, k0 and gamma. Applying the finite difference in (2) to (3), and
Taylor expanding its first term once more, yields

    N sum_delta [J_delta^N(u-a_delta)-J_delta^N(u)]
      =-(1/2) sum_delta (a_delta.grad)F_delta(p(u/N))+O(N^-1).

Finally

    (1/2)sum_delta a_delta tensor delta
       =(1/2)sum_delta(delta-e_1) tensor delta=I.

Thus the exact microscopic initial expectation satisfies the uniform bound

    sup_(black u) |N [d/dt E I_u(t)]_(t=0)
                         +div F(p)(u/N)| <= C_p/N.  (4)

The constant is finite for the declared fixed smooth profile and rates. This
is a nonlinear, inhomogeneous **initial-derivative** result for the existing
local stochastic dynamics. It strengthens the connection between its exact
current and the candidate nonlinear conservation law without asserting a
finite-time hydrodynamic limit, preservation of local equilibrium, or shock
control. The finite-N k0 correction and all higher color moments remain
present in the exact formula (1).

## III. The smooth-time hydrodynamic theorem

**Status:** proposed conditional theorem with complete proof; author controls
and independent review pending. **Date:** 2026-09-21.

This extends the initial-derivative calculation to a fixed macroscopic time
interval on which a supplied strictly positive smooth solution exists. It
uses the existing stochastic permanent-color exchange law on a fixed winding
matching, not a new quantum Hamiltonian or a local-equilibrium assumption
imposed at later times. The inhomogeneous initial preparation is supplied;
the birth process and moving matching geometry are not part of this theorem.

### 1. Model, profile and conclusion

Let N>=8 be even, G_N the black sites in the N-periodic cubic lattice, and
K=|G_N|=N^3/2. The winding pairing sends black u to white u+e_1. A pair carries
one of the fourteen colors of DIMER_ROUTED_RECORD_TRANSPORT.md. Its permanent
key and color move together; the observable color process is the finite
Markov exchange process already specified there.

For delta in {+/-e_i} the route displacement is a_delta=delta-e_1.
The delta=+e_1 route is fixed. The other five have four distinct contexts
l=u-a_delta,u,w=u+a_delta,r=u+2a_delta. With
S_delta(a,b)=(gamma/2)delta.[e_a cross b_b+e_b cross b_a], their rates are

    r_(u,delta)=k0/2+
       [S(l,a)+S(a,r)-S(l,b)-S(b,r)]/4.

Fix k0>|gamma|, so every rate is at least r_*=(k0-|gamma|)/2>0.
The microscopic generator is L_N; the Euler-time process has generator
N L_N. Its homogeneous product law with any color probability p is invariant.
Indeed the swap reverses the bracketed h, and sum_u h_(u,delta)=0 on each
route cycle, by shifting its nearest and next-nearest S sums. In particular
the uniform product pi_N=14^-K is invariant.

Use the flux, entropy and complete moments from
DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md:

    F_a(p)=gamma p_a[e_a cross Y+X cross b_a-2X cross Y],
    eta(p)=sum_a p_a log p_a.

Suppose p(t,x) is a periodic C^3 solution on [0,T] times the unit three-torus
of partial_t p+div F(p)=0, with sum_a p_a=1 and p_a>=epsilon>0.
Bounds below may depend on this fixed solution, epsilon,T,k0,gamma.
Existence of such a solution is a hypothesis; global smooth existence,
shock selection and continuation to the simplex boundary are not claimed.

Let nu_N(t) be the product law with probabilities p(t,u/N), and mu_N(t) the
law of the actual Euler-time process. Suppose

    H(mu_N(0) | nu_N(0))=o(K).                       (1)

Then

    sup_(0<=t<=T) H(mu_N(t) | nu_N(t))/K -> 0.       (2)

For every fixed smooth test phi and color a, this implies the uniform-time
empirical limit, in probability,

    sup_(0<=t<=T) |K^-1 sum_(u in G_N) phi(u/N) I_(u,a)(t)
                           -integral phi(x)p_a(t,x) dx| -> 0. (3)

Neither (2) nor (3) says the full microscopic law is close to a product law
in total variation. Correlations may remain and the total entropy may grow.
The limits keep T and the smooth interior profile fixed.

### 2. Entropy dissipation and finite-block mixing

Write f_t=d mu_N(t)/d pi_N. For the bare exchange Dirichlet form use

    D_N(sqrt f)=(1/2) sum_(u,delta nonfixed)
           E_pi [sqrt(f(eta^uw))-sqrt(f(eta))]^2.

Stationarity of pi, the scalar inequality log z<=2(sqrt z-1), and r>=r_*
give

    d/dt H(mu_N(t)|pi_N) <= -2 N r_* D_N(sqrt f_t),
    integral_0^T D_N(sqrt f_t) dt <= K log14/(2 N r_*). (4)

The second inequality uses 0<=H(mu|pi)<=K log14 for any probability law
on this finite color space. It does not require the initial local-equilibrium
hypothesis. Zero probabilities can be treated by an arbitrarily small
positive admixture and a limit, or directly with the entropy dissipation
inequality.

A convenient block uses the three actual route generators

    g_0=-2e_1, g_1=e_2-e_1, g_2=e_3-e_1,
    B_ell={r_0 g_0+r_1 g_1+r_2 g_2:0<=r_i<ell}.

They generate the even-parity sublattice. For fixed ell and N>8ell these
blocks embed without wrapping identifications, contain m=ell^3 sites, and
have physical diameter O(ell). Their three internal nearest-generator
exchange families form a connected rectangular grid. For each fixed set
of fourteen color counts the uniform measure on block color arrangements
is invariant and irreducible under these bare swaps. Its Poincare gap is
positive. Taking the minimum over the finitely many nontrivial count
sectors defines g_ell>0. Constant sectors have zero variance and need no gap.

No uniform estimate on g_ell is assumed here. The argument first holds ell
fixed, sends N to infinity, and then sends ell to infinity. A quantitative
convergence rate would require more information.

For a bounded local block observable V with conditional count-sector mean
zero, Cauchy-Schwarz and the Poincare inequality give, after conditioning
on exterior colors and block counts,

    |E_mu V| <= 2||V||_infty sqrt(E_pi Var_B(sqrt f))
             <= 2||V||_infty g_ell^-1/2
                                      sqrt(E_pi D_B(sqrt f)). (5)

For clarity, the first inequality follows by writing f=(sqrt f)^2,
subtracting (E_B sqrt f)^2, whose pairing with V is zero, and using
E_B(sqrt f+E_B sqrt f)^2<=4 E_B f. Averaging exterior/count sectors and
Cauchy-Schwarz use E_pi f=1. The gap is applied in each sector to sqrt f.
This does not assume mu has conditionally uniform colors.

Each physical bare bond belongs to at most m translated blocks, up to a
fixed orientation-count constant. Summing (5) over all K translated blocks,
then integrating time and using (4), bounds the sum of block errors by

    C K sqrt(T m/(N g_ell)) = K C_(ell,T)/sqrt N.     (6)

All block comparisons use swaps actually present in the process. Their
contexts may extend outside the block; the uniform lower rate bound in
(4) makes that harmless.

### 3. One-block replacement of the current

Let j_delta(u)=r_(u,delta)(I_u-I_(u+a_delta)), a fourteen-vector outgoing
current. It is bounded and depends on the four distinct sites above. Its
homogeneous product expectation is exactly F_delta(p)/2.

For each block average these currents over anchors whose whole stencil is
inside the block. The excluded fraction is O(1/ell). This follows because
the five displacements are g_0,g_1,g_2,g_0-g_1,g_0-g_2, and the stencil
uses at most two such steps. The current average remains uniformly bounded.

Conditional on the block color counts, any four distinct block positions
have the law of four draws without replacement from that multiset.
Couple these with four draws with replacement. The coupling fails only
when sampled indices repeat, with probability at most 6/m. Therefore,
uniformly over every count vector, including boundary color densities,

    |E_count j_delta - F_delta(pbar)/2| <= C/m.     (7)

The normalized block average has the same estimate, plus O(1/ell) if
normalized by all m anchors instead of the number with internal stencils.
There is no assumption that the actual block law is a product law.

Apply (5)-(7), average translated blocks, and move a fixed smooth test
coefficient from each anchor to its block anchor. The coefficient error is
O(ell/N). Thus for any fixed smooth bounded vector coefficient b(t,x),

    integral_0^t sum_u b(s,u/N).j_delta(u,s) ds
      = integral_0^t sum_u b(s,u/N).F_delta(pbar_u(s))/2 ds
        + R_(N,ell)(t),                             (8)

as an equality of expectations under mu, with

    sup_(t<=T) |R_(N,ell)(t)|/K
       <= C_T(1/ell+1/m+ell/N)+C_(ell,T)/sqrt N.    (9)

Here pbar_u is the empirical probability in u+B_ell. Averaging preserves
the full sum up to the same boundary and smooth-coefficient errors.
The proof also permits replacing a single-site indicator by its block
average in a smooth weighted sum, with error at most C K ell/N.

### 4. Relative entropy and the cancellation of first-order terms

Put theta_a=log p_a and h_N(t)=H(mu_N(t)|nu_N(t)).
Since log(d nu_N/d pi_N)=sum_u theta_(I_u)(t,u/N)+K log14, differentiation
and the first inequality in (4), with its negative term dropped, yield

    h_N'(t) <= -N E_mu L_N sum_u theta_(I_u)(t,u/N)
                         -E_mu sum_u partial_t theta(t,u/N).I_u.
                                                               (10)

For an exchange u to w, the log-density difference is
[theta(w/N)-theta(u/N)].(I_u-I_w). Taylor expanding only the smooth
coefficient, with bounded rates and K channels, gives

    h_N'(t) <= -E_mu sum_(u,delta)
          [(a_delta.grad)theta](t,u/N).j_delta(u)
                  -E_mu sum_u theta_t(t,u/N).I_u + O(K/N).       (11)

This uses the exact generator. It neither expands the random color field
nor imposes a time-dependent product law on that process.

After time integration, apply (8) and the indicator replacement. The tensor
identity (1/2)sum_delta a_delta tensor delta=I reduces the first term to

    -sum_u {sum_j partial_j theta(t,u/N).F_j(pbar_u)
                                  +theta_t(t,u/N).pbar_u}.      (12)

Taylor-expand the polynomial F about the deterministic profile p(t,u/N).
The constant term theta_t.p is zero pointwise. The remaining spatial
constant sum is O(K/N): its continuum integrand is a divergence because

    partial_j theta.F_j = partial_j(theta.F_j-q_(eta,j)),

where the entropy flux q_eta is the one derived in the nonlinear-flux note.
The periodic integral vanishes, and the black-sublattice Riemann-sum error
is O(K/N) for these fixed smooth functions.

The terms linear in pbar-p vanish on the simplex tangent. Indeed the
entropy symmetrizer H_eta=diag(1/p) satisfies symmetry of H_eta DF_j on
that tangent. Together with p_t=-sum_j DF_j(p) partial_j p this gives

    [theta_t+sum_j DF_j(p)^T partial_j theta].(pbar-p)=0.          (13)

The equality is a tangent-space statement; an irrelevant vector proportional
to the all-ones vector need not vanish in the ambient coordinates.
The remaining terms in (12) have absolute value at most

    C sum_u |pbar_u-p(t,u/N)|^2.                                  (14)

This uses bounded second derivatives of the cubic flux and fixed bounded
theta derivatives. Block empirical probabilities may touch the boundary;
only the deterministic profile must stay in the interior.

### 5. Product exponential bound and Gronwall

A direct product-law estimate closes (14). Under nu_N(t), write
qbar_u=E_nu pbar_u. Smoothness gives |qbar_u-p(t,u/N)|<=C ell/N.
For m independent, possibly nonidentical fourteen-color variables,
coordinate Hoeffding bounds and a union bound imply

    P(m |pbar-qbar|^2>s) <= 28 exp(-s/7),
    E exp[(m/14)|pbar-qbar|^2] <= 29.                             (15)

The second formula follows by integrating the first tail bound; it is
uniform in the deterministic probability profile. An elementary proof of
the coordinate Hoeffding bound follows from the Bernoulli exponential
moment bound E exp[t(X-E X)]<=exp(t^2/8) and independence.

The overlap graph of translated B_ell blocks has degree at most
(2ell-1)^3-1, so it admits a coloring with chi=8m colors, allowing empty
classes. Blocks in a color class are disjoint and independent under nu.
Holder's inequality over these chi classes, (15), and
|pbar-p|^2<=2|pbar-qbar|^2+2|qbar-p|^2 give, for alpha=1/224,

    log E_nu exp[alpha sum_u |pbar_u-p(t,u/N)|^2]
       <= K log29/(8m) + C alpha K ell^2/N^2.                    (16)

Indeed 2 alpha chi/m=1/14. This argument uses a coloring, not an assumed
exact tiling of the finite winding torus.

The entropy inequality applied to (16) gives

    E_mu sum_u |pbar_u-p(t,u/N)|^2
       <= h_N(t)/alpha + K log29/(8m alpha)+C K ell^2/N^2.        (17)

Combining (9)-(14) and (17), uniformly for t<=T,

    h_N(t)/K <= h_N(0)/K + C integral_0^t h_N(s)/K ds
         + C_T(1/ell+1/m+ell/N+ell^2/N^2+1/N)
         + C_(ell,T)/sqrt N.                                    (18)

Gronwall first with fixed ell, followed by limsup_(N->infinity), (1),
and then ell->infinity proves (2). No choice of ell depending on an
unproved spectral-gap rate is required. This is a qualitative smooth-time
hydrodynamic theorem; the constants in the finite-block step may grow
rapidly with ell.

### 6. Empirical convergence and limits of the result

At any fixed time, a bounded weighted empirical color average under nu_N
has exponentially small probability, exp(-c K), of a fixed nonzero deviation
from its deterministic mean. This follows from the same independent
Bernoulli exponential bound, with the bounded test weights. The entropy
event inequality

    mu(A) <= [H(mu|nu)+log2]/log(1/nu(A))

and (2) prove convergence in probability at each fixed time. Its deterministic
mean is the black-lattice Riemann sum of phi p, which converges to the integral.

For a smooth test phi, one exchange changes the empirical average by at most
C/(N K), since it moves a color only a fixed microscopic distance. There are
O(K) bounded-rate channels and the Euler generator multiplies rates by N.
Its martingale quadratic variation on [0,T] is at most C_T/(N K); its drift
is uniformly bounded by C. Doob's inequality makes the martingale uniformly
small. A finite time mesh, the bounded drift and continuity of the target
profile upgrade fixed-time convergence to (3).

The result proves finite-amplitude nonlinear evolution only while the
stipulated solution remains smooth and strictly positive, on a fixed winding
matching with the supplied inhomogeneous preparation. It does not prove
preparation by record births, coupled moving-geometry hydrodynamics, behavior
through shocks, quantum dynamics, a spacetime metric or a TOE. It does
establish that the candidate nonlinear flux can govern the existing
permanent-color stochastic process over an entire such time interval,
rather than just its initial derivative.

## Verification and remaining physics

[The evidence packet](../.claude/science/mobile-record-smooth-nonlinear-euler-20260921/README.md) preserves three complete source
arguments, the unchanged transport dependency, seven author mathematical
groups and two completed selective independent reconstructions. Three
mutations target the nonlinear flux, entropy-flux correction and exponential
block bound. The proofs supply the all-volume conclusions; finite checks
test their load-bearing steps and counterexamples.

The entropy method has established antecedents, including Toth and Valko's
[one-dimensional systems with several conservation laws](https://arxiv.org/abs/math/0210426).
That abstract supplies methodological context. No theorem from that work is
imported into this three-dimensional proof; the required block geometry,
conditional centering, current replacement and exponential estimate are
proved here.

The smooth-time theorem uses finite-sector irreducibility at fixed block
size and takes N to infinity before the block size grows. It asserts no
numerical convergence rate. Its initial-drift O(1/N) estimate is a separate
Taylor bound. The initial author's finite-N threshold failure and the narrow
grid extension remain in the independent source history.

Smooth existence is an explicit hypothesis. Birth preparation of a spatially
varying profile, coupled moving-geometry nonlinear evolution, shock selection,
quantum dynamics, matter, gravity and empirical identification remain open.
The homogeneous birth preparation and earlier linear waves cannot supply
these missing conclusions by composition.
