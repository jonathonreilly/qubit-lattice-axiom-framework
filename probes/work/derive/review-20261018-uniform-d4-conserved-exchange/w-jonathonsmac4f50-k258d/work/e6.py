from e5 import *
import time
rng=np.random.default_rng(5)
dirs=[rng.standard_normal(4) for _ in range(40)]
dirs+= [np.array([1,1e-2,0,0.]),np.array([1,1e-2,1e-2,0]),np.array([1,1,1,1.01]),np.array([1,1,1e-3,1e-3]),np.array([1,-1,1,-1.]),np.array([1,1,0,0.]),np.array([1,1,1,0.]),np.array([1,2,0,0])]
for kap in (0.,1/24):
  worst=[];t0=time.time()
  al,be=-4,(4/3 if kap==0 else 2)
  for d in dirs:
    d=d/np.linalg.norm(d);res=[]
    for t in (.02,.01):
        qq=t*d;Ts,w=cons_basis(qq);K,Bs=Kmat(C,qq,kap,Ts,w);nF=np.linalg.norm(F(Ts,al,be))
        e0=np.linalg.norm(K-F(Ts,al,be))/nF; e1=np.linalg.norm(K-Ftil(Ts,qq,-1,al,be))/nF
        D=K-F(Ts,al,be);
        res.append((e0,e1,np.linalg.norm((D+D.conj().T)/2)/nF,np.linalg.norm((D-D.conj().T)/2)/nF,np.abs(D.real).max()/nF,np.abs(D.imag).max()/nF))
    worst.append((res[0][0]/res[1][0], res[0][1]/res[1][1], res[1][1]/.01**2, res[1][0]/.01, res[1][2]/.01**2, res[1][3]/.01))
  w_=np.array(worst);print('kap',kap,'time',time.time()-t0)
  print(' ratio fitT (e0 .02/.01): min/max',np.nanmin(w_[:,0]),np.nanmax(w_[:,0]))
  print(' ratio fitTtilde: min/max',np.nanmin(w_[:,1]),np.nanmax(w_[:,1]))
  print(' sup e1/t^2',np.nanmax(w_[:,2]),' sup e0/t',np.nanmax(w_[:,3]),' herm part/t^2',np.nanmax(w_[:,4]),' antiherm/t',np.nanmax(w_[:,5]))
