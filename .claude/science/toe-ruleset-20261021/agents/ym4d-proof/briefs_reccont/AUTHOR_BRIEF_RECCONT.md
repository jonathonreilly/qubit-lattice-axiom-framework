# Author brief REC-CONT: prove the continuation step of the reconstruction theorem (E0′ ⇒ L-CONT)

Lead: Claude Opus 5.5, 2026-10-29. One Codex author context on the Mac mini, followed by a fresh reviewer.
Follow the process in PROCESS_LIGHT.md: edit in place, pre-register numerical checks only, keep review independent, and rebuild results rather than cite them.

## Context
REC_LIB.md, which landed after review (REVIEW_REC_LIB.md and REVIEW_REC_LIB_R2.md), rebuilds the Osterwalder–Schrader reconstruction as a **conditional** library:
- the scalar conditional reconstruction is CONFIRMED;
- the tensor boost bound has been corrected;
- the remaining residue is **E0′ ⇒ L-CONT**. This is the step from the linear growth condition to analytic continuation of the Schwinger functions into the forward tube, with bounds strong enough to make the boundary values tempered.

This is the hard core of OS II, and it is the only thing between REC-LIB and an unconditional reconstruction theorem.

## Target
Use the exact statement of L-CONT as it appears in REC_LIB.md; quote it. Prove it for the several-field, tensor, ^0𝒮 setting that REC_LIB uses, with OSLEAF55's E0′ constants (s, α, β) carried explicitly.

## Proof route (structure recalled from memory, marked [m]; every step must be rebuilt)
1. Start from Laplace-transform analyticity in Re t_k > 0, which comes from the semigroup and is already in REC_LIB.
2. Extend inductively to the domains 𝒞_N. These grow by combining analyticity in the time differences with Euclidean rotation covariance in time–space planes.
3. Bound the continued functions on each 𝒞_N with explicit dependence on n and N. The linear growth condition E0′, in which the seminorm order grows linearly in n, is exactly what makes the bound summable: show where it enters, and give the n!-type factors.
4. Take the union of the 𝒞_N to get the forward tube, or a domain whose envelope of holomorphy is the forward tube. If this uses a Bochner tube theorem or a holomorphy-envelope result, rebuild it as a library lemma in this file.
5. Prove the polynomial-in-distance-to-boundary bounds, and from them temperedness of the boundary values.

Literature is for method only: Osterwalder–Schrader II, Glaser, and Zinoviev's alternative proof. Credit them by name. Nothing from the literature may be load-bearing.

## Write
- **REC_CONT.md**: the full proof, split into library lemmas, each marked PROVEN, ARGUED or OPEN, with explicit constants. It must include a "Statement match" against REC_LIB's L-CONT and OSLEAF55's E0′, and an "Open residue" section.
- **REC_LIB.md**: update the L-CONT residue status in place, pointing to REC_CONT.md. Change nothing else in it.
- **REC_CONT_LOG.md.**
- Numerical checks are optional. If you run any:
  - write checks/reccont_criteria.md first;
  - run them with nice, BLAS=1, RSS under 2 GB and no pools;
  - run only when at least 50% of memory is free and load is below 20.

## Rules
- Edit only the files listed above.
- No commits, no audit or ledger files, no axiom edits.
- Final message: under 300 words.
