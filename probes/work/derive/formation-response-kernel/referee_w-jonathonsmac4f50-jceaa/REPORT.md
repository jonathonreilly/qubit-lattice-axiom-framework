# Referee report: J:derive:formation-response-kernel:a3

**Author:** w-macbookpro90c72-j28fe (grok-4.6).
**Referee:** w-jonathonsmac4f50-jceaa (claude-opus-5).
**Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `afb554e0`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact rationals, sympy, mpmath).

## The problem and the claim

The task has four parts:
- (a) the exact linear response `R(k, w) = 1/(1 − φ e^{iw})` and its static limit;
- (b) its real-space form, with exact constants;
- (c) whether any channel decays like `1/r` in three dimensions, and if none does, what replaces it: the static response,
  the time-integrated covariance, the response in the co-moving frame, and the eight-corner symmetrization;
- (d) the fluctuation–response relation.

The attempt claims:
- (a) as stated;
- (b) the static kernel `(3/π) e^{x₁+x₂} K₀(√2 r)`, going like `1/√r` downstream and "exponential" upstream;
- (c) "None of the channels decays like `1/r` in three dimensions";
- (d) regression holds and equilibrium fluctuation–response fails.

## Step by step

**Step 1 (generating function): holds.** `Σ_t (φz)^t = 1/(1 − φz)` (W1). The zero mode grows linearly.

**Step 2 (the E-identity): holds.** `E(k) = 3(|1 − φ(q)e^{iw}|² + 1 − |φ(q)|²)` at `k = (q₁ + w, q₂ + w, w)`,
identically (W1). It is a two-line identity: `3(|1 − a|² + 1 − |φ|²) = 6 − 6 Re a` with `a = φ e^{iw} = Σ_j e^{ik_j}/3`.

**Step 3 (continuum static kernel): does not follow off the downstream axis.**

On `Z²` the static response to a persistent unit source solves `G = PG + δ`. The predecessor average moves influence only
into the forward quadrant, so
- `G = 0` off `N²`, and
- `G(x) = (G(x − e₁) + G(x − e₂))/2 + (3/2)δ(x)` on it.

By Pascal's rule this gives, exactly,

```
G(x) = (3/2) · C(x₁ + x₂, x₁) / 2^(x₁+x₂)   on N²,   0 elsewhere.
```

W2 checks this in two ways: the stationary equation solved exactly for `x₁, x₂ ≤ 14`, and the time-summed iteration, which
increases to it. From this form:
- **Downstream: holds.** `G(n, n) = (3/2) C(2n, n)/4ⁿ`, and `G(n, n)√(πn)` is `1.4814, 1.4981, 1.4998, 1.49998` at
  `n = 10, 100, 1000, 10⁴`, tending to `3/2`. This is the continuum's downstream law with the same constant, and it
  answers the attempt's section (4): `c = 3/(2√π)` in `n`.
- **Upstream and sideways: fails.** `G` is exactly `0` there. The continuum kernel `(3/π) e^{x₁+x₂} K₀(√2 r)` is positive
  there, and its "upstream exponential" `e^{−2√2 r}/√r` is not the lattice behaviour.
- **Along the edge: fails.** `G(n, 0) = (3/2) 2^{−n}` decays at rate `log 2 = 0.693`, against the continuum's
  `√2 − 1 = 0.414`.

So "plus lattice corrections `O(1/|x|)` smaller than the leading Bessel" is false off the downstream axis: the continuum
form is wrong there at exponential order, or identically. The author's F3 is a torus diagnostic with wrap-around and does
not test this.

**Step 4 (no `1/r` channel): does not follow in two of its four parts.**

- **(i) The static response: holds as a plane object.** In 3D it is the response to a line source (the site at every
  level), a 2D wake.
- **(ii) The time-integrated covariance: not re-derived here.** Its complex pole at `1 − φ = 0` is as stated.
- **(iii) The co-moving point response: fails.**
  - The response to a point source (one site at one level) is exactly the trinomial kernel
    `T(x) = (x₁+x₂+x₃)!/(x₁!x₂!x₃!) · 3^{−(x₁+x₂+x₃)}` in 3D coordinates. W3 checks this by exact iteration to level 12.
  - Its peak at level `t` sits at the drift centre `t(1,1)/3`, which is the 3D point `(t/3)(1, 1, 1)`, at 3D distance
    `R = t/√3`.
  - So along the level axis `T(n, n, n) · R → 3/(2π)`. W3 gives `0.46698, 0.47641, 0.47736, 0.477464` at
    `n = 10, 100, 1000, 10⁵`, against `3/(2π) = 0.477465`.
  - That is a `1/R` law in three dimensions along that ray. Off the ray the kernel decays exponentially (at `(2n, n, 0)`,
    rate `1.42` per `n`).
  - The attempt's "`1/t` with `t ∼ r²` is `1/r²`" converts using the in-plane co-moving distance. The question asks
    about decay in three dimensions.
- **(iv) The eight-corner average: fails.**
  - "has no `1/k²` pole (it stays `O(1)` along an axis)" is false.
  - Along `k = (κ, −κ, 0)`, `κ² R₈ → 3/2` while `κ²/E → 1/2` (W4, sympy limits), so `R₈ ∼ 3/E` there.
  - The four orders with `ε₁ = ε₂` have no drift across this `k`. In general `R₈` is singular like `1/k²` on the planes
    orthogonal to the `(ε₁, ε₂, ε₃)`.
  - Along a coordinate axis it does tend to `3/2`, as the author says.
  - In real space the average is `1/8` of the eight octants' trinomial kernels: `1/R` along the eight body diagonals.

So (c)'s "none of the channels decays like `1/r`" is false as stated. The formation law's point response decays like
`3/(2πR)` along the level axis, and like `3/(16πR)` along each body diagonal after the eight-order average. It is a
*directed* `1/R`, exponentially small off those rays; there is no isotropic `1/r`. That is the precise replacement the task
asks for in (c), and it is not what the attempt states.

**Step 5 (fluctuation–response): the conclusion holds and the example is wrong.**
- The mode `k = (π/2, 0)` of `L = 4` has `φ = (2 + i)/3`, not `(1 + i)/3`. There `1/(1 − φ) = 3(1 + i)/2` and
  `1/(1 − |φ|²) = 9/4` (W5).
- The attempt's "`3/(2 − i)` vs `9/8`" belongs to `φ = (1 + i)/3`, which is not a mode value of `L = 4`. At that value
  `1/(1 − |φ|²)` is `9/7`, as the author's own F5 prints, not `9/8`.
- The conclusion stands: `φ` is not real, so the static susceptibility is not a real multiple of the variance.

## Classic failure modes

- *Change of variables.* Step 4(iii) measures a 3D decay in an in-plane distance.
- *A continuum approximation used beyond its regime.* Step 3's off-axis form, where the lattice kernel has support only on
  the forward quadrant.
- *A general claim argued from one direction.* Step 4(iv): "no `1/k²` pole" from the axis limit.
- *Circularity.* None.

## Verdict

**First failing step: 3.** The step then fails in 4(iii) and 4(iv).

What survives, re-verified: (a), the E-identity, the downstream `1/√r` law with exact constant `3/(2√π)` in `n`, and the
failure of equilibrium fluctuation–response.

The answer to (c), directed `1/R` along the level axis and the body diagonals with no isotropic `1/r`, contradicts the
attempt's claim.

`check.py` prints `SUMMARY: fails at step 3 - ...` and no `HIT: confirmed` line.
