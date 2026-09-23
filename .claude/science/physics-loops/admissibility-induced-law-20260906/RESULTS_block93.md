# Block 93 — results (2026-09-23)

- Runner `scripts/admissibility_rule_covariance_forces_a_reversible_formation_law_three_covariant_pasts_six_neighbour_past_two_static_laws_2026_09_23.py`: `TOTAL: PASS=14 FAIL=0`; 8 mutations, each in its own family (~1 s).
- T1: 24 rotations; 2187 weightings with weights 0, 1, 2: exactly 9 invariant, all orbit-constant (`w₀`, `w₁`) and symmetric; the level-ordered past's stabiliser has order 3.
- T2: detailed balance for every pair on a ring of four (two values) and a ring of three (four six-axis contents), `t₀`, `t₁` symbolic.
- T3: copy past: one-site kernel symmetric with equal row sums, uniform stationary law; six neighbours: two disjoint cubic tori (384 and 1296 edges at L = 4, 6), slab 0 = even sites of level `t` with odd sites of level `t + 1`; all seven: rung weight `w₀`, slab weight `w₁`; thresholds on `4³`: `18239/35840` (1, 1), `2857397/10250240` (1, 2), `32773/71680` (2, 1), six neighbours `3G_4 = 1517/2560`.
- Control: `β₀ = 0.5905, 0.3174, 0.5398`, six neighbours `0.7582`; orthogonal start at `β = 1.5` on `16³`: six neighbours keep the halves orthogonal for 400 levels (cosine −0.12 … +0.02), all seven align them within ten levels (cosine 0.998).
