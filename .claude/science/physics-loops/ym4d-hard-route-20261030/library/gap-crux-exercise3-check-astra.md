# Repo search

The requested target-specific prior note is absent at `df74a74219b82791f74f14ce61da67de4b36186a`.
The November 8 repository digest records searches of main and PRs 10114,
10133, 10134 and 10141. It predates row 998 and is not a check of W1.
I checked its two nearby hits on fetched main `8b11ae2bb95e`:

- `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:4,79–94`
  concerns finite Z_N on equal even periodic tori. It is useful prior
  covariance work, extended to U(1) by row 786; it is not Wilson U(1).
- `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`
  concerns a determinant-weighted Dirichlet Maxwell law. Its covariance
  bound is for a different measure and boundary; no transfer is made.

Closer lane work is row 708's product device and CAS, row 786's periodic
Villain score, and row 884's centre-even flat-state witness. Their exact
lines are used below. None is repeated as a new result. No renewed broad
search of the PR branches was needed for this bounded W1 check.
The registry search found no owner for PT, KF, CAS or this check.
FINISH records row 999's same-provider check and expressly holds the
cross-provider check requested here. This task supplies that check only.

Provenance: OpenAI/Codex; requested model/effort `gpt-6-astra/xhigh`;
source commit `df74a74219b82791f74f14ce61da67de4b36186a`.
Research text, not an audit; this report grants no status.
The initial FINISH locator exposed row 999's summary. That exposure is
disclosed; verdicts below rest on the source and displayed arguments.
No numerical or computer-assisted proof is used.

## Scope

Completed W1's tests (a)–(e) first, then its statement list. No new attack.
The three important failures are the unsupported Wilson periodic bridge,
the inference that separation must be numerical, and the identification
of CAS with a free-starting-scale CONTR. The other corrections preserve
domains, hypotheses and existing conditional status.

The outline and CA-I were each fetched once into the new empty directory
`/tmp/sa-gap-crux-exercise3-check-astra.6CQ3fa/`, at `31a47c543775`.
Credit for their text belongs to Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors. The prior product device belongs to row 708;
the target text is Claude Fable 5.2's row 998. Other credits follow the
specific arguments below.

## Tests (a)–(e), before the verdict list

Write X for `gap-crux-exercise3-max.md`; other local paths below are in
`library/`. Line references are to the pinned checkout.

**(a) Tensor product, including the projection — passes.**
This tests X:698–713, conditional on each factor's stated (TM).
For a spatial box B let E and V be its links and vertices. Normalized Haar
measure identifies
\[
 L^2((G_1\times G_2)^E)=L^2(G_1^E)\mathbin{\widehat\otimes}L^2(G_2^E).
\]
Write A_i for multiplication by the square root of the spatial plaquette
weight, C_i for the product of temporal one-link convolution operators,
and P_i for averaging the action of G_i^V. Fubini, first on simple tensors,
gives A=A_1\otimes A_2, C=C_1\otimes C_2 and P=P_1\otimes P_2.
Gauge invariance makes A_i and C_i commute with P_i. Consequently
\[
 T=ACP A=(A_1C_1P_1A_1)\otimes(A_2C_2P_2A_2)=T_1\otimes T_2.
\]
Equivalently, restrict to the invariant spaces, whose product is ran P.
The trace norm of this positive tensor product is
Tr(T_1)Tr(T_2). Its eigenvalues are the pairwise products. Simplicity and
positivity of the top eigenvectors pass to their product. This verifies
closure under products; it does not newly prove (TM-gen) for an individual
weight. That remains the input printed in `gap-crux-fp.md:319`.
Credit for the transfer construction: Osterwalder–Seiler and Lüscher;
for the product device in this lane: `gap-mid-max.md:229–232`.

**(b) The bulk constant — passes.** Let q_i(n)=F_i(n)/|n|. By (TM) in
each direction, the monotonicity of the positive eigenvalue l^p norms
makes q_i nonincreasing in each side (`gap-crux-restate.md:37–43`).
Given epsilon>0, choose boxes n^(i) with q_i(n^(i))<f_i+epsilon/2.
At the coordinatewise maximum n of these boxes, both inequalities hold.
Thus inf_n(q_1(n)+q_2(n))<=f_1+f_2+epsilon; the reverse inequality is
pointwise. Let epsilon decrease to zero. Hence f=f_1+f_2 and D=D_1+D_2.
This uses the common directed family of boxes, not an invalid general
interchange of an infimum and a sum.

**(c) Wilson U(1) masslessness to the periodic seed — not supplied.**
X:213 itself says the Wilson coverage was not verified. The existing
source-scope read, `prior/gap-lit-u1.md:9–19`, distinguishes Fröhlich and
Spencer's nonsummable field-strength correlations on Z^4 from this finite
periodic trace statement. It records their detailed Villain proof and
their asserted Wilson extension with omitted derivation. Guth's cited
Villain Wilson-loop bound establishes deconfinement, not this trace seed.
No cited theorem in those records supplies the missing Wilson periodic
bridge. This is a failure of the implication claimed at X:213, not a
counterexample to Wilson U(1) masslessness.

There is relevant prior progress: `gap-tu-retry.md:198–250` gives a bounded
score with nonsummable correlations in every periodic Villain local
limit, for beta>=2^14. It explicitly leaves Wilson cosine open at 53–59.
Do not redo that result. Given the appropriate U(1) transfer and insertion
trace formulas, Theorem S and Lemma COV (`gap-crux-fp.md:323–338`) turn a
seed into exponential summability in a periodic local limit, contradicting
that score result. The transfer/insertion application must remain named;
the Villain result is not a published Wilson periodic-seed theorem.

**(d) First-passage clause — requires correction.**
The outline defines Wilson SU(2) first-passage data at SA 6844–6861 and
the continuum sequence at 6871–6879. CA-I 631–683 gives the matching
reference-window definition. The reference coupling g is fixed and small.
The continuum clause requires K_j=K(beta_j,g) to tend to infinity.
For a fixed beta and fixed g the first-passage cutoff, when defined, is
one integer. Repeating that datum cannot meet K_j→infinity. An individual
datum can of course be repeated; merely saying “has first-passage data”
does not exclude such a sequence. X:738's “arbitrarily small g” is not the
reason. Nor has the account defined that flow for general w_p weights.
One must specify either the Wilson-only clause, false outside its domain,
or an extension with its hypotheses, before using KF(c).

**(e) What changes in row 988 — only the proposed exclusion rule.**
`gap-unit-max.md:231–246,354–357` leaves the scale-crossing input open.
KF supplies no such input. With a genuine ultraviolet clause, K7 alone
does not impose an additional separation *beyond* first passage. This
changes Route 3(c) and N2's last sentence, not the unsuccessful route.
However, Route 3(b)'s specific light-level assertion is only a K7 belief.
Proposition V proves no seed for w_p at beta_t; it does not prove bounded
D there. Hence it cannot replace K7 as a theorem placing w_p in branch G
of Corollary Z4. This is already visible in `gap-phys-seed.md:322`:
the branch conclusion retains “if D is bounded there.”

## Statement verdicts

All HOLDS verdicts retain the source's named inputs. They do not verify
those inputs anew or confer scientific standing.

| W1 statement | Line in X | Verdict | Exact scope or correction |
|---|---:|---|---|
| (i) Lemma PT(a) | 697,705–708 | **HOLDS** | Product Haar integral and the common-box infimum argument in test (b). |
| Lemma PT(b) | 698–700,708–711 | **HOLDS** | Test (a), including the gauge projection. Each factor's (TM) and all required axis exchanges remain premises. |
| Lemma PT(c) | 701,711–713 | **HOLDS** | Divide the tensor-product trace by the product top eigenvalue. The largest nonvacuum normalized eigenvalue is max(r_1,s_1); use m=+infinity for a rank-one factor. |
| Lemma PT(d) | 702–703,713 | **HOLDS** | S=S_1+S_2+S_1S_2>=S_i. If both S_i<=t, then S<=2t+t^2. |
| Corollary PT1 | 715–722 | **HOLDS AFTER CORRECTION** | Replace “U(1) in its massless phase” by an admitted factor with no periodic seed, or retain that as an explicit unproved Wilson premise. A factor-only hypothesis is excluded only when it actually holds on some second factor and survives adjoining the no-seed factor. An always-false hypothesis is no counterexample to a valid implication. |
| PT1's published Wilson supplier I28 | 213 | **FAILS** | “So it has no seed there” is not supplied by the cited published results; test (c). This verdict concerns the asserted deduction. |
| (ii) KF(a) | 730 | **HOLDS** | Given Proposition V, (TM-gen), and ZD-c, applied to the numerical (W) inequality on admissible spacings. A physical seed would give a strict finite-box seed at beta_t for large j, contradicting V. |
| KF(b) | 731 | **HOLDS** | Contraposition, on a class containing M' and with T_W defined there. If the class already excludes M', there is no test instance. |
| KF(c) | 732–733,737–738 | **HOLDS AFTER CORRECTION** | Specify the domain and require K_j→infinity at one fixed g. The repeated finite-cutoff datum fails this stronger clause. The proof's varying-g reason is wrong; test (d). |
| KF(d): H must fail at M' | 734 | **HOLDS** | This is KF(b). |
| KF(d): it must contain a separating number | 734–735,738 | **FAILS** | No such necessity follows from contraposition. The valid conclusion is H(M')=false. A bound on deviation from a linear log weight is a proposed way to separate, not the only logical form. |
| Corollary KF1 | 740–744 | **HOLDS AFTER CORRECTION** | Retain the change to Route 3(c)/N2 and the unchanged unsuccessful route. Delete the unconditional list of necessary U(1)/photon tests: each comparison must meet the same H, including its ultraviolet clause. Apply PT1 only on a product-closed class with H true after adjoining the no-seed factor. |
| (iii) 6c product row | 540 | **HOLDS AFTER CORRECTION** | The product algebra holds. Supply no-seed for the first factor and distinguish a clause about the SU(2) factor from one about the whole model. The “decrease persists” objection remains only ARGUED here. |
| 6c w_p row | 543 | **HOLDS AFTER CORRECTION** | V gives failure of T_fix for every size, conditional on its exact van Enter–Shlosman SU(2), four-dimensional input and (TM-gen). “A number” is not logically forced. The exclusion of a continuum first-passage sequence needs test (d)'s corrected clause. |
| 6c K7 line row | 544 | **HOLDS AFTER CORRECTION** | The BELIEF label is correct. It is an analogue of V only for a seed conclusion, with the preceding w_p row corrected. It is not a theorem about branch G or a universal test of K-flow. |
| 6c frozen Q_8,2T row | 542 | **HOLDS** | In the stated frozen limit, centre-even flat multiplicity is at least two. No fixed finite coupling failing an existential seed at every box is inferred. |
| (iv) 6d row 24 | 577 | **HOLDS AFTER CORRECTION** | The dependency is not T3 alone. Row 982 N2 explicitly also invokes T2 (`gap-hcphys-max.md:266`). Retain the claim as that row's argued restriction on the specified port. W3, not this check, owns a proof of T3. |
| 6d row 28: re-admit K-flow | 581 | **HOLDS AFTER CORRECTION** | The first-passage separation is valid with test (d)'s precise clause. Replace “valid necessary conditions” by tests whose hypotheses must be verified; see KF1. |
| 6d row 28: “(better: w_p)” for Route 3(b) | 581 | **FAILS** | V proves no seed, not branch G. Bounded D at its transition is missing. K7 itself stays belief-grade. |
| 6d row 30 | 583 | **HOLDS** | As a limit on the one-scale exclusion: row 996's search supplies no general exclusion of K-flow. It does not say that every result of row 996 concerns one-scale properties; that row explicitly records path statements and leaves (U1)/(U2) unattempted. |
| 6d row 33 | 585 | **HOLDS** | `gap-escape-opus.md:233–244` says the selected hilltop set and point start did not test the potentially metastable relaxed-slice sets. Thus no ESC refutation follows. This reads the scope of the run, not its numerical evidence as proof. |
| 6d ex2 #18 | 586 | **HOLDS** | The cited MK recursion theorem includes both SU(N) and U(N); see `gap-form-exercise.md:139–145`, credit Ito and Seiler. This checks the group-blind scope, not the unrebuilt MK convergence theorem. |
| 6d ex2 6c point 1 | 587 | **HOLDS** | The blanket Q_8/2T exemption is invalid for the frozen even trace; retain the fixed-beta limitation of check 884. |
| (v) 8.5 correction 1: same mechanism | 799–804 | **HOLDS AFTER CORRECTION** | Credit row 708's contraction mechanism. Replace identity with “continuum dyadic analogue”; the printed quantifiers differ, as shown below. |
| 8.5 correction 1: converse for original CAS unproved | 805–808 | **HOLDS** | CAS starts at size 3 and controls every integer size in its band. Neither Z3 nor D(2a)<=16D(a) proves all its pre-seed inequalities. No separating model is claimed. This does not apply to the existential-base CONTR as printed. |
| 8.5 correction 2 | 809–815 | **HOLDS** | The finite-group correction faithfully retains check 884's centre-even frozen obstruction. |

## The quantifier failure in correction 1

This is a check of X:799's claimed identification, not a new route.
CAS (`gap-mid-max.md:64`) starts at a=3 and quantifies over every integer
a>=3 satisfying eps<D(a)<=M. In contrast, X:750–751 allows an existential
L_0 in the dyadic set P and only triggers when D^+(L)>=eps, where
eps=6.1×10^(-4). It has no prescribed starting size.

Given (PHYS-SEED), the proof of ZD-c
(`gap-phys-seed.md:320`, using Z3 at 283–294) supplies a q in (0,1) and a
seed length l such that
\[
 D^+(2^k l)\le {1024\over5041}q^{2^k}\quad(k\ge0).
\]
Choose k_0 so this is strictly below eps for all k>=k_0. This is an
existence choice from q^{2^k}→0, not a computation. Set
L_0=2^{k_0}l, B=eps and theta=1/2. Every antecedent in CONTR is now false,
and its base bound holds. Thus
\[
  (\text{PHYS-SEED})\ \Longrightarrow
  (\mathrm{CONTR})\quad\text{as X:750–751 actually quantifies it}.
\]
The converse is the finite descent already written at X:761–762. Enlarge
theta to max(theta,1/2) if needed; this preserves the required
inequalities and makes 0<theta<1. Therefore the printed existential-base
CONTR is equivalent to PHYS-SEED, given these lane inputs. X:755–756 and
770 **FAIL** when used to deny that converse. They implicitly fix L_0
before the seed, unlike the displayed definition.

The safe correction is exact: CAS is prior work; its converse is not
established by the cited argument. CONTR reuses its descent mechanism,
but its free starting size makes the converse immediate. A prescribed
pre-seed starting scale would be a different hypothesis. None is added
or attacked here.

## Frozen-sector check and logical limits

Check 884 (`gap-crux-exercise2-check-astra.md:235–259`) supplies the prior
hand witness. In Q_8 and 2T, the commuting triples (1,1,1) and (i,1,1)
remain in different orbits under conjugation and central sign flips:
centrality of the first entry is preserved. Their orbit indicators are
orthogonal centre-even flat vectors. The normalized transfer tends at a
fixed box to the flat projection, whose rank on that sector is at least
two. Its excited thermal sum is consequently at least one in that limit.
This is the existing witness, not a new enumeration. Taking beta to
infinity at each fixed box does not exchange the quantifiers to produce
one finite beta working at every box.
The limiting projection has a nonsimple top eigenvalue, so it is not
itself an instance of (TM)'s simple-vacuum premise. Testing an actual tool
requires the finite-beta estimate or a justified limit of that tool.

The repaired PT1 conclusion is equally conditional. If a factor M_1 has
S_1(N;(2N)^3)>=1/5041 for every N, PT(d) excludes a seed in M_1×M_2.
If H(M_2) holds and H survives that product, a class-wide H⇒seed is false.
If H instead requires the entire model to be Wilson SU(2), the product
does not meet H. Similarly, a literal Wilson-only first-passage clause
already excludes the standalone U(1) and free-photon comparisons. No
comparison model constrains an implication before this domain test.

## Read boundary and disposition

The required X sections were read: 1.2, 3.2, 6c, 6d, 8.1, 8.2 and 8.5;
8.3 was read to compare CONTR with CAS. The W1 source ranges in
`gap-crux-restate.md`, `gap-phys-seed.md`, `gap-crux-fp.md`,
`gap-unit-max.md`, `gap-mid-max.md` and check 884 were read, together with
the bounded supplier ranges cited above. Existing results are used with
their premises, not re-audited.

Before the SA source read, I used the index README, chunk-06:59–72 and
its neighbouring rows, and the first-passage/mass-gap entries of
`obligations.md`. The CA-full index identifies the first-passage chapter;
the CA definition was read at I:610–685. The outline source read was
SA:6836–6879. These are definitions and conditional construction inputs,
not a new proof of the flow. No 4.12–4.19 operator input is used here.

Fröhlich–Spencer, Guth, van Enter–Shlosman and Ito–Seiler are used through
the repository's exact prior source readings, with their stated limits.
Their original papers were not re-fetched or rechecked. In particular,
this report does not certify the omitted Wilson argument, the SU(2)
four-dimensional specialization in V, or MK convergence. Balaban's
papers were not needed. No numerical run, Lean run or audit was performed.
Mechanical source-location checks do not discharge a mathematical step.

Only this output file was written. The checked sources, FINISH, the
registry and every status record remain untouched. The check supplies
corrections to W1; it supplies no order-one estimate or mass-gap result.

RESULT: W1 completed at df74a7421. PT(a)–(d) HOLD under their inputs; PT1, KF(c), KF1 and the specified filter rows require the stated domain and premise corrections; KF(a)–(b) HOLD conditionally; KF(d)'s compulsory-number inference and I28's published Wilson periodic-seed deduction FAIL. The frozen Q_8/2T correction HOLDS. Correction 8.5(1) HOLDS AFTER CORRECTION: original CAS has no proved converse here, but the printed existential-base CONTR is equivalent to PHYS-SEED by Z3, so its claimed non-converse FAILS. No new attack, computer-assisted discharge, status grant or progress through the mass-gap wall.
