#!/usr/bin/env python3
"""Run declared formula perturbations against the actual finite challenges.

This is author evidence of discrimination, not independent review or an audit.
Each perturbed source, stdout and stderr is preserved with its source identity.
"""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import hashlib,json,os,subprocess,sys,time

BASE=Path(__file__).resolve().parent
CASES=[
 ('bridge_cumulant_sign','bridge_cubic_check.py','-3*covariance(A,B,w)/(g*g)','+3*covariance(A,B,w)/(g*g)'),
 ('bridge_four_link_variance','bridge_cubic_check.py','math.sqrt(2*g*g*T)*nodes','math.sqrt(2*g*g*T/4)*nodes'),
 ('bridge_noise_time_weight','bridge_cubic_check.py','noise=2*g*g/delta','noise=2*g*g'),
 ('bridge_shared_link_metric','bridge_cubic_check.py','[0,0,0,1,1,-1,-1]','[0,0,0,-1,1,-1,-1]'),
 ('convex_transition_polynomial','convex_carrier_check.py','1+u-u**3+u**4/2','1+u-u**3+u**4/3'),
 ('convex_carrier_fourier','convex_carrier_check.py','b=(2+np.cos(omega))/3','b=(1+np.cos(omega))/3'),
 ('integer_commutation_sign','integer_filling_check.py','out[(cursor,(mu,nu))]-=1','out[(cursor,(mu,nu))]+=1'),
 ('integer_dual_orientation','integer_filling_check.py','assert derivative=={key:-val for key,val in three.items()}','assert derivative==three'),
 ('integer_witness_exponent','integer_filling_check.py','exponent=mp.mpf(1)/24','exponent=mp.mpf(1)/12'),
 ('magnetic_direct_carrier','magnetic_covariance_check.py','G=(2/3)*np.eye(M)','G=(3/3)*np.eye(M)'),
 ('magnetic_replication_rate','magnetic_covariance_check.py','small=m*base_ops[0]+n*base_ops[1]','small=(m+1)*base_ops[0]+n*base_ops[1]'),
 ('magnetic_positive_majorant','magnetic_covariance_check.py','B=abs(C);P=len(C)','B=C;P=len(C)'),
]


def main():
    start=time.monotonic();rows=[]
    root=BASE/'formula_faults';root.mkdir(exist_ok=True)
    env=os.environ.copy();env['PYTHONPATH']=str(BASE)
    for name,filename,old,new in CASES:
        source=BASE/filename;body=source.read_text()
        assert body.count(old)==1,(name,body.count(old))
        mutant=root/(name+'.py');mutant.write_text(body.replace(old,new))
        run=subprocess.run([sys.executable,str(mutant)],cwd=BASE,env=env,capture_output=True,timeout=120)
        stdout=root/(name+'.stdout.txt');stderr=root/(name+'.stderr.txt')
        stdout.write_bytes(run.stdout);stderr.write_bytes(run.stderr)
        assert run.returncode!=0,(name,'PERTURBATION_NOT_REJECTED')
        assert b'AssertionError' in run.stderr,(name,'FAILED_FOR_OTHER_REASON',run.stderr.decode())
        rows.append(dict(name=name,original_file=filename,old=old,new=new,
                         original_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                         mutant_sha256=hashlib.sha256(mutant.read_bytes()).hexdigest(),
                         exit_code=run.returncode,stderr_tail=run.stderr.decode().splitlines()[-6:],
                         stdout_file=str(stdout.relative_to(BASE)),stderr_file=str(stderr.relative_to(BASE))))
    helper=BASE/'bridge_cubic_check.py'
    out=dict(status='DECLARED_FORMULA_FAULTS_REJECTED',scope=__doc__,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             helper_sha256={helper.name:hashlib.sha256(helper.read_bytes()).hexdigest()},
             cases=rows,elapsed_seconds=time.monotonic()-start)
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
