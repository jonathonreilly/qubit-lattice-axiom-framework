"""Verify this review packet and write its final metadata freeze once."""
from pathlib import Path
import datetime, hashlib, json

OUT = Path(__file__).resolve().parent
FINAL = OUT/'FREEZE.json'
def sha(data): return hashlib.sha256(data).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write_json(path, data): path.write_text(json.dumps(data, indent=2)+'\n')

def main():
    if FINAL.exists():
        raise RuntimeError('Final freeze already exists; refusing a second seal.')
    sources = json.loads((OUT/'SOURCES.json').read_text())
    assert sources['metadata_only'] and sources['scientific_executions']==0
    assert len(sources['sources'])==15
    checked=[]
    for item in sources['sources']:
        original=Path(item['original']).read_bytes()
        captured=(OUT/item['capture']).read_bytes()
        assert original==captured
        assert len(captured)==item['bytes'] and sha(captured)==item['sha256']
        checked.append(item['key'])
    proposal_freeze=json.loads((OUT/'sources/proposal_freeze.json').read_text())
    proposal=next(x for x in sources['sources'] if x['key']=='proposal')
    assert len(proposal_freeze['files'])==1
    assert proposal_freeze['files'][0]['sha256']==proposal['sha256']
    assert proposal_freeze['files'][0]['bytes']==proposal['bytes']
    run=OUT/'metadata_run'
    launch=json.loads((run/'LAUNCH.json').read_text())
    receipt=json.loads((run/'EXECUTION.json').read_text())
    for key,value in launch.items(): assert receipt[key]==value
    assert receipt['exit_code']==0 and not receipt['timed_out']
    assert receipt['source_unchanged'] and receipt['launcher_unchanged']
    for actual,capture,key in [('capture_sources.py','executed_source.py','source_sha256'),
                                ('record_capture.py','executed_launcher.py','launcher_sha256')]:
        assert (OUT/actual).read_bytes()==(run/capture).read_bytes()
        assert sha((run/capture).read_bytes())==receipt[key]
    for stream in ['stdout','stderr']:
        data=(run/stream).read_bytes()
        assert sha(data)==receipt[stream+'_sha256'] and len(data)==receipt[stream+'_bytes']
    assert (run/'stderr').read_bytes()==b''
    output=json.loads((run/'stdout').read_text())
    assert output['selected_sources']==15 and output['scientific_executions']==0
    recovery=json.loads((OUT/'INTERRUPTION_RECOVERY.json').read_text())
    for item in recovery['original_files']:
        data=(OUT/item['local_preserved_copy']).read_bytes()
        assert data==Path(item['root_recovery_source']).read_bytes()
        assert sha(data)==item['sha256'] and len(data)==item['bytes']
    write_json(OUT/'SEAL_VALIDATION.json', dict(
        checked_utc=now(), kind='metadata identity and recovery validation only',
        current_source_identities_checked=checked, upstream_source_count=15,
        proposal_freeze_member_matches=True, metadata_run_source_and_streams_match=True,
        interrupted_originals_match_root_recovery=True,
        scientific_executions=0, scientific_replays=0,
        transitive_historical_freezes_revalidated=False))
    write_json(OUT/'CHECKPOINT.json', dict(
        status='complete exposed analytical review; root acceptance pending', updated_utc=now(),
        proposal_sha256=proposal['sha256'],
        review_sha256=sha((OUT/'REVIEW.md').read_bytes()),
        conclusion='Fixed-plant nominal-duration exponent survives evolved-memory preparation with release-only moment allowances.',
        exponent='72*q^2+260*q+122',
        qualifications=['All fixed-plant spectral/calibration and compressed-inverse premises remain.',
                        'Retain U_E, actual scalar phases and the full correlated input/output.',
                        'Optional moment accuracy is relative to ideal release; no runtime target-moment claim from crude trace bounds.',
                        'Physical amplitude/slew needs its own pointwise certificates; arbitrary prescribed strength ceiling is not supplied.',
                        'Tighten actual phase/timing precision budgets where required; polynomial requests are not physical or oracle wall-time suppliers.',
                        'Rational-M target repair has a separate external trace budget and uniform target certificates.',
                        'Shrinking-bias uniformity, autonomous clock, memory storage, halt/reset/reuse remain outside this result.'],
        scientific_executions=0, metadata_capture_executions=1,
        failed_metadata_executions=0, interruption_preserved='INTERRUPTION_RECOVERY.json',
        original_partial_review_sha256='c9174369fd3d3143b570b8708d912c4c3f330871a7d97e561fa35eb1b724eaa4',
        editable_prompt_files_changed=[], canonical_or_git_actions=False,
        next_decision='Root to inspect and accept, qualify or reject the frozen source review.'))
    members=[]
    for file in sorted(OUT.rglob('*')):
        if file.is_symlink(): raise RuntimeError(f'Symlink in packet: {file}')
        if file.is_file() and file != FINAL:
            data=file.read_bytes()
            members.append(dict(path=str(file.relative_to(OUT)), bytes=len(data), sha256=sha(data)))
    write_json(FINAL, dict(frozen_utc=now(), kind='final exposed analytical review freeze',
                          scientific_executions=0, metadata_capture_executions=1,
                          member_count=len(members), files=members,
                          scope='All local packet files except this root FREEZE.json. Historical nested freezes are included as provenance only.'))
    for item in members:
        data=(OUT/item['path']).read_bytes()
        assert len(data)==item['bytes'] and sha(data)==item['sha256']
    print(json.dumps(dict(status='sealed and member hashes verified', members=len(members),
                          review_bytes=(OUT/'REVIEW.md').stat().st_size,
                          review_sha256=sha((OUT/'REVIEW.md').read_bytes()),
                          freeze_bytes=FINAL.stat().st_size, freeze_sha256=sha(FINAL.read_bytes()),
                          scientific_executions=0)))

if __name__=='__main__': main()
