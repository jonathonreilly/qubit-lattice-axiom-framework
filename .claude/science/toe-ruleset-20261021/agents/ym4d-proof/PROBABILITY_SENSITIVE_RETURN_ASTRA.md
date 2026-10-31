# Probability-sensitive return: an actual chart regulator and the unsummed boundary expansion

**Author research unit; independent review pending. The requested connected
return theorem remains OPEN.** This note proves a coefficientwise quadratic
regulator for the actual one-step chart density, uniformly through ordinary
Gaussian forest weakening. It also gives the exact boundary terms and
reference factors of that construction. It does not prove convergence of a
source-local return expansion. The positive result is the regulator in
§3, not a renamed assumption that the required logarithm exists.

The target remains full four-dimensional existence **and a positive physical
continuum mass gap**. Neither follows from this finite-step result. The
supplied SU(N) Wilson action and normalized paired S4-prime kernel are
mathematical model inputs, not newly adopted physical axioms. Bałaban and
Dimock are credited for the small/large-field, minimizer and localization
architecture. The specialized estimates used here are derived below.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
independent_review: pending
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## 1. Frozen target and the actual consumer

The target is a connected logarithm for the original-cut one-step integral,
with its exact reference, original Wilson sources in a fixed product disc,
the required coarse complex tube, all original readers, and uniform rooted
support-size bounds. The initial denominator read was [RD](RD.md), 583 lines
at commit `3bba91875672becadc0ab120204905d9f1f405a8`, SHA256
`06ad2b5b52bfa66f7784a1fb97936337c59f5164318f89af9a2a065226671e5f`.
Its formulas (2), (5), (11), (14)-(18) were reconstructed before this work.
That read is not a read of the later 1,037-line file.

During this task the coordinator integrated RD pass 2. The separately read
new interface is §5.1, lines 822-891, in RD SHA256
`a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5`,
recoverable at `ddc0515e563507c74050d9c55201abb6981d4d69`. Its R15 exactly
organizes connected simultaneous failures on a **product** reference; R16
accepts their integrated absolute masses, and R17 proves the needed
factorization after bounding interaction atoms in supremum norm. This is a
real improvement over RD18's supremum-defect criterion. It does not accept
an interacting probability from a different reference. The new
[review](REVIEW_RD_R2.md) leaves quantitative convergence and the complete
Gaussian consumer match open. No effective-level result is used here.

The exact bare density throughout this note is

    w_epsilon(U,V)=exp[-u sum_p (1+epsilon_p)s(U_p)]
                     product_c k_(kappa u)(V_c;M_c(U)),
    s(W)=1-Re tr(W)/N,
    k_t(V;M)=exp[-t(1-Re tr(V^-1 M)/N)]/N_t(M),
    N_t(M)=integral_SU(N) exp[-t(1-Re tr(W^-1 M)/N)]dHaar(W),
    Z_cut(V,epsilon)=integral chi_cut(U) w_epsilon(U,V)dHaar(U). (PS1)

The cut is the original product of interior plaquette cuts. It is independent
of epsilon. The kernel stiffness t=kappa u stays real and fixed. In the
bare frozen-block return operation the denominator is the same expression
restricted to the integrated block interiors, retaining every plaquette and
kernel that reads them. It is not a Gaussian-sector denominator by definition.

Use the original [SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md) white cube Omega
and strong-good event G, unchanged. [GC](GRADED_COMPLEMENT_ASTRA.md) supplies
real original-cut conditional witness bounds on its chart C_ch. Their full
labels include the matrix-atom readers and the logarithmic collars, with
O(log^5 u) comparison entropy and an explicit O(log^4 u) packing loss in
the reader-separated product argument. GC is an expectation cover, not an
exact expansion of the complement indicator.

For any fixed source-independent event H, real V and e=Re epsilon,

    |integral chi_cut H w_epsilon / Z_sec(V,epsilon)|
       <=nu_cut^e(H) Z_cut(V,e)/|Z_sec(V,epsilon)|.           (PS2)

This follows directly from |w_epsilon|=w_e. It exhibits the unpaid reference
ratio. Positivity of Z_cut(V,e) and the selected-sector zero-free theorem do
not cancel that ratio. The selected-source theorem [FR](FIXED_SOURCE_RADIUS_ASTRA.md)
also keeps an O(rho p^2) critical-action budget on its curvature window.
Its corrected FR9 compares only polynomial moments with an uncut Gaussian;
general nonlinear readers remain on the finite contour. Neither result is
used to discard a phase or hard boundary below.

## 2. An exact chart identity with all modes and factors

Fix N>=2, odd L>=3, T>=2, D=N^2-1, kappa in its fixed positive compact
interval, and u>=N. Set m0=3L^4+1, n=m0 T^4, d=Dn and sigma^2=N/u.
Use the actual root-pinned axial trees. Their triangular Haar change of
variables has Jacobian and integrated nonroot gauge volume one. All free
links, colours, root modes and harmonic directions remain.

The brick lift U0(V) has identity internal links and crossing links V_c.
Every paired transporter is exactly V_c at this lift, including the labelled
periodic paths. The two-block filling uses the lifted brick, excluding the
extra far seam when T=2. In the fixed HS-orthonormal scalar coordinates put
U_e(a)=exp(a_e)U0_e(V), with zero tree coordinates, and

    F_epsilon(a;V)=F_0(a;V)+sum_p epsilon_p W_p(a;V),
    W_p=tr(2I-U_p-U_p^-1)/2,
    F_0=sigma^2[-log w_0(U(a),V)-sum_free e log j_N(a_e)].    (PS3)

The Haar constant h_N is outside F; j_N occurs exactly once inside F.
The complete compact kernel normalizer is inside F. At the lift,

    F_0(0)/sigma^2=u L^2 sum_coarse P s(V_P)+4T^4 log N_t(I).

This vacuum is retained, including its sign.

Here are the actual precision inputs, with their mechanism recalled to
specify the model rather than assert a generic convexity hypothesis.
[CB6-CB10](COVARIANT_SOFT_BACKGROUND_ASTRA.md) recover a free edge from
curvature and the averaged path inside an exactly flat lifted brick.
Counting its fillings gives
`H_V>=a_gap I`, `a_gap=1/max(C_F,C_Q/kappa_-)`, with
`C_F=4L^3(L+4)(60L^2)^2`, `C_Q=2L^3`. Unitary transports preserve this
bound at arbitrary compatible holonomy. The exact finite-u Hessian is

    K=F_0''(0)=H_V+E_V+kappa(1-c_N(kappa u))B_V+N^2/(6u)I,
    max(row_HS,col_HS)||E_V||<=24 delta_V,                  (PS4)

where delta_V=max_P||I-V_P||op and B_V>=0 is the complete path spread.
The last term is the Haar Hessian. A plaquette's second derivative consists
of four signed insertions and their ordered pairs; replacing its background
plaquette by I changes each colour-block entry by at most delta_V. Four
entries per row and six incident plaquettes give the displayed 24. Thus on
the admitted curvature domain there are fixed gamma,B>0 with
`gamma I<=K<=B I`. K is the full colour matrix of range two. Its force is
`||F_0'(0)||_(infinity,HS)<=6sqrt(N)delta_V`; it is not set to zero.

Choose an **auxiliary** fixed radius r_a>0 no larger than GC's r and the
CB/SA analytic radii, with the additional regulator inequalities in §3.
Define C_a by ||a_e||HS<=r_a/2 at every free link. This does not redefine
GC's C_ch. If r_a<r, the difference C_ch\C_a remains in the outside term.
Four-factor telescoping on interior plaquettes gives defect <=2r_a, so
the original cut is automatic on C_a with GC's r<=epsilon_cut/8.

Set x=a/sigma and R=r_a/(2sigma). This deliberately uses the lift rather
than silently replacing it by a critical point. The chart is the exact
product `D_R=product_e{||x_e||HS<=R}`, independent of epsilon. Let
G_0=K^-1 (this symbol is a covariance, not the good event G), and define

    ell_epsilon=sigma^-1 F_epsilon'(0),
    E_epsilon=sum_p epsilon_p W_p''(0),
    R_epsilon(x)=sum_(q>=3) sigma^(q-2) F_epsilon^(q)(0)[x]^q/q!.

Taylor's theorem on the fixed analytic chart gives exactly

    Z_a(V,epsilon)=P_a(V,epsilon) I_a(V,epsilon),
    P_a=h_N^n (2pi sigma^2)^(d/2) det(K)^(-1/2)
                         exp[-F_epsilon(0;V)/sigma^2],
    I_a=integral_D_R dmu_(G_0)(x)
           exp[-ell_epsilon.x-x^T E_epsilon x/2-R_epsilon(x)]. (PS5)

No determinant power, Gaussian normalizer, root mean, Haar factor or compact
kernel factor has disappeared. In particular ell is present at epsilon=0
whenever the lift is nonstationary. This is an actual part of PS1, not a
chosen new probability model.

Impose the already used selected-sector margins and additionally
`sqrt(D)[C_b delta_V+sigma p M_C]<r_a/2`. For
`p=log(2+u)^alpha`, alpha>5/2, and the admitted delta_V<=c sigma p,
this holds for sufficiently large u with fixed r_a. Then Omega is contained
in C_a and the unchanged exact decomposition is

    Z_cut=Z_sec
       +integral chi_cut 1_(C_a intersect (G\Omega)) w_epsilon
       +integral chi_cut 1_(C_a intersect G^c) w_epsilon
       +integral chi_cut 1_(C_a^c) w_epsilon.              (PS6)

The first three terms sum to Z_a. No estimate from the mutable outside-chart
author packet is consumed. The final integral, including C_ch\C_a when
present, remains explicit. An arbitrary retained history must stay inside
each integral with its exact tree average; the present proof inserts none.

## 3. A coefficientwise quadratic regulator for this actual phase

The following is the new bounded positive result. Fix a finite support rate
beta in the fixed SA boxes. Every local vertex is assigned its entire
connected radius-three reader stencil, including original coarse links and
Wilson coefficient sources. A scalar field slot belongs to that stencil.
There are at most q0=(8L^4+8)D slots per vertex and at most fifteen incident
vertices per scalar coordinate. Choose common radius a0 and bound H from
CB9's centered analytic Wilson/kernel/Haar vertices. They are uniform in
u and real admitted V; the scalar normalizer vacuum was removed only from
the **derivative bound**, not from PS5.

For a full marked-support count one may use SA's fixed
`d0=(9L^4+5)(2R_A+6)^4`, `s=9^4`, enlarged if necessary; R_A is the fixed
box parameter, unrelated to the field radius R above. Define

    f(t)=H(1-t/a0)^(-q0),
    A_q=(1+rho)d0 exp(beta s) f^(q)(0)/q!, q>=3.           (PS7)

Expanding the actual local vertices at a=0, write their degree-q sum as
`sum_(m,S) c_(m,S) x^m`, with |m|=q. The coefficients are analytic in
the original epsilon and local V; each connected S contains all field
slots and every original reader. Multivariate Cauchy followed by summing
all scalar monomials gives

    sup_v sum_(m,S:v in S, |m|=q)
                   exp(beta|S|) sup_|epsilon|<=rho |c_(m,S)|<=A_q. (PS8)

To check PS8, a coefficient of degree m is bounded by H a0^(-|m|).
There are binomial(q0+q-1,q) degree-q monomials on at most q0 slots;
this is f^(q)(0)/q!. Marking the full stencil costs d0 exp(beta s).
The source contribution multiplies only a subset of Wilson vertices and
costs at most rho times the same enlarged bound. No independent-colour
approximation or endpoint-only support is used.

Let arbitrary factors zeta_(m,S) of modulus at most one multiply these
coefficients. They may, in particular, be products of real forest parameters
on any fixed tree spanning the **full** reader S. On D_R,

    sum_(q>=3,m,S) exp(beta|S|)
       |sigma^(q-2) zeta_(m,S)c_(m,S)x^m|
                  <=eta_beta(r_a) sum_i |x_i|^2,
    eta_beta(r_a)=sum_(q>=3) A_q (r_a/2)^(q-2)=O(r_a).    (PS9)

Proof: with |x_i|<=R, the weighted arithmetic-geometric mean inequality is

    |x^m|<=R^(q-2) sum_i(m_i/q)|x_i|^2.

Indeed, apply it to |x_i/R|^2, then use that their weighted average is at
most one. After summing coefficients, the contribution to coordinate i
is bounded by the full marked sum through its owner box in PS8, since
m_i/q<=1. Also sigma R=r_a/2. The series converges for r_a/2<a0 and
starts linearly in r_a. This proves PS9, including every complex source
supremum and complete reader weight. Notice the distinction: the absolute
supremum of the nonlinear interaction can be O(u r_a^3) per coordinate,
while its quadratic-regulator coefficient is O(r_a).

Likewise the local source Hessians and forces give finite constants C2,C1,
chosen before u,T,p, such that, even after modulus-one coefficient weakening,

    max(row,col)||E_epsilon||_absolute<=C2 rho,
    max_i |ell_epsilon,i|<=C1(1+rho)delta_V/sigma.          (PS10)

For the force use the six incident Wilson traces paired with a traceless
insertion and P0-I; kernel and Haar forces vanish at the lift. The absolute
sum is at most 6sqrt(N)(1+rho)delta_V before scalar overcounting. For the
Hessian, differentiate the finite local Cauchy series twice and sum the
same finite stencil incidence. Marked versions of PS10 follow with d1 and
d2 as in SA10. Cancellation between different plaquettes is not needed.

Choose r_a and then a fixed rho>0, no greater than the admitted SA/FR/GC
radii, so that

    eta_beta(r_a)+C2 rho/2<=gamma/8.                       (PS11)

The source interval is independent of u,p and volume. This is an additional
small-radius choice for the auxiliary chart; it does not strengthen a
statement about the original G by changing G's thresholds.

Now take any real forest interpolation matrix s on the free **links**,
with s_ee=1 and s_ef equal to the minimum edge parameter on the forest path,
or zero when no path exists. Put

    G_s(e alpha,f beta)=s_ef G_0(e alpha,f beta).

For each t in [0,1], the relation that all path parameters are >=t partitions
the links. Its block indicator matrix is positive semidefinite. Integration
over t represents s as a convex average of those matrices. Expanding each
link into all D colours preserves this fact. Schur multiplication by this
mask is positive and fixes I. Since `B^-1 I<=G_0<=gamma^-1 I`,

    B^-1 I<=G_s<=gamma^-1 I,
    gamma I<=G_s^-1<=B I.                                (PS12)

For clarity, the positivity assertion can be proved without a named theorem:
write the mask as a Gram matrix `s_ij=<v_i,v_j>`. For a positive matrix A
and scalar z, `sum_ij conjugate(z_i)A_ij s_ij z_j` is the sum, over an
orthonormal basis in the Gram space, of quadratic forms of A. It is
nonnegative. Applying this to A minus its spectral lower bound, and to its
upper bound minus A, proves PS12. Principal compressions obey the same
spectral intervals. The full covariance determinant remains in the density.

Allow separate modulus-one weakening of the nonlinear/source coefficient
atoms as in PS9-PS10, denoting the weakened force by ell_s. Combining
PS9-PS12 and
`|ell_s,i x_i|<=gamma |x_i|^2/8+2|ell_s,i|^2/gamma` gives the uniform
pointwise density envelope

    |1_D_R dmu_(G_s)(x) exp[-ell_s.x-x^T E_s x/2-R_s(x)]|
      <=det(2pi G_s)^(-1/2)
         exp[2||ell_s||_2^2/gamma-gamma||x||_2^2/4] dx.    (PS13)

This inequality is for the actual local phase at s=1 and its displayed
deformations, with complex original Wilson coefficients. Its price is
explicit: `||ell_s||_2^2<=d C1^2(1+rho)^2 delta_V^2/sigma^2`.
On delta_V<=c sigma p it can be O(d p^2), even at zero source. It must
ultimately be absorbed into the **same** saddle/reference normalization,
not declared small. No normalized complex probability or partition-function
lower bound has been obtained by taking the modulus.

## 4. Boundary terms: exact first derivative and a paid chart trace

The chart's ultralocal boundary is useful, but has to remain. Let
`g_s(x)=det(2pi G_s)^(-1/2)exp(-x^T G_s^-1 x/2)` and
`f_s=exp(-ell_s.x-x^T E_s x/2-R_s(x))`. For a covariance parameter between
two distinct links e,f, differentiating the normalized Gaussian gives

    partial_s integral_D_R g_s f_s
      =sum_(alpha,beta) G_0(e alpha,f beta)
             integral_D_R f_s partial_(e alpha)partial_(f beta)g_s
         +integral_D_R g_s partial_s f_s.                 (PS14)

This follows by differentiating the determinant and inverse in the Gaussian
density; the off-diagonal symmetric covariance variation supplies the two
equal half terms. The coefficient derivative in the second term is present
when the interaction/source atoms are also weakened.

For scalar indices i,j in the first term, the divergence theorem on the
product of balls gives

    integral_D_R f partial_i partial_j g
      =integral_D_R g partial_i partial_j f
       +integral_boundary D_R [n_i f partial_j g
                                      -n_j g partial_i f]dS. (PS15)

First integrate the i derivative off g, then the j derivative off g. This
proves the signs and shows precisely which boundary term would be lost by
an uncut integration-by-parts identity. The boundary is the union of its
one-link spheres, with the other link balls retained. Their intersections
have surface measure zero in PS15; repeated integrations can create corner
traces, which must then be retained in the weak derivative formula.

PS13 does pay a first **undifferentiated** chart surface. For a prescribed
link e, |x_e|=R gives, after reserving half the remaining Gaussian exponent,

    integral_(|x_e|=R, other links in D_R) |g_s f_s|dS_e dx_rest
      <=det(2pi G_s)^(-1/2) exp[2||ell_s||^2/gamma]
        area(S^(D-1)) R^(D-1) exp(-gamma R^2/8)
                                   (8pi/gamma)^((d-D)/2). (PS16)

This is direct integration of PS13, enlarging only the remaining Gaussian
integrals to R^(d-D). The exponential is
`exp[-gamma r_a^2/(32sigma^2)]`. It dominates any fixed power of u for a
fixed number of surface derivatives if the other factors are controlled,
but PS16 retains its full-dimensional determinant and force price. It is
not a volume-uniform normalized boundary activity, and it estimates neither
term containing derivatives in PS15 without further polynomial/analytic
derivative bounds. It is not an all-orders trace theorem.

There is a separate boundary for the **unchanged** selected white cube. In
the original a coordinates let `y=sigma^-1 T_*(a-b_0)`, with
T_*=K_*^(1/2) and all the original-reader atoms of SA/GC. Under a smooth
real deformation of these maps, at a fixed real a the distributional formula is

    partial_t 1_(|y_i(t)|<=p for all i)
      =-sum_i sum_(s=+/-1) s delta(y_i-s p) partial_t y_i
                                      product_(j!=i)1_(|y_j|<=p). (PS17)

It follows by differentiating H(p-y_i)H(p+y_i), tested against a smooth
compact density. The level surfaces are regular because the affine map is
invertible. Coarea supplies the factor 1/||gradient_a y_i|| on each surface.
Higher derivatives retain intersections and derivatives of these surface
distributions. A variation of a single T atom localizes partial_t y_i;
it does **not** localize delta(y_i-s p), which still sees the full row and
the other retained requirements. GC23's event cover is an inequality and
does not replace PS17 by local hard factors. No derivative of a hard
indicator has been treated as an ordinary analytic Taylor coefficient.

## 5. Where the attempted connected expansion stops

PS5 and PS13 improve the analytic starting point, but there are three exact
interfaces to settle before this route can meet RD R16. They overlap; no
independence or count of fundamental obstructions is asserted.

**Reference and product structure.** In x=a/sigma the auxiliary chart cut
and local phase vertices are local, while mu_(G_0) is correlated. RD R17's
factorization is therefore unavailable. Whitening x=K^-1/2 W makes the
reference product, but the conditions ||(K^-1/2 W)_e||<=R and the hard
history readers become nonlocal. Assigning their complete support to the
whole volume preserves the identity and loses the rooted exponential
support-size bound. A bare original-cut probability cannot be inserted as
delta_a for the different product reference in RD R16.

**Original-reader localization and Gaussian stability.** PS12 weakens the
whole covariance by its field endpoints. Its entry G_0(i,j;V), including a
diagonal entry, still reads distant original V through the inverse. SA's
parametrix expands it into connected full-reader atoms; it does not assert
that every atom is positive. Independently weakening those full-reader atoms
is a different covariance from G_s. PS12 does not prove its accretivity.
The direct absolute perturbation estimate is bounded by the non-small
full incidence norm Q(G_0), not by a small parameter. This estimate therefore
does not close the positivity step. It is a failed sufficient estimate, not
a proof that a suitable localized covariance deformation cannot exist.
An alternative is to localize the resulting Gaussian component functions
after the positive field forest; that requires its own differentiated
reference and support estimates.

**All derivative trees and the same complex reference.** PS13 is an
integrable envelope, and PS16 is one surface envelope. To sum the forest,
one must control all the derivatives in PS14-PS17, their multiplicities,
their complete readers and the partition normalizers on one common domain.
GC's bound under the original real law is only at the undeformed endpoint.
It gives no bound for those signed surface distributions or for the
interpolated normalized measures. The positive real witness price
`exp[-c p^2+C log^5 u]` cannot be carried through an unproved division by
a complex local partition function.

For comparison, the direct fixed-denominator conditional envelope for an
R_j block uses `0<=s(U_p)<=2`, and costs at most

    |integral chi_cut H w_(R_j)^epsilon / D_(R_j)^0|
      <=exp[2u rho |P(R_j)|]
                         nu_(R_j,cut)^0(H | exterior).    (PS18)

It follows simply by bounding each source exponential before integration
and retaining D_(R_j)^0. Since |P(R_j)|=O(L^4 ell^4) and ell=O(log u),
this supplied bound costs O(rho u log^4 u), whereas the proved witness gain
is O(p^2). For any fixed logarithmic power p and fixed rho>0, that bound
does not give a small activity. This is a failure of this envelope, not a
lower bound on the actual activity. This displayed numerator ratio does not
include H8's source compensator; its elementary modulus bound adds a further
cost rather than proving a cancellation. PS13 is designed to replace this
excessive loss with a quadratic/saddle comparison, but the required local
normalizer cancellation has not been proved.

## 6. A precise next estimate, with its strength stated

A sufficient next producer is an **exact** field-and-reader forest or other
connected decomposition of PS5, including the relevant hard requirements,
whose differentiated connected integrals A_X have a reference fixed in the
construction and satisfy, on a common original-source/coarse-data domain,

    sup_v sum_(X contains v) exp((mu+1)|X|) sup_D |A_X|
                 <=q_small<1/4.                           (PS19)

For a probability-sensitive implementation the pre-summation bound must
give a small factor for a chosen separated set of actual boundary/failure
witnesses **under every interpolation used**, retain derivative factorials
and all colour legs, and pay the complete supports. A usable form is a
bound for each such differentiated integral by

    C^(|X|+number_of_legs) product_vertices(degree!)
      product_edges c_edge(full reader label)
      exp[-c p^2 times paid_witness_count+C_entropy log^5(u)
                                              times paid_witness_count], (PS20)

with summable marked edge families, sufficiently many paid witnesses or
small interaction insertions to sum every tree, and exact cancellation of
the same-component Gaussian/saddle normalizer. PS20 is a specification,
**not a proved estimate**. In particular the force price in PS13 cannot
be left as an all-volume constant on the right. The required witness count
has to be proved for the actual configuration/decomposition, not read off
the number of overlapping GC labels.

Once PS19 holds for an exact hard-core gas, the elementary rooted-tree
Mayer proof in RD yields its connected logarithm. Requiring PS19 directly
is comparable to the selected-chart target, so this note does not count
that reduction as closure. PS9, PS12 and PS13 are strictly weaker supplied
ingredients. Outside-C_a integration, arbitrary histories, inherited
effective actions and full hole supports remain further interfaces. A
complex coarse tube additionally requires its actual contour/boundary
construction: this note proves no such tube for the full hard-cut integral.

The most concrete continuation is to use PS9's relative quadratic bound
in a Gaussian forest with a local small/large decomposition, then prove the
derivative trace estimates before converting the original-reader atoms.
A different live continuation is localizing the positive Gaussian component
functions after field decoupling; this avoids assuming atomwise positivity
but does not avoid reference and reader estimates.

## 7. Primary-source match and preserved failed attempts

[Lohmann, arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1) is a
construction template only. Theorem 1 requires a massive covariance, small
analytic interaction norms and a cutoff that factors over individual sites.
Its equations (11)-(12) impose an additional large-field domination test.
Remarks 2 and 10 exclude an automatic extension to general multilink cuts;
the weak integration-by-parts construction retains surface terms. These
prerequisites were read directly. No theorem from that paper is imported.
The present auxiliary chart has the relevant product geometry before
whitening, while the original white/history requirements still need PS17.
PS9 rebuilds a relative quadratic estimate tailored to the actual phase;
it does not verify the paper's full norm hypotheses.

The failed routes preserved here are: treating GC probabilities as RD18
supremum defects; putting them into R16 under a different reference; using
PS18 at fixed rho; dropping PS15's boundary; and inferring full-reader
accretivity from the endpoint Schur deformation PS12. The first two are
the pre-existing consumer mismatch, not claimed as new counterexamples.
The last three are explicit failed steps in this construction. No toy
model, numerical success or bibliographic analogy is offered as a proof
about the actual Yang-Mills integral.

## 8. No-Go Discipline Gate and review handoff

This is positive bounded support plus a preserved partial attempt, not an
impossibility theorem or an exhaustion claim.

* **N1:** Three mechanisms were actually examined: product-reference
  resampling (PS18), Gaussian field forests with the regulator (PS9-PS17),
  and full-reader atom localization after/before that forest. None is
  declared ruled out. Five closed families have not been established;
  no negative-packet PASS is claimed.
* **N2:** Reference comparison, localization and derivative summation are
  interacting parts of one missing construction. Their pairwise implication
  relations are not proved. No independent-wall count is used.
* **N3:** The supplied model, local analytic radius, real gap, curvature
  domain, auxiliary chart and fixed source radius are explicit. The
  mathematical proof introduces no physical premise through terminology.
* **N4:** RD's reference/product mismatch, GC's expectation-only output and
  FR's finite-contour restriction match the stated consumers exactly. The
  distinct perturbative determinant-residual note is not used as RD.
* **N5:** No numerical runner was executed. The written regulator counts
  scalar legs, whole-colour link spheres, fixed box readers and arbitrary
  finite torus volume. It does not claim all-history or continuum bounds.
* **N6:** No new axiom or primitive is requested. The mathematical model is
  separately supplied. Registry inspection is governance context only.
* **N7:** A strong counterargument to any proposed no-go is that PS9 supplies
  precisely the missing relative large-field stability needed by a
  Gaussian integration-by-parts expansion. Prove its all-order trace and
  normalization estimates, then localize complete readers. This is a live
  construction, not a reason to declare the route impossible.
* **N8:** The narrow local-source search and direct RD/SA/FR/GC reads found
  the same consumer mismatch; FR demonstrates that exact contour side
  accounting can remove a misleading source-radius restriction. That
  mechanism is retained as a possible continuation, not dismissed.

No new numerical experiment was necessary or run; no numerical criteria or
PASS output are fabricated. Hashes and link checks are identity evidence.
The [read manifest](checks/probability_sensitive_return_read_manifest.json)
records complete, bounded, incidental and truncated reads separately.
The [author freeze](checks/probability_sensitive_return_receipt.json) binds
this packet. All historical predecessor receipts remain unchanged.

The methodology source is immutable observed main
`01589af3faf806b736c42dc2f3bd625e9edead9f`, with the lane's
[PROCESS_LIGHT](PROCESS_LIGHT.md). The coordinator owns Git, locks, shared
fronts, PR #10114 and independent review. This author writes only this file
and checks/probability_sensitive_return_* and assigns no independent LAND.
The requested worker configuration was Astra/max; the system identifies
generic GPT-6, so the requested dispatch is not a backend attestation.

**Review request:** check the actual phase and determinant identity PS5,
the full-reader coefficient count PS7-PS10, the colour-block Schur bound
PS12, the force and surface prices PS13/PS16, and the non-closure boundary.
The strongest proved proposal is the fixed-chart regulator, not PS19 or
PS20. Full existence and the physical continuum mass gap remain open.
