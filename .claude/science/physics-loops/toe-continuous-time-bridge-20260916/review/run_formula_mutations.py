#!/usr/bin/env python3
"""Run actual altered programs and retain every source and raw result.
These checks probe assertion sensitivity; they are not independent review.
"""
import hashlib,json,subprocess,sys,time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CASES=[
 ('02_variance_factor','block02_calibrated_transfer_check.py','target=delta*g*g*N*N/(4*math.pi**2)','target=delta*g*g*N*N/(2*math.pi**2)'),
 ('02_alias_normalization','block02_calibrated_transfer_check.py','return weights.sum(axis=0)/denom','return weights.sum(axis=0)/(2*denom)'),
 ('02_poisson_variance_factor','block02_calibrated_transfer_check.py','dual=1-2*J*moments(J)[0]','dual=1-J*moments(J)[0]'),
 ('02_four_links_as_one','block02_calibrated_transfer_check.py','T=(M*lam[None,:]**4)@M','T=(M*lam[None,:])@M'),
 ('02_spatial_factor','block02_calibrated_transfer_check.py','np.sqrt(spatial(delta/(2*g*g),N))','np.sqrt(spatial(delta/(g*g),N))'),
 ('02_gauss_basis_normalization','block02_calibrated_transfer_check.py','/math.sqrt(dim)','/math.sqrt(N)'),
 ('02_restore_tiny_gap_roundoff','block02_calibrated_transfer_check.py','return -math.log1p(-deficit)/delta','return -math.log(float(characters(c,N)[r]))/delta'),
 ('03_product_factor','block03_all_mode_and_states_check.py','a=4*q/(1+q)**2','a=2*q/(1+q)**2'),
 ('03_false_strong_floor','block03_all_mode_and_states_check.py','(2*g*g/math.pi**2)*r*r','g*g*r*r'),
 ('03_reversed_charge_offset','block03_all_mode_and_states_check.py','lam[(n-1)%N]**j','lam[(n+1)%N]**j'),
 ('03_reversed_winding_hop','block03_all_mode_and_states_check.py','h[0,3]=-hop*np.exp(-1j*phi)','h[0,3]=-hop*np.exp(1j*phi)'),
 ('03_unsandwiched_transfer','block03_all_mode_and_states_check.py','T=(M*qdiag[None,:])@M','T=(M*qdiag[None,:])'),
 ('03_missing_gibbs_normalization','block03_all_mode_and_states_check.py','eigh(actual/z-ref/Z,eigvals_only=True)','eigh(actual-ref/Z,eigvals_only=True)'),
 ('03_wrong_gauss_charge','block03_all_mode_and_states_check.py','charge=np.eye(4,dtype=int)[j]-np.eye(4,dtype=int)[0]','charge=np.eye(4,dtype=int)[0]-np.eye(4,dtype=int)[j]'),
]

def run():
    out=ROOT/'review'/'formula_mutations';out.mkdir(exist_ok=True)
    rows=[]
    for name,source,old,new in CASES:
        src=ROOT/'evidence'/source;body=src.read_text();assert body.count(old)==1,(name,body.count(old))
        mutated=body.replace(old,new);target=out/(name+'.py');target.write_text(mutated)
        started=time.time();result=subprocess.run([sys.executable,str(target)],capture_output=True,text=True,timeout=180)
        (out/(name+'.stdout.txt')).write_text(result.stdout);(out/(name+'.stderr.txt')).write_text(result.stderr)
        rows.append({'mutation':name,'original_source':str(src.relative_to(ROOT)),'original_sha256':hashlib.sha256(body.encode()).hexdigest(),'mutant_sha256':hashlib.sha256(mutated.encode()).hexdigest(),'exit':result.returncode,'assertion_rejection':result.returncode!=0 and 'AssertionError' in result.stderr,'seconds':time.time()-started})
    report={'harness_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'all_assertion_rejections':all(r['assertion_rejection'] for r in rows)}
    (out/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
    assert report['all_assertion_rejections']

if __name__=='__main__':run()
