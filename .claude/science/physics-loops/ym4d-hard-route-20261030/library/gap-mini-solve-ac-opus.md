lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T22:16Z

# gap-mini-solve-ac-opus (FINISH row 1249)

Started 2026-11-20T10:16Z (date -u) at commit 418290682 on branch
claude/ym4d-hard-route. Model: Claude Opus 5.5, max reasoning, Mac mini
Claude worker 3. No subagents.

Task (row 1249): prove that four-dimensional SU(2) Yang-Mills theory has a
mass gap in the sense of Jaffe and Witten. First consider how best to attack
it, then do it. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Reading (done 10:25Z by date -u)

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

## Step 1. How best to attack it (judgement; ARGUED unless marked; written 2026-11-20T10:51Z by date -u)

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

## Step 2. The planned two-flow lemma is on file (written 10:56Z by date -u)

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

## Step 3. The last named candidate: the covariant Green's-function flow (written 11:00Z by date -u)

**3.0 The item.** Row 1244 3.1 item 4 names one flow it did not attack: "a covariant flow of the form 'covariant
Green's function applied to the spin coupling of the actual field' is defined on every configuration at every
coupling. Whether its direct term can be bounded at the band is (S-V) in a sharper form ... OPEN, and no claim that
it works." It is the 4D analogue of the Gaussian minimiser K_* = -(1/2) G M_1 of row 1244 Lemma 2.1, with the free
G replaced by G_U = (D_U^* D_U)^(-1), the inverse of the Dirichlet adjoint covariant Laplacian of the cell in the
actual field U. Grep: "covariant Green" occurs only in row 1244; "Combes-Thomas" occurs in row 1237 (Proposition
UNI, for a heat-bath generator), not for D_U^* D_U. I take this flow and ask how far its kernel reaches.

**3.1 Lemma CT (Combes-Thomas for a connection Laplacian; PROVED by hand; the method is Combes and Thomas, 1973,
RECALLED and rebuilt here).** Let X be a finite set of sites, each edge xy of a graph on X carrying an orthogonal
(or unitary) map U_xy with U_yx = U_xy^(-1), fibres R^k (or C^k), at most Delta edges at each site. Let H = B + W on
functions psi: X -> R^k, where (B psi)(x) = sum over edges xy of (psi(x) - U_xy psi(y)) plus any Dirichlet terms
c_x psi(x) with c_x >= 0 for edges to pinned sites, and W >= 0 is a multiplication operator. Assume H >= eps > 0.
Let d be the graph distance. If mu in (0, 1] satisfies 0.78 Delta mu^2 <= eps/2, then for all x, y

    || G(x, y) || <= (2/eps) exp(- mu d(x, y)),     G = H^(-1).

Proof. Fix y and put phi(x) = mu d(x, y), so |phi(x) - phi(x')| <= mu on every edge. Let H_phi = e^phi H e^(-phi)
(conjugation by the multiplication operator). Diagonal entries are unchanged and the edge entry -U_xy becomes
-e^(phi(x) - phi(x')) U_xx'. Since U_x'x^* = U_xx', the Hermitian part (H_phi + H_phi^*)/2 has edge entries
-cosh(phi(x) - phi(x')) U_xx', so (H_phi + H_phi^*)/2 = H - T, with T(x, x') = (cosh(phi(x) - phi(x')) - 1) U_xx' on
edges and T = 0 elsewhere. Each row and each column of T has at most Delta entries of norm at most cosh(mu) - 1
<= 0.78 mu^2 (mu <= 1, cosh(1) < 1.55, cosh(t) - 1 <= t^2 cosh(t)/2). By the Schur test ||T|| <= 0.78 Delta mu^2 <= eps/2,
so the Hermitian part of H_phi is at least eps/2. For every psi, ||H_phi psi|| ||psi|| >= Re <psi, H_phi psi> >= (eps/2)
||psi||^2, so the finite matrix H_phi is invertible with ||H_phi^(-1)|| <= 2/eps. Since H_phi^(-1) = e^phi G e^(-phi), its
(x, y) block is e^(phi(x) - phi(y)) G(x, y) = e^(mu d(x, y)) G(x, y), of norm at most 2/eps. QED

**3.2 Corollary CT-FR (PROVED given Lemma FR+ of row 1018 4.3, which is PROVED there).** For a pinned cell of the
4D lattice (Delta = 8) and any configuration U, let lambda_* := min over interior sites of lambda_x(U)/6, with lambda_x
as in Lemma FR+. If lambda_* > 0, the adjoint covariant Green's function satisfies
||G_U(x, y)|| <= (2/lambda_*) exp(- mu d(x, y)) with mu = min(1, (lambda_*/12.5)^(1/2)).
Proof. Lemma FR+ gives D_U^* D_U >= (1/6) lambda_x as forms ("the adjoint covariant Laplacian of a configuration is
bounded below by lambda_x/6 as a multiplication operator"), so H = D_U^* D_U >= lambda_*. Apply Lemma CT with
eps = lambda_*, Delta = 8: 0.78 * 8 * mu^2 <= lambda_*/2 holds for mu^2 <= lambda_*/12.48. QED

So the covariant Green's-function flow V_U = -(1/2) G_U M_U (row 1244 3.1 item 4, M_U the spin coupling of the actual
field) has a kernel of range at most 1/mu, and on such a configuration its strength is bounded independently of the
cell size: ||V_U|| <= ||M_U|| ||G_U|| <= ||M_U|| / lambda_*.

**3.3 Size on the trajectory (ARGUED from checked statements; the localisation step is not rebuilt).** On typical
bare fields at coupling b the frame defect is of order 1/b per site (row 1141 (8), checked by row 1142; Lemma FR,
FR+). Lemma CT needs a lower bound on the whole operator, not on every site; a lower bound lambda_x >= c/b on a set of
sites that meets every ball of a fixed radius gives H >= c'/b by the localisation argument for Laplacians with a
dense potential (rebuilt as Lemma LOC in 3.6; the probabilistic density input stays ARGUED). Granting that, mu is of
order b^(-1/2): **the bare
covariant Green's function of a typical field has range of order sqrt(b) lattice spacings.** The origin of the mass is
the white noise of the bare links (each transport deviates from any smooth frame by about b^(-1/2)); it is the same
quantity NA that makes frame moves cost (rows 1011, 1018, 1141). In perturbation theory this is the lattice tadpole
mass of D_U^* D_U, which the full Hessian cancels by gauge invariance; D_U^* D_U alone does not cancel it.

**3.4 Consequence for the candidate (ARGUED).**
1. Above the band, on bare links. By 3.2-3.3 the bare covariant Green flow is a flow of bounded strength in the
   sense of row 1244 Proposition 2.3 (operator norm of order ||M|| b, independent of the cell size). Row 1244 proves,
   in its Gaussian model, Proposition 2.3 (iii): every real flow K, translation-invariant or not, loses at least
   (V ||m_0||_F^2/(2048 pi^2))(log(eps L^2) - 1) of the spin bubble, eps = min(1, ||m_0||_F^2/(20480 pi^2 n ||K||_op^2)),
   whenever log(eps L^2) >= 2; only ||K||_op enters. So for cells of side L >> b ||M|| / ||m_0||_F
   the bare covariant Green flow drops the logarithm, and its Jensen bound sees screening, exactly like the bounded
   flows that row 1244 excludes. The transfer from row 1244's Gaussian model (free background) to the rough bare
   background is the ARGUED step.
2. The long-range object that would keep the logarithm is the inverse of the full fluctuation Hessian (where the
   tadpole mass cancels). At a typical configuration, which is not a critical point of the action, that Hessian is not
   positive, so its inverse defines no positive flow kernel; on smooth (blocked) fields it is positive and nearly
   free, and the flow is the fluctuation part of an RG step (row 1244 3.1 item 2). So the candidate, made to work,
   is an RG step on blocked variables: the account's control, which ends at first passage.
3. At the band (cells of side 1 to 2 at b = 2.3 to 2.6, row 1018 4.5) the range sqrt(b) is one to two lattice
   spacings, the flow is local, and its direct term against the abelian value is a comparison of local expectations
   with order-one constants: a (K-one) statement with a number in it, which no hand tool reaches (row 1229: u = 0.48
   against the hand edge 0.045).

**3.5 What this step adds and what it does not.** New, as far as the grep goes: Lemma CT for the connection
Laplacian with its explicit constants, and its combination with Lemma FR+ (Corollary CT-FR), which places row 1244's
last named candidate in the class row 1244 already excludes when it is built on bare links. Not shown: that typical
Wilson fields at coupling b have lambda_x >= c/b on an R_0-dense set (the probabilistic input of 3.3; Lemma LOC in
3.6 is the deterministic half); the transfer of Proposition 2.3 (iii) from row 1244's Gaussian model; that no other
non-bare flow does better at the band. The covariant Green flow on blocked links is the RG step, so (S-V) is again "an RG step through
the band", the wall of `parts/gap.md`.

**3.6 Addendum: Lemma LOC (a dense frame defect gives a spectral gap; PROVED by hand; elementary).** In the setting
of Corollary CT-FR, let kappa > 0, S = {x : lambda_x >= kappa} and suppose every interior site lies within graph distance R of
S along a path of interior sites. Then

    D_U^* D_U >= 1 / ( (2R + 1)^4 (12/kappa + 4R) ).

Proof. Write Q(v) = sum over links of |D_l v|^2. (a) Q(v) >= (1/6) sum over s in S of kappa |v_s|^2 (Lemma FR+).
(b) |a - O b| >= | |a| - |b| | for an orthogonal O, so Q(v) >= sum over links xy of (|v_x| - |v_y|)^2. For each site x
fix s(x) in S and a path gamma_x of at most R links from x to s(x). Then |v_x| <= |v_s(x)| + sum over links of gamma_x
of the jumps of |v|, so |v_x|^2 <= 2 |v_s(x)|^2 + 2R sum over gamma_x of (jump of |v|)^2. Sum over x. A site s is s(x) for
at most |B_R| <= (2R + 1)^4 sites x, and a link lies on gamma_x only if x is within distance R of its tail, so on at most
(2R + 1)^4 paths. Hence ||v||^2 <= 2 (2R + 1)^4 (6/kappa) Q(v) + 2R (2R + 1)^4 Q(v) <= (2R + 1)^4 (12/kappa + 4R) Q(v). QED

With Lemma CT this gives a kernel range of order (2R + 1)^2 (12/kappa + 4R)^(1/2) for the bare covariant Green flow on
every configuration whose frame defect lambda_x is at least kappa on an R-dense set. What stays ARGUED in 3.3 is only the
probabilistic input (typical bare fields at coupling b have lambda_x >= c/b on an R_0-dense set, R_0 fixed) and the
transfer of row 1244 Proposition 2.3 (iii) from its Gaussian model. Note: Proposition 2.3 (iii) needs only the operator
norm, ||V_U|| <= ||M_U||/(2 lambda_min(D_U^* D_U)); Lemma CT adds the range, which is what makes the flow local at the
band (3.4, item 3).

## Step 4. State at the end (written 11:03Z by date -u)

| Statement | Label | Where |
|---|---|---|
| Mass gap of 4D SU(2) Yang-Mills (Jaffe-Witten) | OPEN; not proved, nothing disproved | Steps 1-3 |
| (N-phys), the one open lattice input of the gap clause | OPEN | Step 0 (rows 1161, 1179, 1225) |
| How to attack: the seed contains the band; (K-one) needs a number, (K-flow) needs a selective step; (S-V) is the frontier | ARGUED (record) | Step 1 |
| Two-flow variance bound H_c <= Q_V - Cov(Psi_V, Psi_W)^2/Var(Psi_W) | PROVED, but it is Jensen with the flow V + t_* W, covered by Theorem EXT of row 1046; withdrawn as new | Step 2 |
| Lemma CT: Combes-Thomas for a connection Laplacian, ||G(x,y)|| <= (2/eps) e^(-mu d(x,y)), 0.78 Delta mu^2 <= eps/2 | PROVED by hand (method of Combes and Thomas), unchecked | 3.1 |
| Corollary CT-FR: with Lemma FR+ (row 1018), the adjoint covariant Green's function of any configuration with lambda_x >= 6 lambda_* everywhere has range <= (12.5/lambda_*)^(1/2) | PROVED given FR+, unchecked | 3.2 |
| Lemma LOC: a frame defect lambda_x >= kappa on an R-dense set gives D_U^* D_U >= 1/((2R+1)^4 (12/kappa + 4R)) | PROVED by hand, unchecked | 3.6 |
| The bare covariant Green flow of row 1244 3.1 item 4 is a bounded-strength flow of range about sqrt(b), so it drops the bubble's logarithm above the band (row 1244 Proposition 2.3 (iii)); made long-range it is an RG step on blocked links; at the band it is local and its comparison is a (K-one) number | ARGUED (probabilistic density input and the Gaussian-model transfer not proved) | 3.3-3.4 |
| (S-V) with any flow at the band | OPEN | 3.5 |

Stop rule (FINISH How we work, item 4): this row made two attempts at the frontier statement (S-V), the two-flow
bound (found on file) and the covariant Green flow (reduced to an RG step through the band, or to (K-one) at the band),
with no closure. A third way, an exact identity that fixes the sign at order-one coupling, is the one row 1243 2.2
screened against every identity on file. The row stops here.

Note for the lead (a recommendation, not a ruling). This row confirms row 1244 3.4: the last mechanism named on the
frontier reduces to an RG step on blocked variables through the band. A further plain-brief crux row is unlikely to
move (N-phys) unless it brings a named new mechanism that passes the tests of `parts/gap.md` (U(1), d = 5, products,
typical fields) before it is attacked.

What was read and limits. Read in full: the files and line ranges listed in Step 0, and `gap-direction3-max.md` L470-530,
`gap-short-step-max.md` L105-137 and L217-256, `gap-mini-solve-z-opus.md` L90-182, `gap-mini-solve-aa-opus.md` L150-200 and
L242-292, `gap-univk-opus.md` L372-420, `gap-crux-exercise3-max.md` L111-131 and L238-252. One arXiv API query (mass gap and
Yang-Mills, newest first) found nothing that is not on file (arXiv:2611.11534 is on file, row 825). No numeric run, no
subagent. Credit: Lemma FLOW, Lemma FR+ (row 1018), Proposition 2.3 and the covariant Green flow (row 1244), the (S-V)
reduction (row 1243), Theorem EXT (row 1046), the frame-defect size (row 1141, checked by row 1142); the Combes-Thomas
method (J. M. Combes and L. Thomas, 1973), RECALLED and rebuilt in 3.1.

RESULT: Row 1249 (Claude Opus 5.5 max, Mac mini worker 3, 10:16Z-11:05Z by date -u; author only, checked by no one; no numeric run, no subagent): the Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; (N-phys) stays OPEN. Attacked the frontier statement (S-V) of rows 1243-1244 two ways: the two-flow variance bound is Jensen with an improved flow and is covered by Theorem EXT of row 1046 (withdrawn as new); the last named candidate, row 1244's covariant Green's-function flow, is short-ranged on bare fields. PROVED by hand, unchecked: Lemma CT (Combes-Thomas for a connection Laplacian, explicit constants), Corollary CT-FR (with Lemma FR+ of row 1018: range at most (12.5/lambda_*)^(1/2)), Lemma LOC (a frame defect lambda_x >= kappa on an R-dense set gives the spectral gap 1/((2R+1)^4 (12/kappa + 4R))). ARGUED: on typical bare fields the flow has range about sqrt(b), so by row 1244 Proposition 2.3 (iii) it drops the spin bubble's logarithm above the band; made long-range it is an RG step on blocked links, and at the band it is local with a (K-one) comparison; so (S-V) is again an RG step through the band. OPEN: (S-V), (N-phys), the probabilistic density input of 3.3, the Jaffe-Witten gap. Output library/gap-mini-solve-ac-opus.md.
