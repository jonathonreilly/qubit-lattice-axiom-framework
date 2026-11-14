# Check of gap-crux-exercise-astra.md, Sections 8.1 and 8.4

- Checker: Claude Opus 5.5. Date: 2026-11-11.
- Author of the checked text: Codex gpt-6-astra. Every statement marked HOLDS below is the author's result; credit is theirs.
- Read in full: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-crux-exercise-astra.md` lines 749-984 (8.1), 1194-1390 (8.4, 8.5). Background: `gap-crux-restate.md` line 31 (action convention: A = sum_p (1 - (1/2) tr U_p), sides >= 3; GC2 uses the same convention).
- Not read: `gap-seed-limit.md` (Lemma L / P'), `gap-skeleton-final.md` 13.18-13.19. The continuum passage in A4 is therefore not checked.
- Method: by hand. Guides only (pure Python, `python3 -I`, in this folder): `chk.py` (Monte Carlo of the Haar identity; ball volume; GC2 thresholds) and `geo.py` (the 8.1 interval cover for ell = 12, 13, 17 and several N; overlap, separation, and which pair types have a mixed vertex). These runs decide nothing.
- Not an independent check in the strict sense: same source text, one reader. My derivations are my own, done by hand.

## Verdict table

| Statement | Verdict |
|---|---|
| Cover (d,K,r) and the explicit cover of 8.1 | HOLDS |
| PA (definition) | HOLDS (well posed) |
| A1: PA => A^2 >= (1 - d eta) A, ker A = constants | HOLDS |
| A2: detectability bound q = (1 + gamma/d^2)^(-1/2) | HOLDS |
| A3: covariance identity and decay | HOLDS |
| A4: constants, lattice spectral exclusion | HOLDS (lattice part); continuum passage via Lemma L/P' NOT CHECKED |
| GC1 | HOLDS (read the right side as abs(mu_beta(x_p)); trivial) |
| GC2 | HOLDS; it is nontrivial only for beta >= about 12.7 |
| GC3 | HOLDS (the cutoff-trajectory clause is conditional on beta_h -> infinity) |
| GC4 (PA_g => A4; GC1 does not refute PA_g) | HOLDS; PA_g itself is open, and a gauge-invariant test near the same corner is not done (risk, Section 9) |
| Cover dependence | Mechanism needs a "mixed vertex"; present in every product cover of overlapping boxes with base-assigned links (opposite-sign diagonal pairs); not decided for all covers |

## 1. The cover and PA

Intervals [x_i - floor(2 s_(i-1)/3), x_i + floor(2 s_i/3)], s_i in [ell, 2 ell], ell >= 12, at least 12 intervals.

- Overlap of neighbours, in sites: 2 floor(2 s_i/3) - s_i + 1 >= s_i/3 - 1/3 >= 3.67, so at least 4 sites. The author's "length at least s_i/3 - 2 >= 2" is weaker and true. Guide: minimum 4 sites seen.
- Gap between intervals i and i+2: s_i - floor(2 s_i/3) + s_(i+1) - floor(2 s_(i+1)/3) >= (s_i + s_(i+1))/3 >= 8. Guide: minimum distance 8 seen.
- Cover: every point between x_i and x_(i+1) lies in interval i or i+1. Every site lies in a block, so every link (by its base) lies in a block.
- A plaquette spans two consecutive values in each coordinate. If two block indices differ by 2 or more in some coordinate, the gap of 8 separates them. So neighbours differ by at most 1 in every coordinate: d <= 80, greedy colouring K <= 81.
- Block side <= floor(2 s_(i-1)/3) + floor(2 s_i/3) <= 8 ell/3; with links and the one-plaquette collar the diameter is <= 8 ell/3 + 3 <= 3 ell + 2. HOLDS.
- PA: E_(B union C)^tau is the projection on constants of the fibre. If the true intersection of ran E_B^tau and ran E_C^tau were larger, the PA norm would be 1 on the difference, so eta < 1 already forces the intersection to be constants. PA is well posed. HOLDS.

## 2. A1

- Two projections P, Q with intersection R, k = ||PQ - R||: on ker R, ||P + Q|| = 1 + k (standard; the author's J-map argument is correct: J*J = P + Q, JJ* has identity diagonal blocks and off-diagonal block (P-R)(Q-R) of norm k). So S = (I-P) + (I-Q) >= 1 - k on ker R and 0 on ran R; S^2 >= (1-k) S; equivalently {I-P, I-Q} >= -k S. Checked.
- Fibrewise: E_B, E_C, E_(B union C) condition on sigma-algebras that contain the exterior of B union C, so they act fibre by fibre; the quadratic-form inequality integrates over tau. Checked.
- Non-interacting blocks: disjoint and no common plaquette, so given the exterior the conditional density factorizes and E_B, E_C commute; the anticommutator of commuting complementary projections is >= 0. Checked.
- A^2 = sum a_B + sum_(B<C) {a_B, a_C} >= A - eta sum_B deg(B) a_B >= (1 - d eta) A. ker A = constants by the product-Haar argument. HOLDS.

## 3. A2

I rebuilt the Anshu-Arad-Vidick step. With D = P_1 ... P_N (P_N applied first), Q_i = I - P_i: move Q_i to the right; past a commuting P_j drop P_j by contraction; at a non-commuting P_j use Q_i P_j X = Q_i X - Q_i Q_j X and ||Q_i Q_j X f|| <= ||Q_j X f|| = loss_j; stop at Q_i P_i = 0. So ||Q_i D f|| <= sum of at most d losses. Cauchy-Schwarz and the neighbour count give <v, A v> <= d^2 sum loss_j^2 = d^2 (||f||^2 - ||v||^2) (Pythagoras). D preserves mean zero; A >= gamma on mean-zero functions by A1. So ||v||^2 (1 + gamma/d^2) <= ||f||^2. HOLDS. Ordering inside a colour layer does not matter (those projections commute).

## 4. A3

- One update E_B either fixes the current function (B misses its support) or replaces the support by a subset of supp union (B with collar); B with collar has diameter <= r and meets the support, so the support grows by at most r. Same-colour blocks have disjoint collars from each other, so one layer grows it by at most r.
- A block acting nontrivially in layer j+1 <= kK lies within distance (j+1) r <= kKr of supp G, hence misses supp F when dist > kKr; for it, <F~, E_B h> = <E_B F~, h> = <F~, h>. So Cov(F,G) = <F~, D^k G~> exactly (no off-by-one). Then A2 gives q^k. HOLDS.
- Remark (not needed): the bound only needs G~ in a D-invariant subspace on which A2 holds; F may be arbitrary. This matters for GC4.

## 5. A4

- eta <= 1/160 gives d eta <= 1/2, gamma >= 1/2, gamma/d^2 >= 1/12800. -log q >= (1/2) log(1 + 1/12800).
- Rate per physical length: -log q / (K r h). With ell_h <= R/h + 1 and h <= R/12, (3 ell_h + 2) h <= 3R + 5h <= 4R. So m_h >= (1/2) log(1+1/12800) / (81 * 4R) = log(1+1/12800)/(648 R). The constant 648 = 2 * 81 * 4 is correct. HOLDS.
- The Laplace-transform argument (no spectral mass in [0, m_h)) is correct for a positive transfer matrix on the centred sector.
- NOT CHECKED: the passage through Lemma L / Proposition P' of `gap-seed-limit.md`.

## 6. GC1

Geometry (test 1). Let B have indices (i, j, k3, k4) and C have (i+1, j-1, k3, k4). Coordinate-1 intervals I_i = [a_i, b_i], I_(i+1) = [a_(i+1), b_(i+1)]; coordinate-2 intervals J_(j-1) = [c_(j-1), e_(j-1)], J_j = [c_j, e_j]. v = (a_(i+1), c_j, v3, v4), v3 and v4 at least one step inside the common intervals.

- v: coordinate 1 in I_i and I_(i+1) (overlap); coordinate 2 in J_j and J_(j-1) (overlap). v in B and C.
- z = v - e1: a_(i+1) - 1 is in I_i, not in I_(i+1). z in B only.
- w = v - e2: c_j - 1 is in J_(j-1), not in J_j. w in C only.
- u = v - e1 - e2: fails C in coordinate 1 and B in coordinate 2. Exterior.
- Links by base: U = (z, +1) in B \ C; V = (w, +2) in C \ B; A_0 = (u, +1): u -> w and B_0 = (u, +2): u -> z are exterior. Outgoing links at v have base v (in B and C); incoming links in directions 3, 4 have bases v - e3, v - e4 in B and C. So all eight links at v lie in the union, and a rotation at v fixes the exterior. Correct.
- Guide (`geo.py`): for ell = 12, 13, 17 and 12 values of N, the 2D enumeration finds a mixed vertex for offset (1,-1) and none for (1,1), (1,0), (0,1). This agrees with the author's 8.5 remark that opposite-sign offsets are essential.

Calculation.
- Rotation at v: U -> U k^-1, V -> V k^-1 (with U_xy -> g_x U_xy g_y^-1). The conditional law at fixed tau is invariant (Haar and the action are). The marginal of U, and of TV with T = B_0^-1 A_0 fixed, is right-invariant, so Haar. Then E_tau x(U) = 0, E_tau x(U)^2 = 1/4. Correct.
- Identity: chi * chi = chi/2 for the fundamental character of SU(2) and chi(S k^-1) = chi(k S^-1) (real character), so integral x(R k^-1) x(S k^-1) dk = (1/4) x(R S^-1). Correct. Guide: Monte Carlo agrees within noise (-0.0197 against -0.0191, noise about 0.0006).
- x(U (TV)^-1) = x(TV U^-1) (inversion) = x(B_0^-1 A_0 V U^-1) = x(A_0 V U^-1 B_0^-1) (cyclic) = x_p, with U_p the path u -> w -> v -> z -> u. Correct.
- E_C f = f (U not in C), E_B g = g (V and T not in B), E_(B union C) f = 0. So <g, (E_B E_C - E_(B union C)) f> = E(fg) = mu_beta(x_p)/4, with ||f|| = ||g|| = 1/2. Hence the norm is >= abs(mu_beta(x_p)). HOLDS.
- Note: the same computation at fixed tau gives the fibre statement ||E_B^tau E_C^tau - E_(B union C)^tau|| >= abs(E_tau x_p) for every tau. That is the form PA quantifies directly.

## 7. GC2 (test 2)

- Haar density of the class angle theta on SU(2): (2/pi) sin^2 theta. For delta <= 1, sin theta >= theta/2, so the ball volume >= (2/pi) delta^3/12 = delta^3/(6 pi) >= delta^3/24 (pi <= 4). Correct (crude; guide: true ratio about 4).
- theta is the bi-invariant geodesic distance to I on S^3, so theta(U_p) <= 4 delta and 1 - x_p = 1 - cos theta_p <= theta_p^2/2 <= 8 delta^2. Correct.
- Z >= (delta^3/24)^(N_e) exp(-8 beta delta^2 N_p). With delta = beta^(-1/2) <= 1 (beta >= 1): -log Z <= N_e (log 24 + (3/2) log beta) + 8 N_p. Correct.
- F = -log Z: F(0) = 0, F' = mu_beta(A), F'' = -Var(A) <= 0. Concavity gives 0 = F(0) <= F(beta) - beta F'(beta). Correct.
- Divide by beta N_p, N_e/N_p = 4/6 = 2/3: average of 1 - mu(x_p) <= [(2/3) log 24 + log beta + 8]/beta. Translation and axis permutations of the cubic torus make every plaquette mean equal. HOLDS, uniformly in N. Side >= 3 is more than needed; harmless.
- Size: the constant is 8 + (2/3) log 24 = 10.119. The bound is below 1 only for beta >= about 12.66, below 79/80 (i.e. mu > 1/80) for beta >= about 12.84 (guide). So the rigorous obstruction bites only at beta above about 13. This does not affect GC3, which is a large-beta statement.

## 8. GC3 (test 3)

- The global operator E_B E_C - E_(B union C) is the direct integral over tau of the fibre operators (Section 2), so its norm is the essential supremum of the fibre norms. PA's every-tau bound gives global norm <= eta. Simpler: the fibre form of GC1 gives abs(E_tau x_p) <= eta for every tau, and averaging gives abs(mu(x_p)) <= eta.
- With GC2, mu(x_p) > eta once [log beta + 10.119]/beta < 1 - eta. Contradiction. HOLDS for every fixed eta < 1, at every R and ell >= 12 (the corner pair exists in every such cover), on all sufficiently large tori.
- The clause "along a Wilson cutoff trajectory with beta_h -> infinity" is conditional on beta_h -> infinity, which is an input (asymptotic freedom), not proved here. The author states it as a hypothesis; correct as written.
- The author's scope statement (refutes only this full-L^2 PA; not B7, W or GAP; does not show the sum A has a small gap) is correct.

## 9. GC4 (test 4)

- Gauge action at vertices whose incident links all lie in the union: each link variable is mapped to a function of itself, the exterior is fixed, and the conditional law is invariant. So sigma(links outside B) is stable, and E_B, E_C commute with the action. The invariant subspace is preserved; constants are invariant. Correct.
- Globally gauge-invariant functions restrict to invariant fibre functions (a.e. tau). The two-projection lemma holds on the invariant subspace of each fibre. Integration gives A^2 >= (1 - d eta) A as forms on the global invariant subspace H_G, and A preserves H_G (global gauge maps commute with every E_B). A2 holds on H_G (D preserves it). A3 needs only G~ in H_G. Gauge-invariant scalar tests lie in H_G. HOLDS (continuum passage not checked, as in A4).
- Does PA_g escape GC1? Yes, and more strongly than stated. At v, U is the only incident link not in C (outgoing links and directions 3, 4 are in B and C, V is in C). A function in ran E_C invariant under the rotation at v is invariant under U -> U k^-1 for all k, so it does not depend on U. Likewise a function in ran E_B invariant at v does not depend on V. So no admissible pair can use the vertex v at all. GC1's mechanism is excluded, not only its two test functions.
- Risk, not a verdict on PA_g. PA_g still admits functions that are not invariant at boundary vertices of the union. Example: z and z + e3 are boundary vertices (B_0 and (u + e3, +2) are exterior). The (2,3)-plaquette at u has one link (z, +3) in B \ C and three exterior links; the (1,3)-plaquette at u has one link (w, +3) in C \ B and three exterior links. Their traces are fully gauge invariant and lie in ran E_C and ran E_B respectively. Their conditional correlation is not estimated anywhere. At weak coupling the conditional law is close to Gaussian, where normalized short-distance correlations of such local invariants do not go to zero as beta grows. If such a correlation exceeds 1/160 on some fibre, PA_g fails for a gauge-invariant reason. I did not compute it. This is a concrete next test for PA_g, not a refutation.

## 10. Does the obstruction depend on the cover?

- What the argument uses: an interacting pair B, C and a vertex v such that all links at v lie in B union C, one link at v lies in B \ C, and another lies in C \ B ("mixed vertex"), plus a closing path made of links not in C on one side and not in B on the other. With a plaquette closing path one gets GC1 as written. With a longer closing loop the same calculation gives abs(mu(x(loop))) and, at fixed lattice loop, a lasso/triangle-inequality bound makes it tend to 1 as beta -> infinity (my sketch; not checked in detail).
- In this cover, with links assigned by base: mixed vertices occur exactly for opposite-sign diagonal pairs; face pairs and same-sign diagonal pairs have none (by hand, confirmed by the guide). Every product cover of overlapping boxes with base-assigned links has opposite-sign diagonal pairs (they overlap, so they interact) and thus a mixed vertex. Non-overlapping box partitions have mixed vertices already at face pairs.
- So the obstruction is not special to the chosen interval lengths; it applies to every overlapping product-box cover of this kind. I have not decided whether some other cover (different link assignment or block shapes) can avoid mixed vertices for every interacting pair.

RESULT: All statements of 8.1 (cover, PA, A1-A4 lattice part) and 8.4 (GC1, GC2, GC3, GC4) HOLD as written, credit to Codex gpt-6-astra; GC1 should read abs(mu_beta(x_p)) (trivial), GC2 bites only for beta >= about 12.7, A4's continuum passage was not checked, and PA_g remains open with an unevaluated gauge-invariant corner test (boundary plaquettes at u) as the next risk.
