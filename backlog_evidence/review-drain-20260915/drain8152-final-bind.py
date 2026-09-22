import json,pathlib,hashlib,gzip,subprocess
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'author-draft-slot'
def read(n):return json.loads((r/n).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(w),*a])
f=read('drain8152-author-final-freeze.json');c=read('drain8152-cold-confirmation-v2.json');o=read('drain8152-original-review.json');h=read('drain8152-author-source-handoff-v1.json');e=read('drain8152-execution-8152.json');p=read('drain8152-phrase-repair-v2.json')
assert git('write-tree').decode().strip()==f['tree']=='5e5a612454c64cfbb315bf721bb0fa45d0055b07'
assert not git('diff','--name-only')
for path,digest in f['source_paths'].items():
 assert sha((w/path).read_bytes())==digest
 assert sha(git('show',':'+path))==digest
for path,digest in c['source_hashes'].items():assert f['source_paths'][path]==digest
extra=set(f['source_paths'])-set(c['source_hashes']);assert len(extra)==1
cache=next(iter(extra));assert cache.startswith('logs/runner-cache/')
for path,digest in f['inputs'].items():assert sha((w/path).read_bytes())==digest
for rows in c['inputs'].values():
 for row in rows:assert sha((w/row['path']).read_bytes())==row['sha256']
assert e['status']=='ok' and e['exit_code']==0 and not e['stderr'] and 'TOTAL: PASS=15 FAIL=0' in e['stdout']
assert e['elapsed_sec']<e['timeout_sec']==60
v=e['whole_tree_watchdog'];assert not v['violations'] and v['peak_tree_rss_bytes']<v['limit_bytes']==512*1024**2
assert sha(pathlib.Path(e['capture_script']).read_bytes())==e['capture_script_sha256']
s=(w/cache).read_text();assert e['stdout'] in s and p['declared_input_fingerprint'] in s and f['source_paths'][e['runner']] in s
mapped={x['original_path']:x for x in h['original_dispositions']};rows=[]
for old in o['original_dispositions']:
 m=mapped[old['original_path']];b=(w/m['final_path']).read_bytes();assert sha(b)==m['final_sha256'];assert sha(gzip.decompress(b))==old['original_sha256']
 rows.append({**old,'final_path':m['final_path'],'final_sha256':m['final_sha256'],'retention':'Exact original gzip recovery; historical verdicts are not current authority.'})
assert len(rows)==22
refs={}
for n in ['drain8152-original-review.json','drain8152-cold-findings-v1.json','drain8152-cold-confirmation-v2.json','drain8152-author-unit-draft-v2.json','drain8152-phrase-repair-v2.json','drain8152-author-final-freeze.json','drain8152-execution-8152.json','drain8152-independent-control.json']:
 refs[n]={'path':str(r/n),'sha256':sha((r/n).read_bytes())}
out={'status':'FINAL SOURCE PASS — POSITIVE CONSTRUCTIONS ONLY','reviewer':'/root/review_8012','head':o['head'],'delta_base':o['delta_base'],'base':f['base'],'tree':f['tree'],'source_hashes':f['source_paths'],'inputs':c['inputs'],'final_input_hashes':f['inputs'],'original_dispositions':rows,'accepted_claims':['Normalized equivariant frame and supplied finite Borel atomic-kernel constructions on fixed ordered noncollinear slots, with explicit weights and extra coordinates.','Five cube-orbit examples and invariant supplied orbit laws/mixtures, without exhaustive or minimal certification.','Induction for an explicitly supplied antipodal kernel and one-previous-neighbor order.','Aligned and tilted overlap evaluations, without selecting formation probabilities.'],'deferred_claims':['Exhaustive support/menu classification and minimality/negative certification remain deferred; no N1–N8 PASS.','Original general seed-generation and Born-support assertions are withdrawn/corrected, not premises of accepted constructions.'],'closure':{'disposition':'partial positive salvage','preserve_original_branch':True,'reason':'Unique original negative certification remains deferred; exact full original recovery does not establish those claims.'},'evidence':{'total_pass':15,'total_fail':0,'count_scope':'Grouped authority, finite mathematical, text and resolution checks; not 15 independent mathematical proofs.','elapsed_sec':e['elapsed_sec'],'timeout_sec':60,'peak_tree_rss_bytes':v['peak_tree_rss_bytes'],'rss_limit_bytes':v['limit_bytes'],'cache':cache,'cache_sha256':sha((w/cache).read_bytes()),'input_fingerprint':p['declared_input_fingerprint'],'capture_script_sha256':e['capture_script_sha256'],'source_unchanged_since_cold':True,'only_added_path':cache},'main_interaction':c['main_interaction'],'references':refs,'boundary':'No primary/control/preflight rerun. Root owns canonical final schema2 record from v2 and sole final --cache. This is source review, not an audit verdict.'}
path=r/'drain8152-final-review.json';assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n');print(path,sha(path.read_bytes()))
