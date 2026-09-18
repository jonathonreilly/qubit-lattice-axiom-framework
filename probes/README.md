# Science probes — tasking location, work log and strategy

This directory is the repository's job list for executable science work that needs volume rather than judgment: re-execution,
mutation censuses, refuter re-runs, searches for counterexamples, parameter scans, provenance audits and independent falsifier
implementations. The owner assigns workers (any model, any number); each worker runs tasks, checks its own log, and pushes it.
Nothing here changes notes, runners or packs, and nothing here is a claim. Logs are evidence addresses for later blocks.

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
6. Commit and push as in section 0. A `hit: true` log is also reported by opening an issue titled `probe HIT: <task_id>` with the log path and your review sentence. Do not "fix" anything you find.
7. Requirements: Python 3.12 with numpy, scipy, sympy; `gh` authenticated for `P:` tasks. Searches are single-process CPU jobs: run several in parallel with different seeds.

## 2. Task types and what each buys
| type | id prefix | tier | what a HIT means | who |
|---|---|---|---|---|
| runner re-execution | `R:` | 0 | a FAIL, or a TOTAL line differing from the pinned cache | any worker; one pass per week |
| mutation census | `M:` | 0 | a mutation that fails no family or the wrong family | any worker |
| PR re-execution | `P:` | 0 | on an open science PR: a FAIL, a census mismatch, a runner that does not run (isolated worktree) | any worker; every open PR, weekly |
| lints | `L:` | 0 | any lint error on the checkout | any worker; daily |
| refuter re-run | `F:` | 1 | an inconsistency reported by a refuting control | any worker (controls live on PR branches: see `J:refuter-rerun-new-seeds`) |
| search | `S:` | 1 | a counterexample to an open conjecture of blocks 32–33 (a site whose cheapest tree costs more than 0; a tight sibling pair; a non-admissible restriction; `c* > 1`) | any worker; broad seed and box sweeps — the best return per CPU-hour |
| scan | `X:` | 1 | none; the value is the table (threshold locations on every weight line; the `1/|m|²` and `c(β)` grids; long plane runs) | any worker; fill the grids stated in `what` |
| judgment | `J:` | 2 | a falsifier that fires; an unsourced number; a refuter inconsistency; a disagreeing re-implementation | capable models; the return is a committed script plus numbers, never a verdict |

## 3. Strategy
- Tier 0 first and continuously: it is cheap and it turns every open PR into something independently executed on another machine, which the review loop can cite.
- Tier 1 searches next, at volume: one `S:` hit changes a theorem's status; no hits at scale are recorded evidence the harvest reports.
- Tier 1 scans fill tables the notes left open; each log is one point of a grid stated in the task.
- Tier 2 for capable workers: one note at a time, one script, one summary line; a `HIT` there is the most valuable thing this directory can produce.

## 4. Judgment tasks (`J:`)
Create `probes/work/<stub>/<script>.py`; it must print a final line starting with `SUMMARY:` and, if it finds something, a line starting with `HIT:`. Run it through `run_probe`: `python3 probes/run_probe.py J:<task> --worker <name> --review "..." --extra "python3 probes/work/<stub>/<script>.py"`. The check refuses a judgment log whose script is not committed.

## 5. Harvest
`python3 probes/harvest.py` prints runs, hits and failures per task and every HIT with its review sentence. The supervisor or the owner reads it; a confirmed hit becomes the input of a block.

## 6. Extending the catalog
Add a task to `probes/tasks/<file>.json` (id, type, lane, tier, command with `{SEED} {SECONDS} {A} {B} {L} {EXTRA}` placeholders, `hit_pattern`, `parse`, `what`), then `python3 probes/generate_tasks.py`. Controls of a lane that live on a PR branch: `git show origin/<branch>:<path> > probes/lib/<name>.py`, make it self-contained, and reference it. Counts at the last generation are printed by the generator.
