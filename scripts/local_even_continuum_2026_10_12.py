#!/usr/bin/env python3
"""Run complete unchanged finite controls; no expected-result data is imported.

Scientific reads are the explicitly declared original source resources and,
for recorded refinement comparisons, the original finite result payloads.
Integrity reads are RUNTIME.json and source bytes checked against its pins.
The complete observed streams and generated binary files precede evaluation.
"""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-local-continuum-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/16bf95965aa787e08cf27e2310d79d6f42906deeb1b939f614a6412b7bdce526.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/18aca21255385ffb9303b676436ef33f39d3bdd92aa4c94fa37e12a27292bf2b.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/22420585adc5ab638e2a74dd89bb7940de391181ad747a8bae560631d96c17dd.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/24e6aec6b47ff0262594ee8aa2a1736311dd93ac0493c31a9ae2996c4c1676da.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/2772f72a00ab8304879ccea6244f4bb5bb36d531e95dd7576514b63560346242.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/282ae272efc0a44d9cca6ba1af7d80ac832f929b427e54106d6a699af0ebef34.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/61c4e253c9df24c15ba1df098fdbd72a7c130055cd9d6038ca7a65a30cb84a9d.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/762906075a1967e5165fed53b037872060ff26f0441236d57a2752d0dc0e6da2.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/7b27daa596bbe29009feb101b04e409c06e86ad1127cc95f43f543eba27a2903.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/9ca0038239cc51c69ab74e2bde491e4410f7ed11d087cda414b40a1cd08d5af0.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/9cdf66ad93e91e1a460a8a763b3db1e252be38244c59b188b36382fa2e7cdf77.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/b8f0196d56d78f77fd9f563eb85312650f11788f0a052b6a8008f5f294f024f1.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/LocalEven/fc8ce286a6f8c1cc420f9bbc33c6a512640c328360fe69013b423ab2b4823e9d.py']
PACKET = ".claude/science/physics-loops/toe-local-continuum-20261012"
KEY = "LocalEven"
sys.dont_write_bytecode = True


def predicates(data, case):
    if case['rows_mode'] == 'nested_checks':
        return [c for row in data['rows'] for c in row['checks']]
    return data[case['rows_key']]


def main():
    if not __debug__ or os.environ.get('PYTHONOPTIMIZE'):
        raise RuntimeError('Original assertions must remain enabled')
    parser = argparse.ArgumentParser()
    parser.add_argument('--case')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    packet = root / PACKET
    config = json.loads((packet/'RUNTIME.json').read_bytes())[KEY]
    names = [args.case] if args.case else config['baselines']
    if len(set(names)) != len(names) or any(n not in config['cases'] for n in names):
        raise RuntimeError('Unknown or duplicated original case')
    passed = failed = 0
    codes = []
    for name in names:
        case = config['cases'][name]
        with tempfile.TemporaryDirectory(prefix='local_continuum_'+KEY+'_') as temporary:
            # Reporting helpers use Path.resolve(): use the same actual spelling.
            folder = Path(temporary).resolve()
            for relative, pin in case['resources'].items():
                data = (packet/pin['packet_path']).read_bytes()
                if len(data) != pin['bytes'] or hashlib.sha256(data).hexdigest() != pin['sha256']:
                    raise RuntimeError('Original resource identity changed: '+relative)
                destination = folder/relative
                if not destination.is_relative_to(folder):
                    raise RuntimeError('Resource escapes isolated execution')
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
            for relative in case['outputs']:
                (folder/relative).parent.mkdir(parents=True, exist_ok=True)
            argv = [sys.executable, '-B', str(folder/case['entry']), *case['arguments']]
            started = time.monotonic()
            timed_out = False
            try:
                value = subprocess.run(argv, cwd=folder, stdin=subprocess.DEVNULL,
                    capture_output=True, timeout=case['timeout_seconds'],
                    env={**os.environ, **case['environment'], 'PYTHONDONTWRITEBYTECODE':'1'})
                stdout, stderr, code = value.stdout, value.stderr, value.returncode
            except subprocess.TimeoutExpired as exc:
                stdout, stderr, code, timed_out = exc.stdout or b'', exc.stderr or b'', 124, True
            output_files = {p:base64.b64encode((folder/p).read_bytes()).decode('ascii')
                            for p in case['outputs'] if (folder/p).exists()}
            raw_result = stdout if case['result_mode'] == 'stdout' else (folder/case['result_file']).read_bytes() if (folder/case['result_file']).exists() else b''
            envelope = {'case':name, 'argv':argv, 'cwd':str(folder),
                'resources':case['resources'], 'environment':case['environment'],
                'elapsed_seconds':time.monotonic()-started, 'timeout_seconds':case['timeout_seconds'],
                'timed_out':timed_out, 'exit_code':code, 'stdout':stdout.decode(),
                'stderr':stderr.decode(), 'result_raw':raw_result.decode(),
                'output_files_base64':output_files}
            print('SCIENTIFIC_ENVELOPE '+json.dumps(envelope, ensure_ascii=False, allow_nan=False), flush=True)
            if timed_out:
                return 124
            data = json.loads(raw_result)
            rows = predicates(data, case)
            if not rows or any(type(row[case['pass_key']]) is not bool for row in rows):
                raise RuntimeError('Original predicate schema differs')
            passed += sum(row[case['pass_key']] for row in rows)
            failed += sum(not row[case['pass_key']] for row in rows)
            codes.append(code)
    print(f'TOTAL: PASS={passed} FAIL={failed}', flush=True)
    return next((c for c in codes if c != 0), 0)


if __name__ == '__main__':
    raise SystemExit(main())
