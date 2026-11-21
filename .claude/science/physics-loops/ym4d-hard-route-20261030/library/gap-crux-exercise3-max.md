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
- Step 6a does not cover rows 879 to 956. Rows 962-997 were read from their RESULT lines.
- No numeric run. No literature search on the network: published theorems are recalled, and marked so.
- The account was not read in this run; its statements are quoted through the lane's files.
- Lemma PT, Proposition KF and every table of this file are unchecked.

## Status block

The plan has eight steps. Each maps to steps of the skill.

| Plan step | Skill step | Content | State and main result |
|---|---|---|---|
| P1 | 0, 1 | Locate the record; open and closed lists; the wall, plain and precise | done (written before 2026-11-15T13:44Z) |
| P2 | 2 | Inventory of what is known, with marks; the inputs since rows 858/878/899 | done 2026-11-15T13:44Z: 40 items; 9 are BELIEF |
| P3 | 3, 4 | Reason up from the inventory; assumptions table | done 2026-11-15T13:48Z: C1-C8; 38 assumptions; top five ranked |
| P4 | 5 | Open the closed list; compare; mark found or new | done 2026-11-15T13:50Z: most conclusions found again; added: the product test, a correction to row 988 Route 3 (b)-(c), the contract for H_L; I34 corrected |
| P5 | 6 | Audit of the discard tests (K7, U(1), Q_8, 2T, ceilings), set-aside methods, working rules | done 2026-11-15T13:53Z: one verdict too strong (row 988 Route 3 (c), N2; row 996 scope); two lead rules rest on unchecked or unrebuilt inputs; no verdict shown wrong |
| P6 | 7 | Routes: generate, try to kill, rank | done 2026-11-15T13:57Z: seven families; none survives unwounded; three are blocked as target-equivalent or stronger |
| P7 | 8 | Real attempts on the best routes; fact tests | (corrected 2026-11-15T14:00Z: Proposition CT is the lane's (CAS), row 708, found again; see 8.5) done 2026-11-15T13:57Z: Lemma PT, Proposition KF, Proposition CT proved by hand (unchecked); no numeric run; the decisive test of the flow route is deferred with its cost |
| P8 | 9 | Report, work items as complete briefs, RESULT line | done 2026-11-15T14:00Z |

Status log (UTC, each time read from `date -u`):

- 2026-11-15T13:31Z. File created. Read: `GOAL.md` in full, `FINISH.md` lines 1-84, queue row 998 (line 1077).
- 2026-11-15T13:34Z. Skill and references fetched into `/tmp/row998-skill/` and read. Rule 0a grep: `library/open-core.md`
  (564 lines) has no line with Z4, gapless, scale-invariant, (U1), (U2), order one, or seed. FINISH rows that hold
  the wall: 982, 988, 996 (all ended, with RESULT lines). No queued row other than this one names it.
- 2026-11-15T13:44Z. Steps 0 to 2 on disk.
- 2026-11-15T13:48Z. Steps 3 and 4 on disk (attack files still closed).
- 2026-11-15T13:50Z. Step 5 on disk. Closed list opened by grep and by targeted reads (lines named in Step 5), not read in full.
- 2026-11-15T13:53Z. Step 5 addendum and Step 6 on disk.
- 2026-11-15T13:57Z. Steps 7 and 8 on disk. No numeric job was started (no route had a test that fits the budget; see 8.4).
- 2026-11-15T14:00Z. 8.5 (corrections after reading rows 708 and 884) and Step 9 on disk.
- 2026-11-15T14:02Z. Last pass: the persistence claim of L5 and C5 is lowered to ARGUED (its two factors were not constructed); the tests of (CONTR) in 8.3 are restated through "no seed"; Lemma PT (a) proof wording fixed. Run ended.

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

**L5, the product test (the constraint is PROVED given I28; the persistence claim is ARGUED; corrected at the end of the run).** Let M' be the product of compact U(1) at a large coupling and
SU(2) at a small coupling: the group is U(1) x SU(2), the action is the sum of the two Wilson actions, the measure
is the product measure. M' has (TM) and the axis exchange, so it is in the engine's class (F1). Its thermal sum
obeys 1 + S = (1 + S_1)(1 + S_2), its D is D_1 + D_2, and its gap is the smaller of the two gaps. M' has no seed,
because the U(1) factor has none (Lemma PT (d) in 8.1). Its D is D_1 + D_2; D_2 tends to 0, and D_1 stays above
6.1 x 10^(-4) at every size (Theorem ZD (B)). ARGUED, not proved: at a scale where D_1 is nearly constant and D_2
still falls, D of M' falls under a doubling and later stops falling. This needs a massless factor whose D
converges and a massive factor with a long correlation length; I did not construct them. So the statement "no
class-wide step of the form: a decrease of D under doubling persists" is ARGUED only. For a trajectory: a
decoupled photon next to the account's SU(2) theory satisfies every first-passage hypothesis about the SU(2)
factor, and (W) fails. So a tool for T_W must use that **no part of the low spectrum is a decoupled sector**: it
must read the whole state space (a count of states, or the simplicity of the group). This last statement is the
proved part (Corollary PT1).

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
- **C5 (the constraint PROVED given I28; the rest ARGUED).** The product test L5: a tool for T_W must read the whole
  state space. ARGUED only: no class-wide statement "a decrease under doubling persists".
- **C6 (PROVED from C1, C5, I9, with F3 as BELIEF).** A proof anchored in the ultraviolet needs a statement H_L with
  four properties: (i) it holds at first-passage sizes by the account; (ii) it is false for U(1), for frozen
  groups and for the product models; (iii) it passes from L to 2L; (iv) it gives the seed after finitely many
  doublings, uniformly in the cutoff. By (ii) and F3, H_L is a strict inequality that the free photon saturates,
  and by C5 the step (iii) is not class-wide. No such H_L is in the inventory.
- **C7 (reading; I34-I36).** The one known source of an order-one crossing that is open for SU(2) is (s2): an exact
  inequality towards a hierarchical flow that is monotone for non-abelian groups.
- **C8 (PROVED; I8, I25).** The consumer may need only the zero-flux half of (Z-UNB) (Q2). With that target, the
  frozen-group tests change sides. **Corrected in Step 5 and 8.5: true for Z_2 only; false as stated for Q_8, 2T.**

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
| C3 (K7 and w_p test T_fix; against T_W they bind only tools that do not read first-passage data) | **partly; the second half was not found in the searched scope and contradicts row 988** | first half: `gap-skeleton-final.md` L537 ("The tests, corrected", Proposition T1; ranges from beta about 0.44, 1, 1.6). Against it: `gap-unit-max.md` L238-242 (Route 3 (b), (c)) and its N2 (L357), repeated in row 996's goal | grep of the same files and of `FINISH.md` for "no first-passage", "has no trajectory", "not a trajectory", "constant sequence", "constant trajectory": 1 and 0 hits |
| C4 (U(1), frozen groups force continuous and non-abelian) | yes | Facts T and B, `gap-crux-restate.md` L62; every fact-test table since row 697 | - |
| C5, the product test | partly (see the addendum: the device is row 708's; the massless-factor use was not found) | `gap-mid-max.md` L226-229 | grep of the same files and of `FINISH.md` for "product model", "U(1) x SU(2)", "U(1) times SU(2)", "decoupled photon", "decoupled sector", "decoupled massless": 6 and 1 hits (outside this file) |
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
   It shows that a tool for T_W must read the whole state space (PROVED given the U(1) theorem). That it also
   refutes every class-wide step "a decrease under doubling persists" is ARGUED only (3.2, L5).
2. A correction of a filter (C3). Row 988 Route 3 (b)-(c) concludes that branch G "can only be excluded by an
   input that tells the Wilson trajectory from the endpoint family". The valid form gives less: K7 refutes
   class-wide soft statements that do not read ultraviolet data. A statement whose hypothesis contains the
   first-passage data is not tested by K7 at all. Step 6 states this as a row of the audit.
3. The contract for H_L (C6): four properties that an ultraviolet-anchored statement must have.

**What it only found again:** C1, C2, C4, C7, C8, F4, Q1, Q2, 3.6, and the idea of a drift along doublings (row 975).

### Step 5, addendum (after reading `gap-crux-exercise2-max.md` 6a-6d, 8.1b, 9.3-9.6 and `gap-mid-max.md` L219-234)

Three more items of mine are in the earlier work. I correct the table above.

- **The product device is not new.** Row 708 (`gap-mid-max.md`, "The two parts are independent in the class", checked in
  row 709, `gap-mid-check.md` L64) takes the product of Wilson SU(2) with an Ising model: the transfer operator is the
  tensor product and 1 + S = (1 + S_g)(1 + S_I). So the grep count above was a count of other wordings; the device
  is credited to row 708. What is added here is one use of it: the product with a massless gauge factor as a
  test of any step "a decrease under doubling persists", and as a test on a trajectory (L5). Mark of that use:
  not found in the searched scope.
- **C6 is the blockage sentence of exercise 2** (row 878, 6b): "Every engine found is blind, so its seed sits in the
  order-one band; and the one selective fact that is provable today (asymptotic freedom at small coupling) has
  no engine that carries it across the band." Its kinds (K1) small number, (K2) induction with a selective step,
  (K3) exact formula are my sources (s1)-(s5) in other words.
- **Convexity along doublings with a base at weak coupling** is route CX of exercise 2 (8.1b): Lemma CX1 proved,
  (CVX) "false in the class", the base "not available from the account". Its 9.6 states the price in words: "the
  wall equals the absence of one selective inequality that holds at every scale between first passage and about
  ten correlation lengths".

So the fresh pass of this run added two things only: the correction C3 (stated as a verdict in 6d below) and the
massless-factor use of the product device. Everything else was found again.

## Step 6. The blockage: discard tests, set-aside methods, working rules

### 6a. Methods set aside

Rows 1-18 of exercise 2 (`gap-crux-exercise2-max.md` 6a, row 878) are taken as they stand; I do not copy them.
The rows below are the methods set aside since then (rows 879 to 997). They are taken from RESULT lines of
`FINISH.md` (a digest), not from the files, except where a line is named. The list covers the rows that the queue
row names (962, 970, 977-997) and the rows my reading touched (957, 967, 968, 973-976). It does not cover rows 879-956.

| # | Method (authors: the lane's rows) | Reason given | Where | Kind of reason |
|---|---|---|---|---|
| 19 | Box-uniform tilted covariance (TILT-COV-sup), (ABS-flow) | Lemma SUB; frozen-slice runs at beta 2.5, 2.6; Theorem D2 from beta 1.07 up | rows 970, 977, 979 | refuted, theorem-grade GIVEN two ported lemmas |
| 20 | Quotient form (TILT-COV-quot), box-uniform | q_0 about 0.24 (run) with QUOT-CAP | rows 977, 980 | fails a test that rests on a GUIDE |
| 21 | Hypotheses uniform over plaquette coupling fields (TILT with Brascamp-Lieb) | Lemma SHEET: empty on large tori | rows 996, 997 | refuted, theorem-grade |
| 22 | Relaxations of the constraint system (17 ideas: geometry, boundaries, shears, projected seeds, ...) | "no relaxation is a new input" | row 962 | wrong quantity (an engine change is not an input) |
| 23 | A carrier of a seed from one coupling to finer cutoffs | it is (NOCRIT) plus a climb; false for U(1), frozen groups, K7 lines | row 978 | fails a test; open premise |
| 24 | (LSI-br) on the fine lattice from the account's small-field convexity | short by beta_K/beta_0 (T3) | row 982 (N2) | needs a small number; the reason is ARGUED and unchecked (row 984) |
| 25 | (UNIT) by a fine metric, by no metric, by a count of states | all stop at the thermal sum of the cube in the band | row 982 | was tried |
| 26 | A seed below the massless floor (twisted or small boxes) | Lemma FLOOR: side times gap above 17.04 | row 988 | needs a number that first-passage boxes do not have |
| 27 | The beta_t path from zero temporal coupling (Identity G) | needs three-dimensional mixing and (NOCRIT) | rows 988, 992 | open premise |
| 28 | Soft exclusion of branch G by asymptotic freedom | "K7 refutes every soft form"; needs an input that tells Wilson from the K7 family | row 988 Route 3, `gap-unit-max.md` L231-246 | fails a test |
| 29 | Route Z in its Schwarz form (zero-free torus families) | needs n-uniform zero-freeness on periodic tori; the tube width would not give a physical gap | rows 988, 991 | open premise |
| 30 | One-plaquette separating properties (Turan log-concavity, convexity of the trace density, ...) | no consumer; Proposition 4F: the trace density is not log-concave | rows 995, 996 | wrong quantity (no consumer) |
| 31 | Averaged curvature / Polchinski flow; Piazza-Shen disintegration | did not close; averaged forms reduce to pointwise or to Poincare itself | rows 957, 968 | circular / was tried |
| 32 | Plaquette cellular automata; squeeze, rotate, vary the box | GUIDE and analysis rows; no input | rows 960-967 | was tried |
| 33 | Entropy drift (DRIFT)_c along doublings; escape (ESC) | (DRIFT) open and target-like; the u_xy set is transient in one step | rows 975, 976 | open premise; the ESC test was on the wrong set (row 976's own reading) |

### 6b. First principles on the blockage

A tool must give one inequality at one physical size, uniformly in the cutoff (1.2). By F1 the engine is blind. By
L1 and L5 the input cannot be blind: it must fail for a massless factor. By F3 it cannot be read off at first
passage. So the input is one of two kinds:

- (K-one) a property of the measure at one scale in the band, with a number in it; or
- (K-flow) a statement that starts from first-passage data and is carried through the band by a step that fails
  for U(1), for frozen groups and for products with a massless factor.

**The blockage in one sentence** (exercise 2's sentence, with one clause added): every engine found is blind, so its
seed sits in the band; the one selective fact that is provable today, asymptotic freedom at small coupling, has
no engine that carries it across the band; **and since row 988 the lane has searched (K-one) only.**

### 6c. The discard tests in their logical form

Definitions as in the skill: a tool is a hypothesis H with a written proof of "H(M) implies T(M)" on a class K. A
model M' with T(M') false refutes the tool only if H(M') is true. Otherwise it says what a proof of H must use.
T_fix: a seed at the coupling of M'. T_W: (W) along a sequence with first-passage data. T_per: the periodic seed
(flux sectors included). T_ev: the even-sector statement (G_ev) of row 731.

| Test (model M') | Class K | The exact T that fails in M' | How the failure is known | What a tool must use to pass | Binds from |
|---|---|---|---|---|---|
| Compact U(1), Coulomb phase | reflection-positive gauge models with (TM) | T_fix, T_per, T_ev, and T_W along every sequence beta_j to infinity (L1) | THM, published, recalled (Guth; Frohlich and Spencer); in the lane for Villain at beta >= 2^14 (row 786, per exercise 2). At beta of order 1 to a few it is a BELIEF. | the non-abelian structure | theorem-grade at very large beta only. T_W-tools are bound in full, because their couplings tend to infinity. |
| Free photon "through the rate" | Gaussian model on the same lattice | T_per at every size: S_2 >= 5.06 constant (row 975, L428-430); the massless floor 17.04 (row 988) | THM, lane (hand calculations; check 991 for FLOOR) | a rate or a drift that the photon does not have | every size |
| Product with a massless factor (L5; device of row 708) | the engine's class (F1) | T_fix, T_per, T_W (PROVED given the U(1) theorem). ARGUED only: it also refutes a class-wide step "a decrease of D or S under doubling persists" (3.2, L5) | THM given the U(1) theorem and a strong-coupling seed (I27, I28); the product algebra is checked (row 709) | the whole state space (no decoupled sector) | as the U(1) test |
| Frozen Z_2 | same | T_per only. T_ev and the full seed are true there. | THM, lane (Peierls, beta above 2.191; exercise 2, 6c) | connectedness, for T_per tools only | beta above 2.191 |
| Frozen Q_8, 2T | same | T_per; and, in the frozen limit, T_ev too: the frozen transfer operator has at least two centre-even flat states at every box (cross-provider check, row 884, `gap-crux-exercise2-check-astra.md` L227-259). **Corrected in 8.5.** | BELIEF at order one (transition couplings from numerics); the frozen-limit statement is the check's | as Z_2 for T_per; for T_ev: the non-abelian flat states | order one: belief |
| w_p at its transition coupling (Proposition V) | positive-character weights on SU(2) | T_fix at one coupling, every size | THM, published (van Enter and Shlosman), cited; Proposition V proved in the lane given it | a number (how far log w is from linear), **or** first-passage data | one coupling per p, p large. It does not test T_W-tools that read first-passage data (C3). |
| K7 line | same | T_fix on the line | BELIEF (numerics; row 995: supported for beta_A about 1.3 to 1.5 only) | as w_p | as w_p; it is the belief-grade form of the w_p test |
| K7 end point (a massless scalar) | same | T_fix at one point | BELIEF (row 995 doubts the 1981 end point) | as w_p | one point |
| Theorem D2; Lemma SUB | any gauge group in the class | not a model: a theorem that a form of hypothesis is false (supremum over tilts) | THM, lane, GIVEN two ported lemmas not rebuilt (row 979) | typical tilts, or a flow-weighted form | beta above 4 G_S (1.07 on side 4), so also on the trajectory |
| Lemma SHEET | any group | a form of hypothesis is false (uniform over coupling fields) | THM, lane (check 997, same provider) | typical coupling fields | every large torus |
| Lemmas CAP, COUNT | - | necessary conditions on a rate obtained through Theorem BR | THM, lane (check 984) | - | they bind that route only |
| Ceilings 1/3, 2/3, 0.775, 1.0109 | - | not models: ranges where a family of majorants stops | THM, lane (checks 840, 841, 849, 857) | another family | "needs a small number": valid as ranges; each caps one family (row 861) |
| Gauge theories with matter in the conformal window | outside K (non-local weight after integrating the matter) | T_W | BELIEF | the Markov property of the gauge field | not a valid test for tools that use locality of the weight |

Points that follow from the valid form.

1. **K7 and w_p test T_fix.** A tool for T_W whose hypothesis contains first-passage data has H(M') false at K7 and at
   w_p for a trivial reason, so these models give no constraint on it. They do refute class-wide soft statements
   with no ultraviolet hypothesis, as row 988 Route 3 (b) says.
2. **For T_W the theorem-grade tests are U(1), the free photon, the product with a massless factor, D2 and SHEET.**
   None of them asks for a number at one scale. They ask for: non-abelian structure, a rate, the whole state
   space, typical fields.
3. **The K7 line itself is a belief; its theorem-grade form is Proposition V.** A row that discards on K7 should cite
   Proposition V and say for which p.
4. **A pass is no support.** (DRIFT), (CVX), (HC-phys), (U1), (U2) all pass every test. That says only what their
   proofs must use.
5. **The tests are not enough for (K-flow).** No test on record is a model of the SU(2) class with first-passage data
   and no gap. None is believed to exist (I32). So for (K-flow) tools the lane has constraints (points 1, 2) and
   no refutation device. This is a property of the problem, not a gap of the lane.

### 6d. Verdicts re-judged

| # of 6a | The verdict assumes | Valid in the corrected form? | If not: what comes back, and where |
|---|---|---|---|
| 19 | supremum over all tilts; any box | valid for that form, GIVEN the two ported lemmas (not rebuilt, cross-provider check held). Not re-derived. | - |
| 20 | box-uniform quotient form at beta 2.3 | valid as a GUIDE at fixed coupling. It does not bind T_W formally (F4). Not re-derived. | nothing today |
| 21 | uniformity over coupling fields | valid (theorem-grade, same-provider check) | - |
| 22 | an engine change is not an input | valid as reported; not re-derived (the run was partial) | - |
| 23 | the carry runs along beta at fixed physics | valid. It is a T_fix-type tool, so K7 and w_p bind it. | - |
| 24 | T3: the port is short by one logarithm | valid as reported, but ARGUED and unchecked (row 984 lists it as not checked). A lead rule rests on it. | work item W3 |
| 25 | three routes | "was tried": rules out nothing. | - |
| 26 | a class-wide seed threshold | valid in range: it binds every blind trigger. It does not bind a selective trigger (C6). | - |
| 27 | - | valid as reported; not re-derived | - |
| 28 | (c): "the branch can only be excluded by an input that tells the Wilson trajectory from the endpoint family beyond first passage"; N2: no new row "without an input that separates the Wilson trajectory from K7" | **too strong.** (b) is valid: K7 (better: w_p) refutes soft class-wide statements. (c) does not follow: first-passage data already tell the trajectory from K7. The valid necessary conditions are points 1 and 2 of 6c. | The (K-flow) kind comes back as admissible. No instance exists (exercise 2, 6b; route CX failed at its base). On the path of the target. |
| 29 | n-uniform zero-freeness | valid as reported; not re-derived | - |
| 30 | the input is a one-scale property of the weight | valid in range: it covers (K-one) candidates only | as 28 |
| 31, 32 | - | "was tried" / valid as reported; not re-derived | - |
| 33 | the ESC test set | row 976 itself says the test set was trivially transient; the verdict on ESC is "not tested", not "fails" | a real ESC test needs a set of the relaxed slice (row 976's reading) |
| ex2 #18 | Migdal-Kadanoff is group-blind | valid; my own inventory slip (I34) confirms it | - |
| ex2 6c point 1 | Q_8, 2T bind T_per only | **FAILS as a blanket exemption** (cross-provider check, row 884). It holds for Z_2. For frozen Q_8 and 2T the even sum is at least one in the frozen limit; the question at one fixed finite coupling is not settled. Corrected in 6c and 8.5. | nothing comes back; a tool for the even sector is still tested by Q_8 and 2T |

Where the corrected verdicts matter: row 28 and row 30 are on the path. They change what the lead asks of the next
direction row. They do not supply a tool.

### 6e. The working rules (group (f); questioned on paper, all obeyed in this run)

| Rule | What it does | Finding |
|---|---|---|
| "Fact tests before any proof, one verdict each" (rows 988, 996) | filters approaches before work | Sound in the valid form. The fact-test tables have one K7 column for all tools. By 6c point 1 the column should say for which T it is used (T_fix or T_W) and cite Proposition V. |
| Lead notes "do not queue X" (rows 970, 982 N2, 988 N2, 996 note) | discard whole families | Rows 970 and 996: theorem-grade for the forms named. Row 982 N2 rests on T3, ARGUED and unchecked. Row 988 N2 is too strong (6d row 28). |
| "Write blind approaches before reading" | fresh look | In rows 988, 996 and here the blind pass found again what the record holds. In this run it cost 3 of 8 steps and added two small items. A grep of the anchors right after writing would cut the cost. |
| Same-provider checks while the other provider is held | keeps the queue moving | Every check of rows 977-996 (979, 981, 984, 989, 991, 994, 997) is same-provider. Theorem D2, Lemma SHEET, FLOOR and the (DET) chain carry discard verdicts on that basis. |
| "A proof lane stops after three failed routes" | bounds cost | The stop is fine. The summary "failed by three routes" is then quoted as a property of the statement (rows 982, 988). It is a record of a search. |
| No computer-assisted step | contract | Not used. On paper: dropping it would not reach the band; it could only move a ceiling. |
| One row, one session, 128,000 tokens per response | recoverability | A (K-flow) attack is one long induction. It cannot be owned by rows of 40 minutes unless a part file carries its state (the research procedure's `parts/<part>.md`). The gap lane has no such file; its state is spread over row results. |

## Step 7. Routes: generate, try to kill, rank

`proof-search-governance.md` was read in full before this step. No subagent is allowed, so the passes below are
separate passes of this session. They are not independent.

### 7.1 Exact target contract

| Target statement | Quantifiers, domain | Allowed premises | Forbidden weakenings | Edge cases | Completion witness | Not closure |
|---|---|---|---|---|---|---|
| (W) of 1.2: one L in P with z^-(L) > 256 D_0 + 30, D^+ <= D_0 from L/4 on. Equivalent: (PHYS-SEED); D^+(l') < 6.1 x 10^(-4) at one l' in P. | Wilson SU(2); the account's trajectory; uniform in the cutoff | the lane's checked theorems; the account's statements with their status; rebuilt published theorems | a fixed coupling; one finite box; lattice units; a supremum over tilts or coupling fields | must fail for U(1), frozen groups (periodic seed), products with a massless factor | a written proof, checked by another model | a GUIDE run; a conditional theorem; a statement for the even sector with no step |

The contract is neutral: it does not assume that (W) is provable with the allowed premises.

### 7.2 Sources of routes, and the passes

- From the ranking of Step 4: c2 dropped gives the flow kind (K-flow); a5 dropped gives the dichotomy theorem.
- Tools that came back in Step 6: none as a tool; (K-flow) as an admissible kind (6d row 28).
- From 6b: the least a tool must use is a selective step.

**Pass with a lens from outside the lane's words.** I looked down the skill's list. One line each for the empty ones.
*Dynamical systems:* the engine is a map of one variable with an unstable fixed point at 1/5041; a strict Lyapunov
function of the flow across scales would exclude cycles, not fixed points; the wall is a classification of fixed
points. *Probability, marginal dimension:* the one technique I know that proves a logarithmic gain per scale with
no small parameter is that of Aizenman and Duminil-Copin (four-dimensional Ising; recalled, not read). Exercise 2
proposed a reading row on it (its 9.4 item 2); FINISH rows that name it: 689, 735, 740, 746, 878, 885. It
needs a positive geometric representation, which SU(2) lacks. *Operator algebras, categories, K-theory, number
theory:* empty for this wall as far as I can see. *Logic:* the tests show that (W) is not provable by class-wide
means; that is a statement about methods, not an independence result. *Information theory:* row 975, Approaches 5 and 9.

**Pass that argues the wall is misframed.** Four candidate misframings, each tested against the record.
(i) "The seed must be a number at one scale": too narrow, corrected in 6d row 28. (ii) "The flux half is needed":
already corrected by row 731 for the limit half; the step still needs flux sectors. (iii) "Fixed coupling 2.3 to
2.6": already corrected by `gap-skeleton-final.md` L535. (iv) "The gap lane is on the critical path": `GOAL.md` L37
names the gap as a later target and says existence is not proved. That is an owner choice, not a framing error
of the mathematics. Result: no misframing that removes the wall. The question that replaces "which number
separates Wilson from K7" is: **which strict inequality, saturated by a massless factor, passes from L to 2L?**

### 7.3 Routes

| Route | Family: object; mechanism; terminal obligation | Assumption dropped | What one must believe | First artifact | Cost | What it changes |
|---|---|---|---|---|---|---|
| RA | D^+ along doublings; a strict contraction; (CONTR)_theta of 8.3 on the band | c2 | the Casimir free energy contracts by a fixed factor per doubling until the seed | Proposition CT (8.3, done) | proof of (CONTR): unknown, it is the crux | the input becomes a rate, with the extensive bound (TH) as base |
| RB | the plaquette shift on fixed boxes; a sign in beta; (MON') / Theorem D (f) | c6 | abar_n <= abar_2n at every coupling of the trajectory | none new | unknown | same as RA in the coupling variable |
| RC | a property of the measure at one scale; a number; the seed itself | - | a hand bound in the band exists | none | unknown | - |
| RD | the dichotomy as the theorem; no new input; none | a5 | the owner accepts a conditional milestone | a clean statement with its three cases (F2) | one writing row and one check | closes the lane's exact part; opens no new mathematics |
| RE | sector engines; an even step; (EV-STEP), (KP) | a2 | a step for the even sector alone exists | row 731's list | unknown | the tests Q_8, 2T leave the path |
| RF | functional inequalities on the unit chain; (HC-phys), (U1), (U2) | - | a hypercontractive rate uniform in the cutoff | rows 982, 988 | unknown | - |
| RG | comparison with a hierarchical flow; the step where U(1) departs | c1 | an exact inequality that is strict for non-abelian groups | none | unknown | would be the first selective engine |

### 7.4 Kill pass

For each route: does it assume the target; does it contradict a checked result; was it tried; does it fail a
test in the valid form; does it break an owner rule; is its terminal obligation target-equivalent.

| Route | Verdict | Reason |
|---|---|---|
| RA | wounded; **blocked: its terminal obligation is the target or stronger** | (CONTR) gives (W) (Proposition CT); (W) does not give (CONTR) by the lane's theorems (8.3). It passes every test, which is no support. It is (CAS) of row 708 (`gap-mid-max.md` L64-67: "restates the seed in steps"); same family as (MONO-Delta) (row 720) and (DRIFT)_c (row 975). |
| RB | wounded; blocked as RA | a sign with no small number; false in the class (exercise 2, 6a row 5) |
| RC | dead for now | no candidate; every one-scale property found has no consumer (row 996) |
| RD | survives | it is weaker than the target by design; the owner decides whether it counts |
| RE | wounded | (EV-STEP) is open; the even sector alone has no symmetric form (Remark 2.A) |
| RF | wounded; blocked: stronger than the target | (HC-phys) with (TH) gives the seed; the converse is unknown (row 984) |
| RG | dead as a mechanism | the hierarchical flow is group-blind (row 878, 6a row 18); the departing step is the crux |

### 7.5 Ranking and registry

Ranked by what a route would change, divided by what it costs to find out.

| Rank | Route | Strength against the target | Status (governance words) | Concrete evidence | Stop or reopen condition |
|---|---|---|---|---|---|
| 1 | RD, the dichotomy theorem | weaker | candidate-complete as a weaker statement, GIVEN its inputs | Theorem ZD-c, Corollary Z4 (row 720) | owner says a conditional theorem counts, or not |
| 2 | RA, contraction of D | stronger | blocked-equivalent | Proposition CT (8.3) | reopen on a mechanism that gives theta < 1 from the group |
| 3 | RE, sector engines | unknown | blocked-local | row 731 | reopen on an even step |
| 4 | RF, functional inequalities | stronger | blocked-equivalent | rows 978-988 | reopen on a typical-field or flow-weighted form with a supplier |
| 5 | RB, sign in beta | stronger | blocked-equivalent | Theorem D (f) | as RA |
| 6 | RC, one-scale number | target-equivalent | blocked-equivalent | row 996 | reopen on a hand bound in the band |
| 7 | RG, hierarchical comparison | unknown | retired | rows 859, 876, 878 | reopen on an exact inequality that fails for U(1) |

No route is near closure. Three families are blocked because their terminal obligation is the target or stronger.

## Step 8. Real attempts

Rule 0a before each attempt: `library/open-core.md` has no line for these statements (status log). FINISH rows that
name (CONTR): none; files with a contraction of D in these words: gap-phys-seed.md.
All three results are off the direct path: they are statements about filters and about the strength of a route.

### 8.1 Lemma PT (products; PROVED by hand, unchecked; the device is row 708's)

Let M_1 and M_2 be two models on the same lattice. Each has a compact gauge group G_i, a one-plaquette weight w_i
that is a positive class function, (TM), and a partition function that is invariant under the exchange of two
axes. Let M be the model with group G_1 x G_2 and weight w_1(U_1) w_2(U_2). Write Z, F, f, D, T, S, m for M and
the same letters with an index for the factors. Then, for every box B and every time k >= 1:

- (a) Z(n) = Z_1(n) Z_2(n); so F = F_1 + F_2, f = f_1 + f_2 and D = D_1 + D_2.
- (b) T_B is the tensor product of the two transfer operators. It is positive and trace class, and its top
  eigenvalue is the product of the two top eigenvalues, simple, with a strictly positive eigenfunction. So M is
  in the engine's class.
- (c) 1 + S(k; B) = (1 + S_1(k; B))(1 + S_2(k; B)), and m(B) = min(m_1(B), m_2(B)).
- (d) If M has a seed at N, then each factor has a seed at the same N. If S_1 and S_2 are at most t at (N; (2N)^3),
  then S <= 2t + t^2 there.

Proof. (a) The integral factorizes, because the Haar measure of the product group is the product measure and the
weight is a product. Z is invariant under the exchange of two axes because both factors are. f is the infimum
of F(n)/abs(n). Each F_i(n)/abs(n) does not increase in each side (I3). So along tori whose four sides all grow,
both quotients tend to their infima together, and the infimum of the sum is the sum of the infima. (b) The slice space is the tensor product, and the kernel of
T_B is the product of the two kernels; the gauge projection is the tensor product of the two projections. The
eigenvalues of a tensor product are the products lambda_i mu_j. The largest is lambda_0 mu_0; it is simple
because lambda_0 and mu_0 are. The eigenfunction is the product of two positive functions. (c) Tr T_B^k =
(Tr T_1^k)(Tr T_2^k); divide by (lambda_0 mu_0)^k. The second eigenvalue of T_B is the larger of lambda_1 mu_0 and
lambda_0 mu_1. (d) By (c) and S_i >= 0, S >= S_1 and S >= S_2. The second claim is (c) again. QED

**Corollary PT1 (PROVED given I28).** Let M_1 be compact U(1) at a coupling in its massless phase and M_2 any model of
the class. Then M has no seed, at every size. In particular, for a tool (H, "H implies the seed") that is valid
on the engine's class, H(M) is false. So a hypothesis H that reads only the factor M_2 (its group, its weight,
its first-passage data, the decrease of its D or S under doubling) cannot belong to a valid tool.

**Reading.** This is the exact content of "a tool must read the whole state space" (L5). It is a constraint. It
refutes no statement of the lane that I know. It would refute a future step of the form "if the SU(2) part of
the measure has property P at scale L, then the seed follows", for every P that survives the tensor product.

### 8.2 Proposition KF (what K7 and w_p bind; PROVED, a statement of logic, unchecked)

Let K be a class of models. Let a tool for T_W be a hypothesis H on sequences (a_j, beta_j, model) with a proof
of "H implies (W)" on K. Let M' be the constant sequence at the transition coupling beta_t of a weight w_p for
which the theorem of van Enter and Shlosman holds (I30).

- (a) (W) is false for M' (Proposition V and Theorem ZD-c: a seed at beta_t would follow).
- (b) So H(M') is false for every valid tool.
- (c) If H contains the clause "the sequence has first-passage data in the sense of the account (I22)", then H(M')
  is false by that clause, whatever the rest of H says. So M' gives no constraint on the rest of H.
- (d) If H contains no clause about the ultraviolet side, then the rest of H must fail at M': it must contain a
  number that separates the weight from w_p (the conclusion of `gap-crux-fp.md` L363).

Proof. (a) and (b) are the valid form of a test. (c): beta_t is one finite coupling, and first-passage data require
running couplings that enter a window at arbitrarily small g. (d) is (b) for such H. QED

**Corollary KF1 (correction of `gap-unit-max.md` Route 3 (c) and N2, row 988).** The sentence "the branch can only be
excluded by an input that tells the Wilson trajectory from the endpoint family beyond first passage" holds for
hypotheses of kind (d). For kind (c) the necessary conditions are those of the theorem-grade tests of 6c: fail
for U(1), for the free photon, and for products with a massless factor (Corollary PT1). Mark: PROVED as logic;
the row's own conclusion (the route FAILS at its step (b)) is not changed.

### 8.3 Proposition CT (the strength of the flow route RA; **found again: it is (CAS) of row 708**, see 8.5; the proof below is mine, unchecked)

Let (a_j, beta_j) be a trajectory and P the set of sizes of Theorem ZD-c. Put eps_0 = 6.1 x 10^(-4).

**(CONTR)_theta.** There are L_0 in P, B < infinity and theta < 1 with D^+(L_0) <= B, and for every L >= L_0 in P:
if D^+(L) >= eps_0 then D^+(2L) <= theta D^+(L).

- (a) (CONTR)_theta gives (PHYS-SEED), so (W), at a size L <= 2^k L_0 with k = the least integer above
  log(B/eps_0)/log(1/theta).
- (b) (PHYS-SEED) does not give (CONTR)_theta for any fixed theta by the lane's theorems: they bound D^+ only from
  the seed size on (Lemma Z3), and between L_0 and the seed size the class-wide bound is D^+(2L) <= 16 D^+(L) (I3).
- (c) The base of (CONTR) is available in an extensive form: by (TH) (row 981, as its RESULT line reads; conditional
  on the account and on (DET)) B may be taken as C l^4, with l the side in units of the first-passage length. So
  the number of doublings is at most about (4 log l + log(C/eps_0))/log(1/theta). It is uniform in the cutoff.

Proof. (a) Let L_k = 2^k L_0. If D^+(L_i) >= eps_0 for all i < k, then D^+(L_k) <= theta^k B < eps_0 by the choice of
k. So some L_i with i <= k has D^+(L_i) < eps_0. This is (PHYS-SEED-Delta), and Theorem ZD-c gives (PHYS-SEED).
(b) is a statement about what is proved, not a counterexample. (c) restates (TH). QED

**Tests of (CONTR) in the valid form** (a pass is no support): by (a), read at one coupling, (CONTR) is false in
every model without a seed. So it is false for U(1) in its massless phase, for the frozen groups, and for a
product with a massless factor (Corollary PT1). At the transition couplings of K7 and w_p it is false for the
same reason; as tests of a trajectory statement they do not apply (Proposition KF (c)).

**Strength.** (CONTR) implies the target and is not implied by it. By the governance rule the route is not near
closure: its status is blocked-equivalent. What the proposition adds is the form of the price: **with the
account's extensive bound as base, the whole order-one input is one number theta < 1, the contraction factor of
the Casimir free energy of the symmetric torus under doubling, at the sizes between first passage and the seed.**
For a model with a seed, D falls doubly exponentially from the seed size on (Lemma Z3); for a model without a
seed no theta < 1 can work; class-wide only D(2L) <= 16 D(L) is proved.

### 8.4 Tests: what was run and what is deferred

No numeric job was started in this row. Reason: the only decisive quantity is theta(L) = D(2L)/D(L) in the band.
By Theorem D (f) and I1, D(n; beta) = 6 n^4 times the integral over s in [0, beta] of (abar_inf(s) - abar_n(s)). An
error delta on the plaquette shift gives an error 6 n^4 beta delta on D. For n = 8 and beta = 2.5 one needs delta
well below 1.6 x 10^(-5) at about 25 couplings, and the bulk value to the same precision. With the lane's plain
numpy heat bath (about 13 ms per sweep at 3,500 sites, my memory note of row 936) this is of the order of days.
It does not fit this row, and it would be a GUIDE on a fixed-coupling proxy (F4).

Pre-registered reading, for whoever runs it (written before any run): at n = 4, 8, 16 and beta in [2.2, 2.6],
compute D(n) and D(2n) from the integral above with a stated error. **Fail for RA** (GUIDE): D(2n) >= D(n) within
errors at two successive doublings while D(n) > 0.05. **Not a pass:** any decrease. The test waits on a probe row
with compiled code or on published finite-size plaquette data; it is not proposed as urgent (9.5).

The toy for a running coupling (3.3) was not built: with (CVX) and (MONO-Delta) already known to be selective
(exercise 2, 8.1b), a pass in the toy would be no support and a failure would only repeat that finding.

### 8.5 Corrections after the attempts (rows 708 and 884 read)

The skill asks for the registry search before each attempt. I ran the grep for 8.3 in the same call that wrote 8.3,
and read its hit afterwards. Two corrections follow. Both are against my own text.

1. **Proposition CT is not new.** (CONTR)_theta is (CAS) of row 708, `gap-mid-max.md` L64: "There are theta < 1 and M
   such that Delta(3^4) <= M and, for every a >= 3 with 6.1 x 10^(-4) < Delta(a^4) <= M: Delta((2a)^4) <= theta
   Delta(a^4)". Its verdict there (L67, L209-215): no fixed point of the doubling map above the threshold; "it
   restates the seed in steps"; its form in the coupling is (NOCRIT); "it needs only theta < 1, a number of order
   one". The base in extensive form is row 978's "Where (TH) comes from" (`gap-ladder-max.md` L150) and (APR) of
   row 720. By rule 0a I stop here and attack nothing under it. One remark stays (ARGUED): row 708 says (CAS) has
   the same strength as the seed. As written, (CAS) asks for a decrease at every doubling in a range. A seed gives
   that only if Delta does not rise under a doubling before the seed size, and class-wide only Delta((2a)^4) <=
   16 Delta(a^4) is proved. So the exact relation is "(CAS) gives the seed; the converse is not proved". I know no
   model that separates them.
2. **The finite-group narrowing is struck in part.** I took from exercise 2 (6c point 1) that Q_8 and 2T test only
   tools for the periodic seed. The cross-provider check of that exercise (row 884, Codex gpt-6-astra xhigh,
   `gap-crux-exercise2-check-astra.md` L227-259, L352) marks that argument FAILS: the frozen transfer operator
   of Q_8 or 2T has at least two centre-even flat states at every box, so the even thermal sum is at least one
   in the frozen limit; "local gappedness does not supply ES". The narrowing holds for Z_2. I corrected C8, the
   table of 6c and the last row of 6d. Consequence for the audit: **Q_8 and 2T remain tests of even-sector tools.**
   A fact-test table that drops them for an even-sector route, on the strength of exercise 2, is wrong.

What Step 8 leaves: Lemma PT with Corollary PT1, and Proposition KF with Corollary KF1 (PROVED by hand, unchecked).
Proposition CT is a found-again statement with a governance label.

## Step 9. Report

### 9.1 The wall, in plain words (corrected by the exercise)

We want to prove that a model of the strong force has a lightest particle with positive mass. The lane has an
exact machine: if a certain number, measured on one box, is below a threshold, every larger box has a mass gap.
The machine works for every model of a wide class, also for models that have no gap. So the machine cannot
decide; the number must. On small boxes the theory is nearly free and the number is on the wrong side. It has to
cross to the right side on boxes where the force is strong, and there no expansion works. The exercise confirms
that the missing piece is one statement: on each doubling of the box, between the last small box and the first
good box, a certain free energy shrinks by a fixed factor. In a model with a massless particle it never gets small.
Nobody has a reason, usable in a proof, why this model shrinks it. (No blind check of this text ran.)

### 9.2 What the exercise found

- The exercise did not pass the wall. It did not price it more exactly than rows 708 and 720 already do (found again).
- Almost every conclusion of the fresh pass is already in the lane: rows 697, 708, 720, 731, 859, 876, 878, 975 (reading).
- One verdict since the last exercise is too strong: row 988's conclusion that the missing input must "tell the
  Wilson trajectory from K7". The valid form asks less (Proposition KF, PROVED as logic, unchecked).
- One test use was added: a product with a massless factor. A tool must read the whole state space (Lemma PT,
  Corollary PT1; PROVED given the U(1) theorem, unchecked; the product device is row 708's).
- Two lead rules rest on weak ground: row 982's N2 on an ARGUED, unchecked step (T3); the rule against supremum
  forms on two ported lemmas that are not rebuilt.
- I made two errors against the record and corrected them in place: the Migdal-Kadanoff flow is group-blind
  (I34), and the finite-group narrowing of exercise 2 was struck in part by its cross-provider check (8.5).

**This run produced mainly a map that the lane already had.** By the skill's own measure that is not success. The
two small results count as suggestions until another model checks them.

### 9.3 Filters corrected

| Filter | Verdict | Valid form | What comes back |
|---|---|---|---|
| Row 988 Route 3 (c), its N2, and the scope of row 996: "the input must separate the Wilson trajectory from K7 beyond first passage" | too strong (ARGUED until checked) | K7, and its theorem-grade form w_p, bind hypotheses with no ultraviolet clause. A hypothesis that reads first-passage data is bound by U(1), the free photon, products with a massless factor, Theorem D2 and Lemma SHEET (6c). | The flow kind of input is admissible again. No instance of it exists; its known forms ((CAS), (DRIFT), (MON'), (CVX)) are the target in steps. |
| "K7" as a test | belief-grade | cite Proposition V (van Enter and Shlosman) and name p | - |
| "Q_8 and 2T test the flux half only" (exercise 2) | struck in part by check 884 | holds for Z_2; Q_8 and 2T stay tests of even-sector tools in the frozen limit | nothing comes back |
| Row 982 N2 ("do not queue (LSI-br) from sub-unit convexity") | rests on T3: ARGUED, unchecked | valid as reported | a check of T3 (work item W3) |
| "Failed by three routes" quoted as a property of (UNIT), (U1), (U2) | a record of a search | "was tried" rules out nothing | - |

### 9.4 Routes worth doing (at most three)

1. **The dichotomy as a theorem (route RD).** Believe: the owner accepts a conditional milestone. Cost: one writing
   row and one check. First test: none needed; the statements are rows 697-720. It changes: the exact part of
   the lane is closed and stated once, with its three cases (D unbounded; branch G; gap).
2. **Checks that carry lead rules (W1, W3).** Believe: nothing. Cost: two check rows. They change what the lead may
   queue.
3. **None further.** I do not propose a proof row on (CAS), (DRIFT), (CONTR), (U1) or (U2). No mechanism for the
   selective step is on record, in the lane or in the literature I can recall.

### 9.5 What not to do next

- Another fresh-framing exercise on this wall by this model family. Reason: Step 5 of this run and Step 5 of
  exercise 2: the fresh pass finds the record again. A different provider or a human reader would be a
  different derivation; this is not.
- Another search for a one-scale property that separates Wilson from K7 (row 996 covered it; 6d row 30).
- A proof of any monotone or convex statement along scales by class-wide tools: such statements are false in the
  class (exercise 2, 8.1b; `gap-phys-seed.md` L371-373), and Corollary PT1 gives one more reason.
- The numeric measurement of theta(L) as an urgent item: it is days of plain numpy and a GUIDE on a proxy (8.4).
- A comparison with Migdal-Kadanoff flows: group-blind (row 878).

### 9.6 The exact price

Not sharpened by this run. On record, each "PROVED GIVEN" in the lane:

- (W) holds if and only if (BDD-Delta) and (Z-UNB) hold (Theorem ZD-c, row 720).
- (W) follows from (CAS) with theta < 1 and an extensive base (row 708; base: row 978 L150, conditional on the
  account and on (DET)). So the order-one input can be one number theta < 1 on a bounded range of sizes.
- In words (exercise 2, 9.6, and 6b here): the wall is the absence of one selective inequality at every scale
  between first passage and the seed size. Selective means: false for a massless factor.

### 9.7 Work items

Each item is a complete brief. Paths are relative to
`.claude/science/physics-loops/ym4d-hard-route-20261030/`.

**W1. Check of this file (a model that did not write it; a cross-provider model if one is free; high effort).**
*Statement to check:* `library/gap-crux-exercise3-max.md`: (i) Lemma PT and Corollary PT1 (8.1); (ii) Proposition KF
and Corollary KF1 (8.2); (iii) the rows of the table in 6c for "Product with a massless factor", "w_p", "K7 line"
and "Frozen Q_8, 2T"; (iv) 6d rows 24, 28, 30, 33 and the last two rows; (v) the two corrections of 8.5.
*Read:* this file, Sections 1.2, 3.2 (L5), 6c, 6d, 8.1, 8.2, 8.5; `library/gap-crux-restate.md` L36-56 (definitions,
(TM)) and L170-222 (Theorem S); `library/gap-phys-seed.md` L296-323 (Theorems ZD, ZD-c); `library/gap-crux-fp.md`
L356-364 (Proposition V); `library/gap-unit-max.md` L231-246 and L357 (Route 3, N2); `library/gap-mid-max.md` L64-67,
L226-229 ((CAS), the product device); `library/gap-crux-exercise2-check-astra.md` L227-259.
*Test first:* (a) in Lemma PT (b), that the transfer operator of the product model is the tensor product,
including the gauge projection, for the general weights of (TM-gen); (b) in Lemma PT (a), f = f_1 + f_2;
(c) in Corollary PT1, the step from "massless phase" to "no seed" for compact U(1) with the Wilson weight, and
which published theorem covers it; (d) in Proposition KF (c), whether "first-passage data" is a well-defined
clause for a general weight, and whether the clause can be met by a constant sequence; (e) whether Corollary KF1
changes any conclusion of row 988 other than the wording of (c) and N2.
*Verdict per item:* HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. No new attack.
*Stop rule:* one reading; stop at the list. *Output:* `library/gap-crux-exercise3-check-<model>.md`, ending with one RESULT line.

**W2. Lead note (no proof; the lead edits, I may not).** Reword the standing rule of row 988 N2 and of the note under
row 996. Proposed text: "A direction row on the order-one input states its kind. (K-one): a property of the
measure at one scale. It must name a number, and it is tested against Proposition V (`library/gap-crux-fp.md`
L356) with the p named, and against K7 as a belief. (K-flow): a statement that reads first-passage data. It is
tested against compact U(1), the free photon, a product with a massless factor (Lemma PT of row 998), Theorem
D2 and Lemma SHEET. A fact-test table says which T each column tests. Q_8 and 2T are kept as tests for
even-sector tools (check 884)." Apply only after W1 confirms Proposition KF. *Output:* the FINISH note.

**W3. Check and rebuild of inputs that carry lead rules (Opus-class or cross-provider; high effort).**
*Statements:* (i) T3 of row 982: "the account's small-field convexity, fed into Theorem BR, is short by beta_K/beta_0",
`library/gap-hcphys-max.md` L99 and L177 (marked ARGUED; row 984 lists it as not checked). (ii) The two lemmas that
Theorem D2 imports: reflection positivity of the Wilson action at bisecting planes in the abstract form used,
and Frohlich-Simon-Spencer Gaussian domination with hypotheses (G1)-(G4): `library/gap-tiltproof-max.md` Step 5
(5.2, 5.3) and `library/gap-tiltproof-check-opus.md`.
*Task:* for (i), verdict with the line. For (ii), write each lemma with a full hand proof in a new file
`library/gap-d2-inputs.md`, crediting Osterwalder and Seiler, and Frohlich, Simon and Spencer; no computer step.
*Test first:* in (ii), the gauge-fixed crossing links of 5.2 and the end weights. *Stop rule:* a proof, or the first
failing line. *Output:* `library/gap-d2-inputs.md` and a RESULT line. What it changes: rows 970, 977 and 982 N2
discard whole families on these inputs.

**W4. Owner decision, then one writing row (only if the owner says a conditional theorem counts).**
*Question for the owner:* does a theorem "the continuum theory has a mass gap, or it is in branch G at every
size, or its Casimir free energy is unbounded" count as a milestone of the later target?
*If yes, the writing row:* state the dichotomy once, in continuum form, with every input and its mark: Theorem S
(`library/gap-crux-restate.md` 3.4), Proposition Delta (row 708), Theorem SH (row 707; its cross-provider check is
row 959), Theorems ZD and ZD-c and Corollary Z4 (`library/gap-phys-seed.md` L296-330), Theorem EV-L (row 731) for
the sector read by the limit. State the three cases of F2 here. No new mathematics. *Stop rule:* the statement
and its proof by citation of checked lines; list every input that is still "PROVED GIVEN". *Output:*
`library/gap-dichotomy.md`; then one cross-provider check.

**W5. A state file for the gap lane (the lead; no proof).** Create `parts/gap.md` in the format of the research
procedure (formulation; hardest open obligation; routes tried and why they failed; next action). Copy into it:
the registry of 7.5 with its reopen conditions, the test table of 6c, and the price of 9.6. Reason: since row 858
three exercises and about forty rows end at the same sentence, and each row rebuilds the map from row results.
A new row would start from that file, not from the queue.

**Not proposed, with reasons.** A proof row on (CAS) or (DRIFT): no mechanism (row 708's own verdict). A row on a
selective step from a positive geometric representation: row 885 read the marginal-dimension method; it is not
asserted for continuous or gauge measures. The toy with a running coupling: a pass is no support (8.4). The
theta(L) measurement: cost against value (8.4); its pre-registered reading is in 8.4 if someone runs it. A
change of the lattice action: it moves the cost to the existence chain (a1).

### 9.8 Appendix

The tables of Steps 2 to 8 are above, in step order. The approach registry is 7.5.

- **Assumptions most likely to be wrong:** c2 (the input is a one-scale number): too narrow, 6d row 28. e4 (the K7
  line exists on large lattices): row 995 already doubts the end point. b7 ((BDD-Delta) is available): it is open.
- **Assumptions most expensive to be wrong:** e1 (Wilson SU(2) has no critical point and has a gap): if false, the
  target is false. e3 (the small-volume picture): it carries F3, L4 and every "base" of a flow statement, and
  it is perturbative. The same-provider checks of rows 979-997 (f7): several discard verdicts stand on them.
- **Literature proofs worth translating:** none found that crosses the band for a non-abelian gauge group. The
  two ported lemmas of W3 are worth rebuilding because lead rules rest on them.

### 9.9 Strong words, read against what the run did

- "new": used for nothing in the final text. The two additions are marked "not found in the searched scope"
  (322 files `gap-*.md` and `prior/gap-*.md`, and `FINISH.md`, by the wordings listed in Step 5).
- "every": "every engine found is blind" is exercise 2's sentence about the engines on record. "Every conclusion
  of the fresh pass" is "almost every" (9.2).
- "PROVED": by hand in this file, checked by no one. Proposition KF is a statement of logic, not of analysis.
- "theorem-grade": a published theorem that I recalled and did not re-read, or a lane theorem with a
  same-provider check. Neither is `checked` in the sense of the rules.
- "exact price": not found by this run; 9.6 quotes rows 708 and 720.

RESULT: Row 998 (Claude Fable 5.2 max, Mac mini worker 1; author, checked by no one; no numeric run; exercise skill at main 8b11ae2bb9 followed, steps 0 to 9). The wall is NOT passed and NOT priced more exactly than rows 708 and 720 already price it: (W) iff (BDD-Delta) and (Z-UNB) (Theorem ZD-c), and (W) follows from (CAS), one contraction factor theta < 1 of the Casimir free energy under doubling, with the account's extensive bound as base. The fresh pass found the lane's record again (rows 697, 708, 720, 731, 859, 876, 878, 975). PROVED by hand, unchecked: Lemma PT and Corollary PT1 (a product with a massless factor is in the engine's class and has no seed, so a tool must read the whole state space; the device is row 708's); Proposition KF and Corollary KF1 (K7 and w_p bind only hypotheses with no ultraviolet clause). ARGUED only: that the product also refutes class-wide steps "a decrease under doubling persists". ARGUED filter corrections: row 988 Route 3 (c) and N2 and the scope of row 996 are too strong; K7 is belief-grade and should be cited as Proposition V; row 982 N2 rests on the unchecked T3; the rule against supremum forms rests on two ported lemmas that are not rebuilt. FOUND AGAIN, not new: Proposition CT is (CAS) of row 708. FAILS (my own slips, corrected in place): the Migdal-Kadanoff crossing is group-blind (I34); the finite-group narrowing of exercise 2 was struck in part by check 884, so Q_8 and 2T stay tests of even-sector tools. OPEN: (W), (PHYS-SEED), (BDD-Delta), (Z-UNB), (CAS), (U1), (U2), (HC-phys), and any selective step across the order-one band; no route is near closure (three families are blocked as target-equivalent or stronger). Next: W1 check of this file; W2 rewording of the lead rule after W1; W3 check of T3 and rebuild of the two lemmas under Theorem D2; W4 owner decision on the dichotomy theorem as a milestone; W5 a state file for the gap lane.
