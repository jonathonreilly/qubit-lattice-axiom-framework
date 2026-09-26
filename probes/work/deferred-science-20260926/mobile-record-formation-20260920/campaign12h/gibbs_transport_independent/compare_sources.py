#!/usr/bin/env python3
"""Post-seal source/evidence authentication; does not run author calculations."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
CAMPAIGN = HERE.parent
sha = lambda b: hashlib.sha256(b).hexdigest()
sources = []


def read(path):
    data = path.read_bytes()
    sources.append({'path': str(path), 'sha256': sha(data), 'bytes': len(data)})
    return data


pre_bytes = (HERE/'PRE_CHECKER_SEAL.json').read_bytes()
assert sha(pre_bytes) == 'a9709714b8474a7dd96f49f44135f814323094351531ed73800097a98e0f9a05'
pre = json.loads(pre_bytes)
for row in pre['artifacts']:
    data = (HERE/row['path']).read_bytes()
    assert sha(data) == row['sha256'] and len(data) == row['bytes']
corrections = CAMPAIGN/'gibbs_transport_corrections'
metadata = json.loads(read(corrections/'SOURCE_CORRECTIONS.json'))
assert metadata['pre_checker_seal_sha256'] == sha(pre_bytes)
rebuilt_diff = []
changes = []
for change in metadata['changes']:
    current_path = Path(change['path'])
    original_path = corrections/(current_path.name+'.before')
    old = read(original_path); current = read(current_path)
    expected = next(x['sha256'] for x in pre['sources'] if x['path'] == str(current_path))
    assert sha(old) == expected == change['before_sha256']
    assert sha(current) == change['after_sha256']
    before, after = old.decode(), current.decode()
    assert before.count(change['old']) == 1 and after.count(change['new']) == 1
    assert before.replace(change['old'], change['new']) == after
    assert after.replace(change['new'], change['old']).encode() == old
    rebuilt_diff += list(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                         fromfile=original_path.name, tofile=current_path.name))
    changes.append({'path': str(current_path), 'before_sha256': sha(old), 'after_sha256': sha(current),
                    'inverse_replacement_verified': True, 'old': change['old'], 'new': change['new']})
assert ''.join(rebuilt_diff).encode() == read(corrections/'CORRECTIONS.diff')

suite_specs = [
    ('local_gibbs_record_circulation_check.py', 'LOCAL_GIBBS_RECORD_CIRCULATION', 12,
     'f0c012e63355ed14f90ff7ed7e4247a521d427ceaddeffd49f84c353e2cc0037'),
    ('gibbs_transport_1d_check.py', 'GIBBS_TRANSPORT_1D', 5,
     '6eae0e4d6899e907b6c09e9a5bcc6038df13a8b2f17280ea6fa3f75b3426e34a')]
suites = []
for name, stem, expected_count, expected_hash in suite_specs:
    code = read(CAMPAIGN/name)
    result = json.loads(read(CAMPAIGN/(stem+'_RESULTS.json')))
    log = read(CAMPAIGN/(stem+'_RUN.log')).decode()
    assert sha(code) == expected_hash == result['source_sha256']
    assert len(result['checks']) == expected_count
    assert all(row['passed'] is True for row in result['checks'])
    assert log.splitlines() == ['PASS: '+row['name'] for row in result['checks']] + [f'TOTAL: {expected_count} PASS']
    suites.append({'checker': name, 'source_sha256': sha(code), 'groups_reported': expected_count,
                   'log_and_source_binding_match': True, 'execution_repeated_by_reviewer': False})
for item in sources:
    assert sha(Path(item['path']).read_bytes()) == item['sha256']
ack = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'scope': 'Narrow F1/F2 acknowledgment after the sealed independent reconstruction; author scientific checkers unchanged.',
       'pre_checker_seal_sha256': sha(pre_bytes), 'changes': changes,
       'complete_diff_matches_declared_replacements': True,
       'presealed_artifacts_unchanged': len(pre['artifacts']),
       'closed_findings': ['F1 generic nonnegative-rate wording', 'F2 fourteen-label fully occupied restriction'],
       'unresolved_findings': [], 'source_identities': sources}
(HERE/'CORRECTION_ACK.json').write_text(json.dumps(ack, indent=2, sort_keys=True)+'\n')
report = {'scope': 'Post-seal reading/comparison and source authentication; author numerical results are not counted as new independent calculations.',
          'sources': sources, 'author_suites': suites, 'complete_correction_diff_verified': True,
          'independent_presealed_control_groups': 14,
          'coverage_limits': [
              'The first author full generator uses a four-label projected-feature diagnostic and floating point; it is not a full fifteen-label cubic enumeration.',
              'The one-dimensional author rings/transfer checks use floating point; their sixteen-word certificate is symbolic.',
              'The independent controls use exact arithmetic, and the general arguments are reconstructed in the report.']}
(HERE/'SOURCE_COMPARISON.json').write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
print(json.dumps({'authenticated_author_groups': sum(x['groups_reported'] for x in suites),
                  'author_executions_repeated': 0, 'closed_findings': 2,
                  'unchanged_preseal_artifacts': len(pre['artifacts']), 'source_files': len(sources)}, indent=2))
