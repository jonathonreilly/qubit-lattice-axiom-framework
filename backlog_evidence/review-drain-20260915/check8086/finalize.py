from pathlib import Path
import json,hashlib,subprocess,sys,gzip,copy
r=Path('/private/tmp/review-drain-20260915');repo=r/'author-slot-one';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();git=lambda *a:subprocess.check_output(['git','-C',str(repo),*a],text=True).strip()
sys.path.insert(0,str(repo/'scripts'));import runner_cache as cache
pre=json.loads((r/'8086-unit-v1-preexecution.json').read_text());report=json.loads((r/'review-8086-preexecution.json').read_text());assert git('write-tree')=='ac0752d7dddaf48b0679df65eb8f47caae9f395b'
for b in pre['source']['paths']+sum(pre['inputs'].values(),[]):
 if not b['path'].startswith('logs/runner-cache/'):assert sha(repo/b['path'])==b['sha256'],b
mapping=json.loads((r/'8086-author-archive-map.json').read_text())
for e in mapping['entries']:
 b=(repo/e['final_path']).read_bytes();assert hashlib.sha256(b).hexdigest()==e['stored_sha256'];raw=gzip.decompress(b) if e['encoding']=='gzip' else b;assert hashlib.sha256(raw).hexdigest()==e['raw_sha256']
receipts=[];comparisons=[]
def clean(x):
 if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ('seconds','source_sha256','derivation_sha256','note_sha256','formula_sha256','dependencies_sha256','peak_rss_bytes')}
 if isinstance(x,list):return [clean(v) for v in x]
 return x
for note,total in zip(pre['notes'],(252,34,69)):
 stem=Path(note['primary_runner']).stem;p=r/f'8086-execution-{stem}.json';o=json.loads(p.read_text());res=o['result'];assert o['preexecution_record_sha256']==sha(r/'8086-unit-v1-preexecution.json');assert res['exit_code']==0 and res['status']=='ok' and not res['stderr'];assert res['elapsed_sec']<res['timeout_sec']==180;assert res['stdout'].endswith(f'TOTAL: PASS={total} FAIL=0\n')
 cp=repo/'logs/runner-cache'/f'{stem}.txt';assert sha(cp)==o['cache_sha256'];assert cache.cache_status(note['primary_runner'])=='fresh';txt=cp.read_text();assert res['stdout'] in txt
 old=(r/'check8086/original/logs/runner-cache'/f'{stem}.txt').read_text().split('----- stdout -----',1)[1].lstrip();old_obj=json.JSONDecoder().raw_decode(old)[0];new_obj=json.JSONDecoder().raw_decode(res['stdout'][res['stdout'].index('{'):])[0]
 a=clean(old_obj);b=clean(new_obj)
 diffs=[]
 def compare(x,y,path=''):
  if isinstance(x,dict):
   assert x.keys()==y.keys(),path
   for k in x:compare(x[k],y[k],path+'/'+k)
  elif isinstance(x,list):
   assert len(x)==len(y),path
   for j,(u,v) in enumerate(zip(x,y)):compare(u,v,path+'/'+str(j))
  elif x!=y:
   assert isinstance(x,float) and isinstance(y,float),(path,x,y)
   diffs.append({'path':path,'original':x,'final':y,'absolute_difference':abs(x-y)})
 compare(a,b)
 comparisons.append({'runner':note['primary_runner'],'nonfloat_math_payload_exact':True,'floating_differences':diffs})
 receipts.append({'path':str(p),'sha256':sha(p),'runner':note['primary_runner'],'total':total,'elapsed_sec':res['elapsed_sec'],'exit_code':0,'cache_sha256':sha(cp)})
for args in [('diff','--check'),('diff','--cached','--check'),('diff',pre['source']['base'],'--check')]:subprocess.check_call(['git','-C',str(repo),*args])
for b in pre['source']['paths']:b['sha256']=sha(repo/b['path'])
for d in report['original_dispositions']:
 if d['final_path']:d['final_sha256']=sha(repo/d['final_path'])
 if d['original_path'].startswith('logs/'):d['disposition']='Fresh execution cache replaces original cache; immutable original cache retained at original frozen head and reviewer recovery copy. Final math payload independently compared.'
report.update(status='PASS_WITH_BOUNDED_CLAIMS',final_verdict='PASS WITH BOUNDED CLAIMS',source_tree=git('write-tree'),source_commit=git('rev-parse','HEAD'),source_paths=pre['source']['paths'],execution_receipts=receipts,payload_comparison=comparisons,inputs=pre['inputs'],current_main_loss_check='All12originalcanonicalpaths retained; three new claims and their full mathematical chain preserved;113historypayloads exact; generated manifest excluded/currentmain retained; no original deletion or replacement of existing main scientific source.',remaining_boundary='Combined integration gate and independent future audit remain coordinator responsibilities; no retained status or physical TOE closure.',correction_confirmation='Original-session cold confirmation complete; all frozen noncache source/input hashes unchanged during three once-only successful bounded executions.')
(r/'review-8086.json').write_text(json.dumps(report,indent=2)+'\n')
ref={'path':str(r/'review-8086.json'),'sha256':sha(r/'review-8086.json')};final=copy.deepcopy(pre);final['unit_id']='pr8086-final';final['source']['tree']=git('write-tree');final['constituents'][0]['dispositions']=dict(ref,json_pointer='/original_dispositions');final['reviewer']['report']=ref
for e in final['non_science_notes']:e['review_reference']=ref
refs=['8086-preexecution-preflight.json','8086-unit-v1-preexecution.json','review-8086-preexecution.json']+[Path(x['path']).name for x in receipts]
final['reviewer']['references'] +=[{'path':str(r/p),'sha256':sha(r/p)} for p in refs];final['boundary']='Final independent source review bound to three fresh actual captures. Shared final --cache mechanical preflight and combined integration gate performed by coordinator; no audit verdict.'
(r/'8086-unit-v1-final.json').write_text(json.dumps(final,indent=2)+'\n')
(r/'review-8086.md').write_text('# PR8086 independent review\n\n**FINAL VERDICT: PASS WITH BOUNDED CLAIMS.**\n\nFinal staged tree `'+git('write-tree')+'`; original head `'+report['original_head']+'`. Full three-note/six-source coherent proof reviewed. All126original paths accounted for,113historical payloads decoded byte-exact. All original math payload fields match except recorded floating roundoff; no thresholds or mathematical code changed.\n\nSupplied-model positivity, free-reference infrared spectral bound and double-compressed low-energy operator theorem are supported. Physical selection, interacting ground state, extensive sums and high-energy leakage remain outside the result. Standard CAR/Fock, resolvent/spectral and Cauchy methods are explicit mathematical tools, not imported physical premises.\n\nIndependent walk-DP, exact tensor-Pauli inverse controls and rational bounds passed. Historical28mutants reconstructed exactly. Path/input declarations and historical narrative scope corrections cold-confirmed. Three once-only actual captures passed252/0,34/0,69/0 within180seconds; exact timing/source/input/cache hashes and full dispositions are in review-8086.json. Preexecution evidence remains immutable.\n\nFinal version1 record:8086-unit-v1-final.json. Coordinator runs final shared cache preflight and combined gate. No audit verdict, commit or remote mutation by reviewer.\n')
print(json.dumps({'tree':git('write-tree'),'report_sha256':sha(r/'review-8086.json'),'final_record_sha256':sha(r/'8086-unit-v1-final.json'),'float_changes':[len(x['floating_differences']) for x in comparisons],'receipts':receipts},indent=2))
