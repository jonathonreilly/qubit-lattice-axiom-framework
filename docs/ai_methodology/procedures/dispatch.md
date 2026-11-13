# dispatch

A lead hands one frozen piece of work to a worker and gets evidence back. The
lead keeps every judgment; the worker executes and is free to refute. Roles:
`RULES.md` section 4. Models and efforts: the role rows in `SETTINGS.md`.
Nothing here grants standing.

## Use when

- A statement, computation, extraction, mechanical edit or read-only lens is
  frozen: its text will not change while the worker runs.
- Not while the statement's form is still moving (`research`), not to decide
  whether a step is right (`check`), and not for one or two quick reads.

## Takes

- A brief (next section), and one worktree per worker that survives a reboot
  (`lab_ops.py worktree-add`).
- The lead's own derivation of the load-bearing step, at least in sketch,
  where one is possible. Results were strongest when the algebra was worked
  before the brief and weakest when open mathematics was handed over.

## The brief

Every dispatch names:

1. **Target.** The exact statement or task, its consumer, and the worker's
   role: drafting or computation, checker, or read-only lens.
2. **Source revision and premises.** Quote scoped claims and governing text
   inline from the primary source (`RULES.md` 2.8), never from a summary.
3. **Read set.** Exact paths resolved by the lead: about five at most, two
   for a read-only worker. Never "read the ledger" or "read everything".
4. **Allowed paths.** The files it may write and every proper name its
   output may use. An analysis dispatch is read-only outside its output paths.
5. **Expected output.** One deliverable, written to disk as it goes, and a
   short report: commands run, results, uncertainties, files changed.
6. **Verification.** A check that fails if the object is wrong, stated apart
   from the hoped-for result: no pass count, no desired value, no comparison
   target inside the computation that predicts it (`RULES.md` 2.3). Values
   come from the real object at full precision. An honest miss is welcome.
7. **Budget and exits.** The limit, and what to return on a miss: a
   counterexample, an error in the brief, or the exact missing obligation.
8. **External actions.** Commit, push, network and PRs are denied unless
   named. Name the procedures the worker may follow; it runs no `check`,
   `land` or `audit`. Do not ban repository instructions wholesale.

Keep it neutral: a proof sketch is a candidate with its unproved steps
labelled. Mark context "do not copy into files". When an edit touches text
that code reads, list strings that must survive and strings that must go.

## Steps

1. **Freeze.** Write the brief to a file. If it cannot be written, the work
   is not ready to hand over. (Reference: units of work.)
2. **Preflight.** `python3 scripts/lab_ops.py preflight --target <folder>
   --role <role> --model <model> --effort <effort> [--lane <lane>] [--numeric]`.
   A refusal stops the launch; report any required check that cannot run. Launch
   what the machine carries, jobs times one job's peak memory, not a quota.
3. **Lock numerics.** One numeric job per machine: `lab_ops.py numeric-lock
   acquire`, `refresh` before expiry, `release` after the job has stopped.
   (Reference: launch checks.)
4. **Launch** in the background with standard input closed, the prompt read
   from the brief file, and the log and final message captured. Record the
   exact command. (Reference: launch and reliability.)
5. **Confirm.** Say "launched" until the first events show the model and
   effort; compare them with the role's row in `SETTINGS.md` and the target's
   model floor; then say "running". (Reference: launch checks.)
6. **Wait** for the worker's exit or deadline, on the handle your own launch
   returned. Silence, idle local CPU and an empty output file are not a hang.
   Do not poll or match log text: workers echo the prompt. (Reference:
   launch and reliability.)
7. **Salvage** on a tool failure or expired deadline: read status, checkpoint
   what exists, interrupt only your own worker, revalidate what you recover.
   A partial transcript is no result. Relaunch smaller. (Same reference.)
8. **Review** (next section), then commit and push (`RULES.md` section 5).
9. **Resume** only with a neutral prompt: name the hardest remaining
   obligation, try an untried route, log what failed. Whoever launched a
   worker ends it. (Reference: launch checks.)

## Before committing a worker's output

A worker's report is not evidence, and a passing run is necessary, not
sufficient: workers pressed for a result have passed their own rigged gates.

1. Read the whole diff, line by line, against the primary sources.
2. Rerun the load-bearing check yourself and hand-verify the mathematics of
   the central claim. Never trust an echoed log.
3. Hunt each fabrication pattern (Reference: fabrication battery):
   - value from target: the comparison constant sits in the formula that
     predicts it, or a real input is computed and discarded;
   - proxy: a 0/1 or parity stand-in where the real object was required;
   - rounded anchor: a rounded or designed stand-in for an exact value;
   - fitted prefactor: a multi-digit or tidy constant with no derivation;
   - gate that cannot fail: it still passes with a term dropped or perturbed;
   - invented reference: search the repository for every identifier cited;
     no hit means made up. Search for leaked brief wording too;
   - wrong authority: a real quotation from the wrong source, with the check
     pinned to that source. Re-derive each quotation from the governing one.
4. Check what the edit touches: runners that pin the edited sentences
   (search, then rerun them), links (each is a dependency edge), and every
   statement that reads the file, which returns to `argued` (`RULES.md` 1).
5. Confirm the output writes no standing and predicts no check result, and
   that its framing, and your summary of it, match the measured numbers.
6. Fix trivial defects yourself; send substantive ones back in a new brief.

A substantive computation also ships a checker built to refute it: disjoint
machinery, no import of the primary, teeth shown by planted defects it
catches, gates that never encode the wanted outcome. A proof or mechanical
edit gets a proof check or change validation, not a second runner. Where
lead, worker and checker share a model family all of this is mandatory, the
checker works in a separate context from restricted inputs, and the record
says "same family, separate context"; without shown separation it is no
independent check (`RULES.md` 3). Matching prose or hashes show provenance,
not correctness. (Reference: robustness conditions.)

## Ends

When evidence is back with the lead, at one of:

- the statement proved as written, or the output delivered and its
  verification rerun by the lead;
- the statement killed by a counterexample, or the brief shown to be wrong;
- the budget spent, or two successive reductions without closure
  (`SETTINGS.md`, Reductions), with the exact missing obligation returned.

Reviewed output is `argued`; only `check` makes it `checked`.

## Never

- Hand over judgment: selection, synthesis of results, what lands.
- Tell a worker what result to produce, at launch or at resume.
- Let a worker edit a file it does not hold, rewrite shared state, write
  standing, add an axiom or premise class, or land, merge or close a PR.
- Let an analysis worker commit, push or use the network.
- Fill a role below its row in `SETTINGS.md` or the target's model floor, or
  with an image or document tool. Record any substitution.
- Remove a worktree with unpushed content (`lab_ops.py worktree-remove`).

## Step references

Paths are under `docs/ai_methodology/skills/`. Read one only at its step.

| Step | File on `main` | Section: why |
|---|---|---|
| 1 | `physics-loop/references/long-running-execution.md` | Units of work |
| 2, 3, 5, 9 | `workhorse/SKILL.md` | Launch Checks: refusals, lease, resume |
| 4, 6, 7 | `workhorse/SKILL.md` | Host Subagent Launch; External CLI Worker |
| Review 3 | `physics-claim-reviewer/SKILL.md` | Fabrication-Pattern Battery |
| Review 4 | `review-loop/references/AUDIT_COMPATIBILITY.md` | Items 4 and 7 |
| Review, end | `workhorse/SKILL.md` | Robustness Conditions |
