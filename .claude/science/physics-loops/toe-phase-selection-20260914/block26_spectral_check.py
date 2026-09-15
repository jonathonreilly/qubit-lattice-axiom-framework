#!/usr/bin/env python3
"""Finite spectral falsifiers, not independent validation of the clock phase."""
import datetime
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


def phi(x):
    return F(1,4)-F(4,3)*x/(x+1)+F(25,12)*x/(x+4)


def energy(u):
    return 2*np.arcsinh(np.sqrt(u)/2)


def stieltjes_atom(u,z):
    return u/(u+z)


def poisson(lam,omega):
    return (1-lam*lam)/(1-2*lam*np.cos(omega)+lam*lam)


def susceptibility_weight(lam):
    return (1+lam)/(1-lam)


def moment(T,obs,t):
    return obs.conj().T@np.linalg.matrix_power(T,t)@obs/len(T)


def band_probe(total,Sa,S4a):
    return total/4-(4/3)*Sa+(25/12)*S4a


def check_physical_score_contact():
    mp.mp.dps=65
    beta=mp.mpf('2.3');rows=[]
    for N in [5,9]:
        theta=[2*mp.pi*j/N for j in range(N)]
        prob=[];mean=[];var=[];Y=[]
        for t in theta:
            XX=[mp.sqrt(beta)*(t-2*mp.pi*m) for m in range(-18,19)]
            image=[mp.exp(-x*x/2) for x in XX];mass=mp.fsum(image)
            conditional=[v/mass for v in image]
            mu=mp.fsum(c*x for c,x in zip(conditional,XX))
            prob.append(mass);mean.append(mu)
            var.append(mp.fsum(c*(x-mu)**2 for c,x in zip(conditional,XX)))
            weight=mp.fsum(mp.cos(n*t)*mp.exp(-n*n/(2*beta)) for n in range(-35,36))
            derivative=-mp.fsum(n*mp.sin(n*t)*mp.exp(-n*n/(2*beta)) for n in range(-35,36))
            score=-derivative/(mp.sqrt(beta)*weight)
            Y.append(score)
        prob=[v/mp.fsum(prob) for v in prob]
        error=max(abs(y-m) for y,m in zip(Y,mean))
        assert error<mp.mpf('1e-55')
        vbar=mp.fsum(p*v for p,v in zip(prob,var))
        actual_variance=mp.fsum(p*y*y for p,y in zip(prob,Y))-mp.fsum(p*y for p,y in zip(prob,Y))**2
        allowed=[n for n in range(-35,36) if n%N==0]
        ww=[mp.exp(-n*n/(2*beta)) for n in allowed];mass=mp.fsum(ww);ww=[w/mass for w in ww]
        Cn=mp.fsum(w*n*n for w,n in zip(ww,allowed))-mp.fsum(w*n for w,n in zip(ww,allowed))**2
        predicted=1-vbar-Cn/beta
        assert abs(actual_variance-predicted)<mp.mpf('1e-55')
        assert vbar>1e-6 and abs(actual_variance-(1-Cn/beta))>1e-6
        rows.append({'N':N,'mean_error':str(error),
                     'vbar':str(vbar),'covariance_error':str(abs(actual_variance-predicted))})
    return {'model':'one-plaquette clock control, not a 4D phase test','rows':rows}


def check_positive_probe():
    x=sp.symbols('x',nonnegative=True)
    direct=(x-1)**2/((x+1)*(x+4))
    assert sp.factor(phi(x)-direct)==0
    derivative=(x-1)*(7*x+13)/((x+1)**2*(x+4)**2)
    assert sp.factor(sp.diff(direct,x)-derivative)==0
    assert phi(F(1))==0 and phi(F(0))==F(1,4)
    assert sp.limit(phi(x),x,sp.oo)==1
    assert F(1,4)+F(4,3)+F(25,12)==F(11,3)
    cases=[]
    for alpha,gamma in [(F(1,4),F(4)),(F(9,10),F(11,10)),(F(99,100),F(101,100))]:
        m=min(phi(alpha),phi(gamma));K=F(11,3)/m
        assert m>0
        cases.append({'alpha':str(alpha),'gamma':str(gamma),'m':str(m),'K':str(K)})
    assert cases[1]['m']=='1/1071' and cases[1]['K']=='3927'
    return {'symbolic_identity':True,'intervals':cases}


def check_finite_markov_transfer():
    # An independently specified five-state lazy nearest-neighbor chain.
    # This is a one-dimensional finite control, not the 4D clock model.
    n=5;T=np.eye(n)/2
    for j in range(n):
        T[j,(j-1)%n]+=0.25;T[j,(j+1)%n]+=0.25
    angle=2*np.pi*np.arange(n)/n
    obs=np.column_stack([np.sin(angle),np.cos(angle),np.sin(2*angle)])
    assert np.max(abs(obs.sum(axis=0)))<1e-14
    eigen,Q=np.linalg.eigh(T)
    assert min(eigen)>0 and max(abs(T.sum(axis=1)-1))<1e-14
    weights=[np.outer(row.conj(),row)/n for row in Q.T@obs]
    errors=[]
    for t in range(6):
        direct=np.zeros((3,3))
        for path in itertools.product(range(n),repeat=t+1):
            prob=1/n
            for j in range(t):prob*=T[path[j],path[j+1]]
            direct+=prob*np.outer(obs[path[0]],obs[path[-1]])
        spectral=sum((e**t*W for e,W in zip(eigen,weights)),np.zeros((3,3)))
        got=moment(T,obs,t)
        errors.extend([np.max(abs(got-direct)),np.max(abs(spectral-direct))])
    assert max(errors)<2e-13
    assert np.max(abs(moment(T,obs,0)-np.eye(3)/2))<1e-14
    active=[(e,W) for e,W in zip(eigen,weights) if np.linalg.norm(W)>1e-20]
    frequency_errors=[]
    for omega in [0.0,0.37,1.2,math.pi]:
        geom=sum((poisson(e,omega)*W for e,W in active),np.zeros((3,3)))
        direct=moment(T,obs,0)+2*sum((math.cos(omega*t)*moment(T,obs,t) for t in range(1,250)),np.zeros((3,3)))
        reconstructed=np.zeros((3,3))
        z=4*np.sin(omega/2)**2
        for lam,W in active:
            u=(1-lam)**2/lam
            reconstructed+=susceptibility_weight(lam)*stieltjes_atom(u,z)*W
        frequency_errors.extend([np.max(abs(geom-direct)),np.max(abs(geom-reconstructed))])
    assert max(frequency_errors)<2e-13
    return {'states':5,'enumerated_separations':list(range(6)),
            'moment_error':float(max(errors)),'frequency_error':float(max(frequency_errors))}


def check_midpoint_magnetic_symbol():
    # Direct origin-based d matrix, then separately apply cell midpoint phases.
    pairs=list(itertools.combinations(range(4),2))
    errors=[];ranks=[]
    for k in [np.array([.3,.4,-.2,.1]),np.array([1.2,-.6,.3,.2]),np.array([0,.4,.3,-.2])]:
        v=np.exp(1j*k)-1
        d=np.zeros((6,4),dtype=complex)
        for a,(i,j) in enumerate(pairs):d[a,j]=v[i];d[a,i]=-v[j]
        dmid=np.diag([np.exp(-.5j*(k[i]+k[j])) for i,j in pairs])@d@np.diag(np.exp(.5j*k))
        Pe=dmid@np.linalg.pinv(dmid)
        BB=np.zeros((3,6));BB[0,pairs.index((2,3))]=1;BB[1,pairs.index((1,3))]=-1;BB[2,pairs.index((1,2))]=1
        xi=2*np.sin(k[1:]/2);r2=xi@xi;w2=4*np.sin(k[0]/2)**2
        PT=np.eye(3)-np.outer(xi,xi)/r2
        expected=r2/(r2+w2)*PT
        magnetic=BB@Pe@BB.T
        errors.append(np.max(abs(magnetic-expected)))
        assert np.linalg.norm(magnetic@xi)<1e-13
        ranks.append(int(np.linalg.matrix_rank(magnetic,tol=1e-10)))
    assert max(errors)<2e-14 and ranks==[2,2,2]
    return {'momenta':3,'max_error':float(max(errors)),'magnetic_ranks':ranks}


def check_matrix_band_projection():
    # Noncommuting positive atom weights are constructed as direct Gram rows.
    p=np.array([.3,-.4,.2]);xi=2*np.sin(p/2);r=np.linalg.norm(xi);a=r*r
    normal=xi/r
    e1=np.cross(normal,[0,0,1.]);e1/=np.linalg.norm(e1);e2=np.cross(normal,e1)
    basis=np.column_stack([e1,e2])
    q1=np.array([1.,0.]);q2=np.array([0.,1.]);q3=np.array([1.,1.])/np.sqrt(2);q4=np.array([1.,-1.])/np.sqrt(2)
    small=1e-7
    u=a*np.array([1.,1.,.2,3.,40.])
    rows=np.array([np.sqrt(1-small)*q1,np.sqrt(1-small)*q2,
                   np.sqrt(small)*q3,np.sqrt(small)*q4,np.zeros(2)])
    chi_atoms=[np.outer(v,v) for v in rows]
    EE=energy(u);ll=np.exp(-EE)
    nu_atoms=[np.tanh(E/2)*W for E,W in zip(EE,chi_atoms)]
    A=np.array([np.sqrt(np.tanh(E/2))*v for E,v in zip(EE,rows)])
    T=np.diag(ll)
    errors=[]
    for z in [0,a,4*a,4]:
        omega=2*np.arcsin(np.sqrt(z)/2)
        original=A.T@(np.eye(5)-T@T)@np.linalg.inv(np.eye(5)-2*np.cos(omega)*T+T@T)@A
        S=sum((stieltjes_atom(uu,z)*W for uu,W in zip(u,chi_atoms)),np.zeros((2,2)))
        errors.append(np.max(abs(original-S)))
        assert np.linalg.norm(S-a/(a+z)*np.eye(2),2)<=small+1e-13
    assert max(errors)<1e-13
    total=sum(chi_atoms,np.zeros((2,2)))
    Sa=sum((stieltjes_atom(uu,a)*W for uu,W in zip(u,chi_atoms)),np.zeros((2,2)))
    S4a=sum((stieltjes_atom(uu,4*a)*W for uu,W in zip(u,chi_atoms)),np.zeros((2,2)))
    combined=band_probe(total,Sa,S4a)
    independent=sum((((uu/a-1)**2/((uu/a+1)*(uu/a+4)))*W for uu,W in zip(u,chi_atoms)),np.zeros((2,2)))
    assert np.max(abs(combined-independent))<1e-14
    assert np.linalg.eigvalsh(combined).min()>-1e-14
    assert np.linalg.eigvalsh(combined).max()<11*small/3
    alpha,gamma=.9,1.1
    mask=(u>=alpha*a)&(u<=gamma*a)
    lower_E,upper_E=energy(alpha*a),energy(gamma*a)
    projected=A.T@np.diag((EE>=lower_E)&(EE<=upper_E))@A
    direct=sum((W for ok,W in zip(mask,nu_atoms) if ok),np.zeros((2,2)))
    assert np.max(abs(projected-direct))<1e-14
    lower=np.sqrt(alpha)*r/np.sqrt(alpha*r*r+4)*(1-3928*small)
    upper=np.sqrt(gamma)*r/np.sqrt(gamma*r*r+4)*(1+small)
    assert np.linalg.eigvalsh(projected).min()>=lower
    assert np.linalg.eigvalsh(projected).max()<=upper
    physical=basis@projected@basis.T
    assert np.linalg.matrix_rank(physical,tol=1e-10)==2
    assert np.linalg.norm(physical@xi)<1e-14
    # Noncommuting weights: their product order is not silently interchanged.
    assert np.linalg.norm(chi_atoms[0]@chi_atoms[2]-chi_atoms[2]@chi_atoms[0])>1e-9
    return {'frequency_error':float(max(errors)),'ordinary_band_eigenvalues':np.linalg.eigvalsh(projected).tolist(),
            'ordinary_lower':float(lower),'ordinary_upper':float(upper),'physical_rank':2}


def check_contacts_and_invariant_atoms():
    # A contact can be tiny in susceptibility but dominant in equal-time norm.
    r=1e-10;eps=1e-7;u=r*r;E=energy(u)
    chi_band=1-eps;chi_contact=eps
    nu_band=np.tanh(E/2)*chi_band;nu_contact=chi_contact
    for z in [0,u,4*u,4]:
        S=chi_band*stieltjes_atom(u,z)+chi_contact
        reference=stieltjes_atom(u,z)
        assert abs(S-reference)<=eps+1e-15
    assert chi_band>.9999
    assert nu_band/(nu_band+nu_contact)<.001
    # Kernel of T is an allowed equal-time atom; it is not deleted.
    T=np.diag([0.,.4]);obs=np.array([[1.],[0.]])*np.sqrt(2*eps)
    assert abs(moment(T,obs,0)[0,0]-eps)<1e-20
    assert moment(T,obs,1)[0,0]==0
    # An invariant atom has a temporal Fourier delta, not a bounded density.
    Q=np.diag([1.,.4]);b=np.array([[1.],[0.]])
    for t in [0,1,10,100]:assert moment(Q,b,t)[0,0]==.5
    return {'static_band_fraction':chi_band,'ordinary_band_fraction':float(nu_band/(nu_band+nu_contact)),
            'contact_at_zero_transfer_kept':True,'invariant_atom_nondecay':.5}


def continuous_S(a,width,z):
    if z==0:return mp.mpf(1)
    return 1-z/(2*a*width)*mp.log((a*(1+width)+z)/(a*(1-width)+z))


def check_continuous_spectrum_and_nongaussianity():
    mp.mp.dps=65
    width=mp.mpf(1)/1000
    bound=4*width**2/(81*(1-width**2))
    assert bound<mp.mpf(1)/10**7
    errors=[];diffs=[]
    for a in [mp.mpf(1),mp.mpf(1)/100,mp.mpf(1)/10**8]:
        for ratio in [mp.mpf(0),mp.mpf('.1'),mp.mpf('.5'),mp.mpf(1),mp.mpf(4),mp.mpf(100)]:
            z=a*ratio
            numerical=mp.quad(lambda u:u/(u+z),[a*(1-width),a*(1+width)])/(2*a*width)
            exact=continuous_S(a,width,z)
            errors.append(abs(numerical-exact))
            diff=a/(a+z)-exact;diffs.append(diff)
            assert diff>=-mp.mpf('1e-58') and diff<=bound
    assert max(errors)<mp.mpf('1e-58')
    # Independent Gaussian scale mixture: same covariance, different fourth moment.
    scales=[F(1,2),F(3,2)]  # squared amplitudes, equiprobable
    variance=sum(scales)/2
    fourth=3*sum(s*s for s in scales)/2
    assert variance==1 and fourth==F(15,4) and fourth!=3*variance**2
    return {'continuous_uniform_relative_width':str(width),'global_covariance_error_bound':str(bound),
            'quadrature_error':str(max(errors)),'largest_sampled_error':str(max(diffs)),
            'no_spectral_atoms_by_definition':True,'scale_mixture_variance':str(variance),'fourth_moment':str(fourth)}


def check_parameter_certificate():
    beta=F(2000);a=beta/384-F(31,10)
    beta1_upper=(107*F(11,10)+F(7,5))/(4*F(157,50)**2)
    assert beta1_upper<F(31,10)
    assert a==F(253,120) and beta/a<1000
    assert 2*F(157,50)**2*a>59*F(7,10)
    delta_upper=F(8765200000,2**59)
    assert delta_upper<F(1,50000000)
    assert F(256016,2**9000)<F(1,50000000)
    eps=F(1,10000000)
    assert 2*F(1,50000000)<eps
    fraction=1-3927*eps/(1-eps)
    assert fraction>F(9996,10000)
    assert 1-3928*eps>F(9996,10000)
    assert F(16384**2,64*2000)>2000
    # Direct dispersion inversions across scales, independently using cosh.
    errors=[]
    for r in [1.,.1,.01,1e-4]:
        for factor in [.9,1.,1.1]:
            E=energy(factor*r*r)
            errors.append(abs((2*np.sinh(E/2))**2-factor*r*r))
            assert abs(np.arccosh(1+factor*r*r/2)-E)<2e-12
    assert max(errors)<1e-14
    return {'delta_rational_upper':str(delta_upper),'epsilon_certificate':str(eps),
            'susceptibility_fraction_lower':str(fraction),'energy_inversion_error':float(max(errors))}


FAMILIES=[check_positive_probe,check_physical_score_contact,check_finite_markov_transfer,check_midpoint_magnetic_symbol,
          check_matrix_band_projection,check_contacts_and_invariant_atoms,
          check_continuous_spectrum_and_nongaussianity,check_parameter_certificate]


def main():
    rows={}
    for fn in FAMILIES:
        rows[fn.__name__]=fn();print(json.dumps({'family':fn.__name__,'result':rows[fn.__name__]}),flush=True)
    receipt={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'scope':'eight finite families; conditional proof in text; upstream phase not independently validated',
             'families':rows}
    Path(__file__).with_name('BLOCK26_SPECTRAL_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')


if __name__=='__main__':main()
