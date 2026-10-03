You are lane A33 of an overnight, derivation-focused physics exploration ("Campaign 8"). Topic: **can the calm empty background itself supply the π-flux pattern that light-like matter needs?** This is A31's top open problem. The method is an exact F₂ (Clifford/stabilizer) search with low compute.

## Background (read the primary files; do not trust summaries)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- `SP/c8/BRIEF.md`: the four axioms verbatim and the owner's readings. Q3 means possibilities turn along with the grid (soldered covariance).
- `SP/c8/A31/REPORT.md`, the assembly v2. Read §3 Task 2, Task 6, D2–D5, D14 and Theorem S. It establishes:
  - **D2/D3.** Over a calm PRODUCT vacuum, a homogeneous glued NN pair change must be Heisenberg, whose ripples form one analytic band (z = 2) with no cone (EXACT).
  - **D4/D5.** A cone needs π flux per face. Supplied as a KS sign pattern, it is either physical, so records can show it, or it privileges a possibility axis.
  - **Theorem S.** No π-flux sign pattern can share the gravity field's 2×2×2 role layout (A25 F6).
  - **D14.** A20's two covariant calm stabilizer vacua, the star and face states, have IMMOBILE single defects: no Pauli moves a lone defect on 6³, a fracton-like signature.
- `SP/c8/A20/REPORT.md` §C3 and the scripts `SP/c8/A20/cliff_*.py`, `pauli.py`, `grp.py`, `wsym.py`: the classification of O-covariant, translation-invariant stabilizer states on one qubit per site (the free module Ru₀ ⊕ Ru₂; the star and face states). You may reuse or adapt this code; cite what you reuse.
- `SP/c8/A31/c5_defects.py`: A31's F₂ rank test for defect mobility.
- `SP/c8/A25/REPORT.md`: F6, the field's 1-of-8 role layout, a superselected state label under a covariant law. A state-level pattern of this kind is regarded as much milder than a law-level pattern (A31 ledger ranks 3 vs 4).

## The target
Find a vacuum state Ω on Z³, one qubit per site, ordinary tensor product, such that:
1. **Law covariant.** There is a homogeneous, soldered-covariant (all 24 proper turns, with possibilities turning along: Q3), star-local or short-range Hamiltonian H for which Ω is an exact eigenstate ("calm": stationary). Prefer frustration-free (each local term annihilates Ω or has it as an eigenstate), since formation weights must be able to annihilate the vacuum's star marginals (A9 quiet criterion; A28 edge floor).
2. **State-level pattern only.** Ω may break translations down to 2Z³ (8 translates, like F6), but the LAW may not carry any pattern.
3. **Mobile excitations.** Some local, law-covariant operator moves a single elementary defect (excitation) by a lattice vector. If only composites move, say so.
4. **Emergent π flux.** For mobile defects, compute the group commutator of the x-, y- and z-movers around a plaquette. A phase of −1 on every face means the vacuum supplies π flux, i.e. a projective translation symmetry for the excitations (COMPARATOR: Wen's projective symmetry groups; a toric code with a background charge per site). Also report whether the movers' algebra gives an isotropic linear cone once a covariant hopping Hamiltonian is built from them (two or more bands, anticommuting velocity matrices).

## Plan (adapt as needed; record what you actually did)
1. **Translation-invariant class (A20 C3).** Confirm or extend the classification of covariant stabilizer vacua at low degree.
   - For each, test calmness (frustration-free covariant parent), defect mobility (F₂ rank test as in A31 c5, on L = 4, 6, 8), and the mover commutator phases.
   - Expectation from A31: the star and face states fail mobility. Check whether other members of the module, or products and sums at higher degree, behave differently.
2. **Period-2 class.** Stabilizer states invariant under 2Z³ translations, and covariant under the 24 turns about some site up to an even translation; that is, the pattern is a state label.
   - Enumerate generators supported on small clusters (for example a 2×2×2 cell plus neighbours). Impose the stabilizer (commuting, independent, full rank) and covariance conditions.
   - Then run the same calm/mobility/flux tests.
   - Keep the search exhaustive within a stated finite class, so that a negative result is an exact statement about that class.
3. If nothing is found, state the exact class searched and any structural obstruction you can prove. For example: commuting-projector (stabilizer) parents always give immobile single defects in some class, or covariance plus one qubit per site forbids string movers.
4. If something is found, build the covariant hopping Hamiltonian from the movers and compute its band structure near the cone.
   - Check calmness of the full change (Ω stays an eigenstate).
   - Check whether records (Z- or n-type) can tell the 8 translates apart once two records interact (cf. A16's test).

## Rules
- **Grading.** Grade every claim EXACT (proof or exact F₂ arithmetic), CHECKED (numerics in a stated toy), ARGUED, SUPPLIED or COMPARATOR (literature from memory, never adopted). A negative search result is EXACT only for the precisely stated finite class.
- **Language.**
  - Never say a possibility is "read" or that a "question is asked".
  - Never present "records form on a beat or heartbeat" as adopted.
  - Propose no axioms or imports as adopted. Frame choices as owner decisions.
- **Compute.** This is an 8 GB machine with another agent running.
  - Every run: `nice -n 10`, with OMP_NUM_THREADS, OPENBLAS_NUM_THREADS, MKL_NUM_THREADS and VECLIB_MAXIMUM_THREADS all set to 1. Each run under 60 s and 300 MB.
  - Check `uptime` before each run, and run only if the 1-minute load is below 6.
  - F₂ linear algebra on tori up to 8³ is fine. No dense state vectors beyond 2^20.
- **Files.** No git, no repo edits, no PRs, no review or audit lanes. Put scripts and outputs in `SP/c8/A33/`.
  - Your sandbox may refuse to let you write REPORT.md. If so, return the report as your final message; the coordinator will save it.

## Output
A report with these sections:
1. Question
2. Answer: short, graded
3. Derivation and search: classes searched, exact statements
4. Checks: script, run, numbers
5. Real-physics match: comparators flagged
6. Open edges
7. Plain-language summary: one paragraph for a non-specialist owner

Return it as your final message.
