import json,pathlib,hashlib,subprocess,gzip,ast,math
r=pathlib.Path('/private/tmp/review-drain-20260915');s=r/'drain-author-slot'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=s)
f=json.loads((r/'drain8164-author-final-freeze.json').read_text());d=json.loads((r/'drain8164-author-unit-draft-v1.json').read_text());plan=json.loads((r/'drain8164-capture-plan-v1.json').read_text());hand=json.loads((r/'drain8164-author-source-handoff-v1.json').read_text())
assert f['tree']=='672fc49167bd4653e1da96b2ab3e8bef223d9d9e'
idx={l.split('\t')[1]:l.split('\t')[0].split()[:2] for l in git('ls-files','--stage').decode().splitlines()};tr={l.split('\t')[1]:[l.split()[0],l.split()[2]] for l in git('ls-tree','-r',f['tree']).decode().splitlines()};assert idx==tr
assert not git('diff','--name-only').strip();assert set(git('diff','--cached','--name-only').decode().splitlines())==set(f['source_paths'])
assert len(f['source_paths'])==212
for p,h in f['source_paths'].items():assert sha((s/p).read_bytes())==h==sha(git('show',':'+p))
for x in d['source']['paths']:assert f['source_paths'][x['path']]==x['sha256']
for p,h in f['inputs'].items():assert sha((s/p).read_bytes())==h
assert len(hand['original_dispositions'])==178
inv={x['path']:x for x in json.loads((r/'drain8164-original-inventory.json').read_text())}
for x in hand['original_dispositions']:
 o=inv[x['original_path']];data=(s/x['final_path']).read_bytes();assert sha(data)==x['final_sha256'];assert sha(gzip.decompress(data))==o['sha256']==x['original_sha256'];assert (o['mode'],o['blob'])==(x['original_mode'],x['original_blob'])
rows=[]
for ref,p in zip(f['executions'],plan['programs']):
 rp=pathlib.Path(ref['receipt']);assert sha(rp.read_bytes())==ref['sha256'];e=json.loads(rp.read_text());runner=p['runner'];assert e['runner']==runner and e['status']=='ok' and e['exit_code']==0 and e['stderr']==''
 assert e['timeout_sec']==180 and e['elapsed_sec']<180 and e['capture_script_sha256']==sha((r/'drain8164-capture.py').read_bytes())
 w=e['whole_tree_watchdog'];assert not w['violations'] and w['samples']>0 and w['peak_tree_rss_bytes']<=w['limit_bytes']==p['process_tree_rss_cap_bytes']
 raw=(s/p['json_destination']).read_bytes();assert sha(raw)==e['raw_output']['sha256']==f['raw_output_hashes'][p['json_destination']]
 j=json.loads(raw,parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)));assert j['source_sha256']==p['source_sha256'];assert j['canonical_total']==p['expected_total'] and j['canonical_completed_families']==p['completed_families']
 stdout=e['stdout'];parsed,end=json.JSONDecoder().raw_decode(stdout);assert parsed==j;tail=stdout[end:].strip().splitlines();assert tail[0]==f"TOTAL: PASS={p['expected_total']} FAIL=0";assert len(tail)==6
 cache=(s/p['stdout_cache']).read_text();header,body=cache.split('----- stdout -----\n',1);out,err=body.split('\n----- stderr -----\n',1);assert out.rstrip('\n')==stdout.rstrip('\n') and not err.strip()
 for text in [f'runner: {runner}',f'runner_sha256: {p["source_sha256"]}','timeout_sec: 180','exit_code: 0','status: ok']:assert text in header
 a=ast.parse((s/runner).read_text());paths=next(ast.literal_eval(n.value) for n in a.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets));h=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
 for path in paths:
  pb=path.encode();bb=(s/path).read_bytes();h.update(len(pb).to_bytes(8,'big'));h.update(pb);h.update(len(bb).to_bytes(8,'big'));h.update(bb)
 assert 'input_fingerprint_sha256: '+h.hexdigest() in header
 rows.append({'runner':runner,'families':p['expected_total'],'elapsed_sec':e['elapsed_sec'],'peak_sampled_tree_rss_bytes':w['peak_tree_rss_bytes'],'sample_count':w['samples'],'input_fingerprint_sha256':h.hexdigest(),'stdout_cache_sha256':sha((s/p['stdout_cache']).read_bytes()),'raw_json_sha256':sha(raw),'receipt_sha256':ref['sha256'],'top_level_data_keys':list(j)})
assert len(rows)==8
result={'tree':f['tree'],'verified_prior_sources':196,'verified_new_evidence_paths':16,'verified_original_dispositions':178,'source_unchanged_since_cold':True,'rows':rows,'root_cache_preflight_executed':False,'primary_executions':0}
p=r/'drain8164-final-static-v1.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
