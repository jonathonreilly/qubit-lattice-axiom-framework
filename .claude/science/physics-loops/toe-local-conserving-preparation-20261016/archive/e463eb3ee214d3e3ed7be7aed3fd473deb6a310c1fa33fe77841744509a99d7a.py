"""Metadata-only validation and immutable final inventory of this review packet."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

OUT = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_control_author_exposed_check')
sha=lambda b:hashlib.sha256(b).hexdigest()
assert not (OUT/'FREEZE.json').exists()
assert not (OUT/'FREEZE.sha256').exists()
manifest=json.loads((OUT/'SOURCE_MANIFEST.json').read_text())
for row in manifest['source_records']:
    original=Path(row['original_path']).read_bytes()
    captured=(OUT/row['capture']).read_bytes()
    assert len(original)==len(captured)==row['bytes']
    assert sha(original)==sha(captured)==row['sha256']
for row in manifest['prior_root_only_exposure_unchanged']:
    raw=Path(row['path']).read_bytes()
    assert len(raw)==row['bytes'] and sha(raw)==row['sha256']

run=OUT/'runs'/'source_capture'
receipt=json.loads((run/'EXECUTION.json').read_text())
assert receipt['exit_code']==0 and receipt['scientific_execution'] is False
assert sha((run/'executed_source.py').read_bytes())==receipt['source_sha256']
assert (run/'executed_source.py').read_bytes()==(OUT/'capture_sources.py').read_bytes()
assert sha((run/'launcher_source.py').read_bytes())==receipt['launcher_sha256']
assert (run/'launcher_source.py').read_bytes()==(OUT/'run_metadata_capture.py').read_bytes()
for name in ['stdout','stderr']:
    raw=(run/name).read_bytes()
    assert len(raw)==receipt[name+'_bytes'] and sha(raw)==receipt[name+'_sha256']
assert receipt['stderr_bytes']==0
actual=json.loads((run/'stdout').read_text())
assert actual['source_records']==13 and actual['author_freeze_members_verified']==12
assert actual['all_identities_match'] and actual['prior_root_exposure_unchanged']
finding=json.loads((OUT/'SEARCH_RECEIPT_FINDING.json').read_text())
assert finding==actual['search_receipt_finding']
assert finding['saved_regex_arguments_equal']

verification={
 'utc':datetime.now(timezone.utc).isoformat(),
 'kind':'metadata_integrity_validation_not_scientific_execution',
 'all_13_source_records_rechecked_at_seal':True,
 'all_12_author_freeze_members_verified':True,
 'prior_root_only_review_and_freeze_unchanged':True,
 'source_at_launch_and_launcher_match_current_scoped_sources':True,
 'full_stream_lengths_and_hashes_match':True,
 'metadata_exit_code':0,
 'scientific_executions':0,
 'readiness_energy_extension_counterexample':'analytical calculation in REVIEW.md, not an executable result',
 'root_acceptance':'pending',
 'editable_prompt_changes':[],
}
(OUT/'SEAL_VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
members=[]
excluded={'FREEZE.json','FREEZE.sha256'}
for p in sorted(OUT.rglob('*')):
    relative=str(p.relative_to(OUT))
    if p.is_file() and relative not in excluded:
        raw=p.read_bytes()
        members.append({'path':relative,'bytes':len(raw),'sha256':sha(raw)})
assert 'author_source/FREEZE.json' in {r['path'] for r in members}
freeze={
 'utc':datetime.now(timezone.utc).isoformat(),
 'packet':str(OUT),
 'status':'sealed_qualified_source_exposed_analytical_review',
 'source_derivation_sha256':'c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60',
 'source_freeze_sha256':'3128a438f020588eb8e8e945b1cbe9f4e6d64f5524831e19e530ff28a1e08c9b',
 'prior_root_only_exposure_freeze_sha256':'f17710dd8d161053aa6f8168496dc739aeea8488105c422d834e274a2cc043cd',
 'scientific_executions':0,
 'retained_audit_or_root_acceptance_claimed':False,
 'members':members,
}
raw=(json.dumps(freeze,indent=2)+'\n').encode()
(OUT/'FREEZE.json').write_bytes(raw)
(OUT/'FREEZE.sha256').write_text(sha(raw)+'  FREEZE.json\n')
review=(OUT/'REVIEW.md').read_bytes()
print(json.dumps({'member_count':len(members),'review_bytes':len(review),'review_sha256':sha(review),'freeze_bytes':len(raw),'freeze_sha256':sha(raw),'utc':freeze['utc']},indent=2))
