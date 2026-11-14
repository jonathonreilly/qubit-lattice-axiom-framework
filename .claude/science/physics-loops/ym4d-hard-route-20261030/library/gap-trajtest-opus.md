lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T04:53Z

# gap-trajtest-opus (row 974): GUIDE refutation test of (LSI-traj-seed) through X(2m+2; B)

Queue row 974 of FINISH.md (attack A2 of row 970). Pinned commit 27a48373b. Started 2026-11-14T16:53Z.
A run guides or refutes; it proves nothing.

## Status log
- 2026-11-14T16:53Z: file created with plan.

## Plan (at most eight steps; one per response)
1. Read row 970 section 7.3 ((LSI-traj-seed)_a, (EC-traj)), Proposition HC and X(2m+2; B) in gap-direction-max.md,
   Corollary BR-J (K_a) and row 954 (m_G >= K_a). Write the exact target quantity and the needed rate.
2. Read the slab / chain code in library/guide/ (lanes 950-970); choose the estimator of X; time a smoke test.
3. Write the pre-set criteria (REFUTED / NOT REFUTED / INCONCLUSIVE) and controls in this file BEFORE any run.
4. Smoke run at side 4, beta 2.3; check controls.
5. Main runs: sides 4-8, beta 2.3 and 2.6, sample size N and 2N; record error bars.
6. Fit the decay rate in m; compare with the needed rate.
7. Verdict against the pre-set criteria; what is left.
8. RESULT line.
