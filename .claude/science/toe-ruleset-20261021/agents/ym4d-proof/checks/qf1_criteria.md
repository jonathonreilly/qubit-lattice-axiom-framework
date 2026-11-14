# checks/qf1_criteria.md — pre-registered criteria for T55-N (QFIX.md)

Written **2026-10-28 21:48 UTC**, **after** `QFIX.md` §1 (PRE-STATED) and **before** `checks/qf1_q.py`
exists. Every constant below is **inherited** and carries its file:line. **No constant in this file was
derived in session 25.**

Arithmetic: plain python, `fractions.Fraction` + `decimal.Decimal`, single thread, no numpy/BLAS, no
numeric lock (exact/decimal only, per the brief's rule 6).

---

## 0. Inherited inputs (file:line for each)

| symbol | value | source |
|---|---|---|
| c_s | 411.9229708842423061 | `STAR_CONST.md` §7 (exact); used at `checks/es1_eps.py` l.33 |
| c_g | 5699.632830341894211 | `STAR_CONST.md` §7 (exact); `checks/es1_eps.py` l.34 |
| \|𝒩_S\| = \|L_rev\| | 3 | `STAR_CONST.md` Lemma A2; `EPSSTAR.md` l.147 |
| \|N_1^plaq\| / \|N_3^plaq\| | 486 / 14406 | `CONST_T.md` §2.3 |
| F (schedule) | 175.8 | `CONST_T.md` §3.2 |
| R_0 | 64 | `SQ.md` l.1466 (written value) |
| B(m) = Π_{i≥0}(p_i−1)^{m/p_i}, p_i = 2^{i+1} | B(4) = 43.95, B(8) = 1931.5 | `CONST_T.md` §3.1 |
| β-power conventions | **P-max** B(4·max{a,2}) = B(8) ∀q ≥ 8; **P-ct** B(4a) | `STAR_CONST.md` §6.4, l.386 |
| A_sγ_s | 36·c_s·\|𝒩_S\| | `EPSSTAR.md` l.21, l.272 |
| 288·C_1·Q | 288·[c_g + 18(\|𝒩_S\|·c_s·‖V_s‖_∞ + 1/(36m))], ‖V_s‖_∞ ≤ R_0^{−2+8/q} | `STAR_CONST.md` l.282; `checks/es1_eps.py` l.153 |
| A_cγ_c | ≤ (1+√6)·C_{S1}(q,m)/m (Theorem ES-1) | `EPSSTAR.md` §3, l.733 |
| C_{S1}(q,m) | {[1 − ¼ − 1/(4m)]^{−1}[c_ϑ(27c_s)^a + 4096c_g]}^{1/2} | `EPSSTAR.md` l.733 |
| c_ϑ | (1−ϑ)(4ϑ)^{ϑ/(1−ϑ)}, ϑ = 4/q, a = 1/(1−ϑ) = q/(q−4) | `EPSSTAR.md` l.238 |
| m (allocation) | 19615 (A_cγ_c ≤ 1) and 7 (A_cγ_c ≤ 2.87·10³) | `EPSSTAR.md` l.545, l.351 |
| C_T′ | 2^{2+4/q}·4·C_T | `SQ.md` l.1513; `REVIEW_SQ_S4.md` l.370 |
| A_0 | c_N·C_T′·(2.47N√κ_+ + 32^{1/q}C_0) | `SQ.md` l.1624; `REVIEW_SQ_S4.md` l.370 |
| 2.47N√κ_+ | 4.94 (N = 2, κ_+ = 1) | `REVIEW_SQ_S4.md` l.371 |
| C_0 | 3.34 | `REVIEW_SQ_S4.md` l.371 |
| c_N | ∈ [1, 2] | `REVIEW_SQ_S4.md` l.371 |
| B_0 | 46.8 (= 4.1C_r/(1 − **q**L²) — note: that **q is SQ.md l.1524's decay ratio, not the Moser exponent**) | `REVIEW_SQ_S4.md` l.371; `SQ.md` l.1144, l.1524 |
| C_D | max{G, C_r}, G = 2(1.011A_0 + B_0) | `SQ.md` l.1633-1634 |
| C_D ≈ (0.5−0.9)·10³·C_T | the recorded reduced form | `REVIEW_SQ_S4.md` S4-16 (l.374); `EPSSTAR.md` l.472 |
| C_err | 1.655·10⁷·C_D² | `REVIEW_SQ_S4.md` S4-16; `EPSSTAR.md` l.472 |
| θ_0^{SUP} = t_pr | 1/(2C_err) = 1/(3.31·10⁷·C_D²) | `EPSSTAR.md` l.472, l.519 |
| η_♭ | c_♭t_pr²/C′⁴ = t_pr²/5.05·10⁹ (c_♭ = 1/640, C′ = 53) | `EPSSTAR.md` l.521; `TAUFLAT.md` §2.2 |
| DESC-ε size clause | η_♭ ≥ 4C_3ε_1² | `EPSSTAR.md` l.527; `REVIEW_HIST_S4` strategic 4 |
| C_D ceiling (RLARGE a_bad) | C_D ≤ 6.7·10¹⁵ | `REVIEW_SQ_S4.md` S4-16; `EPSSTAR.md` l.602 |
| ε_1 (headline) | 6.7·10⁻⁴⁰ | `RLARGE.md` l.72 |
| a_RS at the four live ε_1 | 7.65720e−165 (1.27e−39), 2.41770e−165 (9.52e−40), 1.88863e−165 (8.95e−40), **5.93136e−166 (6.7e−40)** | `ARS_FIX.md` §2.2 table |
| a_RS ceiling convention | a_RS/10² (bare, `RLARGE.md` l.616-617) and a_RS/(c_RS·10²), c_RS = 5⁴ = 625 (`RLARGE.md` l.1021) | `ARS_FIX.md` §2.2 |
| DX′ | 2.456·10⁻¹⁵²/C_Ω, every figure linear in C_Ω | `REVIEW_SF_S7.md` l.203 |
| margin convention | margin = log₁₀(item ceiling) − log₁₀(DX′) | `ARS_FIX.md` l.267-271 |
| θ_G | ≤ 1.46·10⁻¹³ at q = 8; largest θ with qβ ≤ ½; **θ_G ∝ 1/q** | `REVIEW_SQ_S4.md` S4-14; `CONST_T.md` l.309-312 |
| θ_ε | ε_*/max{4·2.47N√κ_+, 16·32^{1/q}C_0} (= ε_*/84 at q = 8) | `EPSSTAR.md` l.439-441 |
| ε_* floor | 84·θ_0^{SUP} = 1.12·10⁻³⁷ | `EPSSTAR.md` l.482 |

---

## 1. PRE-REGISTERED VERDICTS

`QFIX.md` §1.4 pre-registered **QF1-1 … QF1-7**. They are repeated verbatim in substance below.
**QF1-8 and QF1-9 are added here**, before the script exists, and **QF1-8 carries a disclosure**: I
formed its expectation by hand arithmetic while reading `EPSSTAR.md` §6.6, *before* writing this file,
so the script **verifies** rather than discovers it. It is labelled **POST-HOC-HAND** in the output and
in `QFIX.md`. QF1-9 is blind.

| id | claim | PASS | FAIL |
|---|---|---|---|
| **QF1-1** | harness reproduction | my C_T(q) reproduces `EPSSTAR.md` l.547-553's seven-row q-table (m = 19615 and m = 7) to **3 significant figures**, and B(4), B(8) to `CONST_T.md` §3.1's values within 0.5 % | any m = 19615 row off by > 1 % |
| **QF1-2** | monotonicity and plateau | C_T(q) strictly decreasing on q ∈ (4, ∞) under P-max, with a finite positive limit as q → ∞ | non-monotone or divergent |
| **QF1-3** | q ≥ 11 is a *consumer ceiling*, not admissibility | every structural clause of the step (q > 4; σ = q/2 > 2; ϑ = 4/q; a = q/(q−4) > 1; the identity (−2 + 8/q)·a = −2) is satisfied **as an exact Fraction** at q = 5, 6, 8, 10, 12, 16, 32, 100 — i.e. nothing in the mathematics excludes q < 11 | some structural clause fails as an exact Fraction at some q > 4 |
| **QF1-3b** | the one structural clause with a floor above 4 | ϑ = 4/q ≤ ½ (hence c_ϑ ≤ 1 as `CONST_T.md` l.158 asserts) is **FALSE** for q ∈ (4, 8) and TRUE for q ≥ 8, as an exact Fraction | it holds for all q > 4 (which would make `CONST_T.md` §4.2's "all hold for every q > 4" correct) |
| **QF1-4** | the C_D prefactor is q-dependent and was frozen | Λ(q) := 4·2^{2+4/q}·(4.94 + 3.34·32^{1/q}) satisfies \|Λ(12)/Λ(8) − 1\| > 5 %, and Λ(8)/Λ(∞) > 1.5 | \|Λ(12)/Λ(8) − 1\| ≤ 5 % |
| **QF1-5** | the objective has a finite plateau | the objective (defined in §2) is non-decreasing in q over q ∈ [8, 10⁶] and its total rise from q = 12 to q = 10⁶ is finite and ≤ 20 decades | the objective is unbounded in q (⇒ a consumer has been missed) |
| **QF1-6** | **designed-FAIL control** | a control run in which C_T and Λ are replaced by q-independent constants returns **NO-LEVER** (objective spread **exactly 0** decades over the grid), while the live run returns a spread > 0.30 decades (the threshold `EPS1_EXEC` used for VALUE-PARAMETRIC, itself inherited from `EPS1_SWEEP` §1.1's dismissal of a 0.28-decade spread) | the control also moves, i.e. the harness moves for some reason other than q |
| **QF1-7** | exactness | every reported figure is identical at Decimal precision 40 and 60 | any disagreement |
| **QF1-8** | **[POST-HOC-HAND]** `EPSSTAR.md` l.525's internal consistency | solving η_♭ = t_pr²/5.05·10⁹ ≥ 4C_3ε_1² at ε_1 = 6.7·10⁻⁴⁰, C_3 = 1 reproduces `EPSSTAR.md` l.525's "t_pr ≥ 3.01·10⁻³⁵" to within 1 % | it does not — in which case I report the self-consistent value, the ratio, and the knock-on to l.525's C_D and C_T ceilings |
| **QF1-9** | a_RS's power in ε_1 | a_RS(ε_1) = 5.93136·10⁻¹⁶⁶·(ε_1/6.7·10⁻⁴⁰)^p reproduces **all four** other `ARS_FIX.md` §2.2 rows to ≤ 0.2 % for **exactly one** integer p ∈ {1,…,6}, and the resulting margins reproduce ARS_FIX's −14.506 / −15.007 / −15.114 / −15.617 / −35.032 to ≤ 0.01 decades | no single integer p fits, or the margins do not reproduce |

---

## 2. The objective, defined before it is computed

For each q, with C_3 = 1, C_Ω = 1, N = 2, κ_+ = 1, c_N ∈ {1, 2}:

1. **C_T(q, m)** from §0's formula, under P-max (headline) and P-ct (sensitivity).
2. **C_D(q) = 2(1.011·A_0(q) + B_0)**, A_0(q) = c_N·4·2^{2+4/q}·C_T(q)·(4.94 + 3.34·32^{1/q}).
3. **t_pr(q) = θ_0^{SUP}(q) = 1/(3.31·10⁷·C_D(q)²)**.
4. **ε_1^cut(q)** = the largest ε_1 with η_♭ = t_pr²/5.05·10⁹ ≥ 4C_3ε_1², i.e.
   **ε_1^cut(q) = t_pr(q)/(2√(5.05·10⁹·C_3))**.
5. **ε_1^eff(q) = min{6.7·10⁻⁴⁰, ε_1^cut(q)}**.
6. **OBJECTIVE(q) := log₁₀(a_RS(ε_1^eff(q))/10²) − log₁₀(2.456·10⁻¹⁵²)**, the a_RS margin against DX′
   in the bare convention; reported also in the c_RS = 625 convention.
   Reported alongside, as the other live ceilings: the **(CLS-min)→RLARGE** headroom
   log₁₀(6.7·10¹⁵/C_D(q)); the **a_bad** headroom log₁₀(t_pr(q)/ε_1^eff(q)); and the **DESC-ε**
   shortfall log₁₀(4C_3(6.7·10⁻⁴⁰)²/η_♭(q)) at the *unlowered* ε_1.

**Reported, not optimised:** θ_G(q) = 1.46·10⁻¹³·(8/q) and its headroom over ε_1^eff(q); this is the
only consumer that moves against q.

**Argmax rule, fixed now:** the recommended q is the smallest grid point whose objective is within
**0.05 decades** of the supremum over the grid. (Chosen so the recommendation is a plateau entry point,
not a spurious last digit.)

---

## 3. What would make me report NO RESULT

If QF1-1 fails at > 1 %, I report the reproduction FAIL and do **not** publish an objective curve built
on an unreproduced harness; I would then report only the structural findings (QF1-3, QF1-3b, QF1-4) and
the provenance of q.
