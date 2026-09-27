# Block 189 — results (2026-09-28)

- **Runner.** `scripts/admissibility_rule_the_stretch_rules_hops_decay_exponentially_2026_09_28.py`: `TOTAL: PASS=12 FAIL=0`. Six mutations (four in families A–D, two in G), each failing in its own family only.
- **T1.** The rule is `M = E − e sin E`, with `M = 2k`, `E = 2k₀` and `e = 1 − ℓ²`. The slope of the squared energy has hops `(2/(ne)) J_n(ne)`, checked through `e⁷`.
- **T2.** The fold gives the decay rate `κ = arccosh(1/|e|) − √(1 − e²)`.
- **T3.** `κ > 0` for `0 < ℓ² < 2`, and the reach is finite at `ℓ = 1`. `κ` depends only on `|1 − ℓ²|`. It behaves as `ln(2/|e|) − 1` near `ℓ = 1` and as `s³/3` near the ends, where the decay length diverges.
