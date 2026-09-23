import pathlib,json,hashlib,subprocess,ast,gzip
r=pathlib.Path('/private/tmp/review-drain-20260915');w=r/'author-draft-slot';h=lambda b:hashlib.sha256(b).hexdigest();sha=lambda p:h(p.read_bytes());f=json.loads((r/'drain8165-author-final-freeze.json').read_text());cold=json.loads((r/'drain8165-cold-source-confirmation-v1.json').read_text());git=lambda *a:subprocess.check_output(['git','-C',str(w),*a]);assert f['tree']=='089466fd15737f02c43a535857eeb64f7fe87f21';assert git('rev-parse','HEAD').decode().strip()==f['base'];assert len(f['source_paths'])==80
assert set(git('diff','--cached','--name-only').decode().splitlines())==set(f['source_paths']);assert not git('diff','--name-only').strip()
for p,hh in f['source_paths'].items():assert sha(w/p)==h(git('show',':'+p))==h(git('show',f['tree']+':'+p))==hh
for x in cold['source_paths']:assert f['source_paths'][x['path']]==x['sha256']
for p,hh in f['inputs'].items():assert sha(w/p)==hh
summaries=[]
for e in f['executions']:
 p=pathlib.Path(e['receipt']);assert sha(p)==e['sha256'];a=json.loads(p.read_text());assert a['status']=='ok' and a['exit_code']==0 and not a['stderr'];assert a['timeout_sec']==120 and a['elapsed_sec']<120;watch=a['whole_tree_watchdog'];assert not watch['violations'] and watch['samples']>0 and watch['peak_tree_rss_bytes']<536870912;assert sha(pathlib.Path(a['capture_script']))==a['capture_script_sha256'];raw=w/a['raw_output']['path'];assert sha(raw)==a['raw_output']['sha256']==f['raw_output_hashes'][a['raw_output']['path']];j=json.loads(raw.read_text());assert j['source_sha256']==sha(w/a['runner']);stdout_json,end=json.JSONDecoder().raw_decode(a['stdout']);assert stdout_json==j;assert a['stdout'][end:].startswith('\nTOTAL: PASS=3 FAIL=0\n');assert j['completed_diagnostic_families']==3
 tree=ast.parse((w/a['runner']).read_text());vals={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['AUDIT_INPUT_PATHS','EXPECTED_INPUT_SHA256']};assert j['input_sha256']==vals['EXPECTED_INPUT_SHA256'];dig=hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
 for ip in vals['AUDIT_INPUT_PATHS']:
  body=(w/ip).read_bytes();assert h(body)==j['input_sha256'][ip];b=ip.encode();dig.update(len(b).to_bytes(8,'big'));dig.update(b);dig.update(len(body).to_bytes(8,'big'));dig.update(body)
 cache=w/'logs/runner-cache'/pathlib.Path(a['runner']).with_suffix('.txt').name;ct=cache.read_text();assert 'runner_sha256: '+j['source_sha256'] in ct and 'input_fingerprint_sha256: '+dig.hexdigest() in ct;out=ct.split('----- stdout -----\n',1)[1].split('\n----- stderr -----',1)[0];assert out.rstrip()==a['stdout'].rstrip()
 summaries.append(dict(runner=a['runner'],elapsed_sec=a['elapsed_sec'],sampled_peak_bytes=watch['peak_tree_rss_bytes'],watch_samples=watch['samples'],raw_sha256=sha(raw),cache_sha256=sha(cache),stdout_sha256=h(a['stdout'].encode()),families=3,static_assert_statements=j['static_source_assert_statements']))
# Recover all originals, not just hashes of compressed bytes.
hand=json.loads((r/'drain8165-author-source-handoff-v1.json').read_text());assert len(hand['original_dispositions'])==88
for d in hand['original_dispositions']:
 data=(w/d['recovery']).read_bytes();data=gzip.decompress(data) if d.get('recovery_encoding')=='gzip' or d['recovery'].endswith('.gz') else data;assert h(data)==d['original_sha256']
print(json.dumps(summaries,indent=2));(r/'check8165/final_verified_evidence.json').write_text(json.dumps(summaries,indent=2)+'\n')
