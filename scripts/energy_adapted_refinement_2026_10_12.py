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
AUDIT_INPUT_PATHS = ['docs/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-energy-adapted-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-energy-adapted-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-energy-adapted-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-energy-adapted-20261012/MUTATION_SOURCE_MAP.json', '.claude/science/physics-loops/toe-energy-adapted-20261012/EXPECTED_RECORD_IDENTITIES.json', '.claude/science/physics-loops/toe-energy-adapted-20261012/SPECIFICATIONS.json', '.claude/science/physics-loops/toe-energy-adapted-20261012/RUNNER_TEMPLATE.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/reconstruct.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/0ab1092663ddea1beb7fd065cf073c2a8e2f7e12849183e63881c597e8aa6951.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/0d4df5085cbda776e992f4363bb389db8b28044b349cdf8686dcb6ab8aed4fd6.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/1b18e11b3fa3cc9da24b53a06d96358605350391b690efac73202e22dc3a0c31.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/27b3708347c9cede2b909c7d5003e8fb170b18d9eae85cb760786c8f8f5c6b9e.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/2816edbd9b5763f63c675bcb4fccdf7ad6fe965214994bd00dc1bdd55b1d6bf4.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/388ab163be73f7dc8febb6518732faf83fa59fc3dcc448afb6f7efeeaf827ed8.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/51117c510e7694708a310a4271b6f97380d89e90f27d7d7c549e5a4cecc901f5.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/5c08dc60542f8e935e202c0f2add73cc600fe50182679146a69077179c07931e.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/73f3814517a0b6b68997f41d74c1fbe6813438ef358678cdf92cd6579f61239d.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/78e921f1e326a995fe7397f3745d02db945dc3b606bf47bedc30db51c13f67c2.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/94afdc8d941194ac543626ea6c90461d4fdb2efc334cffa7eab0f101ee06494a.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/98169b3bb5ca2f784d7c1dc2f4dd0f0342adffd169eab362e2635c47768893b4.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/a710f498cb728f0a69f63a93e1f8029f61589273b1325a3853852b4dc7d85872.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/b1c5b362d3f8facef7cc6fd3422cf497bdb47c57f3298cf0d6031b0a9253522a.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/b28f2ecf8d59ccb88a5117cb65cd6c76826394ffabd965a7072d915d4deef288.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/c64686fd5fad25c258a61b3925e9d6ad59eca58b87ce2c3cdd794043645dad3d.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/c7126d0c2ab1e3a257c6094f7154d65fa2ee936a6b5e84158e0fc5c02b487e78.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/c7bb400fbc26ee68d767870fafa17424811c35e5d650311f822a69f06f80c457.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/d0d179407916f02e362eaa1360184d546cb261f2a46c1abbab03eff89b5967b7.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/d3678249ce49be99a0f8a6d98333a1defe7f490013399f5960e7412930898b5c.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/d58ea5e4e7b93e285dcbdd746ad7f658e485ccdd835bb75180e88427f76cdce7.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/d8093dcb1e7e8b68faa4a230903a659e1a007aa83116bfe5d61b28f1452eaf87.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/dc3c3598cf3a1d1e0f9f8213e94fd8ac92a43306ff37cbcaaa0617071945779c.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/e0465f9496125eb334b92ea017a963468d835b0784799fd663e732966f382894.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/e492688e1aab4c62179f9d0f259225c0c1a2400b05f2389f6f12b458cc471745.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/e89399865add08546caf81edb9557aed3848826e883efd9ddda0847bab923a42.py', '.claude/science/physics-loops/toe-energy-adapted-20261012/runtime/ec46dc2402444b0423cd5a3ae6601ae3456a992bc133c152080f091f127e5c7e.py']
PACKET = ".claude/science/physics-loops/toe-energy-adapted-20261012"
KEY = "EnergyAdapted"
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
        with tempfile.TemporaryDirectory(prefix='energy_adapted_'+KEY+'_') as temporary:
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
