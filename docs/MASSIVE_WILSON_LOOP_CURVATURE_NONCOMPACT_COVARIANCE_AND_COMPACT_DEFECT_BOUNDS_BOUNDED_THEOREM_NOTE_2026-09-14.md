# Massive Wilson loop curvature, noncompact covariance and compact defect bounds

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author proposal; independent scientific review is pending. The actual source
status is conditional-support. No axiom, primitive or established TOE claim
is changed.

A sufficiently massive paired lattice determinant has an explicit Hessian
bound in units of the Maxwell curl form, uniform in the field and box volume.
For a supplied noncompact Wilson model this yields two-sided field covariance
bounds and a translation-invariant limiting field distribution whose
plaquette correlations are not absolutely summable. For a supplied compact
U(1) Villain model, the same loop fillings give controlled defect-sector
ratios and a volume-uniform bound on mean squared defect density.

These are different, precisely specified models and limits. The compact
infrared phase, finite link payload and Hamiltonian correspondence are open.
An abstract signed-activity source lemma supplies a possible consumer for a
future renormalized-current representation; that representation is not proved
for the determinant-coupled model. Explicit counterexamples show why density
alone and positive determinant weights do not complete that step.

**Runner:** [self-contained primary runner](../scripts/massive_wilson_loop_curvature_noncompact_covariance_and_compact_defect_bounds_2026_09_14.py).
**Receipt:** [canonical execution cache](../logs/runner-cache/massive_wilson_loop_curvature_noncompact_covariance_and_compact_defect_bounds_2026_09_14.txt).
**Review:** [historical author review record](work_history/repo/review_feedback/pr8108-massive-gauge-evidence/REVIEW_HISTORY.md); the [preserved evidence packet](work_history/repo/review_feedback/pr8108-massive-gauge-evidence/README.md) records its original execution and reading limits.

## Premises and exact claim structure

| Input | Provenance and use | Remaining bridge |
|---|---|---|
| Cubical Euclidean box, massive hopping blocks and paired determinant | Supplied data, explicitly defined and bounded below | No native microscopic law or physical matter identification is inferred |
| Exterior Dirichlet noncompact Maxwell action | Specified boundary for the covariance exhaustion | Not the compact internal-cell boundary; no transfer matrix is supplied |
| Internal-cell compact Villain action with integer charge | Exact periodization and cochain quotient proved below | No finite Z_N regulator or compact infrared phase is established |
| Brascamp-Lieb variance inequality | Checked strictly positive finite Hessian hypotheses; primary source below | Used as existing mathematical machinery |
| Integer fillings, covariance-score identity and marginal Schur complement | Direct derivations below with separate finite challenges | General proofs still require independent review |
| Framework axioms and approved primitives | `MINIMAL_AXIOMS_2026-06-29.md`, context only | They do not select these models, states or couplings |

The common premise is the massive closed-walk expansion. Its curl Hessian
bound supports the noncompact covariance construction; its integer filling
extension separately supports compact sector and density bounds. The signed
source lemma is conditional on an additional exact generating-function
representation. Neither counterexample is a premise of the positive bounds.
No unmerged science note is a load-bearing dependency.

## Part I. Massive loops and a noncompact field distribution

### 1. Closed walks and a quantitative local filling

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

### 2. Hessian bound in units of the curl form

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
    c_d,m(q) = (m/2) sum_(n>=4) n^3 (2n+1)^d q^n.          (1)

Every coefficient of this conservative majorant is nonnegative and the series
converges for q<1. The same counting with additional powers of n justifies
termwise differentiation. The bound is uniform in A and in the box volume.
It is not a statement that every Fourier coefficient of W is nonnegative.

There is no claim of optimal mass threshold. At fixed d,m the explicit bound
vanishes as O(q^4). The absence of n=2 curl response is an algebraic
backtracking cancellation, not an assumption that two-step fermion loops vanish.

### 3. Noncompact finite-volume covariance implication

For a clean exhaustion argument, extend the internal link field A by zero to
the infinite cubical lattice and let C include every plaquette meeting an
active link. This is a specified exterior Dirichlet Maxwell boundary. It
includes the internal plaquettes used in (1), so that inequality remains
valid. Work on the finite-dimensional quotient represented by
V=(ker C)^perp; C^*C is strictly positive there. Closed walks have zero
circulation along ker C, so W is well-defined on this quotient.

Define the actual finite-volume noncompact probability measure

    dmu(A)=Z^(-1) exp[-beta ||C A||^2/2] W(A) dA,  A in V.

Let alpha=e^2 c_d,m(q) and beta>alpha. Its action S has

    (beta-alpha) C^*C <= Hess S(A) <= (beta+alpha) C^*C.     (2)

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
       <= Cov(F) <= (beta-alpha)^(-1) P_Lambda,            (3)
    F=C A,  P_Lambda=C(C^*C)^(-1)C^*.

These are quadratic-form bounds on centered random fields. They do not assert
pointwise positivity of every position-space correlation. An upper bound
alone would not establish long-range fluctuations.

### 4. Even Wilson realization and the infinite-volume construction

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
These parameters define a supplied massive Wilson realization. Alternatively W(A)W(-A) makes a generic model even while doubling
alpha; that distinct model must be named if used.

For any finite plaquette test f, tilt the finite-volume measure by exp(s F(f)).
The action Hessian is unchanged. Brascamp-Lieb applied to this tilted measure
gives d^2/ds^2 log E exp(s F(f)) <= (beta-alpha)^(-1)||f||^2.
The untilted mean is zero, so integrating twice gives the sub-Gaussian bound

    E exp(s F(f)) <= exp[s^2 ||f||^2/(2(beta-alpha))].       (4)

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
(4) preserve the two covariance bounds,

    (beta+alpha)^(-1) P_infinity
       <= Cov(F) <= (beta-alpha)^(-1) P_infinity.          (5)

The exact global Bianchi identity dF=0 also passes to the limit, since every
one of its local equations is a finite linear combination of coordinates.
This proves existence of a centered translation-invariant limiting field
distribution with the stated bounds. Uniqueness, a full DLR identification
and a continuum scaling limit are not asserted by this construction.

There is a direct orientation-by-orientation non-summability consequence.
For one fixed plaquette orientation mu<nu the Fourier diagonal of P_infinity is

    P_(mu nu,mu nu)(k)
       = (|q_mu(k)|^2+|q_nu(k)|^2)/sum_r |q_r(k)|^2,
    q_r(k)=exp(i k_r)-1,  k!=0.                            (6)

This follows from the curl symbol q wedge: its nonzero squared singular
values are |q|^2, and the squared norm of the mu,nu row is the numerator.
If this orientation's centered covariance were absolutely summable, its
Fourier transform h_mu,nu(k) would be continuous. Equation (5) bounds it
between (beta+alpha)^(-1)P_(mu nu,mu nu)(k) and
(beta-alpha)^(-1)P_(mu nu,mu nu)(k) almost everywhere. Continuity of both
sides away from zero extends the inequalities to every nonzero k.
Along the mu axis the projection diagonal is 1; along a third coordinate
axis rho outside {mu,nu} it is 0. Thus h_mu,nu cannot be continuous at zero.
For d>=3 under the preceding even-model hypotheses, every plaquette
orientation therefore has a covariance that is
not absolutely summable. In d=2 the projection diagonal is 1 everywhere
away from zero and the argument gives no such conclusion.

An alternative matrix proof checks the mechanism. Under absolute summability
of every covariance component the full Fourier covariance H(k) would be
continuous. Bianchi gives q(k) wedge H(k)=0. Taking k=epsilon v forces the
range of H(0) into intersection_v ker(v wedge : exterior^2 -> exterior^3),
which is zero for d>=3. But Tr H(k)>=(d-1)/(beta+alpha) for nonzero k by
(5), contradicting H(0)=0. The scalar argument above is stronger because
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

### 5. Compact and periodic boundaries

The compact cosine action is not globally convex, so replacing its Hessian
by beta C^*C is invalid. A Villain/defect expansion or another matched argument
would be needed. Periodic boxes have winding walks which need not bound a
plaquette chain; the direct global curl bound cannot silently include them.
The open/exterior-Dirichlet box is part of this supplied-model theorem.
These boundaries are not axiomatic impossibility claims.


### Current author checks and exact strict domain

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

    alpha < 0.066164 < beta.

The remaining series tail in c_d,m is below 1.46e-116. A rigorous rounded
presentation can simply use alpha<=0.066164, giving covariance comparison
constants (1+0.066164)^(-1) and (1-0.066164)^(-1). The decimal is a reported
evaluation of a declared convergent majorant, not a fitted physical coupling.
The exact rational inequalities are now checked directly before float
conversion in the primary runner. The tail estimate uses the positive-term ratio

    a_(n+1)/a_n <= q [(n+1)/n]^(d+3),

and its monotone decrease after the retained cutoff. The declared rational comparison and its tail estimate, rather than the
float conversion, certify this rounded strict point.

## Part II. Compact Villain sectors

### 1. Exact extension of the determinant on physical Villain sectors

Use the full internal cochain complex of a contractible rectangular box,
with C=d1 from links to plaquettes and D2=d2 from plaquettes to three-cells.
This is a different boundary convention from the exterior Dirichlet Maxwell
exhaustion in the noncompact field construction. Normalize compact charge to
integer e=1; weak coupling is controlled by beta in the Maxwell term.

Precisely, integrate theta over T^E with normalized link Haar measure and
sum an integer plaquette cochain n. The supplied joint measure is

    dmu_V(theta,n)=Z_V^(-1) W(theta)
       exp[-beta ||C theta+2pi n||^2/2] product_l dtheta_l/(2pi),
    n in Z^P, theta_l in [-pi,pi), F=C theta+2pi n.

Equivalently its theta marginal has weight W(theta) times the product over
plaquettes of the periodized Gaussian. The joint definition specifies the
real Villain field F and defect current m=d2 n used below. Representative
changes in theta shift n by an integer exact cochain and preserve F.

For each rooted closed fermion walk gamma choose the integer plaquette
filling s_gamma from the stable-axis construction. The convergent log-loop
expansion defines a real function on all real plaquette fields,

    L_tilde(F)=2 Re sum_gamma a_gamma exp(i<s_gamma,F>).

Here a_gamma includes the exact spin trace, M^(-length), alternating log
sign and 1/length. At F=C theta+2 pi n with integer plaquette n,

    exp(i<s_gamma,F>)=exp(i<gamma,theta>).

Hence exp L_tilde(F) equals the paired massive determinant on EVERY Villain
sector. The statement uses integer charge and integer filling multiplicities;
a generic real charge in the same 2pi convention would not obey it.

The area/incidence proof applies to arbitrary plaquette variations u, giving

    |Hess L_tilde(F)[u,u]| <= c_d,m(q)||u||^2.

No Bianchi condition on u is needed. The coefficient series and derivative
series converge uniformly per plaquette by the same polynomial-times-q^n
majorant. The extension away from physical affine sectors depends on filling
choice, but all its physical sector values are the original determinant.

For the d=4 Wilson blocks with real r,t0 every spin trace is real: expand the
product in real Clifford coefficients, reduce every gamma word to a signed
ordered Clifford monomial, and use zero trace for every nonempty monomial.
For a nonempty ordered monomial of even degree choose a contained gamma;
for odd degree choose an absent gamma (odd degree is at most 3 in d=4).
Conjugation by that gamma reverses the monomial sign, proving its trace
vanishes. The identity monomial has trace 4. Thus the spin trace is real.
Each loop then contributes a real coefficient times cos(<s_gamma,F>), so
L_tilde is even on the FULL plaquette space. This coefficient-level argument
is stronger than evenness restricted to exact fields. Generic complex
hoppings require a separate evenness proof or an explicitly evenized model.

Set S(F)=beta||F||^2/2-L_tilde(F), beta>c=c_d,m(q). Then, on the full
plaquette vector space,

    kappa I <= Hess S(F) <= K I,
    kappa=beta-c>0, K=beta+c, S(-F)=S(F).

### 2. Marginal curvature without a volume prefactor

Decompose plaquette space orthogonally as X=range C and Y=X^perp. For y in Y
set

    Z(y)=integral_X exp[-S(x+y)] dx, R(y)=-log Z(y).

Gaussian tails and bounded derivatives justify differentiation. For vectors
v in Y the exact second derivative is

    R''[v,v]=E S_yy[v,v]-Var(S_y[v]).

Brascamp-Lieb in x bounds the variance by
E <S_xy v,S_xx^(-1) S_xy v>. Thus R'' is bounded below by the expectation
of the Schur complement of S_xx in Hess S. Since Hess S>=kappa I,
min_u <(u,v),Hess S (u,v)> >=kappa||v||^2; its minimizer is exactly the
Schur-complement quadratic form. The upper bound follows by dropping the
nonnegative variance. Consequently

    kappa I_Y <= Hess R(y) <= K I_Y.

Evenness implies R'(0)=0. Integrating along the segment from zero to y gives

    exp[-K||y||^2/2] <= Z(y)/Z(0) <= exp[-kappa||y||^2/2].  (7)

The ratio is for an actual constrained marginal. Comparing separate
Gaussian partition functions would instead introduce an unjustified
volume-growing factor and is not the argument used here.

### 3. Periodization and integer sector labels

Let Gamma=C Z^E, an integer lattice spanning X. Push normalized link Haar
measure on T^E through C to Haar measure on X/(2pi Gamma). Decompose the
Villain integer plaquettes into cosets [n] in Z^P/Gamma and unfold the
fundamental domain separately in each coset. This gives a common
sector-independent covolume factor times

    sum_[n] Z(2pi Q n), Q=I-P_X.

The tangent shift 2pi P_X n is absorbed in x. Gauge-kernel multiplicities
are accounted for by the Haar pushforward; no unnormalized gauge volume
is silently set to one. The factor is 1/covol(2pi Gamma), for Euclidean Lebesgue measure on X.
It cancels in all sector ratios. Surjectivity of the pushforward follows
because every x in X has a real link preimage; changing that preimage by
2pi integer links changes x by 2pi Gamma.

For the full cell complex of a contractible box, integral cellular
cohomology H^2=0 gives ker(D2 over Z)=C Z^E. Thus the sector label is
m=D2 n, with one coset per admissible integer three-cochain m. H^3=0
identifies the admissible set with ker d3 in dimensions where that next
map is present. An explicit integer contracting homotopy proves these claims. On an interval,
let h:C^1->C^0 be (hf)(x)=sum_(t=0)^(x-1) f(t), and let pi on C^0
replace a function by its value at the base vertex, with pi=0 on C^1.
Then dh+hd=I-pi. On the graded tensor product of d interval complexes use

    H=h_1 tensor I + pi_1 tensor h_2 tensor I + ...
      + pi_1 tensor ... tensor pi_(d-1) tensor h_d.

The tensor differential has its usual degree signs. The displayed h_i terms
are graded tensor maps; the preceding pi factors force preceding degrees
to zero whenever the term is nonzero. Cross terms cancel by the graded
Leibniz rule and the interval identities telescope, giving

    dH+Hd=I-pi_1 tensor ... tensor pi_d.

All matrices have integer entries. On a closed positive-degree cochain z,
the final projection vanishes, so z=d(Hz) with an INTEGER primitive. This
establishes exactness over the integers, including degree 2 and degree 3;
real rank counts would not suffice. The integer-matrix check in the primary runner verifies
the full identity on boxes in dimensions 2,3,4 and checks unit nonzero Smith
invariant factors on the one-interval boxes.

Writing y_m=2pi Q n, (7) compares each actual determinant-coupled defect
sector with the no-defect sector. Since D2 P_X=0 and ||D2||^2<=4d,

    ||y_m||^2 >= (pi^2/d)||m||^2,
    w(m)=Z(y_m)/Z(0) <= exp[-a||m||^2],
    a=kappa pi^2/(2d), w(0)=1.                            (8)

The operator-norm estimate follows by compression of the infinite cubical
exterior derivative, whose Fourier norm is at most |q(k)|<=2sqrt(d).

### 4. A density bound, not a phase theorem

Let N3>0 be the number of three-cells and Qm=||m||^2. If N3=0, there
are no defect cells and the density conclusion is vacuous. For 0<s<a, the normalized
sector ensemble obeys

    E exp(s Qm) <= [sum_(z in Z) exp(-(a-s)z^2)]^N3,

because its partition function is >=w(0)=1 and dropping the integer
closed-current constraint only enlarges the numerator. Jensen and s=a/2 give

    E Qm/N3 <= (2/a) log theta(a/2)
                <= 4 exp(-a/2)/[a(1-exp(-3a/2))],         (9)
    theta(b)=sum_(z in Z) exp(-b z^2).

The last estimate uses z^2>=1+3(z-1) for positive integers z and log(1+x)<=x.
For d=4,m=4,q=1/20,beta=100, the exact majorant certificate
c<=6.6164 gives kappa>=93.3836. In (9), a>115 using pi>3.14.
The positive rational Taylor partial sum through degree 200 proves
exp(57.5)>9*10^24, and exp(172.5)>100 already follows from 1+172.5.
Consequently the displayed upper bound is strictly less than 4*10^(-27).
This is a conservative supplied-model parameter point, not a physical fit.

Occupied-current-cell density is also bounded by this expression, since a
nonzero integer component has square at least one. This bound is independent
of volume and does not assert that the whole finite box is defect-free.

### 5. Exact stronger consumer still missing

The full Villain field obeys dF=2pi m, so the exact Bianchi identity used in
the noncompact non-summability theorem no longer holds. Conditional covariance
at fixed defect sector gives Cov(F|m)>=K^(-1)P_X by the same score
argument on X. Total covariance preserves this transverse lower bound, but the defect
contribution can fill the vanishing Fourier directions. Projecting to P_X F
would restore closure at the price of a nonlocal observable; that does not
solve the local-field problem.

A possible terminal estimate is a small long-wavelength current covariance,
schematically Cov(m) <=epsilon d2 d2^* with sufficiently small epsilon.
Along an axis outside a tested plaquette plane, dF=2pi m would then bound
that plaquette's Fourier covariance above by 4pi^2 epsilon. Its transverse
lower bound is 1/K, so 4pi^2 epsilon<1/K would preserve a directional
separation. This is a proposed consumer, not a proved implication for the
actual interacting current ensemble until its limiting and normalization
hypotheses are established. Density (9) alone supplies no such estimate.

Summing closed interacting monopole loops with a controlled area/response
bound remains the phase task. Positivity, convexity and the individual
sector Gaussian comparison do not automatically supply positive Fourier
type or an infrared-uniform cluster expansion. No axiom update follows.

### 6. Two distinct inference controls

Part III gives a stationary ensemble of
closed integer currents with component second moment rho and required
infrared-response coefficient at least rho L^3/2. It is a comparison
ensemble, not the determinant-coupled gas. The finite direct-boundary Fourier
check verifies the area enhancement and exact integer conservation. Thus
one must use more of the actual action than density and closedness.

Positive Fourier type also fails for a supplied member of the actual Wilson
family. On a single open square, with four spin components, r=2,t0=2,M=80,
exact integer complex-matrix determinants obey

    det D(flux 0)  =2793699536637539555790009139456,
    det D(flux pi) =2793707190016896642234870398976.

Both are positive, the second is strictly larger, and M>8*t0*(|r|+1)/2.
The paired weight therefore has W(pi)>W(0). A continuous function of positive
Fourier type would obey |W(phi)|<=W(0). This supplies an actual family
counterexample to an unrestricted positive-Fourier-type import; it does not
settle the special r=1 family, and does not disprove phase stability.
The source proof in Frohlich-Spencer section 2.12 uses positive Fourier type
at equation (2.99). Its use for the present family needs replacement or a
separately verified narrower hypothesis.

A full four-dimensional box gives a second certificate, with all 16 vertices
of {0,1}^4, the same r=2,t0=2 and M=10000. Change one corner link from +1
to -1. The length-two trace is unchanged and the exact fourth-power trace
difference is -1344. Therefore the leading change in log W is +672/M^4.
Both log-series tails together, starting at length 6 by bipartiteness, are
bounded by (4*64/6)q^6/(1-q), q=24/M. Exact rational comparison gives

    log W(flipped link)-log W(all links +1)
       >=672/M^4-(4*64/6)q^6/(1-q)>0.

This verifies the obstruction on a full d=4 box, using an independent finite
trace/remainder certificate rather than an ill-conditioned float subtraction.

## Part III. Why closed-current density does not control response

On the dual Z^4 lattice choose the oriented boundary j_L of an L by L square
in the 1,2 plane, with 4L unit current edges. For every translated square
anchor x take independent centered integer variables Z_x distributed as the
difference of two Poisson(lambda/2) variables. Thus E Z_x=0 and Var Z_x=lambda.
Define the stationary integer current j=sum_x Z_x tau_x j_L. Each edge sees
only finitely many terms (2L in each of the two active orientations), so this
is a well-defined translation-invariant probability field. Every square
boundary is divergence-free, hence delta j=0 exactly. Lattice Hodge duality
identifies it, up to orientation shifts and signs, with an integer closed
three-cochain m.

For either active edge orientation,

    E j_e^2=2L lambda.

Set lambda=rho/(2L), for arbitrary rho>0. Every component's second moment is
then at most rho, and P(j_e !=0)<=rho. This is a uniform small-density bound,
including integer-current conservation.

Use Fourier convention sum_x f(x) exp(-i k.x), q_mu=exp(i k_mu)-1. The square
surface is a product of geometric sums S_L(-k_1)S_L(-k_2), with
S_L(k)=sum_(r=0)^(L-1) exp(i k r). Its boundary Fourier vector obeys

    jhat_L,1 = (1-exp(-i k_2)) S_L(-k_1) S_L(-k_2),
    jhat_L,2 = -(1-exp(-i k_1)) S_L(-k_1) S_L(-k_2),

for the square with bottom edge in the positive 1 direction. Its squared
norm is (|q_1|^2+|q_2|^2)|S_L(k_1)S_L(k_2)|^2, and it is transverse in the
matching divergence convention. The current spectral covariance is exactly

    H_j(k)=lambda jhat_L(k) jhat_L(k)^*.

For k=(u,0,0,0), its active transverse eigenvalue divided by |q(k)|^2 is
lambda L^2 |S_L(u)|^2. Consequently

    lim_(u->0) ||H_j(u,0,0,0)||/|q(u,0,0,0)|^2
       =lambda L^4=rho L^3/2.

Any inequality H_j(k)<=epsilon |q|^2 P_transverse(k), equivalently the
Hodge-dual current-response comparison, requires epsilon>=rho L^3/2.
At fixed arbitrarily small density rho this necessary coefficient is
unbounded as L grows. Thus density and exact closedness alone cannot supply
the small response coefficient needed by the proposed compact photon
consumer. A quantitative large-loop area or susceptibility bound is essential.

This ensemble is intentionally not claimed to satisfy the derived sector
weight comparison or the Wilson determinant action. It does not show that
the actual model lacks a compact Coulomb phase, or that any axiom is wrong.
The affirmative alternative is to exploit the actual loop-energy penalty
and control the area-weighted response, as in the pure-model renormalized
current machinery, with the determinant perturbation's hypotheses checked.

## Part IV. Signed activities and a shifted-source lemma

Let Q be a positive definite real matrix on a finite-dimensional vector space
V. Let B:V->R^r have rows b_j, and let z_j be real with |z_j|<1. Put

    v_j(u)=-log(1+z_j cos u),
    eta_j=|z_j|(1+|z_j|)/(1-|z_j|)^2,
    R=diag(eta_j),
    I(theta)=integral_V exp(-a.Qa/2) product_j[1+z_j cos((Ba)_j+theta_j)] da.

Terms with z_j=0 can be deleted. Every integrand is strictly positive, and
v_j is smooth and even. Direct differentiation gives

    v_j''(u)=(z_j cos u+z_j^2)/(1+z_j cos u)^2,
    |v_j''(u)|<=eta_j.

Assume the explicit matrix inequality B^* R B<=delta Q for some 0<=delta<1.
The action for the normalized a-integral has Hessian at least (1-delta)Q,
uniformly in theta. All derivatives and integrations by parts are justified
by the Gaussian tail and the bounded periodic factors.

For a phase-direction h in R^r, differentiating the integral gives

    D^2 log I(theta)[h,h]
       =-E sum_j v_j'' h_j^2 + Var(sum_j v_j' h_j).

The variance is nonnegative, proving the lower bound -h.Rh. For the upper
bound apply Brascamp-Lieb in a. With D=diag(v_j''),

    Var(sum_j v_j' h_j)
       <=(1-delta)^(-1) E h.D B Q^(-1) B^* D h.

The hypothesis implies ||R^(1/2) B Q^(-1/2)||^2<=delta. Thus
B Q^(-1) B^*<=delta R^(-1), and D R^(-1) D<=R. Therefore

    -R <= Hess_theta log I(theta) <= R/(1-delta).             (10)

Evenness under (a,theta)->(-a,-theta) gives grad log I(0)=0. Integrating
(10) along the segment from zero to theta yields the all-source ratio bounds

    exp(-theta.Rtheta/2) <= I(theta)/I(0)
       <=exp(theta.Rtheta/[2(1-delta)]).                     (11)

Negative activities are explicitly allowed. The upper ratio may exceed one;
positive Fourier type, which would force the upper ratio to be at most one
for the pure shift integral, is not assumed or concluded.

### Mixtures and distinct current/source maps

Let G be positive definite on a finite-dimensional source space. Suppose
an actual generating function admits a finite or convergent positive
mixture representation

    M(h)=exp(h.Gh/2) [sum_gamma c_gamma I_gamma(U_gamma h)]
                           /[sum_gamma c_gamma I_gamma(0)],
    c_gamma>=0,  0<sum_gamma c_gamma I_gamma(0)<infinity,

where every I_gamma has the preceding form, each B_gamma^*R_gamma B_gamma
is <=delta Q_gamma with the same delta<1, and

    U_gamma^* R_gamma U_gamma <=epsilon G

uniformly in gamma. The source map U_gamma need not equal the current map
B_gamma; replacing it by B_gamma without proof would be an error. The
normalized weights c_gamma I_gamma(0) are positive and sum to one. Applying
(11) separately before summing gives

    exp[(1-epsilon)h.Gh/2] <= M(h)
       <=exp[(1+epsilon/(1-delta))h.Gh/2].                   (12)

For 0<=epsilon<1, differentiation at h=0 proves a strictly positive lower
covariance comparison and a finite upper comparison with G. Uniform
integrability or finite-dimensional analyticity must justify differentiation
for an infinite mixture; it follows, for instance, from the displayed
uniform Gaussian moment-generating bounds in a neighborhood of zero.

This is a sufficient consumer for a renormalized-current expansion. It
requires positive mixture coefficients, uniformly small weighted current
forms AND source forms, and exact equality for the generating function.
A partition-function identity alone is insufficient, since the local
Gaussian integration used to renormalize currents can change inserted
observables. A signed fermion-loop expansion does not automatically supply
positive mixture coefficients merely because the original determinant
weight is positive. These are still actual-model proof obligations.


## Evidence, falsifiers and verification limits

The self-contained runner contains seven finite challenge families. Integer
chains are checked through closed-word length 8 in d=2 and length 6 in d=3,4.
Full Wilson matrices on 2^d vertices test charge conjugation, gauge nulls and
log-determinant differentiation against a step ladder. A scalar massive ring
provides a separate exact determinant and Gaussian covariance check, including
the score integration-by-parts identities. It is a diagnostic, not a replacement
for the Wilson family in Part I.

Integer matrix identities and Smith forms check the cochain quotient. A
separately constructed six-face/twelve-edge cube curl verifies the rank-five
projection and 5/(6 beta) constrained face variance used in the marginal. Compact
one-face periodization and a six-face cube marginal are compared with analytic
Gaussian formulas; reported numerical tail estimates use a positive floor to
avoid reporting floating underflow as a zero tail. The strict example density
bound uses rational inequalities, including a positive exponential Taylor
partial sum. It is not inferred from numerical sampling.

The full four-dimensional positive-type counterexample uses exact small
integer matrix powers and a rational log-series remainder. The comparison
current ensemble uses direct oriented square boundaries and Fourier sums.
Signed-source integrals use finite Fourier expansions and separate Gaussian
quadrature, with two distinct source/current maps and a positive mixture.
No Monte Carlo fit, extrapolated gap or PASS count supplies a phase proof.

The proposal fails if the stable-axis filling leaves its box or has the wrong
boundary, if the claimed uniform incidence bound fails, if gauge fixing does
not meet the covariance hypotheses, if the integer periodization has missing
sectors or normalization factors, or if the signed-source variance bound fails
under its explicit matrix condition. Independent review must check these
all-volume implications and the weak-limit argument directly. The finite
checks do not establish independence or exhaust all possible proof errors.

## No-Go Discipline Gate

### N1 — Actual alternative routes

| Route | Status | Result or precise remaining obligation |
|---|---|---|
| Massive closed-walk determinant expansion | ATTEMPTED, positive in scope | Explicit curl and full-plaquette Hessian majorants |
| Noncompact covariance and exhaustion | ATTEMPTED, positive in scope | Two-sided bounds and nonsummable orientation correlations for the supplied limiting field |
| Compact periodization and defect sectors | ATTEMPTED, positive in scope | Integer quotient, marginal curvature and uniform mean squared density bound |
| Density plus conservation as an infrared criterion | ATTEMPTED, inference refuted | Dilute large-square currents have unbounded required response coefficient |
| Positive-type import for the full Wilson family | ATTEMPTED, inference refuted | Exact r=2 examples with weight increasing away from zero links |
| Signed-source convexity replacement | ATTEMPTED, conditional positive lemma | Needs an exact actual-model generating representation and two small weighted forms |
| Matched compact-current expansion and Hamiltonian limit | OPEN | Determinant-coupled large-loop response, finite-payload stability and transfer matching |

### N2 — Relations among remaining conditions

The compact current response and compact infrared control are one coupled
phase problem, denoted I. Hamiltonian/continuum matching H and native model
selection/physical identification P are distinct obligations whose logical
independence is not proved.

| Pair | First closes second? | Second closes first? | Independence proved? |
|---|---|---|---|
| I, H | unresolved | unresolved | unresolved |
| I, P | unresolved | unresolved | unresolved |
| H, P | unresolved | unresolved | unresolved |

### N3 — Hidden-condition scan

The mass inequality, hopping norm, integer compact charge, even Wilson
coefficients, boundary choices, field observables and order of limits are
explicit. Strict convexity is proved for the noncompact and extended actions,
not substituted for the compact cosine action. Translation averaging proves
existence of a limiting field distribution; it does not establish uniqueness,
DLR identification or physical reflection positivity. The source lemma assumes
positive mixture coefficients and exact generating-function equality, not just
positive original determinant weights. No framework law is silently supplied. The scan
found "canonical" only as the descriptive execution-cache label; it supplies
no scientific premise.

### N4 — Residual and source matching

The main finite-clock note controls a different supplied regulator and leaves
its phase open. The constrained-fiber KP note concerns another high-mass,
small-beta regime. Frohlich-Spencer's source bounds concern pure compact gauge
models; the positive-type step and renormalized-current hypotheses are not
imported for massive matter. Dimock's bounded-field massive noncompact RG
paper supplies prior context, not an unexamined theorem premise. The present
covariance/discontinuity argument is credited as existing machinery.

| Citation location | Residual or statement examined | Claimed closure | Match |
|---|---|---|---|
| Carlen-Cordero-Erausquin-Lieb, PDF pp. 1-6, variance inequality (1.3) | Finite strictly convex variance bound | That inequality only; the note verifies its hypotheses | yes |
| Frohlich-Spencer, preprint pp. 45-46, (2.90)-(2.92) | Covariance comparison implies directional Fourier discontinuity | Prior method credited; no charged compact bound imported | yes, method only |
| Frohlich-Spencer, preprint p. 48, (2.99) | Positive-type source upper step | Identifies an assumption; no actual-model closure claimed | yes, limitation only |
| Dimock 1988, text pp. 2-13 | Massive noncompact effective-action prior context | None; incomplete formula reading cannot certify a theorem import | context only, not witness support |
| `U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:104` | Fixed-coupling clock comparison and open thermodynamic phase | None; this milestone does not close that carrier's phase | context only, not witness support |
| `WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md:64` | Different high-mass/small-coupling domain | None; no compact weak-coupling import | context only, not witness support |
| `MINIMAL_AXIOMS_2026-06-29.md:116` | Admissibility does not select a Hamiltonian or process | None; supplied model assumptions remain explicit | yes, framework context only |

### N5 — Resolution and rhetoric

The runner reports per_element, per_site, per_mode, per_block and lattice_wide
certificates with the relevant scope. Lattice-wide means the analytic
volume-uniform estimates and specified limiting distribution. It does not mean
a compact Hamiltonian photon has been established. The two counterexamples
reject named inference rules and do not exclude the actual model's phase.

### N6 — Partial closure remains available

The signed-source lemma may replace one positive-type step after a valid
renormalized representation is constructed. A controlled large-loop area bound,
a narrower verified hopping family, direct infrared RG, or a matched transfer
construction may advance the remaining task. None is ruled out. There is no
request for an axiom or primitive update.

### N7 — Hostile steelman

A reviewer should reject the conclusion that a defect density below 4e-27
proves a compact Coulomb phase. That inference is explicitly refuted by the
comparison family. A reviewer should reject applying the signed-source lemma
to the actual determinant without its mixture and source-map hypotheses.
Those hypotheses remain open. Euclidean nonsummability is not by itself an
identified Hamiltonian energy gap or physical polarization count.

### N8 — Cross-cycle distinction

Earlier finite-time cutoff bounds and fixed-box oscillator comparisons do not
supply this volume-uniform massive determinant estimate. Conversely this
noncompact Euclidean distribution does not upgrade the earlier finite cyclic
carrier's ground phase. The new compact density result removes one quantitative
uncertainty while leaving the response task explicit. No repeated open
condition is counted as a new independent obstruction.

Gate disposition: author scope review of these bounded implications; no broad
negative theorem is submitted. Independent scientific review is pending.

## References and exact use

- [Carlen, Cordero-Erausquin and Lieb, covariance estimates of Brascamp-Lieb type](https://arxiv.org/abs/1106.0709), pages 1-6: checked variance inequality and strict Hessian hypotheses. The covariance-score lower bound and marginal calculation are displayed directly here.
- [Frohlich and Spencer, IHES/P/81/40](https://omeka.ihes.fr/files/original/c59d65f61f9b1aba2d8eb6f4c01ceb88.pdf), section 2.11: prior covariance/discontinuity criterion; section 2.12, especially (2.99): the positive-type step whose assumptions require a new check. No numerical renormalized-activity constant is imported.
- [Dimock, bounded-field infrared QED](https://numdam.org/item/AIHPA_1988__48_4_355_0.pdf), introduction and section 2 text: prior massive noncompact gauge-invariant effective-action context. Missing image equations were not treated as verified theorem hypotheses.
- `U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`: repository comparison, not a compact phase premise.
- `WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md`: different coupling region and constrained-fiber model.

## Review and source trace

All evidence is author-generated. The seven families contain separate finite
representations, not seven independent reviews. The source and runner require
independent review before effective retention. No editable prompt or workflow
file is changed by this proposal. The packet records source revisions,
reading limits, corrections and recovery paths.

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A controlled interacting charged gauge phase on a supplied finite-payload carrier, with matched local observables and physical identification."
source_of_blocker_text: "frontier_question"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently review the massive loop, covariance and compact sector bounds; construct and test the actual-model infrared response and Hamiltonian bridges."
conditional_surface_status: "Supplied massive Euclidean paired determinant, explicit boundary and coupling domains; noncompact limiting covariance and compact sector-density bounds, with the compact infrared phase and finite-payload Hamiltonian matching open."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Direct conditional mathematical implications, an abstract source consumer and two explicit inference counterexamples; author checks do not grant retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
