# Planar loops test a fixed Gaussian regulator

Personal conditional mathematical derivation, 2026-09-15. This rejects
one proposed uniform auxiliary-activity bound. It does not prove failure
of a field limit, of renormalization methods, or of the framework axioms.

## 1. Area and energy can have different orders

In Z^4 let S_L be the unit integer sheet of L^2 faces in a coordinate
two-plane, with square side L. Its boundary current j_L=D*S_L has
mass4L, squared l2 norm4L, and

    ||S_L||^2=L^2, E_L=||P S_L||^2=<j_L,G_1 j_L>.

The cubic Hodge Green operator is the scalar lattice Green kernel on
each orientation. Its entries are nonnegative: use the nonnegative
continuous-time random-walk heat kernel and integrate over time.
Each of the two current orientations consists of two parallel, opposite
segments of length L. The negative cross interaction between those
opposite segments can be dropped for an upper bound. A segment's
self-energy is at most

    L sum_(n in Z) G_4(n e_1)=L G_3(0).

The equality follows by summing the heat kernel over that coordinate
(Tonelli applies to its nonnegative entries), leaving the three-dimensional
walk. Hence

    E_L <=4 L G_3(0)<=C L, C=sqrt(3) pi/2.          (1)

For the explicit constant, lambda_3(p)>=4|p|^2/pi^2 on [-pi,pi]^3,
and this cube is contained in the ball of radius sqrt(3)pi. Therefore

    G_3(0)<= (pi^2/4) integral_(|p|<=sqrt(3)pi)
                       |p|^-2 dp/(2pi)^3
           =sqrt(3)pi/8.

No numerical Green value or continuum replacement is used. In particular
the coexact part obeys ||Q S_L||^2>=L^2-C L. This is an explicit family
with filling area growing quadratically and boundary energy at most
linearly. It is stronger for this family than the general l1-l2 energy
bound from Block4.

## 2. Match the free finite boxes, instead of importing an infinite bound

For a fixed finite sheet S, exhaust Z^4 by free contractible cubes
containing its support. Let P_R be their exact face projections, and
extend P_R S by zero outside each cube. Their l2 norms are bounded by
||S||, and ||P_R S||^2=<S,P_R S>.

Every weak limit u is closed: on each fixed interior three-cell,
B P_R S=0 once the cube is large enough. In l2 on Z^4 the Fourier
exterior-algebra identity gives ker B=closure(im D). For any compactly
supported edge field a, Da lies inside a sufficiently large cube and

    <P_R S,Da>=<S,Da>.

Thus the weak limit is exactly P S. The displayed norm identity then
gives convergence of the squared norms to ||P S||^2 and hence strong
convergence. All subsequences have that same limit. Consequently, for
each L one can choose a finite free cube with

    E_(L,R)=||P_R S_L||^2<=2 C L.                   (2)

No bound on the required cube size is claimed. This existence statement
is enough to challenge a constant asserted uniform in all free volumes.
No torus harmonic mode has been dropped in this argument.

## 3. The tested activity and the precise regulator contract

Use A0,T,R from the positive auxiliary note in such a finite cube. For
the pair of orientations of one electric current define

    F_S(eta)=exp[-g^2 S.RS/2] cosh(g eta.TB S).

Consider the fixed quadratic regulator

    G_kappa(eta)=exp[kappa eta.A0^-1 eta/2],
    0<kappa<1,
    ||F_S||_kappa=sup_eta F_S(eta)/G_kappa(eta).      (3)

The upper restriction is exactly Gaussian integrability:
E_gamma(A0) G_kappa=(1-kappa)^(-dim(V)/2)<infinity in
each finite volume. This particular expectation is not asserted to be
uniform in volume. The test concerns a uniform small activity norm.

Put a=TB S and Q_R=I-P_R. From the exact matrix identities,

    a.A0 a=S.(R-P_R)S=:U_S,
    S.RS=E_S+U_S,
    U_S>=||Q_R S||^2.

Evaluate the supremum at eta=(g/kappa)A0 a and use cosh(t)>=exp(t)/2:

    log ||F_S||_kappa
      >=-log2+(g^2/2)[(kappa^-1-1)U_S-E_S].         (4)

For S=S_L and the sufficiently large free cube in (2), this is at least

    -log2+(g^2/(2kappa))[(1-kappa)L^2-2 C L],       (5)

which tends to positive infinity for every fixed g>0 and kappa<1.
For example the lower bound turns positive in its quadratic bracket
once L>2C/(1-kappa). Increasing the fixed electric coupling g does not
repair it. The lower bound is on the actual single positive activity,
not on a loose upper majorant. These S_L are ordinary planar fillings,
not large artificial additions of a closed sheet to one fixed current.

A regulator formed from only part of this positive quadratic energy
cannot improve this supremum bound. The conclusion does not cover a
different nonquadratic regulator, a current-dependent center, an
operator-valued norm, or a cancellation between a differently grouped
set of terms. Nor does it say that all polymer norms used in the
literature have exactly the form (3).

## 4. Constructive escape retained

The exact translation eta -> xi=eta+gGBS in the companion note replaces
F_S by exp[-g^2 E_S/2] times a shifted bounded positive theta function.
It removes the offending filling-area term from the activity exactly.
What remains is a nonlocal dependence of that theta function on the
current through GBS, with integer periodicity. Therefore (5) is a reason
to use that translated representation or a different organization; it
is not a wall on the physical model. The full coupled source estimate
remains to be supplied.

## 5. A separate duality-to-Gaussianity control

Even a self-dual scalar source relation need not force Gaussianity.
Let sigma^2=1/2, He4(z)=z^4-6z^2+3, and epsilon=1/16. The density

    p(x)=Gaussian_(sigma^2)(x)[1+epsilon He4(x/sigma)]

is positive and normalized: min He4=-6 and its Gaussian integral is0.
It has mean0 and variance1/2. Direct Gaussian differentiation gives

    M(t)=exp(t^2/4)(1+epsilon t^4/4),
    chi(t)=exp(-t^2/4)(1+epsilon t^4/4),
    chi(t)=exp(-t^2/2) M(t).                        (6)

The characteristic function is positive for every real t. Also
M(t)<=exp(t^2/2): with u=t^2/4, use
1+4epsilon u^2<=1+u+u^2/2<=exp(u). Nevertheless
its fourth cumulant is6epsilon=3/8, not zero. This is an explicit
probability counterexample to that logical shortcut, not a lattice
gauge state or an axiom-compatible alternative TOE.
