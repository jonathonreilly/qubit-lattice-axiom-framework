# Referee: inertial-gas viscosity and damping, a2

Author `w-macbookpro90c72-jd030` (claude-opus-5-5). Referee `w-macbookpro90c72-jd3a9` (grok-4.6).

Inside the one-point product closure the six-axis sound damping is

`Γ = 2/3 + ρ/6 + γρ/2 + 1/(3γρ)`.

An isolated pair does not keep relaxing at that rate: the redraw is a projector, so a second collision on the same bond does nothing.

## What was recomputed

1. **Redraw.** Two six-axis records are redrawn uniformly inside their total-momentum class. There are 19 classes: 6 singletons (both records equal), 12 pairs (orthogonal records, the two orders), and one class of 6 (opposite records). The matrix `T` is symmetric and stochastic, `T² = T`, and `(T−I)² = −(T−I)`. The isolated-pair semigroup is therefore `I + (1−e^{−γt})(T−I)` and saturates at `T`.

2. **One site.** The linearized collision operator at `k = 0` is `γρ(U+V−6I−J)` with `U = V`. Eigenvalues: `0` four times (density and three momenta) and `−2γρ` twice (the axis quadrupole). One collision with a uniform partner retains `1/2` of the momentum and `1/3` of the quadrupole.

3. **Closure.** Along an axis the transverse mode `(0,0,1,−1,0,0)` has eigenvalue `−(1−cos k) ρ(1/3+γ)`, so `ν_T = ρ/6 + γρ/2` with no `1/(γρ)` piece. `Γ` is minimized at `γρ = √(2/3)`.

4. **Sphere moments.** `⟨s_x²⟩ = 1/3`, `⟨s_x⁴⟩ = 1/5`, `⟨|s_x|⟩ = 1/2`, `⟨|s_x|³⟩ = 1/4`, `⟨|s_x| s_y²⟩ = 1/8`, and `⟨s_x² s_y²⟩/⟨s_y²⟩ = 1/5`. These turn into the kinetic pieces `4/(135γρ)` and `1/(45γρ)`, the streaming pieces `3/(8√3)` and `√3/16`, and `D = 1/(4√3)`.

5. **Leading dampings** at `ρ = 0.3`, `γ = 1`, from `(Γ/2)k²` with `k = 2π/L`. Six axes: `0.0095` and `0.0381` at `L = 64` and `32`. Sphere: `0.0031` at `L = 64`. The attempt's table prints `0.0096` and `0.0396`; the difference is the next order in `k`, which was not recomputed. The tick replacement `γ → 1−e^{−γ}` and `1/λ → 1/λ−1/2` gives a leading six-axis damping `0.0108`.

The Galerkin truncation, block 44's split-tick simulator, and the continuous-time runs were not rebuilt. The exact saturation `(T−I)² = −(T−I)` is the recollision the attempt names: after one redraw an opposite pair stays in the opposite class, and another redraw does not relax it further.

`SUMMARY: confirmed — the closure's six-axis Gamma is 2/3 + ρ/6 + γρ/2 + 1/(3γρ), and an isolated pair saturates after one redraw.`
