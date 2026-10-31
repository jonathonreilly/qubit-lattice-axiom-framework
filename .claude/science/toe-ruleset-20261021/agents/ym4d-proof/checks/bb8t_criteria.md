# bb8t criteria (lane B session 8; written after BFT_B §24 (11:12:37 UTC) and before checks/bb8t_get.py)

Tests Lemma GE-T (BFT_B §24.1) numerically, d = 4, abelian (one su(N) component; every map is componentwise).
Box Ñ_X: local coordinates {0..S-1}^4, S = 4n + 1, centre c = (2n, 2n, 2n, 2n); reflection torus side M_n = 2S; G_M the mean-zero
Green function of -Δ on the 4D torus (exact FFT). For a charge ρ on the box, ρ^R = its 16-fold reflection (Lemma REF), u = G_Mρ^R,
F := d u on the box links. (λ^E_X)^Tψ := -F for ρ = ψ - ⟨ψ⟩δ_c (the representation (a) to be tested against a direct solver).
n ∈ {2, 3, 4, 5, 6} (M = 18, 26, 34, 42, 50).

- T0 (identity (a)): max over the box of |d*_X F - ρ| ≤ 1e-9·max|ρ| (Neumann divergence), and max |du| on the reflection-crossing
  links ≤ 1e-9·max|du| (zero flux), for ρ = δ_w - δ_c with w a box corner, and for a random neutral ρ. PASS required.
- T1 (ℓ¹, (c)): for ρ = δ_w - δ_c, w ∈ {box corner (0,0,0,0), face centre (0,2n,2n,2n), c + e_1, one random site}:
  ||F||_1 ≤ M_n||ρ||_1 = 2M_n (PASS required, all n, all w). GE-F1 test: q(n) := max_w ||F||_1/n; q(6) ≤ 1.25·q(4) (PASS required).
  For random ψ (Gaussian on N_X, and uniform [0, 1] on N_X): ||F||_1 ≤ M_n||ψ - ⟨ψ⟩δ_c||_1 (PASS required).
- T2 ((e), C_∞): max_{y, μ}|∇_μG_M(y)| ≤ 2 for every M above (PASS required); values reported.
- T3 ((e), ℓ^∞): for the two random ψ of T1: ||F||_∞ ≤ (M_n/4)||ψ||_∞ + 32|⟨ψ⟩| (PASS required); ratio reported.
- T4 (adjointness, independent path; n = 2): λ^E_X(x) computed by conjugate gradients on the pinned Neumann normal equation
  (d*_Xd_Xλ = -d*_Xx, λ(c) = 0), for a random 1-form x on the box links; random ψ on the box. |⟨ψ, λ(x)⟩ - ⟨-F_ψ, x⟩| ≤ 1e-8·
  |⟨ψ, λ(x)⟩| (PASS required). Dual bound (d): with x := sign(-F) for ψ = δ_w (w the corner), λ(x)(w) = ||F||_1 to 1e-8 relative
  and ≤ 2M_n (PASS required).
- T5 ((f), combinatorial): d = 4, n = 27, s ∈ {1, 3, 9}: Σ_{level-l links}|d ev χ^5_X| ≤ 240(n/s)³ (PASS required); the ratio
  to (n/s)³ reported.
- T6 (composite Γ_E^T on a torus; coarse side 5, n = 3, fine side 15, l = 0): a random level-0 current j (Gaussian, sup-normalised
  to 1) on links with tail in |z|_∞ ≤ 1; D := d*j; Γ_E^TD := Σ_X(λ^E_X)^T(χ^5_XD). (i) d*(Γ_E^TD) = -D + Σ_X⟨χ^5_X, D⟩δ_{c_X} to
  1e-9 relative (Lemma GE (c) via (a)); (ii) adjointness ⟨D, Γ_Ex⟩ = ⟨Γ_E^TD, x⟩ (Γ_E x by CG per box, x random near the origin)
  to 1e-8 relative; (iii) ||Γ_E^TD||_1 ≤ 4M_n||j||_1; (iv) ||Γ_E^TD||_∞ ≤ 5^4[(M_n/4)||D||_∞ + 32 max_X|Q_X|]. PASS required for
  (i)-(iv); the split into the root part P and the bulk part B reported.
- C1 (control, pinned part): ψ = 1 on N_X: ||F||_∞/(2n + 1)^4 ∈ [0.05, 0.2] for every n (the pinned compensation charge makes
  the sup grow like n^d; PASS = the control behaves as predicted).
- C2 (control, GE-F3): adjacent dipole ρ = δ_{c+e_1} - δ_c: ||F||_1 increases strictly with n, and the two increments per log n,
  (||F||_1(4) - ||F||_1(2))/log 2 and (||F||_1(6) - ||F||_1(3))/log 2, agree within a factor 2 (log growth; PASS = predicted).
Resources: expected < 800 MB, < 5 min.
