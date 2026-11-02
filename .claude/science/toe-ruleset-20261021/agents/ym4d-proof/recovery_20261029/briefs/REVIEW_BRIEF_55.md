# YM4D — Opus 5.5 REVIEW SWEEP of sessions 24-25. Shared brief for every reviewer.

## Why you exist
Every Claude-authored result in sessions 24 and 25 of this proof lane — the lead's consolidation and
every worker file — was produced on **claude-opus-5**, not the model the owner requires (**Claude Opus 5.5
at extra effort or higher; Codex gpt-6-astra at max**). The owner's words: *"its likely all no good because
you were set to the wrong model … review all prior work."* **You are re-establishing, from scratch and at
the right model, which of those results actually hold.** Assume nothing in your batch is right until
you have checked it.

**FIRST LINE OF YOUR DELIVERABLE, before anything else:** `Reviewer model: <your exact model ID, copied
verbatim from your system prompt>`. If that ID is not an Opus 5.5 ID, write that and stop. The lead will
check this line.

## Where things live
Repo root (a git worktree — NEVER run any git command):
  /Users/jonBridger/Toy Physics/.claude/worktrees/yang-mills-proof-df9972
Lane dir ($L): .claude/science/toe-ruleset-20261021/agents/ym4d-proof
Scratch (yours): /private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-yang-mills-proof-df9972/a931aaa3-5369-4512-9e8d-b8590010706c/scratchpad
Project: constructive UV stability + existence (OS axioms, non-triviality) for 4D lattice SU(N)
Yang-Mills via a SOFT gauge-covariant RG with S4' averaging, building on T. Balaban's RG programme
(CMP 1983-89) and J. Dimock's expositions. PROOF.md is the master ledger.

## BINDING RULES (the owner's)
1. **No git. No commits.** The lead commits.
2. **Write ONLY your one deliverable** (named in your scope). Read anything. Append-only.
3. **PRE-STATED first**: the model line, then UTC time, then your targets and what would count as a
   refutation — statements only, written before you derive anything.
4. **Criteria before scripts**: any numeric check gets checks/<id>_criteria.md with pre-registered
   PASS/FAIL **before** the script. Exact rational/symbolic arithmetic in plain python only (no BLAS, no
   floats for verdicts; rigorous rational interval arithmetic for logarithms). Your check ids must start
   with your batch prefix (e.g. `r55c3_`).
5. **Honest verdicts**: per claim, **CONFIRMED** (you re-derived the load-bearing step), **NOT-VERIFIED**
   (you could not settle it — say what is missing), or **REFUTED** (give the correct statement or value
   and its derivation). "The file says PROVEN" is not evidence. A wrong CONFIRMED is worse than an honest
   NOT-VERIFIED.
6. **Never fabricate** a number, a line reference or a PASS.

## What to review, in this order
1. **Every PROVEN / PROVEN-HERE claim** in your batch: re-derive its load-bearing step.
2. **Every REFUTED / "FALSE" / "struck" verdict against an earlier banked item.** A wrong refutation
   deletes correct work, and this batch was written by a model the owner distrusts. These count as much
   as positive claims.
3. **Every number that changed a decision**: decade figures, constants, thresholds, ratios. Check the
   arithmetic, the currency (decades of what, against which ceiling, with which constants frozen), and
   which value of the symbol it was evaluated at.
4. **Everything else**: spot-check, and say which you only spot-checked.

## Inputs you may trust more, and how
**Codex gpt-6-astra/max reviews** (`$L/CODEX_REVIEW_*.md`) ran at an approved setting and from a
different model family. Use them as evidence: where one confirms or refutes a claim in your batch, read
its argument and decide whether you agree, **saying so explicitly in either direction**. Note that some of
these files were still being written when the lead read them; **read the file as it is on disk now**,
and if its last lines look unfinished, say so. Do not treat the lead's summaries of them in
SESSION25_RESULTS.md as accurate.

## Three systemic defects. Check each one in every claim.
1. **Symbol collisions.** At least: 6 distinct ε_1, 4 ε_*, 4 θ_0, 3 η_1, ≥13 C_1, ≥11 c_1, ≥5 κ, and
   `c_RS`, `n_♯`, `q`, `θ`, `α`, `M`, `Q_str` and `C_♭` each found to name more than one object.
   **Before accepting any comparison, verify by file:line which object each symbol denotes.**
2. **Stale minima / stale quantifiers.** A value correct at the constant it was written for, quoted
   after that constant became an output. Ask what each inequality was evaluated at.
3. **Checks that cannot decide.** Ask of every gate: could it have failed? Tautologies, gates built
   from their object's own primitives, controls that do not fire, thresholds no true answer can meet,
   or that a wrong answer also meets.
**Also: status arguments are not proofs.** "P is proven and Q is open" does not show P ≠ Q.

## Read discipline
PROOF.md (720 KB), BFT_B.md (660 KB), PLD.md (390 KB), BFT_A.md (350 KB), HW.md (250 KB): **never read
whole.** grep -n, then sed -n 'A,Bp'. **Line numbers in this lane drift** (PROOF.md moved +79, then +25
again, non-uniformly), so locate cited text **by string**, and report a citation that has drifted.

## Deliverable
`Reviewer model:` line → PRE-STATED → findings (one per claim: verdict, file + locating string, the
derivation or reason) → **a summary table of every claim in your batch with its verdict**. End your reply
to the lead with: counts of CONFIRMED / NOT-VERIFIED / REFUTED, every REFUTED item with its correction,
**any finding that changes what PROOF.md's tally or HANDOFF's critical path should say**, and whether you
agree or disagree with each Codex verdict you used.

## Output-size rule (added 2026-10-29 after a worker died at the 128k output-token limit)
Never compose the whole deliverable in one response. Append it section by section with shell heredocs, each append
well under ~6,000 words, so a stop loses nothing and no single response approaches the output limit.
