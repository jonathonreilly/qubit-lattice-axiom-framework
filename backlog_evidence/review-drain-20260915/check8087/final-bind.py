from pathlib import Path
import json,hashlib,subprocess,sys
r=Path('/private/tmp/review-drain-20260915');w=r/'author-slot-one';sys.path.insert(0,str(w/'scripts'));import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
record=json.loads((r/'8087-unit-v1-preexecution-fixed-method.json').read_text());report=json.loads((r/'review-8087-preexecution-fixed-method.json').read_text());receipt=json.loads((r/'8087-execution-native_growing_formation_current_2026_09_13.json').read_text());result=receipt['result'];tree='1233fde43c326de9e6f4ccaa63b1fd272eea4d6e'
assert git('write-tree')==tree and result['exit_code']==0 and result['status']=='ok' and result['stderr']=='' and result['elapsed_sec']<180
assert receipt['preexecution_record_sha256']==sha(r/'8087-unit-v1-preexecution-fixed-method.json')
cache=Path(receipt['cache_path']);assert sha(cache)==receipt['cache_sha256'];assert runner_cache.cache_status(receipt['runner'])=='fresh'
assert result['stdout'].rstrip().endswith('TOTAL: PASS=472 FAIL=0') and result['stdout'] in cache.read_text()
for x in record['source']['paths']:
 if x['path'].startswith('logs/runner-cache/'):
  x['sha256']=sha(w/x['path'])
 else:assert sha(w/x['path'])==x['sha256']
 assert hashlib.sha256(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']])).hexdigest()==x['sha256']
for rows in record['inputs'].values():
 for x in rows:assert sha(w/x['path'])==x['sha256']
payload=json.JSONDecoder().raw_decode(result['stdout'])[0];counts={k:len(v['checks']) for k,v in payload['checks'].items()};assert counts=={'native':83,'transport':327,'growth':62}
oldtext=(r/'check8087/original/logs/runner-cache/native_growing_formation_current_2026_09_13.txt').read_text();old=json.JSONDecoder().raw_decode(oldtext[oldtext.index('{'):])[0];diffs=[]
def compare(a,b,p=''):
 if isinstance(a,dict):
  assert a.keys()==b.keys(),p
  for k in a:
   if k not in ['seconds','source_sha256','note_sha256']:compare(a[k],b[k],p+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(b),p
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,p+'/'+str(i))
 elif a!=b:
  assert isinstance(a,float) and isinstance(b,float),(p,a,b)
  diffs.append({'path':p,'old':a,'new':b,'absolute_difference':abs(a-b)})
compare(old,payload)
comparison=r/'8087-reviewer-payload-comparison.json';assert not comparison.exists();comparison.write_text(json.dumps({'excluded_fields':['seconds','source_sha256','note_sha256'],'differences':diffs,'nonfloating_math_fields':'identical','counts':counts},indent=2)+'\n')
report.update(status='PASS_WITH_BOUNDED_CLAIMS',final_verdict='PASS WITH BOUNDED CLAIMS',source_tree=tree,source_paths=record['source']['paths'],execution={'receipt':str(r/'8087-execution-native_growing_formation_current_2026_09_13.json'),'total_pass':472,'total_fail':0,'counts':counts,'elapsed_sec':result['elapsed_sec'],'timeout_sec':180,'cache_sha256':sha(cache)},final_confirmation='Only expected cache bytes changed after fixed-context source freeze. All actual runtime/helper/parent/context/tooling hashes and staged source verified. Exact original mathematical payload compared; metadata/time excluded and floating differences separately preserved. Full prior independent proof controls and historical recovery remain applicable. No full pipeline or audit verdict generated.')
for row in report['original_dispositions']:
 if row.get('final_path')==str(cache.relative_to(w)):row['final_sha256']=sha(cache);row['disposition']='Canonical cache regenerated exactly once from frozen final source; original recovered at frozen original head.'
reportfile=r/'review-8087-final.json';assert not reportfile.exists();reportfile.write_text(json.dumps(report,indent=2)+'\n');ref={'path':str(reportfile),'sha256':sha(reportfile)}
record['unit_id']='pr8087-final';record['source']['tree']=tree;record['reviewer']['report']=ref
for c in record['constituents']:c['dispositions']=dict(ref,json_pointer='/original_dispositions')
for x in record['non_science_notes']:x['review_reference']=ref
record['reviewer']['references'] += [{'path':str(r/p),'sha256':sha(r/p)} for p in ['8087-unit-v1-preexecution-fixed-method.json','review-8087-preexecution-fixed-method.json','8087-preexecution-preflight-fixed-method.json','8087-execution-native_growing_formation_current_2026_09_13.json','8087-author-capture.py','8087-author-capture.log','8087-reviewer-payload-comparison.json']]
record['boundary']='Final source review PASS WITH BOUNDED CLAIMS, bound to exact source and one actual472/0 capture. Mechanical final preflight and combined integration remain separate; no audit verdict.'
f=r/'8087-unit-v1-final.json';assert not f.exists();f.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'tree':tree,'report_sha256':sha(reportfile),'record_sha256':sha(f),'floating_differences':len(diffs),'max_float_difference':max([x['absolute_difference'] for x in diffs],default=0)},indent=2))
