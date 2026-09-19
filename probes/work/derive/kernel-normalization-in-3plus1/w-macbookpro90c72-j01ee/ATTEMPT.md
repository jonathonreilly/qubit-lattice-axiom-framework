# kernel-normalization-in-3plus1, attempt 2 (worker w-macbookpro90c72-j01ee, model grok-4.6)

Third route on this problem (a3: cubic mean map `K=gφ`; a1: vMF noise `R=1+(3-G)/(nβ)`). This attempt is the **sum rule** from `|s|=1`, which is the only place `|m|²` and `G_3` enter together as the task expected. Plan locked from `formation_levelplane.py` (Parseval convention `S_0=|FFT|²/N`) before reading a1/a3 in full.

## (1) The statement attempted

**Statement (PARTIAL).** For any unit-vector field on a torus of `V` sites, with two lab-transverse components of equal site variance `C(0)` and mean zero,

```
2 C(0) + ⟨s_z²⟩ = 1,     ⟨s_z²⟩ = |m|² + Var(s_z) ≥ |m|²,
```

hence `C(0) ≤ (1-|m|²)/2`. Parseval for the simulator’s `S_0` is `C(0)=V^{-1}∑_k S_0(k)`. Writing `S_0(k)=R(k)\,σ²/(1-|φ(k)|²)` off zero,

```
R_avg := ∑_{k≠0} R(k) w(k) / ∑_{k≠0} w(k) = C(0)/(σ² G_V) ≤ (1-|m|²)/(2 σ² G_V),
```

with weights `w(k)=1/(1-|φ|²)` and `G_V=V^{-1}∑_{k≠0} w(k)`. This is the **G-weighted average** of `R`, not `lim_{k→0} R(k)`. On `L=4` the weights range from `1` to `8/3` and the heaviest mode is a small fraction of `G_4=1913/1344`, so the sum rule does not determine the infrared ratio and does not yield an `a` for `R(k→0)=1-a/β`.

## (2) Steps

**Step 1 — `|s|=1` (PROVED; CHECKED U1).** Pointwise `s_x²+s_y²+s_z²=1`. Average. `Var(s_z)≥0`. Exhaustive on two-site six-axis configurations.

**Step 2 — Parseval (PROVED; CHECKED U2).** Unnormalized FFT: `∑_k |FFT|² = V ∑_x f²`, `S_0=|FFT|²/V`, `V^{-1}∑_k S_0=C(0)`. Checked on `(Z/2)^3` for all `f∈{-1,0,1}^8`.

**Step 3 — `R_avg` bound (PROVED; CHECKED U3).** Definition of `G_V` and `R_avg`. Linear `S` has `R_avg=1`. Spin-wave `1-|m|²∼2σ² G` saturates the bound at `1`.

**Step 4 — weights are not a delta (CHECKED U4).** `L=4` cosine form of `1-|φ|²`.

## (3) Failure of this route for the IR coefficient `a`

The sum rule controls `R_avg`, not `R(k→0)`. Combining it with a3 (`R(k)` almost constant after Goldstone projection of the mean map) would still not produce a positive `a` from `|m|²` and `G_3` without a separate identification of `Var(s_z)` and of `R(k)`’s shape. First missing step: a theorem that `R(k)→R_avg` as `k→0`, which the executed shells (IR `0.97`, UV `1.01` at `β=6`, `L=32`) already contradict at the 3% level.

## (4) What would finish it

A decomposition `R(k)=R_avg + R̃(k)` with `∑ R̃ w =0` and a Hardy-type bound on `R̃(k)` at small `k`, or a proof that `Var(s_z)` is `O(1/β²)` with an explicit constant, turning the bound into `R_avg=1-σ² G+O(σ⁴)` (still not the IR value).
