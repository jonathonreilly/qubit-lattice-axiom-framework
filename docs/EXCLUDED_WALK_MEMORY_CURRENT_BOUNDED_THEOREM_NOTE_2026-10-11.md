---
claim_id: excluded_walk_memory_current_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
runner: scripts/excluded_walk_memory_current_2026_10_11.py
claim_scope: "For the supplied antisymmetric excluded Weyl pair and canonical compressed energy placement, prove the effective dressing's exact memory equation and absolutely continuous spectral measure, its regulated outgoing formula and explicit selected-datum weighted lower bound, and a joint growing-time current limit for one normalized projected positive-free-band packet family."
upstream_dependencies:
  - excluded_walk_projected_free_band_canonical_current_bounded_theorem_note_2026-10-11
  - excluded_walk_low_energy_energy_current_bounded_theorem_note_2026-10-11
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: "Construct controlled links from microscopic dynamics to macroscopic transport."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Quantify the outgoing-state convergence or test additional specified preparations before using this coherent current result in a macroscopic transport argument."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exact effective memory and a joint growing-time canonical-current limit

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. The four source arguments have
completed selective independent mathematical checks at the identities recorded
in Section 17. The complete publication composition has also received a scoped
source-bound check. Its reviewer's prior source authorship is disclosed in the
[delivery checks](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/d8480b5a6e04102ff076b3dd6f817a2d43f20252/.claude/science/physics-loops/toe-projected-band-current-20261011/DELIVERY_CHECKS.md);
that authorship is not counted as new independent evidence. No independent
retained-status audit is claimed.

For each fixed nonzero kappa, the normalized physical dressing under the
bounded effective generator has an exact Volterra memory equation and an
absolutely continuous spectral measure. Its survival amplitude tends to zero.
An application of Kato's trace-class theorem on the same fixed Hilbert space
gives a unit-norm outgoing transverse datum and a strictly positive weighted
limit W_+. The specified canonical-current observable consequently has the
weighted limit proved below.

For the actual excluded walk, fix any 0<gamma<1/2. The final construction uses
the band parameter 0<lambda<=1/16, weak total-momentum scale delta=lambda^3,
an actual positive free [lambda,2lambda] packet with total-momentum center
lambda^3(1,1,1) and radius lambda^5, and one global contact projection and
normalization. At physical time t_lambda=lambda^(-(3+gamma)), each component
obeys

    Delta<J_a>/lambda^4
      =-W(lambda^(-gamma))/(12pi^2 I0)+O(lambda^(1/2-gamma))
      ->-W_+/(12pi^2 I0)<0,                    a=1,2,3.

The outgoing formula and moment/cone argument in Section 15 give, for the
datum selected by the dressing preparation at each fixed nonzero kappa,

    W_+>=c0=6859/60752858276421362793738298982400
            >1.128*10^(-28),
    lim_(lambda down to 0) Delta<J_a>/lambda^4<=-c0/135<0.

The error estimates the difference from the moving W(lambda^(-gamma)). No
rate for W(t)-W_+ or numerical onset for the final sign is proved, and c0
is not a lower bound for arbitrary unit transverse vectors. This is a
constructed coherent preparation and current change in the supplied generator
clock. It is not a collision clock,
Markov law, monotonic decay, arbitrary-preparation result or many-body closure.

## 1. Supplied model and physical effective space

The [projected-band current companion](EXCLUDED_WALK_PROJECTED_FREE_BAND_CANONICAL_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md)
supplies the physical contract and the finite all-time comparison used in
Section 12. Its frozen composition source has SHA-256
`ecb7eacddc0a11b2636030ed5e4759fabb9945568f3f3f4699f650463f5bf969`.
The [parent low-energy walk theorem](EXCLUDED_WALK_LOW_ENERGY_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-11.md),
original proof-source SHA-256 `9f551fc8d3592e83d15a007495a8f9165a5ddb9bc1e98d9dd3f51b6a2584f401`,
fixes the supplied walk and selected additive symmetric energy placement.
Their proposed status is not promoted by this composition. No stationary
hard-core scattering or Cook-regularity theorem is needed here.

All relative-torus and local total-momentum integrals use dq/(2pi)^3 and
dK/(2pi)^3. The local chart is K=k_1+k_2, q=(k_1-k_2)/2. Even singlet and
odd triplet coefficients implement antisymmetry, with no extra exchange or
half-torus factor. The lattice, generator clock, pair sector, contact rule,
coordinates and canonical placement remain supplied premises.

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

Inner products are linear in their second slot. All q integrals use
`dmu(q)=dq/(2pi)^3` on the periodic three-torus. Write

    s_j=sin q_j,  epsilon=|s|,  n=s/epsilon,
    I0=integral 1/(4epsilon^2),
    zeta=n/(2epsilon sqrt(I0)).                              (E1)

Cone points form a null set. The preceding calculation proves `0<I0<infinity`, the useful
bounds `1/12<=I0<=9/8`, and `||zeta||=1`. The physical zero space is
`Z=F direct-sum span{zeta}`, where F consists of odd transverse triplet
fields `u(q)` satisfying `n·u=0`. The auxiliary constant singlet is absent.

Fix kappa in R^3, put `b=|kappa|`, and define

    d_j=kappa_j cos q_j,     f=d·n,
    J u=i n cross u,        D=f J,
    g=i(d cross n)/(2epsilon sqrt(I0)),
    G=|g|^2=(|d|^2-f^2)/(4epsilon^2 I0),
    A=[ D       g ],
      [ <g|     0 ].                                       (E2)

All these operators have the following full-space domains: D is bounded
self-adjoint on F, `g in F`, and `A=Pi B Pi` on Z, where
`B u=i d cross u` and `||A||<=||B||<=b`. Both pointwise factors in D
change sign under q to -q, so D preserves the odd parity; g is odd.
No inverse of a gapless Hamiltonian or derivative of zeta is used.

The effective evolution is

    exp(-it A)zeta=(u(t),a(t)),   u(0)=0, a(0)=1.            (E3)

When `kappa=0`, A is zero, `a(t)=1`, and no transfer occurs. Every decay
statement below explicitly assumes `b>0`.

For completeness, the transverse-block identity is
(I-nn^T)(d cross u)=(d dot n)n cross u for n dot u=0.
B zeta is already transverse and <zeta,B zeta>=0 pointwise. These facts
verify both entries g and <g| of E2 and their signs. The entire physical
zero projection is Pi of Q3; the auxiliary constant singlet remains absent.
The nonzero coupling also has the following quantitative bound.

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

## 2. Elimination of the transverse field

On a transverse fiber, `J*=J`, `J^2=I`, and `D^2=f^2 I`.
Since g is i times a real vector, `g*Jg=0` pointwise. Consequently

    <g,exp(-it D)g>=K(t),
    K(t)=integral G(q) cos(t f(q)) dmu(q).                  (E4)

Here and below a bra without a point argument denotes the Hilbert-space
inner product; pointwise equalities are identified explicitly. To check
E4, use `exp(-itD)=cos(tf)I-i sin(tf)J`. This also handles `f=0`
without a division. The kernel is continuous, real and even, and
`|K(t)|<=eta:=||g||^2`. It need not be positive at every time.

The exact block equations and bounded variation of constants give

    i u'=Du+a g,   i a'=<g,u>,
    u(t)=-i integral_0^t exp[-i(t-s)D]g a(s) ds,
    a'(t)=-integral_0^t K(t-s)a(s) ds,  a(0)=1.             (E5)

The minus sign is fixed by the two factors of -i. All integrals are
Bochner or ordinary integrals of bounded continuous functions. Iteration
of the integrated equation bounds the n-th uniqueness remainder on
`[0,T]` by a constant times `eta^n T^(2n)/(2n)!`; hence E5 determines
a uniquely. Real coefficients and real initial data make a real for
positive times. Unitarity gives `a(-t)=conj(a(t))`, so a is real and even.
Unitarity also supplies the exact transfer identity

    P_F(t):=||u(t)||^2=1-a(t)^2.                            (E6)

For example, D21 for `||epsilon g||^2` and `epsilon^2<=3`
give `2b^2/81<=eta<=b^2` for b>0. The upper bound follows also from
`||A zeta||<=b`. A useful finite-time consequence is

    eta t^2/2 <= P_F(t) <= eta t^2,
    P_F(t)>=b^2 t^2/81,       whenever |bt|<=1.             (E7)

For a direct proof, let nu be the probability spectral measure of A at
zeta. It is supported in `[-b,b]`, and real a gives
`a(t)=integral cos(tE) dnu(E)`. Its second moment is eta and its fourth
moment is

    mu4=||A^2 zeta||^2=||Dg||^2+eta^2<=b^2 eta.

The elementary cosine remainders imply
`a>=1-eta t^2/2>=1/2` and
`eta t^2/2-mu4 t^4/24<=1-a<=eta t^2/2` on E7's interval.
Thus `1-a>=11 eta t^2/24`, while `1+a>=3/2`; their product is at
least `11 eta t^2/16`, which is stronger than the displayed lower bound.
The upper bound uses `1+a<=2`. This is coherent transfer, not a rate law.

## 3. Scalar resolvent and Laplace transform

Define the finite positive bath measure beta by

    beta(L)=1/2 integral G(q)[1_L(f(q))+1_L(-f(q))] dmu(q).
                                                                  (E8)

Its mass is eta, its support lies in `[-b,b]`, and it is symmetric.
The factor 1/2 follows from the two helicity projections `(I+/-J)/2`:
each has pointwise g weight G/2. It is not a probability normalization.
For `Im z != 0`, block elimination in `(z-A)(v,alpha)=(0,1)` proves

    Sigma(z)=<g,(z-D)^(-1)g>
            =integral z G/(z^2-f^2) dmu
            =integral (z-E)^(-1) dbeta(E),
    M(z):=<zeta,(z-A)^(-1)zeta>
            =1/[z-Sigma(z)].                               (E9)

In the upper half-plane, `Im Sigma(z)<=0`, so the denominator has
strictly positive imaginary part. This verifies its nonvanishing with
the displayed resolvent convention. Fubini in E5, or `i M(ip)`, gives

    integral_0^infinity exp(-pt)a(t)dt
       =1/[p+integral pG/(p^2+f^2) dmu],   Re p>0.          (E10)

The formula is exact for the bounded generator. Replacing its denominator
by a constant damping coefficient is an additional approximation that
is not made here.

There is also an exact formula for the produced field's q distribution.
Let `C_q(t)=integral_0^t cos[f(q)(t-s)]a(s)ds` and define `S_q` by
replacing cosine with sine. E5 gives

    u(q,t)=-i C_q(t)g(q)-S_q(t)J(q)g(q),
    |u(q,t)|^2=G(q)[C_q(t)^2+S_q(t)^2]
       =G(q)|integral_0^t exp[-if(q)s]a(s)ds|^2.            (E11)

The cross term vanishes because `g*Jg=0`; a is real. In particular,
`P_F` is the integral of E11, while the weighted quantity in the actual
diagonal-kappa current is

    W(t)=||epsilon u(t)||^2
        =integral epsilon^2 G |integral_0^t exp(-ifs)a(s)ds|^2 dmu.
                                                                  (E12)

For `kappa=k(1,1,1)`, the identity D20 proved in Section 10 gives
`<exp(-itA)zeta,calJ_a exp(-itA)zeta>=1-(2/3)W(t)`.
E6 and E12 are different observables. Decay of a alone does not supply
a limit of W or a limiting canonical current.

The delta in Sections 4–6 is a spectral edge margin with 0<delta<b.
It is local to those sections. The later weak-momentum parameter delta
has a separate definition in the original-walk comparison.

## 4. A quantitative continuum bath lower bound

Assume b>0. For `0<delta<b` set

    chi=delta/b,       r0=sqrt(chi)/8,
    c_delta=b chi^(3/2)/(16384 pi^2 I0).                    (E13)

Then, as a measure inequality,

    dbeta(E) >= c_delta 1_{|E|<=b-delta/2} dE.             (E14)

This inequality does not assert that beta has no additional singular
part. The lower bound is all that the subsequent proof needs. It is
uniform in the direction of kappa, with the literal normalized torus
measure. The proof uses only a small shell about q=0.

Write `q=r omega`, where omega is on the unit sphere, `0<r<=1/2`,
and `e=kappa/b`. Define

    X(r,omega)=sin(2r omega)/(2r),
    Y(r,omega)=sin(r omega)/r,   h=|Y|,
    v=X/h,    n=Y/h,    f/b=e·v.

Componentwise sine bounds give

    ||X-omega||<=2r^2/3,  ||Y-omega||<=r^2/6,
    1-r^2/6<=h<=1,       ||v-omega||<=r^2,
    ||n-omega||<=r^2/2.                                  (E15)

For a tangent vector H at omega, differentiate the explicit expressions.
One has `||dX[H]-H||<=2r^2||H||`,
`||dY[H]-H||<=r^2||H||/2`, and

    |dh[H]|<=2r^2||H||/(3h),
    ||dv[H]-H||
      <=r^2[13/(6h)+2/(3h^3)]||H||<=4r^2||H||.           (E16)

For the first line, use `omega·H=0`, `||dY[H]||<=||H||`, and
`Y·dY[H]=(Y-omega)·dY[H]+omega·(dY[H]-H)`.
For the second, differentiate X/h and use `||X||<=1`.
Since `h>=23/24`, the final numerical constant is strictly below 4.
Also `||d/b-e||<=r^2/2`, so

    ||(d/b) cross n-e cross omega||<=r^2.                 (E17)

Choose any oriented orthonormal completion of e and parameterize the
sphere by `t=e·omega` and azimuth phi. This is only a change of integration
coordinates; lattice rotational symmetry is not assumed. Here
`|partial_t omega|=(1-t^2)^(-1/2)` and the volume element is
`r^2 dr dt dphi`. Restrict to

    r0/2<=r<=r0,
    -1+chi/4<=t<=1-chi/4,    0<=phi<2pi.

E15–E17 imply on this set

    |f/b-t|<=r^2<=chi/64,
    |partial_t(f/b)-1|<=4r^2/sqrt(1-t^2)<=sqrt(chi)/8,
    7b/8<=partial_t f<=9b/8<2b,
    |d cross n|>=b[sqrt(chi)/2-r^2]>=b sqrt(chi)/4.
                                                                  (E18)

At the two t endpoints, the range of f contains
`[-b+delta/2,b-delta/2]`, since `chi/4+chi/64<chi/2`.
For each r,phi the map t to f is strictly increasing. Moreover
`epsilon<=r`, so `G>=b^2 chi/(64 I0 r^2)` on this shell.
Changing the t variable to E in just the positive-f term of E8 gives,
for each Borel set L in that interval,

    beta(L)>= (1/2)(1/(2pi)^3)
       integral_(r0/2)^r0 integral_0^(2pi)
          [b^2 chi/(64 I0 r^2)] [r^2/(2b)] |L| dphi dr
       = b chi r0 |L|/(2048 pi^2 I0)=c_delta |L|.          (E19)

Only one helicity contribution is used, so no doubling is hidden. The
other term is nonnegative. This proves E14, including every power of r,
b, chi, I0 and the torus normalization.

## 5. Absolute continuity of the dressing spectral measure

Let nu be as in Section 2, so `M(z)=integral (z-E)^(-1)dnu(E)`.
For `|x|<=b-delta` and `0<y<=delta/2`, E14 supplies

    -Im Sigma(x+iy)
      >=c_delta integral_(x-delta/2)^(x+delta/2)
                        y/[(x-E)^2+y^2] dE
      =2c_delta arctan[delta/(2y)]>=pi c_delta/2.

Consequently

    |M(x+iy)|<=C_delta:=2/(pi c_delta)
          =32768 pi I0/[b chi^(3/2)].                     (E20)

This is a bound throughout the indicated upper-half-plane strip, not
merely an almost-everywhere boundary value. It controls singular measure:

    nu([x-y,x+y])<=2y[-Im M(x+iy)]<=2 C_delta y.           (E21)

The first inequality follows by integrating the Poisson kernel, which
is at least `1/(2y)` on that interval. Interval covers and outer regularity
now give absolute continuity of nu on `(-b,b)`, with density at most
C_delta almost everywhere on `[-b+delta,b-delta]`. Indeed every interval
inside that compact interval with length at most delta has nu mass at
most C_delta times its length, by E21 at its midpoint. Subdivision extends
the same bound to longer contained intervals. Countable interval covers
then give domination by C_delta times Lebesgue measure on its interior;
its two endpoints have zero mass by E21 as y tends to zero. Exhausting
`(-b,b)` proves the assertion. Thus no interior atom or singular-continuous
part of the dressing measure is left untreated.

Its only remaining possible singular support is `{−b,b}`. The source's
compression structure excludes both endpoint atoms without an endpoint
integral estimate. For nonzero kappa,

    |d(q)|^2=sum_j kappa_j^2 cos^2(q_j)<b^2

almost everywhere: equality requires `sin q_j=0` for every nonzero
kappa_j, a null set. For any nonzero physical zero-space vector z,
viewed as its triplet field,

    ||A z||<=||B z||
       <=(integral |d(q)|^2|z(q)|^2 dmu)^(1/2)<b||z||.     (E22)

An eigenvector of A at either endpoint would contradict E22. A spectral
atom there would provide such an eigenvector through the spectral
projection. Since the spectrum is contained in `[-b,b]`, nu is therefore
entirely absolutely continuous:

    dnu(E)=rho(E)dE,  rho>=0,  integral rho=1,
    supp rho subset [-b,b].                               (E23)

Strict inequality for each vector in E22 is not an operator-norm gap.
No such gap was used. Nor does this argument classify the entire spectrum
on every reducing subspace of Z: E23 concerns the dressing spectral
measure and its cyclic subspace.

The elementary Fourier consequence can be proved here without a limiting
absorption or scattering theorem. Approximate rho in L1 by finite linear
combinations of interval indicators. The integral of `exp(-itE)` over
each fixed interval tends to zero; the L1 approximation error bounds the
Fourier error uniformly in t. Thus

    a(t)=integral exp(-itE)rho(E)dE ->0 as |t|->infinity,
    P_F(t)->1.                                             (E24)

The same argument applies to `E^j rho(E)`, for each nonnegative integer
j, so every derivative of a tends to zero. No monotonicity, exponential
law, relaxation of the full state, or incoherent mixture follows.

## 6. A finite-horizon bound with an explicit spectral edge term

The proof gives a quantitative mean-transfer bound even before a pointwise
Fourier rate is available. For `0<delta<b`, define directly from E9

    e_delta=min{1, 4delta[-Im M(b+i delta)]},
    H_delta(T)={2C_delta[1+log(2bT)]/T}^(1/2),
    T>=1/(2b).                                            (E25)

Then

    (1/T) integral_0^T P_F(t)dt
      >=max{0,1-[e_delta+H_delta(T)]^2}.                   (E26)

To prove the edge estimate, apply the first inequality in E21 at x=b,
y=delta, without using its second inequality. The upper edge mass is
at most `2delta[-Im M(b+i delta)]`. E9 implies
`M(-conj z)=-conj M(z)`, so the lower edge has the same bound. Hence
`nu({|E|>b-delta})<=e_delta`. Endpoint absence and dominated convergence
also give `e_delta->0`: the relevant integrand is
`delta^2/[(b-E)^2+delta^2]`, which tends to the endpoint indicator.

Split a into the Fourier transforms of the central and edge restrictions
of nu. The latter has absolute value at most e_delta. For the former,
the density bound C_delta and

    |(1/T) integral_0^T exp[-it(E-E')]dt|
                  <=min{1,2/[T|E-E'|]}

alone would give a slightly weaker constant. The squared modulus has an
even difference measure: swapping E,E' cancels the imaginary terms, leaving
`sin[T(E-E')]/[T(E-E')]`, whose absolute value is at most
`min{1,1/[T|E-E'|]}`. Integrating this bound against a density bounded
by C_delta, over differences of absolute value at most 2b, yields

    (1/T) integral_0^T |a_central(t)|^2 dt
           <=2C_delta[1+log(2bT)]/T.

Minkowski's inequality in normalized `L2([0,T])` proves E26. The cancellation
does not require a pointwise positivity claim for sinc or symmetry of the
central measure itself.

All quantities in E25 are explicit in the torus resolvent formula and
E13. C_delta has inverse-frequency units, T has inverse-frequency units,
and e_delta is dimensionless. The bound is conservative and may initially
be zero. First choosing delta small and then T large makes its right side
arbitrarily close to one. This does not supply a simple power or exponential
rate in T: no quantitative bound on e_delta as delta tends to zero is
proved. An unvalidated numerical torus integral is not a certified value
for that remaining term.

## 7. A finite bath that does not decay

The block algebra and memory identity do not imply E24 for an arbitrary
bath. In two transverse dimensions let

    D=[0,-i f; i f,0],   g=(i h,0)^T,
    A=[ 0   -i f   i h ],
      [ i f   0     0  ],
      [-i h   0     0  ].                                 (E27)

For `f=3/5,h=4/5`, direct multiplication gives `A^3=A`.
The exact exponential `I-i sin(t)A+[cos(t)-1]A^2` therefore gives

    K(t)=(16/25)cos(3t/5),
    a(t)=(9+16cos t)/25,
    nu({0})=9/25,     a(2pi n)=1.                         (E28)

The scalar resolvent and Volterra equation remain exactly correct. The
continuum lower bound E14 fails for this finite bath, so the example does
not contradict E24. It rules out deriving irreversible transfer from the
block form alone, and shows why taking an infinite-time limit on a fixed
finite momentum grid would be invalid evidence for this continuum theorem.

## 8. Same-space trace-class comparison

The primary theorem is Theorem 1, p.260, in Tosio Kato, *Perturbation of
Continuous Spectra by Trace Class Operators*, Proceedings of the Japan
Academy 33 (1957), 260–264, [official PDF](https://www.jstage.jst.go.jp/article/pjab1945/33/5/33_5_260/_pdf).
Its proof of completeness is in Section 3, p.263. The locally archived
source was sufficient; no new network lookup was used.

Kato takes a self-adjoint H0 and a bounded self-adjoint trace-class V on
one Hilbert space, and sets H1=H0+V. If P0 and P1 are their absolutely
continuous projections, his equations (1.1)–(1.2) assert

    Omega_+/- = s-lim_(t->+/-infinity) exp(itH1)exp(-itH0)P0,
    Omega_+/-^* = s-lim_(t->+/-infinity) exp(itH0)exp(-itH1)P1,
    Omega_+/-^* Omega_+/-=P0,
    Omega_+/- Omega_+/-^*=P1.                               (W1)

In particular the final subspace is the entire absolutely continuous
subspace of H1. The theorem does not require either operator to be wholly
absolutely continuous, or absence of other bound states. The source's
adjoint stars and both signs were checked on the page image: extracted
text drops some stars and misreads the year in the heading. The proof's
use of both forward and reverse limits was also checked against p.263.
This is an imported mathematical theorem, not a new proof of Kato's result.

Use normalized relative-torus measure `dmu=dq/(2pi)^3` and inner products
linear in the second slot. Set `s_j=sin q_j`, `epsilon=|s|`,
`n=s/epsilon` almost everywhere, and use the normalized dressing vector

    zeta=n/(2epsilon sqrt(I0)),  I0=integral 1/(4epsilon^2).

The fixed physical zero space is `Z=F direct-sum C`, with zeta represented
by `(0,1)` and F the odd transverse L2 triplet fields. The auxiliary
constant singlet is not part of this space. Fix `kappa!=0` and `b=|kappa|`.
E2 supplies

    d_j=kappa_j cos q_j,  f=d·n,
    D u=i f n cross u,
    g=i(d cross n)/(2epsilon sqrt(I0)),
    A=[ D       g ],      A0=[ D       0 ].
      [ <g|     0 ]          [ 0       0 ]                 (W2)

D and A are bounded self-adjoint operators, and `g in F`. All domains
are the full indicated Hilbert spaces. In particular A and A0 act on the
same Z, rather than on different constrained and unconstrained spaces.

Let `gamma=(g,0)` and keep zeta for `(0,1)`. Then

    V=A-A0=|gamma><zeta|+|zeta><gamma|,
    <gamma,zeta>=0,
    ||V||=||g||,       ||V||_1=2||g||.                    (W3)

For a direct trace-norm check, on the orthonormal pair
`gamma/||g||,zeta`, V is `[[0,||g||],[||g||,0]]`; it is zero on the
orthogonal complement. Its only nonzero eigenvalues are `+/-||g||`.
D21 proves `||g||>0` when kappa is nonzero. Thus V has rank two,
is self-adjoint and belongs to the trace class. This matches every
operator and domain hypothesis of W1, with `H0=A0`, `H1=A`.

The scalar zero block of A0 is a pure eigenvalue, so

    P0=P_ac(A0)=P_ac(D) direct-sum 0.                      (W4)

It is not necessary to prove `P_ac(D)=I_F`. Any singular or point subspace
of D is automatically excluded by P0, and Kato's completeness identifies
the part actually needed. The memory theorem establishes the stronger
spectral fact `dnu_zeta=rho(E)dE` for A, hence

    P1 zeta=P_ac(A)zeta=zeta.                             (W5)

W5 uses the full absolute-continuity result E23, not just the scalar
survival-amplitude limit. Its endpoint step was already proved there by
strict pointwise compression, so no possible endpoint atom of the dressing
measure is omitted. Kato itself demands no separate endpoint regularity
or density bound. Other spectral vectors of A are not classified here.

## 9. Unit-norm outgoing datum and weighted limit

For positive time, define

    (u_+,0)=Omega_+^* zeta.                               (W6)

W1, W4 and W5 give `u_+ in ran P_ac(D)` and
`||u_+||^2=<zeta,P1 zeta>=1`. The reverse limit in W1 reads

    exp(itA0)exp(-itA)zeta ->(u_+,0).

Multiplication by the time-dependent unitary `exp(-itA0)` preserves the
norm of the difference, and therefore proves

    r_+(t):=||exp(-itA)zeta-(exp(-itD)u_+,0)|| ->0.
                                                                  (W7)

This implication uses the adjoint wave operator, with the same positive
time sign. Using `Omega_+ zeta` instead would be wrong: zeta is in the
scalar point subspace of A0 and P0 zeta=0. The free outgoing datum lies
in F, not in the scalar channel.

Write `exp(-itA)zeta=(u(t),a(t))`. Every bounded scalar multiplication
operator m(q) preserves F when m is even, and it commutes with D pointwise.
For such a real m, put `Q_m=diag(M_m,0)` on Z. W7 gives

    |<exp(-itA)zeta,Q_m exp(-itA)zeta>
                         -integral m(q)|u_+(q)|^2 dmu|
                    <=2||m||_infinity r_+(t).             (W8)

The right comparison vector in W7 has norm one; the ordinary two-vector
quadratic-form estimate proves the displayed factor. Its expectation is
constant because Q_m commutes with A0. This is the exact point where
strong scattering and the conserved comparison observable are used.

Apply W8 to `m=epsilon^2`, for which `0<=m<=3` and the zero set consists
of finitely many cone points. Since `||u_+||=1`,

    W(t):=||epsilon u(t)||^2 -> W_+:=||epsilon u_+||^2,
    0<W_+<3,
    |W(t)-W_+|<=6r_+(t).                                  (W9)

The lower inequality follows because epsilon is positive almost everywhere
and u_+ is a nonzero L2 vector. The upper inequality is also strict:
`epsilon^2=3` only on a null set. These null-set arguments establish strict inequalities for the
actual outgoing datum, without a computed lower bound at this step. The
selected-datum bound is proved in Section 15 using additional moment and
resolvent control. The multiplication weight alone has no positive uniform
lower bound near a cone.

The same reasoning works for negative times with `u_-=Omega_-^*zeta`.
Each sign has its own unit-norm datum. The conclusions below use the
positive-time convention only; no equality of the two data is assumed.

## 10. The specified canonical-current observable

The current is fixed by the additive symmetric placement
e_x^0=(1/2) sum_i {Pi_(i,x),h_i}, e_x=P e_x^0 P and its energy first
moment D_a=P D0,a P, where
D0,a=(1/2)({X_(1,a),h_1}+{X_(2,a),h_2}). The companion Section 5 proves
the following bounded extension of i[H_D,D_a] on a common finite-support
core. Its unbounded dipole is not applied to the singular dressing vector.

The bounded canonical current is

    J_a(K)=P[sin K_a cos(2q_a)]P
                         -|h'_a><h|-|h><h'_a|,
    h=2 sum_j cos(K_j/2) sin q_j T_j,
    h'_a=-sin(K_a/2)sin q_a T_a.                            (D12)

We use this bounded identity on all physical L2 vectors. We do not
apply the source's unbounded dipole or an H1 commutator to zeta.
Set v=s·T and v_a=s_a T_a; then

    J_a(lambda kappa)/lambda=kappa_a L_a+O(lambda^2),
    L_a=P cos(2q_a)P+|v_a><v|+|v><v_a|,
    ||L_a||<=1+sqrt(3).                                    (D13)

One explicit operator-norm remainder is

    ||J_a(lambda kappa)/lambda-kappa_a L_a||
      <=lambda^2[(1/6+sqrt(3)/24)|kappa_a|^3
                                    +|kappa_a|b^2/8].       (D14)

For D14, ||h||<=sqrt(6), ||v_a||=1/sqrt(2), and
||h-2v||<=lambda^2 b^2/(4sqrt(2)). Also
||h'_a/lambda+kappa_a v_a/2||
<=lambda^2|kappa_a|^3/(48sqrt(2)). Substitute into D12 and
use the cubic sine remainder for its multiplication term. If kappa_a=0,
J_a(lambda kappa) is exactly zero; no division by kappa_a is needed.

The compression of L_a to the entire zero space is

    calJ_a=Pi L_a Pi=[ m_a I_F       r_a ],
                      [ <r_a|        1   ],
    m_a(q)=cos(2q_a),
    r_a(q)=s_a(e_a-n_a n)/(2sqrt(I0)).                       (D15)

Here multiplication by m_a preserves transverse fields. Fv=0,
<v,zeta>=1/(2sqrt(I0)), and
<v_a,zeta>=1/(6sqrt(I0)). Thus the transverse cross term is
Fv_a/(2sqrt(I0)). The lower-right entry retains the exact canonical
cancellation:

    <zeta,(cos(2q_a)-1)zeta>=-1/(6I0),
    <zeta,(|v_a><v|+|v><v_a|)zeta>=+1/(6I0).                (D16)

For z=(u,alpha) in Z, the D15 quadratic form is

    integral m_a|u|^2+|alpha|^2
                  +2 Re[conjugate(alpha)<r_a,u>].          (D18)

On the entire physical zero space, sum_a r_a=0 and
sum_a m_a=3-2epsilon^2. Thus D15 gives, for any normalized (u,alpha),

    sum_a <(u,alpha),calJ_a(u,alpha)>
                    =3-2 integral epsilon^2|u|^2.          (D19)

Write z(tau)=exp(-i tau A_kappa)z for the following cyclic argument.

Take kappa=k(1,1,1), k nonzero, and z=zeta. The even cyclic permutation
of the three coordinates is a proper rotation. In triplet coordinates
it acts as u(q)->R u(R^(-1)q), preserves zeta, commutes with A_kappa,
and cyclically permutes calJ_a. Cross products transform covariantly
under this rotation. No improper-rotation spin convention is needed.
The three expectations are therefore equal, so for all real tau

    <z(tau),calJ_a z(tau)>
             =1-(2/3)||epsilon u(tau)||^2,   a=1,2,3.       (D20)

The compression D15 is

    calJ_a=[ m_a I_F       r_a ],
           [ <r_a|          1  ],
    m_a=cos(2q_a),
    r_a=s_a(e_a-n_a n)/(2sqrt(I0)),
    ||calJ_a||<=1+sqrt(3).                                 (W10)

It comes from the named compressed local energy placement; it is not
defined by differentiating A with respect to kappa. W7 and boundedness
show that its expectation has the same limit as on `(exp(-itD)u_+,0)`.
Both off-diagonal terms have zero expectation on that comparison vector.
The scalar multiplier m_a commutes with D, so

    <exp(-itA)zeta,calJ_a exp(-itA)zeta>
        -> j_(a,+):=integral cos(2q_a)|u_+(q)|^2 dmu
         =1-2W_(a,+),
    W_(a,+):=||sin(q_a)u_+||^2,
    0<W_(a,+)<1,        sum_a W_(a,+)=W_+.                 (W11)

The strict bounds hold for every coordinate a: each zero set of sin q_a
and each set where `sin^2 q_a=1` has three-dimensional measure zero.
Thus `-1<j_(a,+)<1` and the coefficient changes strictly from its initial
value 1. Quantitatively the comparison error is at most
`2(1+sqrt(3))r_+(t)`. No decay rate for r_+ is supplied by W1.

For diagonal `kappa=k(1,1,1)`, k nonzero, the proper cyclic
symmetry just proved makes the three expectations equal at every time. Hence their
limits obey `W_(a,+)=W_+/3`, and

    j_(a,+)=1-(2/3)W_+,      a=1,2,3.                     (W12)

This establishes a persistent, nonzero limiting deficit. It does not fix
whether the final coefficient is above or below zero: W9 alone permits
either sign. In particular the word positive in this note describes the
weighted transfer W_+, not a universal direction or positivity of current.

## 11. Ordered limits for a fixed dressing preparation

In this section lambda denotes only the weak-momentum parameter; the band
parameter used from Section 12 onward is separate. The companion's finite
spectral-cutoff comparison implies, for each fixed z in Z and fixed finite T,
sup_(|t|<=T)||exp[-it H_D(lambda kappa)/lambda]z-exp(-itA)z||->0.
It is a strong fixed-vector statement, not uniform convergence over Z's unit
ball. All current operators below are the bounded extensions in Section 10.

For the fixed dressing vector and each fixed compact interval of t, the
companion proves strong convergence of
`U_lambda(t)=exp[-it H_D(lambda kappa)/lambda]` to `exp(-itA)` as
lambda tends to zero. Since F is bounded, E24 implies the ordered limit

    lim_(t->infinity) lim_(lambda->0) ||F U_lambda(t)zeta||^2=1.
                                                                  (E29)

This is not a joint-limit bound or a large-time theorem at a fixed nonzero
lambda. The earlier source exhibits failure of uniform state convergence over the
zero-space unit ball; the companion's vector-dependent compact-time bound
supplies no automatic interchange with this infinite-time limit.

Let `U_lambda(t)=exp[-it H_D(lambda kappa)/lambda]`. The companion's fixed-vector
strong limit and current expansion give, for every fixed compact t interval,

    <U_lambda(t)zeta,J_a(lambda kappa)U_lambda(t)zeta>/lambda
          ->kappa_a <exp(-itA)zeta,calJ_a exp(-itA)zeta>.

Combining this with W11 proves exactly the ordered limit

    lim_(t->infinity) lim_(lambda->0)
      <U_lambda(t)zeta,J_a(lambda kappa)U_lambda(t)zeta>/lambda
                      =kappa_a[1-2W_(a,+)].              (W13)

The initial scaled current tends to kappa_a. The corresponding ordered
limit of its change is therefore

    Delta_(a,+)=-2kappa_a W_(a,+).                         (W14)

It is nonzero, with sign opposite to kappa_a, whenever kappa_a is nonzero.
If kappa_a=0 the actual a-th current is identically zero, as in the parent.
For diagonal kappa, W14 becomes `-(2k/3)W_+`.

The separation of errors is explicit. Put
`E_lambda(t)=||U_lambda(t)zeta-exp(-itA)zeta||` and use D14 with

    C_a(kappa)=(1/6+sqrt(3)/24)|kappa_a|^3+|kappa_a|b^2/8.

Then the absolute difference between the finite-lambda expression in W13
and its limiting right side is at most

    lambda^2 C_a(kappa)
      +2|kappa_a|(1+sqrt(3))[E_lambda(t)+r_+(t)].           (W15)

The two errors vanish in different proved regimes: E_lambda on fixed
compact t intervals as lambda tends to zero, and r_+ as t tends to infinity
at fixed kappa. These ordered estimates alone justify no joint schedule, finite-lambda
onset, rate, or reversed order. The physical walk time is t/lambda. There
is no assertion of global trace class after a total-momentum direct integral.
The joint theorem below instead uses the finite all-time comparison and a
specific actual positive-free-band preparation with a global envelope.

When kappa=0, the effective dressing remains a zero eigenvector. W5 fails,
and this scattering preparation argument is inapplicable. That case is
excluded explicitly rather than forced into W9 or W14.

## 12. Actual band preparation and finite comparison hypotheses

From this point lambda is the free-band parameter, delta is the independent
weak-momentum parameter, and tau is effective time, with physical time
t=tau/delta. Fix kappa0=(1,1,1) and b=|kappa0|=sqrt(3). All absolute
continuity and weighted conclusions above apply at this fixed kappa0.

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

All these are explicit normalized L2 vectors. Sharp spectral endpoints
are permitted. They require no Cook smoothness assumption. Equations
L6–L8 give

    w_lambda=lambda/(8pi^2 I0) [1+O(lambda^2)],
    beta_lambda^2=9lambda^3/(32pi^2) [1+O(lambda^2)].       (L10)

The constants follow by integrating E^0 and E^1, respectively; more
explicitly beta_lambda=(I0 w_lambda)^(-1/2) integral_I rho(0,E)/E dE.

The O(lambda^2) remainder follows uniformly from the displayed Jacobian
on 0<E<=7lambda/4. Together with n_lambda^2=1-O(lambda^3), these identities
give the following form used by the joint comparison.

For 0<lambda<=1/16, let phi_lambda be the normalized free spectral slice of
zeta on [5lambda/4,7lambda/4], chi_lambda=P phi_lambda/n_lambda, and
A_lambda=<zeta,chi_lambda>. Q13 and L10 give

    F chi_lambda=0, Pi chi_lambda=A_lambda zeta,
    sqrt(lambda)/12 <= A_lambda <=2sqrt(lambda), A_lambda<=1,
    A_lambda^2/lambda=1/(8pi^2 I0)+O(lambda^2).             (G1)

The last identity follows from L10 and n_lambda^2=1-O(lambda^3), not a
numerical threshold fit. All torus integrals retain dq/(2pi)^3.

The finite all-time estimates used next are proved in Sections 3–4 of the
projected-band companion. We reproduce their exact hypotheses and formulas;
the present proof does not substitute a fixed-time limit at a growing T.
Use H_*=H_D(0), F, Pi and Q=P-Pi from Q3.

For fixed kappa put b=|kappa|, d_j=kappa_j cos q_j and

    B_kappa u=i d cross u, B_kappa kills the singlet,
    H_D(delta kappa)/delta=H_*/delta+B_kappa+R_delta,
    ||R_delta||<=r_delta=delta b^2/4+delta^2 b^3/24,
    A_kappa=Pi B_kappa Pi, U_delta(tau)=exp[-i tau H_D(delta kappa)/delta].
                                                               (Q5)

For 0<lambda<=1/16, a=5/4, x=Q chi_lambda and
0<sigma<=min(1/2,a lambda/2), define

    C_lambda=2/(a lambda n_lambda)+beta_lambda sqrt(I0)/n_lambda.

The cutoff inverse in the companion retains the singlet mean subtraction
and the longitudinal contact term. It yields

    ||E_sigma x||<=2A_lambda sqrt(sigma)/sqrt(I0)+sigma C_lambda,
    C_lambda<=4/lambda.                                  (Q15)

For the last inequality, Q13 and sqrt(I0)<2 give
C_lambda<=16/(5lambda)+2<4/lambda on the stated lambda range.

For the dressing orbit, the companion's longitudinal cutoff inverse gives

    sup_(|tau|<=T)||E_sigma Q B_kappa exp(-i tau A_kappa)zeta||
        <=(7/2)(b^2 T/sqrt(I0))sqrt(sigma), 0<sigma<=1/2.

Together with its two finite evolution comparisons, this proves the next
estimate for every finite T>0, every delta>0 and the cutoff domain just
specified. Here u(tau)=F exp(-i tau A_kappa)zeta, as in E3. In particular,
T has not been fixed before this bound is applied. The supremum defining
e_perp is over |tau|<=T.

    e_perp:=sup ||F U_delta(tau)chi_lambda
                           -A_lambda u(tau)||
     <= delta[ A_lambda(2b+2Tb^2)+(2b+Tb^2)]/sigma
        +A_lambda[4+(7/2)b^2T^2]sqrt(sigma)/sqrt(I0)
        +2sigma C_lambda+(A_lambda+1)T r_delta.          (Q16)

The fast complementary evolution has been annihilated by F, not discarded
by a phase average. All displayed bounds are finite for their stated
parameters, so sigma may now be chosen as a function of lambda and delta.

The actual-current trace needed with this comparison also holds on the full
physical space, not just Z:

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

At the diagonal kappa0=(1,1,1), the proper cyclic coordinate rotation acts on
triplets by u(q)->R u(R^(-1)q), and on singlets by f(q)->f(R^(-1)q).
It preserves the measure and chi_lambda, commutes with H_D(delta kappa0),
and permutes the three L_a. Their expectation changes therefore agree.
Initially F chi_lambda=0.

The operator-norm remainder D14 and the trace identity are time independent.
They can therefore be combined with Q16 on any finite interval, as done
next. They require no unbounded observable applied to chi_lambda.

## 13. A growing effective-time comparison and actual current

The fixed-fiber conclusions W7 and W9 give exactly

    ||exp(-i tau A)zeta-(exp(-i tau D)u_+,0)||->0,          (G2)
    W(tau)=||epsilon u(tau)||^2->W_+=||epsilon u_+||^2,
    ||u_+||=1,                 0<W_+<3.                  (G3)

The proof is Sections 8–9: the reverse wave-operator limit and E23 supply
the norm-one datum, and epsilon^2 commutes with D. Nothing here assumes
a rate for this limit or a uniform positive lower weight over unit vectors.

Choose any fixed gamma with 0<gamma<1/2 and set

    delta=lambda^3, sigma=lambda^2, T_lambda=lambda^(-gamma),
    p=1/2-gamma>0.                                       (G4)

Use U_delta(tau)=exp[-i tau H_D(delta kappa0)/delta]. The Q16 bound is
finite for every T and was proved before T was specialized to 1/20.
Its spectral-cutoff domain holds because sigma<=min(1/2,5lambda/8).
With b=sqrt(3), r_delta=3delta/4+3sqrt(3)delta^2/24<=delta, it gives

    e:=sup_(|tau|<=T_lambda)
          ||F U_delta(tau)chi_lambda-A_lambda u(tau)||,

    e/A_lambda <=108 delta T_lambda/(sigma sqrt(lambda))
             +58 T_lambda^2 sqrt(sigma)
             +96 sigma/lambda^(3/2)
             +13 T_lambda delta/sqrt(lambda)
       =108lambda^p+58lambda^(2p)+96lambda^(1/2)
                                      +13lambda^(2+p)
       <=275lambda^p.                                   (G5)

For the first term, divide Q16 by A_lambda and use b<2, T>=1 and
1/A_lambda<=12/sqrt(lambda): (4+8T)+(4+4T)/A_lambda is at most
108T/sqrt(lambda). For the second use I0^(-1/2)<4 and
4[4+(21/2)T^2]<=58T^2. The last two terms use C_lambda<=4/lambda,
A_lambda<=1 and the same lower bound on A_lambda. Thus no fixed-vector
limit or compact-time convergence is substituted for the finite estimate.
The inequalities also make clear why gamma must be strictly below 1/2
for these particular scale choices.

### Actual current comparison, valid at every finite time

For the diagonal fiber the checked full-space identity is

    sum_a L_a=3P-H_*^2/2-2epsilon^2 F,
    ||J_a(delta kappa0)/delta-L_a||<=((13+sqrt(3))/24)delta^2.

The initial state and evolution are cyclically invariant, so all three
changes of <L_a> agree. Initially F chi_lambda=0. Conservation of the
actual H_D(delta kappa0)^2 gives

    |Delta <H_*^2>|<=8sqrt(3)delta(sqrt(3)+r_delta).

These facts hold for every time, not only 1/20. The norm error in G5
also gives | ||epsilon F U_delta chi_lambda||^2-A_lambda^2 W(tau)|
<=3e(2A_lambda+e). Combining both signs of these inequalities proves

    |Delta<J_a>/delta+(2/3)A_lambda^2 W(tau)|
                           <=4A_lambda e+2e^2+8delta      (G6)

for |tau|<=T_lambda. For the last constant the energy-square error divided
by six is at most 4delta+(8/3)delta^2; twice the current remainder is at
most (5/4)delta^2, whose sum is below 8delta when delta<=1.

In particular, at tau=T_lambda, G1,G5-G6 give

    Delta<J_a>/(delta lambda)
       =-W(T_lambda)/(12pi^2 I0)+O(lambda^p), a=1,2,3.    (G7)

One direct finite error budget before replacing A_lambda^2/lambda by its
limit is 16 E_lambda+8 E_lambda^2+8lambda^2, where E_lambda=275lambda^p.
The O(lambda^2) band-weight remainder is bounded using W<=3.

## 14. A genuine global actual free-band preparation

The following finite-K estimates, proved by direct projector comparison and
bounded Duhamel in the companion, are used before taking the direct integral.

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

On |kappa-kappa0|<=1/10 and 0<delta<=1, the exact current gives
||J_a(delta kappa)/delta||<=4 and Lipschitz constant 4 in kappa. Indeed the
multiplication term costs |kappa-kappa0|. The two rank-one terms together
cost at most (sqrt(3)+delta/2)|kappa-kappa0|, using
||h||<=sqrt(6),
||h'_a(delta kappa)-h'_a(delta kappa0)||<=delta|kappa-kappa0|/(2sqrt(2)),
||h(delta kappa)-h(delta kappa0)||<=delta|kappa-kappa0|/sqrt(2), and
||h'_a(delta kappa0)||<=delta/(2sqrt(2)). Their sum is less than four.
The norm bound follows from
(1+sqrt(3))|kappa_a|<=1.1(1+sqrt(3))<4.
Also ||H_D(K)-H_D(K0)||<=|K-K0|, so for every finite tau,

    ||U_(delta,kappa)(tau)-U_(delta,kappa0)(tau)||
         <=|tau||kappa-kappa0|.                           (B20)

This is the same bounded-Duhamel estimate used in G9; unlike the companion's
single-time application, it is kept here at its arbitrary finite time.

Let h be any fixed smooth unit vector in L2(dy/(2pi)^3), supported in
the unit ball and nonzero on an open set. Set eta_lambda=lambda^2 and

    f_lambda(kappa)=eta_lambda^(-3/2)
                         h((kappa-kappa0)/eta_lambda).

For |K|<=lambda/16, take the checked actual free-band vector
phi_(lambda,K)=Pi_++(K)phi_lambda/||Pi_++(K)phi_lambda||. Define

    Phi_lambda(K,q)=delta^(-3/2)f_lambda(K/delta)phi_(lambda,K)(q),
    Chi_lambda=P Phi_lambda/||P Phi_lambda||.              (G8)

This is one global contact normalization. The free packet has norm one
and lies in the actual positive [lambda,2lambda] free band. Its physical
norm before normalization lies between 1-lambda^3/3 and 1 in squared norm.
Its total-momentum center is lambda^3(1,1,1), with radius lambda^5; it has
nonempty three-dimensional support away from zero. Since lambda<=1/16,
the support lies in |K|<=lambda/16 and |kappa-kappa0|<=1/10.

For every finite tau, bounded Duhamel and the exact current estimates B20
give ||U_(delta,kappa)(tau)-U_(delta,kappa0)(tau)||<=|tau||kappa-kappa0|,
current norm at most 4 after division by delta, and current Lipschitz
constant 4. At fixed initial chi_lambda the scaled current drift therefore
changes by at most 8(1+|tau|)|kappa-kappa0|. Replacing this vector by
chi_(lambda,delta kappa) costs at most 512delta/lambda, by Q28 and B20.
After division by lambda the uniform errors at T_lambda are at most

    8(1+T_lambda)eta_lambda/lambda+512delta/lambda^2
                      =520lambda+8lambda^(1-gamma)=o(lambda^p). (G9)

The actual kappa weights after the single projection are
|f_lambda|^2 n_(lambda,delta kappa)^2/||P Phi_lambda||^2. They are positive,
integrate to one and stay inside this ball. Integrating a uniform error
against those exact weights preserves G7 without replacing their law.

Let Psi_lambda(t)=exp(-it H_D)Chi_lambda in the full direct integral.
At the common physical time t_lambda=T_lambda/delta=lambda^(-(3+gamma)),

    [<Psi_lambda(t_lambda),J_a Psi_lambda(t_lambda)>
       -<Chi_lambda,J_a Chi_lambda>]/lambda^4
       =-W(lambda^(-gamma))/(12pi^2 I0)+O(lambda^(1/2-gamma))
       ->-W_+/(12pi^2 I0)<0,             a=1,2,3.         (G10)

This is a joint limit along explicit polynomial scales. G3 supplies its
strict limiting sign; G5-G9 control the original walk at the growing time.
An example is gamma=1/8, t_lambda=lambda^(-25/8), comparison error
O(lambda^(3/8)). The convergence of W itself has no proved rate, so G10
does not give an explicit numerical onset for the final sign.

## 15. Regulated outgoing datum and an explicit selected-datum lower bound

The exact memory, scattering and growing-time premises needed for this
extension have been proved or explicitly imported above. The next argument
uses positive-regulator resolvents only, and retains every power and constant
in the frozen R1–R14 derivation. It gives no scattering-time estimate.
The delta in R11–R12 is the local spectral edge margin of E20. The packet's
weak-momentum delta is separately specified in the R14 consequence.

All q integrals use dmu=dq/(2pi)^3 on the three-torus. Set s_j=sin q_j,
epsilon=|s|, n=s/epsilon almost everywhere, and

    I0=integral (4epsilon^2)^(-1),  1/12<=I0<=9/8,
    Z=F direct-sum C,   zeta=(0,1),
    d_j=kappa_j cos q_j,  b=|kappa|>0,  f=d dot n,
    J=i n cross,  D=f J,
    g=i(d cross n)/(2epsilon sqrt(I0)),
    G=|g|^2=(|d|^2-f^2)/(4epsilon^2 I0),
    A=[D,g;g*,0],   A0=[D,0;0,0].                         (R1)

F is the physical odd transverse L2 triplet space. On each transverse
fiber J is self-adjoint, J^2=I and g*Jg=0. D is bounded self-adjoint;
A is the physical zero-space compression and ||A||<=b. The scalar zeta
coordinate is the physical dressing vector, not an auxiliary singlet.

Sections 2–5 prove, for exp(-itA)zeta=(u(t),a(t)),

    u(t)=-i integral_0^t exp[-i(t-s)D]g a(s) ds,
    a(t)->0, a'(t)->0,
    M(z)=<zeta,(z-A)^(-1)zeta>=1/[z-Sigma(z)],
    Sigma(z)=integral G z/(z^2-f^2) dmu.                  (R2)

Its dressing spectral measure is an even absolutely continuous probability
measure on [-b,b]. Sections 8–9, using the checked trace-class
wave-operator theorem on this same Z, supply a vector u_+ in F with

    ||u_+||=1,
    ||(u(t),a(t))-(exp(-itD)u_+,0)||->0,
    W(t)=||epsilon u(t)||^2 -> W_+=||epsilon u_+||^2.       (R3)

R3 is a premise of this extension, not inferred from scalar decay alone.
The given walk, pair space, exclusion, canonical energy placement and
continuous generator clock are unchanged. The argument introduces no
new physical axiom, bath reset, statistical independence or Markov law.

### Abel representation on the exact physical space

For h>0 let w(t)=exp(itD)u(t). It has norm at most one and tends strongly
to u_+ by R3. Its exponential average therefore obeys

    u_h:=h integral_0^infinity exp(-ht)w(t) dt ->u_+,
    ||u_h||<=1.                                          (R4)

Indeed, split the integral of ||w(t)-u_+|| at any fixed T. Its part up to T
is at most 2(1-exp(-hT)), while the tail is bounded by
sup_(t>=T)||w(t)-u_+||. First choose T, then let h decrease to zero.
This proves norm convergence without assuming an integrable decay rate.

Insert R2 into R4 and interchange the two integrals. The norm of the
absolute majorant is at most
h integral_0^infinity exp(-ht)t||g||dt=||g||/h, so the Bochner interchange
is valid for every h>0. The exact result is

    u_h=-i integral_0^infinity exp(-hs)exp(isD)g a(s) ds
       =M(D+ih)g.                                        (R5)

The last equality follows from the spectral theorem for bounded A:
-i integral_0^infinity exp(izs)a(s)ds=M(z) for Im z>0.
Applying the bounded functional calculus of D then gives R5. No boundary
value of M on the real axis is used, and no singular inverse is taken.

Pointwise on the transverse fiber put P_+=(I+J)/2 and P_-=(I-J)/2.
These are orthogonal projections, with |P_+g|^2=|P_-g|^2=G/2. Thus

    u_h(q)=M(f(q)+ih)P_+g(q)+M(-f(q)+ih)P_-g(q),
    |u_h(q)|^2=(G/2)(|M(f+ih)|^2+|M(-f+ih)|^2)
               =G|M(f+ih)|^2.                            (R6)

Evenness of the dressing measure gives M(-x+ih)=-overline(M(x+ih)),
which proves the last equality, including x=0. Although the individual
helicity labels swap under q to -q, f also changes sign, so the sum is
an odd physical field; no enlargement of F is being assumed.

For every bounded real even scalar weight m(q), R4-R6 give the regulated
integral formula

    integral m|u_+|^2
       =lim_(h down to 0) integral m(q)G(q)|M(f(q)+ih)|^2 dmu,
    |integral m|u_h|^2-integral m|u_+|^2|
       <=2||m||_infinity ||u_h-u_+||.                     (R7)

In particular m=1 gives a limit of one; m=epsilon^2 gives W_+; and
m=sin^2 q_a gives each canonical-current coefficient W_(a,+). Every
integral at h>0 is well defined because |M(x+ih)|<=1/h and G is integrable.
R7 does not authorize exchanging a pointwise h-limit with q integration,
removing the regulator in numerical quadrature, or assigning an error rate.

### A uniform upper bound on the second energy moment

Let eta_g=||g||^2. Separate the diagonal and mixed kappa terms in G.
Each mixed term integrates to zero: reflecting one of its q coordinates
changes the corresponding sine sign while preserving cosines, epsilon
and the torus measure. The remaining expression is

    eta_g=(1/(4I0)) sum_j kappa_j^2
                  integral cos^2(q_j)(1-n_j^2)/epsilon^2
          <=(2/3)b^2.                                    (R8)

For the inequality, use cos^2(q_j)<=1. Permutation symmetry of the
normalized torus gives
integral n_j^2/epsilon^2=(1/3)integral epsilon^(-2), and
integral epsilon^(-2)=4I0. These integrals are finite by the cone bound.
Only lattice permutations and coordinate reflections are used, not a
continuous rotational symmetry of the supplied dispersion.

The outgoing datum has exactly this second energy moment:

    ||D u_+||^2=eta_g.                                   (R9)

Here is a direct proof, avoiding any extra wave-operator import. Set
psi(t)=(u(t),a(t)). The difference (A-A0)psi(t)=(a(t)g,<g,u(t)>) has
squared norm eta_g|a(t)|^2+|a'(t)|^2 by the scalar block equation.
It tends to zero by R2. Conservation gives ||A psi(t)||=||A zeta||
=sqrt(eta_g), so ||D u(t)|| tends to sqrt(eta_g). Since D is bounded
and R3 compares u(t) with exp(-itD)u_+, the same norm tends to ||D u_+||.
This proves R9. On transverse fibers D^2=f^2 I.

Let R be the scalar projection 1_(|f|<=7b/8) on F. Chebyshev's inequality
applied to R9 and then R8 gives the fixed interior-energy mass

    ||R u_+||^2 >=1-eta_g/(7b/8)^2
                  >=1-128/147=19/147=:m0.                (R10)

Thus a fixed positive part of the outgoing norm lies at interior energies.
No estimate on the endpoint density, spectral gap or Fourier decay rate
is assumed in this step.

### Interior mass cannot all concentrate at the cones

Equation E20 supplies, for chi=delta/b in (0,1),

    |M(x+ih)|<=C_delta=32768 pi I0/[b chi^(3/2)]
    whenever |x|<=b-delta, 0<h<=delta/2.                  (R11)

Use delta=b/8, hence chi=1/8. For 0<r<=1/2 let Q_r=1_(epsilon<r).
The cone estimate Q4 is integral_(epsilon<r)epsilon^(-2)<=r.
For 0<h<=b/16, R6 and R11 therefore imply

    ||Q_r R u_h||^2
       <=C_(b/8)^2 integral_(epsilon<r)G
       <=C_(b/8)^2 b^2 r/(4I0)
        =2^37 pi^2 I0 r
       <=K0 r,     K0:=90*2^34=1546188226560.             (R12)

The last relaxation uses I0<=9/8 and pi^2<10. All projections in R12
are bounded and commute, so the strong limit R4 proves the same bound
with u_+ in place of u_h. This passage needs no pointwise limit of M.

Choose r_*=m0/(2K0)=19/454579338608640, which is between zero and 1/2.
Subtract R12 from R10 to obtain
||(1-Q_(r_*))R u_+||^2>=m0/2. Since epsilon>=r_* on this set,

    W_+>=r_*^2 m0/2=m0^3/(8K0^2)=:c0,
    c0=6859/60752858276421362793738298982400
       >1.128*10^(-28).                                  (R13)

The rational expression is the certified value; the decimal is only a
conservative readable bound. This is uniform over fixed kappa!=0 because
the powers of b cancel in R12. It is a bound on the actual outgoing data
selected by the dressing preparation, not a lower bound for arbitrary
unit vectors in F. The latter can concentrate arbitrarily near a cone.

Together with W9, 0<c0<=W_+<3. This bound does not fix
the sign of the final canonical current 1-(2/3)W_+ for diagonal kappa,
nor give a useful physical magnitude estimate or an optimal constant.

### The prepared-packet consequence and scope

For the already constructed family in G1-G10, fix any 0<gamma<1/2,
delta=lambda^3, sigma=lambda^2, effective time T=lambda^(-gamma), and
kappa-envelope radius lambda^2 about (1,1,1). Its actual positive free-band
packet is contact-projected and globally normalized once. Physical time
is lambda^(-(3+gamma)), center lambda^3(1,1,1), and radius lambda^5.
The checked comparison there is

    Delta<J_a>/lambda^4
       =-W(lambda^(-gamma))/(12pi^2 I0)
          +O(lambda^(1/2-gamma)),    a=1,2,3.

Using the G1–G10 premises established in Sections 12–14, R13 gives

    lim_(lambda down to 0) Delta<J_a>/lambda^4
       =-W_+/(12pi^2 I0) <=-c0/135 <0.                   (R14)

Here 12pi^2 I0<=135 by the same elementary bounds. The denominator 135
and c0 are explicit, but the onset in lambda is not: no rate for
W(T)->W_+ is established. The O term bounds comparison to the moving
W(T), not all of the error from its limiting value.

The theorem concerns this supplied effective generator and the specified
prepared-packet family. It proves no generic-current decay law, collision
frequency, Boltzmann closure, monotonicity, incoherent state or new physical
primitive. The finite-bath recurrence counterexample in Section 7
remains valid: norm-one outgoing data require the absolutely continuous
scattering input R3, not only the algebraic resolvent identity R5.

## 16. Distinct finite controls and preserved limitations

The finite-bath recurrence E27–E28 remains a counterexample to inferring
continuum decay from the block form alone. A separate exactly solvable
continuous toy checks the outgoing convention and weighted expectation
without purporting to solve the continuum walk:

In that control, take `F_toy=L2([-1,1],dx/2)`, `D_toy=x`, the normalized
constant f0=1, and an extra scalar vector zeta0. Let U swap f0 and zeta0
and fix their orthogonal complement, and set
`A_toy=U(D_toy direct-sum 0)U*`. With h0=x one computes

    A_toy-A_(0,toy)
      =|h0><zeta0-f0|+|zeta0-f0><h0|,
    exp(-itA_toy)zeta0=(exp(-itx)-a0(t),a0(t)),
    a0(t)=sin(t)/t,
    ||exp(-itA_toy)zeta0-(exp(-itx),0)||=sqrt(2)|a0(t)|.
                                                                  (W16)

These formulas follow directly from U; the asymptotic conclusion does
not invoke Kato in this check. The free datum is f0 with norm one.
For the positive weight x^2, exact integration gives

    integral x^2|exp(-itx)-a0(t)|^2 dx/2
       =1/3+a0(t)^2/3+2a0(t)a0''(t) ->1/3.                (W17)

Symbolic integrations, the continuous norm identity, and separate numerical
quadrature check these formulas. This is an independently designed toy
control, not a numerical solution of the continuum walk or a proof of
Kato's theorem. The finite-dimensional matrix tests do not assert existence
of finite-grid scattering limits. The frozen finite-bath recurrence example
continues to apply to such an unsupported extrapolation.

Failed or unused routes are retained: dropping g freezes the dressing
artificially; a zero-frequency damping substitution changes E5; finite
bath recurrence cannot establish continuum decay; positivity of a bath
density only almost everywhere would not by itself exclude singular
dressing measure; excluding endpoint atoms needs E22 separately; and
unweighted probability does not determine the epsilon-weighted current.
The successful argument uses the stronger uniform local Poisson bound
E20 and does not assume absence of an eigenstate in advance.

The route would have remained incomplete without W5: completeness of the
wave operators does not put an arbitrary vector in ac(A). Keeping only
existence of a forward wave operator would also omit the onto-ac statement
needed for the norm-one outgoing datum. Both premises are explicitly
present here. Positivity almost everywhere alone supplies a strict weight for
that datum, but no numerical coercivity constant. Section 15 obtains the
selected-datum lower bound by its additional moment/resolvent argument;
there is still no positive coercivity constant for arbitrary unit fields. No universal relaxation
law or broad impossibility statement is proposed.

The joint theorem resolves the previously open weighted and growing-time
interfaces only for the stated construction. Section 15 supplies the explicit
selected-datum lower bound c0. Still open here are a rate for the outgoing-state
comparison or W(t)-W_+, evaluation beyond that conservative lower bound,
and extensions to arbitrary projected positive-band data.
There is no claim about optimal exponents, fixed-density gases, the regime
K comparable to lambda, monotonic current or generic unitary dissipation.
The earlier leakage and nonuniform-state-convergence findings remain
preserved research; they are not broadened into impossibility claims.

The separate spectral-edge work is not a source or conclusion of this
publication candidate.

## 17. Evidence, exact sources and publication status

The primary is `scripts/excluded_walk_memory_current_2026_10_11.py`.
It embeds the five complete frozen author helpers byte-for-byte, verifies
their identities, and executes each in a fresh namespace. Its source blocks
are memory_controls.py, mean_controls.py, weighted_controls.py and
scale_controls.py, followed by outgoing_controls.py, from the source map.
They retain their original exact
symbolic, rational and explicitly floating controls; no helper has been
rewritten to mirror this composition.

The memory controls check direct Schur inverses, finite-bath evolution and
Volterra convolution, moment recurrences, eliminated-field quadratures,
cone constants and selected geometry samples, and a Poisson interval bound.
The mean controls check the integration constant and an unrelated continuous
sinc measure. The weighted controls check the rank-two trace norm, adjoint
convention, continuous toy and current cross term. The scale controls check
the stated exponent budgets and an exact nonuniform normalization fixture.
The outgoing controls check exact finite Abel/resolvent algebra, the helicity
measure and R8–R14 rational constants, including a finite-bath counterexample
to dropping the unit-outgoing-state premise. They do not infer continuum
scattering from that bath.
These are author controls. Their replay is not an independent proof of
absolute continuity, Kato completeness, or the infinite-time walk theorem.
The uniform cone and singular-measure arguments are the analytic proofs in
Sections 4–5, and the growing-time conclusion uses the finite estimates in
Sections 12–14.

The reconstructable `memory_current_composition/SOURCE_COMPOSITION.json`
records every retained line range and literal editorial addition. Source
identities are:

| Source | SHA-256 | Role |
|---|---|---|
| Effective memory source | `b667b092d202f3657493983e284ff94b5c02c929e6bc8508c691d6155865567c` | Complete E1–E29 proof chain and recurrence limitation |
| Weighted memory source | `10991ee05a61e3fcd2931b9cd90de007c2c2848771450db787e4634dcce3d324` | Complete W1–W17 import, scattering, current and toy arguments |
| Joint-scale source | `4d6c82f7c46e0ae1a34f8c0c4ebdab90361ab6f3753a5bf95e89e7d40694c278` | G1–G10 scale, current and global-preparation proof |
| Outgoing-resolvent source | `58a96a049701667e673bde1acf98e5346356483101654b3464fe11e94fd02c21` | Complete R1–R14 selected-datum formula, moment, cone and lower-bound proof |
| Projected-band companion source | `ecb7eacddc0a11b2636030ed5e4759fabb9945568f3f3f4699f650463f5bf969` | Physical contract, all-time finite estimate and explicit band/current inputs |
| Degenerate source | `b8f923be6e50de14ba0bb1a35ccfd71aec7575fd710693535cf0417c76daa876` | Reproduced current compression, cyclic argument and nonzero coupling proof |
| Long-time source | `09998aec1dafc9198609237dce2238bc672182d6c1baca3294b8772a5888c324` | Reproduced leading band-weight and contact-loss asymptotics |

The complete memory review is
`c8dbb7860af01dc8c8d0203e23a9bfe34cc26c0895cace0c51af46f3f70669e0`;
the complete weighted review is
`a2bb951a15a90ca8dba4cba928f6307fdde078f30a41f9f07e818561f7bf0484`;
the complete joint review is
`2867fc1179a7b82b095e7719bc2f9015fdd87b5190626f61b0adfbd4fc318bf6`;
the complete outgoing-resolvent review is
`8eb1d81e91227a0cda36e75459e32be80b1523709a5f82fc5af4c1e8fd6d74de`.
The joint review's originally pending weighted-review dependency is updated by a
separate source-bound addendum, leaving the frozen original report unchanged.
These reviews found no consequential defect within their exact scopes. The
weighted review covers the fixed-fiber and ordered-limit result; the joint
review separately covers the all-time substitution, current errors and
single global normalization. Neither source status nor a passing helper is
an independent retained-status audit of this new publication composition.
The outgoing review independently checks the new root-authored R1–R14
extension while reusing its reviewer's own earlier author sources only as
explicit premises, with their separate independent reviews. It does not
independently certify those earlier authored proofs by reusing them.

The exact primary Kato PDF has SHA-256
`12ce9d67ed67d096f82b55a6ef7b778a83c16d5e2f020d4946d58112f3f93fe5`.
The theorem and reverse-limit/onto-ac argument were checked in the original
pages 260 and 263. The general trace-class theorem is an explicit imported
mathematical result. It is not reproved by the finite toy or controls.

The external composition receipt records source identities, complete changed
argument coverage and actual primary replay separately from historical
evidence. New mutation runs, Lean coverage and formal audit outcomes must be
reported by their own execution records; none is inferred here. The supplied
physical contract, actual-current placement and companion finite-estimate
dependency remain explicit conditional support.

The exact earlier three-source candidate and executed four-helper primary
are preserved under `memory_current_composition/pre_extension/`, with an
original-to-recovery path index. The updated composition map records every
extension edit. The spectral-edge work remains outside this source boundary.

## Publication evidence and parent dependency

The [delivery checks](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/d8480b5a6e04102ff076b3dd6f817a2d43f20252/.claude/science/physics-loops/toe-projected-band-current-20261011/DELIVERY_CHECKS.md)
record final source identities, selective review coverage, canonical primary
execution and actual semantic source-copy controls. The primary is self-contained
apart from NumPy, SciPy and SymPy. Its finite controls and literal-helper replay
do not replace the continuum proof or independently certify it. No Lean proof
of the analytic memory/current theorem is asserted.

This milestone depends on the complete parent walk delta at
b9b032ae790c66e762a6296a1306bfb64ae7cd70. It must land after that parent or
receive cumulative review from main a13caa4885f547c8d206265b031ba7649e539fd9.
The separate flux/form and supplied stochastic transport branches are not
premises of these current and memory results.
