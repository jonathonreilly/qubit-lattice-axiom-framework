#!/usr/bin/env python3
"""Finite-spin compatibility and Gaussian reservoir adaptation controls."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np
import scipy.linalg as la
import scipy.sparse as ss
import scipy.sparse.linalg as sla
import sympy as sp

import local_gauge_record_cooling_check as geom

OUT=Path(__file__).resolve().parent


def finite_spin_controls():
    dependency=OUT/'local_gauge_record_cooling_check.py'
    expected='9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552'
    assert hashlib.sha256(dependency.read_bytes()).hexdigest()==expected
    rows=[]
    for shape,periodic in [((2,2),False),((3,2),False),((2,2,2),False),((2,2,2),True)]:
        vertices,edges,faces=geom.geometry(shape,periodic)
        if periodic:
            seed=sum(1<<j for j,(v,a,w) in enumerate(edges) if sum(v[b] for b in range(3) if b!=a)%2==0)
            states,tree=geom.component(seed,faces)
        else:
            groups=[];unseen=set(range(1<<len(edges)))
            while unseen:
                states,tree=geom.component(min(unseen),faces);unseen.difference_update(states);groups.append(states)
            states=max(groups,key=len)
        pairs=geom.pairs_from_component(states,faces);d=len(states)
        nf=np.zeros(d,dtype=int);lops=[];hrk=np.zeros((d,d),float)
        for pairlist in pairs:
            for a,b in pairlist:nf[a]+=1;nf[b]+=1
            l=geom.matching_matrix(d,pairlist)/2
            hrk+=2*l.T@l
            if d<=9:lops.append(l)
        mean=Fraction(int(sum(nf)),d)
        variance=Fraction(int(sum(nf*nf)),d)-mean*mean
        u=np.ones(d)/np.sqrt(d);assert np.max(abs(hrk@u))<1e-12
        row={'shape':shape,'periodic':periodic,'dimension':d,'flippability_census':dict(sorted(Counter(map(int,nf)).items())),
             'mean_flippability':str(mean),'variance_flippability':str(variance),
             'squared_HS_residual_over_delta2':str(2*variance),
             'pure_stationary_with_unchanged_jumps_at_nonzero_delta':variance==0}
        if d<=9:
            nmat=np.diag(nf);delta=.4;ham=hrk-delta*nmat;eye=np.eye(d)
            g=-1j*(np.kron(eye,ham)-np.kron(ham.T,eye))
            for p,l in enumerate(lops):
                pm=l.T@l;rate=p+1
                g+=rate*(np.kron(l,l)-(np.kron(eye,pm)+np.kron(pm.T,eye))/2)
            target=np.outer(u,u);res=(g@target.reshape(-1,order='F')).reshape((d,d),order='F')
            assert abs(la.norm(res)**2-2*delta*delta*float(variance))<1e-12
            lhs=g.copy();rhs=np.zeros(d*d,complex);lhs[0]=np.eye(d).reshape(-1,order='F');rhs[0]=1
            rho=la.solve(lhs,rhs).reshape((d,d),order='F')
            assert la.norm(rho-rho.conj().T)<1e-10 and la.eigvalsh(rho).min()>-1e-10
            assert la.norm(g@rho.reshape(-1,order='F'))<1e-10
            purity=float(np.trace(rho@rho).real)
            if variance:assert purity<1-1e-5
            else:assert abs(purity-1)<1e-10
            row['finite_stationary_control']={'delta':delta,'rates':'p+1','purity':purity,
                'RK_fidelity':float((u@rho@u).real),'stationary_residual':float(la.norm(g@rho.reshape(-1,order='F'))),
                'jump_intensity':float(sum((p+1)*np.trace(l.T@l@rho).real for p,l in enumerate(lops)))}
        rows.append(row)
    return {'geometry_dependency_sha256':expected,'cases':rows}


def symbolic_covariance():
    a,b,r,nu=sp.symbols('a b r nu',positive=True,real=True)
    z=nu**2+4*a*b;d0=a/r-b*r
    q=r/2+a*d0/z;p=1/(2*r)-b*d0/z;c=nu*d0/(2*z)
    v=sp.Matrix([[q,c],[c,p]]);drift=sp.Matrix([[-nu/2,a],[-b,-nu/2]])
    noise=nu*sp.diag(r,1/r)/2
    assert (drift*v+v*drift.T+noise).applyfunc(sp.factor)==sp.zeros(2)
    assert sp.factor(v.det()-sp.Rational(1,4)-d0*d0/(4*z))==0
    assert sp.factor((b*q+a*p)/2-(b*r+a/r)/4)==0
    assert sp.factor((q/r+r*p-1)/2-d0*d0/(2*z))==0
    aa,bb,cc=sp.symbols('Q P C',real=True)
    vv=sp.Matrix([[aa,cc],[cc,bb]]);dv=drift*vv+vv*drift.T+noise
    assert sp.factor((b*dv[0,0]+a*dv[1,1])/2+nu*((b*aa+a*bb)/2-(b*r+a/r)/4))==0
    lam=sp.symbols('lambda')
    assert sp.factor(drift.charpoly(lam).as_expr()-(lam+nu/2)**2-a*b)==0
    k,w,u,g,s=sp.symbols('K W U gamma s',positive=True,real=True)
    sub={a:k*s,b:u+w*s,r:sp.sqrt(k/w),nu:g*s}
    newn=((b*r+a/r)/(4*sp.sqrt(a*b))-sp.Rational(1,2)).subs(sub)
    expressions={'Q':q.subs(sub),'sP':(s*p).subs(sub),'C':c.subs(sub),
                 'energy':((b*r+a/r)/4).subs(sub),'sqrt_s_new_occupation':sp.sqrt(s)*newn,
                 'jump_rate':(nu*d0*d0/(2*z)).subs(sub)}
    expected={'Q':sp.sqrt(k/w)/4,'sP':u*sp.sqrt(k/w)/(4*k),'C':-g*sp.sqrt(k/w)/(8*k),
              'energy':u*sp.sqrt(k/w)/4,'sqrt_s_new_occupation':sp.sqrt(u/w)/4,'jump_rate':g*u/(8*w)}
    limits={}
    for name,expr in expressions.items():
        val=sp.simplify(sp.limit(expr,s,0,dir='+'));assert sp.simplify(val-expected[name])==0
        limits[name]=str(val)
    matched=sp.sqrt(a/b)
    assert sp.simplify(d0.subs(r,matched))==0
    assert (v.subs(r,matched)-sp.diag(matched,1/matched)/2).applyfunc(sp.simplify)==sp.zeros(2)
    return {'stationary_covariance_residual':'zero exactly for independent positive a,b,r,nu',
            'determinant':'1/4+(a/r-br)^2/[4(nu^2+4ab)]',
            'energy_identity':'dE/dt=-nu(E-(br+a/r)/4), exactly',
            'old_mode_occupation':'(a/r-br)^2/[2(nu^2+4ab)]',
            'drift_characteristic_polynomial':'(lambda+nu/2)^2+ab',
            'infrared_limits':limits,'matched_bath':'r=sqrt(a/b) gives exact pure ground covariance'}


def covariance_formula(s,K,W,U,gamma,matched=False):
    a=K*s;b=U+W*s;nu=gamma*s;r=np.sqrt(a/b) if matched else np.sqrt(K/W)
    z=nu*nu+4*a*b;d=a/r-b*r
    v=np.array([[r/2+a*d/z,nu*d/(2*z)],[nu*d/(2*z),1/(2*r)-b*d/z]])
    return v,(a,b,nu,r)


def fock_stationary(cutoff,s,K,W,U,gamma,matched=False):
    # Project the normally ordered infinite-oscillator H and observables,
    # rather than squaring truncated q/p and altering the top-level diagonal.
    a=K*s;b=U+W*s;nu=gamma*s;r0=np.sqrt(K/W)
    ann=ss.diags(np.sqrt(np.arange(1,cutoff)),1,shape=(cutoff,cutoff),format='csc')
    cre=ann.T;num=ss.diags(np.arange(cutoff),format='csc');eye=ss.eye(cutoff,format='csc')
    aa=ann@ann;dd=cre@cre
    q2=r0*(aa+dd+2*num+eye)/2
    p2=(-aa-dd+2*num+eye)/(2*r0)
    qp=(aa-dd)/(2j)
    ham=(b*q2+a*p2)/2
    if matched:
        rtarget=np.sqrt(a/b);ratio=np.sqrt(r0/rtarget)
        jump=np.sqrt(nu)*((ratio+1/ratio)*ann+(ratio-1/ratio)*cre)/2
    else:jump=np.sqrt(nu)*ann
    loss=jump.conj().T@jump
    gen=-1j*(ss.kron(eye,ham)-ss.kron(ham.T,eye))+ss.kron(jump.conj(),jump)
    gen-= (ss.kron(eye,loss)+ss.kron(loss.T,eye))/2
    gen=gen.tocsc();system=gen.tolil();system[0,:]=0
    for j in range(cutoff):system[0,j*(cutoff+1)]=1
    rhs=np.zeros(cutoff**2,complex);rhs[0]=1
    vec=sla.spsolve(system.tocsc(),rhs);rho=vec.reshape((cutoff,cutoff),order='F')
    residual=float(np.max(abs(gen@vec)))
    assert residual<1e-9 and la.norm(rho-rho.conj().T)<1e-9
    assert la.eigvalsh(rho).min()>-1e-9
    obs=lambda op:float(np.trace(op@rho).real)
    measured=np.array([[obs(q2),obs(qp)],[obs(qp),obs(p2)]])
    exact,params=covariance_formula(s,K,W,U,gamma,matched)
    energy=obs(ham);target=np.sqrt(a*b)/2
    return {'cutoff':cutoff,'covariance':measured.tolist(),'covariance_max_error':float(np.max(abs(measured-exact))),
            'energy':energy,'ground_energy':target,'new_mode_occupation':energy/(2*target)-.5,
            'jump_intensity':obs(loss),'purity':float(np.trace(rho@rho).real),
            'top_two_probability':float(np.diag(rho)[-2:].real.sum()),'stationary_max_residual':residual}


def numerical_controls():
    rows=[]
    for s,K,W,U,gamma in [(.25,1.,1.,1.,.4),(.0625,1.,1.,1.,1.),(1.,1.,1.,2.,2.),(.36,1.,1.,0.,.7),(.25,2.,.5,1.,.3)]:
        exact,(a,b,nu,r)=covariance_formula(s,K,W,U,gamma)
        drift=np.array([[-nu/2,a],[-b,-nu/2]])
        noise=nu*np.diag([r,1/r])/2
        lyap=la.solve_continuous_lyapunov(drift,-noise)
        assert np.max(abs(exact-lyap))<1e-11
        result=[fock_stationary(n,s,K,W,U,gamma) for n in (32,64,96)]
        assert result[-1]['covariance_max_error']<2e-4,(s,K,W,U,gamma,result[-1])
        assert result[-1]['top_two_probability']<2e-6
        estar=(b*r+a/r)/4
        assert abs(result[-1]['energy']-estar)<2e-5
        rate=nu*(a/r-b*r)**2/(2*(nu*nu+4*a*b))
        assert abs(result[-1]['jump_intensity']-rate)<2e-5
        rows.append({'s':s,'K':K,'W':W,'U':U,'gamma':gamma,'exact_covariance':exact.tolist(),
                     'exact_energy':estar,'exact_jump_rate':rate,'Fock_controls':result})
    matched=[]
    for s in [.25,.0625]:
        result=[fock_stationary(n,s,1.,1.,1.,1.,True) for n in (48,96)]
        assert result[-1]['covariance_max_error']<2e-6
        assert result[-1]['new_mode_occupation']<2e-6
        assert abs(result[-1]['purity']-1)<2e-6
        matched.append({'s':s,'K':1,'W':1,'U':1,'gamma':1,'Fock_controls':result})
    rate_controls=[]
    for gamma in [.02,.2,2.,20.]:
        v,(a,b,nu,r)=covariance_formula(.1,1.,1.,1.,gamma)
        energy=(b*v[0,0]+a*v[1,1])/2
        assert abs(energy-.3)<1e-12
        rate_controls.append({'s':.1,'gamma':gamma,'energy':energy,'ground_energy':np.sqrt(.11)/2,
                              'covariance':v.tolist()})
    return {'mismatched_bath':rows,'matched_positive_alternative':matched,'varying_rate_same_energy':rate_controls,
            'cutoff_boundary':'Direct finite Fock Lindblad solves provide convergence controls only; the exact oscillator proof is the symbolic moment algebra.'}


def main():
    result={'status':'PASS','finite_spin':finite_spin_controls(),'symbolic_gaussian':symbolic_covariance(),
            'numeric_gaussian':numerical_controls(),
            'scope':'Finite supplied spin model plus a separately stipulated Gaussian reservoir; no microscopic derivation of gamma*s, infinite-volume phase proof, or native record compiler.'}
    (OUT/'RK_COOLING_HAMILTONIAN_CHANGE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
