# land

Put reviewed work on `main`. The lander freezes one unit, obtains an
independent read of its complete final source, runs the integration checks on
the exact candidate for current `main`, and lands it. Landing admits honestly
scoped work. It certifies nothing and changes no standing (`RULES.md`
section 1). Reviewers are the landing-reviewer rows in `SETTINGS.md`.

## Use when

- The owner or a lead asks for a named PR, branch or set of PRs to go to
  `main`, or to be reviewed without landing (review only).
- Not to decide a step (`check`), certify (`audit`) or mend (`repair`).

## Takes

- The request: target, focus, iteration cap (default five), and whether it is
  review only. No named target or set means ask; a drain is never the default.
- A unit: one coherent argument in one PR or several dependent PRs, each with
  its number, head commit, declared base, merge base and original delta.
- No drafts, and no owner-reserved content or anything a descendant inherits
  from it (`docs/repo/DEFERRED_DECISIONS.md`), until the owner releases it.
- Every published or outside statement the unit reads must be `checked`;
  otherwise the unit waits or is narrowed to what does not read it.

## Steps

1. **Scope.** Resolve the target first. For a set, run
   `scripts/review_loop_backlog_inventory.py`; its `ready` label is a fact
   about the base branch only. Try the smallest existing unit that stands on
   current `main` before widening; a citation or filename match is a routing
   clue, not a dependency. Never relabel a claim, duplicate an owner or hide a
   reader to make a unit stand alone. Widening is a recorded decision.
2. **Freeze.** Map every source path and claim of every constituent to carried
   unchanged, narrowed, superseded, rejected or deferred, with its final path
   and hash or its reason and recovery location. Include deleted and inherited
   content. Unmapped content blocks the unit. Ancestry, titles, file counts
   and hashes prove no coverage. Check the record with `review_receipt.py`.
3. **Pre-fix mechanics only.** The lander may repair link targets, field
   presence and enum validity, strip author-written audit outputs, and run
   `scripts/vocab_lint.py --fix`, `py_compile` and the diff checks. Scope,
   proof, runner logic and whether an edge is intended are the reviewer's.
4. **Independent read.** One reviewer per unit, independent as `RULES.md`
   section 3 defines. With no other provider, use a separate restricted
   context and label it so; if separation cannot be shown, hold. The reviewer
   reads the complete changed argument and its premises, applies every
   matching lens in one pass, and reports what is material: mathematical
   errors, unsupported physical or quantified conclusions, lost source, and
   evidence that does not reproduce or test the decisive claim. It re-derives
   each changed formula, constant and expected value by a path sharing no
   implementation, mutates each decisive check to see it fail, rebuilds the
   proof-obligation graph, and inventories every imported value. Read the
   registry sources before calling anything a premise or import. A negative
   claim also gets the obstruction questions of `check`. Escalate only an
   unresolved mathematical or premise question, disagreement or failed
   decisive control, with its evidence, to the escalation row. Uncertainty
   that matters to a stated result is never left for audit.
5. **Fix by narrowing.** The lander or author, never the reviewer, makes the
   narrowest honest fix: correct a verified error; cut the claim to what the
   artifact shows; land the supported part and keep the rest with its open
   obligation named; keep a meaningful negative result as a scoped obstruction
   or a failed search (`RULES.md` section 2, rule 6). Where note, runner, log
   and table disagree, weaken the strongest. Never cover a missing step with
   prose. Leave nits, unevidenced findings and gaps needing new derivation.
6. **Accept and freeze.** A unit is ready only when the reviewer that wrote
   the findings accepts the final source in the same session (no session, no
   landing) and the lander freezes heads, reviewed commits and tree, base,
   interacting files, map, inputs, findings and session. A moved head or
   changed byte, premise, input or interaction reopens only the affected part
   and its dependents; unrelated movement of `main` reopens nothing.
7. **Integrate.** In one clean worktree on fresh `origin/main`, apply each
   unit's reviewed source commits once, bottom-up. Never check out a whole
   file from a stale head over a path `main` has changed: merge three ways and
   confirm `main`'s own changes survive. A source conflict or new cross-unit
   interaction returns the unit to its reviewer. The lander resolves only the
   generated citation manifest, by regenerating it.
8. **Gate once.** Run the pipeline, strict lint, changed-evidence check and
   the three diff checks once on the exact candidate. Reuse a result only for
   an identical base, tree, command, tools and inputs. Where affected rows
   hold live audit judgments, read the invalidation set first: cosmetic churn
   that resets them, or an unreviewed claim that they are unaffected, does not
   land. Evidence a statement needs is committed, not left in a PR body. Then
   restore generated audit outputs. On failure land nothing, keep the log and
   retry units singly in dependency order without guessing a culprit.
9. **Push.** Re-verify every frozen head, that `main` is the gated base and
   that the tree is the gated tree, then run the landing loop in the
   `LANDING.md` reference. It pushes the candidate and proves the landed
   commit is contained in `origin/main`. If `main` moved, rebuild and gate
   again. Write on each carried PR what it carries, what it left out and where
   that is kept. The owner has decided a landed PR should show as merged
   (`SETTINGS.md`, PR state); the loop and its contract check change first.
10. **Close out.** Check on `main` that each PR's carried content matches its
    map; containment alone is not coverage. Run the salvage pass before
    closing anything unmerged, hygiene and tooling PRs included; close it with
    the reason and keep its branch. Delete a head branch only when all it
    holds is on `main` or kept elsewhere, its head equals the frozen head, and
    no open PR uses it as base: retarget dependents first and confirm they
    stay open. A failed retarget never justifies closing unreviewed content.
11. **Report** at the end and on material change (`RULES.md` section 6).

## Ends

- Landed: on `main`, each carried PR naming what it carries (step 9).
- Held: the PR stays open with the exact obligation or changed input named.
- Not landed: the PR is closed with the reason and its branch is kept.
- Review only: stops after step 6, or after step 8 on an isolated copy.

## Never

- Grant standing; write, carry or recommend an audit verdict or status; run
  the audit worker; ship a generated ledger, queue or status table.
- Land a draft, owner-reserved content, or anything outside the request.
- Let the lander or author accept its own fix, a new session confirm one, or
  a reviewer edit the source or change GitHub state.
- Add an axiom, primitive, premise or theory vocabulary (`RULES.md`
  section 2, rule 2); force-push; replay a gate result on a moved `main`;
  hand-merge a generated file.
- Restamp evidence, rerun science to change a label, pad a certificate or
  invent route coverage; report a check that could not run as not run.
- Fill a reviewer role below its row in `SETTINGS.md` without the owner.

## Records

- The unit record, reviewer report and findings, pushed where the next
  session can read them (`RULES.md` section 5).
- On each PR: the map summary, the reviewer's actual provider, model and
  effort, the gate base and tree, and the landed commit.
- A check record, filed under `check`, for each independent derivation the
  reviewer completed. That record, not the landing, moves standing.
- Open findings in `docs/repo/ACTIVE_REVIEW_QUEUE.md`.

## Step references

`AM/` is `docs/ai_methodology/`; `SK/` is `AM/skills/review-loop/`.

| Step | Read at that step, at this file's revision | For |
|---|---|---|
| 1, 3 | `SK/references/REVIEW_SETUP.md` | base, changed set, pre-fix list |
| 1, 7, 9 | `SK/references/LANDING.md` | sets, worktrees, batches, push loop |
| 2, 6 | `SK/references/REVIEW_UNITS.md` | map, reuse, `main` advances |
| 2, 6 | `SK/references/UNIT_RECEIPT.md` | record schema for the checker |
| 3, 5 | `AM/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` | one cure per defect class |
| 4 | `SK/references/SCIENCE_LENSES.md` | lens triggers, prompt, findings |
| 4 | `AM/skills/PRIMITIVE_REGISTRY_CHECK.md` | premise or import judgment |
| 4, 8 | `SK/references/AUDIT_COMPATIBILITY.md` | audit guards, hard gates |
| 5, 11 | `SK/references/FIXES_AND_REPORTING.md` | fix policy, checks, report |
| 8 | `SK/references/COMBINED_VALIDATION.md` | gate commands, isolated copy |
| 10 | `SK/SKILL.md`, Model And Tool Boundary | branch and dependent-PR rules |
| 10 | `SK/references/SALVAGE.md` | salvage pass before any close |
| any | `SK/references/OPERATIONS.md` | archive, checkout pool, child heads |
