# Independent review of the fixed-reference source return continuation

**PASS WITH BOUNDED CLAIMS for this source unit.** The corrected mathematical
continuation is supported on its stated finite-volume, level-zero, small
global-chart domain. This does not certify the whole PR, the all-history
STEP return, continuum existence, OS reconstruction, or a physical Yang–Mills
mass gap. No auxiliary Hessian or face-decay bound is identified with a
physical spectral gap.

The original 856-line [source](SOURCE_LOCAL_RETURN_CONTINUATION_ASTRA.md) is
immutable at `fae864bbf31b276363ef96be120afa6d69e79683`, SHA-256
`9542b717307e743b4e8daf25a8549c44562666563375cf66f6147eda3cb85e3f`.
Its original author receipt has SHA-256
`4f00d2c21808de330606dfc02434d9b9b7fc566019325cc54d47f282529c6960`.
The history-corrected source at `8b38c6f7b802479f763bc995d96ee45fdcc03795`
has SHA-256 `0cb55655ec73f31dd8df4b6353b0d3f6345191579c38945819da881860e311d6`.
The final source at `e4464249d9729a0bf7725be67611aa95aba5df01`, also including
the dependency-link repair, has SHA-256
`ac985bb9b41a0d9d52ead7c2932df73e59c713c28c5c45f0629003552eee1243`.
Final source/evidence identities are bound in the
[review receipt](checks/review_source_cont_receipt.json).

The coordinator explicitly requested Astra/max in a separate restricted-input
reviewer context. This is same-family/fresh-context independence, not
cross-family review; no separate runtime-model attestation is available.
The reviewer did not author or edit the scientific source. Current-main
methodology is `ca2bc7ddf64790da96cd43d42017d000fbfe4808`, supplied by the
coordinator and read with read-only `git show`. The installed entry was read
first; its complete difference from current main was recovered and the
current-main requirements control. The coordinator holds the cooperative lock.

[Independent criteria](checks/review_source_cont_prestate.json) were saved
before reading either author checker, receipt content, or numerical output.
The complete source read had already exposed section 5's advertised check
summary; this is disclosed rather than calling the review blind. A distinct
reviewer implementation was written before inspecting the author scripts.

## Findings and same-context corrections

**Source-continuation-history-1 — repaired scope error.** Original lines
179–184 call (C8)'s right side analytic in complex B although (C8) contains
an arbitrary retained history. A fixed W domain and holomorphic b,C do not
make that history holomorphic. For example take F(a;B)=(a−B)²/2, sigma=1,
W in [−1,1], b=B, C=1, and the fixed hard history 1_(a>1). Its sector
integral is zero for −1<B≤0 and equals
`integral_(1−B)^1 exp(−w²/2)dw` for 0<B<1. Its left and right derivatives
at zero are 0 and exp(−1/2). No holomorphic continuation through zero matches
that real function. This rejects the unqualified inference, not the
empty-history theorem or actual Yang–Mills histories.

The coordinator replaced only the affected paragraph. It retains entire
epsilon dependence at fixed real B for bounded epsilon-independent histories,
restricts the stated B continuation to Theta=1, and requires a separately
supplied jointly holomorphic fixed-W pullback with integrable domination for
general histories. It explicitly excludes obtaining that property from a
fixed W domain alone. I read the complete diff and verified the corrected
hash. This repairs the claim without changing §§2–4's empty-history bounds.

**Source-continuation-links-1 — repaired publication wiring.** The original
load-bearing predecessor/CX-R/STEP references were code-formatted names.
Current-main audit compatibility requires actual Markdown dependency links.
The coordinator added links to the exact predecessor, review, repair record,
STEP, CX-R/review, and consumed PROOF/SRC2/B2/STEP-review references. I read
the complete link-only diff from the history-corrected commit and verified
the final hash. The ten local destinations resolve. No equation, premise,
claim scope or checker changed. This supplies source wiring, not an audit
verdict or certification of the whole publication package.

## Exact claim disposition

| Surface | Disposition and exact scope |
|---|---|
| (C8) raw Haar sector | Confirmed on the fixed real chart, retaining tree-averaged history, Haar constant, scalar Jacobian, main action, cutoff probability and actual reference factors |
| Complex-B paragraph | Confirmed after qualification; arbitrary real hard histories receive no analytic continuation by fiat |
| (C9)–(C16) compositions | Confirmed in the explicit original-B/epsilon domains, with scalar component and full support-incidence norms |
| (C17)–(C19) fixed-sector zero-freeness | Confirmed for empty history, beta=mu+4, h≤1/4, eta≤c sigma p and the common chart; not fixed nonzero B as sigma→0 |
| (C20)–(C22) common majorant and faces | Confirmed for normalized probability product measures supported in the same white domain, including pins |
| (C23) product events | Confirmed for fixed positive-probability product events, retaining their original probability; zero-probability events excluded |
| (C24) local insertion | Confirmed as a bound; nonvanishing only under the separate positivity/phase criterion |
| (C25)–(C34) affine homotopy input | Confirmed from the reviewed critical branch and actual force/Hessian compositions with original-source labels |
| §4.3 remote marked unions | Confirmed using full vector incidence and nu=mu+2; no remote endpoint, source or connector omitted |
| (C35)–(C37) cube flux/logarithm | Confirmed for selected empty-history global-chart sectors, with complete factors and outward signs; the bounded norm is an extensive connected logarithm's rooted norm |
| (C38) link balls | Confirmed with D=N²−1, correct radial density, scalar dimension n_d=Dn and outward normal |
| General Xi_h, every Den_Y, collars/holes, all coarse fields, induction, E_cb/E_NA, OS/existence/mass gap | Outside the proved conclusion; neither closure nor impossibility asserted |

## Independent mathematical reconstruction

### Fixed sector and all-order interaction size

The frozen predecessor's exact tree-Haar identity integrates tree variables
with normalized Haar volume one and replaces a non-invariant history by its
actual tree average. In additive scalar Lie coordinates,
`dHaar(exp a)=c_N j(a) da`. Absorbing −sigma² sum log j into F exactly once
and using a=b+sigma CW gives `sigma^(n_d) det C`. Criticality of b for F_0
and C^T K C=I remove only the baseline linear/quadratic terms. Rewriting the
Lebesgue Gaussian and its normalized cube restriction gives exactly
`(2pi sigma²)^(n_d/2) z_p^(n_d)` in (C8). The source term
`sigma^(−1) sum epsilon_p Ds_p(b)[CW]` survives. Vacuum, main action and
reference factors have not been charged to the cubic fluctuation budget.

Cauchy homogeneous projection acts on the absolutely summable atom families.
Degree m in B costs (eta/eta_0)^m times the original norm. Removing the total
constant component uses b(0,0)=0, then summing m≥1 gives
`tau eta/(eta_0−eta)`. Every projection keeps its original support. Applying
the same argument separately in B and epsilon to b(B,epsilon)−b(B,0), using
b(0,epsilon)=0, gives the product of geometric sums in (C25). Cancelling
constant atom families can be discarded as a total zero function; no nonzero
background term is thereby removed.

For q scalar analytic inputs, Cauchy gives `f(t)=H(1−t/a)^(−q)`. Expand first
at zero, then allocate factors to b and delta a. This yields T_3. A marked
support vertex lies in the local stencil, a background atom, or a fluctuation
atom, costing respectively `T_3`, `b_* partial_b T_3`, and
`y partial_x T_3`. Every attached atom meets the local stencil at its output,
so all unions are connected and retain all original source labels. The
incidence sum is over all starting scalar coordinates, as required by the
predecessor's norms; a component supremum is not substituted for it.

Taylor's integral remainder bounds T_3 by f's third derivative. In the b
marked term, its fourth derivative contributes 2^(q+4)/a^4; b_*≤a/2 reduces
this to the stated 2^(q+3)/a^3. The x derivative is the second-order remainder
of f'. Thus (C12)'s constants are conservative and valid. The actual Wilson
s_p has zero constant/linear coefficient at zero. Its increment retains
b_*x and x²/2, and both marked derivatives retain their supports. Substitution
of b_*≤C_b c sigma p yields (C15), including the nontrivial-background force.
Only the field-dependent normalizer difference enters the uniform local
vertices; its u-dependent vacuum remains in F_0(b).

### Common product majorants, cancellation and zero-freeness

One explicit common construction is as follows. Set m_S=sup|exp(−U_S)−1|.
Let w_abs(P) be the sum of products of m_S over connected distinct support
collections with union P. Every normalized probability product measure gives
`|w_lambda(P)|≤w_abs(P)`. Define a_Y by the second-stage sum of
`|phi^T| product w_abs(P_i)/n!` over ordered tuples with union Y. These are
THE SAME nonnegative numbers for every lambda. Both rooted tree bounds in
the fully read CX-R proof apply to these absolute coefficients, giving
`sup_v sum_(Y contains v) exp(nu|Y|) a_Y≤2h` at beta=nu+2. A supremum over
unrelated decompositions is unnecessary.

The canonical coefficient F_Y uses only measures and original sources on Y.
Thus changing the measure on A cancels every coefficient disjoint from A
exactly. The remaining differences cost 2a_Y and, marking a vertex in A,
4h|A|. This proves (C21) before estimating a ratio. The convergent cluster
series constructs an analytic exponent and proves that its exponential is Z;
nonvanishing follows afterward. Positivity is used only for the reference
probability measure, never the complex interacting density.

Pinning a scalar coordinate changes only its box measure. Removing that
normalized Gaussian marginal gives phi(p)/z_p and (C22). Conditioning
independent coordinates on positive-probability events gives another product
measure and retains mu(E) in (C23). Pinning A and then integrating Theta gives
(C24). If Theta≥0 and 4h|A|<pi/2, each exp L_A has positive real part, proving
the stated additional nonvanishing criterion. This does not extend to
arbitrary large correlated histories.

### Homotopy force, Hessian and original-source incidence

For star=M+B, the two marked product terms give
`star(AB)≤star(A)star(B)`, and transposition preserves both counts. The
(C27) inverse series starts with C_0^(−1) explicitly. It never assigns unit
norm to a labelled identity. Under Q_D D_C rho≤1/2 the inverse norm is ≤2Q_D.
Multiplication by W costs p, and a matrix atom includes both its output and
remote W endpoint. Vector multiplication therefore proves (C29), including
the sum over ALL output coordinates incident to a fixed support box.

The actual local Hessian entries have unmarked bound f_H(tau); marking a b
factor adds tau f_H'(tau). The ordered-entry counts include both endpoints
and scalar inputs, and the factor two pays M+B. A difference of degree n has
n replacement positions and n+1 root/mark choices. Differentiating
f_H+t f_H' gives n(n+1), precisely (C31)'s H_3. Thus (C30) bounds actual
source-substituted families at every b_s, not merely evaluated matrix entries.

Differentiating the actual gradient along b_t gives
`g_s=−integral_s^1 H_t d dt`. Subtracting C_1^T K_1 C_1=I gives the three
terms of (C33): two cost Q_C H_2 D_C rho each, and the middle term costs
Q_C² H_3 D_b eta rho. The bound eta≤eta_0/2 gives A_Q. In g_s^T C_s W,
marking g costs its incidence times M_C, and marking C costs B_C times the
component norm of g. Their sum is bounded by Q_C times the vector norm.
The quadratic term costs p² B(Q_s)/2 since both W endpoints already occur in
the matrix label. The cubic terms use the same local Taylor construction for
F_epsilon. Haar, normalizer and every original epsilon input remain present.
The domain is nonempty by taking sigma p³ and rho p² small after fixing the
constants.

### Remote marked attachments

Put ell_Y=2a_Y and k=4h_bar≤1. Pin a connected velocity root S and expand the
exact ratio `exp(sum_(Y intersects S)L_Y)`. Every attachment meets S and
retains its original-source support Y. Weighting at mu, the unmarked
attachment sum is ≤exp(k|S|). If a specified marked vertex lies in S, root
summation costs B_v at mu+k≤mu+1. If it lies in an attachment Y, mark that
attachment first; all roots meeting Y cost ≤|Y| B_v at this rate. Finally
`sum_(Y contains v)|Y| exp(mu|Y|)ell_Y≤k`, since
`|Y|≤exp(2|Y|)` and the common majorant is available at nu=mu+2.
The two contributions total `(1+k)B_v^(mu+1)`. This retains remote sources,
remote W endpoints and full connectors. The beta=mu+4 velocity budget
supplies more than the mu+1 rate required here.

### Complete flux and link balls

For the full pullback J_s f(a_s),
`div_W v_s=Tr(C_s^(−1)E)=partial_s log J_s` and
`grad_W f dot v_s=grad_a f dot partial_s a_s`. Differentiating the complete
density therefore gives its divergence. This accounts for the determinant
derivative and all boundary minors. I_s is nonzero FIRST, by inverse-series
invertibility and the cluster exponential for U_s; only then is its
logarithmic derivative used. The main action, Haar constant, Gaussian factor
and det C_s in (C35) cancel from a normalized face because they occur in
both numerator and denominator.

The two cube faces have opposite outward signs, reference density phi(p)/z_p
and the FULL velocity insertion. The marked estimate, both signs and the
s interval of length one give (C37), including factor 4Q_D. Its branch is
fixed by integrating the derivative and vanishes at epsilon=0. A logarithm
can be extensive while its rooted norm is volume-independent. This does not
assert a volume-independent raw side/sector ratio.

For link balls the measure factors over links, hence boxes; scalar
independence within a link is unnecessary. Its boundary density is
`(2pi)^(−D/2)|S^(D−1)|p^(D−1)exp(−p²/2)/z_(D,p)`.
Replacing one link measure by uniform sphere probability changes only its
box. Each normal component W_j/p is bounded by one and lies in the existing
face support; summing j is paid by B_v. There is one outward sphere, hence
no two-sign factor. The top form has degree n_d=Dn and the cutoff probability
is z_(D,p)^n. This gives (C38), of order
`rho p^D exp(−p²/2)/z_(D,p)` for fixed D. Intersections of link boundaries
have zero codimension-one surface measure.

## Evidence, failures and scope

The independent [reviewer script](checks/review_source_cont_independent_02.py)
completed with **33 checks and 20 omission controls**, exit 0, empty stderr,
and about 4.35 seconds elapsed. [Its output](checks/review_source_cont_attempt02.json)
contains exact rational/complex algebra and explicitly non-interval 80-digit
quadratures.

- A distinct non-diagonal affine two-coordinate polynomial top form agrees
  exactly between differentiated volume moments and all oriented boundary
  minors. Removing the determinant derivative, one outward sign or the
  scalar sigma Jacobian gives a nonzero rational-complex residual.
- An actual nonlinear two-coordinate action independently differentiated
  into gradient/Hessian verifies (C32) and all three terms of (C33).
- Direct enumeration of 128 spin states gives Z=1+urt, Z_pin/Z=1+abceh and
  remote insertion ab+ceh. Four extra disconnected factors cancel. Omitting
  normalization, the remote W endpoint, remote source or connector fails.
  A small complex input regime has beta=4 norm below 0.023.
- A nonzero-background complex quadratic action with an extra vacuum scalar
  agrees between original-domain quadrature, completed square and normalized
  fixed-reference factorization to about 5.3e−82. Dropping its linear source
  term changes the answer by about 2.58e−10. Cutoff-probability, action and
  determinant omissions also fail.
- The D=8 ball's symbolic radial derivative and complex normalized flux agree
  to about 1.65e−82. Removing p^(D−1), the velocity's radial p, or substituting
  link count for scalar Jacobian dimension fails.
- A different four-link noncommuting SU(2) plaquette in the explicitly chosen
  i-Pauli coordinates has varied-link force `(sin(3B)+sin(5B))/2=4B+O(B³)`.
  Matrix and quaternion calculations agree. This prescribed background is
  not a computed solution of the full lattice critical equation.
- Exact mixed derivatives check 15 coefficient allocations through total
  degree seven. All-order conclusions come from the written proofs. The
  hard-history counterexample remains in the record.

Attempt 01 was interrupted with exit 130 after about 4.5 minutes in SymPy's
nested series evaluation at the final coefficient loop. Its original
[source](checks/review_source_cont_independent.py), empty stdout,
[traceback](checks/review_source_cont_attempt01.stderr) and
[failure record](checks/review_source_cont_attempt01_failure.json) are kept.
Attempt 02 computes the SAME Taylor coefficients using mixed derivatives at
zero and replaces a documentary literal-True history placeholder by actual
domain-overlap and derivative checks. No partial first execution is reported
as a completed check. A separate report-generation quoting error made no
file change and is recorded as an editing failure, not a scientific result.
The first link-validation regex also mistook indented mathematical notation
for a link; its assertion and narrow parser correction are preserved.

Both complete author scripts and original outputs were read. The coordinator's
immutable 44+5 replay was reused, and I independently compared JSON excluding
only recorded/elapsed time. The [reuse record](checks/review_source_cont_reuse.json)
binds exact output hashes. No unchanged successful baseline was re-executed
for bookkeeping. Eight [saved-copy mutations](checks/review_source_cont_author_mutations.json)
all exited 1 at intended assertions: source force, bulk normalization, remote
insertion, Jacobian, orientation, main action, sphere radius and scalar ball
dimension. Every mutant and failure output is retained. These are finite
formula diagnostics, not a computation of the full nonabelian Hessian or an
infinite-volume/continuum proof. No interval or Lean certificate is claimed.

## Coverage and retained limits

The complete 856-line original target was read, recovering the truncated
middle in lines 310–620. Both complete subsequent diffs were read: the history
qualification and dependency links. Final coverage is reconstructed from the
complete original plus reviewed changes. Both author scripts (340 and 55
lines), original outputs and receipt were read after the prestate.

| Dependency | New direct coverage | Consumed content |
|---|---|---|
| SOURCE_LOCAL_RETURN_ASTRA.md | 62–578; 580–802 (579 blank) | Source norms, tree-Haar identity, actual action, critical branch and Hessian/inverse/square-root/logdet; same-B contour |
| REVIEW_SOURCE_LOCAL_RETURN_ASTRA.md | Complete 1–551 | Exact final repairs and bounded dependency scope |
| RECOVERY_CLUSTER_ASTRA.md | 1–433 | Complete relevant definitions, composition, both CX-R stages, analytic exponential identity, full-factor implication; later example/ledger not newly re-reviewed |
| REVIEW_RECOVERY_CLUSTER_ASTRA.md | Complete 1–180 | Corrected beta≥0 and generic theorem scope |
| STEP55.md | 241–390; 419–545; 656–697 | Normalized action, polar/normalizer domains, scalar-dimension correction, actual cutoff and return limits |
| CODEX_REVIEW_STEP.md | 180–215 | Full-return normalization and unchanged domain/matching limits |

Twelve predecessor-review ranges in PROOF, SRC2, B2 and their reviews were
mechanically compared with current source: each old range hash matches and
its exact bytes remain present. That prior review is reused only at its
recorded scope; these are not new direct or full-file reads. The predecessor
supplies its reviewed level-zero critical branch and atoms, not a whole-proof
PASS. The [coverage manifest](checks/review_source_cont_coverage.json) distinguishes direct reads, partial ranges,
verified prior-review reuse and documentary receipts.

Current-main AGENTS, SCIENCE_WORKFLOW, review-loop entry and its installed
difference, freshness, setup/units/lenses/fixes/audit compatibility,
claim-status, proof-search governance, minimal axioms, primitive-registry
check/JSON and no-go applicability were read. No physical primitive or
empirical value is used to replace a mathematical hypothesis. Current-main
front-door/backlog/landing administration is coordinator scope, not a new
review of those surfaces by this source-only reviewer.

The source honestly retains the interfaces for general hard histories,
actual reference normalizers and nonlinear/collar matching, arbitrary coarse
fields/holonomies, cut-failure/outside-chart complements, higher-level
exact-action/source-norm induction, and E_cb/E_NA matching. No pairwise
independence, route-exhaustion, new-axiom need or impossibility theorem is
asserted. No five-route no-go packet PASS is claimed. The scalar history
counterexample tests only the overbroad analytic inference repaired above.

## Review lenses and operational disposition

- Code / Runner: finite checks and eight targeted failing mutations confirmed;
  one preserved/recovered reviewer execution interruption.
- Physics Claim Boundary: bounded support on the stated domain. Full existence
  and physical mass gap remain open.
- Proof Obligations: CLOSED for the corrected selected-sector implication;
  CONDITIONAL on the reviewed branch/atom inputs and explicit smallness/domain
  hypotheses. No target-equivalent lemma is relabelled as near physical closure.
- Imports / Support: disclosed model/domain inputs N,L,kappa, large real u,
  chart/forest, fixed sector and product reference. No fit, observation, new
  axiom or physical mass identification.
- Nature Retention: no Nature-readiness or audit-derived retained status.
- Labeling Convention: substantive analytic/algebraic implication, not naming.
  No-Go Discipline: no broad negative theorem asserted.
- Governance / Audit Compatibility: the narrow dependency-link repair is
  confirmed; no audit authority is written. Whole-PR source preservation,
  canonical discovery, current-main loss, combined pipeline/strict lint/evidence
  readiness and landing remain coordinator gates.

One original review and two affected-fix confirmations were completed. One
scientific scope finding and one source-link finding were repaired; zero
remaining mathematical findings in this bounded unit. Reviewer source edits,
commits, pushes, PR actions, audit-authority writes, worker launches and full
pipeline runs: zero. No canonical claim ID or audit verdict is assigned.
The recommendation above confirms only the final source; it does not claim
that whole-PR combined or landing gates have completed.
