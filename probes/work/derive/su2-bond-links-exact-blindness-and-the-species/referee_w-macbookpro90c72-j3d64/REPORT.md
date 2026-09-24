# Referee report: J:derive:su2-bond-links-exact-blindness-and-the-species:a3

- **Author:** `w-macbookpro90c72-j5d78` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j3d64` (`grok-4.6`). Different model family.
- **Checks:** Gaussian-rational SU(2) on the `4³` torus, written independently of the attempt's script.

## The statement

The task asks for a link-dressed frame walk that is hermitian and gauge covariant, for block 65's twist hop as the first-order pure-gauge link, for the species maps as a flat `ℤ₂` connection, and whether that changes block 74's count of two species served out of eight. The attempt answers the last question in the negative at first order. That is the statement, not a claim that all eight are served.

## Steps

**R1–R2.** Inverse stereographic images of rational points lie in SU(2). Conjugation of the Pauli matrices is a rational rotation of determinant 1.

**R3–R4.** For a rational frame, rational links and two states, `⟨φ, Hψ⟩ = ⟨Hφ, ψ⟩`. For a site-dependent `g`, `H[gEg†, g_x U g_y†] gψ = g Hψ` at every site. Exact covariance is the blindness the task asked for.

**R5.** With `g = exp(−iθ·σ/2)`, the first-order link is `U = 1 + (i/2)(d_e θ)·σ`. In the anticommutator with `σ_j` only the longitudinal piece survives, and it equals `½ C_j[∂_j θ_j]`. Together with the rotated frame `σ_j + (θ × e_j)·σ`, the sum equals `−(i/2)[θ·σ, H]`. The task's `exp(+iθ·σ/2)` flips the sign of `θ` on both sides of that identity; the attempt records the flip. The identity itself holds.

**R6.** `g_x = (−1)^{n·x} iσ_c` is in SU(2) for every species `n` and axis `c`. It sends `U = 1` to `U' = (−1)^{n_j}`, whose plaquettes are `1`. A species-`n` zero mode maps to a constant zero mode of `H[ρ_c E, U']`. The eight species are the eight flat `ℤ₂` backgrounds of one species.

**R7.** `Θ_a^j = Re ψ† σ_a S_j^U ψ` turns by the same rotation. A coin-blind energy, built from `EᵀE` and holonomies, therefore has the same served-species count at fixed links.

The dynamical step uses only the structure the attempt marks as assumed: transporting a connection produces curvature plus a gauge term, and the gauge term drops out of a gauge-invariant energy. The species backgrounds are flat, so the curvature they induce is first order in the content and the force is second order. Block 74's shear deficit is first order. No connection term cancels it at that order. The count stays two of eight. That does not meet a HIT that all eight are served; the attempt does not claim it does.

## Verdict

The partial result survives.
