# Regional critical fields with complete boundary and membership readers

This extends the existing actual one-step critical-field/covariance producer
to arbitrary deterministic subsets of the already gauge-fixed free **whole
links**, with arbitrary holes and sufficiently small frozen boundary fine
coordinates. Deep exterior links may remain arbitrary real compact fields in
a separate outside factor. All regional constants are uniform in the subset
and the ambient torus.
The atom library is canonical across region choices: agreeing original data
and membership on a full reader label give the same coefficient.

This is an author proposition awaiting fresh independent review. It is not a
rough-boundary theorem, a hard-history return, an effective-level induction,
or a proof of four-dimensional continuum existence or a positive physical
continuum mass gap. Both physical objectives remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual bare-step regional critical field and full-reader covariance on a fixed small joint coarse/source/boundary domain, uniform in deterministic whole-link regions and their holes; arbitrary deep exterior retained separately."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Prior scope and the exact regional object

[Source-local return](SOURCE_LOCAL_RETURN_ASTRA.md) already treats specified
Dirichlet compressions and constructs a critical branch on a global chart
near the trivial field. Its section 4 explicitly does not assert the arbitrary
holonomy/curvature-only class or arbitrary hole histories. [CB](COVARIANT_SOFT_BACKGROUND_ASTRA.md),
[SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md) and [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md)
provide the actual finite-u lift, analytic vertices and global critical branch
used here. [CD](CRITICAL_DETERMINANT_READER_ASTRA.md) and
[CA](CRITICAL_ACTION_READER_ASTRA.md) localize its full determinant and action.
[RD4](RD4.md), L1--L4, keeps an exact outside/inside factorization and states
the additional matched-reference obligations. LARGE55's regional discussion
still separates the small-field producer on regions with holes from those
history/normalization obligations. [GC13](GRADED_COMPLEMENT_ASTRA.md) already
gives a real conditional minimizer with a small local boundary, arbitrary far
exterior and an actual normal-cone equation; that minimizer may lie on the
chart boundary. It does not supply the analytic interior critical branch or
complete-reader/local-agreement expansion constructed here. None of these matches is
substituted for the construction below. No claim of literature priority is made.

Fix N>=2, D=N^2-1, odd L>=3, T>=2, real u>=1 and the admitted positive
compact kappa interval. Let E be the globally fixed set of free links in
FU's rooted block-tree quotient; n=|E|=(3L^4+1)T^4, n0=D(3L^4+1),
d=Dn and sigma^2=N/u. Tree coordinates stay zero. Every retained link has
all D scalar HS coordinates; no new gauge fixing or mode deletion is made.

Choose an arbitrary deterministic Lambda subset E. Put m_e=1_(e in Lambda)
and let I_Lambda be its scalar projection on every colour. From the fixed
actual field stencils of the original vertices define exactly

    B(Lambda)=union_(v: I_v intersects Lambda)(I_v minus Lambda).

Only these boundary links require complexified Lie-algebra coordinates
max_(e in B(Lambda))||y_e||HS<zeta. Put y^B_e=1_(e in B(Lambda))y_e and
extend it by zero elsewhere. This extension is used only to compute the
regional phase: every touching vertex has all its field inputs in
Lambda union B(Lambda). No restriction on deeper exterior links follows.

Decompose the **unsubtracted** actual phase into its original local vertices:

    F_epsilon(a;V)=sum_v F_v(a;V,epsilon),
    F_epsilon=F_0+sum_p epsilon_p W_p,
    F_0=sigma^2[-log w_0(U(a),V)-sum_(e in E)log j_N(a_e)],
    W_p=tr(2I-U_p-U_p^-1)/2.                              (RF1)

The original vertices are the Wilson terms (including their original
sources), normalized compact-kernel logarithms and free-link Haar logarithms.
Fix each field stencil I_v geometrically before choosing data or Lambda.
Overestimates of the actual word stencil are allowed, but no data-dependent
cancellation changes its membership. Define exactly

    F_Lambda(x;y,V,epsilon)
       =sum_(v: I_v intersects Lambda) F_v(I_Lambda x+y^B;V,epsilon).
                                                                  (RF2)

Every cross-boundary vertex belongs to F_Lambda once. If all exterior links
also admit small coordinates, write y^ext=(1-I_Lambda)y and define
`F_out(y^ext)=sum_(v:I_v disjoint from Lambda) F_v(y^ext)`; then exactly
`F_epsilon(I_Lambda x+y^ext)=F_Lambda(x;y^B)+F_out(y^ext)`.
An empty-stencil vertex belongs to F_out. Both sums retain their original
scalar vacua and source-only terms. For arbitrary deep compact exterior,
the outside **physical weight** is retained instead, as in RF27 below;
no global exterior coordinate phase is asserted. The finite-t normalizers
remain field dependent, with t=kappa u real and fixed. Complex continuation
uses inverse negative edges and separate backward means, not conjugation.

For a fixed chart D_Lambda define
`I_Lambda^chart=h_N^|Lambda| int_(D_Lambda) exp(-F_Lambda/sigma^2)dx`.
When the full exterior is in this coordinate chart, the exact joint top form factors as

    h_N^n exp(-F_epsilon/sigma^2) dx dy
      =[h_N^|E\Lambda| exp(-F_out/sigma^2)dy]
         [h_N^|Lambda| exp(-F_Lambda/sigma^2)dx].          (RF3)

Here w_epsilon=w_0 exp[-sigma^-2 sum_p epsilon_p W_p]. There is a useful
distinction if the exterior is held with its **physical Haar** measure. Put J_out(y)=prod_(e outside Lambda)j_N(y_e). The raw
conditional Haar fibre of w_epsilon is

    exp(-F_out/sigma^2) I_Lambda^chart / J_out(y),
    exterior Haar measure=h_N^|E\Lambda| J_out(y)dy.      (RF4)

This division only removes the inactive Haar factors already in F_out;
it is not a reference normalization. RF3--RF4 follow by multiplying the
actual chart densities. At complex data they are identities of the continued
top forms. No chart integral estimate or hard-selector transport is inferred.

## 2. The inherited local library and one ambient cover

Let K=F_0''(0;V), G_Lambda=(I_Lambda K I_Lambda)|_Lambda^-1, and denote
its precision on the retained scalar space by K_Lambda. Inverses below are
on that space and are zero-extended only afterward. In particular an ambient
zero extension is not inverted as a singular full matrix.

For real admitted V, FU2 gives gamma I<=K<=B I, scalar row/column bound
b=D B, field range two in coarse sup distance, and radius-three readers, with

    a_gap=1/max(4L^3(L+4)(60L^2)^2,2L^3/kappa_-),
    gamma=a_gap/2, delta0=min(1/24,a_gap/48),
    B=25+24kappa_+(5L)^2+N^2/6, c0=1/(2B).               (RF5)

This is the actual K including Wilson curvature error, the finite-t spread
kappa(1-c_N(kappa u))B_V and N^2/(6u) Haar term. Take FU's preliminary
coarse tube V_c=exp(v_c)Vbar_c, max||v_c||HS<eta, about real centers of
curvature delta_*. Its local derivative constant J0 gives
`max(row,col)||K(V)-K(Vbar)||<=J0 eta`. Initially require eta<gamma/(4J0)
and retain all FU/CB fine/coarse chart restrictions. Principal compressions
on **any** subset of scalar indices then have Hermitian part >=3gamma/4.

Use the already chosen ambient R of the matching NRR/CD/CA library. Its
cutoffs are geometry-only and independent of Lambda: for T>=16R they obey
sum_A chi_A^2=1 with chi_A supported in N_(R+1)(Q_A),
A=N_(2R)(Q_A), S_A=N_(2R+4)(Q_A), and Lipschitz constant C_chi/R.
For T<16R there is one whole-torus patch with chi=1. Set

    J=16^4, s_R=(16R)^4, n_R=n0 s_R, beta=1/s_R, w=exp(1),
    C_chi=16(1+sqrt(2J)), r0=8,
    b_c=D B+gamma/4, m=(1/8)log(1+gamma/(4b_c)),
    g=(2n0/gamma)coth(m/4)^4,
    vK=n0*5^4, b_abs=vK*(B+gamma/4), J_abs=vK*J0,
    p=w J g, r=w(2J C_chi r0 b_abs g)/R.                 (RF6)

Every S_A has at most s_R ambient blocks; at most J labels meet a block.
The support is never intersected with Lambda or stripped of its holes.
It contains all original K-entry readers, both coarse-link endpoints, and
membership of every free whole link owned in A. A whole-torus patch on a
small torus has size <s_R, so that case has a uniform cardinality cost.

All matrix/vector norms below take individual coefficient suprema before
summing, uniformly also over the deterministic membership masks. M_beta is
the maximum absolute weighted row/column sum, B_beta marks a reader cell
and sums all scalar entries, and Q_beta=M_beta+B_beta. V_beta is the maximum
vector component-root and full marked-incidence sum. Labels are connected
ambient original blocks, and contain field endpoints and all data and
membership readers. Products obey

    M(AB)<=M(A)M(B), B(AB)<=B(A)M(B)+M(A)B(B),
    V(Ah)<=Q(A)V(h).                                    (RF7)

Marking the second factor uses the first factor's column bound. Each product
union is connected because consecutive factors meet at their summed scalar
index. Taking a supremum over masks is not summing over regions; it introduces
no region-count entropy. The entry envelopes and ambient incidence counts
below are uniform before that supremum.

## 3. Holes preserve the complete-reader lift covariance construction

For any A, let A_Lambda be its retained whole links and G_(A,Lambda) the
principal inverse of K on those scalar coordinates, zero-extended on Lambda.
An empty compression contributes zero. Conjugation by exp(m d_1(X_i,X_j0))
changes its operator norm by at most gamma/4: both endpoint sums change by
at most `(exp(m r0)-1)b_c`, and restriction can only decrease that bound.
Accretivity and a Neumann inverse then give

    sup |G_(A,Lambda)(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)],
    max(row,col)sum sup |G_(A,Lambda)(i,j)|<=g.           (RF8)

The n0-colour-density torus sum is bounded by the Z^4 sum. Arbitrary holes
introduce no new entries in the weighted perturbation. This proves both
endpoint bounds, including suprema over all masks; it is not merely a
pointwise operator estimate.

Restrict chi_A to Lambda and set, as operators on Lambda,

    P_A=chi_A G_(A,Lambda)chi_A,
    D_A=chi_A[G_(A,Lambda)-c0 I_(A_Lambda)]chi_A,
    R_A=-[K_Lambda,chi_A]G_(A,Lambda)chi_A,
    P_Lambda=sum_A P_A, R_Lambda=sum_A R_A.              (RF9)

Then exactly

    K_Lambda P_Lambda=I_Lambda-R_Lambda,
    G_Lambda=P_Lambda sum_(j>=0)R_Lambda^j,
    P_Lambda=c0 I_Lambda+sum_A D_A.                     (RF10)

To check the boundary identity, chi_A vanishes before the ambient patch
boundary by more than the K range. Thus
`chi_A K_Lambda G_(A,Lambda)chi_A=chi_A^2` on Lambda. Expanding K_Lambda
past chi_A gives RF10 and its negative commutator sign. Links absent from
Lambda are absent from both principal products. There is no omitted coupling
across a hole; such coupling to fixed exterior coordinates enters the force
in section 4, not this zero-field principal precision.

For real V, each principal inverse is >=1/B=2c0, so D_A is positive as a
whole full-colour matrix. The same ambient cutoff counts as FU apply: at
most 2J cutoff differences meet a K-neighbor pair, each costs C_chi r0/R;
then sum the K and inverse endpoints. The column estimate first restricts
the final cutoffs and uses the K and inverse columns. A marked patch has
at most n_R ambient rows. Consequently

    M(P_Lambda)<=p, B(P_Lambda)<=n_R p,
    M(R_Lambda)<=r, B(R_Lambda)<=n_R r,
    d_core=p+w J c0,
    e_lift=p r/(1-r),
    b_lift=n_R p[r/(1-r)+r/(1-r)^2],
    G_Lambda=c0 I_Lambda+sum_A D_A+E_lift,Lambda,
    M(E_lift,Lambda)<=e_lift, B(E_lift,Lambda)<=b_lift,
    m_G=c0 exp(beta)+d_core+e_lift,
    b_G=n0 c0 exp(beta)+n_R d_core+b_lift,
    Q(G_Lambda)<=A_G:=m_G+b_G.                          (RF11)

Here M(D)<=d_core and B(D)<=n_R d_core. Expand P R^j in actual indices;
symmetrize each j>=1 product with its transpose. Its exact sum is already
symmetric; this preserves its full label and both bounds. Marking P or a
residual factor gives the two displayed b_lift terms. For T<16R,
R_Lambda=0 even if Lambda has many holes; its critical tail need not vanish.
P_Lambda is rebuilt from patch intersections; it is generally not the
compression of the old global P.

Retain FU's eta_PC so `J g^2 J_abs eta<c0/8`. The exact principal inverse
resolvent identity bounds the aggregate unweighted endpoint norm of
`D_A(V)-D_A(Vbar)` by that quantity, uniformly over masks. Thus complex
continuation of the large core is a controlled perturbation of a real
positive core; it is not called positive by analytic continuation.

## 4. The new boundary force and a nonempty fixed joint domain

The boundary mask b_e(m)=1_(e in B(Lambda)) depends on membership of every
field stencil incident to e. Each such stencil has a radius-four root
reader; its other field owners lie within distance eight of X_e. Give the
common ambient coordinate family `y^B_e=b_e(m)y_e` the conservative reader
N_9(X_e), including both endpoints and all those membership flags. Unused
y values are ignored. With max_(e in B)||y_e||HS<zeta,

    V_beta(y^B)<=Y:=c_y zeta,
    c_y=n0*19^4 exp(beta*19^4).                          (RF12)

A marked cell sees at most n0*19^4 scalar coordinates with such readers.
The component-root sum is smaller. This pays the boundary-mask geometry,
not just the flag m_e. It is a per-reader bound, not a total-volume bound
on the boundary or a smallness assumption on the deep exterior.

Use FU's actual local majorants, recomputed at the fixed R above:

    q=(8L^4+8)D, s0=9^4, d0=(9L^4+5)9^4, d1=q d0, d2=q^2 d0,
    f(t)=H(1-t/a)^(-q), S(t)=f'(t)-f'(0)-t f''(0),
    N(t)=d1 exp(beta s0)[S(t)+t S'(t)],
    B_src=2d2 exp(beta s0)f''(0),
    D_H(t,rho)=2d2 exp(beta s0){f''(t)-f''(0)+t f'''(t)
                               +rho[f''(t)+t f'''(t)]},
    g_*=4sqrt(N)d1 exp(beta s0).                          (RF13)

H bounds the actual vacuum-subtracted local phase vertices, and a Wilson
vertex separately, on the common fine polydisc of radius a. Sources occur
only in their original Wilson roots. Taylor-expand there before substitution.
Root marks and substituted-field marks give respectively S and t S' for
the nonlinear force, and f'' and t f''' for the Hessian. The at most
9L^4+5 phase vertices per block, q scalar slots and radius-four readers
give d0,d1,d2. These are FU's actual finite-t/Haar counts. Restriction to
Lambda or insertion of membership masks can only discard terms; the full
ambient labels are retained. In particular, for h in the vector atom ball,

    F_epsilon'(h)=g0+K h+H_epsilon h+N_0(h)+N_epsilon(h),
    V(g0)<=g_*(1+rho)delta_hat, Q(H_epsilon)<=rho B_src,
    V(N_0(h)+N_epsilon(h))<=(1+rho)N(V(h)),
    Lip(N_0+N_epsilon; radius t)<=(1+rho)N'(t),
    Q(F_epsilon''(h)-K)<=D_H(V(h),rho).                  (RF14)

The source-linear Hessian H_epsilon=sum_p epsilon_p W_p''(0) remains.
Only the N terms start at quadratic order. The curvature factor in g0
comes from the actual Wilson force; kernel and Haar forces vanish at the
all-zero lift. They generally do not vanish at nonzero exterior y.

For a local K family assign K_ij the reader N_3(X_i) union N_3(X_j), of
size at most 11^4. A mark restricts its row to N_5 of that mark. Hence

    k_M=exp(beta*11^4)b_abs, k_B=n0*11^4*k_M, K_Q=k_M+k_B,
    Q_beta(K)<=K_Q,
    F_bd=g_*(1+rho)delta_hat+(K_Q+rho B_src)Y+(1+rho)N(Y).
                                                                  (RF15)

Indeed the regional initial force is exactly
`g_Lambda(y)=I_Lambda F_epsilon'(y^B)` and equals the projection of
`g0+K y^B+H_epsilon y^B+N_0(y^B)+N_epsilon(y^B)`.
This proves V(g_Lambda(y))<=F_bd. Terms containing y have actual touching
vertex readers near the retained/exterior interface before applying the
inverse. The bound is uniform in interface size; it does not assert a
small total boundary force or zero force at a flat V with nonzero y.

The following explicit ordering gives a nonempty domain. The constants
needed for the later active-core Gaussian inverse are R-independent:

    A1=(2n0/gamma)sum_(z in Z^4)|z|_1 exp[-m|z|_1/2],
    theta=min(m/2,c0/(2A1)), v_I=(2n0/c0)coth(theta/2)^4,
    a_P=c0/g^2,
    e_*=min(c0/8,1/(4v_I),a_P/(64v_I^2)).                 (RF16)

Fix the common ambient R, before choosing Lambda, so
`r<=min(1/4,c0/(32p),e_*/(4p))`, exactly the stronger NRR choice.
Recompute RF11 and RF13 at that R. Set

    d_reg=min(gamma/4,1/(4m_G),c0/(32m_G^2),e_*/(4m_G^2)).

Choose tau>0, then rho>0, inside the existing source/fine radii, with

    tau<min(a/16,r_CB/(8sqrt(D))),
    A_G[rho B_src+(1+rho)N'(2tau)]<=1/4,
    d_H:=D_H(2tau,rho)<=d_reg.                           (RF17)

Choose delta_*,eta,zeta positive last, below FU's real-curvature and
preliminary complex radii and eta_PC, so

    delta_*<=min(delta0,delta_CB,delta_A),
    delta_hat=delta_*+8eta<=min(delta_CB/2,delta_A,1/2),
    Y=c_y zeta<=tau/2, A_G F_bd<=tau/4.                 (RF18)

All choices are possible because N'(0)=D_H(0,0)=0 and F_bd tends to zero
with delta_hat,Y. They are independent of u,T,Lambda. Any previously imposed
consumer restrictions may further shrink this domain. Large-u conditions
for an integral theorem are not part of this field construction. The
construction remains valid under further restrictions satisfying RF17--RF18;
a chart margin can be imposed before the final tau/source/boundary choices.
The coefficient formulas and branch do not change on such common subdomains.

## 5. Actual regional stationarity and canonical local agreement

On V_beta(x)<=tau, set

    L_y(x)=I_Lambda[(N_0+N_epsilon)(x+y^B)
                                  -(N_0+N_epsilon)(y^B)],
    x_(n+1)=-G_Lambda[g_Lambda(y)
                         +I_Lambda H_epsilon I_Lambda x_n+L_y(x_n)],
    x_0=0.                                               (RF19)

All vectors on the right are zero outside Lambda. Since tau+Y<=2tau,
RF14--RF18 give contraction constant <=1/4. The image has norm at most
tau/4+tau/4=tau/2. The complete atom space therefore has a unique limit

    partial_x F_Lambda(b_Lambda;y)=0,
    V_beta(b_Lambda)<=t_Lambda:=2A_G F_bd<=tau/2,
    V_beta(b_Lambda+y^B)<=t_Lambda+Y<=tau.              (RF20)

The ordinary scalar-supremum contraction follows from the same local
Taylor counts and inverse row bound, without assigning an arbitrary
pointwise field a small marked norm. It identifies the same unique point
in the small complex cube. For real V,epsilon,y it is real, and throughout
the real cube the regional Hessian is >=3gamma/4 by RF17 and the real
principal gap. Thus it is the unique local minimum of the actual conditional
coordinate-density action there, not a global compact minimizer.

Here is the promised canonical construction, stronger than unrelated
per-region bounds. Fix the ambient torus/cover and a single list of original
vertices, Taylor monomials, scalar indices and patch-path words. Keep zero
coefficients when a mask removes a field or makes A_Lambda empty. The
zero-extended principal inverse reads only Lambda in A and V in S_A; its
matrix masks are part of S_A. The selection of a touching vertex reads every
membership flag in I_v, already inside that vertex's ambient reader.
The boundary atom b_e(m)y_e reads its original y value and the complete
incident-stencil membership mask inside N_9(X_e).

Expand RF19 by this fixed list of rooted substitution trees, with inverse
paths on its edges. At a nonlinear vertex choose x or y for each original
field slot; subtracting N(y) removes precisely the terms with no x child.
The linear H_epsilon chains are retained. Finite Picard depth includes the
corresponding finite-height trees. The positive scalar recursion
`Psi(t)=A_G[F_bd+rho B_src t+(1+rho)(N(t+Y)-N(Y))]` bounds their absolute
weighted sum. Its derivative is <=1/4 for 0<=t<=tau and Psi(0)<=tau/4.
Thus the finite-height positive tree sums increase to a bound <=tau/2; the
coefficient limit agrees with RF19 by uniform convergence. There is no
geometry-dependent choice of a branch. Every finite
word reads only its full connected union S. The limit, and any grouping of
words by S, converge absolutely and uniformly in the common parameter domain
and membership masks. This proves:

**Local agreement.** At the same ambient torus, corresponding atom
coefficients agree whenever original V,epsilon, the boundary y values where
they are defined, and every fine whole-link membership flag agree on the
complete ambient reader S. Dummy y values off B(Lambda) are ignored. The same
statement holds on overlapping coarse-center charts because the formulas
use actual V and the same pointwise branch. Membership is discrete data,
not a variable being differentiated. Joint holomorphy concerns V,epsilon,y.

This agreement does not integrate any exterior field or cancel any matched
reference by itself. It retains precisely the local information needed for
such a later comparison.

## 6. Regional critical covariance, active inverses and endpoint factorization

The exact regional precision and its complete-reader perturbation are

    K_*,Lambda=partial_x^2 F_Lambda(b_Lambda;y)
       =[I_Lambda F_epsilon''(b_Lambda+y^B)I_Lambda]|_Lambda,
    Delta_Lambda=K_*,Lambda-K_Lambda,
    Q_beta(Delta_Lambda)<=D_H(t_Lambda+Y,rho)<=d_H.        (RF21)

This retains boundary y, original sources, all substituted b readers and
membership. It is local in its field indices, not generally in its original
data; principal compressions of K_*,Lambda are not substituted for the local
lift core. Its inverse has the exact ordered series

    C_*,Lambda=G_Lambda(I+Delta_Lambda G_Lambda)^-1
             =P_Lambda+E_lift,Lambda+T_crit,Lambda,
    T_crit,Lambda=sum_(j>=1)G_Lambda(-Delta_Lambda G_Lambda)^j,
    h=m_G d_H<=1/4, b_h=d_H(m_G+b_G),
    t_crit=m_G h/(1-h),
    b_crit=b_G h/(1-h)+m_G b_h/(1-h)^2,
    M(T_crit,Lambda)<=t_crit, B(T_crit,Lambda)<=b_crit.    (RF22)

Mark the initial G or one of the j Delta G factors to obtain the displayed
two sums. Transpose-symmetrize each term without changing its full reader.
Both tails have M<=c0/16 and M<=e_*/3. Thus the actual total signed family
E=E_lift,Lambda+T_crit,Lambda has

    M_beta(E)<=2e_*/3, B_beta(E)<=B_E:=b_lift+b_crit.     (RF23)

B_E is finite and need not be small. Every word has the canonical local
agreement proved above; there is no unlabelled boundary dependence.

For independent 0<=theta_A<=1 and complex |z_l|,|w_j|<=1 the family

    C=c0 I_Lambda+sum_A theta_A D_A(V)
                         +sum_l z_l E_lift,l+sum_j w_j T_crit,j

has Hermitian part >=3c0/4. The real core is positive; its aggregate complex
perturbation is <c0/8, and the two tails each cost <=c0/16. With
`U_*=c0+d_core+e_lift+t_crit`, its precision satisfies
`Re C^-1 >= (3c0/4)/U_*^2` and `||C^-1||op<=4/(3c0)`.
These are auxiliary Gaussian statements, not physical mass-gap statements.

The undeformed local core also has the R-independent entry envelope
`sup|P_Lambda(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)]`: Cauchy--Schwarz gives
sum_A chi_A(i)chi_A(j)<=1. Hence its row/column sum is <=g and Re P_Lambda
>=c0. For every active whole-link set I subset Lambda, conjugating P_Lambda[I]
by exp(theta distance) changes its norm by at most theta A1<=c0/2.
Therefore its inverse obeys

    max(row,col)sum sup |P_Lambda[I]^-1(i,j)|<=v_I,
    Re P_Lambda[I]^-1>=a_P, ||P_Lambda[I]^-1||<=1/c0.     (RF24)

The last lower bound follows from
`Re P^-1=P^{-*}(Re P)P^-1` and ||P||<=g. These estimates also hold for
disconnected active sets and arbitrary holes. They are the normalized-active-
marginal inverse inputs, not an assertion that a physical marginal has a
principal precision.

To decouple by original readers, attach to each whole core or signed atom
a product of bond variables along a fixed spanning tree of its **complete**
ambient S. A crossing reader tree has a zero bond at a disconnected endpoint.
This removes remote-reader diagonal atoms as well as off-diagonal ones.
The baseline c0 I_Lambda is local. Every remaining coefficient depends only
on its full reader component, including exterior data and membership, and
the active Gaussian matrix is block diagonal there. Its determinant and
normalized density factor exactly; a component without active coordinates
contributes one. Positivity/accretivity follows from the admissible factors
above. This proves endpoint factorization, not an all-order differentiated
forest sum or nonlinear integral theorem. Derivatives of bond monomials
must still pay their full chain rule.

## 7. Determinant and action corollaries with all outside factors retained

The same principal construction applies to
`K_theta,Lambda=(1-theta)B I_Lambda+theta K_Lambda`, 0<=theta<=1.
The commutator gains theta and the gap/entry bounds stay uniform. Thus its
inverse has M<=m_det=p/(1-r), B<=b_det=n_R p/(1-r)^2.
For K_Lambda-B I_Lambda use
`a_K=exp(beta*11^4)(b_abs+B)`, `b_K=n0*11^4*a_K`.
Jacobi's finite homotopy and the actual critical trace series give

    LogDet K_*,Lambda=sum_(connected S) l_(Lambda,S),
    ||l_Lambda||_beta<=C_det,0+C_det,crit,
    C_det,0=n0 exp(beta)|log B|+b_det a_K+m_det b_K,
    C_det,crit=(m_G+b_G)d_H/(1-m_G d_H).                 (RF25)

The constant is D times the number of retained links owned at a block,
multiplied by log B, bounded by n0|log B|; its local membership is retained.
Every closed scalar path has full ambient readers. Marking a trace power
costs j and cancels its 1/j. Along K_Lambda+s Delta_Lambda accretivity
is >=gamma/2, so the determinant branch agrees with the accretive matrix
logarithm by the same finite Jacobi argument. Its inverse-square-root
budget is half RF25. This is generally an extensive, non-small determinant.

Holding y,V,epsilon fixed, stationarity gives the exact regional identity

    F_Lambda(b_Lambda;y)-F_Lambda(0;y)
      =-int_0^1 s b_Lambda^T partial_x^2 F_Lambda(s b_Lambda;y)b_Lambda ds.
                                                                  (RF26)

The Hessian has M<=k_M+d_H, B<=k_B+d_H uniformly on that segment.
Marking either vector or the Hessian, as in CA8, gives complete-reader atoms
for the difference divided by sigma^2, with budget
`(2k_M+k_B+3d_H)t_Lambda^2/(2sigma^2)`. Canonical local agreement is retained.
This is not an O(1/u) remainder. F_Lambda(0;y) remains its exact finite sum
of the original touching local vertex values. The outside phase/physical
weight remains separate as specified in sections 1 and 8. At nonzero y neither can be replaced by CA11's all-zero-lift formula:
actual means can differ from V_c and compact normalizers depend on y. Their
local vacuum constants and source values have not been canceled or discarded.

## 8. Fixed physical exterior, with arbitrary deep compact fields

Fix actual real exterior free links U_out, without making their deep values
move with U0(V). Define the outside-only physical weight W_out^H as the
product of the original Wilson/source and normalized-kernel factors whose
fixed field stencils miss Lambda. Haar factors are in the measures, not
in W_out^H. For boundary links only, set

    y_e(V)=log[U_out,e U0_e(V)^-1], e in B(Lambda).

Whenever these logarithms lie in the independent boundary domain above,
the actual touching factors equal those used to define F_Lambda. Thus
for real data the ordinary conditional chart Haar fibre is exactly

    Z_Lambda^H(U_out;V,epsilon)
       =W_out^H(U_out;V,epsilon)
                         I_Lambda^chart(y_B(V);V,epsilon). (RF27)

Both sides have the indicated coordinate continuation in complex V,epsilon.
This is a factorization identity, not a bound or nonvanishing theorem for
the integral. If all exterior coordinates are small, W_out^H is exactly
exp(-F_out/sigma^2)/J_out of RF4. No outside-only factor is normalized away.

Here is a nonempty physical specialization with a quantified tube. Suppose
at the real center Vbar each boundary link has
`U_out,e=exp(bar y_e)U0_e(Vbar)`, ||bar y_e||HS<=zeta/8. Additionally take
zeta<=1/4 and eta<=zeta/8. Internal lift links are I, so their boundary
coordinate is constant. For a crossing lift link U0_e=V_c,

    U_out,e U0_e(V)^-1=exp(bar y_e)exp(-v_c).

Its difference from I has HS norm at most
`exp(zeta/4)zeta/4`, hence operator norm <1/2. The convergent principal
logarithm series has HS norm at most `2exp(zeta/4)zeta/4<zeta`.
It is traceless by determinant one and continuity of this small branch.
Consequently the physical specialization maps into the independent joint
domain and is holomorphic. The extra coarse-link reader is within N_1(X_e),
already in RF12's full N_9 label. Its coefficient suprema and canonical local
agreement therefore preserve every bound above. RF18 still has positive
choices after these additional eta,zeta restrictions.

An outside-only kernel has all its actual fine inputs fixed real in U_out
(and the fixed tree links), so its mean M is fixed and its normalizer
N_t(M)>0 is the original real compact integral. Only its numerator varies
holomorphically with coarse V. Outside Wilson factors retain their actual
fixed real plaquette and original epsilon. No rough deep link has been
analytically moved with U0(V), and no assertion about a complex normalizer
at a rough moved mean is used. W_out^H remains explicit, without a uniform
price, logarithmic norm, history identification or exterior integration
conclusion. In particular the field-dependent normalizers are not replaced
by z_t, nor is a real maximizing functional analytically continued.

For Lambda empty the regional phase is zero, its field/covariance families
are empty, det=1 and LogDet=0; I_Lambda^chart=1. RF27 then gives the actual
entire w_epsilon(U_out;V), as required. RF3--RF4 give the same result when
the whole exterior happens to be in the small chart. For Lambda=E the
field/covariance construction reduces to FU on the common restricted domain;
adding any empty-stencil outside constants recovers the entire original
phase. Every retained link has all its colour coordinates.

No hard good/bad predicate, failure history or large-field event is part of
this analytic construction. An arbitrary or data-dependent region selected
by such an event requires its exact additional readers and normalization;
it cannot be inferred from the deterministic-mask supremum. No reference
ratio has been divided or a rough exterior integrated. Relevant-term
extraction, shifted-chart bounds, the entire original-cut return, effective
iteration, continuum existence and physical mass gap remain separate.

Bałaban's constructions and Dimock's expositions are architectural antecedents.
No scalar Dirichlet or multiscale gauge patch theorem is imported for this
nonabelian soft operator: its actual principal-compression proof is above.
No new primary-source theorem or numerical physics experiment is used.
Source freeze precedes compact provenance and fresh independent review.
The coordinator owns Git, PR #10114, shared fronts and audit/integration gates;
this author assigns no independent LAND or retained grade.
