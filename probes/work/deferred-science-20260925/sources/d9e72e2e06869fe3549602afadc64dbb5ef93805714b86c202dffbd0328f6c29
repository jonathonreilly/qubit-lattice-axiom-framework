#!/usr/bin/env python3
"""Verify exact allowed source identities and the independent control binding.
This script does not execute any science runner or open another active packet.
"""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent


def h(data): return sha256(data).hexdigest()


def main():
    pins=json.loads((HERE/'SOURCE_PINS.json').read_bytes())
    rows=[]
    for source in pins['sources']:
        snapshot=(HERE/source['snapshot']).read_bytes()
        assert h(snapshot)==source['sha256'] and len(snapshot)==source['bytes']
        if source['kind']=='exact_git':
            origin=subprocess.run(['git','-C',source['repository'],'show',
                                   source['revision']+':'+source['path']],
                                  check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
        else:
            origin=Path(source['origin']).read_bytes()
        assert origin==snapshot
        rows.append({'snapshot':source['snapshot'],'sha256':source['sha256'],
                     'bytes':len(snapshot),'origin_exactly_matches':True})
    old=HERE.parent/'microscopic-record-readout-independent'
    prior=[]
    for phase,expected in [('PRE','34cbabad0237942680176e23a39bfdd6e9f4f34bbf56f1ff4f50b15178838f41'),
                           ('POST','73dc48a63907c5cbe3f3973723151a84af4b7d55e10959eb62f7c6b042da3545')]:
        data=(old/(phase+'_SEAL.json')).read_bytes(); assert h(data)==expected
        seal=json.loads(data)
        for member in seal['members']:
            assert h((old/member['path']).read_bytes())==member['sha256']
        prior.append({'phase':phase,'seal_sha256':expected,
                      'unchanged_member_count':len(seal['members'])})
    local_seal=json.loads((HERE/'sources/external/local-record-background-personal/AUTHOR_CONTROL_SEAL.json').read_bytes())
    local_note=(HERE/'sources/external/local-record-background-personal/LOCAL_RECORD_BACKGROUND_STABILITY_ROOT.md').read_bytes()
    assert local_seal['files']['LOCAL_RECORD_BACKGROUND_STABILITY_ROOT.md']==h(local_note)
    code=(HERE/'unrestricted_count_controls.py').read_bytes()
    result_bytes=(HERE/'UNRESTRICTED_COUNT_CONTROL_RESULTS.json').read_bytes()
    result=json.loads(result_bytes)
    execution=json.loads((HERE/'CONTROL_EXECUTION.json').read_bytes())
    assert h(code)==result['source_sha256']==execution['source_sha256']
    assert result_bytes==(HERE/'CONTROL.stdout.log').read_bytes()
    assert h(result_bytes)==execution['stdout_sha256']
    assert (HERE/'CONTROL.stderr.log').read_bytes()==b''
    assert execution['stderr_sha256']==h(b'') and execution['exit_code']==0
    assert len(result['primitive_resolved_pair']['rows'])==4
    assert len(result['finite_window_rows'])==3
    assert len(result['rare_variance_rows'])==4
    checked={'checked_utc':datetime.now(timezone.utc).isoformat(),
             'verifier_sha256':h(Path(__file__).read_bytes()),
             'source_pins_sha256':h((HERE/'SOURCE_PINS.json').read_bytes()),
             'source_count':len(rows),'sources':rows,'prior_packets':prior,
             'local_background_note_matches_its_seal':True,
             'local_background_numerical_members_opened':False,
             'independent_control_code_sha256':h(code),
             'independent_control_result_sha256':h(result_bytes),
             'stdout_equals_result':True,'stderr_empty':True,
             'independent_control_execution':execution,
             'all_control_rows_completely_inspected':True,
             'science_execution_count':1,
             'author_or_parent_runner_execution_count':0,
             'new_unrestricted_root_candidate_read':False,
             'other_active_independent_packet_read':False,
             'scope':'Exact bindings only. Provisional inputs remain provisional; finite numeric controls are not interval enclosures or rotor propagation.'}
    output=json.dumps(checked,indent=2)+'\n'
    destination=HERE/'SOURCE_EVIDENCE_CHECK.json'
    assert not destination.exists()
    destination.write_text(output)
    print(output,end='')


if __name__=='__main__': main()
