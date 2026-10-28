# kf55_1 — criteria (pre-registered; written 2026-10-28T23:19Z UTC, BEFORE checks/kf55_1.py exists)

Owner: KFACTOR_O55.md (Opus 5.5 worker, step 4 / T56-4). Exact arithmetic only: Python `fractions.Fraction` and ints,
no floats in any verdict, no numpy/BLAS. Logarithm and e by rigorous rational enclosures (partial sums + explicit tail
bounds). Single thread.

## What is being checked, and what it can and cannot decide
- Part A checks two numbers of REVIEW_BFT_B_S9_S10 S10-6 that changed decisions (HANDOFF item 5): the "≈ 25(k−1)" and
  whether its optimising θ is admissible in Theorem COF's window 0 < α < θ < 1 at lane A's α = 1/4.
- Part B checks ONLY the algebra of my Lemma TR (KFACTOR_O55 §4): from the transport inequality (TR-1) to the row bound
  (TR-2), the class-norm bound (TR-3) and the level-sum bound (TR-4). It CANNOT test (TR-1)'s inputs (Lemma RT-cc (c),
  Lemma TC, Lemma FT, the a-priori slot sizes); those are source lemmas re-derived in the text, not numerically. It can
  fail on an exponent/units slip in (★)/(TR-2) (B1) or on a wrong closed-form constant (B2). B3 is a control that must
  fire. Inputs are free positive rationals (the source's constants are crude/uncomputed), so the check is about
  structure, not about the size of any physical constant.

## Part A (S10-6 numbers)
- **A1.** C_f := 1 + 2d/(1 − L^{−3}) at d = 4, L = 3 equals 121/13 exactly; and C_f·e lies in [25.30, 25.31] with e
  enclosed rigorously. PASS iff both. (Expectation: PASS.)
- **A2.** With α = 1/4, L = 3, θ*(k) := 1/((k−1)·ln 3): θ*(k) > α for k ∈ {2, 3, 4} and θ*(k) < α for every
  k ∈ [5, 10000], decided with a rigorous rational enclosure of ln 3 (no k may be undecided). PASS iff exactly this
  pattern. (Expectation: PASS. FAIL refutes my claim that S10-6's optimum leaves COF's window for k ≥ 5.)

## Part B (Lemma TR bookkeeping), exact
Parameters (all combinations): L = 3; κ_- = 1; κ_+ ∈ {1, 2, 4} (so κ̂ = κ_+); η ∈ {1/10, 1/100, 1/1000};
A_s ∈ {1, 10, 100}; A_j ∈ {1, 10, 100}; c_B := 1; θ with L^θ ∈ {4/3, 2, 5/2} (θ ≈ 0.262, 0.631, 0.834, all in
(1/4, 1)). Write A_B := c_Bκ_+L² (the a-priori per-level row bound is A_Bη²).
- **B1 (TR-1 ⇒ TR-2 algebra).** For every m ∈ [0, 400]: T_m := κ_-^{−1}[L^{−2m}A_sη² + L^{−2m}(κ_+η + A_sη² + mA_jη²)]
  and P_m := c_Bκ_+L^{m+2}η·T_m. PASS iff P_m == A_Bη²·κ̂·L^{−m}·[1 + (2A_s + mA_j)η/κ_+] (Fraction equality) for all m
  and all combinations.
- **B2 (k-uniformity).** a_m := min{1, κ̂L^{−m}[1 + (2A_s + mA_j)η/κ_+]} (per-level row bound in units of A_Bη²). For
  every k ∈ [2, 400]: N_k := max_{1≤l≤k−1}(L^θ)^{k−l}·a_{k−1−l} and S_k := Σ_{l=1}^{k−1}a_{k−1−l}. Closed forms:
  M := max_{m≥0} m·(L^θ/L)^m (exact max over m ∈ [0, 3000], with a check that the sequence is decreasing on its last
  half so the max is attained inside the range); B_Pc := L^θ·κ̂·[1 + 2A_sη/κ_+ + (A_jη/κ_+)·M];
  B_S := κ̂·[(L/(L−1))(1 + 2A_sη/κ_+) + (L/(L−1)²)(A_jη/κ_+)]. PASS iff N_k ≤ B_Pc and S_k ≤ B_S for all k, all
  combinations.
- **B3 (control; must fire).** Old bounds a^old_m ≡ 1: N^old_k = (L^θ)^{k−1}, S^old_k = k − 1. PASS iff at k = 400,
  N^old_k ≥ 10·N_k and S^old_k ≥ 10·S_k for every combination. (If the control does not fire, B2 is uninformative and
  the whole of Part B is reported as FAILED-CONTROL.)
- **B4 (no claim at the top level).** PASS iff a_0 = 1 for every combination (Lemma TR gives no gain at l = k − 1).

## Verdict rule
Overall PASS iff A1, A2, B1, B2, B3, B4 all PASS. Any FAIL is reported verbatim in KFACTOR_O55.md with its consequence;
no criterion may be edited after the script exists (amendments, if any, are appended below with a timestamp and do not
change these lines).
