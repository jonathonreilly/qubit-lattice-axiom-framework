# GOAL — block 22: block 19's strong-coupling threshold sharpened — `3G(0) < 76/100` by exact return counts of the cubic walk with an explicit tail bound; the kernel's window becomes `[√3/6, 76/100]` (2026-09-15)

**Owner directive (2026-09-15):** don't stop; assess the next lane at each conclusion; no subagents; derivations over computation.

**Why this block.** Block 19 (PR #8153) proves long-range order and the Green-function channel for `β > 3G(0)`, with the crude bound `G(0) ≤ √3π/8` giving `β > 3√3π/8 ≈ 2.04`; block 21 (PR #8155) proves no channel for `β < √3/6 ≈ 0.289`. The band is a factor seven wide. The constant `3G(0)` is the return sum of the simple random walk on `Z³`, `3G(0) = (1/2)Σ_n P_{2n}(0,0)`, and its partial sums are exact rationals; an explicit tail bound then pins it: `3G(0) < 76/100`, and the partial sum alone gives `3G(0) > 75/100`. The route's constant is thereby fixed within about a percent, the threshold improves by a factor `2.7`, and the window becomes `[√3/6, 76/100]`.

**Object.** `φ(k) = (1/3)Σ_i cos k_i` on `[−π, π]³`; `E(k) = 6(1 − φ(k))`; `G(0) = (2π)^{−3}∫ dk/E(k)`; `P_{2n}(0,0) = (2π)^{−3}∫ φ(k)^{2n} dk = 6^{−2n} · #{closed walks of length 2n}`; `S_N = Σ_{n ≤ N} P_{2n}`.

**Contract.**
- V1 (the return sum): `3G(0) = (1/2)Σ_{n≥0} P_{2n}(0,0)` (monotone convergence with the paired series `(1 + φ)Σ φ^{2m}`); `P_{2n} = 6^{−2n} C(2n, n) Σ_a C(n, a)² C(2(n−a), n−a)` (closed-walk counting with the Vandermonde identity).
- V2 (the tail bound): for every `n ≥ 1`, `P_{2n} ≤ (36/11)^{3/2}/(4π^{3/2} n^{3/2}) + 2e^{−4n/(3π²)}`, from `1 − cos u ≥ 11u²/24` on `|u| ≤ 1` (the quartic Taylor bound) and `1 − cos u ≥ 2u²/π²` on `[−π, π]` (Jordan), the split of the cube at `|k|_∞ = 1`, `|φ|^{2n} ≤ e^{−2n(1−|φ|)}`, and the two-region bound `1 − |φ(k)| = min(1 − φ(k), 1 − φ(k − (π,π,π)))`.
- V3 (the certificate): with `N = 1000`, `Σ_{n>N} n^{−3/2} ≤ 2/√N`, `π ≥ 3` and `e^{−2/15} ≤ 197/225`: `3G(0) ≤ (S_N + T_1 + T_2)/2 < 76/100` as an exact rational comparison (`T_1² ≤ (36/11)³/(108N)`, `T_2 = (225/14)(197/225)^{N+1}`); and `3G(0) ≥ S_N/2 > 75/100`.
- V4 (the placement): block 19's G3–G5 hold for `β > 76/100`; with block 21, the kernel's window is `[√3/6, 76/100]`; the route's constant cannot be pushed below `75/100`.
- N-gate: the negative "the route's threshold is not below `75/100`" is exact; the escapes: another route to order (not attempted); the band.

**Lens pass (self-run panel).**
- *"The Watson integral has a closed form."* Yes, through elliptic integrals; not used — the exact partial sums and an elementary tail bound suffice and are re-proved at scope.
- *"Why not the true `β_c`?"* The threshold is the sufficient condition of block 19's route; the true transition is not claimed (the route's constant is pinned, not the transition).
- *"Is the runner's exact sum feasible?"* `S_{1000}` as one rational with a `1553`-digit denominator takes about ten seconds; the certificate compares rationals.
- *"The exponential term."* Bounded by an exact geometric series with `e^{−2/15} ≤ 197/225`, below `10^{−57}` at `N = 1000`.

**Forbidden phrases (beyond the lane's standing list):** "phase transition", "critical", "converge", "certified", "emergent", "the physical coupling", "the transition point".

**Prior-art search at `origin/main`.** Block 19's `G(0) ≤ √3π/8`; block 13's return probabilities `p_{2n}^{SRW}` (a different use: the heat kernel); nothing on the return sum's value. Open PRs: #8153, #8154, #8155 (this lane).
