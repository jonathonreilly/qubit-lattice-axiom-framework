# Nonlinear chart estimates for the two-plaquette terminal marginal

Author proof, 2026-11-09. Conditional finite-model mathematics; independent
checking pending. This concerns the actual normalized marginal rho_J, restricted
to a fixed chart. It does not confer retained status or physical identification.
Assigned source revision: `fbdfb3c1b8852e5de302fab6f0f7cfc70ba04cac`.

## 1. Inputs, quantified domain, and exact density

Fix odd L>=3, kappa>0, m>=3, fine torus side N=L²m, u>=1. Use the
supplied actual two-layer SU(2) model and terminal-root fine forest, with
arbitrary internal spanning trees. All intermediate links and all non-tree
fine links are coordinates; tree links equal I. J consists of the seven
terminal edges bounding two adjacent distinct elementary plaquettes; O is
its complement. Only terminal kernels in J are deleted, including their
normalizers. q_u and every level-zero kernel remain. Terminal outputs in O
are V_c=exp(i v_c dot sigma). Put U_e=exp(i a_e dot sigma).

Inputs read in full, relative to this pack (SHA-256):

- `parts/two-plaquette-compact-coercivity.md`:
  `b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e`.
- `parts/partial-terminal-normalizer-hessian.md`:
  `a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139`.
- `parts/nonlinear-chart-response.md`:
  `5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1`.

Repository AGENTS.md, SCIENCE_WORKFLOW.md and workhorse/SKILL.md were also
read. Parent supplied preflight and science lease; no numerical job is used.
The first input's compact theorem is an explicit mathematical dependency,
not independently re-proved here. The exact kernel, path length, reader
locality and quotient-Haar descriptions of these inputs are the model data.
Parent's completed literature pass found the undeleted chart proof closest;
general whole-space Helffer--Sjoestrand/Brascamp--Lieb results and
Kolesnikov--Milman smooth-boundary results do not supply the cube-domain
step automatically. The proof below uses the weighted-resolvent idea of
Helffer--Sjoestrand and supplies that step directly, importing no covariance
or boundary theorem from those works.

Let M_h,c be the actual positively weighted path mean, r_h,c=|M_h,c|,
Z(s)=integral exp(s w(Q))dQ under probability Haar, h(s)=log Z(s)-s,
and j(a)=(sin|a|/|a|)². Define

 E_J,V(a)=W0(a0)+kappa sum_all level-0 c (r_0,c-<U1,c,M0,c>)
                       +kappa sum_c in O (r_1,c-<V_c,M1,c>).

Up to an a-independent constant the exact negative logarithmic density is

 S(a;v)=u E_J,V(a)+sum_all level-0 c h(kappa u r_0,c(a))
                     +sum_c in O h(kappa u r_1,c(a))
                     -sum_retained e log j(a_e).                 (1)

All readers of a surviving factor, including its radial normalizer, belong
to its support. The local Haar factor -log j(a_e) also counts as a factor: if
I includes one component of link e, its other frozen components are readers. Removing a terminal kernel removes its whole term in (1).
Normalization of the unrestricted posterior, or subsequent chart/conditional
normalization, changes only an a-independent constant.

For a set I of scalar coordinates (any subset of the three components of
any retained links), fix every coordinate outside I at b. The domain is the
Cartesian cube D_I=(-delta,delta)^I, with its conditional probability density
proportional to exp[-S(a_I,b;v)]. It suffices that every fixed hidden coordinate
read by a factor involving I obey |b_i|<=delta; unrelated coordinates do not
matter. Require also |v_c,r|<=delta for each terminal output read by such a
factor. The global chart is the case I=all coordinates. Blocks label the
terminal cells containing coordinate tails, and d is their nearest-neighbor
torus distance. Scalar splitting does not change these labels. Empty I has
only constants and covariance zero. No region connectivity is required.

The result is: there are delta>0, u_*, c>0, C_H<infinity and alpha>0,
depending only on L,kappa, such that for every specified J, internal forest,
m and admissible boundary field, and u>=u_*,

 D²_I S >= (u c/2) Id,    sup_i sum_j |(D²_I S)_ij| <= u C_H,   (2)

and, for f,g in C¹(closure D_I), with actual coordinate-block gradient
supports A,B,

 |Cov(f,g)| <= 4/(u c) exp[-alpha d(A,B)]
                    ||grad_I f||_L²(mu) ||grad_I g||_L²(mu).   (3)

Here support means the blocks in which the corresponding coordinate
derivative is not identically zero. Constants have zero covariance and
are handled separately. Nonlocal observables must use their actual supports,
not their nominal anchor positions. All gradients and norms in (3) are
for the exact restricted measure, with the frozen coordinates fixed.

This is uniform over the stated geometries and over u>=u_*, not over L or
kappa. The optional V_O extension is small-coordinate-chart uniformity only.
It asserts no compact estimate for arbitrary nonidentity terminal outputs.

## 2. Actual identity Hessian and its positive lower bound

At V=I, the compact input gives E_J,I(U)>=c sum_e(1-w(U_e))
with c=C(L,kappa)^(-1)>0, uniform in the entire listed domain and trees.
Along U_e=exp(i epsilon a_e dot sigma), dividing by epsilon²/2 and
letting epsilon tend to zero gives

 H_E,J:=D²E_J,I(0)>=c Id.                                  (4)

This supplies an actual lower bound, not a translation-invariant proxy.
For completeness the local differentiation identifies its content. For
one mean let p_gamma be the signed sum of input tangent vectors on path
gamma, with occurrence multiplicities, q=sum alpha_gamma p_gamma and
v_path=sum alpha_gamma |p_gamma|²-|q|²>=0. A unit path quaternion has
scalar part 1-epsilon²|p_gamma|²/2+O(epsilon³). Therefore

 r=1-epsilon² v_path/2+O(epsilon³),
 r-<exp(i epsilon b dot sigma),M>
       =epsilon² |b-q|²/2+O(epsilon³).

With Q_h the actual linear means and P_O terminal restriction this gives

 <a,H_E,J a>=||d0 a0||²+kappa||a1-Q0 a0||²
                                      +kappa||P_O Q1 a1||². (5)

If B(t)=Z'(t)/Z(t), symmetry of w under w -> -w and w<=1 imply
0<=B(t)<=1 for t>=0. Since r'(0)=0,
D²[h(t r)](0)[a,a]=t(1-B(t))v_path, while
D²[-log j](0)=(2/3)Id. In particular the exact finite-u germ is

 u^(-1)D²S(0;0)=H_E,J+kappa[1-B(kappa u)] diag(V0,V1,O)
                                      +(2/(3u))Id,         (6)

where each V is the positive sum of path-variance forms. Deleted kernels
contribute neither a variance form nor a mismatch. Equations (4)-(6)
retain the complete normalizer and Haar corrections; neither is replaced
by a large-u asymptotic expression.

## 3. Finite-template bounds through any fixed derivative order

Here is the needed uniformity argument rather than an invocation of
translation symmetry. Put ell=5L-4. Each actual path has at most ell edge
occurrences: each of the two root legs has at most 2(L-1) edges and the
bridge has L. Tree edges become constants. The number of paths in a mean
is finite (24L^4), and their positive weights sum to one. Wilson plaquettes
have four occurrences. Factors have a bounded set of terminal-cell offsets
and a bounded number of scalar readers depending only on L. For arbitrary
internal forests, fixing tree links only removes readers from these
expressions. If coordinates are obtained by the original gauge change,
its endpoint trees are in the endpoint blocks; this observation concerns
the pullback support, not an omission of those readers.

Choose a larger closed coordinate cube |a_i|,|v_i|<=delta_0 with
sqrt(3)ell delta_0<1/2 and sqrt(3)delta_0<pi. Telescoping each path gives
|P-I|<=ell sqrt(3)delta_0. Averaging gives |M-I|<1/2, so r>=1/2.
Choose delta_0 also inside a fixed strict injectivity margin. Quaternion
multiplication, exp(i a dot sigma) (with its removable singularity at
zero), sqrt(M dot M) on r>=1/2, and -log j are smooth on this larger
compact set. Every derivative of a fixed order has a finite supremum.

More precisely, list all local factor templates, including all internal
tree deletion patterns and terminal deletion patterns in a footprint.
Their number is finite for fixed L. A template contains at most n_*(L)
scalar slots, and a scalar coordinate occurs in at most D_*(L) anchored
factor templates, counted with multiplicity. Such a D_* exists because
there are finitely many anchor offsets for a reader. Periodic projection
can identify slots or anchors; count slots before identification and add
multiplicities afterwards. The total slot count and the number of anchors
reading a fixed coordinate remain bounded by these finite offset counts,
also at m=3. If desired include the finite slot-identification patterns in
the template list. This gives constants independent of torus size and of
which tree was chosen in each block. No identical-tree or translation-
invariance assumption about the resulting coefficient matrix is made.

For any fixed integer p, take the maximum of all absolute partial
derivatives of each energy template through order p on that closed cube,
and multiply by the finite slot/incidence counts. This is a finite
constant C_p(L,kappa). Equivalently the full energy tensors obey the
absolute anchored bounds

 sup_i sum_(i2,...,ip) |partial_i partial_i2 ... partial_ip E|
       <= C_p,                                             (7)

for p>=1, including mixed hidden/output derivatives when their slots are
included. The same argument works at every fixed p; there is no assertion
of one p-independent constant. Slots absent from a factor give zero.
For p=3 the mean value formula along (a,v)->s(a,v) and (7) give

 sup_i sum_j |(D²_a E_J,V(a)-H_E,J)_ij| <= C_3 delta.        (8)

The hidden Hessians are symmetric, so the column bound is the same, and
the operator norm is at most C_3 delta by the elementary row/column bound.
All readers must lie in the cube for this statement; knowing only the
variables being differentiated lie there is insufficient.

For radial normalizers there is a further u-uniform step. Under Haar,
X=1-w has density (2/pi)sqrt(x(2-x)) on [0,2], and
h(z)=log integral exp(-zx)(2/pi)sqrt(x(2-x))dx.
For z>=1 its denominator is at least a fixed positive constant times
z^(-3/2), integrating 0<=x<=1/z. Its nth moment numerator is at most
(2sqrt(2)/pi) integral_0^infinity exp(-zx)x^(n+1/2)dx
=const_n z^(-n-3/2). For z<=1 boundedness of X suffices. Thus
E_z X^n<=C_n(1+z)^(-n). The finite moment-partition formula for cumulants
then proves for every fixed q>=1

 |h^(q)(z)|<=C'_q(1+z)^(-q).                               (9)

Every term in the order-p chain rule for h(t r(a)) contains
 t^q h^(q)(t r) times q derivatives of r whose total order is p.
For r>=1/2, t^q/(1+t r)^q<=2^q. Bounded template derivatives of r and
the finite partition count prove that, for every fixed p>=1, derivatives
of each h(kappa u r) through order p are uniformly bounded in u>=1.
Its value itself need not be uniformly bounded and is not used. Applying
the same slot/incidence argument gives constants C_N,p for the sum of
all surviving normalizers. Haar gives constants C_A,p similarly.
In particular, through order four the full action's anchored derivative
bounds are u C_p+C_N,p+C_A,p. These are actual finite-template estimates,
not formal powers of t left uncontrolled.

Choose delta<=delta_0 with C_3 delta<=c/4 and then
u_*>=max(1,4(C_N,2+C_A,2)/c). Combining (4),(8),(9) with (1) proves
D² S>=u c/2 and its row bound <=u C_H. The range is at most a finite
R(L) in terminal-block distance: define R as the maximum distance between
any two hidden readers in one template. This safe finite range suffices;
no exact value two is required. Haar is diagonal.

For a regional principal-coordinate restriction, its Hessian is the
principal submatrix of the local Hessian just bounded. Extend the nearby
fixed reader coordinates to any full small-chart field, for example by
zero on unrelated coordinates. Derivatives involving I are unchanged,
so the full lower bound implies the principal lower bound. This also
proves the row and range bounds. Arbitrary holes and scalar-coordinate
subsets require no new coercivity theorem. Their exterior readers must
remain in the chart, precisely as specified in section 1.

## 4. Cube corners, mixed vector domains, and exact covariance identity

This section proves the analytic step for any finite-dimensional rectangular
cube D and any smooth S on its closure with D²S>=M Id, M>0. Use the
probability measure mu=Z_D^(-1)e^(-S)dx. Constants in intermediate existence
arguments may depend on dimension and density oscillation; the eventual
estimate depends only on M and the row/range bounds.

The scalar Neumann operator L is defined by the closed form
q_0(u,z)=integral grad u dot grad z dmu on H¹(D). Its kernel consists
of constants. The usual elementary unweighted cube Poincare inequality
(obtainable coordinate by coordinate from the one-dimensional fundamental
theorem of calculus) and positive upper/lower bounds for e^(-S) give some
positive scalar gap. Thus for centered f in L²(mu) there is a unique
mean-zero weak solution Lu=f. This establishes existence without assuming
the desired uniform gap.

We record enough regularity and density to justify differentiating that
solution at corners. Since grad S is bounded on this finite cube, the
weak weighted equation implies the unweighted weak Neumann equation

 -Delta u=f-grad S dot grad u=:F in L²(D).

Indeed use the weighted test e^S z for z in H¹(D) and cancel the weight.
The cosine tensor basis for the unweighted Neumann Laplacian diagonalizes
this equation. For nonconstant modes, coefficients satisfy
lambda_k u_k=F_k; hence sum lambda_k² |u_k|²<infinity. The cosine
partial sums converge in H²(D): pure and mixed second derivatives have
squared Fourier norms controlled by lambda_k². This simultaneously proves
H² regularity, the zero normal trace on each face, and density in that
Neumann H² domain of finite cosine polynomials. It uses the box geometry
directly and does not assert arbitrary smooth-domain regularity at corners.
In particular L u_n -> f in L²(mu) for such approximants u_n.

For vector fields set

 V={v in H¹(D;R^d): trace v_i=0 on the two faces normal to i}.

All other face conditions are natural Neumann conditions of the component
form; they are not imposed as extra H¹ trace conditions. Define

 q_1(v,w)=integral [sum_i grad v_i dot grad w_i+v^T(D²S)w]dmu.

This is a closed form on V with q_1(v,v)>=M||v||². Denote its
self-adjoint operator by T. It is a diagonal collection of scalar mixed
Dirichlet/Neumann diffusion operators plus multiplication by D²S.
Thus T is invertible with ||T^(-1)||<=1/M. This specifies the vector
domain; it is not the scalar Neumann operator tensored with identity.

Here is the intertwining argument including the boundary details. For a
finite cosine polynomial u_n, grad u_n lies in V. On a face normal to j,
partial_j partial_i u_n=0 if i differs from j, because the normal
first derivative of each cosine vanishes; when i=j, a test v_j in V
vanishes. Integration by parts componentwise therefore gives

 q_1(grad u_n,v)=integral grad(Lu_n) dot v dmu
               =integral (Lu_n) D_mu^* v dmu,                (10)
 D_mu^* v=-div v+grad S dot v.

The second equality has no boundary term since v dot n=0 on every face.
These equalities initially hold for smooth v with the stated traces.
They extend to all V: smooth mixed-trace fields are dense there, obtained
componentwise by odd reflection across the component's Dirichlet faces,
even reflection across its remaining faces, and symmetric convolution,
followed by restriction. These reflections yield H¹ extensions; the odd
ones use exactly the zero trace. For a rectangular cube there are no
extra compatibility conditions on codimension-two intersections for H¹
form density. Alternatively the corresponding sine/cosine tensor bases
give the same density. Faces account for the full integration-by-parts
boundary measure; corners introduce no additional measure term.

Let f be H¹(D), and take the preceding H² approximants to its mean-zero
Neumann solution u. Then grad u_n -> grad u in H¹, and Lu_n -> f in
L². Passing to the limit in (10) gives, for every v in V,

 q_1(grad u,v)=integral f D_mu^*v dmu
             =integral grad f dot v dmu.

In the last equality only f in H¹ and zero normal trace of v are needed.
By the defining weak equation for T,

 grad u=T^(-1)grad f,
 Cov_mu(f,g)=integral T^(-1)grad f dot grad g dmu             (11)

for every f,g in H¹, the latter equality also following directly by
testing Lu=f-E f against g. C¹ functions on the closed cube are included.
In particular Var(f)<=M^(-1)||grad f||², now with the uniform constant.
This argument addresses cube corners and the actual mixed vector domain
without a whole-space formula or an unsupported smooth-boundary limit.

## 5. Weighted spatial estimate and exact source scope

Apply section 4 with M=u c/2 to any I from section 1. Write
T=A+H where A is the diagonal collection of the just-defined mixed scalar
operators and H=D²_I S is bounded symmetric matrix multiplication.
Its matrix row and column sums are <=u C_H and H_ij=0 when the distance
between their block labels exceeds R. For nonempty A_f, the actual support
of grad f, let W be the fixed diagonal matrix

 W_ii=exp[alpha d(block(i),A_f)].

For each finite cube W and W^(-1) are bounded. They preserve each component
form and operator domain and commute with the diagonal operator A.
Consequently W T W^(-1)=T+K on the operator domain of A, where
K=W H W^(-1)-H is bounded multiplication. The distance-to-set function
is 1-Lipschitz on the torus graph, so

 sup_i sum_j |K_ij|, sup_j sum_i |K_ij|
                        <=u C_H (exp(alpha R)-1).

The elementary Schur bound gives the same operator norm in L²(mu;R^I).
Choose alpha>0 with C_H(exp(alpha R)-1)<=c/4 (if R=0, any fixed
alpha works). Thus ||K||<=M/2. The resolvent identity or its norm-convergent
Neumann series gives

 ||(T+K)^(-1)||=||W T^(-1)W^(-1)||<=2/M=4/(u c).             (12)

The equality is legitimate at each finite volume because the conjugation
preserves domains; it does not require W to have a volume-uniform norm.
Since W grad f=grad f and W^(-1) on grad g is at most
exp[-alpha d(A_f,A_g)], (11)-(12) prove (3). The bound uses only the
ambient torus metric and finite reader range, so arbitrary holes and
principal-coordinate selections cause no additional boundary assumption.
No translation invariance or connectedness of the selected region enters.

For one variation of a surviving terminal output c, the exact score is

 A_c=D_c log k(V_c|U1)=kappa u <D_c V_c,M1,c>, c in O;
 A_c=0, c in J.                                            (13)

The radial normalizer is independent of its output, which is the reason
its derivative in (13) vanishes; it remains in the measure in (1).
On a fixed chart and fixed frozen boundary, differentiation of the
chart-conditioned expectation of a terminal-parameter-independent quotient function gives
D_c E f=Cov(f,A_c). Its estimate is exactly (3), with the actual readers
of A_c as its support, and ||grad A_c||<=u C(L,kappa) for unit-speed
output variation by the same templates. If all its readers are frozen,
the score is constant on this conditional cube and that covariance is zero.
There is no deleted score or omitted conditional-normalization derivative.

For general original sources F,G that also depend on the independent
forest orbit variables omega, let nu be their exact orbit-Haar measure,
f(a)=E_nu F(a,omega), g(a)=E_nu G(a,omega). On the gauge-invariant
chart event (and the quotient regional restriction), the exact identity is

 Cov_(mu x nu)(F,G)=Cov_mu(f,g)
                  +E_mu[Cov_nu(F(a,omega),G(a,omega))].     (14)

When f,g are C¹, (3) applies only to the first term, with their actual
quotient-coordinate supports, including all readers from gauge pullback.
The second term is retained separately; no smallness or spatial decay is
asserted for it. If either original source is invariant under the integrated root-fixed orbit,
it vanishes; global conjugation invariance alone is insufficient.
If a proposed region/event conditions on orbit-dependent original variables,
the product disintegration assumed in (14) must be re-established; that
is outside this fixed quotient-chart statement.

## 6. Scope and checkpoint

Equations (2)-(3) hold globally on the fixed chart and on every stated
regional principal-coordinate cube, with complete small-chart exterior
readers. Equations (4)-(9) supply the actual deleted-law nonlinear Hessian
and finite-order constants; (10)-(12) supply the cube-domain covariance
argument; (13)-(14) retain deleted-score and orbit terms correctly.
The compact coercivity input is an explicit inherited premise whose proof
and check are separate from this note; ancestral inputs were not rechecked
here. This author's argument awaits the parent's full read and fresh decisive
check. No connected-four-cumulant decay, rough-collar control, probability
of the chart, full compact covariance, compact nonidentity coercivity,
physical mass gap, or retained-grade conclusion is asserted. No failed
numerical route or external theorem is hidden in this proof. Only this
assigned note was edited; no Git mutation, prompt edit or external action
was performed.
