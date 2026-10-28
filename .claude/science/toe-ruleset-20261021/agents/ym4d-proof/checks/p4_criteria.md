# p4 criteria (lane E, session 4; written 2026-10-28 ≈10:31 UTC, AFTER the §16.1-§16.9 derivations in PLD.md and BEFORE
checks/p4_pld.py exists)

Order disclosure: the statements tested were derived first (PLD.md §16); these criteria are fixed before any script is written
or run. No criterion is edited after the run; any change is disclosed in p4_time.txt.
Scope: elementary statements and arithmetic of session 4 only. Nothing here tests (LI^U), (SF-cap), (LCR), (J-NS), (SC)_k or any
lattice measure. "Rigorous" = exact or quadrature with stated tolerance; "evidential" = sampled.

## A. Lemma KD (SU(2))
- A1 (quadrature, mpmath 30 digits) For the kernel angle law ν_b(dw) ∝ e^{-bw}√(w(2 - w))dw on [0, 2] (w = 1 - cos α; KS (a)),
  exact tail T(b, s) := ν_b(w ≥ s) vs the bound B(b, s, λ) := (1 - λ)^{-3/2}e^{-λbs}, on b ∈ {1, 10, 100, 10³, 10⁴},
  s ∈ {0.01, 0.1, 0.5, 1, 1.5}, λ ∈ {0.25, 0.5, 0.75, 0.9}. PASS iff B ≥ T(1 - 1e-20) at every grid point.
- A1n (negative control; must FAIL the inequality somewhere, else FAIL): e^{-λbs} (no prefactor) < T somewhere on the grid.
- A2 (sampled, 20000 Haar SU(2) V, M = rŴ with Ŵ Haar and r ∈ (0, 1]) φ_M(V) := r - ½Re tr(V^{-1}M) equals r||V - Ŵ||²_op/2 to 1e-12,
  and M = mean of 1-12 Haar SU(2) elements satisfies M^†M = ||M||²·1 to 1e-12 (real combinations of SU(2) are r·SU(2)).
- A3 (sampled, 20000 quadruples, half near 1, half Haar) ||1 - V_1V_2V_3^{-1}V_4^{-1}|| ≤ ||1 - W_1W_2W_3^{-1}W_4^{-1}|| +
  Σ||V_i - W_i|| + 1e-12.

## B. Lemma DIL-1
- B1 (sampled, 20000 pairs) SU(2): with M = mean of n Haar or near-1 elements and M° a perturbation of the same family,
  ||M/r - M°/r°||_op ≤ 2||M - M°||_op/r° + 1e-12 whenever r° > 1e-6.
- B1n (negative control; must FAIL somewhere): the same with factor 1 in place of 2 fails for some pair (explicit pair
  r° = 1, r = ½, opposite directions included).
- B2 (sampled, 2000 random contour families) for n_c contours, each a product of ℓ links from a pool, and U, U° differing on a link
  set E with ||U_e - U°_e|| ≤ δ: ||mean T(U) - mean T(U°)|| ≤ f·ℓ_E·δ + 1e-12, f the fraction of contours meeting E, ℓ_E the max number
  of E-links on one contour.

## C. Proposition CC (a), illustrative toy (one plaquette, 4 links, SU(2), no C(Q) factors)
Kernel centres x^0 with ||1 - V^0_P|| = ε_1 - δ/8, ε_1 = 0.02, κ = 1, g = 1e-3 (b = 1e6 per link, r = 1), δ = g; 10⁵ samples of the
4 links from the kernel (angle law ν_b, uniform axis).
- C1 PASS iff the sampled P(||1 - V_P|| ≥ ε_1) ≥ 0.05 (the frozen activity is O(1), not e^{-a/g²}).
- C2 PASS iff it exceeds the proven lower bound Haar_δ/16^4·e^{-4bδ²/2}... (the toy form of §16.8 (a): (m_{δ/16})^4·e^{-2κu δ²}, m_r := Haar
  measure of the op-ball of radius r in SU(2), computed exactly by quadrature).
- C1n (negative control, must hold): with the centre at ε_1/2 (10 standard deviations below), the sampled frequency is < 1e-3.

## D. Proposition WALL arithmetic and shadow geometry
- D1 The scalar recursion C(k) = max{C_0, 243ηe^{aR}C(k-1)}, C(0) = C_0 = 1, k ≤ 400, a = 1e-86, R = 10: PASS iff C(400) ≤ C_0 for
  η ∈ {1/243, 0.5/243} and C(400) ≥ 10^{100} for η ∈ {1, 1/81} (the LOOP-const side).
- D2 (exact, sets in Z⁴) shadows Σ(A) = N_1(π(A)), L = 3, for a cube Q, for x under Q (all 81 choices), and for an adjacent pair
  S = {Q_1, Q_2}, levels m = 1..10:
  - D2a sh_m(x) ⊇ sh_m(Q) for every x, m (monotonicity used in §16.6 (b));
  - D2b the excess Σ_{m=1}^{10}(|sh_m(x)| - |sh_m(Q)|) + 81 ≤ Δ_sh = 3073361;
  - D2c (evidential) |sh_m(S)| ≤ |sh_m(Q_1)| + |sh_m(Q_2)| for all m, and |sh_m(S)|/max_i|sh_m(Q_i)| ≤ 2 (deep shadows overlap; printed).
  - D2d each |sh_m(·)| ≤ 2401(16 + 32(n - 1)3^{-m}) (Lemma H-geo (iii)).

## E. Arithmetic of §16.5, §16.8 (mpmath 40 digits)
- E1 c_pr = 1/(640·53²) = 5.5625·10⁻⁷ (to 1e-10 relative); κ_min := 256c_pr/(24·½) = 1.1867·10⁻⁵ (< 1.2·10⁻⁵).
- E2 N = 2, L = 3, A_d = 9: η_q = ε_1/4608 (ε_1/(256NA_d) < ε_1/(2L²)); σ_fl² = 16/λ_min for λ_min ∈ {3.17·10⁻³, 4.23·10⁻³};
  a_fl := 49η_q²/(1024σ_fl²), a_J := ε_1²/4096 (κ = 1), a_KN := (35/256)²ε_1²/128; a_ret := min. PASS iff a_ret = a_fl and
  a_ret/(c_prε_1²) is within 1% of 8.0·10⁻⁷ at λ_min = 3.17·10⁻³, and a_fl/ε_1² within 1% of 4.47·10⁻¹³.
- E3 at ε_1 = 6.7·10⁻⁴⁰: a_ret printed; the coupling ceiling g² solving a_ret/g² = (12 + p)ln(1/g) + ln C, p ∈ {6, 12},
  ln C ∈ {0, 50}, printed; PASS iff every solution lies in [10⁻⁹⁶, 10⁻⁹³] (the "≈ 10⁻⁹⁴" of §16.8).
- E4 Δ_sh = 81 + 2401·32·80·Σ_{m≥1}3^{-m} = 3073361 exactly.
- E5 a_A/a_bad with λ = ½, κ = 1, θ ↑ 1/24: min{ε_1²/512, 6θc_prε_1²}/(c_prε_1²) → 0.25 (printed; PASS iff the min is the 6θ entry).
