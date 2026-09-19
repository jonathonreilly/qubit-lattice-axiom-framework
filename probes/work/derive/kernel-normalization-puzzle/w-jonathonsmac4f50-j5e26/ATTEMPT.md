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
- **Wandering zero mode:** `−σ² t̄/L^d`. It is negligible at `L ≥ 48` and about `−0.02` at `L = 24` for the light-cone at `β = 1`, which is the direction of the measured finite-size drop.
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

| run | predicted | measured plateau |
|---|---|---|
| backward, `β = 2`, `L = 64` | 1.0251 | 1.0342 |
| backward, `β = 2`, `L = 48` | 1.0260 | 1.0334 |
| backward, `β = 6`, `L = 32` | 1.0101 | 1.0103 |
| backward, `β = 24`, `L = 64` | 1.0024 | 1.0024 |
| light-cone, `β = 1`, `L = 24` | 1.0805 | 1.0865 |
| light-cone, `β = 1`, `L = 48` | 1.0785 | 1.1033 |
| light-cone, `β = 1`, `L = 96` | 1.0775 | 1.1050 |
| light-cone, `β = 1.5`, `L = 48` | 1.0552 | 1.0649 |
| light-cone, `β = 2`, `L = 48` | 1.0425 | 1.0474 |

- Every residual is at most `0.028`, and each is between `0.02σ⁴` and `1.8σ⁴`.
- The lowest shells lie within `|z| ≤ 1.7` of the predicted plateau times the transient factor. The factor is the mean over the shell and the measurement window of `(1 − u^t)`, which is `0.979–1.000`. The sampling s.e. assumes AR(1) autocorrelation `u^s` of `|θ̂_k|²`.

## 3. Where the route stops

- The one-loop closure (S5) is assumed, not proved.
- The light-cone residual at `β = 1` (`0.025–0.028`) and the mild rise of `R` with `k` at `β = 2` in the backward runs are order `σ⁴`. They are not computed here.

## 4. What would finish it

- The two-loop terms, which would give the `σ⁴` coefficients and the `k`-dependence of `R` at small `β`.
- A proof of the closure: for example, a cluster expansion of the stationary law around the aligned state, whose large-`β` validity is the regime of the tables.
- Longer runs, or more levels in the lowest shell, would bring its s.e. below `0.02` and test the flat-in-`k` prediction there.
