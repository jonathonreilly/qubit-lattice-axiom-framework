import sys, itertools, numpy as np
import os; sys.argv=['x',os.environ.get('LL','4')]
import corner_psg as C
# 2O
def q2su(q):
    a,b,c,d=q; return np.array([[a+1j*b,c+1j*d],[-c+1j*d,a-1j*b]])
qs=[]
for i in range(4):
    for s in (1,-1):
        v=[0]*4; v[i]=s; qs.append(v)
for sg in itertools.product((1,-1),repeat=4): qs.append([x/2 for x in sg])
r=1/np.sqrt(2)
for i,j in itertools.combinations(range(4),2):
    for si,sj in itertools.product((1,-1),repeat=2):
        v=[0]*4; v[i],v[j]=si*r,sj*r; qs.append(v)
G2=[q2su(q) for q in qs]
P=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
def so3(U): return np.rint(np.array([[0.5*np.real(np.trace(P[i]@U@P[j]@U.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
def rid(R): return [k for k,S in enumerate(C.ROTS) if (S==R).all()][0]
proj=[rid(so3(U)) for U in G2]
def w1(R):
    p=[C.DIRS.index(C.rot_dir(R,d)) for d in C.DIRS]
    s=1; p=list(p)
    for i in range(6):
        while p[i]!=i:
            j=p[i]; p[i],p[j]=p[j],p[i]; s=-s
    return 0 if s==1 else 1
W1=[w1(R) for R in C.ROTS]

def run(F, twist=True, verbose=True):
    out,u,Ms=C.classify(F)
    loc=[C.VID[((0,0,0),c)] for c in C.CORNERS]
    li={g:i for i,g in enumerate(loc)}
    def Mloc(k):
        Pm,s=Ms[k]; M=np.zeros((12,12),complex)
        for i,g in enumerate(loc):
            M[li[Pm[g]],i]=(-1.0)**s[g]
        return M*(1j**W1[k] if twist else 1)
    Ml=[Mloc(k) for k in range(24)]
    # find homomorphism lift: for each 2O element g with image R choose sign so that it's a rep
    # brute: choose sign for one lift per R via GF(2) solve on consistency
    sec=[proj.index(k) for k in range(24)]
    def gidx(U):
        for k,V in enumerate(G2):
            if np.allclose(U,V): return k
    rows=[];rhs=[]
    for a in range(24):
        for b in range(24):
            prod=G2[sec[a]]@G2[sec[b]]; ab=proj[gidx(prod)]
            w=0 if np.allclose(prod,G2[sec[ab]]) else 1
            X=Ml[a]@Ml[b]; Y=Ml[ab]
            if np.allclose(X,Y): e=0
            elif np.allclose(X,-Y): e=1
            else: return None
            rows.append([a,b,ab]); rhs.append(e^w)
    # solve beta(a)+beta(b)+beta(ab)=rhs (mod 2) with repeated indices handled
    rows2=[]
    for rr in rows:
        cnt={}
        for x in rr: cnt[x]=cnt.get(x,0)^1
        rows2.append([x for x,v in cnt.items() if v])
    beta=C.gf2_solve(rows2,rhs,24)
    if beta is None:
        if verbose: print("   no lift to 2O: class is not w2 (twist=%s)"%twist)
        return None
    sg=[((-1.0)**int(beta[proj[k]]))*(1 if np.allclose(G2[k],G2[sec[proj[k]]]) else -1) for k in range(48)]
    Mt=[sg[k]*Ml[proj[k]] for k in range(48)]
    # verify homomorphism
    for a in range(48):
        for b in range(48):
            ab=gidx(G2[a]@G2[b])
            assert np.allclose(Mt[a]@Mt[b],Mt[ab])
    return Mt, loc, u
