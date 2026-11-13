# Source-marked compact decomposition on fixed real domains

Author proof, 2026-11-09; independent check pending. This extends only the
real-domain compact-insertion construction in
`two-step-compact-polymer-decomposition.md`, read in full at SHA-256
`1e3772f4781fa082de6d117e8f61adef616deb00fe293bbd01e07f030107d54e`.
That note is preserved, including its prescribed LEAST-K choice. Its prior
architecture is HC10–HC21 of `HOLOMORPHIC_COMPACT_RETURN_ASTRA.md` at
`89faef229ff6e6bde42baad15ed8270c2f4087d8`; credit and the Bałaban/Dimock
antecedents remain as recorded there. This extension proves source-parameter
analyticity and exact marked identities, not the historical holomorphic-field
or connected-log consumer claims. Only this new file is written; no Git,
network or numerical action is used.

## 1. Four fixed insertions and their domains

Use the full compact two-hidden-layer quotient at terminal V=I from the
unmarked note, with β=u, both kernel strengths κu, no cut, and every
normalizer retained. All integration variables remain REAL compact group
variables, or real variables in the fixed product logarithm cube C. The
cube, q, α, K, I_j,R_j,S_j, and selectors are independent of all sources.
In particular K is the least positive integer satisfying the unmarked (P3),
so K=O(log(1/q)). We change the core connectivity radius below, not the
shell increments, energy, or physical reader radius one.

Let X_1=F, X_2=G, X_3=A_c and X_4=A_d be bounded REAL functions on the
full compact quotient, with c≠d and

    A_c(a)=κu <i v_c·σ_Pauli,M_(1,c)(a)>, |v_c|=1,     (S1)

and the analogous definition for d. These scores are fixed functions
evaluated at terminal identity; no terminal-field parameter is varied in
this decomposition. Original F,G must be invariant under the shared
root-fixed gauge group ℋ, so they are genuine quotient functions. C² local
original F,G are permitted, but this argument needs only bounded measurable
quotient functions with bounded local reader sets. It does NOT require
analyticity in the fine fields or extend those functions to complex fields.
Global conjugation invariance alone does not replace ℋ invariance; original
noninvariant sources require a separate orbit reconstruction, not projection
onto separate source means.

Let S_i be each source's complete syntactic retained-coordinate support,
expressed as its owned terminal-cell set. Fix an integer D≥1 bounding all
nonempty S_i diameters in periodic l-infinity distance, uniformly in volume.
Retain their finite cardinality bounds as part of the source class. Empty
S_i means a constant function, discussed explicitly below. Write

    L_i=||X_i||_infinity,  ε=1/16,
    U_ε={ξ∈C^4: Σ_i |ξ_i|L_i<ε},
    w_ξ(a)=w(a) exp[Σ_i ξ_i X_i(a)].                   (S2)

The convenient polydisc |ξ_i|<ε/(4 max(1,L_i)) lies in U_ε. Its score
radii are of order 1/u since L_3,L_4≤κu, and the F,G radii are fixed for
fixed norm bounds. All analyticity statements are in ξ, at each fixed u,
with volume-independent norm-controlled radii. No field-variable analytic
regularity is claimed.

Define Z_c(ξ)=integral_compact w_ξ and Z_a(ξ)=integral_C w_ξ. All integrals
are entire functions before division, by bounded differentiation on compact
real domains. For any subset J of source labels, at every real configuration,

    |Σ_(i∈J)ξ_iX_i|≤ε,
    Re exp[Σ_(i∈J)ξ_iX_i]≥e^(−ε)cos ε>0.              (S3)

Thus regional and global integrals against the positive zero-source density
lie in a common phase wedge; in particular Z_c,Z_a never vanish on U_ε.
The normalized chart functional below is complex and is not assigned total
variation one or a probability interpretation.

## 2. Source-aware separation and whole-factor allocation

Replace the unmarked core connectivity radius by

    d_conn=4K+2D+4.                                    (S4)

Cores are connected in this distance-d_conn graph. Shells remain
I_j=N_(2j)A, R_j=N_(2j+1)A and S_j=N_(2j+2)A\R_j for 0≤j<K.
Use exactly the same local selector ell_(A,j): A bad, R_j\A good,
first successful T_(S_j)≤α T_(I_j), and failures at smaller indices.
The shell-growth argument uses only 2K<d_conn and the same (P3), so the
pointwise identity Σ_h Π_h=1 remains exact for these enlarged components.
The actual bad set has unique d_conn-components and each has a unique first
successful j. No source-dependent threshold or selector has been introduced.

Regions belonging to distinct history cores obey

    dist(R_j(A),R_l(B))≥(d_conn+1)−2(2K−1)=2D+7.       (S5)

For a region R, assign to it every WHOLE physical factor touching J_R and
also each entire source factor exp(ξ_iX_i) whose full support S_i meets R.
Define the latter label set L(R)={i:S_i∩R≠empty}. No source can meet two
active regions: such a support would have diameter at least 2D+7>D.
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

    I_R(ξ;z)=integral_(C on J_R) w_R,ξ dH,
    N^c_(A,j)(ξ;z)=integral_(compact J_R) ell_(A,j) w_R,ξ dH,
    N^a_(A,j)(ξ;z)=integral_(C on J_R) ell_(A,j) w_R,ξ dH,
    N^out=N^c−N^a,
    B^c_ξ=N^c/I_R, B^a_ξ=N^a/I_R, D_ξ=N^out/I_R.       (S8)

All physical factors and selected source functions occur inside the SAME
regional integrals, with the same exterior. These are not zero-source
normalizers with externally appended marks. By (S3),

    |I_R(ξ;z)|≥Re I_R(ξ;z)≥cos ε e^(−ε) I_R(0;z)>0.   (S9)

Hence B^c_ξ,B^a_ξ,D_ξ are analytic in ξ on U_ε. The difference N^out is
literally the one integral on compact J_R minus its product-chart subset,
with the same real selector and marked density. Consequently

    |N^out(ξ;z)|≤e^ε N^out(0;z),                       (S10)

and the analogous estimates hold for N^c,N^a. This uses the positive
zero-source complement measure; it does not bound a difference of two
unrelated absolute integrals and introduces no factor two.

As in the unmarked construction, extend all three ratios by zero off the
q-good PHYSICAL shell S_j. This zero extension is independent of ξ and
preserves analyticity pointwise in the exterior, together with
B^c_ξ=B^a_ξ+D_ξ. No smallness condition on the additional source exterior
readers is needed for (S9)–(S10), because X_i are globally bounded on real
compact fields. In the exact resummation those readers will in fact lie in
the imposed good annulus, as checked next.

Let C be the fixed unmarked constant in (P11) and W_ε=e^(2ε)/cos ε.
For each admitted exterior, the unmarked energy/Haar calculation and
(S9)–(S10) imply

    |B^c_ξ|, |B^a_ξ|, |D_ξ|
        ≤W_ε C^|R| exp[−c_Eu q|A|/4]
        ≤C_ε^|R| exp[−c_Eu q|A|/4],                  (S11)

where C_ε=C W_ε and |R|≥1. Thus the only new price is a fixed factor per
core, absorbable into a volume-independent regional constant. The original
exact H(κu)^k and Haar u powers were already canceled within (P11); all
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
chart regions gives the actual product Π_R I_R(ξ), so the same finite
algebra as in unmarked (P13) gives

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
remain uncapped. It depends only on Q_R. On the remaining variables,
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

    |Θ_g(ξ)|≤exp[(log C_ε)V_K n_g−c_Eu q n_g/4],        (S19)

with complete-reader size bounds

    |H_g|≤(8K+4D+9)^4 n_g,
    |Γ_g|≤(8K+6D+13)^4 n_g.                            (S20)

The second expression is 2(d_conn+D+2)+1 to the fourth power; the first
is 2d_conn+1 to the fourth power. Fixed D does not change K=O(log u).
Thus on the same sufficiently-large-u type of domain, increasing its lower
threshold for C_ε if necessary, (S19) improves to

    |Θ_g(ξ)|≤exp[−c_Eu q n_g/8].                        (S21)

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

For the actual hidden-chain integral with original sources sF+tG and
terminal fields varied at distinct c,d, direct differentiation at V=I gives

    D_cD_d ∂s∂t log Z(V;s,t)|_(I,0,0)
        =κ4(F,G,A_c,A_d).                              (S23)

This is because the last-layer log-weight derivative at c is exactly (S1)
and D_d A_c=0 when c≠d; output-independent radial normalizers remain in
the hidden law. Thus the FIXED-score generating coefficient (S22) equals
the desired distinct-boundary coefficient at the stated point. No identity
between finite terminal variations and score tilts, no moving chart, and no
terminal complex neighborhood is needed. Repeated-link differentiation
would add a derivative-of-score term and is outside (S23).

For a normalized coarse conditional, the original exact relation remains
log p=log W−log Q. Its entire corresponding source/boundary coefficient
from log Q must be subtracted. This note treats the fixed-terminal Z_c and
its chart decomposition; it supplies no additional Q-law estimate. Empty-
support source functions remain as global factors exp(ξ_i X_i); their mixed
cumulants vanish as dictated by differentiation, not by erasing their
source-only terms before forming the generating function.

## 7. Limits and author checkpoint

Closed at author-proof level: uniform regional/global nonvanishing by the
phase wedge; source-complete whole-factor allocation; enlarged core/readers
preventing a source from reading two active regions; compact-complement
bounds with only a fixed per-core factor; exact simultaneous resummation on
fixed real domains; and the analytic four-source insertion-gas identity.
The zero-source parent remains unmodified at its pinned least-K revision.

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
