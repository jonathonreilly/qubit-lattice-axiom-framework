"""Root outer recorder for the already-read, genuinely read-only final verifier."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time

E=Path(__file__).resolve().parent
D=E/'native-ground-energy-budget-independent/publication_comparison'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=D/'PUBLICATION_COMPARISON_SEAL.json'
assert sha(seal)=='cd01b9df653f64846803d461a0c0ed516f42b7bbf42a9611a69bd8f151d4418f'
s=json.loads(seal.read_text());assert len(s['members'])==176
paths={seal}
for row in s['members']:
    p=D/row['path'];assert sha(p)==row['sha256'];assert p.stat().st_size==row['bytes'];paths.add(p)
pins=json.loads((D/'SOURCE_PINS.json').read_text());assert len(pins['origins'])==168
for row in pins['origins']:
    p=Path(row['origin']);assert p.read_bytes()==(D/row['frozen']).read_bytes();paths.add(p)
def inventory():
    return {str(p):(sha(p),p.stat().st_size,p.stat().st_mtime_ns,p.stat().st_ctime_ns) for p in paths}
before=inventory();start=time.perf_counter()
run=subprocess.run([sys.executable,str(D/'verify_publication_readonly.py')],capture_output=True)
elapsed=time.perf_counter()-start
assert before==inventory()
assert run.returncode==0 and run.stderr==b''
old=json.loads((D/'VERIFICATION_REPORT.json').read_bytes());new=json.loads(run.stdout)
assert {k:v for k,v in old.items() if k!='at_utc'}=={k:v for k,v in new.items() if k!='at_utc'}
for name,body in [('MICROSCOPIC_ENERGY_BUDGET_FINAL_READONLY_RESULT.json',run.stdout),
                  ('MICROSCOPIC_ENERGY_BUDGET_FINAL_READONLY.stderr',run.stderr)]:
    with (E/name).open('xb') as stream:stream.write(body)
P=E/'campaign-working/.claude/science/physics-loops/mobile-record-next-gaps-20260924'
active=json.loads((P/'ACTIVE_OBSERVATION_SOURCES.json').read_text())
for row in active['files']:assert sha(Path(row['path']))==row['sha256'],row['path']
assert len(active['files'])==928
receipt={'at_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root',
 'report_sha256':sha(D/'PUBLICATION_COMPARISON.md'),'seal_sha256':sha(seal),
 'complete_report_and_verifier_read':True,'complete_execution_and_scope_logs_read':True,
 'clipped_display_repaired':'VERIFICATION_REPORT.json read separately in full; historical reference receipt used only as schema with complete builder and selected context fields.',
 'seal_members_unchanged':176,'snapshot_origins_bound':168,'observed_files_unchanged_content_size_mtime_ctime':len(paths),
 'readonly_verifier_sha256':sha(D/'verify_publication_readonly.py'),'readonly_elapsed_seconds':elapsed,
 'exit_code':run.returncode,'stderr_bytes':len(run.stderr),'full_output_exact_except_at_utc':True,
 'output_sha256':hashlib.sha256(run.stdout).hexdigest(),'prior_recovery_pins_reverified':928,
 'required_scientific_repairs':[],
 'scope':'Root rereview and identity validation of previously reviewed personal37/38, separate PRE/POST and final released-source correspondence. No fresh independent scientific reconstruction or audit disposition.',
 'scientific_program_or_original_seal_writer_executions':[]}
with (E/'MICROSCOPIC_ENERGY_BUDGET_FINAL_ROOT_VERIFICATION.json').open('x') as stream:
    json.dump(receipt,stream,indent=2);stream.write('\n')
print(json.dumps(receipt,indent=2))
