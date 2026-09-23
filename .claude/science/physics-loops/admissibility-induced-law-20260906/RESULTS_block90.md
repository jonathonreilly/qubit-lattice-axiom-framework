# Block 90 — results (2026-09-23)

- Runner `scripts/admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_stationary_law_one_layer_of_a_reflection_positive_bilayer_2026_09_23.py`: `TOTAL: PASS=15 FAIL=0`; 9 mutations, each in its own family (~1 s).
- T1: detailed balance with `π = Π Z(h_x)` for every pair on a ring of four (two values) and a ring of three (four six-axis contents), symbolic `t`; the level-ordered past violates the cycle criterion: ratio `t⁸` on the ring from the transition probabilities, exponent `8` on `4³` (light-cone: `0`).
- T2: the parity relabelling maps 448 (L = 4) and 1512 (L = 6) edges onto the bilayer; all 128 vectors `i^{n·x}(1, ±1)` are exact eigenvectors of the `4³` bilayer (eigenvalues `E`, `E + 2`); `E(k + π) = 12 − E`.
- T3: 13 reflections on `4³`: no fixed vertex, crossing edges mirror pairs, every edge covered; layer halves: `⟨d, Md⟩ = −64` (open cube), `−1280 = −20N` (`4³` torus).
- T4: `⟨|m₀|²⟩ ≥ 1 − (3/(2β))(G_L + H_L)`; the trace of `1/λ` over the 127 nonzero eigenvalues equals `N(G_4 + H_4)`; `β_4 = 18239/35840`, `β_6 = 27735979/51891840`.
- Control: `I₀ = 0.252731009859 = W/6`, `I₂ = 0.140931488113`, `β₀ = 0.5904937`; `β_L` from `0.5089` (L = 4) to `0.5852` (L = 64); independent simulator plateaus `0.126/0.088` (β = 0.55, L = 24/32), `0.351/0.339` (0.58), `0.415/0.416` (0.60), `0.472/0.468` (0.62), `0.529/0.523` (0.65): onset in `(0.55, 0.58)`.
