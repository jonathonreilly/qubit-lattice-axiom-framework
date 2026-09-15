"""Capture frozen8091/92/94 once each; preserve original outputs and every attempt."""
from pathlib import Path
import json,hashlib,subprocess,sys
w=Path.cwd();r=w.parent;rp=r/'8094-unit-v1-preexecution.json';record=json.loads(rp.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();pref=json.loads((r/'8094-preexecution-preflight.json').read_text())
assert pref['mechanical_status']=='ok' and pref['record_sha256']==sha(rp)
assert pref['tree']==record['source']['tree']==subprocess.check_output(['git','write-tree'],text=True).strip()
inputs={x['path']:x['sha256'] for x in record['source']['paths']}
for rows in record['inputs'].values():
 for x in rows:
  assert x['path'] not in inputs or inputs[x['path']]==x['sha256'];inputs[x['path']]=x['sha256']
for p,h in inputs.items():assert sha(w/p)==h,p
sys.path.insert(0,str(w/'scripts'));import runner_cache
counts={'native_lapse_source_contact_response_2026_09_13':218,'native_common_frame_spin_connection_2026_09_13':423,'native_weyl_stress_logarithm_contact_response_2026_09_13':133};changed=set()
for note in record['notes']:
 runner=note['primary_runner'];stem=Path(runner).stem;count=counts[stem];output='outputs/'+stem+'.json';saved=r/('8094-original-output-'+stem+'.json');attempt=r/('8094-execution-'+stem+'-started.json');receipt=r/('8094-execution-'+stem+'.json')
 assert not saved.exists() and not attempt.exists() and not receipt.exists(),'Prior attempt must remain preserved'
 assert all(output not in {x['path'] for x in rows} for rows in record['inputs'].values()),'Output is execution input'
 with saved.open('xb') as f:f.write((w/output).read_bytes())
 assert sha(saved)==inputs[output]
 with attempt.open('x') as f:json.dump({'runner':runner,'limit_sec':60,'preexecution_record_sha256':sha(rp),'original_output_sha256':sha(saved)},f,indent=2)
 result,cache=runner_cache.execute_and_write_cache(runner,timeout_sec=60)
 entry={'runner':runner,'limit_sec':60,'preexecution_record_sha256':sha(rp),'result':result,'cache_path':str(cache) if cache else None,'cache_sha256':sha(cache) if cache else None,'original_output_sha256':sha(saved),'output_path':output,'output_sha256':sha(w/output)}
 with receipt.open('x') as f:json.dump(entry,f,indent=2);f.write('\n')
 assert result['status']=='ok' and result['exit_code']==0,receipt
 assert f'TOTAL: PASS={count} FAIL=0' in result['stdout'] and cache and runner_cache.cache_status(runner)=='fresh',receipt
 changed.update([output,cache.resolve().relative_to(w.resolve()).as_posix()])
 for p,h in inputs.items():
  if p not in changed:assert sha(w/p)==h,p
 subprocess.run(['git','add',str(cache),output],check=True)
 print(stem,count,'PASS seconds',result['elapsed_sec'],flush=True)
for args in [('diff','--check'),('diff','--cached','--check'),('diff','HEAD','--check')]:subprocess.run(['git',*args],check=True)
print('Final staged tree',subprocess.check_output(['git','write-tree'],text=True).strip())
