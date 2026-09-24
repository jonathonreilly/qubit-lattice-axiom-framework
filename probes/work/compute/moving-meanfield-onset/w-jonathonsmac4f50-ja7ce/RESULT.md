# A first theory of the clumping onset: the six-axis gas with vacancies — run 1

Worker `w-jonathonsmac4f50-ja7ce`, model `claude-opus-5-5`. The blocks and the scan logs come from the same model family (Claude). `run.py` takes about 70 seconds.

## Mean field

Take the variational (Gibbs–Bogoliubov, i.e. Bragg–Williams) bound with a product trial law: each site is occupied with probability `ρ` and carries content `s` with probability `x_s`. The free energy per site, i.e. the static law's `−log` weight per site with 3 bonds per site, is

`f(ρ, x) = −3ρ² Σ_{s,s'} x_s x_{s'} log(c ω(s,s')) + ρ log ρ + (1−ρ) log(1−ρ) + ρ Σ_s x_s log x_s`.

## Exact results (sympy), at the disordered point `x = 1/6`

- **Density:** `∂²f/∂ρ² = 1/ρ + 1/(1−ρ) − 6L̄`, with `L̄ = log c + (log p + log q + 4 log r)/6`, the geometric-mean log weight.
- **Content:** in the sum-zero directions the curvature is `6ρ(1 − ρ log(p/q))` for the vector (alignment) mode and `6ρ(1 − ρ log(pq/r²))` for the quadrupole mode.
- **No coupling:** the disordered point has no cross term between `ρ` and content.

So the three instabilities of the uniform disordered state are:
- **Density (uniform clumping):** `6ρ(1−ρ)L̄ = 1`. On `(p,1,2)` at `ρ = 0.3` this is `p = 7.31` at `c = 1` and `p = 468` at `c = 1/2`. At the neutral scale there is none, since `L̄ < 0` for every `p`: the geometric mean of `c₀ω` is below the arithmetic mean, which is 1.
- **Alignment:** `ρ log(p/q) = 1`, i.e. `p = e^{10/3} = 28.0`, independent of `c`.
- **Quadrupole:** `ρ log(pq/r²) = 1`, i.e. `p = 112`.

## Coexistence of a dilute and a dense aligned phase

This comes from the lower convex hull of `min_x f(ρ, x)` (floating point). The onset `p*` is the least `p` at which `ρ = 0.3` lies in a two-phase region.

| scale c | mean-field p* | tie line just above p* | executed bracket (X logs, ρ = 0.3, clumped := neighbours/random > 1.5) | MF / midpoint |
|---|---|---|---|---|
| neutral `6/(p+9)` | 6.23 | ρ 0.292 ↔ 0.933 (aligned) | 11–12 (task's first look: 8–12) | −46% |
| 1 | 3.74 | ρ 0.258 ↔ 0.975 | 4–6 (first look: 5–6) | −25% |
| 1/2 | 5.51 | ρ 0.288 ↔ 0.954 | 7–8 (first look: 8–12) | −27% |

The executed brackets come from the 121 logs under `logs/probes/X:moving-clumping-line-p12/`. The mean neighbours/random ratio by `p` is:
- **neutral:** 7:1.02, 8:1.03, 9:1.05, 10:1.17, 11:1.43, 12:1.54, 14:1.69, 16:1.81, 20:1.92;
- **c = 1:** 4:1.49, 6:2.28, and a plateau near 2.5;
- **c = 1/2:** 6:1.13, 7:1.18, 8:1.60, 9:1.96, …

The executed neutral onset sits nearer 11–12 than the first look's "near 10".

## Reading

**Clumping is a first-order event.** At all three scales the onset comes from coexistence, not from a spinodal:
- A dense, fully aligned phase (ρ ≈ 0.93–0.98) coexists with a dilute disordered one.
- Every coexistence onset lies well below the alignment spinodal (28) and below the density spinodal (7.3 at c = 1, and none at the neutral scale).

**Agreement with the task's expectation.**
- Mean field puts the onset too low by 25–46%.
- It gets the ordering in `c` right: `c = 1 < 1/2 <` neutral, which is also the executed order.
- No result contradicts the expectation, so there is no HIT.
