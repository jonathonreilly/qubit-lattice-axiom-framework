# Second independent hostile review of LIB1

2026-10-29. **No material defect found in parts A–C or their explicitly
conditional H24 application.** Two nonblocking findings follow. This is a
fresh reviewer context with no authorship of LIB1. Earlier review conclusions
were claims to test, not premises. No numerical checker, enumeration, or
mutation was executed; the user expressly requested source inspection only.

Reviewed worktree HEAD: `9658cc870d82401001e56b29f351aec5f5f58fa1`.
The LIB1 revision last changed at `8034d12aed139c0703f80cd0b979c251633bdd83`.
The relevant workflow/reviewer instructions match the locally available
`origin/main`, `01589af3faf806b736c42dc2f3bd625e9edead9f`; no remote freshness
or new audit status is asserted. All file/line references below are relative
to this working folder and refer to this reviewed snapshot unless stated
otherwise.

| Source | SHA-256 |
|---|---|
| `LIB1.md` | `1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1` |
| `LIB1_LOG.md` | `f87c381ddea9d356bbbb583d589a94a5095435c009148b504ceef6390e24be27` |
| `REVIEW_LIB1.md` | `6d81bcc64fa4ce4ef970549474791c6c9c8ad17d138a5ec972c930ac58e3bff8` |
| `REVIEW_LIB1_R2.md` | `c917e2a9c00a6e9f46aba74461b4c52172a7221eb74776426ef7564ab45c311b` |
| `checks/lib1_check_v2.py` | `89a35d0d9dc4dd0707ad1813174c83a31081c4a17a3e5e71cc328c2401ba6626` |
| `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md` | `d2e9c49eedceb14b654f5be640e2b55efc16b902fd789acbc3d73c2849b9a850` |

**Findings, ranked by severity.** No critical, high, or medium finding.

1. **Low — the finite entropy check cannot challenge the claimed constant,
   and the tree/decay predicates admit an identically zero tree table.**
   Locations: `checks/lib1_check_v2.py:127–132,161–174,190,201–202,219–245`;
   `checks/lib1_criteria_v2.md:10–12` inherits
   `checks/lib1_criteria.md:17–35`; coverage summary `LIB1.md:630–646`.
   Each tested entropy sum has a fixed root in a six-vertex graph. There
   are at most `2^5=32` subsets containing that root, and each summand is at
   most one for any nonnegative supplied length. Thus the comparison with
   1024 cannot fail within that input class, even if every length is zero.
   With a zero table, tree monotonicity reads `0<=0`, every input coefficient
   becomes one, and each grouped decay comparison has at most 63 terms
   against 1024. The native-4D routine does not call this table. This is a
   static counteranalysis of test discrimination, not a claimed mutant run.
   The actual `steiner_table` code correctly minimizes over connected
   supersets; I found no error in its implementation.

   **Fix:** before treating these predicates as regression protection for
   tree lengths, assert independent exact lengths, for example distance 5
   between the endpoints of `path6` and distance 3 between opposite vertices
   of `cycle6`, through the actual table. Describe the entropy comparison
   as a loose finite sanity check. This is nonblocking because §§2–5 supply
   the uniform proof, `LIB1.md:630,665–667` explicitly limits the program's
   evidentiary role, and no rejection of a wrong tree-table implementation
   is claimed. It is not the false mutation-rejection claim of historical B1.

2. **Low — current citation/provenance lookup needs a revision-aware map.**
   Locations: `LIB1.md:567–569,600–604`;
   `checks/lib1_validate.py:32–35,38–40,80`;
   `checks/lib1_source_manifest.json:6–128`.
   The R10 quotation is now at `SOFTHARD.md:496`, and the two HANDOFF
   quotations are at `HANDOFF.md:620–621,626–628`, not the printed old
   offsets. All ten producer/consumer quotations still match exactly after
   whitespace normalization; this is locator drift, not changed wording.
   The validator also reads another machine's absolute paths and pins an
   earlier HEAD. After mapping the 17 text entries to this folder, 12 hashes
   match and five differ: SOFTHARD, HANDOFF, APPROACH_REGISTRY, REC_LIB and
   PROOF. The eight recorded PDF paths are unavailable here. Consequently
   R2's historical one-file drift inventory (`REVIEW_LIB1_R2.md:102–121`)
   cannot be reused as a current inventory.

   **Fix:** retain the historical receipts and append a current relative-path,
   revision-pinned source/locator map before reusing that validator. Do not
   restamp an old PASS. This does not block LIB1: the actual H24 producer is
   byte-identical, the consumer words and open obligations survive, and
   `LIB1_LOG.md:267–274` already treats the old validator receipt as history.

**What I re-derived.** The following conclusions come from the definitions
and displayed hypotheses, not from either earlier verdict or saved PASS counts.

1. **Component geometry, identity, and locality** (`LIB1.md:68–92,216–273`).
   Every added component of `Γ\Λ` intersects or neighbors connected X, so
   their union is connected. Distinct components cannot share an edge;
   every component meeting the union is therefore included completely.
   Only inactive vertices are added, giving `Y∩Λ=X∩Λ`. Any ambient tree
   containing `X∩Ω` contains `X∩Λ`, hence `d_Λ(Y)<=d_Ω(X)`. The fibres
   partition exactly the inputs meeting Λ. Inputs disjoint from Λ stay
   in `B_inactive`; exponentiation and integration preserve that term and
   every prefactor. Since `X⊆Y`, complete original argument supports remain
   local in Y. Finite sums preserve the assumed source holomorphy.
   No independence, positive measure, or denominator estimate enters.

2. **Uniform counting** (`LIB1.md:275–331`). Put `S=X∩Ω` and `n=t(S)`.
   A minimum tree has `n+1` vertices. Choose one deterministically, traverse
   its edges twice from the fixed root, and record the S-markings. This is
   an injective encoding of S with at most `8^(2n) 2^(n+1)` descriptions.
   Every included inactive component must have an edge to S: the first
   exit along a path to S cannot enter a different inactive component.
   There are at most `8|S|` such components. Choosing their subset gives

       8^(2n) 2^(n+1) 2^(8(n+1)) = 512·32768^n.

   The geometric series converges precisely under the stated sufficient
   restriction `a>log(32768)` and gives `C(a)` as printed; at `a=16 log 2`
   it gives 1024. This establishes uniformity without bounding the sizes
   or number of holes. As a second encoding check, a rooted plane-tree
   shape has at most `2^(2n)` up/down words, and its n outward edges have
   at most `8^n` choices. With the same markings and hole choices this
   gives the stronger majorant `512·16384^n`. Neither calculation uses a
   sampled count or an imported lattice-animal theorem.

3. **Fibre decay** (`LIB1.md:333–355`). A single chosen vertex of `Y∩Λ`
   belongs to every X in its fibre. Split the exponent into `a` and
   `κ_B−a`, use monotonicity for the latter, and apply the rooted count to
   the former. This gives exactly `C(a)B₀ exp[-(κ_B−a)d_Λ(Y)]`, without
   an output-volume factor. Empty fibres give zero. No smallness of B₀
   or later cluster-expansion hypothesis is inferred.

4. **Both norms, with their quantifiers** (`LIB1.md:107–127,357–412`). For
   an active root, membership pulls back exactly, and
   `|X∩Λ|<=|X∩Ω|<=|X|` gives contraction for `μ>=0`. For the full norm,
   at most `8|X|` components enlarge X; if each has at most M vertices,
   `|R_Λ(X)|<=(1+8M)|X|`. If an inactive vertex v belongs to the output,
   its component `H_v` meets or neighbors a preimage X. Thus X contains
   some vertex of `N[H_v]`, a set of at most `9M` vertices. Summing the
   input rooted bounds over that set gives
   `||B'||_μ<=9M||B||_(1+8M)μ`. Retaining the separate inactive family
   adds at most one more input norm. Uniform full-norm control requires
   uniform M and the stronger input rate; no such bound is hidden in the
   active norm. Singleton/empty/full active sets, the one-vertex graph,
   disconnected active sets, and `μ=0` introduce no exception.

5. **Source differences and Cauchy estimates** (`LIB1.md:199–214,414–438`).
   With graph, masks, F and real-data domain fixed, regrouping is linear
   and commutes with subtraction and source differentiation. Zero lies
   in the centered source polydisc, so subtraction costs at most two.
   Iterated Cauchy contours inside the outer polydisc give
   `α!(r−r')^(-|α|)`, including after rooted summation. Coordinates outside
   Y have zero derivative. These are bounds for each specified multi-index,
   not a dimension-free sum of all derivatives. The zero-radius case has
   no derivative conclusion. No holomorphy through a data-dependent mask
   or in hard-selected real coarse fields is used.

6. **Producer/consumer implication** (`LIB1.md:440–526,559–585`). H24 has
   exactly the required order `sup_root sum_support weight sup_data`, not
   the weaker `sup_data` outside the support sum. Its graph, original
   sources, fixed kernel, real-field supremum and fixed F agree with
   `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:106–120,435–459,565–620` and the
   kernel in `LINEAR_PACKAGE.md:65–82`. At Ω=Γ its connected supports are
   admissible and give the active norm `d_q`, or `2d_q` after subtraction.
   A connected X has `t(X)=|X|−1`, proving L19. Replacing μ by
   `ν=(1+8M)μ` in H21 gives precisely L20 and the output budget
   `9M d_q(ν)`, not `d_q(μ)`. H21's `d_q(ν)<=1/4` alone does not pay
   the output budget. H25 is only preserved if supplied. No result on the
   remaining sea expectation or higher-level actions follows.

   The six consumer rows match their quoted contracts: SOFTHARD R10 at
   current line 496; HANDOFF steps 2/4 at 620–628; assembly items 11/13 at
   `CODEX_REVIEW_ASSEMBLY.md:229,231`; and `STEP55.md:583`. Each purported
   discharge is an identified subproblem, with the full consumer explicitly
   open. The new ambient graph distance is not silently identified with
   SF's continuum touching distance or a metric that contracts holes.

7. **Scope witness and repaired norm controls** (`LIB1.md:528–557,669–707`;
   `checks/lib1_check_v2.py:153–155,275–320,367–411`). The punctured 4D torus
   is connected by keeping a nonzero coordinate fixed while setting a second
   coordinate to 1, then keeping that coordinate fixed while changing the
   others. Its singleton activity therefore saturates to Γ. The input,
   active output and full output norms are respectively
   `b e^μ`, `b e^μ`, and `b e^(μ|Γ|)`.

   On the four-cycle, a unit activity consequently gives `(2,16,2)` at
   `μ=log 2`. On the path with active endpoints and positive coefficients
   a,b, the full output root sums are `4a,4(a+b),4b`; restricting roots
   gives `4 max(a,b)`, while the active norm is `2 max(a,b)`. This proves
   both witness discriminators independently of the code's maximum routine.
   The inequality and witnesses call the same full-output function. The two
   specified return substitutions therefore change the asserted values to
   2 instead of 16, and 4 instead of 8, respectively. The existing three
   static contrasts remain static; v2 accurately says so. In particular the
   two literal dictionary inequalities at lines 264–265 supply no independent
   implementation-discrimination evidence.

**Evidence inspection and limits.** I read the complete LIB1 argument and
both requested reviews, the log and criteria, and the checker/validator
sources; inspected the JSON/stdout records and their bindings without
executing the programs; and inspected the cited producer, consumer and
related-work passages at their actual locations. The v1 source equals its
archival copy. AST comparison confirms the common graph, norm and resource
functions are unchanged in v2; inside `exercise` only the shared output-norm
call changes. The baseline source hash and both mutant hashes reconstruct
from the current source and recorded single-line substitutions. The separate trial records equal the
suite entries, stdout equals the suite, and stderr is empty. Recorded
resource observations meet their stated thresholds. These are consistency
checks of saved evidence, not new execution results or authentication of
historical machine state.

The alternative `lib1_norm_control_*` repair is not current v2 evidence.
Its driver expects a helper absent from the restored v1 file and would
stop at `checks/lib1_norm_control_run.py:22`. This is already correctly
qualified by `HANDOFF.md:199–209`, `APPROACH_REGISTRY.md:182–193`, and
`PROOF.md:368–379`. I recovered its corrected source read-only from the
pinned commit `fcdd32c83bc5aed08ef4f3aa5da512e668d8b216`; its hash and all
five recorded executed-source/output bindings agree. It would be incorrect
to treat the restored v1 file as a regression of the separately delivered
v2 repair, or to transfer the older review's source identity to v2.

The original 8,489-byte PRE-STATED prefix and the 9,835/28,105-byte log
prefixes match their recorded hashes. The nine final note/check-file
receipts also match. I did not authenticate original first-edit ordering
from the old session transcript, or revalidate historical nanosecond times.

For literature, I inspected the saved equation-page images and the official
arXiv text for [Dimock III, Appendix B, p.35](https://arxiv.org/pdf/1304.0705v1)
and [Dimock II, Appendix E, pp.88–91](https://arxiv.org/pdf/1212.5562v2).
They support the credited regrouping/counting strategy; their continuum
metric and unspecified constants are not imported. The potentially wrong
family label in III's first line of (244) is not copied into L11, which
continues to sum over `P_Ω`. The [QED paper's official abstract](https://arxiv.org/abs/1712.10029v3)
confirms its stated comparison scope only. No specialized external theorem
or load-bearing memory-only `[m]` step is needed for LIB1's proof.

**What I did not re-derive or verify:** H18–H25 as assertions about actual
Yang–Mills activities; the full SF/CX-R, reconstruction, flow or reference
integration arguments; all auxiliary papers inventoried in the manifest;
global novelty across branches/literature; the historical execution/session
claims; numerical predicate totals by replay; a fresh documentation-validator
or integration PASS; or any continuum existence/mass-gap result. The source
PDF byte hashes could not be rebound to the missing local files; two web
page-render requests also failed, so the saved images and readable official
text were used. None of these omitted operations is substituted for a
load-bearing step of the conditional graph theorem reviewed here.

The remaining scientific obligations are exactly the actual full-history
activity/sea estimates, unrestricted-hole full-norm control or a compatible
alternative representation, source normalization after integration, and
the higher-level induction (`LIB1.md:766–777`). This review leaves them open.
Only this report is added; no source fix, numerical rerun, commit, consumer
edit, or audit operation is performed.
The final inventory found unchanged sizes and hashes for all 409 pre-existing
inventoried Markdown/check artifacts. HEAD is unchanged and the tracked diff
is empty; the four pre-existing REVIEW2 files were preserved.

VERDICT: CONFIRM
