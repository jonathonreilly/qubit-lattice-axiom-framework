exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
import pickle
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[np.exp(1j*np.pi*n/6) for n in range(12)]
onH=[(f"H{a}.{b}",Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]) for a,b in itertools.product(range(12),repeat=2)]
onL=[(f"L{a}.{b}.{c}",Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]) for a,b,c in itertools.product(range(12),repeat=3)]
cands=onH+onL
cube=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
other=[c for c in cube if not (np.allclose(np.exp(1j*(c-kst)),1) or np.allclose(np.exp(1j*(c+kst)),1))]
g=np.linspace(-np.pi,np.pi,8,endpoint=False)
G=[np.array(k)+0.13 for k in itertools.product(g,repeat=3)]
G=[k for k in G if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.5]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k)}
pre={nm:{"kst":f(kst),"oth":[f(c) for c in other],"G":[f(k) for k in G],"d":[f(kst+1e-3*d) for d in DIRS[:6]]} for nm,f in links.items()}
out=[]
for lname in links:
  P=pre[lname]
  for name,U in cands:
    e0=np.angle(np.linalg.eigvals(P["kst"]@U))
    for E in e0:
        if np.sum(np.abs(wrap(e0-E))<1e-7)!=2: continue
        sp=[]
        for M in P["d"]:
            ee=wrap(np.angle(np.linalg.eigvals(M@U))-E); ee=np.sort(ee[np.abs(ee)<0.05]); sp.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
        sp=np.array(sp)
        if np.isnan(sp).any() or sp.min()<1e-3: continue
        if min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(M@U))-E))) for M in P["oth"])<1e-3: continue
        dmin=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(M@U))-E))) for M in P["G"])
        out.append((round(dmin,4),lname,name,round(float(E),4),round(sp.mean(),6),round(np.ptp(sp),8)))
out=sorted(set(out),reverse=True)
print(len(out),"Weyl at k* without cube-point doublers; best far-grid distances:")
for o in out[:20]: print(o)
pickle.dump(out,open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/pi6_out.pkl','wb'))
