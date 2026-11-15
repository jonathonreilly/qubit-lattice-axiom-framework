# Compact shell growth pays the original outside-chart denominator

**Author proposal; new independent review required.** This proves an actual
original-cut, fixed-V probability bound for every prescribed finite set of
outside-chart defects. A finite cover of enlarged regions pays the exterior
cost in CS27. The argument uses compact group distances and the exact soft
kernel, including its normalizer; it uses no convexity outside the chart.

There are two outputs beyond a single-defect estimate: a connected-component
expectation bound with every original reader charged, and a real avoidance
and reference comparison. A shrinking-threshold version also gives a real
comparison with the unchanged actual selected cube, on a materially smaller
coarse-curvature window. None of these probability bounds is a local analytic
activity representation. Complex normalized return, the full history/sea
interfaces, nonlinear flow, continuum existence and physical mass gap remain
open.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Bałaban and Dimock are the antecedents of the large-field denominator and
localization problem. The compact shell-growth argument and its original-law
matching are proved below. The real avoidance induction is rebuilt in the
form of the lopsided local lemma, credited to Erdős--Spencer and the
Scott--Sokal exposition. No literature theorem replaces a displayed step.
This author wrote CS and GC and previously reviewed CC. The predecessor
reviews are independent of those author units, not of this new unit.

## 1. Exact original cut, local energy and the compact reference

Use the supplied model and geometry of [CS1--CS6](CUT_SECTOR_COERCIVITY_ASTRA.md):
d=4, SU(N), N>=2, odd L>=3, T>=2, u>=1, 0<kappa_-<=kappa<=kappa_+, fixed real
coarse V, and a fixed original-source interval |e_p|<=rho with 0<=rho<1.
The original interior-plaquette cut has epsilon_1>0. No new smallness ceiling on epsilon_1
is needed here. The model is mathematical input, not a derivation from the
framework axioms or adoption of a physical primitive.

Put D=N^2-1, m0=3L^4+1, p_L=5L. Work in the exact root-pinned tree quotient.
All free positive links, roots and winding information remain; probability
Haar on the eliminated nonroot gauge variables integrates to one. There is
no FP factor. The reference U0(V) has internal links I and positive crossing
links V_c. Every actual paired contour at U0 equals its V_c, including at
T=2 when the two face labels between the same blocks remain distinct.

For |A|_n=||A||HS/sqrt(N), the actual density is

    w_e=exp[-u E^e] product_c Ntilde_(kappa u)(M_c)^(-1),
    E^e=sum_p(1+e_p)s(U_p)+kappa sum_c psi_c,
    s(P)=|I-P|_n^2/2,
    psi_c=m(M_c)-Re tr(V_c^* M_c)/N,
    m(M)=max_(Q in SU(N)) Re tr(Q^*M)/N,
    Ntilde_t(M)=int exp[-t(m(M)-Re tr(Q^*M)/N)]dQ.             (OC1)

M_c is the arithmetic mean of the actual paired contour words, not a polar
or Gaussian substitute. The identical exp[-t(1-m)] factors have canceled
between the original kernel numerator and its original normalizer; all
remaining field dependence stays in OC1. Let nu_e be its normalized original
cut measure and Z_cut(V,e) its raw mass. Both are positive at real e.

Let N_s(A) be the periodic coarse sup-distance-s neighborhood of a set A.
For a block set R, integrate ALL free positive links J_R owned by R, leaving
all other free variables z fixed. P_R contains every plaquette reading J_R;
C_R contains every kernel whose complete paired words read J_R. Retain
inverse occurrences and all labels across a periodic seam. CS5 gives

    |J_R|=m0|R|,  |P_R|<=6m0|R|,  |C_R|<=8|R|.

All free-variable readers of these factors lie in N_1(R). The remaining
interior cut consists exactly of the block cuts in R. This is the conditional
law in the exact free-link quotient, not a conditional on frozen ungauged
fine links. An exterior is admissible when its own block cuts hold.

Define the compact charge and fixed coercivity constants

    Q_X=sum_(free links owned X) |W_e-U0_e|_n^2,  0<=Q_X<=4m0,
    Q(A)=sum_(X in A)Q_X,
    B_fill=30L^2,
    C_F=8 B_fill^2 L^3(L+20),  C_psi=8L^3,
    c=min((1-rho)/C_F,kappa_-/C_psi)>0.                     (OC2)

The exact localized consequence of CS7--CS12 that will be used is

    E_R^e(W|z,V)>=c Q(B)     whenever N_1(B) subset R.        (OC3)

Here E_R includes precisely P_R and C_R. To check this qualification, every
internal free edge owned by B has its complete tree-loop filling in its
block. A crossing edge owned by B has both endpoint blocks in R, so its
complete two-block brick, straight root path and every paired contour also
lie in R. The extra far seam of a T=2 torus is excluded from each lifted
brick, not erased from the list of distinct readers. Every plaquette in
these block/brick fillings has a free edge in J_R; hence it belongs to P_R.
Each required mean-path kernel belongs to C_R. There is no exterior energy
term subtracted in OC3.

For completeness, the path fillings give respectively 2 B_fill^2 times the
block Wilson sum, and 20 B_fill^2 times the brick Wilson sum plus 8 psi_c,
as upper bounds for a squared free-link chord. The latter uses
|S_c-V_c|_n^2<=4 psi_c+8 B_fill^2 sum_(p in brick(c))s(U_p).
A fine plaquette is in at most eight labelled bricks. Summing these estimates
for the indicated links gives C_F,C_psi above. This is an all-compact
nonabelian word argument, with repetitions counted; no logarithm is taken.

## 2. A sum of all exterior readers, rather than a maximum boundary field

Reset just J_R to U0, calling the result W^R. Its internal plaquettes in R
are I, so it is strictly within the original cut for every admissible z.
Use the comparison phase

    A_ref^e(z)=sum_(p in P_R)(1+e_p)s(U_p(W^R))
                 +kappa sum_(c in C_R) phi_c(W^R),
    phi_c=1-Re tr(V_c^* M_c)/N.

As m(M)<=1, E_R<=A_R for this comparison action; A_R is not a substituted
model. Set delta_V=max_P||I-V_P||op. The needed strengthening of CS27 is

    A_ref^e(z)<=a_bulk delta_V^2 |R|
                     +a_shell Q(N_1(R)\R),
    a_bulk=6(1+rho)m0,
    a_shell=24(1+rho)+4kappa_+ p_L^2.                       (OC4)

Here the shell includes every boundary component, including boundaries of
holes. To prove OC4, for an affected plaquette telescope about its U0 word.
Writing d_f=|z_f-U0_f|_n for its exterior free occurrences gives

    s(U_p(W^R))<=2s(U0_p)+4 sum_(exterior occurrences f in p)d_f^2.

Each free link is incident to six plaquettes. This yields the Wilson shell
coefficient 24(1+rho), with the reference term bounded by a_bulk delta_V^2|R|.
For a paired word P, its reference is exactly V_c, and

    |P(W^R)-V_c|_n^2<=p_L sum_(exterior occurrences f in P)d_f^2.

A fixed internal free link can enter only the eight kernels incident to its
block; a crossing link enters its one face kernel. Each word has at most
p_L occurrences of any link. Averaging the actual words and multiplying by
kappa/2 gives at most 4kappa_+ p_L^2 per exterior squared chord. This bound
retains repetitions, both periodic face labels, every adjacent kernel and
its original coarse-data reader. All these exterior owners are in
N_1(R)\R. No maximum-times-boundary-area estimate is needed.

## 3. The actual cap and the polynomial normalizer cost

The compact maximizer-cap proof in CS15 gives, for every mean M including
singular and zero M,

    1<=Ntilde_(kappa u)(M)^(-1)<=C_norm(1+u)^(D/2).

C_norm is the explicit finite constant of CS16. At an actual maximizing Q,
the first variation of Re tr(Q^*M)/N vanishes and its second variation is
bounded by ||A||HS^2/N. Integrating an HS group cap of radius proportional to
(1+t)^(-1/2) proves this polynomial; no Gaussian law is substituted.
Let r_H and c_H be CS15's radius and probability-Haar cap constant, so a
radius-r cap has mass at least c_H r^D for r<=r_H. Define

    s_*=min(r_H,epsilon_1/8,1),
    C_cap=2[48(1+rho)m0+4kappa_+ p_L^2],
    a0=C_cap s_*^2
           +m0 log(max(1,(c_H s_*^D)^(-1)))+8 log C_norm,
    a1=D(m0+8)/2,    P_R(u)=exp[(a0+a1 log(1+u))|R|].        (OC5)

A product of radius-s_*/sqrt(1+u) caps around W^R lies strictly inside the
original cut. Every formerly identity internal plaquette moves by at most
four times this radius. The inequality (x+y)^2<=2x^2+2y^2, applied to the
actual plaquettes and words, gives the exact denominator lower bound

    D_R(z,V,e)>=exp[-2u A_ref^e(z)-C_cap s_*^2|R|]
                  (c_H s_*^D)^(m0|R|)(1+u)^(-D m0|R|/2).   (OC6)

Every inverse centered normalizer was bounded below by one in this cap.
For an event on which E_R^e>=2 A_ref^e(z)+h, its numerator is at most
C_norm^(8|R|)(1+u)^(4D|R|) exp[-u(2 A_ref^e(z)+h)].
The remaining product probability-Haar mass is at most one. Dividing by
OC6 yields P_R(u) exp(-u h). This comparison keeps the complete kernel
polynomial and original Haar dimension. All exterior action factors cancel
only inside this conditional ratio. They remain in the outside measure.

## 4. One finite shell cover for any prescribed set of defects

Fix a charge threshold 0<q_*<=4m0. Let E_X be any source-independent event
that reads only the free links owned by X (at fixed V), with

    E_X implies Q_X>=q_*.

The actual outside-chart event will be such an E_X. No bound on any exterior
field is assumed. Put

    alpha=min(1,c/(8a_shell)),  g=log(1+alpha),
    K=ceil(max(1,(8/g)^2,(2/g)[1+log(2500m0/q_*)])),
    V_K=(4K+1)^4,  R_*=2K-1,
    S_K=(4K+5)^4,  M_K=(4K-1)^4.                           (OC7)

These deliberately large constants are finite. Since log K<=sqrt(K),
4log K<=gK/2 at this choice, and 4K+1<=5K. Therefore

    (1+alpha)^K q_*>4m0(4K+1)^4.                          (OC8)

For any fixed nonempty finite set A of distinct coarse blocks, define

    B_n=N_n(A),  q_n=Q(B_n),
    R_j=B_(2j+1),  I_j=B_(2j),
    shell_j=B_(2j+2)\B_(2j+1),  j=0,...,K-1.                (OC9)

Neighborhoods are actual sets on the torus. Counts never count a wrapping
site twice. In particular |B_n|<=(2n+1)^4|A|, and N_1(I_j) subset R_j.
If all E_X, X in A, occur, q_0>=q_*|A|. There is at least one j with

    Q(shell_j)<=alpha q_(2j).                              (OC10)

Otherwise q_(2j+2)>(1+alpha)q_(2j) at every j, and hence
q_(2K)>(1+alpha)^K q_*|A|>4m0 V_K|A|. This contradicts the compact bound
q_(2K)<=4m0|B_(2K)|<=4m0 V_K|A|. The same K works for every A and T.
If a neighborhood fills the torus, its next exterior shell is empty and
OC10 holds immediately. No infinite exterior or uncharged terminal region
is introduced. No connectedness of A was needed for this argument.

Impose the explicit coarse-curvature window

    delta_V^2<=c q_*/(8a_bulk V_K).                        (OC11)

For each j let H_(A,j) be the indicator of all E_X, X in A, together with
OC10 for this j. It is a local hard event, independent of e. It need not be
a partition; do not select the first successful radius and thereby add
readers. The cover is the finite pointwise inequality

    product_(X in A)1_E_X <=sum_(j=0)^(K-1) H_(A,j).         (OC12)

On H_(A,j), OC3 uses the FULL energy on P_(R_j),C_(R_j) to give
E_(R_j)^e>=c q_(2j). OC4, OC11 and |R_j|<=V_K|A| give

    2 A_ref^e(z)
       <=2a_bulk delta_V^2 V_K|A|+2a_shell alpha q_(2j)
       <=(c/4)q_*|A|+(c/4)q_(2j)
       <=(c/2)q_(2j).
    E_(R_j)^e-2 A_ref^e(z)>=c q_*|A|/2.                   (OC13)

The comparison A_ref^e(z) is fixed when the true conditional is taken.
Thus OC13 is exactly the numerator-denominator comparison after OC6, even
though the successful-shell test compares an exterior charge to an interior
charge. No random interior threshold is taken outside an integral. One
could instead use dyadic interior-charge bands, paying the extra factor two
in their shell bounds; OC13 avoids that extra decomposition altogether.

For EVERY admissible exterior z, the actual conditional probability obeys

    nu_(R_j)^e(H_(A,j)|z,V)
       <=exp[(a0+a1 log(1+u))V_K|A|-c u q_*|A|/2].         (OC14)

This is not a concentration statement under an arbitrarily small boundary;
the event itself has a payable shell, and the deterministic cover ensures
some such event for every prescribed defect configuration. Arbitrarily
frustrated small conditionals are consistent with OC14.

Let B_out>=0 be bounded and independent of J_(N_(R_*)(A)) in the exact tree
quotient. It is therefore exterior to every R_j. Disintegrate OC14 under
the actual interacting original measure and sum OC12. With

    b(u,q_*)=K exp[(a0+a1 log(1+u))V_K-c u q_*/2],

one obtains the main bound

    E_(nu_e)[B_out product_(X in A)1_E_X]
                         <=b(u,q_*)^|A| E_(nu_e) B_out.    (OC15)

Indeed the immediate prefactor is K times the same exponential to |A|;
K<=K^|A|. The bound is useful when b<1. No independence, separated-site
selection or packing loss has been used. The conditional energy, exterior
reference and original coarse-curvature cost have all been paid locally.
If A covers the whole torus, the same derivation pays the whole-torus cap
against q_*|A|. It never introduces a total-volume curvature loss unrelated
to the prescribed defect set.

## 5. The actual outside-chart events and complete connected readers

Let r be the fixed radius of GC's full Hessian chart, and keep its event
C_ch=C_(r/2) unchanged. Its radius is below the admitted injectivity bound.
The present proof uses only this definition, not convexity there or outside.
For a free link let Q=W_e U0_e^*. Define

    eta_ch=min(r/(pi sqrt(N)),2sin(pi/(2N))/sqrt(N)),
    q_ch=eta_ch^2,
    E_X^ch={some free link owned X is outside exp(||a||HS<=r/2)U0_e}.
                                                                  (OC16)

If |Q-I|_n<eta_ch, then ||Q-I||op<2sin(pi/(2N)). Every principal eigenangle
has absolute value <pi/N. Their sum is a multiple of 2pi, since det Q=1,
and has absolute value <pi, so it is zero. The principal logarithm is
therefore traceless, not just a U(N) logarithm. The scalar sine inequality
on principal eigenangles gives

    ||log Q||HS<=(pi/2)||Q-I||HS<r/2.

Consequently E_X^ch implies Q_X>=q_ch. This proves the required fixed-chord
witness even for compact fields with no chosen global logarithm. Its
indicator is a well-defined group event. Both the principal-log trace
margin and the normalized-to-unnormalized HS factor have been retained.

Apply OC15 with q_*=q_ch and E_X=E_X^ch. This prices ALL of C_ch^c inside
the original cut, including G outside C_ch if GC6's additional threshold
margin is unavailable. G is not redefined. For fixed q_ch, K and all collar
sizes are fixed independently of u,T. The new curvature ceiling OC11 is
additional to any chosen CB/SA/FR domain. When identifying C_ch^c as part
of the original complement, also retain GC6's actual Omega subset C_ch
margins. The probability bound itself is valid without that identification.

Every H_(A,j) retains the whole set B_(2j+2), its free-link endpoint trees,
U0 coarse links, all local plaquettes and complete normalized-kernel words.
Their original fine/coarse readers fit in

    Gamma_A=N_(2K+2)(A),  |Gamma_A|<=S_K|A|.                (OC17)

This conservative collar includes both source and tree readers. It is
connected if A is face connected. A distance or diameter has not replaced
these readers. The family of all j is covered by this same complete label.

Let D(W)={X:E_X^ch occurs}. On the coarse face graph (degree at most eight),
its exact connected-component indicator is

    C_A=product_(X in A)1_E_X^ch
                  product_(Y in partial_face A)(1-1_E_Y^ch),            (OC18)

for each nonempty face-connected A. The boundary includes every adjacent
complement vertex, along all holes as well as the outer boundary. Thus the
nonzero C_A are precisely the components of D(W), without an assumed
independence or a changed strong-good sector. Their native readers and all
readers used to price them lie in Gamma_A. No factor reads the unlisted
interior of a hole merely because it is a hole. If a later history actually
reads that entire interior, its complete reader must be added and paid; that
extra assertion is not hidden in OC18.

Since C_A<=product_(X in A)1_E_X^ch, OC15 gives E C_A<=b^|A|. A connected
k-set through a fixed vertex has at most 64^(k-1) choices: a deterministic
spanning-tree traversal of length 2(k-1), with at most eight choices per
step, determines its visited set. For v in Gamma_A, some X in A is within
2K+2 of v, giving at most S_K possible anchors. Therefore, for any fixed
original-block support rate tau>=0,

    sup_v sum_(A connected:v in Gamma_A)
                   exp(tau|Gamma_A|) E_(nu_e) C_A
       <= S_K t/(1-64t),   t=exp(tau S_K)b,   64t<1.        (OC19)

This is an actual normalized original-law, full-reader expectation bound.
It includes component shape entropy and all collars; it is not a local
analytic activity norm. The expectation depends on the global interacting
measure. No original-source locality of that integrated number is asserted.

For an explicit large-u choice at fixed q_*, set a=c q_*/2. Using
log(1+u)<=sqrt(u), the conditions

    u>=max(1,(4a1 V_K/a)^2,4(log K+a0 V_K)/a)               (OC20)

give b<=exp(-a u/2). If also a u/2>=tau S_K+log(128) and
a u/4>=tau S_K+log(2S_K), OC19 is at most exp(-a u/4).
Requiring a u/2>=log(4M_K) supplies the avoidance condition below.
These are fixed constants, not numerical claims of a useful threshold.

## 6. A real avoidance induction and the exact chart reference

There is a stronger consequence of OC15 with |A|=1. For ANY nonnegative
factor determined by free variables outside N_(R_*)({X}),
E[B_out 1_E_X]<=b E B_out. In particular this holds when B_out is an
intersection of good events at any set of block owners outside that region.
The events E_Y^ch read only the free variables owned by Y at fixed V, so
these are genuinely exterior events in the quotient conditional. Their
original tree readers are still included in OC17; this probabilistic
qualification does not shrink those geometric readers. The same proof
applies to any family E_X satisfying the native-reader and charge
hypotheses in section4.

Connect distinct block owners when their PERIODIC COARSE SUP-distance is
at most R_*. Each closed neighborhood has at most M_K vertices. This is a
graph for the proved conditional bound, not an assumed independence graph.
Suppose

    b<=1/(4M_K),  h=2b.
    b<=h(1-h)^(M_K-1).                                    (OC21)

The second inequality follows from (1-h)^(M_K-1)>=1-(M_K-1)h>=1/2.
Write A(S)=intersection_(Y in S) E_Y^c. We prove simultaneously, by induction
on |S|, positivity of its probability and

    nu_e(E_X|A(S))<=h       for X not in S.                 (OC22)

Split S into owners outside X's closed neighborhood and its neighbors.
The numerator conditioned on avoidance at the distant owners is at most b
by the actual exterior-factor bound. Inserting the neighboring avoidances
in the denominator, one at a time, costs at least 1-h each by the induction
hypothesis: every intermediate conditioning set is smaller than S. There
are at most M_K-1 such factors. OC21 closes the induction. Multiplying
these positive conditional avoidance factors also proves the required
positivity at the next size. The empty conditioning set starts the proof.
No conditional independence has been assumed.

For disjoint finite S,B this gives

    nu_e(A(S union B))/nu_e(A(S)) >= (1-h)^|B|.
    (1-h)^(T^4)<=Z_ch(V,e)/Z_cut(V,e)<=1,
    Z_ch=int Haar chi_cut 1_C_ch w_e.                      (OC23)

This is a comparison of actual positive integrals, with all normalizers,
Haar factors and source vacuum inside them. Its volume factor is explicit.
It is not a uniform bound on Z_cut/Z_ch independent of volume, nor a
complex zero-free statement.

A useful further scalar estimate keeps the full reference. Let

    Z_A=int Haar chi_cut [D(W)=A] w_e,
    Z_empty=Z_ch,
    eta=b(1-h)^(-M_K)<=2b.

For every A, including disconnected A,

    Z_A/Z_empty<=eta^|A|.                                 (OC24)

To prove it, let R=N_(R_*)(A) and B_out=1_(A(R^c)). This factor is exterior
to J_R, exactly as required by OC15. The numerator for the exact defect
pattern A is no larger than E[B_out product_A 1_E_X]. The denominator
nu_e(A(all blocks)) is at least (1-h)^|R| E B_out by OC23. Since
|R|<=M_K|A|, OC24 follows. The bound eta<=2b uses
(1-h)^M_K>=1-M_K h>=1/2. Thus the denominator is actually paid; no
selected-sector mass was inserted by assumption.

The exact identity Z_cut/Z_ch=sum_A Z_A/Z_empty follows by partitioning
by the bad set. It is not a hard-core gas with weights Z_A: these integrated
ratios depend on the whole chart exterior and need not factor for separated
components. The indicator [D(W)=A] itself checks every owner outside A.
Accordingly OC24 is not assigned the finite reader Gamma_A as an analytic
activity. OC19 concerns local component indicators, a distinct object.

## 7. Shrinking thresholds and a real comparison with the unchanged cube

This subsection is an additional, explicitly narrower domain. It is not
needed for the fixed outside-chart result. Take the actual zero-source
SA background b_0, K_*=F_0''(b_0), C_0=K_*^(-1/2), and T_*=K_* C_0.
SA14's scalar row/column and marked-reader norms give, by absolute matrix
multiplication,

    sup_i sum_j |T_*ij|<=M,
    M=max(1,Q_beta(K_*)Q_beta(C_0)),
    ||b_0||_(infinity,HS)<=C_b delta_V.                    (OC25)

Choose M from the admitted UNIFORM bounds on Q_beta, fixed before V,u,T;
it is not a measured row norm depending on distant data in the current V.
Here C_b can be the admitted CB13 zero-source constant. No operator norm
has been substituted for a scalar row sum. All colours and modes remain.
Define a local group cap and its complement by

    eta_u=sigma p/(4pi sqrt(N)M),  sigma^2=N/u,
    q_*(u)=eta_u^2=p^2/(16pi^2 M^2 u),
    E_X^u={Q_X>=q_*(u)},
    Q_good=intersection_X {Q_X<q_*(u)}.                   (OC26)

Retain 0<q_*(u)<=4m0, eta_u<=eta_ch, the original SA/CB/FR chart and
strong-good margins, and

    C_b delta_V<=sigma p/(8M),
    delta_V^2<=c q_*(u)/(8a_bulk V_(K(q_*(u)))).             (OC27)

On Q_good each relative principal logarithm is traceless and has HS norm
at most (pi sqrt(N)/2)eta_u=sigma p/(8M). Thus every scalar coordinate of
a-b_0 has magnitude at most sigma p/(4M), and OC25 gives
|sigma^(-1)T_*(a-b_0)|infinity<=p/4. Consequently Q_good is contained in
the ACTUAL selected cube Omega, with room to spare. Its Haar preimage is
used throughout. This does not rotate the cube, replace it by a white ball,
or change G. Under the admitted original margins Omega remains a subset
of the original G and cut.

The new curvature restriction is material: V_K=O(K^4), so OC27 requires
an additional constant multiple of sigma p/K^2. It is not the original
larger FR window merely renamed. All of its stated bounds, including
FR's delta_V<=c_* sigma p when FR is used, must hold simultaneously.
The original source radius stays fixed; rho does not shrink with p or u.
If invoking the upstream analytic SA/FR conclusions, also intersect their
fixed source-radius domains. The real probability proof itself only needs
rho<1.

Choose p=(log(2+u))^alpha_cut with any fixed alpha_cut>5/2. Formula OC7 gives
K(q_*(u))<=C_K(1+log u), since p>=1. Therefore

    log b(u,q_*(u))
       <=C_ent(1+log u)^5-c p^2/(32pi^2 M^2)
       <=-c p^2/(64pi^2 M^2)          for sufficiently large u.          (OC28)

This pays the actual cap's O(K^4 log u) cost. Both tau S_K=O((log u)^4)
and log M_K are smaller costs, so OC19 and OC21 apply as well. Because the
shell argument started from all prescribed defects at once, no K^4 packing
loss occurs in the exponential charge. For every fixed alpha_cut, the
conditions sigma p^3 small and sigma^2 p^12 small are eventually compatible
with the frozen IC inequalities. This is only parameter compatibility; no IC theorem
is needed, and it supplies none of the missing source/history interfaces.

Apply OC23--OC24 to E_X^u, now writing Z_cap for Z_empty. By the exact
inclusion Q_good subset Omega, for real original sources,

    Z_cut(V,e)>=Z_sec(V,e)>=Z_cap(V,e)
                             >=(1-2b)^(T^4) Z_cut(V,e),
    0<=log[Z_cut(V,e)/Z_sec(V,e)]
                          <=-T^4 log(1-2b)<=4b T^4.       (OC29)

Every exact Q-charge bad-pattern integral, divided by Z_sec(V,e), is also
bounded by (2b)^|A|, because Z_sec>=Z_cap. This is a scalar real comparison;
the exact pattern checks the whole exterior and has not become a local
analytic coefficient. The volume factor in OC29 is retained explicitly.

Both actual complementary terms remain in

    Z_cut=Z_sec+I_(G minus Omega)+I_(G^c).                  (OC30)

Each integrand is nonnegative at real e. Since Q_good subset Omega subset G,
each complementary event is contained in the union of the E_X^u. Their
combined raw mass is exactly Z_cut-Z_sec and satisfies the real ratio
consequence of OC29. They are not relabelled as a new choice of G or as the
cap complement by equality. This does not yet give their connected analytic
original-source logarithm.

## 8. Complex sources, actual returned gases and retained histories

For complex original epsilon with |epsilon_p|<=rho, the actual kernel and
cut stay fixed and |w_epsilon|=w_(Re epsilon). All events and shell tests
above are independent of epsilon. In particular the exact raw envelope is

    |int Haar chi_cut B_out product_A 1_E_X w_epsilon|
       <=b^|A| int Haar chi_cut |B_out| w_(Re epsilon),     (OC31)

whenever |B_out| has the required exterior free-variable readers. For local
component indicators one may take B_out=1 and use the positive expectation
bound OC19. No complex conditional law, normalized complex ratio or
nonvanishing of 1+B_comp follows. In particular replacing the positive
Re(epsilon) reference by Z_sec(V,epsilon) is not justified by OC29 or by
FR's selected-sector nonvanishing. The source-dependent vacuum remains.

There is an optional extension to H24's ACTUAL positive returned gas on its
exact admitted u/source/completion domain. Require every complete retained
failure-factor reader to avoid the changed-link endpoint set for
J_(N_(R_*)(A)). It then avoids that set for every R_j. The failure factors
are exterior in each conditional; the successful gas includes its empty
term, and its log oscillation is at most 2|K_(R_j)|d_q<=10d_q|R_j|.
For OC14--OC15 and their raw envelopes on these prescribed A, the same
proof replaces

    a0 by a0+10d_q                                        (OC32)

and uses the exact positive history mass as reference. The shell construction
and all complete readers remain. If d_q<=1/4, this is a fixed extra cap cost.
Complex use of this extension requires H's exact numerator/compensator
absolute-value comparison and retains the positive Re(epsilon) HISTORY mass; it introduces no division by a complex history.
This extension is not claimed when a failure reader meets an integrated
region. The full-family avoidance and reference conclusions OC21--OC29
do not follow for an arbitrary failed history: every event in the proposed
avoidance family would first need its required conditional bound.
Entire hole readers cannot be shrunk to a boundary, diameter or
distance modulo holes in applying this condition.

An original insertion that reads a replaced interior must enter H8's JOINT
replacement integral before its pre-return expectation is identified.
Noninvariant insertions require their exact tree average; original ungauged
support alone does not establish the exterior hypothesis in OC15 or OC31.
Nothing here supplies the effective-level/history identity or estimates all
interacting failure and sea factors. Zero-reference histories receive no
conditional normalization assertion.

## 9. What this closes and what the next consumer must prove

The fixed-threshold theorem closes an actual original-cut outside-chart
probability input: OC15 is uniform over arbitrary admissible exterior data
outside its explicit finite integration neighborhoods; OC19 prices the exact
connected bad components with complete cardinality. OC23 and OC24 pay a
real chart reference. The shrinking version additionally pays the actual
real selected-sector reference as OC29, with its volume factor and the
strictly smaller curvature window stated. These are substantive actual-law
bounds, not assumptions about a convenient Gaussian or chosen small exterior.

They do not instantiate the original RD18 supremum criterion unchanged:
an indicator attaining zero still has ||Theta-1||infinity=1. A probability-
sensitive construction must turn these real conditional and component estimates into locally supported
analytic original-source coefficients for the actual interacting exterior,
retaining its source vacuum and complete history readers. The newer RD
pass2 R15--R17 hard-cut/L1 criterion requires masses under its specified
PRODUCT reference and supremum-controlled interaction atoms. OC15 is under the actual interacting
original law and is not that product-reference input. A matching construction
must identify the exact effective-level return and prove its complex
normalization. The integrated component expectations and exact bad-pattern
ratios above have not been asserted to be such coefficients. The coarse law outside OC11,
and its integration through later effective levels, is also unestimated;
the present fixed-V window is not a conclusion about that coarse law.

There is a simple scope control. Independently of this gauge model, fix
0<b<1 and mix with equal probability an all-zero occupation field and independent Bernoulli
occupations of probability b. Every conditional occupation probability
outside any region is at most b, and all joint occupation probabilities are
at most b^|A|. Nevertheless distinct sites have covariance b^2/4 regardless
of separation. Its occupation generating function is
(1+product_x(1+b z_x))/2; choosing 1+b z_x=exp(i pi/n) gives a zero with
|z_x| tending to zero as n grows. Thus bounds of the probabilistic form
proved here, by themselves, do not imply analytic locality or a fixed
complex product radius. This auxiliary counterexample is not the actual
finite-range gauge law, not a no-go result for it, and not a numerical test.

The discarded approaches are recorded in the routes note. In particular,
a fixed-width reset with a maximum exterior amplitude did not pay CS27;
using local q without its full brick collars would leave an uncharged energy;
and a whole-torus U0 comparison would have left an extensive curvature loss.
OC3, OC4 and the finite shell cover repair those specific steps. There is no
unreported Gaussian or arbitrary-boundary-smallness assumption.

The relevant primary comparisons are precise. [Bałaban, CMP122(1989),
printed356--358](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf)
analyzes the denominator action using constrained stationarity and localized
quadratic forms before exponentiation. The constraints and analytic coarse
extension differ from this original soft-cut law; our compact cap and shell
growth are proved here. [Dimock1212.5562v2, section3.13](https://arxiv.org/html/1212.5562v2#S3.SS13)
localizes both the covariance/background and separates bulk and boundary
terms. Its attachment of full exterior components uses distance modulo
holes, which is not the full-cardinality reader norm in OC19. Neither paper
supplies the remaining history or complex-return step by citation.
[Scott--Sokal, cond-mat/0309352v2, Theorem1.2 and section4.1](https://arxiv.org/html/cond-mat/0309352v2#S4.SS1)
distinguishes conditional avoidance from independence. OC21--OC24 rebuild
the needed elementary real induction for this measure; their independent-set
polynomial is not identified with our Wilson-source partition function.

No numerical experiment is used. The source and read receipt will freeze
this analytic unit for a DIFFERENT fresh reviewer. All previous CC, CS, GC,
SA, CB, H, FR and IC artifacts are untouched; GC's separately frozen metric
correction and review are bound separately from its historical author source.
Full 4D existence and the physical continuum mass gap remain OPEN.

[PROCESS_LIGHT](PROCESS_LIGHT.md) governs. Only this source and
checks/outside_chart_return_* are authored. See the
[routes note](checks/outside_chart_return_routes.md),
[read manifest](checks/outside_chart_return_read_manifest.json) and
[receipt](checks/outside_chart_return_receipt.json). No Git, shared-front,
audit, ledger, lock or PR edit is part of this unit.
