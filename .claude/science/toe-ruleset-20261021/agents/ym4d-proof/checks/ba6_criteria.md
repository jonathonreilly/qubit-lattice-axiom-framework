# ba6 criteria (BFT lane A, session 6). Written before checks/ba6_w0.py exists (see BFT_A_LOG for the file times).

Tests the statements of BFT_A §26 (PRE-STATED, session 6). Thresholds are exactness tolerances, inequality checks, the
a-priori factor 2 and trend rules. No constant derived in session 6 appears here. Model: the matrix-free chain of
checks/ba5_y.py (read-only import; c26 axial template, L = 3, κ ≡ 1, d = 4), p = the (0,1)-plaquette at the origin.

- **E1 (dualities).** (a) k = 1, T = 3 and k = 2, T = 2: for a random level-0 2-form G_0 (supported in a cube of side 5)
  and a co-closed plain current j_0 (Coulomb projection of a random 1-form in a cube of side 5), the solved response has
  f_0(p) = ⟨G^c_0, dY^p_0⟩ + n²⟨j_0, Y^p_0⟩ to 1e-8 relative. (b) k = 2, T = 2: for a random level-1 2-form G_1,
  dx_0(p) = ⟨G_1, dY^p_1⟩ to 1e-8 relative. (c) Lemma TOPD: for the response of (a) at k = 1, T = 3,
  r_{k-1}(x)(b) = ⟨G_0, dY^{(b)}_0⟩ + ⟨j_0, Y^{(b)}_0⟩ at one level-k link b, to 1e-8 relative. PASS iff all hold.
- **E2 (rigorous upper bound of 𝒬_H, α = ¼).** U_H(k, T) := Σ_q|dY^p_0(q)|w(q), w = (d/n)^α for ℓ^∞ base-point distance
  d ≤ n and w = 2 for d > n. S1(k, T) := Σ_q|dY^p_0(q)| (contrast, informational).
  - **H1 (trend):** at k = 1, U_H(1, 6) - U_H(1, 5) ≤ U_H(1, 5) - U_H(1, 4) + 0.02·U_H(1, 4).
  - **H2 (depth):** for T ∈ {2, 3, 4}: U_H(2, T) ≤ 2·max_{T'}U_H(1, T').
- **E3 (designed plain current, lower bound).** j* := Π_cc(tsign(Π_ccY^p_0)) (threshold 1e-12·max), D_N(k, T) :=
  |⟨j*, Y^p_0⟩|/(n·max|j*|). Informational upper proxy: ||Π_ccY^p_0||_1/n.
  - **N1 (trend):** at k = 1, D_N(1, 6) - D_N(1, 5) ≤ D_N(1, 5) - D_N(1, 4) + 0.02·D_N(1, 4).
  - **N2 (depth):** for T ∈ {2, 3}: D_N(2, T) ≤ 2·max_{T'}D_N(1, T').
- **E4 (Lemma CS inequalities).** k = 2, T = 2; 3 random level-l 2-forms for each l ∈ {0, 1}; m from l + 1 to 2.
  PASS iff max|d*G| ≤ 6max|G|(1 + 1e-12) and max|Q_str^{(l→m)}d*G| ≤ 6max|G|(1 + 1e-12) in every case (Q_str = the direct
  straight average of side L^{m-l}, own units of level m). Also d*G co-closed to 1e-12. Informational: the designed
  level-1 ratio n²|⟨G*, dY^p_1⟩|/(L^{2(k-1)}max|G*|), G* := tsign(dY^p_1).
- **E5 (Lemma LE ratio, informational).** max over level-k sites X of E_∇(dY^p_0; X)^{1/2}/max|n²dY^p_0| at k = 1,
  T = 2..6. **LE1 (trend):** the T = 6 value ≤ the T = 4 value·1.1.
- Resources: every part < 20 min and well under 1 GB RSS (k = 2 runs at T ≤ 4 only for E2, T ≤ 3 otherwise). Lock, nice
  10, threads 1.
