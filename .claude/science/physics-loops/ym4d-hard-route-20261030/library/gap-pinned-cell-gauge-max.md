lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T05:44Z

# Row 1011, gap-pinned-cell-gauge-max: does the 2D pinned-cell stiffness iteration have a 4D SU(2) gauge form?

Worker: Claude Fable 5.2, max effort, Mac mini worker 1. Pinned at commit c216eeef9. Started 2026-11-15T17:44Z.
Research-stage working state. Nothing here is a claim of the mass gap or of any part of T0. Marks used: PROVED (written
by hand here, not yet checked by another model), ARGUED, OPEN, FAILS. A numeric run, if any, only refutes or guides.

Credit. The pinned-cell stiffness iteration is OpenAI's (posted, unrefereed preprints, github.com/openai/math commit
4eaee87548250b2682affda7d05d947c05554bae: "Sharp mass bounds for the two-dimensional O(4) model", Section 3; "The
canonical massive continuum limit of the two-dimensional O(3) model", Sections 2 and 8). The readings this row starts
from are rows 1007, 1009, 1010 of this lane. The Schrodinger-functional coupling is Luscher, Narayanan, Weisz, Wolff
(1992). Sussman and Alpoge (with Claude and Codex as authors of their text) are credited where their account is read.

## 0. Plan (save protocol; at most eight steps, one step per response, result appended before the next)

1. Read the inputs: `parts/gap.md`, rows 1009, 1010, 1007 in full, the exercise skill at main 8b11ae2bb9. Note what
   each gives. Then the registry grep (open-core, FINISH rows, idea digests) for every object the row names.
2. Read the primary text of the O(4) paper Section 3 at the points the transfer needs (class, stiffness, Ward
   identity, bracket gain, shell family), and state the 2D mechanism in one page as a list of steps with the
   property each step uses.
3. Task 1: state each piece on the 4D lattice: the class, the stiffness, the Ward identity with its bracket term,
   the family, the one-step gain.
4. Task 2: run the tests first (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET at fixed b, compact U(1), frozen
   Q_8 and 2T, the five-dimensional test, the instanton and refilling obstruction).
5. Task 3: for the first piece that survives, prove it by hand or build the counterexample.
6. Task 4: if the one-step gain survives, its statement with constants, the remaining lemma to the 4D mixing bound
   and the exponent condition. If it does not, the exact step that fails and why.
7. Exercise-skill report: set-aside table, blockage sentence, what the next row should be (a complete brief).
8. Print every cited anchor, fix drift, write the RESULT line.

## Status log

- 2026-11-15T17:44Z: file created, plan written. Nothing read beyond GOAL.md, the FINISH head and the queue row.
- 2026-11-15T18:08Z: Step 1 done (inputs read, record located). See Section 1.

## 1. Step 1: inputs read, and where the lane's record sits (exercise step 0)

Model and provenance: Anthropic, Claude Fable 5.2, max effort, one session, no subagents. Nothing in this file is
checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no
computer-assisted step, Lean-formalizable proofs) replaces the framework refresher read of the exercise skill.
The skill was fetched at main 8b11ae2bb9 with its reference `proof-search-governance.md` (both read in full).

Read in full: `parts/gap.md` (the state file), row 1009 (`library/prior/gap-o4-pinned-cell-read-opus.md`),
row 1010 (`library/prior/gap-o3-continuum-rg-read-opus.md`). Read in part: row 1007
(`library/prior/gap-2don-proofs-read-opus.md`, A(5) L84-100 and Step 6 L112-176).

What the inputs give (all OpenAI's mathematics, as restated by rows 1009 and 1010; unchecked):

- The 2D engine is a statement about one class C_b: every pinned square, every boundary pin, every strength field
  with |b_e| <= b (O(4): also signs and right twists). Monotone: the twist stiffness H_Q = direct cost minus
  current covariance (row 1009 L84). Start H <= b (L85). Step: H_c <= h on the class at side R gives H <= h - delta
  at side l R, delta >= (log l)/pi - C log B (O(4), L141-147) or (log l)/(4 pi) (O(3), L272).
- Why the step closes: (i) conditioning a square on cell rings gives cells of the same class, and the ring action's
  Hessian is the sum of cell stiffnesses, exactly (3.16) (L102-103); (ii) Gaussian augmentation turns "stiffness at
  most v" into "variance of the augmented current at least the gain" (3.19) (L107); (iii) a Brascamp-Lieb /
  Helffer-Sjostrand identity (3.21) and Cauchy-Schwarz give Var J(A) >= (signal)^2 / (cost) (3.50) (L139-140);
  (iv) the signal is the bracket term of the Ward identity: the derivative of the current J(A) along a rotation
  u_i about a perpendicular axis is 2 J(u_i A') with A' = -a x A (3.28)-(3.29) (L115-117); (v) the test directions
  are u_i = chi phi_i/|k_i| over a frequency annulus M <= |k| <= K_1, and the sum of |k|^(-2) over a 2D annulus is
  (1/(2 pi)) log(K_1/M) (3.37) (L127).
- After small stiffness: local rotations are cheap, coarse orientations, disagreement percolation, then abelian
  decompositions with association give mixing for all observables (L158-187). The seed follows by the coupling
  integral (3.70), which is the lane's Theorem D (f) (L190-195, L419).
- Row 1010: the band is crossed only by that mixing bound at one bare coupling; the RG only carries a box number
  across cutoffs under the exponent condition (8.3); its 4D transcription asks for a mixing exponent below 3/2
  times one loop (L202, unchecked).
- Row 1007 B(5) (L159-161): a constant gauge rotation of a pinned boundary layer is undone inside (SU(2) is
  connected); a local gauge change of variables gives no inequality on gauge-invariant data.

Where the lane's own record on the row's objects sits (located, NOT read yet; closed until the compare step):
Schrodinger functional: `gap-constraints-max.md`, `gap-crux-exercise-astra.md`, `gap-flux-exercise.md`,
`gap-form-exercise.md`, `gap-phys-seed.md`, `gap-skeleton-final.md`, `prior/gap-kflow-read-opus.md`,
`prior/gap-small-volume-lit.md`, `prior/gap-fullread-1.md`, `prior/gap-seed-lit.md`, `prior/gap-vir-lit.md`.
Stiffness: 20 gap files (among them `gap-sc-max.md`, `gap-fc-max.md`, `gap-hcphys-max.md`, `gap-tiltproof-max.md`,
`gap-direction2-max.md`, `gap-brainstorm-max.md`). "gauge wave": no file. `library/open-core.md` has no hit for
pinned, stiffness, Schrodinger, background field, helicity or step scaling.

Companion row 1012 (`gap-gauge-stiffness-read-opus`, queued at the same time, reading only) searches the published
literature on SF coupling rigour, gauge Ward identities and stiffness bounds, and gauge McBryan-Spencer bounds.
This row does not repeat that search; it uses the lane's files and the primary OpenAI text.
