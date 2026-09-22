import pathlib,json,hashlib,subprocess,gzip,sys,re
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'drain-author-slot'
def sh(b):return hashlib.sha256(b).hexdigest()
def load(n):return json.loads((r/n).read_text())
def git(*a):return subprocess.check_output(['git','-C',str(w),*a])
cold=load('drain8150-preexecution-review.json');freeze=load('drain8150-author-final-freeze.json');assert git('write-tree').decode().strip()==freeze['tree']=='2d2b9031ee7c0ef7d8724f9caffa9671fc659445';assert not git('diff','--name-only')
changed=git('diff','--name-status',cold['source']['tree'],freeze['tree']).decode().splitlines();assert len(changed)==3 and all(x.startswith('A\tlogs/runner-cache/') for x in changed)
for x in cold['source']['paths']:assert sh((w/x['path']).read_bytes())==x['sha256']
for items in cold['inputs'].values():
 for x in items:assert sh((w/x['path']).read_bytes())==x['sha256']
for p,h in freeze['source_paths'].items():assert sh((w/p).read_bytes())==h
sys.path.insert(0,str(w/'scripts'));import runner_cache as c
runs=[]
for pr,count in [(8148,22),(8149,18),(8150,17)]:
 e=load(f'drain8150-execution-{pr}.json');assert e['exit_code']==0 and e['status']=='ok' and not e['stderr'];assert f'TOTAL: PASS={count} FAIL=0' in e['stdout'];assert e['elapsed_sec']<e['timeout_sec']==300
 watch=e['whole_tree_watchdog'];assert not watch['violations'] and watch['samples']>0 and watch['peak_tree_rss_bytes']<watch['limit_bytes']==3221225472
 assert sh((r/'drain8150-capture.py').read_bytes())==e['capture_script_sha256'];assert c.cache_status(w/e['runner'])=='fresh'
 p='logs/runner-cache/'+pathlib.Path(e['runner']).stem+'.txt';t=(w/p).read_text();assert e['stdout'].strip() in t;fp=c.declared_input_fingerprint(w/e['runner']);assert fp in t
 old=next((r/'drain8150-originals'/str(pr)/'logs/runner-cache').glob('*.txt')).read_text()
 # Compare all numerical tokens in B-E actual check lines. Source-label changes do not alter mathematics.
 def vals(s):return [re.findall(r'\d+(?:\.\d+)?',line.split(' ',2)[-1]) for line in s.splitlines() if re.match(r'PASS: [BCDE]\d+ ',line)]
 a,b=vals(old),vals(e['stdout']);differences=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y];assert len(a)==len(b)
 # Unit C3/E1 label correction intentionally changes stated coverage numbers, retained exact numerical results are unchanged.
 runs.append(dict(pr=pr,pass_count=count,elapsed_sec=e['elapsed_sec'],timeout_sec=300,watchdog=watch,cache_path=p,cache_sha256=sh((w/p).read_bytes()),input_fingerprint=fp,cache_status='fresh',numerical_token_label_difference_indices=differences))
for row in cold['original_dispositions']:
 assert sh(gzip.decompress((w/row['final_path']).read_bytes()))==row['original_sha256']
 if row['original_path'].startswith('logs/runner-cache/'):
  run=next(x for x in runs if x['pr']==row['pr']);row['current_execution_cache']={'path':run['cache_path'],'sha256':run['cache_sha256']};row['disposition']+=' Original cache is historical only; the current fresh execution cache supersedes it for the narrowed live source.'
refs=cold['references'][:]
for name in ['drain8150-preexecution-review.json','drain8150-capture.py','drain8150-author-final-freeze.json']+[f'drain8150-execution-{p}.json' for p in [8148,8149,8150]]:
 refs.append({'path':str(r/name),'sha256':sh((r/name).read_bytes())})
out=dict(cold);out.update(status='FINAL SOURCE PASS: PARTIAL POSITIVE SALVAGE ONLY',source={'base':freeze['base'],'commit':freeze['base'],'tree':freeze['tree'],'paths':[{'path':p,'sha256':h} for p,h in freeze['source_paths'].items()],'deleted_paths':[]},executions=runs,references=refs,final_scope='Retain only the revised conditional positive identities, sufficient constructions and finite witnesses. Universal exclusions/necessity certifications are deferred, not passed or disproved. Preserve all three original branches and exact archived proofs. No audit verdict.',output_assessment='All totals, finite numerical outputs and scope lines read against unchanged arithmetic. Historical negative-sounding E2/E4 labels in rate stdout describe the displayed plaquette identities; they are not a completed negative-certificate verdict and cannot promote the explicitly deferred canonical universal claims. No changed scientific threshold or rerun.',final_cache_preflight_owner='root; this reviewer checked the lightweight cache freshness API only, not a duplicate versioned preflight.')
out.pop('allowed_capture',None)
p=r/'drain8150-final-review.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
(r/'drain8150-final-review.md').write_text('# PR8148–8150 final source review\n\nPASS for partial positive salvage at tree `'+freeze['tree']+'`. The three captures passed 22/18/17 checks, respectively, within 300 seconds and 3 GiB sampled process-tree RSS. Only the three fresh caches changed after cold confirmation; all source and input bytes remained fixed.\n\nAll 66 original versions remain recoverable. Universal negative certification and the arbitrary fixed-boundary converse remain deferred; preserve the original branches. This is no audit verdict. Root owns the sole final versioned cache preflight.\n')
print(json.dumps({'report_sha256':sh(p.read_bytes()),'tree':freeze['tree'],'outputs':runs},indent=2))
