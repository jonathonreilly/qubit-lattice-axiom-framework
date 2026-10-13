#!/usr/bin/env python3
"""Direct author's analytic fluid construction and conditional controls.

No parameter fitting or independent observational validation is performed.
The proper-time momentum oracle and N-coordinate acceleration are separate
implementations of the supplied action. Failures are written, never erased.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import sys
import math
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import expm
import sympy as sp

HERE = Path(__file__).resolve().parent
FIX = json.loads((HERE/'NUMERICAL_FIXTURES_v1.json').read_text())
CHECKS = []


def check(name, passed, **evidence):
    CHECKS.append({'name':name, 'passed':bool(passed), **evidence})


def close(name, actual, expected, atol=2e-10, rtol=2e-10):
    a, b = np.asarray(actual, dtype=float), np.asarray(expected, dtype=float)
    error = np.abs(a-b)
    tolerance = atol+rtol*np.maximum(np.abs(a), np.abs(b))
    units = float(np.max(error/tolerance))
    check(name, np.all(np.isfinite(a)) and units<=1,
          max_tolerance_units=units,
          actual=a.tolist(), expected=b.tolist())


def exact(name, expression):
    reduced = sp.factor(sp.cancel(expression))
    check(name, reduced==0, reduced_expression=str(reduced))


def functions(phi, a, nu, hv):
    u, x, y = phi
    d = 1+(2/3)*(1+a)*(x*x+y*y)
    k = np.array([1.,4*a/(9*d),a/(3*d)])
    f = a/2-np.sqrt(a)*u+2*u*u
    v = hv*hv*(1.5+f*x*x+(a/3)*y*y+nu*u*u/2)
    dv = hv*hv*np.array([(-np.sqrt(a)+4*u)*x*x+nu*u,
                        2*f*x,(2*a/3)*y])
    dx, dy = (4/3)*(1+a)*np.array([x,y])/d
    gamma = np.zeros((3,3,3), dtype=np.result_type(phi,float))
    gamma[1,1,1] = -dx/2
    gamma[1,1,2] = gamma[1,2,1] = -dy/2
    gamma[1,2,2] = 3*dx/8
    gamma[2,2,2] = -dy/2
    gamma[2,1,2] = gamma[2,2,1] = -dx/2
    gamma[2,1,1] = 2*dy/3
    return k, v, dv, gamma


def n_rhs(n, state, a, nu, hv):
    phi, p = state[:3], state[3:6]
    sm, sr = state[6:8]
    k, v, dv, gamma = functions(phi,a,nu,hv)
    norm = np.sum(k*p*p)
    denominator = 3-norm
    if denominator <= 0 or sm+sr+v<=0:
        raise ValueError(('Friedmann chart boundary',n,denominator,sm+sr+v))
    h2 = 2*(sm+sr+v)/denominator
    hlog = -(sm+4*sr/3)/h2-norm
    force = dv+np.array([np.sqrt(a)*sm,0.,0.])
    accel = -(3+hlog)*p-0.0*np.einsum('ijk,j,k->i',gamma,p,p)-force/(k*h2)
    return np.r_[p,accel,(-3+np.sqrt(a)*p[0])*sm,-4*sr]


def momentum_quantities(phi, pi, sm, sr, a, nu, hv):
    # Independent Euler-Lagrange momentum form. No connection function.
    u,x,y = phi
    c = 2*(1+a)/3
    d = 1+c*(x*x+y*y)
    constants = np.array([1.,4*a/9,a/3])
    k = constants/np.array([1.,d,d])
    velocity = pi/k
    f = 2*(u-np.sqrt(a)/4)**2+3*a/8
    v = hv**2*(1.5+f*x*x+a*y*y/3+nu*u*u/2)
    gradv = hv**2*np.array([(4*u-np.sqrt(a))*x*x+nu*u,2*f*x,2*a*y/3])
    dk = np.zeros((3,3))
    for j,z in [(1,x),(2,y)]:
        dk[j,1:] = -2*c*z*constants[1:]/(d*d)
    norm = np.dot(pi,velocity)
    h = np.sqrt((2*(sm+sr+v)+norm)/3)
    pidot = -3*h*pi+(dk@(velocity*velocity))/2-gradv
    pidot[0] -= np.sqrt(a)*sm
    density_dot = np.array([(-3*h+np.sqrt(a)*velocity[0])*sm,-4*h*sr])
    metric_dot = velocity@dk
    acceleration = (pidot-metric_dot*velocity)/k
    hdot = -(sm+4*sr/3)-norm
    return {'K':k,'V':v,'gradV':gradv,'dK':dk,'velocity':velocity,
            'H':h,'Hdot':hdot,'T':norm,'pi_dot':pidot,
            'acceleration':acceleration,'density_dot':density_dot}


def symbolic_controls():
    a,nu,hv = sp.symbols('a nu H_v',positive=True)
    u,x,y = sp.symbols('u x y',real=True)
    q = sp.Matrix([u,x,y])
    d = 1+sp.Rational(2,3)*(1+a)*(x*x+y*y)
    k = sp.diag(1,4*a/(9*d),a/(3*d))
    inv = k.inv()
    v = hv**2*(sp.Rational(3,2)+(a/2-sp.sqrt(a)*u+2*u*u)*x*x+a*y*y/3+nu*u*u/2)
    gamma = [[[sum(inv[i,l]*(sp.diff(k[l,j],q[m])+sp.diff(k[l,m],q[j])-sp.diff(k[j,m],q[l]))/2 for l in range(3)) for m in range(3)] for j in range(3)] for i in range(3)]
    dx,dy = sp.diff(d,x)/d,sp.diff(d,y)/d
    explicit = {(1,1,1):-dx/2,(1,1,2):-dy/2,(1,2,1):-dy/2,(1,2,2):3*dx/8,
                (2,2,2):-dy/2,(2,1,2):-dx/2,(2,2,1):-dx/2,(2,1,1):2*dy/3}
    for i in range(3):
        for j in range(3):
            for m in range(3):
                exact('symbolic metric connection '+str((i,j,m)),gamma[i][j][m]-explicit.get((i,j,m),0))
    hb = hv*sp.sqrt(d)
    flow = sp.Matrix([0,-sp.Rational(3,2)*hb*x,-2*hb*y])
    sm,sr = hv**2*x*x,hv**2*y*y
    kinetic = (flow.T*k*flow)[0]
    v0 = v.subs(u,0)
    hdot = sum(sp.diff(hb,q[i])*flow[i] for i in range(3))
    exact('symbolic exact Friedmann',3*hb*hb-2*(sm+sr+v0)-kinetic)
    exact('symbolic exact Raychaudhuri',hdot+sm+sp.Rational(4,3)*sr+kinetic)
    for i in range(3):
        acceleration = sum(sp.diff(flow[i],q[j])*flow[j] for j in range(3))
        connection = sum(gamma[i][j][m]*flow[j]*flow[m] for j in range(3) for m in range(3))
        force = (sp.diff(v,q[i]).subs(u,0)+(sp.sqrt(a)*sm if i==0 else 0))/k[i,i]
        exact('symbolic full scalar equation '+str(i),acceleration+connection+3*hb*flow[i]+force)
    for i in [1,2]:
        exact('symbolic gradient velocity '+str(i),(k*flow)[i]+a*sp.diff(hb,q[i])/(1+a))
    lower = hv**2*(sp.Rational(3,2)+3*a*x*x/8+a*y*y/3+nu*u*u/2)
    exact('symbolic coercive square',v-lower-2*hv**2*(u-sp.sqrt(a)/4)**2*x*x)
    hessian = sp.hessian(v,q).subs({u:0,x:0,y:0})
    mass = (inv*hessian).subs({u:0,x:0,y:0})
    for i,target in enumerate([nu,sp.Rational(9,4),2]):
        exact('symbolic canonical vacuum mass '+str(i),mass[i,i]-hv*hv*target)
    # Off-trajectory energy with generic velocities; Friedmann is not used.
    vel = sp.Matrix(sp.symbols('v_u v_x v_y',real=True))
    dens,rad,hh = sp.symbols('sigma r H',positive=True)
    dk = [k.diff(qq) for qq in q]
    t = (vel.T*k*vel)[0]
    force = sp.Matrix([sp.diff(v,qq) for qq in q])+sp.Matrix([sp.sqrt(a)*dens,0,0])
    acc = -3*hh*vel-inv*force-sp.Matrix([sum(gamma[i][j][m]*vel[j]*vel[m] for j in range(3) for m in range(3)) for i in range(3)])
    tdot = 2*(vel.T*k*acc)[0]+sum((vel.T*dk[i]*vel)[0]*vel[i] for i in range(3))
    edot = tdot/2+sum(sp.diff(v,q[i])*vel[i]for i in range(3))+(-3*hh+sp.sqrt(a)*vel[0])*dens-4*hh*rad
    exact('symbolic full off trajectory energy exchange',edot+3*hh*(t+dens+sp.Rational(4,3)*rad))
    return {'vacuum_mass_squared_over_Hv_squared':[str(nu),'9/4','2'],
            'energy_derivative':'-3 H (K_AB v^A v^B+sigma+4r/3)',
            'role':'exact algebra within the supplied action; not observations'}


def off_trajectory_controls():
    rows=[]
    for a in FIX['a']:
        for nu in FIX['nu']:
            for case in FIX['off_trajectory_cases']:
                phi=np.array(case['phi'],dtype=float)
                phi[0]*=np.sqrt(a)
                velocity=np.array(case['velocity'],dtype=float)
                velocity[0]*=np.sqrt(a)
                sm,sr=case['densities']
                k,v,dv,gamma=functions(phi,a,nu,1.)
                pi=k*velocity
                z=momentum_quantities(phi,pi,sm,sr,a,nu,1.)
                nstate=np.r_[phi,velocity/z['H'],sm,sr]
                got=n_rhs(0.,nstate,a,nu,1.)
                expected=(z['acceleration']-velocity*z['Hdot']/z['H'])/z['H']**2
                tag=str(len(rows))
                close('off trajectory full KG '+tag,got[3:6],expected)
                close('off trajectory full conservation '+tag,got[6:],z['density_dot']/z['H'])
                close('off trajectory independent K '+tag,k,z['K'])
                close('off trajectory independent V '+tag,v,z['V'])
                close('off trajectory independent gradient '+tag,dv,z['gradV'])
                # Complex-step derivatives check actual implementation, not
                # another explicit copy of its supplied gradient/connection.
                grad=np.empty(3);dk=np.empty((3,3))
                for j in range(3):
                    shifted=phi.astype(complex);shifted[j]+=1e-25j
                    kk,vv,_,_=functions(shifted,a,nu,1.)
                    grad[j]=vv.imag/1e-25;dk[j]=kk.imag/1e-25
                close('off trajectory potential derivative '+tag,dv,grad)
                close('off trajectory metric derivative '+tag,dk,z['dK'])
                edot=np.dot(k*velocity,z['acceleration'])+np.dot(velocity@dk,velocity*velocity)/2+np.dot(dv,velocity)+sum(z['density_dot'])
                close('off trajectory energy balance '+tag,edot,-3*z['H']*(z['T']+sm+4*sr/3))
                lower=1.5+3*a*phi[1]**2/8+a*phi[2]**2/3+nu*phi[0]**2/2
                check('off trajectory coercivity '+tag,v>=lower-1e-13*max(1,v),value=float(v),lower=float(lower))
                check('off trajectory positive metric '+tag,np.min(k)>0,diagonal=k.tolist())
                denominator=3-np.dot(k,nstate[3:6]**2)
                close('off trajectory Friedmann chart '+tag,2*(sm+sr+v)/denominator,z['H']**2)
                rows.append({'a':a,'nu':nu,'case':case,'N_state':nstate.tolist(),
                             'H':float(z['H']),'H_J':float(np.exp(-np.sqrt(a)*phi[0])*(z['H']+np.sqrt(a)*velocity[0])),
                             'implemented_accelerations':got[3:6].tolist(),
                             'momentum_oracle_accelerations':expected.tolist()})
    return rows


def tracking_rhs(n,state,a,nu,hv,x0,y0,s0,r0):
    # Exact invertible time-dependent coordinates, not a trajectory constraint.
    ex=x0*np.exp(-1.5*n);ey=y0*np.exp(-2*n)
    u,xx,yy,pu,px,py,lm,lr=state
    actual=np.array([u,xx*ex,yy*ey,pu,px*ex,py*ey,s0*np.exp(lm),r0*np.exp(lr)])
    z=n_rhs(n,actual,a,nu,hv)
    return np.array([z[0],z[1]/ex+1.5*xx,z[2]/ey+2*yy,
                     z[3],z[4]/ex+1.5*px,z[5]/ey+2*py,
                     z[6]/actual[6],z[7]/actual[7]])


def tracking_histories():
    omega=FIX['calibration']['Omega_gamma'];m=FIX['calibration']['m']
    hv=np.sqrt(1-m-omega)
    cfg=FIX['tracking'];n0=-np.log1p(cfg['z_start']);n1=cfg['N_end']
    sites=np.array(sorted(set([n0]+[-np.log1p(z)for z in cfg['redshifts']]+cfg['future_N'])))
    rows=[]
    for a in FIX['a']:
        x0=np.sqrt(3*m/(2*(1+a)*hv*hv));y0=np.sqrt(3*omega/(2*(1+a)*hv*hv))
        s0=hv*hv*x0*x0;r0=hv*hv*y0*y0
        for nu in FIX['nu']:
            runs=[]
            for level in cfg['refinements']:
                initial=np.array([0.,1.,1.,0.,-1.5,-2.,-3*n0,-4*n0])
                sol=solve_ivp(lambda n,y:tracking_rhs(n,y,a,nu,hv,x0,y0,s0,r0),(n0,n1),initial,
                              method='DOP853',rtol=level['rtol'],atol=level['atol'],max_step=level['max_step'],dense_output=True)
                check('tracking solver success '+str((a,nu,level)),sol.success,message=sol.message)
                got=sol.sol(sites).T
                target=np.array([[0,1,1,0,-1.5,-2,-3*n,-4*n]for n in sites])
                close('tracking full trajectory '+str((a,nu,level)),got,target,cfg['comparison_atol'],cfg['comparison_rtol'])
                hrows=[]
                for n,y in zip(sites,got):
                    ex=x0*np.exp(-1.5*n);ey=y0*np.exp(-2*n)
                    phi=np.array([y[0],ex*y[1],ey*y[2]])
                    pp=np.array([y[3],ex*y[4],ey*y[5]])
                    k,v,_,_=functions(phi,a,nu,hv)
                    hh=2*(s0*np.exp(y[6])+r0*np.exp(y[7])+v)/(3-np.dot(k,pp*pp))
                    intended=m*np.exp(-3*n)+omega*np.exp(-4*n)+hv*hv
                    close('tracking actual H2 '+str((a,nu,n,level)),hh/intended,1.,cfg['comparison_atol'],cfg['comparison_rtol'])
                    hrows.append(float(hh))
                runs.append({'refinement':level,'evaluations':sol.nfev,'states':got.tolist(),'H2':hrows})
            close('tracking refinement '+str((a,nu)),runs[0]['states'],runs[1]['states'],cfg['comparison_atol'],cfg['comparison_rtol'])
            rows.append({'a':a,'nu':nu,'Hv':float(hv),'x0':float(x0),'y0':float(y0),'S0':float(s0),'R0':float(r0),'N_sites':sites.tolist(),'runs':runs})
    return rows


def scaled_n_rhs(n,z,a,nu):
    weights=np.array([1.,2*np.sqrt(a)/3,np.sqrt(a/3)])
    unscaled=np.r_[z[:3]/weights,z[3:6]/weights,z[6:8]]
    result=n_rhs(n,unscaled,a,nu,1.)
    return np.r_[result[:3]*weights,result[3:6]*weights,result[6:8]]


def scaled_momentum_rhs(t,z,a,nu):
    weights=np.array([1.,2*np.sqrt(a)/3,np.sqrt(a/3)])
    phi=z[:3]/weights;pi=z[3:6]*weights
    sm,sr=z[6:8]
    r=momentum_quantities(phi,pi,sm,sr,a,nu,1.)
    return np.r_[weights*r['velocity'],r['pi_dot']/weights,r['density_dot'],r['H']]


def disturbed_histories():
    cfg=FIX['disturbed'];rows=[]
    for a in FIX['a']:
        weights=np.array([1.,2*np.sqrt(a)/3,np.sqrt(a/3)])
        for nu in FIX['nu']:
            for case in cfg['cases']:
                phi=np.array(case['phi'],dtype=float);phi[0]*=np.sqrt(a)
                vel=np.array(case['velocity'],dtype=float);vel[0]*=np.sqrt(a)
                sm,sr=case['densities'];k,v,_,_=functions(phi,a,nu,1.)
                pi=k*vel;initial=momentum_quantities(phi,pi,sm,sr,a,nu,1.)
                nn=np.r_[weights*phi,weights*vel/initial['H'],sm,sr]
                zz=np.r_[weights*phi,pi/weights,sm,sr,0.]
                nmax=cfg['N_end'];sites=np.linspace(0,nmax,cfg['sites'])
                ns=solve_ivp(lambda n,z:scaled_n_rhs(n,z,a,nu),(0,nmax),nn,method='DOP853',
                             rtol=cfg['rtol'],atol=cfg['atol'],max_step=cfg['max_step'],dense_output=True)
                def event(t,z):return z[8]-nmax
                event.terminal=True;event.direction=1
                ts=solve_ivp(lambda t,z:scaled_momentum_rhs(t,z,a,nu),(0,nmax+1),zz,method='RK45',
                             rtol=cfg['rtol'],atol=cfg['atol'],max_step=cfg['max_step'],events=event,dense_output=True)
                check('disturbed N solver '+str(len(rows)),ns.success,message=ns.message)
                check('disturbed proper solver '+str(len(rows)),ts.success and len(ts.t_events[0])==1,message=ts.message)
                from scipy.optimize import brentq
                times=[0.]+[brentq(lambda t:ts.sol(t)[8]-n,0,ts.t[-1],xtol=2e-13)for n in sites[1:-1]]+[ts.t[-1]]
                reference=[];energies=[];fields=[];minrho=math.inf
                for t in times:
                    raw=ts.sol(t);ph=raw[:3]/weights;pip=raw[3:6]*weights
                    r=momentum_quantities(ph,pip,raw[6],raw[7],a,nu,1.)
                    reference.append(np.r_[raw[:3],weights*r['velocity']/r['H'],raw[6:8]])
                    energies.append(1.5*r['H']**2);fields.append(ph.tolist())
                    minrho=min(minrho,float(min(raw[6:8])))
                values=ns.sol(sites).T
                close('disturbed different formulations '+str(len(rows)),values,reference,cfg['comparison_atol'],cfg['comparison_rtol'])
                e=np.array(energies)
                check('disturbed energy monotone '+str(len(rows)),np.max(np.diff(e))<=cfg['energy_tolerance']*max(1,e[0]),max_increment=float(np.max(np.diff(e))))
                check('disturbed energy floor '+str(len(rows)),min(e)>=1.5-cfg['energy_tolerance'],minimum=float(min(e)))
                check('disturbed nonnegative density within precision '+str(len(rows)),minrho>=-cfg['density_tolerance'],minimum=minrho)
                rows.append({'a':a,'nu':nu,'case':case,'N':sites.tolist(),'proper_times':times,
                             'N_states':values.tolist(),'proper_reference_states':np.asarray(reference).tolist(),
                             'energies':energies,'fields':fields,'N_evaluations':ns.nfev,'proper_evaluations':ts.nfev,
                             'scope':'finite interval solver comparison; global future convergence is a separate proof'})
    return rows


def mode_controls():
    rows=[]
    for mass in FIX['nu']+[2.]:
        for t in FIX['mode_times']:
            q0,p0=.2,-.1
            if mass<2.25:
                z=np.sqrt(2.25-mass)
                core=q0*np.cosh(z*t)+(p0+1.5*q0)*np.sinh(z*t)/z
            elif mass==2.25:
                core=q0+(p0+1.5*q0)*t
            else:
                z=np.sqrt(mass-2.25)
                core=q0*np.cos(z*t)+(p0+1.5*q0)*np.sin(z*t)/z
            expected=np.exp(-1.5*t)*core
            actual=(expm(np.array([[0.,1.],[-mass,-3.]])*t)@np.array([q0,p0]))[0]
            close('vacuum closed mode '+str((mass,t)),actual,expected,1e-13,1e-12)
            rows.append({'mass_squared_over_Hv_squared':mass,'Hv_t':t,'mode':float(expected),'matrix_exponential':float(actual)})
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-json',required=True);args=ap.parse_args()
    dest=Path(args.output_json)
    if dest.exists():raise FileExistsError(dest)
    result={'started_at':datetime.now(timezone.utc).isoformat(),
            'scope':'Conditional analytic construction; exposed photon calibration and supplied matter/vacuum inputs. No fit, independent empirical acceptance, or full spacetime stability.'}
    result['symbolic']=symbolic_controls()
    result['off_trajectory']=off_trajectory_controls()
    result['modes']=mode_controls()
    result['tracking']=tracking_histories()
    result['disturbed']=disturbed_histories()
    result['checks']=CHECKS
    result['passed']=sum(x['passed']for x in CHECKS);result['failed']=sum(not x['passed']for x in CHECKS)
    result['ended_at']=datetime.now(timezone.utc).isoformat()
    result['versions']={'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__}
    files=['check_analytic_fluid_v1.py','NUMERICAL_FIXTURES_v1.json','HAND_DERIVATION_v1.md','HAND_DERIVATION_v2.md','MODE_AND_FRAME_CORRECTION_v2.json','PROTOCOL_v1.json','CALIBRATION_SCOPE_v1.json']
    result['source_sha256']={f:hashlib.sha256((HERE/f).read_bytes()).hexdigest()for f in files}
    with dest.open('x')as out:json.dump(result,out,indent=2,allow_nan=False);out.write('\n')
    print(json.dumps({'passed':result['passed'],'failed':result['failed'],'failures':[x for x in CHECKS if not x['passed']]},indent=2))
    return int(result['failed']>0)


if __name__=='__main__':
    sys.exit(main())
