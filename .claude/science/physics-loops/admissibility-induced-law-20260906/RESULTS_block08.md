# RESULTS — block 08: the three-dimensional formation law of the monotone class (2026-09-15)

**Deliverables (branch `physics-loop/admissibility-induced-law-block08-z3-formation-law-20260915`, cut from main `5deabeb698`):** the note `docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md`; the runner `scripts/admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15.py` (33 checks, 26 mutations, exact arithmetic, about 27 s); the pinned cache; the controls `specs/supervisor_control_block08_z3.py`, `_b.py`, `_refuter.py` with outputs; `GOAL_block08.md`; `CHECKER_block08_findings.md`; this record.

## Result, in one paragraph

For the six-axis product rule under the records-only reading, the monotone class on a box of `Z^3` is one formation law with the product form `(1/6) Π K / Π K_2 / Π K_3`, whose three-body normalizer `K_3` is irreducible (third difference `2160/2197` at (3,1,2)). The first plane of a box cannot be summed out: this is equivalent to the plane transfer preserving the two-dimensional law, which fails on the `2×2` cross-section on all 1296 states (TV `356696849/806187919680` at (3,1,2)), hence on every larger cross-section; the successor triple of a site is never a predecessor triple, so the two-dimensional telescoping has no analogue. The sweep of planes is a strictly positive Markov chain with a unique stationary law per cross-section; its boundary planes carry the two-dimensional law; the stationary `2×2` law is exact (32 orbits) and differs from the two-dimensional law by `0.000454716…`. With `c = max(c_1, c_2, c_3)` the one-neighbor sensitivity, the causal coupling gives `|Cov| ≤ 4‖g‖‖h‖(3c)^{⌈|x−y|_1/2⌉−1}`, mixing at rate `c/(1−2c)` uniformly in the cross-section, and for `c < 1/3` the unique translation-invariant law on `Z^3` to which every box law converges. `c = 27/110, 10650/63407, 5782/30885` at the three silent triples: inside. Corollary at scope: no long-range record two-point function under the monotone formation law in the region.

## Certificate

- Runner: `TOTAL: PASS=33 FAIL=0`; 26 mutations, each failing in exactly its family (census at the final sha, see REVIEW_HISTORY.md); stdout 5887 characters; no floating-point literal or conversion call in the source (F3); classical names only under Prior art and Imports (F4).
- Refuting pass (supervisor, disjoint machinery): five load-bearing numbers recomputed by different routes, all equal (`CHECKER_block08_findings.md`); three drafting defects found and fixed before the census.
- Claim type `bounded_theorem`; surface status `bounded-support`; trace `upstream_support`; audit required before any retained status.

## What is proved versus executed

| statement | proved | executed |
|---|---|---|
| Q1a–e (one law; covariance; axis symmetry; down-sets; product form) | every box, every positive symmetric rule | the cube (48 extensions; marginals; the `x_3 = 0` down-set); the `1×2×2`, `2×2×1` product forms; 2000 sampled cube configurations |
| Q1f (three-body irreducibility) | the criterion | the ratio at (3,1,2), (5,2,4); the constant control |
| Q2a, c, e (reduction; one cross-section refutes all; the mechanism lemma) | yes | — |
| Q2b (2D translate consistency) | re-proved from P7(a) | the `2×3` rectangle |
| Q2d (the refutation) | — | all 1296 states at (3,1,2), (5,2,4); the constant control; the pair facts |
| Q3a–d (contraction; column law; boundary planes; quadrant column) | every finite cross-section, every positive rule | positivity and row sums of `P_{C_2}`; the coordinate-line pairs under `π_{C_2}` |
| Q3e (the stationary `2×2` law) | — | 32 orbits; representative independence; exact solve; TV and the interior pair |
| Q4a–c (influence; covariance; sweep rate) | every box and column | the cube influence vs `6c^3`; the `2×3` influence vs `3c^3`; the sector contraction vs `θ^n` |
| Q4d–e (full cross-section; `Z^3` law; convergence of box laws) | for `c < 1/3` | region membership at eight triples |
| Q5 (decay of two-point functions) | corollary in the region | the cube's pairs (bound not informative at cube distances, stated) |

## Not claimed

Anything about the static law of `Z^3` at the silent triples; anything for `c ≥ 1/3` beyond the finite-box bounds; the distinctness of the eight corner laws on `Z^3`; a physical order or corner; the region's boundary in `(p, q, r)`; a proof of Q2d at every nonconstant triple.
