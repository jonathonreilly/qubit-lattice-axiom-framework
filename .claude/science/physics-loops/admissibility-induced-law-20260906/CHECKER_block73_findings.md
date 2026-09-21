# Block 73 — control and findings (2026-09-21)

1. Disjoint machinery (`specs/supervisor_control_block73_only_momentum.py`): no symbolic algebra — sampled linear systems and singular values. It checks T1 in a form the runner does not (the full commutant's dimension at reach 1, 2, 3 against the count of `a + cH`), and T2, T3 by rank and residual.
2. **A wrong count in the control's first run (supervisor).** At reach three the null space came out 132 against 88: 60 sampled wave vectors give 240 equations for 252 unknowns. Raised to 200 wave vectors; all three counts then agree, with fourteen orders between kept and dropped singular values.
3. **A claim withdrawn before writing (supervisor).** Least reach for ALL couplings with an exactly conserved response was considered and not claimed: a response that is divergence-free on every stationary state makes the pure-gauge part of the coupling a commutator with the walk, but the generator need not be local, and the note's class (N1.1) says so.
4. Finding folded: the runner's E1 mutation was a flipped constant; replaced by a computed condition (the first-order coefficient at each zero).
5. Finding folded: T3(b)'s proof first said "forced to zero in two steps"; it now lists which rotation kills which coefficient.
6. Finding folded: the note's W3 numbers were first taken from a scratch run with a different random stream; replaced by the committed output's.
