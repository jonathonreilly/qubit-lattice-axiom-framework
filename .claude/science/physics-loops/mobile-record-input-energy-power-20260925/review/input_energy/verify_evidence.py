"""Read-only source/result/certificate binding check; no science runner rerun."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import subprocess
import json
import sys
import numpy as np

BASE=Path(__file__).resolve().parent
def digest(data):return sha256(data).hexdigest()
def load(name):return json.loads((BASE/name).read_text())
def flow(row):return tuple(map(tuple,row['flow']))

def main():
    source=load('SOURCE_PINS.json');source_rows=[]
    for row in source['sources']:
        expected=row['sha256'];frozen=Path(row['frozen_path'])
        assert digest(frozen.read_bytes())==expected
        if 'path' in row:assert digest(Path(row['path']).read_bytes())==expected
        if 'git_revision' in row:
            data=subprocess.check_output(['git','-C',row['git_repository'],'show',
                                          row['git_revision']+':'+row['git_path']])
            assert digest(data)==expected
        source_rows.append({'sha256':expected,'frozen_copy_and_available_origin_match':True})
    code_pairs=[('magnetic_increment_control.py','MAGNETIC_CONTROL_RESULTS.json'),
                ('combinatorial_formula_check.py','COMBINATORIAL_RESULTS.json'),
                ('electric_and_coefficients_check.py','ELECTRIC_RESULTS.json'),
                ('energy_form_control.py','ENERGY_FORM_RESULTS.json')]
    bindings=[]
    for code,result in code_pairs:
        data=load(result);actual=digest((BASE/code).read_bytes())
        assert data['source_sha256']==actual
        bindings.append({'code':code,'code_sha256':actual,'result':result,
                         'result_sha256':digest((BASE/result).read_bytes())})
    assert source['freeze_code_sha256']==digest((BASE/'freeze_inputs.py').read_bytes())
    cert_rows=[]
    for side in (6,8):
        path=f'LAURENT_DATA_L{side}.json';data=load(path);data_hash=digest((BASE/path).read_bytes())
        for result,key in [('MAGNETIC_CONTROL_RESULTS.json','data_sha256'),
                           ('ELECTRIC_RESULTS.json','input_data_sha256'),
                           ('ENERGY_FORM_RESULTS.json','input_data_sha256')]:
            assert next(row for row in load(result)['rows'] if row['side']==side)[key]==data_hash
        terms=load(f'SURFACE_DECOMPOSITION_L{side}.json')
        reconstructed={():data['summary']['defect_constant']}
        for term in terms:
            ff=flow(term);assert term['cos_coefficient']%2==0
            coefficient=term['cos_coefficient']//2
            reconstructed[ff]=coefficient
            reconstructed[tuple((ed,-pw) for ed,pw in ff)]=coefficient
            accumulation={}
            for surf in term['plaquette_surface']:
                for ed,pw in surf['plaquette_flow']:
                    accumulation[ed]=accumulation.get(ed,0)+surf['sign']*pw
            assert tuple(sorted((ed,pw) for ed,pw in accumulation.items() if pw))==ff
        actual={flow(row):row['coefficient'] for row in data['haar_defect_polynomial']}
        assert reconstructed==actual
        prepared={flow(row):row['coefficient'] for row in data['prepared_polynomial']}
        empty={flow(row):row['coefficient'] for row in data['empty_polynomial']}
        diff={k:prepared.get(k,0)-empty.get(k,0) for k in set(prepared)|set(empty)}
        assert {k:v for k,v in diff.items() if v}==actual
        assert not data['haar_killed_polynomial']
        constant=data['summary']['defect_constant']
        assert sum(actual.values())==constant+418
        assert len(terms)==70
        assert sum(term['cos_coefficient']*len(term['plaquette_surface'])**2 for term in terms)==436
        cert_rows.append({'side':side,'primitive_minus_empty_equals_combinatorial_certificate_exact':True,
                          'all_surface_sums_exact':True,'data_sha256':data_hash})
    for row in load('COMBINATORIAL_RESULTS.json')['rows']:
        name=f"SURFACE_DECOMPOSITION_L{row['side']}.json"
        assert row['surface_certificate_sha256']==digest((BASE/name).read_bytes())
    stderrs=['MAGNETIC_CONTROL_STDERR.txt','COMBINATORIAL_STDERR.txt','ENERGY_FORM_STDERR.txt',
             'ELECTRIC_STDERR.txt','SOURCE_FREEZE_STDERR.txt']
    assert all((BASE/name).read_bytes()==b'' for name in stderrs)
    assert b'No such file or directory' in (BASE/'COMBINATORIAL_FIRST_PATH_FAILURE_STDERR.txt').read_bytes()
    assert not (BASE/'COMBINATORIAL_FIRST_PATH_FAILURE_STDOUT.txt').read_bytes()
    print(json.dumps({'verified_utc':datetime.now(timezone.utc).isoformat(),
                      'source_origin_rows':source_rows,'code_result_bindings':bindings,
                      'coefficient_certificate_rows':cert_rows,
                      'successful_control_stderrs_all_empty':True,
                      'initial_path_failure_preserved':True,
                      'python':sys.version,'numpy':np.__version__,
                      'scope':'mechanical verification of prior independently executed controls; no author or primary rerun',
                      'verifier_sha256':digest(Path(__file__).read_bytes())},indent=2))

if __name__=='__main__':main()
