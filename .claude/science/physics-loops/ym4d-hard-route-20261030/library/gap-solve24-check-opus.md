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
