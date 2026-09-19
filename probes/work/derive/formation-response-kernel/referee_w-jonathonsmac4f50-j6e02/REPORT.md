# Referee report: J:derive:formation-response-kernel:a2

- **Author:** w-macbookpro90c72-j88ab (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j6e02 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `f57f7576`, and its log.

`check.py` in this directory re-verifies the finite facts with independent code (exact rationals, sympy, mpmath).

This attempt was committed before this referee family's a3 referee report. Where the results coincide (the quadrant Green
function, the `3/(2πr)` spine, `R_sym = 3/2` on an axis), they were found independently.

## The problem and the claim

The task has four parts: the linear response, its real-space form with exact constants, the "any `1/r` channel?" question,
and fluctuation–response.

The attempt claims the following:
- (a) `R = 1/(1 − φe^{iw}) = 3/(3 − Σ e^{iq_j})`, the E-identity, and that `1/E` is not a multiple of `R` or `|R|²`;
- (b) the impulse response is the multinomial, with the co-moving Gaussian `3√3/(2πt) e^{−3(y₁² + y₂² + y₁y₂)/t}`;
- (b) the static Green function is `G = (3/2) C(n+m, n)/2^{n+m}` on the forward quadrant, and a pin gives `αG/G(0)`;
- (c) a table of channels, none of which is an isotropic `1/r`;
- (d) equilibrium fluctuation–response fails.

## Step by step

**Steps 1–2 (generating function, 3D embedding, E-identity): hold.**
- The impulse response is the multinomial. H2 checks this by exact iteration to `t = 8`.
- `R = 3/(3 − Σ e^{iq_j})`, `E = 3(|1 − φe^{iw}|² + 1 − u)` and `1/E = |R|²/(3(1 + (1 − u)|R|²))` hold identically (H1).

**Step 3 (torus `(I − P)^{−1}`): holds.** It is the standard DFT inversion on mean-zero functions and was not re-derived
beyond H2.

**Step 4 (jets, co-moving Gaussian): holds** as stated. `C = (1/9)[[2, −1], [−1, 2]]`, `det C = 1/27`,
`C^{−1} = [[6, 3], [3, 6]]`, and the constant is `3√3/(2πt)` (H2). The local-CLT remainder is marked ASSUMED.

**Step 5 (infinite-plane Green function): holds.**
- `3/(2 − X − Y)` expands to `G(n, m) = (3/2) C(n+m, n)/2^{n+m}` (H2, to order 6), and `G(n, 0) = 3/2^{n+1}`.
- The pin profile `αG/G(0)` is harmonic off the pinned site and equals `α` there (H2).
- On a torus the pinned field is constant, as stated.

**Step 6 (time-integrated covariance): holds.**
- `Σ_s C_s = σ²/|1 − φ|²` is an identity in `φ` (H3).
- At `w = 0` its ratio to `1/E` takes the values `9/2`, `27/5` and `9` on the nonzero `L = 4` modes (H3), matching the
  attempt's "at least three".

**Step 7 (fluctuation–response): holds.** 10 of the 16 `L = 4` modes have non-real `φ`. `(1 − u)/(1 − φ)` takes 8
distinct values, some of them non-real (H5).

**Step 8 (eight corners): holds.**
- `R_sym(λ, 0, 0) = 3/2` identically.
- `R_sym(λ, λ, λ) → 7/2`.
- `G_sym(n, 0, 0) = 3^{−n}/2`.
- `n G(n, n, n)` is `0.275053`, `0.275658` and `0.275664` at `n = 10², 10⁴, 10⁶`, tending to `√3/(2π)` (H4).

**Step 9 (no isotropic `1/r`): holds**, with one loose phrase.
- The conclusion follows. An isotropic `c/|x|` would have Fourier transform `∼ c'/|q|²` along every path to the origin,
  and `R_sym` stays at `3/2` along an axis.
- The bullet "Eight-corner static symbol: … not `1/k²`" is true on the axes and the body diagonal, which are the
  directions it names.
- It is false as a blanket statement. Along `(κ, −κ, 0)`, `κ² R_sym → 3/2` (H4): the four orders with `ε₁ = ε₂` have no
  drift across this `k`. This does not affect the conclusion; it locates the directed `1/R` of the body-diagonal spines in
  Fourier space.

## Classic failure modes

- *A statement read beyond the checked directions.* The Step 9 bullet, which is harmless to the conclusion.
- *Outside theorems.* The local CLT and Stirling are marked ASSUMED, as they should be.
- *Circularity.* None.

## Verdict

The partial result survives with no failing step. One bullet of Step 9 is overstated as a blanket claim.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
