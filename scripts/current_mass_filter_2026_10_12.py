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
AUDIT_INPUT_PATHS = ['docs/CURRENT_MASS_FILTER_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/GAPPED_CHAIN_SCATTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-current-mass-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-current-mass-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-current-mass-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-current-mass-20261012/EXTERNAL_SOURCE_INVENTORY.json', '.claude/science/physics-loops/toe-current-mass-20261012/AUTHOR_EVIDENCE_README.md', '.claude/science/physics-loops/toe-current-mass-20261012/formal/MassThreshold.lean', '.claude/science/physics-loops/toe-current-mass-20261012/formal/MissingEnergySign.lean', '.claude/science/physics-loops/toe-current-mass-20261012/formal/MissingCrossTerms.lean', '.claude/science/physics-loops/toe-current-mass-20261012/formal/FalseControls.lean', '.claude/science/physics-loops/toe-current-mass-20261012/formal/README.md', '.claude/science/physics-loops/toe-current-mass-20261012/formal/SEAL.json', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/08c576193c06809331caa71657f9376f9c733c4e562b0de6b37577f8a73e7560.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/37aec0d0579e9d262ee9ac88e064ab601157e6434980c18497471f5f4e9d3e3f.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/45370c5d495b50eb0dbdd7bbec603117ab3d9692389e876618a99c4dfaecf327.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/5750ea9ee1ce771d06582697daabbe1695809369ef41d74802afb84ba688f0d1.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/6296e5cb5c78ed4ed3fe55a3a2542db19b35f8f3037591e71e9d09b90a02f947.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/65a13777ab07ae2aa2842a20a801447f8fe655d54a22bd3a9d90ad93158ec0b9.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/6832091c0d3f3a979ab7c10574c43386bd2491f9ab8547466757c4d581e0ed29.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/a4b5ee72b6f1fabb4b7dae4378a1424d30a4ec7c4efdfd343570e83eadc15123.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/caa66c6b28267a5a10e360c56b72ba8ef4d64e69397ed950e8d0fa0d594467a6.py', '.claude/science/physics-loops/toe-current-mass-20261012/runtime/dfdefccc86d7b58eccfd3a6e8d44f204bd382eaaf5e21df2831097add4e1e3d0.py']
PACKET = ".claude/science/physics-loops/toe-current-mass-20261012"
KEY = "CurrentMass"
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
        with tempfile.TemporaryDirectory(prefix='current_mass_'+KEY+'_') as temporary:
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
                    env={**os.environ, **case['environment_overrides']})
                stdout, stderr, code = result.stdout, result.stderr, result.returncode
            except subprocess.TimeoutExpired as exc:
                stdout, stderr, code, timeout = exc.stdout or b'', exc.stderr or b'', 124, True
            elapsed = time.monotonic()-started
            raw_result = output.read_bytes() if case['result_mode']=='file' and output.exists() else stdout if case['result_mode']=='stdout' else b''
            envelope = {'case':name, 'argv':argv, 'cwd':str(folder),
                'resources':case['resources'], 'environment_overrides':case['environment_overrides'], 'elapsed_seconds':elapsed,
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
