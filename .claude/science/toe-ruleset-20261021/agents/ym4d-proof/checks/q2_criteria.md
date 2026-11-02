# q2 criteria (lane G session 1; written BEFORE checks/q2_decay_min.py exists; not to be edited after the script is written)

Purpose: the LINEAR case of hypothesis (REG-min) of SQ.md §0: the cone-local, free-boundary minimiser of the linearised
chain energy, with a single top plaquette as data, lies in the decay class Σ_dec with a depth-independent constant.

Setting: the linearised soft chain (LINEAR_PACKAGE Setting SC), one real component, κ_i ≡ 1, L = 3. The straight average
Q_str of LINEAR_PACKAGE §1.2 replaces Q_root (SQ.md §0.4 records why curvatures, residual sizes and the minimum are the same
for both). The cone box of the level-k plaquette P in the (0,1) plane: level-i extents 2L^{k-i} × 2L^{k-i} (d = 2) and
2L^{k-i} × 2L^{k-i} × L^{k-i} × L^{k-i} (d = 4). Unknowns: the link fields B_0, …, B_{k-1} on all links of the level-i boxes.
Data: B_k on P's four links, B_k = θ on the first link (θ = 1), 0 on the others, so dB_k(P) = θ. Energy (cone terms only,
free boundary): E := ½Σ_{level-0 box plaquettes}|dB_0|² + Σ_{i<k}½Σ_{level-(i+1) box links c}|r_i(c)|², r_i := Q_strB_i - B_{i+1}.
Minimiser by sparse least squares (LSQR, atol = btol = 1e-12); converged iff the normal-equation residual ≤ 1e-8·(initial).
Measured: C_curv(k) := max_{0 ≤ i ≤ k-1} max_{level-i box plaquettes p} |dB_i(p)|·L^{2(k-i)}/θ;
C_res(k) := max_{0 ≤ i ≤ k-1} max_{level-(i+1) box links c} |r_i(c)|·L^{2(k-1-i)}/θ; C_D(k) := max{C_curv, C_res};
e(k) := E_min/θ².
Depths: d = 2, k = 1, …, 5; d = 4, k = 1, 2.

- **C1** every solve converged.
- **C2** depth-uniformity (d = 2): C_D(5) ≤ 1.5·C_D(3) + 0.5 and C_D(4) ≤ 1.5·C_D(3) + 0.5.
- **C3** the price bound in the linear case: e(k) ≥ 1/C_loc = 1/40 (E-loc, κ ≡ 1, L = 3, d = 4) for every d = 4 depth. No
  E-loc constant is derived for d = 2, so for d = 2 the criterion is e(k) > 0 for all k and e(5) ≥ 0.5·e(3).
- **C4** d = 4: C_D(2) ≤ 2·C_D(1) + 1 (two depths only; a weak monotonicity check).
- C5 (info) the tables C_curv, C_res, e per depth; the per-level profile max|dB_i|L^{2(k-i)}/θ.

OVERALL PASS iff C1-C4 all PASS. Resources as q1 (numeric lock, nice 10, threads 1, load < 8, ≥ 25% free memory, peak RSS
< 1 GB, python3 without -I, no `timeout`). Records: checks/q2_time.txt, checks/q2_out.txt.
