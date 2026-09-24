# Referee: filling-between-the-a-terms-levels-chiral-content a2

Worker `w-macbookpro90c72-jb764` (`grok-4.6`). Author `w-macbookpro9927a-j4067` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed. On an even torus the free sea below `a0` holds `N − z/2` records, and every Fermi level in `(a0+2a, a0+6a)` holds at least `N + 6 + z/2`. One record per site allows at most `N` records, so that filling does not exist. At exactly `N` records the hard-core generator of either composition is the constant `N a0`.

The task's single-sense filling is not claimed, and the interacting anomaly theorem stays assumed. That matches the attempt.

## What was checked

- **Corners.** The eight nodes sit at `a0 + 2a(3 − 2|n|)`, with multiplicities `1:3:3:1` and sense `(−1)^|n|`. Four of each sense, net zero. `Σ χ_n L_n^p` is `0, 0, 0, 384 a^3`.
- **Record counts.** Exact band arithmetic on the `2^3`, `4^3` and `6^3` grids, for `(a0, a) = (1/3, 1/10), (0, 1/4), (−2/5, 2/3)`. The identity `#(E < a0) = N − z/2` holds, `z` is even, and the open windows lie on the claimed sides of `N`. On `4^3` at `a = 1/4` one has `z = 12` and `58` states below `a0`, so the `z` term is doing work. On the odd `3^3` the same parameters give `26` states below `a0` out of `54`, with `z = 0`: the wrap of an odd cycle is not a bipartition, and even sides are required.
- **Staggered term.** On every basis vector of `4^3`, `ε` anticommutes with `A`, `(A + mε)^2 = A^2 + m^2`, and `ε T_1` anticommutes with `A + mε`. `A` has no on-site piece. Plane waves fix the normalization: `k = 0` has `A = 6a`, and `k = π/2` has `A = 4a + σ_1`.
- **Bipartition.** `Σ ε = 0` on even tori and not on the `3`-torus, so a full lattice of site terms is `N a0`.
- **Full ring.** Four records on a ring of four, symmetric and antisymmetric: the generator is exactly `4 a0` on all `16` coin states.
- **Holes.** A hop `a I + σ_j/(2i)` has column radius `|a| + 1/2` on the first two axes and `√(a^2 + 1/4)` on the third, and the third is no larger. On the ring, one and two holes give hermitian generators, at most two hops per hole, and float widths `2.039 ≤ 2.4` and `3.533 ≤ 4.8`. The cubic bound is six such hops per hole.
- **Lower window.** At `a = 1/20`, `56` of the `1728` momenta on `12^3` have `|sin k| < 12a`. The `6^3` window at `μ = −4a` leaves `6` holes against the bound `16`. A float count on `48^3` gives `0.0160` states per site inside `6a` of `a0`, under the zone bound `0.1375`.

## Consequence

The free comparator between `a0 + 2a` and `a0 + 6a` asks for more records than there are sites. Under the supplied hard-core rule that filling is absent, and the middle of an even torus is the constant `N a0` once every site is occupied.
