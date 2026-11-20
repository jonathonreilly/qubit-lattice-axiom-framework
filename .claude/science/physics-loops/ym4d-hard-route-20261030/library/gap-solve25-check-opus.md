lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T17:55Z

# Check of row 1227 (`library/gap-solve25-astra62.md`), row 1230

Started 2026-11-20T05:55Z (date -u). Claude Opus 5.5, max effort, Mac mini worker 2.
Cross-provider check of a gpt-6.2-astra author file. Check by hand, line by line; no numeric run is a proof step.

## Plan (at most eight steps)

1. Read the target file in full, the FINISH rules it falls under, and list its numbered statements with their author labels.
2. Check the tunnelling-energy bounds (10)-(15) line by line.
3. Check the eight-state thermal limit (the step from (10)-(15) to the limit).
4. Check the winding-weight bound (22).
5. Check the joint-information example (23).
6. Check everything else in the file (the remaining numbered displays, (27) and the stated OPEN items), and for each cited earlier row read the cited statement and its proof where a step depends on it.
7. Say whether the main comparison restates an earlier row (grep `library/open-core.md`, FINISH rows, earlier gap-solve files).
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with line) and RESULT line.

## Step log

(Each step appends its result below as it finishes.)

### Step 1. Inventory (done 2026-11-20, after reading the target in full)

Target: `library/gap-solve25-astra62.md`, 327 lines, read in full at commit 49128e805. Author pin: `bb8b3eeb2`. Author: gpt-6.2-astra max. Checker: Claude Opus 5.5 max, by hand. No numeric run was used.

Statements, with author labels (line of the label):

| # | Statement | Author label | Line |
|---|---|---|---|
| (1) | one-vertex neutral transfer T = M C1C2C3 M, V = 2 sum abs(v_i x v_j)^2, C_j positive | PROVED | 23-28 |
| (2) | one-coordinate translation bound by D_j^(1/2) | PROVED | 30-34 |
| (3) | confinement along commuting directions | PROVED | 36-45 |
| (4)-(5) | Friedrichs operator and spacing limit (1-lambda_k)/h -> eps_k | PROVED | 49-78 |
| (6) | limiting generator on test functions | PROVED | 71-76 |
| (7)-(8) | heat-trace limit and counting bound N_h(A) <= C(1+A)^(27/2) | PROVED | 82-93 |
| hom. | homogeneous restriction misses the thermal time | PROVED | 95 |
| (9) | fixed-cube localization F <= (Lambda_n + C_n d_beta) I - c_n R | PROVED | 101-128 |
| (10) | tunnelling upper bound E_e <= C_n exp(-c_n sqrt(beta)) | PROVED | 132-138 |
| (11) | lower bounds on E_e and E_{1,+}; upper E_{1,+} <= C_n d_beta | PROVED | 140-170 |
| (12)-(13) | set B; averaged kernel lower bound | PROVED | 148-161 |
| (14) | eight-state thermal limit, trace norm | PROVED | 174-182 |
| (15) | thermal times tau_+, tau_all | PROVED | 184-190 |
| (16) | collective winding estimate, beta >= n^32 | PROVED | 194-203 |
| (17) | bridge bound for P_i at physical coupling | PROVED | 205-210 |
| D-bound | norm of 1_D F at beta = O(log n) | PROVED | 212 |
| (18) | restricting the physical neutral trace | PROVED | 214-221 |
| (19)-(21) | trace of an observation; comparison (20); eigen-expansion (21) | PROVED | 225-247 |
| (22) | physical-scale winding-array weight bound | PROVED | 249-254 |
| (23) | joint determination with small individual traces | PROVED | 260-272 |
| (24) | paired readings | PROVED | 274-279 |
| iter. | iterating the Haar comparison fails (l <= C/beta, v >= c beta^(3/2)) | PROVED | 281 |
| count | counting obstruction for fresh-link sampling | PROVED | 283 |
| (25) | inverse-square trace bound | PROVED GIVEN (PL3) | 289-302 |
| (26) | spectral-weight corollary | PROVED GIVEN reconstruction | 304-309 |
| (27) | exact split of s_+ | PROVED | 315-321 |
| open | upper bound in (27), continuum theory, gap | OPEN | 311, 323 |

Cited earlier rows the steps depend on (file, check on file):

- Row 1215, `gap-solve23-astra62.md`: Gaussian norm L(D), affine Gaussian operations (2)-(3), flat formula S_n(theta), strict inequality, Fourier expansion (7), patch comparisons (16)-(18), flat-cap trial. Check: row 1221, `gap-solve23-check-opus.md`, every statement HOLDS (Claude Opus 5.5, cross-provider for that row).
- Row 1161, `gap-solve9-astra62.md`, (23): one-link character bound, private-link density bound. Check `gap-solve9-check-opus.md`.
- Row 1145, `gap-solve2-astra62.md`, (2): Fourier product bound.
- Row 1155, `gap-solve7-astra62.md`, (9): marked-plaquette exponential moment.
- Row 1171, `gap-solve14-astra62.md`: orbit reconstruction by short trace words.
- Sussman-Alpoge outline lines 3205-3254, (PL1)-(PL3): used as a named input for (25).

Not used as a step: rows 1143, 1179, 1183, 1211, 1218, 1222 (context or pointers only).
