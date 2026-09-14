# Direct strong-scaling Maxwell field and charged Wilson-loop interactions

Personal derivation, 2026-09-14. Proposed, not independently reviewed.
This proof uses an explicitly stronger dimension-dependent scaling regime
than the preceding affine-covariance route. It does not use that provisional
affine estimate. The finite-clock law, its couplings and their scaling are
supplied; no fixed-alphabet phase, native law or charged matter is inferred.

## 1. Model, lifts and the target estimate

Let T_L=(Z/LZ)^4, with even L>=4 and V=L^4 vertices. Use canonical positive
cell orientations, ordinary sum inner products, and integer coboundaries
d_k. Write d=d_1, S=im_R d, K=d Z^E, P_e for the orthogonal projection
onto S, and P_perp=I-P_e. There are 4V edges and 6V plaquettes. Put

    r=dim S=3V-3, m=dim S_perp=3V+3.

These ranks follow from the Fourier symbol: each nonzero four-momentum
has exact two-form rank three, while the zero-momentum exact rank is zero.

For N>=2, clock links theta=2pi a/N have a in (Z/NZ)^E. Their probability
is proportional to the product of the supplied Villain weights

    phi_beta(u)=sum_n exp[-n^2/(2 beta)]exp(i n u)
              =sqrt(2pi beta)sum_k exp[-beta(u-2pi k)^2/2].

The positive lift has independent plaquette integers conditional on all
clock links. With representatives a_e in {0,...,N-1}, write

    y=d theta-2pi k, z=d a-N k,
    M_N=K+N Z^P, sigma=N^2/(4pi^2 beta), X=sqrt(beta)y=z/sqrt(sigma).

The number of representatives a that yield each z in M_N is
|ker(d mod N)|; k is then uniquely determined. Thus z has exactly the
centered discrete Gaussian law on M_N with variance parameter sigma.
This includes gauge and flat-holonomy multiplicities for composite N.

The finite-volume target, to be proved in sections 2–5, is

    | E exp(i<h,X>)/exp(-||P_e h||^2/2) - 1 |
       <= 2 exp(-pi^2 sigma/32)
          +4 exp(-pi^2 beta/16+||P_e h||^2/2),        (1.1)

provided

    beta >=16m log5/pi^2,
    sigma>=32r log5/pi^2,
    ||P_e h||<=pi sqrt(sigma)/8.                     (1.2)

The relative bound, rather than only an absolute characteristic-function
error, will control Wilson expectations that themselves tend to zero.

## 2. Integral cochain contraction and lattice saturation

On one periodic coordinate circle, define a degree-preserving integral
cochain projection p. For zero-cochains, (p f)(x)=f(0). For one-cochains,
(p u)(x)=1_(x=L-1)sum_t u(t). Define h:C^1->C^0 by

    (h u)(x)=sum_(0<=t<x)u(t), h u(0)=0.

The forward coboundary has (d f)(x)=f(x+1)-f(x), including the periodic
last edge. Direct telescoping gives

    d h=I-p on C^1, h d=I-p on C^0,

and p commutes with d. On the tensor product of the four coordinate
cochain complexes, use

    H=h tensor I tensor I tensor I
      +p tensor h tensor I tensor I
      +p tensor p tensor h tensor I
      +p tensor p tensor p tensor h,

with the usual degree sign when an h passes earlier one-form factors.
Then d H+H d=I-P, P=p tensor p tensor p tensor p: the four terms telescope.
All matrices have integer entries.

For a closed integer two-cochain n, P n has six coefficients, its integer
fluxes through the six coordinate two-tori at the other coordinates zero.
The represented cocycles are supported on the last edges in the two
form directions and are constant in the other directions. If n is real
exact, each such flux vanishes by telescoping around its two-torus.
Therefore P n=0 and n=d H n with H n integer. This proves the saturation
identity directly:

    K=Z^P intersect S.                              (2.1)

The same contraction shows that a closed integer two-cochain is an
integer exact cochain plus the indicated integral period cocycles. No
torsion-freeness theorem with unchecked cell conventions is required.

Let Lambda=P_perp Z^P in S_perp. It is a full-rank lattice in that
subspace: P_perp is a rational finite-dimensional matrix, its integer
images form a discrete finitely generated group, and those images span
S_perp. By (2.1), projection gives a bijection

    M_N/K  <->  N Lambda.                           (2.2)

Indeed every image is N P_perp n. If two representatives have the same
image, their difference is an integer cochain in S and hence belongs
to K. This injectivity rules out an unaccounted multiplicity of affine
curl cosets with the same perpendicular part.

## 3. Two uniform shortest-vector estimates

The scalar periodic Laplacian has symbol sum_mu 4sin^2(k_mu/2)<=16.
The cochain identity d_k* d_k+d_(k-1)d_(k-1)* equals this scalar
Laplacian on each component. In particular ||d_1||,||d_2||<=4.

For w in the dual lattice K* inside S, the condition <w,d a> in Z for
every integer one-cochain a is equivalent to d* w being integer.
If w!=0 then d* w!=0 because d* is injective on S. Hence

    1<=||d* w||<=4||w||, so ||w||>=1/4.              (3.1)

For a nonzero w=P_perp n in Lambda, n integer, either d_2 n!=0 or n is
closed. In the first case d_2 w=d_2 n is a nonzero integer cochain, so
||w||>=1/4. In the second case the coexact part vanishes, and w is the
harmonic projection of n. Closedness makes each coordinate two-torus
flux independent of the two transverse coordinates, by summing d_2 n=0
and telescoping. If those six fluxes are k_mu,nu in Z, the harmonic
constant component is k_mu,nu/L^2. Consequently

    ||P_h n||^2=L^4 sum_(mu<nu)(k_mu,nu/L^2)^2
               =sum_(mu<nu)k_mu,nu^2.              (3.2)

If w!=0 this is at least one. Thus every nonzero vector of Lambda also
has length at least 1/4. Equal four-dimensional sides are used in (3.2).
The ranks of K* and Lambda are r and m, respectively.

## 4. Dimension-dependent theta packing and exact-sector probability

Let Gamma be any rank-b Euclidean lattice with nonzero vector lengths
at least lambda>0. The disjoint radius-lambda/2 balls about its lattice
points in ||w||<(k+1)lambda lie inside the radius-(k+3/2)lambda ball.
Volume comparison bounds the number in that ball by (2k+3)^b. Therefore

    sum_(w!=0) exp(-t||w||^2)
      <=sum_(k>=1)(2k+3)^b exp(-t lambda^2 k^2).

For integer k>=1, 2k+3<=5^k<=5^(k^2). If t lambda^2>=2b log5, the last
sum is at most sum_(k>=1)exp(-t lambda^2 k^2/2). Since
t lambda^2/2>=b log5>=log2 when b>=1, the geometric-series comparison
gives

    sum_(w!=0)exp(-t||w||^2)<=2exp(-t lambda^2/2).    (4.1)

For a full-rank lattice Gamma in its real span and a centered Gaussian
parameter sigma, Poisson summation gives its shifted theta function as
a positive constant times

    sum_(w in Gamma*)exp(-2pi^2 sigma||w||^2)exp(2pi i<w,u>).

Nonnegative Fourier coefficients imply Z_Gamma(u)<=Z_Gamma(0) for every
real u. This scalar theta maximum is not an affine covariance upper bound.

Use (2.2) to condition the M_N Gaussian on its K cosets. A coset with
perpendicular part N w has mass proportional to

    exp[-N^2||w||^2/(2 sigma)] Z_K(u_w),

for some real internal shift u_w in S. The zero coset is exactly K and
has factor Z_K(0). The theta maximum and N^2/(2 sigma)=2pi^2 beta imply

    p_bad:=Pr(z notin K)
        <=sum_(w in Lambda,w!=0)exp(-2pi^2 beta||w||^2).

With lambda=1/4, b=m and the first inequality in (1.2), (4.1) gives

    p_bad<=2exp(-pi^2 beta/16).                      (4.2)

Conditional on z in K, z is exactly the centered Gaussian on K with
parameter sigma. No infinite-volume phase statement is contained in
(4.2); its sufficient beta grows with the dimension m.

## 5. Relative source estimate on the exact lattice

For the conditional K law and h_e=P_e h, Poisson summation gives

    E_K exp(i<h,X>)
      =exp(-||h_e||^2/2)
       [1+sum_(w in K*,w!=0) exp(-2pi^2 sigma||w||^2
                                      +2pi sqrt(sigma)<w,h_e>)]
       /[1+sum_(w in K*,w!=0)exp(-2pi^2 sigma||w||^2)].

The source in this dual expression is real. Pairing w with -w shows
that its numerator tail is at least the denominator tail. If
||h_e||<=pi sqrt(sigma)/8, then using ||w||>=1/4 gives

    2pi sqrt(sigma)|<w,h_e>|<=pi^2 sigma||w||^2.

Thus the numerator tail is bounded by sum_(w!=0)exp(-pi^2 sigma||w||^2).
Applying (4.1) with b=r and t=pi^2 sigma under (1.2) proves

    0 <= E_K exp(i<h,X>)/exp(-||h_e||^2/2)-1
          <=2exp(-pi^2 sigma/32).                  (5.1)

The full M_N law is a mixture with weight p_bad outside K. The
characteristic functions of both mixture components have absolute value
at most one. Its absolute difference from the K characteristic function
is therefore at most 2p_bad. Dividing by exp(-||h_e||^2/2), then using
(4.2) and (5.1), proves (1.1). Conversion of the absolute mixture
estimate alone requires the positive ||h_e||^2/2 in its second error
term. A relative bound without this factor needs additional control
of the mixture components, supplied below.

For every centered full-rank lattice Gaussian, completing the square
and the same theta maximum also imply

    E exp(<h,X>)<=exp(||h||^2/2).                    (5.2)

It follows that each coordinate has tail
Pr(|X_p|>=u)<=2exp(-u^2/2), and centered smeared moments have uniform
Gaussian bounds at each fixed source norm. The statement (5.2) does not
extend to arbitrary shifted lattice measures.

A stronger relative estimate is also available by controlling every
internal affine coset before mixing. If its real shift in S is b, the
conditional characteristic function divided by the same Gaussian is

    [1+sum_(w!=0)exp(-2pi^2 sigma||w||^2
             +2pi sqrt(sigma)<w,h_e>)exp(2pi i<w,b>)]
    /[1+sum_(w!=0)exp(-2pi^2 sigma||w||^2)exp(2pi i<w,b>)].

The shift appears only as a unit-modulus phase. Let
eta=2exp(-pi^2 sigma/32). The numerator tail and denominator tail have
absolute values at most eta by the same source-radius and packing
argument. Under (1.2), eta<=2/5^r<1, so the relative error from one is
at most 2eta/(1-eta), uniformly for every real b. Multiplying by the
deterministic perpendicular phase of each coset and averaging changes
one by at most 2p_bad plus this error. Thus

    |E exp(i<h,X>)/exp(-||P_e h||^2/2)-1|
       <=4exp(-pi^2 beta/16)+2eta/(1-eta).          (5.3)

This refinement avoids the Gaussian amplification in the cruder (1.1)
by proving a stronger bound for the nonexact mixture components. Both
estimates remain valid. The source-radius hypothesis still matters:
at a clock charge q=N, a plaquette character is identically one, while
its putative unaliased Gaussian expression can be arbitrarily small.

## 6. An explicit finite-clock scaling family and physical fields

Take any a_j->0 and even L_j>=4 with ell_j=a_j L_j->infinity. Set

    beta_j=64 L_j^4, N_j=8 beta_j,
    sigma_j=16 beta_j/pi^2.                         (6.1)

These integers N_j are finite at every stage. Both dimension inequalities
in (1.2) hold for L>=4: beta/(3V+3)>21, whereas 16log5/pi^2<3; and
sigma/(3V-3)>34, whereas 32log5/pi^2<6. The elementary loose numerical
bounds can be replaced by log5<2 and pi>3, with still ample margin.

For bounded-norm source families h_j, (1.1) tends to zero and gives
Gaussian characteristic functions with the exact projector covariance.
There is no all-affine covariance premise. This sufficient scaling is
much more restrictive than a volume-uniform finite-coupling estimate.

Two actual bounded clock observables will be considered:

    Y_p=-phi_beta'((d theta)_p)/(sqrt(beta)phi_beta((d theta)_p)),
    R_p=sqrt(beta) principal((d theta)_p), principal in [-pi,pi).

The first is the score and satisfies Y_p=E[X_p|theta]. Conditional lift
independence gives

    E|<h,X-Y>|^2=sum_p h_p^2 E Var(X_p|theta).

Using the principal representative as a comparison predictor, it equals
the lift whenever |X_p|<pi sqrt(beta), and otherwise the difference
from X_p has absolute value at most 2|X_p|. The Gaussian tail from (5.2)
therefore implies

    E|<h,X-Y>|^2<=epsilon(beta)||h||^2,
    epsilon(beta)=(8pi^2 beta+16)exp(-pi^2 beta/2).   (6.2)

Jensen gives E exp(<h,Y>)<=exp(||h||^2/2), hence all fixed-order moments
of bounded-norm score sources are uniformly integrable.

For the principal field R, the coupling R=X on every plaquette outside
an event of probability

    p_wrap<=12V exp(-pi^2 beta/2).                   (6.3)

Always |R_p|<=|X_p|, since the principal representative minimizes the
absolute angle; the endpoint pi is included in the bad event. For each
fixed positive integer k, Minkowski and the coordinate Gaussian moments
give ||<h,X-R>||_(2k)<=C_k||h||_1. Holder with the bad event then gives

    E|<h,X-R>|^k<=C_k ||h||_1^k sqrt(p_wrap)
                 <=C_k(6V)^(k/2)||h||^k sqrt(p_wrap).   (6.4)

This tends to zero under (6.1) for bounded ||h||. In particular endpoint
asymmetry of the principal convention has no surviving mean or moment.
For k=2, (6.4) gives a uniform second-moment bound for the principal
field along this sequence. It is not asserted to have the exact centered
MGF bound of the score at finite parameters.

For each orientation, tile a translated fundamental box near the origin
by side-a four-cells centered at its plaquette midpoints. Embed either
Y or R as a piecewise constant two-form a^-2 times its lattice value,
zero outside that box. For real f in L2(R^4;Lambda^2), its source is

    (J_j f)_p=a_j^-2 integral_(cell_p) f_mu,nu(x)dx,
    ||J_j f||_l2<=||f||_L2.                         (6.5)

The following geometric limit is independent of the probability law:

    <J_j f,P_e,L_j J_j g> -> <f,P g>,

where P has Fourier symbol, for p!=0,

    P_(mu,nu;rho,sigma)(p)=
     [p_mu p_rho delta_(nu,sigma)-p_mu p_sigma delta_(nu,rho)
      -p_nu p_rho delta_(mu,sigma)+p_nu p_sigma delta_(mu,rho)]/|p|^2.

To prove it, start with Schwartz tests whose smooth Fourier transforms
have compact support separated from zero. Periodization changes their
L2 values on the expanding boxes by a vanishing amount. In midpoint
bases, the lattice exterior derivative symbol is i xi wedge, with
xi_mu=2sin(a p_mu/2). Cell averaging contributes
product_mu sinc(a p_mu/2). For small enough a there are no aliases on
the fixed Fourier support. The unitary lattice coefficient is
ell^-2 fhat(p) product sinc(a p_mu/2), so the pairing is an ell^-4
Riemann sum converging to (2pi)^-4 integral fhat*P ghat. Uniform
contraction of J_j, P_e and P extends this to all L2 tests by density.

Equations (1.1), (6.2), (6.4) and (6.5) show that both physical fields
converge on every finite family of L2 tests to the centered Gaussian
two-form F with covariance P=d(-Delta)^-1 d*. All joint polynomial
moments converge, by (5.2), Jensen and (6.4).

These are also random-distribution limits locally in H^-s for every
s>2. Indeed the score has E|F_j(f)|^2<=||f||^2. The principal field has
the same bound with a uniformly bounded multiplier by (6.4). On a
bounded box and after a smooth interior cutoff, the Laplacian
eigenbasis therefore bounds the expected H^-u norm by a constant times
sum_n(1+lambda_n)^-u, finite for u>2 in four dimensions. Compact
inclusion H^-u into H^-s for 2<u<s and a countable box exhaustion give
tightness. The Gaussian F=P W, W six-component white noise, uniquely
identifies all subsequential limits by the finite-dimensional laws.

## 7. Genuine Wilson loops and surface-independent Gaussian energy

Let C be a contractible oriented lattice loop with integer edge current
j_C=d* S_C, where S_C is an integer plaquette surface. For integer q,
the actual clock Wilson observable is

    W_q(C)=exp(i q<j_C,theta>)
          =exp(i q<S_C,d theta-2pi k>)
          =exp(i<h_C,X>), h_C=q S_C/sqrt(beta).     (7.1)

The lift integers disappear exactly because q and S_C are integer.
This is a character of the clock configuration, not a new definition
using the score or a fractional power of a link phase.

If two surfaces have the same boundary, their difference is in ker d*,
so P_e gives identical projections. The Gaussian exponent therefore
depends only on the loop current. Write Q=d* d on one-forms. Since
j_C is in range Q, divergence free and orthogonal to harmonic one-forms,

    ||P_e S_C||^2=<j_C,Q^+ j_C>
                  =sum_(l,l') j_C(l)j_C(l')
                     1_(orientation(l)=orientation(l'))G_L(x_l-x_l'),

where G_L is the inverse of the scalar periodic Laplacian on zero-mean
functions. Link tails x_l can be used because equal-orientation midpoint
offsets cancel. More generally

    <P_e S_1,P_e S_2>=<j_1,(-Delta_L)^+ j_2>.       (7.2)

No longitudinal gauge propagator or harmonic current is inserted here.
For arbitrary real lattice sources the full-rank Gaussian characteristic
function is strictly positive by its Poisson sum of positive Gaussians;
in particular the Wilson expectations in the ratios below are nonzero.

## 8. Off-diagonal Green-function convergence with periodic control

For the continuous-time nearest-neighbor walk on Z^4 whose rate to EACH
of the eight neighbors is one, let K(t,n) be its heat kernel. The
positive scalar Laplacian has symbol lambda(k)=sum_mu 4sin^2(k_mu/2).
Thus

    K(t,n)=(2pi)^-4 integral_[-pi,pi]^4
                     exp(-t lambda(k)+i k.n)dk,
    G_infinity(n)=integral_0^infinity K(t,n)dt.

The rate convention matters: this is not the discrete-time walk Green
function; its total jump rate is eight.

Here are the bounds needed for a direct limit proof. The Fourier bound
lambda(k)>=c|k|^2 on the Brillouin zone yields
K(t,0)<=C(1+t)^-2 and hence the same supremum bound for every n.
The coordinate moment generating function of the walk is
exp[2t(cosh(s)-1)]. Chernoff with s a fixed small constant or proportional
to |n|/t, whichever is smaller, bounds a displacement tail by
C exp[-c min(|n|,|n|^2/t)]. Splitting the convolution for K(t,n) at
time t/2 according to whether the first or second displacement has
length at least |n|/2 combines the two estimates into

    K(t,n)<=C(1+t)^-2 exp[-c min(|n|,|n|^2/t)].      (8.1)

Changing between Euclidean and maximum norms changes only C,c, which
are independent of t,n,L and a.

For each u>0 and a n tending to x, substituting k=a p and using the same
Fourier domination gives

    a^-4 K(u/a^2,n)->(4pi u)^-2 exp(-|x|^2/(4u)).

This is uniform for x in a compact set. To integrate in u uniformly
away from x=0, fix |x|>=rho>0. For u below a constant times rho a,
(8.1) bounds the integral by C a^-2 exp(-c rho/a), tending to zero.
For larger u below a small eta it is bounded by
C integral_0^eta u^-2 exp(-c rho^2/u)du, tending to zero with eta.
For u above A it is bounded by C/A. Dominated convergence on the
intermediate interval then proves, uniformly on compact sets separated
from zero,

    a^-2 G_infinity(n)->integral_0^infinity
                (4pi u)^-2 exp(-|x|^2/(4u))du
              =1/(4pi^2 |x|^2).                    (8.2)

For the periodic zero-mean Green function,

    G_L(n)=integral_0^infinity [K_L(t,n)-L^-4]dt,
    K_L(t,n)=sum_(w in Z^4)K(t,n+Lw).

When |n|<=L/4, split the difference G_L-G_infinity at t=L^2. On
0<=t<=L^2, the omitted zero-mode contribution has size L^-2. The
nonzero images are bounded by (8.1) with distances at least cL|w|.
For t<=L, summing their exponential tails gives Ce^-cL. For
L<=t<=L^2, split image shells at |w|=t/L: Gaussian shells below that
threshold and exponential shells above it give
C t^-2 exp(-c L^2/t). Its integral is at most C L^-2.

For t>=L^2, the periodic Fourier series and
lambda(2pi k/L)>=c |k|^2/L^2 in the canonical momentum box give

    |K_L(t,n)-L^-4|<=C L^-4 exp(-c t/L^2).

Its integral, and the infinite-kernel tail integral, are each at most
C L^-2. Consequently

    |G_L(n)-G_infinity(n)|<=C L^-2, |n|<=L/4.       (8.3)

Together with aL->infinity, (8.2)–(8.3) prove the required uniform
off-diagonal physical limit

    a^-2 G_L(n)->1/(4pi^2 |x|^2), a n->x!=0.       (8.4)

This argument keeps the finite periodic zero mode until its contribution
has been bounded. It does not sum the non-absolutely convergent image
series of Green functions term by term.

## 9. Normalized thin Wilson loops and Coulomb probe interactions

Take two fixed disjoint rectilinear closed loops in R^4 with strictly
positive separation, and lattice approximations with bounded physical
lengths and integer spanning surfaces satisfying
||S_C,j||^2<=C a_j^-2. Coordinate rectangles satisfy this explicitly;
finite rectangle decompositions provide further admitted examples.
Choose integers q_i,j nearest to g_i sqrt(beta_j), for fixed real g_i.
Their clock charges are well defined modulo N_j, and q_i,j/N_j tends
to zero, so there is no eventual charge-alias ambiguity.

For the two individual sources and their sum, ||h||^2<=C a^-2. Under
(6.1), a^-2/L^4=a^2/ell^4 tends to zero. Therefore the source-radius
condition (1.2) eventually holds and the right side of (1.1) tends to
zero, including its relative-error factor. Write these relative errors
as o(1); they remain relative errors even if each Wilson expectation
tends to zero due to its self-energy.

Dividing the joint expectation by the two individual expectations now
cancels the Gaussian self terms exactly:

    E[W_(q1)(C1)W_(q2)(C2)]/[E W_(q1)(C1) E W_(q2)(C2)]
      =(1+o(1))exp[-(q1 q2/beta)<j1,(-Delta_L)^+ j2>].

By (8.4), the positive separation and the edge-current Riemann sums,
the limit is

    exp[-g1 g2 integral_C1 dx_mu integral_C2 dy_mu
                          /(4pi^2 |x-y|^2)].       (9.1)

The repeated component index is summed. To see the normalization, each
oriented edge contributes a times its signed unit tangent to the line
integral, while G_L supplies a^2 G_continuum. There are O(a^-2) edge
pairs; the uniform off-diagonal error is o(a^2). This step does not
treat a thin surface or line as a continuous test functional on H^-s.

For an explicit electrostatic consequence, take two disjoint temporal
rectangles with time extent T and spatial endpoints A,B for the first,
C,D for the second. Their temporal orientations have signs +,- at
each pair, respectively. Choose the spatial closing paths so the loops
remain disjoint. The temporal-line contribution for endpoints separated
by R is exactly

    I(T,R)=integral_0^T dt integral_0^T ds
                  /(4pi^2[(t-s)^2+R^2])
      =[(T/R)arctan(T/R)-0.5 log(1+T^2/R^2)]/(2pi^2).

Thus I(T,R)/T tends to 1/(4pi R). Temporal-spatial cross contractions
vanish because their tangent components are orthogonal. Spatial closing
path contributions are O(1) at fixed endpoints as T grows. Taking the
continuum/infinite-volume limit in (9.1) at fixed T first, and then
T->infinity, yields the cross interaction energy

    -lim_(T->infinity) T^-1 log[normalized loop ratio]
       =g1 g2/(4pi)[1/|A-C|-1/|A-D|
                       -1/|B-C|+1/|B-D|].         (9.2)

The return endpoints B,D can subsequently be sent to infinity with all
three return-related distances diverging, leaving g1 g2/(4pi|A-C|).
This is a stated subsequent external-probe limit, not a construction of
normalizable charged particle states or a dynamical matter sector.

## 10. Explicit Gaussian physical modes and remaining scope

The limiting covariance in section 6 has the Maxwell curvature form.
Its physical mode count follows directly, without an interacting
reconstruction theorem. Set E_i=F_0i and B=(F_23,-F_13,F_12). Time
reflection changes the sign of E and preserves B. At spatial p!=0,
let r=|p|, P_T=I-p p^T/r^2, C_p v=p cross v, and M=-i C_p/r.
Then M*=M and M^2=P_T. The Euclidean Fourier blocks are

    S_EE=(p0^2 I+p p^T)/(p0^2+r^2),
    S_BB=r^2 P_T/(p0^2+r^2),
    S_EB=-p0 C_p/(p0^2+r^2), S_BE=+p0 C_p/(p0^2+r^2).

For strictly positive times s,t, subtract the EE contact term at
s+t=0, Fourier transform p0 and include its odd reflection sign. The
result is

    (r/2)exp[-r(s+t)] [[P_T,M],[M,P_T]].             (10.1)

The block matrix is the Gram matrix of (u,v)->P_T u+M v and has rank
two. Positive-time Laplace transforms of smooth tests have dense range
in the transverse fibers: a nonzero nonnegative positive-time function
has a strictly positive Laplace transform on r>0, which can be divided
out on compact momentum sets separated from zero. Time translation is
exp(-u|p|); thus the one-particle energy is |p| with two transverse
polarizations. The measure is (r/2)d^3p/(2pi)^3, and p=0 contributes
no additional normalizable state.

For the Gaussian field, Wick exponential reflection products equal
exp(<J_OS f,J_OS g>), the inner products of symmetric Fock exponential
vectors. Differentiation gives the Wick-polynomial isometry; density
gives the full positive-time quotient as symmetric Fock space, with
Hamiltonian dGamma(|p|). The Euclidean Bianchi identity dF=0 holds.
Euclidean d*F=0 is not asserted: its covariance has Schwinger contacts.

This direct theorem has stronger coupling growth and weaker parameter
generality than the preceding affine-input theorem, but eliminates
that provisional premise and adds actual thin charged-probe ratios.
It supplies a free Maxwell scaling construction and external Coulomb
interactions inside a chosen finite-clock family. It does not select
the law from framework axioms, establish a phase for fixed N=3, derive
charged matter or Born statistics, or address gravity. Those obligations
remain open, and this result supplies no axiom-update conclusion.
