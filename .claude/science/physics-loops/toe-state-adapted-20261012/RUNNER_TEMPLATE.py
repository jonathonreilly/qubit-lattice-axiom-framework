#!/usr/bin/env python3
"""Execute complete frozen author helpers; no expected-result data is imported.

The envelope retains every raw helper stream and complete result object. Its
TOTAL counts the actual helper predicates only, not independent evidence.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = __AUDIT_INPUTS__
PACKET = "__PACKET__"
KEY = "__KEY__"
if not __debug__:
    raise RuntimeError("Run without -O: original assertions must stay enabled")
sys.dont_write_bytecode = True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', help='One complete original baseline or whole-source variant')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    packet = root / PACKET
    config = json.loads((packet / 'RUNTIME.json').read_bytes())[KEY]
    ids = [args.case] if args.case else config['baselines']
    if len(ids) != len(set(ids)) or any(name not in config['cases'] for name in ids):
        raise RuntimeError('Unknown or duplicate original case')
    passed = failed = 0
    codes = []
    certificates = []
    for name in ids:
        case = config['cases'][name]
        with tempfile.TemporaryDirectory(prefix='state_adapted_'+KEY+'_') as temporary:
            folder = Path(temporary).resolve()
            for relative, pin in case['resources'].items():
                source = packet / pin['packet_path']
                data = source.read_bytes()
                if len(data) != pin['bytes'] or hashlib.sha256(data).hexdigest() != pin['sha256']:
                    raise RuntimeError('Frozen whole-helper source changed: '+relative)
                destination = folder / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
            output = folder / 'observed.result.json'
            argv = [sys.executable, '-B', str(folder/case['entry'])]
            argv += [str(output) if x == '{output}' else str((folder/x[1:]).resolve()) if x.startswith('@') else x for x in case['arguments']]
            started = time.monotonic()
            timeout = False
            try:
                result = subprocess.run(argv, cwd=folder, capture_output=True,
                    stdin=subprocess.DEVNULL, timeout=case['timeout_seconds'],
                    env={**os.environ, **case['environment_overrides']})
                stdout, stderr, code = result.stdout, result.stderr, result.returncode
            except subprocess.TimeoutExpired as exc:
                stdout, stderr, code, timeout = exc.stdout or b'', exc.stderr or b'', 124, True
            elapsed = time.monotonic()-started
            raw_result = stdout
            envelope = {'case':name, 'argv':argv, 'cwd':str(folder),
                'interpreter':sys.executable, 'python':sys.version, 'role':case['role'],
                'resources':case['resources'], 'environment_overrides':case['environment_overrides'], 'elapsed_seconds':elapsed,
                'timeout_seconds':case['timeout_seconds'], 'timed_out':timeout,
                'exit_code':code, 'stdout':stdout.decode(), 'stderr':stderr.decode(),
                'result_raw':raw_result.decode()}
            # Preserve the whole observed envelope before parsing or evaluating it.
            print('SCIENTIFIC_ENVELOPE '+json.dumps(envelope, ensure_ascii=False, allow_nan=False), flush=True)
            if timeout:
                return 124
            objects = [json.loads(line) for line in raw_result.decode().splitlines() if line.startswith('{')]
            rows = [row for row in objects if 'name' in row and 'passed' in row]
            if not rows or any(type(row['passed']) is not bool for row in rows):
                raise RuntimeError('Original predicate schema changed')
            counts = {'total':len(rows), 'passed':sum(row['passed'] for row in rows), 'failed':sum(not row['passed'] for row in rows)}
            summary = objects[-1]
            if summary.get('summary') is not True or any(summary.get(k) != v for k,v in counts.items()):
                raise RuntimeError('Original summary disagrees with actual rows')
            for relative, pin in case['resources'].items():
                if hashlib.sha256((folder/relative).read_bytes()).hexdigest() != pin['sha256']:
                    raise RuntimeError('Helper source changed during execution')
            for line in raw_result.decode().splitlines():
                if line.startswith(('per_element:', 'per_site:', 'per_mode:', 'per_block:', 'lattice_wide:')) and line not in certificates:
                    certificates.append(line)
            passed += counts['passed']
            failed += counts['failed']
            codes.append(code)
    for line in certificates:
        print(line, flush=True)
    print(f'TOTAL: PASS={passed} FAIL={failed}', flush=True)
    return next((code for code in codes if code != 0), 0)


if __name__ == '__main__':
    raise SystemExit(main())
