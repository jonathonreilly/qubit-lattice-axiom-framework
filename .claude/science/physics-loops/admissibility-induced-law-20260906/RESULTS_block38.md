# Block 38 — results (2026-09-20)

- Runner `scripts/admissibility_rule_how_records_form_static_law_outside_adapted_hull_clause_independence_causal_structure_2026_09_20.py`: `TOTAL: PASS=15 FAIL=0`; seven mutations, each in its own family.
- T1: the product inequality with its equality cases for every tuple (k ≤ 4, four triples); `Z < D_min` on the plaquette (20784 < 22464), the 2×3 rectangle (6000000 < 7008768) and the cube (6982520832 < 10933678080) at (3,1,2), likewise at (5,2,4), (7,3,5); `Z = D_min` on the path and the star; every order of the plaquette and the rectangle; 60 random adapted schemes on the plaquette (bound 3/832 attained, static 27/6928).
- T2: 24 readiness-gated value-dependent schemes on the diamond and the V give the product law exactly; antichain joint law = product; same-level sites of `Z³` are never neighbours.
- Control: undirected path of 3, total variation 1/72.
- Refuter: enumeration, linear program (infeasible), adversarial adapted scheme `0.0201 ± 0.0003` < bound `0.02163` < static `0.02338`, gated scheme within sampling error.
