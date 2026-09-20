# Block 36 — refuting pass and findings (2026-09-20)

Machinery disjoint from the primary: (i) a single-site acceptance sampler of the equilibrium laws named by T1 and T2, against the chains' exact heat bath; (ii) an exact enumeration of the infrared bound on a two-valued instance, which tests the normalization of T3 independently of the proof.

1. **T2 against equilibrium.** Seven-site chain plateau against one layer of the doubled graph: `0.7699 / 0.7706` (β = 1, L = 12), `0.8601 / 0.8594` (β = 1.5), `0.6451 / 0.6455` (β = 0.75, L = 16). No discrepancy.
2. **T1(b) against equilibrium.** Six-site chain's space-time checkerboard against the static law: `0.6919 / 0.6928`, `0.8210 / 0.8206`, `0.4507 / 0.4503`. No discrepancy. The tick-`t` configuration itself is NOT the static law (it is `μ_A ⊗ μ_B`); the note says so.
3. **The ordering coupling against the executed onset.** `β₀ < 0.5914`; no plateau at `β = 0.5`, a plateau at `β = 0.6`. Consistent (a proved ordering coupling below the true onset would have refuted the proof).
4. **Infrared bound, exact.** Every nonzero mode of both bands on the doubled 4- and 6-cycle satisfies the bound; largest ratio `0.318`.
5. **Finding folded.** The first draft carried the number `0.5931` from the worker's own tail bound for `I₀`; the supervisor did not re-verify that tail bound and replaced it by block 22's bracket (open PR), stating the dependence.
6. **Finding folded.** The bound on the plane sums was restated with `m₁² + m₂² ≥ 2m₁m₂` so that it needs no lattice-sum constant.
7. **Not checked here.** The power-series step of the reflection inequality for the sphere menu is proved, not enumerated; the exact instance is two-valued.
