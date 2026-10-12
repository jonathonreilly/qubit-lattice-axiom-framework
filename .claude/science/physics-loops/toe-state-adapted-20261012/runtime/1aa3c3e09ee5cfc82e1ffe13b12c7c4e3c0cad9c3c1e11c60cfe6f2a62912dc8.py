"""Deterministic evidence bookkeeping; does not rerun scientific controls."""
from pathlib import Path
import json,hashlib,datetime
e=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
all_rows=[];receipts=[];disposition=[]
for job,manifest_name in [('baseline','execution_manifest.json'),('wrong_frame_sign','execution_manifest.json'),('omit_continuum_unrotation','execution_manifest.json'),('half_angle','half_angle_manifest.json')]:
 manifest=json.loads((e/manifest_name).read_text());mh=sha(e/manifest_name)
 for layer in ['inner','outer']:
  rp=e/'runs'/f'{job}_{layer}.receipt.json';r=json.loads(rp.read_text())
  assert r['expected_manifest_sha256']==mh==r['actual_manifest_sha256']
  assert r['source_before']==manifest['files']==r['source_after']
  assert r['source_unchanged'] and not r['timeout']
  for typ in ['stdout','stderr']:assert sha(r[typ])==r[typ+'_sha256']
  assert not Path(r['stderr']).read_text()
  receipts.append({'job':job,'layer':layer,'receipt_path':str(rp),'receipt_sha256':sha(rp),
                   **{k:r[k] for k in ['returncode','start_utc','end_utc','elapsed_seconds','timeout_seconds','timeout']},
                   'streams_verified':True,'sources_verified':True})
 raw=e/'runs'/f'{job}_inner.stdout.txt';rows=[];summaries=[]
 for line,txt in enumerate(raw.read_text().splitlines(),1):
  if not txt.startswith('{'):continue
  x=json.loads(txt)
  if 'name' in x:
   row={'job':job,'raw_path':str(raw),'raw_line':line,**x};rows.append(row);all_rows.append(row)
  elif x.get('summary'):summaries.append(x)
 assert len(summaries)==1
 sm=summaries[0];assert sm['total']==len(rows) and sm['failed']==sum(not x['passed'] for x in rows)
 assert len({r['name'] for r in rows})==len(rows)
 disposition.append({'job':job,'summary':sm,'failed_rows':[r['name'] for r in rows if not r['passed']],
                     'surviving_rows':[r['name'] for r in rows if r['passed']]})
for name,obj in [('row_inventory.json',all_rows),('verified_execution_receipts.json',receipts),('result_disposition.json',disposition)]:
 (e/name).write_text(json.dumps(obj,indent=2)+'\n')
base=[x for x in all_rows if x['job']=='baseline']
summary={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'complete_rows':len(all_rows),
 'job_summaries':[j['summary']|{'job':j['job']} for j in disposition],
 'baseline_largest_2e10_identity_residual':max(r['value'] for r in base if r.get('tolerance')==2e-10),
 'baseline_symbolic_issue':'Original SymPy trigsimp/expand_trig did not return structural zero. Separate post-observation frozen exact half-angle checks both true. Original false rows retained.',
 'all_eight_receipts_verified':True,'largest_inner_seconds':max(r['elapsed_seconds'] for r in receipts if r['layer']=='inner'),
 'independence':'Same-author controls. Fresh separate-context review is external and pending.'}
(e/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
