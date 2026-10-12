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
AUDIT_INPUT_PATHS = ['docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/WEIGHTED_CURRENT_CLOSURE_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/GAPPED_BOOST_INVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MICROSCOPIC_BOOST_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-supplied-chain-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/02769912067e93ee1b6ff93b80eac0259da608d354f53107ef435cc11a0426ec.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/1bfd0a92426a5082d1c18b0a8b8a43ed14cde56a839de2bf6eda171a489fb3b0.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/55fd74db7787aa9eee72867e49a2ff3e44c5adb383f13985b7a2497b27bc9e5b.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/5d7504c7bbb8b03e9098fe47f1d8c07d90ac2d3fa694d54ce4acd49a3dbc843f.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/66afcfbddfd7180d1165d5e4964e734701d1ff94ba0975f97afd759ecd2e7831.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/739b3d163cb276fa45290e8ca9308d2b699fba42cb0e1406c99d0f1a2e3c8b2f.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/963cb5d3d135f89e93c61142e715e1f3d7e5831cfacf1d1b11b183c323c92f73.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/c8a9234ce2b7a8061367cbac7ba1b609acbef0befa278f20e800944721e56a1f.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/d073471ca162c2014bf2afae4faa761709fbd69a919ff3b7180c5e1ad62cd077.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Concrete/f35823dd06e25a538dcbd4cf5fc013572f4b3471695b7db0361337da6a017af6.py']
PACKET = ".claude/science/physics-loops/toe-supplied-chain-20261012"
KEY = "Concrete"
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
