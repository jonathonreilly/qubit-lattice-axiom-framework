#!/usr/bin/env python3
"""Preserved formula faults for the gauge join, integer fill and third variation."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=['block04_dynamical_gauge_join_check.py','block05_integer_local_filling_check.py','block06_third_curl_variation_check.py']
import hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FAULTS=[
 ('gauge_join_missing_endpoints',0,'v=four_tensor_action(half,VAC);state=v.copy()','v=VAC.copy();state=v.copy()'),
 ('gauge_join_ignores_charge',0,'electric=lam(CHARGE)','electric=lam(0*CHARGE)'),
 ('gauge_history_missing_normalization',0,'for t in range(Nt-1)])/N','for t in range(Nt-1)])'),
 ('gauge_join_wrong_spin_multiplicity',0,'reduced=abs(state[OMEGA])**4','reduced=abs(state[OMEGA])**2'),
 ('hamiltonian_missing_electric_energy',0,'full=diags(.5*g*g*CHARGE**2','full=diags(0*g*g*CHARGE**2'),
 ('filling_wrong_orientation',1,'orientation=1 if a<b else -1','orientation=1'),
 ('filling_wrong_negative_displacement',1,'n*direction*orientation','n*orientation'),
 ('physical_curl_missing_time_divisor',1,'physical=curl/time_factor','physical=curl'),
 ('third_variation_wrong_mixed_factor',2,'C3-3*B@A+2*A@A@A','C3-2*B@A+2*A@A@A'),
 ('third_variation_missing_contact',2,'C3-3*B@A+2*A@A@A','0*C3-3*B@A+2*A@A@A'),
 ('third_variation_wrong_cubic_factor',2,'C3-3*B@A+2*A@A@A','C3-3*B@A+A@A@A'),
]

def run():
    out=ROOT/'formula_mutations_followup';out.mkdir(exist_ok=True)
    env=dict(os.environ);env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
    rows=[]
    for name,i,old,new in FAULTS:
        original=ROOT/AUDIT_INPUT_FILES[i];source=original.read_text();assert source.count(old)==1,name
        mutant=out/(name+'.py');mutant.write_text(source.replace(old,new))
        result=subprocess.run([sys.executable,str(mutant)],capture_output=True,timeout=60,env=env)
        (out/(name+'.stdout.txt')).write_bytes(result.stdout);(out/(name+'.stderr.txt')).write_bytes(result.stderr)
        rows.append({'fault':name,'original_source':original.name,'original_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'mutant_sha256':hashlib.sha256(mutant.read_bytes()).hexdigest(),'exit_code':result.returncode,'assertion_rejected':result.returncode!=0 and b'AssertionError' in result.stderr,'stderr_tail':result.stderr.decode()[-700:]})
    print(json.dumps({'harness_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'formula_faults':rows},indent=2))
    assert all(r['assertion_rejected'] for r in rows),'Declared fault survived or failed for a different reason; inspect actual output'

if __name__=='__main__':run()
