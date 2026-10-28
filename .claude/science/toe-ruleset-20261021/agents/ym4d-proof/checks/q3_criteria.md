# q3 criteria (lane G session 2; written BEFORE checks/q3_src_decay.py exists; not to be edited after the script is written)

Purpose: SQ.md §T2 target Q3. Does the weighted-sup (decay-class) response of the LINEAR cone-local minimiser to sources
of unit weighted size grow with the depth k? REVIEW_SQ_S1 S1-4 predicts linear growth in k (sources at every level adding
at a fine site; the BNA-F2 Calderón-Zygmund log). The session-2 owner's prediction (exploratory sketch, not a proof at the
time of writing): residual sources (A) depth-flat; rough level-0 plaquette source (B) growing; smooth level-0 source (C)
depth-flat.

Setting: as checks/q2 (linear soft chain, one real component, κ_i ≡ 1, L = 3, Q_str in place of Q_root (SQ.md §0.4; the
argument there is unchanged by sources: the shift B' = B + dλ leaves the residual sources and the level-0 plaquette source
untouched)). Cone box of the level-k plaquette P in the (0,1) plane, level-i extents 2L^{k-i} × 2L^{k-i} (in-plane) and
L^{k-i} (each transverse direction), free boundary. Top data B_k = 0 (θ = 0): pure source response.
Energy: E := ½Σ_{level-0 box plaquettes}|dB_0 + q_0|² + Σ_{i<k}½Σ_{level-(i+1) box links c}|(Q_strB_i - B_{i+1})(c) + s_i(c)|².
Minimiser by LSQR (atol = btol = 1e-12); converged iff the normal-equation residual ≤ 1e-8·(initial).
Measured objects: F̂_0 := dB_0 + q_0; F̂_i := dB_i (1 ≤ i ≤ k - 1); r̂_i := Q_strB_i - B_{i+1} + s_i.
Weighted sizes: level-i plaquettes × L^{2(k-i)}, level-(i+1) links × L^{2(k-1-i)} (the decay-class weights of SQ.md §0.3).
- 𝔑 := max over all levels of the weighted sup of F̂_i and r̂_i, divided by the source size σ (defined per part);
- N_0 := the level-0 part alone, max_p L^{2k}|F̂_0(p)|/σ;
- R_ctr := L^{2k}|F̂_0(p*_0)|/σ, p*_0 the level-0 (0,1)-plaquette with base ((n-1)/2, (n-1)/2) in-plane and the middle
  site (n-1)/2 in each transverse direction (n = L^k), i.e. the fine plaquette at the centre of P.
Centre plaquettes p*_j at level j: the (0,1)-plaquette with base ((L^{k-j}-1)/2, (L^{k-j}-1)/2) in-plane and middle sites
(L^{k-j}-1)/2 transversally (p*_k = P).

Parts (σ = 1 throughout):
- **(A) aligned residual sources at every level.** For each i = 0, …, k - 1: s_i := σL^{-2(k-1-i)} times the
  counter-clockwise unit circulation on the four links of p*_{i+1} (so ds_i(p*_{i+1}) = 4σL^{-2(k-1-i)}: unit weighted size,
  the same sign at the same coarse point at every level), and s_i = 0 elsewhere; q_0 = 0. Depths: d = 2, k = 1, …, 5;
  d = 3, k = 1, 2, 3; d = 4, k = 1, 2 (information only).
- (A1, information) the same source at one level l only, for each l; (A2, information) independent random signs
  ±σL^{-2(k-1-i)} on every level-(i+1) box link, every level (numpy seed 3).
- **(B) rough level-0 plaquette source, d = 3 only, k = 1, 2, 3.** s ≡ 0; q_0 on (0,1)-plaquettes only:
  q_0(p) := σL^{-2k}·sign(3y_2² - |y|²), y := centre(p) - X*, X* := (n/2, n/2, (n-1)/2) (the extremal sign pattern of the
  Riesz transform ∂_2²Δ^{-1} at the centre).
- **(C) coarse-Lipschitz level-0 source (control), d = 3, k = 1, 2, 3.** As (B) with q_0(p) := L^{-2k}(3y_2² - |y|²)/n²;
  σ := max_p L^{2k}|q_0(p)| (its actual weighted sup).

Criteria:
- **Q1** every solve converged.
- **QA** (A) depth-flat, fine level and overall: d = 2: N_0(5) ≤ 1.10·N_0(3) + 0.05 and 𝔑(5) ≤ 1.10·𝔑(3) + 0.05;
  d = 3: N_0(3) ≤ 1.10·N_0(2) + 0.05 and 𝔑(3) ≤ 1.10·𝔑(2) + 0.05. (REVIEW_SQ_S1's prediction, linear growth, fails QA.)
- **QB** (B) grows (the CZ log is present at the fine level): R_ctr(3) ≥ 1.10·R_ctr(2) and R_ctr(3) - R_ctr(2) ≥ 0.05.
- **QC** (C) depth-flat: N_0(3) ≤ 1.10·N_0(2) + 0.05 (d = 3).
- Q4 (information) tables of 𝔑, N_0, R_ctr and the per-level weighted profiles; A1, A2; d = 4 (A).

OVERALL PASS iff Q1, QA, QB, QC all PASS (all four of the session-2 owner's predictions hold). Resources: numeric lock (one
mkdir, one rmdir), nice 10, threads 1, load < 8 at start, ≥ 25% free memory, peak footprint < 1 GB, python3 without -I, no
`timeout`, job < 20 min. Records: checks/q3_out.txt, checks/q3_time.txt.
