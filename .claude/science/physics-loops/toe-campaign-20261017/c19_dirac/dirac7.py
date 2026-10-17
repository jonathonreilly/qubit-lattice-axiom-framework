import itertools, numpy as np
exec(open('dirac6.py').read().split("# exact cross-check")[0])
grid=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,12,endpoint=False),repeat=3)))
rng2=np.random.default_rng(3)
Xs=[np.tensordot(rng2.normal(size=len(Xb)),Xb,1) for _ in range(3)]; Xs=[x/np.abs(x).max() for x in Xs]
best=[]
for xi,Xc in enumerate(Xs):
  for t2 in (0.05,0.1,0.2,0.3):
    for delta in (0.02,0.05,0.1,0.2):
        Hb=H0(-1.0,t2)+delta*Xc; blb=blocks_from(Hb)
        for m in (0.02,0.05):
            f=lambda k: np.linalg.eigvalsh(Hfold(blb,blM,k,m))
            e=np.array([f(k) for k in grid])
            g=e[:,2].min()-e[:,1].max()
            ek=f(kst); mD=(ek[2]-ek[1])/2
            best.append((g, xi, t2, delta, m, mD))
best.sort(reverse=True)
for b in best[:8]: print('global gap %.5f  X#%d t2=%.2f delta=%.2f m=%.2f  Dirac half-gap at k* %.5f'%b)
print('parameter points with a positive global gap:', sum(1 for b in best if b[0]>0), 'of', len(best))
