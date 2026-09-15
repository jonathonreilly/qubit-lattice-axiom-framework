#!/usr/bin/env python3
"""Personal inverse-moment checks using Fourier diagonalization and direct solves."""
from pathlib import Path
import hashlib,itertools,json
import numpy as np
from scipy.special import logsumexp

def main():
    cases=[]
    for N,beta in [(2,.3),(2,.85),(3,.4),(3,1.1),(4,.8)]:
        config=np.array(list(itertools.product(range(N),repeat=4)))
        count=len(config)
        theta=2*np.pi*np.arange(N)/N
        w=np.exp(logsumexp(-beta*(theta[:,None]+2*np.pi*np.arange(-10,11))**2/2,axis=1))
        coeff=np.fft.fft(w).real/N
        assert np.max(abs(np.fft.fft(w).imag))/N<1e-13 and coeff.min()>0
        ks=np.arange(-50,51)
        alias=np.array([np.exp(-ks[ks%N==k]**2/(2*beta)).sum() for k in range(N)])
        assert np.max(abs(coeff/coeff[0]-alias/alias[0]))<3e-13
        # Nonconstant spatial weight, as in a physical spatial square.
        V=w[config.sum(axis=1)%N];root=np.sqrt(V)
        diff=(config[:,None,:]-config[None,:,:])%N
        C=np.prod(w[diff],axis=2)/count
        T=root[:,None]*C*root[None,:]
        eig,vec=np.linalg.eigh(T);largest=eig[-1];Omega=vec[:,-1]
        if Omega.sum()<0:Omega=-Omega
        assert Omega.min()>0 and eig[0]>0
        # Product characters diagonalize C independently of eigh(T).
        fourier=np.exp(2j*np.pi*(config@config.T)/N)/np.sqrt(count)
        ceig=np.prod(coeff[config],axis=1)
        assert np.linalg.norm(C@fourier-fourier*ceig[None,:])<2e-12
        for j in [np.array([q,0,0,0]) for q in (0,1,N-1,N)]+[np.array([1,1,0,0]),np.ones(4,dtype=int)]:
            phase=np.exp(2j*np.pi*(config@j)/N);psi=phase*Omega
            ratios=coeff[config]/coeff[(config+j)%N]
            K=float(np.prod([max(coeff/coeff[(np.arange(N)+int(q))%N]) for q in j]))
            assert K>=1-1e-13 and abs(K-ratios.prod(axis=1).max())<2e-11*max(1,K)
            inverse=largest*float(np.vdot(psi,np.linalg.solve(T,psi)).real)
            spectral=float(np.sum(abs(vec.conj().T@psi)**2*largest/eig))
            assert abs(inverse-spectral)<3e-9*max(1,inverse)
            assert inverse<=K*(1+3e-10) and inverse>=1-3e-10
            # Whitened C-inverse comparison has exactly the local ratios.
            cinv=(fourier/ceig[None,:])@fourier.conj().T
            csqrt=(fourier*np.sqrt(ceig)[None,:])@fourier.conj().T
            shifted=np.conj(phase)[:,None]*cinv*phase[None,:]
            whitened=csqrt@shifted@csqrt
            high=float(np.linalg.eigvalsh(whitened)[-1])
            assert abs(high-K)<3e-9*max(1,K)
            weights=abs(vec.conj().T@psi)**2;energies=-np.log(eig/largest)
            moments=[float(np.sum(weights*energies**p)) for p in (1,2,3)]
            for p,moment in zip((1,2,3),moments):
                import math
                assert moment<=math.factorial(p)*K*(1+3e-10)
            if np.all(j%N==0):assert abs(inverse-1)<3e-10 and abs(K-1)<1e-13
            cases.append({'N':N,'beta':beta,'j':j.tolist(),'dimension':count,'K':K,'inverse_moment':inverse,
                'spectral_inverse_moment':spectral,'direct_spectral_relative_error':abs(inverse-spectral)/max(1,inverse),
                'whitened_comparison_norm':high,'energy_moments_1_2_3':moments})
    # A zero-shift comparison K=1 is actually false for a charged insertion.
    assert max(x['inverse_moment'] for x in cases)>1.1
    result={'status':'personal_floating_checks_not_independent_review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'cases':cases,'limits':'Finite floating comparisons, no interval proof of matrix positivity or infinite-volume passage.'}
    dest=Path(__file__).with_name('BLOCK32_STATIC_TRANSFER_INVERSE_CHECKS.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cases':len(cases),'max_inverse_moment':max(x['inverse_moment'] for x in cases),
      'max_relative_discrepancy':max(x['direct_spectral_relative_error'] for x in cases),'output':str(dest)}))
if __name__=='__main__':main()
