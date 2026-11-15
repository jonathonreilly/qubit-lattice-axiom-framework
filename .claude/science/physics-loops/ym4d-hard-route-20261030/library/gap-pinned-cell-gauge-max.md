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
