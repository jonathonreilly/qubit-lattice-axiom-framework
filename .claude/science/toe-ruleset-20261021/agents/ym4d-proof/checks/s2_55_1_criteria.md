# s2_55_1 — criteria (written before the script; SPHERE2_55 §1). Exact symbolic/rational arithmetic only (sympy).

Object under test. ROTDEF §3.2's lattice Lie derivative Ξ_v = ½(Ξ^left_v + Ξ^right_v), with
𝔣^ν_b = (2a²)^{-1}[π(P^{+ν}_b) − π(P^{−ν}_b)], ξ_b = −a Σ_{ν≠μ} v^ν(m_b) 𝔣^ν_b, π(M) = (M − M†)/2 − tr(M − M†)/(2N),
and the claimed EXACT identity (all configurations, every v read at link midpoints):
  (D-link)  div Ξ^left_b = div Ξ^right_b = (N C_F / a) Σ_ν v^ν(m_b) [ s(P^{+ν}_b) − s(P^{−ν}_b) ],  s(U) = 1 − Re tr U / N,
            C_F = (N² − 1)/(2N);
  (D-plaq)  hence div Ξ_v = −N C_F Σ_p (∂_μ v^μ + ∂_ν v^ν)(c_p) s(U_p) for every v quadratic in x (p in plane (μ,ν),
            c_p its centre), and = −2N C_F Σ_p (div v/4)(c_p) s(U_p) for the conformal Killing fields of the chart.
Basis: T_α orthonormal for ⟨X, Y⟩ = −2 tr(XY) (SU(2): T_α = −(i/2)σ_α; SU(3): T_α = −(i/2)λ_α, Gell-Mann).

PASS/FAIL gates (each must be decided by exact simplification to 0 or by exact rational comparison):
- C1 (Casimir contraction). For N = 2 and N = 3 and a generic symbolic complex N×N matrix M:
  Σ_α tr(T_α π(T_α M)) + ½(N − 1/N) Re tr M ≡ 0.  PASS iff identically 0 for both N.
  Control X1 (must FIRE): with π replaced by the Hermitian part h(M) = (M + M†)/2 the same difference is NOT identically 0.
- C2 (one link, both halves, exact rational SU(2) data). U, W_+, W_- ∈ SU(2) with rational entries (normalised integer
  quaternions), a and v^ν rational. Left: div := Σ_α d/dt ⟨T_α, ξ(e^{tT_α}U)⟩|_{t=0} with ξ(U) = −a v (2a²)^{-1}[π(UW_+) − π(UW_-)].
  Right (mirror, U → U e^{tT}): Q_± := U^{-1}W̃_± (plaquettes based at the far end, starting with U^{-1}),
  ξ̃(U) = −a v · (−(2a²)^{-1})[π(Q_+) − π(Q_-)]; div~ := Σ_α d/dt ⟨T_α, ξ̃(U e^{tT_α})⟩|_{t=0}.
  PASS iff div = (N C_F/a) v [s(UW_+) − s(UW_-)] and div~ = (N C_F/a) v [s(Q_+) − s(Q_-)] exactly, on at least 3 data sets.
  Control X2 (must FIRE): with the right half's sign convention flipped (𝔣̃ := +(2a²)^{-1}[π(Q_+) − π(Q_-)]) the right
  divergence equals −(N C_F/a) v[s(Q_+) − s(Q_-)] ≠ the claimed value (on data where s(Q_+) ≠ s(Q_-)).
  Also: the classical-sign test — for Q_± = U^{-1}W̃_± built from the SAME plaquettes as P_± (W̃ chosen so that Q_± is the
  cyclic/inverse relabelling of P_±), Re tr Q_± = Re tr P_± exactly (so the two halves give the same divergence).
- C3 (quadratic collapse). Boost v_c(x) = R²c + 2(c·x)x − |x|²c, symbolic. (a) For each ν and h = (a/2)e_ν:
  v^ν(x − h) − v^ν(x + h) + a ∂_ν v^ν(x) ≡ 0. (b) For each μ: ∂_μ v^μ (no sum) − div v/4 ≡ 0.  PASS iff all ≡ 0.
  Control X3 (must FIRE): v = (x_1², 0, 0, 0) violates (b).
- C4 (whole-lattice rearrangement, 2D torus 3×3, SU(2), exact rational links, arbitrary rational midpoint values v^ν(m_b)).
  LHS := Σ_b div Ξ_b computed link by link by direct differentiation (C2's method, both halves averaged).
  RHS := (N C_F/a) Σ_p s(U_p)[v^ν(m_bot) − v^ν(m_top) + v^μ(m_left) − v^μ(m_right)] (p in plane (μ,ν) = (1,2)).
  PASS iff LHS = RHS exactly. Control X4 (must FIRE): RHS with bottom/top labels swapped differs from LHS.
- C5 (scheme family Ξ′_λ: 𝔣′ = w 𝔣, w = 1 + λ[s(P^{+ν}) + s(P^{−ν})], leading order). For SU(2), X_± = t A_± with rational
  traceless anti-Hermitian A_± and P_± = exp(X_±) (series to order t⁴): the extra divergence term per (b, ν) is
  E(t) := −(λ/N) Re tr(𝔣 (P_+ + P_-)) with 𝔣 = (2a²)^{-1}[π(P_+) − π(P_-)].  Claim: E(t) = (λ/a²)[s(P_+) − s(P_-)] + O(t⁴).
  PASS iff the t¹, t², t³ coefficients of E(t) − (λ/a²)[s(P_+) − s(P_-)] all vanish exactly, and the t² coefficient of
  s(P_+) − s(P_-) is nonzero on the data (so the claim is not vacuous). Consequence recorded (arithmetic): tree-level trace
  coefficient m̃(Ξ′_λ) = C_F − λ/N, equal to 0 at λ = N C_F = (N² − 1)/2.
  Control X5 (must FIRE): the same comparison with the 1/N dropped from E(t) fails at order t².
- C6 (numbers; π enclosed by the rational bounds 333/106 < π < 355/113). For N = 2..6:
  ratio_N := C_F/(2β_0) = 12π²(N² − 1)/(11N²) with 2β_0 = 11N/(24π²) (u = 1/g² units). PASS iff the enclosure gives
  ratio_2 > 8 and ratio_N < 12π²/11 < 10.77 for all N tested, and C_F > 2β_0 for N = 2..6.
  Control X6 (must FIRE, i.e. evaluate False): the statement "ratio_2 < 8" under the same enclosure.
Informational (no verdict): profile spans in β-units over one octave of spacing: 2N·2β_0·log 2 (perturbative value,
SEAM55 §1.5) vs 2N·C_F·log 2 = (N² − 1) log 2 (tree-level value), with log 2 ∈ [6931/10000, 6932/10000].
What this check cannot decide: whether LCS-a holds; the value of the fluctuation part B^fl; anything nonperturbative.
VERDICT PASS iff C1-C6 PASS and X1-X6 all FIRE.
