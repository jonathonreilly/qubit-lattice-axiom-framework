lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T07:39Z

# gap-global-reform-max (row 1016): an exact reformulation with a global non-abelian symmetry

Status: IN WORK. Research-stage working state. Nothing here grants status. No claim of a mass gap.
Pinned at commit b9125417f of `claude/ym4d-hard-route`. Started 2026-11-15T19:39Z (`date -u`).
Author: Claude Fable 5.2 (max), Mac mini worker. Not yet checked by another model.

## 0. Plan (at most eight steps; one step per response; each result is appended before the next step)

1. Read the inputs (`parts/gap.md`, rows 1011, 1014, 1013, and 1009/1010 as needed) and the exercise skill. Write
   Section 1: the question, the three slots, the reopen conditions, in the lane's own words with anchors.
2. Run the exercise skill's blind pass and its literature lens. Write the candidate list. Grep the registry
   (`library/open-core.md`, FINISH rows, the idea digests) for each candidate before any attack.
3. Candidates with auxiliary fields: frozen or integrated Higgs field with its custodial group (Fradkin-Shenker),
   Hubbard-Stratonovich, character expansion, rotor / quantum link. For each: exact lattice identity, group, action,
   does it move gauge-invariant observables.
4. Candidates without auxiliary fields: gauge fixing with a global non-abelian residual group (Gribov, Jacobian),
   the Hamiltonian with Gauss law, a one-sided comparison with a model that has the symmetry.
5. Tests on every candidate: Lemma CEN / Elitzur, compact U(1), the five-dimensional test, Lemma PT, Proposition NP,
   Theorem D2, Lemma SHEET, Lemma SLAB, and the three slots of row 1013 Section 2.
6. For a survivor: the first lemma (exact Ward identity with bracket term in the reformulated variables, blind
   bound), proved by hand, or the counterexample.
7. Reopen condition (ii) (covariant moves, controlled Jacobian, curl cost form at order-one response) and the
   homogeneous-strength case of Proposition B' that row 1014 left ARGUED.
8. Consumer (which step of the chain to (W) or to a 4D analogue of Proposition 2.1 is replaced, with the exponent
   condition of row 1010), registry of what is new against what is found again, report, RESULT line.

## Status log (times from `date -u`)

- 19:39Z file created with the plan. Nothing proved yet.
- 19:56Z step 1 done (inputs read, wall and contract written). Nothing proved yet.
- 20:08Z step 2 blind pass written (inventory, conclusions C1-C8, assumptions, candidates). Proofs follow in Sections 3, 4, 7.
- 20:10Z comparison with the lane and with main / PR #10114 written (2.5). No row holds the items attacked below.
- 20:15Z step 3 written (auxiliary fields: Lemma AUX, H1-H3, Lemma HW, Proposition LG, HS1; all five FAIL).
- 20:18Z step 4 written (Lemma CEN+, Lemma REM, Lemma MC, Identity HAM1; gauge fixings, Hamiltonian, comparisons: all FAIL).
- 20:22Z steps 5 and 6 written (test table; no survivor for (i); the reopen condition corrected to rigid + charged pins + on the gauge-invariant algebra).
- 20:25-20:26Z GUIDE control of the algebra of Theorem BH run under the numeric lock (two runs of 27 s; lock released); all four pre-registered readings pass.
- 20:28Z step 7 written (Identity AV, Corollary AV2, Theorem BH, Lemma GT, Lemma SOFT; reopen (ii) FAILS pointwise).

## 1. Step 1: inputs, the wall stated twice, the target contract (exercise steps 0 and 1)

**Provenance.** Anthropic, Claude Fable 5.2, max effort, one session on the Mac mini worker, no subagents. Nothing in
this file is checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no
computer-assisted step; proofs that could be formalized in Lean) replaces the framework refresher read of the
exercise skill. The skill was fetched at main 8b11ae2bb9 into `/tmp/row1016-skill/` with its one reference file
`proof-search-governance.md`; both were read in full.

**Read in full:** `GOAL.md`; `FINISH.md` L1-84 and row 1016; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md`
L102-376 and L393-622 (row 1011: Sections 2-4.7, 5-9); `library/gap-invent-selective-max.md` L35-299 (row 1013).
**Read by headings only so far:** `library/gap-pinned-cell-gauge-check-opus.md` (row 1014; its B' part is read in
step 7). **Closed until the comparison step (exercise step 5):** every other lane file on reformulations, frame
changes, dualities, gauge fixing, Hamiltonian forms, Higgs fields and idea lists, in particular
`gap-outside-box-max.md` (row 1004), `gap-brainstorm-max.md`, `gap-brainstorm2-max.md`, `gap-next3-max.md`,
`gap-constraints-max.md`, `gap-crux-fp.md`, `gap-loop-eq-opus.md`, `gap-sgstep-opus.md`, `gap-pca-opus.md`,
`gap-skeleton-max-b.md`, and `library/open-core.md`. They are grepped before any attack (rule 0a) and before any
item is called new.

**Credit.** The 2D mechanism is OpenAI's (github.com/openai/math, posted, unrefereed) as read by rows 1007, 1009,
1010 (Claude Opus 5.5). Rows 1011, 1013 (Claude Fable 5.2) and check 1014 (Claude Opus 5.5) supply Lemma CEN,
Corollary CEN2, Propositions A, W, B, B', SEAG, Lemmas EMB, FR, WN, TWIST, JEN, SLAB and the reopen condition. The
layer idea is Durhuus and Frohlich's (1980). Other sources are credited where they are used.

### 1.1 The wall, plain version

OpenAI's two-dimensional proof works because one can turn all spins of a magnet together at no cost. Turning them
by an amount that varies slowly from place to place is then cheap, on every arrangement of the spins. The proof
shows that the price of such a slow turn falls as the block grows, because turns about different axes do not
commute. In the four-dimensional gauge field the "turn everything together" operation exists too, but it is
invisible: it changes no quantity that can be measured. So its price is always exactly zero and tells nothing.
This row asks whether the gauge theory can be rewritten, exactly, in other variables in which a visible operation
of this kind exists. It also asks for moves that follow the field and still have a controlled price. Getting past
the wall means such a rewriting together with its first exact identity, or a proof that a named family of
rewritings cannot have one.

### 1.2 The wall, precise version (quoted; not rewritten)

- Reopen condition of row 1013 (`library/gap-invent-selective-max.md` L277): "(i) An exact reformulation of pure 4D
  SU(2) lattice theory in which a continuous non-abelian group acts as a global symmetry on the integration
  variables and moves gauge-invariant observables; or (ii) covariant moves with a controlled Jacobian whose cost
  form stays a curl form when the response is of order one."
- Reopen condition of family G1 of row 1011 (L612): "a reformulation with an exact non-abelian zero-form symmetry
  on every configuration".
- The homogeneous-strength case (row 1011 L259-261, check 1014): Proposition B' is PROVED for the strength field
  "b on boundary plaquettes, 0 inside" and ARGUED for the homogeneous field beta_p = b.
- The three slots (row 1013 L91): "(i) A response quantity with a blind upper bound and gradient invariance (R2,
  R3). (ii) Two non-commuting families of trivial moves whose commutator is the twist, with a scale-invariant
  cost (R4-R6). (iii) A representation that turns a small response into decay of all observables (R9), inside a
  class that survives Theorem D2, the slab device and Lemma SHEET (R7)."
- What blocks now: Lemma CEN and Corollary CEN2 (the only configuration-independent link symmetries are central,
  for every gauge group), Lemma TWIST (every gauge twist of pinned data is removable), Lemma WN (the cost form of
  lab-frame link translations is diagonal in corners), Propositions B and B' (the pin supremum is blind to colour
  coherence).

### 1.3 Exact target contract (proof-search governance)

| Field | Content |
|---|---|
| Target statement | T_i: there is an exact reformulation R of Wilson SU(2) on a finite 4D lattice (same partition function up to an explicit factor, same expectations of gauge-invariant observables), a compact connected non-abelian Lie group K acting on the integration variables of R, and a gauge-invariant observable O of the original theory whose image in R is not K-invariant; and the K-twist of R has the three slots. T_ii: a family of field-dependent link moves with an explicit Jacobian whose second-order cost is a curl form, uniformly, at response of order one. T_h: Proposition B' with beta_p = b on all plaquettes. |
| Quantifiers, domain | Every finite box or torus, every beta > 0 (the engine must work at one fixed bare coupling, as in 2D), SU(2), Wilson action. For T_h: every box with a boundary plaquette, every b > 0. |
| Allowed premises | The definitions; the lane's proved lemmas with their marks; published theorems as labelled inputs. |
| Forbidden weakenings | A symmetry that moves no gauge-invariant observable (Elitzur); a comparison model in place of an identity unless the inequality and its direction are written; a gain that also holds for compact U(1); a statement that reads first-passage data and is called a one-scale engine; any numeric step in a proof. |
| Required edge cases | Compact U(1) (gain must vanish), Q_8 and 2T (the Lie algebra must be used), d = 5, products with a massless factor (Lemma PT), Proposition NP, Theorem D2, Lemma SHEET, Lemma SLAB, kappa = 0 limits of auxiliary fields. |
| Completion witness | For T_i or T_ii: the identity, the group action, the Ward identity with its bracket term and its blind bound, all proved by hand; or, per candidate, a proved lemma that shows the failing slot. For T_h: a proof or a counterexample. |
| Outcomes that do not count | A list of candidates with no lemma; a symmetry of an enlarged model that decouples from the gauge-invariant algebra, reported as a pass; "would follow by standard arguments". |

**Step 1 result.** The question is posed with its quantifiers. Nothing is proved in this step.

## 2. Step 2: the blind pass (exercise steps 2 to 4), written before the lane's attack files were opened

Marks as in the skill: DEF, THM (with standing and reading state), BELIEF; statements of this run are `argued`
until a check. "PROVED" below means proved by hand in this file by Claude Fable 5.2, checked by no one.

### 2.1 Inventory

| # | Item | Mark | Source | Standing, reading state |
|---|---|---|---|---|
| I1 | Wilson SU(2): links in SU(2) = unit quaternions, Haar measure, weight prod_p exp(beta_p t_p), t_p = Re U_p. The action is affine in each link (a real-linear function of U_l in R^4). | DEF | row 1011 3.1 | - |
| I2 | Lemma CEN, Corollary CEN2: configuration-independent link multipliers that keep every plaquette energy are closed centre fields. | THM | row 1011 L263-288 | lane; check 1014 (same provider), no WRONG; read in full |
| I3 | Lemma TWIST: Z(u^Omega) = Z(u) for pinned boundary data u. Lemma WN: E[X(F)^2] = sum_p beta_p E[x_p] sum_corners theta^2 for lab-frame link-end translations at free sites. | THM | row 1013 4.1, 4.2 | lane, unchecked (check = row 1015, running); read in full |
| I4 | Propositions A, W, B, B' (boundary strengths), SEAG; Lemmas EMB, FR. | THM | row 1011 3-4, 7.3 | lane; check 1014, no WRONG; B' homogeneous case ARGUED; read in full |
| I5 | Elitzur: a local gauge symmetry cannot break; expectations of non-invariant local functions vanish. | THM | Elitzur 1975 | published; recalled; used here only in the one-line form "average over the gauge group at a free site" |
| I6 | Fundamental Higgs: Higgs and confinement regions are analytically connected in the region of convergent expansions (large hopping or small beta). | THM | Osterwalder and Seiler 1978; Fradkin and Shenker 1979 | published; recalled; not read in this run |
| I7 | Diamagnetic inequality for lattice Higgs fields: Z_H(U) <= Z_H(1). | THM | Brydges, Frohlich and Seiler 1979 | published; recalled; the loop-gas proof for frozen fields is rebuilt in Section 3 |
| I8 | Complex translations give power-law upper bounds for 2D rotor correlations. | THM | McBryan and Spencer 1977 | published; recalled |
| I9 | Twist flows on spaces of surface-group representations; torus actions on moduli of flat SU(2) connections; volume formula. | THM | Goldman 1986; Jeffrey and Weitsman 1992; Witten 1991 | published; recalled; used only as a lens |
| I10 | The 2D engine: one exact Ward identity of a rigid on-site non-abelian symmetry, at every stiffness. | THM | OpenAI (unrefereed), through rows 1009, 1010, 1013 | read in those rows, not here |
| I11 | Compact U(1) in 4D is massless at weak coupling. | THM | Guth; Frohlich and Spencer | published; recalled; in the lane for Villain at beta >= 2^14 |
| I12 | 4D SU(2) has a mass gap at every beta. | BELIEF | - | used in no proof |

### 2.2 Reasoning up from the inventory (conclusions; each is proved or attacked in a later section)

- C1 (from I1; one line). A transformation group that preserves the Gibbs measure at two values of beta preserves
  the Haar measure and the action S. So a beta-independent symmetry is a symmetry of the microcanonical shells.
- C2 (from I1; PROVED in Section 4, Lemma MC). Such symmetries exist, are continuous, non-abelian, and are not
  gauge transformations: given the other links, the law of U_l is a von Mises-Fisher law on S^3 with mean
  direction the normalised staple sum, and the SO(3) of rotations of S^3 about that direction keeps the Haar
  measure and S. They move single plaquette traces. So reopen condition (i), read literally, has a void solution.
  **What the 2D engine uses is more: the group acts rigidly (the same field-independent map on each on-site
  variable), so that its localised version is not a symmetry and has a cost.** A field-dependent local symmetry
  has no cost form at all. The condition has to say "rigid".
- C3 (extends I2; PROVED in Section 4, Lemma CEN+). Rigid on-site maps in link variables: every family of maps
  phi_l: SU(2) -> SU(2), one per link, with no assumption of continuity, group structure or measure, that keeps
  every plaquette trace is a gauge transformation times a closed Z_2 field. Proof idea: t_p = <U_1, M> with
  M = U_4 U_3 U_2^(-1); put U_1 = M to get M' = phi_1(M); then phi_1 keeps the inner product of S^3, so it is in
  O(4); the functional equation phi_1(U_4 U_3 U_2^(-1)) = phi_4(U_4) phi_3(U_3) phi_2(U_2)^(-1) excludes the
  orientation-reversing component and forces L_1 = +-L_4 at each corner.
- C4 (from I3). In any formulation whose rigid group is global colour (complete axial or tree gauge, plaquette
  variables with Bianchi constraints), a relative colour rotation of a union of connected components of the
  pinned link graph is removable (Lemma REM, Section 4; it is Lemma TWIST for a general pinned set). A relative
  rotation inside one connected component changes the gauge orbit of the pin; then it is a member of the
  Schrodinger-functional family of row 1011.
- C5 (from the definitions; Section 3). An auxiliary field phi drawn from a gauge-covariant probability kernel
  rho(phi given U), with a group K acting on phi only, leaves the U-marginal exact, and K fixes every function of
  U. Its twist response is the Wilson expectation of an explicit gauge-invariant functional (a ratio of twisted
  and untwisted kernel normalisers). For the frozen fundamental Higgs kernel that functional is a series of
  products of Wilson loops with non-negative coefficients.
- C6 (the least a solution must contain). A rigid group K, a pinned datum that is charged under K and cannot be
  rotated back by a change of the integrated variables, and a cost form of the localised K. In pure gauge theory
  a pinned datum is charged under colour only relative to another pinned datum joined to it by pinned links.
- C7 (reopen (ii); Section 7). In SU(2) the class angles phi_p of the plaquettes are not tied by a linear Bianchi
  identity. The map from gauge orbits (dimension 9N on a 4D torus of N sites) to the 6N plaquette traces has
  fibres of dimension 3N at generic points, and the law of the trace field under Haar measure has a density. So
  for every real plaquette field v there are covariant link moves that shift the class angles by v to first
  order; for U(1) only exact v exist. The Wilson part of their cost is exactly the abelian one. All of the
  difficulty sits in the Jacobian, a beta-independent entropy functional.
- C8 (the homogeneous case of B'; PROVED in Section 7, Theorem BH). For every pin-translation field B,
  E_free[H_c(.; B)] = E_free[(E_omega X_c(B))^2], where E_free is the same box with all links integrated. With
  psi = D_B t_p for one boundary plaquette, Cauchy-Schwarz and Lemma WN-type gauge averages give
  sup over pins of H_c(omega; a d lambda_z) >= 6 (E_free t_p)^2 / E_free(1 - t_p^2) > 0 for homogeneous strength b,
  every b > 0. So Proposition B' holds for homogeneous strengths, with an explicit constant.

### 2.3 Assumptions (ranked by how much the problem changes if dropped)

| ID | Assumption | Needed or habit | If wrong or dropped | Check |
|---|---|---|---|---|
| A1 | The symmetry must be an identity of the same model ("exact reformulation"). | needed by the reopen condition; habit for the target | a comparison model with a rigid symmetry may be used if an inequality with a written direction links it to Wilson SU(2) | Section 4 (diamagnetic, layer, complex translation) |
| A2 | The group acts rigidly and on-site. | needed by the 2D engine | field-dependent symmetries exist (C2) but have no cost form | Lemma MC |
| A3 | The response must be a second derivative in a real twist. | habit | complex translations (McBryan and Spencer) give one-sided bounds without a symmetric model; they use one abelian direction only | Section 4 |
| A4 | The class is a supremum over all pins. | needed by the 2D iteration; habit here | a free-ensemble average over pins is exact (C8) but is as blind to colour coherence as the supremum | Section 7 |
| A5 | Moves are one-axis link rotations along a frame. | habit | angle moves (C7) have an abelian cost and an entropy Jacobian | Section 7 |
| A6 | The symmetry must move observables of the pure gauge algebra. | needed (Elitzur) | a symmetry of an added sector gives a quenched response of that sector | Section 3 |
| A7 | Owner rules: no computer-assisted proof step; hand proofs. | working rule | not questioned | - |

First five, one line each: A1 dropped: look for an inequality with a symmetric model. A2 dropped: nothing gained
(C2). A3 dropped: only blind bounds. A4 dropped: the average is still blind. A5 dropped: the open object is the
entropy functional of C7.

### 2.4 Candidate list for Sections 3 and 4

Auxiliary fields: (H) frozen fundamental Higgs with custodial group, as a model and as an exact kernel; (N) adjoint
unit field with the U(1) about it; (HS) Hubbard-Stratonovich; (CH) character expansion and plaquette variables with
Bianchi constraints; (QL) rotor and quantum-link forms.
Without auxiliary fields: (GF) gauge fixings with a global residual group (tree, temporal, two-dimensional
residual, Landau); (HAM) the Hamiltonian with Gauss law and the unprojected kernel; (CMP) one-sided comparisons
(diamagnetic inequality, the layer comparison, complex translations); (MC) microcanonical rotations; (ANG) the
trace field and angle moves.

**Step 2 result.** The blind pass gives two statements to prove at once (Lemma CEN+, Theorem BH), one void
solution of condition (i) that sharpens it (Lemma MC), and ten candidates to write out. Nothing is "new" before
the comparison of Section 2.5.

### 2.5 Comparison with the earlier work (exercise step 5; rule 0a)

Search scope. (a) grep of `library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md`, `library/open-core.md` and
`FINISH.md` for: custodial, Fradkin, unitary gauge, Hubbard, quantum link, rotor, axial / tree / temporal / Landau
gauge, Gribov, Gauss law, overrelax, microcanonical, von Mises, Goldman, Jeffrey, diamagnetic, McBryan, complex
translation, isometry, homogeneous strength, exponential family, gluelump, static charge, Georgi, adjoint Higgs,
plaquette formulation, Batrouni, free ensemble, average over pins, conditional Neumann, single-link map, stabiliser,
Elitzur, rigid, residual gauge, global colour, zero-form, class angle, entropy functional, trace field, loop gas.
(b) Across branches: bare blob-less depth-1 fetch of `main` (8b11ae2bb9) and PR #10114 (f76f6c649c) into
`/tmp/row1016-git`; `git grep` for custodial, Fradkin, Elitzur, global symmetry, residual gauge, overrelax, von
Mises, Schrodinger functional, unitary gauge, global colour, non-abelian symmetry, zero-form, Gribov in the 67 `.md`
files of main with ym4d in the path and in 42 files of `agents/ym4d-proof/` picked by name. Hits: on main only
"unitary gauge" and "residual gauge" in the existence chain (Balaban's gauges); on PR #10114 two uses of global
colour invariance in coupling computations. No reformulation with a global symmetry, no custodial twist and no
Schrodinger-functional average on either branch. `library/open-core.md` lists no item of this row. A bounded
search gives "not found in the files searched", not "absent".

| Item of the blind pass | Already in the lane? | Where | Credit |
|---|---|---|---|
| C2, Lemma MC (single-link rotations about the staple as exact non-gauge symmetries; condition (i) needs "rigid") | partly: the von Mises-Fisher law of a link and overrelaxation are used in the lane's samplers; the reading as a void solution of condition (i) was not found | `gap-fctest-opus.md` L147 (sampler) | row 946 for the sampler |
| C3, Lemma CEN+ (arbitrary single-link maps) | partly: multipliers only | row 1011 Lemma CEN, Corollary CEN2; `gap-arealaw2-opus.md` 3.1 (stabiliser of a slab law under sitewise rotations) | rows 1011, 831 family |
| C4, Lemma REM | yes in substance | Lemma TWIST (row 1013 4.2); `gap-brainstorm-max.md` L283, L356 (idea 7: "One rotated boundary condition is a pure gauge and costs exactly nothing", with the squared-link-angle cost); `gap-crux-exercise-r858-max.md` L257 (C2) | rows 1013, 859, 858 |
| C5, auxiliary kernels | partly | row 1013 C7 (soft gauge kernel; "the frame decouples from every gauge-invariant observable"); `gap-outside-box-max.md` L146 (I10: fundamental Higgs as a larger theory, first reading S0); `gap-brainstorm-max.md` L406 (idea 33: the Higgs handle, continuation in kappa); `gap-tiltproof-max.md` L125-127 ((S4): gauge-Higgs form with a custodial background). Not found: the custodial twist response as a Wilson-loop series with non-negative coefficients | rows 1013, 1004, 859, 979 |
| Adjoint unit field | yes | `gap-outside-box-max.md` L147 (I11) and Lemma GG (kappa = infinity is compact U(1) exactly) | row 1004 |
| Layer comparison | yes | Durhuus and Frohlich; `gap-outside-box-max.md` L149 (I13); rows 712, 825, 831; Lemma SLAB (row 1013) | those rows |
| Hamiltonian with Gauss law | partly: as gap stability along a path (I14), and the gluelump reading of the Witten Laplacian on 1-forms (`gap-brainstorm-max.md` L299). Global colour on an unprojected space: not found | rows 1004, 859 |
| Hubbard-Stratonovich on quaternions | yes | `gap-brainstorm-max.md` L329 (idea 41 (c)) | row 859 |
| Complex translations | yes, as a recalled source | `prior/gap-gauge-stiffness-read-opus.md` L98-100 (M4, M5) | row 1012 |
| C7, plaquette variables and the Bianchi constraint | partly | `gap-skeleton-max-b.md` L215-220 (A12: FALSE as a route, because the Poincare inequality in the plaquette metric also holds for U(1)) and L581 ("the only interaction is the Bianchi constraint"); `gap-pca-opus.md` 5.1. Not found: the fibre count, and "every plaquette field v is a first-order move for SU(2), only exact v for U(1)" | rows 670, 967 |
| C8, Identity AV and Theorem BH | not found. Check 1014 (L104-109) names another route (omega = 1 minimises F_int), unproved | scope as above | - |

**What the fresh pass added (pending proofs below):** Lemma CEN+, Lemma MC with the sharpened condition "rigid",
Identity AV and Theorem BH, the loop-gas form of a kernel's twist response, the fibre count behind the angle moves.
**What it only found again:** Lemma REM, the Higgs field as a larger theory, the adjoint field, the layer
comparison, the quaternion Hubbard-Stratonovich idea, plaquette variables with the verdict of A12. Where the
earlier work is stronger I use it: A12's verdict (a covariance bound in the plaquette metric says nothing about
decay) is the test that candidate (ANG) must meet, and it is applied in Section 7.

## 3. Step 3: candidates with auxiliary fields (Task 1: identity, group, action, what it moves)

Notation. Quaternions: SU(2) = unit quaternions, Re q = (1/2) tr q, Im q in R^3 = su(2), <p, q> = Re(p-bar q) the
inner product of R^4. For a link l = (x -> y): U_l -> g_x U_l g_y^(-1). YM_beta is the Wilson measure
prop. to exp(beta sum_p t_p(U)) dU on a finite box or torus, t_p = Re U_p. L = number of links.
Marks: PROVED = proved by hand here, checked by no one.

### 3.0 Lemma AUX (what a symmetry of an added field can say; PROVED, three lines)

Let (Phi, d phi) be a measure space, K a group that acts on Phi and keeps d phi, and r(U, phi) >= 0 measurable with
N(U) = int r(U, phi) d phi in (0, infinity) and r(U, k phi) = r(U, phi). Put P(dU, d phi) = YM_beta(dU) r(U, phi) d phi / N(U).
(a) The U-marginal of P is YM_beta. (b) P is K-invariant, and K fixes every function of U. (c) For a subset of Phi
(a pin) and a map T of the pinned data, E_P of the twisted weight ratio equals E_YM[N^T_pin(U) / N_pin(U)]: the
expectation of a functional of U alone.
Proof. (a) Integrate phi. (b) r and d phi are invariant and K does not act on U. (c) Integrate phi at fixed U. QED

So every Ward identity of K is an identity for the conditional law of phi given U, integrated against YM_beta. It
contains no derivative of YM_beta in a direction that changes the gauge orbit of U. Reopen condition (i) asks for
a group that "moves gauge-invariant observables"; in this class K moves only observables that contain phi.

### 3.1 Candidate (H): frozen fundamental Higgs field, custodial SU(2)

**Identity H1 (the model and unitary gauge; DEF plus one change of variables).** Sites carry phi_x in SU(2).
h_l(U, phi) = Re(phi_x^(-1) U_l phi_y) = <phi_x, U_l phi_y>. GH(beta, kappa) has weight
exp(beta sum_p t_p(U) + kappa sum_l h_l) dU d phi. Gauge: phi_x -> g_x phi_x. Custodial K = SU(2): phi_x -> phi_x k^(-1).
With V_l = phi_x^(-1) U_l phi_y: t_p(U) = t_p(V), h_l = Re V_l, and (U, phi) -> (V, phi) keeps the Haar measures. K acts
by V_l -> k V_l k^(-1).

**Identity H2 (pure gauge theory, exactly; the kernel).** N_kappa(U) = int exp(kappa sum_l h_l(U, phi)) d phi is positive
and gauge invariant. By Lemma AUX with r = exp(kappa sum h_l): under P the field V has the law
  mu(dV) prop. to exp(beta sum_p t_p(V) + kappa sum_l Re V_l) / N_kappa(V) dV,
phi is uniform and independent of V, and E_YM[O(U)] = E_mu[O(V)] for every gauge-invariant O. So Wilson SU(2) is
the gauge-Higgs model in unitary gauge divided by the non-local factor N_kappa(V).

**Identity H3 (the local twist is a gradient; PROVED).** For f: sites -> R and a unit a in R^3 put k_x = e^(f_x a).
Then Re(k_x V k_y^(-1)) = Re(e^((f_x - f_y) a) V) = cos((df)_l) Re V + sin((df)_l) a . Im V, with (df)_l = f_y - f_x. The
map V_l -> k_x V_l k_y^(-1) keeps the Haar measure, every t_p and N_kappa. So in mu the localised custodial rotation
changes the weight only through df, on every configuration. This is property (M2) of row 1011 Section 2.
Proof. Re(AB) = Re(BA), and e^(theta a)(v_0 + v) has real part cos(theta) v_0 - sin(theta) a . v. QED

**Lemma HW (the first lemma: Ward identity with bracket, and blind bound; PROVED).** Fix U, any dimension, any
hopping strengths kappa_l in [0, kappa], any set of pinned sites. Write V_l = t_l + s_l. For a field F: sites -> R^3
put Delta_l F = F_x - F_y and J(F) = - sum_l kappa_l Delta_l F . s_l, the derivative of the hopping energy along
phi_x -> phi_x e^(-F_x).
(i) Re(e^(F_x) V e^(-F_y)) = t - Delta F . s - (1/2) |Delta F|^2 t - (F_x x F_y) . s + O(F^3).
(ii) If F vanishes on the pinned sites and F' is any field, then in the law of phi given U
  E[J(F) J(F')] = E sum_l kappa_l [ t_l Delta_l F . Delta_l F' - s_l . ((F_x + F_y) x Delta_l F') ].
For F = a f, F' = c g with a perpendicular to c the first (contact) term is zero and
  E[J_a(f) J_c(g)] = - E sum_l kappa_l (f_x + f_y)(g_x - g_y) (a x c) . s_l,
a current about the third axis. For one axis the bracket term vanishes.
(iii) For a twist f that does not vanish on the pins, the second derivative of - log N_pin(U; f) is
  H(f) = E sum_l kappa_l t_l (df)_l^2 - Var(J_a(f)) <= kappa sum_l (df)_l^2.
Proof. (i) Expand both exponentials to second order; Re(Fq) = Re(qF) = - F . Im q, Re(F^2 q) = - |F|^2 Re q,
Re(F_x V F_y) = Re(F_y F_x V) = - (F_x . F_y) t - (F_y x F_x) . s. (ii) The integral of
exp(A(phi e^(-delta F) e^(-eps F'))) over the free phi does not depend on delta (right translation by fixed elements).
Its mixed derivative at 0 is E[D_delta D_eps A] + E[J(F) J(F')] = 0. The delta eps coefficient of
Re(e^(eps F'_x) e^(delta F_x) V e^(-delta F_y) e^(-eps F'_y)) is Re(F'_x F_x V) + Re(V F_y F'_y) - Re(F'_x V F_y) - Re(F_x V F'_y)
= - t Delta F . Delta F' + s . ((F_x + F_y) x Delta F'). (iii) H3 and |t_l| <= 1. QED

Remark. Given U, the field phi with bond quaternion phi_x^(-1) U_l phi_y is a member of OpenAI's local class (fixed unit
quaternion on each bond, the symmetry on the other side), in any dimension. Lemma HW is their (3.5)-(3.8) in that
generality; nothing in it uses d = 2. The statements hold jointly in GH(beta, kappa) and in P as well, because K
does not act on U.

**Proposition LG (the twist response is a Wilson-loop series; PROVED; the diamagnetic inequality rebuilt).** Let eta
be a real field on links and N^eta_kappa(U) = int exp(kappa sum_l Re(e^(-eta_l a) phi_x^(-1) U_l phi_y)) d phi (no pins). Then
  N^eta_kappa(U) = sum over (n, pi) of prod_l (kappa^(n_l)/n_l!) prod_x c(m_x) prod over cycles gamma of 4 t_gamma(U) cos(eta(gamma)),
where n_l >= 0 are integers with even degree 2 m_x at each site, pi is a perfect matching of the half-edges at each
site, c(m) = 1/(4 . 6 ... (2m + 2)), the cycles gamma are the closed lattice walks traced by (n, pi), t_gamma = Re U_gamma,
and eta(gamma) is the signed sum of eta along gamma. All coefficients are non-negative. Hence |N^eta_kappa(U)| <= N_kappa(1),
N^(df)_kappa = N_kappa, and
  N^eta_kappa(U) = 1 + kappa^2 L/8 + (kappa^4/64) sum_p t_p(U) cos((d eta)_p) + (terms without U at order kappa^4) + O(kappa^6).
Proof. Re(e^(-eta a) phi_x^(-1) U phi_y) = <phi_x, T_l phi_y> with T_l = (left multiplication by U_l)(right multiplication by
e^(-eta_l a)) in SO(4). Expand each exponential. For the uniform measure on S^3 and vectors w_1, ..., w_2m in R^4,
E prod <phi, w_i> = c(m) sum over matchings of prod <w_i, w_j> (the Gaussian Wick rule divided by the radial moment
4 . 6 ... (2m + 2); odd moments vanish). Matching at every site turns the product into traces over R^4 of products of
T_l and T_l^T along closed walks. Left and right multiplications commute, so the trace along gamma is
tr(L_(U_gamma) R_(e^(-eta(gamma) a))) = 4 Re(U_gamma) cos(eta(gamma)) (the character of the representation (1/2, 1/2) of
SU(2) x SU(2)). The series converges absolutely: its terms are bounded by the terms at U = 1, eta = 0, which sum to
N_kappa(1). The low orders: one doubled link gives (kappa^2/2)(1/4); one plaquette gives kappa^4 (1/4)^4 . 4. QED

So the custodial response of the kernel is W(eta) = E_YM[N^eta_kappa/N_kappa], and at leading order in kappa
  - d^2/d eps^2 log W(eps eta) at 0 = (kappa^4/64) E_YM[t_p] sum_p (d eta)_p^2 + O(kappa^6).
It is a curl form in eta at every beta. Its coefficient is the mean plaquette, and at higher orders a sum of
Wilson loops weighted by kappa^(length) and by the squared flux of d eta through them.

**Verdict on (H): FAILS as a reopening, with the exact reasons.**
1. Condition (i), last clause. K moves no function of U (Lemma AUX). The observables it moves contain phi.
2. Slot (i) is filled, and trivially: H(f) <= kappa |df|^2 on every background (Lemma HW (iii)). But the response
   is a property of the probe field phi in a YM background (Proposition LG). At kappa -> 0 it is
   O(kappa^4) times the mean plaquette.
3. Slot (ii), the dimension. The cost form kappa |df|^2 is a Dirichlet form of a 0-form. A unit twist across a box
   of side R costs kappa R^(d-2): scale invariant in d = 2, growing like R^2 in d = 4. The shell sum of |k|^(-2)
   is a logarithm only in d = 2. ARGUED consequence: no gain per scale in d = 4. This agrees with the known
   order of the 4D O(4) model at large kappa in a flat background (Frohlich, Simon and Spencer; RECALLED).
4. Five dimensions (K7), valid form. For kappa below a constant that depends only on the dimension the field
   phi is in its high-temperature regime in every background (RECALLED: Dobrushin uniqueness, uniform in U; not
   rebuilt). So "the custodial response is small" is true in d = 5 at weak gauge coupling, where the gauge
   field is believed massless. A step "small custodial response implies decay of all observables" would be
   refuted there at belief level, and at theorem level by the product of GH with a Villain U(1) factor (Lemma PT).
5. As a comparison model, GH(beta, kappa) is row 1004's I10 and row 859's idea 33: the open step is uniformity as
   kappa -> 0, which is the crux at the pure end. Found again; no new input.

### 3.2 Candidate (N): a unit adjoint field and the U(1) about it

Kernel: M_kappa(U) = int exp(kappa sum_l n_x . Ad(U_l) n_y) dn, n_x in S^2. It is exact by Lemma AUX. The only maps of
S^2 that commute with all rotations are +-1, so the added field has **no continuous rigid group at all** (PROVED: a
map of S^2 commuting with SO(3) fixes or negates each point, by the stabiliser of the point). The moves
U_l -> e^(theta_l n_x) U_l keep the hopping term and change beta t_p by the curl of theta plus the frame defect of n
(Lemma FR of row 1011), and they change M_kappa(U), which is not gauge-related. The comparison model without
1/M_kappa is the Georgi-Glashow family, whose kappa = infinity end is compact U(1) exactly (Lemma GG, row 1004).
**FAILS; found again** (row 1004 I11; row 1011 7.3).

### 3.3 Candidate (HS): Hubbard-Stratonovich variables

**Identity HS1 (PROVED; a positive form).** For p with links l_1, ..., l_4 put A_p = U_1 U_2 and B_p = U_4 U_3 (the two
two-link paths from x to x + mu + nu). Then t_p = <A_p, B_p> = (1/2)|A_p + B_p|^2 - 1, and with gamma_beta the centred
Gaussian law on R^4 of covariance beta,
  exp(beta t_p) = e^(-beta) int gamma_beta(d w_p) exp(<w_p, U_1 U_2> + <w_p, U_4 U_3>).
So YM_beta is the U-marginal of a positive measure on (U, w), w_p a quaternion on the diagonal of p, with a
three-body weight on each of the two triangles of p. A second step, exp(<a, b>) = e^(-(|a|^2+|b|^2)/2) int gamma_1(d z)
exp(<z, a + b>) with a = U_1^(-1) w, b = U_2, makes every link appear linearly; the links then integrate to
prod_l Phi(|J_l|), Phi(r) = 2 I_1(r)/r > 0, J_l a sum of quaternion products of the Gaussian fields.
Proof. |A + B|^2 = 2 + 2 <A, B> for unit quaternions, and int gamma_beta(dw) e^(<w, v>) = e^(beta |v|^2/2). QED
Group: the gauge group acts on w_p by g_x w_p g_(x+mu+nu)^(-1) and on z likewise. There is no other rigid group: the
auxiliary fields sit on diagonals and corners and transform as links do. The radial part |w_p| is a random
plaquette coupling (Identity MIX of row 996 is the same device). **FAILS for (i): no group beyond the gauge
group.** Found again in kind (row 859 idea 41 (c), row 996).

### 3.4 Candidate (CH): characters, and plaquette variables with Bianchi constraints

The character expansion has discrete variables (spins on plaquettes, intertwiners on links): no continuous group.
In plaquette variables the Wilson weight prod_p exp(beta Re W_p) is invariant under W_p -> h_p W_p h_p^(-1) for
every p separately, a rigid on-site action of SU(2)^(plaquettes). The Bianchi constraints (one group-valued
equation per 3-cube, with transporters) are invariant only under the diagonal subgroup, which is global colour.
A localised conjugation violates a hard constraint. So the only rigid group is global colour, which moves no
invariant, and its twists are removable (Lemma REM, Section 4). **FAILS; found again** (A12 of row 670,
`gap-skeleton-max-b.md` L215-220 and L581; row 967 5.1).

### 3.5 Candidate (QL): rotor form, temporal gauge, quantum links

**Identity QL1 (DEF; exact on a time interval with free ends).** Fix U_4 = 1 by a gauge transformation (Jacobian
one). The variables are A_l(t), l a spatial link. The weight is
prod_t exp(beta sum_(spatial p) t_p(A(t))) prod_(l,t) exp(beta <A_l(t), A_l(t+1)>).
The kinetic factor is, for each spatial link, an O(4) chain in time with a rigid SU(2) x SU(2) acting on that link
alone. The magnetic factor breaks the product over links to the time-independent gauge group
G_3 = SU(2)^(spatial sites). So G_3 is a continuous non-abelian group that acts rigidly on the integration
variables, on-site in time. Its localisation g_x(t) changes only the kinetic factor, through g_x(t)^(-1) g_x(t+1):
a gradient in time, one chain per spatial site.
What it moves: no gauge-invariant observable (the gauge-invariant functions in this gauge are the G_3-invariant
ones). Its twist is a field of pinned temporal links. With free ends it is removable (Lemma TWIST). With pinned
ends it is the kernel of exp(-T H) without the Gauss projection, composed with a gauge transformation of one end:
the weights of sectors with static colour charges. ARGUED: these decay in T at a rate given by the energy of a
static charge, in every gauge theory of the class, compact U(1) included (a static charge has positive energy
there too). So the response is blind, and a small response says nothing about gauge-invariant correlations.
**FAILS at condition (i) (Elitzur) and at slot (iii).** Quantum link models are other models (finite link
spaces), not identities for the Wilson weight: no inequality to Wilson SU(2) is on record. **FAILS as stated.**

**Step 3 result.** Five candidates written with their identities. PROVED: Lemma AUX, Identity H3, Lemma HW,
Proposition LG, Identity HS1. All five FAIL the reopen condition. The nearest is (H): it has a rigid non-abelian
group, a local gradient twist, a bracket identity and a blind bound, on every gauge background. It fails because
the group acts on the probe only, and because its cost form is a Dirichlet form, which is scale invariant in two
dimensions and not in four.

## 4. Step 4: candidates without auxiliary fields, and three structural lemmas

### 4.1 Lemma CEN+ (every rigid on-site map of link variables is a gauge transformation times a centre field; PROVED)

**Statement.** Let p have links l_1, ..., l_4 with U_p = U_1 U_2 U_3^(-1) U_4^(-1) (row 1011 3.1). Let phi_1, ..., phi_4 be
arbitrary maps SU(2) -> SU(2) (no continuity, no group law, no measure) with
  Re(phi_1(U_1) phi_2(U_2) phi_3(U_3)^(-1) phi_4(U_4)^(-1)) = Re(U_1 U_2 U_3^(-1) U_4^(-1))   for all U in SU(2)^4.
Then there are g_x, g_(x+mu), g_(x+mu+nu), g_(x+nu) in SU(2) and signs sigma_i with product +1 such that
phi_i(U) = sigma_i g_tail(i) U g_head(i)^(-1). On a lattice in which the corner graph at each site is connected
(every box or torus of dimension at least 2), a family (phi_l) that keeps every plaquette trace is a gauge
transformation times a closed Z_2 link field.

**Proof.** Put M = U_4 U_3 U_2^(-1) and M' = phi_4(U_4) phi_3(U_3) phi_2(U_2)^(-1). Then Re U_p = Re(U_1 M^(-1)) = <M, U_1>, and
the hypothesis reads <M', phi_1(U_1)> = <M, U_1> for all U_1, ..., U_4.
Step 1. Take U_1 = M. Two unit vectors with inner product 1 are equal, so M' = phi_1(M):
  (*)  phi_4(U_4) phi_3(U_3) phi_2(U_2)^(-1) = phi_1(U_4 U_3 U_2^(-1))   for all U_2, U_3, U_4.
Step 2. So <phi_1(M), phi_1(U_1)> = <M, U_1> for all U_1 and all M in SU(2). With f_i = phi_1(e_i) for the basis
e_0, ..., e_3 = 1, i, j, k: the f_i are orthonormal, <phi_1(u), f_i> = <u, e_i>, and the squares of these numbers
sum to 1 = |phi_1(u)|^2. So phi_1(u) = sum <u, e_i> f_i: phi_1 is the restriction of some T in O(4).
Step 3 (classical fact, used as an input: every rotation of R^3 is conjugation by a unit quaternion). Let
c = T(1) and T' = c^(-1) T. T' fixes 1, so it maps Im H to itself by an element of O(3). If that element is
Ad(q), then T(u) = c q u q^(-1). If it is - Ad(q), then T(u) = c q u-bar q^(-1). So phi_1(u) = L u R^(-1) (proper) or
phi_1(u) = L u^(-1) R^(-1) (improper).
Step 4. Put two of the three variables in (*) equal to 1. Then phi_4 = phi_1 times a constant on the right,
phi_3 = constant . phi_1 . constant, and phi_2(u) = phi_1(u^(-1))^(-1) . constant. So all four maps have the same type.
Proper case: phi_i(u) = L_i u R_i^(-1), and (*) reads
  L_4 U_4 R_4^(-1) L_3 U_3 R_3^(-1) R_2 U_2^(-1) L_2^(-1) = L_1 U_4 U_3 U_2^(-1) R_1^(-1).
With U_3 = U_2 = 1: (L_1^(-1) L_4) U_4 = U_4 z for all U_4, with z constant. At U_4 = 1, z = L_1^(-1) L_4; then z commutes
with all of SU(2), so L_4 = +-L_1. Cancel U_4 and repeat with U_2 = 1: R_4^(-1) L_3 = +-1. Cancel U_3 and repeat:
R_3^(-1) R_2 = +-1 and R_1^(-1) L_2 = +-1. These are the four corners: l_1, l_4 share the tail x (g_x = L_1); l_1 ends
where l_2 starts (g_(x+mu) = R_1); l_2 and l_3 share the head (g_(x+mu+nu) = R_2); l_4 ends where l_3 starts
(g_(x+nu) = R_4). Putting the maps back in the hypothesis at U = 1 gives the product of the signs.
Improper case: (*) reads L_4 U_4^(-1) R_4^(-1) L_3 U_3^(-1) R_3^(-1) R_2 U_2 L_2^(-1) = L_1 U_2 U_3^(-1) U_4^(-1) R_1^(-1). Put U_3 = 1 and
P = R_4^(-1) L_3 R_3^(-1) R_2. With U_4 = 1: L_1^(-1) L_4 P = R_1^(-1) L_2 = eps = +-1. With U_2 = 1: L_1^(-1) L_4 = eps' = +-1 and
R_1^(-1) L_2 P^(-1) = eps'. So P = eps eps' and the identity becomes U_4^(-1) U_2 = U_2 U_4^(-1) for all U_2, U_4. This is false
(U_2 = i, U_4 = j). So the improper case does not occur.
Lattice statement: by the plaquette statement each phi_l is u -> L_l u R_l^(-1), and at each corner the two
link-end elements agree up to sign. A connected corner graph gives one g_x per site up to signs; the signs form a
link field whose product around each plaquette is +1. QED

**What it adds to Lemma CEN.** Row 1011 assumed multipliers U -> h U. Here the maps are arbitrary. So in link
variables there is no hidden rigid symmetry of any kind, continuous or discrete, beyond the gauge group and the
centre one-form symmetry. Remark (ARGUED, not written out): for a compact group G and the energy Re tr rho(U_p)
with rho faithful and irreducible, the same steps give phi_l(U) = L_l alpha(U) R_l^(-1) with alpha an automorphism of G
that keeps Re tr rho. For SU(N), N >= 3, complex conjugation is such an alpha; for SU(2) every automorphism is
inner.

### 4.2 Lemma REM (which colour twists of pinned data are removable; PROVED; Lemma TWIST for a general pin)

Let P be any set of pinned links with data u, the other links integrated, Z(u) the partition function. For every
site map g, Z(u^g) = Z(u) (gauge transformation of all links; row 1013 Lemma TWIST). Let P_B be a subset of P and k
in SU(2), and let u' be u with u_l replaced by k u_l k^(-1) for l in P_B. If no site is an end of both a link of P_B
and a link of P minus P_B, then u' = u^g with g = k on the sites of P_B and g = 1 elsewhere, so Z(u') = Z(u).
So a relative colour rotation of a union of connected components of the pinned graph costs nothing. A rotation of
part of one component changes the gauge orbit of the pin: it is a Schrodinger-functional deformation, the object
of row 1011 and of Section 7. Credit: rows 1013 (TWIST), 859 (idea 7), 858 (C2).

Consequence (C6 made exact). Pinned data are charged under global colour only relative to other pinned data in
the same connected component. A "colour twist between two pins" exists as a non-trivial response only if a pinned
path joins them. Then the response is the dependence of Z on the holonomy of that path: a correlation of field
strengths transported along a pinned line.

### 4.3 Lemma MC (exact, continuous, non-abelian symmetries that are not gauge transformations; PROVED)

**Statement.** Fix a link l with tail x and strengths beta_p >= 0. Write S(U) = Re(U_l Sigma_l) + S', where
Sigma_l = sum over p containing l of beta_p sigma_p, sigma_p the staple with U_(p, based at x, starting along l) = U_l sigma_p,
and S' does not contain U_l. On the set where Sigma_l is not 0 put Sigma-hat = Sigma_l/|Sigma_l| and, for k in SU(2),
  R_(l,k): U_l -> k U_l Sigma-hat k^(-1) Sigma-hat^(-1),   all other links fixed.
Then: (a) R_(l,k) keeps the Haar measure and S, so it keeps YM for every beta, and R_(l,k) R_(l,k') = R_(l,kk'): an
action of SO(3). (b) With W = U_l Sigma-hat = w_0 + w and q_p = Sigma-hat^(-1) sigma_p = q_(p,0) + q_p-vec:
t_p = w_0 q_(p,0) - w . q_p-vec, and under R_(l,k) the vector w turns by Ad(k) while w_0 and all q_p stay. So t_p changes
unless q_p-vec = 0 or w = 0, and sum_p beta_p q_p-vec = 0. (c) R_(l,k) R_g = R_g R_(l, g_x^(-1) k g_x) for a gauge transformation
R_g, so the average of F o R_(l,k) over k with a conjugation-invariant law maps gauge-invariant F to
gauge-invariant functions, and it is not the identity.
**Proof.** (a) For fixed other links the map is a left translation by k and a right translation by
Sigma-hat k^(-1) Sigma-hat^(-1), and Sigma-hat does not depend on U_l; Fubini gives the product Haar measure.
Re(U_l' Sigma_l) = |Sigma_l| Re(k W k^(-1)) = Re(U_l Sigma_l). (b) Re(U_l sigma_p) = Re(W q_p). (c) Under g, W -> g_x W g_x^(-1). QED

**Reading.** This is the conditional law of one link: a von Mises-Fisher law on S^3 about the staple direction,
with its SO(3) of rotations (the continuous form of an overrelaxation step). It shows that reopen condition (i)
as worded is met in a void way: a continuous non-abelian group, exact for every beta, on the integration
variables, moving gauge-invariant observables. It gives nothing, for the reason Elitzur's theorem gives: it is a
local invariance. Each R_(l,k) is separately a symmetry, so a "localised" version is again a symmetry and no cost
form exists. For compact U(1) the same group is the reflection about the staple (discrete). **The reopen
condition must read: a rigid group** (field-independent maps of on-site variables, a symmetry only when applied
everywhere with the same element), with pinned data that are charged under it in the sense of Lemma REM.
Lemma CEN+ then says: in link variables there is none.

### 4.4 Candidate (GF): gauge fixings with a global residual group

- **Tree gauge** (U_l = 1 on a maximal tree; Jacobian one; exact). Residual group: constant g, acting by
  conjugation on the other links. It is rigid and non-abelian. It moves no invariant. Its localisation
  U_l -> e^(f_l a) U_l e^(-f_l a) with a real field f on links has, in the theory without gauge fixing, the cost form
  (Lemma WN (iii) of row 1013 with F equal to f_l at both ends of l)
    E[X^2] = sum_p beta_p E[x_p] sum over corners (l, l') of p of (f_l' - f_l)^2.
  **Remark (a sharpening of row 1013's corner-graph sentence; PROVED given Lemma WN).** For general link-end
  fields the corner graph is one K_(2,2,2,2) per site. For conjugation fields the two ends of a link carry the same
  value, the graph on links is connected, and the cost form is a Dirichlet form on the lattice of links. So a
  gradient structure does exist for the localisation of global colour. It does not help: without pins the
  response is identically zero (the map keeps the Haar measure, so direct cost and variance cancel exactly); with
  pins it is removable or a Schrodinger-functional deformation (Lemma REM); and a Dirichlet form of a field on
  links is not scale invariant in d = 4 (a unit variation across a box of side R costs beta R^2).
- **Temporal gauge**: Identity QL1 of 3.5 and Identity HAM1 below.
- **A two-dimensional residual group.** Fix U_4 = 1 everywhere and U_3 = 1 on the hyperplane x_4 = 0 (Jacobian one;
  free ends). The residual transformations are g(x_1, x_2). For each z = (x_1, x_2) and mu in {1, 2} the field
  q_(z,mu)(x_3, x_4) = U_mu(z; x_3, x_4) is a two-dimensional chiral field with left group g_z and right group g_(z+mu);
  the (mu, 4) plaquettes are O(4) bonds without twist, the (mu, 3) plaquettes are O(4) bonds twisted on both sides by
  the in-plane fields, and the (1, 2) plaquettes couple four chiral fields at one point. This is the transverse
  lattice picture (Bardeen, Pearson and Rabinovici 1980; RECALLED). The residual group is rigid in the two long
  directions and non-abelian. It is a subgroup of the gauge group, so it moves no invariant; its localisation is
  a field of pinned in-plane links, and the response is a function of their gauge orbit. **FAILS (Elitzur).**
- **Landau gauge.** The minimal Landau gauge is defined by a global minimum; it is non-local and has Gribov
  copies, and its Jacobian is a Faddeev-Popov determinant on the fundamental region (RECALLED; not rebuilt).
  Its soft form is the kernel of 3.1 with kappa in place of 1/alpha (row 1013 C7 uses the divergence-squared
  functional). The residual group is global colour, as for the tree gauge. **FAILS; found again.**

### 4.5 Candidate (HAM): the Hamiltonian with Gauss law

On a torus, or a box with free ends, the physical space is the space of gauge-invariant functions of the spatial
links. A constant gauge rotation is a gauge transformation, so global colour acts on it as the identity. It acts
on the larger space without the Gauss projection.

**Identity HAM1 (PROVED).** Take a lattice periodic in time with T slices, all temporal links pinned to 1 except
those of one layer, pinned to k_x in SU(2) (x a spatial site). Let Z({k_x}) be the integral over the spatial links.
Then Z is a class function of each k_x, and
  Z({k_x}) = Z_YM sum over (j_x) of prod_x chi_(j_x)(k_x) E_YM[ prod_x chi_(j_x)(P_x) ],
where P_x is the Polyakov loop at x, the sum is over all assignments of spins j_x in {0, 1/2, 1, ...}, and Z_YM, E_YM
belong to the periodic theory with all links integrated.
Proof. A time-independent gauge transformation g keeps the integral and maps k_x to g_x k_x g_x^(-1): Z is a class
function of each k_x. Its Peter-Weyl coefficient at (j_x) is the integral of Z prod chi_(j_x)(k_x) over all k_x. Gauging
the other temporal links back from 1 to Haar-distributed links (Jacobian one) turns k_x into the Polyakov loop
and the integral into Z_YM E_YM[prod chi_(j_x)(P_x)]. QED

So the response of the unprojected theory to a colour twist in time is exactly the family of Polyakov-loop
correlators: weights of sectors with static charges. For large T each term with some j_x not 0 is small whenever
static charges have positive energy. ARGUED: that holds in compact U(1) at weak coupling too (the analogue of
HAM1 with characters e^(i n theta)), so the response is blind. It is slot (i) with nothing for slot (iii).
**FAILS.** Found again in part: row 1004 I14 treats the Hamiltonian as a path in g; the gluelump reading is
row 859 idea 20 (b).

### 4.6 Candidate (CMP): one-sided comparisons with a model that has the symmetry

- **Diamagnetic.** Z_GH(beta, kappa) = Z_YM(beta) E_YM[N_kappa] <= Z_YM(beta) N_kappa(1) (Proposition LG). The direction is
  fixed and the inequality is exact. It compares free energies only. No statement on correlations follows.
- **Layer comparison** (Durhuus and Frohlich). Given the other links, one layer of links of one direction is a
  chiral model one dimension down in a two-sided background. Its rigid group is the stabiliser of the
  background (`gap-arealaw2-opus.md` 3.1): the full group for a flat one-sided background (Lemma EMB of row
  1011), and Z_2 for a generic one. In d = 4 the layer is three-dimensional and orders at weak coupling for flat
  backgrounds (Lemma SLAB of row 1013, with a recalled theorem). **FAILS; found again.**
- **Complex translations** (McBryan and Spencer). For a holomorphic observable and a real one-axis link-end field
  F, the contour shift tau_(iF) is exact. For U(1) the Wilson loop gains the factor exp(-<theta, C>) pointwise. For
  SU(2) in the lab frame it gains nothing: at a free site the insertion e^(i theta a) = cosh(theta) + i a sinh(theta)
  averages over the gauge group to cosh(theta) >= 1, so E[x_p o tau_(iF)] = E[x_p] prod cosh(theta_(p,x)) (Lemma JEN (ii) of
  row 1013, continued to imaginary eta; both sides are entire), and the supremum of the shifted loop is at least
  cosh of the total shift (value at the trivial configuration). The fundamental representation contains both
  weights about any axis. A gain needs a colour frame, as every real twist does. **FAILS.**

**Step 4 result.** PROVED: Lemma CEN+, Lemma REM, Lemma MC, Identity HAM1, and the remark on conjugation
fields. All candidates of the list FAIL condition (i) in its rigid form. The common reason has two exact parts:
in link variables every rigid on-site map is a gauge transformation or a centre field (CEN+), and a colour twist
of pinned data is removable unless a pinned path carries it (REM).

## 5. Step 5: the tests (Task 2), in the valid form of the exercise skill

A model refutes a candidate only if the candidate's hypothesis holds there and its conclusion fails. Otherwise the
test says what a proof must use. "Elitzur" = does the group move a function of U alone. The slots are those of
row 1013 Section 2: (i) a response with a blind bound and gradient invariance, (ii) a bracket of trivial moves
with a scale-invariant cost, (iii) a step from small response to decay of all observables.

| Candidate | Elitzur, Lemma CEN+ | Compact U(1): gain must vanish | d = 5 | Lemma PT, Proposition NP | Theorem D2, Lemma SHEET, Lemma SLAB | Slots (i) / (ii) / (iii) | Verdict |
|---|---|---|---|---|---|---|---|
| (H) custodial SU(2) of a frozen fundamental field | fails: K fixes every function of U (Lemma AUX) | passes as a constraint: for U(1) the field phi_x in U(1) has a rigid U(1), a gradient twist and no bracket | the hypothesis "custodial response small" holds for small kappa in every dimension; the conclusion fails in d = 5 at belief level | PT: GH times a Villain U(1) factor has a small custodial response and no seed, so a step (iii) that reads phi only is refuted at theorem level (given the U(1) theorem). NP not reached | as a class over all backgrounds: at U = 1 the field phi is the 4D O(4) model, ordered at large kappa (RECALLED); so a uniform statement needs small kappa, where it is trivial | (i) yes, H <= kappa abs(df)^2 (Lemma HW); (ii) bracket yes, scale-invariant cost no in d = 4; (iii) no | FAILS (PROVED parts: AUX, HW, LG) |
| (N) adjoint unit field | no continuous rigid group on the field (3.2) | - | - | - | kappa = infinity is compact U(1) (Lemma GG, row 1004) | none | FAILS |
| (HS) Gaussian quaternion fields | gauge group only | same form for U(1) with complex Gaussian fields | no input | - | radial parts are coupling fields: Lemma SHEET binds any statement uniform in them | none | FAILS |
| (CH) characters; plaquettes with Bianchi | discrete; or global colour only | for U(1) the constraint is linear and the dual is a gauge theory with the one-form symmetry | - | - | - | none | FAILS |
| (QL), (HAM) temporal gauge, group G_3 | fails: G_3 is a subgroup of the gauge group | the U(1) form of HAM1 has the same content | no input | the response reads static charges, not the spectrum of gauge-invariant states | - | (i) yes, blind; (ii) a gradient in one direction only; (iii) no | FAILS (PROVED: QL1, HAM1) |
| (GF) tree gauge, global colour | fails | abelian: trivial action | - | - | - | response identically 0 without pins | FAILS |
| (GF) two-dimensional residual group | fails | same | - | - | contains the sheets of Theorem D2 as conditional laws | none | FAILS |
| (CMP) diamagnetic | - | holds for U(1) too | holds in every d | - | - | free energies only | FAILS |
| (CMP) layer comparison | rigid group = stabiliser of the background | - | - | - | Lemma SLAB: the 3D layer orders | hypothesis false at weak coupling | FAILS |
| (CMP) complex translations | needs a colour frame (cosh factors) | U(1): gives the perimeter law, which is the truth there | - | - | - | one abelian direction, no bracket | FAILS |
| (MC) single-link rotations about the staple | moves invariants, but is a local invariance | U(1): a reflection | every d | - | - | no cost form, so no slot (i) | void (PROVED: Lemma MC) |

No test had to be bent. Two tests gave more than a verdict. The U(1) column shows again the split of row 1011:
the rigid group with a gradient twist exists where the bracket vanishes, or on a probe. The d = 5 column kills
(H) in the valid form: its hypothesis is true there for a blind reason.

## 6. Step 6 (Task 3): no survivor for condition (i); the lemmas that close it, and the condition in its exact form

### 6.1 What was proved for and against

- For the nearest candidate (H) the "first lemma" exists and is proved: Lemma HW (Ward identity with bracket term
  and blind bound H <= kappa |df|^2 on every gauge background, every dimension) with Proposition LG (the response
  as a Wilson-loop series with non-negative coefficients). They are statements about the probe field.
- Against condition (i): Lemma AUX (a group on an added field fixes every function of U), Lemma CEN+ (no rigid
  on-site map of link variables beyond gauge and centre), Lemma REM (colour twists of pins are removable unless
  a pinned path carries them), Identity HAM1 (the colour response in temporal gauge is the family of Polyakov
  loop correlators), Lemma MC (the literal condition has a void solution).

### 6.2 The reopen condition, corrected (a filter correction; ARGUED from the lemmas above)

Row 1013's condition (i) reads "a continuous non-abelian group acts as a global symmetry on the integration
variables and moves gauge-invariant observables". Lemma MC meets it and gives nothing. The condition that the 2D
engine uses has three parts, and each must be stated:

(R-a) **Rigid.** The group acts by field-independent maps of on-site variables and is a symmetry only as a whole.
Then its localisation has a cost form.
(R-b) **Charged pins.** There is a class of pinned data, closed under the conditioning that the iteration uses,
on which the group acts and cannot be undone by a change of the integrated variables.
(R-c) **On the gauge-invariant algebra.** The response to the twist is a derivative of the Wilson measure in a
direction that changes the gauge orbit, not a conditional response of an added field.

Status of each part for pure SU(2), on record after this row:
- (R-a) in link variables: only the gauge group and the centre (Lemma CEN+, PROVED). In variables with an added
  field: rigid groups exist, for example the custodial group (3.1).
- (R-b): for colour, pins are charged only along pinned paths (Lemma REM, PROVED). For an added field with a
  rigid group, pins of the added field are charged (3.1), and (R-c) fails (Lemma AUX, PROVED).
- (R-a), (R-b), (R-c) together: no candidate. This is "not found in the ten families of Sections 3 and 4", not
  a theorem that none exists. The families cover the row's seeds: auxiliary fields with a custodial group,
  Hubbard-Stratonovich and character variables, rotor and quantum-link forms, gauge fixings with a global
  residual group, the Hamiltonian with Gauss law, and one-sided comparisons.

### 6.3 Why no general theorem is claimed

A general no-go would need a definition of "exact reformulation". With none, the claim is false as stated:
Lemma MC and every Gibbs sampler give measure-preserving maps of the orbit space. With "the new variables are
link variables and the maps are on-site and rigid" it is Lemma CEN+. With "an added field and a group on it" it
is Lemma AUX. A statement between these two is OPEN and is not attacked here; no consumer needs it.

## 7. Step 7: the homogeneous-strength case of Proposition B' (proved), and reopen condition (ii)

### 7.0 Pre-registration of a GUIDE control (written before the run; a run may refute or guide, it proves nothing)

Script `/tmp/row1016-scripts/bh_control.py` (plain Python, no numpy; kept beside its output
`/tmp/row1016-scripts/bh_control.out`). Model: the open box {0,1,2}^3 with all 54 links integrated, weight
exp(b sum_p w_p t_p), w_p = 1/2 in the boundary faces and 1 elsewhere, b = 1 and b = 3; heat bath; 100,000 sweeps
after 300; blocked errors (40 blocks). Boundary plaquette p_0 = ((0,0,0); 1, 2), site z = (1,0,0), field
B = a d lambda_z on the four boundary links at z, X = D_B A, psi = D_B t_(p_0) (central differences, step 1e-4;
second difference with step 1e-3; step-halving printed). The identities under test are dimension-free, so a
three-dimensional box is a valid control of the algebra. Readings fixed now:
- C1: E[X psi] - 2 E[t_(p_0)] is 0 within 3 standard errors.
- C2: E[psi^2] - (2/3) E[1 - t_(p_0)^2] is 0 within 3 standard errors.
- C3: E[X^2] + E[D_B^2 A] is 0 within 3 standard errors.
- C4: the nested estimate of E_free[(E_omega X)^2] (500 pins from the chain; for each, the 6 interior links are
  resampled in two independent runs of 300 sweeps and the two means are multiplied) is at least
  6 E[t_(p_0)]^2 / E[1 - t_(p_0)^2] minus 3 standard errors.
A failure of C1-C3 beyond 5 standard errors means an error in the algebra of 7.2. A failure of C4 means an error
in Identity AV or in the Cauchy-Schwarz step. A pass decides nothing.

### 7.1 Identity AV (the free-ensemble mean of the pinned stiffness; PROVED)

Setting and notation of row 1011 3.1-3.2: a box c, pin omega on the boundary links, A_c = sum_p beta_p w_p t_p,
Z_c(omega) the integral over the interior links, F_c = - log Z_c, and for a field B on the boundary links
H_c(omega; B) = d^2/d eps^2 F_c(e^(eps B) omega) at 0, X_c(B) = d/d eps A_c(e^(eps B) U) at 0 with B extended by zero.
E_omega is the pinned expectation. **E_free** is the expectation in the same box with all links integrated; under it
the boundary links have density Z_c(omega)/Z_free with respect to Haar measure.

**Statement.** For every box, every strength field, every gauge group and every fixed boundary field B:
  E_free[ H_c(.; B) ] = E_free[ (E_omega X_c(B))^2 ] >= 0.
**Proof.** Z(eps, omega) = Z_c(e^(eps B) omega) is smooth and positive, and its integral over the pins does not depend on
eps (left translation of each boundary link by a fixed element). So the integral of the second eps-derivative of Z
over the pins is 0. With F = - log Z: F'' = - Z''/Z + (Z'/Z)^2, hence int Z F'' d omega = int Z (F')^2 d omega. Divide by
Z_free. Last, Z' = Z E_omega[X_c(B)], so F' = - E_omega[X_c(B)]. QED

**Corollary AV2 (the mean over pins is blind to colour coherence; PROVED given Proposition A (iii) of row 1011).**
Write X_c(B) = - sum over boundary links of B_l . N_l and n_l(omega) = E_omega[N_l]. For a unit a and a real boundary field
theta,
  E_free[ H_c(.; a theta) ] = (1/3) sum over boundary sites x of E_free | sum over boundary links l with tail x of theta_l n_l |^2.
Proof. N_l(U^g) = Ad(g_tail(l)) N_l(U) (from D_B A(U) = D_(Ad_g B) A(U^g)), so n_l(omega^g) = Ad(g_tail(l)) n_l(omega), and the
free ensemble of pins is invariant under omega -> omega^g. Average over independent Haar elements g_x: terms with
different tails vanish, and int (a . Ad(g) u)(a . Ad(g) v) dg = u . v/3. QED
So the mean response to a fixed-colour field is a site-diagonal form in theta: no derivative of theta appears. This
is the averaged form of Proposition B of row 1011. Replacing the supremum over pins by a gauge-invariant
average over pins does not restore the colour coherence (assumption A4 of 2.3).

### 7.2 Theorem BH (Proposition B' holds for homogeneous strengths; PROVED, with an explicit constant)

**Statement.** Let c = prod {0, ..., S_mu} in dimension d >= 3 with all S_mu >= 1, and beta_p = b > 0 on every
plaquette (weights w_p as in row 1011). Let p_0 = (x; mu, nu) be a boundary plaquette, z = x + mu, lambda the indicator
of z, a a unit vector, and B = a d lambda on the boundary links ((d lambda)_l = lambda(head) - lambda(tail)). Then
  sup over pins of H_c(omega; B) >= E_free[H_c(.; B)] >= 6 (E_free t_(p_0))^2 / E_free(1 - t_(p_0)^2).      (BH)
There is a boundary plaquette with E_free t_(p_0) > 0, for every b > 0. The boundary field theta = d lambda has the
extension d lambda with zero curl on every plaquette. So for homogeneous strength there is no constant K with
H_c(omega; a theta) <= K inf over extensions of sum_p w_p (d theta~)_p^2 for all pins and all real boundary fields theta.
Moreover the right side of (BH) tends to infinity as b -> infinity at a fixed box, at least like b/log b.
(BH) holds for every strength field; only the last two sentences use that the strengths are homogeneous.

**Proof.** Step 1. The supremum is at least the mean, and the mean is E_free[(E_omega X)^2] by Identity AV, X = X_c(B).
Step 2. psi = d/d eps t_(p_0)(e^(eps B) U) at 0 depends only on the links of p_0, which are boundary links. So psi is a
function of the pin, E_free[psi E_omega X] = E_free[psi X], and by Cauchy-Schwarz
  E_free[(E_omega X)^2] >= (E_free[psi X])^2 / E_free[psi^2].
Step 3. In the free model the map U -> e^(eps B) U (B extended by zero) keeps the Haar measure, so the integral of
exp(A_c(e^(eps B) U)) psi(e^(eps B) U) does not depend on eps. Its derivative at 0 gives
E_free[X psi] = - E_free[D_B psi], with D_B psi = d^2/d eps^2 t_(p_0)(e^(eps B) U) at 0.
Step 4 (the plaquette). On p_0: B_1 = a (the head of l_1 is z), B_2 = - a (the tail of l_2 is z), B_3 = B_4 = 0. Put
V = U_2 U_3^(-1) U_4^(-1), so U_p = U_1 V, and a' = Ad(U_1) a, t = Re U_p, s = Im U_p. Then
t_(p_0)(e^(eps B) U) = Re(e^(eps a) U_1 e^(-eps a) V), and with Re(v q) = - v . Im q and a a' = - a . a' + a x a':
  psi = Re(a U_p) - Re(a' U_p) = - (a - a') . s,
  D_B psi = Re(a^2 U_p) - 2 Re(a a' U_p) + Re(a'^2 U_p) = - 2 t + 2 (a . a') t + 2 (a x a') . s.
(These are - delta . s and - (|delta|^2 t + kappa . s) of Proposition A with delta = a - a', kappa = - 2 a x a'.)
Step 5 (gauge averages; the free model is invariant under the gauge group at every site of c). The gauge
transformation h at x maps s -> Ad(h) s, a' -> Ad(h) a', and keeps t and a' . s. The Haar mean of Ad(h) v is 0 and
that of (Ad(h) v)_i (Ad(h) w)_j is (v . w/3) delta_ij. So E[(a . a') t] = 0, E[(a x a') . s] = 0 (the trace of v -> a x v is
0), E[(a . s)(a' . s)] = 0 and E[(a . s)^2] = E|s|^2/3. The gauge transformation h' at z maps U_1 -> U_1 h'^(-1),
U_2 -> h' U_2, keeps U_p, and maps a' . s to (Ad(h'^(-1)) a) . (Ad(U_1^(-1)) s); so E[(a' . s)^2] = E|s|^2/3. Hence
  E_free[X psi] = 2 E_free[t],   E_free[psi^2] = (2/3) E_free|s|^2 = (2/3) E_free[1 - t^2].
Steps 1-5 give (BH).
Step 6 (a boundary plaquette with positive mean). Let l_e be the link from the corner 0 along axis 1. The
plaquettes that contain it are (0; 1, nu), nu = 2, ..., d; each lies in a boundary face (x_rho = 0 for a third
direction rho; this uses d >= 3). Given the other links, U = U_(l_e) has density prop. to exp(Re(U Sigma)) with
Sigma = sum_nu b w_nu sigma_nu, and Re(U Sigma) = sum_nu b w_nu t_((0;1,nu)). With c = Re(U Sigma-hat) the conditional mean of c is
int c e^(rc) (1 - c^2)^(1/2) dc / int e^(rc) (1 - c^2)^(1/2) dc with r = |Sigma|, which is > 0 for r > 0 (pair c with - c).
Sigma is continuous and equals b sum w_nu at the trivial configuration, so r > 0 with positive probability. Hence
sum_nu b w_nu E_free t_((0;1,nu)) > 0 and one of these boundary plaquettes has E_free t > 0. Label it (0; 1, nu), z = e_1.
Step 7 (large b). Let phi(b) = log int exp(- b sum_p w_p (1 - t_p)) dU and e(b) = - phi'(b) = E_free[sum_p w_p (1 - t_p)]. phi is
convex and phi <= 0 = phi(0), so (b/2) e(b) <= phi(b/2) - phi(b) <= - phi(b). On the set where |U_l - 1| <= r for all links
(r <= 1): |U_p - 1| <= 4 r, so 1 - t_p = (1/2)|U_p - 1|^2 <= 8 r^2; the Haar measure of {|U - 1| <= r} is at least
(2/pi) int_0^r sin^2 >= 8 r^3/(3 pi^3). With r = b^(-1/2), b >= 1, W = sum_p w_p and L links:
phi(b) >= - 8 W - L log(3 pi^3/8) - (3 L/2) log b, so e(b) <= (16 W + 4.92 L + 3 L log b)/b. For every plaquette
E_free(1 - t_p) <= e(b)/w_p <= 2^(d-2) e(b), E(1 - t^2) <= 2 E(1 - t), and the right side of (BH) is at least
3 (1 - 2^(d-2) e(b))^2 / (2^(d-2) e(b)). QED

**Corollary BH2 (every fixed-colour boundary field; PROVED).** For a real boundary field theta and a boundary
plaquette p write theta_(p,y) for the corner twists of B = a theta (with row 1011's labels they are theta_1 - theta_4 at x, theta_2
at x + mu, theta_3 at x + nu, 0 at x + mu + nu) and m_p(theta) = sum_y theta_(p,y)^2. Let Q be any set of boundary plaquettes with
E_free t_p > 0, and n_Q the largest number of plaquettes of Q with a non-zero corner twist at one site. Then, for
every strength field,
  sup over pins of H_c(omega; a theta) >= E_free[H_c(.; a theta)]
      >= 3 (sum over Q of E_free[t_p] m_p(theta))^2 / ( n_Q max over Q of E_free[1 - t_p^2] sum over Q of m_p(theta) ).
Proof. As Steps 1-3 with psi = sum over Q of D_B t_p. By Lemma WN (i) of row 1013, D_B t_p = - sum_y theta_(p,y) a . s_(p,y),
with s_(p,y) the imaginary part of the holonomy of p based at y. The gauge average at y kills every product of
terms at two different sites and gives (1/3) s_(p,y) . s_(q,y) at one site. So E_free[X psi] = sum over Q of E_free[t_p] m_p
(Lemma WN (iii) for one plaquette), and E_free[psi^2] = (1/3) sum_y E_free | sum over Q of theta_(p,y) s_(p,y) |^2, which by
Minkowski's inequality and |s|^2 = 1 - t^2 is at most (1/3) max E(1 - t^2) n_Q sum over Q of m_p. QED
For Q = {p_0} and theta = d lambda_z this is (BH). The functional sum_p m_p(theta) is the one of row 1011's second bound in
Proposition B' (L242-243). So that bound holds for homogeneous strengths with b replaced by a ratio of plaquette
means of the free box. ARGUED only: that this ratio is bounded below uniformly in the size of the box at fixed b
(it needs lower bounds on E_free t_p for boundary plaquettes that do not depend on the size).

**What this closes.** Check 1014 (defect 1) left the physical Schrodinger-functional class (homogeneous bare
coupling, all Dirichlet data) refuted at ARGUED level only, and named an unproved route (omega = 1 minimises
F_int). Theorem BH proves the failure of a pin-uniform curl bound in that class for every b > 0, without that
minimisation, and gives a lower bound that grows with b. It does not give row 1011's ARGUED growth in the cell
size ("at least of order b S"): that statement stays ARGUED. Family G1 of row 1011 9.8 is now retired by proof for
homogeneous strengths as well. Theorem BH says nothing about the trivial pin: the Schrodinger-functional bound
H_c(1; a theta) <= b times the classical action stays OPEN (row 1011 4.4).

### 7.3 Result of the control pre-registered in 7.0 (GUIDE; run 2026-11-15 20:25-20:26Z under the numeric lock)

Memory free 63 percent at the start. Output `/tmp/row1016-scripts/bh_control.out`. Step-halving changed X, psi and
the second difference by less than 1e-9, 2e-9 and 6e-7.

| b | E t_(p_0) | C1: E[X psi] - 2 E[t] | C2: E[psi^2] - (2/3) E[1 - t^2] | C3: E[X^2] + E[D_B^2 A] | C4: nested E_free[(E_omega X)^2] | bound of (BH) | E[X^2] |
|---|---|---|---|---|---|---|---|
| 1 | 0.1248(15) | -0.0011(32) | 0.0004(20) | -0.0032(33) | 0.243(19) | 0.126 | 0.2488(12) |
| 3 | 0.3610(11) | -0.0014(42) | 0.0002(19) | -0.0015(154) | 2.12(14) | 1.148 | 2.164(11) |

All four readings pass at both couplings as pre-registered (C1-C3 within one standard error of zero; C4 above
the bound by 6 and 7 standard errors). The run did not refute the algebra of 7.2. It decides nothing.

### 7.4 Reopen condition (ii): covariant moves, Jacobian, curl form

Three exact statements locate it. None gives a survivor.

**(a) One-axis moves along a frame: a curl-form cost forces a reducible field (PROVED from Lemma FR's identity).**
Let n be a unit-vector field on sites and B = theta_l n_tail(l). By row 1011 7.3 ("Use"), for theta = d lambda the field B is
a gauge direction plus the field lambda_head(l) D_l n. So "the direct cost of theta n vanishes for every closed theta" holds
on a configuration only if D_l n = 0 on every link, and then by Lemma FR every plaquette axis at every site is
parallel to n (NA = 0). At a response of order one the non-abelian part is of order one per site (ARGUED size,
row 1011 7.3). So the cost form of a frame move is not a curl form pointwise, for any frame, field-dependent or
not. What is left is a cancellation against the current variance: items (N1)-(N3) of row 1011 7.4, OPEN, of the
first-passage kind.

**(b) Lemma GT (holonomy-axis twists: the only frame that is covariantly constant at every coupling lives on
curves; PROVED).** Let alpha be a closed lattice path through distinct sites y_0, ..., y_(m-1) such that no other
lattice link joins two of its sites, h_i its holonomy based at y_i, and, where h_0 is not +-1, n_i = Im h_i/|Im h_i|.
Then n_i = Ad(u_i) n_(i+1) for the transporter u_i of the link from y_i to y_(i+1): the axis is covariantly constant
along alpha, at every coupling. Let E be a set of link-ends (l, y_i) with l not in alpha, and tau_t the map that multiplies
U_l by e^(t n_i) on the left if y_i is the tail of l and by e^(-t n_i) on the right if y_i is its head, for (l, y_i) in E.
(i) tau_t keeps the Haar measure (the multipliers depend only on links of alpha, which do not move), and it is a
one-parameter group. (ii) A plaquette that contains a link of alpha and the legs e at y_i, e' at y_(i+1) changes by the
insertion e^(t (1_E(e') - 1_E(e)) n_i); a plaquette with a corner at y_i and no link of alpha changes by
e^(t (1_E(e') - 1_E(e)) n_i) for its two link-ends there. (iii) In d = 2, with alpha a simple closed curve and E the
link-ends on one side, every plaquette trace is invariant: tau_t is an exact symmetry of every action that is a
sum of class functions of single plaquettes, it is not a gauge transformation, and twists along crossing curves
do not commute. This is Goldman's twist flow on the lattice (Goldman 1986; RECALLED for the name only). (iv) In
d >= 3 every E that is neither empty nor complete at a site cuts corners there. If each plaquette has at most
one cut corner, then with X = sum over cut corners of (+-) beta_p n_i . s_(p, y_i):
  E[X] = 0 and E[X^2] = sum over cut corners of beta_p E[t_p].
Proof. h_i = u_i h_(i+1) u_i^(-1) gives the axis rule. (i) Fubini. (ii) U_l e^(t n_(i+1)) = e^(t n_i) U_l for the link of alpha.
(iii) follows from (ii). (iv) Along the flow n does not change, a single insertion gives
Re(e^(theta n) U_(p,y)) = cos(theta) t_p - sin(theta) n . s_(p,y), and the integral of exp(S o tau_t) does not depend on t; take two
derivatives at 0. QED
Reading. The rigid-symmetry structure of the 2D engine does exist in a gauge theory, exactly and at every
coupling, on one-dimensional sets: the axis of a loop's own holonomy. A twist along it has Jacobian one. In
d >= 3 its cost is a line of corner terms, one-dimensional, with the white-noise sum rule (iv), which holds for
U(1) too. A surface has no such axis unless the field on it is reducible. So (ii) fails by dimension, not by
the Jacobian.

**(c) Lemma SOFT and Identity CUBE (the Bianchi constraint on class angles is soft for SU(2); PROVED).** For the
twelve links of one 3-cube under Haar measure, the class angles phi_1, ..., phi_6 of the six plaquettes have the joint
density
  r(phi) = (2/pi)^6 prod_i sin(phi_i) sum over k >= 1 of k^(-4) prod_i sin(k phi_i)   on [0, pi]^6,
a continuous function. At the centre c = (pi/2, ..., pi/2): r(c) = 2/(3 pi^2) > 0, the gradient of log r is 0, and
the Hessian of log r is - (1 + 12/pi^2) times the identity. Consequently there is a configuration of the cube at
which the differential of the map U -> (t_1, ..., t_6) is onto: every first-order change of the six traces is made
by a link field. For compact U(1) the six angles satisfy one linear equation and the image is a hyperplane.
Proof. With chi_k(phi) = sin(k phi)/sin(phi), d mu = (2/pi) sin^2 and a_k(beta) = int e^(beta cos) chi_k d mu, the character expansion
and the gluing rule int chi_j(A U) chi_k(U^(-1) B) dU = delta_jk chi_j(AB)/j give, for six couplings,
Z(beta_1, ..., beta_6) = sum_k k^2 prod_i (a_k(beta_i)/k) (for equal couplings this is the lane's formula,
`gap-skeleton-max-b.md` L581). The series sum_k k^(-4) prod chi_k(phi_i) prod sin^2(phi_i) converges absolutely to a bounded
function with the same Laplace transform in the variables cos phi_i; a finite measure on a compact set is fixed by
its Laplace transform. At c only odd k contribute: sum over odd k of k^(-4) = pi^4/96. For the Hessian, with
P = prod sin and Q the series: the first derivatives of P and Q vanish at c (cos(pi/2) = 0; for odd k,
cos(k pi/2) = 0; for even k the other factors vanish), the mixed second derivatives vanish for the same reason,
and the pure ones are - 1 and - (sum over odd k of k^(-2))/(pi^4/96) = - (pi^2/8)(96/pi^4). The image of the trace map
has positive measure near c, so by Sard's theorem it contains a regular value. QED
Reading (ARGUED). On a 4D torus of N sites the gauge orbits have dimension 9N and there are 6N plaquettes, so
the same holds generically with fibres of dimension 3N; this count is not proved here. So SU(2) has
"angle moves": covariant link fields that change the class angles of chosen plaquettes and no others, which
do not exist for U(1). Along them the Wilson weight changes exactly as in an abelian theory, plaquette by
plaquette. Their Jacobian is the change of r, a beta-independent entropy of the Bianchi constraint. This is the
exact form of "covariant moves with a controlled Jacobian": the cost form is abelian at every response, and
the whole problem moves into the Hessian of log r. Tests. Row 670's verdict on plaquette variables
(`gap-skeleton-max-b.md` L215-220) binds: a bound on the covariance of the angle field in its own metric holds
for a massless photon too and says nothing about decay. Five dimensions: the same structure, no dimension-4
input. Consumer: none. **FAILS as a route; the two exact statements are constraints.**

**Step 7 result.** PROVED: Identity AV, Corollary AV2, Theorem BH (the homogeneous-strength case of Proposition B',
every b > 0, with constant 6 (E t)^2/E(1 - t^2) and growth at least b/log b at a fixed box), Lemma GT,
Lemma SOFT with Identity CUBE. A GUIDE control of the algebra of BH passed. Reopen condition (ii): FAILS in the
pointwise form (Lemma FR); its averaged form is (N1)-(N3) of row 1011, OPEN and not attacked; the two other
readings (holonomy-axis twists, angle moves) are exact and have no consumer.
