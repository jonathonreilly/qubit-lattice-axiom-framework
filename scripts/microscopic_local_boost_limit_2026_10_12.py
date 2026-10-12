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
AUDIT_INPUT_PATHS = ['docs/MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-local-continuum-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/01b61c31938ecc34b14f1ba9f098c039fb6f8def616337e5c003b1496130f879.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/06e9a8f66b5609699e7568ab402ff71553a8016184be13485f4b62427d06c707.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/0ca19c11d0a0aee5cf39d1d1bea87ba777a0cd4791f51bf74eb995ac433c55ba.npz', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/12d88b064b19a438019526431ceafcab7d7294bebd6d7bb5d86bc1f75d0630d9.npz', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/2a2e1d6307fc1fc926aac703132b21bb0bcabdc7bbe8925fd0526ed69a99d8db.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/2e2ada1807cdc8b9deef0a017a3f3a521ca7d8f27aa821bcfb36b0be41a3a590.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/4fe10789c0a227a0621601d95c1d8064384ddfb871990c1cdb66774d350ef600.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/64c29dade3a44b0abe5c9f3aadde456cd9ec135a98b2ef95bb6bbe4de5637e71.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/6820afe8e2a28234f2b305b3733ad5a3730d77dea0310e9636592d8dd8e46994.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/73202e0581956fb5b9715b514a1938d5586d66a891d6f62292d2db9e5745d7db.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/83204c74cd695a5a5e65b5458fcf2433b6b0e9100c81cb5ef46b54028febfc95.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/9ed0e40e929d7edf3fef9b70d096df85f672b0de9e0f7547936d8f63b9f75202.npz', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/b01735fe298a27dd5e554ac10f342d6d3bb763092f1ce1eb7798329bc3f118aa.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/b62eb32bced662f9e616ea94d01e360ccb55f72021565e958c3c272abca8cbc0.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/c99aed46f388a7e8c128cff93baccbf01651db1c8da22b3a4ec547f20c3cb1c5.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/cd4b819f7eac9cdafe15ec705b0cc056bc8748f4b3d6232ab033330d8a56eff1.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/ce7974b40c3c5bacdee6200525205c8f6b1cafe42e83562eded7d3f20963667d.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/edcecdaa6e7997062bf190466ed971e87792945402b640101fe13791e9ad7bea.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/ef9f3f66e2e054a3e868f4f2c113aed7cea1b0998527d87cda4cc1d4b03974ef.py', '.claude/science/physics-loops/toe-local-continuum-20261012/runtime/MicroscopicBoost/fce65306a18258459046fd5d3353087a898533c832d18c13c3a522975d3f1b85.py']
PACKET = ".claude/science/physics-loops/toe-local-continuum-20261012"
KEY = "MicroscopicBoost"
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
