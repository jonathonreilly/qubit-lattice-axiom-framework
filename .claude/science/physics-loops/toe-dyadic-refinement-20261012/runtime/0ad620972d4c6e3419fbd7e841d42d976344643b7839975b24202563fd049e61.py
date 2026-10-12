"""Bookkeeping only: validate complete raw receipts and index every science row."""
from pathlib import Path
import hashlib,json

E=Path(__file__).resolve().parent
anchor='dfe56a005e018555d7d93b522d195042b94c74ff8aff67f53783d1cf7276a35f'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(E/'execution_manifest.json')==anchor
manifest=json.loads((E/'execution_manifest.json').read_text())
jobs={'exact_baseline_v2':0,'state_baseline_v2':0,'mutant_missing_normalization':1,
      'mutant_tensor_shortcut':1,'mutant_missing_state_formfactor':1}
all_rows=[];disposition={};receipts=[]
for name,expected_rc in jobs.items():
 for layer in ('inner','outer'):
  p=E/'runs'/f'{name}_{layer}.receipt.json';r=json.loads(p.read_text())
  assert r['returncode']==expected_rc and not r['timeout']
  assert r['source_before']==r['source_after']==manifest['files']
  assert r['source_unchanged'] and r['actual_manifest_sha256']==anchor
  for stream in ('stdout','stderr'):
   assert sha(r[stream])==r[stream+'_sha256']
  assert Path(r['stderr']).read_bytes()==b''
  if layer=='inner':assert r['timeout_seconds']==60
  if layer=='outer':assert r['timeout_seconds']==70
  receipts.append({'name':name,'layer':layer,'path':str(p),'sha256':sha(p),
                   'start_utc':r['start_utc'],'end_utc':r['end_utc'],
                   'elapsed_seconds':r['elapsed_seconds'],'returncode':r['returncode']})
 p=E/'runs'/f'{name}_inner.stdout.txt';rows=[];summary=None
 for lineno,line in enumerate(p.read_text().splitlines(),1):
  if not line.startswith('{'):continue
  d=json.loads(line)
  if 'name' in d:
   assert isinstance(d['pass'],bool)
   rows.append(d);all_rows.append({'run':name,'stdout':str(p),'line':lineno,'row':d})
  if 'summary' in d:summary=d['summary']
 assert len({r['name'] for r in rows})==len(rows)
 failed=[r['name'] for r in rows if not r['pass']]
 assert summary=={'rows':len(rows),'pass':len(rows)-len(failed),'fail':len(failed),'failed':failed}
 disposition[name]={'summary':summary,'failed_names':failed,
                    'surviving_names':[r['name'] for r in rows if r['pass']],
                    'complete_stdout_sha256':sha(p),'all_rows_indexed':True}
baseline={r['row']['name']:r['row'] for r in all_rows if r['run'].endswith('baseline_v2')}
for name,d in disposition.items():
 if not name.startswith('mutant'):continue
 rows=[r['row'] for r in all_rows if r['run']==name]
 d['same_row_as_baseline']=[r['name'] for r in rows if baseline.get(r['name'])==r]
 d['changed_row_from_baseline']=[r['name'] for r in rows if baseline.get(r['name'])!=r]
 d['changed_survivors']=[r['name'] for r in rows if r['pass'] and baseline.get(r['name'])!=r]
(E/'row_inventory.json').write_text(json.dumps(all_rows,indent=2)+'\n')
(E/'result_disposition.json').write_text(json.dumps(disposition,indent=2)+'\n')
(E/'verified_execution_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
summary={'valid_scientific_runs':len(jobs),'valid_scientific_rows':len(all_rows),
         'baseline_rows':sum(d['summary']['rows'] for n,d in disposition.items() if n.endswith('baseline_v2')),
         'baseline_failed':sum(d['summary']['fail'] for n,d in disposition.items() if n.endswith('baseline_v2')),
         'mutant_rows':sum(d['summary']['rows'] for n,d in disposition.items() if n.startswith('mutant')),
         'mutant_failed':sum(d['summary']['fail'] for n,d in disposition.items() if n.startswith('mutant')),
         'mutant_surviving':sum(d['summary']['pass'] for n,d in disposition.items() if n.startswith('mutant')),
         'invalid_initial_scientific_attempts':2,
         'invalid_attempts_record':'INVALID_INITIAL_RECORDING.json',
         'all_valid_INNER_and_OUTER_receipts_verified':True,
         'all_failures_and_survivors_retained':True,
         'independent_review':False}
(E/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
