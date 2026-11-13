# Fixed-reference density forest for bounded compact insertions

Author derivation, 2026-11-09; decisive independent check pending. This is a
finite-volume analytic and combinatorial lemma, with the hypothesis contract
below. It is not a physical gap, a theorem about varying coarse backgrounds,
or an automatic transfer of a one-step construction to the two-step law.

The architecture comes from MK12–MK35 of
`MARKED_COMPACT_CHART_ASTRA.md` at
`89faef229ff6e6bde42baad15ed8270c2f4087d8`, read in full. Here the Gaussian
reference is FIXED at zero sources and terminal identity. All varied labels
occur only in explicit bounded functions. There is no moving critical point,
translation, surface flux, field derivative of an insertion, parity gain,
or source-dependent covariance. This allows a direct normalized-density
estimate in place of the historical density reader-list expansion. The
finite forest and hard-core logarithm arguments are given below, rather
than inferred from their historical names.

## 1. Hypothesis contract and what support means

Let Lambda be a finite periodic four-dimensional cell lattice, with at most
k real scalar coordinates per cell. The statements also hold for any finite
graph with the support and counting bounds stated here. All functions are
integrated on REAL coordinate spaces. The sources zeta range in a fixed
complex polydisc D; they never change those integration domains.

The normalized Gaussian covariance is a fixed real symmetric matrix

    C=P+E,  p0 I<=P<=U I,  range(P)<=R0.               (F1)

For every ordered scalar pair i,j, fix a connected nearest-neighbor path
Gamma_ij containing its endpoint cells. Put

    e_ij=exp(beta |Gamma_ij|)|E_ij|,
    e=sup_i sum_j e_ij,
    B=sup_x sum_(i,j:x in Gamma_ij) e_ij,              (F2)

where beta>0 is fixed, e<=p0/4 and B<infinity. Symmetry of E is required,
and Gamma_ij=Gamma_ji as CELL SETS: choose one path for each unordered pair.
This lets re-rooting preserve every path and matches the unoriented
edge-cut count. There is no assumption E>=0. Every entry
of C, P and E is independent of zeta and of all local fields. In particular
this lemma does NOT assert locality under varying action or coarse-field
parameters. Path supports record spatial connections in the covariance
forest, not an unproved local dependence of C on such parameters.

The chart is the product scalar cube Box_p, with p>0. There are two families
of bounded measurable, zeta-holomorphic functions:

* distinct local factors 1+W_v, with complete bounded coordinate reader
  sets J_v that are unions of WHOLE owner cells' coordinates; each W_v is
  extended by zero outside that whole-cell reader cube. A function reading
  fewer scalars is supplied with the remaining cell-body indicators before
  this extension, and its full-cell normalization cost is paid in (F5);
* compact labels g, with functions Theta_g of the coordinates in H_g,
  where H_g also denotes a union of WHOLE owner cells' coordinates,
  and nonempty native connected cell readers Gamma_g containing those cells.
  Theta_g is zero outside a fixed product cap on H_g contained in Box_p.
  Its source dependence uses only the source labels declared at Gamma_g.
  Field-independent Theta_g with nonempty Gamma_g are retained.

The exact object to be evaluated is

    Z_* = E_gamma_C[1_Box_p product_v(1+W_v)
                    sum_(Gamma-compatible F) product_(g in F)Theta_g],
    Z_a = E_gamma_C[1_Box_p product_v(1+W_v)],          (F3)

with compatibility meaning disjoint native Gamma_g. All source supports
of W_v and Theta_g are included in their declared geometric readers, even
when numerical cancellation reduces an individual function's dependence.
One may retain additional fixed syntactic readers. The common external
Gaussian/Haar/vacuum prefactor of a physical realization is not included
in (F3); it must be restored exactly once and cancels in Z_*/Z_a.

A constant source factor with empty support can be carried separately as
exp(V_vac(zeta)) in BOTH physical integrals. It cancels in their ratio. Its
contribution to each absolute logarithm is still V_vac, not an omitted
normalization. For LINEAR coupling to constant observables, V_vac is linear
in their source parameters and its mixed derivatives of order at least two
vanish. Any additional nonlinear field-independent source normalization
retains its derivatives in each individual physical logarithm.

Give each primitive a NONEMPTY connected base S_o, including any retained
field-free vertex. Empty-support factors must instead be the declared
nonzero common exp(V_vac), or carry a nonempty priced syntactic reader.
For a vertex use a connected
envelope of its full reader and its R0 collar; for a bad cell use its R0
collar; for a compact label use the R0 collar of Gamma_g. These envelopes
are fixed in zeta and contain every activated coordinate and source reader.
They must ensure that disjoint bases have no cross entry of P. Taking
N_R0 of a connected full-reader envelope suffices. Every incompatibility
or body/cap absence condition described below is then internal to base
overlap components. No compatibility is defined using H_g alone.

Set c=p0/2, G=U+p0, a=1/G, b=1/c and

    D0=b*b/a+b/2, L=max(1,sqrt(2 exp(1) D0)),
    K_g=max(1,sqrt(4/(a*c))).                          (F4)

Use the following positive primitive bounds, with suprema on D:

    a_v=K_g^(k |reader_cells(v)|) sup|W_v|,
    a_bad=K_g^k exp(-a p^2/8),
    a_g=K_g^(k |H_g|) sup|Theta_g|.                    (F5)

Here |H_g| counts cells. The full-cell costs include coordinates on which
the original function was constant, because their chart bodies are retained.
Let h_base be the beta-weighted rooted sum of vertex and bad primitives,
and h_comp the same sum of compact primitives:

    h_t=sup_x sum_(o of type t:x in S_o)
                                  exp(beta |S_o|) a_o.             (F6)

All families are finite at fixed volume before their Gaussian integrals and
forest parameters. Uniform estimates refer to (F1)–(F6), not family size.

There exists H>0 depending only on beta,k,L,e,B such that, if

    h_base<=H/2, h_comp<=H/2,                          (F7)

the ratio has an absolutely convergent connected expansion

    log(Z_*/Z_a)=sum_Y Psi_Y(zeta),
    sup_x sum_(Y contains x) exp((beta/2)|Y|)
                         sup_D |Psi_Y| <= C_H h_comp. (F8)

Y is a connected geometric support containing every actual varied source
reader of its coefficient. Each term contains at least one compact label.
The logarithm is the branch continued from the zero-primitive identity.
No full-volume lower bound on the all-chart probability is a premise.
The proof supplies H and C_H below.

## 2. Exact activation and marginal covariance

Fix a compatible compact family F and put M=union_g H_g. Expand the product
in DISTINCT selected W_v. On M the chart indicators are redundant by the
compact caps. Keep the chart body on every selected vertex reader, and
expand every remaining cell body as 1 minus its actual exterior. The bad
cell set B0 therefore satisfies

    B0 disjoint M union (union_(selected v) reader_cells(v)).       (F9)

Selected compact labels keep their original Gamma-disjointness; vertices
and bad cells cannot repeat. All these presences AND absences are retained.
The activated scalar set I consists of ALL coordinates in M, B0 and the
selected vertex reader cells. Every such full-cell cost is included in
(F5); no residual cell-body indicator is lost by marginalization.
The other normalized Gaussian coordinates integrate out to the PRINCIPAL
COVARIANCE C[I]. This is not (C^(-1)[I])^(-1).

Each resulting fixed function Phi is a product of bounded functions, kept
chart bodies, compact caps, and bad-cell exterior indicators, with the
sign (-1)^|B0|. It is independent of the artificial covariance interpolation
below. No derivative of Phi is taken. The empty primitive family has no
activated coordinates and is exactly one. A field-independent compact
label is a genuine nonempty primitive with an empty active scalar set.

Partition primitives by overlap of their S_o. Keep their entire lists,
all incompatibilities and (F9) in each component. The partition is unique.
Different components have disjoint coordinate sets, P[I] is block diagonal
between them, and no admissibility condition couples disjoint components.
The component support S_B is the union of its primitive bases, hence is
connected. Its active scalar set I_B has size at most k|S_B|.

## 3. All-order jets of the normalized density

For each unordered pair of distinct primitive components introduce an
independent parameter s_BB'. Multiply only cross-component entries of E
by that parameter; keep all within-component entries unchanged. For real
|s_BB'|<=1, the absolute perturbation row bound is at most e, so

    c I <= C_I(s)=P[I]+E[I](s) <= G I.                (F10)

For complex |s_BB'|<2 the real part is at least c I and its norm at most G.
The symmetric complex Gaussian with the determinant branch from the real
positive matrices is holomorphic there. Its inverse has real part at least
c/G^2, ensuring integrability against every bounded fixed Phi, including
the unbounded bad-field domains. This also justifies differentiating its
normalizing determinant; the density has never been replaced by an
unnormalized quadratic exponential.

For a real forest mask, put J=C_I(s)^(-1). Then a I<=J<=b I. For real x
and complex z, expansion of the quadratic form and Young's inequality give

    |g_CI(s)(x+z)| <= (2pi c)^(-|I|/2)
                         exp[-a|x|^2/4+D0 sum_i |z_i|^2].         (F11)

Indeed the cross term is at most b|x||z|, bounded by a|x|^2/4+b^2|z|^2/a,
and the remaining z-quadratic term is at most b|z|^2/2. Scalar Cauchy radii
sqrt(nu_i/(2D0)), with zero-order coordinates omitted, imply

    |partial^nu g_CI(s)(x)| <= (2pi c)^(-|I|/2)
       exp[-a|x|^2/4] L^|nu| product_i sqrt(nu_i!).    (F12)

Here nu! / nu^(nu/2) <=sqrt(nu!) coordinatewise; this proves the stated
factorials directly. There is no factorial of the total degree at a whole
component. (F12) is uniform in the forest mask and all finite volumes.

For a bad block |x_X|>=p. Split the Gaussian damping in (F12) in half,
using one half on each distinct bad block. Integrate the other half over
all active coordinates, and bound every W_v and Theta_g by its supremum.
The result is

    |integral Phi partial^nu g_CI(s)|
        <= L^|nu| product_i sqrt(nu_i!) product_o a_o. (F13)

The integral of the remaining scalar Gaussian costs K_g per coordinate.
Assign each active coordinate to an actual primitive; overcounting shared
vertex readers is harmless because K_g>=1. No Gaussian tail is charged on
marked compact fields: their cost is exactly the bulk factor in (F5).
Their physical energy rarity has already been spent in sup|Theta_g|.
No total-volume determinant or normalization factor remains in (F13).

## 4. Forest identity and the exact raw gas

Differentiation of the NORMALIZED density gives the heat identity

    partial_(s_BB') integral Phi g_CI(s)
       =sum_(i in I_B,j in I_B') E_ij
                            integral Phi partial_i partial_j g_CI(s). (F14)

The two symmetric off-diagonal entries cancel the usual factor 1/2. Iterate
in independent pair variables before imposing any forest mask. The fixed
functions, indicators, source labels and primitive admissibility are held
fixed. Compact boundedness and (F10) justify all orders needed at finite I.

For completeness, the finite forest formula can be checked first on a pair
monomial product_e s_e^n_e. For each edge with positive n_e give an independent
clock of distribution t^n_e on [0,1]. Partition the clocks by their maximum
spanning forest, with fixed tie convention (ties have probability zero).
Given its tree clocks, a non-tree clock is no larger than the minimum clock
on its tree path. Integrating it gives exactly the monomial forest mask.
The densities n_e t^(n_e-1) on tree edges give the forest derivatives.
An edge with zero power cannot be selected. Extend linearly and then by
the uniformly convergent power series on the radius-two pair polydisc of
(F10). This proves the forest formula for the present integrals, without
differentiating a path minimum or a hard cutoff.

At a disconnected forest mask every cross-component entry between its
different connected parts is zero. P already has this property. The
normalized Gaussian density, determinant, fixed functions and admissibility
therefore factor over those parts. A raw connected label z consists of
its exact primitive components, a tree on them, scalar endpoints on each
tree edge and the integrated forest parameters. Its base and full support are

    B_z=union_B S_B,
    Y_z=B_z union_(tree edges i,j) Gamma_ij.            (F15)

The tree joins its component supports, so Y_z is connected. A field-free
component has no Gaussian incident edges, but remains a raw singleton.
Its native reader is not erased. The exact representation is a gas of raw
labels whose BASES B_z are pairwise disjoint; full Y_z can still overlap.

No density loop readers need to be introduced here. Every covariance entry
and determinant coefficient is a fixed number independent of the varied
sources; all its active endpoints are already inside the joined component.
The explicit forest edges provide every required spatial connection between
components. This simplification would be invalid for a source-dependent
covariance or a claim about remote coarse-field readers; those are expressly
outside (F1). All varied source readers remain in the primitive bases.

## 5. Positive counts with scalar incoming legs

Set delta=min(beta/8,1/8), beta_j=beta-j delta. Let h=h_base+h_comp.
Choose H sufficiently small that, for all 0<=h<=H,

    h<=delta,
    L^2 e h<=1/2, 4k L^2 e h<=delta,
    r(h):=h+L^2 B h^2<=delta/4.                       (F16)

Such a fixed H>0 exists; zero values of e or B cause no division problem.

First group overlapping primitives. At rate beta_1, a rooted positive
tree series has recursion T_o=v_o exp(sum_(o' overlaps o) T_o'), with
v_o=a_o exp(beta_1 |S_o|). The supersolution
T_o<=a_o exp(beta|S_o|) holds because the neighboring sum is at most
h|S_o|<=delta|S_o|. Iteration from zero proves the inequality. Rooting a
connected family at a primitive covering the marked cell and at one of its
spanning trees overcounts it. Therefore the connected primitive-component
weights w_B=product_(o in B)a_o obey

    sup_x sum_(B:x in S_B) exp(beta_1 |S_B|) w_B<=h.   (F17)

Only the positive estimate relaxes admissibility. The exp recursion counts
unordered children with their 1/j! factors. For globally distinct labels
their permutations cancel those factorials; repeated formal labels add
nonnegative terms without assigning them repeated physical moments.

Now root a Gaussian tree at a primitive component. Allocate its unordered
children scalar by scalar. A component has either no incoming edge, or one
incoming scalar leg at a specified i. The factorial at a scalar with j
outgoing legs is sqrt(j!), or sqrt((j+1)!) at the incoming scalar. Thus the
child sums are bounded by

    H0(y)=sum_(j>=0) y^j/sqrt(j!) <=exp(2y),
    H1(y)=sum_(j>=0) sqrt((j+1)!) y^j/j! <=exp(4y),    (F18)

for 0<=y<=1/2. For example H0<=1/(1-y)<=exp(2y); also
sqrt((j+1)!)/j!<=j+1, so H1<=1/(1-y)^2<=exp(4y).
The child's incoming-scalar rooted weight at any fixed scalar l is bounded
by h using (F17). The scalar attachment argument is therefore

    y_i=L^2 sum_j e_ij T(j)<=L^2 e h.

There are at most k|S_B| scalars. The product of (F18) is at most
exp(4k L^2 e h |S_B|), paid by the next delta in (F16). Iteration of the
nonnegative rooted-tree equations gives BOTH the ordinary root and each
incoming-scalar root the supersolution exp(beta_1|S_B|)w_B at the lower
rate beta_2. This proves the claimed bound T(j)<=h rather than assuming it.

A mark on a full Y_z has two possible witnesses: it is in a primitive base,
or on a tree-edge path. The first has rooted sum at most h. For the second,
cut the distinguished edge at its two scalar endpoints. Each resulting
tree is an incoming-scalar rooted tree with sum at most h. Summing the
weighted paths through x gives B. Counting ordered orientations, rather
than dividing by two, is a safe overcount. Consequently

    sup_x sum_(z:x in Y_z) exp(beta_2 |Y_z|) sup_D|a_z|
                                        <=h+L^2 B h^2=r(h).        (F19)

All Gaussian tree derivatives in (F13), all scalar endpoints and all source
labels have been counted. The normalized density itself creates no additional
source-reader mark in the present frozen setting. A separate scalar-leg
derivation may be used to audit (F17)–(F19), but their proof is included here.

## 6. Regrouping, the connected logarithm, and preserved compact charge

Regroup each base-compatible raw family by connected overlap of its FULL
Y_z, retaining its original base-disjointness inside each group. This is a
unique finite partition. It gives an exact gas with disjoint full readers.
The same overlap-tree recursion, now losing a third delta, bounds its
full-reader rooted activities by r(h); (F16) pays the neighboring sum.

For this hard-core gas, expand the logarithm in connected incompatibility
graphs. The absolute value of the alternating connected graph sum is at
most its spanning-tree sum: use a fixed edge order to assign each connected
graph its Kruskal spanning tree. For a given tree the allowable extra-edge
sets form an interval of subsets; summing (-1) over those extra edges is
zero or has modulus one. This proves the required tree bound directly.
Root the tree at a polymer whose reader contains the marked cell. With
the fourth delta, its neighboring rooted sum is at most r(h)|S|<=delta|S|.
The same supersolution bounds the absolute connected logarithm by r(h) at
rate beta_4>=beta/2. Rooting may count one cluster more than once, which is
permitted for this upper bound.

These absolutely convergent series agree with the finite gas identities
near zero amplitudes, where their formal logarithmic coefficients can be
obtained by direct multiplication. Scale all primitive amplitudes along a
complex unit disc. The uniform bounds just proved extend the exponential
identity analytically across that disc, so the partition functions are
nonzero and the specified log branch is legitimate throughout the admitted
smallness domain. This is not merely a formal connected-series assertion.

At ZERO compact primitives, the whole coefficient list is IDENTICAL to
the chart construction in (F3): same W labels, bad cells, masks, Gaussian,
base-overlap components, paths, raw grouping and hard-core graphs. All
no-compact terms cancel coefficient by coefficient in log Z_*-log Z_a.
Source-only W terms and their normalization responses are among those
terms; their cancellation in this RATIO does not drop log Z_a from a full
physical response.

To bound the terms that remain, if h_comp>0 rescale only the positive
compact primitive amplitudes by T=H/(2h_comp)>=1. Keep every actual field
function, covariance, source parameter, cutoff and domain fixed. The total
positive primitive budget is at most H by (F7). Every remaining term gains
at least one factor T. The entire absolute connected logarithm at this
larger counting budget is at most r(H). Undoing that factor proves

    ||Psi||_(beta/2)<= (2r(H)/H) h_comp.              (F20)

If h_comp=0, the remaining family is empty. This is a rescaling of counting
bounds, not a modified physical measure or an assertion of positivity of
complex chart expectations. Equations (F8) and (F20) follow with
C_H=2r(H)/H. No unrelated bulk logarithmic bound has been subtracted.

## 7. Consequence for a fixed finite source coefficient

Suppose a label i can occur only in primitives whose base includes its
complete actual support S_i. Then a mixed coefficient of Psi_Y is zero
unless Y contains every differentiated S_i. On a source polydisc of radius
r for q distinct normalized labels, Cauchy's formula gives

    sum_(Y contains all S_i) |partial_1 ... partial_q Psi_Y(0)|
       <= r^(-q) C_H h_comp exp[-(beta/2) tau],         (F21)

where tau is the minimum number of nearest-neighbor edges of a tree meeting
those supports; the stronger definition requiring their entire union is
also allowed when that is the support convention. Every admitted Y is
connected and contains those supports, so tau<=|Y|-1. To use the rooted
norm, fix one cell of a nonempty differentiated support. Empty-support
constants have already been kept in V_vac and give zero mixed coefficients.

When source radii are given as an open polydisc, apply Cauchy at any smaller
fixed radius and use that radius in (F21). There is no assertion of a
uniform field-analytic neighborhood of the compact functions. Actual source
norms multiply (F21) when undoing the normalized labels.

This concludes the abstract author proof. Its physical use still requires
checking (F1)–(F7), the exact same-chart identity, the actual source-reader
assignment, and any separate chart cumulant estimate. A coarse conditional
denominator of a different law, repeated-link score derivatives, further
blocking depth and continuum reconstruction are not consequences of this
lemma. No numerical computation or formal retained-status operation is used.
