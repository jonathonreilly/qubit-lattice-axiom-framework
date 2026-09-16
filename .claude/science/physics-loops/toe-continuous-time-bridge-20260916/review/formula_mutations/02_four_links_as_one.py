#!/usr/bin/env python3
"""Integer Gaussian calibration, character aliases, and a physical ring transfer.
Finite cutoff comparisons are diagnostics, not interval or thermodynamic proofs.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_FILES=[]
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def moments(c,extra=0):
    M=max(3,math.ceil(math.sqrt(55/c))+extra)
    assert M<100000
    k=np.arange(-M,M+1,dtype=float);w=np.exp(-c*k*k);w/=w.sum()
    return float(w@(k*k)),float(w@(k**4)),k,w


def calibrate(delta,N,g):
    target=delta*g*g*N*N/(4*math.pi**2)
    lo=min(1.,1/(4*target));hi=max(1.,1/target)
    assert moments(lo)[0]>target and moments(hi)[0]<target
    logc=brentq(lambda z:moments(math.exp(z))[0]-target,math.log(lo),math.log(hi),xtol=2e-14)
    c=math.exp(logc);assert abs(moments(c)[0]/target-1)<2e-12
    return c


def characters(c,N):
    r=np.arange(N);M=max(3,math.ceil(math.sqrt(55*c)/math.pi)+2)
    z=np.arange(-M,M+1,dtype=float)
    # Poisson form is positive even when the character sum cancels severely.
    weights=np.exp(-math.pi**2*(z[:,None]+r[None,:]/N)**2/c)
    denom=np.exp(-math.pi**2*z*z/c).sum()
    return weights.sum(axis=0)/denom


def stable_energy(c,N,r,delta):
    # Positive sine sum resolves gaps far below the spacing of floats near one.
    _,_,k,w=moments(c)
    deficit=2*float(w@np.sin(math.pi*r*k/N)**2)
    assert 0<=deficit<1
    return -math.log1p(-deficit)/delta


def spatial(y,N):
    theta=2*math.pi*np.arange(N)/N;n=np.arange(-8,9)
    w=y**(n*n);val=np.cos(theta[:,None]*n)@w/w.sum()
    assert val.min()>0 and val.max()<1+1e-14
    return val


def ring_transfer(delta,N,g,calibrated=True):
    c=calibrate(delta,N,g) if calibrated else 2*math.pi**2/(delta*g*g*N*N)
    lam=characters(c,N)
    r=np.arange(N);U=np.exp(2j*math.pi*np.outer(r,r)/N)/math.sqrt(N)
    M=(U*np.sqrt(spatial(delta/(2*g*g),N)))@U.conj().T
    T=(M*lam[None,:])@M
    assert np.linalg.norm(T-T.conj().T)<2e-12
    return T,c


def full_ring_angle_check(N,g,delta):
    c=calibrate(delta,N,g);v,mu4,k,w=moments(c)
    folded=np.zeros(N)
    for kk,ww in zip(k.astype(int),w):folded[kk%N]+=ww
    direct_lam=np.fft.fft(folded).real
    alias_lam=characters(c,N)
    assert np.max(abs(direct_lam-alias_lam))<2e-13
    # Actual N^4 angle configurations and the integer-divergence Gauss basis.
    coords=np.indices((N,)*4);total=coords.sum(axis=0)%N;dim=N**4
    phi=np.exp(2j*math.pi*total.reshape(-1,1)*np.arange(N)[None,:]/N)/math.sqrt(dim)
    assert np.linalg.norm(phi.conj().T@phi-np.eye(N))<2e-12
    flux=spatial(delta/(2*g*g),N)[total].reshape(-1)
    F=(np.sqrt(flux)[:,None]*phi).reshape((N,)*4+(N,))
    four=np.fft.fftn(F,axes=(0,1,2,3),norm='ortho')
    diag=np.ones((N,)*4)
    for i in range(4):diag*=direct_lam[coords[i]]
    transformed=np.fft.ifftn(four*diag[...,None],axes=(0,1,2,3),norm='ortho').reshape(dim,N)
    observed=phi.conj().T@(np.sqrt(flux)[:,None]*transformed)
    expected,_=ring_transfer(delta,N,g)
    err=float(np.linalg.norm(observed-expected))
    assert err<2e-12
    # A physical electric state has equal oriented flux on all four links.
    gauss_bad=0
    for fluxes in itertools.product(range(N),repeat=4):
        ok=all((fluxes[i]-fluxes[(i-1)%4])%N==0 for i in range(4))
        gauss_bad+=ok and len(set(fluxes))!=1
    assert gauss_bad==0
    return {'N':N,'full_angle_states':dim,'physical_dimension':N,'character_duality_error':float(np.max(abs(direct_lam-alias_lam))),'full_angle_vs_reduced_transfer_error':err}


def rotor_vector(g,t,cut):
    n=np.arange(-cut,cut+1);H=np.diag(2*g*g*n*n+1/(g*g))
    H+=np.diag(np.full(2*cut,-1/(2*g*g)),1)+np.diag(np.full(2*cut,-1/(2*g*g)),-1)
    e,u=eigh(H);return (u*np.exp(-t*e))@u[cut,:]


def ring_paths():
    g=.7;t=.8;out=[]
    for path in ['inverse_N','inverse_N_squared','inverse_N_cubed']:
        rows=[]
        for N in [9,17,33,65,129]:
            delta=1/N if path=='inverse_N' else 4/N**2 if path=='inverse_N_squared' else 4/N**3
            steps=max(1,math.floor(t/delta));tt=steps*delta
            T,c=ring_transfer(delta,N,g);ev,u=eigh(T)
            assert ev.min()>-2e-13 and ev.max()<1+2e-13
            vec=(u*ev**steps)@u[0,:].conj()
            cut=80;ref=rotor_vector(g,tt,cut);ref2=rotor_vector(g,tt,cut+20)
            target=np.zeros_like(ref,dtype=complex);r=np.arange(N);signed=np.where(r<=N//2,r,r-N)
            target[cut+signed]=vec
            err=float(np.linalg.norm(target-ref));tailcheck=float(np.linalg.norm(ref-ref2[20:-20]))
            assert tailcheck<2e-13
            wrong,_=ring_transfer(delta,N,g,False);ee,uu=eigh(wrong);wv=(uu*ee**steps)@uu[0,:].conj();wtarget=np.zeros_like(ref,dtype=complex);wtarget[cut+signed]=wv
            rows.append({'N':N,'delta':delta,'steps':steps,'actual_time':tt,'calibration_c':c,'joint_J':delta*g*g*N*N/2,'calibrated_semigroup_vector_error':err,'uncalibrated_heat_sample_error':float(np.linalg.norm(wtarget-ref)),'rotor_cutoff_change':tailcheck})
        assert rows[-1]['calibrated_semigroup_vector_error']<rows[0]['calibrated_semigroup_vector_error']/8,rows
        assert rows[-1]['calibrated_semigroup_vector_error']<2e-3,rows
        out.append({'path':path,'rows':rows})
    assert out[1]['rows'][-1]['uncalibrated_heat_sample_error']>.05
    return out


def run():
    started=time.time();moment_rows=[]
    for c in [.001,.01,.1,.3,1.,3.,10.,30.]:
        v,m4,k,w=moments(c);vv,mm,_,_=moments(c,10)
        assert abs(v-vv)<1e-11 and abs(m4-mm)<1e-7
        assert m4<=224*(v+v*v)
        vd=moments(math.pi**2/c)[0];err=abs(v-(1-2*math.pi**2/c*vd)/(2*c))
        assert err<1e-10
        moment_rows.append({'c':c,'variance':v,'fourth_moment':m4,'moment_bound_ratio':m4/(v+v*v),'poisson_variance_error':err})
    crossover=[]
    for J in [.1,.5,1.,2.,4.,8.,16.]:
        D=2*math.pi**2/J*moments(math.pi**2/J)[0];dual=1-2*J*moments(J)[0]
        assert -1e-13<D<1+1e-13 and abs(D-dual)<2e-13
        N=1025;g=.7;delta=2*J/(g*g*N*N);lam=characters(math.pi**2/J,N)[1]
        energy=stable_energy(math.pi**2/J,N,1,delta);pred=g*g/2*D
        assert abs(energy-pred)<2e-6
        assert abs(energy/pred-1)<2e-5
        crossover.append({'J':J,'D':D,'finite_energy':energy,'limiting_energy':pred})
    low=[]
    for N in [17,65,257,1025]:
        for power in [1,2,3]:
            g=.7;delta=N**(-power);c=calibrate(delta,N,g);lam=characters(c,N)
            for r in [1,2,3]:
                observed=stable_energy(c,N,r,delta);target=g*g*r*r/2
                bound=400*r**4*(g*g/N**2+delta*g**4)
                assert abs(observed-target)<=bound+2e-6,(N,power,r,observed,target,bound)
                low.append({'N':N,'power':power,'r':r,'energy':observed,'target':target,'error':abs(observed-target),'analytic_bound':bound})
    physical=[full_ring_angle_check(N,.7,.03) for N in [3,5]]
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'integer_gaussian_moments':moment_rows,'uncalibrated_crossover':crossover,'calibrated_low_modes':low,'physical_ring_checks':physical,'joint_ring_paths':ring_paths(),'seconds':time.time()-started},indent=2))

if __name__=='__main__':run()
