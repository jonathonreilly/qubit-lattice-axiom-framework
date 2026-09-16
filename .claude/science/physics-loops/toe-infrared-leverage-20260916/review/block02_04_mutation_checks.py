#!/usr/bin/env python3
"""Actual source perturbations of the new reference-vertex checks."""
import hashlib,json,os,subprocess,sys,tempfile,time
from pathlib import Path
p=Path(__file__).resolve().parents[1]
files={2:p/'evidence/block02_one_photon_vertex_check.py',3:p/'evidence/block03_infrared_vertex_check.py',4:p/'evidence/block04_coupled_vacuum_check.py'}
cases=[
(2,'gram_factor','U.T@As@ddf@As@U/(2*g*g)','U.T@As@ddf@As@U/(4*g*g)'),
(2,'midpoint_mean_missing','m_mid+t/2-m_end','t/2-m_end'),
(2,'final_mean_missing','m_mid+t/2-m_end','m_mid+t/2'),
(2,'raising_vertex_sign','m_mid+t/2-m_end','m_mid-t/2-m_end'),
(2,'vertex_gram_normalization','expected=math.sqrt(2)*g*matfun(Gep,-.5)','expected=math.sqrt(2)*g*np.eye(len(Gep))'),
(2,'vertex_root_two','expected=math.sqrt(2)*g*','expected=g*'),
(3,'transverse_projector','p=1-x/w2[mask]','p=np.ones_like(w)'),
(3,'inverse_energy_power','np.sum(p/w**3)','np.sum(p/w**2)'),
(3,'jacobian_power','(1-rr*rr*n*n/4)**(-.5)','(1-rr*rr*n*n/4)**(.5)'),
(3,'quartic_coefficient','predicted4=lam**4/(96*math.pi**2)','predicted4=lam**4/(48*math.pi**2)'),
(3,'quadratic_coefficient','base=lam*lam/(6*math.pi**2)','base=lam*lam/(4*math.pi**2)'),
(3,'logarithmic_coefficient','c=1/(3*math.pi**2)','c=1/(2*math.pi**2)'),
(4,'paired_factor','observed=2*value/V','observed=value/V'),
(4,'photon_only_denominator','den=w+e+e2','den=w'),
(4,'current_midpoint_phase','xx@k+k[i]/2','xx@k-k[i]/2'),
(4,'current_reverse_sign','+=1j*phase*T[i].conj().T','+=-1j*phase*T[i].conj().T'),
(4,'pauli_projector_factor','out=.5*((1+','out=1.*((1+'),
(4,'photon_normalization','math.sqrt(2*w)','math.sqrt(w)')]
helper=p/'evidence/block01_affine_theta_check.py';env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1');results=[]
with tempfile.TemporaryDirectory(prefix='toe-vertex-mutations-') as temp:
    (Path(temp)/helper.name).write_bytes(helper.read_bytes())
    for family,name,old,new in cases:
        source=files[family].read_text();assert source.count(old)==1,(name,source.count(old))
        dest=Path(temp)/(name+'.py');dest.write_text(source.replace(old,new));started=time.time()
        r=subprocess.run([sys.executable,str(dest)],capture_output=True,text=True,timeout=120,env=env)
        row={'name':name,'source':str(files[family].relative_to(p)),'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest() if family==2 else None,'old':old,'new':new,'returncode':r.returncode,'rejected_by_assertion':r.returncode!=0 and 'AssertionError' in r.stderr,'stdout':r.stdout,'stderr':r.stderr,'seconds':time.time()-started};results.append(row)
        print(name,'REJECTED' if row['rejected_by_assertion'] else 'UNRESOLVED',flush=True)
(p/'review/BLOCK02_04_MUTATIONS.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(r['rejected_by_assertion'] for r in results)
print('All18 actual changes rejected at assertions. A particle-hole basis phase is not tested by a squared norm.')
