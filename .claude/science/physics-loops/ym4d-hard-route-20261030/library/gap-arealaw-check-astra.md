## Repo search

The target-specific `prior/gap-arealaw-check-astra.md` is absent at
`ba60ad8acfea963184744af70113135d5599d967`. The lead's reusable
`prior/repo-search-2026-11-08.md` records searches of main and PRs 10114,
10133, 10134 and 10141. It concerns older UV targets, not this slab theorem.
Its closest named hits concern a single plaquette transfer correlation and
a noncompact Maxwell covariance; neither supplies the rectangular SU(2)
area law. I fetched and checked the relevant current sources:

- Main `bb4ec020d5ada57c630dd89acc98a68397ade423`,
  `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`,
  370–482: existing finite-product comparison and a covariance bound.
  This is prior Dobrushin machinery, not the sharp slab theorem.
- The same main, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md`,
  120–145: a noncompact Maxwell covariance bound, with a different measure.
- PR 10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`,
  `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`,
  106–149: a positive one-step transfer witness. It supplies no rectangular
  loop area estimate. The prior digest records its identical PR 10133 copy.

There is no target-specific “Repo prior work” line in row 828. I reused the
lead's wider PR search and did not repeat unrelated UV searches.
`open-registry.md` has no area-law, vMF, Dobrushin, Durhuus or CNS owner.
The only area-law files found here are the assigned author note and this
check. Row 825 is the source being checked, not a competing check owner.

The `sa-index` README, matching chunk rows and their neighbours, and
`obligations.md` were consulted first. Searches for area law, Dobrushin,
von Mises, Durhuus and Cao found no occurrence in either downloaded source
or the CA 4.12–4.19 index. Chunk 01 and chunk 29 point to outline
588–599 and 31860–31882; those source ranges explicitly separate the
scalar existence construction from a mass-gap estimate. They supply no
slab-area-law proof. No stronger absence claim is made.

## Check record

Codex, gpt-6-astra, xhigh; 2026-11-12; FINISH row 828. This is a research
check of Claude Opus 5.5's row 825 at the pinned commit, not an audit.
It grants no scientific status. Only this output file is edited.

The check covers every mathematical statement of `gap-arealaw-opus.md`,
including its boundary extensions, and checks the scope of its comparison
claims. Existing single-site results are named inputs; their prior check is not counted as
a second independent proof. No numerical or computer-assisted proof is used.
Literature novelty is restricted to sources actually read and is not an
absence theorem.

Downloads, each fetched once, are kept outside the repository:

- Sussman–Alpoge outline and CA-I at `31a47c543775`:
  `/tmp/sa-gap-arealaw-check-astra.sHYzYQ/`.
- Cao–Nissim–Sheffield, arXiv:2509.04688v2:
  `/tmp/cns-gap-arealaw-check-astra.06UWRt/`.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text; Sky Cao, Ron Nissim and Scott Sheffield; Bergfinn Durhuus
and Jürg Fröhlich for the slab method; Dobrushin for comparison. The lane's
single-site input is due to Codex gpt-6-astra, and its layer formulation
to Claude Fable 5.2. No Balaban estimate is used here.

Checkpoint: complete. Sources remain unchanged at the pinned commit.
The remaining obligation is to apply the endpoint, face-label and scope
corrections in the author's note; this check does not edit that file.
No load-bearing proof step failed. No numerical proof route was attempted.

## Verdicts: conventions and the covariance bridge

Line numbers below refer to `gap-arealaw-opus.md` at the pinned commit.

**Conventions, lines 59–95: HOLDS.** The lane weight is
`exp(beta_W Re U_p)`. CNS (1.2) is `exp(N beta_CNS Re Tr Q_p)`.
For SU(2), `N Re Tr Q_p = 4 Re U_p`, hence `beta_W=4 beta_CNS`.
The fixed additive Wilson-action constant cancels from every probability.
Quaternion conjugation and unit left/right multiplication preserve the
Euclidean norm. In particular,
`Re(q_x a conj(q_y) conj(b)) = <q_x,b q_y conj(a)>`.
Thus the slab bond coefficient is exactly `beta_W`, without a further
factor of two. CNS's `1/[8(d-1)]` becomes `1/[2(d-1)]`; at `d=4`
this is `1/6`. The proposed threshold is four times this sufficient range.

**Lemma S(i)–(iii), lines 188–211: HOLDS.** The spatial plaquettes are
fixed after conditioning on H. Every remaining plaquette contains two
vertical edges at the same height k. For its displayed orientation,
`Re(a q' conj(a') conj(q)) = <q,a q' conj(a')>`.
Its factor therefore involves only slab k. Product Haar measure and the
finite positive density give an explicit conditional product over k,
with each factor divided by its own partition function. Integrating the
other slabs does not leave a coupling between the remaining slabs.
Faces shared by two slabs are fixed variables under H. Periodicity joins
height `L_nu-1` to height zero, but still creates no plaquette with vertical
variables at two distinct k. This checks the independence assertion itself.

**Named inputs, lines 166–184: HOLDS as an invocation of the stated
inputs.** Read `gap-vmf-lip.md` Theorem V, Corollary V1, Lemma DC and
Lemma INF(12), and its twist proof (lines 59–338, 352–417).
Read the corresponding prior Opus check. The new proof uses the
all-field chord bound, not the older radius-restricted conjecture.
Each neighbour contributes at most `beta/4`, and there are six distinct
neighbours when every periodic side is at least three. Lemma DC explicitly
permits any second probability measure whose kernels agree off D,
including a measure supported on `h_y=xi`. Absolute continuity with
respect to the first measure is not a hypothesis.

**Lemma SC(a), including Steps 1–3, lines 215–242: HOLDS.** To check the
pinning without conditioning on a null event, put
`K(h)=exp(beta sum_b J_b h_u.O_b h_v)`, and define
`Z_y(xi)=integral K(h_{-y},xi) d sigma^{B minus {y}}`.
This is positive and continuous. Then

`mu^xi = delta_xi(dh_y) K(h_{-y},xi) d sigma^{B minus {y}}/Z_y(xi)`

is defined for every xi, and its mixture with density `Z_y(xi)/Z`
recovers mu. For z different from y, cancel factors not incident to z
in this density. What remains is precisely `exp(F_z.h_z)` divided by
its one-site integral, with `h_y=xi`. This proves the off-y kernel
identity at every environment in its support. At y the kernel is
`delta_xi`, which DC allows to differ without restriction.

For `f=e.h_x`, DC yields `|e.(mu^xi h_x-mu h_x)| <= 2 G_xy`.
Taking the supremum over real unit e gives the vector norm without a
factor of four. Positivity and the row bound give
`(C^n)_xy=0` for `n<d(x,y)` and `(C^n)_xy <= q^n` otherwise.
Thus `G_xy <= q^d/(1-q)`. Zero bond coefficients can remove paths;
using the full nearest-neighbour distance still gives the stated bound.

**Lemma SC(b), Step 4, lines 223, 243–244: HOLDS.** Disintegrate against
`h_y=xi` before taking an absolute value. The covariance is the integral
of `(mu^xi h_x-mu h_x).M xi`. Since `|M xi|<=1`, the bound is `2G_xy`.
No sum over coordinates and no dimension factor are needed.

**Lemma SC(c), Step 5 and beta zero, lines 224–248: HOLDS.** Simultaneous
sign reversal preserves every bilinear bond, even for negative J and
arbitrary orthogonal O. It gives zero one-site means. At beta zero,
product Haar measure gives zero covariance at distinct sites directly.

**Corollary H, lines 252–276: HOLDS AFTER CORRECTION at beta zero.**
For `0<beta_W<2/3`, all claimed constants and quantifiers hold.
Writing each U(2) background as a scalar phase times SU(2) changes its
bond coefficient to `J=cos(theta-phi)`, with `|J|<=1`. Either choice
of phase square root produces the same original bond action.
An entry and an inverse entry each have two signed real coordinates;
their bilinear covariance has four terms, each bounded by `2G_xy`.
Hence `C1=8/(1-q)`, `C2=log(1/q)` work for distinct sites. The elementary
same-site bound 2 is smaller than C1. The nontrivial centre element is -I.

First undefined expression: line 258 at `beta_W=0`, where `log(1/q)`
is not a finite real constant. Correct text: use those constants for
`0<q<1`; for `q=0`, take `C1=8`, `C2=1` and use independence at distinct
sites. In the power notation define `0^0=1` for coincident sites.
The theorem's desired positive finite constants then exist at beta zero.
For the black-box formulation over every L, the omitted slices L=1,2
can also be included: their graph diameter is at most 3, and
`C1' = max(C1,2 exp(3 C2))` handles them by the bound 2. No new influence
estimate on double bonds is required. The rectangle conclusion for L=2
can instead be absorbed into its final prefactor, as the author suggests.

**Section 3.5, the eight-step interface table: HOLDS with the beta-zero
convention just specified.** Uniformity is in backgrounds, sites and
side lengths, not just in a selected slab configuration.

**Section 3.6, lines 295–305: HOLDS AFTER CORRECTION of logical wording.**
The proof uses INF and DC, not (AS-bg). The displayed twist identity
controls a summed one-plane response and supplies no covariance inequality
by the argument given. This establishes that the present proof has not
derived the CNS hypothesis from (AS-bg) alone. It does not prove a general
non-implication between all conceivable versions of the two properties.
Keep the author's ARGUED/GUIDE labels; do not upgrade this observation to
a no-go theorem. The recalled electric-flux picture is unused.

## Verdicts: slab reduction and area law

**Lemma R, lines 334–356: HOLDS.** A direct recursion checks the
noncommuting order. Number the T slabs from 0. Put `X_0=H_b` and
`X_{j+1}=conj(q_{x,j}) X_j q_{y,j}`. Induction gives

`X_j = conj(q_{x,0} ... q_{x,j-1}) H_b (q_{y,0} ... q_{y,j-1})`.

Thus `<X_T,H_t>` is the real part of the stated loop product, by cyclic
invariance of the real part. The order is `T_{T-1} ... T_0`, not its
reverse. Given H, each T_j is a function of its own slab; horizontal
holonomies are deterministic. Integrating each matrix entry in the
conditional product law gives `E[T_{T-1} ... T_0|H] = E[T_{T-1}|H] ... E[T_0|H]`.
No independence of the two vertical edges within a slab is asserted.

For unit quaternions X,Y,q,q', orthogonality of left multiplication gives
`<Y,conj(q)Xq'> = <qY,Xq'> = <q,R_Y^T L_X q'>`.
Both `R_Y` and `L_X` are orthogonal real maps. The norm of the mean
matrix is the supremum of these bilinear forms over X,Y, bounded by the
supremum over O(4) in the lemma. Submultiplicativity finishes the proof.
Distinct slabs are essential and are guaranteed by `T<L_nu`.
The half-side bound on R keeps the two vertical sides distinct.

**Theorem A, lines 311–330 and 363–379: HOLDS AFTER CORRECTION** of the
beta-zero rewriting only; its power-form bound HOLDS. Keep the exponential
rewriting restricted to `beta_W>0`. In the first orientation the slab
sites are graph distance R apart, since `R<=L_mu/2`. SC(c) bounds each
of the T mean matrices by `2q^R/(1-q)`. R gives its T-th power before
averaging H, uniformly in H. Reversing the two coordinate directions
gives the other bound. Since `2/(1-q)>1`, their minimum is

`|<W_l>| <= (2/(1-q))^min(R,T) q^(RT)`.

All constants are independent of the four torus side lengths. At beta
zero every rectangle has distinct boundary edges; integrating one edge
against Haar measure makes its fundamental Wilson loop mean zero.
The power-form bound remains valid, with `RT>=1`. Its logarithmic
rewriting in line 328 should not be evaluated at zero.
First failing proof step: none in the power-form theorem.

**Corollary A1(i)–(iii), lines 383–391: HOLDS AFTER CORRECTION at beta
zero.** State its finite constants for `0<beta_W<2/3`. The inequalities
`min(R,T)<=(R+T)/2` and, with `s=min(R,T), t=max(R,T)`,

`s(c0-s0 t/2) <= 2c0^2/s0`

prove (i) and (ii), with exactly the constants printed. If
`t>=2c0/s0`, the left side is nonpositive. Otherwise it is at most
`c0 t < 2c0^2/s0`. No perimeter-law input is used. Part (iii) follows
by division by RT. For any existing loop string-tension limit with
`max(R,T)->infinity`, its lower bound is s0; existence of that limit
is not proved. Interpret `-log 0=+infinity` when a loop mean vanishes.
At beta zero use `|<W_l>|=0` directly, with, for example, `C=c=1` in (ii).
This fixes the undefined `s0=log(1/q)` at line 383.

**The numerical example, lines 393–395: HOLDS by hand.** At beta_W=1/2,
`q=3/4`, and the prefactor is 8. To check the strict decimal inequalities
without numerical evaluation, use
`log((1+z)/(1-z))=2 sum_{j>=0} z^(2j+1)/(2j+1)`.
For z=1/3, the first three terms sum to `842/1215` and the tail is
at most `1/6804`. Their sum is `23581/34020 < 52/75`; after multiplying
by 170100 the strict inequality is `117905<117936`.
Thus `20 log 8 = 60 log 2 < 41.6`. For z=1/7, the first two terms give
`log(4/3)>296/1029>23/80`, since `23680>23667`.
Therefore `400 log(4/3)>115`, and the exponent is below `-73.4<-73`.
These rational inequalities are the verification; no run supplies them.

**Corollary A2, lines 397–401: HOLDS.** A fixed rectangle eventually
satisfies both half-side restrictions. Its Wilson observable is a bounded
continuous cylinder function. Convergence of the finite-dimensional
probability laws passes both inequalities to the limit. This assertion
needs no claim of uniqueness or choice of subsequence.

**Lemma INF' and Corollary A3(a), lines 403–423: HOLDS.** A free box gives
finite slab cubes, with at most six neighbours per site. Removing bonds
cannot increase the row bound. Conditional product factorization and
global sign symmetry persist. The ordinary cube distance between the two
slab sites is R, including loops on the free boundary. Therefore both
orientations of Theorem A hold for every rectangle in the box.

**Corollary A3(b), lines 407–410 and 414–428: HOLDS.** In a slab with
fixed exterior links, every plaquette containing a variable vertical edge
contains either a second variable edge in that slab or one fixed exterior
vertical edge. The latter terms are fixed local fields `b_z.h_z`, supported
on the boundary of K. They depend on h_z, but b_z depends on no variable
spin. This is the precise meaning needed at line 420.
All-field V1 still gives the neighbour coefficient `beta/4`, regardless
of these fields. SC(a),(b), which require no sign symmetry, therefore
bound the connected part by `2q^R/(1-q)`.

Compare this slab law with the law with b_z deleted. Their kernels agree
at every site off the boundary; the latter law has zero mean by sign
symmetry. DC applied to every unit scalar projection gives
`|mu_k h_x| <= 2q^m/(1-q)` and the same bound at y. Taking the supremum
over projections introduces no dimension factor. Hence, for every
orthogonal O,

`|mu_k(h_x.O h_y)| <= 2q^R/(1-q) + 4q^(2m)/(1-q)^2`.

The original T slab maps remain conditionally independent. Multiplying
their bounds proves exactly (b), uniformly in omega. For m=0, specify
`0^0=1` if beta zero is kept in this formula; the direct Haar argument
also covers that case.

**Corollary A3(c), lines 411–433: HOLDS.** For a fixed rectangle, put
`r=max{|coordinate of a vertex of l|}` and `m=n-r`. The DLR equation
expresses its mean as the integral of finite-volume conditional means.
The bound in (b) holds for every exterior condition, so the absolute
value of that integral obeys it. With R,T fixed and n tending to infinity,
`q^(2m)` tends to zero. Repeat in the other direction and take the smaller
bound. This proves the assertion for every DLR state, without a symmetry,
extremality, periodic-approximation, or uniqueness assumption.

**Remark A4, lines 437–448: HOLDS AFTER CORRECTION at beta zero.** For
`0<beta_W<2/3`, let `a=(beta_W/4)(2e^theta+4)` on the torus. With the
specified D, the identity is `A^n_xy=e^{-theta R}(D^{-1}AD)^n_xy`.
In the distinguished direction each of two neighbours changes phi by
at most 1; the other four leave phi fixed. Consequently the weighted
row sum is at most `2e^theta+4`, even at the cusp of periodic distance.
Summing gives `G_xy <= e^{-theta R}/(1-a)` for `a<1`.
The slab product and orientation swap give line 443 with its exact
prefactor. Any theta below `log(2/beta_W-2)` is admissible. Take the
large-loop lower limit first, then take the supremum over theta. This
proves the stated string-tension lower bound; it does not claim a finite
prefactor at the endpoint theta.

In a free cube take a signed linear coordinate phi, increasing from x
toward y. The weighted row sum is at most `e^theta+e^{-theta}+4`.
Thus replace a by `beta_W(2+cosh(theta))/2`. The allowable rates are
exactly those below `arccosh(2/beta_W-2)`. For arbitrary-boundary cubes,
keep this weighted connected bound and the unweighted mean-error bound
from A3(b). The latter tends to zero on exhaustion, proving the same
rate for every Gibbs state. At beta zero the displayed logarithm and
inverse-beta expressions are undefined; state instead that all loop
means vanish, so every finite exponential rate is allowed.

**Remark A5, lines 450–454: HOLDS.** In d dimensions the slab has
`2(d-1)` distinct neighbours and coefficient `beta_W/4` per neighbour.
Thus `q=(d-1)beta_W/2`; every preceding pinning and product argument is
unchanged, with this q. The sufficient range is `beta_W<2/(d-1)`.
CNS's range in Wilson normalization is `beta_W<1/[2(d-1)]`.
The factor four compares these two stated sufficient conditions. It
asserts neither optimality nor novelty in dimension two.

**Remark A6, lines 456–461: HOLDS only as the labelled consistency
comparison, after retaining its recalled-input qualification.** Elementary
expansion of `arccosh(2/beta-2)` gives
`log(4/beta)-beta+O(beta^2)` as beta decreases to zero.
The Bessel series give `I_2(beta)/I_1(beta)=beta/4+O(beta^3)`.
These are compatible leading terms. A fixed-loop character expansion
does not by itself justify exchanging beta small and area large to
identify the true string tension. Its claimed expansion remains a
recalled literature input here; neither this check nor the note proves
that uniform expansion. It is unused by Theorem A.

**Remark A7, lines 463–465: HOLDS given the explicitly cited CNS
Theorem 2.3**, with Corollary H's beta-zero and small-L qualifications
above. This is a second way to state the implication, not an independent
validation of the area law or a check of DF80's full proof.

## CNS source reading

The pinned [Cao–Nissim–Sheffield paper](https://arxiv.org/abs/2509.04688v2)
was fetched once. Its PDF hash is
`b74d2ca0555260cf218fe15bb105f34faeaa6674fcbe87215d597a83c3a373f5`.
I read pages 1–5 and page 6 through the end of Proposition 3.2, and visually
checked the formulas on pages 2–5. `pdftotext` was unavailable; pypdf
extraction and PyMuPDF rendering supplied the reading. These tools were
used for retrieval only.

| Source statement / target lines | Verdict on the reading | Finding |
|---|---|---|
| Definition 2.1, Remark 2.2 / 103–107 | HOLDS | Product Haar on sites; the two bond fields may be U(N)-valued. The latter extension is used for the U(N) conditioning argument. |
| Slab interpretation / 109–111, 211 | HOLDS AFTER CORRECTION of face labels | For the upward q used in Lemma S, set CNS `A=a^{k+1}`, `B=a^k`. Alternatively use inverse vertical spins and keep `A=a^k`, `B=a^{k+1}`. |
| Theorem 2.3 hypothesis / 113–126 | HOLDS | Matrix entry versus inverse entry; constants uniform in fields and volume; a nonidentity scalar centre element. The source does not define its distance explicitly. Our periodic graph-distance bound is sufficient for graph or the usual Euclidean distance. |
| Theorem 2.3 conclusion, Remark 1.2 / 128–132 | HOLDS | Rectangles with both sides at most L/2; periodic tori. Remark 1.2 describes the free-box extension. |
| Proof sketch and missing prefactor / 134–142 | HOLDS as a reading, conditional on its cited perimeter bound | Multiplication of T covariance estimates gives `C1^T`, not a single C1. This is another perimeter exponential, so the indicated absorption still works after enlarging its perimeter coefficient. |
| Proposition 3.2 / 144–148 | HOLDS | It states decay for smooth local observables, with both gradient and L2 norm factors. The proof gives `4(d-1)N beta` in (3.1), and `K=(N+2)/2-1-4N beta(d-1)` for SU(N). For SU(2), d=4, this is `1-24 beta_CNS`; positivity is exactly `beta_W<1/6`. It imports the remaining estimates from SZZ, as the note says. |
| Companion paper / 150–156 | HOLDS | [2505.16585v3](https://arxiv.org/abs/2505.16585v3), pages 1–3,6–7, states its theorem for U(N), all N≥1; the new proof assumes large N, with bounded N referred to the classical result. Its weight is `exp(2 beta Re Tr U_p)`. No SU(2) theorem is stated there. |
| Unread DF80 and Chatterjee / 158–160 | HOLDS as the stated verification boundary | Their full proofs were not checked here either. The direct proof of Theorem A does not import them. |

The face-label correction is algebraic. With the upward variables,
`Re(a q_y conj(a') conj(q_x)) = Re(q_x a' conj(q_y) conj(a))`.
That is CNS's displayed action with A=a' and B=a. For example,
`q_x=1`, `q_y=a=i`, `a'=1` gives -1 for the actual plaquette,
but +1 if one keeps upward q and inserts A=a, B=a' in Definition 2.1.
Simultaneous inversion of the vertical variables, or swapping the two
fixed faces, resolves it. All estimates are uniform in both faces, so
no constant, threshold, or independence conclusion changes.

The CNS sketch also prints `z != 0` where its zero-mean inference uses
`z != 1`. Its theorem has the correct hypothesis, which the target uses.
These are observations about the reading, not a check of the full
DF80/SZZ dependency chain or an outward correction request.

## Novelty and scope verdicts

**Strong coupling, all Gibbs states, and no continuum or 4D spectral-gap
conclusion, lines 469–484: HOLDS.** The proof supplies a fixed-coupling
Wilson-loop bound. It neither follows the asymptotically free trajectory
nor proves the neutral transfer-matrix spectral gap. It needs no uniqueness
assumption. The larger-group extension is not supplied by the S^3 input
and quaternion argument. The stated `2/9` uniqueness range is the range
of the cited lane input, not a universal ceiling on every method.

**The claimed slab ceiling near 0.94, lines 485–489: HOLDS AFTER
CORRECTION if read as a conclusion rather than GUIDE.** The flat slab
is indeed the three-dimensional O(4) nearest-neighbour model. If a
thermodynamic sequence of its symmetric periodic laws has nondecaying
two-point correlations at some beta, uniform exponential decay cannot
hold at that beta. That implication is rigorous. The numerical location
of ordering is recalled, not proved or checked here. Replace the
conclusive wording by: “Such ordering would obstruct the uniform slab
hypothesis; about 0.94 is a recalled numerical guide.” No numerical
ceiling is established by this report. The row-sum sufficient test ceases
to contract at 2/3; this does not rule out stronger comparison arguments.

**Novelty comparisons, lines 499–560: HOLDS AFTER CORRECTION of the
priority wording and one cited condition.** The checked mathematical
comparison is a fourfold extension of the sufficient interval in CNS
2509.04688v2, with explicit constants and an every-DLR-state conclusion.
The method remains a consequence of the named single-site input,
Dobrushin comparison and the classical slab idea. It is not a new
slab mechanism. Source-specific findings:

| Comparison | Verdict | Primary reading and limit |
|---|---|---|
| CNS 2509, 503–507 | HOLDS | The exact thresholds, unspecified constants and torus/free-box forms agree with pages 2–6. The explicit formulas and every-DLR-state proof are not stated there. “New relative to this text” is the supported comparison. |
| CNS 2505, 508–509 | HOLDS | The U(N) theorem and normalization were read on pages 1–3,6–7. U(2) must not be identified with SU(2). |
| Osterwalder–Seiler, 510–512 | HOLDS AFTER CORRECTION | The companion CNS description leaves the dimensional constant unspecified. That does not determine a numerical SU(2) endpoint. Say “the cited description does not state 2/3”; it does not establish a strict improvement over every version of the original result. OS78 itself was not read. |
| Shen–Zhu–Zhu, 513–515 | HOLDS as an attributed comparison | CNS page 1 says its area-law question was not addressed by SZZ; page 2 says SZZ's threshold is half its own. This gives Wilson `1/12`. No new check of SZZ's full proof is claimed. |
| DF80/Chatterjee, 516–519 | HOLDS | CNS 2505 page 1 describes conditional mass-gap-to-area-law results. Their method receives credit; their original statements were not read here. |
| Refereed priority of the quarter, 520–522 | HOLDS AFTER CORRECTION | “Not located in row 819's bounded search” is supported as that report's conclusion. The present check does not certify universal refereed priority or redo the Royer/Wu literature review. |
| BB October 18, 525–532 | HOLDS AFTER CORRECTION | Theorem 7 states the quarter; Theorems E,F state the `2/9` range. Theorem G and Proposition 18 require HGDS for the area law. **Proposition 21 states GDS in 2D, not the stronger HGDS.** Replace “the condition is verified only for 2D” by “GDS is verified in 2D; the displayed HGDS area-law criterion remains conditional.” No 4D slab range appears in these passages. |
| BB v4.47.1, 533–536 | HOLDS for the cited proposition | `strong-coupling/paper/main.tex` lines 866–899 still states HGDS as an assumption before deducing area law. A search of that source has no Durhuus or slab hit. This is not a full read of the archive or a check of every companion file. |
| Hexagon v4/v7, 537–539 | HOLDS as a bounded report; v7 rechecked | The downloaded v7 introduction cites CNS for area law. Its two area-law matches are this citation and the bibliography. No Durhuus or sigma-model match was found. It has other “slab” uses concerning transfer operators, not this uniform spin-model criterion. The earlier v4 search remains attributed to row 819; it was not downloaded again here. |
| Mihajlovic, 540–546 | HOLDS | Pages 355–356 explicitly use `exp(beta sum Re Tr U_p/N)`, so beta equals beta_W without an inferred convention. Theorem 78.1 has `18 beta<1`, followed by a Chatterjee area-law application. Page 383 labels its stronger starting statement an external input. This gives the stated factor twelve against `2/3`. |
| Faizal–Shabir, 547–550 | HOLDS AFTER CORRECTION of priority wording | PDF pages 26 and 171 (printed 24 and 169) contain Theorems 3.2 and B.4 with existential `beta_1` or `beta(N)` and constants not evaluated to an SU(2) number. Say “no numerical threshold comparison is established by these passages.” An unspecified threshold does not prove that their whole range is smaller. |

The last distinction matters at lines 552–557. Replace the blanket NEW
summary by: “The range extends CNS's stated SU(2) interval from 1/6 to
2/3. No matching explicit slab-area-law threshold was located in the
bounded sources examined. Priority against unread works and unspecified
strong-coupling constants is not established.” This retains the useful
result without an unsupported literature-wide conclusion.

The “beyond every claimed gap range” heading at lines 474–478 also needs
its printed bounded-search qualification in the headline. The cited
Mihajlovic abstract gives a conditional three-link functional at 0.354,
not a proved physical gap. That distinction is present in the body and
must survive any summary. These comparisons grant no validity to those
papers' proofs. Their computer certificates, where mentioned, are not
used by this check.

## Source record and disposition

Additional downloads each used a fresh empty directory. No downloaded
paper, extracted text or rendered page was added to the checkout.

| Source | Scratch directory |
|---|---|
| CNS 2505.16585v3 | `/tmp/arealaw-cns-companion-astra.WCduBl/` |
| Mihajlovic 2611.11534v1 | `/tmp/arealaw-mihajlovic-astra.WKDNPJ/` |
| Faizal–Shabir 2606.19362v1 | `/tmp/arealaw-faizal-shabir-astra.xmjJQH/` |
| Hexagon 2610.00341v7 | `/tmp/arealaw-hexagon-v7-astra.wBftsQ/` |
| BB `v4.47.1/strong-coupling/paper/main.tex` | `/tmp/arealaw-bb-v4471-astra.WEcXv9/` |
| BB October 18 archive and selected paper | `/tmp/arealaw-bb-oct-astra.V9AwT8/` |

The [October 18 Zenodo record](https://zenodo.org/records/23449466)
labels the record version 2.0.0 but distributes release v2.0.2. The paper
read was its `preprintYangMillsDobrushinCeiling/YangMillsDobrushinCeiling.pdf`:
abstract; Theorems E–G and 7; Proposition 18 and its proof; Proposition 21's
statement; Table I. The v4.47.1 proposition was read from the tagged
[primary source](https://github.com/creelie/4Y-M/blob/v4.47.1/strong-coupling/paper/main.tex#L875).
The later [Hexagon v7](https://hexagonmath.org/pdf/2610.00341v7),
[Mihajlovic](https://arxiv.org/abs/2611.11534v1) and
[Faizal–Shabir](https://arxiv.org/abs/2606.19362v1) passages read are
specified in the comparison table. None of their claimed proofs is
imported into Theorem A.

Retrieval hashes are in
`/tmp/sa-gap-arealaw-check-astra.sHYzYQ/download-manifest.json`.
Index search output is in that directory's `index-hits.txt`.
A short additional web search used “SU(2) area law 2/3”, the BB title,
and both CNS identifiers. It found no matching explicit threshold;
this is only a search result, not proof of priority. The original
source and both single-site proof/check files remain byte-identical
to the pinned commit. No audit, ledger, registry, source proof or
FINISH row was changed. No proof computation or external post was made.

**Section 7 marks and the opening summary: HOLDS AFTER CORRECTION**
by the individual verdicts above. Keep the checked-input dependency,
restrict logarithmic formulas to positive coupling, distinguish face
orientation from equality of the family of laws, and retain the stated
limits on recalled inputs and novelty. There is no FAILS verdict on a
load-bearing lemma. The first undefined constant is Corollary H line 258
at beta zero; its correction is explicit above. The GDS/HGDS citation
error first occurs at line 530 and affects only the literature comparison.

RESULT: HOLDS AFTER CORRECTION — the power-form SU(2) area law for 0<=beta_W<2/3, including free boxes and every Gibbs state, holds from the named inputs; no load-bearing step fails. Correct the beta-zero logarithmic constants, face labels, GDS/HGDS citation and novelty/ceiling wording. This is a research check and grants no status.
