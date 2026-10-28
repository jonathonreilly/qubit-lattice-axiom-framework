# COFUN.md — target T55-I: (CO-fun)

Owner: the T55-I worker (session 25). Writes confined to this file and `checks/cf1_*`.
Append-only after §1.

## 1. PRE-STATED (session 25, target T55-I) — statements only

**This is the FIRST edit of this file, written at 2026-10-28 21:33 UTC**, before any derivation of
mine, before any criteria file and before any script. Nothing in §1 cites a result produced in
session 25 — not by me and not by another worker. (My scope prompt referred me to a session-25 item
as the *reason* the target exists; no statement below depends on it, and nothing below is a claim
about it.)

Exploratory reading preceded this append and is not recorded as a result: the shared brief;
`SESSION25_RESULTS.md`; `BFT_B.md` §29-§32 and §34-§36.2; `REVIEW_BFT_B_S9_S10.md` headings and
Parts J, K, O and the binding-fix list. The only claim §1 makes is file order.

### 1.0 Scope

Background: trivial. Mass: m = 0 unless a statement says otherwise. Everything below is in lane B's
composite (BFT) setting, elliptic slice S_E (lead decision D1), d = 4, L = 3 where a number is
quoted.

### 1.1 Targets

- **T-I.1 (statement with quantifiers).** Write (CO-fun) out with every quantifier: what is bounded,
  in which norm, uniformly in which of (k, T, X_0, l, α, the source), and under which hypothesis on
  the source. Separate the statement's *asserted* class from the class its consumer supplies.
  *Planned outcome: a statement, labelled as a statement.*
- **T-I.2 (exponent, as a separate symbol).** Name the exponent (CO-fun) needs **θ_c**, never
  inheriting the symbol θ_w, and determine the full admissible range of θ_c and of the Hölder
  exponent α for which the estimate can be run. Decide whether (CO-fun) imposes any *upper* bound on
  θ_c of its own, or only α < θ_c. *Planned: PROVEN-HERE or REFUTED, with the step that binds.*
- **T-I.3 (handle 1, re-derived).** Re-derive the block-interior support statement for the funnel
  transpose h_l^T from the definition of h_l, not by citation: the kernel coefficients, the support,
  and the ℓ^∞ → ℓ^∞ and ℓ¹ → ℓ¹ operator norms. *Planned: PROVEN-HERE or a correction.*
- **T-I.4 (handle 2, re-derived, and the L^{k−l} question).** Re-derive the size estimate for the
  funnel source at level l, and decide whether a power of L^{k−l} is genuinely absent or is hidden
  in a constant, in the units conversion, or in the summation that consumes it. State which units
  each inequality is in at every step. *Planned: PROVEN-HERE, or the hidden power exhibited.*
- **T-I.5 (consumer audit).** Determine which source class BFT-5 clause (b) actually feeds to
  (CO-fun): (i) the solvability class Ξ^T S = 0 (composite-co-closed), (ii) the strictly co-closed
  sub-class, or (iii) something narrower. Decide whether the gap between (i) and (ii) is non-empty
  **and reached by a named consumer in this lane**, by exhibiting the consumer or showing there is
  none. *Planned: PROVEN-HERE as a reading of cited constructions, each cited by file and section.*
- **T-I.6 (the residue).** For the part of the class in the gap of T-I.5, decide whether the term
  that (CO-fun) does not cover admits a k- and T-uniform bound once a norm of the level-k root
  charges is added to the source class as its own slot; if it does, give the reduction with its
  constant, and name what is then left. *Planned: PROVEN, CONDITIONAL on a named item, or REFUTED.*
- **T-I.7 (the verdict asked for).** State plainly whether BFT-5 clause (b)'s curvature half is
  unconditional for the composite-co-closed class, and if not, name every condition that remains and
  which of them is upstream of which. *Planned: a status, with no distance-to-finish commentary.*

### 1.2 Failure modes (labelled before any derivation; no pre-registration weight beyond the labels)

- **I-F1.** The target is **stale**: (CO-fun) has already been decided (proved, refuted, or both,
  under different hypotheses) in a lane file later than the one my scope cites, so the work asked for
  is a re-derivation and the real remaining item has a different name. *If this occurs it is to be
  reported as the headline, not buried.*
- **I-F2.** The two handles are correct but **not load-bearing**: the estimate that (CO-fun) needs is
  obstructed somewhere neither handle touches, so "two proven handles" is not evidence of good odds.
- **I-F3.** The absence of L^{k−l} in handle 2 is **real per level but immaterial**, because the
  level sum that consumes it is not geometric for the sources the consumer supplies, and a factor
  growing in k enters there instead.
- **I-F4.** The gap class of T-I.5 is **non-empty and reached**, so a theorem proved under strict
  co-closedness does not discharge clause (b) as clause (b) is stated.
- **I-F5.** The residue of T-I.6 is bounded by two factors each of which is separately uncontrolled,
  so adding a root-charge slot moves the obstruction without reducing it.
- **I-F6.** d = 4 binds: some step needs d < 4, or needs a summability that holds only for d < 4.

### 1.3 Checks (criteria file to be written after this section and before any script)

- **cf1** — exact rational arithmetic (`fractions.Fraction` and Python ints only; no numpy, no BLAS;
  single thread; brief rule 6 exempts exact arithmetic from the numeric lock). Targets: the funnel
  kernel coefficients and support of T-I.3, and the per-level convolution inequality of T-I.4, on an
  explicitly constructed small block decomposition. Every gate carries a **designed-FAIL control**
  whose firing is to be reported (defect 3).
- No floating-point numerics are planned. If any is run, it is labelled post-hoc.

### 1.4 What I will not do

- I will not edit any file but this one and `checks/cf1_*`.
- I will not re-judge a lane-A item; where one is used I quote its status with the file and line and
  say it is quoted.
- I will not run a git command.

---
