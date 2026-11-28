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

### Step 1 (done about 2026-11-20T06:55Z): inventory

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

### Step 3: claim B, the joint observation bound (30), with its inputs (16)-(26), (29)

Cited inputs read: row 1145 (`gap-solve2-astra62.md` L19-L30: (1) I_d/I_1 <= exp[-(d-1)/(1+6 beta)] by the
Riccati comparison R_k' = 1 - (2k+1)R_k/s - R_k^2 against its positive root e^{-arsinh((k+1/2)/s)};
(2) ||p-1||_inf <= sum_{d>=2} d^2 e^{-(d-1)m/b_beta}); both re-derived here, HOLD. Row 1211
(`gap-solve22-astra62.md` L76-L92: (6), the marked-slab bound from the periodic marked moment by repeating
the marks on a circle of length b, ||A||^b <= Tr A^b <= ||A||^{b-1} Tr A, and factoring each step at
C_J^{1/2}); re-derived, HOLDS. Row 1227 (`gap-solve25-astra62.md` L225-L253: (19) partition trace,
(20) product-bin bound, (22) windings); re-derived, HOLD.

- **(16) L173-L179. HOLDS.** The coordinate-ordered paths take their 1-steps on the root line, so no path
  uses a marked 1-link (third coordinate differs from the anchor's). The spacing-4 subgrid makes the pairs
  plaquette-disjoint. Note for (23): the plaquettes at p - e_2 and p + e_2, which carry G^(1), G^(2), lie in
  the neighbouring columns y -/+ e_2, not in column y.
- **(17) L181-L189. HOLDS.** Good pair: the unshared-face targets are within sqrt(2K/beta) of the witness,
  g_* within 3 sqrt(2K/beta) of 1; on the product of beta^{-1/2} caps every incident deficit is O((K+1)/beta);
  normalizer <= C beta^{-3} from the two unshared faces, cap mass >= c beta^{-3/2} each, so the conditional
  law dominates a_K times the uniform cap product. Under the cap law the nine products (Im h)_j (Im k~)_l are
  orthogonal (cap reflection symmetry kills every term with a scalar coordinate), orthogonal to all
  one-variable terms, with coefficient -Im(e_j g_* e_l); at g_* = 1 the sum over j,l of the squared e'-component
  of e_j x e_l is sum_j |e' x e_j|^2 = 2. Var >= a_K inf_c E_cap(...-c)^2 gives (17).
- **(18) L191-L196. HOLDS.** |xi.(G-G')| <= 2 b_0 |xi| <= 1/2 on |xi| <= 1/(4 b_0); Fejer kernel
  sinc^2(y/2) = Int_{-1}^{1}(1-|t|)e^{ity}dt; the condition sqrt3/L_0 <= 1/(4 b_0) holds for L_0 = 8(R+b_0).
- **(19) L198-L210. HOLDS.** Bad exterior: each bad pair has an incident face of deficit > K/beta for every
  completion, faces disjoint between pairs, so beta sum_D d > Km/2; row 1211 (6) gives
  exp[-alpha K m/2 + 11 m log C_0]. Good exterior: pointwise kernel domination by (18). The neutral-trace
  factor 8 holds: Tr(A Pi_+) <= Tr A for A >= 0 and a projection Pi_+, and Tr(T^u Pi_+) >= Tr(T^u)/8 since each
  twisted integral is >= 0.
- **(20)-(21) L214-L226. HOLD.** At r = n/16, R_n = n^{1/8}/sqrt beta: (R_n + C sqrt beta/r) sqrt(beta/r)
  = O(n^{-3/8}); four independent small balls give n^{-9/2} per anchor, n^{-3/2} after the union.
  (21): <P psi, T P psi> >= lambda_0 (1 - 2p) by positivity of T on (1-P) psi.
- **(22) L232-L237. HOLDS.** Marked 3-links at heights of parity y_1 + y_2: parallel 3-links in one face sit
  in adjacent columns at one height (opposite parities), collinear ones never share a face, temporal faces
  meet one slice. Each stem has >= c r marked links, so row 1145 (2) gives deviation C e^{-cr/(1+6 beta)} per
  column, C r^2 columns.
- **(23) L239-L247. HOLDS.** Upper: one-link adjoint multiplier e^{-2/(1+6 beta)} per straight 3-link,
  E|B_y|^2 <= C(1+beta)/r. Lower: with selected columns four apart, B_y for a selected column carries only the
  shared-face terms of its own pairs, so selected B_y are conditionally independent; covariance >= c/(r beta);
  (18) with beta/sqrt r -> 0 gives P(|B_y| >= a/sqrt(r beta)) >= 1/2; E 2^{-X} <= (3/4)^j gives the
  binomial tail 2^{j/4}(3/4)^j; bad exteriors cost e^{-cr^3}.
- **(24) L249-L257. HOLDS.** |sinc x| <= (1+cx^2)^{-1/2} (c < 1/3 near 0, compactness on [0,2], 1/|x| beyond);
  concavity of t -> log(1+ct|xi|^2) with t_y <= lambda^2, sum t_y = 3 gives (1+c lambda^2|xi|^2)^{-3/(2 lambda^2)};
  Taylor gives C lambda^2 |xi|^4 e^{-c|xi|^2} for |xi| <= lambda^{-1/4}, using sum d_y^4 <= 3 lambda^2; so
  sup|f-g| <= C lambda^2. Gaussian tail by the two-set split and sinh(x)/x <= e^{x^2/6}. Integrating
  min{g + C lambda^2, Ce^{-c|z|^2}} with radius sqrt(C'|log lambda|) gives (24).
- **(25)-(26) L259-L276. HOLD.** For u >= 1 the time-0 slice is in the exterior of the time-u stems, so each
  good bin contributes <= (1+eta_n) Int_A h_lambda; the bad bin contributes <= ||U 1_B||^2 = ||U 1_B U|| for
  u >= 2. (26) is row 1227 (20) with a two-sided reference: ratio of densities to g on |z| <= J is within
  1 +/- C(lambda^2 + eta_n)/min g; u >= 2 is needed so that no temporal face meets both stem arrays.
- **(29) L299-L309. HOLDS.** Joint conditional density <= prod (1+eta) h_lambda; total mass
  [1 + C(beta^2 r^{-1}(1+log r)^{3/2} + r^2 e^{-cr/(1+beta)})]^m = 1 + o(1) iff n^3 r^{-4} polylog -> 0,
  i.e. alpha > 3/4; the whole-array bad bin costs <= m C e^{-cr^2} by U 1_{union} U <= sum U 1_{B_i} U.
- **(30) L311-L318. HOLDS (claim B).** The residue rule (base-coordinate sum = 2i mod 6, edges not wrapping in
  their own direction) is plaquette-disjoint on even n: parallel edges in a face differ in sum by 1 or 1-n
  (odd); perpendicular edges at one corner have residues 2i != 2j; the far pair has equal sums unless exactly
  one base step wraps, and then the edge based at x+e_j in direction i wraps in its own direction and is not
  selected; an edge and its turn partner differ by an odd amount. Each edge lies on one straight line, so
  the 3n^2 holonomies are conditionally independent and near Haar (eps_n <= C n^2 e^{-cn/(1+beta)}). The
  private edges avoid every cell, so Y is in their exterior, and row 1227 (20) gives
  T_{Y,W}(u) <= (1+O(eps_n)) T_Y(u) = 1 + o(1) by (29).

Scope of claim B: (30) is an upper bound on the thermal weight carried by one observation subspace. The
radial readings are normalized by sqrt(3/S_r), which removes their scale; the windings were already
negligible alone (row 1227 (22)). (30) bounds nothing outside that subspace, which the file states at
L318 and L463-L470. New relative to row 1227: (22)-(25) and (29); the winding step is row 1227 (20), (22)
applied with Z = the packet array. First failing step: none.

### Step 4: claim C, the complete fixed patch (40), with (37)-(39), the grid and winding extensions (L442-L444)

Cited input re-used: row 1211 (6) (Step 3). Compared with row 1227 (25)-(26) (`gap-solve25-astra62.md`
L287-L311), see the restatement note at the end of this step.

- **(37) L395-L403. HOLDS.** The filling H_i (dH_i = C_i) has bounded size; in the good-box gauge the
  conjugating transports are within O_Q(b^{-7/2}) of 1, and on {rescaled distances <= H} the rescaled log of
  the product equals the signed sum of rescaled imaginary parts up to O_Q(H^2/sqrt beta); the linear sums obey
  the proof of (9) (fixed coefficients, bounded l^1 norm). The law of z is invariant under a common rotation
  at each root (root gauge at times 0 and u separately), so rotation-averaged tests suffice. Two-time
  spatial-spatial cross covariance: the numerator involves spatial components of k^ only, so it is
  n^{-3} sum_{q != 0} e^{iqx} N(q) e^{-u omega}/(2 sinh omega), bounded by C n^{-3} sum |q| e^{-cu|q|} -> 0
  uniformly in n and x as u -> infinity. Nondegeneracy: d*P_inf H = d*H = sum a_i C_i, whose coefficient on the
  i-th non-tree edge is a_i, so <H, P_inf H> >= ||a||^2/||d*||^2.
- **(38) L405-L413. HOLDS.** Change of variables from non-tree edges to h is a two-sided translation (Haar
  preserving). Scaled derivatives of F_o of order s are O(beta^{1-s/2}); at a maximum the Hessian bound and
  nu_beta(unit scaled ball) >= c give sup rho_o <= C_Q; |grad F|^2 <= 2 C_Q (max F - F) along the gradient
  geodesic; so every scaled derivative of rho_o is a polynomial in (max F - F)^{1/2} times e^{-(max F - F)},
  bounded. Lower bound: p_beta -> Gaussian locally uniformly (weak limit (37) plus equicontinuity), so
  p_beta(1) >= c; E rho_o(1) <= c/2 + C_Q P(rho_o(1) >= c/2); on that event max F - F(1) <= log(2C_Q/c), then
  Taylor along a shortest geodesic. For u >= 2 no face meets non-tree edges of both slices, so the joint
  conditional density factorizes and k_{beta,u} has bounded derivatives.
- **(39) L415-L432. HOLDS.** d_beta(h,1)^2 <= C_Q beta sum_{p in Q}(1-w) (bi-invariant metric, bounded
  filling), so row 1211 (6) gives ||U 1_{D_j} U|| <= C_Q e^{-c_Q j^2}. For a non-invariant f the two-time
  form equals that of its root-conjugation average, which is supported on the conjugation-invariant D_j and
  has smaller norm, so the rare-event bound holds on every unit vector of the unreduced frame. The shell
  trace splits exactly over F (+) (F-perp within L^2(D_j)): dim F <= C(2+j)^D t^{-D}; on F-perp the return is
  E_o[conj(m_0) m_u] with m = <f, rho_o/p_beta>, bounded by E|m_0|^2 (Cauchy-Schwarz, stationarity), and
  Bessel with the Taylor remainder |rho_o - pi_o| <= C t^s gives C t^{2s} Int_{D_j} p_beta^{-1} dnu_beta.
  The choice t = e^{-eps(2+j)^2}/4, D eps < c_Q/2, 2 s eps > C_Q + 1 closes both sums.
- **(40) L434-L440. HOLDS (claim C).** On the ball the partition sums converge to Int k(h,h)/p(h) dnu (k, p
  continuous, p bounded below); for u_n -> infinity this tends to P(|G_Q| < J); shells j >= J cost
  sum C e^{-cj^2}; the trace is >= 1 (vacuum). Second clause: with u_n = ceil(1/e_n), u_n e_n <= 2, so the
  weight of (0, e_n] is <= e^2 (Tr - 1) -> 0.
- **Grid and windings, L442-L444. HOLD.** Equal-time cross entries between patches at separation ~ n/v:
  the time-integrated symbol is continuous on the torus (O(|q|) at 0), a trigonometric polynomial
  approximation has vanishing coefficients at separations outside its finite support mod n. Windings: same
  product-bin step as (30), with O(v(D_0+2)) excluded axial coordinates per direction. The diagonal choice
  v_n = j on [N_j, N_{j+1}) with excess <= 1/j and N_j >= j^4 is valid; no rate is claimed, and none follows.

Scope and restatement (for the row's question): the conclusion "all L^2 readings of a fixed microscopic
patch have vanishing weight at bounded physical energy" is already in row 1227 (26) (L304-L309), for an
infinite-volume state, given (PL3) of Sussman and Alpoge and a time-translation reconstruction, with a
factor [C(1+beta)^{3/2}]^p. (40) is an extension, not a restatement: it holds on the finite spatial cube
used by the thermal seed, without (PL3), and for every u_n -> infinity (row 1227 (25) needs
t >> (1+beta)^{3p/4}). It concerns a patch of fixed lattice side; the grid version covers a vanishing
fraction O(v_n^6/n^3) of the bonds. It bounds nothing about the complementary trace in (42), as the file
says. First failing step: none.

### Step 5: claim D, cube relaxation (35), with (36) and the torus correlation (L367-L373)

Cited input read: row 1218 (`prior/gap-onebound-read-sol.md` L127-L161, L185-L195): BP(n, varpi) is
varpi Var f <= n^{-4} sum_x mu|f - P_x f|^2 on real gauge-invariant f, i.e. A = n^{-4} sum_x (I - P_x) >= varpi
on mean-zero gauge-invariant functions; B-BP allows cube sides n_k up to l/a_k on an infinite set of even
tori R >= 2 n_k + 4; B-local is ||K^t (f - mu f)|| <= (1 - varpi n^4/R^4)^t ||f - mu f|| for f supported in a
box of side <= R/2. The file's m, N are row 1218's n, R. The file's two hypotheses match these.

- **Torus correlation L367-L373. HOLDS.** The periodic time Green's function is
  [e^{-t omega} + e^{-(N-t) omega}]/[(1 - e^{-N omega}) 2 sinh omega]; N omega >= c on q != 0 and N omega -> infinity at
  fixed rescaled momentum (N >> r), so the limit is K(s,0) of (11), including s = 0. Substituting k' = sk,
  s^4 D(s,0) -> |phi^(0)|^2/pi^2 > 0 (L111 chooses Int phi > 0), so K(s,0) ~ a_1 D^2 ~ s^{-8}.
- **(36) L375-L385. HOLDS.** <f,g> = <S_tau f, g> + Int_0^tau <A S_t f, g> dt. First term <= e^{-varpi tau}||f||^2
  under either hypothesis (for B-local, S_t = e^{-tN^4/m^4} sum_j (tN^4/m^4)^j K^j/j!). Second term: only cubes
  meeting supp g count (<= C m^4 (1+b)^3 of them); P_x h depends only on (supp h \ V_x) and the links sharing a
  face with V_x, so a realization without a chain of cubes (consecutive bases within m+3) from supp f to V_x
  leaves V_x unread and (I - P_x) kills it; the number of chains of length k is
  <= C m^4 (1+b)^3 (C m^4)^{k-1}, each with expected (t/m^4)^k/k! ordered ring tuples (factorial moments of
  Poisson clocks, repeated labels included); bridging the temporal gap floor(sr) < N/3 needs
  k >= c_1 s b; for t <= tau = eps s b, (C eps s b)^k/k! <= e^{-csb}. ||f||_inf <= 1 holds since F_r in [0,1].
- **(35) L357-L365, L387. HOLDS (claim D).** For b = r/m >= 1/C_0 the second term of (36) is
  <= C e^{-cs} < K_mag(s)/4 for large fixed s; the cutoff limit then gives
  limsup varpi b <= (eps s)^{-1} log(C K(0)/K(s)) = O(log s / s) for every large s, so varpi r/m -> 0. The tori
  can be taken large enough for beta <= B log N because B-BP and B-local quantify over an infinite set of
  tori at each cutoff.

Scope of claim D: it constrains only cube sides m <= C_0 beta^delta, a slowly growing number of lattice
units. B-BP allows cube sides up to a fixed physical length l/a_k, and (35) says nothing there; the file
says this at L387. It is a necessary condition on the auxiliary dynamics, not a statement about the
physical transfer. First failing step: none.

### Step 6: everything else, in file order

Outline lines read for this step (fetched by URL at 31a47c543775 into a scratch folder; not committed):
1733-1762 (projection symbol P_a = B_a B_a*/omega_a; its 12,12 numerator is |t_1|^2 + |t_2|^2), 3205-3254 (PL1-PL3:
for A, B in the algebra of Q_r and n = |y|_inf - 2r >= 1, |nu(A~ tau_y B) - Pl(A,B)| <= C[(r/n)^2 + (r/n)^3]
N(A)^{1/2} N(B)^{1/2}, for translation-invariant laws with sixteen-family mirror positivity), 3305-3318 (PL5:
cosh E + cos eta_lambda >= 2). The index `sa-index/chunk-03.md` L67-L68, L76 records PL3 and PL5 as proved
conditionally in their account.

- **L212 (variance growth, small balls at r >> beta). HOLDS.** (18)-(19) give P(|A_r| <= R) <= eps_r -> 0;
  integrating (17) on good exteriors gives E|A_r|^2 >= c r/beta. No conflict with (9): at r = beta^delta,
  c r/beta -> 0.
- **(27) L278-L282. HOLDS.** Collinear 3-links share no face, 12-faces contain no 3-link; one adjoint
  multiplier e^{-2/(1+6 beta)} per link occurring once. Different columns or disjoint intervals: <= C r^8 pairs
  times r^{-4} e^{-2d/(1+6 beta)} <= C r^4 r^{-A/3}; overlapping intervals: sum over the endpoints of J of
  e^{-2(|i_1-j_1| + |i_2-j_2|)/(1+6 beta)} <= C(1+beta)^2, times r^{-4} C r^4.
- **(28) L284-L293. HOLDS given (PL3).** With l > 4(d+2), n = l - 2(d+2) >= l/2, PL3 gives C(d+2)^2/l^2 times
  reflected sizes, which are <= ||H_k||_2^2 = O(1) by Cauchy-Schwarz and reflection invariance of the Wilson
  limit. The shell count gives r^{-4} r^3 (d+1)^2 [(d+2)^3 + (d+2)^2 r] <= C (d+2)^4. The label states the
  infinite-lattice premise of the source theorem.
- **L295 (ergodic standardization). HOLDS given (PL3) and ergodicity.** s_r >= c r/beta from (23) passed to
  infinite volume; ||S_r/s_r - 1||_2 <= C beta (d^2+1+beta)/r -> 0 at beta = O(log r); conditional
  independence of stems on distinct slices plus the total-variation form of (24) gives the joint normal limit.
- **(31)-(32) L322-L336. HOLD.** ||U(P_*-P_0)||_HS^2 = T(2) - 1 exactly (P_0 <= P_*, U P_0 = P_0); weight in
  (0,E_0] <= e^{2E_0}(T(2)-1). B_k = M U^k with 0 <= M = sin^2(k p_1/2) <= 1 commuting with U, so
  ||B_k P_*|| = ||M U^{k-1} U(P_*-P_0)|| <= ||U(P_*-P_0)||, and the three off-diagonal blocks are o(1) uniformly
  in k >= 1.
- **(33) L338-L342. HOLDS.** B_k >= 0, so ||B_k|| >= (<x, B_k^j x>/||x||^2)^{1/j}; the j-th moment limit is
  Int (e^{-E} sin^2(p_1/2))^j dmu; E >= |p_1| and max_{x>=0} e^{-x} sin^2(x/2) = e^{-pi/2}/2 at x = pi/2
  (f' = (e^{-x}/2)(sin x + cos x - 1)); the l = 1 term has mass near k = k' = (pi/4,0,0) since
  (k_1^2+k_2^2)|phi^|^2 > 0 a.e. there.
- **L344 (||B_k|| -> q_0). HOLDS given (PL5).** cosh E + cos eta >= 2 is sinh(E/2) >= |sin(eta/2)|, i.e.
  E >= 2 arsinh|sin(eta/2)|; k g(x/k) -> x uniformly on [0,pi].
- **(34) L346-L351. HOLDS.** The symbol difference BB* mu^2/(omega_0(omega_0+mu^2)) is positive semidefinite.
  The k_0 integral actually gives <= C mu^2/|q^| per frequency; the file's C mu^2 |q^|^{-2} is weaker and
  still true (|q^| <= 2 sqrt3), and its shell sum gives C' mu^2. mu = mL/n is o(sqrt(Delta_b)). The reading
  is right: (9) cannot tell a massless from a massive free comparison, so it carries no gap information.
- **(41) L446-L455. HOLDS.** Per colour [[B(0), B(u)],[B(u), B(0)]] with 0 < B(u) < B(0); root averaging
  leaves radial functions; the radial Mehler operator has eigenvalue rho^{2j} on degree-2j radial
  polynomials, which are complete (exponential transform argument); trace 1/(1-rho_u^2). B_inf(0) = 3/6 by
  rank 3 of 6 and axis permutation symmetry; rho_u^2 ~ (1/(pi^2 u^4))^2/(1/4) = 4/(pi^4 u^8).
- **L459 (Gaussian cylinder test). HOLDS.** The v = (1,0,0) term alone gives c_K n^{-4} (all terms are
  positive at x = 0); the cosine mode has exact cross-time covariance e^{-|t| omega(q)} I_3, its singlet
  return e^{-2 t omega}, a point spectral mass at 2 omega(q), physical energy -> 4 pi/L. This concerns the
  free comparison field only, as the file says.
- **(42) L463-L470.** The identity HOLDS (row 1227 (27) with a larger projection; the vacuum is in P_n).
  The OPEN label on the bound is correct.
- **GUIDE and OPEN statements (L3-L15, L76, L171, L230, L355, L391, L461, L470).** Labels are honest: no
  GUIDE statement is used as a proof step. Outline citations spot-checked above match. Not checked: the
  repo-search hits of L3, the CA-I lines cited at L5, row 1141 (2) cited at L461, row 1171 cited at L468.

First failing step in Step 6: none.

### Step 7: is the main comparison a restatement of an earlier row?

Searches run: `grep` of open-core.md (564 lines) for mass gap / heat trace / heat bath / cube relaxation /
B-local: no match; FINISH rows for B-local / heat bath / cube relaxation: no row owns this; earlier gap files
for open-box comparisons, transported curvature, varpi, finite-speed arguments; then the matches read below.

**Main comparison (2) and (9): not a restatement; an extension of row 1151 (24) by the same method.**
Row 1151 (24) (`gap-solve5-astra62.md` L302-L317, checked HOLDS in `gap-solve5-check-opus.md` 9.3) already
compares translation-averaged Lipschitz tests of l plaquette radii at arbitrary, lattice-dependent offsets
with independent open-box Gaussians, by the entropy bound C V Delta_b and Gaussian concentration. The new
parts are: (1), which couples the open boxes to one periodic free Gaussian PZ, so that offsets in different
boxes are compared with the correct free covariance; the extension to every even period M >= n; and in (8)-(9)
transported colour vectors with l^1 weight r^2, tests invariant under separate rotations, uniform in
displacements. The proofs reuse row 1151's steps; the file credits row 1151 and Sourav Chatterjee.

Other comparisons, statement by statement:
- (3)-(6): the logarithmic-coupling, growing-box version of row 1215 (14)-(15) (`gap-solve23-astra62.md`
  L240-L265), which used a diagonal sequence beta_j chosen by convergence on a fixed box. Not a restatement.
- (12)-(13): the reflection argument of row 1222 (20) (`gap-solve24-astra62.md` L309-L330, elementary
  plaquettes, constant 20 per axis), extended to observables of growing width; credited at L137.
- (14): row 1163 (27) (`gap-solve10-astra62.md` L361-L370) gives a count of c d^{-3} neutral levels at
  physical scale d, conditional on (SD-cyl-CA). (14) is unconditional but at lattice scale r = beta^delta.
  Not a restatement; credited at L76.
- (25), (26), (30): the partition trace and the product-bin bound are row 1227 (19)-(20); (30)'s winding step
  is row 1227 (22) with Z = the packet array. New inputs: (22)-(24), (29). Credited at L265, L313.
- (40): extends row 1227 (25)-(26) (see Step 4); acknowledged at L391.
- L344 upper bound: restates row 1204 (3) (`gap-solve21-astra62.md` L48-L60), as the file says. The Wilson
  lower bound (33) is new.
- **(36), the propagation estimate behind claim D: restates a checked published argument that the file does
  not credit.** Row 1224 (`gap-mini-solve-q-fable.md` L199-L210) checked, HOLDS, Lemma 6.2 (finite speed
  of the cube chain) and Theorem 6.3 / Corollary 6.4 (BP(n, varpi) gives static correlation decay at lattice
  rate varpi/(e^2 q_n n) >= 16 varpi/(625 e^2 n)) of A = Bhattacharjee, Bhattacharya, Lockwood, Romanov,
  Sessford and Singha Roy, "One Bound at One Scale" (Preprints.org 202611.1282 v1); B's Theorem 66 carries
  the same constant (row 1218 L145-L148). (36) is that mechanism in continuous time with Poisson clocks. What
  is new in (35) is its conjunction with the Wilson power law K_mag(s) ~ s^{-8} from (9)-(11). This turns into
  a proof, for cube sides m <= C_0 beta^delta and without assuming non-triviality, the ARGUED Claim A of
  row 1229 (`gap-mini-solve-t-opus.md` L120-L130: bounded-block BP along the trajectory would force an
  infinite continuum gap). Rows 1224 and 1229 were queued 03:53Z and 05:27Z, close to row 1231's 05:41Z start;
  they may not have been visible to its author. Correction (wording, not mathematics): credit A's Lemma 6.2
  and Theorem 6.3 at L375-L385.

### Step 8: verdicts and result

Provenance: Claude Opus 5.5 max, Mac mini worker 3, commit 0b36dd3d0, one line-by-line reading by hand,
2026-11-20T06:49Z-07:15Z (date -u). One reading by the other provider; not an audit, no status granted. No
numeric run was made. Every verdict below is an implication from the inputs named in Steps 2-7.

| statement | lines | verdict |
|---|---|---|
| (1) box curl rank count | L21-L26 | HOLDS |
| (2) Wilson vs one periodic Gaussian | L30-L36 | HOLDS (input: row 1151 (24), checked HOLDS) |
| (3) plaquette covariance | L40-L46 | HOLDS |
| (4)-(6) cylinder kernel, scaling, t^-8 band | L48-L72 | HOLDS |
| (7)-(8) packet, good-box linearization | L78-L93 | HOLDS |
| (9) transported-curvature comparison | L95-L107 | HOLDS |
| (10)-(11) Gaussian limit, K(s,y), reflection average | L111-L127 | HOLDS |
| (12)-(13) 6^3 frame bound | L129-L150 | HOLDS |
| **(14) neutral bands (claim A)** | L152-L161 | **HOLDS** |
| (15) thermal lower bound | L163-L167 | HOLDS |
| (16)-(19) two-link term, small balls, restriction | L173-L210 | HOLDS (input: row 1211 (6), re-derived) |
| L212, (20)-(21) | L212-L226 | HOLD |
| (22)-(26) normalized radial reading and traces | L232-L276 | HOLD (inputs: row 1145 (1)-(2), row 1227 (19)-(20), re-derived) |
| (27) | L278-L282 | HOLDS |
| (28); L295 | L284-L295 | HOLD given (PL3) (and ergodicity for L295), as labelled |
| (29) | L299-L309 | HOLDS |
| **(30) packets plus windings (claim B)** | L311-L318 | **HOLDS** (input: row 1227 (22)) |
| (31)-(33) | L322-L342 | HOLD |
| L344 | L344 | HOLDS given (PL5), as labelled; upper bound is row 1204 (3) |
| (34) | L346-L351 | HOLDS |
| **(35) cube relaxation (claim D)** | L357-L365, L387 | **HOLDS** |
| torus correlation K_mag | L367-L373 | HOLDS |
| (36) propagation estimate | L375-L385 | HOLDS; wording correction: credit A's Lemma 6.2, Theorem 6.3 (Step 7) |
| (37)-(39) | L393-L432 | HOLD |
| **(40) complete fixed patch (claim C)** | L434-L440 | **HOLDS** |
| grid and windings extension | L442-L444 | HOLDS |
| (41) | L446-L455 | HOLDS |
| Gaussian cylinder test | L459 | HOLDS |
| (42) identity; OPEN remainder | L463-L470 | identity HOLDS; OPEN label correct |
| GUIDE / OPEN statements | L3-L15, L76, L171, L230, L355, L391, L461 | labels honest; none used as a proof step |

First failing step: none. Statements FAILS: none. HOLDS AFTER CORRECTION: none in the mathematics.

Defects (ranked by what they break; none breaks a consumer):
1. L375-L385: (36) is the finite-speed and decay-from-one-cube argument of Deep Bhattacharjee, Ushashi
   Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy
   ("One Bound at One Scale", Lemma 6.2, Theorem 6.3; checked HOLDS in row 1224), in continuous time. Add the
   credit. Nothing else changes.

Restatement: the main comparison (2)/(9) is not a restatement. It extends row 1151 (24) by the same method,
adding the periodic coupling (1) and transported vector packets. (36) restates a checked published argument
(defect 1). The upper half of L344 restates row 1204 (3), as the file says. The trace steps reuse row 1227 (19),
(20) and (22) with new inputs.

Scope, which the checked file states itself: (14) counts ultraviolet states (physical energy ~ n/(rL) -> infinity).
(30) and (40) bound the weight seen by particular observation subspaces: normalized radial readings plus
windings, and complete patches of fixed lattice side covering a vanishing fraction of the bonds. (35) excludes
a uniform cube-dynamics rate only for cube sides <= C_0 beta^delta, not at a fixed physical cube size. None of
the four bounds the complementary trace in (42). The neutral heat trace at a fixed physical side, and with it
the Jaffe-Witten mass gap, stay open.

RESULT: Row 1235 check of row 1231 (Claude Opus 5.5 max, by hand, first failing step none): all four positive claims HOLD: (14) neutral bands at shrinking physical wavelength, the observed-weight bounds (30) and (40), and the cube-relaxation size (35). Every other numbered statement HOLDS; (28) and L295 hold given (PL3), L344 given (PL5), as labelled. One wording correction: (36) restates the checked Lemma 6.2 and Theorem 6.3 of Bhattacharjee et al., "One Bound at One Scale", and needs that credit. The main comparison (2)/(9) extends row 1151 (24); it is not a restatement. OPEN: the complementary neutral heat trace in (42) at a fixed physical side, hence the mass gap.
