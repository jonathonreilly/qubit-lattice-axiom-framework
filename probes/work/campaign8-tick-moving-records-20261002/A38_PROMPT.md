You are lane A38 of an overnight, derivation-focused physics exploration ("Campaign 8"). Topic: **patterned calm backgrounds and light-like ripples.**

Can an empty background whose spots point in different directions on different sub-grids (a pattern held in the STATE, 1 of 8 translates) be exactly calm under a law that treats every spot and turn alike? And can its ripples then see the π twist on every face, which light-like (Dirac-cone) motion needs, with no sign pattern painted onto the law?

Work derivation-first, then use small exact numerics.

## Background (read primary files; do not trust summaries)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- `SP/c8/BRIEF.md`: the axioms verbatim. Q3 means possibilities turn along with the grid (soldered, "glued" covariance). Also the owner's readings and the discipline rules.
- `SP/c8/A31/REPORT.md` and its ERRATA. Key points:
  - **D1.** Glued homogeneous NN pair terms are J σ·σ + K σ^aσ^a (compass) + D(σ_x×σ_{x+a})_a (DM).
  - **D2.** A UNIFORM product vacuum |n⟩^⊗ is calm only for K = 0, and also D = 0 once a −n record exists.
  - **D3.** Over a uniform calm product vacuum single ripples form one band, so there is no cone.
  - **D4–D5.** A cone needs π flux per face; supplied KS signs are either physical or privilege an axis.
  - **Open edge 5:** "Patterned calm product vacua when compass terms are allowed" is UNTESTED. That is your main target.
- `SP/c8/A34/REVIEW.md` C56: glued star terms beyond pairs (e.g. the chiral three-spin term) also keep aligned states calm.
- `SP/c8/A33/REPORT.md` and its ERRATA, especially:
  - the parity formula: plaquette flux = |t_xa|²|t_ac|²·p(x)p(c), where p is the ripple's parity under the face-diagonal half-turn at the two fixed corners;
  - π on every face is symmetry-allowed in a period-2 vacuum if p_V ≠ p_F and p_E ≠ p_C (roles V vertex, E edge, F face, C cube of the 2×2×2 cell).
- `SP/c8/A34/REVIEW2.md` C89: on one qubit per site, vertex and cube places carry only the trivial one-dimensional label, and σ^axis at edge and face places has parity −1. Its 8-band π-flux toy (`SP/c8/A34/c7_parity_route.py`) shows unequal bond strengths keep the cone, while unequal role energies gap or split it.
- `SP/c8/A25/REPORT.md`: the field's role layout F6 (vertex, edge, face, cube roles of the period-2 cell).
- **Standard mechanism (COMPARATOR, from memory, not adopted).** Magnons over a non-collinear spin texture hop with Berry phases set by the local spin directions, i.e. an emergent gauge field (spin chirality). A suitable texture can give π flux per plaquette.

## Tasks
1. **Patterned calm product states.** Consider period-2 product states, with one spin direction m_r for each of the 8 sites of the 2×2×2 cell, under a homogeneous glued covariant NN law H = J σ·σ + K σ^aσ^a + D(DM). Optionally add glued covariant three-spin star terms (C56).
   - Find (exactly, or by exact numerics) which textures are EXACT eigenstates (calm). Single-flip and double-flip amplitudes must vanish, as in A31 D2's method.
   - Respect the state-level pattern condition: the texture may break translations down to 2Z³, and the 24 turns may act on it only up to a translation. The LAW must stay pattern-free.
   - Consider the role layout of A25 (V, E, F, C) as a natural candidate.
2. **Records.** Calmness next to records, i.e. formation weights that annihilate the background's star marginals (A9/A28 quiet criterion). Which record contents keep it calm (cf. A31: −n records force D = 0 for uniform vacua)?
3. **Magnons.** For each calm texture found, build the single-flip (magnon) Bloch Hamiltonian (8×8 for period 2).
   - Compute the gauge-invariant plaquette fluxes (Berry phases) on every face type.
   - Find the band touchings: linear and isotropic? at the background's energy (zero cost)? how many cones?
   - Compare with A33's parity conditions and A34 c7's tuning conditions (equal role energies).
4. **Readability.** Can records tell the 8 translates apart, and at what order (cf. A16, A31 c3)?
5. **Verdict.** Does any patterned calm background give light-like single ripples with no law-level pattern? If not, state the exact obstruction found, for the exact class searched. If yes, what is supplied?

## Rules
- **Grading.** Grade every claim EXACT (proof or exact arithmetic), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED or COMPARATOR (literature from memory, never adopted). Negative search results are EXACT only for the precisely stated class.
- **Language.** Never say a possibility is "read" or that a "question is asked". Never present "records form on a beat or heartbeat" as adopted. Propose no axioms or imports as adopted; frame choices as owner decisions.
- **Compute.** This is an 8 GB machine with other agents running.
  - Every run: `nice -n 10`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all set to 1. Each run under 60 s and 300 MB.
  - Check `uptime` before each run; run only if the 1-minute load is below 6.
  - Use Bloch matrices up to 16×16, exact small systems up to 12 qubits, and optimization over the 8 directions plus (J, K, D).
- **Files.** No git, no repo edits, no PRs, no review or audit lanes. Put scripts in `SP/c8/A38/`.
- **Time box.** About 60 minutes. Return what you have, graded honestly. If your sandbox blocks writing REPORT.md, return the full report as your final message.

## Output
A report with these sections:
1. Question
2. Answer: short, graded
3. Derivation
4. Checks
5. Real-physics match: comparators flagged
6. Open edges
7. Plain-language summary: one paragraph for the owner, no jargon
