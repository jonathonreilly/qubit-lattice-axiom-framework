lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:06Z

# gap-solve30-check-opus: line-by-line check of row 1262 (`library/gap-solve30-astra62.md`)

Row 1271 of FINISH.md. Checker: Claude Opus 5.5 (max reasoning), Mac mini worker. Cross-provider check of a row
written by another provider (astra62). Started 2026-11-20T12:06Z (date -u). Source pinned at commit 536662306.

## Plan (at most eight steps; one step per response, each appended here)

1. Read row 1262's file in full, its queue row, and the rules (FINISH.md head, GOAL.md); list every statement and
   its line; record which earlier rows it cites.
2. Check the conditional Wilson estimate: (15), (17) (finite-volume bound), (30), (35), by hand, line by line.
3. Check the variance loss (31)-(32) and the slow sheets (20), (25), by hand.
4. Check the remaining statements (everything else), in file order.
5. For each cited earlier row: read the cited statement and its proof where a step depends on it; verdict on the
   dependence.
6. Restatement question: is the main comparison a restatement of an earlier row (grep open-core.md and FINISH rows).
7. Optional guide-only numeric run (only at >= 50 percent memory free, under the numeric lock).
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with line), open items, RESULT line.

## Status log

- 2026-11-20T12:06Z: file created; step 1 starting.

## Step 1. Inventory of row 1262 (done 2026-11-20T12:07Z)

Source: `library/gap-solve30-astra62.md`, 454 lines, read in full. Queue row 1262 is FINISH.md line 1343; it was a
plain-brief solve run (gpt-6.2-astra max, 10:50Z-11:59Z). Labels in the file: PROVED, ARGUED, GUIDE, OPEN.

Statements by equation, with the line of the statement and of its proof:

| Item | Statement line | Proof lines | Content |
|---|---|---|---|
| setup | L13 | - | Wilson law on even N^4 torus; D_x = 1 - P_x for side-s cube; H_s = s^-4 sum_x D_x; patch I_z of R^4 origins, t = R+s-1; Q_z, L_z |
| (1)-(2) | L15-29 | L31-51 | local patch variance (1) gives global gap of H_s at least b_R gamma - e_(s,R) |
| (3) | L31-36 | L31 | Cauchy-Schwarz with sine weights p |
| (4) | L38-47 | L38-47 | sum_z norm(W_z f)^2 <= B(norm(H_s f)^2 + e_(s,R) E) |
| kernel, b_R, e bound | L49, L51 | L49, L51 | ker H_s = constants; b_R >= 1/16; e_(s,R) <= 40 pi^2 (s/(R+1))^2 |
| (5) | L61-66 | L68-73 | conditional mean of a box average of q_p <= m_s, every exterior |
| (6)-(8) | L75-81 | L83-95 | energy fraction of bad exteriors on spectral subspace 1_[0,1](H_s) |
| (9) | L97-100 | L101 | gap with (1) known only on good exteriors |
| choice | L103 | L103 | beta -> infinity parameters make rho -> 0 |
| (10) | L107-109 | L111-113 | m_s = min(1, C(1/s + 1/beta)) from row 1155 (9) |
| (11) | L115-118 | L120 | exclusion by local conditional probabilities |
| (12)-(13) | L122-131 | L135-142 | face colour Poincare from row 1141 (3)-(7) |
| (14)-(15) | L148-156 | L158 | collar version of (1)-(2) and (9) |
| face readings | L160 | L160 | Q_z f = 0 for readings on the outer face, b >= 2 |
| collar tests | L162-166 | L162 | mesoscopic four-box tests at cost C(R/s)^3 e^(-c l^4) + Cs/R |
| (16) | L168-174 | L168-174 | sufficient physical-scale condition gamma >= C_* (s/R)^2 |
| (17) | L178-182 | L184-188 | gamma = 2^-8 exp(-440 beta t^3) for every outer exterior, dyadic t |
| oscillation | L190 | L190 | first bisection density ratio >= exp(c beta t^3) |
| (18) | L198-202 | L204 | at R ~ beta^delta, (14) cannot hold with gamma/(s/R)^2 -> infinity |
| collar cost | L206 | L206 | electric action of a w-step interpolation >= beta d_G^2/(2w) |
| (19) | L210-215 | L217 | relative two-face quaternion Poincare |
| (20)-(22) | L223-249 | L229-259 | slow conditional sheet: two-plane pinned sheet of time links, Rayleigh quotient <= C(d/s)^2 d^2 e^(-cd) |
| (23) | L263-270 | L272 | one released neighbouring plane kills the variance of F |
| (24) | L274-281 | L276-300 | fixed thickness w: another reading with quotient (20) |
| (25)-(26) | L304-308 | L310-337 | thickness w ~ sqrt(beta): quotient <= C(1+w/s)(d/s)^2 d^2 e^(-cwd) |
| (27)-(28) | L341-349 | L341-350 | loop deficit by peeling; probability of coherent end holonomies |
| (29) | L352-356 | L357 | energy cost of excluding perimeter banks |
| filling test | L359 | L359 | exterior test of existence of a common filling |
| (30) | L363-375 | L377-394 | patch comparison with a revealed codimension-two tube |
| (31) | L398-400 | L402 | the reading F of (20) in the full periodic Wilson law: Pr(F != +1) <= C d^2 e^(-c beta d) |
| (32) | L404-406 | L408-412 | the reading of (25) in the full law: Pr(F != 0) <= C d^2 e^(-cKd) |
| correlations | L414 | L414 | the readings have vanishing correlation with L^2-bounded families |
| (33) | L418-421 | L423-425 | larger right-side form; (17) holds for it at every pin value |
| (34) | L427-430 | L427 | dense pin grid costs c (s/h)^2 in (4) |
| dense grid | L434 | L436 | coefficient ((s-h+1)/s)^4 >= 1/16 with planes pinned in four directions |
| (35) | L440-444 | L446 | least local constant = sup over g of integrated squared semigroup norm |
| power tail | L448 | L448 | dyadic power tail suffices; 2-dimensional example |
| OPEN | L194, L450, L452 | - | (17) far below (16); no estimate of (35) at order (R/s)^2; continuum |

Earlier rows and sources it cites (each to be read where a step depends on it):

- row 1254 `gap-solve29-astra62.md`: (17), (18)-(19) overlap estimate, (20), (33), (37), (39), (1)-(4). Unchecked at the pin (row 1262 says so, L452).
- row 1155 `gap-solve7-astra62.md`: (9) periodic marked-plaquette moment; (20) angle lemma and gauge-optimized distance; check `gap-solve7-check-opus.md`.
- row 1141 `gap-crux2-astra62.md`: (3)-(7) acceptance probability and Poincare.
- row 1139 `gap-frameless-2d-astra.md`: template with two marked bonds; folded chessboard.
- row 1231 `gap-solve26-astra62.md` (35) packet, check `gap-solve26-check-opus.md`; row 1222 `gap-solve24-astra62.md` (1)-(2) wall factorization; row 1177 `gap-solve17-astra62.md` (22); row 1224 `gap-mini-solve-q-fable.md` 7.6; `gap-skeleton-max.md` B7 (inverse-square threshold proposal).
- Literature named: Knabe; Gosset-Mozgunov; Froehlich-Israel-Lieb-Simon (chessboard); Durhuus-Froehlich (layer representation); Bhattacharjee, Bhattacharya, Lockwood, Romanov (finite-speed bound); Sussman-Alpoge (transfer and insertion method).

Order of the check (row 1271): (15), (30), (35), (17) first; then (31)-(32) with (20), (25); then the rest.
