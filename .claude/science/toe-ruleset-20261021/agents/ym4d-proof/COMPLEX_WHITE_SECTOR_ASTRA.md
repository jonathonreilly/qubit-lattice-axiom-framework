# The original white scalar cube on a joint coarse/source tube

This constructs an explicit holomorphic integration chain continuing the
ORIGINAL source-free white scalar cube, and a connected logarithm of its
ratio to the TRANSPORTED original-a chart. The original Wilson sources
have one fixed positive radius. The coarse tube is quantified below and
can match HC35 when its cutoff and the supplied white cutoff are compatible.
No hard indicator is continued. Every actual critical-action, determinant,
Haar, finite-u kernel and scalar-cutoff factor is retained until its stated
exact cancellation. On the shrinking family below its logarithm is small,
generally O(sigma p_Omega^3), not asserted to be exponentially rare.

Bałaban's localization architecture and Dimock's expositions are credited.
The source mathematics is [SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), corrected
[FR](FIXED_SOURCE_RADIUS_ASTRA.md), [IC](INTERACTING_SELECTED_CORE_ASTRA.md),
[FK](FINITE_COUPLING_KERNEL_ASTRA.md), [RF](REGIONAL_CRITICAL_FIELD_ASTRA.md)
and [RC](REGIONAL_CHART_RETURN_ASTRA.md). The separately frozen
[WS](WHITE_SECTOR_MATCHING_ASTRA.md), 631 lines, is provisional at this
authoring checkpoint; its real matching is reconstructed here, and its
pending review is not a premise. [FT](FROZEN_TRANSPORTED_CHART_ASTRA.md)
and [HC](HOLOMORPHIC_COMPACT_RETURN_ASTRA.md) identify the intended chart
consumer; their frozen critical point is not substituted for this one.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. The literal phase, white cube and transported chart

Fix N>=2, D=N^2-1, odd L>=3, T>=2, and the supplied compact positive
kappa interval. Put m0=3L^4+1, n=m0 T^4, n0=Dm0, d=n0 T^4,
sigma^2=N/u and t=kappa u. The pinned internal trees, retained free
positive whole links, HS-orthonormal scalar basis and brick lift U0 are
those of SA1--SA3. Root, crossing and harmonic modes remain. The integrated
nonroot gauge Haar volume and its tree Jacobian are one.

About a REAL center Vbar with curvature at most delta, take

    V_c=exp(v_c)Vbar_c, max_c ||v_c||HS<eta,
    max_p |epsilon_p|<rho,
    U_e(a;V)=exp(a_e)U0_e(V),
    F_epsilon(a;V)=sigma^2[-log w_epsilon(U(a;V),V)
                                      -sum_e log j_N(a_e)]
                   =F_0(a;V)+sum_p epsilon_p W_p(a;V),
    W_p=tr(2I-U_p-U_p^-1)/2.                              (CW1)

The original paired-word kernel is, exactly,
k_t(V;M^+,M^-)=exp{t tr(V^-1 M^++M^- V)/(2N)}/Z_t(M^+,M^-).
For complex fine links M^- is the average of inverse words; it is neither
the inverse of M^+ nor its complex conjugate. Negative edges use inverse.
The complete field-dependent Z_t, original 24L^4 word average, Wilson
factors and one exponential Haar Jacobian per free link are in CW1.
All matrix transposes below are BILINEAR.

Let b_epsilon solve the actual equation F_epsilon'(b_epsilon;V)=0 and put

    K_epsilon=F_epsilon''(b_epsilon;V),
    b0=b_epsilon|_(epsilon=0), K0=K_epsilon|_(epsilon=0),
    C0=K0^(-1/2), T0=C0^-1=K0 C0.                       (CW2)

Their existence and branches on the joint domain are proved below. K0 is
the FULL finite-u, Haar-inclusive CRITICAL precision. It is not the lift
Hessian K_b=F_0''(0;V), the tree-phase Hessian, or the critical covariance.

Let p=p_Omega>=1 be the supplied original white radius. Define the chain
and its integral by their actual pullbacks:

    w in [-p,p]^d -> a=b0(V)+sigma C0(V)w -> U(a;V),
    Z_Omega(V,epsilon)
      =h_N^n sigma^d det C0(V)
          int_([-p,p]^d) exp[-F_epsilon(b0+sigma C0w;V)/sigma^2] dw,
    Z_a,tr(V,epsilon)
      =h_N^n int_(product_e B_(r_a)^D)
                              exp[-F_epsilon(a;V)/sigma^2] da.   (CW3)

B_(r_a)^D is the original whole-link HS ball; the white domain is the
original SCALAR cube. The white chain depends on V, not epsilon. At real
V it is exactly SA15's physical Omega, once branch equality is checked.
At complex V, CW3 is its definition as an oriented holomorphic chain.
It is not an indicator of a complex event. The complex Jacobian is
sigma^d det C0, never its modulus or a Hermitian Gram square root.
The holomorphic Haar top form has pullback h_N j_N(a_e) da_e:
right multiplication by U0_e(V) preserves it since SL(N,C) is unimodular.
In the white Jacobian V is held fixed while differentiating w. Thus no
extra moving-lift Jacobian is hidden in CW3.

For the real interpretation keep the original SA30 margins, with
A_box=sqrt(D)[C_b delta_hat+sigma p M_C]:

    A_box<r_ch, delta_hat+4A_box<delta_f,
    5L A_box<eta_G, delta_f<=epsilon_1,
    r_a<=epsilon_1/8, delta_hat=delta+8eta.               (CW4)

Here delta_f,eta_G are the supplied G thresholds. On the real coarse slice
these imply Omega subset G subset chi_cut and D_a subset chi_cut, the
latter since every interior plaquette has defect <=4r_a<epsilon_1.
The original cut is INTERIOR-plaquette only. Neither Omega nor G is
redefined, and no inclusion between Omega and D_a is required.

## 2. Actual local analyticity before any shrinking radii

FK1--FK16 prove for the independent pair (M^+,M^-) near (G,G^-1), with
G unitary, the exact nonzero factorization
Z_t=exp(t phi_*)t^(-D/2) A exp E_t for real t>=2t0. Its proof translates
the WHOLE compact group, retains the scalar SU constraint and Haar
amplitude, and bounds the remainder by C/t on a fixed pair neighborhood.
In particular the logarithm is a specified holomorphic function there.
Use u>=u_F=max(N,2t0/kappa_-); there is no small-complex-t assertion.

The field matching is quantitative. Let eta_N be FK3 and p_L=5L-4.
Set a_joint=log(1+eta_N/(4sqrt(N)))/(p_L+1). A word has at most p_L fine
and p_L coarse displacement factors. Telescoping their exponential series
gives a mean distance at most sqrt(N)(exp[p_L(a_x+a_v)]-1) from its
fixed real unit pair. Choose a common scalar radius a_f>0, smaller than
a_joint/(32sqrt(D)) and the original fine, coarse and Haar-log radii.
On twice these scalar polydiscs and eta_pre<=a_f/4, the sum of fine and
coarse HS displacements is at most 4sqrt(D)a_f+eta_pre<a_joint/4.
All actual means therefore stay strictly inside FK's fixed neighborhood. The analytic
traceless exponential branch and the nonzero j_N branch stay there too.

These local logarithms have actual-data branch agreement. FK4--FK6's
uniqueness on overlapping unit-pair neighborhoods gives the same saddle
W_*, hence the same S,lambda and full Hessian H_kernel. Its amplitude
uses the convergent Log(N H_kernel) near I; the error uses Log(1+r_t)
near one. Thus FK17 defines the same local phase on such overlaps,
including its real lift vacuum. A chosen Vbar does not add a logarithm
branch to the vertex coefficients below.

This supplies a finite constant H for each vacuum-subtracted local vertex
of CW1 and for a Wilson vertex separately, uniformly in u>=u_F and T.
Indeed sigma^2 t=N kappa is bounded; in FK17 the field variation of log A
is bounded and that of E_t is O(1/u). Their sigma^2 multiples are bounded.
The scalar kernel vacuum removed ONLY for this estimate is

    c_c(u)=sigma^2 log Ntilde_(kappa u)(I),
    sum_c c_c(u)=4T^4 sigma^2 log Ntilde_(kappa u)(I).     (CW5)

It is restored in F everywhere. Haar has vacuum zero. The Wilson lift
value is bounded and is not deleted. Sources multiply the same original
Wilson vertices. Thus the scaled local analytic constants have no hidden
u, 1/eta, 1/delta, 1/r_a or 1/zeta factor. This argument uses the full
finite-t factorization to establish analyticity and bounds, not a tree
replacement of the phase.

Let gamma,B,delta_lift be RF5's actual real lift gap, upper bound and curvature
ceiling. Set q_f=(8L^4+8)D. Enlarging H if necessary, the fixed number

    J_K=1000 q_f^3(H+1)/a_f^3                           (CW6)

bounds BOTH sums of individual entry suprema of K_b(V)-K_b(Vbar), divided
by eta. Differentiate a local vertex twice in fine scalars and once in a
coarse scalar. The Cauchy bound is 6H/a_f^3; a fine scalar sees at most
15 vertices and each vertex at most q_f slots of each remaining kind.
Summing those bounds before the parameter supremum gives CW6. There is
no interchange of a sum of suprema with a supremum of operator norms.

Choose eta_pre<min(a_f/4,1/100,gamma/(4J_K), the supplied local coarse
ceilings). For real centers in the real gap class,
Re K_b(V)>=3gamma/4 in the Hermitian-part sense. Every principal
compression has the same bound. The four-factor telescope gives coarse
curvature <=delta_hat=delta+8eta. A transported fine insertion and its
inverse have bounded norm, so an incident Wilson force is <=2sqrt(N)
delta_hat. Kernel and Haar fine forces vanish at the actual all-zero lift
also at complex V: all paired words there equal V_c, their first doubled
mean variation is tangent to (G exp(sX),exp(-sX)G^-1), and complex Haar
translation makes its normalizer and stationary value constant. This is
the local analytic identity proved by FK7/FK20, not positivity at a
complex mean. Hence the initial force is curvature-small.

## 3. Complex resolvents with complete scalar readers

The following conservative metric choice also handles every colour.
Let vK=n0*5^4, b_abs=vK B, b_c=b_abs+gamma/4 and b_s=max(1,gamma,b_c).
Use face distance d_1 between original block owners. Sup-distance range
two implies face-distance range r0=8. Set

    m=(1/8)log(1+gamma/(8b_s)),
    Q_m=n0 coth(m/2)^4, S_m=2b_s exp(8m).               (CW7)

The envelope row and column sums of K_b(V) are <=b_c. The same is true
with bound 2b_s for K_theta=(1-theta)b_s I+theta K_b(V). Conjugation by
exp(m distance) changes either endpoint sum by at most gamma/4. Together
with accretivity and the Schur inequality, a Neumann inverse gives, for
all principal compressions, theta in [0,1] and lambda>=0,

    |(K_(theta,Omega)+lambda)^-1(i,j)|
                    <=2 exp[-m d_1(X_i,X_j)]/(gamma+lambda).     (CW8)

This is a complex accretive estimate proved from a real center, not an
assertion that complex K is positive. The Z^4 sum is Q_m; periodic images
are counted with their original multiplicities.

Choose ONE R>=8 satisfying the white residual condition below and RF16's
stronger core/tail condition. Both endpoint requirements have constants
independent of R before this choice. Recompute RF/RC and, if consumed,
FT/HC on that same numerical R. Their cutoff-core and the white resolvent
families are distinct, explicitly retained representations.
Partition into R-boxes of side R to 2R, using a whole interval when shorter
than R. For each box q let Omega_q=N_R(q), D_q=N_(R+8)(q), filled by boxes.
There are at most s=J=9^4 boxes in D_q and at most J labels containing
a marked box. Its one-dimensional extent is <=6R; the safe count nine
also covers intersecting partition intervals and wraps. A box contains
at most n_w=n0(2R)^4 scalar modes.

Each K_ij reads N_3(X_i) union N_3(X_j). A residual outside index is
within sup-distance two of an inside index, so D_q contains both endpoints,
all principal entries, and every coefficient reader. In particular no
connector or remote coefficient reader is replaced by just its endpoints.
Use beta_w=9, w_w=exp(beta_w s), and individual coefficient suprema:

    M_w(A)=max{max_i sum_(j,S), max_j sum_(i,S)}
                                      e^(beta_w|S|) sup|A_ij;S|,
    B_w(A)=sup_q sum_(i,j,S contains q)e^(beta_w|S|)sup|A_ij;S|,
    Q_w=M_w+B_w, V_w=max(component-root, full vector incidence). (CW9)

All suprema include the whole admitted coarse/source domain. The exact
product estimates are M(AB)<=M(A)M(B),
B(AB)<=B(A)M(B)+M(A)B(B), V(Ah)<=Q(A)V(h). A product joins labels at
the summed scalar index; marking its second factor uses the FIRST
factor's COLUMN bound. These rules apply to every matrix power below.

Define local functions of the ACTUAL V, with no center-dependent Taylor
replacement of the matrix,

    P_q(lambda)=(K_b,Omega_q(V)+lambda)^-1 1_q,
    R_q(lambda)=-1_(Omega_q^c)K_b(V)(K_b,Omega_q(V)+lambda)^-1 1_q,
    p_w(lambda)=2w_w Q_m/(gamma+lambda),
    r_w(lambda)=2w_w S_m n0 coth(m/4)^4
                                  exp(-mR/2)/(gamma+lambda).     (CW10)

The identity (K_b+lambda)P=I-R_w has this negative residual sign.
Residual endpoints have d_1>R; spending half the exponential gives
M(P)<=p_w and M(R_w)<=r_w. At a marked box there are <=J labels q,
each with <=n_w columns. Thus B(P)<=Jn_w p_w, B(R_w)<=Jn_w r_w.
Choose R so r_w(0)<1/2. Its exponential decrease and RF's O(1/R)
condition can be imposed together, before any final field/source radii.

The actual inverse and its COMPLETE marked bound are

    G_lambda=sum_(k>=0)P R_w^k=(K_b+lambda)^-1,
    Q_w(G_lambda)<=A_w/(gamma+lambda),
    A_w=2w_w Q_m[(1-r_w(0))^-1+Jn_w(1-r_w(0))^-2],
    Q_w(K_b)<=Q_K=[1+n0(2R+10)^4]w_w b_c.              (CW11)

The squared denominator pays a mark on any residual. For the last bound
a marked box restricts the row owner to its distance-five collar. An
empty or small torus needs no lost volume factor; a whole-torus patch has
zero residual. Symmetrizing inverse atoms retains their full union and
does not increase either endpoint or marked bound.

## 4. Original sources, canonical critical atoms and both half powers

The actual local Taylor majorants at this fixed R are

    d0=(9L^4+5)(2R+8)^4, d1=q_f d0, d2=q_f^2 d0,
    f(t)=H(1-t/a_f)^(-q_f), S(t)=f'(t)-f'(0)-t f''(0),
    N_w(t)=d1 w_w[S(t)+t S'(t)], g_w=12sqrt(N)d1 w_w,
    B_src=2d2 w_w f''(0),
    D_w(t,rho)=2d2 w_w{f''(t)-f''(0)+t f'''(t)
                              +rho[f''(t)+t f'''(t)]}.          (CW12)

They count original vertices, original field slots and every substituted
reader. The doubled g_w covers section 2's complex transported Wilson force.
The source-linear Hessian has Q_w bound rho B_src; only the nonlinear
force starts at degree two. Its bound is (1+rho)N_w and its Lipschitz
bound (1+rho)N_w'. A reader mark is at the root or a substituted field,
giving S+tS' and f''+t f'''. This is the SA/RF proof with joint complex
local majorants; the real-V hypothesis is not silently carried over.

Choose bar_tau>0, then rho0>0, within all preliminary source/fine ceilings,
so RF17 and the following strict inequalities hold:

    bar_tau<min(a_f/16,r_CB/(8sqrt(D))),
    (A_w/gamma)[rho0 B_src+(1+rho0)N_w'(bar_tau)]<=1/4,
    d_w=D_w(bar_tau,rho0)<=gamma/4, A_w d_w<=gamma/2.     (CW13)

Next choose delta_pre>0 and reduce eta_pre if necessary so the real
curvature ceilings hold and
(A_w/gamma)g_w(1+rho0)delta_pre<=bar_tau/4. In the final tube require
eta<=eta_pre and delta_hat<=delta_pre, with delta_pre<=delta_lift and
the other real curvature ceilings. All choices are positive:
N_w'(0)=D_w(0,0)=0.
The constants were computed on fixed local analytic ceilings before this
choice; none depends on a future shrinking tube.

The exact Picard equation a=G_0[-F_epsilon'(a)+K_b a] gives

    V_w(b_epsilon)<=C_b delta_hat,
    C_b=2(A_w/gamma)g_w(1+rho0),
    Q_w(K_epsilon-K_b)<=d_w.                            (CW14)

For a coefficient construction fix original vertices, Taylor monomials,
scalar indices and patch words once on the ambient torus. Iterate by
rooted substitution trees, retaining the source-linear chains. Their
positive scalar recursion is
t -> (A_w/gamma)[g_w(1+rho0)delta_hat+rho0 B_src t+(1+rho0)N_w(t)].
It maps the bar_tau ball inside itself and has derivative <=1/4. Finite
height sums increase to its bounded fixed point and dominate every atom.
Thus the sums converge absolutely and locally uniformly, with all sources
at their original Wilson roots. A function's projection to its full reader
is controlled by completing data with the real center outside that reader.

The same unmarked row estimates give pointwise contraction in the ordinary
scalar cube ||a||infinity<=bar_tau; no arbitrary pointwise field is assigned
a small marked norm. To identify the original SA branch, retain its old
finite C_b,old and positive delta_A,old,rho0,old and further restrict
rho0<=rho0,old and delta_pre<=min(delta_A,old,bar_tau/(2C_b,old)).
On real V its original solution then lies in this same cube and equals
CW14. On the source-free IC common tube the same reasoning identifies
its actual critical branch; one may also impose its fixed ceilings and
delta_pre<=bar_tau/(2C_b,IC). These are finite positive restrictions.

For the global RF/RC branch use Lambda=E and tau_a<=bar_tau, retaining
RF17--RF18. Its solution also lies in the pointwise cube. The difference
of any two such solutions is <=one quarter of itself; hence the solutions,
their Hessians and their full critical values agree. No equality of
DIFFERENT atom decompositions is deduced from this uniqueness argument.

At every admitted joint datum the critical matrix has Hermitian part
>=gamma/2. The full resolvent family and its Stieltjes integral give

    (K_epsilon+lambda)^-1
       =G_lambda sum_(j>=0)[-(K_epsilon-K_b)G_lambda]^j,
    Q_w((K_epsilon+lambda)^-1)
                        <=A_w/(gamma+lambda-A_w d_w),
    C_epsilon=(1/pi)int_0^infinity lambda^-1/2
                                      (K_epsilon+lambda)^-1 d lambda,
    Q_w(C_epsilon)<=Q_C=A_w/sqrt(gamma-A_w d_w),
    Q_w(T0)<=Q_T=(Q_K+d_w)Q_C.                          (CW15)

Every series and integral is absolutely summable in M_w AND B_w, so its
reader marks commute with the integral. For Re z>0 the scalar integral is
z^-1/2: evaluate at positive z by substitution, then use holomorphy.
Applying that identity and its derivatives to a triangular matrix proves
C_epsilon^2 K_epsilon=I without diagonalizability. Its resolvents commute
with K_epsilon, and symmetry is bilinear; thus C_epsilon^T K_epsilon
C_epsilon=I. The right-half-plane branch is positive on real positive
matrices. In particular CW15 supplies the ACTUAL C0 and T0=K0 C0=C0^-1,
including all matrix readers, with no independent-colour factorization.

Canonical local agreement is stronger than existence on overlapping tubes.
The local principal inverses in CW10, all original vertex Taylor
coefficients, tree operations and Stieltjes weights are functions of ACTUAL
V and original epsilon on their stipulated readers. Fix their indexing
independently of Vbar, v and sources. Equal actual data on one complete
reader give equal coefficients term by term. Uniform absolute convergence
preserves this property. Different centers provide bounds for these same
formulas, not different chosen atoms. Only pointwise branch equality, not
atom equality, is asserted with RF or a different SA cover.

For completeness the same K_theta resolvents localize
d log b_s+int_0^1 Tr[K_theta^-1(K_b-b_s I)]dtheta, then
TrLog(I+G_0(K_epsilon-K_b)) localizes the critical determinant difference.
The full trace is paid by B_w. These non-small background terms are kept
in the physical prefactor, not added to a rare remainder.

## 5. Precision recentering on an independent-pair polydisc

Set C0,T0 at source zero, and define the source differences by projection
of the SAME coefficient lists before taking products:

    h=sigma^-1 T0(b_epsilon-b0),
    E_G=C0^T(K_epsilon-K0)C0,
    Q_epsilon=C0^T K_epsilon C0=I+E_G.                  (CW16)

Both h and E_G vanish coefficientwise at epsilon=0. This definition avoids
leaving spurious zero-source atoms in C0^T K0 C0-I. Radial Cauchy on the
rho0 original-source disc, for rho<=rho0/2, gives

    V_w(b_epsilon-b0)<=2C_b delta_hat rho/rho0,
    Q_w(K_epsilon-K0)<=2d_w rho/rho0,
    Q_w(E_G)<=C_E rho, V_w(h)/p<=C_h rho delta_hat/(sigma p),
    C_E=2Q_C^2 d_w/rho0, C_h=2Q_T C_b/rho0.             (CW17)

The lift part cancels before Cauchy. The argument scales the original
epsilon array by one auxiliary scalar to estimate its Taylor series;
it does not replace independent sources by a new uniform source. All
source labels and both half-power readers stay in the products. Symmetrize
precision atoms with their transposes, retaining the entire reader.

For ANY partition into coordinate objects, multiply each off-object
precision entry by its independent symmetric pair variable z_AB, |z_AB|<=2;
keep diagonal and within-object entries unchanged. The total perturbation
has both absolute endpoint sums <=2M_w(E_G). Hence

    Re Q(z)>=1-2M_w(E_G)>=1/2                           (CW18)

under the smallness condition below, uniformly in the number of objects.
This proves the actual independent-pair polydisc, not just a real forest
segment. Q is symmetric bilinear and Q_0=I even at complex V. Its logarithm
is the convergent trace series in E_G. No positive probability measure at
complex coefficients is asserted.

## 6. Exact recentering, end segments and bounded nonlinear readers

In CW3 put z=w-h. Subtract each original local vertex's Taylor polynomial
through degree two at b_epsilon. The linear jets sum to zero and the
quadratic jets sum to the ACTUAL Q_epsilon, so exactly

    F_epsilon(b0+sigma C0w)/sigma^2
      =F_epsilon(b_epsilon)/sigma^2+(1/2)z^T Q_epsilon z+U(z).   (CW19)

Individual vertices need not be stationary. U retains all higher terms
of the full finite-u density; no effective action is substituted.
For r=1/16 the exact one-coordinate integration chain is

    [-p-h_i,p-h_i] = [-p,p]+[-p-h_i,-p]+[p,p-h_i]
                         in holomorphic integration.          (CW20)

A primitive verifies the oriented endpoints. Its tensor product retains
all bulk, side and corner terms with their complex dz measures. Require
|h_i|/p<=r/4. Every coordinate on the deformation then obeys
|z_i|<=(1+r)p. With M_C=B_C=Q_C it is sufficient that

    C_b delta_hat+sigma(1+r)p M_C<a_f/2.                 (CW21)

This places the entire contour homotopy in the actual normalizer/Haar
analytic domain from section 2. There is no deformation of a hard G,
Omega-complement, cut or history predicate.

Expand each original vertex at zero BEFORE substituting b_epsilon and C0
atoms. A resulting reader contains its root, every background and whitening
reader, and every white coordinate used. Each U_S is bounded holomorphic
on the finite polydisc |z_i|<=(1+r)p. No finite physical-slot incidence is
asserted for white coordinates. Put t_*=C_b delta_hat,
x=sigma(1+r)p M_C, y=sigma(1+r)p B_C and
T3=f(t_*+x)-f(t_*)-x f'(t_*)-x^2 f''(t_*)/2. Then

    ||U||_(beta_w)<=sigma^-2 d0 w_w(1+rho0)
                       [T3+t_* partial_t T3+y partial_x T3]
                    <=A_U sigma p^3,
    A_U=(1+rho0)d0 w_w H 2^(q_f+3)(1+r)^3/(6a_f^3)
       *{[(q_f)_3+(q_f)_4]M_C^3+3(q_f)_3 B_C M_C^2}.    (CW22)

The three marks are root, background and whitening; (q)_k is rising
factorial. The integral cubic remainder and its two derivatives prove
CW22 when t_*+x<=a_f/2. This bound retains polynomial p cost instead of
claiming a high-degree white-field moment estimate from local incidence.

## 7. The FR precision forest with complex coarse coefficients

Here are the actual hypotheses and the proof checks for the general FR
library. Let z_p=(2pi)^-1/2 int_(-p)^p exp(-x^2/2)dx and

    Z_p(E_G,U,h)=z_p^-d(2pi)^-d/2
       int_(product_i Gamma(h_i)) exp[-z^T(I+E_G)z/2-U(z)] dz,
    delta_G=Q_w(E_G)+V_w(h)/p.                          (CW23)

Use beta_w=9 and output R-box rate one. Take C_s=B_s=2^20,
A_FR=2^20(1+C_s+B_s)^20 and
delta_G0=h_G0=min(r/256,1/(2^20 A_FR)). After fixing the previous constants
choose one FIXED radius

    0<rho<=min(rho0/2, rho_HC, delta_G0/[2(1+C_E+C_h)]),
    delta_hat<=min(delta_pre,sigma p),
    A_U sigma p^3<=h_G0/2.                              (CW24)

The optional rho_HC is omitted when HC is not a consumer. These conditions
give delta_G<=delta_G0/2, CW18 and the strict cube-shift margin. Source
radius does not decrease with u or p.

Split the diagonal eta_i of E_G from its off-diagonal pairs. Precisely,
q_p(eta_i,h_i/p)=(2pi)^-1/2 int_(Gamma(h_i))
exp[-(1+eta_i)z_i^2/2] dz_i. Divide this integral functional by q_p
to obtain nu_i(1)=1, and retain every outside factor q_p/z_p.
On fixed circles |eta_i|,|h_i|/p<=r, the oriented end pieces have
Re[(1+eta_i)z_i^2]>=3p^2/4 and |q_p|>1/4. Inserting exp(|z_i|/16), then
|z_i|^k<=k!16^k exp(|z_i|/16), proves the coefficient moment bound

    exp[C_s(a_i+s_i)] B_s^k k!, s_i=sum_(j!=i)e_ij.      (CW25)

Here a_i and e_ij are the weighted absolute atom masses, including h_i/p
and diagonal atoms. Marks on q_p's denominator are included by Cauchy.
At a_i=s_i=k=0 the normalized value is exactly one. Thus no fixed
constant is raised to the number of otherwise untouched scalar modes.
These estimates allow a bounded holomorphic reader on the finite
polydisc; they do not extend that reader to the full real Gaussian domain.

Mayer-group e^(-U_S)-1 by complete-reader overlap. Each decoration object
contains ALL white coordinates in its reader; unused coordinates are
singletons. Keep internal precision pairs. Between objects apply the
exact exponential forest with
u_AB=-sum_(i in A,j in B)(E_G)_ij z_i z_j and path-minimum factors.
Coefficientwise its proof assigns each occupied edge a clock with density
n_e t^(n_e-1); the possible maximum spanning forests partition probability
one. Expand every edge into its scalar endpoints and original coefficient
readers. The algebra works at arbitrary complex V and epsilon; the bounds
needed for the integrals are precisely CW18, CW21 and CW25.

For k_i incident legs the factorial is the INDIVIDUAL k_i!. Assigning
unordered children l_i leaves l_i+1 at an incoming endpoint, and one at
each other coordinate. The resulting planted majorant is

    T_i<=exp(epsilon_i)(1-x_i)^-2
       [1+sum_(Y contains i) a_Y^* exp(sum_(k in I(Y),k!=i)epsilon_k)
                                      product_(k in I(Y),k!=i)(1-x_k)^-1],
    x_i=B_s^2 sum_j e_ij T_j, epsilon_i=C_s(a_i+s_i).     (CW26)

The complete incidence norms imply
sum_(i in I(Y))(a_i+s_i)<=delta_G |Y| and
sum_(i in I(Y),j)e_ij<=delta_G |Y|. They follow by charging each term
to its reader, not by bounding the number of vertices using a white
coordinate. With CW24, T<=2 is a supersolution, its derivative row sum
is <1/2, and attachment costs are <=exp[(C_s+4B_s^2)delta_G |Y|].
Root marks are on a decoration, tree/internal pair, or scalar functional.
An internal-pair mark adds two scalar legs and has factor
2B_s^2(1-x)^-3; its pin sum is B_w(E_G). The opposite endpoint uses the
column bound. The differentiated recursion has inverse bound two. These
facts pay readers far from the final field endpoints as well as local ones.

Keep occupied-coordinate and decoration-core incompatibility. Reader
intersection is an allowed overcount for its tree bound, not a declaration
of physical independence. The FR support margins pay decoration grouping,
precision attachments, full-reader regrouping and the final hard-core log.
The Kruskal ordered-graph partition bounds its signed connected coefficient
by spanning trees. Isolated undecorated coordinates contribute one.
This gives an absolutely convergent complete-reader logarithm. Equality
first holds as a finite-volume interaction series near zero multiplier;
absolute convergence on the full multiplier disc proves nonvanishing and
the continued logarithm, before any division is made.

For U=0 ONLY, the corrected FR9 polynomial-moment comparison reserves a
factor exp(-p^2/64) on at least one changed tail/end. Summing the remaining
quadratic Taylor terms is legitimate by
sum_(i<j)e_ij|z_i z_j|<=sum_i s_i|z_i|^2/2 and CW18. The full Gaussian
integral is det Q^-1/2, including all scalar modes. A Cauchy multiplier of
the bounded U decorations then gives, with a fixed finite C_FR,

    log Z_p(E_G,0,h)=-(1/2)TrLog Q+T_p,
    ||T_p||_1<=C_FR delta_G exp(-p^2/64), T_p|_(epsilon=0)=0,
    log Z_p(E_G,U,h)-log Z_p(E_G,0,h)=J_p,
    ||J_p||_1<=C_FR A_U sigma p^3.                      (CW27)

This checks the FR proof on the joint domain, including independent pairs,
scalar normalizations, all factorials and marked sums. Its native real-V
scope was not extended by naming an analytic-continuation principle.
The O(rho) raw Gaussian determinant in the first line is NOT a rare term.
No rough compact numerator, discontinuous buffer or inherited history is
inserted into this bounded-holomorphic-reader theorem.

## 8. Cancellation of the identical full physical prefactor

The exact CW3/CW19/CW23 change gives

    Z_Omega=h_N^n(2pi sigma^2)^(d/2)det C0
       exp[-F_epsilon(b_epsilon)/sigma^2]
               z_p^d exp[-(1/2)TrLog Q+T_p+J_p].         (CW28)

For complex V, det C0=exp[-(1/2)LogDet K0] on the accretive functional
branch, not on a principal argument of the extensive scalar determinant.
The finite identity det Q=(det C0)^2 det K_epsilon and equality at
epsilon=0 give on the connected source polydisc, for EACH complex V,

    TrLog Q=LogDet K_epsilon-LogDet K0,
    det C0 exp[-(1/2)TrLog Q]=exp[-(1/2)LogDet K_epsilon]. (CW29)

One can verify the log identity by differentiation of determinants and
its zero value at epsilon=0. It uses no multiplication rule for
noncommuting matrix square roots. The common actual prefactor is

    P_epsilon=h_N^n(2pi sigma^2)^(d/2)
       exp[-F_epsilon(b_epsilon)/sigma^2-(1/2)LogDet K_epsilon].  (CW30)

Every colour, root/harmonic mode, finite-t spread, Haar constant and raw
kernel vacuum is here. The critical action and determinant are generally
extensive and non-small. IC's separate intrinsic TREE-Hessian/Gram and
white-ball Ward formulas are not used at the Haar-inclusive critical point.

For Lambda=E the RF/RC phase may omit original empty-field-stencil
vertices. Their explicit outside factor exp(-F_empty/sigma^2) restores
the full F in CW30. Scalar vacua inside nonempty vertices are already
retained and are not moved to F_empty. By the pointwise uniqueness in
section 4, RC's full K and critical phase in this formula are identical.
Keep every RC8/RC13 hypothesis at its recomputed fixed preliminary
ceilings and final shrinking radii. Its exact whole-region result gives

    Z_Omega=P_epsilon z_p^d exp(T_p+J_p),
    Z_a,tr=P_epsilon exp H_a,
    ||H_a||_(beta_a/2)<=epsilon_a, beta_a=(16R)^-4,       (CW31)

where epsilon_a is the full RC13 expression, including both covariance
tails, all modes, density normalizers, side/corner factors and translations.
No white inverse is substituted for its positive-core construction.

Fill each white R-box reader S by original blocks Y. It stays connected,
|Y|<=(2R)^4|S|, and a marked original block belongs to exactly one box.
Grouping equal readers by absolute convergence costs no root multiplicity.
Thus its output rate one gives rate 1/(2R)^4 in original blocks. Put
mu=beta_a/4; both families are controlled at rate 2mu. The exact ratio is

    log(Z_Omega/Z_a,tr)=sum_Y Gamma_Y
                         =d log z_p+T_p+J_p-H_a,
    ||Gamma||_(2mu)<=E_white
      :=n0 exp(2mu)|log z_p|+C_FR delta_G exp(-p^2/64)
                                    +C_FR A_U sigma p^3+epsilon_a. (CW32)

Assign n0 log z_p to each original block. This is the full d log z_p,
not a discarded vacuum. Both integrals and the ratio are nonzero on the
joint domain. The series chooses the logarithm matching the real positive
ratio at v=epsilon=0. It is a rooted local bound, not a volume-independent
bound on the unnormalized scalar ratio. No cancellation between the
different nonlinear coefficient libraries J_p and H_a has been asserted.

## 9. An explicit common shrinking family, including cutoff compatibility

First fix all local analytic ceilings, gamma,B,J_K and the single R. Then
choose bar_tau,rho0 with CW13 and RF17, compute all RC and white constants,
and fix rho by CW24 and any HC fixed-source restriction. Constants do not
depend on the final eta or on u,T. Restrict to the old SA/IC ceilings used
for branch identification. These are finite positive choices.

Let p_a=r_a/sigma denote the auxiliary chart cutoff, kept distinct from
the supplied p=p_Omega. Choose c_a>0 with strict RC8/RC17/FT21 margins
and put tau_a=c_a sigma p_a. Use the explicit RC17 boundary ceiling or
HC35's smaller c_z sigma p_a, although the full white/chart comparison has
empty exterior. For the HC-compatible example use exactly

    p_a=(log(2+u))^alpha, alpha>5/2,
    r_a=sigma p_a, tau_a=c_a sigma p_a, zeta=c_z sigma p_a,
    q=c_q sigma^2 p_a^2, K=K(q),
    delta=d_delta sqrt(q)/(4K+1)^2,
    eta=d_eta sqrt(q)/(4K+1)^2,                         (CW33)

with the strictly positive c_q,d_delta,d_eta satisfying HC35--HC36 and
the RF/RC constants recomputed at this R. Such constants exist there.
The additional white conditions are EXPLICIT:

    delta+8eta<=min(delta_pre,sigma p),
    sigma p^3->0, p->infinity, and CW4/CW21/CW24.       (CW34)

If the original cutoff is chosen as p=p_a, K(q)->infinity and
K(q)=O(log u), so (delta+8eta)/(sigma p)=O(K^-2). All fixed ceilings,
pointwise branch radii and CW34 therefore hold eventually. The same is
true for any already supplied profile with p_a/K(q)^2<=C_p p, after
choosing the fixed d_delta,d_eta so
sqrt(c_q)(d_delta+8d_eta)C_p<=1. They remain positive.
No replacement of an already fixed white cutoff is inferred from this
example. If that compatibility fails, the proved common window is instead

    delta<=min[d_delta sqrt(q)/(4K+1)^2, sigma p/4],
    eta<=min[d_eta sqrt(q)/(4K+1)^2, sigma p/32].         (CW35)

These positive widths imply CW34's curvature bound for sufficiently large
u and only restrict HC's proved tube; its cutoff limits remain required.
They may be strictly narrower; the real-center curvature class is
restricted at the same time. The original cube itself is unchanged.

For the common p_a=p profile, sigma p^3->0 and sigma p->0, while
delta_hat/tau_a=O(K^-2). Thus the full RF/RC force and contour margins,
normalizer analytic margins, eta<=zeta/16, real G/cut inclusions, white
end-segment margin and every small-log condition hold beyond ONE finite
u0 independent of T. Increase it for u_F and the finite fixed ceilings.
This is a finite list of demonstrated limiting inequalities, not an
unspecified intersection with an unproved shrinking domain. The source
rho remains fixed. In the general two-cutoff case one tests the same
displayed inequalities on the actual supplied profiles.

RC18 and the elementary scalar Gaussian tail yield

    epsilon_a<=C_a sigma^2+C_bnd(1+p_a^(91D+2))exp(-a_P p_a^2/64),
    |log z_p|<=C p^-1 exp(-p^2/2),
    E_white<=C_w sigma p^3+C_a sigma^2
       +C_w' rho exp(-p^2/64)
       +C_bnd(1+p_a^(91D+2))exp(-a_P p_a^2/64)
       +C_z p^-1 exp(-p^2/2).                           (CW36)

Every constant is fixed before u and volume. With p_a=p this has the
claimed O(sigma p^3) plus O(sigma^2) and explicitly rare cutoff terms.
A rare bound for the entire ratio would need a further matched
cancellation between J_p and H_a, which is not proved here.
For a bounded p the exact CW32 comparison and nonvanishing still hold
under CW24, but its retained scalar cutoff normalization need not tend
to one. No vanishing ratio error is asserted in that case.

## 10. Original derivatives, local agreement and the remaining interfaces

On concentric half tubes, for fixed original scalar multiindices ell,nu,
Cauchy's formula and the complete-reader construction give

    ||partial_v^ell partial_epsilon^nu Gamma||_(2mu)
       <=E_white ell! nu! (2D/eta)^|ell| (2/rho)^|nu|.   (CW37)

One uses the bound on the full outer tube; in CW35 eta means that actual
narrower outer width. A derivative at data outside Y is zero. Source
normalization subtracts Gamma(V,0); its bound is at most twice CW32 and
the constant d log z_p cancels exactly. No unscaled coarse derivative
class uniform in u is claimed.

There is also a summed anchored-input bound at rate mu. A reader Y has
at most 4D|Y| original coarse scalar inputs and 6L^4|Y| original sources.
For k derivatives, summing their positions therefore adds at most
(4D+6L^4)^k |Y|^k. Spend the rate reserve using
|Y|^k exp(-mu|Y|)<=k! mu^-k, besides CW37's actual radius factors.
This gives full input incidence without an ambient-volume derivative
norm. In the common profile eta^-1 has log size O(log u); CW36's leading
polynomial smallness need not survive arbitrary such derivative orders.

All white coefficients are canonical functions of actual V and original
epsilon on their full readers. Their pullbacks read Vbar and v on those
same owners. The RC family has its own fixed ambient indexing and its
own local agreement. Their labelled disjoint union and subtraction in
CW32 are a canonical ratio family; no false termwise identification of
their Gaussian or nonlinear decompositions is needed.

At real V the literal identity is still
Z_cut=Z_Omega+I_(G minus Omega)+I_(G^c), with the original definitions.
At complex V this unit defines ONLY the white chain CW3. The physical
Z_cut in HC continues its real fine integration with all its selectors
fixed at Vbar. CW3 does not transport those selectors, a rough mean,
a positive rough normalizer or either complement event. After independent
validation, HC39 and CW32 can be composed through the IDENTICAL
Z_a,tr; that algebra does not separately estimate the two histories.

The scalar cube is not the white-ball sector with its separate Ward
identity, nor STEP55's slice/effective input. Selected conditional
derivatives, inherited or future-conditioned histories, effective-class
closure and iteration remain OPEN. Full non-free continuum existence and
a positive physical continuum mass gap remain OPEN. A conditional optical
precision gap is not a physical continuum gap.

The primary antecedents actually inspected here are
[Abdesselam--Rivasseau, hep-th/9409094v1](https://arxiv.org/pdf/hep-th/9409094v1),
the exponential forest statement in section II and its ordered-forest
proof, and [Dimock, 1212.5562v2](https://arxiv.org/pdf/1212.5562v2),
Appendix F's product-measure cluster expansion. The latter assumes
independent fields and bounded small local interactions in a d=3 scalar
setting. Neither source supplies the complex-coarse Yang--Mills reader
bounds or a hard-history theorem. CW25--CW27 rebuild the needed mechanism
from FR's complete proof with the new coefficients. Literature is credit,
not a missing hypothesis.

No numerical science run is part of this unit. Only this source and
checks/complex_white_sector_* are authored. Freeze mathematics before the
minimal manifest/receipt, then request a DIFFERENT fresh hostile review.
No predecessor, shared front, Git, PR, audit or ledger is edited. Root
owns publication; author provenance and same-family review are not an audit.
