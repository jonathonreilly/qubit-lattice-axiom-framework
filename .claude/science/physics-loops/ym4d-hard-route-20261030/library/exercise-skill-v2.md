lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-12T02:35Z

# exercise-skill-v2 (FINISH row 721)

Written by Claude Fable 5.2 at high effort (Mac mini worker 1), at commit 3d74e7aa3 of `claude/ym4d-hard-route`.
This is a process item. It makes no physics claim and grants no status. Nothing here is committed or pushed by the worker; the lead lands changes by a pull request to main.

Status of this file: in progress. Parts are appended in the order of the queue row: (0) sources read, (1) evaluation, (2) improved skill, (3) command wrapper and `openai.yaml`, (4) edits to the process stack, (5) application to this lane.

## 0. Sources read

Repo search (rule "Repo first"): `grep` for `exercise-skill`, `skills/exercise`, `commands/exercise` in this checkout. Hits: FINISH row 721 only (the brief), and the local copy of the skill, which is older than main. No earlier run of this item exists; this file starts it. Open-lemma check (rule 0a): this row attacks no lemma, so there is nothing to match in `library/open-core.md`.

Fetched from the public repository at main commit 1ddab64621 into `/tmp/exskill-v2-src/` (scratch, not committed), each read whole:

| File at 1ddab64621 | Lines | Note |
|---|---|---|
| `docs/ai_methodology/skills/exercise/SKILL.md` | 424 | the existing skill ("v1" below) |
| `docs/ai_methodology/skills/exercise/agents/openai.yaml` | 7 | |
| `.claude/commands/exercise.md` | 97 | |
| `.claude/commands/first-principles.md` | 168 | |
| `docs/ai_methodology/SCIENCE_WORKFLOW.md` | 81 | **At this commit it is a section map only** (line 6: "It adds no rule and grants no status"). It names no exercise, panel, blocked lane or author run. |
| `docs/ai_methodology/RULES.md` | 200 | not in the row's list; read because the map sends every rule there. At its 200-line budget (section 7). |
| `docs/ai_methodology/SETTINGS.md` | 93 | not in the row's list; method defaults |
| `docs/ai_methodology/PROCEDURES.md` | 48 | not in the row's list; line 32 says `research` supersedes the `exercise` skill and command as entry point |
| `docs/ai_methodology/procedures/research.md` | 150 | not in the row's list; **the one place that says when the exercise runs** (step 3, lines 77-78, and the step-reference row at line 147). At its 150-line budget. |
| `scripts/sync_methodology_skills.py` | 301 | searched only; it copies skill folders and reads no skill text |

**Finding that changes part 4.** The row asks for edits to `SCIENCE_WORKFLOW.md` that say when the exercise runs. At 1ddab64621 that rule lives in `procedures/research.md` step 3, and `RULES.md` section 7 says "One home per rule". So part 4 gives the rule edit for `procedures/research.md` (line-neutral, the file is at its budget), a pointer-only edit for `SCIENCE_WORKFLOW.md`, and the edit for `first-principles.md`. The lead chooses. The local checkout's `SCIENCE_WORKFLOW.md` (242 lines) is an older file and is not the edit target.

From this checkout, read whole: `library/gap-crux-fp.md` (502 lines), FINISH rows 712 and 716, `library/gap-crux-fp-check.md`, `library/gap-skeleton-final.md` Section 13.14; FINISH rows 697 to 726 and Section 13 of the skeleton for part 5.

## 1. Evaluation of row 712

Evidence read: `library/gap-crux-fp.md` (cited below as "fp L<line>"), its check `library/gap-crux-fp-check.md` (row 716, Claude Opus 5.5 high, same provider; "chk L<line>"), `library/prior/gap-ves-read.md` (row 717; "ves L<line>"), `library/prior/gap-tests-lit.md` (row 718; "tests L<line>"), the status block and Sections 0, 2.1, 3.4 to 5 of `library/gap-phys-seed.md` (row 720; "ps L<line>"), and the existing skill at main 1ddab64621 ("v1"). I did not re-check any proof. Every verdict on a statement below is the verdict of row 716, not mine.

Cost of the run, from the RESULT of FINISH row 712: 58 minutes, 322,570 output tokens, cost_equiv 12.5, one session, no subagents.

### 1.1 What produced results

| Step of row 712 | Result | Where | State after rows 716 to 718 |
|---|---|---|---|
| Inventory of knowns with a mark on each item (16 items: DEF, THM with source, GUIDE), written before any attack file was opened | P1 (the seed is not local: at least 7.4 by 14.8 correlation lengths); P2 (the seed contains the twist criterion); the split of the crux into two ranges R1, R2 (C1); the valid form of the tests (C6) | fp L24, L34-51, L55-59, L98-103 | P1, P2 HOLD (chk L20, L24). C1 and C6 are readings that Part 3b makes exact |
| Reasoning up from the inventory only: "what must a proof contain at the least" | The step from one size to all sizes is blind to the model, so everything enters through one base inequality, which must fail in each comparison model. Two tests the lane did not have (N-test, dimension test) | fp L68-78 | Not statements for a check. The two tests are GUIDE; row 718 agrees with the numbers after rounding and narrows "N >= 5" (tests L33, L45) |
| Assumptions table, row d1 ("a tool that also holds for U(1) cannot work": needed or habit? if wrong?) | Propositions T1 to T3: the worded test is false; a tool is refuted only by a model in its class where its hypothesis holds and the seed fails; where each test starts to bind | fp L150, L274-287 | T1, T2 HOLD; T3 HOLDS AFTER CORRECTION (the model must be in the class of the tool) (chk L42-58). The check adds: T2 refutes the short wording; the skeleton already used "at every coupling" (chk L48; fp L205) |
| Assumptions table, row d2 ("test K7 rests on numerics, not on a theorem") | Lemma COV, Lemma REG, Proposition V: a test of the same kind from a published statement; and "one well is not enough" | fp L151, L323-365 | COV, REG HOLD. V HOLDS AFTER CORRECTION as an implication from two unchecked inputs (chk L84-102). See 1.3, points 3 and 4 |
| Assumptions table, row a1 with a6 (the fixed-beta lattice gap is a habit; the target is a continuum statement) | The reading that the fixed-beta range from 1/18 to about 2 is not on the path of the target (GAP) | fp L113, L118, L176, L458 | The reading holds as logic (chk L139). The form (C) itself is not new (1.3, point 1) |
| Assumptions table, row c6 (one tool for the whole seed is a habit) with the re-judging of verdicts 6, 7, 11, 13 | Identity L; Proposition TW (the flux half for beta below 1/6); Lemma P; the open statement (vMF-Lip) | fp L144, L297-303, L377-400, L431-433 | Identity L, TW, Lemma P HOLD (chk L104-124). All are in R1, off the path of (GAP) by the file's own reading (fp L445) |
| Assumptions table, row a2 | Remark 2.A: the centre-even sector has no symmetric form; Theorem S needs the flux sectors | fp L114, L120-124 | (a) HOLDS, (c) HOLDS AFTER CORRECTION (citation) (chk L30-40) |
| Assumptions table, group (f) (owner rules, kept) | "This rule is not what blocks the crux": with machine bounds the proved range would move to a few tenths and R2 would not move | fp L170-172 | A GUIDE estimate, not checked. It answers an owner question without breaking a rule |
| First principles on the blockage: "what must a tool do, from the definitions" | A tool must control the difference of two extensive quantities to an absolute error; only locality or an exact identity can do that; every tool that proves something contracts at the lattice scale | fp L250-255 | Not in the check's scope (chk L12) |
| Audit of the tests: one row per comparison model, with how the failure is known and from where the test binds | The tests bind only from beta about 0.44, 1 and 1.6; below that "what stops the tools is the size of their constants" | fp L259-266, L285-287 | HOLDS AFTER CORRECTION: "is sound" becomes "if sound"; the stop range is GUIDE (chk L60-62) |
| Re-judging all 22 set-aside methods ("the verdict assumes", "valid?", "if wrong") | Three verdicts too strong (lines 6-7, 11, 13), each in R1; one tool comes back; 19 verdicts stand | fp L223-246, L291-309 | Not in the check's scope (chk L12) |
| Compare step, after Parts 1 and 2 | A table of 21 items: 12 already in the earlier work, 2 partly, 7 marked new or not found. It also corrected two items of the author's own inventory (F6, the box sizes of P3) | fp L41, L191-215 | One of the 7 "new" marks is wrong (1.3, point 1) |
| Real attempts at the end, each after a grep of `open-core.md` and the FINISH rows | 11 statements with proofs; three open statements named exactly; five proof items written as complete briefs | fp L313, L468-482, L490-498 | Of the 15 statements row 716 was asked to check: none FAILS, 4 hold after correction (chk L10) |

Downstream use, as evidence that the output was usable by others: rows 716 to 719 were queued from the proof items of fp L490-498; row 720 applied Proposition T1 to fourteen candidates (ps L166-169, L431).

### 1.2 What did not produce results

1. **No tool for the crux.** "No mass gap at a coupling of order one is proved. The seed there is open, and I found no tool for it" (fp L464). "Not proposed: another author run on the middle range" (fp L500).
2. **Most of Part 1 found again what the lane had.** 12 of the 21 compared items were already in the earlier work, among them P2 (in the stronger form of Identity FL), P3, P4, the first critical point (c5 is Theorem CRIT) and the step-scaling picture (fp L194-203, L209-210). This is the cost of the reading rule "do not read the attack files yet". The run has no control arm, so I cannot say that the new items (C6, the split R1/R2) needed that rule.
3. **19 of 22 re-judged verdicts stand**, and the three that change are in a range that the same file takes off the path (fp L309, L445).
4. **Everything proved in Part 4 is strong coupling or a restatement.** Proposition TW, Lemma P and the reductions R-a, R-b "move a lattice theorem. They do not move the crux" (fp L445). Corollary C is one line (fp L449-450).
5. **Group (e), beliefs, produced no check.** Each row names a check that is "numerics only" or none (fp L159-164). The group's value was the mark GUIDE on each belief, which then drove rows 717 and 718.
6. **Rows with no effect.** a3, a4, a5, b2, b4, c1, c2, c3: "No", "-" or "Unknown" in the columns "easier" and "check" (fp L115-117, L131-141).
7. **The method table rests on digests read at their synthesis sections only** (fp L10 item 1, L221, L229 "as read in the digest; not converted here"). So the "reason given" column is second-hand for most of the 22 lines.

### 1.3 Defects of the run that a skill should prevent

1. **A false "new".** The run marks the form (C), (PHYS-SEED), as new: "Not found in the passages read ... To be checked against 13.8 to 13.10 before use" (fp L200), and the RESULT of row 712 lists it as finding (1). It is (SEED-phys) with Propositions P and P' of `library/gap-seed-limit.md` (row 700, checked in row 703) (chk L126-139); row 697 also has it in scaling form (ps L30). Cause: the brief limited the compare step to named sections (fp L189), and no search for the statement itself ran before the word "new" was written. Three sentences of the file and one finding of the row are wrong as written (chk L135-138).
2. **The limit step was left unnamed.** "The passage from uniform gaps of periodic cubes to the limit theory ... is not written anywhere that I read" (fp L456). It is Proposition P', with four open inputs from the T0 chain (chk L141-153). Same cause as point 1.
3. **A test aimed at a different constant than the tool.** Proposition V shows the failure of the 1/5041 seed; the audit defines the seed with 1/1650 (fp L272, L358; chk L92). A counter-model must fail the same statement that the tool proves.
4. **Marks stronger than the weakest input.** One table marks Proposition V "THM" (fp L264); it is PROVED GIVEN a published statement in a reading (chk L94). The published theorem is stated for compact groups in dimension at least 3 and sketched for U(1) in three dimensions; no proof for SU(2) in four dimensions is written, in the preprint or in the journal article (chk L99; ves L36). So "a test that rests on a published theorem" (FINISH row 721, "Why") is exact only as "a test that rests on a published statement whose proof for this case is not written".
5. **A hidden hypothesis in the valid form.** T3 needs the comparison model to be in the class of the tool (chk L52). "Is sound" was written for a tool that has no written proof of "hypothesis implies seed" (chk L62).
6. **Numbers from memory decided ranges.** The binding ranges 0.44, 1, 1.6 are GUIDE (fp L280-282). Row 718 confirms most after rounding and finds a later end point of the K7 line near (1.2, 1.25) against the (1.5, 0.9) used (tests L61).
7. **A limit of the valid form that the run did not state.** Row 720 found it: for a hypothesis that is itself sufficient for the target, the valid-form test "is no filter"; a pass only says what a proof of the hypothesis must use (ps L166-169, L431). A skill must say what a pass shows.

### 1.4 Row 712 against the existing skill (v1)

The brief of row 712 does not name the skill. The match below is by content.

| v1 part | Used by row 712? | Evidence |
|---|---|---|
| Step 0, search the repo's own record first | In part, and in a different order: an index-level read before Part 1 (fp L24), a grep before the compare (fp L189) and before each attempt (fp L313). The search was too narrow (1.3, point 1) | |
| Step 0, literature search before reduction | No new search. The run reused four digests and fetched one paper (fp L10, L221, L354). The lead ran rows 713 and 714 beside it | |
| Step 1, plain version, blind check | Not used. Nearest: "what the two exercises say, in five sentences" (fp L486) | |
| Step 1, precise version | Taken from the brief (Theorems S, SH), not written again | |
| Step 1, three-column split (axioms, supplied, proved) | Replaced by the mark on each inventory item (DEF, THM with source and check state, GUIDE) (fp L32-51). Finer: it separates "proved and checked here" from "published, recalled" | |
| Step 2, ledger of load-bearing assumptions with "what if wrong" and "cheapest test" | Used, with other columns: needed or habit; if wrong; easier; check (fp L111-172) | |
| Step 3, reduction (less wrong, delete, shrink, split, price) | Used in substance: less wrong (a1), split (R1/R2; glue half, flux half), shrink (P4, the smallest object). No toy was built | fp L64, L98, L101, L113 |
| Step 4, fan-out to independent agents; a misframing agent | Not used: one session, no subagents (fp L6) | |
| Step 5, lenses and reframes lists | Not used as lists | |
| Step 6, try to kill every new route | Used on a different object: the kill verdicts of the old routes (3b.4), and its own tool against U(1) and Z_2 (fp L407) | |
| Step 7, rank routes | Ranked assumptions (fp L174-185), then wrote proof items | |
| Step 8, cheapest decisive test, pre-registered | Hand proofs in place of runners. Two guide runs "that tried to refute" (fp L340, L437); no pass or fail reading was written before the runs | |
| Step 9, plain report with labels | Used in another form: status block kept current, marks on every statement, "what this run did not cover", RESULT line, proof items (fp L10-20, L462-502) | |
| Non-negotiables: no new axioms, no promotion, a map is reported as a map | Kept. "Not proposed" and "No mass gap is claimed" are stated (fp L6, L500) | |
| Skill freshness, framework refresher read, approved primitives | Not needed here: the lane is a proof target with its own contract (`GOAL.md`), and it reads no framework axiom | |

**Added by row 712, not in v1:**

1. The inventory is written first, from the definitions and the target statement, and the earlier attack files stay closed until the compare step (fp L24, L28, L107).
2. Every inventory item carries a mark, a source and a check state (fp L32).
3. "Reasoning up" ends in a short numbered list of conclusions that the later parts cite (fp L96-103).
4. The assumptions are grouped, and three of the groups are not about the mathematics: the discard tests (d), the beliefs (e), the working rules (f) (fp L146-172).
5. The columns "needed or only habit" and "does a change make the problem easier", and a ranking by how much the problem changes (fp L174-185).
6. Owner rules are listed, kept, and "what a different rule would give" is written as not used (fp L166-172).
7. The audit of the discard tests in logical form, with the standing of each test (theorem or numerics) and the range where it binds (fp L259-287).
8. A table of every set-aside method with the reason given, then a verdict on each verdict (fp L223-246, L291-307).
9. First principles applied to the blockage itself (fp L250-255).
10. The compare step as its own late step, with "already", "partly", "new" and the place (fp L191-213).
11. A grep for duplicates before each real attempt, with the matches named (fp L313).
12. Proof items for workers, each a complete brief, and a "not proposed" list (fp L488-500).

**In v1, not used by row 712, and worth keeping (my judgement, not a measured gain):** the plain statement of the wall; pre-registered readings for the two guide runs; the rule to check strong words against what was actually done. v1 states that rule for subagent results. Applied to the run's own summary it names the three words that the check corrected: "new", "THM", "is sound".

### 1.5 Verdict of this evaluation

The exercise was productive in one specific way: it audited the lane's own filters and habits, and it did not find a tool. Its checked output is (i) the valid form of the discard tests, (ii) the reading that the fixed-beta range is off the path of the continuum target, (iii) two lemmas and one conditional test, (iv) strong-coupling results off the path. Its main defect is a compare step that was too narrow, which let a statement of row 700 pass as new. The improved skill keeps the order "fresh first, compare later" and adds a full search before any "new" mark.
