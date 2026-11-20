lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T20:16Z

# gap-mini-solve-z-opus: the mass gap for four-dimensional SU(2) Yang-Mills (row 1243)

Queue row 1243 of `FINISH.md`, pinned at commit 5fe43dc83 on branch `claude/ym4d-hard-route`.
Started 2026-11-20T08:16Z (date -u). Worker: Claude Opus 5.5, max effort, Mac mini worker 3.
No subagents. Labels: PROVED, ARGUED, GUIDE, OPEN. No numeric run is a proof step.

## Step 0. Reading log (reading only; no new claim; written 08:55Z by date -u)

Read at this pin: GOAL.md; FINISH.md sections Where it stands, How we work, Joining, Working efficiently, Rules,
and the RESULT cells of rows 924-925, 1007, 1009-1010, 1216-1220, 1225, 1228-1229, 1233-1238, 1241-1246;
`parts/gap.md` L1-104 (state of attack, routes, lead rules) and the obligation list L105-222 (skimmed);
all of `library/prior/gap-onebound-read-sol.md` (row 1218); `library/gap-mini-branch-fable.md` L285-330
(the exact (N-phys) and Theorem BP); `library/gap-mini-solve-w-opus.md` L12-94 (row 1237's map of engine kinds);
the RESULT lines of rows 1192, 1201-1202, 1204, 1211-1215, 1222, 1224, 1227, 1239 and of row 842 (S1).

**Where the problem stands on file (no new claim).**

- For SU(2) along the account's trajectory, the Jaffe-Witten gap on the account's tr F^2 sector follows from ONE
  open lattice estimate, (N-phys), beside the account's premises (row 1179 Theorem BP, check 1183; row 1225
  Theorem E-N, check 1232).
- (N-phys) (row 1161 L146-148; row 1179 L304-310): at one physical side L and for all cutoffs j >= j_0, the
  periodic centre-neutral excited trace of the cube n_j^3 at some time u_j <= n_j/K is at most 1/2.
- Row 1180 Step 2.1: (N-phys) iff each fine coupling has a finite seed and limsup a_j nu(beta_j) < infinity.
  Row 1225 (ARGUED): modulo the ultraviolet carry (UNIV-K), the crux is the lattice gap of Wilson SU(2) at one
  fixed weak coupling beta_0, with a finite seed.
- Engines on file and their 4D SU(2) status: row 1237 Step 1.2 table (stiffness of a rigid non-abelian twist;
  positivity; curvature; dilute defect gas; large N or exact recursion; compactness and continuity in beta), the
  36 methods of `parts/gap.md` L52-103 and the screening tables of rows 1189, 1194, 1199. Each has a named failing
  step. Hellmann-Feynman forms (40 files), trace-anomaly forms (25 files), continuity in beta (Theorem CR, row
  1017) and the twisted thin torus (row 842 S1, Lemma PE rows 862 and 880) are among them.
- Row 1218's sources: (A) Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy, a one-scale
  full thermal seed with a proved conditional ascent; (B) the same first four authors, cube-dynamics criteria
  and a weak-coupling bound for straight-path block variables (Corollary 166); (C) Zeng Chunping, a common
  all-channel rate. None proves (N-phys) at weak coupling. Row 1220: B's Corollary 166 also holds for massless
  Villain U(1) on bounded tori, so it is not selective. Row 1224: A's slab criterion fails for a centre-valued
  exterior (Lemma NC, with a GUIDE run).

**Rule 0a.** `library/open-core.md` holds no gap-lane item (checked again before Step 1; see there). Rows running
on the same brief now: 1241 (`gap-mini-solve-y-opus`), 1244 (`gap-mini-solve-aa-opus`), 1246 (`gap-solve28-astra62`);
checks 1242 (of row 1233) and 1245 (of row 1236) are running. This row does not repeat their items.

## Step 1. How best to attack it (judgement; ARGUED; written 09:25Z by date -u)

**1.1 What a proof must contain (cited, not new).** Beside the T0 chain, the gap clause reads (N-phys) only
(Step 0). Modulo the ultraviolet carry (UNIV-K), (N-phys) is a lattice gap of Wilson SU(2) at one fixed weak
coupling beta_0 with a finite seed (rows 1180, 1225, 1229, 1237). The seed box sits where the running coupling is
of order one (the band). Two kinds of input are possible (lead rule W2, `parts/gap.md` L97): (K-one), a property of
the measure at one scale in the band; (K-flow), a step that starts from first-passage data and is carried through
the band by an identity that fails for U(1), for frozen groups and for products with a massless factor.

**1.2 Why both kinds stop (ARGUED; each clause cites a statement on file).**

- (K-one) needs a number at the band. No convergent expansion reaches the band (character ratio about 0.48-0.52
  in the window against about 0.045 at the hand-proved strong-coupling edge, row 1229). GOAL.md forbids a computed
  certificate. So a (K-one) seed has no hand proof unless a structure valid at every coupling supplies it.
- (K-flow) needs an exact identity with a non-abelian gain that holds at order-one response. In the 2D O(N) proofs
  this identity is the Ward identity of a GLOBAL non-abelian symmetry, with its bracket term (rows 1009, 1010).
  In 4D lattice gauge theory every link symmetry that preserves each plaquette term is central, for every gauge
  group (Lemma CEN, Corollary CEN2, row 1011; CEN+ modulo gauge maps, row 1016). This is the lattice form of a
  general fact: global symmetries that act on 1-form fields (higher-form symmetries) are abelian (Eckmann-Hilton
  argument; Gaiotto, Kapustin, Seiberg and Willett, 2014; RECALLED, not rebuilt). For SU(2) the only such group is
  the centre Z_2. Its Ward identities read one factor of a product (the flux half), so Lemma PT binds them for the
  neutral half that (N-phys) needs.
- The non-abelian bracket of 4D Yang-Mills does enter one identity: the Ward identity of background gauge
  invariance. That identity needs a colour frame. A frame costs at least the non-abelian part NA of the pin
  (Lemma FR, row 1011 7.3, PROVED). On typical Wilson fields NA is of order 1/b per site: E lambda_x >= 1/(64(1+6b))
  on every four-torus with periods at least 3, and a spatially simultaneous form except with probability
  e^(-c R^d) (row 1141, `gap-crux2-astra62.md` (8) and Phase 1; all 34 statements HOLD in check row 1142; earlier
  form 1/(3924 b^2) by row 1018 Lemma NAB, check 1022). So the frame's cost is mass-like at link level at every
  coupling, and a frame exists only at block scales where the non-abelian part of the block field is small, above
  the band ((N1)-(N3) of row 1011 7.4). In the form of row 1018 5.5 the open selective half is (DEC): non-abelian
  content at scale l must lower the cross-cell response at scale 2l; "no exact identity is found" (row 1018 L352).
- Every other engine kind on file (positivity, curvature, dilute defect gas, large N or exact recursion,
  compactness, Hellmann-Feynman level derivatives) has a named failing step (row 1237 Step 1.2; row 1238 Step 1.2).

**1.3 Decision.** I found no engine of a new kind, and I do not claim an attack on the seed itself.

Correction, written 09:52Z by date -u, before any Step 2 work. The first version of this section (09:25Z) said that
the size of NA on typical fields was ARGUED only, and chose to prove it. That was wrong: row 1141 proved it and row
1142 checked it (see the bullet above, now corrected). My rule-0a grep at 09:24Z covered `open-core.md` and the
FINISH rows that name "NA(omega)" or "Lemma FR"; it did not open rows 1018, 1022 and 1141, which state the bound in
other words ("E lambda_x", "bare estimate"). The planned Step 2 is withdrawn, so this row does not repeat row 1141.

New plan. The sharpest open form on file is (DEC) of row 1018 5.5, with its tests (row 1018 5.5 table) and the
sign structure of the frame-twist Hessian (row 1011 7.3, row 1018 4.1-4.2: H = direct term - Var(current)). Step 2
asks one precise question about it that I did not find on file: can an exact identity of the Wilson measure, with no
frame and no symmetry, fix the SIGN of the non-abelian part of the net response at order-one coupling? I test the
question against the comparison models already on file before claiming anything.

## Step 2. The sign question (ARGUED; written 10:12Z by date -u)

**2.1 The question, made exact from statements on file.** For a pinned cell with boundary data omega and a
boundary move B extended to the interior by a flow V, row 1018 Lemma FLOW (PROVED; Proposition A (ii) of row 1011)
gives the exact split

    H_c(omega; B) = - E_omega[V Psi_V] - Var_omega(Psi_V) <= - E_omega[V Psi_V],    Psi_V = V A + div V,

for EVERY extension V, with equality iff Psi_V is constant. So every V gives an upper bound on the stiffness, and a
(K-flow) step of the 2D kind ((DEC) of row 1018 5.5) needs a V whose direct term -E[V Psi_V] at scale 2l is below
the response at scale l by a margin of order NA. Write delta H := H_c - H_cl for the correction to the classical
stiffness. Known signs:

- U(1), Gaussian (non-compact) form, any pin: delta H = 0 exactly, since the pinned free energy is quadratic in the
  boundary data with the classical Dirichlet-to-Neumann coefficient (PROVED, elementary; this is the "zero gain"
  of the abelian model, row 1011 tests).
- SU(2), supremum over pins: delta H is mass-like and positive, the best uniform constant grows like b S
  (row 1011 Proposition B', PROVED for all strength profiles; ARGUED for homogeneous strengths, check 1014).
- SU(2), frame moves V = theta n on typical fields: the direct term carries a mass-like part >= (b/6) theta^2 NA
  with NA of order 1/b per site (Lemma FR, FR+; row 1141 (8), checked by row 1142). So frame moves give a LARGER
  upper bound on non-abelian fields than on abelian ones: the wrong sign for (DEC).
- SU(2), typical pins at small coupling: delta H < 0 by the one-loop law (paramagnetic part 4 against diamagnetic
  part 1/3 of the coefficient 11/3; RECALLED, row 1011 7.4 (N3)). The account controls this regime g_k <= gamma
  (row 1018 L353), above the band.

**2.2 Which exact identities could fix the sign at order-one coupling.** I list every exact identity of the Wilson
measure on file and its reach (each line cites the row that tested it).

- Gauge Ward identities: X(G) = 0 for every gauge generator G (row 1018 Lemma PROJ (ii)-(iii)). They move no
  gauge-invariant observable. With a frame they give PROJ (iii), whose defect term is the frame cost above.
- Link symmetries: only central ones (row 1011 Lemma CEN, Corollary CEN2, for every gauge group; CEN+ row 1016).
  Their identities are those of Z_2 and read the flux half (row 1018 Lemma PAR, Corollary MP = Mack and Petkova's
  criterion); Lemma PT binds them for the neutral half.
- Lattice symmetries: the hypercubic group is non-abelian but finite; it has no continuous twist and no stiffness
  (row 1201, ARGUED).
- Integration by parts on the interior (Schwinger-Dyson, master loop equations): exact at every coupling and they
  carry the non-abelian splitting terms, but they fix no sign without a small parameter; their published uses are
  strong coupling and large N (row 1238 Step 1.2 table; row 1199 table).
- Reflection positivity: Schwarz and convexity inequalities in the twist and time directions; every inequality of
  that family holds for the free photon (row 1217, Lemma E), so it is blind.

**2.3 Verdict (ARGUED).** No identity on file fixes the sign of delta H for typical pins at order-one coupling.
Frame moves give the wrong sign (2.1, third item), and the identities of 2.2 either do not move gauge-invariant
observables, read only the centre, are finite, or need a small parameter. The negative sign at the band is the
continuation of one-loop asymptotic freedom into the region where the account's control ends. So the sign is a
dynamical fact of the Wilson measure there, not a consequence of a known identity. A proof of (N-phys) by a (K-flow)
step therefore needs a NEW exact identity, or a new non-frame extension V whose direct term is provably below the
abelian value on typical SU(2) fields. Route (ii) of row 1018 (field-dependent moves, aligned frames of row 1026) is
the only open candidate of the second kind on file; its frames found so far cost order one per site (row 1026,
ARGUED). I did not find a candidate of the first kind.

**What this step does not show.** It is not a theorem that no such identity exists. It is a reading of the identities
on file. No new PROVED statement is in this step except the elementary Gaussian line of 2.1.
