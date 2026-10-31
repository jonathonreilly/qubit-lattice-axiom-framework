# Independent hostile review of RD pass 2

**HOLD for Theorem RD as consumed.** The finite effective-density identities
and the new hard-cut/L¹ lemma are correct at their stated scope. They do not
establish the common zero-free domain, uniform activity/reference estimates,
or the effective-level induction required by the consumers. No material
algebraic defect was found in those scoped results; the binding work below
is missing science, not a request to erase the partial results.

B1 alone: RESOLVED.

Here B1 means the author brief's exact finite-construction deliverable:
specify a legal history partition for the actual Decision-4 step and prove
a complete representation. It does **not** mean that the representation is
already the Gaussian (ID) in RECOVERY_CLUSTER_ASTRA, or that the specified
H12 history equals a legacy sigma-history. Literal consumer matching remains
part of B3. These distinctions are necessary when carrying this verdict
downstream.

| Item | Verdict | Evidence and remaining fix |
|---|---|---|
| B1 — actual object and complete identity | **RESOLVED** at the specified finite-history scope | `RD.md:249–486,551–579` constructs the actual chain, the explicit history partition, the local/joint quotient, and a finite connected identity. Inherited factors, failures and complementary sectors are retained. No correction is required to these identities. Preserve the history and normalization qualifications at `:304–309,348–369,410–429`; do not promote this verdict to the consumer's Gaussian (ID). |
| B2 — quantitative and analytic inputs on that identity | **PARTIAL** | `RD.md:497–549` proves finite-fibre reference bounds, source/terminal-coarse holomorphy and a nonuniform zero-free germ. `:822–891` correctly proves an integrated hard-event criterion. No actual-model uniform bound for that criterion, the history mass, or all local prefactors is supplied. Complete the sub-lemmas at `:993–1004` on one matching reference/domain. |
| B3 — consumer, reference and induction closure | **PARTIAL** | The full history sum and algebraic recursion are explicit at `RD.md:313–323,391–420`; `:893–926,968–991` preserves inactive terms and all displayed prefactors. The comparison after integration/summation, unrestricted-hole full norm, quantitative induction, legacy-history identification and complete Gaussian consumer match remain open. Complete `:1006–1016`, not merely the finite recursion. |

Reviewer: user-assigned Codex in a fresh context, 2026-10-29. I authored none
of the candidate science. This is same-family review, not cross-family or
blind review: the required RD_LOG reading exposes earlier verdicts. Those
verdicts were not used as proof. I did not open the separate
`checks/rd2_review.md` report or delegate this review.

**Source binding and recovery.** The reviewed checkout HEAD is
`295b508bea2c65bf548172f3190e32f7f7eaf6cf`; RD has 1,037 lines and RD_LOG
344. I read both completely and the complete 670-line
`git diff HEAD -- RD.md`. Line references below refer to the frozen working
files, not HEAD's earlier RD. HEAD remains the recovery source for the
pre-pass-2 text.

| File relative to the working folder | SHA-256 |
|---|---|
| `RD.md` | `a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5` |
| `RD_LOG.md` | `2099d4512e66add04684efcd8028a99d15979db283ac236f090f21978b9570df` |
| `briefs_rd/AUTHOR_BRIEF_RD2.md` | `140dd200e994033454b38bfd2599116e2705264ee1264dfdd46f3a8ca35621a5` |
| `briefs_rd/REVIEW_BRIEF_RD2.md` | `fbb5b078f9a79f1769aa83b4d7d9abebc7cbd16370c6aa8367562f0e510321dd` |
| `REVIEW_RD.md` | `59154a352ac9f1b2e201606ab6e2d4c4e5b5624f446fed1f28ce08ab2787101e` |
| `RECOVERY_CLUSTER_ASTRA.md` | `9c9264bd4d92b60798e48ccd2eb0ff230e221c3ffd2107c0f6443ec86de563cf` |
| `CODEX_REVIEW_STEP.md` | `32bab8cbc920447280b3da93a1754bf792509a115bbf8cfffc7101350fe64a0d` |
| `STEP55.md` | `aa785cf1ba03a53e79b52e8b9eb677927d18abb26178c4c018c3c37e7e1af0ce` |
| `LIB1.md` | `1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1` |
| `LARGE55.md` | `79bc36d60687376716aa425ad3c271b681ca9549f5d217693e2736b805cdf0e7` |
| `RLARGE.md` | `4f3d2777bcd736ad6936946f6c072ebebd8fe2638839538ea0db28825f2438d2` |
| `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md` | `d2e9c49eedceb14b654f5be640e2b55efc16b902fd789acbc3d73c2849b9a850` |
| `SOURCE_LOCAL_RETURN_ASTRA.md` | `2eee991e4e4546aa3ed10ad0ffe40d840c5347a002d623aac47b2fc515fd7769` |
| `SOURCE_LOCAL_RETURN_CONTINUATION_ASTRA.md` | `ac985bb9b41a0d9d52ead7c2932df73e59c713c28c5c45f0629003552eee1243` |
| `PROOF.md` | `ad6611c0100c6163015903e233137b51e6dbac70acbe258bca95732f5180c9a9` |
| `HANDOFF.md` | `61af84850caaf3f2ec04808cb9d0924b2879dd7c79d430e8e1507cf53770eb08` |
| `PROCESS_LIGHT.md` | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| `REVIEW_LIB1_R2.md` | `c917e2a9c00a6e9f46aba74461b4c52172a7221eb74776426ef7564ab45c311b` |

The applicable SCIENCE_WORKFLOW, repository physics-claim-reviewer skill,
skill-freshness instructions and proof-search governance match local
`origin/main=01589af3faf806b736c42dc2f3bd625e9edead9f`. The repository
reviewer skill controls its minor wording differences from the installed
copy. The planning fetch returned success; the attempted main fetch failed
at the shared FETCH_HEAD with “Operation not permitted.” Therefore this is
a review of the identified local source, not a claim of freshly fetched
remote-main science or audit provenance. Planning supplied no proof input.
The user's single-report/no-commit scope controls the work.

**B1 reconstruction: the operation, not just its successful factor.**

1. **Density and histories, R1–R4 (`RD.md:251–323`).** R1 is precisely
   the normalized-kernel recursion in `LARGE55.md:61–66`, with sources
   inserted only in the original Wilson action. Substitution of each
   earlier integral gives the product of all kernels exactly once.
   For a fixed pair of real fields, the strict chi cuts select one B in
   R3; the zero/one completion and size tests then select one failure
   list F. Summing F is one, including cut-boundary conventions.
   Inductively summing the finite decision tree gives sum_h Xi_h=1.
   Fubini therefore proves both R4's recursion and sum_h rho_(k,h)=rho_k.
   As a normalization cross-check, integrating the next coarse field
   after summing F recovers the preceding total mass because each K_k
   integrates to one. No partition function or history mass disappears.

   The H11 completion minimum exists on compact SU(N) interior variables
   and is continuous in the real frozen data; its indicator is measurable
   (`SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:266–299`). The masks in R2
   depend on recorded failures. All hole fields remain in the chain, so
   this is an exact partition even without a theorem permitting their
   later integration to one. It does not prove LARGE55 (R_m)(a)–(c).

2. **Conditional denominator and inherited density, R5–R6
   (`RD.md:327–369`).** The factor b_k is nowhere zero and
   b_k J_(k,h)=rho_(k,h) identically. Thus using b_k is bookkeeping,
   not a Wilson approximation at higher levels. Every current plaquette
   or kernel reading I(B) is included in w_(k,B); the remaining O is
   independent of those integration variables. The two conditional
   integrals are exactly O N and O D, giving N/D where D is nonzero.
   At k=0 this recovers `RLARGE.md:850–855` without an unspecified
   proportionality constant.

   The actual contour paths stay inside their two endpoint blocks:
   their axial legs stay in their respective blocks and the straight leg
   runs between them (`PROOF.md:1254–1264,1313–1324`). This verifies the
   reader allocation and G2 separation used here. Inherited J may read
   the entire exterior, which is why freezing only the bare collar would
   be wrong. R6 correctly freezes all eta and leaves earlier fields in
   their original joint integral.

   A direct diagnostic explains why the joint insertion is essential.
   For two interiors having good/bad states, let an inherited positive
   weight have entries J_GG=a, J_BG=b, J_GB=c, J_BB=d. After removing
   the bare bad/good mass ratios, the true joint ratio is d/a, whereas
   multiplying individual ratios evaluated at the good sea gives bc/a².
   They agree only if ad=bc. R6/R7 retain d; a product replacement would
   silently impose this rank-one condition. This is a written algebraic
   diagnostic, not a claimed SU(N) counterexample.

3. **Full replacement, R7–R9 (`RD.md:373–429`).** Fix B and its
   G2-components. Their bare reader factors and interior coordinates are
   disjoint. The decisive equality at fixed exterior data is

       integral chi_B w_B^0 (R_B L) = integral zeta_B w_B^0 L.

   Indeed R_B L no longer depends on the old good-interior coordinates.
   Their integral is exactly product_Y C_(k,Y), which cancels precisely
   R7's denominator. Multiplying by the untouched exterior weight and
   chi_(A minus B), then summing B, proves R8. A current selector is
   evaluated on the replacement fields, inside L; a lower-level selector
   stays in its lower-level integral. This retains joint histories and
   every failure instead of multiplying them by their sea-sample values.
   The identity works for complex sources by compact-domain domination,
   without taking a logarithm.

   R7 divides only by a positive bare cut integral. It never equates this
   reference with the inherited D. The extra D/product C in
   `RD.md:413–418` is indispensable for recovering STEP55's original
   quotient. R9 is a different reference, usable only on positive fibres.
   Zero-mass histories remain zero summands and are not normalized by zero.

4. **Connected identity, R10–R11 (`RD.md:433–495`).** Substituting R4
   into R6 cancels the artificial b_k and yields
   O D=E_mu[chi_B Xi_h rho_0 product_(j<=k) K_j]. All earlier
   normalizers and all original source coordinates remain. Product Haar
   really is a product after grouping free coordinates by owner; adding
   external readers and connector vertices to supports only coarsens
   the overlap graph.

   To check the finite gas without assuming a cluster theorem, attach
   independent formal markers t_i to each F_i−1. The coefficient of
   product_(i in A) t_i in the original integral is E product_(i in A)b_i.
   A selected label set A has a unique partition into overlap-connected
   components. Their free-coordinate sets are disjoint, so their integrals
   multiply. The hard-core gas in R11 has exactly that same coefficient.
   This proves all coefficients, including multiplicities and signs;
   no analytic continuation or smallness is needed. A label reaching
   zero causes exact cancellations in this finite identity, not a
   contradiction or an automatic nonzero result. Empty integrations and
   the empty gas are covered by the stated scalar convention.

   Keeping an entire history test as one possibly global atom is legitimate
   for this identity. It gives no estimate paying that atom's full support.

5. **All chart and contour sectors, R14 and (13)–(16)
   (`RD.md:551–659`).** If P_l is the product of the first l test
   indicators, then q_l=P_(l−1)−P_l and q_0=P_m. Telescoping proves
   q_0+sum_l q_l=1, so simultaneous failures are counted once. The Haar
   identity integrates every sector and makes no contour deformation.

   On a permissible forest, successive Haar translations have unit
   Jacobian and normalized gauge volume. Any noninvariant inherited
   insertion remains in the tree average. The differential of the
   exponential is the integral of exp(−s ad_a), giving the displayed
   Haar determinant j. With a=sigma Q^(−1/2)W, the real Jacobian is
   sigma^d det(Q)^(−1/2); conversion to normalized Gaussian measure gives
   the factor (2 pi)^(d/2). Thus (14) has precisely
   Z_ref^−1 c_N^n (2 pi sigma²)^(d/2), exp(−S_0),
   det(Q)^(−1/2), N_chi and the retained expectation.
   The sign of −log j in U and the retained linear term are correct.
   Moving an inherited factor into S_eff requires removing it from the
   insertion, as the revised text now says.

   An optional E_side=D_0−D_0^new is exact bookkeeping, not a proved
   contour deformation for an arbitrary hard history. Leaving it unevaluated
   is legitimate for the undeformed finite identity. It does not establish
   the adapted Gaussian identity or its estimates. No complementary term
   has been proved negligible.

**B2 reconstruction: which bounds exist, and which do not.**

The elementary bounds in `RD.md:101–177` are valid at bare scope.
The entry-grid cap cover has at most M_N(delta) cells and gives Haar cap
mass at least its reciprocal. Four-link telescoping places the cap product
inside every interior cut. There are 4 L³(L−1) interior links per block,
at most six affected plaquettes per link, and at most eight incident coarse
kernels. Since 0<=s<=2 and exp(−2t)<=k_t<=exp(2t), multiplying these
bounds gives (3), including its 16 kappa u coefficient. Centering s at 1
gives the half-plane estimate (7) on the stated l¹ source domain. Its
guaranteed product radius still shrinks with u|Y|.

For the new effective-level reference (`RD.md:499–516`), the integrand
chi_B Xi_h is zero or one. All remaining real chain factors are strictly
positive and bounded between exp(−2u_0 P_0−2T_k) and exp(2T_k).
Integrating and dividing by the explicit positive O gives R12.
Consequently D(0)>0 if and only if gamma>0. This correctly diagnoses
zero fibres; it supplies no uniform lower bound for gamma. It also retains
global volume/depth costs, rather than proving a local prefactor budget.

The holomorphy claim at `RD.md:518–549` has the right variable restriction.
The original-source dependence is entire. For the new terminal V,
tr(V^−1 M)+tr(M* V) is holomorphic on SL(N,C); M* is fixed relative
to V, and the kernel normalizer still has real M as its argument.
Xi_h has no dependence on this new V. Compact domination therefore
justifies integration. It would not justify continuation of eta, or of
the new selected output through I_(k,F|h)(U_k,V).

In R13, the original-source contribution to |H| is at most
2u_0 sum|epsilon_p|. Each terminal link contributes at most
t_k(exp(||Z_c||)−1), by bounding both trace differences by
N(exp(||Z_c||)−1). The positive-reference expectation then satisfies
Re E exp H >= exp(−r) cos r for r<pi/2. Dividing by the nonzero O ratio
is valid. This proves the germ actually stated, not a volume-independent
product disc or the full consumer's complex boundary domain.

**The hard-cut repair is proved, but conditional.**
At `RD.md:824–848`, inclusion-exclusion followed by the unique
overlap-component partition proves R15 pointwise. For a path of three
labels with S_1 disjoint from S_3 and S_2 meeting both, the result is

    1 − e_1 − e_2 − e_3 + e_1 e_2 + e_2 e_3
      + e_1 e_3 − e_1 e_2 e_3,       e_i=1_(E_i).

Here the e_1 e_3 term is a compatible pair of singleton types; the other
two pair terms and the triple term are connected types. This checks both
simultaneous failures and the absence of a fictitious independent-overlap
term. If two overlapping requirements fail on the same event E of
probability p, their joint failure mass is p, not p²: inclusion-exclusion
gives 1−p, as the exact product of the two identical requirements demands.

R17 (`RD.md:865–881`) takes suprema of interaction factors first.
The surviving defect supports are disjoint, so product measure then
factorizes their absolute integrals. Hence the correct majorant is
product ||f_i||_infinity times product delta_a even when interactions
overlap defects. Compatibility may be dropped only after this bound.
This ordering is present in the proof and repairs the previous erroneous
inference from a tail probability to ||Theta−1||_infinity.

The two tree bounds also have the right weights. With
v_i=exp((mu_0+1)|S_i|) times the corresponding sup or L¹ size,
v_i exp(|S_i|) is a supersolution because the child sum is at most
q_1|S_i|. Marking an atom through a fixed vertex bounds the first gas at
rate mu_0+1 by q_1. The connected-graph logarithm then spends the second
unit of support weight and gives the rate-mu_0 bound. Marking the root
changes 1/n! to 1/(n−1)!; repeated polymer labels are required in the
logarithm. The ordered-edge tree partition used in the note gives the
correct absolute graph bound. Scaling all atoms by t leaves a margin
through |t|<=2 when q_1<=1/4, so continuation from the formal identity
near zero is justified.

A separate check of the zero-free consequence uses vertex deletion.
For the first gas restricted to A,

    Z_A = Z_(A minus {v})
          + sum_(P subset A, v in P) w(P) Z_(A minus P).

Inductively smaller one-vertex ratios have modulus at least 1−q_1.
Deleting the remaining |P|−1 vertices bounds the quotient in the sum by
(1−q_1)^−(|P|−1) <= exp(|P|). The proved first-gas rooted bound
then gives |Z_A/Z_(A minus {v})−1|<=q_1<1. This confirms conditional
nonvanishing without using the logarithmic identity as its own premise.
It establishes no actual-model smallness.

Actual application is still missing at `RD.md:883–891,993–1004`.
The direct Haar U estimate (17b) grows with u; it does not certify a small
q_1. The needed delta_C are joint-event masses with all label
multiplicities under the chosen product reference. An interacting-law tail
bound, or separate marginal failure probabilities, is not that input.
A rare required history can have a very common complementary event.
Complex contour sides need total-variation/reference estimates, not an
indicator-event interpretation. These are substantive B2 obligations.

**B3 reconstruction: the unchanged consumer gap.**

At `RD.md:790–811`, matching product measures and unchanged atoms away
from A imply coefficient cancellation for supports missing A. Summing the
two rooted bounds over A costs at most 2q|A|; source subtraction gives
2p_*+2q in (22). Those are valid pointwise statements. They do not cancel
the history-dependent Z_(k,A)^cut,0, compare different sea measures, or
commute a logarithm with R8's expectation and history sum. Even an
expectation of local exponentials can produce mixed coefficients equal
to correlations of its underlying nonproduct law. The required comparison
after integration remains absent.

The LIB1 use at `RD.md:893–926` matches its actual statement and proof
(`LIB1.md:68–126,216–273,357–438`). The identity
R_Lambda(X) intersect Lambda = X intersect Lambda proves contraction of
the active-root/active-size norm. At most 8|X| hole components can enlarge
X. If each has at most M>=1 vertices, this gives
|R_Lambda(X)|<=(1+8M)|X|; an inactive output root has at most 9M possible
input-root witnesses in its hole's closed neighborhood. Thus (25) and
the extra inactive-family cost are correct. The identity/no-active-site
endpoints are retained. Nothing here supplies bounded M for the histories
being constructed, or a compatible alternative full-norm estimate. Keeping
unsaturated labels avoids a false conversion but does not by itself prove
the consumer's missing bound.

The literal prefactor comparison is:

| Operation/factor | Exact present accounting | Missing consumer conclusion |
|---|---|---|
| Frozen exterior | Full conditional denominator is O D; R10 divides by O exactly once | Local bounds/cancellations for the convention actually used downstream |
| Inherited density and history | All earlier kernels and Xi_h in the lifted Haar integral; alternatively J inside the chart insertion | Match the chosen consumer history and its domain, without double counting |
| Gauge/Haar/Gaussian | Unit permitted tree-gauge volume, c_N^n, (2 pi sigma²)^(d/2), det(Q)^(−1/2) | Uniform local decompositions on the same original-source domain |
| Exact action | exp(−S_0); linear and quadratic-mismatch terms retained in U | Main-term/determinant variation bounds separate from nonlinear smallness |
| Cut and complement | N_chi times the retained selected insertion; all outside sectors and oriented sides added | A controlled local logarithm for the full sum, not just the selected term |
| Reference | D(0,eta,Vbar) only on gamma>0; bare C and Z_cut kept distinct | Stable admissible fibres and reference comparison through R8 |

In particular `RD.md:981–991` gives r=N/(A Z_sel+E), not
N/(A Z_sel). On a domain where the factors and branches exist,

    log D = log A + log Z_sel + Log(1+E/(A Z_sel)).

The last logarithm is not constructed or bounded locally. The full
Gaussian (ID) assumed at `RECOVERY_CLUSTER_ASTRA.md:344–357` is therefore
**not yet instantiated** by the finite Haar gas. Its (FULL)/(VAR) at
`:366–393` still needs the separate prefactor norms. This is consistent
with `CODEX_REVIEW_STEP.md:194–214,318`: for Q(z)=1+z and zero reduced
interaction the determinant alone contributes −Log(1+z)/2. RD correctly
retains this term and does not repeat the refuted O(|Y| H_V) full bound.

Likewise `STEP55.md:472–481,530–542,683–685` concerns a particular
white-cut/single-background quotient and a common complex boundary domain.
R1–R14 identify a complete integration target; they neither supply that
representation nor show that an alternative representation satisfies all
its norm and numerator requirements. The explicit H12 iteration is an
honest exact history convention, not a proved equality to legacy sigma^J.
The algebraic recursion closes at every finite depth; the quantitative
hypotheses required for the next level do not.

**Active inputs and hidden imports.** FR, KR and TC at
`RD.md:937–946` are named requested interfaces, not accepted conclusions.
Their stronger all-history/reference/domain requirements are not supplied
merely by HANDOFF's completed scoped reviews or active selected-core and
graded-complement assignments (`HANDOFF.md:280–344`). No such result is
silently used in R1–R17.

LIB1 is explicitly authorized by the brief, and its current bytes match
`REVIEW_LIB1_R2.md:20–27`. I reconstructed the norm interface actually
used; I did not recertify its numerical suite or assert new main/audit
provenance. The predecessor successful-gas statement is consumed only
with its H20–H24 hypotheses and does not control the final sea expectation
(`SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:528–620`). No physical axiom,
fitted value, unproved action ansatz or load-bearing literature theorem
was found hidden in the finite construction or conditional mixed proof.

The official abstracts confirm the stated scalar, three-dimensional scope
of Dimock's [Part I](https://arxiv.org/abs/1108.1335),
[Part II](https://arxiv.org/abs/1212.5562) and
[Part III](https://arxiv.org/abs/1304.0705). This is attribution checking
only; none of those papers was imported to discharge an SU(N) proof step.

**Binding fixes before LAND for the requested theorem.**

1. **Complete B2 on the actual integral.** Establish a useful positive-fibre
   history/collar class stable under the operation, quantitative reference
   bounds, a common original-source and required coarse-field domain, local
   prefactor/interaction budgets, and connected joint-failure and contour
   bounds under the same reference. Prove the inequalities and multiplicities
   in R16, or a complete alternative criterion. The finite germ and the
   existence of the finite gas are not these estimates
   (`RD.md:497–549,883–891,993–1004`).
2. **Complete the integrated comparison and full norm in B3.** Carry the
   comparison through R8 with its actual measures, history-dependent
   references and all inactive terms. Supply (25)'s geometry/rate hypotheses
   for the constructed histories or prove a matching full-norm alternative
   (`RD.md:803–811,893–926,1006–1012`).
3. **Complete induction and literal consumer matching.** Identify the history
   convention used by the consumer, prove its output satisfies the next
   level's analytic/reference/norm hypotheses, and identify the complete
   quotient with the corrected CX-R representation or a fully proved
   replacement of matching strength. Include every factor in the table and
   the local contribution of E; prove the normalized numerator estimates
   where STEP55's returned-activity conclusion requires them
   (`RD.md:304–309,953–991,1012–1016`; consumer locations above).

These are overlapping obligations, not a count of independent obstructions.
No additional algebraic repair to B1 or R15–R17 is required by this review.
The open status already stated in RD must remain until this binding work
is actually done.

**Verification limits and output scope.** This report records written
proof reconstruction, direct coefficient/normalization diagnostics, the
separate vertex-deletion nonvanishing check, source comparison and
deterministic hashing. No numerical physics experiment, symbolic-enumeration
runner, Lean build, integration pipeline or audit was run. Therefore no
numerical criteria file or lock was needed. Earlier runner/review results
were not treated as new checks of this theorem.

Necessary source coverage includes the complete RD/RD_LOG and RD diff;
both pass-2 briefs and PROCESS_LIGHT; REVIEW_RD's B1–B3 and relevant
supporting discussion; the named consumers; the exact density, bare
quotient and H1–H14/H21–H25 producers; S4-prime path locality; the
tree/Haar/chart and continuation interfaces; and LIB1's consumed geometry
and norm proof. Large retrievals that truncated were not accepted as
complete reads; the needed passages were retrieved in smaller ranges.
This is not a whole-repository review or a proof of uniform RG closure.

Only `REVIEW_RD_R2.md` is written. No author source, consumer, check,
editable prompt, audit or ledger file is edited, and no commit is made.
The final inventory comparison found all 3,304 pre-existing working-folder
files byte-identical, no deletions, and this report as the sole addition.

VERDICT: HOLD
