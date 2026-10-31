# The bare original-cut / original white-cube logarithm

This assembles an actual bare-step normalized logarithm and its ordered
real (6,4) coarse/original-source jets. It compares the unchanged original
interior-plaquette cut with the original source-free white SCALAR cube.
One common radius construction identifies the intermediate transported
chart literally. Frozen and transported critical prefactors are kept
distinct. The total price includes O(sigma p_Omega^3); it is not purely rare.

The mathematical inputs are [HC](HOLOMORPHIC_COMPACT_RETURN_ASTRA.md),
[CW](COMPLEX_WHITE_SECTOR_ASTRA.md), [WR](WEIGHTED_RETURN_JETS_ASTRA.md),
[FT](FROZEN_TRANSPORTED_CHART_ASTRA.md),
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md) and
[RC](REGIONAL_CHART_RETURN_ASTRA.md). [WS](WHITE_SECTOR_MATCHING_ASTRA.md)
identifies the literal real white sector. HC734 has SHA256
`890a56113ad3ceac890ec72efe59b40f73bbda283c8dfb69c331bc4ea5376c49`,
CW747 has `fb72d33bddb727e85548ad96f0e45585cf06254190aa182008e80aa3fbbc5a3c`,
and WR937 has `c728997d978a5a15cb9e7fcde5fd806b03ae4874b1b0956a69ba327a62a4deb3`.
All three were read completely. Their formulas and proofs, not verdicts,
are used. CW is still under a separate fresh review at this authoring
checkpoint; this assembly inherits that provisional review dependency.
Bałaban and Dimock are credited for the localization architecture.
No new external mathematical theorem is invoked.

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

## 1. Literal objects and normalization

Fix N>=2, odd L>=3, T>=2, the admitted positive compact kappa interval,
u>=N, D=N^2-1, m0=3L^4+1, n=m0 T^4, k=Dm0, d=kT^4 and sigma^2=N/u.
The pinned trees, free WHOLE links, lifted T=2 seam convention and scalar
HS basis are common. All colour, crossing, harmonic and root modes remain.
Nonroot gauge Haar volume and tree Jacobian are one; no further slice or
Faddeev--Popov factor is introduced. The exact density is

    w_epsilon(U,V)=exp[-u sum_p(1+epsilon_p)s(U_p)]
       product_c exp{t tr(V_c^-1 M_c^+ + M_c^- V_c)/(2N)}/Z_t(M_c),
    t=kappa u, s(P)=tr(2I-P-P^-1)/(2N),
    F_epsilon(a;V)=-sigma^2 log w_epsilon(exp(a)U0(V),V)
                                      -sigma^2 sum_e log j_N(a_e). (BW1)

M^+ averages the original 24L^4 words; M^- averages their inverses.
It is not (M^+)^-1. Every original field-dependent normalizer, source
label and raw kernel vacuum is retained. On rough real fine inputs Z_t
is its positive compact integral and independent of output V. Small
complex fine inputs use CW section 2's checked paired-normalizer branches.

About real Vbar write V_c=exp(v_c)Vbar_c, max||v_c||HS<eta. Let chi_cut
be the ORIGINAL block-interior plaquette cut, independent of V. Define

    Z_cut(V,epsilon)=int_(real SU(N)^E) chi_cut w_epsilon dH,
    Z_a,fr(V,epsilon)=int_(U=exp(a)U0(Vbar), ||a_e||HS<r_a) w_epsilon dH,
    Z_a,tr(V,epsilon)=h_N^n int_(product_e B_ra^D)
                                      exp[-F_epsilon(a;V)/sigma^2] da. (BW2)

The last expression is both HC2/FT42's transported physical chart and
CW3/RC's whole-region chart. Indeed, for each crossing link
Phi(a)=Log[exp(a)exp(v_c)],
exp(Phi(a))U0(Vbar)=exp(a)U0(V), and
j_N(Phi(a))det D Phi(a)=j_N(a). This is equality of holomorphic Haar
TOP FORMS on the checked fine/log branch, with complex determinant,
not its modulus. Internal links have Phi=a. Empty-field-stencil factors
multiply RC's touching integral explicitly, restoring the full BW1.
Nonempty-vertex vacua remain in their original vertices. Thus every
physical factor, all d scalar modes and h_N^n match exactly in BW2.

Let b_epsilon(V) solve F_epsilon'(b_epsilon;V)=0 and
K_epsilon=F_epsilon''(b_epsilon;V). The source-zero quantities are
b0=b_epsilon|0, K0=K_epsilon|0, C0=K0^(-1/2). CW's accretive Stieltjes
branch equals the positive inverse square root on real V and the old SA
critical branch by its common-cube uniqueness proof. For the SUPPLIED
p=p_Omega, define

    Z_Omega(V,epsilon)=h_N^n sigma^d det C0(V)
       int_([-p,p]^d) exp[-F_epsilon(b0(V)+sigma C0(V)w;V)/sigma^2] dw.
                                                                    (BW3)

At real V this is the literal original Omega, fixed as epsilon varies.
At complex V it is the explicit oriented white chain, not a continued
indicator. C0 is the full source-free CRITICAL inverse square root,
not a lift inverse, covariance, colourwise square root or tree Hessian.
Its real Gram determinant is det(C0^T C0)=det K0^-1 and its positive
Jacobian is sigma^d det C0. BW3 uses the corresponding complex top form.

## 2. One family and a nonempty common domain

All coefficient norms below put the individual parameter supremum INSIDE
all reader sums. For original connected block readers Y write

    ||A||_lambda=sup_x sum_(Y contains x) e^(lambda|Y|) sup |A_Y|.
                                                                    (BW4)

Fix the original vertices, scalar/source labels, geometry-only partitions,
patch cutoffs and ordering of all words, trees and graphs before varying
Vbar,V or epsilon. Choose ONE integer R>=8 satisfying RF16's endpoint
residual condition and CW10's exponentially small white residual condition.
The constants in these two endpoint tests are R-independent before the
choice, so a finite common R exists. Put beta=(16R)^-4 and lambda0=beta/2.
Recompute every finite marked constant and source threshold at this R.
RF/RC/WR use the SAME transported actual-V atom family, with both signed
covariance tails; the white resolvent is its distinct labelled construction.
HC/FT keep their distinct frozen-coordinate phase and real-center core.
No equality between these different cores or critical points is assumed.
Their labelled union on one original block graph is the assembly family.

CW's face range eight, R+8 reader collars and both endpoint/marked
half-power norms are used. Filling an R-box reader S by original blocks
costs |Y|<=(2R)^4|S|. One marked original block has one owner R-box;
there is no root multiplicity. CW's output rate one therefore gives
1/(2R)^4, which exceeds lambda0. RF/RC, HC/FT and WR retain their
lambda0 output after four beta/8 losses. All sums in BW4 use the full
readers, including normalizers, inactive collars and original sources.

Here is an explicit common order, including the moving-jet radius.
First fix the local fine/coarse analytic ceilings and bounds, RF's gap,
CW6's mixed derivative bound, and this R. Choose preliminary bar_tau,rho0
with the STRICT RF17/CW13 contraction and critical-tail inequalities,
then compute all local majorants and choose FIXED rho>0 satisfying
CW24, QC19/HC's source debit and WR's source restrictions. Its possible
small size depends on the fixed constants, not on u,T or either cutoff.
Choose c_tau,c_z with strict HC35/FT40/RC8 margins, and
0<c_q<=min(1/(2N),c_z^2/(64pi^2 N)). Set

    p_a=(log(2+u))^alpha, alpha>5/2,
    r_a=sigma p_a, tau=c_tau sigma p_a, zeta=c_z sigma p_a,
    q=c_q sigma^2 p_a^2, K=K(q) as HC10,
    s_u=sqrt(q)/(4K+1)^2.                                      (BW5)

Keep HC's exact c,a_bulk,C_quad,B_delta,B_eta,C_bar, and WR's
B_d=2A_G g_*(1+rho), enlarged fixed constants if their bounds differ.
Choose fixed POSITIVE d_delta,d_eta so all four inequalities hold:

    d_delta^2<=c/(8a_bulk), d_eta^2<=c/(32C_quad),
    (B_delta d_delta+B_eta d_eta)^2<=cN/(4096 C_bar k^2),
    B_d^2(d_delta+8d_eta)^2<=cN/(4096 C_bar k^2).                 (BW6)

There are only upper bounds by fixed positive numbers, so this choice
exists. Use the SAME outer coarse radius for HC/CW and WR's auxiliary xi:

    delta=min(d_delta s_u, sigma p/4),
    eta=xi=min(d_eta s_u, sigma p/32).                           (BW7)

Further fixed preliminary ceilings can be imposed by increasing u0.
In particular delta+8eta<=sigma p/2, as required by CW24; shrinking
WR's xi only improves its actual force and translation budgets.
Its inverse jet-radius cost is kept below, not discarded.

The supplied white profile must satisfy p>=1, sigma p^3 sufficiently
small and every original real-sector margin. To state a vanishing bound,
assume p->infinity and sigma p^3->0. Keep, with CW's actual C_b,M_C,

    A_box=sqrt(D)[C_b(delta+8eta)+sigma p M_C]<r_ch,
    delta+8eta+4A_box<delta_f, 5L A_box<eta_G,
    delta_f<=epsilon_1, r_a<=epsilon_1/8,
    C_b(delta+8eta)+sigma(1+1/16)p M_C<a_f/2,
    A_U sigma p^3<=h_G0/2.                                    (BW8)

The given G thresholds and their original Sea/SA conditions are unchanged.
Fixed small admissible delta_f,eta_G satisfy BW8 eventually. If an earlier
consumer fixed shrinking thresholds, BW8 must be checked on those literal
thresholds; changing them or p is not inferred. Flat coarse fields show
the curvature class is nonempty. With fixed admissible thresholds, any
supplied p satisfying the two limits above gives a positive common family
for all sufficiently large u, including p=sqrt(log(2+u)) if that was supplied.
Such a profile need not admit the un-narrowed HC window.

Indeed K->infinity, K=O(log u), sigma p_a->0 and s_u/(sigma p_a)=O(K^-2).
HC35--36 pay their quadratic coarse and buffer fractions by BW6 exactly;
smaller delta,eta preserve these inequalities. Regional force nonlinear
terms are O((sigma p_a)^2), and eta<=zeta/16 eventually. RC's strict
chart/side/corner conditions, CW's old-SA/IC/RF branch caps and its
independent-pair precision domain then all hold with their actual constants.
HC's remaining positive entropy exponent is O((log u)^5), while
u q=N c_q p_a^2. Its one ledger still spends 1/2-1/16-1/16=3/8.
WR's ledger spends 1/2-1/16=7/16, with no frozen/transport correction.
No original energy is spent a second time by this assembly.

The finite number of remaining strict small-log and analytic conditions
therefore hold beyond ONE volume-independent finite u0. For WR, p>=1
and p_a/K^2->infinity imply eta^-1=O(sigma^-1); hence its finite
R_h^-6 jet loss is polynomial in u and its rare proof still applies.
If p_a/K^2<=C_p p, the min restrictions in BW7 can instead be removed
after making sqrt(c_q)(d_delta+8d_eta)C_p<=1. Otherwise BW7 is the
explicit narrower curvature AND coarse tube. No wider RG domain follows.

## 3. Exact logarithm and all physical prefactors

On this family HC31/38--39, FT42 and CW31--32 give

    Z_cut/Z_a,fr=exp Psi_comp,  Z_a,fr/Z_a,tr=exp R_tr,
    Z_Omega/Z_a,tr=exp Gamma,
    Gamma=d log z_p+T_p+J_p-H_a,
    z_p=(2pi)^(-1/2) int_(-p)^p exp(-x^2/2) dx.                  (BW9)

Each symbol is its absolutely convergent sum of connected full-reader
coefficients. All three actual denominators and Z_cut are nonzero on
the common tube. The sign of R_tr is fr/tr. Define their LABELLED union
with the indicated signs; equal readers may be grouped absolutely. Then

    B_fr=log(Z_cut/Z_Omega)=Psi_comp+R_tr-Gamma
       =-d log z_p+Psi_comp+R_tr-T_p-J_p+H_a.                  (BW10)

This chooses the real logarithm of the positive ratio at v=epsilon=0.
The exponential identity and analytic continuation on this connected
polydisc fix its branch; no principal argument of an extensive scalar
ratio is taken. The singleton coefficient is -k log z_p at each block.
It remains even at epsilon=0. No volume-uniform bound on the scalar
ratio itself is asserted: |B_fr|<=T^4 ||B_fr||_lambda0.

For clarity the uncancelled physical formulas are

    P_fr=h_N^n(2pi sigma^2)^(d/2)
                    exp[-F_fr(b_fr)/sigma^2-LogDet K_fr/2],
    P_epsilon=h_N^n(2pi sigma^2)^(d/2)
                    exp[-F_epsilon(b_epsilon)/sigma^2-LogDet K_epsilon/2],
    Z_cut=P_fr exp(H_fr+Psi_comp),
    Z_a,tr=P_fr exp(H_fr-R_tr)=P_epsilon exp H_a,
    Z_Omega=P_epsilon z_p^d exp(T_p+J_p).                       (BW11)

The middle equality is equality of the actual chart integrals proved in
section 1. It does NOT identify P_fr with P_epsilon or their critical
points: the Haar-inclusive coordinate phases differ by the nonlinear
Jacobian. Equivalently P_fr/P_epsilon=exp(H_a-H_fr+R_tr); this is an
exact matched identity, not an independent small critical-action estimate.
CW's cancellation uses det C0 exp[-TrLog(C0^T K_epsilon C0)/2]
=exp[-LogDet K_epsilon/2]. The raw Gaussian log contains this full
determinant; it is not T_p. All kernel vacua, Haar, modes and action terms
in BW11 remain generally extensive. No IC tree-Gram identity is substituted.

With constants recomputed as in section 2, put

    A_comp=exp(-kappa_c p_a^2), kappa_c=cN c_q/32,
    A_tr=C_T(eta/sigma)(1+p_a^(91D+1))exp(-a p_a^2/64),
    E_w=k e^lambda0 |log z_p|+C_FR delta_G exp(-p^2/64)
                                  +C_FR A_U sigma p^3+epsilon_a,
    ||B_fr||_lambda0<=A_comp+A_tr+E_w=:B_hol.                   (BW12)

Here delta_G<=delta_G0/2 is CW23--24's complete source-precision/shift
mass, and epsilon_a is the EXACT recomputed RC13 budget. In particular

    epsilon_a<=C_a sigma^2+C_bnd(1+p_a^(91D+2))exp(-a_P p_a^2/64),
    |log z_p|<=C p^-1 exp(-p^2/2), delta_G<=C rho.               (BW13)

Compact roots, transport currents and white Gaussian tails have their
separate rare witnesses. J_p contributes the small O(sigma p^3) term;
H_a includes O(sigma^2). No purely rare J_p-H_a comparison is claimed.
For fixed bounded p the exact theorem still holds when its smallness
conditions do, but the retained -d log z_p need not vanish as u grows.

Source normalization is also exact, with J=u epsilon:

    log{[Z_cut(V,epsilon)/Z_cut(V,0)] /
                   [Z_Omega(V,epsilon)/Z_Omega(V,0)]}
                  =B_fr(V,epsilon)-B_fr(V,0).                  (BW14)

The constant -d log z_p cancels. Its norm is at most twice BW12 with
that singleton term removed. This is a ratio of actual source-normalized
objects; no source-dependent prefactor has been dropped from either one.
At half tubes, fixed-center scalar multiindex jets have bound B_hol times
ell!nu!(2D/eta)^|ell|(2/rho)^|nu|, with the actual BW7 radius.
These differentiate v while Vbar and HC selectors stay fixed.

## 4. Actual real moving-center coefficients and ordered jets

Now let V vary on the OPEN real curvature domain delta_V<delta and let
real |epsilon_p|<rho/4. WR33--38 constructs a canonical real coefficient
family Psi_diag for log[Z_cut(V,epsilon)/Z_a,tr(V,epsilon)]. Its proof
uses U_e=Z_e U0_e(V): the original cut is internal and the relevant Q
selectors become functions of Z only. Finite real rough-insertion Taylor
classes, the actual moving core/determinant and the normalized density
forest give genuine C^(6,4) coefficients; choosing a new center for each
value would not prove this. Keep that exact construction and its domains.

CW10--15, CW27 and RC16 also give canonical functions of ACTUAL V:
patch inverses use K_b(V); all local vertex Taylor coefficients, Picard
substitution trees, Stieltjes weights, normalized scalar contours and
forest/cluster indices are fixed independently of Vbar. Equal data on
a complete reader give equal coefficients before and after their uniformly
absolute sums. Normalizer and accretive branches agree on overlap.
The RC family uses the same transported actual-V indexing fixed above.
Thus Gamma from BW9 is one actual-V coefficient family on overlapping
tubes, not just a family of equally bounded pointwise logarithms.

Consequently, on the real domain, define

    B_diag=Psi_diag-Gamma=log[Z_cut(V,epsilon)/Z_Omega(V,epsilon)]. (BW15)

This is the same REAL scalar logarithm as BW10 evaluated with Vbar=V.
Their individual reader coefficients need not agree; their assemblies
are separately labelled. Derivatives of BW15 use the two proved canonical
families. We do not differentiate the substitution Vbar=V in HC's fixed
center coefficients, or infer that R_tr's fixed-center derivatives vanish
from its value R_tr(v=0,epsilon)=0.

Hold u,kappa, every normalized kernel and all jet weights fixed. For
D_B F(V)=d/dt F((exp(tB_c)V_c)_c)|0 and original directions |xi_p|<=r_p,
D_J,xi=u^-1 D_epsilon,xi. Define T^(6,4) by summing the suprema of
ordered D_B1...D_Bm D_J,xi1...D_J,xin, 0<=m<=6,0<=n<=4, with
1/(m!n!), max||B_ic||op<=h and r_*=max r_p. This has total coarse
order six AND source order four, not total mixed order four.

For Gamma use the actual complex paths

    V(t)=exp(t_m B_m)...exp(t_1 B_1)V,
    epsilon(s)=epsilon+sum_(j=1)^n s_j xi_j/u,
    |t_i|<=eta/(16m sqrt(N)h), |s_j|<=u rho/(4n r_*).           (BW16)

Absent directions need no radius. The exponential/log series gives
||Log[V(t)V^-1]||HS<=4sqrt(N)h sum|t_i|<=eta/4; sources stay in
rho/2. Thus these are in the SAME admitted outer CW tube. Reversing the
exponential order gives exactly the stated ordered invariant derivative.
Each formal parameter is differentiated once, even for repeated physical
directions. Cauchy therefore gives, for each coefficient envelope e_Y,

    |D_B^m D_J^n Gamma_Y|
       <=e_Y(16m sqrt(N)h/eta)^m(4n r_*/(u rho))^n.             (BW17)

There is no extra m!n!. This checks the group vector-field derivatives,
not just coordinate partials. Put 0^0=1,
P6(x)=sum_(m=0)^6(16m)^m x^m/m!,
Q4(y)=sum_(n=0)^4(4n)^n y^n/n!. WR38 on the narrowed xi=eta gives

    ||B_diag||_(lambda0;6,4;h,r)
       <=A_diag+E_w P6(sqrt(N)h/eta)Q4(r_*/(u rho)),
    A_diag=exp(-kappa_d p_a^2), kappa_d=cN c_q/64.              (BW18)

The A_diag clause holds eventually for any specified polynomial bounds
on h,r_* with volume-independent constants. BW7 keeps its inverse-radius
cost polynomial; WR34--38's actual Taylor/density proof then applies.
No analyticity of a rough moved mean is used. Uniform derivative-envelope
sums prove termwise C^(6,4) on compact subsets of the open real domain.

## 5. Complete label counts, weighted smallness and the precise consumer

A complete original reader Y contains at most 4D|Y| coarse scalar labels
and 6L^4|Y| ORIGINAL plaquette source labels. With an HS-orthonormal
basis, a direction of operator norm h has each scalar component <=sqrt(N)h.
Let T_abs sum all absolute ordered scalar tensors with these weights and
the actual r_p. This dominates the dense-direction T just defined and
any test pairing whose word coefficients are bounded by the product of
these weights; it does not identify every norm called a test-function norm.

For s>0 put B0(s)=1 and Bj(s)=max(1,[j/(exp(1)s)]^j). Since
|Y|^j e^(-s|Y|)<=Bj(s), the exact counts and BW17 give

    C_w(s)=sum_(m=0)^6 sum_(n=0)^4 B_(m+n)(s)/(m!n!)
          *[64m D sqrt(N)h/eta]^m[24n L^4 r_*/(u rho)]^n,
    C_d(s)=sum_(m=0)^6 sum_(n=0)^4
                    B_(m+n)(s)(4D sqrt(N))^m(6L^4)^n,
    ||B_diag||_(lambda0-s;T_abs)<=C_d(s) A_diag+C_w(s) E_w.     (BW19)

For C_w, apply Cauchy to a single HS basis generator, then multiply by
its sqrt(N)h weight and sum its 4D|Y| positions; no second sqrt(N)
factor is inserted. For C_d use WR's uniform derivative envelopes on
single-site directions; its stated enlargement drops harmless factorials.
The largest reader power is ten. Choose s=beta/8, leaving 3beta/8.
Derivatives at labels outside the COMPLETE reader vanish, including for
inactive/tail normalizer readers, which are never replaced by endpoints.

For four labelled profiles xi_i(p)=r_i f_i(p), each source subset B has
factor (4|B|)^|B| product_(i in B)||xi_i||infinity/(u rho) in BW17.
Sum all sixteen subsets, with 1/m! and NO source factorial. The absolute
version retains sum_(p read by Y)|xi_i(p)|, or its upper bound
6L^4|Y|||xi_i||infinity. Repeated original labels remain. The same finite
subset extraction applies to WR's diagonal family. No profile sum is
replaced by one without its specified normalization.

For fixed C_h,C_J, assume h<=C_h sigma and r_*<=C_J u. Under the two
white limits in section 2,

    h/eta<=C_h max{(4K+1)^2/(d_eta sqrt(c_q)p_a),32/p}->0.
                                                                    (BW20)

Thus C_w(beta/8) is eventually at most the explicit fixed constant
obtained from BW19 by replacing h/eta by one and r_*/u by C_J.
C_d is already fixed. Combining BW13 and BW19 proves

    ||B_diag||_(3beta/8;T_abs)
       <=C_beta[ sigma p^3+sigma^2+rho exp(-p^2/64)
                 +p^-1 exp(-p^2/2)
                 +(1+p_a^(91D+2))exp(-a_P p_a^2/64)]
                                      +exp(-kappa_d p_a^2/2).  (BW21)

Constants are independent of T,u after the stated threshold and may
depend on N,L,R,rho,C_h,C_J. This tends to zero and includes the scalar
cutoff normalization. With h=1 the explicit BW18--19 bounds still hold,
but their white sixth-order cost can destroy smallness. No unscaled
small-jet statement is inferred. For a next-level weight h=sqrt(N/u'),
h/eta contains sqrt(u/u'); the needed lower bound on u'/u is an
additional coupling-flow input. Source-normalized BW15 subtracts its
value at epsilon=0 exactly as BW14; the same jet bound with twice the
nonconstant right side suffices, and positive source orders need no doubling.

This supplies a concrete SMALLER-RATE integrated finite-jet consumer.
If the BW19 bound B at lambda=3beta/8 is <=beta/128, put
k_Y=exp(B_diag,Y)-1, keeping the labelled family and singleton scalar.
Ordered Leibniz on the (6,4) rectangle, also after absolute weighted
word summation, gives T(FG)<=T(F)T(G) and
T(k_Y)<=exp(T(B_diag,Y))-1. The actual product representation has
A_I=product_(Y in I)k_Y, A_empty=1 and exact overlap factorization;
its input sum Q_lambda<=exp(B)B<=beta/64. Two rooted overlap/log
recursions with losses beta/16 each therefore give output rate beta/4.
Indeed a neighbor sum <=Q_lambda|Y| fits each available beta/16;
the Kruskal tree partition bounds the signed connected graph sum, and
the same absolutely convergent series with activity multiplier |z|<2
proves nonvanishing. The finite ordered Leibniz bound passes all included
jets through those sums. This is WR43--45 instantiated by the ACTUAL
already integrated cut/white coefficients, not a new interacting estimate.

The native [REALRGA](REALRGA.md) input exp[(mu+2)|Y|], its retained
fine/coarse jets and RGA14 joint reference/regulator estimate are NOT
supplied by the much smaller beta/2 starting rate. Nor does this output
identify STEP55's white su(N) BALL, slice covariance, Ward identity,
inherited effective interaction or scale-uniform H1--H4. BW11 retains
the full extensive prefactor; these estimates do not perform its Wilson
extraction, determinant matching through scales or coupling flow.

On real admitted data the literal identity remains
Z_cut=Z_Omega+I_(G minus Omega)+I_(G^c). BW10/15 bound its TOTAL
cut/white logarithm. They do not separately return these two histories,
construct arbitrary conditioned denominators, estimate retained fine or
rough boundary jets, or close the all-history/effective iteration.
At complex V only BW3's white chain and BW2's actual cut integral are
used; no G/Omega complement predicate is transported. Non-free continuum
existence and the positive physical continuum mass gap remain OPEN.

This source is frozen before its compact author provenance. A DIFFERENT
fresh hostile review is required. No scientific numerical runs, extra
workers, predecessor/shared-front/Git/PR/audit edits occur in this unit.
Root owns publication; metadata checks provide no proof or audit status.
