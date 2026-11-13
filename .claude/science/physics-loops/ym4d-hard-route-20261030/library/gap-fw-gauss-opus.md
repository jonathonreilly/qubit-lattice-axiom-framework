# FINISH row 903: (WALL-1) and (WALL-2) in the lattice free massive scalar (and Maxwell/Proca) with periodic time and free space walls

Author: Claude Opus 5.5 (high effort), by hand; numerics labelled GUIDE.
Clone: /Users/jonreilly/ym4d-lead/clone at 4c53df409a5b061cd32f73708dcb489a5f1e66e4 (pulled 2026-11-13, already up to date).
Source read: D/library/gap-next3-max.md lines 396-458 (6.1 FW1-FW4, 6.3 FW5, FW6, WALL-1, WALL-2) and 476-490 (attack 1, GUIDE estimate), D = .claude/science/physics-loops/ym4d-hard-route-20261030. Row 898 is unchecked (its check is row 902); I use only its definitions and the algebra of FW5/FW6, which I re-derive in the free field.

## Plan
1. Model and boundary condition: which scalar wall matches the Wilson free wall; normalisation invariance of g, p, c, gamma, delta_e.
2. Mode reduction: every FW5 term as a sum over transverse modes of one-dimensional Fourier data; image (Poisson) formula; exact closed forms.
3. Positivity: signs of the Fourier coefficients (complete monotonicity); propagator representation of p and delta_e.
4. (WALL-1): exact best constant (Neumann); Dirichlet variant.
5. (WALL-2): rigorous bound by a propagator comparison; best constant (GUIDE numerics for the supremum).
6. Maxwell / Proca (natural cellular walls): tower decomposition; what carries over.
7. GUIDE computation: direct 4D determinants against the formulas; scan of the two ratios.
8. Meaning for the engine; RESULT.

## Step 1. Model, boundary condition, normalisation (PROVED unless marked)

Box: time t in Z_a (periodic); space x = (x_1, x_2, x_3) with x_1 in {1..b}, x_2 in {1..c}, x_3 in {1..d}. Free massive scalar, weight exp(-S) prod dphi_x/sqrt(2 pi),
  S = (1/2) sum over bonds <xy> with both ends in the box of (phi_x - phi_y)^2 + (m^2/2) sum_x phi_x^2,  m > 0.
No bond leaves the box. The spatial operator is the graph Laplacian of the induced subgraph: this is the lattice NEUMANN wall. The mass term is the same on every site.

Which wall matches the Wilson free wall. The Wilson free wall keeps the a-priori measure (Haar, flat, no on-site term) and deletes the plaquettes that leave the box. In the Gaussian (weak-coupling) limit U = exp(iA), Haar is flat in A and exp(beta x_p) = e^beta exp(-(beta/4)|F_p|^2 + ...). Deleting plaquettes then gives the natural (cellular) boundary condition of the box complex, times a constant e^beta per plaquette. For the scalar the same recipe (flat a-priori measure, delete the bonds that leave) is the Neumann wall. The DIRICHLET wall (phi = 0 outside) corresponds to a fixed Gaussian on-site measure exp(-(8 + m^2) phi^2/2) with only the cross terms phi_x phi_y in the bonds; on SU(2) the two recipes coincide because the "on-site" part of a plaquette is constant (|U| = 1), but in a non-compact field they differ, and the Gaussian limit of Wilson selects Neumann (for the gauge field: the natural cellular wall, Step 6). Dirichlet is computed below only as a robustness variant. ANSWER: Neumann matches the Wilson free-wall box.

Sign of FW2 and normalisation. For Neumann, Z(b_1 + b_2)/(Z(b_1) Z(b_2)) = E_prod[exp(-(1/2) sum_cross (phi_x - phi_y)^2)] is at most 1: the bare Gaussian is SUB-multiplicative (FW2 fails as stated). A constant factor e^kappa per bond with kappa at least (1/2) max E(phi_x - phi_y)^2 restores FW2 by Jensen, exactly as the factor e^beta per plaquette does for Wilson. The number of bonds per time step in a box with free side b is n(b) = (b-1)cd + b(c-1)d + bc(d-1) + bcd, affine in b. So a per-bond (or per-site) constant changes log W(a, b) by a kappa n(b) and e(b) by kappa n(b). Hence:
  g, p, c, gamma, delta_e are independent of the normalisation; only f and D_inf move.
Below I use the bare normalisation and the definitions f := lim e(b)/b, D(b) := f b - e(b), D_inf := lim D(b), delta_e(b) := D_inf - D(b). When FW2 holds these coincide with FW3's sup-definitions. FW5 and FW6 use only e(b) = f b - D_inf + delta_e(b) with delta_e -> 0, delta_e at least 0, and r_k at most r_0, so they hold verbatim (delta_e at least 0 is shown in Step 3).

## Step 2. Mode reduction and exact closed forms (PROVED)

Neumann path with b sites: eigenvalues lambda(theta) = 2 - 2 cos theta, theta in Theta^N_b = {pi k/b : k = 0..b-1}, eigenvectors cos(theta (x - 1/2)). Spatial modes K = (theta, T), theta in Theta^N_b, T = (theta_2, theta_3) in Theta^N_c x Theta^N_d, transverse mass M_T^2 = m^2 + lambda(theta_2) + lambda(theta_3), at least m^2. Mode energy omega_T(theta) > 0:
  cosh omega_T(theta) = 1 + (M_T^2 + 2 - 2 cos theta)/2.
Periodic chain identity: prod_{j=0}^{a-1} (mu^2 + 2 - 2 cos(2 pi j/a)) = 2 cosh(a omega) - 2 = (2 sinh(a omega/2))^2, cosh omega = 1 + mu^2/2. Hence (bare normalisation)
  log W(a, b) = - sum_K log(2 sinh(a omega_K/2)),  e(b) = -(1/2) sum_K omega_K,  g(a, b) = sum_K F_a(omega_K),  F_a(omega) = -log(1 - e^(-a omega)),
and the time transfer M_b has spectrum exp(-sum_K (n_K + 1/2) omega_K), n_K at least 0 (product of oscillators).

Image (Poisson) formula. For h even, 2 pi-periodic, analytic, with hat h(n) = (1/2pi) int_{-pi}^{pi} h cos(n theta) d theta: sum_{k=0}^{2B-1} h(pi k/B) = 2B sum_{j in Z} hat h(2Bj), and the 2B-sum equals 2 sum_{k=0}^{B-1} h(pi k/B) - h(0) + h(pi). Therefore
  (N)  sum_{k=0}^{b-1} h(pi k/b) = b hat h(0) + (h(0) - h(pi))/2 + 2b sum_{j>=1} hat h(2bj),
  (E)  sum_{k=1}^{b-1} h(pi k/b) = b hat h(0) - (h(0) + h(pi))/2 + 2b sum_{j>=1} hat h(2bj),
  (D)  sum_{k=1}^{b} h(pi k/(b+1)) = (b+1) hat h(0) - (h(0) + h(pi))/2 + 2(b+1) sum_{j>=1} hat h(2(b+1)j).
(E) is the edge spectrum of the path (needed in Step 6); (D) is the Dirichlet path.

Apply (N) with h = omega_T, h = F_T := F_a o omega_T, h = H_T := F_T - (a/2) omega_T = -log(2 sinh(a omega_T/2)), and sum over T. Exact results for the Neumann box (every m > 0 and every a, b, c, d at least 1):
  f = -(1/2) sum_T hat omega_T(0);   D_inf = (1/4) sum_T [omega_T(0) - omega_T(pi)]  (bare normalisation; NEGATIVE, see Step 1);
  delta_e(b) = - b sum_T sum_{j>=1} hat omega_T(2bj);
  p(a) = sum_T hat F_T(0) = sum_T (1/pi) int_0^pi F_a(omega_T(theta)) d theta;
  W_N(a) := (1/2) sum_T [F_T(0) - F_T(pi)];
  g(a, b) = b p(a) + W_N(a) + 2b sum_T sum_{j>=1} hat F_T(2bj);
  eps(a) = sum_T hat H_T(0),  omega(a) = eps(a) + (1/2) sum_T [H_T(0) - H_T(pi)],  gamma(b, a) = 2b sum_T sum_{j>=1} hat H_T(2bj);
  c(a) = omega(a) - a (f - D_inf) = p(a) + W_N(a).
Checks. (i) p(a) = eps(a) - a f (FW5 (i)) because H_T + (a/2) omega_T = F_T. (ii) gamma - a delta_e = 2b sum sum [hat H_T + (a/2) hat omega_T](2bj) = 2b sum sum hat F_T(2bj), so (b - 1) p + c + gamma - a delta_e = b p + W_N + 2b sum sum hat F_T(2bj) = g: FW5 (ii) holds identically. (iii) The split of log W = sum_T sum_k H_T into (linear in b) + (constant) + (terms tending to 0) is unique, so gamma above is FW5's log(1 + S_W).
Reading: W_N is the thermal sum of the wall modes (the theta = 0 end of each tower; the theta = pi end is a lattice term); the j-sums are images at distance 2bj.
Dirichlet (all three space directions): replace (N) by (D): g_D = (b+1) p_D - W_D + 2(b+1) sum sum hat F_T(2(b+1)j) with W_D = (1/2) sum_T [F_T(0) + F_T(pi)], delta_e^D(b) = -(b+1) sum_T sum_j hat omega_T(2(b+1)j), T over Theta^D_c x Theta^D_d.

## Step 3. Propagator representation and positivity (PROVED)

Let G_s(t, x) = int int_{[-pi,pi]^2} e^{i(k t + theta x)} / (s + 4 - 2 cos k - 2 cos theta) dk dtheta/(2pi)^2 be the Z^2 lattice propagator with mass^2 s > 0. Facts: G_s > 0 (random-walk expansion); G_s(t, x) = G_s(x, t); doing the k-integral, G_s(t, x) = (1/2pi) int e^{i theta x} e^{-|t| omega_s(theta)} / (2 sinh omega_s(theta)) d theta with cosh omega_s = (s + 4 - 2 cos theta)/2; so t -> G_s(t, 0) is strictly decreasing in |t| and is a positive mixture of exponentials. Note omega_T = omega_{M_T^2}.
Differentiate in s: d omega_s/ds = 1/(2 sinh omega_s). Hence d hat omega(n)/ds = G_s(0, n); dF_a/ds = -a sum_{r>=1} e^{-r a omega}/(2 sinh omega), whose n-th coefficient is -a sum_{r>=1} G_s(ra, n); dH/ds = -(a/2) coth(a omega/2)/(2 sinh omega), coefficient -(a/2) sum_{r in Z} G_s(ra, n). As s -> infinity, omega_s = log s + (4 - 2cos theta)/s + O(s^-2) uniformly and F_a -> 0, so the non-constant coefficients of omega and all coefficients of F_a, H (n at least 1) vanish there; G_s(t, n) is O(s^-(|t|+|n|+1)), so the integrals converge. Therefore, for n at least 1 (and n = 0 in R2):
  (R1) -hat omega_T(n) = int_{M_T^2}^inf G_s(0, n) ds > 0;
  (R2) hat F_T(n) = a int_{M_T^2}^inf sum_{r>=1} G_s(ra, n) ds > 0;
  (R3) hat H_T(n) = (a/2) int_{M_T^2}^inf sum_{r in Z} G_s(ra, n) ds > 0.
Consequences (Neumann box, exact):
  delta_e(b) = b sum_T sum_{j>=1} int_{M_T^2}^inf G_s(2bj, 0) ds   (positive; non-increasing in b, since b sum_j e^{-2bj w} = b/(e^{2bw} - 1) decreases);
  p(a) = a sum_T int_{M_T^2}^inf sum_{r>=1} G_s(ra, 0) ds;
  gamma(b, a) = a b sum_T sum_{j>=1} int sum_{r in Z} G_s(ra, 2bj) ds   (positive, non-increasing in b);
  g - b p - W_N = 2ab sum_T sum_{j>=1} int sum_{r>=1} G_s(ra, 2bj) ds   (positive);
  W_N > 0 because theta -> F_a(omega_T(theta)) is strictly decreasing on [0, pi].
Reading: p is the propagator wound r times around the time circle, integrated over the mass; delta_e is the propagator between a wall and its images at distance 2bj, integrated over the mass (the lattice Casimir term). The time-space symmetry of the 2D propagator, G_s(0, n) = G_s(n, 0), is what makes the two comparable.

## Step 4. (WALL-1) (PROVED for Neumann; Dirichlet in Step 7)

Theorem W1 (Neumann). For every m > 0 and all a, b, c, d at least 1:
  b p(a) < g(a, b),  precisely  g(a, b) - b p(a) = W_N(a) + 2ab sum_T sum_{j>=1} int sum_{r>=1} G_s(ra, 2bj) ds > 0.
Elementary second proof: for each T, theta -> F_a(omega_T(theta)) is decreasing on [0, pi], and sum_{k=0}^{b-1} F_T(pi k/b) (pi/b) is its left Riemann sum, which is at least int_0^pi F_T.
So (WALL-1) holds with C_1 = 1. Best constant: C_1* = sup b p/g = 1, because at fixed a, c, d, m the ratio g/(b p) = 1 + (W_N + corner)/(b p) tends to 1 as b -> infinity (the corner term tends to 0, W_N is fixed). Not attained.
Also: the thermal wall term is positive, c(a) = p(a) + W_N(a) > p(a) > 0, so FW5's lower-bound reading of (WALL-1) holds with nothing to spare and nothing lost.

## Step 5. (WALL-2) (PROVED for Neumann, every m > 0, every c, d)

Theorem W2. For all integers a, b at least 1 with a at most 2b, all c, d, and every m > 0, with k := floor(2b/a):
  a delta_e(b) at most b p(a)/k  <  g(a, b)/k.
In particular, on the engine's domain a at most b/2 (k at least 4): a delta_e(b) at most g(a, b)/4, so C_2 = 1/4 works.
Proof. Fix T. By Step 3,
  a delta_T(b) = a b int ds sum_{j>=1} G_s(2bj, 0),   b P_T(a) = a b int ds sum_{r>=1} G_s(ra, 0).
G_s(., 0) is decreasing. For r in {(j-1)k + 1, ..., jk} we have r a at most j k a at most 2bj, so G_s(ra, 0) at least G_s(2bj, 0). Summing, sum_{r>=1} G_s(ra, 0) at least k sum_{j>=1} G_s(2bj, 0) for every s. Integrate over s at least M_T^2, sum over T, and use Theorem W1. QED.
The proof uses three things only: positivity of the 2D propagator, its monotone decay on an axis, and the exchange symmetry G_s(0, n) = G_s(n, 0) between the time axis and the free axis. The bound is uniform in m, c, d: no constant grows with a, b or 1/m.
Best constant (C_2*). Asymptotic values (continuum, GUIDE-level, consistent with row 898's estimate): in the 4D massless regime a delta_e/g is about (1/16)(a/b)^4 (1/256 at a = b/2); for one transverse tower with M_T b small it is about (a/b)^2/4 (1/16 at a = b/2); for M_T b large it is exponentially small, at most of order a e^{-(2b - a) M_T}. Step 7 scans the exact lattice ratio.

## Step 6. Proca and Maxwell with natural (cellular) walls

Wall. The gauge field lives on the cell complex of the box (time a cycle, space three paths); every plaquette inside the box is kept, none leaves. This is the Gaussian limit of the Wilson free wall (Step 1).
Hodge Laplacian on 1-forms of the product complex is diagonal in the component mu: Delta^(mu) = L^E_mu + sum_{nu != mu} L^V_nu (edge Laplacian in the own direction, vertex (Neumann) Laplacian in the others). On the cycle L^E and L^V are isospectral. On the path with b vertices L^E has spectrum Theta^E_b = {pi k/b : k = 1..b-1}.
Proca (PROVED): with S = (1/2)|dA|^2 + (m^2/2)|A|^2 and the Hodge decomposition (H^1 = time cycle only),
  Z = m^(-N_0) prod_{mu=0}^{3} det(Delta^(mu) + m^2)^(-1/2) det(Delta_0 + m^2)^(1/2) = m^(-N_0) prod_{i=1}^{3} det(Delta^(i) + m^2)^(-1/2),
because Delta^(0) is isospectral to Delta_0 (time direction is a cycle): the time component cancels the ghost exactly. m^(-N_0) is a per-site constant (Step 1). So Proca = three scalar towers: tower 1 has the EDGE spectrum (E) in the free direction b and Neumann transverse modes (including T = (0,0) with M_T = m); towers 2, 3 have Neumann in direction b and one edge factor transversally. GUIDE check of this formula against the direct 1-form determinant: agreement to 1e-13 (Step 7, A2).
Maxwell (ARGUED: Gaussian limit of the Gauss-law-projected transfer matrix; zero-mode bookkeeping not written): physical modes = co-exact spatial 1-forms. As multisets of spatial modes K = (k_1, k_2, k_3) on the grids pi k/side: multiplicity 2 if all k_i at least 1, 1 if exactly one k_i = 0, 0 otherwise. In the b-direction: for T with k_2, k_3 at least 1, one N-tower and one E-tower; for T with exactly one zero, one E-tower; T = (0,0) absent. Every tower has M_T > 0, so m = 0 is allowed.
What carries over (PROVED, given the mode formulas): the tail formula (E) has the same image term 2b sum_j hat h(2bj) as (N). Hence each tower has the same delta_T(b) and P_T(a) as a Neumann tower with the same M_T, and Theorem W2 holds tower by tower:
  a delta_e(b) at most b p(a)/floor(2b/a)  (Proca, Maxwell, and Dirichlet with b+1 in place of b).
What does not carry over: an E-tower (and the Dirichlet tower) has the wall term -(1/2)[F_T(0) + F_T(pi)] < 0, so g at least b p fails in general and C_1 must be above 1. I have no hand proof of a uniform C_1 for E-towers (the Riemann bound g_E at least (b/pi) int_{pi/b}^{pi} F_T loses a slab whose share I did not bound uniformly); Step 7 gives the GUIDE values. The worst case is the light E-tower T = (0,0) of Proca as m -> 0 (it has no zero mode to inflate g).

## Step 7. GUIDE computations (scripts guide_checks.py, guide_scan.py, guide_refine.py, guide_shape.py in this directory; logs scan_*.log, refine.log, shape.log; each run under 1 min, under 100 MB)

A. Direct dense 4D determinants (Neumann and Dirichlet; boxes up to 6x5x4x4) against the oscillator formula (spatial eigenvalues from eigvalsh) and against the analytic theta-grid: agreement to 4e-13 in log W.
A2. Proca on the cellular complex, direct 1-form determinant det(d1^T d1 + m^2) against the three-tower formula: agreement to 1e-13 (3 boxes).
B. delta_e for one tower three ways: e(b) - f b + D_inf from the eigenvalue sum; the image tail; the propagator integral (R1), truncated at j at most 5. First two agree to 1e-10 relative; (R1) agrees up to its truncation (e.g. M_T^2 = 0.09, b = 8: 2.49419e-4 all three).
C. Scan of R1 = b p/g and R2 = a delta_e/g on 3 at most a at most b/2, b in {6,...,96}, c, d at least b (up to 16 b), m from 1e-4 to 1 (configurations where delta_e is below floating-point resolution are excluded from R2; there R2 is tiny by Theorem W2 and the massive asymptotics):

| model (wall) | sup R1 found | sup R2 found | where | max of floor(2b/a) a delta_e/(b p) (W2 says < 1) |
|---|---|---|---|---|
| scalar, Neumann (matches Wilson) | 0.970 (< 1, PROVED) | 0.0116 | a = b/2, c = d = b, m b about 0.1; stable for b = 16..96 | 0.119 |
| scalar, Dirichlet | 1.53 (b = 64, c = d = 2b); continuum hand limit about 1.70 at a = b/2 | 0.0031 | a = b/2, c = d large, m -> 0 | 0.0025 |
| Proca, natural walls | 1.225 | 0.023 | a = b/2, c = d = b, m -> 0 (light E-tower) | 0.071 |
| Maxwell, natural walls (m = 0) | 1.264 (c = b, d = 16b; slowly rising with d/b) | 0.007 | a = b/2, c = b, d large | 0.014 |

Continuum hand value for Dirichlet (GUIDE): massless, transverse sides infinite, plate distance L = b + 1, x = a/L: R1 = 2 zeta(4)/(pi x sum_{n>=1} J(pi n x)), J(u) = sum_r e^{-ru}(u/r^2 + 1/r^3); at x = 1/2 this is 1.70; R1 -> 1 as x -> 0.
No ratio grows with a, b, c, d or 1/m in any of the four models; R2 stays two orders below the proved 1/4.

## Step 8. What this means for the engine

1. The free massive scalar with the wall that matches Wilson (Neumann) satisfies both inequalities with absolute constants, proved for every m > 0, every a at most 2b and every c, d: C_1 = 1 (best, not attained), C_2 at most 1/floor(2b/a), at most 1/4 on a at most b/2 (true supremum about 0.012, GUIDE). In this model FW6 with h = b gives g(a, 2b) at most 2.25 g(a, b); directly, g(a, 2b) at most 2 g(a, b) (W_N at least 0, and the corner term at 2b is at most twice the one at b because G_s(t, x) is non-increasing in |x| at fixed t: reflect a walk to (t, x+1) after its first crossing of the line x + 1/2, which injects it into the walks to (t, x)). So the free field does NOT kill the engine. It is evidence only, as the task says.
2. The variants (Dirichlet, Proca, Maxwell) also pass, with C_1 between 1.2 and 1.7 (GUIDE) and the same proved W2 bound against b p. A wall term of either sign is harmless: C_1 is an absolute constant in all four.
3. Where the free-field proof gets its strength, and why it does not port as is. The proof of W2 compares one propagator at the winding points ra on the time axis with the same propagator at the image points 2bj on the free axis. It needs (i) the image identity: the Neumann box of side b is the reflection-even sector of the periodic box of side 2b, so the free wall acts as a mirror and delta_e is a sum over image distances; (ii) mode-by-mode factorisation of log W, so the wall-vector overlap, which is exponentially small in the wall area, cancels inside logarithms; (iii) exchange symmetry of the 2D propagator. (iii) is the axis exchange that the class of 6.2 already has. (i) and (ii) are Gaussian properties: for the Wilson weight a free wall is not a mirror (the reflection-even sector of the 2b-torus keeps the plaquettes across the reflection plane), and log W does not split into modes. The counterexample of 6.2 lives exactly in the gap left by (i) and (ii). So the free-field pass says what an interacting proof must supply: a substitute for the image identity, i.e. a bound of the wall-to-wall term delta_e(b) by the same correlation that builds the thermal sum, at distance 2b on the free axis against a on the time axis (W2 is a statement that the free wall reflects no more strongly than a mirror), plus a linked (logarithmic) form of the wall overlap. A natural first target: prove a delta_e(b) at most C b p(a) for the Wilson weight from reflection positivity across the planes perpendicular to the free axis, using the Neumann/even-sector comparison as a one-sided inequality instead of an identity.
4. FW2's sign is normalisation-dependent in non-compact fields (Neumann bare Gaussian is sub-multiplicative; a per-bond constant restores FW2). None of g, p, c, gamma, delta_e depends on it, so FW5 and FW6 are unaffected; only D_inf (here negative in bare normalisation) moves.

Status. PROVED (here, by hand): Steps 2-5 for the Neumann scalar; the Proca tower formula; W2 tower by tower for Proca, Dirichlet and (given the mode formula) Maxwell. ARGUED: Neumann is the Wilson-matched wall (Gaussian limit); the Maxwell photon multiset. GUIDE: the sup values in Step 7 and every C_1 above 1. Not checked by anyone else; a check should redo Step 3 (R1-R3) and the comparison in Theorem W2 line by line.

RESULT: Row 903 (Claude Opus 5.5, by hand + GUIDE): in the lattice free massive scalar with periodic time and Neumann space walls (the wall that matches the Wilson free-wall box in the Gaussian limit) every FW5 term is exact, p(a) = a sum_T int_{M_T^2}^inf sum_{r>=1} G_s(ra,0) ds, a delta_e(b) = a b sum_T sum_{j>=1} int G_s(2bj,0) ds, g = b p + W_N + (positive corner), c = p + W_N, gamma > 0, and both wall inequalities hold with absolute constants, PROVED for all m > 0 and all c, d: (WALL-1) with C_1 = 1 (best) and (WALL-2) with C_2 = 1/floor(2b/a), at most 1/4 for a at most b/2 (GUIDE supremum about 0.012); Dirichlet, Proca and Maxwell walls also pass (W2 against b p PROVED tower by tower; C_1 about 1.2-1.7 GUIDE); nothing grows with a, b or 1/m, so the free field does not kill the engine; the proof rests on the image (mirror) identity and mode factorisation, which the Wilson weight lacks, so the interacting (WALL-2) needs a substitute for the image identity and stays OPEN.
