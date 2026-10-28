# QFIX.md — fixing the Moser exponent q on the merits

Target **T55-N**, session 25. Owner of this file: the T55-N worker. Writes confined to this file and
`checks/qf1_*`. No git, ever.

---

## 1. PRE-STATED (first edit of this file, 2026-10-28 21:37:59 UTC)

**This is the first edit of this file. It contains STATEMENTS ONLY. It cites nothing produced in
session 25** — every reference below is to a file whose content predates this session (`SQ.md`,
`REVIEW_SQ_S4.md`, `CONST_T.md`, `STAR_CONST.md`, `EPSSTAR.md`, `TAUFLAT.md`, `RLARGE.md`,
`REVIEW_SF_S7.md`, `HANDOFF.md`, `PROOF.md`). Where my commissioning brief quotes a session-25 finding
I restate the *question* only and re-derive the *answer* from pre-session sources.

### 1.1 The object

`q` is the integrability exponent of the ε-regularity / Moser iteration **EPS-T** in `SQ.md` §15
(l.1467-1504, threshold clause l.1608-1613, fixed at `q := 8` at l.1621). It enters the Moser absorption
exponent **a = q/(q−4)** (`CONST_T.md` l.158, l.181) and hence the energy-inequality constant
**C_T = √6·F·B(4a)·[ ½(A_sγ_s)^a + ½(A_cγ_c)² + 288·C_1·Q ]** (`CONST_T.md` l.181; `EPSSTAR.md` l.21).
`CONST_T.md` l.272 lists q as **CHOICE, free, q > 4**, and l.286 calls it "the lever".

### 1.2 What I will do — targets, as statements

- **(Q1) Census.** Enumerate every consumer of q in this lane by file:line, give each one's monotone
  direction in q (wants q larger / smaller / indifferent), and give each one's q-elasticity as a number
  or as a parametric form. I expect the census to include at least: a = q/(q−4); the β-telescope factor
  B(4a) and the P-max/P-ct convention dispute (`STAR_CONST.md` l.386, l.568); the downstream conversion
  C_T′ = 2^{2+4/q}·4C_T and 32^{1/q}C_0 (`CONST_T.md` l.313-317); the EPS-0b-avg threshold θ_G ∝ 1/q
  (`CONST_T.md` l.309-312, from `REVIEW_SQ_S4` S4-14); the (CLS-min) → RLARGE interface ceiling
  C_T ≲ 10¹³ (`REVIEW_SQ_S4` S4-16); RLARGE's a_bad branch via C_D ≤ 6.7·10¹⁵ (`EPSSTAR.md` l.602);
  HIST A5's size clause via DESC-ε, which `EPSSTAR.md` l.605-608 says needs C_T ≲ 3.5·10¹⁰; and the
  ε_1 ceiling of `TAUFLAT.md` §4/§6.
- **(Q2) Admissible range, re-derived.** Derive from the mathematics the constraint set on q. I will
  separate (i) constraints that are *theorems about the step* (q > d = 4; σ = q/2 > 2; ϑ = 2/σ ≤ ½;
  exact scale-invariance) from (ii) constraints that are *consumer ceilings* (C_T ≤ 10¹³ and the like).
  I state in advance that these are different kinds of object and that a "q_min" of the second kind is
  **not** an admissibility constraint — it is one consumer's inequality, and it may be the optimand
  rather than the domain.
- **(Q3) Provenance of the current value.** Establish, by file:line, where q = 8 was fixed and for what
  question, and where q = 12 was fixed and for what question, and state whether each reason is still
  live.
- **(Q4) Objective.** Write the lane's total objective as a function of q: for each consumer, the
  decades of margin it holds at that q, and the minimum over consumers. The currency is margin against
  the binding smallness ceiling **DX′ = 2.456·10⁻¹⁵²/C_Ω** (`REVIEW_SF_S7.md` l.203), every figure
  linear in C_Ω. Report the whole curve over the admissible range, not only the argmax.
- **(Q5) Interior or endpoint.** Say whether the optimum is interior or at an endpoint; if at an
  endpoint, name the constraint that caps q, and say whether that constraint is a theorem or a
  convention.
- **(Q6) Deliverable.** Give (a) the recommended q as a number; (b) the parametric form of every
  downstream quantity in q, to be carried beside its number in the convention `TAUFLAT.md` l.566-567
  sets for η_♭; (c) the resulting ε_1^cut target, both parametrically and at the recommended q.
- **(Q7) Append-ready patch text** for files I do not own, in a `## FOR OTHER FILES (not edited)`
  section.

### 1.3 Things I state in advance that I will NOT do

- I will **not** re-open the value of ε_1. It is settled at ε_1 ≤ 6.7·10⁻⁴⁰ (`RLARGE.md` l.72) and is
  another target's scope. My output is q and what q does to the ε_1 *target*.
- I will **not** re-derive (★), C_1, C_V, c_s, c_g, F, B(m), C_err, C_3, θ_0, τ_R or the Green's-function
  constants. I read them. Any number of mine inherits their status.
- I will **not** edit any file but this one and `checks/qf1_*`.
- I will **not** treat any "room", "margin" or "slack" figure I read as q-independent without checking
  what it was evaluated at. `HANDOFF.md`'s closing paragraph names this as the lane's standing defect.

### 1.4 PRE-REGISTERED verdicts (criteria before scripts; no constant derived in this session)

Any numeric check I run gets `checks/qf1_criteria.md` written **before** the script, and a designed-FAIL
control. Pre-registered now:

| id | claim under test | PASS | FAIL |
|---|---|---|---|
| **QF1-1** | harness reproduction | my C_T(q) harness reproduces `EPSSTAR.md` l.547-553's q-row (q = 10,11,12,16,24,32,100 at m = 19615 and m = 7) to 3 significant figures, and `CONST_T.md` l.294-305's B(4a) column to 2 s.f. | any row off by > 1 % at m = 19615 |
| **QF1-2** | monotonicity | C_T(q) is strictly decreasing on q ∈ (4, ∞) under P-max, and the limit as q → ∞ is finite and positive | non-monotone, or divergent |
| **QF1-3** | the q ≥ 11 claim is a *consumer ceiling*, not an admissibility constraint | every clause of the step (q > 4, σ > 2, ϑ ≤ ½, c_ϑ ≤ 1, the scale-invariance identity) is satisfiable as an exact rational at q = 5, 6, 8, 10 — i.e. nothing in the mathematics excludes q < 11 | some clause fails as an exact rational at some q > 4 |
| **QF1-4** | the downstream prefactor is q-dependent and was frozen | the ratio Λ(q)/Λ(8) with Λ(q) := 4·2^{2+4/q}·(2.47N√κ_+ + 32^{1/q}C_0) differs from 1 by more than 5 % at q = 12, so C_D ≈ (0.5-0.9)·10³·C_T carries a q = 8 evaluation inside it | the ratio is within 5 % of 1 over q ∈ [8, ∞) |
| **QF1-5** | the objective has a finite plateau | the total objective, as the min over consumers of decades of margin, is non-decreasing in q up to the first consumer that opposes, and the position of its maximum is reported with the cost of the two neighbouring q | the objective is unbounded in q, which would mean a consumer has been missed |
| **QF1-6** | designed-FAIL control | a control row in which C_T is replaced by a q-independent constant returns "NO-LEVER" (objective flat in q, spread exactly 0 decades), while the real row does not | the control also moves, i.e. the harness moves for a reason other than q |
| **QF1-7** | exactness | every arithmetic result is computed in `fractions.Fraction` / `decimal.Decimal` and is identical at 40 and 60 digits | disagreement between precisions |

### 1.5 Pre-registered structural expectations, so that agreement is evidence

Stated now, before computing, so that confirmation counts and refutation is reportable:

- **(X1)** I expect to find **no consumer that genuinely wants q small** other than θ_G ∝ 1/q, and I
  expect θ_G's headroom to be ≥ 20 decades, i.e. non-binding. If so, the brief's framing that "some
  consumers will want q small while others want it large — that opposition is the actual content" is
  **wrong**, and the honest finding is that q has a one-sided optimum at a plateau.
- **(X2)** I expect the binding cap on q to be **not a constraint at all** but the *saturation* of
  C_T(q) at its plateau: the source term ½(A_sγ_s)^a → ½A_sγ_s as a → 1, so C_T cannot fall below
  √6·F·B·[½A_sγ_s + ½(A_cγ_c)² + 288C_1Q].
- **(X3)** I expect the **P-max vs P-ct β-power convention** (`STAR_CONST.md` l.386, l.568) to be worth
  more at large q than the q-raise itself is beyond q ≈ 30, and therefore to be the thing worth
  attacking once q is at the plateau.
- **(X4)** I expect **HIST A5's size clause via DESC-ε** (needs C_T ≲ 3.5·10¹⁰) to remain dead at the
  P-max plateau and to become *live or nearly live* under P-ct at large q. If so that is a status
  change in someone else's file and goes in `FOR OTHER FILES`.
- **(X5)** I expect the recommended q to be a **plateau value around 30-100**, not an exact optimum,
  and I expect the correct deliverable to be a parametric statement plus a recommended evaluation
  point, not a bare integer.

Three of these five being wrong would be the normal rate for this lane.

---
