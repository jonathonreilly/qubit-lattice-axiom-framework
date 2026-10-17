"""Build portable runners while preserving exact historical executions."""
from pathlib import Path
import hashlib
import json
import shutil
import textwrap

N = Path(__file__).resolve().parents[1]
W = N.parent / 'correlation_worktree'
F = W / 'outputs/autonomous_boundary_reflection_2026_10_16_inputs'
S = W / 'scripts'
source = N / 'autonomous_reflection_candidate'
review = N / 'reflection_halt_independent_check'

def pin(p):
    b = p.read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

copied = {}
for family, directory, names in [
    ('frozen_sources', source, ['CANDIDATE.md', 'CANDIDATE_V2.md', 'V2_CHANGE.md', 'FINITE_READINESS_ADDENDUM.md', 'FREEZE.json', 'FREEZE_V2.json', 'FINITE_READINESS_FREEZE.json']),
    ('author', source, ['diagnostic.py', 'DIAGNOSTIC.json']),
    ('independent_check', review, ['REVIEW.md', 'check.py', 'check_addendum.py', 'run_check.py', 'run_addendum.py', 'EXECUTION.json', 'ADDENDUM_EXECUTION.json', 'RESULTS.json', 'ADDENDUM_RESULTS.json', 'stdout.txt', 'stderr.txt', 'addendum_stdout.txt', 'addendum_stderr.txt', 'SOURCES.json', 'V2_AND_ADDENDUM_SOURCES.json']),
    ('author/execution', N / 'runs/reflection_diagnostic', ['EXECUTION.json', 'stdout', 'stderr']),
]:
    for name in names:
        dest = F / family / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(directory / name, dest)
        copied[str(dest.relative_to(F))] = pin(dest)

# The independently written implementation remains separate from the author
# implementation. Only wrapping, output routing, resource metadata and explicit
# fail-closed assertions are changed; original sources are retained above.
head = '''"""Portable independently written finite diagnostics for boundary reflection.

The original source-exposed implementation and execution receipts are preserved
under outputs/autonomous_boundary_reflection_2026_10_16_inputs/independent_check.
This adaptation returns reports to the primary runner. It is not a proof of
infinite volume or all future times. No helper registry change is needed:
the primary imports this module directly.
"""
import hashlib
import json
import math
import platform
import resource
import sys
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal, expm
from scipy.special import roots_legendre, jv
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

'''
body = (review / 'check.py').read_text()
body = body[body.index('START = time.monotonic()'):]
body = body.replace('"wall_seconds_cap": 180,', '"wall_seconds_cap": "primary runner envelope",')
body = body.replace("(ROOT/'RESULTS.json').write_text(json.dumps(RESULTS,indent=2,sort_keys=True)+'\\n')", 'return RESULTS')
anchor = 'emit("full_joint_phase_and_aging_discriminators",joint_rows)'
assert body.count(anchor) == 1
body = body.replace(anchor, anchor + '''
assert max(row["full_joint_operator_error"] for row in joint_rows) < 0.12
assert min(row["wrong_no_global_phase_error"] for row in joint_rows) > 1
assert min(row["wrong_no_old_aging_error"] for row in joint_rows) > 1
''')
addendum = (review / 'check_addendum.py').read_text()
addendum = addendum[addendum.index('start=time.monotonic()'):]
addendum = addendum.replace("'cpu_cap_seconds':60,'wall_cap_seconds':90,", "'cpu_cap_seconds':120,'wall_cap_seconds':'primary runner envelope',")
addendum = addendum.replace("(ROOT/'ADDENDUM_RESULTS.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\\n')", 'return results')
helper = head + 'def run_reflection_checks():\n' + textwrap.indent(body, '    ') + '\n\ndef run_readiness_checks():\n' + textwrap.indent(addendum, '    ')
(S / 'autonomous_boundary_reflection_check_2026_10_16.py').write_text(helper)

primary = (source / 'diagnostic.py').read_text()
primary = primary.replace('import hashlib', 'import os\nfor _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):\n    os.environ[_name] = "1"\n\nimport hashlib', 1)
primary = primary.replace('START = time.monotonic()\nHERE = pathlib.Path(__file__).resolve().parent', '''from autonomous_boundary_reflection_check_2026_10_16 import run_reflection_checks, run_readiness_checks

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/AUTONOMOUS_BOUNDARY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-16.md',
    'scripts/autonomous_boundary_reflection_check_2026_10_16.py',
    'outputs/autonomous_boundary_reflection_2026_10_16_inputs/frozen_sources/CANDIDATE_V2.md',
    'outputs/autonomous_boundary_reflection_2026_10_16_inputs/frozen_sources/FINITE_READINESS_ADDENDUM.md',
)
START = time.monotonic()
ROOT = pathlib.Path(__file__).resolve().parents[1]''')
primary = primary.replace("report = dict(status=", "independent_reflection = run_reflection_checks()\nindependent_readiness = run_readiness_checks()\n\nreport = dict(status=", 1)
primary = primary.replace("'finite author diagnostics passed; not all-future verification'", "'finite author and source-exposed checker diagnostics passed; all-future claim rests on the written proof'")
primary = primary.replace("source_sha256=hashlib.sha256((HERE/'CANDIDATE.md').read_bytes()).hexdigest()", "input_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}")
primary = primary.replace('elapsed_seconds=time.monotonic()-START)', 'independent_reflection=independent_reflection, independent_readiness=independent_readiness, elapsed_seconds=time.monotonic()-START)')
primary = primary.replace("(HERE/'DIAGNOSTIC.json').write_text", "(ROOT/'outputs/autonomous_boundary_reflection_2026_10_16.json').write_text")
primary = primary.replace("print(json.dumps(report, indent=2))", "print(json.dumps({'status': report['status'], 'author_diagnostics': results, 'sufficient_parameter_examples': resource_examples, 'input_sha256': report['input_sha256'], 'elapsed_seconds': report['elapsed_seconds']}, indent=2))")
(S / 'autonomous_boundary_reflection_2026_10_16.py').write_text(primary)
manifest = {'scope': 'Immutable historical source and execution evidence; local original paths in receipts describe historical runs, not current checkout dependencies.', 'files': copied, 'portable_adaptations': {'primary': 'Author diagnostic mathematical path retained; input identities, output path and explicit import of separately written checker added.', 'helper': 'Both separately written checker bodies wrapped as functions; output writes replaced by returns, resource metadata adjusted to primary envelope, three finite joint discriminator assertions added.'}}
(F / 'ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'copied_files': len(copied), 'primary': pin(S/'autonomous_boundary_reflection_2026_10_16.py'), 'helper': pin(S/'autonomous_boundary_reflection_check_2026_10_16.py')}, indent=2))
