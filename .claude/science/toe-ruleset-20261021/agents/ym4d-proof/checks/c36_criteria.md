# c36 criteria (written before any c36 script; session 20, 2026-10-28 UTC; targets RTARGET.md §44)

Run discipline: machine-wide numeric lock (mkdir/rmdir), nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, load < 8 and
memory >= 25% free before each job, peak RSS < 1 GB, no `timeout`. A FAIL is recorded as pre-registered; no criterion is
edited after a run. Parts are independent: `python3 c36_nah1.py A|B|C|D`.

## A. The exact lift (Lemma U0), SU(2), d = 4, L = 3, coarse torus T = 2 (fine side 6)
Random level-1 field V (coarse links exp(t X_c), X_c Gaussian in su(2), t = 0.7 — the lemma is exact, no smallness),
then a random Haar coarse gauge G applied (so V is not near 1).
- A1: max_c ||M̄_c(U^(0)(V)) - V_c||_HS ≤ 1e-12 (M̄ = mean of the 24 × 81 S4' contour transporters).
- A2: every fine plaquette that is not a block corner has ||U_p - 1|| ≤ 1e-12; every corner plaquette equals the coarse
  plaquette holonomy V_P of its coarse site and plane (≤ 1e-12), up to the orientation fixed in the lemma.
- A3: gauge covariance: U^(0)(GV) = Ĝ U^(0)(V) Ĝ^{-1} (Ĝ the block-constant extension) to ≤ 1e-12.
- A4: soft fluctuation ρ_c(U^(0)(V), V) = 0: ||log(V_c^{-1} W_0(M̄_c))|| ≤ 1e-12 (W_0 = M̄/sqrt(det M̄) for SU(2)).
PASS iff A1-A4.

## B. Critical branch and the Schur-complement identity, d = 2 SU(2) model, L = 3, coarse torus T = 2 (fine 6 × 6)
F(U, V) := S_W(U) + κ_0 Σ_c φ̂_c, φ̂_c := 2 sqrt(det M̄_c(U)) - Re tr(V_c^{-1} M̄_c(U)) (the exact N = 2 tree-level soft
density Nφ of NA-alg (b) for SU(2)), κ_0 = 1. S4' with the 2 orders of d = 2. Backgrounds: V_c = exp(t X_c), t ∈ {0.05,
0.15}, then a random Haar coarse gauge. The level-0 operator O(U, V) = Hess_A F + D_U P_res^U D_U^* with NA-FP's h_U,
M_U, P_res^U; C := Π(ΠOΠ)^{-1}Π on ker h_U.
- B1: the contraction iteration from U^(0)(V) on ker h_{U^(0)} (with the fixing term) converges: final gauge-fixed
  residual ≤ 1e-11; the limit is critical for F without the fixing (max gradient block norm ≤ 1e-9) and has
  ||P_res D^* A*|| ≤ 1e-9 (Lemma NA-crit with multipliers).
- B2: for 6 random directions B on level-1 links, d²/ds² E^br(e^{sB}V)|_0 (fourth-order central differences with
  re-solved branch, steps 1e-3 and 5e-4, Richardson) agrees with ⟨B, (F_VV - F_VU C F_UV) B⟩ to relative 1e-5.
- B3: at the branch, ||Hess_A F (D_U λ)|| ≤ 1e-7 ||λ|| for random λ ∈ Λ (NA-inv), and the Schur result changes by
  ≤ 1e-8 relative when the fixing weight on P_res D^* is changed from 1 to 3 (fixing independence).
- B4 (informational): λ_min of the level-0 Õ at the branch and of the Schur-complement Hessian restricted to the
  complement of level-1 gauge directions, against t.
PASS iff B1-B3.

## C. Target B: c35 C2 in exact rational arithmetic (L = 3, d = 4, κ = 1), on Z⁴
Rows of Õ_0 = ΠO_0Π + (1 - Π) for the 324 links of the reference block, O_0 = d*d + κQ^TQ + dP_resd*, every entry a
Python Fraction, computed on Z⁴ (no torus).
- C1: every row vanishes outside the links based in the 3⁴ blocks around the reference block (exact zero), and the
  4 × 81 rows of 1 - Π give ν_w = 30/13 exactly.
- C2: exact symmetry Õ_0(b, b') = Õ_0(b', b) for b, b' both in the reference block.
- C3: N_exact := max_b Σ_{b'}|Õ_0(b, b')| and M1_exact := max_b Σ_{b'}|Õ_0(b, b')| d(b, b') (ℓ¹ distance of base points)
  agree with c35's floats 25.4760 and 41.0765 to relative 1e-5, and M1_exact ≤ 41.077.
- C4: with m := 193/10^12 (= 1.93·10⁻¹⁰), the exact rational inequality M1_exact·m·(1 + 40m) ≤ γ_0/2 holds,
  γ_0 = (1/(3.5·10⁶))·(1/2)/9 (Lemma N5-coer at i = 0), which proves D_m(|Õ_0|) ≤ γ_0/2 since e^x - 1 ≤ x e^x and
  e^{20m} ≤ 1 + 40m for 20m ≤ 1, d ≤ 20 on the support (also checked exactly).
PASS iff C1-C4.

## D. Level 1 at the trivial background: measured gap and decay of Õ_1 against level 0 (abelian, κ ≡ 1, L = 3)
Ĥ_1(p) := κ_0 1_4 - κ_0² Q̂(p) Ĉ_0(p) Q̂(p)^* on the level-1 momentum grid (2π/12)Z⁴, Ĉ_0(p) := Õ_0(p)^{-1} - (1 - Π̂)
(Bloch fibres of the level-0 objects, as in c35 C3); Õ_1(K2) the 324 × 324 fibre of Π(H_1 + κQ^TQ + dP_resd*)Π + 1 - Π
at level-2 momenta K2 ∈ (2π/4)Z⁴.
- D1 (validation): max_p ||Ĥ_1(p) ν(p)|| ≤ 1e-10 (gauge direction, ν the null vector of the level-1 d*d symbol) and at
  p = (π, π, π, π) the ratio min_b ½b^*Ĥ_1b / b^*(d*d)^(p)b over b ⊥ ν equals c31 E's k = 1 per-mode minimum 0.030950 to
  relative 1e-4.
- D2: γ_meas(1) := min over the K2 grid of λ_min(Õ_1(K2)) is ≥ N5-triv's proven γ_1 = 1.29·10⁻¹⁰; report the ratio
  γ_meas(1)/γ_meas(0) with γ_meas(0) recomputed on the same-size grid for Õ_0 (and c35's 0.039849).
- D3 (informational): the real-space rows of Ĥ_1 (inverse FFT, level-1 torus side 12): decay profile, fitted rate, and
  N_0(|Õ_1|), Σ|Õ_1|d on the torus (aliased; measured only).
PASS iff D1-D2.
