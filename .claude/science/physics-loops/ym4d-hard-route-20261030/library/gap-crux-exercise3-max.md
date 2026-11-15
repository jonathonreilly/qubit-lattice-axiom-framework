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
- Step 5 opened the closed list by grep and by targeted reads of the lines it names. No attack file was read in full.
  The files of rows 858, 878, 899 were searched, not re-read. So a "new" mark below means: not found in the
  searched scope, which is written next to it.
- (further items are added below as the run goes)

## Status block

The plan has eight steps. Each maps to steps of the skill.

| Plan step | Skill step | Content | State and main result |
|---|---|---|---|
| P1 | 0, 1 | Locate the record; open and closed lists; the wall, plain and precise | done (written before 2026-11-15T13:44Z) |
| P2 | 2 | Inventory of what is known, with marks; the inputs since rows 858/878/899 | done 2026-11-15T13:44Z: 40 items; 9 are BELIEF |
| P3 | 3, 4 | Reason up from the inventory; assumptions table | done 2026-11-15T13:48Z: C1-C8; 38 assumptions; top five ranked |
| P4 | 5 | Open the closed list; compare; mark found or new | done 2026-11-15T13:50Z: most conclusions found again; added: the product test, a correction to row 988 Route 3 (b)-(c), the contract for H_L; I34 corrected |
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
- 2026-11-15T13:48Z. Steps 3 and 4 on disk (attack files still closed).
- 2026-11-15T13:50Z. Step 5 on disk. Closed list opened by grep and by targeted reads (lines named in Step 5), not read in full.

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
| I34 | The Migdal-Kadanoff recursion for SU(2) in four dimensions flows to strong coupling from every start value (Ito 1985; Muller and Schiemann 1985). It is the one written proof I know of an order-one crossing for a gauge-type model with no second small parameter. **Corrected in Step 5:** the same flow holds for U(N), so for U(1) (Ito and Seiler's Theorem 2.1, quoted in `gap-form-exercise.md` L143). The crossing is group-blind. | THM, published, recalled | literature | not re-read; hypotheses recalled only in outline; the lane's record of it is looked up in Step 5 |
| I35 | Tomboulis (2007): the partition function is bounded above and below by Migdal-Kadanoff decimations. His confinement conclusion has a gap (Ito and Seiler 2007). | THM, published, recalled (the bounds); open (the conclusion) | literature | not re-read |
| I36 | Order-one crossings with a second small parameter 1/N: Kupiainen 1980 (O(N), d = 2), Kopper, Magnen, Rivasseau 1995 (Gross-Neveu mass generation), Gawedzki and Kupiainen 1986 (hierarchical O(N)). | THM, published, recalled | literature | not re-read |
| I37 | The mass gap of the O(3) model in two dimensions at every beta is unproved. The engine has a two-dimensional form (Corollary S2), so the same wall stands there. | BELIEF (state of the literature) and THM, lane (Corollary S2, scope corrected in row 698) | `gap-crux-restate.md` 3.4 | read |
| I38 | Asymptotically free, reflection-positive gauge theories with matter can be gapless in the infrared (Banks and Zaks 1982, perturbative; lattice studies of SU(2) with two adjoint Dirac flavours). | BELIEF | literature | recalled |
| I39 | Fact T: the single-plane twist has classical cost zero for SU(2); for U(1) it costs beta pi^2 n_3 n_4/(2 n_1 n_2). Fact B: b_0 = 11/(24 pi^2) > 0. "No exact inequality found here or in the sources uses Fact B at couplings of order one." | DEF-level fact (T); THM, published, perturbative, recalled (B); reading (the last sentence) | `gap-crux-restate.md` L62 | read |
| I40 | In SU(N) Wilson theories with N >= 4 a bulk first-order transition exists at a finite coupling, and the continuum limit lies beyond it. | BELIEF (numerics, recalled) | literature | recalled |

**Counts.** 40 items: 9 BELIEF (I31, I32, I33, I37 in part, I38, I40, and the numeric parts of I29, I14, I16), the rest DEF, SUPPLIED or THM with the standing shown.
No item of this table is used in a proof below with a mark stronger than its own.

## Step 3. Reasoning up from the inventory

Only items of Step 2 are used. Each statement names its items. T_fix means "a seed at one fixed coupling";
T_W means the wall (W) on a trajectory.

### 3.1 What follows at once

**F1 (PROVED from the proof text of I4).** The engine is blind to the group. Its proof uses (TM), Lemma A and the
exchange of two axes. So it holds for every model with these three properties: compact U(1), Q_8, 2T, K7, w_p,
and every product of two such models.

**F2 (PROVED from I8).** By Theorem ZD (A) iff (D), a model of the class at one coupling has no seed if and only if
D is unbounded, or D is bounded and b m(b^3) is bounded (branch G). So "no seed" has two parts, and Corollary Z4
speaks about one of them. The comparison models sit in branch G in two different ways (reading, from I28-I31):
*G1, degenerate sectors:* z tends to 0 (frozen groups through their flux sectors; coexistence at a first-order
point). *G2, massless particles:* z stays of order one (the photon of U(1); a critical end point). In G1 the
local observables can still have a gap inside one sector or one phase.

**F3 (BELIEF, from I33).** On the account's trajectory the pair (z, D) starts at (near 0, large) at small physical
size. D is large there because the constant modes are not Gaussian. (W) asks for z > 256 D_0 + 30 later.

**F4 (PROVED, a reading of the quantifiers of 1.2, with I22).** (W) reads the couplings beta_j for large j only, and
beta_j tends to infinity on the account's family. So a seed at one fixed coupling is neither necessary nor
sufficient for (W). A bulk first-order point at one finite coupling of the Wilson axis would not contradict (W)
(I40 is the believed example for SU(N), N >= 4).

### 3.2 The least that a solution must contain

**L1 (PROVED given I28, I29).** If (W) held for compact U(1), or for a frozen group, along a sequence beta_j that
tends to infinity, then by Theorem ZD-c a seed would exist at beta_j for large j. This contradicts I28, I29. So
T_W is false for these two kinds of model along every such sequence, and a proof of (W) must use that the
group is continuous and non-abelian.

**L2 (PROVED given I30).** For T_fix the weights w_p give a theorem-backed model where T_fix fails at one coupling.
For T_W they give only the constant sequence at the transition coupling, and that sequence has no first-passage
data. So a tool for T_W passes this test if its hypothesis contains the first-passage data of I22, or a number.
The lane's sentence "the separating property is a number, not a qualitative property" (I30, I21) is therefore
established for T_fix and for tools that do not read the ultraviolet side. For T_W it is not established.

**L3 (PROVED given I8 and (TM-c)).** A proof of (W) gives both halves of (Z-UNB): the zero-flux gap times L and each
flux energy times L are unbounded. So it contains a weak confinement statement.

**L4 (PROVED from F1, I9).** The engine starts above the massless floor (side times gap above 17.04). First-passage
data lie below it (F3, BELIEF). So a proof needs a second mechanism M2 that works between first passage and the
seed scale. M2 cannot hold for every model of the class, because for U(1) nothing changes with the scale.

**L5, the product test (PROVED given I28, I27).** Let M' be the product of compact U(1) at a large coupling and
SU(2) at a small coupling: the group is U(1) x SU(2), the action is the sum of the two Wilson actions, the measure
is the product measure. M' has (TM) and the axis exchange, so it is in the engine's class (F1). Its thermal sum
obeys 1 + S = (1 + S_1)(1 + S_2), its D is D_1 + D_2, and its gap is the smaller of the two gaps. M' has no seed,
because the U(1) factor has none. But D of M' decreases with the size at the scale of the SU(2) correlation
length, and then stops at D_1 > 0. So no statement of the form "if D (or S) decreases under doubling at one
scale, it goes on decreasing" can hold for the whole class. The same holds for a trajectory: a decoupled photon
next to the account's SU(2) theory satisfies every first-passage hypothesis about the SU(2) factor, and (W) fails.
So a tool for T_W must use that **no part of the low spectrum is a decoupled sector**: it must read the whole
state space (a count of states, or the simplicity of the group).

**L6 (reading; BELIEF through I38).** In the wider class of gauge theories with matter, asymptotic freedom,
reflection positivity and centre symmetry together do not give a gap. So a proof must use that the field is the
gauge field alone: the Markov property of the gauge field, or the positivity of the transfer kernel.

### 3.3 The smallest object

The wall is one inequality between two functions of one variable, z^-(L) and D^+(L), at one L (I8). In the form
(PHYS-SEED-Delta) it is one function: D^+(L) < 6.1 x 10^(-4) at one L. The engine then does the rest.

Toy models. The wall bites in the Ising model on rings at its critical coupling (the lane ran this, I8's file L338;
not rebuilt here). A toy with a running coupling and an exactly known finite-size gap is the O(N) model in two
dimensions at N = infinity (the gap equation on a circle). It can test a claimed monotone or convex statement in
log L. I did not build it in this step: no candidate statement to test exists yet (see C6).

### 3.4 Where the result can come from

Every written proof of an order-one crossing that I can name uses one of five sources (I34, I36, I27):

| Source | Example | For Wilson SU(2) in four dimensions |
|---|---|---|
| (s1) a second small parameter | 1/N: I36 | none: N = 2 |
| (s2) a hierarchical model with a monotone quantity | Migdal-Kadanoff: I34 | the model is not hierarchical; only inequalities towards one exist (I35) |
| (s3) an exact solution or a duality with positive weights | Ising, U(1) Villain | none known; for U(1) the dual form proves that there is no gap (I28) |
| (s4) a correlation inequality that is monotone in the coupling | Griffiths for Z_2, Ginibre for U(1) | none known for a non-abelian gauge group |
| (s5) computer-assisted bounds | rigorous numerics | forbidden here (I26) |

How T_W can fail: an infrared fixed point (G2); a decoupled massless sector (L5); degenerate sectors (G1).
It is three problems, not one: by sector (zero flux; flux), by scale (first passage to the floor; floor to the
threshold), and by form (T_fix; T_W).

### 3.5 Making the requirement less wrong

- **Q1.** The fixed-coupling window 2.3 to 2.6 is a proxy (F4, I17). The consumer needs T_W. Tests and tools should be
  judged against T_W.
- **Q2.** The consumer is the gap of the infinite-volume theory on the states made by local observables (I25).
  Flux states on a torus are not such states. So the consumer may need less than (Z-UNB): the zero-flux half.
  The engine as stated in I4 reads the whole space. Whether a zero-flux engine exists in the lane is a Step 5
  question. If the target is the zero-flux gap, the frozen groups are no longer models where the target fails:
  their local observables have a gap for a known reason (F2, G1).
- **Q3.** A dichotomy theorem "gap, or branch G at every scale" is true as stated (I8), given the T0 chain and
  (BDD-Delta). It is a milestone, not the consumer's statement.

### 3.6 The price

If (W) is not derived, the missing input is exactly (Z-UNB) given (BDD-Delta), by I8. In words: no infrared fixed
point, no decoupled massless sector, no degenerate sector. No smaller equivalent statement follows from the
inventory. Note that (BDD-Delta) beyond first passage is itself not in the inventory as proved: the stability
bounds of I24 are extensive, and D is the part of order one.

### 3.7 Conclusions

- **C1 (PROVED; I4).** The engine is group-blind (F1).
- **C2 (PROVED; I8).** No seed means: D unbounded, or branch G. Branch G has two kinds, G1 and G2 (reading).
- **C3 (PROVED; quantifiers of 1.2, I22, I30).** K7 and w_p are tests of T_fix. Against T_W they bind only tools that
  do not read first-passage data. "The separating property is a number" is proved for T_fix only.
- **C4 (PROVED given I28, I29).** For T_W the theorem-backed tests are U(1) and the frozen groups. They force a
  qualitative property: continuous and non-abelian.
- **C5 (PROVED given I28, I27).** The product test L5: no class-wide statement "a decrease under doubling persists".
  A tool for T_W must read the whole state space.
- **C6 (PROVED from C1, C5, I9, with F3 as BELIEF).** A proof anchored in the ultraviolet needs a statement H_L with
  four properties: (i) it holds at first-passage sizes by the account; (ii) it is false for U(1), for frozen
  groups and for the product models; (iii) it passes from L to 2L; (iv) it gives the seed after finitely many
  doublings, uniformly in the cutoff. By (ii) and F3, H_L is a strict inequality that the free photon saturates,
  and by C5 the step (iii) is not class-wide. No such H_L is in the inventory.
- **C7 (reading; I34-I36).** The one known source of an order-one crossing that is open for SU(2) is (s2): an exact
  inequality towards a hierarchical flow that is monotone for non-abelian groups.
- **C8 (PROVED; I8, I25).** The consumer may need only the zero-flux half of (Z-UNB) (Q2). With that target, the
  frozen-group tests change sides.

## Step 4. The assumptions table

"Needed": T = by the target, M = by the method, H = habit. Group (f) is questioned on paper only.

| ID | Assumption | Where used | Needed | If wrong or dropped | Easier? | Check |
|---|---|---|---|---|---|---|
| **(a) Target** | | | | | | |
| a1 | The gap is wanted for the account's own theory (Wilson SU(2), periodic limit points). | I22, I13 | T | Another action of the class needs its own T0 chain. | no; it moves the cost | none known |
| a2 | The gap is wanted on the whole space of the periodic cube, flux sectors included. | I4, I8 | M | Target = zero-flux gap. Frozen groups stop being counter-models; (Z-UNB) loses its flux half. | maybe | Step 5: is there a zero-flux engine? |
| a3 | The gap is wanted uniformly in the cutoff at one physical size. | 1.2 | T | A gap in lattice units at each coupling gives no continuum gap. | no | - |
| a4 | The statement is wanted for every limit point (no uniqueness of the limit is assumed). | I22 | T | With a unique scaling limit, derivatives in the coupling become derivatives in the size. | yes, if scaling were proved | open in the account |
| a5 | Closure means a proof of (W); a conditional theorem does not count. | 1.2 | T | The dichotomy theorem Q3 becomes the deliverable. | yes | owner decision |
| **(b) Formulation** | | | | | | |
| b1 | All four directions are periodic (a trace). | I2, I4 | M | Other boundaries have no trace engine. | no | row 962 (I13) |
| b2 | The lattice is hypercubic and the coupling isotropic (axis exchange). | I4 | M | An engine without axis exchange was claimed, not written (row 962). | unknown | row 962 |
| b3 | The state space is all gauge-invariant functions of one slice. | I2 | M | Sector-wise or local state spaces change the thermal sum. | maybe (a2) | Step 5 |
| b4 | The criterion is the seed: a thermal sum below 1/5041 on the box (N; (2N)^3). | I4, I7 | M | Another trigger (C6) would need another engine. | unknown | - |
| b5 | D is measured from the exact bulk density f. | I1, I6 | M | Two-torus forms (Phi) avoid f (I5). | no | done in the lane |
| b6 | The trajectory is the account's first-passage family; the unit is where the coupling is g. | I22 | T | - | - | - |
| b7 | (BDD-Delta) is available when the wall is stated as "exclude branch G". | I8, 3.6 | M | The third case "D unbounded" must be excluded too. | no | not proved beyond first passage |
| **(c) Reduction** | | | | | | |
| c1 | One class-wide engine carries the whole infrared, and one order-one input feeds it. | I4, I8 | M | A group-specific step at every scale (C6). | unknown | none known |
| c2 | The order-one input is a property of the measure at one scale (a number). | I21, I30 | H | By C3 a tool for T_W may read the ultraviolet side instead. | unknown | C3 |
| c3 | The window 2.3 to 2.6 at fixed coupling stands for the crux. | I14-I16, I32 | H | Fixed-coupling refutations (GUIDE) at 2.3 to 2.6 do not bind T_W. | - | F4 |
| c4 | The continuum input has the form of a hypercontractive rate (HC-phys), (U1), (U2). | I10, I11 | M | (U3) gives (U2) only; a weaker input may do: one size with z > 256 D_0 + 30. | maybe | I8 |
| c5 | The start value (TH) comes from the account through (DET). | I12, I24 | M | Without (TH) the reduction of I10 has no start. | no | rows 986-994 |
| c6 | The carry from strong coupling along beta is the way to order one ((NOCRIT), Route Z). | I17, I9 | H | T_W needs no carry along beta (F4). | - | F4 |
| c7 | The seed size is at least of the order of the correlation length ("rate filter"). | I4 text | M | - | no | proved in the lane |
| **(d) Discard tests** | | | | | | |
| d1 | K7: a tool must fail on the first-order line of the mixed action. | I31, I19 | M | It rests on numerics; and by C3 it tests T_fix. | - | Step 6 |
| d2 | w_p: the theorem-backed form of d1. | I30 | M | It binds at one coupling; by C3 it tests T_fix. | - | Step 6 |
| d3 | U(1): a tool must fail for compact U(1) at weak coupling; the free photon "must fail through the rate". | I28 | T | - | - | Step 6 |
| d4 | Q_8, 2T: a tool must fail for the frozen groups. | I29 | M | For the zero-flux target they are not counter-models (C8). | - | Step 6 |
| d5 | Ceilings 1/3, 2/3, 0.775, 1.0109: methods of a family stop there. | I27 | M | Each caps one family of majorants, not every method. | - | Step 6 |
| d6 | No supremum over tilts (Theorem D2); no uniformity over coupling fields (Lemma SHEET). | I15, I19 | T | They kill a form of hypothesis, not a method; typical-field forms stay. | - | Step 6 |
| d7 | Lemmas CAP and COUNT as necessary conditions on any rate. | I11 | M | They bind the route through Theorem BR only. | - | Step 6 |
| d8 | "It lands on existing lane material", "it was tried". | I18, row 988 | H | A failed search rules out nothing. | - | Step 6 |
| **(e) Beliefs** | | | | | | |
| e1 | Wilson SU(2) has no critical point at any finite coupling, and a gap. | I32 | H | Then (W) is false and the target changes. | - | numerics only |
| e2 | Universality: local SU(2) actions have the same continuum limit. | I40 | H | a1 could then matter in the other direction. | - | none |
| e3 | The small-volume picture (z near 0, D large at small L). | I33 | H | F3, L4, C6 lose their basis. | - | perturbative only |
| e4 | The K7 line exists on large lattices. | I31 | H | d1 is void; d2 remains. | - | row 995 |
| e5 | The wall is the Clay problem itself, so a short argument cannot exist. | - | H | A cheap route is discarded too early. | - | - |
| e6 | A proof must use a number at order one. | I30, I21 | H | See C3: proved for T_fix only. | - | C3 |
| **(f) Working rules** (obeyed; questioned on paper) | | | | | | |
| f1 | No computer-assisted step. | I26 | owner | Not used: even with it, no finite computation bounds a 10^6-dimensional integral; it could only push a ceiling of d5. | no | - |
| f2 | Port the account; do not redo it. Wilson SU(2) is fixed by the account. | I26, I13 | owner | See a1. | - | - |
| f3 | No duplicate attacks; grep the open core first. | I26 | owner | - | - | done (status log) |
| f4 | One row, one session, a fixed budget; 128,000 tokens per response. | row 998 | driver | Long derivations are cut into rows; a multi-row induction has no owner. | - | - |
| f5 | Fact tests before any proof; one verdict each. | rows 988, 996 | lane | A test used outside its valid form discards live tools (Step 6). | - | Step 6 |
| f6 | Write blind approaches before reading the record. | rows 988, 996 | lane | Seven of seven blind approaches landed on old material (I18): the blind step costs about a third of a row. | - | - |
| f7 | Checks run on the same provider while the other provider is held. | I9-I19 | lane | The checks of rows 979-997 are not independent. | - | held rows |
| f8 | Numerics are GUIDE only, under the lock. | I26 | owner | - | - | - |

**Ranking** (by how much the problem changes if the assumption is dropped):

1. **c2 with c3 and c6 (owner-level).** If the order-one input need not be a number at one scale, the lane would
   stop looking for a property that separates Wilson from K7, and would look for a statement H_L of C6.
2. **a2 with d4.** If the target is the zero-flux gap, the lane would re-judge every use of Q_8 and 2T, and would
   state the engine by sector.
3. **c1.** If the infrared engine may use the group at every step, the lane would look for an exact inequality
   that is strict for non-abelian groups (source (s2)).
4. **b7.** If (BDD-Delta) is not available, the wall has a second open half and the dichotomy has a third case.
5. **a5 (owner decision).** If a conditional theorem counts, the lane would write the dichotomy theorem cleanly and stop.

## Step 5. Comparison with the earlier work

The closed list was opened by grep over the 322 files `gap-*.md` and `prior/gap-*.md` of `library/` and by reading the
lines named below. "Found" items are credited to their rows.

| Item | In the earlier work? | Where | Search scope for a "new" mark |
|---|---|---|---|
| C1, engine group-blind | yes | `gap-crux-restate.md` L62 (row 697); "WALL G" `gap-brainstorm-max.md` L257 (row 859) | - |
| C2, first half (no seed = D unbounded or G) | yes | Theorem ZD (D), row 720 | - |
| C2, second half (G1 degenerate sectors, G2 massless) | partly | `gap-flux-exercise.md` 3.4 L181 (row 731: periodic seed = electric flux heavy, full seed = magnetic flux heavy); `gap-ymcons-opus.md` L433 (row 975) | - |
| F4 and Q1 (the fixed-coupling range is not on the path) | yes | `gap-skeleton-final.md` L535 ("stated with no fixed-beta range in it"); row 978 (I17) | - |
| C3 (K7 and w_p test T_fix; against T_W they bind only tools that do not read first-passage data) | **partly; the second half is new in the searched scope and contradicts row 988** | first half: `gap-skeleton-final.md` L537 ("The tests, corrected", Proposition T1; ranges from beta about 0.44, 1, 1.6). Against it: `gap-unit-max.md` L238-242 (Route 3 (b), (c)) and its N2 (L357), repeated in row 996's goal | grep of the same files and of `FINISH.md` for "no first-passage", "has no trajectory", "not a trajectory", "constant sequence", "constant trajectory": 1 and 0 hits |
| C4 (U(1), frozen groups force continuous and non-abelian) | yes | Facts T and B, `gap-crux-restate.md` L62; every fact-test table since row 697 | - |
| C5, the product test | **new in the searched scope** | - | grep of the same files and of `FINISH.md` for "product model", "U(1) x SU(2)", "U(1) times SU(2)", "decoupled photon", "decoupled sector", "decoupled massless": 6 and 1 hits (outside this file) |
| C6, the contract for an ultraviolet-anchored statement H_L | partly | `gap-ymcons-opus.md` Approach 9, L415-446 (row 975): (DRIFT)_c for the Renyi-2 entropy along doublings, calibrated on the photon (S_2 >= 5.06 constant), "asymptotic freedom at the small boxes and the absence of an infrared fixed point"; its own remark L441: "a monotone that is constant at fixed points gives no drift by itself". Lemma META (row 975). Row 720 Part 2 (step scaling, twist ratios) was not re-read. | the four-property form, with the product models in (ii), was not found by the greps above |
| C7, source (s2) | yes, and **my inventory was wrong** | The Migdal-Kadanoff flow also carries U(N), so U(1), to strong coupling: `gap-form-exercise.md` L143-145, L190; "group-blind: they confine 4D U(1) too": `gap-crux-exercise2-max.md` L413 (row 878), `gap-brainstorm-max.md` L407; "name the step where the true U(1) departs from the toy": `gap-brainstorm2-max.md` L163 (row 876); Tomboulis's bounds: `gap-crux-fp.md` L234, `gap-exit-max.md` L292 | - |
| C8 and Q2 (the consumer needs the zero-flux half) | yes, in a stronger form | Row 731, `gap-flux-exercise.md`: C1 and C3 (Theorem EV-L: the limit half reads the even sector only), C4-C6 (the step needs flux sectors, Remark 2.A; three self-dual sector sets; Theorem S-w), 3.4 (the full seed holds in the Z_2 large-beta case), (EV-STEP) open, (KP) proved for Z_2 | - |
| 3.6, (BDD-Delta) is itself open beyond first passage | yes | row 720 (Theorem ZD-c, Class I); row 982 ("named matches not attacked: (BDD-Delta), (MONO-Delta), (Z-UNB)") | - |
| Ranking 1 (c2, c3, c6) | partly | as C3 | as C3 |
| Ranking 2 (a2, d4) | yes | row 731 | - |
| Ranking 3 (c1, a group-specific step) | yes as a wish, no instance | `gap-brainstorm2-max.md` L210 ("invariant cone": none known) | - |

**Corrections to my own Steps 2 to 4.** (1) I34 and C7: the Migdal-Kadanoff crossing is group-blind (corrected in
place in the table). Source (s2) therefore gives no mechanism that separates SU(2) from U(1); the lane's verdict
stands. (2) C8: the lane already has the even-sector limit theorem. The right reading is finer than mine: the
target reads the even sector, the step of the engine needs flux sectors, and there are three engines by sector
set. So the frozen-group tests must be applied per engine: they refute tools for the periodic seed, and they are
positive examples for the full seed (Z_2 at large beta).

**What the fresh pass added** (all unchecked):

1. The product test (L5, C5). It is a model of the engine's class, backed by the same theorem as the U(1) test.
   It refutes every class-wide step "a decrease under doubling persists", and it shows that a tool for T_W must
   read the whole state space.
2. A correction of a filter (C3). Row 988 Route 3 (b)-(c) concludes that branch G "can only be excluded by an
   input that tells the Wilson trajectory from the endpoint family". The valid form gives less: K7 refutes
   class-wide soft statements that do not read ultraviolet data. A statement whose hypothesis contains the
   first-passage data is not tested by K7 at all. Step 6 states this as a row of the audit.
3. The contract for H_L (C6): four properties that an ultraviolet-anchored statement must have.

**What it only found again:** C1, C2, C4, C7, C8, F4, Q1, Q2, 3.6, and the idea of a drift along doublings (row 975).
