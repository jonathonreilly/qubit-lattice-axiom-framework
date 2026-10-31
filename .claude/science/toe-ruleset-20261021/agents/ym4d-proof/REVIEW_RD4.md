# Independent hostile review of RD4

**HOLD for the uniform B2/B3 normalized RG step.** Neither requested route
establishes its actual-model inputs or next-step closure. The exact
factorizations, conditional expansion, reference-price accounting and
representation-specific diagnostics are valid partial support. There is
one minor correction to the prospective invariance template, identified
below; it is not the reason the actual uniform theorem remains open.

This disposition concerns the target in `briefs_q/RD4/AUTHOR.md:1–20` and
`REVIEW_RD3.md:287–328`. The existing `checks/rd4_review.md:3–17,332–337`
uses LAND for the partial note and expressly holds theorem completion.
That narrower approval does not discharge B2/B3. No GO or NO-GO for the
uniform RG construction follows, and no audit or retained status is granted.

Reviewer: user-assigned Codex in a fresh context, not an author of RD4.
This is **same-family review, Codex reviewing Codex**, not cross-family or
blind corroboration. The log and predecessor reviews exposed prior
dispositions. I reconstructed the arguments from the definitions and
source passages; approvals and validator success were not mathematical
premises. No subreviewer was delegated.

All RD4 line numbers refer to the complete 741-line source with SHA-256
`60d27c7ec5e5fda254e8394c34639cccdfe42cd9f85898bb22952bc6fa6067c6`.

**F1 — minor correction: make the contraction range explicit.**
At `RD4.md:594–599`, I2 gives `lambda<1` and
`B_generated <= (1-lambda) h_*`. Those written conditions alone do not
preserve the ball of radius `h_*`. For `h_*>0`, take `lambda=-1`,
`B_generated=2h_*`, and a scalar map `T(x)=2h_*-|x|` on `|x|<=h_*`.
Then `|T(x)| = lambda |x| + B_generated` throughout the proposed input
class, yet `T(0)=2h_*` leaves it. This is an exact counterexample to
using the displayed inequalities alone as an invariant-budget criterion,
not a Yang–Mills counterexample. I2 is explicitly unproved, so this does
not refute a claimed established recurrence.

**Fix:** state `0<=lambda<1` (and nonnegative norm/error budgets). Then
`a<=h_*` implies `lambda*a+B_generated<=h_*`. Alternatively use the
stronger budget `B_generated<=h_*-max(lambda,0)*h_*` if allowing negative
lambda. The conventional contraction interpretation should be made
explicit before I2 is consumed.

**Requested items: verdicts and fixes.** “OPEN” means an unmet scientific
obligation, not a demonstrated obstruction. Locations are in RD4.

| Item | Route C verdict | Route L verdict | Binding completion work |
|---|---|---|---|
| B2a — uniform common domain | **OPEN**, `:63–69,179–194,211–229,317–327,643`. C7 assumes a common domain, holomorphic cells and nonzero cell masses. C11 disproves obtaining such a radius from arbitrary conditioning alone. | **OPEN**, `:352–387,409–422,643`. L5 is a raw numerator envelope, not a zero-free denominator or analytic continuation of new hard selectors. | Establish a stable admissible history/chart class and the same original-source and required coarse-field domain for the actual selected integrals. |
| B2b — reference, interaction and failure budgets | **PARTIAL; actual input OPEN**, `:133–163,220–229,280–332,644`. C3a/C3b give a mandatory Haar mass. C6 is unverified; the stated direct Wilson-atom test fails in C10's coupling range. | **PARTIAL; actual input OPEN**, `:373–460,492–519,644`. The integrated price ledger is valid conditionally. No actual matched joint expansion or constants satisfying L7 are supplied. | Prove full prefactor, residual-interaction, joint-event, total-variation and multiplicity bounds under the very reference used. An adapted reference remains possible. |
| B3a — local comparison after full integration, including K | **OPEN**, `:265–276,523–574,645`. C9/K1 apply only after the specified complete integrations. Actual budgets for R_h and its different Z_A are missing. | **OPEN**, `:361–387,449–460,502–519,645`. L4 controls a scalar integrated relative weight; it does not construct local connected logarithms. | Construct the integrated original-source coefficients for the actual R8 comparison, and separately the terminal reference-weighted comparison, with the K budget needed by K2/K3. |
| B3b — output closure and literal STEP55/CX-R match | **OPEN**, `:576–637,646`. The next effective interaction and invariant radii/rates are unestimated. Conditional cells are not automatically the consumer's white-cut reference. | **OPEN**, `:464–500,576–637,646`. Reserved prices, small failed components, boundary readers and history gluing still need induction estimates. | Correct F1; prove output-to-input estimates, growing-hole control, normalized numerator bounds, and the actual history/chart/Hessian/reference match. |

**Per-result mathematical dispositions.**

| Result and RD4 lines | Verdict | Fix or restriction |
|---|---|---|
| Actual integral and normalization, `:27–53` | **CONFIRMED** against RD R4–R10 and RD3 D4/D8/RC1–RC3. | No algebraic fix. Keep local D_h, fully integrated R_h, history mass A_h and all-cut Z_A distinct. |
| C1–C4, including C3a/C3b, `:79–185` | **CONFIRMED** at the stated history and reference scope. | No fix. The Haar mandatory mass is not the weighted whole-history mass or D_h(0). |
| C5–C9, `:187–276` | **CONFIRMED conditional theorem** with the displayed locality, fixed-predicate, holomorphy, envelope and smallness hypotheses. | No new proof repair. Actual-model verification of these hypotheses is B2a/B2b/B3a. |
| C10/C11, `:280–315` | **CONFIRMED scoped diagnostics**. | No fix. C10 excludes satisfying C6 with the specified separate atoms in its stated range; C11 concerns a sign law, not Wilson/Decision-4 zeros. |
| Adapted reference, `:317–332` | **ARGUED**, accurately labelled. | Supply the conditional law and full-reader interaction estimates; replacing it by the exact interacting law does not estimate its cumulants. |
| L1–L4 and boundary cancellation, `:336–397` | **CONFIRMED identity/conditional bounds**. | No fix. Equality of the references and the TV ratio are substantive premises. |
| L5–L8 and gluing, `:399–460` | **CONFIRMED conditional accounting**. | Exact joint factorization and the mixed majorant remain required; scalar prices do not prove them. |
| L9, raw-cone scope and L10, `:464–519` | **CONFIRMED** at their stated scopes. | No algebraic fix. Spend the final exponent once; retain cone readers. L10 is a bad upper majorant, not a lower-bound obstruction. |
| K1–K3, `:523–574` | **CONFIRMED conditional norm transfer**. | No geometric fix. Supply the actual K input and a uniform growing-hole mechanism or a matched alternative norm. K3 is only sufficient. |
| I1–I4 and consumer dictionary, `:576–637` | **CONFIRMED accounting; OPEN closure**, with **F1** on the proposed I2 template. | Correct lambda's range; establish the missing quantitative and identification inputs. |
| Status, interfaces and negative scope, `:639–741` | **CONFIRMED as partial/open**, not completion. | Preserve the qualifications. There is no independent-wall count, exhausted-route certificate or physical no-go. |

**Reconstruction and discriminating checks.**

1. **Actual history and mandatory mass.** Substituting RD R4 into R6
   cancels the bookkeeping density b_k, leaving exactly (4.1), including
   O_h inverse and every kernel normalizer. For a fixed prefix, Y is a
   maximal bad G2-component precisely when all its blocks are bad and
   its active G2 exterior neighbours are good. Multiplication by `1-a_j(Y)`
   selects failing components. Thus the list of b-values identifies the
   entire failing list, and C2 enforces equality to F_j, including absence
   of additional failures. Successful singleton components have b=0 and
   are not erroneously excluded. Empty lists and incompatible records
   obey the same pointwise identity (`RD.md:264–323`).

   Conditioning gives `int E A F dnu = p int A F dnu_E` by substitution,
   without an independence premise. Cell factorization enters only after
   every mandatory reader is contained in one disjoint cell. For Y0 the
   size test already fails, so it has no surviving completion dependence.
   Independently counting its neighbourhood by inclusion-exclusion gives
   `2*5^4 - 4*5^3 = 750`, hence 748 shell blocks. The interior-link cuts
   are independent under product Haar (`RD.md:72–88`); consequently
   `p_h=(1-c)^2*c^748`.

   Each block has `4(L-1)L^3` internal links. The identity cap makes
   plaquettes closer than `4delta=1/4` to identity; a marked-link cap
   preserves a plaquette distance greater than `2-1/4>1`. The entry-grid
   cover of SU(N) gives mass at least m_delta per link, so both c and
   1-c are at least `m_delta^n_I`. Multiplication proves C3b. A radius-two
   old-block displacement crosses at most one containing-block boundary
   for L>=3, placing the mandatory readers inside H1. These computations
   use the actual cuts and witness in `RD3.md:25–90`; they do not estimate
   the action-weighted avoidance integral remaining in C3.

2. **Complex measures and the connected logarithm.** Integrate unvisited
   normalized cells before taking absolute values. For visited cells,
   remove interaction factors by their suprema. Compatible defect types
   occupy disjoint whole cells, so their absolute integrals multiply.
   Any visited cell outside those defects belongs to an interaction;
   its variation is covered by that interaction's tau(S). Repeated
   charges only enlarge the bound because each tau_C>=1. This proves
   C8 and explains why a volume-wide product of unvisited TVs is absent.

   A separate exact discriminator uses a two-point complex cell with
   weights `(1+2i)/2,(1-2i)/2` at x=+1,-1. Its mass is one and TV is
   sqrt(5), while for `f(x)=epsilon*x`, `int f=2i*epsilon`. Dropping tau
   would falsely bound `2|epsilon|` by `|epsilon|`. Adding an untouched
   cell leaves the integral unchanged. Thus both retaining visited TV
   costs and integrating unvisited cells first are necessary distinctions.

   Expand the interaction product and the inclusion-exclusion defect gas.
   A selected set has a unique overlap-component partition; different
   components involve disjoint cells and their integrals factor. Write
   alpha_i for its atom bounds and
   `v_i=exp((mu+1)|S_i|)*alpha_i`. Connected collections are bounded by
   rooted trees, allowing repeated labels only in the positive majorant.
   The tree recursion `T_i=v_i exp(sum_(j overlaps i) T_j)` is dominated by
   `v_i exp(|S_i|)`, since the child sum is at most `q_C |S_i|`.
   Root marking therefore bounds the integrated gas at rate mu+1 by q_C.
   For the logarithm, the alternating connected-graph sum is bounded by
   the spanning-tree sum: distinct edge ordering partitions subgraphs into
   Kruskal intervals, each with alternating sum zero or unit modulus.
   A second tree estimate at rate mu gives the stated q_C bound.
   The logarithmic tuples include repeated polymers and the root marking
   changes `1/n!` to `1/(n-1)!`; omitting either would change the series.
   Scaling the original atoms by t preserves convergence for |t|<=2,
   so the identity near zero extends to t=1. Fixed predicates, local
   holomorphic densities and the stated envelopes justify parameter
   integration. This checks the hypotheses as well as the formal algebra.

   As a separate finite-polynomial check, deletion of a vertex v gives
   `Z_A=Z_(A\{v})+sum_(P subset A,v in P) w(P) Z_(A\P)`.
   Inductively smaller one-vertex ratios have modulus at least 1-q_C.
   The quotient in each summand is at most
   `(1-q_C)^(-(|P|-1))<=exp(|P|)`. The first-gas bound then puts the
   new ratio within q_C of one, proving nonvanishing without assuming
   a logarithm. This supplies neither an actual-model q_C nor its locality.
   Subtracting the constructed prefactor and cluster logs at zero costs
   `2b_C+2q_C`, as in C9. The unchanged numerical constant cancels; a
   parameter-dependent unlocalized factor cannot cancel by declaration.

3. **Failed inequalities.** The displayed SU(N) matrix has trace N-4,
   hence Wilson s=4/N. On a plaquette outside the mandatory cells,
   unrestricted Haar neighbourhoods approach this value. Therefore its
   separate interaction atom has supremum at least `1-exp(-4u_0/N)`.
   Nonempty support costs at least exp(beta). Solving for this lower
   bound to exceed 1/4 gives exactly C10's threshold. This is stronger
   than a growing upper bound, but only for that representation.
   Absorbing the Wilson action into another reference changes the test.

   For the sign law, exactly two configurations survive E, each with
   conditional mass 1/2. Thus Z=cosh(sum z_i), its mixed log derivative
   is one at zero, and setting every coordinate to `i*pi/(2m)` gives a
   zero. As m grows no positive uniform product radius follows from
   positivity and mandatory-mass extraction alone. This is a precise
   non-implication under matching premises, not an actual gauge example.
   The covariance identity in `:329–332` also has the correct sign:
   differentiating `exp(-u_0 sum epsilon_p s_p)` twice gives
   `u_0^2 Cov(s_p,s_q)` in log D_h.

4. **Regional integration and prices.** Fubini yields L1 with cross-boundary
   factors retained inside the small-field integral. Given L2's actual
   nonzero denominator, triangle inequality gives
   `|W_rel|<=T_h exp(-tau*n+c_ref*n+b_partial*|Bdy_h|)`.
   Positivity makes T_h one only for a real positive reference. If two
   expansions use the same measure and identical atoms off Bdy_h,
   coefficients with supports disjoint from Bdy_h cancel. Summing the
   two rooted bounds over boundary vertices gives `2(q+b)|Bdy_h|`.
   This does not follow from geometry alone when reference laws differ.

   For L5, the holomorphic normalized kernel at `V=W exp X` has real
   exponent change `(t/N) Re tr[(cosh X-I)W^(-1)M]`. Diagonalizing the
   positive matrix `cosh X-I` bounds this by `t(cosh(alpha)-1)` when
   `||M||<=1`. Multiplying over at most c_link*n kernels and integrating
   absolute densities proves the envelope. It gives no lower denominator
   bound and cannot replace an absolute integral by a signed activity.

   A connected type of size n contributes at most
   `[A exp(beta*c_s-nu_L)]^n` after paying all displayed costs. Summing
   yields L6; `|exp(-U)-1|<=exp(||U||)||U||` gives the small-field budget.
   Allocating 1/8 to large regions is exactly `r/(1-r)<=1/8`, hence
   `r<=1/9` and L8. The separately required common-reference gluing and
   mixed majorant at `:449–460` are essential. A collection of scalar
   integrated history bounds does not supply that identity.

   Maximizing `u^d exp(-Delta*u)` gives `u=d/Delta` for d>0 and exactly
   L9's constant; for d=0 its supremum is one. Keeping a unchanged would
   leave an unbounded u^d. The scale-majorant ratio is
   `L^(4+c_B-n*a_eff*beta_-)`, so its summability requires the displayed
   strict inequality. This is a statement about that sufficient bound.
   Reader-free normalized outputs integrate to one; with an insertion f
   they instead give `int k*f`. A fixed output is not integrated at all.
   Finally RD3 RC1 gives L10 literally: its logarithmic upper majorant
   contains extensive positive terms at fixed two-block core size. It
   cannot certify L6; it does not prove that Q_h grows or that a better
   estimate is impossible.

5. **Integrated K, holes, factors and closure.** K1 subtracts two
   already integrated normalized local logarithms, giving
   `2(b+q+b_ref+q_ref)`. It cannot be inferred for R_h/Z_A from a bound
   on the different local D_h. The terminal comparison is A_h/Zbar_A
   with its reference weight retained (`RD3.md:332–382`).

   Saturation of this one hole adds at most 81 vertices. Its closed face
   neighbourhood has `3^4+8*3^3=297` vertices. Active output roots already
   occur in the input; inactive output roots can be charged to this
   neighbourhood. Root summation and the unchanged inactive family give
   `1+297 exp(81mu)`. Generally each connected input meeting the active
   set touches at most 8|X| holes, and an inactive root has at most 9M
   witnesses. With M=81 this gives rate 649mu and total constant 730.
   A singleton adjacent to H1 becomes size 82, directly detecting an
   incorrect active-size weight. The proof matches
   `LIB1.md:68–126,216–273,377–438` and `RD3.md:425–473`.

   The real chart substitution `a=sigma Q^(-1/2)W` contributes
   `sigma^d det(Q)^(-1/2)`; normalized Gaussian measure adds `(2pi)^(d/2)`.
   Together with c_N^n, the main action and white-cut mass this gives I3.
   The permitted tree gauge has unit Haar volume; its Jacobian and all
   inherited insertions remain allocated once. A nonzero linear term
   and quadratic mismatch stay in U. Complements and oriented contour
   sides add to D, so their relative logarithm needs its own local
   estimate. In Lemma O, marking a step of a closed operator walk cancels
   the trace-log's 1/n and sums to
   `q_dim*b_op/[2(1-r_op)]`, as quoted. For I4,
   `|exp(sum F)|>=exp(-q|X|)` proves the ratio bound only with the same
   reference division in N/P and all relevant supports included.
   None of these calculations establishes an extraction map or invariant
   output budgets. After F1's correction, I2 would be sufficient norm
   arithmetic; its actual estimate remains unproved.

**Sources, locators and scope.** The required B2a/B2b/B3a/B3b locator is
exactly `REVIEW_RD3.md:287–328`; RD4 has not discharged it. C1/C2 match
`RD.md:264–302`; C3a uses `RD.md:72–88` and `RD3.md:25–90`; L10 matches
`RD3.md:334–351`. The K constants match D22/D23 and the actual LIB1 map,
not an active norm. LIB1's current hash agrees with its scoped R2 review
at `REVIEW_LIB1_R2.md:20–27`; no main or audit status is inferred from that.

The literal consumer accounting matches the restrictions of corrected
CX-R at `RECOVERY_CLUSTER_ASTRA.md:89–176,231–309,342–393`, including
the separate full-factor budgets. STEP55's white-noise product cut is
at `STEP55.md:472–497`, its quotient at `:530–542`, and restored factors
at `:683–685`. `CODEX_REVIEW_STEP.md:194–214` explains why a determinant
cannot inherit an O(H_V) bound. RD4 correctly makes this prospective:
chosen Q is not identified with the slice Hessian, and neither a
history match nor a budget for the full additive complement is established.

The cited large-field restrictions also match their sources:
`RLARGE.md:385–415` is SU(2), bad-only and conditional;
`REVIEW_RLARGE_V3.md:99–142` retains the future-tilt/law gap.
`LARGE55.md:285–306,318–339` supplies the stated MIS/COL/KA scopes.
Its PRICE at `:475–486`, E13 at `:725–734`, and
`CODEX_REVIEW_LARGE.md:35–69,193–213` retain allocation, boundary,
post-normalization-price and small-failure obligations. RD4 does not
silently consume their stronger unproved interfaces.

HANDOFF's supplier descriptions at `HANDOFF.md:280–317,412–430` leave
the needed all-history extensions open. The source-sea result explicitly
concerns coarse integration and leaves fixed-V connected logs open
(`SOURCE_SEA_CONSTRUCTION_ASTRA.md:5–9,379–409`). Those unconsumed
upstream results were checked for scope, not recertified as theorems.
The primary abstracts verify the limited Balaban/Dimock attribution and
scalar d=3 scope in RD4: [Part II](https://arxiv.org/abs/1212.5562),
[Part III](https://arxiv.org/abs/1304.0705). No external theorem or
memory-only assertion supplies a missing proof step here.

The N1–N8 discussion correctly preserves two real routes, their dependence,
explicit assumptions and untested alternatives. C10 is a technique failure;
C11 is a general conditioning non-implication; L10 is only an insufficient
upper estimate. None excludes an adapted conditional/reference construction,
proves five-family exhaustion, or establishes a continuum or mass-gap result.

**Binding fixes and research work.**

1. Correct F1 at `RD4.md:594–599` before using I2 as an invariant-budget
   template. This is a small statement repair, not a closed RG estimate.
2. **B2a:** specify the stable admissible histories and prove the actual
   common source/coarse domain, including selected child predicates
   (`:47–69,179–194,211–218,643`).
3. **B2b:** construct the matched conditional or regional reference and
   verify all prefactor, interaction, joint-avoidance, TV, boundary and
   multiplicity budgets. For C, repair the actual expansion failing C10;
   for L, produce the exact gluing and mixed majorant rather than assume
   them (`:220–229,265–276,317–327,373–460,492–519,644`).
4. **B3a:** supply local logarithms after the actual full integrations of
   R_h and Z_A, and the separate terminal reference-weighted comparison,
   with the K norm required by K2/K3 (`:523–574,645`).
5. **B3b:** prove output-to-input closure for the new effective action,
   invariant domains/rates, growing or merged holes, the normalized
   numerator, and literal STEP55/CX-R identification (`:576–637,646`).

Items 2–5 are overlapping scientific obligations. They cannot be repaired
by relabelling the conditional statements PROVEN. No deletion or demotion
of the correctly scoped identities and diagnostics is requested.

**Frozen sources, recovery and verification limits.** Checkout HEAD is
`3dff074621aa3a842ffef0a3d43d89c674ce78e2`; observed local origin/main is
`01589af3faf806b736c42dc2f3bd625e9edead9f`. The applicable workflow,
repository reviewer skill, freshness guidance and proof-governance files
match that main snapshot. The installed reviewer copy has minor wording
drift; the repository source was used. The entry-point planning fetch
succeeded and its ref remains
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0`. Main was not freshly fetched;
planning contributes no scientific premise. No branch or commit was changed.

| Source | SHA-256 |
|---|---|
| RD4.md | `60d27c7ec5e5fda254e8394c34639cccdfe42cd9f85898bb22952bc6fa6067c6` |
| RD4_LOG.md | `80faa436b9c43dfdf8c99a64d2981ff9b5177ba8f0b0f08ea6ee91fca6a65d79` |
| RD.md | `a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5` |
| RD3.md | `55274cfe3d6c90b6eb6e2f5412bdb5633660f6e47054e1db52f8a1ca9ac3d3cc` |
| REVIEW_RD3.md | `3035fde3f75182f74cf54004cc2d8ccd21f9ffef5bcf9d2158bd483b07655a8e` |
| LIB1.md | `1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1` |
| RECOVERY_CLUSTER_ASTRA.md | `9c9264bd4d92b60798e48ccd2eb0ff230e221c3ffd2107c0f6443ec86de563cf` |
| STEP55.md | `aa785cf1ba03a53e79b52e8b9eb677927d18abb26178c4c018c3c37e7e1af0ce` |
| RLARGE.md | `4f3d2777bcd736ad6936946f6c072ebebd8fe2638839538ea0db28825f2438d2` |
| LARGE55.md | `79bc36d60687376716aa425ad3c271b681ca9549f5d217693e2736b805cdf0e7` |
| checks/rd4_review.md | `39733be892a218e4aaa816f08524e7612f2ba14b4a5a9d495e8269143674de53` |
| checks/rd4_input_manifest.json | `b523282dbf0a65c8b7f5e61509e86305b07b05ebf78364305457194a6c5e0299` |

All 3,470 author-baseline entries were independently rehashed and matched.
The seven author additions give 3,477 pre-review files with aggregate
digest `7e2150fc8265b28087931cbd252c523fb1bf5e936ee702be27248e4b3fb8e71d`.
This is SHA-256 of UTF-8 Python
`json.dumps(relative_path_to_sha256, sort_keys=True, separators=(',', ':'))`.
It also binds the cited sources not repeated in the table.

The 143-line validator was read in full. It checks inventories, links,
labels, tables and source bindings, not mathematics; it accepts either
review verdict. I ran its unchanged main function with only its output
write intercepted in memory. It returned 0, all listed error collections
were empty, and all saved receipt artifact hashes matched. Its historical
first-run missing-receipt-link failure remains honestly recorded. No
author receipt was overwritten, and this replay is not scientific evidence.

Coverage includes all of RD4, RD4_LOG, RD3 and the RD/RD2/RD3 review reports;
the needed RD history, integral, chart and mixed-expansion proofs; the
complete consumed LIB1 geometry/norm arguments; and the cited cluster,
consumer, price and supplier-scope passages. Needed portions of truncated
retrievals were recovered in bounded reads. The previous RD4 report was
checked for its exact source binding, corrections and scope after the
core reconstruction; its conclusions were not substituted for proof.
No upstream numerical suite, numerical physics experiment, Lean build,
repository integration pipeline or independent audit was executed.
The scientific checks in this report are written derivations and exact
examples; deterministic hashing and validator replay are bookkeeping.

Recovery starts from the pinned RD4 bytes, F1 and the four open interfaces
above. Any source or hypothesis change requires refreshing its affected
checks. Only REVIEW_RD4.md is written; no editable prompt, author source,
check, audit or ledger file is edited, and no commit is made.
The post-write comparison reproduced the same aggregate digest for all
3,477 pre-existing files, with this report as the sole addition. The
tracked diff remains empty.

VERDICT: HOLD
