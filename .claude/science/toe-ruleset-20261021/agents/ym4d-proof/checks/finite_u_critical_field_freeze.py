"""Identity-only packaging after the mathematical source was frozen."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
STEM = ROOT / 'checks/finite_u_critical_field_'
SOURCE = ROOT / 'FINITE_U_CRITICAL_FIELD_ASTRA.md'
EXPECTED_SOURCE = 'ecace773f964a18fe6e5c14d46d38913dc52f95afbd2c8763e4766f0c286377d'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(suffix, obj):
    Path(str(STEM) + suffix).write_text(json.dumps(obj, indent=2) + '\n')


assert sha(SOURCE) == EXPECTED_SOURCE, 'Frozen mathematical text changed'
manifest_path = Path(str(STEM) + 'read_manifest.json')
manifest = json.loads(manifest_path.read_text())
inputs = []
for item in manifest['sources']:
    path = Path(item['path'])
    actual = sha(path)
    inputs.append({'path': str(path), 'expected_sha256': item['sha256'],
                   'actual_sha256': actual, 'matches': actual == item['sha256']})
protected = []
for item in manifest['protected_ps_and_pc_packets']:
    path = Path(item['path'])
    actual = sha(path)
    protected.append({'path': str(path), 'expected_sha256': item['expected_sha256'],
                      'actual_sha256': actual, 'matches': actual == item['expected_sha256']})
links = []
for link in re.findall(r'\]\(([^)]+)\)', SOURCE.read_text()):
    if '://' in link:
        continue
    target = SOURCE.parent / link.split('#')[0]
    links.append({'target': str(target), 'exists': target.exists()})
result = {
    'role': 'mechanical identities/local-link check only; no mathematical validation',
    'source_sha256': sha(SOURCE), 'source_lines': len(SOURCE.read_bytes().splitlines()),
    'source_matches_prepackaging_freeze': sha(SOURCE) == EXPECTED_SOURCE,
    'inputs': inputs, 'protected_packets': protected, 'local_links': links,
    'all_inputs_match': all(x['matches'] for x in inputs),
    'all_protected_records_match': all(x['matches'] for x in protected),
    'all_local_links_exist': all(x['exists'] for x in links),
    'numerical_experiments': 0,
}
emit('identity_check.json', result)
assert result['all_inputs_match']
assert result['all_protected_records_match']
assert result['all_local_links_exist']
paths = [SOURCE, manifest_path,
         Path(str(STEM) + 'author_checks.md'),
         Path(str(STEM) + 'identity_check.json'),
         Path(str(STEM) + 'freeze.py')]
records = [{'path': str(p), 'sha256': sha(p), 'bytes': p.stat().st_size} for p in paths]
receipt = {
    'schema_version': 1,
    'role': 'author freeze; fresh independent mathematical review required',
    'source_revision_context': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'source_sha256': sha(SOURCE), 'source_lines': len(SOURCE.read_bytes().splitlines()),
    'mathematical_text_frozen_before_packaging': True,
    'records': records,
    'existing_results_reused': [
        'SA13 actual finite-u field for real admitted V and fixed original-source disc; no delta<=sigma p condition for its existence',
        'FR uses that same actual critical field in its narrower selected contour/integral',
        'IC12 source-free complex-coarse field on its stated domain',
        'Reviewed PC lift covariance core and reader interpolation, with used estimates rebuilt',
    ],
    'new_proposed_scope': [
        'Joint coarse/source critical-field atom contraction with actual linear source Hessian retained',
        'Local real uniqueness/positive Hessian and identification with existing branches on their common domains',
        'Small complete-reader critical-Hessian covariance tail with M_beta<=c0/16',
        'Unchanged lift PSD core, complex accretivity >=3c0/4, and explicit precision alpha_*/U_*^2',
        'Complete-reader Gaussian endpoint factorization and exact real translated-chart identity with all normalizers',
    ],
    'rate': 'beta=(16R)^(-4) in original coarse-block units; no larger arbitrary rate or unchanged RD/FR consumer match',
    'not_proved': [
        'First existence of the actual finite-u critical field (already known)',
        'A global compact minimizer or good-event typicality',
        'Stationarity of separately weakened centers/covariances for a separately weakened nonlinear phase',
        'Interacting determinant/log/reference normalization cancellation',
        'Moving-boundary complex contour and all integrated derivative trees/surfaces/histories',
        'Full original-cut return or its complex nonvanishing',
        'Inherited/effective-level identification, multiscale iteration, continuum existence, physical continuum mass gap',
    ],
    'protected_ps_pc_records': len(protected),
    'numerical_experiments': 0,
    'git_mutations_by_this_author': 0,
    'audit_ledger_lock_operations': 0,
    'independent_review_status': 'requested from coordinator; pending, no self-issued LAND',
}
emit('receipt.json', receipt)
receipt_path = Path(str(STEM) + 'receipt.json')
print(json.dumps({'source_sha256': sha(SOURCE), 'source_lines': receipt['source_lines'],
                  'receipt_sha256': sha(receipt_path), 'packet_files_including_receipt': len(paths)+1,
                  'inputs_matched': len(inputs), 'protected_records_matched': len(protected),
                  'identity_checks_only': True}))
