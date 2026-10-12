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
AUDIT_INPUT_PATHS = ['docs/GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-supplied-chain-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-supplied-chain-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-supplied-chain-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-supplied-chain-20261012/EXTERNAL_SOURCE_INVENTORY.json', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/2a64bd05166adf7b15a7b1a06a4585523630ea539ba93b8b35888ef8f9cbf5d2.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/2f3a2af5df8c9ea466ccaf004d873442558f260c7ae4e46cac3f939ef1310854.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/5bc8c41f8e46eed6b9f8adb382162cb1cfa274b02d3f3f481a3227cbbc4801ce.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/6880923b1442119696f5365a08dc2e49c3017a7825b8cfbddbcdad06cbf2c928.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/7234fec125ded2f5f047044d2085be0afd5275d4a05664b4ebf5bce7bd8c0e36.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/78c64119fad4d216f5425faacad61882cf82eacd88fbd721289e55a213dbeb5a.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/8854091b1bc56ff19dfb48d5dc2d26014bc0bc5b6f25e05d9d4dbfdc1e0a440d.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/89538b7eebe5e1c67e9aedfcc907d58489c0578e82fca9de5f90f717a2b8f60a.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/a438ff30f6218b3c5bade34bae91e7e918bfa4c94107f630455ff422554299b9.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/ab3f50ed00d756347c6d61a0476a30eb4f0e92a0461f15c0013766695bd4cf40.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/deea79b1dd37a89a60780f9235570b092aee39b774d7de06200d0af4037eca4d.py', '.claude/science/physics-loops/toe-supplied-chain-20261012/runtime/Continuum/f774aa95b6b894037d3d1eb12509cdba47722389a16c31ec0f8ec929cbd6fb4b.py']
PACKET = ".claude/science/physics-loops/toe-supplied-chain-20261012"
KEY = "Continuum"
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
