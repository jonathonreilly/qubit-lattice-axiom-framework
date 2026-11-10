# Science workflow: section map

This file used to hold the rules. They now live in three files beside it:
`RULES.md` (invariants), `SETTINGS.md` (the owner's current choices) and
`PROCEDURES.md` (the six procedures). This map exists so that an older
reference of the form "SCIENCE_WORKFLOW.md section N" still resolves. It adds
no rule and grants no status. Remove it when nothing cites it.

## Where each section went

| Old reference | Now |
|---|---|
| Opening paragraph | `RULES.md`, opening paragraph |
| Section 1, read the task first | `RULES.md` section 4, last bullet |
| Section 2, rule 1, keep claim types apart | `RULES.md` section 1 |
| Section 2, rule 2, premises stay explicit | `RULES.md` section 2, "Premises stay named" |
| Section 2, rule 3, no new axioms without the owner | `RULES.md` section 2, "Mathematics is free; axioms are not" |
| Section 2, rule 4, never fabricate | `RULES.md` section 2, "Never fabricate" |
| Section 2, rule 5, predictions vs fits | `RULES.md` section 2, "Predictions are declared first" |
| Section 2, rule 6, exact claims need exact statements | `RULES.md` section 2, "Exact claims need exact statements" |
| Section 2, rule 7, negative results are graded | `RULES.md` section 2, "Negative results are graded" |
| Section 2, rule 8, independence means a different path | `RULES.md` section 3 |
| Section 2, rule 9, literature first | `RULES.md` section 2, "Search before building"; `SETTINGS.md`, method defaults |
| Section 3, formal verification (Lean) | `RULES.md` section 3 |
| Section 4, current owner settings | `SETTINGS.md` |
| Section 5, research cadence | `SETTINGS.md`, cadence; `RULES.md` sections 1 and 3 |
| Section 6, stages and authority | `RULES.md` section 4; `PROCEDURES.md` |
| Section 7, selecting work | `procedures/research.md`; `SETTINGS.md`, method defaults; `RULES.md` section 6 |
| Section 8, where material belongs | `RULES.md` section 5; `AGENTS.md` |
| Section 9, changing this process | `RULES.md` section 7 |
| Section 10, working as a lab | `RULES.md` sections 3 to 5; `procedures/research.md`, `dispatch.md`, `check.md` and `write.md` |

## Section 4: owner settings

The owner-settings table is `SETTINGS.md`. The landing-review setting that
`skills/review-loop/SKILL.md` cites is its "Landing review" row together with
the "Models by role" table.

## Section 6: shared landing validation

Kept word for word because `skills/review-loop/` and its contract check read
it here. `procedures/land.md` is where the step is carried out.

For authorized backlog integration, a coherent argument may be reviewed as one
frozen unit across cumulative or dependent PRs, preserving each constituent's
source/head provenance and claim disposition. Run focused source, runner and
premise checks per unit, then one full mechanical pipeline, strict lint, and changed-evidence validation on the exact integrated
current-main candidate. Reuse identical successful validation only with
matching input, tool and scope receipts. Grouping confers no blanket approval;
the detailed contract and landing guards live in `skills/review-loop/SKILL.md`.
Drafts stay excluded unless draft triage is explicitly authorized; a
still-draft PR never lands and marking ready is not PASS. Owner-reserved
content stays excluded until released.

## Words that changed

Older files use several status vocabularies. `RULES.md` section 1 has one:
`open`, `argued`, `checked`, `retained`, `refuted`.

| Older word | Standing in `RULES.md` |
|---|---|
| `gap` | `open` |
| `unchecked`; `proposed_retained`, `proposed_promoted`; author support words such as `exact-support`, `bounded-support` | `argued` |
| `implication` | `checked`, naming what it rests on that is not |
| `discharged` | `checked`, with nothing open beneath it |
| "killed" | `refuted` |
| `advance`, `correct-no-advance` | A `right` check with a steering note; not a standing |
| Ledger effective status `retained`, `retained_bounded`, `retained_no_go` | `retained` |
| Ledger `retained_pending_chain` | `checked`, given the row named in its reason |
| Ledger `unaudited`, `audit_in_progress` | Whatever check records give; `argued` if none |
| Ledger `audited_conditional`, `audited_renaming`, `audited_numerical_match` | Not `retained`; `open` where the verdict names an unclosed step |
| Ledger `audited_failed` | `refuted` where the record shows a counterexample, otherwise `open` |
| Ledger `open_gate` | `open` |
| Ledger `meta` | No standing; not a statement |
| Reviewer PASS, runner PASS, landed on `main` | Not standing |

Three older words collide with the ladder and keep their own meaning where
tooling reads them: the ledger's `audited_*` values are verdicts, `open_gate`
is a claim type, and a validation report's `REFUTED` means "did not
reproduce". Tooling that reads the older words keeps reading them until it is
changed together with the files it reads (`RULES.md` section 7).
