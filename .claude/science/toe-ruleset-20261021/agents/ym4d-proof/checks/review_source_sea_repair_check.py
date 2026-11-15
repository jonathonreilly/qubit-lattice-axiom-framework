#!/usr/bin/env python3
"""Affected confirmation of the additive probability/reference control repair."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json

root = Path(__file__).parent
old = json.loads((root/'source_sea_run_02.json').read_text())
new = json.loads((root/'source_sea_run_03.json').read_text())
replay = json.loads((root/'review_source_sea_author_replay_01.json').read_text())
reported = new['z2_penalty']['result']['probability_only_counterexample']
universe = {0, 1, 2, 3}
law = [(frozenset([i]), Fraction(1, 4)) for i in universe]
checked = []
for size in range(5):
    for elements in combinations(sorted(universe), size):
        event = frozenset(elements)
        mass = sum(weight for pattern, weight in law if event.issubset(pattern))
        expected = Fraction(1, 4)**size
        mask = sum(2**i for i in elements)
        row = next(r for r in reported['all_subset_moments'] if r['subset'] == mask)
        assert mass <= expected
        assert Fraction(row['moment']) == mass and Fraction(row['budget']) == expected
        checked.append(mask)
assert sorted(checked) == list(range(16))
empty_mass = sum(weight for pattern, weight in law if not pattern)
assert empty_mass == 0 and Fraction(reported['empty_reference_mass']) == 0
failures = [sum(2**i for i in pattern) for pattern, weight in law
            if weight > Fraction(1, 4)**len(pattern)*empty_mass]
assert sorted(failures) == reported['failed_reference_inequality_patterns'] == [1, 2, 4, 8]
assert reported['zero_reference_division_used'] is False
for group in ['geometry', 'su2_reflection', 'replacement_fixture', 'su2_normalizer', 'scaling_and_sources']:
    assert old[group] == new[group] == replay[group]
for key, value in old['z2_penalty']['result'].items():
    assert new['z2_penalty']['result'][key] == value
assert old == replay
hashes = {name: hashlib.sha256((root/name).read_bytes()).hexdigest() for name in
          ['source_sea_check.py', 'source_sea_check_v2.py', 'source_sea_run_02.json',
           'source_sea_run_03.json', 'source_sea_control_fix_receipt.json']}
print(json.dumps({'finding': 'SEA-CONTROL-01', 'disposition': 'resolved by additive corrected runner',
                  'all_16_subset_moments_independently_reconstructed': True,
                  'zero_empty_mass_and_four_reference_violations_without_division': True,
                  'original_frozen_author_replay_identical': True,
                  'five_other_groups_and_previous_z2_fields_identical': True,
                  'source_hashes': hashes,
                  'scope': 'generic probability-law counterexample only; the Wilson theorem uses a different tilted RP hypothesis'}, indent=2))
