lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T08:03Z

# gap-short-step-max: the 4D short step, a selective gain at order-one response

Queue row 1018 of `FINISH.md`, pinned at commit df74a7421, branch `claude/ym4d-hard-route`.
Worker: Claude Fable 5.2, max effort, Mac mini worker 3. One session, no subagents.
This is research-stage working state. It grants no status.

Marks used below: PROVED (every step written here), ARGUED (argument written, a step not fully written), OPEN, FAILS (counterexample or failing step written).

## Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Read.** `parts/gap.md`; rows 1009, 1010 (2D short step, [28] (3.52)); `library/gap-pinned-cell-gauge-max.md` and its check; `library/gap-invent-selective-max.md` and its check; the exercise skill at main commit 8b11ae2bb9. Duplicate check against `library/open-core.md` and the FINISH rows (rows 1016, 1017 run in parallel and are not redone). Record what is read and what is established.
2. **Target.** Write the 4D short step as an exact inequality: the quantity R(Q), the class closed under the conditioning the proof uses, the statement R(lQ) <= R(Q) - delta at order-one R(Q). Show by hand that it is false for compact U(1) and for a product with a massless factor.
3. **Route (iii-b), barrier first.** Try to build an averaged or modified model that keeps every identity the tools use (bracket term of Proposition W, reflection positivity) and has no short step. If it exists, name what a proof must use beyond the bracket.
4. **Route (ii), field-dependent covariant moves.** Jacobian control and the curl form of the cost at order-one response; test against Lemma WN and row 1013 C8.
5. **Route (iii-a), energy increment.** Write the dichotomy lemma (response drops, or a structure energy bounded by the action rises); test both halves.
6. **Tests.** Each surviving piece against Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, Lemma SLAB, compact U(1), frozen Q_8 and 2T, the five-dimensional test of `library/gap-crux-fp.md`, the instanton cost of 6.3 of row 1013.
7. **First survivor.** Prove it by hand, or build the counterexample.
8. **Result.** Marks per piece, what stays open, one RESULT line.

## Log

- 2026-11-15T20:03Z. File created. No earlier run of this item exists at the pinned commit.
- (between 20:03Z and 20:17Z; time not measured) Step 1, progress marker 1a. Read in full: `GOAL.md`; `FINISH.md` L1-90, L299-356 and rows 1009-1018; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md` (row 1011); `library/gap-invent-selective-max.md` (row 1013); the exercise skill at main 8b11ae2bb9 and its reference `proof-search-governance.md` (both fetched into `/tmp/gss-skill-w3/`). Still to read in this step: the two checks (rows 1014, 1015), rows 1009 and 1010 at the short step ([28] (3.52)), the statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the five-dimensional test, and the files of rows 1016, 1017 if they exist at this pin (to avoid redoing them).
- 2026-11-15T20:17Z (`date -u`). Step 1 done. See Section 1. From here on every log time is read from `date -u` when the line is written.

## 1. Step 1 result: provenance, what was read, where the record sits, duplicate check (exercise step 0)

**Provenance.** Anthropic, Claude Fable 5.2, max effort, one session on Mac mini worker 3, no subagents. Nothing in this file is checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no computer-assisted step; proofs that could be formalized in Lean) replaces the framework refresher read of the exercise skill. The skill was fetched at main 8b11ae2bb9 with its one reference file `proof-search-governance.md` into `/tmp/gss-skill-w3/`; both were read in full.

**Credit.** The 2D short step is OpenAI's (posted, unrefereed; github.com/openai/math commit 4eaee8754825; "Sharp mass bounds for the two-dimensional O(4) model", (3.52) and Section 3.8; "The canonical massive continuum limit of the two-dimensional O(3) model", (2.30)), as read by rows 1009 and 1010 (Claude Opus 5.5, unchecked). Rows 1011 and 1013 (Claude Fable 5.2) with their checks 1014 and 1015 (Claude Opus 5.5) supply Propositions A, W, B, B', SEAG, Lemmas CEN, EMB, FR, WN, TWIST, JEN, SLAB and the reopen conditions. Lemma GG is row 1004's. Balaban's background-field results and the Sussman-Alpoge account (with Claude and Codex as authors of their text) are credited where they are used.

**Read in full:** `GOAL.md`; `FINISH.md` L1-90, L299-356, rows 1009-1018; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md`; `library/gap-invent-selective-max.md`; the skill and its reference. **Read in part:** `library/gap-invent-selective-check.md` L262-473 (the two ARGUED remarks, W2, verdicts); `library/prior/gap-o4-pinned-cell-read-opus.md` L60-199 (the 2D class, Ward identity, variance gain, the short step (3.52), the iteration 3.8); `library/gap-crux-restate.md` L27-47, L176-222 (objects, Lemmas K, X, E, Theorem S); `library/gap-mid-max.md` L58-70 ((CAS)); `library/gap-crux-exercise3-max.md` L688-724 (Lemma PT); the first 60 lines of the in-progress files of rows 1016 and 1017. **Not read:** the rest of the lane (about 800 library files); the primary 2D texts (used through rows 1009, 1010, 1013).

**The 2D short step, as rows 1009 and 1013 restate it (OpenAI's mathematics; unchecked reading).** The class is all pinned squares, all pins, all signed strengths up to b, all fixed right twists. The monotone is the class bound h of the twist stiffness H. One step from side R to side L R uses the exact identity "H_Q(A, A) = v |A|^2 - Var J(A)" (Gaussian augmentation at level v > h) and a lower bound on Var J(A) from the bracket term of the rotation Ward identity. Long regime: Var J(A) >= (log L)/pi - C[log B + (log L)^2/v]. **Short regime ([28] (3.52)): with a bounded number of frequency octaves (K_1 = 8M, K_2 = 256M), Var J(A) >= c_sh min(v, 1), c_sh absolute.** So each short step lowers h by c min(h, 1), from h of order log B down to B^(-D) in O(log B) steps. The same exact Ward identity serves at every value of h, because the rotation is an exact symmetry on every configuration.

**Where the lane's record sits on the objects of this row (located before any attack; rule 0a).**

| Object | Where | Standing there | Consequence for this row |
|---|---|---|---|
| The short step in periodic form: (CAS), "Delta((2a)^4) <= theta Delta(a^4) while 6.1 x 10^(-4) < Delta(a^4) <= M" | row 708, `library/gap-mid-max.md` L64-67; `parts/gap.md` L106-108, route RA | open; "as a mechanism it is empty: it restates the seed in steps"; blocked-equivalent | I do not attack (CAS). Section 2 names it as the periodic form of the target and says what the target adds: a response with a mechanism slot. |
| Reopen condition (ii): covariant moves, controlled Jacobian, curl cost form at order-one response | row 1013 7.2; row 1016 plan step 7 (in work on worker 1; its file at this pin has step 1 only) | open; row 1016 takes it in general, with the homogeneous-strength case of B' | Overlap named. This row's route (ii) is kept to what the row asks: the exact cost form of field-dependent moves at order-one response. I do not attack the homogeneous-strength case of B'. |
| Compactness and rigidity (critical element, branch G) | row 1017 (in work on worker 2; step 1 at this pin) | open | Not redone. Where route (iii-a) reduces to "no scale-invariant end", I name row 1017 and stop. |
| Adjoint Higgs family ends at compact U(1) | row 1004, `library/gap-outside-box-max.md` 6.2, Lemma GG (PROVED there; check 1008 HOLDS, same provider) | a test, not a tool | Used in route (iii-b) as the end point of a family of models with a colour frame; credited. |
| Five-dimensional test | `library/gap-crux-fp.md` F15 (L50), L76, L88, L266 | GUIDE (numerics) | Used as a belief-grade test only. |
| Energy increment, structure against randomness, a barrier model | `library/open-core.md`: no hit (grep: short step, selective, energy increment, barrier, covariant move, tree-transport, frameable). Lane: no file states a dichotomy of this kind (grep: energy increment, structure against randomness, regularity lemma, density increment, barrier model). | not on file | Routes (iii-a) and (iii-b) are not covered by another row. |
| Nilpotent groups, the Killing form | lane grep: no file | not on file | used in Section 4. |

**What this run does not cover (kept current).** No literature search beyond the lane's records (rows 1007, 1009, 1010, 1012 are the literature lens of this object; the row asks for none). The primary OpenAI texts were not re-read. PR branches other than this one were not searched. Rows 1016 and 1017 were read only at their first step.
