exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.linalg import expm
from scipy.optimize import minimize
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,np.asarray(k))
cands=[]
for n in range(1,9):
    for sgn in (1,-1):
        cands.append((f"exp({sgn}i pi Hon/{n})",expm(sgn*1j*np.pi*Hon0/n)))
        cands.append((f"exp({sgn}i pi Lam/({n}sqrt2))",expm(sgn*1j*np.pi*Lam/(n*np.sqrt(2)))))
        cands.append((f"exp({sgn}i pi (Hon+Lam)/{n})",expm(sgn*1j*np.pi*(Hon0+Lam)/n)))
links={"S":SK,"S.RL":lambda k: SK(k)@RL(np.asarray(k))}
cube=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
other=[c for c in cube if not (np.allclose(np.exp(1j*(c-kst)),1) or np.allclose(np.exp(1j*(c+kst)),1))]
res=[]
for ln,L in links.items():
  for nm,U in cands:
    W=lambda k: L(k)@U
    e0=np.angle(np.linalg.eigvals(W(kst)))
    for E in e0:
        if np.sum(np.abs(wrap(e0-E))<1e-7)!=2: continue
        sp=[]
        for d in DIRS[:6]:
            ee=wrap(np.angle(np.linalg.eigvals(W(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); sp.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
        sp=np.array(sp)
        if np.isnan(sp).any() or sp.min()<1e-3: continue
        oc=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(c)))-E))) for c in other)
        dist=lambda k: np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E)))
        g=np.linspace(-np.pi,np.pi,14,endpoint=False)
        pts=sorted(((dist(np.array(k)+0.07),np.array(k)+0.07) for k in itertools.product(g,repeat=3) if min(np.linalg.norm(wrap(np.array(k)+0.07-kst)),np.linalg.norm(wrap(np.array(k)+0.07+kst)))>0.4),key=lambda x:x[0])
        best=pts[0][0]
        if best>0.02:
            for d0,k0 in pts[:25]:
                r=minimize(dist,k0,method='Nelder-Mead',options=dict(xatol=1e-8,fatol=1e-12,maxiter=3000))
                kk=r.x
                if min(np.linalg.norm(wrap(kk-kst)),np.linalg.norm(wrap(kk+kst)))>0.05: best=min(best,r.fun)
        res.append((round(best,5),round(oc,4),ln,nm,round(float(E),4),round(sp.mean(),6),round(np.ptp(sp),8)))
res.sort(reverse=True)
print(len(res),"Weyl-at-k* steps; (refined min distance to E away from +-k*, min at other cube points, ...):")
for r in res[:15]: print(r)
