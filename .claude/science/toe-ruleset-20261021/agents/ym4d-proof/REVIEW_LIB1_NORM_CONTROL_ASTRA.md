# Affected review of LIB1 B1

**B1 is resolved by the frozen repair at
`fcdd32c83bc5aed08ef4f3aa5da512e668d8b216`.** The shared full-output
computation is exercised by both the exhaustive inequality and genuinely
discriminating exact witnesses. The three claimed substitutions fail at
their intended assertions. No further material finding remains in this
repair.

This is an independent affected review of the coordinator's implementation,
with no role in authoring it. It is same-family review: Codex reviewing
Codex. Requested Astra/max configuration is not independently observable
from the backend. The repair summary and code were read before the numerical
criteria; no blind or cross-family review is claimed. This is not a second
review of the complete LIB1 graph theorem, its literature, the whole PR or
an audit. The prior covariance review is separate and remains unchanged.
[PROCESS_LIGHT.md](PROCESS_LIGHT.md) governs this focused review.

The reviewed [repair receipt](checks/lib1_norm_control_fix_receipt.json) has
SHA256 `b5bed0e03189ff647c148aa501e3f9da68a93b87a4708dff65c840e6ebe0b70b`.
All 18 bound files match both the specified commit and the working files.
The corrected [checker](checks/lib1_check.py) is SHA256
`0bcd86c97aa91b6897241f6998693de15c6131e54785c77a32ee6beb097300b8`;
[LIB1.md](LIB1.md) is SHA256
`098bd38d680f82877911b34782f66394e2d6139c43e61b344b9d3bcef24ff35f`.

## Why the repair addresses the defect

The [original review](REVIEW_LIB1.md) correctly identifies an evidence
failure. Replacing the full norm on the left of an upper bound by a smaller
active norm makes that inequality easier to satisfy. Comparing independent
literal powers of two cannot test which norm the inequality computed.

In the repaired source, `exercise()` assigns `output_full` by calling
`full_output_norm(grouped, out_labels, allv, lam)` and uses that value in
`bounded_hole_full_norm`. The same function supplies the values asserted
in both exact witnesses. It chooses all graph vertices as roots and counts
every vertex in the output support. The active set is present as an argument
to support the actual mutation controls; the correct formula does not use
it. The report's norm values now come from these computations.

The full norm and active norm in LIB1 part C differ in two independent
places: permitted roots and the number of support vertices in the weight.
Both distinctions must be tested. With weight 2 per vertex:

- On the four-cycle, filling the inactive connected component enlarges the
  supported singleton to all four vertices. Coefficient q therefore gives
  input full norm 2q, output full norm 16q, and active norm 2q. Restricting
  roots alone leaves the output value 16q, so this witness cannot detect
  that error.
- On the path 0–1–2 with retained endpoints, the singleton inputs become
  supports {0,1} and {1,2}. Coefficients a,b>0 give full norm 4(a+b) at
  inactive vertex 1, full weight with retained roots 4 max(a,b), and active
  norm 2 max(a,b). These expressions differ whenever both coefficients are
  positive. For a=b=1 they give the claimed 8,4,2. The independent asymmetric
  fixture a=1/3,b=2/5 gives 44/15,8/5,4/5.

These are direct sums of the specified supported activities, not outputs
copied from the maximum routine. They explain why the two witness shapes
are needed. The repair detects the stated selector substitutions in the
shared routine; it does not claim exhaustive mutation coverage for every
possible code alteration.

## Executions and their linkage

The [review criteria](checks/review_lib1_norm_criteria.md), SHA256
`e159322586c475e9ee2a16a599f0e935a1d1deae1c696b8cbecb003570c9cdeb`,
precede the new numerical implementation. All comparisons use integers and
Fractions with exact equality. The [independent check](checks/review_lib1_norm_check.py)
uses set-valued reachability, iterative adjacent-inactive growth and direct
rooted sums. It uses the author's resource monitor and the function under
test; it does not reuse the author's graph, filling or norm routines for
its oracle.

The [results](checks/review_lib1_norm_result.json) confirm:

- 646 full-norm comparisons on all 44 connected labelled graphs with 1–4
  vertices and every retained subset, using 5,220 saturated input supports
  with nonconstant positive rational coefficients;
- 72 relabelled/coefficient-varied four-cycle cases and all six relabellings
  of the asymmetric path witness;
- runtime calls to the same full-output function in all 2,184 exhaustive
  inequality cases and both witnesses, each checked against the independent
  sum;
- every original predicate count retained in the corrected complete
  baseline, plus exactly seven new exact predicates.

The frozen source functions were compiled with recorded original and
compiled-source hashes, and their unchanged `main()` was invoked. A reviewer
wrapper replaces the final invocation/report-writing block to record
exceptions, resource refusals and results in the reviewer namespace. The
checker functions retain their original resource gates. The baseline
additionally wraps the shared function
with the oracle assertion and call counter. Mutants do not have that wrapper:
their rejection must come from the repaired author's assertions.

| Executed source | Observed outcome |
|---|---|
| Original checker, active norm substituted at its original inequality call | Exit 0, including its false “rejected by exact witness” report |
| Corrected baseline | Exit 0, complete original enumeration and new predicates |
| Shared routine: both roots and support weight active | Exit 1, `exact_cycle_output_full_norm` |
| Shared routine: only roots active | Exit 1, `exact_inactive_root_output_full_norm` |
| Shared routine: only support weight active | Exit 1, `exact_cycle_output_full_norm` |

All five new executions have empty stderr. No parser exception, resource
refusal or unrelated assertion is counted as detection. The raw child
outputs, source mutations and hashes are retained in the review namespace.
All new numerical checks reached their expected outcomes; no numerical
threshold changed.

I also verified the coordinator's five actual temporary source copies,
not only its summary receipt. Each file equals the pinned original or
corrected source with exactly its recorded single substitution. Its hash
matches both the runner's compiled-source record and the executed checker's
`script_sha256`. Each copied criteria file matches the historical criteria;
each saved result is byte-identical to its recorded stdout. Exit codes,
exact assertion names and resource receipts agree. Those checks are in the
[bindings record](checks/review_lib1_norm_bindings.json).

All original functions except `exercise` and `mutations`, including the
resource guard, are AST-identical; `full_output_norm` is the new helper. Resource observations in the new executions
and set oracle comprise 78 samples: maximum RSS 24,903,680 bytes, minimum
free memory 57%, maximum load 2.82373046875, minimum niceness 10, and maximum
sampled elapsed time about .517 seconds. All five thread settings were 1;
no pool was used. The existing 2 GB, 50% free-memory, load<20 and 60-second
program gates remain. The coordinator owns the lane lock.

One administrative binding-check command initially had an extra closing
brace and failed parsing before executing any check. The corrected retry
is recorded as such; it is not a failed norm control or evidence of detecting
a mutant. No scientific input or criterion changed in that correction.

## Preservation and scope

The complete original review, corrected checker, exact old/new source diff,
repair record, both criteria files and repair runner were read. Source
coverage is LIB1 lines 45–127, 164–214, 357–414 and 615–685, plus the
complete affected documentation diff. This covers the norm definitions,
conditional full-norm interface and evidence claims; it is not a complete
LIB1 reread. Detailed identities and read scope are in the binding record
and final receipt.

Against original commit `f15a7ad33f90d3de8ef2f8b40cada95d009f60bd`, the whole
current LIB1 file is exactly the old file with the one §10 evidence paragraph
replaced. The first 8,489 bytes retain SHA256
`1f7367c972e1ad49e81cfccdab1bec07b2259a44616fc45bab28e89174941c3d`.
Thus every other source byte, including every mathematical section, is
unchanged. The original log is preserved with only its marked repair
appendix. The original review and ten historical criteria/output/validator
artifacts are unchanged. The archived checker is the exact
original `63256a04b6d2fc46dad13ee26ae0b0c592e93ac7d271157076ef32d23650fdbc`.

The documentation now distinguishes the original toy comparison, the
surviving source substitution, the corrected shared computation and its
separate executions. It accurately leaves the old validator and result
receipts attached to the historical artifact set. The current checker's
new result filename avoids overwriting that old result. Its “affected
confirmation pending” labels describe the input reviewed here; this report
provides that confirmation without rewriting those frozen input files.

No source, shared register, git state or audit record was edited for this
review. No further source repair is required for B1. Its original HOLD is
preserved against the original package, while this affected finding is now
resolved. Bounded holes and the stronger input norm rate remain premises;
unrestricted histories, source/sea integration, full four-dimensional
existence and the physical continuum mass gap remain OPEN. No broader
library, PR or audit verdict follows.

VERDICT: LAND
