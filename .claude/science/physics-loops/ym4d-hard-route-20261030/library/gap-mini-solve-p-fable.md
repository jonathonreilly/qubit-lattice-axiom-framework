lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T15:52Z

# gap-mini-solve-p-fable: the mass gap of four-dimensional SU(2) Yang-Mills (row 1220)

Provenance: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit 7ec64b498. One session, no subagents.
This is research-stage working state. It grants no status. Nothing here is a public claim.

Labels: PROVED (argument written in full here), ARGUED (argument with a named gap), GUIDE (numeric or heuristic,
never a proof step), OPEN.

## 0. Status log

- 2026-11-20T03:52Z (date -u): file created. Plan: (1) read the row's new input, `library/prior/gap-onebound-read-sol.md`
  (row 1218), and the lane's state map `parts/gap.md`; (2) per the lesson of rows 1188-1198 (blind candidate
  lists are exhausted for this model family), start from an OPEN lemma with a consumer in the newest chain rows
  and from the new published input, not from a candidate list; (3) grep the registry before calling anything new;
  (4) attack one statement to closure, appending after each step.
- 2026-11-20T04:00Z (date -u): read FINISH.md rule sections, GOAL.md, row 1220 (this row), `library/prior/gap-onebound-read-sol.md`
  in full, `parts/gap.md` L1-104, and the RESULT lines of rows 1186-1218. Section 1 written from these.

## 1. Repo search and how the attack was chosen

**Repo search (this folder; cross-branch hits taken from row 1218's table, not searched again).** The row's
one new input is row 1218's reading of three published texts. Credit: (A) D. Bhattacharjee, U. Bhattacharya,
J. M. Lockwood, T. Romanov, I. J. Sessford, S. Singha Roy, "The Yang-Mills Mass Gap from One Bound at One Scale"
(Preprints.org 202611.1282); (B) Bhattacharjee, Bhattacharya, Lockwood, Romanov, "One Cube Estimate Implies the
Yang-Mills Mass Gap" (Hexagon 2610.00341v7); (C) Zeng Chunping, Hexagon 2611.00543v1 and 2611.00492v1. All are
read here through row 1218's digest unless a section below says a primary passage was read.

State of the lane taken as given (not re-derived):

- The Jaffe-Witten gap clause follows from the neutral one-cube bound (N-phys) and the matched continuum datum
  (row 1161 `gap-solve9-astra62.md` L146-148; row 1179). (N-phys) is the crux lemma (GLUE-FP)_sigma of rows 895
  and 920 with other constants (row 1184). Rows 1186-1215 restate it five ways: two-slice information (26), the
  binary test (28), the probability ratio of row 1192, the mass detector Q of row 1204, the wall test of row 1211.
  Each check (rows 1191, 1203, 1210, 1214) confirms the restatement and that the Wilson estimate is OPEN.
- Fifteen plain-brief rows of this model family (1188-1202, letters a to l) each generated candidate attacks
  from the target and found every one on the lane's map. The lesson recorded after row 1198: do not start from a
  candidate list again.

**How the attack was chosen.** Two questions decide the row.

1. Does the new published input supply, or shorten the way to, the missing Wilson estimate? Section 2 answers
   this with proofs, not by reading alone: for (B)'s weak-coupling theorem the answer is no, and the reason is
   exact (Lemma NULL below).
2. Which open statement with a consumer is attacked? Chosen in Section 3, after Section 2.
