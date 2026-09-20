# Block 37 — results (2026-09-20)

- Runner `scripts/admissibility_rule_six_axis_formation_threshold_unit_budget_false_one_seed_witness_family_constant_ten_ninths_2026_09_20.py`: `TOTAL: PASS=14 FAIL=0`; seven mutations, each failing in its own family.
- T1: 37 one-sites in `[0,3]³` (boxes `[0,3]³` and `[−2,6]³` agree; the rule at every site of `[−1,4]³`), level sizes `1,3,3,4,3,6,7,6,3,1`, one seed, 9 amplified, 27 processed, cyclic symmetry.
- T2: exact minimum of `E − |A|` at `333` is `1` (tree `E = 6`, `|A| = 5`); of `E − (10/9)|A|` is `0` (tree `E = 10`, `|A| = 9`); positive at `1`, `109/99`, `11/10`.
- T3: rooted values of `233, 323, 332` are `0`; of `333` is `1`; largest among the other 36 sites `0`.
- Control: the integer program gives `10/9`; local search found nothing larger.
