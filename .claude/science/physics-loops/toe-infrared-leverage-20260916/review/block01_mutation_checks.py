#!/usr/bin/env python3
"""Run actual altered finite sources; successful rejection must be AssertionError."""
import hashlib,json,os,subprocess,sys,tempfile,time
from pathlib import Path
p=Path(__file__).resolve().parents[1]
cases=[
('affine','fractional_kernel','matfun(H2,-.5)@q','matfun(H2,-1)@q'),
('affine','gaussian_split_sign','T=(A-c0*A@A)/2','T=(A+c0*A@A)/2'),
('affine','mean_sign','mp=-A@grad/(2*g*g)','mp=A@grad/(2*g*g)'),
('affine','covariance_factor','A@hess@A/(4*g**4)','A@hess@A/(8*g**4)'),
('affine','hopping_midpoint','dual(cycles,A,a+t/2,g,4)','dual(cycles,A,a+t/3,g,4)'),
('affine','poisson_prefactor','(math.pi/g**2)**(cycles.shape[1]/2)','(2*math.pi/g**2)**(cycles.shape[1]/2)'),
('ring','electric_coulomb_factor','g*g/2*(coulomb[c]@coulomb[c]+4*second)','g*g/4*(coulomb[c]@coulomb[c]+4*second)'),
('ring','hop_gaussian_factor','eta=math.exp(-g*g/32)','eta=math.exp(-g*g/16)'),
('ring','magnetic_midpoint','thmid=theta(a+.5,g)[0]','thmid=theta(a+.25,g)[0]'),
('ring','mean_square_missing','(ddF+dF*dF)/(16*g**4)','ddF/(16*g**4)'),
('ring','charge_transport_sign','dn=ds if x==L-1 else 0','dn=-ds if x==L-1 else 0'),
('ring','theta_dual_width','-math.pi**2*k*k/(2*g*g)','-math.pi**2*k*k/(g*g)')]
files={'affine':p/'evidence/block01_affine_theta_check.py','ring':p/'evidence/block01_charged_ring_compression.py'}
out=[];env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
with tempfile.TemporaryDirectory(prefix='toe-affine-mutations-') as temp:
    for family,name,old,new in cases:
        source=files[family].read_text();assert source.count(old)==1,(name,source.count(old))
        dest=Path(temp)/(name+'.py');dest.write_text(source.replace(old,new))
        started=time.time();r=subprocess.run([sys.executable,str(dest)],capture_output=True,text=True,timeout=120,env=env)
        out.append({'name':name,'source':str(files[family].relative_to(p)),'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'old':old,'new':new,'returncode':r.returncode,'rejected_by_assertion':r.returncode!=0 and 'AssertionError' in r.stderr,'stdout':r.stdout,'stderr':r.stderr,'seconds':time.time()-started})
        print(name, 'REJECTED' if out[-1]['rejected_by_assertion'] else 'UNRESOLVED',flush=True)
(p/'review/BLOCK01_MUTATIONS.json').write_text(json.dumps(out,indent=2)+'\n')
assert all(x['rejected_by_assertion'] for x in out)
print('All 12 actual changes rejected at assertions. Personal checks only.')
