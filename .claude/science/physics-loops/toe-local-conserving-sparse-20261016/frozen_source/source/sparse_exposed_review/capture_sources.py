"""Metadata-only immutable-source capture and receipt validation. No science replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from pypdf import PdfReader

OUT=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_exposed_check')
SRC=OUT.parent/'local_conserving_sparse_compiler_candidate'
sha=lambda b:hashlib.sha256(b).hexdigest()
freeze_raw=(SRC/'FREEZE.json').read_bytes()
assert sha(freeze_raw)=='1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9'
freeze=json.loads(freeze_raw)
destroot=OUT/'author_source'
destroot.mkdir(exist_ok=False)
rows=[]
for row in list(freeze['members'])+[{'path':'FREEZE.json','bytes':len(freeze_raw),'sha256':sha(freeze_raw)}]:
 rel=Path(row['path']);assert not rel.is_absolute() and '..' not in rel.parts
 raw=(SRC/rel).read_bytes();assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
 dest=destroot/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 assert dest.read_bytes()==raw
 rows.append({'original_path':str(SRC/rel),'capture':str(dest.relative_to(OUT)),'bytes':len(raw),'sha256':sha(raw)})
assert sha((destroot/'DERIVATION.md').read_bytes())=='6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b'
assert sha((destroot/'sources/LOCAL_CONTROL_PARENT.md').read_bytes())=='c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60'
pdf=destroot/'sources/BAI_MARVIAN_2309.11051v3.pdf'
assert sha(pdf.read_bytes())=='add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8'

run_checks=[]
for name,launcher_name in [('exact_sparse_check','run_exact_check.py'),('exact_sparse_check_retry','run_exact_check_retry.py')]:
 run=destroot/'runs'/name
 receipt=json.loads((run/'EXECUTION.json').read_text())
 source=(run/'SOURCE_AT_LAUNCH.py').read_bytes()
 launcher=(run/'LAUNCHER_AT_LAUNCH.py').read_bytes()
 assert source==(destroot/'exact_sparse_check.py').read_bytes()
 assert launcher==(destroot/launcher_name).read_bytes()
 assert sha(source)==receipt['source_sha256']==receipt['source_sha256_after']
 assert sha(launcher)==receipt['launcher_sha256']
 for stream in ['stdout','stderr']:
  assert sha((run/(stream+'.txt')).read_bytes())==receipt[stream+'_sha256']
 run_checks.append({'run':name,'receipt_sha256':sha((run/'EXECUTION.json').read_bytes()),'exit_code':receipt['exit_code'],'source_and_launcher_match':True,'full_stream_hashes_match':True,'argv':receipt['argv'],'failure':receipt.get('failure')})
assert run_checks[0]['exit_code'] is None and run_checks[1]['exit_code']==0
assert (destroot/'runs/exact_sparse_check/stderr.txt').read_text()=="SubprocessError('Exception occurred in preexec_fn.')"
report=json.loads((destroot/'runs/exact_sparse_check_retry/stdout.txt').read_text())
assert all(report['checks'].values())

prior=OUT.parent/'local_conserving_control_author_exposed_check'
prior_ids={'REVIEW.md':'0f87bf70c55412bf1fca93e2c3c5c3be569b7257b4b986dc0fb084ff562273f1','FREEZE.json':'5f1dc73712ed9e82ffb30becb9d310b5d146ee2686c530b44bb83b9915dc7dfa'}
prior_rows=[]
for name,expected in prior_ids.items():
 raw=(prior/name).read_bytes();assert sha(raw)==expected
 prior_rows.append({'path':str(prior/name),'bytes':len(raw),'sha256':expected,'current_action':'Identity check only; prior source-exposed review is unchanged.'})

reader=PdfReader(pdf)
pages=list(range(8,17))
text='\n'.join(f'=== PDF PAGE {p} ===\n{reader.pages[p-1].extract_text()}\n' for p in pages)
(OUT/'PRIMARY_SCOPE.txt').write_text(text)
manifest={'utc':datetime.now(timezone.utc).isoformat(),'kind':'actual_metadata_only_capture_and_receipt_validation','source_records':rows,'all_author_freeze_members_verified':True,'author_freeze_member_count':len(freeze['members']),'author_execution_receipts_checked':run_checks,'prior_parent_review_unchanged':prior_rows,'primary_pages_extracted_and_read':pages,'author_successful_scientific_executions':1,'author_preserved_preexec_failures':1,'new_reviewer_scientific_executions':0,'science_program_replayed':False}
(OUT/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'source_records':len(rows),'author_freeze_members_verified':len(freeze['members']),'author_execution_receipts':run_checks,'primary_pages':pages,'prior_parent_review_unchanged':True,'new_reviewer_scientific_executions':0},indent=2))
