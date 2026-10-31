# c32 criteria (written BEFORE checks/c32_rlarge.py; session 17, 2026-10-27, after RLARGE.md §0-§8)

Purpose: instances of the counted constants of RLARGE.md Lemma RS (re-seeding), of the hard-core combinatorics used in
Theorem R1 (i), and of the B_4 orbit average of Lemma GT-lat' (ii); the n_* arithmetic is informational. Not a proof.
Four parts, each its own job (`python3 c32_rlarge.py A|B|C|D`), one job at a time, nice 10, OPENBLAS/OMP/MKL/vecLib
threads 1, no `timeout`. No float tolerance beyond those written here; any needed later goes into an addendum to THIS
file before the run that uses it.

## Part A: Lemma RS on explicit SU(2) configurations, d = 4, L = 3
Region U_4: x_0, x_1 ∈ {-1, …, 4}, x_2, x_3 ∈ {-1, 0, 1} (four blocks of side 3 centred at 0, 3e_0, 3e_1, 3e_0 + 3e_1); all
links with both ends in U_4. Coarse plaquette P in plane (0, 1): c_1 = 0 → 3e_0, c_2 = 3e_0 → 3e_0 + 3e_1,
c_3 = 3e_1 → 3e_0 + 3e_1, c_4 = 0 → 3e_1. Convention: path transporter = ordered product of link matrices,
U_{-b} = U_b^†; plaquette U_p = U_{x,μ}U_{x+μ,ν}U_{x+ν,μ}^†U_{x,ν}^†. Contours T^σ_y = P^σ(c_start → y)·leg_L(y)·
P^σ(c_end → y + 3e_dir)^†, σ over all 24 orders, y over the 81 sites of the start block; S_c the straight transporter.
η := max over all plaquettes of U_4 of ||1 - U_p||_op. A_4(3) = 9, L² = 9.
Configurations:
- R: random SU(2), U_b = exp(i t Σ_k a_kσ_k/2), a_k iid N(0, 1), t ∈ {0.01, 0.05, 0.2}, seeds 0-4 (15 configurations).
- S1 (sharp ribbon): U_b = exp(iθ_bσ_3), θ_{x,0} := -f(x_1 + x_2 + x_3), θ_{x,α} := 0 (α ≥ 1), f = 0.001.
- S2 (sharp square): θ_{x,1} := f·x_0, other θ = 0, f = 0.001.
- S3 (control field): S1 plus θ_{x,2} += f·x_1, θ_{x,3} += f·(x_1 + x_2) (flux in the planes (1,2), (1,3), (2,3)), f = 0.001.
Criteria:
- **A1 (ribbon, R1):** for every R configuration and every c ∈ ∂P: max_{σ,y}||T^σ_y - S_c||_op ≤ 9η. Also for S1, S2, S3.
- **A2 (square, R2):** for every configuration: ||1 - S_P||_op ≤ 9η.
- **A3 (full R2):** for every R configuration, V_c := S_c·exp(i s Σ b_kσ_k/2) with b iid N(0,1), s ∈ {0.05, 0.3}, 5 draws
  each: ||1 - V_P|| ≤ 9η + Σ_c||V_c - S_c||.
- **A4 (kernel inequality, R4):** for every R configuration, every c, and 200 Haar-random V ∈ SU(2) plus 200 V near S_c:
  1 - ½Re tr(V^{-1}M̄_c) ≥ ||V - S_c||²_op/4 - ||M̄_c - S_c||_op, with M̄_c the mean of the 24·81 contours.
- **A5 (sharpness, power):** S1: the ribbon ratio max_{σ,y}||T^σ_y - S_{c_1}||/η ∈ [8.9, 9.0]; S2: ||1 - S_P||/η ∈ [8.9, 9.0].
- **A6 (pairing is load-bearing):** for S3, the UNPAIRED contours T^{σ,σ'}_y := P^σ(c_X → y)·leg(y)·P^{σ'}(c_Y → y + 3e_0)^†
  (σ ≠ σ' allowed) for c_1 reach max ratio > 9.5, while the paired ones (A1) stay ≤ 9.
- A7 (informational): max ratios over the R configurations.
- **PASS iff A1-A6.**

## Part B: hard-core combinatorics (Theorem R1 (i))
- **B1 (fattening = touching, d = 4):** torus (Z/6)⁴. 3000 random pairs (Y, Y') of random sets (sizes 1-6, cubes uniform),
  plus 500 pairs built at sup-distance exactly 1 and 500 at exactly 2: [(Y + {0,1}⁴) ∩ (Y' + {0,1}⁴) ≠ ∅] ⇔
  [∃x ∈ Y, x' ∈ Y' with x - x' ∈ {-1, 0, 1}⁴ mod 6]. PASS iff equal in every case.
- **B2 (components ↔ disjoint fattened families, d = 4):** torus (Z/6)⁴. 2000 random sets B (sizes 1-12): its *-components
  have pairwise disjoint fattenings. 2000 random families of *-connected sets (grown by random *-adjacent steps) with
  pairwise disjoint fattenings: the *-components of their union are exactly the family. PASS iff all hold.
- **B3 (locality of the graded logarithm, d = 1):** torus Z/T, *-adjacency = nearest neighbours, Ŷ = Y + {0, 1}. Activities
  r_Y = t^{|Y|}u_{|Y|} for intervals Y (u_1..u_8 fixed: 1.0, 0.7, -0.4, 0.9, 0.3, -0.2, 0.5, 0.1). Ξ_T(t) := Σ_BΠ r(components)
  by exhaustive enumeration (T = 12, 14, 16); c_N(T) := the t^N coefficient of log Ξ_T(t) (exact power-series log of the
  polynomial). PASS iff |c_N(T)/T - c_N(16)/16| ≤ 1e-9·max(1, |c_N(16)/16|) for N ≤ 4 and T ∈ {12, 14}.

## Part C: n_* arithmetic (informational, one consistency criterion)
β' := 11N²/(12π²) (one-loop rate in R4D-iso's normalisation; LF-count [inference]), a'' := 0.9·ε_1²/(4N),
n_* := ⌊4/(a''β')⌋, for N ∈ {2, 3}, ε_1 ∈ {0.25, 0.5, 1, 2}. **C1:** (n_* + 1)a''β' > 4 ≥ n_*a''β' in every case. Print n_*
and, at d = 4, L = 3, κ = 1, N = 2, ε_1 = 0.5: η_1, the RS exponents η_1²/(2N), κε_1²/(256N), and ε_loc (b_1 as in CL).

## Part D: B_4 orbit average on Λ²R⁴ (Lemma GT-lat' (ii))
Λ²(R) for the 384 signed permutations R (basis e_a∧e_b, a < b). 20 random symmetric 6 × 6 matrices t (seed 0).
- **D1:** ||(1/384)Σ_RΛ²(R)^TtΛ²(R) - (tr t/6)·1||_max ≤ 1e-12 for all t.
- **D2 (control):** over the 192 rotations (det R = +1) the average differs from (tr t/6)·1 by ≥ 1e-3 for at least 15 of
  the 20 t (self-dual/anti-self-dual split; c19 P1).
- **PASS iff D1, D2.**
