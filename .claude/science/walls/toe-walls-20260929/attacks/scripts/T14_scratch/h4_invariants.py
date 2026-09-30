"""Count invariants of 2-index tensors c_{mu nu} (spinor kinetic coefficient psibar gamma_mu d_nu psi; also scalar-kinetic sym form)
under: cubic O_h x time (48, time fixed), hypercubic B4 (384), proper hypercubic B4+ (192), and the proper cubic O (24) x time."""
import itertools, numpy as np
def group(n, proper_only=False, time_fixed=False):
    G=[]
    axes=range(n)
    for p in itertools.permutations(axes):
        if time_fixed and p[0]!=0: continue
        for signs in itertools.product([1,-1],repeat=n):
            if time_fixed and signs[0]!=1: continue
            M=np.zeros((n,n)); 
            for i,(pi,s) in enumerate(zip(p,signs)): M[pi,i]=s
            if proper_only and round(np.linalg.det(M))!=1: continue
            G.append(M)
    return G
def inv_dim(G, rep):
    # dimension of invariant subspace of the rep given by function rep(M)->matrix
    P=sum(rep(M) for M in G)/len(G)
    return round(np.trace(P))
rep2=lambda M: np.kron(M,M)                       # c_{mu nu} -> M c M^T (all 16)
def repsym(M):                                     # symmetric 10
    n=4; idx=[(i,j) for i in range(n) for j in range(i,n)]
    R=np.zeros((10,10))
    for a,(i,j) in enumerate(idx):
        for b,(k,l) in enumerate(idx):
            R[b,a]=0
    # build via projector on 16
    Pm=np.zeros((16,16))
    for i in range(n):
        for j in range(n):
            Pm[i*n+j,i*n+j]+=0.5; Pm[i*n+j,j*n+i]+=0.5
    return Pm@np.kron(M,M)@Pm
res={}
for name,G in [("O_h x time (48; spatial cubic, time fixed)",group(4,False,True)),
               ("proper O x time (24)",[M for M in group(4,False,True) if round(np.linalg.det(M[1:,1:]))==1]),
               ("B4 hypercubic (384)",group(4)),
               ("B4+ proper hypercubic (192)",group(4,True))]:
    print(f"{name:48s} |G|={len(G):4d}  invariant c_(mu nu), all 16: {inv_dim(G,rep2)}   symmetric 10: {inv_dim(G,repsym)}")
