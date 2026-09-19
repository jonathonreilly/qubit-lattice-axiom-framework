# ordering-threshold-down: derivation attempt 4 of 5

Worker `w-jonathonsmac4f50-jc31e` (claude-opus-5), unit `J-derive-ordering-threshold-down-a4`.

Objects come from block 30 (PR #8174, head `cc7662e1`):
- the two-level automaton `η'`;
- the deviations `d_1, d_2, d_3`, with closed forms on `(p, 1, 2)`: `d_1 = 33/(p³ + 33)`, `d_2 = (p + 32)/(p² + p + 32)`, `d_3 = (2p + 11)/(p² + 2p + 11)`;
- `ε₁ = d_1` and `ε₂ = max(d_2, d_3)`.

Round 1's refinement-history construction and its grammar come from `probes/work/derive/beyond-the-union-bound/w-jonathonsmac4f50-jae8a/ATTEMPT.md`: moves `d ∈ {1, 2, 3}³` per refinement, bad pairs `b(d) = #{k : d_k = k}`, the Steiner-tree shapes, and the physical weight `ε₁^{F+1} ε₂^{B}` of a history. That weight is realizable only under the potential constraint `R ≤ F + B`.

**Provenance and independence.** The round-1 history count is my model family's own (`jae8a`). The three round-1 referee reports on the grok attempts (`j10d4`, `j3743`, `j5777`) are also claude-opus-5. This attempt builds on the history grammar that survived refereeing, so it is not independent of it. No other round-2 attempt was on `origin/ai/probes` when I wrote this.

## 1. The statement attempted

The task asks for a proved threshold below 58 on `(p, 1, 2)`. **None is proved here.** What is proved:

**(N) A precise no-go for route (ii) and for every re-summation of the history count.**
- Let `𝔉` be any family of history encodings that contains the chains `𝒞` of §2 (S3–S6), and bound `P(η'_x = 1)` by `Σ_{h∈𝔉} ε₁^{F(h)+1} ε₂^{B(h)}`.
- Then the bound is `+∞` whenever `27 ε₂ > 1`, that is, for every `p ≤ 57` on `(p, 1, 2)`.
- `𝒞` lies in round 1's grammar `𝔊`. It also lies in every thinning of `𝔊` that acts only on forks, such as a diamond-free lift of the fork displacements. It lies in every thinning that acts only on coincident poles, such as typing by pole configuration.
- So route (ii) (refinement histories combined with the diamond-free lift) cannot pass `ε₂ = 1/27` either. Neither can any rearrangement of the same sum: σ-tilts, typed recursions, or other super-solutions.
- The ceiling `1/27` is not an artefact of round 1's σ-trick. It is the exponential growth rate of the grammar's fork-free, separated-pole chains, each weighted by its exact physical cylinder weight.

**(D) The domination facts on `(p, 1, 2)`.**
- `d_1 ≤ max(d_2, d_3)` holds for every `p ≥ 1`. This is block 30's T1(a), which is false for general weights, established on this line.
- `d_2 = d_3` exactly at `p = 21`. Hence `ε₂ = d_2` for `p ≤ 21` and `ε₂ = d_3` for `p ≥ 21`.

## 2. Steps

**S1 (PROVED; CHECKED `D1`, `D2`). The deviations.**
- The numerators over positive denominators are:
  - `d_2 − d_1`: `p²(p − 1)(p + 33)`;
  - `d_3 − d_1`: `p²(2p² + 11p − 33)`;
  - `d_2 − d_3`: `p²(21 − p)`.
- So `d_1 ≤ d_2` for `p ≥ 1`, and `d_1 ≤ max(d_2, d_3)` on the whole line from `p = 1`.
- `ε₂ < 1/27` exactly for `p ≥ 58`, since `d_3(57) = 125/3374 > 1/27 ≥ d_3(58) = 127/3491`.
- Values of `ε₂`:

| `p` | 11 | 13 | 14 | 21 | 30 | 40 | 57 | 58 | 84 |
|---|---|---|---|---|---|---|---|---|---|
| `ε₂` | 0.2622 | 0.2103 | 0.1901 | 0.1073 | 0.0731 | 0.0538 | 0.0370 | 0.0364 | 0.0247 |

**S2 (PROVED; CHECKED `G1`). Weights.**
- In the grammar, a refinement chooses `d ∈ {1, 2, 3}³`. The 27 patterns split as `8, 12, 6, 1` by `b = 0, 1, 2, 3`, and `Σ_d r^{b(d)} = (2 + r)³`.
- A fork-free chain of `R` refinements ending in a seed has `F = 0`, a single seed and `B = Σ b` bad pairs.
- Its physical weight is `ε₁ ε₂^B`. The bad sites of a history are distinct (round 1, 2d).
- It is admissible under the potential constraint iff `B ≥ R`.

**S3 (PROVED; CHECKED `G2`, `G3`). The blocks.**
- A block is `m` refinements in which charge `k` makes exactly `a` moves 1, `a` moves 2 and `m − 2a` moves 3, with the same `a` for the three charges and the moves in any order.
- Its bad pairs number `a + a + (m − 2a) = m`, so `B = R` on blocks.
- The predecessor step `X ↦ X − e_d` moves the in-plane coordinates `(X₁, X₂)` by `(−1, 0)`, `(0, −1)` or `(0, 0)`. So each block moves every pole by the same `(−a, −a)`, and the relative positions of the poles are restored exactly.
- Inside a block, `ℓ = X₁ − X₂` changes by at most `1` per pole per step. Poles whose pairwise `ℓ`-gaps are `≥ 2m + 1` at the start of a block therefore stay pairwise distinct through it.
- The number of blocks is `M_m = Σ_a (m!/(a!² (m − 2a)!))³ ≥ multinomial(m; m/3, m/3, m/3)³ ≥ 27^m/(m + 1)⁶` for `m ∈ 3ℤ`.
  - The formula matches brute force at `m = 1, 2, 3`.
  - `(1/m) log M_m = 1.79, 2.28, 2.52, 2.67, 2.98, 3.12` at `m = 3, 6, 9, 12, 30, 60`, against `log 27 = 3.296`.

**S4 (PROVED; CHECKED `G5`). The prefix: separating the poles with moves legal at coincident poles.**
- **Refinement 1.** The root `({x}; x, x, x)` is refined as a processed pole with winning pair `{1, 2}`. Its excuses are `x − e₂` (charge 1), `x − e₁` (charge 2) and `x − e₁` (charge 3), the pattern `(2, 1, 1)` with `b = 0`.
- **Refinement 2.** Charge 1 alone at `x − e₂` moves 3. Charges 2 and 3, coincident at `x − e₁`, form a processed pole with winning pair `{2, 3}`, with excuses `3` and `2`. This is the pattern `(3, 3, 2)` with `b = 0`.
- The poles are now `x − e₂ − e₃`, `x − e₁ − e₃` and `x − e₁ − e₂`, pairwise distinct, with `ℓ = 1, −1, 0`.
- **Gap-making.** Then `n = 2m` refinements of `(2, 1, 3)`, each with `b = 1`, give `ℓ = 1 + n, −1 − n, 0`, so gaps `n + 1 ≥ 2m + 1`.
- Only these two refinements use coincident poles, and both patterns are processed-type excuse patterns. They are therefore legal in a grammar typed by pole configuration.

**S5 (PROVED; CHECKED `G5`). The suffix: merging to a seed.**
- In the prefix frame the poles sit at `(0, −1 − n)`, `(−1 − n, 0)` and `(−1, −1)`. They are moved in `2n` refinements to `(−n, −1 − n)`, `(−1 − n, −n)` and `(−1 − n, −1 − n)`, keeping them pairwise distinct. `check.py` finds such a schedule for `m = 3`, where it is the `12`-step merge.
  - Pole 1 makes `n` moves 1 (bad) and `n` moves 3.
  - Pole 2 makes `n` moves 2 (bad) and `n` moves 3.
  - Pole 3 makes `n` moves 1 and `n` moves 2 (neither bad for charge 3).
  - So the suffix has `B = R = 2n`.
- These targets are `u + e₁`, `u + e₂` and `u + e₃` for one site `u`. The last refinement `(1, 2, 3)`, with `b = 3`, amplifies each pole along its own charge and sends all three terminals to `u`. That makes the next cluster the singleton `{u}` with coincident poles, which is a seed.
- **Budget.** The prefix has `R = 2 + n` and `B = n`; the blocks have `B = R`; the suffix has `B = R`; the last refinement has `B − R = 2`. In total `B = R`, so the potential constraint `R ≤ F + B` holds with `F = 0`.
- `G5` builds such a chain with five random blocks and verifies every clause: `R = B = 36`.

**S6 (PROVED; CHECKED `G4`). Divergence.**
- For `N` blocks, the chains `𝒞` number at least `M_m^N`, each of weight `ε₁ ε₂^{R_pre + R_suf + 1} · ε₂^{Nm}`.
- So `Σ_{h∈𝒞} ε₁^{F+1} ε₂^{B} ≥ C_m (27 ε₂ (m + 1)^{−6/m})^{Nm}`. This tends to `∞` as `N → ∞` once `27 ε₂ > (m + 1)^{6/m}`.
- For every `ε₂ > 1/27` such an `m` exists, since `(m + 1)^{6/m} → 1`. At `p = 57`, where `27 ε₂ = 3375/3374`, `m = 251802` works (exact integers: `3375^m > 3374^m (m + 1)⁶`).
- Chains are distinct as encodings because their move sequences differ. Being fork-free, they are untouched by any operation on forks.

## 3. The first failing step

- **Route (ii)** fails at its combination step. The diamond-free lift thins fork (and arrow-lift) duplications. The ceiling-achieving histories contain no forks, and their separated poles admit no two encodings of one lattice object. So the combined count keeps `𝒞`, and its sum diverges for every `p ≤ 57` (S6).
- **Every re-summation of the history grammar** (tilts, typed recursions, super-solutions) bounds a sum over a family containing `𝒞`, and fails the same way.

## 4. What would finish it

A threshold below 58 needs a count that excludes most of `𝒞` using facts about configurations that the grammar ignores:

- **Processed poles.** A processed pole needs a second 1-predecessor, which is never charged. In `𝒞` roughly `8/27` of the pole moves are processed and free.
- **Connectivity.** A cluster holding three separated poles is connected through lower-level 1-sites, which the history does not charge.
- **Realizability of `𝒞`.** It is not decided here whether a configuration realizing each chain of `𝒞` exists.
  - If `e^{−o(R)}` of them are realized, the union bound over *realized* histories diverges too. The history route would then be capped at `1/27` for any bookkeeping.
  - If not, a realizability-aware count is the way through.

The other two routes need tools beyond the grammar:
- **Route (i).** A pair-branching domination with collision control. BK for disjointly occurring pieces plus a tree-graph bound for shared ancestors, since positive correlations defeat product closures.
- **Route (iii).** A block renormalization.

Separately, the located strength `p ∈ (10.5, 11)` has `ε₂ = d_2 = 0.262`. That value is above the pair-kernel mean-one point `(−2 + √7)/3 = 0.215` of round 1's a2 attempt. Any `η'`-route near `11` would also need a value-aware domination.
