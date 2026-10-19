exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
onH=[(f"H{a}{b}",Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
rng=np.random.default_rng(4)
G=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,10,endpoint=False),repeat=3)))+0.137
far=[k for k in G if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.6]
dirs=DIRS[:8]; out=[]
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
        # cleanliness: min distance of any band from E at far momenta
        dmin=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))) for k in far)
        out.append((round(dmin,4),lname,name,round(E,4),round(Sx.mean(),6)))
out.sort(reverse=True)
print(len(out),"Weyl hits; best by far-zone gap at node quasi-energy:")
seen=set()
for o in out[:25]:
    key=(o[0],o[4])
    if key in seen: continue
    seen.add(key); print(o)
