import itertools, numpy as np
from diraclib import *
exec(open('dirac5.py').read().split("res={}")[0].replace("from diraclib import *","").replace("import itertools",""))
# 2O elements and projection to O
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
Pm=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
def so3(U): return np.rint(np.array([[0.5*np.real(np.trace(Pm[i]@U@Pm[j]@U.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
def rid(R): return [k for k,S in enumerate(C.ROTS) if (S==R).all()][0]
proj=[rid(so3(U)) for U in G2]
def gidx(U):
    for k,V in enumerate(G2):
        if np.allclose(U,V): return k
def mat(k): P,s=rots[k]; M=np.zeros((nV,nV)); M[P,np.arange(nV)]=(-1.0)**s; return M
Mf=[mat(k)*(1j**W1[k]) for k in range(24)]
# restrict to a subspace basis Vs (columns) invariant under the group; find lift signs making a rep of 2O (or 2T)
def chars(Vs, elems):
    Rm={k: Vs.conj().T@Mf[k]@Vs for k in set(proj[e] for e in elems)}
    sec={}
    for e in elems:
        R=proj[e]
        if R not in sec: sec[R]=e
    # sign eps(e) = +1 for section element; solve beta on R for homomorphism
    Rs=sorted(sec); idx={R:i for i,R in enumerate(Rs)}
    rows=[];rhs=[]
    for a in Rs:
        for b in Rs:
            prod=G2[sec[a]]@G2[sec[b]]; g=gidx(prod); ab=proj[g]
            w=0 if g==sec[ab] else 1
            X=Rm[a]@Rm[b]; Y=Rm[ab]
            e=0 if np.allclose(X,Y) else (1 if np.allclose(X,-Y) else None)
            if e is None: return None
            cnt={}
            for x in (idx[a],idx[b],idx[ab]): cnt[x]=cnt.get(x,0)^1
            rows.append([x for x,v in cnt.items() if v]); rhs.append(e^w)
    beta=C.gf2_solve(rows,rhs,len(Rs))
    if beta is None: return None
    out={}
    for e in elems:
        R=proj[e]; sg=((-1.0)**int(beta[idx[R]]))*(1 if e==sec[R] else -1)
        out[e]=sg*np.trace(Rm[R])
    return out
def spin_char(j2,U):
    tr=max(-1,min(1,np.real(np.trace(U))/2)); th=2*np.arccos(tr)
    if abs(np.sin(th/2))<1e-12: return float(j2+1)*(1 if np.isclose(tr,1) else (-1)**j2)
    return np.sin((j2+1)*th/2)/np.sin(th/2)
allO=list(range(48)); Tel=[e for e in allO if W1[proj[e]]==0]
def dec(ch, elems):
    out={}
    for name,j2 in (('spin1/2',1),('spin3/2',3),('spin5/2',5)):
        out[name]=round(np.real(sum(np.conj(spin_char(j2,G2[e]))*ch[e] for e in elems))/len(elems),3)
    return out
A=np.random.default_rng(42).normal(size=(12,12)); A=A-A.T
S=np.zeros((nV,nV),complex); S[np.ix_(loc0,loc0)]=1j*A
Mmass=sym(S,True,True); Mmass=(Mmass+Mmass.conj().T)/2; Mmass/=np.abs(Mmass).max()
for m in (0.0,0.05):
    Hr=Hbase+m*(Mmass if m else 0)
    ev,V=np.linalg.eigh(Hr)
    i=0; levels=[]
    while i<len(ev) and len(levels)<3:
        j=i
        while j<len(ev) and abs(ev[j]-ev[i])<1e-7: j+=1
        levels.append((i,j)); i=j
    print(f'mass m={m}:')
    for (i,j) in levels[:2] if m else levels[:1]:
        Vs=V[:,i:j]
        cO=chars(Vs,allO) if m==0 else None
        cT=chars(Vs,Tel)
        print(f'   level E={ev[i]:.5f} deg {j-i}:', ('O: '+str(dec(cO,allO)) if cO else ''), ' T(about site): ', dec(cT,Tel) if cT else 'no lift')
