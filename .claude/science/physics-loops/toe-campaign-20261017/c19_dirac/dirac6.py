from diraclib import *
import itertools
exec(open('dirac5.py').read().split("res={}")[0].split("rng=np.random.default_rng(11)")[1].split("def w1(R):")[0].replace("X=np.tensordot","_X=np.tensordot").replace("X/=np.abs(X).max()","").replace("Hbase=H0(-1.0,0.2)+0.05*X","").replace("bl=blocks_from(Hbase); EN=np.linalg.eigvalsh(Hk(bl,kst))[0]","").replace("ev0,V0=np.linalg.eigh(Hbase); idx=np.where(np.abs(ev0-EN)<1e-6)[0]; P4=V0[:,idx]","")) if False else None
exec(open('dirac5.py').read().split("res={}")[0].split("def w1(R):")[0].replace("from diraclib import *",""))
exec("def w1(R):"+open('dirac5.py').read().split("def w1(R):")[1].split("res={}")[0])
# dimension of the imaginary A2 staggered on-site mass space
seeds=[]
for t in range(10):
    A=rng.normal(size=(12,12)); A=A-A.T
    S=np.zeros((nV,nV),complex); S[np.ix_(loc0,loc0)]=1j*A
    Mm=sym(S,True,True); Mm=(Mm+Mm.conj().T)/2; seeds.append(Mm.ravel())
sv=np.linalg.svd(np.array(seeds),compute_uv=False); dimM=int(np.sum(sv>1e-8*sv[0]))
print('dimension of the on-site imaginary staggered A2 mass space:',dimM)
Mm=seeds[0].reshape(nV,nV); Mm/=np.abs(Mm).max()
blM=blocks_from(Mm)   # momentum-Q operator: <k+Q|M|k> = sum_r M[(r,.),(0,.)] e^{i k.r}
def Hfold(blH,blM,k,m):
    A=Hk(blH,k); Bq=Hk(blM,k)   # couples k -> k+Q
    return np.block([[A, m*Bq.conj().T],[m*Bq, Hk(blH,k+Q)]])
# exact cross-check with the real-space spectrum on L = 4
m=0.05
Hr=Hbase+m*Mm
er=np.sort(np.linalg.eigvalsh(Hr))
ks=[np.array(t)*2*np.pi/L for t in itertools.product(range(L),repeat=3)]
half=[k for k in ks if (np.round(k/np.pi*L/2).astype(int)%L).sum()>=0]
# folded zone: take one representative of each pair {k, k+Q}
reps=[];seen=set()
for k in ks:
    key=tuple(np.round((k/(2*np.pi/L))).astype(int)%L); key2=tuple((np.array(key)+L//2)%L)
    if key2 in seen: continue
    seen.add(key); reps.append(k)
ef=np.sort(np.concatenate([np.linalg.eigvalsh(Hfold(bl,blM,k,m)) for k in reps]))
print('folded Bloch spectrum equals the real-space spectrum on L = 4:', np.allclose(ef,er,atol=1e-9))
e0=np.linalg.eigvalsh(Hfold(bl,blM,kst,m)); print('levels at k*:',np.round(e0[:6],5))
