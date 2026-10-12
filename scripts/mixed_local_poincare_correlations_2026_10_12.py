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
AUDIT_INPUT_PATHS = ['docs/MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-local-continuum-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/1324ccfec5f9e454160a703b020f42441528b8df481a5aa22b6954d825172bae.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/203b21f53cce6f4d97893da4c7ce4bf4696d585fa53bdbae8e081e4050b65296.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/2be059ee28e19bff2f0eaecae56d063d4044a74b1fb12b018d3507ffe5ee20c4.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/31cb86a69736e2e2051ddf3a57e7fb7229a615de1a26698bf901970b58d5543c.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/583cda0650d70336bd625b3be960f748b575b0a97382bd8ee3d291663a03e8b9.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/5b7aad9adeb6b5aaf86080932b598957753eb2732c78b18ae6b0e6e0b80a5e31.json', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/744517cab4b4856050ee029cf518164241ae28a3f1b9d4e40f00b4bebce943a6.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/7beaba51bd64df0c38eb0a473fda9dbb479fa27bdaab5353252179248af924f2.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/91999282d93243c438d2a3f9a786c1f1e98d663b3296259422749405f8803c11.json', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/96b221fdfb48734d15f1355ebf8efe73f1689f99ea721ebf9a5fba227c312e8a.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/9f64fedfcd4262b32bab71652fc88ca22e53bc24d742370c6178541088694462.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/b01735fe298a27dd5e554ac10f342d6d3bb763092f1ce1eb7798329bc3f118aa.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/fe643cb4d7abb87b23594eb07348f92887e3bbe3a565cf0f76f9e16f07e1b0f1.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/Mixed/fede9f2342961fdcd9cae27e5554b8f1f21ebb80a9d8e6263e1bdeb2ee2cf7d8.py']
PACKET = ".claude/science/physics-loops/toe-local-continuum-20261012"
KEY = "Mixed"
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
