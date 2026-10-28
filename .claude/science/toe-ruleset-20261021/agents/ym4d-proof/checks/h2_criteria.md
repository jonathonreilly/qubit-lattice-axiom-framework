# h2 criteria (written before h2_constfield.py): Proposition CF (1)-(2), one S4' step — HIST.md §6

d = 4, L = 3, SU(2), S4' paired contours (all 24 axial orders, all 81 offsets y of the block, the same order at both ends,
as RLARGE c32). Box: coordinates (-1..4)³ × (-1..1), block centres 0 and 3e_μ. Field: U(x, 0) = exp(-iF x_1σ_3/2),
U(x, 1) = exp(iF x_0σ_3/2), U(x, 2) = U(x, 3) = 1 (constant curvature F in the (0,1)-planes). Cases F ∈ {0.01, 0.03, 0.058}
(F·A_4(3) = 9F < π/2). Coarse links: the four links of the coarse (0,1)-plaquette at 0 (as c32 C1-C4) and the transverse
link 0 → 3e_2. Tolerance 1e-12 (absolute, operator norm).
- **C1.** For each coarse link c: M̄_c = m_cS_c with m_c := ½Re tr(M̄_cS_c⁻¹) ∈ (0, 1]: ||M̄_cS_c⁻¹ - m_c·1||_op ≤ 1e-12. Print m_c.
- **C2.** W_0(M̄_c) (quaternion formula) = S_c: ||W_0 - S_c||_op ≤ 1e-12, and φ_{M̄_c}(S_c) ≤ 1e-14.
- **C3.** The coarse plaquette W_0(c_1)W_0(c_2)W_0(c_3)⁻¹W_0(c_4)⁻¹ = exp(iL²Fσ_3): error ≤ 1e-12.
- **C4.** Transverse link: every contour transporter equals S_c to 1e-12.
- **C5 (gauge control).** After a random SU(2) gauge transformation of the box field (seed 1): the m_c of C1 are unchanged to
  1e-12, and the C3 coarse plaquette's trace is unchanged to 1e-12 (with W_0 recomputed).
- **C6 (negative control).** Field multiplied link-wise by su2_exp(0.02·Gaussian) (seed 2): for at least one of the four
  plaquette links, ||M̄_cS_c⁻¹ - m_c·1||_op > 1e-6 (the test discriminates).
- **h2 PASS iff C1-C6 PASS in all three cases.** Machine: numeric lock, nice 10, BLAS threads 1.
