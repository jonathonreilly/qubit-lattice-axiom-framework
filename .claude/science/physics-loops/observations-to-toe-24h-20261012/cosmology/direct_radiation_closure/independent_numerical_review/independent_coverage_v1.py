#!/usr/bin/env python3
"""Additional source linkage and exhaustive row-payload checks.
Imports reviewer code only; no author helper import or execution.
"""
from pathlib import Path
import json, hashlib, sys
import numpy as np
import independent_numerics_v2 as own

O=Path(__file__).resolve().parent
a=own.AUTHOR;f=own.FIX;m=own.m;mp=own.mp
own.CHECKS.clear()
t=json.loads((O/'RESULTS_v2.json').read_text())['thermal']['thermal'][1]
omega=m(t['Omega_gamma']);details=[]
for i,row in enumerate(a['old_potential']):
    alpha,z=m(row['a']),m(row['z']);S=mp.mpf('1.5')*m(f['matter_fraction'])/(1+alpha)*(1+z)**3
    R=mp.mpf('1.5')*omega/(1+alpha)*(1+z)**4;L=m(f['old_potential_L'])
    H2=2*((1+alpha)*S+L)/3*(1+2*R/((2+alpha)*S+2*L))
    for key,val in [('S',S),('R',R),('H2_forced',H2)]:own.compare('old fixture linkage '+str(i)+' '+key,row[key],val,rtol='3e-15')
for i,row in enumerate(a['new_background']):
    alpha=m(row['a']);S0=mp.mpf('1.5')*m(f['matter_fraction'])/(1+alpha);R0=mp.mpf('1.5')*omega/(1+alpha)
    L=mp.mpf('1.5')*(1-m(f['matter_fraction'])-omega);b=R0/S0**(mp.mpf(4)/3)
    for key,val in [('S0',S0),('R0',R0),('L',L),('b',b)]:own.compare('new fixture linkage '+str(i)+' '+key,row[key],val,rtol='3e-15')
    for j,run in enumerate(row['runs']):
        for k,(N,state)in enumerate(zip(row['sites_N'],run['states'])):
            u,x,wu,p,lm,lr=map(m,state);ell=x/6
            S,R,Hb,J,U,dc,C2,M=own.canonical_functions(alpha,b,L);z=mp.exp(ell)
            V=U(z)-mp.sqrt(alpha)*S(z)*u+M(z)*u*u/2;vc=(z*J(z)/6)*p
            H2=2*(mp.exp(lm)+mp.exp(lr)+V)/(3-wu*wu-vc*vc)
            expected=2*((1+alpha)*(S0*mp.exp(-3*m(N))+R0*mp.exp(-4*m(N))))/3+2*L/3
            own.compare('stored history physical H2 '+str(i)+'/'+str(j)+'/'+str(k),H2,expected,rtol='4e-11')

lower=[c for c in a['checks'] if c['name']=='grid global transverse lower bound']
dets=[c for c in a['checks'] if c['name']=='grid Hessian determinant']
tiny=[]
for i,row in enumerate(a['local_grid']):
    alpha,b,L=map(m,[row['a'],row['R_over_S'],row['L_over_S']]);S,R,H2,J,U,dc,C2,M=own.canonical_functions(alpha,b,L);z=m(1)
    for j,c in enumerate(lower[7*i:7*i+7]):
        u=m(c['u']);V=U(z)-mp.sqrt(alpha)*S(z)*u+M(z)*u*u/2
        own.compare('actual lower-bound payload '+str(i)+'/'+str(j),c['value'],V,atol='2e-13',rtol='3e-13')
        own.compare('actual lower-bound reference '+str(i)+'/'+str(j),c['bound'],U(z)/2,rtol='3e-15')
    exactdet=alpha*S(z)**2*C2(z)/(U(z)*H2(z)**2)
    own.compare('determinant expected payload '+str(i),dets[i]['expected'],exactdet,rtol='4e-15')
    # The direct floating determinant is cancellation-conditioned, so account
    # separately for its actual error instead of claiming 14-digit precision.
    rel=abs(m(dets[i]['actual'])/exactdet-1)
    own.ck('determinant computed sign '+str(i),m(dets[i]['actual'])>0)
    tiny.append({'grid':i,'a':row['a'],'R_over_S':row['R_over_S'],'L_over_S':row['L_over_S'],'determinant_relative_error':own.s(rel),'exact_determinant':own.s(exactdet)})

for manifest in ['INPUT_RECEIPT_v1.json','PRIMARY_INPUT_RECEIPT_v1.json']:
    obj=json.loads((O/manifest).read_text());rows=obj['files']if isinstance(obj,dict)else obj
    for row in rows:
        for key in ['snapshot']:
            own.ck('snapshot hash '+str(row[key]),hashlib.sha256(Path(row[key]).read_bytes()).hexdigest()==row['sha256'])

# Exact names/hash maps differ between the author freeze and result; both are
# checked against their declared local snapshot, not guessed path aliases.
freeze=json.loads((O/'snapshot/evidence_v1/FREEZE.json').read_text())
for name,digest in a['source_hashes'].items():
    path=O/'snapshot'/('data/'+name if name=='FIRAS_monopole.txt' else name)
    own.ck('author result source pin '+name,hashlib.sha256(path.read_bytes()).hexdigest()==digest)

r={'checks':own.CHECKS,'passed':sum(c['passed']for c in own.CHECKS),'failed':sum(not c['passed']for c in own.CHECKS),'determinant_roundoff':tiny,'reviewer_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'reviewer_dependency_sha256':hashlib.sha256((O/'independent_numerics_v2.py').read_bytes()).hexdigest()}
with (O/'COVERAGE_RESULTS_v1.json').open('x')as out:json.dump(r,out,indent=2);out.write('\n')
print(json.dumps({'passed':r['passed'],'failed':r['failed'],'failures':[c for c in own.CHECKS if not c['passed']],'max_direct_determinant_relative_error':max(float(c['determinant_relative_error'])for c in tiny)},indent=2))
sys.exit(bool(r['failed']))
