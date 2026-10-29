# a2_55_nc — pre-registered criteria (written before the script exists)

Purpose: exact checks of the two algebraic facts behind ALIGN2_55 §3.1 (the chart witness against (NC) and against t_+ of Υ_HC):
(N1) the left-trivialised derivative of a path product, (N2) the first contour moment of the S4′ family. Fractions/ints only; stdout only.

## Part N1 — path-product derivative (nilpotent Lie algebra: strictly upper-triangular 6×6 rationals; exp/log finite)
A path is a sequence of links b_1..b_m with signs s_i ∈ {+1, −1}; the product is P(t) := Π_i (e^{t v_i} e^{y_i})^{s_i} (for s_i = −1 the factor is
(e^{t v_i}e^{y_i})^{−1} = e^{−y_i}e^{−t v_i}). Claim: (d/dt P)(0)·P(0)^{−1} = Σ_i s_i Ad_{A_i} v_i, where A_i := (product of the factors before
step i, at t = 0) for s_i = +1, and A_i := (that product)·e^{−y_i} for s_i = −1.
- **N1 PASS iff** the identity holds exactly for 4 seeded random paths (m = 7, random signs, random y_i, v_i).
- **Control CN1 (must FIRE):** the variant with A_i := (product before step i) also for s_i = −1 fails for at least one seed.

## Part N2 — the first contour moment of the order-averaged S4′ family
LINEAR_PACKAGE §1.2: for a coarse link (X, μ), contours T^σ_y = P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^†, y ∈ B(X), σ ∈ S_d, S_y = L straight steps in
direction μ. For a direction ν, each ν-step of a contour is a link with lower ν-height h (relative to c_X) traversed with sign ±1.
- **N2 PASS iff**, for (d, L) ∈ {(2, 3), (2, 5), (4, 3)}, for EVERY σ and y: (a) if μ = ν, Σ_{ν-steps} (±1)·h = L(L−1)/2 and Σ(±1) = L;
  (b) if μ ≠ ν, the multiset of (sign, h) over ν-steps cancels exactly (every (+1, h) is matched by a (−1, h)), so Σ(±1)·f(h) = 0 for every f.
- **Control CN2 (must FIRE):** replacing the return leg by the axial path in the REVERSED coordinate order (σ reversed at the far end) breaks (b)
  for some contour when d ≥ 2... is NOT used as a pass/fail control; instead **CN2:** with h replaced by the UPPER height h + 1, (a) fails
  (the sum becomes L(L+1)/2), showing the gate reads the convention.

## What this check cannot decide (stated in advance)
No norm statement, no k-dependence, no statement about W_0's first-order variation (taken from Codex KOFF §4.2's "δW₀ = Qδx" at M ∈ SU(N)),
nothing about higher moments beyond (b). OVERALL PASS iff N1, N2 PASS and CN1, CN2 FIRE.
