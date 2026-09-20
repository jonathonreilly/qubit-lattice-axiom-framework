# Block 37 — refuting pass and findings (2026-09-20)

1. **Integer program (disjoint machinery).** `c*(η, 333) = 10/9`, optimal tree `E = 10`, `A = 9`, `S = 1`. Agrees with the dynamic program.
2. **Rooted values with the level cap (integer program).** `0, 0, 0` at the three predecessors, `1` at `333`. Agrees.
3. **Local search around the witness.** No realization with a constant above `10/9` (see the control's output for the count). Not a claim: `c*` may still exceed `10/9`.
4. **Finding folded.** The first census of mutations showed `marks_wrong` failing in two families, because the values family consumed the mutated realization; the values family now builds the declared realization itself.
5. **Finding folded.** "Exactly `10/9`" rested on three sampled budgets below it; replaced by the monotonicity argument in T2.
