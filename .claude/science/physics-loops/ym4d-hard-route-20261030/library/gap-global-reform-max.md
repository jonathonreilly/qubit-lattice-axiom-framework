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
- 19:5xZ step 1 done (inputs read, wall and contract written). Nothing proved yet.

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
