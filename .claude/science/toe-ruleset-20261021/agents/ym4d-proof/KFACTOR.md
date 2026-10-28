# KFACTOR.md — the level-count factor k, attacked from the LEVEL-SUM side (target T55-S)

## §K0 PRE-STATED (first edit of this file; 2026-10-28T21:57Z UTC)

**This is the first edit of this file.** It contains STATEMENTS ONLY — my targets, written before any
derivation, before any grep beyond the orientation reads named below, and before any script. It cites
nothing produced in this session except by *name of the open question*, never by value.

Orientation reads completed before this edit (reads only, no derivation): the session-25 shared brief;
`HANDOFF.md`; `SESSION25_RESULTS.md` entries **T55-I**, **T55-J** and the **CONVERGENCE** block;
`BFT_A.md` l.200-260 and l.805-850.

### What I am attacking
The level-count factor — the ≈ 25(k−1) that the curvature half of BFT-5 clause (b) carries; equivalently
the two GAP-1 (F3) plain-current rows at `BFT_A.md` l.229, l.244 that have **no level decay**;
equivalently the sum Σ_l ‖j^c_l‖ of [RBA2-fix] B3 at `BFT_A.md` l.822-824; equivalently the missing
clause **(W2)/(SPD)** at `BFT_A.md` l.830-831.

A sibling worker (T55-R, `SPD_SIGMA.md`) attacks (W2)/(SPD) directly at positive σ. **I do not duplicate
that.** I attack the same obstruction from the LEVEL-SUM side.

### Targets, in the order I will attempt them

- **(S1) CONSUMER TOLERANCE — attempted FIRST, and it is a read, not a proof.**
  Determine whether the consumer(s) of the k-factor tolerate growth linear in k. Specifically: identify
  by file:line every consumer of the k-uniformity of Theorem NCE (i) / of BFT-5 clause (b)'s curvature
  half, and determine for each whether its own admissible window on the quantity it receives is
  k-independent, or is itself already O(1/k) or weaker (as T55-D reports for failure mode CURV-F2″ on a
  *related* parameter — a report I will verify by file:line before using it, not cite).
  **Pre-stated outcomes.** (S1-a) EVERY consumer tolerates O(k): the obstruction evaporates and I say so.
  (S1-b) SOME consumer requires k-uniformity strictly: name it by file:line; the obstruction stands and
  (S2)-(S4) proceed. (S1-c) The consumers disagree / the window cannot be read off: report as
  undetermined, do not guess.

- **(S2) IS THE SUM OVER k INDEPENDENT LEVELS?**
  Write out the level sum that actually produces the k-factor, and determine what the consumer actually
  needs summed. Then: **does π_l(j_l) decay in l for the sources actually fed in?** The general family is
  "uniform in l" by hypothesis; the question is whether the *class the consumer ever supplies* (the
  composite-co-closed class (cc), a cone, exact level-k data, Ran Q^T data) is a strictly smaller class on
  which decay is forced.
  **Pre-stated outcomes.** (S2-a) The fed class forces geometric decay: state and prove the restricted
  theorem, which is a different theorem from (W2)/(SPD) and may be true where the general one is not.
  (S2-b) The fed class demonstrably contains a no-decay family: exhibit it; the restricted route is dead
  and I say so. (S2-c) The fed class is not pinned down anywhere in the lane: report that as the finding
  — an unpinned source class is itself a defect.

- **(S3) IS 25(k−1) ATTAINED, OR AN ARTEFACT OF SUP-NORM SUMMATION?**
  Either construct an instance achieving growth linear in k, or show the linear growth arises only from
  bounding a sum of signed/structured contributions by a sum of sup-norms level by level — which is lead
  decision **D3**'s defect (absolute row/column-sum norms counting every leg at its sup size). Check in
  particular whether the Bianchi / one-leg-differentiation cancellation that takes K_p from 2.27 to ≈0.12
  on closed inputs applies to the level sum.
  **Pre-stated outcomes.** (S3-a) ATTAINED: exhibit an explicit admissible source family with
  ‖·‖ ≥ c·k; the factor is an object, no resummation can remove it, and only (S1) or (W2) can help.
  (S3-b) ARTEFACT: identify the exact step at which signs/structure are discarded, and bound the structured
  sum. (S3-c) UNDECIDED: say which of the two it is *not*, and what input would decide.

- **(S4) RESUMMATION RATHER THAN TERMWISE BOUNDING.**
  Try, in this order: (i) a signed/telescoping rearrangement of the level sum (summation by parts against
  the weight ω_l = L^{θ(k−l)}), exploiting any sign coherence of the recursion coefficients (T55-O reports
  sign coherence of the funnel coefficients for a different obstruction — to be verified in `GESIGN.md`
  by file:line, not cited); (ii) a Kotecký-Preiss / polymer criterion on the level index; (iii) a
  random-walk expansion in the level index.
  **Pre-stated outcome.** (S4-a) one of (i)-(iii) resums the k-linear sum to a k-uniform bound: state it
  with its hypotheses. (S4-b) each fails for a named reason: give the reason per route. I expect (S4-b)
  for (ii) and (iii) and regard (i) as the only one with a chance; recording that expectation now.

- **(S5) MEET T55-R IN THE MIDDLE.** State precisely what the level-sum side needs from (W2)/(SPD) — the
  *weakest* hypothesis on the level profile that makes my sum converge k-uniformly — so that T55-R's σ > 0
  target and my target are the same target, or provably are not.

### Statuses I may use
PROVEN / ARGUED / CONDITIONAL (input named) / GAP / OPEN, strictly. A failed check is reported as a FAIL
with script and output unaltered. Any probe run after seeing a result is labelled **post-hoc**.

### Gates and controls (pre-committed)
Any numeric or symbolic gate I run gets a **designed-FAIL control**: an input I know should fail it,
reported as having fired. A gate with no fired control is reported as **not evidence**. Criteria files
precede scripts and contain no constant derived in this session. Arithmetic is exact (Fractions /
symbolic) in plain python; no numeric lock needed.

### Symbol discipline (defect 1)
θ is three distinct objects and α is two; ≥13 C_1, ≥11 c_1, ≥5 κ; `c_RS` and `n_♯` are each two objects.
Every symbol I use below is pinned by file:line at first use. Targets in `PROOF.md` are located **by
string, never by line number**.

### What I will NOT do
No git. I write only `KFACTOR.md` and `checks/kf1_*`. Demands on other files go in a
"## FOR OTHER FILES (not edited)" section at the end of this file.

---


---
**[LEAD, 2026-10-28T22:11:08Z] ABANDONED DRAFT.** This worker ran on claude-opus-5 (wrong model) and was STOPPED mid-run by the lead on the owner's instruction. Nothing in this file is a result. The target will be re-run on Opus 5.5.
