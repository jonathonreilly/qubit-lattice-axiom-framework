#!/usr/bin/env python3
"""Finite algebra challenges to the real-overlap source-support proof."""
from pathlib import Path
import hashlib
import itertools
import json
import numpy as np
import scipy.linalg as la


def words(q,N):
    return [w for n in range(1,N+1) for w in itertools.product(range(q),repeat=n)]


def operator(q,N,u,v,J,a,U):
    ws=words(q,N); index={w:i for i,w in enumerate(ws)}
    H=2*U*np.eye(len(ws),dtype=complex)
    for col,w in enumerate(ws):
        for j in range(len(w)-1):
            if w[j]==w[j+1]: continue
            other=w[:j]+(w[j+1],w[j])+w[j+2:]
            H[col,col]+=J; H[index[other],col]-=J
        if len(w)<N:
            for letter in range(q):
                for other,amp in [((letter,)+w,v[letter]),(w+(letter,),u[letter])]:
                    row=index[other]
                    H[row,col]-=a*amp
                    H[col,row]-=a*np.conj(amp)
    return H,ws


def tensor(factors):
    x=np.ones(1,dtype=complex)
    for f in factors: x=np.kron(x,f)
    return x


def fixture(theta):
    N=5; J=.7; a=np.sqrt(3); U=5.
    u=np.ones(3)/np.sqrt(3)
    v=np.exp(1j*np.array([theta,-theta,0]))/np.sqrt(3)
    c=float(np.vdot(u,v).real); s=np.sqrt(1-c*c)
    assert abs(np.vdot(u,v).imag)<1e-14 and c>=-1e-14
    w=(v-c*u)/s
    H3,ws3=operator(3,N,u,v,J,a,U)
    H2,ws2=operator(2,N,np.array([1.,0]),np.array([c,s]),J,a,U)
    embedding=np.zeros((len(ws3),len(ws2)),dtype=complex)
    offsets={n:sum(3**j for j in range(1,n)) for n in range(1,N+1)}
    for col,word in enumerate(ws2):
        n=len(word); f=tensor([u if x==0 else w for x in word])
        embedding[offsets[n]:offsets[n]+3**n,col]=f
    metric_error=float(np.max(np.abs(embedding.conj().T@embedding-np.eye(len(ws2)))))
    intertwiner_error=float(np.max(np.abs(H3@embedding-embedding@H2)))
    source=np.zeros(len(ws3),dtype=complex);source[:3]=u
    source_error=float(np.max(np.abs(embedding[:,0]-source)))
    assert max(metric_error,intertwiner_error,source_error)<2e-12
    off=H2-np.diag(np.diag(H2))
    assert np.max(np.abs(off.imag))<1e-14 and np.max(off.real)<1e-13
    adjacency=np.abs(off)>1e-12
    seen={0};front=[0]
    while front:
        i=front.pop()
        for j in np.flatnonzero(adjacency[i]):
            j=int(j)
            if j not in seen: seen.add(j);front.append(j)
    assert len(seen)==len(ws2)
    eig,ev=la.eigh(H2)
    assert eig[1]-eig[0]>1e-8 and abs(ev[0,0])**2>1e-10
    alpha=np.arccos(c)
    direct_error=0.
    for n in range(1,8):
        curve=lambda r:np.cos((1-r)*alpha)*u+np.sin((1-r)*alpha)*w
        xi=tensor([curve(j/(n+1)) for j in range(1,n+1)])
        xnext=tensor([curve(j/(n+2)) for j in range(1,n+2)])
        left=np.vdot(xnext,np.kron(v,xi));right=np.vdot(xnext,np.kron(xi,u))
        predicted=np.prod(np.cos(alpha*np.arange(1,n+2)/((n+1)*(n+2))))
        direct_error=max(direct_error,float(abs(left-predicted)),float(abs(right-predicted)))
    assert direct_error<2e-12
    textures=[]
    for size in [16,64,256]:
        ns=np.arange(size,2*size+1)
        coeff=np.sin(np.pi*np.arange(1,size+2)/(size+2));coeff/=la.norm(coeff)
        rings=(ns-1)*np.sin(alpha/(ns+1))**2
        overlaps=np.array([np.prod(np.cos(alpha*np.arange(1,n+2)/((n+1)*(n+2)))) for n in ns[:-1]])
        excess=float(J*np.dot(coeff**2,rings)+4*a*(1-np.dot(coeff[:-1]*coeff[1:],overlaps)))
        bound=float(J*alpha**2/size+4*a*(1-(1-alpha**2/(2*(size+1)))*np.cos(np.pi/(size+2))))
        assert -2e-12<=excess<=bound+2e-12
        textures.append({'N':size,'exact_product_Rayleigh_excess':excess,'analytic_upper_bound':bound})
    return {'theta':theta,'real_overlap':c,'full_dimension':len(ws3),'binary_dimension':len(ws2),
            'embedding_metric_error':metric_error,'full_operator_intertwiner_error':intertwiner_error,
            'source_error':source_error,'connected_binary_vertices':len(seen),
            'finite_lowest_energy':float(eig[0]),'full_infinite_floor':float(2*U-4*a),
            'finite_ground_source_weight':float(abs(ev[0,0])**2),
            'direct_tensor_overlap_error':direct_error,'textures':textures}


def main():
    result={'status':'PASS','scope':'finite algebra; infinite support from written positivity proof',
            'fixtures':[fixture(x) for x in [.4,1.1,2*np.pi/3]],
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out=json.dumps(result,indent=2);Path(__file__).with_suffix('.json').write_text(out+'\n');print(out)


if __name__=='__main__':main()
