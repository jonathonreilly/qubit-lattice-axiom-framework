from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
Q=Path(__file__).resolve().parent;N=Q.parent;A=N/'local_clock_single_port_mediator_candidate';V=N/'local_clock_single_port_mediator_decisive_check';W=N.parent/'correlation_worktree'
def read(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def same(p,r):
 a=pin(p);assert a['sha256']==r['sha256'] and ('bytes' not in r or a['bytes']==r['bytes']),str(p)
def seal(folder,digest):
 f=read(folder/'FINAL_FREEZE.json');assert pin(folder/'FINAL_FREEZE.json')['sha256']==digest
 assert {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
 for r in f['files']:same(folder/r['path'],r)
 return len(f['files'])+1
ac=seal(A,'bf32aa1e08256fbf38e3989c9f7d69718bb52b56c8ca7ade0485abbc5e7285c3');vc=seal(V,'a5b22abc0ecb1e684d8cf8ca3719bbe62e25aaa3c8b8a52a19eea1b60a86e5d7')
m=read(V/'SOURCE_MANIFEST.json');count=0
for r in m['files']+m['final_files']:
 same(V/r['snapshot'],r);same(r['source'],r);count+=1
for r in read(A/'SOURCE_MANIFEST.json')['sources']:same(A/r['snapshot'],r);same(r['source'],r)
for r in m['instruction_reuse_checks']:
 b=subprocess.check_output(['git','show','origin/main:'+r['path']],cwd=W);assert hashlib.sha256(b).hexdigest()==r['old_sha256'],r['path']
receipts=[]
for prefix,src,result in [('METADATA','verify_metadata.py','METADATA_CHECK.json'),('FINAL_FRESHNESS','check_final_freshness.py','FINAL_SOURCE_FRESHNESS.json')]:
 r=read(V/(prefix+'_EXECUTION_RECEIPT.json'));assert r['exit_code']==0;assert pin(V/src)['sha256']==r['source_sha256']
 for stream in ['stdout','stderr']:
  p=pin(V/(prefix+'_'+stream.upper()+'.log'));assert p['sha256']==r[stream+'_sha256'] and p['bytes']==r[stream+'_bytes']
 j=read(V/result);assert j['source_sha256']==r['source_sha256'];assert all(x.get('passed',x.get('same',False)) for x in j['checks']);receipts.append({'receipt':pin(V/(prefix+'_EXECUTION_RECEIPT.json')),'result':pin(V/result),'start':r['started_utc'],'finish':r['finished_utc'],'scope':r['scope']})
closure={'utc':datetime.now(timezone.utc).isoformat(),'candidate':pin(A/'DERIVATION.md'),'candidate_seal':pin(A/'FINAL_FREEZE.json'),'review':pin(V/'REPORT.md'),'review_seal':pin(V/'FINAL_FREEZE.json'),'candidate_files':ac,'review_files':vc,'review_manifest_rows_checked':count,'reused_candidate_closure':pin(Q/'CANDIDATE_SOURCE_CLOSURE.json'),'review_metadata_receipts':receipts,'acceptance':pin(Q/'ACCEPTANCE.md'),'root_scientific_executions':0,'limits':'Identity/receipt closure only; scientific acceptance is explicit analytic reading in ACCEPTANCE.md, not predicate totals. Author selected fixture plus retrospective adjacency analysis not rerun. No audit.'}
(Q/'SOURCE_CLOSURE.json').write_text(json.dumps(closure,indent=2)+'\n')
files=[p for p in sorted(Q.rglob('*')) if p.is_file() and p.name!='FINAL_FREEZE.json'];out={'sealed_utc':datetime.now(timezone.utc).isoformat(),'status':'Root conditional source acceptance for milestone review; not audit','files':[dict(pin(p),path=str(p.relative_to(Q))) for p in files]};(Q/'FINAL_FREEZE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'acceptance':pin(Q/'ACCEPTANCE.md'),'closure':pin(Q/'SOURCE_CLOSURE.json'),'freeze':pin(Q/'FINAL_FREEZE.json'),'candidate_files':ac,'review_files':vc,'science_executions':0}))
