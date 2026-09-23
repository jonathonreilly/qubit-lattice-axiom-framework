"""Authenticate the selected one-link exponential-field review unit."""

from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
manifest = json.loads((HERE/'PUBLICATION_UNIT_EXPONENTIAL_FIELD.json').read_text())
assert manifest['base_pr'] == 8865
assert manifest['base_commit'] == '79ab61e5aee8945bf96924815c7e0f9dd4d256a5'
assert manifest['claim_status'] == 'conditional reviewed source proposal; no audit verdict'
assert manifest['pre_sealed_before_author_comparison'] is True

for group in ('artifacts','sources'):
    seen = set()
    for row in manifest[group]:
        rel = row['path']
        assert rel not in seen
        seen.add(rel)
        blob = (HERE/rel).read_bytes()
        assert len(blob) == row['bytes'], (group,rel,'bytes')
        assert hashlib.sha256(blob).hexdigest() == row['sha256'], (group,rel,'sha256')
    assert len(seen) == manifest[group+'_count']

artifact_paths = {row['path'] for row in manifest['artifacts']}
assert 'EXPONENTIAL_FIELD_PUBLICATION_README.md' in artifact_paths
assert 'local_field_exponential_author/ONE_LINK_EXPONENTIAL_MOMENT_BOUND.md' in artifact_paths
assert 'local_field_exponential_author/ABSOLUTE_FIELD_EXPONENTIAL_COROLLARY.md' in artifact_paths
assert 'local_field_exponential_independent/PRE_SEAL.json' in artifact_paths
assert 'local_field_exponential_independent/POST_COMPARISON_SEAL.json' in artifact_paths
assert 'local_field_exponential_review/ROOT_REVIEW.md' in artifact_paths
assert manifest['artifacts_count'] == 25 and manifest['sources_count'] == 4
print(json.dumps({'verified_artifacts':manifest['artifacts_count'],
                  'verified_sources':manifest['sources_count'],
                  'claim_status':manifest['claim_status']},indent=2))
