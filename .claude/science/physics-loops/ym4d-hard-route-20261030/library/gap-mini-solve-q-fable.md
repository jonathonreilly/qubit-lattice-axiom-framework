lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:39Z

# Row 1224 `gap-mini-solve-q-fable`: plain brief "prove that 4D SU(2) Yang-Mills has a mass gap (Jaffe-Witten)"

Provenance: queued for Claude Fable 5.2 max; the Mac mini account hit its Fable weekly limit at about 04:05Z, so per the
lead note of 2026-11-20 04:12Z this row runs on Claude Opus 5.5 (max reasoning) from its start. No Fable text existed in
this file at pin 4260d44bd (file absent). Branch claude/ym4d-hard-route, pin 4260d44bd. No commit, no push (relay copies).

Labels: PROVED, ARGUED, GUIDE, OPEN as the brief asks. A numeric run is never a proof step.

## Status log

- 2026-11-20T04:39Z started (date -u); file created as the first write of this run.
- 2026-11-20T04:41Z Section 1 written (sources read: FINISH rule sections L52-73, L299-350; GOAL.md; parts/gap.md L1-104;
  library/prior/gap-onebound-read-sol.md in full; RESULT lines of rows 1204, 1211, 1215, 1218, 1220).
- 2026-11-20T04:56Z Section 2 written: attack judgement after a registry grep of about 90 candidate terms; choice made.
- 2026-11-20T04:58Z Section 2a written: the computation chosen in Section 2 is A's own Proposition H.4; choice void.
- 2026-11-20T05:01Z Section 3 opened: check of A's Theorem D chain; Lemmas 11.4-11.6 and Proposition 11.7 HOLD.
- 2026-11-20T05:03Z 3.3 written: Theorem 11.8, Lemmas G.1-G.2, Theorem G.4 and the finite-volume half of Theorem D HOLD.
- 2026-11-20T05:06Z 3.4 written: Lemma 6.2, Theorem 6.3, Corollary 6.4, Proposition 2.1, Theorem B HOLD; A's (M) to gap chain checked end to end.
- 2026-11-20T05:08Z Sections 4-6 written (consequences, crux outcome, recommendation).
- 2026-11-20T05:13Z Section 7 opened: kill test of A's (M) in four dimensions through ordered boundary layers (rows 950, 952).
- 2026-11-20T05:15Z 7.1 written: row 950 evidence read and mapped to A's box (GUIDE + ARGUED).
- 2026-11-20T05:17Z 7.2 written: direct GUIDE test in A's box geometry designed; criteria fixed before any run.
- 2026-11-20T05:20Z 7.3 written: A's own statement of this open point (pp. 96-99, 105) recorded; batch 1 running under the lock (started 05:19Z).
- 2026-11-20T05:20Z 7.4 opened: batch 2 criteria fixed (d-dependence at beta 4.0 and 6.0) after seeing only the d = 3 rows of batch 1.
- 2026-11-20T05:21Z 7.4 amended before reading any d = 4 value: beta 2.6 d-scan made primary.
- 2026-11-20T05:27Z 7.5 written: batch 1 results (run 05:19:02Z-05:25:42Z by the log's date -u stamps, under the lock); batch 2 started 05:26Z.
- 2026-11-20T05:31Z 7.6 written: Lemma NC (classical symmetry breaking at the pi-flux face), PROVED by hand.
- 2026-11-20T06:06Z 7.7 written: batch 2 results (run 05:26:00Z-06:05:27Z by the log's date -u stamps, under the lock) and verdicts.
- 2026-11-20T06:07Z 7.8 criteria fixed for batch 3 (replicas at beta 2.6 and 2.8, d = 8) before it runs.
- 2026-11-20T06:08Z Section 8 written (consequences; revises Sections 4 and 6); batch 3 running (started 06:07:14Z by its log stamp), verdict pending in 7.9.

## 1. What the target is, and where the lane stands (read, not re-derived)

The target is the Jaffe-Witten clause for SU(2): a quantum Yang-Mills theory on R^4 (Osterwalder-Schrader axioms)
whose Hamiltonian H satisfies spec(H) in {0} union [m, infinity) with m > 0. This lane takes existence (T0) from the
hard-core lane and works on the gap clause only. Its present reduction (cited, not re-derived here):

- Consumer. Row 1161 (`gap-solve9-astra62.md` L146-148): the gap clause follows from the one-cube neutral bound
  (N-phys) alone; the charged half is branch selection (BS), and row 1179 wrote a bypass for it.
- (N-phys) in explicit form (row 1218 reading, from row 1161 and row 1179 L304-310): there are a physical side L and
  a cutoff index j_0 such that for every j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
  s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2 (U_j the vacuum-normalised periodic spatial-cube transfer,
  H_+ its centre-neutral sector, n_j = L/a_j). It is a TRACE (all neutral levels with multiplicity).
- Row 1184: (N-phys) is the crux lemma (GLUE-FP)_sigma of rows 895 and 920 with other constants.
- Row 1218 (gpt-6.1-sol reading, unchecked): published work on the same target. A = Bhattacharjee, Bhattacharya,
  Lockwood, Romanov, Sessford, Singha Roy, "One Bound at One Scale" (Preprints.org 202611.1282 v1; authors' Zenodo
  copy read): a full-thermal one-scale seed (A-B*) / (A-B**) Z(s,T_0)^2 <= e^{gamma V(s)} Z(s, 2 T_0) on the shape
  window 2T_0 <= s_i < 48 T_0, gamma = y_0/(2 (96 T_0)^3), y_0 <= 1/20, with a proved conditional ascent (Theorem
  7.56) to a full periodic transfer gap. It is STRONGER than (N-phys). B = the same group's "One Cube Estimate
  Implies the Yang-Mills Mass Gap" (Hexagon 2610.00341v7): cube heat-bath criteria BP(n, varpi), different in kind,
  and a real but restricted weak-coupling theorem (Corollary 166, straight-path block law). C = Zeng Chunping,
  Hexagon 2611.00492 and 2611.00543: a common all-channel rate (C-MG) and a conditional tunneling package.
  None proves the lane's open Wilson estimate at weak coupling.
- Row 1220 (Opus 5.5, unchecked): B's Corollary 166 is the near-Haar property of long straight transports and holds
  for massless Villain U(1) too (Proposition U), so it is not selective; at a near-Haar step B's split inequality
  contains the finer-level Poincare inequality (Lemma NULL).
- Rows 1204, 1211, 1215 (gpt-6.2-astra, chain): each ends OPEN at the strict infrared estimate on the weak-coupling
  trajectory (Q of row 1204; the strict infrared bound of row 1211; the matched continuum construction of row 1215).

So every route on file ends at ONE kind of statement: an estimate at one physical scale, uniform in the cutoff, along
the weak-coupling trajectory, that fails for massless comparison models (free photon, Villain U(1) at weak coupling).

## 2. How best to attack it (judgement, with the registry evidence)

**Registry check first (lane rule 0a).** Before choosing, I grepped about 90 candidate terms over
\`library/gap-*.md\`, \`library/prior/gap-*.md\` and \`parts/gap.md\` (file counts at pin 4260d44bd). Almost every
mechanism I could name is on file, with a verdict:

| Candidate I considered | Files | Where the verdict is |
|---|---|---|
| Orbit-space curvature (Singer, Feynman; O'Neill gain; Lott's weighted Ricci tensor) | 24 / 13 / 7 | idea 27 \`gap-brainstorm-max.md\` L309; idea 18 \`gap-brainstorm2-max.md\` L165, L223, G2 L257; F1 \`gap-afield-a-max.md\` L336 |
| Thin twisted torus, centre-stabilised small circle (Tanizaki-Unsal) | 19 + 5 | Route T, row 842 Theorem S1 (\`gap-s1-opus.md\`), Lemma PE false as printed (FINISH L939); I5, I6 \`gap-outside-box-max.md\` L138, L187 |
| Area law (charged decay) gives the neutral gap | 4 | dead in the class: \`gap-measured-vectors-max.md\` L144 (row 1065: a critical end point inside a confined phase) |
| Thermal route: trace anomaly, interaction measure, Stefan-Boltzmann subtraction | 19 | (ANOM), (RATE)_mu, row 931 \`gap-direction-max.md\` L186-232 (the seed is an integrated interaction measure) |
| Small-volume toron dynamics (Luscher, van Baal) as the selective start | 52 / 40 / 46 | row 1215 (levels coalesce at fixed spatial size); the start is selective but no engine carries it (row 998 6b) |
| Langevin / Bakry-Emery / Polchinski / BBD / spectral independence | many | rows 957, 968, 821; method 31 in \`parts/gap.md\` |
| Knabe, detectability, martingale finite-size criteria | 24 | rows 1013-1016, 1186; B's BP family (row 1218) |
| Stochastic quantization (Chevyrev, Hairer), gradient flow | 18 / 14 | on file, no gap mechanism |

Terms with zero hits: "NSVZ", "Cho decomposition", "Kac-Rice", "Weyl law", "Birman-Schwinger", "Fefferman-Phong",
"Kirkwood", "Witsenhausen", "Lancaster", "Kolmogorov-Rozanov". The eigenvalue-counting tools (Weyl, CLR,
Lieb-Thirring, Fefferman-Phong) bound a trace with an error that is extensive in the volume; (N-phys) needs the trace
to precision 1/2, so they cannot replace the gap half (ARGUED; same reason as row 1211 L330: "the known pressure
estimate gives only a bound per spatial site").

**Judgement (ARGUED).**

1. The reduction on file is complete and checked: the Jaffe-Witten gap follows from the continuum datum of T0 and one
   one-scale estimate, (N-phys) (row 1161; check 1162), or from any of its stronger published relatives (A's
   (A-B*), A's (A-M), B's BP; row 1218).
2. Every such estimate is a statement at ONE physical scale in the crossover band, uniform in the cutoff. Every
   proof method on file is either blind (it also holds for a massless comparison model, so it cannot give a gap) or
   not uniform in the cutoff (strong-coupling methods stop near beta_W = 0.36-0.43; rows 1065, 1218).
3. So the only attack that can succeed must bring a NEW selective fact at the physical scale. I did not find one.
   Seventeen plain-brief rows before this one (rows 1188-1223) reached the same point.

**Choice for this row.** I do not repeat a blind search. I take the one new object of the brief, the published
one-scale criteria of row 1218, and settle one exact question about them that no row has settled: **where does each
criterion sit relative to the massless comparison, and by how much must a selective input beat it?** For A's slab
criterion (A-M) this is a sharp computation: I show below that the massless Gaussian field sits EXACTLY at A's
threshold 1/2 in the flat-box limit. That locates the whole selective content of (A-M) in its aspect clause, and it
gives the exact margin that any proof of (A-M) must supply at the physical scale. The work is short, exact and
checkable. It does not move (N-phys); I say so in the RESULT line.

### 2a. The chosen computation is already in A (found before writing it)

Before writing the computation I fetched A's archive copy (Zenodo record 24147967, release v5.0.0, file
\`papers/4Y-MPaper.pdf\`, 157 pages; the same copy row 1218 read) into my own scratch folder and read Section 11.1
(pp. 87-89) and Appendix H.1 (pp. 129-131). A already proves exactly what I planned:

- A, p. 87: "The value 1/2 is the exact limit of the method (Proposition H.4 in Appendix H)".
- A, Proposition H.4 (p. 130), the Gaussian chain with mass mu, 2 cosh kappa = 2 + mu^2: the slab constant is
  sinh(kappa s)/sinh(kappa (w+1)); for w = 2s - 1 it is 1/(2 cosh(kappa s)), and 1/2 for mu = 0; for mu = 0 it is at
  least 1/2 in every admissible geometry. Part (ii): the massless chain has no slab-dynamics gap (gamma_M <= 16/(3M)).
  A's comment after the proof (p. 131): "In the chain the hypothesis is exactly a mass at the scale l/2."
- A, Appendix H.4-H.6 (announced p. 129): four other routes (curvature of the Wilson measure, entropy
  factorisation, tensorisation over blocks of fixed lattice size, the transfer matrix alone) "cannot give (D) without
  an input of the same strength".

So the massless borderline of (A-M) is A's result (credit: Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford,
Singha Roy). I do not restate it as mine. Two facts from the same pages that the lane's files do not record (grep of
"Proposition H.4", "fat box" and "M_{d,m}" over \`library/\` found only row 1218's summary):

- A's exact hypothesis (Definition 11.3 (i), p. 88), written (M_{d,m}(c)): rho^omega(Q-, Q+) <= c for every box Q
  all of whose widths lie in [2d - 1, md - 1], every coordinate i in which Q has width 3d - 1, the splitting into
  widths d, d - 1, d, and every exterior configuration omega. The observables are A^omega_Q, the functions invariant
  under the gauge group G_Q of the vertices INTERIOR to Q ("the boundary condition having fixed the gauge on the
  boundary", p. 87). The boxes are fat; A notes (p. 88, Theorem H.8, Proposition H.17) that the same condition for
  boxes one link wide FAILS in two dimensions along the weak-coupling tuning (a pinned strip breaks a global
  symmetry), while the fat form HOLDS there. This is the lane's method-36 lesson (worst case over a thin layer's
  background is false at weak coupling; \`parts/gap.md\` method 36) found independently by A, with the repair "fat
  boxes only".
- A, p. 87: in four dimensions (M_{d,m}(c)) "is a form of mass generation at the physical scale and it is not
  proved here".

## 3. New choice: a line-by-line check of A's route from slab decorrelation to the cube condition

**Why this, after 2a (ARGUED).** A's Section 11 is a published implication from a one-scale slab hypothesis
(M_{d,m}(c)), c < 1/2, to the cube condition (D), and A's Theorem B (B's Theorem 66 in A's form) takes (D) uniform
along the tuning to the continuum gap. If the chain holds, the lane has a second, published consumer, for an input of
a different kind than (N-phys): a finite-box statement with a boundary condition, no torus, no flux sectors. If it
fails, that is a correction of A's text. Lane rule 9 ("check their proof first") applies. This is a check of THEIR
proof; it is not progress on the crux, and I say so.

Source: A, archive copy as in 2a, pages 87-92. Credit for every statement in this section: Bhattacharjee,
Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy. My part is the check only.

### 3.1 Setting (A 11.1, p. 87)

G compact in U(N), phi a positive continuous class function (the plaquette weight; Wilson and Villain weights
qualify). A box Q has links V(Q) = links with base point in Q. nu^omega_Q is the law of sigma_{V(Q)} with density
proportional to the product of phi over plaquettes meeting V(Q), given the exterior omega; it is the DLR conditional
law. A vertex is interior to Q if all 8 incident links lie in V(Q). G_Q = gauge transformations equal to 1 off the
interior vertices. A^omega_Q = G_Q-invariant elements of L^2(nu^omega_Q). Lemma 11.1 (G_Q-invariance of nu, of the
sigma-algebras sigma(sigma_S) and of conditional expectations; A^omega_Q closed, preserved by every E_A, with
everywhere-invariant versions): **HOLDS** (read; the argument is the standard one: h multiplies each link by fixed
elements, so it preserves Haar measure, plaquette holonomies are conjugated, phi is a class function; the version
F~(sigma) = int F_0(h sigma) dh is everywhere invariant by right invariance of Haar measure on the compact group G_Q).

### 3.2 Verdicts so far

| A's statement | Verdict | Note |
|---|---|---|
| Lemma 11.4 (two projections; Friedrichs angle) | HOLDS | On N^perp: P_k g is orthogonal to N; s = p^2 + q^2; norm of (P_1 + P_2) g squared at most (1 + c) s; s at most (1 + c) norm(g)^2; so X >= 1 - c on N^perp, X = 0 on N, and X^2 - X = Q_1 Q_2 + Q_2 Q_1. Every line checked. |
| Lemma 11.5 (chain of projections) | HOLDS | Non-adjacent products of commuting projections are projections, so nonnegative; each Q_t occurs at most twice in the adjacent sum, so the adjacent sum is at least -2cH; spectrum of H in {0} union [1 - 2c, infinity). |
| Lemma 11.6 (only constants are measurable off every R_t) | HOLDS | The density is bounded above and below because phi is positive and continuous on a compact group and the product is finite; then L^2(nu) = L^2(Haar) with the same null sets, and the product of the Haar integrations over R_0, ..., R_M integrates out the union V(Q). |
| (11.1) (geometry of R_t, Q_t, Q_t^+-) | HOLDS | R_t = [dt, dt + 2d - 1), R_{t+1} = [dt + d, dt + 3d - 1) in coordinate i (relative to alpha); union = Q_t, differences = Q_t^-, Q_t^+, intersection = Q_t^0 of width d - 1; the R_t cover [0, (M + 2)d - 1) since 2d - 1 >= d. |
| Proposition 11.7 (one direction) | HOLDS | Non-adjacent moves: base points of V(R_t) have i-th coordinate at most dt + 2d - 2, those of V(R_{t'}) (t' >= t + 2) at least dt + 2d, so no plaquette meets both and the conditional laws factor. Adjacent moves: E_e = E_{V(Q_t)} preserves K, so E_e x = E_e y = 0 for x, y orthogonal to N; a link of e has no end point interior to Q_t (an interior end point would put the link in V(Q_t)), so G_{Q_t} fixes sigma_e and the slices X_eta, Y_eta are G_{Q_t}-invariant everywhere; the conditional law given sigma_e = eta is nu^{(eta, omega)}_{Q_t}; the hypothesis with omega' = (eta, omega) and Cauchy-Schwarz in eta give the angle bound; Lemma 11.4 then 11.5; ker H = constants by Lemma 11.6. |

Use of the hypothesis: Proposition 11.7 needs the slab bound for the boxes Q_t, whose widths other than i are those
of R. So (M_{d,m}(c)) covers it only when every other width of R lies in [2d - 1, md - 1]. Theorem 11.8 below must
keep R inside that window in every direction it applies 11.7 to; I check this next.

### 3.3 From the slab bound to BP on every large torus (A 11.4 and Appendix G, pp. 90-92, 124-127)

| A's statement | Verdict | Note |
|---|---|---|
| Theorem 11.8 (patch gap (1 - 2c)^4 from (M_{d,m}(c))) | HOLDS | Induction over the four directions. Step k to k + 1: fibre over omega' = links of the patch outside V(R^(k)_tau); G_R is inside G_Pi and fixes omega'; the fibre law is nu^{(omega', omega)}_R; Proposition 11.7 with i = k + 1, M = m - 2, applied to boxes of widths 2d - 1 (directions <= k), 3d - 1 (direction k + 1), md - 1 (directions > k + 1), all in [2d - 1, md - 1] since m >= 4; the conditional laws of a block given the rest agree under nu and nu'. Base k = 0 is equality; at k = 4, V(R^(4)_tau) = B_tau. |
| Lemma G.1 (i)-(iv) (commuting resampling of non-interacting blocks; blocks at coarse distance >= 2 do not interact when K >= 4; cover; only constants are fixed by every P_j) | HOLDS | (ii): in a coordinate with v_i >= 2 the base-point ranges are at cyclic distance at least min{(v_i - 2)d + 2, (K - v_i - 2)d + 2} >= 2; a plaquette's base points differ by at most one per coordinate. |
| Lemma G.2 (Knabe-type step: H_s^2 >= gamma H_s for every patch gives H^2 >= eps H) | HOLDS | I re-derived c_v = prod_i (p - abs(v_i)) (patch count, exact because K >= 2m), the bound -2H <= A_v + A_{-v} <= 2H, the 8/24/32/16 split of the 80 unit displacements, c_v - c_* = p^3, p^2, -p(p^2 - 3p + 1), -2p(p - 1)(p - 2) + 1 with c_* = p^3 (p - 2), Sigma = 72p^3 - 168p^2 + 96p - 16, and eps >= (gamma p - 74)/(p - 2) >= gamma/2 when gamma p >= 148. All algebra checked by hand. |
| Theorem G.4 (finite-size criterion: patch gap gamma gives BP(2d - 1, eps/16) on every even torus with d dividing L, L >= 2md) | HOLDS | Fibrewise: G_Q fixes the exterior, so each fibre of a gauge-invariant F lies in A^omega_Q, where Definition G.3 gives spectrum {0} union [gamma, infinity); integrate in omega; Lemma G.2 on A; kernel = constants by G.1(iv); average over the d^4 shifts; d^4 >= n^4/16 with n = 2d - 1. |
| Theorem D, finite-volume half: (M_{d,m}(c)), c < 1/2, m - 1 >= 148/(1 - 2c)^4 give BP(2d - 1, (1 - 2c)^4/32) on every even torus with d dividing L, L >= 2md | HOLDS | Theorem 11.8 gives gamma_{d,m} >= (1 - 2c)^4 (Definition G.3 has exactly the quantifiers of 11.8: every patch box, every omega, every F in A^omega); Theorem G.4 with gamma = (1 - 2c)^4. |
| Theorem D, continuum half ((D) along the tuning gives the gap (1 - 2c)^4/(1250 e^2 l)) | NOT CHECKED here | It is A's Theorem B applied with varpi = (1 - 2c)^4/32 (16 varpi/(625 e^2 l) = (1 - 2c)^4/(1250 e^2 l), arithmetic checked). Theorem B is A's main continuum theorem; see 3.4. |

**What this gives the lane (PROVED, as a check of A's text; label: checked by Claude Opus 5.5, same session, not an
independent second check).** At every fixed lattice coupling and on every even torus with d | L and L >= 2md:

(M_{d,m}(c)) with c < 1/2 and m - 1 >= 148/(1 - 2c)^4  ==>  BP(2d - 1, (1 - 2c)^4/32).

This step is pure Hilbert-space geometry (alternating projections and a Knabe-type count); it uses no property of
SU(2) and no asymptotic freedom. All of the selective content of A's route sits in (M_{d,m}(c)) itself, and A
says so (p. 87). A's own Proposition H.4 shows the step loses nothing at the massless point (2a).

### 3.4 From BP along the tuning to the continuum gap (A Section 6, pp. 8-9, 15-17; A's Theorem B)

Definitions used (A Definition 6.1, p. 15): BP(n, varpi): varpi Var_mu(f) <= n^(-4) sum_x mu((f - P_x f)^2) for every
real gauge-invariant f, P_x = conditional expectation given the links outside the cube V_x of side n; K = |Lambda|^(-1)
sum_x P_x; q_n = (2 + 1/n)^4; y ~> z iff the boundary links of V_z meet V_y (so |z - y|_inf <= n and at most q_n n^4
cubes y feed one z); Y_1(S) = cubes meeting S, Y_{j+1}(S) = Y_j(S) plus the cubes feeding Y_j(S).

| A's statement | Verdict | Note |
|---|---|---|
| Lemma 6.2 (finite speed: the chain with moves outside Y = Y_{m_0}(S) suppressed differs from K^t on f by at most (2 abs(S)/q_n) norm(f) sum_{m > m_0} (q_n tau)^m/m!, tau = t n^4/abs(Lambda)) | HOLDS | Coupling with common cube choices; a difference reaching S needs a chain x_{s_1} ~> ... ~> x_{s_m} started outside Y_{m_0}(S) and ending in Y_1(S), so m > m_0; union bound with t^m/m! time choices, n^4 abs(S) last cubes, q_n n^4 per earlier step, probability abs(Lambda)^(-m) each. |
| Theorem 6.3 (decay from one cube) | HOLDS | varpi <= 4 from one plaquette trace (at most 4 n^4 cubes see it). Spectral part: on centred elements of A, 0 <= K <= 1 - eps with eps = varpi n^4/abs(Lambda), so norm(K^T) <= e^(-eps T). (The text writes norm(K^T h)^2 <= e^(-eps T) norm(h)^2, which is weaker than what it then uses; the bound it uses, first term <= e^(-eps T) norm(f) norm(g), is right by the spectral bound. Wording only.) Local part: I re-derived the distance bookkeeping: base points of S_f and S_g joined through V_x and a boundary link of a cube in Y_{m_0}(S_f) are at most n(m_0 + 1) - 1 < d apart in each coordinate, so K_Y^t f does not see V_x, x in Z_g. Choice T = floor(k abs(Lambda)/(e^2 q_n n^4)); the tail bound (ez/k)^k e^z <= e^(-k(1 - e^(-2))); tau/q_n <= k/(256 e^2) since q_n > 16; varpi/(e^2 q_n) < 1 - e^(-2). All checked. |
| Proposition 2.1 (covariance decay at rate m on a dense class gives a transfer gap m) | HOLDS | Spectral measure of T at the centred vector; a positive mass on (e^(-m + delta), 1] would beat C_F e^(-mt); the centred vectors are dense in Omega-perp. |
| Corollary 6.4 (lattice gap m_n = varpi/(e^2 q_n n) >= 16 varpi/(625 e^2 n) for every torus limit along tori with BP) | HOLDS | Theorem 6.3 is uniform in L; q_n <= (5/2)^4 for n >= 2. |
| Theorem B (BP(n_k, varpi) on infinitely many large tori at each beta_k, n_k a_k <= l, gives sigma(H) in {0} union [16 varpi/(625 e^2 l), infinity) with 0 simple, for every continuum limit in the sense of A's Definition 6.5) | HOLDS | The lattice gap in physical units is at least 16 varpi/(625 e^2 n_k a_k) >= Delta; <phi_k, T_k^t phi_k> <= e^(-Delta tau) norm(phi_k)^2 passes to the limit (Definition 6.5 at tau and at 0); density in Omega-perp and continuity in tau; the Laplace-transform argument excludes spectrum in [0, Delta - eta] for every eta > 0. The constants do not depend on the size of the observable's support, because the bound is used only through the transfer-matrix gap at each fixed k. |

**Result of Section 3 (PROVED as a check of A's text; one reading by Claude Opus 5.5 max in this row, no failing
step; A's authors keep the credit; a check by another provider is still owed under lane rule 7).** A's conditional
theorem holds as stated:

> If along a tuning (beta_k, a_k), a_k -> 0, with integers d_k >= 2, (2 d_k - 1) a_k <= l, the slab bound
> (M_{d_k, m}(c)) holds for every k with one c < 1/2 and one m >= 4 with m - 1 >= 148/(1 - 2c)^4, then every
> continuum limit (A's Definition 6.5, built from torus limits along tori with d_k | L) has
> sigma(H) in {0} union [(1 - 2c)^4/(1250 e^2 l), infinity), and 0 is a simple eigenvalue.

Every step is elementary Hilbert-space geometry (alternating projections, a Knabe-type count, a finite-speed coupling,
a Laplace-transform argument). Nothing in it is specific to SU(2), and no step is computer-assisted. It is a clean
candidate for a port, and A's archive already formalises some of its arithmetic in Lean (for example
\`YangMills/GapFree.lean\`, \`YangMills/AveragedCondition.lean\`; I did not check the Lean files).

**What it does NOT give.** It does not prove (M_{d_k, m}(c)) in four dimensions along the tuning; A says this is
"a form of mass generation at the physical scale and it is not proved here" (p. 87). Theorem B's continuum limit is
taken infinite volume first at each cutoff; a construction that takes the cutoff first on a torus of fixed physical
side needs A's Section 7 hypotheses (W), (U) (not checked here).

### 3.5 One precision of wording (not a failure)

Theorem B's statement (A p. 2) asks for BP(n_k, varpi) "on all large tori", and statement (D) (A p. 6) leaves the
tori implicit. The proof of Theorem B uses only an infinite set of even tori L >= 2 n_k + 4 (Corollary 6.4), and
Theorem D supplies BP only on tori with d_k | L, L >= 2 m d_k; A's Theorem D says so ("every continuum limit as in
Theorem B along the tori with d_k | L"). So (D) should be read "on infinitely many even tori", with the continuum
limits built along them. This changes no conclusion.

## 4. What the check gives the lane (ARGUED unless marked)

*Revised by Section 8: Section 7 found that A's hypothesis (M) fails at GUIDE level under a centre-valued exterior. Read Section 8 before using items 1-2 below.*

1. **A second checked consumer, of a different kind.** The lane's consumer of row 1161 takes the periodic neutral
   trace (N-phys) to the gap. A's chain (Section 3, PROVED as a check, one reading) takes the finite-box slab bound
   (M_{d_k, m}(c)), c < 1/2, uniform along the tuning, to the gap of every volume-first continuum limit.
2. **It fits the lane's own target.** The lane's target (GAP) is stated on a volume-first limit: each nu_j is a
   limit point of periodic symmetric tori l = 2 L^m at fixed spacing (\`gap-flux-exercise.md\` L80, L93, from
   the account at L1690, L1726, as read by row 731; not re-read here). A's Theorem B uses exactly this order (torus
   limit at fixed spacing, then the continuum). Theorem D needs d_k | (torus side); choosing d_k as a divisor of
   2 L^m for all large m (for example d_k a power of L, with (2 d_k - 1) a_k <= l) makes the account's tori admissible.
   Theorem B gives the gap on the whole gauge-invariant Hilbert space, so in particular on the cyclic sector of
   tr(F^2) in (GAP). The canonical-component clause becomes void, since BP makes the torus limit cluster.
3. **What (M) is, in the lane's terms.** (M_{d,m}(c)) is uniform over EVERY exterior configuration and every fat box
   shape: a strong-spatial-mixing statement at the physical scale (A Proposition 11.11: (M*_w(c)) gives exponential
   decay under every boundary condition). The lane's (N-phys) and row 1211's (17) are periodic statements with no
   worst case. So (M) is a sufficient finite-box input for the uniform physical transfer gap that (17) is used for
   (A Corollary 6.4 then Theorem B), but it is not weaker than the lane's inputs: it adds the worst case over
   boundary conditions. The lane's method-36 lesson (worst case over a THIN layer's background is false at weak
   coupling) does not refute it, because A restricts to fat boxes; A found the same thin-strip failure in two
   dimensions (Proposition H.17) and proved the fat-box form there (Theorem H.8). In four dimensions neither a proof
   nor a refutation of the fat-box worst case is on file. OPEN.
4. **Where the selective content sits.** Every step of A's chain after (M) is blind (Hilbert-space geometry); A's
   Proposition H.4 shows the step loses nothing at the massless point. So, as for (N-phys), the whole difficulty is
   one estimate at the physical scale that must fail for the massless comparison (A Section 12: (D) "fails in the
   Coulomb phase of the abelian theory"). The check does not shorten the crux; it gives the crux a second,
   checked, Lean-friendly consumer.

## 5. The attack on the crux itself: outcome

I did not find a selective one-scale mechanism. The registry check of Section 2 found every mechanism I could name
already on file with a verdict; my one new choice (the massless borderline of A's slab criterion) turned out to be A's
own Proposition H.4. So this row proves nothing new about (N-phys), (M) in four dimensions, (W), (BS) or the
continuum datum. Mass gap NOT proved; nothing disproved.

What I can state about the remaining difficulty, in A's form (ARGUED): a proof of (M_{d_k, m}(c)) along the tuning
must (i) hold for fat boxes of physical size between about l and m l/2, (ii) hold for every boundary condition, (iii)
beat the massless value 1/2 by a margin 1 - 2c with m - 1 >= 148/(1 - 2c)^4 (so a small margin forces very flat boxes:
1 - 2c = 0.5 needs m >= 2369), and (iv) use the non-abelian structure at the physical scale, since the Coulomb phase
of compact U(1) violates it (A Section 12; A Proposition H.4 for the Gaussian chain).

## 6. Recommendation to the lead (process; not a proof claim)

*Superseded in part by Section 8.4.*

- A cross-provider check of Section 3 is cheap: A pp. 8-9 (Proposition 2.1), 15-17 (Definition 6.1, Lemma 6.2,
  Theorem 6.3, Corollary 6.4, Theorem B), 87-92 (Section 11), 124-127 (Appendix G). It would make A's chain the
  lane's second checked consumer. A port into \`library/\` (rule 2) is then short, since nothing in it is
  specific to SU(2).
- This is the eighteenth plain-brief "solve" row (rows 1188-1225) to end at the same wall. Each such row costs
  roughly $10-15. A row that takes ONE precise question with a consumer has done better: for example (a) a kill test
  of A's fat-box worst case in four dimensions (can an exterior configuration create a boundary soft mode that
  correlates Q- and Q+ through a face?), (b) a check of A's Section 7 hypotheses (W), (U) against the account's
  construction order, (c) a check of A's full-thermal ascent (Theorem 7.56 and Theorem F).

## 7. Kill test of A's hypothesis (M) in four dimensions: ordered boundary layers (opened)

**Question.** Does (M_{d,m}(c)), c < 1/2, fail for four-dimensional SU(2) Wilson at weak coupling because some
exterior configuration omega makes the 3D face layer of a fat box order? A excludes thin boxes for exactly this reason
in two dimensions (a pinned strip breaks a global symmetry, A Proposition H.17), and proves the fat form there
(Theorem H.8). In two dimensions the face of a fat box is one-dimensional, where a continuous symmetry cannot break; in
four dimensions the face is three-dimensional, where it can. So A's fat-box restriction need not protect (M) in four
dimensions.

**Mechanism on file (GUIDE, lane rows 950 and 952).** \`gap-sc-max.md\` (row 950) and \`gap-sg2test-opus.md\`
(row 952) found that next to a frozen layered pi-flux slice (u_y = (-1)^x, other links 1) the colour direction of the
first free slice orders for SU(2) between beta 2.4 and 2.5, and (SG2) is refuted at GUIDE level at beta 2.6
(\`gap-sg2test-opus.md\` 4.3: "(SG2) at beta needs that no Dirichlet boundary layer orders"). I read the setting and
evidence next, then map it to A's box.

**Map to A's box (ARGUED, to be checked against rows 950/952 below).** Take the exterior omega center-valued (every
exterior link +1 or -1), with the slice just outside one transverse face of Q set to the layered pi-flux pattern and
the exterior normal links into that face set to 1. Then: (i) the constant gauge transformation h_v = g at every
vertex fixes omega (center elements commute with g), so nu^omega_Q has an exact global SU(2) symmetry that is NOT in
G_Q; (ii) the face vertices are not interior, so the face links are themselves G_Q-invariant observables (A's
A^omega_Q), and the face slice is exactly the "first free slice in temporal gauge" of rows 950/952; (iii) the face
spans the split direction, so it meets Q-, Q0 and Q+. If the face layer orders, a colour-direction reading X from
the face links in Q- and the same reading Y in Q+ have correlation near the squared order parameter over its
variance, close to 1 at weak coupling; then rho^omega(Q-, Q+) >= corr(X, Y) > 1/2 and (M_{d,m}(c)) fails for every
c < 1/2.

### 7.1 What rows 950 and 952 measured, and why it is A's face layer (read; mapping ARGUED)

Row 950 (\`gap-sc-max.md\` 5.1, 5.7; GUIDE, Claude Fable 5.2 max, unchecked as a run) took a half-space slab in
temporal gauge, slices t = 0..T (T = 6, control T = 10), spatially periodic L^3, slice 0 frozen to the layered pi-flux
slice u_xy (u_y = (-1)^x, u_x = u_z = 1), heat bath on the free slices, and measured the first-step field (the
log of w_l u_l^(-1), w = slice 1). The classical first step is a staggered pattern w_l = exp(sigma_l theta n) u_l with
theta near 0.70 and a free colour direction n in S^2 (5.1); the global SU(2) moves n because every u_l is +-1. Result
(5.7, its table): the top eigenvalue lambda of the first-step covariance at k = (pi, pi, 0) grows like L^3 from
beta 2.5 up: at beta 2.6, lambda/L^3 = 0.0655, 0.0525, 0.0442, 0.0416, 0.0375 for L = 4..12, fit m2 + c/L with
m2 = 0.024; at beta 6.0, lambda/L^3 = 0.19; at beta 2.3 and 2.4 it saturates. Controls passed (hot/cold start 1
percent, T = 10 against 6: 3 percent). Its caveat: boxes of side 8-12 are near the bulk deconfinement extent at beta
2.5-2.6, so the order might stop at a finite length (batch 4 went to L = 20 at beta 2.5; growth reported there in
row 950's later batch and in the lane's notes). Row 952 (\`gap-sg2test-opus.md\` 4.3) states the general form: a
statement uniform over Dirichlet slices needs that "no Dirichlet boundary layer orders".

Why this is A's setting (ARGUED). In A's box Q pick a transverse face, say x_4 = alpha_4, and the split direction
i = 1. Let omega be: the exterior slice x_4 = alpha_4 - 1 carries u_3 = (-1)^(x_2), u_1 = u_2 = 1 (pi-flux in the
(2, 3) planes, uniform along the split direction); the exterior normal links into the face are 1; every other exterior
link is 1. Then:

1. Every plaquette meeting V(Q) at the face is u_mu 1 U_mu^(-1) 1 with U_mu a face link: the face links are pinned
   toward u_mu with strength beta, exactly the temporal-gauge first step of row 950 (exterior normal links = 1 play
   the temporal links; A's face vertices are not interior, so no gauge freedom remains there, as in temporal gauge).
2. G_Q acts only at interior vertices, so it can put the interior normal links in temporal gauge; the face layer then
   couples to a free interior of depth w >= 2d - 1, row 950's slab with T = w (row 950: T does not matter at 3
   percent).
3. All exterior links are +-1, so the constant gauge transformation h = g fixes omega: nu^omega_Q has an exact global
   SU(2) symmetry outside G_Q. The face links are G_Q-invariant (both end points non-interior), so the staggered
   readings M(R) = sum over face links l in R of sigma_l Im(U_l u_l^(-1)) (a vector in R^3) lie in A^omega_Q for every
   region R of the face.
4. The face spans the split direction. With R- = face links based in Q- and R+ = those based in Q+,
   X = M(R-)_z and Y = M(R+)_z are centred (global symmetry) and G_Q-invariant, so rho^omega(Q-, Q+) >= corr(X, Y).

If the face layer has long-range colour order, corr(X, Y) tends to m2/(m2 + O(1/d)) as the regions grow, close to 1,
so (M_{d,m}(c)) FAILS for every c < 1/2. Differences from row 950 that a direct test must cover: A's face is finite
with pinned edges (row 950 is periodic), and the readings are region averages across the split, not a Fourier mode.
The strengthening of the order with beta (m2 = 0.024 at 2.6, lambda/L^3 = 0.19 at 6.0) is what would carry the
failure along the weak-coupling tuning (ARGUED: the frustration geometry does not depend on beta, and the layer's
classical stiffness, about 0.3 beta per bond against the 3D Heisenberg critical 0.69 (row 950 5.1), grows with beta).

### 7.2 Direct GUIDE test in A's geometry (design and criteria fixed before any run)

Model. SU(2) Wilson, S = beta sum_p (1 - Re tr U_p / 2), standard beta (the lane's normalisation; A's beta_W is the
same up to A's stated factor). Box Q = [1, 3d - 1] x [1, w]^3 (axis 0 is the split direction i; axes 1-3 transverse),
w = 2d - 1 (the fattest-allowed minimum), plus one exterior shell. Free links: base point in Q (A's V(Q)). Exterior
omega (all links +-1): on the slice x_3 = 0 below the lower face x_3 = 1, u_2(x) = (-1)^(x_1), all other exterior links
1 ("pi-flux"); control omega = all exterior links 1 ("trivial"). Heat bath (Creutz/Kennedy-Pendleton for SU(2);
credit Creutz, Kennedy and Pendleton), checkerboard by direction and parity, own code written in this row, run under
the numeric lock.

Readings. Face links: base on the face x_3 = 1, directions 1 and 2, both end points on the face (all such vertices are
non-interior, so these links are in A^omega_Q). b_l = imaginary (vector) part of U_l u_l^(-1), u_l the pinning value
from the slice below. Primary staggered pattern P1 (row 950 5.1 with x -> axis 1, y -> axis 2): sigma = (-1)^(x_1+x_2)
on axis-1 links, -(-1)^(x_1+x_2) on axis-2 links. M(R) = sum over face links in R of sigma_l b_l in R^3, R- = base
x_0 in [1, d] (inside Q-), R+ = base x_0 in [2d, 3d - 1] (inside Q+). By the exact global SU(2) symmetry,
corr(M(R-)_z, M(R+)_z) = <M- . M+>/sqrt(<|M-|^2><|M+|^2>) =: r. Error by jackknife over 20 bins.
Secondary (reported, not used for the verdict): pattern P2 (same sign on both axes) and the unstaggered sum.

Criteria (fixed now). For each (beta, d):
- r >= 1/2 + 3 SE: (M_{d,m}(c)) FAILS at this beta and d for every c < 1/2 (GUIDE: rho^omega >= r for this omega).
- r <= 1/2 - 3 SE at every point: no refutation at these sizes; the boundary-order route to refuting (M) is not
  supported (inconclusive for the tuning).
- Trend check: if the mechanism is right, r at pi-flux increases with beta at fixed d, and the trivial-omega control
  stays well below 1/2. A pi-flux r above 1/2 with a control also above 1/2 would mean the reading is not the
  ordering mechanism (then report, no verdict on the mechanism).
Points: beta in {2.6, 3.0, 4.0} x d in {3, 4} at pi-flux; controls at beta 3.0, d in {3, 4} with trivial omega;
hot-start repeat at beta 3.0, d = 4. Sweeps: 500 thermalisation (cold start: interior links 1) + 2000 measured.
What a pass cannot show: anything at the tuning's d_k (thousands of lattice units at beta 4) or at beta -> infinity;
it shows failure of (M) at the tested beta and d only. The extrapolation stays ARGUED (7.1).

### 7.3 A already names this question and leaves it open (read before the results)

A pp. 96-99 (after Lemma 11.15, and Lemma 11.16 "pinned two-state chain"): "A boundary condition can, however, push
the slab correlation above 1/2 at a fixed physical scale while the transfer matrix has a gap at that scale"; A's exact
model is a spin chain, "not a gauge theory, so it decides only the abstract implication: no statement about the
transfer matrix or about the vacuum alone can supply the slab hypothesis". A also proves (same pages) that
sup_omega rho^omega is the essential supremum over omega under the torus measure (rho^omega is continuous in omega),
so the slab hypothesis "is a statement about the torus measure alone ... and not about exceptional boundary data of
measure zero".

A p. 105 (Section 11.8, "Two dimensions"): "In four dimensions the seam carries a three-dimensional layer of links ...
Boundary conditions with values in the centre, 't Hooft's twisted ones [57], leave a global conjugation symmetry of
the box, and in the two-dimensional strip such a symmetry is broken at weak coupling (Proposition H.17); in four
dimensions the hypothesis asks that the twisted sectors be disordered at the scale l/2, which is the form that
confinement takes here. We know no boundary condition that refutes (M_{d,m}(c)) along the four-dimensional tuning, and
no proof of it."

So the mechanism class (centre-valued omega, global conjugation symmetry) is A's; A's expectation is that confinement
disorders it at the scale l/2. The test of 7.2 asks whether one explicit centre-valued omega, the layered pi-flux
slice of rows 950/952, orders the face layer instead. The lane's contribution is the specific omega and the evidence
of rows 950/952 and of 7.4; the question is A's. Credit accordingly.

Why confinement need not disorder this face (ARGUED, to be weighed against the run). The face links have both end
points non-interior, so no gauge transformation of G_Q acts on them. The cost of a slow twist of the colour direction
n along the face comes from the face's own plaquettes (all four links on the face), about 0.3 beta per bond in row
950's classical estimate; the bulk cannot gauge it away. That stiffness grows with beta, while the layer's thermal
noise stays of order one. So along the tuning the face is a three-dimensional system with an exact global SU(2)
symmetry and a stiffness that diverges; a 3D system of that kind orders. The bulk is integrated, not quenched, so it
renormalises the face couplings; it does not act as a random field. This argument is heuristic. It does not control
the bulk-induced couplings, which are also of order beta.

### 7.4 Batch 2 criteria (fixed after seeing only the d = 3 rows of batch 1, before any d = 4 row)

Reason: a value above 1/2 at one d refutes (M) at that d only. Along the tuning d grows without bound, so what matters
is whether r stays above 1/2 as d grows (long-range order of the face) or falls (finite correlation length).
Points: pi-flux, P1, beta in {4.0, 6.0}, d in {5, 6} (w = 2d - 1), cold start, 500 + 2000 sweeps; plus beta 6.0,
d in {3, 4}. Criteria: (a) persistence: at beta 4.0 and at 6.0, r(d) >= 1/2 + 3 SE for every d tested and no
decrease of r from d = 3 to d = 6 beyond 3 combined SE: GUIDE evidence that the face order is long-range on the
sizes tested. (b) decay: r falls below 1/2 + 3 SE at d = 6 at both betas: the order is short-range on these sizes;
then (M) is refuted only at small d, and the route to refuting it along the tuning is not supported.

**Amendment (fixed at the time in the status log, before reading any d = 4 value of batch 1).** At beta 4.0 the
boxes d <= 6 are far smaller than the bulk correlation length (two-loop scaling puts a m_0++ near 0.01 there), so beta
4.0 probes only small physical volume, where (M) is expected to fail anyway (A: l must be chosen large). The physical
regime is reachable only near beta 2.6, where a m_0++ = 0.51(3) (Teper, hep-th/9812187, as recorded in
\`gap-trajtest-opus.md\` L158), so a correlation length of about 2 lattice units: a box with d = 5..8 spans 2.5 to
4 correlation lengths between Q- and Q+. Primary scan: beta 2.6, pi-flux, P1, d = 5, 6, 7, 8 (w = 2d - 1; 500 + 2000
sweeps, 500 + 1500 for d = 7, 8), trivial-omega control at d = 6. Criteria:
(a) order survives confinement: r >= 1/2 + 3 SE at d = 6, 7, 8 and no fall beyond 3 combined SE from d = 5 to d = 8:
GUIDE evidence that (M_{d,m}(c)) fails at beta 2.6 on boxes of 3-4 correlation lengths, against A's expectation that
confinement disorders the centre-twisted face at the physical scale;
(b) confinement disorders: r falls with d to below 1/2 - 3 SE at d = 8: the face order is cut off near the physical
scale, as A expects; the refutation then holds only for small physical boxes;
(c) otherwise inconclusive. The beta 4.0 (d = 5, 6) and beta 6.0 (d = 3, 4) points stay as fixed in 7.4.

### 7.5 Batch 1 results (GUIDE; run 05:19:02Z-05:25:42Z by the log's own date -u stamps, under the numeric lock, 57-59 percent memory free)

Code checks first (same lock, before the batch): quaternion product against 2 x 2 matrices (error 1e-16); the
single-link sampler against the exact mean of a under sqrt(1 - a^2) e^(alpha a) at alpha = 0.5, 1.9, 2.1, 6, 20
(200,000 draws each; deviations 0.6, 1.3, 1.1, -0.2, 0.3 SE); the staple sum against a direct change of the total
action for one link move (-2.3039139870525 both ways). Speed 9 ms per sweep at d = 3, 23 ms at d = 4.

| beta | d (w = 2d - 1) | omega | start | P1: r (SE) | <abs(M-)^2>, <abs(M+)^2> | P2: r | unstaggered: r |
|---|---|---|---|---|---|---|---|
| 2.6 | 3 | pi-flux | cold | 0.406 (0.046) | 393, 618 | 0.096 | -0.004 |
| 3.0 | 3 | pi-flux | cold | 0.516 (0.038) | 494, 833 | 0.127 | 0.042 |
| 4.0 | 3 | pi-flux | cold | **0.727 (0.026)** | 788, 1294 | 0.279 | 0.089 |
| 3.0 | 3 | trivial | cold | -0.012 (0.013) | 17, 19 | -0.013 | -0.006 |
| 2.6 | 4 | pi-flux | cold | 0.538 (0.056) | 2362, 3986 | 0.042 | -0.021 |
| 3.0 | 4 | pi-flux | cold | **0.689 (0.050)** | 4875, 7309 | 0.160 | 0.014 |
| 4.0 | 4 | pi-flux | cold | **0.886 (0.013)** | 8239, 11554 | 0.330 | 0.130 |
| 3.0 | 4 | trivial | cold | -0.009 (0.010) | 49, 52 | 0.008 | 0.043 |
| 3.0 | 4 | pi-flux | hot | 0.612 (0.054) | 4610, 6241 | 0.155 | 0.105 |

Against the criteria of 7.2 (bold = r >= 1/2 + 3 SE):
- (M_{d,m}(c)) FAILS for every c < 1/2 at beta 4.0 with d = 3 and d = 4, and at beta 3.0 with d = 4 (cold start;
  the hot start gives 0.612 (0.054), 1 combined SE from the cold value, and alone does not pass 3 SE). GUIDE.
- The trend predicted by the mechanism holds: at pi-flux r rises with beta at each d, and it rises with d at each beta
  (d = 3 to 4: +0.13, +0.17, +0.16). The trivial-omega control stays at zero within 1 SE, and the order-parameter
  scale <abs(M)^2> is 20 to 150 times larger at pi-flux than at trivial omega.
- The secondary patterns carry much less signal (P2 at most 0.33, unstaggered at most 0.13), so the correlation sits
  in row 950's predicted staggered pattern. The asymmetry <abs(M+)^2> > <abs(M-)^2> comes from A's convention
  V(Q) = links based in Q: the lower faces in axis 0 are pinned by the exterior, the upper ones are not.

What this shows and does not show. At beta 3.0-4.0 a box with d = 3, 4 is far below the bulk correlation length, so
these are small physical boxes; there the failure of (M) is a fact about the pinned face, not about confinement. The
regime of A's tuning (boxes of several correlation lengths) is tested only by the beta 2.6 scan of batch 2.

### 7.6 Lemma NC: the classical ground states of the pi-flux box break the global SU(2) (PROVED by hand)

Setting of 7.2: Q = [1, 3d - 1] x [1, w]^3, w = 2d - 1, face Phi = {x in Q : x_3 = 1}, exterior omega_pi (all exterior
links 1 except U_2(y) = (-1)^(y_1) for y_3 = 0). S(U) = sum over plaquettes p meeting V(Q) of (1 - Re tr U_p / 2).
Call U "central on the face" if U_mu(x) is +1 or -1 for every x in Phi and mu in {1, 2}.

**Lemma NC.** If d >= 314, every minimiser of S over G^{V(Q)} has a face link U_mu(x), x in Phi, mu in {1, 2}, that is
not central. So the global conjugation U -> gUg^(-1) (which fixes omega_pi) moves every classical ground state, and
no element of G_Q can undo it, since face links have no interior end point.

*Proof.* (a) Lower bound for central faces. For x in Phi and mu in {1, 2} the plaquette pi_mu(x) in the plane
(mu, 3) based at x - e_3 meets V(Q) and has holonomy u_mu(x) U_mu(x)^(-1) (its other three links are exterior:
u_mu(x) = U_mu(x - e_3) with u_1 = 1, u_2 = (-1)^(x_1), and two normal links equal to 1). For central U its cost is
2 if U_mu(x) != u_mu(x) and 0 otherwise. Let D be the set of face links with U_mu(x) != u_mu(x), and F the set of
(1, 2)-plaquettes based at x in Phi with x_1, x_2 <= w - 1 (all four links based in Phi), |F| = (3d - 1)(w - 1)^2.
The holonomy of u on every p in F is u_2(x + e_1) u_2(x) = -1, so for central U the holonomy of p is
-(-1)^{|D cap p|} and its cost is 2 [|D cap p| even]. The plaquettes pi_mu(x) and those of F are distinct, and each
face link lies in at most two plaquettes of F, so #{p in F : |D cap p| odd} <= 2|D|. Hence
S(U) >= 2|D| + 2 max(0, |F| - 2|D|) >= |F|.
(b) A competitor. Let J be a unit imaginary quaternion, theta = pi/4, s(x) = (-1)^(x_1 + x_2), and on the face
lattice {x_3 = 1} put w_0 = 1, w_1(x) = exp(theta s(x) J), w_2(x) = u_2(x) exp(-theta s(x) J). All factors lie in
the abelian group {+-1} x exp(RJ); every (0, mu)-plaquette is 1 (w does not depend on x_0 and w_0 = 1), and every
(1, 2)-plaquette is u_2(x + e_1) u_2(x) exp(4 theta s(x) J) = -exp(+-pi J) = 1. So w is flat on the (simply connected)
face lattice and w_mu(x) = g(x) g(x + e_mu)^(-1) for some g. Let h = g on the face lattice and h = 1 elsewhere,
V~ = the gauge transform of the all-1 configuration by h (every plaquette of V~ is 1), and let V = V~ on V(Q). The
cost of V comes only from plaquettes meeting V(Q) that contain an exterior link on which omega_pi differs from V~.
These are (i) the pinning plaquettes pi_mu(x), x in Phi: cost 1 - cos theta for mu = 1, 2 and 0 for mu = 0, so in total
(1 - cos theta) 2 (3d - 1) w^2; and (ii) plaquettes containing an exterior link with an end point on the face lattice
outside Q at l_inf-distance 1 from Phi: at most 32 d^2 + 2 such points (the difference (3d + 1)(w + 2)^2 -
(3d - 1) w^2), 4 links each (three face directions and the normal one), 6 plaquettes per link, cost at most 2 each:
at most 1536 d^2 + 96. So S(V) <= 2 (1 - 1/sqrt 2)(3d - 1)(2d - 1)^2 + 1536 d^2 + 96.
(c) For d >= 314 the bound in (b) is below |F| = (3d - 1)(2d - 2)^2 (both sides are polynomials in d; at d = 314:
368,755,316 against 368,146,100, and the difference grows like 4.97 d^3 - 1536 d^2). A minimiser exists (compact
configuration space, continuous S), its action is at most S(V) < |F|, so by (a) it is not central on the face. QED

What Lemma NC does and does not give. It is the classical root of the ordering: the ground states form non-trivial
orbits of the global SU(2), as in row 950's one-step estimate (5.1). It does not show that, inside one ground state,
the readings M(R-) and M(R+) point the same way, and the constant d >= 314 is crude (the edge count is generous);
the GUIDE runs of 7.5 suggest alignment and symmetry breaking at d = 3, 4 already. It says nothing about the
tuning regime, where d grows at fixed physical size and the bulk is not classical.

### 7.7 Batch 2 results and verdicts (GUIDE; run 05:26:00Z-06:05:27Z by the log's date -u stamps, under the lock)

| beta | d (w = 2d - 1) | omega | sweeps | P1: r (SE) | <abs(M-)^2>/N^2, <abs(M+)^2>/N^2 | P2: r | unstaggered: r |
|---|---|---|---|---|---|---|---|
| 2.6 | 5 | pi-flux | 500 + 2000 | **0.659 (0.044)** | 0.0172, 0.0247 | 0.074 | 0.001 |
| 2.6 | 6 | pi-flux | 500 + 2000 | 0.459 (0.072) | 0.0170, 0.0273 | 0.114 | 0.040 |
| 2.6 | 6 | trivial | 500 + 2000 | 0.014 (0.014) | 0.0001, 0.0001 | 0.003 | 0.003 |
| 2.6 | 7 | pi-flux | 500 + 1500 | 0.335 (0.072) | 0.0175, 0.0214 | 0.015 | -0.024 |
| 2.6 | 8 | pi-flux | 500 + 1500 | **0.776 (0.036)** | 0.0178, 0.0189 | 0.101 | 0.079 |
| 4.0 | 5 | pi-flux | 500 + 2000 | **0.849 (0.018)** | | 0.379 | 0.166 |
| 4.0 | 6 | pi-flux | 500 + 2000 | **0.869 (0.020)** | | 0.432 | 0.147 |
| 6.0 | 3 | pi-flux | 500 + 2000 | **0.835 (0.014)** | | 0.415 | 0.134 |
| 6.0 | 4 | pi-flux | 500 + 2000 | **0.907 (0.014)** | | 0.519 | 0.195 |

N = number of direction-1, 2 face links in the region, 2 d w^2 (810, 1452, 2366, 3600 for d = 5..8).

Verdicts against the criteria fixed in 7.4 before the run:
- beta 4.0 (d = 3..6) and beta 6.0 (d = 3, 4): criterion (a) of 7.4 holds: r >= 1/2 + 3 SE at every d, and r does
  not fall from d = 3 to d = 6 (0.727, 0.886, 0.849, 0.869). GUIDE: at these couplings (M_{d,m}(c)) fails for every
  c < 1/2 on every box tried, and the face order is long-range on these sizes. These are small physical boxes.
- beta 2.6, the physical regime (d = 5..8, 2.5 to 4 bulk correlation lengths across Q0): by the amended criteria of
  7.4 the scan is INCONCLUSIVE. Criterion (a) fails (d = 6 and d = 7 are below 1/2 + 3 SE); criterion (b) fails
  (d = 8 is 0.776, far above 1/2). Single points d = 5 and d = 8 pass the 3-SE test. The spread between d = 5 and d = 8
  (0.34 to 0.78) is much larger than the jackknife errors, so those errors miss a slow mode; the d = 8 point alone is
  not a reliable refutation.
- Post hoc observation (not a criterion fixed in advance): at beta 2.6 the within-region order parameter
  <abs(M-)^2>/N^2 stays at 0.017-0.018 from d = 5 to d = 8. A region's squared magnetisation that grows like N^2 is the
  signature of order inside each region of up to 8 x 15 x 15 face sites (for short-range order it would fall like 1/N).
  The noisy quantity is the RELATIVE orientation of the Q- and Q+ regions. That fits a face layer near its own
  ordering transition (row 950 put it near beta 2.45), with slow relative-orientation dynamics.

### 7.8 Batch 3: replicas in the physical regime (criteria fixed before the run)

Purpose: resolve the beta 2.6 scan with an error that does not rely on the jackknife (7.7 shows it misses a slow mode).
Points: pi-flux, P1, d = 8 (w = 15), 500 + 2000 sweeps, cold start, three independent replicas each at beta 2.6
(seeds 801-803) and beta 2.8 (seeds 811-813). At beta 2.8, two-loop scaling from Teper's beta 2.6 value gives
a m_0++ near 0.30 (estimate, not a measurement), about 2 bulk correlation lengths across Q0 (width 7).
Per replica: r as before, plus the integrated autocorrelation time of the per-sweep dot product M- . M+.
Combined: r_bar = mean over the three replicas, err = (replica standard deviation)/sqrt(3).
Criteria, for each beta: (a) r_bar - 3 err > 1/2: (M_{8,m}(c)) FAILS at that beta for every c < 1/2 (GUIDE), at a box of
2-4 bulk correlation lengths; (b) r_bar + 3 err < 1/2: this reading does not refute (M) there; (c) otherwise
inconclusive. The batch-2 point (beta 2.6, d = 8: 0.776) is reported beside the new replicas but not pooled.

## 8. Consequences of Sections 3 and 7 (revises Sections 4 and 6)

### 8.1 What is established, by kind

- PROVED as a check of A's text (one reading, no failing step): A's chain (M_{d_k, m}(c)) along the tuning, c < 1/2,
  m - 1 >= 148/(1 - 2c)^4, gives BP(2 d_k - 1, (1 - 2c)^4/32) on every even torus with d_k | L, L >= 2 m d_k, and then
  the continuum gap (1 - 2c)^4/(1250 e^2 l) for every volume-first continuum limit (Section 3).
- PROVED by hand: Lemma NC (7.6). With the pi-flux exterior, every classical ground state of a box with d >= 314 is
  moved by the global SU(2), which no interior gauge transformation undoes.
- GUIDE, against criteria fixed before each run: under the pi-flux exterior, (M_{d,m}(c)) fails for every c < 1/2 at
  beta 3.0 (d = 4), beta 4.0 (d = 3..6) and beta 6.0 (d = 3, 4); the face correlation does not fall with d there
  (7.5, 7.7). These boxes are small in physical units. In the physical regime (beta 2.6, d = 5..8) batch 2 was
  inconclusive; batch 3 (7.8, 7.9) decides it or not.
- ARGUED: the failure persists along the tuning. The face links have no interior end point, so G_Q cannot gauge a twist
  of the face order away; the face's own plaquettes give it a stiffness of order beta per bond, which diverges along the
  tuning, while its noise stays of order one; the bulk is integrated (annealed), so it renormalises the face couplings
  and does not act as a random field (7.3). Not proved: control of the bulk-induced face couplings.
- ARGUED (A's own continuity lemma, pp. 96-97): rho^omega is continuous in omega, so a failure at omega_pi is a failure
  on an open set of exteriors, which has positive probability under the torus measure. Exteriors near omega_pi have a
  trivial stabiliser, so restricting the observables to stabiliser-invariant ones (as in A's Proposition G.5 (c))
  does not rescue (M) there.
- ARGUED (heuristic dynamics): along the tuning A's uniform patch gap gamma_{d,m} of Appendix G also fails, since near
  omega_pi the patch dynamics must rotate an ordered face by single-block moves against a stiffness of order beta d
  (relaxation time of order m^2 beta d). This would close A's finite-size route to (D) as well; it does not refute (D)
  (BP on the torus) itself, which has no exterior.

### 8.2 What it means for the lane

1. A's slab route is a valid implication whose hypothesis fails at weak coupling in four dimensions at GUIDE level
   (small boxes, pre-registered) and, by the argument above, along the tuning. So it cannot be the lane's second
   consumer in its stated form. This answers, at GUIDE level, the question A leaves open on p. 105 ("We know no
   boundary condition that refutes (M_{d,m}(c)) along the four-dimensional tuning"): the layered pi-flux exterior of
   rows 950/952 is a candidate. A expected the opposite ("the twisted sectors [to] be disordered at the scale l/2").
2. The lane's crux (N-phys) is a periodic statement with no exterior; this mechanism does not touch it. The lane's
   general lesson gains a third instance: statements uniform over boundary data fail at weak coupling through
   boundary-layer order (rows 950/952 for (SC) and (SG2); method 36, row 1139, for thin layers; A's (M) here, for fat
   boxes, because the face of a fat four-dimensional box is three-dimensional).
3. Nothing here proves or disproves the mass gap, (N-phys), (W), (BS) or A's (D).

### 8.3 What stays open

(N-phys) and the continuum datum (unchanged). A's (D) itself. Whether some repaired slab hypothesis (exteriors
restricted in a way that the induction of Theorem 11.8 preserves) holds and still implies (D): OPEN, and the
continuity remark above says a restriction to typical exteriors cannot work. The physical-regime verdict of batch 3:
pending in 7.9.

### 8.4 Recommendation (replaces the first item of Section 6)

- Do not port A's slab chain as a lane consumer in its stated form. The check of Section 3 stays useful as a record that
  the implication is sound, if the lead wants a cross-provider check of it; low priority now.
- The Section 7 finding is about an outside authors' stated open question. Under FINISH rules 0g-0i and 6 any message to
  them is the lead's and the owner's decision, after a check by the other provider. I only flag it.
- The second item of Section 6 (replace plain-brief "solve" rows by rows with one precise question) stands; this row
  is an example: the precise question "does a centre-valued exterior refute (M)?" produced a definite GUIDE answer
  within the row.
