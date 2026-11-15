lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T01:31Z

# Row 998, `gap-crux-exercise3-max`: third wall exercise on the order-one crux

**Header.** Written by Anthropic Claude Fable 5.2, max effort, Mac mini worker 1, one session, started 2026-11-15T13:31Z.
Pinned at commit 637d50c60 of `claude/ym4d-hard-route`. Research-stage working state; it grants no status.
**Nothing in this file is checked by another model.** No commit, no push, no subagents.
Skill: `docs/ai_methodology/skills/exercise/SKILL.md` at main commit 8b11ae2bb9 (fetched by URL, read in full), with
`proof-search-governance.md` (read in full), `RULES.md` sections 1-2 and `procedures/research.md` steps 1-3 (read).
Refresher read: this target is a standalone proof target (its `GOAL.md` reads no framework axiom or primitive). So I
read `GOAL.md` (in full) and the rules of `FINISH.md` (lines 1-84) in place of the framework list. This replacement
is the one the skill allows.

**Marks.** The row asks for PROVED, ARGUED, OPEN, FAILS. The skill allows no mark stronger than `argued` for my own
text. So here: PROVED = proved by hand in this file from named inputs, **not checked** (the skill's `argued`);
ARGUED = an argument with a named gap; OPEN = not proved; FAILS = the route or statement fails, with the failing
line; GUIDE = a run or a number, it decides nothing. Inventory marks are the skill's: DEF, SUPPLIED, THM, BELIEF.

**What this run did not cover** (kept current):

- No blind check of the plain statement of the wall (no fresh agent is allowed in this row).
- The fresh pass (Steps 2 to 4) is not fully blind. The queue row and the result lines of rows 962-997 name the
  failed routes and several idea names, and I read those lines before Step 2. The attack files stayed closed.
- Input rows were read from their RESULT lines in `FINISH.md`, not from their files, until Step 5.
- (further items are added below as the run goes)

## Status block

The plan has eight steps. Each maps to steps of the skill.

| Plan step | Skill step | Content | State and main result |
|---|---|---|---|
| P1 | 0, 1 | Locate the record; open and closed lists; the wall, plain and precise | done (written before 2026-11-15T13:44Z) |
| P2 | 2 | Inventory of what is known, with marks; the inputs since rows 858/878/899 | done 2026-11-15T13:44Z: 40 items; 9 are BELIEF |
| P3 | 3, 4 | Reason up from the inventory; assumptions table | pending |
| P4 | 5 | Open the closed list; compare; mark found or new | pending |
| P5 | 6 | Audit of the discard tests (K7, U(1), Q_8, 2T, ceilings), set-aside methods, working rules | pending |
| P6 | 7 | Routes: generate, try to kill, rank | pending |
| P7 | 8 | Real attempts on the best routes; fact tests | pending |
| P8 | 9 | Report, work items as complete briefs, RESULT line | pending |

Status log (UTC, each time read from `date -u`):

- 2026-11-15T13:31Z. File created. Read: `GOAL.md` in full, `FINISH.md` lines 1-84, queue row 998 (line 1077).
- 2026-11-15T13:34Z. Skill and references fetched into `/tmp/row998-skill/` and read. Rule 0a grep: `library/open-core.md`
  (564 lines) has no line with Z4, gapless, scale-invariant, (U1), (U2), order one, or seed. FINISH rows that hold
  the wall: 982, 988, 996 (all ended, with RESULT lines). No queued row other than this one names it.
- 2026-11-15T13:44Z. Steps 0 to 2 on disk.

## Step 0. The record of the wall, and the two lists

**Where the record is.**

- The wall's statement: `library/gap-phys-seed.md` L296-330 (Theorem ZD, Theorem ZD-c, Corollary Z4; row 720).
- The definitions: `library/gap-crux-restate.md` Section 1 (L36-56); the engine, Theorem D (3.1) and Theorem S with
  Lemmas K, X, E, E' and Corollary S3' (3.4, L170-222; rows 697-699).
- The unit forms: `library/gap-hcphys-max.md` L135-163 ((U1), (U2), (U3), (UNIT); row 982, corrected by row 984).
- The first-passage data of the account: `library/gap-phys-seed.md` 1.1.1 (L60-66), quoting Sussman and Alpoge
  (with Claude and Codex), SA L6844-6869, L6913, L21518-21532.
- Queue rows: 982/984, 988/991, 996/997 (the last three attacks and their checks); 978/981 and 986-994 (continuum
  reduction and (DET)); 962, 970, 977-980 (constraint audit, tilt forms, Theorem D2).
- Earlier exercises on this wall: rows 858 (`gap-crux-exercise-max.md`, `gap-crux-exercise-r858-max.md`), 878
  (`gap-crux-exercise2-max.md`, check `gap-crux-exercise2-check-astra.md`), 899 (`gap-wall-assume-max`), and
  `gap-crux-exercise-astra.md`.

**Open now** (read before Step 2): `GOAL.md`; `FINISH.md` rules; the statements at the lines above (with the short
proofs of Theorems D, S, ZD, which are the lane's checked engine); the RESULT lines of rows 962, 970, 977-982, 984,
986-991, 993-997.

**Closed until Step 5:** the attack and direction files (`gap-unit-max.md`, `gap-hcphys-max.md` Steps 5-7,
`gap-sepinput-max.md`, `gap-tiltproof-max.md`, `gap-direction2-max.md`, `gap-ladder-max.md`,
`gap-constraints-max.md`, `gap-avgcurv-max.md`, `gap-ymcons-opus.md`); the earlier exercises named above and
`gap-flux-exercise.md`, `gap-form-exercise.md`, `gap-shape-exercise-astra.md`; the idea inventories
(`gap-brainstorm-max.md`, `gap-brainstorm2-max.md`, `gap-next3-max.md`, `gap-skeleton-max-b.md`,
`gap-means-max.md`, `gap-status-1113.md`); the literature digests under `library/prior/gap-*`.

**Literature.** The lane has a literature record (`library/prior/gap-*lit*.md`, rows 971, 992, 995). I reuse it in
Step 5 and add only what a new route asks for.

## Step 1. The wall, stated twice

### 1.1 Plain version

We study a model of the strong nuclear force on a four-dimensional grid. We want to prove that its lightest
excitation has a positive mass. This is the "mass gap". The lane has an exact machine: if one number, measured on
one box, is below a fixed threshold (the "seed"), then every larger box has a mass gap of the same size. On very
small boxes the force is weak, the model is nearly free, and the number is above the threshold. The number has to
fall below the threshold on a box where the force has normal strength. There, nothing is small, so no expansion
applies. Every attempt stops at that box. The evidence shows that the machine is right and that the seed is
equivalent to the gap. It does not show the seed. Passing means a written proof of the seed at one box size, or an
exact statement of the one missing input. (Analogy: we proved that a zip, once it engages, closes all the way.
Nobody has made the first tooth engage.)

No blind check ran (no fresh agent is allowed here).

### 1.2 Precise version

**Objects** (DEF, `gap-crux-restate.md` Section 1). Wilson SU(2) on a periodic torus with sides n_mu >= 3; action
A(U) = sum over plaquettes of (1 - (1/2) tr U_p); Z(n) = integral of exp(-beta A) over Haar measure; F = log Z;
f = inf F(n)/|n|. For a box B of three sides, T is the transfer operator, with eigenvalues lambda_0 > lambda_1 >= ...;
m(B) = log(lambda_0/lambda_1); S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k (the thermal sum at time k).
D(a) := F(a^4) - f a^4 >= 0 (the excess free energy of the symmetric torus of side a, called the Casimir free energy).

**The engine** (THM, the lane's; `gap-crux-restate.md` 3.4, checked in rows 698 and 699). If s := S(N; (2N)^3) < 1/5041
for one N >= 3 (the seed), then m(L^3) >= log(1/(5041 s))/N for every integer L >= 2N.

**The dichotomy** (THM, the lane's; Corollary Z4, `gap-phys-seed.md` L322, row 720, "PROVED GIVEN Theorem ZD"). Let
D(a) <= D_0 for all a >= a_0. Then either (branch G) b m(b^3) < 256 D_0 + 29.64 for every multiple b >= 4 a_0 of 4,
or (branch M) there are N and c > 0 with m(L^3) >= c/N for every L >= 2N. Branch G is the gapless, scale-invariant
branch: every cube has a level within a constant times 1/b of its ground state.

**The continuum form** (THM, the lane's; Theorem ZD-c, same file L311). Along a trajectory (a_j, beta_j), with
physical sizes P = {2^i l_1}, D^+(L) := limsup_j D_j(L/a_j) and z^-(L) := liminf_j (L/a_j) m_j((L/a_j)^3):
(PHYS-SEED) holds if and only if (BDD-Delta) D^+ is bounded on P from some size on, and (Z-UNB) z^- is unbounded on P.

**The wall.** For Wilson SU(2) along the account's trajectory (first-passage data, dilated), prove:

> (W) There is a physical size L in P with z^-(L) > 256 D_0 + 30, where D_0 bounds D^+ on the sizes from L/4 on.

Equivalent or sufficient forms on record: (PHYS-SEED); the fixed-coupling seed (SEED) at each beta of the window
2.3 to 2.6 with a carry to finer cutoffs; (U1) or (U2) of row 982 together with the start value (TH) from the
account. "Beyond first passage" means: at box sizes where the running coupling is of order one. The account
controls only boxes that are large against the length where the coupling is g, for one small g; there z is small.

**Quantifiers and domain.** One gauge group, SU(2). One action, Wilson. All four sides periodic. The statement is
needed uniformly in the cutoff (in j), at one physical size.

**Allowed premises.** The lane's checked theorems; the account's statements with their declared status; published
theorems, rebuilt in `library/` before they count. **Forbidden:** any computer-assisted step (GOAL.md, owner
2026-11-01); a number from a run as an input of a proof.

**Outcomes that do not count as closure.** A gap at strong coupling only (below the ceilings). A gap of one finite
box (every finite box has one). A gap in lattice units that is not uniform in the cutoff. A statement with a
supremum over tilts (false by Theorem D2, row 977) or uniform over plaquette coupling fields (false by Lemma
SHEET, row 996). A statement for the zero-flux sector only, unless the flux part of (Z-UNB) is supplied too.

**Required comparison cases.** Any proof must fail for the models where the conclusion is false: compact U(1) at
weak coupling, the frozen finite subgroups Q_8 and 2T, the K7 endpoint of the mixed action, the free photon.

**What fails now.** Each route ends at an inequality for the thermal sum of the cube at order-one coupling. The
last six rows (982, 988, 996 and their checks) end at the same sentence: no input excludes branch G beyond first
passage.

**What would count.** Progress: a proved property of the Wilson measure that fails at the comparison cases and that
a written lemma consumes. Closure: a proof of (W). Price: a proof that (W) is equivalent to one named statement.
No-go: a model of the class in which every proved input of the lane holds and (W) fails.

## Step 2. The inventory: what is known to be true

Sources: the "open now" list of Step 0 and results recalled from the literature. Marks are the skill's. "Lane" means
a theorem of this repository; its standing word is the lane's own, with the check row. I did not re-check any item.
"Read here" says how much of the item I read in this run. A recalled published theorem was not re-read.

### 2.1 The object and the engine

| # | Item | Mark | Source | Standing; read here |
|---|---|---|---|---|
| I1 | The Wilson SU(2) measure on a periodic torus; Z, F, f, D(a), T, m(B), S(k; B) as in 1.2. | DEF | `gap-crux-restate.md` L36-56 | definitions read in full |
| I2 | (TM): Z(n) = Tr T^(n_mu) with T positive, trace class; the top eigenvalue is simple with a positive eigenfunction. | THM, lane | `gap-transfer.md`, row 667 | checked rows 671, 698, 699; statement only |
| I3 | Lemma A and (LB): (Tr T^k)^(1/k) does not increase; F(n)/abs(n) does not increase in each side; D >= 0. | THM, lane | `gap-crux-restate.md` L46-52 | two-line proofs read |
| I4 | Lemmas K, X, E, E', Theorem S, Corollary S3': one seed S(N; (2N)^3) < 1/5041 gives m(L^3) >= log(1/(5041 s))/N for all L >= 2N. The proof uses (TM) and the exchange of two axes only. | THM, lane | same file 3.4 | checked rows 698, 699 (one correction); read in full |
| I5 | Theorem D: 1 + S(n; (2n)^3) <= exp(Phi(n)), Phi(n) = 16 F(n^4) - F((2n)^4); Phi(n; beta) = 96 n^4 times the beta-integral of the finite-size shift of the plaquette mean. | THM, lane | same file 3.1 | checked rows 698, 699; read in full |
| I6 | Proposition Delta: log(1 + S(a; b^3)) <= (b/a)^3 D(a). | THM, lane | row 708 | checked row 709; statement only |
| I7 | Theorem SH: the table of box shapes and thresholds (1/5041, and 1/1650 with two stages). | THM, lane | row 707 | same-provider check; cross-provider check row 959 queued; read only through its use |
| I8 | Theorem ZD and ZD-c: the seed is equivalent to "D bounded and b m(b^3) unbounded"; (PHYS-SEED) iff (BDD-Delta) and (Z-UNB). Corollary Z4: the dichotomy G or M. | THM, lane | `gap-phys-seed.md` L296-330 | "PROVED GIVEN" I4, I6, I7; row 727 checked a conditional part; statements and proofs read |
| I9 | Lemma FLOOR: no seed below the massless floor (side times gap above 17.04). Identity G: S = 0 at zero temporal coupling. Lemma ORD. The Schwarz form of the Route Z transport, with Lemma BC. | THM, lane | rows 988, 991 | check 991 (same provider): HOLDS; RESULT lines only |
| I10 | Lemma IHC and Corollary CU: (SEED-phys) follows from a start value (TH) at the account's torus time and (HC-phys), a hypercontractive rate M_H a uniform in the cutoff. | THM, lane | rows 978, 981 | check 981 (same provider): HOLDS after correction; RESULT lines only |
| I11 | Lemmas CAP, TEL, EE, COUNT: the bridge constants are capped; (U1) gives (U2); (U3) gives (U2), not the converse; (HC-phys) with (TH) is the state count of a massive gas. | THM, lane | rows 982, 984 | check 984 (same provider); RESULT lines only |
| I12 | (TH) needs (DET), a bound between Gaussian normalisers of two tori. Lemma A' and Corollary B give (DET) from (I-loc), R, W; (ID-a) and (ID-b) identify the account's step normaliser, up to one normalisation (r4). | THM, lane; partly ARGUED | rows 986-994 | same-provider checks 989, 994; open: (r4), pr-lay W, the cross-provider check; RESULT lines only |

### 2.2 Results since the last exercises (rows 962 to 997), with their marks

| # | Item | Mark | Source | Standing; read here |
|---|---|---|---|---|
| I13 | Audit of 19 constraints and 17 relaxations: no relaxation of the constraint system is a new input for the seed. | reading (the lane's ARGUED) | row 962 | partial run, unchecked; RESULT line only |
| I14 | Lemma SUB: a tilted covariance is bounded below by the variance at any frozen slice. A box-uniform (TILT-COV-sup), its quotient form and (ABS-flow) are refuted at GUIDE level at beta 2.5 and 2.6. Open form: (LSI-traj-seed). | THM, lane, and GUIDE | row 970 | unchecked (check 972 held); RESULT line only |
| I15 | Theorem D2: a pinning tilt leaves O(4)-symmetric sheets; the sup-over-tilts covariance is at least lam_* times the zero-tilt value, lam_* >= 8.54 (side 4), 21.78 (side 8). So no criterion with a supremum over tilts reaches the seed at beta 2.3. It holds for Q_8 and 2T too. | THM, lane, GIVEN two ported lemmas (reflection positivity at bisecting planes; Frohlich-Simon-Spencer) | rows 977, 979 | check 979 (same provider): HOLDS; the two ported lemmas are not rebuilt |
| I16 | The quotient form is refuted at GUIDE level at beta 2.3 (q_0 about 0.24 to 0.25). | GUIDE | row 980 | unchecked run |
| I17 | A seed at one coupling has no carrier to finer cutoffs except (NOCRIT) plus an asymptotic-freedom climb; beta 2.3 is not a lattice of the account's family. | reading (lane's ARGUED) | row 978 | check 981; RESULT line only |
| I18 | (UNIT) failed by three routes (fine metric, no metric, count of states). (U1), (U2) failed by three more routes (massless floor; a beta_t path that needs three-dimensional mixing and (NOCRIT); no soft exclusion of branch G). | FAILS (records of failed attempts; they rule out nothing) | rows 982, 988 | RESULT lines only |
| I19 | Identity MIX: K7 is Wilson with annealed Gaussian plaquette couplings of variance 8 beta_A/3. Lemma SHEET: every hypothesis uniform over plaquette coupling fields fails on large tori, for every group. Propositions TILT, LIP, MF, ELL, 4F. | THM, lane | rows 996, 997 | check 997 (same provider): HOLDS; RESULT lines only |
| I20 | The Wilson character coefficients c_j = I_(2j+1)/I_1 are strictly log-concave in j (Turan); K7 points and w_p (p >= 2) violate it. No consumer is known. | THM, published, cited; consequence proved in the lane | row 995 | unchecked; RESULT line only |
| I21 | No separating input with a consumer was found. The inputs that tell Wilson from the comparison models and that a lane tool can use are three path statements: (ZF) with Route Z, (VIR_K), the finite-size plaquette shift of I5. | reading | row 996 | RESULT line only |

### 2.3 The account and the consumer

| # | Item | Mark | Source | Standing; read here |
|---|---|---|---|---|
| I22 | The account (Sussman and Alpoge, with Claude and Codex) controls tori whose side is at least l_*(g) times the length where the running coupling is g, g small ("first passage"). "No step of the account integrates the scales between 1 and l." | SUPPLIED (the account, conditional on its packages) | `gap-phys-seed.md` L60-66; SA L6844-6869, L21518-21532 | quoted through the lane's file; SA lines not re-read here |
| I23 | The account's Theorem 0 does not assert clustering, a unique vacuum or a gap. | SUPPLIED | `GOAL.md` L46 (CA-I 2706-2710) | read in GOAL.md |
| I24 | The stability bounds give the start value (TH) after correction, given (DET). | THM, lane, conditional | row 981 | same-provider check |
| I25 | The consumer of (W): the mass gap is a later target, not part of T0. | DEF (contract) | `GOAL.md` L37 | read |
| I26 | Owner rules: no computer-assisted step; port, do not redo; no duplicate attacks; credit by name. | SUPPLIED (working rules) | `GOAL.md` L10-18, L39-48; `FINISH.md` L52-73 | read |

### 2.4 The nearest models, where the conclusion is true or false for a known reason

| # | Item | Mark | Source | Standing; read here |
|---|---|---|---|---|
| I27 | Small beta: a gap and an area law (Osterwalder and Seiler 1978). The lane's proved ranges stop at 1/3, 2/3, 0.775 and 4 G_3 = 1.0109, each for one family of methods. | THM, published, recalled; THM, lane | `gap-status-1113.md` L68, L110, L112, L341 | lane rows 834-841, checks 840, 841, 849, 857; lines read |
| I28 | Compact U(1) in four dimensions has a massless, deconfined phase at large beta (Guth 1980; Frohlich and Spencer 1982). So it has no seed there. | THM, published, recalled | literature | not re-read; whether the source covers the Wilson form of U(1) was not verified here |
| I29 | A finite gauge group is frozen at large beta: perimeter law, flux sectors degenerate up to exponentially small terms. So Q_8 and 2T have no seed there. | THM, published, recalled (Peierls argument); lane check 870 | literature; row 870 | not re-read; the freezing couplings (about 2.2 for 2T) are BELIEF from numerics |
| I30 | The weights w_p = exp(beta ((1 + x)/2)^p) have a first-order transition for large p (van Enter and Shlosman 2005). At the transition coupling there is no seed (Proposition V). | THM, published, cited; THM, lane, GIVEN it | `gap-crux-fp.md` L356-364 | statement and proof of Proposition V read; the published theorem not re-read |
| I31 | K7: the mixed action exp(beta_F x + beta_A (4x^2 - 1)/3) has a first-order line (Bhanot and Creutz 1981). Row 995: the 1981 end point is not a bulk end point on large lattices (Gavai 1996); coexistence is supported for beta_A about 1.3 to 1.5. | BELIEF (numerics) | `gap-mid-max.md` L48; row 995 | lines read |
| I32 | Wilson SU(2) has no bulk transition; a m(0++) = 1.22 to 0.51 at beta 2.3 to 2.6 (Teper); the lattice beta function dips by 25 percent without a zero (Engels, Karsch, Redlich). | BELIEF (numerics) | row 995 | RESULT line only |
| I33 | Small-volume expansion (Luscher; van Baal): in a small periodic box the zero-flux gap is 4.1167 g^(2/3)/L and the flux splitting is of order exp(-12.4637/g). So z tends to 0 at small L. | BELIEF (perturbative, not rigorous) | `gap-phys-seed.md` L194; van Baal hep-ph/0008206 | recalled through the lane's file |
| I34 | The Migdal-Kadanoff recursion for SU(2) in four dimensions flows to strong coupling from every start value (Ito 1985; Muller and Schiemann 1985). It is the one written proof I know of an order-one crossing for a gauge-type model with no second small parameter. | THM, published, recalled | literature | not re-read; hypotheses recalled only in outline; the lane's record of it is looked up in Step 5 |
| I35 | Tomboulis (2007): the partition function is bounded above and below by Migdal-Kadanoff decimations. His confinement conclusion has a gap (Ito and Seiler 2007). | THM, published, recalled (the bounds); open (the conclusion) | literature | not re-read |
| I36 | Order-one crossings with a second small parameter 1/N: Kupiainen 1980 (O(N), d = 2), Kopper, Magnen, Rivasseau 1995 (Gross-Neveu mass generation), Gawedzki and Kupiainen 1986 (hierarchical O(N)). | THM, published, recalled | literature | not re-read |
| I37 | The mass gap of the O(3) model in two dimensions at every beta is unproved. The engine has a two-dimensional form (Corollary S2), so the same wall stands there. | BELIEF (state of the literature) and THM, lane (Corollary S2, scope corrected in row 698) | `gap-crux-restate.md` 3.4 | read |
| I38 | Asymptotically free, reflection-positive gauge theories with matter can be gapless in the infrared (Banks and Zaks 1982, perturbative; lattice studies of SU(2) with two adjoint Dirac flavours). | BELIEF | literature | recalled |
| I39 | Fact T: the single-plane twist has classical cost zero for SU(2); for U(1) it costs beta pi^2 n_3 n_4/(2 n_1 n_2). Fact B: b_0 = 11/(24 pi^2) > 0. "No exact inequality found here or in the sources uses Fact B at couplings of order one." | DEF-level fact (T); THM, published, perturbative, recalled (B); reading (the last sentence) | `gap-crux-restate.md` L62 | read |
| I40 | In SU(N) Wilson theories with N >= 4 a bulk first-order transition exists at a finite coupling, and the continuum limit lies beyond it. | BELIEF (numerics, recalled) | literature | recalled |

**Counts.** 40 items: 9 BELIEF (I31, I32, I33, I37 in part, I38, I40, and the numeric parts of I29, I14, I16), the rest DEF, SUPPLIED or THM with the standing shown.
No item of this table is used in a proof below with a mark stronger than its own.
