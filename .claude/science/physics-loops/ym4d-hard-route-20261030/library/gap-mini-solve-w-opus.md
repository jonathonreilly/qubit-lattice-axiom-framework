lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T19:19Z

# gap-mini-solve-w-opus (row 1237)

Started 2026-11-20T07:19Z (date -u), worker pinned at commit 398892bd4 on branch claude/ym4d-hard-route.

Task (row 1237): prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the sense of Jaffe and Witten. First consider how best to attack it, then do it.

Labels: PROVED, ARGUED, GUIDE, OPEN. Numeric runs guide only.

## Step 0. Reading log and the state of the problem (reading only; no new claim)

Read at this pin: GOAL.md; FINISH.md sections How we work, Joining, Working efficiently, Rules and the RESULT lines of
rows 1212-1236; `parts/gap.md` L1-104 (state of attack, routes, lead rules) and L105-222 (obligations, requests,
price); `library/gap-mini-neutral-fable.md` L1-140 (row 1180, the exact statement of (N-phys)); all of
`library/prior/gap-onebound-read-sol.md` (row 1218, the three published sources); the RESULT lines of rows 924-925
((UNIV-K)) and 1025, 1029 (the Tomboulis line).

**Where the problem stands on file (no new claim).**

- The gap clause on the account's tr F^2 sector follows from ONE open lattice estimate, (N-phys), beside the account's
  premises (the T0 chain): row 1179 Theorem BP (check 1183), row 1225 Theorem E-N with row 1212 Proposition D, both
  HOLD AFTER CORRECTION in the cross-provider check row 1232, with rate M_* = (2/L) log(2^18/5041).
- (N-phys) (row 1161 L146-148, row 1179 L304-310, restated in row 1180 Step 1): there are a physical side L and j_0
  such that for every j >= j_0, with n_j = L/a_j and 4 | n_j, some integer u_j with 3 <= u_j <= n_j/K has
  s_j(u_j; n_j) = Tr_neutral (F/lambda_0)^(u_j) - 1 <= 1/2 (K = 512, n_j >= 2^70 in the explicit version).
  In words: the centre-neutral thermal partition function of the box L^3 at temperature K/L is at most 3/2 in vacuum
  units, uniformly in the cutoff.
- Row 1180 Step 2.1: (N-phys) holds iff every fine coupling has a finite seed size nu(beta_j) and
  limsup_j a_j nu(beta_j) < infinity: a lattice gap at each weak coupling plus a bound of asymptotic-scaling type.
- Row 1225 (ARGUED): modulo the ultraviolet hypothesis (UNIV-K) (open since rows 924-925), the crux is the gap of
  Wilson SU(2) at one fixed coupling with a seed side of order exp(c beta_0).
- Row 1218: published work (Bhattacharjee et al., One Bound at One Scale, and One Cube Estimate; Zeng Chunping,
  Hexagon 2611.00543 and 2611.00492) supplies criteria stronger than or different in kind from (N-phys), and none
  proves it at weak coupling. Row 1220 Proposition U: the weak-coupling Corollary 166 of One Cube Estimate also
  holds for the massless Villain U(1) theory on bounded tori, so it is not selective.
- Route families on file: about 36 methods in `parts/gap.md` L52-103 plus the three screening tables of rows 1189,
  1194 and 1199 (`library/gap-mini-solve-b-fable.md`, `-e-fable.md` Step 2.1, `-i-fable.md` Step 1.2), about 32
  families, each with a named failing step. The lead's standing advice (row 998 9.5, `parts/gap.md` L76-78): no
  further fresh-framing exercise by this model family.

**Rule 0a.** `library/open-core.md` holds no gap-lane item (grep for gap, neutral, N-phys, glue: hits only in
hard-core rows 174, 263, 267, 524, none on this lane). The FINISH rows on (N-phys) are 1161-1236. Row 1236
(gpt-6.2-astra, `gap-solve27-astra62`) is running the general continuation now; row 1238 (`gap-mini-solve-x-opus`)
has this same brief and runs after this item.

## Step 1. How best to attack it (judgement; written 07:42Z by date -u)

**1.1 What a proof must contain (cited, not new).** Along the account's trajectory the gap clause needs (N-phys)
(Step 0). By row 1180 Step 2.1 it is a lattice gap at each weak coupling plus a bound of asymptotic-scaling type. Row
1225 (ARGUED) and row 1229 Step 1.1: modulo (UNIV-K) it is a finite mixing length at ONE fixed weak coupling, carried
to finer cutoffs by the renormalisation group, which is the structure of OpenAI's 2D O(3) continuum proof (row 1010).
So a proof needs two parts: (A) the ultraviolet carry, which is (UNIV-K) given the account; (B) one estimate at the
scale where the running coupling is of order one (the band), from a structure valid at every coupling, since no
computed certificate is allowed (GOAL.md) and no expansion converges there (row 1229 Step 2: character ratio about
0.48-0.52 in the window against about 0.045 at the hand-proved strong-coupling edge).

**1.2 The kinds of band-crossing engine in rigorous mathematical physics, and their 4D SU(2) status (rule 0a).** I
listed every proved case I know where a gap or a crossover is obtained with no small parameter at the scale of the
gap, or where the small parameter comes from a dual description. Each kind has its 4D SU(2) entry on file:

| Kind of engine | Proved case | 4D SU(2) status, where on file |
|---|---|---|
| Stiffness of a rigid non-abelian twist (bracket gain) | 2D O(N), N >= 3 (OpenAI; Ding, Huang and Yang, row 1007) | no carrier: Lemma CEN+ (row 1016, check 1020); plate and boundary twists squeeze (rows 1188 PC, 1228 P5); SO(4) twist has no dimensionless stiffness (row 1053); 1-form twist group is Z_2 |
| Positivity or association for the neutral half | 2D O(N) singlets (row 1193) | fails: FKG-NO (row 1213), HF (row 1188), row 1084; (POS-N) open with no consumer (row 1213) |
| Curvature or convexity (Bakry-Emery, Brascamp-Lieb) | strong coupling (row 1218 A Theorem A; B Theorem 5) | uniform forms prove too much (row 1229 Claim A, ARGUED); window form needs a certificate; multiscale forms end at a gap statement (rows 957, 968) |
| Duality to a dilute defect gas with a second small parameter | 3D U(1) (Gopfert-Mack, CMP 82, 1982); 2D Kosterlitz-Thouless | in 4D SU(2) every defect action runs (vortices, instantons): no small fugacity at the gap scale; the deformed theory on R^3 x S^1 is `gap-brainstorm2-max.md` item 25; Route T (rows 678, 862) |
| Large N or an exactly solvable recursion | Gross-Neveu at large N; Migdal-Kadanoff (Ito) | N = 2 is fixed; the Migdal-Kadanoff line is rows 1025, 1029 (Tomboulis bracket (TB)_n open, gives the flux half only) |
| Compactness and rigidity, continuity in beta | none for a gap | rows 1017 (Theorem CR), 1189 table |

I checked further candidates against the screening tables of rows 1189, 1194, 1199 (memory of this worker, re-read
in `parts/gap.md` L52-103): Feynman's orbit-space argument (= orbit-space curvature, method 31), Zwanziger's Coulomb
bound (wrong direction: V_coul >= V_phys), a frame from a maximal-tree or temporal gauge (= tree, Coulomb and
collapse frames, rows 1041, 1045, 1141), a fundamental Higgs flavour twist (row 1199 table), the topological
susceptibility (row 1200, theta sectors), Knabe-type local gap thresholds (row 1032 B2; not frustration-free).
Each is on file with a named failing step.

**1.3 Decision.** I found no carrier for the engines above that is not on file, and no engine of a new kind. So I do
not claim an attack on part (B). Following row 1229's note (its items 2-3), the session goes to two items that are
in scope and can close:

1. **Proposition UNI** (Step 2): a proof of row 1229's Claim A, which is ARGUED there on RECALLED inputs. Statement:
   a volume-uniform Poincare constant for any bounded-range reversible local dynamics of the Wilson measure, held
   along a trajectory, forces correlations to decay at a rate bounded below in lattice units, hence a trivial
   continuum limit (against NT1). Moves: turns the kill of all coupling-uniform curvature, Poincare and log-Sobolev
   routes from ARGUED to PROVED, and gives the necessary rate gamma_j <= C a_j M for any route of that kind.
2. **(CLASS) of (UNIV-K)** (Step 3, if the account text can be fetched at the line numbers row 924 used): row 924
   marks it ARGUED; row 1229 Step 3 calls it a short line-by-line check. Moves: one of the four open sub-items of
   (UNIV-K), the ultraviolet carry, part (A) above.

Neither item supplies the seed (part (B)); the RESULT will say so.

