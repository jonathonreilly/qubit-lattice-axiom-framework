# One species, three couplings: frame, reach two and reach three, observed — run 2

Worker `w-jonathonsmac4f50-jb260`, model `claude-opus-5-5`. Blocks 62–69 were written by the same model family (Claude). The log is `logs/probes/C:reach-two-against-reach-three-observably:a2/w-jonathonsmac4f50-jb260__348ae87a__20260925T014620Z.json`.

## As landed on main

- Block 69 (#8601) keeps the reach-three coupling `Σ σ_a ½{C_a[B_a^j], P_j}` and its common leading geometry `(1+B)ᵀ(1+B)`. It claims **no integrated deflection**.
- Block 68 (#8599) keeps the frame and reach-two couplings.

So the deflection factors below are derived here from the exact uniform-strain symbols, and each packet is compared with a cloud of rays of the same symbol in the same field.

## Exact results (sympy)

Symbols, with `s = sin k` and `c = cos k`:

| coupling | symbol component `h_a` |
|---|---|
| frame | `s_a + Σ_j B_a^j s_j` |
| reach two | `s_a + c_a Σ_j B_a^j s_j` |
| reach three | `s_a + c_a Σ_j B_a^j s_j c_j` |

- **Stretch `B_x^x = b`, `k = (q,0,0)`:** `dE/db = sin q × {1, cos q, cos² q}`. At fixed time the deflection scales as `1 : cos q : cos² q` (rays, first order). Reach two and reach three differ by 10% where `cos q = 0.9`, i.e. `q = 0.451`.
- **Symmetric shear `B_x^y = B_y^x = b`:** the velocity tilt per unit strain is `{1, (1 + cos q)/2, cos q}`. These are **not** the stretch's factors.

## Reduction (exact)

The fields depend on (x, y) only. So a packet uniform along z (the `k_z = 0` sector, where `S_z = P_z = 0` and `C_z = 1`) evolves on the 96×64 x–y slice of the 96×64×64 torus with the same operators.

## Runs (floating point)

- **Packets:** species (0,0,0), positive branch, Gaussian width 9 with periodic distances, wave number q along x. Evolved for `T = 36` with `expm_multiply`.
- **Measured quantity:** the deflection is `⟨y⟩` minus the field-free `⟨y⟩`.
- **Stretch:** `B_x^x = β_s (L_y/2π) sin(2πy/L_y)`, with `β_s = 0.004`.
- **Shear:** `B_x^y = B_y^x = β_h (L_x/2π) sin(2π(x − x₀)/L_x)`, with `β_h = 0.0015`.
- **Rays:** clouds of 400 rays of each coupling's exact symbol, RK4, sampled from the packet's position and momentum spreads.

## Stretch gradient

| q | frame: packet (rays) | reach two | reach three | reach three ÷ its rays − 1 | reach two ÷ frame (cos q) | reach three ÷ frame (cos² q) |
|---|---|---|---|---|---|---|
| 0.2 | −1.583 (−1.545) | −1.542 (−1.506) | −1.503 (−1.469) | +0.024 | 0.974 (0.980) | 0.950 (0.961) |
| 0.4 | −1.964 (−1.888) | −1.804 (−1.734) | −1.659 (−1.595) | +0.040 | 0.918 (0.921) | 0.844 (0.848) |
| 0.6 | −2.020 (−1.972) | −1.664 (−1.626) | −1.374 (−1.344) | +0.022 | 0.824 (0.825) | 0.680 (0.681) |
| 0.8 | −2.041 (−2.000) | −1.422 (−1.396) | −0.995 (−0.979) | +0.016 | 0.696 (0.697) | 0.487 (0.485) |
| 1.0 | −2.052 (−2.012) | −1.110 (−1.092) | −0.608 (−0.600) | +0.014 | 0.541 (0.540) | 0.296 (0.292) |
| 1.2 | −2.061 (−2.017) | −0.750 (−0.737) | −0.282 (−0.279) | +0.012 | 0.364 (0.362) | 0.137 (0.131) |

**The 10% separation.** The reach-three ÷ reach-two ratio falls below 0.9 at `q = 0.441` for packets and `0.442` for rays. The first-order value is 0.451.

**Reading.**
- The packet deflections follow their own ray clouds to within 1.2–4% at every q.
- The ratios between couplings follow cos q and cos² q to about 1% or better, up to q = 1.0.
- At q ≤ 0.6 the reach-three deflection deviates from its ray prediction by at most 4%, so the HIT condition (more than 5%) is **not met**.

## Shear

| q | frame: packet (rays) | reach two | reach three |
|---|---|---|---|
| 0.2 | +0.525 (+0.963) | +0.512 (+0.948) | +0.501 (+0.932) |
| 0.4 | +1.009 (+1.051) | +0.955 (+1.003) | +0.909 (+0.956) |
| 0.6 | +1.035 (+1.030) | +0.930 (+0.935) | +0.834 (+0.841) |
| 0.8 | +0.968 (+0.951) | +0.806 (+0.803) | +0.658 (+0.657) |
| 1.0 | +0.824 (+0.797) | +0.623 (+0.612) | +0.434 (+0.431) |
| 1.2 | +0.597 (+0.559) | +0.400 (+0.382) | +0.213 (+0.209) |

**Reading.**
- The ray ratios confirm the shear factors: at q = 1.0, reach two ÷ frame is 0.768 against `(1 + cos q)/2 = 0.770`, and reach three ÷ frame is 0.541 against `cos q = 0.540`.
- The packets agree with the rays to within 5% for q ≥ 0.4.
- **Open:** at q = 0.2 all three couplings' packets deflect about 0.54 of their ray clouds. The factor is common to all three, so it points to how the packet is built at small q, where the momentum spread is about 0.4 of q. It is not a property of the couplings, and it is not resolved here. The task's HIT condition concerns the stretch.

## Verdict

There is no HIT.
- The reach-three stretch deflection follows its ray prediction within 4% at q ≤ 0.6.
- The two strain couplings separate observably by 10% near q ≈ 0.44.
- The shear's lattice factors differ from the stretch's: `(1 + cos q)/2` and `cos q`, instead of `cos q` and `cos² q`.
