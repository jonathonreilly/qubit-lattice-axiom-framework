# Smooth shell weights and charged retained-field conditional returns

This constructs a source-local, jointly differentiated conditional return
on the ACTUAL original-cut compact law. Its numerator can contain bounded
finite-real-jet insertions, including functions not analytic in the fine
variables. One charged bad core pays the common density/normalizer bill
and an explicit allowance for its attached inputs. The conditional
coefficients have the native REALRGA support reserve mu+2. Both original
source-free and same-source conditional denominators are distinguished.

The new representation replaces ONLY an auxiliary first-success shell
choice by a C^6 partition. Its sum is exactly one on the same bad-core
event. Original cuts, kernels, sources, Haar measure, outside factors and
previous histories are unchanged. Whole-block conditional cancellation
is proved before retained-field jets; zero outside fibres are not divided
by. The remaining integration of the outside law is displayed explicitly.
This is not a completed global R_h/Z_A expansion or an invariant RG class.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

Bałaban's large-field localization and Dimock's exposition are antecedents.
No scalar/d=3 conclusion is imported. The finite-jet norm of
[REALRGA](REALRGA.md), RGA3/RGA14, and the actual positive quotient scores
of [MIXSMALL](MIXSMALL.md), MS4--MS9, are rebuilt at the needed scope.
The local charge and cap are the actual word estimates of
[CS](CUT_SECTOR_COERCIVITY_ASTRA.md)/[OC](OUTSIDE_CHART_RETURN_ASTRA.md),
not a Gaussian probability estimate. The novelty is their simultaneous
retained-field/source use with the smooth payable-shell partition and
the source-FREE reference, including a concrete mixed input allowance.

## 1. Literal reference, retained variables and complete factors

Fix the supplied d=4 SU(N) model, N>=2, odd L>=3, finite periodic coarse
torus of side T>=2, u>=N and kappa in its admitted positive interval.
Set D=N^2-1, m0=3L^4+1, sigma^2=N/u, t=kappa u. Work in CS4's EXACT
root-pinned block-tree quotient, with all m0 free positive whole links
per block. Nonroot gauge Haar volume is one; roots, winding and every
colour remain. This conditional is in the free-link quotient. It is not
identified with fixing the ungauged fine exterior before taking that
quotient. No metric-slice/Gram determinant is silently introduced or removed.

Write J_p=u epsilon_p in ORIGINAL absolute Wilson-source units. All kernels,
their normalizers, u and kappa stay fixed when J is differentiated. Let

    w_J(U,V)=exp[-sum_p (u+J_p)s(U_p)] product_c k_t(V_c;M_c(U)),
    s(P)=1-Re tr(P)/N, k_t(V;M)=exp[t Re tr(V* M)/N]/Z_t(M),
    Z_t(M)=int_SU(N) exp[t Re tr(Q* M)/N] dH(Q).          (RT1)

M_c is the unchanged arithmetic average of the 24 L^4 paired contour
words. Their actual length is <=ell=5L-4; 5L is a convenient geometric
upper bound. Inverse occurrences and both labelled T=2 seams remain.
The original chi_cut cuts only plaquettes entirely inside each block.

For a deterministic block set R let J_R contain ALL its owned free links.
P_R and C_R contain every plaquette/kernel whose actual field word reads
J_R. They have |P_R|<=6m0|R|, |C_R|<=8|R|; all their fine readers lie in
N_1(R), the periodic sup-neighborhood. Include coarse-link endpoints,
original source labels and the local lift U0(V), whose internal links are
I and whose positive face-crossing link equals that face's V_c.

Assign each touching factor to w_R,J and every other factor to W_out,J.
An internal block plaquette reads no crossing link, so exactly

    chi_cut w_J=chi_out W_out,J chi_R w_R,J,
    D_R^0(y)=int dH_(J_R) chi_R w_R,0 >0,
    D_R^J(y)=int dH_(J_R) chi_R w_R,J >0.               (RT2)

y denotes the REAL retained exterior free links, V, and any additionally
retained input data. Every crossing-boundary normalized kernel belongs to
w_R,J, including its full Z_t(M). Outside-only kernels belong literally
to W_out,J. Positivity follows, for every real exterior, from a product
cap about the reset U0 on J_R; its internal plaquettes satisfy the cut.

On a positive original fibre the conditional law at J=0 is

    dnu_R^0=chi_R w_R,0 dH_(J_R)/D_R^0.                 (RT3)

The identical chi_out W_out,0 cancels BEFORE differentiating this ratio.
If chi_out=0, the displayed cancellation of raw fibre masses would be 0/0.
RT3 itself defines the positive local extension there; agreement with the
original conditional is asserted only on its support. No jet of chi_out
is taken. An outside-only HISTORY weight or outside source tilt appearing
only in the numerator does not cancel in R_h/Z_A; it remains in RT27 below.
The same cancellation with a common extra outside factor is valid on its
positive fibres, but never removes its mass from the outer integral.

## 2. An exact C^6 replacement for the auxiliary shell choice

Choose 0<rho0<1 and use the real source domain |J_p|<rho0 u. Put

    Q_X=sum_(free e owned X)||U_e-U0_e(V)||HS^2/N, 0<=Q_X<=4m0,
    C_F=8(30L^2)^2 L^3(L+20), C_psi=8L^3,
    c=min((1-rho0)/C_F,kappa_-/C_psi),
    a_bulk=6(1+rho0)m0, a_shell=24(1+rho0)+4kappa_+(5L)^2,
    alpha=min(1,c/(8a_shell)), g_s=log(1+alpha/2),
    K=ceil(max(1,(8/g_s)^2,(2/g_s)[1+log(2500m0/q)])),
    V_K=(4K+1)^4, r=4K+4, d=r+2, W_K=(8K+13)^4,       (RT4)

where 0<q<=4m0. This K uses alpha/2, unlike the old hard-selector K.
All following regions and counts are recomputed with this K. Fix nonempty
A, n=|A|, I_j=N_(2j)A, R_j=N_(2j+1)A and
S_j=N_(2j+2)A minus R_j, for 0<=j<K. On Q(A)>=qn, some j has
Q(S_j)<=alpha Q(I_j)/2. Otherwise Q(N_(2K)A)>(1+alpha/2)^K qn,
whereas it is <=4m0 V_K n. To check the strict contradiction, put
b=log(2500m0/q). K>=1 and log K<=sqrt(K) give
4 log K<=g_s K/2 and b<=g_s K/2-1. Thus
g_s K>log(4m0/q)+4 log(4K+1). Wrapping only removes cells; a terminal
empty shell is successful. No terminal exterior is left unpaid.

Define the explicit source-independent cutoff

    chi(v)=1 (v<=0), 0 (v>=1),
    chi(v)=[13!/(6!)^2] int_v^1 s^6(1-s)^6 ds (0<v<1),
    v_j=[Q(S_j)-(alpha/2)Q(I_j)]/[(alpha/2)qn],
    s_j=chi(v_j), omega_Aj=s_j product_(i<j)(1-s_i).      (RT5)

chi is globally C^6, takes values in [0,1], and its first six derivatives
vanish at both joining points. It is not asserted C^7. The telescoping
product and the existence of an s_j=1 give EXACTLY

    sum_(j<K) omega_Aj=1 on {Q(A)>=qn},
    supp D_field^m omega_Aj subset {Q(S_j)<=alpha Q(I_j)},
          0<=m<=6, whenever Q(A)>=qn.                  (RT6)

The support assertion relevant here differentiates ONLY retained variables
after integrating J_Rj, as proved in section 4. At order zero, nonzero s_j
implies Q(S_j)<alpha Q(I_j)/2+alpha qn/2<=alpha Q(I_j).
At positive order chi's derivatives are supported in 0<v_j<1.

There is an exact full-volume partition, not just a partition of a bound.
Decompose the actual q-bad set into its range-r connected components A.
For each component sum its shell labels with omega_Aj. Set

    L_Aj=1_(Q_X>=q on A) 1_(Q_X<q on R_j minus A) omega_Aj,
    Pi_h^sm=1_(Q_X<q on O_h) product_((A,j) in h) L_Aj,
    O_h=blocks minus union_h R_j.
    sum_h Pi_h^sm=1.                                    (RT7)

Here the allowed A are range-r connected and mutually at distance >r.
For any nonzero summand the bad set is exactly union A, so its components
are those labels. Conversely each actual component configuration has
sum of shell weights product_A sum_j omega_Aj=1. Q=q is assigned bad.
The empty history is the all-good cap. Thus inserting RT7 under ANY
original integrand, including its earlier history weight, preserves it
pointwise. Individual old hard first-success summands are not equated
to the new summands. This is a changed auxiliary proof representation.
The original bare cut, G/Omega tests and past selectors are not smoothed.

All earlier shells S_i, i<j, and all I_i lie inside R_j. Distinct selected
R_j have distance at least seven, since their cores are separated by >4K+4.
Their N_1 physical neighborhoods are disjoint. Consequently no original
plaquette or normalized kernel touches two such active regions. This
geometric separation concerns physical factors, not future Gaussian readers.

## 3. Source-free denominator comparison on the SAME compact law

The energy representation used only for VALUES is exact:

    E_R^epsilon=sum_(p in P_R)(1+epsilon_p)s(U_p)
                            +kappa sum_(c in C_R) psi_c,
    psi_c=m(M_c)-Re tr(V_c* M_c)/N,
    m(M)=max_Q Re tr(Q* M)/N,
    w_R,J=exp[-u E_R^epsilon] product_(c in C_R) Ntilde_t(M_c)^-1,
    Ntilde_t(M)=int exp[-t(m(M)-Re tr(Q* M)/N)]dH(Q).     (RT8)

The identical field-dependent centering factor cancels in the original
kernel quotient. Ntilde_t is not replaced by e^-t Z_t for a rough mean.
Neither m nor psi is differentiated: the jet proof returns to RT1.

Here is the actual local energy calculation. Tree/brick word filling uses
at most 30L^2 plaquette factors. Squared free-link chords are bounded by
2(30L^2)^2 times their block Wilson sum for internal links, and
20(30L^2)^2 times their brick Wilson sum plus 8 psi_c for crossing links.
Each plaquette belongs to at most eight labelled bricks. Summing gives
E_R^epsilon>=c Q(I) if N_1(I) subset R. All complete brick plaquettes
then belong to P_R, even at the labelled T=2 seam. In particular

    E_Rj^epsilon>=c Q(I_j).                              (RT9)

Reset exactly J_R to U0, holding its real exterior fixed, and define
A_ref^e using the original Wilson terms with coefficients 1+e_p and
the comparison kernel term kappa[1-Re tr(V_c* M_c)/N] at that reset.
Plaquette telescoping gives the bound 24(1+rho0) times exterior squared
chords. Averaging the actual words of length <=5L gives
4kappa_+(5L)^2 times those chords. Coarse plaquettes at U0 contribute
at most a_bulk delta^2|R|. Hence, for BOTH e=0 and e=epsilon,

    A_ref^e<=a_bulk delta^2|R|+a_shell Q(N_1(R) minus R),
    delta^2<=c q/(8a_bulk V_K)
       ==> A_ref^e<=c Q(I_j)/4 on RT6's support.         (RT10)

This includes every hole boundary. For R=R_j, N_1(R) minus R=S_j.
The first term is <=c qn/8 and the second <=c Q(I_j)/8. Thus
E_Rj^epsilon-2A_ref^0>=c qn/2. The numerator source and the source-free
denominator have NOT been equated: they have separate actions, and this
last inequality is their explicit comparison. The same-source version
uses A_ref^epsilon and obeys the same bound.
In RT12--RT13, D_R^e means D_R^0 for e=0 and D_R^J for e=epsilon=J/u.

For completeness retain all cap and mode costs. Let

    r_H=min(1,pi/(2sqrt(N))),
    c_H=[sin(r_H)/r_H]^(N(N-1)) v_D/Vol_HS(SU(N)),
    c_*=c_H r_H^D exp[-r_H^2/(2N)],
    C_norm=max(1,c_*^-1 max(1,kappa_+)^(D/2)),
    s_*=min(r_H,epsilon_1/8,1),
    C_cap=2[48(1+rho0)m0+4kappa_+(5L)^2],
    a0=C_cap s_*^2+m0 log max(1,(c_H s_*^D)^-1)+8 log C_norm,
    a1=D(m0+8)/2, p(u)=a0+a1 log(1+u).                   (RT11)

At a compact maximizer the first variation vanishes and the second is
bounded by ||a||HS^2/N. Its radius-r_H/sqrt(1+t) Haar cap therefore gives
1<=Ntilde_t(M)^-1<=C_norm(1+u)^(D/2), including M=0. A product of
radius-s_*/sqrt(1+u) caps about the reset is inside chi_R. Telescoping
with (x+y)^2<=2x^2+2y^2 and bounding inverse Ntilde below by one yields

    D_R^e>=exp[-2u A_ref^e-C_cap s_*^2|R|]
              (c_H s_*^D)^(m0|R|)(1+u)^(-D m0|R|/2).    (RT12)

Here the group exponential Jacobian is bounded below by
[sin(r_H)/r_H]^(N(N-1)) on the cap: every half eigenangle difference has
absolute value <=r_H, and each positive-root sine quotient is squared.
This proves the stated c_H using the D-dimensional HS ball volume v_D.

Define payable={Q(A)>=qn, Q(S_j)<=alpha Q(I_j)}. For any measurable
subset of this event, its w_R,J mass is at
most C_norm^(8|R|)(1+u)^(4D|R|) exp[-u(2A_ref^0+c qn/2)]. Divide by
RT12 at e=0, or repeat with e=epsilon for the same-source denominator:

    [int chi_R 1_payable w_R,J dH]/D_R^e
          <=exp[p(u)V_K n-c u qn/2], e in {0,epsilon}.   (RT13)

No critical determinant is canceled or bounded by a dimension-independent
constant: this proof uses the exact compact denominator and its Haar cap,
with D m0|R| modes in RT12. If one also writes its regional chart subintegral
as the full critical prefactor times a chart log, that remains an additional
identity; D_R is not that chart subintegral. Deep outside weights are absent
from RT13 only because the exact fibre factorization RT2 already retained
them outside. This proof needs no smallness of those compact fields.

## 4. All six retained-field and four original-source positions

Retained fine directions act on exterior FREE links and on any additional
declared retained input fields. Coarse directions act on the actual V.
Their weights are those of RGA3: h_level on each field and r_p in original
J units. Put h_f=max weight for current exterior fine directions,
h_c=coarse weight, H=h_f+h_c, r_*=max_p r_p. Additional retained fields
are read only by the declared inserted functions below, with their own
unchanged weights. Use total fine-plus-coarse order <=6, source order <=4.
No within-species invariant derivatives are commuted.

Use the actual REAL Haar change of variables on integrated free links

    U_e=Z_e U0_e(V), e in J_R.                            (RT14)

Product Haar is invariant. Internal cuts and all Q_X for X in R are
independent of V in Z_R coordinates. Thus the hard A-bad and R-minus-A
absence factors, and all earlier s_i for i<j, are fixed. An optional
extra fixed selector 0<=vartheta(Z_R)<=1, for example the complement of
the original-a product chart, can also be kept. It is not differentiated.
No such statement is made for a general G/Omega/history selector.

On the retained current shell, Z_e=U_out,e U0_e(V)^-1. A field word of
length 1<=m<=6 has the bound |D^m Q(S_j)|<=2m0 |S_j| H^m: differentiating the
two unitary trace words retains their exact order, and each occurrence
has norm bounded by its declared fine or coarse radius. Source hits give
zero. Since |S_j|<=V_K n, let

    d_chi=4m0 V_K/(alpha q),
    c_l=[13!/(6!)^2] sum_(a=0)^6 binom(6,a)(6+a)!/(7+a-l)!,
       1<=l<=6,
    W_0=1,
    W_m=H^m sum_(pi partition [m]) c_|pi| d_chi^|pi|, 1<=m<=6,
    P_chi=sum_(m=0)^6 2^m W_m/m!.                        (RT15)

The constants c_l bound sup|chi^(l)| by differentiating its displayed
polynomial. The ordered scalar chain rule gives W_m. All previous
(1-s_i) are fixed and bounded by one, so each derivative of omega_Aj
is bounded by W_m on the SAME payable event and vanishes outside it.
There is no K-fold differentiated product or new charge. The two field
species give sum_(a+b=m)1/(a!b!)=2^m/m!. chi has no sources, so C^6
suffices even though the joint density needs all ten positions.

For the density, use its original smooth kernel RT1, not the maximizer
representation RT8. Define for a constant B>=0 the positive Bell polynomials

    M_0=I_0=C_0=1, M_m(B)=sum_pi B^|pi|,
    L_m(B)=sum_pi (|pi|-1)! product_(Q in pi) M_|Q|(B),
    I_m(B)=sum_pi |pi|! product_(Q in pi) M_|Q|(B),
    C_m(B)=sum_(l=0)^m binom(m,l) M_l(B) I_(m-l)(B).      (RT16)

Ordered differentiation of exp H assigns each new position to an existing
block or a new block. Integrating and dividing by the positive integral
bounds |D_I Z|/Z by M_|I|. Differentiating Z Z^-1=1, or the finite log
series, gives I_m and L_m without commuting any derivative word. For the
actual compact kernel, its normalized fine score is bounded by
(ell H)^m L_m(t), since every original word derivative of its exponent
is <=t(ell H)^m. Its numerator additionally costs t[(ell+1)H]^m.
All means, including zero and singular means, obey this positive estimate.
Each Wilson factor costs u(1+rho0)(4H)^m; a single source hit costs
2r_* at field order zero or r_*(4H)^m otherwise. Higher source hits on
the log density vanish. A simultaneous bound through order ten is

    S=1+2r_*+sum_(m=1)^10 {u(1+rho0)(4H)^m
            +t[(ell+1)H]^m+(ell H)^m L_m(t)+r_*(4H)^m},
    d_*=6m0+8, B_R=d_* |R| S,
    Q_64(B)=sum_(a+b<=6, c<=4) C_(a+b+c)(B)/(a!b!c!).     (RT17)

Both numerator w_R,J and denominator D_R^0 have these score bounds.
The latter's original J derivatives are exactly zero. Using the larger
common B_R is an upper bound, not a retuning of its sources. Pointwise,

    T^(6,4)[w_R,J/D_R^0]
                     <=(w_R,J/D_R^0) Q_64(B_R).           (RT18)

This quotient is not a normalized density at J!=0. Its integral is
D_R^J/D_R^0, which is kept exactly. The estimate follows by ordered
Leibniz with numerator M and denominator I; positivity supplies no small
value bound. Smallness below comes only from restricting to RT6 and RT13.
For the same-source normalized density replace D_R^0 by D_R^J; RT18
remains valid with all its source derivatives INCLUDED.

For four distinct labelled source directions replace the c sum in RT17
by sum_(c=0)^4 binom(4,c) C_(a+b+c)/(a!b!). This is <=4! Q_64(B).
All fifteen nonempty subsets are retained; no factorial is inserted into
the actual labelled coefficient identity. Directions may coincide.

## 5. A concrete mixed conditional integration theorem

Let f_i(Z_R,y;J) be measurable in integrated variables and C through the
declared retained (6,4) orders, with dominated derivatives on real compact
parameter sets. They have specified complete original readers Y_i and

    sup_(Z_R,y,J) T^(6,4) f_i <= a_i.                    (RT19)

These are UNREGULATED bounds. A regulated norm alone is not RT19. Sources
and additional retained input labels have their original weights. Fine
analytic functions are allowed, but not required. Retained hard selectors
depending on y fail RT19 unless they are constant on the stated domain
or have actually been summed. Integrated hard predicates are allowed.

For one core and shell define, with B_A the fixed internal bad/absence
predicate from RT7,

    A_Aj,I^0(y,J)=[int dH chi_R B_A vartheta omega_Aj
                         product_(i in I) f_i w_R,J]/D_R^0,
    A_Aj,I^J(y,J)=[same numerator]/D_R^J.                (RT20)

Keep the same exterior and every touching original factor on both sides.
At J=0 this is an expectation under the actual normalized cut law RT3.
At nonzero J the first line is precisely the local original-source tilt
over that source-FREE reference, as required by literal RGA2. It is not
replaced by the second line. Both statements below are proved separately
by RT13/RT18. Signed f_i cause no positivity assumption on A itself.

Ordered Leibniz in the downward-closed Taylor index set gives T(fg)<=Tf Tg.
Differentiate on the fixed compact domain after RT14, use RT15 and RT18,
then apply RT13 on their common derivative support. This proves

    sup T^(6,4) A_Aj,I^e
       <=P_chi Q_64(d_* V_K n S)
                  exp[p(u)V_K n-c u qn/2] product_(i in I) a_i,
          e in {0,J}.                                    (RT21)

Use an additional factor 4! if the stated norm includes all four labelled
source subsets. This is a JOINT integrated estimate: the differentiated
reference, its inverse normalizer, the shell, and every input are integrated
together. No inverse rare-event mass is used. Dominated differentiation
is justified on finite compact groups by RT17--RT19, including at zeros
of fixed selectors. There are no sphere/corner traces because the original
active compact measure and its fixed hard predicates have not been moved
across an external-parameter boundary.

The class is nonempty and contains actual finite-jet inputs. For an
original local Wilson observable f_p=lambda_p s(U_p), the explicit bound
a_p=|lambda_p|[2+sum_(m=1)^6(8H)^m/m!] follows by differentiating its
four unitary occurrences. It is a fine-analytic example with original
plaquette reader. A bounded measurable function of an internal active
plaquette, times a retained C^(6,4) function, is a rough example: U0=I
on those internal links, so its hard integrated predicate is fixed in
RT14. It is charged only as part of RT20, never as an uncharged atom.

For an inherited input independent of the current output V, its genuine
coarse path after RT14 is a fine path with directions Ad_(Z_e) B_c on
crossing links. Their operator norms are unchanged. If its original
current fine radius is h_in, an explicit sufficient conversion of a
finite-jet bound a_i^in is

    a_i=2^6 max(1,h_f/h_in,h_c/h_in)^6 a_i^in.             (RT22)

Other retained levels keep their own radii. This follows from the exact
ordered path product and the sum of fine/coarse allocations, not from
analyticity or a new center at each point. If an input explicitly reads
V or has a different coefficient map, its own full RT19 bound is required.
RT22 does not convert a regulated norm into an unregulated one.

For countably many optional attached inputs sum absolutely BEFORE estimating
their allowed subsets; the product rule gives the exact upper bound

    sum_(I finite) product_(i in I) a_i=product_i(1+a_i)=exp H_in,
    H_in=sum_i log(1+a_i).                                (RT23)

The same proof bounds products of 1+f_i with this price. The input-size
obligation is explicit: H_in<=b_in n. It is verified, for example, when
every Y_i is nonempty and contained in the fixed Gamma_A below and
sup_x sum_(i:x in Y_i) a_i<=a_in, since then H_in<=a_in |Gamma_A|.
Thus b_in=a_in W_K is sufficient. A finite incidence family of at most
n_in n inputs with a_i<=u^M A has instead
b_in=n_in log(1+A u^M). These are two different checkable budgets;
neither is asserted for arbitrary inherited histories or multiplicities.
Empty-support factors instead retain their explicit sum of log(1+a_i)
in H_in; no rooted sum pays them automatically.

## 6. Full readers, one-use ledger and the native mu+2 sum

Take Gamma_A=N_d(A), d=4K+6, with |Gamma_A|<=W_K n. It includes all
physical kernel/source readers, every shell and absence test, original
coarse endpoints of U0, and all deterministic region memberships.
Require every attached input's FULL original reader Y_i subset Gamma_A,
including earlier retained labels if it has them. No hidden past reader
may be projected onto this set. A larger supplied support needs its own
weight and count; no arbitrary long-reader conclusion follows here.
Input label lists are fixed on the real evaluation domain; their complete
membership records belong to Gamma_A. A remote rule for choosing a list
cannot be hidden in this hypothesis. Any earlier-level embedding keeps
its original reader labels and is admitted only if they really fit here.

The actual local ratio RT20 agrees whenever all these original data and
membership lists agree. Its integrals are over the same finite product
of probability-Haar groups. No global minimizer or center selection is
involved. A derivative in an absent original label is identically zero.
Gamma_A is face connected when A is range-r connected. The optional input
readers are not replaced by their endpoint sets. For the current-level
data it contains at most D m0 |Gamma_A| fine scalar labels,
4D |Gamma_A| coarse labels and 6L^4 |Gamma_A| original source labels.
RT17 counts dense directions directly. Summing extra absolute labelled
coordinate jets would add the corresponding finite powers of these
counts; that is not silently identified with RGA3's direction norm.

Let Q*=4! Q_64(1), which also covers the labelled-source version. Since
Q_64 has nonnegative coefficients and degree at most ten,
Q_64(B)<=Q_64(1)(1+B)^10. For n>=1, 1+bn<=(1+b)^n. Define

    D_jet=log max(1,P_chi)+log Q*+10 log(1+d_* V_K S),
    alpha_Aj=exp{[p(u)V_K+D_jet+b_in-c u q/2]n}.          (RT24)

RT21--RT23 prove the bound alpha_Aj for the sum of the declared attached
inputs at this core. One explicit allocation is

    D_jet<=c u q/16, b_in<=c u q/16,
    alpha_Aj<=exp{[p(u)V_K-3c u q/8]n}.                 (RT25)

This ledger spends c u q/16 on ALL shell/reference/normalizer jet positions
and c u q/16 on the input sum. It leaves 3c u q/8 of the SAME original
conditional reserve; it has not independently spent c u q/2 again. The
Haar and inverse-normalizer value price p(u)V_K is still present. No later
forest may reuse either paid fraction or forget that value price.

Let Delta=max(1,(2r+1)^4-1). An r-connected n-set through an owner has at
most Delta^(2(n-1)) choices, from a fixed spanning-tree traversal. A reader
containing a fixed x has at most W_K choices of a nearby anchor in A.
At most K shell choices are bounded by K^n. For ANY fixed mu>0 put

    t_ret=K exp[(mu+2)W_K+p(u)V_K-3c u q/8],
    Q_ret=sup_x sum_(A,j:x in Gamma_A)
                         exp[(mu+2)|Gamma_A|] alpha_Aj
              <=W_K t_ret/(1-Delta^2 t_ret).             (RT26)

This is the literal native support reserve mu+2 on conditional coefficients,
not a relabeling of the much smaller Gaussian beta. The sum is over
specified optional input families satisfying RT23. It does not include
an uncounted independent family of such prescriptions for each A.

Nonempty order: fix N,L,kappa bounds, rho0, epsilon_1 and mu first, hence
all cap and geometric constants. Choose p_cut=(log(2+u))^a with a>5/2,
q=c_q sigma^2 p_cut^2 and fixed c_q>0. Eventually q<=4m0; take K from
RT4 and an open real curvature window strictly inside RT10. No complex
coarse or source analyticity is required. For polynomially bounded H,r_*,
log S and log P_chi are O(log u+log K), including all rough Z_t scores.
Thus D_jet=O(log u+log K). If a_in is bounded, b_in=a_in W_K=O(log^4 u);
more generally retain the literal RT25 bound or a finite-incidence input
bill of order log^5 u, for example n_in<=C W_K and fixed A,M in RT23.
Meanwhile K=O(log u), p(u)V_K=O(log^5 u) and
u q=N c_q p_cut^2. These prove RT25 and, by a finite uniform threshold,
Delta^2 t_ret<=1/2 and Q_ret<=exp[-c N c_q p_cut^2/8]<=1/4.
The native h_l=sqrt(N/u_l) are included when the specified current/coarse
radii and input conversion obey these explicit budgets. No bound for an
unspecified cross-level radius ratio or arbitrary growing b_in is inferred.

## 7. Exact outer normalization and the remaining construction

The conditional estimate is a genuine RGA14/MS7 supplier on one bare
compact fibre, including retained jets. To exhibit its exact place in
R_h/Z_A, fix R and decompose a history/input insertion into an inside
function L_R and an outside-only function L_out whenever such a
factorization is actually valid. Define the SOURCE-FREE outside marginal

    dnu_out,R^0=Z_cut(V,0)^-1 chi_out W_out,0 D_R^0 dH_out,
    E_out(J)=exp[-sum_(p notin P_R) J_p s(U_p)],
    R_L(V;J)/Z_cut(V,0)
       =int dnu_out,R^0 L_out E_out(J)
             [int chi_R L_R w_R,J dH_(J_R)/D_R^0].       (RT27)

This is Fubini and RT2, not a comparison estimate. Every outside-only
kernel and its normalizer, and the mass of any previous history, remain
in this equality. All original source labels outside P_R are in E_out,
not replaced by source labels at the coarse scale. If L_R is RT20's
charged smooth-shell product, RT21 controls its bracket. For a history
with active/exterior readers entangled, its actual inside factor must
first be opened; no factorization into L_R L_out is assumed by definition.

For several fixed separated whole-block regions, the original compact
conditional on their union factors into their individual w_R and chi_R
laws, because no physical factor reads two of them. At e=0 its EXACT
normalizer is product D_R^0. A joint product of charged insertions, each
reading no other integrated region, therefore satisfies the product of
RT21 on this one common conditional reference. Shared exterior readers
remain shared parameters; they do not destroy this pointwise identity.
If an inserted reader meets another active region, join it before using
this statement; the separate charge bounds cannot simply be multiplied.

Sources require a further distinction even in this separated example.
With sources on all touching regions the unselected conditional mass is
product D_R^J/D_R^0. Normalizing a generating product of charged insertions
by D_union^J yields a unit empty term and same-source coefficients A^J.
Relative to D_union^0 it also has the EXACT prefactor product D_R^J/D_R^0.
It is not a rare correction and is not deleted. RT21 at e=0 controls
the fully charged source-free-reference coefficients, but it does not
turn an uncharged source tilt into an empty coefficient equal to one.

In particular there is a complete conditional construction for a FIXED
finite collection of separated regions R_g satisfying these hypotheses.
Let Phi_g=B_A vartheta omega_Aj product_i(1+f_i), with the optional input
family of RT23 assigned to that g and no other integrated region in its
field readers. Write A_g^J=int Phi_g dnu_Rg^J and S_g=D_Rg^J/D_Rg^0.
Direct conditional product integration, without a Gaussian approximation,
proves the exact physical-source identity

    T_cond(J)= [int chi_union w_union,J product_g(1+Phi_g) dH]
                                          /D_union^0
             = product_g S_g product_g(1+A_g^J),
    log T_cond=sum_g log S_g + sum_g l_g,
    l_g=sum_(n>=1)(-1)^(n-1)(A_g^J)^n/n.                 (RT28)

For real inputs with alpha_g<=1/4, every S_g>0 and 1+A_g^J>0; this is
the real logarithm. For complex-valued test insertions the displayed
series instead specifies the branch continued from zero insertion.
The full source tilt is present on EVERY integrated region even in the
unselected term. The first term in the log is kept, with the explicit
finite, generally LARGE bound

    T^(6,4) log S_g <=12rho0 u m0|R_g|
       +2 sum_(a+b<=6,c<=4,a+b+c>=1)
                        L_(a+b+c)(B_Rg)/(a!b!c!).        (RT29)

The value estimate follows from s<=2 and |P_R|<=6m0|R|; each derivative
follows by applying RT16 to both positive compact normalizers. At J=0,
S_g=1 exactly, but its original-source jets do not disappear. RT29 is
not assigned a small polymer norm or hidden in a rare coefficient.

By the product jet inequality and RT24, T l_g<=-log(1-alpha_g)<=2alpha_g.
Every derivative series through the ten positions converges uniformly on
real compact parameter sets, so these are jets of the SAME functions.
Thus the genuinely small conditional correction satisfies

    sup_x sum_(g:x in Gamma_g) exp[(mu+2)|Gamma_g|]
                                    sup T l_g <=2 Q_ret. (RT30)

All original readers and the canonical agreement above persist. This
product identity uses one fixed union and one fixed outside fibre; it is
not a sum over region-dependent references. No overlap-tree reserve was
spent to prove RT30. Such trees in a later global assembly still need
their own losses. For the empty collection the inside mass is one and
both displayed logarithmic sums are zero; its full outside weight remains.

Nor does factorization of these fixed conditional fibres prove the global
overlap-component factorization required by RGA15. RT27 has a correlated,
region-dependent outside marginal. Its derivative already at first order
contains a covariance with the log score of W_out,0 D_R^0; source/outside
history derivatives remain as well. The currently missing, precise estimate
is a complete-reader bound, on ONE actual outside reference, for

    T^(6,4) int dnu_out,R^0 [L_out E_out(J) A_R,I^0],

with rooted size product alpha_i, native mu+2 reserve, the actual history
mass, all ten derivative positions, and compatible identifications as R
varies. A pointwise bound on A_R,I^0 bounds a positive scalar expectation
when the other factors are controlled; it does not bound these derivatives
or supply exact global overlap factorization. The remaining hard exterior
good/absence selectors in RT7 have not become C^6 in retained variables.
They must be summed, canceled on the proper common reference, or paid with
their own exact boundary representation. RT5 only resolves the SHELL test.

## 8. Relation to the current Gaussian suppliers and limits

[MK](MARKED_COMPACT_CHART_ASTRA.md)/[WR](WEIGHTED_RETURN_JETS_ASTRA.md)
and [CG](COMPACT_RETURN_GLUING_ASTRA.md) already give the bounded bare
chart gas at their stated scope; their old hard selectors and original
sources are preserved. RT7 proves the changed shell partition directly;
it does not cite their old partition as an identity for new summands.
WR's fixed-Z argument is extended here to true retained exterior fields
by differentiating the one smooth current shell, with all full compact
normalizer scores included. The value charge/cap remains OC's antecedent.

The entire [SG](STRONG_LOCAL_GAUSSIAN_CORE_ASTRA.md) construction was
inspected. It supplies an exponentially small complete-reader covariance
tail and the displayed RJ density-support price on its actual small
domain. Its large symmetrized core atoms need not be individually PSD.
That Gaussian decomposition is not the actual outer law in RT27. No
independent PSD weakening, beta-to-mu+2 conversion or product-history
inference is used here. The present compact proof spends none of SG's
beta margins, and does not make them available for a later step.

[MEAN](MEAN_READER_RETURN_ASTRA.md) supplies fine-analytic mean attachment
and small-boundary jets within its proved scope. It does not imply RT19
for arbitrary inherited regulated inputs. Conversely, RT21 integrates
bounded nonanalytic inputs only when attached to a genuinely charged root.
It gives no uncharged fine-analytic sector closure, no free price for b/sigma,
and no simultaneous arbitrary regulator-multiplicity moment. Whole-block
geometry was used for chi_R's fixed domain; arbitrary holes in the set of
FREE LINKS can make an interior cut read a retained variable and require a
different boundary calculation. Block sets may have geometric holes because
every remaining block is included whole and RT10 keeps every boundary.

For literature comparison, [Dimock, arXiv:1212.5562v2, section 3.10](https://arxiv.org/html/1212.5562v2#S3.SS10)
uses exact complementary characteristic-function sums and retains the
normalization/outside fields in the next density. Its scalar/d=3 theorem
is not a gauge conditional jet theorem. [Brydges--Slade,
arXiv:1403.7244v2, Lemma 6.4](https://arxiv.org/html/1403.7244v2#S6.SS2)
permits a measurable function of integrated boson fluctuations in a fixed
Gaussian norm estimate; it does not justify differentiating a retained
hard selector or a parameter-dependent normalized gauge law. RT5 and
RT16--RT21 rebuild the finite compact calculation required here. These
papers provide antecedents and comparisons, not imported closure.

All statements concern one supplied bare step and its explicitly bounded
mixed conditional class. Original G-minus-Omega/G^c histories, complete
R_h/Z_A return, extraction of an invariant class, repeated effective
trajectories, non-free continuum existence and physical mass gap remain
OPEN. Source mathematics is frozen before its compact provenance. No
scientific numerical run, predecessor edit, Git/front/PR/audit action or
extra worker is part of this unit. Pinned repository procedure 01589af
and [PROCESS_LIGHT](PROCESS_LIGHT.md) govern; root owns a different fresh
review and publication. No review verdict is a mathematical premise.
