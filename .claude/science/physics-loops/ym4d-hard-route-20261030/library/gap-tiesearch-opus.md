lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T04:51Z

# gap-tiesearch-opus (FINISH row 973): GUIDE refutation test of box-uniform (TILT-COV-sup) at beta 2.3 and 2.4

Started 2026-11-14T16:51Z on Mac mini worker 2, pinned at a250c7f59. GUIDE level only: a run guides or refutes; it proves nothing.

## Plan (at most eight steps)

1. Read row 970 (library/gap-direction2-max.md sec. 3.4, 3.5, 4 A1, 7a), Lemma SUB, rows 950/952 runs and code (library/guide/lane952/, lane970/).
2. Write the criteria (REFUTED / NOT REFUTED) in this file before any run.
3. Set up library/guide/lane973/ by reusing lane952/lane970 code; dry-run small sizes.
4. Control: reproduce one beta 2.6 value of row 950/970 within 5 percent.
5. beta 2.4: tie-mode variance on sides 8..16, frozen slices incl. reduced-symmetry ones (as row 952).
6. beta 2.3: same.
7. Analysis: per-step growth factors vs 1.25; verdict per beta.
8. RESULT line.

