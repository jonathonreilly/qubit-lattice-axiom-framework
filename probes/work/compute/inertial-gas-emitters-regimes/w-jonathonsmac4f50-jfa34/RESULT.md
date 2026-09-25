# Emitting bodies across regimes — run 1 of 2

Worker `w-jonathonsmac4f50-jfa34`, model `claude-opus-5-5`. Block 44 was written by the same model family (Claude). The log is `logs/probes/C:inertial-gas-emitters-regimes:a1/w-jonathonsmac4f50-jfa34__5b8b2de3__20260925T095553Z.*`. No HIT line: the task gives two rival expectations and asks which holds where.

**Result:** in every resolved case (13 of 27 grid points, at 2σ) emitting bodies **repel**. No point attracts. The repulsion is present at all three γ, including γ = 4, whose estimated mean free path (0.08 sites) is far below the separations. So no crossover to the ideal-fluid attraction appears on this grid. At separation 32 nothing is resolved.

## As landed on main

Block 44 (#8550):
- T4: no mean force on a reflecting body in the uniform state.
- Forces between bodies are "historical author observations, not fresh evidence".
- The author's emitting pair (Q = 5, γ = 1, side 96, no single-body subtraction) had −0.209, −0.061, −0.004 (± 0.02) at separations 12, 20, 32.

## Set-up

- **Simulator.** `probes/lib/inertial_bodies.py` / `inertial.py`, unchanged: `emit()`, then `tick_s(..., absorb=False)`, then `reservoir()` each tick, as in the lib's main.
  - Reflecting spherical bodies of radius 3, each emitting Q records per tick with the recoil booked.
  - Side 96 (the author's; the task names none), density 0.3, reservoir on the two outer layers, 2000 warm-up ticks.
- **Grid.** Q = 2, 5, 10; separations 12, 20, 32; γ = 0.1, 1, 4.
- **Each point.**
  - An emitting pair: the force towards the other body, averaged over the two bodies.
  - A single emitting body at the pair's first position: the control, subtracted.
- **Statistics.** 4000 measured ticks (3000 at γ = 4), one seed per job. Errors are standard errors over blocks of 500 ticks, so 6–8 blocks; the error bars themselves are uncertain by about 25 %.
- **Scope against the task.** The whole grid ran, in 4.6 h on six processes.
- **References printed.**
  - The ideal-fluid attraction Q²/(4πρr²) named in the task.
  - A product-state mean-free-path estimate (1/√3)/(6γρ): 3.2, 0.32 and 0.08 sites at γ = 0.1, 1, 4. It is an estimate, not a measurement.

## Net force towards the other body per tick (pair minus single control)

| γ | Q | sep 12 | sep 20 | sep 32 |
|---|---|---|---|---|
| 0.1 | 2 | −0.073 ± 0.033 | −0.064 ± 0.028 | −0.004 ± 0.046 |
| 0.1 | 5 | −0.214 ± 0.047 | −0.090 ± 0.042 | −0.029 ± 0.033 |
| 0.1 | 10 | −0.514 ± 0.043 | −0.194 ± 0.045 | +0.011 ± 0.048 |
| 1 | 2 | −0.061 ± 0.026 | −0.016 ± 0.040 | +0.001 ± 0.033 |
| 1 | 5 | −0.113 ± 0.029 | −0.054 ± 0.042 | +0.006 ± 0.035 |
| 1 | 10 | −0.258 ± 0.028 | −0.137 ± 0.047 | +0.036 ± 0.039 |
| 4 | 2 | −0.062 ± 0.037 | −0.011 ± 0.043 | +0.027 ± 0.048 |
| 4 | 5 | −0.195 ± 0.042 | −0.063 ± 0.046 | −0.015 ± 0.035 |
| 4 | 10 | −0.413 ± 0.045 | −0.108 ± 0.044 | −0.025 ± 0.072 |

For comparison, the ideal-fluid attraction Q²/(4πρr²) at separation 12 is +0.0075, +0.047 and +0.19 for Q = 2, 5 and 10.

## What the numbers say

- **Sign.** Repulsion wherever resolved. The ideal-fluid attraction, which is +0.19 per tick at Q = 10 and separation 12, is not seen.
  - The measured force there is −0.26 to −0.51, opposite in sign and larger.
- **Dependence on Q.** At separation 12, F/Q is roughly constant:
  - −0.036, −0.043, −0.051 at γ = 0.1;
  - −0.031, −0.023, −0.026 at γ = 1;
  - −0.031, −0.039, −0.041 at γ = 4.
  - So the force grows about linearly in Q, not as Q₁Q₂ = Q².
  - Each body is a reflecting obstacle in the other's outflow, so the push on one body scales with the other's emission rate. This fits the author's reading, "each stands in the other's outflow".
- **Dependence on separation.** From 12 to 20 at Q = 10 the force falls by 2.6 (γ = 0.1), 1.9 (γ = 1) and 3.8 (γ = 4), against 2.8 for 1/r².
  - At 32, the three Q = 10 values average about +0.01 ± 0.03. A 1/r² extrapolation from 20 predicts about −0.08, −0.05 and −0.04.
  - So the repulsion may fall faster than 1/r² beyond 20, or be offset there by an attraction of the ideal-fluid size (+0.026 at Q = 10, separation 32). This grid cannot tell which.
- **Dependence on γ.**
  - The repulsion does not weaken monotonically as the mean free path shrinks. At separation 12 it is weakest at γ = 1: Q = 10 gives −0.51, −0.26 and −0.41 at γ = 0.1, 1 and 4, and Q = 5 gives −0.21, −0.11 and −0.20.
  - No crossover to attraction appears, even though the estimated mean free path is below the separation at all three γ.
- **Against the author.** My pair-only value at Q = 5, γ = 1, separation 12 is −0.166 ± 0.022, against the author's −0.209 ± 0.016 (1.6σ).
  - The single-body control there is −0.053 ± 0.020, so part of the raw pair force is the box's effect on an off-centre emitter.

## Answer

- **Sign and size in each regime.** Emitting bodies repel in all three regimes, by 0.06–0.5 per tick at separation 12 (growing about linearly with Q), and by 0.06–0.2 at separation 20 wherever resolved there (γ = 0.1 at every Q; Q = 10 at every γ).
- **Crossover.** None appears on this grid as the mean free path falls, and the ideal-fluid attraction is not observed.
- **Separation 32.** The force is unresolved there; better statistics or a larger box are needed to see whether a weak attraction takes over at large separation.
