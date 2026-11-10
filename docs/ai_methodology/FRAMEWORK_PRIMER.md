# Framework primer: how to read the axioms file

This primer restates no axiom and has no standing. It says where the axioms
are, in what order to read them, which words mislead, how the owner reads
them, and where readers go wrong. Every item says which of two kinds it is:
`[axioms: H]` means the canonical file says it under heading H; the words
"owner guidance, not in the axioms file" mean exactly that.

## Where the text is and how to quote it

- The canonical text is `docs/MINIMAL_AXIOMS_2026-06-29.md` on `origin/main`.
  Read and quote it with
  `git show origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md`, never from this
  primer, a skill, a summary, memory or a working tree. Quote whole
  sentences and name the heading they sit under. Owner guidance, not in the
  axioms file; the rule's home is `AGENTS.md` item 4.
- The date in the file name is not the date of the text: the file is revised
  in place and its path is kept unchanged. [axioms: Historical Context]
- The machine-readable source of the axiom set is the `minimal_axioms` entry
  of `docs/audit/data/axiom_premise_nodes.json`.
  [axioms: Audit-Pipeline Treatment]

## Reading order

The order is owner guidance, not in the axioms file. Each step names its
heading; the short name in brackets is how later sections cite it.

1. The lines above `Purpose`, then `Purpose` [Purpose]: status, where the
   owner's approval is recorded, what the memo supersedes, the four names.
2. `The Four Framework Axioms`: the governing statements, one subsection
   each. `Lattice / Physical Locality` [Lattice], `Qubit / Site Possibility`
   [Qubit], `Admissibility / Local Constraint` [Admissibility],
   `Record / Fixed Reality` [Record].
3. `Qualification` [Qualification]: what further structure needs before it
   is used as a premise, and what "state" and "law" mean here.
4. `Relation To Dynamics And Kinetic Branch Selection` [Dynamics] and
   `Open Gates Outside The Axioms` [Open Gates]: what the axioms leave out.
5. `Relation To The 2026-06-05 Record Wording` [Record Wording] and
   `Relation To The Older Observable-Principle Parent` [Older Parent]: read
   both before any note written against an earlier wording.
6. `Audit-Pipeline Treatment` [Audit]: how a dependency on an axiom or an
   approved primitive is treated.
7. `Historical Context` [History]: last. It quotes sentences of earlier
   revisions, so nothing in it is quoted as the current statement.

## Words a newcomer misreads

Each entry gives the misreading and the heading that settles it.

- **`A1`, `A2`, "Quantum".** Older names, not current ones. [axioms: Purpose]
- **Qubit.** The name of the site axiom, not a licence to assume textbook
  qubit dynamics. [axioms: Qubit; Dynamics]
- **Nearest-neighbor, neighborhood.** `Lattice` and `Admissibility` use
  different words; carry neither into the other. `History` quotes an
  earlier sentence. [axioms: Lattice; Admissibility; History]
- **Admissibility; probability distribution.** Not a dynamics axiom, and not
  Born weights, transition probabilities or an update law. What it does not
  choose, supply or define is listed. [axioms: Dynamics; Open Gates]
- **Admissible, available; "law-level".** Explained only in the paragraph
  titled "Reading notes", which the file marks interpretive and
  non-governing. Cite it as a reading note, never as the axiom.
  [axioms: Admissibility]
- **Record; readable; readout.** Not a measurement outcome in a chosen
  basis, and not a readout context: sector decompositions and `K`/CPT
  structure are placed downstream. [axioms: Record; Record Wording; Older
  Parent; Open Gates]
- **"Records form."** That records occur, not where, how often or by what
  process. [axioms: History; Open Gates]
- **State; law.** Both are defined terms here. [axioms: Qualification]
- **Approved primitive; bounded; admission.** What the supplied foundation
  is, whether depending on it bounds a result, and whether an admission
  class exists. [axioms: Audit]
- **Open gate.** Something the axioms do not close, import or rename. The
  list opens with "In particular", so it is not complete, and it does not
  say that any gate can be closed. The arrow and the time metric are on it.
  [axioms: Open Gates]
- **`I`, additivity.** No longer Record content. [axioms: Older Parent]

## The lens the owner works with

Every item in this section is owner guidance, not in the axioms file, except
a clause that carries an `[axioms: ...]` tag. A lens is a way of reading.
Nothing in it is a premise until it meets what the file requires of further
structure. [axioms: Qualification]

- **Register, not read.** The owner reads `Record` as the place where
  physical fact lives. An operator or state written down before any record
  is a reconstruction: a device for computing what records would hold.
- To establish an observable under this lens, show what records hold. Do not
  shape a pre-record operator into a wanted form.
- The lens is usually worked with a sector decomposition `{P_k}` and the map
  `D(M) = sum_k P_k M P_k`; only the sector-diagonal part counts as
  registered. A decomposition is downstream of the axioms [axioms: Record
  Wording], so it is a named input of the lane that uses it, never chosen
  to fit an answer, and its coarseness needs a named condition.
- The decomposition delivers which sector, and sector overlaps. Per-sector
  weights belong to the realized pattern of records; a reference state's
  weights are a reconstruction. No weighting is "the" measure, and Born
  weight values are listed outside the axioms. [axioms: Open Gates]
- The lens gives outcome structure only. It derives no decoherence and no
  dynamics; both are listed outside the axioms. [axioms: Open Gates]

## Common traps

- Quoting an axiom from memory, a skill, a summary or a stale checkout. The
  wording has been revised in place more than once. [axioms: History]
- Quoting a sentence from `History`, or from a note written against an
  earlier wording, as the current axiom. [axioms: History; Record Wording]
- Citing `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` as the axiom note.
  [axioms: Older Parent]
- Treating structure the axioms are compatible with as included in them.
  [axioms: Dynamics; Qualification]
- The realist slip: taking a pre-record operator or reference state for the
  physical fact. Likewise, conflating what a decomposition delivers with a
  per-sector weight. Owner guidance, not in the axioms file.
- Reading "outside the axioms", or a blocker, as "impossible" or as "surely
  derivable". The file says neither. [axioms: Open Gates] How a negative
  result is graded, and how a blocker's scope is read, is in `RULES.md`
  section 2, rules 6 and 8. Owner guidance, not in the axioms file.
