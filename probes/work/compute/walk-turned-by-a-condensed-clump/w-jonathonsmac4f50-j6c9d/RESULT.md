# Walk turned by a condensed clump — run 2 of 2

Worker `w-jonathonsmac4f50-j6c9d`, model `claude-opus-5-5`. Blocks 54, 95 and 98 were written by the same model family (Claude). The log is `logs/probes/C:walk-turned-by-a-condensed-clump:a2/w-jonathonsmac4f50-j6c9d__bc55a0ba__20260925T085938Z.*`. No run 1 existed when this ran.

**HIT, on the task's expectation sentence:** "first-order formula good at large b" fails at every b in the task. Even at b = 30, block 98's first-order kick is −3.15 against the walk's −0.50.

The task's HIT sentence, the walk departing from its rays, does **not** fire. The walk and the ray bundles agree to within 0.02 at every b and time, while the bundles' spreads are 0.08–0.42.

## As landed on main

- **Block 98 (#8878).**
  - T2: for the supplied continuum profile u = 6λ/(4πr), a unit-speed straight ray gets the first-order transverse kick 3λ/(πb), whose magnitude is 2|U(b)|.
  - T3: the ray law is a conditional weak-field model; "no nonlinear bending or changed-length result".
- **Block 54 (#8570).** `H_w = √W H √W`, with `H = Σ σ_a S_a`. The exact packet force is withdrawn, and T4 is a conditional ray model.
- **Block 95 (#8860).** `log w = 6 log κ Σ_r G(z − r)`, with log κ = −g and G the zero-mean kernel: a neutralized torus law.

## Set-up

- **Clump.** Block 95's gas on the 16³ torus (N = 96, g = 1, 2·10⁶ events, seed 7).
  - The dynamics is the loop body of `probes/lib/clocked_gas.py`, copied so the final positions come back.
  - The lib's own run with the same seed has a time-weighted largest-cluster share of 0.947.
  - The final state has a largest cluster of 91 of 96 records, with radius of gyration 2.39.
  - It is unwrapped and placed at the centre of an 80³ torus, whose field is `u = 6λ Σ G_80`.
  - u is −22.0 at the centre. On the line x = c it is −3.03, −1.49, −0.76, −0.35 and −0.11 at b = 10, 15, 20, 25 and 30. At the packet starts (x = c − 30) it is −0.04 to +0.25.
- **Walk.**
  - Positive branch, k0 = (0.8, 0, 0), position sd 4, starting at x = c − 30 with impact parameter b along y.
  - Evolved by expm_multiply on 2·80³ components.
  - The turn is the change of ⟨sin k_y⟩, read by FFT.
- **Rays.** `H = w(x) ε(k)`, with ε = √Σ sin²k_j, in the same field (cubic splines). There are 2000 rays per b from the packet's Wigner Gaussian, integrated by RK4 with dt = 0.05.
- **First-order kick.**
  - (a) Block 98's Σ_i 2|U(b_i)|, y-projected, for a unit-speed ray.
  - (b) (a) × tan k0, which converts it to the lattice ray (ε0 = sin k0, v = cos k0).
  - (c) The straight-line integral −(ε0/v)∫∂_y u dx of the actual lattice field along the path the free packet covers in t = 80.

## Results (floating point), change of ⟨sin k_y⟩ at t = 80

| b | walk | rays (mean, spread) | first order (a) | (b) | (c) |
|---|---|---|---|---|---|
| 10 | −0.383 | −0.367, 0.328 | −9.26 | −9.53 | −8.86 |
| 15 | −0.633 | −0.631, 0.298 | −6.14 | −6.32 | −5.31 |
| 20 | −0.728 | −0.728, 0.267 | −4.60 | −4.73 | −3.45 |
| 25 | −0.643 | −0.654, 0.334 | −3.68 | −3.78 | −2.25 |
| 30 | −0.500 | −0.501, 0.421 | −3.06 | −3.15 | −1.37 |

- **Walk against rays.** At t = 20, 40 and 60 they agree just as closely: the largest difference is 0.019, at b = 30, t = 40.
  - The packet centres agree too; at b = 30 they differ by up to 4 sites at t = 80 as the packet spreads.
  - The norm is kept to 1e−6.
- **The packets do not pass the clump.** At every b the packet centre moves forward, stops and comes back along x, and the rays do the same:
  - b = 10: x = 17.5 at t = 20, then 14.2, then 4.9, then −5.2.
  - b = 30: x = 23.2 at t = 20, then 27.7, then 25.3, then 17.7.
- **Why they come back.**
  - For motion along x, conserving `E = w ε` means a straight pass needs `w(closest)/w(start) ≥ sin k0 = 0.717`.
  - At b = 30 that ratio is `e^{−0.111 − 0.246}` = 0.70. At smaller b it is far smaller.
  - The field drives k_x past the band maximum π/2, where the x-velocity changes sign.
  - So in this set-up the clump's slow-clock zone turns back every packet of the task. The first-order kick, which assumes a weak field and a straight path, overestimates the turn by 6× (b = 30) to 25× (b = 10).
  - A constant shift of u only rescales time and E together, so the zero-mode convention does not change this.

## Weak-field control: the same field × 1/100, t = 80

| b | walk | rays (mean, spread) | (b) block 98 × tan k0 | (c) straight-line lattice integral |
|---|---|---|---|---|
| 10 | −0.0430 | −0.0375, 0.083 | −0.0953 | −0.0886 |
| 20 | −0.0332 | −0.0335, 0.043 | −0.0474 | −0.0345 |
| 30 | −0.0142 | −0.0143, 0.016 | −0.0315 | −0.0137 |

- **Walk and rays** agree in the weak field too.
- **The straight-line lattice integral (c)** matches the walk to 4 % at b = 20 and 30.
- **Block 98's continuum sum (b)** overestimates by 1.4× at b = 20 and 2.2× at b = 30. It integrates an unscreened 1/r field over an infinite line. The torus field has its constant mode removed, and the packet covers only 56 sites of the line.
- **At b = 10** the packet's width (sd 4, growing to about 8 transverse by closest approach) carries part of it past the clump's far side. That halves the mean turn relative to (c). The rays reproduce this.

## Answer

- **Does the walk follow its rays?** Yes, well inside the spreads, in both the strong and the weak field.
- **Is the first-order formula good at large b?**
  - Not for this clump at any b = 10–30. With 96 records the field along every path is strong enough to turn the packets back.
  - Where the field is weak (the ×1/100 control), the first-order kick is right once it is computed along the actual path in the actual (neutralized, periodic) field.
  - The unscreened infinite-line formula still overestimates by 1.4–2.2× at b = 20–30 in an 80³ box.
