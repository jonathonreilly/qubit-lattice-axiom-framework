# All-order link-ball traces and the Gaussian cutoff component

**Author mathematical unit; fresh independent review pending.** The new
estimates below control every order of weak differentiation of a product of
single-link HS balls. They retain all sphere intersections. For a normalized
Gaussian, exact marginalization pays the determinant and complex mean on the
active failed links only; this gives a convergent connected cutoff expansion.
A separate finite-range version has complete original-data reader supports.
The actual Yang–Mills nonlinear chart integral is not proved to satisfy that
connected estimate. Its all-order trace bound, full covariance chain rule,
and remaining summation/normalization requirement are stated explicitly.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
independent_review: pending
bare_retained_allowed: false
audit_required_before_effective_retained: true
full_existence_established: false
physical_continuum_mass_gap_established: false
```

The target remains full four-dimensional SU(N) existence **and a positive
physical continuum mass gap**. The Wilson action, paired normalized S4-prime
kernel and original cut are supplied model data. No physical axiom, empirical
number or new primitive is introduced. Bałaban and Dimock are credited for
the localization and small/large-field architecture. Lohmann's
[arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1), Theorem 1,
§2.1.4, Proposition 3 and Remarks 2/10 motivate the weak-cutoff construction.
His theorem is not imported: its analytic norms and positivity hypotheses
are not established here for the complete Yang–Mills consumer. The proofs
used in this note are given below.

## 1. Actual input, exact normalization, and covariance contract

The fully read starting source is
[PS](PROBABILITY_SENSITIVE_RETURN_ASTRA.md), 544 lines, SHA256
`6ef027d54bd0ca1948444c9b82c673ed0cae2e23cd59b25f0c53498194e9b18b`.
Its PS19/PS20 are open specifications, not inputs that have been proved.
The [read manifest](checks/chart_boundary_forest_read_manifest.json) records
actual ranges and hashes of the consumed CB/SA/CS/FR producers.

For fixed N>=2, odd L>=3, T>=2 and real t=kappa u, put D=N^2-1,
`n=(3L^4+1)T^4`, `d=Dn`, and `sigma^2=N/u`. The pinned axial-tree quotient
has unit Haar Jacobian and unit integrated nonroot gauge volume. Every free
link, colour, root and harmonic direction remains. The lift has internal
links I and crossing links V_c. Each actual paired path equals V_c there.
CB's lifted two-block fillings exclude the extra far seam when T=2.

In the fixed scalar HS coordinates, the actual phase is

    F_epsilon(a)=sigma^2[-log w_epsilon(exp(a)U0,V)
                                      -sum_e log j_N(a_e)],
    w_epsilon=exp[-u sum_p(1+epsilon_p)s(U_p)] product_c k_t(V_c;M_c),
    k_t(V;M)=exp[-t(1-Re tr(V^-1 M)/N)]/N_t(M).             (BF1)

Only original Wilson coefficients vary. The complete compact N_t, Haar log
and vacuum stay in F. In particular the actual lift Hessian is

    K=H_V+E_V+kappa(1-c_N(kappa u))B_V+N^2/(6u)I,
    ||E_V||_(row/column,HS)<=24 delta_V,
    ||F_0'(0)||_(infinity,HS)<=6sqrt(N)delta_V.             (BF2)

CB's flat-brick recovery gives a positive gap before the curvature error;
its local centered normalizer/Haar analytic bounds give the coefficients
used by PS9. SA keeps their full original readers. CS15 retains the compact
normalizer even for degenerate means; none of its interacting tail estimates
is inserted into a Gaussian probability below. USM, read separately, concerns
the **u-stripped tree phase** and explicitly omits the finite-u spread term.
It supplies no finite-u Hessian or minimizer to this argument. FR9 compares
polynomial moments only; no arbitrary finite-chart reader is extended to an
uncut Gaussian by that formula.

With auxiliary radius r_a and `R=r_a/(2sigma)`, let
`D_R=product_e B_R^D`, the ORIGINAL unwhitened product ball. The exact PS5 is

    Z_a=P_a integral_D_R g_(K^-1)(x)
                   exp[-ell.x-x^T E x/2-R_epsilon(x)] dx,
    P_a=h_N^n(2pi sigma^2)^(d/2)det(K)^(-1/2)
                                        exp[-F_epsilon(0)/sigma^2]. (BF3)

Here ell=sigma^-1 F_epsilon'(0), E is the source Hessian, and
R_epsilon starts in degree three. The original cut is automatic on this
auxiliary chart under PS's margins. G and Omega are unchanged, and their
complements, outside-chart integral and every retained history remain as in
PS6. The current theorem inserts no history.

All covariance estimates below use the **actual deformation's** constants.
For every finite index set A and every parameter value used, require constants
c,U fixed before u and T with

    C=C^T,   Re C>=c I,   ||C||_2<=U,   c>0,
    a=c/U^2,                b=1/c.                        (BF4)

The same holds for principal C_A. Indeed, for y=C_A x,
`Re(y* C_A^-1 y)=Re(x* C_A* x)>=c||x||^2>=c||y||^2/U^2`,
and `||C_A^-1||<=1/c`. Thus `Re C_A^-1>=aI` and its norm is <=b.
The normalized density uses the determinant branch continued from positive
real C. There is no normality assumption. A complex covariance here is an
analytic functional, not a probability measure.

BF4 is an explicit hypothesis on a full-reader deformation. This note does
not consume the concurrent positive-reader covariance or critical-center
candidate. In particular its a may be much smaller than PS's gamma.
Whenever BF4 replaces PS12, the regulator choices must be redone against a,
as done in §5. No old two-unit support-weight margin is assumed. X and A below are sets of
free links; H_e and Y are sets of original level-zero coarse boxes. Rates in
reader norms refer to those original boxes. To use PS's coefficient bound
expressed in fixed R_A-boxes at an original-box rate beta, fill each R_A-box
and evaluate that bound at beta_box=beta(2R_A)^4. Its constants may grow but
remain finite; this is a conversion of the local-vertex majorant, not an
upgrade of a covariance tail's available rate.

## 2. Gaussian derivatives with square-root factorial growth

For a finite link set A, m in C^(D|A|), and K_A=C_A^-1, write

    g_(C_A,m)(x)=det(2pi C_A)^(-1/2)
                     exp[-(x-m)^T K_A(x-m)/2],
    c_g=2b^2/a+b,               L_g=max(1,sqrt(2e c_g)).    (BF5)

All transposes inside the analytic quadratic form are bilinear. For every
scalar multi-index nu, uniformly in finite A,

    |partial^nu g_(C_A,m)(x)|
      <=(b/(2pi))^(D|A|/2) exp[c_g||m||_2^2]
             L_g^|nu| sqrt(nu!) exp[-a||x||_2^2/4].        (BF6)

This includes the entire determinant. To prove it, put w=z-m. Cauchy--Schwarz
and Young's inequality give

    Re[(x+w)^T K_A(x+w)]
      >=(a/2)||x||^2-(2b^2/a+b)||w||^2.

Consequently the modulus of the Gaussian at x+z is bounded by its displayed
determinant times `exp[-a||x||^2/4+c_g||m||^2+c_g||z||^2]`.
For a coordinate differentiated k>0 times, choose the Cauchy circle of radius
`sqrt(k/(2c_g))`. The derivative factor is
`k! (2c_g/k)^(k/2) exp(k/2)<= (2e c_g)^(k/2)sqrt(k!)`,
using `k!<=k^k`. Undifferentiated coordinates need no circle. Multiplying
proves BF6. These radii may grow with the derivative order because the
Gaussian is entire. A fixed-radius Cauchy estimate would unnecessarily
produce k!, and can destroy covariance Taylor summation.

Let eta_e(x_e)=1_{|x_e|>R}; replacing strict by nonstrict boundaries changes
no Gaussian integral. Give a finite ordered list of scalar derivative legs
at each link e, of length k_e. Let B be the set with k_e>0 and r=sum k_e.
Choose the first leg j_e at each e in B and let nu be the list left after
removing it. Weak differentiation gives EXACTLY

    <product_(e in A) partial^(k_e) eta_e, g_(C_A,m)>
       =(-1)^(r-|B|) integral_(sphere_R^B x outside_R^(A\B))
             product_(e in B)n_(e,j_e) partial^nu g_(C_A,m). (BF7)

This notation records the specified scalar components, not radial
k_e-th derivatives. It follows from `partial_j eta_e=n_j dS_R` and moving
every subsequent derivative onto the smooth test function. Since a cutoff
reads one whole link only, these moves never differentiate another link's
cutoff. There is one sphere per touched link, and all products of spheres
are retained. No derivative of a surface normal is dropped: the higher
normal/surface distributions are precisely represented by their action in
BF7. Approximation by compact test functions and Gaussian decay justifies
the unbounded exterior integrals.

Put `omega_D=area(S^(D-1))`, and suppose max_e||m_e||_2<=M. Define

    q_R=(b/(2pi))^(D/2) exp(c_g M^2-aR^2/8)
                  max{omega_D R^(D-1),(8pi/a)^(D/2)}.     (BF8)

Integrating BF6 on BF7 proves, at EVERY derivative order,

    |<product_e partial^(k_e) eta_e,g_(C_A,m)>|
      <=q_R^|A| L_g^r product_(e in B)sqrt((k_e-1)!).      (BF9)

For an untouched exterior coordinate reserve `exp(-aR^2/8)` and integrate
`exp(-a|x|^2/8)` over R^D. For a sphere use its exact area and the same
reserved exponent. The remaining scalar factorials obey
`nu!<=product_(e in B)(k_e-1)!`. This proves BF9, including r=0.
Its force and determinant price is **|A|-dimensional**, not all-volume.
That statement relies on the exact Gaussian marginal below.

## 3. Exact force completion, marginalization, and every covariance chain rule

If Q=K+E is invertible on the chosen analytic branch and C=Q^-1, completing
only the quadratic part in BF3 gives the exact identity

    Z_a=h_N^n(2pi sigma^2)^(d/2)det(Q)^(-1/2)
         exp[-F_epsilon(0)/sigma^2+ell^T C ell/2]
         integral_D_R g_(C,m)(x) exp[-R_epsilon(x)] dx,
    m=-C ell.                                             (BF10)

No domain has moved. The factor `exp(ell^T C ell/2)` and the full Q determinant
are retained; they can be extensive and are not called small. This is a
Gaussian completion, not a claim that m is the nonlinear critical point.
For the Gaussian part alone define

    J_G=integral_D_R g_(C,m),
    F_A=integral_(outside_R^A) g_(C_A,m_A).                 (BF11)

Then `J_G=sum_(A subset links)(-1)^|A| F_A`, with F_empty=1.
Integrating all coordinates outside A gives exactly the principal covariance
C_A and mean m_A. For real positive C this follows by completing the square
in the complementary coordinates (the Schur complement inverse is C_A).
For complex accretive C and complex m it follows by analytic continuation:
the whole-space Gaussian is dominated on compact parameter neighborhoods,
its mass is one, and the real identity extends to the connected accretive
matrix domain. Equivalently differentiating its mass by a covariance or mean
parameter gives a vanishing whole-space derivative. Determinant branches
match at positive real C. Thus BF8 contains no hidden unused-mode factor.
With exp[-R_epsilon(x)] present, this marginal identity is unavailable.

For completeness, here is the full chain rule needed for actual reader
weakening. Let z_1,...,z_k be independent parameters, C(z),m(z) smooth near
the evaluated point, and H(x,z) a compact piecewise smooth insertion. For
nonempty B subset {1,...,k}, define

    D_B=(1/2)(partial_B C):partial_x partial_x
                            +(partial_B m).partial_x.     (BF12)

Differentiation of the normalized Gaussian determinant and inverse gives
its heat identity. Repeated differentiation and the ordinary product rule
then give

    partial_J integral g_(C,m) H
      =sum_(S subset J) sum_(pi partition of S)
            <product_(B in pi) D_B partial_(J\S)H,g_(C,m)>. (BF13)

All x derivatives on H are weak derivatives. The empty partition is the
identity. One can verify every multiplicity by introducing labelled formal
increments dz_j: the translated Gaussian density is generated by the
commuting operators `(Delta C):partial^2/2-(Delta m).partial` on the density;
extract the coefficient containing each dz_j once, then integrate by parts.
A partition block is one differentiated C or m. This also proves BF13 by
induction without a formal infinite-series convergence assumption.

In the centered PS convention set m=0 and H=1_D_R f_z. Then BF13 includes
all derivatives of f_z. For f_z=exp(-V_z),
`partial_J f_z=f_z sum_(pi partition J)product_(B in pi)(-partial_B V_z)`.
Here V_z includes the weakened force, source Hessian and nonlinear vertices.
If the completed mean is used, `partial_B m=-sum_(A subset B)
(partial_A C)(partial_(B\A)ell)`; the two zero-order factors are included.

In particular, if a full-reader atom is multiplied by
`zeta_a(s)=product_(e in tau(S_a))s_e`, then `partial_B C` contains that atom
whenever B is a subset of its tree, even for |B|>1. For the simple term
`C_a s_e s_f`, the mixed second derivative contributes
`C_a:partial_x^2/2` in addition to the product of two first-derivative
operators. Dropping this term is not a forest identity.

BKAR uses derivatives in **independent pair coordinates**, followed by
evaluation at the path-minimum matrix. It does not differentiate the minimum
map. A direct derivative in a tree-edge t instead reads the chain rule
`sum_(pairs pq) partial_(s_pq) H partial_t s_pq`; on each strict ordering
chamber the latter derivative is the indicator that t is the path minimum.
Higher direct derivatives can have distributions on tie walls. None is
replaced here by PS14's single independent-pair derivative.

## 4. Two genuinely summed Gaussian cutoff results

### 4.1 Correlated Gaussian, with field supports

Assume BF4 for C and a volume-uniform scalar colour sum

    c_row=sup_e sum_(f!=e) sum_(alpha,beta)|C_(e alpha,f beta)|<infinity.

For a forest mask s on links, `C_s(e alpha,f beta)=s_ef C(e alpha,f beta)`.
Write s as the Gram matrix of unit vectors v_e. The isometry
`W(e alpha)=e alpha tensor v_e` gives `C_s=W*(C tensor I)W`.
Thus Re C_s>=cI and ||C_s||<=U, including all principal compressions.
The same a,b in BF8 apply. Keep m fixed in this endpoint interpolation.

For a nonempty X define the activity

    a_X=(-1)^|X| sum_(T tree on X) integral_[0,1]^T
                          partial_T F_X(s^T) dt.          (BF14)

For |X|=1 there is the empty tree and a_X=-F_X. Finite forest interpolation,
factorization at disconnected masks, and BF11 give EXACTLY

    J_G=sum_(families of disjoint nonempty X) product_X a_X. (BF15)

Here is a proof of the interpolation algebra used. For the monomial
`H(s)=product_e s_e^(m_e)`, give each present edge an independent clock with
CDF t^(m_e). Its maximum spanning forest is unique almost surely. Conditional
on that forest's clocks, a nonforest clock must be no larger than the minimum
on its forest path. Its CDF supplies precisely the path-minimum monomial;
the forest-edge densities supply the independent derivatives. Summing these
disjoint probabilities proves the formula for monomials, hence polynomials.
Smooth tensor-polynomial approximation, with derivatives through the finite
forest order, proves it for smooth H. Only jets at the compact forest-mask
locus enter. If the Gaussian is defined only in its open accretive
neighborhood, extend it smoothly to the cube, identically near that locus,
before this argument; the chosen extension cannot change the result.
No nonpositive covariance in the rest of the cube is integrated.

Let c_ef be the scalar colour sum in c_row. A tree T on n>=2 links supplies
2n-2 field legs. BF9 gives

    |a_X|<=q_R^n L_g^(2n-2)
               sum_T product_(ef in T)c_ef
                              product_e sqrt((deg_T(e)-1)!). (BF16)

This is an estimate for all n, with the exact D colours already summed.
For a fixed labelled tree, summing its nonroot positions by stripping leaves
costs at most c_row^(n-1). Dropping distinctness only enlarges the bound.
Prüfer coding gives

    sum_(labelled T) product_e(deg_T(e)-1)!
                  =(n-2)! binomial(2n-3,n-1).

Indeed the occurrence counts in the Prüfer word sum to n-2; for fixed counts
there are `(n-2)!/product counts!` words. Multiply and sum the compositions.
The square-root factorials in BF16 are smaller. Dividing by (n-1)! for the
unlabelled nonroot positions and using the binomial bound 4^(n-1), for q_w=
exp(w)q_R and lambda=4 L_g^2 c_row q_w<1, we obtain

    sup_e sum_(X contains e) exp(w|X|)|a_X|
       <=q_w[1-log(1-lambda)]<=q_w/(1-lambda).             (BF17)

Thus for any output rate mu>=0 and any slack alpha>0, if BF17 with
w=mu+alpha is <=alpha, this Gaussian cutoff gas has a connected logarithm.
The criterion eventually holds when `aR^2/8-c_g M^2` tends to infinity faster
than log R, with fixed D,a,b,c_row,mu,alpha. In the actual Gaussian part,
`M<=sqrt(D) M_C C_1(1+rho)delta_V/sigma=O(p)` if a full scalar row bound M_C is supplied;
`R^2=O(u)` and p a fixed logarithmic power meet this condition for large u.
The exact quadratic reference in BF10 stays outside this small logarithm.

BF17 controls **field sets X**. If C or m reads distant original V, its a_X
still does too. Giving a_X only its field endpoints is not a source-local
return theorem. This paragraph is a limitation of the theorem just proved,
not a claim that localization is impossible.

### 4.2 Finite-range Gaussian with complete original readers

There is a directly usable source-local special case. Suppose for each link
e there is a fixed connected original-box set H_e containing its field
owner, with |H_e|<=h and at most J such labels through one box. Suppose
m_e reads only H_e; C_ef reads only H_e union H_f; and C_ef=0 whenever
H_e and H_f are disjoint. Assume the label-overlap graph has maximum degree
Delta, and BF4/BF8 hold on a common analytic original-source/data domain.
These are extra finite-range hypotheses; they are not asserted for K^-1.

For each nonempty connected set A in that overlap graph, put

    b_A=(-1)^|A| F_A,        support(b_A)=H_A=union_(e in A) H_e. (BF18)

The density marginal for disconnected A is block diagonal and factors.
Grouping BF11 by overlap components therefore proves an exact hard-core gas
with activities b_A and disjoint full supports H_A. These activities are
holomorphic on the stipulated domain by their fixed exterior integration
and Gaussian domination. No hard indicator is declared holomorphic after
moving a coarse datum: the analytic object is this integrated marginal.

Write K_Delta=max(1,Delta)^2. A connected n-link set containing a specified
link has at most K_Delta^(n-1) possibilities: choose its deterministic
rooted spanning tree and encode the depth-first walk of length 2n-2.
The walk determines its visited set and at each step has at most Delta
choices. Anchoring a box by one of its at most J incident H_e gives

    sup_v sum_(A:H_A contains v) exp(beta|H_A|)|b_A|
       <= J exp(beta h) q_R/[1-K_Delta exp(beta h)q_R].     (BF19)

For beta=mu+alpha, any alpha>0, the right side <=alpha proves a connected
original-reader logarithm at rate mu. Thus this theorem can use a tiny
positive available support rate: take 0<alpha<beta and mu=beta-alpha.
There is no requirement that beta exceed two. All constants h,J,Delta may
be large, but are fixed before u,T. The finite-range core of a proposed
covariance construction is an intended future application only; its signed
nonlocal tail and the mean it induces are not deleted to claim that
application here.

For reference, the elementary gas argument behind both conclusions is as
follows. Expand a finite hard-core gas into ordered tuples and sum connected
incompatibility graphs in its logarithm. The absolute connected coefficient
is bounded by the sum of incompatibility spanning trees. To see this, order
vertices, root at the least, and map a connected graph to the tree whose
parent of i is its least-labelled neighbor one level nearer the root in
breadth-first distance. For a fixed tree T, the permitted optional edges
join equal levels, or join i to a previous-level vertex whose label is no
smaller than its tree parent. Adding these edges changes neither distances
nor least parents; every graph giving T is in exactly this interval. Intersect
its upper endpoint with the fixed incompatibility graph. The alternating sum
over an interval is zero or has modulus one. Summing intervals proves the
tree bound. For an activity
of support S, the rooted tree recursion is bounded by
`|a_S|exp(mu|S|) exp(sum_(B incompatible S)T_B)`.
The hypothesis `sup_v sum_(B contains v)|a_B|exp((mu+alpha)|B|)<=alpha`
makes `T_S=|a_S|exp((mu+alpha)|S|)` a supersolution, since incompatibility
can be charged through the |S| boxes. Iteration from the bare activity proves
absolute convergence. The connected series exponentiates to the finite gas
near zero activities by the graph identity; absolute convergence uniformly
under multiplying all activities by |t|<=1 extends that equality to t=1.
Consequently the gas is nonzero on the stated analytic domain. This proves
the logarithm assertion without borrowing RD's two-unit convention.

## 5. The actual nonlinear chart: all orders, with its unpaid price visible

The product geometry also supplies an all-order estimate for BF3 itself.
It does not supply its connected summation. Fix an analytic field-circle
radius h_f>0, independent of u,T. Rechoose r_a and a fixed positive rho so
that the actual PS coefficient majorant satisfies

    eta_beta(2r_a)+C_2 rho/2<=a/64,
    sigma h_f<=r_a/2,       2r_a<a_0 (the scalar analytic radius). (BF20)

The first two choices are possible because eta_beta(r)=O(r); the last
sigma condition holds at sufficiently large u. The force bound remains
PS10. This explicitly replaces PS11's gamma threshold by the possibly much
smaller BF4 constant a. The original G and Omega are not altered by this
choice; their inclusion in the auxiliary chart still needs PS's margins.

For the weakened local phase on a finite component X, set
`f=exp(-ell.x-x^T E x/2-R_epsilon(x))`. At every real x in its product balls
and every complex |z_i|<=h_f, the same coefficientwise AM--GM proof as PS9
at radius r_a+2sigma h_f gives

    |f(x+z)|<=M_X exp[a||x||^2/16],
    M_X=exp[16||ell||^2/a+a D|X| h_f^2/16].                (BF21)

Indeed the nonlinear plus source-quadratic coefficient is <=a/64, and
`||x+z||^2<=2||x||^2+2D|X|h_f^2`. Apply
`|ell_i x_i|<=a|x_i|^2/32+8|ell_i|^2/a` and
`h_f|ell_i|<=8|ell_i|^2/a+a h_f^2/32`.
This proof works coefficientwise under modulus-one full-reader atom
weakening. No interaction supremum at the large boundary is called small.

Take any r labelled field derivatives of `1_D_R f`. First assign each leg
to f or to its link's cutoff. At each touched cutoff keep one first leg,
`partial_j 1_B=-n_j dS`, and integrate every remaining cutoff derivative
onto the Gaussian or f. This gives an exact sum of at most 4^r patterns;
each has a set B of distinct sphere links, the other links staying in their
balls, and smooth derivative orders totalling k_e-1_{e in B} at link e.
All corner products are present. Applying BF6 with mean zero, Cauchy to
BF21, and the product integration bound gives for EACH such pattern

    absolute value <= E_X H^r
                 product_e (k_e-1_{e in B})! t_R^|B|,
    H=max(1,L_g,h_f^-1),
    E_X=(8b/a)^(D|X|/2) M_X,
    t_R=(a/(16pi))^(D/2) omega_D R^(D-1) exp(-aR^2/16).    (BF22)

To verify the constants, the product integrand after the two Cauchy bounds
has exponent at most `-3a||x||^2/16`. Bound each ball integral by
`(16pi/a)^(D/2)` and each sphere integral by
`omega_D R^(D-1)exp(-aR^2/16)`; the determinant prefactor combines with the
former to give `(8b/a)^(D|X|/2)`. The factorial inequality is
`sqrt(zeta!)mu!<=product_e(k_e-1_{e in B})!`.
For t_R<=1, the sum of all patterns with at least b_0 spheres is bounded by
`E_X(4H)^r product_e k_e! t_R^b_0`. This is a bound for every r, not merely
for each fixed order followed by an unspecified constant.

BF13 supplies the exact conversion from independent reader-parameter
forests to these field derivatives, including the derivatives of the local
interaction. Original Wilson-source derivatives follow by Cauchy between
nested fixed source discs, with their explicit source factorials. They do
not change the hard chart. Each differentiated coefficient keeps its actual
full reader S; a union is used only when those coefficients are multiplied.
The scalar colour contractions and partition multiplicities in BF13 remain
to be summed. BF22 pays the indicated spheres but its B=empty terms have
none. Crucially,

    log E_X includes 16||ell_X||^2/a
           <=(16/a)D|X| C_1^2(1+rho)^2 delta_V^2/sigma^2.  (BF23)

On delta_V<=c sigma p this may grow as |X|p^2. There is no normalized
interacting marginal identity cancelling it. BF22 is an all-order analytic
trace producer, not PS20 and not a volume-uniform return activity.

## 6. An exact vector-ball shift with all side and corner chains

A useful alternative to leaving BF23 in a modulus estimate is to recenter
and retain the side chains explicitly. The geometric identity itself needs
no minimizer theorem. Let F(z)dz_1...dz_D be holomorphic on the whole sweep
of B_R by -tm, 0<=t<=1, with m in C^D. Then

    integral_(B_R-m) F(z) dz
      =integral_(B_R) F(y)dy
         -integral_0^1 integral_(sphere_R)(m.n(y))F(y-tm)dS dt. (BF24)

The left side means the translated real chain with its translation
orientation. Differentiate `integral_B F(y-tm)dy` in t and use the real
divergence theorem on the holomorphic components; integration in t proves
BF24 and its sign. Tensoring this identity over links expands a translated
product into all products of interiors and side chains, with sign
(-1)^(number of sides). Translation has Jacobian one. A side link retains
its factor m_e.n_e, its t_e integral, and its whole colour sphere.

For BF10 the substitution y=x-m changes the actual domain to D_R-m.
BF24 is applicable to its smooth chart integrand if the entire swept domain
is inside the original analytic chart. That is a separate checked condition,
for example `sigma(R+max_e|m_e|)` below its analytic link radius. Applying
BF6 on a side pays a factor `|m_e| omega_D R^(D-1)` and an exponential
`exp[-aR^2/8+C|m|^2]`, together with the other retained factors. Parameter
derivatives act on m, on this factor, and on F(y-tm); parameterizing the
fixed spheres makes all these terms explicit. No old white cube is moved.
Additional hard plaquette/history indicators are not holomorphic F and are
not transported by BF24. This identity is offered for a future same-component
critical reference construction; that construction is not assumed here.

## 7. Exact remaining inequality and failed shortcuts

For the actual full-reader covariance family, define the labelled derivative
terms by BF13, using every full reader S_a of C, ell and phase atoms. For a
forest edge set J, a term selects a subset S, a partition pi of S, and one
actual coefficient atom in each derivative D_B, plus the corresponding
phase derivative partition. Its field legs and corners are evaluated by
BF7/BF22. The support is the union of all selected full readers and field
owners. These data give an explicit majorant, rather than an endpoint-only
replacement covariance.

What is still needed is a bound, on one common original-source/coarse domain,
for the EXACT resulting connected component integrals A_Y with their own
same-component reference, of the form

    sup_v sum_(Y contains v) exp((mu+alpha)|Y|) sup_D |A_Y|
                    <=alpha,                 alpha>0,    (BF25)

with 0<mu+alpha below the actual available reader rate. In trying to prove
BF25 from the present work, the concrete unsummed terms are the BF13
partition/atom sums with the BF22 factor E_X and with no guaranteed sphere
in their B=empty part. For a covariance `C_core+sum_a C_a` the independent
weakening additionally contains `partial_B C_a` for every B subset of its
support tree. One atom can connect many reader boxes while differentiating
only one link's cutoff, so a count of forest vertices is not a count of paid
sphere witnesses. The finite-range BF19 argument does not bound those terms.

This is a narrower residual than an unspecified all-order cutoff derivative:
BF7, BF9 and BF22 have proved the weak-derivative and trace step for all
orders; BF13 fixes the chain rule; BF17 actually sums every Gaussian endpoint
tree, and BF19 closes the finite-range reader case. BF25 for the original
nonlinear/full-reader family remains a new connected estimate. Its reference
cancellation cannot be replaced by BF23, a real GC/CS probability under a
different law, or the product factorization R17. Arbitrary histories, the
unchanged G/Omega boundaries, outside-chart integration, effective-level
closure, continuum existence and the physical mass gap remain further work.

Two attempted shortcuts were discarded explicitly. Fixed-radius Cauchy on a
Gaussian gives (2k)! for k repeated covariance insertions; division by k!
can make that *bound* divergent even though the exact covariance dependence
is analytic. BF6's optimized radii remove that artificial factorial loss.
Completing the force and then integrating out inactive coordinates succeeds
for BF11; with a nonlinear reader it is not a marginal identity. BF24 gives
a possible contour route, while keeping its side chains and reader problem.
Neither failed bound is a no-go theorem, and no attack family is declared
exhausted.

No numerical experiment was needed or run. The results are analytic author
proposals, with independent review pending. Source identities and the scoped
search are recorded in the read manifest; the
[author freeze](checks/chart_boundary_forest_receipt.json) binds this note.
The immutable methodology revision is
`01589af3faf806b736c42dc2f3bd625e9edead9f`, with the lane's
[PROCESS_LIGHT](PROCESS_LIGHT.md). The coordinator owns Git, locks, shared
fronts, PR #10114 and review. This author edits only this file and
checks/chart_boundary_forest_*; it assigns no LAND or audit verdict.

**Review request:** independently check the optimized Cauchy factorial in
BF6, distributional sign and corner identity BF7, active-marginal force and
determinant accounting, the complete partition chain rule BF13, tree and
reader combinatorics BF17/BF19, the changed regulator threshold BF20, the
nonlinear all-order envelope BF22/BF23, and the vector-ball contour BF24.
The full requested Yang–Mills proof remains open.
