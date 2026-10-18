exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.optimize import minimize
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
def UH(a,b): return Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]
def UL(a,b,c): return Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]
for lab,U in (("H23*L110",UH(2,3)@UL(1,1,0)),("H23*L330",UH(2,3)@UL(3,3,0)),("H23*L200",UH(2,3)@UL(2,0,0))):
    W=lambda k: SK(k)@RL(k)@U
    lv=levels(W,kst); E=[a for a,m in lv if m==2 and abs(abs(a)-np.pi/2)<1e-6][0]
    def dist(k):
        e=wrap(np.angle(np.linalg.eigvals(W(np.asarray(k))))-E); return np.sort(np.abs(e))
    # node bands: two closest; others: third closest
    g=np.linspace(-np.pi,np.pi,20,endpoint=False)
    worst=9; worstk=None; pts=[]
    for k in itertools.product(g,repeat=3):
        k=np.array(k)+0.0731
        d=dist(k)
        dk=min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))
        pts.append((d[0],k))
    pts.sort(key=lambda x:x[0])
    # refine minima of smallest |eps-E| among all bands, from 15 lowest seeds
    mins=[]
    for d0,k0 in pts[:15]:
        r=minimize(lambda k: dist(k)[0],k0,method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-10,maxiter=3000))
        kk=r.x; dk=min(np.linalg.norm(wrap(kk-kst)),np.linalg.norm(wrap(kk+kst)))
        mins.append((round(r.fun,6),round(dk,4)))
    print(lab,"node quasi-energy",round(E,4),"levels at k*",[(round(a,3),m) for a,m in lv])
    print("   refined minima of min|eps-E| (value, distance to nearest node):",sorted(set(mins))[:10])
    # gap of OTHER bands near the node: third-closest at points near k*
    near=[dist(kst+r*d)[2] for r in (0.02,0.1,0.3) for d in DIRS[:20]]
    print("   min distance of non-node bands to E within 0.3 of k*:",round(min(near),4))
