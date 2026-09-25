# Two records with a delayed clock field — run 1

Worker `w-jonathonsmac4f50-j1524`, model `claude-opus-5-5`. Block 95 was written by the same model family (Claude), as was the derivation in issue #9158 on this problem. The log is `logs/probes/C:the-delayed-clock-two-records:a1/w-jonathonsmac4f50-j1524__17164df8__20260925T060451Z.*`.

**HIT:** the expectation fails on two counts. In label time the pair law does not return at large Γ, and the record's diffusion does not slow for small Γ. Details below.

## As landed on main

Block 95 (#8860), T2/T3: with the clock recomputed after every move, the relative weight per offset is `exp(−qλG(d))`. It is a neutralized-torus residence weight, and "formation and delayed clocks are absent".

## The task's dynamics

- Field: `du_z/dt = Γ w_z ((1/q) Σ_e u_{z+e} − u_z + λ(n_z − n̄))`, with `w = e^u`.
- Hops: a record at x hops to each empty neighbour at rate `w_x/q`; the bare total rate is 1.
- Settings: ring of 12 (q = 2) and 8³ torus (q = 6); λ = −1/2, −1; Γ = 100, 10, 1, 0.1.

## Exact statements (sympy)

1. **Fixed points.** They are block 95's field plus any constant.
2. **Scaling.** The dynamics is invariant under `u → u + c`, `t → t e^{−c}` (residual 0). So the process in internal time `dτ = e^{ū} dt`, with the mean projected out, is exactly the label-time process; the label time adds only the global factor.
3. **Conserved quantity.** `d/dt Σ_z 1/w_z = −Γ Σ_z r_z = 0`: **Σ 1/w is conserved, the mean clock is not.** This invariant is also derived in #9158.
   - In the slaved limit, `u = u95(C) + c(C)` with `e^{c(C)} = Z(C)/S0`, where `Z(C) = Σ_z exp(−qλ Σ_r G(z − r))`.
   - Every rate carries this configuration factor.
   - So the **label-time** slaved law is block 95's law divided by `Z(C)`, while the **internal-time** law is block 95's.

**Predicted label-time law π95/Z**, as `⟨G(d)⟩` fraction of the way from random placement to block 95's law:

| system | λ = −1/2 | λ = −1 |
|---|---|---|
| ring of 12 | 0.627 (TV 0.064 from π95) | 0.349 (TV 0.217) |
| 8³ | 0.989 (TV 1e−4) | 0.973 (TV 6e−4) |

The instantaneous chain (block 95's own) was simulated separately during development and reproduces π95 (TV 0.004).

## Separation law

Simulated with numba: RK4 for the field (step bounded for stability), thinning for hops, 4 seeds per point. The table gives `⟨G(d)⟩` as the fraction of the way from random to block 95's law.

| ring of 12 | Γ = 100 | 10 | 1 | 0.1 |
|---|---|---|---|---|
| λ = −1/2, internal time | **1.047 ± 0.008** | 0.987 ± 0.029 | 0.700 ± 0.022 | 0.211 ± 0.010 |
| λ = −1/2, label time | **0.678 ± 0.009** | 0.650 | 0.545 | 0.202 |
| λ = −1, internal time | **1.038 ± 0.020** | 1.019 ± 0.025 | 0.998 ± 0.010 | 0.687 ± 0.009 |
| λ = −1, label time | **0.395 ± 0.026** | 0.389 | 0.577 | 0.567 |

**On 8³** (weak signal: uniform placement is within TV 0.009 and 0.018 of the target), internal time, λ = −1: 0.98 ± 0.29, 1.26 ± 0.18, 0.55 ± 0.15, 0.13 ± 0.15. Label time agrees with internal time there, since Z(C) is nearly constant.

**Reading.** As Γ grows, the internal-time law returns to block 95's. The label-time law, which is the task's "time-weighted law", goes instead to π95/Z(C): measured 0.678 and 0.395, against 0.627 and 0.349 predicted. The small excess is consistent with finite Γ and the start from the farthest separation. On the ring of 12 the difference is large. On 8³ it is below the noise.

## One record: mean-square displacement per unit label time (bare 1)

32 seeds per point.

| system, λ | Γ = 100 | 10 | 1 | 0.1 | own clock `exp(qλG(0))` |
|---|---|---|---|---|---|
| ring, −1/2 | 0.368 | 0.285 | 0.866 | 0.932 | 0.370 |
| ring, −1 | 0.173 | 0.137 | 0.199 | 0.555 | 0.137 |
| 8³, −1/2 | 0.470 | 0.685 | 0.678 | 0.896 | 0.510 |
| 8³, −1 | 0.227 | 0.320 | 0.438 | 0.809 | 0.260 |

**Reading.** At large Γ the record carries its own slow clock (the adiabatic value). As Γ **falls** the record outruns its well and diffuses faster, approaching bare. This is the opposite of the expectation. It agrees with #9158's first-order result: for κ < 1 the lagging record is faster than the slaved one.

Diffusion is never faster than bare in label time (≤ 0.93), so that part of the HIT condition is not met. In internal time, with the mean-zero convention, the ring reaches 1.20 at Γ = 1 (λ = −1/2).

## Verdict

**HIT**, on the ring of 12 and all four 8³ runs:
1. In label time (the task's time), block 95's pair law does not return at Γ = 100 on the ring of 12. It goes to π95/Z(C), because Σ 1/w (not the mean clock) is conserved. In internal time it returns.
2. The record's diffusion does not slow for small Γ: it is fastest at Γ = 0.1 and slowest at large or intermediate Γ.

Both are consistent with #9158's analytic derivation. This run confirms them numerically at the task's parameters.
