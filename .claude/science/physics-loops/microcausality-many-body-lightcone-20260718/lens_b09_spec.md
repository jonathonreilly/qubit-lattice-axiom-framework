# Combined adversarial lens — block09 (matrix-fiber trace-norm lemma and feed)

Role: hostile referee + independent mathematician. Attempt to REFUTE the note. Report BLOCKER / MAJOR / MINOR with exact sentences/gates attacked and concrete counterexamples or fixes. State survivals explicitly. Cross-family check (no Opus worker was used this block; the supervisor's ground truth is in the loop pack).

Files (read-only):
- docs/MICROCAUSALITY_MATRIX_FIBER_TRACE_NORM_LEMMA_AND_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md
- scripts/microcausality_matrix_fiber_trace_norm_lemma_and_feed_2026_07_18.py
- docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md (the sibling being extended)

Attack surfaces:
1. THE LEMMA: ||sum k_ab c†_xa c_yb + h.c.|| = ||k||_S1 for x != y. Attack hard: recompute independently on your own instances (include complex k, n_f = 3 if feasible, degenerate singular values). Is the SVD/mode-rotation proof airtight (does the rotation preserve CAR for COMPLEX U, V — the runner gates a real orthogonal instance only)? Do the rotated hops really commute (they share no modes — but check the h.c. cross terms)? Joint spectrum = sums — justified?
2. On-site: is max(sum lambda+, sum lambda-) exactly right? The <= S1 direction?
3. The feed: does multiplying every step by n_f really work (on-site AND pair, shell sums unchanged)? The 585 n_f value? Does uniformity really carry (n_f fixed across backgrounds)?
4. Scope: the CT-note-has-no-fiber claim (verify by searching that note if accessible via the sibling's quotes); the sharper-data remark; non-claims completeness.
5. Runner: complex-rotation gap (M2 is real orthogonal only), n_f = 2 only (lemma claimed for all n_f), gate strength vs descriptions, manifest, needles.
6. Overlap: does any landed note already prove the trace-norm identity? Is it genuinely new?

House conventions: axioms supply no dynamics; bounded_theorem notes claim exactly what runners gate; N1-N8 with ATTEMPTED markers and Status; presence needles are not correctness oracles.
