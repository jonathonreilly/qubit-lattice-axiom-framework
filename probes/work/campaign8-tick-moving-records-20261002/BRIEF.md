# Campaign 8 brief: ticks, moving records, flow (overnight 2026-10-02 20:30 → 10-03 08:30 EDT)

You are one agent in a derivation-focused exploration for the owner of a physics framework. The owner is asleep. Your report will be read by the coordinator, who will verify it and summarize it for the owner in plain language.

## The framework: four axioms, verbatim from the canonical memo (origin/main docs/MINIMAL_AXIOMS_2026-06-29.md)

- **Lattice.** "Physical sites are the points of the cubic lattice Z^3, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site. No site is privileged. Sites are distinguished by the supplied lattice structure alone."
- **Qubit.** "Each site has a domain of local possibilities. The full one-site possibility domain has algebraic presentation M_2(C). ... No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone."
- **Admissibility.**
  - "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations. For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
  - Reading notes, which are non-governing:
    1. The distribution is law-level. The law supplies the odds; the realized state supplies the pick.
    2. Read with Record, it concerns which possibility a forming record locks, conditional on formation. It does not supply the formation site, probability or rate.
    3. "available" means the support of the distribution (the menu).
- **Record.** "Records form. When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."
- **Qualification.**
  - "A state is a configuration of records."
  - "A law privileges no states."
  - "A choice not fixed by the supplied structure remains a named conditional or open dependency."
- **Time.** The axioms have no time. The owner treats time as the accumulation of records.

## Owner readings decided on 2026-10-02 (from the one-clause walk-through)

- **Q1: sharing.** Approved wording: "The nearest-neighbor conditions include the possibilities of neighbors with no record. Sites with no record share their possibilities: one site's possibilities can be linked with those of many other sites at once. When a record forms, the shared possibilities change at once to agree with it. Whether one record forming makes another form is left open."
- **Q2: the film reading.** The system evolves continuously and has no final state. The rule acts locally on the full snapshot: records plus shared possibilities.
- **Q3: the soldering split.** Influence between records (the change) is glued to the grid's rotations. Formation odds are not glued; they depend on the site's possibilities relative to the menu.
- **Q4: equal odds.** An uninfluenced site has equal odds for all outcomes. This is Qubit's "No possibility is privileged".
- **Q7: menus.** The menu, meaning the possibilities with nonzero odds, is set by the conditions, including recorded neighbours.

For context, the Campaign 7 "one clause" candidate has not been adopted. Its four sentences are:
1. a joint possibility on the tensor algebra of the site domains;
2. change that is continuous, reversible, homogeneous, rotation-soldered and star-local (a sum of nearest-neighbour terms), which keeps locked possibilities;
3. odds taken from the site's own part, with a cut (Lüders compression) when a record forms;
4. no-signalling.

## Ideas under exploration

These are the owner's instincts, NOT positions. Never present them as adopted. Phrase everything as "if ... then ...".

- **I1.** Records form only at set ticks, and two records can form on the same tick. Open: is the tick global or local to a neighbourhood, and is it constant or influenced?
- **I2.** A record can move at most one grid space per tick. A site with no record can form at most one new record per tick, so sites can be reused after their record moves away.
- **I3.** Where a record moves is decided by odds set by the neighbourhood conditions, like formation. If two records want the same site, one wins with its relative probability, also like formation.
- **I4.** The shared possibilities flow ("neighbourhoods can shift") rather than swapping.
  - With one site's worth of possibilities per site, net flow across any cut of a line is the same at every cut. A rightward push is therefore a standing conveyor through the whole line, every tick: a step with a built-in direction (an index).
  - Smooth (continuous) change cannot produce such steps. Campaign 7 flagged "Continuity sets aside index-carrying discrete steps, which bear on chirality (ARGUED)".
- **I5.** A fully recorded (jammed) region may behave like a black hole. Nothing can form or move inside it, so time stops there.
- **I6.** The grid is infinite (Z^3).
- **Open question.** Does an empty site far from any record form a record on its own, or only when its neighbourhood conditions call for it?

## Prior toy results (ai/probes bebecfb8fa, probes/work/formation-timing-probes-20261002/)

Supplied ring model: a Heisenberg ground-state preparation, Lüders cuts, and locked records that either push or drop.

- With fixed menus and no change between records, order and simultaneity of formation leave no mark. This is exact, because compressions at different sites commute.
- The timing of formation is readable only in two ways:
  - through change between records (gap, pace γ/J, triggering);
  - through menus set by records that already formed. Neighbours that form "together" do not share a frame; neighbours that form in sequence do.
- A per-site metronome cannot be distinguished from random times. What is readable is exact coincidence of linked sites.
- The reach of a record's timing is the existing links plus how far the change carries during the gap.

## Discipline

- **No new imports.** Do not adopt new axioms, literature models, comparators or framing as framework content. You may cite literature as COMPARATOR (not adopted) in a clearly marked section.
- **Grade every claim:**
  - EXACT: proved, or exact arithmetic;
  - CHECKED: a numeric check with stated tolerance;
  - ARGUED: reasoning without proof.
- Never write "only route", "last route", "exhausted", "closes the route", or finite-enumeration closure language.
- **Language rule.** Never say a possibility is "read" or that a "question is asked". A forming record locks one possibility. Only records are read, by their content alone.
- Do not overclaim physics. Say "toy", "supplied model", "analog" where that is what you have.

## Constraints

- Derivation first.
- Tiny numeric checks are allowed only if each run:
  - finishes in under 60 s and uses under 300 MB;
  - runs with `nice -n 10`;
  - sets these thread caps to 1: `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS`, `MKL_NUM_THREADS`.
- This is an 8 GB machine shared with other jobs. If a bigger toy is needed, include the script in your report and do not run it.
- No git operations, no repo edits, no PRs, no audit or review lanes.
- Scratch files go only under your assigned directory.

## Deliverable

Your final message IS the report; the coordinator saves it. Use these sections:

1. **Question.** Restate your sharp question.
2. **Answer.** Yes, no, or conditional, in one paragraph, with its grade.
3. **Derivation.** The steps, each graded.
4. **Checks.** What you ran, with code summary, numbers and tolerances; or what should be run.
5. **Real-physics match.** What the result implies for matching known physics, and what would falsify it.
6. **Open edges and next steps.**
7. **Plain-language summary.** 3 to 6 sentences for the owner: very layman, in the axioms' register, with no jargon.
