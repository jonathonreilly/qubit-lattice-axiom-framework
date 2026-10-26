from t8 import *
rng=np.random.default_rng(7)
allrows=[]
best=[]
t=time.time()
for it in range(600):
    c=rng.normal(size=5); c/=np.linalg.norm(c)
    rows=scanM(Mof(c),tabs)
    for r in rows: allrows.append((it,)+r)
    if rows:
        m=max(rows,key=lambda r:r[3]); best.append((m[3],it,m[0],m[1],m[2],c))
print(time.time()-t,len(allrows))
A=np.array([r[1:] for r in allrows if True],dtype=float) if False else None
mx=max(allrows,key=lambda r:r[4])
print('max ev',mx)
print('max first-order residual',max(r[6] for r in allrows))
best.sort(key=lambda b:-b[0])
for b in best[:8]: print(b[0],b[1],'E',b[2],'g',b[3],'mult',b[4],np.round(b[5],3))
# distribution by E
import collections
byE=collections.defaultdict(float)
for r in allrows: byE[round(r[1],3)]=max(byE[round(r[1],3)],r[4])
for E in sorted(byE)[:12]: print(E,byE[E])
print('...')
for E in sorted(byE)[-6:]: print(E,byE[E])
pickle.dump(allrows,open('scan600.pkl','wb'))
