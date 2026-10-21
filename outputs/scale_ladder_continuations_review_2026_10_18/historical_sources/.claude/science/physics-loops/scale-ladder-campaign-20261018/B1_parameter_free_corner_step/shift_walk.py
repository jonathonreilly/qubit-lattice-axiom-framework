exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
print("S(k) unitary off-grid", np.allclose(SK(np.array([0.3,1.1,-0.7]))@SK(np.array([0.3,1.1,-0.7])).conj().T,np.eye(12)), "shifts", sorted(blS.keys()))
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
onH=[(f"H{a}{b}",Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH[::3] for l in onL[::5]]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k)}
dirs=DIRS[:12]; hits=[]
for lname,UL in links.items():
  for name,U in cands:
    W=lambda k: UL(k)@U
    lv=levels(W,kst)
    for E,m in lv:
        if m!=2: continue
        Sx=[]
        for d in dirs:
            ee=wrap(np.angle(np.linalg.eigvals(W(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05])
            Sx.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
        Sx=np.array(Sx)
        if np.isnan(Sx).any() or Sx.min()<1e-3: continue
        flat=max(sum(abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))<1e-6) for k in KG)
        gap=min([abs(wrap(E2-E)) for E2,m2 in lv if abs(wrap(E2-E))>1e-7]+[9])
        hits.append((lname,name,round(E,4),round(Sx.mean(),6),round(np.ptp(Sx),9),flat,round(gap,4)))
print(len(hits),"Weyl doublet hits")
seen=set()
for h in sorted(hits,key=lambda x:(x[5],x[4],-x[6])):
    key=(h[0],h[3],h[5],h[6])
    if key in seen: continue
    seen.add(key); print(h)
