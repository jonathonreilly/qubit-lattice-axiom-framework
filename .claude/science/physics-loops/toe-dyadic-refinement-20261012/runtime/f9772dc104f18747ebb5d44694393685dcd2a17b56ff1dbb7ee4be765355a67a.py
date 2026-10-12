from pathlib import Path
import json,hashlib,difflib,datetime,math
S=Path(__file__).resolve().parent;D=S/'dyadic_route_readiness/dyadic_even_refinement';R=S/'dyadic_author_root_verification';R.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();js=lambda p:json.loads(Path(p).read_text())
assert sha(D/'final_manifest.json')=='e25e34e5200340a92cd2d60949eec7b4b698708fc43b533711666111e7bdbe4e'
m=js(D/'final_manifest.json');assert len(m['files'])==94
for path,pin in m['files'].items():assert sha(path)==pin['sha256'] and Path(path).stat().st_size==pin['bytes']
manifest=js(D/'execution_manifest.json');anchor='dfe56a005e018555d7d93b522d195042b94c74ff8aff67f53783d1cf7276a35f';assert sha(D/'execution_manifest.json')==anchor
note=D.parent/'DYADIC_EVEN_REFINEMENT_PROBE.md';executed=D/'frozen/EXECUTED_ARGUMENT.md';assert sha(note)=='646ad05eb2f3ba02b6410e4043a4f258ca84ea2c15b92a4ca7d0ab25e05ecc9c';assert sha(executed)=='983c435bbe33f954136cc5d506582f80fa38f9d722766ad854b2aafe49d4630d'
assert note.read_bytes().startswith(executed.read_bytes())
assert ''.join(difflib.unified_diff(executed.read_text().splitlines(True),note.read_text().splitlines(True),fromfile='executed_argument',tofile='final_argument'))==(D/'FINAL_EVIDENCE_APPENDIX.diff').read_text()
for path,h in manifest['files'].items():assert sha(executed if Path(path)==note else path)==h
for row in js(D/'source_inventory.json')['source_rows']:assert sha(row['source'])==row['sha256']==sha(D/'sources'/row['name'])
repro=js(D/'reproduction_manifest.json');assert sha(D/'reproduction_manifest.json')=='e3fb00cfd543ecb7b09624b4fc366df1dd5cd3a6f41d198d7071434365fa4ad2'
expected_map=dict(manifest['files']);old=expected_map.pop(str(note));expected_map[str(executed)]=old;assert repro['files']==expected_map
for path,h in expected_map.items():assert sha(path)==h
for path,h in js(D/'INVALID_INITIAL_RECORDING.json')['retained_files'].items():assert sha(path)==h
jobs={'exact_baseline_v2':0,'state_baseline_v2':0,'mutant_missing_normalization':1,'mutant_tensor_shortcut':1,'mutant_missing_state_formfactor':1};allrows=[];receipts=[]
for name,code in jobs.items():
 for layer,limit in [('inner',60),('outer',70)]:
  path=D/'runs'/f'{name}_{layer}.receipt.json';r=js(path)
  assert r['returncode']==code and not r['timeout'] and r['timeout_seconds']==limit and r['source_unchanged']
  assert r['source_before']==r['source_after']==manifest['files'] and r['actual_manifest_sha256']==r['expected_manifest_sha256']==anchor
  assert 0<=r['elapsed_seconds']<=limit
  for stream in ['stdout','stderr']:assert sha(r[stream])==r[stream+'_sha256']
  assert Path(r['stderr']).read_bytes()==b''
  receipts.append({k:v for k,v in r.items() if k not in ['source_before','source_after']})
 path=D/'runs'/f'{name}_inner.stdout.txt';rows=[];summary=None
 for no,line in enumerate(path.read_text().splitlines(),1):
  if not line.startswith('{'):continue
  row=json.loads(line)
  if 'name' in row:
   assert type(row['pass']) is bool;rows.append(row);allrows.append({'run':name,'stdout':str(path),'line':no,'row':row})
   if 'actual' in row and 'expected' in row and isinstance(row['actual'],dict):assert row['pass']==(row['actual']==row['expected'])
   if 'minimum_margin' in row:assert row['pass']==(row['coarse_minus_mid']>row['minimum_margin'] and row['mid_minus_refined']>row['minimum_margin'])
   if 'residual' in row:assert row['pass']==(row['residual']<row['tolerance'])
   if 'coefficient' in row:assert row['pass']==(row['coefficient']==row['expected'])
   if 'hypothesis_holds' in row:assert row['pass']==(row['hypothesis_holds']==row['expected_hypothesis'])
  if 'summary' in row:summary=row['summary']
 failed=[r['name'] for r in rows if not r['pass']];assert len(set(r['name'] for r in rows))==len(rows)
 assert summary=={'rows':len(rows),'pass':len(rows)-len(failed),'fail':len(failed),'failed':failed}
assert allrows==js(D/'row_inventory.json') and len(allrows)==297
base=[r['row'] for r in allrows if r['run'].endswith('baseline_v2')];mut=[r['row'] for r in allrows if r['run'].startswith('mutant')]
assert len(base)==206 and all(r['pass'] for r in base) and len(mut)==91 and sum(not r['pass'] for r in mut)==35
(R/'verified_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
r={'status':'stored_author_evidence_checked','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_files':94,'executed_inputs':39,'refreshed_parent_sources':6,'valid_complete_receipts':10,'valid_rows':297,'baseline_rows':206,'mutant_rows':91,'mutant_failures':35,'mutant_survivors':56,'invalid_initial_attempts':2,'no_science_rerun':True,'independent_review':False,'root_all_helpers_and_297_original_rows_read':True,'scope_limits':['local_support_children checks string width only','trace_preserved rows are on retained images','infinite and CP theorems analytic','floating integrals not interval certified'],'pending':['complete fresh-review helper/evidence read']}
(R/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
