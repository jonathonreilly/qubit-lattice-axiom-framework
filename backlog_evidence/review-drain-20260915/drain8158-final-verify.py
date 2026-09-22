import pathlib,json,hashlib,subprocess,sys
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot';load=lambda n:json.loads((r/n).read_text());sha=lambda b:hashlib.sha256(b).hexdigest();git=lambda *a:subprocess.check_output(['git','-C',str(w),*a])
cold=load('drain8158-cold-confirmation-v1.json');f=load('drain8158-author-final-freeze.json');e=load('drain8158-execution-8158.json')
assert git('write-tree').decode().strip()==f['tree'];assert git('rev-parse','HEAD').decode().strip()==f['base']
for p,h in f['source_paths'].items():assert sha((w/p).read_bytes())==h;assert git('show',':'+p)==(w/p).read_bytes()
for x in cold['source']['paths']:assert f['source_paths'][x['path']]==x['sha256']
cache=set(f['source_paths'])-{x['path'] for x in cold['source']['paths']};assert len(cache)==1;cache=cache.pop();assert cache.startswith('logs/runner-cache/')
for rows in cold['inputs'].values():
 for x in rows:assert sha((w/x['path']).read_bytes())==x['sha256']
assert set(git('diff','--cached','--name-only').decode().splitlines())==set(f['source_paths'])
assert e['status']=='ok' and e['exit_code']==0 and not e['stderr'];assert e['stdout'].endswith('TOTAL: PASS=20 FAIL=0\n');assert sum(x.startswith('PASS: ')for x in e['stdout'].splitlines())==20
assert e['timeout_sec']==180 and e['elapsed_sec']<180;watch=e['whole_tree_watchdog'];assert watch['limit_bytes']==1073741824 and not watch['violations'] and watch['peak_tree_rss_bytes']<watch['limit_bytes'];assert sha((r/'drain8158-capture.py').read_bytes())==e['capture_script_sha256']
assert e['stdout'] in (w/cache).read_text()
sys.path.insert(0,str(w/'scripts'));import runner_cache as rc
assert rc.cache_status(w/e['runner'])=='fresh';assert rc.declared_input_fingerprint(w/e['runner'])==cold['input_fingerprint']
for a in [('diff','--check'),('diff','--cached','--check'),('diff',f['base'],'--check')]:subprocess.run(['git','-C',str(w),*a],check=True)
out={**cold,'status':'FINAL SOURCE PASS WITH BOUNDED POSITIVE CLAIMS; PARTIAL SALVAGE ONLY; NO AUDIT VERDICT','source':{'base':f['base'],'commit':f['base'],'tree':f['tree'],'paths':[{'path':p,'sha256':h}for p,h in f['source_paths'].items()],'deleted_paths':[]},'source_paths':f['source_paths'],'execution':e,'final_evidence_confirmation':'Only one new canonical cache after cold26-path freeze. All source/input hashes unchanged; cache stdout matches actual20/0 receipt, fingerprint fresh. Mathematical calculations unchanged; abstract-graph and scope wording corrections accurately reflected. All22 originals remain exact bound historical recovery; current-main preservation unchanged.','closure':'Accept only finite supplied-model factorization/attachment formulas/identified finite witnesses and uniform linear averaging. Defer universal attachment iff and all-axiom models/physical reading certification; preserve original branch.','final_cache_preflight':'Root owns sole final schema2 --cache check; this reviewer performed only read-only runner_cache.cache_status, no primary or shared preflight rerun.'}
out.pop('permitted_capture',None)
out['references']=cold['references']+[{'path':str(r/p),'sha256':sha((r/p).read_bytes())}for p in ['drain8158-cold-confirmation-v1.json','drain8158-execution-8158.json','drain8158-author-final-freeze.json','drain8158-capture.py']]
p=r/'drain8158-final-review.json';p.open('x').write(json.dumps(out,indent=2)+'\n');print(sha(p.read_bytes()))
(r/'drain8158-final-review.md').open('x').write('# PR8158 final source review\n\nPASS with bounded positive claims; partial salvage only. Exact source tree `'+f['tree']+'`. All27 source paths and22 original dispositions bound in JSON. Sole capture20/0,7.192633s, sampled peak197951488bytes under180s/1GiB. Source and inputs unchanged; new cache fresh.\n\nUniversal graph converse and all-axiom/physical-reading certification remain deferred; preserve original branch. No audit verdict or primary rerun.\n')
