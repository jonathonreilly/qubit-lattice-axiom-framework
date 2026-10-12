#!/usr/bin/env python3
"""Prepare sentinel-only copies and freeze them without launching children."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path

E = Path(__file__).resolve().parent
F = E / 'integrity_01' / 'fixtures'
F.mkdir(parents=True, exist_ok=False)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


original = json.loads((E / 'PRE_EXECUTION_SEAL.json').read_text())
for rel, expected in original['files'].items():
    assert digest(E / rel) == expected

fixtures = {}
for name in ['valid', 'tampered_checker', 'exit_only_survivor']:
    root = F / name
    for rel in original['files']:
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((E / rel).read_bytes())
    for checker in ['check_fock.py', 'check_strong_limit.py']:
        status = 7 if name == 'exit_only_survivor' and checker == 'check_fock.py' else 0
        source = ('# Integrity fixture sentinel; no scientific computation.\n'
                  'from pathlib import Path\n'
                  'import sys\n'
                  'Path(__file__).with_suffix(".launched").write_text("launched\\n")\n'
                  'print("SENTINEL " + Path(__file__).name, flush=True)\n'
                  f'sys.exit({status})\n')
        (root / checker).write_text(source)
    fixture_seal = {'fixture': name, 'scientific_execution': False,
                    'sealed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'files': {rel: digest(root / rel) for rel in original['files']}}
    (root / 'PRE_EXECUTION_SEAL.json').write_text(json.dumps(fixture_seal, indent=2) + '\n')
    before = (root / 'check_fock.py').read_text()
    if name == 'tampered_checker':
        after = before + '# Deliberate post-fixture-seal source tamper.\n'
        (root / 'check_fock.py').write_text(after)
        (E / 'integrity_01' / 'CHECKER_TAMPER.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile='fixture-sealed/check_fock.py', tofile='post-seal/check_fock.py')))
    fixtures[name] = {'driver_sha256': digest(root / 'execute_checks.py'),
                      'fixture_manifest_sha256': digest(root / 'PRE_EXECUTION_SEAL.json'),
                      'declared_checker_sha256': fixture_seal['files']['check_fock.py'],
                      'actual_checker_sha256': digest(root / 'check_fock.py')}
    assert fixtures[name]['driver_sha256'] == 'e73d595995f41edf3ca14e218c1010d865081d8136ebec953960dd2475cc8051'

inputs = [E / 'INTEGRITY_PROTOCOL.md', E / 'prepare_integrity_fixture.py', E / 'run_integrity_fixture.py']
inputs.extend(p for p in sorted((E / 'integrity_01').rglob('*')) if p.is_file())
seal = {'frozen_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scientific_execution': False, 'fixture_execution_before_this_seal': False,
        'original_independent_seal_sha256': digest(E / 'INDEPENDENT_CHECKS_SEAL.json'),
        'fixtures': fixtures,
        'files': {str(p.relative_to(E)): digest(p) for p in inputs}}
path = E / 'INTEGRITY_EXECUTION_SEAL.json'
assert not path.exists()
path.write_text(json.dumps(seal, indent=2) + '\n')
print(json.dumps({'path': str(path), 'sha256': digest(path), 'files': len(inputs), 'fixtures': fixtures}, indent=2))
