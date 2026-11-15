# A positive local Gaussian core with an exponentially small reader tail

This constructs a different finite-range core for the ACTUAL local lift
precision, uniformly on all deterministic regions of retained whole links.
It gives an exponentially small complete-original-reader remainder, in both
endpoint and marked norms. The critical/source correction is then added
with its actual RF atoms on a newly specified common domain. The resulting
covariance meets the support-cost inequality proposed in [RJ25](REAL_GAUSSIAN_JET_FOREST_ASTRA.md).

The construction reuses the column-patch method of [WS5--WS6](WHITE_SECTOR_MATCHING_ASTRA.md)/[CW9--CW11](COMPLEX_WHITE_SECTOR_ASTRA.md),
rebuilt below for K_lift, arbitrary holes and ORIGINAL microscopic reader
weights. Its symmetric part becomes positive by closeness to the inverse.
No stronger estimate for the old RF partition-of-unity core is asserted.
The candidate polynomial/chunk method is not needed and is not imported.

    actual_current_surface_status: bounded-support
    author_proposal_status: pending_fresh_independent_review
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    reachability_to_target: partially_closes
    audit_required_before_effective_retained: true
    bare_retained_allowed: false
    full_existence_established: false
    physical_continuum_mass_gap_established: false

Bałaban's gauge localization and Dimock's exposition are antecedents. The
auxiliary Gaussian precision bounds below are not physical mass-gap bounds.
The nonlocal critical mean, inherited vertex sizes, full histories and both
physical targets remain separate obligations. No review verdict is a premise.

## 1. Actual matrix, domain and complete scalar counts

Fix the supplied finite-u action, real u>=1, N>=2, odd L>=3 and the original
rooted block-tree quotient. Put D=N^2-1, k=D(3L^4+1), sigma^2=N/u. Each
original block owns k scalar HS coordinates of the free whole links.
All root, harmonic, crossing and colour modes remain. The ambient torus
and a deterministic whole-link region Lambda may have arbitrary holes.

Use [RF1--RF5](REGIONAL_CRITICAL_FIELD_ASTRA.md)'s actual Haar-inclusive source-free lift Hessian

    K(V)=F_0''(0;V), K_Lambda=K(V)[Lambda],
    gamma Id<=K(Vbar)<=B Id,
    B=25+24 kappa_+(5L)^2+N^2/6.                              (SG1)

The curvature-only real center is admitted by RF5. K includes the finite-t
kernel spread and Haar term, with t=kappa u held fixed. Its field range is
two in block sup distance, hence at most eight in periodic face distance
d_1. Each entry reads N_3(X_i) union N_3(X_j). Every inverse on Lambda or
a smaller patch is taken on its retained scalar coordinates, then extended
by zero; no singular zero extension is inverted.

Choose a fixed preliminary coarse tube with the [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md)/RF analytic normalizer
and lift domains, small enough that

    ||K(V)-K(Vbar)||op <= J_K eta_K <= gamma/4,
    Re K_Lambda >= 3gamma/4,
    ||K_Lambda||op <= U_K:=B+gamma/4.                         (SG2)

One may take the conservative scalar perturbation constant J_K=RF6's
J_abs and impose eta_K<=gamma/(4J_K) together with the original restrictions.
Principal compression cannot increase this perturbation. Varying Lambda
requires no new radius. Let

    v_K=k*5^4, b_abs=v_K(B+gamma/4),
    m=(1/8)log(1+gamma/(4b_abs)),
    g=(2k/gamma)coth(m/2)^4,
    a_G=(3gamma/4)/U_K^2.                                  (SG3)

These constants are independent of patch scale, torus, region and holes.
The scalar envelope sum b_abs bounds both rows and columns before taking
suprema over all admitted data and membership masks.

For any principal patch A intersected with Lambda, conjugation by
exp[m d_1(X_i,X_j0)] changes its matrix by operator norm at most
(exp(8m)-1)b_abs=gamma/4, using both endpoint sums and the Schur inequality.
Its inverse therefore has norm <=2/gamma after conjugation. Consequently

    sup |K_(A intersect Lambda)^-1(i,j)|
                     <=(2/gamma)exp[-m d_1(X_i,X_j)],
    max(row,col)sum_j sup |K_(A intersect Lambda)^-1(i,j)|<=g.
                                                                    (SG4)

Restriction only removes entries from the perturbation estimate. The torus
distance sum is bounded by its Z^4 counterpart coth(m/2)^4; a chosen set
of shortest periodic representatives is a subset of Z^4. Every colour is
counted by k. Thus SG4 includes small tori and disconnected perforated
patches. It is an entry-envelope estimate, not just operator decay.

## 2. One geometric cover and original-cell reader norm

Let R>=8 be an integer, to be fixed in section 6 BEFORE final field/source
radii. Partition each circle into intervals of lengths R to 2R, with a
single whole interval if its length is <R. Take the product boxes q. Their
origin and ordering depend only on the ambient geometry, never on V or
Lambda. Define

    Omega_q=N_R(q),
    D_q=union of partition boxes intersecting N_(R+8)(q),
    J=9^4, n_R=k(2R)^4,
    s_R=J(2R)^4, beta=(16R)^-4, w=exp(2).                    (SG5)

There are at most nine intervals per direction in D_q. Before filling,
the enlarged interval has length <=6R; intervals meeting it have minimum
length R except in the single-interval case. The same bound applies in
reverse to boxes q whose D_q contains a fixed original cell. Wrapping
cannot increase these counts. Thus |D_q|<=s_R and at most J such labels
contain any original cell. Since J=6561<8192,

    exp(beta |D_q|)<=exp(J/4096)<w.                         (SG6)

This is an ORIGINAL-cell weight. It is not CW's separate white-box weight.
Every D_q is connected and includes every field endpoint and all original
coarse and membership data used by its patch. In particular entries of
K inside Omega_q read N_(R+3)(q); a residual row outside Omega_q is within
sup distance two of it and its K reader is inside N_(R+5)(q). D_q covers
both. It includes membership of all whole links in the patch and every
retained residual row. No support is intersected with Lambda to erase holes.

For an analytic matrix-atom family A define

    M_beta(A)=max{max_i sum_(j,S), max_j sum_(i,S)}
                                      exp(beta|S|) sup |A_ij;S|,
    B_beta(A)=sup_x sum_(i,j,S contains x)
                                      exp(beta|S|) sup |A_ij;S|.      (SG7)

All suprema precede the sums and include the stated data/membership domain.
The usual scalar-index multiplication gives, by the triangle inequality,

    M(AB)<=M(A)M(B),
    B(AB)<=B(A)M(B)+M(A)B(B).                              (SG8)

A product joins its two complete readers at a summed scalar index, so its
union is connected. The second marked term uses the first factor's COLUMN
bound. These statements hold for individual envelopes, not just a bound
on the final matrix. Symmetrizing each matrix atom with its TRANSPOSE and
the SAME reader preserves both norms and holomorphy. The transpose is
bilinear; Hermitian conjugation is not used in an analytic coefficient.

## 3. The exact column parametrix and exponential reader remainder

On the active scalar space let 1_q denote projection onto Lambda-owned
coordinates in q. Zero-extend the patch inverse on Omega_q intersect
Lambda, and put

    Q_q=K_(Omega_q intersect Lambda)^-1 1_q,
    R_q=-1_(Lambda minus Omega_q) K_Lambda
                         K_(Omega_q intersect Lambda)^-1 1_q,
    Q=sum_q Q_q, R_tail=sum_q R_q.                           (SG9)

If a patch has no retained coordinates its contribution is zero. Inside
the patch, K Q_q=1_q; outside it the displayed negative residual gives

    K_Lambda Q=Id_Lambda-R_tail,
    G_Lambda:=K_Lambda^-1=Q sum_(n>=0)R_tail^n.              (SG10)

The first identity includes every cross-patch active coupling. An inactive
link is absent from both principal products; its physical boundary force
belongs to RF's actual exterior problem, not to a missing matrix term here.

Assign each entire Q_q(i,j) or R_q(i,j) the reader D_q and treat it as one
analytic coefficient. Each column j belongs to exactly one q. From SG4,

    p=w g,
    r(R)=(2w b_abs exp(8m)k/gamma)coth(m/4)^4 exp(-mR/2),
    M(Q)<=p, M(R_tail)<=r(R),
    B(Q)<=J n_R p, B(R_tail)<=J n_R r(R).                 (SG11)

For the residual, i outside Omega_q and j in q imply d_1(X_i,X_j)>R.
Multiplication by K changes distance by at most eight, giving the entry
bound (2/gamma)b_abs exp(8m)exp[-m d_1(X_i,X_j)]. Spend half this
exponential on R and sum the other half over all endpoints. This proves
BOTH endpoint bounds in SG11 even though different columns use different
patches: their entry envelope is uniform before the sums. For a marked
cell there are at most J labels q and n_R columns in each, which proves
the marked bounds. The finite propagation of the residual keeps its row
and all K data inside D_q; the inverse is not truncated inside that patch.

For r:=r(R)<1, expand every Q R_tail^n into its patch/scalar-index words.
The reader is the actual union of its n+1 labels D_q, with cardinality at
most (n+1)s_R. The weight is paid factor by factor by SG8; the word is NOT
assigned a ball of radius nR with cardinality O((nR)^4). Define

    P_R=(Q+Q^T)/2,
    E_R=sum_(n>=1) sym(Q R_tail^n),
    G_Lambda=P_R+E_R,
    e_R=p r/(1-r),
    b_R=J n_R p [r/(1-r)+r/(1-r)^2].                       (SG12)

The equality follows because G_Lambda is symmetric and SG10 is absolutely
convergent. Symmetrize EACH word with its complete reader, not only the
final sum. Then

    M(P_R)<=p, B(P_R)<=J n_R p,
    M(E_R)<=e_R, B(E_R)<=b_R.                              (SG13)

Indeed marking Q or one of n residual factors gives
J n_R p(1+n)r^n; summing n>=1 yields SG12. Thus e_R is O(exp(-mR/2))
and b_R is O(R^4 exp(-mR/2)), with displayed constants. All series retain
every original-cell reader and all scalar modes. No ungrouped path-wise
contraction of K or an unweighted operator tail is substituted for SG13.

## 4. Positive core, complex stability and active marginal inverses

The support of Q_q is Omega_q by q, so P_R has field range at most 3R in
block sup distance (the two coordinates lie in q and its R-neighborhood).
Its coefficient readers are the full D_q. It is a genuinely finite-range
matrix with finite local data readers, although the two ranges differ.
Its local symmetrized atoms need NOT be positive individually.
Patch intersections are rebuilt for each region: P_(R,Lambda) generally
differs from the compression P_(R,E)[Lambda] of the whole-torus core.

Re G_Lambda=G_Lambda^*(Re K_Lambda)G_Lambda and SG2 imply
Re G_Lambda>=a_G Id. Choose R so e_R<=a_G/2 and e_R<=1/(4B), and set

    c_P=a_G/2, b_P=1/c_P, B_cov=2/c_P.
    Re P_R>=c_P Id; at real data P_R>=3/(4B) Id.            (SG14)

This follows from P_R=G_Lambda-E_R and ||E_R||op<=e_R. It proves positivity
of the whole real core, including arbitrary holes, without asserting any
positivity for an individual sym(Q_q). The complex continuation is
accretive on the fixed preliminary tube; it is not called positive.

Also |P_R(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)] by SG4, so its two
unweighted endpoint sums and operator norm are <=g, independently of R.
For every principal active scalar set I define P_R[I] as a COVARIANCE
compression, not an inverse principal precision. Set

    A1=(2k/gamma)sum_(z in Z^4)|z|_1 exp[-m|z|_1/2],
    theta=min(m/2,c_P/(2A1)),
    v_P=(2k/c_P)coth(theta/2)^4, a_P=c_P/g^2.               (SG15)

Conjugation of P_R[I] by exp(theta distance) changes its norm by at most
theta A1<=c_P/2. The same Neumann inverse proof as SG4 gives

    max(row,col)sum sup |P_R[I]^-1(i,j)|<=v_P,
    ||P_R[I]^-1||op<=b_P,
    Re P_R[I]^-1>=a_P Id.                                (SG16)

The last inequality uses Re P^-1=P^{-*}(Re P)P^-1 and ||P||<=g. These
are R-independent constants. Physical I retain whole links with every
colour; the matrix inequalities also hold for any smaller principal set.

## 5. Exact critical covariance, with a different retained atom family

Re-instantiate RF's original definitions on this SAME numerical R and
beta, imposing its RF16 condition as well as the conditions above. Its
partition-of-unity inverse atoms are a DIFFERENT representation of the
same matrix G_Lambda. Denote their bounds by m_G^old,b_G^old,A_G^old, as
computed by RF11 on this R. They are finite and can be large. Do not
identify their atoms with the Q/R_tail words by intersecting scalar domains.

Use RF's actual regional phase F_Lambda and its unique critical field
b_Lambda on the RF17--RF20 small joint domain, with boundary data only on
B(Lambda), the N_9 membership mask and
Y=k*19^4 exp(beta*19^4)zeta. All deeper exterior factors stay separate.
The actual local Hessian perturbation and critical tail are

    Delta=F_Lambda''(b_Lambda;y)-K_Lambda,
    Q_beta(Delta)<=d_H:=D_H(2tau,rho),
    h=m_G^old d_H<=1/4,
    T_crit^old=sum_(j>=1)G_Lambda(-Delta G_Lambda)^j,
    e_crit=(m_G^old)^2 d_H/(1-h),
    b_crit=b_G^old h/(1-h)
       +m_G^old*d_H*(m_G^old+b_G^old)/(1-h)^2.              (SG17)

Here the G factors INSIDE T_crit^old retain their RF patch/path coefficients
and every boundary, critical-field, original source and membership reader.
SG17 is RF21--RF23's exact convergent series, including its source Hessian
H_epsilon and all finite-t/Haar vertices. The local majorant D_H(t,rho)
vanishes at (0,0). The same original action and same unique b_Lambda are
used; no new field is postulated for the new core.

The reconstruction of the ACTUAL covariance is exactly

    C_*,Lambda=F_Lambda''(b_Lambda;y)^-1
              =P_R+E_new,
    E_new=E_R+T_crit^old,
    M_beta(E_new)<=e:=e_R+e_crit,
    B_beta(E_new)<=b_E:=b_R+b_crit.                        (SG18)

The old lift remainder is not added a second time. It occurs only inside
the explicitly retained old G words in T_crit^old. SG10 identifies their
matrix sum with G_Lambda before SG18; it does not equate two atom lists.
All new tail atoms are individually transpose-symmetric and keep their
full connected unions. b_E need not be small.

For independent complex |z_a|<=2 multiplying these tail atoms,

    C(z)=P_R+sum_a z_a E_new,a,
    Re C(z)>=c_P-2e,
    ||C(z)||op<=g+2e.                                    (SG19)

If e<=c_P/8 this gives Re C(z)>=c_P/2,
||C(z)^-1||op<=B_cov and Re C(z)^-1>=(c_P/2)/(g+2e)^2.
Every real symmetric weakening in this family is a genuine positive
covariance, including the independent real component-pair masks used by
RJ. A full-reader bond monomial of modulus <=1 can likewise multiply
each SMALL tail atom. All its derivatives must still pay their chain rule.

## 6. Nonempty parameter order and the RJ support inequality

Compute gamma,B,J_K,m,g,a_G,c_P,v_P,a_P FIRST on fixed preliminary ceilings,
independently of R and final source/field radii. For each integer R>=8 let
beta=(16R)^-4 and define the positive threshold

    e_goal(R)=min{c_P/8,1/(4v_P),a_P/(64v_P^2),
                 [1-exp(-beta/(6k))]/(4B_cov)}.             (SG20)

Choose ONE R satisfying RF16's old lift-core requirements and

    r(R)<=1/4,
    e_R<=min(1/(4B),a_G/2,e_goal(R)/2).                    (SG21)

This is possible: e_R decreases exponentially in R, whereas the only
vanishing threshold in SG20 is of order R^-4. The old RF requirements
have fixed endpoint constants before choosing R and are also achievable.
No numerical search or fitted threshold is needed for this existence
argument. Fix this R, its covers/orderings, beta and ALL old/new budgets.

Next choose positive tau and rho inside the original analytic fine/source
ceilings, imposing RF17 and the additional restriction

    D_H(2tau,rho)<=e_goal(R)/(4(m_G^old)^2).                (SG22)

This is possible because D_H(0,0)=0 and RF's force-derivative majorants
also vanish at the origin. Keep rho fixed once chosen. Finally choose
positive curvature, coarse radius eta and boundary radius zeta satisfying
RF18, eta<=eta_K, and, for fixed physical exterior specialization,
eta<=zeta/16. Thus the ACTUAL RF boundary force, not just curvature, lies
in the contraction ball. Every norm is recomputed for this one family.

Equations SG17/SG22 imply e_crit<=e_goal/3, hence
e<=5e_goal/6<e_goal. In particular 4B_cov e<1 and

    k[-log(1-4B_cov e)]/2 <= beta/12 < beta/6.              (SG23)

Thus the exact inequality named RJ25 holds, with a further beta/12 reserve,
on a nonempty fixed-source, small coarse/boundary domain. The source radius
can be much smaller than in an earlier instance; it has not been claimed
to retain a previously chosen numerical value. This is an original-reader
estimate on the exact covariance SG18, not an improved 1/R bound for RF.

The entire construction is uniform in u,T,Lambda on RF's admitted parameter
range. If a shrinking chart family is wanted, retain this R,beta,rho and
the chosen preliminary ceilings; then take tau(u)<=tau tending to zero
and curvature/eta/zeta small enough to satisfy the actual RF18 force bound.
For example tau(u)=c sigma p(u) with p(u)->infinity and sigma p(u)->0
works for sufficiently large u, with fixed sufficiently small coefficients
in curvature/eta/zeta proportional to tau(u). N(t)=O(t^2) makes RF18 hold
after decreasing those coefficients. The already chosen rho satisfies the
linear source/contraction requirements, and further decreasing tau only
improves SG22. No integral or all-cut theorem is inferred from this field
window. The nonlocal mean b/sigma can still grow like p(u).

## 7. Local agreement, interpolation scope and finite original jets

The partition, patch restrictions, scalar lists and orderings are fixed
once and for all. A Q_q or R_q coefficient agrees across two deterministic
regions whenever actual V and whole-link membership agree on D_q. Its
principal inverse is unique; all masks used in forming it are on that
reader. Product words, transpose symmetrization and absolutely convergent
tail sums preserve this canonical agreement. The old RF critical words
already have the same property on their own complete readers. Thus the
mixed representation SG18 has actual original-data/membership agreement.
This does not mean two DIFFERENT scale choices have identical coefficients.

For active fields I_a enlarge each primitive's reader by every D_q for
which Omega_q meets I_a. These added readers lie in a fixed finite collar
(N_(8R) of the field owners suffices); they include both Q_q and Q_q^T.
Disjoint overlap components then have disjoint field sets and zero cross
P_R covariance. Their principal core marginals, inverses, determinants and
normalized densities factor exactly. A component with no active coordinates
contributes one. P_R itself has no field-dependent arbitrary branch.

This is precisely the WHOLE-core grouping used in RJ's finite-core supplier.
It does NOT give RF's stronger independent theta_A>=0 weakening of large
PSD local core atoms: sym(Q_q) need not be PSD. Any interpolation which
weakens those large atoms separately requires another proof. Only the
unchanged core within its overlap components and the SMALL independent
tail weakenings SG19 are authorized here. A remote diagonal tail reader
must still be attached or removed by its full-reader mask, not treated as
a function of its endpoints alone.

The atoms are holomorphic on the stated small-chart domain, including the
actual critical field and physical boundary substitution from RF27. This
holomorphy is not asserted for a rough input vertex. For actual original
real coarse/source jets use [WR1](WEIGHTED_RETURN_JETS_ASTRA.md)/RJ11's genuine ordered paths

    V_c(t)=exp(t_m B_mc)...exp(t_1 B_1c)V_c,
    epsilon(s)=epsilon+sum_(j=1)^n s_j xi_j/u,
    ||B_ic||op<=h, |xi_jp|<=r_p, m<=6,n<=4.

On the half evaluation domain the exact log-chart displacement is bounded
by 4sqrt(N)h sum|t_i|. The Cauchy radii eta/(16m sqrt(N)h) and
u rho/(4n r_*) therefore remain in the common tube. With 0^0=1,

    F_mn=(16m sqrt(N)h/eta)^m [4n r_*/(u rho)]^n,
    M_beta(D_V^m D_J^n A)<=F_mn M_beta(A),
    B_beta(D_V^m D_J^n A)<=F_mn B_beta(A).                  (SG24)

Here each right-side norm is its full-domain envelope for the SAME atom
family A=P_R,E_R,T_crit^old or C_*. Source-bearing derivatives of P_R,E_R
vanish; all original sources in T_crit^old remain. Coefficient suprema are
inside the sums, so SG24 retains marks and spatial zeros. Finite joint
label sets use the corresponding product of their actual weights. All
couplings and prescribed kernel normalizers are held fixed in the original
J derivative. Moving-center and fixed-center functions are not interchanged.

For the physical fixed-exterior fibre keep U_out fixed REAL, set only
y_e(V)=Log[U_out,e U0_e(V)^-1] on B(Lambda), and apply SG24 to the composed
atoms. RF27 with eta<=zeta/16 maps the full tube inside their boundary
domain; its extra coarse reader is already within RF's N_9 mask reader.
Thus these are actual boundary-moving coarse jets. Holding y fixed would
compute a different derivative. Arbitrary deeper compact U_out only
occurs in the separate outside physical factor, which is not bounded here.

If absolute original-label jets rather than dense-direction jets are
required, each reader S has at most 4D|S| coarse scalar labels and
6L^4|S| original plaquette sources. For any d_rate>0 the additional loss
beta -> beta-d_rate has the explicit constant

    C_abs=sum_(m=0)^6 sum_(n=0)^4 B_(m+n)(d_rate)/(m!n!)
          [64m D sqrt(N)h/eta]^m [24n L^4 r_*/(u rho)]^n,
    B_0(d)=1, B_j(d)=max(1,[j/(exp(1)d)]^j).               (SG25)

The M and B finite-jet sums are bounded by C_abs times their respective
SG24 zero-order envelopes at beta. This follows by summing actual labels
and maximizing |S|^j exp(-d_rate|S|). For example d_rate=beta/12 is a
separate explicit loss; its large finite constant is not called small.
SG23 pays the covariance-density support price only. Later forest, reader
overlap, mean localization and vertex-jet estimates must pay their own
losses; neither SG24 nor SG25 asserts a completed connected return theorem.

## 8. Exact normalization and the remaining interfaces

For a principal active I, SG18 is the exact Gaussian covariance C_*[I].
Its density contains the full det(2pi C_*[I])^-1/2, on the branch continued
from real positive data. Re-expanding about P_R[I] changes no normalized
Gaussian measure. In the proposed RJ absolute-density estimate the factor
(1-4B_cov e)^(-|I|/2) is now bounded by

    exp[beta |I|/(12k)] <= exp[beta |S_base|/12]

whenever the full base reader contains the owners of I. All modes are
counted. This only pays that particular covariance-reader cost; RJ itself
is under a different fresh review at the start of this unit, and no verdict
from it is used as proof of the present matrix construction or SG23.

The actual full critical prefactor remains
h_N^|Lambda|(2pi sigma^2)^(D|Lambda|/2)
exp[-F_Lambda(b_Lambda;y)/sigma^2-LogDet K_*,Lambda/2], with the original
outside factor, inactive-Haar convention, kernel vacua and branches of
RF3--RF4/RF25--RF27. These were not changed by a covariance decomposition.
For Lambda empty all matrix families are empty, determinants are one,
log determinants zero and the regional chart integral is one; the full
outside physical weight remains. No reference denominator or original
hard-history predicate is normalized away.

The zero-order critical mean b_Lambda/sigma still has its full nonlocal
RF reader expansion. Positivity of a real Gaussian removes its unexpanded
mean price, not its reader-localization cost. No truncation, growing
collar or mean-tail compensation is proved here. Likewise no unregulated
small norm for inherited effective vertices is supplied, no rough retained
field is differentiated through a hard selector, and R_h/Z_A has not been
replaced by a product law. General histories, all-cut assembly, extraction,
effective iteration, non-free continuum existence and physical mass gap
remain OPEN.

## 9. Method comparisons and review status

The immediate antecedent is the explicit WS/CW column-patch parametrix,
not their white K_b matrix or their white-box norm. SG1--SG13 recheck the
actual local lift, all principal holes, microscopic counts and complete
readers. SG14's positivity-by-remainder and SG20--SG23's matched critical
radius order are the new compatibility steps. This is an alternative
representation; every predecessor source remains immutable.

[Bauerschmidt, arXiv:1206.2212v2](https://arxiv.org/html/1206.2212v2)
develops positive finite-range decompositions using finite propagation and
spectral/polynomial constructions. Its quadratic-form hypotheses and
regularity framework are not imported as a theorem about these gauge
reader atoms. [Benzi--Simoncini, arXiv:1501.07376v1](https://arxiv.org/html/1501.07376v1)
discusses decay of sparse matrix functions; entry decay alone is distinct
from the coefficient-wise reader bounds needed here. SG4--SG13 rebuild the
required inverse and marked estimates. The bounded primary read windows
are recorded in the manifest; no unread source supplies an estimate.

This source is an author proposal awaiting a different fresh hostile review.
No scientific numerical experiment, physical axiom change, predecessor edit,
Git/publication operation or audit action was performed in this unit.
