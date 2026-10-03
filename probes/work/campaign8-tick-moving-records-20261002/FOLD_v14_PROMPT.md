You are the fold-in editor for the Campaign 8 report. Your task is to apply the repo-consistency check's corrections to the report draft, producing version v14. This is plain-language editing only: add no new science.

SP = /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad

## Files
- **Draft body:** `SP/c8/MORNING_DRAFT.md` (v13).
- **One-page summary:** `SP/c8/MORNING_SUMMARY_DRAFT.md`.
- **Assembled report:** `SP/c8/FINAL_REPORT.md`. It is built by `SP/c8/assemble_final.py` as title + summary + the draft from "## How to read this" onward. The checkers quoted FINAL_REPORT.md; the same text lives in the two draft files, so edit the drafts and rebuild.
- **Checker reports:** `SP/c8/CHECK/G1.md` to `G7.md`. Each has a claims table with a "suggested change" column, exact replacement texts, and "Top 3 issues". The replacement texts are in G1 §2a (E1–E12), G3 §2b (R-A to R-N), and inline in the tables of the others.
- **Coordinator findings:** entries K2–K17 at the end of `SP/c8/LOG.md`.

Before editing, make backups: `MORNING_DRAFT_v13_pre_check.md` and `MORNING_SUMMARY_DRAFT_v13_pre_check.md`, both in `SP/c8/`.

## What to apply
1. **Which checker suggestions to apply.**
   - Apply every suggested replacement text whose verdict is one of:
     - CONFLICT;
     - STALE PREMISE;
     - overbroad or too broad;
     - needs a proviso, scope or premise;
     - adds needed repo credit ("ALREADY IN REPO" where the report presents the result as new).
   - Rules in item 3 override the checkers.
   - Optional suggestions: apply them only when they add a needed premise or credit in one sentence or less. Skip pure cross-references, and skip extra quotes of note titles.
   - Repo credits must say "unaudited" (nothing on main is retained). Cite notes in words, not file paths, except where the checker text already uses a short name.
2. **Merging.** Where two checkers rewrite the same sentence, merge them into one sentence that carries both corrections. Never stack two parentheticals with the same content.
3. **Coordinator rulings.** These override the checkers wherever they differ.
   a. **Item 1 of the summary (the hard limit).** Replace it with:
      "**1. A hard limit on motion (exact, for the premises listed).** Suppose a change is reversible, reaches only next-door sites in one tick, uses one qubit per site with sites combined the ordinary (not the fermionic) way, and treats every site and turn of the grid exactly alike on every tick, with each site's possibilities turning exactly as the grid turns (your Q3). Then nothing can move under it: no record it carries, no light, no matter wave. Something has to give.
      - **Your Q3 does the work.** The repo's archived census of the simplest ticks (Clifford ticks; July, no claim authority) finds the same limit when possibilities turn with the grid. But when the turns move places and leave the possibilities alone, it finds next-door ticks that spread content, and those treat some possibilities differently from others. New tonight: the proof for every reversible next-door tick, not only the simplest ones."
      In §3's first bullet, make the matching premise edits (G1 E1) and the archive credit (G1 R1, R2; LOG K17) in the body's register.
   b. **Decision 13 is parked.** The parking registry `docs/repo/DEFERRED_DECISIONS.md` §4 covers it: the Qubit-domain enlargement, with standing default "M₂(ℂ) stands as postulated". Its preamble says not to list a parked item among standing decisions in campaign records.
      - Remove (13) from "The decisions that matter most".
      - In the full list, replace decision 13's text with: "13. **Parked.** More room per place touches the parked Qubit-domain entry in the deferred-decisions registry, whose standing default is one qubit per place. Work proceeds under that default; a lane that needs more room carries it as a named supplied premise."
      - Elsewhere, keep findings that say a route needs more room per place, but change any pointer "(decision 13)" to "(a named supplied premise; decision 13 is parked)".
      - Do not phrase it as a question to the owner anywhere.
   c. **Add decision 7 to "The decisions that matter most"**, as: "**(7)** "Records are permanent": should it mean "never destroyed, may move" (needed for records that step), and do you want that as axiom wording, or kept as your reading, as now?" In the full list, decision 7 takes G7's D7 replacement text.
   d. **The summary's "Minimum tick" bullet** becomes: "- **Minimum tick.** Your approved primitive already says one tick is one edge "in form". Nothing tonight derives a smallest tick; what follows is a longest one: if nothing may outrun one site per tick and light goes equally fast every way, the tick must be shorter than light's time to cross a grid step, divided by √3. If the record tick were the primitive's tick (main lists that tie as an open gate), light would outrun records on the diagonals. That is fine in the record-tick shape, where light is not held to one site per tick, but not if one site per tick is to limit everything."
      Full decision 18 becomes: "18. **What a tick means.** Is "records form at set ticks" a physical statement or bookkeeping? If physical, something must keep the count: either a hidden counter that is not a record (the axioms say "A state is a configuration of records"), or the records themselves, as an ever-growing front of fresh records (an archived July note shows a repeating round needs one or the other). And is the record tick your primitive's "one tick is one edge in form" (an open gate on main), or shorter?"
      Headline (18) becomes: "**(18)** Is "records form at set ticks" physical or bookkeeping (if physical, what keeps the count), and is the record tick your primitive's "one tick = one edge"?"
      Also apply G2's P3k and S4d texts in §5 and §4 where they differ from the summary.
   e. **Decision 17.**
      - Headline: "**(17)** If light-like matter uses a painted sign pattern, under which reading of the turns? Under yours (Q3, exact turns) the pattern costs half the turns; under the repo's (turns up to a local phase) it keeps all 24. Neutral matter with two internal parts that turn with the grid is a lead under study; it needs two internal states per place."
      - Full list: make the same correction inside the longer text.
   f. **Q4 (equal odds).** Wherever it appears, call it "your reading of 'No possibility is privileged'". Add once, in "How to read this": "Readings of Qubit's second sentence at the level of the law sit in a parked registry entry, so tonight carries Q4 as a named supplied premise." Do not ask the owner about it.
   g. **"How to read this", Status bullet.** Append: "A repo-consistency check (seven read-only checkers, 3 October) compared every section with main at b6fda5ae1d. Nothing on main is currently retained (all 5,336 ledger rows are unaudited; formal audit is deferred), so "already in the repo" always means an unaudited note, and nothing tonight conflicts with a settled result."
   h. **Unadopted-premises bullet.** Use G7's H2 replacement, including Q2 (the film has no final state). Use G7's H3 and H4 additions.
   i. **Closing line.** Remove "*Final review round of A36, A37 and this report in progress.*".
   j. **Swap-step dependence.** In §11 add G7's S7 "Not redone" bullet. In §9 add one line saying the sealing and capture results assume the swap step and need redoing for push or flow steps (A37 errata).
   k. **Wording rules.**
      - Replace "empty site" / "empty neighbour" (meaning a site with no record) with "site with no record" / "neighbour with no record" everywhere (G1 E5). Search the whole draft and summary, not only the cited lines; leave "empty space" (a region) alone.
      - Never write that a possibility is "read", "readable" or "asked". Never present anything as adopted. Never imply a beat or heartbeat. Keep "your instincts, not positions".
   l. **Titles.**
      - First line of MORNING_DRAFT.md: "(v14, after nine review rounds and a repo check)" replaces "(v13, after nine review rounds)".
      - In `assemble_final.py`, change the title sentence ending "nine rounds of hostile review folded in." to end "nine rounds of hostile review and a check against the repo folded in."
4. **Summary length.** Keep the one-page summary within about +20% of its current length. Push detail into the sections. The summary must still read as plain language for a non-specialist owner: short sentences, no file paths, no internal check numbers (K, C, R, E ids).

## Output
- Edit the files, then run `cd SP/c8 && python3 assemble_final.py`.
- Write `SP/c8/CHANGES_v14.md`:
  - a numbered list, one line per applied fix: checker row id → location → what changed, in 25 words or fewer;
  - a "Not applied" list with reasons;
  - a "Conflicts resolved" list.
- Final message: counts (applied / not applied), the new summary word count against the old one, and anything the coordinator must decide.

## Rules
- The repo at `/Users/jonreilly/Projects/Physics/.claude/worktrees/focused-noyce-9a3983` is read-only. You may use `git -C <repo> show origin/main:<path>` to confirm a quote. Never fetch, commit, push, or edit repo files.
- Write only the files named above. Time box: 60 minutes.