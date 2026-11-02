"""Mechanical identity packaging only; no scientific or numerical experiment."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
PREFIX = ROOT / 'checks/positive_reader_covariance_'
SOURCE = ROOT / 'POSITIVE_READER_COVARIANCE_ASTRA.md'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(suffix, obj):
    Path(str(PREFIX) + suffix).write_text(json.dumps(obj, indent=2) + '\n')


manifest_path = Path(str(PREFIX) + 'read_manifest.json')
manifest = json.loads(manifest_path.read_text())
inputs = []
for item in manifest['sources']:
    path = Path(item['path'])
    actual = sha(path)
    inputs.append({'path': str(path), 'expected_sha256': item['sha256'],
                   'actual_sha256': actual, 'matches': actual == item['sha256']})
protected = []
for item in manifest['protected_ps_packet']:
    path = Path(item['path'])
    actual = sha(path)
    protected.append({'path': str(path), 'expected_sha256': item['sha256'],
                      'actual_sha256': actual, 'matches': actual == item['sha256']})
links = []
for link in re.findall(r'\]\(([^)]+)\)', SOURCE.read_text()):
    if '://' in link:
        continue
    target = SOURCE.parent / link.split('#')[0]
    links.append({'target': str(target), 'exists': target.exists()})
result = {
    'role': 'mechanical identities and local links only; not proof validation',
    'source_sha256': sha(SOURCE),
    'source_line_count': len(SOURCE.read_bytes().splitlines()),
    'inputs': inputs, 'protected_ps_packet': protected, 'local_links': links,
    'all_input_identities_match': all(x['matches'] for x in inputs),
    'all_protected_ps_identities_match': all(x['matches'] for x in protected),
    'all_local_links_exist': all(x['exists'] for x in links),
    'numerical_experiments': 0,
}
dump('identity_check.json', result)
assert result['all_input_identities_match']
assert result['all_protected_ps_identities_match']
assert result['all_local_links_exist']
paths = [SOURCE, manifest_path,
         Path(str(PREFIX) + 'author_checks.md'),
         Path(str(PREFIX) + 'identity_check.json'),
         Path(str(PREFIX) + 'freeze.py')]
records = [{'path': str(p), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in paths]
receipt = {
    'schema_version': 1,
    'role': 'author freeze; independent scientific review requested and pending',
    'source_revision_context': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'source_sha256': sha(SOURCE),
    'source_line_count': len(SOURCE.read_bytes().splitlines()),
    'records': records,
    'proved_proposal': [
        'Actual finite-u full-colour lift Hessian and uniform complex principal-inverse bounds',
        'Geometry-only smooth cutoff cover with a bounded whole-torus small-volume case',
        'Exact commutator residual, separate absolute row/column and marked incidence bounds',
        'Positive complete-reader local covariance core plus symmetrized residual atoms of M_beta<=c0/16',
        'Uniform accretivity under nonnegative core weakening and modulus-one residual weakening',
        'Complete-reader monomials, exact normalized Gaussian endpoint factorization, and finite-order coefficient chain-rule bounds',
    ],
    'output_rate': 'beta=(16R)^(-4) in original coarse-block units; not an arbitrary preassigned rate; use beta/2 if reserving derivative weight',
    'open_interfaces': [
        'RD convergence support-margin compatibility',
        'New weaker Gaussian precision constant in the combined chart regulator',
        'All integrated derivative trees, hard surfaces/corners and histories',
        'Same-component reference and saddle/vacuum normalization cancellation',
        'Original-cut complex nonvanishing and full return expansion',
        'Inherited/effective history identification and multiscale control',
        'Full 4D continuum existence and positive physical continuum mass gap',
    ],
    'numerical_experiments': 0,
    'git_mutations_by_this_author': 0,
    'audit_or_lock_operations': 0,
    'independent_review_status': 'requested from coordinator; not self-assigned LAND',
}
dump('receipt.json', receipt)
receipt_path = Path(str(PREFIX) + 'receipt.json')
print(json.dumps({'source_sha256': sha(SOURCE), 'source_lines': receipt['source_line_count'],
                  'receipt_sha256': sha(receipt_path), 'packet_files_including_receipt': len(paths)+1,
                  'identity_checks_only': True}))
