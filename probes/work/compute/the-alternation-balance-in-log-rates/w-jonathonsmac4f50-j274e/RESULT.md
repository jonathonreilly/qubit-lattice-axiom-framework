# Block 84's balance in log rates (block 89) — run 1

Worker `w-jonathonsmac4f50-j274e`, model `claude-opus-5-5`. Block 89 was written in this campaign by the same model family (Claude), so this is not a check by an independent model family. The log is `logs/probes/C:the-alternation-balance-in-log-rates:a1/w-jonathonsmac4f50-j274e__6d64750c__20260925T031204Z.*`.

## As landed on main (#8678)

- T2: the local coefficient is `6κ − 3I/2`, so the threshold is `κ = I/4`. The landed note calls these restricted quadratic signs, with higher order needed at equality.
- T3: the anisotropy zero is at `β = (χ_a + 2J)/72`.
- T4: the objective is unbounded below, with the witness `δ_w = 6 + 12√3 κ`.

Nothing below uses withdrawn wording.

## Method

Zone averages use an exact one-dimensional representation:
- `√x = (1/2√π) ∫(1 − e^{−tx}) t^{−3/2} dt`
- `⟨e^{−t sin²k}⟩ = e^{−t/2} I₀(t/2)`

The integrals are evaluated by adaptive quadrature in double precision. `I` and `J` were also computed to 30 digits with mpmath.
- Derivatives are taken under the integral.
- Critical points are found by brentq on the analytic derivative.
- Cross-checks use midpoint grids `L³`, L = 32 … 256.

SciPy emits a few IntegrationWarnings at the requested 1e−13 relative tolerance. The 256³ grid reproduces the barrier at 2κ_c to all 8 printed digits.

## Constants

| quantity | value | 256³ midpoint grid |
|---|---|---|
| `I = ⟨1/√S⟩` | 0.91068810328886025104 | 0.91067252 (error falls ×4.00 per doubling) |
| `J = ⟨√S⟩` | 1.1938011214297952098 | 1.1938011222 |
| `κ_c = I/4` (three axes **and** one axis) | **0.2276720258** | 0.22766813 |
| `β_c = ⟨√A⟩''(0)/72` | **0.0593101040** | 0.0593101041 |
| landed `(χ_a + 2J)/72`, with `χ_a = 1.8827252545` the linear-rate model's second derivative | 0.0593101041 | |

**Consistency.** The landed T3 formula agrees with the direct second derivative to 1e−10.

## Beyond second order: a non-analytic term (new)

With the added gap `m²`, `(⟨√(S+m²)⟩ − J − m²I/2)/m⁴` is −0.2900, −0.2548, −0.2195, −0.1837 at m = 0.02, 0.04, 0.08, 0.16. Its slope in `log m` is 0.0508, 0.0510, 0.0516, against `1/(2π²) = 0.0507`.

- **Origin:** eight conical nodes, each contributing `−(m⁴/16π²) log(1/m)`.
- **Consequence:** the sea's gain carries `+(m⁴/2π²) log(1/m)` in the objective, which is positive for small m.
  - Three axes (`m² = 3 sinh²δ`): `F − F(0) = (6κ − 3I/2)δ² + (9/2π²)δ⁴ log(1/δ) + O(δ⁴)`.
  - One axis (`m² = sinh²δ`): the log term has coefficient `1/(2π²)`, and the analytic `−(I/6)δ⁴` overtakes it near δ ≈ 0.3.

**So for the alternation, κ_c is where δ = 0 changes stability, but not where the barrier vanishes.**

## Three axes, `F = −⟨√(S + 3 sinh²δ)⟩ + 6κδ²`

| κ/κ_c | local min near 0: δ (F − F(0)) | barrier: δ (height) | runaway crosses F(0) at δ | T4 witness |
|---|---|---|---|---|
| 0.8 | — (F < F(0) for every δ > 0) | — | — | |
| 0.9 | 0.392 (−7.9e−3) | 1.3475 (+0.0875) | 1.7072 | 10.26 |
| 0.95 | 0.2217 (−1.4e−3) | 1.5177 (+0.2286) | 1.9871 | 10.50 |
| 0.99 | 0.0760 (−3.6e−5) | 1.6281 (+0.3641) | 2.1560 | 10.69 |
| 0.999 | 0.0195 (−2.4e−7) | 1.6509 (+0.3972) | 2.1901 | 10.73 |
| 1.0 | — | **1.6534 (+0.4009)** | 2.1939 | 10.73 |
| 1.001 | — | 1.6559 (+0.4046) | 2.1976 | 10.74 |
| 1.01 | — | 1.6779 (+0.4388) | 2.2303 | 10.78 |
| 1.05 | — | 1.7694 (+0.6013) | 2.3642 | 10.97 |
| 1.1 | — | 1.8718 (+0.8280) | 2.5113 | 11.21 |
| 1.25 | — | 2.1270 (+1.6527) | 2.8672 | 11.92 |
| 1.5 | — | 2.4509 (+3.4572) | 3.3028 | 13.10 |
| 2 | — | 2.9103 (+8.4317) | 3.8984 | 15.46 |
| 3 | — | 3.5004 (+22.717) | 4.6352 | 20.20 |
| 5 | — | 4.1914 (+63.927) | 5.4693 | 29.66 |
| 10 | — | 5.0760 (+214.48) | 6.5058 | 53.32 |

**Reading.**
- Below κ_c, the alternation from uniform rates stops at a small δ, which grows as κ falls; a barrier still separates it from the runaway.
- At κ_c the barrier stands at δ = 1.65 with height 0.40.
- **Grid check (2κ_c, 256³):** barrier at 2.910320 with height +8.43168321, and crossing at 3.898355, identical to the exact representation.

## One axis, `F = −⟨√(S + sinh²δ)⟩ + 2κδ²`

| κ/κ_c | local min | barrier: δ (height) | crosses F(0) at δ |
|---|---|---|---|
| 0.8, 0.9, 0.95, 0.99 | — (F < F(0) for every δ > 0) | — | — |
| 0.999 | 0.0553 (−5.8e−7) | 0.2380 (+2.4e−5) | 0.3000 |
| 1.0 | — | **0.2606 (+5.3e−5)** | 0.3366 |
| 1.001 | — | 0.2788 (+8.6e−5) | 0.3646 |
| 1.01 | — | 0.3804 (+5.5e−4) | 0.5137 |
| 1.05 | — | 0.5992 (+5.2e−3) | 0.8275 |
| 1.1 | — | 0.7678 (+0.0161) | 1.0689 |
| 1.25 | — | 1.1099 (+0.0785) | 1.5565 |
| 1.5 | — | 1.5018 (+0.2774) | 2.1021 |
| 2 | — | 2.0370 (+1.0107) | 2.8163 |
| 3 | — | 2.7006 (+3.6454) | 3.6638 |
| 5 | — | 3.4492 (+12.511) | 4.5866 |
| 10 | — | 4.3794 (+48.617) | 5.6969 |

**Reading.** The local threshold is the same as for three axes. The barrier at κ_c is tiny: δ = 0.26, height 5e−5. Below κ_c the small-δ minimum exists only in a very narrow window, seen at 0.999κ_c and not at 0.99κ_c.

## Anisotropy, `G = −⟨√(e^{4ε}s_x² + e^{−2ε}(s_y² + s_z²))⟩ + 36βε²`

The landscape is analytic in ε. Its third derivative is `⟨√A⟩''' = 6.93 > 0`, so the side ε > 0 is lower.

| β/β_c | ε > 0: barrier (height); crossing | ε < 0: min; barrier (height); crossing |
|---|---|---|
| 0.8 | none, G < G(0) all along | min −0.2687 (−9.6e−3); −1.9277 (+0.956); −2.5585 |
| 0.9 | none | min −0.1262 (−1.1e−3); −2.1586 (+1.852); −2.8907 |
| 0.95 | none | min −0.0621 (−1.4e−4); −2.2574 (+2.373); −3.0282 |
| 0.99 | none | min −0.0123 (−1.1e−6); −2.3306 (+2.822); −3.1285 |
| 1.0 | none | −2.3481 (+2.939); −3.1525 |
| 1.001 | below the scan (< 0.002); crosses at +0.0022 | −2.3499 (+2.951); −3.1548 |
| 1.01 | +0.0123 (+1.1e−6); +0.0185 | −2.3654 (+3.058); −3.1760 |
| 1.05 | +0.0614 (+1.3e−4); +0.0921 | −2.4320 (+3.549); −3.2660 |
| 1.1 | +0.1231 (+1.1e−3); +0.1848 | −2.5102 (+4.201); −3.3706 |
| 1.25 | +0.3101 (+0.0170); +0.4620 | −2.7173 (+6.396); −3.6436 |
| 1.5 | +0.5806 (+0.1296); +0.8320 | −2.9979 (+10.775); −4.0048 |
| 2 | +0.9153 (+0.763); +1.2696 | −3.4162 (+21.853); −4.5291 |
| 3 | +1.2783 (+3.443); +1.7358 | −3.9725 (+51.386); −5.2067 |
| 5 | +1.6648 (+13.001); +2.2173 | −4.6383 (+131.84); −5.9961 |
| 10 | +2.1358 (+52.987); +2.7837 | −5.5022 (+412.64); −6.9957 |

**Reading.** On the ε > 0 side the barrier grows from zero at β_c, as a quadratic against a cubic predicts: position ≈ `2·36(β − β_c)/(3·⟨√A⟩'''/6)`. The scan starts at |ε| = 0.002, so the small ε < 0 minimum at 0.999 and 1.0 β_c lies inside the gap.

## Verdict

There is no HIT. The landed thresholds are confirmed to 1e−10: `κ_c = I/4 = 0.2276720` and `β_c = (χ_a + 2J)/72 = 0.0593101`.

What this run adds:
- Beyond second order the alternation is non-analytic (`δ⁴ log δ` from the eight conical nodes). So its threshold is where δ = 0 changes stability, not where a barrier vanishes.
- The runaway branch crosses the uniform value at finite δ for every κ, consistent with T4 and well inside its witness.
