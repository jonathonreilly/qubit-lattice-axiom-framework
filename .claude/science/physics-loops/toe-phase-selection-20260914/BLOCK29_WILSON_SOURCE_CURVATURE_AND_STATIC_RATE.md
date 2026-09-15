# Block29: from current-source curvature to Wilson and static-rate bounds

Private author derivation, 2026-09-15; independent review pending.
Main5deabeb698a27c2c3f68c5df685af2521ef15307. Provisional source unit:
PR8133 at f8e7219b5e79bcb271bb3c1df635ecdeeb57dbe8, specifically the
free-cubic magnetic source note equations(4),(9),(10) and the current
Poisson/Wilson note equation(10). No axiom change or physical-law selection.

## 1. Target and source restrictions

The new target is an actual Wilson-character lower bound for the finite
clock, and its consequence for long rectangular loops in a thermodynamic
limit. A stronger static charged-sector energy interpretation needs a
matched stationary reflection-positive state or transfer limit. That bridge
is a separate obligation, not assumed to follow from a covariance theorem.

Keep the supplied N-state clock Villain law on FREE FOUR-DIMENSIONAL CUBES,
beta>0, N a positive integer. Let C=ker d0* be the real conserved-current
space and Lambda=C intersect Z^edges. On C set G=H1^-1. The actual character
formula from the pinned source is

    W_N(J)=T(J/N)/T(0), T(s)=sum_(a in Lambda) exp[-V(a+s)],
    V(a)=N^2(a,G a)/(2beta)-F(N d1 G a), J in Lambda.       (1)

Under the source's large-beta carrier conditions, F is even, real and smooth
on all real two-form sources, and

    F(0)=0, F<=0, D2 F>=-epsilon I.

Consequently V is even, has Gaussian lower growth, and

    D2 V <= M:=N^2(beta^-1+epsilon) G.                    (2)

The upper curvature bound suffices below; positivity of D2 V is not needed.
It was derived in the source using the exact physical magnetic gas and a
fixed real interpolation, not by replacing the integer current measure
with a continuous one. Its values on the physical cosets in(1) are independent
of the chosen integer filling, although the interpolation itself need not be.

The source explicitly excludes arbitrary thin rectangles: a short relative
boundary carrier can require a long fill there. Thus it is invalid to obtain
a finite-spatial-box, infinite-time transfer estimate merely by applying(2)
to arbitrarily long slabs. Any proposed transfer extension must resolve that
boundary issue. The cubic thermodynamic limit below does not use that extension.

## 2. An elementary periodized curvature lemma

Let Lambda be any full-rank lattice in a finite Euclidean space, and V be
even and C2, with enough Gaussian lower growth to sum the following terms.
Suppose D2 V<=M for a fixed positive quadratic form M. Then for every s,

    T(s)/T(0) >= exp[-(s,M s)/2].                       (3)

Here is a proof without differentiating the lattice sum. Integrating the
second derivative along a+s t gives

    V(a+s)+V(a-s)-2V(a)<=(s,M s).

Hence sqrt(exp[-V(a+s)] exp[-V(a-s)]) is at least
exp[-V(a)]exp[-(s,M s)/2]. Sum over a and apply Cauchy-Schwarz. Evenness
and lattice reversal give T(-s)=T(s), so

    T(s)=sqrt(T(s)T(-s))
        >=sum_a sqrt(exp[-V(a+s)]exp[-V(a-s)])
        >=T(0)exp[-(s,M s)/2].

This proves(3), including s=0. It uses no continuous Brascamp-Lieb claim
about an integer law. It also holds for any translated representative
s+lambda, lambda in Lambda, because T is Lambda-periodic.

## 3. Alias-preserving finite-clock Wilson bound

Applying(3) with(1)-(2) yields

 exp[-(beta^-1+epsilon)/2 * min_(c in Lambda)(J+N c,G(J+N c))]
       <= W_N(J) <= 1.                                (4)

The upper bound follows either from the original probability characteristic
or the positive dual representation in the source. The lower bound proves
strict positivity. The minimum exists since G is positive definite and the
current lattice is discrete. In particular one may omit the minimization
and use the representative c=0. If J=N c, the minimum is zero and(4) gives
the exact alias W_N(J)=1. This retains the finite clock's character algebra.

For a simple oriented loop current J_C and integer charge q, one can choose
any representative q_eff=q mod N with |q_eff|<=N/2. Then

    W_N(q J_C)>=exp[-a q_eff^2 (J_C,G J_C)/2],
    a=beta^-1+epsilon.                                (5)

No lower bound on N is needed beyond the clock definition. This distinction
matters: a Wilson perimeter lower bound alone cannot distinguish a massless
Coulomb phase from a gapped deconfined finite-group phase. A claim of a photon
or of dynamical matter from(4) would be unsupported.

## 4. Cubic thermodynamic Green passage

For any fixed finite conserved J, the free-cube Coulomb energy (J,G_L J)
converges to the infinite-lattice energy (J,H1^-1 J) as the source recedes
from the boundary. Here is a direct projection proof. Choose a finitely
supported integer two-form S with d1*S=J; a finite cycle bounds in Z4.
In a box containing its support, let P_L=d1 G_1,L d1* and let Q_L be the
projection onto ker d1,L* on two-forms. Contractibility gives P_L=I_L-Q_L.
The zero extensions of the co-closed spaces defining Q_L are nested and
remain globally co-closed: every edge of an included face is included, so
d1* commutes with this extension. Their union is dense in ker d1* on ell2.
Indeed cut a co-closed Fourier field away from frequency zero, write it
as d2* H3^-1 d2 u there, approximate the three-form potential by finite
support, then remove the frequency cutoff. There is no ell2 harmonic
vector at the single zero Fourier point. Thus Q_L converges strongly to Q,
and P_L converges strongly to P. Moreover every receding rooted box contains
a growing centered box; the nesting sandwich makes the convergence uniform
over such placements. Therefore

    (J,G_1,L J)=(S,P_L S) -> (S,P S)=(J,H1^-1 J).      (6a)

This argument concerns co-closed zero extension. It does not assert that
a closed charge remains closed after extending a free box by zero.

Every local weak limit of centered free-cube clock laws, or uniformly
rooted free-cube laws, now inherits(5). For root averages most roots recede
from every face, the bound is uniform there, and the remaining fraction
vanishes. Compact finite-clock link configurations give subsequential
limits; no uniqueness or reflection positivity is inferred from compactness.
The finite nearest-neighbor Gibbs specification is strictly positive and
continuous, so its local conditional identity also passes to these limits.
Uniform root limits are stationary, but stationarity alone is not the
missing reflection-positive transfer identification.

## 5. Exact rectangular-loop Green energy

For a rectangular loop C_(R,T) in the0-1 plane, let R be its fixed spatial
separation and T its temporal length. The Green calculation is

 lim_(T->infinity) (J_(R,T),H1^-1 J_(R,T))/T
       =2[G3(0)-G3(R e1)],                            (6)

where G3 is the scalar nearest-neighbor Laplacian Green function on Z3,
with Fourier denominator lambda(k)=sum_(i=1)^3 |exp(i k_i)-1|^2.
The following exact identity proves(6), and fixes its normalization. Put

    lambda_i=2-2cos k_i,
    r=(lambda+2-sqrt(lambda(lambda+4)))/2,
    D_R(k1)=sum_(x=0)^(R-1) exp(i k1 x),
    dmu(k)=d^3k/(2pi)^3 on [-pi,pi]^3.

For lambda>0 the scalar time Green function is
g_lambda(t)=r^|t|/sqrt(lambda(lambda+4)). The temporal sides of the
rectangle carry delta_0-delta_(R e1) for T consecutive links, while the
spatial sides carry a length-R path at times0 and T with opposite signs.
The one-form Hodge Green kernel is diagonal in orientation, so the two
contributions have no cross term. Summing g_lambda(t-s) on the temporal
sides gives

    sum_(t,s=0)^(T-1) g_lambda(t-s)
      =T/lambda-2(1-r^T)/(lambda sqrt(lambda(lambda+4))).

The spatial sides contribute
2|D_R|^2(1-r^T)/sqrt(lambda(lambda+4)). Using
|1-exp(i R k1)|^2=lambda_1 |D_R|^2 therefore yields

 E(R,T):=(J_(R,T),H1^-1 J_(R,T))
   =2T[G3(0)-G3(R e1)]
    +2 integral |D_R|^2 (1-r^T)/sqrt(lambda(lambda+4))
                    * (lambda_2+lambda_3)/lambda dmu(k).   (6b)

The integrand is nonnegative and its singularity at k=0 is integrable.
Since |D_R|<=R and the last factor is at most1, the remainder is bounded
between0 and2R^2 G4(0), uniformly in T. Here
G4(0)=integral [lambda(lambda+4)]^-1/2 dmu(k), obtained by integrating the
fourth Fourier coordinate. This proves(6) with the explicit bound

 0<=E(R,T)/T-2[G3(0)-G3(R e1)]<=2R^2 G4(0)/T.          (6c)

It also shows that E(R,T)/T decreases with T at fixed R, since
(1-r^T)/T decreases for 0<r<1. Two exact checks are E(1,1)=1/2, from the
four-dimensional Hodge projection's diagonal, and
lim E(1,T)/T=1/3, from6[G3(0)-G3(e1)]=1. The scalar Laplacian convention
is essential for both constants. The exchanged rectangle has E(R,T)=E(T,R)
by four-dimensional cubic symmetry, an additional independent check.

The inherited Wilson bound now gives the actual rate statement

 limsup_(T->infinity) -log W_N(q C_(R,T))/T
       <=a q_eff^2 [G3(0)-G3(R e1)].                  (7)

It is an upper bound, not an equality or a derived Coulomb force. In
particular subtracting an unknown self energy from both sides does not
turn it into a two-sided interaction-potential estimate. The companion clock-Ginibre/transfer proof supplies a proposed matching
of the free-boundary state and its static insertion spectrum; its
independent review remains pending. Neither endpoint charges here nor
Wilson insertions construct dynamical charged particles.

The ordinary lattice Green asymptotic is G3(R e1)=1/(4pi R)+O(R^-3),
with G3>=0 and finite G3(0). Thus the right side of(7) is uniformly bounded
in separation. This is a bound on the rate, not a claimed asymptotic formula
for it. The Green asymptotic is standard mathematics; the normalization is
H_(Z3)=6(I-P_SRW), as in Lawler-Limic Theorem4.3.1. Even without the asymptotic,
positivity and finiteness of G3(0) give the uniform bound.

For growing rectangles of arbitrary aspect ratio, the four-dimensional
Green bound G4(x)<=C/(1+|x|^2) gives E(R,T)<=C' perimeter(C_(R,T)):
from a fixed edge, the sum over the two parallel sides is at most
2C sum_(n in Z)(1+n^2)^-1, independently of their lengths and separation.
Only parallel orientations couple. Summing over the rectangle's edges
proves the stated bound. Therefore these cubic-limit Wilson expectations
have a perimeter lower bound. A strictly positive area-law coefficient
for this rectangle family is incompatible with it. This says nothing
about all physical phases or the separate N=3 penalty Hamiltonian.

## 6. Completed author challenges and the transfer companion

Separate direct clock enumeration and current-coset summation agree in12
cases, with analytic finite-tail expressions evaluated in floating arithmetic.
Explicit periodic currents, a sparse scalar Poisson solve and a separately
integrated time kernel challenge the Green formula and its normalizations.
The initial current-cutoff failure is preserved with its diagnosis.

The companion BLOCK29_CLOCK_GINIBRE_FREE_STATE_AND_STATIC_TRANSFER.md gives
a proposed state/transfer bridge using the published carpet limit followed by
clock pinning. It identifies the free-boundary state across cofinal shapes
and proves existence of the Wilson-visible static rate. That argument never
extends the source-curvature theorem to excluded slabs. Direct temporal-link
sums separately challenge its finite transfer representation.

These are author derivations and finite checks, pending independent review.
The result applies prior source curvature and standard Wilson/transfer
machinery; it is not a new discovery of the classical nonconfinement criterion.

