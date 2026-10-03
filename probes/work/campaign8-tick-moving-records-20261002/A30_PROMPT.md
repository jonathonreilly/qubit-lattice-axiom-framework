You are lane A30 of an overnight, derivation-focused physics exploration ("Campaign 8"). Topic: **the owner's black-hole instinct (I5) under the campaign's most coherent package so far.** Use derivations first, then small low-compute toys.

## Read first (primary files; do not trust summaries)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- `SP/c8/BRIEF.md`: the framework's four axioms verbatim, the owner's decided readings (Q1–Q4, Q7), the owner's instincts I1–I6, and the discipline rules. I5 says: "A fully recorded (jammed) region may behave like a black hole. Nothing can form or move inside it, so time stops there." These instincts are explorations, NOT positions.
- `SP/c8/A27/REPORT.md`: "Option R", the package you work inside.
  - Records step on ticks by their own swap rule (SW) and settle clashes by the claim rule (CL).
  - Unrecorded possibilities change smoothly between ticks by a covariant generator that holds recorded sites fixed, so records act as walls and fixed weights.
- `SP/c8/A24/REPORT.md`: energy-gentle records only via "catch first, record later", i.e. records form on caught, settled things, slowly.
- `SP/c8/A28/REPORT.md`, if present: gated formation, "records form only next to records". If it is not there yet, read its partial outputs `SP/c8/A28/out_*.txt` and do NOT redo its growth runs. Its 2D growth of record regions is its job, not yours.
- `SP/c8/A4/REPORT.md` and `SP/c8/A6/REPORT.md`: the earlier jam and black-hole toys, under the older rules.
  - Jams always leak.
  - Swallowing needs a "stopped" mark.
  - A16's correction: jam lifetime grows as N, because loss rates are about equal.
- `SP/c8/A23/REPORT.md`, `SP/c8/A25/REPORT.md` and `SP/c8/A26/REPORT.md`: the gravity field route.
  - A tensor "shape" field of the shared possibilities, never locked (F1).
  - Matter couples through lapse and frame.
  - The field needs a fixed role pattern.
- `SP/c8/LOG.md` is long. Grep for "^## " and for "CORRECTION" and read only what you need. Corrections C1–C26 and K1 supersede earlier lane wording.

## Questions
1. **Wall or absorber?**
   - Under Option R a jam is a wall for unrecorded possibilities. Something arriving at the jam can be caught and recorded at its surface, by catch-first formation, gated or not.
   - What fraction of an incoming wave is captured, and what fraction reflected? Derive exactly in 1D: a semi-infinite recorded wall plus a capture channel at the surface site, as a rate or as a per-tick chance.
   - Can the surface be black for all energies?
   - Check whether fast capture reflects (a Zeno-type effect), whether there is a critical coupling, and whether a graded or porous surface layer can be near-black across energies.
   - Then run a small 2D check: a recorded disk and a wave packet. Measure the capture cross-section against the geometric one.
2. **Does a jam leak or seal?**
   - Under SW, surface records can step into empty neighbours.
   - With A27's odds options (a straight average over what the empty neighbour holds, or fixed odds), can the odds of stepping into a quiet empty neighbour be exactly zero, so that the jam is sealed?
   - If so, is that consistent with exact rotation covariance, no faraway signalling (A7/A16 C-corrections) and Q7? What does it cost elsewhere, for example records then never crossing empty space?
   - If it leaks, how do the rate and the lifetime scale?
3. **Does time stop inside (I5)?**
   - Inside a full jam under Option R, no record forms, none moves, and the smooth change has nothing unlocked to change in the record sector.
   - In the field route, clock rates come from the lapse field, which stays unlocked (F1) even inside a jam.
   - Sort out exactly what "time stops" can mean here. Does a record lock the field part of a site's possibilities?
   - State which reading of the Record axiom and F1 each answer needs.
4. **Field-route estimate (COMPARATOR, from memory, flagged).**
   - Suppose caught matter at grid density carries ordinary mass-energy. When is a jam inside its own horizon?
   - Give the scaling with a Planck-length grid.
   - State what the linear field route can and cannot say, given that there is no horizon at linear order.
5. **Information.**
   - What falls in becomes permanent, readable surface records.
   - Contrast this with a GR horizon. What could an outside reader of records in principle learn?
6. **Evaporation.**
   - If anything leaks, compare its scaling with Hawking's lifetime ∝ M³ (COMPARATOR).
   - Is there any Option R channel for a thermal-like emission? Argue only, unless a tiny exact toy decides it.

## Rules
- **Grading.** Grade every claim EXACT (proof), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED (a premise put in by hand) or COMPARATOR (literature from memory, never adopted). Name every conditional.
- **Language.**
  - Never say a possibility is "read" or that a "question is asked".
  - Never present "records form on a beat or heartbeat" as adopted.
  - Propose no new axioms or imports as adopted; frame any needed choice as an owner decision.
- **Compute.** This is an 8 GB machine with other agents running.
  - Every numeric run: `nice -n 10`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all set to 1. Each run under 60 s and 300 MB.
  - Before EACH run, check `uptime`. Run only if the 1-minute load is below 6. Otherwise continue on paper and re-check later.
  - Keep lattices at or below 128×128 in 2D and use exact or sparse methods.
- **Files.** No git, no repo edits, no PRs, no review or audit lanes. Write only inside `SP/c8/A30/`.

## Output
Write `SP/c8/A30/REPORT.md` with these sections:
1. Question
2. Answer: short, graded
3. Derivation: numbered steps, graded
4. Checks: script, run, numbers, tolerance
5. Real-physics match: comparators flagged, plus falsifiers
6. Open edges
7. Plain-language summary: one paragraph for a non-specialist owner, no jargon

Return the full report as your final message.
