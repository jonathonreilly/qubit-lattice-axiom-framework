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

- 13:50Z Section 2 written ((Q1) cited, (Q2) answered: Lemma 2.1, Proposition 2.2, Corollary 2.3).

## 2. (Q1) and (Q2): what a boundary layer can do to the published slab consumer

Credit for every statement of the source in this section: Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and
Singha Roy (A below), Section 11 and Appendix G, as read and checked line by line in row 1224 (Sections 3.1-3.3 of
`gap-mini-solve-q-fable.md`) and in check 1239 (`gap-slabm-check-astra.md`). I did not re-read A's PDF in this row.

**2.1 (Q1) is on file; not re-derived.** A gauge transformation supported on the non-interior vertices of a box
changes only the plaquettes that contain a fixed exterior link at a vertex where it jumps; every other plaquette,
the bulk included, is invariant. This is Lemma TWIST of row 1013 (4.2) and Lemma REM of row 1016 ("colour twists of
pins are removable unless a pinned path carries them"); check 1239 uses the same construction for its twist h_t. So the
bulk sees the boundary layer only through gauge-invariant data, and the frame of the layer is seen only by the
plaquettes that touch the exterior. I cite these and add nothing.

**2.2 Setting of the consumer (READ, row 1224 3.2).** A's Proposition 11.7 bounds the Friedrichs angle of two
resampling projections. For x, y in the gauge-invariant space A, orthogonal to the common kernel, it fixes the links
e outside V(Q_t) (value eta) and uses the slices X_eta = x(., eta), Y_eta = y(., eta). They are functions of the two
outer parts Q_t^+, Q_t^-, invariant under the interior gauge group G_(Q_t). The hypothesis (M) is applied at the fibre
exterior omega' = (eta, omega) for EVERY eta, then integrated (Cauchy-Schwarz in eta). Theorem 11.8 and Definition
G.3 keep the quantifier "every exterior". So the consumer needs (M) only for the class

  S(Q_t, omega') = { normalized slices of gauge-invariant functions at the fibre omega' },

a subclass of A's class (all G_Q-invariant functions). The question (Q2) is whether boundary-layer order is visible
to S. Two facts answer it.

**Lemma 2.1 (central fibres are frame-blind; PROVED, elementary).** If every link of eta is central (in {+1, -1}),
then every slice X_eta of a gauge-invariant x is invariant under the global conjugation sigma -> g sigma g^(-1) of the
free links, g in SU(2).

Proof. The constant gauge transformation g on the whole torus maps (sigma, eta) to (g sigma g^(-1), g eta g^(-1)) =
(g sigma g^(-1), eta), since eta is central. x is invariant under it. QED

So at exactly central exteriors (the case of row 1224's Lemma NC and of its GUIDE runs) the consumer's tests cannot
read the orientation of an ordered face: the staggered vector M_+- of row 1224 7.2 is not in S, only rotation-
invariant functions of it are. The violation of (M) found there (for G_Q-invariant components of M_+-) is a violation
of A's hypothesis as stated, not yet of what A's proof uses.

**Proposition 2.2 (near-central fibres see the frame; PROVED, elementary).** Let eta_0 be central-valued. Use
coordinates with the split axis 0 and lower box corner 1 = (1,1,1,1). Let f_- = U_2(v) with v in Q_t^-, f_+ = U_2(w)
with w in Q_t^+ be free links in direction 2 on the hinge H = {x_1 = x_3 = 1} (in four dimensions the set where two
coordinates sit at their lower bound is two-dimensional; H runs through Q_t^-, Q_t^0, Q_t^+ in direction 0). Each end
point of f_+- lies on H, so it carries two incoming exterior links, in directions 1 and 3. [Corrected 2026-11-20 in the
same session: the first text said "U_0 along an edge"; links in direction 0 on H also qualify, but in the pi-flux
exterior of row 1224 they are pinned to the identity by two plaquettes and carry no frame, while for links in
direction 2 on H the two pinning plaquettes at x_1 = 0 and x_3 = 0 pull to +1 and -1 and cancel exactly, so these
links carry the face orientation J of Lemma NC's ground states.] For A, B in su(2) put q_(A,B)(f) = <A, Ad_f B>
(Killing form; Ad_f in SO(3)). Then

  sup over fibres omega' near (eta_0, omega) and over X in S(Q_t^-), Y in S(Q_t^+) of corr(X, Y)
     >= rho_fr := sup_(A,B) corr_(nu_0)( q_(A,B)(f_-), q_(A,B)(f_+) ),

where nu_0 is the conditional law at the central fibre. Hence, if rho_fr > c for one admissible box, one central
exterior and one pair of edge links, then (M_(d,m)(c)) fails already in the consumer's own class S, and Theorem 11.8
cannot be applied with that c.

Proof. Let v' = v + e_2. Both v and v' lie on H, so each has the two incoming exterior links in directions 1 and 3;
let C, C' be the exterior (1,3)-plaquettes with corner v, resp. v' (vertices v, v - e_1, v - e_1 - e_3, v - e_3;
all four links have base point with x_1 = 0 or x_3 = 0, so all are exterior). They are closed loops of exterior links
through v, resp. v'. The loop v -> v' (along f_-), around C' at v', back along f_-^(-1), around C at v,
is closed, so x = Re tr( f_- Hol(C') f_-^(-1) Hol(C) ) is a gauge-invariant function on the torus; build y the same way
at f_+ with exterior plaquettes D, D'. Change one exterior link in each of C, C', D, D' so that the holonomies become
Hol(C) = z e^(eps A), Hol(C') = z' e^(eps B), and the same with A, B at D, D' (z, z' central). Call this fibre
eta_eps; eta_eps -> eta_0 as eps -> 0. Then

  x(., eta_eps) = z z' Re tr( e^(eps Ad_f B) e^(eps A) ) = z z' [ 2 - (eps^2/2) |Ad_f B + A|^2 ] + O(eps^3)

with the normalization Re tr e^X = 2 - |X|^2/2 + O(|X|^4) for X in su(2), |X|^2 = -(1/2)... (any fixed positive
multiple of the Killing form; only the f-dependent cross term matters). The f-dependent part at order eps^2 is
-z z' eps^2 <A, Ad_(f_-) B> (cross term of the square), and the remainder is O(eps^3) uniformly in f because SU(2)
is compact. The conditional density depends continuously on the exterior and is bounded above and below at fixed
box (row 1224 3.2, Lemma 11.6), so nu_(eta_eps) -> nu_0 in total variation. Since nu_0 has full support,
Var_(nu_0) q_(A,B)(f_-) > 0 for A, B nonzero. Centre and normalize the two slices; the order eps^2 factors and the sign
z z' cancel in the correlation, and

  lim_(eps -> 0) corr_(nu_(eta_eps)) ( x(., eta_eps), y(., eta_eps) ) = corr_(nu_0) ( q_(A,B)(f_-), q_(A,B)(f_+) ).

Take the supremum over A, B. QED

**Corollary 2.2' (the angle in A's proof itself, not only its hypothesis; PROVED, elementary).** Under the hypotheses
of Proposition 2.2, the Friedrichs angle that A's Proposition 11.7 must bound by c (between the ranges of the two
adjacent resampling projections, modulo their common kernel, in L^2 of the measure on which 11.7 is applied) has
cosine at least rho_fr. Proof. The fibre law depends continuously on the fibre, so the slice correlation stays above
rho_fr - delta on a neighbourhood B of the fibre eta_eps; take B gauge-invariant (cut out by exterior holonomies, which
determine the fibre up to gauge) and of positive measure (the Wilson density has full support). Put x' = 1_B(e) (x -
E[x | e]) and y' = 1_B(e) (y - E[y | e]). Both are gauge-invariant (A's Lemma 11.1), lie in the two ranges, are
orthogonal to the common kernel, and <x', y'> / (norm x' norm y') is a weighted average of fibre correlations over B,
hence at least rho_fr - delta. QED. So under (FO) the alternating-projection step of Theorem 11.8 fails at that d as a
method (Lemma 11.5 needs the adjacent cosine below 1/2), whatever the patch gap itself is (check 1239's two-sign
example shows a gap can coexist with a large angle).

**Corollary 2.3 (what decides the published route; PROVED given the definitions).** Call (FO) at (beta, d, m) the
statement: for some admissible box (widths in [2d - 1, md - 1], split axis 3d - 1 = d + (d - 1) + d), some
central-valued exterior and some pair of direction-2 links f_+- on the hinge H, rho_fr > 1/2. Then:

- (FO) at (beta_k, d) for every d in [2, (l/a_k + 1)/2] and infinitely many k excludes every choice (c, m, l, d_k) in
  A's Theorem D along that tuning, through the consumer's own test class (Proposition 2.2 and check 1239's
  quantifier analysis, "for each eligible c, m, l there must be arbitrarily fine cutoffs at which every allowed d
  fails").
- If (FO) fails at all large d along the tuning, Proposition 2.2 says nothing; (M) can still fail for other reasons.

So A's route and the boundary obstruction meet exactly at (FO), the orientation order of the frames of an edge, read at
a central exterior. Row 1224's GUIDE (r up to 0.91 at beta 3-6, d 3-6; r_bar 0.69 at beta 2.8, d 8) measured the
corresponding face quantity; the edge version is the one the consumer sees.

**2.4 What is open, and why (ARGUED).** (FO) uniformly in d at large beta is a statement of continuous-symmetry
breaking in a three-dimensional boundary layer: by 2.1 the only terms that see the frames are the pinning plaquettes
(strength beta, frustrated by the pi-flux pattern), and the bulk sees the layer only through face holonomies. The
standard proof of continuous-symmetry breaking in three dimensions (Frohlich-Simon-Spencer infrared bounds) needs
reflection positivity with a torus structure in the layer directions. A's boxes never wrap (widths at most md - 1 < L),
and a box with a fixed exterior admits only one reflection per direction, so neither the chessboard estimate nor
Gaussian domination is available. I know no other tool. So (FO) stays OPEN, and with it A's open question of p. 105.
The fixed-d limit beta -> infinity (Laplace method around the minimizers of Lemma NC) would give (FO) at fixed d only;
check 1239 explains why that does not touch the tuning.

Status: Lemma 2.1 and Proposition 2.2 PROVED (elementary; checked by no one). Corollary 2.3 PROVED given A's
definitions as read in rows 1224 and 1239. (FO) OPEN.
