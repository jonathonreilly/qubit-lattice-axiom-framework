exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
onH=[(f"H{a}{b}",Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]+[(l[0]+"*"+h[0],l[1]@h[1]) for h in onH for l in onL]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
cube=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
other=[c for c in cube if not (np.allclose(np.exp(1j*(c-kst)),1) or np.allclose(np.exp(1j*(c+kst)),1))]
hs=[np.zeros(3),np.pi*np.ones(3)]+[np.pi*e for e in np.eye(3)]+[np.pi*(1-e) for e in np.eye(3)]
links_K={nm:{tuple(np.round(k,6)):f(k) for k in [kst]+cube+hs} for nm,f in links.items()}
dirs=DIRS[:6]; good=[]
for lname,UL in links.items():
  for name,U in cands:
    W0=links_K[lname][tuple(np.round(kst,6))]@U
    e0=np.sort(np.angle(np.linalg.eigvals(W0)))
    lv=levels(lambda k: W0, kst)
    for E,m in lv:
        if m!=2: continue
        # extra levels at E at the other cube points or high-symmetry points?
        bad=False
        for k in other+hs:
            ee=np.abs(wrap(np.angle(np.linalg.eigvals(links_K[lname][tuple(np.round(k,6))]@U))-E))
            if ee.min()<1e-6: bad=True; break
        if bad: continue
        W=lambda k: UL(k)@U
        sp=[]
        for d in dirs:
            ee=wrap(np.angle(np.linalg.eigvals(W(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); sp.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
        sp=np.array(sp)
        if np.isnan(sp).any() or sp.min()<1e-3: continue
        good.append((lname,name,round(E,4),round(sp.mean(),6)))
print(len(good),"Weyl candidates with no level at E at the other cube points or high-symmetry points")
for g_ in good[:40]: print(g_)
import pickle; pickle.dump(good,open('cube_good.pkl','wb'))
