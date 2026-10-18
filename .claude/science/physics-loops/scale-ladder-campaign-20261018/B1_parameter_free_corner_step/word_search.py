exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
import pickle, time
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
onH=[Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2] for a,b in itertools.product(range(4),repeat=2)]
onL=[Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3] for a,b,c in itertools.product(range(4),repeat=3)]
ons=onH+onL
rng=np.random.default_rng(int(time.time())%100000)
cube=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
other=[c for c in cube if not (np.allclose(np.exp(1j*(c-kst)),1) or np.allclose(np.exp(1j*(c+kst)),1))]
g=np.linspace(-np.pi,np.pi,8,endpoint=False)
G=[np.array(k)+0.13 for k in itertools.product(g,repeat=3)]
G=[k for k in G if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.5]
pts=[kst]+other+G
def kfac(name,k):
    if name=="S": return Hk(blS,k)
    if name=="Si": return Hk(blS,k).conj().T
    if name=="R": return RL(k)
cacheK={nm:[kfac(nm,k) for k in pts] for nm in ("S","Si","R")}
best=[]; t0=time.time(); n=0
while time.time()-t0<3300:
    n+=1
    L=rng.integers(2,5)
    word=[]
    for _ in range(L):
        t=rng.integers(0,3)
        if t==0: word.append(("k",["S","Si","R"][rng.integers(0,3)]))
        else: word.append(("o",int(rng.integers(0,len(ons)))))
    if not any(w[0]=="k" and w[1] in ("S","Si") for w in word): continue
    def Wat(i):
        M=np.eye(12,dtype=complex)
        for t,x in word: M=M@(cacheK[x][i] if t=="k" else ons[x])
        return M
    e0=np.sort(np.angle(np.linalg.eigvals(Wat(0))))
    lv=[]
    for x in e0:
        if lv and abs(wrap(x-lv[-1][0]))<1e-7: lv[-1][1]+=1
        else: lv.append([x,1])
    if len(lv)>1 and abs(wrap(lv[0][0]-lv[-1][0]))<1e-7: lv[0][1]+=lv[-1][1]; lv.pop()
    for E,m in lv:
        if m!=2: continue
        dmin=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Wat(i)))-E))) for i in range(1,len(pts)))
        if dmin<0.05: continue
        # Weyl velocity check
        def Wk(k):
            M=np.eye(12,dtype=complex)
            for t,x in word: M=M@(kfac(x,k) if t=="k" else ons[x])
            return M
        sp=[]
        for d in DIRS[:6]:
            ee=wrap(np.angle(np.linalg.eigvals(Wk(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); sp.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
        sp=np.array(sp)
        if np.isnan(sp).any() or sp.min()<1e-3: continue
        best.append((round(dmin,4),[(t,x) for t,x in word],round(E,4),round(sp.mean(),6),round(np.ptp(sp),8)))
        print("HIT",best[-1],flush=True)
print("tried",n,"hits",len(best))
pickle.dump(best,open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/word_hits.pkl','wb'))
