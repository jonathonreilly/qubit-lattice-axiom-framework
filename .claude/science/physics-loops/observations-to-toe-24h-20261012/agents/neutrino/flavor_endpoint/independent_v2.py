#!/usr/bin/env python3
"""Independent boundary V2: inverse spectral polynomial plus bounded solves."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import datetime
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial as Pol
import scipy
from scipy.optimize import least_squares, minimize_scalar

CENTRAL=(.0851,.3092)
SIGMA=(.0024,.0087)
S_STARTS=(.0101,.03,.1,.3,.7,.99,1.01,1.5,2.,3.,5.,7.,9.99)
U_STARTS=(0.,.02,.1,.3,.6,.95)

def direct(s,b):
    J=np.array([[b,-np.sqrt(s),0.],[-np.sqrt(s),s+2,-np.sqrt(2*(s+1))],
                [0.,-np.sqrt(2*(s+1)),s+4]])
    x,U=np.linalg.eigh(J)
    U*=np.sign(U[0])
    v=np.array([np.ones(3),(b-x)/np.sqrt(s),
                ((s+2-x)*(b-x)-s)/np.sqrt(2*s*(s+1))])
    v/=np.sqrt(np.sum(v*v,axis=0))
    w=U[0]**2
    t12=w[1]/(1-w[2]);t13=w[2];t23=U[1,2]**2/(1-w[2])
    cosine=(U[1,0]**2-t12*(1-t23)-(1-t12)*t23*t13)/(2*np.sqrt(t12*(1-t12)*t23*(1-t23)*t13))
    gaps={}
    for p in (1,2):
        xp=x**p
        gaps[str(p)]={'r21_over_31':float((xp[1]-xp[0])/(xp[2]-xp[0])),
                      'r21_over_32':float((xp[1]-xp[0])/(xp[2]-xp[1]))}
    margin=b-min(s,1.)
    return {'s':float(s),'b':float(b),'delta':float(b-s),'x':x.tolist(),
            'electron_weights':w.tolist(),'U_e_mu_tau':U.tolist(),
            'sin2_2theta13':float(4*w[2]*(1-w[2])), 'sin2_theta12':float(t12),
            'sin2_theta13':float(t13),'sin2_theta23':float(t23),
            'cos_delta_standard':float(cosine),'Jarlskog':0.,'fixed_mass_maps':gaps,
            'infinite_nonnegative_support':bool(margin>=-1e-10),
            'positivity_margin_b_minus_bmin':float(margin),
            'threshold_zero_atom':float((s-2)/(s-1)) if s>2 and abs(b-1)<1e-10 else 0.,
            'finite_positive':bool(x[0]>0),
            'checks':{'analytic_eigenvector_error':float(np.max(np.abs(U-v))),
                      'analytic_eigen_residual':float(np.max(np.abs(J@v-v*x))),
                      'analytic_orthogonality':float(np.max(np.abs(v.T@v-np.eye(3))))}}

def inverse_polynomial(a13,q12,branch):
    w3=(1+branch*np.sqrt(1-a13))/2
    w2=q12*(1-w3); w1=(1-q12)*(1-w3)
    r=Pol([0.,1.]);A=w2*r+w3; B=w2*r*r+w3;C=w2*r*r*r+w3
    h=B-A*A;N=C-2*A*B+A*A*A;Q=(1+r-A)*h-N
    F=(1+r*r-A*A-6*h)*h*h-2*(N*N+Q*Q-N*Q)
    all_roots=F.roots()
    retained=[]
    for root in all_roots:
        if abs(np.imag(root))>1e-7 or not 0<np.real(root)<1: continue
        r0=float(np.real(root))
        aa=float(A(r0));hh=float(h(r0));a1=float(N(r0)/hh);a2=1+r0-aa-a1
        dd=a2-a1
        rec={'r':r0,'polynomial_residual':float(F(r0)),
             'a0':aa,'a1':a1,'a2':a2,'beta1_squared':hh,
             'a2_minus_a1':dd}
        if dd<=0:
            rec['status']='rejected: physical positive scale requires a2>a1'
        else:
            k=2/dd;s=k*k*hh;shift=s+2-k*a1;b=shift+k*aa
            obs=direct(s,b)
            rec['scale']=k;rec['shift']=shift;rec['observables']=obs
            rec['calibration_residual']=[obs['sin2_2theta13']-a13,obs['sin2_theta12']-q12]
            rec['weight_reconstruction_error']=float(max(abs(np.array(obs['electron_weights'])-np.array([w1,w2,w3]))))
            ok=(.01<=s<=10 and min(s,1)<=b+1e-10 and b<=30)
            rec['status']='admissible within declared domain' if ok else 'rejected: outside declared domain or infinite positivity'
        retained.append(rec)
    return {'branch':'small_sin2theta13' if branch<0 else 'large_sin2theta13',
            'weights':[float(w1),float(w2),float(w3)],'polynomial_coefficients_ascending':F.coef.tolist(),
            'all_polynomial_roots':[[float(np.real(x)),float(np.imag(x))] for x in all_roots],
            'real_roots_in_open_unit_interval':retained}

def exact_central_sturm(branch):
    """Exact Sturm signs in Q(sqrt(9149)), with rational dyadic isolation."""
    import sympy as sp
    r=sp.Symbol('r');d=sp.sqrt(9149)
    w3=(1+branch*d/100)/2;w2=sp.Rational(773,2500)*(1-w3)
    A=w2*r+w3;B=w2*r*r+w3;C=w2*r*r*r+w3
    h=B-A*A;N=C-2*A*B+A*A*A;Q=(1+r-A)*h-N
    expr=(1+r*r-A*A-6*h)*h*h-2*(N*N+Q*Q-N*Q)
    P=sp.Poly(expr,r,extension=d)
    sequence=P.sturm()
    def exact_sign(value):
        value=sp.expand(value)
        b=value.coeff(d);a=sp.expand(value-b*d)
        assert a.is_Rational and b.is_Rational
        if b==0:return int(sp.sign(a))
        if a==0:return int(sp.sign(b))
        if a*b>0:return int(sp.sign(a))
        cmp=sp.sign(a*a-9149*b*b)
        return int(cmp if a>0 else -cmp)
    def variations(at):
        signs=[exact_sign(p.eval(at)) for p in sequence]
        signs=[s for s in signs if s]
        return sum(a!=b for a,b in zip(signs[:-1],signs[1:]))
    v0,v1=variations(sp.Rational(0)),variations(sp.Rational(1))
    pending=[(sp.Rational(0),sp.Rational(1),v0,v1)];isolated=[]
    while pending:
        lo,hi,vl,vh=pending.pop()
        count=vl-vh
        if count==0:continue
        if count==1 and hi-lo<sp.Rational(1,10**10):
            isolated.append({'lo':str(lo),'hi':str(hi),'lo_float':float(lo),'hi_float':float(hi)})
            continue
        mid=(lo+hi)/2;vm=variations(mid)
        pending.extend([(lo,mid,vl,vm),(mid,hi,vm,vh)])
    return {'field':'Q(sqrt(9149))','degree':P.degree(),'exact_root_count_0_1':v0-v1,
            'variations_at_0_1':[v0,v1],'isolating_intervals':sorted(isolated,key=lambda z:z['lo_float']),
            'note':'Exact polynomial root count/isolation; physical parameter classification separately numerical'}

def sb_from_su(s,u):
    bmin=min(s,1.)
    return s,bmin+(30-bmin)*u

def residual_su(params,target=CENTRAL):
    obs=direct(*sb_from_su(*params))
    return (np.array([obs['sin2_2theta13'],obs['sin2_theta12']])-target)/SIGMA

def multistart():
    runs=[];roots=[]
    for s in S_STARTS:
        for u in U_STARTS:
            fit=least_squares(residual_su,[s,u],bounds=([.01,0.],[10.,1.]),
                              ftol=1e-12,xtol=1e-12,gtol=1e-12,max_nfev=2000)
            sb=sb_from_su(*fit.x);obs=direct(*sb);norm=float(np.linalg.norm(fit.fun))
            run={'initial_s_u':[s,u],'final_s_u':fit.x.tolist(),'final_s_b':[float(t) for t in sb],
                 'scaled_residual':fit.fun.tolist(),'norm':norm,'success':bool(fit.success),
                 'status':int(fit.status),'nfev':fit.nfev,'message':fit.message}
            runs.append(run)
            if norm<1e-7 and all(np.linalg.norm(np.array(sb)-np.array([r['s'],r['b']]))>1e-6 for r in roots):roots.append(obs)
    boundary=[]
    curves=[('s=.01',lambda t:(.01,t),(0.,1.)),('s=10',lambda t:(10.,t),(0.,1.))]
    for u in (0.,1.):
        for bounds in ((.01,1.),(1.,10.)):
            curves.append((f'u={u},s={bounds}',lambda t,u=u:(t,u),bounds))
    for name,curve,bounds in curves:
        grid=np.linspace(*bounds,501)
        values=np.array([np.dot(residual_su(curve(t)),residual_su(curve(t))) for t in grid])
        mi=int(np.argmin(values));left=grid[max(0,mi-1)];right=grid[min(len(grid)-1,mi+1)]
        opt=minimize_scalar(lambda t:np.dot(residual_su(curve(t)),residual_su(curve(t))),
                            bounds=(left,right),method='bounded',options={'xatol':1e-12})
        choices=[(float(grid[mi]),float(values[mi])),(float(opt.x),float(opt.fun))]
        t,val=min(choices,key=lambda q:q[1])
        boundary.append({'name':name,'minimum_numerical_squared_scaled_residual':val,
                         'at_s_u':list(curve(t)),'grid_size':len(grid)})
    return {'starts':len(runs),'runs':runs,'distinct_admissible_roots':roots,'boundary_diagnostics':boundary}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    campaign=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
    assert not any((campaign/n).exists() for n in ('STOP_REQUESTED','USER_STOP_REQUESTED'))
    assert time.time()<json.loads((campaign/'DEADLINE.json').read_text())['deadline_epoch']
    started=time.monotonic();out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                'source_status':'root protocol only; no root code/results read',
                                'central_inputs':list(CENTRAL),'quoted_errors':list(SIGMA)}
    central=[]
    for branch in (-1,1):
        result=inverse_polynomial(*CENTRAL,branch)
        result['exact_sturm']=exact_central_sturm(branch)
        central.append(result)
    out['inverse_spectral_central']=central
    out['bounded_multistart']=multistart()
    corners=[]
    for za in (-1.96,1.96):
        for zq in (-1.96,1.96):
            target=(CENTRAL[0]+za*SIGMA[0],CENTRAL[1]+zq*SIGMA[1])
            corners.append({'input_z':[za,zq],'targets':list(target),
                            'branches':[inverse_polynomial(*target,b) for b in (-1,1)]})
    out['separate_error_rectangle_corners']=corners
    out['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out['software']={'numpy':np.__version__,'scipy':scipy.__version__}
    out['elapsed_seconds']=time.monotonic()-started
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'central':central,'multistart_roots':out['bounded_multistart']['distinct_admissible_roots'],
                      'boundary':out['bounded_multistart']['boundary_diagnostics'],
                      'elapsed_seconds':out['elapsed_seconds']},indent=2))

if __name__=='__main__':main()
