#!/usr/bin/env python3
"""One-time local PRE42 seal WRITER. Never a read-only verifier."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

base=Path(__file__).resolve().parent
seal_path=base/'PRE_SEAL.json'
assert not seal_path.exists()
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
manifest=json.loads((base/'EVIDENCE_PINS.json').read_text())
for row in manifest['members']:
    p=base/row['path']
    assert digest(p)==row['sha256'] and p.stat().st_size==row['bytes']
sources=json.loads((base/'SOURCE_PINS.json').read_text())['sources']
for row in sources:
    assert digest(Path(row['origin']))==row['sha256']
receipt=json.loads((base/'verification_attempt01/EXECUTION.json').read_text())
assert receipt['exit_code']==0 and receipt['observed_unchanged']
assert receipt['observed_before']==receipt['observed_after']
for name,sha in receipt['observed_after'].items():
    assert digest(Path(name))==sha
assert digest(base/'verification_attempt01/stdout.json')==receipt['stdout_sha256']
assert digest(base/'verification_attempt01/stderr.txt')==receipt['stderr_sha256']
assert (base/'verification_attempt01/stderr.txt').read_bytes()==b''
files=[p for p in sorted(base.rglob('*')) if p.is_file()]
assert all(not p.is_symlink() for p in files)
members=[dict(path=str(p.relative_to(base)),sha256=digest(p),bytes=p.stat().st_size) for p in files]
seal=dict(sealed_utc=datetime.now(timezone.utc).isoformat(),phase='PRE42 before author disclosure',
          report='PRE.md',report_sha256=digest(base/'PRE.md'),members=members,
          member_count=len(members),source_origins=sources,
          genuinely_readonly_verifier='verify_readonly.py',
          verifier_report='verification_attempt01/stdout.json',
          historical_model_exposure_disclosed=True,author42_access=False,
          author_or_parent_scientific_programs_executed_or_imported=False,
          delegation=False,public_or_audit_mutations=False,
          scope='Full common rotor original-instrument first-birth charge law; no finite-resource microscopic stopping theorem or particle/detector claim')
with seal_path.open('x') as out:
    out.write(json.dumps(seal,indent=2,sort_keys=True)+'\n')
for p in files+[seal_path]:
    p.chmod(0o444)
for row in members:
    assert digest(base/row['path'])==row['sha256']
print(json.dumps(dict(report_sha256=seal['report_sha256'],seal_sha256=digest(seal_path),
                     members=len(members),source_origins=len(sources),
                     seal_path=str(seal_path),all_members_reverified=True),indent=2,sort_keys=True))
