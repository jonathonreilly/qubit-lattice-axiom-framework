#!/usr/bin/env python3
"""Independent Hamiltonian evolution with analytically conserved fluid numbers.

Six dynamical field variables replace the parent's eight N-coordinate
acceleration/density variables.  This source imports no parent helper.  Radau
is distinct from the parent's DOP853 and RK45 integrators.  Reference factors
in the tracking chart are invertible scales, never projections onto a target.
"""
from pathlib import Path
import datetime
import hashlib
import json
import math
import numpy as np
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parent
FIX=json.loads((ROOT/'source_snapshot/NUMERICAL_FIXTURES_v1.json').read_text())
AUTHOR=json.loads((ROOT/'source_snapshot/evidence_v1/RESULTS.json').read_text())
CHECKS=[]


def check(name, passed, **evidence):
    CHECKS.append({'name':name,'passed':bool(passed),**evidence})


def compare(name, actual, expected, atol, rtol):
    aa,bb=np.asarray(actual,float),np.asarray(expected,float)
    ratios=np.abs(aa-bb)/(atol+rtol*np.maximum(np.abs(aa),np.abs(bb)))
    check(name,aa.shape==bb.shape and np.all(np.isfinite(ratios)) and np.max(ratios)<=1,
          max_tolerance_units=float(np.max(ratios)),max_absolute_error=float(np.max(np.abs(aa-bb))))


def tracking_evaluator(n,z,a,nu,hv,x0,y0):
    s=math.sqrt(a);c=2*(1+a)/3;ax=4*a/9;ay=a/3
    ex=x0*math.exp(-1.5*n);ey=y0*math.exp(-2*n)
    dr=1+c*(ex*ex+ey*ey);hr=hv*math.sqrt(dr)
    scaleq=np.array([1.,ex,ey]);scalepi=np.array([hr,ax*hr*ex/dr,ay*hr*ey/dr])
    q=z[:3]*scaleq;pi=z[3:6]*scalepi
    u,x,y=q
    d=1+c*(x*x+y*y)
    f=2*(u-s/4)**2+3*a/8
    kinxy=pi[1]**2/ax+pi[2]**2/ay
    kinetic=pi[0]**2+d*kinxy
    potential=hv*hv*(1.5+f*x*x+a*y*y/3+nu*u*u/2)
    sigref=hv*hv*ex*ex
    sm=sigref*math.exp(s*u);sr=hv*hv*ey*ey
    hh=math.sqrt((kinetic+2*(potential+sm+sr))/3)
    velocity=np.array([pi[0],d*pi[1]/ax,d*pi[2]/ay])
    # The combined u force uses an equivalent stable difference near u=0,
    # x/ex=1. It remains a general function of all six evolved variables.
    grad_u=hv*hv*u*(4*x*x+nu)+s*sigref*(math.expm1(s*u)-(z[1]-1)*(z[1]+1))
    gradient=np.array([grad_u,c*x*kinxy+2*hv*hv*f*x,c*y*kinxy+2*hv*hv*a*y/3])
    qprime=velocity/hh
    piprime=-3*pi-gradient/hh
    logdr=-c*(3*ex*ex+4*ey*ey)/dr
    logq=np.array([0.,-1.5,-2.])
    logpi=np.array([logdr/2,-logdr/2-1.5,-logdr/2-2.])
    derivative=np.r_[qprime/scaleq-logq*z[:3],piprime/scalepi-logpi*z[3:6]]
    recorded=np.r_[z[:3],qprime/scaleq,-3*n+s*u,-4*n]
    return derivative,recorded,hh*hh


def disturbed_evaluator(n,z,a,nu,sm0,sr0,u0):
    u,X,Y=z[:3];Pu,Px,Py=z[3:6]
    s=math.sqrt(a);wx=2*s/3;wy=s/math.sqrt(3)
    bx=3*(1+a)/(2*a);by=2*(1+a)/a
    d=1+bx*X*X+by*Y*Y
    f=2*(u-s/4)**2+3*a/8
    x=X/wx
    kinetic=Pu*Pu+d*(Px*Px+Py*Py)
    potential=1.5+f*x*x+Y*Y+nu*u*u/2
    sm=sm0*math.exp(-3*n+s*(u-u0));sr=sr0*math.exp(-4*n)
    energy=kinetic/2+potential+sm+sr
    hh=math.sqrt(2*energy/3)
    coord_velocity=np.array([Pu,d*Px,d*Py])
    gradient=np.array([(4*u-s)*x*x+nu*u+s*sm,
                       bx*X*(Px*Px+Py*Py)+2*f*X/(wx*wx),
                       by*Y*(Px*Px+Py*Py)+2*Y])
    qprime=coord_velocity/hh
    pprime=-3*z[3:6]-gradient/hh
    derivative=np.r_[qprime,pprime,1/hh]
    recorded=np.r_[z[:3],qprime,sm,sr]
    return derivative,recorded,energy


def main():
    tracking=[];disturbed=[]
    tc=FIX['tracking'];dc=FIX['disturbed']
    sites=np.array(sorted(set([-math.log1p(tc['z_start'])]+[-math.log1p(z)for z in tc['redshifts']]+tc['future_N'])))
    target=np.array([[0,1,1,0,-1.5,-2,-3*n,-4*n]for n in sites])
    tindex={(r['a'],r['nu']):r for r in AUTHOR['tracking']}
    check('tracking complete Cartesian coverage',len(tindex)==12 and set(tindex)=={(a,nu)for a in FIX['a']for nu in FIX['nu']})
    omega=FIX['calibration']['Omega_gamma'];m=FIX['calibration']['m'];hv=math.sqrt(1-m-omega)
    for a in FIX['a']:
        x0=math.sqrt(3*m/(2*(1+a)*hv*hv));y0=math.sqrt(3*omega/(2*(1+a)*hv*hv))
        for nu in FIX['nu']:
            original=tindex[a,nu]
            compare(f'tracking sites {a} {nu}',sites,original['N_sites'],atol=1e-14,rtol=1e-14)
            initial=np.array([0.,1.,1.,0.,-1.5,-2.])
            solution=solve_ivp(lambda n,z:tracking_evaluator(n,z,a,nu,hv,x0,y0)[0],
                               (sites[0],tc['N_end']),initial,method='Radau',rtol=3e-11,atol=3e-13,max_step=.04,dense_output=True)
            check(f'independent tracking solver {a} {nu}',solution.success,message=solution.message)
            row={'a':a,'nu':nu,'success':solution.success,'evaluations':solution.nfev,'N':sites.tolist()}
            if solution.success:
                vals=[];h2=[]
                for n,z in zip(sites,solution.sol(sites).T):
                    _,rec,hh=tracking_evaluator(n,z,a,nu,hv,x0,y0);vals.append(rec.tolist());h2.append(hh)
                row.update({'states':vals,'H2':h2,'canonical_scaled_states':solution.sol(sites).T.tolist()})
                compare(f'independent tracking target {a} {nu}',vals,target,tc['comparison_atol'],tc['comparison_rtol'])
                for j,run in enumerate(original['runs']):
                    compare(f'independent tracking author refinement {a} {nu} {j}',vals,run['states'],tc['comparison_atol'],tc['comparison_rtol'])
                    compare(f'independent tracking H2 {a} {nu} {j}',h2,run['H2'],atol=tc['comparison_atol'],rtol=tc['comparison_rtol'])
            tracking.append(row)
            print(json.dumps({'completed':'tracking','a':a,'nu':nu,'success':solution.success,'evaluations':solution.nfev}),flush=True)

    def casekey(case):return json.dumps(case,sort_keys=True)
    dindex={(r['a'],r['nu'],casekey(r['case'])):r for r in AUTHOR['disturbed']}
    expected={(a,nu,casekey(case))for a in FIX['a']for nu in FIX['nu']for case in dc['cases']}
    check('disturbed complete Cartesian coverage',len(dindex)==48 and set(dindex)==expected)
    nsites=np.linspace(0,dc['N_end'],dc['sites'])
    for a in FIX['a']:
        s=math.sqrt(a);weights=np.array([1,2*s/3,s/math.sqrt(3)])
        for nu in FIX['nu']:
            for case_index,case in enumerate(dc['cases']):
                original=dindex[a,nu,casekey(case)]
                compare(f'disturbed sites {a} {nu} {case_index}',nsites,original['N'],atol=1e-14,rtol=1e-14)
                q=np.asarray(case['phi'],float);q[0]*=s
                vel=np.asarray(case['velocity'],float);vel[0]*=s
                sm0,sr0=case['densities'];u0=q[0]
                d0=1+2*(1+a)*(q[1]*q[1]+q[2]*q[2])/3
                k0=weights**2/np.array([1,d0,d0]);pi0=k0*vel
                initial=np.r_[weights*q,pi0/weights,0.]
                solution=solve_ivp(lambda n,z:disturbed_evaluator(n,z,a,nu,sm0,sr0,u0)[0],
                                   (0,dc['N_end']),initial,method='Radau',rtol=3e-11,atol=3e-14,max_step=.04,dense_output=True)
                tag=f'{a} {nu} {case_index}'
                check('independent disturbed solver '+tag,solution.success,message=solution.message)
                row={'a':a,'nu':nu,'case_index':case_index,'N':nsites.tolist(),'success':solution.success,'evaluations':solution.nfev}
                if solution.success:
                    raw=solution.sol(nsites).T;values=[];energies=[]
                    for n,z in zip(nsites,raw):
                        _,recorded,e=disturbed_evaluator(n,z,a,nu,sm0,sr0,u0);values.append(recorded.tolist());energies.append(e)
                    for origin in ['N_states','proper_reference_states']:
                        compare('independent disturbed '+origin+' '+tag,values,original[origin],dc['comparison_atol'],dc['comparison_rtol'])
                    compare('independent disturbed proper times '+tag,raw[:,6],original['proper_times'],dc['comparison_atol'],dc['comparison_rtol'])
                    compare('independent disturbed energy '+tag,energies,original['energies'],dc['comparison_atol'],dc['comparison_rtol'])
                    check('independent disturbed energy floor '+tag,min(energies)>=1.5-dc['energy_tolerance'])
                    check('independent disturbed energy decreasing '+tag,max(np.diff(energies))<=dc['energy_tolerance']*max(1,energies[0]))
                    row.update({'states':values,'canonical_momenta':raw[:,3:6].tolist(),'proper_times':raw[:,6].tolist(),'energies':energies})
                disturbed.append(row)
                print(json.dumps({'completed':'disturbed','a':a,'nu':nu,'case_index':case_index,'success':solution.success,'evaluations':solution.nfev}),flush=True)

    out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'formulation':'Canonical Hamiltonian momenta in N, exact dust number and radiation constants; Radau; no parent imports.',
         'tracking':tracking,'disturbed':disturbed,'checks':CHECKS,
         'summary':{'total':len(CHECKS),'passed':sum(c['passed']for c in CHECKS),'failed':sum(not c['passed']for c in CHECKS)}}
    (ROOT/'HAMILTONIAN_HISTORIES_v1.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(out['summary'],sort_keys=True),flush=True)
    for c in CHECKS:
        if not c['passed']:print(json.dumps(c,sort_keys=True),flush=True)
    return int(out['summary']['failed']>0)


if __name__=='__main__':
    raise SystemExit(main())
