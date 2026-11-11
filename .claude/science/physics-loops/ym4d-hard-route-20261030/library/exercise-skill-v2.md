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

**Not new to this lane.** Items 1 and 2 have a precedent in rows 669 and 670 (the two max plans): the brief of row 669 says "Part 1, your own thinking, BEFORE you read any digest or paper on the gap" (FINISH row 669), and `library/gap-skeleton-max.md` L55-57 keeps Part 1 unedited with facts "from memory" marked and corrected in Part 2. Each of its approaches B1 to B14 carries "the U(1) test" in the form "the crux statement must fail for U(1)" (for example L109). So what row 712 added in this lane is the explicit inventory table, the assumptions table with the groups (d) to (f), and the audit of the tests and verdicts as objects in their own right.

**In v1, not used by row 712, and worth keeping (my judgement, not a measured gain):** the plain statement of the wall; pre-registered readings for the two guide runs; the rule to check strong words against what was actually done. v1 states that rule for subagent results. Applied to the run's own summary it names the three words that the check corrected: "new", "THM", "is sound".

### 1.5 Verdict of this evaluation

The exercise was productive in one specific way: it audited the lane's own filters and habits, and it did not find a tool. Its checked output is (i) the valid form of the discard tests, (ii) the reading that the fixed-beta range is off the path of the continuum target, (iii) two lemmas and one conditional test, (iv) strong-coupling results off the path. Its main defect is a compare step that was too narrow, which let a statement of row 700 pass as new. The improved skill keeps the order "fresh first, compare later" and adds a full search before any "new" mark.

## 2. The improved skill (full text)

Ready to replace `docs/ai_methodology/skills/exercise/SKILL.md` at main 1ddab64621. The text is between the two four-backtick fences below: 700 lines, 35,807 bytes, sha256 prefix `5673d58a50bb28d3` (the file starts at the line `---` and ends at the line that ends "against what it actually computed."). v1 is 424 lines.

**What is kept from v1, word for word or nearly:** the Skill Freshness section; the purpose and the three success forms; the model and tool boundary; the Framework Refresher Read; the arguments `--artifact`, `--slug`, `--subagents`, `--no-web`, `--test-budget`; the plain and the precise statement of the wall with the blind check; the text on what each approved primitive grants; the fan-out rules, the lenses and the reframes; the kill checks; the ranking rule; the rules for runs (pre-registration, searched class, no long extrapolation, fresh adversarial check before a negative conclusion); the plain-language report; the non-negotiables.

**What is new, each from a line of row 712 (Section 1 above):**

| New in v2 | From |
|---|---|
| Step 0 sorts the record into "open now" and "closed until step 5" | fp L24 (the reading rule) |
| Step 2, the inventory with a mark, a source and a reading state on every item | fp L32-51; defect 1.3.4 |
| Step 3, reasoning up, ending in numbered conclusions | fp L53-103 |
| Step 4, six groups; the columns "needed or habit" and "easier"; group (f) kept; the ranking | fp L105-185 |
| Step 5, the compare step, with a full search before any "new" mark | fp L187-215; defect 1.3.1 |
| Step 6a, 6d, every set-aside method listed and re-judged | fp L219-246, L289-309 |
| Step 6b, first principles on the blockage | fp L248-255 |
| Step 6c, the valid form of a discard test: refutation, constraint, range, standing of the test, what a pass shows, the same T | fp L270-287; chk L52, L92; ps L166-169 |
| Step 8, a duplicate search before each attempt; "on the path or off it" | fp L313, L445 |
| Step 9, "filters corrected", work items as complete briefs, a RESULT line, the strong-words pass over the run's own report | fp L488-502; defects 1.3.1, 1.3.4, 1.3.5 |
| Output rules: write as you go, header with "not covered", status block | fp L8-20; FINISH "Save as you go" |
| A fourth success form, "a corrected filter" | fp L274-276 |
| The section "Relation to other procedures" (first-principles, races and panels, checks) | FINISH row 721, deliverable (4); `RULES.md` section 3 |
| Step 4 starts from an existing counterfactual pass | `skills/physics-loop/references/assumption-import-audit.md` L57-90 at main (found by a search of main for "exercise") |

**Changes to v1 that the lead should accept or strike (each is a choice, not a need):**

1. `--subagents` default goes from 4 to 0. Reason: row 712 ran with none; FINISH "Working efficiently" allows subagents only when an item needs a separate reader. With 0, the misframing pass and the kill pass still run, as context-isolated passes.
2. The report labels `proved / checked / suggested / reading` become the marks of the Output rules. Reason: v1's "checked (a finite or numerical test)" collides with `checked` of `RULES.md` section 1 (an independent check record), and `PROCEDURES.md` L23-25 says the newer file wins.
3. A standalone proof target reads its `GOAL.md` contract in place of the framework refresher list. Reason: this lane reads no framework axiom. Strike this paragraph if every exercise must read the axioms.
4. The seven-file packet becomes `EXERCISE.md`, `SUMMARY.md`, `APPROACH_REGISTRY.md` and `scripts/`. Reason: one file written in step order survives a lost session.
5. The literature citation `SCIENCE_WORKFLOW.md section 2, rule 9` becomes `RULES.md section 2, rule 7`, which is where the map sends it.
6. v1's steps 3 (reduction), 4 (routes), 5 (outside view), 6 (kill), 7 (rank) are merged into v2's steps 3 and 7. What v2 drops or moves: "Speed up the loop, then automate" (v1 step 3 item 6) is dropped; "Delete" (v1 step 3 item 2) and "mark which rows the wall would survive without" (v1 step 2) are carried by the column "needed or habit"; the three-column split of v1 step 1 is carried by the marks AXIOM, SUPPLIED, THM; the table "cluster the rows into candidate routes" (v1 step 2) is replaced by the ranking and by "sources of routes" in step 7; the reframe table keeps its list and loses its column layout; the appendix lists "candidates for a physics-loop PR, or for a no-go or opportunity ledger" are replaced by the work items.

**Length.** If the lead wants it shorter, the blocks that can go to a reference file without loss of a rule are: the lenses and reframes lists (step 7), the rules for runs (step 8), and the primitive paragraph (step 4, also in the command wrapper).

````markdown
---
name: exercise
description: "Use when repo physics or proof work hits a hard wall (a blocked lane) and the goal is to get past it or to price it: state the wall in plain words, list what is known to be true with a mark on every item, reason up from that list before reading earlier attacks, list every assumption (target, formulation, reduction, discard tests, beliefs, working rules) and ask what follows if it is wrong, audit the tests that were used to discard ideas, re-judge every method that was set aside, compare with earlier work, make real attempts, and report in plain language. Trigger on requests for 'exercise', 'assumptions exercise', 'first-principles exercise', 'Elon exercise', 'math sector search', 'reframing exercise', 'audit the discard tests', 'why are we stuck', or help getting unstuck on a blocker without immediately adding new theory."
---

# Exercise

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

## What the exercise is for

A wall is a place where a lane keeps failing in the same way. The exercise
exists to get past it, or to show exactly what getting past it would cost.
It is not a completeness drill and not a defence of the current framework
story.

The exercise has two halves. The first half looks at the problem with the
earlier attacks closed: what is known to be true, and what follows from that
alone. The second half looks at the lane's own filters: its assumptions, the
tests it used to discard ideas, and its verdicts on the methods it set aside.
A lane can be blocked by a filter as well as by the mathematics.

An exercise has succeeded when it delivers at least one of:

- **a route with its first test actually run**, and the result recorded;
- **an exact price**: a proof, or decisive checked evidence (an exhaustive
  finite certificate, or a runner backed by a theorem that makes it
  decisive, where the target's contract allows such evidence), that the wall
  is equivalent to a named premise or to one exact open statement;
- **a misframing**: checked evidence (a proof, runner or exact counterexample)
  that the wall comes from a supplied model, method, reading or habit rather
  than from the axioms or the target, together with the question that
  replaces it;
- **a corrected filter**: a discard test or a verdict shown false or too
  strong in its valid form (step 6), with the methods that come back and the
  range where they come back.

An argument that has not been checked counts as a suggestion, not as a price,
a misframing or a corrected filter.

A long map of possible attacks with nothing tried is not success. Say so if
that is all the exercise produced.

The exercise may produce routes, proof plans, lemmas with proofs, runners and
literature bridges. It must not apply audit verdicts, promote claims, add
axioms, primitives or imports, or treat existing repo content as
unquestionable.

## Relation to other procedures

- `docs/ai_methodology/procedures/research.md` step 3 says when a target
  runs the exercise. This file says how.
- `/first-principles` derives one target from the allowed premises. The
  exercise uses the same discipline on a wall: the inventory of step 2 is
  that command's premise ledger, with a mark on every entry. A route that
  leaves step 7 as a derivation goes to `/first-principles`.
- A race or a panel is several independent attempts or readers on one
  question. It answers a question that is already posed. The exercise asks
  whether the question and the filters are right. On a blocked part, run the
  exercise first and brief the race or panel from its work items (step 9).
  The judicial panel of the audit path is a different thing; the exercise
  never touches it.
- The exercise is not a check. Its statements are `argued` until
  `procedures/check.md` records a check of them.

## Model And Tool Boundary

Use the strongest available reasoning model/profile, as configured by the
user. Report the actual model, effort and provider at the top of the output.
Use subagents only when the caller allows them. Subagents that attack the
physics must be maximum-reasoning physics agents, not lightweight
summarizers; report their actual model and vendor family, and do not describe
same-family agents as independent referees. Every main agent and subagent
performs the Framework Refresher Read before its slice. Do not use
image-generation or visual artifact tools for this skill.

For theorem, proof, or multi-step bridge work, read
[`../physics-loop/references/proof-search-governance.md`](../physics-loop/references/proof-search-governance.md)
before step 7 and apply all of it: the exact target contract, the
approach-family registry, independent rounds, the concrete-return contract,
the theorem-strength gap test, the candidate-proof audit, and the round
synthesis and handoff.

For literature, browse current scholarly sources when network access is
available and cite them precisely. Literature suggests proof templates,
known no-go results and known escapes. It is never imported as authority: an
external proof is translated into repo objects, checked by a runner or proof
artifact where possible, and then reviewed like native theory. A published
theorem enters the inventory (step 2) with its source and with how much of it
was read.

A run (a script, a numerical test, a search) can refute a statement or guide
a guess. It discharges nothing by itself. Where the target's contract forbids
computer-assisted steps, every statement the exercise marks as proved has a
written proof.

## Framework Refresher Read

Before step 0, do a short framework refresher read. If a current repo-native
`framework-refresher` skill or command exists, use it first; otherwise read
directly:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full, for the Lattice, Qubit,
  Admissibility and Record baseline;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` for how approved
  primitives enter assumption, import, wall and bounded-status judgments;
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` for the scale-reference boundary;
- `docs/audit/data/axiom_premise_nodes.json` for the complete supplied
  foundation, and `docs/audit/data/premise_decision_history.json` only when
  historical provenance matters;
- `docs/audit/data/derivation_obligations.json` for registered derivation
  obligations that touch the wall;
- `docs/ai_methodology/skills/review-loop/SKILL.md` for review and audit
  boundaries, especially the axiom/approved-primitive distinction and the
  Record guardrails;
- `docs/repo/CONTROLLED_VOCABULARY.md` when proposing names, statuses or new
  surfaces.

Each subagent states which refresher surfaces it read before giving
conclusions. The refresher prevents stale framework language. It does not
exempt framework premises from challenge: in this exercise every premise,
the axioms included, is an assumption.

A target whose `GOAL.md` contract reads no framework axiom or primitive (a
standalone proof target) reads that contract and its rules in place of the
list above. Say in the output that this replacement was made.

## Arguments

- problem/wall text: required unless resuming a named exercise packet or
  working from a caller's brief;
- `--artifact`: write a durable packet under `.claude/science/exercises/<slug>/`;
- `--slug SLUG`: optional packet slug;
- `--subagents N`: independent route fan-out in step 7; default `0`, which
  means context-isolated passes by the main agent;
- `--no-web`: perform the literature search offline and mark unverified or
  unavailable sources;
- `--test-budget H`: hours allowed for step 8's attempts and tests (default 2).

**The brief.** A caller that runs the exercise inside a target names, in its
brief: the wall (file and section of the statement); where the definitions
are; the files to keep closed until step 5 (attack files, route notes,
digests of methods, lists of set-aside methods); the output file; the budget;
the binding limits (for example no commits, no subagents). Without a brief,
the main agent makes this list in step 0 and writes it down.

Without `--artifact` and without a brief, return the report (step 9) in the
conversation, with the tables as an appendix. Inside a target folder, write
one file, the one the brief names. With `--artifact`, write:

```text
.claude/science/exercises/<slug>/
  EXERCISE.md            # the run, in step order, appended step by step;
                         # opens with the header and the status block
  SUMMARY.md             # the plain-language report (step 9), read first;
                         # it links to EXERCISE.md rather than copying it
  APPROACH_REGISTRY.md   # the proof-search governance registry
  scripts/               # step 8's scripts; outputs beside them
```

## Output rules

**Write as you go.** Put each step on disk before you think about the next
step. Text on disk is the only thing that survives a lost session. When a
step grows long, stop, write what you have and the exact point where you
stopped, and continue. If the output file already holds work of an earlier
run, keep it and continue from it.

**Header.** The file opens with: who wrote it (provider, model, effort,
session), the commit, the date, the words "nothing in this file is checked by
another model" until a check record exists, and a list "what this run did not
cover". Keep that list true: a source read in part is listed as read in part.

**Status block.** After the header, keep one short block current: one line
per step, done or not, with its main result. Bring it up to date after each
step, so that the file is complete if the run ends early.

**Marks.** Every item of the inventory and every statement of the run
carries one mark. A mark is never stronger than the weakest input it names.
Standing words are those of `docs/ai_methodology/RULES.md` section 1.

```text
Inventory items (step 2):
  DEF       a fact of the definitions, with the place of the definition
  AXIOM     a framework axiom or approved primitive, with what its source
            note grants
  SUPPLIED  a model, comparator, reading, convention or method that we chose
  THM       a theorem, with its source and its standing:
              checked (path of the check record) | argued | retained
            for a published theorem also how it was read in this run:
              read in full | read in part (which pages) | recalled
            and whether the source writes the proof for the case used
  BELIEF    from physics, numerics, experience or habit; used in no proof

Statements made by the run:
  argued    proved here from named inputs; each input with its mark
            ("argued, given X" when an input X is open, recalled or a belief)
  refuted   an explicit counterexample, written so that it can be checked
  guide     a run or a number; it decides nothing
  reading   an interpretation
  open      not proved
```

Nothing the exercise writes is `checked`. A statement becomes `checked` only
through a check record by a model that did not write it (`RULES.md`
section 3). Say who checked what in plain words: "proved by <model>, not yet
checked", "checked line by line by <model> (same provider), first failing
step none".

## Step 0: Locate the record, and keep the attack files closed

After the refresher read and before generating anything, find where the
repo's own record of the wall is. Do not read the arguments yet.

- landed notes and runners on main whose titles or scopes name the object;
- this lane's open PRs, probe notes, queue rows, registries and indexes;
- decision records, panel syntheses and earlier exercise packets under
  `.claude/science/exercises/` and `archive/campaigns/`;
- held or unlanded blocks on campaign and backlog branches, and candidate
  packs with kill sheets under `.claude/science/candidates/`.

Search by the physical or mathematical object and its synonyms, not only by
words in titles: unlanded blocks are where earlier answers most often hide.

Sort what you find into two lists and write both down:

- **Open now:** the target statement, the statement of the wall, the
  definitions, and the statements (not the proofs, not the route discussion)
  of theorems that the lane has `checked` or cites.
- **Closed until step 5:** attack files, route notes, digests and surveys of
  methods, lists of set-aside methods, earlier exercises on the same wall.

The purpose of the closed list is a fresh look, not ignorance. Step 5 opens
every file on it, and no item is called new before that.

Literature: reuse the lane's literature record. If the lane has none, run
the search described in step 7 now and record it, including a search that
found nothing. Before step 5, read from it only statements of results:
theorems, known no-go results, known counterexamples. With `--no-web`, search
available local sources and name missing coverage; do not invent a completed
search.

Do not re-derive a mapped wall or re-run a recorded test unless the exercise
names what is new.

## Step 1: State the wall twice

**Plain version**, written for a smart reader with no physics training:

- at most about 150 words, no undefined jargon;
- what we are trying to get, and in one sentence why it matters;
- what keeps happening instead;
- what exactly the evidence covers, and what it does not;
- what would count as getting past it;
- at most one picture or analogy, marked as an analogy.

**Precise version:** the target claim, theorem, import, selector, no-go or
bridge; its quantifiers and domain; allowed premises and forbidden
weakenings; required boundary or degenerate cases; outcomes that do not count
as closure; what currently fails; what would count as progress, closure,
demotion or no-go. Where the lane has a checked statement of the wall, quote
it with its path and do not rewrite it.

**Blind check.** When a fresh agent is allowed, give it only the plain
version and ask it to say back what is blocked and what would count as
passing. Fix the plain version until the restatement matches the precise
one. Otherwise correct the plain version in step 9 and say that no blind
check ran. Keep both versions neutral: do not smuggle the desired answer, or
the favoured escape, into either.

## Step 2: The inventory: what is known to be true

List what is known to be true about the problem. Use only the "open now"
list of step 0, the refresher read and the literature's statements of
results.

```text
# | Item, in one or two sentences | Mark (DEF / AXIOM / SUPPLIED / THM / BELIEF) |
Source (path:line or citation) | Standing and reading state (for THM)
```

Rules:

- Every item gets a mark. An item with no mark is not in the inventory.
- A theorem stated from memory is marked `recalled`, with what was not
  re-read. A theorem read in part names the pages read.
- A belief stays in the table. It is marked BELIEF and no proof step may use
  it. Beliefs from numerics name the numbers and where they come from.
- Include what is known about the nearest models where the target is false
  or true for a known reason. These become the tests of step 6.
- Framework lanes: enumerate approved primitives from
  `docs/audit/data/axiom_premise_nodes.json` and read their source notes
  (step 4 says what each grants). Walls often sit in the SUPPLIED items. A
  wall built from supplied parts presses on those parts, not on the axioms,
  and the report must say so.

## Step 3: Reason up from the inventory

Reason only from the items of step 2. Do not import the framing of the
earlier work, and do not argue by analogy with an earlier attempt. Answer, in
this order, and prove what can be proved in a few lines:

1. **What follows at once.** Short facts that the inventory gives directly.
   Each one names the items it uses.
2. **The least a solution must contain.** What must any proof, derivation or
   construction of the target contain, whatever its method? Which known
   models must it fail on, and so which property must it use?
3. **The smallest object.** What is the smallest object, carrier, sector or
   finite set of numbers that holds the information the target needs? If a toy
   model in which the wall still bites can be built in under an hour, build
   it and confirm that it bites.
4. **Where the result can come from.** Which mechanisms could make the
   target true, and in which ways can it fail? Is it one problem or several
   (by range, by sector, by scale; a selector, readout, dynamics,
   normalization or representation problem)?
5. **Make the requirement less wrong.** Is the target stated too strongly,
   or inherited from a stale route? What does the consumer actually need?
6. **Price it.** If the target cannot be derived, what is the exact missing
   input?

End the step with a short numbered list of conclusions (C1, C2, ...). Each
conclusion names the inventory items it rests on. A conclusion that rests on
a BELIEF is a belief. Later steps cite these numbers.

## Step 4: The assumptions table

List every assumption you can find, in these six groups. Take them from the
wall's statement, the governing notes' premise lists and the runners, not
from memory. Then add the hidden ones: finiteness, locality, smoothness,
symmetry, perturbative level, choice of state, boundary conditions, readings
of the axioms, and "obvious" steps. Where the lane already has an
assumptions and imports ledger with a counterfactual pass
(`../physics-loop/references/assumption-import-audit.md`), start from its
rows and do not write them again.

- **(a) Target.** What is wanted: which theorem, which limit, which
  observables, which domain, which strength, and who consumes it.
- **(b) Formulation.** What the problem is built on: axioms and approved
  primitives (marked as such), definitions, the model, conventions, boundary
  conditions, choices of representation.
- **(c) Reduction.** Every step from the target to the wall: the route
  chosen, the intermediate statement, "one tool proves all of it", "one
  parameter value at a time", runner and numerical choices.
- **(d) Discard tests.** Every rule the lane uses to set an idea aside: "it
  also holds for model X", "it needs a small number", "its constant depends
  on the answer", "it bounds the wrong quantity", "it was tried".
- **(e) Beliefs.** What physics, numerics or reputation say, and what the
  plan depends on.
- **(f) Working rules.** Owner rules, the limits of the target's contract,
  method defaults.

```text
ID | Assumption, in plain words | Where it is used (path:line) |
Needed or habit (needed by the target / needed by the method / habit) |
If it is wrong or dropped: what follows | Does a change make the problem easier? |
Check (already run: path and result / cheapest check / none known)
```

Rules:

- Every row gets a real "if wrong". If no consequence is visible, say what
  would have to be inspected to know.
- "Needed by the method" is not "needed by the target". Say which.
- Group (f) is questioned on paper only. The run obeys every owner rule and
  every limit of the contract. You may write what a different rule would
  give, marked "not used". Name an axiom change only as a price.
- Framework lanes, group (b): the scale-reference primitive grants the
  Planck scale reference as units conversion only: it does not make
  downstream rows bounded and grants no dimensionless content. The
  kinetic-isotropy primitive grants only structural OS0 kinetic-form isotropy
  `c_t = c_s`, with no dynamics, Lorentz-closure theorem, absolute scale,
  spacing-ratio theorem, selector or empirical content. The realized-state
  primitive grants only pointwise evaluation at a supplied law-admissible
  realized state; it supplies no state, state-selection rule, measure,
  typicality or genericity assumption, weighting, probability rule, or any
  state-contingent value (quantities that vary across the law-admissible
  family remain registered data).

**Ranking.** Rank the assumptions by how much the problem changes if the
assumption is dropped. For the first five, write one line: what the lane
would do differently. Mark the rows whose drop would change an owner
decision.

## Step 5: Compare with the earlier work

Now open the "closed" list of step 0 and read it. For every conclusion of
step 3 and every assumption ranked in step 4:

```text
Item | Already in the earlier work? (yes / partly / new) | Where (path:line) |
Search scope for a "new" mark
```

Rules:

- Before you write "new", search the whole record of the lane for the
  statement itself: every file of the target folder, its indexes and
  registries, its queue rows, and the open PR branches. Search by the
  objects of the statement and by at least two wordings. Write the scope
  next to the mark. A search of named sections only gives "not found in
  <those sections>", never "new".
- Where the earlier work is right and the inventory is wrong, correct the
  inventory in place and say so at the item.
- Where the earlier work has a stronger form, say so and use it.
- Credit the earlier row, note or author for every item marked "yes" or
  "partly".
- End with two short lists: what the fresh pass added, and what it only
  found again.

## Step 6: The blockage: discard tests and set-aside methods

This step applies steps 2 to 4 to the lane's filters.

**6a. List every method that was set aside.** One row per method, from the
lane's files and digests. Do not sample.

```text
# | Method (with its authors) | Reason given | Where (path:line; read
first-hand, or taken from a digest) | Kind of reason (fails a test / circular /
needs a small number / wrong quantity / other setting / unverified / open premise)
```

**6b. First principles on the blockage.** From the definitions: what exactly
must a tool do here? Which kinds of statement can do it at all? Which
property of the model is the least that a tool must use? Write the blockage
in one sentence.

**6c. Audit every discard test in its logical form.** Definitions:

- A **tool** is a hypothesis H together with a written proof of "H(M)
  implies T(M)" for every model M of a class K that contains ours. T is the
  statement the lane needs, with its constants and quantifiers. A method
  with no written proof of this implication is a candidate, not a tool.
- A **test** is a comparison model M'.

The valid form has two parts.

- **Refutation.** A method is refuted as a tool on K only by a model M' in K
  where H(M') is true and T(M') is false, for the same T. Then "H implies T"
  is false on K.
- **Constraint.** For a tool with a written proof, T(M') false gives H(M')
  false. So a proof of H for our model must use a property that M' does not
  have. The test says what the proof of H must use. It does not refute the
  tool.

The test does not refute the tool when:

- the proof also runs for M', and T(M') is true there;
- M' is outside K;
- T(M') fails for another constant, quantifier or range than the tool's T;
- H(M') is not known.

The range form: let H be blind to the difference of M and M' at a parameter
value (H(M) implies H(M') there). Then the hypothesis of a sound tool fails
for M at every value where T(M') fails, and the tool proves nothing for M
there. So a test has a range. Write from which value it binds.

For each test, fill one row:

```text
Test (model M') | In which class K | The exact T that fails in M' |
How the failure is known (THM with standing and reading state / BELIEF) |
What a tool must use to pass | From which parameter value the test binds
```

Rules:

- A test that rests on a BELIEF is a belief. Say so, and look for a test of
  the same kind that rests on a theorem.
- A pass is no support. A hypothesis that implies T on K is false in every
  model of K where T fails, so it passes every valid test. A pass says only
  which property a proof of H must use.
- Ask whether the tests are enough. Step 2 lists the nearest models where
  the target is false; each one is a test.
- The other kinds of reason have a valid form too. "Circular": not circular
  when the constant depends on a smaller case (an induction), or in a proof
  by contradiction at a first bad point. "Needs a small number": valid as a
  range only; write the proved range. "Wrong quantity": name the quantity
  the target needs and the gap between the two. "Other setting": name the
  hypothesis of the tool that fails in ours. "Was tried": a failed search
  rules out nothing; name what was tried.

**6d. Re-judge every verdict.** One row per row of 6a:

```text
# | The verdict assumes (how the tool is used, in which range, for which
form of the target) | Valid in the corrected form? (valid / valid only in
range R / too strong / wrong / moot) | If not valid: what comes back, and where
```

Rules:

- A verdict that you did not re-derive is "valid as reported; not
  re-derived". Do not upgrade it.
- A verdict shown wrong or too strong is a result. Prove it or mark it.
- A tool that comes back goes to step 8.
- State where the corrected verdicts matter: on the path of the target, or
  off it.

## Step 7: Routes: generate, try to kill, rank

**Sources of routes.** The first-ranked assumptions of step 4, dropped or
changed; the tools that came back in step 6; a new form of the target from
step 3; the "least a tool must use" of 6b.

**Independent routes.** With `--subagents N`, fan out to `N` agents; with
`0`, use context-isolated passes. Give each a neutral, route-local brief
built from step 1's precise version and step 4's table. Do not give any
agent the favoured approach or another agent's conclusions. Choose the
briefs so that the approach families are materially different. Always
include one lens from outside the lane's own vocabulary, and one pass whose
brief is to argue that the wall is misframed and to name the question that
replaces it. Each pass returns one to three routes under the
concrete-return contract: a lemma with its proof skeleton, a construction,
an equation or invariant, a falsifier, or an exact missing obligation.
Reject vague returns ("topology might help").

```text
Route | Family (object, mechanism, terminal obligation) | Assumption it drops or changes |
What you would have to believe for it to work | First artifact | Cost |
What it would change if it worked
```

**Outside view.** Reuse the literature record of step 0 and update it only
for new route questions. Literature always runs
(`docs/ai_methodology/RULES.md` section 2, rule 7). `--no-web` skips live
search: the agent may still cite sources it knows, marked `recalled`. Prefer
primary sources. Look first for known no-go theorems and known escapes for
this kind of wall, then for proof templates.

```text
Source | What it shows | Premises | Maps to the repo? | What does not map |
Translation or runner | Import risk | Citation | Read in full / in part / recalled
```

**Mathematical lenses.** Choose them from the wall's structure; do not run a
fixed checklist. For each lens used, give the object that changes, the
invariant or theorem type, a minimal toy example, what would falsify it and
the first artifact. Before choosing, glance down this list so the search is
not too narrow: finite groups and representations; operator algebras and
noncommutative geometry; categories and universal properties; algebraic
topology, cohomology, K-theory and index theory; spectral graph theory and
combinatorics; convexity, optimization and variational methods; probability,
information theory and large deviations; dynamical systems, ergodic theory
and stability; PDE and functional analysis; number theory and lattices; logic
and independence. Lenses considered and found empty get one line each.

**Reframes.** Try moving the boundaries that repo walls usually hide behind:
pre-record vs recorded; object vs readout; selector vs admissible dial;
dynamics vs kinematics; finite carrier vs limiting family; exact theorem vs
bounded theorem vs no-go; value derivation vs value availability; central
sector vs within-sector data; representation choice vs physical observable;
supplied model vs axiom content; local pattern vs global or collective
structure; obstruction vs missing input. A reframe is useful only if it is
stated in framework objects, not lane fixtures.

**Try to kill every route.** Before ranking, give each route to a different
agent or pass whose brief is to break it. It checks:

- whether the route quietly assumes the target;
- whether it contradicts a checked or landed result;
- whether it was already tried (step 5);
- whether it fails a test of step 6 in the valid form;
- whether it breaks an owner rule or needs a new axiom, primitive or import;
- whether its terminal obligation is target-equivalent. If it is, the route
  is `blocked-equivalent` under the proof-search governance and is not near
  closure.

Record a verdict for every route: survives, wounded (with the named gap) or
dead (with the reason; a test kills a route only in the valid form of
step 6).

**Rank.**

```text
Rank | Route | Family | Assumption challenged | What you would have to believe |
Terminal obligation | Strength vs target | Kill verdict | Cost | First artifact |
What it changes | Stop/reopen condition
```

Rank by what the route would change if it worked, divided by what it costs
to find out. A cheap test that would move an owner decision outranks an
elegant reduction that ends at a target-equivalent lemma.

## Step 8: Real attempts

Within the budget, take the best two or three routes and go as far as you
can on each: prove the first lemma, find a counterexample, or reduce the
route to one exact statement.

- Before each attempt, search the lane's open registry and queue for the
  statement. If another row holds it, stop, name the match, and take the
  next route.
- A reduction counts only if the equivalence is proved, or the remaining
  statement is named exactly with its quantifiers and constants.
- A dropped assumption that gives a different target counts only if the new
  target is proved to give the old one, or the missing step is named.
- Say for each result whether it is on the path of the target or off it.

For each run (script, numerical test, search):

- pre-register the pass and fail reading before running, and never change
  it after the result is seen. If the result shows the reading was badly
  chosen, add a new, dated follow-up test with its own reading;
- state exactly which class a search covered. A search that finds no pass
  in a finite class is a bounded result ("no pass in the searched class"),
  not a no-go, and a run that fails to refute a lemma does not prove it;
- do not let a verdict rest on extrapolating a fit over many orders of
  magnitude. When it would, compute the decisive quantity directly;
- keep the script, the output and the result, and hold the numeric lock
  where the repo requires one;
- report and preserve the actual result immediately, including failures.
  Before interpreting a failure as a scientific negative conclusion or no-go,
  obtain a fresh adversarial check under the allowed review configuration.
  Prefer another vendor's model where configured; label a same-family check
  honestly and do not call it an independent referee. If the user prohibits
  subagents, use a separate primary-session pass and state that it is not
  independent. Record the interpretation, corrections and review limitation
  without changing the original result or pre-registered reading;
- say plainly whether it moved the wall, and in which direction.

If no route can be attempted inside the budget, say why, and give the
smallest test that would decide the top route and what it needs. A deferred
test must name who or what it is waiting on: the owner, a probe queue, or a
missing input.

Results of the exercise are exercise evidence, not repo claims. A result
worth keeping goes through the normal note, check and review path.

## Step 9: Report

The report leads with plain language. Write it for the owner, who will act
on it. Every claim in it carries one mark of the Output rules.

1. **The wall, in plain words:** step 1's plain version, corrected by the
   exercise.
2. **What the exercise found:** three to six plain sentences. Include what
   changed since the exercise started, and the attempts with their results.
3. **Filters corrected:** each discard test or verdict that changed, in its
   valid form, with the range and what comes back. "None" is an answer.
4. **Routes worth doing:** at most three. For each, say what you would have
   to believe, what it costs, the first test, and what it would change.
5. **What not to do next,** with the reason.
6. **The exact price,** if the exercise found one: the premise, decision or
   open statement the wall is equivalent to.
7. **Work items:** each a complete brief that a fresh session can run with
   no other context: the statement, the files and lines to read, the points
   to test first, the stop rule, the output file. The first item is the
   check request for the statements of this run, by a model that did not
   write them. Add a list "not proposed", with reasons.
8. **Appendix:** the tables of steps 2 to 8, the approach registry, and
   short lists of the assumptions most likely to be wrong, the assumptions
   most expensive to be wrong, and literature proofs worth translating.

End the file with one line that starts `RESULT:` and states what was proved
(with marks), what was corrected, and what stays open.

Before you finish, read the report's strong words ("new", "every", "no
candidate", "exact", "proves", "theorem", "sound") against what the run
actually did, and correct each one that says more.

The report must not claim the wall is solved without a proof, a decisive
runner or a decisive no-go artifact.

## Non-Negotiables

- Plain language first. The report's first three sections contain no
  undefined jargon and no lane fixture presented as framework content.
- Fresh first, compare later. Steps 2 to 4 are written with the attack
  files closed, and step 5 opens all of them. Nothing is "new" without the
  search of step 5.
- Every inventory item and every statement carries a mark, and a mark is
  never stronger than its weakest input.
- A discard test refutes a tool only in the valid form of step 6. Every
  set-aside method is re-judged; none is skipped.
- Do not over-rely on existing framework content. It is evidence, and the
  exercise may find it wrong, overbroad or misframed.
- Do not miss approved primitives or overstate what they grant (step 4).
- Owner rules and the limits of the target's contract are not broken in the
  exercise. They are listed in group (f) and questioned on paper only.
- Do not apply audit verdicts, promote claims, add axioms, primitives or
  imports, or declare the wall solved without an actual proof, runner or
  decisive no-go artifact.
- Name an axiom change only as a price. Draft candidate wording only when the
  owner asks for it. It must start from a layman-simple sentence, say why the
  existing axioms cannot supply it, and be marked as not adopted.
- Do not import literature as proof. Translate it into repo-native theory,
  check it, and cite the source. Credit by name every author whose work is
  used.
- A run may refute or guide. It never discharges a statement by itself.
- Write the file as you go. Say who wrote it and who checked what.
- Report honestly when the exercise produced only a map.
- Before quoting a subagent's result, check its strong words ("every",
  "no candidate", "exact", "proves") against what it actually computed.
````

## 3. The command wrapper and `agents/openai.yaml` (full text)

### 3.1 `.claude/commands/exercise.md`

Ready to replace the file at main 1ddab64621 (97 lines there). 135 lines, 7,930 bytes, sha256 prefix `aa3ee55407be7f91`. It keeps the v1 layout (invocation, examples, required behaviour, non-negotiables) and the v1 text on primitives word for word. It adds the pointer to `procedures/research.md` and the sentence "where the two differ, the skill wins", so that the wrapper is a summary and not a second home of the rules.

````markdown
# /exercise — Physics Wall Exercise

Run the repo-native exercise skill from:

`docs/ai_methodology/skills/exercise/SKILL.md`

`docs/ai_methodology/procedures/research.md` step 3 says when a target runs
it. The skill says how. This file is a summary; where the two differ, the
skill wins.

## Invocation

```text
/exercise "<physics wall or blocker>" [--artifact] [--slug SLUG] [--subagents N] [--no-web] [--test-budget H]
```

Examples:

```text
/exercise "we cannot derive the K-real generation readout instrument"
/exercise "Koide r=1/2 is available as a dial but not selected" --artifact
/exercise "Planck-scale primitive keeps leaking into bounded status" --subagents 4
/exercise "every attack on this lemma stops at the same step; audit the tests that discarded the other tools"
```

## Required Behavior

1. Read the skill file above before acting.
2. Perform the skill freshness check described in
   `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`.
3. Perform the Framework Refresher Read required by the skill: the current
   minimal axioms, primitive registry check, approved primitive source notes,
   axiom-premise registry, derivation-obligation registry, review-loop skill
   and controlled vocabulary. Every subagent does the same and states which
   surfaces it read. A standalone proof target that reads no framework axiom
   reads its `GOAL.md` contract instead, and says so.
4. Write the output file as you go: header (model, effort, commit, what the
   run did not cover), a status block kept current, then each step on disk
   before the next is thought through. Every item and statement carries a
   mark; no mark is stronger than its weakest input.
5. Step 0: locate the repo's own record of the wall (landed notes, open PRs,
   queue rows, registries, decision records, panels, earlier exercises, held
   blocks, candidate packs), by object as well as by title. Sort it into
   "open now" (target, wall, definitions, statements of theorems) and
   "closed until step 5" (attack files, route notes, digests of methods,
   set-aside lists). Reuse the literature record, or run and record the
   search. `--no-web` makes that search offline, with unavailable or
   unverified sources labelled explicitly.
6. Step 1: state the wall twice, plainly for a non-physicist and precisely.
   Check the plain version with a blind restatement where a fresh agent is
   allowed.
7. Step 2: the inventory. List what is known to be true, each item with a
   mark: definition, axiom or primitive, supplied choice, theorem (source,
   standing, how much of the source was read), or belief.
8. Step 3: reason up from the inventory only. What follows at once; the
   least a solution must contain; the smallest object; where the result can
   come from; whether the requirement is stated too strongly; the price.
   End with numbered conclusions.
9. Step 4: the assumptions table, in six groups: target, formulation,
   reduction, discard tests, beliefs, working rules. For each row: where it
   is used, needed or only habit, what follows if it is wrong, whether a
   change makes the problem easier, the check. Owner rules are listed and
   kept. Rank the rows by how much the problem changes if they are dropped.
10. Step 5: open the closed files and compare. Mark each item yes, partly or
    new, with the place. Search the whole lane record for the statement
    before writing "new", and write the search scope.
11. Step 6: the blockage. List every method that was set aside, with the
    reason given. Say from the definitions what a tool must do. Audit every
    discard test in its valid form: a method is refuted as a tool only by a
    model in its class where its hypothesis holds and the needed statement
    fails; otherwise the test only says what a proof of the hypothesis must
    use, and from which parameter value. Say how each test's failure is
    known (theorem or belief). Re-judge every verdict.
12. Step 7: routes. Take them from the dropped assumptions, the tools that
    came back and the new forms of the target; add independent passes across
    materially different families (`--subagents N`, default 0 = isolated
    passes), with one lens from outside the lane and one pass arguing that
    the wall is misframed. Revisit the literature for new questions only.
    Give every route to a different pass to break; target-equivalent endings
    are `blocked-equivalent`. Rank by what a route would change, divided by
    its cost.
13. Step 8: real attempts on the best two or three routes: prove the first
    lemma, find a counterexample, or reduce to one exact statement. Search
    the open registry and queue before each attempt. Pre-register every
    run; never change a reading after seeing the result; say exactly which
    class a search covered; compute decisive quantities directly. Report and
    preserve raw failures immediately. Before interpreting them as negative
    conclusions or no-go results, obtain a fresh adversarial check under the
    allowed review configuration, and label same-family checks honestly. A
    deferred test names what it is waiting on.
14. Step 9: report plain language first: the wall, what was found, filters
    corrected, at most three routes, what not to do, the exact price, work
    items as complete briefs (the first is the check request), and one
    `RESULT:` line. Read the report's strong words against what the run did.
    With `--artifact`, write the packet under
    `.claude/science/exercises/<slug>/`; inside a target, write the one file
    the brief names.

## Non-Negotiables

- Use the strongest available reasoning. Use subagents only when the caller
  allows them; they must be maximum-reasoning physics agents that run the
  framework refresher before their slice. Report their actual model family
  and do not call same-family agents independent referees.
- Fresh first, compare later: steps 2 to 4 are written with the attack files
  closed; nothing is "new" without the search of step 5.
- A discard test refutes a tool only in the valid form of step 6. Every
  set-aside method is re-judged.
- Do not over-rely on existing framework content. It may be useful evidence,
  but the exercise is allowed to find it wrong, overbroad, or misframed.
- Do not miss approved primitives. The registered `scale_reference_primitive`
  grants the Planck scale reference as units conversion only, without making
  downstream rows bounded and without granting dimensionless content. The
  registered `kinetic_isotropy_primitive` grants only structural OS0
  kinetic-form isotropy `c_t = c_s`; it does not supply dynamics, a
  Lorentz-closure theorem, scale, spacing-ratio theorem, selector, or empirical
  content. The registered `realized_state_primitive` grants only pointwise
  evaluation at a supplied law-admissible realized state; it does not supply
  a state, state-selection rule, measure, typicality or genericity assumption,
  weighting, probability rule, or any state-contingent value (quantities that
  vary across the law-admissible family remain registered data).
- Owner rules and the limits of the target's contract are not broken in the
  exercise. They are questioned on paper only.
- Do not apply audit verdicts, promote claims, add axioms, primitives or
  imports, or declare the wall solved without an actual proof, runner, or
  decisive no-go artifact. A price, a misframing or a corrected filter needs
  a proof or decisive checked evidence.
- A run may refute or guide. It never discharges a statement by itself.
- Name an axiom change only as a price. Draft wording only when the owner asks,
  starting from a layman-simple sentence.
- Do not import literature as proof. Translate it into repo-native theory,
  script/review it, and cite the source.
- Nothing the exercise writes is `checked`. Say who wrote it and who checked
  what.
- A map of attacks with nothing tried is reported as exactly that.
````

### 3.2 `docs/ai_methodology/skills/exercise/agents/openai.yaml`

Two strings change; the policy is unchanged. 7 lines, 520 bytes, sha256 prefix `b0b0dcc7ab1a21c9`. The file parses as YAML (checked with `yaml.safe_load`; the frontmatter of the new `SKILL.md` parses too, keys `name` and `description`, description 833 characters).

Old:

```yaml
  short_description: "Get past a physics wall, or price it"
  default_prompt: "Use $exercise to state the current physics wall plainly, find the premise it rests on, generate and try to kill independent routes, run the cheapest decisive test, and report in plain language."
```

New (full file):

```yaml
interface:
  display_name: "Exercise"
  short_description: "Get past a blocked lane, or price it"
  default_prompt: "Use $exercise on the current wall: state it plainly, list what is known to be true with a mark on each item, reason up from that list before reading earlier attacks, list every assumption and what follows if it is wrong, audit the discard tests and re-judge every set-aside method, compare with earlier work, make real attempts, and report in plain language."

policy:
  allow_implicit_invocation: true
```

Tooling. I searched main at 1ddab64621 (a shallow clone without blobs in `/tmp/exskill-v2-clone/`, then `git grep -i exercise` over `scripts/check_*`, `scripts/validate_*`, `scripts/sync_*`, `scripts/lab_ops.py`, `tests/`, `.github/`, `docs/ai_methodology/` without `raw/`, `.claude/commands/`, `AGENTS.md`, `CLAUDE.md`: 111 files). No script, test or workflow file in that set names the exercise skill or command, which agrees with `PROCEDURES.md` L32. Other files that name it, and need no edit: `.claude/commands/pstack.md` L39 and L81, `docs/ai_methodology/README.md` L37 ("Reframe a blocked investigation"), `procedures/research.md` L78 and L147 (edited in part 4), `skills/physics-loop/references/assumption-import-audit.md` L67. Not searched: the other 1000+ files under `scripts/`. Not run: `scripts/sync_methodology_skills.py --check` (it compares installed copies outside the repository).

## 4. Exact edits to the process stack

All line numbers are those of the files at main 1ddab64621. I applied every edit below to a scratch copy with a script that requires the old text to occur exactly once, and counted lines afterwards. No edit touches axiom text, audit language, a ledger or a setting.

### 4.0 Where the rule lives, and what the row asked

The row asks for edits to `docs/ai_methodology/SCIENCE_WORKFLOW.md` that say when the exercise runs. At 1ddab64621 that file is a section map: "It adds no rule and grants no status. Remove it when nothing cites it" (L6-7). The rule "when" is in `docs/ai_methodology/procedures/research.md` step 3 (L77-78), and `RULES.md` section 7 says "One home per rule. Other files point to it and none restate it." So:

- E1 and E2 put the rule in `procedures/research.md`, where it already is. This is my recommendation.
- E4 gives `SCIENCE_WORKFLOW.md` a pointer row only, so that the map still adds no rule. Land it only if the lead wants the map to name the exercise.
- If the lead's branch has a `SCIENCE_WORKFLOW.md` that still holds rules (the copy in this checkout is such an older file, 242 lines), the same sentences go there in its Section 7, "Selecting work"; I give no old/new text for it because main is the stated target.

`procedures/research.md` is at its 150-line budget and `RULES.md` at its 200-line budget (`RULES.md` section 7: "Adding past a budget means removing something"). E1 and E2 keep `research.md` at 150 lines. No edit to `RULES.md` or `SETTINGS.md` is proposed.

### 4.1 E1: `docs/ai_methodology/procedures/research.md`, step 3, L77-79 (the rule: when)

Old:

```text
   never a status report. A part that keeps failing the same way gets the wall
   exercise; a map of attacks with nothing tried is not a result. Long and
   numeric jobs pass `lab_ops.py preflight`; numerics hold `numeric-lock`.
```

New:

```text
   never a status report. The wall exercise comes first when a part keeps
   failing the same way, and when a discard test decides a route. Long and
   numeric jobs pass `lab_ops.py preflight`; numerics hold `numeric-lock`.
```

What changes. (1) "Comes first": the exercise runs before the next attempt on the blocked part, so before a new long author run. (2) A second trigger: a route choice that rests on a discard test. (3) Removed, to stay inside the budget: "a map of attacks with nothing tried is not a result". That rule stays in the skill ("A long map of possible attacks with nothing tried is not success. Say so") and in the sentence before it in step 3 ("never a status report"). Lines: 150 before, 150 after; widest prose line 80, as before.

### 4.2 E2: `docs/ai_methodology/procedures/research.md`, step references, L147 (relation to attempts, races and panels)

Old (one table row):

```text
| 3 | `long-running-execution.md`, Lab Operation; `../../exercise/SKILL.md`; `DISCOVERY.md`, Deep Work Rules | Units, leases, handover, disagreement; the wall exercise; fan-out when stuck |
```

New (one table row):

```text
| 3 | `long-running-execution.md`, Lab Operation; `../../exercise/SKILL.md`; `DISCOVERY.md`, Deep Work Rules | Units, leases, handover, disagreement; the wall exercise, run before any further long attempt on a blocked part (it audits the lane's assumptions and discard tests; its work items brief the next attempt, race or panel); fan-out when stuck |
```

Optional, for truth after the skill is replaced (L138-141; 4 lines before, 4 after):

Old:

```text
say so. All predate this file: a loop-pack file they name is now the part file,
and `RULES.md` wins any difference, status words too.
```

New:

```text
say so. All but `exercise/SKILL.md` predate this file: a loop-pack file they
name is now the part file, and `RULES.md` wins any difference, status words too.
```

### 4.3 E3: `.claude/commands/first-principles.md`, section "If the Derivation Blocks", after L96 (relation to first-principles)

Old (the end of the paragraph, L95-96):

```text
closed route only with a concrete changed mechanism, scope, premise, or
counterexample that addresses the original proof.
```

New:

```text
closed route only with a concrete changed mechanism, scope, premise, or
counterexample that addresses the original proof.

When a second route stops at the same wall, run `/exercise` on that wall
before a third route. Its inventory starts from this file's premise ledger.
It lists the assumptions behind the target and behind the routes, and it
audits the reasons for which earlier routes were set aside. A route that
survives it comes back here as a new derivation.
```

Six lines added (168 to 174). The "Allowed Starting Points" section, which holds axiom text, and the `/no-go-gate` sentence are not touched. The other direction of the relation is in the skill, section "Relation to other procedures".

### 4.4 E4: `docs/ai_methodology/SCIENCE_WORKFLOW.md`, table "Where each section went", after L27 (pointer only; optional)

Old:

```text
| Section 6, stages and authority | `RULES.md` section 4; `PROCEDURES.md` |
```

New:

```text
| Section 6, stages and authority | `RULES.md` section 4; `PROCEDURES.md` |
| Section 6, "Skills by job", the exercise | `procedures/research.md` step 3 (when it runs); `skills/exercise/SKILL.md` (how) |
```

Why this row and no more: the older file named the exercise once, in the "Skills by job" line of its Section 6 (this checkout, `docs/ai_methodology/SCIENCE_WORKFLOW.md` L130-131). The map resolves old references; this row resolves that one. It states no rule.

### 4.5 E5: `docs/ai_methodology/PROCEDURES.md`, L27-28 (optional; for truth after the skill is replaced)

Old:

```text
A skill's own `SKILL.md` entry file is superseded by the procedure below. It
stays in place, unedited, because tooling still reads it.
```

New:

```text
A skill's own `SKILL.md` entry file is superseded by the procedure below. It
stays in place, unedited, because tooling still reads it. One exception:
`skills/exercise/SKILL.md` was revised after the procedures and is current.
```

One line added (48 to 49). Without it, "unedited" is false for one skill. The lead may read "unedited" as a rule against this whole item; then the owner's request (row 721) is the override, and the PR should say so.

### 4.6 What `RULES.md` section 7 asks of a process change

"Each change states the defect, a realistic case it decides differently, how it will be measured, and the result that reverts it." Text for the pull request:

- **Defect.** The lane discarded tools with two tests in a wording that is false (`library/gap-crux-fp.md` L274-276, checked in row 716), and three of 22 verdicts were too strong (L309). v1 of the skill has no step that audits a lane's filters, no mark on what is known, and no rule for the word "new"; the run of row 712 marked as new a statement of row 700 (`library/gap-crux-fp-check.md` L126-139). The procedure names no time for the exercise. In this lane two long author runs (rows 697, 708) came before it; I cannot say that an earlier exercise would have changed them.
- **A case it decides differently.** A tool is proposed, and a digest says "it also holds for U(1)". Before: set aside. After: step 6c asks for a model in the tool's class where its hypothesis holds and the needed statement fails; with none, the tool stays, with the range where the test binds. Second case: a part has failed the same way twice and a lead wants another long author run. Before: launch. After: the exercise runs first, and its work items brief the run.
- **Measure.** For each run of the exercise, from its file and its check record: the number of discard tests or verdicts corrected; the number of its statements that a check finds right, right after correction, and wrong; the number of "new" marks that a check finds wrong (the aim is zero); its cost; and whether the next long run on that part was changed or cancelled by it.
- **Revert.** If three runs in a row correct no filter and give no statement on the path of their target, revert E1 to the old sentence and keep the skill as an option the lead may choose. If a check again finds a wrong "new" mark in a run that followed step 5, step 5 has failed: fix that step before the next run.

Not proposed: a new row in `SETTINGS.md`. Its method defaults are the owner's ("Only the owner changes them"), and E1 already carries the timing.
