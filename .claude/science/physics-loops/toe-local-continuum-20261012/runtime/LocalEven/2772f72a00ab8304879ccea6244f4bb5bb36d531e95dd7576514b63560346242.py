#!/usr/bin/env python3
"""Literal Pauli Hamiltonians challenge candidate CAR/time/state/locality formulas."""
import argparse, numpy as np
from fixtures import load_candidate, row, finish, complex_pair

def site(P,n,N):
    A=np.ones((1,1),complex)
    for j in range(N):
        A=np.kron(A,P if n==j else np.eye(2))
    return A

def main():
    p=argparse.ArgumentParser(); p.add_argument('candidate'); p.add_argument('output'); args=p.parse_args()
    c=load_candidate(args.candidate)
    X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]],complex); Z=np.diag([1,-1])
    rows=[]; details=[]
    fixtures=[(1,1.7,0.),(5,1.4,.4),(5,*c.couplings(.4,.8,1.3))]
    for N,g,J in fixtures:
        dim=2**N; eye=np.eye(dim)
        xs=[site(X,n,N) for n in range(N)]; zs=[site(Z,n,N) for n in range(N)]
        H=-g*sum(zs)-J*sum((xs[n]@xs[n+1] for n in range(N-1)),np.zeros((dim,dim),complex))
        vals,vecs=np.linalg.eigh(H); omega=vecs[:,0]
        gammas=[c.jw(n,s,N) for n in range(N) for s in (0,1)]
        D=c.open_kernel(N,g,J); P=c.positive(D)
        actual=np.array([[np.vdot(omega,A@B@omega) for B in gammas] for A in gammas])
        prefix=f'N{N}_g{g:.9g}_J{J:.9g}'
        car=max(np.linalg.norm(A@B+B@A-(2*eye if i==j else 0)) for i,A in enumerate(gammas) for j,B in enumerate(gammas))
        rows.append(row(prefix+'_CAR',car,0))
        rows.append(row(prefix+'_ground_covariance',np.linalg.norm(actual-2*P),0))
        derivative=max(np.linalg.norm(1j*(H@A-A@H)-sum((1j*D[i,j]*gammas[i] for i in range(2*N)),np.zeros_like(H))) for j,A in enumerate(gammas))
        rows.append(row(prefix+'_actual_generator',derivative,0))
        t=.2316
        EH=(vecs*np.exp(1j*t*vals))@vecs.conj().T
        U=c.unitary(D,t)
        clock=max(np.linalg.norm(EH@A@EH.conj().T-sum((U[i,j]*gammas[i] for i in range(2*N)),np.zeros_like(H))) for j,A in enumerate(gammas))
        rows.append(row(prefix+'_actual_clock',clock,0))
        fs=[]; operators=[]
        for j,time in enumerate([0.,0.,.23,.23,-.11,-.11]):
            f=np.sin((np.arange(2*N)+1)*(j+1)*.37)+.2*np.cos((np.arange(2*N)+1)*(j+2)*.19)
            f=f/np.linalg.norm(f)
            fs.append(c.unitary(D,time)@f)
            op=sum((f[i]*gammas[i] for i in range(2*N)),np.zeros_like(H))
            V=(vecs*np.exp(1j*time*vals))@vecs.conj().T
            operators.append(V@op@V.conj().T)
        moments=[]
        for degree in [4,6]:
            W=np.zeros((degree,degree),complex)
            for i in range(degree):
                for j in range(i+1,degree):
                    W[i,j]=2*np.vdot(fs[i],P@fs[j]); W[j,i]=-W[i,j]
            product=eye.copy()
            for A in operators[:degree]: product=product@A
            actual_moment=np.vdot(omega,product@omega); predicted=c.pfaffian(W)
            rows.append(row(prefix+f'_Pfaffian_{degree}',abs(actual_moment-predicted),0))
            moments.append({'degree':degree,'actual':complex_pair(actual_moment),'candidate':complex_pair(predicted)})
        details.append({'N':N,'g':float(g),'J':float(J),'ground_energy':float(vals[0]),'finite_gap':float(vals[1]-vals[0]),'XY':complex_pair(actual[0,1]),'moments':moments})
    N=5; eye=np.eye(2**N); support=[]
    words=[[(1,0),(3,1)],[(1,0),(1,1),(2,0),(3,1)],[(2,0)],[(1,0),(2,1),(3,0)]]
    parity=np.eye(2**N)
    for n in range(N): parity=parity@site(Z,n,N)
    for word in words:
        left0=eye.copy(); left1=eye.copy()
        for n,s in word:
            left0=left0@c.jw(n,s,N,left=0); left1=left1@c.jw(n,s,N,left=1)
        residual=np.linalg.norm(left0-left1,ord=2)
        claim=c.claims_endpoint_independence(len(word))
        support.append({'word':word,'degree':len(word),'endpoint_residual':float(residual),'claims_independence':bool(claim)})
        if claim:
            rows.append(row(f'endpoint_degree_{len(word)}',residual,0))
        if len(word)%2==0:
            rows.append(row(f'exterior_degree_{len(word)}',max(np.linalg.norm(left0@site(P,n,N)-site(P,n,N)@left0) for n in [0,4] for P in [X,Y,Z]),0))
            rows.append(row(f'parity_degree_{len(word)}',np.linalg.norm(left0@parity-parity@left0),0))
    finish({'method':'literal Pauli Hamiltonian and ground eigenvectors; finite open chain only','rows':rows,'spin_fixtures':details,'locality_witnesses':support},args.output)

if __name__=='__main__':main()
