# Real Gaussian density forests and finite original-parameter jets

This proves a dimension-free normalized REAL Gaussian derivative estimate,
its finite real mean/covariance jet version, a simultaneous tail estimate,
and a small-vertex integration theorem for the actual finite-range lift
core. It does not yet give the corresponding complete-reader theorem for
the full critical covariance. Section 8 identifies a quantitative cost of
one attempted localization; the cost is not a no-go theorem for other methods.

    actual_current_surface_status: bounded-support
    author_proposal_status: pending_fresh_independent_review
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    reachability_to_target: partially_closes
    audit_required_before_effective_retained: true
    bare_retained_allowed: false
    full_existence_established: false
    physical_continuum_mass_gap_established: false

Bałaban's localization and Dimock's exposition are antecedents to this lane.
No scalar/d=3 theorem or review verdict supplies a gauge-theory premise.
All variables below are individual real scalar coordinates in an HS basis
of su(N). Put D=N^2-1, m0=3L^4+1 and k=D m0 per original block; retain every
free whole link, root, harmonic, crossing and colour mode. This does not
replace the original Haar fibre, its normalizers, or its physical prefactor.

The actual source interfaces are RF6--RF24, MK14--MK29, WR1--WR29,
CG6--CG27, HC26--HC29, and REALRGA RGA2--RGA4/RGA13--RGA16. Their bounded
read coverage and immutable hashes are recorded after this source is frozen.
In particular CG15 is a normalized interacting chart expectation, not a
product Gaussian law. WR24's full C is P+E_lift+T_crit, not P alone.

## 1. The real normalized density and a sharper Hermite bound

Let I be a finite scalar set, d=|I|, C real symmetric positive definite,
m real, G=C^-1, and G<=B Id. Use the FULL normalized density

    g(x)=(2pi)^(-d/2)(det C)^(-1/2)
                    exp[-(x-m)^T G(x-m)/2].                     (RJ1)

For any multiindex nu, nu!=product_i nu_i!, not |nu|!, one has

    ||(partial^nu g)/g||_(L2(g)) <= B^(|nu|/2) sqrt(nu!),
    ||partial^nu g||_L1 <= B^(|nu|/2) sqrt(nu!).                 (RJ2)

At nu=0 both norms are EXACTLY one; at nu!=0 the signed integral is zero.
There is no factor per undifferentiated coordinate and no real-mean price.
The empty-dimensional density is one, with no nonzero-order field jet.

Proof. If X has density g, put Z=G(X-m), so Cov(Z)=G. Define H_nu^G by

    exp(t^T Z-t^T G t/2)=sum_nu t^nu H_nu^G(Z)/nu!.

The density quotient g(x-t)/g(x) gives
partial^nu g=(-1)^|nu| H_nu^G(G(x-m))g. Introduce an independent possibly
degenerate Gaussian Y with covariance B Id-G. Conditional expectation of
the generating function shows

    H_nu^G(Z)=E[H_nu^(B Id)(Z+Y) | Z].

The components of Z+Y are independent, with variance B. Multiplying two
one-dimensional generating functions and integrating gives exp(Bst), so
their degree-n squared norm is B^n n!. Tensor multiplication and conditional
L2 contraction give RJ2. Coefficient extraction is justified first on a
bounded complex t set by Gaussian exponential integrability; all coefficients
are finite polynomials. Cauchy--Schwarz gives the L1 assertion.

For comparison the exact complex translation identity is

    ||g(. -z)/g||_(L2(g))=exp(z*Gz/2).                         (RJ3)

Writing z=a+ib and integrating exp(2a^TZ-Re(z^TGz)) proves it. Independent
Cauchy radii sqrt(nu_i/B) give the weaker proposed factor
(exp(1)B)^(|nu|/2)sqrt(nu!). RJ2 improves that constant. Neither proof calls
a complex covariance a positive probability density.

If an ambient C satisfies c Id<=C<=Lambda Id, its PRINCIPAL C[I] satisfies
the same inequalities, hence RJ2 has B=1/c, uniformly in I. It is C[I],
not (C^-1[I])^-1, that is the covariance of the normalized marginal.
Integrate unused coordinates before applying any absolute bound.

## 2. Density-only forests on the actual real covariance domain

Fix ONE ambient R and beta=(16R)^-4 with the RF/WR conditions. On real
admitted V,epsilon,y, RF gives a real full-colour family

    C=P+E,  P>=c0 Id, ||P||op<=g_cov,
    M_beta(E)<=e<=min(c0/8,1/(4v_I),a/(64v_I^2)),
    B_beta(E)<=B_E<infinity.                                    (RJ4)

P is rebuilt from the actual principal patch inverses, including holes.
M takes individual atom suprema then absolute row/column sums; B marks a
full original reader and sums all its scalar entries. Both tails and all
membership/exterior readers are present. B_E is not assumed small.

Partition active field coordinates into sets I_a whose full finite-patch
collars are disjoint, so P[I] is block diagonal. Keep diagonal E blocks,
multiply each off-diagonal E_ab by an independent real s_ab=s_ba in [-1,1],
and keep any fixed real mean m_I. Entrywise absolute row bounds prove

    (c0-e)Id<=C_I(s)<= (g_cov+e)Id,
    B_R=(c0-e)^-1, Lambda_R=g_cov+e.                            (RJ5)

Thus the entire real interpolation cube has a normalized positive density;
no independent signed weakening of a large core atom is being used.
For bounded measurable Phi, with all hard predicates held fixed,

    partial_(s_ab) int Phi(x)g_(C_I(s),m_I)(x)dx
      =sum_(i in I_a,j in I_b) E_ij int Phi partial_i partial_j g dx.
                                                                    (RJ6)

The heat identity partial_C g=(1/2)partial^2 g follows by differentiating
the normalized Fourier transform exp(i xi.m-xi^T C xi/2). The two symmetric
off-diagonal entries cancel 1/2. Gaussian differentiation is L1 continuous
on every compact SPD set, by its explicit polynomial-times-density form.
Consequently RJ6 and all repeated density derivatives hold for arbitrary
bounded measurable Phi, without differentiating Phi or its cut boundaries.

Apply the finite forest identity to the independent variables s, BEFORE
evaluating them at path minima. For a forest F its pair value is the minimum
of its edge clocks along the connecting path, or zero between components.
For completeness, this identity follows by successively integrating the
largest clock that first joins two current components; the fundamental
theorem of calculus gives either no new join or that joining derivative.
Order ties have measure zero. Each final forest with a strict clock ordering
has one such sequence; the ordering regions partition [0,1]^F. The empty
forest gives the zero matrix.
This is the MK23 clock argument on a smooth finite-dimensional function.

For n forest edges and an endpoint assignment, let nu_i count its scalar
legs, so |nu|=2n. RJ2 bounds that term by

    ||Phi||infinity B_R^n sqrt(product_i nu_i!)
                         product_(edges ab)|E_(i_ab,j_ab)|.       (RJ7)

All scalar endpoints, repeated legs and full edge-atom readers must be
summed. RJ7 is an all-order derivative bound, not an already summed
connected estimate. At disconnected masks the normalized density factors
over field components, but each diagonal density still reads all data in
its actual C and m. This distinction is essential in section 8.

## 3. Exact finite real parameter jets, including the moving density

Let C(t),m(t) be real C^q families on an open real parameter domain, with
C>=c Id, q<=10. Distinct formal labels may represent repeated physical
directions. Work in the finite algebra t_i^2=0. For a nonempty label set A
write m_A=partial_A m(0), C_A=partial_A C(0) and

    L_A=-m_A.grad+(1/2)sum_ij C_A,ij partial_i partial_j.
    partial_A g =sum_(pi partition A) product_(Q in pi)L_Q g_0.  (RJ8)

This is a finite Taylor identity. Indeed the characteristic function is
multiplied by exp[i xi.(m(t)-m(0))-xi^T(C(t)-C(0))xi/2]. Coefficients of
t_A give its partitions; the constant-coefficient differential operators
commute. Fourier uniqueness gives RJ8. Alternatively differentiate RJ6
and partial_m g=-grad g repeatedly. No holomorphic rough vertex occurs.
The determinant and every inverse derivative are already included in RJ8.

Put L=sqrt(2B), B=1/c, and for an active I define

    s_A(I)=L sum_(i in I)|m_A,i|+B sum_(i,j in I)|C_A,ij|,
    P_A(I)=sum_(pi partition A) sqrt((2|pi|)!)
                                      product_(Q in pi)s_Q(I).  (RJ9)

For an additional arbitrary scalar multiindex nu,

    ||partial^nu partial_A g||_1
                  <= L^|nu| sqrt(nu!) P_A(I), A nonempty.       (RJ10)

The identical bound holds for the L2(g_0) norm of that derivative divided
by g_0. Expand each L_Q into its scalar derivatives. At most 2|pi| extra
legs occur. Use sqrt((nu_i+j_i)!)<=2^((nu_i+j_i)/2)sqrt(nu_i!)sqrt(j_i!)
and product j_i!<=(sum j_i)!. The coefficients of one L_Q sum to s_Q after
the L powers are inserted, proving RJ10 term by term. For A empty use RJ2,
especially its exact zero-derivative value one, rather than introducing a
spurious constant. If s_A(I)<=|I|S, RJ10 costs a degree-|A| polynomial in
|I|, of degree at most ten; it does not cost a constant to the power |I|.

The same formula applies after the ordered Leibniz differentiation of
forest-edge coefficients and externally differentiable vertices. Every
label is assigned once to its actual factor. Forest legs retain their
individual scalar factorials. The fine dependence of each vertex may be
only measurable and bounded. Uniform finite external derivative envelopes
are needed for differentiation under the integral; a hard predicate that
MOVES with an external parameter does not satisfy this hypothesis for free.

## 4. Actual original units, Haar pullback and insertion readers

Use WR1's ordered coarse derivations and original sources J_p=u epsilon_p,
with u,kappa and every prescribed normalized kernel held fixed. At a real
evaluation point the genuine path is

    V_c(t)=exp(t_m B_mc)...exp(t_1 B_1c)V_c,
    epsilon_p(s)=epsilon_p+sum_(j=1)^n s_j xi_jp/u,
    m<=6, n<=4, ||B_ic||op<=h, |xi_jp|<=r_p.                    (RJ11)

The reversed exponential order realizes D_B1...D_Bm; noncommuting Lie
derivatives are not replaced by coordinate derivatives. Put r_*=max r_p.
WR15--WR16 use the ACTUAL real Haar change U_e=Z_e U0_e(V), on every free
link. Within-block links have U0=I. Thus the bare interior-plaquette cut
and Q_X=sum_owned ||Z_e-I||HS^2/N, all CG first-shell/absence tests, and the
original-a product chart are fixed in Z. Haar measure is unchanged. At
real sources the compact numerator and matched regional denominator are
positive, and WR17--WR21 give their genuine real jets under this pullback.
They keep the derivatives of each rough compact normalizer. This does not
make the G or white Omega predicates fixed, nor a general history fixed.

For the small-chart Gaussian the actual canonical RF/WR24 functions are

    m=b(V,epsilon)/sigma, C=K_*(V,epsilon)^-1,
    C=P(V)+E_lift(V)+T_crit(V,epsilon).                         (RJ12)

They are smooth on the real domain and have complete-reader coefficients.
The RF substitution branch and principal inverses agree on overlapping
actual-V charts; no new center or atom decomposition is chosen for each
derivative. For a regional statement retain its original exterior and
membership readers, and differentiate the prescribed physical boundary
substitution if it varies. A derivative at fixed y is not that derivative.

Here is a usable explicit bound, when the WR22 small-chart tube of radius
xi and source radius rho is available. Set t_d=V_beta(b), p=M_beta(P),
b_Pmark=B_beta(P). On the half evaluation tube the actual ordered path
estimate ||Log[V(t)V^-1]||HS<=4sqrt(N)h sum|t_i| permits Cauchy radii
xi/(16m sqrt(N)h) and u rho/(4n r_*). With 0^0=1 put

    F_mn=(16m sqrt(N)h/xi)^m (4n r_*/(u rho))^n.
    M_beta(m_A)<= (t_d/sigma) F_mn,
    M_beta(C_A)<= (p+e) F_mn,
    B_beta(C_A)<= (b_Pmark+B_E) F_mn.                         (RJ13)

The vector marked norm has the same t_d/sigma bound. Coefficient suprema
are inside these sums. Cauchy is used ONLY for the existing analytic
Gaussian library, not for rough vertices. Alternatively RJ8--RJ10 use
their directly proved real derivative budgets. The factor t_d/sigma,
the actual xi,rho, and every J-to-epsilon factor remain. They need not
be uniformly small in u. A large real mean costs nothing in RJ2 but its
derivatives can be large. Fixed-center HC jets and moving-center WR jets
are different functions until WR's real pullback/jet identification is used.

For an insertion-reader mark x replace s_A(I) in RJ9 by

    s_A^x(I)=L sum_(i in I,S contains x)e^(beta|S|)|m_A,i;S|
             +B sum_(i,j in I,S contains x)e^(beta|S|)|C_A,ij;S|.

The marked product bound is the sum over pi and a distinguished Q in pi
of sqrt((2|pi|)!) s_Q^x product_(Q'!=Q)s_Q'. This is a polynomial of degree
at most nine in |I| times the actual marked insertion budget. For several
specified marks sum their assignments to the occurrences, allowing several
marks on one occurrence and retaining that occurrence's full reader. A
union mark is bounded by this occurrence count. This pays NEW insertions,
not the baseline density's otherwise invisible remote readers.

Original label counts are exactly 4D|S| coarse scalar labels and 6L^4|S|
original plaquette sources. The absolute ordered-jet norm weights them by
sqrt(N)h and r_p, respectively. It dominates dense WR1 directions. Its
product inequality follows by assigning each ordered derivative position
to one factor and dividing by m!n!. If a dense coefficient envelope is
converted to this absolute norm, a rate loss d>0 costs exactly

    sum_(m<=6,n<=4) B_(m+n)(d)/(m!n!)
       *[64m D sqrt(N)h/xi]^m [24n L^4 r_*/(u rho)]^n,
    B_0(d)=1, B_j(d)=max(1,[j/(exp(1)d)]^j).                 (RJ14)

This is WR12--WR13's actual counting, not a scale-independent history count.

## 5. Simultaneous volume-tail marks

Assume also C<=Lambda Id. For r>=1 marks let I_l be nonempty scalar sets,
a_l their fixed centers, r_l their radii, H=union I_l, d_H=|H|, and

    r'_l=(r_l-||m_(I_l)-a_l||)_+,
    M=max_i #{l:i in I_l}.

If E is the simultaneous event ||X_(I_l)-a_l||>=r_l for every l, then
sum_l(r'_l)^2<=M ||X_H-m_H||^2. The principal marginal has covariance
<=Lambda Id, so the Gaussian exponential moment at t=1/(4Lambda) gives

    P(E)<=min(1,2^(d_H/2)exp[-sum_l(r'_l)^2/(4Lambda M)]).
    int_E |partial^nu g|
      <=B^(|nu|/2)sqrt(nu!)
         min(1,2^(d_H/4)exp[-sum_l(r'_l)^2/(8Lambda M)]).       (RJ15)

With no marks use the price one. The second line is RJ2 in L2 and
Cauchy--Schwarz. Replace its first factor by RJ10 for physical density
jets. This proves the full simultaneous
multi-mark cost without multiplying unsupported one-event probabilities.
Repeated coincident events cannot earn repeated independent rare prices:
the multiplicity M is necessary. No tail statement follows from G<=B alone.

For r disjoint whole blocks, d_H<=kr and M=1. If each effective radius is
at least p/2, the price per marked block is
2^(k/4)exp[-p^2/(32Lambda)]. It can be made small for large p; every marked
mode is paid. The actual b/sigma must satisfy the stated effective-radius
condition. Unmarked activated coordinates have no such prefactor.
Sphere delta distributions/side chains are not bounded measurable volume
events, so RJ15 does not replace MK/HC's trace/flux estimates. Conditioning
on E divides by its probability and can remove its rare price entirely.

## 6. A finite-core integration theorem for small real-jet vertices

Here is a concrete sufficient bare-step supplier. Use the actual REAL RF
finite core P(V), with zero mean, all scalar modes, and fixed ambient patch
choices. More generally a finite-local real mean is allowed if its entire
reader is included below. This theorem does not replace RJ12's full C by P.

Let a finite primitive family f_a(theta,x_(I_a)) be bounded measurable in
all real fine coordinates, and C^(6,4) in the actual external parameters.
Each has a nonempty connected full ambient reader S_a. Enlarge S_a to
contain every full patch reader touching I_a, all its field owners, data,
membership, boundary, normalizer, and any finite-local mean readers. If a
function is defined only under a fixed cap, extend it by zero outside that
cap BEFORE evaluating it; the cap must be parameter-independent in the
chosen real pullback. Let its uniform finite external jet norm be <=a_a.
Use either WR1's dense norm consistently throughout, or its absolute
ordered-label norm consistently throughout.

Assume the normalized density parameter jets satisfy s_A(I)<=|I|S for
every nonempty labelled derivative set of these orders, uniformly on an
OPEN real evaluation domain, with the corresponding direction/label sums
already included if the absolute norm is used. Define the explicit
degree-ten polynomial

    D_10(n)=1+sum_(0<=m<=6,0<=j<=4,m+j>0) 1/(m!j!)
              sum_(pi partition [m+j]) sqrt((2|pi|)!)(nS)^|pi|
           =sum_(l=0)^10 d_l n^l.                            (RJ16)

For any selected set A of primitives, with I=union_(a in A)I_a,

    T^(6,4)( E_(P,m) product_(a in A) f_a )
                         <=D_10(|I|) product_(a in A) a_a.   (RJ17)

Differentiate under the integral, use RJ8--RJ10 at nu=0 for the labels
landing on the density, and the ordered product rule for the remaining
labels. Factorial-normalized convolution is bounded by the product of
the vertex jet sums and the density jet sum RJ16. Fixed measurable cuts
are untouched. All unused modes integrate to one before differentiation;
the empty selected family is exactly one, with all its parameter jets zero.

This density-jet premise is verifiable for the actual P, not a hypothesis
of rough holomorphy. To see it directly, let kappa_j bound the absolute
row/column sums of j ordered parameter derivatives of the local lift K,
including the indicated direction weights (or the absolute original-label
sums). Its source derivatives vanish. These constants have an explicit
RF instantiation: choose a positive RF coarse radius eta_K on which its
local K-entry bound and b_abs=vK*(B_lift+gamma/4) hold. Each K entry reads
at most 11^4 original blocks. The paths RJ11 and scalar-label counting give

    kappa_j,dense <= b_abs [16j sqrt(N)h/eta_K]^j,
    kappa_j,abs <= b_abs [64j D sqrt(N)h*11^4/eta_K]^j,
    1<=j<=6.

For the absolute bound a single HS-basis direction has HS norm one; its
Cauchy factor 16j/eta_K is multiplied by its sqrt(N)h weight and at most
4D*11^4 labels. The row count is already in b_abs. These are finite-radius
estimates of the local K, not of a rough vertex. Retain eta_K and any
dependence of its admitted choice on other parameters. Inverse
differentiation on each principal patch gives the ordered-partition words

    D_A G_patch=sum_(Q1,...,Ql ordered partition A)
               (-1)^l G_patch K_Q1 G_patch ... K_Ql G_patch.

RF8's absolute row/column bound g_cov applies to every G_patch. Since at
most J=16^4 patches meet a row and e^(beta|S_patch|)<=exp(1), one obtains

    p_j=exp(1)J g_cov sum_(ordered partitions pi of [j])
                                g_cov^|pi| product_(Q in pi)kappa_|Q|,
    M_beta(D^j P)<=p_j,   B_beta(D^j P)<=n_R p_j.            (RJ18)

Here n_R=k(16R)^4; source-bearing covariance derivatives are zero. The
absolute-label version follows by distributing each ordered label among
the K factors before summing; the kappa_j already include those sums.
The cutoffs are geometry-only. Thus S=B max_(1<=j<=6)p_j suffices for zero
mean (with S=0 if P is parameter independent), B=1/c0. Alternatively use
the corresponding finite-radius Cauchy bounds for these same patch atoms.
All constants, h and any u dependence of kappa_j remain in S. No smallness
of S is asserted, and n_R marked constants may be large.

For delta>0 put

    C_delta=max(1,sum_(l=0)^10 d_l k^l B_l(delta)),
    alpha_a=C_delta exp(delta|S_a|) a_a.                       (RJ19)

Since |I|<=k sum_a|S_a| and t^l<=B_l(delta)e^(delta t), RJ17 is at most
product alpha_a for every NONEMPTY selected family. The large fixed
C_delta is a cost per primitive, not per merely activated scalar. When
the reference is parameter independent, D_10=1 and C_delta=1.

Let delta,d1,d2>0, mu=beta-delta-d1-d2>0, and

    Q_beta=sup_x sum_(a:x in S_a)e^(beta|S_a|) a_a,
    Q'=C_delta Q_beta<=min(1,d1,d2)/4.                        (RJ20)

Then the finite-core partition function

    Z_P=E_(P,m) product_a(1+f_a)

has a convergent complete-reader logarithm sum_Y H_Y with

    Z_P=exp(sum_Y H_Y),
    sup_x sum_(Y contains x)e^(mu|Y|) T^(6,4)(H_Y)<=Q'.      (RJ21)

For real vertices Z_P is positive under RJ20, even if an individual
1+f_a was not assumed positive. Complex-valued vertices have the canonical
branch supplied by the same convergent series. A fixed incompatibility
restriction on selected labels is also allowed if every forbidden pair
has intersecting readers; retain it in every selected set and grouping.

Proof of locality and convergence. Disjoint overlap components of the
S_a have disjoint field sets and no cross P covariance: a patch meeting
both would put its reader in both components. Their exact marginal is
therefore block diagonal. Each block and each vertex reads only that
component's full union. This proves factorization of the actual functions
and their jets, not only a moment inequality. Group selected primitives
by their unique reader-overlap components. These are hard-core polymers
with weights given by their jointly integrated products.

With v_a=exp[(beta-delta-d1)|S_a|]alpha_a and
b_a=exp[(beta-delta)|S_a|]alpha_a, the positive rooted-tree recursion
T_a=v_a exp(sum_(b:S_b meets S_a)T_b) has supersolution b_a: its child
sum is <=Q'|S_a|<=d1|S_a|. Every connected overlap graph has a spanning
tree, so this bounds the polymer norm at beta-delta-d1 by Q'. For the
hard-core logarithm, partition each connected incompatibility graph by
its deterministic Kruskal tree. Optional edges sum to (1-1)^number,
of modulus <=1. A second rooted-tree recursion spends d2 and bounds the
log norm by Q'. The finite jet product inequality applies at every node.

To establish nonvanishing without assuming it, multiply each selected
primitive by a scalar z. RJ20 leaves the same two supersolutions for
|z|<2 with doubled primitive weights. The formal exponential of connected
graphs equals the finite partition function by graph-component partition.
Absolute convergence identifies the two functions for |z|<2, hence at one.
All included real derivatives converge uniformly on compact subsets of
the open evaluation domain. This completes the theorem without holomorphic
dependence of the f_a on physical data or fine variables.

For example delta=d1=d2=beta/6 gives mu=beta/2 and the explicit sufficient
condition C_delta Q_beta<=beta/24 (beta<=1). If a dense coefficient bound
is first converted to absolute label jets with RJ14 at loss beta/8, retain
that extra loss: starting at beta and retaining the three margins beta/6
leaves 3beta/8, with all constants recomputed. There is no old two-unit
support reserve.
Enlarging a primitive by its patch collars also changes its input reader
norm; RJ20 is imposed on those enlarged readers, not on smaller old supports.

## 7. What this supplies for the real reblocking question

RJ2, RJ8--RJ15 and RJ17 eliminate the old K_g^|I| zero-order estimate for
a REAL normalized Gaussian used without absolute coefficient expansion.
They are compatible with bounded measurable buffers and finite original
jets. RJ18--RJ21 give an actual finite-core example of a smaller-rate
version of the integrated small-Mayer contract RGA14--RGA16, with explicit
polynomial losses. They do not establish its native input rate mu+2.
The scalar factorials remain available for a further density forest.

These statements do not assert the needed input-size bound on inherited
effective interactions. Their actual unregulated joint integrated jets,
complete readers and common normalized reference must satisfy RJ20. A
large finite C_delta, marked B_E, collar size or coarse/source jet factor
can defeat a claimed input even when its value alone is small. Unresolved
retained fine derivatives are not set to zero. The full R_h/Z_A in RGA2
is not changed to a product-reference expectation.

CG15's buffers already have a rare physical charge; MK/WR/HC pay their
finite active-volume costs with that charge, including scalar modes,
Haar factors, kernel vacua and critical action/determinant. A generic
small effective vertex need not have that reserve. Also the physical
small-chart nonlinear vertices have polynomial regulators and side/corner
chains. RJ21 assumes globally bounded measurable-in-fine vertices with
the displayed finite-jet envelopes; it does not provide those regulator
or trace bounds by dropping chart restrictions.

## 8. The full-reader localization cost that remains

For the actual C=P+E, keeping its normalized real density unexpanded gives
RJ2 but generally reads remote original data through E and b. It is not
a local coefficient on the field set or finite-patch collar. RF's full
reader-bond decoupling does have endpoint factorization, but differentiating
those reader-tree monomials needs its own complete chain rule and summed
forest bound. RJ7 alone does not prove that construction.

One natural alternative is the exact normalized covariance Taylor series,
with G=P[I]^-1<=B Id, fixed real mean and e_beta the absolute weighted
row/column norm of the symmetric E atoms:

    g_(P+E,m)=sum_(r>=0) (1/(2^r r!))(E:partial^2)^r g_(P,m).
                                                                    (RJ22)

Expand every atom and scalar index to retain its complete reader. At
4B e_beta<1, the absolute sum of the L1 norms of these lists, after an
additional scalar nu derivative, is at most

    (2B)^(|nu|/2)sqrt(nu!) (1-4B e_beta)^(-|I|/2).             (RJ23)

At nu=0 one can improve 4 to 2. This is a real-probability improvement of
the old complex pointwise determinant majorant, but it still has a volume
factor for this absolute reader expansion.

Proof. If Z_i are independent standard normals, their absolute moments
a_j obey a_(j+2)=(j+1)a_j, a_0=1, a_1=sqrt(2/pi). Comparing this recurrence
with sqrt(j!)/2^(j/2) proves sqrt(j!)<=2^(j/2)a_j for every j. Apply RJ2
to each list and split the extra nu factorials as in RJ10. With
A_ij=sum_S e^(beta|S|)|E_ij;S|, the resulting positive series is bounded by

    (2B)^(|nu|/2)sqrt(nu!)
            E_Z exp[2B sum_ij A_ij |Z_i Z_j|].

Symmetry and 2|Z_i Z_j|<=Z_i^2+Z_j^2 bound its exponent by
2B e_beta sum_i Z_i^2. Gaussian integration gives RJ23. Without the extra
factorial split its coefficient is B, giving the stated improvement.
Absolute L1 convergence justifies termwise Fourier transform; summing
exp[-xi^TE xi/2] yields the normalized Gaussian of covariance P+E. Thus
RJ22 is an identity, not a formal missing-determinant approximation.

Reader pins can also be kept quantitatively. For a nonempty set A of
specified mark labels x_l define

    D_A(I)=sum_(i,j in I,S contains every x_l,l in A)
                                      e^(beta|S|)|E_ij;S|.

The absolute list sum with each specified mark counted among its atom
occurrences is bounded by RJ23 times

    sum_(pi partition [q]) (2|pi|-1)!!
          [2B/(1-4B e_beta)]^|pi| product_(A in pi)D_A(I).     (RJ24)

To prove this, insert exp(sum_l t_l 1_(x_l in S)) in each positive atom
weight and differentiate once in each t_l. Partitions record which marks
land on the SAME occurrence. Each resulting quadratic form is bounded
by a nonnegative sum of Z_i^2 of total coefficient D_A. Under the isotropic
tilted Gaussian the product of r such forms has moment at most
(2r-1)!! (1-4B e_beta)^(-r) product D_A. This proves RJ24 including
repeated marks. The single-pin D_(x) is bounded by the actual B_beta(E);
it is not an endpoint row sum. No smallness of these marked budgets is
inferred. These are reader marks, distinct from the rare events in RJ15.

The residual support exponent in RJ23 is

    lambda_E=-(1/2)log(1-4B e_beta).

If |I|<=k|S_base|, paying it from a beta/6 support margin would require

    k lambda_E<=beta/6.                                      (RJ25)

RF16/23 and WR25 do NOT establish RJ25. In particular their lift-tail
upper bound is of order 1/R while beta=(16R)^-4; increasing R by itself
does not prove the required comparison. The actual critical shift
b/sigma also has remote readers. Keeping it real avoids a force price
in RJ2, but expanding all of its reader atoms is a separate localization
cost, not paid by that fact. Its finite physical jets RJ13 do not remove
the zero-order locality problem.

There is a precise limitation of this absolute-list method even for a
diagonal toy Gaussian. Take P=Id_d and E=e Id_d, e>0 small. The absolute
L1 sum of the lists in RJ22 factorizes as F(e)^d, where

    F(e)=sum_(n>=0)(e/2)^n ||phi^(2n)||_1/n!
          >=1+(e/2)||phi''||_1>1.                            (RJ26)

Here phi is the standard one-dimensional density. The multiindex factorials
come exactly from expanding the exponential of the commuting diagonal heat
operators. This example does not refute any bound on the signed normalized
integral, which remains one: every higher derivative integrates to zero.
It only rules out a unit bound uniform in d for THIS absolute list sum.
A connected reorganization preserving those cancellations or a directly
summed full-reader forest might improve it; neither is assumed here.

Thus the new supplier is RJ2--RJ21, with RJ22--RJ26 a proved, quantified
remaining obstruction for one attempted extension. No all-history return,
effective induction, full G/Omega comparison, non-free continuum existence
or positive physical mass gap follows. The complete physical critical
action, determinant, Haar/mode and kernel prefactors remain outside this
normalized Gaussian proposition exactly as in the actual parent identities.

## 9. Bounded primary comparisons and status

[Rahman, arXiv:1704.07912v1](https://arxiv.org/pdf/1704.07912v1),
Propositions 6--8, gives the multivariate Gaussian Hermite generating
function and moment identities. The supplied L2 contraction proof rebuilds
the estimate needed here; no novelty of Hermite calculus is claimed.

[Brydges--Slade, arXiv:1403.7244v2](https://arxiv.org/pdf/1403.7244v2),
sections 3.8, 4 and 5.1, separates Gaussian integration, regulator costs
and norm products. Its fermionic Gram contraction is not used as a bosonic
gauge estimate. RJ8--RJ21 rebuild the finite real calculus and grouping.

[Lohmann, arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1),
Theorem 1 and section 2.1.4, use an analytic interaction class and discuss
Gaussian parameter derivatives with compact restrictions. Those hypotheses
are not asserted for the rough vertices here. RJ6 differentiates the real
normalized density and retains fixed measurable predicates. The bounded
search found relevant antecedents, not a directly imported all-history or
full-reader finite-real-jet theorem. Exact returned read windows are in the
manifest; no unread theorem is credited with proof work.

This is an author proposal pending a different fresh hostile review. No
scientific numerical test, new physical axiom, predecessor edit, or review
verdict was used in place of the displayed derivations.
