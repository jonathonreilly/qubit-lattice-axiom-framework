from pathlib import Path
import json,hashlib,subprocess,sys,gzip
r=Path('/private/tmp/review-drain-20260915');w=r/'author-slot-one';sys.path.insert(0,str(w/'scripts'));import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hb=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
record=json.loads((r/'8090-unit-v1-preexecution.json').read_text());report=json.loads((r/'review-8090-preexecution.json').read_text());tree='47114429b535660319341039cdd184feb6b5f3f6';latest='3c71a35aee35ea0896f1c0de54c1cfad1c4a1c9e'
assert git('write-tree')==tree
for rows in record['inputs'].values():
 for x in rows:
  assert sha(w/x['path'])==x['sha256']
  # Inputs added only by this proposal are absent from main; all inherited inputs must match latest main.
  probe=subprocess.run(['git','-C',str(w),'cat-file','-e',record['source']['base']+':'+x['path']],capture_output=True)
  if probe.returncode==0:assert hb(subprocess.check_output(['git','-C',str(w),'show',latest+':'+x['path']]))==x['sha256']
for x in record['source']['paths']:
 if x['path'].startswith(('logs/runner-cache/','outputs/')):x['sha256']=sha(w/x['path'])
 else:assert sha(w/x['path'])==x['sha256']
 assert hb(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']]))==x['sha256']
for e in json.loads((r/'8090-reviewer-archive-map.json').read_text())['entries']:
 b=(w/e['final_path']).read_bytes();raw=gzip.decompress(b) if e['encoding']=='gzip' else b
 assert raw==(r/'check8090/original'/e['original_path']).read_bytes()
executions=[];refs=[];differences=[]
def compare(a,b,p=''):
 if isinstance(a,dict):
  assert a.keys()==b.keys(),p
  for k in a:
   if k not in ['seconds','elapsed_seconds','source_sha256','runner_sha256','note_sha256','derivation_sha256']:compare(a[k],b[k],p+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(b),p
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,p+'/'+str(i))
 elif a!=b:
  assert isinstance(a,float) and isinstance(b,float),(p,a,b)
  differences.append({'path':p,'old':a,'new':b})
for stem,count in [('native_interacting_weyl_2026_09_13',153)]:
 f=r/('8090-execution-'+stem+'.json');receipt=json.loads(f.read_text());res=receipt['result'];cache=Path(receipt['cache_path'])
 assert receipt['preexecution_record_sha256']==sha(r/'8090-unit-v1-preexecution.json')
 assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<60 and receipt['limit_sec']==60
 assert sha(cache)==receipt['cache_sha256'] and runner_cache.cache_status(receipt['runner'])=='fresh'
 assert res['stdout'] in cache.read_text() and res['stdout'].rstrip().endswith(f'TOTAL: PASS={count} FAIL=0')
 payload=json.loads((w/receipt['output_path']).read_text());assert sha(w/receipt['output_path'])==receipt['output_sha256'];assert sha(r/'8090-original-output-before-capture.json')==receipt['original_output_sha256'];old=json.loads((r/'check8090/original'/receipt['output_path']).read_text());compare(old,payload,stem);assert sum(x['total_pass'] for x in payload.values())==153 and all(x['total_fail']==0 for x in payload.values())
 executions.append({'runner':receipt['runner'],'total_pass':count,'total_fail':0,'elapsed_sec':res['elapsed_sec'],'timeout_sec':60,'cache_sha256':sha(cache)})
 refs.append(f.name)
comparison=r/'8090-reviewer-payload-comparison.json';assert not comparison.exists();comparison.write_text(json.dumps({'excluded_metadata':['seconds','elapsed_seconds','source_sha256','runner_sha256','note_sha256','derivation_sha256'],'differences':differences,'mathematical_fields':'Compared recursively against frozen original outputs'},indent=2)+'\n')
report.update(status='PASS_WITH_BOUNDED_CLAIMS',final_verdict='PASS WITH BOUNDED CLAIMS',source_tree=tree,source_paths=record['source']['paths'],executions=executions,remaining=[],current_main_context={'commit':latest,'assessment':'The8089 informative native instrument landed since the proposal base. It offers distinct nonscalar effects and disturbance bounds;8090 uses scalar effects preserving the protected interacting matter functional. Neither changes the common native parent, external RG/LR hypotheses, chosen model or supplied state/clock assumptions. All inherited actual inputs match current main exactly.','related_review':{'path':str(r/'review-8089-final.json'),'sha256':sha(r/'review-8089-final.json')}},final_confirmation='The canonical capture ran once, with fresh caches. All22 staged paths and all actual runtime/parent/context/tool inputs bound. All16 archives decoded exact; complete21 original dispositions retained. Independent controls passed12/0. Prior intermediate/preexecution evidence remains immutable. No full pipeline or audit verdict generated.')
for x in report['original_dispositions']:
 p=x.get('final_path')
 if p and p.startswith(('logs/runner-cache/','outputs/')):
  x['final_sha256']=sha(w/p);x['disposition']='Fresh canonical cache from exactly one final bounded capture; original cache preserved at frozen original head.'
f=r/'review-8090-final.json';assert not f.exists();f.write_text(json.dumps(report,indent=2)+'\n');ref={'path':str(f),'sha256':sha(f)}
record['unit_id']='pr8090-final';record['source']['tree']=tree;record['reviewer']['report']=ref
for c in record['constituents']:c['dispositions']=dict(ref,json_pointer='/original_dispositions')
for x in record['non_science_notes']:x['review_reference']=ref
record['reviewer']['references'] += [{'path':str(r/p),'sha256':sha(r/p)} for p in refs+['8090-unit-v1-preexecution.json','review-8090-preexecution.json','8090-preexecution-preflight.json','8090-author-capture.py','8090-author-capture.log','8090-reviewer-payload-comparison.json','review-8089-final.json','8090-original-output-before-capture.json']]
record['boundary']='Final source PASS WITH BOUNDED CLAIMS; final shared cache check and combined integration remain separate. Supplied interacting Hamiltonian/counterterm, native carrier/state, controls and clocks; external RG theorem remains an import, no physical Hamiltonian or state selection derived.'
p=r/'8090-unit-v1-final.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'tree':tree,'report_sha256':sha(f),'record_sha256':sha(p),'math_differences':differences},indent=2))
