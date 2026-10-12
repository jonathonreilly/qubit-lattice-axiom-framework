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
AUDIT_INPUT_PATHS = ['docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONTINUUM_LOCAL_BOOST_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MICROSCOPIC_LOCAL_BOOST_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/MIXED_LOCAL_POINCARE_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/RUNTIME.json', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/MUTATION_SOURCE_MAP.json', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/EXPECTED_RECORD_IDENTITIES.json', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/SPECIFICATIONS.json', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/RUNNER_TEMPLATE.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/reconstruct.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/036f7cd9c547ec9d7e1498f1ba9e6e7732cd57551b5c2b79c907e264fa710acb.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/0ad620972d4c6e3419fbd7e841d42d976344643b7839975b24202563fd049e61.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/1360bdbf076f12a70dc9682c2f8a5edfd15b798c136b47f3465f4b98c6b531bf.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/197b20060ebfaf29c6e3f1825459e58a4ed72d91bdb6f066e16f41477e4a396c.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/2aab5d041f97fc35a54dacdc1c3a9c38478b75184e73c0c5e45b9fd4cb2432a4.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/3d2461a2df3229f96dd7172fd3afafa1a2001b5535d8b02218bd74992ba3027e.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/4ee8aa0a8ddea4aa6cc435c460822fdc97252e773733ad32b7fb1654bd2e4280.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/73bbaa3192c87764cb98df1fb0469a228df0cd52dab30544b44dcdbe3782bbc0.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/7799eee8ca22f9f74072e748237c0d4b19ab180e20c9e5b9b762c1eb47c0c7c0.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/94afdc8d941194ac543626ea6c90461d4fdb2efc334cffa7eab0f101ee06494a.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/a0e21f59008f5da9c8b035d0cbc82d4780119f81f96c03e9dc0f56cc87cfa827.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/a563cb5fff3175b80e82e2a4504301844fb1d346bc5269f9ad89c2ff6b86bac0.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/b28f2ecf8d59ccb88a5117cb65cd6c76826394ffabd965a7072d915d4deef288.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/b893fe9965465ab6164a2899966dae1c499f4e3af8aea792f20b796ce2821489.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/cda1e92e413598567149eb6dc0606bb65ceb4ab6c9f23603975bfb782154e3e7.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/d3911f8f6bc59719aa1d4aaff4cf2ffe074aca455d6a262f8c4d4a9d4b987f41.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/dc3c3598cf3a1d1e0f9f8213e94fd8ac92a43306ff37cbcaaa0617071945779c.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/e89399865add08546caf81edb9557aed3848826e883efd9ddda0847bab923a42.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/f8d82af98019f69b5ab876cb5f784ec6379677bd8815372616554b135ae92cf5.py', '.claude/science/physics-loops/toe-dyadic-refinement-20261012/runtime/f9772dc104f18747ebb5d44694393685dcd2a17b56ff1dbb7ee4be765355a67a.py']
PACKET = ".claude/science/physics-loops/toe-dyadic-refinement-20261012"
KEY = "DyadicEven"
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
        with tempfile.TemporaryDirectory(prefix='dyadic_even_'+KEY+'_') as temporary:
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
                'interpreter':sys.executable, 'python':sys.version,
                'resources':case['resources'], 'environment_overrides':case['environment_overrides'], 'elapsed_seconds':elapsed,
                'timeout_seconds':case['timeout_seconds'], 'timed_out':timeout,
                'exit_code':code, 'stdout':stdout.decode(), 'stderr':stderr.decode(),
                'result_raw':raw_result.decode()}
            # Preserve the whole observed envelope before parsing or evaluating it.
            print('SCIENTIFIC_ENVELOPE '+json.dumps(envelope, ensure_ascii=False, allow_nan=False), flush=True)
            if timeout:
                return 124
            objects = [json.loads(line) for line in raw_result.decode().splitlines() if line.startswith('{')]
            rows = [row for row in objects if 'name' in row and 'pass' in row]
            if not rows or any(type(row['pass']) is not bool for row in rows):
                raise RuntimeError('Original predicate schema changed')
            counts = {'rows':len(rows), 'pass':sum(row['pass'] for row in rows), 'fail':sum(not row['pass'] for row in rows), 'failed':[row['name'] for row in rows if not row['pass']]}
            if objects[-1] != {'summary':counts}:
                raise RuntimeError('Original summary disagrees with actual rows')
            for relative, pin in case['resources'].items():
                if hashlib.sha256((folder/relative).read_bytes()).hexdigest() != pin['sha256']:
                    raise RuntimeError('Helper source changed during execution')
            for line in raw_result.decode().splitlines():
                if line.startswith(('per_element:', 'per_site:', 'per_mode:', 'per_block:', 'lattice_wide:')) and line not in certificates:
                    certificates.append(line)
            passed += counts['pass']
            failed += counts['fail']
            codes.append(code)
    for line in certificates:
        print(line, flush=True)
    print(f'TOTAL: PASS={passed} FAIL={failed}', flush=True)
    return next((code for code in codes if code != 0), 0)


if __name__ == '__main__':
    raise SystemExit(main())
