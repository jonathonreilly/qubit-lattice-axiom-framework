# repair

Fix a defect that a check, an audit or a landing hold named, at its source,
and hand the statement back to be checked again. A repair changes source and
never a record. Whatever the repairer believes, the repaired statement is
`argued` (`RULES.md` section 1) until `check` or `audit` runs again.

## Use when

- A check or audit record says `wrong` and names the failing step or the
  counterexample.
- Prose, a title or a summary claims more than the statement it cites
  (`RULES.md` 2.8). Narrow the prose; do not work around the mismatch.
- A check or audit could not run: malformed output, timeout, failed
  transaction, missing registration. That is an incident, not a finding.
  Repair the tool, never the statement.
- A landing review held a PR (`land.md`, Ends). The hold comment is the
  authority for that repair. Answer each finding with a new commit on the
  PR's branch, and say in the commit or the PR which finding each commit
  answers. Where the hold asks for something that a later `SETTINGS.md` row
  made optional, cite that row instead of supplying it.
- Not to settle a disagreement between checkers (`RULES.md` section 3), and
  not for a statement that nobody has checked or held.

## Takes

- The exact defect, quoted from its record with the record's identity: for
  landed work the record on current `origin/main`, for unlanded work the
  check record on the target branch that still counts, for a held PR the
  hold comment on that PR. A stale local copy, a generated prompt or a
  summary authorizes nothing.
- The statements that read the defective one. Know the list before the
  first edit: each returns to `argued`.
- The scope asked for: source only, which is the default, or a drain that
  also asks for `land` and `audit`.

## Steps

1. **Start clean.** A dedicated worktree (`lab_ops.py worktree-add`) at
   current `origin/main`, or on the target branch for unlanded work. Keep
   incident files as provenance and never commit them.
2. **Inventory and route.** List every candidate and give each exactly one
   route: source repair, tool repair, wait for a check in progress, a fresh
   checker, or not actionable with the reason. An item without a route is an
   unfinished inventory. (`science_fix_loop.py --dry-run`; reference:
   inventory, route table.)
3. **Validate the authority.** A source edit needs a record that matches
   its source field by field: `origin/main`, the target branch head, or the
   PR head that a hold names. An invalidated, archived or rejected record is
   advice only. Malformed checker output is never an instruction.
   (`science_fix_loop.py --handoff-file`, `--from-archived`.)
4. **Reproduce first.** Show the defect on that source. If `main` already
   settles it, make no edit and report "settled on main" with the
   evidence. Reproduce a tool failure before editing a tool. (Reference:
   inventory.)
5. **Weigh the edit.** An edit to a `checked` or `retained` statement reopens
   everything that reads it. For a wording defect, batch the fix with the
   next edit that already touches the file and record the debt. (Reference:
   narrowing.)
6. **Fix narrowly.** Make the smallest honest change to source or runner. If
   the step cannot be closed, narrow the statement to what the argument
   supports, or leave it `open` with the failure on record. A repair that
   needs new mathematics goes to `research`; a frozen piece goes to a worker,
   who edits only while the lead commits. (`dispatch.md`.)
7. **Tool repairs** change tooling and add a regression test. They never
   touch the statement's source. The same failure with the same fingerprint
   is a tool defect: fix it once instead of spending more checkers.
   (Reference: route table, dispatch work.)
8. **Verify.** Run the statement's own harness and tests, then apply the
   lead's review in `dispatch.md` to any worker output.
9. **Look at `main` again** before publishing. If the statement became
   `checked` or `retained` there since the work forked, defer to `main` and
   stop. (`science_fix_loop.py` does this itself.)
10. **Hand over.** Remove generated outputs, stage intended paths only, push,
    open the PR and name the statements to recheck. Fix mechanical
    non-conformance first. Scope, proof content, dependency intent and runner
    logic belong to the checker. (`science_fix_loop.py`; reference:
    hand-over.)
11. **In a drain**, repeat from step 2 after each landing and each new audit,
    and keep independent items moving while one is stuck. Repair workers,
    checkers and auditors share one machine pool. (Reference: drain loop.)

## Ends

Each item ends at one of:

- a source fix on a pushed branch, the statement `argued`, and a named
  request to recheck it;
- no edit, and a justified request to recheck: settled on `main`, or the
  failure belonged to one checker session and a fresh one is needed;
- the statement narrowed, or left `open` with the failed routes logged;
- a tool fix with its regression test.

A drain ends when every item has one of these, or when the stated budget is
spent. Report counts by route, PR links, what awaits recheck, recurring
fingerprints and the exact remaining blocker. Hard, open and disputed items
are honest outcomes. Report them separately, never as success.

## Never

- Write, edit or predict a check or audit record, or call a repair `checked`
  or `retained`. Review of the fix does not replace the recheck.
- Add an axiom, primitive, fitted input, hidden premise or wider scope to
  make a defect go away (`RULES.md` section 2).
- Read a timeout, a skip or malformed output as a finding about the science,
  or write a placeholder result for it.
- Edit a downstream statement to hide that it reads an unchecked one. Repair
  or check the cheapest blocking upstream statement instead.
- Publish an interrupted worker's partial edits as a finished PR. Preserve
  them for recovery.
- Start `land` or `audit` on a source-only request (`RULES.md` section 4),
  reuse an old audit campaign's working directory, or promote a draft that
  is not this task's own.
- Retry an identical incident before its fingerprint or the source changes.

## Step references

Paths are under `docs/ai_methodology/skills/`. Read one only at its step.

| Step | File on `main` | Section: why |
|---|---|---|
| 2, 3, 4 | `science-fix-loop/SKILL.md` | Build the complete repair inventory |
| 2, 7 | `science-fix-loop/SKILL.md` | Canonical route table |
| 5 | `workhorse/SKILL.md` | No-Go And Narrowing Discipline |
| 6, 7 | `science-fix-loop/SKILL.md` | Dispatch work |
| 10 | `../REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` | Mechanical conformance |
| 10 | `review-loop/references/AUDIT_COMPATIBILITY.md` | Items 4 and 7 |
| 11 | `science-fix-loop/SKILL.md` | Drain loop; Completion |
| any | `../../audit/SCIENCE_FIX_LOOP.md` | Script outcomes and recovery |
