---
claim_id: excluded_walk_projected_free_band_canonical_current_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
runner: scripts/excluded_walk_projected_free_band_canonical_current_2026_10_11.py
claim_scope: "For the supplied antisymmetric excluded Weyl pair and canonical compressed energy placement, construct a normalized projection of an actual positive free-band packet with a finite signed current response at the explicit two-scale choice delta=2^-68 lambda^2."
upstream_dependencies:
  - excluded_walk_low_energy_energy_current_bounded_theorem_note_2026-10-11
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: "Construct controlled links from microscopic dynamics to macroscopic transport."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Determine controlled current evolution beyond this specified projected-band preparation before using it in a macroscopic transport argument."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Explicit long-time canonical-current response from projected free-band preparation

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit
has not occurred. This note composes selectively checked supplied-model
arguments. Its full source-bound publication check is recorded in the milestone
review history, with the reviewer’s prior authorship and exact scope explicit.

The walk, continuous generator clock, antisymmetric pair sector, contact
exclusion, coordinates and canonical local-energy placement are supplied
premises. This result supports the microscopic-current route toward controlled
macroscopic transport. It derives no physical encounter clock or kinetic law.
The state is prepared by projecting an actual free positive-band packet at
time zero and normalizing once on the whole direct integral.

For every 0<lambda<=1/16, the construction below gives a normalized projection
of an actual free [lambda,2lambda] positive-band packet. Set

    delta=2^-68 lambda^2,   tau0=1/20,
    physical time t=tau0/delta=2^68/(20lambda^2).           (Q1)

All three actual canonical energy-current components then obey

    Delta <J_a> <= -delta A_lambda^2/43200
                <= -2^-68 lambda^3/(388800pi^2), a=1,2,3. (Q2)

The factor A_lambda and every preparation normalization are defined below.
The total-momentum packet has center delta(1,1,1) and a strictly positive
specified three-dimensional width. The numerical constants are conservative;
no claim of an optimal exponent, constant or physical onset scale is made.

Here Delta <J_a> means

    <exp(-it H_D)Chi,J_a exp(-it H_D)Chi>-<Chi,J_a Chi>.

The decomposable H_D, bounded canonical J_a, unit free packet and globally
normalized physical Chi are specified below. The statement is for this
constructed family at the single displayed finite time, in supplied clock
units; it is not a monotonicity or arbitrary-preparation assertion.

## 1. Contract and proof organization

The [parent low-energy walk theorem](EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md),
SHA-256 `9f551fc8d3592e83d15a007495a8f9165a5ddb9bc1e98d9dd3f51b6a2584f401`,
fixes the supplied walk and selected additive symmetric energy placement.
Its canonical-current argument is reproduced in Section 5. The present proof
requires none of the parent's stationary-scattering or Cook-regularity inputs.
The supplied-walk and canonical-placement contract remains an explicit
upstream dependency; the parent's proposed status is not promoted by this
composition.

All relative-torus and local total-momentum integrals use dq/(2pi)^3 and
dK/(2pi)^3, respectively. The fixed local chart is K=k_1+k_2,
q=(k_1-k_2)/2. Inner products are linear in their second argument. Even
singlet and odd triplet coefficients implement pair antisymmetry. No extra
exchange or half-torus factor is inserted.

The argument is finite throughout: classify the entire physical zero space,
control the two cutoff inverses, compare the transverse evolution, retain its
small dressing amplitude in the actual-current trace, and transfer the signed
bound to one globally normalized packet of actual free-band preparations.
Every estimate needed for the explicit onset is proved below. The frozen
research sources supply provenance, not substitute proofs.

The source-composition map records exact input hashes, retained argument
ranges, every editorial change, and the separate leakage and nonuniformity
results preserved as research. Those separate results are not premises of
the signed-current theorem. No new literature theorem or physical primitive
is introduced by this publication composition.

## 2. Fixed physical space and estimates available without a spectral gap

On each physical fiber let c be the constant normalized singlet and

    H0(K,q)=sigma_1.sin(K/2+q)+sigma_2.sin(K/2-q),
    C=|c><c|, P=I-C, H_D(K)=P H0(K)P restricted to ran P.

Only bounded operators act on the singular dressing vector below.

Write s(q)=sin q, epsilon(q)=|s(q)| and n(q)=s(q)/epsilon(q) off the cone
points; let T_j=sigma_(1,j)c. The three T_j are an orthonormal Cartesian triplet
basis. In singlet/triplet coordinates the supplied free symbol at K=0 is

    H0(0,q) = [ 0       2s(q)^T ]
              [ 2s(q)  0_(3x3) ].                         (L1)

The antisymmetric fiber has an even singlet coefficient and odd triplet
coefficients under q -> -q. The vectors below have those parities. At
almost every q the free kernel consists of transverse triplets u with
s·u=0. The two remaining energies are +/-2epsilon. Values at the eight
cone points can be chosen arbitrarily because they have measure zero.

Define

    I0 = integral dq/[4epsilon(q)^2],
    zeta(q) = [s(q)·T]/[2epsilon(q)^2 sqrt(I0)].            (L2)

Near each cone the squared norm has an integrable 1/|q|^2 singularity in
three dimensions. Therefore I0 is finite and zeta is a normalized vector.
It is orthogonal to c pointwise and orthogonal to every free transverse
zero mode. Direct multiplication gives

    H0(0) zeta = c/sqrt(I0),
    H_D(0) zeta = P H0(0) P zeta = 0.                    (L3)

Thus the notation H0^{-1}c is valid only as the reduced inverse on the
orthogonal complement of the free kernel, evaluated on this particular
vector c. H0 has no bounded inverse on the whole fiber.

This is the entire additional physical zero space. If psi belongs to P
and H_D(0)psi=0, then H0(0)psi=alpha c for some scalar alpha. Subtract
alpha sqrt(I0) zeta and obtain a free-kernel vector. Conversely every such
vector lies in P and is killed by H_D(0). Consequently

    ker H_D(0)|_P = ker H0(0) direct-sum span{zeta}.        (L4)

Write H_*=H_D(0). Let F be the pointwise transverse-triplet projection,
with zero singlet block, and define on the physical space

    Pi=F+|zeta><zeta|, Q=P-Pi,
    E_sigma=1_(0<|H_*|<=sigma)(H_*).                       (Q3)

The full extension P H0 P also has the auxiliary vector c. It must not be
counted as a physical state. Neither the free flat band nor the dispersive
energies approaching zero leave a spectral gap around zero. An isolated
finite-multiplicity eigenvalue perturbation theorem is inapplicable.

For later explicit estimates, changing variables u=sin q in the eight
charts gives, for 0<r<=1/2,

    integral_(epsilon<r) epsilon^-2 dq <= r,
    integral_(epsilon<r) dq <= r^3/3,
    integral_(epsilon>=r) epsilon^-4 dq <= 9/r,
    integral epsilon^2=3/2,  1/12 <= I0 <= 9/8.          (Q4)

Indeed the radial coefficient is at most
4/[pi^2(1-r^2)^(3/2)] <=32/(3sqrt(3)pi^2)<1. The first
two inequalities follow by radial integration. For the third, integrate
u^-2 from r to 1/2 with that coefficient and bound the remaining integrand
by 16; 1/r+16<=9/r. The last bound uses epsilon^2<=3, the first inequality
at r=1/2, and epsilon^-2<=4 outside that region.

The identity integral epsilon^2=3/2 follows by summing the three
normalized sin-squared integrals.

For fixed kappa put b=|kappa|, d_j=kappa_j cos q_j and

    B_kappa u=i d cross u, B_kappa kills the singlet,
    H_D(delta kappa)/delta=H_*/delta+B_kappa+R_delta,
    ||R_delta||<=r_delta=delta b^2/4+delta^2 b^3/24,
    A_kappa=Pi B_kappa Pi, U_delta(tau)=exp[-i tau H_D(delta kappa)/delta].
                                                               (Q5)

The exact free
singlet/triplet block at K=delta kappa is

    [ 0                         2(a_delta*s)^T ]
    [ 2(a_delta*s)              i b_delta cross ],

    (a_delta)_j=cos(delta kappa_j/2),
    (b_delta)_j=2sin(delta kappa_j/2)cos q_j.                  (D3)

The sign follows directly from
(sigma_(1,l)+sigma_(2,l))T_j=2i epsilon_(ljk) T_k.
Consequently the bounded self-adjoint derivative B_kappa has zero
singlet block and triplet action

    B_kappa u=i d cross u,       d_j=kappa_j cos q_j,
    ||B_kappa||<=b.                                           (D4)

It annihilates c and preserves P. The inequalities
|cos x-1|<=x^2/2 and |sin x-x|<=|x|^3/6 give

    H_D(delta kappa)/delta=H_*/delta+B_kappa+R_delta,
    ||R_delta||<=r_delta:=delta b^2/4+delta^2 b^3/24.      (D5)

Indeed the singlet-triplet remainder before division by delta has norm
at most delta^2 b^2/4; the triplet remainder has norm at most
delta^3 b^3/24. Compression cannot enlarge either norm.

The effective orbit from zeta has coordinates

    exp(-i tau A_kappa)zeta=u(tau)+alpha(tau)zeta,
    i u'=D_kappa u+alpha g_kappa, u(0)=0,
    D_kappa u=i(d.n)n cross u,
    g_kappa=i(d cross n)/(2epsilon sqrt(I0)).             (Q6)

To verify the transverse block, for any transverse u,
(I-nn^T)(d cross u)=(d·n)n cross u. B_kappa zeta is already
transverse, and <zeta,B_kappa zeta>=0 pointwise. This proves both
off-diagonal entries and their signs. The parities are preserved.
The vector g_kappa is in L2 and ||A_kappa||<=b, because A_kappa is a
compression of the bounded D4. No inverse Hamiltonian or derivative
of zeta is being used. The equations act on the entire physical zero
space ran Pi:

    i partial_tau u=D_kappa u+alpha g_kappa,
    i partial_tau alpha=<g_kappa,u>.                          (D7)

Dropping g_kappa would discard the physical threshold dressing's coupling
to the free flat band. It is not a consistent reduction of this generator.

The orbit exp(-i tau A_kappa)zeta has norm one, with alpha(0)=1, so
|alpha|<=1. The multiplication operator D_kappa(q) is
Hermitian on the transverse plane at almost every q. Its pointwise exponential
is unitary. The bounded-operator variation-of-constants formula therefore
also has the following almost-everywhere representative for either sign of
tau:

    |u(tau,q)|<=|tau| |g_kappa(q)|
              <=T b/(2epsilon(q)sqrt(I0)), |tau|<=T.      (Q7)

No spatial derivative of zeta or uniform pointwise bound at a cone is used.

## 3. Quantifying the low nonzero spectral mass of the dressing orbit

Because B_kappa zeta=g_kappa is transverse, the longitudinal part of
Q B_kappa exp(-i tau A_kappa)zeta comes entirely from B_kappa u. Put

    f_raw(q)=n(q).B_kappa u(q), beta(tau)=<zeta,B_kappa u>,
    f(q)=f_raw(q)-beta(tau)/(2epsilon(q)sqrt(I0)).

Then exactly

    Q B_kappa exp(-i tau A_kappa)zeta=f(q)n(q),
    integral f/(2epsilon)=0,
    |f(q)|<=L/epsilon(q), L=b^2 T/sqrt(I0).              (Q8)

To check the constant, Q7 bounds f_raw by b^2T/(2epsilon sqrt(I0)).
Also ||u(tau)||<=T||g_kappa||<=Tb, so |beta|<=b||u||<=Tb^2.
The removed zeta component costs another equal half in the pointwise bound.
The orthogonality of Q to zeta gives the integral identity. It is legitimate
as an ordinary integral because epsilon^-2 is integrable. Both f and its
formal singlet inverse are exchange even.

Let y=f n. The formal inverse f/(2epsilon) has zero mean but need not be
in L2. For 0<r<=1/2 define the allowed singlet vector

    xi_r=P[(f/(2epsilon))1_(epsilon>=r)c],
    m_r=integral (f/(2epsilon))1_(epsilon>=r)
        =-integral (f/(2epsilon))1_(epsilon<r).           (Q9)

Here P subtracts the constant singlet mean. Its contribution cannot be
omitted. Since H_* maps an allowed singlet coefficient h to 2epsilon h n,

    H_*xi_r-y=[-f1_(epsilon<r)-2epsilon m_r]n,
    |m_r|<=Lr/2,
    ||H_*xi_r-y||<=L[sqrt(r)+sqrt(3/2)r]<=2Lsqrt(r),
    ||xi_r||<=3L/(2sqrt(r)).                             (Q10)

The residual bounds use Q4 and |f|<=L/epsilon. The last norm bound uses
that P is an orthogonal contraction before applying the epsilon^-4 bound.
The second residual inequality holds because r<=1/2<2/3.

The spectral theorem, with the zero eigenspace explicitly omitted, gives

    ||E_sigma y||<=||H_*xi_r-y||+sigma||xi_r||.

Set r=sigma<=1/2. Since E_sigma annihilates Pi, Q8-Q10 prove the uniform
bound needed in the finite zero-space comparison below:

    M_zeta(sigma,T):=sup_(|tau|<=T)
             ||E_sigma B_kappa exp(-i tau A_kappa)zeta||
        <=(7/2) b^2 T sqrt(sigma)/sqrt(I0).              (Q11)

This is a special-vector estimate. Q7 used u(0)=0; no uniform estimate over
the zero-space unit ball is asserted.

## 4. The projected band and its complementary spectral estimate

At K=0 the positive contact spectral density for 0<E<2 is

    rho(0,E)=E^2/(16pi^3) integral_(S^2)
                 product_j (1-E^2 n_j^2/4)^(-1/2) dOmega. (L6)

The positive eigenvector of L1 is (c+n·T)/sqrt(2), with eigenvalue
E=2epsilon and contact weight 1/2. The eight sin-coordinate charts,
followed by this radial energy change, give L6 directly. No
limiting-absorption theorem is needed. In particular

    E^2/(4pi^2) <= rho(0,E)
       <= E^2/[4pi^2(1-E^2/4)^(3/2)].                    (L7)

For any positive spectral interval I, the squared norm of the free-band
part of zeta is

    w_I = ||1_I(H0)zeta||^2
        = I0^-1 integral_I rho(0,E)/E^2 dE.              (L8)

Set a=5/4 and, for 0<lambda<=1/16, define

    Gamma_lambda=1_[5lambda/4,7lambda/4](H0(0)),
    w_lambda=||Gamma_lambda zeta||^2,
    phi_lambda=Gamma_lambda zeta/sqrt(w_lambda),
    beta_lambda=<c,phi_lambda>, n_lambda=sqrt(1-beta_lambda^2),
    chi_lambda=P phi_lambda/n_lambda,
    A_lambda=<zeta,chi_lambda>=sqrt(w_lambda)/n_lambda.     (Q12)

The reduced-inverse relation H0(0)zeta=c/sqrt(I0) on the dispersive
subspace gives

    beta_lambda=(I0 w_lambda)^(-1/2)
                         integral_[5lambda/4,7lambda/4] rho(0,E)/E dE>0.

Thus the displayed real square root for n_lambda has the stated phase
convention. The positive band contains only singlet and longitudinal triplet
components; its contact projection introduces no transverse component.

All are explicit through the given spectral interval. In particular
F chi_lambda=0 and Pi chi_lambda=A_lambda zeta. The exact contact
spectral density and volume bound above imply

    n_lambda>=1/2, 0<=beta_lambda<=1/2,
    sqrt(lambda)/(3pi)<=A_lambda<=2sqrt(lambda),
    A_lambda<=1, A_lambda^2>=lambda/(9pi^2).              (Q13)

For explicit bounds on the entire stated range, the q support has
volume at most lambda^3/3 by Q4, so Cauchy-Schwarz gives
beta_lambda^2<=lambda^3/3 and n_lambda>=1/2. In L7 the upper Jacobian
factor is less than two for E<=7lambda/4 and lambda<=1/16. Thus

    lambda/(8pi^2 I0)<=w_lambda<=lambda/(4pi^2 I0)
                                       <=3lambda/pi^2<lambda/3.

Dividing the upper bound by n_lambda^2>=1/4 gives A_lambda<=2sqrt(lambda).
The lower bound uses I0<=9/8 and n_lambda<=1. Finally A_lambda<=1 follows
from Cauchy-Schwarz between the two normalized physical vectors. These
finite bounds do not replace a source O(lambda^2) remainder by an assumed
numerical constant.

Let x=Q chi_lambda=chi_lambda-A_lambda zeta, so ||x||<=1. The complete
approximate inverse constructed below, for 0<r<=min(1/2,a lambda/2), has

    ||H_*xi_r-x||<=A_lambda sqrt(r)/sqrt(I0),
    ||xi_r||<=C_lambda+A_lambda/[sqrt(I0)sqrt(r)],
    C_lambda=2/(a lambda n_lambda)+beta_lambda sqrt(I0)/n_lambda.
                                                               (Q14)

Write vectors in the invariant
singlet/longitudinal space as (F_s,G_l), meaning F_s c+G_l n·T. On P, integral F_s=0,
and the compressed operator acts as

    H_*(F_s,G_l)=(P_s[2epsilon G_l], 2epsilon F_s),
    P_s f=f-integral f.                                 (L13)

Write chi_lambda=(F_s,G_l). For x=chi_lambda-A_lambda zeta, the formal
inverse singlet component is

    f=G_l/(2epsilon)-A_lambda/(4sqrt(I0)epsilon^2).

It has integral zero but is generally not square-integrable. This is
precisely a place where a naive inverse/gap argument fails. Its triplet
partner g=F_s/(2epsilon) is square-integrable. For 0<r<=min(1/2,a lambda/2),
use the allowed singlet

    f_r=1_(epsilon>=r) f-m_r,
    m_r=integral 1_(epsilon>=r) f
       =A_lambda/(4sqrt(I0)) integral_(epsilon<r)epsilon^-2.

Set xi_r=(f_r,g). Direct application of L13 shows that the residual
H_* xi_r-x has only a triplet component,

    A_lambda/(2sqrt(I0)epsilon) 1_(epsilon<r)-2epsilon m_r.

Using Q4, the free-band lower bound 2epsilon>=a lambda, and triangle
inequalities gives

    ||H_* xi_r-x|| <= A_lambda sqrt(r)/sqrt(I0),
    ||xi_r|| <=2/(a lambda n_lambda)
       +beta_lambda sqrt(I0)/n_lambda
       +A_lambda/[sqrt(I0) sqrt(r)].                    (L14)

For example the two terms in the residual have norms at most
A_lambda[ sqrt(r)+sqrt(3/2)r ]/(2sqrt(I0)), which is bounded
as stated for r<=1/2. The epsilon^-4 estimate controls f_r; the
subtracted constant uses |m_r|<=A_lambda r/(4sqrt(I0)).

In the inverse norm, each band-supported piece costs at most
1/(a lambda n_lambda). The constant term of the triplet inverse costs
beta_lambda sqrt(I0)/n_lambda. The cutoff singular singlet term costs
3A_lambda/(4sqrt(I0)sqrt(r)), and its subtracted mean costs at most
A_lambda r/(4sqrt(I0)); the latter two fit the final term because
3+r^(3/2)<=4 for r<=1/2. Its zero mean follows from
integral G_l/(2epsilon)=A_lambda sqrt(I0).

This inverse has both singlet and longitudinal components; it is not the
singlet-only inverse of Section 3. Its cutoff mean and the contribution from
the contact projection are retained. Applying E_sigma and taking r=sigma
proves, with no unquantified limit,

    ||E_sigma x||<=2A_lambda sqrt(sigma)/sqrt(I0)+sigma C_lambda,
    C_lambda<=4/lambda.                                  (Q15)

For the last inequality, Q13 and sqrt(I0)<2 give
C_lambda<=16/(5lambda)+2<4/lambda on the stated lambda range.

### Two finite evolution comparisons

For z in ran Pi, fix T>0 and write B=B_kappa, A=A_kappa.
All inverses in the following comparison are spectral-cutoff inverses.

For sigma>0, let

    Q_sigma=1_(|H_*|>sigma)(H_*),
    E_sigma=1_(0<|H_*|<=sigma)(H_*),
    v(tau)=exp(-i tau A)z,       A=Pi B Pi,
    y_sigma(tau)=-H_*^(-1)Q_sigma B v(tau).                   (D9)

The inverse in D9 is the bounded spectral-cutoff inverse, of norm at
most 1/sigma. It is not an inverse on the gapless complement. Let
w_delta=v+delta y_sigma. Exact differentiation gives

    (H_*/delta+B)w_delta=A v+E_sigma Bv+delta B y_sigma,
    i partial_tau w_delta=A v+i delta partial_tau y_sigma.

The residual is therefore

    i partial_tau w_delta-(H_*/delta+B)w_delta
      =-E_sigma Bv+delta(i partial_tau y_sigma-B y_sigma).   (D10)

We have ||y_sigma||<=b||z||/sigma and
||partial_tau y_sigma||<=b^2||z||/sigma. Compare w_delta with
the exact unitary evolution, accounting for the initial and final
correctors, then compare the evolutions with and without R_delta.
Bounded-operator Duhamel gives the finite estimate

    sup_(|tau|<=T) ||U_delta(tau)z-v(tau)||
      <= (2delta b+2T delta b^2)||z||/sigma
         +T M_z(sigma,T)+T r_delta ||z||,

    M_z(sigma,T)=sup_(|tau|<=T)||E_sigma Bv(tau)||.            (D11)

A vector in ran Q has only singlet and longitudinal-triplet components.
The derivative B kills its singlet component and maps its longitudinal
component to a transverse one. Therefore

    B_kappa Q=F B_kappa Q,  Q B_kappa Q=0.                 (B5)

First take x supported spectrally on |H_*|>sigma, sigma>0. Put

    v(tau)=exp(-i tau H_*/delta)x,
    y(tau)=B_kappa H_*^-1 v(tau),
    w(tau)=v(tau)+delta y(tau).                            (B7)

The inverse is restricted to that spectral support, so its norm is at
most 1/sigma. By B5, y is in ran F and H_*y=0. Differentiation yields
`i delta partial_tau y=B_kappa v`. Hence

    [i partial_tau-(H_*/delta+B_kappa)]w=-delta B_kappa y. (B8)

Initial and final correctors have norm at most delta b||x||/sigma;
the integrated residual costs T delta b^2||x||/sigma. Duhamel for R_delta
adds T r_delta||x||. For general fixed x in ran Q, cutting away its
low nonzero spectral part E_sigma x gives the bound

    sup_(|tau|<=T)||U_delta(tau)x-exp(-i tau H_*/delta)x||
      <=2||E_sigma x||
        +delta(2b+T b^2)||x||/sigma+T r_delta||x||,
    E_sigma=1_(0<|H_*|<=sigma)(H_*).                      (B9)

Combine the finite D11 estimate with Q11 for zeta. Combine B9 with Q15
for x, using B_kappa Q=F B_kappa Q and Q B_kappa Q=0. Finally use
F exp(-i tau H_*/delta)x=0. For |tau|<=T the transverse error satisfies

    e_perp:=sup ||F U_delta(tau)chi_lambda
                           -A_lambda u(tau)||
     <= delta[ A_lambda(2b+2Tb^2)+(2b+Tb^2)]/sigma
        +A_lambda[4+(7/2)b^2T^2]sqrt(sigma)/sqrt(I0)
        +2sigma C_lambda+(A_lambda+1)T r_delta.          (Q16)

The fast complementary evolution has been annihilated by F, not discarded
by a phase average. All displayed bounds are finite for their stated
parameters, so sigma may now be chosen as a function of lambda and delta.

At kappa0=(1,1,1), T=tau0=1/20, 0<delta<=1, the elementary bounds b<2,
1/sqrt(I0)<4, A_lambda<=1, and Q15 yield

    e_perp<=9delta/sigma+17A_lambda sqrt(sigma)
                              +8sigma/lambda+delta/5.   (Q17)

For example the four relaxed coefficients before rounding are 43/5,
807/50, 8, and 2/15, respectively. This estimate quantifies the
lambda-dependent initial vector; fixed-vector convergence alone would not.

## 5. Actual current: a finite error with the dressing amplitude retained

For particle i=1,2 let h_i be the supplied one-body walk with symbol
sigma_i.sin k_i, X_(i,a) its position operator, and Pi_(i,x) its projection
onto site x. Use the additive symmetric local energy densities

    e_x^0=(1/2) sum_(i=1,2) {Pi_(i,x),h_i},
    e_x=P e_x^0 P,
    H_D=sum_x e_x=P H0 P, H0=h_1+h_2.

Here P removes coincident sites in the antisymmetric two-record space.
On finite-support states the energy first moment is

    D_a=P D0,a P,
    D0,a=(1/2)({X_(1,a),h_1}+{X_(2,a),h_2}).       (J1)

The free commutator is bounded:

    i[H0,D0,a]=g_a,
    g_a=sin(k_(1,a))cos(k_(1,a))
           +sin(k_(2,a))cos(k_(2,a))
        =sin K_a cos(2q_a).                        (J2)

This follows from (1/2){partial_a h_i,h_i}=sin k_(i,a)cos k_(i,a) I.
The cross-particle commutators vanish. We compute i[H_D,D_a] first on
the common finite-support core and then obtain its bounded extension.

Work in a local total-momentum chart K=k_1+k_2, q=(k_1-k_2)/2, with
smooth sections compactly supported in K. Torus q is periodic. Let c be
the constant normalized singlet, C=|c><c|, P=I-C in each fiber, and

    h=H0 c, h'_a=partial_(K_a) h,
    Hdiff=h_1-h_2, H0'=partial_(K_a)H0.

P is independent of K. Since X_(1,a)=i(partial_Ka+partial_qa/2) and
X_(2,a)=i(partial_Ka-partial_qa/2), direct symmetrization gives

    D0,a=i H0 partial_Ka+(i/2) Hdiff partial_qa+i H0'. (J3)

The equality partial_qa Hdiff=2H0' is essential to this expression.
Put Dq=(i/2)Hdiff partial_qa+iH0'. Integration by parts in q gives
Dq^*=(i/2)Hdiff partial_qa, so Dq^* c=0. Also Dq c=i h'_a.
Consequently the contact blocks are

    C D0,a P psi = i c <h,partial_Ka psi>,
    P D0,a C (c f) = i partial_Ka(h f).             (J4)

Here c is constant, <c,H0c>=0 and <c,h'_a>=0. These relations retain
the derivatives in K; discarding them would give the wrong current.

Expand the compressed commutator:

    i[PH0P,PD0,aP]
       =P g_a P-i P H0 C D0,a P+i P D0,a C H0 P.

Insert (J4). The terms h<h,partial_Ka psi> cancel. The remaining bounded
finite-rank correction is

    J_a=i[H_D,D_a]=P g_a P+F_a,
    F_a=-|h'_a><h|-|h><h'_a|.                     (J5)

Both h and h'_a lie in P. Thus (J5) is an operator identity for the bounded
extension of this canonical current, and not a postulated current choice.
It uses the specified compressed local densities in (J1).
The finite-support core calculation extends to the smooth compact-chart
sections used above by H1 approximation: D0,a maps H1 to L2 continuously,
and H0 and P preserve H1. These sections need not themselves have finite
spatial support. No self-adjointness claim for the unbounded dipole is
needed to identify its bounded commutator extension.

Pointwise singlet algebra gives

    h(q)=2 sum_j cos(K_j/2) sin q_j sigma_(1,j)c,
    h'_a(q)=-sin(K_a/2) sin q_a sigma_(1,a)c,
    ||h||^2=2 sum_j cos(K_j/2)^2<=6,
    ||h'_a||=|sin(K_a/2)|/sqrt(2),
    ||F_a||<=2sqrt(3)|sin(K_a/2)|.                 (J6)

In particular both g_a and F_a vanish at central total momentum K=0.
This is consistent with special zero-current sectors; no nonzero drift
for every state is asserted.

The remainder of this section uses the bounded extension above on L2
states; it does not apply the unbounded dipole to zeta.

Write v=s.T and v_a=s_a T_a, with T_a=sigma_(1,a)c, and use the bounded
canonical current just derived. On the full physical space its linear
coefficient and trace identity are

    L_a=P cos(2q_a)P+|v_a><v|+|v><v_a|,
    sum_a L_a=3P-H_*^2/2-2epsilon^2 F.                   (Q18)

Indeed H0(0)^2=4epsilon^2(I-F), H0(0)c=2v, and Pc=0 give

    H_*^2=4P epsilon^2 P-4epsilon^2 F-4|v><v|.

Summing the three L_a gives `3P-2P epsilon^2 P+2|v><v|`, proving Q18.
Multiplication by epsilon^2 commutes with F; it need not commute with P.
Its placement in the displayed formulas matters.

The placement correction is included. Since H_D(delta kappa0)^2 is exactly
conserved and both Hamiltonian norms are at most 2sqrt(3),

    |Delta <H_*^2>|<=8sqrt(3)delta(b+r_delta).            (Q19)

To see Q19, add and subtract the conserved expectation of
H_D(delta kappa0)^2. The two endpoint errors are at most
2||H_D(delta kappa0)^2-H_*^2||, bounded by the displayed right side
using Q5 and ||H_D||,||H_*||<=2sqrt(3).

At the diagonal kappa0, the proper cyclic coordinate rotation acts on
triplets by u(q)->R u(R^(-1)q), and on singlets by f(q)->f(R^(-1)q).
It preserves the measure and chi_lambda, commutes with H_D(delta kappa0),
and permutes the three L_a. Their expectation changes therefore agree.
Initially F chi_lambda=0.
One explicit operator-norm remainder is

    ||J_a(delta kappa)/delta-kappa_a L_a||
      <=delta^2[(1/6+sqrt(3)/24)|kappa_a|^3
                                    +|kappa_a|b^2/8].       (D14)

For D14, ||h||<=sqrt(6), ||v_a||=1/sqrt(2), and
||h-2v||<=delta^2 b^2/(4sqrt(2)). Also
||h'_a/delta+kappa_a v_a/2||
<=delta^2|kappa_a|^3/(48sqrt(2)). Substitute into the exact J_a above and
use the cubic sine remainder for its multiplication term. If kappa_a=0,
J_a(delta kappa) is exactly zero; no division by kappa_a is needed.

At kappa0 this gives the actual-current remainder

    ||J_a(delta kappa0)/delta-L_a||
                              <=[(13+sqrt(3))/24]delta^2. (Q20)

Put e=e_perp. The comparison F U_delta chi_lambda=A_lambda u+error, with
||error||<=e, implies

    | ||epsilon F U_delta chi_lambda||^2
                       -A_lambda^2||epsilon u||^2 |
        <=3e(2A_lambda+e).                               (Q21)

This keeps the small dressing amplitude. Bounding the sum of these norms
by a constant independent of A_lambda would needlessly lose a lambda power.
Using Q18-Q21 and r_delta<=delta at kappa0 proves at tau0

    (actual a-current drift)/delta
      <=-(2/3)A_lambda^2||epsilon u(tau0)||^2
                          +4A_lambda e+2e^2+8delta.      (Q22)

For the final 8delta, the energy-square error contributes at most
4delta+(8/3)delta^2, and the two current remainders contribute at most
(5/4)delta^2; their sum is less than 8delta for delta<=1.
The coupling in Q6 is nonzero. More precisely,

    gamma_kappa^2:=||epsilon g_kappa||^2
       =(1/(4I0)) integral[|d|^2-(d·n)^2],
    b^2/(12I0)<=gamma_kappa^2<=b^2/(8I0),
    gamma_kappa^2>=2b^2/27.                                (D21)

To verify the bounds, separate-coordinate reflections make all mixed
integrals in (d·n)^2 vanish. Cubic symmetry makes the remaining common
coefficient L=integral cos^2(q_1)n_1^2. Write
L=1/3-A0, where A0=integral s_1^4/epsilon^2. Cauchy-Schwarz gives

    A0 integral epsilon^2 >= (integral s_1^2)^2,
    A0>= (1/2)^2/(3/2)=1/6.

Hence 0<=L<=1/6, while integral |d|^2=b^2/2. This proves the
first two bounds in D21; I0<=9/8 proves the last. In particular g_kappa
is nonzero for every nonzero kappa, not just the chosen diagonal.

The bounded exponential Taylor remainder gives

    ||u(tau)+i tau g_kappa||<=b^2 tau^2/2,
    ||epsilon u(tau)||>=|tau|gamma_kappa
                                      -sqrt(3)b^2 tau^2/2. (D22)

For 0<|tau|<=sqrt(2)/(9b), the last expression is at least
|tau|gamma_kappa/2. Thus (2/3)||epsilon u(tau)||^2>=tau^2 gamma_kappa^2/6
>=tau^2 b^2/81. At kappa0=(1,1,1) and tau0=1/20, the small-time
condition holds and this proves

    (2/3)||epsilon u(tau0)||^2>=1/10800.                 (Q23)

Consequently the following fully finite conditions suffice for the diagonal
scaled drift to be at most -A_lambda^2/21600:

    e/A_lambda<=1/200000, delta/A_lambda^2<=1/345600.     (Q24)

Indeed 4/200000+2/200000^2+8/345600<1/21600. This step uses the actual
bounded current, not the free current or a leakage observable.

## 6. One polynomial choice valid on the whole stated band range

For every 0<lambda<=1/16 choose

    sigma=2^-40 lambda^(3/2), delta=2^-68 lambda^2.       (Q25)

This lies in 0<sigma<=min(1/2,a lambda/2) and delta<=1. Since pi<4,
Q13 gives A_lambda>=sqrt(lambda)/12. Divide Q17 by A_lambda to obtain

    e/A_lambda
     <=108delta/[sigma sqrt(lambda)]+17sqrt(sigma)
          +96sigma/lambda^(3/2)+(12/5)delta/sqrt(lambda)
     <=108*2^-28+17*2^-23+96*2^-40+(3/80)*2^-68
      <1/200000.                                       (Q26)

The second line uses lambda^(3/4)<=1/8 and lambda^(3/2)<=1/64.
The remaining margins are also explicit:

    delta/A_lambda^2<=9*2^-68<1/345600,
    delta/(A_lambda^2 lambda)<=144*2^-68<1/44236800,
    delta<=lambda/32.                                   (Q27)

Thus Q24 holds for every lambda in the stated range. No unidentified
lambda-dependent onset remains. The exponents and fractions in Q26-Q27
are checked by exact rational arithmetic in the separate control.

## 7. Actual K-dependent free preparation and one global normalization

For |K|<=lambda/16 use the actual positive projector and define

    phi_(lambda,K)=Pi_++(K)phi_lambda/||Pi_++(K)phi_lambda||,
    n_(lambda,K)=||P phi_(lambda,K)||,
    chi_(lambda,K)=P phi_(lambda,K)/n_(lambda,K).          (Q28)

Each positive one-particle projector is (I+ahat.sigma)/2. On the original
support, 5lambda/8<=epsilon<=7lambda/8, and each sine vector changes by at
most |K|/2. The unit-direction inequality
|a/|a|-b/|b||<=2|a-b|/|b| bounds each projector change by
4|K|/(5lambda). Their product therefore changes by at most
8|K|/(5lambda)<=2|K|/lambda. It respects pair antisymmetry.

Its action on phi_lambda is nonzero. Normalizing costs at most twice the
unnormalized distance, so ||phi_(lambda,K)-phi_lambda||<=4|K|/lambda.
The unchanged q support has epsilon<=7lambda/8 and normalized volume at
most lambda^3/3 by Q4. Cauchy-Schwarz against the constant singlet gives
n_(lambda,K)^2>=1-lambda^3/3. Both physical projection norms are at least
1/2; the map u -> Pu/||Pu|| is then Lipschitz with constant four on these
unit vectors. Consequently

    ||chi_(lambda,K)-chi_lambda||<=16|K|/lambda.

The two positive free energies together move by at most |K|. Thus the
interior band [5lambda/4,7lambda/4] remains inside [lambda,2lambda], and
phi_(lambda,K) is an actual positive free-band vector. These preparation
statements do not assert free-band confinement after contact projection or
excluded evolution.

Here are explicit margins for a full-dimensional K packet. On
|kappa-kappa0|<=1/10 and 0<delta<=1, the exact canonical formula gives

    ||J_a(delta kappa)/delta||<=4,
    ||J_a(delta kappa)/delta-J_a(delta kappa0)/delta||
      <=4|kappa-kappa0|,
    ||U_(delta,kappa)(tau0)-U_(delta,kappa0)(tau0)||
      <=tau0|kappa-kappa0|.                              (B20)

For the first bound, use ||J_a(delta kappa)/delta||
<=(1+sqrt(3))|kappa_a|<=1.1(1+sqrt(3))<4.
For the second bound, the multiplication term costs |kappa-kappa0|.
The two rank-one terms cost at most
`(sqrt(3)+delta/2)|kappa-kappa0|`, since
`||h||<=sqrt(6)`, `||h'_a(K)-h'_a(K0)||<=delta|kappa-kappa0|/(2sqrt(2))`,
`||h(K)-h(K0)||<=delta|kappa-kappa0|/sqrt(2)`, and
`||h'_a(K0)||<=delta/(2sqrt(2))`.
Their sum is less than four. The last bound follows from
`||H_D(K)-H_D(K0)||<=|K-K0|` and bounded Duhamel.

Holding the initial chi_lambda fixed, B20 bounds the change of the scaled
drift between kappa and kappa0 by `9|kappa-kappa0|`.
Replacing it by the actual initial chi_(lambda,delta kappa) costs at most
`4*4*32delta/lambda=512delta/lambda`, using the preparation bound above and |kappa|<2.

Choose the fully explicit kappa radius

    eta_lambda=lambda/(6998400pi^2)<=A_lambda^2/777600.   (Q29)

It is smaller than 1/10, and |kappa|<2 on its ball. Q27 ensures
|delta kappa|<=lambda/16. Equations Q27,Q29 make each of the two preceding
errors at most A_lambda^2/86400. Combining with the diagonal bound Q24
therefore gives, for every |kappa-kappa0|<=eta_lambda,

    actual a-current drift <=-delta A_lambda^2/43200.    (Q30)

Let h be any fixed smooth scalar function supported in the unit ball,
nonzero on an open subset, with integral |h|^2 dy/(2pi)^3=1. For example,
normalize exp[-1/(1-|y|^2)] inside the ball and extend by zero. Put

    f_lambda(kappa)=eta_lambda^(-3/2)
                                  h((kappa-kappa0)/eta_lambda),
    Phi_(lambda,delta)(K,q)=delta^(-3/2)
                         f_lambda(K/delta)phi_(lambda,K)(q),
    N_(lambda,delta)=||P Phi_(lambda,delta)||,
    Chi_(lambda,delta)=P Phi_(lambda,delta)/N_(lambda,delta). (Q31)

The free packet has norm one by the exact K=delta kappa Jacobian, and is
supported in the actual free [lambda,2lambda] band. The physical packet
has one global normalization, with

    1-lambda^3/3<=N_(lambda,delta)^2<=1.                  (Q32)

Its actual kappa probability density is
|f_lambda(kappa)|^2 n_(lambda,delta kappa)^2/N_(lambda,delta)^2.
It integrates to one, generally differs from |f_lambda|^2, and retains the
same support. In physical total momentum, the center and radius are

    K_center=2^-68 lambda^2(1,1,1),
    K_radius=2^-68 lambda^3/(6998400pi^2).               (Q33)

This radius is positive, has nonempty three-dimensional support through h,
and the support stays away from K=0. The physical time is the common value
Q1 in every fiber. Integrating the pointwise estimate Q30 with these actual
weights proves Q2 without any fiberwise renormalization assumption.

## 8. Evidence scope and preserved research

The four frozen component notes and their independent research reviews are
source-bound in the composition map. The review identities are

- Long-time kernel/band review:
  `b9525df21cac9721603776dc703314b73e2572b874ac5ef733b35933d6260e2f`.
- Full-zero-space dynamics review:
  `c0a788f05c291a900acf3bc1002e139f2c0eba749ee6cdc7b08c6bf4812dc9a2`.
- Two-scale projected-band current review:
  `7fa575475439af53c7c0cf4af74fea66537b75ce42afd7418504de4dd0e31051`.
- Explicit-onset review:
  `a530a7b1507e7d22af11f08c236af865ec1c8acb004069b249c9b281bcf4cbda`.

Those reviews reconstructed the required arguments and reported no
consequential source defect within their exact domains. Their earlier
existential-onset limitations belong to those earlier sources; the explicit
estimate Q25-Q27 is supplied by the later quantitative note and its separate
review. No component review is silently treated as a review of changed
publication prose or as an applied retained-status audit.

The existing author and independently written finite controls remain evidence
for their stated algebraic fixtures and parameter budgets. A finite weighted
fixture is not the torus measure; a finite exponential does not prove the
gapless evolution theorem. The proof above supplies the continuum integrals,
spectral-cutoff estimates, actual-current identity and global normalization.
The publication primary preserves all four complete author programs. Its
execution, actual source-copy controls and cache identities are recorded in
the milestone delivery record. No Lean proof of this analytic theorem is
asserted.

The source map preserves the unused leakage, pure-dressing cancellation,
generic fixed-vector limit, and state-comparison nonuniformity findings in
their original files, with their original scope. They are not converted into
broader current no-go claims. Here the uncut inverse may fail to be in L2,
both cutoff means are retained, and the small A_lambda factor is essential
to the finite current margin. The claim remains the specified supplied-model
packet theorem with conservative explicit constants and a positive momentum
width. No optimized onset, universal current sign, monotone decay, many-body
closure or new physical law follows from this construction.


## Publication execution record

The [primary controls](../scripts/excluded_walk_projected_free_band_canonical_current_2026_10_11.py) embed all four complete frozen author control programs
in isolated namespaces. The original programs' source-read metadata identifies
this combined runner; scientific calculations use their unchanged literal
fixtures. NumPy, SciPy and SymPy are required. Their finite algebra, matrix
examples, exact budgets and unvalidated quadrature do not prove the continuum
theorem. Canonical execution, source-copy controls and complete selective
review coverage are recorded in the [delivery checks](../.claude/science/physics-loops/toe-projected-band-current-20261011/DELIVERY_CHECKS.md).

The full parent delta at b9b032ae790c66e762a6296a1306bfb64ae7cd70 must
land first, or the cumulative delta from main
a13caa4885f547c8d206265b031ba7649e539fd9 must be reviewed together.
The supplied-walk and energy-placement contract is used exactly as stated.
No flux/form or effective-memory result is a premise of this theorem.
