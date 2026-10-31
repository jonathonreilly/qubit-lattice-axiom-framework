# f1 criteria (written 2026-10-27 23:07 UTC [file mtime], before checks/f1_tree_soft.py)

Object. One step of the u-stripped soft chain, linearised at the trivial background (one colour; this is the Hessian of
the nonlinear tree functional 𝒯_{k+1} at V = 1 by the envelope theorem). Fine energy ½Σ_p(dA)_p², kernel
(κ/2)Σ_c|b_c - (Q_rootA)_c|², Q_root = the S4' root map (LINEAR_PACKAGE §1.2: average over the 24 orders σ and the L⁴
block sites y of the contour T^σ_y = P^σ(c_X→y)·S_y·P^σ(c_{X+μ}→y+Le_μ)^†). Tree form T(b) := min_A. Per coarse momentum p,
with fine aliases q_K = (p + 2πK)/L, Q̃_K := e^{iq_K·o}Q̂(q_K) (o = ((L-1)/2)(1,1,1,1)), D̂(q) := |ŝ|²1 - ŝŝ^†,
ŝ_α = e^{iq_α} - 1:
- direct: T̂ = κ1 - κ²Q̃(L⁴D_blk + κQ̃^†Q̃)^+Q̃^†;
- transverse: T̂_⊥ = (κ^{-1}P_⊥ + S)^{-1} on the coarse transverse space, S = L^{-4}P_⊥Σ_KQ̃_KP_T(q_K)Q̃_K^†P_⊥/|ŝ(q_K)|².
Coarse reference D̂_c(p) = |ŝ_c|²P_⊥ (the form Σ_p(dB)_p² on the coarse lattice).

Pre-registered criteria (L = 3, κ ∈ {0.25, 1, 4, 16} unless stated; directions n ∈ {(1,0,0,0), (1,1,0,0)/√2,
(1,2,3,4)/√30}):
- (G) root covariance Q̂(q)ŝ(q) = ŝ_c(Lq) at 20 random q: max error ≤ 1e-12. Normalisation Q̂(0) = L·1: error ≤ 1e-12.
- (A) direct T̂: Hermitian to ≤ 1e-12·||T̂||; ||T̂ŝ_c|| ≤ 1e-9·||T̂||·|ŝ_c|; axis-permutation covariance
  T̂_{πμ,πν}(πp) = T̂_μν(p) for 5 random permutations and p: ≤ 1e-10·||T̂||. At p ∈ {0.3n, 0.7n, 1.5n'} with n' generic.
- (B) direct and transverse formulas agree on the transverse space: ≤ 1e-8 relative, same p as (A).
- (C) marginal coefficient: the three transverse eigenvalues of T̂_⊥(tn)/|ŝ_c(tn)|² at t = 0.01 lie within 1e-3 of 1,
  and their Richardson limit (from t = 0.02, 0.01, assuming an O(t²) correction) is within 1e-5 of 1, for every κ and n.
  Also at L = 5, κ = 1 (transverse formula only).
- (D) remainder O(p⁴): r(t) := ||T̂_⊥(tn) - D̂_c(tn)||; r(0.1)/r(0.05) ∈ [14, 18] for every κ and n (with r ≥ 1e-12).
- (E) tree background aliases: a_K := L^{-4}D̂(q_K)^+Q̃_K^†T̂_⊥b (b a unit transverse vector), curvature
  c_K := ||ŝ(q_K)∧a_K||; c(t) := max_{K≠0}c_K at p = tn. c(0.02)/c(0.01) ∈ [7, 9] (aliases O(p³)), every κ and n.
- (F) informational with a pass line: λ_𝒬 := L^{-4}max_pΣ_K||Q̃_K(p)||²_op over a 6⁴ midpoint grid of p; PASS if
  λ_𝒬 < 1/2 (the contraction used by Lemma F-depth).

Outcome recorded in checks/f1_out.txt and checks/f1_time.txt; FLOW.md §12 points here. A FAIL is reported as a FAIL.
