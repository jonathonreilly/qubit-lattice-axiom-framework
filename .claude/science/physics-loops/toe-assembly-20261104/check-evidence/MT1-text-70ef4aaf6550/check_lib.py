# Independent check of MT1 Theorems 1,4,5,7,8, Cor 9.1, C3, C7(b,c,d) from the lattice definitions in LW1 section 1.
# Everything is built from R_e,R_o on an even torus; fibre matrices are obtained by Bloch projection, not from the text's formulas.
import numpy as np, itertools, sys
np.set_printoptions(linewidth=200, precision=4, suppress=True)
def torus(L):
    sites=list(itertools.product(range(L),repeat=3)); idx={s:i for i,s in enumerate(sites)}
    return sites,idx
def eta(i,x): return (-1)**(sum(x[:i]))
def hops(L):
    sites,idx=torus(L); n=len(sites)
    Re=np.zeros((n,n)); Ro=np.zeros((n,n)); edges=[]
    for x in sites:
        for i in range(3):
            y=list(x); y[i]=(y[i]+1)%L; y=tuple(y)
            s=eta(i,x)
            M = Re if x[i]%2==0 else Ro
            M[idx[y],idx[x]]+=s; M[idx[x],idx[y]]+=s
            edges.append((x,y,i,s))
    return sites,idx,Re/np.sqrt(3),Ro/np.sqrt(3),edges
def rotations():
    out=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            Q=np.zeros((3,3),int)
            for j in range(3): Q[p[j],j]=s[j]
            if round(np.linalg.det(Q))==1: out.append((Q,p,s))
    return out
def gmap(Q,x,L):
    v=Q@(2*np.array(x)-1)  # 2(x-c0)
    return tuple(((v+1)//2)%L)
def find_lift(Q,L,sites,idx,Re,Ro,improper=False):
    # solve for site signs d: P D commutes with Re and Ro. BFS over edges of Re+Ro
    n=len(sites); P=np.zeros((n,n))
    for x in sites: P[idx[gmap(Q,x,L)],idx[x]]=1
    Ae=P.T@Re@P; Ao=P.T@Ro@P   # need D Ae' ... : (P D) R (P D)^-1 = R  <=> D (P^T R P) D = R... careful
    # (PD) R (PD)^T = R  <=> D R D = P^T R P
    d=np.zeros(n); d[0]=1; stack=[0]; M=Re+2*Ro; T=P.T@M@P
    while stack:
        a=stack.pop()
        for b in np.nonzero(M[a])[0]:
            if abs(T[a,b])<1e-12: return None
            r=T[a,b]/M[a,b]
            if d[b]==0: d[b]=d[a]*r; stack.append(b)
    D=np.diag(d); rho=P@D
    ok=np.allclose(rho@Re@rho.T,Re) and np.allclose(rho@Ro@rho.T,Ro)
    return rho if ok else None
def bloch(L,sites,idx,K):
    # columns |K,r> = sum_b e^{iK.b}|2b+r>, normalised
    nb=(L//2)**3; B=np.zeros((len(sites),8),complex)
    for x in sites:
        b=[c//2 for c in x]; r=[c%2 for c in x]
        B[idx[x], r[0]*4+r[1]*2+r[2]]=np.exp(1j*np.dot(K,b))/np.sqrt(nb)
    return B
def cellmats():
    rs=list(itertools.product([0,1],repeat=3)); ri={r:i for i,r in enumerate(rs)}
    A=[];Z=[]
    for j in range(3):
        a=np.zeros((8,8)); z=np.zeros((8,8))
        for r in rs:
            z[ri[r],ri[r]]=(-1)**r[j]
            if r[j]==0:
                r2=list(r); r2[j]=1; r2=tuple(r2); s=(-1)**sum(r[:j])
                a[ri[r2],ri[r]]=s; a[ri[r],ri[r2]]=s
        A.append(a); Z.append(z)
    G=[1j*Z[j]@A[j] for j in range(3)]
    return A,Z,G
def acomm(a,b): return a@b+b@a
def prop(a,b):
    # is a = c*b with |c|=1 ?
    k=np.argmax(abs(b)); c=a.flat[k]/b.flat[k]
    return np.allclose(a,c*b) and abs(abs(c)-1)<1e-9, c
