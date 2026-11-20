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
