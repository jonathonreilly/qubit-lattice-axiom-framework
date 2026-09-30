"""Solution-space analysis: which continuum-limit invariants of G2 does the identity force?"""
import sys
import numpy as np
from solve import *
R=int(sys.argv[1])
res,(cols,rows,entries,b,A,bb)=analyse(R,'full',exact=False,verbose=False)
labels=[lab for lab,_ in cols]
n=len(labels)
# particular solution and nullspace via SVD
U,S,Vt=np.linalg.svd(A,full_matrices=True)
tol=1e-9*S[0]
rank=int((S>tol).sum())
x0=np.linalg.lstsq(A,bb,rcond=None)[0]
N=Vt[rank:].T   # nullspace basis (n x (n-rank))
print("R",R,"unknowns",n,"rank",rank,"null dim",N.shape[1],"resid",np.linalg.norm(A@x0-bb))
# moment functionals on G2 coefficients per (c,d)
names={0:'xx',1:'yy',2:'zz'}
def funcs(c,d):
    S0=np.zeros(n);Ia=np.zeros(n);Ib=np.zeros(n);Ic=np.zeros(n)
    for j,lab in enumerate(labels):
        if lab[0]=='G2':
            cc,dd,i,jj=lab[1]
            if (cc,dd)==(c,d):
                # NOTE: column was scaled by -1 in build(); coefficient g = -x
                S0[j]=-1; Ia[j]=-0.5; Ib[j]=-i; Ic[j]=-jj
    return S0,Ia,Ib,Ic
def rep(name,f):
    v0=f@x0
    spread=np.linalg.norm(f@N) if N.shape[1] else 0.0
    return v0,spread
print("pair(P,h)   S0 [val,free]    a-b [val,free]    c-b [val,free]")
for c in (0,1,2):
    for d in (0,1,2):
        S0,Ia,Ib,Ic=funcs(c,d)
        s0=rep('S0',S0); ab=rep('ab',Ia-Ib); cb=rep('cb',Ic-Ib)
        print(names[c]+","+names[d], "  %.3f %.2e   %.3f %.2e   %.3f %.2e"%(s0[0],s0[1],ab[0],ab[1],cb[0],cb[1]))
