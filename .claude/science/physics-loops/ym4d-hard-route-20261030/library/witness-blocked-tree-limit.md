# The blocked corner: free limits and the remaining vertex test

Author: openai/gpt-6-astra/max mac-mini-codex, 2026-11-01.
Source: `5f5f1693a60cfcb7aff5ccd1534f626294a37188`.
Status: discharged calculations for the explicit linear block map below;
implication for the selected producer's stated flat linearization. Full
H-TREE, its contractible-regulator identification, nonlinear second jet
and nonzero corner-vertex requirement remain gap. No numerical run.

## 1. Fix the map and regulator before computing [definition / implication]

Text 8.1 does not select a unique M. This probe uses **only** the flat
linearization stated for the independent attempt's final waypoint map,
Texts 1.2, 5.1 and 5.4. It does not substitute that map for the mapped
attempt. The final rule is inactive near the flat field. Its stated
linearization, modulo a coarse gradient annihilated by a closed current,
is the following explicit map, for odd n:

    (Q_n A)_mu(y)=n^(-4) sum_(x in B_n(ny))
                                      sum_(s=0)^(n-1) A_mu(x+s e_mu),
    B_n(0)={-(n-1)/2,...,(n-1)/2}^4.                        (B-1)

All results below are proved for B-1. Identifying this with a producer's
complete nonlinear map beyond first order is not an input to those proofs.
The componentwise maps compose exactly: Q_N on the fine lattice followed
by Q_M on its coarse lattice equals Q_(MN). The digit decompositions
x=Nu+v and s=Nt+r enumerate B_(MN) and {0,...,MN-1} once each, with
normalization (MN)^(-4). Coarse gradients stay gradients: summing a fine
difference along each straight line telescopes to a difference of block
averages. They therefore disappear after pairing with any closed current,
also after repeated blocking. Thus n=L^j is the relevant cutoff ratio,
not n=1 and not one arbitrarily chosen smearing step.

For this free calculation use a periodic fine lattice of side nS, S an
integer tending to infinity, and the Feynman Gaussian covariance
4(-Delta)^(-1) on each colour and direction, with the zero mode removed.
This defines regulated **tree coefficients**, not a Laplace theorem for
the Wilson law on a torus with flat holonomy modes. Text 8.1 names a
contractible gauge chart: the comparison with that prescribed regulator
is a separate obligation, specified in section 4. No torus full-law
expansion is smuggled into this calculation.

## 2. All the quadratic coefficients converge [discharged for B-1]

For a fixed closed coarse path Gamma let J_Gamma be its signed link
current, with Fourier convention Jhat_mu(p)=sum_x J_mu(x)exp(-ip.x).
It is a bounded trigonometric polynomial, and Jhat(0)=0 since a closed
path has zero net displacement in every direction. Put

    s_n(u)=sin(u/2)/(n sin(u/(2n))),   s(u)=2sin(u/2)/u,
    a_(n,mu)(p)=exp(-i(1-1/n)p_mu/2) s_n(p_mu) prod_nu s_n(p_nu),
    j_(Gamma,n,mu)(p)=a_(n,mu)(p) Jhat_(Gamma,mu)(p),
    lambda_n(p)=4n^2 sum_nu sin^2(p_nu/(2n)).                (B-2)

Values at zero are continuous values. The scaled Brillouin zone is
[-pi n,pi n)^4, with p in (2pi/S)Z^4. Differentiating B-1 in Fourier
variables gives Jhat_(Gamma,n)^fine(k)=n j_(Gamma,n)(nk).
Consequently the covariance of the linear loop fluxes is 4P_(n,S), with

    P_(n,S)(Gamma,Delta)=S^(-4) sum_(p!=0)
       sum_mu conj(j_(Gamma,n,mu)(p)) j_(Delta,n,mu)(p)/lambda_n(p).
                                                                    (B-3)

The limit along **any** n->infinity, S->infinity is

    P_infinity(Gamma,Delta)=int_(R4) (dp/(2pi)^4)
       [prod_nu s(p_nu)^2]
       sum_mu s(p_mu)^2 conj(Jhat_(Gamma,mu)(p))Jhat_(Delta,mu)(p)
                                                       /|p|^2.      (B-4)

Here is the domination, including the two simultaneous limits. On the
scaled zone,

    |s_n(u)|<=min(1,pi/|u|),
    lambda_n(p)>=(4/pi^2)|p|^2.                            (B-5)

The first bound uses the normalized geometric sum and
|sin(u/(2n))|>=|u|/(pi n); the second uses the same sine inequality.
Near p=0, Jhat=O(|p|), so the summand in B-3 is bounded. Outside the
unit ball it is bounded by C prod_nu(1+|p_nu|)^(-2), an integrable
product. Both its integral and its grid sum outside max|p_nu|<=R are
O(1/R), uniformly for S>=1: split the complement into four coordinate
tails, and compare each one-dimensional sum with the integral of
(1+|u|)^(-2). Inside a fixed annulus delta<=|p|<=R, B-2 converges
uniformly and its mesh Riemann sums converge. The small ball contributes
at most C(delta+2pi/S)^4. Take n,S to infinity, then R to infinity and
delta to zero. This proves B-4 and a uniform covariance bound. The same
argument without the small-ball cancellation also works in dimension
four with an integrable |p|^(-2) bound, but cancellation is present here.

For any finite list of paths, the Gaussian joint moments of degree<=8
are finite sums of products of these covariances. To verify this rule,
integrate a Gaussian coordinate times a polynomial by parts; it equals
the sum of its covariances with the other coordinates times the remaining
polynomial expectation. Induction gives all pairings; odd moments vanish.
Thus every C_B and energy-product coefficient C_(Gamma1,...,Gammak),
k<=4, converges, with uniform bounds for each fixed template. In the
part's normalization, C_Gamma=(3/2)P_infinity(Gamma,Gamma).
For Gamma_12 the current is nonzero on an open momentum set where all
sinc factors are nonzero. The nonnegative integrand there is strictly
positive, so C_Gamma12>0. This proves a nonzero *quadratic anchor* in this
free prescription, not a nonzero cubic vertex.

## 3. The vertex also has an explicit limit in this prescription

**Discharged for B-1 and the bare Wilson cubic in Feynman gauge.** Let
E_(i,n,S)=(-Delta)^(-1)J_(Gamma_i,n)^fine, without the colour factor 4.
The Wick contractions in Text 2.1, which use only epsilon_abc delta_ab=0
and the six cross pairings, give the finite Gaussian coefficient

    K_vert(n,S)=12 sum_p sum_(s<t on boundary p) eps_s eps_t
           det[( (dE_i)_p, E_i(b_s), E_i(b_t) )]_(i=1,2,3).           (B-6)

Contractions internal to either cubic vanish by colour antisymmetry;
the six bijections between them produce this determinant. The factors
are (1/4)(1/4)(1/2)6(4^3)=12, with the sign of the Wilson cubic as in
Text 2.1. Only the *linear* blocked currents enter B-6. No nonlinear
blocking jet enters t_3 F_3.

Define continuum one-forms E_i by Fourier transforms

    Ehat_(i,mu)(p)=a_mu(p)Jhat_(Gamma_i,mu)(p)/|p|^2,
    a_mu(p)=exp(-ip_mu/2)s(p_mu)prod_nu s(p_nu),
    F_(i,mu nu)=partial_mu E_(i,nu)-partial_nu E_(i,mu).     (B-7)

Then, along the same joint limit,

    K_vert(n,S) -> 24 int_(R4) sum_(mu<nu)
       det[( F_(i,mu nu), E_(i,mu), E_(i,nu) )]_(i=1,2,3) dx
                  =: K_vert,infinity.                    (B-8)

Convergence proof and absolute integrability. Extend scaled fine fields
as cellwise constant functions on the physical torus of side S:
mathcal E=nE, mathcal F=n^2 dE. Their Fourier multipliers are respectively
j_n/lambda_n and n(exp(ip_mu/n)-1)j_n/lambda_n, combined into the curl.
The latter difference multiplier is at most |p_mu|. Write
b(p)=prod_nu min(1,pi/|p_nu|). At large |p| the first multipliers are
bounded by C b(p)/|p|^2 and the second by C b(p)/|p|. These have uniform
L1 integrals and grid sums: on max|p_nu|~2^k, the sum/integral of b is
at most C(1+k)^4, whereas the extra factors are 2^(-2k), 2^(-k).
Near zero Jhat=O(|p|), giving bounds C/|p| and C, integrable also in
uniform mesh sums. Compact-annulus Riemann sums therefore imply local
uniform convergence of the scaled fields to B-7 and a uniform sup bound.

Discrete Fourier orthogonality gives their squared L2 norms as the mesh
sums of squared multipliers, with normalization S^(-4). These converge
to the continuum norms by the same split: at zero the largest bound is
C/|p|^2; at infinity it is C b(p)^2/|p|^2 or faster. After choosing the
torus fundamental domain centred on the templates and extending by zero,
local convergence plus convergence of norms implies strong L2 convergence:
test the cross inner product first on a fixed cube, then use
Cauchy--Schwarz against the continuum L2 tail. The same proof applies to
each fine-link translate used in B-6, since the translate is O(1/n) and
does not change its norm. Cellwise interpolation changes locations by
O(1/n) and preserves these statements; local uniform convergence follows
from the uniformly convergent Fourier sums and their limiting continuous
functions.

Products in B-6 now converge in L1. For example the error from replacing
F_n by F is at most ||F_n-F||_2 ||E_n||_2 ||E_n||_infinity;
the other replacements have the same bound with the appropriate factors.
This also proves integrability of F E E. On a plaquette, the four signed
edge values become E_mu,E_nu,-E_mu,-E_nu at the same continuum point.
The sum over its six pairs gives twice det[F,E_mu,E_nu]. One curl and
two potentials contribute n^(-4), exactly the physical cell volume in
the resulting Riemann sum. This proves the factor 24 and B-8. []

## 4. The actual H-TREE stop: nonlinear jet, scheme, and nonzero value

**Concrete missing inequality [gap].** For the first candidate in Text 8.1,
use in B-7 precisely

    Jhat_12=(1-exp(-ip2), exp(-ip1)-1, 0, 0),
    Jhat_23=(0, 1-exp(-ip3), exp(-ip2)-1, 0),
    Jhat_31=(exp(-ip3)-1, 0, 1-exp(-ip1), 0).

The required test in this chosen Feynman prescription is

    |24 int sum_(mu<nu)
        det[(F_(i,mu nu),E_(i,mu),E_(i,nu))] dx| >= kappa_*>0.       (NV)

The integral is now defined and absolutely convergent. Its integrand is
not asserted to have one sign. No lower bound on this integral was derived
or computed here. Positivity of the quadratic anchor does not imply NV.
The values 0.6157 (total) and 0.2188 (vertex) at n=1 do not give a bound
on B-8 as n=L^j->infinity, and no old computation has been rerun.

**The other tree coefficients [gap].** K_comp requires the second Taylor
jet of the *actual iterated nonlinear map*. In a fixed logarithmic chart
write M_log(z)=Qz+B(z,z)+O(z^3), with B one half of its second derivative.
The chain rule gives the exact finite-depth recurrence

    Q_(j+1)=Q Q_j,
    B_(j+1)(u,v)=Q B_j(u,v)+B(Q_j u,Q_j v).                 (B-9)

Path multiplication adds its specified quadratic holonomy jet. If
psi_(Gamma,j)(gamma X)=gamma ell_(Gamma,j)+gamma^2 q_(Gamma,j)+...,
then the missing contribution is
(1/4)E_0 sum_cyclic q_(Gamma1,j).(ell_(Gamma2,j) x ell_(Gamma3,j)).
The quadratic results above bound and converge the ell variables but
do not bound B_j or q_j. A sufficient precise repair is convergence of
the covariance-weighted second-chaos kernels of each q_j in Hilbert--
Schmidt norm, in a common Gaussian Fourier realization, uniformly in
the volume limit. Pairing a quadratic kernel with two linear Gaussian
variables is twice its contraction with their tensor product, by Wick,
so that repair would imply convergence of K_comp. A weaker repair may
control just these finitely many contractions. Neither is proved here.
B-9 shows what must be estimated; finite-depth tree consistency alone
does not make the accumulated quadratic sources summable.

**Regulator identification [gap].** B-4/B-8 concern the explicit periodic
zero-mode prescription, independent of the joint sequence n,S. To read
them as the contractible-regulator coefficients of NT2-C, the actual
gauge chart, boundary data and iterated block jets must be compared.
One sufficient comparison, for every coefficient alpha being used, is

    sup_n |alpha_(n,S)^contractible-alpha_(n,S)^periodic|
                  <=epsilon_alpha(S),   epsilon_alpha(S)->0.       (REG-T)

It is enough to prove an appropriate joint-limit version along the
specified trajectory; no such estimate is supplied by saying that a
minimum can be taken in two stages. For the total K_T any coordinate
change must carry the cubic action and observable jets together; the
split K_comp/K_vert is a fixed-scheme split and cannot be transferred
unchanged to a different nonlinear chart. No boundary/gauge comparison
has been assumed proved here.

**Conclusion [gap with discharged subcalculations].** The chosen linear
blocking has controlled quadratic and bare-vertex limits, including a
positive energy anchor. H-TREE for the actual scheme still lacks REG-T,
the nonlinear second-jet control for K_comp, and NV for the corner
candidate. Another triple would need its own certified nonzero integral.
This is an independent stop from the G0/NT1 gaps, not evidence for NT2.
