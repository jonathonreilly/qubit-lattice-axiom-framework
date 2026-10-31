"""Replay LIB1's known survivor and check the narrow full-norm repair.

Executions are sequential, resource-gated, and isolated from old receipts.
This is coordinator evidence for B1, not an independent scientific review.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import tempfile

C = Path(__file__).resolve().parent
ROOT = C.parents[5]
original = (C / 'lib1_norm_control_original.py').read_text()
fixed = (C / 'lib1_check.py').read_text()
old_call = 'output_full = norm(grouped, out_labels, allv, allv, 1)'
new_call = 'return norm(grouped, out_labels, allv, allv, 1)'
assert original.count(old_call) == 1
assert fixed.count(new_call) == 1
cases = [
    ('original_active_for_full', original.replace(old_call, 'output_full = norm(grouped, out_labels, lam, lam, 1)'), 0, None),
    ('corrected_baseline', fixed, 0, None),
    ('active_for_full', fixed.replace(new_call, 'return norm(grouped, out_labels, lam, lam, 1)'), 1, 'exact_cycle_output_full_norm'),
    ('active_roots_only', fixed.replace(new_call, 'return norm(grouped, out_labels, lam, allv, 1)'), 1, 'exact_inactive_root_output_full_norm'),
    ('active_weight_only', fixed.replace(new_call, 'return norm(grouped, out_labels, allv, lam, 1)'), 1, 'exact_cycle_output_full_norm'),
]
env = os.environ.copy()
overrides = {key: '1' for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'PYTHONDONTWRITEBYTECODE']}
env.update(overrides)
tmp = Path(tempfile.mkdtemp(prefix='ym-lib1-norm-control-'))
rows = []


def record(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)),
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}


for name, source, expected_code, failure_name in cases:
    directory = tmp / name
    directory.mkdir()
    script = directory / 'lib1_check.py'
    script.write_text(source)
    (directory / 'lib1_criteria.md').write_bytes((C / 'lib1_criteria.md').read_bytes())
    command = ['nice', '-n', '10', sys.executable, '-B', str(script)]
    result = subprocess.run(command, cwd=directory, env=env, capture_output=True, timeout=70)
    stdout = C / ('lib1_norm_control_' + name + '_stdout.json')
    stderr = C / ('lib1_norm_control_' + name + '_stderr.txt')
    assert not stdout.exists() and not stderr.exists()
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    report = json.loads(result.stdout)
    exact_failure = report.get('reason') == ('AssertionError(' + repr(failure_name) + ')') if failure_name else 'reason' not in report
    ok = result.returncode == expected_code and exact_failure and not result.stderr
    if name == 'original_active_for_full':
        ok = ok and report['mutations']['identify_active_and_full_norms'] == 'rejected by exact witness'
    rows.append({'name': name, 'command': command, 'environment_overrides': overrides,
                 'expected_exit': expected_code, 'actual_exit': result.returncode,
                 'expected_assertion': failure_name, 'actual_reason': report.get('reason'),
                 'expected_outcome_observed': ok, 'executed_source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                 'stdout': record(stdout), 'stderr': record(stderr),
                 'predicate_counts': report['counts'], 'resource_samples': len(report['resources'])})
    print(json.dumps({'case': name, 'ok': ok, 'exit': result.returncode, 'reason': report.get('reason')}), flush=True)

out = C / 'lib1_norm_control_execution.json'
assert not out.exists()
receipt = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'scope': __doc__,
           'all_expected_outcomes': all(row['expected_outcome_observed'] for row in rows),
           'runs': rows, 'original': record(C / 'lib1_norm_control_original.py'),
           'corrected': record(C / 'lib1_check.py'), 'criteria': record(C / 'lib1_norm_control_criteria.md'),
           'original_criteria': record(C / 'lib1_criteria.md'),
           'independent_affected_review': 'PENDING', 'whole_library_rereview': False,
           'full_existence': 'OPEN', 'physical_continuum_mass_gap': 'OPEN'}
out.write_text(json.dumps(receipt, indent=2) + '\n')
assert receipt['all_expected_outcomes'], str(out)
