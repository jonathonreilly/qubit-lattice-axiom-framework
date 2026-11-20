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

### Step 2: claim A, the neutral bands (14), with its inputs (1), (2), (7)-(13), (15)

Cited input read: row 1151 (`gap-solve5-astra62.md` L255-L317: (21), (22a), (22b), (23), (24) and proofs)
and its check (`gap-solve5-check-opus.md` L359-L393: 8.1, 8.2, 9.2, 9.3 all HOLDS). (24) is the
open-box comparison credited there to Sourav Chatterjee's weak-coupling free-energy method.

- **(1) L21-L26. HOLDS.** ran P is inside H because a periodic curl restricted to the faces internal to a
  cube is the curl of the restricted 1-form. rank d = 4V - [(V-1) + 4] = 3(V-1) (closed 1-cochains are
  gradients plus four periods); the Fourier count in the file gives the same. Each kept cube has curl rank
  <= 4b^4 - (b^4-1) = 3b^4+1, kept cubes cover at most V sites, omitted faces are O(V(1/b+b/n)). So
  Tr(P_H - P) <= V/b^4 + CV(1/b+b/n) + 3, which is (1). The coupling claims hold: P_H Z on the faces internal
  to one cube is the projection D(D*D)^{-1}D* of Z there, independent across cubes; the dilation costs
  O(V/b^2); Cauchy-Schwarz over translates gives C sqrt(l(1/b+b/n)).
- **(2) L30-L36. HOLDS, given row 1151 (24).** The extension from periods T, 2T to every even M >= n is
  correct: in the proofs of (22b) and (24) the period enters only through the leftover fraction of the time
  circle (< b/M <= b/n) and through trace Hoelder along an axis, which needs positivity of the layer
  operators and no bound on the period. Error terms: the (1) term is D sqrt(l(1/b+b/n)) <= D sqrt(l Delta_b)
  (Delta_b >= 1/b+b/n once log beta >= 1); the zero-on-omitted-faces term is 2||f||_inf l C(1/b+b/n).
- **(3) L40-L46. HOLDS.** Clipped products have bound J^2 and Lipschitz constant O(J^{3/2}); with
  J = A log beta the (2) error is O((log beta)^2 beta^{-gamma/2}) <= C beta^{-eta} for 2 eta < gamma. The
  Gaussian covariance of two half squares is 3P(p,q)^2/2. The M -> infinity limit uses that T is trace class
  with a simple top eigenvalue (strictly positive kernel on gauge-invariant functions).
- **(4)-(6) L48-L72. HOLD.** (4): the 12,12 entry of BB*/|k^|^2 is (q1^2+q2^2)/(|q^|^2 + 2 - 2cos k0); the
  k0-integral is e^{-|t| omega}/(2 sinh omega) with cosh omega = 1 + |q^|^2/2, i.e. omega = 2 arsinh(|q^|/2).
  (5): b(s,0) = (2pi)^{-3}(1/3)(4pi)(6/s^4) = 1/(pi^2 s^4). (6): t^8 times the (3) error is
  beta^{8 delta - eta} -> 0 for 8 delta < eta; the limit law y^7 e^{-y}/7! has Laplace moments (k+1)^{-8};
  the band coefficient 3(d^8-c^8)/(2 pi^4 8!) is right.
- **(7)-(8) L78-L93. HOLD.** A_r rotates by Ad(g_x) under a gauge change; the centre seam signs cancel in
  Ad. (8): Taylor of four small exponentials, then K = D*D >= c b^{-5} on comb coordinates (row 1151 L274,
  from row 1143 (14)), then |Im U_p|^2 = 1 - w^2 <= 2(1-w).
- **(9) L95-L105. HOLDS.** The l^1 norm of the weights is C_phi r^2, so: transport error r^2 * r b^{-7/2};
  linearization error r^2 b^{-1}; entropy error r^2 sqrt(Delta_b) (Young: the RMS over anchors of w*h is
  <= ||w||_1 ||h||_2 / sqrt V, so D = C r^2/sqrt V; Gaussian concentration then gives C D sqrt(C V Delta_b));
  open box to PZ by (1). Separate rotation invariance at each anchor is what allows a separate box gauge
  per window and a single frame for PZ.
- **(10)-(11) L111-L127. HOLD.** The weight transform is r^2 S_r(rq); summation by parts m times gives
  |S_r(k)| <= C_m |k|^{-m} on the rescaled zone. det(I + 2 Sigma)^{-3/2} with Sigma = [[v,D],[D,v]] gives
  (11); its binomial series has positive coefficients and converges at |D| <= v. sigma is even and absolutely
  continuous, so D is real and D^{2l} is the transform of the 2l-fold product pushed to (sum|k_i|, sum k_i).
  The reflected vectors at one anchor converge jointly to (sign) times the same Gaussian vector (singular
  limit covariance), so the eight-reflection average has the limits of e^{-|A|^2}.
- **(12)-(13) L129-L150. HOLD.** (13) is the eigen-expansion of Tr(F_a T^{u-w} F_b T^{n-u-w}) for the
  positive spatial transfer T_1 at finite M, with real symmetric slab kernels (each reading is invariant under
  the axis reflection through its anchor plane); each pair gives a rank-one positive matrix atom.
  The total mass satisfies Int dSigma <= K_w <= K_0. Differences: 2K_u - K_{u+h} - K_{u-h} has weight
  -(1-z^h)^2 (z^{u-h-w} + z^{n-u-h-w}); the circular gaps are >= 2h (also the wrap gap, since
  J = floor(n/(2h))), so the sum over the other centres is <= 2(1-z^h) z^{h-w}/(1+z^h) <= 2. With
  2|c||c'| sqrt(ab) <= |c|^2 a + |c'|^2 b against the positive matrix density, off-diagonal <= 2, diagonal
  ||(1-tau_h)g||^2 <= 4: factor 6 per axis. Grouping by the axis-1 index gives transverse combinations that
  keep the axis-1 reflection invariance, so the iteration over three axes is valid: 6^3.
- **(14) L152-L161. HOLDS (claim A).** Integer-s moments of z = e^{-rE} converge, so the spectral law of
  V_0 converges weakly on [0,1]; the limit puts positive mass on every open band (l = 1 term: phi^ is entire
  and nonzero, so |phi^|^2 (k1^2+k2^2) L(k+k') > 0 off a null set) and no mass at prescribed energies. The
  frame step is right: sum_m |<e,V_m>|^2 = sup_{|c|=1} |<e, sum conj(c_m) V_m>|^2 <= 6^3 for each unit e in
  ran P_I. So Tr P_I >= J^3 w/(2*6^3), J ~ n/(16r).
- **(15) L163-L167. HOLDS.** Including the reading "liminf u_n/[r log(n/r)] >= 3/d for every d > 0".

Scope of claim A (agrees with the file's own RESULT): the bands sit at lattice energy ~1/r with
r = floor(beta^delta), i.e. physical energy ~ n/(rL) -> infinity. (14) is a count of ultraviolet states; it
bears on no low-energy question and on no mass gap. First failing step: none.
