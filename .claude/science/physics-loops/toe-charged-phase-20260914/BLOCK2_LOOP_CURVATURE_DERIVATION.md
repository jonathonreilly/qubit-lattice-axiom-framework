# Massive determinant curvature and a noncompact gauge covariance construction

Author derivation in progress, independently unreviewed. This is a supplied
Euclidean massive model. No identification with the block-1 Hamiltonian,
finite-payload phase or physical photon particle is asserted.

## 1. Closed walks and a quantitative local filling

Let Lambda be the vertex set of a finite rectangular cubical box in Z^d,
d>=2. A is real on its oriented internal links, with A_yx=-A_xy. Each vertex
has m fermionic components. Let

    D(A)=M I+K(A),
    K(A)_xy=T_xy exp(i e A_xy),  ||T_xy||<=t,
    K(A)_xx=0,  K(A)_xy=0 unless x,y are nearest neighbors.

The directed matrices T_xy are supplied; Hermiticity of K is not needed.
Both block-row and block-column sums are <=2dt, so ||K(A)||<=2dt. Assume
M>2dt and put q=2dt/M<1. Normalize the paired determinant by

    W(A)=|det(I+K(A)/M)|^2>0,
    L(A)=log W(A)=2 Re sum_(n>=1) (-1)^(n+1) Tr K(A)^n/(n M^n).

The logarithm converges absolutely in finite volume, uniformly in real A.
It is a sum over rooted closed coordinate walks gamma of length n with
spin amplitude tr(T_x0x1 ... T_x(n-1)x0), bounded in modulus by m t^n.
The phase is exp(i e A(gamma)).

A closed coordinate word can be sorted by coordinate axis through swaps of
adjacent steps on different axes. A swap changes its one-chain by the boundary
of one oriented unit plaquette. Preserve the order of signs within each axis.
Every intermediate word then has the same ordered coordinate subword on each
axis as the original walk. Its coordinate values therefore stay between the
original minimum and maximum for that coordinate. All the swept plaquettes
lie in that rectangular coordinate bounding box, hence inside Lambda.

After sorting, each axis group has zero net displacement and reduces to the
empty word by adjacent inverse-step cancellations, which change no one-chain.
There are at most n(n-1)/2 swaps. Summing their oriented plaquettes gives an
integer chain s_gamma with

    boundary(s_gamma)=gamma,
    ||s_gamma||_1 <= n(n-1)/2 <= n^2/2.

Repeated visits and repeated plaquettes are allowed; the norm counts absolute
integer multiplicity. No choice of globally fixed gauge is used. At n=2 all
walks retrace and have zero circulation. Odd closed walks are absent in an
open cubical box. Thus only n>=4 contribute to field derivatives.

## 2. Hessian bound in units of the curl form

Let C denote the real plaquette curl and vary A in a real direction a.
Discrete Stokes and Cauchy-Schwarz give

    |a(gamma)|^2
      =|sum_p s_gamma,p (C a)_p|^2
      <= ||s_gamma||_1 sum_p |s_gamma,p| (C a)_p^2.

For a fixed plaquette p in a filling of a length-n walk, its root lies within
coordinate distance n of p's anchor, since the whole filling lies in the
walk's coordinate box. There are at most (2n+1)^d possible roots. At each
root at most (2d)^n directed words occur. Bounding
||s_gamma||_1 |s_gamma,p| <= n^4/4 yields

    |D^2 L(A)[a,a]| <= e^2 c_d,m(q) ||C a||^2,
    c_d,m(q) = (m/2) sum_(n>=4) n^3 (2n+1)^d q^n.          (B2.1)

Every coefficient of this conservative majorant is nonnegative and the series
converges for q<1. The same counting with additional powers of n justifies
termwise differentiation. The bound is uniform in A and in the box volume.
It is not a statement that every Fourier coefficient of W is nonnegative.

There is no claim of optimal mass threshold. At fixed d,m the explicit bound
vanishes as O(q^4). The absence of n=2 curl response is an algebraic
backtracking cancellation, not an assumption that two-step fermion loops vanish.

## 3. Noncompact finite-volume covariance implication

For a clean exhaustion argument, extend the internal link field A by zero to
the infinite cubical lattice and let C include every plaquette meeting an
active link. This is a specified exterior Dirichlet Maxwell boundary. It
includes the internal plaquettes used in (B2.1), so that inequality remains
valid. Work on the finite-dimensional quotient represented by
V=(ker C)^perp; C^*C is strictly positive there. Closed walks have zero
circulation along ker C, so W is well-defined on this quotient.

Define the actual finite-volume noncompact probability measure

    dmu(A)=Z^(-1) exp[-beta ||C A||^2/2] W(A) dA,  A in V.

Let alpha=e^2 c_d,m(q) and beta>alpha. Its action S has

    (beta-alpha) C^*C <= Hess S(A) <= (beta+alpha) C^*C.     (B2.2)

All eigenvalues here are on V. The determinant is bounded above and below
by finite-volume positive constants; hence the Gaussian tails justify the
integration by parts used below. For centered A and score G=grad S,

    E G=0,  Cov(A,G)=I,  Cov(G)=E Hess S.

Cauchy-Schwarz in the joint covariance block implies
Cov(A)>=(E Hess S)^(-1)>=(beta+alpha)^(-1)(C^*C)^(-1).
The Brascamp-Lieb variance inequality, with its strictly positive Hessian
hypothesis now explicit, gives the upper bound. Therefore

    (beta+alpha)^(-1)(C^*C)^(-1)
       <= Cov(A) <= (beta-alpha)^(-1)(C^*C)^(-1),
    (beta+alpha)^(-1) P_Lambda
       <= Cov(F) <= (beta-alpha)^(-1) P_Lambda,            (B2.3)
    F=C A,  P_Lambda=C(C^*C)^(-1)C^*.

These are quadratic-form bounds on centered random fields. They do not assert
pointwise positivity of every position-space correlation. An upper bound
alone would not establish long-range fluctuations.

## 4. Even Wilson realization and the infinite-volume construction

Evenness is not automatic for arbitrary complex T_xy. It holds for the
following explicit Wilson spin blocks in d=4, m=4. Choose Hermitian Euclidean
Clifford matrices gamma_mu and real t0>0,r, with

    T_(x,x+mu)=-(t0/2)(r-gamma_mu),
    T_(x+mu,x)=-(t0/2)(r+gamma_mu).

Use t=t0(|r|+1)/2 in the conservative norm hypothesis. For example,
gamma_(1,2,3)=sigma1 tensor sigma_(1,2,3), gamma4=sigma2 tensor I.
Then B=gamma1 gamma3 obeys B gamma_mu^T B^(-1)=-gamma_mu for all four.
Transposing the full site/spin matrix reverses each directed hop, so

    D(-A)=(I tensor B) D(A)^T (I tensor B)^(-1).

Thus det D(-A)=det D(A) and W(-A)=W(A). The exterior Dirichlet Maxwell
term and quotient V are also even. Every finite-volume A and F has mean zero.
This is a supplied massive Wilson realization, not the gapless symbol of
block 1. Alternatively W(A)W(-A) makes a generic model even while doubling
alpha; that distinct model must be named if used.

For any finite plaquette test f, tilt the finite-volume measure by exp(s F(f)).
The action Hessian is unchanged. Brascamp-Lieb applied to this tilted measure
gives d^2/ds^2 log E exp(s F(f)) <= (beta-alpha)^(-1)||f||^2.
The untilted mean is zero, so integrating twice gives the sub-Gaussian bound

    E exp(s F(f)) <= exp[s^2 ||f||^2/(2(beta-alpha))].       (B2.4)

It supplies volume-uniform local moments of every fixed order, tightness of
every finite collection and uniform integrability of quadratic products.

View every finite-volume F as a global field, zero outside the support of
C. The active-edge spaces for nested boxes are nested. Their curl images
are nested finite-dimensional subspaces of the global l2 plaquette space.
Their orthogonal projections P_Lambda converge strongly to P_infinity, the
projection onto the closure of the infinite curl range: finitely supported
edge fields are dense and the global curl is bounded. This argument uses
the specified exterior Dirichlet boundary, not an unproved Neumann limit.

For translation invariance, take an outer box of linear size 4L and mix
translations centered at the vertices of an inner box of linear size L.
All those centers are a distance of order L from the outer boundary. For
a fixed translated finite test, the relevant projections lie between the
projection of a centered active-edge box of size proportional to L and
P_infinity, in quadratic-form order. Strong convergence of the smaller
projection makes this sandwich uniform over the chosen centers. Means are
zero, so mixing preserves covariance bounds without an extra mean term.
The relative boundary of the inner translation set tends to zero under any
fixed translation. Hence every weak subsequential limit of these averaged
measures is translation invariant. Tightness and uniform integrability from
(B2.4) preserve the two covariance bounds,

    (beta+alpha)^(-1) P_infinity
       <= Cov(F) <= (beta-alpha)^(-1) P_infinity.          (B2.5)

The exact global Bianchi identity dF=0 also passes to the limit, since every
one of its local equations is a finite linear combination of coordinates.
This proves existence of a centered translation-invariant limiting field
distribution with the stated bounds. Uniqueness, a full DLR identification
and a continuum scaling limit are not asserted by this construction.

There is a direct orientation-by-orientation non-summability consequence.
For one fixed plaquette orientation mu<nu the Fourier diagonal of P_infinity is

    P_(mu nu,mu nu)(k)
       = (|q_mu(k)|^2+|q_nu(k)|^2)/sum_r |q_r(k)|^2,
    q_r(k)=exp(i k_r)-1,  k!=0.                            (B2.6)

This follows from the curl symbol q wedge: its nonzero squared singular
values are |q|^2, and the squared norm of the mu,nu row is the numerator.
If this orientation's centered covariance were absolutely summable, its
Fourier transform h_mu,nu(k) would be continuous. Equation (B2.5) bounds it
between (beta+alpha)^(-1)P_(mu nu,mu nu)(k) and
(beta-alpha)^(-1)P_(mu nu,mu nu)(k) almost everywhere. Continuity of both
sides away from zero extends the inequalities to every nonzero k.
Along the mu axis the projection diagonal is 1; along a third coordinate
axis rho outside {mu,nu} it is 0. Thus h_mu,nu cannot be continuous at zero.
For d>=3, every plaquette orientation therefore has a covariance that is
not absolutely summable. In d=2 the projection diagonal is 1 everywhere
away from zero and the argument gives no such conclusion.

An alternative matrix proof checks the mechanism. Under absolute summability
of every covariance component the full Fourier covariance H(k) would be
continuous. Bianchi gives q(k) wedge H(k)=0. Taking k=epsilon v forces the
range of H(0) into intersection_v ker(v wedge : exterior^2 -> exterior^3),
which is zero for d>=3. But Tr H(k)>=(d-1)/(beta+alpha) for nonzero k by
(B2.5), contradicting H(0)=0. The scalar argument above is stronger because
it excludes summability for each orientation separately.

The covariance-to-discontinuity argument is existing machinery, explicitly
used by Frohlich-Spencer, IHES/P/81/40, section 2.11, equations (2.90)-(2.92).
Its source is credited; the proposed addition here is the model-specific
massive determinant curvature bound and the matched noncompact construction,
not invention of this masslessness criterion. The pure compact covariance
bounds in that source are not imported into the present massive model.

This is a proposed non-summability theorem for Euclidean field fluctuations
of the explicitly supplied massive noncompact model. It is not an asymptotic
scaling-limit theorem, an established Hamiltonian energy-gap statement, or a
count of physical photon polarizations. Reflection positivity, transfer-matrix
matching and finite compact-payload stability remain separate obligations.

## 5. Compact and periodic boundaries

The compact cosine action is not globally convex, so replacing its Hessian
by beta C^*C is invalid. A Villain/defect expansion or another matched argument
would be needed. Periodic boxes have winding walks which need not bound a
plaquette chain; the direct global curl bound cannot silently include them.
The open/exterior-Dirichlet box is part of this supplied-model theorem.
These boundaries are not axiomatic impossibility claims.


## Current author checks and exact strict domain

The integer-chain runner exhausts closed words through length 8 in d=2 and
through length 6 in d=3,4. It constructs the oriented filling by stable axis
sorting and verifies its boundary, original coordinate-box containment and
area/swap bound. It separately retains a periodic winding word as outside
the open-box domain. These finite exhaustions challenge the signs and the
algorithm; the argument above supplies the all-length proof.

The Wilson matrix check verifies the full transpose/conjugation relation,
gamma5 Hermiticity, gauge-gradient nulls and the differentiated log determinant
against a finite-difference ladder on 2^d-vertex boxes for d=2,3,4. Its direct
curvature formula is 2 Re Tr(D^(-1) D''-D^(-1)D'D^(-1)D'). No positivity
of that curvature is claimed; both signs occur. The general majorant is
conservative by many orders of magnitude in those checks.

For d=4,m=4,q=1/20,e=1/10,beta=1, exact rational summation through n=100
and a geometric upper tail give

    alpha < 0.06616300642975 < beta.

The remaining series tail in c_d,m is below 1.46e-116. A rigorous rounded
presentation can simply use alpha<=0.066164, giving covariance comparison
constants (1+0.066164)^(-1) and (1-0.066164)^(-1). The decimal is a reported
evaluation of a declared convergent majorant, not a fitted physical coupling.
The exact rational inequalities are now checked directly before float
conversion in the exploratory runner. The tail estimate uses the positive-term ratio

    a_(n+1)/a_n <= q [(n+1)/n]^(d+3),

and its monotone decrease after the retained cutoff. The declared rational comparison and its tail estimate, rather than the
float conversion, certify this rounded strict point.
