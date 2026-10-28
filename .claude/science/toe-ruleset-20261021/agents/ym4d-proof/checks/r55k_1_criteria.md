# r55k_1 — pre-registered criteria (REVIEW55_CONST, batch C5). Written BEFORE checks/r55k_1_const.py exists.

Reviewer model: claude-opus-5-5. Plain python3 -I, fractions.Fraction + integer isqrt only; logarithms, powers and
exponentials by rigorous rational interval arithmetic (atanh series / Taylor series with explicit tail bounds, outward
rounding). No floats decide anything. Every verdict is decided on an interval: a claim PASSES only if the whole
interval satisfies it, FAILS only if the whole interval violates it, otherwise UNDECIDED (reported as such).

Convention: "PASS" = the source's statement reproduces / holds; "FAIL" = the source's statement is refuted by the
interval. Inputs are the rounded constants the sources print (transcribed with file:line in the script); a PASS does
not certify those inputs.

## A. CONST_T
- A1  ϑ = 4/q ≤ 1/2 at q = 5, 6, 7 (exact). CONST_T l.307-308 "all hold for every q > 4": PASS iff ϑ ≤ 1/2 at all three.
- A2  c_ϑ := (1−ϑ)(2ϑ)^{ϑ/(1−ϑ)} (CONST_T §2.4(e), λ = 1/(2ϑ)) at q = 5: PASS ("c_ϑ ≤ 1 for every q > 4") iff upper
      end ≤ 1; FAIL iff lower end > 1. Report a rigorous bracket for the q at which c_ϑ = 1.
- A3  c′_ϑ := (1−ϑ)(4ϑ)^{ϑ/(1−ϑ)} (the quarter-split needed when TWO potentials are absorbed) ≤ 1 at q ∈ {8, 9, 10,
      12, 16, 32, 100, 1000}: PASS iff every upper end ≤ 1. (A proof for all ϑ ≤ 1/2 is given in the review text.)
- A4  "q = 8 is the worst admissible choice" (CONST_T l.505, l.551) with admissible = q > 4 (CONST_T l.272): PASS iff the
      file's own dominant term ½(36·C_1C_V·486)^{q/(q−4)} at C_1C_V = 2000 is ≤ its q = 8 value at q = 5 and q = 6.
- A5  B(4), B(8) (β-telescope) — PASS iff enclosures lie within 0.05 % of 43.95 and 1931.5.
- A6  q = 8 floor: √6·175.8·B(8)·½(36·486)² — PASS iff the enclosure rounds to 1.27·10¹⁴ (i.e. ⊂ [1.265, 1.275)·10¹⁴).

## B. STAR_CONST
- B1  c_s = 8(9/T+2)/(7/8 − T), T = (√387 − 18)/4: PASS iff ⊂ [411.92, 411.93]. c_g = 8·310/(7/8 − T) + 272: PASS iff
      ⊂ [5699.63, 5699.64]. Floor (δ_2 = ρ = 0): PASS iff ⊂ [319.19, 319.21].
- B2  §8.3 C_T (R_0 = 32, F = 175.8, B(8), |𝒩_S| = 3, A_cγ_c = 1, cut = 288(c_g + 18·3·c_s·R_0^{−2+8/q})):
      q = 11 PASS iff ⊂ [9.75, 9.85)·10¹²; q = 12 PASS iff ⊂ [5.25, 5.35)·10¹²; q = 100 PASS iff ⊂ [1.35, 1.45)·10¹².
- B3  236.9·c_g vs EPSSTAR's "1.348·10⁶": PASS iff ⊂ [1.3475, 1.3485)·10⁶. c_g/20 vs "×287": PASS iff ⊂ [286.5, 287.5).
      Report 236.9·c_g/4700 and 236.9·c_g/4738.

## C. EPSSTAR
- C1  |N_3|^{3/4} vs EPSSTAR's 1314.21: PASS iff ⊂ [1314.205, 1314.215). |N_3|^{1/4}/|N_1|^{3/4} vs 0.105889: PASS iff
      ⊂ [0.1058885, 0.1058895). ES-1's needed inequality |N_3|^{1/4}/(9|N_1|^{3/4}) ≤ 1/9: PASS iff true (exact).
- C2  C_{S1}(12, 1) vs 6963.995: PASS iff ⊂ [6963.99, 6964.00]. (1+√6)C_{S1}(12,m)/m at m = 1, 7, 19615 vs 2.402·10⁴,
      2.871·10³, 0.99996: PASS iff each rounds to the printed figure.
- C3  C_T(12) (R_0 = 64, F = 175.8, B(8), |𝒩_S| = 3, m = 19615, cut = 288[c_g + 18(3c_sR_0^{−2+8/q} + 1/(36m))]):
      PASS iff ⊂ [5.2883475, 5.2883485)·10¹².
- C4  l.525: t_need := 2·6.7·10⁻⁴⁰·√(5.05·10⁹). PASS (l.525's 3.01·10⁻³⁵ is right) iff 3.01·10⁻³⁵ ∈ [0.995, 1.005]·t_need.
      "exactly √10": PASS iff √10 ∈ the enclosure of t_need/(3.01·10⁻³⁵). Slip explanation: PASS iff t_need/√10 rounds
      to 3.01·10⁻³⁵.
- C5  C_D ceiling (3.31·10⁷·t_need)^{−1/2}: PASS (l.525's 3.17·10¹³) iff ⊂ [3.165, 3.175)·10¹³.
- C6  "C_T ≥ 4.4·10¹² floor" (l.608): (i) C_T(12) at c_s = 319.198 with c_g held at 5699.63: PASS iff ⊂ [4.35, 4.45)·10¹².
      (ii) Whether ANY admissible allocation found in D below gives C_T(12) < 4.4·10¹²: if yes, the floor is FAIL.

## D. F / Stage-1 radius consistency (new)
- D1  CONST_T's rule (i_* = max steps with smallest gap ≥ 12; gaps ∝ 2^{−i}), budget R/2 − 4, R ≥ 32: PASS iff the
      maximum over R of F ⊂ [175.75, 175.85] attained at R = 79 (block-endpoint scan; log F is decreasing-then-
      increasing inside each block, so block endpoints suffice — proved in the review text).
- D2  Same rule, budget R/4 − 3 (Stage 2 confined to B_{3R/4−3}, EPSSTAR §3.1's own Stage-1 radii), R ≥ 64.
      PASS ("F = 175.8 is consistent with EPSSTAR's Stage 1") iff max F ≤ 175.8.
- D3  Budget R(1/2 − 1/c) − 3, R ≥ 16c (Stage-1 gap R/c − 4 ≥ 12), c ∈ {8, 16, 32, 64, 128}: REPORTED (max F, R).
- D4  C_T(12) with D2's F (all else as C3): PASS ("C_T(12) ≤ 10¹³ under EPSSTAR's own radii") iff upper end ≤ 10¹³.
      C_T(12) with D3's F and the m that keeps A_cγ_c ≤ 1: REPORTED.

## E. TAUFLAT
- E1  √(1/(3.31·10⁷·53·2.75·10⁻¹⁵)): PASS iff ⊂ [455.2833, 455.2834].
- E2  At C_D = 900·5.288·10¹²: log10(η_A/η_B) PASS iff rounds to 52.077; energy shortfall log10(4ε_1²/η_B) PASS iff
      rounds to 9.707; required t_pr PASS iff rounds to 9.5224·10⁻³⁵ (with 640·53⁴ in place of 5.05·10⁹).
- E3  log10(5.288/4.4) PASS iff rounds to 0.080; log10(5.288/1.396) PASS iff rounds to 0.578.
- E4  Option A under P-max: rigorous lower bound C_T ≥ √6·F_min·B(8)·Ĉ_min over every δ-allocation, every q ≥ 8 and
      every R_0 ≥ 64 (F_min, Ĉ_min derived in the review text) against the most lenient DESC-ε need
      C_T ≤ (C_D,max/2 − 46.8)/(1.011·c_N·Λ(∞)), c_N = 1. PASS ("option A dead") iff lower bound > need.

## F. EPS1_SWEEP / EPS1_EXEC
- F1  a_RS(6.7·10⁻⁴⁰) = ε⁴/(4·9216²) (N = 2, A_d = 9; RLARGE l.64, l.1020, l.1026): PASS iff rounds to 5.93136·10⁻¹⁶⁶.
      Margin log10(a_RS/100) − log10(2.456·10⁻¹⁵²): PASS iff rounds to −15.62 (−15.617). REPORT at 9.52, 8.95·10⁻⁴⁰
      and 1.27·10⁻³⁹.
- F2  2×2 cross-ratio (1.2687·10⁻³⁹·6.7·10⁻⁴⁰)/(8.95·10⁻⁴⁰·9.52·10⁻⁴⁰): PASS ("exactly factorising") iff = 1 exactly.
      PASS ("factorising within printed precision") iff 1 lies in the range the cross-ratio can take when each entry
      varies over its rounding interval.
- F3  g/ε_1 at fixed g, proposed vs current ε_1: PASS (EPS1_SWEEP "shrinks as ε_1 falls") iff the ratio < 1.
- F4  √(3.52309230578·10⁻⁸⁸/4) vs 9.38495112638·10⁻⁴⁵: PASS (value admissible) iff value ≤ bound. Relative excess:
      PASS (EPS1_EXEC's 2.34·10⁻¹³) iff rounds to 2.34·10⁻¹³ (2.3406·10⁻¹³ to 5 s.f.).
- F5  Δ := log10(6.7·10⁻⁴⁰/9.38495112638·10⁻⁴⁵): PASS iff rounds to 4.853643; 2Δ, 3Δ, 4Δ round to 9.707, 14.561, 19.415.
- F6  EPS1_EXEC q = 8 row: C_T(8) in its own convention (as C3, q = 8) PASS (equals the 1.27·10¹⁴ used) iff
      ⊂ [1.26, 1.28]·10¹⁴. Report 2log10(C_T(12)/C_T(8)) in both.
- F7  η_♭ from TAUFLAT's chain C_D = 900·5.288·10¹² vs EPS1_SWEEP's 3.52309230578·10⁻⁸⁸: PASS iff equal to 12 s.f.

## G. QFIX
- G1  Λ(q) := 4·2^{2+4/q}(4.94 + 3.34·32^{1/q}): PASS iff Λ(8), Λ(12), Λ(∞) round to 228.333, 189.459, 132.48.
- G2  C_D(q) = 2(1.011·2·Λ(q)·C_T(q) + 46.8): C_D(11)/6.7·10¹⁵ PASS ("×1.16") iff rounds to 1.16 and > 1;
      C_D(12) ≤ 6.7·10¹⁵ PASS iff true. "q = 12 is the lowest admissible q": FAIL if C_D(11.5) ≤ 6.7·10¹⁵.
- G3  lever obj(∞) − obj(8), obj := 4·log10(ε_1^cut) + const, ε_1^cut = t_pr/(2√(5.05·10⁹)), t_pr = 1/(3.31·10⁷C_D²):
      PASS iff rounds to 24.089.
- G4  ε_1^cut(1000): PASS iff rounds to 3.8235·10⁻⁴³ (to 5 s.f.). QFIX "3.8·10⁻⁴³" admissible: PASS iff ≤ ε_1^cut(1000).
      QFIX "3.5·10⁻⁴³ at q = 100": PASS iff ≤ ε_1^cut(100).
- G5  With θ_ε = 1.12·10⁻³⁷/(16·3.34·32^{1/q}) also in the min: cutoff(1000) PASS (Codex's 1.4695·10⁻⁴⁴) iff rounds to
      it; ε_* needed to keep t_pr = θ_0^SUP at q = 1000: PASS (Codex's 2.9141·10⁻³⁶) iff rounds to it.
- G6  A_cγ_c bound's q-derivative sign change at q = 16·27·c_s = 432c_s: PASS (QFIX "row 4 wants q large for all q")
      iff no sign change (analytic; derivative formula in the review text). Report the bound at q = 10⁵, 10⁶, 10⁷.
- G7  θ_G(q) = 1.168·10⁻¹²/q crosses θ_0^SUP(∞) at q = 1.168·10⁻¹²·3.31·10⁷·C_D(∞)²: REPORT; QFIX's 5.573·10²⁶ is
      θ_G = θ_ε(∞) at ε_* = 1.12·10⁻³⁷: PASS iff that reproduces.
- G8  "argmax q = 1000": PASS iff obj(1000) ≥ obj(q) for every q in QFIX's grid {8,…,10⁶}.

## Designed-FAIL controls (each must flip, or the item is reported as having NO POWER)
- CTRL-1 A2 at q = 8 (must return ≤ 1). CTRL-2 F4 with the value 9.38495112637·10⁻⁴⁵ (must PASS). CTRL-3 B2 with
  c_g replaced by 20 (must change the q = 12 value by > 1 %). CTRL-4 D1 with budget R/2 − 4 must reproduce 175.8 while
  D2 uses the same code — so D1 is the control for D2. CTRL-5 G8 restricted to q ≤ 1000 (must PASS).
