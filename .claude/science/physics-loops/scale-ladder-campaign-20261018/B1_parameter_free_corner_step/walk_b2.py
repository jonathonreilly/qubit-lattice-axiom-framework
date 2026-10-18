exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
Tb1=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/Tb1.npy')
blb=blocks_from(Tb1); RB=lambda k: Hk(blb,k)/np.sqrt(2)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
onH=[(f"H{a}{b}",Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL
links={"Rb":RB,"Rb.RL":lambda k: RB(k)@RL(k),"RL.Rb":lambda k: RL(k)@RB(k)}
dirs=DIRS[:12]; hits=[]
for lname,UL in links.items():
  for name,U in cands:
    W=lambda k: UL(k)@U
    lv=levels(W,kst)
    for E,m in lv:
        if m!=2: continue
        S=[]
        for d in dirs:
            ee=wrap(np.angle(np.linalg.eigvals(W(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05])
            S.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
        S=np.array(S)
        if np.isnan(S).any() or S.min()<1e-3: continue
        flat=max(sum(abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))<1e-6) for k in KG)
        gap=min([abs(wrap(E2-E)) for E2,m2 in lv if abs(wrap(E2-E))>1e-7]+[9])
        hits.append((lname,name,round(E,4),round(S.mean(),6),round(np.ptp(S),9),flat,round(gap,4)))
print(len(hits),"Weyl doublet hits")
seen=set()
for h in sorted(hits,key=lambda x:(x[5],-x[6])):
    key=(h[0],h[3],h[5],h[6])
    if key in seen: continue
    seen.add(key); print(h)
