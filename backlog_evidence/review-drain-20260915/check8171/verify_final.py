import pathlib,json,hashlib,subprocess,re,ast,gzip
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text());g=lambda *a:subprocess.check_output(['git','-C',str(W),*a])
f=j(R/'drain8171-author-final-freeze.json');old=j(R/'drain8171-author-unit-draft-v2.json');assert g('write-tree').decode().strip()==f['tree'];assert g('rev-parse','HEAD').decode().strip()==f['base'];assert not g('diff','--name-only')
assert len(f['source_paths'])==24 and all(f['source_paths'][e['path']]==e['sha256'] for e in old['source']['paths'])
assert set(g('diff','--cached','--name-only',f['base']).decode().splitlines())==set(f['source_paths'])
for p,d in {**f['source_paths'],**f['inputs']}.items():assert h(W/p)==hashlib.sha256(g('show',':'+p)).hexdigest()==d
binding=j(R/'drain8171-capture-binding-v2.json')
for e in binding['adapters']:
 for k in ['prior','actual']:assert h(pathlib.Path(e[k]['path']))==e[k]['sha256']
 trees=[]
 for k in ['prior','actual']:
  t=ast.parse(pathlib.Path(e[k]['path']).read_text())
  for n in t.body:
   if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='COLD_CLEARANCE_BINDING':n.value=ast.Constant(value=None)
  trees.append(ast.dump(t,include_attributes=False))
 assert trees[0]==trees[1]
receipts=[];refs=[]
plan=j(R/'drain8171-capture-plan-v1.json')
for e in f['executions']:
 p=pathlib.Path(e['receipt']);assert h(p)==e['sha256'];d=j(p);assert d['error'] is None and d['before']==d['after'];watch=d['whole_tree_watchdog'];assert watch['samples']>0 and not watch['violations'] and watch['limit_seconds']==60 and watch['limit_bytes']==402653184
 for a in d['artifacts']:
  q=pathlib.Path(a['path']);assert h(q)==a['sha256']
  if not q.is_relative_to(W):refs.append(a)
 for k in ['record','cold','adapter']:
  a=d[k];assert h(pathlib.Path(a['path']))==a['sha256']
 if 'mutation' in d:
  name=d['mutation'];raw=next(pathlib.Path(a['path']) for a in d['artifacts'] if a['path'].endswith('.stdout.txt'));out=raw.read_text();err=next(pathlib.Path(a['path']) for a in d['artifacts'] if a['path'].endswith('.stderr.txt'));assert not err.read_bytes()
  assert d['exit_code']==1 and d['mutation_attempts']==1 and d['baseline_runs']==0
  tags=re.findall(r'^FAIL: ([A-Z][0-9]+) ',out,re.M);assert tags==plan['mathematical_controls'][name]['expected_failed_tags'];assert 'TOTAL: PASS=15 FAIL=1' in out
  print(name,tags,d['elapsed_seconds'],watch['peak_tree_rss_bytes'])
 else:
  raw=j(R/'drain8171-raw-result-v2.json');assert raw==d['result']['result'];assert raw['exit_code']==0 and raw['status']=='ok' and raw['stderr']=='' and 'TOTAL: PASS=16 FAIL=0' in raw['stdout']
  cache=(W/plan['cache_destination']).read_text();assert raw['stdout'] in cache and plan['primary_sha256'] in cache and plan['input_fingerprint'] in cache;assert d['primary_runs_attempted']==1
 receipts.append({'path':str(p),'sha256':h(p),'elapsed':d['elapsed_seconds'],'peak_rss':watch['peak_tree_rss_bytes']})
hand=j(R/'drain8171-author-source-handoff-v2.json');assert len(hand['original_dispositions'])==18
for e in hand['original_dispositions']:
 q=W/e['recovery']['path'];assert h(q)==e['recovery']['sha256'];raw=gzip.decompress(q.read_bytes());assert hashlib.sha256(raw).hexdigest()==e['original_sha256'];assert raw==g('show','15b6e402b902964ada51ffdd8e8c88fb4e472013:'+e['original_path'])
 if e['final_path']:assert f['source_paths'][e['final_path']]==e['final_sha256']
summary={'status':'verified','source_tree':f['tree'],'source_paths':24,'original_dispositions':18,'adapter_binding_only':True,'execution_receipts':receipts,'external_raw_artifacts':refs,'science_runs_performed_by_verifier':0}
(R/'check8171/final-verification.json').write_text(json.dumps(summary,indent=2)+'\n')
print('All final source, input, archive and nine execution receipts verified.')
