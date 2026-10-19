exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
onH=[(f"H{a}{b}",Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]) for a,b,c in itertools.product(range(4),repeat=3)]
links=[("R",RL),("S",lambda k:(np.eye(12)+1j*RL(k))/np.sqrt(2))]
dirs=DIRS[:12]; hits=[]
cands=[(h[0],h[1]) for h in onH]+[(l[0],l[1]) for l in onL]+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]
for lname,UL in links:
  for name,U in cands:
    W=lambda k: UL(k)@U
    lv=levels(W,kst)
    for E,m in lv:
        if m not in (4,6): continue
        q=1e-3; S=[]
        for d in dirs:
            ee=wrap(np.angle(np.linalg.eigvals(W(kst+q*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05])/q; S.append(ee)
        S=np.array(S)
        if S.shape[1]!=m: continue
        lin=np.abs(S).max(0)
        if lin.max()<1e-2: continue
        flat=max(sum(abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))<1e-6) for k in KG)
        gap=min([abs(wrap(E2-E)) for E2,m2 in lv if abs(wrap(E2-E))>1e-7]+[9])
        hits.append((lname,name,round(E,4),m,flat,np.round(S.mean(0),5),np.round(np.ptp(S,0),6),round(gap,4)))
print(len(hits),"hits")
seen=set()
for h in sorted([x for x in hits if x[3]==4],key=lambda x:(x[4],x[6].max())):
    key=(h[2],h[3],h[4],tuple(h[5]))
    if key in seen: continue
    seen.add(key); print(h)
