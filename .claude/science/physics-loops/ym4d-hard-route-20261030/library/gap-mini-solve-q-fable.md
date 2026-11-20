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
