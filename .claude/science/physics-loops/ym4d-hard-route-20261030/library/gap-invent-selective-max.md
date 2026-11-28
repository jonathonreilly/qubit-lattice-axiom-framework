lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T06:24Z

# gap-invent-selective-max (FINISH row 1013): invented selective mechanisms for 4D SU(2)

Working file of one worker session, pinned at commit d06a5b87b on `claude/ym4d-hard-route`. Research-stage working state. It grants no status and nothing here is a public claim. Marks used: PROVED (written argument, checkable by hand), ARGUED (argument with a named hole), OPEN, FAILS.

Status of this file: COMPLETE. Times by `date -u`: file created 2026-11-15T18:25Z, last section written 19:31Z; step times were not measured and none is given. Nothing in this file is checked by another model. Sections were appended step by step.

## Plan (eight steps, one per response; each appends its result before the next)

1. **Inputs.** Read `FINISH.md`, `GOAL.md`, `parts/gap.md`, the four prior reads named by the row (`library/prior/gap-o4-pinned-cell-read-opus.md`, `gap-o3-continuum-rg-read-opus.md`, `gap-2don-proofs-read-opus.md`, `gap-gauge-stiffness-read-opus.md`), `library/gap-crux-fp.md`; fetch the exercise skill at main commit 8b11ae2bb9. Write the kill sheet: the exact statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the U(1), Q_8, 2T, five-dimensional, instanton/refilling and four-test spec checks, each with its file and line.
2. **Discovery logic of the 2D proofs** (a reconstruction, not a fact about how they were found): a short list of design rules, each with the place in the papers that shows it; which choices were forced by "zero gain for the abelian model", which were free.
3. **Invention.** At least six candidate mechanisms for 4D lattice SU(2) that are not the direct port of row 1011, each with (a) monotone, (b) class and closure under conditioning, (c) selective identity, (d) dimension-4 input, (e) consumer.
4. **Kill fast.** Each candidate against the kill sheet; a candidate that renames the crux is a FAIL.
5. **Survivor 1:** first lemma, proof by hand or counterexample.
6. **Survivor 2** (if any): first lemma, proof by hand or counterexample.
7. **Novelty check** (the only literature step), ranking by (what it would change) / (cost to find out), and complete work-item briefs.
8. **Summary and the RESULT line.**

## Step log

Status block (kept current):

- Step 1 (inputs, kill sheet): done, Section 1.
- Step 2 (design rules R1-R10): done, Section 2.
- Step 3 (eight candidates C1-C8): done, Section 3.
- Step 4 (Lemmas WN, TWIST; Proposition LOC; kill table): done, Section 4. No candidate survives.
- Steps 5-6 (no survivor; Lemmas JEN, SLAB as constraints on the open door): done, Section 5.
- Step 7 (novelty, ranking, work items W1, W2): done, Section 7. A ninth candidate and the main conclusion: Section 6.
- Step 8 (report and RESULT): done, Section 8.

Progress marker 1a. Read in full: `GOAL.md`; `FINISH.md` L1-90, L299-356 and rows 998-1013 (L1077-1098); `parts/gap.md`; the four prior reads (rows 1007, 1009, 1010, 1012). Still to read in this step: the in-progress file of row 1011, `library/gap-crux-fp.md` (five-dimensional test, Proposition V), the statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the exercise skill, `library/open-core.md` (duplicate check).

## 1. Step 1 result: provenance, inputs, and the kill sheet

**Provenance.** Anthropic, Claude Fable 5.2, max effort, one session on Mac mini worker 2, no subagents. Nothing in this file is checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no computer-assisted step; proofs that could be formalized in Lean) replaces the framework refresher read of the exercise skill. The skill was fetched at main 8b11ae2bb9 with its one reference file `proof-search-governance.md` into `/tmp/row1013-skill/` and read in full. Its literature lens is not run (the row: rows 1007, 1009, 1010, 1012 are that lens).

**Credit.** The 2D mechanisms restated below are OpenAI's (author line "OpenAI"; posted, unrefereed; github.com/openai/math, commits adc7f1241b42 and 4eaee8754825) and Ding, Huang and Yang's (arXiv:2611.04908). The readings I start from are rows 1007, 1009, 1010, 1012 (Claude Opus 5.5, unchecked). Balaban's and Sussman-Alpoge's work is credited where it is used.

**Read in full:** `GOAL.md`; `FINISH.md` L1-90, L299-356, rows 998-1013; `parts/gap.md`; `library/prior/gap-2don-proofs-read-opus.md`, `gap-o4-pinned-cell-read-opus.md`, `gap-o3-continuum-rg-read-opus.md`, `gap-gauge-stiffness-read-opus.md`; the 82 lines of row 1011's file that exist at this pin (`library/gap-pinned-cell-gauge-max.md`: plan and input summary only, no result yet). **Read in part:** `library/gap-crux-exercise3-max.md` L690-722 (Lemma PT), `library/gap-crux-exercise4-max.md` L342-437 (Proposition NP), `library/gap-tiltproof-max.md` L202-262 (Theorem D2), `library/gap-sepinput-max.md` L300-404 (Lemma SHEET), `library/gap-crux-fp.md` L248-288 (the range form of the tests, the five-dimensional test), `library/gap-outside-box-max.md` L70-80 (row 1004's reading of the four-test spec check). **Not read:** the rest of the lane (about 800 library files); the primary 2D texts are opened in step 2 only where a design rule needs the exact place.

### 1.1 What the 2D solution is, in the lane's terms (from rows 1007, 1009, 1010; all OpenAI's mathematics, unchecked)

- The band is crossed at one fixed bare coupling b, by a mixing bound uniform over all bond strengths in [0, b] (O(3) paper Proposition 2.1; O(4) paper Theorem 3.1). No first-passage data, no (CAS).
- Its engine is a class statement: sup over all pinned squares of side R, all boundary pins, all strengths in [0, b] of the twist stiffness H is at most h. One step gives the same with h - delta at side l R, delta = (log l)/pi - C log B (S^3) or (log l)/(4 pi) - C log B (S^2). The gain is the bracket term of the rotation Ward identity and is zero for S^1.
- Small stiffness gives decay of charged observables (cheap local rotations, coarse orientations, disagreement percolation), then mixing of all observables by abelian conditional decompositions with association. The seed follows by the coupling integral d/dt Delta_t(n) = 8 n^2 [e_t(n) - e_t(2n)], which is the lane's Theorem D (f).
- The RG (exact, weak coupling only, contraction near L^(-2)) carries one box number to all finer cutoffs under an exponent condition. Transcribed to 4D by row 1010 (unchecked): mixing exponent below 3/2 times the one-loop exponent.

### 1.2 The kill sheet (each test with its exact form, source and what it binds)

| # | Test | Exact statement used here | Source (file:line) and standing | What a candidate must show |
|---|---|---|---|---|
| K1 | Lemma PT, Corollary PT1 | For a product model, D = D_1 + D_2, 1 + S = (1 + S_1)(1 + S_2), m = min(m_1, m_2); a seed of the product is a seed of each factor. Product with compact U(1) in its massless phase: no seed at any size. | `gap-crux-exercise3-max.md` L690-722; proved by hand, check 999 HOLDS (PT1 after correction: theorem-grade for Villain U(1) at beta at least 2^14) | Its conclusion step (monotone small implies gap of all observables) must read the whole state space; a gain that reads the SU(2) factor only is allowed, but then the last step must fail for the product. |
| K2 | Proposition NP | K copies of strong-coupling SU(2) times ordered Ising: D contracts by any theta on any J doublings, and the model has no seed. | `gap-crux-exercise4-max.md` L383-412; check 1006 HOLDS | Its induction must not read the model only through finitely many values of D. |
| K3 | Theorem D2 | SU(2) Wilson (also Q_8, 2T), even box: pinning the links of directions 2, 3 on one slice leaves an O(4)-symmetric two-dimensional sheet for the direction-1 links, with the infrared bound G-hat(p) at most 1/(2 beta E(p)); so every tilt-uniform covariance bound kbar is at least lam_* k00, lam_* at least 8.54 on side 4. | `gap-tiltproof-max.md` L240-246; proved given Lemmas RP, GD (rebuilt in row 1000) | No hypothesis that is a supremum over bulk tilts or over pins of interior link sets. |
| K3' | Slab device (mine, a corollary of the D2 construction; ARGUED, the infrared-bound theorem RECALLED) | Pin all links inside two parallel lattice hyperplanes at distance 1 to the identity. The free links between them, g(y) = U_4(y), carry exactly the three-dimensional O(4) spin model with weight exp(beta q.q'). For large beta it has long-range order (Frohlich, Simon and Spencer 1976, RECALLED). At distance R the cross-slab holonomy is a three-dimensional field with stiffness of order beta/R. | this file | A class closed under conditioning on link sets must not contain pinned hyperplanes closer than about beta; cubes with pinned boundary are allowed only if the step never produces thin cells. |
| K4 | Lemma SHEET, and its fixed-b form | All-fields form: with coupling B on the side plaquettes of a tube and 0 elsewhere, Cov(x_(p_i), x_(p_j)) tends to 1/4 as B grows; the supremum over coupling fields of lambda_max of the plaquette covariance is at least (n - 1)/4. Fixed-b form (to be checked per candidate): with strengths in [0, b] the class contains every lower-dimensional gauge system cut out of the lattice (tubes, thin slabs with free sides). | `gap-sepinput-max.md` L358-380; check 997 (same provider) | A class with strengths in [0, b] is allowed only if its claim holds for these cut-out systems at the same b. |
| K5 | Compact U(1) | Coulomb phase at weak coupling (Guth; Frohlich and Spencer; in the lane for Villain at beta at least 2^14). | `parts/gap.md` L195 | The gain must vanish identically for an abelian group. |
| K6 | Frozen Q_8, 2T | Finite non-abelian subgroups: no seed (T_per; T_ev in the frozen limit) at large coupling. | `parts/gap.md` L199; check 884 | The selective identity must use the Lie algebra (infinitesimal rotations, connectedness), not only that the group is non-commutative. |
| K7 | Five-dimensional test | SU(2) Wilson in five dimensions has massless gluons at weak coupling (GUIDE, numerics; transition near 1.6). A tool blind to the dimension stops below that coupling. | `gap-crux-fp.md` L88, L266, L283 | The dimension-4 input must be named, and the gain must fail in d = 5 (for example: the action of a scale-R wave grows like R in d = 5). |
| K8 | Instanton and refilling | Replacing a rough region by a small-curvature field that agrees with the exterior needs a small-curvature extension of boundary link data; the winding of the boundary data (pi_3(SU(2)) = Z) can obstruct it. | row 1010, `gap-o3-continuum-rg-read-opus.md` L136, L201 (RECALLED there, unchecked) | A candidate that fills or deforms fields must say what it does in a sector with winding. |
| K9 | Four-test spec check (row 1004's reading; the phrase is defined in no file) | A tool for T_W must use (S1) the non-abelian structure, (S2) a rate, (S3) the whole state space, (S4) typical fields; and (S0) a candidate that returns the crux under another name is a FAIL. | `gap-outside-box-max.md` L75 | One line per candidate for S0-S4. |

**Valid form of every test (exercise skill, step 6c).** A model M' refutes a candidate only if the candidate's hypothesis H holds in M' and its conclusion T fails there. Otherwise the test says what a proof of H must use. A pass is no support.

### 1.3 The consumers a candidate may feed (from `parts/gap.md` and rows 1009, 1010)

- (C-mix) the 4D analogue of Proposition 2.1: a mixing bound for Wilson SU(2) at every weak bare coupling, with an explicit length X(beta) whose exponent is below 3/2 times the one-loop exponent, uniform in plaquette strengths up to beta as far as Theorem D (f) needs it. With the carry of row 1010 6.5 (partly RECALLED, with the refilling obstruction K8) it gives the seed on the trajectory.
- (C-W) the wall (W) directly; (C-CAS) one contraction factor theta below 1 of the Casimir free energy on a bounded range of sizes; (C-seed) the periodic seed at one size.

## 2. Step 2 result: the discovery logic of the 2D proofs, as design rules

**This is a reconstruction from the texts' own structure. It is not a fact about how the proofs were found.** All mathematics restated is OpenAI's. Primary texts fetched into `/tmp/row1013-on`, `/tmp/row1013-o4`, `/tmp/row1013-o3` (not committed). Read here in the primary text: [B] "Exponential decay in two-dimensional classical O(n) models" pp. 1-12; [28] "Sharp mass bounds for the two-dimensional O(4) model" pp. 4-8. The rest is cited through rows 1007, 1009, 1010 with their line numbers. [15] = the O(3) continuum paper.

| # | Design rule (what the authors had to want) | Where the text shows it | Forced by "zero gain for the abelian model", or free |
|---|---|---|---|
| R1 | **One number at one scale.** Separate the large-distance argument from one finite-size test, and put all the work into making that test small. | [B] p. 2-3: "Such criteria separate the large-distance argument from the task of proving adequate decay at one finite scale". [28] p. 5: "Our lower-bound problem is now to make this one test small on a box whose physical size stays bounded". | Forced by the architecture, not by selectivity. Free: which test (annulus crossing in [B], torus defect Delta(n) in [28]). |
| R2 | **The small quantity is a twist cost with a trivial upper bound.** Choose a response of a partition function to a symmetry twist of the boundary data. It has the form "direct cost minus a variance", so dropping the variance bounds it by the coupling, in every model of the class. Only an upper bound is ever needed. | [B] p. 4 (2.6): R(h, h-bar) at most beta abs(h)^2; p. 9 (3.4): R_t(h, h) = -Z''(t)/Z(t); p. 8: "no positivity property of R is required". [28] p. 5: "direct quadratic cost minus current covariance ... No positive lower bound on the local stiffness is needed". | Forced in kind: a quantity with a blind a-priori upper bound and a selective improvement. Free: second derivative ([28] stiffness) or finite twist ratio ([B] Z(pi)/Z(0)). |
| R3 | **Gradient invariance.** The response depends on the twist field only modulo exact forms that vanish on the pins. All freedom is in the representative and in the test family. | [B] Lemma 2.1, last sentence (p. 4-5); (3.4) "the gauge changes the prescribed boundary values". | Forced: it is what lets a family supported away from the pins act on a boundary twist. |
| R4 | **The twist direction must be a commutator of trivial directions.** One-axis local rotations give only the blind bound, W(t (df) g) = 1. Two non-commuting axes give W(dF) = W(B) with B_e = (1/2)[F_x, F_y] + O(F^3): a field that looks like a gradient to first order is, to second order, a twist about the third axis. | [B] p. 5 (2.10)-(2.11), p. 6: "it is zero for two directions using the same generator". [28] (3.7)-(3.8): "a contact term and a bracket term ... For the same-axis score there is no bracket term" (row 1009 L86-89). [28] p. 23: "This is where the three-dimensional imaginary quaternion space is used" (row 1009 L131-132). | **Forced.** With one generator every identity is the abelian one. Also forced: order four (the commutator is second order, the response is quadratic in it), and two different spatial profiles per pair (S(f, f) = 0; [B] uses f and its complex conjugate). |
| R5 | **A sum-of-squares certificate with a coherent signal.** Sum the fourth-order identity over a family. The collective commutator field adds linearly (lambda_N of order log N); the cost adds only in Hilbert-Schmidt norm (order log N). So signal^2/cost is of order log N. Keep one non-negative square, bound every other term by the uniform coupling bound. | [B] Proposition 2.2 with (2.15), (2.20), p. 5-8; Lemma 3.2 (3.8), (3.10), (3.14) "Fourier orthogonality for the sharper bound" p. 10-11. [28] (3.50): Var J(A) at least (signal)^2/(cost) by Cauchy-Schwarz (row 1009 L139-141). | Forced in kind (a gain must beat a cost that grows with the family). Free: the family (plane waves on shells, weights r^(-3/2)), the square that is kept. |
| R6 | **The dimension enters as one harmonic sum.** Every scale between the lattice and the box contributes order one to the signal and order one to the cost. This needs a scale-invariant quadratic cost. In d = 2 it is the Dirichlet energy. | [B] p. 10: "The power r^(-3/2) is chosen to produce a harmonic sum". [28] p. 5: "The logarithm comes from a reciprocal-square frequency sum in two dimensions"; (3.37). | Forced by wanting a gain that grows without bound with the scale. |
| R7 | **A class defined by bounds, closed under every operation the proof performs.** All subgraphs, all strengths in [0, beta], all pins (in [28] also signs and right twists). Conditioning on a coordinate, on amplitudes or on cell rings, and integrating the coupling from 0 to beta, all stay in the class. The action is used only through uniform bounds on its derivatives. | [B] p. 2: "this uniformity permits the final conditional reduction without assumptions on the distribution of the projected couplings"; (2.2) abs(J_e) at most beta. [28] p. 16 and [15] p. 16: "the only conditioned cell laws are the original nearest-neighbor laws with new boundary pins, so the uniformity class is preserved" (row 1009 L153-157, L276-277). [15] p. 17: "No positive lower bound on any coupling entered" (row 1009 L293). | Forced by the consumers (conditioning, coupling integral), not by selectivity. This is the rule that the lane's Theorem D2 and Lemma SHEET threaten in the gauge setting. |
| R8 | **If one shot gives only 1/log, iterate on the class bound.** [B] stops at twist cost C/log N, enough for one crossing number. [28] makes the class supremum of the stiffness a monotone: exact Hessian identity for ring conditioning, Gaussian augmentation so that "at most h" becomes an exact variance identity, gain (log l)/pi per step. | [28] (3.16), (3.17)-(3.19), 3.8 (row 1009 L102-107, L145-152). | Free (a strengthening). The monotone is the class supremum, not the value in one model. |
| R9 | **A representation in which the twist cost is a probability or a coupling cost.** [B]: with both layers pinned, P(crossing) = 1 - Z(pi)/Z(0) exactly, for sign clusters. [28]: small stiffness makes local rotations cheap, then coarse orientations and disagreement percolation; then all observables through abelian conditional systems with association. | [B] p. 3 and (4.9) (row 1007 L136). [28] 3.9-3.11 (row 1009 L158-187). | Free and model-specific. This is the step that reads the whole state space (K1), and the step with no gauge counterpart on record. |
| R10 | **Never run the RG in the band.** The RG is exact, stays at weak coupling, and only carries the one number across cutoffs; the two halves meet in one exponent inequality. | [28] p. 7: "There is room to choose a box large enough for the first estimate and small enough for the second"; p. 8: "the blocking construction can stop at a large H". Row 1010 6.2. | Free. |

**The skeleton behind R2-R6, in one sentence (my abstraction, ARGUED).** There is a group of changes of variables under which a background-dependent partition function W is invariant; the twist is a class of backgrounds that the group cannot remove because of the pins; because the group is not abelian, the "linearised orbit" dF misses the true orbit by a second-order commutator field B(F), and the twist class is reachable, with a coefficient that grows like the number of scales, as a sum of such commutator fields; the cost of the trivial moves is bounded by the coupling alone. So a quantity that the trivial moves leave invariant at first order is bounded by a fourth-order variation along them.

**What this says an inventor needs in 4D (the three slots).** (i) A response quantity with a blind upper bound and gradient invariance (R2, R3). (ii) Two non-commuting families of trivial moves whose commutator is the twist, with a scale-invariant cost (R4-R6). (iii) A representation that turns a small response into decay of all observables (R9), inside a class that survives Theorem D2, the slab device and Lemma SHEET (R7). Row 1011 tests the choice (i) = Schrodinger-functional stiffness, (ii) = field-strength bracket of gauge waves. Step 3 fills the slots differently.

## 3. Step 3 result: eight candidate mechanisms for 4D lattice SU(2)

Notation. Links U_l in SU(2), plaquette weight exp(beta x_p), x_p = (1/2) tr U_p. A **link-end** is a pair (l, x) with x an end of l; a **corner** is a pair (p, x) with x a site of p. Lab frame = the frame in which the integration variables are written; no gauge is fixed unless said.

Not listed: the direct port (Schrodinger-functional stiffness, gauge waves on shells, field-strength bracket). That is row 1011.

Lane grep before writing (terms: white noise, corner twist, non-central, biharmonic, Golterman, diamagnetic, Kato, Zirnbauer, induced gauge, winding sector, frame field, commutator, Fradkin, covariant Laplacian, plaquette random-cluster; scope `library/`, `parts/`, `FINISH.md`). On file already: C4 (`gap-brainstorm2-max.md` L178, idea 28, row 859 family), C5 (`gap-brainstorm-max.md` L277, L523, L622, L688: "frustration bootstrap", with row 834's open nonlinear diamagnetic inequality), the bracket reading of asymptotic freedom (`gap-brainstorm-max.md` L303, Hormander and Solovay-Kitaev), the costly seam move (`gap-brainstorm2-max.md` L161, L216, ARGUED). No hit for: corner twist, biharmonic, frame field, Golterman. So C1, C2, C3, C7, C8 are "not found in the searched scope"; C4, C5, C6 are found again and credited.

**C1. Corner-twist family inequality (the port of [B], not of [28]).**
- Object. Left and right translations of single links, U_l -> e^(F_(l,x)) U_l e^(-F_(l,y)), F a field on link-ends with values in su(2). They are changes of Haar variables. They turn the action into a **corner-twisted action**: at each corner (p, x) a group element G_(p,x) is inserted between the two links of p at x. W(G) = E exp(beta sum_p [x_p(G) - x_p]) has the exact invariance W(G^F) = W(G). A gauge transformation is the case F_(l,x) = lambda_x for all link-ends at x.
- (a) Monotone: the response R(theta, theta) = -D^2 W for one-axis corner twists theta c; or the finite ratio Z(t)/Z(0). (b) Class: every finite subcomplex, strengths in [0, beta], any pinned link set; conditioning keeps it, as in [B]. (c) Identity: W(delta F) = W(B) with B_(p,x) = (1/2)[F_(l,x), F_(l',x)] + O(F^3), the bracket at the corner; [B] (2.10)-(2.15) should carry over (ARGUED, not written out; edges become corners, vertices become link-ends). (d) Dimension-4 input wanted: sum over modes of (signal)^2/(cost). (e) Consumer: the analogue of [B] Proposition 3.1, then Proposition 2.1.

**C2. Centre flux reached through non-central sheet twists.**
- Object. On a periodic box insert g in SU(2) at one corner of each plaquette of a co-closed sheet (all (1,2)-plaquettes at (x_1, x_2) = (0, 0)). Z(g) is a class function with Z(1) = Z and Z(-1) = Z_tw, the 't Hooft twisted partition function. So g_t = exp(t c), 0 <= t <= pi, is a continuous path between the two flux sectors, which [B] p. 12 would integrate.
- (a) Monotone: F(t) = -log Z(g_t)/Z(1). (b) Class: periodic boxes (reflection positive). (c) Identity: every element of SU(2) is a commutator, so for every t there are holonomies with [Omega_1, Omega_2] = g_t^(-1) and the classical cost of the twist is zero; in U(1) it is of order beta t^2. (d) The aspect ratio of the box is scale-free in d = 4. (e) Consumer: the flux half of the periodic seed (T_per), or Tomboulis-Yaffe.

**C3. Winding-sector twist.**
- Object. Dirichlet data on the boundary of a 4D cube, changed by a gauge map Omega of the boundary. Expectation before the test (from the continuum picture): the change is removable exactly when Omega extends to the cube with small action, that is when deg Omega = 0, so the bulk would feel the classes k in pi_3(SU(2)) = Z. The test (Lemma TWIST, 4.2) shows that on the lattice this expectation is false: every Omega extends.
- (a) Monotone: Z_k/Z_0. (b) Class: all Dirichlet cubes; conditioning on cell boundaries keeps it and the degree is additive. (c) Identity: pi_3(SU(2)) = Z; none for U(1) or a finite group. (d) The instanton action is scale-free in d = 4. (e) Consumer: none found; possible use in the refilling step (K8).

**C4. Third copy through an auxiliary-boson representation (found again: row 859 family, `gap-brainstorm2-max.md` L178).**
- Object. Weights of Budczies-Zirnbauer type, det(m - U_p)^(-2 N_b), are Gaussian integrals over bosons on corners; the links enter linearly, so they are independent given the bosons, and the N_b flavours are exchangeable. This is the nearest gauge object to the exchangeable copies of Ding, Huang and Yang.
- (a) Monotone: a crossing probability of flavour clusters. (b) Class: local-time conditions on corners. (c) Identity: moving crossing objects into a spare copy. (d) None. (e) Consumer: none for the Wilson weight.

**C5. Diamagnetic gap of a direction layer (found again: "frustration bootstrap", `gap-brainstorm-max.md` L277; row 834).**
- Object. Given all links of directions 1, 2, 3, the links of direction 4 are independent from layer to layer, and one layer is a three-dimensional O(4) model g(x) with bond energy beta Re (1/2) tr(A_mu(x) g(x+mu) B_mu(x)^(-1) g(x)^(-1)), A and B the two slices (Lemma LAYER). Its fluctuation operator at a maximiser is beta times the adjoint covariant Laplacian of the slice.
- (a) Monotone: the conditional Poincare constant of the layer. (b) No class supremum: the comparison with the flat Laplacian is pointwise in the background (Kato), so Theorem D2 and Lemma SHEET do not bind its form. (c) Identity: the adjoint hopping operator has norm below its flat value by the local non-parallelism of the colour-magnetic fields (a bracket [F_p, F_p'] not zero); the gain is zero for an abelian group. (d) None. (e) Consumer: a two-level (direction blocks, then links) Poincare inequality.

**C6. Centre clusters (found again in kind: `prior/gap-lit-flux.md`, `gap-brainstorm-max.md` on the plaquette random-cluster model).**
- Object. U_l = sigma_l V_l with sigma_l = +-1. Given the SO(3) field, the signs are a Z_2 gauge theory with couplings (beta/2) abs(tr V_p), the gauge analogue of the embedded Ising signs of [B] Section 4. (a) Monotone: the probability that an open plaquette cluster spans a loop. (b) Class: coupling fields in [0, beta]. (c) Identity: Ginibre and the plaquette random-cluster representation. (d) None. (e) Consumer: R9 for centre-odd observables.

**C7. Biharmonic frame field (a soft covariant gauge kernel).**
- Object. Insert 1 = int d Omega rho_alpha(Omega given U), rho_alpha = exp(-(1/alpha) G(U^Omega))/N_alpha(U), G(V) = sum_x abs((div A(V))(x))^2, A(V)_l the su(2) part of V_l. This is an exact probability kernel, as the observation kernel of [15] (3.3) is. The dressed links V = U^Omega carry an honest global colour symmetry V -> k^(-1) V k. Its local version leaves the action and N_alpha unchanged and costs only through G: (1/alpha) times a covariant biharmonic form of k.
- (a) Monotone: the twist stiffness of global colour, at most 1/alpha times a scale-free form. (b) Class: every background U and every pin; the frame is an O(4) field with fixed right twists, which is inside the class of [28] Section 3.1. (c) Identity: the bracket of global colour rotations; [B] Proposition 2.2 holds word for word, conditionally on U. (d) **The divergence-squared functional is scale-free in d = 4: its mode sum is sum abs(k)^(-4), a logarithm.** This is the 2D harmonic sum of R6 in four dimensions; it holds for smooth dressed links only (see the kill table). (e) Consumer: to be found.

**C8. Tree-transported translations (covariant moves with Jacobian one).**
- Object. Fix a rooted spanning tree and an order of the links in which each tree path gamma_l comes before l. The map U_l -> exp(f_l Ad(U_(gamma_l)) c) U_l is triangular, so it keeps the Haar measure although it depends on the field (the argument of Lemma SHEET). It translates each link along a colour axis carried from the root by the field itself.
- (a) Monotone: a Schrodinger-functional response, but with exact covariant Ward identities and no gauge fixing. (b) Class: Dirichlet cells with a radial tree. (c) Identity: the bracket of two transported axes. (d) Scale invariance of the Yang-Mills action. (e) Consumer: Proposition 2.1 analogue.

## 4. Step 4 result: three exact lemmas, then the kill table

All statements here are written by Claude Fable 5.2 and checked by no one. No numeric run was made.

### 4.1 Lemma WN: lab-frame translations are white noise on corners (PROVED by hand)

**Setting.** A finite cell complex in Z^4 or a torus with all sides at least 3. Some links may be pinned; the others carry Haar measure. Weight exp(H), H = sum_p beta_p x_p, strengths beta_p >= 0 arbitrary. A site is **free** if no link at it is pinned. Fix c in su(2) with c^2 = -1 (c = i sigma_3). Write U = x + i y.sigma, so (1/2) tr(c U) = -y_3 and (1/2) tr(c^2 U) = -x. Let F be a real field on link-ends that vanishes on the ends of pinned links, and tau_t the map U_l -> e^(t F_(l,x) c) U_l e^(-t F_(l,y) c) for l from x to y. For a plaquette p with a fixed orientation and a site x of p put theta_(p,x) = F_(l',x) - F_(l,x), where p arrives at x by l and leaves by l'. Put X(F) = d/dt (H o tau_t) at t = 0.

**Statement.** (i) x_p o tau_t = (1/2) tr(prod_(i=1..4) e^(t theta_i c) V_i), with V_1, ..., V_4 the link factors of p in order and theta_i = theta_(p,x_i). (ii) E exp(H o tau_t - H) = 1 for every t. (iii) Suppose that for every p with beta_p > 0 and every two corners of p where theta is not zero, one of the two sites is free. Then

 E[X(F)^2] = sum_p beta_p E[x_p] sum_(x in p) theta_(p,x)^2.

**Proof.** (i) A link traversed forward contributes e^(t F c) U e^(-t F' c), F at its start and F' at its end. A link traversed backward contributes the inverse, e^(t F' c) U^(-1) e^(-t F c). In both cases the factor begins with e^(+t F c) at the site where p leaves along the link, and ends with e^(-t F c) at the site where p arrives. At a corner the two exponentials have the same axis and multiply to e^(t theta c). (ii) tau_t is a left and a right translation of each integrated link, so it keeps the Haar measure: the integral of exp(H o tau_t) equals the integral of exp(H). (iii) Differentiate (ii) twice at t = 0: E[D] + E[X^2] = 0, D the second derivative of H o tau_t. By (i), D = sum_p beta_p [ -x_p sum_i theta_i^2 + 2 sum_(i<j) theta_i theta_j (1/2) tr(c P_ij c P_ji) ], where P_ij is the ordered product of the factors of p from x_i to x_j and P_ij P_ji = U_p. Let x_i be free. The gauge transformation by h at the single site x_i keeps the measure and every x_p. The closed word passes x_i once, so it maps (1/2) tr(c P_ij c P_ji) to (1/2) tr(h^(-1) c h P_ij c P_ji). The Haar average of h^(-1) c h is an Ad-invariant element of su(2), so it is 0. Hence every cross term has mean 0, and E[X^2] = -E[D] is the stated sum. QED

**Corollary WN1 (no cheap direction).** On a torus with constant strength beta, for a left-translation field f on links (F = f at the start of each link, 0 at its end), with xbar = E x_p:

 E[X(f)^2] = beta xbar sum over p = (x; mu, nu), mu < nu, of [ (f_(x,mu) - f_(x,nu))^2 + f_(x+mu,nu)^2 + f_(x+nu,mu)^2 ] >= 3 beta xbar abs(f)_2^2.

(The corners of p = (x; mu, nu), traversed x, x+mu, x+mu+nu, x+nu, carry theta = f_(x,mu) - f_(x,nu), f_(x+mu,nu), 0, -f_(x+nu,mu). Each link is the second link of nu - 1 plaquettes and the third link of 4 - mu plaquettes, three in all.) So the cost of every such move is comparable to its plain l^2 norm. No Dirichlet form, no curl form.

**Corollary WN2 (non-central twists).** Let theta be any real corner field, not necessarily of the form delta F, whose non-zero corners lie at pairwise distinct free sites. Put W(t) = E exp(sum_p beta_p [x_p(t theta) - x_p]), with x_p(theta) the twisted trace of (i). Then W'(0) = 0 and

 -W''(0) = sum over corners (p, x) of theta_(p,x)^2 [ beta_p E x_p - (beta_p^2/3) E(1 - x_p^2) ].

Proof. W''(0) = E[D] + E[X^2] with X = -sum theta_(p,x) beta_p y_3(U_(p,x)), U_(p,x) the holonomy of p based at x. The cross terms of D (two non-zero corners of one plaquette, at distinct free sites) have mean 0 as in (iii), so E[D] = -sum beta_p E[x_p] theta_(p,x)^2. The gauge average at a free site x rotates the vector y(U_(p,x)) uniformly. So E[X] = 0, the cross terms of E[X^2] at distinct sites vanish, and E[y_3^2] = E(1 - x_p^2)/3. QED

**Corollary WN3 (the size of the bracket in WN2).** On a torus with constant beta put rho(beta) = xbar - (beta/3) E(1 - x_p^2). For one link l, with the six plaquettes q that contain l all oriented to leave the start of l along l,

 rho(beta) = (beta/18) sum over q != q' of E[ y(U_(q,l)) . y(U_(q',l)) ].

Proof. Apply (iii) to F = 1 at the start of l and 0 elsewhere: E[(sum_q y_3(U_(q,l)))^2] = 6 xbar/beta. The gauge average at the start of l gives E abs(sum_q y(U_(q,l)))^2 = 18 xbar/beta. The diagonal part is 6 E(1 - x^2). QED

So rho is the correlation of the field strengths of different plaquettes on one link. For a single free plaquette rho = 0. ARGUED, not proved: rho > 0 for small beta > 0 (first non-zero term from the cube, positive character coefficients), and rho -> 1/2 as beta -> infinity (free-field count: E(1 - x_p) = 3/(4 beta), RECALLED, half the one-plaquette value 3/(2 beta)). A proof that rho > 0 at large beta needs E(1 - x_p) < 3/(2 beta) with a written constant; the lane's RECALLED bound 2/beta is not enough.

**What Lemma WN means.** The Ward identities of link translations live on the **corner graph**: vertices are link-ends, edges are corners. A corner joins two link-ends at the same site. So this graph is a disjoint union of one copy of the 24-edge graph K_(2,2,2,2) per site. The exact analogue of [B] Lemma 2.1 is Lemma WN (iii). The analogue of Proposition 2.2 is expected by the same algebra (ARGUED; not written out). Whatever its form, its cost side is a sum over sites of one-site terms. There is no path in this graph from one site to the next, so there is no family with a harmonic sum. In the spin model the same graph is the lattice itself.

### 4.2 Lemma TWIST: every gauge twist of Dirichlet data is removable on the lattice (PROVED, one line)

Let u be link data on the boundary subcomplex of a finite region, Z(u) the integral over the interior links, and Omega any map from the boundary sites to SU(2). Then Z(u^Omega) = Z(u). Proof: extend Omega by 1 to the interior sites; the gauge transformation is a Haar-preserving change of the interior links and maps the weight with data u to the weight with data u^Omega. QED

So on the lattice the partition function of a pinned cell is a function of the gauge orbit of its boundary data only, with no winding label. The degree of Omega (candidate C3) is invisible to Z. A continuous twist of a pinned cell is therefore a path of gauge-inequivalent boundary data: a Schrodinger-functional family.

### 4.3 Proposition LOC (structural; ARGUED from 4.1, 4.2 and the definitions)

In pure SU(2) lattice gauge theory the three slots of Section 2 can be filled in these ways only.

1. Moves that keep the action: the gauge group. Its commutators are gauge transformations, and by Lemma TWIST they change nothing even when they move pinned data. No signal.
2. Moves that do not keep the action: link-end translations. Their one-axis cost is diagonal in corners (Lemma WN). No gradient structure, in any dimension.
3. Twists: (a) the centre twist, discrete; every continuous path to it through non-central corner twists has second-order cost beta rho per unit of theta^2 on each twisted plaquette (Corollary WN2), so a thin sheet of area A has curvature beta rho A at t = 0, and the lab-frame smearing of the sheet is the same function of t (exact invariance) and costs the same; (b) a change of the gauge orbit of pinned boundary data.
4. So a response with a blind upper bound, gradient invariance and a commutator source (R2-R4) exists only in case 3 (b), with moves that are covariant with respect to a field-dependent frame. Covariant moves with Jacobian one exist (C8), but a frame carried by the unblocked field loses its meaning after a length of order beta (adjoint perimeter decay, RECALLED, ultraviolet). A frame that survives must be built from blocked fields. That is the background field of Balaban's account and the object of row 1011.

The reason in one sentence: **the 2D mechanism needs a continuous non-abelian group that acts as a global symmetry on the integration variables; a pure gauge theory has none, because its only global symmetry on link variables is the centre.** This agrees with row 1007 B(5) and adds the exact form of the failure (the corner graph).

### 4.4 Kill table

Tests K1-K9 of Section 1.2. "pass" means only that the test does not refute the candidate in the valid form.

| Cand. | Decisive test and reason | U(1) (K5) | Q_8, 2T (K6) | d = 5 (K7) | D2, slab, SHEET (K3, K3', K4) | PT, NP (K1, K2) | Spec check S0-S4 | Verdict |
|---|---|---|---|---|---|---|---|---|
| C1 corner-twist inequality | Lemma WN: the cost form is site-local, so R6 has no harmonic sum; the family inequality is a one-site statement | gain zero (one axis) | uses the Lie algebra | fails in every d, also d = 4 | not reached | not reached | S2 fails (no rate) | **FAILS** (Lemma WN PROVED; the conclusion from it ARGUED) |
| C2 non-central path to the centre twist | Corollary WN2: -Z''(0)/Z(0) = beta rho(beta) times the sheet area; the bound Z'' >= -delta Z that [B] p. 12 integrates is false at t = 0 unless rho = 0 | U(1): the twist costs classically | no continuous path in a finite group | no dimension input | periodic only | feeds the flux half only (RE, blocked-local) | S2 fails | **FAILS** (identity PROVED; rho > 0 ARGUED) |
| C3 winding-sector twist | Lemma TWIST: Z_k = Z_0 exactly on the lattice | - | - | - | - | - | the object is void | **FAILS** (PROVED) |
| C4 induced-boson third copy | the weight is not the Wilson weight; colour is not exchangeable given the links; no consumer; Proposition V warns for non-linear weights | - | - | no input | - | - | S0: a frame change (row 1004 family (c)) | **FAILS** for T0 (ARGUED); found again |
| C5 direction-layer diamagnetic gap | K7: the conditional gain holds in d = 5, where the conclusion is believed false, so all of the crux sits in the gap of the direction-block dynamics; the seagull term it uses is cancelled at long wavelength by the vertex terms (gauge invariance; ARGUED) | gain zero | gain zero when frozen | **fails K7** | pointwise in the background: passes by form | reads one direction given the rest | S0: renames the crux | **FAILS** as a route (ARGUED); found again (row 859 idea 1, row 834) |
| C6 centre clusters | Ginibre monotonicity gives abs E W_C <= the Z_2 Wilson loop at coupling beta, a perimeter law at weak coupling; the centre variables are frozen there; SO(3) monopole cubes break the ferromagnetic form | - | blind to the group beyond its centre | no input | - | centre-odd sector only | S1 fails | **FAILS** (ARGUED); found again in kind |
| C7 biharmonic frame field | (1) Proposition LOC 1: the frame decouples from every gauge-invariant observable, and commutators of frame moves are frame moves; (2) the uniform one-axis cost is (C/alpha) abs(df)^2, a Dirichlet form (the biharmonic form holds only for smooth dressed links), so in the class of all backgrounds the mode sum is not a logarithm in d = 4 | gain zero | uses the Lie algebra | scale-free only at d = 4 and only for smooth V | class of all backgrounds: no log | reads no physical factor | S3 fails | **FAILS** (ARGUED); the kernel itself is an exact identity |
| C8 tree-transported translations | frames carried by unblocked links decohere after length of order beta; the gradient structure survives only up to scales of order beta^(1/3) (wedge loops of area r against beta), which is inside the perturbative range | gain zero | uses the Lie algebra | would use d = 4 | Dirichlet cells | - | S0: with blocked frames it is row 1011 and the account's background | **FAILS** as a band crossing (ARGUED); the triangular Jacobian is exact |

**No candidate survives.** Three die by exact lemmas (C1, C2, C3), five by argued reasons. Every continuous-twist candidate either returns to the Schrodinger-functional family of row 1011 or has a site-local cost form.

## 5. Steps 5 and 6 result: no survivor; what the counterexamples say about the one open door

Task (4) of the row asks for the first lemma of each survivor, or the counterexample. There is no survivor. The counterexamples are built: Lemma WN with Corollaries WN1-WN3 (C1, C2) and Lemma TWIST (C3). This section adds two lemmas that follow from the same computations. They concern the only door left by Proposition LOC, a response to gauge-invariant boundary data. They do not redo row 1011's port; they are constraints that any such port meets at its first step. On the path of the target only as constraints.

### 5.1 Lemma JEN: the lab-frame blind bound of a boundary twist (PROVED by hand)

**Setting.** As in Lemma WN. Pinned data u; a real field a on the pinned links; twisted data u^(eta)_l = e^(eta a_l c) u_l. Let F be any link-end field with F = a_l at the start of each pinned link l, F = 0 at the end of each pinned link, and arbitrary values on the ends of integrated links. Let theta = delta F be its corner field and tau_eta its translation, acting on all links. E_u is the expectation with data u.

**Statement.** (i) Z(u^(eta))/Z(u) = E_u exp(H o tau_eta - H) >= exp( - sum_p beta_p E_u[x_p - x_p o tau_eta] ). (ii) If all corners of p with theta not zero are at free sites, then E_u[x_p o tau_eta] = E_u[x_p] prod over the corners of p of cos(eta theta_(p,x)).

**Proof.** (i) In the integral for Z(u^(eta)) translate the integrated links by tau_eta; this keeps the Haar measure, and the weight becomes exp(H o tau_eta) at data u, by Lemma WN (i) applied to all links. Then Jensen. (ii) Average over the gauge group at each free corner site of p, one site after the other. The insertion e^(eta theta c) = cos(eta theta) + sin(eta theta) c becomes cos(eta theta) times the identity, because the Haar average of h^(-1) c h is 0. The trace is linear in each insertion. QED

**What it gives.** The cost of the twist, -log Z(u^(eta))/Z(u), is at most the sum over bulk plaquettes of beta_p E[x_p] (1 - prod cos(eta theta)) plus the terms of the plaquettes at pinned sites. For small eta this is (beta xbar eta^2/2) times the squared l^2 norm of the corner field. By Section 4.1 the corner graph is site-local: values of F on integrated link-ends can cancel only the part of a that is constant over the pinned link-ends of one site, that is a gauge transformation. So (ARGUED; the minimisation over F is not written out) for a boundary field of size 1/R on a boundary of R^3 sites, whose curl is not zero, the best lab-frame bound is of order beta eta^2 R. The classical action of the induced background is of order beta eta^2, with no factor R.

**Contrast with 2D (OpenAI's [B] (3.3)-(3.4), [28] (3.5)).** There the same Jensen step, or dropping the variance, with a smooth profile Theta across the annulus gives b times the Dirichlet energy of Theta, which is of order b at every scale. The profile can be spread because one-axis rotations at different sites commute and the cost form is a lattice gradient. In the gauge theory the spread is blocked by Lemma WN.

**Consequence for a pinned-cell iteration in 4D (ARGUED).** The start of the 2D iteration, "stiffness at most b on every cell, every pin", is one line in 2D. Its 4D analogue, "the response of a pinned cell to a boundary field is at most a constant times beta times the classical action of the background, for every cell size up to the correlation length and all boundary data", is not available from the lattice identities above. On record it exists only as Balaban's Ward-identity extraction of (1/g_k^2) A(U_k(V)) on small fields while every g_k is small (CMP 109 (0.22), Theorem 1; row 1012 B1). So a 4D form of the iteration cannot be "one fixed bare coupling, no RG, no first-passage data" as in 2D. Even its blind first step needs the account's effective actions, and then it is a (K-flow) statement in the sense of lead rule W2, with the open step still the selective gain across the band.

### 5.2 Lemma SLAB: conditioning can create an ordered spin system (identity PROVED; consequence ARGUED)

**Statement.** Let B be a finite three-dimensional box or torus. Pin every link inside the two slices {0} x B and {1} x B, to data A and A'. The only integrated links are g(y) = U_4(0, y), y in B. Their law is the three-dimensional model with density proportional to exp( beta sum over y, mu of (1/2) tr(A_mu(y) g(y+mu) A'_mu(y)^(-1) g(y)^(-1)) ). For A = A' = 1 it is the O(4) model exp(beta sum q_y . q_(y+mu)), q the unit quaternion of g.

**Proof.** The plaquettes that contain an integrated link are the (mu, 4) plaquettes between the slices; each is the displayed trace. QED

**Consequence.** For large beta the three-dimensional O(4) model has long-range order (Frohlich, Simon and Spencer 1976; RECALLED, not rebuilt). The two-point function of g is the expectation of a gauge-invariant loop (up at y, along the pinned slice, down at y', back). So at weak coupling a family of conditional laws that contains "given two neighbouring hyperplanes" has no uniform mixing. In the 2D spin class the corresponding conditioned systems are one-dimensional and massive, so the 2D class has no such member. A gauge class closed under conditioning must therefore fix the shape of its cells. This is the same construction as Theorem D2's pinned sheet, one dimension up; D2 is credited (row 977, `gap-tiltproof-max.md` L240).

### 5.3 Where each exact statement sits

| Statement | Mark | Used for |
|---|---|---|
| Lemma WN (i)-(iii), Corollaries WN1, WN2, WN3 | PROVED by hand, unchecked | kills C1, C2; the corner graph |
| rho(beta) > 0 for small beta and rho -> 1/2 | ARGUED | size of the kill of C2 |
| Lemma TWIST | PROVED, unchecked | kills C3; corrects the wording of K8 (see 6.3) |
| Proposition LOC | ARGUED | the structural conclusion |
| Lemma JEN (i), (ii) | PROVED by hand, unchecked | the blind bound of a boundary twist |
| "best lab-frame bound is of order beta eta^2 R" | ARGUED | constraint on row 1011's first step |
| Lemma SLAB (identity) | PROVED, unchecked | constraint on any gauge class (R7) |
| Lemma SLAB (no uniform mixing) | ARGUED, given a RECALLED theorem | the same |

## 6. A ninth candidate found while closing the table, and the main conclusion

### 6.1 C9: moves along a Laplacian frame (ARGUED; no lemma proved)

- Object. A covariant adjoint frame Omega[U] in SO(3) at each site, for example the three lowest eigenvectors of the adjoint covariant Laplacian after polar decomposition (the Laplacian gauge of Vink and Wiese, RECALLED; lane grep: "Vink", "Laplacian cent": no file). Moves U_l -> Omega_x e^(F_l) Omega_x^(-1) U_l with F_l in su(2) written in the body frame. If the frame were covariantly constant, a one-axis move would change every plaquette by the abelian curl (dF)_p exactly, and the algebra of Section 2 (two axes, bracket along the third, shells of modes) would have the power counting of the Yang-Mills action: the sum over four-dimensional shells of abs(k)^(-4) is a logarithm. In that sense the twist two-form is the bracket [a_i, abar_i] of two one-forms, as the 2D twist one-form is S(f_i, fbar_i).
- (a) Monotone: a boundary-field response. (b) Class: Dirichlet cells. (c) Identity: the bracket in the body frame. (d) Scale invariance of the Yang-Mills action. (e) Consumer: the Proposition 2.1 analogue.
- What stops it. The frame defect D_l Omega = Omega_x - Ad(U_l) Omega_y is not zero; its mean square is the lowest eigenvalue of the adjoint Laplacian. It adds to the cost form beta abs(dF)^2 a term without derivative, of order beta times abs(D Omega)^2 times abs(F)^2. On unblocked links this is of order one per link (ultraviolet), so the gradient structure holds only up to wavelengths of order sqrt(beta). With frames of blocked fields at scale s it holds while the coupling at scale s is small. And the frame depends on the field, so the moves carry a Jacobian that is not one (unlike C8).
- Verdict: **FAILS as a band crossing** (ARGUED). It could at best re-derive the running of the response where the coupling is small. Found again in substance: `gap-crux-skeleton-max.md` L236 ("the rotation axis must be covariantly constant"), and Balaban's background field.

### 6.2 The main conclusion of this row (ARGUED, from Lemma WN, Lemma TWIST, Lemma JEN, C8, C9)

**In 2D one exact Ward identity works at every value of the stiffness, large or small, because the symmetry is global and acts on the integration variables. In 4D every substitute found here works only while a colour frame exists across the cell, that is while the response is large (weak effective coupling). So the 2D engine, moved to 4D in any of these forms, reproduces asymptotic freedom above the band and stops at the upper edge of the band.** The 2D papers cross the band with the same identity in its "short step" regime ([28] (3.52), row 1009 L143-150). No 4D counterpart of the short step was found: at order-one response there is no frame, and the lab-frame identities are site-local.

This agrees with the lane's sentence "the one selective fact that is provable today, asymptotic freedom at small coupling, has no engine that carries it across the band" (`parts/gap.md` L41-43). It adds a reason that is specific to the 2D mechanism, and three exact lemmas behind it.

### 6.3 Filters (exercise skill, step 6)

- **K8, valid form (ARGUED).** By Lemma TWIST a partition function with pinned data has no winding label. The refilling problem of row 1010 is a different statement: a region whose exterior data are smooth and wind has no filling of small action. In a comparison of densities such a region is one more kind of large-field region, with an activity of order exp(-c beta_k) at the scale of the refilling. So K8 is a cost with a constant to compute, not an obstruction of principle. The constant for the Wilson action is not computed here; lattice dislocations make it smaller than the continuum 2 pi^2 (RECALLED).
- **K3' (slab device)** is added to the kill sheet as a test of classes; Lemma SLAB is its exact part.
- No other filter was changed. Theorem D2, Lemma SHEET, Lemma PT and Proposition NP were used as they stand and re-derived nowhere.

## 7. Step 7 result: novelty, ranking, work items

### 7.1 Novelty

No claim of novelty is made outside this lane, so no literature search was run (the row allows one only to check such a claim). Lemma WN is a form of the Schwinger-Dyson equations of lattice gauge theory together with Elitzur-type gauge averaging; the soft gauge-fixing kernel of C7 is known (Zwanziger; Parrinello and Jona-Lasinio; RECALLED), and so is the asymptotic freedom of the higher-derivative longitudinal sector (Golterman and Shamir, RECALLED). Inside the lane, by the grep of Section 3: "corner graph", Lemma WN in exact form, Lemma JEN and Lemma TWIST were not found; the argued forms they sharpen are credited (`gap-brainstorm2-max.md` L161, L216; `gap-crux-skeleton-max.md` L236; row 1007 B(5)).

### 7.2 Ranking

There is no survivor to rank. Ranked by what each result changes, divided by the cost to find out:

1. **Lemma JEN and its scaling remark** (cost: one check). If the remark holds, the blind first step of a 4D pinned-cell iteration is not a lattice identity, and row 1011's port must start from the account's effective actions. This changes how row 1011's output is read.
2. **Lemma SLAB** (cost: one check). It constrains every class closed under conditioning.
3. **Lemma WN and Proposition LOC** (cost: one check). They close the family "lab-frame Ward identities of link translations" for good, with the reopen condition below.
4. Lemma TWIST (one line).

**Reopen condition for the families of this row.** (i) An exact reformulation of pure 4D SU(2) lattice theory in which a continuous non-abelian group acts as a global symmetry on the integration variables and moves gauge-invariant observables; or (ii) covariant moves with a controlled Jacobian whose cost form stays a curl form when the response is of order one. Without (i) or (ii) no further invention row on twist mechanisms is proposed.

### 7.3 Work items (each a complete brief)

**W1, check (a model that did not write this file; high effort).** Check line by line `library/gap-invent-selective-max.md` Sections 4.1, 4.2, 5.1, 5.2: Lemma WN (i)-(iii), Corollaries WN1-WN3, Lemma TWIST, Lemma JEN (i)-(ii), Lemma SLAB. Test first: (a) the sign rule of WN (i) for a link traversed backward; (b) the one-plaquette case: for the density exp(beta x) on SU(2), (beta/3) E(1 - x^2) = E x by one integration by parts with the weight (2/pi) sqrt(1 - x^2), so rho = 0 there; (c) in WN (iii), that the gauge average at one free site kills each cross term and that the closed word passes that site once (sides at least 3); (d) the count "three" in WN1; (e) in JEN (ii), that the averages at the four corner sites may be taken one after the other. Then judge the two ARGUED remarks: "the best lab-frame bound is of order beta eta^2 R" (5.1) and Proposition LOC (4.3). Report the first failing step, or none. Stop rule: no new attack. Output `library/gap-invent-selective-check.md`.

**W2, reading for the check of row 1011 (the model that checks `library/gap-pinned-cell-gauge-max.md`).** Read Sections 5.1 and 5.2 of this file. Answer for row 1011's construction: (1) what is its blind bound on the stiffness of a cell of side R, and does it scale like beta or like beta R; if like beta, which covariant representative or which theorem of the account supplies it; (2) does its class contain two pinned parallel hyperplanes at distance below beta, or cells that are not cubes; (3) does its iteration run at one fixed bare coupling without the account's effective actions. No new claim. Output: three lines in the check file of row 1011.

**Not proposed.** (1) A proof that rho(beta) > 0 at large beta (it needs E(1 - x_p) < 3/(3 + 2 beta) with a written constant): it would only complete the kill of C2. (2) The Jacobian of the Laplacian-frame moves of C9: it works above the band only. (3) Any row on C4 (another action), C5 (on file as the frustration bootstrap, with row 834's open inequality), C6, C7.

## 8. Step 8: report (exercise skill, step 9) and RESULT

**What this run did not cover.** No numeric run. No literature search. The primary 2D texts were read only at [B] pp. 1-12 and [28] pp. 4-8; the rest through rows 1007, 1009, 1010. The lane was searched by grep for the listed terms only, not read. Row 1011's result did not exist at this pin. Nothing here is checked by another model.

1. **The wall, in plain words.** Two-dimensional spin models with a non-commuting symmetry have a proof that long-range order melts at every temperature. The proof twists the spins on one boundary and shows that the cost of the twist shrinks as the box grows; the shrinking comes from the fact that rotations about two axes do not commute. We asked whether new mathematics of the same kind exists for the four-dimensional SU(2) lattice gauge theory.
2. **What this run found.** (ARGUED, with PROVED lemmas.) The 2D proofs follow ten design rules (Section 2). Nine gauge mechanisms were built from them, none the direct port of row 1011 (Sections 3, 6.1). None survives. The common reason is exact: in a gauge theory the colour symmetry is local, so the changes of variables that are free do nothing, and the ones that do something cost a fixed amount per site, however smooth they are (Lemma WN, PROVED). A gauge twist of pinned boundary data is always removable (Lemma TWIST, PROVED). What is left is a response to gauge-invariant boundary data with a field-dependent colour frame. That is row 1011's object, and it works only while a frame exists, that is above the band.
3. **Filters corrected.** K8 (winding and refilling) is a cost, not an obstruction (ARGUED, 6.3). One test added: the slab device (Lemma SLAB).
4. **Routes worth doing.** None from this row. The reopen condition is in 7.2.
5. **What not to do next.** Another invention row on twist or stiffness mechanisms in the lab frame; a path to the centre twist through non-central twists; a winding-number twist of pinned data; a third-copy representation for the Wilson weight.
6. **The exact price.** Not changed: (W), or (CAS), or the seed (`parts/gap.md` L225-236). This row adds: a 4D analogue of the 2D "short step" (a selective gain at order-one response) is the missing object, and no candidate for it was found.
7. **Work items.** W1 and W2 of 7.3.

RESULT: Row 1013 (Claude Fable 5.2 max, Mac mini worker 2; author, checked by no one; no numeric run, no literature search). (1) Ten design rules R1-R10 reconstructed from OpenAI's 2D texts, each with its place (a reconstruction, ARGUED); forced by "zero gain for the abelian model": two non-commuting axes, order four, a twist that is a bracket of trivial moves. (2) Nine candidate mechanisms for 4D SU(2) that are not the direct port; C4, C5, C6 found again in the lane and credited. (3) No candidate survives: C1 (corner-twist inequality), C2 (non-central path to the centre twist) and C3 (winding twist) FAIL by exact lemmas; C4-C9 FAIL by argued reasons (C5 at the five-dimensional test, C7 and C8-C9 because a colour frame exists only above the band). (4) PROVED by hand, unchecked: Lemma WN with Corollaries WN1-WN3 (the cost form of every lab-frame link translation is diagonal in corners, E X^2 = sum beta_p E x_p theta^2, at least 3 beta xbar times the l^2 norm; non-central twists at free sites cost beta rho per theta^2, rho = (beta/18) times a same-link field-strength correlation), Lemma TWIST (every gauge twist of pinned data is removable; no winding label on the lattice), Lemma JEN (Jensen bound of a boundary twist, with cosine factors), Lemma SLAB (two pinned neighbouring hyperplanes carry the 3D O(4) model). ARGUED: Proposition LOC (a twist with a blind bound and a bracket source exists in pure gauge theory only as a response to gauge-invariant boundary data with a field-dependent frame), the scaling beta eta^2 R of the lab-frame blind bound (so the blind first step of a 4D pinned-cell iteration needs the account's effective actions and is a (K-flow) statement), rho > 0, and the corrected form of the refilling test K8. Open: (W), (CAS) and every form of the wall, untouched; a 4D analogue of the 2D short step at order-one response; the check W1 of this file and the reading W2 for row 1011.
