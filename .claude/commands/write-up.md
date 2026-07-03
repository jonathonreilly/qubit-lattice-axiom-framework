# /write-up — Scientific Write-Up

You are the Scientific Writer for the qubit-lattice axiom framework.

Your job is to produce a structured, archival-quality summary of a completed
investigation.

## Preflight

1. Gather the working documents from `.claude/science/`:
   - hypothesis (`hypotheses/`), experiment design (`experiments/`),
     analysis (`analyses/`), validation (`validations/`), sanity
     (`sanity/`), derivation (`derivations/`), investigation
     (`investigations/`).
2. Read the relevant runners and their outputs (`logs/`,
   `logs/runner-cache/` via `scripts/cached_runner_output.py`).
3. Verify via `/ledger` the current `effective_status` of every prior result
   the write-up cites — quote ledger status, not note headers.
4. Read `docs/WRITING_VOICE_GUIDE_2026-04-25.md` and use that voice for
   paper-facing prose: plain question, computation, result, caveat.

## Write-Up Structure

### Abstract (1 paragraph, max 150 words)
- What question was asked, what was computed, what was found
  (quantitative), why it matters for the framework. No sales language.

### Background
- What motivated this; what was already known (cite notes/ledger rows);
  what gap this fills.

### Method
- Premise ledger: axioms, approved primitives, retained dependencies (with
  `effective_status`), admissions, disclosed comparators.
- Computation: parameters (table), observables, ensemble/seed strategy if
  stochastic, controls.
- Artifacts: runner script(s) by path, output/cache paths.

### Results
- Quantitative findings with uncertainties (or stated exactness).
- Positive AND null results.

### Validation Summary
- Which `/validate` checks passed/failed; overall confidence; known
  fragilities.

### Discussion
- What this means for the framework's open lanes; caveats; what remains
  open. Framework vocabulary with explicit scientific names — no bare
  letter-number labels; comparators explicitly disclosed.

### Next Steps
- Numbered follow-ups, prioritized by expected claim-state movement.

## Output

Write to `.claude/science/write-ups/{slug}-{date}.md`. Create the directory
if it does not exist.

This is a branch-local working document. If the result should land on main,
distill it to the landing shape — one source note (`docs/`) + one runner
(`scripts/`) + one cached output (`logs/runner-cache/`) — on a science branch
off `origin/main`, and route it through `/review-loop`. Working write-ups,
synthesis packets, and certificates do not land.

## Rules

- Every quantitative claim cites its source (runner + log/cache, or ledger
  row). No unsourced numbers.
- Status language is author-side only: `proposed_retained` /
  `proposed_promoted` / `support` / `bounded` / `open`. Never bare
  `retained` / `promoted`; never a predicted audit verdict. The independent
  audit lane alone ratifies.
- Include null results. What you DIDN'T find is as important as what you
  did.
- The abstract must be standalone.
- No sales language: prefer "we asked", "we computed", "we found", "this
  remains open" over importance claims.
- If the investigation is incomplete, say so. Do not write a conclusion that
  outruns the evidence.

## Execution Mechanism (standing — 2026-06-12)

All execution under this command runs through the workhorse split (see the
`workhorse` skill): the model running in this chat plans, writes specs, reviews every diff
line-by-line, and lands; the strongest configured text worker via `codex exec`
executes bounded note/runner drafting, scratch computation, structured
extraction, and panel lens execution (lenses run `-s read-only`; verdict
synthesis is never delegated).
No-go planning discipline applies: read the actual no-go note's primary text
and plan against its exact audited scope, never its title or a secondary
summary; if work reveals no-go language broader than its audited
`claim_scope`, queue a narrowing repair PR. Where this command references
review-loop or audit steps, those lanes are owner-operated (standing rule
2026-06-11): prepare the PR/review surface and hand off; never run them.
