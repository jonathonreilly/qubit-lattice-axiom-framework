"""Root recorder of the completely read immutable generation-one correspondence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, time

E=Path(__file__).resolve().parent
D=E/'formation-response-sum-independent/publication_comparison'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=D/'PUBLICATION_COMPARISON_SEAL.json'
assert sha(seal)=='79e3d680e9316faa167b18f44a5f66f6a27cebb8ce33d8081f82c19b77fa55dd'
assert sha(D/'PUBLICATION_COMPARISON.md')=='504e9dadbdc6d79843480b2c2becc7d90b4b0c0875e3b1e89192f7992288e2cc'
paths={seal}
for row in json.loads(seal.read_text())['members']:
    p=D/row['path']; assert sha(p)==row['sha256']; assert p.stat().st_size==row['bytes']; paths.add(p)
pins=json.loads((D/'SOURCE_PINS_INITIAL.json').read_text())
for row in pins['sources']:
    p=Path(row['origin']); assert p.read_bytes()==(D/row['snapshot']).read_bytes(); paths.add(p)
for name in ['PRE_SEAL.json','POST_SEAL.json']:
    p=D.parent/name; paths.add(p)
    for row in json.loads(p.read_text())['members']:
        q=D.parent/row['path']; assert sha(q)==row['sha256']; paths.add(q)
for row in json.loads((D.parent/'POST_SOURCE_PINS.json').read_text())['author39_sources']:
    p=Path(row['origin']); assert sha(p)==row['sha256']; paths.add(p)
def inventory():
    return {str(p):(sha(p),p.stat().st_size,p.stat().st_mtime_ns,p.stat().st_ctime_ns) for p in paths}
before=inventory(); start=time.perf_counter()
run=subprocess.run([sys.executable,str(D/'verify_publication_readonly.py')],capture_output=True)
elapsed=time.perf_counter()-start
assert before==inventory()
assert run.returncode==0 and run.stderr==b''
old=json.loads((D/'verification_attempt01/VERIFICATION_REPORT.json').read_bytes()); new=json.loads(run.stdout)
assert {k:v for k,v in old.items() if k!='verified_utc'}=={k:v for k,v in new.items() if k!='verified_utc'}
for name,body in [('FORMATION_RESPONSE_GENERATION1_ROOT_READONLY_RESULT.json',run.stdout),
                  ('FORMATION_RESPONSE_GENERATION1_ROOT_READONLY.stderr',run.stderr)]:
    with (E/name).open('xb') as stream: stream.write(body)
receipt={'at_utc':datetime.now(timezone.utc).isoformat(),'report_sha256':sha(D/'PUBLICATION_COMPARISON.md'),
 'seal_sha256':sha(seal),'complete_report_verifier_recorder_scope_and_failure_logs_read':True,
 'complete_verifier_result_read':True,'truncated_display_repaired':'All 75 scientific rows, with all 225 flows, reread as lossless arrays in a separate complete output.',
 'verifier_sha256':sha(D/'verify_publication_readonly.py'),'elapsed_seconds':elapsed,
 'exit_code':run.returncode,'stderr_bytes':len(run.stderr),'full_output_exact_except_verified_utc':True,
 'observed_files_content_size_mtime_ctime_unchanged':len(paths),
 'required_repair':json.loads((D/'REQUIRED_FRONT_REPLACEMENT.json').read_text()),
 'scope':'Root correspondence review using unchanged PRE/POST; no new independent science or applied audit verdict.',
 'scientific_programs_executed':[]}
with (E/'FORMATION_RESPONSE_GENERATION1_ROOT_REVIEW.json').open('x') as stream:
    json.dump(receipt,stream,indent=2); stream.write('\n')
print(json.dumps(receipt,indent=2))
