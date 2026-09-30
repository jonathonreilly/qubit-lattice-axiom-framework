#!/usr/bin/env python3
"""T23 block F extended (exploratory, operator level): what do the exact (dressed) symmetries of the
staggered D do on the 8-dim kernel?  Imports helpers by exec of t23_test.py's definitions (re-declared here)."""
import itertools, numpy as np
from collections import Counter
exec(open('t23_test.py').read().split("# ---------- Block F")[0].replace('print("','print("#'))  # reuse defs quietly
# ---- dressing ----
def find_dressing(U):
    Dg=U@D@U.T
    nz=[np.nonzero(D[i])[0] for i in range(N)]
    for eps in (1,-1):
        s=np.zeros(N,int); s[0]=1; stack=[0]; ok=True
        while stack and ok:
            i=stack.pop()
            for j in nz[i]:
                if abs(Dg[i,j])<1e-12: ok=False;break
                sj=int(round(eps*D[i,j]/Dg[i,j]))*s[i]
                if s[j]==0: s[j]=sj; stack.append(j)
                elif s[j]!=sj: ok=False;break
        if ok and (s!=0).all():
            S_=np.diag(s.astype(float))
            if np.allclose(S_@Dg@S_,eps*D): return eps,S_
    return None
rec=[]
for (p,s,M) in G:
    for t in itertools.product(range(L),repeat=3):
        U=site_unitary(M,t); res=find_dressing(U)
        if res is None: continue
        eps,S_=res; R8=V.T@(S_@U)@V
        rec.append(dict(proper=det(M)==1,eps=eps,R8=R8,t=t,M=M,p=p))
print("dressed records:",len(rec), Counter((r['proper'],r['eps']) for r in rec))
def hw_map(R8):
    # how the dressed op moves hw sectors: for each corner column, which hw does image have (nonzero rows)
    out=set()
    for a,c in enumerate(corners):
        rows=np.nonzero(np.abs(R8[:,a])>1e-9)[0]
        out.add((sum(c),tuple(sorted(set(sum(corners[i]) for i in rows)))))
    return sorted(out)
# 1) pure translations (M=identity), any t
trans=[r for r in rec if (r['M']==np.eye(3,dtype=int)).all()]
print("pure dressed translations:",len(trans),"; hw action of t=(1,0,0):",hw_map([r for r in trans if r['t']==(1,0,0)][0]['R8']))
# 2) triplet-preserving proper dressed ones: their triplet action
def tripact(R8):
    T=R8[np.ix_(triplet,triplet)]
    return T
pres=[r for r in rec if r['proper'] and np.linalg.norm(r['R8'][np.ix_([i for i in range(8) if i not in triplet],triplet)])<1e-10]
print("proper triplet-preserving dressed symmetries:",len(pres))
acts=Counter()
for r in pres:
    T=tripact(r['R8'])
    pmat=np.abs(np.round(T)).astype(int)
    perm=tuple(int(np.argmax(pmat[:,j])) for j in range(3))
    sgn=tuple(int(np.sign(T[perm[j],j])) for j in range(3))
    acts[(perm,sgn)]+=1
print("  triplet actions (perm, signs) -> count:",dict(acts))
print("  translation parts of these:",Counter(r['t'] for r in pres))
# 3) commutant tests on three subgroups
def closure(gens,limit=100000):
    key=lambda A:tuple(np.round(A.flatten(),6)); seen={key(np.eye(8)):np.eye(8)}; fr=[np.eye(8)]
    while fr:
        new=[]
        for A in fr:
            for B in gens:
                Cm=B@A;k=key(Cm)
                if k not in seen: seen[k]=Cm;new.append(Cm)
                if len(seen)>limit: return None
        fr=new
    return list(seen.values())
def uniq(mats):
    d={}
    for R in mats: d[tuple(np.round(R.flatten(),6))]=R
    return list(d.values())
rng=np.random.default_rng(5)
def commutant_spectrum(mats,label):
    grp=closure(uniq(mats))
    def avg(X): return sum(A@X@A.T for A in grp)/len(grp)
    res=[]
    for _ in range(3):
        X=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8)); X=(X+X.conj().T)/2
        res.append(np.round(np.linalg.eigvalsh(avg(X)),6))
    # commutant dimension = dim of fixed space of averaging on real-linear space of 8x8 complex matrices
    # via trace of (1/|G|) sum kron(A,A): dim_C commutant = mean |chi(A)|^2
    dimc=sum(abs(np.trace(A))**2 for A in grp)/len(grp)
    print(f"  [{label}] |group|={len(grp)}  dim commutant={dimc:.3f}  eigen-multiplicity pattern of averaged random Hermitian: {sorted(Counter(res[0]).values())}")
commutant_spectrum([r['R8'] for r in rec if (r['M']==np.eye(3,dtype=int)).all()], "dressed translations only")
commutant_spectrum([r['R8'] for r in rec if r['proper'] and r['t']==(0,0,0)], "proper dressed rotations, t=0")
commutant_spectrum([r['R8'] for r in rec if r['proper']], "proper dressed rotations x translations")
commutant_spectrum([r['R8'] for r in rec], "all (proper+improper) dressed")
commutant_spectrum([r['R8'] for r in pres], "the 32 triplet-preserving proper ones")
