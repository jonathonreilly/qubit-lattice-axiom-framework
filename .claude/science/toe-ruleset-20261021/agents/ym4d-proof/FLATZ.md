# FLATZ.md — the flat 𝔐-pair composite-slice bound: pinning it, and settling its status

**Target T55-Q.** Owner: the T55-Q worker. Writes only this file and `checks/fz1_*`.

---

## §0. PRE-STATED — statements only

**This is the first edit to this file. Written 2026-10-28 21:54 UTC, before any derivation, any grep
of lane A or lane B beyond the three files named below as inputs, and any script.** It cites nothing
produced in session 25 except to *name* its inputs.

### §0.1 Inputs I am allowed to have read before writing this

1. `DRIVE_BRIEF_S25.md` (the shared brief, including the session-25 addendum).
2. `HANDOFF.md`.
3. `SESSION25_RESULTS.md`, the **T55-D** and **T55-K** entries.
4. `NBG_ADJ.md` §2, §4, §5 and its `## FOR OTHER FILES (not edited)` section, in particular
   **finding A6**.

Nothing else has been read at the time of writing. In particular I have not yet opened `BFT_B.md`,
`BFT_A.md`, `BFT_B_LOG.md`, `PROOF.md`, `NORMS.md`, `LINEAR_PACKAGE.md`, `RTARGET.md`, `HESSREL.md`
or `NBG_A.md`.

### §0.2 The question, as handed to me

NBG_ADJ's finding **A6** asserts that NBG_A §A4.3's route **(HESS-rel)** — a Neumann series taking the
flat chain-Hessian inverse to the Z-deformed one — names the **wrong flat input**. A6 says the right
input is a **fourth object**: the **Z = 1 composite-slice chain-Hessian inverse bound in lane B's
𝔐 → Y pair**, distinct from (G♯_0-field) (§33 pair, per-level slice), from (GAP-Z) (general Z), and
from the flat package constant M. A6 is marked **ARGUED**, with the disclosure that the worker searched
for a *record* of that bound rather than for a proof.

### §0.3 Targets, stated before any work

- **(Q1) PIN.** State the fourth object with full quantifiers: what operator, on which slice, between
  which two norms, at which background, uniform in which parameters, with which outputs. Give it a
  name that is not already in use in this lane.
- **(Q2) SEPARATE.** Distinguish it, clause by clause, from (a) (G♯_0-field), (b) (GAP-Z) in each of
  the readings the lane carries, (c) the flat package constant M, and (d) any lane-A object that is
  adjacent to it. The separation must be by **quantifier**, not by name, because the dispute that
  produced this target was two names for one phrase.
- **(Q3) SEARCH.** Determine whether the object is *stated* anywhere in lane B (`BFT_B.md`,
  `BFT_B_LOG.md`) or lane A (`BFT_A.md`), under this or any other name, including backticked
  variants that a plain grep for the prose form would miss.
- **(Q4) STATUS.** Determine whether it is **proven** anywhere, **implied** by something proven, or
  **open**; and if open, attempt a proof.
- **(Q5) NO-GO REACH.** Verify or refute the reading (made by NBG_A §A4.3 and endorsed by NBG_ADJ
  §4.1) that **BFT_B §41.5 (i)'s no-go does not reach a Neumann series**, on the ground that the no-go
  is about *conjugation* and the symbol method. Verify this by reading §41.5 (i) itself, not by
  citing either file's report of it.
- **(Q6) VERDICT.** State whether the cheapest route to (GAP-Z) is **open**, **dead**, or
  **undetermined**, and say what the lane should do next on (GAP-Z).

### §0.4 Named failure modes, stated in advance

These are the ways I expect this target to go wrong. I will report each as OCCURS / DOES NOT OCCUR.

- **FZ-F1 (the fifth object).** I "find" the object in lane B, but what I find differs from the
  object (HESS-rel) needs in a quantifier — pair, slice, background, uniformity, or output class — and
  I have therefore produced a *fifth* name for the collision rather than settling the fourth. Guard:
  every claimed match must be checked against all six quantifier slots of §0.3 (Q1), in a table, with
  file:line for each slot.
- **FZ-F2 (the Neumann series does not close).** The object exists and is proven, but the Neumann
  series still fails, because the perturbation estimate and the inverse estimate are in pairs that
  compose the wrong way (`A^{-1} : Y → 𝔐` against `E : 𝔐 → Y` is what is needed; `A^{-1} : 𝔐 → Y`
  would be useless), or because the smallness condition `‖A^{-1}E‖ < 1` is not achievable uniformly in
  k. Guard: write the composition explicitly with arrows, and write the smallness condition out with
  its k-dependence, before declaring the route open.
- **FZ-F3 (the no-go does reach it).** §41.5 (i) turns out to be about the *inverse itself* rather
  than about conjugation, in which case the route dies and both NBG_A and NBG_ADJ are wrong about it.
  Guard: quote §41.5 (i) in full and decide from the quotation.
- **FZ-F4 (A6's premise is wrong).** (HESS-rel) is *not* stated in the 𝔐 → Y pair, or (G♯_0-field) is
  *not* in the §33 pair / per-level slice, in which case A6's "wrong input" finding collapses and
  NBG_A's original naming was right. Guard: read BFT_B l.3840 and BFT_B §41.2 (c) directly; do not
  take the pair assignments from NBG_ADJ.
- **FZ-F5 (recorded after all).** The object IS recorded, and A6's "status recorded NOWHERE" is an
  artefact of the search terms A6 used. This would be the most valuable outcome and the one I should
  work hardest to produce. Guard: search for the *mathematical content* (operator, slice, pair) and
  not only for the phrase.
- **FZ-F6 (my own tautology).** Any gate I write to test "is the object present" is satisfiable by
  the object's own defining words and would pass on a decoy. Guard: every gate gets a designed-FAIL
  control built from a decoy object that is adjacent but wrong in one quantifier slot, and I report
  that the control fired.

### §0.5 Admissible outcomes, enumerated before looking

Exactly one of:

- **(O-PROVEN)** The object is proven in lane A or lane B under some name; the cheapest route to
  (GAP-Z) is OPEN and should be walked.
- **(O-IMPLIED)** Not stated, but implied by a result that is proven; same consequence, with the
  implication written out.
- **(O-OPEN-REACHABLE)** Not recorded and not implied, but I can state what it needs and give a
  partial or full proof.
- **(O-OPEN-HARD)** Not recorded, not implied, and I cannot prove it; it is a genuine new open item
  of stated size.
- **(O-FALSE)** The object is false, or blocked by a known no-go that reaches it. The (HESS-rel)
  route dies.

### §0.6 Process commitments

- Rule 2: any numeric or symbolic check gets `checks/fz1_<x>_criteria.md` with pre-registered
  PASS/FAIL **before** the script, and the criteria will contain no constant derived in this session.
- Rule 3: statuses PROVEN / ARGUED / CONDITIONAL / GAP / OPEN used strictly. "Still not recorded and
  I could not prove it" is a result and will be reported as one, not dressed up.
- Rule 6: exact rational/symbolic arithmetic in plain python only; no numeric lock taken.
- Rule 8: append-only; a `## FOR OTHER FILES (not edited)` section at the end for anything I want
  changed in BFT_B.md, NBG_A.md, PROOF.md or RTARGET.md.
- PROOF.md is located **by string, never by line number** — its numbering is reported to have drifted
  twice today, non-uniformly. A drifted citation I find is itself reported.
- A concurrent worker is walking (HESS-rel) itself into `HESSREL.md`. I will read it if it exists,
  will not wait on it, and will not duplicate it. My job is its input, not its route.

---
