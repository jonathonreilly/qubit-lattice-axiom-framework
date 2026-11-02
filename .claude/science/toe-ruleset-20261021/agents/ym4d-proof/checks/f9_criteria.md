# f9 criteria (lane C, session 6): the root sector at constant Cartan curvature

Written before any f9 script. Tests FLOW.md §42-§46 (session 6). One script, checks/f9_root_sector.py, output
checks/f9_out.txt, timing checks/f9_time.txt. NUMERIC LOCK, nice 10, all BLAS threads = 1, wall < 20 min, peak < 1 GB.

Notation: j_ν(t) := e^{-2t}I_ν(2t) (scipy.special.ive(ν, 2t)); c_g := 1/(96π²); the "f² coefficient" of a quantity Y(f)
is extracted by Richardson from the second differences D(h) := (Y(h) − Y(0))/h² at h and 2h: c := (4D(h) − D(2h))/3, with
h = 1e-3 unless stated (all Y below are even in f).

## Part G (scalar / ghost pieces)

**G0 (Lemma GH algebra).** Complex charge-1 field (a root sector; the algebra is the same), fine torus with one flux
quantum in the plane 12 (U_{x,2} = e^{iφx_1}, seam links on direction 1 carry e^{-iφTx_2}, φ = 2π/T_1T_2), level-n sites
= the sites with all coordinates ≡ 0 mod 3 (ℓ = 3). Cases: 2D T = 9; 4D T = (3, 3, 3, 3) (flux in plane 12 only).
Build D_0 (0-forms → 1-forms), Δ_0 = D_0^*D_0, Λ' (functions vanishing at level-n sites), Δ', the Schur complement 𝒮,
the slice S_0 = (D_0Λ')^⊥, J = P_{S_0}D_0E (E: extension of μ by zero off the level-n sites).
- (G0a) ||J^*J − 𝒮|| / ||𝒮|| ≤ 1e-10.
- (G0b) |log det Δ_0 − log det Δ' − log det 𝒮| ≤ 1e-9.
- (G0c) ||P_{S_0} − P_{J} − P_{ker D_0^*}|| ≤ 1e-10 (S_0 ⊖ J(Λ_n) = ker D_0^*).
- (G0-ctl) Control: replace S_0 by a non-orthogonal complement S_r of D_0Λ' (S_r := (1 + εR)S_0 with a fixed random R,
  ε = 0.3, then J_r := the S_r-component of D_0E along D_0Λ'). Must FAIL (G0a): ||J_r^*J_r − 𝒮||/||𝒮|| ≥ 1e-3.

**G1 (Lemma G-mag (iii), exact second moment).** 2D open box of side B = 81 (centre site x_0), charge-1 Harper Laplacian
Δ_φ (gauge U_{x,2} = e^{iφ(x_1 − x_{0,1})}); Y(φ) := e^{-tΔ_φ}(x_0, x_0) by sparse expm_multiply. Prediction: the φ²
coefficient equals −½(t²/3)j_1(t)². At t ∈ {0.5, 1, 2, 4, 8, 16}: PASS iff every |c(t)/(−(t²/6)j_1²) − 1| ≤ 1e-6.

**G2 (Lemma G-mag (v), (vi)).** Infinite-volume rational flux φ = 2π/Q (p = 1): 2D Harper Bloch matrices (Q × Q, Landau
gauge, Bloch phases θ_1 ∈ [0, 2π) on the period-Q direction, k_2 ∈ [0, 2π/Q)), τ_2(t) := average over a K × K grid of
(1/Q)Σ_j e^{-tE_j}. ψ(φ) := φ^{-2}∫_0^∞(dt/t)j_0(t)²[j_0(t)² − τ_2(t)] by the trapezoidal rule in u = log t on [−8, 16],
du = 0.01. Q ∈ {16, 32, 64, 128, 256, 512}, K = 4. c'(φ) := ψ(φ) − c_g log(1/φ).
- (G2-acc) accuracy: for Q = 128, |ψ(K = 4) − ψ(K = 8)| ≤ 1e-8 and |ψ(du = 0.01) − ψ(du = 0.02)| ≤ 1e-8.
- (G2a) slope: the least-squares slope of ψ against log(1/φ) over the three smallest φ satisfies |slope/c_g − 1| ≤ 0.02.
- (G2b) (evidence for (vi), not a proof) increments δ_k := c'(φ_{k+1}) − c'(φ_k) along the halving sequence: for the last
  three, |δ_{k+1}| ≤ 0.75|δ_k|, and |δ_last| ≤ 1e-4.

**G3 (Proposition GH-log, ghost-group coefficient).** Δ_ℓ(φ) := ψ(ℓ²φ) − ψ(φ) (per q², the f² coefficient of the ghost
group with F_n = ℓ²f exactly), prediction −2c_g log ℓ.
- (G3a) ℓ = 3: φ = 2π/(9Q'), Q' ∈ {16, 32, 64}: PASS iff |Δ_3/(−2c_g log 3) − 1| ≤ 0.02 at Q' = 64 and the deviation
  decreases monotonically in Q'.
- (G3b) ℓ = 9: Q' ∈ {4, 8} (fine Q = 324, 648): informational (the level-n flux 2π/Q' is not small).

## Part V (vector pieces; SU(2) Wilson action at a Cartan background)

SU(2), s(U) = 1 − ½Re tr U, coordinates X = i(x_1σ_1 + x_2σ_2 + x_3σ_3) (orthonormal for −½tr), U_b → U_be^{X_b}.
Background U_f: U_{x,2} = exp(iσ_3 f x_1), other links 1 (plus seam links on tori as in G0); root charge q = 2, root block =
colours a ∈ {1, 2}, Cartan block a = 3. H := the Hessian of Σ_p s(U_p) at X = 0, computed per plaquette from exact matrix
products (first-order insertions U_bt_a, second-order ½U_b(t_at_c + t_ct_a), with inverses for reversed links);
(D_0λ)_b := Ad(U_b^{-1})λ(x) − λ(x + μ); K_F := H + D_0D_0^*.

**V0 (criticality and structure; 4D torus T = (6, 6, 3, 3), one flux quantum f = 2π/36 in the plane 12).**
- (V0a) the gradient of Σ_p s at U_f: max ≤ 1e-12.
- (V0b) ||HD_0||_max ≤ 1e-11 (HJ = 0 in all sectors, COV-GI (ii)(a), non-tautological in SU(2)).
- (V0c) ||K_FD_0 − D_0Δ_0||_max ≤ 1e-11.
- (V0d) the Cartan-root block of H: max ≤ 1e-12.
- (V0e) (the decomposition of §46) K_F = [K_12 ⊕ Δ^{(12)} ⊗ 1_{comps 3,4}] ⊗ 1_{34} + 1 ⊗ Δ^{free}_{34}, with K_12 (2D Feynman
  operator on components 1, 2) and Δ^{(12)} (2D adjoint covariant Laplacian) built independently by the same code on the
  2D torus 6 × 6: max entry difference ≤ 1e-12.
- (V0-ctl) Control: f = 1.3 × 2π/36 (not flux quantised; the seam plaquettes differ, so U_f is not constant curvature):
  (V0a) and (V0b) must FAIL (≥ 1e-3).

**V1 (scalar calibration in the SU(2) harness).** 2D open box B = 101, root block of the adjoint covariant Laplacian at the
centre: complex heat trace Y(f) (½ × the sum over a ∈ {1, 2} of diagonal entries). Prediction: f² coefficient
−½q²(t²/3)j_1². t ∈ {2, 4, 8, 16, 24}: PASS iff every relative error ≤ 1e-6.

**V2 ((V-heat), the universal check).** Same box; root block of K_12 at the centre: complex heat trace Y(f) (½ × the sum
over μ ∈ {1, 2}, a ∈ {1, 2} of diagonal entries); R_12(t) := c(t)/(q²t²j_0(t)²) at t ∈ {2, 3, 4, 6, 8, 12, 16, 24}.
Prediction (continuum, §46): R_12 → 11/3.
- (V2-norm) at f = 0, Y = 2j_0² to 1e-10 relative.
- (V2a) fit R_12(t) = R_∞ + a/t + b/t² on t ∈ {6, 8, 12, 16, 24}: PASS iff |R_∞/(11/3) − 1| ≤ 0.02.
- (V2b) stability: the same fit on t ∈ {4, 6, 8, 12, 16} gives R_∞ within 0.02 × 11/3 of (V2a)'s.
- (V2c) (no separate prediction; reported) R_V^{4D}(t) = R_12(t) + 2R_S(t) against 10/3, R_12 + R_S against 7/2.

**V4 (Cartan block, "no log").** Same box, Cartan block of K_12: R_C(t) := c_C(t)/(t²j_0(t)²) (real trace over μ ∈ {1, 2},
a = 3). PASS iff |R_C(24)| ≤ 0.01 and |R_C(24)| ≤ 0.5|R_C(12)|.

## Reading rule (pre-stated)

- G0, G1, V0, V1 test PROVEN-HERE identities: any FAIL beyond the tolerances is a defect of the derivation or the code
  and is recorded as such. G0-ctl and V0-ctl must FAIL.
- G2a, G3a test Lemma G-mag (v) and Proposition GH-log numerically; G2b is evidence for the ARGUED item (vi) only.
- V2 tests the OPEN input (V-heat): PASS is evidence, not proof; FAIL is recorded as failure mode S6-F5 (or as a
  finite-t artefact if the fits are unstable, V2b FAIL).
- Nothing here tests (V-IR), (R1), (R2), or the S4' contours.
