# Nonlinear two-step response on a fixed compact-coordinate chart

Author derivation, 2026-11-08. Research checkpoint; the fresh-context
mathematical check and corrected scope are in `../gates/forest-flat-check.md`.
This is a theorem about a specified restricted component of the actual compact
chain. The complementary compact fields are not discarded from the full target.
The full connected-support return norm remains open.

Prior-art reconciliation: draft `89faef229ff6e6bde42baad15ed8270c2f4087d8`,
GLOBAL_RETURN_HISTORY_ASTRA section 16 already gives convexity, variance and
simultaneous tails for its actual inherited second-chart law. The present
argument uses the joint two-layer terminal-root quotient and a fixed Cartesian
cube, proves spatial covariance decay and two-source/one-boundary response,
and does not import that draft's producer-domain or remainder claims.

## 1. Precise statement

Use the two-step SU(2) chain of the main two-region note, with fine side
N=L^2 m, m>=3, odd L>=3, beta=u and both kernel strengths kappa u, for
fixed kappa>0. Use the single shared gauge group and the periodically translated
coordinate-order fine trees rooted at terminal vertices from the flat two-step
proof (a particular forest allowed by `compact-forest-exchange.md`). All intermediate
links remain coordinates. Each remaining compact link is exp(i a_e dot sigma).
Let Omega_delta be the Cartesian cube |a_e,r|<delta for every coordinate.
Take terminal V_e=exp(i v_e dot sigma), with |v_e,r|<delta. The coordinate cube
and forest do not change when V or sources change.

Let mu_delta,V be the quotient posterior on the retained a coordinates,
conditioned on this cube and including its product exponential-coordinate
Haar density. The observables f,g in (C1) are functions of a. The original
conditioned law also has its independent Haar orbit variables; a gauge-variant
observable on that larger space retains the separate orbit covariance from
the compact forest proof. No Wilson action
is inserted at the intermediate layer. There exist delta>0, u_*>0, alpha>0,
depending on L,kappa but not m, such that for u>=u_* and observables
f,g in C^1(closure Omega_delta),

  |Cov_mu(f,g)| <= 4/(u g_*) exp[-alpha d(A,B)]
                          ||grad f||_L2(mu) ||grad g||_L2(mu).       (C1)

Here A,B are their actual terminal-block coordinate supports, d is the
nearest-neighbor terminal-block distance, and g_*=g(L,kappa)>0 is the
variational gap proved for the actual two-step flat operator in
`flat-two-step-bound.md`. Constants are existence constants, not evaluated
numbers. The minimum over Bloch momentum in that proof is not a physical gap.

For a unit-speed tangent change of one terminal link c, write
A_c=D_c log k_(kappa u)(V_c;M_c(U_1)). The normalizer is independent of its
output V_c, so A_c=kappa u <D_c V_c,M_c>, exactly. For each bounded local
C^1 f with a fixed gradient bound, (C1) bounds D_c E_mu f=Cov_mu(f,A_c) with a constant
independent of u and volume, decaying in the distance from f to c's readers.

For two bounded C^1 original gauge-invariant observables F,G, restricted to
the quotient chart, the complete mixed source/one-boundary coefficient is

 D_c partial_s partial_t log Z_delta(V;s,t)|_(s=t=0)
     = kappa_3,mu(F,G,A_c).                                    (C2)

It obeys the explicit bound (C10) below, uniformly in u and volume. Z_delta
is the full restricted, unnormalized integral with exp(sF+tG), including all
normalizers and Haar densities. Source-independent does not mean ignorable
for Z_delta: all its source coefficients are retained.

This statement does not give a full compact-chain covariance, an estimate
uniform over arbitrary terminal fields, an all-depth result, or the parent's
exponential norm in complete connected reader size.

## 2. Uniform normalizer estimates

Let Z(z)=int_SU2 exp(z w(q))dq and h(z)=log Z(z)-z. Under Haar,
X=1-w(q) has density (2/pi)sqrt(x(2-x)), 0<=x<=2. Thus

 h(z)=log int_0^2 exp(-zx)(2/pi)sqrt(x(2-x))dx.                  (C3)

For every fixed integer n>=0 there is C_n<infinity such that the tilted
moments satisfy E_z X^n <= C_n(1+z)^(-n), z>=0. Here is a direct proof.
For z>=1, the denominator is bounded below by integrating 0<=x<=1/z,
where sqrt(2-x)>=1 and exp(-zx)>=exp(-1); this is a fixed positive
multiple of z^(-3/2). The numerator is at most (2sqrt(2)/pi) times
int_0^infinity exp(-zx)x^(n+1/2)dx = const_n z^(-n-3/2).
For 0<=z<=1, use X<=2 and enlarge the constant. No asymptotic equivalence
is used. Differentiation gives h^(r)(z)=(-1)^r cumulant_r(X). The finite
partition formula for cumulants and the preceding moment bounds imply

 |h^(r)(z)| <= C'_r(1+z)^(-r), r=1,2,3.                      (C4)

Consequently, on r>=1/2, the first three r-derivatives of h(t r) are bounded
uniformly over t>=0. This includes t=0 by continuity. The bounds on the
derivatives of the soft normalizer do not grow like t^r after its linear
part has been included in the leading action.

## 3. Actual nonlinear Hessian

Write M_c(a), r_c=|M_c|, and psi_M(V)=r-<V,M>. In the forest coordinates
the exact negative log density relative to Lebesgue, up to an a-independent
constant, is

 S_u,V(a)=u Phi_V(a) + sum_(h,c) h(kappa u r_(h,c)(a))
                       -sum_e log j(a_e),
 Phi_V=W(U_0)+kappa sum_(h,c) psi_(M_(h,c))(U_(h+1,c)),
 j(a)=(sin |a|/|a|)^2.                                      (C5)

At h=1 the output is V. Formula (C5) follows by the exact identity
-t<V,M>+log Z(t r)=t psi_M(V)+h(t r); no normalizer is absent.

Each contour has at most ell=5L-4 occurrences. If sqrt(3)ell delta<1/2,
telescoping products of unitary matrices gives ||T-I||<=sqrt(3)ell delta,
and hence r>=1/2. On this fixed neighborhood Phi is a smooth local function.
Its Hessian at a=0,V=I is precisely H_min of the flat two-step proof.

There are finitely many local factor types, each with a bounded number of
coordinate occurrences depending only on L, and bounded incidence per
coordinate (six Wilson plaquettes, at most eight input kernel footprints,
and at most one output kernel). Repeated path edges are counted with their
multiplicity. Compactness of a slightly larger neighborhood with r>0 gives
a finite C_3(L,kappa) such that the absolute row and column sums obey

 ||Hess Phi_V(a)-H_min||_op <= C_3 delta.                     (C6)

To make this step quantitative in its meaning, define C_3 as the maximum,
over these finitely many factor types on the larger closed neighborhood,
of the sums of absolute third derivatives times their coordinate counts
and incidence, including derivatives in the output v. This finite maximum
is independent of the torus volume. The mean-value theorem and Schur's
test prove (C6). It is not claimed to be a numerically evaluated constant.

(C4), bounded first and second derivatives of r on r>=1/2, and the same
incidence count bound the operator norm of the Hessian of sum h by C_N(L).
The Haar term has bounded Hessian C_J on |a|<=sqrt(3)delta<pi. Choose
delta small enough that C_3 delta<=g_*/4 and then
u_*>=max(1,4(C_N+C_J)/g_*). Equations (C5),(C6) imply, throughout the cube,

 Hess S_u,V >= (u g_*/2) I.                                 (C7)

The Hessian has range at most two in terminal-block labels. Its absolute
row and column sums are at most u C_H(L,kappa), by the same finite local
derivative argument, for u>=u_*. This is an estimate on the actual
nonlinear restricted density; it is not inferred from the flat Hessian
without a neighborhood/error bound. The cube is convex in a coordinates.

## 4. Covariance estimate on the fixed cube

For clarity, the needed weighted covariance argument is included. This is
the finite-dimensional Helffer--Sjoestrand/weighted Brascamp--Lieb method;
the argument below checks the fixed-cube boundary conditions rather than
importing a whole-space formula without them.

Let L_0=-Delta+grad S dot grad be the nonnegative Neumann operator in
L2(mu). Let T have the componentwise differential expression
(-Delta+grad S dot grad)I+Hess S on vector fields, with the mixed domains
specified next; it is not the Neumann operator tensor I. On each cube
face normal to coordinate i, vector component i has Dirichlet boundary
condition and the other components have Neumann boundary condition. For
a smooth Neumann test u, differentiating its equation gives
grad L_0 u=T grad u with these mixed conditions. Integration by parts
gives the quadratic form

 <v,Tv>=sum_i E|grad v_i|^2+E[v^T Hess S v] >= m||v||^2,
 m=u g_*/2.

The scalar Bochner identity on the flat faces gives
||L_0 u||^2=E||Hess u||_HS^2+E[grad u^T Hess S grad u].
There is no negative boundary curvature term. The cube has a positive
Neumann spectral gap by compactness and a positive smooth density; applying
this identity to eigenfunctions shows that this gap is at least m. One
can first use smooth face-compatible functions and close the forms; the
codimension-two edges add no boundary integral. Thus for centered f the
Neumann Poisson solution exists and

 Cov_mu(f,g)=<T^-1 grad f,grad g>.                            (C8)

For W_i=exp[alpha d(block(i),A)], W commutes with the scalar differential
part and preserves the mixed boundary conditions. Its conjugation changes
only the Hessian. The absolute row/column bounds and range two give

 ||W T W^-1-T|| <= u C_H (exp(2alpha)-1).

Choose alpha>0 so this is <=u g_*/4=m/2. A bounded perturbation of T
then gives ||W T^-1 W^-1||<=2/m. Apply this to grad f, whose support is A,
and pair with grad g on B to obtain (C1). The same proof with principal
coordinate domains works with fixed small-chart collars and holes, if
every coefficient reader stays in the same stated neighborhood; it does
not allow a rough field in such a collar without a new estimate.

## 5. Two sources and a boundary insertion

The region Omega_delta is fixed in a as V,s,t vary. Compact differentiation
therefore has no moving-domain term. With sources on the original U0,
all exact source derivatives of log Z_delta are the corresponding
cumulants of the actual restricted measure. In particular (C2) follows.
The two-source coefficient is Cov_mu(F,G); normalizing any retained coarse
conditional subtracts the full source-dependent log normalizer, as in the
landed two-region proof. No conditional covariance is replaced by a product
of conditional means.

Put B_c=A_c/u. Its sup norm and coordinate-gradient norm have a bound
depending only on L,kappa and the chosen unit tangent, since its readers
are those of the last contour mean. Define N(f)=||f||_infinity+
||grad f||_infinity, where the latter is the Euclidean norm over its
actual coordinates. For bounded C^1 f,g,h, the identity

 kappa_3(f,g,h)=Cov(fg,h)-E f Cov(g,h)-E g Cov(f,h)             (C9)

and (C1) imply a bound with coefficient 16/(u g_*) times
N(f)N(g)N(h) and exp[-alpha d(S_h,S_f union S_g)]. Permute the three
functions and choose the strongest separation. Consequently

 |kappa_3(F,G,A_c)| <= (16/g_*) N(F)N(G)N(B_c)
                    exp[-alpha D_sep],
 D_sep=max_i d(S_i, union_(j!=i) S_j),
 (S_1,S_2,S_3)=(supp F,supp G,readers B_c).                  (C10)

For uniformly bounded support diameters this is summable in the position
of c and decays in separation of F,G (polynomial volume factors can be
absorbed by decreasing alpha). Constants depend on their support sizes
and norms, not on the total torus volume or u. This is a three-insertion
spatial estimate, not an exponential norm in arbitrary polymer size.

## 6. The full compact complement and the attempted extension

Let E be the fixed quotient-chart event, p=pi_V(E), mu_E=pi_V(.|E),
mu_B=pi_V(.|E^c). For every bounded f,g the complete covariance is

 Cov_pi(f,g)=p Cov_E(f,g)+(1-p)Cov_B(f,g)
       +p(1-p)(E_E f-E_B f)(E_E g-E_B g).                    (C11)

The same decomposition must be differentiated for source/boundary
responses; p depends on these parameters. For the covered smooth quotient
observables, (C1) bounds only its first term.
A bound on one bad-coordinate probability cannot bound the global event
E^c uniformly in volume. In fact, at each fixed finite u the compact
quotient factors have bounded local log oscillation, so each coordinate
has a uniformly positive conditional probability of lying outside the
chart, independent of total volume. Iterated conditioning bounds pi(E)
above by (1-c(u,delta,L))^n for n selected distinct compact link coordinates. This
uses a lower bound for each full conditional and the tower property, not
independence of the posterior coordinates. It invalidates the attempted
global-good-event completion as a thermodynamic argument.

For the proposed expansion route, the next attempt needs local good-region
estimates with complete bad-component weights. Other all-compact methods
have not been ruled out. The principal-domain version after (C8) offers a local
supplier only when its reader collar is controlled. The normalized joint
weights of rough components, source insertions on their boundaries, and
their iteration are not bounded by the present argument. The exact compact
forest identity remains valid on those fields. No full compact response,
two-step connected-support closure, or Yang--Mills mass gap is claimed.
