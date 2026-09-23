from pathlib import Path
import json,hashlib,ast
r=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=r/'drain8159-capture.py';assert sha(old)=='b7e0a4bcd9235f5d9500b6495d79f9fca6736517dc5463545a205833af877294'
cold=r/'drain8159-cold-confirmation-v2.json';d=json.loads(cold.read_text());assert d['tree']=='4ba6ac5af198073fcac0168d3795ed018139ad32'
pre=r/'drain8159-author-cheap-v2.json';p=json.loads(pre.read_text());assert p['mechanical_status']=='ok' and not p['cache_checked']
plan=json.loads((r/'drain8159-capture-plan-v1.json').read_text())
for row in plan['captures']:
 if row['runner']=='scripts/holonomy_check_2026_09_15.py':
  row['sha256']='c0ee175798de3c1e4f61d8a5f27af37d108c079cc794d8ac75537e9d89cf30fa';row['slab_resource_assessment']={'path':str(r/'drain8159-holonomy-slab-assessment-v1.json'),'sha256':sha(r/'drain8159-holonomy-slab-assessment-v1.json')}
plan['status']='13 prior successes eligible for identity-checked reuse; 28 remaining captures after affected cold confirmation, including repaired holonomy'
plan['cold_confirmation']={'path':str(cold),'sha256':sha(cold)}
planfile=r/'drain8159-capture-plan-v2.json';assert not planfile.exists();planfile.write_text(json.dumps(plan,indent=2)+'\n')
s=old.read_text().replace('author-unit-draft-v1.json','author-unit-draft-v2.json').replace('author-cheap-v1.json','author-cheap-v2.json').replace('cold-confirmation-v1.json','cold-confirmation-v2.json').replace('ba0ef06b15272b36d374c388afa5d4010d6571b6cb8768ab240a80a65a16e457',sha(cold)).replace("cold['status']=='COLD SOURCE CONFIRMED; ELIGIBLE FOR DECLARED BOUNDED CAPTURES; PARTIAL SALVAGE ONLY'", "cold['status']=="+repr(d['status']))
start=s.index('records=[];caches=[];raw_outputs=[]');end=s.index('\n verify();receipt=',start)
replacement='''records=[];caches=[];raw_outputs=[]
planpath=b/'drain8159-capture-plan-v2.json';assert sha(planpath)==PLANHASH;plan=json.loads(planpath.read_text());assert len(plan['captures'])==41
assessment=b/'drain8159-holonomy-slab-assessment-v1.json';assert sha(assessment)==ASSESSMENTHASH;reuse=json.loads(assessment.read_text())['eligible_prior_captures'];assert len(reuse)==13
reused=set();reuse_identity=[]
for item in reuse:
 runner=item['runner'];receipt=Path(item['receipt']['path']);assert sha(receipt)==item['receipt']['sha256'];e=json.loads(receipt.read_text())
 assert e['status']=='ok' and e['exit_code']==0 and not e['whole_tree_watchdog']['violations']
 assert c.cache_status(runner)=='fresh' and c.declared_input_fingerprint(w/runner)==item['declared_input_fingerprint']
 cache,header,body=c.load_cache(runner);assert header['runner_path']==runner and header['status']=='ok' and header['exit_code']=='0'
 assert body.split('----- stdout -----\\n',1)[1].split('----- stderr -----',1)[0].rstrip()==e['stdout'].rstrip()
 raw=w/e['raw_output']['path'];assert sha(raw)==e['raw_output']['sha256'];assert sha(Path(e['capture_script']))==e['capture_script_sha256']
 records.append({'pr':Path(runner).stem,'receipt':str(receipt),'sha256':sha(receipt),'reused_unchanged':True});caches.append(cache.relative_to(w).as_posix());raw_outputs.append(raw.relative_to(w).as_posix());reused.add(runner)
 reuse_identity.append({'runner':runner,'cache_sha256':sha(cache),'raw_sha256':sha(raw),'input_fingerprint':item['declared_input_fingerprint']})
verify()
reusefile=b/'drain8159-capture-reuse-v2.json';assert not reusefile.exists();reusefile.write_text(json.dumps(reuse_identity,indent=2)+'\\n')
remaining=[x for x in plan['captures'] if x['runner'] not in reused];assert len(remaining)==28
for row in remaining:
 assert sha(w/row['runner'])==row['sha256']
 assert not (w/'logs/runner-cache'/Path(row['runner']).with_suffix('.json').name).exists(),row['runner']
for row in remaining:
 primary=row['runner'];pr=Path(primary).stem;cap_seconds=row['time_cap_seconds'];cap_bytes=row['process_tree_rss_cap_bytes']'''
replacement=replacement.replace('PLANHASH',repr(sha(planfile))).replace('ASSESSMENTHASH',repr(sha(r/'drain8159-holonomy-slab-assessment-v1.json')))
s=s[:start]+replacement+s[end:]
s=s.replace("receipt=b/f'drain8159-execution-{pr}.json'","receipt=b/f'drain8159-execution-v2-{pr}.json'")
s=s.replace("subprocess.run(['git','-C',str(w),'add','--',*caches,*raw_outputs],check=True)","assert len(records)==41 and len(set(caches))==41 and len(set(raw_outputs))==41\nverify()\nfor item in reuse_identity:\n assert sha(c.cache_path_for(item['runner']))==item['cache_sha256'] and c.cache_status(item['runner'])=='fresh'\nsubprocess.run(['git','-C',str(w),'add','--',*caches,*raw_outputs],check=True)")
out=r/'drain8159-capture-v2.py';assert not out.exists();compile(s,str(out),'exec');out.write_text(s);print(sha(out))
