lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:52Z

# Check of row 1215 (`library/gap-solve23-astra62.md`), queue row 1221

Started 2026-11-20T04:52Z (date -u). Checker: Claude Opus 5.5, max effort, Mac mini Claude worker 2. The author of row 1215 is gpt-6.2-astra (another provider), so this check is cross-provider. Source checked: `library/gap-solve23-astra62.md` at commit 9be3e60ef (489 lines). Everything is checked by hand; no numeric run is a proof step here.

Verdict scale per statement: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of the source.

## Plan (at most eight steps)

1. Read the source in full; list its statements with line numbers and labels; read the cited earlier rows.
2. Check the coalescence of the periodic neutral levels at fixed spatial size.
3. Check the twisted neutral gap limit 4 arsinh sin(pi/(2n)).
4. Check the gapless comparison trajectory (14)-(15).
5. Check the monopole and low-energy weight bounds (26)-(29).
6. Check everything else, in source order.
7. Restatement search: grep `library/open-core.md` and the FINISH rows for each positive claim; read the cited earlier statements where a step depends on them.
8. Verdict table and RESULT line.

## Step results

(written step by step below)

### Step 1. Inventory of the source (done 2026-11-20)

The source has 489 lines. Its labelled statements, by line, with the equation each one asserts:

| Lines | Label in source | Content |
|---|---|---|
| 17-24 | PROVED | definitions (1): \(V_\eta\), \(M_\eta\), \(C_\beta\), \(F_{\beta,\eta}\); twist \(\eta_p=-1\) on the 12-faces at \(x_1=x_2=n-1\) |
| 26 | PROVED | gauge projection; flips commute with \(F\); Perron uniqueness; \(F\ge0\) |
| 28-40 | PROVED | (2) norm of the Gaussian kernel \(K_D\) |
| 42-61 | PROVED | (3) \(\lim_\beta\lambda_0=\max_{\rm flat}L(D_A)\): lower bound 50, localization 52-57, patch bounds 59-61 |
| 67-88 | PROVED | (4) evaluation; flat classification 80; curl symbol 82; \(S_n(\theta)>S_n(0)\) 84-88 |
| 90-96 | PROVED | (5) coalescence of periodic neutral levels at fixed \(n\) |
| 100-106 | PROVED | twisted sector: eigenvalues on \(\mathcal H_+\) converge to the Gaussian on \(L^2(N)^{H_A}\) |
| 108-114 | PROVED | (6) twisted neutral gap \(\to 2\mu_n=4\operatorname{arsinh}\sin(\pi/(2n))\) |
| 118-145 | PROVED | (7) \(\lim_\beta\mathcal E_m=c_m/n+O(n^{-3})\) |
| 147-159 | PROVED | (8) twisted neutral trace; multiplicity 20; \(t=\lfloor sn\rfloor\) limit; numbers at \(s=1/512,1/2\) |
| 165-211 | PROVED | factorization at fixed periodic \(n\): vacuum concentration 167, (9), (10), (11), moments 209-211 |
| 213-231 | PROVED | (12) plaquette covariance; (13) vanishing low-energy weight of one plaquette |
| 235-265 | PROVED | (14) comparison trajectory; (15) \(h^8C_u(h)\to\frac{3}{2\pi^4}(\int u)^2\) |
| 269-315 | PROVED | (16)-(19) joint range \(\beta\ge n^{32}\) |
| 317-329 | PROVED, given row 1145 | (20) vague limit of level counts |
| 333-354 | PROVED | (21) many large plaquette angles; failure of a global flat patch; converse given row 1211 (6) |
| 356 | ARGUED | infrared consequence |
| 358-371 | PROVED, given row 1211 (6) | (22) geometry of exceptional faces |
| 375-390 | PROVED | (23) vacuum response; \(0\le\mathcal E_m\le2bn\); pointwise sign counterexample |
| 392-417 | PROVED | (24)-(25) response formula; free-endpoint check |
| 423-435 | PROVED | (26) two-sign bound \(p_\beta=c_\varepsilon e^{-(E_*+\varepsilon)\beta}\) |
| 437-445 | PROVED | (27) sign Fourier coefficients; monopole count |
| 447-451 | PROVED, conditional in identification | one-loop slope \(b_*=11/(3\pi^2)\), \(b_*E_*<1\) |
| 453-470 | PROVED | (28) joint sign law; (29) vanishing low-energy weight; joint with straight transports |
| 472-474 | PROVED | monopole current size; reflection test |
| 478-485 | PROVED | (30) response gives the spectral edge |
| 487-489 | OPEN, RESULT | |

Earlier rows the source cites, with files: 1143 `gap-solve-astra62` (charged trial states, rectangle filling §1); 1145 `gap-solve2-astra62` ((1)-(3) straight holonomies, (5), (11)), its check 1146 `gap-solve2-check-opus`; 1149 `gap-solve4-astra62`; 1155 `gap-solve7-astra62` ((9), (20)-(22), coupling conversion); 1175 `gap-solve16-astra62` (change of time axis, selector); 1177 `gap-solve17-astra62`; 1211 `gap-solve22-astra62` ((6), (10), (18)-(20)); 1051 `gap-direction3-max` (Lemma K4); 678 `gap-ac-lat` (Lemma G); 898 `gap-next3-max` (C4).

The four positive claims named by row 1221 are (5) (lines 90-96), (6) (lines 100-114), (14)-(15) (lines 235-265) and (26)-(29) (lines 423-466). Each rests on lines 17-88 ((1)-(4)), so those are checked with them.
