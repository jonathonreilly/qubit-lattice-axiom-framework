"""Create only new POST bindings/seal; never alter prior evidence or author files."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, time

HERE=Path(__file__).resolve().parent

def digest(path):return sha256(path.read_bytes()).hexdigest()

def read(path):return json.loads(path.read_bytes())

def put(path,value):
    data=(json.dumps(value,indent=2)+'\n').encode()
    with path.open('xb') as stream:stream.write(data)
    return data

def preserved(pins):
    for row in pins['preserved_prior_files']:
        path=Path(row['path']);stat=path.stat()
        assert digest(path)==row['sha256'] and stat.st_size==row['bytes']
        assert stat.st_mtime_ns==row['mtime_ns'] and stat.st_ctime_ns==row['ctime_ns']
    for row in pins['new_source_pins']:
        assert digest(HERE/row['frozen_path'])==row['sha256']==digest(Path(row['origin']))
        assert (HERE/row['frozen_path']).stat().st_size==row['bytes']
    for row in pins['inherited_PRE_source_pins']:
        assert digest(HERE/row['frozen_path'])==row['sha256']
        if not row['origin'].startswith('git:'):
            assert digest(Path(row['origin']))==row['sha256']

def main():
    started=datetime.now(timezone.utc).isoformat();tick=time.perf_counter()
    pins=read(HERE/'POST_SOURCE_PINS.json');preserved(pins)
    executions=[]
    for name in ('post_freeze','post_inspect','post_verification','post_payload_review'):
        path=HERE/(name+'.execution.json');receipt=read(path)
        assert receipt['exit_code']==0
        assert digest(Path(receipt['command'][2]))==receipt['source_sha256']
        assert digest(HERE/'post_run_logged.py')==receipt['recorder_sha256']
        for row in receipt['outputs'].values():
            assert digest(HERE/row['path'])==row['sha256']
            assert (HERE/row['path']).stat().st_size==row['bytes']
        assert receipt['outputs']['stderr.txt']['bytes']==0
        executions.append({'path':path.name,'sha256':digest(path),**receipt})
    result=read(HERE/'post_verification.stdout.txt')
    assert result['released_author_members_verified']==27
    assert result['all_PRE_members_preserved']==54
    assert result['prior_files_byte_and_stat_preserved']==55
    bindings={'phase':'POST40 final source and evidence binding',
        'at_utc':datetime.now(timezone.utc).isoformat(),
        'report_sha256':digest(HERE/'POST.md'),
        'pins_sha256':digest(HERE/'POST_SOURCE_PINS.json'),
        'PRE_seal_sha256':digest(HERE/'PRE_SEAL.json'),
        'author_seal_sha256':digest(HERE/'post_sources/author/AUTHOR_SEAL.json'),
        'verification_stdout_sha256':digest(HERE/'post_verification.stdout.txt'),
        'prior_files_preserved':55,'PRE_members_preserved':54,
        'new_executions':executions,
        'findings':'No required mathematical repair within final author scope. Historical source gap and bounded optimizer failures preserved; stronger PRE results retain PRE provenance.',
        'author_program_executed_or_imported':False,
        'scientific_program_rerun_at_sealing':False,
        'publication_or_audit_mutation':False,
        'historical_pyc_preserved_and_not_staged':True}
    put(HERE/'POST_FINAL_BINDINGS.json',bindings)
    exclusions={'POST_SEAL.json','POST_SEAL_RECEIPT.json'}
    members=[]
    for path in sorted(HERE.rglob('*')):
        if not path.is_file():continue
        relative=str(path.relative_to(HERE))
        if relative in exclusions:continue
        if not (relative.startswith('post_') or relative.startswith('POST_') or relative=='POST.md'):continue
        members.append({'path':relative,'sha256':digest(path),'bytes':path.stat().st_size})
    seal={'phase':'Released-source bounded POST40',
          'sealed_utc':datetime.now(timezone.utc).isoformat(),
          'report':'POST.md','report_sha256':digest(HERE/'POST.md'),
          'source_pins':'POST_SOURCE_PINS.json','source_pins_sha256':digest(HERE/'POST_SOURCE_PINS.json'),
          'prior_PRE_seal_sha256':digest(HERE/'PRE_SEAL.json'),
          'released_author_seal_sha256':digest(HERE/'post_sources/author/AUTHOR_SEAL.json'),
          'members':members,
          'scope':'Scientific correspondence only, exact stored arithmetic plus scoped POST reasoning. No author program execution/import, audit verdict or publication action.',
          'all_prior_PRE_bytes_preserved':True,
          'model_and_effort_unchanged':True,'delegation':False,
          'excluded_self_referential_receipt':'POST_SEAL_RECEIPT.json',
          'next_action':'Stop after delivering report and seal hashes.'}
    put(HERE/'POST_SEAL.json',seal)
    for row in members:
        path=HERE/row['path'];assert digest(path)==row['sha256'];path.chmod(0o444)
    (HERE/'POST_SEAL.json').chmod(0o444)
    preserved(pins)
    receipt={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),
        'in_process_seconds_through_seal':time.perf_counter()-tick,
        'seal_path':str(HERE/'POST_SEAL.json'),'seal_sha256':digest(HERE/'POST_SEAL.json'),
        'report_path':str(HERE/'POST.md'),'report_sha256':digest(HERE/'POST.md'),
        'pins_sha256':digest(HERE/'POST_SOURCE_PINS.json'),
        'members':len(members),'all_member_hashes_verified':True,
        'prior_files_preserved':55,'PRE_members_preserved':54,
        'scope':'Final receipt outside content seal to avoid self-reference; no scientific calculation rerun.'}
    data=put(HERE/'POST_SEAL_RECEIPT.json',receipt)
    (HERE/'POST_SEAL_RECEIPT.json').chmod(0o444)
    print(data.decode(),end='')

if __name__=='__main__':main()
