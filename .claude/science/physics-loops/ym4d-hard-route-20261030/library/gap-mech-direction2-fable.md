lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T18:51Z

# gap-mech-direction2-fable (queue row 1386)

Worker: Claude Fable 5.2 (model id claude-fable-5-2), Mac mini worker 1, single session, no subagents.
Pinned commit: 5c9ae786d on `claude/ym4d-hard-route`. File created 2026-11-22T06:51Z (date -u).
Status: IN PROGRESS. Nothing below is checked by a second agent. Each step is appended as it is finished.

## 0. Plan (written before any derivation)

Target: (M-neutral) of row 1367, with the checked chain to the mass gap (rows 1342, 1349, 1356, 1359).
Rules of the row: equivalent is not progress; a mechanism must give no gain for compact U(1) in d = 4, none
for SU(2) in d = 5 at weak coupling, and a gain for SU(2) in d = 4.

Steps, in order:

1. Read the facts on file since the switch: rows 1379 to 1384 and their files, the statement (M-neutral) of
   row 1367, the chain rows 1342, 1349, 1356, 1359, and the lead notes after Theorem ZD-c in
   `library/gap-phys-seed.md`. Record exact statements with file anchors (Section 1).
2. Inventory: which facts on file can carry to a statement uniform in n = L/a at physical side L
   (Section 2). One verdict per fact, with the reason.
3. Pick one. State its first exact lemma. Show it is not equivalent to the seed. Run the U(1) test and the
   five-dimensional test on it (Section 3).
4. Attack the lemma as far as the session allows (Section 4 onward), one step per response, each appended.
5. If no route on file can reach (M-neutral): a quantified negative with the class it covers and the kind
   of new input needed.
6. The next two rows and their decisive outcomes; RESULT line.

Status log (times from date -u in the command that wrote the line):

- 2026-11-22T07:01Z read: FINISH.md L1-84, L299-360 (rules); GOAL.md; rows 1342, 1349, 1356, 1359, 1367, 1378 to
  1386 in full; rows 1132, 1141 to 1144, 978, 988, 1326, 1332 (RESULT parts); `gap-mech-direction-fable.md` in
  full; `gap-selective-5d-check-astra62.md` L1-64 and L105-125; `gap-seed-astra62.md` L9-60;
  `gap-phys-seed.md` L311-326; `gap-council-op-astra.md` L1-60 (statement (A)); `parts/gap.md` L8-104;
  `gap-solve-astra62.md` L108 and L285-293. Not read in full: `gap-short-step-variance-fable.md` (RESULT line
  of row 1383 only), `gap-selective-5d-sweep-opus.md`, `gap-mech-direction-check-astra62.md` (RESULT line of
  row 1381 only), `prior/gap-mech-lit-luna.md` (RESULT line of row 1379 only).

## 1. Repo search and the target as read

**Repo search (rule "Repo first").** One loop of `grep -l -i -F` over `library/gap-*.md`,
`library/prior/gap-*.md` and `parts/gap.md` for 22 terms that a blind pass would propose. Every term is on
file (number of files): small-volume (66), toron (60), femto (6), step-scaling (26), Tomboulis (117), Tanizaki
(25), adiabatic (18), conformal window (8), Banks (8), van Baal (59), Schrodinger functional (18), g^(2/3)
(19), twisted box (35), twist eater (23), Gonzalez-Arroyo (10), c-theorem (3), Ito and Seiler (28),
Migdal-Kadanoff (41), 51/121 (10). `library/open-core.md` has no entry for the gap lane (grep for gap, seed,
mass, toron, small-volume, first-passage: no hit). The cross-branch search of this programme is row 1379's
and row 1384's (main, PR 10114, 10133, 10134, 10141: no mechanism); I did not repeat it.

**The target.** (M-neutral), `gap-seed-astra62.md` L11 (gpt-6.2-astra, row 1367; Lemma M1 and Corollary M2 are
Claude Fable's row 1356, checked by row 1359). Fix one physical side L on the trajectory, n_j = L/a_j, 4 | n_j,
beta_0 <= beta_j <= B_0 log n_j. In the range of P_0 (zero spatial twist, mean over the eight electric centre
translations) put s_(n,beta)(t) = sum over a >= 1 of (lambda_a/lambda_0)^t. Wanted: one L with
s_(n_j,beta_j)(2 w_j) <= 4/21 at every late cutoff, w_j = floor(n_j/1024). The quantifier is one physical
side and all late cutoffs. It is not uniform in the volume at one cutoff: that form is false by row 1367 (1).

**Three facts on file that fix where the target sits (none is mine).**

- (R1) No seed in a small box. Row 1143 (7) and (10), checked by row 1144: at fixed lattice side n all seven
  charged bottom energies are at most of order n/beta, and a seed needs n^2 at least about 15 beta/K. Lemma
  FLOOR of row 988 (HOLDS AFTER CORRECTION in its check): no seed with side times gap below 17.04.
- (R2) The account reaches a physical size only while the running coupling is at most gamma (row 1012, as
  quoted in row 1380 M-D; `parts/gap.md` L46-48: "the one selective fact that is provable today, asymptotic
  freedom at small coupling, has no engine that carries it across the band").
- (R3) A non-sharp infrared carry is enough. Row 1332 Theorem T (Claude Fable, PROVED GIVEN named statements,
  check row 1335): one finite inequality (KER) at a window coupling beta_w, the ultraviolet carry (UNIV-K) in
  rate form, and an infrared carry "a seed at beta_w gives a seed at every larger coupling at a size at most
  C exp(c beta)" give the seed; GUIDE: c below about 4.0 per unit of beta, against 2.7 for asymptotic
  freedom. So the lane already holds the architecture of the 2D proofs (one all-coupling bound with slack,
  the renormalization group only as a carry). What it lacks is the engine of the all-coupling bound.

## 2. Inventory: which facts on file carry to a statement uniform in n = L/a at physical side L

"Carries" means: from the fact, with inputs that are proved or that the account states, one can write a
statement about the lattices (n_j, beta_j), n_j = L/a_j, for all late j at one physical L. "Reach" is the set
of physical sides L for which that statement has content. Verdicts are mine (ARGUED unless a row is cited).

| # | Fact (row; author; check) | Kind | Uniform in n at physical L? | Reach | Sees the scale? |
|---|---|---|---|---|---|
| F1 | The one-loop step of the account on Balaban's renormalization group (Sussman and Alpoge with Claude and Codex; Balaban) | flow, weak coupling | yes, by construction | L at most L_gamma (running coupling at most gamma) | yes: the logarithm exists only in d = 4; shared classical part with U(1) (check 1384) |
| F2 | Row 1143 (1)-(6), (11)-(13): Z of every periodic or one-plane-twisted torus against the four-holonomy integral J_4(s), of order s^(-3) log s; twist cost (3/2) log beta + log log beta + O_n(1) (gpt-6.2-astra; checked by row 1144; survivor named by check 1384) | fixed lattice, beta to infinity | no as proved: the remainder is extensive in the fine sites (row 1143 L108, OPEN there). Only through F1: Section 2.1 | none as proved; with F1, L at most L_gamma | yes: dt/t at D = 4, integrable at D = 5. Section 2.2: this is classical scale invariance of the quartic valley, not the quantum logarithm |
| F3 | Row 1132: the Haar-commutator multiplier q_G = 1/4 for SU(2), 1 for U(1), and statement (A) (gpt-6.2-astra; (A) OPEN; margin named by check 1384) | (A) is a (K-one) statement in Moser coordinates | (A) is uniform by its wording, and it is OPEN | proved only at beta at most 1/48 (row 1135), by a high-temperature argument that works in five dimensions (check 1384, 8e) | no. q_G is one number of the group. (A) at a physical time implies (Z-UNB): it is a target of seed strength, not a fact |
| F4 | Local selective facts: row 1141 (2), (8), (9)-(13); Lemmas NAB, FR, FR+; CUBE, SOFT; WN2; LF; BD; G1 (rows 1011-1034) | lattice-local, typical fields | yes, trivially: they read cells of a fixed lattice size | they say nothing at the scale L (lengths are lattice units) | no: verbatim in five dimensions (row 1382 as corrected by check 1384) |
| F5 | Row 1380: Lemmas H, H', SP, BR, PIN, Theorem C1 (Claude Fable; check 1381 HOLDS AFTER CORRECTION) | negative, any scale | yes | all L | they exclude lab-frame engines; no positive content |
| F6 | Row 1383: Proposition LIFT, Lemma THIN, Theorem U1, Lemma BOG (Claude Fable; check 1385 running) | identities, one block step | yes (identities) | all L | no: the literal (BUB) holds for U(1) (Theorem U1); the level form is OPEN and has no consumer |
| F7 | Row 1367 (1), (2), (5)-(7), (10) (gpt-6.2-astra; check 1369) | spectral identities and tests on one cube | yes | all L | no: (2) is a disproof test, (5)-(7) bound high angular modes, (10) is a negative |
| F8 | The 2D proofs (OpenAI; Ding, Huang and Yang; rows 1007-1010, 1379) | all-coupling engine in 2D | in 2D | in 2D | the gauge port is closed for lab-frame moves (F5) and has no exact first lemma for dressed moves (rows 1380, 1381, 1383) |

