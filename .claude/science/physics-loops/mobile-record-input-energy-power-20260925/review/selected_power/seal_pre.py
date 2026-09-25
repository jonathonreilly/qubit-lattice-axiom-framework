#!/usr/bin/env python3
from datetime import datetime,timezone
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
assert not (HERE/'PRE_SEAL.json').exists()
def sha(data):return hashlib.sha256(data).hexdigest()
def dump(path,data):
 with path.open('x') as f:json.dump(data,f,indent=2,allow_nan=False);f.write('\n')
pins=json.loads((HERE/'SOURCE_PINS.json').read_text())
for row in pins['sources']:
 a=Path(row['origin']).read_bytes();b=(HERE/row['frozen_path']).read_bytes()
 assert a==b and len(a)==row['bytes'] and sha(a)==row['sha256']
assert (HERE/'COEFFICIENT_TABLE.md').read_text() in (HERE/'PRE.md').read_text()
scripts={sha(p.read_bytes()):p.name for p in HERE.glob('*.py')}
execution_rows=[]
for path in sorted(HERE.glob('*.execution.json')):
 r=json.loads(path.read_text());label=path.name[:-len('.execution.json')]
 assert r['script_sha256'] in scripts
 for stream in ('stdout','stderr'):
  data=(HERE/(label+'.'+stream+'.txt')).read_bytes()
  assert len(data)==r[stream+'_bytes'] and sha(data)==r[stream+'_sha256']
 if label=='verify':assert r['exit_code']==1
 else:assert r['exit_code']==0 and r['stderr_bytes']==0
 execution_rows.append(dict(label=label,script_version=scripts[r['script_sha256']],exit_code=r['exit_code'],elapsed_seconds=r['elapsed_seconds']))
assert json.loads((HERE/'verify_corrected.stdout.txt').read_text())==json.loads((HERE/'EVIDENCE_VERIFICATION.json').read_text())
dump(HERE/'FINAL_RECHECK.json',dict(checked_utc=datetime.now(timezone.utc).isoformat(),
 source_origins_unchanged=len(pins['sources']),source_sha256={row['origin']:row['sha256'] for row in pins['sources']},
 executions=execution_rows,expected_failed_verifier_runs=1,retained_initial_Fourier_scope_correction=True,
 full_coefficient_table_in_PRE=True,author_candidate_seen=False))
members=[]
for path in sorted(HERE.rglob('*')):
 if path.is_file():
  data=path.read_bytes();members.append(dict(path=str(path.relative_to(HERE)),bytes=len(data),sha256=sha(data)))
seal=dict(phase='Blind independent PRE',sealed_at_utc=datetime.now(timezone.utc).isoformat(),
 scope='Original selected common-rotor mark power on exact charged compact preparation; full gain and anticommutator, fixed-L weak-field limit, exact local coefficients and winding controls.',
 source_origins=10,member_count=len(members),members=members,
 author_candidate_read=False,author_code_read_imported_or_run=False,delegation=False,audit_or_publication_mutation=False,
 preserved_corrections=['Initial L6 raw gain table used large-lift offset; exact net coefficient unchanged.',
                       'Initial evidence verifier assumed 264 local pairs on L6; actual 261-pair scientific output unchanged.'],
 preservation='One-time content-hash ledger; all members and this seal made read-only. Sources and prior packets untouched.')
dump(HERE/'PRE_SEAL.json',seal)
for row in members:
 path=HERE/row['path'];path.chmod(0o444);assert sha(path.read_bytes())==row['sha256']
(HERE/'PRE_SEAL.json').chmod(0o444)
print(json.dumps(dict(seal_path=str(HERE/'PRE_SEAL.json'),seal_sha256=sha((HERE/'PRE_SEAL.json').read_bytes()),
 PRE_sha256=sha((HERE/'PRE.md').read_bytes()),members=len(members),source_origins=10,logged_executions=len(execution_rows)),indent=2))
