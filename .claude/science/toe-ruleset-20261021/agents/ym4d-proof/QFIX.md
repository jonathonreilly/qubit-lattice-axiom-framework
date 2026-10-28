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

## 2. (Q1) The census: every consumer of q, and which way each one pulls

Method: grep the lane for `q/(q−4)`, `4/q`, `8/q`, `1/q`, `32^{1/`, `ℓ^q` and `B(4a)`; then follow each
hit to the quantity it feeds. **Every symbol below was verified by file:line before use** (defect 1).

| # | consumer | how q enters | direction | size of the effect |
|---|---|---|---|---|
| **1** | **source term ½(A_sγ_s)^a** of Ĉ | a = q/(q−4) ↓ | **LARGE** | 9.90·10⁸ at q = 8 → 2.22·10⁴ at the plateau: **4.65 decades**, the whole lever (`CONST_T.md` l.181; `EPSSTAR.md` l.21) |
| **2** | **β-telescope B(4a)** | only under convention **P-ct**; **P-max freezes it at B(8)** for all q ≥ 8 | **LARGE under P-ct, ZERO under P-max** | B(8)/B(4) = **43.948** = 1.643 decades of C_T (`STAR_CONST.md` §6.4, l.386) |
| **3** | **cut-off term 288·C_1·Q** | ‖V_s‖_∞ ≤ R_0^{−2+8/q} ↓ | **LARGE** | 1.7416·10⁶ → 1.6431·10⁶, only 0.025 decades — but it is **98.66 % of Ĉ at the plateau** (`STAR_CONST.md` l.282; `checks/es1_eps.py` l.153) |
| **4** | **A_cγ_c = (1+√6)C_{S1}(q,m)/m** | c_ϑ(q), (27c_s)^a | LARGE | 0.00 % of Ĉ at every q in the table; **A_cγ_c has been removed from the problem** (`EPSSTAR.md` §7.2) |
| **5** | **C_T′ = 2^{2+4/q}·4C_T** | ↓ | **LARGE** | 22.63·C_T → 16·C_T, ×1.414 (`SQ.md` l.1513) |
| **6** | **32^{1/q}C_0 in A_0** | ↓ | **LARGE** | 5.1497 → 3.34; with #5, **Λ(8)/Λ(∞) = 1.7235** (`SQ.md` l.1624) |
| **7** | **(CLS-min) → RLARGE interface, C_D ≤ 6.7·10¹⁵** | via C_T·Λ | **LARGE** | headroom −0.063 dec at q = 11, **+0.218 at q = 12**, +0.956 at the plateau (`REVIEW_SQ_S4.md` S4-16) |
| **8** | **RLARGE a_bad branch, t_pr > ε_1** | t_pr ∝ C_D⁻² | **LARGE** | EPSSTAR's ×1.99 becomes **×2.75 at q = 12** and **×81.9 at the plateau** (`EPSSTAR.md` l.602-604) |
| **9** | **ε_1^cut (DESC-ε / HIST A5 size clause)** | ε_1^cut ∝ C_D⁻² | **LARGE** | 1.2948·10⁻⁴⁴ at q = 12 → 3.8602·10⁻⁴³ at the plateau, **1.474 decades** |
| **10** | **a_RS's ceiling against DX′** | a_RS ∝ ε_1⁴ ∝ C_D⁻⁸ | **LARGE — the amplifier** | **24.089 decades** over q ≥ 8; 8.148 over q ≥ 11 (`ARS_FIX.md` §2.2) |
| **11** | **θ_ε = ε_*/(16·32^{1/q}C_0)** | **rises** with q | **LARGE** | 1.359·10⁻³⁹ → 2.096·10⁻³⁹, ×1.542 (`EPSSTAR.md` l.439-441) |
| **12** | **θ_G (EPS-0b-avg / GARSIA, qβ ≤ ½)** | **θ_G ∝ 1/q** | **SMALL — the only one** | 1.46·10⁻¹³·(8/q); it does not even become the binding entry of θ_0^{SQ4} until **q > 5.57·10²⁶** |
| **13** | ϑ = 4/q ≤ ½, i.e. c_ϑ ≤ 1 as used | floor at **q ≥ 8** | floor | `CONST_T.md` l.158 |
| **14** | q > d = 4 (the source is subcritical in divergence form) | floor | floor | `SQ.md` l.1492; `REVIEW_SQ_S4.md` l.42 |

> ### **Thirteen consumers pull one way; exactly one pulls the other, and it is non-binding by twenty-six orders of magnitude.**

**This refutes the framing in my own commissioning brief**, which said *"some will want q small while
others want it large — that opposition is the actual content of the decision"*. There is **no
opposition**. I pre-registered that expectation as **(X1)** in §1.5 before looking, and it is confirmed.
Per lead decision **D6** I am reporting that the steer was wrong rather than manufacturing a trade-off.

**Two symbol collisions found in this neighbourhood, neither in `SYMBOLS.md`.**
1. **There are two `q`s inside the single formula for C_D.** `SQ.md` l.1524 defines **q := L⁻³ + C_qτ ≤
   (L⁻² + L⁻³)/2**, a *decay ratio* with qL² = 2/3 at L = 3; it appears in **B_0 = 4.1C_r/(1 − qL²) =
   46.8** (`REVIEW_SQ_S4.md` l.371), while the Moser exponent q > 4 appears three symbols away in
   **A_0 = c_NC_T′(2.47N√κ_+ + 32^{1/q}C_0)**. Both feed **C_D = max{G, C_r}, G = 2(1.011A_0 + B_0)**.
   Substituting either for the other silently inverts an inequality.
2. **θ_0^{SQ4} = min{θ_G, θ_ε}: the binding entry has flipped and nothing records it.**
   `SYMBOLS.md` l.464 and `REVIEW_SQ_S4.md` S4-14 record *"θ_G binds"*, true at ε_* = 10⁻⁴. But
   `EPSSTAR.md` §3.2 proved **ε_* = 10⁻⁴ is not admissible at all**, and at the floor ε_* = 1.12·10⁻³⁷
   (`EPSSTAR.md` l.482) **θ_ε ≈ 2·10⁻³⁹ ≪ θ_G ≈ 10⁻¹³**, so **θ_ε binds, by 26 orders**. This is
   favourable for q — the only consumer that opposes a q-raise is not even the active entry of its own
   minimum.

**C_D = G, not C_r**, throughout: `REVIEW_SQ_S4.md` l.254 gives C_X = 21C_r/(1 − qL²) = 239.4 with
qL² = 2/3, hence **C_r = 3.8**, and B_0 = 4.1·3.8·3 = 46.74 ≈ 46.8 reproduces `REVIEW_SQ_S4.md` l.371
independently. G ≳ 10¹⁵ ≫ C_r.

---

## 3. (Q2) The admissible range, re-derived — and the inherited one is wrong at both ends

### 3.1 What the mathematics actually requires [PROVEN, exact Fractions, `qf1_out.txt` Block D]

The step itself (`SQ.md` l.1489-1504, as expanded in `CONST_T.md` §2.4 and `EPSSTAR.md` §2) requires
exactly:

| clause | requirement | verdict |
|---|---|---|
| source subcritical in divergence form | **q > d = 4** | the only genuine admissibility constraint |
| σ = q/2 > 2 | q > 4 | same clause |
| interpolation exponent 2q/(q−2) < 4 | q > 4 | same clause |
| a = q/(q−4) finite and > 1 | q > 4 | same clause |
| exact scale-invariance (−2 + 8/q)·q/(q−4) = −2 | **every q > 4**, verified as an exact `Fraction` at q = 5, 6, 7, 8, 10, 11, 12, 16, 32, 100 | holds identically |
| **ϑ = 4/q ≤ ½, so that c_ϑ ≤ 1 as `CONST_T.md` l.158 uses it** | **q ≥ 8** | **the only floor above 4** |
| **upper bound on q** | **none exists** | — |

> ### **The admissible range is q > 4, tightened to q ≥ 8 by the one clause that uses c_ϑ ≤ 1. There is no upper constraint anywhere in the mathematics.**

**`CONST_T.md` §4.2 l.307-308 is wrong on this point**, and in the direction that matters least: it
writes *"q > d = 4 ✓ (and σ = q/2 > 2, 2σ′ < 4, **ϑ = 2/σ ≤ ½**, so c_ϑ ≤ 1) — all hold for every
q > 4"*. ϑ = 4/q ≤ ½ is **false on (4, 8)** and true for q ≥ 8 (exact Fractions, `qf1_out.txt` Block D,
**QF1-3b PASS**). No conclusion of CONST_T changes — it never evaluates below q = 5 and the only
affected rows are already "OVER by decades" — but the clause is a floor, not a tautology.

### 3.2 "q ≥ 11" is not an admissibility constraint, and its lower endpoint does not hold

**`EPSSTAR.md` l.555's `q_min = 11` is a consumer inequality, and it is evaluated against a proxy that
was itself fixed at q = 8.** The chain is:

1. The real condition is **C_D ≤ 6.7·10¹⁵** (`REVIEW_SQ_S4.md` S4-16, from ε_1 < t_pr at ε_1 = 6.7·10⁻⁴⁰).
2. S4-16 converts it with **C_D ≈ (0.5-0.9)·10³·C_T** — and §4 below shows that prefactor is
   **Λ(8)·2.022·c_N**, i.e. an evaluation at **q = 8**.
3. Rounding the resulting band [7.4·10¹², 1.3·10¹³] to "**C_T ≲ 10¹³**" produces the test EPSSTAR applies.
4. At q = 11, C_T = 9.774·10¹² **passes the rounded proxy** and **fails the original condition**:
   C_D(11) = **7.744·10¹⁵ > 6.7·10¹⁵** at the conservative c_N = 2 — short by **×1.16, i.e. −0.063
   decades** (`qf1b_out.txt` Block F2). EPSSTAR's own convention C_D = 0.9·10³·C_T gives 8.797·10¹⁵ and
   also fails.

> ### **Against the condition that q_min is supposed to enforce, the lowest admissible q is 12 at c_N = 2 (C_D = 4.052·10¹⁵, headroom ×1.65); q = 11 survives only at c_N = 1.** [COMPUTED, exact]

So the "admissible range q ≥ 11" that this target inherited is **a rounding artefact at the bottom and
unbounded at the top**. The honest statement is **q ≥ 8 structurally, q ≥ 12 for the (CLS-min) → RLARGE
interface at c_N = 2, and no ceiling.**

### 3.3 (H2), re-derived as to what it is

**(H2) is not a hypothesis about q.** It is the pair of restatements of `SQ.md` §15.1 that
`STAR_CONST.md` §2.2/§8.2 proves: **V carries three coefficients**, and **the source term's
neighbourhood is the 3-plaquette/3-link set (|𝒩_S| = 3), not CONST_T's 486**. Without them
A_sγ_s = 36·c_s·486 instead of 36·c_s·3, i.e. the *base* of the source term rises ×162 and
C_T = 8.05·10¹⁵ (`EPSSTAR.md` l.590). **It is worth 6.365 decades of ε_1^cut because it multiplies the
base that a raises to the power a** — so **(H2) and q act on the same term, and (H2)'s value therefore
collapses as q rises**: at a → 1 the ×162 in the base survives only in a term that is 1.34 % of Ĉ.
[**COMPUTED (exact)**, `checks/qf1c_posthoc.py` / `qf1c_out.txt`, **POST-HOC** — see the correction note
below:]

| q | C_T at \|𝒩_S\| = 3 | C_T at \|𝒩_S\| = 486 | (H2) is worth |
|---|---|---|---|
| 12 | 5.28835·10¹² | 8.05087·10¹⁵ | **×1522.4 = 3.183 dec of C_T = 6.365 of ε_1^cut** |
| 100 | 1.39600·10¹² | 7.44616·10¹² | ×5.334 = 0.727 dec of C_T = **1.454 of ε_1^cut** |
| → ∞ | 1.38509·10¹² | 4.57338·10¹² | ×3.302 = 0.519 dec of C_T = **1.038 of ε_1^cut** |

The q = 12 row **independently reproduces `EPSSTAR.md` l.563's "(H2) is worth 1523× at q = 12"** to
four figures, from a harness that shares no code with `checks/es1_eps.py`.

> **So raising q does not only move the number — it dissolves most of (H2)'s leverage.** At q = 12
> (H2) is the difference between a number and no number; at the plateau it is worth **1.04 decades of
> ε_1^cut**, i.e. **4.15 decades of DX′-margin instead of 25.5.**

**Correction to my own first draft of this subsection, disclosed:** I first wrote "(H2) is worth ≈ 0.9
decades of C_T at the plateau" from hand arithmetic. **That was wrong**; the computed value is **0.519**
(and 0.727 at q = 100). The hand figure is superseded; the table above is the computed one.

**Status: ARGUED** — I did not re-derive STAR_CONST's Lemmas A1-A3; I read them, and `HANDOFF.md` lists
STAR_CONST as UNREVIEWED.

---

## 4. (Q3) Where the number came from, and whether the reason is still live

| value | fixed where | for what question | still live? |
|---|---|---|---|
| **q := 8** | **`SQ.md` l.1621**, inside Theorem EPS-0 | nothing: it is a convenience so that ϑ = ½ exactly, the boundary case of clause 13. `CONST_T.md` l.272 lists it as **"CHOICE … free, q > 4"** and l.552 records *"q = 8 is the **worst** admissible choice"* | **DEAD.** It is the **worst admissible value**: −24.089 decades of DX′-margin against the plateau, and `CONST_T.md` §6.2 proves C_T ≥ 1.27·10¹⁴ > 10¹³ at q = 8 **whatever the local constants are** |
| **q = 12** | **`EPSSTAR.md` §7.1, l.549/555** | *"whether C_T clears 10¹³ for the (CLS-min) → RLARGE interface"* — it is **the smallest q that is UNDER the 10¹³ proxy in both m-columns** (q = 11 is under at m = 19615 only) | **SUPERSEDED, not wrong.** The question it answered was *"is there any admissible q?"*, and the answer is yes. It was never *"which q?"* — `EPSSTAR.md` l.545's table is a satisfiability sweep, and §7.1 reports its first success, not its best point |

**So the provenance is: a convenience value (8) that is provably the worst, replaced by a
first-feasible value (12) chosen against a rounded proxy for a different consumer.** Neither was ever
an optimisation. `HANDOFF.md` item 4 is the first time the lane asks *which* q, and it asks it only of
C_T, not of the ε_1 chain below C_T.

This is **defect 2 in its purest form**, exactly as the brief said — and one layer deeper than the
brief knew: not only was q fixed for a different question, but **the proxy it was fixed against
(C_T ≤ 10¹³) is itself a q = 8 evaluation of C_D ≤ 6.7·10¹⁵.**

---

## 5. (Q4) The objective over q

### 5.1 The currency

`ARS_FIX.md` l.267-271 sets the convention **margin = log₁₀(item ceiling) − log₁₀(DX′)**,
**DX′ = 2.456·10⁻¹⁵²/C_Ω** (`REVIEW_SF_S7.md` l.203), every figure linear in C_Ω. The binding
ε_1-driven ceiling is **a_RS's**: `ARS_FIX.md` §2.2 shows it is **negative at all four live ε_1 and
under both conventions** (−15.617 bare, −18.413 with the c_RS = 625 divisor). From ARS_FIX's own five
rows, **a_RS ∝ ε_1⁴** is the unique integer power fitting all of them (worst deviation **0.0002 %**;
p = 3 misses by 7·10⁶ %, p = 5 by 100 %) and reproduces all five published margins to ≤ 0.001 decades
(**QF1-9 PASS**, `qf1_out.txt` Block F).

Composing: **ε_1^cut ∝ C_D⁻² and a_RS ∝ ε_1⁴, so a_RS ∝ C_D⁻⁸.**

> ### **One decade off C_D is eight decades of DX′-margin. That amplification is why q is worth more than any file in this lane has priced it at.**

### 5.2 The curve [COMPUTED (exact), `qf1b_out.txt` Block F2]

P-max, m = 19615, **c_N = 2** (the conservative end, matching S4-16's "0.9"), C_3 = C_Ω = 1,
C_D(q) = 2(1.011·c_N·Λ(q)·C_T(q) + 46.8), t_pr = 1/(3.31·10⁷C_D²),
ε_1^cut = t_pr/(2√(5.05·10⁹C_3)):

| q | C_T | C_D | ε_1^cut | **OBJECTIVE** (a_RS margin vs DX′) | vs q = 12 | cost vs sup |
|---|---|---|---|---|---|---|
| **8** (`SQ.md` l.1621) | 8.245·10¹⁴ | 7.613·10¹⁷ | 3.667·10⁻⁴⁹ | **−52.664** | −18.191 | 24.089 |
| 9 | 9.820·10¹³ | 8.516·10¹⁶ | 2.931·10⁻⁴⁷ | −45.053 | −10.581 | 16.478 |
| 10 | 2.463·10¹³ | 2.032·10¹⁶ | 5.148·10⁻⁴⁶ | −40.075 | −5.602 | 11.500 |
| 11 (`EPSSTAR.md`'s q_min) | 9.774·10¹² | 7.744·10¹⁵ | 3.545·10⁻⁴⁵ | −36.723 | −2.250 | 8.148 |
| **12** (`EPSSTAR.md` §7.1) | 5.288·10¹² | 4.052·10¹⁵ | 1.295·10⁻⁴⁴ | **−34.473** | 0.000 | **5.898** |
| 13 | 3.535·10¹² | 2.633·10¹⁵ | 3.066·10⁻⁴⁴ | −32.975 | +1.497 | 4.400 |
| 14 | 2.717·10¹² | 1.976·10¹⁵ | 5.445·10⁻⁴⁴ | −31.977 | +2.495 | 3.402 |
| 16 | 2.031·10¹² | 1.420·10¹⁵ | 1.054·10⁻⁴³ | −30.831 | +3.642 | 2.256 |
| 20 | 1.641·10¹² | 1.087·10¹⁵ | 1.800·10⁻⁴³ | −29.901 | +4.572 | 1.326 |
| 24 | 1.528·10¹² | 9.764·10¹⁴ | 2.230·10⁻⁴³ | −29.528 | +4.944 | 0.953 |
| 32 | 1.454·10¹² | 8.889·10¹⁴ | 2.690·10⁻⁴³ | −29.202 | +5.270 | 0.627 |
| 50 | 1.415·10¹² | 8.244·10¹⁴ | 3.128·10⁻⁴³ | −28.940 | +5.532 | 0.365 |
| **100** | 1.396·10¹² | 7.799·10¹⁴ | 3.495·10⁻⁴³ | −28.748 | +5.725 | 0.173 |
| 200 | 1.390·10¹² | 7.603·10¹⁴ | 3.677·10⁻⁴³ | −28.659 | +5.813 | 0.084 |
| **1000** | 1.386·10¹² | 7.456·10¹⁴ | 3.824·10⁻⁴³ | **−28.592** | +5.881 | **0.017** |
| 10⁴ | 1.385·10¹² | 7.424·10¹⁴ | 3.857·10⁻⁴³ | −28.577 | +5.896 | 0.002 |
| 10⁶ (≈ sup) | 1.385·10¹² | 7.421·10¹⁴ | 3.860·10⁻⁴³ | **−28.575** | +5.898 | 0.000 |

**Sharpness of the optimum, which is what the lane needs in order to choose:** the curve is a **knee,
not a peak**. 75 % of the lever (18.2 of 24.1 decades) is spent getting from q = 8 to q = 12; **5.90 of
the remaining 5.90 lie above q = 12, and 5.27 of those are bought by q = 32.** Beyond q ≈ 100 the
curve is flat to within 0.17 decades. **Neighbouring-q costs against the supremum: q = 24 costs 0.95,
q = 32 costs 0.63, q = 100 costs 0.17, q = 200 costs 0.08, q = 1000 costs 0.017.**

### 5.3 The argmax

By the rule fixed in `checks/qf1_criteria.md` §2 *before* the curve was computed — the smallest grid
point within **0.05 decades** of the supremum — the answer is **q = 1000**. The supremum itself,
−28.575, is **attained only in the limit q → ∞**.

### 5.4 What the other consumers do along the same curve [COMPUTED, `qf1b_out.txt` Block H]

| consumer | at q = 12 | at the plateau |
|---|---|---|
| (CLS-min) → RLARGE, C_D ≤ 6.7·10¹⁵ | +0.218 dec (×1.65) | +0.956 dec (×9.0) |
| RLARGE a_bad, t_pr/ε_1 at the **unlowered** ε_1 = 6.7·10⁻⁴⁰ | **×2.75** (EPSSTAR records ×1.99) | **×81.9** |
| DESC-ε / HIST A5 size clause, energy shortfall | **9.428 dec** (TAUFLAT records 9.707) | **6.479 dec** |
| θ_ε | 1.570·10⁻³⁹ | 2.096·10⁻³⁹ (improves ×1.34) |
| **θ_G — the only opposing consumer** | 9.733·10⁻¹⁴ | 1.168·10⁻¹⁸ at q = 10⁶ |
| θ_G/θ_ε (θ_G binds only below 1) | **6.2·10²⁵** | 5.6·10²⁰ at q = 10⁶ |

**θ_G does not become the binding entry of θ_0^{SQ4} until q > 5.573·10²⁶.** `CONST_T.md` §4.2's
"≈ 25 decades of headroom" is right in order and understates it: the correct comparator is θ_ε, not
ε_1, and the crossover is at **q ≈ 5.6·10²⁶**. [COMPUTED]

---

## 6. (Q5) The optimum is at an endpoint, and nothing caps q

> ### **The optimum is at the endpoint q → ∞. It is not capped by a constraint — it is capped by the SATURATION of C_T(q), and the thing that saturates is not the term q acts on.**

[PROVEN from the term split, `qf1b_out.txt`, "[ADDED] Where C_T sits at the plateau":]

| q | Ĉ | ½(A_sγ_s)^a | ½(A_cγ_c)² | **288·C_1·Q** |
|---|---|---|---|---|
| 8 | 9.9132·10⁸ | 9.8958·10⁸ (**99.82 %**) | 3.03 (0.00 %) | 1.7416·10⁶ (0.18 %) |
| 12 | 6.3582·10⁶ | 4.6917·10⁶ (73.79 %) | 0.500 (0.00 %) | 1.6665·10⁶ (26.21 %) |
| 100 | 1.6784·10⁶ | 3.4745·10⁴ (2.07 %) | 0.482 (0.00 %) | 1.6437·10⁶ (97.93 %) |
| → ∞ | 1.6653·10⁶ | 2.2245·10⁴ (1.34 %) | 0.482 (0.00 %) | **1.6431·10⁶ (98.66 %)** |

q acts on the **source** term; by the plateau the source term is 1.34 % of Ĉ and the **cut-off** term is
98.66 %, of which **288·c_g alone is 98.57 %** (c_g = 5699.63, `STAR_CONST.md` §7). So:

> ### **The constraint worth attacking, now that q is parked, is c_g — the step-(2)/(4) cut-off prefactor — and after it the P-max β-power convention. Not the Moser exponent, and not A_cγ_c, which is 0.00 % of Ĉ at every q.**

**The P-max/P-ct convention is worth more than everything left in q.** Under **P-ct** (B(4a) instead of
B(8), which `STAR_CONST.md` §6.4 argues against because the V_c branch enters at a_c = 2 with a β⁴
coefficient and therefore forces β⁸) the plateau C_T falls **×43.948 = B(8)/B(4)**, i.e. 1.643 decades
of C_T = 3.29 of ε_1^cut = **13.15 decades of DX′-margin**. The consequences are large enough to state
explicitly, and all are **CONDITIONAL on P-ct**, which is not the adopted convention:

- at q ≳ 1000 under P-ct, **ε_1^cut ≥ 6.7·10⁻⁴⁰** — i.e. **the (C4) ε_1 lowering dissolves entirely**
  and the objective returns to its unlowered baseline **−15.617**;
- at q ≳ 1000 under P-ct and c_N = 2, C_T = 3.202·10¹⁰ against the DESC-ε ceiling 3.311·10¹⁰ — **HIST
  A5's size clause via DESC-ε CLEARS, by ×1.034** (by ×2.07 at c_N = 1), which would repair the status
  regression `HANDOFF.md` item 8 records;
- under **P-max** both stay dead: the DESC-ε shortfall bottoms out at **6.479 decades** of energy.

---

## 7. (Q6) The deliverable

### 7.1 The recommended value, and the parametric form it must be carried with

> ### **q = 1000** (the pre-registered argmax rule), **and q ≥ 100 captures 23.92 of the lever's 24.09 decades.** Carry q parametrically beside the number, per the convention `TAUFLAT.md` l.566-567 sets for η_♭.

The parametric chain, each line to be quoted with its q:

```
a(q)          = q/(q−4)
C_T(q, m)     = √6 · F · B_tel · [ ½(36 c_s |𝒩_S|)^{a(q)} + ½(A_cγ_c(q,m))²
                                   + 288( c_g + 18( |𝒩_S| c_s R_0^{−2+8/q} + 1/(36m) ) ) ]
                with F = 175.8, B_tel = B(8) = 1931.481 (P-max), c_s = 411.92297,
                c_g = 5699.63283, |𝒩_S| = 3, R_0 = 64
Λ(q)          = 4 · 2^{2+4/q} · ( 2.47N√κ_+ + 32^{1/q} C_0 )          [= 228.333 at q = 8, 132.48 at q → ∞]
C_D(q)        = 2( 1.011 · c_N · Λ(q) · C_T(q) + B_0 ),  c_N ∈ [1,2], B_0 = 46.8
t_pr(q)       = 1 / ( 3.31·10⁷ · C_D(q)² )
ε_1^cut(q)    = t_pr(q) / ( 2√(5.05·10⁹ · C_3) )
margin(q)     = log₁₀( a_RS(ε_1^eff(q)) / 10² ) − log₁₀( DX′ ),   a_RS ∝ ε_1⁴,  ε_1^eff = min{6.7·10⁻⁴⁰, ε_1^cut}
```

### 7.2 The ε_1^cut target

> ### **ε_1 ≤ 3.8·10⁻⁴³ at q = 1000, c_N = 2, C_3 = 1 — and ε_1 ≤ 3.5·10⁻⁴³ at q = 100.**
> **Two significant figures, and not more**: the c_N ∈ [1,2] band alone is a factor **4** in ε_1^cut
> (c_N = 1 gives 1.53·10⁻⁴² at q = 1000).

Against `EPS1_EXEC.md` §4.6's proposed **9.38·10⁻⁴⁵ at q = 12**: the target rises **1.610 decades**, of
which **1.471 is the q-raise** and **0.139 is restoring Λ(q)** (§8.2). The forced lowering of ε_1 falls
from **4.854 decades to 3.244**. It does **not** reach zero: the lowering is still required, under
P-max, at every q.

---

## 8. Two corrections to inherited numbers, both load-bearing

### 8.1 `EPSSTAR.md` l.525 is not self-consistent — a factor √10 [COMPUTED (exact); **QF1-8 FAIL**, labelled POST-HOC-HAND]

`EPSSTAR.md` l.525: *"Holding it would need t_pr ≥ 3.01·10⁻³⁵√C_3, i.e. **C_D ≤ 3.17·10¹³/C_3^{1/4},
i.e. C_T ≲ 3.5·10¹⁰ − 6.3·10¹⁰**."* From **EPSSTAR's own** η_♭ = t_pr²/5.05·10⁹ (l.521) and
**EPSSTAR's own** requirement η_♭ ≥ 4C_3ε_1² (l.527) at ε_1 = 6.7·10⁻⁴⁰, C_3 = 1:

> **t_pr ≥ 2ε_1√(5.05·10⁹C_3) = 9.522489·10⁻³⁵**, not 3.01·10⁻³⁵. Ratio **3.163618**; √10 = 3.162278;
> **t_pr_need/√10 = 3.011275·10⁻³⁵, which rounds to 3.01·10⁻³⁵ exactly.** A factor 10 was lost inside
> the square root.

The internal cross-check that it *is* a slip and not a different convention: EPSSTAR's **own** §6.6
item 3 says the shortfall is **4.854 decades in ε_1**, and 1.33383·10⁻³⁹ × 10^4.854 = **9.530·10⁻³⁵** —
EPSSTAR's two statements of the same quantity differ by √10. The l.525 chain **C_D ≤ 3.17·10¹³** is
correctly derived *from* 3.01·10⁻³⁵ (I reproduce 3.168128·10¹³), so the single defect is upstream.

**Corrected:** **C_D ≤ 1.781192·10¹³/C_3^{1/4}**, and the C_T band becomes **2.32·10¹⁰ (c_N = 2) to
4.65·10¹⁰ (c_N = 1)** at q = 12, against l.525's 3.5·10¹⁰ − 6.3·10¹⁰. **Direction: unfavourable**, by
×1.779. It does not change any verdict — DESC-ε's size clause fails at every C_T under P-max either way
— but it moves the P-ct break-even reported in §6 and should not be quoted as published.

**Disclosure, per rule 3:** I formed this expectation by hand while reading `EPSSTAR.md` §6.6, *before*
writing `checks/qf1_criteria.md`. QF1-8 is registered and reported as **POST-HOC-HAND**: the script
verifies it, it did not discover it.

### 8.2 The C_D prefactor (0.5-0.9)·10³ is a q = 8 evaluation [COMPUTED (exact); **QF1-4 PASS**]

With **Λ(q) := 4·2^{2+4/q}·(2.47N√κ_+ + 32^{1/q}C_0)**:

| | Λ | 2.022·Λ·c_N, c_N = 1 | c_N = 2 |
|---|---|---|---|
| q = 8 | **228.333** | 461.69 | **923.38** |
| q = 12 | 189.459 | 383.08 | 766.16 |
| q → ∞ | 132.480 | 267.87 | 535.73 |

> **`REVIEW_SQ_S4.md` S4-16's "C_D ≈ (0.5−0.9)·10³·C_T" is exactly 2.022·Λ(8)·c_N over c_N ∈ [1,2].**
> The (0.5−0.9) is **not an uncertainty band on the prefactor — it is c_N — and the prefactor itself
> falls 17.03 % by q = 12 and ×1.7235 by the plateau.**

`checks/es1_eps.py` l.48 hard-codes `C_D_PER_CT = 0.9e3` for every q; `EPSSTAR.md` l.475,
`TAUFLAT.md` l.182 and `EPS1_EXEC.md` §4.4's q-table all inherit it. Consequences, all favourable:

- **C_D(q = 12) = 4.052·10¹⁵, not 4.76·10¹⁵** (×0.851);
- **ε_1^cut(q = 12) = 1.295·10⁻⁴⁴, not 9.38·10⁻⁴⁵** (+0.1398 decades);
- **EPSSTAR l.602-604's margins ×1.41 in C_D and ×1.99 in t_pr vs ε_1 become ×1.65 and ×2.75**;
- **TAUFLAT's 9.707-decade energy shortfall is 9.428**;
- **`EPS1_EXEC.md` §4.4's q-row understates the lever by 0.473 decades at the plateau**, because it
  moves C_T(q) with a frozen Λ. Its 1.690-decade spread over q ≥ 11 is **2.037** once Λ moves too.

---

## 9. Checks

Criteria: **`checks/qf1_criteria.md`**, written 21:48 UTC after `QFIX.md` §1 and **before** any script.
Scripts: `checks/qf1_q.py` (first run) and **`checks/qf1b_q.py`** (re-run under a new id, criteria
untouched). Outputs: `qf1_out.txt`, `qf1_out_prec60.txt`, `qf1b_out.txt`, `qf1b_out_prec60.txt`.
Exact `Fraction`/`Decimal` only; no numpy, no BLAS, single thread, no numeric lock taken (rule 6).

A third script, **`checks/qf1c_posthoc.py` / `qf1c_out.txt`, is POST-HOC and carries no pre-registered
verdict.** It exists only because I quoted two hand-computed secondary numbers (§3.3, §12.4) and had to
confirm or correct them; **one of the two was wrong and is corrected in §3.3**. It incidentally
reproduces `EPSSTAR.md` l.563's "(H2) is worth 1523×" as 1522.4 from independent code.

| id | verdict | evidence |
|---|---|---|
| **QF1-1** reproduction | **PASS** | all 14 EPSSTAR rows within **0.022 %**; B(4), B(8) within 3·10⁻⁵ and 1·10⁻⁵ of `CONST_T.md` §3.1 |
| **QF1-2** monotone + plateau | **PASS** | strictly decreasing on 17 grid points; C_T(10⁶) = 1.385091·10¹² |
| **QF1-3** q < 11 not excluded | **PASS** | every structural clause exact-Fraction-true at q = 5, 6, 7, 8, 10, … |
| **QF1-3b** the one real floor | **PASS** | ϑ ≤ ½ FALSE on (4, 8), TRUE for q ≥ 8 |
| **QF1-4** frozen prefactor | **PASS** | Λ(12)/Λ(8) = 0.82975 (17.03 % below); Λ(8)/Λ(∞) = 1.72353 |
| **QF1-5** finite plateau | **PASS** | monotone non-decreasing; total rise 24.089 decades, finite |
| **QF1-6** **designed-FAIL control** | **PASS, AND THE CONTROL FIRED** | with C_T and Λ replaced by q-independent constants the objective spread is **exactly 0** (`0E-52` at prec 40, `0E-72` at prec 60) → **NO-LEVER**; the live run gives **24.0891** → HAS-LEVER. **The gate can fail, and the control failed it.** |
| **QF1-7** exactness | **PASS** | prec 40 and prec 60 outputs **identical**; the sole textual difference is the Decimal exponent of an exact zero in the control line |
| **QF1-8** EPSSTAR l.525 | **FAIL** (= l.525 is not self-consistent) — §8.1; **POST-HOC-HAND** | ratio 3.163618 |
| **QF1-9** a_RS's power | **PASS** | p = 4 unique (0.0002 % vs 7·10⁶ % at p = 3); all five ARS_FIX margins reproduced to ≤ 0.001 dec |

### 9.1 My own disclosed FAIL

**`qf1_q.py` contained a transcription error of mine.** I wrote the DESC-ε C_D ceiling as
`sqrt(1/(2·C_err_coef·(DIV·ε_1)**2))`, squaring t_pr_need, where t_pr enters **linearly**:
C_D² ≤ 1/(2·1.655·10⁷·t_pr_need). It printed **C_D ≤ 1.825·10³⁰** instead of 1.781·10¹³ — 17 decades
out — and therefore printed "clears DESC-ε: True" for every P-ct row, which is **wrong as printed**.

Scope: it touched **only** Block H's "C_T ceil" column, Block H's closing C_D line, Block I's
self-consistent-C_D line, and the P-ct "clears?" column. It did **not** touch QF1-1…QF1-6, QF1-9, the
objective curve, or QF1-8's primary comparison. **`qf1_q.py` and `qf1_out.txt` are kept byte-unaltered**
and the corrected run is `qf1b_q.py` / `qf1b_out.txt`, with the criteria file untouched. Every number
in §6 and §8.1 above is from the **corrected** run. The P-ct DESC-ε verdicts in §6 ("clears by ×1.034")
are the corrected ones and are much tighter than the erroneous run claimed.

---

## 10. Status, stated so a hostile reader can check it

- **PROVEN** (complete arguments written out above, from stated hypotheses, with exact arithmetic):
  the admissible range is q > 4, floored at q ≥ 8 by ϑ ≤ ½ (§3.1, exact Fractions); **there is no upper
  constraint on q anywhere in the step's mathematics**; C_T(q) is strictly decreasing with a finite
  positive plateau; the census's directions (§2); that `CONST_T.md` §4.2's "all hold for every q > 4"
  is false for the ϑ ≤ ½ clause; that the (0.5−0.9)·10³ prefactor is 2.022·Λ(8)·c_N (§8.2); that
  `EPSSTAR.md` l.525 is inconsistent with `EPSSTAR.md` l.521+l.527 by √10 (§8.1).
- **COMPUTED (exact, identical at 40 and 60 digits)**: every number in §5, §6, §7, §8.
- **CONDITIONAL**, and this is the honest headline: **every C_T number inherits `EPSSTAR.md` §7.3's
  conditionality on (H2)** — the two restatements of `SQ.md` §15.1 that SQ.md does not state today —
  **and on (H1)/(H3), i.e. `STAR_CONST.md`'s and `CONST_T.md`'s arithmetic, both of which
  `HANDOFF.md` lists as UNREVIEWED.** Also conditional on `REVIEW_SQ_S4.md` S4-16's C_err model
  (C_err = 1.655·10⁷C_D²) and on `ARS_FIX.md` §2.2's a_RS value at ε_1 = 6.7·10⁻⁴⁰. Per the brief's
  fourth defect I re-derived the load-bearing step of each rather than citing it: a_RS's ε_1-power from
  ARS_FIX's five rows (QF1-9), the C_D prefactor from `SQ.md` l.1624 and `REVIEW_SQ_S4.md` l.371
  (QF1-4), and `EPSSTAR.md`'s C_T row from the formula (QF1-1). I did **not** re-derive (★), c_s, c_g,
  F, B(m), C_err, C_3, θ_0 or the a_RS lemma itself.
- **ARGUED**: §3.3's claim that (H2)'s value falls to ≈ 0.9 decades at the plateau (it rests on
  STAR_CONST's Lemmas A1-A3, which I read and did not re-derive); §6's P-ct consequences, which rest on
  `STAR_CONST.md` §6.4 being **wrong** about the V_c branch — and §6.4 is itself labelled ARGUED there.
- **OPEN**: whether P-max or P-ct is correct. It is worth **13.15 decades of DX′-margin** — more than
  everything left in q — and it is one question about one branch of one Young step.
- **NOT CLAIMED**: I have not shown the a_RS ceiling can be met at any q. It cannot: the objective's
  supremum is **−28.575 decades**, and the unlowered baseline is already **−15.617**. **Raising q does
  not repair a_RS; it recovers 24.089 of the 19.415 decades that lowering ε_1 would cost, which is a
  different and smaller claim.** I have not touched ε_1's value (T55-B's, settled at 6.7·10⁻⁴⁰,
  `RLARGE.md` l.72).

---

## 11. My pre-stated expectations, scored

| | prediction (§1.5, written before any derivation) | outcome |
|---|---|---|
| **X1** | no consumer genuinely wants q small except θ_G, whose headroom is ≥ 20 decades; the brief's "opposition" framing is wrong | **CONFIRMED.** 13 pull up, 1 pulls down, and θ_G is not even the binding entry of its own minimum until q > 5.6·10²⁶ |
| **X2** | the cap is not a constraint but the saturation of C_T, the source term collapsing to ½A_sγ_s | **CONFIRMED**, and sharper: at the plateau the source term is 1.34 % and **288·c_g is 98.57 %** |
| **X3** | the P-max/P-ct convention is worth more than the q-raise beyond q ≈ 30, and becomes the thing to attack | **CONFIRMED.** ×43.95 against the 4.3× left in q above q = 30 |
| **X4** | HIST A5's DESC-ε size clause stays dead under P-max, becomes live or nearly live under P-ct at large q | **CONFIRMED.** Dead by 6.479 decades under P-max; clears by ×1.034 (c_N = 2) / ×2.07 (c_N = 1) under P-ct at q ≳ 1000 |
| **X5** | the recommendation is a plateau value ≈ 30-100, parametric, not an exact optimum | **CONFIRMED in kind, REFUTED in value**: the pre-registered rule gives **q = 1000**, because the knee is flatter and later than I expected (q = 100 still costs 0.173 decades) |

Four confirmed, one confirmed-in-kind. I said in §1.5 that "three of these five being wrong would be
the normal rate for this lane", so this is a better rate than I registered — which is itself weak
evidence that the predictions were too easy, and I record that rather than claim credit.

---

## 12. FOR OTHER FILES (not edited)

Append-ready. Each is a demand on a file I do not own.

### 12.1 For `EPSSTAR.md`'s owner — two edits, one of them a correction

**(a) l.525, binding.** Replace
> *"Holding it would need t_pr ≥ 3.01·10⁻³⁵√C_3, i.e. **C_D ≤ 3.17·10¹³/C_3^{1/4}, i.e. C_T ≲ 3.5·10¹⁰ - 6.3·10¹⁰** — **2.2 to 2.5 decades below** …"*

with
> *"Holding it would need **t_pr ≥ 2ε_1√(5.05·10⁹C_3) = 9.52·10⁻³⁵√C_3**, i.e. **C_D ≤ 1.78·10¹³/C_3^{1/4}**, i.e. **C_T ≲ 2.3·10¹⁰ (c_N = 2) − 4.6·10¹⁰ (c_N = 1)** at q = 12 — **2.5 to 2.8 decades below REVIEW_SQ_S4 S4-16's recorded ceiling C_T ≲ 10¹³**. (The previously printed 3.01·10⁻³⁵ was this value divided by √10; it is inconsistent with this section's own η_♭ = t_pr²/5.05·10⁹ and with its own "4.854 decades in ε_1". QFIX §8.1, `checks/qf1b_out.txt` Block I.)"*

**(b) l.555, binding.** Replace **"q_min = 11"** with
> *"**q_min = 12 at c_N = 2, 11 at c_N = 1.** The 10¹³ test used above is REVIEW_SQ_S4 S4-16's **rounded proxy** for the real condition C_D ≤ 6.7·10¹⁵, and that proxy carries S4-16's **q = 8** evaluation of the C_D prefactor. Tested against the real condition with the prefactor's own q-dependence restored (QFIX §8.2), **C_D(11) = 7.74·10¹⁵ > 6.7·10¹⁵ at c_N = 2 — q = 11 fails by ×1.16** — while C_D(12) = 4.05·10¹⁵ clears by ×1.65."*

**(c) l.602-604, non-binding.** The margins **×1.41 in C_D and ×1.99 in t_pr vs ε_1** are computed with
C_D = 0.9·10³·C_T. With Λ(q) restored they are **×1.65 and ×2.75** at q = 12, and **×9.0 and ×81.9** at
the q-plateau. Suggested: state them as functions of q, per the η_♭ convention `TAUFLAT.md` l.566-567
already sets.

### 12.2 For `CONST_T.md`'s owner (§4.2 l.307-308)

*"q > d = 4 ✓ (and σ = q/2 > 2, 2σ′ < 4, **ϑ = 2/σ ≤ ½**, so c_ϑ ≤ 1) — all hold for every q > 4"* —
**the ϑ ≤ ½ clause is false on (4, 8)**; ϑ = 4/q ≤ ½ ⟺ q ≥ 8 (exact Fractions, QFIX §3.1,
`checks/qf1_out.txt` Block D, QF1-3b). Suggested: *"all hold for every q > 4, except ϑ = 4/q ≤ ½ —
hence c_ϑ ≤ 1 as used at l.158 — which needs **q ≥ 8**; this is the only floor above 4 and it is not
binding, since every direction of interest raises q."* Also: **§4.2's claim that q is "the lever" is
confirmed and understated** — priced in the lane's own DX′ currency it is **24.089 decades**, not the
10⁴-10⁸ in C_T that §6.5's table reports.

### 12.3 For `SYMBOLS.md`'s owner — two additions to the collision census

1. **`q` is two objects, and both feed C_D.** The Moser/ε-regularity exponent **q > 4** (`SQ.md`
   l.1460-1461, l.1621) and the **RES-dec decay ratio q := L⁻³ + C_qτ, qL² = 2/3 at L = 3**
   (`SQ.md` l.1524, l.1144), which appears in **B_0 = 4.1C_r/(1 − qL²) = 46.8**
   (`REVIEW_SQ_S4.md` l.371) three symbols from **A_0 = c_NC_T′(2.47N√κ_+ + 32^{1/q}C_0)`**. Both are
   inputs to **C_D = max{G, C_r}, G = 2(1.011A_0 + B_0)**.
2. **θ_0^{SQ4}'s binding entry has flipped and no file records it.** `SYMBOLS.md` l.464 and
   `REVIEW_SQ_S4.md` S4-14 record **"θ_G binds"**, correct at ε_* = 10⁻⁴. `EPSSTAR.md` §3.2 ruled
   ε_* = 10⁻⁴ **inadmissible**; at the floor ε_* = 1.12·10⁻³⁷ (`EPSSTAR.md` l.482), **θ_ε ≈ 2.1·10⁻³⁹
   ≪ θ_G ≈ 10⁻¹³ and θ_ε binds, by 26 orders.** θ_G regains the min only for **q > 5.57·10²⁶**
   (QFIX §5.4).

### 12.4 For `TAUFLAT.md`'s owner (§4 A, §6)

The **9.707-decade** energy shortfall and the **4.854-decade** ε_1 shortfall are both evaluated at
C_D = 0.9·10³·C_T(q = 12). With the prefactor's own q-dependence restored they are **9.428 / 4.714** at
q = 12 and **6.479 / 3.240** at the q-plateau. Suggested: carry both as functions of q beside their
numbers, exactly as l.566-567 instructs for η_♭. Option **A stays dead** at every q (QFIX §6: the
plateau is 98.57 % c_g). Priced exactly [`checks/qf1c_out.txt`, POST-HOC]: the room between
c_s = 411.92297 and `EPSSTAR.md` l.608's floor c_s ≥ 319.2 is **0.1166 decades of C_T at q = 12**
(reproducing TAUFLAT's 0.080 against its rounded 4.4·10¹² floor), **0.0067 at q = 32** and **0.0014 at
the plateau** — so **the 0.578 decades `EPS1_EXEC.md` §4.5 found "over q" is the q-lever itself, not
room in c_s**, and once q is spent option A has ≈ 0.001 decades, not 0.578. Option A stays dead either
way; the point is that the two were never additive.

### 12.5 For `EPS1_EXEC.md`'s owner / whoever lands (C4)

- The §4.4 q-table moves C_T(q) with **Λ frozen at its q = 8 value**. With Λ(q) restored the spread
  over q ≥ 11 is **2.037 decades, not 1.690**, and the plateau gain is **1.474, not 1.157**.
- **The value to land is not 9.38·10⁻⁴⁵.** At the recommended q it is
  **ε_1 ≤ 3.8·10⁻⁴³ (q = 1000, c_N = 2, C_3 = 1)**, or **3.5·10⁻⁴³ at q = 100** — two significant
  figures, with the parametric form of §7.1 beside it, because the c_N ∈ [1,2] band alone is a factor 4.
- §4.6's reasoning ("three significant figures, admissible at every published precision") is **right
  and should be kept**; only the evaluation point changes.

### 12.6 For the lead / `HANDOFF.md` item 4

- **Item 4's question is answered: take q at the plateau.** q = 8 is not merely "the worst admissible
  choice" — in the lane's own DX′ currency it is **24.089 decades below the plateau**, and q = 12 is
  **5.898** below it. Item 4's "at q ≈ 30 it is under [10¹³]" is true and understates the target:
  q = 32 still leaves **0.627 decades** on the table and the curve is flat only above q ≈ 100.
- **The 10¹³ ceiling should be retired in favour of C_D ≤ 6.7·10¹⁵.** It is a rounded, q = 8-evaluated
  proxy and it has already produced one wrong endpoint (`EPSSTAR.md`'s q_min = 11).
- **The next target after q is `c_g` = 5699.63 (`STAR_CONST.md` §7), which is 98.57 % of Ĉ at the
  plateau**, and before it the **P-max vs P-ct β-power question** (`STAR_CONST.md` §6.4, ARGUED), which
  is worth **13.15 decades of DX′-margin** — more than everything remaining in q, and enough to
  **dissolve the (C4) ε_1 edit entirely** and to **restore HIST A5's DESC-ε size clause**. One branch of
  one Young step decides it.
