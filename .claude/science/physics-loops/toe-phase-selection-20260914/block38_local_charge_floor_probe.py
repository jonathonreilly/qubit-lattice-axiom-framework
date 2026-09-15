#!/usr/bin/env python3
from pathlib import Path
import itertools,hashlib,json
import numpy as np

def main():
    rows=[]
    D=np.zeros((4,4),dtype=int)
    for e in range(4):D[e,e]=-1;D[e,(e+1)%4]=1
    for N,beta in [(2,.4),(3,.6),(4,.8)]:
        a=np.array(list(itertools.product(range(N),repeat=4)));size=len(a)
        theta=2*np.pi*np.arange(N)/N
        w=np.exp(-beta*(theta[:,None]+2*np.pi*np.arange(-10,11))**2/2).sum(axis=1)
        delta2=float((w.min()/w.max())**2);delta6=float((w.min()/w.max())**6)
        r=1-delta2;assert 0<r<1
        Fourier=np.exp(2j*np.pi*(a@a.T)/N)/np.sqrt(size)
        diff=(a[:,None,:]-a[None,:,:])%N
        C=np.prod(w[diff],axis=2)/size
        root=np.sqrt(w[a.sum(axis=1)%N]);T=root[:,None]*C*root[None,:]
        lam=np.linalg.eigvalsh(T)[-1];Tf=Fourier.conj().T@T@Fourier
        kernels={}
        def kernel(rho):
            key=tuple(rho%N)
            if key not in kernels:
                K=np.zeros((size,size),dtype=complex)
                for eta in a:
                    K+=np.prod(w[(diff+D@eta)%N],axis=2)*np.exp(-2j*np.pi*(rho@eta)/N)/(size**2)
                kernels[key]=K
            return kernels[key]
        K0=kernel(np.zeros(4,dtype=int));assert np.max(abs(K0.imag))<2e-13 and K0.real.min()>0
        cases=[]
        for current in [np.array([1,0,0,0]),np.array([1,1,0,0]),np.array([1,0,1,0]),np.array([N,0,0,0])]:
            rho=D.T@current;charge=rho%N;support=np.flatnonzero(charge)
            independent=[]
            for bits in itertools.product((0,1),repeat=len(support)):
                selected=[int(v) for v,bit in zip(support,bits) if bit]
                if all((u-v)%4 not in (1,3) for u,v in itertools.combinations(selected,2)) and len(selected)>len(independent):independent=selected
            count=len(independent);bound=r**count
            mask=np.flatnonzero(np.all((a@D)%N==charge,axis=1));assert len(mask)==N
            block=Tf[np.ix_(mask,mask)];ratio=float(np.linalg.eigvalsh(block)[-1]/lam)
            K=kernel(rho);projected=root[:,None]*K*root[None,:]
            direct_ratio=float(np.linalg.eigvalsh(projected)[-1]/lam)
            assert abs(ratio-direct_ratio)<3e-12
            assert np.max(abs(K)-bound*K0.real)<3e-13
            assert ratio<=bound+3e-12 and ratio>0
            energy=float(-np.log(ratio));floor=float(-count*np.log(r));floor6=float(-count*np.log1p(-delta6))
            assert energy>=floor-3e-12 and floor>=floor6-3e-12
            if not len(support):assert abs(ratio-1)<3e-12
            cases.append({'current':current.tolist(),'charge':charge.tolist(),'independent_vertices':independent,
                'transfer_ratio':ratio,'kernel_ratio_bound':bound,'energy':energy,'degree2_floor':floor,'cubic_degree6_floor':floor6})
        harmonic=[]
        for b0,b1 in itertools.product(range(N),repeat=2):
            probability=w[(b0+np.arange(N))%N]*w[(b1-np.arange(N))%N];probability/=probability.sum()
            assert probability.min()>=delta2/N-2e-13
            for q in range(1,N):
                value=abs(np.sum(probability*np.exp(2j*np.pi*q*np.arange(N)/N)))
                assert value<=r+2e-13;harmonic.append(float(value))
        assert abs(np.sum(probability))-r>1e-5
        rows.append({'N':N,'beta':beta,'min_max_weight_ratio':float(w.min()/w.max()),'cases':cases,
            'maximum_nontrivial_conditional_harmonic':max(harmonic),'conditional_harmonic_bound':r,
            'conditional_distributions':N*N,'trivial_harmonic_exceeds_bound':float(1-r)})
    print(json.dumps({'status':'personal_finite_checks_not_independent_review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':rows,'limits':'Finite squares and exact charge projections; cubic degree6 and infinite history passage are analytic statements.'},indent=2))
if __name__=='__main__':main()
