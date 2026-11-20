lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T18:49Z

# Check of row 1231 (`library/gap-solve26-astra62.md`), queue row 1235

Checker: Claude Opus 5.5 max, Mac mini worker 3, started 2026-11-20T06:49Z (date -u),
at commit 0b36dd3d0 on branch claude/ym4d-hard-route. Cross-provider check of a
gpt-6.2-astra max author run. By hand; no numeric run is a step of any verdict.

## Plan (at most eight steps)

1. Read FINISH.md (rules, efficiency, row 1231/1235) and the full checked file; list its
   numbered statements and the earlier rows it cites.
2. Positive claim A: the neutral energy bands at shrinking physical wavelengths. Check
   line by line, with the cited earlier statements read where the step depends on them.
3. Positive claim B: the thermal-weight bound (30).
4. Positive claim C: the thermal-weight bound (40).
5. Positive claim D: the cube-relaxation necessary update size (35).
6. Everything else in the file, in order (labels PROVED/ARGUED/GUIDE/OPEN, side claims).
7. Is the main comparison a restatement of an earlier row? Grep open-core.md, the
   FINISH rows and the earlier gap-solve files; cite matches.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with line), RESULT line.

## Step log

(Each step appends its result below as it completes.)

### Step 1 (done 2026-11-20T07:0xZ): inventory

Checked file: `library/gap-solve26-astra62.md`, 472 lines, as at commit 0b36dd3d0. Its header says
checkout `a8687ae94`; the file is unchanged in content as far as this check reads it.
Rules read: FINISH.md lines 1-84 and 299-352 (How we work, Working efficiently, Rules), GOAL.md.

Regime fixed by the file (lines 30, 67, 107): lattice units, periodic torus of sides n,n,n,M (M even,
M >= n, then M -> infinity), beta -> infinity with beta <= B log n, open boxes of side
b = ceil(beta^gamma), 0 < gamma < 1/12, smearing radius r = floor(beta^delta), 0 < delta < 1/48,
4 delta < gamma. U = T/lambda_0, E = -log of its eigenvalues.

Numbered statements and their positive-claim class:

| # | line | claim | class |
|---|---|---|---|
| (1) | 21-26 | rank count of a box curl space | input to A |
| (2) | 30-36 | Wilson vs one periodic Gaussian, radii | input to A; extends row 1151 (24) |
| (3)-(6) | 40-72 | single-plaquette covariance and a spectral band of weight t^-8 | side |
| (7)-(11) | 78-127 | transported curvature packet, its Gaussian limit, covariance K | input to A, C-side, D |
| (12)-(13) | 129-150 | 6^3 frame bound for translated packets | input to A; extends row 1222 (20) |
| (14) | 152-161 | **A: neutral bands, count >= kappa (n/r)^3** | positive claim A |
| (15) | 163-167 | thermal lower bound from (14) | corollary of A |
| (16)-(21) | 171-226 | two-link non-abelian term, small balls, restriction of D | side (exclusion) |
| (22)-(25) | 232-267 | normalized radial reading, envelope, trace bound | input to B |
| (26)-(28) | 271-295 | column norm reading; (28) given (PL3) | side |
| (29)-(30) | 299-318 | **B: array of radial readings plus windings, excess o(1)** | positive claim B |
| (31)-(34) | 322-351 | compression of B_k, short-distance norm q_0, mass precision | side |
| (35)-(36) | 357-387 | **D: cube relaxation, varpi r/m -> 0 for m <= C_0 r** | positive claim D |
| (37)-(40) | 393-444 | **C: complete patch of fixed lattice side, excess -> 0** | positive claim C |
| (41) | 446-455 | single-plaquette channel trace 1/(1-rho_u^2) | side |
| (42) | 463-470 | OPEN identity from row 1227 (27) | open, not checked as a claim |

Earlier rows the steps depend on (to read where a step uses them):
row 1151 = `gap-solve5-astra62.md` (22a)-(24) and its check `gap-solve5-check-opus.md` (for (2), (8), (9));
row 1145 = `gap-solve2-astra62.md` (1)-(3) (one-link Fourier multiplier, for (22), (30));
row 1211 = `gap-solve22-astra62.md` (6) (marked-slab tilt, for (19), (23), (39));
row 1222 = `gap-solve24-astra62.md` (20) (for (12));
row 1227 = `gap-solve25-astra62.md` (19), (22), (25)-(27) (for (25), (30), (40), (42));
row 1204 = `gap-solve21-astra62.md` (3) (for (33) upper bound);
row 1215 = `gap-solve23-astra62.md` (12)-(18) (for (4));
row 1218 = `prior/gap-onebound-read-sol.md` BP, B-local (for (35));
SA outline YM4_sketch_500.tex at 31a47c543775, lines 1670-1762 (projection symbol), 3195-3254 (PL3), 3311-3427 (PL5).
