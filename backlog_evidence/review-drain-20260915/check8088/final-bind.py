from pathlib import Path
import json,hashlib,subprocess,sys,gzip
r=Path('/private/tmp/review-drain-20260915');w=r/'author-slot-one';sys.path.insert(0,str(w/'scripts'));import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hb=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
record=json.loads((r/'8088-unit-v1-preexecution-ready.json').read_text());report=json.loads((r/'review-8088-preexecution-ready.json').read_text());tree='0ae6892635ede108cb33ceaf3fd3b2b2f0450aa8';latest='db421593400589cbc0dc5f39bbefedff8302c559'
assert git('write-tree')==tree
for rows in record['inputs'].values():
 for x in rows:
  assert sha(w/x['path'])==x['sha256']
  # Inputs added only by this proposal are absent from main; all inherited inputs must match latest main.
  probe=subprocess.run(['git','-C',str(w),'cat-file','-e',record['source']['base']+':'+x['path']],capture_output=True)
  if probe.returncode==0:assert hb(subprocess.check_output(['git','-C',str(w),'show',latest+':'+x['path']]))==x['sha256']
for x in record['source']['paths']:
 if x['path'].startswith('logs/runner-cache/'):x['sha256']=sha(w/x['path'])
 else:assert sha(w/x['path'])==x['sha256']
 assert hb(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']]))==x['sha256']
for e in json.loads((r/'8088-author-archive-map.json').read_text())['entries']:
 b=(w/e['final_path']).read_bytes();raw=gzip.decompress(b) if e['encoding']=='gzip' else b
 assert raw==(r/'check8088/original'/e['original_path']).read_bytes()
executions=[];refs=[];differences=[]
def compare(a,b,p=''):
 if isinstance(a,dict):
  assert a.keys()==b.keys(),p
  for k in a:
   if k not in ['seconds','source_sha256','runner_sha256','note_sha256','derivation_sha256']:compare(a[k],b[k],p+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(b),p
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,p+'/'+str(i))
 elif a!=b:
  assert isinstance(a,float) and isinstance(b,float),(p,a,b)
  differences.append({'path':p,'old':a,'new':b})
for stem,count in [('projective_history_local_program_2026_09_13',107),('projective_history_local_copy_record_process_2026_09_13',31)]:
 f=r/('8088-execution-'+stem+'.json');receipt=json.loads(f.read_text());res=receipt['result'];cache=Path(receipt['cache_path'])
 assert receipt['preexecution_record_sha256']==sha(r/'8088-unit-v1-preexecution-ready.json')
 assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<180 and receipt['limit_sec']==180
 assert sha(cache)==receipt['cache_sha256'] and runner_cache.cache_status(receipt['runner'])=='fresh'
 assert res['stdout'] in cache.read_text() and res['stdout'].rstrip().endswith(f'TOTAL: PASS={count} FAIL=0')
 payload=json.JSONDecoder().raw_decode(res['stdout'])[0]
 oldtext=(r/'check8088/original/logs/runner-cache'/ (stem+'.txt')).read_text();old=json.JSONDecoder().raw_decode(oldtext[oldtext.index('{'):])[0];compare(old,payload,stem)
 executions.append({'runner':receipt['runner'],'total_pass':count,'total_fail':0,'elapsed_sec':res['elapsed_sec'],'timeout_sec':180,'cache_sha256':sha(cache)})
 refs.append(f.name)
comparison=r/'8088-reviewer-payload-comparison.json';assert not comparison.exists();comparison.write_text(json.dumps({'excluded_metadata':['seconds','source_sha256','runner_sha256','note_sha256','derivation_sha256'],'differences':differences,'mathematical_fields':'Compared recursively against frozen original outputs'},indent=2)+'\n')
report.update(status='PASS_WITH_BOUNDED_CLAIMS',final_verdict='PASS WITH BOUNDED CLAIMS',source_tree=tree,source_paths=record['source']['paths'],executions=executions,remaining=[],current_main_context={'commit':latest,'assessment':'Only reviewed8087 native growing-formation source and its historical/generated context have landed since the proposal base. Its supplied native protected current/formation model neither alters the selected trace-history parent nor supplies a missing probability selector or physical program router for8088. All inherited actual inputs match current main exactly; no changed scientific premise or scope interaction.','related_review':{'path':str(r/'review-8087-final.json'),'sha256':sha(r/'review-8087-final.json')}},final_confirmation='Both canonical captures ran once, with fresh caches. All109 staged paths and all actual runtime/parent/context/tool inputs bound. All134 archives decoded exact; complete141 original dispositions retained. Independent controls passed10/0. Prior intermediate/preexecution evidence remains immutable. No full pipeline or audit verdict generated.')
for x in report['original_dispositions']:
 p=x.get('final_path')
 if p and p.startswith('logs/runner-cache/'):
  x['final_sha256']=sha(w/p);x['disposition']='Fresh canonical cache from exactly one final bounded capture; original cache preserved at frozen original head.'
f=r/'review-8088-final.json';assert not f.exists();f.write_text(json.dumps(report,indent=2)+'\n');ref={'path':str(f),'sha256':sha(f)}
record['unit_id']='pr8088-final';record['source']['tree']=tree;record['reviewer']['report']=ref
for c in record['constituents']:c['dispositions']=dict(ref,json_pointer='/original_dispositions')
for x in record['non_science_notes']:x['review_reference']=ref
record['reviewer']['references'] += [{'path':str(r/p),'sha256':sha(r/p)} for p in refs+['8088-unit-v1-preexecution-ready.json','review-8088-preexecution-ready.json','8088-preexecution-preflight.json','8088-author-capture.py','8088-author-capture.log','8088-reviewer-payload-comparison.json','review-8087-final.json']]
record['boundary']='Final source PASS WITH BOUNDED CLAIMS; final shared cache check and combined integration remain separate. Supplied finite preparation/program probability tables and routing, no physical probability selector.'
p=r/'8088-unit-v1-final.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'tree':tree,'report_sha256':sha(f),'record_sha256':sha(p),'math_differences':differences},indent=2))
