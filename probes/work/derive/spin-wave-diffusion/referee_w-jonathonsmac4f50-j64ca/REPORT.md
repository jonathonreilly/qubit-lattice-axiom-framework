# Referee report: J:derive:spin-wave-diffusion:a1

- **Author:** w-macbookpro90c72-j2b02 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j64ca (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `f9d3e0bd`, and its log.

**Provenance.** The attempt proves the `L = 1` law that this referee family's report on a2 recorded as `1/A(3β)` up to
`e^{−6β}` (`referee_w-jonathonsmac4f50-j1ab5`, check V5). The checks here are written afresh with sympy and mpmath.

## The claim

On `L = 1` the single site is its own three predecessors, so `κ = 3β` and `m̂ = s`. The one-step direction rate is
`1 − A(3β)`, and

```
D₁L²/σ² = [1 − 6β/(e^{6β} − 1)] / A(3β) = 1 + 1/(3β) + 1/(9β²) + …
```

This is not identically 1, so a2's `1/(1 − σ²G_L)²`, which equals 1 at `L = 1`, is false as a finite-`L` identity. The
attempt also records `G_4 = 189/128` and the sphere Jacobian `1/|M|²`. It leaves the general-`L` combination open.

## Step by step

**Step 1 (vMF chordal moment): holds.**
- `E|s − u|² = 2 − 2A(κ)`, checked by quadrature at `κ = 0.7`, `3` and `10`.
- `A(κ) = 1 − 1/κ + 2/(e^{2κ} − 1)` holds identically (U1).

**Step 2 (the `L = 1` ratio): holds.**
- `κ(1 − A(κ)) = 1 − 2κ/(e^{2κ} − 1)`.
- So `(1 − A)/σ² = [1 − 6β/(e^{6β} − 1)]/A(3β)`. Its values at `β = 6, 12, 24, 48` are `1.0588`, `1.0286`, `1.0141`
  and `1.0070`.
- The remainder after `1 + 1/(3β) + 1/(9β²)`, multiplied by `β³`, tends to `1/27` (U2). The expansion is as stated, and
  the ratio is not identically 1.

**Step 3 (`G_4`, `G_1`): holds.** `G_4 = 189/128`, and `G_1 = 0` because `L = 1` has no nonzero mode (U3).

**Step 4 (Jacobian): holds.** `(n_x/ε)² → 1/m²` (U3).

**A point of reading.** On `L = 1`, the script's estimator at lag `ℓ` is `(1 − A^ℓ)/ℓ`, and its smallest lag is 25 levels.
At `β = 6` that gives `0.0304` at `ℓ = 25`, against `0.0556` at `ℓ = 1` (U4, INFO). So "the script's `D₁` is `1 − A(3β)`"
holds for the one-step rate, which is the natural meaning of a diffusion constant, and not for the script's lag-25 number on
`L = 1`. At `L = 16`, where block 34's table was executed, the per-lag displacements are small and this does not arise.

## Classic failure modes

None found. The general-`L` statement is explicitly left open, and the product formula of section (3) is labelled unproved.

## Verdict

The exact `L = 1` law survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
