# Wall attack brief

You are attacking ONE wall of the qubit-lattice theory-of-everything (TOE)
repository. The goal is to get past it, or to show exactly what passing it
would cost. This follows the repository's exercise skill, compressed.

## Setup

- **The repository.** It is checked out at
  `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt`
  (current main). Never edit it; write only in the scratch folder your
  prompt names.
- **The wall's entry.** It is in the lane file your prompt names, which
  gives the wall's plain and precise statements and its evidence.
- **Read first:** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full, and
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. Say at the top
  of your report that you read them.

## Steps

1. **Check the wall is real.** Open its evidence. Is it stated correctly? Is
   it already solved somewhere? Search `docs/`, open PRs (`gh pr list
   --state open --limit 200`), and `archive/`. If it is misstated or
   solved, say so with paths and stop there.
2. **Restate it in two versions.**
   - Plainly: at most 100 words, for a smart non-physicist.
   - Precisely: the target, its quantifiers and premises, what counts as
     passing, and what does not.
3. **Find the load-bearing premises.** List only the premises the wall
   actually rests on, each with path:line. For each, give:
   - its kind: axiom, primitive, supplied model, method, reading or hidden;
   - what happens if it is wrong;
   - whether it was already tested;
   - the cheapest test.
4. **Routes.** Give two or three routes from materially different
   approaches.
   - At least one from outside the lane's own vocabulary: how another field
     gets past this kind of wall, with a precise citation.
   - One that asks whether the wall is misframed, and what cheaper question
     would replace it.

   For each route give:
   - the object and mechanism;
   - the premise it drops or changes;
   - what you would have to believe for it to work;
   - the first concrete artifact: a lemma with its proof skeleton, a
     construction, a computation, a falsifier, or an exact missing
     obligation;
   - its cost;
   - what it would change.
5. **Run the cheapest decisive test** within about 45 minutes of work.
   - Pre-register its pass and fail readings in your scratch folder before
     running it.
   - Write the script there, run it, and record the result.
   - If no route can be tested in that time, say why, and name the smallest
     test that would decide the best route.
6. **Try to kill your own routes.** Does a route assume its conclusion,
   contradict a landed result, repeat an earlier attempt, or end at a lemma
   as hard as the wall itself? That last case is "blocked-equivalent", not
   progress. Give each route a verdict: survives, wounded (name the gap) or
   dead (give the reason).

## Report

Write it to the file your prompt names, in this format, under 900 words.

```
# Attack on <wall id>: <title>

Read: <refresher surfaces and the key notes read>

## Verdict in plain words (3-5 sentences)
<what the wall is, whether this attack moved it, and what it would take>

## The wall (checked)
- Plain: ...
- Precise: ...
- Real? <yes / misstated / already solved, with paths>

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |

## Test run
- Pre-registered: <pass and fail readings>
- Script: <path>
- Result: <numbers>
- Reading: <what it moved, if anything>

## Outcome
One of: PASSED (route found; say which, and at what cost) /
PRICED (the wall is equivalent to a named premise; give the argument and its
label) / MISFRAMED (with the cheaper question) / STANDS (with the best route
and its first artifact).

## Claims and labels
<every substantive claim, labelled proved, checked, suggested or reading>
```

## Rules

- Label every claim:
  - **proved:** a landed or referee-confirmed note, with its path;
  - **checked:** a test you ran;
  - **suggested:** an argument not yet checked;
  - **reading:** an interpretation.
- Never claim the wall is solved without a proof, a decisive runner, or a
  decisive no-go.
- Literature can suggest templates, but it is never proof here. Cite
  precisely.
- Plain language first.

## Campaign context (added by the supervisor, 2026-09-29)

- **Walls folder.** W = `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls`.
- **Your wall.** Your wall is one distinct TOE wall `T<nn>` in `W/clusters.py`. It groups one or more lane walls that the lane probes logged today. Each member's full entry is in its lane file, `W/L<nn>_<name>.md`, under the heading `### <member id>`. The `.jsonl` next to each file has one line per wall.
  - Treat the members as one wall.
  - If a member does not belong with the others, say so.
- **Sibling walls.** Many walls cite each other (`same_as`). Stay on yours, and name any sibling that your route would also move.
- **The gravity wall (T64) was exercised today.** The packet is at `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-wall-finite-records-20260929/` (`SUMMARY.md` first). Reuse it where it bears on your wall; do not redo it.
- **Branch-only sources.** The viability map and probes 1–21 are on branch `origin/claude/toe-viability-probes-20260927` (PR #9363). Read them with `git -C W/../main_wt show origin/claude/toe-viability-probes-20260927:docs/<name>`.
- **Output.**
  - The report goes to `W/attacks/T<nn>.md`.
  - Scratch files go in `W/attacks/T<nn>_scratch/`.
  - Also write `W/attacks/T<nn>.json` with these keys:
    - `id`
    - `outcome`: one of PASSED, PRICED, MISFRAMED or STANDS
    - `plain`: 2–3 plain sentences
    - `best_route`: one line
    - `test`: one line saying what ran and what it gave
    - `price`: the named premise, if PRICED; otherwise ""
    - `cheaper_question`: if MISFRAMED; otherwise ""
- **Provenance.** You are Claude Sonnet 5.5, the same vendor family as the supervisor (Opus 5.5). Say so in the report's header line. Your checks are same-family checks, not independent referees.
- **Final message.** Reply with one line only: `T<nn>: <OUTCOME> — <one-sentence verdict>`.
