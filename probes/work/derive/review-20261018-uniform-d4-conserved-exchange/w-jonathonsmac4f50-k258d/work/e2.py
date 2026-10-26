from ana import *
OFF,Sm=d4cone(); C=CA(OFF,Sm)
np.set_printoptions(linewidth=200,precision=5)
for d in ([0,0,0,1],[.3,-.5,.6,.55],[1,1,1,1],[1,0,0,0]):
  d=np.array(d,float); d/=np.linalg.norm(d)
  for t in (0.02,0.01):
    q=t*d; Q=C.Q(q); ev=np.linalg.eigvalsh(Q)
    nz=ev[np.abs(ev)>1e-9]; lowr=ev[(np.abs(ev)>1e-9)&(np.abs(ev)<1)]
    print(d,t,'n|ev|<1e-9:',np.sum(np.abs(ev)<1e-9),'low:',lowr/t**2, ' pos:',ev[ev>1e-9]/t**2)
