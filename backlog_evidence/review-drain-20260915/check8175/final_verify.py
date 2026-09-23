import pathlib,json,hashlib,subprocess,re
r=pathlib.Path('/private/tmp/review-drain-20260915'); w=r/'drain-author-slot'; main='e46c78efd91d00c8a96ea4f11ea8bc5a8e3ed0e6'
sha=lambda b:hashlib.sha256(b).hexdigest(); read=lambda n:json.loads((r/n).read_text());git=lambda *a:subprocess.check_output(['git','-C',str(w),*a])
f=read('drain8175-author-final-freeze.json');assert sha((r/'drain8175-author-final-freeze.json').read_bytes())=='e43802a1b91eebed5f21198202642cae8b397f08d03147b4df3bfdea9f819f1a'
assert git('write-tree').decode().strip()==f['tree'];assert not git('diff','--name-only')
assert set(git('diff','--cached','--name-only').decode().splitlines())==set(f['source_paths'])
source=[]
for p,h in f['source_paths'].items():
 assert sha((w/p).read_bytes())==sha(git('show',':'+p))==h
 mode,blob,stage=git('ls-files','-s','--',p).decode().split('\t')[0].split();assert mode=='100644';source.append({'path':p,'sha256':h,'mode':mode,'blob':blob})
maininputs={}
for p,h in f['inputs'].items():
 assert sha((w/p).read_bytes())==h
 if p not in f['source_paths']:
  assert sha(git('show',main+':'+p))==h;maininputs[p]=h
changed=git('diff','--name-only',f['base'],main).decode().splitlines();assert not set(changed)&set(f['source_paths'])
refs={}
def checkrefs(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x and str(x['path']).startswith(str(r)):
   p=pathlib.Path(x['path']);assert sha(p.read_bytes())==x['sha256'];refs[str(p)]=x['sha256']
  for v in x.values():checkrefs(v)
 elif isinstance(x,list):
  for v in x:checkrefs(v)
e=read('drain8175-execution-v2.json');m=read('drain8175-mutation-period_counts_wrong-v1.json');checkrefs(e);checkrefs(m)
for ex in f['executions']:assert sha(pathlib.Path(ex['receipt']).read_bytes())==ex['sha256'];refs[ex['receipt']]=ex['sha256']
assert e['before']==e['after'];assert m['before']==m['after'];assert not e['error'] and not m['error']
raw=read('drain8175-raw-result-v2.json');print('raw keys',list(raw))
res=e['result']['result'];assert res['exit_code']==0 and not res['stderr'] and res['stdout'].count('PASS: ')==20 and 'TOTAL: PASS=20 FAIL=0' in res['stdout'];assert res==raw
ms=(r/'drain8175-mutation-period_counts_wrong-v1.stdout.txt').read_text();assert re.findall(r'^FAIL: (\w+)',ms,re.M)==['B3'];assert ms.count('PASS: ')==19 and 'TOTAL: PASS=19 FAIL=1' in ms
for receipt in [e,m]:assert not receipt['whole_tree_watchdog']['violations'];assert receipt['elapsed_seconds']<60;assert receipt['whole_tree_watchdog']['peak_tree_rss_bytes']<402653184
out={'verified':True,'source':source,'current_main':main,'main_inputs':maininputs,'intervening_paths':changed,'references':refs,'resources':{'primary':{'wall_seconds':e['elapsed_seconds'],'sampled_peak_rss_bytes':e['whole_tree_watchdog']['peak_tree_rss_bytes']},'mutation':{'wall_seconds':m['elapsed_seconds'],'sampled_peak_rss_bytes':m['whole_tree_watchdog']['peak_tree_rss_bytes']}}}
(r/'check8175/final_verify.json').write_text(json.dumps(out,indent=2)+'\n');print('VERIFIED',len(source),'source paths',len(maininputs),'unchanged main inputs')
