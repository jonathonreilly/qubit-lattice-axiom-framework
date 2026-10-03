# Brief: check the night's report against the CURRENT science on main (read-only)

You are one of seven read-only checker workers. The owner asked for this check of the overnight Campaign 8 report "against the current science in the repo, for all sections". Your group of sections is given in your launch message.

## What to check
The report is `SP/c8/FINAL_REPORT.md`. Read only your assigned sections; grep for the headings.

- Lane reports live at `SP/c8/AXX/REPORT.md`. Each ends with ERRATA. Use them for context when a report sentence needs its source.
- SP = /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad

The repo is the git repo at `/Users/jonreilly/Projects/Physics/.claude/worktrees/focused-noyce-9a3983`. Use the ref **origin/main, pinned at b6fda5ae1d**.
- Read files with `git -C <repo> show origin/main:<path>` and list them with `git -C <repo> ls-tree -r --name-only origin/main`.
- Do NOT `git fetch` (seven workers share this repo, so the ref is already fresh). Do not check out, commit, push, or edit any repo file.
- **Axioms (verbatim):** `docs/MINIMAL_AXIOMS_2026-06-29.md`. Quote from there, never from memory.
- **Notes:** about 6,800 notes under `docs/`. Grep them with `git -C <repo> grep -l -i '<term>' origin/main -- docs/` and similar.
- **Ledger (claim status):** follow the procedure in `.claude/commands/ledger.md` on origin/main. It reads the shards with `git archive origin/main docs/audit/data/ledger docs/audit/data/ledger_meta.json docs/audit/data/axiom_premise_nodes.json` in memory.
  - VALID statuses: `retained`, `retained_bounded`, `retained_no_go`.
  - INVALID statuses (never call these retained): `unaudited`, `audited_conditional`, `audited_failed`, `audited_renaming`, `open_gate`.
- **Background only, not authority:** owner memory files under `/Users/jonreilly/.claude/projects/-Users-jonreilly-Projects-Physics/memory/`. The repo on main is the sole status authority.

## For each substantive claim in your sections, give a verdict
- **CONSISTENT.** The repo agrees, or is silent but compatible.
- **ALREADY IN REPO.** A landed note already proves or states this, or a stronger or weaker version. Cite the path and its ledger `effective_status`.
- **CONFLICT.** A landed note or ledger row says otherwise. Quote both sides, with path and status. Say whether the repo row is valid-retained or not.
- **STALE PREMISE.** The report relies on a fact about the repo that is no longer true. Examples: which vacuum the repo currently uses; what is "approved"; what is "unaudited". Verify it on main.
- **REPO SILENT.** The claim is new; nothing on main overlaps.

Also check every claim the report makes ABOUT the repo or the axioms: quoted axiom wording, "approved primitive", "the repo's U(1) role compiler", "unaudited graviton notes", "the repo's current vacuum", PR numbers.

## Rules
- Read-only. Write only your output file.
- No PRs. Do not run the audit pipeline or any review lane; only read the ledger.
- No numerics beyond trivial arithmetic.
- Quote exact text with file paths. Be skeptical: a note's own `Status:` header can be stale, so the ledger row decides.
- The owner's ideas (ticks, moving records, flow, black holes) are instincts, not positions. Never call a beat or heartbeat adopted.
- Never say a possibility is "read".
- Keep it focused. About 40 minutes. Prefer depth on the claims that matter most for the owner's plain-language summary.

## Output
Write `SP/c8/CHECK/<your group id>.md`. If your sandbox blocks file writes, return the full content as your final message; otherwise also return it as your final message. Sections:
1. **Snapshot.** The origin/main SHA you read.
2. **Claims table.** Columns: section · claim (short) · verdict · repo evidence (path · ledger status · exact quote) · suggested change to the plain-language summary (exact replacement text, or "none").
3. **Top 3 issues** for the owner's plain-language summary, most important first.
4. **Repo results the report should mention but does not.** Landed science on main that bears directly on your sections, with paths and statuses.
