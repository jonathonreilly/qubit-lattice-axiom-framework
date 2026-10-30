# Exact compact-minus-chart assembly and real-buffer marginal bounds

This proves an exact simultaneous expansion of the supplied four-dimensional
SU(N) original-cut partition function about ONE actual original-a chart.
The all-good cap is eliminated by summing unselected chart histories, not
by replacing that cap by the chart. Selected compact-minus-chart insertions
retain their actual good annuli. Overlapping absence readers are grouped
before exterior integration. A signed Schur-complement estimate then bounds
arbitrary joint moments of these insertions in the normalized complex chart,
at a cost proportional to their buffers rather than the ambient volume.

The resulting object is a correlated chart expectation. A complete-reader
connected logarithm for its bounded, real-buffer insertions is NOT proved
here. The exact representation is proved at real coarse centers with a
fixed complex original-source radius. A narrower complex coarse tube also
supports the marginal estimate and an explicit unresummed identity, but
does not transport the resummed hard domains automatically. The original
G, white Omega, and their two complements stay distinct. Full non-free
continuum existence and a positive physical continuum gap remain OPEN.

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

Bałaban's localization and large-field work, and Dimock's expositions, are
the constructive antecedents. Every new finite-dimensional step is rebuilt
below. No scalar or three-dimensional cluster theorem is imported into the
four-dimensional nonabelian model.

## 1. Fixed sources, genuine chart references, and original predicates

Use the exact density and pinned-tree quotient in
[SC1--SC6](SOURCE_LOCAL_COMPACT_RETURN_ASTRA.md), with SC frozen at SHA256
`c39e78ac1d31024d5266e16ace022fa86497a6d09c45aa25b215ffa390533dff`.
Use the SAME ambient RF/RC family and
[MR](MATCHED_REGIONAL_RATIO_ASTRA.md), frozen at SHA256
`5f27e55375d59dde30eacb91efce42a16ba266d563833db2ffd5babdd14c4af6`.
RF and RC are respectively frozen at
`45a5665fc51683f026370e774ca8590b221bc5c9e13c07502225226cb13c962b` and
`b098d18ad22946d7b1e0a4d497e0b5d98250674e06803263d1106f14bf659094`.
The inputs are their mathematics; review verdicts are provenance only.

Write Lattice for the T^4 coarse blocks and E for all free WHOLE links.
Here N>=2, odd L>=3, T>=2, D=N^2-1, m0=3L^4+1, n0=D m0,
sigma^2=N/u, and every source epsilon_p labels its ORIGINAL Wilson term.
The supplied density is

    w_epsilon(U,V)=exp[-u sum_p(1+epsilon_p)s(U_p)]
                        product_c exp[t h(V_c,M_c(U))]/Z_t(M_c(U)),
    t=kappa u, s(P)=||I-P||HS^2/(2N),
    M_c=(24L^4)^-1 sum_tau P_(c,tau)(U).                 (CG1)

On real fields h=Re tr(V* M)/N; complex continuation uses the original
paired inverse-edge expressions. All kernel normalizers, finite-u spread,
Haar factors, roots, winding variables and colours remain. Nonroot gauge
Haar volume is exactly one. There is no further gauge deletion.

Fix a real center Vbar, U0=U0(Vbar), and SC's q,K,c,alpha,V_K,p0,p1.
Use the positive source radius rho of SC20, fixed BEFORE u. All q-good
tests below mean the literal original chord test

    Q_X=sum_(f owned X)||U_f-U0_f||HS^2/N < q.           (CG2)

It supplies whole-link principal logarithms of norm <=zeta/16 by SC6.
This is smaller than RF's boundary radius zeta, which is itself smaller
than RC's active chart radius r_a. They are not interchangeable thresholds.
Keep SC12, SC24 and every RF/RC force, tail and contour restriction.
Let C_a(Vbar) be the product of all ORIGINAL whole-link balls B_ra in
a_f=log(U_f U0_f^-1). Impose 4r_a<epsilon_1, as in SC3. Then C_a is a
subset of the original INTERIOR-plaquette cut. Define

    Z_a(Vbar,epsilon)=int_(C_a(Vbar)) dH_E w_epsilon,
    nu_a(dU)=Z_a^-1 1_(C_a(Vbar)) w_epsilon dH_E.       (CG3)

RC for Lambda=E proves Z_a nonzero on |epsilon_p|<rho, including its
complete critical action, Gaussian dimension, determinant and chart log.
nu_a is a complex measure at complex sources; its variation is not one.

chi_cut still restricts only internal block plaquettes. G still requires
ALL fine plaquettes to have defect <delta_f and every actual root-straight
transporter to differ from Vbar_c by <eta_G. Omega is the unchanged
source-free WHITE scalar cube a=b_0+sigma C_0 w, |w_i|<=p_Omega.
Whenever complements are discussed, impose the old Omega subset G subset
cut margins and SC35's all-q-good subset Omega margin. In particular

    Z_cut=Z_sec+I_(G minus Omega)+I_(G^c).               (CG4)

C_a is neither Omega nor G. No identity between their partition functions
is inferred from their containing a neighborhood of the same critical point.

## 2. A simultaneous partition with each physical factor assigned once

Increase the component graph range, while leaving the q,K shell scale
unchanged, to

    r=4K+4, d=r+2,
    H_K=(2r+1)^4=(8K+9)^4,
    W_K=(2d+1)^4=(8K+13)^4.                            (CG5)

Decompose the exact q-bad set into its connected components A in this
range-r graph. Distinct components have distance >r. For each component
use I_j=N_(2j)A, R_j=N_(2j+1)A and S_j=N_(2j+2)A minus R_j, and its
FIRST successful shell Q(S_j)<=alpha Q(I_j), 0<=j<K. SC's compact growth
proof applies to ANY nonempty A: failure at every shell would give
Q(N_(2K)A)>(1+alpha)^K q|A|, whereas compactness gives
Q(N_(2K)A)<=4m0(4K+1)^4|A|. SC7 chooses K so that
(1+alpha)^K q>4m0(4K+1)^4, a contradiction.
Wrapped neighborhoods only reduce these cardinalities.

A history h is a finite unordered collection of pairs (A,j), with each A
range-r connected and pairwise distance >r. Put R_h=union_(A,j in h)R_j,
O_h=Lattice minus R_h. For fixed j define the LOCAL selector

    ell_Aj=1_(all X in A:Q_X>=q) 1_(all X in R_j minus A:Q_X<q)
       times 1_(Q(S_j)<=alpha Q(I_j))
       times product_(i<j)1_(Q(S_i)>alpha Q(I_i)).       (CG6)

All earlier tests use active variables in R_j. The current shell uses the
fixed exterior S_j. Unlike SC8, CG6 does NOT contain a long component-
absence predicate. For a full history the exact selector is

    Pi_h=1_(all X in O_h:Q_X<q) product_(A,j in h)ell_Aj,
    sum_h Pi_h=1.                                      (CG7)

Indeed CG7 fixes the bad set to union A, these A are exactly its range-r
components, and selects precisely one successful shell for each. The empty
history is the all-good cap. Q=q is assigned to bad, so no boundary of a
hard predicate is silently omitted.

Since 2j+1<=2K-1, distinct R_j have distance at least seven. Their
N_1 physical neighborhoods are disjoint. Thus no original plaquette,
normalized kernel, or root-straight criterion can read two active regions.
Assign every physical factor touching J_Rj to w_Rj, and every other
factor to W_out,h. Internal cuts belong to their owner block. Exactly

    chi_cut w_epsilon=chi_(O_h) W_out,h
                         product_(A,j in h) chi_Rj w_Rj.             (CG8)

This uses the actual N_1 field stencils, not enlarged covariance readers.
All sources and every cross-boundary factor occur once. The N_(2K+4)(A)
coefficient readers can overlap; CG8 does not assert their disjointness.

For real exterior z q-good on S_j, define

    N_Aj^c(z)=int_(SU(N)^J_Rj) dH chi_Rj ell_Aj w_Rj,
    N_Aj^a(z)=int_(C_a on J_Rj) dH chi_Rj ell_Aj w_Rj,
    B_Aj^c=N_Aj^c/I_Rj, B_Aj^a=N_Aj^a/I_Rj,
    D_Aj=(N_Aj^c-N_Aj^a)/I_Rj.                         (CG9)

I_Rj is SC3's actual touching-factor chart fibre with that SAME exterior,
sources and u. In N^a the chart is centered at U0(Vbar), just as in CG3.
For complex coarse data a frozen-chart variant will be named explicitly
in section 8. No denominators are evaluated outside the q-good boundary
domain; a local function can be extended by zero there.

The numerator of D is the actual compact slice outside the active product
chart, with chi_Rj ell_Aj retained. Its pointwise majorant is a restriction
of the N^c majorant. Thus no factor two is needed. Recheck the modified
selector against SC's proof: it supplies A-bad, the first payable shell,
and q-good touching boundary. SC11 uses no further absence test. Its
reset inequality E_R-2A_ref>=c Q(I_j)/2, source debit SC21 and coarse debit
SC24 therefore hold unchanged. The complete prefactor bound SC28 gives

    |B_Aj^c|, |B_Aj^a|, |D_Aj| <= b(A),
    b(A)=exp{[p0+p1 log(1+u)]V_K|A|-c u q|A|/2}.       (CG10)

These are bounds on the original finite Haar integrals. In particular
|D| is bounded by applying SC to its restricted numerator, not by
subtracting two unnormalized absolute action estimates. Each D reads
fine exterior variables only in S_j and original continuous/membership
data in N_(2K+4)(A). Its source derivative outside P_Rj is zero.

Integrating CG8, then conditionally integrating the unused regional chart
variables in CG3, proves the two EXACT simultaneous identities

    Z_cut/Z_a = sum_h < 1_good(O_h) product_h B_Aj^c >_a,
            1 = sum_h < 1_good(O_h) product_h B_Aj^a >_a.             (CG11)

The outside cut is satisfied on the good exterior; it is also satisfied
on all chart variables by 4r_a<epsilon_1. The product of conditional
I_Rj factors is obtained from the actual global chart density because
their touching physical sets are disjoint. It is not an arbitrary base
measure. Empty history contributes Z_good/Z_a in BOTH lines, not one.
Subtracting CG11 retains the cap correction exactly.

## 3. Sum the unselected chart histories before taking absolute values

Expand B^c=B^a+D in the first line of CG11. For a selected family s of
D-cores put

    R_s=union_(A,j in s)R_j,
    H_s=(union_(A,j in s)N_r(A)) minus R_s,
    Theta_s=1_good(H_s) product_(A,j in s)D_Aj.          (CG12)

Theta_empty=1. These are FUNCTIONS on the global chart variables; they
are independent of all dummy variables in R_s. The q-good constraint on
H_s guarantees every S_j boundary. Crucially, ALL selected regions are
removed from the annuli, not only the region of the same component.

For fixed s, sum the unselected chart histories as follows. First
conditionally integrate the chart variables in R_s; every D depends only
on S_j, disjoint from any other active region. This supplies product I_Rj
and leaves the actual chart density on the remaining variables. In that
density require q-good on H_s. Every remaining bad component B is then
at distance >r from each selected A. Its R_k and S_k are disjoint from
R_s, so its first-shell selection is the original one on its actual
variables. Conversely every history h containing s supplies exactly such
a remaining component configuration. The unselected chart numerators
N_Bk^a and the final sea cap integrate its exact partition CG7.

There is one necessary intersection check. N_r(A) can meet an unselected
R_k even though the physical factor sets are disjoint. No bad core B lies
in this intersection: distance(A,B)>r. Hence the intersection is contained
in R_k minus B, on which ell_Bk already enforces q-good. Retaining that
absence condition during the sum makes no change. For another SELECTED
R_k it must instead be deleted from H_s, since its actual good-buffer
condition is already inside D_Bk and its chart variables are dummy.
Leaving the condition on those dummy variables would replace I_Rk by a
smaller capped integral and invalidate cancellation.

More explicitly, for EACH fixed selected s the preceding bijection proves

    sum_(h contains s)<1_good(O_h) product_s D_Aj
                                  product_(h minus s) B_Aj^a>_a
                         =<Theta_s>_a.

This proves the resummation, including the empty family,

    Z_cut/Z_a = sum_(s pairwise distance>r) <Theta_s>_a.               (CG13)

All sums are finite at fixed volume, so this algebra uses no convergence
or positivity. It holds for every complex original source in the admitted
disc at real Vbar. It genuinely removes the ambient sea cap: only the
explicit local annuli H_s remain. It does not drop a hard constraint
inside a complex expectation.

To express CG13 with fixed local insertions, give each selected core the
complete reader Gamma_A^+=N_d(A), d=r+2. Partition the selected cores
by OVERLAP of these readers. A group g retains its list (A,j), not merely
its union. Define

    A_g=union_g A, n_g=|A_g|, Gamma_g=union_g Gamma_A^+,
    R_g=union_g R_j, H_g=(union_g N_r(A)) minus R_g,
    Theta_g=1_good(H_g) product_g D_Aj.                 (CG14)

All constraints in CG14 are internal to Gamma_g. If an R_j from one group
could meet another's absence annulus, their Gamma^+ would overlap, so they
would be the same group. Similarly any range-r incompatibility between
two cores forces their Gamma^+ to overlap. Consequently disjoint groups
reconstruct exactly one admissible selected family, with
Theta_s=product_g Theta_g and Gamma_g connected. Thus

    Z_cut/Z_a = < sum_(groups with disjoint Gamma_g)
                              product_g Theta_g >_a.                 (CG15)

This is the promised exact representation with ONE matched chart reference.
Its insertions have full original readers Gamma_g and an actual bounded
real buffer H_g. Their supports obey

    |R_g|<=V_K n_g, |H_g|<=H_K n_g, |Gamma_g|<=W_K n_g,
    ||Theta_g||infinity<=exp{[p0+p1 log(1+u)]V_K n_g-c u q n_g/2}.
                                                                  (CG16)

Neither products over overlapping fibres nor deletion of an annular
predicate was used. The original regional normalization and the source
labels survive the resummation.

## 4. A signed normalized chart marginal for a real small buffer

Let B be ANY deterministic block set and pin all J_B to real physical
values z with Q_X<q on B. At complex V=exp(v)Vbar use the fixed physical
z and set xi_f(V)=log[z_f U0_f(V)^-1]. Denote RC's full physical Haar
chart fibre on A=E minus J_B by Z_A^H(V,epsilon;z), including every
outside physical factor, as in MR5. Define the normalized HYBRID functional

    L_B(f)=Z_E^H(V,epsilon)^-1
        int_(all X in B:Q_X<q) dH_J_B(z) f(z)
                                   Z_(E minus J_B)^H(V,epsilon;z).
                                                                  (CG17)

For V=Vbar, this is exactly <1_good(B) f>_a. At complex V it keeps B
real and uses the transported original-a chart only on its complement.
It is not claimed to be a marginal of the fully transported chart on a
transported hard cap. The fixed-domain functional is holomorphic in V and
epsilon for bounded parameter-holomorphic f; the following bound supplies
the needed domination. Rough compact variables inside f remain real.

Fix preliminary constants before q,K,u. SC14 supplies on the entire fine
cube used below, for the FULL actual phase F=F_epsilon,

    Re F'' >= lambda I, ||F''||op<=B_*,
    lambda=gamma/2, B_*=B_RF+gamma/2,
    C_b=2 sqrt(D) A_G g_*(1+rho_0),
    max_f ||b_E,f||HS<=C_b delta_hat, delta_hat=delta+8eta_c.          (CG18)

The first two bounds are pointwise row-and-column Taylor bounds before
principal restriction, as justified in SC14--SC15. They do not assign
a reader norm to a fixed field. The last line is RF20 with Y=0 plus the
scalar-to-whole-link sqrt(D). Impose the additional explicit restriction

    C_b delta_hat <= zeta/8.                            (CG19)

The weaker bound b_E<=tau alone would not suffice here. By SC6 and MR3,
||bar xi_f||HS<=zeta/16 and ||xi_f(V)||HS<=zeta/2. Therefore the ENTIRE
segment z_s=(1-s)b_E|J_B+s xi(V) lies in the RF boundary tube. RF supplies
b_A(z_s), all its points remain in the same fine cube, and at s=0 its
uniqueness gives b_A(b_E|J_B)=b_E|A. No regional reference is changed along
this argument. All source values and all finite-u kernel/Haar terms stay.

Use the full analytic phase on E, with B pinned to an arbitrary coordinate
zeta_B in that segment's domain, and write

    f_B(zeta_B)=F(b_A(zeta_B),zeta_B),
    S_B=f_B''=F''_BB-F''_BA (F''_AA)^-1 F''_AB,
    M=B_*+B_*^2/lambda.                                (CG20)

Stationarity in A proves the displayed derivatives and
f_B'(b_E|J_B)=0. Every Hessian block in CG20 is evaluated at the same
(b_A(zeta_B),zeta_B). For a complex vector h_B set
h_A=-(F''_AA)^-1 F''_AB h_B. Then
h* F'' h=h_B* S_B h_B, since the A component of F''h vanishes.
CG18 proves Re S_B>=lambda I and ||S_B||op<=M. This proves the Schur
bound directly, with no Gaussian-marginal precision identification.

The holomorphic Hessian is symmetric, so for real x,y

    Re (x+i y)^T S_B(x+i y)
       >=(lambda/2)||x||2^2-(M+2M^2/lambda)||y||2^2.

The estimate is Young's inequality on the cross term, followed by CG20.
Taylor integration on the segment, with
C_s=M/2+M^2/lambda, therefore gives the SIGNED action inequality

    Re[f_B(xi)-F(b_E)]
       >=(lambda/4)||Re(xi-b_E|J_B)||2^2
                                      -C_s||Im(xi-b_E|J_B)||2^2.     (CG21)

For real V this has a negative Gaussian penalty in the actual pinned
field, with adverse cost only C_s m0 C_b^2 delta^2 |B|. There is no
positive u q |B| debit. This is why MR's symmetric absolute action bound
is not used in the marginal estimate.

For the stated complex tube one also needs actual coordinate control.
At a crossing link xi=log(exp(bar xi)exp(-v_c)); at other links it is
bar xi. On zeta<=1/4 and eta_c<=zeta/16, the logarithm power series and
||D exp(-s v)[v]||<=2||v|| give

    ||xi-bar xi||HS<=4eta_c.

Indeed the matrix argument stays within distance 1/2 of I, where the
HS derivative norm of log is <=2. Using eta_c<=delta_hat/8 in CG21 gives

    Re[f_B(xi)-F(b_E)]
       >=(lambda/8)||bar xi-Re b_E|J_B||2^2
                                      -m0 C_A delta_hat^2 |B|,
    C_A=lambda/16+C_s/2+2C_s C_b^2.                    (CG22)

Every constant here is fixed on the preliminary RF/RC tube and contains
no inverse actual zeta, q, or u.

## 5. Exact dimension, determinant and inactive-Haar cancellation

Apply MR5 to Lambda=E and Lambda'=E minus J_B with the SAME physical
template z on J_B. All changed links are small, and both touching
boundaries are small; there is no rough changed-link comparison. There
is no common rough exterior when Gamma=E. Its exact quotient is

    Z_(E minus J_B)^H/Z_E^H
      =h_N^(-m0|B|)(2pi sigma^2)^(-n0|B|/2)
       times exp[-(LogDet K_A^*-LogDet K_E^*)/2]
       times exp[-(f_B(xi)-F(b_E))/sigma^2]
       times exp(H_A-H_E) / product_(f in J_B)j_N(xi_f).              (CG23)

The inactive-Haar denominator is essential. MR13's canonical agreement
gives |(LogDet K_A^*-LogDet K_E^*)/2|<=C_det |B|, with C_det EXACTLY
MR12, including its full finite homotopy and critical trace series.
MR16 similarly gives |H_A-H_E|<=2epsilon_ch |B|. The proof sums each
anchored difference over changed owners; no total-volume log is bounded
twice. These bounds hold on the same ambient family and original sources.

Multiplication by physical Haar measure
dH_J_B=h_N^(m0|B|) product j_N(bar xi_f) d bar xi cancels h_N exactly.
At real V the j_N factors also cancel exactly. At complex V the ACTUAL
remaining ratio is product j_N(bar xi)/j_N(xi(V)), not one. MR15 gives,
for a fixed preliminary ceiling bar zeta<=1/4,

    |product j_N(bar xi)/j_N(xi)|<=exp[m0 D bar zeta^2 |B|].

Insert CG22 into CG23 and enlarge the real cap integration to all of
R^(n0|B|) only in the resulting positive Gaussian majorant. The Gaussian
integral cancels sigma^(-n0|B|), leaving the finite factor
(4/lambda)^(n0|B|/2). Thus

    |L_B(f)| <= ||f||infinity exp{[C_0+C_1 u delta_hat^2]|B|},
    C_0=C_det+2epsilon_ch+m0 D bar zeta^2
                           +(n0/2)log max(1,4/lambda),
    C_1=m0 C_A/N.                                      (CG24)

For a bounded complex measure density the same calculation with |f|<=1
is its total-variation bound, not merely a cancellation estimate for one
test function. Its constants are uniform in B,T and the shape of holes.
The empty-buffer case is one. No u-dependent Gaussian dimension factor,
determinant, Haar term or constant kernel vacuum has been discarded.
For real V one may improve the constants using CG21, but CG24 is convenient
on the common narrow tube. Only complement chart variables were deformed;
no fine input of a rough kernel inside a compact insertion was moved.

## 6. Joint insertion bounds and a summable geometric majorant

Apply CG24 at Vbar to a disjoint family of groups. Let B=union_g H_g
and f=product_(g,A,j)D_Aj. This reproduces exactly their joint chart
moment, since all q-good restrictions in Theta_g are precisely the cap
on B. No ambient sea remains. Impose, in addition to SC12 and CG19,

    delta_hat^2 <= c q/(8 C_1 H_K).                     (CG25)

The physical curvature restriction can always be further reduced by
this fixed constant. It has the same q/K^4 order as SC12. Equations
CG10, CG16 and CG24 now prove, for every such family at real Vbar,

    |<product_g Theta_g>_a| <= product_g a(g),
    a(g)=exp{[p(u)V_K+C_0 H_K-3c u q/8] n_g},
    p(u)=p0+p1 log(1+u).                               (CG26)

The same bound holds for its explicitly defined CG17 hybrid functional
at complex V in SC24 with CG19/CG25, using the fixed-real-chart variants
of the compact insertions. That hybrid bound is not a transported CG15.

There is a finite, uniform entropy estimate. Each A_g is connected in
the graph of range 2d=8K+12: a contact of Gamma_A^+ and Gamma_B^+
joins core vertices at that range. Its degree is at most
Delta=max(1,(16K+25)^4-1). A connected n-set through an owner has at most
Delta^(2(n-1)) choices by deterministic spanning-tree traversal. Given
A_g, its range-r components are the UNIQUE original cores A, so there is
no extra set-partition entropy. The shell choices cost at most K^n.
A mark in Gamma_g has at most W_K choices of a nearby core anchor.
Therefore, for any fixed mu>=0 and

    t=K exp{mu W_K+p(u)V_K+C_0 H_K-3c u q/8},

the geometric majorant satisfies

    sup_x sum_(g:x in Gamma_g) exp(mu|Gamma_g|) a(g)
                      <=W_K t/(1-Delta^2 t),  Delta^2 t<1.           (CG27)

This is a bound on the local insertion labels and the joint-moment
majorant. It is NOT a claimed reader expansion of <Theta_g>_a: that
normalized moment can depend on sources and coarse data arbitrarily far
away through the chart correlations. Those additional readers have not
been erased by assigning it the smaller label Gamma_g.

The parameter domain is nonempty. Choose all preliminary RF/RC constants,
then r_a,tau,zeta and fixed rho as in SC. Pick q>0 satisfying SC5, compute
K, and reduce delta and eta_c to meet SC12, SC24, CG19 and CG25. All are
strict positive upper bounds; flat real coarse centers are available.
Choose u large enough for RC and CG27. For SC33's shrinking family,

    r_a=sigma p, zeta=c_z sigma p, q=c_q sigma^2 p^2,
    p=(log(2+u))^alpha_cut, alpha_cut>5/2,

one has K=O(log u), V_K,H_K,W_K=O((log u)^4), and u q=N c_q p^2.
CG19 holds eventually after the curvature constant is reduced, because
delta_hat/zeta=O(K^-2). CG25 keeps delta=O(sigma p/K^2) with a smaller
fixed constant, and SC24 retains eta_c=O(sigma^2 p^2/K^4). The positive
logarithm of CG27 is O((log u)^5), so eventually

    CG27 <= exp[-c N c_q p^2/16].                      (CG28)

The source radius remains fixed. Ordinary finite-order derivatives of
the LOCAL coefficients and HYBRID functionals on half their tubes obey
Cauchy bounds with factors alpha! nu! (2D/eta_c)^|alpha|(2/rho)^|nu|.
Local D coefficients have zero derivatives outside their actual readers;
normalized chart moments do not have that vanishing property. This gives
no wider D_* tube, uniform unscaled coarse jets, or inherited RG norm.

## 7. Original complements, positivity, and the first connected gap

At real sources all D_Aj>=0, because CG9 subtracts a subset of the same
compact integral. Thus CG15 and CG26 imply the finite-volume real pressure
bound, writing s for the right side of CG27 at mu=0,

    0 <= (1/T^4)log(Z_cut/Z_a) <= s.                    (CG29)

Indeed discard group compatibility only in the positive majorant, bound
the sum by product_g(1+a(g))<=exp(sum_g a(g)), and use
sum_g a(g)<=T^4 s. This is a one-step pressure comparison, not a mass gap.
For complex sources the same argument bounds an absolute series by
exp(T^4 s); it does not give nonvanishing or a local logarithm.

For the TWO unchanged complementary events let P be either
1_(G minus Omega) or 1_(G^c), evaluated at real Vbar. Define for each
history h the joint conditional observable

    C_h[P](z)= [product_h I_Rj(z)]^-1
       int_(product_h SU(N)^J_Rj) product_h[dH chi_Rj ell_Aj w_Rj]
                                      P(U_(R_h),z).                 (CG30)

This integrates the exact original predicate, including every original
white-coordinate reader when P uses Omega. The simultaneous factorization
CG8 proves

    I_P/Z_a = sum_(h nonempty)<1_good(O_h) C_h[P]>_a,
    |C_h[P]|<=product_h b(A).                          (CG31)

The inequality follows from the same disjoint pointwise energy payments
as CG10 and |P|<=1, not from fictitious independent predicates. The empty
term vanishes by all-q-good subset Omega subset G. CG31 is an exact
complement identity, but it need not factor into local insertions: Omega
is the source-free white cube and its actual readers are retained.

There is a useful optional local refinement for G alone. Impose the actual
strict margins delta+4r_a<delta_f and (5L)r_a<eta_G. Then the whole chart
lies in G. A G criterion whose field stencil misses R_h is automatic on
the q-good sea. Assign each remaining original plaquette/straight-path
criterion to the unique R_j it touches. Their physical stencils are in
N_1(R_j), so this assignment is unique. Insert those criteria into N^c
to obtain N^G; N^a is unchanged, and D^G=(N^G-N^a)/I_R satisfies CG10.
The same proof gives a CG15 expansion of Z_G/Z_a with D^G. Subtracting
the two exact group sums represents I_(G^c)/Z_a. This still does not
replace G minus Omega by an original-a annulus; its remaining reference
is the actual Z_sec. No new meaning of G or Omega has been introduced.

The FIRST unproved connected estimate after CG15 is now precise. One
needs a convergent complete-original-reader construction of the truncated
chart expectations of these bounded measurable, real-buffer insertions,
with a rooted sum of connected coefficients of order CG28. Joint bounds
CG26 alone do not imply such a statement. To see the logical gap, let
many disjoint formal local labels all equal the SAME Bernoulli(1/2) variable
X, times a small parameter z. Every joint moment has modulus <=|z|^k,
yet E product_(i=1)^m(1+zX)=[1+(1+z)^m]/2 has zeros approaching z=0
as m grows. This is not a Yang--Mills counterexample; it shows why a
joint-moment bound without spatial connectedness cannot prove a uniform
zero-free disc or a local pressure expansion.

A concrete route is the actual Gaussian density forest of
[SN sections 6--10](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md), with RC's
regional coefficient choices. A group would be a new bounded bulk
primitive, with all H_g variables retained REAL. Only its complement
could be translated. Then the Gaussian translation has support on H_g
as well as the old side spheres; its full b-reader attachments and mixed
density jets must be paid at C u delta^2|H_g|, not C u tau^2|H_g|.
Nonlinear vertices touching that buffer keep the same physical fields,
and the primitive-group/presence/absence constraints must remain internal
before the forest. SN presently proves the old vertex/side/bad species,
not this additional bounded bulk species. Its required mixed-jet and
marked-incidence extension has not been proved in this unit. There is no
import of its conclusion with the new species silently inserted.

MR's absolute action budget is not an adequate substitute: in the
shrinking family it can cost O(p^2) per changed buffer owner, yielding
O(K^4 p^2 n_g), whereas the compact reserve is O(p^2 n_g). CG21--CG24
remove that obstruction for joint marginals, but do not by themselves
construct the required connected-reader coefficient cancellation.

## 8. What is exact on the narrower complex coarse tube

Keep every physical fine numerator variable REAL and every selector
frozen at Vbar. Let Z_a^fr(V,epsilon) integrate the fixed physical chart
C_a(Vbar), while Z_a(V,epsilon)=Z_E^H denotes RC's transported original-a
chart. Define N_Aj^(a,fr) and D_Aj^fr with that fixed physical local
chart in CG9; their CG10 bounds use SC24's original
fixed-positive-normalizer proof. The original chi_cut is V-independent;
it is not changed into a moving coarse predicate.

The exact fixed-domain unresummed identities on SC24 are

    Z_cut/Z_a = sum_h L_(O_h)(product_h B_Aj^c),
    Z_a^fr/Z_a = sum_h L_(O_h)(product_h B_Aj^(a,fr)).   (CG32)

Here L_(O_h) uses the actual joint chart on R_h. CG8 proves that its
conditional fibre is W_out,h product_h I_Rj with the identical exterior
physical Haar variables and factors. Consequently

    Z_cut/Z_a=1+Delta_chart
       +sum_(h nonempty) L_(O_h)
                   [product_h B_Aj^c-product_h B_Aj^(a,fr)],
    Delta_chart=Z_a^fr/Z_a-1.                           (CG33)

At V=Vbar, Delta_chart=0 and sections 2--3 perform the exact resummation.
At complex V, CG33 keeps the contour-domain correction visible. The
fixed-chart resummation can still be done BEFORE normalization, but its
remaining fine contours are fixed at Vbar, not those of CG17. Replacing
them by the transported chart would require their actual boundary fluxes
and any retained hard-domain corrections. CG24 does not prove that
replacement. Setting Delta_chart=0 by fiat, or equating a frozen
Omega(Vbar) continuation with the transported original Z_sec(V), would
be a new unproved identity. The same distinction applies to the original
G/Omega predicates in CG31.

The linear coarse width remains SC24's eta_c=O(q/K^4), with CG19/CG25
only further restricting its constants. No larger coarse domain is used.
In particular, a coarse-dependent change of rough physical fine variables
inside a compact kernel would move its mean and lose the fixed positive
normalizer premise. This unit never makes that change.

## 9. Scope, literature check and review boundary

The new proved steps are CG7--CG16's exact simultaneous and resummed
assembly, CG20--CG24's signed real-buffer marginal estimate, CG26--CG28's
joint-moment majorant with its explicit payment, and the literal original-
complement and coarse-contour identities CG30--CG33. They address actual
factors of the supplied bare density. The first remaining connected-forest
estimate and coarse-domain correction are stated above rather than
renamed as hypotheses of an allegedly completed return theorem.

[Dimock, arXiv:1212.5562v2, sections 3.13--3.14](https://arxiv.org/html/1212.5562v2#S3.SS13)
first localizes the fluctuation
integrand and then applies a cluster expansion with holes under specified
analytic bounds and an ultralocal fluctuation measure. That paper treats
scalar phi-four in d=3; it does not supply the bounded-buffer density
forest or the rough-kernel contour return needed here. Its retained
boundary terms motivated the explicit annular bookkeeping. Bałaban's
[large-field localization paper](https://doi.org/10.1007/BF01238433) is
credited as an antecedent; its full text was not recovered in the earlier
web attempt and no theorem from it is a premise. No priority claim is made.

This is a single BARE step. No arbitrary future-conditioned kernel product,
effective Wilson replacement or inherited-history normalization appears.
The full RD4 interface, actual source-local connected compact return,
wider RG-domain matching, non-free continuum existence and positive
physical continuum mass gap remain OPEN. The current source does not
update any retained/audit status.

No scientific numerical experiment, Git/PR mutation, shared-front edit,
predecessor edit or audit/ledger edit is part of this author unit.
The mathematical source is frozen before its compact
[read manifest](checks/compact_return_gluing_read_manifest.json) and
[receipt](checks/compact_return_gluing_receipt.json).
[PROCESS_LIGHT](PROCESS_LIGHT.md) requires a DIFFERENT fresh hostile
reviewer. Particular review targets are the fixed-history resummation,
removal of other selected R's from H_s, all Schur-segment domains, exact
Haar/dimension cancellation, and the distinction between joint moments
and connected-reader bounds. Root owns review and integration.
