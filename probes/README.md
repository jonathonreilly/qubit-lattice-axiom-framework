# Science probes — tasking location, work log and strategy

This directory is the repository's job list for executable science work that needs volume rather than judgment: re-execution,
mutation censuses, refuter re-runs, searches for counterexamples, parameter scans, provenance audits and independent falsifier
implementations. The owner assigns workers (any model, any number); each worker runs tasks, checks its own log, and pushes it.
Nothing here changes notes, runners or packs, and nothing here is a claim. Logs are evidence addresses for later blocks.

## Kickoff: you were pointed at this branch and told nothing else
You need no number, no name and no task list, and you must not pick tasks by hand: work is checked out in units through an atomic claim on the remote (`probes/claim.py`), so any number of workers can run at once without doing the same thing twice. **Do not run `git checkout`, `git pull` or `git commit` in the directory you were started in** (other workers may share it); everything below happens in private directories the tools create for you.

**A. Any thinking setting up to high: run the mechanical worker.** One line, from anywhere inside any checkout or clone of this repository:
```
git fetch origin ai/probes && B=$(mktemp -d ~/.probe-workers-boot.XXXXXX) && for f in claim work_loop; do git show FETCH_HEAD:probes/$f.py > $B/$f.py; done && (nohup python3 $B/work_loop.py --model <your-model-name> > $B/loop.log 2>&1 &) ; echo "log: $B/loop.log"
```
It takes a free slot on the machine, makes its own private worktree (`~/.probe-workers/<repo>/slot-<k>`, about one gigabyte of disk per slot), and then repeats: claim a unit, run it through `run_probe.py` (every log self-checked), commit the logs, push every ten minutes, release the claims. Unit kinds are drawn at random with weights (open-PR re-executions most often), so nothing starves: re-execution of every open PR's runners, runner re-executions against the pinned caches, mutation censuses, seeded refuter controls, the scan grids (threshold lines, the sphere tables, the long plane runs), counterexample searches (thousands of half-hour units: it will not run out). Leave it running and look at the log every 10 to 15 minutes. A runner that fails because a file it reads is gone is triaged `stale` by the loop itself (a `STALE` line; nothing for you to do). **A line starting `ATTENTION` is your real job.** It names a log with a HIT or a failed self-check. Read that log and the `.txt` beside it (inside the slot worktree) and the task's `what`, then record your triage on the log: `python3 probes/check_log.py <log.json> --reviewer <your worker name> --verdict science|false-positive|machine --triage-note "<one concrete sentence>"`, and commit it with the next push (`git add logs/probes` in the slot worktree is done by the loop). `false-positive` = the task's pattern fired on something that is not a failure (say which text matched); `machine` = a missing package, a timeout, a full disk; `science` = the run shows what the task calls a HIT. **Open an issue only for `science`**, only after `gh issue list --search "<task_id> in:title"` shows none (add a comment to the existing one otherwise), titled `probe HIT: <task_id>`, with the log path, the finder's review sentence and the HIT lines. One issue per task, never one per run. Fix nothing. The loop commits failing logs on purpose: that is how a failing runner becomes visible, and it gets exactly one second opinion from another worker.

**B. Maximum (extended) thinking: work judgment units instead.**
```
git fetch origin ai/probes && B=$(mktemp -d ~/.probe-workers-boot.XXXXXX) && git show FETCH_HEAD:probes/claim.py > $B/claim.py && python3 $B/claim.py next --kind J --model <your-model-name>
```
This claims one judgment unit and creates a private worktree for it. Units come in this order: **confirmations and referee reports** of what other workers claimed, then **derivations** (the open problems of the programme: section 8), then the checking work. Confirmations of hits other workers logged (an independent reproduction with different machinery; the claim tool never gives you a hit found by your own model family, which is why `--model` matters; one confirmation per defect per PR), then **attacks**, one per open PR per pattern, in the order of their yield so far: (g) a proof step verified literally by brute force at small sizes, (a) witness realizability, (b) the same test on both sides of a separation claim, then (d) quantifier scope, (e) sampled evidence, (f) normalizations; then **falsifier** implementations, **provenance** audits, and last the notes already on main. The claim prints `KNOWN HITS ON THIS PR` when there are any: re-finding one of those is a wasted unit, and `SUMMARY: pattern has no purchase on this note` is a valid, cheap result. It prints `UNIT`, `TASK`, `WORKER`, `WORKTREE` and the task. `cd` to that worktree and do everything there, following sections 0, 1 and 4; when the log says `CHECK PASS`, commit `logs/probes` and `probes/work` and run `python3 probes/claim.py finish <unit>` (it pushes, releases the claim and removes the worktree). Then claim the next one. If you cannot finish, `python3 probes/claim.py release <unit>`. If you do not know your thinking setting, do A. A judgment hit is reported like any other: triage it yourself as `science` only when your script demonstrates the defect, and open ONE issue per task.

**Owner's view:** `python3 probes/claim.py status` in an up-to-date `ai/probes` checkout prints units by kind (total, done, claimed, free) and every live claim with its holder and age. A claim expires after 8 hours, so a dead worker blocks nothing for long. Hand-running `P:`, `R:`, `M:`, `F:`, `S:` or per-PR `J:` tasks outside the claim tools is what causes duplicate work: do not. Scans (`X:`) and the generic `J:` tasks are still run by hand (sections 1 and 4); duplicates there are harmless.

## 0. Where your work lands (read this twice)
- **Branch:** `ai/probes` only. It is cut from `main` and never merged into `main`. Never push to any other branch.
- **Logs:** `logs/probes/<task_id>/<worker>__<git-sha8>__<utc>.json` and the same name `.txt` (full stdout). `run_probe.py` writes them; you never write them by hand.
- **Your scripts (judgment tasks only):** `probes/work/<stub>/<name>.py`, where `<stub>` is a short name of the note or PR you are working on. Commit them together with their log.
- **Nothing else.** Do not edit anything under `docs/`, `scripts/`, `.claude/`, `probes/lib/` or `probes/tasks/`. If a library script is wrong, say so in an issue.
- **Commit only** `logs/probes/` and `probes/work/`: `git add logs/probes probes/work && git commit -m "probe: <task_id> <worker>" && git pull --rebase && git push origin ai/probes`.

## 1. Worker protocol (every task)
1. `git fetch origin && git checkout ai/probes && git pull --rebase origin ai/probes`.
2. Choose a task id from `probes/TASKS.json` (human list: `probes/TASKS.md`). Read its `what` field: it says what the task tests, what counts as a HIT, and what to vary.
3. Run it: `python3 probes/run_probe.py <task_id> --worker <name> --model <model> [--seed N] [--minutes M] [--box AxBxL] [--extra "..."] --review "<one sentence>"`.
   `P:` tasks run through their own script instead: `python3 probes/run_pr_branch.py <pr-number> --worker <name> --review "..."`.
4. **Check your own log.** `run_probe.py` runs `probes/check_log.py` on the log at once; the last line must be `CHECK PASS`. If it says `CHECK FAIL`, read the findings: a run that did not finish (non-zero exit), a summary line the parser did not find, a review sentence missing, a judgment script not committed, a TOTAL line differing from the pinned cache. Fix the cause (wrong arguments, an incomplete run, a missing `--review`) and run again, or discard the log. Never commit a `CHECK FAIL` log.
5. **The review sentence** (`--review`) is your own reading of the output, written after looking at it: what it shows and whether it matches the task's `what`. One sentence, concrete ("climb reached 3/4 at seed 7, no value above 1"; "TOTAL matches the cache, 53/0"). A log without it fails the check. You may add it after the run: `python3 probes/check_log.py <log.json> --review "..."`.
6. Commit and push as in section 0. A `hit: true` log is triaged before anyone is told: `python3 probes/check_log.py <log.json> --reviewer <name> --verdict science|false-positive|machine --triage-note "..."`. Only a `science` verdict becomes an issue titled `probe HIT: <task_id>`, one per task (search first, comment on the existing one otherwise), with the log path, the review sentence and the HIT lines. Do not "fix" anything you find. Failed self-checks are committed too, with a `machine` or `science` triage.
7. Requirements: Python 3.11 or later with numpy, scipy, sympy; `gh` authenticated for `P:` tasks. Searches are single-process CPU jobs: run several in parallel with different seeds.

## 2. Task types and what each buys
| type | id prefix | tier | what a HIT means | who |
|---|---|---|---|---|
| runner re-execution | `R:` | 0 | a FAIL, or a TOTAL line differing from the pinned cache | any worker; one pass per week |
| mutation census | `M:` | 0 | a mutation that fails no family or the wrong family | any worker |
| PR re-execution | `P:` | 0 | on an open science PR: a FAIL, a census mismatch, a runner that does not run (isolated worktree) | any worker; every open PR, weekly |
| lints | `L:` | 0 | any lint error on the checkout | any worker; daily |
| refuter re-run | `F:` | 1 | an inconsistency reported by a refuting control | any worker; the two seeded controls under `probes/lib/` (blocks 27 and 30) take `--seed`; other controls live on PR branches (see `J:refuter-rerun-new-seeds`) |
| search | `S:` | 1 | a counterexample to an open conjecture of blocks 32–33 (a site whose cheapest tree costs more than 0; a tight sibling pair; a non-admissible restriction; `c* > 1`) | any worker; broad seed and box sweeps — the best return per CPU-hour |
| scan | `X:` | 1 | none; the value is the table (threshold locations on every weight line; the `1/|m|²` and `c(β)` grids; long plane runs) | the work loop claims every point of a task's `grid`; run by hand only points outside it |
| judgment | `J:` | 2 | a confirmed hit; a defect an attack script demonstrates; a falsifier that fires; an executed number that disagrees with its control output | maximum-thinking workers through `claim.py next --kind J`; per open PR: `J:attack`, `J:falsifier`, `J:provenance`; per logged hit: `J:confirm` (derived from the logs, never listed). The return is a committed script plus numbers, never a verdict on the physics |

## 3. Strategy
- Tier 0 first and continuously: it is cheap and it turns every open PR into something independently executed on another machine, which the review loop can cite.
- Tier 1 searches next, at volume: one `S:` hit changes a theorem's status; no hits at scale are recorded evidence the harvest reports.
- Tier 1 scans fill tables the notes left open; each log is one point of a grid stated in the task.
- Tier 2 for capable workers: one note at a time, one script, one summary line; a `HIT` there is the most valuable thing this directory can produce.

## 4. Judgment tasks (`J:`)
Create `probes/work/<stub>/<script>.py`; it must print a final line starting with `SUMMARY:` and, if it finds something, a line starting with `HIT:`. Run it through `run_probe`: `python3 probes/run_probe.py J:<task> --worker <name> --review "..." --extra "python3 probes/work/<stub>/<script>.py"`. The check refuses a judgment log whose script is not committed.

## 5. Harvest
`python3 probes/harvest.py` prints runs by kind, hits grouped by triage verdict (untriaged first, then science, then pattern false positives for the supervisor to fix) and the runners that fail on current main with no passing log (repository hygiene). `python3 probes/harvest.py --by-pr` prints one line per open PR: re-execution, falsifier, attack, provenance, confirmations. A hit becomes the input of a block or a corrigendum only after a `science` triage and, for judgment and search hits, an independent confirmation. Corrigenda on PR branches are written by the supervisor or the owner, never by probe workers.

## 6. Extending the catalog
Add a task to `probes/tasks/<file>.json` (id, type, lane, tier, command with `{SEED} {SECONDS} {A} {B} {L} {EXTRA}` placeholders, `hit_pattern`, `parse`, `what`), then `python3 probes/generate_tasks.py`. Controls of a lane that live on a PR branch: `git show origin/<branch>:<path> > probes/lib/<name>.py`, make it self-contained, and reference it. Counts at the last generation are printed by the generator.

## 7. Batch mode (a manual tool; the work loop of the Kickoff section replaces it for normal operation)
One command runs a shard of the mechanical tasks and writes one checked log per task:
`python3 probes/run_batch.py --type R --shard 3/40 --worker <name> --review "<sentence about the shard: machine, python version>" --skip-done 7`.
Shard `k/n` takes every n-th task of that type; `--skip-done D` skips tasks with a passing, hit-free log younger than D days by any worker, so many workers can share the 3177 re-executions without coordination (pick distinct shards, or the same shard on a different day). The last line is `BATCH: ran= pass= fail= hits= skipped=`; commit `logs/probes` when it finishes. `--type M` runs the mutation censuses the same way; `--type F --seed <s>` the seeded refuter controls.


## 8. Derivations: the science itself
Everything above checks work that exists. `J:derive:<problem>:a<k>` units are the open problems of the research programme, stated precisely in `probes/tasks/derivations.json`: each is attempted independently by several workers (independent attempts are wanted here, unlike everywhere else), and every attempt that claims a proof, a counterexample or a new exact partial result is refereed line by line by a worker of another model family before the supervisor looks at it. An attempt is `probes/work/derive/<problem>/<worker>/ATTEMPT.md` (numbered steps marked PROVED, CHECKED or ASSUMED; the first failing step if the route fails) plus `check.py` (exact arithmetic for every finite claim). A precise account of where a route fails is a result. Nothing here is a claim of the repository until the supervisor or the owner turns a refereed attempt into a block with its own runner, note and review. Current problems: the tight-sibling lemma (ordering threshold 4165 to 453), the repair of block 17's chessboard constant, the response kernel of the formation law (what replaces the Green-function kernel of the gravity node when records form), the direction-diffusion theorem, memory loss on the infinite plane, counting beyond the union bound, the no-memory region, the static law against value-dependent orders, and what each formation clause does to the three-dimensional law.
