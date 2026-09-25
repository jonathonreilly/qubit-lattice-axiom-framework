# The sideways drift of the clocked walk's packets, as a grid — run 2

Worker `w-jonathonsmac4f50-j6c55`, model `claude-opus-5-5`. Block 54 was written by the same model family (Claude). The log is `logs/probes/C:clocked-walk-sideways-drift-grid:a2/w-jonathonsmac4f50-j6c55__2dd85f70__20260925T022643Z.*`.

## As landed on main

The landed block 54 (#8570) narrows three things:
- Its sideways-drift fits are historical author calculations, not claims (N8).
- T3 is polynomial algebra, and its force reading is refuted.
- T4 is a conditional ray model.

Nothing here builds on the withdrawn force statement.
- The comparison model is the standard semiclassical ray of `E = w ε` with the anomalous velocity `−k̇ × Ω`, **ASSUMED** and tested here.
- The evolutions are the walk itself, `H_w = √w H √w` with `u = ±g (r·ĝ)`.

## Exact results (sympy)

**Curvature formula.** For `h(k) = sin k · σ` and `ε = |sin k|`:

  `d̂·(∂_{k_y} d̂ × ∂_{k_z} d̂) = sin k_x cos k_y cos k_z / ε³`, and cyclically.

This was checked by `simplify` and at three points to 40 digits. The branch curvature is `Ω_± = ∓ ½ (that vector)`, in the convention `ṙ = ∂E/∂k − k̇ × Ω`. The overall sign was fixed once, on orientation A.

- **Along an axis, `k = (q, 0, 0)`:** `|Ω_x| = 1/(2 sin² q)`. The force has size `g ε`, so the anomalous speed is `g/(2 sin q)` and the drift is `gT/(2 sin q)`. This equals `gT/(2q)` only as `q → 0`: at q = 1.2 the two differ by a factor 1.26.
- **Branch independence:** with `k̇ = −b g w ε ĝ` on branch b, the anomalous velocity is `−(g w ε/2) ĝ × (ε³-normalized vector)`, the same on both branches.
- **The eight zero-energy points `k = πn + δ`:**
  - `h = D·sin δ` with `D = diag((−1)^{n_j})`, and the curvature picks up the factor `det D = (−1)^{n_x+n_y+n_z}`.
  - The signs over the eight points are `+ − − + − + + −`, summing to 0.
  - The staggering `(−1)^{n·r}` maps the walk at `πn + δ` to the walk at `δ` with `σ_j → (−1)^{n_j} σ_j`. That map is a qubit rotation when `det D = +1`, and minus a qubit rotation when `det D = −1`.

## Reduction (exact)

For a gradient along a primitive integer vector `m`, the states `e^{ik·r} f(m·r)` are closed under `H_w`. So a packet that is a plane wave across `ĝ` and Gaussian along it (width `max(6, 5/q)`) evolves exactly on the chain `n = m·r`.
- The displacement along `d = ĝ × v̂₀` is `∫⟨∂H_w/∂k_d⟩ dt`, integrated with Simpson's rule over 160 steps.
- Parameters: `g = 0.004`, `T = 30`.
- The odd part is half the difference between `+g` and `−g`.
- The most weight within two sites of the chain ends was `1.5e-6`.

The same δ = `q·(motion)` is used at every zero-energy point, so the packet moves the same way at all eight points: along +motion on the + branch, −motion on the − branch.

## Grid

The table gives the + branch at point (0,0,0), as drift along `ĝ × v̂` over `gT/2k`, and the drift itself.

| orientation | q = 0.15 | 0.25 | 0.35 | 0.5 | 0.8 | 1.2 |
|---|---|---|---|---|---|---|
| A: motion x, gradient y | −0.995 (−0.3981) | −0.996 (−0.2391) | −1.004 (−0.1722) | −1.024 (−0.1229) | −1.090 (−0.0818) | −1.262 (−0.0631) |
| B: motion (x+z)/√2, gradient y | −0.988 | −0.976 | −0.964 | −0.941 | −0.872 | −0.734 |
| C: motion (x+y+z)/√3, gradient y | −0.820 | −0.806 | −0.792 | −0.763 | −0.682 | −0.528 |
| D: motion (x−y)/√2, gradient (1,1,1)/√3 | −0.940 | −0.761 | −0.383 | +0.714 | +5.48 | +18.2 |

- **Against the lattice curvature:**
  - Over the whole grid (4 orientations × points (000), (100), (110), (111) × 2 branches × 6 wave vectors), the measured drift equals the central ray with the curvature term, averaged over the packet's momentum spread, to within **0.96%**.
  - The ratio is 1.008 at q = 0.15 and falls to 1.0003 at q = 1.2.
  - Along an axis (A), measured ÷ `gT/(2 sin q)` = −0.992, −0.986, −0.984, −0.982, −0.978, −0.981. The ray, which also follows the change of k during the run, accounts for the rest.
- **Continuum value.** `gT/(2k)` times the sine of the angle between gradient and motion: C's small-q value is 0.820 against `√(2/3) = 0.816`.
- **Oblique gradient (D).**
  - The ordinary rays of `E = w ε` already move sideways: +0.0185, +0.0511, +0.0993, +0.198, +0.477, +0.945 at q = 0.15 … 1.2.
  - The walk's drift is that plus the curvature term. Walk minus ray at q = 0.5 is −0.1127 at points with `det D = +1` and +0.1140 at points with `det D = −1`.
  - Measured ÷ (ray + curvature) is 1.007, 1.000, 0.994, 1.007, 1.002, 1.001.

## Signs

- **By zero-energy point:** the drift vector flips with `det D`. At every q and orientation, (000) and (110) have one sign and (100) and (111) the other, with identical magnitude on axis gradients.
- **By branch:** at fixed δ the drift vector is the **same** on both branches, while the velocity reverses.
  - Relative to `ĝ × v̂`, the drift is `−det D` on the + branch and `+det D` on the − branch.
  - Example, block 54's case (motion x, gradient z, + branch, point 000): the drift is along `−(ĝ × v̂)`, matching block 54's measured sign (−0.119).

## Eight points in a symmetric superposition

This is at q = 0.5, + branch, with the same δ at all eight points.

| gradient | sum of the eight drifts | sum of walk minus ray | single anomalous drift |
|---|---|---|---|
| along an axis (A) | −1.2e−15 | −1.2e−15 | 0.1229 |
| along (1,1,1) (D) | **+1.59** | +5.2e−3 | 0.1127 |

**Reading.**
- The anomalous (curvature) parts cancel between the four points of each chirality.
- On an axis gradient the whole drift cancels, to rounding.
- On the oblique gradient, the ordinary lattice ray's sideways motion is the same at all eight points (ε(πn + δ) = ε(δ)), so it adds: 8 × 0.198.
- The residual `5e−3` of the anomalous sum is 0.6% of one drift, the size of the ray model's mismatch.

## 3D check (block 54's propagation)

Setup: box 68, width 5, q = 0.5, motion x, gradient z.
- **3D packet:** sideways drift, odd in g, of **−0.1200**. The weight within two sites of the walls is `3.1e−4`, below `1e−3`.
- **3D cloud of rays:** −0.1174 with the curvature term (ratio 1.022), and 0.0000 without it.
- **Reduced chain** (plane wave across): −0.1229.
- **Block 54's executed value:** −0.119.

## Verdict

There is no HIT.
- The executed sideways drift of block 54 is the anomalous velocity of the branch curvature of `h = sin k·σ`. This holds in a model that is **ASSUMED**, but it matches the walk to within 1% across the grid.
- The drift equals `gT/(2k)` only for small k and for motion perpendicular to the gradient.
- Its sign follows the chirality `det D` of the zero-energy point, and it does not depend on the branch.
- The eight points cancel in the curvature part. The total cancels only when the gradient is along an axis.
