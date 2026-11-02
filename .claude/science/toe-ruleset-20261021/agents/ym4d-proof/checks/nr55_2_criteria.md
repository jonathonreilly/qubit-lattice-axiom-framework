# nr55_2 — pre-registered criteria (written BEFORE checks/nr55_2.py exists)

Owner: NODEA_RES55.md (Opus 5.5, claude-opus-5-5). Purpose: an exact witness that the SU(2) Wilson action is NOT convex
on the single-level small-field set (the Nielsen–Olesen / Atiyah–Bott mechanism on the lattice), i.e. that hypothesis
(LC) of route (a) cannot be supplied by "every plaquette is small" alone.

## Setting
2D lattice patch, sites (i, j) ∈ {0..N}², links ((i,j),1) and ((i,j),2); plaquette (i,j): U_P = U_{(i,j),1}U_{(i+1,j),2}
U_{(i,j+1),1}^{-1}U_{(i,j),2}^{-1}, i, j ∈ {0..N−1}. Variable links: every link except those with BOTH endpoints on the
boundary (a coordinate 0 or N). Background C (uniform abelian field, Landau gauge): C_{(i,j),1} = diag(w^{-j}, w^{j}),
C_{(i,j),2} = 1, with w := (1 + iτ)/(1 − iτ) (|w| = 1, Gaussian-rational), so every plaquette equals diag(w, w̄) and
‖1 − U_P‖_op = 2τ/√(1 + τ²). Perturbation U_ℓ = e^{εX_ℓ}C_ℓ, X_ℓ = i(aσ1 + bσ2 + cσ3). S := Σ_P (1 − ½ tr U_P).
Q_C(v) := 2·[ε²]S(ε v) (exact, Gaussian rationals, truncated exponentials of order 2), G_C(v) := [ε¹]S(εv).
A float search (pure python power iteration on the exactly assembled Hessian) proposes v; v is then rounded to rationals
(denominator 10⁶) and every verdict is computed exactly from the rounded v.

## Gates (run at (τ, N) = (1/4, 8); optional second run (1/8, 12) if time permits, same gates)
- G5a (criticality): G_C(e_a) = 0 exactly for every coordinate direction e_a of every variable link. PASS iff all vanish.
  (Needed so that the sign of the Hessian is chart-independent.)
- G5b (non-convexity): Q_C(v) < 0 exactly for the rounded v. PASS iff strictly negative.
- G5c (record + sanity): Q_1(v) (same v, trivial background τ = 0) recorded; PASS iff Q_1(v) > 0 (the free Hessian is
  positive on v, so "H ≥ (1 − δ)M" fails for every δ < 1 on v).
- G5d (multiscale reading, record): |1 − w^9|² (the 3×3-blocked plaquette of the same background) recorded exactly and
  compared with |1 − w|²; PASS iff |1 − w^9|² > 81/100·|1 − w|²·... — no: PASS iff |1 − w^9|² > |1 − w|² (the coarse
  plaquette is larger than every fine one), recorded as the statement that the witness is a coarse-level defect for every
  ε_1 between the two norms.
## Controls (must FAIL as designed)
- G5n: at τ = 0 (C ≡ 1), the most negative float eigenvector v0 of the assembled free Hessian, rounded: Q_1(v0) < 0 must
  FAIL (the free Hessian Σ_P |linearised curvature|² is PSD), i.e. Q_1(v0) ≥ 0 exactly.
- G5n2: G5b applied to the vector v with its charged components (a, b) zeroed (only σ3 components kept) must FAIL
  (the abelian part of the Hessian at an abelian background is the free U(1) Hessian, PSD).
