# Exact shifted-chart sides and mixed Gaussian boundary prices

This unit applies the product-ball translation identity to the **actual
finite-u critical field** of [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md), using
[BF24](CHART_BOUNDARY_FOREST_ASTRA.md). It keeps
the critical action, determinant, compact normalizer and Haar factors, and
all side/corner chains. It also proves an active-marginal estimate mixing
distinct original nonlinear vertices, bad balls and side chains. Each
nonlinear vertex costs O(sigma); each side costs a polynomial in sigma^-1
times exp(-c/sigma^2), on an explicitly reduced fixed joint data domain.
Independent review is pending.

The estimates are uniform in volume but do not themselves sum a connected
logarithm with the covariance's complete original readers. Critical-field
reader decorations are explicitly expanded and bounded; the remaining
covariance-reader assembly is named in section 8. The original hard cut,
G/Omega, arbitrary histories and the complementary chart integral are not
moved by this argument. Continuum existence and a positive physical continuum
mass gap remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact actual critical-chart translation with every side/corner and uniform mixed Gaussian marginal prices, retaining the unresolved covariance-reader connected assembly."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Actual phase, critical field and uniform constants

Use FU1--FU3: N>=2, D=N^2-1, odd L>=3, T>=2, u>=1, kappa in its fixed
positive compact interval, sigma^2=N/u, n=(3L^4+1)T^4, d=Dn, and every
free scalar colour/root/harmonic coordinate. The pinned tree quotient has
integrated gauge volume and Jacobian one. In U_e(a)=exp(a_e)U0_e(V),

    F_epsilon(a;V)=F_0(a;V)+sum_p epsilon_p W_p(a;V),
    F_0=sigma^2[-log w_0(U(a),V)-sum_e log j_N(a_e)],
    b=b_*(V,epsilon), F_epsilon'(b;V)=0,
    K_*=F_epsilon''(b;V), C=K_*^-1.                       (SC1)

w_0 contains the exact finite-t paired-S4-prime normalized compact kernel,
including its denominator. Haar's j_N is included once; h_N stays outside.
Only original Wilson coefficients vary, while t=kappa u is fixed real.
The lift Hessian underlying FU retains its finite-t spread and Haar
Hessian; the critical Hessian here is its actual FU24 continuation.

The original domain is FU3,
`V_c=exp(v_c)Vbar_c`, `max||v_c||HS<eta`, `|epsilon_p|<rho`, with
real-center curvature <=delta_*. All radii below are fixed before u,T.
Write delta_hat=delta_*+8eta. Its use is essential: delta_V on a real
configuration is not a supremum over this complex product tube.

FU21 supplies connected original-reader scalar atoms b_(i;S), with

    t_b:=2 A_G g_*(1+rho)delta_hat,    V_beta(b)<=t_b,
    beta=(16R)^-4.                                       (SC2)

Each S includes its scalar output's owner and all original coarse/source
readers. The component-root sum is <=t_b; the marked sum over all outputs
whose reader contains a fixed original box is also <=t_b. For a link e set

    r_e=sum_(alpha,S)exp(beta|S|)sup|b_(e alpha;S)|,
    d_v(e)=sum_(alpha,S:v in S)exp(beta|S|)sup|b_(e alpha;S)|,
    r_e<=s_b:=D t_b,                  sum_e d_v(e)<=t_b.  (SC3)

These are scalar l1 sums, not an unproved vector-norm conversion. In
particular ||b_e||HS<=r_e. Suprema are on projected **original-data** domains.
No solved field is made into new independent physical data.

For FU27's whole-component covariance family use the fixed bounds

    alpha=3c0/4, U_bar=c0+d_core+c0/8,
    Re C>=alpha I, ||C||op<=U_bar,
    a_g=alpha/U_bar^2, b_g=1/alpha,
    Re(C[J]^-1)>=a_g I, ||C[J]^-1||op<=b_g                (SC4)

for every principal covariance C[J]. The same bounds apply at the actual
endpoint SC1. The upper bound uses both tail endpoint budgets <=c0/16;
no smallness of their marked sums is asserted. A principal covariance
inherits accretivity and the operator upper bound. If y=C[J]^-1 x,
`Re<x,C[J]^-1 x>=alpha||y||^2` and `||x||<=U_bar||y||`, proving the
precision bound. Its determinant modulus is >=alpha^(D|J|). This argument
needs no Gaussian-return theorem or nonlinear connected expansion.

## 2. Explicit chart and shift margins

Rename FU's local fine polydisc radius a_f and its common vertex bound H_f.
Every local phase vertex and its separate Wilson source vertex, after a
constant subtraction, has the coefficient majorant

    f(t)=H_f(1-t/a_f)^(-q), q=(8L^4+8)D.

There are at most q scalar slots per original vertex, and a scalar coordinate
belongs to at most I=15 distinct original vertices. These are the actual
six Wilson, eight kernel and one Haar incidences from FU3/FU13. The base
Wilson term and its epsilon_p contribution are grouped as ONE original
plaquette vertex; they are not separate members of the Mayer vertex set. Complex
coarse/source continuation remains on the admitted FU tube.

Take rho_max<=1 above the final rho and within the already admitted source
radius. Define constants, independent of u,T,

    c_g=2b_g^2/a_g+b_g, L_g=max(1,sqrt(2exp(1)c_g)),
    choose 0<r_a<a_f/8 such that
    kappa_0:=3(1+rho_max)r_a f'''(2r_a)<=a_g/64,
    C_sh=L_g^2+2kappa_0.                                 (SC5)

These choices exist because f''' is bounded near zero. Reduce FU's data
domain, retaining its positive source radius, until

    s_b<=r_a/8,            C_sh s_b^2<=a_g r_a^2/32.       (SC6)

For an explicit compatible construction, set
`s_0=min(r_a/8,r_a sqrt(a_g/(32C_sh)))`, take FU's critical-field ball
radius tau<=s_0/D in addition to FU18, and then choose its positive
rho,delta_*,eta by FU18--FU19. Those conditions give t_b<=tau/2 and hence
SC6. Equivalently, on an already constructed FU branch, shrink delta_*,eta
until the SC2 bound satisfies SC6. Uniqueness on overlapping tubes identifies
the restricted branch with the same actual b. No delta_hat<=sigma p window
is needed, and none is substituted for the fixed positive complex tube.

Let R_c=r_a/sigma and m_e=b_e/sigma. On a side set H and parameters
0<=t_e<=1 put

    z_e=y_e-t_e m_e for e in H,  z_e=y_e otherwise,
    |y_e|=R_c on H,        |y_e|<=R_c on its bulk chart.    (SC7)

Then the original field is b+sigma z, with each scalar bounded by
r_a+s_b. The absolute Taylor margin at b is bounded by
`max_i|b_i|+max_i|sigma z_i|<=r_a+2s_b<2r_a<a_f`.
This holds along every intermediate product homotopy, not just at its
endpoints. It also holds when only some of the link translations have been
performed. All local logarithms/vertices therefore remain on their existing
analytic branches. Original hard-history or plaquette cut indicators have
not been analytically continued by this statement.

## 3. Exact contour identity, signs and all finite-u factors

Let D_a=product_e B_(r_a) in the original real HS coordinates. Define its
auxiliary-chart analytic integral by the fixed coordinate domain

    Z_a(V,epsilon)=h_N^n integral_(D_a)
                                  exp[-F_epsilon(a;V)/sigma^2] da.

On its real admitted domain the original cut is automatic only when the
previously specified chart-cut margin is satisfied. For complex data this
formula means the analytic chart integral itself, not a definition of a
complex hard predicate. Additional indicators are excluded from its integrand.

Exact Taylor subtraction and actual stationarity give

    R_*(z)=sigma^-2[F_epsilon(b+sigma z)-F_epsilon(b)]
                                      -(1/2)z^T K_*z,
    P_*=h_N^n(2pi sigma^2)^(d/2)det(K_*)^-1/2
                                      exp[-F_epsilon(b)/sigma^2],
    Z_a=P_* integral_(product_e(B_Rc-m_e)) g_C(z)e^-R_*(z) dz. (SC8)

The determinant square root uses the accretive C branch, so
`det(K_*)^-1/2=det(C)^(1/2)` on that same branch. A complex translation
of the real chain has Jacobian one and its translation orientation. SC8
is direct substitution on that chain, with no boundary discarded. The
critical action contains the original compact normalizer and Haar logarithm.

Rebuild the ball identity used in BF24. For a holomorphic F on the sweep,
`d/dt integral_B F(y-tm)dy=-integral_B m.partial F(y-tm)dy`.
The real divergence theorem, applied to each complex component, makes the
right side `-integral_sphere (m.n)F(y-tm)dS`. Integrating t from zero to one
and then tensoring this identity over the n links gives exactly

    Z_a/P_*=sum_(H subset links)(-1)^|H| S_H,
    S_H=integral_[0,1]^H integral_(sphere_Rc^H x B_Rc^(H^c))
                  product_(e in H)(m_e.n_e(y_e))
                                g_C(y-t m_H)e^-R_*(y-t m_H) dS_H dy_Hc dt_H. (SC9)

Every H, including the empty set and every corner, is present. The normal
is the outward real unit normal to the full D-dimensional link sphere; the
dot product is bilinear, and its absolute value is bounded by the scalar
l1 sum used in SC3. Each side retains its own t_e integral and flux. The
parameters only move the coordinates in H.

The scale factors can be checked in original a coordinates: the factor
sigma^d from the affine change, times each side's b_e/sigma and
sigma^(-(D-1)) surface scaling, and each bulk's sigma^-D scaling, is
exactly sigma^(d-Dn)=1. Thus no side Jacobian, power of sigma, h_N or
colour-sphere measure is missing. Source/coarse derivatives of SC9 act on
b, the flux, K_*, critical action and remainder. Stationarity removes only
the total linear Taylor term; it does not freeze any of those readers.

## 4. Local cubic remainders and distinct-vertex incidence

Decompose F_epsilon into its actual local vertices phi_v, including their
original source coefficients. Define

    R_v(z)=sigma^-2[phi_v(b+sigma z)-phi_v(b)
            -sigma phi_v'(b).z-(sigma^2/2)phi_v''(b)[z,z]],
    W_v(z)=exp[-R_v(z)]-1,
    R_*=sum_v R_v,          exp[-R_*]=product_v(1+W_v).    (SC10)

Individual vertices are not stationary. Their linear terms have been
subtracted explicitly; their sum vanishes only by SC1. Their quadratic
terms sum to the full K_*. The product is finite at fixed volume and its
Mayer expansion selects **distinct original vertices**, not repeated copies
of one vertex. Let F(V) be the set of link slots in a selected vertex set V.
Then |F(V)|<=q|V|.

Here are the local bounds needed for the boundary estimate, rebuilt from
FU's coefficient majorant. A degree-j monomial in q_i=sigma z_i, with
|q_i|<=t and j>=k, obeys

    product_i |q_i|^(alpha_i)
         <=t^(j-k) sum_i (alpha_i/j)|q_i|^k, k=2 or 3.

Indeed write r_i=|q_i|/t<=1, apply weighted AM--GM to r_i^k, and use
`(sum_i alpha_i r_i^k/j)^(j/k)<=sum_i alpha_i r_i^k/j`.
For b bounded by s_b, the absolute Taylor coefficient sum at b is bounded
by the coefficients of f(s_b+t). With t=r_a+s_b and s_b+t<2r_a, its
third-order divided remainder is <=f'''(2r_a)/6. Put

    C_3=(1+rho_max)f'''(2r_a)/6.

On every selected vertex's chart slots, these bounds give

    |R_v(z)|<=sigma C_3 sum_(i in slots(v))|z_i|^3,
    sum_(v in V)|R_v(z)|<=kappa_0 sum_(i in F(V))|z_i|^2. (SC11)

For the second line, the bound is initially
`I(r_a+s_b)C_3<=15(9r_a/8)C_3<=kappa_0`. The finite incidence I applies
because V is a set of distinct original vertices. These bounds also hold
for absolute Taylor sums after inserting the critical-field atoms with
weight exp(beta|S|): replace each scalar b by its component atom norm,
which is <=s_b. Each root label and every attached reader is retained.
The normalizer and Haar vertices obey the same local count and are not
removed from V.

For any complex numbers R_v,

    product_(v in V)|e^-R_v-1|
         <=product_(v in V)|R_v| exp[sum_(v in V)|R_v|].   (SC12)

This follows by integrating each exponential along its straight scalar
segment. It is valid without a sign or positivity assumption.

## 5. Exact mixed active marginals, with every remaining cut

In a term of SC9, expand the finite product in SC10. For a selected V,
retain the ball cut on every link of F(V) outside H. Only for the remaining
links outside H union F(V) write `1_B=1-1_outside` and expand. Thus

    Z_a/P_*=sum_V sum_H sum_(A subset links\(H union F(V)))
                          (-1)^(|H|+|A|) I_(V,A,H).      (SC13)

Let J=F(V) union A union H. Its coordinates have balls on F(V)\H,
spheres on H and exteriors on A. The term is exactly

    I_(V,A,H)=integral_[0,1]^H integral_(B_Rc^(F(V)\H)
                                  x sphere_Rc^H x outside_Rc^A)
       product_(e in H)(m_e.n_e)
       product_(v in V)W_v(y-t m_H)
                      g_(C[J])(y-t m_H) dy_bulk dS_H dy_A dt_H. (SC14)

The original covariance marginal C[J] is used; it is not K_*[J]^-1.
All inactive coordinates were integrated over their whole real spaces.
Only the Gaussian depends on those coordinates, and its translation is
supported in H subset J. Integrating them therefore gives precisely the
normalized Gaussian marginal in SC14. Real positive covariance proves the
identity by completing a square. Analytic continuation on the accretive
complex domain proves it there, with local Gaussian domination. It stays
valid for complex active means because the Gaussian is entire and decays
on the real inactive coordinates.

The condition A disjoint from F(V) is crucial. Every nonlinear vertex is
only evaluated on its bounded chart slots, where SC7 and SC11 apply.
No local Taylor series has been extended to a bad-ball exterior. If
V=A=H=empty the integral is exactly one, with no unused-mode determinant
or residual vacuum factor. Inactive coarse/source data can still be read
by C[J] or b; marginalization is not a locality assertion about that data.
Each term is holomorphic on the reduced joint domain, by its fixed active
chains and uniform Gaussian domination, with that full dependence retained.

## 6. Mixed all-order bound and explicit rare side prices

We prove a stronger version that also sums the critical-field decorations
at fixed covariance argument. The meaning and remaining reader limit of
that coefficient norm are stated in section 7. First derive the Gaussian
estimate used in it. From SC4, for every scalar multiindex nu,

    |partial^nu g_(C[J])(y)|
       <=(b_g/(2pi))^(D|J|/2) exp[-a_g||y||^2/4]
                                       L_g^|nu|sqrt(nu!). (SC15)

Indeed Young's inequality bounds the Gaussian at y+z by the displayed
normalizer times exp[-a_g||y||^2/4+c_g||z||^2]. Cauchy's circle for an
order-k scalar derivative has radius sqrt(k/(2c_g)). The inequality
k!<=k^k leaves the square-root factorial. The Gaussian is entire, so this
field radius may grow with k; the original-data analytic radii do not grow.
This repeats the proved Gaussian part of BF6, with the actual SC4 precision.

Expand g_(C[J])(y-tm_H) in every scalar component of m_H. If the absolute
weighted scalar amplitudes are s_i, then sum_i s_i<=s_b/sigma per boundary
link. For S(t)=sum_(k>=0)t^k/sqrt(k!), Cauchy--Schwarz gives

    S(t)<=sqrt(2)exp(t^2),
    S'(t)<=sqrt(2)sqrt(1+2t^2)exp(t^2).                  (SC16)

For the first inequality insert 2^(-k/2) and sum the exponential series;
for the second its squared series is `(1+2t^2)exp(2t^2)`.
Consequently the absolute shift series for the Gaussian has bound

    (b_g/(2pi))^(D|J|/2) 2^(D|H|/2)
       exp[-a_g||y||^2/4+L_g^2(s_b/sigma)^2|H|].          (SC17)

This is supported only on H. No force price over all d coordinates has
been introduced.

For the vertex factors in SC14, expand the critical-field substitutions
and the Mayer exponentials absolutely. By SC11--SC12 their majorant is
bounded by a product of cubic sums times
`exp[2kappa_0||y||^2+2kappa_0(s_b/sigma)^2|H|]`.
Each root reader label can be paid once per selected original vertex;
repeated powers in its exponential do not require repeated copies of that
fixed root reader. All attached field-atom readers remain in the sums.

Expand the cubic sum for each v into its <=q scalar choices. Since no
scalar belongs to more than I distinct selected vertices, its resulting
power is 3j with j<=I. The repeated powers inside a single Mayer
exponential were absorbed in the stability factor; only one cubic factor
per selected original vertex is extracted. On a boundary link,
`|y_i-t_i m_i|<=|y_i|+s_b/sigma`; elsewhere no shift occurs. Thus all
shift-polynomial costs on H are bounded by
`(1+s_b/sigma)^(3DI|H|)` times products of (1+|y_i|)^(3j).
A finite explicit moment constant is

    M=8 max{1,(48I/a_g)^(3/2)}.

For 1<=j<=I, `(1+t)^(3j)<=M^j exp(a_g t^2/32)`: use
1+t<=2max(1,t) and maximize t^(3j)exp(-a_g t^2/32).
The product of these bounds costs M^|V| and uses at most
exp(a_g||y||^2/32). Combining it with SC17, 2kappa_0<=a_g/32 and the
Mayer majorant leaves Gaussian decay at least exp[-3a_g||y||^2/16].
We retain the weaker exp[-a_g||y||^2/8].

Reserve exp(-a_g R_c^2/16) for each A or H link, and integrate the remaining
exp(-a_g|y_e|^2/16) on bulk or exterior coordinates. A boundary sphere
keeps its exact area omega_D R_c^(D-1), omega_D=area(S^(D-1)). The full
shift-exponential cost is <=exp[a_g R_c^2|H|/32] by SC6. Define

    Z_g=(8b_g/a_g)^(D/2),
    nu_v=exp(beta s_v) sigma C_3 q M max(1,Z_g)^q,
    q_bad=exp(beta) Z_g exp[-a_g R_c^2/16],
    Q_surf=exp(beta) 2^(D/2)(b_g/(2pi))^(D/2)
                    omega_D R_c^(D-1) exp[-a_g R_c^2/32],
    q_side=Q_surf(s_b/sigma)(1+s_b/sigma)^(3DI),
    s_v=9^4.                                             (SC18)

The factor Z_g for F(V)\H is charged at most q times per original vertex.
The harmless exp(beta) factors pay an owner box for each bad or side link;
exp(beta s_v) pays each original vertex's radius-four reader. Omitting
all reader weights only decreases the bound. We obtain

    |I_(V,A,H)|<=nu_v^|V| q_bad^|A| q_side^|H|.           (SC19)

More precisely SC19 also bounds the weighted absolute sum of its vertex
and critical-field decorations, with covariance C[J] regarded as the
remaining analytic argument, as defined next. The vertex cost is O(sigma).
Both bad and side prices tend to zero faster than any fixed power of sigma.
In particular the flux, surface-area and degree-45D polynomial costs do
not defeat the exp[-a_g r_a^2/(32sigma^2)] side price.

Let M_V be the number of original vertices in the finite volume. Taking
absolute values and dropping the constraints in SC13 gives the explicit
summable bound

    sum_(V,H,A admissible) |I_(V,A,H)|
       <=(1+nu_v)^(M_V)(1+q_bad+q_side)^n.                (SC20)

For terms with at least one side, the bound is the same vertex factor
times `[(1+q_bad+q_side)^n-(1+q_bad)^n]`. These are exponential-volume
upper bounds with rare price per specified side; they are not a uniform
relative error or a nonvanishing theorem. Connected summation is still
needed before taking a logarithm or dividing by an interacting reference.

## 7. Critical-field reader expansion and a boundary-mark estimate

Here is the precise reader content of the stronger statement following
SC19. Keep C[J] as an explicit matrix argument satisfying SC4 while doing
this algebra. Expand each local phi_v at zero, substitute the actual
connected FU atoms for every occurrence of b, form the cubic remainder
and Mayer series, and expand the Gaussian translation and each flux.
Copies of b appearing as a center or as a translation are expanded
separately and then identified with the same solved function. Cauchy
majorants are applied before that identification, which only overcounts
the positive bound. The original Wilson source and each local coarse-data
coefficient keep their root label.

A decoration has the following partial original reader, with C[J] still
displayed as a separate analytic argument:

    S_dec=owners(A union H) union union_(v in V)S_v
                      union_(all selected critical-field occurrences)S. (SC21)

Every attached field atom meets its output's vertex root or boundary owner.
Labels are never replaced by their field endpoints. Since
`|union S|<=sum|S|`, its exponential reader weight is dominated by the
root/owner factors in SC18 and the individual atom weights from SC3.
The local Taylor coefficient majorant is f(s_b+t), and the Gaussian series
is controlled by SC15--SC17. The moment proof of SC19 is therefore also
an absolute convergence proof for these decorations on their projected
original-data domains. The covariance argument has deliberately not been
included in the partial reader weight SC21; its actual composition is
discussed below, rather than called local by omission.

For a sharp boundary-rooted check take V=empty. Define s=s_b/sigma and

    K_s=1+L_g s(1+sqrt(2)L_g s).

For H nonempty, mark one critical-field occurrence whose original reader
contains a specified box v. Differentiating the positive shift series
SC16 marks a scalar Taylor occurrence; marking a flux selects one of its
linear atoms. The sum of both possibilities is bounded by

    q_bad^|A| Q_surf^|H| (s^(|H|-1)/sigma) K_s
                                  sum_(e in H)d_v(e).    (SC22)

The unmarked pure Gaussian bound is `q_bad^|A|(Q_surf s)^|H|`.
To see the coefficient in SC22, a flux mark costs d_v(e)/sigma and removes
one unmarked factor s. A translation mark costs
`(d_v(e)/sigma)L_g(1+sqrt(2)L_g s)` while all flux factors remain.
The other scalar series have the same Gaussian envelope. No additional
exponential is needed. Repeated reader occurrences are counted separately,
so a union-reader indicator is bounded by this marked count.

For one side, summing its boundary link e pays
`sum_e d_v(e)<=t_b`; its marked price is therefore at most
`q_bad^|A| Q_surf (t_b/sigma)K_s`, uniformly in volume and the covariance
argument. This proves that an arbitrarily remote critical-field reader
can be charged at a boundary anchor with a finite marked cost. All those
polynomial sigma^-1 factors are still paid by Q_surf's Gaussian tail.
If t_b=0 then every side flux vanishes identically; SC22 is interpreted
through its polynomial expression, with 0^0=1 only for the single-side
factor, and no division by t_b or s_b. The original covariance dependence
has not been marked by this estimate.

Local vertex coefficients have the same explicit reader mechanism: a mark
at the root costs its fixed S_v, while a mark in b is counted by one
coefficient derivative of f(s_b+t). Those derivatives are finite on the
strict SC7 margin. We do not promote that observation to a summed mixed
full-reader theorem; SC19 proves the absolute decoration bound and SC22
proves the stated pure-boundary marked bound.

## 8. What remains after these estimates

At the actual endpoint C[J] is a solved original-data function as well.
FU27 gives its complete-reader atoms, including the diagonal atoms reading
remote data. The coefficient functions in the expansion of section 7 read
those atoms through C[J] and its inverse/determinant. Their complete reader
is SC21 together with **every covariance reader used by an eventual
covariance expansion**. Merely assigning them SC21 would be false locality.
One may keep their full original covariance dependence unexpanded, but the
resulting support can be the whole finite volume and does not satisfy a
claimed volume-uniform exponential reader norm.

The unresolved assembly is consequently precise. On a common original
source/coarse domain, one must expand or interpolate those covariance
readers, retain their complete supports and marked budgets, combine them
with SC19's distinct vertices/bad balls/sides and SC22's boundary pins,
and prove an absolutely summable connected activity criterion with margins
strictly below FU's beta. The covariance determinant normalization must
remain the one of SC14. Normalizing by a different interacting law or
moving the original hard histories would not be that missing step.

The author's separate READER_LOCAL_GAUSSIAN_RETURN unit and the other
worker's nonlinear unit are not premises of this note. A future composition
must match their independently reviewed covariance families, domains,
precision constants and support rates; it is not supplied by their names.
Stationarity alone provides none of this reader summation.

What is proved here is the exact actual-chart decomposition SC8--SC14,
the homotopy margin SC5--SC7, the uniform mixed estimate SC19 with its
finite-volume absolute summation SC20, and the explicit critical-field
reader convergence/marked boundary estimate SC21--SC22. The full prefactor
P_* is never bounded away, canceled or replaced. It may be extensive. The
same is true of the original critical action and its source dependence.

If an auxiliary chart has been chosen inside the original cut/good-event
window, SC9 handles that chart integral only. Its exterior, the original
G/Omega interfaces, any unchanged plaquette/history indicator and every
extra retained reader remain separate exact terms. No complex deformation
of those nonholomorphic indicators is asserted. Effective-level iteration,
four-dimensional continuum existence and a positive physical continuum
mass gap remain further obligations.

The product divergence identity is the already reviewed BF24, rebuilt here
with the actual FU critical field and exact scaling. The needed Gaussian
jet and single-link sphere arguments are likewise reconstructed at SC4's
precision. No external theorem import or numerical experiment is needed.
Bałaban's constructions and Dimock's expositions remain the constructive
antecedents. The limited producer reads and unchanged identities are bound
by the [read manifest](checks/shifted_chart_return_read_manifest.json) and
[author receipt](checks/shifted_chart_return_receipt.json). The mathematical
source is frozen before that compact package and a fresh hostile review.
Root owns Git, PR #10114 integration, shared fronts and all audit operations.
