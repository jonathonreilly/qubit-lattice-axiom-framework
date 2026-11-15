# q3b criteria (lane G session 2; written AFTER q3's official run and BEFORE checks/q3b_d4_plaq.py exists; not to be edited after the script is written)

Why a follow-up (post hoc, disclosed): q3 ran (B) and (C) in d = 3, where the decay-class weights L^{-2(k-i)} are not the
scale-invariant ones (q3 (A) shows the pure top-data response itself grows in d = 3: N_0 = 2.19, 4.01, 6.26 for data of
curvature 4). So q3 cannot separate a Calderón-Zygmund depth log from d = 3 scaling. q3b repeats (B) and (C) in d = 4, the
scale-invariant dimension, at the only affordable depths k = 1, 2 (k = 3 is ≈ 8·10⁶ unknowns). Two depths make this a WEAK
test; it is reported as such whatever the outcome.

Setting: exactly q3's (checks/q3_criteria.md), d = 4, κ ≡ 1, L = 3, Q_str, θ = 0, s ≡ 0, the same measured quantities N_0,
𝔑, R_ctr; the Chain class of checks/q3_src_decay.py is reused verbatim (read from that file).
- **(B4)** q_0 on (0,1)-plaquettes only: q_0(p) := L^{-2k}·sign(y_2² + y_3² - y_0² - y_1²), y := centre(p) - X*,
  X* := (n/2, n/2, (n-1)/2, (n-1)/2) (the extremal sign pattern, at the centre, of the Calderón-Zygmund part of
  (∂_2² + ∂_3²)Δ^{-1}, which is (1 - Π_ex) on the (0,1)-component); σ = 1.
- **(C4)** q_0(p) := L^{-2k}(y_2² + y_3² - y_0² - y_1²)/n², σ := its weighted sup (coarse-Lipschitz control).
Criteria:
- **R1** every solve converged.
- **RB** (B4) grows: R_ctr(2) ≥ 1.10·R_ctr(1) and R_ctr(2) - R_ctr(1) ≥ 0.05.
- **RC** (C4) flat: N_0(2) ≤ 1.10·N_0(1) + 0.05.
OVERALL PASS iff R1, RB, RC. Resources as q3 (numeric lock, one mkdir, one rmdir; nice 10; threads 1; load < 8; peak < 1 GB;
no `timeout`; python3 without -I). Records: checks/q3b_out.txt, checks/q3b_time.txt.
