# Two-time dynamics and the missing Gaussian-moment input

Author: openai/gpt-6-astra/max macbook-codex, 2026-11-01.
Pinned source: 45b3989670a64c7d0ce7b293a56ed6beb37dee14.
Status: implications with named premises; discharged elementary covariance
counterexample. No numerical job, independent review or audit.
Sources: witness Theorems 4.1, 4.3 and upper-chain Text 10 at the pinned commit.
The OS reconstruction is a named hypothesis, not a lemma imported from a paper.

## 1. Theorem 4.1 [implication, proof discharged under H-NET]

Assume H-NET in witness Text 8.1. Let A,B be real bounded members of its
family. Suppose the two configurations (A,tau_x B) and
(A,tau_(x+t e4) B), t>0, have supports strictly ordered along every axis,
and their limiting connected correlators c(x),c(x+t e4) differ.

Choose a time plane in the first positive gap. The same plane separates
the supports for every added displacement s e4, 0<=s<=t. After translating
that plane to zero, A lies on its negative side and tau_x B on its positive
side. Reflect A and mollify it and the translated B with nonnegative,
unit-integral mollifiers of sufficiently small support. Call the resulting
positive-time objects F_epsilon,G_epsilon. H-NET gives

    S(Theta F_epsilon tau_(s e4) G_epsilon)
      -S(Theta F_epsilon)S(G_epsilon)
      = <[F_epsilon]_perp, exp(-sH)[G_epsilon]_perp>.          (1)

For real observables reflection invariance identifies the subtracted
one-point functions with those defining the centred OS vectors. If
H vanishes on Omega-perp, (1) is independent of s. The mollified connected
correlator is an average of c(y+s e4) over displacements y close to x.
Ordered-configuration local uniform convergence/continuity in H-NET
therefore lets epsilon decrease to zero at s=0 and s=t, giving
c(x)=c(x+t e4), a contradiction. Thus H does not vanish on Omega-perp.

The ordering condition ensures every mollifier used here stays inside the
same admissible separated region. No product of point fields is assumed.
This proves the stated implication; it proves neither H-NET nor the two
unequal values for the Wilson trajectory.

For the continuum Maxwell coefficients used in Corollary 4.2,
P(x)=3/(500 pi^2 d^4), P(x')=11/(3375 pi^2 d^4), hence
P(x)^2/P(x')^2=(81/44)^2=6561/1936>3. Relative errors at most 1/2 in
both positive covariance values still give unequal values, because
(1/2)P(x)^2>(3/2)P(x')^2. Applying this to actual blocked coefficients
requires their controlled far-field approximation; this arithmetic does
not establish that approximation.

## 2. A precise restricted version of 4.3 [implication]

The raw wording "a polynomial of bounded degree in psi_p/g" must specify
frames and degree. Here the fluxes are transported to one fixed base point,
and P is invariant under the common adjoint SO(3), of degree <=8. This is
the class needed for the energies and B in candidate NT2. It does not claim
convergence of all gauge-variant colour components or arbitrary degrees.

Here is one exact interpretation of the norm/closure hypotheses H-G0 and
H-LIFT. Index transported plaquette flux components by (p,a), where p
includes the specified transport tail. In (2), dist(p,o) means the maximum
distance from o of the entire plaquette-and-tail support. Expand P
using symmetric coefficient tensors, with a fixed monomial convention, and
put

    ||P||_(8,alpha) = sum_(n=0)^8 sum_(p1,a1,...,pn,an)
       |c_(p1 a1...pn an)| exp(alpha max_l dist(p_l,o)),         (2)

with the maximum zero for the constant term. Finite templates have finite
norm; exponentially summable extensions are its completion. Distances are
in the level's coarse lattice. Different fixed tails specifying a template
are part of its label and of the required kernel estimates, not silently
changed by a gauge transformation. Uniform flux moments bound expectations
of a norm-one polynomial by Holder and the coefficient sum.

Let A_j be a colour-equivariant linear lift. Let b_j be centred Gaussian,
independent of the coarse Gaussian, with covariance Gamma_j^fib. Require

    Gamma_j=Gamma_j^fib+A_j Gamma_(j+1) A_j^T,
    Q_j P(z):=E_b P(A_j z+b),
    ||[Q_j P]_(degree>=2)||_(8,alpha) <= q_0 ||P||_(8,alpha),
                       q_0<1, uniformly in j.                (3)

This is a hypothesis about the actual transfer operator in a stated norm.
It is NOT derived here from |psi(V^*)|<=C_s L^(-kappa) sup|psi(W)|.
Since Q_j preserves common-colour invariance, its degree-one part is zero:
an invariant linear form on copies of R^3 would have coefficient vectors
fixed by every SO(3) rotation, and each such vector is zero.

Assume (G0), H-MOM, H-TREE and H-FLOW as stated in Text 8.1, with (2)-(3)
as the precise norm reading. Set s_j=gamma_(j+1)/gamma_j. H-FLOW implies
s_j=1+O(gamma_j^2). Replacing A_j by s_j A_j multiplies each degree-k
coarse coefficient by s_j^k. Thus (3) has factor at most
q_0 max(1,s_j^8)<=q<1, for all sufficiently ultraviolet levels.

Define

    e_j=sup_(||P||<=1) |E_mu_j P(Z_j)-E_Gamma_j P|,
    Z_j=psi_j/gamma_j.

These numbers are uniformly finite under H-MOM and H-TREE. Constants cancel
in e_j. The expectation of a degree-one invariant polynomial vanishes as
just proved. The one-step inequality (G0), the Gaussian identity in (3),
and addition/subtraction of E_Gamma_(j+1) E_b P(s_j A_j Z+b) give

    e_j <= q e_(j+1)+delta_8(gamma_j)+C|s_j-1|+eta_bad(gamma_j),
                   eta_bad(g)->0.                            (4)

For the last error: for a fixed window, the event G^c costs at most
C R(g)^4 gamma_(j+1)^N by Markov and H-MOM, for arbitrary N, with
R(g)=C log(1/g). Cauchy–Schwarz and higher moments bound its contribution
to a norm-one polynomial. The Gaussian surrogate has the same moment
control using (3) and H-TREE. For summable kernels first truncate at that
radius; the remaining expectation is bounded by C exp(-alpha R) from
(2) and the moments. This is also why the hypothesis is needed on the
completed class, not merely on polynomials of fixed finite support.

Put delta(g)=delta_8(g)+C g^2+eta_bad(g). In UV indexing m, iteration gives

    e_m <= q^(m-m_0) C_top
           +sum_(ell=0)^(m-m_0-1) q^ell delta(gamma_(m-ell)).   (5)

Choose a finite tail cutoff N so that the bounded geometric tail is small;
for ell<N, gamma_(m-ell)->0, so each error tends to zero. Hence e_m->0.
The bound is uniform in the cutoff and volume only because ALL the stated
hypotheses were uniform. No limit exchanges beyond the named H-SCALE and
H-TREE are being supplied by this argument.

Taylor expansion s_p=|psi_p|^2/8+O(|psi_p|^4), followed by H-MOM, yields

    Cov(s_p,s_q)/gamma_m^4 -> (3/2)P_pq^2,
    E prod_(l=1)^k s_pl/gamma_m^(2k) -> C_(p1,...,pk), k<=4.

For Gaussian moments use E[X_i f(X)]=sum_j C_ij E[partial_j f(X)],
proved by integration by parts against its Gaussian density; induction on
the polynomial degree gives the pairing rule. Thus
Cov(|Z_p|^2,|Z_q|^2)
=2 sum_(a,b)(4P_pq delta_ab)^2=96 P_pq^2; dividing by 64 gives 3/2.
For a general fixed closed lattice path, its holonomy is a finite product
of plaquette holonomies transported to its base point. One elementary
construction swaps neighbouring steps in different coordinate directions,
each swap inserting the corresponding plaquette conjugated by the prefix;
backtracking steps cancel. Sorting the coordinate directions of a closed
word reduces it to the empty word after finitely many such moves. Thus the
product identity uses finitely many plaquettes and specified finite tails.
Expanding this product near their identity matrices gives a linear sum of
transported fluxes plus terms of degree at least two. The leading energy
and B terms are therefore invariant polynomials in the stated class.
Their Taylor remainders are controlled by the higher moments in H-MOM;
the event outside a fixed small chart is negligible to any required power
by Markov. This extends the energy-product conclusion to every fixed path
template, with constants depending on that template.

The analogous expansion of B gives its leading coefficient. The anchor
then gives g_m/gamma_m->1. This proves a RESTRICTED conditional replacement
for 4.3 under (G0) and (3), not 4.3 from its old listed source clauses.
For T it gives only E T=o(gamma_m^3), which is insufficient for NT2's
gamma_m^4 coefficient. No first-order cubic result follows from (5) alone.

## 3. Why the original covariance clause does not give (G0) [discharged example]

For 0<a<1/2 consider the two scalar covariance matrices

    Sigma_+ = [[1,a,a],[a,1,a],[a,a,1]],
    Sigma_- = [[1,a,a],[a,1,-a],[a,-a,1]].

For either sign v^T Sigma v >=(1-2a) sum_i v_i^2>0, since
2|v_i v_j|<=v_i^2+v_j^2. Let X_1,X_2,X_3 be three colour vectors with
Cov(X_i^b,X_j^c)=(Sigma_+ or Sigma_-)_ij delta_bc. Both laws are invariant
under the common colour rotations. All diagonal block traces are 3 and
all off-diagonal block Hilbert–Schmidt norms are sqrt(3)a. These are exactly
the data controlled by upper-chain OS_j(d).

Nevertheless Wick expansion gives, for colour dimension n,

    E |X_1|^2 |X_2|^2 |X_3|^2
      =n^3+2n^2(s_12^2+s_23^2+s_31^2)+8n s_12 s_23 s_31.    (6)

To check the count: pairings with no links between the three squared
factors give n^3; a double edge between a chosen pair gives 2n^2 s_ij^2;
a three-cycle has eight pairings and one colour sum, giving 8n times the
product. Those exhaust the pairings. At n=3 the two answers are
27+54a^2+24a^3 and 27+54a^2-24a^3, different by 48a^3.
This is a scalar invariant polynomial of degree six, inside the degree-eight
range of OS_j(c); it is not a gauge-variant counterexample.

Thus equal traces and pairwise block norms do not determine the needed
Gaussian moments. One could define a covariance to be Sigma_+ at flat W
and Sigma_- at every nonflat W while satisfying those particular norm and
trace bounds with zero error. This last observation concerns the displayed
bounds only, not an assertion that such a covariance is a Wilson Hessian
or satisfies all smoothness properties a producer may eventually prove.

An exact sufficient additional inequality in a COMMON frame is

    E_mu[1_G | E_(N(0,Gamma(W^pi))) P(phi+b)
                  -E_(N(0,Gamma(1))) P(phi+b) |]
         <= epsilon_8(gamma_j)||P||_(8,alpha),
         epsilon_8(g)->0,    deg P<=8.                        (COV8)

A weighted full-matrix continuity bound plus suitable high moments could
supply it. Pairwise HS-norm and trace continuity cannot do so. This is a
missing input to (G0), not a proof that the true Wilson covariance fails it.

There is also a framing issue if the original theorem is read literally:
for plaquette logarithms based at different vertices, independent local
gauge rotations force E psi_p^a psi_q^b=0 at distinct base points. A
nonzero unframed 4P_pq delta_ab cannot be that expectation. Specifying
parallel transport and restricting to invariant polynomials avoids that
mistake; it does not supply (COV8).

## 4. Honest stop

The first unresolved source-to-consumer step for repaired 4.3 is (G0),
specifically (COV8), (TV-P), and the completed-class contraction (3).
The old OS_j(d) fails to determine even the degree-six moment (6).
Additional hypotheses were made visible, not proved for either attempt.
The stronger first-order version for T and its uniform cubic recursion
are not reached. The NT2 implication from the original source clauses,
its actual realization by a Wilson limit, and T1 remain open.
