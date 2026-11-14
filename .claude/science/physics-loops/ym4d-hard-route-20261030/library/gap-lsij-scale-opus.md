lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T22:07Z

# gap-lsij-scale-opus (row 954): does the two-slice Poincare ratio R_J stay bounded as the box grows?

Claude Opus 5.5 max, Mac mini worker 2, started 2026-11-14T10:07Z, pinned at branch commit 2a9e82c69.
GUIDE item (refute only). No statement here is a proof step of the chain. A run may refute or guide; it proves nothing.

Credit: the (LSI-J) / (LSI-J-seed) framework is row 947 (`library/gap-fc-max.md`, Claude Fable 5.2 max), built on rows 931-946 and on the Sussman-Alpoge complete account (CA-I/II/III at 31a47c543775, authored with Claude and Codex). Any statement or construction taken from them is credited where used.

## Plan (at most eight steps; one step per response)

1. Read row 947 (`library/gap-fc-max.md`): Theorem BR, Corollary BR-J, (LSI-J-seed), its test, the definition of the two-slice law, of grad, of K_a, and the seed threshold 1/(2 beta K_a). Read check 943's finite-cylinder caveat and row 946's code under `library/guide/lane946/` for reuse. Write the exact definitions used here (Section 1).
2. Pre-state the measurement, the observable span, and pass/fail criteria before any run (Section 2). Free-photon exact formula for R_J by hand (Section 3).
3. Write the code (SU(2) and U(1) heat-bath/overrelaxation on L^3 x T, two-slice extraction, gradient estimator, generalized-eigenvalue variational ratio). Unit tests: free-photon and one-plaquette calibrations (Section 4).
4. Controls: compact U(1) at beta about 1.5, L = 4..10; compare with the photon formula (Section 5).
5. SU(2) runs at beta 2.3, L = 4, 6, 8, 10 (12 if cheap) (Section 6).
6. SU(2) runs at beta 2.6, same sides (Section 6).
7. Analysis: R_J versus L with errors, scaling exponent fit, comparison with 1/(2 beta K_a), finite-cylinder handling (Section 7).
8. Verdicts per statement and the RESULT line (Section 8).

## State of work

(updated in place after each step)

- Step 0 (2026-11-14T10:07Z): file created; FINISH row 954 read; no earlier run of this item exists at 2a9e82c69.
