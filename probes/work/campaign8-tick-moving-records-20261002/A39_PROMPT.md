You are lane A39 of an overnight, derivation-focused physics exploration ("Campaign 8"). Your topic: **is a quiet empty background compatible with light-like ripples at all?** Every lane tonight has circled this tension. Work derivation-first, then use small exact numerics. Time box: about 55 minutes.

## The tension (read primary files; do not trust summaries)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- **Empty space must be quiet.** Records must essentially never form there, or regions freeze.
  - A9's quiet criterion: formation weights must annihilate the vacuum's star marginals, i.e. the marginals must be rank-deficient.
  - A28's edge floor: next to records, a full-rank vacuum is recorded at a positive rate.
  - See `SP/c8/A9/REPORT.md`, `SP/c8/A12/REPORT.md` and `SP/c8/A28/REPORT.md` (with its ERRATA).
- **Light needs gapless, linear (z = 1), isotropic ripples.**
  - A31 (`SP/c8/A31/REPORT.md` with ERRATA): over a calm aligned product vacuum, single ripples form one analytic band (z = 2), so there is no cone without a painted sign pattern.
  - A34 C57 (`SP/c8/A34/REVIEW.md`): an entangled stationary vacuum, the antiferromagnet with J > 0, has linear ripples (COMPARATOR). But it is full rank at matter's edges.
  - A33 (`SP/c8/A33/REPORT.md`): stabilizer vacua with independent checks give protected excitations that move only in planes.
- **COMPARATOR, from memory, to be checked by you and flagged, not adopted.** There are results that frustration-free Hamiltonians, if gapless, have dynamical exponent z ≥ 2: Gosset–Mozgunov on local gap thresholds; Masaoka–Soejima–Watanabe (about 2024) on quadratic dispersion in gapless frustration-free systems. State what you can derive yourself versus what you only recall.
- `SP/c8/BRIEF.md`: the axioms verbatim, the readings, and the discipline rules.

## Questions
1. **Quiet means rank-deficient star marginals (A9).** Under gating (A28), quietness is needed only next to records. Formalize "quiet": the formation weights F annihilate ρ_star at every star where formation can happen. For a vacuum that is an exact eigenstate of the change, does quiet plus stationary imply a frustration-free parent Hamiltonian? (A weight F ≥ 0 with tr(F ρ_star) = 0 gives local projectors annihilating Ω.) Exactly what is implied, and what is not?
2. **Frustration-free plus gapless.** Does that force z ≥ 2? Derive what you can, for example a variational argument: with a frustration-free H and a local "twist" excitation, the energy is ∝ k² by a Goldstone/twisting bound. State the assumptions: uniqueness of the ground state, translation invariance, locality. Where does the recalled theorem apply, and where not? Note that the vacuum need not be the ground state of the change: excited stationary states such as product states with negative-energy magnons exist. How does that loophole interact with quietness and with energy positivity?
3. **The loopholes, concretely.**
   - (a) A vacuum that is stationary but not the ground state, e.g. |0⟩^N under π-flux hopping, which has Dirac magnons at E = 0 with negative-energy states below. What is wrong with it physically (stability, records, heating)?
   - (b) Quietness only next to records (gating), while the vacuum is full rank elsewhere: does that help?
   - (c) Light as a composite (two-ripple bound state) over a calm product vacuum: any linear branch?
   - (d) Light not as an excitation of the change at all, but carried by the record-tick structure: argue briefly.
4. **Verdict.** State a precise tension theorem if one holds (with hypotheses), or the precise loophole that escapes it, and what it would cost in the axioms' register.

## Rules
- **Grading.** Grade every claim EXACT (proof), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED (a premise put in by hand) or COMPARATOR (literature from memory, never adopted). Be strict: if you only recall a theorem, grade it COMPARATOR.
- **Language.** Never say a possibility is "read" or that a "question is asked". Never present "records form on a beat or heartbeat" as adopted. Propose no axioms or imports as adopted; frame choices as owner decisions.
- **Compute.** This is an 8 GB machine with another agent running.
  - Every run: `nice -n 10`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all set to 1. Each run under 60 s and 300 MB.
  - Check `uptime` before each run, and run only if the 1-minute load is below 6.
  - Exact toys at most 12 qubits, or single- and two-excitation sectors on lattices up to 64² in 2D.
- **Files.** No git, no repo edits, no PRs, no review or audit lanes. Put scripts in `SP/c8/A39/`. If your sandbox blocks writing REPORT.md, return the full report as your final message.

## Output
A report with these sections:
1. Question
2. Answer: short, graded
3. Derivation
4. Checks
5. Real-physics match: comparators flagged
6. Open edges
7. Plain-language summary: one paragraph for the owner, no jargon. It must answer directly: can empty space be both quiet and carry light?
