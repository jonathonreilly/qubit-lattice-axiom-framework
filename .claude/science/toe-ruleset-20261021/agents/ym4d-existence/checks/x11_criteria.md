# x11 criteria (written 2026-10-28 ~05:04 UTC, after EXISTENCE §21.0 (05:02) and before any x11 script)

Purpose: T35 (iii). The order-g⁴ coefficient of the Wilson-measure expectation of the corner observable
  O := tr(Y_12[Y_23, Y_31])  (§20.4; plaquettes at the origin in directions 1, 2, 3 of a 4D periodic T⁴ lattice),
with S_W = (2/g²)Σ_P Re tr(1 - U_P), U_b = exp(g a_b), basis tr(T^aT^b) = -½δ^{ab}. Expansion (fixed by hand before this file):
  Y_P = g L_P + g² B_P + O(g³),  B_P := ½Σ_{i<j}[X_i, X_j]  (X = signed path-ordered link logs of P),
  S_W = Σ_P[½|L_P|² - g Σ_{i<j} tr(L_P[X_i, X_j])] + O(g²·quartic),
  E[O] = g⁴ N(N² - 1)·κ + O(g⁶),  κ = κ_PO + κ_V,
  κ_PO := -½ Σ_cyc Σ_{i<j} ½[γ(X_i, L_Q)γ(X_j, L_R) - γ(X_i, L_R)γ(X_j, L_Q)]   (path ordering; = Lemma PO with Γ = the gauge
          propagator; cyclic (P, Q, R) over the three corner plaquettes),
  κ_V := ¼ Σ_{all plaquettes P'} Σ_{i<j} det[γ(L_r, ·)]_{r ∈ (12, 23, 31); columns (L_P', X'_i, X'_j)}   (three-gluon vertex),
with γ the colour-stripped covariance of the lattice covariant-gauge propagator
  D_μν(k) = δ_μν/k̂² - (1 - ξ)k̂_μk̂_ν/k̂⁴, k ≠ 0, link fields at link midpoints. Ghosts and the Haar Jacobian do not contribute at
this order (ghost tadpole ∝ f^{abb} = 0; Jacobian even).

Run plan: ξ ∈ {0, 1, 2}; T ∈ {12, 16, 20, 24, 32}; colour-stripped (κ is N-independent); single run, fixed seeds for C-E.

A (load-bearing for "the tree-level Wilson value is κ ≠ 0 with the stated sign").
  - A1 (gauge independence) PASS iff at T = 32, max_ξ |κ(ξ) - κ(1)| ≤ 0.02·|κ(1)|, and the spread at T = 32 is ≤ the spread at
    T = 16. (Expected exact up to rounding if the zero-mode removal does not break the order-g⁴ Ward identity; if the spread is
    > 1e-8 relative, that is reported as a finite-volume effect.) FAIL means a sign/factor error or a missing term: then no
    value of κ is claimed.
  - A2 (box convergence and non-vanishing) PASS iff |κ(1, 32) - κ(1, 24)| ≤ 0.01·|κ(1, 32)|, and |κ(1, 32)| ≥ 10× both the
    T = 32 ξ-spread and the T = 24 → 32 drift.
B (reproduces x10 B). κ_PO(ξ = 1, T) = 0.008268 within 2e-6 for T ≥ 16. PASS/FAIL.
C (Wick identity for two f-cubics). For SU(2) and SU(3) and a fixed random 6×6 positive-definite colour-stripped covariance Γ
  (with within-triple correlations), Monte Carlo n = 4·10⁵ samples per N of tr(A[B, C])·tr(D[E, F]) against
  ¼N(N² - 1)·det Γ_{(A,B,C),(D,E,F)}. PASS iff within 4 SE for both N.
D (BCH cubic of the Wilson action). 200 random plaquettes (unit Gaussian link logs, SU(2) and SU(3)), exact exponentials and
  logs: e(g) := max |[(2/g²)Re tr(1 - U_P(g)) - ½|L|²]/g - S_3'|, S_3' := -Σ_{i<j}tr(L[X_i, X_j]). PASS iff e(1e-3) ≤ 0.2·e(1e-2)
  and e(1e-3) ≤ 1e-2.
E (star corner trees). For each of the 8 star corner trees T_0 (the three links U_μ(0), μ = 1, 2, 3, plus one outer link of each
  corner plaquette) and 50 random SU(2) and SU(3) configurations of the 9 corner links: after the gauge transformation that
  sets the six tree links to 1 (h(0) = 1), each corner plaquette equals the remaining (non-tree) link of that plaquette or its
  inverse, and O(configuration with the three non-tree links inverted) = -O. PASS iff all to 1e-10.

Resource rules: numeric lock (mkdir/rmdir once, no trap), nice 10, BLAS/OMP threads 1, python3 without -I, no timeout,
load < 8; expected < 5 min, < 1 GB.
