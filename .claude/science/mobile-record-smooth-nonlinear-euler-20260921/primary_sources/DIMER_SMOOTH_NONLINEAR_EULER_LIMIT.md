# Smooth nonlinear Euler evolution for the actual routed color process

**Status:** proposed conditional theorem with complete proof; author controls
and independent review pending. **Date:** 2026-09-21.

This extends the initial-derivative calculation to a fixed macroscopic time
interval on which a supplied strictly positive smooth solution exists. It
uses the existing stochastic permanent-color exchange law on a fixed winding
matching, not a new quantum Hamiltonian or a local-equilibrium assumption
imposed at later times. The inhomogeneous initial preparation is supplied;
the birth process and moving matching geometry are not part of this theorem.

## 1. Model, profile and conclusion

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

## 2. Entropy dissipation and finite-block mixing

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

## 3. One-block replacement of the current

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

## 4. Relative entropy and the cancellation of first-order terms

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

## 5. Product exponential bound and Gronwall

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

## 6. Empirical convergence and limits of the result

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

