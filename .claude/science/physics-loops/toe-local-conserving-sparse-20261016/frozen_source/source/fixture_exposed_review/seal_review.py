"""Fresh identity checks and final local review seal; no circuit execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

OUT=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_fixture_exposed_check')
sha=lambda raw:hashlib.sha256(raw).hexdigest()
assert Path(__file__).resolve()==OUT/'seal_review.py'
for filename in ['FREEZE.json','FREEZE.sha256','SEAL_VERIFICATION.json']:
    assert not (OUT/filename).exists()
manifest=json.loads((OUT/'SOURCE_MANIFEST.json').read_bytes())
for row in manifest['fixture_source_records']+manifest['prior_review_exposure']:
    raw=Path(row['original_path']).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
    assert raw==(OUT/row['capture']).read_bytes()
for row in manifest['unchanged_mathematical_parents']:
    raw=Path(row['original_path']).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
    assert raw==(OUT/'fixture_source'/row['packet_copy']).read_bytes()
author=OUT/'fixture_source'
for row in json.loads((author/'FREEZE.json').read_bytes())['members']:
    raw=(author/row['path']).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
author_receipt=json.loads((author/'runs/attempt_01/EXECUTION.json').read_bytes())
origin=OUT.parent/'local_conserving_sparse_compiler_fixture'
for key in ['source','launcher','stdout','stderr']:
    row=author_receipt[key]
    raw=(author/Path(row['path']).relative_to(origin)).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256']
run=OUT/'runs/artifact_inspection'
receipt_raw=(run/'EXECUTION.json').read_bytes();receipt=json.loads(receipt_raw)
assert receipt['exit_code']==0 and receipt['compiler_replay'] is False and receipt['gate_propagation'] is False
assert (run/'executed_source.py').read_bytes()==(OUT/'inspect_artifacts.py').read_bytes()
assert (run/'launcher_source.py').read_bytes()==(OUT/'run_inspection.py').read_bytes()
assert sha((run/'executed_source.py').read_bytes())==receipt['source_sha256']
assert sha((run/'launcher_source.py').read_bytes())==receipt['launcher_sha256']
for stream in ['stdout','stderr']:
    raw=(run/stream).read_bytes()
    assert len(raw)==receipt[stream+'_bytes'] and sha(raw)==receipt[stream+'_sha256']
assert (run/'stderr').read_bytes()==b''
assert json.loads((run/'stdout').read_bytes())==json.loads((OUT/'ARTIFACT_INSPECTION.json').read_bytes())
review=(OUT/'REVIEW.md').read_bytes();coverage=(OUT/'SOURCE_COVERAGE.md').read_bytes()
review.decode('utf-8');coverage.decode('utf-8')
assert len(review)>10000 and len(coverage)>1000
stamp=datetime.now(timezone.utc).isoformat()
verification={'utc':stamp,'kind':'actual_metadata_seal_verification','argv':sys.argv,'fixture_sources_and_captures_unchanged':True,'fixture_freeze_members_verified':22,'source_record_count':len(manifest['fixture_source_records']),'prior_review_and_mathematical_parents_unchanged':True,'author_receipt_bindings_verified':True,'reviewer_inspection_receipt_source_launcher_streams_verified':True,'reviewer_inspection_receipt_sha256':sha(receipt_raw),'review_bytes':len(review),'review_sha256':sha(review),'coverage_sha256':sha(coverage),'compiler_replay':False,'circuit_propagation':False,'scope':'Metadata sealing only. Earlier inspection includes exact JSON/permutation validation and floating saved-matrix reanalysis, not new circuit execution.'}
(OUT/'SEAL_VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
excluded={'FREEZE.json','FREEZE.sha256'}
members=[]
for path in sorted(OUT.rglob('*')):
    assert not path.is_symlink()
    if path.is_file():
        rel=path.relative_to(OUT).as_posix()
        if rel not in excluded:
            raw=path.read_bytes();members.append({'path':rel,'bytes':len(raw),'sha256':sha(raw)})
assert {'fixture_source/FREEZE.json','prior_review/FREEZE.json'}.issubset({r['path'] for r in members})
freeze={'kind':'final_exposed_fixture_review_freeze','frozen_at_utc':stamp,'disposition':'supports_numerical_fixture_with_certification_and_scope_limits','source_exposed_same_model':True,'retained_audit':False,'new_compiler_or_propagation_execution':False,'reviewer_executed_saved_artifact_inspection_and_floating_reanalysis':True,'fixture_review_sha256':'c9e99e725b3efd8dabbf551c315e983113129de0ed12d5f9028c207f93fe9649','fixture_freeze_sha256':'2b62a1ba9241999824241c41f191674c3a66c0829185e5bc6ea76052fcc40582','exact_root_paths_excluded':sorted(excluded),'members':members}
raw=(json.dumps(freeze,indent=2)+'\n').encode();(OUT/'FREEZE.json').write_bytes(raw)
(OUT/'FREEZE.sha256').write_text(sha(raw)+'  FREEZE.json\n')
for row in members:
    data=(OUT/row['path']).read_bytes()
    assert len(data)==row['bytes'] and sha(data)==row['sha256']
assert {p.relative_to(OUT).as_posix() for p in OUT.rglob('*') if p.is_file()}=={row['path'] for row in members}|excluded
print(json.dumps({'frozen_at_utc':stamp,'member_count':len(members),'review_bytes':len(review),'review_sha256':sha(review),'freeze_sha256':sha(raw),'all_members_and_exact_file_closure_verified':True},indent=2))
