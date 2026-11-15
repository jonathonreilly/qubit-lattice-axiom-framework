# h1 criteria (written before h1_kernel_max.py): Lemma PM, Lemma KQ, Lemma RS-lin (b) — HIST.md §3

Groups SU(2) (maximiser in closed form: W_0 = v/|v| in the quaternion basis, v_a = Re tr(τ_a†M), τ = (1, iσ_1, iσ_2, iσ_3))
and SU(3) (maximiser by Riemannian gradient ascent W ← W exp(t·P(W⁻¹M)) from S and from 20 random starts, best value kept;
globality spot-checked against 2000 random W). Fixed seeds. Tolerance 1e-11 on every inequality.

- **P1 (PM).** For δ ∈ {δ_0, δ_0/3, δ_0/10, δ_0/100}, δ_0 = min{1/(640N), 2/N³}: 300 random pairs (S Haar, E random complex
  with ||E||_op = δ, M := S(1 + E)) plus 100 adversarial pairs (E anti-Hermitian traceless, ||E||_op = δ). PASS iff
  max ||W_0 - S||_op/δ ≤ 3 and max ||M - W_0||_op/δ ≤ 4 in every case. Print both maxima.
- **P2 (informational, no criterion).** The same maxima at δ ∈ {0.01, 0.03, 0.1, 0.3} (outside the lemma's range).
- **G (globality).** For 50 of the P1 instances per N: no random W (2000 Haar samples) has Re tr(W⁻¹M) > Re tr(W_0⁻¹M) + 1e-11.
  PASS iff no violation.
- **K1 (KQ lower).** 300 random M (half generic with ||M||_op ≤ 1, half M = S(1 + E) with ||E|| ≤ 0.05, rescaled to ||M|| ≤ 1),
  10 random V each: φ_M(V) ≥ x²/(2N) - x||M - W_0||_op - 1e-11. PASS iff no violation.
- **K2 (KQ upper).** V = W_0 exp(X), X random in su(N) with ||V - W_0||_op ≤ 1/(4N) (rescaled), same M's: φ_M(V) ≤ 2.5x² + 1e-11.
  PASS iff no violation; print max φ/x².
- **K3 (global upper).** φ_M(V) ≤ x + 1e-11 on the K1 samples. PASS iff no violation.
- **R (RS-lin (b) exponent).** For ε_1 ∈ {0.25, 0.5, 1.0}: δ := A_dη_q with A_d = 9 (d = 4, L = 3) and η_q = min{ε_1/18,
  ε_1/(256·9N), δ_0/9}; 200 pairs (S, M) with ||M - S||_op = δ (generic and adversarial) and 50 V each on the sphere
  ||V - S||_op = ε_1/8 (V = S exp(X), X scaled by bisection to hit the radius to 1e-12): φ_M(V) ≥ ε_1²/(1024N) - 1e-11. PASS iff
  no violation; print min φ·1024N/ε_1².
- **h1 PASS iff P1, G, K1, K2, K3, R all PASS.** Machine: numeric lock, nice 10, BLAS threads 1, peak RSS < 1 GB.
