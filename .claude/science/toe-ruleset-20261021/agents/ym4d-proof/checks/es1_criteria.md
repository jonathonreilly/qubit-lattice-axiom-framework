# es1_criteria.md — pre-registered criteria for the (EPS-STAR) check

Written **2026-10-28 14:14 UTC** (local 10:14 EDT), **after** EPSSTAR.md §1 (14:00:05 UTC) was on disk and
**before** `checks/es1_eps.py` existed. The time in this header is the time of writing; if it later disagrees
with the file's mtime by a minute I will record that in EPSSTAR.md rather than edit this file.

## 0. Rule compliance

**This file contains no constant derived in this session.** Every number appearing below is one of:

| symbol | value | provenance (all landed before this file existed) |
|---|---|---|
| c_s = C_1·C_V^source | 411.9229708842423061 | STAR_CONST.md §7 (exact, `sc1_out.txt` SC1-4) |
| c_g = C_1 | 5699.632830341894211 | STAR_CONST.md §7 (exact) |
| c_K = C_1·C_V^{curv,lin} | 17.51·C_K′·c_N | STAR_CONST.md §8.1 |
| c_RB = C_1·C_V^{curv,quad} | 17.51·290·(576c_N² + C_B²c_N⁴) ≈ 3.0·10⁶ at (c_N,C_B) = (1,3.6) | STAR_CONST.md §8.1 |
| C_K′ | SUPPLIED, ∈ [3.9, 1.92·10⁴] | STAR_CONST.md §4.4, §8.1 |
| c_N | ∈ [1, 2] | REVIEW_SQ_S4 S4-16 |
| C_B | SUPPLIED, no bound in SQ.md; reference 3.6 | SQ.md l.1429 (q5 B1); STAR_CONST §4.3 |
| \|N_3^plaq\| | 7⁴·6 = 14406 | CONST_T.md §2.3 |
| \|N_1^plaq\| | 3⁴·6 = 486 | CONST_T.md §2.3 |
| \|𝒩_S\|, \|L_rev\| | 3, 3 | STAR_CONST.md Lemmas A1-A3 (the sharpened source counts) |
| C_S | 3 | SQ.md l.1453 (SOB (a)) |
| F | ≤ 175.8 | CONST_T.md §3.2 (optimised schedule) |
| B(4), B(8) | 43.95, 1931.5 | CONST_T.md §3.1 |
| the telescope factor to use | B(4·max{a,2}) = B(8) for q ≥ 8 (P-max) | STAR_CONST.md §6.4, §11.2 |
| C_T ceiling | 10¹³ | REVIEW_SQ_S4 S4-16 |
| A_cγ_c target | 3.4·10³ (3.35·10³ at q = 12) | STAR_CONST.md §8.3 |
| ε_* floor for t_pr > ε_1 | 5.6·10⁻³⁸ | REVIEW_SQ_S4 S4-16 ("θ_ε ≈ ε_*/84, so t_pr > ε_1 needs ε_* ≳ 5.6·10⁻³⁸") |
| θ_ε / ε_* | 1/84 | REVIEW_SQ_S4 S4-16 (from SQ.md l.1622) |
| θ_G, τ_R, η_♭, t_pr, ε_1 | 1.46·10⁻¹³, 2.75·10⁻¹⁵, 4.2·10⁻³⁶, 1.5·10⁻¹³, 6.7·10⁻⁴⁰ | REVIEW_SQ_S4 S4-14, S4-16 |
| C_err model, C_D | C_err = 1.655·10⁷·C_D², C_D ≈ (0.5-0.9)·10³·C_T, C_D ≤ 6.7·10¹⁵ | REVIEW_SQ_S4 S4-16 |
| C′, c_♭ | 53, 1/640 | SQ.md §0.3, l.219, l.349 |
| A5's energy / η_♭ clause | ε_1 ≤ ½√(η_♭/C_3) | REVIEW_HIST_S4 strategic 4 (l.498); SQ.md l.223 |
| R_0 | 64 (SQ.md l.1466, written), 128 (REVIEW_SQ_S4 S4-6), 32 (CONST_T §3.2) | as cited |

Arithmetic: `fractions.Fraction` and `decimal.Decimal` only, in plain `python3 -I`, single thread, no numpy,
no BLAS, **no numeric lock taken** (exact rational / fixed-precision decimal only). Two precisions, 40 and 60
significant digits, must agree on every verdict.

## 1. What the script computes

The script evaluates the formulas EPSSTAR.md §2-§4 will derive. **The formulas are inputs to the script, not
outputs of it**; the script's job is arithmetic, precision control and monotonicity. Its blocks:

- **Block A — harness validation.** B(m) := Π_{i≥0}(p_i − 1)^{m/p_i}, p_i = 2^{i+1}, at m = 4 and m = 8.
- **Block B — the Stage-1 constant** C_{S1}(q, m) from its closed form, and the scale-invariance identity
  (−2 + 8/q)·q/(q−4) = −2 checked as an exact rational at every q on the grid.
- **Block C — the uniform bound** on A_cγ_c as a function of the margin m, with no c_K, c_RB, C_B, C_K′ or c_N
  in it; and the smallest integer m meeting the 3.4·10³ target and the 1 target.
- **Block D — C_T** under P-max (B(8)) and, for comparison, P-ct (B(4a)), at q ∈ {10, 11, 12, 16, 24, 32, 50, 100}.
- **Block E — ε_*'s value and the audit floors**: ε_*(m, c_K, c_RB) from the Stage-1 absorption inequality at the
  two ends of C_K′ × c_N, against 5.6·10⁻³⁸ and against the no-change floor 84·θ_0^{SUP}, θ_0^{SUP} = 1/(2C_err).
- **Block F — precision**: Block A-E rerun at 60 digits; verdicts compared.

## 2. PRE-REGISTERED verdicts

| id | verdict statement | PASS iff |
|---|---|---|
| **ES1-1** | the B-harness reproduces CONST_T §3.1 | B(4) and B(8) each within 0.5 % of 43.95 and 1931.5 |
| **ES1-2** | the Stage-1 step is exactly scale-invariant and C_{S1} is finite | (−2 + 8/q)·q/(q−4) = −2 **exactly** as a Fraction at every q on the grid, AND C_{S1}(12, 1) < 10⁵ |
| **ES1-3** | **the result.** The uniform bound on A_cγ_c clears STAR_CONST §8.3's condition at some integer margin m | there is an integer m ≤ 10³ with the uniform bound ≤ 3.4·10³ **and** 3.35·10³ (the q = 12 value) |
| **ES1-3b** | the stronger reading STAR_CONST §6.3 assumed | there is an integer m ≤ 10⁶ with the uniform bound ≤ 1 |
| **ES1-4** | **the interface.** C_T at q = 12 under P-max, with the ES1-3b margin, is a number under the ceiling | C_T(q = 12, P-max) ≤ 10¹³ |
| **ES1-4b** | the same at the ES1-3 margin (minimal m) | C_T(q = 12, P-max) ≤ 10¹³ |
| **ES1-5** | **the audit.** The ε_* that the ES1-3b margin needs exceeds REVIEW_SQ_S4's floor at BOTH ends of the SUPPLIED range of C_K′·c_N | ε_*(m, c_K) > 5.6·10⁻³⁸ at c_K = 17.51·3.9·1 **and** at c_K = 17.51·1.92·10⁴·2 |
| **ES1-5b** | the same against the no-change floor 84·θ_0^{SUP} computed at the ES1-4 value of C_T | ε_*(m, c_K) > 84/(2·1.655·10⁷·C_D²) with C_D = 0.9·10³·C_T, at both ends |
| **ES1-6** | monotonicity sanity | the uniform bound is non-increasing in m; C_T(q) is non-increasing in q on the grid under P-max; A_cγ_c is increasing in ε_* at fixed c_K |
| **ES1-7** | precision | 40-digit and 60-digit runs give identical verdicts and identical values to the stated precision |

## 3. What counts as a FAIL, and what I will do with one

- **ES1-3 FAIL** (no integer m ≤ 10³ reaches 3.4·10³) ⟹ EPSSTAR verdict **FAIL-ARITH**. The failing output and
  script are kept unaltered; any repair runs under a new id (`es1b_`) with this criteria file untouched.
- **ES1-4 FAIL** ⟹ the interface carries no number at q = 12; I must then report the smallest q that works, or
  that none does, and the verdict is **FAIL-ARITH** on the interface clause.
- **ES1-5 or ES1-5b FAIL** ⟹ EPSSTAR verdict **FAIL-CONSUMER**: lowering ε_* enough to pin A_cγ_c pushes ε_*
  below a floor a consumer needs. This is the outcome my brief singles out as a real finding and I report it as
  one, naming the consumer and the clash in decades, whatever it does to the rest.
- **ES1-2 FAIL** on the exact-rational identity ⟹ the Stage-1 step is not scale-invariant as derived and the
  derivation is wrong, not the arithmetic: **OPEN-STEP**, with the error named.
- Any probe I run after seeing an output is labelled **[POST-HOC]** in the script source and in the output.

## 4. One thing this check cannot decide

It cannot decide whether C_B and C_K′ are finite — that is BIA's and WB's business and SQ.md states both lemmas
with a finite constant. The check can only confirm that **no number it reports depends on them**. If any
reported C_T value changes when C_K′ or C_B is varied over its SUPPLIED range, that is a genuine failure of the
uniformity claim and I will report it as such (it is tested explicitly in Block D as a sensitivity sweep).
