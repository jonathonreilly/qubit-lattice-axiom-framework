lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:15Z

# Check of row 1272 (`library/gap-solve31-astra62.md`), FINISH row 1282

Started 2026-11-20T13:15Z (date -u). Checker: Claude Opus 5.5, max effort, Mac mini Claude worker 3, cross-provider check of a gpt-6.2-astra author row. Pinned at commit 4e5eb6512 on branch claude/ym4d-hard-route. Hand check; no numeric run is a proof step here.

## Plan (at most eight steps)

1. Read FINISH.md (efficiency rules, build-on-published-work section) and the whole of `library/gap-solve31-astra62.md`; list its numbered statements with author labels.
2. Check (25), the finite-volume estimate on gauge-reduced cell boundaries, line by line, with every earlier statement it consumes ((1)-(24) as needed).
3. Check (26)-(29), recovery of elementary curvature correlations from paired long loops, line by line.
4. Read each cited earlier row (statement and proof) where a step depends on it; record whether the main comparison restates an earlier row (grep `library/open-core.md` and the FINISH rows).
5. Check the remaining statements ((30)-(33) and anything else in the file), including the OPEN labels.
6. Cross-check against published work (the Sussman-Alpoge account, `library/prior/gap-onebound-read-sol.md`) for credit and for prior appearance of the claims.
7. Verdict table: HOLDS / HOLDS AFTER CORRECTION / FAILS per statement, with line numbers.
8. RESULT line.

## Progress log

(Each step appends below as it finishes.)

Provenance: Claude Opus 5.5, max effort, commit 4e5eb6512, one reading by one other-provider model; not an audit and not human review. Verdict labels follow the queue row: HOLDS, HOLDS AFTER CORRECTION, FAILS. Line numbers refer to `library/gap-solve31-astra62.md` at this commit (481 lines).

### Step 1 (done 13:25Z): inventory of the author file

The author file has these numbered statements (label as written by the author; all are PROVED unless noted).

| Stmt | Lines | Content |
|---|---|---|
| partition | 17-21 | Borel cells of chord diameter at most delta = 1/(5 sqrt(1+beta)), inversion-equivariant |
| (1) | 23-28 | Dobrushin coefficients c_ij = beta delta^2 m_ij / 4 of the fixed-label law, row sum <= 9/50 < rho = 1/5 |
| (2) | 30-36 | boundary coupling bound with B^D = sum_k C_DD^k C_{D,D^c}, row sums <= rho^dist |
| (3) | 38-49 | (1-rho) E Var(f given labels) <= E_s(f) |
| (4) | 51-55 | spectral corollary |
| (5) | 59-64 | label prediction across a collar |
| sep. ins. | 66 | two separated insertions |
| (6) | 68-78 | density of joint law of U_A, U_Z given labels off A within e^{+-h_r} |
| (7) | 82-94 | v_t lower bound from label constant with volume factor |
| (8) | 96-100 | gauge-sector comparison, cited from row 1254 (8) |
| (9) | 102-106 | conditional consequence |
| (10)-(13) | 110-155 | volume-free comparison v_t >= vbar_s/(K^2 (t/s)^4 + vbar_s/(1-rho)) |
| (13a) | 161-169 | label-law single-link Dobrushin test fails |
| (14)-(15) | 173-193 | unsigned conditional label correlations > 2 with probability -> 1 |
| (16) | 199-207 | cell disintegration: E_{(k+4)b}(f) >= (k/(k+4))^4 [E^Y_k(M_W f) + norm((I-M_W)f)^2] |
| wall factor | 209 | oscillation of log K_C at most 72 beta b^3 d |
| (17) | 211-224 | v_b/16 <= vtilde_2, v_{8b} >= c_1 vtilde_2, c_1 = 1/1056 |
| (18) | 228-251 | adjacent wall-label blocks strongly dependent |
| (19) | 255-266 | tree-reduced variables Q: vhat_4 >= v_b/256, v^inv_{10b} >= vhat_4/200 |
| (20) | 270-280 | for every tree choice, adjacent reduced groups have max correlation -> 1; distant covariance bound |
| (21)-(22) | 286-308 | one-link averaging norm in fixed representation; product suppression |
| (23)-(24) | 310-349 | finite-band versions |
| unrestricted | 321-333 | count of Haar-centred components cannot replace angular restriction |
| **(25)** | 353-369 | **main positive claim 1**: pinned straight coarse transports, v^inv_{10b+2} >= theta_b (10b/(10b+2))^4 vhat_4(1)/200 |
| pinned (20) | 369 | adjacent invariant correlation persists in the pinned law |
| **(26)-(29)** | 373-398 | **main positive claim 2**: joint law of (A,B) given I^c; moments of Z_p; covariance transfer |
| reflected forms | 402-407 | reflection seminorm comparison |
| (30) | 413-428 | Abelian Gaussian comparison: vanishing coarse constant |
| (31)-(32) | 434-460 | Lovasz local lemma selection; Haar averaging along long tree segments |
| (33)-(34) | 464-479 | conditional mass gap bound H >= v_*/(78125 e^2 L) from liminf vhat_4(1) > 0 plus a matched continuum |

Dependency chain of (25): (1) -> (2) -> (6) -> (10) with (11)-(13), applied on the coarse lattice (line 222) -> (16) -> (17) -> (19) -> (25), plus row 1254 (9) (straight-path density estimate of Bhattacharjee, Bhattacharya, Lockwood and Romanov) and row 1254 (6).
Dependency chain of (26)-(29): the one-link Fourier/convolution estimate of row 1145 (1)-(2) as used in (20) (line 280), with the private-link selection of line 280 and line 369.
