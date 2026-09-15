# Carrier-preserving one-step convexification of a closed integer charge gas

Personal proof draft,2026-09-14. Scope is the explicitly supplied charge gas
below, not yet the full finite-clock gauge measure. The purpose is a
checked component for the fixed-law phase route. No independent review,
formal retained status, native law, or axiom update.

## 1. Geometry and the supplied gas

Fix d>=2 and1<=p<d. Let B be all positively oriented p-cells based in a
finite rectangular set of vertices of Z^d. A charge q is an integer p-form
supported in B, extended by zero to the whole lattice, satisfying dq=0
there. This is a compact-support closure condition, including boundary
cells. Define adjacency of p-cells by sharing a(p+1)cell, and include self
adjacency when discussing incompatibility. Its degree is bounded by

 Delta=2(d-p)(2p+1).

Every closure equation involves mutually adjacent cells. Therefore every
connected support component of q is separately closed. The charge has a
unique decomposition into nonzero connected closed charges, with pairwise
nonadjacent supports. This is a LOCAL closure property, not merely a
global scalar-neutrality constraint.

Let H be the componentwise Dirichlet lattice Laplacian on B, equivalently
its quadratic form is the full-lattice energy of a zero-extended p-form:

 <h,Hh>=||dh||_2^2+||d*h||_2^2=sum_{x,I,mu}|h_I(x+mu)-h_I(x)|^2.

It is positive definite in the finite box and ||H||<=4d. Let G=H^-1,
c=1/(8d), and beta>0. Thus G>=2cI. The explicitly supplied gas is

 Z_beta(sigma)=sum_{q integer,supp q subset B,dq=0}
   exp[-2pi^2 beta <q,Gq>] exp[2pi i<q,sigma>].         (1)

This finite-volume kernel and the whole-lattice compact-support closure
are part of the definition. A gauge-model application must derive its own
boundary/source representation and cannot replace its harmonic sectors or
boundary Green operator by(1) without proof.

## 2. Exact Gaussian split and hard-core representation

Let phi have centered Gaussian covariance beta(G-cI). Independently let
zeta have covariance beta cI. Then phi+zeta has covariance beta G. First truncate the charge sum,
integrate zeta in that finite sum, and only then remove the cutoff. The
resulting summable bound exp[-t||q||^2] justifies dominated convergence.
No interchange with an undamped infinite Fourier series is used. This gives

 Z_beta(sigma)=E_phi Theta_t(phi+sigma),
 Theta_t(u)=sum_{q closed}exp[-t||q||^2]exp[2pi i<q,u>],
 t=2pi^2 beta c=pi^2 beta/(4d).                         (2)

A polymer gamma is a nonzero connected closed integer charge. Write
X_gamma=supp gamma and s_gamma=||gamma||_1. Two polymers are incompatible
if their supports meet or are adjacent. By section1 the exact polymer
activity is

 z_gamma(u)=exp[-t||gamma||_2^2]exp[2pi i<gamma,u>],
 Theta_t(u)=sum_{compatible finite sets of polymers}prod z_gamma(u).

There are countably many charges per support. All sums are absolutely
convergent in finite volume. The local integer norm inequality
||gamma||_2^2>=s_gamma>=|X_gamma| is essential below.

## 3. A root bound that retains total cluster mass

Let

 u_t=2 exp[-t/2]/(1-exp[-3t/2]),
 R_t=e u_t/(1-Delta^2 e u_t).                           (3)

Assume Delta^2 e u_t<1 and(Delta+1)R_t<=1. The number of connected
m-cell sets containing a fixed cell is at most Delta^(2(m-1)): choose a
canonical spanning tree and its length2(m-1) depth-first walk. The visited
set determines the original set, so counting walks is an upper bound.
For a fixed support of size m, after reserving half the Gaussian exponent,

 sum_{gamma:supp gamma=X}exp[-(t/2)||gamma||_2^2]
 <=(2 sum_{n>=1}exp[-(t/2)n^2])^m<=u_t^m.

Dropping the closure restriction only enlarges the sum. Hence

 sup_x sum_{gamma:x in X_gamma}exp[-(t/2)||gamma||^2]e^{|X_gamma|}
 <=R_t.

For a root polymer gamma_0, at most(Delta+1)|X_gamma_0| cells can touch
its support, and therefore

 sum_{gamma incompatible gamma_0}a_gamma e^{|X_gamma|}
 <=|X_gamma_0|, a_gamma=exp[-(t/2)||gamma||^2].          (4)

For completeness, the hard-core connected coefficient is

 U(gamma_1,...,gamma_n)=sum_{connected spanning A subset incompatibility graph}
                       (-1)^{|A|}.

It satisfies the tree bound |U|<=number of spanning trees of that graph.
One proof orders graph edges, associates a spanning tree by Kruskal's
algorithm, and partitions connected subgraphs into intervals[T,T_max].
The alternating sum in each interval has magnitude at most1.

A rooted-tree generating sum obeys the positive majorant iteration
T_gamma^(0)=a_gamma,
T_gamma^(k+1)=a_gamma exp[sum_{eta incompatible gamma}T_eta^(k)].
Equation(4) proves inductively T_gamma^(k)<=a_gamma e^{|X_gamma|}.
Taking its increasing limit bounds the absolute connected cluster expansion
with a marked root. The factorials are those of labeled exponential trees;
a cluster with at least one polymer containing x can be bounded by choosing
one such root and dropping overcounting restrictions. Thus the absolute
logarithm-cluster sum whose carrier contains x is at most R_t at the
half-strength activities a_gamma.

Write a full-strength cluster weight as

 w(C;u)=U(gamma_1,...,gamma_n)/n! *prod_i z_gamma_i(u),
 S(C)=sum_i s_gamma_i, U(C)=union_i X_gamma_i.

Here U(C) is connected; the Fourier charge Q(C)=sum_i gamma_i may have
DISCONNECTED support or be zero. The full-strength coefficient has the
additional factor exp[-(t/2)sum_i||gamma_i||^2]<=exp[-t S(C)/2]. Hence,
for every integer S>=1,

 sum_{C: x in U(C), S(C)=S}|w(C;u)| <=R_t exp[-tS/2].  (5)

This estimate is uniform over real u and finite boxes. It retains total
integer mass S, which does not shrink when opposite charges cancel.

The convergent cluster expression

 V_t(u)=sum_C w(C;u), Theta_t(u)=exp[V_t(u)]             (6)

is real, since charge reversal pairs complex conjugates. Equality follows
first as a formal power series and then by uniform absolute convergence
under activity scaling lambda in[0,1]; analytic continuation fromlambda=0
where Theta=1 supplies the same logarithm. In particular Theta_t(u)>0
for all real u under(3)-(4). Positivity is proved by convergence and real
pairing, not assumed from an oscillatory integrand. There is also a direct
check valid for every t>0: the compact closed integer charges form a
lattice K in their real span. Poisson summation gives

 Theta_t(u)=(pi/t)^(rank K/2)/covol(K)
   *sum_{w in K*}exp[-pi^2||w-P_span(K)u||^2/t]>0.

This independent positivity proof does not imply convexity of the effective
action; that still needs the derivative estimate.

## 4. Integer filling with the carrier still present

A compactly supported closed integer p-form gamma, p<d, admits an integer
(p-1)form n_gamma with dn_gamma=gamma, supported in its bounding cube with
a fixed one-cell enlargement, and

 ||n_gamma||_infty<=d ||gamma||_1.                       (7)

An explicit construction uses the dual cubical lattice. The charge is a
finite(d-p)cycle, of positive degree because p<d. Contract the product
of coordinate intervals to a corner one coordinate at a time. The standard
interval prism H_j satisfies boundary H_j+H_j boundary=I-P_j. The sum
H_1+P_1 H_2+...+P_1...P_(d-1)H_d contracts the product. The projection to
a point annihilates positive-degree cycles. Each input cell contributes at
most one prism in each coordinate direction to any given output cell;
integer coefficients stay integer, giving(7). All prisms stay within the
coordinate box. Dualizing back gives the asserted cochain filling and the
fixed enlargement. This also proves why top-degree charges require an
extra total-charge condition and are excluded here.

For a connected cluster carrier U(C) with S=S(C), its diameter in base-cell
coordinates is at most S-1. Put n_C=sum_i n_gamma_i. Its support lies in
the carrier's enlarged bounding cube D(C), whose side may be bounded by6S.
Use the deliberately loose constants

 C0=2^d d^2 6^d, C1=2^d 11^d.

Then

 dn_C=Q(C), ||n_C||_2^2<=C0 S^(d+2),
 |<Q(C),h>|^2=|<n_C,d*h>|^2
 <=C0 S^(d+2) sum_{y in D(C)}|(d*h)(y)|^2.             (8)

Any y in this enlarged box lies within5S in base coordinates of any
chosen x in U(C). There are at most C1 S^d possible p-cell anchors x
at that distance. We deliberately count all orientations rather than
optimizing geometric constants.

## 5. Uniform Hessian and strictly convex effective measure

Twice differentiating a cluster phase gives
D^2 w(C;u)[h,h]=-(2pi)^2<Q(C),h>^2 w(C;u).
The mass reserve(5) justifies termwise differentiation. Combining(5),(8),
and the anchor count yields

 |D^2 V_t(u)[h,h]| <=epsilon_t ||d*h||_2^2,
 epsilon_t=4pi^2 C0 C1 R_t sum_{S>=1}S^(2d+2)e^(-tS/2). (9)

For h supported in B, all derivatives on the right use zero extension.
The bound is uniform in u and in the box, including clusters whose net
charge has cancelled support. The coefficient tends to zero exponentially
as t increases, up to fixed dimension-dependent constants. For an explicit
closed bound, put r=exp[-t/2] and m=2d+2. The Eulerian generating polynomial
has nonnegative coefficients summing to m!, so

 sum_{S>=1}S^m r^S <=m! r/(1-r)^(m+1).                (9a)

This follows inductively by applying r d/dr to the geometric series. It
avoids treating a truncated numerical tail sum as a proof of(9).

By(2),(6), the source-free expectation uses the positive density

 dmu_beta(phi) proportional exp[-H_eff(phi)]dphi,
 H_eff(phi)= (1/(2beta))<phi,(G-cI)^-1 phi>-V_t(phi).

The Gaussian precision has the convergent expansion

 (G-cI)^-1=H(I-cH)^-1=sum_{k>=0}c^k H^(k+1), c||H||<=1/2.

It dominates H, and its correction has exponentially decaying spatial
range by the finite range of H and the norm-geometric series. Therefore

 D^2 H_eff(phi)[h,h]>=(beta^-1-epsilon_t)<h,Hh>.         (10)

If beta epsilon_t<=1/2, the effective field is uniformly convex relative
to the Dirichlet gradient energy with constant1/(2beta), independently
of volume. The word uniform refers to this gradient-energy inequality,
not a volume-uniform ordinary Euclidean spectral gap of H.

The usual finite-dimensional integration-by-parts covariance machinery can
then be applied to this specified positive effective measure after its
hypotheses are checked. No central-limit or homogenization conclusion is
asserted from(10) alone. The source term is exactly

 Z_beta(sigma)/Z_beta(0)=E_mu_beta exp[V_t(phi+sigma)-V_t(phi)]. (11)

It is a generally nonlinear observable of the convex field. Replacing it
by a linear Gaussian observable without controlling the difference would
lose the main physical task.


## 6. Source lower bound and a charge-covariance consequence

Let F(a)=log Z_beta(a sigma), with sigma real. By(2),(6), the a-dependent
measure on phi is positive. Differentiating its finite-dimensional integral,

 F''(a)=E_a D^2 V_t(phi+a sigma)[sigma,sigma]
          +Var_a(D V_t(phi+a sigma)[sigma])
 >=-epsilon_t ||d*sigma||^2.

Evenness gives F'(0)=0. Integrating twice and using the original
positive-weight characteristic sum for the upper bound gives

 exp[-epsilon_t ||d*sigma||^2/2]
 <=Z_beta(sigma)/Z_beta(0)<=1.                         (12)

The lower bound is real and strictly positive. It uses the Hessian bound
and positivity of the effective source ensemble; it does not require
beta epsilon_t<=1/2. The convexity condition is useful for further
correlation analysis, and is logically stronger than what(12) needs.
At zero source, F''(0)=-4pi^2 Var(<q,sigma>), so

 4pi^2 Var(<q,sigma>)<=epsilon_t ||d*sigma||^2.         (13)

This is a covariance upper bound for the supplied charge gas. It does not
determine all higher cumulants or identify the original gauge score.
A positive mixture of source ensembles has the extra nonnegative variance
term shown explicitly; dropping it would reverse the reasoning.

## 7. Exact cancellation witness

In Z^3 let n_1 be the sum of positively oriented x-edges at positions
(0,y,0), y=0,...,R, along a line transverse to the edge orientation. Let
n_2 be minus the same edges for y=1,...,R-1.
Set q_i=dn_i. The only nonzero components of d n for an x-edge string are

 q_01(x,y,z)=n_0(x,y,z)-n_0(x,y+1,z),
 q_02(x,y,z)=n_0(x,y,z)-n_0(x,y,z+1).

Both q_i are closed, have connected support and overlap. Their sum is
the sum of the two isolated endpoint-edge curls at y=0,R. For R>=4 the
net support is disconnected, while the union of original supports remains
connected. Their mixed labeled order-two logarithm coefficient is
- exp[-t(||q_1||^2+||q_2||^2)] exp[2pi i<q_1+q_2,u>].
It is nonzero as a marked two-polymer coefficient; no claim about the
absence of cancellations after full unmarked resummation is needed. This
directly falsifies the generic step 'connected cluster
implies connected net Fourier-charge support'. It does not imply any
physical phase is absent or invalidate a theorem using a marked carrier.

An analogous gauge-degree example in Z^4 sets n_1 to a line of01plaquettes
based at(0,0,z,0), z=0,...,R, transverse to both plaquette directions,
and n_2 to its negative interior. Their exterior
derivatives are closed3forms; cancellation again leaves only the two
endpoint plaquette derivatives. The exact sparse-cochain check must retain
all orientations, closure signs and support components.

## 8. Application boundary and next decisive work

The derivation establishes a positive convex representation for(1) at
sufficiently large beta, with explicit sufficient inequalities(3),(9),(10).
It is a reusable closed-charge lemma. It is not yet an exact representation
of the finite-clock Villain field or the supplied N=3 penalty Hamiltonian.
The actual finite-clock proof must keep electric and magnetic defects and
their coupling; topology and sources must match the original law.

Dario-Wu2023section3 and Bauerschmidt2016sections4.3,5.5 provide the standard
Gaussian-split/cluster/convex-field strategy. The carrier-retaining version
here avoids inferring support connectivity after charge cancellation.
Their principal theorems are not judged by this elementary bookkeeping
control. Novelty of the cluster machinery is not claimed. The fixed-law
score's nonlocal covariance and higher connected cumulants still require
a matched effective representation and a homogenization argument.
