"""Full-record verification and deterministic indexing, not a science rerun."""
from pathlib import Path
import json,hashlib,datetime
e=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
m=json.loads((e/'execution_manifest.json').read_text());mh=sha(e/'execution_manifest.json')
rows=[];diagnostics=[];receipts=[];jobs=[]
for job in ['baseline','drop_jacobian','reverse_cell_phase']:
 for layer in ['inner','outer']:
  path=e/'runs'/f'{job}_{layer}.receipt.json';r=json.loads(path.read_text())
  assert r['expected_manifest_sha256']==mh==r['actual_manifest_sha256']
  assert r['source_before']==m['files']==r['source_after'] and r['source_unchanged'] and not r['timeout']
  for kind in ['stdout','stderr']:assert sha(r[kind])==r[kind+'_sha256']
  assert not Path(r['stderr']).read_text(),Path(r['stderr']).read_text()
  receipts.append({'job':job,'layer':layer,'receipt_path':str(path),'receipt_sha256':sha(path),
       **{key:r[key] for key in ['returncode','start_utc','end_utc','elapsed_seconds','timeout_seconds','timeout']},'streams_verified':True,'sources_verified':True})
 raw=e/'runs'/f'{job}_inner.stdout.txt';own=[];summaries=[]
 for line,txt in enumerate(raw.read_text().splitlines(),1):
  if not txt.startswith('{'):continue
  value=json.loads(txt);indexed={'job':job,'raw_path':str(raw),'raw_line':line,**value}
  if 'name' in value:own.append(indexed);rows.append(indexed)
  elif 'diagnostic' in value:diagnostics.append(indexed)
  elif value.get('summary'):summaries.append(value)
 assert len(summaries)==1;sm=summaries[0]
 assert sm['total']==len(own) and sm['failed']==sum(not x['passed'] for x in own)
 assert len({r['name'] for r in own})==len(own)
 jobs.append({'job':job,'summary':sm,'failed_rows':[x['name'] for x in own if not x['passed']],
              'surviving_rows':[x['name'] for x in own if x['passed']]})
for name,value in [('row_inventory.json',rows),('diagnostic_inventory.json',diagnostics),('result_disposition.json',jobs),('verified_execution_receipts.json',receipts)]:
 (e/name).write_text(json.dumps(value,indent=2)+'\n')
summary={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predicate_rows':len(rows),'diagnostic_rows':len(diagnostics),
 'job_summaries':[j['summary']|{'job':j['job']} for j in jobs],
 'all_six_receipts_verified':True,'largest_inner_seconds':max(r['elapsed_seconds'] for r in receipts if r['layer']=='inner'),
 'baseline_max_2e10_identity_residual':max(r['value'] for r in rows if r['job']=='baseline' and r.get('tolerance')==2e-10),
 'independence':'Author controls. Fresh independent source review remains pending.'}
(e/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
print(json.dumps({'failed_names':{j['job']:j['failed_rows'] for j in jobs}}))
print(json.dumps({'diagnostics':diagnostics}))
