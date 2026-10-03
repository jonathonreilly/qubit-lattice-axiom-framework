# Brief: review the repo's work on TIME (read-only)

The owner asked: "there is a lot of work on time in the repo - review it all. we had derivations that forced it from prior smaller axiom sets etc".

You are one of six read-only reviewers. Each reviewer has one theme, given in your launch message. Together you cover the repo's work on time: emergent time, the single clock, the arrow, ticks and minimum time, Lorentz/relativity, clocks and rates, and the archived and intake history.

## Where things are
- SP = /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- **Repo:** the git repo at `/Users/jonreilly/Projects/Physics/.claude/worktrees/focused-noyce-9a3983`, ref **origin/main = b6fda5ae1d**.
  - Read files with `git -C <repo> show origin/main:<path>`.
  - Do NOT fetch, check out, commit, push or edit anything in the repo.
- **Inventories (use these instead of listing the tree yourself):**
  - `SP/c8/all_files.txt`: every tracked path on origin/main.
  - `SP/c8/time_files2.txt`: 572 paths whose names suggest time. They include false friends; for example, TRANSFER and HAMILTONIAN often have nothing to do with time.
  - Your theme may need notes whose names do not match. Find those with a targeted `git grep -l` (see "Load" below).
- **Current axioms, verbatim:** `docs/MINIMAL_AXIOMS_2026-06-29.md` (the 2026-06-29 foundation reset, with owner-approved edits on 2026-08-05 and 2026-08-13).
- **Axiom history and owner approvals:** `docs/audit/AXIOM_MINIMALITY_POLICY.md`. Approved primitives: `docs/audit/data/axiom_premise_nodes.json`. Parked decisions: `docs/repo/DEFERRED_DECISIONS.md`.
- **Ledger (claim status):**
  - Follow `.claude/commands/ledger.md`: read the shards in memory with `git archive origin/main docs/audit/data/ledger docs/audit/data/ledger_meta.json docs/audit/data/axiom_premise_nodes.json`.
  - At b6fda5ae1d no row is retained-grade: 4960 rows are unaudited and 376 are meta. Report each note's `effective_status` anyway, and never call anything "retained".
  - A note's own Status header can be stale; the ledger decides.
- **`archive/`** has no claim authority ("Nothing under archive/ is a claim surface"). Treat it as history only. The same holds for `archive_unlanded/`, `docs/historic_intake/` and `docs/work_history/` unless the ledger says otherwise.

## The question for each note in your theme
1. **What does it say about time?** Give a one-line claim.
2. **From which axiom set or premises?** The owner says several derivations "forced" time from earlier, smaller axiom sets. Identify which axiom text the note used. Is it the pre-2026-06-29 wording (for example the earlier Lattice / Quantum / Record wording, the A1/A2 numbering, a Hamiltonian-bearing axiom), the 2026-06-29 four axioms, or later edits? Quote the premise text the note itself states.
3. **Forced, derived, or supplied?** Was time (or the clock, signature, arrow, tick) forced or derived there, or put in as a premise? Quote the note's own claim scope or boundary.
4. **Does it still hold under the current four axioms?** Choose one:
   - **SURVIVES**: the premises are still axiom text or approved primitives.
   - **CONDITIONAL**: it now rests on supplied premises.
   - **SUPERSEDED**: a later note or an axiom edit removed a premise it needs.
   - **NEEDS RE-CHECK**: it quotes old axiom text and the dependence is unclear.

   Say why, with the quote.
5. **Does it bear on the owner's current thinking?**
   - The owner's instincts, which are explorations, not positions, and must never be recorded as adopted: records form at set ticks; ticks are "a basic unit and hence alike"; records move at most one site per tick.
   - The night's results (`SP/c8/FINAL_REPORT.md`, sections 3, 5 and 15):
     - with uniform ticks no count is needed;
     - a law-level tick is global;
     - only the chances per tick can follow gravity carried by the possibilities;
     - "one tick = one edge in form" is the approved kinetic-isotropy primitive, and record tick = that tick is an open gate on main;
     - an upper bound τ < a/c holds if one site per tick bounds all influence;
     - a new observation, not yet checked against the repo: if records must never outrun light, then τ ≥ a/c, so τ = a/c would be the smallest such tick.

   Flag any repo note that already has these, contradicts them, or settles them.

## Rules
- Read-only. Write only your output file. No PRs, no audit or review lanes, no ledger edits, no numerics beyond trivial arithmetic.
- Quote exact text with paths. Be skeptical of titles: read the claim scope and boundary sections.
- Never say a possibility is "read". Never call a beat or heartbeat adopted.
- **Load.** This machine has 8 GB. Before any repo-wide `git grep`, check `uptime`; if the 1-minute load is above 10, wait by doing reading instead, then retry. Prefer `git show` of specific files and targeted greps over loops of repo-wide greps.
- Time box: about 45 minutes. Depth over breadth. Rank notes by how load-bearing they are for "time is forced or derived". You need not read all 400 notes: triage by title and claim scope, read the important ones in full, and list the rest briefly.

## Output: `SP/c8/TIME/<your id>.md`
If your sandbox blocks the write, return the full content as your final message; otherwise also return it.
1. **Snapshot.** The origin/main SHA you read.
2. **Map.** A table with columns: path · date · ledger status · axiom set used · claim about time (short) · forced / derived / supplied · status now (SURVIVES / CONDITIONAL / SUPERSEDED / NEEDS RE-CHECK) · key quote.
3. **The derivation chains.** What forced what, step by step, with the premises each step used, and which link breaks or survives under the current axioms.
4. **Bearing on the owner's tick thinking.** Agrees, contradicts, already has it, or settles it, with quotes.
5. **Top findings.** At most 5, in plain language for a non-specialist owner.
