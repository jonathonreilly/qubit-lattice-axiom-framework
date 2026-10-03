You are lane A42 of Campaign 8, a daytime follow-up the owner asked for on 3 October. Topic: **does the hard limit (Theorem N) need the owner's Q3 gluing?** Work derivation first, with tiny exact checks only. Time box: 60 minutes.

SP = /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
The repo is at /Users/jonreilly/Projects/Physics/.claude/worktrees/focused-noyce-9a3983, ref origin/main (b6fda5ae1d), and is READ-ONLY. Read files with `git -C <repo> show origin/main:<path>`. Do not fetch.

## Context (read the primary files; summaries are not enough)
- `SP/c8/A20/REPORT.md`:
  - §3B: Theorem N, proof N1–N6, corollary N-d;
  - §3C: Clifford ticks;
  - §3F: the obstruction and relaxations;
  - §6: open edges.
- `SP/c8/A21/`: the independent check of Theorem N. Read REVIEW_FINAL.md if present.
- `SP/c8/CHECK/G1.md`, rows R1–R4 and §4 item 1. These cover the repo's archived July 2026 QCA notes, which have NO claim authority; cite them as prior art and check whatever you use. All paths are on origin/main:
  - `archive/notes/docs/work_history/repo/review_feedback/CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md`. It is an exact census of range-one, six-neighbour, one-qubit Clifford QCAs, sorted by onsite rotation action:
    - site-only: 18 neighbour-coupled skeletons in 4 classes, two of them "propagating companion rules";
    - sign quotient: 2;
    - full Pauli-axis quotient: 0.
    The Clifford census sees Pauli axes only up to sign.
  - `archive/notes/docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md`: with one number-preserving fermion mode per site, a covariant tick is an onsite phase; a six-mode escape exists.
  - `archive/notes/docs/work_history/repo/review_feedback/FUNDAMENTAL_ONE_QUBIT_QCA_COMPILATION_CYCLE12_NOTE_2026-07-14.md`.
- The soldering menu on main: `docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md`. It lists four actions: trivial (unsoldered), sign twist (A1+2A2), axis soldering (A2+E, through the axis permutation) and full soldering (T1). It states "No action is adopted."
- Axioms, quoted verbatim from `docs/MINIMAL_AXIOMS_2026-06-29.md`:
  - Qubit: "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone."
  - Qualification: "A law privileges no states."
- Law-level readings of Qubit's second sentence are parked in `docs/repo/DEFERRED_DECISIONS.md` §2, standing default "not adopted, either way". State any result that leans on such a reading as conditional on it.

## Setting (as in A20)
- One qubit per site of Z³.
- A tick α is an automorphism of the quasi-local algebra, so it is reversible.
- Nearest-neighbour reach: α(A_x) ⊆ A_{N̄(x)}, where N̄(x) is x and its six neighbours.
- α is covariant under translations, and under the 24 proper rotations about each site with a stated onsite action, on every tick.

## Questions
1. **Possibility covariance.** Add the condition that α commutes with every global internal rotation (the same SU(2) turn applied to every site's possibilities).
   - Under each of the four actions, is α = id? The expected short exact proof: the only SU(2)-invariant unital subalgebras of M₂ are C·1 and M₂, and then N1 plus a half-turn that swaps two neighbours removes all neighbour support.
   - Check carefully that this half-turn argument applies under the trivial action, and check the onsite step.
   - Is "invariance under every internal rotation" stronger than the axiom text? Is a weaker invariance enough?
2. **Axis soldering and sign twist, without possibility covariance.**
   - Redo N2–N6 with the correct onsite action of each rotation. For instance, under A2+E a quarter turn about axis a acts on the Bloch vector as a signed swap of the other two axes; work out each case exactly.
   - Say where each step survives and where it breaks.
   - Either prove α = id, or construct an explicit nontrivial nearest-neighbour covariant tick (non-Clifford allowed).
   - Cross-check against the archived Clifford census.
3. **Unsoldered (site-only) action.** The archive has neighbour-coupled covariant Clifford ticks, two of which spread content.
   - Show, or refute, that every nontrivial nearest-neighbour covariant tick under the trivial action fails possibility covariance.
   - Find the weakest symmetry of the possibilities that removes them all: for example the flip (σ → −σ, all three), a finite internal subgroup such as the Pauli group, or the cubic group acting internally.
   - Say in plain words what those ticks privilege.
4. **Fermionic combination.** Take one fermion mode per site with the graded (CAR) product. Ticks are parity-preserving automorphisms with nearest-neighbour reach that are translation and rotation covariant.
   - Rotations act on one mode by at most a phase, so the soldering menu changes. Say what replaces it.
   - The archive covers number-preserving ticks. Do number-violating (Bogoliubov) or interacting nearest-neighbour covariant ticks move anything? Consider Majorana-type shifts with two Majoranas per site; in 1D the Majorana translation is a nontrivial fermionic QCA.
   - Does the support lemma N1 survive grading, given that odd elements anticommute?
5. **Plain verdict.** In one sentence, state exactly which set of hypotheses makes "nothing can move" true. Then list which escapes each relaxation opens.

## Grades
EXACT (proved), CHECKED (finite computation), ARGUED, or COMPARATOR (literature, not adopted). Use literature only as a comparator, cited from memory and marked so: GNVW 2012 flow index; Fidkowski–Po–Potter–Vishwanath on fermionic QCA; Haah; Freedman–Hastings.

## Compute
Tiny checks only: exact algebra on small matrices, Pauli strings, sympy.
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
- Put scripts in `SP/c8/A42/`. If your sandbox blocks writing `SP/c8/A42/REPORT.md`, return the full report as your final message. Otherwise write it and also return it.

## Output
1. Question
2. Answer, graded
3. Derivations: per action, then fermionic
4. Checks: scripts and results
5. Open edges
6. Plain-language summary for the owner, in 4–6 sentences with no jargon