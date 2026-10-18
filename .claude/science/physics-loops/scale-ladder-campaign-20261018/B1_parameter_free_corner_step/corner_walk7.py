exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
X0=1j*(Hon0@Lam-Lam@Hon0); A0=Hon0@Lam+Lam@Hon0
for nm,M in (("X0=i[Hon,Lam]",X0),("A0={Hon,Lam}",A0)):
    print(nm,"hermitian",np.allclose(M,M.conj().T),"spec",np.round(np.linalg.eigvalsh(M),4))
def projs(M):
    w,V=np.linalg.eigh(M); ls=sorted(set(np.round(w,6)))
    return [V[:,np.abs(w-l)<1e-6]@V[:,np.abs(w-l)<1e-6].conj().T for l in ls]
ops={"H":projs(Hon0),"L":projs(Lam),"X":projs(X0),"A":projs(A0)}
def refls(Pl):
    out=[]
    for sg in itertools.product((1,-1),repeat=len(Pl)-1):
        out.append(sum(s*P for s,P in zip((1,)+sg,Pl)))
    return out
R={k:[(f"{k}{i}",U) for i,U in enumerate(refls(v))] for k,v in ops.items()}
singles=[x for k in R for x in R[k]]
pairs=[(a[0]+b[0],a[1]@b[1]) for a in singles for b in singles if a[0][0]!=b[0][0]]
links=[("R",RL),("S",lambda k:(np.eye(12)+1j*RL(k))/np.sqrt(2))]
dirs=DIRS[:10]; hits=[]
for lname,UL in links:
  for name,U in singles+pairs:
    W=lambda k: UL(k)@U
    lv=levels(W,kst)
    for E,m in lv:
        if m!=2: continue
        q=1e-3; S=[]
        for d in dirs:
            ee=wrap(np.angle(np.linalg.eigvals(W(kst+q*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); S.append((ee[-1]-ee[0])/(2*q) if len(ee)==2 else np.nan)
        S=np.array(S)
        if np.isnan(S).any() or S.min()<1e-2: continue
        flat=max(sum(abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))<1e-6) for k in KG)
        gap=min([abs(wrap(E2-E)) for E2,m2 in lv if abs(wrap(E2-E))>1e-7]+[9])
        hits.append((lname,name,round(E,4),round(S.mean(),6),round(np.ptp(S),9),flat,round(gap,4)))
print(len(hits),"Weyl doublet hits")
seen=set()
for h in sorted(hits,key=lambda x:(x[5],x[4],-x[6])):
    key=(h[3],h[5],h[6])
    if key in seen: continue
    seen.add(key); print(h)
