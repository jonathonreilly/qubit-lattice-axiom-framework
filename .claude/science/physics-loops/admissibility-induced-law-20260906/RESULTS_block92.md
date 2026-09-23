# Block 92 — results (2026-09-23)

- Runner `scripts/admissibility_rule_zero_field_bound_on_the_formation_bilayer_held_source_kernel_in_3plus1_no_memory_on_planes_2026_09_23.py`: `TOTAL: PASS=17 FAIL=0`; 7 mutations, each in its own family (~1 s).
- T1: `u(k) ≥ (M²/3)²/(βE(k) + 2/(3V))` at zero field on the bilayer (d = 2, 3): derivation identities on a symbolic configuration; the quadratic identity; the weakening `2a²N(1 − 3a)/(…) ≥ 0`; Parseval on the `4 × 4` bilayer.
- T2 (3+1): `R̂ = βu`; zero-field window `((1 − β_L/β)/3)²/(E + 2/(3βV)) ≤ R̂ ≤ 1/E` in every finite volume; floors at `β = 1`: `34421689/1284505600` (`4³`) and the `6³` value; limit `(β − β₀)²/(9β²)`.
- T3 (2+1): plane relabelling (80, 180 edges), 9 reflections, stiffness `2N E₂(k)`; `Σ_{n≠0}|n|⁻² ≥ 4H_{L/2−1}` for every even `L` from 4 to 24; `M⁴ ≤ (6π²β + 1/2)/H_{L/2−1}`; `⟨|m_0|²⟩ = M² + ⟨|N⁻¹Ŝ_−(π)|²⟩` (enumeration) `≤ M² + 3/(20βN)`.
- Control: plane plateaus `0.393 → 0.073` (β = 1), `0.809 → 0.729` (β = 2), `0.910 → 0.878` (β = 4) from side 16 to 128; 3+1 floors `0.0186 … 0.0903`, limit `1/9`; the plane bound bites at `L/2 ~ 350` (β = 0.1), `~10^25` (β = 1).
