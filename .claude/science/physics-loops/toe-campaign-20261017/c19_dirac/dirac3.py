import sys, itertools, numpy as np
exec(open('dirac2.py').read().split("for t1,t2,delta in")[0])
Q=np.array([np.pi]*3)
grid=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,16,endpoint=False),repeat=3)))
for t1,t2,delta in ((-1.0,0.2,0.05),(-1.0,0.3,0.1),(-1.0,0.3,0.2)):
    Hr=H0(t1,t2)+delta*X; bl=blochify(Hr); f=lambda k: Hk(bl,k)
    EN=np.linalg.eigvalsh(f(kst))[0]
    E=np.array([np.linalg.eigvalsh(f(k)) for k in grid])
    b0max=E[:,0].max(); b1min=E[:,1].min(); b2min=E[:,2].min()
    print(f'\nt1={t1} t2={t2} delta={delta}: node energy {EN:.5f}; band0 max {b0max:.5f}; band1 min {b1min:.5f}; band2 min {b2min:.5f}')
    for m in (0.02,0.05):
        fm=lambda k: np.block([[f(k),m*np.eye(12)],[m*np.eye(12),f(k+Q)]])
        e0=np.linalg.eigvalsh(fm(kst))
        # folded zone: states at k* (k* and k*+Q fold together); lowest two bands each 2-fold?
        gap=e0[2]-e0[1]
        # global gap over folded zone between band 1 (2nd) and band 2 (3rd) -> 2 bands per folded cell filled = 1 band of original zone
        Ef=np.array([np.linalg.eigvalsh(fm(k)) for k in grid[::3]])
        ggap=Ef[:,2].min()-Ef[:,1].max()
        # hyperbolic isotropic dispersion near k*
        rows=[]
        rng=np.random.default_rng(1)
        for d in (0.01,0.03,0.06):
            n=rng.normal(size=3); n/=np.linalg.norm(n)
            ee=np.linalg.eigvalsh(fm(kst+d*n)); mid=(e0[1]+e0[2])/2
            up=ee[2]-mid; pred=np.sqrt((0.5*0.1288 if delta==0.05 else (0.5*0.2577 if delta==0.1 else np.nan))**2*d*d+(gap/2)**2)
            rows.append((d, round(up,5), round(pred,5) if not np.isnan(pred) else None, int(np.sum(np.abs(ee[:4]-ee[0])<1e-9))))
        print(f'   m={m}: levels at k* {np.round(e0[:4],5)} -> Dirac gap {gap:.5f} (2m would be {2*m}); global gap between bands 2 and 3 of the folded zone {ggap:.5f}; upper-band E(d) vs sqrt(v^2 d^2 + (gap/2)^2): {rows}')
