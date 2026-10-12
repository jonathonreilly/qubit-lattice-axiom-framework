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
AUDIT_INPUT_PATHS = ['docs/STATE_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-state-adapted-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-state-adapted-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-state-adapted-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-state-adapted-20261012/MUTATION_SOURCE_MAP.json', '.claude/science/physics-loops/toe-state-adapted-20261012/ARITHMETIC_REPAIR_SOURCE_MAP.json', '.claude/science/physics-loops/toe-state-adapted-20261012/EXPECTED_RECORD_IDENTITIES.json', '.claude/science/physics-loops/toe-state-adapted-20261012/SPECIFICATIONS.json', '.claude/science/physics-loops/toe-state-adapted-20261012/RUNNER_TEMPLATE.py', '.claude/science/physics-loops/toe-state-adapted-20261012/reconstruct.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/00d14d807196ee6e420dbb543a73dc8ad0d475e540b1650bf925836139357678.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/0ab1092663ddea1beb7fd065cf073c2a8e2f7e12849183e63881c597e8aa6951.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/0c3a179a2310c0e72f64e5e5c48ba85dbaf66228bb7a08cab20ce839262888a1.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/1aa3c3e09ee5cfc82e1ffe13b12c7c4e3c0cad9c3c1e11c60cfe6f2a62912dc8.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/3d5b148f65fb941afaee70e300b97aac1b3f9ba747469702e724f4a50185a8f5.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/48a98dd055d874a1d06d4e7fd7843c121f221812c6ff3c4a6ac3af46e4728fe5.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/4c68256f1d60191f0eced0d10370fdbadb3b3462de50d5d67bb3c79ead650166.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/623a978bb4a53ab84e02fbc0a9e8e2ff93b93657486432b5138c5a7b78c75a9b.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/770e4bf3d208f3a6cbb9e34cd491747735ea6ec7621616c7a9def44212f2906b.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/7c76db00697bf2086338742f46d3cc0da84c06a44a6a9210a6969bb18309e2a6.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/8786277bfac41f9502d48ff8f5b68062f00a975f383f0b5ef4845536cda4a19f.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/94afdc8d941194ac543626ea6c90461d4fdb2efc334cffa7eab0f101ee06494a.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/a2c7edc4702b368cc6a68dba1689e5d621d8b94a4515c3834df646cf77d771d5.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/a3fd1b36d0de4dda9ac4a83735c3e650202b7dace578969f7ed9ede14a369511.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/a989e993e3a1868e2967dec6f43e5ab3b6dae4c844f3466c5be672c27dd4ef58.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/ae7089947b5c5a2a158ff61924d3e1061464698ab90ea5c401d5d5f5eeb9d78c.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/b0008df1d04c3348474af28b7cf55abf40f8800350595d27c0d55b331abbb982.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/b28f2ecf8d59ccb88a5117cb65cd6c76826394ffabd965a7072d915d4deef288.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/b5a2ea74d2cce5e93aa2dc9293139a181412441b7d46cdfe139d744708a8fe49.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/cc273d77ea9a0b07945999f6bb1c2079a2a75586bcdddad92d85ec9e527b0e5c.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/d39f2bbee80e5351a93fef1334ebb9168e2ad16e367cae1b659ed5a726685f75.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/d8934d593355a6076ef9f188df0acf2a666bdab2e8a37114e86f63ecac52a6f2.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/dc3c3598cf3a1d1e0f9f8213e94fd8ac92a43306ff37cbcaaa0617071945779c.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/e15a63f74361154d68d630f855bee55fd8e0c39b56933af5e142173063f0af93.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/e73d595995f41edf3ca14e218c1010d865081d8136ebec953960dd2475cc8051.py', '.claude/science/physics-loops/toe-state-adapted-20261012/runtime/e89399865add08546caf81edb9557aed3848826e883efd9ddda0847bab923a42.py']
PACKET = ".claude/science/physics-loops/toe-state-adapted-20261012"
KEY = "StateAdapted"
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
