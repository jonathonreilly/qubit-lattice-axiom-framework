lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T22:16Z

# gap-mini-solve-ac-opus (FINISH row 1249)

Started 2026-11-20T10:16Z (date -u) at commit 418290682 on branch
claude/ym4d-hard-route. Model: Claude Opus 5.5, max reasoning, Mac mini
Claude worker 3. No subagents.

Task (row 1249): prove that four-dimensional SU(2) Yang-Mills theory has a
mass gap in the sense of Jaffe and Witten. First consider how best to attack
it, then do it. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Reading (in progress)

Reading FINISH.md, GOAL.md, parts/gap.md, library/open-core.md and
library/prior/gap-onebound-read-sol.md before choosing an attack.

Reading done 2026-11-20T10:25Z (date -u). Read: GOAL.md in full; FINISH.md L1-84 and L299-356 (rules,
joining, efficiency), queue row 1249 in full; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `library/prior/gap-lit-refresh-2026-11-20-luna.md` (row 1216) L1-40; the screening tables of
rows 1189 (`gap-mini-solve-b-fable.md` 2.1), 1194 (`gap-mini-solve-e-fable.md` 2.1, Step 3) and 1199
(`gap-mini-solve-i-fable.md` 1.2); the RESULT lines of rows 1219-1256 that exist at this pin; the opening of the
sibling row 1255 (`gap-mini-solve-ae-opus.md`, running, no attack chosen yet at this pin).

**What the record fixes (cited; not re-derived; statements about the record, not evidence).**
- The gap clause on the account's tr F^2 sector reads one open lattice estimate beside the account's premises:
  (N-phys) (row 1161 L146-148; row 1179 Theorem BP, check 1183; row 1225 Theorem E-N). In row 1218's notation:
  there are L and j_0 such that for every j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
  s_(+,j)(u_j; n_j^3) = Tr_(H_(+,j)) U_j^(u_j) - 1 <= 1/2.
- Row 1180: (N-phys) holds iff every fine coupling has a finite one-cube seed and limsup a_j nu(beta_j) is finite;
  row 1233 pays the second half from the account's two-cutoff comparison, given its inputs. Row 1225: modulo the
  ultraviolet carry (UNIV-K), the crux is a lattice gap of SU(2) Wilson at one fixed coupling with a seed.
- About 45 route families are on file with a first failing step (tables of rows 1189, 1190, 1194, 1199;
  `parts/gap.md` methods 19-36; route registry RA-RG). The published inputs of row 1218 are used up:
  A's seed (A-B*) asks for the same dilute glueball gas as (N-phys) (row 1219 GUIDE); A's slab route is blocked
  by a boundary-condition construction (row 1224, ARGUED along the tuning); B's Corollary 166 holds for Villain
  U(1) too, so it is not selective (row 1220 Proposition U); Zeng's (TUN) is the gap (row 1251).
- Jensen-type one-step bounds see screening in 4D (row 1244); a selective step needs an identity that fixes the
  sign of the non-abelian correction at order-one coupling, and none is on file (row 1243).

## Step 1. How best to attack it (judgement; ARGUED unless marked; written 2026-11-20 about 11:05Z by date -u)

**1.1 What a proof has to contain (ARGUED; each piece is on file).**
1. Existence (T0) is the account's chain with its premises; this row does not touch it.
2. The gap clause reads one lattice estimate, (N-phys). Modulo the ultraviolet carry (UNIV-K), it is a seed at one
   fixed weak coupling beta_0: a periodic cube of side nu(beta_0) whose neutral excited trace at time nu/K is at most
   1/2 (rows 1180, 1225). By the carry's structure the cube is far larger than the lattice correlation length, so the
   seed already contains the whole band (the scales where the running coupling is of order one). There is no
   shortcut through strong coupling: the carry compares consecutive cutoffs only where the cutoff scale is
   perturbative (row 1225; `gap-chain-ce-opus.md` Step 7).
3. So a proof must cross the band inside one lattice model at one coupling. In 4D it must read the gauge group
   (compact U(1) is gapless), the dimension (d = 5 test, K7) and the typical fields (Theorem D2, Lemma SHEET:
   worst cases over pins, tilts or coupling fields are false). Asymptotic freedom is the only selective fact that is
   provable today, and it is perturbative.

**1.2 The three shapes, and the one I take.** (K-one): a property of the measure at one scale with a number in it;
with no computed certificate allowed, a hand proof at u = I_2/I_1 of about 0.48 is out of reach (the hand edge is
about 0.045, row 1229). (K-flow): a scale step carried through the band; the 2D engine of OpenAI's O(3) paper is the
only example, and its gain is a variance lower bound through the bracket (row 1016 (N3)). Rows 1243-1244 put the 4D
step at one statement: the stiffness split H_c = D_V - Var(Psi_V) of row 1018 Lemma FLOW, where every explicit
extension V of a boundary move has a bulk Psi_V (row 1243 3.2), and a Jensen bound (drop Var) with any bounded
linear flow sees screening at one loop (row 1244, ARGUED). Row 1243 stops at (S-V): "the bulk cost must be recovered
from Var(Psi_V), which an explicit V does not control".

**Choice.** I attack exactly that point: a lower bound on Var(Psi_V) by explicit objects. Plan:
- Step 2. Lemma TF (two flows): for every interior flow W, Var(Psi_V) >= (E[W Psi_V])^2 / E[-W Psi_W], all terms
  expectations of explicit local functions under the pinned measure, with equality in the supremum over W. So
  H_c <= D_V - sup_W (E[W Psi_V])^2 / E[-W Psi_W] (an upper bound on the stiffness with no dropped term).
- Step 3. One-loop test in the Gaussian model of row 1244: does a bilinear W recover the spin bubble that every
  linear flow loses (row 1244 Proposition 2.3)? If yes, row 1244's obstruction is a property of Jensen bounds, not of
  the step.
- Step 4. The band: the statement (S-VW) that remains, three distinct ways at it (perturbative control, exact
  Schwinger-Dyson identities, convexity in the coupling), each to its first failing step; compact U(1) control.
- Step 5. Result.
Grep before the attack (rule 0a): "Psi_W", "second flow", "two flows", "W(Psi", "trial current", "Bogoliubov" give
no two-flow bound on file; `gap-boundary-q.md` L43 uses Cov(Psi_theta, Psi_(d lambda)) for two boundary moves (row
1036), and method 31 (averaged curvature, `gap-avgcurv-max.md`) uses the Bochner form of E[Psi^2]. I credit both and
claim nothing new until Step 2 is written against them.

## Step 2. The planned two-flow lemma is on file (written 11:15Z by date -u)

Grep after Step 1 (rule 0a), `gap-direction3-max.md` (row 1051) L504: "H_c = inf over flows of Q_V (Lemma FLOW;
Theorem EXT of row 1046)". My planned Lemma TF is that statement in another form, so I withdraw it as a new item.
The reduction, written so a reader can check it (PROVED, elementary; it uses only Lemma FLOW of row 1018 and that
Psi_V is linear in V): for an interior flow W the extension V + tW moves the same boundary data, so by Lemma FLOW
H_c = Q_(V+tW) - Var(Psi_V + t Psi_W) for every t, and Q_(V+tW) = H_c + Var(Psi_V + t Psi_W). Minimising over t
gives Q_(V + t_* W) = H_c + Var(Psi_V) - Cov(Psi_V, Psi_W)^2 / Var(Psi_W), which is the two-flow bound. So the
two-flow bound is the Jensen bound of the improved flow V + t_* W; Theorem EXT of row 1046 (infimum over flows is
exact) covers its exactness. Integration by parts, E[W f] = -E[f Psi_W] for interior W, writes the covariance as
-E[W(Psi_V)]; this is the form `gap-boundary-q.md` L43 already uses (row 1036). Nothing new here.

Consequence for the plan. Row 1244's obstruction is stated for linear flows; a flow that is quadratic in the
fluctuations is the flow V + t_* W with W bilinear, so "a 4D step must carry an RG step's fluctuation response"
(row 1244 Step 3) already says what Step 3 of my plan would show at the Gaussian level. Step 3 is dropped as a
repetition. What stays open is (S-V) as row 1243 states it.
