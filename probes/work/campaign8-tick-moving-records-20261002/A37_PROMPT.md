You are lane A37 of an overnight, derivation-focused physics exploration ("Campaign 8"). Your topic: **records that push the possibilities along ("flow") instead of trading places with them ("swap").** This is the owner's own picture, tested inside the campaign's "record-tick shape". Work derivation-first, then use tiny toys.

## The owner's own words (instincts, NOT positions)
- "I kinda think records can move. records can move one grid space per tick. A site without a record can form a single record per tick."
- When asked what happens to the shared possibilities when a record moves: "i wasnt thinking swap but flow neighborhoods can shift"
- On the claim that in one line of sites flow and swap look the same: "no the probabilities can all push right? how is this actually true?"
- "probability still defines the outcome, one wins with its relative probability just like formation" (clashes)
- "yep the grid is infinite"

## Read first (primary files; do not trust summaries)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- `SP/c8/BRIEF.md`: the axioms verbatim, readings Q1–Q4 and Q7, instincts I1–I6, discipline rules.
- `SP/c8/A27/REPORT.md`: Option R, the "record-tick shape".
  - Records step by the swap step SW: a record trades places with an empty neighbour, keeping its content, and the neighbour's possibilities go back to the record's old spot.
  - Clashes are settled by the claim rule CL.
  - Possibilities change smoothly between ticks, holding records fixed.
- `SP/c8/A29/REVIEW.md` (C40: admissibility of a moved record) and `SP/c8/A34/REVIEW.md` (C60: swap energy costs; C67: seal versus move).
- `SP/c8/A1/REPORT.md` (flow, index, covariance kills net flow) and `SP/c8/A3/REPORT.md` (consistent move rules; "follow the net flow").
- `SP/c8/LOG.md` is long. Grep "^## " and "CORRECTION" and read only what you need.

## Questions
1. **Define "push" steps.** When a record moves x → y, the possibilities at y are not sent back to x. They are pushed onward or around. Cover at least:
   - (a) a line push: y's content goes to y+e, that content to y+2e, …, up to the first spot that can absorb it. This is a conveyor along a line, which is unbounded in reach unless capped.
   - (b) a sideways or around push: y's content is spread over the empty neighbours of y other than x, or flows around the record.
   - (c) a "fill behind" rule that relies on the smooth change to carry possibilities back into x over the next interval, with x left in a quiet state at the step.

   For each, check:
   - one record step per tick, and the reach of the possibilities' displacement;
   - covariance under the 24 turns with soldered possibilities (Q3);
   - linearity and no signalling (A7/A16: records cut to agree with their sites);
   - admissibility (C40);
   - conservation: what happens to the possibilities' content and to energy (C60).
2. **Is push observably different from swap?**
   - Exact statements for single records in 1D, where the owner disputed "flow = swap", and in 2D/3D.
   - Does pushing transfer momentum to the possibilities, giving a wake or a drag on a moving record? Does it give records any inertia (A19 found sharp registration erases inertia)?
   - Does a moving record leave a readable trace in later records?
3. **The owner's 1D challenge.** "the probabilities can all push right": a global conveyor carries net flow.
   - Is a record-driven push compatible with Theorem N and A1's "covariance kills net flow"? A1 concerns the possibilities' own law; a record-driven push is triggered by records.
   - What does a record-driven conveyor do to the strict record cone, and to the possibilities' light cone (reach)?
4. **Clashes.** Two records pushing into the same region. Combine with the claim rule ("one wins with its relative probability").
5. **Verdict.** Is "flow" a consistent alternative to "swap" for moving records in the record-tick shape? What does it cost, and what (if anything) does it buy, for example momentum, drag or inertia?

## Rules
- **Grading.** Grade every claim EXACT (proof), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED (a premise put in by hand) or COMPARATOR (literature from memory, never adopted). Name every conditional.
- **Language.** Never say a possibility is "read" or that a "question is asked". Never present "records form on a beat or heartbeat" as adopted. Propose no new axioms or imports as adopted; frame choices as owner decisions.
- **Compute.** This is an 8 GB machine with other agents running.
  - Every run: `nice -n 10`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all set to 1. Each run under 60 s and 300 MB.
  - Check `uptime` before each run, and run only if the 1-minute load is below 6.
  - Exact toys at most 12 qubits, or single-excitation chains.
- **Files.** No git, no repo edits, no PRs, no review or audit lanes. Put scripts in `SP/c8/A37/`. If your sandbox blocks writing REPORT.md, return the full report as your final message.

## Output
A report with these sections:
1. Question
2. Answer: short, graded
3. Derivation: numbered steps, graded
4. Checks
5. Real-physics match: comparators flagged
6. Open edges
7. Plain-language summary: one paragraph for the owner, no jargon. It must answer directly: can records "flow" the possibilities aside rather than swap with them, and does it make a difference?
