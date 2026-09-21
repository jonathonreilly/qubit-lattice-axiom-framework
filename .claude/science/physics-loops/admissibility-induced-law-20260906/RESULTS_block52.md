# Block 52 — results (2026-09-21)

- Runner `scripts/admissibility_rule_a_streaming_clause_with_an_isotropic_second_order_term_content_as_a_bias_on_a_symmetric_walk_2026_09_21.py`: `TOTAL: PASS=13 FAIL=0`; eight mutations, each in its own family.
- T1: rates non-negative, total `3α`, first moment `c s`, second moment `αδ` for 150 rational unit contents; any axis-hop law with first moment `c s` has second moment `≥ c|s_k|`, equality only for forward hops; a content-independent second moment is `≥ c`.
- T2: streaming operator `= −c s·∇ + (α/2)∇²` exactly on fields of degree two.
- T3: capture `3α` per site, `α/2` per exposed face for a cube, a `2×2×1` plate and a ball; two-content witness: captured mean = gas mean `(1/5, −2/5, 0)`.
- T4: flows balanced at 1755 two-record configurations (three content pairs); not if a blocked hop does nothing.
- T5: shares against / across the content: `0, 2/3` (axis), `1/10, 1/3`, `2/9, 0`, `5/21, 0`.
- Executed (`ρ = 0.1`, `γ = 2`, eight seeds, r 6 to 10): biased walk `0.2563, 0.2531, 0.2548` (`± 0.0035`), ratio `1.006 ± 0.019` (closure `0.2653`); forward hops (block 51) `0.1754, 0.1485, 0.1304`, ratio `1.35 ± 0.03`.
