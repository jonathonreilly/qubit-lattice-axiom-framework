# Goal

Repair the failed Step 3 Lieb-Robinson tail estimate in
`docs/AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`
without promoting spatial clustering.

The audit blocker has two parts:

1. Provide a correct LR/Poisson-tail estimate for the stated `J_*`,
   `D_int`, and `R_int` constants.
2. Separately supply spatial or target-state gap authority before any
   L2 spatial clustering statement is promoted.

This branch addresses only part 1. It leaves part 2 explicitly open.
