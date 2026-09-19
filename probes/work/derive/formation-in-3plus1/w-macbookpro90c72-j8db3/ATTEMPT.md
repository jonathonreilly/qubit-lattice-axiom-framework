# formation-in-3plus1, attempt 1 (worker w-macbookpro90c72-j8db3, model grok-4.6)

Plan: settle the linear dichotomy (task (c) and the linear half of (b), (d))
exactly, and not claim nonlinear LRO. Objects: formation on the event lattice
`Z^{d+1}` in level order, `n = d+1` predecessors `{x, x−e_j}_{j=1..d}` wait:
the LEAD is a record at `x` formed from `x−e_1,…,x−e_4` on `Z^4`, i.e. four
backward neighbours, level planes three-dimensional. Linear
`φ(k) = (1 + e^{ik_1} + e^{ik_2} + e^{ik_3})/4`. Simulation in
`probes/lib/formation_levelplane.py` is evidence address only.

## (1) The statement attempted

**Dichotomy.** For linear formation on a `d`-dimensional level plane,
`1 − |φ(k)|² = k^T M k + O(|k|^4)` with `M` positive definite. The zero-mode
integral `∫_{|k|<1} d^d k / (k^T M k)` converges at the origin if and only if
`d > 2`. Hence `3+1` (`d=3`, event lattice `Z^4`) is the lowest dimension whose
linear equal-level kernel is a three-dimensional Green function (`1/r` at large
equal-level separation). The campaign's `Z^3` law (`d=2`) is logarithmic.

**Drift.** `∂φ/∂k_j |_{0} = i/4`, so the zero mode of the 3+1 linear theory
drifts at velocity `(1,1,1)/4` per level.

**Not claimed.** Sphere LRO (`liminf E[m_t · e] > 0`); two-sided nonlinear
`S(k)` bounds; the physical reading of the non-equilibrium response.

## (2) Steps

**Step 1 — `φ(0)=1` and drift (CHECKED as E0).**
`φ = (1+e^{ik_1}+e^{ik_2}+e^{ik_3})/4`. At `k=0`, `φ=1` and `1−|φ|²=0`.
`∂φ/∂k_j|_0 = i/4`.

**Step 2 — Hessian of `1−|φ|²` at 0 is positive definite (CHECKED as E1).**
The Hessian is `(1/8)` times `[[3,−1,−1],[−1,3,−1],[−1,−1,3]]`, eigenvalues
`1/8` (once) and `1/2` (twice). Cauchy identity
`4|k|² − (1·k)² = |k|² + Σ_{i<j}(k_i−k_j)² ≥ 0`, vanishing iff `k=0`.

**Step 3 — integral test (PROVED).**
In polar coordinates `∫_{|k|<1} d^d k / |k|² ∼ ∫_0 k^{d−3} dk`, which converges
at `0` iff `d−3 > −1` iff `d > 2`. Combined with Step 2 (equivalence of
`k^T M k` and `|k|²`), the zero-mode sum is finite iff `d > 2`.

**Step 4 — campaign `d=2` (CHECKED as E3).**
`φ = (1+e^{iq_1}+e^{iq_2})/3`, Hessian of `1−|φ|²` at 0 has eigenvalues
`2/3, 2/9 > 0`. The integral is logarithmic (`d=2`).

**Step 5 — LRO (not attempted).** Comparison with the linear model via
`A(κ)/κ` has the same sign obstruction as in plane-memory-loss a4 (`|S| ≥ n|m|`
and `A` increasing). Chessboard/Lyapunov not attempted.

## (3) First failing step of LRO

The linear comparison (task route: block 27's sign lemma) fails for the same
reason as on `Z^3`: triangle inequality gives the wrong sign for an upper bound
on `|m'|`. The linear theory *conserves* the uniform mode (`φ(0)=1`) and so
cannot by itself prove a strictly positive liminf of `|m|` either — it only
says the kernel is summable, which is necessary for a nonzero infinite-volume
magnetization in a Gaussian field, not sufficient for the sphere PCA.

## (4) What would finish it

A Lyapunov or energy-entropy argument for the plane average of the sphere PCA
at large `β`; two-sided `S(k)` bounds in the ordered phase; the `d=2` vs `d=3`
dichotomy for the *nonlinear* sphere (block 26 vs the LEAD simulation).

Nothing here edits notes or runners.
