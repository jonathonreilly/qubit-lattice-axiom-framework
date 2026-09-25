"""Root fresh execution of the completely read final correspondence verifier."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
E=Path(__file__).resolve().parent;D=E/'formation-response-sum-independent/publication_comparison_generation2'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
seal=D/'PUBLICATION_COMPARISON_SEAL.json';assert sha(seal)=='dc07b3e6b01a3668f52eefd5110843725d786d34a8ed0e1cefb5c5ca0d34792c'
assert sha(D/'PUBLICATION_COMPARISON.md')=='a23e997e59c0376be029b4b78e40964d9fb7a8c18a7a0253e79c66d191ea8255'
paths={seal}
for row in json.loads(seal.read_text())['members']:
 p=D/row['path'];assert sha(p)==row['sha256'];assert p.stat().st_size==row['bytes'];paths.add(p)
pins=json.loads((D/'SOURCE_PINS_INITIAL.json').read_text())
for row in pins['sources']:
 p=Path(row['origin']);assert p.read_bytes()==(D/row['snapshot']).read_bytes();paths.add(p)
for row in pins['prior_seals']:
 s=Path(row['origin']);assert sha(s)==row['sha256'];paths.add(s)
 for member in json.loads(s.read_text())['members']:
  p=s.parent/member['path'];assert sha(p)==member['sha256'];paths.add(p)
def state():return {str(p):(sha(p),p.stat().st_size,p.stat().st_mtime_ns,p.stat().st_ctime_ns) for p in paths}
before=state();t=time.perf_counter();r=subprocess.run([sys.executable,str(D/'verify_generation2_readonly.py')],capture_output=True);elapsed=time.perf_counter()-t
assert state()==before and r.returncode==0 and r.stderr==b''
prior=json.loads((D/'verification_attempt01/VERIFICATION_REPORT.json').read_text());fresh=json.loads(r.stdout)
assert {k:v for k,v in prior.items() if k!='verified_utc'}=={k:v for k,v in fresh.items() if k!='verified_utc'}
for name,body in [('FORMATION_RESPONSE_GENERATION2_ROOT_READONLY_RESULT.json',r.stdout),('FORMATION_RESPONSE_GENERATION2_ROOT_READONLY.stderr',r.stderr)]:
 with (E/name).open('xb') as f:f.write(body)
receipt={'at':datetime.now(timezone.utc).isoformat(),'report_sha256':sha(D/'PUBLICATION_COMPARISON.md'),'seal_sha256':sha(seal),'new_sealed_members':36,'prior_sealed_members_unchanged':91,'source_origins_bound':18,
 'complete_report_all_verifier_and_recorder_code_full_result_and_failure_logs_read':True,
 'scope':'Focused corrected-generation correspondence with unchanged full proof/PRE/POST review reused; no additional independent reconstruction or audit verdict.',
 'elapsed_seconds':elapsed,'exit_code':r.returncode,'stderr_bytes':len(r.stderr),'observed_files_content_size_mtime_ctime_unchanged':len(paths),
 'output_exact_except_verified_utc':True,'output_sha256':hashlib.sha256(r.stdout).hexdigest(),
 'generation1_finding_resolved':True,'required_repairs':[],
 'root_read_filename_failure':'Initial cat used nonexistent verify_publication_generation2_readonly.py; file listing located verify_generation2_readonly.py, subsequently fully read. No execution failure or source change.'}
with (E/'FORMATION_RESPONSE_FINAL_ROOT_VERIFICATION.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt,indent=2))
