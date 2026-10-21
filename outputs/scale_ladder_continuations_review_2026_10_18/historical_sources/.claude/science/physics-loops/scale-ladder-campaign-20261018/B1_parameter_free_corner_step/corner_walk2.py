import sys, itertools, numpy as np
sys.path.insert(0,'.')
exec(open('diraclib.py').read().split("Xb=np.load")[0])
Hon=H0(1.0,0.0); Hli=H0(0.0,1.0)
blon=blocks_from(Hon); blli=blocks_from(Hli)
Hon0=Hk(blon,np.zeros(3)).real
w,V=np.linalg.eigh(Hon0); print("onsite eigenvalues", np.round(w,4))
P2=V[:,np.abs(w-2)<1e-6]; Uon=np.eye(12)-2*P2@P2.T
def W(k): return (Hk(blli,k)/np.sqrt(2))@Uon
rng=np.random.default_rng(1); dirs=rng.normal(size=(200,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
for k0,lab in ((kst,'k*'),(-kst,'-k*')):
    for q in (2e-3,1e-3):
        S=[]
        for d in dirs:
            ee=np.angle(np.linalg.eigvals(W(k0+q*d))); ee=np.sort(ee[np.abs(ee)<0.1])/q; S.append(ee)
        S=np.array(S)
        print(lab,"q",q,"eps/q per band: mean",np.round(S.mean(0),6),"spread",np.round(np.ptp(S,0),9))
# global: is quasi-energy 0 touched anywhere else? scan grid
g=np.linspace(-np.pi,np.pi,24,endpoint=False)
mins=[]
for k in itertools.product(g,repeat=3):
    ee=np.abs(np.angle(np.linalg.eigvals(W(np.array(k))+0j))); mins.append((ee.min(),k))
mins.sort(); print("smallest |eps| on 24^3 grid:", [(round(a,4),np.round(np.array(k)/(np.pi/2),3)) for a,k in mins[:6]])
print("count |eps|<0.05:", sum(1 for a,k in mins if a<0.05))
