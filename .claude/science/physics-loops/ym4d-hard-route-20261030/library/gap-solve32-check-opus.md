lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:21Z

# Check of row 1283 (`library/gap-solve32-astra62.md`), FINISH row 1289

Research-stage working state. It grants no status and is not a public claim.

Checker: Claude Opus 5.5, max effort, Mac mini worker 3, at commit 1ce538a51
on branch `claude/ym4d-hard-route`. The checked file was written by a
gpt-6-astra lane (row 1283), so this is a cross-provider check. It is one
check by one model; it is not an independent derivation unless a step below
says it uses a different route.

## Plan (at most eight steps; each response does one step and appends here)

1. Read FINISH rules (Build on published work, efficiency), the row 1283
   text, and the checked file in full; list its numbered claims and the
   earlier rows it cites.
2. Check the short-time slice information bounds (29)-(32), line by line.
3. Check the recovery (35) of flux sector ratios from neutral histories.
4. Check the endpoint removal (36)-(40).
5. Check everything else in the file (setup, definitions, remaining
   numbered statements, the conclusion), with cited earlier rows read where a
   step depends on them.
6. Decide whether the main comparison is a restatement of an earlier row
   (grep `library/open-core.md`, FINISH rows, cited files).
7. Optional numeric guide only if useful and memory allows (guides only;
   no verdict rests on it).
8. Verdict table per statement and the RESULT line.

## Step log

(Each step appends below as it finishes.)

### Step 1 (done 14:35Z): inventory and cited rows

Read in full: `library/gap-solve32-astra62.md` (541 lines, at 1ce538a51), the
row 1283 text, GOAL.md, FINISH.md (opening sections, How we work, Working
efficiently, Rules).

Numbered claims of the checked file, by section and line:

| Lines | Claims | Label in file |
|---|---|---|
| L16-56 | (1) adjoint-mode count, (2) two-plaquette defect, (3) block Poincare, (4) | PROVED |
| L59-84 | (5) rare-slice probability, (6) energy-band bound, (7) trace ratios | PROVED; L84 OPEN |
| L87-126 | (8) annealed Green bound, (9) kernel domination, (10) walk bounds | PROVED |
| L129-170 | (11) temporal law, (12) covariance, (13)-(14) patch coherence | PROVED |
| L173-220 | (15)-(18) recovery of Ad g_x, (19) replica overlap | PROVED |
| L223-268 | (20)-(22) chessboard and strip bounds, (23) global sign | PROVED |
| L271-343 | (24)-(26) contraction, (27)-(28) endpoint recovery | PROVED; L343 ARGUED |
| L346-401 | (29) separating event, (30) prism identity, (31)-(32) information | PROVED |
| L404-451 | (33) twist candidates, (34) decoding, (35) sector ratios | PROVED |
| L454-487 | (36) singlet bound, (37) restricted kernel | PROVED |
| L490-521 | (38) orbit volume, (39) layer information | PROVED; L521 OPEN |
| L524-539 | (40) rank-one distance | PROVED; L537-539 OPEN |

Earlier rows the positive claims depend on, with their checks (FINISH RESULT
lines read): row 1141 (`gap-crux2-astra62.md`, check 1142 HOLDS); row 1145
(`gap-solve2`, check 1146 HOLDS); row 1149 (`gap-solve4`, check 1150 HOLDS);
row 1151 (`gap-solve5`, check 1152 HOLDS); row 1153 (`gap-solve6`, check 1154
HOLDS); row 1155 (`gap-solve7`, check 1156 HOLDS); row 1215 (`gap-solve23`,
check 1221 HOLDS); row 1231 (`gap-solve26`, check 1235 HOLDS, one credit
correction); row 1262 (`gap-solve30`, check 1271 HOLDS); row 1272
(`gap-solve31`, check 1282 HOLDS). Each was checked once by Claude Opus 5.5;
those checks are not evidence here. I read the cited statements and proofs
where a step below depends on them.
