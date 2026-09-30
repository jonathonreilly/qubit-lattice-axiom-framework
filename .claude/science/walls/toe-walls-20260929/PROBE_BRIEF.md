# Lane probe brief: find and log every wall

You are probing ONE lane of the qubit-lattice theory-of-everything (TOE)
repository for its walls.

A **wall** is a place where the lane is stuck. The lane keeps failing in the
same way, or it needs an input it cannot derive, or a no-go blocks the next
step. Walls include:
- open derivation obligations;
- named no-go results that block the lane's goal;
- premises that are posited because they could not be derived;
- targets reached only by fitting or tuning.

**A wall is not:** a routine TODO, a pending audit, a typo, or a result
nobody has tried to get.

## Where to look

- **The repository.** It is checked out at
  `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt`
  (current `origin/main`).
  - Front-track notes are in `docs/`. The audit ledger is
    `docs/audit/data/ledger/<xx>/<claim_id>.json`, with fields
    `effective_status` and `audit_status`.
  - Registered open gates are in `docs/audit/data/derivation_obligations.json`
    and the notes named in `docs/KEY_SCIENCE.md`.
  - The axioms' own list of open gates is in
    `docs/MINIMAL_AXIOMS_2026-06-29.md`, section "Open Gates Outside The
    Axioms".
  - Owner decisions parked with wake conditions are in
    `docs/repo/DEFERRED_DECISIONS.md`.
- **Archived notes** are in `archive/notes/`, mapped by `archive/PATHMAP.tsv`.
  They are record without authority, but useful for history.
- **Open pull requests:** `gh pr list --state open --limit 200 --json
  number,title,headRefName`. Many lanes' newest results are in open PRs, for
  example #9363, the TOE viability probes and gravity lane.
- **The owner's project memory**, for lane history (read-only):
  `/Users/jonBridger/.claude/projects/-Users-jonBridger-Projects-Physics-baremetal-probes/memory/`
  (`MEMORY.md` is the index).
- **The viability map:** `docs/TOE_VIABILITY_MAP_WHERE_THE_AXIOMS_ARE_EXPOSED_AND_THE_FASTEST_DECISIVE_TESTS_2026-09-27.md`,
  on the branch `origin/claude/toe-viability-probes-20260927`. Read it with
  `git -C <repo> show origin/claude/toe-viability-probes-20260927:docs/<name>`.

## Method

1. Read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full, and
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
2. Map the lane. Which question does it try to answer for the TOE? What is
   its current best result, and what is its status? Use the notes' claim
   scopes, their audit statuses and their "open", "residual", "wall",
   "no-go", "obligation" and "not shown" sections.
3. List every wall. For each, check whether other lanes or earlier attempts
   already hit it. Where it is the same wall seen from another lane, say
   which.
4. Keep the three columns separate: what the axioms say, what the lane
   supplied, and what was proved.

## Output

Write your answer to the file your prompt names, in exactly this format.

```
# Lane <code>: <lane name> — walls

## Lane map (under 200 words, plain language first)
<what the lane is for, its best current result with status, where it stands>

## Walls

### <code>-W1: <short title>
- Plain: <at most 80 words a smart non-physicist can follow>
- Precise: <the target; what fails; its quantifiers and premises>
- Evidence: <path:line references, notes and PRs>
- Axioms / supplied / proved: <one line each>
- Tried already: <path:line of attempts and what happened>
- Same wall elsewhere: <other lanes, or none>
- Why it matters: <what the TOE cannot do while this stands>
- Cheapest known test or next step: <concrete>
- Severity: blocking / major / minor
- Status: open / priced (equivalent to a named premise) / possibly misframed

(repeat for every wall)

## Walls considered and rejected
<one line each: why it is not a wall, e.g. already solved (path) or routine>
```

Also append one JSON line per wall to the `.jsonl` file your prompt names,
with the keys `id`, `lane`, `title`, `plain`, `severity`, `status`,
`evidence` (a list of paths) and `same_as` (a list of other wall ids or
lane names).

## Rules

- **Do not edit the repository.** Write only your two output files and any
  scratch scripts, in the folder your prompt names.
- **Label claims:**
  - proved: a landed or referee-confirmed note;
  - checked: a test you ran;
  - suggested: an argument not yet checked;
  - reading: an interpretation.
- **Bound your reading.** Use `grep` and `ls` to find the lane's notes; read
  claim scopes, statuses and the open sections. Do not read hundreds of
  notes in full.
- **Be complete about walls, and honest about severity.** Do not invent
  walls to fill the list.
- **Plain language first** in the lane map and in every "Plain" line.
