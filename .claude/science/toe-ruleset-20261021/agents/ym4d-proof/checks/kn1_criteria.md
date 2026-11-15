# kn1 — pre-registered criteria (written BEFORE any script of this session)

Owner: the T55-A worker, session 25. Companion file: `../KN_ADOPT.md`.
**Written before `kn1_h1.py` and `kn1_gain.py` exist.** Every constant named below is transcribed from a
file that predates session 25, with its file:line; **no constant derived in session 25 appears here.**

Arithmetic contract: exact `fractions.Fraction`; `Decimal` at **50 and 100** digits for log10 display
only; plain `python3 -I`, single thread, no numpy / BLAS / SciPy. No numeric lock (exact rational
arithmetic, brief rule 6). Every decade figure formed as an exact rational ratio.

## Transcribed inputs (file:line, all pre-session-25)

| symbol | value | source |
|---|---|---|
| d, L | 4, 3 | RLARGE.md l.1009 (constants block), PROOF.md l.703 |
| A_d(L) | (d−1)L(L−1)/2 = 9 | RLARGE.md l.973 |
| η_1 (quadratic, symbol 1) | min{ε_1/(2L²), ε_1²/(512N·A_d)} = min{ε_1/18, ε_1²/(4608N)} | RLARGE.md l.64, l.1009 |
| η_q | min{ε_1/(2L²), ε_1/(256N·A_d), δ_0/A_d} = min{ε_1/18, ε_1/(2304N), δ_0/9} | RLARGE.md l.64; HIST.md l.180 |
| η_1 (linear, symbol 2) | c_1ε_1, c_1 = 1/(2(L² + 5.5A_d)) = 1/117 | EXISTENCE.md l.1771, l.1774-1775 |
| a_η (bare level) | η_1²/(2N) | RLARGE.md l.1026 |
| a_RS | min{a_η, κε_1²/(256N)}, κ = 1 | RLARGE.md l.1020 |
| c_RS | 5⁴ = 625 | RLARGE.md l.1021 |
| joint-route cube factor | 81 | HIST.md l.186 |
| ceiling convention | g_K² ≲ a/10² | RLARGE.md l.616-617 |
| DX′ | 2.456·10⁻¹⁵²/C_Ω, taken at C_Ω = 1 | REVIEW_SF_S7.md l.203 |
| ε_1 "today" | 6.7·10⁻⁴⁰ | **RLARGE.md l.72** (headline) |
| ε_1 "proposed" | 9.38495112638·10⁻⁴⁵ | **EPS1_SWEEP.md l.455** (owner-gated, undecided) |
| S4′ index set | σ ∈ S_d (d! orders) × y ∈ B(X) (L^d sites) | PROOF.md l.711-714 |
| M̄_c | (d!L^d)^{-1} Σ_σ Σ_{y∈B(X)} T^σ_y(U) | **PROOF.md l.1754** |

Figures **under test** (transcribed, never inputs): gain 82.141 / 91.848 decades and margins
−15.617 / +66.523 (ARS_FIX.md l.451-455); η_1/η_q = 39.3846 (N = 2) / 59.0769 (N = 3) and the route
figure **1551×** (ARS_FIX.md l.526, l.536-537); η_q/η_1 → 117/4608 (ARS_FIX.md l.538).

---

## kn1-1 — H1: is the S4′ average a convex combination?

**Object.** The weight family w of PROOF.md l.1754, on the index set of PROOF.md l.711-714.

- **CONVEX** iff, as exact rationals, (i) every w_i ≥ 0 and (ii) Σ_i w_i = 1 **exactly**, with the index
  count equal to d!·L^d, for **every** (d, L) in {(2,3),(3,3),(4,3),(5,3),(4,5)} — i.e. the property is
  not an accident of d = 4, L = 3.
- **NOT-CONVEX** iff either clause fails for any of those (d, L).
- **DEGENERATE-BUT-CONVEX** (a reportable third outcome) iff distinct index pairs (σ,y) can give the
  *same* transporter, so the induced weights on **distinct** transporters are non-uniform: then I must
  check that the induced family is still nonnegative and sums to 1, and say so.

**Designed-FAIL control (mandatory, defect 3).** A signed family with the same total mass 1 —
w_1 = 1 + a, w_2 = −a, a > 0 — on T_1 = e^{X}, T_2 = e^{−X}, X = iθ·diag(1,−1) ∈ su(2), θ = 1/4,
a = 3, S = 1. The control **must**:
  (c-i) be rejected by clause (i) of the CONVEX test, and
  (c-ii) **break Lemma KN′'s conclusion ‖W′^{-1}M̄ − 1‖_op ≤ 3δ²** with δ = max_i‖X_i‖_op = θ,
         i.e. return ‖R‖_op > 3δ² = 3/16.
If (c-ii) does **not** fail, the gate has **NO POWER** — convexity would not be load-bearing in KN′ —
and I report NO POWER rather than a PASS, and re-run under a new id.

**Second control (independent, from a different owning file).** PROOF.md l.1755 separately asserts
**‖M̄_c‖_op ≤ 1**. For a mean of unitaries that holds iff the weights are a probability vector. The
control family above **must** violate ‖M̄‖_op ≤ 1. If it does not, this leg has no power and is reported
as such.

## kn1-2 — the two decade gains (ARITH-F1 is the failure mode)

For each ε_1 ∈ {today (RLARGE l.72), proposed (EPS1_SWEEP l.455)} and each N ∈ {2,3}: compute, exactly,
η_1 in both forms; a_η = η_1²/(2N); a_RS = min{a_η, ε_1²/(256N)}; which branch is active; the ceiling
a_RS/10² and a_RS/(c_RS·10²); the margin log10(ceiling/DX′); and **GAIN := margin_linear − margin_quadratic**.

- **GAIN-REPRODUCES** iff the gain at today's ε_1, N = 2, is within **0.1 decade** of 82.141 **and** the
  gain at the proposed ε_1, N = 2, is within 0.1 decade of 91.848.
- **SOURCE-DISAGREES** otherwise, with both figures given exactly and the direction stated.
- The **branch** verdict is reported separately: EXP-4 if the a_η entry is active under the quadratic form
  (so a_RS ∝ ε_1⁴), EXP-OTHER otherwise.
- The gain's **N-dependence** is reported, since c_1 is N-free and the quadratic entry is not. A gain that
  differs between N = 2 and N = 3 must be labelled with its N.

**Designed-FAIL control (ARITH-F1 itself).** Recompute the gain with the two ε_1 **swapped** against
their labels. The control **must** return a figure differing from the correct one by ≥ 1 decade (the
signature of quoting a difference at the wrong ε_1). If swapping the ε_1 changes nothing, the check
cannot detect ARITH-F1 and has **NO POWER**.

**Power leg.** Recompute with the counterfactual c_1 = 1/(2L²) = 1/18 (RLARGE's own linear entry). The
gain **must** move by 2·log10(117/18) ≈ 1.6 decades; if it does not, the gain is not a function of c_1
and the check has no power.

## kn1-3 — the two reversals the adoption forces

**(a) RLARGE l.65's ordering.** η_1/η_q, with the δ_0/A_d entry of η_q omitted (its omission can only
lower η_q and enlarge any reversal; recorded as a stated one-sided reading).
- **ORDER-PRESERVED** iff η_1 ≤ η_q; **ORDER-REVERSED** iff η_1 > η_q.
- Pre-registered: the **quadratic** form must return ORDER-PRESERVED at every ε_1 ≤ 2 (this is
  REVIEW_RLARGE_V2 §2.3's "CORRECT", a verdict written before this proposal, for another purpose — so
  this leg can fail against another author's endorsement). The **linear** form's verdict is the result.
- The ratio η_1/η_q under the linear form must be an **ε_1-free constant**; I test it at two ε_1 values
  and require exact equality. Its value is the result (transcribed figure under test: 39.3846 / 59.0769).

**(b) HIST l.186's route comparison.** HIST l.186-187 names **two** factors: c_RS = 81 against 5⁴ = 625,
**and** η_q² against η_1². The route comparison is therefore the ratio of **binding exponents**
  RS/joint = [a_η(η_1)/625] / [a_η(η_q)/81] = (81/625)·(η_1/η_q)².
- **RS-WORSE** iff that ratio < 1, **RS-BETTER** iff > 1. Pre-registered: quadratic → RS-WORSE,
  linear → the result.
- Separately report the **η-factor alone**, (η_1/η_q)². **ROUTE-FIGURE-REPRODUCES** iff the *route*
  ratio (binding exponents, both factors) is within a factor 1.2 of the transcribed **1551**;
  **SOURCE-DISAGREES** iff it is not, in which case I state which of the two quantities 1551 is.

**(c) HIST l.181's η_q/η_1.** Under the quadratic form it must come out **2/ε_1** (ε_1-DEPENDENT); under
the linear form it must come out the ε_1-free constant 117/4608 at N = 2. The quadratic leg is this
check's **own designed-FAIL control for the "ε_1-free" property**: it must return ε_1-DEPENDENT.

## kn1-4 — the patch's identities

Exact, at d = 4, L = 3: (i) c_1 = 1/(2(L² + 5.5A_d)) = **1/117**; (ii) (L² + 5.5A_d)·c_1 = **1/2**;
(iii) t/2 + 4·(t/8) = t; (iv) (t/8)²/(4N) = t²/(256N).
- **IDENTITIES-HOLD** iff all four are exact equalities of Fractions.
- **Designed-FAIL control:** replace 5.5 by 5 and keep c_1 = 1/117. Clause (ii) **must** fail. If it does
  not, the identity check has no power.

## kn1-5 — two precisions

Every decade figure recomputed at 50 and 100 Decimal digits. **PASS** iff the worst disagreement is
< 10⁻³⁰ decades; otherwise **FAIL of the arithmetic** (not of the claim), reported as such.

---

## Statuses available to the outcome

PROVEN / COMPUTED / ARGUED / CONDITIONAL (naming the input) / GAP / OPEN. A failed check is reported as a
**FAIL** with script and output kept **byte-unaltered**; a re-run takes a new id and leaves this file
untouched; anything run after seeing a result is labelled **POST-HOC**.
