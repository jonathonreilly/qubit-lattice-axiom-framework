from pathlib import Path
import json,hashlib,subprocess,sys,gzip
r=Path('/private/tmp/review-drain-20260915');w=r/'author-slot-one';sys.path.insert(0,str(w/'scripts'));import runner_cache
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();hb=lambda b:hashlib.sha256(b).hexdigest()
git=lambda *a:subprocess.check_output(['git','-C',str(w),*a],text=True).strip()
record=json.loads((r/'8094-unit-v1-preexecution.json').read_text());report=json.loads((r/'review-8094-preexecution.json').read_text());tree='025c01c9dda284cf8a0936a00c23713ec1aad222'
assert git('write-tree')==tree
latest=git('rev-parse','origin/main');base=record['source']['base']
for rows in record['inputs'].values():
 for x in rows:
  assert sha(w/x['path'])==x['sha256']
  exists=subprocess.run(['git','-C',str(w),'cat-file','-e',base+':'+x['path']],capture_output=True).returncode==0
  if exists:assert hb(subprocess.check_output(['git','-C',str(w),'show',latest+':'+x['path']]))==x['sha256'],x['path']
expected={n['primary_runner'].removeprefix('scripts/').removesuffix('.py') for n in record['notes']}
allowed={'outputs/'+s+'.json' for s in expected}|{'logs/runner-cache/'+s+'.txt' for s in expected}
for x in record['source']['paths']:
 if x['path'] in allowed:x['sha256']=sha(w/x['path'])
 else:assert sha(w/x['path'])==x['sha256']
 assert hb(subprocess.check_output(['git','-C',str(w),'show',':'+x['path']]))==x['sha256']
for e in report['archive_entries']:
 raw=(w/e['final_path']).read_bytes();raw=gzip.decompress(raw) if e['encoding']=='gzip' else raw
 assert raw==(r/f"check8094/original-{e['number']}"/e['original_path']).read_bytes()
differences=[]
def compare(a,b,path):
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
  assert abs(a-b)<=1e-10*(1+abs(a)),(path,a,b)
  differences.append(dict(path=path,old=a,new=b,absolute_difference=abs(a-b)))
refs=[];executions=[]
for n,count,stem in [(8091,218,'native_lapse_source_contact_response_2026_09_13'),(8092,423,'native_common_frame_spin_connection_2026_09_13'),(8094,133,'native_weyl_stress_logarithm_contact_response_2026_09_13')]:
 receiptpath=r/('8094-execution-'+stem+'.json');receipt=json.loads(receiptpath.read_text());res=receipt['result'];cache=Path(receipt['cache_path']);saved=r/('8094-original-output-'+stem+'.json');out=w/receipt['output_path']
 assert receipt['preexecution_record_sha256']==sha(r/'8094-unit-v1-preexecution.json')
 assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<60 and receipt['limit_sec']==60
 assert sha(cache)==receipt['cache_sha256'] and runner_cache.cache_status(receipt['runner'])=='fresh'
 assert res['stdout'] in cache.read_text() and f'TOTAL: PASS={count} FAIL=0' in res['stdout']
 assert sha(out)==receipt['output_sha256'] and sha(saved)==receipt['original_output_sha256']
 original=r/f'check8094/original-{n}'/receipt['output_path'];assert saved.read_bytes()==original.read_bytes()
 old=json.loads(original.read_text());new=json.loads(out.read_text());compare(old,new,stem)
 if n==8091:assert sum(x['checks'] for x in new.values())==count and all(x['status']=='PASS' for x in new.values())
 elif n==8092:assert new['checks']==count and new['status']=='PASS'
 else:assert new['check_count']==count and new['status']=='ok'
 executions.append(dict(runner=receipt['runner'],total_pass=count,total_fail=0,elapsed_sec=res['elapsed_sec'],timeout_sec=60,cache_sha256=sha(cache),output_sha256=sha(out)))
 refs += [receiptpath,saved,r/('8094-execution-'+stem+'-started.json')]
comparison=r/'8094-reviewer-payload-comparison.json';assert not comparison.exists();comparison.write_text(json.dumps(dict(excluded_metadata=['elapsed_seconds','source_sha256'],differences=differences,boundary='Exact structural and nonfloat comparison. Float differences checked against1e-10 relative-plus-absolute bound only for evidence comparison; no primary tolerance changed.'),indent=2)+'\n')
for rows in report['original_dispositions'].values():
 for x in rows:
  p=x['final_path']
  if p in allowed:x['final_sha256']=sha(w/p);x['disposition']='Fresh designated canonical output/cache from one bounded capture; original output saved byte-exact outside checkout and all original bytes recoverable at frozen constituent head.'
report.update(status='PASS_WITH_BOUNDED_CLAIMS',final_verdict='PASS WITH BOUNDED CLAIMS',source_tree=tree,source_paths=record['source']['paths'],executions=executions,remaining=[],current_main_context={'commit':latest,'assessment':'All inherited runtime, repository premise, mandatory authority and methodology/tooling inputs match current main exactly. Shared native code and supplied free source/frame hypotheses remain unchanged; the three notes reconstruct their interacting lapse/frame/stress steps without hidden sibling proof imports.'},final_confirmation='All291 staged source paths and363 original dispositions bound; exact decoded archives retained. One capture per primary218/423/133 checks,60second caps. All other source/input bytes unchanged. Seven independent controls passed. This is source review only; no audit verdict or combined integration gate is inferred.')
final=r/'review-8094-final.json';assert not final.exists();final.write_text(json.dumps(report,indent=2)+'\n');ref=dict(path=str(final),sha256=sha(final))
record['unit_id']='pr8091-8092-8094-final';record['source']['tree']=tree;record['reviewer']['report']=ref
for c in record['constituents']:c['dispositions']=dict(ref,json_pointer='/original_dispositions/'+c['id'])
for x in record['non_science_notes']:x['review_reference']=ref
refs += [r/'8094-unit-v1-preexecution.json',r/'review-8094-preexecution.json',r/'8094-preexecution-preflight.json',r/'8094-author-capture.py',r/'8094-author-capture.log',comparison]
record['reviewer']['references'] += [dict(path=str(p),sha256=sha(p)) for p in refs]
record['boundary']='Final source PASS WITH BOUNDED CLAIMS. Shared cache validation and combined integration are separate; no full dynamical gravity, source-law selection or audit verdict.'
fp=r/'8094-unit-v1-final.json';assert not fp.exists();fp.write_text(json.dumps(record,indent=2)+'\n')
md=r/'review-8094.md';assert not md.exists();md.write_text('# PR8091 + PR8092 + PR8094 independent source review\n\n**PASS WITH BOUNDED CLAIMS** at tree `'+tree+'`.\n\nReviewed all three proofs/primaries and363 original paths, including historical failures and73 exact mutation variants. Seven independent controls passed. Actual captures completed once each:218/0,423/0,133/0 under60second caps. Source/input bytes stayed frozen except designated outputs/caches; all original outputs preserved.\n\nThe conclusions concern supplied free lapse/frame/stress models and explicit contact families. They do not select physical geometry or prove full gravitational dynamics. External spin geometry is reconstructed; Osborn–Petkou is a normalization comparator.\n\nFinal report SHA256: `'+sha(final)+'`. Final v1 record SHA256: `'+sha(fp)+'`. Combined integration and audit remain separate.\n')
print(json.dumps(dict(tree=tree,report_sha256=sha(final),record_sha256=sha(fp),float_differences=len(differences),maximum_float_difference=max([x['absolute_difference'] for x in differences],default=0),latest_main=latest),indent=2))
