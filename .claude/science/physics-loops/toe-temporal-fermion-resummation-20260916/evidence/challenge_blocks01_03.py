#!/usr/bin/env python3
"""Run declared formula faults; preserve each actual source and output stream.

These checks challenge finite implementations. They are not independent audits
of the general theorems or evidence that untested faults cannot survive.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[
    'block01_temporal_resummation_check.py',
    'block02_physical_curl_hessian_check.py',
    'block03_open_boundary_hamiltonian_check.py',
]
import hashlib,json,os,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
FAULTS=[
 ('run_weight_missing_x',0,'direct+=delta*x**(r+1)*','direct+=delta*x**r*'),
 ('rectangle_missing_pair_factor',0,'rectangle+=2*kappa*kappa*w*w*','rectangle+=kappa*kappa*w*w*'),
 ('time_closure_discarded',0,'closed=(delta*x)**ell/(1-x*x*math.exp(2*b*delta))**(ell-1)','closed=(delta/(1+mu*delta-math.exp(b*delta)))**ell'),
 ('continuum_response_wrong_mass_power',0,'hess=-kappa*kappa/(2*mu**3)','hess=-kappa*kappa/(2*mu**2)'),
 ('hessian_missing_contact',1,'np.diag(second)-np.einsum','0*np.diag(second)-np.einsum'),
 ('hessian_missing_pair_factor',1,'H=2*np.real(','H=np.real('),
 ('curl_wrong_boundary_orientation',1,'zip(keys,[1,1,-1,-1])','zip(keys,[1,1,1,-1])'),
 ('schur_missing_prefactor',2,'schur=logD+np.linalg.slogdet','schur=np.linalg.slogdet'),
 ('complementary_missing_prefactor',2,'complementary=logA+np.linalg.slogdet','complementary=np.linalg.slogdet'),
 ('fock_missing_energy_shift',2,'fparts[0]+=mu*r*np.eye(len(states))','fparts[0]+=0*mu*r*np.eye(len(states))'),
 ('car_missing_creation_parity',2,'s2=(-1)**((after&((1<<i)-1)).bit_count())','s2=1'),
 ('exterior_missing_scalar_prefactor',2,'F=math.exp(np.linalg.slogdet(A)[1]-2*r*math.log1p(mu*delta))*exterior','F=exterior'),
]

def run():
    outdir=ROOT/'formula_mutations';outdir.mkdir(exist_ok=True)
    env=dict(os.environ);env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
    rows=[]
    for name,which,old,new in FAULTS:
        original=ROOT/AUDIT_INPUT_FILES[which];source=original.read_text()
        assert source.count(old)==1,(name,'mutation target must occur exactly once')
        mutant=outdir/(name+'.py');mutant.write_text(source.replace(old,new))
        result=subprocess.run([sys.executable,str(mutant)],capture_output=True,env=env,timeout=60)
        (outdir/(name+'.stdout.txt')).write_bytes(result.stdout)
        (outdir/(name+'.stderr.txt')).write_bytes(result.stderr)
        assertion=b'AssertionError' in result.stderr
        rows.append({'fault':name,'original_source':original.name,'original_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'mutant_sha256':hashlib.sha256(mutant.read_bytes()).hexdigest(),'exit_code':result.returncode,'assertion_rejected':result.returncode!=0 and assertion,'stderr_tail':result.stderr.decode()[-700:]})
    print(json.dumps({'harness_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'formula_faults':rows},indent=2))
    assert all(row['assertion_rejected'] for row in rows),'A declared fault survived or failed for a non-assertion reason; inspect all preserved streams'

if __name__=='__main__':run()
