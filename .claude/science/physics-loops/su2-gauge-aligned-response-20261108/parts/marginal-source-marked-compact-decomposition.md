# Source-marked compact insertions for the seven-edge marginal

Author proof, 2026-11-09; conditional on the pinned compact coercivity and
actual reader templates recorded below. Independent mathematical checking
pending; no retained status is asserted. Assigned HEAD:
`c0497327ec81143f6f8b5369c86583ad3387d785`.

This rebuilds the real first-successful-shell and simultaneous resummation
method of `two-step-compact-polymer-decomposition.md` and
`source-marked-compact-decomposition.md` for the actual marginal. Credit for
the architecture remains with those authors and their recorded historical
HC10–HC21 source; Bałaban localization and Dimock's exposition are its stated
antecedents. No old all-terminal probability comparison or imported
connected-log theorem is used. The old proofs were read in full as methods.

## 0. Actual factors, shell scale, and the regional energy payment

Fix odd L≥3, κ>0, m≥3, and the permitted terminal-block forest with arbitrary
internal trees. The fine torus side is L²m. J is the seven distinct terminal
edges of two adjacent distinct plaquettes; O=E2\J; all O outputs are I.
The quotient coordinates are all fine non-tree and intermediate links.
Their product probability Haar measure is da. There are
M=3L^8+1+4L^4 coordinates owned by each terminal cell (tail ownership).
Set b_e=1−w(a_e), T_x=sum_owned b_e, T_A=sum_(x in A) T_x.
Modulo one field-independent positive constant, the ACTUAL density is

    w_J(a)=exp(−u E_J(a)) product_(all K0 and K1,c with c in O) H(κu r_c),
    E_J=W0+κ sum_(same surviving kernels)(r_c−<output_c,M_c>),
    H(t)=exp(t)/Z(t), Z(t)=integral_SU(2) exp(t w(Q))dQ.   (M1)

Thus w_J is exactly rho_J=q_u K0 product_(c in O)K1,c(I|U1) up to that
constant. Every K0 output remains hidden; every surviving radial normalizer
remains; no J numerator or normalizer remains. Zero means are allowed.

Use terminal-cell periodic l-infinity distance. For any cell region R,
select every whole surviving factor whose full syntactic reduced reader
meets its coordinate set Q_R^coord. This includes normalizer readers and
hidden outputs even if a selected factor happens to be conditionally
constant. Its exterior readers lie in B=N_1(R)\R. With n=M|R| and actual
surviving selected kernel count k_R^J, the exact regional factor is

    w_R=exp(−u E_R^J) product_(selected surviving c) H(κu r_c).

The fully read marginal-regional supplier proves

    E_J≥c_J T_all, c_J>0,
    E_R^J≥c_J T_R−K_E T_B,
    E_R^J≤K_E(T_R+T_B),
    κ sum_selected(1−r_c)≤K_r(T_R+T_B),                (M2)
    K_E=24+9κ(5L+1)^2, K_r=9κ(5L)^2.

For clarity the localization step is not an all-terminal comparison:
replace coordinates outside R union B by I; the selected factors are
unchanged, omitted surviving energies cost at most K_E T_B, and apply
E_J≥c_J T_all to this replaced field. The normalizer comparison follows
from (log H)'=1−E_t w in [0,1], by symmetry of probability Haar:
H(κu)e^(−κu(1−r))≤H(κu r)≤H(κu).

Fix A_scale>5/2, p=log(2+u)^A_scale, ρ=u^(−1/2)p and q=ρ²/(2π²).
The product chart C is a_e=exp(i z_e·σ) with each real component |z_e,k|<ρ.
Take sufficiently large u that sqrt(3)ρ is within injectivity and within
the fixed δ chart of the marginal nonlinear supplier. The latter's
covariance theorem is not used here. A cell is good iff T_x<q, bad iff
T_x≥q. Principal angle θ obeys θ²≤π² b_e/2, hence good implies θ<ρ/2
for each owned link. Thus all-good implies chart, never the converse.

Put C_shell=2K_E+K_r, α=min(1,c_J/(4C_shell)), V_K=(4K+1)^4 and
choose K as the LEAST positive integer satisfying

    (1+α)^K q > 2M(4K+1)^4.                           (M3)

Existence follows from exponential growth; K=O(1+log(1/q)), because
K=ceil(Cα(1+log(1/q))) satisfies the inequality at small q whenever
Cα>2/log(1+α). All subsequent quantities use this prescribed least K.

For core A and 0≤j<K put I_j=N_(2j)(A), R_j=N_(2j+1)(A),
S_j=N_(2j+2)(A)\R_j. The selector ell_(A,j) is the product of indicators:
all cells of A bad; all cells of R_j\A good; T_Sj≤α T_Ij;
and T_Si>α T_Ii for every i<j. Earlier tests lie within R_j.
For R=R_j, its physical collar is S=S_j. Fix a good real exterior on S.
Take 0<d0≤1 fixed and increase u so (π/2)d0<p. The chord cap
|a_e−I|≤d0/sqrt(u) lies in C. Its Haar mass is at least
(c_cap d0³)^n u^(−3n/2), since SU(2) Haar radial density is
(2/π)sin²θ dθ. The actual zero-source CHART denominator obeys

    I_R(0;z)≥H(κu)^(k_R^J)
      exp[−(K_E+K_r)u T_S−(K_E+K_r)n d0²/2]
      (c_cap d0³)^n u^(−3n/2)>0.                      (M4)

The compact numerator with ell has H(κu)^(k_R^J) as its upper prefactor.
Combining its energy with the denominator collar cost, ON ell,

    c_J T_R−C_shell T_S
      ≥(c_J/2)T_R+(c_J/2)T_I−C_shell T_S
      ≥(c_J/2)T_R+(c_J/4)T_I
      ≥(c_J/2)T_R+(c_J/4)q|A|.                       (M5)

This spends the shell payment while T_I is still variable, extracts ONE
fixed core charge, and retains (c_J/2)T_R for integration. For each link

    integral exp[−(c_J u/2)b(a)]da ≤ K_H u^(−3/2),     (M6)

using b=1−cosθ≥2θ²/π², sin²θ≤θ² and extending the radial Gaussian
integral to infinity. Divide by (M4): exactly the SAME actual k_R^J powers
of H and the SAME n Haar powers cancel. Therefore each compact, chart,
or compact-minus-chart selector integral divided by I_R(0;z) is between
zero and

    C^|R| exp[−c_J u q|A|/4],                         (M7)
    C=max(1,[exp((K_E+K_r)d0²/2)K_H/(c_cap d0³)]^M).

The difference here is the single integral over compact coordinates
outside the regional product chart, with the same selector and exterior;
it has no factor two. The chart denominator is never the complement of
an entire-core-rough event. Regions may wrap or equal the torus. Empty
collars simply have T_S=0 and all estimates remain valid.

## 1. Four fixed insertions and their domains

Use the actual seven-edge-deleted marginal specified in §0, with β=u,
both surviving kernel strengths κu, terminal exterior I, and no cut. All integration variables remain REAL compact group
variables, or real variables in the fixed product logarithm cube C. The cube, q, α and least K of §0, and all selectors, are independent
of sources. In particular K=O(log(1/q)); the physical reader radius is one.

Let X_1=F, X_2=G, X_3=A_c and X_4=A_d be bounded REAL functions on the
full compact quotient, with distinct c,d in O and

    A_c(a)=κu <i v_c·σ_Pauli,M_(1,c)(a)>, |v_c|=1,     (S1)

and the analogous definition for d. These scores are fixed functions
evaluated at terminal identity; no terminal-field parameter is varied in
this decomposition. F,G here are fixed bounded measurable quotient functions with bounded
complete reader supports. No field analyticity is needed. Reconstruction
of general original orbit-dependent sources is a separate task; separate
source means are not substituted here.

Let S_i be each source's complete syntactic retained-coordinate support,
expressed as its owned terminal-cell set. Fix an integer D≥1 bounding all
nonempty S_i diameters in periodic l-infinity distance, uniformly in volume.
Retain their finite cardinality bounds as part of the source class. Empty
S_i means a constant function, discussed explicitly below. Write

    L_i=||X_i||_infinity,  ε=1/16,
    U_ε={ξ∈C^4: Σ_i |ξ_i|L_i<ε},
    w_ξ(a)=w_J(a) exp[Σ_i ξ_i X_i(a)].                   (S2)

The convenient polydisc |ξ_i|<ε/(4 max(1,L_i)) lies in U_ε. For the score
parameters one can in particular choose radii ε/(4 max(1,κu)), and the F,G radii are fixed for
fixed norm bounds. All analyticity statements are in ξ, at each fixed u,
with volume-independent norm-controlled radii. No field-variable analytic
regularity is claimed.

Define Z_c(ξ)=integral_compact w_ξ and Z_a(ξ)=integral_C w_ξ. All integrals
are entire functions before division, by bounded differentiation on compact
real domains. For any subset B_labels of source labels, at every real configuration,

    |Σ_(i∈B_labels)ξ_iX_i|≤ε,
    Re exp[Σ_(i∈B_labels)ξ_iX_i]≥e^(−ε)cos ε>0.              (S3)

Thus regional and global integrals against the positive zero-source density
lie in a common phase wedge; in particular Z_c,Z_a never vanish on U_ε.
The normalized chart functional below is complex and is not assigned total
variation one or a probability interpretation.

## 2. Source-aware separation and whole-factor allocation

Define the source-aware core connectivity radius by

    d_conn=4K+2D+4.                                    (S4)

Cores are connected in this distance-d_conn graph. Shells remain
I_j=N_(2j)A, R_j=N_(2j+1)A and S_j=N_(2j+2)A\R_j for 0≤j<K.
Use exactly the same local selector ell_(A,j): A bad, R_j\A good,
first successful T_(S_j)≤α T_(I_j), and failures at smaller indices.
A history h is an unordered finite family of pairs (A,j), with nonempty
cores connected in this graph, pairwise core distance >d_conn, and 0≤j<K.
Include the empty history. Define R_h=union_(h)R_j(A), O_h=torus\R_h and

    Π_h=1_good(O_h) product_(h) ell_(A,j).

Then sum_h Π_h=1 pointwise on the entire compact space. To prove this,
take the actual bad set and its unique d_conn-connected components A.
Every cell of N_(2K)(A)\A is good because 2K<d_conn. If all K shell
tests fail, I_(j+1) contains the disjoint I_j and S_j, so
T_I(j+1)>(1+α)T_Ij and T_IK>(1+α)^K q|A|. But
T_IK≤2M|N_(2K)(A)|≤2M V_K|A|, contradicting (M3). Hence there is a
unique first successful j. Its selector holds, producing a history with
Π_h=1. Conversely a nonzero Π_h identifies all bad cells exactly as the
union of its cores: separation and connectedness identify their unique
components, and the earlier failures identify j uniquely. The all-good
configuration belongs only to the empty history. Threshold equality T_x=q
is bad, and a successful equality T_S=α T_I is assigned to the first
success. Saturated torus balls still obey the volume bound; once S is
empty the success condition holds. No source affects this partition.

Regions belonging to distinct history cores obey

    dist(R_j(A),R_l(B))≥(d_conn+1)−2(2K−1)=2D+7.       (S5)

For a region R, assign to it every WHOLE physical factor touching Q_R^coord and
also each entire source factor exp(ξ_iX_i) whose full support S_i meets R.
Define the latter label set L(R)={i:S_i∩R≠empty}. No source can meet two
active regions: such a support would have diameter at least 2D+7>D.
The radius-one physical reader property likewise prevents a surviving
physical factor from meeting two active regions.
Splitting a source into fragments, or assigning it by a preferred endpoint,
is neither needed nor allowed. For a history h the exact identity is

    w_ξ=W_out,h(ξ) Π_(R∈h) w_R,ξ,
    w_R,ξ=w_R exp[Σ_(i∈L(R))ξ_iX_i].                   (S6)

W_out,h contains all untouched original physical factors and every source
factor whose support meets no active region. In particular a constant X_i
with empty support is ALWAYS in W_out,h. It remains in both global partition
functions and in the normalized source generating functional; it has not
been silently set to zero as a source-only vacuum.

The exterior coordinate reader set of w_R,ξ and its regional integrals is
contained in

    Q_R=N_D(R)\R.                                    (S7)

This includes the physical collar N_1(R)\R and every exterior coordinate of
each FULL assigned source support. For R=R_j(A), all such readers are in
N_(2K−1+D)(A)\R. Equation (S5) ensures they cannot be in any other active
region, including an unselected region in a history containing this core.
Membership of a source label in L(R) is fixed geometric data independent of
fields and ξ, including at configurations where that source happens to be
constant. Every originally assigned source parameter and its full support
remain attached to the regional label even if a later cancellation removes
its dependence from a numerical ratio.

## 3. Nonzero regional denominators and compact-complement bounds

Fix R=R_j(A) and a real exterior z. Define

    I_R(ξ;z)=integral_(C on Q_R^coord) w_R,ξ dH,
    N^c_(A,j)(ξ;z)=integral_(compact Q_R^coord) ell_(A,j) w_R,ξ dH,
    N^a_(A,j)(ξ;z)=integral_(C on Q_R^coord) ell_(A,j) w_R,ξ dH,
    N^out=N^c−N^a,
    B^c_ξ=N^c/I_R, B^a_ξ=N^a/I_R, D_ξ=N^out/I_R.       (S8)

All physical factors and selected source functions occur inside the SAME
regional integrals, with the same exterior. These are not zero-source
normalizers with externally appended marks. By (S3),

    |I_R(ξ;z)|≥Re I_R(ξ;z)≥cos ε e^(−ε) I_R(0;z)>0.   (S9)

Hence B^c_ξ,B^a_ξ,D_ξ are analytic in ξ on U_ε. The difference N^out is
literally the one integral on compact Q_R^coord minus its product-chart subset,
with the same real selector and marked density. Consequently

    |N^out(ξ;z)|≤e^ε N^out(0;z),                       (S10)

and the analogous estimates hold for N^c,N^a. This uses the positive
zero-source complement measure; it does not bound a difference of two
unrelated absolute integrals and introduces no factor two.

By the construction in §0, extend all three ratios by zero off the
q-good PHYSICAL shell S_j. This zero extension is independent of ξ and
preserves analyticity pointwise in the exterior, together with
B^c_ξ=B^a_ξ+D_ξ. No smallness condition on the additional source exterior
readers is needed for (S9)–(S10), because X_i are globally bounded on real
compact fields. In the exact resummation those readers will in fact lie in
the imposed good annulus, as checked next.

Let C be the regional constant in (M7) and W_ε=e^(2ε)/cos ε.
For each admitted exterior, the actual marginal energy/Haar calculation (M4)–(M7) and
(S9)–(S10) imply

    |B^c_ξ|, |B^a_ξ|, |D_ξ|
        ≤W_ε C^|R| exp[−c_Ju q|A|/4]
        ≤C_ε^|R| exp[−c_Ju q|A|/4],                  (S11)

where C_ε=C W_ε and |R|≥1. Thus the only new price is a fixed factor per
core, absorbable into a volume-independent regional constant. The original
exact H(κu)^k and Haar u powers were already canceled within (M7); all
source factors and their normalization are retained in (S8). At ξ=0 the
unmarked real nonnegativity is recovered. For complex ξ the ratios and
polymer weights below need not be nonnegative.

## 4. Exact common-chart identities with complex weights

Define the normalized complex chart functional by

    <f>_(a,ξ)=Z_a(ξ)^(-1) integral_C f(a) w_ξ(a)dH.     (S12)

Its denominator is nonzero by (S3). This notation is an integration
functional, not a positive conditional probability. The history partition
is pointwise on real fields, and (S6) is a pointwise factorization of the
original complex integrand. Conditional integration over separated active
chart regions gives the actual product Π_R I_R(ξ), so finite conditional-integration algebra gives

    Z_c(ξ)/Z_a(ξ)=Σ_h <1_good(O_h) Π_(h)B^c_ξ>_(a,ξ),
               1=Σ_h <1_good(O_h) Π_(h)B^a_ξ>_(a,ξ).   (S13)

The q-good zero extension is harmless: each physical shell is in O_h.
All-good exterior coordinates lie in C, ensuring the compact and common-
chart exterior domains in the first identity agree. No complex fine point
is inserted in a source, predicate, path mean or Haar factor.

The empty-history contribution is Z_good(ξ)/Z_a(ξ) in BOTH identities;
it is not one in general. This retains any field-independent or source-only
factor in the original density. Because all sums and domains are finite,
Fubini and absolute integrability justify the algebra; no positivity of the
complex functional, total-variation-one estimate or infinite-volume
convergence theorem is invoked.

For a selected family s define exactly

    R_s=union_(s)R_j(A),
    H_s=(union_(s)N_(d_conn)(A))\R_s.                  (S14)

Every exterior reader of every selected source-marked regional ratio lies
in H_s. Indeed Q_R⊂N_(2K−1+D)(A)\R⊂N_(d_conn)(A)\R, and (S5)
prevents Q_R from meeting any other selected region. This checks more than
the physical-shell inclusion: entire assigned source supports are retained.
The same separation prevents Q_R from meeting any additional active region
of a history containing s. Thus the selected I_R(ξ) and D_ξ are constant
in each additional region when it is integrated or restored.

The exact resummation identity is

    Σ_(h contains s)<1_good(O_h) Π_(s)D_ξ Π_(h\s)B^a_ξ>_(a,ξ)
           =<1_good(H_s) Π_(s)D_ξ>_(a,ξ).              (S15)

To verify it, first integrate every selected region as an unrestricted
DUMMY chart region. Its selector and compact-minus-chart integration have
already been incorporated in D_ξ, and its actual I_R(ξ) must therefore
remain uncapped. It depends only on Q_R (a geometric envelope, not necessarily a minimal support). On the remaining variables,
good(H_s) excludes bad cells within d_conn of any selected core. The remaining
bad components are exactly the additional cores allowed in a history
containing s. Their first-shell tests use N_(2K), disjoint from selected
regions, so their first successful indices are unaffected by the dummy
integration. Source supports do not change those tests. Complete additional
region factorization still holds, now including their uniquely assigned
whole source factors, and selected I_R(ξ),D_ξ are constant during each such
integration by the preceding paragraph. Summing their chart histories
therefore partitions these remaining real domains exactly.

As in the prior architecture, N_(d_conn)(A) may meet an UNSELECTED active
region but cannot contain its bad core; that intersection lies in its
region-minus-core and is already good under its selector. If it meets
another SELECTED region, its good condition must instead be removed, because
those variables are dummy. Removing ALL R_s in (S14) enforces exactly this
rule. The extra source readers do not reintroduce any selected-region
condition: (S5) excludes them from other selected regions. Thus the argument
is a fixed-domain identity for the complex marked density, not an analytic
continuation of an unproved real conditional probability argument. The
empty selected family in (S15) resums to one, in contrast to the individual
empty history in (S13).

## 5. Complete marked readers and the exact analytic insertion gas

Set

    Γ_A=N_(d_conn+D+2)(A).                              (S16)

This larger than necessary geometric envelope contains each regional
physical factor, every selected source's FULL S_i, all physical/source
exterior readers Q_R, and every absence/failure predicate in (S14). Attach
to the regional label the full list L(R) of original source parameters and
the full S_i for each i∈L(R); those are not replaced by c,d or by a preferred
source endpoint. Parameter labels remain even when a ratio happens to be
independent of them. Sources assigned to W_out retain their original labels
in the common chart functional. The original source labels have not been
reindexed as new blocked observables.

A polymer label g is a nonempty separated family of pairs (A,j), with
pairwise core distance >d_conn and connected Γ_A-overlap graph. Retain its
entire list, not only its union set. Write

    Γ_g=union_(g)Γ_A, n_g=Σ_(g)|A|,
    H_g=(union_(g)N_(d_conn)(A))\(union_(g)R_j(A)),
    Θ_g(ξ)=1_good(H_g) Π_(g)D_(A,j)(ξ).                (S17)

Define Θ_g=0 off good(H_g) before evaluating the ratios. This predicate is
fixed in ξ, so Θ_g is analytic in ξ pointwise on real chart fields, with
live coordinate arguments in H_g and complete native labeled reader Γ_g.
The assigned source-support lists are part of this reader declaration.
If H_g is empty, any resulting field-independent analytic coefficient is
retained with its nonempty native Γ_g and source labels.

Compatibility is disjointness of Γ_g. A selected family splits uniquely
into Γ-overlap groups. Conversely a compatible family of labels reconstructs
a unique separated selected family: any cross-group distance conflict or
annular/active-region intersection would force Γ overlap. The same geometric
fact gives H_s as the disjoint union of H_g. Hence (S13)–(S15) imply exactly

    Z_c(ξ)/Z_a(ξ)
       = < Σ_(Γ-compatible families F) Π_(g∈F)Θ_g(ξ) >_(a,ξ).     (S18)

Every field and every selector in (S18) is real. The empty polymer family
contributes one after resummation. All families are finite for a fixed finite
torus, and all regional/global denominators are nonzero on U_ε. Therefore
(S18) is an identity of analytic functions on U_ε, not merely equality of
a fixed number of formal coefficients. It also holds as an identity of
formal Taylor series at zero.

The uniform marked activity bound is

    |Θ_g(ξ)|≤exp[(log C_ε)V_K n_g−c_Ju q n_g/4],        (S19)

with complete-reader size bounds

    |H_g|≤(8K+4D+9)^4 n_g,
    |Γ_g|≤(8K+6D+13)^4 n_g.                            (S20)

The second expression is 2(d_conn+D+2)+1 to the fourth power; the first
is 2d_conn+1 to the fourth power. Fixed D does not change K=O(log u).
Since V_K=O(log(u)^4) while u q=log(2+u)^(2A_scale)/(2π²),
A_scale>5/2 implies (log C_ε)V_K≤c_J u q/8 for all sufficiently large u.
Increasing the lower threshold accordingly, (S19) improves to

    |Θ_g(ξ)|≤exp[−c_Ju q n_g/8].                        (S21)

The constants do not depend on volume, positions of the four bounded-size
source supports, or u except through the displayed q,K and the specified
source-parameter radii. The norm bounds L_i and diameter ceiling D define
the admitted source class. No independent scalar-activity factorization of
the common chart functional is asserted; its source dependence remains
part of (S18).

## 6. Normalized source coefficients and the distinct-boundary identity

The ordinary normalized generating function of the actual compact law is
Z_c(ξ)/Z_c(0). Its logarithm has the same positive-degree Taylor coefficients
as log Z_c(ξ), and

    ∂_(ξ1)∂_(ξ2)∂_(ξ3)∂_(ξ4) log Z_c(ξ)|_(ξ=0)
       =κ4(F,G,A_c,A_d).                               (S22)

The phase wedge permits an analytic logarithm of each global integral near
zero, with its branch fixed by its positive value there. Locally the exact
identity (S18) gives log Z_c=log Z_a+log(right side of S18), with consistent
branches. It does NOT permit dropping the full source-dependent log Z_a:
marks can fall on that chart law, on its normalization, and on the regional
ratios. A source factor wholly outside a particular region may cancel from
that particular ratio, but remains in the global generating function and
in the correct common-chart factorization.

For empty-support X_i=k_i, write v(ξ)=exp(sum_empty ξ_i k_i).
Then Z_c(ξ)=v(ξ) Z_c,nonempty(ξ) and Z_a(ξ)=v(ξ) Z_a,nonempty(ξ).
The factor cancels in Z_c/Z_a and in the normalized chart functional, but
Z_c(ξ)/Z_c(0) retains v(ξ). Thus constant-source linear coefficients are
correct, and their mixed fourth cumulants vanish by differentiation.
Nothing was discarded before this cancellation.

Writing R_ins(ξ) for the entire right side of (S18), the exact NORMALIZED
insertion identity is

    Z_c(ξ)/Z_c(0) = [Z_a(ξ)/Z_a(0)] [R_ins(ξ)/R_ins(0)].       (S24)

Here R_ins(0)>0, and R_ins(ξ)=Z_c(ξ)/Z_a(ξ) is nonzero on U_ε. Analytic logarithms
near zero therefore give log Z_c−log Z_c(0) as the sum of the two normalized
logarithms in (S24). This preserves all chart-law and normalization marks.
The coefficient for four distinct labels is the actual marginal cumulant
κ4(F,G,A_c,A_d). Since c,d are distinct surviving terminal edges and the
source functions are held fixed, it also equals the mixed terminal/source
jet at identity whenever that jet is formed from the corresponding actual
marginal partition function: the log-weight derivatives are F,G,A_c,A_d,
and every derivative involving two distinct labels is zero (the output
normalizers are independent of terminal outputs). Thus the ordinary joint
cumulant formula applies. This is a coefficient identity, not equality
of finite terminal variations with score tilts.

## 7. Limits and author checkpoint

Closed at author-proof level: uniform regional/global nonvanishing by the
phase wedge; source-complete whole-factor allocation; enlarged core/readers
preventing a source from reading two active regions; compact-complement
bounds with only a fixed per-core factor; exact simultaneous resummation on
fixed real domains; and the analytic four-source insertion-gas identity.
All supplier notes remain unmodified; least K was rebuilt with c_J.

The geometry would fail if one kept separation seven while allowing an
arbitrary source diameter: one source could then couple two active regions
and invalidate the product of regional denominators. Equations (S4)–(S7)
explicitly prevent that case. Empty source supports, zero-norm sources,
zero compact means, wrapped regions and whole-torus regions are included.
The polydisc uses max(1,L_i) to handle zero norms without division by zero.

The independent checker should examine entire-source allocation, the
source-reader inclusion in H_s, the complex conditional algebra and the
nonvanishing denominator bound. No connected-log norm, density-forest
hypothesis, uniform connected-correlation estimate, physical gap, transported
chart, inherited multi-step closure, or noninvariant-source orbit theorem
is assumed or proved here. Those require their own arguments; bounded
analytic insertions are inputs to such work, not its conclusion.

## 8. Source identities, coverage and handoff

The source identity below is the assigned worktree HEAD, not a claim of a
fresh network fetch. No network, commits, pushes, audits, numerical jobs or
other tracked edits were performed by this worker. The supervisor supplied
the science lease and passed preflight. Repo AGENTS.md, SCIENCE_WORKFLOW.md,
workhorse/SKILL.md and SKILL_FRESHNESS_CHECK.md were read; the task uses that
repo procedure rather than the differing installed distribution copy.
The three procedure files were byte-compared with supplied current-main
`bf92a1d763030836ed55631d5d7a7ef3b288f284` and all matched.

Mathematical source SHA-256 values (relative to this pack):

| Source | Actual coverage | SHA-256 |
|---|---|---|
| `parts/marginal-regional-moments-and-ratios.md` | Full, 432 lines; load-bearing (M1)–(M2) supplier | `b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f` |
| `parts/marginal-nonlinear-chart-estimates.md` | Lines 1–180; statement and fixed real domain only, no covariance theorem used | `b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7` |
| `parts/two-step-compact-polymer-decomposition.md` | Full, 359 lines; method checked and rebuilt | `1e3772f4781fa082de6d117e8f61adef616deb00fe293bbd01e07f030107d54e` |
| `parts/source-marked-compact-decomposition.md` | Full, 373 lines; source-allocation/resummation method checked and adapted | `c6299e40fb15b87d5d01a007467e11468da72e949dd164b35f22ea0665f4fa8e` |
| `sources/connected-response-literature-scan-20261109.md` | Bounded exact rereads lines 1–20 and 125–160; earlier combined display truncated, not counted as full | `3826e5a46894f25f168992304c71658114668829d45649a8b9eea0b903d5553d` |
| `sources/frozen-forest-literature-addendum-20261109.md` | Full 29 lines; search provenance only | `238180b21668096a1715d913d9e602543011ad799fd66590316039cf1c130bcd` |

The parent supplied the preliminary literature comparison; the existing
search records were reused. Abdesselam–Procacci–Scoppola, Lohmann, and
Abdesselam–Rivasseau provide architectural comparisons with differing
Gaussian/model/insertion hypotheses, not an imported theorem here. No new
external result was needed for the finite partition, phase-wedge or regional
ratio arguments. The conditional dependency is precisely the actual
quotient law/Haar ownership, c_J coercivity, and full radius-one/incidence
reader templates in the fully read marginal-regional supplier. That
supplier's upstream geometric proof was not independently re-proved here.

Author checks performed: reread the resulting entire argument, followed the
single energy payment (M5), matched actual k_R^J and n powers across (M4)–(M7),
checked whole-source separation by (S5), and followed the simultaneous
conditional integration with ALL selected dummy regions removed in (S14).
These are author reasoning checks, not independent certification. In
particular no dummy chart integral is capped; no good-event complement is
substituted for C; and the unresummed empty history is Z_good/Z_a while only
the fully resummed empty insertion family equals one. If the torus is
smaller than the geometric radii, the same distance/volume inequalities
hold and any saturated region forbids a second separated core. Sources
and field-free insertion coefficients retain their native labeled readers.

Current checkpoint: conditional author proof of the real-domain marginal
insertion representation (S18), normalized identity (S24), and activity
bound (S19) is complete. Parent line-by-line inspection and an independent
mathematical check remain due. No scalar-activity independence,
connected-log/tree norm, or general original-orbit reconstruction is
claimed. Only this deliverable was edited; no editable prompt files or
platform instructions were changed.
