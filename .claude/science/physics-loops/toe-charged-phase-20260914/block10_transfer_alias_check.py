from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.linalg import eigh
from scipy.special import ive


def wilson_Q(N,delta,t):
    alpha=1-np.cos(2*np.pi/N);x=delta*t*(2 if N==2 else 1)
    beta=np.log(1/x)/alpha;angles=2*np.pi*np.arange(N)/N
    weights=np.exp(-beta*(1-np.cos(angles)));weights/=weights.sum()
    Q=np.zeros((N,N))
    for q,p in enumerate(weights):Q+=p*np.roll(np.eye(N),q,axis=0)
    assert np.min(eigh(Q,eigvals_only=True))>0
    return Q,beta


def villain_Q(N,delta,t):
    x=delta*t;Q=np.zeros((N,N));normal=0.
    for q in range(-8,9):
        weight=x**(q*q);Q+=weight*np.roll(np.eye(N),q,axis=0);normal+=weight
    return Q/normal,N*N*np.log(1/x)/(2*np.pi**2)


def matched_single_plaquette():
    rows=[];t=.7;K=1.1
    for N in [2,3,4,5,8]:
        X=np.roll(np.eye(N),1,axis=0);angles=2*np.pi*np.arange(N)/N
        H=4*t*(2*np.eye(N)-X-X.T)+np.diag(K*(1-np.cos(angles)))
        previous={key:float('inf') for key in ['Wilson','Villain']}
        for delta in [1e-2,1e-3,1e-4]:
            for regulator,make_Q in [('Wilson',wilson_Q),('Villain',villain_Q)]:
                Q,beta_t=make_Q(N,delta,t)
                if regulator=='Wilson':
                    B=np.exp(-delta*K*(1-np.cos(angles)));beta_s=delta*K
                else:
                    y=delta*K/2;B=sum(y**(n*n)*np.cos(n*angles) for n in range(-8,9))/sum(y**(n*n) for n in range(-8,9));beta_s=1/(2*np.log(1/y))
                D=np.diag(np.sqrt(B));T=D@np.linalg.matrix_power(Q,4)@D
                eigen,U=eigh(T);assert np.min(eigen)>0
                generator=(U*(-np.log(eigen)/delta))@U.T
                error=np.linalg.norm(generator-H,2)
                assert error<previous[regulator] and error/delta<200
                previous[regulator]=error
                rows.append({'N':N,'delta':delta,'regulator':regulator,'generator_error':error,'bare_product':beta_s*beta_t})
    print('matched_single_plaquette',rows,flush=True)


def exact_alias_schedule():
    rows=[]
    with mp.workdps(100):
        N=8;t=mp.mpf('.7');eta=mp.mpf('.5')
        for ell in map(mp.mpf,[8,16,32,64]):
            delta=mp.exp(-ell)/t;x=delta*t;beta=N*N*ell/(2*mp.pi**2)
            M=int(mp.ceil(mp.sqrt(1+eta)*ell/mp.pi+mp.mpf('.5')))
            a=mp.pi**2/ell;tail=2*mp.exp(-a*(M+mp.mpf('.5'))**2)/(1-mp.exp(-a*(2*M+2)))
            schedule_bound=16*t**(1+eta)*delta**eta/mp.expm1(2*mp.pi*mp.sqrt(1+eta))
            assert x<=mp.mpf(1)/8 and 2*tail<=mp.mpf(1)/4
            assert 8*tail/delta<=schedule_bound
            errors=[]
            for k in range(-N//2,N//2+1):
                dual=mp.fsum(x**(r*r)*mp.cos(2*mp.pi*r*k/N) for r in range(-8,9))/mp.fsum(x**(r*r) for r in range(-8,9))
                aliases=lambda kk,m:mp.fsum(mp.exp(-(kk+j*N)**2/(2*beta)) for j in range(-m,m+1))
                truncated=aliases(k,M)/aliases(0,M);full=aliases(k,100)/aliases(0,100)
                assert abs(full-dual)<mp.mpf('1e-95')
                assert abs(full-truncated)<=2*tail
                gap_error=abs(mp.log(full)-mp.log(truncated))/delta
                assert gap_error<=8*tail/delta
                target=t*(2-2*mp.cos(2*mp.pi*k/N))
                assert abs(-mp.log(dual)/delta-target)<20*delta
                errors.append(gap_error)
            rows.append({'ell':str(ell),'alias_cutoff':M,'max_generator_error':str(max(errors)),'rigorous_bound':str(8*tail/delta),'uniform_delta_eta_bound':str(schedule_bound)})
        divergence=[]
        for M in [0,2]:
            for ell in map(mp.mpf,[100,1000,10000]):
                delta=mp.exp(-ell)/t;beta=N*N*ell/(2*mp.pi**2);k=1
                A=lambda kk:mp.fsum(mp.exp(-(kk+j*N)**2/(2*beta)) for j in range(-M,M+1))
                gap=-mp.log(A(k)/A(0))/delta;asymptotic=k*k/(2*beta*delta)
                ratio=gap/asymptotic
                assert gap>100 and ratio>0
                if ell==10000:assert abs(ratio-1)<.01
                divergence.append({'fixed_alias_cutoff':M,'ell':str(ell),'gap_over_divergent_asymptotic':str(ratio)})
    print('exact_alias_schedule',{'controlled_cutoffs':rows,'fixed_cutoff_divergence':divergence},flush=True)


def spatial_hessian_and_local_shift():
    rows=[];N=8;t=.7;K=1.1
    for ell in [5,10,20,40]:
        delta=np.exp(-ell)/t;y=delta*K/2;beta_s=1/(2*np.log(1/y))
        curvature=sum(n*n*y**(n*n) for n in range(-8,9))/sum(y**(n*n) for n in range(-8,9))
        assert abs(curvature/(delta*K)-1)<3*delta*K
        alphaN=1-np.cos(2*np.pi/N);beta_t=ell/alphaN;B=6*beta_t
        shift=np.arcsinh(N/B);I=N*shift-np.hypot(B,N)+B
        expected=N*N/(2*B)
        # Direct Bessel ratio checks the actual zero-background conditional
        # harmonic, independent of the optimized complex-shift upper estimate.
        conditional=ive(N,B)/ive(0,B)
        assert abs(I/expected-1)<.002 and conditional<=np.exp(-I)+1e-12
        if ell>=10:assert abs((1-conditional)/expected-1)<.1
        rows.append({'ell':ell,'periodized_spatial_curvature_over_delta':curvature/delta,'bare_spatial_beta_over_delta':beta_s/delta,'optimized_suppression':np.exp(-I),'actual_conditional_Nth_harmonic':conditional})
    print('spatial_hessian_and_local_shift',rows,flush=True)


if __name__=='__main__':
    matched_single_plaquette()
    exact_alias_schedule()
    spatial_hessian_and_local_shift()
