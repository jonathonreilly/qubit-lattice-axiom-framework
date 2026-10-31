# f5 criteria (written 2026-10-27 23:39 UTC [file mtime], before checks/f5_cov_kernel.py)

Purpose (FLOW.md §14, T1 (R4), failure mode U-F2). The soft kernel's background dependence (its parallel transports)
produces kernel vertices in the one-loop polarisation. The claim tested: those vertices are IR-concentrated (their total
contribution to β is O(1), no log ℓ), and the full β has the universal log coefficient, κ-independently. A scalar
(abelian, Ω² channel) instance: it does not test the vector/ghost structure (L4b, f2, f3 do the channels).

Object. Fine lattice Z⁴, complex scalar φ, U(1) background A. M_A: φ^*M_Aφ = Σ_{x,μ}|φ(x+e_μ) - e^{iA_{x,μ}}φ(x)|²
(massless). Blocks of odd side ℓ centred at c ∈ ℓZ⁴. Covariant block average (Q_Aφ)(c) := ℓ^{-4}Σ_{x∈B(c)}
(1/24)Σ_σ exp(i∫_{σ: x→c}A)φ(x), σ running over the 24 coordinate orders of the monotone (axial) path from x to c (this
family is B_4-symmetric about c; Q_Aφ is gauge covariant: Q_{A+dλ}(e^{iλ}φ) = e^{iλ(c)}Q_Aφ). Kernel K_A := κQ_A^†Q_A,
κ = κ_cℓ² (κ_c fixed in coarse units, as f2). Γ(A) := log det(M_A + K_A): gauge invariant, B_4-symmetric, ℓZ⁴-periodic.
β := Σ_zz_1z_2Π_12(z) of the ℓ-translation-averaged Hessian at A = 0 (= -∂_{k1}∂_{k2}T_12(k) at 0, T_μν(k) the
per-site ε_1ε_2 coefficient for modes ε_1e^{ikx} on μ-links, ε_2e^{-ikx} on ν-links); c_Γ := β/2 (f3's normalisation;
universal slope 1/(48π²) per log ℓ, the IR scale ℓ playing the role of 1/m). Split: c_Γ = c^M + c^K, c^M from the
diagrams whose vertices all come from M_A (kernel only in the propagator), c^K from all diagrams with ≥ 1 kernel vertex.
Computed per coarse momentum class (ℓ⁴ aliases; diagonal + low-rank algebra, exact), coarse midpoint grid n_P⁴.

Pre-registered criteria:
- (A) validation, dense torus 6⁴ (ℓ = 3, coarse side 2), κ_c = 1, k = (2π/6)(1, 1, 0, 0): T_12 from the class formula on
  the torus momenta vs a central finite-difference mixed derivative (step 1e-4) of log det(M_A + K_A) built densely with
  complex-analytic A; same for the M-only quantity (log det(M_A + K_0)): relative difference ≤ 1e-6 for both.
- (A2) dense gauge invariance: |Γ(A + dλ) - Γ(A)| ≤ 1e-9 for random real A, λ (amplitude 0.3) on the 6⁴ torus.
- (B) Ward identity of the class formula on the 6⁴ torus momenta: |Σ_ν(e^{ik_ν} - 1)T_ν2(k)| ≤ 1e-10·Σ_ν|T_ν2(k)| at
  k ∈ {(2π/6)(1, 1, 0, 0), (2π/6)(1, 2, 1, 0)}; the M-only analogue is
  reported (informational; it is not expected to vanish).
- (C) quadrature: c_Γ(5, κ_c = 1) with n_P = 6 and n_P = 10: |difference| ≤ 1e-5·|c_Γ|.
- (D) k-step: c_Γ(5, 1) with finite-difference steps h = 1e-3 and 2e-3: |difference| ≤ 1e-6·|c_Γ|.
- (E) universality: slopes s(ℓ_1, ℓ_2) := (c_Γ(ℓ_2) - c_Γ(ℓ_1))/log(ℓ_2/ℓ_1) for consecutive odd ℓ in {3, …, 13}
  (n_P = 8); at (11, 13): |s·48π² - 1| ≤ 0.03 for each κ_c ∈ {0.25, 1, 4}.
- (F) κ-independence: at (11, 13), max_κ s - min_κ s ≤ 0.03/(48π²).
- (G) kernel vertices carry no log: the same slopes of c^K: at (11, 13), |s^K·48π²| ≤ 0.05 for each κ_c, and |s^K| at
  (11, 13) ≤ |s^K| at (7, 9).
Informational: c^M slopes (expected → 1/(48π²)); c^K values (expected to converge); the slope deviations |s·48π² - 1|
against ℓ^{-2} (T2's prediction, f6).

Outcome in checks/f5_out.txt, checks/f5_time.txt. A FAIL is reported as a FAIL.
