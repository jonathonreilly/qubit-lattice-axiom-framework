# spin-wave-diffusion, attempt 1 (worker w-macbookpro90c72-j2b02, model grok-4.6)

Own plan from `probes/lib/sphere_torus_msd.py` and the vMF one-step of the plane average, before using a2/a3. After locking: the referee of a2 (`referee_w-jonathonsmac4f50-j1ab5`) reports that a2’s `1/(1-σ² G_L)²` misses an `O(N^{-1})` term, visible at `L=1` where `G_1=0` predicts `1`. This attempt proves that `L=1` law exactly.

Setting (blocks 26, 34; PRs #8170, #8178): sphere formation on the `L×L` torus, three predecessors, `σ²=A(3β)/(3β)`. The estimator is `D_1=\mathrm{MSD}/(2\ell)` of the unit plane-average `m̂=M/|M|`, against `σ²/L²`.

## (1) The statement attempted

**Statement (PARTIAL).** On `L=1` the unique site is its three predecessors, `κ=3β` constantly, and `m̂=s`. One vMF step about the old direction has `E[s'·s]=A(3β)` and chordal `E|s'-s|²=2(1-A(3β))`. The script’s `D_1` is therefore `1-A(3β)`, and

```
D_1 L² / σ² = 3β (1-A(3β)) / A(3β) = [1 - 6β/(e^{6β}-1)] / A(3β).
```

This tends to `1` as `β→∞`, with power series `1 + 1/(3β) + 1/(9β²)+⋯`. It is **not** identically `1`, so a2’s `1/(1-σ² G_L)²` (which equals `1` at `L=1`) is false as a finite-`L` identity. The missing piece is the zero-mode’s own vMF self-noise, order `σ²/N` at general `L`.

Separately (geometry, not a2): the map `M↦M/|M|` has transverse Jacobian `1/|M|`, so Cartesian zero-mode variance `v` becomes direction variance `v/|M|²` (CHECKED).

## (2) Steps

**Step 1 — vMF chordal (PROVED; CHECKED S1).** `Z=4π sinhκ/κ`, `A=∂_κ log Z`. Unit vectors: `E|s-u|²=2-2A`. Exact `A=1-1/κ+2/(e^{2κ}-1)`.

**Step 2 — `L=1` ratio (PROVED; CHECKED S2).** `κ=3β`, `σ²=A/κ`, `D_1=1-A`, ratio `κ(1-A)/A`. Substitute `1-A=1/κ-2/(e^{2κ}-1)` to get `[1-6β/(e^{6β}-1)]/A(3β)`. Limit `1`; series `1+1/(3β)+1/(9β²)` (exponentially small terms dropped by `series` at infinity). Not identically `1`.

**Step 3 — `G_4` and `G_1` (CHECKED S3).** `1-|φ|²=(6-2\cos k_1-2\cos k_2-2\cos(k_1-k_2))/9`, `G_4=189/128`. `G_1=0`.

**Step 4 — sphere Jacobian (PROVED; CHECKED S4).** `n_x=ε/\sqrt{m²+ε²}`, `(n_x/ε)²→1/m²`.

## (3) Where the route stops

`L=1` is exact. For `L>1`, `κ_x=β|S_x|` fluctuates and `|M|<1`. Combining Step 4 with spin-wave `|M|=1-σ² G_L` (a2’s Step 2, ASSUMED for the nonlinear law) and the present self-noise would suggest

```
D_1 L²/σ² = [1-6β/(e^{6β}-1)] / A(3β)  ·  1/|M|²  + remainder,
```

but the product is not proved: the self-noise and the spin-wave factor are not independent, and the Itô correction on `S²` for `N>1` is not the `L=1` formula. The referee’s objection to a2 stands until that remainder is controlled.

## (4) What would finish it

A two-sided bound at general `L` of the form
`1/A(3β)·1/(1-σ² G_L)² · (1-C σ²) ≤ D_1 L²/σ² ≤ 1/A(3β)·1/(1-σ² G_L)² · (1+C σ²)`
for `σ² G_L≤1/2`, or an exact Lyapunov computation of the zero-mode on `L=2`.
