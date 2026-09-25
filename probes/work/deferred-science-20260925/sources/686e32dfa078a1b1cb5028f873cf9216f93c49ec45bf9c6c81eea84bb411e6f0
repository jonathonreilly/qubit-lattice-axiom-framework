#!/usr/bin/env python3
"""Reverify the allowed exact sources and complete control receipts only."""
import ast
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def sha(data):return hashlib.sha256(data).hexdigest()


def verify(path,row):
    assert path.is_file() and not path.is_symlink(),str(path)
    data=path.read_bytes()
    assert sha(data)==row['sha256'],str(path)
    assert len(data)==row['bytes'],str(path)
    return data


def git_blob(repo,spec):
    p=subprocess.run(['git','-C',repo,'show',spec],capture_output=True,check=True)
    assert p.stderr==b''
    return p.stdout


def main():
    pins=json.loads((ROOT/'SOURCE_PINS.json').read_text())
    checked=[]
    for row in pins['scientific_sources']:
        data=verify(ROOT/row['snapshot'],row)
        spec=row['revision']+':'+row['git_path']
        assert git_blob(row['repository'],spec)==data
        assert (ROOT/row['snapshot']).stat().st_mode & 0o222==0
        checked.append({'git_source':spec,'sha256':row['sha256'],'bytes':len(data)})
    for row in pins['supplied_prior_lower_bound']:
        assert verify(Path(row['source']),row)==verify(ROOT/row['snapshot'],row)
    prior_seal=json.loads((ROOT/'sources/RECENT_BIRTH_PRE_SEAL.json').read_text())
    assert prior_seal['files']['PRE.md']==pins['supplied_prior_lower_bound'][0]['sha256']
    for row in pins['instructions']:
        data=verify(ROOT/row['snapshot'],row)
        if row['source'].startswith('git:'):
            spec=row['source'][4:]
            assert git_blob(pins['scientific_sources'][0]['repository'],spec)==data
        else:assert Path(row['source']).read_bytes()==data
    for row in pins['own_evidence']:verify(ROOT/row['path'],row)

    attempts=[]
    for attempt,result_name in [(1,'CONTROL_ATTEMPT_1_RESULTS.json'),(2,'INDEPENDENT_SOURCE_AGE_RESULTS.json')]:
        name=f'CONTROL_ATTEMPT_{attempt}'
        execution=json.loads((ROOT/(name+'_EXECUTION.json')).read_text())
        assert execution['returncode']==0
        for rel,row in execution['files'].items():
            target=result_name if rel=='INDEPENDENT_SOURCE_AGE_RESULTS.json' else rel
            verify(ROOT/target,row)
        result_bytes=(ROOT/result_name).read_bytes()
        assert result_bytes==(ROOT/(name+'.stdout.txt')).read_bytes()
        assert (ROOT/(name+'.stderr.txt')).read_bytes()==b''
        result=json.loads(result_bytes)
        assert result['source_sha256']==sha((ROOT/(name+'_SOURCE.py')).read_bytes())
        attempts.append({'attempt':attempt,'exit_code':0,'elapsed_seconds':execution['elapsed_seconds'],
                         'result':result_name,'result_sha256':sha(result_bytes),'stderr_bytes':0})
    final=json.loads((ROOT/'INDEPENDENT_SOURCE_AGE_RESULTS.json').read_text())
    assert (ROOT/'independent_source_age_controls.py').read_bytes()==(ROOT/'CONTROL_ATTEMPT_2_SOURCE.py').read_bytes()
    rows=final['primitive_graded_sources']['rows'];assert len(rows)==12
    for row in rows:
        assert row['first_high_grade_row_coefficient_norm2_orders_0_to_3']==['0','0',row['R_norm2'],'0']
        assert row['second_high_grade_row_coefficient_norm2_orders_0_to_3']==['0']*4
    boundary=[r for r in rows if r['domain']=='spin_one' and r['input']=='one_face_circulation']
    assert [(r['mark'],r['B_norm2'],r['R_norm2']) for r in boundary]==[('plus','0','0'),('minus','1','1'),('coherent','1','1')]
    max_error=max(r['age_quadrature_absolute_mean_error'] for r in final['scalar_age_moments']['rows'])
    assert max_error<5.6e-12
    imports=[]
    for node in ast.parse((ROOT/'independent_source_age_controls.py').read_text()).body:
        if isinstance(node,ast.Import):imports.extend(n.name for n in node.names)
        if isinstance(node,ast.ImportFrom):imports.append(node.module)
    assert set(imports)=={'collections','functools','fractions','itertools','math','pathlib','hashlib','json','time'}
    record={
        'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Exact source identity and complete evidence verification; no author source or primary control execution',
        'scientific_git_sources':checked,
        'supplied_prior_PRE_and_seal_bytes_verified':True,
        'prior_historical_packet_members_not_reverified':True,
        'instruction_sources_verified':len(pins['instructions']),
        'own_evidence_files_verified':len(pins['own_evidence']),
        'control_executions':attempts,
        'primitive_rows':len(rows),
        'scalar_age_rows':len(final['scalar_age_moments']['rows']),
        'envelope_rows':len(final['age_envelope_exponents']['rows']),
        'maximum_scalar_age_quadrature_error':max_error,
        'control_imports':imports,
        'PRE_sha256':sha((ROOT/'PRE.md').read_bytes()),
        'SOURCE_PINS_sha256':sha((ROOT/'SOURCE_PINS.json').read_bytes()),
        'current_root_candidate_read':False,
        'delegation_used':False,
        'large_parent_calculation_repeated':False,
        'audit_verdict':None,
    }
    data=json.dumps(record,indent=2)+'\n'
    (ROOT/'SOURCE_EVIDENCE_CHECK.json').write_text(data)
    print(data,end='')


if __name__=='__main__':main()
