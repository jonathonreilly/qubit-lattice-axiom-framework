import numpy as np, time
from fractions import Fraction
from lib import *
from tiles import patch
def is_pd_exact(A):
    """A: list of lists of Fractions (symmetric). Exact LDL^T; True iff positive definite."""
    n=len(A)
    A=[row[:] for row in A]
    for k in range(n):
        p=A[k][k]
        if p<=0: return False
        rowk=A[k]
        for i in range(k+1,n):
            if A[i][k]!=0:
                f=A[i][k]/p
                Ai=A[i]
                for j in range(k+1,n):
                    if rowk[j]!=0:
                        Ai[j]-=f*rowk[j]
                Ai[k]=Fraction(0)
    return True
def tile_cert(shape,ferm,Nlist,Lrat):
    """certify lambda_min(H_tile) >= -Lrat in each sector (N,Nup=N//2): 2H+2L*I PD? (strict => lambda>-L)"""
    n,b=patch(shape)
    ok=True
    for N in Nlist:
        H,_=build_sector(n,b,N,N//2,ferm)
        A=(2*H).toarray()
        assert np.all(np.abs(A-np.round(A))<1e-12)
        d=A.shape[0]
        M=[[Fraction(int(round(A[i,j]))) for j in range(d)] for i in range(d)]
        for i in range(d): M[i][i]+=2*Lrat
        t=time.time()
        r=is_pd_exact(M)
        print(shape,"F" if ferm else "B",N,d,r,round(time.time()-t,1),flush=True)
        ok&=r
    return ok
if __name__=="__main__":
    print(tile_cert((2,2),True,range(1,4),Fraction(1414214,1000000)+Fraction(1,10**6)))
    print(tile_cert((2,2,2),True,range(1,8),Fraction(34641017,10**7)+Fraction(1,10**6)))
