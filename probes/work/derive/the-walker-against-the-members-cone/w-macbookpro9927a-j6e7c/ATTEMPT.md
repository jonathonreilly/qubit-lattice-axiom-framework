# The walker against the member's cone: block 149 checked, T3 scoped, and a pair that can radiate

Worker `w-macbookpro9927a-j6e7c` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in under a second with a peak of about 60 MB, and all of them are exact: fractions, sympy, and exact algebraic sign checks.

The families are:
- **B**: T1.
- **M**: T2.
- **D**: T4.
- **S**: T5.
- **X**: T3's scope.
- **W**: two walkers.

## Sources, provenance and overlap

**Block 149.** PR #9242 is open, so the note is not on main. I read it on its branch at head `5aacd93e4b`: `docs/ADMISSIBILITY_RULE_A_FREE_WALKER_NEVER_EMITS_OR_ABSORBS_ONE_OF_THE_MEMBERS_TRAVELLING_DISTURBANCES_…_2026-09-25.md`. Its statements T1–T5 are the hypotheses under test. It quotes, as landed:
- block 54's walk `H = Σσ_aS_a`, with energies `±|s(k)|` and `s_j = sin k_j`;
- block 139's staggered mass, with energies `±√(μ² + |s|²)`;
- blocks 62 and 101 (the member), with differences `p_j = 2 sin(q_j/2)`;
- at `α = K/4` (blocks 134–135) and unit rate, travelling disturbances of frequency `ω = |p(q)|`.

Its premise defines emission and absorption as `k → k ∓ q` with `E(k) = E(k ∓ q) ± ω(q)`, and the coupling keeps total lattice momentum.

**Provenance.** The claim printed no prior attempts on this problem. My related unit is **#9256** (`deferred-20260925-same-band-radiation-boundary`, `w-macbookpro9927a-j7390`). It recovered block 149's T5 channel: a nonzero pair-creation amplitude at an exact interband resonance. It did not re-check T1–T4, which is what is done here. Family X reuses T5's resonance condition only as a kinematic statement.

## (1) The statement attempted

- **(i) T1.** For every `k` and every `q ≢ 0`, `||s(k)| − |s(k−q)|| < |p(q)|`. The equality case is handled completely, including `s(k) = 0` or `s(k−q) = 0`.
- **(ii) T2, T4 and T5 hold as stated.**
- **(iii) T3's scope.**
  - T3 holds for transitions within one band. Above the filled sea these are all the single-excitation transitions:
    - for a particle, the lower band is full;
    - for a hole, the moves stay in the lower band.
  - In the first-quantized two-band walk, one walker in the upper band at `k` can emit a disturbance `q` by dropping to the lower band at `k − q` exactly when `|s(k)| + |s(k−q)| = |p(q)|`.
  - This is solvable for every `q` with `Σ_a cos q_a > 0`, for example `q = (π/3, 0, 0)`.
  - So T3's headline, "no single free walker emits or absorbs", needs the words "within its band" or "above the filled sea".
- **(iv) Two walkers.** A pair of walkers in the upper band can emit one disturbance with energy and lattice momentum kept:
  - `(π/2,0,0) + (−π/2,0,0) → (a*,0,0) + (π/3,0,0) + q`, with `q = (−a* − π/3, 0, 0)`;
  - `a* ∈ (0, π/6)` is the unique root of `sin a + √3/2 + 2 sin((a+π/3)/2) = 2`.

  So the lowest-order emission rate of a scattering pair does not vanish by kinematics.

## (2) Steps

**Step 1 (PROVED; CHECKED B1, B2): T1.**
- `s_j(k) − s_j(k−q) = 2cos(k_j − q_j/2) sin(q_j/2)` (B1). So `|s(k) − s(k−q)| ≤ |p(q)|`, and the reverse triangle inequality gives `||s(k)| − |s(k−q)|| ≤ |p(q)|`.
- *Equality in the first step* holds iff `cos(k_j − q_j/2) = ±1` for every `j` with `sin(q_j/2) ≠ 0`, that is for every `j` with `q_j ≢ 0`. For those `j`, `s_j(k−q) = −s_j(k)` (B1). For the other `j`, `q_j ≡ 0` and `s_j(k−q) = s_j(k)`. So `|s(k−q)| = |s(k)|`, and the left side is `0 < |p(q)|`, because `p(q) ≠ 0` for `q ≢ 0`.
- *Otherwise* the first step is strict.
- Either way the inequality is strict.
- *The note's clause.* The note says that equality in the triangle step needs `s(k−q)` to be a nonnegative multiple of `s(k)`. That misses `s(k) = 0 ≠ s(k−q)`, where the triangle step is an equality. The route above does not use that clause.
- *The sweep.* B2 confirms the strict inequality exactly at 4000 points, with `k_j` and `q_j/2` at rational points of the circle. It squares twice, with signs tracked.

**Step 2 (PROVED; CHECKED M1): T2.**
- `(μ² + a²)(μ² + b²) − (μ² + ab)² = μ²(a − b)² ≥ 0`, so `√(μ²+a²)√(μ²+b²) ≥ μ² + ab`.
- Hence `(√(μ²+a²) − √(μ²+b²))² ≤ (a − b)²`.
- With `a = |s(k)|` and `b = |s(k−q)|`, T1 gives the massive bound.
- Processes that shift the momentum by `Q = (π, π, π)` have the same energies, since `|s(k − Q)| = |s(k)|`.

**Step 3 (PROVED; CHECKED D1): T4.**
- Along an axis, `sin q − 2 sin(q/2) = −q³/8 + q⁵/128 + …`.
- `s_j(q) = p_j(q) cos(q_j/2)`. So `|s(q)| ≤ |p(q)|`, with equality only at `q ≡ 0`.

**Step 4 (PROVED; CHECKED S1): T5.**
- `|p(q)| = 2|s(q/2)|`.
- At `k_a = π/2 − q_a/2`, both `|s(k)|` and `|s(k+q)|` equal `|cos(q/2)|`, where `cos(q/2)` is the vector `(cos(q_a/2))_a`.
- `(2|cos(q/2)|)² − |p(q)|² = 4Σ_a cos q_a`.
- At `k = 0` the pair energy is `|s(q)| < |p(q)|`.
- The torus is connected, so the resonance exists whenever `Σ cos q_a > 0`.

**Step 5 (PROVED; CHECKED X1): T3's scope.**
- *The process.* The first-quantized walk has both bands. An upper-band walker at `k` goes to the lower band at `k − q` and emits `q`. Energy is kept iff `|s(k)| = −|s(k−q)| + |p(q)|`, that is `g(k) := |s(k)| + |s(k−q)| − |p(q)| = 0`.
- *The witness.* For `q = (π/3,0,0)`, `|p(q)| = 1`:
  - `g(q) = √3/2 − 1 < 0`;
  - `g(2π/3, π/2, π/2) = √11 − 1 > 0`.
- *The general case.* `g` is continuous, so it vanishes on the segment between these points. For general `q` with `Σ cos q_a > 0`, Step 4's two anchors, shifted by `q`, do the same.
- *Absorption.* The time-reversed process is absorption by a lower-band walker, which is T5's pair creation.
- *Above the filled sea.* A particle's lower-band target is occupied. A hole moves when a lower-band state fills it, and that is intraband, so T1 applies. So T3 holds for every single-excitation transition above the filled sea.
- *The massive walk.* It needs `|p(q)| ≥ 2μ`, since every pair costs at least `2μ` (block 149 T5).

**Step 6 (PROVED; CHECKED W1, W2): two walkers.**
- Take upper-band walkers at `k₁ = (π/2,0,0)` and `k₂ = (−π/2,0,0)`, each with energy 1 and total momentum 0.
- Take final walkers at `(a,0,0)` and `(π/3,0,0)`, and one disturbance at `q = (−a − π/3, 0, 0)`. Momentum is kept.
- *Energy.* Let `f(a) = sin a + √3/2 + 2 sin((a+π/3)/2) − 2`.
  - `f(0) = √3/2 − 1 < 0`.
  - `f(π/6) = √3/2 + √2 − 3/2 > 0`, since `(√3/2 + √2)² = 11/4 + √6 > 9/4`.
  - `f′(a) = cos a + cos((a+π/3)/2) > 0` on `[0, π/6]`, because both arguments lie in `[0, π/4]`.
  - So there is exactly one root `a* ∈ (0, π/6)`.
- The final momenta are distinct (`a* < π/6 < π/3`). `q_x ∈ (−π/2, −π/3)`, so `|p(q)| = 2 sin((a*+π/3)/2)`.
- So one disturbance can carry off energy and momentum from a pair. What forbids it for one walker (T1) does not forbid it for two.

## ASSUMED

None. Every step is argued in full. The trigonometric identities and the finite sign checks are exact.

## (3) Where the route stops

**The two-walker rate is not computed.** The first unresolved step is the amplitude. At lowest order it is the pair's scattering amplitude (block 143, under one record per site, block 78), combined with block 136's stress vertex taken off shell. Then comes the phase-space integral over the pair-plus-one-disturbance shell, which Step 6 shows is nonempty.

It is not decided whether the amplitude vanishes in some regime. Candidates are:
- one dimension, where one record per site gives pure transmission or reflection;
- the long-wavelength limit, where the two cones meet (T4).

## (4) What would finish it

- The two-body `T`-matrix of block 143 at the resonance, with the off-shell emission vertex. #9256's vertex `K_q` is a starting point.
- The phase-space measure of the pair-emission shell. For example, its dimension and whether its Jacobian is regular at generic `(k₁, k₂)`.
- A regime in which the combined amplitude vanishes, if one exists. Otherwise the leading power of the rate in the scattering strength.
