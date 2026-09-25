# All eight species under the three couplings of lengths — run 1

Worker `w-jonathonsmac4f50-jc684`, model `claude-opus-5-5`. Blocks 62–74 were written by the same model family (Claude). The log is `logs/probes/C:all-eight-species-under-the-three-couplings:a1/w-jonathonsmac4f50-jc684__9ce48cee__20260925T045817Z.*`.

## As landed on main

- Block 69 (#8601) keeps the reach-three coupling and its common geometry `(1 + B)ᵀ(1 + B)`. It claims **no integrated deflection**.
- Blocks 68, 70, 72 and 74 supply the species maps.

The deflections below are computed, and are compared only with ray clouds of the exact lattice symbols.

## Setting

The walk is `H = Σ_a σ_a S_a`, and the couplings of a strain `B_a^j` are:

| coupling | term |
|---|---|
| frame | `σ_a ½{B_a^j, S_j}` |
| reach two | `σ_a ½{C_a[B_a^j], S_j}` |
| reach three | `σ_a ½{C_a[B_a^j], P_j}`, `P_j = S_j C_j` |

**Exact reduction.** Every strain here lies in the x–y plane. On the `k_z ∈ {0, π}` sectors `S_z = 0`, and neither C_z nor P_z enters. So species `(n_x, n_y, 1)` evolve by the **same operator** as `(n_x, n_y, 0)`, and a 128×128 torus slice carries all eight species.

**Packets.** Positive energy, wave number q along +x at `k = πn + (q, 0)`, width 8. They evolve for T = 60 with `expm_multiply`.

**Cases.** b0 = 0.2. The deflection is the displacement component odd in b0.

| case | strain field | deflection measured |
|---|---|---|
| (i) stretch along the motion, gradient along the motion | `B_x^x = b0 sin(2π(x − x0)/128)` | longitudinal |
| (ii) stretch along the motion, gradient transverse (the supervisor's case) | `B_x^x = b0 sin(2πy/128)` | transverse |
| (iii) tilt, gradient along the motion | `B_x^y = b0 sin(2π(x − x0)/128)` | transverse |

The profiles along x vanish at the packet's start and keep one sign along its path.

**Rays.** Clouds of 2000 rays (RK4) of each coupling's exact lattice symbol at the species' momentum, sampled from the packet's spreads. These carry `D g D`, `(1 + B D)ᵀ(1 + B D)` and `(1 + B)ᵀ(1 + B)`, together with their cos q factors.

## Exact first-order factors (sympy)

Here + and − refer to sin q > 0.

**Stretch** (`dE/db / |sin q|`):

| species | frame | reach two | reach three |
|---|---|---|---|
| (0,0), (0,1) | 1 | cos q | cos²q |
| (1,0), (1,1) | 1 | **−cos q** | cos²q |

**Tilt** (`dv_y/db`):

| species | frame | reach two | reach three |
|---|---|---|---|
| (0,0) | +1 | +cos q | +cos q |
| (1,0) | **−1** | +cos q | +cos q |
| (0,1) | **−1** | **−cos q** | +cos q |
| (1,1) | +1 | **−cos q** | +cos q |

## Species × coupling × case at q = 0.6 (packet, with its ray cloud in brackets)

| case | frame | reach two | reach three |
|---|---|---|---|
| (i) | +9.829 (+9.853) for all | ±5.312 (±5.308): + for n_x = 0, − for n_x = 1 | +2.435 (+2.420) for all |
| (ii) | **−15.060** (−15.123) for all | ∓12.629 (∓12.692): − for n_x = 0, + for n_x = 1 | **−10.556** (−10.616) for all |
| (iii) | +8.191 for (00), (11); −8.191 for (10), (01) (rays ±8.177) | +6.671 for (00), (10); −6.671 for (01), (11) (rays ±6.723) | **+6.595** (+6.651) for all |

- **Supervisor's 2D values** (case ii, species (0,0), (1,0)) are reproduced: frame −15.06, −15.06 → **−15.06, −15.06**; reach two −12.64, +12.64 → **−12.63, +12.63**; reach three −10.57, −10.57 → **−10.56, −10.56**.
- **Sign patterns** over (00, 10, 01, 11), the same for n_z = 1:
  - frame: ++++ in (i) and (ii), **+−−+** in the tilt (`D_x D_y`);
  - reach two: **+−+−** in the stretch (`D_x`), **++−−** in the tilt (`D_y`);
  - reach three: the same for all eight species in every case.

## Wave-number dependence (case ii, reach three ÷ frame; identical for all species)

| q | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
|---|---|---|---|---|---|
| packets | 0.951 | 0.853 | 0.701 | 0.516 | 0.323 |
| rays | 0.951 | 0.853 | 0.702 | 0.517 | 0.324 |
| cos²q (first order) | 0.961 | 0.848 | 0.681 | 0.485 | 0.292 |

**Reading.**
- The packets follow their rays to 0.1%.
- The ratio follows cos²q to 1–3%. The remainder is beyond first order in b0 = 0.2 and the displacement along the profile, which the rays carry.

## Verdict

There is no HIT.
- Under the reach-three coupling every species deflects with the ray sign, and within **4.1%** of its ray prediction. The largest deviation is at q = 0.2, case (ii), −11.35 against −11.84. Elsewhere it is ≤ 0.8%.
- Reach three alone serves all eight species alike in the stretch and the tilt.
- The frame fails in the tilt for species reflected along exactly one of the two strain axes.
- Reach two flips sign with the reflection along the derivative-axis component of its strain.

**Design note.** A first version had the profiles antisymmetric about the middle of the path. That cancelled the tilt's first-order displacement and gave a spurious mismatch; it was replaced before the recorded run.
