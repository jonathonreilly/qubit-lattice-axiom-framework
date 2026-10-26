from t8 import *
rng=np.random.default_rng(7)
cs=[]
for it in range(600):
    c=rng.normal(size=5); c/=np.linalg.norm(c); cs.append(c)
for it in (161,291,514):
    c=cs[it]; Mz=Mof(c); Mall=build_M_all(Mz)
    M24=np.zeros((24,24),complex)
    for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
    print('it',it,'c',np.round(c,4),'eigM',np.round(np.linalg.eigvalsh(Mz),4))
    for E in (4.8,5.2,5.6,5.9,6.3):
        tab=make_tab(E,60)
        gl=levels_tab(tab,M24)
        s=[]
        for g in gl:
            o=weights_tab(tab,g,M24)
            if o is None: continue
            ev=np.linalg.eigvalsh(o['Wsum'])
            s.append((round(g,4),o['null'],round(ev.min(),3),round(ev.max(),3),round(o['gap'],3)))
        print('  E',E,s)
