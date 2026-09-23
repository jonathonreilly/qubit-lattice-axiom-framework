# Review units and validation placement

Required before defining, reviewing, confirming, or reusing a review unit. Read the complete requirements below; they govern single-target reviews as well as backlog units.

## Coherent review units and validation placement (owner-directed 2026-09-07)

A review unit is one frozen, reviewable source argument. It may be one PR or
several cumulative/dependent PRs whose surviving claims and interactions can
be examined together. Shared Git ancestry is routing evidence, not proof of
scientific equivalence. Split large or incoherent groups into comprehensible
units; retain bottom-up delta review when a coherent final packet is unavailable.
Do not review a constituent concurrently in another unit.

For every constituent, freeze its PR number, original head SHA, declared base,
actual merge base, and original source delta. Record every source path and claim
in a complete disposition map: accepted unchanged, narrowed, superseded,
rejected, or deferred, with the final source path/blob hash or the explicit
reason and recovery location. Include deleted content, inherited proofs,
runners, helper inputs, and interacting premises. A later cumulative head
covers an earlier PR only after this map proves where its content went; a
parent's earlier PASS does not certify the final argument. Unmapped content
blocks unit confirmation. Verify original constituent deltas and the final
current-main delta independently; neither PR titles nor file counts prove
content coverage.

Run every applicable reviewer lens on the complete final unit and its
interactions. Preserve theorem, proof-obligation, import, independent-math,
no-go, labeling, and governance standards without exception for batch size.
Use the same reviewer session for findings, fixes, and final confirmation.
Freeze the disposition map hash, source/dependency/input blob hashes, original
PR heads, reviewed commits/tree, confirmation base, and reviewer findings hash
with that session's final source verdict. A changed PR head fails the provenance
gate even if source bytes look identical. A changed premise, input, source byte,
or semantic interaction reopens the affected conclusion even if a PR head did
not change. Both require renewed frozen provenance and same-session confirmation.

### Overlap repairs and review without changing acceptance

When repair authorship is authorized, hand off evidenced, finding-scoped fixes
before the original review finishes if their source and dependency boundary is
already bounded. Freeze the original heads, deltas and inspected inputs; the
author works on a separate copy while the original reviewer continues reading
the immutable originals. This is one unit, not a concurrent second review of
its constituents. Early findings are provisional, not a complete finding set
or permission to enroll the unit. Keep finding IDs and evidence revisions in
an append-only record, including superseded or withdrawn findings. Later
counterevidence can invalidate an early fix: revise or withdraw it, reopen any
affected shared source, premises and dependents, and retain the earlier record.
Before final repair executions, reconcile the complete original review with
the correction and freeze all changed prose, source and actual inputs. The
original reviewer still covers the complete final unit and all applicable
lenses, independently checks the mathematics, and confirms the affected
corrections and interactions in the same session.

Prioritize a ready final confirmation with its original reviewer before that
reviewer starts another unit's long run or review. Switch at a safe execution
boundary: finish an active bounded run or preserve its supported checkpoint
and outputs; never kill it merely to improve queue latency or silently rerun it.
The coordinator can read an immutable correction draft, proof-critical findings
and publication/input changes while the author finishes bounded controls.
Check actual note discovery, citation targets, primary/helper bindings and
declared inputs before expensive final runs. This early read does not replace
the author's complete cold diff read or final independent confirmation. If an
input changes after execution, preserve the prior receipt; never restamp it.
Re-execute affected evidence only within the actual authorization and budget.

Reuse independently verified immutable mechanical facts, such as complete Git
path/mode/blob inventories, when their exact object identities and checked
scope match. Cache the verified facts, not an assumption that an inventory is
complete: retain deleted/inherited content and the verification provenance.
Recompute changed endpoints and check current-main preservation and semantic
interactions; unchanged bytes alone do not establish unchanged premises.
Prefer tested existing tools to bespoke scripts, but do not claim an absent
verifier exists. `scripts/open_pr_science_coverage.py` records self-reported
reading coverage; it does not verify complete constituent/proof closure or
grant semantic coverage, receipt authenticity or PASS. Mechanical reuse never
substitutes for complete source/claim accounting or independent scientific reads.

Prefer one canonical unit record with immutable evidence references and
generated handoff/status summaries over several manually repeated packets.
For new units, use the versioned schema in [`references/UNIT_RECEIPT.md`](UNIT_RECEIPT.md) and
[`scripts/review_receipt.py`](../scripts/review_receipt.py) for shared preflight against actual repository APIs.
Current proof fragments that belong to a canonical claim use the version-2
`supporting_proofs` relationship, with full scientific review and owner input
pins; they are never non-science exemptions.
Run the cheap source/publication/input checks before final execution, then the
cache check against the final frozen evidence. Keep reviewer reports immutable;
adapt an older valid record once with its original hashes and explicit mappings,
never infer a scientific verdict or restamp an old execution. Mechanical success
does not establish proof closure, reviewer authenticity or landing PASS.
Keep proof explanations, original/current identities, finding dispositions,
failures, commands and final reviewer bindings explicit in that record.
Historical success, provisional findings and final confirmation remain distinct.
For measured historical-payload duplication or size costs, use the exact archive
mapping and externally pinned manifest checks in [`references/OPERATIONS.md`](OPERATIONS.md).
Keep all active proof/runtime/link targets accessible, preserve every original
path/mode/disposition, and review changed consumers. Equal historical bytes may
share storage; scientific conclusions still depend on their caller context.
Schedule bounded contemporary units separately from legacy dependency recovery
when useful; preserve every legacy obligation and reserved-source boundary.
File counts do not establish a bounded closure. These scheduling choices do
not expand an owner-frozen backlog: the active campaign retains its original
254 PR cutoff, with new arrivals excluded unless the owner changes that scope.

Perform focused source, runner, premise, vocabulary, and all three diff checks
per unit before freezing it. Reuse a prior focused result only when its exact
source, input, hypotheses, tool versions, and checked conclusion still match.
The full pipeline, strict lint, and changed-evidence gates run once on the exact
integrated current-main candidate, covering all units. They are not required
again on each constituent or unit before enrollment. References throughout this skill to the
pipeline, queue inspection, strict lint, and changed-evidence checks are parts
of this one combined pass, not additional full runs at each mention. Inspect
its affected rows and outputs for every unit. A source verdict allows enrollment;
review-loop landing PASS still requires the combined gate and all source gates.
A named review-only candidate uses one combined pass on its final candidate
with `--include-worktree` for uncommitted changes; it grants no landing authority.

Reuse successful validation only for an identical frozen base and candidate
tree, command/options, tool/runtime versions, declared inputs, and evidence
scope, with accessible successful logs and their hashes. This includes an
already validated unit whose raw tree equals the whole integrated candidate:
do not rerun the same full gate merely because its role changed to integration.
Record the tested source tree before generated validation churn and the exact
landing tree after permitted generated cleanup and manifest acknowledgment;
verify all non-generated bytes stayed identical. A missing receipt, failed
command, changed base/tree/input, or changed validation scope invalidates reuse.
Changing only commit metadata with identical base/tree does not invalidate the
mechanical result; it never waives original-head checks or reviewer provenance.
A changed base requires current-main science-loss and interaction checks before
revalidation. An uncommitted candidate is not reusable for landing until its
exact intended bytes are committed and verified against the receipt.

Exclude drafts by default. Explicit owner-directed draft triage may review a
draft and recommend close-with-reason or mark-ready on its verified head;
mark-ready is not PASS, and a still-draft PR cannot land. Exclude owner-reserved
PRs from units and their inherited content unless that reservation is explicitly
lifted. Read `docs/repo/DEFERRED_DECISIONS.md` and the current owner exclusions
before grouping; a descendant does not authorize landing a reserved ancestor's science.
For the active campaign, formal audit is deferred until a solid TOE candidate
is ready. Mechanical validation may prepare audit data, but review-loop must
not invoke an auditor or apply a scientific verdict/status.

The [collection policy](LANDING.md) is orchestrator procedure. The backlog inventory
is read-only and the contract checker checks instructions and shell structure;
neither automatically proves unit coherence, dispositions, reviewer coverage,
or validation-receipt authenticity. Those remain explicit review obligations.
