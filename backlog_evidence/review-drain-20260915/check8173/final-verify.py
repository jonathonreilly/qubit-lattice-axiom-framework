import pathlib,json,hashlib,subprocess,gzip,ast,re
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(W),*a])
fpath=R/'drain8173-author-final-freeze.json';assert sha(fpath)=='5ac4b03b2c92b401eace32b67df83c80ea788a3eb038dfd705fbcf698e108203';f=json.loads(fpath.read_text());assert git('rev-parse','HEAD').decode().strip()==f['base'];assert not git('diff','--cached','--name-only',f['tree']);assert not git('diff','--name-only')
rows=[]
for p,h in f['source_paths'].items():
 assert sha(W/p)==h==hashlib.sha256(git('show',':'+p)).hexdigest();info=git('ls-files','--stage','--',p).decode().split();rows.append(dict(path=p,mode=info[0],blob=info[1],sha256=h))
assert len(rows)==26
for p,h in f['inputs'].items():assert sha(W/p)==h
old=json.loads((R/'drain8173-author-prepared-v3.json').read_text())
for e in old['source']:assert f['source_paths'][e['path']]==e['sha256'];assert next(x['mode'] for x in rows if x['path']==e['path'])==e['mode']
m=json.loads((W/'docs/work_history/review_loop/pr8173/pr8173-original-manifest.json').read_text());assert len(m['entries'])==20
for e in m['entries']:assert hashlib.sha256(gzip.decompress((W/e['recovery']['path']).read_bytes())).hexdigest()==e['original_sha256']
b=json.loads((R/'drain8173-capture-binding-v2.json').read_text())
for e in b['adapters']:
 for k in ['old','new','diff']:assert sha(pathlib.Path(e[k]['path']))==e[k]['sha256']
 oldt=ast.parse(pathlib.Path(e['old']['path']).read_text());newt=ast.parse(pathlib.Path(e['new']['path']).read_text())
 for t in [oldt,newt]:
  for n in t.body:
   if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='COLD_CLEARANCE_BINDING' for x in n.targets):n.value=ast.Constant(None)
 assert ast.dump(oldt)==ast.dump(newt)
assert sha(pathlib.Path(b['binding']['path']))==b['binding']['sha256']
stats=[];refs=[]
for e in f['executions']:
 p=pathlib.Path(e['receipt']);assert sha(p)==e['sha256'];d=json.loads(p.read_text());assert d['error'] is None and d['before']==d['after'];watch=d['whole_tree_watchdog'];assert watch['samples']>0 and not watch['violations'];assert watch['limit_seconds']==60 and watch['limit_bytes']==402653184
 for a in d['artifacts']:assert sha(pathlib.Path(a['path']))==a['sha256'];refs.append(a)
 assert sha(pathlib.Path(d['adapter']['path']))==d['adapter']['sha256']
 if 'mutation' in d:
  assert d['mutation_attempts']==1 and d['baseline_runs']==0 and d['exit_code']==1
  s=d['structured_result'];assert s['passed']==13 and s['failed']==1 and s['failed_tags']==s['expected_failed_tags'];body=pathlib.Path(d['artifacts'][0]['path']).read_text();assert re.findall(r'^FAIL: ([A-Z][0-9]+) ',body,re.M)==s['failed_tags']
 else:
  assert d['primary_runs_attempted']==1;rr=d['result']['result'];assert rr['exit_code']==0 and rr['status']=='ok';assert 'TOTAL: PASS=14 FAIL=0' in rr['stdout'];assert len(re.findall(r'^PASS: ',rr['stdout'],re.M))==14
 stats.append(dict(receipt=str(p),status=d['status'],elapsed_seconds=d['elapsed_seconds'],peak_rss=watch['peak_tree_rss_bytes']))
print(json.dumps(dict(base=f['base'],tree=f['tree'],source=rows,all_inputs_verified=True,original_payloads=20,binding_only_adapter_change=True,executions=stats,raw_artifacts=refs),indent=2))
