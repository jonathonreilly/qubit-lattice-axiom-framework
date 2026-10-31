# p2 criteria (lane E session 2; written 2026-10-27 23:40 UTC, before checks/p2_pld.py exists)

Scope: the abelian linear block map and elementary arithmetic used by PLD.md §14. Nothing about SU(N) measures, the
chessboard lemmas or Lemma CONE is tested.

A (straight-flux identity, Lemma LC's representation). d = 4, L = 3, coarse torus sides T = 2 and T = 3 (fine side LT).
Random real 1-form A on the fine torus (3 seeds). Compute (d Q_str A)(P) for every coarse plaquette P from the definition
(Q_str A)(X, mu) = L^{-4} sum_{y in B(X)} sum_{j<L} A_mu(y + j e_mu), and sum_q w_P(q)(dA)(q) with
w_P(q) = L^{-4} m(z_mu) m(z_nu) (q of orientation (mu, nu), z its base point relative to the block origin of X,
0 <= z_mu, z_nu <= 2L - 2, z_perp in the block, m(t) = min(t + 1, 2L - 1 - t)).
PASS iff max |difference| <= 1e-12 (scaled by max |dQ_str A|). Also sum_q w_P(q) = L^2 and
sum_q w_P(q)^2 = (2L^2 + 1)^2/(9L^4) = 361/729 to 1e-14. FAIL otherwise.

B (projected weight norm; informational with one PASS condition). ||Pi w_P||^2 with Pi the orthogonal projector onto
im d (fine level), computed by solving d^T d x = d^T w (sparse CG, tolerance 1e-12) and Pi w = d x. PASS iff
||Pi w_P||^2 <= 361/729 + 1e-9 and Pi w_P satisfies ||d^T(w - Pi w)|| <= 1e-8 ||w||. Report the value (T = 2, 3).

C (flow arithmetic, Proposition GR). Sequences 1/g_j^2 = 1/g_k^2 + b(k - j) log L with b in {beta_-, beta_+} =
{0.3, 0.45} and one sequence with per-level increments drawn uniformly in [beta_-, beta_+] log L; g_k^2 in {0.05, 0.2};
k in {10, 10^2, 10^3, 10^4, 10^5}; c = theta beta_- log L, theta in {0.5, 1, 1.5}.
Compute P_k := prod_{j<k}(1 + c g_j^2) and R_k := g_0^2 P_k / g_k^2.
PASS iff (C1) P_k <= (g_k^2/g_0^2)^theta for every case (the proven upper bound); (C2) for theta <= 1, R_k <= 1 for every
case; (C3) for theta = 1.5 on the b = beta_- sequence, R_k is increasing in k and R_{10^5}/R_{10^4} is within 20% of the
predicted ratio ((1 + beta_- 10^5 log L g_k^2)/(1 + beta_- 10^4 log L g_k^2))^{0.5}; (C4) Sum_j g_j^4 <= g_k^2/(beta_- log L)
+ g_k^4 for every case.

D (one-loop arithmetic used in §14.1 and §14.4). beta_1(N) := 11N^2/(12 pi^2). PASS iff floor(4/(a'' beta_1(2))) = 382 with
a'' = 0.9 eps_1^2/(4N), eps_1 = 0.5, N = 2 (RLARGE's n_* = 382) and the same formula gives 255 for N = 3. Report
log(24 L^4)/log L at L = 3 and the smallest N with (2/N) 4 beta_1(N) > log(24 L^4)/log L (informational).

E (tail integration, Proposition PLD-AF (ii)). For (a, C, p) in {(0.1, 1, 0), (1/(4*117^2), 10, 8), (0.25, 1e3, 3)},
g in {0.05, 0.1, 0.3}, eps_1 in {0.5, 2}: with the tail profile P(X >= t) = min(1, C g^{-p} e^{-a t^2/g^2}) for t <= eps_1
and = min(1, C g^{-p} e^{-a eps_1^2/g^2}) for eps_1 < t <= 2, compute E X^2 = int_0^2 2t P(X >= t) dt numerically
(scipy quad or a 10^6-point midpoint rule). PASS iff the closed form (g^2/a)(1 + log_+(C g^{-p})) + 4 C g^{-p} e^{-a eps_1^2/g^2}
is >= the numerical value in every case (and min(closed form, 4) is reported).

Resource rules: numeric lock, nice 10, OPENBLAS/OMP/MKL threads 1, load < 8, memory >= 25% free, peak < 1 GB. One run;
any rerun is recorded with the reason in checks/p2_time.txt.
