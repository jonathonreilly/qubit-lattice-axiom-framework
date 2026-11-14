# r55h_arith — criteria (written BEFORE checks/r55h_arith.py exists). Reviewer: claude-opus-5-5 (REVIEW55_HWPLD).

Exact rational arithmetic (fractions.Fraction) for every verdict. Logarithms only as RIGOROUS rational enclosures
(atanh series with an explicit geometric tail bound). No floats in any comparison; floats only in printed summaries.
Every input constant is quoted from a file written before this review (source named). Nothing derived in this review
appears in a PASS/FAIL threshold; where a value is unknown in advance the item is a RECORD, not a criterion.

Inputs (all quoted): a = 1.0e-86 (HW §30.6 "a = θa_bad ≲ 1.0·10⁻⁸⁶", the value w5/w6/REVIEW_HW_S5 compute at);
beta_- = 0.186; L = 3; C_l = 1; R = 0; c_A = 0; c_U = 1 (HW §35.7 "At c_A = 0, c_U = 1, C_ℓ = 1, R = 0");
formulas HW §35.7: b_n = C_sh·81·h_n·c_+ + h'_n·c_U, b_D = h_D·(C_sh·81·c_+ + c_U), c_f = C_sh·81·c_+,
(C_sh,h_n,h'_n,h_D) = (6561,38418,38417,38416) [s5] / (81,10002,10001,10000) [s6];
g2CRC = a/(b_n + aR + ln(12800·C_l)) (HW l.1639); n_T = b_D/(a·beta_-·ln L) (HW l.1552, (T));
REL-boot: r ≤ 1/2 ⟺ g² ≤ a/(h·B_* + aR + ln(12800 C_l)), B_* = c_f + 1 (HW l.1195); HIST-sum: g² ≤ a/(h·B_0 + ln(12800 C_l)),
B_0 = c_f + 2 (HIST l.551, HW §35.7 (ii)); n_H = floor((4 + c_B)/(a beta_-)), c_B = h_D'·B_0/ln L (HIST l.550), with
(h, h_D') = (38417, 38416) [HIST as written] or (10001, 10000) [Corollary H-geo′];
(S1): g² ≤ a_A/(c_+·c_att + ln(2·Δ_ρ²)), Δ_ρ = 17⁴ − 1, c_att(8) = 320001 [s6] (HW §30.4, §35.7); a_ret = 2.0e-91 (HW §30.6).

## A1 (PRE-REGISTERED reproduction of HW §35.7's table, HW.md l.2003-2007): for the five rows
(s5,c_+=1), (s5,82), (s6,1), (s6,17), (s6,82): b_n, b_D, c_f equal the printed integers exactly, and the rigorous
enclosures of g2CRC and n_T round to the printed 6-significant-figure values. PASS iff all 25 entries agree.
## A2 (PRE-REGISTERED reproduction of REVIEW_HW_S5 S5-12 and HW §35.1/§38 item 1): at s5, c_+ = 1:
(S2) 4.89789e-97 [review] / 4.897894e-97 [HW]; REL-boot 4.89802e-97 / 4.898021e-97; HIST-sum 4.898e-97 / 4.898012e-97;
n_T 9.99104e96 / 9.991038e96; n_H 9.99102e96 [review, "B_0 = 531441c_+"] / 9.991019e96 [HW]. PASS iff each printed value
is the correct rounding of the enclosure at its printed precision; for n_H, record which B_0 (c_f, c_f + 2) reproduces each.
## A3 (PRE-REGISTERED reproduction of decision ratios): s5 slack vs 2.5e-152: "1.96e55" (S5-13), "1.9592e55" (w6 A5);
s6 ×17 slack "3.5855e56" and break-even "c_+ ≤ 6.0954e57" (HW §35.7 (iii)); ratios to 1e-94: 204.17, 11.16, 53.81, 1.52
(HW §35.7 (i)); 311.1 / 311.2 (HW §35.7); (S1) ceiling 1.83822e-93 and g²_ret 3.67644e-98 at the ×17 ring (HW §35.7);
REL-boot at ×17 with 38417: 2.33375e-96 and breach ×42.85; n_H at ×17 with 38416: 2.09688e96 and ×3.84 over n_T;
w6 A2 spreads 3.8415 (HIST as written) and 1.0001 (H-geo′). PASS iff every printed figure is the correct rounding.
## A4 (RECORD, no pass/fail): the HW-route binding ceiling min{(S2), REL-boot, HIST-sum} at c_+ ∈ {1, 17, 82}, with
HIST as written and with H-geo′; and its slack against 2.5e-152.
## A5 (PRE-REGISTERED): PLD.md l.1097: least m ≥ 0 with (L²/(2C_I))^m·η_1 ≥ 2·C_I·ε_1/L², L = 3, C_I ∈ {1, 3/2, 2}.
(i) η_1 = c_1ε_1, c_1 = 1/117 (PLD l.1096): PLD's (3,4,5) CONFIRMED iff the exact least m are (3,4,5).
(ii) η_1 = RLARGE l.64's min{ε_1/(2L²), ε_1²/(512·N·A_d)}, A_d = 9 (RLARGE l.973), N = 2, ε_1 = 67/10^41 (RLARGE l.72):
SYMBOLS.md §2.4's (66,90,122) CONFIRMED iff the exact least m are (66,90,122).
(iii) control: (ii) at ε_1 = 2 — REVIEW_PLD_S3 l.435's recorded (5,7,10) CONFIRMED iff reproduced.
## A6 (PRE-REGISTERED): HW l.604: B(θ) = (1/640)·(θ/53)² at θ = 10⁻⁸ (HW l.183/604) and θ = 3·10⁻⁸ (SQ l.216).
SYMBOLS §4.4's "5.00623·10⁻²²" CONFIRMED iff B(3e-8) rounds to it at 6 s.f.; ratio B(3e-8)/B(1e-8) and B(3e-8)/(5e-23)
recorded. Also SQ l.216's "≈ 3·10⁻²³ (C_D = 2)" checked as B(3e-8)/16 (record).
## A7 (PRE-REGISTERED reproduction + RECORD): PLD §18.10 B3: the factor (b_n + ln 12800 + 10⁹)/(b_n + ln 12800) at the
s5 b_n = 20416938755 is "1.0490" — PASS iff it rounds to 1.0490. RECORD the same factor at the s6 b_n of the no-ring,
×17 and ×82 rows, and the analogous factor for (S1)'s denominator (c_+·c_att + ln(2Δ_ρ²)) at c_+ ∈ {1, 17, 82}.
## A8 (PRE-REGISTERED reproduction + RECORD): PLD §18.7.2 (α)/(β): u·ε_1² = ε_1²/g_K² at g_K² = 10⁻⁹⁴, ε_1 = 6.7·10⁻⁴⁰:
"4.489·10¹⁵" PASS iff it rounds to 4.489e15. RECORD the same quantity at g_K² = 2.5·10⁻¹⁵² and at g_K² = the A4 ×82 value.

## Scope
Arithmetic about constants recorded in earlier sessions. Nothing here is evidence about any measure or open statement.
