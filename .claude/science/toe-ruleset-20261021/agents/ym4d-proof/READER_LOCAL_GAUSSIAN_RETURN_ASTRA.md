# A complete-reader logarithm for the centered Gaussian chart cutoff

This unit sums the **centered, exactly normalized Gaussian cutoff** for the
actual lift covariance of [PC](POSITIVE_READER_COVARIANCE_ASTRA.md), including
its infinite complete-reader residual. A larger fixed patch radius makes
that residual small in a row algebra whose constants do not grow with the
patch radius. A marginal determinant/inverse expansion, followed by a
regrouping of overlapping readers, gives a connected logarithm at an explicit
positive original-block rate. Independent review is pending.

The Gaussian reference has zero mean here. The actual finite-u phase has
nonzero force and nonlinear terms; neither is set to zero in the actual
model. This result concerns one factor that would be needed in that larger
return problem. It does not establish the interacting return, arbitrary
histories, effective-level iteration, continuum existence, or a positive
physical continuum mass gap. Both physical targets remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Complete-reader connected logarithm and complex nonvanishing for the centered normalized Gaussian link-ball cutoff of the actual lift covariance."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Exact object and producer input

Fix PC's N>=2, D=N^2-1, odd L>=3, kappa in its fixed positive interval,
u>=1, and T>=2. There are m0=3L^4+1 free links per original coarse box,
n0=Dm0 scalar coordinates, and Lambda=(Z/TZ)^4. The covariance is

    C(V)=K(V)^-1,   K(V)=F_0''(0;V),   sigma^2=N/u,
    J_0(V)=integral product_e 1_{|x_e|<=R_c} g_C(x) dx,
    R_c=r_a/sigma,     g_C=(2pi)^(-d/2)det(C)^(-1/2)
                                      exp[-x^T C^-1 x/2].  (RG1)

Here |x_e| is the D-dimensional HS norm, d=n0 T^4, and 0<r_a<a0/2 is a fixed
auxiliary chart radius, using PC's fine analytic radius a0. The square root uses the matrix logarithm on the
right half-plane. PC1--PC4 use the actual Wilson action, normalized paired
S4-prime kernel at finite t=kappa u, and Haar factor exactly once. In
particular their K retains the finite-t spread and N^2/(6u) Haar Hessian;
all colours, roots, crossings and harmonic directions remain. This note
uses that K, not a different flat or zero-mode-removed precision.

The real centers satisfy PC's delta_Vbar<=delta0. All suprema below include
the common complex coarse tube max_c||v_c||HS<rho_PC, with
V_c=exp(v_c)Vbar_c, and all admitted real centers, u,T. Negative complex
edges use inverse, not conjugation. When a coefficient has reader S, its
supremum is on the projected tube of the actual coarse data in S. PC's
completion argument makes it independent of values outside S. We neither
increase rho_PC nor use the separately proposed critical-field covariance.

The input rebuilt in PC6--PC22 is the exact decomposition

    C=P+E,       P=sum_A chi_A G_A chi_A,
    G_A=(K restricted to patch A)^-1,
    E=sum_a E_a,       sum_A chi_A(i)^2=1, chi_A>=0.        (RG2)

Each patch covariance has a connected complete reader S_A, |S_A|<=s_R,
s_R=(16R)^4, with at most J=16^4 patch readers through a box. R>=4 is
fixed before u,T and will be increased in section 3. Both endpoints of
each symmetric E_a belong to its connected complete reader S_a. Repeated
paths/labels in PC remain separate atoms. For beta=1/s_R,

    eps=M_beta(E)<=p r/(1-r),
    B_E=B_beta(E)<=n_R p[r/(1-r)+r/(1-r)^2],
    p=exp(1)Jg, r=exp(1)C_R/R, n_R=n0 s_R.               (RG3)

M is the maximum row/column sum of exp(beta|S_a|)sup|E_a(i,j)|;
B is the supremum over a marked original box v of the sum over all i,j,a
with v in S_a. PC gives g,C_R,c0>0 independent of R,u,T. B_E is finite
and can be large. It is not assumed small. These are sums of entrywise
suprema, not suprema of operator norms. The whole-torus small-volume patch
when T<16R is included; its residual is exactly zero.

No interacting tail theorem, original-cut estimate, or proposed critical
covariance is an input. PC's reviewed status does not replace the matrix
estimates used below. The needed PC input was read in full; the analytic
steps newly needed here are proved explicitly.

## 2. The row algebra does not lose powers of the patch radius

PC6 gives, with the periodic owner distance d_1 and fixed m>0,

    sup|G_A(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)].

Cauchy--Schwarz in the fixed cutoff labels gives
`sum_A chi_A(i)chi_A(j)<=1`. Therefore

    sup|P(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)],
    max(row,col)sum sup|P(i,j)|<=g,
    Re P>=c0 I,                 ||P||op<=g.              (RG4)

For the last lower bound, at real Vbar every G_A>=2c0 I_A, so P>=2c0 I
by the partition of unity. PC21--PC22 cost less than c0/8 on the complex
tube. We use the weaker c0. The entry sum in RG4 is at most PC's
`g=(2n0/gamma)coth(m/4)^4`. In particular it is independent of R.

The same estimates hold for a principal matrix P[X] on any set X of
whole links, followed by any positive Gram mask s on those links with
0<=s_ef<=1 and s_ee=1. Write P[X,s]_(e alpha,f eta)=s_ef P_(e alpha,f eta).
If s_ef=<v_e,v_f>, the isometry W(e alpha)=e alpha tensor v_e gives
`P[X,s]=W*(P[X] tensor I)W`. Thus its Hermitian part is >=c0 I and its
norm is <=g. This includes every forest path-minimum mask used later: such a mask is the
integral, over threshold t in [0,1], of the block all-ones matrices on
components of the forest edges with values >=t. Each integrand is positive
semidefinite with diagonal one.

To control its inverse entrywise, define the finite geometric constant

    A_1=(2n0/gamma) sum_(z in Z^4) |z|_1 exp[-m|z|_1/2],
    theta=min(m/2,c0/(2A_1)),
    v_0=(2n0/c0)coth(theta/2)^4.                           (RG5)

The series for A_1 is a product of four geometric series with one
differentiated factor; explicitly its sum before 2n0/gamma is
`8 exp(-m/2)(1-exp(-m/2))^-2 coth(m/4)^3`. All constants are positive
and independent of R. Fix a column j and conjugate P[X,s] by
exp(theta d_1(X_i,X_j)). The absolute row and column changes are at most

    (2n0/gamma) sum_z exp(-m|z|_1)(exp(theta|z|_1)-1)
       <=theta A_1<=c0/2.

Here `exp(theta t)-1<=theta t exp(theta t)` and theta<=m/2. Torus distance
representatives form a subset of Z^4; a compression or mask can only
decrease this bound. The operator norm of the change is at most its
geometric mean row/column bound, by weighted Cauchy--Schwarz. The conjugated
matrix has Hermitian part >=c0/2, hence inverse norm <=2/c0. Undoing the
weight proves, for G_X,s=P[X,s]^-1,

    sup|G_X,s(i,j)|<=(2/c0)exp[-theta d_1(X_i,X_j)],
    max(row,col)sum_j sup|G_X,s(i,j)|<=v_0.                (RG6)

This proof applies to arbitrary principal failed-link sets, including
highly disconnected ones, and to all the masks. It does not assume that
the principal inverse is finite-range. Its reader is the fixed union of
the component readers; that reader will be paid once, not per G factor.

For later Gaussian bounds set

    a=c0/g^2,       b=1/c0.
    Re G_X,s>=a I,  ||G_X,s||op<=b.                       (RG7)

Indeed for y=P[X,s]^-1 x, `Re<x,G_X,s x>=c0||y||^2` and
`||x||<=g||y||`. This precision lower bound is rederived for this reference;
PS's original gamma is not substituted for it.

## 3. A fixed larger R, with its reduced support rate retained

Reapply PC's fixed geometric cover with one R large enough that

    r<=min(1/4,c0/(32p),1/(4p v_0),a/(64p v_0^2)).        (RG8)

This is possible because p,C_R,a,v_0 were fixed independently of R.
PC's coarse tube can stay rho_PC: its radius bound contains J,g,J_abs,c0,
not R. By eps<=2pr, RG8 gives

    tau=v_0 eps<=1/2,
    t_0=v_0^2 eps/(1-tau)<=a/16,
    ell_0=-(1/2)log(1-tau).                              (RG9)

We retain the new `beta=(16R)^-4`. It is not held at an old value when R
is increased. All constants involving R, including B_E, are chosen before
taking u large. The precision a in RG7 and these bounds are uniform in u.

Give each link e the fixed connected collar

    H_e=union_(A:chi_A(e)!=0) S_A,       H_X=union_(e in X)H_e.

Every S_A in this union contains e's owner, so H_e is connected and
|H_e|<=h:=J s_R. The cover geometry in PC8--PC10 puts H_e within coarse
sup distance 8R of that owner. A safe incidence bound is

    sup_v #{e:v in H_e}<=J_H:=m0(32R+1)^4.                (RG10)

The small-torus patch obeys the same bound. The entries P_ef read only
H_e union H_f and vanish when those collars are disjoint. G_X,s and its
determinant read H_X; no inverse factor is assigned another copy of H_X.
If X has several collar-overlap components, P[X,s] and G_X,s split over
them. Keeping all of H_X once is a permissible larger reader.

## 4. Only normalized marginal densities are expanded

Set eta_e(x_e)=1_{|x_e|>R_c}. Exact marginalization of the normalized
Gaussian gives

    J_0=sum_(X subset links)(-1)^|X| F_X,
    F_X=integral product_(e in X)eta_e g_(C[X]), F_empty=1. (RG11)

C[X] is the principal covariance, not the inverse of the principal
precision K[X]. For real positive C the identity is the Schur-complement
Gaussian integral. For complex symmetric accretive C it follows by
holomorphic continuation of that identity, with local Gaussian domination.
The determinant branches match at positive real matrices. PC supplies
this domain; RG8 also keeps P[X,s]+E[X,s] accretive by the row bound eps.

Fix nonempty X, its mask s, and write G=G_X,s, E_s=E[X,s], y=x+z. The
exact density ratio has the convergent expansion

    g_(P[X,s]+E_s)(y)=g_(P[X,s])(y) exp L_X(y),
    L_X(y)=sum_(k>=1) (-1)^k Tr[(G E_s)^k]/(2k)
         +(1/2)sum_(k>=1)(-1)^(k-1)y^T(G E_s)^k G y.      (RG12)

The first sum is the full determinant ratio. The second is the full inverse
correction. This follows by expanding log(I+GE_s) and (I+GE_s)^-1, since
||GE_s||op<=tau<1. The determinant identity is fixed along the segment
P[X,s]+zeta E_s from zeta=0; both sides are nonzero and agree there.

Expand each E_s into its actual labelled atoms and every matrix product
into all scalar indices. Call an individual term in the first sum a loop
and one in the second a chain. Expand the exponential as an ordered list
of such terms with its exact 1/k! for list length k. Repeated indices,
colours, atoms and loops are retained. Let omega denote one such finite list,
and f_omega(y) its contribution including g_(P[X,s])(y). The empty list is
included. This is a countable expansion, with no cancellation used in
its norm. Its complete reader lies in

    H_X union union_(atom occurrences a in omega) S_a.        (RG13)

Only H_X once is required, although a long loop has many G factors. Each
residual occurrence has both scalar endpoints in X. At X=empty there
are no loops, chains, fields or determinant ratio: the normalized marginal
is precisely one. There is no residual vacuum species to exponentiate.

Write w(omega)=exp[beta sum_(occurrences a in omega)|S_a|]. With d_X=D|X|, the
absolute row algebra and `|y_i y_j|<=(|y_i|^2+|y_j|^2)/2` give

    sum_(loops) weighted absolute value <=d_X ell_0,
    sum_(chains) weighted absolute value <=t_0||y||^2/2.

Thus the full exponential list sum is bounded by
exp(d_X ell_0+t_0||y||^2/2). These estimates use RG6 for sums of suprema
of inverse entries, and RG3 for sums of suprema of individual atoms.
They cover finite atom truncations uniformly and then their absolute limit.

For the unperturbed Gaussian, the least singular value of P[X,s] is
>=c0, so its determinant modulus is >=c0^d_X. RG7 and Young's inequality imply

    |g_P(x+z)| <=(b/(2pi))^(d_X/2)
       exp[-a||x||^2/4+c_g||z||^2], c_g=2b^2/a+b.

Since ||x+z||^2<=2||x||^2+2||z||^2 and t_0<=a/16, we have

    sum_omega w(omega) sup|f_omega(x+z)|
      <=(b/(2pi))^(d_X/2)exp[d_X ell_0]
          exp[-3a||x||^2/16+(c_g+t_0)||z||^2].            (RG14)

Sup here includes the projected coarse domain and all forest masks. It
retains the determinant at dimension d_X. No factor from unused modes
survives marginalization.

## 5. A marked reader bound and all orders of link-ball traces

For an original box v define the nonnegative scalar envelope

    d_v(i)=sum_(j,a:v in S_a) exp(beta|S_a|)sup|E_a(i,j)|,
    D_v(X)=sum_(i owned by links in X)d_v(i).
    sum_i d_v(i)<=B_E.                                   (RG15)

Let n_v(omega) count residual occurrences in omega whose reader contains v,
including repetitions. The indicator that any residual reader contains v
is <=n_v(omega). Differentiating the positive exponential majorant with one
marked atom gives loop and chain factors bounded by

    D_v(X)[A_0+A_2||y||^2],
    A_0=v_0/[2(1-tau)], A_2=v_0^2/[2(1-tau)^2].          (RG16)

For loops, the k possible marked positions cancel 1/k and leave a
geometric resolvent with row bound v_0/(1-tau). Its trace against the
marked entry envelope is at most that bound times D_v(X). For chains,
mark one of k residual factors. The two remaining geometric sides cost
v_0^2/(1-tau)^2. The operator norm of the marked nonnegative matrix is
at most its total entry sum, <=D_v(X), which bounds its quadratic form
by D_v(X)||y||^2. This argument also covers diagonal remote-reader atoms.

Multiplying RG14 by RG16 and absorbing the polynomial using
`u exp(-a u/16)<=16/a`, `u exp(-u)<=1` gives, with

    c_*=c_g+t_0+1,
    K_m=A_0+2A_2(16/a+1),
    L_*=max(1,sqrt(2 exp(1)c_*)),

both of the bounds

    sum_omega w(omega) sup|f_omega(x+z)|
      <=A_X exp[-a||x||^2/8+c_*||z||^2],
    sum_omega n_v(omega)w(omega) sup|f_omega(x+z)|
      <=K_m D_v(X) A_X exp[-a||x||^2/8+c_*||z||^2],
    A_X=(b/(2pi))^(D|X|/2)exp[D|X|ell_0].               (RG17)

These are absolute coefficient bounds, not just a bound on their sum.
For any scalar multiindex nu, apply Cauchy to each entire f_omega with radius
sqrt(nu_i/(2c_*)) when nu_i>0. Since nu_i!<=nu_i^(nu_i), the resulting
factor is <=L_*^|nu|sqrt(nu!). Tonelli on the positive majorant permits
summing omega before the contour integrals. In RG17 the same two right sides
at z=0 therefore bound the corresponding derivative sums, multiplied by
L_*^|nu|sqrt(nu!). The factor K_m D_v(X) is unchanged.

For clarity, the required hard-ball integration is also rebuilt. Give link
e an ordered list of k_e scalar derivatives; B={e:k_e>0}, r=sum_e k_e.
Keep its first leg j_e and let nu be all the remaining legs. Distributional
integration by parts gives exactly

    <product_e partial^(k_e)eta_e, f_omega>
      =(-1)^(r-|B|) integral_(sphere_Rc^B x outside_Rc^(X\B))
                product_(e in B)n_(e,j_e) partial^nu f_omega.  (RG18)

Here partial_j eta_e=n_j dS. Subsequent derivatives are moved onto f_omega;
no other link cutoff depends on those coordinates. Thus every corner
product of spheres remains, and all higher normal distributions act as
RG18 states. Gaussian decay supplies the limiting compact test functions.
No cutoff is analytically continued or smoothed away.

Let omega_D=area(S^(D-1)) and set

    q=(b/(2pi))^(D/2)exp[D ell_0-a R_c^2/16]
          max{omega_D R_c^(D-1),(16pi/a)^(D/2)}.          (RG19)

Reserve exp(-a R_c^2/16) from each exterior or sphere; integrate the
remaining exp(-a|x_e|^2/16) or bound the exact surface area. Equations
RG17--RG18 then give, at EVERY derivative order,

    sum_omega w(omega) sup|<product_e partial^(k_e)eta_e,f_omega>|
      <=q^|X| L_*^r product_(e in B)sqrt((k_e-1)!),

    sum_omega n_v(omega)w(omega) sup|<product_e partial^(k_e)eta_e,f_omega>|
      <=K_m D_v(X) q^|X| L_*^r
                                  product_(e in B)sqrt((k_e-1)!). (RG20)

Scalar factorials were bounded by the factorial of the total remaining
legs at that link. No dimension, force, or determinant cost was discarded.
The force is absent because the object RG1 is centered; the determinant
cost is explicitly in q. Fixed r_a>0 gives q->0 as u->infinity uniformly
in T and admitted V, since R_c^2=r_a^2 u/N.

## 6. Endpoint forests with all covariance readers attached afterwards

First use independent endpoint-pair mask coordinates on the marginal
C[X]. At a forest mask the full covariance is accretive: the same Gram
isometry proves it, or use P[X,s] and the residual norm eps. Its normalized
Gaussian factors over disconnected forest components. Differentiation in
one independent pair gives the exact heat identity

    partial_(s_ef) F_X(s)=sum_(alpha,eta) C_(e alpha,f eta)
         <partial_(e alpha)partial_(f eta)product_g eta_g,
                                                   g_(C[X,s])>. (RG21)

Indeed differentiating the density in a symmetric direction dot C gives
`g_C[x^T C^-1(dot C)C^-1 x-Tr(C^-1 dot C)]/2`, which is
`(dot C):partial_x^2 g_C/2`. Integrate by parts in the weak sense.
The two symmetric ordered entries cancel this 1/2. Its normalizer has
therefore been differentiated as well. A list of distinct pair derivatives
therefore gives a product of those constant covariance entries and the
corresponding weak field derivatives.

For a tree T on X define the usual path-minimum mask s^T. Forest algebra
and RG11 yield the exact endpoint gas with activity

    a_X=(-1)^|X| sum_(T tree on X) integral_[0,1]^T
                              partial_T F_X(s^T) dt.      (RG22)

For one link the tree is empty. This is an independent-pair derivative
followed by evaluation, not a derivative of a minimum map. There is no
replacement of PC29 by a single covariance pair and no omitted reader
monomial chain rule: complete-reader interpolation is not used here.

One proof of the finite forest identity is to check monomials in pair
variables. Give each present edge with exponent m an independent clock
with distribution function t^m. Its maximum spanning forest is unique
almost surely. Given its tree clocks, every other clock is below the
minimum on its forest path; its probability gives the remaining monomial,
while the tree densities give the derivatives. Sum the disjoint events.
Polynomial approximation with the required finite derivatives proves the
smooth formula. If needed, extend the function smoothly from the open
accretive neighborhood of the compact forest-mask locus to the cube;
only its original jets on that locus enter. Factorization there gives
RG22 and the gas on disjoint field sets X. This proof uses no nonpositive
Gaussian integral outside that locus.

In each term of RG22, expand each tree entry as P_ij+sum_a E_a(i,j),
and expand the remaining normalized density by RG12. Keep tree colours,
chosen tree atoms, and the ordered loop/chain list omega as separate species
z. Integrate the tree parameters as part of its activity a_z. Its field
set is X_z=X and its complete support is

    S_z=H_X union union_(tree residual atoms a)S_a
                        union union_(density occurrences a in omega)S_a. (RG23)

S_z is connected. A nonzero P tree entry requires H_e and H_f to meet;
a residual tree entry has a connected reader containing both owners.
The tree therefore connects all H_e. Each extra density occurrence has
an endpoint in X, so its whole connected reader attaches to that union.
This includes diagonal atoms with remote data. Both H_X and every new
residual reader are paid. No collar is charged separately at each inverse
factor. Each a_z is holomorphic and reads only S_z by the locally uniform
absolute expansion and fixed-domain integration. All formulae agree on
projected tube overlaps, as their unexpanded entries do.

Species are initially incompatible when their **field sets** intersect.
It would be incorrect simply to replace this by reader intersection.
Section 8 performs the required exact regrouping instead.

## 7. Summing every complete-reader species through a marked box

Use the nonnegative endpoint weights

    c_ef=sum_(alpha,eta)[sup|P_(e alpha,f eta)|
             +sum_a exp(beta|S_a|)sup|E_a(e alpha,f eta)|],
    c_row=sup_e sum_(f!=e)c_ef<=D(g+eps),
    Q=exp(beta h)q,       lambda=4L_*^2 c_row Q.          (RG24)

The determinant coefficient bounds RG20 and the n-vertex tree's 2n-2
legs give the absolute activity bound with factor
`Q^n L_*^(2n-2) product_(ef in T)c_ef product_e sqrt((deg_T(e)-1)!)`.
The factor exp(beta h n) pays H_X once. Residual support weights multiply
per occurrence and dominate the exponential of their union's cardinality.

The tree counting used in the sum is explicit. For n>=2, Prüfer codes
have occurrence numbers k_e=deg(e)-1 summing to n-2, so

    sum_(labelled trees T) product_e(deg_T(e)-1)!
                 =(n-2)! binomial(2n-3,n-1).

The square-root factorials are smaller. With one field link fixed,
remove leaves to sum all other positions at cost c_row^(n-1), and divide
by (n-1)! for their ordering. Dropping distinctness only enlarges this
positive sum. Since the binomial is <=4^(n-1), the sum through that fixed
link is <=Q/(1-lambda), provided lambda<1.

There are exactly three possible ways a marked original box v belongs
to S_z; union bounds suffice. If it lies in H_X, anchor a field link with
v in H_e and pay J_H. If it lies in a density residual reader, use the
second RG20 and sum its pinned weight D_v(X); RG15 gives total pin mass
<=B_E. These contributions are bounded by

    (J_H+K_m B_E)Q/(1-lambda).

For a marked tree residual entry, let c^v_ef be its colour sum restricted
to atoms with v in S_a. Then sum_(e,f)c^v_ef<=B_E. Remove that tree edge;
summing positions in the two resulting trees costs
`B_E c_row^(n-2)`. There are n-1 possible distinguished edges. Dividing
by n! for the vertex ordering and using the Prüfer identity gives a
coefficient `binomial(2n-3,n-1)/n<=4^(n-1)`. Summing n>=2 bounds this
third contribution by `4 B_E L_*^2 Q^2/(1-lambda)`. Hence

    sup_v sum_(z:v in S_z) exp(beta|S_z|) sup|a_z|
       <=epsilon_G:=Q[J_H+K_m B_E+4B_E L_*^2 Q]/(1-lambda). (RG25)

No smallness of B_E was required. It is a fixed finite multiplier of the
Gaussian bad-link price. Every colour in these estimates is explicit:
the D in c_row sums the first endpoint's colours; B_E already sums both
endpoints' scalar colours. Diagonal residual atoms contribute through
RG15--RG20 even though tree edges have distinct field links.

For any chosen fixed R satisfying RG8, beta,h,B_E and all other constants
are finite and independent of u,T. Thus there exists u_0, depending on
those constants and r_a, such that for all u>=u_0,

    R_c>=1, lambda<1,              epsilon_G<=beta/3.     (RG26)

These displayed inequalities, not an unstated generic smallness condition,
are the threshold. Increasing R to meet RG8 can make u_0 very large; no
useful numerical size or continuum scaling is claimed.

## 8. Exact reader regrouping, logarithm, and nonvanishing

The endpoint gas from RG22 is a sum over unordered families of species
whose nonempty X_z are pairwise disjoint. At fixed volume its absolutely
summed activity is finite by RG25: sum_z|a_z|<=|Lambda|epsilon_G. Families
contain at most m0|Lambda| members, since every species has a nonempty
field set. Thus the entire endpoint gas is absolutely summable, and
regrouping its countable decorations is legitimate.

For such a family, form the graph joining species when their S_z overlap.
For each nonempty connected subfamily Gamma with pairwise disjoint X_z,
make a new species with

    b_Gamma=product_(z in Gamma)a_z,
    S_Gamma=union_(z in Gamma)S_z.                        (RG27)

Every original family has a unique decomposition into these connected
components. Conversely, a family of these new species with disjoint
S_Gamma has pairwise disjoint X_z across components and recovers one
original family. Consequently J_0 is EXACTLY the hard-core gas of the
b_Gamma with incompatibility S_Gamma intersection. Distinct Gamma having
the same support remain separate species. This operation does not assert
that a hard indicator has finitely many covariance-noise readers.

Here is a complete bound for this regrouping. Put delta=beta/3 and
beta_1=beta-delta=2beta/3. For raw species use
`p_z=sup|a_z|exp(beta_1|S_z|)`. The total rooted overlap-tree series is the
monotone iteration of

    T_z=p_z exp[sum_(z':S_z' meets S_z) T_z'].

Expansion of the exponential supplies the factorial for unordered children;
iteration enumerates finite rooted trees with these symmetry factors.
Every connected family has a spanning tree, so the sum of these trees
majorizes its weight, even after dropping field-disjointness. By RG25--26,
`T_z^*=p_z exp(delta|S_z|)` is a supersolution: its neighbors sum to at most
|S_z|epsilon_G<=delta|S_z|. Root a connected family at a species whose
support contains v, and use `|union S_z|<=sum|S_z|`. It follows that

    sup_v sum_(Gamma:v in S_Gamma)
              exp(beta_1|S_Gamma|)sup|b_Gamma|
        <=epsilon_G<=beta/3.                             (RG28)

This also proves the needed absolute regrouping uniformly in volume in
its marked norm, rather than merely at each fixed volume.

For completeness the logarithm estimate uses another, distinct margin
alpha=beta/3, leaving the output rate mu=beta_1-alpha=beta/3. The formal
logarithm of a finite hard-core gas is the sum over connected
incompatibility graphs with one -1 per edge. Its absolute coefficient is
bounded by the sum of its spanning trees. To verify that last statement,
root at the least-labelled vertex and map each connected graph to its
breadth-first tree, with the least-labelled previous-level neighbor as
parent. For a fixed resulting tree, optional edges join equal levels or
join a vertex to a previous-level vertex whose label is no smaller than
its parent. Every such graph lies in one interval between the tree and
this maximal graph. Intersect the maximal graph with the fixed
incompatibility graph. The alternating sum on the interval is zero or
has modulus one. These disjoint intervals prove the tree bound.

Apply the same rooted exponential recursion to
`sup|b_Gamma|exp(mu|S_Gamma|)`. Equation RG28 makes
`sup|b_Gamma|exp((mu+alpha)|S_Gamma|)` a supersolution. Anchoring a connected
cluster through a box bounds its total series by epsilon_G. The graph
identity exponentiates to the gas for sufficiently small common activity
multiplier. Uniform absolute convergence for multipliers of modulus <=1
extends the identity to one. Finite sums first, followed by the dominated
species limit, give

    J_0(V)=exp[sum_(connected original-box Y) L_Y(V_Y)],
    sup_v sum_(Y contains v) exp(mu|Y|) sup|L_Y|<=epsilon_G,
    mu=beta/3=1/[3(16R)^4],         J_0(V)!=0.             (RG29)

The L_Y collect connected clusters with union Y, retaining their multiplicities
and the exact logarithm coefficients. Their support and analytic domain are
actual complete original readers. The branch is defined by the convergent
series and tends to zero as R_c->infinity. Equation RG29 is uniform in T
and on the admitted coarse tube for u>=u_0. It uses two explicit margins
beta/3, not RD's two units of support weight. Large supports are controlled
at the reduced rate written in RG29, not an arbitrary preassigned rate.

## 9. Scope of the gain and remaining physical interfaces

The result RG29 goes beyond a finite-range covariance or an endpoint-only
activity bound. It uses the actual PC residual sum, includes its infinite
complete readers and marked incidence, keeps the normalized marginal
vacuum one, and proves both exact factorization after reader regrouping
and absolute connected summability. RG6 is the uniform row-algebra estimate
that allows R to be enlarged without losing its perturbative advantage.
RG12--RG20 give the all-order coefficient/trace estimate, with determinant
loops, repeated indices and corner distributions explicit.

The source-free lift K has no original Wilson source epsilon dependence.
The present functions are holomorphic in their stated coarse readers;
extending them constantly in an already admitted epsilon disc is trivial
and gives no source-bearing interacting estimate. The nonzero actual force,
source Hessian and nonlinear remainder are still present in the exact
one-step chart identity

    Z_a=h_N^(m0 T^4)(2pi sigma^2)^(d/2)det K^(-1/2)
        exp[-F_epsilon(0;V)/sigma^2]
        integral_D dmu_(K^-1)(x)
          exp[-ell_epsilon.x-x^T E_epsilon x/2-R_epsilon(x)]. (RG30)

Replacing its last integral by J_0 would change that model. RG29 does not
cancel its determinant or vacuum, normalize its interacting hard event,
or absorb the extensive force cost. The auxiliary chart is a fixed product
of single-link HS balls. The original cut, G/Omega, extra chart complement,
retained histories and source insertions still require their exact interfaces.
No translated complex hard domains or contour side chains enter this unit.
The separately proposed joint critical-field packet was not consumed.

The primary point of contact is Martin Lohmann's
[arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1), especially its
intersection-component regrouping, independent-pair Gaussian derivatives,
and its warning that the sphere procedure is restricted to single-site
cutoffs. We rebuild the necessary algebra and estimates above; its full
Theorem 1 is not imported for this covariance or the interacting model.
Bałaban's constructions and Dimock's expositions remain the constructive
background. This note is a bounded Gaussian producer, not a claimed
replacement for their multiscale work.

The unsuccessful shortcut of giving endpoint activities only their field
supports is explicitly avoided by RG23 and RG27. A direct residual expansion
without a connected spanning structure gives only an extensive absolute
sum; RG22 supplies that structure before complete-reader regrouping. An
infinite independent-noise representation was not used and would not make
these hard indicators finitely local. None of those limitations is a no-go
statement about another construction.

This is written analysis, with no numerical experiments or author-issued
independent verdict. The unchanged BF and PC sources remain immutable.
The [read manifest](checks/reader_local_gaussian_return_read_manifest.json)
and [author receipt](checks/reader_local_gaussian_return_receipt.json) bind
the scoped source reads, explicit self-checks and frozen identities. Root
owns integration into PR #10114 and commissions a fresh hostile review.
Review does not confer audit status or either physical conclusion.
