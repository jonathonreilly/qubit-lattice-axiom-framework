# Independent hostile rereview of LIB1

Review date: 2026-10-29. **LAND at the stated finite-graph, conditional
application scope.** The sole binding finding, B1, is resolved. The corrected
checker uses the same full-output computation in its inequalities and exact
witnesses, and both specified implementation mutations were rejected in this
review's replay. The theorem and its analytic residue are unchanged.

This is the fresh independent follow-up expressly requested by the user. I
authored none of the submitted files and am not the original reviewer. No
same-session or cross-family confirmation is claimed. LAND is the disposition
of this library packet; it confers no audit status or completed Yang–Mills
construction. Only this report is written; no commit or landing operation is
performed.

Candidate HEAD remains `4f04b662f4d72d7ef269f6d9693ae9ff6424acf9`; freshly
fetched `origin/main` remains `ca2bc7ddf64790da96cd43d42017d000fbfe4808`.
Repository review guidance was applied within the user's one-report scope.

| Frozen artifact | SHA-256 |
|---|---|
| `REVIEW_LIB1.md` | `6d81bcc64fa4ce4ef970549474791c6c9c8ad17d138a5ec972c930ac58e3bff8` |
| `LIB1.md`, 44,321 bytes | `1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1` |
| `LIB1_LOG.md`, 36,082 bytes | `f87c381ddea9d356bbbb583d589a94a5095435c009148b504ceef6390e24be27` |
| `checks/lib1_check_v2.py` | `89a35d0d9dc4dd0707ad1813174c83a31081c4a17a3e5e71cc328c2401ba6626` |
| `checks/lib1_criteria_v2.md` | `acb1ccbd406668737d32777ce57dc9294d88ba9ecb38979da27bb35187e8c6ca` |
| `checks/lib1_check_v2_result.json` and identical stdout | `cec721cd99576a3301337ffb579faae622bf5f4cb010979d23f655d02464ad57` |

I read the complete revised note, log and v2 source/criteria, compared the
runner with v1, inspected all v2 receipts against their source, and checked
the actual producer and consumer passages. The individual trial JSONs equal
their corresponding suite entries. All recorded script, criteria and mutant
source hashes reconstruct exactly. Recorded stderr is empty.

**Binding finding B1 — RESOLVED, correct and honestly scoped.** R1 identifies
one blocking finding, with the following required parts; these rows separate
its obligations without inventing additional findings.

| Required part | Verdict and evidence |
|---|---|
| Connect the witness to the inequality's full-output computation | **RESOLVED.** `checks/lib1_check_v2.py:153–155` defines `full_output_norm` with all graph vertices as roots and all support vertices in the weight. Lines 209, 284 and 308 call that same function. AST comparison confirms the only change inside `exercise` is this shared call. `LIB1.md:674–676` and `LIB1_LOG.md:209–216` describe it accurately. |
| Assert independently derived four-cycle values, including the full value | **RESOLVED.** Criteria lines 24–31 and runner lines 275–295 specify and compute input/full output/active output `(2,16,2)`. For one unit activity, the input has one vertex; its saturated output has four. At μ=log 2 the weights are respectively 2 and 16, while the active weight remains 2. This follows directly from the definition, independently of `norm`. Line 294 asserts the computed full value. Note lines 678–681 and log lines 214–215 agree. |
| Detect omission of inactive roots using overlapping outputs | **RESOLVED.** Criteria lines 32–39 and runner lines 297–320 use the path 0–1–2 with active endpoints. Outputs `{0,1}` and `{1,2}` each weigh 4, giving full rooted sums `(4,8,4)` and a unique inactive maximizing root. The computed norms are `(2,8,2)`. Restricting roots to the endpoints produces 4, which line 319 rejects. Note lines 682–686 and log lines 215–216 agree. |
| Run the baseline and actual mutants under the existing resource gates; retain distinct outcomes | **RESOLVED.** Runner lines 367–430 compile two copies with exactly one changed return expression, preserve the assertions and resource monitor, share one deadline, and require the particular assertion and wrong value. This review reproduced baseline success and both required failures after all 2,184 full-norm inequalities in every trial. Separate author receipts and the log at lines 218–254 accurately distinguish caught assertion classifications from subprocess exits. |
| Correct the positive coverage claims | **RESOLVED.** `LIB1.md:648–655` and `LIB1_LOG.md:174–196` withdraw the unsupported v1 implementation-coverage interpretation while preserving the historical text. Note lines 688–707, log lines 239–245, and runner lines 252–272 identify exactly two new implementation mutations; the other three inherited comparisons are explicitly static contrasts. Finite regression evidence is not promoted to an all-volume proof or independent author review. |
| Preserve the immutable prefix and theorem | **RESOLVED.** Removing only the marked §10 repair and restoring the quoted bullet reconstructs the original 40,718-byte note with R1's hash `cc1252b360b00e0463452febefba22313a1329cfee17515f012d3f4aa9bc8c76`. The 8,489-byte PRE-STATED prefix retains hash `1f7367c972e1ad49e81cfccdab1bec07b2259a44616fc45bab28e89174941c3d`. The original 9,835-byte log also remains an exact prefix with R1's hash. No theorem, hypothesis, consumer qualification or analytic residue was rewritten. |

The log's later timestamp-precision correction (`LIB1_LOG.md:584–808`) is
honest bookkeeping: the nine final content hashes and sizes match, as do the
remeasured decimal-string mtime/ctime values. The intermediate 28,105-byte
log prefix matches its recorded hash. Criteria creation precedes script
creation, and both precede the recorded author run. The author expressly
discloses prior exposure to v1's failure; no blind-experiment claim is made.

**Replay and adversarial outcomes — PASS.** I reran the existing v2
`run_suite()` once at `2026-10-29T20:47:15.590875+00:00`, with Python `-B`,
`PYTHONDONTWRITEBYTECODE=1`, `nice -n 10`, and all five recorded thread
variables set to 1. No pool was used. Because the script intentionally refuses
existing receipt paths, I intercepted only the existence checks and exclusive
opens for its four JSON outputs, capturing them in memory. Unexpected writes
were rejected. Source text, mathematical predicates, mutations, source-hash
calculation and resource guards were unchanged. No author output was replaced.

| Trial | Observed result | Compiled-source SHA-256 |
|---|---|---|
| Baseline | Classification 0; four-cycle `(2,16,2)` and overlap `(2,8,2)` | `89a35d0d9dc4dd0707ad1813174c83a31081c4a17a3e5e71cc328c2401ba6626` |
| Active for full: `norm(grouped, out_labels, lam, lam, 1)` | Classification 1, `AssertionError: four_cycle_full_output_norm_exact`; computed 2, required 16 | `5ec74c31c916eb3cd74d3d98229e72e13bf2e0de0cafb15b9a8c253abb59e166` |
| Inactive roots omitted: `norm(grouped, out_labels, lam, allv, 1)` | Classification 1, `AssertionError: overlap_full_output_norm_exact`; computed 4, required 8 | `b4bbf14ec5c52f19fce2d392682fccac6bb8218a198113c1449b5bc70806b641` |

Suite exit was 0. All scientific receipt fields matched the saved author
results, including predicate counts, graph coverage, computed witnesses,
failure reasons and compiled-source identities. Each trial completed 2,187
polynomial identities, 36,873 small-graph support cases, 576 entropy and 8,972
decay comparisons, 2,187 active-norm and 2,184 bounded-hole comparisons, and
6,288 native-4D support cases before its witness outcome. The mutants still
pass the weaker inequalities, which is precisely why the exact assertions
are necessary.

The replay's 51 resource observations gave maximum RSS 26,918,912 bytes,
minimum free memory 60%, maximum load average 2.10888671875 and observed
niceness 20. Outcome guards ran after the expected failures. Elapsed time was
1.3266217499622144 seconds, with empty stderr. No execution was sandbox- or
resource-blocked. This replay verifies implementation behavior; the independent
mathematical check is the explicit support/root calculation above and the
proof examination below.

**Earlier scientific confirmations — retained.** R1 calls these PASS rather
than CONFIRMED. I checked their continued validity in the complete revised
argument; hash preservation alone was not used as a proof.

| Earlier item | R2 disposition |
|---|---|
| First-edit provenance and stated target | **CONFIRMED.** The previously authenticated PRE-STATED bytes and original log are preserved. R1's provenance conclusion is unaffected. The library target and its four selection criteria remain unchanged. |
| Target choice and nonduplication | **CONFIRMED at the bounded library scope.** SOFTHARD R10 still requests this operation; HANDOFF steps 2/4 and assembly items 11/13 remain open consumers. A repeated folder search found no duplicate arbitrary nested-component saturation result. The closest source/history boundary cancellation remains a fixed-boundary operation. No all-literature absence claim is accepted. |
| Part A, note lines 216–273 | **CONFIRMED.** Added components meet or neighbor connected X, distinct inactive components cannot neighbor one another, and only inactive vertices are added. Thus the result is connected and saturated, with `Y∩Λ=X∩Λ`. Fibres partition exactly the inputs meeting Λ. Complete original arguments and the separate inactive sum survive. Finite sums preserve the stated source holomorphy. |
| Counting and decay, lines 275–355 | **CONFIRMED.** A minimum n-edge tree has n+1 vertices. Its rooted traversal and marked vertices encode the active set; each included hole has an edge to that set. This gives `8^(2n)·2^(n+1)·2^(8(n+1)) = 512·32768^n`. The geometric sum is valid for `a>log(32768)` and gives 1024 at `a=16 log 2`. A single common active root in each fibre and tree monotonicity give the stated decay loss. No numerical sample supplies this uniform proof. |
| Norms and sources, lines 357–438 | **CONFIRMED.** Active-root membership pulls back exactly and μ≥0 gives the weight comparison. With holes bounded by M, `|Y|≤(1+8M)|X|`; any inactive root's preimage meets a neighborhood of at most 9M vertices. This proves the stronger-rate full-norm bound and the additional inactive-family cost. Linearity, the factor-two difference estimate and the inner-polydisc Cauchy estimate retain their hypotheses. |
| Producer and consumer matching, lines 440–526 and 559–585 | **CONFIRMED as implications and narrowing.** All ten literal quotations still match the actual files. H24's original source domain, real-field supremum, fixed F and fixed kernel remain explicit. Full output requires H24 at `(1+8M)μ`, its changed smallness threshold, uniform M and the downstream budget. The gas identity preserves supplied H25 only; it does not establish a sea expectation or completed consumer. |
| Four-dimensional scope witness, lines 528–557 | **CONFIRMED.** The punctured torus is connected by the displayed coordinate path. Saturating the singleton gives Γ, so the exact full norm grows from `b exp(μ)` to `b exp(μ|Γ|)` while the active norm stays fixed. This concerns the specified support map and a permitted test activity, not an actual Yang–Mills coefficient or an obstruction to other constructions. |
| Existing finite checks | **CONFIRMED within their enumerated scope.** The graph, closure, tree, generic norm, native-4D and resource routines are AST-identical to v1. The replay preserves all earlier finite predicates. The old unsupported active/full mutation claim is expressly superseded by the resolved B1 evidence. |

**Current provenance limitation — disclosed, nonblocking for B1.** The frozen
documentation validator was also attempted without permitting its output
write. It exited 1 at `checks/lib1_validate.py:35`: the old source manifest
still pins `REC_LIB.md` at 68,974 bytes and hash
`79e570f5c21c0ceceb4dc076fabb1e7ce696afa1bbd4630da036456d3de53b13`, whereas
the current file has 74,755 bytes and hash
`3a0052652fd4146fd9803b069624ddc7a5357c1a90ff063875a8514a79ef6ae3`.

An independent inventory found exactly this one mismatch: the other 24 source
entries still match, including the actual H24 producer, consumers and cited
PDFs. I inspected the marked REC-LIB corrections and their log: they concern
tensor boost bounds and reconstruction/consumer residues. LIB1 invokes no
REC-LIB result; its graph proof and producer interface do not use those
arguments. The drift therefore invalidates a present-tense 25/25 manifest
claim, not a LIB1 theorem or B1 check. The earlier 25/25 observation and old
`lib1_validation.json` remain historical receipts, as the repair log states
at lines 270–274. I separately verified the ten quotes and all v2 source,
output and resource bindings. **A fresh full documentation-validator PASS
remains unclaimed; the incidental manifest binding needs reconciliation if
that old validator is reused.** No failed validation was relabelled PASS.

**Remaining residue — explicitly open, with no closure inferred.** The revised
note names the following limitations at lines 159–162, 199–214, 352–355,
479–526, 565–585, 723–764 and 766–777; the log agrees at lines 125–129 and
282–287:

- Actual full-history boundary activities or a source-local inactive
  expectation; a full output norm for unrestricted holes, or a proved
  compatible representation. Uniform M, the stronger input rate and the
  output smallness budget are hypotheses to establish where needed.
- Reference/sea and COL-compatible integration, failure suppression, the
  complete returned denominator and its zero-free/normalization estimates.
- Complete N1/N2 over all coarse fields and histories, higher-level actions,
  source estimates at each level, coupled flow and induction. HANDOFF steps
  1, 3 and 5, existence and the physical mass gap are not discharged.
- Conversion to other support-distance conventions; locality through
  data-dependent masks; hard-route activities, domains and bounds; and the
  hypotheses of any subsequent cluster expansion. No hard-kernel limit is
  proved by this reindexing.
- No exhaustive no-go result or successful negative-claim packet. Alternative
  support labels, hole-aware consumers and actual-weight suppression remain
  available routes; the scope example excludes none of them.

The author's pending-review statements at note lines 716–721 and log lines
282–287 accurately describe the author handoff. This fresh R2 supplies the
requested independent assessment of B1, without editing the historical HOLD.
There are no remaining binding repairs for this scoped library artifact.
Repository-wide integration checks and audit operations were not run; no
integration or retained-grade verdict is claimed. The 2,206 pre-existing files
in the working folder were unchanged during this review; this report is the
sole added file.

VERDICT: LAND
