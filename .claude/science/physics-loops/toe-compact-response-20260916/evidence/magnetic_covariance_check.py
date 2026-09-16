#!/usr/bin/env python3
"""Independent matrix/Fourier covariance, rate-replication and majorant checks.

All matrices are finite test objects. The static response calculation challenges
the transport majorant but is not a stochastic bridge or phase simulation.
"""
AUDIT_TIMEOUT_SEC=120
from itertools import product,combinations
from pathlib import Path
import hashlib,json,math,time
import numpy as np
from scipy.linalg import eigh,solve


def incidence(L):
    vertices=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(vertices)}
    faces=list(combinations(range(3),2));N=L**3
    C=np.zeros((3*N,3*N))
    for x in vertices:
        for face,(i,j) in enumerate(faces):
            row=3*index[x]+face
            xi=list(x);xi[i]=(xi[i]+1)%L
            xj=list(x);xj[j]=(xj[j]+1)%L
            C[row,3*index[tuple(xi)]+j]+=1
            C[row,3*index[x]+j]-=1
            C[row,3*index[tuple(xj)]+i]-=1
            C[row,3*index[x]+i]+=1
    assert np.max(np.abs(C).sum(axis=0))==4
    assert np.max(np.abs(C).sum(axis=1))==4
    return C


def difference(n):
    D=-np.eye(n)
    for i in range(n):D[i,(i+1)%n]+=1
    return D


def psd_inverse(A):
    val,vec=eigh(A)
    assert val.min()>-1e-9
    keep=val>1e-9
    return (vec[:,keep]/val[keep])@vec[:,keep].T,dict(nullity=int((~keep).sum()),
            minimum_positive=float(val[keep].min()),maximum=float(val.max()))


def fourier_apply(h,L,M,T,wrong=False):
    H=np.fft.fftn(h.reshape(M,L,L,L,3),axes=(0,1,2,3),norm='ortho')
    out=np.zeros_like(H);maximum=0.
    for nt,nx,ny,nz in product(range(M),range(L),range(L),range(L)):
        theta=2*np.pi*nt/M;k=2*np.pi*np.array([nx,ny,nz])/L
        delta=np.exp(1j*k)-1
        C=np.array([[-delta[1],delta[0],0],[-delta[2],0,delta[0]],
                    [0,-delta[2],delta[1]]])
        ls=float(np.sum(abs(delta)**2));lt=4*np.sin(theta/2)**2/(T*T)
        b=1. if wrong else (2+np.cos(theta))/3
        K=C@C.conj().T/(lt+b*ls) if ls else np.zeros((3,3))
        if ls:
            q0=ls/(lt+ls);A=T*T/6*ls*lt/(lt+ls)
            if not wrong:assert np.max(abs(K-C@C.conj().T/ls*q0/(1-A)))<2e-13
        maximum=max(maximum,float(np.linalg.eigvalsh(K).max()))
        out[nt,nx,ny,nz]=K@H[nt,nx,ny,nz]
    real=np.fft.ifftn(out,axes=(0,1,2,3),norm='ortho')
    assert np.max(abs(real.imag))<2e-12
    return real.real.reshape(-1),maximum


def covariance_checks():
    rng=np.random.default_rng(160916);L=4;C=incidence(L);P=C.shape[0];rows=[]
    for M,T in ((3,.2),(4,.1)):
        Dt=difference(M)/T
        G=(2/3)*np.eye(M)+(np.roll(np.eye(M),1,axis=0)+np.roll(np.eye(M),-1,axis=0))/6
        A=np.kron(Dt.T@Dt,np.eye(P))+np.kron(G,C.T@C)
        inverse,spectrum=psd_inverse(A)
        fullC=np.kron(np.eye(M),C)
        K=fullC@inverse@fullC.T
        maxerr=0.;wrongerr=0.;variances=[]
        for _ in range(3):
            h=rng.normal(size=M*P)
            direct=K@h;fourier,kmax=fourier_apply(h,L,M,T)
            wrong,_=fourier_apply(h,L,M,T,True)
            maxerr=max(maxerr,float(np.max(abs(direct-fourier))))
            wrongerr=max(wrongerr,float(np.max(abs(direct-wrong))))
            assert maxerr<2e-10 and kmax<=1+1e-12
            variances.append(float(h@direct))
        assert wrongerr>1e-4
        rows.append(dict(L=L,M=M,T=T,matrix_dimension=len(A),spectrum=spectrum,
                         maximum_matrix_Fourier_error=maxerr,
                         wrong_one_slice_error=wrongerr,test_variances=variances))
    return rows


def product_laplacians(sizes):
    total=math.prod(sizes);out=[]
    for axis,n in enumerate(sizes):
        D=difference(n);A=D.T@D
        out.append(np.kron(np.kron(np.eye(math.prod(sizes[:axis])),A),
                           np.eye(math.prod(sizes[axis+1:]))))
    return out


def replication_checks():
    rows=[]
    base_ops=product_laplacians((3,4))
    for m,n in ((2,1),(1,2),(3,2)):
        sizes=[3]*m+[4]*n;ops=product_laplacians(sizes)
        phi=np.zeros((math.prod(sizes),12))
        for row,x in enumerate(product(*[range(s) for s in sizes])):
            phi[row,4*(sum(x[:m])%3)+sum(x[m:])%4]=1
        big=sum(ops);small=m*base_ops[0]+n*base_ops[1]
        numerator=sum(ops[m:]);smallnumerator=n*base_ops[1]
        assert np.max(abs(big@phi-phi@small))<1e-13
        assert np.max(abs(numerator@phi-phi@smallnumerator))<1e-13
        biginverse,_=psd_inverse(big);smallinverse,_=psd_inverse(small)
        residual=float(np.max(abs(numerator@biginverse@phi-phi@smallnumerator@smallinverse)))
        assert residual<3e-12
        # The pullback preserves normalized lp norms, not raw counting norms.
        f=np.arange(12,dtype=float)-5.5
        for p in (1.5,2.,3.):
            assert abs(np.mean(abs(phi@f)**p)-np.mean(abs(f)**p))<1e-12
        rows.append(dict(temporal_copies=m,spatial_copies=n,T=math.sqrt(n/m),
                         larger_dimension=math.prod(sizes),ratio_residual=residual))
    return rows


def positive_majorant_checks():
    rng=np.random.default_rng(1931);L=4;m=3;T=.2;delta=T/m
    C=incidence(L);B=abs(C);P=len(C)
    Dt=(2*np.eye(m-1)-np.eye(m-1,k=1)-np.eye(m-1,k=-1))/(delta*delta)
    D=np.kron(Dt,np.eye(P));CC=np.kron(np.eye(m-1),C)
    G=np.linalg.inv(Dt);major=np.kron(G,B@B.T)
    r=2*T*T;W=np.linalg.inv(np.eye(len(major))-major)
    assert major.min()>=0 and W.min()>-1e-14
    row=float(major.sum(axis=1).max());col=float(major.sum(axis=0).max())
    assert row<=r+1e-13 and col<=r+1e-13
    assert W.sum(axis=1).max()<=1/(1-r)+1e-12
    f=rng.uniform(-np.pi,np.pi,len(major))
    precision=D+CC.T@(np.cos(f)[:,None]*CC)
    h=rng.normal(size=len(f));k=rng.normal(size=len(f));l=rng.normal(size=len(f))
    # Include sharply concentrated physical-time/spatial variations.
    h[len(h)//2:]=0;k[::2]=0;l[:len(l)//2]=0
    responses=[];envelopes=[]
    for z in (h,k,l):
        S=solve(precision,-CC.T@(np.cos(f)*z),assume_a='pos')
        U=z+CC@S;envelope=W@abs(z)
        assert np.max(abs(U)-envelope)<1e-12
        assert np.max(abs(CC@S)-W@major@abs(z))<1e-12
        responses.append(U);envelopes.append(envelope)
    uh,uk,ul=responses
    second=solve(precision,CC.T@(np.sin(f)*uk*ul),assume_a='pos')
    second_envelope=W@major@(envelopes[1]*envelopes[2])
    assert np.max(abs(CC@second)-second_envelope)<1e-12
    cubic=delta*np.dot(h,-np.sin(f)*uk*ul+np.cos(f)*(CC@second))
    norms=[(delta*np.sum(abs(z)**3))**(1/3) for z in (h,k,l)]
    bound=math.prod(norms)/(1-r)**3
    assert abs(cubic)<=bound+1e-10
    return dict(L=L,physical_grid=m,T=T,row_sum=row,column_sum=col,row_upper=r,
                static_cubic=float(cubic),space_time_cubic_bound=bound,
                input_l3_norms=norms,scope='Static coefficient response; not the tilted stochastic bridge.')


def main():
    start=time.monotonic()
    out=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope=__doc__,
             covariance=covariance_checks(),replication=replication_checks(),
             majorant=positive_majorant_checks(),status='PERSONAL_CHECKS_COMPLETED')
    out['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
