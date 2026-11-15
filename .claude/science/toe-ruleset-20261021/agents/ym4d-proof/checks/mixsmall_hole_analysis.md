# MIXSMALL author assistance: fixed-mask mixed jets and hole costs

**Author analysis, not independent review.** The fixed-mask real-jet transfer is
PROVEN below as a mathematical implication. The actual mixed-group estimate
uniform in history, volume and holes remains OPEN. No numerical experiment,
commit, audit verdict, ledger change or retained-status claim is made.

The checked working HEAD is `0f561ef0b2dba3b024190fc55717c5b0ca7db881`.
Sources were read at this local snapshot; remote freshness was not asserted.
RD3, RD4 and LIB1 were read completely. Relevant REALRGA definitions, real
calculus, H-contract and carry-over rows were read. Additional RD definitions
were read only to verify the explicit history construction below. This file
is the sole worker deliverable. The supervising author owns synthesis and
any later independent review.

| Source | SHA-256 at the read snapshot |
|---|---|
| `RD.md` (specified definition excerpts) | `a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5` |
| `RD3.md` | `55274cfe3d6c90b6eb6e2f5412bdb5633660f6e47054e1db52f8a1ca9ac3d3cc` |
| `RD4.md` | `60d27c7ec5e5fda254e8394c34639cccdfe42cd9f85898bb22952bc6fa6067c6` |
| `LIB1.md` | `1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1` |
| `REALRGA.md` | `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed` |
| `PROCESS_LIGHT.md` | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| `briefs_q/MIXSMALL/AUTHOR.md` | `40f9355313dd29a65df1c84f34555f31ddfa7c48a68eb1acbf0906769435117b` |

The small/large-field and boundary-resummation methods are credited to Tadeusz
Balaban and Jonathan Dimock. Their expositions supply historical attribution
here, not an imported gauge-theory theorem. Every load-bearing argument in
this assistance note is reconstructed below; no memory-only lemma is used.

## 1. The exact real mixed-jet transfer

Use REALRGA RGA3/RGA4 and RGA7 (`REALRGA.md:75–126,156–172`). Write
`j(K_X)=sup_(D^R) T(K_X)` for either its ordinary or labelled finite jet
seminorm, with precisely the same domain, original source directions and
frozen weights on input and output. It includes every still-retained fine
field, coarse field and source order required by the contract. Define

    ||K||_(mu,T) = sup_(v in Gamma) sum_(X contains v) e^(mu |X|) j(K_X).

Supports are nonempty connected subsets of the face graph of maximum degree
8. Let fixed masks satisfy Lambda subset Omega subset Gamma and use LIB1's
P_Omega (`LIB1.md:68–84`). Let H run over components of Gamma minus Lambda,
and set

    R_Lambda(X) = X union {H : dist(H,X)<=1},
    K'_Y = sum_(X meets Lambda, R_Lambda(X)=Y) K_X.

Keep every `X` not meeting Lambda as an **individually supported labelled
inactive activity**. The notation `K_inactive` denotes their sum inside the
actual integrand, not one supportless scalar. Let `K_out` be the union of
the labelled inactive family and the family K'. Coincident output supports
may subsequently be combined by triangle inequality.

**Lemma 1 — PROVEN, fixed-mask real-jet version of LIB1 L3–L15.** If every
inactive component has at most M>=1 vertices, then, for mu>=0,

    ||K'||_(mu,T) <= 9 M ||K||_((1+8M)mu,T),
    ||K_out||_(mu,T) <= (1+9M) ||K||_((1+8M)mu,T).       (MH1)

The exact sum and original-data locality are preserved. An active-root,
active-size norm instead contracts, but is a different consumer norm.

Proof. Every added H is connected to X by intersection or an edge, so R(X)
is connected. Distinct inactive components have no connecting edge. Thus
R(X) is saturated, contains X, and R(X) intersect Lambda = X intersect
Lambda. The fibres of the fixed finite set map X -> R(X) partition the
input supports meeting Lambda. This proves the sum identity and locality;
every original argument of K_X lies in X subset R(X). All ordered derivative
words commute with this **fixed finite linear regrouping**. The triangle
inequality for every component of T consequently gives

    j(K'_Y) <= sum_(X:R(X)=Y) j(K_X).

If a component H meeting X is added, a path in connected X from X intersect
H to X intersect Lambda exits H along an edge incident to X. A disjoint H
added by adjacency also has such an edge. Distinct H use distinct edges,
so at most 8|X| components are added. Therefore

    |R(X)| <= (1+8M)|X|.

For an active output root v, v in R(X) implies v in X, giving constant 1
at the stronger input rate. For inactive v in H_v, a contributing X meets
the closed neighborhood N[H_v], whose size is at most 9M. Sum the input
rooted bounds over those at most 9M vertices. This proves the first bound.
The inactive family retains its old supports and has norm at most the
input norm at rate mu, hence also at the stronger rate. Add it to prove
the second bound. The argument uses only finite sums, nonnegative weights,
and triangle inequalities, so no holomorphic continuation or Cauchy estimate
is involved. If Lambda is empty there is no active output; if Lambda=Gamma
the map is the identity. These endpoint cases are also covered. QED.

The analogous active norm contracts because retained active roots are
unchanged and output active size is no larger than input active size. This
gives no inequality for full output
sizes or inactive roots without a conversion such as MH1.

Source differences commute with the same map. If estimated only from
absolute jet bounds, `j(K_X(J)-K_X(0))<=2 j(K_X)` on the same domain, where
evaluation at zero source retains the same original support labels. There
is no derivative-order increase, no derivative acquisition, no source-weight
change and no regulator removal in this lemma. Any regulated input must
first be converted to the unregulated integrated norm, or use a separately
proved compatible regulator comparison. A data-dependent mask is outside
the lemma: differentiating through a jump of the map is an additional
operation.

## 2. Constants 730, 649 mu and the same-rate alternative

RD3 D1 has the single hole H={-1,0,1}^4 in a torus of side T>=7
(`RD3.md:25–44`). Its size is 81. Substituting M=81 in MH1 gives

    ||K'||_(mu,T) <= 729 ||K||_(649mu,T),
    ||K_out||_(mu,T) <= 730 ||K||_(649mu,T).             (MH2)

This reconstructs RD3 D22 (`RD3.md:425–444`) and RD4 K2
(`RD4.md:541–554`) with every requested real mixed derivative present.

For this one hole, saturation adds at most 81 vertices, independently of
|X|. Its closed face-neighborhood has exactly

    |N[H]| = 3^4 + 8*3^3 = 297.

The 216 exterior vertices have one coordinate equal to +2 or -2 and the
other three in {-1,0,1}; the T>=7 hypothesis prevents identifications.
Using `e^(mu|R(X)|)<=e^(81mu)e^(mu|X|)` in the same rooted proof gives

    ||K'||_(mu,T) <= 297 e^(81mu) ||K||_(mu,T),
    ||K_out||_(mu,T) <= (1+297 e^(81mu)) ||K||_(mu,T).    (MH3)

**The input rate in MH3 is mu, not 649mu.** This is what RD3 D23 explicitly
proves (`RD3.md:446–470`); RD4 K2 also states the same-rate formula.
REALRGA's carry-over row (`REALRGA.md:495`) should spell out the two norms
to remove the ambiguity of “at the same rate.” Both estimates are valid;
one uses a stronger input rate, the other a geometry-dependent prefactor.
The same-rate estimate does not assert a history-independent prefactor.

### An optional sharpening, proved here

For a hole H define its **exterior face boundary**

    boundary_out(H) = {x notin H : x has an edge to H}.

Every such x is active: an edge to another inactive component would merge
the components. If R(X) contains H and X meets Lambda, then X meets this
exterior boundary. For an adjacency-only addition this is immediate. If
X meets H, follow a path in connected X to an active vertex and take its
first exit from H. This argument replaces N[H] by boundary_out(H) in the
inactive-root estimate.

Hence the general active output constant 9M can be replaced by 8M, with
the same stronger input rate (1+8M)mu, and the full labelled constant by
1+8M. More precisely use `max(1,max_H |boundary_out(H)|)` for the active
family. For the specified cube the same-rate bounds improve to

    ||K'||_(mu,T) <= 216 e^(81mu) ||K||_(mu,T),
    ||K_out||_(mu,T) <= (1+216 e^(81mu)) ||K||_(mu,T).    (MH4)

MH4 is a new author proof, not an independently reviewed replacement of the
source constants. It is useful only after the actual input jets have been
proved, and does not remove the arbitrary-hole issue.

## 3. Unbounded holes: actual masks and abstract coefficient witnesses

### 3.1 Actual positive-mass RD histories have unbounded holes

This construction uses exactly RD R2/R3 (`RD.md:264–302`) and the marked-link
witness of RD3 (`RD3.md:46–89`). It keeps the illustrative cut=1 and n_0=1;
it does not silently impose those values on another consumer.

For any integer m>=1 choose a compatible level-one block torus of side
T>=m+6. Let C_m={0,...,m-1}^4 on that graph, and let Y_m consist of **all**
level-zero blocks projecting to C_m. In old block coordinates Y_m is a
box of side Lm. In every old block of Y_m put

    g=diag(-1,-1,1,...,1)

on the oriented e_1 link based at within-block coordinates (1,1,1,1), and
put identity on every other old link. All plaquettes reading a marked link
are wholly inside its own block; none reads two marked links. They are g
or g inverse, at distance 2 from identity. All other plaquettes are
identity. Thus the bad-block set is exactly Y_m. It is G_2-connected and
has (Lm)^4>1 blocks, so it is one size-failed component whatever the next
coarse field and completion threshold are. There are no other failures.

Vary every old link within an open operator-norm delta=1/16 ball. A
plaquette product changes by at most 4delta=1/4. Previously good interior
plaquettes remain below cut 1; each previously bad block retains a
plaquette at distance at least 7/4. The same failed list holds on this
open product set for **every** real U_1. Every open group ball has positive
Haar mass, and all finite real action/kernel factors are strictly
positive. Consequently h_m=(F_0={Y_m}) has positive inherited density on
every real U_1 fibre. The exact hole recursion gives

    H_1 = N_1(pi_0(Y_m)) = {-1,...,m}^4,
    |H_1| = (m+2)^4.                                  (MH5)

The active set is nonempty and no periodic identification affects this
box. Therefore **no uniform maximum hole size follows for unrestricted
positive-mass RD histories even at one step**. This is an actual-model
statement about the masks, not about the size of their effective activity.
Its positive cap may have an extremely small, volume-dependent mass.

The same argument works for any fixed cut strictly between 0 and 2 after
shrinking delta to preserve the two margins, and for any finite n_0 after
choosing m with (Lm)^4>n_0. No claim is needed at the endpoint cut=2.

### 3.2 Exact saturation witnesses, on those actual masks

Let H be the cube of side s=m+2 from MH5, let Lambda=Gamma minus H,
Omega=Gamma, and let a be one exterior face neighbor. Give the single
support {a} a constant coefficient b>0; every other coefficient is zero.
Its full real finite-jet seminorm is b at every order. Saturation gives
R({a})=H union {a}. At any fixed input rate nu>=0 and output rate mu>=0,

    ||K||_(nu,T) = b e^nu,
    ||K'||_(mu,T) = b e^(mu(|H|+1)).                    (MH6)

For fixed mu>0 and any finite fixed nu the ratio diverges with m. Thus
there is no constant uniform in holes for this operator on **all** local
coefficient families, even after a fixed finite input-rate increase.

At mu=0 the singleton witness alone has ratio one. To test inactive roots
at that endpoint, put a distinct coefficient b on **each** singleton
{a}, a in boundary_out(H). There are exactly 8s^3 such vertices. Every
input root sees one coefficient, while every root inside H sees all 8s^3
different saturated output supports. Exactly,

    ||K||_(nu,T) = b e^nu,
    ||K'||_(mu,T) = 8s^3 b e^(mu(|H|+1)).               (MH7)

In particular at mu=nu=0 the ratio is 8s^3, unbounded. This exposes both
full-size growth and accumulation at inactive roots. All coefficients are
nonnegative, so cancellation cannot change these equalities.

The masks in MH6/MH7 are attained by actual positive RD histories. The
chosen coefficient families **are abstract test inputs**, not asserted to
equal actual fully integrated Yang–Mills coefficients. These witnesses
refute a geometry-only operator estimate over arbitrary coefficients.
Additional suppression tied to the actual unnormalized histories, or a
different consumer representation, remains possible.

## 4. Mixed-reader statements that do and do not carry

### 4.1 A real mixed-jet version of the fixed-product estimate

**PROVEN implication.** Let mu be a fixed product probability in the
integration variables, independent of the external parameters y. Let
d_C be the signed joint hard-event types of RD3 D14, fixed in y. Types in
a compatible family have disjoint full integration-coordinate supports.
Let every interaction f_i have the required mixed y jets with a common
dominating envelope, and put

    a_i = sup_(y,x) T_y(f_i),
    p_C = mu(intersection_(ell in C) E_ell).

For any compatible family F of defect types and any interaction set I,

    sup_y T_y( int product_(i in I) f_i product_(C in F) d_C dmu )
                         <= product_(i in I) a_i product_(C in F) p_C. (MR1)

Proof. Differentiate under the fixed integral. The ordered Leibniz rule,
with the factorial weights or labelled-source subsets of RGA3/RGA4,
gives `T(product f_i)<=product T(f_i)`. The hard types contribute no y
derivatives. Take the interaction suprema and use absolute values. Each
remaining factor is the indicator of its joint event, not a product of
marginal probabilities. Disjoint type-coordinate supports factor under
the product reference. This proves MR1, including the empty families.

Exactly the same proof works for **fixed positive conditional cell laws**
as in RD4 C4 when complete readers have first been closed under the cells.
Their probability normalizations contribute no derivative because they
are fixed in y. Their conditional correlation inside a cell is retained.
If cells or densities depend on y, a fixed-domain differentiable-density
representation and dominated derivatives must first be supplied. Under
those hypotheses MR1 is replaced by

    T_y int F_y n_y d lambda <= int T_y(F_y) T_y(n_y) d lambda,       (MR2)

with every normalizer and selector-boundary contribution included. This
is REALRGA RGA13 (`REALRGA.md:273–312`). Positivity makes the value-level
TV equal to one; it does not set `int T(n_y)` to one. A moving hard sector
does not acquire the required density regularity automatically.

For the actual RD3/RD4 fixed-Haar representation, MR1 is legitimate for
outer original-source/terminal-coarse jets after all previous fields have
actually been placed in the integral and current outcomes have been
summed. It is not a proof of small a_i or p_C, and the product Haar law is
not the actual interacting all-cut normalized law. If a history selector
reads a still-retained field being differentiated, it is not fixed in y,
and MR1 does not apply to that derivative. A price under a different law
cannot be substituted for p_C without an actual comparison.

To get the real Mayer theorem from MR1 one still needs exact overlap
factorization, complete supports, and the **summed** budget

    sup_v sum_(i:v in H_i) e^((mu+2)|H_i|) alpha_i <= 1/4.

A fixed per-group estimate `epsilon^(number of labels)` alone does not pay
support enlargement or the number of possible labels. If the group-size
convention instead counts full support blocks, it must explicitly include
all reader/cell/hole enlargements. REALRGA RGA16 is the precise interface.

### 4.2 Actual finite relative outer jets: no inverse-history-mass loss

There is a useful genuine soft-kernel estimate that requires neither a
product law nor a lower bound uniform in history mass. It is weaker than
the local mixed-group estimate.

Fix a past history h of positive mass. In the unselected transfer R_h of
RGA2 all previous fields are integrated and all current outcomes summed.
The old selector Xi_h is independent of the new terminal V and original
coefficient sources epsilon. Write the positive opened integrand as

    W(V,epsilon;x) = Xi_h(x) exp[-u_0 sum_p(1+epsilon_p)s_p(x)]
                                  product_(ell<=j) K_ell,
    R_h(V,epsilon) = int W(V,epsilon;x) dx.

All fields in x and Haar domains are real and compact. The positive
support of Xi_h is fixed in these external parameters. Let b terminal
coarse derivations have arrays B_i with `max_c ||B_(i,c)||op<=h_c`, and let
C be the number of terminal links in the union of their nonzero supports.
For b=0 set C=0. Let c coefficient-source directions v_l satisfy

    2 u_0 sum_p |v_(l,p)| <= A  for each l.

Here h_c is the actual frozen coarse jet weight h_(j+1); A is in original
source units. Define the Bell polynomial

    B_b(z) = sum_(pi partition {1,...,b}) z^(number of blocks of pi),
    B_0(z)=1.

Then, for all real source values and terminal group fields,

    |D_c^b D_epsilon^c R_h| / R_h
                       <= h_c^b B_b(t_j C) A^c.         (MR3)

The notation D_c^b in MR3 means b ordered coarse derivations, whereas the
superscript c on D_epsilon counts source derivatives. No direction-order
commutation inside the coarse species is assumed.

Proof. On the positive support, terminal field dependence of log W is
`t_j sum_d Re tr(V_d^* M_d(x))/N`; each kernel normalizer depends on x,
not on the new V. An ordered word of r>=1 terminal derivatives on one
trace inserts r fixed matrices, so its modulus is at most h_c^r since
||M_d||op<=1. Summing the at most C affected links gives a log-weight
derivative bound `t_j C h_c^r`. Repeated differentiation of an exponential
partitions derivative positions into blocks, preserving the inherited
order in each block. Induction gives this partition formula: a new
derivative either starts a block by differentiating the exponential or
joins one block by differentiating its log-weight derivative. Consequently

    |D_c^b W| <= W h_c^b B_b(t_j C).

The source tilt is linear and every kernel is held fixed. Each source
derivative multiplies W by `-u_0 sum_p v_p s_p(x)`, of modulus at most A
because 0<=s_p<=2. This score is independent of terminal V. The mixed
bound for W follows by multiplication. On compact real parameter sets
the smooth finite factors and their derivatives have an integrable
envelope. Integrating the pointwise bound, then dividing by R_h>0,
proves MR3. No lower bound for the history mass was used. QED.

For the actual all-cut denominator Z_(j,A), the same proof applies and
there is no original-source derivative when that reference is defined
source-free as in RGA2. Its cuts are internal and independent of terminal
V. RGA11 then gives finite outer log-jet bounds; the quotient recursion
RGA12 gives finite normalized-density and R_h/Z_(j,A) relative bounds.
These statements include the differentiated reference, rather than
pretending its nonzero-order jets vanish.

For clarity, a direct recurrence for a fixed normalized density is enough
to see the last assertion. For a word I let b_I majorize
`|D_I W|/W`, with b_empty=1; positivity gives
`|D_I R_h|/R_h<=b_I`. Write n=W/R_h and use `n R_h=W`.
Setting d_empty=1, the recursive bound

    d_I = b_I + sum_(B proper subset I) d_B b_(I minus B)

gives `|D_I n|<=n d_I`, with orders inherited in each subset. Every term
on the right uses a shorter d_B. Thus `int T(n)` is bounded by the finite
weighted sum of these d_I. A kernel composition with a reader is bounded
by this density-jet cost and the reader's mixed jets through MR2. It need
not be a contraction, and it does not delete the reader.

**Exact scope of MR3.** For a fixed finite number of specified local
directions its constants are independent of volume, h's probability and
hole size, at fixed t_j and h_c. This is actual-model boundedness. In the
RGA3 supremum over arbitrary unit arrays, C can be the number of all
terminal links and A can be `2u_0 sum_p r_p`; those can be extensive.
Even a bounded derivative in each chosen local direction supplies no decay
with the separation of distinct directions, no complete-reader support
expansion and no smallness of connected mixed groups. Large-u scaling
also remains explicit in t_j and h_c. Fine derivatives of fields already
integrated out are absent legitimately; fine derivatives of a retained
hard history are not established by this theorem.

### 4.3 Reader elimination is exact, not reader suppression

For a normalized positive soft kernel,

    int k(V;M) dV=1,
    |int k(V;M) F(V) dV| <= sup_V |F(V)|.

The first identity can be used only if no other factor reads V. With a
reader F the output is the second integral. Its derivatives include those
of the kernel's normalized density, as MR2 shows. Repeating the integration
over a reader-free terminal cone proves RD4's raw-cone identity
(`RD4.md:483–490`); a fixed terminal field or boundary insertion prevents
that deletion. This algebra is available for the actual step. Small local
mixed-reader prices after the remaining interacting integration are OPEN.

## 5. Explicit failure classes and their exact classification

### 5.1 Mandatory mass cannot pay a normalized insertion again

For any actual selected event E of probability p>0 under its stated real
reference, `int |1_E/p|dmu=1`. If such an insertion is treated as a small
defect of nonempty support S, the zero-order contribution to the mixed
jet budget is at least `e^((mu+2)|S|)`. All positive jet terms only increase
the budget. This proves the RD3 D16 failure unchanged in the real contract
(`RD3.md:278–304`). The unnormalized history mass remains available once;
extracting it into a conditional reference is an admissible different
representation. There is no physical obstruction inferred here.

### 5.2 Direct conditional Haar fails, also in an integrated block version

RD4 C10 already proves an actual zero-order failure when a remote Wilson
plaquette is separately expanded against the conditional Haar reference:

    q_C >= e^beta (1-e^(-4u_0/N)),  beta=mu+2,

which exceeds 1/4 at the displayed source threshold
`u_0>-(N/4)log(1-e^(-beta)/4)` (`RD4.md:280–299`). Since a mixed-jet norm
contains its value term, adding real derivatives cannot repair that exact
supremum-based sufficient criterion. It does not refute a direct estimate
of differently grouped, fully integrated atoms.

Here is a related **actual integrated failure** for another explicit
conditional-Haar construction. Use the histories h_m in MH5. Extract only
the mandatory b_(0,Y_m) event as in RD4 C1–C4; retain every avoidance factor
and smooth action/kernel factor in the residual expansion. Its Haar mass
is positive by the same cap. Since |Y_m|>n_0, the mandatory event is just
badness of its blocks and goodness of its G_2 shell, independent of U_1.
Its old-block readers project inside H_1: the radius-two old-block shell
projects at most one coarse block outward because L>=3. Use the entire
connected H_1 as its conditional cell, as allowed by RD4 C4.

Choose an old block Q in Y_m, and combine its interior Wilson plaquettes
into one exact interaction. At zero sources it is

    S_Q = sum_(p wholly interior to Q) s(U_p),
    f_Q = exp(-u_0 S_Q)-1.

At general original sources use
`f_Q(epsilon)=exp[-u_0 sum_(p interior Q)(1+epsilon_p)s_p]-1`.
This grouping preserves the original action; all other plaquette and kernel
factors remain as separate residual factors. Evaluated at zero sources,
the selected-set coefficient
with only this atom present is exactly `A_{ {Q} }=int f_Q dnu_E`, where
nu_E is the positive conditional Haar law and unused normalized cells
have been integrated to one.

On E the block Q is bad. For every unitary U,

    s(U) = ||I-U||_HS^2/(2N) >= ||I-U||op^2/(2N).

At least one interior plaquette in Q has norm distance at least the cut
epsilon_cut>0, so `S_Q>=epsilon_cut^2/(2N)` on all of E. Therefore

    A_{ {Q} } <= -delta_u,
    delta_u = 1-exp[-u_0 epsilon_cut^2/(2N)] >0.         (MF1)

There is no sign cancellation: f_Q is nonpositive throughout E. Closing
this interaction's readers under the conditional cell assigns support
containing H_1. Every product majorant of the RGA16 type must therefore
take `alpha_Q>=delta_u`, since its singleton bound already includes MF1.
Consequently

    Q_Mayer >= e^((mu+2)|H_1|) delta_u.                  (MF2)

For every fixed u_0>0 and epsilon_cut in (0,2), MF2 exceeds 1/4 for sufficiently
large m. This disproves a history-uniform real Mayer bound for the specified
conditional-Haar, cell-closed, unabsorbed-Wilson-block representation at
the level of an **integrated coefficient**, not just a loose upper bound.
It also shows that a cell-sized smallness requirement cannot be supplied
by the mandatory mass after that mass has been extracted.

MF1/MF2 do not prove that the actual optimized mixed groups of a matched
Gaussian/interacting reference are large. Absorbing the block action in
the reference, retaining its unnormalized weight, or changing reader
organization changes the displayed coefficient. No failure of those
alternatives has been proved here. The exhibited atom is a conditioned
large-cell atom; it is not advertised as a counterexample to every group
containing both small-field and large-field insertions.

### 5.3 Positivity and TV=1 do not imply local jet decay: abstract witness

RD4 C11's sign example is useful entirely on the real domain
(`RD4.md:301–315`). On an m-vertex path, start with independent fair signs,
condition on all signs being equal, and extract the event mass 2^(1-m).
The remaining probability law is supported equally on all-plus/all-minus.
For real sources,

    Z(z)=cosh(sum_i z_i)>0,
    partial_i partial_j log Z(0)=1  for every i != j.

These equations follow by the two-term sum and direct differentiation.
Consider any decomposition `log Z=sum_X F_X` with connected full original
source supports. For two labels i,j distance d apart, only supports
containing both can contribute to their mixed derivative. Each such support
has at least d+1 vertices. In the labelled two-source jet norm with weights
one,

    ||F||_(mu,T^[2])
      >= e^(mu(d+1)) sum_(X contains i,j) |partial_i partial_j F_X(0)|
      >= e^(mu(d+1)).                                  (MF3)

The first inequality roots at i and drops nonnegative terms; the second
uses the derivative identity and triangle inequality. Thus positivity,
smooth real sources, extracted mass and TV=1 are insufficient premises
for a uniform local connected-jet norm. This is an **abstract finite-sign
law**, not a Wilson/Decision-4 measure. Its relevance is only the rejected
general inference from positivity/conditioning to local decay.

### 5.4 Moving cuts and value-only derivative acquisition

The actual block cut is discontinuous in a retained field crossing its
threshold. For SU(2), put `diag(e^(i theta),e^(-i theta))` on the same
interior link used above. Its plaquette distance is `2|sin(theta/2)|`;
at cut 1, theta=pi/3 crosses the good/bad boundary. Putting the same link
in two adjacent blocks with n_0=1 makes their prescribed failure indicator
and next mask jump. Thus a domain crossing that threshold cannot treat
the retained selector as a C^6 small atom or the mask as a differentiable
fixed reindexing. Integrating the relevant variables, summing selectors,
or an exact domain decomposition may restore a usable operator; that is
additional work, not a consequence of MH1.

Independently, on a fixed real source interval a local function
`b sin(n J/r)` has bounded values b while its r-weighted first derivative
at zero is bn. A field-chart factor `sin(theta/h)` makes the mixed
source/field derivative grow in the same way with bounded values. Hence
no bound for the required real mixed jets follows from value bounds alone.
These are analytic test functions, not alleged actual RG coefficients.
LIB1 L16 is therefore obsolete as a real-contract proof mechanism; actual
real jets must be supplied before applying its fixed-mask linear map.

## 6. Proposed carry-over rows for the consumed results

These rows update the **scope description in this assistance file only**.
No source carry-over map was edited and no review disposition is assigned.

| Consumed source and exact location | Real-contract disposition | What is proved here / what remains |
|---|---|---|
| RD R2/R3, `RD.md:264–302`; RD3 cap witness, `RD3.md:46–96` | **CARRIES**, with an additional actual history family PROVEN in MH5 | The prescribed real history masks occur at positive mass and may have unbounded components. This refutes deriving a uniform M from unrestricted RD histories, but does not determine actual activity sizes. |
| RD3 sections 1–2,5,7–8, especially D4–D10, RC1–RC3 and D24–D26 | **CARRIES** at the finite real scope | Exact inherited density, exterior inverse, all-cut comparison, complete integration and prefactor bookkeeping remain. MR3 adds finite outer relative jets on fixed positive sectors. The extensive cap comparisons do not give local full-norm smallness. |
| RD3 D14–D15, `RD3.md:225–274` | Fixed-reference real mixed-jet implication **PROVEN** as MR1; actual smallness **OPEN** | Full joint events, common product/cell law and full reader supports are required. Differentiated references use MR2. Scalar prices under another law do not supply the mixed majorant. |
| RD3 D16, `RD3.md:278–304` | **CARRIES** unchanged | A normalized mandatory indicator has L1 norm one. Every mixed seminorm contains that zero-order cost; the extracted mass cannot be spent again. |
| RD3 D21, `RD3.md:414–423` | **CARRIES** for original-source derivatives on fixed positive fibres | `partial_p partial_q log D_h=u_0^2 Cov_(nu_h)(s_p,s_q)` follows by differentiating the actual integral. Boundedness of individual cumulants does not prove spatial decay or the full norm. |
| RD3 D22–D23, `RD3.md:425–473`; RD4 K2, `RD4.md:541–554` | **CARRIES** for supplied real mixed jets and fixed masks | State explicitly `norm(K_out)_(mu,T)<=730 norm(K)_(649mu,T)` **or** `<= (1+297 exp(81mu)) norm(K)_(mu,T)` for the specified hole. The alternative has no rate loss. MH4 optionally improves 297 to 216 by an exterior-boundary proof. Actual input jets remain OPEN. |
| RD4 C1–C4, `RD4.md:79–194` | **CARRIES** for exact extraction and fixed positive conditional cells | Extract the mandatory mass once, retain avoidance factors, merge shared readers and keep the full cell. TV=1 is a value-level probability fact. A parameter-dependent cell reference needs its own derivatives. |
| RD4 C6–C9 and C10, `RD4.md:196–299` | Jet theorem **PROVEN conditionally** via MR1/RGA16; direct conditional-Haar instances **FAIL**; adapted actual estimates **OPEN** | C10's exact supremum failure survives every jet norm. MF1/MF2 add an integrated block-atom failure on arbitrarily large actual mandatory cells. An adapted reference changes these atoms and is not ruled out. |
| RD4 C11, `RD4.md:301–315` | **CARRIES** as an abstract real non-implication witness | Its real log has nondecaying pair derivatives, giving MF3. Its sign law is not an actual SU(N) history measure. Complex zeros are unnecessary for this real conclusion. |
| RD4 L1–L4 and raw-cone rule, `RD4.md:338–397,483–490` | Exact real integration and scalar matched comparison **CARRY**; local mixed bounds **OPEN** | Positive matched reference has value-level TV=1; readers still stay inside the integral and all density derivatives are paid. Kernel normalization deletes only unread outputs. |
| RD4 L6–L8, `RD4.md:399–460`; REALRGA RGA18, `REALRGA.md:513–521` | Real price arithmetic **CARRIES conditionally**; evaluated actual jet tuple **OPEN** | Remove complex-only polar/TV terms, but retain reference, boundary, support, entropy and all real jet/regulator debits. Exact overlap gluing is a separate required identity. A value-level scalar history price is insufficient. |
| RD4 K1–K3, `RD4.md:521–574` | **CARRIES** once both fully integrated real local log-jet decompositions are supplied | A normalized matched ratio subtracts both complete logarithms; the same triangle/fixed-mask bounds then apply. No such actual uniform K input is supplied by RD3/RD4 or by this note. |
| RD4 I1–I4, `RD4.md:576–637`; REALRGA H5/RGA17, `REALRGA.md:433–467` | Conditional invariance/accounting **CARRIES**; actual transition **OPEN** | New effective atoms, relevant extraction, normalized numerator bounds and every hole/reader loss must fit the next identical norm. Repeated multiplication by hole constants is not a contraction argument. |
| LIB1 parts A,C / L3–L15, `LIB1.md:216–273,357–423` | **CARRIES** as fixed-mask real finite-jet inequalities | MH1 reconstructs the full-root/full-size bound and inactive remainder. MH6/MH7 disprove a uniform arbitrary-hole operator bound for unrestricted inputs, including root accumulation at mu=0. |
| LIB1 part B / L6–L11, `LIB1.md:275–355` | **CARRIES** as a Banach-seminorm triangle/counting implication, not used as an actual smallness input here | Its hypothesis is decay in the stated ambient active-tree length. That length and an active norm do not replace the full output norm or supply effective activities. |
| LIB1 L16, `LIB1.md:425–438` | **OBSOLETE** as a real proof mechanism; required derivative input **OPEN** | Real jets are supplied directly before regrouping. Value-only bounds, positivity and fixed-mask linearity do not acquire derivatives. |

## 7. H-clause status reached by this bounded subtask

| Clause | Status reached here |
|---|---|
| H0 | **PROVEN finite algebra / OPEN full local state.** Exact selectors, masses, references and every reader survive the operations. Positive-mass large-hole histories have been exhibited. |
| H1 | **PROVEN finite outer smoothness on the unselected positive step / OPEN invariant mixed regularity.** MR3 controls all fixed finite outer coarse/source orders at their stated constants. Retained hard cuts and changing masks require separate sector work. |
| H2 | **PROVEN conditional integration calculus / OPEN actual uniform mixed-group input.** MR1/MR2 are sufficient interfaces, not evaluated regulators or local charges for the actual interacting reference. |
| H3 | **OPEN for the actual matched construction.** The explicitly specified conditional-Haar schemes fail in C10 or MF2. No actual adapted-reference RGA16 tuple or localized prefactor-log budget is proved. |
| H4 | **OPEN actual extracted output.** Fixed-mask jets transfer whenever supplied; this does not construct the output K or Loc. |
| H5 | **PROVEN conditional hole transfer / OPEN history-uniform transition.** MH2/MH3 reconstruct the requested costs; MH4 sharpens one count. MH5–MH7 show why one cannot insert a universal hole constant on the unrestricted coefficient class. An actual price-compensated construction or another matching norm remains available. |

The minimal next decision is to choose one **actual matched representation**
for an integrated mixed group, including its differentiated reference and
full original readers, and prove its RGA14/RGA16 bound. If that representation
uses whole-hole saturation, its input must contain suppression paying the
explicit support/root growth, or restrict to a stable admissible class with
its complement retained and priced. If it keeps original reader labels,
the consumer theorem must be proved in the same norm. Positivity and a
normalized conditional probability alone do not decide this choice.

## 8. Negative-claim scope check and recovery checkpoint

The repository no-go-discipline instructions were consulted only to bound
the negative statements inside this author assistance. The assignment
forbids commits and audit/ledger writes; no landing packet, route-exhaustion
claim or packet PASS is asserted. This file records partial constructive
results and precisely quantified failures of specified representations.

- **N1, routes.** Fixed-mask transfer was reconstructed and sharpened;
  direct conditional Haar was tested at a supremum and an integrated block
  coefficient. Adapted interacting/Gaussian references, unnormalized
  price-weighted regional groups, and original-reader consumer norms remain
  unclosed alternatives, not exhausted families. No five-route submission
  claim is made.
- **N2, dependence.** No number of independent walls is asserted. Actual
  integrated jet bounds, regularity of a chosen sector representation and
  a compatible hole norm may be supplied by one construction. Pairwise
  implications between those unresolved tasks are not established here.
  Within the proved transfer, bounded-hole geometry plus supplied stronger-
  rate jets implies a full output bound; it does not imply the actual input
  jets. A complete direct integrated bound could avoid the bounded-hole
  premise entirely.
- **N3, premises.** Fixed masks, connected full supports, common real jet
  domain/weights, positive fixed sectors, exact conditional reference,
  explicit source/kernel conventions, and the indicated illustrative cuts
  are all named. No small effective action or uniform history probability
  has been assumed. MH6/MH7's arbitrary coefficients and MF3's sign law are
  explicitly distinguished from actual effective coefficients.
- **N4, residual matching.** LIB1 L23 addresses saturation of arbitrary
  coefficients; MH6/MH7 address that same operator and add inactive-root
  accumulation. RD4 C10 addresses a direct-Haar supremum atom budget; MF1/MF2
  address a specified block-grouped conditional-Haar integrated coefficient.
  RD4 C11 addresses an inference from conditioning to locality; MF3 uses
  exactly that inference, not an SU(N) claim. None is used as evidence
  against all matched representations.
- **N5, resolution.** The actual constructions concern finite lattice
  histories, local retained cuts and finite integrated coefficients. The
  norm witnesses concern finite connected-support families as their volume
  grows. No continuum, spectral, per-mode, physical mass-gap or general RG
  impossibility statement is tested or inferred. No numerical check was
  executed or represented as passing.
- **N6, partial closure.** Absorbing action into the reference, retaining an
  unnormalized history weight, or changing a compatible reader norm are
  mathematical constructions requiring proofs, not new physical axioms.
  The fixed-hole positive inequalities already supply partial closure.
- **N7, strongest counter-route.** A matched construction could absorb
  mandatory block actions into positive cell/reference factors, retain each
  region's one-use unnormalized price, and integrate every boundary reader
  jointly before imposing the final supported-jet norm. This changes the
  atom in MF1 and can attach hole-volume suppression absent from MH6/MH7.
  RD4 L1/L2 and its proposed boundary grouping (`RD4.md:338–397,513–519`)
  preserve that possibility. The concrete unresolved obligation is a
  uniform integrated mixed-jet and original-reader estimate for that
  **same** reference, including its local normalizer derivatives.
- **N8, recovery evidence.** RD3's normalized-species diagnostic is repaired
  algebraically by RD4's mandatory-mass extraction, while the new reference
  creates fresh interaction estimates. LIB1's active/full distinction and
  RD4 K2 already show that regrouping geometry changes apparent costs.
  These inspected sources support testing another representation; they
  supply no proof that all alternatives fail. Their complete mathematical
  arguments and all failure witnesses remain unchanged.

**Current checkpoint.** Completed: full fixed-mask proof in the exact real
mixed-jet norm, reconstructed constants, an exterior-boundary sharpening,
actual positive histories with unbounded holes, exact norm witnesses,
finite actual outer relative jets, and a specified integrated conditional-
Haar failure. Open: actual matched local mixed-group/reader prices and
prefactor logarithmic jets uniformly in histories, plus a stable compatible
hole/sector/extraction transition. No existing editable prompt, source,
audit or ledger file was changed. Later use should retain the source hashes,
recheck affected sources if they move, and submit any new substantive lemma
to the independent review required by PROCESS_LIGHT.
