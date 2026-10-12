from pathlib import Path
import hashlib,json,datetime
S=Path(__file__).resolve().parent;D=S/'dyadic_even_refinement_review';R=S/'dyadic_review_root_verification';R.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
js=lambda p:json.loads(Path(p).read_text())
anchor='fc3848fc0889aeaf8e33a64c5216c2662a1b763643706ea17960c1368a0fc65c'
assert sha(D/'FINAL_REVIEW_MANIFEST.json')==anchor
m=js(D/'FINAL_REVIEW_MANIFEST.json');assert len(m['files'])==81
for p,b in m['files'].items():
 q=D/p;assert sha(q)==b['sha256'] and q.stat().st_size==b['bytes'],p
assert sha(m['review_path'])==m['review_sha256']=='09b4f24a4c07f03a2f2f14e90a6dd1812159093fb67f2e96c1c82885c33ae472'
assert sha(m['target_path'])==m['target_sha256']=='646ad05eb2f3ba02b6410e4043a4f258ca84ea2c15b92a4ca7d0ab25e05ecc9c'
for name,h in m['parent_hashes'].items():assert sha(S/name)==h==sha(D/'sources'/name)
seal=js(D/'INDEPENDENT_EVIDENCE_SEAL.json')
assert sha(D/'INDEPENDENT_EVIDENCE_SEAL.json')==m['independent_seal_sha256']
for b in seal['files']:
 q=D/b['path'];assert sha(q)==b['sha256'] and q.stat().st_size==b['bytes']
rows={};receipts=[]
for name in ['exact_01','numeric_01','author_integrity_01','tamper_integrity_01']:
 q=D/'runs'/name;i=js(q/'INNER.receipt.json');o=js(q/'OUTER.receipt.json')
 assert i['returncode']==0 and not i['timed_out'] and i['timeout_seconds']==60 and 0<=i['elapsed_seconds']<=60
 assert o['inner_receipt_sha256']==sha(q/'INNER.receipt.json') and o['status']=='completed_zero' and o['recorded_before_inspection']
 assert o['source_sha256']==i['source_sha256']==sha(i['command'][1])
 assert i['protocol_sha256']==sha(D/'CONTROL_SPEC.md')
 for stream in ['stdout','stderr']:
  p=q/('INNER.'+stream);assert i[stream+'_sha256']==o['inner_'+stream+'_sha256']==sha(p) and i[stream+'_bytes']==p.stat().st_size
 assert (q/'INNER.stderr').read_bytes()==b''
 if name!='author_integrity_01':
  rs=[json.loads(line) for line in (q/'INNER.stdout').read_text().splitlines()]
  assert all(r['ok'] is True for r in rs);rows[name]=rs
 else:
  report=js(D/'author_evidence_validation.json');assert report['all_checks_hold'] and all(c['ok'] for c in report['checks'])
  assert len(report['checks'])==34 and len(report['rows'])==297
 receipts.append({'name':name,'inner':i,'outer':o})
assert len(rows['exact_01'])==27 and len(rows['numeric_01'])==36 and len(rows['tamper_integrity_01'])==7
for r in rows['numeric_01']:
 for key in ['max_residual','residual']:
  if key in r and not r['name'].startswith(('mutation','wrong')):assert abs(r[key])<2e-12,(r['name'],key)
 if r['name']=='Fourier_projector_vs_scalar_quadrature':assert r['max_difference']<2e-12 and r['imaginary']<2e-12
 if r['name']=='fixed_refinement_state_discrepancy':assert r['coarse_minus_fine']>1e-5
 if r['name']=='choi_positive_and_formula_matches':assert r['min_eigenvalue']>-2e-12 and r['block_residual']<2e-12
assert js(D/'FINAL_REVIEW_RECEIPT.json')['manifest_sha256']==anchor
(R/'verified_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
result={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete_source_bound_root_review','review_manifest_files':81,'preexposure_bindings':17,'refreshed_parent_sources':5,'complete_inner_outer_runs':4,'exact_rows_including_summary':27,'numerical_rows_including_summary':36,'integrity_rows_including_summary':7,'author_integrity_predicates':34,'no_science_rerun':True,'manual_coverage':['Full target D1-D32 and evidence appendix','Full fresh review and necessary premises','All five reviewer helpers and recording code','All independent scientific and integrity raw rows','Literal author source variants and all 297 author rows in preceding root review'],'limits':['Same selected model family, separate formula-exposed reviewer; not blinded or diverse-family','Root coauthor of state-adapted conjugacy addendum','Numerical diagnostics support analytic infinite-volume proofs; no formal retained verdict','Narrow support and trace diagnostics do not alone prove support positioning or general trace preservation','Fixed Haar state and energy failures preserved; state-adapted locality and dynamics are a new open route'],'pending':[]}
(R/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
coverage=dict(result,target={'path':m['target_path'],'sha256':m['target_sha256']},review={'path':m['review_path'],'sha256':m['review_sha256']},review_manifest={'path':str(D/'FINAL_REVIEW_MANIFEST.json'),'sha256':anchor},author_root_result={'path':str(S/'dyadic_author_root_verification/RESULT.json'),'sha256':sha(S/'dyadic_author_root_verification/RESULT.json')})
(S/'Dyadic_even_refinement_root_review_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
print(json.dumps(result))
