"""Independent annulus dual witness and linear-program optimum checks."""
AUDIT_TIMEOUT_SEC=120
import numpy as np
from scipy.optimize import linprog
import json
rows=[]
def ck(n,c,d=None):rows.append({'name':n,'passed':bool(c),'detail':d})
def Q(z):return np.array([np.ones(len(z)),z.real,z.imag,z.real**2,z.real*z.imag,z.imag**2])
e=np.array([1.,0,0,0,0,0]);rng=np.random.default_rng(217)
for i,(r,R) in enumerate([(.3,.33),(.2,.5),(.7,2.),(.1,1.5)]):
    bound=(R*R+r*r)/(R*R-r*r);dual=np.array([bound,0,0,-2/(R*R-r*r),0,-2/(R*R-r*r)])
    zz=rng.uniform(r,R,100)*np.exp(1j*rng.uniform(-np.pi,np.pi,100));ck('dual_witness_'+str(i),np.max(abs(dual@Q(zz)))<=1+1e-12 and dual@e==bound)
    # Six-point attaining design: two rotated equilateral triangles.
    theta=.37+np.arange(3)*2*np.pi/3
    z=np.r_[r*np.exp(1j*theta),R*np.exp(1j*theta)]
    mat=Q(z);lp=linprog(np.ones(12),A_eq=np.c_[mat,-mat],b_eq=e,bounds=(0,None),method='highs')
    assert lp.success
    u=lp.x[:6]-lp.x[6:];ck('lp_sharp_'+str(i),abs(lp.fun-bound)<1e-8 and np.max(abs(mat@u-e))<1e-10,{'optimum':float(lp.fun),'bound':bound})
    eps=.004;ck('noise_attains_'+str(i),abs(u@(eps*np.sign(u))-eps*bound)<1e-10)
    # Extra irregular points cannot reduce below the dual bound.
    zz=np.r_[z,zz[:10]];mat=Q(zz);n=len(zz);lp=linprog(np.ones(2*n),A_eq=np.c_[mat,-mat],b_eq=e,bounds=(0,None),method='highs')
    ck('augmented_lp_'+str(i),lp.success and abs(lp.fun-bound)<1e-8)
# A circle is inconsistent, even with arbitrary real weights.
z=np.exp(1j*np.arange(9)*2*np.pi/9);mat=Q(z);lp=linprog(np.ones(18),A_eq=np.c_[mat,-mat],b_eq=e,bounds=(0,None),method='highs');ck('circle_infeasible',lp.status==2)
result={'summary':{'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},'checks':rows};print(json.dumps(result,indent=2));assert not result['summary']['failed']
