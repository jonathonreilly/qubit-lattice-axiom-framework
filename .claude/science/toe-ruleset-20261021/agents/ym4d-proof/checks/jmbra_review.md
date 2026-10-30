# Independent hostile review of JMBRA

The final revised note can **LAND as partial research**. The initial HOLD's
sole binding correction is resolved: `JMBRA.md:643-652` now correctly states
the strict uniform depth margin as sufficient, and preserves summable
nongeometric alternatives. The added bulk-source diagnostic and explicit
singleton-cutoff qualification also survive the affected-source check. No
binding findings remain. The exact all-cut representation, ancestral
factorization, two tree estimates, weighted full-root/tail bound, finite
complex germ and actual failed-singleton witness survive at their stated
scopes. **LF-JMBR itself remains OPEN.**

This is a fresh-context, same-family review using the inherited configured
model and effort. I did not author or edit JMBRA. Earlier reviews were used
to locate obligations, not as proofs or votes. The load-bearing calculations
were reconstructed; section 4 below gives a different derivation of the
weighted full-root estimate. There were no subagents, numerical experiments,
formal-verification runs, Git mutations, audit actions or ledger changes.
The denied priority probe was not bypassed. Hashing and source inventories
were bookkeeping only.

The final reviewed note is the 767-line revision with SHA256
`6dd077a3383ea69b6ab04b629ee8d13be5b60958e542b1ae778eb48f90fc7c5a`.
The initial 729-line revision is preserved at `checks/jmbra_review_base.md`,
SHA256 `cc583e9e35ce344400e85d33315c2f6f32ff704027236ee290122638f56da8fb`.
The initial verdict was HOLD solely for the necessity overstatement recorded
in section 1. The complete affected diff and surrounding arguments were
read; the rest of the completed review is reused on unchanged content.
`checks/jmbra_review_fixes.patch`, SHA256
`62d0fd004ff0cd94521a9c99b4d510f84335936e7f5366280923150515965db9`,
matches the exact diff between those two note revisions. All 26 source
hashes were refreshed and still match `checks/jmbra_sources.json`, whose SHA256 is
`34eec395ddae3f8c32b3f1e915bd0f0da86462f64ea0de99564d44f34e21c8bf`.
The read-only ref check gave HEAD
`211e2ad24fade6c187de967ecb9d432c391f3796` and locally available origin/main
`01589af3faf806b736c42dc2f3bd625e9edead9f`. Remote freshness was not checked:
the task forbids Git mutations. AGENTS, SCIENCE_WORKFLOW and the inspected
claim-reviewer/freshness procedures agree with that local origin/main.
PROCESS_LIGHT and the explicit AUTHOR/reviewer allowlist govern this review;
only this review file is written.

Line locators below refer to the final JMBRA revision, unless another source
or the initial revision is named. A confirmed conditional theorem is not
confirmation of its actual Yang--Mills hypotheses.

| Substantive item | Finding | Binding fix or remaining obligation |
|---|---|---|
| Model, actual reference and source supports, 24-70 | CONFIRMED supplied-model scope | None. Keep R_h distinct from b_1 and retain original readers. |
| All-cut cancellation and exact failure predicates, 72-147 | CONFIRMED finite algebra | None. The inherited J_h remains joint; no product over bad components follows. |
| Elimination, creators and ancestral factorization, 149-237 | CONFIRMED | None. Fixed terminal kernels, outside parents and all other readers remain factors/supports. |
| Coefficient factorization, connected groups and logarithm, 239-310 | CONFIRMED conditional theorem | None. Actual coefficient rules, complete joint majorants and common-domain holomorphy remain inputs. |
| Weighted full roots, long tails and gas budget, 312-382 | CONFIRMED conditional theorem | None. Actual q_eta, d and Q_sf have not been evaluated. |
| Survival factor and complex-TV diagnostic, 386-422 | CONFIRMED at their stated inference-diagnostic scope | None. Neither diagnostic asserts an actual Wilson zero or failure of every adapted reference. |
| Boundary cancellation, finite-halo geometry and A23, 424-473 | CONFIRMED conditional estimates; actual A23 OPEN | Construct matched coefficients and their joint original-reference estimate. |
| Direct Haar/supremum failure and raw charge allocation, 475-501 | CONFIRMED | None. The failed majorant is not a no-go for joint L1 or adapted-reference methods. |
| Actual bulk-source response, 503-529 | CONFIRMED finite diagnostic | None. This concerns the complete log without a bulk/source remainder, not decay or analytic radius. |
| Common finite complex germ, 531-562 | CONFIRMED finite-volume result | Uniform D_* and local TV accounting remain OPEN. |
| Actual completion-failed singleton, 564-609 | CONFIRMED | None. Its n<n_0 applicability is now explicitly restricted to n_0>=2. |
| Exact size partition, final-price double sum and polynomial debit, 611-642 | CONFIRMED | Actual small-return activities and all failed alternatives remain unestimated. |
| Variable added depth exponent, 643-652 | CONFIRMED after correction | None. The criterion is now sufficient; the valid nongeometric escape and dyadic convergence proof resolve the initial HOLD. |
| Variable cutoff and next-step extraction, 654-677 | CONFIRMED arithmetic / correctly OPEN application | Supply uniform return estimates and the actual projection, contraction and generated-term budget. |
| Five-clause status and no-exhaustion scope, 679-767 | APPROPRIATE partial-research disposition | No LF-JMBR completion, retained status, universal obstruction or independent-wall count follows. |

## 1. Resolved correction: a uniform depth margin is not necessary

The initial revision's `:612-615` claimed a necessary strict uniform margin.
The final revision's `:643-652` states a sufficient geometric criterion and
includes the following counterexample to necessity. The initial HOLD is
resolved by this change.

For a small unreturned component put

    c = (4+c_B-n a_eff beta_-) log L >= 0.

The displayed final-price majorant, after the lower coupling bracket, is a
constant times `exp(c r-lambda_r r)`. For r>=1 choose

    lambda_r = c + 2 log(r+1)/r.

It becomes a constant times `(r+1)^(-2)`, whose sum converges, although

    n a_eff beta_- + lambda_r/log L - (4+c_B)
      = 2 log(r+1)/(r log L)

tends to zero. This counterexample satisfies precisely the proposed form
`exp(-lambda_r r)`; it does not require changing any Yang--Mills premise.
It rejects only the asserted necessary *uniform* margin, not A27.

The adopted wording distinguishes the sufficient geometric bound from
general summability. Its added convergence proof is valid: for k>=0 the
dyadic interval [2^k,2^(k+1)) has 2^k integers and each corresponding
`(r+1)^(-2)` is at most 2^(-2k). The interval contributes at most 2^(-k),
and these contributions have a convergent geometric sum. The r=0 term
is finite and does not affect this tail argument.

The same distinction is already explicit in `LFPRICE.md:122-131`. It is
particularly useful here because LF-JMBR permits extra suppression rather
than requiring every failure to obey one particular geometric estimate.

## 2. Actual matching and the integration algorithm

For fixed B write the all-cut density as
`chi_(A\B) W_out product_Y(chi_Y w_Y)`. The fresh-coordinate expression
T_B J_h is independent of all old I(B) variables. Integrating those old
variables produces exactly `product_Y C_Y`; cancellation leaves

    Z_A^(-1) integral chi_(A\B) zeta_B b_1 J_h K_1 dU_1.

Summing over B gives R_h/Z_A. This reconstructs A5 without a pointwise
ratio of the good/bad hard supports. Positivity of C_Y uses only the
interior cuts: setting each interior link sufficiently close to identity
satisfies them regardless of the frozen exterior. Positive real kernels
and a compact domain give a positive finite mass. None of this bounds it
uniformly as the system grows.

The factorization of the *bare* w_Y uses G_2 separation. A plaquette or a
two-endpoint-block kernel cannot read the interiors of two such separated
components. The completion predicate reads the larger retained collar,
and J_h can read the whole earlier chain; those facts are not erased by
the bare factorization. The representation agrees with `RD.md:325-430`,
especially R7/R8, and with `RD3.md:332-381`. The output fixed at V is not
an integrated normalized creator.

For A6, b_Y=1 requires every block of Y to be bad and every active block
at G_2 distance one from Y but outside it to be good. Thus Y is exactly a
maximal bad component. Multiplication by 1-a(Y) selects its actual
failure. The product over b_Y and 1-b_Y records the complete failure
list, including absence of every other failure. This reconstructs RD R3;
it does not turn a global history into independent local events.

The DAG calculation can be checked by inspecting a latest unselected
vertex. If it had a child in the selected ancestor set, it would itself
be an ancestor, a contradiction. It consequently appears only in its
creator and creators already removed, so its integral is one. Repeating
this proves A8. For two groups with disjoint full H supports, an edge
between their ancestor sets would put the parent in both ancestor
closures. Shared outside parents have already been put in both H
supports. Therefore the remaining factors separate exactly. This proves
A9, including the advertised qualification about later integration of y.
It fails if the terminal likelihood, Wilson action, predicate or another
reader is silently discarded. JMBRA does not make that substitution.

## 3. Connected types, both tree estimates and nonvanishing

The coefficient rule is essential. A selected set has one partition into
connected components of its H-overlap graph. A9 and factorization of c_I
give the product of the component weights w_J. Because H_i is nonempty,
two groups sharing a label cannot have disjoint supports. Thus the
resulting gas has exactly the selected sets of A11, without multiplicity
or a logarithm/integration interchange. A12 bounds the complete component
weight, not an independently estimated factor later placed under a new
law. It also retains local total variation in the complex case.

To check constants, let

    b_i = exp((mu+2)|H_i|) alpha_i,
    v_i = exp((mu+1)|H_i|) alpha_i.

The overlap sum of b_j through H_i is at most Q|H_i|. Hence b is a
supersolution of the rooted-tree recursion with vertex weight v when
Q<=1. Every distinct-label connected selection has at least one spanning
tree; allowing repeated labels only increases this positive majorant.
Its exponential child factors supply the unordered-child factorials.
Marking a constituent containing any specified ambient vertex bounds
the integrated-polymer norm at mu+1 by Q. Roots have not been restricted
to a charged core or active region.

For the logarithm, fix an order on the incompatibility-graph edges. In
Kruskal's algorithm an edge not in T can be freely present precisely when
it is later than every edge of the T-path joining its endpoints. All
connected subgraphs with that tree are therefore one interval [T,R(T)].
Their alternating sum is
`(-1)^|T| (1-1)^|R(T)\T|`, of modulus at most one. This bounds each Mayer
coefficient by its spanning-tree count, including tuples with repeated
polymer labels. The rooted coefficient is 1/(m-1)!; the remaining unit of
support exponent bounds the log norm at mu by Q.

There is no assumed logarithm hidden in this step. Scaling original
atoms by z gives the same absolute bounds with |z|Q; for |z|<=2 this is
at most 1/2. The convergent connected series exponentiates to the finite
gas near zero by its algebraic expansion and then throughout the disc.
Its exponential cannot vanish. Holomorphy in physical parameters requires
the separate fixed-selector, holomorphic-factor and envelope hypotheses
at `:258-260`; analyticity in z alone would not suffice. These hypotheses
repair the external-parameter qualification in REVIEW_LFPRICE rather than
treating its verdict as proof.

## 4. Independent full-root check of A15, then the tail

Here is an alternative to JMBRA's core-fugacity rescaling. Tilt every
small-field weight by `exp(eta |H_i|)` and let T_i be the positive
rooted-tree series for the full mixed family, with vertex weights

    v_i = exp((sigma+eta)|H_i|) alpha_i,
    v_gamma = exp(sigma|D_gamma|) a_gamma.

Let b_i=e^|H_i| v_i and b_gamma=e^|D_gamma| v_gamma. Their full rooted
input sum is q_eta+d<=1/2. The recursion consequently yields the stronger
pointwise bound

    T_i <= v_i exp((q_eta+d)|H_i|)
         <= b_i exp(-|H_i|/2),

and likewise for core labels. Let T_i^0 be the tree series containing
only small-field labels, and set Delta_i=T_i-T_i^0 for those labels;
for a core label set Delta_gamma=T_gamma. These nonnegative differences
are exactly the tree majorant with at least one core. For a small-field
root, subtracting the two recursions gives

    Delta_i
      = T_i [1-exp(-sum_(j overlaps i) Delta_j)]
      <= T_i sum_(j overlaps i) Delta_j.

Let C be the supremum over *all* ambient roots of the sum of Delta-label
weights whose supports contain the root. It is finite by the already
convergent tree majorant. Sum the last inequality through x, and then
sum the children through each y in H_i. Using
`k exp(-k/2)<=2` for k>=1 gives

    C <= d + C sup_x sum_(i:x in H_i)|H_i| T_i
      <= d + 2 q_eta C.

Therefore `C<=d/(1-2q_eta)`. Every integrated group containing a core,
rooted at an arbitrary vertex of its complete support, is dominated by
this difference series. Undoing the positive tilt proves A15. This
derivation does not anchor the output root to a core and independently
checks the denominator in the stated estimate.

If a group contains a vertex at distance at least r from the union of
its core supports, take a connected-support path from that vertex until
its first core. Its portion outside cores is covered by selected
small-field supports, so their total cardinality is at least r. The
tilt paid at least exp(eta r); removing it proves A16. Connected hulls
and the specified original graph are essential here. No contracted-hole
metric is substituted. Countable tails can be passed through the same
absolute majorant under the stated integration envelopes.

For a single distinguished core with only small-field decorations, its
rooted tree weight is bounded by
`a exp(sigma|D|) exp(q_eta |D|)`, proving A17 at its anchored scope.
It is not a substitute for the preceding full-root proof. A18 then
reserves a sufficient gas budget for the core-containing groups and a
separately supplied budget for the groups containing no core. It has
not calculated either budget on R_h/Z_A.

## 5. Reference survival, boundary bills and the actual failed attempt

Normalized creators alone give E_P 1=1. Inserting reference cuts instead
gives a(y)=E_P chi. The ratio of the raw uninserted cone to this reference
is 1/a(y), with all other readers retained if present. For A19, the
SU(2) event q>=1-delta has unnormalized mass at most
exp(-t(1-delta)); the opposite cap has positive mass m_delta and contributes
at least m_delta exp(t(1-delta)) to Z. Division gives the claimed exponential
loss. The mean -I is realizable, for example by a pure-gauge assignment
whose endpoint gauge values differ by -I, so every contour transporter
has that value. This is still only an inference test, not an identified
all-cut failure in the eventual stable class.

For a complex reference, triangle inequality gives A20 with
`T_ref=integral|w|/|integral w|`. On the two-point reference its denominator
is epsilon and the inserted numerator is epsilon+e^a-1. The loss cannot
be set to one. Neither positivity propagation nor a raw analytic kernel
bound controls it.

Under complete coefficient matching, every term in the log difference
touches Bdy. Summing through a boundary vertex pays at most q+b for each
sign and proves A21. The tail variant spends an additional support weight.
For A22, a spanning-tree walk has 2(n-1) star steps; each segment of
L^ell steps spans at most L^ell in each coordinate and meets at most 16
contracted blocks. The collar and geometric sum give exactly the stated
16 V_w r+32 V_w(n-1)/(L-1). Multiplying by 2(q+b) gives
`c_B=32 V_w(q+b)/log L`. This conclusion requires the initial halo and the
stated star-connected core/hull convention, not every G_2 core by name.

The direct-Haar test is an actual failed sufficient estimate. With the
displayed g, Re tr g=N-4 and s(g)=4/N. Hence the supremum of
`|exp(-u_0 s_p)-1|` is at least `1-exp(-4u_0/N)`. Every nonempty full
support supplies at least exp(mu+2), giving A23a and its threshold.
Closing ancestors cannot improve this supremum majorant. Separately,
expanding the Hilbert--Schmidt norm proves
`s(U)=||I-U||_HS^2/(2N)`. Allocating theta/m to terms owned at most m
times leaves a nonnegative raw rest. At an effective step, however,
`b_1 J_h=rho_h`; a charge taken from b_1 is not a price for rho_h unless
its compensating insertion is estimated jointly. A23 is correctly OPEN.

## 6. The finite analytic germ

At fixed real fine fields the terminal normalizers contain no continued
V. In the two trace terms, multiplication by the unitary Vbar and the
bound ||M||<=1 give an exponent change at most
`t_1 (exp(||Z_c||)-1)` per link. The original coefficient variation
costs at most `2u_0 sum|epsilon_p|`. This proves A24 for each complete
integral, including the source-independent denominator's smaller bound.

For |H|<=r<pi/2, each exp H has real part at least e^(-r)cos r.
Integration against the positive normalized real reference gives
nonvanishing; its absolute integral is at most e^r, yielding
`T_ref<=e^(2r)/cos r`. Compact domination supplies holomorphy and the
right half-plane fixes the branch. Zero-mass sectors are not normalized.
All earlier predicates are source-independent functions of integrated
real fields; a new V-dependent selector would require the separate
treatment stated in the note.

The bound for a fixed source polydisc grows with the number of original
plaquettes. Failure of this sufficient sector test is not proof of a zero.
The common uniform domain in clause 3, including the selected-output
interface emphasized in `REVIEW_RD3.md:287-325`, remains unproved.

## 7. The actual singleton and return arithmetic

For L>=3 the first e_1 link based at (1,1,1,1) and every plaquette reading
it remain inside Q. Each affected plaquette has value g or g^{-1} and
distance two. The second marked link starts at fine coordinates
`(L-1,L+1,1,1)` and ends at `(L,L+1,1,1)`, in the two blocks e_2 and
e_1+e_2. Its e_1,e_3 plaquette lies in N_1(Q), reads no I(Q) link and
has curvature distance two. Every plaquette containing this second link
crosses a block boundary, so none is an interior cut plaquette. The bad
block set is exactly {Q}.

The H11 completion cannot change that exterior plaquette. Its first
maximum is therefore at least two for every completion and every V;
the second maximum is nonnegative. Perturbing every link in a delta cap
changes any plaquette by at most 4delta. The displayed strict cap
preserves good cuts, the bad cut and the completion failure. Haar gives
positive mass, and Wilson/soft factors are strictly positive there even
at fixed V. This is a genuine legal-history witness, not a symbolic
failure predicate or a zero-mass sector.

**Cutoff clarification, now explicit at :607-609.** The witness passes any
local size-success threshold at least one. Its membership in the *separate*
n<n_0 return class requires n_0>=2; that class is empty when n_0=1. The
final note states this and distinguishes the two thresholds. The
witness remains valid regardless of that final cutoff. It neither
belongs automatically to an eventual stable chart class nor proves
that its rough exterior cannot earn an extra action charge.

Sorting every exact bad-set sector into small and large components is
an identity. Successful and failed completions partition each small
piece; integration alone supplies no activity bound or chart membership.
Every small failure must consequently retain an estimated return,
genuinely paid merger or sufficient extra suppression.

For A27, the lower bracket gives a term at most
`z^n L^((4+c_B-n a_eff beta_-)r)`. The floor-plus-one cutoff makes the
largest r-ratio, at n=n_0, strictly smaller than one. Summing r, then n,
gives both stated denominators. Maximizing
`d log u-(a_0-a_eff)u` gives the polynomial prefactor in :640-642;
retaining a_0 after absorbing an unbounded power would be wrong.
The variable-cutoff geometric sum in :654-660 is also correct. Neither
calculation constructs returns, supplies the relevant-operator
projection, or proves A28. A fixed vacuum term repeated over levels
must retain its level volume factor.

## 8. Source cross-checks and all five clauses

The necessary original passages inspected were LFPRICE section 6,
LF1/LF2/LF6-LF10 and REVIEW_LFPRICE; RD R2-R8; RD3 D1-D13, D16-D21 and
RC1-RC3; RD4's target and L1-L8; REVIEW_RD3's binding B2/B3 obligations;
SOURCE_LOCAL_HISTORY_RETURN_ASTRA H1-H5 and H11-H14; LARGE55 TL/PP/COL
and E9/E11-E16 with CODEX_REVIEW_LARGE F1-F3/F5/F6/F9; LIB1 sections 1,
5-6 and its full-root qualification; and SOFTHARD G1/G2. Decision 4 was
checked in the original `PROOF.md:2446-2455`. The complete initial JMBRA
argument was read, including text omitted from initially truncated tool
output; targeted rereads supplied all missing passages. The complete final
diff and surrounding affected arguments were then read and checked against
the preserved source; no changed argument was omitted.

These sources confirm the intended boundaries, not the truth of their
predecessor reviews. In particular COL excludes surviving readers;
TL/PP are scalar bounds rather than source-polymer propagation; H11/H12
really include the fixed exterior curvature maximum; and LIB1 counts
inactive roots and full original readers. None of these supplies A23.

The attribution to Balaban and Dimock is properly limited. The primary
abstracts identify Dimock's [Large fields](https://arxiv.org/abs/1212.5562)
and [Convergence](https://arxiv.org/abs/1304.0705) as expositions using a
scalar phi^4 model in three dimensions. No external lemma or unread
paper proof bears a mathematical step in this review.

| LF-JMBR clause | Reviewed disposition |
|---|---|
| 1 | Exact finite representation and support-sector matching are proved. This does not establish uniform local reference budgets or the full complex-domain construction. |
| 2 | OPEN: the actual joint charged/reference/boundary integral A23 and its full rooted sum remain unproved. |
| 3 | OPEN: only a finite nonzero germ and its extensive sufficient bound are established. |
| 4 | OPEN on the actual model: exact conditional grouping/factorization and weighted sufficient bounds are proved, but their actual local coefficients and matched reference are unconstructed. |
| 5 | OPEN: exact partitions and a positive failed-singleton sector do not prove small returns, their failed alternatives or next-step extraction. The local necessity wording is corrected. |

JMBRA has not manufactured a closed lemma from conditional graph algebra.
Its stated next construction remains comparable in strength to the
missing joint part of LF-JMBR. The final acceptance means partial research
only, with no retained/audit status, physical
identification, RG induction, Yang--Mills theorem or all-route no-go.

## 9. Confirmed addition: actual-reference bulk source response

The final addition at `:503-529`, with its N5 scope entry at `:737-742`,
was read and checked in full. Its mathematical content is correct at the
following scope:

    partial_(epsilon_p) log Q_h |_(epsilon=0)
       = -u_0 E_(nu_h,V) s_p,

where nu_h,V is the complete positive R_h law at fixed real V. Z_A has
no original coefficient sources. Differentiating the compact finite
integral proves the formula. For RD3 D1's two-block size-forced failure,
the strict original-field cap fixes the whole history independently of
U_1. A sufficiently small nontrivial perturbation of an unmarked link
on a distant original plaquette preserves the cuts and makes s_p>0 on
a positive-measure open subcap. Positive kernels make the expectation
strictly positive for every fixed real V.

Thus the *complete* log Q_h cannot be represented by coefficients
confined to a fixed finite core collar with no bulk/source remainder.
This does not refute a boundary expansion after that remainder is
retained, a spatial-decay estimate, or a uniform analytic-domain
construction. No uniform lower bound is obtained. It is useful finite
reference bookkeeping and does not perform the coordinator's source-
radius work. The final prose retains these qualifications. The derivative
formula normalizes only a positive-mass sector; RD3's explicitly rebuilt
two-block sector supplies that premise. The note's existing zero-mass
convention is unchanged.

**Unresolved binding findings: none.** The initial sole binding finding is
resolved in the identified final revision. The author note and every
editable prompt remain unchanged by this reviewer. Only
`checks/jmbra_review.md` was created and updated. This verdict accepts a
partial research artifact; it does not certify completion of LF-JMBR.

VERDICT: LAND
