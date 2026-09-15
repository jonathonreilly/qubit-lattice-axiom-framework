"""Exact-moment and integrated Bochner challenges from the original clock source.

The source sums original tree-gauge clock links and image integers, then
applies Gaussian smoothing. It does not sample the proposed generator.
These finite floating checks are not a response theorem or interval proof.
"""
import json
import math
from pathlib import Path
import numpy as np
from block1_hybrid_generator_check import PhysicalSource


def check(N, beta):
    law=PhysicalSource(N,beta,1/64)
    h=2*math.pi*math.sqrt(beta)
    moves=np.array([s*h*np.eye(6)[p] for p in range(6) for s in [-1,1]])
    qs=np.einsum('vi,ij,vj->v',moves,law.A,moves)
    pair=moves@law.A@moves.T
    moments=[]
    maximum=0.
    for v,q in zip(moves,qs):
        Av=law.A@v
        vals={k: float((math.exp(-k*q/4)*law.mgf(-k*Av/2)).real)
              for k in [0.,.5,1.,1.5,2.,3.,4.]}
        targets={2.:1.,3.:math.exp(q/2)*vals[1.],4.:math.exp(q)}
        for k,target in targets.items():
            error=abs(vals[k]-target)/max(abs(target),1e-300)
            maximum=max(maximum,error)
            assert error<2e-12, (N,beta,k,error)
        assert abs(vals[.5]-vals[1.5])/vals[.5]<2e-12
        assert vals[1.]<=math.exp(-q/8)+2e-13
        moments.append(dict(q=float(q),mean=vals[1.],second=vals[2.],
                            fourth=vals[4.],variance=vals[2.]-vals[1.]**2))
    weights=np.empty((12,12))
    for i,v in enumerate(moves):
        for j,w in enumerate(moves):
            weights[i,j]=(math.exp(-(qs[i]+qs[j])/4)
                           *law.mgf(-law.A@(v+w)/2)).real
    r=np.exp(-pair/4)
    bound=np.exp(-(qs[:,None]+qs[None,:])/8)
    assert np.max(weights*r-bound)<3e-13
    # Complex Fourier test: |exp(i t.z)|=1, so all products reduce to
    # original-law rate-product moments. No stationarity is assumed here.
    source=np.array([.17,-.31,.23,.07,-.19,.11])
    bochner=[]
    for scale in [.25,.5,1.,2.]:
        diffs=np.expm1(1j*(moves@(scale*source)))
        cross=np.conjugate(diffs[:,None])*diffs[None,:]
        lhs=np.sum(weights*cross)
        second=np.sum(weights*r*(abs(diffs[:,None]*diffs[None,:])**2))/4
        residual=np.sum(weights*(1-r)*cross)
        rhs=second+residual
        error=abs(lhs-rhs)/max(abs(lhs),1e-30)
        assert error<2e-12,(N,beta,scale,error)
        assert abs(lhs.imag)<2e-13
        assert lhs.real>=0
        bochner.append(dict(scale=scale,lhs=float(lhs.real),
                            second_difference=float(second),
                            residual=float(residual.real),relative_error=float(error)))
    return dict(N=N,beta=beta,max_moment_relative_error=maximum,moments=moments,
                max_pair_weight_minus_bound=float(np.max(weights*r-bound)),bochner=bochner)


def main():
    result=dict(status='actual_source_moments_and_integrated_identity_checked',
                rows=[check(N,beta) for N,beta in [(2,.25),(3,.5),(4,.8)]],
                scope='Finite three-cube algebra; no gap, perturbative response, '
                      'infinite-volume theorem, interval certificate, or independent review.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
