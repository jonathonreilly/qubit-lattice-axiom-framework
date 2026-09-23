# Bending over fall at strong field — attempt 2

Worker `w-jonathonsmac4f50-j3a05`, model `claude-opus-5-5`. Task `J:derive:bending-over-fall-at-strong-field:a2`.

**Provenance.** Blocks 54, 59, 60 and 77 were written by the same model family (Claude Opus). They are open and unrefereed; I restate what I use. The referee should come from another family. There were no prior attempts at claim time.

**Scope.** This works within the supplied clauses: block 60's ledger linear in the rates with the curvature member, block 60 T4's exact one-body field, and block 77's staggered rest energy for a massive walker. Nothing is adopted. The parked decisions are untouched. No gravitational claim is made. "Bending" and "fall" are the framework's own quantities, in the ray limit. The comparator is geometric optics.

## 1. The exact statement attempted

**(a) The laws at finite field.**
- **Rays.** Block 60 says bonds are crossed at `√(w_x w_y)/(χ_x χ_y)`. At long wavelength a massless packet therefore has `H = c(x)|k|` with `c = w/l = N/χ³`. A ray moving along `y` has transverse acceleration `−c ∂_x c = c² ∂_x ln(l/w)`.
- **Slow bodies.** Block 77's rest energy is timed by the clock, and the kinetic part is seen through the frame, so `E = w √(m² + |k|²/l²)`. At rest the body accelerates at `−(w/l)² ∇ ln w`.

**(b) Bending over fall in the exact one-body field** (`χ = 1 + Qg`, `N = 1 − Pg`, `P = Q w₀`, `w₀ = 1/(1 + 2Qg₀)`).
- The ratio of the two accelerations at the same point is

  `(2 + 3Qg₀ − Qg)/(1 + Qg₀) = 1 + 2/(1 + w₀/w(x))`,

  for **any** shape of the Green's function `g`.
- It is linear in `g`. It equals block 60's `1 + (1 + 2Qg₀)/(1 + Qg₀)` far away and **exactly 2** at the body.
- Since `0 ≤ g ≤ g₀`, it lies in `[2, 3)` at every point and every strength.
- The ratio integrated along a straight line (first order in the deflection, exact fields) is a weighted mean of the local ratio, so it lies in `[2, 3)` as well.
- At first order this recovers block 60's far-field ratio.

**(c) The nonlinear rays.** Their own paths add something else. The index `n = l/w = (1 + a/r)³/(1 − w₀a/r)`, with `a = Q/(4π)`, has a capture radius `r* = a(1 + w₀ + √(w₀² + w₀ + 1))` (the minimum of `r n(r)`). Rays with impact parameter near `b_c = r* n(r*)` are deflected without bound, while the straight-line fall stays finite. This is a capture effect of the rays' paths, not a change of the ratio in (b). It is reported alongside (b); see the reading of the HIT condition below.

**The task's HIT condition (a ratio above 3 or below 1 at any strength), read precisely:**
- **Not met** by the ratio at a point, nor by the ratio integrated along a straight line. Block 60's bound `[2, 3)` holds at every point, not only far away.
- **Met** by the path-integrated nonlinear comparison: the exact ray deflection over the straight-line fall is 3.75 at `b = 3b_c` for `Qg₀ = 7.58`, and diverges at `b_c`.
- The HIT line states both, so that the referee can judge which ratio the task means.

## 2. Steps

### Step 1 — (a) (PROVED; CHECKED 1.1–1.3)
- **Ray.** From `H = c|k|`: `ẋ = c kₓ/|k|` and `k̇ₓ = −|k| ∂ₓc`. At `kₓ = 0` this gives `ẍ = c k̇ₓ/|k| = −c ∂ₓ c` (1.1).
- **Slow body.** From `E = w √(m² + k²/l²)`: at `k = 0`, `ẋ = w k/(m l²) + O(k³)` and `k̇ = −m ∇w`. So `ẍ = −(w/l)² ∇ ln w` (1.2).
- **The ratio** of the two along one direction is `∂ ln(l/w)/(−∂ ln w)` (1.3).
- **The long-wavelength limit.** The reach-three coupling of isotropic lengths (symbol `(1/2) sin 2k ≈ k`) and block 60's bond crossing agree there, so both give `c = w/l`.

### Step 2 — (b) (PROVED; CHECKED 1.4–1.6)
- **The formula.** With block 60 T4's field, `ln l = 2 ln(1 + Qg)` and `ln w = ln(1 − Pg) − ln(1 + Qg)`. Both are functions of `g` alone, so the common factor `∇g` cancels in the ratio (1.4). The ratio is `(2 + 3Qg₀ − Qg)/(1 + Qg₀) = 1 + 2/(1 + w₀/w)`.
- **Its end values** (1.5):
  - at `g = 0` it is block 60's far-field value;
  - `w(g₀) = w₀` (block 60 T4's `w₀ = 1/(1 + 2Qg₀)`), so at the body it is exactly 2.
- **The range** (1.6).
  - The lattice Green's function obeys `0 ≤ g ≤ g₀`: it is largest at the source, by the maximum principle for `−Δ`.
  - The ratio decreases in `g`, so it lies in `[2, R_far]`.
  - `3 − R_far = 1/(1 + Qg₀) > 0`.
- **Straight lines.** Both integrands, `∂_b ln(l/w)` and `−∂_b ln w`, are positive multiples of `−∂_b g` along a straight line. So their ratio is a weighted mean of the local ratio. Executed (E1): 2.08 to 2.87 for `Qg₀` from 0.5 to 7.6 and `b = 3, 6, 12`, always between 2 and the far value.

### Step 3 — (c) (PROVED for the continuum field; executed E2)
- **The capture radius.** With `g = 1/(4πr)`, `r n(r)` is stationary where `r² − 2(1 + w₀)ar + w₀a² = 0`. The larger root is `r* = a(1 + w₀ + √(w₀² + w₀ + 1))` (2.1). It lies outside the lattice scale once `a ≳ 1`, that is `Qg₀ ≳ 3`.
- **Executed at `Qg₀ = 7.58`** (`r* ≈ 5` sites). The exact Fermat deflection divided by the straight-line fall is 2.92 at `b = 60b_c`, 3.75 at `3b_c` and 5.50 at `1.5b_c`, and it grows without bound as `b → b_c` (E2).
- **How it differs from (b).** It compares a path-integrated nonlinear quantity with a straight-line one. At every point on the ray's path the local ratio is still in `[2, 3)`.

### Step 4 — packets on a slice (executed E3)
- **Setup.** A `72²` slice with the one-body field (smoothed at the source with the lattice `g₀`). Block 60's bond crossing rates and a mass term `m w σ₃` for the slow packet.
- **Measure.** The force on the momentum, `d⟨S_x⟩/dt = ⟨i[H, S_x]⟩`, converted to an acceleration with the local `w` and `l`. The centroid's second derivative is not used: at `t = 0` it is dominated by the packet spreading in a medium of varying speed, the same for both packets.
- **Result.** Both packets fall toward the body. The ratio is between 2 and 3 and approaches `1 + 2/(1 + w₀/w)` as the packet moves out: at `x₀ = 18`, 2.63 against 2.657 at `Qg₀ = 2.02`, and 2.80 against 2.868 at `Qg₀ = 7.58`. The residuals come from the packet width (5 sites) against the field's gradient scale.

## 3. Where the route stops

- Everything is in the ray limit. Nothing is claimed at finite wavelength.
- The massive walker's frame coupling (the kinetic part through `1/l`, the rest energy timed by `w`) follows blocks 60 and 77 as stated; it is not re-derived from a lattice placement of the mass.
- The capture statement uses the continuum `g = 1/(4πr)`.

## 4. What would finish it

1. The finite-wavelength corrections to both laws, from the lattice dispersion.
2. A strong-field comparison that uses exact trajectories for both the ray and a slow body, with a normalisation that stays meaningful near capture.
3. The same for block 56's simplest member (half bending), where `l = 1`.
