"""New finite graded controls; no author or earlier model builder imported."""
import sympy as sp
import numpy as np

def exact_blocks():
    # Basis: N=0: P0,P1,Q0,Q1,R; N=2: P2,P3,Q2; N=4: P4.
    W=sp.diag(0,0,1,1,2,0,0,1,0)
    N=sp.diag(0,0,0,0,0,2,2,2,4)
    T=sp.zeros(9);C=sp.zeros(9)
    for row,col,value in [(2,0,1),(2,1,1),(3,1,2),(4,2,1),(4,3,-1),(7,5,1),(7,6,-2)]:
        T[row,col]=value;T[col,row]=value
    for ix,block in [([0,1],sp.Matrix([[1,2],[2,-1]])),
                     ([2,3],sp.Matrix([[3,1],[1,-2]])),
                     ([5,6],sp.Matrix([[2,1],[1,0]]))]:
        for i,x in enumerate(ix):
            for j,y in enumerate(ix):C[x,y]=block[i,j]
    C[4,4]=4;C[7,7]=-1;C[8,8]=sp.Rational(1,3)
    j1,j2=sp.zeros(9),sp.zeros(9)
    for row,col,value in [(5,2,1),(6,3,2),(7,4,1),(8,7,1)]:j1[row,col]=value
    for row,col,value in [(6,2,1),(5,3,1),(7,4,-sp.Rational(1,2)),(8,7,sp.Rational(1,2))]:j2[row,col]=value
    return W,N,T,C,[j1,j2]

def numpy_matrix(M):return np.array(M.tolist(),dtype=complex)

def ingredients(W,T,C,jumps):
    ix=[i for i in range(W.rows) if W[i,i]==0]
    qx=[i for i in range(W.rows) if W[i,i]!=0]
    r1=[i for i in range(W.rows) if W[i,i]==1]
    r2=[i for i in range(W.rows) if W[i,i]==2]
    A=T.extract(r1,ix);Z=T.extract(r2,r1)*A;M=A.H*A
    C0=C.extract(ix,ix);C1=C.extract(r1,r1)
    K2=C0-M
    K4=M*M-sp.Rational(1,2)*Z.H*Z+A.H*C1*A-(M*C0+C0*M)/2
    B=[-j.extract(ix,r1)*A for j in jumps]
    return ix,qx,A,Z,M,C0,C1,K2,K4,B

def canonical_rotation(W,T,C,eps):
    h=W+eps*T+eps*eps*C;w=np.real(np.diag(W)).astype(int)
    values,vectors=np.linalg.eigh(h)
    labels=np.rint(values).astype(int);S=np.zeros_like(h)
    for r in sorted(set(w)):
        cols=np.flatnonzero(w==r);eig=np.flatnonzero(labels==r)
        assert len(cols)==len(eig)
        Q=vectors[:,eig]@vectors[:,eig].conj().T
        S[:,cols]=Q[:,cols]
    G=S.conj().T@S;g,V=np.linalg.eigh(G);assert min(g)>.5
    U=S@((V*(g**(-.5)))@V.conj().T)
    return U,U.conj().T@h@U
