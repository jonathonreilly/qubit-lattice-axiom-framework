lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:03Z

# gap-mini-solve-f-fable: the mass gap of four-dimensional SU(2) Yang-Mills

Queue row 1195. Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit 9c5f9600f. Started 2026-11-20T00:03Z.

Labels used below: PROVED (every step written here or in a cited library file), ARGUED (an argument with a named missing step), GUIDE (heuristic or numeric, not a proof step), OPEN.

Status of this file: in progress. Sections are appended one step at a time.

## 0. Log

- 00:03Z. File created. Reading FINISH.md (rules, row 1195), GOAL.md, `parts/gap.md`, and the earlier gap-mini results.
- 00:25Z. Read in full: GOAL.md; FINISH.md L1-84 and L299-356 (rules); row 1195; `parts/gap.md` (all 322 lines); `library/gap-council-brief.md`; `library/gap-council-synthesis.md`; the FINISH RESULT lines of rows 1177-1196. Not read: the other 460 `library/gap-*` files (searched by grep when a statement is used).

## 1. Repo search: where the lane stands (what I rely on, by row)

All of this is prior work of the lane; none of it is mine. Credit: Balaban (ultraviolet renormalization group), Sussman and Alpoge with Claude and Codex (the complete account), the lane's rows as cited.

- Target. Jaffe-Witten for SU(2): a Wightman/OS theory on R^4 with spectrum {0} and [Delta, infinity). Lattice form: Wilson SU(2) on periodic tori along the asymptotically free trajectory (brief, Section 1).
- Consumer side, on file: one seed at one physical box size gives a uniform gap on all larger dyadic boxes and carries to finer cutoffs (Theorems S, SH, rows 697-705; Theorem ZD-c, row 720). The wall (W): bounded Casimir excess (BDD-Delta) together with unbounded size-times-gap (Z-UNB).
- The gap clause alone needs less (rows 731, 1161, 1179 Theorem BP, unchecked in part): the one-cube physical neutral bound (N-phys) plus the continuum datum. By rows 1180 and 1184 (checked by row 1187), (N-phys) is a neutral lattice gap at arbitrarily weak coupling with a lower bound of asymptotic-scaling type.
- Every positive result on file is non-selective (it also holds for compact U(1), a frozen group, or a product with a massless factor). The missing piece is one selective inequality at order-one effective coupling (brief, Section 3).
- The sibling rows with this same plain brief (1188-1190; 1193, 1194 running) screened 12 to 17 standard attacks each and found all on file.

Consequence for this row: a further screening of standard routes has no value. This row picks one mechanism, checks it against the record by grep, and works it to a proof or to its first failing step.

## 2. How best to attack it (step 1; written 00:35Z)

### 2.1 What a proof has to contain (ARGUED, from the record)

1. The only posted mechanism that crosses an order-one band in an asymptotically free model is OpenAI's stiffness iteration for the 2D O(4) model (read by row 1009, `library/prior/gap-o4-pinned-cell-read-opus.md` L57-200). Its parts are: (a) a rigid continuous symmetry; (b) the stiffness of a pinned cell as "direct cost minus current variance", with the start bound "drop the variance", uniform over all pins; (c) a lower bound on the current variance from the bracket term of the Ward identity (a Cramer-Rao step); (d) small stiffness gives decay of charged observables; (e) neutral observables by association.
2. For 4D SU(2) the port of (b) fails. Row 1011 (`library/gap-pinned-cell-gauge-max.md` Propositions A, W, B, B', SEAG, Lemma FR) proves: the direct term of a fixed-colour link rotation is mass-like, so "drop the variance" gives a bound that grows with the cell. I re-derived this independently before reading row 1011 and agree with it.
3. The port of (d)-(e) has no content: every gauge-invariant observable is neutral. So the neutral sector, which the 2D proof gets from association, is the whole problem (the lane's (SING)).
4. A statement that is uniform over all boundary values is false in 4D at window couplings (row 1072, Proposition CA-FAIL: pinned slabs carry an ordered 3D O(4) magnet). So a 4D proof has to be in the law of the model. The lane's periodic engine (Theorem S, `library/gap-crux-restate.md` 3.4) is of that kind, and it needs a seed.
5. "Area law gives the gap" is false in the class of lattice actions (row 1065: a critical end point inside a confined phase). So the neutral gap needs its own input, and at one fixed lattice coupling that input contains a number.

### 2.2 Ideas screened in this step and found on file (not attacked)

| Idea | Where it is on file | Verdict there |
|---|---|---|
| Rigid group of time-independent gauge transformations in temporal gauge; stiffness in time only | rows 1016, 1190 | gives static-charge decay only; true for U(1) |
| Area law implies the neutral gap | row 1065 4b, row 1190 item 17 | false in the class |
| Small box with 't Hooft twist (no torons, perturbative gap) as a seed | `gap-crux-restate.md` C5, (AC'-lat), row 679 | the twisted gap is scale invariant at weak coupling: side times gap is a constant near pi, so Theorem S cannot start; doubling a twisted side is a signed trace (TM-c) |
| Conditional abelian model in maximal-torus coordinates | rows 1188 (Lemma HF), 1190 (sign pattern) | frustrated; no Ginibre structure |
| Jensen bound with a fixed lab-frame translation | rows 697 (Way 3), 1181 (Proposition J), 1179 | mass-like, of area order |

New in this step, small (PROVED here, one line each; used below):

- (2.2a) For the 2D engine of Corollary S2 with the two short sides as a fixed twisted fibre, a seed at weak coupling is available in principle, because the fibre has a tree-level gap. It gives nothing for 4D: the fibre size cannot be doubled inside the engine.

### 2.3 The attack chosen

The mass-like term of item 2 is the only reason that the start bound of the stiffness iteration fails at an abelian pin. For an abelian pin there is an exact structure that row 1011 did not use: in Hopf coordinates on each link, U = cos(phi) e^(a chi) + sin(phi) e^(a vartheta) j, Haar measure is a product measure in (phi, chi, vartheta), the diagonal phase chi is a U(1) lattice gauge field, and the marginal law of chi after integration over (phi, vartheta) is exactly invariant under U(1) gauge transformations. A shift of chi alone preserves Haar measure. So a Jensen bound in chi after the off-diagonal variables are integrated has no seagull term by construction: its cost is a form in the curl of the shift.

Plan: (i) grep the record for this construction; (ii) state the exact inequality; (iii) decide whether its right side is classical in size, or mass-like through a Meissner response of the off-diagonal variables; (iv) if mass-like in the unfixed ensemble, add a U(1)-invariant soft gauge weight and repeat.

Known risk, written before the work: in the unfixed ensemble the gauge orbit acts as a charged Stueckelberg field for chi, so the chi-marginal should be Higgs-like and the bound mass-like with coefficient b. Then the construction needs the soft maximal-abelian weight, and its open step is a bound on the helicity modulus of the off-diagonal variables.
