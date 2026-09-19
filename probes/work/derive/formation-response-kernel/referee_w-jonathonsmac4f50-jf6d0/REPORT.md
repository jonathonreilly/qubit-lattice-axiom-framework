# Referee report: J:derive:formation-response-kernel:a6

- **Author:** w-macbookpro90c72-jc53b (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jf6d0 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `3811449d`, and its log.

**Provenance.** The attempt says it locked its own route first. It then uses the referee report of attempt a3 as a
refereed partial (`referee_w-jonathonsmac4f50-jceaa`). That report was written by this referee's model family and first
derived the quadrant Green function, the trinomial point response with `3/(2π)`, and the `1/k²` pole of `R₈`. So this
confirmation is not independent of where those results came from. It is a line-by-line check of the attempt as written,
with checks written afresh. The attempt itself, by another family, acts as the independent re-derivation of the a3-report
findings. a6 adds three items not in that report, all checked below: `R₈ ≡ 3/2` on an axis, no `1/k²` on the drift
diagonal, and the count of non-real modes.

## The problem and the claim

The task asks for four things:
- (a) the linear response and its static limit;
- (b) its real-space form, with exact constants;
- (c) whether any channel decays like `1/r` in three dimensions, and what replaces it;
- (d) the fluctuation–response relation.

The attempt claims the following:
- (a) `R = 1/(1 − φz)`;
- (b) the quadrant Green function `G(n, m) = (3/2) C(n+m, n)/2^{n+m}`;
- (c) a point response that is the trinomial kernel, with `T(n, n, n) · R → 3/(2π)` (a directed `1/R`); `R₈ ≡ 3/2` on an
  axis; a `1/k²` pole of `R₈` along `(κ, −κ, 0)`; none along `(κ, κ, κ)`; and no isotropic `1/r`;
- (d) equilibrium fluctuation–response fails, shown at `φ(π/2, 0) = (2 + i)/3`.

## Step by step

**Step 1 (generating function): holds.** `Σ_t (φz)^t = 1/(1 − φz)` (G1).

**Step 2 (E-identity): holds** identically (G1).

**Step 3 (quadrant Green function): holds.**
- `G(n, m) = (3/2) C(n+m, n)/2^{n+m}` solves `G = PG + δ` on `N²` and is zero outside (G2, exact for `x₁, x₂ ≤ 12`).
- It equals the visit sum `Σ_p multinomial(n+m+p; n, m, p) 3^{−(n+m+p)}` (four points, gap below `10⁻⁴⁰`).
- `G(n, n) √(πn) → 3/2`, which is `G(n, n) ∼ 3/(2√(πn))` as stated.

**Step 4 (point source): holds.**
- The point response is the trinomial kernel (G3, exact iteration to `t = 10`).
- `n T(n, n, n)` is `0.2750525`, `0.2756583` and `0.2756644` at `n = 10², 10⁴, 10⁶`, against `√3/(2π) = 0.2756644`.
- With `R = √3 n`, `T·R → 3/(2π)`.
- The step covariance is `I/3 − 11ᵀ/9`, as used in section (4).
- Off the axis the kernel decays exponentially. G3 measures rates `1.42` along `(2, 1, 0)` and `0.304` along `(2, 1, 1)`,
  per unit of `n`.

**Step 5 (eight-corner classification): holds.**
- `R₈(κ, 0, 0)` simplifies to `3/2` identically. It also equals `3/2` at 20 rational `κ`, to 40 digits (G4).
- Along `(κ, −κ, 0)`, `κ² R₈ → 3/2` and `κ²/E → 1/2`.
- Along `(κ, κ, κ)`, `κ² |R₈|` is `0.034`, `3.5·10⁻⁴` and `3.5·10⁻⁶` at `κ = 0.1, 0.01, 0.001`, so it tends to 0. No
  `ε ∈ {±1}³` has `ε₁ + ε₂ + ε₃ = 0`, so every order drifts along that `k`.

**Step 6 (fluctuation–response): holds.**
- `φ(π/2, 0) = (2 + i)/3`, `1/(1 − φ) = 3(1 + i)/2`, and `1/(1 − |φ|²) = 9/4`.
- 10 of the 15 nonzero modes of `L = 4` have non-real `φ` (G5).
- Regression `C_s = C₀ φ^s` is the linear Gaussian recursion.

**ASSUMED item.** The `Γ(3n)/Γ(n)³` asymptotics are standard Stirling and are stated as ASSUMED. G3's values at
`n = 10⁶` agree with the limit to `6·10⁻⁸`.

## Classic failure modes

None found:
- The directed `1/R` is along one ray, and the attempt says so ("not isotropic").
- `R₈`'s pole is directional, and the residue varies with direction.
- No statement is extended beyond what is checked or proved.

## Verdict

The partial result survives with no failing step. `check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
