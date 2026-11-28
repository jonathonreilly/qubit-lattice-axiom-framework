lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T00:50Z

# gap-constraints-max: the constraints of the seed system, and ideas that relax them (row 962)

Brainstorm item with a hard filter. Author: Claude Fable 5.2 (max), Mac mini worker 1, pinned at commit aa7b2e875.
Not checked by another model. Research-stage working state; no status is granted here.

Labels used: PROVED (full argument written here or cited to a checked note), CONDITIONAL, GUIDE (numerics, refute or
guide only), ARGUED (reasoning, not a proof), OPEN. Each idea is also marked NEW INPUT or REFRAMING.

Credit: the account of the lattice theory and its tori is Sussman and Alpoge's (with Claude and Codex as authors of
their text); the seed chain is this lane's (rows 700-961). Each section names what it takes from where.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Read the frame: row 962's inputs (rows 960, 961, 957, 947, 949, 954, 931, 913, 904, 706; Theorem SH in
   `library/gap-seed-shape.md` 1.4-1.5; the latest status note). Write the system as it stands (Section 1).
2. Constraint audit: each constraint of the system, FORCED (by the account, by the finish line, or by mathematics)
   or CHOICE, with the line that forces it (Section 2).
3. Repo search for each idea family before calling anything new (Section 3).
4. Ideas, group A: geometry, boundary conditions, time direction, anisotropy, several transfer directions (Section 4).
5. Ideas, group B: twists, sectors, gauge group, beta together with geometry, placement in the RG, others (Section 5).
6. Fact tests for every surviving idea: U(1), frozen Q_8 / 2T, K7, SMALL-BOX, the ceilings (Section 6).
7. First step of the best one or two ideas, attempted as a theorem; a GUIDE run only if it can refute (Section 7).
8. Ranked list of at most five ideas, each with first step and fact test; RESULT line (Section 8).

## Status log

- 2026-11-14T12:52Z: file created with the plan. Nothing proved yet.
- 2026-11-14T13:05Z: Step 1 done (Section 1). Next: Step 2, the constraint audit, with greps for each idea family (Step 3 merged into it).
- 2026-11-14T13:08Z: Steps 2 and 3 done (Sections 2, 3). Next: Steps 4-6, the ideas with their fact tests.
- 2026-11-14T13:11Z: Steps 4-6 done (Sections 4, 5, 6); audit row 15 corrected. Next: Step 7, Theorem 2O and Section 7.4.
- 2026-11-14T13:15Z: Step 7 done (Section 7: Theorem 2O proved by hand, Lemma SHIFT, projected doubling, GUIDE kill test with no violation). A2 and B2 texts corrected. Next: Step 8, ranked list and RESULT.
- 2026-11-14T13:16Z: Step 8 done (Section 8, RESULT). Item finished. The RESULT line is the last line of the file.

## 1. The system as it stands (READ at aa7b2e875; nothing here is new)

Sources read for this section: FINISH rows 947, 954, 957, 960-962 (lines 1024, 1031, 1034, 1037-1039), RESULT parts of
rows 706, 904, 913, 916, 924; `gap-crux-restate.md` L168-228 (Lemmas K, X, E, E', Theorem S, Corollary S3');
`gap-seed-shape.md` L45-136 (Theorem SH, thresholds); `gap-finishline-opus.md` L96-171 ((SEED-FP), the chain, 2.3-2.6);
`gap-status-1113.md` L23-57, L298-357; `gap-direction-max.md` L38-170, L400-458 (fact tests, 19 forms, F1-F4);
`gap-next3-max.md` L258-390 (the inventory of about 110 scored ideas, candidates C1-C16).
Row 960's output `gap-vargeom-opus.md` and check 959 are not on disk at this commit.

**1.1 The engine (PROVED, checked rows 698, 699, 707; group-blind).** Abstract class: a positive function
W(a, b) of two integer sides, with a positive trace-class operator T_b such that W(a, b) = Tr T_b^a, and
W(a, b) = W(b, a). For Wilson SU(2): W = Z(a, b, c, d) on the periodic torus with c, d fixed; the symmetry is the
lattice symmetry that exchanges two axes. With e(b) = log lambda_0(T_b), ell = inf log W/(ab), kappa(b) = e(b) - ell b,
g(a, b) = log W - a e(b) = log(1 + S(a; b)):
- Lemma K: kappa is non-negative, convex and non-increasing.
- Lemma X (crossing): a kappa(b) + g(a, b) = b kappa(a) + g(b, a); hence (b - a) kappa(b) <= g(a, b) for a < b.
- Lemma E': 1 + S(a; h) <= (1 + S(a; b))^(h/(b - a)) for h >= b > a.
- Theorem S / SH: one seed S(a; B) below a threshold t(shape) gives a gap on every larger cube; t = 1/1650 at
  ratio 2, 1/25 at 4, 1/10 at 6, 3/10 at ratio >= 24, tending to 1; the ceiling is 1 at every shape (two phases).
The proof uses three things only: (TM) in each direction, the exchange of two axes, a simple top eigenvalue.

**1.2 The finish line.** (SEED-FP): one physical size ell and one margin s_* < 1/5041 such that the thermal sum of the
BARE Wilson transfer operator on the periodic cube of physical side ell, at physical time ell/2, is at most s_* for
every first-passage datum (K, beta in W_K(g)), K >= K_0. Chain (a)-(f) of row 837, with links (c), (e) of row 916: it
gives (GAP) on the tr F^2 sector of every volume-first limit of the account's periodic tori. The integral of the
account's density rho_k is Z at every level k, so the seed is one number, the same at every level of the flow.

**1.3 The crux.** By Lemma SPLIT (row 892, check 893) the SH seed on the slab (a; (24a)^3) holds if the glue half
S_ev <= 1/10 and the flux half Q_0 <= 1/20. Row 931: the weakest form passing all fact tests is this split seed; the
glue half is a count (entropy level), the flux half a variance. Row 947: the smallest unproved inequality is
(LSI-J-seed)_a, a log-Sobolev constant alpha_J >= 2 beta K_a for the two-slice vacuum law on (24a)^3, a >= 30; row 954:
it needs m_G >= K_a. Row 957: the Piazza-Shen adaptation does not close it. Model arena of all of this: the unit
lattice at one bare beta_W in 2.3-2.6 (shared assumption SA1 of row 899); the real object is first passage.

**1.4 Fact tests (necessary conditions on any form).** FT-U1: false for the free photon and compact U(1) Coulomb
(glue: log(1 + S_ev) > 31 on the seed slab; flux: p -> 1/2). FT-FROZEN: false for frozen Q_8, 2T (S_ev >= 1/2;
p = 10/23, 30/61). K7: the mixed-action endpoint with no seed at any size (row 708, Proposition V). SMALL-BOX: a fixed
small box at large beta has no gap in units of its side, so a small-slice statement must carry a beta-dependent size.
FT-CEIL: worst-case single-link 1/3, single-site Dobrushin 2/3, vertex blocks 0.775, background-uniform layer bounds
false above 4 G_3 = 1.0109, environment-uniform parity bounds false, literal (AN1) is the worst case, clustering cannot
give the flux half.

**1.5 One reading used below (ARGUED from 1.1-1.2, arithmetic GUIDE).** In the dilute regime the SH seed on the slab
is a bound on the thermal pressure: log(1 + S(a; b^3)) = b^3 p(1/a) a. At ratio 24 the free value (three photons)
is 3 x 0.2193 x 24^3, about 9.1e3, and the seed asks 0.26: a pressure 35,000 times below Stefan-Boltzmann at a
temperature near 0.4 T_c. With one scalar of mass m the count is 878 (m a)^(3/2), so m a is about 12 (row 706 has
the same range). Every relaxation below is judged by whether it changes THIS number or only its representation.

## 2. The constraint audit (Step 2)

Verdicts: FORCED-A (by the Sussman-Alpoge account as written), FORCED-F (by the finish line (SEED-FP) or its proof
chain), FORCED-M (by mathematics: a theorem or a checked ceiling), CHOICE. Many rows are forced at one place and free
at another; the table says where. Row 858's partial file (`gap-crux-exercise-r858-max.md` 4.A-4.C, mined by row 900)
already holds an assumption table for the action (A1-A4) and the twists (C1-C4); I cite it where it decides a row and
do not repeat its arguments. Rows 14-19 are constraints that row 962 does not list and the system uses.

| # | Constraint | Verdict | What forces it, or what the freedom is | Cost of changing it |
|---|---|---|---|---|
| 1 | Periodic tori of the account's family (four equal sides 2 L^m, untwisted) | FORCED-A at the end of the chain; FORCED-F (proof) in the two exchanged directions; CHOICE elsewhere | (GAP) is a statement on the limits of the account's periodic tori (row 837 (c); row 916 Lemma C). The engine needs a trace in both channels of an exchanged pair (1.1). Equal sides are not needed (Theorem SH, any box; S3', any integer side). Spectator directions need (TM) only | Another box family needs a new node: its limit state is the account's state (OPEN for free walls, row 907) |
| 2 | Isotropic action (equal time and space couplings) | FORCED-A for the measure of the finish line; CHOICE for the engine | The crossing step uses the exchange of two axes (row 858 A2: "needed by the method"). Section 7 (Theorem 2O) removes the exchange at the price of one seed per orientation | An anisotropic account does not exist; an anisotropic seed has no route to (SEED-FP) |
| 3 | One box shape for all times | FORCED-M for the trace form | Tr T_B^a needs one operator on one space. Maps between boxes are row 960's subject (running; not attacked here) | row 960 |
| 4 | One time direction | CHOICE in the attack; not a constraint of the engine | The engine uses transfer operators in all four directions. The seed number has two readings: thermal count in one channel, Casimir deficit b kappa(a) in the crossed channel (Lemma X) | none; a reading |
| 5 | State space L^2 of one spatial slice | FORCED-M for a Markov transfer operator of the Wilson measure; the representation is a CHOICE | Other spaces (two-slice law J, T^2 after a time decimation, the OS space of a block field) carry the same Z. The number does not change (1.2) | none; a reading |
| 6 | Slab (a; (24a)^3), thresholds of Theorem SH | CHOICE inside the table of 1.5; FORCED-M at its edges | Edges: threshold below 1 at every shape (two phases, `gap-seed-shape.md` 4.1); q a < min b_i; SMALL-BOX. Between t(r) and 1 the engine is OPEN. Leverage is small: for the log-Sobolev form the cube r = 2 changes the needed exponent by 3 log 12 - log 495 = 1.25 only (my arithmetic: volume 8 a^3 against 13824 a^3, threshold 1/1650 against 3/10) | none |
| 7 | Split into glue and flux halves | CHOICE (Lemma SPLIT is one sufficient split) | The flux half exists because of rows 1 and 10: a torus and a finite centre (SA4 of row 899). Row 931 F2: no weaker sufficient form is on the table | a consumer without flux sectors (free walls: stops at (JOIN-TH)) or with a vacuum multiplet (row 876 G11) |
| 8 | One coupling, beta_W in 2.3-2.6 | The finish line is FORCED-F to cover every first-passage datum, K >= K_0. The band is a CHOICE of model arena (SA1) | The band is on the chain only through (ONE-K) + (UNIV-K) (rows 916, 924; OPEN) or (EXIT) (rows 846-877; OPEN) | (UNIV-K) or (EXIT) |
| 9 | Wilson weight | FORCED-A; not forced by the engine or the target | Row 858 A1; row 904: the account's universality covers a fixed ball of analytic irrelevant profiles at one horizon, for normalized regular laws on one volume | re-run the account for another weight |
| 10 | SU(2), centre Z_2, centre-flip sectors | FORCED-A and by GOAL.md (SU(2) first) | The sectors follow from rows 1 and 10 together | outside the target |
| 11 | Periodic, not twisted, open or Dirichlet | as row 1 | Twisted tori: engine available ((TM-tw)), outside the account (row 837 2.4 item 4). Free space walls: no centre sector (FW1, check 902), doubling needs a new input at every scale (row 910) | as row 1 |
| 12 | Fact tests | FORCED-M as necessary conditions; the list of rivals is a CHOICE | A relaxation can change the tests in one way only: by removing a rival from the class (free walls remove the periodic Q_8/2T test; a glue-only consumer keeps U(1) and K7) | none |
| 13 | No computer-assisted proof | FORCED by the owner (GOAL.md) | Not binding today (ARGUED): the seed box holds more than 3 x 10^5 links at ratio 2 and 5 x 10^8 at ratio 24 at beta 2.3, far beyond any enclosure method | none |
| 14 | The seed is a trace (a ratio of partition functions), not a matrix element or a correlation | FORCED-F (proof) | Only traces cross: W(a, b) = Tr T_b^a = Tr T'_a^b. Vector seeds exist on free walls and give a gap on a cyclic subspace only (row 898 6.2) | boundary-uniform mixing (FT-CEIL) or correlation inequalities (none for SU(2)) |
| 15 | Integer multiplicities and a simple top eigenvalue | FORCED-F (proof) | Lemma E is Tr X^(2b) <= (Tr X^b)^2. A projected trace is an average over N sheared operators in the crossed channel; the doubling then reads the other sectors at second order and the crossing identity gains an entropy term between -log N and 0 (Section 7.4) | none known |
| 16 | The vacuum is subtracted exactly (lambda_0^a) | FORCED-M | The energies are extensive; a comparison operator must reproduce lambda_0 to relative accuracy 1/(a |B|) (row 934's (VAC-SUB) is this) | the Doob chain and (LSI-J) are the exact subtraction |
| 17 | One physical size and one margin for all large cutoffs | FORCED-F | Row 837 2.4 item 1 | none |
| 18 | Time shorter than the sides | FORCED-F (proof) | Lemma X gives (b - a) kappa(b) <= g(a, b) only for a < b | none; at a = b the lemma is empty |
| 19 | Hypercubic lattice | FORCED-A | the account | outside the target |

**Reading of the table.** Three constraints are forced by the account and cannot be changed without a new account: the
measure (rows 2, 9, 10, 19 and the first-passage family of row 8) and the periodic limit state (row 1). Five are forced
by the present proof of the engine and by nothing else: trace, exchange symmetry, integer multiplicity, a < b, simple
top (rows 14, 15, 18, and row 2 for the engine). The rest are choices of representation that do not change the
number of 1.5 (rows 4, 5, 6, 7). So a relaxation can help in two ways only: (i) a new engine, whose seed is a
different statement about the same measure; (ii) a new node from another measure to the account's. The ideas below
are sorted by this.

## 3. Repo search (Step 3; greps at aa7b2e875 over `library/gap-*.md`, `library/prior/gap-*.md`, FINISH.md, `library/open-core.md`)

`library/open-core.md` has 0 hits for every pattern below; no FINISH row owns any of them as a target, except row 960.
Counts are files in the gap lane that mention the pattern; "as idea" means it was scored and not given a proof lane.

| Idea family | Hits | Status in the lane |
|---|---|---|
| anisotropic couplings, beta_s = 0 line, Hamiltonian limit | 41 files | KNOWN as idea 32 of row 859 (`gap-brainstorm-max.md` L317: "With beta_s = 0 ... solved at every beta_t ... Continue in beta_s"); row 858 A2: the engine "is lost in its present form", cost "Theorem S for unequal axes", not written |
| engine without axis exchange | 2 files | only the cost line of row 858 A2; no statement, no proof. Section 7 is new to the lane |
| free walls, open boundaries | 64 files | KNOWN and attacked: rows 898, 903, 907, 910 ((W'-ENG), (JOIN-TH)); stopped |
| Dirichlet walls, Schrodinger functional | 11 files | KNOWN (`gap-phys-seed.md` L25 search list; row 903 chose Neumann walls) |
| twists, C-periodic gluing | 11 files | KNOWN (twist-eaters, row 876 idea 15; twisted thin torus rows 842, 862) |
| Klein-bottle or orientation-reversing gluing | 16 files | KNOWN as idea 24 of row 876 (`gap-brainstorm2-max.md` L174), for the flux; no identity written |
| shifted (skew, helical) tori, Tr(T^a tau_v) | 0 relevant (the 7 hits are "shear" maps of other notes) | NEW to the lane |
| momentum or symmetry projection of the trace | 13 files | used for observables and channels (`gap-channel-astra.md` L698), not as an engine |
| diagonal reflections | 5 files | only as "diagonal reflected correlators" of the limit step; no diagonal transfer operator |
| corner transfer matrices, wedge operators | 0 files | NEW to the lane |
| positively curved space (S^3 slices) | 0 as geometry (31 hits are SU(2) = S^3) | NEW as geometry; hyperbolic lattice is idea of row 859 |
| inhomogeneous couplings, strong-coupling walls | 2 files | random inhomogeneous couplings as idea 4 of row 859; no superlattice |
| time decimation, T -> T^2 | 32 files | KNOWN (decimation and soft block steps, rows 846-877) |
| sum over twists, SO(3) form, vacuum multiplet | (row 858 C3, row 876 G11, 35) | KNOWN as ideas; (MULTIPLET) never attacked |
| operator inequalities (Golden-Thompson, Araki-Lieb-Thirring) | 4 files | used once (row 913 Theorem ABS, Lowner-Heinz); stop at (VAC-SUB) |
| step scaling, small volume | 19 files | KNOWN (row 720; row 859); SMALL-BOX |
| Higgs handle | 41 files | KNOWN |

## 4. Ideas, group A: geometry, boundaries, time direction, anisotropy, several directions (Step 4)

Format: Buys / Relaxes (allowed?) / Fact tests / First theorem / Worth-doing / Mark. "KNOWN" refers to Section 3.
All chances are my judgement (ARGUED). No idea below supplies the order-one number of 1.5; I say so once here.

**A1. An engine without axis exchange (Theorem 2O, Section 7).**
- Buys: a seed-to-gap theorem for every model with positive transfer operators in two directions, with no symmetry
  between them. It is the consumer that A2, A3, B8 lack (row 858 A2 names it as the cost of anisotropy).
- Relaxes: row 2 of the audit, for the engine only. Allowed as mathematics; the account stays isotropic.
- Fact tests: the engine is group-blind. Its hypothesis is a pair of seeds, one per orientation; U(1) fails both
  (the photon in each channel), frozen groups fail both (degenerate flat vectors), SMALL-BOX binds both sides.
- First theorem: Theorem 2O in two-direction form, PROVED in 7.1-7.3 (threshold 1/1400 on the larger log-sum).
- Worth-doing: moves no item of the (SEED-FP) chain by itself. It moves the model arena: any anisotropic or
  time-decimated seed now has a consumer. NEW as a theorem; REFRAMING for the seed.

**A2. The solvable line beta_s = 0 as the start of a transport, at the target beta_t.** KNOWN as idea 32 of row 859.
- Buys: at beta_s = 0 the model is solved for every beta_t (independent link chains in time; in the crossed channel a
  3D Polyakov-loop spin model with link weight sum_j (c_j(beta_t)/c_0)^a chi_j chi_j). GUIDE arithmetic (mine): the
  lowest gauge-invariant excitation is one plaquette, rate 4 log(I_1/I_2)(beta_t), about 2.9 per step at beta_t = 2.3,
  against 1.22 at the isotropic point (row 706); the slab count 3 (24a)^3 e^(-2.94 a) is below 3/10 from a = 6.
  So the seed holds at the START of the path, at the same beta_t, on a box smaller than the target box.
- Relaxes: row 2 (needs A1 as engine) and row 8 (a path in beta_s, not in the common beta).
- Fact tests: compact U(1) is solved and confined on the same line (rate 4 log(I_0/I_1)); it must lose the seed on the
  path at its Coulomb transition, so a transport inequality along beta_s must fail there: the same automatic test as
  row 708's path. Frozen groups fail at the start (beta_t = infinity: all character coefficients equal, rate 0).
- First theorem: the exact solution on the line with its thermal sum (routine), and the evenness Z(beta_t, beta_s) =
  Z(beta_t, -beta_s) for even space sides (flip, on every time slice, the space links (x, i) with sum over j < i of
  x_j odd; every space plaquette then changes sign and no time plaquette does), so the first beta_s-derivative of
  every seed quantity vanishes at the start (PROVED by this change of variables; it acts alike in the vacuum and on the torus).
- Worth-doing: no. The transport step is the open (THERM-DI)/(VIR-log) inequality with the (VAC-SUB) stop (rows 905,
  913, 934); the path is new, the missing inequality is not. And an anisotropic seed has no route to (SEED-FP).
  REFRAMING (a new path for a known transport).

**A3. The Hamiltonian (time-continuum) form.** KNOWN (idea 32, 37 of row 859). With A1 it has an engine. Tools:
Schrodinger operator on a product of 3-spheres. No order-one method (row 957's GUIDE: the curvature absorber fails
at typical fields). Not on the chain. REFRAMING. Not worth a lane.

**A4. Sheared tori: the trace with a translation, Tr(T_B^a tau_v).** NEW to the lane (Section 3).
- Buys: momentum-resolved thermal sums as partition functions of tori Z^4/Lambda, Lambda generated by (a, v) and the
  box periods. Exact relabelling (Lemma SHIFT, 7.4): in two directions, with d = gcd(b, v), the torus (a, b; shift v)
  is the torus (d, ab/d; shift v'). So a unit shift turns the pair (a, b) into one helix: time 1 on a box of side ab.
- Relaxes: row 1 (the family of tori), inside the engine's class: each sheared torus has positive transfer operators.
- Fact tests: identities, group-blind. SMALL-BOX: the shortest loops of the sheared torus are unchanged (lengths b
  and about a), so a helix carries no large-box information.
- First theorem: Lemma SHIFT and the projected doubling inequality of 7.4 (PROVED).
- Worth-doing: weak. A zero-momentum seed would need m a of about 6 in place of 12 (the one-particle count goes, the
  two-particle count stays; GUIDE arithmetic). But 7.4 shows the projected engine reads the other momentum sectors at
  second order and needs the shear deficits, which only the full sum bounds. It changes a constant, not the crux.
  REFRAMING.

**A5. Orientation-reversing gluing (Klein bottle in a time-space plane).** KNOWN as idea 24 of row 876.
- Buys: K(a, b) := Tr(T_b^a R), R the reflection of one space direction, equals a matrix element
  <C| (T'_{2a})^(b/2) |C> of the crossed operator between two crosscap vectors that do not depend on b (ARGUED: cut
  the Klein bottle along the two fixed lines of R). So K is log-convex in b and has VECTOR form in one channel:
  only reflection-even states with zero momentum in that direction are counted.
- Fact tests: FAILS as a selective form. R reverses U(1) flux, so the U(1) flux tower of that direction drops out of
  the trace (row 876 idea 24), while the Z_2 flux of SU(2) stays: the gluing helps the rival. Photons stay.
- Worth-doing: no. REFRAMING.

**A6. Diagonal reflections and diagonal transfer operators.** NEW as an engine ingredient.
- Buys: the reflection x_1 <-> x_2 is a reflection-positive symmetry of the Wilson weight (ARGUED: a plaquette cut by
  the diagonal is (1/2) Re tr(A theta(A)^*) with A the product of its two links on one side, a sum of terms
  F theta(F-bar); the other plaquettes lie on one closed side). So tori periodic along (1,1) and (1,-1) have a positive
  transfer operator, and the torus of periods (b, b), (b, -b) is at once a diagonal box and the double of the square
  b x b. This could fill the empty case a = b of Lemma X (audit row 18).
- Fact tests: group-blind. Gain bounded by the ceiling 1 on thresholds (audit row 6).
- Worth-doing: no; thresholds are not the obstacle. REFRAMING.

**A7. Corner (wedge) transfer operators: two transfer directions at once.** NEW to the lane; dead.
A quadrant operator needs free walls in two directions ((JOIN-TH) again), and its spectrum is the entanglement
spectrum of a half-space, not the mass: in solvable 2D models its level spacing is of order 1/log(xi) (RECALLED, not
read). No seed can be read from it. Not worth a lane.

**A8. Free walls in some space directions only.** VARIANT of row 898 C1. Free walls in direction i make every twist
in a plane containing i a gauge transformation (FW1's argument, check 902), so the sector group shrinks from Z_2^3 to
Z_2^2 or Z_2. The engine cannot enlarge a free direction (row 910: doubling is not structural). Dead at (JOIN-TH).

**A9. A positively curved slice (S^3 in place of the 3-torus).** NEW as geometry; dead for three forced reasons.
No exchange of axes and no trace in the crossed channel (audit rows 14, 2); the small-radius gap 2/R is geometric
and is the same for Maxwell theory, so it fails FT-U1 as a mechanism and SMALL-BOX as a seed; no account.

**A10. A box whose shape varies in time.** Row 960 (running on worker 2). Named, not attacked (rule 0a).

## 5. Ideas, group B: twists, sectors, group, beta with geometry, place in the RG, others (Step 5)

**B1. Graded or projected seeds (momentum, cubic irreps, parity, centre).** The direct channel is fine (an invariant
subspace); the crossed channel is an average over sheared or twisted operators (7.4). For the centre grading this is
the lane's Theorem R and Proposition CL (the light group of four). For momentum it is A4. REFRAMING.

**B2. The twist-summed (SO(3)-type) torus as the engine's model.** KNOWN (row 858 C3; row 876 ideas 35, G11).
W_Sigma := (1/8) sum over the 64 twists of Z^tw is exchange-symmetric and is a trace of one positive operator, the
direct sum over the 8 magnetic classes of the even parts (ARGUED from `gap-flux-exercise.md` 3.0-3.1). Its seed is
FALSE in the confined phase: the 8 magnetic classes have top eigenvalues within exp(-area law) of each other, so its
thermal sum is at least 7 - o(1). So the choice "periodic, not twist-summed" is forced by the phase: the periodic
torus has heavy electric sectors, the summed torus has light magnetic ones. A summed engine needs the multiplet
consumer (MULTIPLET), which nobody attacked. Fact tests: frozen Q_8, 2T would PASS a summed seed at large beta
(magnetic classes heavy, even sector gapped), correctly: they are gapped on centre-blind functions. This is the
reading of row 876 (G4, G5, G11) and of Theorem R: the gap needs pattern purity (each flux weight near 0 or 1) and
the glue half. Purity is still a flux statement; U(1) fails it. Nothing new. REFRAMING of the flux half; the glue
half stays.

**B3. The place of the seed in the flow.** The number is level-free (1.2). Known placements: every cutoff (as
stated); one cutoff with (UNIV-K); after exact steps with (EXIT). A small physical box at first passage is perturbative
but fails the seed (SMALL-BOX; row 720 read van Baal's numbers). No new placement exists that is not one of these
(ARGUED: any exact step keeps Z). REFRAMING.

**B4. beta together with geometry.** (i) The cutoff step at fixed physical size is (UNIV-K) (rows 916, 924; OPEN).
(ii) A fixed lattice with beta falling from infinity is a transport from the weak side; its start has the free value
of 1.5 (9.1e3 against 0.26), so no smallness is transported, and a monotonicity of S in beta would point the wrong
way. Dead. (iii) A2 is the one path whose start is solved at the target beta_t.

**B5. Inhomogeneous couplings: a superlattice of strong-coupling walls.** Lemma WALL0 (PROVED, one line): if every
plaquette meeting a wall layer has coupling 0, the links of the layer are Haar-distributed and Z factorizes into
free-wall blocks. Turning the walls on is a block expansion that needs exterior-uniform control of a block larger
than the correlation length: FT-CEIL (W2, row 836). The averaged door (check 852) has no supplier. KNOWN family; dead
in its uniform form.

**B6. Operator comparison along the time step (Golden-Thompson, Araki-Lieb-Thirring).** For a weight whose time
kernel is a semigroup (heat kernel in time), refining the time step lowers the trace and the top eigenvalue together
(log-majorization, RECALLED). The seed is their ratio. Dead by audit row 16 ((VAC-SUB)).

**B7. Time decimation as the flow (T -> T^2).** KNOWN family. It keeps (TM) in every direction and the exchange of
space axes, and loses the time-space exchange; Theorem 2O is its engine. The seed says: the kernel of T^a/lambda_0^a
is within s of rank one in trace norm. REFRAMING.

**B8. The crux read in the crossed channel.** By Lemma X the count of the glue half is b kappa(a): the excess of the
ground energy of the slab operator of thickness a over a times the bulk rate. No count appears; one difference of
two top eigenvalues does. KNOWN as (CAS), (SEED-Delta) (row 931 form 18). A log-Sobolev form for the crossed slab
law is not a different statement: the trace of one channel is the vacuum of the other. REFRAMING.

**B9. Other groups.** SO(3) is B2. SU(N), N >= 3, and other lattices are outside the account (audit rows 10, 19).

## 6. Fact tests, all ideas in one table (Step 6)

Y = the form fails for the rival, as it must; N = the rival passes (the form is not selective); - = not applicable
(an identity or an engine, group-blind). SMALL = respects SMALL-BOX. CEIL = uses no statement a ceiling refutes.

| Idea | U(1) | Q_8, 2T | K7 | SMALL | CEIL | Mark | Verdict |
|---|---|---|---|---|---|---|---|
| A1 Theorem 2O | - (seeds: Y) | - (seeds: Y) | - | Y | Y | NEW theorem, REFRAMING | proved here; a tool |
| A2 beta_s = 0 path | Y on the path | Y at the start | not tested | Y | Y | REFRAMING (KNOWN path idea) | stops at (VAC-SUB) |
| A3 Hamiltonian form | Y | Y | - | Y | Y | REFRAMING | no tool |
| A4 sheared tori | - | - | - | Y | Y | NEW identities, REFRAMING | changes a constant |
| A5 Klein gluing | N (flux tower drops) | Y | - | Y | Y | REFRAMING | not selective |
| A6 diagonal reflections | - | - | - | Y | Y | REFRAMING | thresholds only |
| A7 corner operators | - | - | - | - | - | NEW, dead | wrong spectrum |
| A8 partial free walls | Y (seed) | removed in part | Y | Y | Y | VARIANT | (JOIN-TH) |
| A9 S^3 slices | N (2/R is Maxwell's too) | - | - | N | Y | NEW, dead | no engine |
| B1 projected seeds | - | - | - | Y | Y | REFRAMING | 7.4 |
| B2 twist-summed engine | Y | N by design (correct) | Y | Y | Y | REFRAMING (KNOWN) | needs (MULTIPLET) |
| B3 place in the flow | - | - | - | Y | Y | REFRAMING | none new |
| B4 beta with geometry | - | - | - | N for (ii) | Y | REFRAMING | (UNIV-K) or dead |
| B5 strong walls | Y | Y | Y | Y | N in uniform form | KNOWN family | ceilings |
| B6 operator comparison | - | - | - | - | - | dead | (VAC-SUB) |
| B7 time decimation | - | - | - | Y | Y | REFRAMING | none new |
| B8 crossed reading | Y | Y | Y | Y | Y | REFRAMING (KNOWN) | none new |

**Finding of Steps 4-6 (the answer to the row's main question).** No relaxation of the constraint system is a NEW
INPUT for the seed. Each one is of one of three kinds: (i) an engine change, which trades the seed for another
statement about the same measure at the same scale (A1, A4, A6, B1, B2); (ii) a change of measure with no node back to
the account (A2, A3, A8, A9, B5); (iii) a reading of the same number (A5, B3, B4, B6, B7, B8). The reason is in the
audit: the number of 1.5 is fixed by the measure and the scale, and the measure is forced by the account.

## 7. First step of A1 as a theorem: the engine without axis exchange (Step 7)

Status: PROVED here by hand; not checked by another model. A GUIDE run (7.5) tried to refute the lemmas and did not.
The proof follows the lane's Lemmas K, X, E (`gap-crux-restate.md` 3.4, rows 697-699) step by step; the one new
step is Lemma D, which replaces "kappa(a) >= kappa(b) for a < b" (the only use of the symmetry) by a second seed.

### 7.1 Setting (2O)

W(a, b) > 0 for integers a, b >= 3. For each b >= 3 a positive trace-class operator T_b, and for each a >= 3 a
positive trace-class operator T'_a, with

W(a, b) = Tr T_b^a = Tr (T'_a)^b for all a, b >= 3.

No symmetry W(a, b) = W(b, a) is assumed. Put e(b) = log lambda_0(T_b), e'(a) = log lambda_0(T'_a),
ell = inf over a, b of log W(a, b)/(ab) (assumed finite), kappa(b) = e(b) - ell b, kappa'(a) = e'(a) - ell a, and

g(a, b) = log W(a, b) - a e(b) = log(1 + S(a; b)) >= 0 (direct: time a, box b),
g'(b, a) = log W(a, b) - b e'(a) = log(1 + S'(b; a)) >= 0 (crossed: time b, box a).

Here S(a; b) = sum over the eigenvalues other than one copy of the top one of (lambda_i/lambda_0)^a, for T_b, and S'
is the same for T'_a. Use: W = Z of a torus in two directions whose couplings differ (others fixed), or any
partition function with positive transfer operators in two directions.

### 7.2 Lemmas

**Lemma K2 (PROVED).** kappa and kappa' are non-negative, convex and non-increasing on the integers >= 3.

Proof (for kappa; kappa' is the same with the two families exchanged). (a) For a positive trace-class T,
(Tr T^a)^(1/a) decreases to lambda_0 (Lemma A (a)); so e(b) = lim over a of (1/a) log W(a, b) = inf over a.
(b) W(a, jb) = Tr (T'_a)^(jb) <= (Tr (T'_a)^b)^j = W(a, b)^j by Lemma A (a) for T'_a; divide by a and let a grow:
e(jb) <= j e(b). By (a), ell = inf over b of e(b)/b, so kappa >= 0. (c) For fixed a, b -> log W(a, b) =
log sum_i mu_i^b (mu_i the eigenvalues of T'_a) is convex; e is a pointwise limit of convex functions, and kappa
differs from e by a linear term. (d) If kappa(b_0 + 1) - kappa(b_0) = c > 0, convexity gives kappa(b) >= c (b - b_0)
for b >= b_0, so e(b)/b >= ell + c/2 for b >= 2 b_0; choose b_1 with e(b_1)/b_1 < ell + c/2; by (b) the same holds at
every multiple j b_1: contradiction. QED

**Lemma X2 (crossing; PROVED).** For all a, b >= 3: a kappa(b) + g(a, b) = b kappa'(a) + g'(b, a).
Proof. Both sides equal log W(a, b) - ell a b. QED

**Lemma E2o (one side doubled; PROVED).** g(a, 2b) <= 2 g(a, b) + 2a kappa(b), and
g'(b, 2a) <= 2 g'(b, a) + 2b kappa'(a). Also (T): S(2a; b) <= S(a; b)^2, S'(2b; a) <= S'(b; a)^2, and g, g' are
non-increasing in their time argument.
Proof. W(a, 2b) = Tr (T'_a)^(2b) <= (Tr (T'_a)^b)^2 = W(a, b)^2, so a e(2b) + g(a, 2b) <= 2a e(b) + 2 g(a, b), and
2 e(b) - e(2b) = 2 kappa(b) - kappa(2b) <= 2 kappa(b). The crossed line is the same with T_b. (T) is
sum r_i^(2a) <= (sum r_i^a)^2 for r_i in [0, 1]. QED

**Lemma D (the deficit from two seeds; PROVED; new).** For integers alpha >= 3 and b'' > b >= 3:

kappa(b) <= [ b g(alpha, b'') + b'' g'(b, alpha) ] / ( alpha (b'' - b) ).

Proof. Lemma X2 at (alpha, b), dropping g(alpha, b) >= 0: alpha kappa(b) <= b kappa'(alpha) + g'(b, alpha).
Lemma X2 at (alpha, b''), dropping g'(b'', alpha) >= 0: b'' kappa'(alpha) <= alpha kappa(b'') + g(alpha, b'').
Insert the second in the first and use kappa(b'') <= kappa(b) (Lemma K2):
alpha kappa(b) <= (b/b'') alpha kappa(b) + (b/b'') g(alpha, b'') + g'(b, alpha). Collect kappa(b). QED

**Lemma D' (PROVED).** For a, b >= 3 and alpha > 2a: (alpha - 2a) kappa(b) <= 2 g(a, b) + 2 g'(b, alpha).
Mirror: for A, B >= 3 and beta > 2B: (beta - 2B) kappa'(A) <= 2 g'(B, A) + 2 g(A, beta).
Proof. Lemma D with b'' = 2b: alpha kappa(b) <= g(alpha, 2b) + 2 g'(b, alpha). Since alpha >= a,
g(alpha, 2b) <= g(a, 2b) <= 2 g(a, b) + 2a kappa(b) (Lemma E2o). Collect kappa(b). The mirror is the same proof with
the two families exchanged. QED

In the symmetric case (g' = g, kappa' = kappa) Lemma X of the lane gives (b - a) kappa(b) <= g(a, b) from one seed.
Lemma D' asks two: the direct sum at time a and the crossed sum at time b on the box alpha. No relation between
a and b is assumed; the relation "time shorter than the side" (audit row 18) is replaced by the second seed.

### 7.3 Theorem 2O (two directions)

**Theorem 2O (PROVED).** In the setting (2O) let a, b >= 3 and

u := max( g(a, b), g'(b, 4a) ) <= 1/1400.

Put a_k = 2^k a, b_k = 2^k b, u_k := max( g(a_k, b_k), g'(b_k, 4 a_k) ), K = 1365. Then for all k >= 0:
(i) u_(k+1) <= K u_k^2, hence K u_k <= (K u)^(2^k);
(ii) S(a_k; b_k) <= 1.001 (K u)^(2^k)/K and S'(b_k; 4 a_k) <= 1.001 (K u)^(2^k)/K;
(iii) if the top eigenvalues are simple, the gap of T_(b_k) is at least log(1/(K u))/a and the gap of T'_(4 a_k) is
at least log(1/(K u))/b (gap = log(lambda_0/lambda_1)).

Proof. Write x = g(a, b), y = g'(b, 4a).
(1) Lemma D' with alpha = 4a: 2a kappa(b) <= 2x + 2y, so a kappa(b) <= x + y.
(2) Lemma E2o: g(a, 2b) <= 2x + 2a kappa(b) <= 4x + 2y. Again, with kappa(2b) <= kappa(b):
g(a, 4b) <= 2 g(a, 2b) + 2a kappa(2b) <= 10x + 6y.
(3) Mirror D' with A = 4a, B = b, beta = 4b: 2b kappa'(4a) <= 2 g'(b, 4a) + 2 g(4a, 4b) <= 2y + 2 g(a, 4b), so
b kappa'(4a) <= 10x + 7y.
(4) New direct seed: S(2a; 2b) <= S(a; 2b)^2 <= (e^(4x + 2y) - 1)^2 <= (e^(6u) - 1)^2.
(5) New crossed seed, time 2b, box 8a = 4 (2a): g'(b, 8a) <= 2y + 2b kappa'(4a) <= 20x + 16y <= 36u, and
S'(2b; 8a) <= S'(b; 8a)^2 <= (e^(36u) - 1)^2.
(6) For u <= 1/1400: e^(36u) - 1 <= 36u e^(36u), and e^(72u) <= e^(0.05143) < 1.0528, so both new sums are at most
1296 x 1.0528 u^2 < 1365 u^2; g <= S gives u_1 <= K u^2 <= (1365/1400) u. The pair (2a, 2b) satisfies the
hypothesis again, so (i) follows by induction. (ii): for k >= 1 by (4)-(6) at stage k - 1; for k = 0,
S = e^g - 1 <= 1.001 u. (iii): lambda_1/lambda_0 to the power a_k is at most S(a_k; b_k), so the gap is at least
(1/a_k)(2^k log(1/(K u)) + log K - log 1.001) >= log(1/(K u))/a; the same for T'. QED

Remarks. (a) The constants are not optimised (the lane's symmetric Corollary S2 has threshold 1/20 in two directions).
(b) The hypothesis is on ONE pair of sizes; the conclusion covers the dyadic multiples; other sizes need Lemma E'
in this setting (not written). (c) The four-direction form for the anisotropic Wilson weight (time coupling beta_t,
space coupling beta_s): the pairs (time, space_i) are in setting (2O) with the other sides as spectators, the pairs
(space_i, space_j) are symmetric. A recursion that enlarges the three space sides and the time, as Proposition B3 and
Theorem SH do, needs seeds for the time operator and for one space operator; I did not write its bookkeeping.
OPEN (expected routine; ARGUED).

### 7.4 Sheared tori and projected traces (the first step of A4 and B1)

**Lemma SHIFT (PROVED; a relabelling of a lattice).** Let Lambda be the sublattice of Z^2 generated by (a, v) and
(0, b), 0 < v < b, and d = gcd(v, b), with integers m, n such that m b + n v = d. Then Lambda is generated by
(ab/d, 0) and (na, d). So, with tau and tau' the unit translations of the two slices,

Tr( T_b^a tau^v ) = Z(Z^2/Lambda) = Tr( (T'_(ab/d))^d tau'^(na) ).

Proof. Lambda = {(ia, iv + jb)}. The second coordinates fill dZ. Those equal to 0 have i in (b/d)Z, first coordinate
in (ab/d)Z. The element i = n, j = m is (na, d). QED
For v = 1: a time a on the box b with a unit shift is a time 1 on the box ab with the shift na: one helix. The
shortest closed loops keep their lengths (b, and about a), so no large-box information is gained (SMALL-BOX).

**Projected doubling (PROVED given (TM) for sheared slices, which is the same reflection argument and is not
rewritten here).** Let direction 3 be a spectator of period N, P_0 the projection on zero momentum in it,
W_v(a, b) = Tr(T_b^a tau_3^v) = Tr X_v^b with X_v the direction-2 operator of the slice sheared by v, and write
W_v = lambda_0^a (1 + sum over p of e^(ipv) S_p), S_p >= 0 the thermal sum of momentum p (the vacuum has p = 0).
Then W_P := Tr(T_b^a P_0) = (1/N) sum_v W_v = lambda_0^a (1 + S_0), and

1 + S_0(a; 2b) <= [ (1 + S_0(a; b))^2 + sum over p != 0 of S_p(a; b)^2 ] exp(a (2 e(b) - e(2b))).

Proof. Tr X_v^(2b) <= (Tr X_v^b)^2 for each v; average over v and use Parseval on Z_N. QED
**The crossing identity of the projected trace (PROVED).** With Delta_v := log lambda_0(X_0) - log lambda_0(X_v) >= 0
(because |Tr T^a tau^v| <= Tr T^a for every b):

a e(b) + log(1 + S_0(a; b)) = b e'(a) + log[ (1/N) sum_v e^(-b Delta_v) (1 + S'_v(b)) ],

and the last term lies between -log N and log(1 + max_v S'_v(b)).
Reading (ARGUED). The doubling reads the other momenta only at second order: that is the possible gain (m a near 6
in place of 12 in the dilute picture). But the deficit step needs the last term near 0, that is b Delta_v << 1 for
every shear, and W_v/W_0 = (1 + sum_p e^(ipv) S_p)/(1 + S) is near 1 for all v only if the FULL sum S is small. So
a projected seed does not replace the full one in the deficit step. The count is intrinsic to the crossing.

### 7.5 GUIDE run (a run can refute or guide; it proves nothing)

Model: 2D Ising on the a x b torus with unequal couplings J_1, J_2 (no axis exchange), sizes 3 to 11 in both
directions (dense transfer matrices up to 2048 x 2048), ell from Onsager's double integral on a 3000 x 3000 midpoint
grid. Criteria written first: FAIL if kappa or kappa' is negative or increases, if the crossing identity is off by
1e-8, or if Lemma D, D', its mirror or Lemma E2o is violated by 1e-9 at any admissible sizes. Script and log:
`/tmp/gap-constraints-962/test2o.py`, `test2o.log` (scratch, not committed). One job under the numeric lock, memory
free 73 percent, peak RSS 354 MB, a few seconds each.

| (J_1, J_2) | crossing error | max lhs/rhs: Lemma D | D' | mirror D' | E2o direct | E2o crossed | result |
|---|---|---|---|---|---|---|---|
| (0.30, 0.60) | 1.6e-14 | 0.717 | 0.203 | 0.127 | 0.489 | 0.862 | no violation |
| (0.20, 1.00) | 2.8e-14 | 0.704 | 0.217 | 0.033 | 0.381 | 0.972 | no violation |
| (0.80, 0.10) | 2.0e-14 | 0.380 | 0.024 | 0.226 | 0.999 | 0.114 | no violation |
| (0.10, 0.25) | 2.0e-14 | 0.727 | 0.221 | 0.075 | 0.675 | 0.999 | no violation |
| (0.44, 0.44) | 2.6e-14 | 0.678 | 0.171 | 0.171 | 0.666 | 0.666 | no violation |
| (0.60, 0.35) | 2.9e-14 | 0.529 | 0.119 | 0.189 | 0.799 | 0.524 | no violation |

What the run can establish: no algebra slip of the kind a small anisotropic model would expose; kappa and kappa'
are different functions when J_1 != J_2 (for (0.20, 1.00): kappa(11) = 3.7e-2, kappa'(11) = 4.3e-4), so the
symmetric step kappa(a) >= kappa(b) is really unavailable. What it cannot: the theorem; the recursion step (5)
(its crossed box 8a is beyond dense sizes).

## 8. Ranked list and result (Step 8)

### 8.1 What the audit and the brainstorm say, in plain words

- The seed is one number, fixed by the measure and the scale (1.5). The measure is forced by the account (audit rows
  1, 2, 8, 9, 10, 19). So no change of geometry, boundary, direction, sector or place in the flow makes the number
  smaller or easier. This is the answer to "can we relax the constraint system": not for the seed.
- The slack is on the engine side only (audit rows 14, 15, 18 and row 2 for the engine). One piece of it is used
  here: the axis exchange is not needed (Theorem 2O).
- A relaxation that changes the measure (anisotropy, free walls, another weight, another slice) needs a NEW NODE
  back to the account's state. No such node exists for any of them; (UNIV-K) and (EXIT) are the two known nodes of
  this kind and both are open (rows 924, 846-877).
- So a NEW INPUT can enter at two places only: an order-one inequality for the fixed number ((LSI-J-seed) and its
  equivalents, row 947), or a comparison node between two measures. Nothing in Sections 4-5 is either.

### 8.2 Ranked list (at most five; here three, because the others fail the worth-doing test outright)

None of the three moves an item of the (SEED-FP) chain. By rule 0 of FINISH ("Is it worth doing?") the lead may
rightly launch none. They are ranked by what a lane would leave behind. Chances are my judgement (ARGUED).

1. **Theorem 2O: one cross-provider check, then its four-direction form.** REFRAMING for the seed; NEW theorem.
   First step: check Section 7.1-7.3 line by line (Lemma D is the new step); then write the recursion for the
   anisotropic Wilson weight with seeds for the time operator and one space operator (7.3 remark (c)).
   Fact test: the engine is group-blind; both seeds must fail for U(1) (photon in each channel) and for frozen groups.
   Moves: audit row 2 for the engine; the cost line of row 858 A2. Chance the check passes: 85 percent. Chance it
   supplies a seed: 0.
2. **A proved gap at the target time coupling, on the anisotropic strip (A2 with 1).** REFRAMING (KNOWN path idea 32
   of row 859, new consumer). First step: the exact thermal sum on the line beta_s = 0 (independent link chains;
   one-plaquette rate 4 log(I_1/I_2)(beta_t)), the two seeds of Theorem 2O there, and their stability for
   beta_s beta_t below an explicit constant (a strong-coupling expansion in space only). Result if it lands: a
   volume-uniform gap for SU(2) at beta_t in 2.3-2.6 and small beta_s, and a second proved start for the transport
   family of rows 708, 913, at the target beta_t. Fact test: compact U(1) passes on the strip too (it is confined
   there), so the strip is not selective and must not be; the transport from it must fail at the U(1) transition.
   Moves: nothing on the chain (no anisotropic account); the transport's stop (VAC-SUB) is unchanged. Chance the
   strip theorem lands: 60 percent. Chance of a seed at beta_s = beta_t: below 1 percent.
3. **Decide the projected engine (A4, B1).** REFRAMING. First step: either bound the shear deficits Delta_v of 7.4 by
   second-order sums (then a zero-momentum seed with m a near 6 has an engine), or exhibit a model in the class with
   a small projected sum and no gap (then the count is forced, audit row 15). Fact test: identities; SMALL-BOX holds
   by Lemma SHIFT. Moves: the size of the seed box by a factor near 2, not its nature. Chance of a decision: 50
   percent.

Not worth a lane, with the reason (Sections 4-5): A3 (no tool), A5 (the gluing helps U(1)), A6 (thresholds are not
the obstacle), A7 (wrong spectrum), A8 ((JOIN-TH)), A9 (no engine, fails FT-U1 and SMALL-BOX), B2 (KNOWN; purity is
still a flux statement), B3 and B7 and B8 (readings), B4 ((UNIV-K) or dead), B5 (ceilings), B6 ((VAC-SUB)). A10 is
row 960.

### 8.3 Result table

| Statement | Label |
|---|---|
| Audit of 19 constraints (Section 2): which are forced by the account, by the proof of the engine, by mathematics, and which are choices | ARGUED from READ lines; each row cites its source |
| The seed number is the same at every level of the flow and in both channels; relaxations of representation do not change it | PROVED in the cited rows (row 837 2.2; Lemma X) |
| Lemmas K2, X2, E2o, D, D' and Theorem 2O (engine without axis exchange, two directions, threshold 1/1400, K = 1365) | PROVED (hand); not checked by another model; GUIDE kill test found no violation |
| Four-direction form of Theorem 2O for the anisotropic Wilson weight | OPEN (expected routine) |
| Lemma SHIFT (sheared torus relabelling); projected doubling inequality; projected crossing identity with its entropy term | PROVED (hand; the doubling given (TM) for sheared slices) |
| A projected seed does not replace the full sum in the deficit step | ARGUED |
| Evenness in beta_s for even space sides; Lemma WALL0 | PROVED (one change of variables each) |
| Seed on the line beta_s = 0 at beta_t = 2.3 from a = 6 | GUIDE arithmetic |
| Diagonal reflection positivity of the Wilson weight; the Klein-bottle crosscap identity | ARGUED (not written out) |
| Twist-summed torus: seed false in the confined phase (at least 7 - o(1)) | ARGUED; KNOWN reading (row 876 G11) |
| No relaxation of the constraint system is a NEW INPUT for the seed | finding of Sections 4-6 (a reading of the table, not a theorem) |
| (LSI-J-seed), (SEED-FP), (UNIV-K), (EXIT), (JOIN-TH), (VAC-SUB) | OPEN, unchanged; owned by their rows, not attacked here |

Limits. One author, no check by another model. The 4D gauge-theory statements about anisotropic weights ((TM) in
each direction for unequal couplings, the solved line) are ARGUED from the lane's (TM) and not re-proved. Row 960's
file and check 959 were not on disk. The Sussman-Alpoge outline was not re-read in this row; it enters through the
lane's ports (rows 837, 904, 916, 924), credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text. No cross-branch search was run. Nothing here is a seed, a mass gap or a public claim.

RESULT: Row 962 (Claude Fable 5.2 max, author, checked by no one). Audit of 19 constraints: the measure (isotropic Wilson SU(2) on the hypercubic lattice, every first-passage datum) and the periodic limit state are forced by the Sussman-Alpoge account; trace form, axis exchange, integer multiplicities, time shorter than the sides and a simple top are forced only by the present proof of the engine; slab shape, split, time direction, state space and place in the flow are choices of representation that do not change the seed number. Brainstorm of 19 ideas with fact tests: none is a NEW INPUT for the seed; each is an engine change, a change of measure with no node back to the account, or a reading of the same number; most are KNOWN to the lane (rows 858, 859, 876, 898). PROVED (hand, unchecked): Theorem 2O, a seed-to-gap engine with NO axis exchange (two seeds, one per orientation, max log-sum at most 1/1400, rate log(1/(1365 u))/a), with Lemmas K2, X2, E2o, D, D'; Lemma SHIFT for sheared tori; the projected doubling inequality and crossing identity (other momenta enter at second order, but the deficit step still needs the full sum, ARGUED). GUIDE: a kill test of the lemmas on the anisotropic 2D Ising model at six coupling pairs found no violation. Ranked, none moving the (SEED-FP) chain: 1. check Theorem 2O and write its four-direction form; 2. a proved gap strip at the target beta_t for small beta_s from the solved line beta_s = 0 (fact test: U(1) passes there too, correctly); 3. decide the projected engine. OPEN and unchanged: (LSI-J-seed), (SEED-FP), (UNIV-K), (EXIT), (JOIN-TH), (VAC-SUB); the four-direction form of Theorem 2O.
