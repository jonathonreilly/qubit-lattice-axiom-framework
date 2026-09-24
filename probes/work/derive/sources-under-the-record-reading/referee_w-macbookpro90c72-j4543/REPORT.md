# Referee report: J:derive:sources-under-the-record-reading:a3

- **Author:** `w-jonathonsmac4f50-j556e` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j4543` (`grok-4.6`). Different model family.
- **Checks:** the held-wall operator and the formation ledger, recomputed. The author's script is not called.

## The statement

Replacing an amplitude of ledger `L` by one record at `y` keeps the ledger exactly when the record's bare energy is `L / (1 − (γ/12) g_yy L)`. At weak field the record must be heavier by `(γ/12) E² (g_yy − ⟨ρ, gρ⟩)`. Averaged over odds this excess is nonnegative on `Z³` and can have either sign in a box. For a symmetric star it does not depend on the walls.

## Steps

**1.** The algebra `m' / (1 + (γ/12) g_yy m') = L` solves to the displayed `m'`.

**2.** On the interior of the `5³` box, with walls held at 1, the uniform 7-site star at `γ = 1` gives exactly `1188/1091`. The same float, to `10⁻⁹`, comes out of the `7³` box. A centre-heavy star at `γ = 7/3` matches across the two boxes. Lopsided weights give `1.082359` against `1.082223`.

**3.** On the `7³` interior the star's excess `Σ ρ_y g_yy − ⟨ρ, gρ⟩` is positive (`0.966`). An amplitude with weight `99/100` at the centre and `1/100` at a corner, with the odds at that corner, gives `g_corner = 1.11341 < 1.34676`.

**4.** At `γ = 10⁻⁸` the ledger's slope is `−⟨ρ, gρ⟩/12`, to `10⁻¹¹`.

On `Z³` the same excess is `G₀(0) − ⟨ρ, gρ⟩`. Positive-definiteness gives `g_xy ≤ G₀(0)`, so it is nonnegative for every odds. That bound was not recomputed as an infinite-lattice sum. Parts (a), (c) and (d) are the attempt's reading and a numerical proposal; they were not re-run.

## Verdict

The formation bookkeeping survives. The required record energy is the displayed rational, and the walls drop out for a symmetric star.
