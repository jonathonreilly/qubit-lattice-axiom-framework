lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T16:30Z

# gap-twist-chart: the gauge chart (CH) at the twist-eating configuration

Queue row 679 of `FINISH.md`, item P2 of Part 4 of `library/gap-skeleton-max.md` (lines 548-553). Worker session on the Mac mini, pinned at commit 1b6bf3372, written section by section. Research-stage working state; not checked by any other model; nothing here is a public claim.

## 0. Repo search, duplicate check, credits

- **Duplicate check.** `library/open-core.md` has no entry containing "twist-eating" or "thin torus" (grep count 0). In `FINISH.md` the statement (CH) occurs only in row 679, this row. `library/gap-ac-lat.md` line 13 lists row 679 as a statement it does not attack, and its line 151 uses "the chart of row 679" only heuristically. No file `library/gap-twist-*` existed at the pinned commit. So nothing else covers (CH).
- **Repo prior work used.** `library/gap-skeleton-max.md` 3.1 (objects) and 3.4 (Facts 1-3), by run 1 (Claude Fable 5.2 max). Facts 1-3 are not cited as proved: Fact 1 is re-proved in 1.2, Fact 2 is replaced by the quantitative Lemmas R and Q (sections 4, 6), Fact 3 by Lemma L and Theorem (b) (sections 2, 7). `library/lattice-uhlenbeck.md` (Lemma U) was read as the model of a lattice gauge chart; nothing of its proof is used, because here the smallness is pointwise and a contraction replaces the continuity method, as the brief suggested.
- **Credits.** The twisted torus is 't Hooft's; the twist-eating configuration and the count of masses are as in Tanizaki and Unsal, arXiv:2201.06166, (19)-(24) (read by run 1, not re-read here). The weighted resolvent estimate of Lemma G is the Combes-Thomas argument (rebuilt in full in 2.3). Gauge fixing near a configuration by a contraction with a Green function is the method of Balaban's small-field charts and of Uhlenbeck's theorem (not read for this row; nothing is cited from them). The Sussman-Alpoge account was not needed for this statement and was not opened in this session.
- **No computer-assisted step.** One numerical sanity check of Lemma L is reported in section 9; it discharges nothing.

## 1. Setting and the statement proved

### 1.1 Objects

n >= 2. B = {0..L_3} x {0..L_4} a rectangle in Z^2 (L_3, L_4 >= 0). Sigma = Sigma_B = (Z/n)^2 x B, sites y = (x_1, x_2, b), b = (b_3, b_4) the base point of y. Links (y, mu): mu = 1, 2 always (fibre links, periodic); mu = 3, 4 when b + e_mu is in B (base links). Plaquettes (y; mu < nu) when both links at y exist. The base point of a link or plaquette is that of its site y. Base distance: the l^1 distance of base points.

U assigns an element of SU(2) to each link. U_p = U_mu(y) U_nu(y+mu) U_mu(y+nu)^{-1} U_nu(y)^{-1}. Gauge transformations: h on sites, (U^h)_mu(y) = h(y) U_mu(y) h(y+mu)^{-1}. P_0 = the (1,2)-plaquettes at sites with (x_1, x_2) = (n-1, n-1). Defect d_p(U) = 1 - (1/2) tr U_p off P_0, 1 + (1/2) tr U_p on P_0. A^tw(U) = sum of d_p over the plaquettes of Sigma.

On su(2): (X, Y) = -2 tr(XY), |X|^2 = (X, X). Orthonormal basis e_c = i sigma_c / 2, c = 1, 2, 3. For X = theta (i/2) u.sigma with u a unit vector, |X| = theta and exp(X) = cos(theta/2) + i sin(theta/2) u.sigma, so (1/2) tr exp(X) = cos(|X|/2). On SU(2): rho(g, g') = |log(g^{-1} g')| in [0, 2 pi], the bi-invariant geodesic distance of the 3-sphere of radius 2. If g, g' are unit quaternions with Euclidean inner product q, then q = cos(rho(g, g')/2). Rules used throughout: (R1) the triangle inequality; (R2) rho(a g b, a g' b) = rho(g, g'); so replacing one factor of a product by another moves the product by at most the distance of the two factors; (R3) rho(1, -1) = 2 pi.

Gamma_1 = i sigma_1, Gamma_2 = i sigma_2. V_1(y) = Gamma_1 if x_1 = n-1, else 1; V_2(y) = Gamma_2 if x_2 = n-1, else 1; V_3 = V_4 = 1. V_mu(y) depends on y only through the coordinate x_mu.

Constants. mu_n = (2 sin(pi/2n))^2. Since sin t >= 2t/pi on [0, pi/2]: 4/n^2 <= mu_n <= 2. alpha_n = sqrt(mu_n / 8), so 1/(sqrt 2 n) <= alpha_n <= 1/2.

### 1.2 Fact 1 again, and the frame

For mu < nu the V-plaquette is z_p := V_mu(y) V_nu(y+mu) V_mu(y+nu)^{-1} V_nu(y)^{-1} = V_mu V_nu V_mu^{-1} V_nu^{-1} with V_mu = V_mu(x_mu), V_nu = V_nu(x_nu), because V_nu(y+mu) = V_nu(y) and V_mu(y+nu) = V_mu(y). This is 1 unless both factors are non-trivial, that is {mu, nu} = {1, 2} and x_1 = x_2 = n-1, where it is Gamma_1 Gamma_2 Gamma_1^{-1} Gamma_2^{-1} = -1. So z_p = -1 exactly on P_0, and A^tw(V) = 0.

Transport. tau_l := Ad(V_l^{-1}), tau_l v = V_l^{-1} v V_l, for a link l = (y, mu). In the basis e_c, Ad(Gamma_1) = diag(1, -1, -1) and Ad(Gamma_2) = diag(-1, 1, -1). So tau_l is diagonal with entries s^c_l in {1, -1}: s^c_l = -1 exactly when l is a seam link of direction 1 (mu = 1, x_1 = n-1) and c in {2, 3}, or a seam link of direction 2 and c in {1, 3}. Call direction i(c) *antiperiodic for c*: i(1) = 2, i(2) = 1, i(3) = 1 (direction 2 also is).

If U_l = V_l exp(X_l) on all links then, moving the V's to the outside (e^{X} V_nu = V_nu e^{tau_nu X}, V_mu^{-1} e^{-X} = e^{-tau_mu X} V_mu^{-1}),

    U_p = z_p W E_p W^{-1},  W = V_mu V_nu,
    E_p = exp(tau_nu X_mu(y)) exp(X_nu(y+mu)) exp(-X_mu(y+nu)) exp(-tau_mu X_nu(y)),          (1.1)

(tau_nu, tau_mu the transports of the links (y+mu, nu), (y+nu, mu)). Hence d_p(U) = 1 - (1/2) tr E_p = 1 - cos(|Y_p|/2) with Y_p := log E_p whenever E_p is not -1.

Linear operators. For lambda on sites, X on links (values in su(2)):

    (D_0 lambda)(y, mu) = lambda(y+mu) - tau_l lambda(y),
    (D_1 X)(y; mu, nu) = tau_nu X_mu(y) + X_nu(y+mu) - X_mu(y+nu) - tau_mu X_nu(y),
    (D_0^* X)(y) = sum over links l ending at y of X_l  -  sum over links l starting at y of tau_l X_l.

D_0^* is the adjoint of D_0 for the inner products <.,.> = sum over cells of (.,.) (tau_l is symmetric). Each site has at most 4 links ending and 4 starting, so sup |D_0^* X| <= 8 sup |X|. Delta_0 := D_0^* D_0 = deg - A, where deg(y) is the number of links at y and (A lambda)(y) = sum over neighbours y' of tau^{+-1} lambda(y'). X is called *transverse* when D_0^* X = 0 at every site of Sigma.

If g = exp(lambda), then (V e^X)^g at the link l = (y, mu) is e^{lambda(y)} V_l e^{X_l} e^{-lambda(y+mu)} = V_l exp(tau_l lambda(y)) exp(X_l) exp(-lambda(y+mu)).            (1.2)

### 1.3 The statement proved

**Theorem (CH).** Fix n >= 2. There are delta_0(n) > 0, C(n) and eps_1(n) > 0 (defined in 8.1, explicit up to two absolute constants C_3, C_4 of the group SU(2)) such that for every rectangle B and every U on Sigma_B with d_p(U) <= delta <= delta_0(n) at every plaquette:

(a) There is a gauge transformation h on the sites of Sigma_B with U^h = V exp(X) link by link, X transverse, sup |X| <= C(n) sqrt(delta). If h' is another gauge transformation with U^{h'} = V exp(X'), X' transverse, sup |X'| <= eps_1(n), then h' = h or h' = -h, and X' = X. (C(n) sqrt(delta_0) <= eps_1.) In particular X is a gauge-invariant function of U.

(b) A^tw(U) >= (mu_n / 16) sum over links of |X_l|^2.

(c) If U' is a second configuration on Sigma_B with all defects at most delta_0(n), and U' = U on all links whose two ends have base distance at most r from the base point b_0 of a link l, then |X_l(U) - X_l(U')| <= C(n) (sqrt(delta) + sqrt(delta')) exp(-r / (3n)). [This is the meaning given to "X at a link depends on U at base distance r with weight at most C exp(-c r/n)"; c = 1/3 is absolute.]

Values: C(n) is a power of n (n^16 with the crude constants below) and delta_0(n) is a negative power of n. They are not optimised; see 8.3 for what an optimisation would give.

Plan: section 2 linear theory (Lemma L: gap; Lemma G: Green function), 3 group estimates, 4 Lemma R (rough gauge), 5 Lemma T (transverse gauge), 6 Lemma Q (uniqueness), 7 part (b), 8 part (c) and the constants, 9 sanity check, 10 status.

## 2. Linear theory

### 2.1 The product structure

The operators D_0, D_1 act on each colour component c separately, since every tau is diagonal. Fix c and write s_nu(j) for the sign of component c on the link of direction nu at coordinate x_nu = j (s_nu(j) = -1 only if nu in {1, 2} is antiperiodic for c and j = n-1; s_3 = s_4 = 1). The sign depends only on the direction and on the coordinate in that direction.

Sigma is the product of four one-dimensional complexes: for nu = 1, 2 the cycle Z/n, with vertices j and edges [j, j+1]; for nu = 3, 4 the interval with vertices 0..L_nu and edges [j, j+1], j < L_nu. Let E^0_nu, E^1_nu be the real functions on the vertices and edges of factor nu, and delta_nu : E^0_nu -> E^1_nu, (delta_nu f)([j, j+1]) = f(j+1) - s_nu(j) f(j). A cell of Sigma is a product of one cell from each factor, and real cochains of all degrees form the tensor product over nu of (E^0_nu + E^1_nu). Let gamma_nu be +1 on E^0_nu and -1 on E^1_nu, and extend delta_nu by 0 on E^1_nu. Define

    d_nu = gamma_1 x ... x gamma_{nu-1} x delta_nu x 1 x ... x 1,      d = d_1 + d_2 + d_3 + d_4.

*Check that d is D_0 on sites and D_1 on links.* On functions of sites all gamma are +1, so (d lambda)(y, mu) = lambda(y+mu) - s lambda(y) = D_0. On a link field X, for mu < nu: d_nu acts on X_mu with gamma_mu = -1, giving -(X_mu(y+nu) - s_nu X_mu(y)); d_mu acts on X_nu with all earlier gamma equal to +1, giving X_nu(y+mu) - s_mu X_nu(y). The sum is (D_1 X)(y; mu, nu).

*Anticommutation.* For nu != rho: d_nu d_rho^* + d_rho^* d_nu = 0 and d_nu^* d_rho + d_rho d_nu^* = 0. Proof: take nu < rho. In every slot except nu and rho the two products agree (gamma^2 = 1 or 1). In slot rho the factor is delta_rho^* in both orders (d_nu has 1 there). In slot nu the two orders give delta_nu gamma_nu and gamma_nu delta_nu; delta_nu gamma_nu = delta_nu (delta_nu lives on E^0, where gamma = 1) and gamma_nu delta_nu = -delta_nu (its values are in E^1). So the two orders differ by a sign. The other three cases (d_nu^* with d_rho, and nu > rho) are the same computation with delta_nu^* gamma_nu = -delta_nu^*, gamma_nu delta_nu^* = delta_nu^*. QED

Hence, on cochains of any degree,

    d^* d + d d^* = sum over nu of 1 x ... x (delta_nu^* delta_nu + delta_nu delta_nu^*) x ... x 1,                  (2.1)

since the cross terms cancel in pairs and gamma^2 = 1. Every term is non-negative.

### 2.2 Lemma L (the gap)

*Chain fact.* Let f be a real function on Z/n and s(j) = 1 for j < n-1, s(n-1) = -1. Then sum_{j=0}^{n-1} |f(j+1) - s(j) f(j)|^2 >= mu_n sum |f(j)|^2. Proof: extend f to F on Z by F(j + n) = -F(j). The sum equals sum_{j=0}^{n-1} |F(j+1) - F(j)|^2 (for j = n-1: F(n) - F(n-1) = -f(0) - f(n-1), and the term is |f(0) + f(n-1)|^2). F is a combination of the n functions e^{ikj}, k in (pi/n)(2Z+1) mod 2 pi, which are orthogonal over one window of length n, and the difference operator multiplies e^{ikj} by e^{ik} - 1, with |e^{ik} - 1|^2 = 2 - 2 cos k >= 2 - 2 cos(pi/n) = mu_n. QED. So delta_i^* delta_i >= mu_n on E^0_i when i is antiperiodic for c. On a cycle E^0_i and E^1_i both have dimension n, so delta_i is a square matrix, invertible by the bound, and delta_i delta_i^* = delta_i (delta_i^* delta_i) delta_i^{-1} has the same spectrum. So delta_i^* delta_i + delta_i delta_i^* >= mu_n on E^0_i + E^1_i.

**Lemma L.** For every rectangle B, every colour component, and every cochain omega of Sigma_B: |d omega|^2 + |d^* omega|^2 >= mu_n |omega|^2. In particular
(i) <lambda, Delta_0 lambda> = |D_0 lambda|^2 >= mu_n |lambda|^2 for su(2)-valued functions on sites;
(ii) |D_1 X|^2 >= mu_n |X|^2 for every transverse link field X.
Proof. By (2.1) the left side is the sum over nu of non-negative forms, and the term nu = i(c) is at least mu_n by the chain fact applied in slot i(c), for cochains of every type. Summing over colour components gives (i) and (ii). QED

The boundary of B is free: all cells of Sigma_B and no others enter, and transversality is imposed at every site including those over the boundary of B. No boundary term appears, because the gap comes from a fibre direction.

### 2.3 Lemma G (Green function of Delta_0)

By Lemma L(i) Delta_0 is invertible; G_0 := Delta_0^{-1}, diagonal in colour, with real kernels g_c(y, y').

**Lemma G.** (i) |g_c(y, y')| <= (2/mu_n) exp(-alpha_n |b(y) - b(y')|_1).
(ii) Let phi be a real function on B with |phi(b) - phi(b')| <= |b - b'|_1, and w(y) = exp((alpha_n/2) phi(b(y))). Then for every su(2)-valued f on sites, sup_y w(y) |(G_0 f)(y)| <= K_n sup_y w(y) |f(y)|, K_n := 25 n^6. (phi = 0 gives the plain sup norm.)

Proof. (i) Fix c, a 1-Lipschitz phi and alpha = alpha_n; M := multiplication by exp(alpha phi(b(y))), T := M Delta_0 M^{-1}, a real matrix with T(y, y') = Delta_0(y, y') exp(alpha (phi(y) - phi(y'))). For real u, <u, T u> = sum Delta_0(y, y') cosh(alpha (phi(y) - phi(y'))) u(y) u(y') (symmetrise in y, y'). The diagonal is unchanged, and so are the fibre neighbours (same base point). So <u, T u> = <u, Delta_0 u> - sum over ordered pairs of base neighbours of A(y, y') (cosh(alpha (phi(y) - phi(y'))) - 1) u(y) u(y'). Each site has at most 4 base neighbours, |A(y, y')| = 1, and cosh(alpha) - 1 <= alpha^2 for alpha <= 1, so the subtracted sum is at most 4 alpha^2 |u|^2 = (mu_n/2) |u|^2 in absolute value (Schur). With Lemma L(i): <u, T u> >= (mu_n/2) |u|^2, hence |T u| >= (mu_n/2) |u| and the operator norm of T^{-1} = M G_0 M^{-1} is at most 2/mu_n. So |g_c(y, y')| exp(alpha (phi(y) - phi(y'))) <= 2/mu_n. Take phi(b) = -|b - b(y)|_1.
(ii) Since G_0 is diagonal in colour with entries bounded by m(y, y') := (2/mu_n) exp(-alpha_n |b(y) - b(y')|_1), |(G_0 f)(y)| <= sum_{y'} m(y, y') |f(y')|. And w(y) <= w(y') exp((alpha_n/2) |b(y) - b(y')|_1). So w(y) |(G_0 f)(y)| <= (2/mu_n) sum_{y'} exp(-(alpha_n/2) |b(y) - b(y')|_1) w(y') |f(y')|. There are n^2 sites over each base point, and the sum over b' in Z^2 of exp(-t |b - b'|_1) is (coth(t/2))^2 with coth(t/2) = 1 + 2/(e^t - 1) <= 1 + 2/t. With t = alpha_n/2 >= 1/(2 sqrt 2 n): coth <= 1 + 4 sqrt 2 n <= 7 n. So the bound is (2/mu_n) n^2 49 n^2 <= (n^2/2) 49 n^4 <= 25 n^6. QED

Remark (not used). The plain sup norm of G_0 is in fact at most (1 + log n)/mu_n, from the heat kernel of the product (the base factor is a Markov semigroup, the fibre factor decays as n e^{-t mu_n} in sup norm). With it the constants of 8.1 improve; the weighted bound of that argument has rate 1/n^2 only, so Lemma G is kept for (c).

*State after section 2:* linear theory complete. Next: section 3 (group estimates).

## 3. Group estimates

**G1 (defect to angle).** If d_p(U) <= delta then rho(U_p, z_p) <= theta_delta := pi sqrt(2 delta). Proof: z_p U_p = exp(Y) with |Y| = t in [0, 2 pi] and d_p = 1 - cos(t/2) = 2 sin^2(t/4) >= 2 (t/(2 pi))^2, by sin u >= 2u/pi on [0, pi/2]. QED

**G2 (near the centre).** Let S in SU(2) with rho(S, Gamma_i S Gamma_i^{-1}) <= omega for i = 1, 2, omega <= 2. Then S = s_0 + i s.sigma has s_0 != 0 and rho(S, sign(s_0)) <= 1.2 omega. Proof: Gamma_1 S Gamma_1^{-1} = s_0 + i (s_1, -s_2, -s_3).sigma, so the quaternion inner product with S is 1 - 2 (s_2^2 + s_3^2) = cos(rho/2) >= cos(omega/2) >= 1 - omega^2/8. So 2 (s_2^2 + s_3^2) <= omega^2/8, and likewise 2 (s_1^2 + s_3^2) <= omega^2/8 from Gamma_2. Adding, |s|^2 <= omega^2/8 < 1, so s_0 != 0, and the inner product of S with sign(s_0) is |s_0| = cos(rho/2), so sin(rho/2) = |s| and rho = 2 arcsin |s| <= pi |s| <= pi omega/(2 sqrt 2) <= 1.2 omega. QED

**G3 (near an anticommuting pair).** Let A, B in SU(2) with rho(A B A^{-1} B^{-1}, -1) <= eta <= 2. Then there is k in SU(2) with rho(k A k^{-1}, Gamma_1) <= 1.2 eta and rho(k B k^{-1}, Gamma_2) <= 1.2 eta. Proof: write A = a_0 + i a.sigma, B = b_0 + i b.sigma. A B A^{-1} = b_0 + i (R b).sigma, R the rotation about a/|a| by twice the angle of A (if a = 0 the commutator is 1, excluded by eta < 2 pi). So (1/2) tr(A B A^{-1} B^{-1}) = b_0^2 + (R b).b, and the hypothesis says this is at most -cos(eta/2) = -1 + kappa, kappa := 1 - cos(eta/2) <= eta^2/8. Split b = b_par + b_perp along and across the axis: (R b).b >= |b_par|^2 - |b_perp|^2 = 2 |b_par|^2 - |b|^2. So b_0^2 + 2 |b_par|^2 - |b|^2 <= -1 + kappa, and with |b|^2 = 1 - b_0^2 this is 2 b_0^2 + 2 |b_par|^2 <= kappa. The trace of the commutator is symmetric in A and B (B A B^{-1} A^{-1} is the inverse), so also 2 a_0^2 <= kappa. Choose a rotation taking a/|a| to e_1 and b_perp/|b_perp| to e_2 (b_perp != 0 since |b_perp|^2 = 1 - b_0^2 - |b_par|^2 >= 1 - kappa/2 > 0), and k in SU(2) above it. Then k A k^{-1} = a_0 + i |a| sigma_1, with inner product |a| with Gamma_1, so sin(rho/2) = |a_0| <= sqrt(kappa/2) and rho <= pi |a_0| <= pi eta/4. And k B k^{-1} = b_0 + i (beta sigma_1 + |b_perp| sigma_2) with beta = +-|b_par|, with inner product |b_perp| with Gamma_2, so sin(rho/2) = sqrt(b_0^2 + |b_par|^2) <= sqrt(kappa/2) and rho <= pi eta/4 <= 1.2 eta. QED

**G4 (the two absolute constants).** On {(a, b, c) in su(2)^3 : |a|, |b|, |c| <= 1/2} the product e^a e^b e^c has distance at most 3/2 < 2 pi from 1, so L_3(a, b, c) := log(e^a e^b e^c) (the logarithm of norm below 2 pi) is real-analytic on a neighbourhood of this compact convex set. N_3 := L_3 - (a + b + c) vanishes at 0 with its first derivative. Let C_3 be the supremum over the set of the operator norm of the second derivative of N_3 (Euclidean norm on su(2)^3 = R^9); it is finite by compactness. By the mean value theorem, for u, u' in the set,

    |N_3(u) - N_3(u')| <= C_3 max(|u|, |u'|) |u - u'|.                                   (3.1)

Also N_3(0, b, 0) = 0. In the same way, on {|a|, |b|, |c|, |d| <= 1/2} (distance at most 2 from 1), Q_4 := log(e^a e^b e^c e^d) - (a + b + c + d) has second derivative bounded by a finite C_4, and

    |Q_4(u)| <= (C_4/2) |u|^2.                                                      (3.2)

C_3, C_4 depend on nothing. Explicit values can be had from the Baker-Campbell-Hausdorff series; they are not needed. We take C_3, C_4 >= 1.

## 4. Lemma R (rough gauge)

**Lemma R.** Let U on Sigma_B have d_p(U) <= delta at every plaquette, theta := pi sqrt(2 delta), and 27 n^3 theta < 2 pi. Then there is a gauge transformation h with U^h = V exp(X^0) and sup |X^0| <= eps_0 := 6.5 n^3 theta.

Proof. By G1, rho(U_p, z_p) <= theta for every plaquette; this is gauge invariant.

*Step A (one fibre).* Fix b. In the fibre torus over b take the spanning tree made of the links (x; 1) with x_2 = 0, x_1 < n-1, and the links (x; 2) with x_2 < n-1 (all x_1). It has (n-1) + n(n-1) = n^2 - 1 links and reaches every site. Choose the gauge on the fibre in which U = 1 on the tree. Then:
- For x_1 < n-1 and 1 <= x_2 <= n-1, the plaquette at (x_1, x_2 - 1) has its two vertical links in the tree and z_p = 1, so it is U_1(x_1, x_2 - 1) U_1(x_1, x_2)^{-1}; hence rho(U_1(x_1, x_2), U_1(x_1, x_2 - 1)) <= theta, and rho(U_1(x_1, x_2), 1) <= x_2 theta <= (n-1) theta.
- With A(x_2) := U_1(n-1, x_2): the same plaquettes at x_1 = n-1 (not in P_0, since x_2 - 1 < n-1) give rho(A(x_2), A(0)) <= (n-1) theta. Put A := A(0).
- With B(x_1) := U_2(x_1, n-1): for x_1 < n-1 the plaquette at (x_1, n-1) is U_1(x_1, n-1) B(x_1 + 1) U_1(x_1, 0)^{-1} B(x_1)^{-1} with U_1(x_1, 0) = 1 and z_p = 1. So rho(B(x_1 + 1), B(x_1)) <= theta + (n-1) theta = n theta, and rho(B(x_1), B(0)) <= n(n-1) theta. Put B := B(0).
- The plaquette at (n-1, n-1) is A(n-1) B(0) A(0)^{-1} B(n-1)^{-1}, within theta of -1. Replacing A(n-1) by A and B(n-1) by B: rho(A B A^{-1} B^{-1}, -1) <= theta + (n-1) theta + n(n-1) theta = n^2 theta =: eta. (eta <= 2 by the hypothesis.)
By G3 there is k with rho(k A k^{-1}, Gamma_1), rho(k B k^{-1}, Gamma_2) <= 1.2 eta. Apply the constant gauge transformation k to the fibre: the tree links stay 1, the distances above are unchanged. Now every fibre link has rho(U_l, V_l) <= n(n-1) theta + 1.2 n^2 theta <= 2.2 n^2 theta =: eps_f. Call this gauge transformation of the fibre h_b.

*Step B (base links).* Use the gauges h_b on all fibres. Fix a base link (b, b + e_a), a in {3, 4}, and S(x) := U_a(x, b). For mu in {1, 2} the plaquette (mu, a) at (x, b) is U_mu(x, b) S(x + mu) U_mu(x, b + e_a)^{-1} S(x)^{-1}, within theta of 1. Replacing the two fibre links by V_mu(x): rho(V_mu(x) S(x + mu) V_mu(x)^{-1}, S(x)) <= theta + 2 eps_f <= 5.4 n^2 theta =: theta_1. Going n steps around the cycle of direction mu from x, the V's multiply to Gamma_mu (one seam link), so rho(S(x), Gamma_mu S(x) Gamma_mu^{-1}) <= n theta_1 for mu = 1, 2 (conjugation by Gamma_mu and by its inverse agree). By G2 (n theta_1 <= 2 by the hypothesis), rho(S(x), e(x)) <= 1.2 n theta_1 <= 6.5 n^3 theta = eps_0 with e(x) in {1, -1}. The sign does not depend on x: for neighbours, rho(S(x + mu), V^{-1} S(x) V) <= theta_1, and V^{-1} S(x) V is within eps_0 of e(x); if e(x + mu) = -e(x) then 2 pi <= 2 eps_0 + theta_1 < 19 n^3 theta, against the hypothesis. So each base link carries a sign e_a(b) with rho(U_a(x, b), e_a(b)) <= eps_0 for all x.

*Step C (the signs are a pure gauge).* A base plaquette at (x, b) is within theta of 1, and each of its links is within eps_0 of its sign, so the product of the four signs is within theta + 4 eps_0 <= 27 n^3 theta < 2 pi of 1; it is 1. Define zeta(b_3, b_4) := prod_{j < b_3} e_3(j, 0) prod_{j < b_4} e_4(b_3, j). Then e_4(b) = zeta(b) zeta(b + e_4) by definition, and e_3(b) = zeta(b) zeta(b + e_3) by induction on b_4: it holds for b_4 = 0, and the plaquette at (b_3, b_4 - 1) gives e_3(b_3, b_4) = e_3(b_3, b_4 - 1) e_4(b_3 + 1, b_4 - 1) e_4(b_3, b_4 - 1). Put h(x, b) := zeta(b) h_b(x). Central factors do not change fibre links, and a base link becomes zeta(b) zeta(b + e_a) U_a = e_a(b) U_a, within eps_0 of 1 = V_a. Fibre links are within eps_f <= eps_0 of V. With X^0_l := log(V_l^{-1} U^h_l), |X^0_l| = rho(U^h_l, V_l) <= eps_0. QED

*Where a vortex would enter, and why it does not.* The only global step is C. The signs e_a(b) are a Z_2 gauge field on the base, and its curvature at a base plaquette is forced to vanish by the small defect of that plaquette. On a rectangle a flat Z_2 field is a pure gauge. So over a rectangle there is no configuration with all defects small that is not a small perturbation of V up to gauge: the second alternative of the stop rule does not occur. (On a periodic base the two base cycles carry signs that cannot be removed: the four minima of Fact 2. A centre vortex needs one base plaquette with defect of order one in each fibre over its core.) The price is the size of delta_0: Step A needs n^2 theta small and Step B n^3 theta small.

*State after section 4:* rough gauge done with eps_0 = 6.5 n^3 pi sqrt(2 delta). Next: section 5, the transverse gauge by contraction.
