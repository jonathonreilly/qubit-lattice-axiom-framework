# kernel-normalization-puzzle: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-j5e26` (claude-opus-5), unit `J-derive-kernel-normalization-puzzle-a3`.

**Sources.**
- The model and estimator are `probes/lib/formation_levelplane.py`, with blocks 26, 34 and 35's objects.
- The GIVEN comes from the round-1 `kernel-normalization-in-3plus1` reports: grok authors, claude-opus-5 referees, so partly my model family.
- The executed tables are `logs/probes/X:formation-3plus1-*`, `X:lightcone-*` and `X:formation-linear-calibration` on `ai/probes`.

No other round-2 attempt on this problem was on `origin/ai/probes` when I started.

## 1. The statement attempted

**Answer to the puzzle.** The measured kernel does not sit below the linear one. The quantity `R(k) = S(k)(1 − |φ(k)|²)/σ²` has a plateau above 1 in every executed run, and the plateau decreases with `β` as predicted:
- **backward 3+1 (`n = 4`):** plateaus `1.033–1.034` at `β = 2`, `1.010` at `β = 6`, `1.0024` at `β = 24`;
- **light-cone (`n = 7`):** `1.087–1.105` at `β = 1`, `1.065` at `β = 1.5`, `1.047` at `β = 2`.

The sub-1 values quoted in the task (`0.95–0.99`) are the lowest `|k|` shell only. There the finite-level transient from the aligned start costs at most 2%, and the sampling error of that shell is `0.02–0.12`. Every lowest shell lies within `|z| ≤ 1.7` of the predicted value.

**The formula (order `1/β`, one-loop).** For the lab-frame transverse field `θ_x = s_x^⊥` of the sphere formation law with `n` predecessors, `σ² = A(nβ)/(nβ)`:

`S(k) = σ² [1 + σ² (2 − W)] / (1 − |m(k)|²) + O(σ⁶)`, with `W = L^{−d} Σ_{k≠0} 1/(1 − |φ(k)|²)`.

- `W` is the site variance per component over `σ²`, the return sum.
- The mean-map symbol is `m(k) = φ(k)` for the backward simplex stencils. There `R = 1 + σ² (2 − W)` is independent of `k`.
- For the light-cone, `m(k) = φ(k) − (Δ/343) E(k)` with `Δ = C(2e) + 4 C(e₁ − e₂) − 5 C(e)`, the equal-time covariances per component. So at small `k`, `R(0+) = [1 + σ²(2 − W)]/(1 + σ² Δ_c/49)`, where `Δ = σ² Δ_c`.

**How the task's candidates enter:**
- **Fluctuating concentration `β|S_x|`:** `+σ²`, from `E[δ]/n` with `δ = n − |S|`.
- **Lab-frame projection** (the tilt of the local mean away from `e₃`, the "`sin θ` versus `θ`" effect): `−σ² (W − 1)`.
- **Gain `g`:** no order-`1/β` term. The Hartree gain is `A(nβ)(1 + σ²) = 1 + O(1/β²)`, which is the GIVEN's cancellation.
- **Wandering zero mode:** a factor `1 − σ² t̄/L^d` at leading order, where `σ² t̄/L^d` is half the expected squared tilt of the mean direction, averaged over the measurement window. It is at most `0.0025` in every run except the light-cone run at `β = 1, L = 24`, where it is `0.0199`.
  - With it, the three light-cone `β = 1` residuals are equal: `+1.84σ⁴` at `L = 24, 48, 96`. Without it they are `+0.40σ⁴, +1.66σ⁴, +1.83σ⁴`.
  - It is an expectation. A single run's tilt is one sample of a random walk, and at the next order the factor carries `1/|M|²`.
- **Exchange (Fock) term:** absent for simplex stencils, present for the light-cone.

## 2. Steps

**S1 (PROVED). Exact one-step facts.** For `s ~ vMF(κ Ŝ)`:
- the mean is `A(κ) Ŝ`;
- the covariance is `(A/κ)(I − ŜŜᵀ) + A'(κ) ŜŜᵀ`;
- `|S|² = n² − Σ_{y<y'} |s_y − s_{y'}|²`, so `δ = n − |S| = (1/(2n)) Σ_{y<y'} |θ_y − θ_{y'}|² + O(θ⁴)`;
- the lab-frame mean map is `F = A(β|S|) S^⊥/|S| = A(nβ)(1 + δ/n)(Pθ) + O(θ³/β)`.

**S2 (PROVED; CHECKED `E1`). The uniform-stencil identity.** `Σ_{y<y'} (1 − cos k·(y − y')) = (n²/2)(1 − |φ(k)|²)`, symbolic for the three stencils. With the linear stationary covariance this gives `E[δ] = nσ²` exactly: the return sum drops out.

**S3 (PROVED; CHECKED `E2`). The gain.** The Hartree gain is `A(nβ)(1 + E[δ]/n)`. With `x = 1/(nβ)` it is `(1 − x)(1 + x(1 − x)) = 1 − 2x² + x³`, or `1 − x²` with the leading `σ² = x` (the GIVEN). In both, the order-`1/β` term cancels.

**S4 (PROVED; CHECKED `E3`). The exchange term.**
- The Wick linearization of the cubic term `(δ/n)(Pθ)` has two parts:
  - **Hartree:** `E[δ]/n · Pθ`;
  - **exchange:** `(1/n²) Σ_y (Γ(y) − Γ̄) θ_y`, with `Γ(y) = Σ_{z∈pred} C(y − z)`.
- **Backward stencils.** The predecessors are the event-lattice points `X − ε_a`. Their pairwise differences `ε_a − ε_b` form one orbit of the stencil's symmetry, so `Γ` is constant and the exchange term vanishes.
- **Light-cone.** `Γ(0) − Γ̄ = −(6/7)Δ` and `Γ(±e_j) − Γ̄ = Δ/7`, so the exchange term is `(Δ/343) ×` the nearest-neighbour Laplacian.

**S5 (ASSUMED: the one-loop Gaussian closure).**
- The stationary two-point recursion `C = M C Mᵀ + N_eff` is truncated at one loop. `M` is the linear map plus the Hartree and exchange linearizations; `N_eff` is the noise covariance averaged over the leading Gaussian law.
- Neglected: two-loop terms, non-Gaussian corrections of the stationary law, and `O(β⁻²)` pieces of `A` and `A'`.
- This is the standard perturbative closure. It is not re-proved here, and the residuals in N1 are of the neglected order, `σ⁴`.

**S6 (PROVED under S5; CHECKED `E4`). The noise.**
- Per component: `E[Cov(θ_x | preds)] = σ² [1 + E[δ]/n − E|Pθ|²/2] + O(σ²/β)`.
- `E|Pθ|²/2 = σ² L^{−d} Σ_{k≠0} |φ|²/(1 − |φ|²) = σ² (W − 1)`.
- Hence the noise is `σ² [1 + σ² (2 − W)]`, and the ratio formula of §1 follows.

**N1 (numerical, labelled). Comparison with the executed runs.** `W` and the light-cone covariances are computed in floating point on the executed tori, and the plateaus (shells 4–6) are parsed from the logs.

| run | predicted | measured plateau | residual / σ⁴ (without, with the zero-mode factor) |
|---|---|---|---|
| backward, `β = 2`, `L = 64` | 1.0251 | 1.0342 | +0.76, +0.84 |
| backward, `β = 2`, `L = 48` | 1.0260 | 1.0334 | +0.62, +0.81 |
| backward, `β = 6`, `L = 32` | 1.0101 | 1.0103 | +0.15, +1.02 |
| backward, `β = 24`, `L = 64` | 1.0024 | 1.0024 | +0.60, +0.97 |
| light-cone, `β = 1`, `L = 24` | 1.0805 | 1.0865 | +0.40, +1.84 |
| light-cone, `β = 1`, `L = 48` | 1.0785 | 1.1033 | +1.66, +1.84 |
| light-cone, `β = 1`, `L = 96` | 1.0775 | 1.1050 | +1.83, +1.84 |
| light-cone, `β = 1.5`, `L = 48` | 1.0552 | 1.0649 | +1.30, +1.55 |
| light-cone, `β = 2`, `L = 48` | 1.0425 | 1.0474 | +1.10, +1.42 |

- Every plateau lies above its prediction, by at most `0.028`.
- With the zero-mode factor the residual is `+0.81σ⁴` to `+1.02σ⁴` for the backward runs and `+1.42σ⁴` to `+1.84σ⁴` for the light-cone runs. That is the neglected order.
- The `β = 24` residual is `0.0001`, below the four printed decimals of the logged shells, so its `σ⁴` multiple is not resolved.
- The lowest shells lie within `|z| ≤ 1.7` of the predicted plateau times the transient factor. The factor is the mean over the shell and the measurement window of `(1 − u^t)`, which is `0.979–1.000`. The sampling s.e. assumes AR(1) autocorrelation `u^s` of `|θ̂_k|²`.

## 3. Where the route stops

- The one-loop closure (S5) is assumed, not proved.
- The positive residual (`+0.8σ⁴` to `+1.0σ⁴` backward, `+1.4σ⁴` to `+1.8σ⁴` light-cone, with the zero-mode factor) is order `σ⁴`, and so is the rise of `R` with `k` at `β = 2` in the backward runs. There the logged shells go from `1.0193` (`0.3 ≤ |k| < 0.6`) to `1.0426` (`3.2 ≤ |k| < 6`) at `L = 64`, and from `1.0175` to `1.0416` at `L = 48`, around the flat one-loop `1.025`. Neither is computed here.

## 4. What would finish it

- The two-loop terms, which would give the `σ⁴` coefficients and the `k`-dependence of `R` at small `β`.
- A proof of the closure: for example, a cluster expansion of the stationary law around the aligned state, whose large-`β` validity is the regime of the tables.
- Longer runs, or more levels in the lowest shell, would bring its s.e. below `0.02` and test the flat-in-`k` prediction there.
