# Loop factors of the pinned law — run 1

Worker `w-jonathonsmac4f50-j22fd`, model `claude-opus-5-5`. Blocks 39 and 40 were written by the same model family (Claude). The log is `logs/probes/C:pinned-loop-factors-table:a1/w-jonathonsmac4f50-j22fd__f2304df7__20260925T030312Z.*`.

## As landed on main

- **Block 40 (#8546):**
  - T2: a factor of 1 on every forest.
  - T3: the single-cycle factor `1 + 3λ₁ⁿ + 2λ₂ⁿ`. It evaluates one simple cycle and is **not** a product rule for overlapping cycles.
  - The onset table is historical, not fresh evidence.
  - The value `c₀` is proposed, not registered.
- **Block 39 (#8530):** the content-less calibration.

Accordingly, the factors of multi-cycle sets below are computed by the full content contraction.

## Method (exact)

An occupied set G with n sites and E bonds weighs `(6z)ⁿ f(G)`, where

  `f(G) = 6^{E−n} P_G(p,q,r)/(p+q+4r)^E`,  `P_G = Σ_contents p^{#equal} q^{#opposite} r^{#orthogonal}`.

`P_G` is an integer polynomial, found by enumerating all `6ⁿ` content assignments. The polynomials are printed in the log. The enumeration reproduces T3 exactly for the plaquette and the skew hexagon (PASS).

## (1) Plaquette factor `1 + 3λ₁⁴ + 2λ₂⁴`

Here `λ₁ = (p−q)/(p+q+4r)` and `λ₂ = (p+q−2r)/(p+q+4r)`. The log gives exact rationals for p = 3 … 24 on all four lines.

| p | (p,1,2) | (p,1,1) | (p,2,4) | (p,1,3) |
|---|---|---|---|---|
| 3 | 433/432 = 1.00231 | 261/256 = 1.01953 | 64882/64827 = 1.00085 * | 4101/4096 = 1.00122 * |
| 6 | 17554/16875 = 1.04024 | 17766/14641 = 1.21344 | 433/432 = 1.00231 | 132198/130321 = 1.01440 |
| 8 | 91974/83521 = 1.10121 | 40566/28561 = 1.42033 | 28806/28561 = 1.00858 | 67282/64827 = 1.03787 |
| 10 | 154806/130321 = 1.18788 | 206/125 = 1.64800 | 2451/2401 = 1.02083 | 300774/279841 = 1.07480 |
| 11 | 12387/10000 = 1.23870 | 7221/4096 = 1.76294 | | 7591/6912 = 1.09824 |
| 12 | 83842/64827 = 1.29332 | 156726/83521 = 1.87649 | 17554/16875 = 1.04024 | 17574/15625 = 1.12474 |
| 16 | 599622/390625 = 1.53503 | 5526/2401 = 2.30154 | 91974/83521 = 1.10121 | 888438/707281 = 1.25613 |
| 20 | 1265286/707281 = 1.78894 | 208446/78125 = 2.66811 | 154806/130321 = 1.18788 | 559378/395307 = 1.41505 |
| 24 | 804802/395307 = 2.03589 | 2106486/707281 = 2.97829 | 83842/64827 = 1.29332 | 2974326/1874161 = 1.58702 |

- `*` marks `p + q < 2r`: there ω is not positive semidefinite, so no scale makes the law with vacancies reflection positive.
- `(2p, 2, 4)` equals `(p, 1, 2)`: λ depends only on the ratios.
- Every line tends to 6 as p → ∞.

**Crossings (exact roots in p):**

| line | passes 1.2 at | reaches `exp(4K_c) = 2.4269` at |
|---|---|---|
| (p,1,2) | **10.2463** | 30.9519 |
| (p,1,1) | 5.8541 | 17.2963 |
| (p,2,4) | 20.4926 | 61.9039 |
| (p,1,3) | 14.4203 | 44.4680 |

**Expectation.** "The plaquette factor passes about 1.2 near p = 10 on (p,1,2)": f(10) = 1.1879 and f(11) = 1.2387, with the root at 10.246. **Confirmed.**

## (2) The smallest sets with cycles: exact factors on (p,1,2)

| p | plaquette | two plaquettes sharing an edge (rank 2) | skew hexagon around a cube corner (rank 1) | three faces at a corner (rank 3) | cube (rank 5) |
|---|---|---|---|---|---|
| 6 | 1.04024 | 1.08757 (÷f² 1.0051) | 1.00424 | 1.14913 (÷f³ 1.0209) | 1.39234 (÷f⁶ 1.0989) |
| 8 | 1.10121 | 1.23609 (1.0193) | 1.01592 | 1.44630 (1.0831) | 2.56088 (1.4361) |
| 10 | 1.18788 | 1.47168 (1.0430) | 1.03889 | 1.99409 (1.1897) | 5.64525 (2.0093) |
| 12 | 1.29332 | 1.79054 (1.0705) | 1.07436 | 2.84302 (1.3142) | 12.0616 (2.5773) |
| 16 | 1.53503 | 2.63438 (1.1180) | 1.17951 | 5.49857 (1.5202) | 40.1752 (3.0708) |
| 24 | 2.03589 | 4.80038 (1.1582) | 1.47670 | 13.9830 (1.6571) | 174.276 (2.4474) |

The log has these as exact rationals, e.g. `1315492452/893871739` for two plaquettes sharing an edge at p = 10.

**Task wording.** The "two smallest two-cycle occupied sets" are read here as:
- the domino (6 sites, 7 bonds, cycle rank 2);
- the six-cycle around a cube corner, which is a single cycle (rank 1) and equals `1 + 3λ₁⁶ + 2λ₂⁶` exactly.

Three faces at a corner and the whole cube are added.

**Reading.** Overlapping cycles do not multiply: they **reinforce**. The factor exceeds the product of its plaquette factors, by up to 2–3× for the cube.

## (3) Translating the content-less onset

- **The content-less value.** In the content-less gas a bond between records weighs y (block 40 T4: `y = c/c₀`). With `n = (1+s)/2`, `y^{n n'}` is an Ising coupling `log(y)/4` per bond. So the literature onset (density 1/2, zero field, `K_c = 0.2216544`) is `y_c = e^{4K_c} = 2.4269` **per bond**.
- **At c₀.** At `c₀` the content-less part has `y = 1`, and all binding sits on cycles.

**Comparable.** Compare the weight per site of a fully occupied region. The cubic lattice has 3 bonds and 3 plaquettes per site. So to leading order in the loop expansion (plaquette factors multiplying), a plaquette factor f matches a bond activity `y = f`. The match is at f = 2.4269, which is p = 30.95 on (p,1,2). The naive reading "four bonds per plaquette", `f = y_c⁴ = 34.7`, is never reached, because f < 6.

**Not comparable:**
1. The plaquette factors reinforce (table (2)), so the leading-order match **overstates** the p needed in a dense region.
2. A bond activity binds any two neighbours. A loop factor needs an occupied four-site ring, so at low density the loop binding is far weaker than the matching bond activity.
3. The content-less onset is condensation at density 1/2. The pinned onsets are alignment of contents together with clumping, at densities 0.1–0.7.

## (4) Executed onsets at the pinned scale

This is a fresh one-seed run of `probes/lib/moving_gas.py` on (p,1,2) at c₀, side 16, 2000 sweeps, seed 1. It is evidence only. Each cell gives recorded neighbours per record over the random value / aligned fraction (1/6 at random).

| density | p = 4 | 6 | 8 | 10 | 12 | 16 | 24 |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.99 / 0.31 | 0.99 / 0.40 | 0.99 / 0.47 | 0.99 / 0.53 | 1.00 / 0.58 | 1.02 / 0.65 | 1.02 / 0.74 |
| 0.3 | 1.01 / 0.31 | 1.02 / 0.41 | 1.04 / 0.51 | 1.09 / 0.62 | 1.39 / 0.83 | 1.71 / 0.94 | 1.84 / 0.97 |
| 0.5 | 1.01 / 0.32 | 1.03 / 0.47 | 1.19 / 0.81 | 1.27 / 0.89 | 1.32 / 0.93 | 1.35 / 0.95 | 1.36 / 0.97 |
| 0.7 | 1.01 / 0.33 | 1.05 / 0.71 | 1.09 / 0.85 | 1.10 / 0.90 | 1.10 / 0.90 | 1.10 / 0.91 | 1.09 / 0.90 |

**Agreement with the historical table.** The fresh run agrees with the historical landed table (block 40):
- above p = 16 at density 0.1;
- between 8 and 12 at 0.3 (here the jump is between 10 and 12);
- between 6 and 8 at 0.5;
- below 6 at 0.7 (here 0.71 aligned at p = 6 against 0.47 at 0.5).

**Against the loop factors.**
- At density 0.3 the onset (p ≈ 10–12) sits where the plaquette factor passes 1.2–1.3, and where the cube factor is 5.6–12.
- At density 0.5 the onset (p ≈ 6–8) comes at plaquette factors of only 1.04–1.10.
- At density 0.1 no onset appears through p = 24, where the plaquette factor is 2.04.

So the executed onsets track density at least as much as the plaquette factor, and they sit far below the leading-order content-less match (p ≈ 31). This agrees with the "not comparable" items (1)–(3).

## Verdict

There is no HIT.
- The plaquette factor passes 1.2 at p = 10.246 on (p,1,2), as expected.
- Overlapping loops reinforce rather than multiply.
- The content-less onset per bond, `e^{4K_c}`, translates to a plaquette factor of 2.43 only to leading order and only in a dense region (p ≈ 31). The executed alignment onsets happen much earlier and depend on density.
