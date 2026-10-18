import sys, itertools, numpy as np
sys.path.insert(0,'.')
exec(open('diraclib.py').read().split("Xb=np.load")[0])
Hon=H0(1.0,0.0); Hli=H0(0.0,1.0)
blon=blocks_from(Hon); blli=blocks_from(Hli)
Hon0=Hk(blon,np.zeros(3)).real
w,V=np.linalg.eigh(Hon0)
Ps=[V[:,np.abs(w-l)<1e-6]@V[:,np.abs(w-l)<1e-6].T for l in (-1-np.sqrt(3),np.sqrt(3)-1,2.0)]
ph=[1,1j,-1,-1j]
rng=np.random.default_rng(2); dirs=rng.normal(size=(40,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
kgen=[rng.uniform(-np.pi,np.pi,3) for _ in range(6)]
def wrap(x): return np.angle(np.exp(1j*x))
res=[]
for lname,Ul in (("R",lambda k: Hk(blli,k)/np.sqrt(2)),("S",lambda k:(np.eye(12)+1j*Hk(blli,k)/np.sqrt(2))/np.sqrt(2))):
  for a,b in itertools.product(range(4),repeat=2):
    Uon=Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]
    W=lambda k: Ul(k)@Uon
    e0=np.sort(np.angle(np.linalg.eigvals(W(kst))))
    lv=[]
    for x in e0:
        if lv and abs(wrap(x-lv[-1][0]))<1e-7: lv[-1][1]+=1
        else: lv.append([x,1])
    if len(lv)>1 and abs(wrap(lv[0][0]-lv[-1][0]))<1e-7: lv[0][1]+=lv[-1][1]; lv.pop()
    for E,m in lv:
        # flat bands: count eigenvalues equal to E at generic k
        flat=max(sum(abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))<1e-6) for k in kgen)
        sp={}
        for q in (2e-3,1e-3):
            S=[]
            for d in dirs:
                ee=wrap(np.angle(np.linalg.eigvals(W(kst+q*d)))-E); S.append(np.sort(ee[np.abs(ee)<0.05])/q)
            sp[q]=np.array(S)
        lin=np.abs(sp[1e-3]).max(0); spread=np.ptp(sp[1e-3],0); spread2=np.ptp(sp[2e-3],0)
        res.append((lname,a,b,round(E,4),m,flat,np.round(sp[1e-3].mean(0),5),np.round(spread,9),np.round(spread2,9)))
for r in res:
    if r[4]>=2 and np.abs(r[6]).max()>1e-3: print(r)
