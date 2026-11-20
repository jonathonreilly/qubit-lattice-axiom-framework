lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:18Z

# gap-mini-solve-an-opus: four-dimensional SU(2) Yang-Mills mass gap (row 1277)

Queue row 1277 of `FINISH.md` (line 1358), plain brief: prove that four-dimensional SU(2) Yang-Mills theory has a mass
gap in the sense of Jaffe and Witten. Run by Claude Opus 5.5 at max effort on the Mac mini worker 1, from branch
`claude/ym4d-hard-route` at commit 135dd9026. Started 2026-11-20T13:18Z (date -u).

Labels: PROVED (a written argument, checkable by hand), ARGUED (a sketch with a named gap), GUIDE (a numeric run or
heuristic; never a proof step), OPEN.

## 0. Status log

- 13:18Z file created; reading the brief, GOAL.md, the newest RESULT lines and row 1218's reading.
- 13:20Z read: FINISH top rules, GOAL.md, `parts/gap.md` state of attack, row 1218 reading header, RESULT lines of rows
  1241-1275, branch tip 4a5d911 (siblings in flight: rows 1278 ao, 1280 ap, 1281 laptop-solve3, 1283 solve32, 1284 aq).
  Candidate under reading: the open question left UNDECIDED by check 1239 of row 1224 (does the slab hypothesis (M) of
  Bhattacharjee et al. fail along the 4D Wilson tuning?).
- 13:42Z selection finished (about 60 minutes of reading; recorded in Section 1). Blind-site expansions (the carry's one
  unowned item) is blocked: Balaban CMP 116 is not in the papers folder, Project Euclid and Deep Blue both answer with a
  bot check (stopped there, per the rules).

## 1. How best to attack it (ARGUED; a reading of the record, not a proof)

**1.1 Where the problem stands in this lane (READ, with sources).** The reduction of the Jaffe-Witten gap clause to one
infrared input is written and checked: (N-phys) alone gives a cutoff-uniform gap on the centre-blind sector and, with
the continuum datum, the gap clause (row 1179 Theorem BP, check row 1183); (N-phys) holds iff every fine coupling has a
finite one-cube seed size with limsup a_j nu(beta_j) finite (row 1180). At ONE fine coupling, the Dobrushin-Shlosman
weak-mixing hypothesis (W) at some finite (R, delta) already gives the seed and the one-cutoff datum (row 1258, Lemma WS,
check row 1265), and the one-cutoff carry transports it (rows 1233-1275; open there: the account's
`9.1:prop-blind-site-expansions`, (FC-T), (DET)'s inputs). So the infrared core, in its sharpest form on file, is:

> (SL-1) at one fine coupling beta_0 in the carry's range, the four-dimensional SU(2) Wilson measure has weak mixing
> (exponential decay of the boundary influence on gauge-invariant interior observables) at SOME finite scale R, with
> explicit constants.

No size condition on R is needed. (SL-1) is the infinite-volume lattice mass gap at one weak coupling. No rigorous
method reaches it today: strong-coupling expansions and Bakry-Emery curvature stop near beta_W = 0.36 (Bhattacharjee et
al., Theorems A, 9.5, 9.14, read in row 1218); every engine on file is blind (`parts/gap.md`, "The exact price"); the
two fixed-coupling mechanisms known for asymptotically free models are two-dimensional (Ding-Huang-Yang's loop-soup
third copy; OpenAI's pinned-cell bracket gain), and their 4D gauge analogues are missing (row 1007 A(5), B(5); rows
1011, 1016, 1139).

**1.2 What a session can still decide.** A proof of (SL-1) needs a new selective mechanism; I have none that is not on
file (I checked my candidates against the inventories: Migdal-Kadanoff and Tomboulis (group-blind, row 878, 998 I34-I35),
twisted thin torus (row 842, S1), 2D O(N) ports (rows 1007-1016), diamagnetic/paramagnetic comparisons (rows 1139, 1194,
1199, 1244), vortex doubling maps (row 1269 Lemma D), instantons and self-duality (46 and 35 files)). So I spend the
session on the one place where a definite answer is in reach and where the answer changes how the lane reads a published
consumer of the same crux:

**Chosen item.** The slab hypothesis (M_(d,m)(c)) of Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and
Singha Roy ("The Yang-Mills Mass Gap from One Bound at One Scale", their Section 11 and Theorem D) is the published
one-scale input closest to (SL-1). Row 1224 found an exterior that orders a boundary face (Lemma NC, classical) and
check 1239 left its persistence along the tuning UNDECIDED. Their open question (p. 105) is whether any boundary
condition refutes (M) along the 4D tuning. Two definite questions follow, and I attack them in this order:

- (Q1) Structure: which part of the conditional law can an exterior order at all? I aim to PROVE an exact
  decoupling: the bulk of the box sees the boundary layer only through gauge-invariant face holonomies, and the only
  terms that see the face's frame are the plaquettes that touch the fixed exterior. This turns "face order" into a
  statement about a three-dimensional gauge-Higgs-type layer, and it is what any proof or disproof of persistence
  must use.
- (Q2) Consumer: does Theorem D need (M) for every exterior, including such layers, or does a version that excludes a
  collar near the exterior (the form of (SL-1) and of Lemma WS) feed the same Knabe-type step? If yes, the boundary
  obstruction is irrelevant to the crux and the published route and the lane's route ask for the same infrared fact.
  If no, the published route carries an extra, possibly false, hypothesis.

Stop rule: if (Q1) and (Q2) close or fail, I record it and return to (SL-1) with whatever (Q1) gives.
