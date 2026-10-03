You are lane A31 of an overnight, derivation-focused physics exploration ("Campaign 8"). Your task is **to assemble the "Option R" package into one consistent model (assembly v2) and find where it breaks.** Do derivations first, then tiny checks.

## Read first (primary files; do not trust summaries)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- `SP/c8/BRIEF.md`: the four axioms verbatim, the owner's decided readings (Q1–Q4, Q7), the owner's instincts I1–I6 (explorations, NOT positions), and the discipline rules.
- `SP/c8/A13/REPORT.md`: assembly v1, the pre-Option-R model, and its decisions D1–D8.
- `SP/c8/A20/REPORT.md` with `SP/c8/A21/REVIEW_FINAL.md`: Theorem N. A NN, reversible, soldered-covariant tick with one qubit per site and an ungraded product is the identity.
- `SP/c8/A27/REPORT.md`: Option R.
  - Records step on ticks by the swap rule SW and settle clashes by the claim rule CL.
  - Possibilities change smoothly between ticks, holding records fixed.
  - Note its own remark that a sampled smooth naive Dirac generator has a spatial partner at k = π.
- `SP/c8/A24/REPORT.md`: catch first, record later.
- `SP/c8/A28/REPORT.md`: gated formation, "records form only next to records".
- `SP/c8/A23/REPORT.md`, `SP/c8/A25/REPORT.md` and `SP/c8/A26/REPORT.md`: the gravity field route.
  - A25 Theorem A: a collocated, covariant, gauge-invariant field has a spatial doubler at (π,π,π), so the field needs a 2×2×2 role pattern, 1 of 8 translates.
  - A26: matter couples through lapse and frame, the two-site mass split is ST, and a shear sandwich is needed.
- `SP/c8/A10/REPORT.md` and `SP/c8/A16/REVIEW.md`: KS-signed staggered matter, and the finding that A10's sublattices become readable once records interact.
- `SP/c8/A29/REVIEW.md`: the third hostile review, if present. Its corrections supersede lane wording.
- `SP/c8/LOG.md`: long. Grep "^## " and "CORRECTION" and read only what you need. Corrections C1–C26 and K1 are binding.

## Tasks
1. **Write the assembled model.** State it explicitly and in one place: records, possibilities' smooth change, matter, the gravity field, coupling and formation.
   - For every ingredient, say whether it is axiom text, an owner-decided reading, an unadopted Campaign 7 sentence, a named conditional (F1–F6, G1, …) or a supplied pattern.
2. **Spatial doubling for matter under smooth change.**
   - With one qubit per site, a Dirac-like light cone for matter under a smooth NN covariant generator seems to need the Kogut–Susskind staggered encoding, gauge-equivalent to π-flux hopping. Derive whether that is forced, given the axioms plus Option R plus one qubit per site, at the grade the argument supports.
   - Is the KS sign pattern a SUPPLIED pattern, or covariant up to a possibility relabelling allowed by Q3?
   - A16 found A10's sublattices readable once records interact. Is the sign pattern readable from Z-type records under smooth change? Under which record bases? Check with a tiny exact toy, at most 12 qubits.
3. **One shared cell?**
   - Matter's staggered taste cell and the field's role cell (A25) are both 2×2×2.
   - Can they be one shared choice, 1 of 8, so the package carries ONE supplied pattern instead of two?
   - What would that require in the coupling (A26's frame sandwich and the ST split)?
   - Give an exact statement or a counter-example.
4. **Consistency sweep.** For each pair of ingredients, check for a conflict:
   - SW/CL against the smooth change;
   - gated formation against catch-first;
   - catch-first against the energy source of the field (F3, the ghost source);
   - the lapse pacing the field (A23 D16) against Option R's tick-free possibilities;
   - records as walls against light that must pass through matter;
   - A14's photon-mass bound against walls.
   List every conflict with its grade.
5. **The supplied-items ledger.** List the complete set of supplied items and named conditionals the assembled model needs, minimal and de-duplicated. Rank them by how much each costs relative to the axioms. Then give the owner decisions in plain language, de-duplicated against the draft's decision list in `SP/c8/MORNING_DRAFT.md` (§ "Decisions this raises").
6. **The single most important open problem** for the assembled model, and the smallest next calculation that would move it.

## Rules
- **Grading.** Grade every claim EXACT (proof), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED (a premise put in by hand) or COMPARATOR (literature from memory, never adopted). Name every conditional.
- **Language.**
  - Never say a possibility is "read" or that a "question is asked".
  - Never present "records form on a beat or heartbeat" as adopted.
  - Propose no new axioms or imports as adopted; frame any needed choice as an owner decision.
- **Compute.** This is an 8 GB machine with other agents running.
  - Every numeric run: `nice -n 10`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all set to 1. Each run under 60 s and 300 MB.
  - Before EACH run, check `uptime`. Run only if the 1-minute load is below 6.
  - Exact toys at most 12 qubits.
- **Files.** No git, no repo edits, no PRs, no review or audit lanes. Write only inside `SP/c8/A31/`.

## Output
Write `SP/c8/A31/REPORT.md` with these sections:
1. Question
2. The assembled model, as a table
3. Answers to tasks 2–6, graded
4. Derivations
5. Checks
6. Real-physics match: comparators flagged
7. Open edges
8. Plain-language summary: one paragraph for a non-specialist owner

Return the full report as your final message.
