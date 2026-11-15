# The actual centered nonlinear chart with every covariance reader

This unit constructs a connected logarithm for the **actual centered
finite-u nonlinear fixed-ball chart transform**, with the full joint
critical covariance and both infinite complete-reader tails retained.
The logarithm is small at an explicit positive rate in original blocks;
its convergent series proves complex nonvanishing. The raw one-step
action, normalized compact kernel, Haar constant and full determinant
remain outside this small nonlinear logarithm.

This is a centered-contour result. Returning a fixed original physical
chart requires its translated side/corner chains. The original-cut
complement, arbitrary histories, effective-level identification,
multiscale iteration, four-dimensional continuum existence and a positive
physical continuum mass gap are not proved here. Both physical targets
remain **OPEN**. A fresh independent review of this new unit is required.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact connected logarithm and complex nonvanishing for the actual joint critical-Gaussian centered nonlinear fixed-ball chart, including all complete-reader covariance tails."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Producer matches, exact object, and parameter order

The actual finite-u critical field and covariance are those of
[FU](FINITE_U_CRITICAL_FIELD_ASTRA.md), SHA256
`ecace773f964a18fe6e5c14d46d38913dc52f95afbd2c8763e4766f0c286377d`.
[NC](NONLINEAR_CHART_ACTIVITY_ASTRA.md), SHA256
`72651905fa554d44e7d42406af199ec0e9a75a88c030009626929f9f77dc1dec`,
supplies complete-reader nonlinear vertex envelopes on that joint domain.
NC was provisional when this unit began. Its fresh review subsequently
accepted it unchanged, SHA256
`4e782d52b86bd7bd25ad5cd8ac123ec32d21b516f501df8c3eb92a2b8a57df84`.
Its finite-range-core logarithm is not substituted for the present object.

[RG](READER_LOCAL_GAUSSIAN_RETURN_ASTRA.md), SHA256
`4f94b5e2102391441233621d99be3e4b14dc46b9be89ea35915b354a4d0a06d6`,
and its fresh review SHA256
`74332f30c4b51a8886c61883b9c6a4077d0f59716d2aab067d2ccd4d261fa6b1`
supply the rebuilt principal-core inverse and normalized-marginal
loop/chain library. RG's endpoint theorem is Gaussian-only. The nonlinear
component forest, scalar-coordinate attachment sum, primitive-compatible
reader regrouping and parity improvement are proved below. The separate
critical-Gaussian bridge and shifted-chart return units are not mathematical
premises here; the needed retuning is independently rebuilt below.

Fix N>=2, D=N^2-1, odd L>=3, T>=2, real u>=N and kappa in its admitted
positive compact interval. Put sigma^2=N/u, m0=3L^4+1, n0=Dm0, n=m0 T^4
and d=n0 T^4. All free colours, root modes, crossings and harmonic
directions of the actual pinned-tree quotient are retained. Its integrated
gauge volume is one. The exact phase and normalized transform are

    F_epsilon=F_0+sum_p epsilon_p W_p,
    F_0=sigma^2[-log w_0-sum_free e log j_N(a_e)],
    W_p=tr(2I-U_p-U_p^-1)/2,
    b=b_*(V,epsilon), F_epsilon'(b)=0,
    K_*=F_epsilon''(b), C_*=K_*^-1,
    J(V,epsilon)=E_(C_*)[1_D_p exp(-sum_v R_v(z))],
    D_p=product_free e {||z_e||HS<=p}, p=r_a/sigma.        (NR1)

The local centered remainders R_v are NC4, recalled in section 3. The
normalized compact kernel at fixed real t=kappa u and the complete Haar
log are included exactly once in F. Negative complex edges use inverses
and the separate backward means. Original Wilson sources vary on the
fixed product disc |epsilon_p|<rho; coarse data vary as
`V_c=exp(v_c)Vbar_c`, max ||v_c||HS<eta, about admitted real centers.
FU supplies a common product domain. Its joint suprema retain
`delta_hat=delta_*+8eta`; delta_V replacements apply only at fixed real V.
Stationarity holds throughout that joint domain, not merely at a flat center.

The order of choices matters. Fix the R-independent core row constants
below, enlarge the fixed patch radius R, then recompute FU's marked
budgets and choose its positive field/source/coarse radii. Next choose a
fixed r_a, and only then take u large. All constants remain independent
of u,T. Increasing R decreases beta; no old support rate is retained.

## 2. Retuning the actual critical tail, with the core unchanged

Keep PC/FU's geometry-only partition and the actual lift core

    P=sum_A chi_A G_A chi_A=c0 I+sum_A D_A,
    G_A=(K restricted to A)^-1, K=F_0''(0;V),
    C_*=P+E, E=E_lift+T_crit.                            (NR2)

The whole matrices D_A are positive at real V. On the reduced common
complex tube the core has Re P>=c0 I. Each entry obeys
`sup|P(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)]`: the principal-inverse bound
from FU5 is multiplied by chi_A(i)chi_A(j), whose sum is <=1 by
Cauchy--Schwarz and sum_A chi_A^2=1. Consequently

    max(row,col)sum sup|P(i,j)|<=g,
    g=(2n0/gamma)coth(m/4)^4, ||P||op<=g.                 (NR3)

These constants do not grow with R. For every principal active matrix
P[I] on whole links, conjugate it by exp(theta distance from a fixed
column). Set

    A_1=(2n0/gamma)sum_(z in Z^4)|z|_1 exp[-m|z|_1/2],
    theta=min(m/2,c0/(2A_1)),
    v_I=(2n0/c0)coth(theta/2)^4,
    a=c0/g^2, b_P=1/c0.                                 (NR4)

The conjugation changes both row and column sums by at most theta A_1,
using exp(theta t)-1<=theta t exp(theta t). Hence its inverse has norm
<=2/c0 and entries <=(2/c0)exp[-theta distance]. Summing proves

    max(row,col)sum sup|(P[I])^-1(i,j)|<=v_I,
    Re (P[I])^-1>=a I, ||(P[I])^-1||<=b_P.               (NR5)

The last bound follows from Re P[I]>=c0; the lower precision bound follows
from `Re G=G^*(Re P[I])G` and ||P[I]||<=g. Periodic representatives form
a subset of Z^4, so these estimates cover all T and every disconnected
active set. They are sums of entrywise suprema on the original-data tube.

For matrix atoms, M_beta is the maximum weighted absolute row/column sum;
B_beta sums all scalar entries through a marked complete reader, with
individual coefficient suprema inside. Choose

    e_* = min(c0/8,1/(4v_I),a/(64v_I^2)),
    r_PC<=min(1/4,c0/(32p_PC),e_*/(4p_PC)),
    beta=(16R)^-4, p_PC=exp(1)J g,
    d_H<=min(d_* of FU17,e_*/(4m_G^2)).                   (NR6)

Here r_PC is PC's O(1/R) residual bound, not the chart radius. The
constants p_PC,v_I,a,c0 are R-independent, so the R choice is possible.
Afterward FU's N(t), A_G and d_H majorants give a positive joint domain
with the extra Hessian requirement, by choosing tau and rho and then
curvature/eta smaller. The same actual b is selected by local uniqueness
on overlaps. This is a restriction of FU, not an assumption of a new field.

Indeed

    M_beta(E_lift)<=p_PC r_PC/(1-r_PC)<=e_*/3,
    M_beta(T_crit)<=m_G^2 d_H/(1-m_G d_H)<=e_*/3.          (NR7)

FU17 ensures m_G d_H<=1/4. Thus a fixed uniform bound eps<=e_* can be
used for M_beta(E), and a fixed finite B_E bounds B_beta(E), with the
explicit value supplied by adding FU10 and FU26. B_E can be large and
will be paid, not declared small. At T<16R the whole-torus lift patch is
allowed with its bounded reader cost; E_lift then vanishes, but T_crit
is still retained.

Write

    t=v_I eps<=1/4,
    t_E=v_I^2 eps/(1-t)<=a/48,
    ell=-(1/2)log(1-t).                                  (NR8)

All residual atoms keep both field endpoints and every original coarse
and source reader. Both tails are exact, symmetric, absolutely convergent
families on the joint domain. Their row and marked bounds are those of
the full colour matrix, with no deleted modes or trace directions.

## 3. Exact primitives and the nonlinear envelopes used

For each original local vertex v subtract its own jets at b:

    R_v(z)=sigma^-2[F_v(b+sigma z)-F_v(b)
                  -sigma F_v'(b)z-sigma^2 F_v''(b)[z,z]/2]. (NR9)

The sum of the first jets vanishes; individual first jets need not vanish.
Combine (1+epsilon_p)W_p into its one original Wilson vertex. There are
6L^4 Wilson, four kernel and m0 Haar vertices per block. If L_v is its
actual free-link stencil, let I_v contain all their scalar colours. NC3
gives |I_v|<=q=(8L^4+8)D and at most d_inc=15 original vertices per scalar.
A vertex with no field dependence has R_v=0 and creates no primitive;
its entire value remains in the phase prefactor.

The NC5 coefficient expansion is obtained at fine field zero, then
substitutes FU's connected b atoms. Its root mark and attached-field mark
are bounded by f^(l)(tau) and tau f^(l+1)(tau), where
f(t)=H(1-t/a_f)^-q is the actual finite-u local Cauchy majorant. The
fluctuation variables remain in I_v; solved b is never new independent
data. For a fixed small r_a, define

    chi_e=1_(||z_e||<=p), chi_v=product_(e in L_v)chi_e,
    f_v=chi_v[exp(-R_v)-1], h_e=1-chi_e,
    P_k(v,z)=sum_(i in I_v)|z_i|^k.                       (NR10)

The functions and all reader atoms are zero outside their local chart.
NC10--NC16 give positive complete-reader families w_v,S and e_v,S such that

    |f_v;S|<=chi_v sigma P_3 exp[2A sigma P_3] w_v,S,
    |f_v;S^even|<=chi_v sigma^2(P_4+P_3^2)
                       exp[2A(sigma P_3+sigma^2 P_4)] e_v,S,
    sup_v sum_S exp(beta|S|)w_v,S<=W0,
    sup_x sum_(v,S containing x)exp(beta|S|)w_v,S<=W1,
    sup_v sum_S exp(beta|S|)e_v,S<=E0,
    sup_x sum_(v,S containing x)exp(beta|S|)e_v,S<=E1.     (NR11)

These constants are the finite NC7/10/15 constants, recomputed at the
restricted FU domain and new beta. In particular W0=2A3, W1=2B3,
E0=2A4+2A3^2 and
`E1=2B4+4A3 B3+2A3^2(B3+B4)/A`, with A=max(1,A3,A4).
Their individual-atom proof uses
`Y^(k-1)/(k-1)!<=(2A)^(-(k-1))exp(2AY)` in the Mayer series; the reader
mark cancels its remaining k denominator. The even family consists of
one even seed or two odd seeds and the two geometric remainder factors.
Thus it includes the marks in both seeds and in each geometric factor.

All labels S are connected original-block labels and contain the original
vertex stencil and every b/source/coarse reader. Supremum is inside their
sums. These are integrand coefficient labels; they do not yet localize an
integral against C_*.

For DISTINCT selected original vertices the product regulator is bounded
by exp(eta_r||z||^2), where eta_r=2A d_inc r_a(1+r_a). Choose r_a>0
within the fixed Taylor/chart margins and with

    eta_r<=min(a/32,alpha_FU/(4U_FU^2)).                  (NR12)

The constants A,a were fixed first, so this is a nonempty fixed choice.
Here alpha_FU and U_FU are the covariance accretivity and upper-norm
constants in FU28. This preserves NC's own regulator condition and the
stronger slack needed below. Taylor powers, parity, b, C_* and t=kappa u are always considered
at fixed actual u. The even part starts at sigma^2; the odd part at sigma.
No change of u is hidden in an auxiliary parity parameter.

The exact primitive expansion is

    J=sum_(W,H)(-1)^|H| E_(C_*)[product_(v in W) f_v
                                             product_(e in H)h_e]. (NR13)

It follows from `1_D_p exp(-sum R_v)=product_e(1-h_e)product_v(1+f_v)`.
Each original vertex and cut link is chosen at most once; each selected
vertex chooses one of its reader atoms. A failure in L_v annihilates its
selected f_v. All global chart indicators are retained. No interacting
or globally conditioned marginal is used.

## 4. Core components of a primitive family

Give each primitive (v,S) the enlarged reader S+=S union Q_v, and a cut
primitive e the reader Q_e, where Q=N_(16R)(root) in coarse sup distance.
The actual patch geometry gives displacement <=5R+9<=16R from a field
vertex root to every core patch reader touching its field stencil. Thus

    |Q|<=s_c=(32R+1)^4,
    d_c=(9L^4+5)s_c, d_h=m0 s_c                         (NR14)

bound the nonlinear and cut root incidences. This also covers the
whole-torus small-volume patch. These are fixed geometry-only readers.

For a selected primitive family, partition its enlarged readers into
overlap-connected components B. Each B retains its actual primitive list,
not just its union S_B; let I_B be its active scalar field set. Different
B have disjoint S_B and hence disjoint fields. P[I] is block diagonal
over the B: any contributing patch entry connecting two components would
put the same complete patch reader in both collars. Its inverse and
normalized Gaussian therefore split over these components. Each block
P[I_B], its inverse and its determinant read only S_B. The latter may
be large; it is charged once, not once per inverse entry.

This partition is exact and unique. Conversely, internally connected
primitive components with pairwise disjoint S_B reconstruct precisely one
original primitive family. All original-vertex uniqueness and cut
compatibility conditions remain inside the components and across their
disjoint readers. Their removal is permitted only in positive estimates.

## 5. Normalized marginal loops, chains and scalar-coordinate jets

Let I be the active union of a nonempty collection of B. The exact
normalized marginal of C_* is C_*[I], the principal **covariance**, not
the inverse of a principal precision. For real positive matrices this
is Gaussian completion of the square; it continues holomorphically to
Re C>0 under uniform local Gaussian domination. Inactive normalizers
therefore disappear by that exact identity, not by a bound on a ratio.

Write G=(P[I])^-1. Independently mask only the E entries between different
B by coordinates s_BB'; entries within one B are unchanged. Since P is
block diagonal, C_I(s)=P[I]+E_I(s). For |s_BB'|<2 its Hermitian part is
>=c0-2eps>=3c0/4 and its norm is <=g+2eps<=5g/4. The Gaussian integrals
are holomorphic on this entire pair polydisc. At a forest mask they
factor by its components in the field variables, even before their
possibly remote data readers are localized.

The radius-two polydisc is used only for the analytic forest identity.
All quantitative list and jet bounds below are evaluated on real forest
masks, where every |s_BB'|<=1. The normalized density ratio there is exactly

    g_(P[I]+E_I(s))(y)=g_(P[I])(y) exp L_I(y),
    L_I(y)=sum_(k>=1)(-1)^k Tr[(G E_I(s))^k]/(2k)
       +(1/2)sum_(k>=1)(-1)^(k-1)y^T(G E_I(s))^k G y.    (NR15)

The first series is the full determinant ratio and the second the full
inverse correction. Expand each E into its original atoms and all
matrix indices. Expanding the exponential as ordered loop/chain lists
omega retains its list factorial. Let g_omega(y) include the base g_P
and the contribution of one list. All G factors have both indices in
one B and read S_B. Consequently the coefficient reader is contained in

    union_B S_B union union_(E occurrences in omega) S_a. (NR16)

At empty I there is precisely the normalized marginal one. There are no
loops, chains or residual vacuum species without a selected primitive.

Here is the quantitative library, rebuilt to include the joint-source
tail. Use the positive matrix envelope of E with weight exp(beta|S_a|).
Its row/column norm is <=eps, so loops cost at most |I|ell and chains
at most t_E||y||^2/2. The ordered-list sum is their exponential.
For G, Re G>=a and ||G||<=b_P; Young's inequality gives

    |g_P(x+z)|<=(b_P/(2pi))^(|I|/2)
            exp[-a||x||^2/4+c_g||z||^2],
    c_g=2b_P^2/a+b_P.                                   (NR17)

For a marked block x_0 define

    d_(x_0)(i)=sum_(j,a:x_0 in S_a)exp(beta|S_a|)sup|E_a(i,j)|,
    D_(x_0)(I)=sum_(i in I)d_(x_0)(i),
    sum_i d_(x_0)(i)<=B_E.                              (NR18)

Marking a loop cancels its 1/k and costs
`A0 D_(x_0)(I)`, A0=v_I/[2(1-t)]. Marking a chain splits it into two
geometric sides and costs `A2 D_(x_0)(I)||y||^2`,
A2=v_I^2/[2(1-t)^2]. This uses the total entry sum of its marked matrix;
it includes diagonal atoms whose coefficient reads distant data.

With

    c_*=c_g+t_E+1, K_m=A0+2A2(16/a+1),
    L_jet=max(1,sqrt(2 exp(1)c_*)),
    A_I=(b_P/(2pi))^(|I|/2)exp(|I|ell),                  (NR19)

the unmarked and marked absolute list sums are bounded respectively by
`A_I exp[-a||x||^2/8+c_*||z||^2]` and that expression times
K_m D_(x_0)(I). This follows from t_E<=a/16 and absorbing the marked
quadratic with `s exp(-a s/16)<=16/a` and `s exp(-s)<=1`.
All sums contain individual coefficient suprema on the projected joint
domain. Complex source dependence is inside those suprema.

For any scalar multiindex nu, each g_omega is entire in y. Cauchy radii
sqrt(nu_i/(2c_*)) for nu_i>0 give the same two bounds at z=0 multiplied by

    L_jet^|nu| product_(i in I)sqrt(nu_i!).                  (NR20)

Indeed nu_i!<=nu_i^(nu_i) gives the square-root factorial after optimizing
the circle. Tonelli permits summing positive coefficient envelopes before
the Cauchy integrals. The individual scalar factorials are retained. They
will not be replaced by the factorial of all legs on a large component.

Multiply by the actual primitive functions at real x; no derivative is
moved onto them. NR12 leaves exp(-a||x||^2/16) after the nonlinear
regulator. A scalar Gaussian of variance 8/a then dominates the fields.
Define

    K_g=max(1,exp(ell)sqrt(8b_P/a)),
    M90=max_(0<=j<=90) E_(X~N(0,8/a)) |X|^j,
    C_V=q(1+q)(K_g M90)^q,
    q_H=K_g^D 2^(D/2)exp[-a r_a^2/(32sigma^2)].           (NR21)

For a hard link, the exponential Markov moment of
exp(a||x_e||^2/32) under that product Gaussian is 2^(D/2).
For a nonlinear vertex use P_3, or P_4+P_3^2<=P_4+qP_6. Since original
vertices are distinct, every scalar polynomial exponent is <=6*15=90.
Thus for any admissible primitive family A and any nu, its integrated
absolute density-jet list sum is at most

    L_jet^|nu| product_i sqrt(nu_i!) product_(o in A) a_o,
    a_(v,S)=C_V sigma w_v,S, a_e=q_H.                    (NR22)

Its density-reader-marked version has the additional factor
K_m D_(x_0)(I). If a hard link overlaps a selected local vertex cutoff,
the product is identically zero. Otherwise the hard coordinates separate
under the dominating product law. The factor K_g^|I| pays the **active**
normalized determinant and all colours; |I|<=q|W|+D|H|. No inactive-volume
factor, force cost or interacting normalizer has been canceled.

For a single nonlinear primitive with nu=0, every individual g_omega is
even under x->-x: the base Gaussian and all its chains are even. Its odd
Mayer part integrates to zero. Its signed bound therefore uses
`a_(v,S)^even=C_V sigma^2 e_v,S`. This cancellation is valid separately
at each complete reader decoration, with u held fixed. It does not
improve the absolute moment of an unintegrated Mayer function.

## 6. Exact block-pair forests and complete reader species

Fix one admissible collection of primitive components B_1,...,B_m and
let Phi be its product of primitive functions, including hard failures
and their signs. The function `F(s)=integral Phi g_(C_I(s))` is analytic
in the pair polydisc above. Differentiating its **normalized density** gives

    partial_(s_BB') F(s)=sum_(i in I_B,j in I_B') E(i,j)
                   integral Phi partial_i partial_j g_(C_I(s)). (NR23)

The identity is obtained by differentiating both determinant and inverse:
`dot g=g[x^T C^-1 dot C C^-1 x-Tr(C^-1 dot C)]/2`.
The two symmetric ordered off-block entries cancel the factor 1/2.
Repeated independent-pair derivatives give the corresponding product of
constant E entries and the scalar field derivatives of the density.
The primitives, their coefficients and their fixed cutoffs are untouched.
There is no integration by parts and hence no suppressed cutoff surface.

Apply the finite forest identity, then evaluate each independent-pair
derivative at the path-minimum forest mask. One proof checks a monomial:
give every present pair with exponent k an independent clock with
distribution t^k. Its almost surely unique maximum spanning forest
partitions the event space; conditional on its tree clocks, all other
clocks lie below the minimum along their path. Their probabilities and
the tree densities give exactly the forest formula. The analytic Taylor
series on the radius-two pair polydisc permits termwise passage to F.
This is not differentiation of a path minimum or of a reader monomial.

At a disconnected forest mask the Gaussian and Phi factor over its
components in field variables. Grouping forest components yields a gas
whose raw connected species consists of: a nonempty set of primitive
components B with pairwise disjoint S_B; a tree on them; each scalar
endpoint and E atom on every tree edge; and a normalized-density list
omega from NR15 after the derivatives are taken. Explicitly, orient the
edges once, let nu count their scalar endpoint incidences, and write

    a_z=product_(edges e) E_(a_e)(i_e,j_e)
        * integral_[0,1]^T dt integral_R^I
                   Phi_B(x) partial^nu g_omega(x;s^T) dx. (NR23a)

Here Phi_B is the product of the selected reader-labelled Mayer functions
and signed hard failures. The density list includes its ordered-list
factorial and every normalization term. An empty tree has product one
and nu=0. No field derivative acts on Phi_B. Its base support and complete
support are

    B_z=union_(B in z) S_B,
    S_z=B_z union union_(tree E atoms)S_a
                    union union_(density E occurrences)S_a. (NR24)

S_z is connected: its tree E readers join the connected S_B; each density
occurrence has an active endpoint and attaches its complete reader there.
All inverse-core coefficients read their own S_B, charged only once.
Each a_z is holomorphic in its actual original readers by the uniform
absolute density/jet series. The formulas agree on projected tube overlaps.

The raw species gas is compatible when the B_z are disjoint, not merely
when field sets are disjoint. This is precisely the compatibility inherited
from the unique primitive-component partition. It preserves original
vertex uniqueness and field compatibility. The full S_z may overlap
across compatible raw species; that issue is handled exactly in section 9.
No residual-only species is created from an empty primitive family.

## 7. Per-coordinate attachments sum the Gaussian trees

Set delta=beta/8, beta1=beta-delta, beta2=beta-2delta. Define primitive
root budgets, including the fixed core collars, by

    h_v=C_V sigma exp(beta s_c)(W1+d_c W0),
    h_2=C_V sigma^2 exp(beta s_c)(E1+d_c E0),
    h_h=d_h exp(beta s_c)q_H, h=h_v+h_h.                  (NR25)

A reader mark in the original vertex atom costs W1 or E1; a mark in its
new collar costs d_c W0 or d_c E0. The inflation exp(beta s_c) pays the
whole added reader. The cut budget counts all m0 free links per block.

For a primitive component B put u_B=product_(o in B)a_o, retaining only
its admissible internally connected primitive families. If h<=delta,

    sup_x sum_(B:x in S_B) exp(beta1|S_B|)u_B<=h.         (NR26)

To verify this, weight each primitive by exp(beta1|S_o|), bound connected
collections by rooted overlap trees, and use the recursion
`T_o=v_o exp(sum_(o' overlaps o)T_o')`. The supersolution
`T_o<=a_o exp(beta|S_o|)` is stable since its neighbor sum is <=h|S_o|.
Rooting at an object whose reader contains x proves NR26. Constraints
are dropped only in this positive counting bound. No Gaussian moment
claim is made for the fictitious repeated-vertex objects thereby added.

Define the nonnegative scalar endpoint envelope

    e_ij=sum_a exp(beta|S_a|)sup|E_a(i,j)|,
    max(row,col)sum e_ij<=eps.                           (NR27)

For the Gaussian tree sum at rate beta2 give B weight
`v_B=u_B exp(beta2|S_B|)`. A subtree rooted at B with one incoming
scalar leg at i in I_B has a positive majorant T(B,i). At each coordinate
j let k_j be the number of child legs. NR20 assigns the factor
`product_j sqrt((k_j+1_(j=i))!)`. Each child edge costs L_jet^2 e_jk.
Consequently the exact exponential child counting is bounded by

    T(B,i)<=v_B product_(j in I_B) H_(1_(j=i))(y_j),
    y_j=L_jet^2 sum_(B',k in I_B') e_jk T(B',k),
    H0(y)=sum_(k>=0)y^k/sqrt(k!),
    H1(y)=sum_(k>=0)sqrt((k+1)!)y^k/k!.                  (NR28)

The multinomial for allocating unordered children to scalar coordinates
gives the product of their 1/k_j! factors. Keeping these coordinates is
essential. For 0<=y<=1/2, the coefficient bounds 1/sqrt(k!)<=1 and
sqrt((k+1)!)/k!<=k+1 give

    H0(y)<=1/(1-y)<=exp(2y),
    H1(y)<=1/(1-y)^2<=exp(4y).                           (NR29)

Use the supersolution `T*(B,i)=u_B exp(beta1|S_B|)`.
For each fixed scalar k, NR26 bounds
`sum_(B':k in I_B')T*(B',k)<=h`, because its owner lies in S_B'.
Thus y_j<=L_jet^2 eps h and
`sum_(j in I_B)y_j<=n0 |S_B| L_jet^2 eps h`. Choose once

    h_c=min(delta/2,1/[4(1+L_jet^2 eps)],
                         delta/[8n0(1+L_jet^2 eps)]).       (NR30)

If h<=h_c, the y_j are <=1/4 and the exponent in NR29 is <=delta|S_B|/2.
The supersolution is therefore stable. Monotone iteration sums every
finite rooted tree. The tree with no incoming leg uses H0 at every
coordinate and has the same bound. Relaxing component compatibility or
allowing repeated components enlarges only this formal positive tree sum;
no inadmissible moment is used to derive NR22.

In particular, attachments cost an exponential **linear** in |S_B|.
Replacing product_i sqrt(nu_i!) by sqrt((sum_i nu_i)!) before the child
allocation would instead allow a bound growing as exp(c|I_B|^2); that
unsummable shortcut is not used.

## 8. Every marked tail reader is paid, then parity improves the bound

The tree edge parameters have integration volume one. NR22, NR27 and
NR28 therefore bound the absolute raw species sum, including all ordered
density lists, at reader rate beta2. There are three ways a marked block
x_0 can lie in S_z.

If it lies in B_z, root the Gaussian tree at a component whose S_B
contains it. NR26 and the supersolution bound this contribution by h.
If it lies in a density residual reader, use the marked NR22. Since
`D_(x_0)(I)=sum_B sum_(i in I_B)d_(x_0)(i)`, rooting at the component
containing that pinned scalar gives at most K_m B_E h. The pin mass is
B_E, not a presumed small row norm.

For a tree residual reader mark, distinguish the marked edge and remove
it in the positive tree majorant. The two sides are rooted subtrees with
one incoming scalar leg, precisely the T(B,i) in NR28. The ordering
factor for the two sides is at most one (its exact unoriented value is
1/2). Summing the marked edge entries gives B_E; summing either rooted
side through its fixed scalar endpoint costs <=h. This third contribution
is at most L_jet^2 B_E h^2. This is a factorization of the positive tree
count, not an asserted factorization of the original coupled integral.
All scalar colours are already summed in e_ij and B_E. Hence

    sup_(x_0)sum_(z:x_0 in S_z)exp(beta2|S_z|)sup|a_z|
       <=C0 h+L_jet^2 B_E h^2, C0=1+K_m B_E,              (NR31)

as an initial absolute bound. Each complete base reader is paid once;
each residual occurrence is paid by its exp(beta|S_a|) weight, which
dominates the required union weight. There is no bound on B_E assumed
except its fixed finiteness.

To obtain the small nonlinear order, count primitive objects, not density
loops or inverse factors. A species with exactly one primitive has no
Gaussian tree edge. If that primitive is nonlinear, the even density
list and fixed ball imply the signed singleton bound in section 5,
with all its readers retained. If it is a cut, use q_H. The same base
and density-reader mark bounds give

    singleton raw-species norm <=C0(h_2+h_h).             (NR32)

For species with at least two primitives use homogeneous rescaling in
the positive majorant, keeping u, b, C_*, the density lists and all
Gaussian constants fixed. Multiply every primitive amplitude by
t=h_c/h>=1. Its component/tree bounds remain valid, with total primitive
budget h_c. Every species of primitive degree at least two is then
multiplied by at least t^2. Applying NR31 at t and undoing it gives

    higher-degree norm <=[C0/h_c+L_jet^2 B_E] h^2,
    epsilon_N=C0(h_2+h_h)+[C0/h_c+L_jet^2 B_E]h^2.          (NR33)

For h=0 the assertion is trivial. The fictitious multiplier is applied
to f_v and -h_e after their exact definitions; it does not vary u or
erase their regulators. Original-vertex distinctness remains in every
actual species. Nonempty active sets are essential: a degree-zero
residual vacuum would invalidate this improvement, and NR15 creates none.

Require h<=h_c, q_H<=1 and epsilon_N<=delta/2. These explicit conditions
hold for all sufficiently large u after the preceding choices: h_v is a
fixed constant times sigma, h_2 a fixed constant times sigma^2, and h_h
a fixed constant times exp[-a r_a^2/(32sigma^2)]. Therefore

    epsilon_N<=C_1 sigma^2+C_2 exp[-a r_a^2/(32sigma^2)],   (NR34)

with fixed finite constants independent of u,T. They may be enormous.
This is a nonempty analytic regime, not a numerical threshold or a
continuum scaling claim.

## 9. Exact reader regrouping, connected log and nonvanishing

At finite volume the absolute raw activity sum is finite by NR33:
it is <=|Lambda|epsilon_N. Every raw species has a nonempty base support,
so a compatible family has finitely many members. All reader decorations
can therefore be regrouped absolutely.

For a raw family with pairwise disjoint B_z, join species whenever their
complete S_z overlap. Each nonempty connected subfamily Gamma, retaining
that base compatibility, becomes a new species with

    b_Gamma=product_(z in Gamma)a_z,
    S_Gamma=union_(z in Gamma)S_z.                        (NR35)

Every old family has one such component partition. Conversely a family
of these new species with disjoint S_Gamma reconstructs one old family,
since full-reader disjointness implies base-reader disjointness across
components. Compatibility within Gamma is still imposed. Thus the new
hard-core gas with reader exclusion is **exactly J**, not a gas obtained
by replacing the old incompatibility relation by fiat.

Spend a third margin delta, from beta2 to beta3=beta-3delta. The rooted
overlap recursion for raw species is
`T_z=p_z exp(sum_(S_z' meets S_z)T_z')`,
with `p_z=sup|a_z|exp(beta3|S_z|)`. By NR33, the supersolution
`T_z<=sup|a_z|exp(beta2|S_z|)` is stable: neighbors cost at most
epsilon_N|S_z|<=delta|S_z|. Dropping base compatibility only in this
positive bound gives a rooted norm <=epsilon_N for the b_Gamma at beta3.

For the logarithm spend a fourth margin delta, leaving mu=beta/2.
The finite hard-core log has connected incompatibility-graph coefficients.
Their alternating sum is bounded by the number of spanning trees:
fix a total edge order and partition connected graphs by their Kruskal
minimum spanning tree. The permitted extra edges form a Boolean interval,
whose alternating sum has modulus zero or one. The same rooted-tree
recursion, now for b_Gamma, is stable under its beta3 norm bound and yields

    J(V,epsilon)=exp[sum_(connected original-block Y)H_Y(V_Y,epsilon_Y)],
    sup_x sum_(Y containing x)exp(mu|Y|)sup|H_Y|<=epsilon_N,
    mu=beta/2=1/[2(16R)^4]>0, J(V,epsilon)!=0.             (NR36)

The finite graph identity holds near zero common gas multiplier.
Absolute convergence throughout its unit multiplier disc extends the
identity to one and proves nonvanishing before defining the logarithm.
Finite atom/list truncations followed by the uniform dominated limits
justify every expansion, derivative, integration and regrouping above.
Each coefficient is holomorphic on its projected original coarse/source
domain and retains its complete connected reader union. The resulting
branch tends to zero as u grows in the displayed regime.

Four margins beta/8 were paid separately: primitive overlap components,
Gaussian attachments, full-reader regrouping, and the logarithm. The
output rate is not an arbitrary preassigned rate. Fixed-order original
coarse/source derivatives can spend any further margin mu-mu'>0 on the
half parameter tube by the NC30 Cauchy count. No unchanged RD two-unit
consumer or stronger FR box margin follows from NR36.

## 10. Exact phase normalization and the unclosed physical return

The auxiliary centered contour a=b+sigma z, z in D_p, has the exact raw
integral

    Z_cent=h_N^n(2pi sigma^2)^(d/2)det(K_*)^(-1/2)
                        exp[-F_epsilon(b)/sigma^2] J(V,epsilon). (NR37)

The full critical action includes the source-dependent vacuum and the
finite-u compact normalizer. Haar j_N occurs once inside it and h_N
once outside. All d modes and the full colour determinant remain. The
prefactors are holomorphic and nonzero on the FU domain, so NR36 also
proves nonvanishing of this specified centered-contour integral. The
small O(1/u) norm belongs to log J, not to the entire prefactored action.
On a fixed real V the source-critical action still has its separate
O(rho delta_V^2/sigma^2) budget; joint tube suprema use delta_hat.

For real data, positive fixed chart/cut margins can place this sector
inside the original cut, as in NC31, by choosing the domains before u.
That does not make it the entire original-cut integral or redefine G
or Omega. At complex source it is a specified pulled-back top form.
A fixed physical original-a chart D_a instead gives `(D_a-b)/sigma`;
its translated side/corner chains and sweep-domain bounds remain the
separate shifted-chart task. Their absence is not inferred from the
evenness of D_p, nor is an original hard history transported here.

The result resolves the covariance-tail interface **for the centered
nonlinear chart object NR1**. It does not identify same-component
normalizers in a retained failure history, cancel action/determinant
ratios in the original-cut denominator, price every complement, establish
effective iteration, or provide a continuum construction or physical gap.
The positive Gaussian precision used in the proof is an auxiliary
one-step bound, not an interacting physical mass-gap statement.

## 11. Rejected shortcuts, provenance, and review boundary

Several potentially fatal shortcuts are explicitly avoided:

- Using RG's Gaussian-only endpoint theorem as if it included nonlinear
  insertions: NR22--NR33 derive the nonlinear moment and attachment costs.
- Reading an active marginal as an inverse principal precision, or
  dropping its determinant: NR15 retains both normalized density series.
- Charging the entire active-reader union at each inverse factor: G splits
  over the primitive components and each S_B is charged only once.
- Replacing per-coordinate factorials by one component factorial: NR28
  allocates unordered children before summation, keeping a linear size cost.
- Assuming the marked tail norm is small: B_E appears in C0 and NR33 and
  is paid by weak/bad primitives before any reader gas is summed.
- Replacing primitive/base compatibility by reader incompatibility:
  NR35 is a unique regrouping with the old compatibility retained inside.
- Producing an uncharged residual vacuum: the normalized empty marginal
  is exactly one, and every nontrivial species contains a primitive.
- Applying parity to an absolute Mayer moment or to a translated chart:
  only signed fixed-u singleton integrals on the centered chart use it.

Bałaban's constructions and Dimock's expositions are the architectural
antecedents. RG's locally rebuilt forest/marginal library and NC's
locally rebuilt Mayer/parity envelopes are credited at their exact
reviewed scopes. The nonlinear extension and its compatibility/attachment
proof are provided here, with no new external theorem imported by citation.
No numerical experiment is needed; the positive thresholds are the
displayed inequalities. A mechanical hash/link check is not a theorem test.

All NC, FU, PC and PS source/package bytes remain immutable. The new
mathematical source is frozen before its read and author packet. Requested
Astra/max is not backend attestation; a fresh independent reviewer must
examine this exact new argument. The coordinator owns PR #10114, Git,
shared fronts, preservation checks and audit gates. This author neither
performs those operations nor assigns an independent LAND or retained grade.
