"""Final reviewer binding only: no science/preflight execution or source mutation."""
from pathlib import Path
import json,hashlib,subprocess,sys,gzip
r=Path('/private/tmp/review-drain-20260915');w=r/'author-slot-one'
sys.path.insert(0,str(w/'scripts'));import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hb=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
assert len(sys.argv)==2,'exact final staged tree required'
tree=sys.argv[1];assert git('write-tree')==tree
record=json.loads((r/'8095-unit-v1-preexecution.json').read_text());report=json.loads((r/'review-8095-preexecution.json').read_text())
latest=git('rev-parse','origin/main');base=record['source']['base']
for rows in record['inputs'].values():
 for x in rows:
  assert sha(w/x['path'])==x['sha256']
  exists=subprocess.run(['git','-C',str(w),'cat-file','-e',base+':'+x['path']],capture_output=True).returncode==0
  if exists:assert hb(subprocess.check_output(['git','-C',str(w),'show',latest+':'+x['path']]))==x['sha256'],x['path']
runner=record['notes'][0]['primary_runner'];stem=Path(runner).stem
cache_rel='logs/runner-cache/'+stem+'.txt'
old_paths={x['path'] for x in record['source']['paths']}
changed=set(git('diff','--cached','--name-only',base).splitlines());assert changed==old_paths|{cache_rel}
for x in record['source']['paths']:assert sha(w/x['path'])==x['sha256']
record['source']['paths']=[dict(path=p,sha256=sha(w/p)) for p in sorted(changed)]
for x in record['source']['paths']:assert hb(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']]))==x['sha256']
for e in report['archive_entries']:
 raw=(w/e['final_path']).read_bytes();raw=gzip.decompress(raw) if e['encoding']=='gzip' else raw
 assert raw==(r/'check8095/original-8095'/e['original_path']).read_bytes()
receipt_path=r/('8095-execution-'+stem+'.json');receipt=json.loads(receipt_path.read_text());res=receipt['result'];cp=Path(receipt['cache_path'])
assert receipt['preexecution_record_sha256']==sha(r/'8095-unit-v1-preexecution.json')
assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<60 and receipt['limit_sec']==60
assert cp.resolve()==(w/cache_rel).resolve() and sha(cp)==receipt['cache_sha256'] and runner_cache.cache_status(runner)=='fresh'
assert res['stdout'] in cp.read_text() and 'TOTAL: PASS=274 FAIL=0' in res['stdout']
new,_=json.JSONDecoder().raw_decode(res['stdout']);assert new['status']=='ok' and new['check_count']==len(new['checks'])==274
old,_=json.JSONDecoder().raw_decode((r/'check8095/original-8095/.claude/science/physics-loops/native-canonical-metric-20260913/AUTHOR_RUN.stdout').read_text())
differences=[]
def compare(a,b,path=''):
 assert type(a)==type(b),(path,type(a),type(b))
 if isinstance(a,dict):
  assert a.keys()==b.keys(),path
  for k in a:
   if k not in ['elapsed_seconds','source_sha256']:compare(a[k],b[k],path+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(b),path
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,path+'/'+str(i))
 elif a!=b:
  assert isinstance(a,float),(path,a,b)
  differences.append(dict(path=path,old=a,new=b,absolute_difference=abs(a-b)))
compare(old,new)
# Preserve actual field differences for review; this is not a new tolerance.
comparison=r/'8095-reviewer-payload-comparison.json'
assert not comparison.exists();comparison.write_text(json.dumps(dict(excluded_metadata=['elapsed_seconds','source_sha256'],differences=differences,boundary='All structural and nonfloating fields unchanged; floating differences logged individually. Decisive scientific thresholds remain original unchanged assertions; no cross-run threshold replaces them.'),indent=2)+'\n')
print(json.dumps(dict(tree=tree,latest=latest,differences=len(differences),maximum_difference=max([d['absolute_difference'] for d in differences],default=0),elapsed=res['elapsed_sec']),indent=2))
# Finalization is a separate command after actual differences are inspected.
