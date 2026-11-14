# fl55_1 criteria — the leading-coefficient chain, exact arithmetic (written before any fl55_1 script)

Owner: FLOW55.md (worker claude-opus-5-5). Script: checks/fl55_1.py (to be written AFTER this file). Plain python 3,
`fractions.Fraction` and `sympy` exact rationals / sqrt(3) only; no numpy, no floats in any verdict. nice 10. Output:
checks/fl55_1_out.txt (stdout), checks/fl55_1_err.txt (stderr). No constant below was derived in this session: 11, 12, 1,
1/12, 1/22, 21/22, −20, 1/24, 1/4, 1/8, 1/(24π²), 1/(48π²), 2N·2b_0 = 11N²/(12π²) are the values of PROOF L4b (a_2
decomposition), FLOW §0/§15 (Lemma F-norm), FLOW §5.7 (scalar channel), FLOW §74 (FINE-IR) and FLOW §88 (C_{K_F} = −20c_g).

## Part A — the Feynman-form ratio from the a_2 coefficients (G = SU(2) and SU(3))
Definitions. Hermitian generators T^a (Pauli/2 for SU(2); Gell-Mann/2 for SU(3)), tr(T^aT^b) = δ_ab/2, structure constants
f_abc := −2i tr([T^a, T^b]T^c) (exact; SU(3) entries in Q(√3)). Real antisymmetric adjoint matrices (ad_a)_{cb} := f_{abc}.
A fixed pseudo-random rational field F^a_μν (μ, ν ∈ {1..4}, F^a_νμ = −F^a_μν, numerators in [−9, 9], denominators in
[1, 7], seeded by the integer 5501). Ω_μν := Σ_a F^a_μν ad_a. Vector bundle = Lorentz ⊗ adjoint; curvature
Ω^vec_μν := 1_4 ⊗ Ω_μν; spin endomorphism E^vec with Lorentz blocks (E^vec)_{(μ),(ν)} := s·Ω_μν, s = 2 (the BF spin
coupling). S := Σ_{a,μ,ν}(F^a_μν)² (ordered pairs).
  X_vec := (1/12)Σ_{μν}tr(Ω^vec_μνΩ^vec_μν) + ½tr((E^vec)²),   X_gh := (1/12)Σ_{μν}tr(Ω_μνΩ_μν).
Verdict lines:
- **A0 (normalisation).** Σ_{c,d}f_acd f_bcd = N δ_ab exactly (N = 2, 3). PASS iff exact equality for all a, b.
- **A1 (the 11).** (½X_vec − X_gh)/(−X_gh) = 11 exactly, for SU(2) and SU(3). PASS iff both equal 11.
- **A2 (dia/para split).** D := (½·(1/12)Σtr(Ω^vecΩ^vec) − X_gh)/(−X_gh) and P := ½·½tr((E^vec)²)/(−X_gh) satisfy
  D = −1 and P = 12 exactly (so 11 = 12 − 1, i.e. 11/3 = 4 − 1/3). PASS iff both, both groups.
- **A3 (C_A).** X_gh = −(N/12)·S exactly. PASS iff both groups.
- **A-c (designed FAIL control).** With s = 1 instead of 2, the ratio of A1 is NOT 11. The control line must print
  "control fires" (ratio ≠ 11). If it does not fire, Part A is INVALID (cannot fail).

## Part B — normalisation conversions (symbolic in N, π)
- **B1.** For the explicit hermitian traceless rational matrices X_2 = [[1, 2−i],[2+i, −1]] (N = 2) and
  X_3 = diag(1, 2, −3) + (offdiag: X_12 = 1+i, X_21 = 1−i, X_23 = 2, X_32 = 2) (N = 3), the t² coefficient of
  1 − N^{-1}Re tr exp(itX) (sympy series in t to order 5) equals tr(X²)/(2N) and the t³ coefficient is 0. PASS iff exact.
- **B2.** 2N·2b_0 with b_0 = 11N/(48π²) simplifies to 11N²/(12π²). PASS iff sympy simplify gives 0 difference.
- **B3.** 2·(1/(48π²))/(11/(12π²)) = 1/22; (1/22)·11N²/(12π²) = N²/(24π²); and from C_{K_F} = −20 (units c_g):
  ½(−20) − 1 = −11, ½(−20) − ½ = −21/2, (−21/2)/(−11) = 21/22. PASS iff all exact.
- **B-c (designed FAIL control).** The wrong conversion 2N·b_0 (FLOW's FN-1 error) does NOT equal 11N²/(12π²). Must fire.

## Part C — S³ averages and the scalar Ω² channel coefficient
- **C1.** With the Gaussian-moment method (x ∈ R⁴ standard normal: E[x_1²x_2²] = 1, E[x_1⁴] = 3, E[x_1²] = 1,
  E|x|⁴ = d(d+2) = 24, E|x|² = 4, and E[x^α] = ⟨n^α⟩_{S³}E|x|^{|α|}): ⟨n_1²n_2²⟩ = 1/24, ⟨n_1⁴⟩ = 1/8, ⟨n_1²⟩ = 1/4. PASS iff
  exact. (The moments E[...] are computed exactly by sympy integration of polynomials against the Gaussian.)
- **C2.** Angular average of q⁴·[−32q_1²q_2²/q⁸ + 4q_1²/q⁶ + 4q_2²/q⁶ − 1/q⁴] equals −1/3; times (2π²)/(2π)⁴ = 1/(8π²) gives
  −1/(24π²); hence β = 1/(24π²) per log(1/m) and c_Γ = β/2 = 1/(48π²) = 2c_g with c_g = 1/(96π²); and (2π²/24)(2π)^{-4} =
  1/(192π²), 4/(192π²) = 1/(48π²) (FLOW §74 (iii)). PASS iff all exact.
- **C-c (designed FAIL control).** Using ⟨n_1²n_2²⟩ = 1/16 (the product-of-marginals error) the C2 total is NOT −1/3. Must
  fire.

## Overall
PASS iff every verdict line above PASSes and every control fires. A control that does not fire makes its Part INVALID
(reported as such, not as PASS). Run once; output kept unaltered; any re-run under a new id with these criteria untouched.
