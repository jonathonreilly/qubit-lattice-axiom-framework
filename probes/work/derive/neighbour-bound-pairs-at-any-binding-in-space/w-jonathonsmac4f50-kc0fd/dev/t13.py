from t8 import *
rng=np.random.default_rng(7)
cs=[]
for it in range(600):
    c=rng.normal(size=5); c/=np.linalg.norm(c); cs.append(c)
c=cs[312]; print('c312',repr(c))
Mz=Mof(c); print('eig M(e_z):',np.round(np.linalg.eigvalsh(Mz),4))
Mall=build_M_all(Mz)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
# all bound levels vs g: use find_levels at several g with N=48 (E range)
g=5.87
V=g*M24
roots=find_levels(V,48,+1,nscan=16,eta=0.02)
for js,r in sorted(roots,key=lambda t:t[1]):
    o=level_weights(r,V,48)
    ev=np.linalg.eigvalsh(o['Wsum'])
    print('E=%.6f dE_edge=%.4f mult=%d Wsum=%s'%(r,r-EC,len(js),np.round(ev,4)))
