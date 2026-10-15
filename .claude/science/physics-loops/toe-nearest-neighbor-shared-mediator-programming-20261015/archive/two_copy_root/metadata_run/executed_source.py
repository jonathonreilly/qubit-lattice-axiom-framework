from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
Q=Path(__file__).resolve().parent;N=Q.parent;W=N.parent/'correlation_worktree'
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(Path(p).read_text())
def same(p,r):
 a=pin(p);assert a['sha256']==r['sha256'] and ('bytes' not in r or a['bytes']==r['bytes']),str(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'scope':'Metadata identity closure; complete analytic root read recorded separately. No scientific program executed.','packets':{}}
for name in ('local_clock_shared_mediator_candidate','local_clock_shared_mediator_decisive_check'):
 p=N/name;f=read(p/'FINAL_FREEZE.json');actual={str(x.relative_to(p)) for x in p.rglob('*') if x.is_file()};expected={r['path'] for r in f['members']}|{'FINAL_FREEZE.json'}
 assert actual==expected,(name,actual^expected)
 for row in f['members']:same(p/row['path'],row)
 m=read(p/'SOURCE_MANIFEST.json');rows=m.get('files',m.get('sources'));live=[]
 for row in rows:
  same(p/row['snapshot'],row)
  if row['source'].startswith('/'):
   same(row['source'],row);live.append(pin(row['source']))
 out['packets'][name]={'freeze':pin(p/'FINAL_FREEZE.json'),'manifest':pin(p/'SOURCE_MANIFEST.json'),'members':len(f['members']),'total_files':len(actual),'live_origins':live}
p=N/'local_clock_shared_mediator_decisive_check'
a=read(p/'metadata_run_01/SOURCE_FRESHNESS.json');b=read(p/'SOURCE_FRESHNESS.json');assert a['checks']==b['checks'] and a['refs']==b['refs'] and a['all_matched'] and b['all_matched'];assert len(b['checks'])==161
out['review_receipts']=[]
for label in ('metadata_run_01','metadata_run_final'):
 d=p/label;r=read(d/'EXECUTION.json');l=read(d/'LAUNCH.json');assert r['returncode']==0 and all(r[k]==v for k,v in l.items())
 for file,field in [('executed_source.py','source_sha256'),('stdout','stdout_sha256'),('stderr','stderr_sha256')]:same(d/file,{'sha256':r[field]})
 assert pin(d/'executed_source.py')['sha256']==pin(p/'verify_sources.py')['sha256']==r['source_after_sha256']
 out['review_receipts'].append({'receipt':pin(d/'EXECUTION.json'),'start':r['started_utc'],'end':r['completed_utc'],'exit':r['returncode']})
c=N/'local_clock_shared_mediator_candidate';r=read(c/'runs/selected_01/EXECUTION.json');assert r['returncode']==0
for file,field in [('executed_source.py','source_sha256'),('stdout','stdout_sha256'),('stderr','stderr_sha256')]:same(c/'runs/selected_01'/file,{'sha256':r[field]})
same(c/'PRE_EXECUTION_SEAL.json',{'sha256':r['seal_sha256']})
mapping={'selected_exact_fixture.py':'executed_source.py'}
for row in read(c/'PRE_EXECUTION_SEAL.json')['files']:same(c/'runs/selected_01'/mapping.get(row['path'],'pre_execution_'+row['path']),row)
out['author_science_receipt']=pin(c/'runs/selected_01/EXECUTION.json');out['root_scientific_replays']=0
out['current_refs']={k:subprocess.check_output(['git','rev-parse',k],cwd=W).decode().strip() for k in b['refs']}
out['ref_changes_since_review']={k:{'then':v,'now':out['current_refs'][k]} for k,v in b['refs'].items() if out['current_refs'][k]!=v}
assert set(out['ref_changes_since_review'])=={'HEAD'} and out['current_refs']['HEAD']=='3e647b40c1f554205aa63d97fe0b5c9bf97a9917'
out['ref_change_explanation']='Root published independent compensation PR9602 after review; all pinned scientific/instruction source bytes remain unchanged.'
(Q/'SOURCE_CLOSURE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'closure':pin(Q/'SOURCE_CLOSURE.json'),'packets':{k:{j:v[j] for j in ('members','total_files')} for k,v in out['packets'].items()},'review_metadata_comparisons':len(b['checks']),'ref_changes':out['ref_changes_since_review'],'science_replays':0}))
