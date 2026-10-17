"""Scientific fail-closed mutations on independent disposable copies."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

N = Path(__file__).resolve().parents[1]
W = N.parent / 'correlation_worktree'
OUT = N / 'reflection_integration/mutations'
OUT.mkdir(parents=True, exist_ok=True)
PRIMARY = 'autonomous_boundary_reflection_2026_10_16.py'
HELPER = 'autonomous_boundary_reflection_check_2026_10_16.py'
cases = [
    ('reflection_orientation', PRIMARY,
     'return -(w + J * np.exp(1j * k)) / (w + J * np.exp(-1j * k))',
     'return -(w + J * np.exp(-1j * k)) / (w + J * np.exp(1j * k))',
     'boundary_res < 2e-15'),
    ('complete_global_phase', PRIMARY,
     'wanted = np.kron(old @ R, beta[:, None])',
     'wanted = np.kron(old @ W, beta[:, None])',
     'err < 0.2'),
    ('literal_old_drift', PRIMARY,
     'K = 2 * I4 + np.kron(Z, Z)',
     'K = 2 * I4 + np.kron(Z, I2)',
     'K @ W - W @ K'),
    ('bound_state_sign', PRIMARY,
     'bound_vector = (-J / w) ** np.arange(M)',
     'bound_vector = (J / w) ** np.arange(M)',
     'residual < 1e-13'),
    ('packet_normalization', HELPER,
     'amp = sp.sqrt(15)/(4*sp.sqrt(sigma))',
     'amp = sp.sqrt(15)/(3*sp.sqrt(sigma))',
     'f2 == 1'),
    ('positive_boundary', PRIMARY,
     'boundary = w0 * number_ops[0] @ oldPm',
     'boundary = -w0 * number_ops[0] @ oldPm',
     'eigvalsh(boundary).min() > -1e-14'),
    ('sufficient_gate_schedule', PRIMARY,
     '16 * (CA + CB) ** 2 / (np.pi * np.sqrt(3) * J * eps**2)',
     '4 * (CA + CB) ** 2 / (np.pi * np.sqrt(3) * J * eps**2)',
     'budget <= eps'),
    ('finite_path_off_by_one', HELPER,
     'd=M-N+1', 'd=M-N+2',
     'assert not nonzero'),
    ('ready_cutoff_origin', HELPER,
     'cutoff=math.ceil(2*Jf*T+required)',
     'cutoff=math.ceil(required)',
     'tail<=eta_p/4'),
    ('independent_joint_phase', HELPER,
     'target=np.kron(c*old@W,beta[:,None])',
     'target=np.kron(old@W,beta[:,None])',
     'full_joint_operator_error'),
]

def pin(p):
    b = p.read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def run_case(case):
    name, filename, before, after, expected = case
    root = OUT / name
    root.mkdir(exist_ok=False)
    (root / 'scripts').mkdir()
    (root / 'outputs').mkdir()
    # Only read-only source inputs are shared; every executed script and output
    # is local to this disposable case. Historical evidence is never edited.
    (root / 'docs').symlink_to(W / 'docs', target_is_directory=True)
    (root / 'outputs/autonomous_boundary_reflection_2026_10_16_inputs').symlink_to(
        W / 'outputs/autonomous_boundary_reflection_2026_10_16_inputs', target_is_directory=True)
    for fn in (PRIMARY, HELPER):
        shutil.copyfile(W / 'scripts' / fn, root / 'scripts' / fn)
    p = root / 'scripts' / filename
    s = p.read_text()
    assert s.count(before) == 1, (name, s.count(before))
    p.write_text(s.replace(before, after))
    env = os.environ.copy()
    for var in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
        env[var] = '1'
    cmd = [sys.executable, str(root / 'scripts' / PRIMARY)]
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    tick = time.monotonic()
    proc = subprocess.run(cmd, cwd=root, env=env, capture_output=True, timeout=120)
    (root / 'stdout').write_bytes(proc.stdout)
    (root / 'stderr').write_bytes(proc.stderr)
    # A source-load failure or absent input is not scientific rejection.
    stderr = proc.stderr.decode()
    good = proc.returncode != 0 and 'AssertionError' in stderr and expected in stderr
    record = {'name': name, 'mutation_file': filename, 'before': before, 'after': after,
              'expected_rejection_site': expected, 'scientific_assertion_rejected': good,
              'started_utc': started, 'elapsed_seconds': time.monotonic()-tick,
              'argv': cmd, 'exit_code': proc.returncode, 'wall_cap_seconds':120,
              'source_files': {fn: pin(root/'scripts'/fn) for fn in (PRIMARY, HELPER)},
              'stdout': pin(root/'stdout'), 'stderr': pin(root/'stderr')}
    (root / 'EXECUTION.json').write_text(json.dumps(record, indent=2)+'\n')
    return record

baseline = {fn: pin(W/'scripts'/fn) for fn in (PRIMARY, HELPER)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(run_case, cases))
assert baseline == {fn: pin(W/'scripts'/fn) for fn in (PRIMARY, HELPER)}, 'canonical sources changed'
report = {'scope':'Finite scientific mutation sensitivity, not theorem verification or a complete fault model.',
          'canonical_sources':baseline, 'cases':records,
          'all_rejected_at_expected_scientific_assertion':all(r['scientific_assertion_rejected'] for r in records)}
(OUT/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'cases':[{'name':r['name'],'rejected':r['scientific_assertion_rejected'],'exit_code':r['exit_code']} for r in records], 'all_rejected': report['all_rejected_at_expected_scientific_assertion']},indent=2))
if not report['all_rejected_at_expected_scientific_assertion']:
    sys.exit(1)
