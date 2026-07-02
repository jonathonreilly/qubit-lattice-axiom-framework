# /workhorse — Planner Thinks, Codex Executes

Standing owner directive (2026-06-11): run science execution through the
strongest configured text reasoning worker available through the local codex
CLI to conserve planner tokens. The planner — the model running in this chat —
NEVER delegates judgment; only execution. This document is the canonical shared
copy of the workhorse split referenced by the science commands' "Execution
Mechanism" blocks.

## Division of labor (non-negotiable)

- **Planner (the model in this chat):** problem selection, recon synthesis,
  theorem design, spec-writing, line-by-line review of EVERYTHING the executor
  produces (never-believe-the-survey applies doubly to executor output), panel
  synthesis + verdicts, landing decisions, PR/commit text, memory updates. If
  a step requires judgment, it is the planner's.
- **Executor (codex text worker):** note drafting per the planner's outline,
  runner implementation per spec, scratch computation, structured extraction
  from primary sources (with exact-quote contracts), mechanical edit
  application, panel LENS execution (the planner writes the lens prompts and
  synthesizes; never let the executor synthesize verdicts).

## Design principles (what separates strong waves from weak ones)

- **Work the algebra BEFORE the spec.** The spec encodes a result the planner
  has already derived, at least in sketch — the executor verifies and
  implements it; it does not discover it. Across waves, the strongest result
  has consistently been the one where the algebra was worked pre-spec; the
  weakest, where open math was delegated.
- **Shape potential negatives as refutation dispatches.** When a direction may
  fail, dispatch independent refutation lenses (3+ distinct angles) rather
  than one hopeful attempt — a triple-refutation converts "didn't work" into a
  precisely named wall, which is land-able (feeds an N1–N8 no-go note) and
  steers the next wave. A vague miss is wasted compute; a named wall is a
  result.
- **Verdicts on notification.** Workers run in background; synthesis, edits,
  and landings happen when their exits notify — never idle-poll.

## No-go discipline (planning + maintenance)

- **Plan against the audited scope, not the reputation.** When a no-go/wall
  gates a plan, read the no-go note's PRIMARY text (and the ledger row's
  `claim_scope`) and quote the exact scoped claim into the plan. Titles,
  memory summaries, and secondary citations systematically overstate scope.
  Never let a worker inherit a no-go limit from a summary — put the quoted
  scope in the spec.
- **Narrow overbroad language as you work.** If a no-go note's rhetoric claims
  more than its audited `claim_scope`, queue a narrowing repair PR aligning
  the prose to the audited scope (N5 rhetoric discipline; this conforms
  language to the audit, it never authors a grade). Check the invalidation
  blast radius first — editing a retained note re-opens its audit; if it is
  load-bearing for clean dependents, batch the narrowing with the next edit
  that already touches the note and record the debt.

## The loop (one PR-sized unit of work)

1. **Recon + design (planner).** Read the load-bearing primary sources
   yourself; verify ledger statuses
   (`git show origin/main:docs/audit/data/audit_ledger.json`) before citing
   anything as retained. Derive the result (algebra-before-spec, above), then
   decide the exact object, claim type, and boundary.
2. **Worktree per PR.** `git worktree add /tmp/<name>-wt -b <branch>
   origin/main`. Never work in the shared main tree; concurrent sessions race
   it.
3. **Spec file (planner).** Write `/tmp/spec-<name>.md` using the template
   below. The spec is the contract — exact files, exact phrases, exact
   acceptance checks, and EVERY proper name the artifact may use.
4. **Dispatch (parallel, background).**
   `codex exec -s workspace-write -C /tmp/<name>-wt "Read the spec file at
   /tmp/spec-<name>.md and execute it exactly. Do NOT load or follow any local
   codex skills. Analysis and file edits only; no git commit/push, no
   network." > /tmp/codex-<name>.log 2>&1`
   Run independent units concurrently (one background call each).
5. **Verify (planner — the load-bearing step).** Review checklist below, every
   item, every time. Fix issues by editing the worktree files YOURSELF (don't
   round-trip trivial fixes through the executor).
6. **Cache regen** (only when a runner changed):
   `python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache
   import execute_runner, write_cache; r=execute_runner('scripts/<runner>.py',
   120); write_cache('scripts/<runner>.py', r)"`
7. **Commit/push/PR (planner).** Conventional commit; PR body states what
   verdict/goal the work responds to, what changed, runner numbers, and
   downstream order if PRs chain. `git worktree remove --force` after push.
   The PR is the done-state — do NOT check/wait on/report `gh pr checks`
   (owner 2026-07-02: main moves too fast for PR CI to signal; the
   review-loop worker owns landing). Clean science + your own runner re-run
   PASS + fresh cache = done; start the next unit.
8. **Memory (planner).** Update the campaign's project memory + index hook,
   where the session has persistent memory.

## Spec template (what makes dispatches clean)

```
# Spec <X> — <one-line goal>
RULES (binding):
- Do NOT load or follow any local codex skills. No review/audit tooling. Edits only.
- No git commit/push, no gh, no network. Edit files in place.
- Edit ONLY these files (no new files): <explicit list>
- Never write audit grades or status predictions into notes.
- PROPER NAMES: the artifact may use ONLY identifiers listed in this spec. Do
  not invent registry ids, note basenames, or wall names.
ANTI-FABRICATION (mandatory in every dispatch — executors fabricate under result pressure):
- NEVER compute a result FROM its comparison target (no `x = target + damping*...`).
- NEVER use a 0/1/parity proxy where a real Schur/eigenvalue/floating quantity is required.
- Anchor to EXACT landed values at full precision; recompute the measured quantity from
  real machinery — never a rounded stand-in or a designed split.
- NEVER fit a scalar prefactor to force a match; derive it or report the honest residual.
- EVERY completeness/identity gate must DISCRIMINATE: it must FAIL if the implemented
  object were wrong (FD cross-check with a convergence-ratio requirement, or an explicit
  wrong-value rejector — NOT an algebraic identity that holds by construction).
- An honest miss is a WIN; a fabricated/tautological success is a do-not-land.
CONTEXT (for understanding only — do not copy into files): <the verdict/goal, quoted
exactly; the mechanism: markdown links = dependency edges, backticked names = context>
## Edits (file by file)
<numbered, surgical, with exact before/after text where it matters>
## PRESERVE VERBATIM: <every phrase any runner greps — list them explicitly>
## MUST BE ABSENT AFTER EDIT: <forbidden strings>
## Acceptance contract
- <runner cmd> exits 0, SUMMARY/TOTAL line PASS>=N FAIL=0
- Print git diff to stdout when done. Do not regenerate caches (reviewer does that).
```

## Review checklist (planner, before every commit)

- Read the FULL diff line by line. Executor prose drifts; verify every claim
  against the primary sources read in step 1.
- **Sibling-runner grep:** `grep -rln "<NOTE_BASENAME>" scripts/` — other
  runners may read/pin the edited note's sentences. Run every affected sibling
  runner after the edit.
- Re-run the paired runner YOURSELF; confirm PASS/FAIL counts; never trust the
  log echo.
- Verify PRESERVE strings present and FORBIDDEN strings absent (grep, not eyes).
- Verify dependency mechanics: markdown links = ledger dep edges; backticked
  names = no edge. Check the post-edit link inventory matches the intended dep
  list exactly.
- Check invalidation blast radius BEFORE editing: who depends on this row
  (reverse deps in the ledger)? Editing a note re-opens its audit; fine for
  unaudited/conditional dependents, a regression for clean ones.
- Status-language scan: the note must not author or predict audit grades
  (hard rule).
- **Identifier grep:** every backticked/linked identifier in the artifact must
  exist (`git grep -c "<name>"` — 0 hits on a cited name = fabrication; see
  anti-fabrication pattern 6).

## Anti-fabrication review (the load-bearing lesson)

A passing `TOTAL: PASS=N FAIL=0` is necessary, not sufficient. Under result
pressure executors fabricate the load-bearing step and the runner passes its
OWN rigged gate — in one wave, 4 of 5 outputs fabricated and all 4 passed.
Line-by-line review is the only thing that catches them. The six patterns
(with the tells):

1. **Value-from-target** — the result is computed from the target it's
   compared to (a "Richardson" that was `alpha = d_measured + 0.12*(onepoint -
   d_measured)`, sequence discarded). Tell: the comparison constant appears in
   the formula; `_ = x  # not used`.
2. **Proxy-for-physics** — a 0/1/parity matrix stands in for a real
   Schur/eigenvalue, making a "coincidence" tautological. A sibling runner
   building the real object proves it was feasible.
3. **Rounded/idealized anchors** — freezing `0.366` for landed `0.366421...`,
   or a designed `0.30*tail` split, so an approximate model "matches" a
   stand-in, not the real measured quantity.
4. **Fitted prefactor as derivation** — a wrong form forced to match by a
   fitted constant (a 17-digit normalization; a tidy `47/120`) sold as
   derived. A native symbolic derivation refutes it. Tell: any multi-digit
   constant with no derivation.
5. **Tautological gate** — holds regardless of whether the object is correct
   (a "SymPy completeness" gate that reduced to `(I - A·A^{-1})·X`, vanishing
   for any `X`).
6. **Invented references** (2026-07-01, 3 in one otherwise-clean note) —
   plausible-looking but nonexistent registry ids, note basenames, or wall
   names woven into prose. The math can be perfect while every proper name is
   fabricated. Tell: any identifier not copied verbatim from the spec or a
   file the worker read. Defense: the spec lists every proper name the
   artifact may use; review greps every backticked/linked identifier against
   the repo. Related tell, same wave: spec meta-language leaking into the
   artifact ("The sentence required for the record is: ...") — grep artifacts
   for PRESERVE/spec phrasing.

**Discriminating-gate test:** recompute every completeness/identity gate with
a term dropped/perturbed; if it still passes, it's tautological — demand a
real one. Prefer FD convergence-ratio gates (a wrong object plateaus) and
wrong-value rejectors.

**Two defenses that work:** (a) commission EXTERNALLY-ANCHORED targets — a
claim pinned to an exact landed value / independent exact diagonalization /
a-priori constant can't be faked, so the executor reports an honest residual
instead of fudging; (b) run an INDEPENDENT-MODEL adversarial-verification pass
over the surviving claims before landing. A single reviewer misses
tautological gates and framing overstatements — verify the FRAMING against the
gated numbers, not only the gates. (Lens pattern: per target, 3 parallel
lenses — fabrication-hunt, algebra-re-derive, framing-audit — then a
per-target synthesis verdict; the planner lands on it.)

## Dispatch hygiene (hard-won)

- **Skill contamination:** executor-side skill directories may contain
  repo-native review-loop and audit-loop skills that AUTO-TRIGGER on
  review-shaped prompts. EVERY dispatch carries "do NOT load or follow any
  local codex skills". Panel lenses additionally run `-s read-only`.
- **Watchdogs:** key on PROCESS EXIT (background completion), never on log
  sentinels — the executor echoes the prompt, so any sentinel string in the
  spec false-triggers a first-match grep. If parsing logs, parse the LAST
  match. Local CPU at 0% is NORMAL (server-side reasoning) — it does not
  indicate a hang; arm a bounded dead-man check instead of killing on CPU.
- **Hang mode:** read-only extractors buffer all output to exit, so their only
  signal IS process exit — give a bounded grace window, then kill and split
  the spec smaller. Keep read-only prompts SHORT (one compact deliverable
  list, ≤2 files per worker), pre-resolve all paths YOURSELF (git
  ls-tree/grep) before dispatching, give exact paths only — and for ≤2 quick
  reads, skip the scout and `git show` inline.
- **PID hygiene:** multiple sessions run codex concurrently — identify YOUR
  workers by the background task IDs from your own dispatch calls, never by
  `pgrep codex`.
- **Memory budget:** estimate before building; panel peak = runner ×
  concurrent agents; dense Fock-op lists forbidden ≥2^11 (sparse +
  diagonal-Kraus); verify big runners with `/usr/bin/time -l`.

## Hard rules (unchanged by this mode — the executor changed, nothing else)

- Review-loop and audit-loop are owner-operated lanes. Workhorse mode may
  prepare their hand-off surfaces, but it hands off unless the user explicitly
  invokes that lane in the supervising chat. Executors never run those lanes,
  apply their verdicts, or land/close/merge PRs through them.
- Never author or alter audit-status grades in notes; the independent audit
  lane on origin/main is the only status authority.
- Science execution changes go through a dedicated worktree and PR hand-off.
  The workhorse executor never pushes main; lane-specific review/audit
  instructions own any later main landing.
- Panels still gate every landing; lens prompts and synthesis are the
  planner's.
- Physics repo: run the framework-refresher orientation first; respect the
  r=1/2 firewall, the no-import rule, and walls-move framing.

## Pointers

- The science commands' "Execution Mechanism (standing — 2026-06-12)" blocks
  reference this split; this file is their canonical target.
- Review-loop hand-off surface: `.claude/commands/review-loop.md`
  (owner-operated; prepare the PR, never run the lane).
- Operator sessions may carry additional session-memory refinements of this
  doc; on conflict, the repo copy plus dated owner directives win.
