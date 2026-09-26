#!/usr/bin/env python3
from pathlib import Path
from math import exp,log,cosh,sinh
import hashlib,json,platform
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

HERE=Path(__file__).resolve().parent
z,r=sp.symbols('z r',positive=True)
q=z**(-r)
sT=q*(3-z)*(z+1)/(4*z);sS=q*(2+7*z-5/z)/4;sS2=4*q*(z+1)/3
assert sp.simplify(sT.subs(z,1)-1)==0 and sp.simplify(sS.subs(z,1)-1)==0
assert sp.simplify(sT.subs(z,3))==0 and sp.simplify((sS-sS2).subs(z,3))==0
assert sp.simplify(sp.diff(sT,z)*4*z**(r+2)-(r*(z-3)*(z+1)-(z*z+3)))==0
assert sp.simplify(sp.diff(sS,z)*4*z**(r+2)-(-(z-1)*(14*z+20)-(r-3)*(7*z*z+2*z-5)))==0
assert sp.simplify(sp.diff(sS2,z)*3*z**(r+1)/4-((1-r)*z-r))==0
j,eps=sp.symbols('j epsilon',positive=True)
assert sp.simplify(-sp.diff(sT,z).subs({z:1,r:3/j**2})*2*eps*j*j-eps*(6+2*j*j))==0
assert sp.simplify(-sp.diff(sS,z).subs({z:1,r:3/j**2})*2*eps*j*j-6*eps*(1-j*j))==0
f=(z-1)**2/(4*z**(r+1));zs=(r+1)/(r-1)
assert sp.simplify(sp.diff(f,z).subs(z,zs))==0
# Equivalent log expression avoids symbolic power-branch assumptions.
logopt=(r-1)*sp.log(r-1)-(r+1)*sp.log(r+1)
assert sp.simplify(sp.diff(logopt,r)-sp.log((r-1)/(r+1)))==0

I=np.eye(2,dtype=complex)
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
V=np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)])
T=sum(np.kron(s,s) for s in pauli);PS=(np.eye(4)-T)/4;PT=np.eye(4)-PS
rows=[]
for coupling in [.05,.1,.25,.5,.8,.99,-.5]:
    rr=3/coupling**2
    def survival(x):
        qq=exp(-rr*x);zz=exp(x)
        if zz<=3:
            alpha=qq*(1+cosh(x))/2;beta=-qq*sinh(x)
        else:alpha=qq*(zz+1)/3;beta=-alpha
        return alpha+beta,alpha-3*beta,alpha,beta
    grid=np.unique(np.r_[0,np.geomspace(1e-9,min(2,700/rr),1000),log(3)])
    previous=np.array([1.,1.]);max_constraint=0.;max_row_error_gap=0.
    for x in grid:
        st,ss,alpha,beta=survival(float(x));eig=np.array([st,ss])
        assert eig.min()>-1e-14 and eig.max()<=1+1e-14
        assert np.max(eig-previous)<1e-14;previous=eig
        errors=[abs(alpha+beta*u-exp(-(rr+u)*x)) for u in [-1,0,1]]
        wanted=exp(-rr*x)*((cosh(x)-1)/2 if x<=log(3) else (exp(x)-2)/3)
        max_row_error_gap=max(max_row_error_gap,abs(max(errors)-wanted));assert abs(max(errors)-wanted)<1e-14
    optimum=exp((rr-1)*log(rr-1)-(rr+1)*log(rr+1))
    xstar=log((rr+1)/(rr-1))
    opt=minimize_scalar(lambda x:-exp(-rr*x)*(cosh(x)-1)/2,bounds=(xstar/4,xstar*4),method='bounded',options={'xatol':1e-14})
    assert abs(-opt.fun-optimum)<1e-12
    effects=[np.kron(I+coupling*sum(v[k]*pauli[k] for k in range(3)),I+coupling*sum(v[k]*pauli[k] for k in range(3))) for v in V]
    R=sum(effects);rt=6+2*coupling**2;rs=6*(1-coupling**2)
    Rinvroot=PT/np.sqrt(rt)+PS/np.sqrt(rs)
    marks=[Rinvroot@F@Rinvroot for F in effects]
    assert np.max(abs(sum(marks)-np.eye(4)))<1e-12
    for F,Q in zip(effects,marks):
        assert np.max(abs(F@PS-PS@F))<1e-13
        assert np.linalg.eigvalsh(Q).min()>-1e-13
        assert np.max(abs(rt*PT@Q@PT+rs*PS@Q@PS-F))<1e-12
    rows.append({'j':coupling,'r':rr,'deadline_grid_points':len(grid),'sharp_Kolmogorov_error':optimum,'maximizing_time_epsilon_one':xstar/(2*coupling**2),'numerical_maximum_error':-float(opt.fun),'pointwise_error_formula_max_residual':max_row_error_gap,'marked_initial_effects_checked':6})
result={'symbolic_checks_passed':True,'clock_cases':rows,'status':'new primary simultaneous-deadline extension; independent check pending','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'versions':{'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__}}
s=json.dumps(result,indent=2)+'\n';(HERE/'QUANTUM_DEADLINE_RESULTS.json').write_text(s);print(s,end='')
