#!/usr/bin/env python3
"""Independent local-vector checks, with raw sphere quadrature and moments.

No author imports and no spherical-Bessel reduction. Reads frozen synthetic
receipts only, not fitted galaxy/solar arrays.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from numpy.polynomial.legendre import leggauss
import sympy as s
import mpmath as mp

HERE=Path(__file__).resolve().parent
RT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
mp.mp.dps=60
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def guard():
    assert time.time()<read(RT/'DEADLINE.json')['packaging_epoch']
    assert not any((RT/n).exists() for n in ('STOP_REQUESTED.json','USER_STOP_REQUESTED.json',
         'STOP_REQUESTED','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'))
def dump(name,data):
    p=HERE/name;assert not p.exists();p.write_text(json.dumps(data,indent=2)+'\n')

def symbolic_checks():
    N,D,alpha,G=s.symbols('N D alpha G',positive=True)
    rho=s.symbols('rho',real=True);mu,beta=1/N,1/D-1/N
    u=s.Matrix(s.symbols('u0:3',real=True));vel=s.Matrix(s.symbols('v0:3',real=True))
    e=s.Matrix(s.symbols('e0:3',real=True));grad=s.Matrix(3,3,s.symbols('h0:9',real=True))
    div=s.trace(grad);Q=mu*sum(x*x for x in grad)+beta*div**2
    lag=(alpha*vel.dot(vel)-Q)/(8*s.pi*G)-rho*e.dot(u)
    for j in range(3):
        assert s.simplify(s.diff(lag,vel[j])-alpha*vel[j]/(4*s.pi*G))==0
        assert s.diff(lag,u[j])==-rho*e[j]
        for i in range(3):
            expected=-(mu*grad[i,j]+beta*int(i==j)*div)/(4*s.pi*G)
            assert s.simplify(s.diff(lag,grad[i,j])-expected)==0
    ham=sum(s.diff(lag,vel[j])*vel[j] for j in range(3))-lag
    assert s.simplify(ham-((alpha*vel.dot(vel)+Q)/(8*s.pi*G)+rho*e.dot(u)))==0
    k=s.Matrix(s.symbols('kx ky kz',real=True));k2=k.dot(k);I=s.eye(3)
    B=mu*k2*I+beta*k*k.T
    inverse=N*I/k2+(D-N)*k*k.T/k2**2
    assert (B*inverse-I).applyfunc(s.simplify)==s.zeros(3)
    assert s.factor(B.det())==k2**3/(D*N**2)
    e_unit=s.Matrix([s.Rational(1,3),s.Rational(2,3),s.Rational(2,3)])
    assert s.simplify((e_unit.T*inverse*e_unit)[0]-(N*k2+(D-N)*e_unit.dot(k)**2)/k2**2)==0
    t,c=s.symbols('t c',positive=True)
    f=s.sin(c*s.sqrt(k2)*t)/(alpha*c*s.sqrt(k2))
    assert s.simplify(s.diff(f,t,2)+c*c*k2*f)==0
    assert s.simplify(f.subs(t,0))==0 and s.simplify(s.diff(f,t).subs(t,0))==1/alpha
    # Primitive h in the intervening region and its Hessian coefficients.
    r,cL,cT=s.symbols('r cL cT',positive=True)
    h=t/(4*s.pi)*(1/r-1/(cL*t))
    hp=s.diff(h,r);hpp=s.diff(hp,r)
    assert hp==-t/(4*s.pi*r**2)
    assert s.simplify(hpp-hp/r-3*t/(4*s.pi*r**3))==0
    assert s.simplify(hp/r+t/(4*s.pi*r**3))==0
    # Delta(r-c*t)=Delta(t-r/c)/c and r=c*t on its support.
    front_from_jump=s.simplify((t/r**2/c).subs(t,r/c))
    assert front_from_jump==1/(c*c*r)
    z=s.symbols('z',real=True)
    time_integrated=((1-z*z)/cT**2+z*z/cL**2+
        (3*z*z-1)*(1/cT**2-1/cL**2)/2)/(4*s.pi*alpha*r)
    assert s.simplify(time_integrated.subs({cT:1/s.sqrt(alpha*N),cL:1/s.sqrt(alpha*D)})-
                     (N+D+(N-D)*z*z)/(8*s.pi*r))==0
    return {'Euler_derivatives_and_source_sign':True,'Hamiltonian_including_interaction':True,
       'full_three_coordinate_static_inverse':True,'three_nonzero_kinetic_eigenvalues':True,
       'Fourier_ODE_and_unit_impulse_jump':True,'middle_Hessian':True,
       'shell_delta_Jacobian':True,'retarded_to_static_integral':True}

def raw_angular_geometry(order=96,nphi=12):
    q,w=leggauss(order);az=2*np.pi*np.arange(nphi)/nphi
    khat=np.array([1.,2.,-2.])/3
    transverse=np.cross(khat,[0.,0.,1.]);transverse/=np.linalg.norm(transverse)
    other=np.cross(khat,transverse)
    n=(q[:,None,None]*khat[None,None,:]+np.sqrt(1-q*q)[:,None,None]*(
        np.cos(az)[None,:,None]*transverse[None,None,:]+
        np.sin(az)[None,:,None]*other[None,None,:])).reshape(-1,3)
    aw=np.repeat(w,nphi)*(2*np.pi/nphi)
    nn=n[:,:,None]*n[:,None,:]
    return n,aw,nn,khat,transverse

def raw_transform(N,D,alpha,k,t,order=96):
    n,aw,nn,khat,transverse=raw_angular_geometry(order)
    cT,cL=1/np.sqrt(alpha*N),1/np.sqrt(alpha*D)
    a,b=cT*t,cL*t;I=np.eye(3);flat=nn.reshape(-1,9)
    def angular(radius):
        phase=np.cos(np.outer(np.atleast_1d(radius)*k,n@khat))
        weighted=phase*aw[None,:]
        return weighted.sum(axis=1), (weighted@flat).reshape(-1,3,3)
    j,dyadic=angular([a,b])
    fronts=(I*j[0]-dyadic[0]+dyadic[1])*t/(4*np.pi*alpha)
    x,w=leggauss(order)
    rr=(a+b)/2+(b-a)*x/2;rw=(b-a)*w/2
    jr,mr=angular(rr)
    middle=(t/(4*np.pi*alpha))*np.einsum('r,rij->ij',rw/rr,3*mr-jr[:,None,None]*I)
    PL=np.outer(khat,khat);PT=I-PL
    direct=(t/alpha)*(PT*np.sinc(k*a/np.pi)+PL*np.sinc(k*b/np.pi))
    return fronts+middle,direct,fronts,khat,transverse

def distribution_moments(N,D,alpha,t):
    n,aw,nn,khat,transverse=raw_angular_geometry(48)
    I=np.eye(3);cT,cL=1/np.sqrt(alpha*N),1/np.sqrt(alpha*D);a,b=cT*t,cL*t
    s0=aw.sum();s2=np.einsum('p,pij->ij',aw,nn)
    mass=t/(4*np.pi*alpha)*(I*s0-s2+s2+(3*s2-I*s0)*np.log(b/a))
    expected_mass=t/alpha*I
    maximum=0.
    for aa in range(3):
        for bb in range(3):
            weight=aw*n[:,aa]*n[:,bb]
            scalar=weight.sum();matrix=np.einsum('p,pij->ij',weight,nn)
            actual=t/(4*np.pi*alpha)*(a*a*(I*scalar-matrix)+b*b*matrix+
                  (b*b-a*a)/2*(3*matrix-I*scalar))
            ea,eb=I[:,aa],I[:,bb]
            expected=t**3/(6*alpha**2)*(2/N*int(aa==bb)*I+
                       (1/D-1/N)*(np.outer(ea,eb)+np.outer(eb,ea)))
            maximum=max(maximum,float(np.max(np.abs(actual-expected))))
    assert np.max(np.abs(mass-expected_mass))<2e-12 and maximum<2e-12
    return {'N':N,'D':D,'alpha':alpha,'t':t,'mass_error':float(np.max(np.abs(mass-expected_mass))),
            'all_81_second_moment_components_max_error':maximum}

def sharp_flux_controls():
    rows=[]
    normal=np.array([2.,-2.,1.])/3
    for N,D,alpha in [(2.,1.,1.),(5.,.2,.7),(1.4,1.4,2.),(7.,.4,1.3)]:
        mu,beta=1/N,1/D-1/N;cL=np.sqrt((mu+beta)/alpha)
        # Equality case: longitudinal traveling wave, grad=n*n^T, u_t=cL*n.
        grad=np.outer(normal,normal);v=cL*normal
        traction=mu*(normal@grad)+beta*normal*np.trace(grad)
        Q=mu*np.sum(grad*grad)+beta*np.trace(grad)**2
        normalized_flux=2*abs(v@traction)/(cL*(alpha*(v@v)+Q))
        assert abs(normalized_flux-1)<2e-15
        # Bound for every gradient follows from the exact 9D quadratic form.
        trace=np.eye(3).reshape(-1);C=mu*np.eye(9)+beta*np.outer(trace,trace)
        H=np.stack([np.outer(normal,e).reshape(-1) for e in np.eye(3)],axis=1)
        acoustic=H.T@C@H
        assert np.max(abs(acoustic-(mu*np.eye(3)+beta*np.outer(normal,normal))))<1e-14
        vals=np.linalg.eigvalsh(acoustic)/alpha
        assert np.max(abs(vals-np.array([1/(alpha*N),1/(alpha*N),1/(alpha*D)])))<1e-13
        rows.append({'N':N,'D':D,'alpha':alpha,'longitudinal_flux_ratio':float(normalized_flux),
                     'acoustic_eigenvalues':vals.tolist(),'sharp_outer_speed':float(cL)})
    return rows

def main():
    start=time.monotonic();guard()
    manifest=read(HERE/'snapshot_manifest_v1.json')
    for row in manifest['files']:
        assert sha(row['source'])==sha(HERE/row['snapshot'])==row['sha256']
    author=read(HERE/'snapshots/RESULTS.json')
    for name,digest in author['identities'].items():assert sha(HERE/'snapshots'/name)==digest
    symbolic=symbolic_checks();guard()
    cache={};checks=[];parentmax=0.;rawmax=0.
    for given in author['numerical']['real_to_Fourier_rows']:
        key=tuple(given[x] for x in ['N','D','alpha','k','t'])
        if key not in cache:cache[key]=raw_transform(*key)
        actual,expected,fronts,khat,transverse=cache[key]
        u=given['cos_theta'];e=u*khat+np.sqrt(1-u*u)*transverse
        val=float(e@actual@e);spec=float(e@expected@e)
        error=float(np.max(np.abs(actual-expected)))
        assert error<2e-11
        receipt_error=max(abs(val-given['real_integral']),abs(spec-given['spectral']))
        assert receipt_error<2e-11
        rawmax=max(rawmax,error);parentmax=max(parentmax,receipt_error)
        checks.append({**{x:given[x] for x in ['N','D','alpha','k','t','cos_theta']},
             'raw_tensor_contraction':val,'spectral_contraction':spec,
             'max_full_tensor_error':error,'max_parent_receipt_discrepancy':receipt_error})
    assert len(checks)==64 and len(cache)==16
    new=[]
    for key in [(7.,.4,1.3,.7,1.2),(1.7,.9,.6,2.1,.4),(3.,3.,.8,1.1,.7)]:
        real,direct,fronts,khat,transverse=raw_transform(*key)
        err=float(np.max(abs(real-direct)));assert err<2e-11
        new.append({'parameters':key,'max_full_tensor_error':err})
    real,direct,fronts,khat,transverse=cache[(5.,.2,.7,1.3,.9)]
    mutation=float(abs(khat@(fronts-direct)@khat));assert mutation>.5
    assert abs(mutation-author['numerical']['missing_intervening_term_mutation']['difference'])<2e-11
    moment_rows=[distribution_moments(*p) for p in [(2.,1.,1.,.7),(5.,.2,.7,.3),
                (1.4,1.4,2.,.9),(7.,.4,1.3,.4)]]
    fluxes=sharp_flux_controls()
    assert author['numerical']['flux_samples']==120 and 0<=author['numerical']['max_flux_bound_ratio']<=1
    assert len(author['numerical']['off_cone_samples'])==9
    for row in author['numerical']['off_cone_samples']:assert row['outside_front']
    # Isotropic tensor must equal a scalar wave times I for every k.
    for key,(actual,expected,fronts,khat,transverse) in cache.items():
        if key[0]==key[1]:assert np.max(abs(actual-np.eye(3)*np.trace(actual)/3))<2e-14
    guard()
    for row in manifest['files']:assert sha(row['source'])==row['sha256']
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':sha(__file__),
      'author_source_sha256':author['identities'],'symbolic':symbolic,
      'raw_tensor_transform_checks':checks,'unique_full_tensor_transforms':len(cache),
      'fresh_full_tensor_checks':new,'maximum_raw_tensor_error':rawmax,
      'maximum_parent_transform_receipt_discrepancy':parentmax,'distribution_moments':moment_rows,
      'sharp_flux_checks':fluxes,'omission_mutation_error':mutation,
      'author_flux_receipt_scope':'120 count and reported maximum checked; not an independent repetition of the author random draws. Sharp acoustic-form proof and saturated controls independently checked.',
      'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'no_author_imports':True,'empirical_arrays_read':False,'author_sources_unchanged':True,
      'scope':'Constant coefficients 0<D<=N, alpha>0, G>0, unit constant e, full compact vector data; no nonlinear or empirical inference.'}
    dump('independent_vector_checks_v1.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ['raw_tensor_transform_checks','symbolic','distribution_moments','sharp_flux_checks']},indent=2))

if __name__=='__main__':main()
