# ru55_3 — criteria (written BEFORE checks/ru55_3_u1.py exists; `date -u` appended at the end)

Question: RLARGE_U55 §1 (U1). Exact/rigorous arithmetic for (a) a_ret^{PLD}'s entries and its ratio to a_bad; (b) the (L618-δ)
budget (RLF-δ vs DX′) as a function of (SC)_k's unknown (C, p); (c) the "+63.6" family of margins under the live alternatives;
(d) route (iii)'s a_A ≥ θa_bad threshold. Plain python, Fractions; every logarithm is a rigorous rational enclosure (atanh series
with an explicit geometric remainder bound; ln x = ln m + k·ln 2, m ∈ [1, 2)); floats only in labelled displays.

Inputs: d = 4, L = 3, A_d = 9, n_P = 1296, b_1 = 1296 + 1200κ; c_pr = 1/(640·53²) = 1/1797760; ε_1 = 6.7·10⁻⁴⁰ (exact decimal);
a_bad = c_prε_1² (ε_1 < t_pr); η_q = ε_1/(256NA_d); ε_loc² = ε_1²/(4Nb_1); σ_fl² = 16/λ_min (PLD's Gaussian part);
λ_min ∈ {3.17·10⁻³, 4.23·10⁻³} and, as a sensitivity row only, 6.6·10⁻¹⁰ (REVIEW_PLD_S3 L0-1; settled by [SF7-edit]);
DX′ = 2.5·10⁻¹⁵²/C_Ω with C_Ω ∈ {1, 3(N² − 1)/2}; grid N ∈ {2, 3}, κ ∈ {1, 1/4}.

Gates (pre-registered):
- U1-1 (binding entry): with a_J := κε_1²/(2048N), a_fl := 49η_q²/(1024σ_fl²), a_γ := κε_loc²/(64N): PASS iff a_fl < min{a_J, a_γ}
  at all 2·2·3 grid points. Report a_ret^{PLD}/a_bad exactly and as a display.
- U1-2 (reproduction of PLD check p4 E2): at N = 2, κ = 1: a_fl/ε_1² within 0.1% of 4.465·10⁻¹³ (λ_min = 3.17·10⁻³) and of
  5.958·10⁻¹³ (4.23·10⁻³); a_ret/a_bad within 0.1% of 8.027·10⁻⁷ and 1.071·10⁻⁶. PASS iff all four.
- U1-3 ((L618-δ) budget): t_DX := C_Ω/(2.5·10⁻¹⁵²), B := a_ret^{PLD}·t_DX, Lt := ln t_DX (enclosure). Condition (L618-δ):
  ln C + (P/2)·Lt ≤ B, P := 12 + p(SC). Report B, Lt, P_max(ln C = 0) and lnC_max(P = 12). Pre-registered envelope tests at
  N = 2, κ = 1, C_Ω = 1: (i) λ_min = 3.17·10⁻³: the condition HOLDS at (P, ln C) = (10⁵⁸, 10⁶⁰); (ii) λ_min = 6.6·10⁻¹⁰: it HOLDS at
  (10⁵¹, 10⁵³). Also verify t_DX ≥ P/(2a_ret) at those P (monotonicity premise of RLARGE_U55 §1.3). PASS iff (i), (ii) and the
  premise all hold.
- U1-4 ((RLF-δ) ceiling, illustrative, and reproduction of PLD p4 E3): solve a_ret·t = (P/2)ln t + ln C for t (geometric bisection,
  rigorous logs) and report g²_δ = 1/t for (p(SC), ln C) ∈ {(6, 0), (6, 50), (12, 0), (12, 50)} (PLD's E3 set, with P = 12 + p)
  and (702, 10⁵) (illustrative: p of CL^J's size; ln C of the size of CL^J's r^{-(N²−1)n_ℓ} factor — labelled ILLUSTRATIVE).
  Reproduction PASS iff the four E3 values are within 2% of PLD's printed 1.03·10⁻⁹⁴, 1.0·10⁻⁹⁴, 7.71·10⁻⁹⁵, 7.56·10⁻⁹⁵ (in the
  order PLD printed them; I will report which order matches). Report log10(g²_δ/DX′).
- U1-5 (margins, the "+63.6" family): g²_H := a/D with a = θa_bad and D ∈ {100 (RLARGE l.617's form), ln 12800 + 324 ln(4/3)
  (B_0 = 0), ln 12800 + 324 ln(4/3) + 38417 (B_0 = 1)} (ln C_fc and aR omitted, as REVIEW_RLARGE_V3 Part 4 does);
  θ ∈ {1/24 (route iii, supremum), 1/15000 (route iv), a_ret^{PLD}/a_bad (route ii fallback, N = 2, κ = 1, λ_min = 3.17·10⁻³)}.
  Report log10(g²_H/DX′) at C_Ω = 1. Reproduction PASS iff (θ = 1/24, D = 100) gives +63.619267 ± 10⁻⁶ (REVIEW55_ARS F04) and
  (θ = 1/24, B_0 = 1) gives g²_H within 1% of 2.70·10⁻⁹¹ and (B_0 = 0) within 1% of 1.01·10⁻⁸⁸ (REVIEW_RLARGE_V3 Part 4).
  Sign gate: PASS iff every margin in this gate and in U1-4 is > 0 (reported; a negative one would be a finding, not an error).
- U1-6 (route iii's a_A): κ_min := 256θc_pr/λ at θ = 1/24, λ = 1/2: PASS iff κ_min == 1/84270 exactly; and at κ = 1, λ = 1/2,
  θ = 1/24: a_A/a_bad = min{λκ/(256c_pr), 6θ} == 1/4 with the 6θ entry binding.
Controls (must behave as stated, else UNABLE TO DECIDE): K1 (U1-3 can FAIL): P = 10⁶² at λ_min = 3.17·10⁻³, ln C = 0 → FAILS;
K2 (B_0 matters): the B_0 = 0 and B_0 = 1 margins at θ = 1/24 differ by > 2 decades; K3 (U1-6 can flip): λ = 10⁻⁶ makes
λκ/(256c_pr) < 6θ at κ = 1, θ = 1/24 (first entry binds); K4 (log enclosure sanity): the enclosure of ln 10 contains
2.302585092994045684 and has width < 10⁻³⁰.
Written at (date -u, appended): 2026-10-29T00:38:05Z
