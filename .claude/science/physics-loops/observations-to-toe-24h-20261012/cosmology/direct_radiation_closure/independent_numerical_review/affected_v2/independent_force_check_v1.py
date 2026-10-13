#!/usr/bin/env python3
"""Affected-source independent checks. No author helper import/execution.

Differentiate in z=S^(1/6), obtain canonical N accelerations, then transform
using the actual canonical Jacobian. Author results are comparison data only.
"""
from pathlib import Path
import json,hashlib,sys
from itertools import product
import mpmath as mp

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'snapshot'
mp.mp.dps=95
CFG=json.loads((SOURCE/'OFF_TRAJECTORY_FIXTURES_v2.json').read_text())
RESULT=json.loads((SOURCE/'evidence_v2/RESULTS.json').read_text())
checks=[];evidence=[]
def m(v):return mp.mpf(str(v))
def st(v):return mp.nstr(v,85)
def check(name,ok,**kw):checks.append({'name':name,'passed':bool(ok),**kw})
def close(name,got,expected,atol='2e-12',rtol='3e-13'):
    error=abs(m(got)-expected);bound=m(atol)+m(rtol)*abs(expected)
    check(name,error<=bound,error=st(error),bound=st(bound),got=str(got),expected=st(expected))

cases=list(product(CFG['a'],CFG['R_over_S'],CFG['L_over_S'],CFG['disturbances']))
check('54 actual fixtures',len(cases)==len(RESULT['off_trajectory']['rows'])==54)
for i,((aa,rr,ll,mode),record)in enumerate(zip(cases,RESULT['off_trajectory']['rows'])):
    alpha,ratio,vac=map(m,[aa,rr,ll]);x=m(mode['x']);z0=mp.exp(x/6)
    b=ratio/z0**2;L=vac*z0**6
    check('fixture labels '+str(i),record['a']==aa and record['R_over_S']==rr and record['L_over_S']==ll and record['disturbance']==mode)
    def S(z):return z**6
    def R(z):return b*z**8
    def Hbar2(z):return 2*((1+alpha)*(S(z)+R(z))+L)/3
    def J(z):return -2*mp.sqrt(alpha)*z*z*mp.sqrt(1+4*b*z*z/3)/mp.sqrt(Hbar2(z))
    def U(z):return L+alpha*S(z)/2+alpha*R(z)/3
    def dchi(fun,z):return mp.diff(fun,z)/J(z)
    def curvature(z):return dchi(lambda q:dchi(U,q),z)
    def M(z):return alpha*dchi(S,z)**2/curvature(z)+alpha*S(z)**2/U(z)
    def potential(u,z):return U(z)-mp.sqrt(alpha)*S(z)*u+M(z)*u*u/2
    u=m(mode['u_over_sqrt_a'])*mp.sqrt(alpha)
    udot=m(mode['udot_over_sqrt_a_Hbar'])*mp.sqrt(alpha*Hbar2(z0))
    chidot=m(mode['chi_velocity_factor'])*mp.sqrt(alpha*(S(z0)+4*R(z0)/3))
    sm=m(mode['matter_factor'])*S(z0);sr=m(mode['radiation_factor'])*R(z0)
    V=potential(u,z0);Vu=mp.diff(lambda q:potential(q,z0),u);Vchi=dchi(lambda z:potential(u,z),z0)
    H2=(2*(sm+sr+V)+udot**2+chidot**2)/3;H=mp.sqrt(H2)
    w=udot/H;v=chidot/H;hN=-(sm+4*sr/3)/H2-w*w-v*v
    # Canonical N operator; transformation only after these accelerations.
    wu=-(3+hN)*w-(Vu+mp.sqrt(alpha)*sm)/H2
    wc=-(3+hN)*v-Vchi/H2
    D=z0*J(z0);p=6*v/D
    connection=(1+z0*mp.diff(J,z0)/J(z0))/6
    pp=6*wc/D-connection*p*p
    state=[u,x,w,p,mp.log(sm),mp.log(sr)]
    proper=[H2*(wu+w*hN),H2*(wc+v*hN)]
    for k,expected in enumerate(state):close('state '+str(i)+'/'+str(k),record['state'][k],expected,atol='2e-15',rtol='4e-15')
    close('H2 '+str(i),record['H2'],H2,atol='2e-14',rtol='4e-15')
    for k,expected in enumerate(proper):close('proper acceleration '+str(i)+'/'+str(k),record['canonical_accelerations'][k],expected,atol='2e-13',rtol='4e-14')
    for key in ['expected_p_accelerations','actual_p_accelerations']:
        close(key+' u '+str(i),record[key][0],wu)
        close(key+' p '+str(i),record[key][1],pp)
    denominator=3-w*w-v*v
    check('domain '+str(i),alpha>0 and b>0 and L>0 and denominator>0 and H2>0 and J(z0)<0,denominator=st(denominator))
    check('nonzero acceleration '+str(i),abs(pp)>m(CFG['minimum_abs_p_acceleration']),p_acceleration=st(pp))
    evidence.append({'fixture':i,'canonical_N_accelerations':[st(wu),st(wc)],'coordinate_N_accelerations':[st(wu),st(pp)],'H2':st(H2),'denominator':st(denominator),'chi_ell':st(D),'connection':st(connection),'omitted_force_discrepancy':st(abs(pp))})

newchecks=RESULT['checks'][1195:]
check('378 new checks',len(newchecks)==378)
for i,row in enumerate(newchecks):
    if 'actual'in row:
        e=abs(row['actual']-row['expected']);check('stored assertion '+str(i),row['passed'] and e<=row['tolerance'] and e==row['error'])
    else:check('stored force guard '+str(i),row['passed'] and abs(row['expected_p_acceleration'])>CFG['minimum_abs_p_acceleration'])

out={'review_scope':'affected v2 controls only; no author imports','checks':checks,'passed':sum(x['passed']for x in checks),'failed':sum(not x['passed']for x in checks),'rows':evidence,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
with (HERE/'FORCE_RESULTS_v1.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'passed':out['passed'],'failed':out['failed'],'failures':[x for x in checks if not x['passed']],'min_abs_p_acceleration':min(float(x['omitted_force_discrepancy'])for x in evidence),'max_abs_p_acceleration':max(float(x['omitted_force_discrepancy'])for x in evidence),'min_denominator':min(float(x['denominator'])for x in evidence)},indent=2))
sys.exit(bool(out['failed']))
