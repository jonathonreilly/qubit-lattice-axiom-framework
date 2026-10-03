You are lane A43 of Campaign 8, a daytime follow-up the owner asked for on 3 October. Topic: **can neutral matter with two internal parts that turn with the grid, which gets clean light-like crossings, come from one qubit per place?** Work derivation first; use only small Bloch-matrix or spin-wave toys. Time box: 60 minutes.

SP = /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
The repo is at /Users/jonreilly/Projects/Physics/.claude/worktrees/focused-noyce-9a3983, ref origin/main (b6fda5ae1d), and is READ-ONLY. Read files with `git -C <repo> show origin/main:<path>`. Do not fetch.

## Why
- The repo check (`SP/c8/CHECK/G5.md`, row R3) found that the two-part walk H = Σ_a σ_a sin k_a has two internal states per place, turning with the grid as in the owner's Q3. It has eight exactly round, equal-speed crossings, four of each hand, with no heavy or flat partners.
- Sources:
  - the repo note `docs/ADMISSIBILITY_RULE_THE_SPECIES_SYMMETRY_FORCES_ONLY_DOUBLING_EVERY_NONZERO_LEVEL_IN_A_VARYING_FIELD_IS_A_PAIR_AND_A_RATE_FIELD_KEEPS_EXACTLY_SIXTEEN_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-24.md`;
  - its sibling, found with `git -C <repo> ls-tree -r --name-only origin/main docs/ | grep THE_AXIOMS_OWN_GENERATOR`;
  - campaign lane A1, D21.
- The difficulty: with one qubit per place, a single disturbance of a calm product background has only one internal state. So two internal parts seem to need more room per place.
- More room touches a parked registry entry. `docs/repo/DEFERRED_DECISIONS.md` §4 has the standing default "M₂(ℂ) stands as postulated". Treat more room only as a named supplied premise, never as available.

## Read (primary files; summaries are not enough)
- `SP/c8/A1/REPORT.md` (D21, D26–D28).
- `SP/c8/A31/REPORT.md` (calm product vacuum; Theorem S).
- `SP/c8/A33/REPORT.md` (Theorem C).
- `SP/c8/A38/REPORT.md`.
- `SP/c8/A39/REPORT.md` (Theorem T: quiet + visibility + twist gives z ≥ 2, and its escapes).
- `SP/c8/A40/REPORT.md` and `SP/c8/A41/REPORT.md`.
- The ERRATA section of each report above.
- `SP/c8/CHECK/G5.md` (rows R1–R4, R10) and `SP/c8/CHECK/G6.md` (top issues).
- On the repo: the two notes above, and `docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md`. That note finds three covariant couplings under full soldering: Heisenberg, compass and Moriya.

## Questions
1. **The walk itself.** Confirm the two-part walk's crossings exactly: count, hand, speed and partners. Confirm its covariance under full soldering (σ turning with the grid). Grade: EXACT.
2. **Routes to two internal parts with one qubit per place.** Give the cost of each.
   - (a) **More room per place.** This is parked. State only what it would give, as a named supplied premise.
   - (b) **A composite over two places** (bond-centred objects, or two-site cells). Does it need a supplied pattern, against "No site is privileged", or can bond-centred objects be covariant?
   - (c) **Disturbances of a patterned background held in the state.** Examples: the alternating (Néel-type) background of the Heisenberg coupling with the antiferromagnetic sign, and the backgrounds of the compass and Moriya couplings. For each, give the linear spin-wave dispersion, the number of branches, the speed, isotropy at long wavelength, and any partners. These are bosonic ripples with no handedness; say what kind of "light-like" they are and how they differ from the walk's crossings.
   - (d) **Fractionalized disturbances of an entangled background.** In the parton construction there are two-component fermions per site with one fermion per site. A soldered hopping f†(iσ^a)f at half filling puts the walk's crossings at zero energy. Grade this COMPARATOR/ARGUED. Say what it needs (a gauge field, a projection, a parent rule) and what is known in the literature, cited from memory and marked as comparator.
3. **Compatibility with the record-tick shape, route by route.**
   - (i) The gate: records form only next to records, so voids are quiet.
   - (ii) A39's Theorem T, its hypotheses and its escapes. Does route (c) contradict Theorem T, or which hypothesis fails? Settle this exactly where you can.
   - (iii) A33's Theorem C.
   - (iv) The owner's Q3 (exact turns, no extra local phase).
4. **Verdict.** Is there a route to clean round crossings with one qubit per place under full soldering, and at what cost? Give a plain-language summary.

## Grades
EXACT, CHECKED, ARGUED, or COMPARATOR.

## Compute
Small Bloch matrices and linear spin waves only.
- Before any run:
  - check that `uptime` shows a 1-minute load below 6;
  - take the shared numeric lock with `mkdir SP/c8/NUMLOCK`. If the lock exists and is under 3 minutes old, do derivation work and retry later. If it is older, it is stale: remove it.
- Run with `nice -n 10` and the four BLAS thread caps (OMP, OPENBLAS, MKL, VECLIB) set to 1.
- Each run must stay under 30 s and 200 MB.
- Release the lock with `rmdir SP/c8/NUMLOCK` right after the run.

## Rules
- No git writes, no repo edits, no PRs.
- Never say a possibility is "read", or that a "question is asked".
- Never present anything as adopted, and never imply a beat or heartbeat.
- Put scripts in `SP/c8/A43/`. If your sandbox blocks writing `SP/c8/A43/REPORT.md`, return the full report as your final message. Otherwise write it and also return it.

## Output
1. Question
2. Answer, graded
3. Derivation per route
4. Checks: scripts and results
5. Open edges
6. Plain-language summary for the owner, in 4–6 sentences with no jargon