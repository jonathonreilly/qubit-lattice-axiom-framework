# A positive local covariance core with complete original readers

This author unit constructs a covariance interpolation for the **actual
source-free lift Hessian** of the normalized one-step Wilson / paired-S4-prime
model. Its large local pieces are positive for real coarse data; its remaining
complete-reader atoms have a genuinely small absolute row/column sum. The
interpolation is uniformly accretive on a specified complex coarse tube and
factorizes at reader-disconnected endpoints, including diagonal atoms that
read remote data. Independent review is pending.

This repairs one proposed covariance obstruction in
[the frozen chart-regulator unit](PROBABILITY_SENSITIVE_RETURN_ASTRA.md).
It does not sum differentiated interacting integrals, normalize hard events,
prove the returned denominator theorem, or establish four-dimensional
continuum existence or a positive physical continuum mass gap. Both physical
targets remain **OPEN**. The positive precision here is an auxiliary Gaussian
reference, not the covariance or a mass gap of the interacting theory.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual lift-Hessian covariance with a positive complete-reader local core, small absolute residual atoms, and a uniform complex interpolation domain."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Actual precision, modes, and local analytic domain

Fix N>=2, D=N^2-1, odd L>=3, T>=2, u>=1 and
`0<kappa_-<=kappa<=kappa_+`, with t=kappa u real and fixed under source
variation. There are m0=3L^4+1 free links per coarse block and
`n0=Dm0` scalar coordinates per block. Write Lambda=(Z/TZ)^4. Each scalar
coordinate i=(free link,colour) has an owner X_i in Lambda. All roots,
harmonic directions, crossings and colours remain. The block-root-pinned
tree quotient has Jacobian one and integrated nonroot gauge volume one.

The lift U0(V) is I on internal links and V_c on the crossing face. Every
actual paired transporter equals V_c there. The T=2 coercivity proof uses
the lifted two-block brick, excluding its extra far periodic seam. In the
fixed HS-orthonormal scalar basis, put U_e(a)=exp(a_e)U0_e(V) and

    F_0(a;V)=sigma^2[-log w_0(U(a),V)-sum_e log j_N(a_e)],
    sigma^2=N/u,                  K(V)=F_0''(0;V).             (PC1)

The exact w_0 contains the Wilson weight and every normalized compact kernel.
The constant h_N in `dHaar(exp a)=h_N j_N(a)da` is outside F_0. The normalizer
and j_N each occur once. K is at the lift, not at the shifted critical point.
Its force is generally nonzero.

Here is the actual model input, recalled from
[CB, sections 1--4](COVARIANT_SOFT_BACKGROUND_ASTRA.md), rather than replaced
by a convexity assumption. The flat lifted-brick recovery of a free edge
from curvature and averaged paths yields

    a_gap=1/max(C_F,C_Q/kappa_-),
    C_F=4L^3(L+4)(60L^2)^2, C_Q=2L^3,
    K=H_V+E_V+kappa(1-c_N(kappa u))B_V+N^2/(6u)I,
    H_V>=a_gap I, B_V>=0,
    max(row_HS,col_HS)||E_V||<=24 delta_V.                  (PC2)

The finite-t factor c_N is the actual compact tilted-Haar mean, with
0<c_N<1. The spread B_V and Haar Hessian are not deleted. A Wilson plaquette
second variation has four signed insertions and their ordered pairs;
replacing its background plaquette by I changes each colour-block entry by
at most delta_V. Four entries and six incident plaquettes give 24. Thus set

    delta0=min(1/24,a_gap/48), gamma=a_gap/2,
    B=25+24 kappa_+(5L)^2+N^2/6, b=D B,
    c0=1/(2B).                                             (PC3)

For every real reference Vbar with delta_Vbar<=delta0,
`gamma I<=K(Vbar)<=B I`. K has range at most two in coarse sup distance;
its scalar absolute row/column norm is <=b. Every entry reads a radius-three
coarse stencil. We enlarge each reader by one cell below to include both
endpoints of every original coarse-link datum. Principal compressions of
this matrix inherit the spectral interval. They are not Hessians of a
nonlinear collar-conditioned interacting law.

Use the same local complex continuations as CB9 and IC2: negative edges
use inverses, the two means are `average T_tau` and `average T_tau^-1`,
and no conjugated complex variable is differentiated. Fix a common scalar
radius a0>0 so twice its polydisc is inside CB9's joint fine/coarse analytic
domain, and let H0 bound each vacuum-subtracted local vertex there. These
are uniform in real u>=1 and admitted real Vbar. The kernel assertion is
for its centered logarithm at fixed real t, not its unremoved vacuum.
There are at most q=(8L^4+8)D scalar slots per local vertex, at most fifteen
vertices per fine coordinate, and a radius-three reader stencil.

For `V_c=exp(v_c)Vbar_c`, complex v_c in sl(N,C), the Cauchy bound
`6H0/a0^3` on a third derivative and at most 15q^2 incident ordered slots
bound each scalar row/column of a change of K. The conservative constant

    J0=1000 q^3(H0+1)/a0^3,
    max(row,col)||K(exp(v)Vbar)-K(Vbar)||<=J0 max_c||v_c||HS  (PC4)

therefore suffices after restricting `max||v_c||HS<a0/4`. This repeats the
joint local argument in [IC6](INTERACTING_SELECTED_CORE_ASTRA.md); no
all-order integrated IC theorem is needed. Only fine derivatives enter K,
so subtracting a local vacuum for this estimate does not alter K or PC1.

Choose a preliminary radius

    rho_pre<min(a0/4,1/100,gamma/(4J0)),
    b_c=b+gamma/4, r0=8,
    m=(1/r0)log(1+gamma/(4b_c)).                            (PC5)

The actual K(V) and every principal compression on this tube are complex
symmetric with Hermitian part >=3gamma/4. The number r0=8 safely converts
range two in four-dimensional sup distance to coarse l1 distance. No
smallness of the individual real Vbar_c or its holonomies is assumed.
The final radius below is smaller and remains independent of T and u.

## 2. Principal inverses with scalar, entrywise-uniform bounds

For any set A of coarse cells, K_A is the principal matrix on **all** owned
free-link and colour coordinates there; G_A denotes its inverse, extended
by zero. Fix a column j. Conjugate K_A by the positive diagonal weight
`exp(m d_1(X_i,X_j))`, where d_1 is the periodic coarse l1 metric. Each
nonzero entry changes by a factor of modulus at most `exp(m r0)-1`.
Both absolute row and column changes are <=gamma/4 by PC5. The operator
norm is bounded by the geometric mean of these two sums: this follows
from weighted Cauchy--Schwarz applied to each row, then summing columns.
An accretive matrix with Hermitian part >=a has inverse norm <=1/a,
since `a||x||^2<=Re<x,Kx><=||x||||Kx||`. Hence the conjugated inverse
has norm <=2/gamma. Undoing the weight proves, uniformly on the tube,

    sup |G_A(i,j)| <=(2/gamma) exp[-m d_1(X_i,X_j)],
    max_i sum_j exp[(m/2)d_1(X_i,X_j)] sup |G_A(i,j)| <=g,
    max_j sum_i exp[(m/2)d_1(X_i,X_j)] sup |G_A(i,j)| <=g,
    g=(2n0/gamma)coth(m/4)^4.                              (PC6)

The suprema include all admitted centers and the stated complex changes.
For the sum, representatives of the torus distances form a subset of Z^4,
and `sum_(z in Z) exp[-(m/2)|z|]=coth(m/4)`. Every cell has n0 scalar
indices. Periodic path multiplicities in K have already been added in its
actual entries; no colour, winding or root coordinate is removed. The
bounds also hold for the whole-torus compression.

The proof later needs sums of **suprema of entries**, not only a supremum
of row sums. Make that distinction explicit. Set

    vK=n0*5^4, b_abs=vK*(B+gamma/4), J_abs=vK*J0.           (PC7)

At most vK scalar columns can meet a row of K. A real entry is bounded
by B, and its complex change is <=J0 rho_pre<=gamma/4. Therefore
`max(row,col) sum sup|K_ij|<=b_abs`. Likewise the entrywise envelope of
`K(V)-K(Vbar)` has row/column sums <=J_abs max||v_c||HS. These finite
stencil factors prevent the invalid exchange of sum and supremum.

## 3. A fixed geometric cover on every torus

Choose an integer R>=4; its quantitative choice is in section 5 and depends
only on N,L,kappa bounds and the local analytic constants. It never depends
on u,T or V. If T<16R, use one patch A=Lambda and chi_A=1. Its reader is
the whole torus, with cardinality <(16R)^4. This bounded small-volume cost
is retained even though the cutoff is then constant.

For T>=16R, partition each coordinate circle into intervals of integer
length between R and 2R, and take their product boxes Q. This is possible
using floor(T/R) intervals and distributing the remainder. Regard an
interval as the union of its unit cells in the continuous circle. Choose
once a smooth function psi with values in [0,1], equal to one on [0,1/4],
zero on [1,infinity), and |psi'|<=4. Define on the continuous torus and
then restrict to lattice owners

    f_Q(X)=product_(nu=1)^4 psi(dist_circle(X_nu,I_Q,nu)/R),
    h(X)=(sum_Q f_Q(X)^2)^(1/2), chi_Q(X)=f_Q(X)/h(X),
    A_Q=N_(2R)(Q), S_Q=N_(2R+4)(Q).                        (PC8)

The constant plateaux make these periodic cutoffs smooth even at the
interval endpoints and the circular distance cut locus. At every lattice
owner some f_Q=1, so h>=1 and `sum_Q chi_Q^2=1`. All D colours at an owner
use the same scalar chi. The support of chi_Q is contained in N_(R+1)(Q),
strictly before the boundary of A_Q. Since R>=4 and K has sup range two,
any matrix neighbor of that support is still in A_Q.

The following deliberately loose geometry constants cover both cases:

    J=16^4, s_R=(16R)^4, n_R=n0 s_R,
    C_chi=16(1+sqrt(2J)).                                  (PC9)

Each S_Q is connected, contains all endpoints and original readers of K_A,
and has at most s_R cells. A fixed cell belongs to at most J such labels.
For the large torus, the side of S_Q is at most 6R+8<=8R. Intervals meeting
a one-dimensional neighborhood of radius 2R+4 number at most sixteen,
since their lengths are at least R; take products. Small-torus counts are
one. No data-dependent cover or favorable-boundary selection occurs.

The function f_Q is 16/R-Lipschitz in sup distance. For a pair X,Y,
at most 2J of the differences f_Q(X)-f_Q(Y) can be nonzero. The reverse
triangle inequality in Euclidean space gives
`|h(X)-h(Y)|<=16 sqrt(2J) d_infinity(X,Y)/R`. Since h>=1 and f_Q<=1,

    |chi_Q(X)-chi_Q(Y)|<=C_chi d_infinity(X,Y)/R.           (PC10)

This bound includes a zero cutoff just outside its support. It is the
boundary-collar control needed below, not an omission of patch boundaries.

## 4. Positive local core and the exact residual identity

Write chi_A for the diagonal multiplier from PC8 and define

    P_A=chi_A G_A chi_A, P=sum_A P_A,
    D_A=chi_A(G_A-c0 I_A)chi_A,
    P=c0 I+sum_A D_A.                                     (PC11)

For real admitted V, `G_A>=B^-1 I_A=2c0 I_A`; therefore every D_A is
positive semidefinite, in fact D_A>=c0 chi_A^2. Each P_A,D_A is a single
local matrix component with label S_A. Splitting D_A into individual
matrix entries and independently weakening them is **not** allowed by
this positivity proof. Its entire full-colour matrix is weakened together.

All products in the next identity are global zero-extended matrices.
Because chi_A is supported inside A,
`chi_A K G_A chi_A=chi_A^2`. Consequently

    K P_A=chi_A^2+[K,chi_A]G_A chi_A,
    R_A=-[K,chi_A]G_A chi_A,
    Rcal=sum_A R_A=I-KP.                                  (PC12)

Here `[K,chi_A]_ik=K_ik(chi_A(k)-chi_A(i))`. The sign and order follow by
expanding K chi_A; they are not chosen from a formal Neumann analogy.
The identity includes all zero-extension boundary entries. With the
PC8 collar, any nonzero commutator row or column connected to G_A chi_A
lies in A, so both field endpoints of R_A lie in A. Its coefficients read
only S_A. In the whole-torus case the commutator is exactly zero.

For labelled matrix families define, with a supremum on their actual
projected coarse-data domains,

    M_beta(F)=max{sup_i sum_(j,a) exp(beta|S_a|) sup|F_a(i,j)|,
                 sup_j sum_(i,a) exp(beta|S_a|) sup|F_a(i,j)|},
    B_beta(F)=sup_X sum_(a:S_a contains X) sum_(i,j)
                              exp(beta|S_a|) sup|F_a(i,j)|. (PC13)

Repeated labels and repeated paths are separate atoms, not erased by
cancellation. Both endpoints belong to their label. The norms distinguish
the genuinely small row/column bound M from the generally large marked
incidence B. Set beta=1/s_R, w=exp(beta s_R)=exp(1), and

    p=w J g, C_R=2J C_chi r0 b_abs g,
    r=w C_R/R, d_core=p+w J c0.                            (PC14)

PC6 and the at most J cutoffs at a row or column give `M_beta(P)<=p`.
For a residual row, take absolute values in

    R_A(i,j)=-sum_k K_ik(chi_A(k)-chi_A(i))G_A(k,j)chi_A(j).

For each (i,k), at most 2J cutoffs have nonzero difference; each difference
is <=C_chi r0/R. Sum j by PC6 and k by b_abs. This gives the displayed r.
For a residual column j, at most J factors chi_A(j) are nonzero. For
each A first sum i in K's column, paying C_chi r0 b_abs/R, and then sum k
in G_A's column, paying g. This is <=r/2 before the common weight. Thus

    M_beta(P)<=p, M_beta(Rcal)<=r, M_beta(D)<=d_core,
    B_beta(P)<=n_R p, B_beta(Rcal)<=n_R r,
    B_beta(D)<=n_R d_core.                                (PC15)

For the marked bounds, a fixed mark belongs to <=J labels and each patch
has <=n_R scalar rows. Use the **per-patch** row bound, then sum patches;
this avoids an extra extensive sum. All constants pay the scalar colour
density n0. An operator norm estimate alone would not prove PC15.

## 5. Connected residual atoms and their small absolute sum

The constants p and C_R in PC14 do not depend on R: w=exp(1), and J,g,
b_abs,C_chi,r0 were fixed first. Choose once an integer R>=4 with

    r=w C_R/R <=min(1/4,c0/(32p)).                         (PC16)

Then the exact PC12 identity gives the **ordered** expansion

    K^-1=P(I-Rcal)^-1=P+sum_(n>=1) P Rcal^n.              (PC17)

For each sequence omega=(A_0,...,A_n), n>=1, retain the matrix product
`A_omega=P_(A_0)R_(A_1)...R_(A_n)` with label
`S_omega=union_(j=0)^n S_(A_j)`. Discard only products identically zero.
A nonzero product has a shared scalar summation index between each pair
of successive factors. Thus consecutive labels meet, their union is
connected, and it includes every original datum read by the product.

For these families the absolute sums directly give

    M_beta(FH)<=M_beta(F)M_beta(H),
    B_beta(FH)<=B_beta(F)M_beta(H)+M_beta(F)B_beta(H).        (PC18)

Indeed `|S union S'|<=|S|+|S'|`. For a mark in S, sum the right factor by
its row bound; for a mark in S', sum the left factor by its column bound.
This proves the marked inequality without a translation-invariance or
independence assumption. Suprema of products are bounded by products of
suprema on the projected original-data domains.

Symmetrize every product separately,

    E_omega=(A_omega+A_omega^T)/2, E=sum_omega E_omega.

Since K and P are symmetric, the unsymmetrized sum in PC17 is symmetric,
so E=K^-1-P exactly. A transpose swaps the two endpoint bounds and leaves
the same full reader label. Consequently

    M_beta(E)<=e_res:=p r/(1-r)<=c0/16,
    B_beta(E)<=n_R p{r/(1-r)+r/(1-r)^2}.                   (PC19)

Convergence is absolute and locally uniform on the complex tube. The
right-hand marked budget may be large; no smallness of it is needed for
positivity. There is no dimension-dependent conversion from M to operator
norm: the two endpoint sums give it directly. The exact decomposition is

    K(V)^-1=c0 I+sum_A D_A(V_(S_A))
                         +sum_omega E_omega(V_(S_omega)).  (PC20)

This construction has original-block rate `beta=(16R)^-4`. It proves no
arbitrary preassigned original-block rate. Increasing R while silently
holding such a rate fixed would replace w by exp(beta s_R), defeating the
stated smallness argument. A consumer may use any smaller positive rate.

## 6. Complex continuation and independently weakened components

A positive real D_A need not remain positive at complex V. Control the
change instead. On the preliminary tube the exact resolvent identity is

    G_A(V)-G_A(Vbar)=-G_A(V)[K_A(V)-K_A(Vbar)]G_A(Vbar).

PC6, PC7, and the at most J cutoff factors at a fixed endpoint imply the
unweighted **sum of absolute matrix entries over all local components**
bound

    M_0({D_A(V)-D_A(Vbar)})<=J g^2 J_abs max||v_c||HS.     (PC21)

Choose the final radius

    0<rho_PC<min(rho_pre,c0/(8J g^2 J_abs)).               (PC22)

It can be decreased further to lie inside any previously chosen positive
CB/IC coarse tube. Every atom is holomorphic on the projection of this
tube to its complete reader label: complete projected data with Vbar
outside that label and use the same accretive principal inverse. The
formula is a function of actual V, not of a secretly supplied completion
or the chosen reference center. Formulas agree on overlapping tubes.
This is a tube about each admitted real configuration, not a global
logarithm of all coarse links or an arbitrary curvature-free domain.

For independent real numbers 0<=theta_A<=1 and independent complex numbers
|zeta_omega|<=1, define

    C(theta,zeta;V)=c0 I+sum_A theta_A D_A(V)
                              +sum_omega zeta_omega E_omega(V). (PC23)

The positive core at Vbar is >=c0 I. PC21 costs <c0/8 in operator norm;
PC19 costs <=c0/16, uniformly for every separate residual coefficient.
Hence, on the common tube,

    Re C >=(13/16)c0 I >=(3/4)c0 I=:a_C I,
    ||C||op <=U:=c0+d_core+e_res.                          (PC24)

Here Re C means its Hermitian part. For real V and real residual
coefficients C is real positive definite; complex coefficients give an
accretive complex symmetric matrix. Allowing arbitrary complex coefficients
on the **large** D_A components is outside this theorem. Nonnegative
forest monomials do satisfy the required real interval.

PC24 gives an explicit Gaussian precision lower bound even on the complex
domain:

    Re C^-1=C^{-*}(Re C)C^-1 >=(a_C/U^2)I.                (PC25)

It follows by setting y=C^-1 x in the accretivity inequality and using
`||x||<=U||y||`. This bound may be much smaller than gamma. Thus PS13's
old gamma-coefficient envelope cannot simply be copied for this new
interpolation. To combine that regulator with PC23, its auxiliary radius
and source radius must be chosen to fit a_C/U^2 instead. Original G,
Omega, and their thresholds are not changed by such an auxiliary choice;
any extra chart complement is retained.

## 7. Complete-reader interpolation and endpoint factorization

For every connected label S choose, using geometry alone, a nearest-neighbor
spanning tree tau(S) on all its coarse cells. An ordered breadth-first tree
with a fixed torus ordering suffices. For bond variables 0<=t_e<=1 put

    w_S(t)=product_(e in tau(S)) t_e, w_singleton=1,
    C(t;V)=c0 I+sum_A w_(S_A)(t) D_A(V)
                     +sum_omega w_(S_omega)(t) E_omega(V). (PC26)

Both endpoints and every original coarse-link reader, including its second
endpoint, belong to S. Weaken the whole D_A and each symmetrized E_omega
with its own complete-label monomial. PC24 applies. At t=1, C=K^-1.

Let Pi be any partition of Lambda, and set every bond crossing Pi to zero.
If a label S meets two parts, its spanning tree contains a crossing bond,
so its entire atom vanishes. Every surviving matrix atom has both field
endpoints and every datum it reads in one part. Thus

    C(t;V)=direct_sum_(B in Pi) C_B(t_internal,V_B).        (PC27)

This handles diagonal entries: an atom with i=j in B that reads data
outside B is removed when its label crosses Pi. Keeping it merely because
its field endpoints coincide would invalidate PC27. The coefficients of
C_B use no data in the other parts. The statement holds for the projected
complex domain as well as real admitted data.

To check actual Gaussian factorization, retain the normalized density on
all d=n0 T^4 scalar coordinates:

    g_C(x)=(2pi)^(-d/2) exp[-(1/2)Tr Log C]
                                     exp[-x^T C^-1 x/2].   (PC28)

Log is the holomorphic matrix logarithm on the right half-plane. PC24
keeps its spectrum there, so it fixes the determinant square-root branch
without a separate phase choice. This density integrates to one. One way
to verify the complex assertion is to start with real positive symmetric
C, where diagonalization gives the ordinary Gaussian integral, and continue
holomorphically on the convex domain of accretive complex symmetric
matrices. PC25 gives local dominated convergence; an open real symmetric
slice determines that holomorphic identity. At PC27, Log, the trace and
the quadratic form are direct sums. Consequently g_C is **exactly** the
product of the g_(C_B), and an integral of product functions over a product
of full-colour link balls factorizes with these same normalizers. No
expectation under a different interacting law is substituted.

This supplies Gaussian and coefficient locality at disconnected endpoints.
It does not assert that an unchanged white-cube indicator or arbitrary
retained history is already a product of such local functions. Every
additional interaction or reader in a proposed expansion still needs its
own exact full-support interpolation and domain justification.

## 8. Derivative scope, rate loss, and the intended exact consumer

The complete-reader interpolation is not the endpoint-only Schur mask of
PS12. For an independent bond variable e its derivative is

    partial_(t_e) C=sum_(atoms a:e in tau(S_a))
          [product_(f in tau(S_a),f!=e) t_f] F_a,
    F_a is D_A or E_omega.                                (PC29)

Every changed atom and every colour pair is included. Higher derivatives
are obtained by differentiating these monomials, not by differentiating
one covariance pair. For any 0<beta'<beta, absolute summation over ordered
k-tuples of bond derivatives has the finite bounds

    M_(beta')^(k)({w_(S_a)(t)F_a})
       <=k! (beta-beta')^(-k) M_beta({F_a}),                (PC30)

Here M_(beta')^(k) puts the k ordered bond indices into the atom sum,
with the endpoint supremum outside that entire sum. Precisely, it is the
maximum of
`sup_i sum_(j,a,e_1,...,e_k) exp(beta'|S_a|) sup|partial^k[w_(S_a)(t)F_a(i,j)]|`
and its column version. The supremum includes real t in [0,1]. The analogous
marked norm has its mark supremum outside the sum and is bounded with B_beta.
Each monomial contributes at most |S_a|^k ordered
choices, and `z^k exp[-(beta-beta')z]<=k!/(beta-beta')^k`. This proves the
claim and justifies fixed-order termwise differentiation. It is a bound
for covariance coefficients, not for all Gaussian-integral derivatives.

For a smooth test factor f_t on a fixed product chart, direct differentiation
of PC28 gives

    partial_t integral f_t g_C
      =(1/2)sum_(i,j) (partial_t C_ij)
                             integral f_t partial_i partial_j g_C
                       +integral (partial_t f_t)g_C.       (PC31)

The full determinant derivative is included. If bond values are later
chosen as path minima of a forest, the full chain rule through **all**
changed bonds and atoms is still required; forest-path connectors must
also be retained in any resulting support bound. Integration by parts on
the finite chart produces the PS15 boundary terms and higher corner traces.
PC30 has not summed those traces, the Gaussian derivative trees, or hard
history derivatives.

The currently supplied RD convergence lemma spends **two units** of
exponential support weight. The new beta in original-block units can be
far below two. Therefore PC19/PC30 cannot be inserted into that consumer
with its margins unchanged. A valid smaller-margin cluster estimate or an
explicitly matched regrouping and weight prescription remains a separate
obligation. For any actual joint use, output rates are at most the minimum
of this beta (or beta/2 after a derivative reserve) and the predecessors'
converted original-block rates. No rate conversion is implicit.

At the undeformed endpoint this is still the exact auxiliary-chart
identity, for the same original Wilson sources epsilon:

    Z_a=h_N^(m0 T^4) (2pi sigma^2)^(d/2) det K^(-1/2)
           exp[-F_epsilon(0;V)/sigma^2]
           integral_D dmu_(K^-1)(x)
               exp[-ell_epsilon.x-x^T E_epsilon x/2-R_epsilon(x)]. (PC32)

Here x=a/sigma, `ell_epsilon=sigma^-1 F_epsilon'(0)` is retained, and
E_epsilon and R_epsilon are the unchanged quadratic source and cubic-up
Taylor terms from PS5. K has no epsilon dependence, so its interpolation
is compatible with any already admitted original-source product disc;
this does not establish new bounds on the source-bearing factors. The
vacuum at epsilon=0 remains
`F_0(0)/sigma^2=uL^2 sum_P s(V_P)+4T^4 log N_t(I)`.
At intermediate t, PC28 includes its full det C normalizer. No replacement
of det K in PC32, component vacuum cancellation, or equality to the original
cut returned denominator is made. Complex Gaussian continuation proves
no complex continuation of moving physical hard indicators.

## 9. Exact achievement, remaining work, and provenance

The new author result is PC11--PC27: an actual finite-u, full-colour
covariance decomposition whose large reader-local pieces can be weakened
nonnegatively and whose remaining complete-reader atoms are uniformly
small in the absolute endpoint norm. PC6 and PC15--PC19 rebuild the inverse,
incidence and Neumann estimates; PC21--PC25 prove the complex stability.
PC28--PC31 fix normalization, factorization and finite-order chain-rule
meaning. This is a bounded positive construction, not a no-go assertion.

Still open are the interacting differentiated-integral estimates, all hard
surfaces and histories, same-component reference cancellation, the support
margin needed by RD, original-cut complex nonvanishing, effective-level
history identification and the multiscale/continuum arguments. The outside
chart theorem is not consumed here. The older PS packet and its receipt
are unchanged; this unit does not restamp their scope.

Bałaban's constructions and Dimock's expositions motivate the local
Gaussian organization. Positive finite-range covariance decompositions
are also studied by [Bauerschmidt, arXiv:1206.2212v2](https://arxiv.org/abs/1206.2212v2),
using finite propagation and spectral methods, and by
[Runa, arXiv:1510.07604v1](https://arxiv.org/abs/1510.07604v1) for spatially
varying elliptic coefficients. Those works are background only here: no
Dirichlet-form, translation-invariant, mean-zero or elliptic-system theorem
is imported as a theorem about this K or its original readers. This note
rebuilds the patch construction and its bounds directly. The limited
primary-source coverage is recorded in the read manifest.

The proof is written analysis. There are no numerical experiments, fitted
constants, claimed runner PASSes or independent author-issued verdicts.
Astra/max was requested; that request is not a backend attestation. Current
procedure is the same immutable observed-main methodology as the frozen PS
work, with every reused hash rechecked and PROCESS_LIGHT reread. The
coordinator owns PR #10114 integration and commissions the fresh hostile
review. Read ranges, protected-source identities and the author-only
algebra checks are frozen in this unit's checks/positive_reader_covariance_*
packet. Neither review nor eventual source landing constitutes an audit.
