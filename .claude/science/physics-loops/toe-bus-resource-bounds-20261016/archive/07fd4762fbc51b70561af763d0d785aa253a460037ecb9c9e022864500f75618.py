"""Verify source provenance and record the root's already performed analytic judgment."""
from pathlib import Path
import datetime, hashlib, json

OUT=Path(__file__).resolve().parent
N=OUT.parent
R=N/'bus_preparation_resource_exposed_check'
def sha(b): return hashlib.sha256(b).hexdigest()
def pin(p):
    b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=sha(b))
def read(p): return json.loads(p.read_text())
def write(p,x): p.write_text(json.dumps(x,indent=2)+'\n')
def main():
    assert not (OUT/'QUALIFIED_ACCEPTANCE.json').exists()
    assert sha((R/'FREEZE.json').read_bytes())=='57657ae8f3568932180c78d6504deae992650eb260e1039eb0d5fce7db7f24d4'
    assert sha((R/'REVIEW.md').read_bytes())=='f4b8ca6c62a2b5a45b2af3e5a00b9d92d9812e5cbe8bf5702cb47875a359b23f'
    freeze=read(R/'FREEZE.json')
    assert len(freeze['files'])==33
    for item in freeze['files']:
        p=R/item['path']; b=p.read_bytes()
        assert not p.is_symlink() and len(b)==item['bytes'] and sha(b)==item['sha256']
    assert {str(p.relative_to(R)) for p in R.rglob('*') if p.is_file()}=={x['path'] for x in freeze['files']}|{'FREEZE.json'}
    sources=read(R/'SOURCES.json')
    assert len(sources['sources'])==15
    for item in sources['sources']:
        b=Path(item['original']).read_bytes()
        assert b==(R/item['capture']).read_bytes()
        assert len(b)==item['bytes'] and sha(b)==item['sha256']
    run=R/'metadata_run'
    e=read(run/'EXECUTION.json'); launch=read(run/'LAUNCH.json')
    assert all(e[k]==v for k,v in launch.items())
    assert e['exit_code']==0 and not e['timed_out'] and e['scientific_executions']==0
    assert e['source_unchanged'] and e['launcher_unchanged']
    for original,copy,key in [('capture_sources.py','executed_source.py','source_sha256'),('record_capture.py','executed_launcher.py','launcher_sha256')]:
        b=(R/original).read_bytes()
        assert b==(run/copy).read_bytes() and sha(b)==e[key]
    for stream in ['stdout','stderr']:
        b=(run/stream).read_bytes()
        assert sha(b)==e[stream+'_sha256'] and len(b)==e[stream+'_bytes']
    assert (run/'stderr').read_bytes()==b''
    assert read(run/'stdout')['selected_sources']==15
    for item in read(R/'INTERRUPTION_RECOVERY.json')['original_files']:
        b=(R/item['local_preserved_copy']).read_bytes()
        assert b==Path(item['root_recovery_source']).read_bytes()
        assert len(b)==item['bytes'] and sha(b)==item['sha256']
    record=dict(accepted_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        status='qualified conditional source acceptance; unpublished; not retained audit',
        controlling_qualifications=pin(OUT/'FINAL_QUALIFICATIONS.md'),
        proposal=pin(N/'bus_preparation_resource_root_proposal/PROPOSED_LEMMAS.md'),
        proposal_freeze=pin(N/'bus_preparation_resource_root_proposal/FREEZE.json'),
        review=pin(R/'REVIEW.md'),review_freeze=pin(R/'FREEZE.json'),
        source_inventory=pin(R/'SOURCES.json'),metadata_execution=pin(run/'EXECUTION.json'),
        review_members_verified=33,current_selected_sources_verified=15,
        scientific_executions=0,historical_scientific_replays=0,
        verification_scope='Root analytic reconstruction and complete final review; source-exposed same-model composition check. Metadata does not certify mathematics.',
        result='Fixed-plant nominal duration exponent survives evolved-memory preparation and release-only moment allowances.',
        duration_exponent='72*q^2+260*q+122',
        unresolved=['native preparation and physical calibration','shrinking-bias uniformity not provided by this result','runtime target moment accuracy','physical amplitude/slew and storage','arbitrary oracle wall time','autonomous scheduling and halt/reuse'],
        editable_prompt_files_changed=[])
    write(OUT/'QUALIFIED_ACCEPTANCE.json',record)
    members=[pin(p) for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='FREEZE.json']
    write(OUT/'FREEZE.json',dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=members))
    print(json.dumps(dict(acceptance=pin(OUT/'QUALIFIED_ACCEPTANCE.json'),freeze=pin(OUT/'FREEZE.json'),source_count=15,review_members=33,scientific_executions=0)))
if __name__=='__main__': main()
