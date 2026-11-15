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
| P1 | 0, 1 | Locate the record; open and closed lists; the wall, plain and precise | done 13:36Z |
| P2 | 2 | Inventory of what is known, with marks; the inputs since rows 858/878/899 | pending |
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
