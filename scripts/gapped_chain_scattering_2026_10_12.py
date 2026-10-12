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
AUDIT_INPUT_PATHS = ['docs/GAPPED_CHAIN_SCATTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-supplied-chain-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/3b663258db4fdc8e741ac08fc9ddc62a76e5c007d4b5db5a746167f943cc7dcd.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/4bf3707aa0be3b1a6236624b11836068ed7c1ac425993616def402a2c47c8b5d.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/4da959f48fa092cefda71e87ceec09d3e810d28002b45a0f69107cc179f40340.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/65aff5f3afc2b31c2827ccd23c2a80946c4884deac8aa247e8566851dd38d72c.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/6d25a4a73238b863eff15d239183ec327bbcc8899af276a58238552e0cf97bd7.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/788eafa6746d4550d28aad68de50947be72ab0b40780c0966f23fc325f3c7e86.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/a261878c4d49c0edf1f6ef9d29d5f86b00e9cc413548fc87bb0ab7959bfbf545.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/a608404dce5778add2112fa34497499e11fb1048ecdfe2a2fd6561b696d54884.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/a61ce8753e2602a4ad4152d5d939e39d6f56e651084caba1afd3c277f03fa286.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/b60167c323cfc6589a98743a1ddf3c18533b8caf2226503bdd64e7c5f2fb0a1c.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/b7308470ca28d8d93433ac8e9377d26f7355d7ed68c3d23beae534df69d4e337.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/d3faf6e4c56249786b5be36a8c24672553a5da3c4489f2d6fbbac6ec0a012e64.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/e20461fb279f8194b7b6f9fefe597a2c607905ea42f987df2b4728f9018e7d97.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/fccd339db3cfdb53928f1430f2a7ce4d708a00a8678d50ddcde5eae1c443d8c5.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Scattering/fea7c19a5734e1c3a662981a9c08d6da318b05481c0a6802f76e2227a499c382.py']
PACKET = ".claude/science/physics-loops/toe-supplied-chain-20261012"
KEY = "Scattering"
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
    for name in ids:
        case = config['cases'][name]
        with tempfile.TemporaryDirectory(prefix='supplied_chain_'+KEY+'_') as temporary:
            folder = Path(temporary)
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
            argv += [str(output) if x == '{output}' else str(folder/x[1:]) if x.startswith('@') else x for x in case['arguments']]
            started = time.monotonic()
            timeout = False
            try:
                result = subprocess.run(argv, cwd=folder, capture_output=True,
                    stdin=subprocess.DEVNULL, timeout=case['timeout_seconds'],
                    env={**os.environ, 'PYTHONDONTWRITEBYTECODE':'1'})
                stdout, stderr, code = result.stdout, result.stderr, result.returncode
            except subprocess.TimeoutExpired as exc:
                stdout, stderr, code, timeout = exc.stdout or b'', exc.stderr or b'', 124, True
            elapsed = time.monotonic()-started
            raw_result = output.read_bytes() if case['result_mode']=='file' and output.exists() else stdout if case['result_mode']=='stdout' else b''
            envelope = {'case':name, 'argv':argv, 'cwd':str(folder),
                'resources':case['resources'], 'elapsed_seconds':elapsed,
                'timeout_seconds':case['timeout_seconds'], 'timed_out':timeout,
                'exit_code':code, 'stdout':stdout.decode(), 'stderr':stderr.decode(),
                'result_raw':raw_result.decode()}
            # Preserve the whole observed envelope before parsing or evaluating it.
            print('SCIENTIFIC_ENVELOPE '+json.dumps(envelope, ensure_ascii=False, allow_nan=False), flush=True)
            if timeout:
                return 124
            data = json.loads(raw_result)
            rows = data[case['rows_key']]
            if not rows or any(type(row[case['pass_key']]) is not bool for row in rows):
                raise RuntimeError('Original predicate schema changed')
            passed += sum(row[case['pass_key']] for row in rows)
            failed += sum(not row[case['pass_key']] for row in rows)
            codes.append(code)
    print(f'TOTAL: PASS={passed} FAIL={failed}', flush=True)
    return next((code for code in codes if code != 0), 0)


if __name__ == '__main__':
    raise SystemExit(main())
