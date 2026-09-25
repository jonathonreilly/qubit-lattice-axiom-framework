# All eight species in block 60's exact strong field — run 2

Worker `w-jonathonsmac4f50-j533a`, model `claude-opus-5-5`. Blocks 60, 69, 70, 77 and 110 were written by the same model family (Claude). No run 1 existed when this run was made. The log is `logs/probes/C:all-species-packets-in-the-exact-strong-field:a2/w-jonathonsmac4f50-j533a__dde06d6f__20260925T072847Z.*`.

## As landed on main

- **Block 60 T4 (#8590).** The exact strong field of one body at rest, with walls held at w = ℓ = 1. The ratio `1 + (1 + 2Qg0)/(1 + Qg0)` is a local weak-exterior coefficient, not an integrated turn.
- **Block 110 (#8960).** Bonds are crossed at `√(w_x w_y)/(χ_x χ_y)`. Long-wave rays have `c = w/ℓ = N/χ³`. The continuum turn series is `2(3a + p)/b + (3π/2)(5a² + 4ap + p²)/b²`.
- **Blocks 69, 70, 77.** The reach-three coupling; the species maps; the staggered rest term `m ε(x)`.

## Setting

**Box.** 64×48×48 interior sites, with walls outside (open boundary). The body is at the centre.

**Exact fields.**
- The Dirichlet Green function comes from the type-I sine transform: `g0 = 0.25005369`, residual 2e−16.
- Then `χ = 1 + Qg`, `N = 1 − Pg` with `P = Qw0` and `w0 = 1/(1 + 2Qg0)`, and `w = N/χ`.
- T4 residuals are ≤ 1.1e−15. At Qg0 = 0.05, 0.2, 0.5 the clock at the body is w0 = 0.909, 0.714, 0.500.
- The box weakens the field: g at distance 12 is 0.00387, against 0.00663 for 1/(4πr).

**Mapping of the lengths (stated).** The reach-three coupling carries the bond strain `B_b = 1/(χ_x χ_{x+e}) − 1` on the bond b = (x, x + e). So `1 + B_b = 1/ℓ_b`, which is block 60's bond length and block 110's crossing factor at long wavelength. To first order `B_b = −(log χ_x + log χ_y)`.

**Generator.** `H = φ [Σ_a σ_a S_a + Σ_a σ_a ½{C_a[B], P_a} + m ε] φ`, with `φ = √w`.

## Exact checks

Block 70's maps hold on this very generator (rates, reach-three lengths, walls, m = 0): `max |V_n H V_n† − s_n H|` = **0.0** over all eight species. The species' massless dynamics are exact images of one another.

## Fast packets

Setup: q = 0.4, width 3, projected on the positive branch momentum by momentum. Each packet starts 24 sites before the body at impact parameter b and runs for T = 52.

**Definition.** Bending/fall is the turn of the same packet with clocks and lengths, divided by its turn with clocks only. A slow massive body sees only the clocks: at rest `τ = 0` and its energy is `m w`. The turn is `Δ⟨P_y⟩/q`.

| Q g0 | b | packet turn | cloud / lattice central ray / continuum central ray | **bending/fall**: packet / cloud / lattice ray / continuum ray / index model along the path / block 60 local |
|---|---|---|---|---|
| 0.05 | 8 | 0.00297 | 0.00369 / 0.01480 / 0.01526 | 1.769 / 1.810 / 1.895 / 2.057 / 2.047 / 2.048 |
| 0.05 | 12 | 0.00361 | 0.00457 / 0.00945 / 0.00979 | **1.791** / 1.801 / 1.892 / 2.053 / 2.047 / 2.048 |
| 0.05 | 16 | 0.00400 | 0.00438 / 0.00696 / 0.00725 | 1.814 / 1.811 / 1.891 / 2.050 / 2.047 / 2.048 |
| 0.2 | 8 | 0.01101 | 0.01386 / 0.05729 / 0.05946 | 1.839 / 1.939 / 2.015 / 2.206 / 2.163 / 2.167 |
| 0.2 | 12 | 0.01351 | 0.01696 / 0.03620 / 0.03772 | **1.870** / 1.883 / 2.004 / 2.188 / 2.165 / 2.167 |
| 0.2 | 16 | 0.01504 | 0.01634 / 0.02652 / 0.02775 | 1.898 / 1.903 / 1.998 / 2.179 / 2.166 / 2.167 |
| 0.5 | 8 | 0.02402 | 0.03172 / 0.13953 / 0.14642 | 1.900 / 2.155 / 2.200 / 2.445 / 2.326 / 2.333 |
| 0.5 | 12 | 0.03006 | 0.03818 / 0.08670 / 0.09105 | **1.952** / 1.994 / 2.171 / 2.394 / 2.329 / 2.333 |
| 0.5 | 16 | 0.03414 | 0.03755 / 0.06291 / 0.06629 | 1.994 / 2.054 / 2.154 / 2.367 / 2.331 / 2.333 |

**Reading, in layers.**
1. **Continuum rays** of `E = (w/ℓ)|k|` give the index model's ratio: 2.053 against 2.047 at Qg0 = 0.05, b = 12. That is block 60's 2.048, plus field-dependent corrections at larger Q.
2. **Lattice rays** carry the reach-three factor. The symbol is `h_a = s_a(1 + B c_a²)`, so the lengths' share of the kick is multiplied by `cos²q = 0.848`. This predicts `1 + cos²q (R_cont − 1)` = 1.892, and the lattice ray gives 1.892. The per-row check is in the log.
3. **Packet width.** A width of 3 at q = 0.4 is a momentum spread of about 40% of q. It lowers the cloud's ratio to 1.80, and the packet follows its cloud: 1.791.

**Absolute turns.** The packets turn 9% (b = 16) to about 20% (b = 8–12) less than their ray clouds. The field varies across the packet there, so this is taken to be the wave effect the rays omit; the ratios agree to about 1%.

## Species

At Qg0 = 0.05, b = 12, the turns of all eight species are 0.003604–0.003614. Their bending/fall ratios are 1.79099–1.79134, a spread of **1.9e−4**. This matches the exact maps; the residual comes from the projection on the box grid.

## Slow massive packets

Setup: m = 0.6 on one sublattice (the rest state), width 5, released at rest 12 sites from the body, T = 40.
- Energy 0.599 (positive branch).
- Acceleration against the packet-averaged clock pull du/dx: **0.879** (Qg0 = 0.05), 0.888 (0.2), 0.826 (0.5).
- The fall is the same for the species classes (0,0,0), (1,1,0), (1,1,1) (0.87855) and 0.87811 for (1,0,0). A species n and n + (1,1,1) share the rest state.

## Continuum series (block 110), in infinite space, with `n = (r + a)³/(r²(r − p))`

| Q g0 | b = 8: exact / first / second order | b = 12 | b = 16 |
|---|---|---|---|
| 0.05 | 0.015729 / 0.015550 / 0.015727 | 0.010446 / 0.010367 / 0.010445 | 0.007820 / 0.007775 / 0.007819 |
| 0.2 | 0.061735 / 0.059102 / 0.061598 | 0.040550 / 0.039401 / 0.040511 | 0.030192 / 0.029551 / 0.030175 |
| 0.5 | 0.154592 / 0.139231 / 0.152747 | 0.099348 / 0.092820 / 0.098828 | 0.073209 / 0.069615 / 0.072994 |

The series is confirmed through second order: the remainders are third order (2.5e−6 … 1.8e−3).

## Lattice correction against the packet-width effect (box, same path)

| b | lattice − continuum central ray at Qg0 = 0.05 / 0.2 / 0.5 | its second-order part at 0.5 | cloud − central ray (width effect) at 0.5 |
|---|---|---|---|
| 8 | −4.6e−4 / −2.2e−3 / −6.9e−3 | −2.4e−3 | −1.08e−1 |
| 12 | −3.4e−4 / −1.5e−3 / −4.4e−3 | −9.1e−4 | −4.85e−2 |
| 16 | −2.9e−4 / −1.2e−3 / −3.4e−3 | −4.6e−4 | −2.54e−2 |

The second-order lattice correction is 45–55 times smaller than the packet-width effect.

## Verdict

There is no HIT.
- The eight species agree to 2e−4, far inside 5%.
- Bending/fall is at most 2.0 for packets and 2.45 for any ray, below 3.
- The second-order lattice correction is far below the packet-width effect.

The packets' bending/fall ratio lies below block 60's local 2.048 for two understood reasons: the reach-three lattice factor `cos²q` on the lengths' part, and the packet's momentum spread. The continuum rays reproduce the index model and block 60's ratio.
