lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T03:52Z

# Check of row 1053 (gap-wall-vectors-max), row 1062

Row 1062, `gap-wall-vectors-check-opus`. Written by Claude Opus 5.5 at max effort on Mac mini worker 3, started 2026-11-16T15:52Z (date -u), from commit 1b75bdfba of branch claude/ym4d-hard-route. It checks `library/gap-wall-vectors-max.md` (row 1053, written by Claude Fable 5.2 max). Same provider as the author (Anthropic), so this is not an independent check in the sense of the working rules; row 1061 is the cross-provider check and this file does not read it. A research check, not an audit; no mass gap is claimed. No new attack.

Marks: HOLDS, HOLDS AFTER CORRECTION (with the corrected text), FAILS (with the first failing line).

## Plan (at most eight steps; one per response, appended before the next)

1. Read FINISH.md (efficiency rules, build on published work) and row 1053's file in full; record brief B1 (section 8.2) and its file list.
2. Line-by-line check of 6.1 Lemma FACE-LIM, 6.2 Lemma ANCH and Corollary ANCH-W, 6.3 Lemma RIG.
3. Line-by-line check of 6.4 Lemma FACE-MW (capacity bound 24 t^2/log(R/r); constants 12 pi^2 and 48 pi^2).
4. Line-by-line check of 6.5 Proposition ITER and 6.7 Lemma EVEN.
5. Judge the S0 verdicts of 4.1-4.4, the dimension count of 4.1 (flux twist with frames on a two-dimensional set: excluded, or only not found), the one-loop formula of 4.2, and the Gaussian checks of 6.6.
6. Step 7's claim that Orland's papers hold the anchor: read the papers (open copies only, each in a new empty directory under /tmp) and judge.
7. Judge the five vector verdicts (V1 FAILS as a route since (BR-L) contains the target; V2-V4 renamings; V5 a GUIDE-grade test).
8. Verdict table, what this check did not cover, RESULT line.

## Step log

### Step 1 result: what is checked, and from which files

Read in full: `library/gap-wall-vectors-max.md` at 1b75bdfba (387 lines, 63,004 bytes, the size the lead note records). Read: FINISH.md sections "How we work", "Working efficiently", "Rules"; row 1062 and row 1053 of the queue.

**Items, from brief B1 (8.2 of row 1053) and row 1062.**

- Line-by-line checks: C1 = 6.1 Lemma FACE-LIM (comb tree, weak limit); C2 = 6.2 Lemma ANCH; C3 = 6.2 Corollary ANCH-W; C4 = 6.3 Lemma RIG (the two-sign identity, the constant beta_M/2 times D, the Cauchy-Schwarz step); C5 = 6.4 Lemma FACE-MW (the capacity bound 24 t^2/log(R/r), the constants 12 pi^2 and 48 pi^2); C6 = 6.5 Proposition ITER (K_j = (1 - eps_j) Kbar_j + eps_j R_j, the zero average); C7 = 6.7 Lemma EVEN.
- Judgements: J1-J4 = the S0 verdicts of 4.1-4.4; J5 = the dimension count of 4.1 (is a flux twist with frames on a two-dimensional set excluded, or only not found); J6 = the Gaussian checks of 6.6; J7 = the one-loop formula of 4.2; J8 = step 7's claim that Orland's papers hold the anchor; J9 = the five vector verdicts V1-V5.
- Files named by B1: this file; `library/gap-global-reform-max.md` L491-530 and L1040 (Lemma REM, line F3); `library/gap-invent-selective-max.md` L52-63 (kill sheet); `library/prior/gap-2don-proofs-read-opus.md` L113-176.

**Two notes on the brief.** (1) B1 names the output `library/gap-wall-vectors-check.md`; row 1062 names `library/gap-wall-vectors-check-opus.md`. I follow the row. (2) Row 1062 says I do not read row 1061's file; I do not.

## Status

Step 1 done. Next: step 2 (C1-C4).
