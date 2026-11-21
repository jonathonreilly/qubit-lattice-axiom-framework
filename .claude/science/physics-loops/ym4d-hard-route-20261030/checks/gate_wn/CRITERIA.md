# Pre-registered pass/fail criteria (written before any script below was run)

Reviewer own code in this directory. No import or copy from SNAP/checks.

## wn01_coeff.py (tree coefficient, Prop 2.1, 2.2, 2.3, 2.4)
- A1 T identity: for random SU(2) triples, |T - 2 v1.(v2 x v3)| < 1e-13; for small psi, |T - psi1.(psi2 x psi3)/4| / |psi|^5 bounded (< 1).
- A2 K values on torus, Feynman, own FFT: T = 8, 16, 24, 32. PASS if within 2e-5 of the part's table for K_comp, K_vert, K_total.
- A3 Ward: random theta shift on E_3, E_1 separately, T = 6. PASS if relative change of K_total < 1e-10 and K_comp moves by > 1e-3.
- A4 Formula against a first-principles tree: open box, tree gauge, numerically minimise F - sum tau_i . psi_i and take the third derivative (d^3 w / 4 contracted with eps). PASS if relative difference from K_comp + K_vert on the same box (E_i from the box's own solution of d^T d E = J) < 1e-3. FAIL otherwise.
- A5 d = 2 plane: lassos around disjoint plaquettes on a large 2d torus: K_total scales as 1 / V (ratio near 4 per doubling of T), K_comp does not.

## wn02_rect.py (Lemma 3.2, 3.4)
- R1 (3.1) on a random rotation-invariant covariance, no translation invariance, torus T = 8, D = 2: residual / (largest term) < 1e-10. Equal-increments residual < 1e-10.
- R2 Feynman: sum K_comp^(k) / P_k + 24 Flux < 1e-10 relative.
- R3 Table: T = 40, D = 3, R = 6, 8, 12, 16, x = (R, 0, c, c). PASS if Stk_comp, Stk_total within 2% of the part's table (torus same size).
- R4 Decay: Stk_total slope between R = 8, 12 (T = 48 or more) steeper than -4.6, and |Stk_total / 24 Flux| decreases.
- R5 Flux closed form: at T large, R = 12, ratio to -24 D^2 (1 - 2t) / (pi^2 x^4) within 5%.

## wn03_form.py (Lemma 3.6, (3.4), (3.6), d-dependence)
- F1 closed form of Lemma 3.6 against a direct sum of V_p over the six plaquettes at a site, random complex polarisations, k^1 + k^2 + k^3 = 0: relative < 1e-12.
- F2 (3.4) against direct colour contraction with random complex h, v_i in S: relative < 1e-11.
- F3 (3.6) at level 0 by finite difference: relative < 1e-5.
- F4 d = 2 axial slice: form = 0 to 1e-12 on random momenta.
- F5 d = 3, axial slice n = e_3 (colour isotropic): evaluate the limit k^3 -> 0 of k3hat^2 Z at v_1, v_2 in S^0, v_3 in Q. Report the scaling. PREDICTION by reviewer: the leading term vanishes as eta -> 0 (the soft equation is passed) while the full form is non-zero at finite k^3. If the leading term does not vanish, the reviewer's reading of "d = 3 fails" is wrong.
- F6 d = 4, axial slice: the same limit does not vanish for generic k.
- F7 Isotropic kernel (reviewer's suspected gap at line 342 to 346): construct phi on P_k with an isotropic kernel and confirm that the displayed equation at that v carries no information on (v_3, sin k). Then minimise over phi (bounded) and over 2-dim Q in S_(k^3) the sup over v in P_k, v_3 in Q of |12 (v,v) (v_3, sin k) / k^4 + 2 phi(v) (v_3, D v)|. PREDICTION: the infimum is > 0 unless Q is P_k, i.e. the theorem survives by using the whole quadratic form. If the infimum is 0 at a Q not equal to P_k, the theorem's proof cannot be repaired this way.

## wn04_composite.py (NT2 wording: a Gaussian field composed with a nonlinear map)
- N1 Law: a Gaussian on links with covariance (4 / beta) G, A = a - (1/3) G grad S3tilde(a), with S3tilde = sum_p Phi_p . Q_p. U = exp(i A . sigma / 2). No vertex in the measure. PREDICTION: beta^2 <T> at the corner cluster tends to K_total, not K_comp. PASS if the fit at beta = 64, 128, 256 is within 3 standard errors + 5% of K_total at this T, and more than 3 standard errors from K_comp. FAIL if it is near K_comp.
- N2 Exact Wick evaluation of the same coefficient (no sampling): relative to K_total < 1e-10.
- N3 Mixture: moments of s_p: the mixture of two scales has E[s^2] / E[s]^2 differing from any Sum lambda_i z_i^2 law matching mean and with third moment. Checked by a small exact computation of the first three cumulants.

## wn05_noB.py (Theorem 3.5: reach of (B))
- B1 Construct on a torus an actual positive Gaussian potential A = a + grad phi, phi linear in a, rotation invariant, such that on the explicit rectangle family at D = 1 with a set of far plaquettes the tree values K_comp^(k)[c] = K_total^(k) and all pair values equal the Wilson ones. PASS (construction works) if residual < 1e-8 relative. Report link variance and the l^2 norm entering (B).

## wn07b (written after seeing wn07 at D = 3, where rho = 1 moved the sum 0.40 and rho = 2 moved it 0.85: D = 3 is not large against rho)
- Same law, D = 5, R = 12 and D = 7, R = 16, T = 40, rho = 0, 1, 2, 3. PREDICTION: at fixed rho the fraction of the way from -24 Flux to Stk_W falls with D about as 1 / D^2: at rho = 1, at most 0.2 at D = 5 and at most 0.12 at D = 7. If it does not fall, the claim that a strictly local map keeps the reading -24 Flux is withdrawn.
