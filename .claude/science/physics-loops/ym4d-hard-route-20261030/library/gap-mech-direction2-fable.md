lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T18:51Z

# gap-mech-direction2-fable (queue row 1386)

Worker: Claude Fable 5.2 (model id claude-fable-5-2), Mac mini worker 1, single session, no subagents.
Pinned commit: 5c9ae786d on `claude/ym4d-hard-route`. File created 2026-11-22T06:51Z (date -u).
Status: DONE 2026-11-22T07:17Z (date -u). Nothing below is checked by a second agent. No commit, no push (relay
copies). Reading order: Section 3 (decision and negative), 2.2 (Lemma GRP), 4 (the new input), 5 (rows), 6 (report).

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

- (R1) No periodic seed in a small box. Row 1143 (7) and (10), checked by row 1144: at fixed lattice side n
  all seven charged bottom energies are at most of order n/beta, and a periodic seed needs n^2 at least
  about 15 beta/K. Lemma FLOOR of row 988 (HOLDS AFTER CORRECTION in its check): no seed with side times gap
  below 17.04. For the neutral test in a small box the file has the belief I33 only (Remark STAB).
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
| F2 | Row 1143 (1)-(6), (11)-(13): Z of every periodic or one-plane-twisted torus against the four-holonomy integral J_4(s), of order s^(-3) log s; twist cost (3/2) log beta + log log beta + O_n(1) (gpt-6.2-astra; checked by row 1144; survivor named by check 1384) | fixed lattice, beta to infinity | no as proved: the remainder is extensive in the fine sites (row 1143 L108, OPEN there). Only through F1: Section 2.1 | none as proved; with F1, L at most L_gamma | yes: dt/t at D = 4, integrable at D = 5. Section 2.2: the borderline is the coincidence D = 2N/(N - 1) at N = 2; four-dimensional SU(3) has no such logarithm |
| F3 | Row 1132: the Haar-commutator multiplier q_G = 1/4 for SU(2), 1 for U(1), and statement (A) (gpt-6.2-astra; (A) OPEN; margin named by check 1384) | (A) is a (K-one) statement in Moser coordinates | (A) is uniform by its wording, and it is OPEN | uniformly in the box, proved only at beta at most 1/48 (row 1135), by a high-temperature argument that works in five dimensions (check 1384, 8e); at larger beta only at a box-dependent time (row 1132) | no. q_G is one number of the group. (A) at a physical time implies (Z-UNB): it is a target of seed strength, not a fact |
| F4 | Local selective facts: row 1141 (2), (8), (9)-(13); Lemmas NAB, FR, FR+; CUBE, SOFT; WN2; LF; BD; G1 (rows 1011-1034) | lattice-local, typical fields | yes, trivially: they read cells of a fixed lattice size | they say nothing at the scale L (lengths are lattice units) | no: verbatim in five dimensions (row 1382 as corrected by check 1384) |
| F5 | Row 1380: Lemmas H, H', SP, BR, PIN, Theorem C1 (Claude Fable; check 1381 HOLDS AFTER CORRECTION) | negative, any scale | yes | all L | they exclude lab-frame engines; no positive content |
| F6 | Row 1383: Proposition LIFT, Lemma THIN, Theorem U1, Lemma BOG (Claude Fable; check 1385 running) | identities, one block step | yes (identities) | all L | no: the literal (BUB) holds for U(1) (Theorem U1); the level form is OPEN and has no consumer |
| F7 | Row 1367 (1), (2), (5)-(7), (10) (gpt-6.2-astra; check 1369) | spectral identities and tests on one cube | yes | all L | no: (2) is a disproof test, (5)-(7) bound high angular modes, (10) is a negative |
| F8 | The 2D proofs (OpenAI; Ding, Huang and Yang; rows 1007-1010, 1379) | all-coupling engine in 2D | in 2D | in 2D | the gauge port is closed for lab-frame moves (F5) and has no exact first lemma for dressed moves (rows 1380, 1381, 1383) |


### 2.1 What F1 and F2 give together: the small-volume statement, and why it is on the wrong side

**Statement (SV-Z) (OPEN; not on file as an exact statement; its content is the belief I33 of row 998).**
There is L_gamma > 0 such that for every admissible L <= L_gamma and all late j, with b(L) the account's
running inverse coupling at the scale L,

  | - log(Z_eps/Z_+)(n_j, beta_j) - (3/2) log b(L) - log log b(L) | <= C,   C independent of j and L.

Here Z_eps is the one-plane-twisted partition function of the torus of side n_j = L/a_j. In words: row 1143 (6)
with the bare coupling replaced by the running coupling at the box scale.

- How it would follow (ARGUED). Run the account down to a coarse torus of a fixed side M. The remaining
  integral is over a block field on M^4 sites with weight exp(- b(L) A(V) + E(V)), E bounded on the coarse
  torus by the account's stability bounds. Row 1143 (1)-(3) compares such an integral with J_4(c b(L)) by a
  comb tree gauge and a triangular change of variables. It is written for the exact Wilson weight. It
  survives a multiplicative error exp(+-C) in total, which is what a fixed coarse volume allows.
- What is missing. (i) The account's effective action at flat block fields with a non-trivial holonomy, on the
  whole toron valley and not only near the identity. (ii) The large-field part of the last coarse torus with
  the twist inserted. (iii) Row 1143's comparison for a weight that is Wilson's only up to exp(+-C). None is
  on file. The published picture is Luscher's small-volume expansion and Koller and van Baal (I33: zero-flux
  gap 4.1167 g^(2/3)/L, flux splitting of order exp(-12.4637/g); BELIEF, recalled through the lane's file).
- Uniform in n: yes, at each L <= L_gamma. This is the one statement in the inventory that is uniform in n,
  reads the group and the dimension, and is not lattice-local.
- Tests. Compact U(1), d = 4: the twist is a flux quantum and costs order b (check 1384); no logarithm and no
  running. Passes. SU(2), d = 5: J_5 has no logarithm and b(L) grows like L. Passes. So (SV-Z) is selective.
- Not equivalent to the seed: it holds where the seed fails. As L goes to 0 the twist cost goes to infinity
  and, by I33, the neutral gap times the side goes to 0 like g(L)^(2/3). By (R1) and Lemma FLOOR a seed needs
  side times gap above 17.04.
- **Verdict.** (SV-Z) is a start value of a flow, not a step. It reaches (M-neutral) only through a statement
  that carries it from L_gamma to the seed size, across the band where the running coupling is of order one.
  That statement is (K-flow), M-D of row 1380. So F1 with F2 does not shorten the problem. I do not pick it:
  it would cost a port of the account to twisted coarse tori and would move no open item of the chain
  (rule 0, "Is it worth doing?").

### 2.2 Lemma GRP: the group test on the five-dimensional survivor

The lane's selectivity tests are compact U(1), five dimensions and the adjoint Higgs. I add one that costs
nothing: **a mechanism for the four-dimensional gap must not rest on a fact that is absent for SU(3) in four
dimensions**, since the gap is expected for every SU(N) and the account's extension target is SU(N).

**Lemma GRP (the count is ARGUED here; the threshold is a published theorem, abstract read).** Let G = SU(N),
of dimension g = N^2 - 1 and rank rho = N - 1, and p = g - rho. Let J_D^G(s) be the integral over G^D of
exp(- s sum over i < j of a([h_i, h_j])), a(h) = 1 - Re tr(h)/N. Near a central D-tuple, on the stratum where
the D Lie-algebra vectors lie in one Cartan subalgebra at the common size R, the radial weight is

  R^(D rho + p - 1) dR * (s R^2)^(-(D - 1) p / 2)   for s R^4 >= 1.

(D rho Cartan coordinates and p orbit directions; (D - 1) p transverse directions, each with stiffness of
order s R^2.) The power of R is e = D rho + p - 1 - (D - 1) p. It is - 1, a logarithm, exactly when

  D = D_*(N) := 2 p / (p - rho) = 2N/(N - 1).

So D_*(2) = 4, D_*(3) = 3, and D_*(N) < 3 for N >= 4. For D > D_* the tail in R is integrable and the
constant modes sit at the quartic scale R of order s^(-1/4); then J_D^G(s) is of order s^(-g D/4) with no
logarithm. For SU(2) the count is row 1143's (e = 3 - D). For SU(3) and D = 4: e = 8 + 6 - 1 - 18 = - 5.

Published form: Austing and Wheater, "The convergence of Yang-Mills integrals" (arXiv:hep-th/0101071;
abstract read 2026-11-22): the flat SU(N) bosonic matrix integral converges for D >= D_c, with D_c = 5 for
N = 2, D_c = 4 for N = 3 and D_c = 3 for N >= 4, in agreement with the Monte Carlo of Krauth and Staudacher
(arXiv:hep-th/9804199; abstract read). D_c is the first integer above D_*(N). The lane had credited the SU(2)
threshold to Krauth and Staudacher as recalled (`gap-uv-rigidity-max.md` L646); the general N was not on
file (grep for Austing, for "2N/(N-1)" and for SU(3) in the three files of rows 1028, 1143, 1384: no hit).

**Consequence (ARGUED).** For SU(3) in four dimensions the flat integral converges, so the constant-mode
integral of a fixed four-torus is of order s^(-8), the largest holonomy radius concentrates at beta^(-1/4),
and the twist cost has no log log beta. In this observable four-dimensional SU(3) behaves as five-dimensional
SU(2) does (check 1384: J_5 of order s^(-15/4), radius beta^(-1/4) in probability). Four-dimensional SU(3)
is expected to have a gap and five-dimensional SU(2) at weak coupling is expected to have none. So the
borderline logarithm of row 1143 is not correlated with the gap. It is the coincidence 4 = 2N/(N - 1) at
N = 2, and it does not come from the scale invariance of the coupling: that enters J only through
s = beta n^(D - 4).

**Verdict on F2.** It passes the five-dimensional test and fails the group test. It is not the seed of a
mechanism. (What a check must test: the stratum count for SU(3) near a central tuple, including the lower
strata, where the D vectors commute with an SU(2) subgroup. My count there: the radial power is 7 - 3D = - 5
at D = 4 and the sub-block's own logarithm is cut off at the small end, so no logarithm survives. This agrees
with the convergence theorem, which is what the consequence rests on.)

### 2.3 F3: statement (A) of row 1132 is a target, not a fact

(A) asks, at one physical time t and for all boxes and late cutoffs, that the two-slice law in Moser
coordinates dominates p times a kernel followed by an independent Haar commutator on every link. Its consumer
is proved in row 1132: norm at most 1 - 3p/4 on the mean-zero space, so (Z-UNB). The margin is selective
(q_G = 1/4 against 1). But uniformly in the box (A) is known only at beta <= 1/48 (row 1135), by a
high-temperature argument that check 1384 (8e) transfers to five dimensions at 24 beta < 1. With the full
Wilson slab it holds at a time that depends on the box (row 1132, RESULT). On the trajectory (A) is of the kind (K-one) at
seed strength: it gives the spectral half of the wall outright. Nothing on file bounds p from below at any
coupling above the high-temperature range. In the inventory's terms: uniform in n by its wording, no proved
reach on the trajectory, does not see the scale. Not picked.

- 07:06Z Sections 1, 2 and 2.1 to 2.3 written. Two arXiv abstracts fetched into a scratch folder (Austing and
  Wheater; Krauth and Staudacher). Next: the decision and the quantified negative (Section 3).

## 3. Decision: no route on file reaches (M-neutral). The quantified negative

**Decision.** I pick no fact for an attack. Of the two survivors that check 1384 named, F2 fails the group
test (Lemma GRP) and has no reach, and F3's statement (A) is a target of seed strength with no proved reach.
The one statement that is uniform in n, (SV-Z), lies on the small-box side, where there is no seed. Every
other proved statement with content in the band is lattice-local, an identity or a negative.

**Proposition NEG (the logic is elementary; each input is a cited row; nothing here is a theorem about all
possible proofs).** Let F be the proved statements of the inventory (F1 to F7) and the entries that row 1382
swept, as corrected by check 1384. Split F by domain:

- F_uv: F1 and what the account proves. Content at physical sides L <= L_gamma.
- F_fix: F2. Proved at a fixed lattice side or for n^2 = o(beta) (row 1143, RESULT). On the trajectory
  beta_j <= B_0 log n_j, so for late j no lattice (n_j, beta_j) at any physical L is in its domain.
- F_ht: the proved range of (A), beta <= 1/48. Below the trajectory's couplings.
- F_loc: F4. Lattice-local and selective.
- F_id: F5, F6, F7. Identities, tests and negatives.

Then:

(a) Domain. For L > L_gamma and late j, the members of F with content at (n_j, beta_j) lie in F_loc and F_id.
(b) Blindness. Every member of F_loc holds for SU(2) in five dimensions at the same coupling, with changed
    local counts (check 1384, item by item). Every member of F_id holds for every compact group or is a
    negative. So a derivation of the seed test at a lattice (n, beta) from F_loc and F_id, by steps that are
    themselves valid in five dimensions, gives the same test for SU(2) in five dimensions at that beta.
    Under the premise (P5) that SU(2) in five dimensions has no seed at beta >= beta_5 (belief grade on
    file: row 1011 Section 6), no such derivation exists at beta >= beta_5.
(c) Small boxes. For L <= L_gamma the account has content, but the seed fails there: at a fixed lattice by
    (R1) (PROVED, rows 1143 and 1144, for the periodic test; Lemma FLOOR), and uniformly in the cutoff by the
    small-volume picture I33 (BELIEF). For the neutral test at a fixed lattice the file has I33 only; see
    Remark STAB below.

Conclusion. A proof of (M-neutral) that starts from the file needs at least one statement outside F that
(i) has content at some L > L_gamma for all late cutoffs, and (ii) uses the dimension four in a way that no
local count gives. The candidates on file for that statement are all OPEN and all name the same step:
(K-flow) (row 998), M-D with its level form (rows 1380, 1383), the infrared carry (A2) of row 1332, (VIR_K)
with Theorem TR (row 708), (NOCRIT) with a rate (rows 708, 709, 978), (LEV_K) (row 708).

**Class covered.** Conjunctions of proved statements on file, combined by inferences that hold in five
dimensions. **Not covered:** a new statement; an inference that uses d = 4 through a sum over scales (that is
what a mechanism is); the premise (P5) itself.

**How wide the uncovered band is (numbers on file; the one-loop conversion is GUIDE).** Every first-passage
coupling is above 5 (check 1331). The window is 2.3 to 2.6. At the one-loop rate, 3 pi^2/11 = 2.69 per unit
of beta, the couplings from 5 down to 2.6 are 6.5 e-folds of scale, 9.3 doublings; the true first-passage
coupling 4/gamma^2 is far larger. The file's only proved carry of a seed along the coupling is Lemma CLIMB
of row 1332: at most 8.7e-9/n^4 in total, below 1e-12 at the window size (HOLDS in check 1335 as a bound for
the specified estimate). So the proved cover of the band is a fraction below 1e-12.

**Remark STAB (a filter that follows from (R1); the periodic form is PROVED GIVEN row 1143 (10); the neutral
form is at belief grade, one attempt failed).** Let H(n, beta) be any hypothesis that implies the seed test on the lattice (n, beta). Then
for each n the set of beta with H(n, beta) is bounded above: by K n^2/15 for the periodic test (row 1143
(10)). So a hypothesis that stays true when beta grows at fixed n is false on every large lattice. A first
lemma of a mechanism must contain an upper bound on an inverse coupling at the box scale. Roughness bounds,
small-field statements and plaquette concentration improve with beta and cannot be that hypothesis alone.
The account gives upper bounds on the running inverse coupling only while it is at least 1/gamma^2.
Neutral form: NOT proved here. Row 1143 (10) rules out the periodic seed for n^2 = o(beta) "even if there
is a positive gap inside the neutral sector" (its Section 5, last line). For the neutral test at a fixed
lattice the file has the belief I33 only (neutral gap times side of order beta^(-1/3)). I tried the thin
trial vector F = P_1^2 - <P_1^2>, P_1 a straight Polyakov line, with row 1143's ribbon bound
<|P_1(1) - P_1(0)|^2> <= 2 K n/beta. It FAILS: in the cube vacuum the holonomy radius is of order
beta^(-1/3) (I33), so the variance of P_1^2 is of order beta^(-4/3), and the quotient grows like
n beta^(1/3). The ribbon bound is dominated by the ultraviolet noise of the thin line, not by the constant
mode. A proof needs a line averaged over the transverse positions and a lower bound on the variance of
its square in the vacuum. That is open, and I did not attempt it: the filter (t4) below uses the periodic
form, and for the neutral test it is at belief grade.

**Blind candidates of this session that are on file (so that the next row does not redo them).**

| What I derived before reading | On file at | Standing there |
|---|---|---|
| The seed as a curve in the (log n, beta) plane; a carry with slack in the exponent suffices | row 1332 Theorem T, (A2) and (A3); check 1335 | PROVED GIVEN (A1), (A2), (A3); (A2) OPEN |
| Transport of the thermal sum along beta at a fixed box, from a bound on the beta-derivative of each level (Hellmann-Feynman; the thermal trace anomaly) | (VIR_K) and Theorem TR, row 708 (`gap-mid-max.md` Section 4); (SUM-RULE); M-E of row 1380; row 998 item 16 | three ways failed; blocked-equivalent (registry RB) |
| Monotone doubling defect along the scale; a c-theorem on the torus | (MONO-Delta), `gap-phys-seed.md` L355; row 1143 (13) at fixed lattice | OPEN; false for the ordered Ising model as a class statement (`gap-phys-seed.md` L371-373) |
| Migdal-Kadanoff or hierarchical step as a template (the curvature gain of a convolution on S^3 times the classical factor 2^(d-4)) | Proposition G1 (row 1128); row 1025 (Tomboulis's line: Proposition BR, Lemma FAC, Proposition SIGN, Identity MOV) | bond moving has no sign on the twist quotient; the line reads the flux half only |
| A seed on a thin twisted torus and continuation in its width | `gap-ac-lat.md`; rows on twisted boxes (35 files) | Lemma FLOOR; I add in Section 4, test (t2), that the twisted thin gap is present in five dimensions too (ARGUED) |
| A consumer for a small mean one-link Fisher information of a blocked law | open item of row 1383; lead rule CL (Lemma AFF, Example PROD); Lemma PT | a one-sample mean is not sufficient without a uniqueness clause; see Remark FI in Section 4 |

- 07:12Z Section 3 written. Read rows 924, 925 ((UNIV-K)) and the RESULT of row 1025. Next: Section 4, the
  kind of new input, then the rows.

## 4. What kind of new input is needed

### 4.1 The exact place

Theorem T of row 1332 (HOLDS in check 1335) has three hypotheses beside one finite inequality: (A1) the
ultraviolet carry, (A2) the infrared carry, (A3) their rate fit. (A1) is on the side where the account's
tools work. (A2) is the band. The new input is an engine for (A2), or for a step of the same content in a
renormalized variable ((K-flow)). In one line:

  (STEP) for every coupling b at or above a window value b_w: a seed on the box of side N at the coupling b
  gives a seed on a box of side at most 2N at the coupling b + delta, with one delta > (log 2)/4.0 = 0.173.

The one-loop value is delta = (11/(3 pi^2)) log 2 = 0.2575 (GUIDE; the slack 4.0 against 2.69 is row 1332's
(A3) at one loop). (STEP) above the first-passage coupling follows from the seed (row 1332, consistency
remark), so there it is equivalent to the target and proposing it again is no progress. I do not propose it.
I use it to say what an engine must deliver.

### 4.2 Remark PAIR: apply the five-dimensional test to the step, not to each fact (ARGUED; the reading is row 1128's)

Row 1382 asked each selective fact to see the dimension, and found none (check 1384 found F2). A mechanism
need not contain such a fact. Asymptotic freedom itself is a pair:

- a gain per scale that reads the group and not the dimension (for example Proposition G1 of row 1128,
  Claude Fable: the stiffness of the convolution of two class weights on S^3 is s/2 minus a constant, of
  which Ricci/12 = 1/6 is curvature and vanishes on the circle; row 1128 3.2 already reads it as "stay,
  minus a constant per doubling" in the marginal dimension; for the Wilson profile part of the constant is
  group-blind, 3/8 against 1/8 on the circle);
- a carry between scales that reads the dimension and not the group: the classical factor 2^(d-4) on the
  inverse coupling (check 1384: "the classical constant-field twist scaling also sees the dimension and is
  shared by an abelian field").

Together: x(2L) = 2^(d-4) x(L) - g_G. In d = 4 the gains add up to a logarithm. In d = 5 the inverse coupling
doubles and no gain accumulates. For U(1) g_G = 0. So the pair passes both tests and neither member does.
The Migdal-Kadanoff recursion is this pair made exact on a hierarchical lattice. On the true lattice the
carry (bond moving) is not exact and has no sign on the quantities the chain reads (row 1025, Proposition
SIGN and Identity MOV). **So the missing object is the carry, not the gain.** The lane holds several proved
local gains (G1, NAB, FR, row 1141 (2), (8)) and one exact carry identity (Proposition LIFT of row 1383). It
holds no inequality that passes a local gain through an exact carry at a coupling of order one.

### 4.3 Requirements on an engine, each with its source

| # | Requirement | Source |
|---|---|---|
| (a) | Content at L > L_gamma for all late cutoffs: an all-coupling statement on bare lattices, or a step in a renormalized variable that starts from first-passage data | Proposition NEG (a); lead rule W2 |
| (b) | Uses d = 4 through the exact classical factor of a carry over all scales of the band, not through local counts | Remark PAIR; rows 1382, 1384 |
| (c) | Zero gain for compact U(1); fails at a named line for frozen Q_8 and 2T, for a product with a massless factor, for the adjoint Higgs, and at the K7 endpoint (the lane's belief-grade gapless comparison in the fundamental-adjoint family of SU(2) actions) | rows 1141, 1378, 1380; `parts/gap.md` L28-30 and its test table (L287) |
| (d) | Group test: the same statement makes sense, and is believed, for SU(3). It may not rest on dim G = 3 | Lemma GRP (new here) |
| (e) | Its hypothesis fails when beta grows at a fixed lattice: it contains an upper bound on an inverse coupling at the box scale | Remark STAB; row 1143 (10); Lemma FLOOR |
| (f) | Reads typical Wilson fields. No supremum over pins, tilts, coupling fields or backgrounds | rows 977, 996, 1011, 1014, 1139 |
| (g) | If it is an engine of the 2D kind: a family of moves with a spread of softness (Lemma H). Not lab-frame moves (Theorem C1). Not pin-measurable site frames (Theorem BD) | rows 1034, 1380, 1381 |
| (h) | Rate: a gain per doubling of at least 0.173 in beta, at every coupling of the band | row 1332 (A3), GUIDE |
| (i) | If it ends in a statement about a blocked law: a quasi-locality clause for the blocked specification, not only a mean | Remark FI below; lead rule CL; row 1332 Proposition CH |

**Remark FI (elementary; PROVED here by a three-line example, unchecked; of the kind of Example PROD of rule
CL and of the two-level models of row 1332).** "A small one-link Fisher information gives a seed" is false
in the class of gauge-invariant hypercubic families with a reflection-positive transfer matrix in every
direction, even with the supremum of the score in place of its mean. Example: Z(Lambda) = c_1^|Lambda|
Z_(beta_1)(Lambda) + c_2^|Lambda| Z_(beta_2)(Lambda), two Wilson SU(2) models at small couplings beta_1 not
equal to beta_2, with c_1, c_2 chosen so that the two bulk free energies agree. This is the gauge field with
one global label. Its transfer matrix in each direction is the direct sum of the two, so it is reflection
positive. Its law on a torus is a mixture with density f = sum of a_i exp(beta_i S). The score of a link is
sum of w_i(U) beta_i grad_l S with weights w_i in [0, 1] of sum 1, so its norm is at most 6 max(beta_1,
beta_2) at every configuration. The two top eigenvalues differ by a factor that tends to 1 as the box grows
(each model has a gap, so the finite-size corrections of its free energy are exponentially small). Both
block vacua are centre-neutral. So the neutral thermal sum at the test time tends to at least 1 and the
seed fails at every large size. Consequence for row 1383's
open item: a consumer for the level form of M-D must take a clause that excludes a global label, that is,
quasi-locality of the blocked specification. In Dobrushin's form that clause is a supremum over fields of
mixed second derivatives of the blocked action. The end-class form on file is row 1332 Proposition CH.

### 4.4 The three kinds of input that could meet (a) to (i), and my judgement

- **K-I, an exact positivity or monotonicity theorem for the carry.** A proof that an exact block step of
  ratio 2 moves a named typical-field stiffness by the classical factor at most, so that a proved local gain
  survives. It is the gauge analogue of the 2D bracket identity. Nothing on file or in the literature read
  (rows 1012, 1379) has this form. The nearest objects: Proposition LIFT with (BUB) (row 1383; the literal
  form is not selective, the level form has no statement for an averaging map); Tomboulis's bracket (row
  1025; no sign).
- **K-II, a rigorous renormalization step at an effective coupling of order one.** Balaban's method without
  a small coupling. This is the core of the open problem. No tool on file.
- **K-III, a verified computation.** Row 1326 (check 1331): no statement on file is both finite and
  sufficient, and the cost of the smallest instance is out of reach. It needs (A1) and (A2) first.

I found no candidate of kind K-I in this session. Every sufficient or step statement that I derived blind
is on file (table of Section 3). I judge the programme to have no first lemma to attack in the band.

### 4.5 Five cheap tests to run on any future candidate before a proof row (the filter)

- (t1) Compact U(1), d = 4, weak coupling: the gain must be zero at a named line.
- (t2) SU(2), d = 5, weak coupling, applied to the step (Remark PAIR). Example of a failure (ARGUED): a
  seed on a thin torus with a centre twist in its two short directions. The twist leaves no constant mode,
  so the lowest level is of order pi over the short side at tree level. The same holds on a twisted
  two-torus times R^3 in five dimensions. So the twisted gap is kinematic, and all selectivity would have
  to come from the continuation in the width, which is the band again.
- (t3) Group test, SU(3) (Lemma GRP).
- (t4) Remark STAB: let beta grow at a fixed lattice. If the hypothesis survives, the candidate is dead
  (PROVED GIVEN row 1143 (10) for the periodic test; belief grade for the neutral test).
- (t5) Equivalence (rule of 2026-11-22): above the first-passage coupling (STEP) is the target. A candidate
  must name the method that proves it, not the statement.

- 07:16Z Section 4 written. One error of mine found on re-reading and corrected in place: the neutral form of
  Remark STAB (the thin Polyakov-line trial vector fails; the text now records the failure). (R1) reworded to
  the periodic seed. Next: the rows, the report, the RESULT line.

## 5. What the programme does next, and the next two rows

**Recommendation to the lead (a judgement; the owner decides pace and priorities).**

1. Record the negative of Section 3 in `parts/gap.md`: no proved statement on file has content in the band
   for late cutoffs except lattice-local facts, identities and negatives; F2 is struck as a mechanism seed
   (Lemma GRP); (A) of row 1132 is a target.
2. Queue no further attack row on the band until a candidate passes the filter (t1) to (t5) of 4.5 and names
   its carry (requirement (b)). The reopen condition is an input of kind K-I or K-II of 4.4.
3. Put the freed capacity where the account's tools work and where the result is needed twice: the
   ultraviolet carry (A1) = (UNIV-K) in rate form. It is one of the three hypotheses of Theorem T, and it is
   also the uniqueness of the continuum limit at a fixed physical size, which the existence target does not
   yet have (T0 is stated along a sequence). Its open inputs are named on file: (MAPCONV), (VAC-ID),
   (DENS-K), (CLASS) (row 924, check 925).

**Row 1. `gap-mech-direction2-check-astra62` (cross-provider check; gpt-6.2-astra).**
Moves: the standing of the two survivors of check 1384 and the negative of Section 3.
Task: check this file. Test first, in this order: (i) Lemma GRP: the stratum count near a central tuple for
SU(3) in four dimensions, including the lower strata, and whether the convergence theorem of Austing and
Wheater gives order s^(-8) with no logarithm for the compact integral; (ii) Proposition NEG (a) and (b), item
by item against check 1384; (iii) Remark FI (the two-coupling mixture: reflection positivity, the score
bound, the near-degenerate top eigenvalues); (iv) Remark PAIR against rows 1128 and 1025; (v) the
non-equivalence and the tests of (SV-Z); (vi) the periodic form of Remark STAB.
Decisive outcome: F2 is struck as a mechanism seed and the negative stands with its class; or the first
failing line names a proved statement with content in the band, which then gets the next proof row.

**Row 2. `gap-univk-rate-fable` (direction and first proofs on (A1); Claude Fable 5.2 high, then medium).**
Moves: hypothesis (A1) of Theorem T (row 1332), and the uniqueness of the continuum limit at a fixed
physical size.
Start from: rows 924 and 925 ((UNIV-K) holds exactly when the changes of Phi between a datum and its
predecessor are summable; regular part at most C ell^4 q^K GIVEN (MAPCONV), (CLASS) and matched endpoints;
vacuum part GIVEN (VAC-ID)); row 1332 4.4 (the rate form that Theorem T reads); the account's linear system
and vacuum criterion at the lines row 924 cites.
Task: decide which of (MAPCONV), (VAC-ID), (DENS-K), (CLASS) the account proves, sketches or assumes (rules
9 and 10: quote the passages), and prove the first one that it does not prove. State the rate form with the
dependence on ell written out.
Decisive outcome: (A1) in rate form as an implication from statements the account proves, which closes one
of the three hypotheses of Theorem T; or the first input that fails, with the explicit failure. In the
second case Theorem T has two open hypotheses that no tool on file reaches, and the lead can tell the owner
that the gap chain is parked on both sides.

**Not queued, with the reason.**
- A port of (SV-Z): no consumer (Section 2.1).
- A proof row on (STEP), (A2), (VIR_K) or the level form of (BUB): no engine; (STEP) above first passage is
  the target (rule Equivalent is not progress).
- A sweep of the selective facts against the group test: useful only if an attack on the band is queued.
- The neutral form of Remark STAB: a fixed-lattice fact with no consumer beyond the filter.

## 6. Report

**Kind of result.** A direction row with a negative verdict. No step of the gap chain is proved. Nothing
here is checked by another model. No numeric run was made (none was needed; no lock was taken).

**Verdicts.**
- Facts on file that carry to a statement uniform in n at a physical side L: only the pair F1 with F2, as
  the small-volume statement (SV-Z), at L <= L_gamma. It is selective, not equivalent to the seed, and on the
  side where there is no seed. Not picked.
- F2 (row 1143 (2), (6)), the five-dimensional survivor of check 1384: fails the group test. Its logarithm
  is the coincidence 4 = 2N/(N - 1) at N = 2 (Lemma GRP).
- F3 (row 1132): the margin is one number of the group; (A) is a target of seed strength.
- No route on file reaches (M-neutral) (Proposition NEG, with its class and its premise (P5)).
- The missing object is an exact carry with a sign at a coupling of order one, not a local gain (Remark
  PAIR). In the chain's terms it is (A2) of Theorem T.

**PROVED here (elementary, unchecked).** Remark FI: in the class of gauge-invariant hypercubic families with
reflection-positive transfer matrices, a uniformly small one-link score does not give a seed (two-coupling
mixture). The logic of Proposition NEG from its cited inputs.

**ARGUED here.** Lemma GRP's stratum count for SU(N) (its consequence for SU(3) in four dimensions rests on
the published convergence theorem); the derivation sketch of (SV-Z) and its tests; Remark PAIR; test (t2) on
twisted thin tori; the width of the band at one loop.

**Failed here.** A variational proof that the neutral seed fails at a fixed lattice as beta grows (thin
Polyakov line; Remark STAB).

**Equivalence rule.** I propose no sufficient condition. (STEP) is written only to state what an engine must
deliver, and Section 4.1 says where it is the target.

**Not done.** `gap-short-step-variance-fable.md`, `gap-selective-5d-sweep-opus.md`,
`gap-mech-direction-check-astra62.md` and `prior/gap-mech-lit-luna.md` were read in their RESULT lines only.
Rows 708, 709, 1025, 1128 and `gap-ac-lat.md` were read in RESULT lines or by grep only. The cross-branch
search was not repeated (rows 1379 and 1384 ran it for this programme). The Austing-Wheater and
Krauth-Staudacher papers were read in their abstracts only. Check 1385 of row 1383 was running; I did not
wait for it.

**Credits.** Balaban; Sussman and Alpoge with Claude and Codex (the account; first-passage data; the flow).
Luscher; Koller and van Baal (small volume, as recalled on file). Krauth and Staudacher; Austing and Wheater
(the convergence threshold of the matrix integrals). OpenAI; Ding, Huang and Yang (the 2D proofs). Tomboulis;
Ito; Migdal and Kadanoff (as on file in row 1025). The lane's rows, by gpt-6.2-astra, Claude Fable, Claude
Opus and gpt-6-luna, named at each use: 708, 924, 925, 978, 988, 998, 1011, 1025, 1128, 1132, 1135, 1141,
1143, 1144, 1326, 1331, 1332, 1335, 1342, 1349, 1356, 1359, 1367, 1379 to 1385.

- 07:17Z Sections 5 and 6 written; citations re-read against the rows (three wording corrections: (NOCRIT)
  rows, the range of (A), the credit of Remark PAIR to row 1128). RESULT written.

RESULT: Row 1386 (Claude Fable 5.2 high, Mac mini worker 1; author, checked by no one; no numeric run, no subagents). Direction row with a negative verdict: no route on file reaches (M-neutral). Inventory (Section 2): the only statement that carries to a form uniform in n at a physical side L is the pair of the account's one-loop step with row 1143's toron integral, as the small-volume statement (SV-Z) at L at most L_gamma; it is selective and not equivalent to the seed, but it lies where no seed exists and is a start value, not a step; not picked. Lemma GRP (count ARGUED; threshold is Austing and Wheater's theorem, abstract read): the borderline logarithm of row 1143, the five-dimensional survivor of check 1384, occurs at D = 2N/(N - 1), that is at D = 4 for SU(2) only; four-dimensional SU(3) has none and behaves there as five-dimensional SU(2); so the survivor fails a group test and is struck as a mechanism seed. Statement (A) of row 1132 is a target of seed strength, proved uniformly in the box only at beta at most 1/48. Proposition NEG (elementary logic from cited rows, under the belief-grade premise that five-dimensional SU(2) has no seed at weak coupling): every proved statement on file with content in the band at late cutoffs is lattice-local, an identity or a negative, and holds in five dimensions, so no conjunction of them by dimension-blind inference gives the seed; the proved cover of the band is Lemma CLIMB's 1e-12 in beta against at least 9 doublings at one loop (GUIDE). PROVED here, unchecked: Remark FI (a uniformly small one-link score does not give a seed in the class of reflection-positive gauge-invariant hypercubic families: two-coupling mixture), so a consumer of the level form of (BUB) needs a quasi-locality clause. ARGUED: Remark PAIR (credited to row 1128: a mechanism is a group-reading local gain times a dimension-reading exact carry; the lane has gains and lacks a carry with a sign at a coupling of order one), the requirements (a) to (i) and the filter (t1) to (t5) for any future candidate, including the new group test and the growing-beta test. FAILED here: a variational proof that the neutral seed fails at a fixed lattice as beta grows (thin Polyakov line). New input needed: an exact carry with a sign for a typical-field stiffness (kind K-I), or a renormalization step at an effective coupling of order one (K-II); in the chain's terms an engine for (A2) of Theorem T (row 1332); none found, and every sufficient or step statement that I derived blind in this session is on file (table of Section 3). Next rows proposed: the cross-check of this file (Lemma GRP first); a row on the ultraviolet carry (A1) = (UNIV-K) in rate form, where the account's tools work, with no further attack row on the band until a candidate passes the filter. OPEN: (M-neutral), the seed, (A1), (A2), the carry, the neutral form of Remark STAB, the premise on five dimensions, the mass gap.
