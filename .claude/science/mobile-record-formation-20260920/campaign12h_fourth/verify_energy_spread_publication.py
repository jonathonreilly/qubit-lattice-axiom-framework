"""Verify the selected first-birth energy-spread review unit."""

from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
manifest = json.loads((HERE / 'PUBLICATION_UNIT_ENERGY_SPREAD.json').read_text())
assert manifest['base_commit'] == '79ab61e5aee8945bf96924815c7e0f9dd4d256a5'
assert manifest['base_pr'] == 8865
assert manifest['claim_status'] == 'provisional review proposal; no audit verdict'
assert manifest['independent_post_result_review'] == 'not completed'

for group in ('artifacts', 'sources'):
    seen = set()
    for row in manifest[group]:
        rel = row['path']
        assert rel not in seen
        seen.add(rel)
        path = HERE / rel
        blob = path.read_bytes()
        assert len(blob) == row['bytes'], (group,rel,'bytes')
        assert hashlib.sha256(blob).hexdigest() == row['sha256'], (group,rel,'sha256')

assert len(manifest['artifacts']) == manifest['artifacts_count']
assert len(manifest['sources']) == manifest['sources_count']
assert {row['path'] for row in manifest['artifacts']} == {
    'ENERGY_SPREAD_PUBLICATION_README.md',
    'energy_spread_author/FIRST_BIRTH_ENERGY_SPREAD_ON_SEVEN_SITE_PATH.md',
    'energy_spread_author/FIRST_BIRTH_ENERGY_SPREAD_RESULTS.json',
    'energy_spread_author/FIRST_BIRTH_ENERGY_SPREAD_RUN.stdout',
    'energy_spread_author/FIRST_BIRTH_ENERGY_SPREAD_RUN.stderr',
    'energy_spread_author/FIRST_BIRTH_ENERGY_SPREAD_RUN_RECEIPT.json',
    'energy_spread_author/first_birth_energy_spread_check.py',
}
assert {row['path'] for row in manifest['sources']} == {
    'formation_capacity_author/capacity_and_dark_state_check.py',
    'formation_capacity_independent/FINITE_PATH_RESULTS.json',
    'terminal_path_author/EXACT_TERMINAL_COUNTS_ON_SEVEN_SITE_PATH.md',
}
print(json.dumps({'verified_artifacts':len(manifest['artifacts']),
                  'verified_sources':len(manifest['sources']),
                  'claim_status':manifest['claim_status']},indent=2))
