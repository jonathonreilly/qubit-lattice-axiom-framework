from pathlib import Path
R=Path('/private/tmp/review-drain-20260915')
s=(R/'drain8033-capture-v2.py').read_text().replace('PR8033','PR8178').replace('drain8033','drain8178').replace('/root/review_8033','/root/review_8178').replace("W=R/'author-draft-slot'","W=R/'review-draft-slot'").replace("R/'author-draft-slot.json'","R/'review-draft-slot.json'")
s=s.replace(" and plan['parent_landed_exact'] is True",'')
s=s.replace("program=dict(plan['runner'],mathematical_checks=18,ordered_inputs=plan['ordered_inputs'],N5_scopes=plan['N5_scopes'],stdout_cache=plan['output_contract']['stdout_cache'])","program=dict(plan['runner'],mathematical_checks=11,ordered_inputs=plan['ordered_inputs'],stdout_cache=plan['output_contract']['canonical_stdout_cache'])\n assert plan['limits']['wall_seconds']==60 and plan['limits']['sampled_aggregate_process_tree_rss_bytes']==384*1024*1024\n assert plan['planned_checks']=={'total':16,'mathematical':11,'metadata':5,'families':{'A':4,'B':2,'C':2,'D':3,'F':4,'G':1}}")
s=s.replace('execute_and_write_cache(sys.argv[2],180)','execute_and_write_cache(sys.argv[2],60)').replace('limit_seconds=180,limit_bytes=256*1024*1024','limit_seconds=60,limit_bytes=384*1024*1024').replace('elapsed>=180','elapsed>=60')
a=s.index("  data=json.loads(side.read_text());count=");b=s.index('  after=snapshot();',a)
s=s[:a]+'''  data=json.loads(side.read_text());assert data['passed']==16 and data['failed']==0 and data['failed_families']==[] and data['mutation'] is None and data['expected_mutation_family'] is None
  assert data['input_sha256']=={e['path']:e['sha256'] for e in program['ordered_inputs']}
  assert re.search(r'^TOTAL: PASS=16 FAIL=0$',rr['stdout'],re.M) and Path(result['cache']).resolve()==cache.resolve()
  assert len(re.findall(r'^PASS: ',rr['stdout'],re.M))==16 and not re.search(r'^FAIL: ',rr['stdout'],re.M)
'''+s[b:]
s=s.replace("  assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']","  assert e['path'] not in ids or ids[e['path']]==e['sha256'];ids[e['path']]=e['sha256']")
# Preserve live partial output externally too if worker is killed before returning.
s=s.replace(" finally:\n  with receipt.open('x')", " finally:\n  partial=Path(str(prefix)+'.partial-live.txt')\n  if live.is_file():\n   with partial.open('xb') as f:f.write(live.read_bytes())\n  with receipt.open('x')")
s=s.replace('[side,raw,workerout,log,cache,live] if p.is_file()','[side,raw,workerout,log,cache,live,partial] if p.is_file()')
with (R/'drain8178-capture-v1.py').open('x') as f:f.write(s)
