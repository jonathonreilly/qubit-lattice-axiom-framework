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
  (Lemma FR, row 1011 7.3, PROVED). The size of NA on typical fields is ARGUED there, not proved (row 1011 7.3:
  "NA is of order (number of sites)/b"). If that size is right, the frame's cost is mass-like at link level at every
  coupling, and a frame exists only at block scales where the non-abelian part of the block field is small, above
  the band ((N1)-(N3) of row 1011 7.4). Then this repair does not cross the band.
- Every other engine kind on file (positivity, curvature, dilute defect gas, large N or exact recursion,
  compactness, Hellmann-Feynman level derivatives) has a named failing step (row 1237 Step 1.2; row 1238 Step 1.2).

**1.3 Decision.** I found no engine of a new kind, and I do not claim an attack on the seed itself. The step of
1.2 that is still ARGUED on file, and on which the verdict "the typical-field repair stops above the band" rests,
is the size of the frame cost NA on typical Wilson fields. The session proves it (Step 2).

Moves: the kill of route G2 of row 1011's registry (typical pins with a colour frame, "blocked-local") at link
level becomes PROVED instead of ARGUED. If the lower bound holds with explicit constants at every beta, no
link-level frame removes the mass-like term anywhere on the trajectory, so a frame must live at a block scale; any
future (K-flow) row has to supply a block frame with its own defect bound. If the bound failed (typical fields
with small NA at large beta), the typical-field repair would reopen at link level, which changes the lane's map.

Rule 0a for this statement: grep for "NA(omega)", "non-abelian part", "Lemma FR", "frame defect" in
`library/open-core.md` and the FINISH rows (09:24Z): open-core.md has no match; FINISH matches are rows 1011 and
1014-1016 (the source and its checks; row 1014: "FR's gloss of NA = 0" is a minor defect, not a proof of the size).
No row attacks the size of NA.
