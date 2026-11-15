#!/usr/bin/env python3
"""Exact checks of external proof implications; not Wilson-model simulations."""
from fractions import Fraction as F
import json

checks = []
def check(name, value, detail):
    checks.append({'name': name, 'passed': bool(value), 'detail': detail})

T = (F(1), F(1, 2))
Tp = (F(1), F(99, 100))
check('both_transfers_positive_contractions', all(0 < x <= 1 for x in T + Tp),
      'Diagonal entries: (1,1/2), (1,99/100).')
check('same_unique_vacuum', T[0] == Tp[0] == 1 and T[1] < 1 and Tp[1] < 1,
      'The first coordinate is the unique eigenvector at eigenvalue one.')
check('printed_lower_comparison_holds', all(y >= x for x, y in zip(T, Tp)),
      'Pi=I, R=0, epsilon=0; Tprime >= T in operator order.')
check('claimed_upper_comparison_is_falsified', Tp[1] > T[1],
      'The nonvacuum quadratic form exceeds the asserted upper bound by 49/100.')
check('correct_upper_comparison_rejects_fixture', not all(y <= x for x, y in zip(T, Tp)),
      'Negative control: replacing the premise by Tprime <= T rejects this example.')
check('contraction_gap_shrinks_despite_zero_lower_defect', 1-Tp[1] < 1-T[1],
      'The transfer contraction gap falls from 1/2 to 1/100.')
initial_gap, series_sum = F(1), F(2)
check('summable_is_not_small_budget', initial_gap-series_sum < 0,
      'epsilon_k=2^(-k), k>=0, has sum two, larger than initial gap one.')
ratios = [(F(1, 2**k)/F(1, 2**(k+1))) for k in range(20)]
check('spacing_rescaling_defeats_unweighted_summability', set(ratios) == {F(2)},
      'epsilon_k/a_(k+1)=2 for epsilon_k=2^(-k), a_(k+1)=2^(-(k+1)); the infinite sum diverges.')
print(json.dumps({'arithmetic': 'fractions.Fraction', 'checks': checks,
                  'passed': sum(c['passed'] for c in checks), 'total': len(checks),
                  'scope': 'external displayed implications only; no whole-paper verdict'}, indent=2))
assert all(c['passed'] for c in checks)
