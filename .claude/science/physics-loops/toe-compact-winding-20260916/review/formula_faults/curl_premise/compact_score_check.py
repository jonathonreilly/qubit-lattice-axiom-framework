#!/usr/bin/env python3
"""Finite compact score challenges, not a photon or thermodynamic proof.

The torus test is a Fourier-cutoff zero-harmonic electric sector of an actual
2x2 plaquette complex. The independent-rotor limit is a gapped comparator.
"""
AUDIT_TIMEOUT_SEC=120
from itertools import product
from pathlib import Path
import hashlib,json,math,time
import numpy as np
from scipy.linalg import eigh,eigvalsh
from scipy.special import logsumexp


def torus_curl():
    vertices=list(product(range(2),repeat=2))
    edges=[(x,y,mu) for x,y in vertices for mu in range(2)]
    index={e:i for i,e in enumerate(edges)};C=np.zeros((4,8),dtype=int)
    for row,(x,y) in enumerate(vertices):
        for e,s in [((x,y,0),1),(((x+1)%2,y,1),1),
                    ((x,(y+1)%2,0),-1),((x,y,1),-1)]:C[row,index[e]]+=s
    assert np.array_equal(C.sum(axis=0),np.zeros(8,dtype=int))
    assert np.linalg.matrix_rank(C)==3
    return C


def model(g,N):
    C=torus_curl();G=C[:3]@C[:3].T
    sites=list(product(range(-N,N+1),repeat=3));lookup={s:i for i,s in enumerate(sites)}
    n=np.asarray(sites);kinetic=g*g/2*np.einsum('bi,ij,bj->b',n,G,n)
    shifts=np.vstack((np.eye(3,dtype=int),-np.ones(3,dtype=int)))
    cosine=[];sine=[]
    for v in shifts:
        A=np.zeros((len(sites),len(sites)))
        for col,x in enumerate(n):
            row=lookup.get(tuple(x+v))
            if row is not None:A[row,col]=1
        cosine.append((A+A.T)/2);sine.append((A-A.T)/(2j))
    D=np.diag(kinetic+4/g**2)
    return C,n,D,cosine,sine


def logtrace(H,beta):return float(logsumexp(-beta*eigvalsh(H)))


def thermal_ward(H,M,contact,beta):
    E,V=eigh(H);weights=np.exp(-beta*E-logsumexp(-beta*E))
    A=V.conj().T@M@V
    gap=E[None,:]-E[:,None]
    numerator=weights[:,None]-weights[None,:]
    mask=abs(gap)>1e-10
    divided=np.empty_like(gap)
    divided[mask]=numerator[mask]/gap[mask]
    midpoint=(weights[:,None]+weights[None,:])/2
    divided[~mask]=beta*midpoint[~mask]
    mean=float(np.sum(weights*np.diag(A)).real)
    variance=float(beta*np.sum(abs(A)**2*divided)-(beta*mean)**2)
    expectation=float(np.sum(weights*np.diag(V.conj().T@contact@V)).real)
    return variance,beta*expectation


def torus_checks():
    records=[]
    for g,beta in ((.8,.4),(1.25,.7)):
        refinements=[]
        for N in (3,4):
            C,n,D,cosine,sine=model(g,N);H=D-sum(cosine)/g**2
            z0=logtrace(H,beta);cases=[]
            for label,h in [('exact',np.array([1.,-.4,.2,-.7])),
                            ('nonexact',np.array([1.,.3,-.1,.2]))]:
                M=sum(a*S for a,S in zip(h,sine))/g
                contact=sum(a*a*A for a,A in zip(h,cosine))
                var,w=thermal_ward(H,M,contact,beta)
                assert var<=beta*np.dot(h,h)+2e-10
                if label=='exact':assert abs(var-w)<2e-10
                else:assert w-var>1e-7
                tests=[]
                for t in (-.8,.45,1.1):
                    R=np.sqrt(1+g*g*t*t*h*h);phi=np.arctan(g*t*h)
                    amplitude_phase=D.astype(complex)
                    amplitude_only=D.copy()
                    for a,b,A,S in zip(R,phi,cosine,sine):
                        amplitude_phase-=a*(math.cos(b)*A+math.sin(b)*S)/g**2
                        amplitude_only-=a*A/g**2
                    matrix_error=float(np.max(abs(amplitude_phase-(H-t*M))))
                    assert matrix_error<2e-12
                    actual=logtrace(H-t*M,beta)-z0
                    unphased=logtrace(amplitude_only,beta)-z0
                    amplitude_bound=beta*np.sum(R-1)/g**2
                    gaussian_bound=t*t*beta*np.dot(h,h)/2
                    assert actual<=unphased+2e-11
                    assert unphased<=amplitude_bound+2e-11
                    assert amplitude_bound<=gaussian_bound+2e-11
                    rec=dict(t=t,log_mgf=actual,unphased_log_ratio=unphased,
                             amplitude_bound=float(amplitude_bound),gaussian_bound=float(gaussian_bound),
                             matrix_error=matrix_error)
                    if label=='exact':
                        # Exact shifted background and independently assembled unitary.
                        shifted=D.astype(complex)
                        for a,A,S in zip(h,cosine,sine):
                            shifted-=(math.cos(g*t*a)*A-math.sin(g*t*a)*S)/g**2
                        phase=np.exp(1j*g*t*(n@h[:3]))
                        unitary=phase[:,None]*H*phase.conj()[None,:]
                        assert np.max(abs(unitary-shifted))<2e-12
                        assert abs(logtrace(shifted,beta)-z0)<2e-11
                        truncated=H+t*M+t*t*contact/2
                        remainder=float(np.linalg.norm(shifted-truncated,2))
                        delta=g*abs(t)**3*beta*np.sum(abs(h)**3)/6
                        ratio=logtrace(truncated,beta)-z0
                        assert beta*remainder<=delta+2e-11
                        assert abs(ratio)<=delta+2e-11
                        rec.update(ward_taylor_log_ratio=ratio,remainder_norm=remainder,delta=float(delta))
                    tests.append(rec)
                cases.append(dict(kind=label,h=h.tolist(),variance=var,ward_contact=w,tests=tests))
            refinements.append(dict(N=N,dimension=len(n),log_partition=z0,cases=cases))
        # A coarse/fine comparison is recorded, not called a rigorous tail bound.
        delta=max(abs(refinements[0]['cases'][i]['tests'][j]['log_mgf']-
                      refinements[1]['cases'][i]['tests'][j]['log_mgf']) for i in range(2) for j in range(3))
        assert delta<.003
        records.append(dict(g=g,beta=beta,cutoffs=refinements,maximum_refinement_change=delta))
    return records


def independent_rotors():
    results=[]
    for g,beta,N in ((.5,.8,18),(1.1,.5,14)):
        n=np.arange(-N,N+1);A=np.diag(np.ones(2*N),k=1)
        C=(A+A.T)/2;S=(A-A.T)/(2j)
        D=np.diag(2*g*g*n*n+1/g**2);H=D-C/g**2
        E,V=eigh(H);p=np.exp(-beta*E-logsumexp(-beta*E))
        contact=beta*float(np.sum(p*np.diag(V.T@C@V)))
        gap=float(E[1]-E[0]);assert gap>0
        z0=logtrace(H,beta);rows=[]
        for copies in (1,16,256,4096):
            t=.9;source=t/math.sqrt(copies)
            direct=copies*(logtrace(H-source*S/g,beta)-z0)
            R=math.sqrt(1+g*g*source*source)
            amplitude=copies*(logtrace(D-R*C/g**2,beta)-z0)
            assert abs(direct-amplitude)<2e-8
            target=t*t*contact/2
            rows.append(dict(copies=copies,log_mgf=direct,amplitude_log_mgf=amplitude,
                             gaussian_target=target,error=abs(direct-target)))
        assert rows[-1]['error']<2e-5
        assert rows[-1]['error']<rows[0]['error']/100
        results.append(dict(g=g,beta=beta,cutoff=N,single_rotor_gap=gap,variance=contact,rows=rows))
    return results


def main():
    start=time.monotonic()
    out=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope=__doc__,torus=torus_checks(),gapped_comparator=independent_rotors(),
             status='PERSONAL_CHECKS_COMPLETED')
    out['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
