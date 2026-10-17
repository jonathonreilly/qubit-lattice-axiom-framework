"""Bounded, durable prelaunch recorder for one exact-arithmetic corroboration run."""
import datetime
import fractions
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent
RUN = ROOT / sys.argv[1]
RUN.mkdir(exist_ok=False)


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def pin(path):
    p = Path(path).resolve()
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


def durable_json(path, value):
    with path.open('x') as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())


checker = ROOT / 'check_preparation.py'
checker_copy = RUN / 'checker.py'
with checker_copy.open('xb') as f:
    f.write(checker.read_bytes())
    f.flush()
    os.fsync(f.fileno())
sources = json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text())
source_pins = []
for item in sources['files']:
    p = pin(ROOT / item['snapshot'])
    assert p['sha256'] == item['sha256'] and p['bytes'] == item['bytes']
    source_pins.append(p)
bindings = [pin(ROOT / x) for x in ('CANDIDATE.md', 'FREEZE.json', 'SOURCE_MANIFEST.json',
                                     'check_preparation.py', 'launch_check.py')]
bindings += source_pins
bindings += [pin(checker_copy), pin(sys.executable), pin(fractions.__file__),
             pin(json.__file__), pin(math.__file__)]
env = dict(os.environ)
env.update(PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
command = [sys.executable, '-I', '-B', str(checker_copy)]
plan = {'serialized_utc': utc(), 'command': command, 'cwd': str(RUN), 'bindings': bindings,
        'limits': {'cpu_soft_seconds': 15, 'cpu_hard_seconds': 15,
                   'external_wall_seconds': 30, 'output_file_bytes': 8 * 1024 * 1024,
                   'memory_cap': None, 'thread_environment_requested': 1},
        'scope': 'Exact fraction/Pauli identities on an abstract M=17 register, complete 4x4 pair matrices, rational scalar checks. No large matrix, thermal density, dynamics or scattering calculation.',
        'runtime_coverage': 'Interpreter plus selected standard-library files pinned, not the entire runtime or operating system. Thread count requested, not measured.',
        'independence': 'Root authored both candidate and this checker before seeing the separately assigned preparation derivation; this is corroboration, not independent review.'}
plan_path = RUN / 'PRELAUNCH.json'
durable_json(plan_path, plan)
directory_fd = os.open(RUN, os.O_RDONLY)
os.fsync(directory_fd)
os.close(directory_fd)
plan_pin = pin(plan_path)


def caps():
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    resource.setrlimit(resource.RLIMIT_FSIZE, (8 * 1024 * 1024, 8 * 1024 * 1024))


start, before = utc(), time.monotonic()
timeout = False
with (RUN / 'stdout.txt').open('xb') as out, (RUN / 'stderr.txt').open('xb') as err:
    try:
        result = subprocess.run(command, cwd=RUN, env=env, stdout=out, stderr=err,
                                timeout=30, preexec_fn=caps, check=False)
        returncode = result.returncode
    except subprocess.TimeoutExpired:
        timeout, returncode = True, 124
    for f in (out, err):
        f.flush()
        os.fsync(f.fileno())
elapsed, end = time.monotonic() - before, utc()
post = [pin(item['path']) for item in bindings]
unchanged = all(x == y for x, y in zip(bindings, post))
receipt = {'started_utc': start, 'ended_utc': end, 'elapsed_seconds': elapsed,
           'returncode': returncode, 'timeout': timeout, 'prelaunch': plan_pin,
           'all_bindings_unchanged': unchanged, 'binding_count': len(bindings),
           'stdout': pin(RUN / 'stdout.txt'), 'stderr': pin(RUN / 'stderr.txt'),
           'limits': plan['limits'], 'runtime_coverage': plan['runtime_coverage']}
durable_json(RUN / 'EXECUTION.json', receipt)
print(json.dumps(receipt, indent=2))
assert unchanged
raise SystemExit(returncode)
