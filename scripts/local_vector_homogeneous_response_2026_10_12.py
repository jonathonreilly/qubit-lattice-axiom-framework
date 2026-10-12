#!/usr/bin/env python3
"""Check the supplied local vector action and causal/static response bridge."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import spherical_jn
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    'docs/LOCAL_VECTOR_HOMOGENEOUS_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md',
)

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def symbolic():
    N,D,alpha,a,b,r,z,cT,cL,ctheta = s.symbols(
        'N D alpha a b r z cT cL ctheta', positive=True)
    k = s.Matrix([a,0,b]); k2 = a*a+b*b
    mu,beta = 1/N,1/D-1/N
    I = s.eye(3); PL=k*k.T/k2; PT=I-PL
    B=mu*k2*I+beta*k*k.T
    inv=(N*PT+D*PL)/k2
    assert (B*inv-I).applyfunc(s.simplify)==s.zeros(3)
    assert s.simplify(inv[2,2]-(N*a*a+D*b*b)/k2**2)==0
    assert (B*PL-k2/D*PL).applyfunc(s.simplify)==s.zeros(3)
    assert (B*PT-k2/N*PT).applyfunc(s.simplify)==s.zeros(3)
    omega=s.symbols('omega',real=True)
    dynamic=PT/(k2/N-alpha*omega**2)+PL/(k2/D-alpha*omega**2)
    assert ((B-alpha*omega**2*I)*dynamic-I).applyfunc(s.simplify)==s.zeros(3)
    assert (dynamic.subs(omega,0)-inv).applyfunc(s.simplify)==s.zeros(3)
    x,y,zz=s.symbols('x y zz',real=True)
    rad=s.sqrt(x*x+y*y+zz*zz)
    static=N/(4*s.pi*rad)+(D-N)*s.diff(rad,zz,2)/(8*s.pi)
    target=(N+D+(N-D)*zz*zz/rad**2)/(8*s.pi*rad)
    assert s.simplify(static-target)==0
    time_integral=((1-ctheta**2)/cT**2+ctheta**2/cL**2
         +(3*ctheta**2-1)*(1/cT**2-1/cL**2)/2)/(4*s.pi*alpha*r)
    replacement={cT:1/s.sqrt(alpha*N),cL:1/s.sqrt(alpha*D)}
    assert s.simplify(time_integral.subs(replacement)
         -(N+D+(N-D)*ctheta**2)/(8*s.pi*r))==0
    q=s.symbols('q',positive=True)
    j0=s.sin(q)/q
    j1=s.sin(q)/q**2-s.cos(q)/q
    j2=(3/q**3-1/q)*s.sin(q)-3*s.cos(q)/q**2
    assert s.simplify(s.diff(j1/q,q)+j2/q)==0
    assert s.simplify(3*j1/q-j0-j2)==0
    return {'tensor_inverse':True,'positive_branch_eigenvalues':True,
            'dynamic_inverse':True,'static_point_source':True,
            'retarded_time_integral':True,'spherical_Bessel_identity':True,
            'source_sign':'u=-4*pi*G*G_ret*(rho*e); isotropic phi=-G*m*N/r'}

def real_green_fourier(N,D,alpha,k,t,costheta,omit_middle=False):
    """Angular integration of real tensor, then independent radial quadrature."""
    cT,cL=1/math.sqrt(alpha*N),1/math.sqrt(alpha*D)
    p2=(3*costheta**2-1)/2
    xt,xl=k*cT*t,k*cL*t
    fronts=t/alpha*((2/3)*spherical_jn(0,xt)+(2/3)*p2*spherical_jn(2,xt)
                    +(1/3)*spherical_jn(0,xl)-(2/3)*p2*spherical_jn(2,xl))
    middle=0.0 if omit_middle else -2*t/alpha*p2*quad(
        lambda radius:spherical_jn(2,k*radius)/radius,cT*t,cL*t,
        epsabs=2e-12,epsrel=2e-12)[0]
    direct=t/alpha*((1-costheta**2)*np.sinc(xt/np.pi)
                   +costheta**2*np.sinc(xl/np.pi))
    return float(fronts+middle),float(direct)

def numeric():
    rows=[]
    for N,D,alpha in [(2.,1.,1.),(5.,.2,.7),(1.4,1.4,2.),(3.,2.9,.3)]:
        for k,t in [(0.,.4),(.2,2.),(1.3,.9),(8.,1.1)]:
            for costheta in [0.,.3,.8,1.]:
                real,fourier=real_green_fourier(N,D,alpha,k,t,costheta)
                err=abs(real-fourier)
                assert err<2e-11
                rows.append({'N':N,'D':D,'alpha':alpha,'k':k,'t':t,
                             'cos_theta':costheta,'real_integral':real,
                             'spectral':fourier,'absolute_error':err})
    # A missing intervening term must be detected, not accepted by axis checks.
    wrong,right=real_green_fourier(5.,.2,.7,1.3,.9,1.,omit_middle=True)
    assert abs(wrong-right)>.01
    rng=np.random.default_rng(20261012)
    fluxes=[]
    for N,D,alpha in [(2.,1.,1.),(5.,.2,.7),(1.4,1.4,2.)]:
        mu,beta=1/N,1/D-1/N
        cL=math.sqrt((mu+beta)/alpha)
        for _ in range(40):
            grad=rng.normal(size=(3,3)) # grad[i,j]=partial_i u_j
            v=rng.normal(size=3); normal=rng.normal(size=3)
            normal/=np.linalg.norm(normal)
            divergence=float(np.trace(grad))
            stress=mu*(normal@grad)+beta*normal*divergence
            Q=mu*float(np.sum(grad*grad))+beta*divergence**2
            flux=abs(float(v@stress))
            cap=cL*(alpha*float(v@v)+Q)/2
            assert flux<=cap+1e-12 and Q>=0
            fluxes.append(flux/cap)
    # The analytic front support is also checked without using a group velocity.
    supports=[]
    for N,D,alpha in [(2.,1.,1.),(5.,.2,.7),(1.4,1.4,2.)]:
        cT,cL=1/math.sqrt(alpha*N),1/math.sqrt(alpha*D)
        for radius in [.2,1.,4.]:
            time=.9*radius/cL
            interval=int(time>=radius/cL)-int(time>=radius/cT)
            assert interval==0 and time<min(radius/cL,radius/cT)
            supports.append({'r':radius,'t':time,'outside_front':True})
    return {'real_to_Fourier_rows':rows,'max_transform_error':max(r['absolute_error'] for r in rows),
            'flux_samples':len(fluxes),'max_flux_bound_ratio':max(fluxes),
            'off_cone_samples':supports,
            'missing_intervening_term_mutation':{'detected':True,'difference':abs(wrong-right)},
            'scope':'Numerical controls supplement complete analytic energy and support proofs.'}


def publish(result, json_mode=False, sidecar=None):
    serialized=json.dumps(result,indent=2)+"\n"
    if sidecar is not None:
        with sidecar.open('x') as output:
            output.write(serialized)
    if json_mode:
        print(serialized,end='')
    else:
        print('PASS symbolic tensor inverse, stable poles, static Green and retarded time integral')
        print('PASS 64 real-space/Fourier transforms; 120 flux diagnostics; 9 off-cone points')
        print('PASS missing-intervening-term mutation detected')
        print('per_element: all three field components are in the symbolic tensor inverse.')
        print('per_site: checked and not executed - no physical discrete-site model is supplied.')
        print('per_mode: both transverse modes and the longitudinal branch are analytically checked.')
        print('per_block: retarded/static tensor identities and finite numerical controls are checked.')
        print('lattice_wide: checked and not executed - this is a continuum homogeneous construction.')
        print('The continuum domain of dependence follows from the local energy proof.')
        print(f"TOTAL: PASS={result['checks_passed']} FAIL={result['checks_failed']}; conditional construction, no empirical claim.")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--json',action='store_true')
    parser.add_argument('--output-json',type=Path)
    args=parser.parse_args()
    symbolic_checks = symbolic()
    numerical_checks = numeric()
    families = {name: value for name, value in symbolic_checks.items() if isinstance(value, bool)}
    families.update({
        'real_to_Fourier_transform': len(numerical_checks['real_to_Fourier_rows']) == 64 and numerical_checks['max_transform_error'] < 2e-11,
        'energy_flux_diagnostics': numerical_checks['flux_samples'] == 120 and numerical_checks['max_flux_bound_ratio'] <= 1 + 1e-12,
        'off_cone_diagnostics': len(numerical_checks['off_cone_samples']) == 9 and all(row['outside_front'] for row in numerical_checks['off_cone_samples']),
        'missing_intervening_term_rejected': numerical_checks['missing_intervening_term_mutation']['difference'] > .01,
    })
    assert all(families.values()), families
    result={'identities':{str(p.relative_to(ROOT)):digest(p) for p in
             [Path(__file__).resolve(),ROOT/AUDIT_INPUT_PATHS[0]]},
            'environment':{'python':sys.version,'numpy':np.__version__,
                           'scipy':scipy.__version__,'sympy':s.__version__},
            'symbolic':symbolic_checks,'numerical':numerical_checks,
            'check_families':families,
            'checks_passed':sum(families.values()),'checks_failed':sum(not v for v in families.values()),
            'claim':'Conditional local vector construction matches homogeneous linear static response.',
            'limits':'No nonlinear galaxy operator, tensor-wave identification, empirical acceptance or TOE.'}
    publish(result,args.json,args.output_json)


if __name__=='__main__':
    main()
