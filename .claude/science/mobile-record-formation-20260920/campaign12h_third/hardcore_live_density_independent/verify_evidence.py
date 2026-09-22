from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import numpy as np

HERE=Path(__file__).resolve().parent
def load(p):return json.loads(p.read_text())
def identity(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
checks=[]
for script,result in [('finite_sector_check.py','FINITE_SECTOR_RESULTS.json'),('fourth_order_paths.py','FOURTH_ORDER_RESULTS.json'),('density_bound_check.py','DENSITY_BOUND_RESULTS.json')]:
    stem=Path(script).stem.upper();data=load(HERE/result);receipt=load(HERE/(stem+'_RECEIPT.json'))
    assert receipt['returncode']==0 and receipt['script_sha256']==identity(HERE/script)['sha256']==data['script_sha256']
    assert receipt['command'][-1]==str(HERE/script)
    assert (HERE/(stem+'_RUN.stderr')).read_bytes()==b''
    assert (HERE/(stem+'_RUN.log')).read_bytes()==(HERE/result).read_bytes()
    checks.append({'script':identity(HERE/script),'result':identity(HERE/result),'receipt':identity(HERE/(stem+'_RECEIPT.json')),'streams':'stdout exactly equals complete JSON; stderr empty'})
current=load(HERE/'FINITE_SECTOR_RESULTS.json');prior=load(HERE/'development/before_coherence_control/FINITE_SECTOR_RESULTS.json')
for key in prior['cases']:
    row=dict(current['cases'][key]);assert row.pop('coherent_vs_resolved_controls')==[];assert row==prior['cases'][key]
max_difference=0.0
for a,b in zip(current['dynamics']['rows'],prior['dynamics']['rows']):
    assert a.keys()==b.keys()
    for key in a:
        if isinstance(a[key],(int,float)):
            difference=abs(a[key]-b[key]);max_difference=max(max_difference,difference);assert difference<1e-12
        else:assert a[key]==b[key]
assert len(current['dynamics']['rows'])==24
for key in current['dynamics']:
    if key!='rows':assert current['dynamics'][key]==prior['dynamics'][key]
case=current['cases']['cycle_6'];occ=np.array([[int(v!=0) for v in q] for q in case['charges']]);bpop=occ[:,1::2].sum(axis=1)
with np.load(HERE/'FINITE_DENSITIES.npz') as arrays:
    assert len(arrays.files)==6
    for key in arrays.files:
        rho=arrays[key]
        assert rho.shape==(27,27) and abs(np.trace(rho)-1)<1e-10
        assert np.max(abs(rho-rho.conj().T))<1e-10 and np.linalg.eigvalsh(rho).min()>-1e-10
        row=next(r for r in current['dynamics']['rows'] if r['potential']+'_'+r['instrument']==key and r['time']==1.0)
        assert abs(np.dot(np.diag(rho).real,bpop)/6-row['B_occupation_density'])<1e-12
        assert abs(np.dot(np.diag(rho).real,occ.sum(axis=1))/6-row['record_density'])<1e-12
failed=load(HERE/'failed_attempts/numpy_scalar_diag/FINITE_SECTOR_CHECK_RECEIPT.json')
assert failed['returncode']==1 and failed['script_sha256']==identity(HERE/'failed_attempts/numpy_scalar_diag/finite_sector_check.py')['sha256']
assert 'ValueError: not enough values to unpack' in (HERE/'failed_attempts/numpy_scalar_diag/FINITE_SECTOR_CHECK_RUN.stderr').read_text()
failed2=load(HERE/'failed_attempts/bitwise_float_replay/RECEIPT.json')
assert failed2['original_observed_exit_code']==failed2['reproduction_exit_code']==1
assert 'AssertionError' in (HERE/'failed_attempts/bitwise_float_replay/REPRODUCTION.stderr').read_text()
assert max_difference==failed2['maximum_difference']
out={'created_utc':datetime.now(timezone.utc).isoformat(),'scientific_checks':checks,'physical_dimensions':{k:v['physical_dimension'] for k,v in current['cases'].items()},'previous_exact_results_preserved':True,'max_float_replay_difference':max_difference,'float_replay_verification_tolerance':1e-12,'finite_density_artifact':identity(HERE/'FINITE_DENSITIES.npz'),'all_six_numeric_density_arrays_verified':True,'failures_preserved':['numpy_scalar_diag','bitwise_float_replay'],'read_boundary':'Only neutral task and own reconstruction code/results; no author new hard-core, density, homogeneous-star, ramp source or output opened.','status':'Evidence authenticates; exact controls and finite numerical coverage are distinguished.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'EVIDENCE_VERIFICATION.json').write_text(text);print(text,end='')
