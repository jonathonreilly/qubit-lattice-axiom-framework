# discrete-step-walk-under-the-clock-clause, attempt 1 of 3 — unitary, local, a clock: pick two

Worker `w-jonathonsmac4f50-j0f4f` (`claude-opus-5`), unit
`J-derive-discrete-step-walk-under-the-clock-clause:a1`.

**Provenance.** No prior attempt existed on this problem at claim time. Blocks 53 and 54 are taken
as the unit states them (both **supplied clauses, not adopted**); I did not re-derive them, and
they were produced in the same campaign by the same model family.

## 1. What is claimed

> **No formulation of "the amplitude at a site advances in that site's own time" is
> simultaneously unitary, local, and a clock.** The three natural candidates each fail a different
> one of the three:
>
> | formulation | unitary | local | a clock |
> |---|---|---|---|
> | site-dependent coin angle `θ_x` | **yes** | **yes** (range 1) | **no** — it is a *mass* gradient |
> | site acts on a fraction `w_x` of ticks | **no** | yes | yes (in the mean) |
> | a genuine fractional step `U^{w_x}` | yes | **no** (unbounded range) | yes |
>
> **(a)-i.** A coin gradient is unitary for *any* assignment `x ↦ θ_x` (a block-diagonal unitary
> composed with a fixed shift) and strictly nearest-neighbour. But the dispersion is
> `cos ω = cos θ cos k`, which is **not separable** as `w(x)ε(k)`: the ratio `ω(π/6)/ω(π/3)` runs
> `0.6436 → 0.8519 → 1.0000` across `k = π/6, π/3, π/2`. A clock rescales every energy by one
> factor; a coin angle reshapes the band. The gap is `ω(0) = θ`, so **θ is a mass**.
>
> **(a)-ii.** As a deterministic map, "act on a fraction `w`" is `M = wU + (1−w)I`, and
>
> ```
> (M†M − I)₀₀ = −2 w (w−1) (cos k cos θ − 1)
> ```
>
> Since `cos k cos θ − 1 ≤ 0` and `w(w−1) < 0` strictly on `0 < w < 1`, this is nonzero at every
> intermediate `w` and vanishes **only** at the endpoints `w ∈ {0,1}`. Read instead as a *random*
> choice of which sites step, each realization is unitary and the clause holds in the mean — but
> the state then evolves by a channel, not a unitary, which is a different theory.
>
> **(a)-iii.** A true fractional step `U^w` has eigenvalues `e^{−iwω}`, so its symbol's trace is
> `2cos(wω)`; at `w = 1/2` that is `√((1 + cos θ cos k)/2)`. A strictly range-`R` operator has a
> symbol whose entries are trigonometric **polynomials** of degree `≤ R`. This square root has
> Fourier coefficients `+0.651706, +0.191074, −0.031422, +0.010706, −0.004632, …` — decaying
> geometrically but **never truncating**. A site cannot take a fraction of a step without reaching
> arbitrarily far.
>
> **(b)** For the one formulation that is unitary *and* local, the rays are the Hamiltonian flow of
> `ω = arccos(cos θ(x) cos k)`:
> `ẋ = cos θ sin k / sin ω`, `k̇ = −(sin θ cos k / sin ω)·θ′(x)`.
> A propagation on a line tracks this to **0.23 %** of a 54.7-site displacement. Block 54's law
> `dv_j/dt = −w²cos(2k_j)∂_j u + 2(v·∇u)v_j` **does not apply**: its `2(v·∇u)v` term is the
> signature of the separable `E = w(x)ε(k)`, and (a)-i showed the discrete dispersion is not
> separable. The two agree only where the gradient vanishes.
>
> **(c) No.** With a uniform coin gradient the entrywise ratios `(UT)_ij/(TU)_ij` take **12
> distinct values**, so no scalar `λ` satisfies `UT = λTU`. Block 54's identity rests on
> `H_w = √w H √w` being *multiplicative* in the clock, so a uniform gradient rescales it by a
> constant under translation. The discrete step is a coin composed with a shift, and a coin
> gradient enters **inside a cosine**, not as a prefactor — there is nothing for a translation to
> factor out.

## 2. The steps

1. **PROVED + CHECKED (`W1`).** One step is unitary with `det = 1`; `trace = 2cos θ cos k`, hence
   `cos ω = cos θ cos k`; group velocity `cos θ sin k/√(1 − cos²θ cos²k)`.
2. **CHECKED (`W2`).** Unitarity on a ring of 6 with `θ_x = 1/5 + x/10`, exactly.
3. **PROVED + CHECKED (`W3`).** Non-separability, from the three exact ratios.
4. **PROVED + CHECKED (`W4`).** The factored deviation, plus three exact intermediate values.
5. **PROVED + CHECKED (`W5`).** The half-angle identity verified by squaring
   (`2cos²(ω/2) − 1 = cos ω`, with `cos(ω/2) ≥ 0` on `0 ≤ ω ≤ π` fixing the branch), and the
   Fourier coefficients computed to 30 digits.
6. **PROVED (`W6`).** The ray law read off `ω` by differentiation.
7. **CHECKED, NUMERIC (`W7`).** Propagation of a 241-site line, 60 steps, gradient `0.0020`:
   centroid `174.6836` against ray `174.8119`. Norm held to `1.000000000000`.
8. **CHECKED (`W8`).** The 12 distinct ratios.

## 3. Where this stops

- **`W7` is floating point**, unlike everything else. It follows **one** ray, not the cloud the
  unit mentions, so it tests that `W6`'s law is the right one — it is not a measurement of the
  packet's spread, and it says nothing about the sideways drift `gT/(2k)` that block 54 reports
  and that no ray has.
- **The sideways drift is untouched.** That is the most interesting open number in block 54 and
  this attempt does not address whether a discrete walk shows it.
- **One coin convention, one dimension.** I use the rotation coin `[[c,−s],[s,c]]` with a
  right/left shift on a line. A split-step walk, or the 3D walk of block 54 with `σ_j`, may admit
  a formulation I have not considered — in particular, the table's "pick two" is a statement about
  *these three* candidates, not a proof that no fourth exists.
- **(a)-iii's locality argument is about the symbol.** I show `cos(ω/2)` is not a trigonometric
  polynomial and exhibit non-truncating coefficients numerically; I do not prove a general theorem
  that no finite-range `V` has `V² = U`.
- **`W8` is one ring, one gradient.** A single counterexample suffices to deny the identity, but I
  have not characterized what weaker identity, if any, survives.

## 4. What would finish it

1. The sideways drift in discrete steps: propagate a packet with a transverse gradient and look
   for `gT/(2k)`. If the discrete walk shows it too, it is not an artifact of continuous time.
2. A theorem for (a)-iii: no finite-range `V` with `V² = U`, rather than the symbol argument.
3. The split-step walk, which has two angles and might separate the mass from the rate — that is
   the obvious place a fourth formulation could hide, and it is where I would look next.
4. Another model family on all of it; and blocks 53/54 are same-family inputs.

## 5. Running it

```
python3 probes/work/derive/discrete-step-walk-under-the-clock-clause/w-jonathonsmac4f50-j0f4f/check.py
```

`sympy` and `mpmath`; 17 checks. Everything is exact symbolic or exact rational except `W7`'s
propagation and `W5`'s Fourier coefficients (30-digit quadrature), both marked as such in the
output. Runs in about a minute.

**One correction made before shipping.** My first `W7` initialized the packet as an equal
superposition of the two coin states. That splits into the two bands and its centroid tracks *no*
single ray — the packet drifted left while the ray went right, a 407 % "error" that was entirely
my own setup. Starting in the band eigenvector of the symbol at `(k₀, θ(x₀))` brought it to
0.23 %. The lesson is worth stating: a coined walk has two bands, and a ray comparison is only
meaningful for a state prepared in one of them.
