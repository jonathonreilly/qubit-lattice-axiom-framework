#!/usr/bin/env python3
"""Finite matched-phase paths for an explicit candidate connection, no data."""
from pathlib import Path
import hashlib,json,math
import numpy as np

pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
I=np.eye(2,dtype=complex)
def axis(a):return np.einsum('i,ijk->jk',a,pauli)
def step(a,b,n,kappa):
    assert np.dot(a,b)>-1+1e-10
    A=axis(a);B=axis(b);theta=kappa*np.dot(n,np.cross(a,b))
    return (I+B@A)/np.sqrt(2*(1+np.dot(a,b)))@(np.cos(theta/2)*I-1j*np.sin(theta/2)*A)
def latitude(beta,N):
    return [np.array([np.sin(beta)*np.cos(2*np.pi*j/N),np.sin(beta)*np.sin(2*np.pi*j/N),np.cos(beta)]) for j in range(N)]
def based_loop(beta,N,rotation):
    points=[rotation@x for x in latitude(beta,N)];z=np.array([0.,0.,1.])
    return [z]+points+[points[0],z]
def transport(path,n,kappa):
    U=I.copy();W=np.zeros(3)
    for a,b in zip(path,path[1:]):U=step(a,b,n,kappa)@U;W+=np.cross(a,b)
    return U,W
def gamma(beta,N):return -np.pi+N*np.arctan(np.cos(beta)*np.tan(np.pi/N))

def main():
    checks=[]
    def ck(name,value,**kw):
        assert bool(value),name
        checks.append(dict(name=name,passed=True,**kw))
    rotate=np.diag([1.,-1.,-1.]);n=np.array([.2,-.3,.7]);k=.37;rows=[]
    for N in [3,4,8,16,32,64]:
        for betaA in [.2,.7,np.pi/3,1.4]:
            ga=gamma(betaA,N);betaB=np.arccos(np.tan((np.pi+ga/2)/N)/np.tan(np.pi/N))
            assert 0<betaB<betaA,'half-phase domain'
            A=based_loop(betaA,N,np.eye(3));B1=based_loop(betaB,N,np.eye(3));B2=based_loop(betaB,N,rotate);B=B1+B2[1:]
            ua,wa=transport(A,n,0);ub,wb=transport(B,n,0);va,_=transport(A,n,k);vb,_=transport(B,n,k)
            W=N*np.sin(betaA)**2*np.sin(2*np.pi/N)
            assert np.linalg.norm(ua-ub)<2e-12,'equal reference matrices'
            assert abs(ua[0,0]-np.exp(1j*ga))<2e-12,'finite reference phase'
            assert np.linalg.norm(wa-np.array([0,0,W]))<2e-12 and np.linalg.norm(wb)<2e-12,'context vector sum'
            assert abs(va[0,0]/vb[0,0]-np.exp(-1j*k*n[2]*W/2))<2e-12,'context phase discriminator'
            assert np.linalg.norm(vb-ub)<2e-12,'context echo cancellation'
            rows.append(dict(N=N,betaA=betaA,betaB=float(betaB),reference_phase=float(ga),W=float(W)))
    ck('finite matched-phase matrices and contextual discriminator',len(rows)==24,cases=rows)
    # The entire construction can be rotated; compare full matrices to SO(3)
    # transport, and the accumulated extra phase along the rotated anchor.
    beta=np.pi/3;N=16;ga=gamma(beta,N);bb=np.arccos(np.tan((np.pi+ga/2)/N)/np.tan(np.pi/N));z=np.array([0.,0.,1.]);baseA=based_loop(beta,N,np.eye(3));baseB=based_loop(bb,N,np.eye(3))+based_loop(bb,N,rotate)[1:];W=N*np.sin(beta)**2*np.sin(2*np.pi/N)
    axes=[np.eye(3),np.array([[0,0,1],[1,0,0],[0,1,0]],float),np.array([[0,1,0],[0,0,1],[1,0,0]],float)]
    for R in axes:
        a=[R@x for x in baseA];b=[R@x for x in baseB];u,_=transport(a,n,k);v,_=transport(b,n,k);anchor=R@z
        relative=u@v.conj().T;theta=k*np.dot(n,anchor)*W
        expected=np.cos(theta/2)*I-1j*np.sin(theta/2)*axis(anchor)
        assert np.linalg.norm(relative-expected)<2e-12,'rotated full relative transform'
    ck('three orthogonal context components',True,axes=3)
    eps=np.abs(k*n)*W/2
    ck('unwrapped component bound is attained',abs(2*np.linalg.norm(eps/W)-np.linalg.norm(k*n))<1e-14)
    alias_k=4*np.pi/W
    ck('modulo phase alias requires unwrapping',abs(np.exp(-1j*alias_k*W/2)-1)<1e-14 and alias_k>0)
    # Exact symmetry integral reduced to one-dimensional quadrature, not MC.
    from scipy.integrate import quad
    for kval in [.0,.2,1.,3.]:
        value=quad(lambda mu:math.cos(kval*W*mu/2),-1,1,epsabs=1e-12)[0]/2
        expected=np.sinc(kval*W/(2*np.pi))
        assert abs(value-expected)<1e-12,'isotropic ensemble visibility'
    ck('conditional isotropic ensemble visibility',True,cases=4)
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK12_v1.md')
    print(json.dumps({'summary':{'passed':len(checks),'failed':0},'checks':checks,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'empirical_validation':False,'scope':'Explicit supplied contextual connection and ideal controlled paths; no derived coupling, state or physical identification.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
