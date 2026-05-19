---
name: audit-loop
description: Run the cl3-lattice-framework audit lane as an adversarial Nature-grade claim auditor. Use when the user asks to audit scoped retained-grade science, process the audit backlog/queue, run an auditor loop, update audit results, apply audit verdicts, or push claim-audit outcomes directly to main.
---

# Audit Loop

## Skill Freshness

Before applying this skill, perform the repo skill freshness check described in
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`. If a newer version of
this `SKILL.md` exists on `origin/main`, follow that version for the current
task.

Use this skill to audit one claim at a time from the repository audit queue and land the audit result. The standard is hostile field review: the claim must survive an adversarial physicist looking for hidden imports, circular logic, definition-as-derivation, stale numerics, misidentified observables, and overstated closure.

## Non-Negotiables

- Audit; do not repair the science. If a claim fails, record a physicist-actionable failure handoff so someone else can fix it.
- Work one claim per commit. This keeps audit verdicts reversible and reviewable.
- Prefer a clean temporary worktree based on `origin/main`. Do not use a dirty shared checkout for audit commits.
- Push routine audit commits directly to `main`. This project has authorized direct-main audit operation for ordinary `apply_audit.py`-accepted verdicts; do not open PRs for routine clean, conditional, renaming, decoration, numerical-match, or non-controversial failed verdicts.
- Do not read broad publication framing while judging the claim. Use the source note, one-hop cited authorities, runner, runner output, and the audit rubric.
- Preserve fresh-context integrity. Do not read prior audit rationales, previous audit entries, rendered `AUDIT_LEDGER.md` history, PR text, publication framing, or downstream summaries while judging a claim.
- Do not grant `audited_clean` unless the derivation closes without hidden premises, unsupported physical identifications, circular dependency, or tuned comparator matching.
- Apply the No-Go Discipline gate (`no-go-discipline` skill, checks N1-N8) before recording any verdict on a row with `claim_type: no_go`, a `bounded_theorem` whose source note names walls/admissions, or an `audited_conditional` whose `verdict_rationale` would name walls. Negative-claim overclaims foreclose investigation paths permanently and require the same scrutiny as positive-claim overclaims. If any N1-N8 check fails on the source note, choose the more conservative non-clean verdict whose `verdict_rationale` reflects the honest narrower claim scope; do not record `audited_clean`, and do not transcribe the source note's inflated wall list into the ledger.
- **Vocabulary is auto-corrected, not adjudicated.** *Forward-looking rule: effective once Cleanup-1 PR lands `scripts/vocab_lint.py`, the `prose_status` schema migration in `apply_audit.py` / `audit_lint.py`, and `docs/repo/controlled_vocabulary.yaml`. Until then, continue with the existing manual vocabulary-correction behavior and do not run nonexistent vocabulary tooling or write `prose_status` / `prose_corrections` to ledger rows — the validator will reject them.* The repo's process vocabulary will be canonical in [`docs/repo/controlled_vocabulary.yaml`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md) (cleanup PR creates the YAML; design is in [`VOCABULARY_HYGIENE_DESIGN.md`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md)). After Cleanup-1, before writing an audit verdict, run `scripts/vocab_lint.py --fix` on the source note under audit. Routine drift (legacy aliases, forbidden filename suffixes, deprecated wording, F-letter finding labels) is rewritten mechanically; this is a normal commit step, never a science verdict. Record what was rewritten in the ledger row's `prose_corrections` field and set `prose_status: auto_corrected`. If `vocab_lint` cannot mechanically rewrite a violation (genuinely new term), set `prose_status: needs_human_vocab_decision` — but **do not** translate this into a non-clean `audit_status`. Physics and prose are separate verdicts. A clean derivation with vocabulary drift lands as `(audit_status: audited_clean, prose_status: auto_corrected)`; a clean derivation that introduces a genuinely new term lands as `(audit_status: audited_clean, prose_status: needs_human_vocab_decision)`. Never assign `audited_renaming` or `audited_conditional` on prose grounds alone.
- If the author family appears to be Codex and the current auditor is Codex, do not let the current context self-ratify a clean result. Restart the claim in a distinct restricted-input sub-agent when sub-agents are available, and record a clean result only as `independence: fresh_context` with a distinct `auditor` identity if `apply_audit.py` accepts it. If no sub-agent is available, skip clean application and report that a non-Codex, human, or fresh-context agent audit is required.
- Do not stop after producing an audit JSON unless the user explicitly asks for a dry run, no-apply, or JSON-only result. If the user asks to "return JSON" as part of an audit-loop task, treat that as the required verdict format and still apply, verify, commit, and push the audit result according to this skill.

## Setup For Each Session

1. Fetch `origin/main`.
2. Create or reuse a clean worktree based on `origin/main`.
3. Run:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

The graph-cycle warning is currently expected. Treat any error as a blocker.

## Clean-Context Guards

- Do not run broad content searches over `docs/audit/data/audit_ledger.json`, `docs/audit/AUDIT_LEDGER.md`, or other audit-history files. Use exact `jq` field extraction for selected rows and dependencies.
- When reading `audit_ledger.json`, extract only operational metadata such as `claim_id`, `note_path`, `runner_path`, statuses, `criticality`, `deps`, `note_hash`, and graph-degree fields. Do not print or inspect `verdict_rationale`, `chain_closure_explanation`, `previous_audits`, `audit_history`, or prior auditor notes.
- File-name listing is allowed when needed, but do not search file contents in audit data/history to find alternate candidate sources or prior conclusions.
- If fresh-context contamination occurs before a verdict is applied, discard the current context's judgment for that claim and restart the claim in a distinct restricted-input sub-agent when sub-agents are available. Do not pass the contamination, prior conclusion, or audit-history text to the sub-agent. If no sub-agent is available, stop before applying any audit and report the contamination.

## Blocked-Row Loop Guard

- If applying a verdict and rerunning the pipeline immediately invalidates that same row, returns it to the ready queue, or creates a dependency-status cycle that cannot be resolved by the audit verdict alone, do not keep retrying the row in the same audit loop.
- Restore the pre-claim generated audit diff for that row, record a session-local blocked/skip entry with the claim id and the exact tooling reason, and continue with the next ready row.
- Do not write an unsupported blocked verdict into the ledger unless `apply_audit.py` provides such a route. Report skipped blocked rows at the end of the loop and require upstream dependency/status repair before retrying them.

## Long-Running Runner / Timeout Guard

- A wall-time timeout, missing stdout, or noncompletion of a runner is not scientific evidence against the claim. Do not apply `audited_conditional`, `audited_failed`, or any other terminal non-clean verdict solely because the runner may need a long compute run.
- When analysis needs runner stdout, use `python3 scripts/cached_runner_output.py <runner_path>` instead of running the runner directly. This reuses a fresh SHA-pinned cache, or writes one if the cache is missing/stale, so later audits and non-audit analysis do not rerun the same expensive computation.
- If the load-bearing step cannot be judged without a long run and there is no completed log, cached certificate, sliced deterministic runner, or independent derivation in the restricted packet, record a session-local `compute_required` skip with the claim id, runner path, timeout/budget used, and the exact artifact needed; then continue with the next ready row.
- Apply a non-clean verdict only when there is a substantive audit reason beyond wall-time noncompletion, such as a completed output mismatch, stale number, unsupported dependency, import/API failure, hard-coded contested premise, or an over-broad claim not supported by completed finite evidence.
- If a prior audit row appears to have used timeout/noncompletion as the primary reason for a terminal verdict, do not treat that prior verdict as settled science. Queue it for policy repair or re-audit under this guard.
- Do not blanket-reset older rows just because the rationale mentions a timeout. If the same rationale contains an independent blocker, re-audit the blocker under restricted inputs; if timeout/noncompletion is the primary or only reason, leave the row pending for compute or policy repair instead of citing it as non-clean science.

## Compute-Limited Backlog Repair

`runner_breakage_inventory.json` lists runners that the audit triage timed out or that exited nonzero. The default pipeline timeout is 60-120s; some load-bearing runners (lattice MC, large eigenvalue, dense sweeps) legitimately need 300-1800s. Treat these as compute-limited, not science-failed (per the Long-Running Runner / Timeout Guard above), and repair them with the canonical batch helper:

```bash
# Refresh a curated list of broken runners with extended timeouts:
python3 scripts/precompute_audit_runners.py \
  --runners scripts/frontier_plaquette_self_consistency.py,scripts/frontier_color_projection_mc.py,...

# Or, for one runner with an ad-hoc longer budget:
python3 scripts/cached_runner_output.py scripts/<runner>.py
```

Per-runner declared timeout (preferred for runners that are persistently slow): add a top-level `AUDIT_TIMEOUT_SEC = <N>` assignment to the runner file. `scripts/runner_cache.runner_timeout_for()` reads this and overrides the default.

After bulk cache refresh, commit `logs/runner-cache/*.txt` and the mechanical `audit_ledger.json` delta together. The full audit pipeline (`docs/audit/scripts/run_pipeline.sh`) will then regenerate `runner_classification.json`, `audit_queue.json`, `effective_status_summary.json`, and `AUDIT_QUEUE.md` against the new cache.

**Refresh propagation**: refreshed cache files land on `main` via PR. After merge:

- The `.github/workflows/audit.yml` nightly cron at `0 6 * * *` UTC automatically runs the pipeline against `main` and auto-commits any refresh deltas as `audit: nightly repair and pipeline refresh (automated) [skip ci]`. **No manual action required.**
- For immediate refresh (skipping the wait for the nightly run), trigger `workflow_dispatch`: `gh workflow run audit.yml` (or via Actions UI). The same auto-commit pattern runs.
- Audit verdicts are **never** auto-minted; the cron only updates classification + queue + load-bearing. Auditors still pick from the refreshed `AUDIT_QUEUE.md` and apply verdicts via `apply_audit.py`.

## Legacy Claim-Type Re-Audits

- `claim_type_backfill_reaudit` rows are migration cleanup under the PR291 regime. Audit the current scoped claim, not the old source-note status prose.
- For critical rows with already confirmed legacy clean cross-confirmation whose summaries predate `claim_type`, a restricted-input re-audit may own the scoped `claim_type` and `claim_scope`; missing `claim_type` in the old summaries is not by itself a cross-confirmation disagreement.
- If the new restricted-input audit changes the actual clean/non-clean verdict, or if `apply_audit.py` records a real cross-confirmation disagreement, follow the normal escalation path.

## Pick The Next Claim

If the user names a candidate file or other constrained selection source, that source is authoritative. After the pipeline, check the exact path exists. If it is absent, stop and report the missing file; do not search for substitutes or fall back to the default queue unless the user explicitly authorizes that fallback.

### Cascade Re-audit Source

Before falling through to the regular queue, check
`docs/audit/data/reaudit_candidates.json`. This is the cascade-resolution
stream for non-clean audited theorem/no-go/open-gate rows whose blocker may
have been repaired after the original audit. The main `candidates` stream
covers rows whose one-hop dependencies have since become retained-grade; the
secondary `runner_drift_candidates` stream covers runner-artifact rows whose
runner hash changed after the audit snapshot.

Process cascade candidates before fresh queue rows, with the same scoped
claim-type filter and the current session's blocked/skip set:

1. Read `docs/audit/data/reaudit_candidates.json`.
2. If `candidates` is non-empty, pick the highest-leverage entry with
   `claim_type` in `{positive_theorem, bounded_theorem, no_go, open_gate}`.
   The producer sorts by criticality, descendants, load-bearing score, and
   claim id.
3. If `candidates` is empty but `runner_drift_candidates` is non-empty, pick
   the highest-leverage entry there with the same `claim_type` filter.
4. Exclude any claim id recorded in the current session's blocked/skip set.
5. If no cascade candidate is eligible, fall through to
   `docs/audit/data/audit_queue.json` and use the default queue rules below.

Use this snippet when useful:

```bash
python3 - <<'PY'
import json
p=json.load(open("docs/audit/data/reaudit_candidates.json"))
for e in p.get("candidates", []) + p.get("runner_drift_candidates", []):
    if e.get("claim_type") in {"positive_theorem","bounded_theorem","no_go","open_gate"}:
        print(e["claim_id"], e["note_path"], e.get("runner_path") or "-")
        break
PY
```

If the snippet prints no candidate, fall through to the regular queue.

`audited_conditional` with `dependency_not_retained` is the expected state
when a downstream theorem lands before its upstream dependencies reach
retained-grade. The cascade-first ordering resolves these naturally as
upstream cleanup lands, instead of letting fresh `unaudited` queue rows starve
now-unblocked downstream conditionals.

### Default queue selection

Default fall-through selection is the highest-priority ready scoped claim:

1. Read `docs/audit/data/audit_queue.json`.
2. Pick the first row with `ready = true`, `audit_status` in `{unaudited, audit_in_progress}`, and `claim_type` in `{positive_theorem, bounded_theorem, no_go, open_gate}`.
3. If the user explicitly says strict queue order, take the top queue row even if `claim_type` is unset.
4. Exclude any claim id recorded in the current session's blocked/skip set by the Blocked-Row Loop Guard.
5. If only `meta` or `decoration` rows remain, process them only when the user explicitly asks for those classes.

### Empty-Queue Refresh

If step (2) finds no eligible row in the current `audit_queue.json` (queue exhausted, or every remaining row excluded by `ready=false` / session-blocked / wrong `claim_type` filters), **refresh the pipeline locally before stopping**. Newly landed runner caches or upstream audit results may have made fresh rows ready since the queue was last regenerated.

Refresh exactly once per session per empty-queue event, in this order:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

Then re-attempt selection (steps 1-5). If the refreshed queue is still empty by the same filters, the audit lane is genuinely caught up — report the empty queue, the refresh attempt, and stop the loop. Do not refresh repeatedly in one session and do not invoke `gh workflow run audit.yml` from inside the audit loop (the CI workflow runs its own pipeline and could race the local one).

The empty-queue refresh exists because runner caches and audit verdicts land continuously; the queue snapshot can lag behind by several commits when the session started. A single local refresh covers the common case where a recent PR (e.g. a compute-limited backlog repair) made dozens of rows newly auditable but the local queue hasn't yet caught up.

Use this snippet when useful:

```bash
python3 - <<'PY'
import json
q=json.load(open("docs/audit/data/audit_queue.json"))["queue"]
for e in q:
    if e.get("ready") and e.get("claim_type") in {"positive_theorem","bounded_theorem","no_go","open_gate"}:
        print(e["claim_id"], e["note_path"], e.get("runner_path") or "-")
        break
PY
```

## Context To Read

For the selected claim, read only:

- source note at `note_path`;
- one-hop dependency notes listed in `docs/audit/data/audit_ledger.json` under `deps`;
- the primary runner, if any;
- current runner output, if the runner can be executed safely;
- `docs/audit/README.md`, `FRESH_LOOK_REQUIREMENTS.md`, `AUDIT_AGENT_PROMPT_TEMPLATE.md`, and `ALGEBRAIC_DECORATION_POLICY.md`.

When writing the verdict, also load `references/nature-grade-rubric.md` from this skill.

Do not use `CLAIMS_TABLE.md`, `PUBLICATION_MATRIX.md`, `ARXIV_DRAFT.md`, or earlier review summaries to bias the verdict.

## Audit Questions

Answer these before choosing a verdict:

- What exact sentence/equation is load-bearing?
- Is the claimed observable the same observable being compared or derived?
- Does the result follow from cited inputs, or is a symbol identity being introduced?
- Are any physical carriers, unit maps, source laws, boundary conditions, sectors, normalizations, or readouts selected without a retained theorem?
- Are dependencies unaudited, open gates, retained-pending-chain, stale, or themselves conditional?
- Does the runner compute the hard bridge, or does it hard-code the contested premise and check consistency afterward?
- Is this an independent theorem, or algebraic decoration of an upstream claim?
- Are numerical values current with the runner and the source note?
- Would a hostile specialist be able to reject the conclusion without making a mistake?
- If the claim is a `no_go`, a wall-naming `bounded_theorem`, or its rationale would cite walls: have at least 5 distinct attack routes against the no-go been considered (N1)? Are the named walls actually independent (N2)? Are any hidden in "bridge context" / "we assume" / "standard QFT" / "registered" prose (N3)? Do cited witness residuals match the claim's residual (N4)? Are "X is not a Y-fact" phrases verified at every named resolution (N5)? Is the "needs new axiom" framing actually a convention-reframe / labeling ratification (N6)? Can a steelman against the no-go be made convincing (N7)? Has a structurally similar prior wall been retired by a mechanism not considered here (N8)? See `no-go-discipline` skill.

## Verdict Rules

Use the audit-lane verdict enum exactly:

- `audited_clean`: derivation closes from the cited inputs; no hidden physical identification; runner checks the load-bearing step or the proof is purely exact algebra over independent retained inputs. Effective status is derived from ledger `claim_type` plus dependency closure, not source-note status prose. `support` is not a claim class, and old support prose neither grants nor blocks retained status after a clean audit.
- `audited_conditional`: depends on an unaudited dependency, open gate, retained-pending-chain row, unratified physical bridge, or an explicit premise not closed by the cited authorities.
- `audited_renaming`: the load-bearing step defines/renames the target quantity or identifies two concepts without derivation.
- `audited_decoration`: exact algebraic corollary with no independent comparator, falsifiability, compression, or new physical content beyond an upstream parent.
- `audited_numerical_match`: result depends on tuned/calibrated input or chosen scale/value rather than a structural theorem.
- `audited_failed`: chain is wrong, stale relative to the runner, mismatches the observable, contradicts dependencies, or does not close on its own terms.

When in doubt, choose the more conservative non-clean verdict.

For claims with `claim_type: no_go`, `bounded_theorem` whose source note names walls/admissions, or any verdict that would record walls in `verdict_rationale`, apply the No-Go Discipline gate (`no-go-discipline` skill, N1-N8) before recording. Any FAIL forbids `audited_clean`; instead, choose the non-clean verdict whose `verdict_rationale` reflects the corrected narrower claim scope. Specifically:

- if N1 fails (fewer than 5 distinct attack routes considered against the no-go), record `audited_conditional` with `notes_for_re_audit_if_any: scope_too_broad — alternative attack routes not exhausted`;
- if N2/N3 fails (walls not independent, or hidden walls promoted), record `audited_conditional` with the collapsed/expanded honest wall list;
- if N4 fails (witness-residual mismatch in cited authorities), record `audited_conditional` with `notes_for_re_audit_if_any: missing_dependency_edge — cited witness residual does not match the claim residual`;
- if N5/N6 fails (over-broad phrasing, or convention-reframe misclassified as new axiom), record `audited_renaming` if the failure is purely scope/framing, or `audited_conditional` with a sharper wall list;
- if N7/N8 fails (convincing steelman exists, or prior-wall retirement mechanism not considered), record `audited_conditional` with `notes_for_re_audit_if_any: scope_too_broad — named alternative not foreclosed`.

See [`docs/ai_methodology/skills/no-go-discipline/SKILL.md`](../no-go-discipline/SKILL.md). The audit lane must not transcribe a source note's inflated no-go into the ledger as `audited_clean` — that cements the overclaim and forecloses investigation paths permanently.

## Required Failure Handoff

For any verdict other than `audited_clean`, make the ledger useful to the physicist who fixes the science. Put this structure inside `verdict_rationale` and keep `chain_closure_explanation` short but specific:

```text
Issue: <exact failed step, stale number, hidden premise, or observable mismatch>.
Why this blocks: <why the conclusion cannot be claimed from current inputs>.
Repair target: <specific theorem, derivation, runner computation, or dependency status needed>.
Claim boundary until fixed: <what may still be safely said>.
```

For `audited_clean`, still explain why the load-bearing step closes and what residual risk remains.

## Conditional Repair Surfacing

For every `audited_conditional` result, make the next repair lane sortable.
Prefix `notes_for_re_audit_if_any` with exactly one repair class:

- `missing_dependency_edge`: a needed source note or authority exists or is
  named, but is not wired as a direct dependency for the audited claim.
- `dependency_not_retained`: a direct dependency exists but is not retained
  grade.
- `missing_bridge_theorem`: the claim needs a new theorem for a physical
  carrier, readout, unit map, boundary condition, sector choice,
  normalization, or observable bridge.
- `scope_too_broad`: a clean bounded core exists, but the current claim scope
  includes an unclosed extension.
- `runner_artifact_issue`: a runner, log, classifier, threshold, import, or
  pass/fail accounting problem blocks closure despite otherwise local scope.
- `compute_required`: closure needs a completed long run, sliced runner,
  cached certificate, or independent derivation.
- `other`: use only when none of the above fits, and state why.

After the class, name the cheapest next repair action, such as adding an
explicit citation/dependency edge, auditing a named dependency first, creating
an open bridge theorem, splitting the clean bounded core from the conditional
extension, or repairing/slicing the runner. Do not repair during the audit
unless the user explicitly asks for repair work.

## Apply The Audit

Create an audit JSON matching `docs/audit/scripts/apply_audit.py`. Returning this JSON to the user is not the end of the task unless they explicitly requested dry-run/no-apply behavior. Required metadata:

- `claim_type`: one of `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`, `decoration`, `meta`.
- `claim_scope`: a short citeable statement of exactly what was audited.
- `auditor`: use a stable string such as `codex-audit-loop`.
- `auditor_family`: use the actual family if known; otherwise use `codex-current`. Do not claim `codex-gpt-5.5` unless that is true for the session.
- `independence`: use `cross_family` for non-Codex-authored claims, `weak` for same-family audits, `strong` for independent human review, `external` for off-project review.

Apply it:

```bash
python3 docs/audit/scripts/apply_audit.py --file /tmp/audit-result.json
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

For critical claims, the first clean audit records `audit_in_progress` and awaits cross-confirmation. That is expected.

`apply_audit.py` is the gate. Critical claims receive two independent audit
passes through the cross-confirmation flow. If those two passes disagree, do
not resolve the disagreement with a single judicial third auditor. Run a
five-judge panel in the same loop using the restricted source packet plus the
full first-audit and second-audit arguments as explicit context. Each judge
must run at the required audit model/reasoning level with a distinct auditor
identity, vote on the full tuple `(sided_with, ratified_verdict,
ratified_claim_type, ratified_load_bearing_step_class)`, and explain errors in
the other position. A majority is at least three matching votes out of five.

After a panel majority, go with the majority only if the majority tuple is
applyable by the audit tooling and the normal gates pass. Apply a representative
judicial JSON for the majority side, rerun the pipeline, strict lint, and
`git diff --check`, then land it as the audit result. If the panel has no
3-of-5 majority, the majority tuple cannot be represented by `apply_audit.py`,
the tooling rejects it, strict lint fails, or the panel majority sides with
neither original audit, open/keep a human-review PR and record the panel vote
breakdown in the PR body or comment. Do not keep retrying individual judges
after a completed five-judge panel.

Only stop for human review when the five-judge panel is unresolved or
unapplyable, the tooling rejects the majority judgment, strict lint fails, or
another hard-rule/exceptional routing case remains after the panel.

If `apply_audit.py` accepts the JSON and `audit_lint.py --strict` passes after the pipeline refresh, land the audit by direct push to `main` for these routine cases:

| Verdict / state | Audit-loop action |
| --- | --- |
| First or second `audited_clean` in the cross-confirmation flow | Direct push to `main` |
| Cross-confirmation disagreement resolved by a five-judge panel majority that confirms an applyable first or second verdict | Direct push to `main` after applying the majority judicial JSON |
| `audited_conditional`, `audited_renaming`, `audited_decoration`, or `audited_numerical_match` | Direct push to `main` |
| `audited_failed` on a non-controversial claim | Direct push to `main` |

Open a PR and flag for human review only when there is an unresolved hard-rule conflict or exceptional routing case:

| Exception | Audit-loop action |
| --- | --- |
| Five-judge panel has no 3-of-5 majority, sides with neither original audit, or produces an unapplyable majority tuple | Open PR; flag for human |
| Cross-confirmation disagreement exists but the five-judge panel cannot be run with the required context/model | Open PR; flag for human |
| `apply_audit.py` rejects the verdict JSON or blocks on a hard rule | Open PR; flag for human |
| `audit_lint.py --strict` fails after applying the verdict | Open PR; flag for human |

## Commit And Push

Review the diff. It should normally touch only:

- `docs/audit/data/audit_ledger.json`;
- `docs/audit/data/effective_status_summary.json`;
- `docs/audit/data/audit_queue.json`;
- `docs/audit/AUDIT_LEDGER.md`;
- `docs/audit/AUDIT_QUEUE.md`;
- possibly generated load-bearing/runner files if the pipeline refreshed them.

Commit:

```bash
git add docs/audit
git commit -m "audit: <claim-id> <verdict>"
```

Before pushing, fetch and confirm `origin/main` is still the parent or rebase cleanly and rerun the pipeline:

```bash
git fetch origin main
git push origin HEAD:main
```

If the push is rejected, fetch/rebase onto `origin/main`, rerun pipeline/lint/diff-check, amend only if it is the same audit commit and no one else has consumed it, then push.

## Loop Control

After each successful direct-main push:

1. Report the claim id, verdict, and one-sentence reason.
2. If time and user intent allow, fetch `origin/main`, refresh the queue, exclude any session-local blocked/skip rows, and start the next claim.
3. Stop if there is an ambiguous independence issue, source-note hash drift that cannot be resolved mechanically, or an audit requiring domain expertise beyond the provided authorities.

For unresolved exception cases listed above, create a branch/PR instead of pushing to `main`, flag the reason for human review in the PR body, and stop the loop until the human decision lands. Do not stop merely because a five-judge panel occurred; stop only if the panel remains unresolved or the tooling/verification gates fail.
