#!/usr/bin/env python3
"""Personally derived epoch-limit checks; no observational likelihood."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import importlib.util
import json
import sys
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
FIX=json.loads((HERE/'NUMERICAL_FIXTURES_v1.json').read_text())
PARENT=HERE.parent/'direct_analytic_fluid_completion'
spec=importlib.util.spec_from_file_location('analytic_full_equations',PARENT/'check_analytic_fluid_v1.py')
FULL=importlib.util.module_from_spec(spec);spec.loader.exec_module(FULL)
CHECKS=[]


def check(name,passed,**evidence):
    CHECKS.append({'name':name,'passed':bool(passed),**evidence})


def close(name,actual,expected,atol=2e-10,rtol=2e-10):
    x,y=np.asarray(actual,float),np.asarray(expected,float)
    units=float(np.max(np.abs(x-y)/(atol+rtol*np.maximum(np.abs(x),np.abs(y)))))
    check(name,np.all(np.isfinite(x)) and units<=1,max_tolerance_units=units,actual=x.tolist(),expected=y.tolist())


def exact(name,e):
    out=sp.factor(sp.cancel(e));check(name,out==0,residual=str(out))


def dust_rhs(n,z,a):
    u,v,p,w=z
    beta=2*a/(3*(1+a));ff=.5-u+2*u*u
    denominator=3-a*v*v-beta*p*p
    if denominator<=0 or w<=0:raise ValueError(('dust limiting chart',denominator,w))
    f=2*(w+a*ff)/denominator
    hh=-w/f-a*v*v-beta*p*p
    return np.array([v,-(3+hh)*v-(-1+4*u+w)/f,
                     -(3+hh)*p-2*a*ff/(beta*f),w*(-3+a*v-2*p)])


def radiation_rhs(n,z,a):
    p,w=z;beta=a/(2*(1+a))
    denominator=3-beta*p*p
    if denominator<=0 or w<=0:raise ValueError(('radiation limiting chart',denominator,w))
    f=2*(w+a/3)/denominator;hh=-4*w/(3*f)-beta*p*p
    return np.array([-(3+hh)*p-2*a/(3*beta*f),w*(-4-2*p)])


def dust_jacobian(a,point):
    d=1/(1+a)
    if point==0:
        return np.array([[0,1,0,0],[-6*d,-1.5,0,-1.5*d],
                         [4.5*d,0,-1.5,2.25*d],[0,a,-2,0.]])
    return np.array([[0,1,0,0],[-2*d,-1.5,0,-.5*d],
                     [4.5*d,0,-1.5,.75*d],[0,3*a,-6,0.]])


def full_dust_rhs(n,z,a,nu):
    u,v,p,w,ell=z;x=np.exp(ell)
    state=np.array([np.sqrt(a)*u,x,0.,np.sqrt(a)*v,x*p,0.,x*x*w,0.])
    r=FULL.n_rhs(n,state,a,nu,1.)
    return np.array([r[0]/np.sqrt(a),r[3]/np.sqrt(a),r[4]/x-p*p,
                     r[6]/(x*x)-2*p*w,p])


def full_radiation_rhs(n,z,a,nu):
    p,w,ell=z;y=np.exp(ell)
    state=np.array([0.,0.,y,0.,0.,y*p,0.,y*y*w])
    r=FULL.n_rhs(n,state,a,nu,1.)
    return np.array([r[5]/y-p*p,r[7]/(y*y)-2*p*w,p])


def symbolic_controls():
    a=sp.symbols('a',positive=True);u,v,p,w=sp.symbols('U V P W',real=True)
    beta=2*a/(3*(1+a));ff=sp.Rational(1,2)-u+2*u*u
    f=2*(w+a*ff)/(3-a*v*v-beta*p*p)
    hh=-w/f-a*v*v-beta*p*p
    vec=sp.Matrix([v,-(3+hh)*v-(-1+4*u+w)/f,
                   -(3+hh)*p-2*a*ff/(beta*f),w*(-3+a*v-2*p)])
    matrix=vec.jacobian([u,v,p,w]);d=1/(1+a)
    lam=sp.symbols('lambda');z=lam*(lam+sp.Rational(3,2));output={}
    points=[{u:0,v:0,p:-sp.Rational(3,2),w:1},{u:-sp.Rational(1,2),v:0,p:-sp.Rational(3,2),w:3}]
    explicit=[sp.Matrix([[0,1,0,0],[-6*d,-sp.Rational(3,2),0,-3*d/2],[9*d/2,0,-sp.Rational(3,2),9*d/4],[0,a,-2,0]]),
              sp.Matrix([[0,1,0,0],[-2*d,-sp.Rational(3,2),0,-d/2],[9*d/2,0,-sp.Rational(3,2),3*d/4],[0,3*a,-6,0]])]
    polynomials=[z*z+(21+3*a)*d*z/2+27*d*d/2,z*z+(13+3*a)*d*z/2-9*d*d/2]
    for index,point in enumerate(points):
        for j,x in enumerate(vec.subs(point)):exact('dust fixed point '+str((index,j)),x)
        jac=matrix.subs(point).applyfunc(sp.factor)
        for i in range(4):
            for j in range(4):exact('dust symbolic Jacobian '+str((index,i,j)),jac[i,j]-explicit[index][i,j])
        characteristic=(lam*sp.eye(4)-jac).det()
        exact('dust characteristic polynomial '+str(index),characteristic-polynomials[index])
        output['dust_'+str(index)]={'jacobian':str(jac),'polynomial':str(sp.factor(characteristic))}
    beta=a/(2*(1+a));f=2*(w+a/3)/(3-beta*p*p);hh=-4*w/(3*f)-beta*p*p
    rad=sp.Matrix([-(3+hh)*p-2*a/(3*beta*f),w*(-4-2*p)])
    point={p:-2,w:1};jac=rad.jacobian([p,w]).subs(point).applyfunc(sp.factor)
    expected=sp.Matrix([[-1,2*d],[-2,0]])
    for j,x in enumerate(rad.subs(point)):exact('radiation fixed point '+str(j),x)
    for i in range(2):
        for j in range(2):exact('radiation Jacobian '+str((i,j)),jac[i,j]-expected[i,j])
    exact('radiation characteristic polynomial',(lam*sp.eye(2)-jac).det()-(lam*lam+lam+4*d))
    exact('dust transverse polynomial',(lam+2)*(lam+sp.Rational(5,2))-(lam*lam+sp.Rational(9,2)*lam+5))
    exact('radiation transverse polynomial',(lam+sp.Rational(3,2))*(lam+sp.Rational(7,2))-(lam*lam+5*lam+sp.Rational(21,4)))
    output['radiation']={'jacobian':str(jac),'polynomial':str(lam*lam+lam+4*d)}
    return output


def eigenvalue_controls():
    output=[]
    for a in FIX['eigenvalue_a']:
        for point in [0,1]:
            j=dust_jacobian(a,point);ev=np.linalg.eigvals(j);d=1/(1+a)
            coefficient=(21+3*a)*d/2 if point==0 else (13+3*a)*d/2
            constant=27*d*d/2 if point==0 else -9*d*d/2
            z=ev*(ev+1.5)
            close('numeric dust eigenpolynomial '+str((a,point)),np.abs(z*z+coefficient*z+constant),np.zeros(4),2e-10,0)
            if point==0:check('dust E0 negative real parts '+str(a),np.max(ev.real)<0,eigenvalues=[[float(q.real),float(q.imag)]for q in ev])
            else:check('dust E1 one positive real part '+str(a),sum(ev.real>0)==1,eigenvalues=[[float(q.real),float(q.imag)]for q in ev])
            output.append({'a':a,'point':point,'eigenvalues':[[float(q.real),float(q.imag)]for q in ev]})
        er=np.linalg.eigvals([[-1,2/(1+a)],[-2,0]])
        check('radiation radial negative real parts '+str(a),max(er.real)<0,eigenvalues=[[float(q.real),float(q.imag)]for q in er])
        output.append({'a':a,'radiation_eigenvalues':[[float(q.real),float(q.imag)]for q in er]})
    return output


def asymptotic_controls():
    rows=[]
    for a in FIX['eigenvalue_a']:
        for nu in FIX['nu']:
            for state in FIX['dust_force_states']:
                expected=dust_rhs(0.,np.array(state),a);series=[]
                for size in FIX['field_scales']:
                    got=full_dust_rhs(0.,np.r_[state,np.log(size)],a,nu)[:4]
                    series.append({'size':size,'full':got.tolist(),'maximum_error':float(max(abs(got-expected)))})
                close('full dust approaches limiting force '+str((a,nu,state)),series[-1]['full'],expected,FIX['limit_atol'],FIX['limit_rtol'])
                rows.append({'kind':'dust','a':a,'nu':nu,'state':state,'limiting':expected.tolist(),'series':series})
            for state in FIX['radiation_force_states']:
                expected=radiation_rhs(0.,np.array(state),a);series=[]
                for size in FIX['field_scales']:
                    got=full_radiation_rhs(0.,np.r_[state,np.log(size)],a,nu)[:2]
                    series.append({'size':size,'full':got.tolist(),'maximum_error':float(max(abs(got-expected)))})
                close('full radiation approaches limiting force '+str((a,nu,state)),series[-1]['full'],expected,FIX['limit_atol'],FIX['limit_rtol'])
                rows.append({'kind':'radiation','a':a,'nu':nu,'state':state,'limiting':expected.tolist(),'series':series})
        # Actual full-equation symmetric derivative in a transverse field;
        # the reduced two-coordinate systems never supply this comparison.
        size=FIX['field_scales'][-1]
        for kind in ['dust','radiation']:
            if kind=='dust':
                base=np.array([0.,size,0.,0.,-1.5*size,0.,size*size,0.]);idx=2
                expected=np.array([-5.,-4.5])
            else:
                base=np.array([0.,0.,size,0.,0.,-2*size,0.,size*size]);idx=1
                expected=np.array([-5.25,-5.])
            # Symmetric finite differences avoid calling the physical-domain
            # branch comparisons with complex Friedmann denominators.
            slope=[]
            for coordinate in [idx,idx+3]:
                plus=base.copy();minus=base.copy();plus[coordinate]+=1e-4;minus[coordinate]-=1e-4
                slope.append((FULL.n_rhs(0.,plus,a,1.,1.)[idx+3]-FULL.n_rhs(0.,minus,a,1.,1.)[idx+3])/(2e-4))
            close('full transverse '+str((kind,a)),slope,expected,2e-9,2e-9)
            rows.append({'kind':'transverse_'+kind,'a':a,'actual_slope':slope,'expected_slope':expected.tolist()})
    return rows


def history_controls():
    cfg=FIX['integration'];sites=np.linspace(0,cfg['N_end'],cfg['sites']);rows=[]
    for a in cfg['a']:
        for kind in ['dust_E0','dust_E1','radiation']:
            if kind=='radiation':
                eq=np.array([-2.,1.]);direction=np.array([.7,-.4]);func=radiation_rhs
                jac=np.array([[-1,2/(1+a)],[-2,0.]])
                full=full_radiation_rhs
            else:
                point=int(kind[-1]);eq=np.array([0.,0.,-1.5,1.])if point==0 else np.array([-.5,0.,-1.5,3.])
                direction=np.array([.3,-.2,.4,-.5]);func=dust_rhs;jac=dust_jacobian(a,point);full=full_dust_rhs
            linear=np.array([expm(jac*n)@direction for n in sites])
            eps=cfg['variation_epsilon'];pair=[]
            for sign in [-1,1]:
                sol=solve_ivp(lambda n,z:func(n,z,a),(0,cfg['N_end']),eq+sign*eps*direction,
                              method='DOP853',rtol=cfg['rtol'],atol=cfg['atol'],max_step=cfg['max_step'],dense_output=True)
                check('limiting variation solver '+str((a,kind,sign)),sol.success,message=sol.message);pair.append(sol.sol(sites).T)
            derivative=(pair[1]-pair[0])/(2*eps)
            close('limiting central variation '+str((a,kind)),derivative,linear,cfg['variation_atol'],cfg['variation_rtol'])
            perturb=cfg['nonlinear_displacement']*direction
            limiting=solve_ivp(lambda n,z:func(n,z,a),(0,cfg['N_end']),eq+perturb,
                              method='DOP853',rtol=cfg['rtol'],atol=cfg['atol'],max_step=cfg['max_step'],dense_output=True)
            check('limiting nonlinear solver '+str((a,kind)),limiting.success,message=limiting.message)
            target=limiting.sol(sites).T
            fullruns=[]
            for nu in FIX['nu']:
                raw=solve_ivp(lambda n,z:full(n,z,a,nu),(0,cfg['N_end']),np.r_[eq+perturb,np.log(cfg['initial_large_field'])],
                              method='RK45',rtol=cfg['rtol'],atol=cfg['atol'],max_step=cfg['max_step'],dense_output=True)
                check('full finite-era solver '+str((a,kind,nu)),raw.success,message=raw.message)
                values=raw.sol(sites).T
                close('full versus limiting history '+str((a,kind,nu)),values[:,:-1],target,cfg['history_atol'],cfg['history_rtol'])
                fullruns.append({'nu':nu,'states':values.tolist(),'evaluations':raw.nfev})
            rows.append({'a':a,'kind':kind,'equilibrium':eq.tolist(),'direction':direction.tolist(),'N':sites.tolist(),
                         'central_variation':derivative.tolist(),'linear':linear.tolist(),'limiting_nonlinear':target.tolist(),
                         'distance_initial':float(np.linalg.norm(target[0]-eq)),
                         'distance_final':float(np.linalg.norm(target[-1]-eq)),'full_runs':fullruns})
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-json',required=True);args=ap.parse_args();out=Path(args.output_json)
    if out.exists():raise FileExistsError(out)
    result={'started_at':datetime.now(timezone.utc).isoformat(),'role':'Limiting-system mathematics and controlled full-equation comparisons, no new observations or independent empirical test.'}
    result['symbolic']=symbolic_controls();result['eigenvalues']=eigenvalue_controls()
    result['asymptotic']=asymptotic_controls();result['histories']=history_controls()
    result['checks']=CHECKS;result['passed']=sum(x['passed']for x in CHECKS);result['failed']=sum(not x['passed']for x in CHECKS)
    result['ended_at']=datetime.now(timezone.utc).isoformat()
    files=[Path(__file__),HERE/'HAND_DERIVATION_v1.md',HERE/'HAND_DERIVATION_v2.md',HERE/'LIMIT_DOMAIN_CORRECTION_v2.json',HERE/'NUMERICAL_FIXTURES_v1.json',PARENT/'check_analytic_fluid_v1.py',PARENT/'NUMERICAL_FIXTURES_v1.json']
    result['source_sha256']={str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in files}
    with out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in CHECKS if not x['passed']]},indent=2))
    return int(result['failed']>0)


if __name__=='__main__':sys.exit(main())
