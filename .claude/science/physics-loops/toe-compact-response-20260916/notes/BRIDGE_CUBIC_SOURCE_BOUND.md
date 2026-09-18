# Volume-uniform cubic source bounds for a lifted Hamiltonian bridge

Working personal derivation, 2026-09-16. Proposed theorem with personal finite challenges completed;
not independently reviewed. The supplied model and every limit are specified
below. The claim concerns one lifted bridge action; it does not replace
the compact winding sum by one lift or prove a photon phase.

## 1. Statement and norms

Let C be the oriented plaquette-link incidence matrix of a finite cubic
spatial graph in dimension3, either a free box or an even periodic torus
of side at least4. A plaquette has four links and a link touches at most
four plaquettes. Thus, for1<=p<=infinity,

    ||C||_(l^p->l^p)<=4,  ||C*||_(l^p->l^p)<=4.             (1)

These deliberately common bounds follow from the absolute row and column
sums and interpolation. The products are uniformly bounded by16, without
dependence on the link or plaquette count.

Let eta_e be independent real Brownian bridges on[0,T], with covariance
g^2 G_T(s,t), G_T(s,t)=min(s,t)-st/T. For a continuous real plaquette
source f(s), define

    V(z)=sum_p(1-cos z_p),
    F(f)=-g^2 log E exp[-g^(-2) integral_0^T V(f(s)+Ceta(s))ds],
    P(f)=integral_0^T V(f(s))ds, R(f)=F(f)-P(f),
    H_p(h)=sup_(0<=s<=T) ||h(s)||_(l^p(plaquettes)).         (2)

Here g>0 and0<T<1/sqrt(2). Set

    kappa=T^2/8, r=16kappa=2T^2<1,
    delta0=r + g^2 T/[2(1-r)],
    delta3=delta0+(1-r)^(-3)-1.                             (3)

The proposed volume-uniform cubic bounds are

    |D^3F(f)[h,k,l]| <= T(1-r)^(-3) H_3(h)H_3(k)H_3(l),
    |D^3R(f)[h,k,l]| <= T delta3 H_3(h)H_3(k)H_3(l).       (4)

All sources and directions are real and continuous in physical time;
finite-dimensional endpoint sources are a special case. Constants are
independent of spatial volume and of the physical-time approximation
used in the proof. They are not bounds on derivatives of the logarithm
of the periodized compact kernel.

For physical lifted endpoints x,y, take

    f(s)=C[(1-s/T)x+(s/T)y].                                (5)

The exact covering-space kernel of

    H=-(g^2/2)Delta+g^(-2)sum_p(1-cos(Ctheta)_p)

is the free real heat kernel multiplied by exp[-F(f)/g^2]. The exact
compact Haar kernel remains(2pi)^E sum_(n in Z^E) k_T(x,y+2pi n).
That identity follows from Feynman-Kac and periodicity; no winding term
is omitted. An endpoint variation u=(u0,u1) gives h(s)=C[(1-s/T)u0+
(s/T)u1], so H_3(h)<=max(||Cu0||_3,||Cu1||_3). Pure-gauge directions
have exactly zero response, as required.

## 2. Positive time-grid approximation

Use m equal subintervals, delta=T/m, interior times t_i=i delta,
i=1,...,m-1, and Dirichlet endpoint values eta_0=eta_m=0. The Gaussian
bridge values have density proportional to

    exp[-delta/(2g^2) sum_i <eta_i,D_m eta_i>],
    D_m=delta^(-2) tridiagonal(-1,2,-1).                    (6)

The reference covariance is g^2 delta^(-1) D_m^(-1), exactly the sampled
Brownian covariance. Weight the density by
exp[-delta g^(-2) sum_i V(f_i+Ceta_i)], and denote its action byF_m.
The Dirichlet heat matrices exp(-sD_m) have nonnegative entries. Since

    (D_m^(-1)1)_i=t_i(T-t_i)/2,

their integrated row sums are bounded bykappa=T^2/8. This holds for
every m>=2. In particular, the inverse precision has operator norm at
mostkappa on the time l^2 space, so the total fluctuation Hessian obeys

    D_m+C*diag(cos(f+Ceta))C >=(1-r)D_m>0.                  (7)

The constant is more conservative than the continuum spectral value
T^2/pi^2. Its advantage here is positivity of the finite time-grid heat
kernel and a row-sum estimate usable with spatial l^p norms. No positivity
of a truncated sine-series covariance kernel is assumed.

## 3. Synchronous transport and its deterministic response bounds

Introduce an auxiliary stochastic-quantization time tau, distinct from
physical time t_i. In ordinary coordinates the diffusion is

    d eta_i = -[D_m eta+C* sin(f+Ceta)]_i d tau
                      +sqrt(2g^2/delta) dB_i(tau).          (8)

The noise coefficient is fixed by the physical-time weight delta in(6).
Its invariant density is precisely the tilted finite-grid bridge density.
Strict convexity(7) makes the flow contractive in its finite-dimensional
Euclidean norm, with a positive rate for every fixed m and spatial graph.
Run all source values with the same additive noise, start at zero at
tau=-A and let A->infinity to obtain a stationary coupling. Bounded sine
forcing and the quadratic precision give finite moments; contraction
makes this pullback limit unique for each source.

For finite A, subtracting the additive noise leaves an ordinary integral
equation with smooth globally Lipschitz drift. Its first and second
source variations therefore follow by ordinary difference quotients.
Let S_h=D_h eta, U_h=h+C S_h, and S_hk=D_k D_h eta. With zero variation
at tau=-A they satisfy

    dot S_h = -D_m S_h-C* [cos(f+Ceta) U_h],
    dot S_hk = -D_m S_hk-C*[cos(f+Ceta) C S_hk]
                            +C*[sin(f+Ceta) U_h U_k].       (9)

Products in the right-hand side are componentwise plaquette products.
For a link/plaquette array Z define

    ||Z||_(infinity,p)=sup_(tau in[-A,0]) max_i ||Z_i(tau)||_p.

Apply the positive heat matrix in variation of constants, take its
physical-time row sum, and then use(1). The first equation gives

    ||S_h||_(infinity,p)
        <=4kappa[H_p(h)+4||S_h||_(infinity,p)],
    ||C S_h||_(infinity,p)<=r/(1-r) H_p(h),
    ||U_h||_(infinity,p)<=H_p(h)/(1-r).                     (10)

This order of estimates matters: the maximum over physical time is taken
before the integrated row-sum bound. We do not replace an integral of
operator norms by the norm of the integrated operator for an arbitrarily
time-dependent forcing.

Use p=3/2 in the second equation of(9), and spatial Holder for the
product U_h U_k, with each factor in l^3. It gives

    ||C S_hk||_(infinity,3/2)
                       <=r/(1-r)^3 H_3(h)H_3(k).          (11)

These bounds are deterministic and independent of noise, A, m and
spatial volume. At each fixed finite m and graph, contractivity also
passes the first two variations to the stationary limit. Indeed the
difference of two solutions of the first-variation equation has a stable
homogeneous part and an inhomogeneous term bounded by the decaying
difference of the base flows. The second equation has the same property
after the first variations have converged. Variation of constants gives
an exponentially decaying bound times at most a fixed polynomial inA.
Finite-dimensional norm equivalence suffices for this convergence;
the volume-uniform bounds(10)-(11) survive the limit unchanged.

## 4. Differentiating the free energy through the coupling

Directly differentiating the finite positive integral gives

    D_h F_m = delta sum_i E <sin(f_i+Ceta_i),h_i>.          (12)

Use the stationary synchronous coupling to differentiate this expectation
twice more. The bounded response estimates justify differentiation under
expectation. With X=f+Ceta,

    D_h D_k F_m = delta sum_i E <cos X_i U_k,i,h_i>,
    D_h D_k D_l F_m
       =delta sum_i E < -sin X_i U_k,i U_l,i
                              +cos X_i C S_kl,i,h_i>.      (13)

The expression is symmetric in the three source directions, since it
is a third derivative of the finite smooth integral, although its
transport representation singles out h.

At each physical time use spatial Holder with exponents3,3,3 for the
first term and3,3/2 for the second. Equations(10)-(11), and
delta(m-1)<=T, bound the cubic coefficient by

    T[(1-r)^(-2)+r(1-r)^(-3)] =T(1-r)^(-3),                (14)

proving the first part of(4) on each grid. No factor of the number of
spatial sites or plaquettes has entered.

## 5. The small cubic correction to the straight-source action

Gaussian integration by parts on the grid gives

    E eta=-D_m^(-1) C* E sin(f+Ceta).

The positive inverse row sum and the four incident plaquettes imply
|E eta_e(t_i)|<=4kappa and |E(Ceta)_p(t_i)|<=16kappa=r.
The finite-dimensional Brascamp-Lieb covariance bound with(7) gives

    Var((Ceta)_p(t_i)) <= g^2 T/(1-r).                     (15)

Here four independent reference link variances contribute, and the
sampled Brownian diagonal is t_i(T-t_i)/T<=T/4. This variance bound
also follows by the usual convex Gibbs covariance argument on the
finite grid; it is not a physical Hamiltonian gap assertion.

Taylor expansion around a scalar random variable's mean, using the
bounded second derivative of sine, now gives pointwise

    |E sin(f+Ceta)_p -sin f_p|<=delta0.                     (16)

Subtract D^3P_m=-delta sum_i <sin f_i h_i,k_i l_i> from(13).
The term with sin X-sin f is bounded byT delta0 times the product of
the H_3 norms. Write U_k=k+C S_k in the remaining product. From(10),

    ||U_k U_l-kl||_(infinity,3/2)
        <=[(1-r)^(-2)-1] H_3(k)H_3(l).                    (17)

The second-variation term is bounded by(11). Summing the coefficients,

    delta0+[(1-r)^(-2)-1]+r(1-r)^(-3)
                                  =delta0+(1-r)^(-3)-1,   (18)

which proves the second part of(4) on the grid. At fixed g,
delta3=O(T^2+g^2 T); this estimates the cubic correction itself, not
merely the full cubic derivative ofF.

## 6. Stronger space-time norms from a positive entrywise majorant

The maximum-in-time estimates above have a stronger version. This step
uses an entrywise positive majorant; it does not integrate operator norms
of a varying signed coefficient. On the finite time grid let B=|C| be
the entrywise absolute incidence matrix, acting separately at each time.
Let D denote D_m tensored with the link identity, and put

    L=B D^(-1) B*,  W=(I-L)^(-1).                         (19)

Every entry of L is nonnegative. Its absolute row AND column sums are
at most16kappa=r, since D^(-1) is symmetric positive entrywise with
row sums at mostkappa and B,B* have row/column sums at most4. Therefore
||L||_(p->p)<=r and ||W||_(p->p)<=1/(1-r) for every1<=p<=infinity,
also with the common physical-time weight delta in the l^p norms.
The inverse W is defined by its convergent nonnegative Neumann series.

At finite auxiliary horizon A, take the componentwise supremum over
auxiliary time of |S_h|. Variation of constants and positivity of the
Dirichlet heat matrix give the vector inequality

    z_h:=B sup_tau |S_h(tau)| <= L(|h|+z_h).

All vectors here have finite size and z_h is bounded by(10). Iterating
the inequality and letting the number of iterations increase gives

    z_h<=W L|h|,    sup_tau |U_h(tau)|<=W|h|.              (20)

For the second variation the same reasoning gives

    B sup_tau |S_hk(tau)|
                 <=W L[(W|h|)(W|k|)].                    (21)

Products remain componentwise. Spatial and physical-time Holder together
now yield, with ||h||_p^p=delta sum_(i,p)|h_i,p|^p,

    ||sup_tau |U_h|||_p<=||h||_p/(1-r),
    ||B sup_tau |S_hk|||_(3/2)
                          <=r||h||_3||k||_3/(1-r)^3.     (22)

The time weight is important: it is the same measure in the product
Holder inequality and in the derivative pairing. No extra grid factor
is introduced. Using(22) in(13), and repeating the subtraction in(17),
proves the stronger finite-grid bounds

    |D^3F[h,k,l]| <=(1-r)^(-3)||h||_3||k||_3||l||_3,
    |D^3R[h,k,l]| <=delta3 ||h||_3||k||_3||l||_3.         (23)

Moreover the transport representation of the Hessian gives an operator
bound, stronger than a quadratic-form estimate:

    ||R''(f)||_(p->p)<=delta2:=delta0+r/(1-r),
                                     1<=p<=infinity.     (24)

To verify it, the Hessian applied to k is the time/plaquette vector
 E[cos X (k+C S_k)]-cos f k. The first diagonal term has magnitude
at mostdelta0|k| by the same mean/variance Taylor bound used for(16),
now applied to cosine. The remaining term is majorized byW L|k|.
Its l^p norm is at most r/(1-r)||k||_p. This proves(24) with the
physical-time inner product defining the operator.

The majorant is a proof estimate, not a replacement for the signed
plaquette incidence or for the physical kernel. It keeps both the row
and column bound that a space-time l^p statement needs. The finite-volume
continuous-time passage below gives(23) with L^3([0,T] times plaquettes).
For continuous sources, duality in(24) passes the bilinear form bound to
L^p and its conjugate; endpoint sources then require only finite matrices.

## 7. Passing to the continuous bridge and endpoint scaling

Couple each time grid to the same continuous Brownian bridges by sampling
their values. For a fixed finite spatial graph, the Riemann sums of the
bounded continuous potential converge almost surely to their integrals.
The same is true of the first three explicit source derivatives of the
potential. The weights are between exp(-2PT/g^2) and1, so the finite
partition function has a strictly positive lower bound at that fixed
graph and g. Dominated convergence passesF_m and the derivatives of its
logarithm toF; the latter can equivalently be written as bounded weighted
moments and cumulants of the first three potential derivatives. The
constants in(4) do not depend on the graph, so they survive this
finite-volume continuum-time limit uniformly. No interchange of a
spatial thermodynamic limit with differentiation is claimed here.

For normalized endpoint fields x=g a0,y=g a1, let

    R_scaled(a0,a1)=g^(-2)R(C[(1-s/T)g a0+(s/T)g a1]).

Its cubic derivative is bounded byg delta3 times the product of the
L^3 norms of the interpolated endpoint curls. For a chain of time slabs,
Jensen's inequality for affine interpolation gives

    sum_n integral_0^T |(1-s/T)b_n+(s/T)b_(n+1)|^p ds
                                      <=T sum_n |b_n|^p, p>=1.

Boundary endpoints enter only once and do not increase this bound. Sum
(23), apply Holder across slabs, and obtain

    |D^3 sum_n R_scaled(a_n,a_(n+1))[u,v,w]|
       <=g delta3 product_(z=u,v,w)
                        [T sum_n ||C z_n||_3^3]^(1/3).    (25)

The coefficient is g delta3. The earlier maximum-in-time estimate would
have given the weaker coefficient2g delta3; the positive space-time
majorant removes that loss. The fullF_scaled has the same estimate with
delta3 replaced by(1-r)^(-3). This is a volume-uniform cubic curl norm;
it is not a theorem about the compact periodized law.

## 8. Relation to earlier work and outstanding checks

Draft PR8164 atc4a31d8d1bc43096080bd5f88b16ffcf24344146, note
BLOCK08_SHORT_TIME_BRIDGE_AND_ENDPOINT_ACTION.md, was reread in full.
It establishes a proposed uniform Hessian correction and spatial locality
using a different covariance proof, but states no C3 result. This note
reconstructs the carrier and adds the transport derivative argument,
so it does not silently treat that earlier draft as an independently
reviewed premise. The source of the finite-dimensional covariance tool
is Carlen/Cordero-Erausquin/Lieb1106.0709v2, previously read at PDF1-8;
the actual hypotheses are verified in(7) and(15).

Completed personal challenges compare third log derivatives by Gaussian
moments/cumulants and Fourier-Bessel one-face integrals, and check the
positive time-grid Green row sum, incidence norms, noise normalization,
physical endpoint scaling and static response majorants. See the linked
review for the exact finite scope and preserved source revisions. A finite check cannot prove
the all-volume bound. The compact winding sum and the source dependence
of its normalized mixture remain explicit open obligations.

## Author evidence and status

See [personal review](../review/PERSONAL_REVIEW.md), [claim status](../CLAIM_STATUS_CERTIFICATE.md), and [negative-claim discipline](../NO_GO_DISCIPLINE_CHECKLIST.md). Finite checks are challenges to the proof, not independent review or an execution of an infinite-volume theorem.
