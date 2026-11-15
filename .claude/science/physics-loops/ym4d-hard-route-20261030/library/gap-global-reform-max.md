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
