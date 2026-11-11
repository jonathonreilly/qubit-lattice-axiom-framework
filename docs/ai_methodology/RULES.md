# Rules

This program builds and tests a candidate theory of everything from four
axioms. Whether any candidate succeeds is an open question. These rules exist
to keep the record true, keep the work recoverable, and keep the owner's
attention for the decisions only the owner can make. They supply no physics
and grant no standing. Optimize for obligations closed and for evidence that
discriminates, never for favorable verdicts or for counts of notes, PRs or
passes.

## 1. Statements and standing

The unit of record is a **statement**: one claim with its quantifiers, its
domain and the premises it reads. Its kind is one of: definition or
construction, theorem, obstruction (a theorem that rules out an explicitly
quantified family), computation with stated uncertainty, prediction,
comparison or fit, conjecture.

Standing is computed from records. Nobody writes it by hand.

| Standing | Means | Comes from |
|---|---|---|
| `open` | Stated, with no argument | |
| `argued` | An argument or computation exists and has not been checked here | Its author, or a published source |
| `checked` | An independent check of this exact text found it right | A check record (section 3) |
| `retained` | Formal audit of this text and of everything it reads | The audit path only |
| `refuted` | A counterexample to the statement as written | A check record |

- Standing binds to content. Editing a statement, or anything it reads,
  returns it to `argued` until it is checked again.
- A check that finds a failing step, but no counterexample, returns the
  statement to `open` and keeps the failure on record.
- A statement is no stronger than the weakest thing it reads. A `checked`
  theorem resting on an `argued` lemma is checked given that lemma; say so.
- A conditional theorem proves an implication, not that its hypotheses hold in
  the world. A checked formal statement is not its physical identification.
- Axioms and approved primitives are named premises. They carry no standing
  and need none; how a statement uses them is still judged. Context that is
  not a claim has no standing and cannot sit inside a `retained` closure.
- `retained` is the audit ledger's computed grade (`retained`,
  `retained_bounded`, `retained_no_go`). The ledger's `audited_*` values are
  verdicts, not standing.
- Older files use other words. `SCIENCE_WORKFLOW.md` maps them, and a file a
  validator reads keeps the words that validator requires.
- Standing is neither location nor mechanics. Being on `main` means a change
  was reviewed for honest scope and clean integration. A runner or pipeline
  pass means code ran. Neither changes standing, and no title, summary, label
  or status file can.
- A candidate is a connected chain of statements with its open obligations
  named. Calling it established needs every statement in the chain `retained`
  and its empirical comparisons declared in advance.

## 2. Evidence

1. **Premises stay named.** Supplied dynamics, observable identifications,
   selectors and empirical values are premises until derived. A definition or
   a formalization derives nothing.
2. **Mathematics is free; axioms are not.** New definitions, lemmas, theorems
   and proofs from stated premises are welcome and add no axiom. Adopting a
   framework axiom or physical primitive is the owner's decision alone.
3. **Never fabricate.** No invented log, number or pass. No prefactor tuned to
   a comparison target. A test's expected value is justified independently of
   the code it tests.
4. **Predictions are not fits.** Keep predictions apart from calibration,
   fitted inputs and post hoc matches. Declare comparison criteria and
   uncertainty before looking at the result where possible; disclose prior
   exposure when not.
5. **Exact claims need exact statements.** Domain, quantifiers, edge cases and
   a proof or exhaustive certificate. Numerical agreement proves no general
   theorem.
6. **Negative results are graded.** A failed search reports what was tried and
   rules out nothing. An obstruction is a theorem about an explicitly
   quantified family. Underdetermination needs witnesses, or a proof under
   matching premises. Failed routes, spent budgets and failure to imagine a
   counterexample are not evidence of impossibility. Equally, wanting a result
   is not evidence that a route to it exists: a blocker is a dated record with
   an exact scope, neither terminal nor presumed removable.
7. **Search before building.** Search the repo, open PRs and the literature
   for the statement and the method. Record the search once where the next
   session will find it, including a search that found nothing. Credit authors
   by name. Using a published result means verifying it: build on it at once
   as `argued` and check it in order of load. A citation, or a source calling
   its result proved, carries no weight. Novelty counts neither for nor
   against.
8. **Say no more than the statement.** Titles, summaries and reports claim
   what the cited statement claims and nothing wider. Plan against the primary
   text and its scope, never against a reputation or a memory of it.

## 3. Checks

- A check is independent when it reaches the load-bearing step by a different
  derivation or implementation, from the raw artifacts, without the author's
  conclusion, in a session outside the author's lineage, on another provider
  where one is available. Re-running the same calculation is not a check; two
  results traced to one expected constant are one path; a role name or a
  second agent is not independence. A lead's review of work it briefed is a
  self-check.
- A check attacks premises, domains, normalization and physical
  identification, not prose. It records `right`, `wrong` (with the failing step
  or counterexample) or `undecided`, what it read, the path it took, and its
  provider, model and effort.
- Disagreement is recorded. Rank and majority do not settle whether a step is
  right. The audit path resolves a split between its seats with a recorded
  panel; that belongs to `procedures/audit.md` and licenses nothing elsewhere.
- Check where it pays: before other work builds heavily on a step, above all
  a bridge that fixes an observable, dynamics, symmetry or normalization; at
  every interface between parts; at assembly; and early when a result matches
  a target unexpectedly well. Do not check note by note.
- Lean is for a named risk: a subtle domain, a long chain, hard edge cases, a
  heavily reused lemma. `sorry`, admitted lemmas and axioms that assert the
  conclusion discharge nothing. Record revision, statement and hypotheses,
  toolchain and dependency versions, checker output and axioms used, and
  confirm the formal statement is the claim. A pending formalization is shown
  downstream and blocks only what reads it. A provider's Lean-verified theorem
  may be cited with its exact statement, assumptions and provenance; it covers
  nothing beyond that statement.
- Audit is the publication-grade check: fresh context, restricted evidence,
  the whole dependency closure, its own verdict vocabulary. It runs only when
  the owner asks and is the only source of `retained`. Deferring it never
  permits a known false claim, an unlabelled assumption or fabricated evidence
  on `main`.

## 4. Authority

| Who | Decides | Never |
|---|---|---|
| Owner | Axioms and primitives, public statements, spending, pace, audits, these rules | Is asked to pick between scientific forks |
| Target lead | Parts, interfaces, budgets, which route gets the next budget | Settles by rank whether a step is right |
| Author | What to attempt inside its task | Certifies, lands or grades its own work |
| Worker | Nothing beyond its dispatch; it may refute the brief | Edits a file it does not hold |
| Checker | Its check record, which it pushes | Checks its own lineage; edits what it checks; merges, closes or labels a PR |
| Lander | Whether a reviewed change lands, within the requested scope | Grants standing |
| Auditor | Audit records | Repairs what it audits |

- A scientific fork gets probes, each with its decisive outcome stated first,
  not a question to the owner. Record the choice, the reason, the evidence
  that would reverse it and the date.
- Something only a person can do is a request that names what it blocks. Other
  work continues.
- Unattended sessions may read, compute, commit, push to their own or their
  target's branch, and open PRs. They do not merge to `main` outside the
  landing procedure, force-push a shared branch, post outside the repository
  or edit axioms.
- A public claim needs one clean document, an independent line-by-line check
  of its whole chain, and the owner's approval of the exact text. A post to an
  outside project carries only a checked error or a checked proof that helps
  it, with the same approval. Credit by name everyone whose work helped.
- A procedure is not permission to widen the task. A request to review rules
  or procedures starts no campaign, drain or audit. Report real conflicts; do
  not invent approval gates.

## 5. State

- `origin/main` holds rules, science and audit records. A target's working
  state is its folder on its pushed branch. Nothing else is state: session
  logs, memories, planning notes and old summaries are retrieval aids.
- One writer per file. A lead holds a file by a lease it commits and pushes;
  git decides who was first. Workers return evidence to their lead.
- Push at every stop. Unpushed work does not exist for anyone else. Commits
  carry `Provenance: <provider>/<model>/<effort> <session>` for the session
  that produced the content, and for both when a lead commits a worker's
  output. It records who did the work and claims nothing about its quality.
- A handover is complete when a fresh session on any provider can state the
  hardest open obligation and the next action from the pushed branch alone.
- Summaries are computed, not written (`lab_ops.py status`).
- Science and rules reach `main` only through `land`, from a PR. Audit
  records and generated pipeline refreshes are written to `main` by their own
  tools and by nothing else. Whether a PR landed is read from its landing
  record, never guessed from its state (`SETTINGS.md`, PR state).
- Stage intended paths only. Regenerate derived files with their owning tool;
  never copy generated files from a moving `main` into an older branch. On
  failure, preserve dirty or unpushed work and report where it is.

## 6. Progress

Report the closures since the last report, meaning critical-path obligations
that became `checked` or `refuted`, and the named ones still `open` or
`argued`. A right step that makes nothing smaller closes nothing. An author
never counts its own closure. A budget stop with a dated log of the routes
tried is an honest result. A frontier target with no critical path reports
its concrete changes instead. Never report a percentage of completion. Notes,
lanes, PRs and passes written are not progress.

## 7. Changing these rules

- A rule exists to prevent a named failure. Each change states the defect, a
  realistic case it decides differently, how it will be measured, and the
  result that reverts it.
- What a script can check, a script checks. Prose is for judgment. Where a
  rule is enforced mechanically, code and prose change together.
- One home per rule. Other files point to it and none restate it. A copy
  outside this repository exists only as an installed artifact that a tool
  writes and checks; nobody edits one by hand.
- Budgets: this file 200 lines, `AGENTS.md` 30, a procedure's core 150 with
  its mechanics in scripts. Adding past a budget means removing something.
- Settings carry a date. Each campaign ends with one short retrospective: for
  each process change in force, what was measured and whether it stays.
  Revert by PR what did not help.
- Platform instructions are outside this repository. Report conflicts with
  them; never claim to override them.
