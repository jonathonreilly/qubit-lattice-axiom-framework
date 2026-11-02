#!/usr/bin/env python3
"""Reviewer mutation tests of the author runner; no author bytes are changed."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
base=Path(__file__).resolve().parent
p=base/'mass_gap_construction_exact.py';src=p.read_text()
mutations=[
('omit_normalizer','sp.diff(Z_mom,z)/Z_mom','sp.diff(Z_mom,z)'),
('omit_spatial','mult=np.exp((beta/2)*np.cos(theta))','mult=np.ones_like(theta)'),
('omit_perron','P=T*psi[None,:]/(lam*psi[:,None])','P=T/lam'),
('wrong_dagger','def qad(a): return (a[0],-a[1],-a[2],-a[3])','def qad(a): return a'),
('drop_source_log','source_cov=sp.diff(sp.log(mgf),J,H).subs({J:0,H:0})','source_cov=sp.Integer(0)'),
('wrong_cycle_power','trans=(mat*(r**4))@mat.T','trans=(mat*r)@mat.T'),
('wrong_dimension','r=iv(np.arange(1,D+1),beta)/iv(1,beta)','r=np.arange(1,D+1)*iv(np.arange(1,D+1),beta)/iv(1,beta)')]
res=[]
for name,old,new in mutations:
 assert src.count(old)==1,(name,src.count(old))
 changed=src.replace(old,new);prefix=base/('review_massgap_construction_mutant_'+name)
 sp=prefix.with_suffix('.py');sp.write_text(changed)
 t=time.monotonic();r=subprocess.run([sys.executable,str(sp)],capture_output=True,text=True,timeout=30)
 prefix.with_suffix('.stdout.json').write_text(r.stdout);prefix.with_suffix('.stderr').write_text(r.stderr)
 d=json.loads(r.stdout)
 res.append({'mutation':name,'exit':r.returncode,'seconds':time.monotonic()-t,'failed_checks':[x['name'] for x in d['checks'] if not x['passed']],'source_sha256':hashlib.sha256(sp.read_bytes()).hexdigest(),'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'stderr_bytes':len(r.stderr.encode())})
print(json.dumps({'author_source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mutations':res},indent=2))
