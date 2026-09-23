# Salvage and source preservation

Required before closing or rejecting a PR, marking it non-landable, discarding a stretch/campaign packet, or attempting salvage. Apply the [branch and dependent-PR recovery rules](../SKILL.md#model-and-tool-boundary) before any closure or deletion; a salvage decision does not authorize losing unlanded work.

## Salvage Pass

Run this pass before closing a PR, marking it non-landable, or discarding a
stretch/campaign packet. The goal is to preserve meaningful science without
lowering the review bar.

1. Inventory the branch into these buckets:
   - canonical source candidates: theorem/no-go/open-gate notes and paired
     runners;
   - useful negative results: failed routes that name a durable obstruction and
     have a runner or exact calculation;
   - support-only calculations: exact algebra or bookkeeping that may be useful
     as bounded support but not as retained/Nature-grade science;
   - audit/process hygiene: dependency-graph repairs, audit queue unlocks,
     stale runner-cache detection, generated-data normalization, cycle-break
     hygiene, and pipeline/tooling fixes that make audit results more reliable;
   - non-source material: claim-status certificates, handoffs, campaign state,
     generated audit files, expected audit verdicts, and branch-local logs.
2. For each source candidate, decide whether it can be salvaged with only
   review-level edits:
   - the claim can be narrowed to a canonical `claim_type`:
     `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`,
     `decoration`, or `meta`;
   - all imported physics, textbook machinery, observations, fitted values,
     and conventions are explicitly labelled;
   - the runner tests the actual load-bearing bridge, not just downstream
     arithmetic after the premise is assumed;
   - load-bearing dependencies can be represented as markdown links and
     non-load-bearing siblings can be kept out of the citation graph;
   - the salvage does not rely on a closed, unlanded, unaudited, or rejected
     sibling PR unless the dependency is copied in as a self-contained
     derivation and reviewed in the same salvage branch.
3. Do not salvage by papering over missing science. If the durable part is
   only an obstruction or failed route, salvage it as a narrow `open_gate` or
   `no_go` only when the runner directly supports that negative boundary.
4. Strip all non-source material from salvage branches:
   claim-status certificates, handoffs, campaign state, expected audit
   verdicts, `target_effective_status_*`, `audit_status = ...`, generated audit
   verdict payloads, and branch-local logs.
5. Prefer small salvage slices grouped by coherent topic. Split unrelated
   lemmas rather than bundling them only because they came from the same failed
   PR, but do not open follow-up PRs for those slices. Land them through the
   current requested landing path or report that the work cannot be landed yet.
6. Run the normal [audit-system compatibility gate](AUDIT_COMPATIBILITY.md) on every salvage slice.
   The resulting rows must remain `unaudited`; the independent audit lane owns
   all verdicts.
7. For audit/process hygiene, preserve the durable repair rather than the
   generated symptom. Land source/tooling/pipeline/controlled-data changes when
   they strengthen the repo or unblock auditing without changing science.
   Regenerate audit JSON/Markdown from the pipeline afterward only from the
   reviewed source repair on current `main`. Do not land PR-authored
   `effective_status`, `intrinsic_status`, `audit_status`, auditor-output,
   previous-audit, or expected-verdict edits as the authority for the change.
   Source repairs may intentionally invalidate a prior row hash and make a row
   visible for re-audit; that is allowed. The independent audit loop must still
   produce the verdict after landing.
8. If no salvage is possible, leave a concise PR comment or review summary
   saying why, for example: "runner only rechecks assumed premise",
   "claim depends on closed sibling", "noncanonical stretch packet with no
   theorem-grade boundary", or "overbroad theorem not supported by runner".

Salvageable examples:

- a parity/counting/no-go lemma with a decisive finite algebra runner;
- a conditional textbook lemma that is useful only when explicitly marked as
  bounded support;
- a negative route that conclusively rules out one proposed mechanism and
  narrows the remaining open gate;
- an audit-hygiene PR whose generated status change reveals a real durable
  graph/tooling/pipeline defect, salvaged as the underlying repair plus
  regenerated audit outputs.

Not salvageable without a new research task:

- branch-local certificates and handoffs with no source theorem;
- broad "closing derivations" whose runner assumes the missing bridge;
- expected audit verdicts or status-elevation packages;
- stretch-attempt notes that document research direction but do not define a
  canonical theorem/no-go/open-gate boundary.
