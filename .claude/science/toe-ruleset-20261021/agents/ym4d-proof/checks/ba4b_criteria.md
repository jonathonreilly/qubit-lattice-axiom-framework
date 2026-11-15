# ba4b criteria (BFT lane A, session 4): post-hoc diagnostic, written after ba4 ran and before ba4b_diag.py exists

**Not a pre-registration of ba4.** ba4's T2 criterion FAILED for Q_XR (checks/ba4_out_D2.txt). This diagnostic asks
whether the T-uniform quantity that Theorem XR's proof bounds Q_XR by actually saturates. Written after seeing ba4's
outputs; it has no pre-registration weight for ba4, only for itself. No session-4 proof constant appears here.

- Quantity: B(T) := ||A - Q_0^T𝔽^{(0→1)}A||_1 / L² (k = 1, l = 0, A := Π_cc B'_0, B' the source-free response to the unit
  datum at (0, 0)); by the duality identity (S2, S3 of ba4), κ|r_0(0, 0)| = |⟨w, A - Q^T𝔽A⟩| ≤ sup|w|·L²B(T) for every
  rough w, so Q_XR(T) ≤ B(T) for every rough family. Also W(T) := Σ_b|∇A(b)| / L² (informational) and Q_a (as ba4 D1).
  T = 2, 3, 4, 5, 6.
- Discriminator (a priori numbers): with Δ_T := B(T) - B(T-1), compare TΔ_T at T = 6 and T = 3. For B = a + b log T the
  ratio (6Δ_6)/(3Δ_3) is 6 log(6/5)/(3 log(3/2)) = 0.90; for B = a - b/T it is (1/5)/(1/2) = 0.40. **PASS (saturation
  favoured) if the ratio ≤ 0.65 or B is non-increasing at T = 6**; FAIL = log growth not excluded.
- Also: Q_XR(T) ≤ B(T) at T = 2..5 using ba4's Q_XR values (exact inequality; a violation would be a code or proof error).
