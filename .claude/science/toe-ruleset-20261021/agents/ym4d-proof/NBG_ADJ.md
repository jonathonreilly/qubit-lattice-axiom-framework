# NBG_ADJ.md — adjudication of the (N-bg) / (G♯_0-field) / (GAP-Z) obstruction count

Worker: T55-K (adjudicator). Lane: ym4d-proof. Session 25.

---

## §0. PRE-STATED — statements only

**This is the first edit to this file. UTC 2026-10-28T21:33:53Z.**

This section cites nothing produced in session 25 except the names of the two files placed under
adjudication: `NBG_A.md` and `NBG_B.md`. It contains no derivation, no constant, and no verdict.
Everything below it was written after it.

### §0.1 What this file is for

Two workers attacked the same question in parallel without reading each other. One reports that
(N-bg), (G♯_0-field) and (GAP-Z) are **one** obstruction; the other reports **three**. This file rules
on the count and on the dependency structure behind it. It does not prefer a status label: a PROVEN
outranks an ARGUED only if its proof survives reading.

### §0.2 Targets, stated before any work

- **(T-K1)** Decide whether **(GAP-Z)|_{Z=1} = M** of LINEAR_PACKAGE Theorem 4.2′, by reading
  (GAP-Z)'s own definition in BFT_B.md and Theorem 4.2′ in LINEAR_PACKAGE.md. The step that can fail
  is **admissibility of Z = 1 inside (GAP-Z)'s own quantifier**; (T-K1) is decided only if that step
  is checked explicitly and separately.
- **(T-K2)** Decide whether **(N-bg) ⟵ (GAP-Z)** (the reduction claimed on the (N-bg) side) survives,
  by reading the three hypotheses of the theorem that carries it and checking whether the hypothesis
  the reduction's author could not prove is doing the work. A reduction whose unproven hypothesis
  already entails the conclusion is **circular** and does not reduce anything; a reduction whose
  unproven hypothesis is strictly weaker than the conclusion is a genuine reduction.
- **(T-K3)** Evaluate **all six ordered implications** among the three items, in both directions, each
  one against the quantifiers its *consumer* needs rather than the quantifiers the source statement
  asserts. A single surviving implication changes the count.
- **(T-K4)** State the **count** and the **dependency graph**: which item implies which, under what
  named hypotheses, and how many genuinely independent items remain.
- **(T-K5)** Attribute. For each worker, state which specific claim survives and which does not, and
  say explicitly where an argument is right while the count built on it is wrong.
- **(T-K6)** Rule on whether PROOF.md's [S25-fix 2] stands or must be reversed, and if it must be
  reversed, supply append-ready replacement text in a `## FOR OTHER FILES (not edited)` section,
  since PROOF.md is the lead's to edit.

### §0.3 Named failure modes for this adjudication, stated in advance

- **ADJ-F1 (too convenient).** The hypothesis that "both are right, the answer is two" is attractive
  because it costs neither worker an argument. It fails if the reduction of (T-K2) and the
  non-identity of (T-K1) cannot both be true of the *same* (GAP-Z) — i.e. if the (GAP-Z) that (N-bg)
  reduces to is not the (GAP-Z) whose restriction to Z = 1 is M. If the lane carries two (GAP-Z)s,
  the count is not two and the convenient answer is wrong.
- **ADJ-F2 (label deference).** Ruling for the PROVEN over the ARGUED without re-deriving the PROVEN.
  Controlled by requiring that (T-K1) be settled from the primary definitions, not from either
  worker's quotation of them.
- **ADJ-F3 (line-number drift).** Every cite verified by **string**, never by line number. A cite that
  no longer says what the citing file claims is reported as a defect of the citing file.
- **ADJ-F4 (phrase collision inherited).** Both workers may share one ambiguous phrase, in which case
  the disagreement is verbal and the count question is ill-posed until the phrase is split. If this
  occurs, the ruling must split the phrase and then count.
- **ADJ-F5 (counting units).** "Obstruction" is itself undefined. The count depends on whether one
  counts *statements*, *unproven inputs*, or *paper-scale tasks*. If the two workers are counting in
  different units, that must be said and the count given in all units used.

### §0.4 Admissible outcomes, enumerated before looking

Exactly one of: **ONE** (all three collapse), **TWO** (reduction holds, identity fails), **THREE**
(no implication survives), or **ILL-POSED-THEN-N** (the question is verbal, resolved by splitting a
phrase, after which the count is N). Any other outcome is a failure of this adjudication to decide
and must be reported as such.

### §0.5 Scope and process

Writes only `NBG_ADJ.md` and `checks/ad1_*`. Reads anything. No git. Appends only. If a numeric or
symbolic check is run, criteria are pre-registered in `checks/ad1_*_criteria.md` before the script is
written, and every gate carries a designed-FAIL control whose firing is reported.

---
