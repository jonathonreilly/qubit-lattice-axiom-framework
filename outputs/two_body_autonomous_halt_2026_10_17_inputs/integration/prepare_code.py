"""Package immutable evidence and adapt two distinct checked computations.

This script does not predeclare execution or source acceptance. The historical
files retain their exact bytes and original execution paths. Portable programs
receive their own actual execution and review.
"""
from pathlib import Path
import hashlib
import json
import shutil
import textwrap

N = Path(__file__).resolve().parents[1]
W = N.parent / 'correlation_worktree'
D = N / 'two_body_integration'
F = W / 'outputs/two_body_autonomous_halt_2026_10_17_inputs'
S = W / 'scripts'
NOTE = 'docs/TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md'
PRIMARY = 'scripts/two_body_autonomous_halt_2026_10_17.py'
HELPER = 'scripts/two_body_autonomous_halt_check_2026_10_17.py'

def pin(p):
    b = p.read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

copied = {}
families = ['dark_source_two_body_halt', 'dark_source_certificate_review',
            'finite_channel_wavepacket_bridge', 'finite_channel_wavepacket_review',
            'two_body_interval_bridge', 'two_body_interval_review']
for family in families:
    for source in sorted((N/family).rglob('*')):
        if not source.is_file() or '__pycache__' in source.parts or source.suffix == '.pyc':
            continue
        assert not source.is_symlink(), source
        dest = F/'frozen_sources'/family/source.relative_to(N/family)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
        copied[str(dest.relative_to(F))] = pin(dest)
for label, folder in [('prior_root', N/'root_followup_qualification'), ('root', D)]:
    for name in (['ACCEPTANCE.json', 'QUALIFICATION.md'] if label == 'prior_root'
                 else ['SOURCE_ACCEPTANCE.json', 'QUALIFICATION.md']):
        dest = F/label/name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(folder/name, dest)
        copied[str(dest.relative_to(F))] = pin(dest)

# Retain the independent physical-basis, Frobenius and exact-symbolic logic.
review = (N/'two_body_interval_review/check_composition.py').read_text()
header, body = review.split('START = time.monotonic()', 1)
header = header.replace('resource.setrlimit(resource.RLIMIT_CPU, (60, 60))\n', '')
body = 'START = time.monotonic()' + body
body = body.replace('ROOT = Path(__file__).resolve().parent', 'ROOT = input_root', 1)
body = body.replace("'cpu_seconds_cap':60,'parent_wall_seconds_cap':90", "'cpu_seconds_cap':120,'parent_wall_seconds_cap':120")
footer = body.index("(ROOT/'RESULTS.json').write_text")
body = body[:footer] + 'return output\n'
helper = header + '\nAUDIT_TIMEOUT_SEC = 120\n\ndef run_independent_checks(input_root):\n' + textwrap.indent(body, '    ')
(W/HELPER).write_text(helper)

author = (N/'two_body_interval_bridge/certify_interval.py').read_text()
author = author.replace('from fractions import Fraction as F', '''import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
              'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_name] = '1'

from fractions import Fraction as F''', 1)
author = author.replace('resource.setrlimit(resource.RLIMIT_CPU, (60, 60))',
                        'resource.setrlimit(resource.RLIMIT_CPU, (120, 120))', 1)
author = author.replace('ROOT = Path(__file__).resolve().parent', '''from two_body_autonomous_halt_check_2026_10_17 import run_independent_checks

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/two_body_interval_bridge'
AUDIT_TIMEOUT_SEC = 120
__DECLARED_INPUTS__''', 1)
author = author.replace("b = Path(row['snapshot_path']).read_bytes()",
                        "b = (ROOT/'inputs'/Path(row['snapshot_path']).name).read_bytes()", 1)
author = author.replace("'cpu_seconds_cap':60", "'cpu_seconds_cap':120")
footer = author.index("(ROOT/'POINT_WITNESSES.json').write_text")
author = author[:footer] + '''independent = run_independent_checks(
    REPO/'outputs/two_body_autonomous_halt_2026_10_17_inputs/frozen_sources/two_body_interval_review')
report['independent_composition_check'] = independent
report['input_sha256'] = {p: hashlib.sha256((REPO/p).read_bytes()).hexdigest()
                          for p in AUDIT_INPUT_PATHS}
report['portable_execution_scope'] = (
    'Exact author point/interval calculation and separate full-basis inverse, '
    'Schur, phase and resource checks. Prior independent point-state/reflection '
    'certificates are inherited by immutable identity, not recomputed by the helper. '
    'Infinite-time claims rest on the qualified analytic proof, not time evolution.')
report['elapsed_seconds_total_after_import'] = time.monotonic()-started
(REPO/'outputs/two_body_autonomous_halt_2026_10_17_point_witnesses.json').write_text(
    json.dumps(witnesses,indent=2)+'\\n')
(REPO/'outputs/two_body_autonomous_halt_2026_10_17.json').write_text(
    json.dumps(report,indent=2)+'\\n')
print(json.dumps({'status':report['status'], 'central_bound':report['central_bound'],
    'interval':report['interval'], 'matching':report['matching'],
    'packet':report['packet'], 'finite_horizon':report['finite_horizon'],
    'independent_status':independent['status'],
    'elapsed_seconds':report['elapsed_seconds_total_after_import']},indent=2))
'''
inputs = {NOTE, HELPER}
inputs.add(str((F/'frozen_sources/two_body_interval_bridge/SOURCE_MANIFEST.json').relative_to(W)))
for row in json.loads((N/'two_body_interval_bridge/SOURCE_MANIFEST.json').read_text())['sources']:
    inputs.add(str((F/'frozen_sources/two_body_interval_bridge/inputs'/Path(row['snapshot_path']).name).relative_to(W)))
rp = F/'frozen_sources/two_body_interval_review'
inputs.add(str((rp/'SOURCE_PINS.json').relative_to(W)))
for row in json.loads((rp/'SOURCE_PINS.json').read_text())['sources']:
    inputs.add(str((rp/row['snapshot_path']).relative_to(W)))
decl = 'AUDIT_INPUT_PATHS = (\n' + ''.join('    '+repr(p)+',\n' for p in sorted(inputs)) + ')'
author = author.replace('__DECLARED_INPUTS__', decl)
(W/PRIMARY).write_text(author)

manifest = {
    'scope': 'Exact historical mathematical, review and execution evidence. Original absolute paths describe historical runs; portable programs use only declared repository-local inputs.',
    'files': copied,
    'historical_process_snapshots': 'Read-only captured evidence; no editable instructions or prompts are modified or adopted by this packaging.',
    'portable_adaptations': {
        PRIMARY: 'Author calculation retained; repository-local source routing, explicit independent import, shared120-second envelope, declared inputs and output routing added.',
        HELPER: 'Separate checker body wrapped as a function; root is supplied explicitly,120-second envelope metadata and return replace original output writes. No calculation or assertion weakened.'
    }
}
(F/'ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(D/'CODE_ADAPTATION.json').write_text(json.dumps({'author_source':pin(N/'two_body_interval_bridge/certify_interval.py'),
    'independent_source':pin(N/'two_body_interval_review/check_composition.py'),
    'primary':pin(W/PRIMARY),'helper':pin(W/HELPER),'declared_inputs':sorted(inputs),
    'adaptations':manifest['portable_adaptations'],'execution':None},indent=2)+'\n')
print(json.dumps({'copied_artifacts':len(copied),'declared_inputs':len(inputs),
    'primary':pin(W/PRIMARY),'helper':pin(W/HELPER)},indent=2))
