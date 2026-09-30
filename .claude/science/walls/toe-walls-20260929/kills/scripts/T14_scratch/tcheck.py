import sys,numpy as np
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T14_scratch')
from yukawa_euclid_gap import run
def T(Nt,Ns,eps,m,w=0.0,p=0.0):
    th=2*np.pi*np.arange(Nt)/Nt; ks=2*np.pi*np.arange(Ns)/Ns
    Tt,X,Y,Z=np.meshgrid(th,ks,ks,ks,indexing='ij')
    def s(Tt,X,Y,Z): return (np.sin(Tt)/eps,np.sin(X),np.sin(Y),np.sin(Z))
    a=s(Tt,X,Y,Z); b=s(Tt+eps*w,X+p,Y,Z)
    d1=m*m+sum(x*x for x in a); d2=m*m+sum(x*x for x in b)
    num=4*(m*m-sum(x*y for x,y in zip(a,b)))
    return np.sum(num/(d1*d2))/(eps*Nt*Ns**3)
eps,m=0.5,0.5; Nt,Ns=32,20; h=0.1
T0=T(Nt,Ns,eps,m)
tt=(T(Nt,Ns,eps,m,w=h)+T(Nt,Ns,eps,m,w=-h)-2*T0)/h**2/2
ts=(T(Nt,Ns,eps,m,p=h)+T(Nt,Ns,eps,m,p=-h)-2*T0)/h**2/2
r=run(Nt,Ns,eps,m,0.4)
print("FD  tt,ts:",tt,ts); print("attacker tt,ts:",r['tt'],r['ts'])
