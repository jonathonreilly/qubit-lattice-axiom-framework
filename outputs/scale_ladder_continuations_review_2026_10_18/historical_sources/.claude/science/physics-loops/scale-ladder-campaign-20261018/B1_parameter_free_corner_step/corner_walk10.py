exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
X0=1j*(Hon0@Lam-Lam@Hon0); A0=Hon0@Lam+Lam@Hon0
def projs(M):
    w,V=np.linalg.eigh(M); ls=sorted(set(np.round(w,6)))
    return [V[:,np.abs(w-l)<1e-6]@V[:,np.abs(w-l)<1e-6].conj().T for l in ls]
ph=[1,1j,-1,-1j]
def cliff(Pl,tag):
    out=[]
    for c in itertools.product(range(4),repeat=len(Pl)-1):
        if all(x==0 for x in c): continue
        out.append((tag+"".join(map(str,c)),Pl[0]+sum(ph[x]*P for x,P in zip(c,Pl[1:]))))
    return out
S={t:cliff(projs(M),t) for t,M in (("H",Hon0),("L",Lam),("X",X0),("A",A0))}
singles=[x for t in S for x in S[t]]
tags=list(S)
pairs=[(a[0]+"."+b[0],a[1]@b[1]) for i,t1 in enumerate(tags) for t2 in tags[i+1:] for a in S[t1] for b in S[t2]]
pairs+= [(b[0]+"."+a[0],b[1]@a[1]) for i,t1 in enumerate(tags) for t2 in tags[i+1:] for a in S[t1] for b in S[t2]]
pairs=[]
print(len(singles),"singles",flush=True)
RLs=RL(kst); RLd=[(RL(kst+1e-3*d)) for d in DIRS[:8]]
links=[("R",lambda K:K),("S",lambda K:(np.eye(12)+1j*K)/np.sqrt(2))]
hits=[]
for lname,f in links:
  A_s=f(RLs); A_d=[f(K) for K in RLd]
  for (n1,U1),(n2,U2) in itertools.combinations(singles,2):
    name=n1+"|"+n2; U=None
    Ws=A_s@U1@A_s@U2
    e=np.angle(np.linalg.eigvals(Ws)); e=np.sort(e)
    # levels
    lv=[]
    for x in e:
        if lv and abs(wrap(x-lv[-1][0]))<1e-7: lv[-1][1]+=1
        else: lv.append([x,1])
    if len(lv)>1 and abs(wrap(lv[0][0]-lv[-1][0]))<1e-7: lv[0][1]+=lv[-1][1]; lv.pop()
    for E,m in lv:
        if m not in (2,4): continue
        Ssp=[]
        ok=True
        for Ad in A_d:
            ee=wrap(np.angle(np.linalg.eigvals(Ad@U1@Ad@U2))-E); ee=np.sort(ee[np.abs(ee)<0.05])/1e-3
            if len(ee)!=m: ok=False; break
            Ssp.append(ee)
        if not ok: continue
        Ssp=np.array(Ssp)
        if np.abs(Ssp).max()<1e-2: continue
        if m==2:
            v=(Ssp[:,1]-Ssp[:,0])/2; iso=np.ptp(v); kind='Weyl' if v.min()>1e-2 else 'partial'
        else:
            half=(Ssp[:,3]-Ssp[:,0])/2; inner=(Ssp[:,2]-Ssp[:,1])/2; iso=np.ptp(half)+np.ptp(inner)
            kind='Dirac' if np.allclose(half,inner,atol=1e-3) else 'multifold'
            v=half
        hits.append((kind,lname,name,round(E,4),m,round(float(np.mean(v)),5),round(float(iso),7)))
from collections import Counter
print(Counter(h[0] for h in hits))
for kind in ('Weyl','Dirac'):
    seen=set()
    for h in sorted([h for h in hits if h[0]==kind],key=lambda x:x[6]):
        key=(h[5],h[4])
        if key in seen: continue
        seen.add(key); print(h)
