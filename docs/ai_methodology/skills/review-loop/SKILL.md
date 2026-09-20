---
name: review-loop
description: Use when an LLM agent needs to run `/review-loop`, review branch changes, run parallel physics-specific reviewers, identify overclaims/imported values/support-only material, apply narrow honest fixes, verify audit-system compatibility without applying audit verdicts, and re-review only files changed by those fixes.
---

# Review Loop

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

Run a local review/fix/re-review loop for this physics repo. This is not a
generic software review. Its job is to protect the live claim boundary:
retained/Nature-grade claims must have artifact support, imported values must
be explicit, and support-only results must not be promoted by prose.

## Model And Tool Boundary

Review-loop is a text/code/math review path. Owner direction (2026-09-08):
use **Astra low** (`gpt-6-astra`, `low`) for ordinary pre-landing science review.
Use one independent reviewer per coherent unit, applying the relevant lenses
in one focused pass. Escalate a material mathematical or premise question,
reviewer disagreement or failed decisive control that the unit review cannot
resolve through a narrow correction to
**Astra xhigh**; send its source and evidence, not the entire backlog. An
escalation is not a routine second review. Reuse completed valid reviews and
the original reviewer's affected-fix confirmation; do not rerun them just to
change model labels. Respect a later explicit owner choice. If a requested
model is unavailable, report that fact and use an available reviewer only
with its actual configuration stated. Do not silently substitute a model.

Do not use image-generation, image-editing, presentation, document-rendering,
or visual-generation tools unless the user explicitly asks for a separate
visual artifact task.

If a run surfaces an image-generation model/tool error such as a stale
`gpt-image-*` tool configuration, treat it as a local Codex tooling/config
problem, not as part of review-loop. Do not retry the review by invoking
imagegen, changing the science-review model, or routing science review through
visual tooling.

This skill is **review only**. It may make branch/package hygiene changes that
allow the independent audit system to parse and queue claims, but it must not
apply audit verdicts, write `audited_clean`, or run the audit worker.
Audit results have a strict provenance boundary: review-loop must never land
PR-submitted audit verdicts, audit-status promotions/demotions, effective-status
changes, auditor transcripts, or `apply_audit.py` outputs as authority. Audits
come only from the independent post-landing audit loop. PRs may land source
repairs, runners, controlled-data dispatch sidecars, and explicit audit or
re-audit targeting metadata when those are review-clean; they may not carry the
answer to the audit they request.
It must not create or open pull requests. When reviewing an existing PR or
branch, review-loop either fixes/narrows that existing landing path and lands it
when requested, or rejects/closes it with a clear reason. Salvage, dependency
chain repair, audit queue regeneration, and parent re-audit gates are part of
that same landing path, not follow-up PRs.
Delete a closed PR's head branch **only when durable content actually landed** --
its reviewed content was salvaged to `main`, or it was merged. Preserve the
branch instead when deferred content still needs that recovery
handle; partial salvage does not authorize deleting unlanded work. Immediately
before closing, refetch the PR head and require the frozen head SHA. If it moved,
leave the PR open and the branch intact for a fresh review of the new head. For
an unchanged same-repository head, delete only with an exact lease, for example
`git push --force-with-lease=refs/heads/<head>:<frozen-head-sha> origin
:refs/heads/<head>`, and close the PR only after that deletion succeeds. A fork
head that cannot be lease-deleted from `origin` may be closed but must be left
intact. **Do NOT delete the head branch when a PR is closed without landing its
content** -- rejected as non-landable with nothing salvaged, or with salvage
deferred to a later pass: keep that branch as the working handle on the
un-landed work. Never delete a head that still backs another open PR, nor `main`
or a protected branch. Before deleting a landed branch, list open PRs that
use it as their base, including drafts and PRs outside the current review unit.
Freeze each dependent PR's number, head SHA, original base and original delta.
Fetch newly discovered child heads before computing their deltas and verify
metadata again after fetching; [`references/OPERATIONS.md`](references/OPERATIONS.md) provides the guarded
`scripts/review_workspace.py fetch-head` command. Missing local objects never
justify skipping a child or substituting a stale base.
After verifying the parent's complete reviewed source is durable on `main`,
retarget those dependent PR bases to `main` without changing their heads or
closing them. This is base maintenance, not review or landing of their content.
Verify each dependent remains open with its frozen head and the new base, then
re-list open PRs targeting the old base immediately before deletion. If any
remain or a head changed, preserve the parent branch for recovery and record
the pending base maintenance; do not delete it. GitHub closes open PRs whose
base branch is deleted, so a same-head check alone cannot preserve the stack.
After deletion, verify the expected dependent PRs remain open; if GitHub closed
one, restore the exact deleted parent ref with an absent-ref lease, reopen the
unchanged dependent, retarget its base, and repeat the checks before deletion.
A failed retarget or recovery is a recorded operation failure, never permission
to close unreviewed content.
(Closed PRs retain their commits either way; the live
branch matters as the recovery handle precisely when the content did not land.)
It auto-corrects status vocabulary and terminology so a PR follows repo
conventions by running `scripts/vocab_lint.py --fix` on all
branch-modified files before any landing gate. Vocabulary is canonical
in
[`docs/repo/controlled_vocabulary.yaml`](../../../repo/controlled_vocabulary.yaml)
(design in
[`VOCABULARY_HYGIENE_DESIGN.md`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md)).
Routine local drift that has a non-link-aware rewrite rule, such as legacy
aliases and deprecated wording, is rewritten mechanically as part of the
same review commit; this is never a science blocker. Link-aware filename
suffix migrations and F-letter finding-label migrations are reported but
deferred to Cleanup-2 tooling. Genuinely new terms, pending link-aware
renames, or pending F-letter migrations that `vocab_lint` cannot
mechanically rewrite are recorded as
`prose_status: needs_human_vocab_decision` for the periodic
vocab-extension review; they do not block the landing. Review-loop
must not introduce new repo-wide axioms, new theory
language, new retained-surface claims, framework primitives, or new
foundational premises without explicit user approval. Imports are allowed for
bounded theorem surfaces when they are scoped, labelled, and
dependency-checked; repo-wide axiom additions and primitive additions are not
review-loop fixes.

## Focused landing review (owner-directed 2026-09-08)

Landing admits useful, honestly scoped science to main. It does not certify
the TOE or confer a retained grade. Read the complete changed argument and
necessary actual premises/inputs. Focus on consequential mathematical errors,
unsupported physical or quantified conclusions, source loss, and evidence
that fails to reproduce or does not test the decisive claim. Fix known false
claims, or narrow/defer them explicitly, before landing. A passing runner
alone cannot supply a missing proof or physical premise.

Use the [detailed lenses](references/SCIENCE_LENSES.md) to find these risks. Their exhaustive catalogs
are escalation guidance: ordinary landing review does not require a separate
report for every sentence, callable, predicate, tensor, array or conceivable
route. Keep one concise report with material findings, exact source/input
identities, relevant independent checks, honest scope and final disposition.
Retain complete constituent source recovery/disposition and the current-main
loss check; reuse already verified inventories instead of recreating them.
Uncertainty material to a stated result must be resolved, narrowed or escalated;
it cannot be hidden by postponing audit. Minor editorial detail and exhaustive
claim-by-claim certification can wait for the later formal audit.

Existing provenance, unchanged-head checks, source/input freshness, actual
execution limits, independent final confirmation, one combined mechanical
gate and audit-status separation remain required. Assess no-go quantifiers
and counterexamples carefully; retain honest N1-N8 artifacts where the
mechanical contract requires them without inventing exhaustive route coverage.
This section controls review depth and report granularity in the detailed
referenced checklists. Formal audit remains deferred until a solid TOE is ready.

## Premise Authority

<!-- BEGIN GENERATED: axiom-baseline (generate_skill_axiom_baselines.py) -->
Review-loop must enforce the two supplied premise types. Repo-wide axioms and
explicitly approved framework primitives are registered in
`docs/audit/data/axiom_premise_nodes.json` and chain-satisfy dependencies
without making downstream rows `retained_bounded`. No admission class exists;
`docs/audit/data/premise_decision_history.json` is provenance only and never
chain-satisfies. Do not infer a registered node's current grant or boundary
from a summary in this skill. Before naming a changed dependency as a premise,
import, wall, or bounded-status source, perform the mandatory authority reads
below; the registered current source files control. New axioms and new
primitives both require explicit owner approval and a reviewed registry/policy
update before review-loop may treat them as accepted premises.

Generated by `docs/audit/scripts/generate_skill_axiom_baselines.py`.
**Mandatory authority read:** before any premise, import, wall, or dependency
judgment, read the current axiom memo, primitive registry check, registry data,
and every relevant primitive source listed below. This roster is a freshness
router, not a content substitute; the cited source grant and boundary control.
Do not hand-edit inside the markers.

- axiom authority: `docs/MINIMAL_AXIOMS_2026-06-29.md`
- primitive classification procedure:
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
- primitive registry: `docs/audit/data/axiom_premise_nodes.json`
- `scale_reference_primitive`: `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`
- `kinetic_isotropy_primitive`:
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`
- `realized_state_primitive`:
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
<!-- END GENERATED -->

## Claim Boundary

Do not land new science under bare letter-number names such as `A1`, `A2`,
`G1`, or `R3`; those labels are overloaded with axioms, assumptions, Lie
types, lane stages, route codes, and branch blocks. Use the explicit
scientific name on live science surfaces; archival aliases belong
only in clearly historical work-history/archive material. Review-loop must
not treat the framework baseline as a
new axiom, new supplied premise, regulator interpretation, or optional
theory language. Correcting a PR back to this repo language is allowed. This
does not promote downstream science by itself: physical-species
identifications, `C_3`-breaking selectors, kinetic-branch selectors,
readout/scale/unit bridges, and empirical matches remain separate
bounded/open inputs unless they have their own retained-grade derivation and
independent audit closure.

Review must remove preventable source and packaging defects. The later
fresh-context audit independently tests the claim and may disagree; agreement
is not its objective. Do not pass branches that
leave the audit lane to discover basic claim-boundary, dependency-graph,
status-vocabulary, or runner-validity defects. Do not lose durable science
when a PR fails that bar: before closing or rejecting a branch, run the
[salvage pass](references/SALVAGE.md) and preserve any narrow, runner-backed lemma that can be
made canonical without changing the science.
Review-loop is still not the audit loop: it must never apply verdicts or
describe its review as an audit. Its job is to decide whether source/tooling
math, claim boundaries, and repo language are honest enough to land and be
sent to the independent auditor afterward.
Non-science PRs require the same discipline: do not reject generated
audit/status or hygiene-only work just because it is not theorem science.
First decide whether it exposes a real audit-graph, cache, queue,
normalization, dependency-chain, or audit-readiness defect. If it does,
salvage the value into durable source, tooling, pipeline, or controlled-data
repairs and regenerate the generated surfaces from that repair.
Audit-dispatch manifests are a special non-science case. If a PR lands a
source note whose purpose is to request future re-audit, retagging, cascade
repair, or batch audit selection, review-loop is not done when the source note
lands. It must also make the request machine-visible by adding or updating a
supported dispatcher sidecar under `docs/audit/data/`, rerunning the audit
pipeline, and verifying the target appears in `docs/audit/AUDIT_DISPATCH_QUEUE.md`
or `docs/audit/data/audit_dispatch_queue.json`. The dispatch manifest is
target-selection metadata only; it must not be passed to auditors as evidence
and must not apply audit verdicts.

## Arguments

Parse, in this order:

- `[target]`: optional named branch or PR (a PR number/URL, or a token that
  matches an existing branch). Resolve the target FIRST: a named target
  selects focused single-target mode; anything that is not a resolvable
  branch/PR is focus text, not a target.
- focus text: optional free-text review emphasis. With a target it scopes
  that review; without a target it scopes every slot of the backlog drain.
- `--max-iterations N`: optional iteration cap, default `5`.
- `--no-fix`: review only, do not edit.
- `--no-commit`: fix locally but do not create iteration commits.

ANY flag without a named target is an invalid invocation — flags configure
a focused single-target run and contradict or under-specify the drain
(`--no-fix`/`--no-commit` contradict its land-end-to-end contract) — stop
and ask for a target instead of guessing. Only the zero-argument and
focus-text-only forms select the backlog drain.

## Required reference routing

Use the Arguments section to resolve the actual mode. Before each applicable
operation, read the complete required reference from the same source revision
as this entry point. Triggers accumulate: a named target, a narrow fix, or a
small unit does not waive another applicable requirement. A missing or unread
required reference holds the dependent operation until the source is recovered.
The routing summaries are not substitutes for the detailed instructions.

| Mandatory trigger | Required reference |
|---|---|
| Every branch/PR review, including `--no-fix` and `--no-commit`, before review starts | [Review setup and author input hygiene](references/REVIEW_SETUP.md) |
| Before defining, reviewing, confirming, or reusing any unit, including a single PR | [Complete source disposition, same-session confirmation, and validation placement](references/REVIEW_UNITS.md) |
| Every scientific, code, governance, or methodology review and affected-fix confirmation | [All applicable reviewer lenses, reviewer prompt, and findings](references/SCIENCE_LENSES.md) |
| Before fixes, checks after fixes, re-review, or the final report | [Fix policy, smoketest, re-review tracking, and reporting](references/FIXES_AND_REPORTING.md) |
| Changed source notes, runners, claim tables, lane stubs, or publication/control-plane files; or any matching scientific PASS gate | [Audit compatibility and scientific PASS gates](references/AUDIT_COMPATIBILITY.md) |
| Whenever combined candidate validation is required, in named review-only or landing mode | [Combined pipeline, strict lint, evidence, and clean-state recipes](references/COMBINED_VALIDATION.md) |
| Actual unspecified/focus-text-only invocation, a set of PRs, or any authorized landing | [Backlog orchestration, integration, and fail-closed landing](references/LANDING.md) |
| Before PR closure/rejection, non-landable disposition, discarded stretch/campaign packets, or salvage | [Salvage and source preservation](references/SALVAGE.md) |
| Creating a new canonical unit record, using supporting-proof relationships, or adapting an older record | [Unit receipt schema and preflight](references/UNIT_RECEIPT.md) |
| Historical payload consolidation, exclusive sequential checkout reuse, or dependent-PR head/base maintenance and recovery | [Guarded review operations](references/OPERATIONS.md) |

Apply CodeRunnerReviewer to changed code and runners, PhysicsClaimReviewer to
claims and prose, ProofObligationReviewer to theorem/proof/derivation/reduction
or closure claims, ImportSupportReviewer to supplied inputs,
NatureRetentionReviewer to claimed retention, LabelingConventionReviewer to
labeling-based bounded-theorem candidates, RepoGovernanceReviewer to authority
and placement, and MethodologySkillReviewer when methodology/skill/command
files change. The full lens definitions and hard PASS gates control; this list
does not limit their scope. In particular, a changed formula, constant, matrix,
optimizer, expected value, or proof script requires an independent math check
that does not share the implementation path under review.

Negative claims (`no_go`, `stretch_attempt`, `bounded_with_named_walls`,
derived-no-go-boundary artifacts, or a reviewer's negative-claim `NO-GO`,
`BOUNDED`, or `OVERCLAIM`) require NoGoDisciplineReviewer and the N1-N8
discipline through the lenses and PASS gates. Read and apply the linked
no-go-discipline skill when triggered; do not invent route or resolution
coverage. Drafts remain excluded unless draft triage is explicitly authorized;
mark-ready grants no PASS and a still-draft PR cannot land. Owner reservations
also exclude inherited content until explicitly lifted.

Before final source confirmation, retain complete original/current-main source
and claim dispositions, including deleted/inherited work and recovery paths.
The original independent reviewer must confirm the final affected source and
interactions in the same session; no self-certification or new-session fix
confirmation can replace that requirement. A moved head, changed premise/input,
new interaction, or incomplete coverage holds the affected unit for renewed
confirmation. Landing additionally requires the exact-current-main preservation
check and combined gate. The detailed references supply the executable contract;
mechanical receipts and review PASS never apply an audit verdict.
