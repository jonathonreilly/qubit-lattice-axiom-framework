# ru55_4 — criteria (written BEFORE checks/ru55_4_fi1.py exists; `date -u` appended)

Question: RLARGE_U55 §3 (FI-1). (a) Does the invariance of the one-step window X_k := [u_k − (3/2)β_0'log L − R, u_k + R] under
Φ_k(x) = u_k − b_k − ρ_k(x) hold at its extremes, and is the new γ condition tight for the lower end? (b) Is the Lipschitz
hypothesis (A-Lip) load-bearing for (SF-cont) of the A5 sequence, i.e. can a continuous family with |ρ| ≤ ε and slope > 1 make
the smallest-fixed-point selection jump? These are checks of the algebra and an explicit counterexample, not of node A.
Exact Fractions; no floats in verdicts. Write ℓ := β_0'log L (a positive number), C := C_ρ.

Gates (pre-registered):
- F1 (upper end): over a grid of rational (ℓ, R, Cγ²) with 0 < Cγ² ≤ ℓ/2, R ≥ 0, and the extremes b ∈ {ℓ − R, ℓ + R},
  ρ ∈ {−Cγ², +Cγ²}: max_{b,ρ}(−b − ρ) ≤ R − ℓ/2 (so Φ_k ≤ u_k + R − ℓ/2 < u_k + R). PASS iff true at every grid point.
- F2 (lower end, tightness): with x_lo := max{2R, 2/min{1, κ}} and u_k := γ^{-2} := x_lo + R + (3/2)ℓ (the γ condition at
  equality): min_{b,ρ} Φ_k = u_k − (ℓ + R) − ℓ/2 == x_lo exactly. PASS iff equality at every grid point (κ ∈ {1, 1/4, 4}).
  Control F2-C (designed FAIL): with u_k := γ^{-2} − 1 the minimum is < x_lo.
- F3 (window inside Option A's bracket): at u_k = γ^{-2} as in F2, the left end of X_k equals x_lo (PASS iff equal) and every
  larger u_k only moves it up.
- F4 (A-Lip is load-bearing): family y ↦ y − h(y) = s with h(y) := 2y on |y| ≤ a, 2a·sign(y) beyond (slope 2), a := ε/3, so
  ρ := −h − s has |ρ| ≤ ε for |s| ≤ a; the smallest solution y_min(s) is computed exactly on each linear branch. PASS iff
  y_min(a − 10⁻⁶) − y_min... i.e. |y_min(a + 10⁻⁶) − y_min(a − 10⁻⁶)| ≥ ε (a jump of ≈ 4a = 4ε/3 at s = a).
  Comparison F4-K (contraction, slope ½: h(y) := y/2 on |y| ≤ a, saturated beyond): the unique solution moves by ≤ 2·|Δs|
  between the same two s values. PASS iff so.
Written at (date -u, appended): 2026-10-29T00:40:22Z
