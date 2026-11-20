lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T19:44Z

# Check of row 1222 (`library/gap-solve24-astra62.md`): queue row 1226, `gap-solve24-check-opus`

Started 2026-11-20T07:44Z (date -u) at commit 8653351c2 on branch claude/ym4d-hard-route. Worker: Claude Opus 5.5, max effort,
Mac mini worker. Cross-provider check (row 1222 was written by gpt-6-astra). Research-stage working state; no claim.

Scope of the row: check by hand, line by line, `library/gap-solve24-astra62.md`, positive claims first: the comparisons
(17), (21)-(22) of the finite-cube gap with slice correlations and event disagreement; the estimates (19)-(20), (23),
(24)-(25); then everything else. Say whether the main comparison restates an earlier row. For each cited earlier row,
read the cited statement and its proof where the step depends on it. Verdict per statement: HOLDS, HOLDS AFTER
CORRECTION, FAILS, with the line. Numerics guide only.

## Plan (at most eight steps; one per response, appended as done)

1. Read row 1222's FINISH line and the target file; record its statement list with line anchors (Section 1).
2. Check comparison (17) and its inputs (Section 2).
3. Check comparisons (21)-(22) (Section 3).
4. Check estimates (19)-(20) and (23) (Section 4).
5. Check estimates (24)-(25) (Section 5).
6. Check the remaining statements and every cited earlier row where a step depends on it (Section 6).
7. Restatement question: grep earlier rows and open-core for the main comparison (Section 7).
8. Verdict table and RESULT line (Section 8).

## Status log

- 2026-11-20T07:44Z: file created with the plan.

## 1. Inventory of row 1222 (`library/gap-solve24-astra62.md`, 438 lines, read in full)

Row 1222 = FINISH line 1303 (row n at line n + 81). Author: gpt-6.2-astra max, Mac mini Codex runner, 03:35Z-04:51Z.
Its RESULT: OPEN; (17), (21)-(22) compare the physical finite-cube gap with slice correlations / event disagreement after
fixing the common graph; hand estimates (19)-(20), (23), (24)-(25). IDs below are mine; "L" = line of the target file.

| ID | L | label | content |
|---|---|---|---|
| S1 | 15 | PROVED | setup; conditional expectations preserve gauge invariance |
| S2 | 17 | PROVED | wall set W_s, private sets I_C, conditional independence of cells given W_s |
| S3 | 19-23 | PROVED | (1): b^-4 sum_s d_{W_s}(f) <= E_b(f) |
| S4 | 25-29 | PROVED | (2) for k offsets gives E_b >= omega |
| S5 | 33 | PROVED | S_4 empty; common contractible loop in W_1..W_3; three updates cannot give (2) |
| S6 | 35-45 | PROVED | (3): norm of P_{W_4}P_{S_3} - Pi_0 <= 2 delta/sqrt(1-delta) |
| S7 | 47 | PROVED | (3) -> 0 when h/(1+6 beta) -> infinity, log(N/h) = o(h/(1+6 beta)) |
| S8 | 53-71 | PROVED | (4): Bayes comparison of the law with prescribed segment products; Z^c/Z |
| S9 | 73 | PROVED | local insertions; errors faster than any power of a |
| S10 | 75 | PROVED | thermal doubling defect changes by <= 3[-log(1-delta)] |
| S11 | 79-90 | PROVED | spin variables at identity windings; formula (5) |
| S12 | 92 | PROVED | uniqueness of the conditional infinite-line law on Z^4 |
| S13 | 94 | PROVED | spin Gibbs measure maps to Wilson Gibbs measure |
| S14 | 96 | PROVED | lift of a Wilson Gibbs state to spins; uniqueness of the lift |
| S15 | 98 | PROVED | local invariant spin observables = local gauge-invariant Wilson observables |
| S16 | 102 | PROVED | flat diagonal slice: segment origins on layers l = 0 mod h, all spins one there |
| S17 | 104-110 | PROVED | (6): crossing plaquette across a pinned layer |
| S18 | 112-114 | PROVED | star forest A on one quarter of the lower layer; comparison with delta_{r+1} |
| S19 | 116-122 | PROVED | counting obstruction: at most 2(P-1) of 6P crossing factors become one-sided |
| S20 | 124-130 | PROVED | (7): six-link loop, liminf beta(1 - tr U_gamma/2) >= 1/6 |
| O1 | 134-139 | OPEN | (8): three-wall estimate on boxes |
| S21 | 141-157 | PROVED (cond.) | (8) + matching => gap >= -log q/(4 l), (9) |
| S22 | 161-170 | PROVED | (10): moment bounds of the likelihood ratio between graph fibres |
| S23 | 172-176 | PROVED | (11): exceptional set of L outside [1/2, 2] |
| S24 | 178-191 | PROVED | (12); (13) at the identity fibre suffices for (9) |
| S25 | 195-199 | PROVED | local Wilson words: (13) on restrictions of gauge-invariant functions suffices |
| S26 | 201 | PROVED | (13) with C_0 = e^{4 beta m_B} |
| S27 | 203 | PROVED | charged components pay constant one |
| S28 | 205-214 | PROVED | (14): free-field comparison |
| S29 | 218-222 | PROVED | linear gauge theory: tile-boundary predictors with O(k^-2) loss |
| S30 | 224-231 | PROVED | (15): tile transports predict nothing about bounded words |
| S31 | 235-262 | PROVED | (16): alternating time-column sums satisfy (13) |
| S32 | 266 | PROVED | slice setup; no spatial edge of slices t_0, t_1 lies in G; M <= C_3 (N/h)^3 |
| S33 | 268-273 | PROVED | (17): abs(e^{-2b m_lat} - rho_pi) <= 2 eta_0 + eta_0^2 |
| S34 | 275-281 | PROVED | (18) => rho_pi <= 1 - c/3 |
| S35 | 283 | PROVED | continuum implication of (17)-(18) |
| S36 | 285 | PROVED | (16) along a spatial axis on one slice; (18) for column differences |
| S37 | 289-303 | PROVED | (18) for polynomials of degree d in n separated deficits |
| O2 | 305 | OPEN | constants depend on n |
| S38 | 309-316 | PROVED | (19): (18) for triple-difference arrays |
| S39 | 318-330 | PROVED | (20): variance bound with constant 20 for r-spaced differences |
| S40 | 332 | PROVED | (18) on (19) uniformly as eta_0 -> 0 |
| O3 | 334 | OPEN | slowly varying sums |
| S41 | 338-349 | PROVED | (21): R^-2 g_pi <= 1 - e^{-2b m_lat} <= R^2 g_pi |
| S42 | 351-362 | PROVED | exact decomposition; g_pi >= c/6; distance bound for slow eigenfunctions |
| S43 | 364-377 | PROVED | (22): Phi_nu^2/2 <= 1 - e^{-2b m_lat} <= 2 Phi_nu; Phi_pi within R^2 of Phi_nu |
| O4 | 379 | OPEN | relative disagreement bound for all slice events |
| S44 | 383-395 | PROVED | (23): (18) for every Borel function of n capped deficits |
| O5 | 397 | OPEN | tail events, growing n |
| S45 | 401-408 | PROVED | coupling-averaged specific heat bound |
| S46 | 410-422 | PROVED | (24): coupling average of N^-3[Var Y_0 + 2 int dxi/(1-lambda)] <= C |
| S47 | 424 | PROVED | homogeneous slab: d_i^pi(Y) >= c N^3 at selected couplings |
| S48 | 426-430 | PROVED | (25): N^-3 xi([e^{-aE},1]) <= C a E at selected couplings |
| O6 | 432 | OPEN | finite int dxi/(1-lambda) forces no gap |
| O7 | 436 | OPEN | remaining obligation |

Cited inputs to read where a checked step depends on them: row 1145 (1)-(3) (`gap-solve2-astra62.md`, straight
transports, Bessel-ratio bound) with its check; row 1155 (9) (`gap-solve7-astra62.md`, marked-plaquette exponential
moment); row 1161 (23) (`gap-solve9-astra62.md`, period-8 colouring); row 1165 (7), (14) (`gap-solve11-astra62.md`);
row 1204 (9) (`gap-solve21-astra62.md`); row 1211 (`gap-solve22-astra62.md`); row 1215 (`gap-solve23-astra62.md`);
Sussman-Alpoge outline GL3 (2197-2231), GL8 (2315-2335); four-author v7 prop:plaqvar (lines 18943-18969).

Revised step plan (same eight steps): 2 = S32-S33 (17) with inputs; 3 = S41-S43 (21)-(22) and S34; 4 = S38-S40 (19)-(20);
5 = S44 (23), S45-S48 (24)-(25); 6 = the rest, S1-S31, S35-S37; 7 = restatement question; 8 = verdict table, RESULT.

- 2026-11-20T07:53Z: Section 1 written.

## 2. Comparison (17) and its inputs (S32, S33)

**Input, row 1145 (1)-(3)** (`gap-solve2-astra62.md` L17-38; checked HOLDS by row 1146, `gap-solve2-check-opus.md`
items 18-21). Re-derived here for the steps (17) uses. (a) Given all links except a set in which no plaquette holds two
selected links, the selected links are independent with densities proportional to exp(x . H), |H| <= 6 beta (six
incident plaquettes, each a linear functional of norm beta). (b) The Fourier multiplier in dimension d is
I_d(s)/I_1(s) = prod_{k=1}^{d-1} R_k, R_k = I_{k+1}/I_k. From I_k' = I_{k+1} + k I_k/s and I_{k+1}' = I_k - (k+1) I_{k+1}/s
one gets R_k' = 1 - (2k+1) R_k/s - R_k^2 (I redid this). Its positive root u_k = sqrt(1+c^2) - c = exp(-arsinh c),
c = (k+1/2)/s, increases in s; near 0, R_k ~ s/(2k+2) < u_k ~ s/(2k+1); at a first contact R_k' = 0 < u_k', so no contact.
arsinh x >= x/(1+x) (compare derivatives: 1/sqrt(1+x^2) >= 1/(1+x)^2), and (k+1/2)/(s+k+1/2) >= 1/(1+s) for k >= 1/2.
So I_d/I_1 <= exp(-(d-1)/(1+6 beta)). (c) For a path with m free links, abs(p - 1) <= sum_{d>=2} d * d * (prod of
multipliers) = eta(m/(1+6 beta)) (trace of a d x d matrix against a unitary is at most d times the operator norm).
(d) M segments with h - 2 free interior links each, no plaquette holding two free links: joint density in
[(1-eta)^M, (1+eta)^M], and (1-eta)^M >= 2 - (1+eta)^M = 1 - delta (even binomial terms). HOLDS.

**S32 (L266). HOLDS.** Checked: (i) a link lies in S_3 = W_1 cap W_2 cap W_3 iff its three transverse coordinates have
residues exactly {0, h, 2h} mod b = 4h (three walls need three distinct residues, there are three transverse
coordinates). A spatial edge at time t_0 = 3h or t_1 = 3h + 2b has time residue 3h, so its two other transverse
coordinates cannot supply three residues: no slice edge is in G. (ii) Interior vertices of segments have the cut
coordinate not divisible by h; slice vertices have time 3h or 11h, divisible by h, so no slice vertex is an interior
segment vertex, and every slice function is invariant under the interior vertex gauges. (iii) M: temporal segments
6 (N/b)^3 lines x 28 segments in a slab of 7b; spatial segments 3 x 6 x 7 (N/b)^2 lines x N/h segments; both are at most
C_3 (N/h)^3. (iv) Private links: the h - 2 interior links of each segment; parallel S_3 links at distance one cannot
exist (residues 0, h, 2h with h >= 5), and two perpendicular S_3 links in one plaquette force the plaquette corner to
have both cut coordinates divisible by h, i.e. they are end links. So row 1145 (3) applies.

**S33, (17) (L268-273). HOLDS.** Step by step.
1. Likelihood ratio. Let E' be all links except the private links. Given E' the products have density p_{E'}(c) in
   [1 - delta, 1 + delta]; for E-measurable tests F (E = all links outside the raw graph, containing both slices)
   Bayes gives pi^c F = nu[F p_E(c)]/p(c) with p_E = nu[p_{E'} | E]. So d pi^c/d nu on that sigma-field lies in
   [(1-delta)/(1+delta), (1+delta)/(1-delta)] = [1/R, R], R = 1 + eta_0, eta_0 = 2 delta/(1 - delta). Correct.
2. Raw graph = products. For a test invariant under the interior vertex gauges the map r -> nu[F | raw = r] is
   invariant (substitute E = g.E' using invariance of the joint law and of Haar), hence a function of the products,
   which the interior gauges reach transitively. So conditioning raw links to one equals conditioning products to one
   for such tests; by S32 (ii) every slice test qualifies. Correct (the file says this in one sentence, L273).
3. Correlation comparison. For f, g centred under nu with unit nu-variance: abs(pi(fg) - nu(fg)) <= eta_0 nu|fg| <= eta_0,
   abs(pi f) <= eta_0, Var_pi f <= R. Hence abs(nu(fg)) <= rho_pi R + eta_0 + eta_0^2 and rho_nu - rho_pi <= 2 eta_0 + eta_0^2
   (using rho_pi <= 1). The reverse uses d nu/d pi in [1/R, R]. Correct.
4. rho_nu = e^{-2b m_lat}. In the vacuum cylinder the two-slice law is psi(U) [T^{2b}/lambda_0^{2b}](U,U') psi(U') dU dU'
   on gauge-invariant functions; T is positive self-adjoint and compact on the gauge-invariant space (Osterwalder-Seiler,
   Luscher; outline GL8), f -> f psi is unitary onto that space, and the supremum of abs<f psi, T^ g psi> over centred
   unit f, g is the norm of the normalised T^{2b} on the vacuum complement, (lambda_1/lambda_0)^{2b}. Correct, with
   m_lat taken over all gauge-invariant states of the finite spatial torus (all flux sectors), as the file defines it.

No gap found. Remark (not an error): the sentence "Expose both full spatial slices before the private segment links"
is harmless because no slice edge is private (S32 (i)); the bound would fail for slice positions with time residue in
{0, h, 2h}, which the file avoids by its choice t_0 = 3h, t_1 = 3h + 2b.

## 3. Comparisons (21)-(22) and the slice facts they use (S34, S41, S42, S43)

**S34 (L275-281). HOLDS.** Under pi, given W_i (which contains G), the private cells are independent with their Wilson
conditional laws. Slice t_0 (residue 3h) lies strictly inside one time layer of cells for each offset (i-1)h, i <= 3, and
slice t_1 = t_0 + 2b lies two layers later, so the cells meeting the two slices are disjoint and F_0, G_1 are
conditionally independent given W_i. For centred F_0, G_1: pi(F_0 G_1) = <P_i F_0, P_i G_1> for each i. Averaging,
Cauchy-Schwarz, and sum_i ||P_i F_0||^2 = 3||F_0||^2 - sum_i d_i(F_0) <= (3 - c)||F_0||^2 give abs(pi(F_0 G_1)) <=
(1 - c/3) ||F_0|| ||G_1||. Correct.

**S41, (21) (L338-349). HOLDS.** In nu: nu|F_0 - F_1|^2 = 2<f, (1 - T^^{2b}) f>, f = (F - nu F) psi orthogonal to the
vacuum (stationarity); since T^^{2b} on the vacuum complement has spectrum in [0, e^{-2b m_lat}] (a square of a
self-adjoint operator), the infimum of the quotient is exactly 1 - e^{-2b m_lat}, attained at the first excited
eigenvector. The numerator is a test on the joint slice algebra, so pi and nu agree within the factor R; the
denominator Var = inf_c E|F - c|^2 compares within R for each c, hence for the infimum. The quotient therefore changes
by at most R^2 either way, for every F, and so does the infimum. No additive error. Correct.

**S42 (L351-362). HOLDS.** The decomposition pi|F_0 - F_1|^2 = d_i(F_0) + d_i(F_1) + pi|P_i F_0 - P_i F_1|^2: the cross terms
vanish because F_s - P_i F_s is orthogonal to W_i-measurable functions and the two residuals are conditionally
independent with conditional mean zero (S34). Then pi|F_0 - F_1|^2 >= (1/3) sum_i d_i(F_0) >= (c/3) Var_pi F_0, so
g_pi >= c/6. For centred unit f with quotient u: sum_i d_i(f) <= 3 * 2u, so D(f) <= sqrt(6u). D is a seminorm with
D(g - f) <= sqrt(3) ||g - f||; on the space L, D(g) >= sqrt(c) ||g|| >= sqrt(c)(1 - ||g - f||), which gives the stated
distance bound. Correct.

**S43, (22) (L364-377). HOLDS.** Upper bound: the quotient at the indicator of A is nu(A_0 xor A_1)/(2 p(1-p)) <=
nu(A_0 xor A_1)/min(p, 1-p) = 2 x [the conductance ratio], since p(1-p) >= min(p, 1-p)/2; so 1 - e^{-2b m_lat} <= 2 Phi_nu.
Lower bound (Cheeger, Lawler-Sokal form): with m a median of real f and g = (f - m)_+, every positive superlevel set of
g^2 is a gauge-invariant event of mass at most 1/2, so by the layer-cake formula nu|g_0^2 - g_1^2| >= 2 Phi_nu ||g||^2; and
nu|g_0^2 - g_1^2| <= ||g_0 + g_1|| ||g_0 - g_1|| <= 2||g|| (nu|g_0 - g_1|^2)^{1/2}. Hence Phi_nu^2 ||g||^2 <= nu|g_0 - g_1|^2.
For reals (a - b)^2 >= (a^+ - b^+)^2 + (a^- - b^-)^2 (the cross term -2(a^+ - b^+)(a^- - b^-) = 2(a^+ b^- + b^+ a^-) >= 0),
and Var f <= nu(f - m)^2, so the quotient is at least Phi_nu^2/2. The pinned comparison R^{-2} Phi_nu <= Phi_pi <=
R^2 Phi_nu follows termwise (numerator: joint slice event; each of pi(A_0), 1 - pi(A_0) within R). Correct.
- 2026-11-20T07:54Z: Sections 2-3 written ((17), (21), (22), S34, S42 HOLD).

## 4. Estimates (19)-(20) and the column bounds they reuse (S31, S36, S38, S39, S40)

**Input, row 1155 (9)** (`gap-solve7-astra62.md` L130-134; checked HOLDS by row 1156, `gap-solve7-check-opus.md` item 17,
L349-351): E exp{c beta sum_{p in S}(1 - w_p)} <= C^{|S|} on periodic tori, c = 1/8. Read; the argument (halve marked
electric couplings, multiplier ordering, Schatten Holder along the time circle, Holder over four direction classes) is
generic to any periodic rectangle. Consequences used by row 1222: nu X_p^2 <= 2C/c^2 =: C_2, and (Jensen with S = all
6V plaquettes) E_beta S <= 6V log C/(c beta) = C' V/beta. Both correct.

**Input, the one-link variance (four-author v7 prop:plaqvar, cited L247).** I did not rely on the external text; here is
a hand proof with a better constant. Let x on S^3 have density proportional to e^{x.H}, kappa = |H| <= 6 beta, mu = H/kappa,
and v a unit vector, v = cos(phi) mu + sin(phi) e with e orthogonal to mu. The reflection x -> x - 2(x.e)e preserves the
law, so Cov(x.mu, x.e) = 0 and E x.e = 0; hence Var(x.v) >= min(Var(x.mu), E(x.e)^2). With u = 1 - x.mu, the density of u
is proportional to e^{-kappa u} sqrt(u(2-u)) on [0,2] and E(x.e)^2 = E[u(2-u)]/3. For kappa >= 2 take I_1 = [0, 1/(2 kappa)],
I_2 = [1/kappa, 2/kappa]; every real c is at distance >= 1/(4 kappa) from one of them, so Var u >= min(P(I_1), P(I_2))/(16 kappa^2).
Using Z <= sqrt(2) Gamma(3/2) kappa^{-3/2}: P(I_1) >= e^{-1/2}/(3 sqrt(pi)) > 0.11, P(I_2) >= e^{-2} sqrt(2/pi) > 0.10, so
Var(x.mu) >= 0.006/kappa^2, and E(x.e)^2 >= E[u 1{u<=1}]/3 >= 0.10/(3 kappa) >= 0.06/kappa^2. For kappa <= 2 the density is
at least e^{-2 kappa} >= e^{-4} relative to Haar, so Var(x.v) >= e^{-4} Var_Haar(x.v) = e^{-4}/4 > 0.0045. Hence
Var(w_p | rest) >= 0.0045 (1 + 6 beta)^{-2} >= 2^{-19}(1 + 6 beta)^{-2}, and Var(X_p | rest) >= 2^{-19}/49 for beta >= 1
(beta/(1 + 6 beta) >= 1/7). The cited input HOLDS (with room to spare); it also gives the bound attributed to row 1165 (7)
in S47: Var(H.x) = kappa^2 Var(x.mu) >= 0.006 for kappa >= 2.

**S39, (20) (L318-330). HOLDS.** Checked: (a) the pair formula. With N = rn, a pair lambda_a >= lambda_b contributes
A_ab-vector outer products times lambda_a^{N-rl-s} lambda_b^{rl-s} + lambda_b^{N-rl-s} lambda_a^{rl-s}; writing the weight
lambda_a^{N-r-s} lambda_b^{r-s} and t = (lambda_b/lambda_a)^r, the two terms are exactly t^{l-1} and t^{n-l-1} times it (I
expanded both exponents). Nonnegativity needs T >= 0 (Wilson link-reflection positivity; the kinetic kernel
exp(beta Re tr(U V*)) has positive character coefficients), and A real symmetric (multiplication operator for s = 0;
for s = 1 the reflection of the unit slab preserves the integrand). (b) int dM <= K_1 since K_1 = int (1 + t^{n-2}) dM;
K_1 <= K_0 by Cauchy-Schwarz and stationarity for every real combination; K_l symmetric by reflection about the
midpoint. (c) Fourier: K_{n-l} = K_l (periodicity), so K^(theta) - K_0 = int k(t,theta) dM with
k = sum_{l=1}^{n-1} t^{l-1}(e^{il theta} + e^{-il theta}) real at theta = 2 pi j/n; abs(sum_{l=1}^{n-1} t^{l-1} e^{il theta})
<= 2/abs(1 - t e^{i theta}); abs(1 - e^{i theta}) <= 2 abs(1 - t e^{i theta}) (triangle inequality and 1 - t <=
abs(1 - t e^{i theta})) and <= 2, so abs(1 - e^{i theta})^2 abs(k) <= 16; a real scalar kernel <= 16 integrated against a
positive matrix measure is <= 16 int dM <= 16 K_0; the diagonal gives 4 K_0. (d) The covariance of the differences has
symbol abs(1 - e^{i theta})^2 K^(theta) <= 20 K_0, zero at theta = 0; discrete Parseval gives (20). Correct.

**S38, S40, (19) and (18) on (19) (L309-316, L332). HOLDS.** Odd positions set to zero turn (20) into r-spaced pair
differences tau^{2rl}(1 - tau^r). The plaquette reading is invariant under reflection through the middle of its own slice
(transverse direction, s = 0) or unit slab (in-plane directions, s = 1), and translations in the other directions commute
with that reflection, so (20) applies successively in the three spatial directions: nu|F_z|^2 <= 20^3 C_2 sum |z_m|^2,
first on finite time period, then in the vacuum cylinder (bounded readings converge). Lower bound: the 8 (n/2)^3 sampled
plaquettes sit at distinct positions r(2m + eps), link sets at distance >= r - 1 >= 3; each has a free spatial edge on slice
t_s, which is not in G (Section 2) and lies in at most two of W_1..W_3 (time residue 3h never triggers a wall), so it can be
assigned to a wall omitting it; conditional variances add; sum_q |c_q|^2 = 8 sum_m |z_m|^2. Var_pi F_z <= R nu|F_z|^2.
So (18) holds on (19) with c = 8 * 2^{-19}/(49 * 20^3 C_2 R). Correct; the OPEN remark O3 (L334: (19) annihilates modes
constant along a sampled direction, e.g. the homogeneous action sum) is accurate.

**S31, (16) (L235-262). HOLDS.** Upper bound: in nu the centred time-column covariance is int t^{|s-s'|} d sigma(t) with
sigma([0,1]) = Var X_0 <= C_2; the coefficient sequence has transform (1 - e^{i theta}) sum z_m e^{2im theta}; the Poisson
kernel times abs(1 - e^{i theta})^2 is decreasing in cos(theta) (derivative of (2 - 2c)/(1 - 2tc + t^2) in c is
-2(1-t)^2 <= 0), maximal 4(1-t)/(1+t) <= 4 at c = -1. So nu|F|^2 <= 4 C_2 sum |z_m|^2. Transfer to pi_0: each
X_s X_s' meets a segment in at most eight links, (4) gives an error 2 delta_8/(1 - delta_8) C_2 per pair; summing,
(sum |c_s|)^2 <= 2u sum |c_s|^2 = 4u sum |z_m|^2, and u delta_8 -> 0 (delta_8 is smaller than any power of a). nu-mean of F is
0 by stationarity. Lower bound as in S40, with time separation r >= 2 (no action plaquette holds two marks). Correct.

**S36 (L285). HOLDS.** I recomputed the paired kernel (t^s + t^{N-s})/(1 + t^N) and its sum over s = 0..n-1 at a Fourier
frequency: (1 - t^n)(1 - t^2)/((1 + t^n) abs(1 - t e^{i theta})^2), i.e. (1-t^n)/(1+t^n) times the Poisson kernel; equal pairs
give constants, removed by the differences. Correct.

## 5. Estimates (23) and (24)-(25) (S44-S48)

**S44, (23) (L383-395). HOLDS.** (a) Upper bound: normaliser of e^{x.H} at least e^{|H|-1} times the volume c(1+|H|)^{-3/2} of
the chordal cap of radius (1+|H|)^{-1/2} (on it x.H >= |H| - |H|/(2(1+|H|))), so the tilted density is <= C(1+|H|)^{3/2};
the Haar density of X = beta(1 - x.v) is (2/(pi beta)) sqrt((X/beta)(2 - X/beta)) <= C beta^{-3/2} sqrt X; product <= C' sqrt x
for beta >= 1; the atom at B absorbs P(X >= B) <= 1. So law(Y_p | exposed) <= A_B sigma_B. (b) Lower bound on the good
event (probability >= 1/2 under pi by row 1155 (9), a union bound over 6n faces, and (4)): there all six targets are within
2 sqrt(2K/beta) of v_p, so |H_p - 6 beta v_p| <= 12 sqrt(2K beta), |H_p| >= 3 beta and the direction is within C sqrt(K/beta)
of v_p for large beta; at X_p = x the mark is within sqrt(2x/beta) of v_p, exponent >= |H| - C(K + B + 1); with the normaliser
bound C e^{|H|}(1+|H|)^{-3/2} and the Haar lower bound (2/pi) beta^{-3/2} sqrt x (needs x <= beta, i.e. beta >= B + 1), the density
is >= a sqrt x on (0, B+1); the atom gets >= int_B^{B+1} a sqrt x dx. (c) Conditional independence of the marks (link sets at
distance >= 3) gives the product bounds; Efron-Stein for the three independent groups at fixed common exterior gives
sum_i d_i >= E Var(f | exterior) >= (1/2) a^n Var_sigma f (variance is an infimum over constants), and
Var_pi f(Y) <= int |f - sigma f|^2 d law <= A_B^n Var_sigma f. (d) Events: from S42's decomposition,
pi(A_0 xor A_1) >= (1/3) sum_i d_i(1_A) >= (c/3) p(1-p), and p(1-p) >= min(p,1-p)/2 gives the ratio >= c/12. Correct. The OPEN
remark O5 (the cap merges the tail; the constant decays with n) is accurate.

**S45 (L401-408). HOLDS.** -d/d beta E_beta S = Var_beta S on the finite torus; integrate over [B, 2B], drop E_{2B} S >= 0,
use E_B S <= C' V/B (row 1155 (9), above) and beta^2 <= 4B^2: the average is <= 4C'. Correct.

**S46, (24) (L410-422). HOLDS.** (a) Y_t: electric plaquettes of the unit slab plus half the magnetic plaquettes of both
end slices, times beta; sum_t Y_t = beta S exactly (each magnetic plaquette is shared by two slabs). (b) For 1 <= s < M the
centred one-step insertion A - E(Y_0) T is real symmetric; the trace numerator is sum |A_vw|^2 lambda_v^{s-1} lambda_w^{M-s-1}
>= 0 since T >= 0; at s = 1 the shared magnetic half-weights multiply inside A A, consistent with Y_0 Y_1. I checked the
centring: Tr((A - cT) T^{s-1} (A - cT) T^{M-s-1})/Tr T^M = E Y_0 Y_s - c^2. (c) Var(beta S) = M sum_s C_M(s) by
stationarity, so (beta^2/V) Var S = N^{-3} sum_s C_M(s). (d) M -> infinity at fixed N, beta: C_M(s) -> C(s) =
int lambda^{s-1} d xi (vacuum simple; the centred vector has no vacuum component, so xi has no atom at 1); keep
s = 0..k and M-k..M-1 (nonnegative terms, C_M(M-s) = C_M(s)); Fatou in beta, then monotone convergence in k. (e) Markov:
the set where the bracket exceeds 2C N^3 has measure <= B/2. Correct.

**S47 (L424). HOLDS.** Checked: marks = temporal edges of the slab with spatial coordinates all 1 mod 4; such an edge is in
no W_i (its transverse residues are 1 mod 4, the wall residues 0, h, 2h are 0 mod 8) and no plaquette holds two marks; all
six plaquettes of a mark are electric plaquettes of the slab, so Y = const - H.x per mark with H the true staple tilt; the
six plaquettes contain no G link (a temporal G link needs all spatial coordinates divisible by h, these have two
coordinates 1 mod 4); the good event {beta(1 - w_q) <= K, all six} has pi-probability >= 1/2 and gives
|H| >= H.x >= 6 beta - 6K >= 3 beta for beta >= 2K; Var(H.x | H) >= 0.006 there (Section 4 input); (N/4)^3 marks give
d_i >= c N^3. The slab test reads first links of pinned temporal segments starting at t_s = 3h or 11h, but it is a
plaquette sum, invariant under the interior vertex gauge at time t_s + 1, so the raw = product identification of
Section 2 step 2 applies and (4) holds for it. Var_pi Y <= C' N^3 uses the selected-coupling bound Var_nu Y_0 <= 2C N^3
from (24), as the file says ("at any selected coupling"). Correct.

**S48, (25) (L426-430). HOLDS.** At a selected coupling int d xi/(1 - lambda) <= C N^3, and 1/(1 - lambda) >= 1/(1 - e^{-aE}) on
[e^{-aE}, 1], so N^{-3} xi([e^{-aE}, 1]) <= C(1 - e^{-aE}) <= C a E. The energy reading lambda = e^{-a E_phys} is right. O6 (L432:
(1 - lambda) d lambda has finite int d xi/(1 - lambda) and weight near 1) is a correct counterexample to over-reading (25).
- 2026-11-20T08:01Z: Sections 4-5 written ((19), (20), (23), (24), (25), S31, S36, S45, S47 HOLD; plaqvar re-proved by hand).

## 6. The remaining statements (S1-S30, S35, S37) and the cited sources

Cited-row reads for this section: row 1161 (23) colouring (`gap-solve9-astra62.md` L343-351; row 1162 S39 HOLDS) is the
general form of the period-8 rule used in (4) (A_mu = {2 mu}); row 1165 (7) (`gap-solve11-astra62.md` L103, proof L107-111)
contains the fact cited at L424 ("for s >= 3 it dominates a fixed positive multiple of uniform measure on [1,2] ... variance
at least c"), so that citation is accurate. The v7 line citations L51 (5850-5918, 6106-6120, 8243-8267, 12137-12144) and L201
(7357-7369) fall inside the TeX ranges row 1218 read (`prior/gap-onebound-read-sol.md` L26); prop:plaqvar (18943-18969) lies
outside them and I did not fetch the source: NOT VERIFIED as a citation, but the step no longer depends on it (Section 4).

| ID | L | verdict | what I checked |
|---|---|---|---|
| S1 | 15 | HOLDS | mu and each link sigma-field are invariant under vertex gauges |
| S2 | 17 | HOLDS | a unit plaquette always lies in a closed b-cell; if in two, a transverse coordinate sits on a wall and all four links are retained; private links of different cells are conditionally independent given W_s |
| S3 | 19-23 | HOLDS | the cell projections commute and multiply to P_{W_s}; telescoping into orthogonal differences gives d_{W_s} <= sum_C d_{E minus I_C}; a private link's base lies in x + [0,b)^4 (transverse coordinates strictly inside, own coordinate in [x_mu, x_mu + b - 1]); each x is a lower corner for exactly one offset |
| S4 | 25-29 | HOLDS | apply (2) to translates, average over the b^4 common shifts, then (1); it is an implication, the hypothesis (2) is not proved |
| S5 | 33 | HOLDS | the square x_2 = 0, x_3 = h, corners 2h and 2h + b in (x_0, x_1): every link has transverse residues {0, h, 2h}; at beta = 0 coordinate projections of a product law compose by intersecting retained sets |
| S6 | 35-45 | HOLDS | S_3 links never lie in W_4 (residue 3h); interior segment vertices have degree two; private links share no plaquette; abs(nu g) <= delta norm_{L1(nu)}, sup bound, L1(nu) <= (1-delta)^{-1/2} L2(mu) |
| S7 | 47 | HOLDS | M eta <= 4(N/h)^4 C e^{-(h-2)/(1+6 beta)} -> 0 |
| S8 | 53-71 | HOLDS | a plaquette's links have bases l, l, l+1, l+1; one parity is even and 2 mu mod 8 fixes the direction; h/8 - r private links; Bayes with p_E in [1 - delta_r, 1 + delta_r] |
| S9 | 73 | HOLDS | u >= c h/log(1/a), and h/log^2(1/a) -> infinity makes e^{-u} smaller than any power of a |
| S10 | 75 | HOLDS | each log Z^c - log Z lies in [log(1-delta), log(1+delta)]; the combination 2(.) - (.) costs at most 3[-log(1-delta)] |
| S11 | 79-90 | HOLDS | I expanded U_p in the spins and cycled the trace: (1/2) tr[R(x)^{-1} R(x+mu) R(x+mu+nu)^{-1} R(x+nu)] |
| S12 | 92 | HOLDS | each incident plaquette meets a mu-line in one increment; given the rest, the line is a walk with independent tilted increments (tilt <= 6 beta); a margin of k increments mixes to within eta(k/(1+6 beta)) |
| S13 | 94 | HOLDS | single-link density >= e^{-6 beta}/e^{6 beta}; Doeblin minorisation of a sweep and uniqueness of its invariant law |
| S14 | 96 | HOLDS | left-Haar frames per line; collinear links share no plaquette; the base spin is Haar and independent of increments by S12 |
| S15 | 98 | HOLDS | left rotations remove the line frames; right rotations are the vertex gauges |
| S16 | 102 | HOLDS | every site with l = 0 mod h is a segment end in all four directions, so all four spins are one there; the colouring is origin-free |
| S17 | 104-110 | HOLDS | (6) is (5) with R(x+mu) = R(x+nu) = 1 |
| S18 | 112-114 | HOLDS | colours of y - mu run over Z/4, so each middle site has one chosen predecessor; stars disjoint; each segment meets A only in its terminal link; tree gauge integration; one quarter of the layer |
| S19 | 116-122 | HOLDS | forest edge count: sum_x (k_x - 1)_+ = (incident middle vertices) - (components) <= P - 1; binom(k,2) <= 2(k-1)_+ for k <= 4; 6P - 2(P-1) = 4P + 2 |
| S20 | 124-130 | HOLDS | the six steps return to the start, alternate levels, visit six distinct vertices, and all six links are lower-layer outgoing bonds; abs(E[(1/2) tr U_gamma or rest]) <= I_2/I_1 <= e^{-1/(1+6 beta)}; beta(1 - e^{-1/(1+6 beta)}) -> 1/6 |
| S21 | 141-157 | HOLDS (conditional, as labelled) | abs<u,v> <= abs<u,v>/2 bound gives P + Q <= 3/2 and d_G + d_{W_4} >= norm^2/2; d_{W_i}(f) <= (sum_{p<=i} norm r_p)^2 and Cauchy-Schwarz (1+2+3+4 = 10) give norm(Kf) <= q norm f; support growth 8k(b+2) per k sweeps; <f,g> = <P_i f, g> for conditionally independent supports; log-convexity of C_j(n) and a_j t_j/k_j -> 4 l give C(s) <= C(s_0) q^{(s-s_0)/(4 l)} |
| S22 | 161-170 | HOLDS | E_{pi_0} L^p = (Z_0/Z_1)^p Z_0^{-1} int e^{p S_1 + (1-p) S_0} dQ; for abs(S'') <= A, p S_1 + (1-p) S_0 <= S_p + A p(p-1)/2 (extrapolation form of the two-sided convexity bound, checked); raw graph density = product density in [1 - delta, 1 + delta] at every t; abs(S'') <= beta pi^2/h^2 * 4 * 6 * (Mh) = A |
| S23 | 172-176 | HOLDS | p = log2/(2A) >= 2; A p(p-1)/2 + 4p delta <= p log2/2; Markov gives 2^{-p/2} and 2 * 2^{-p/2} on the two sides; total <= 4 exp(-(log 2)^2/(4A)); in the boxes A ~ C beta k^4/h -> 0 polynomially in a, so epsilon is below e^{-ck} |
| S24 | 178-191 | HOLDS (conditional) | (12) by splitting at the exceptional set; the fibre bound integrates over G_D to (8) because G_D is contained in W_i (i <= 3); the additive term after k sweeps is <= c_0 epsilon norm_inf^2/(1 - q^2), negligible against q^{2k}; the file correctly imposes (13) on all bounded off-graph functions |
| S25 | 195-199 | HOLDS (conditional) | in pi_0 the cell integrals are the Wilson ones at the fixed graph values; three projections, telescoping constant 6, q_3 = (1 - 1/(6 C_0))^{1/2} |
| S26 | 201 | HOLDS | density in [e^{-2 beta m_B}, e^{2 beta m_B}]; Haar projections onto W_i cap B commute with empty intersection; variational formulas give C_0 = e^{4 beta m_B} |
| S27 | 203 | HOLDS | a vertex in all three wall complexes has residues 0, h, 2h in three coordinates, and the link in the fourth direction is an S_3 link; otherwise some W_i has no incident edge, its range is invariant under that vertex gauge, and charged isotypic components are annihilated by P_i |
| S28 | 205-214 | HOLDS | Var L >= <1,phi>^2/E(phi) with a tent zeroed on CR^4/b^3 graph sites; cell Poincare constant b^2; Var(L^2) = 2v^2 and E Var(L^2 or W_i) = 4 v v_i - 2 v_i^2, ratio <= 6 v_i/v = O(k^{-2} + b^{-1}) |
| S29 | 218-222 | HOLDS | tile sides at offset s_i lie on W_i; Stokes on each b-square; projection covariance gives E abs(L - L_i)^2 <= norm(omega_i - omega)^2 = O(R^4 (b/R)^2); trial potential bounds Var L >= c R^4 |
| S30 | 224-231 | HOLDS | (4) applies to any subcollection of the h-tiling of coordinate lines; tile corners sit at multiples of h because the offsets do |
| S35 | 283 | HOLDS (conditional) | delta -> 0 under the stated scaling, so rho_pi - e^{-2b m_lat} -> 0 and e^{-2b m_lat} = e^{-2 (ab)(m_lat/a)}; the continuum step is stated as a matching hypothesis |
| S37 | 289-303 | HOLDS | good event made exposed via the target inequalities (contains the deficit event); abs(H_p) >= 3 beta; density of X_p on [1,2] >= c_K; Efron-Stein over three groups; Gram matrix of monomials on [1,2]^n positive definite; moments to order 2d bounded via row 1155 (9), (4), Holder |

GUIDE statements L3-L11 and L51 (search and approach) make no mathematical claim; their repository citations are
treated in Section 7. OPEN statements O1-O7 are correctly labelled: none of them is proved in the file or, as far as
Section 7 found, elsewhere.
- 2026-11-20T08:03Z: Section 6 written (S1-S30, S35, S37 HOLD; plaqvar citation not verified, step re-proved).
