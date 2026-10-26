import numpy as np, time
from engine import *
lat=Lat((4,4,4,4)); rng=np.random.default_rng(1)
U=random_su3(rng,(4,lat.V),eps=None)
print('unitarity',np.abs(U@dag(U)-np.eye(3)).max(), np.abs(np.linalg.det(U)-1).max())
g=Gauge(lat,6.0)
# plaq of identity
print('cold plaq',g.plaq(np.tile(np.eye(3,dtype=complex),(4,lat.V,1,1))))
# force check gauge
H=herm_traceless_gauss(rng,(4,lat.V))
def Sg(eps): return g.action(expm_ih(eps*H)@U)
e=1e-5
num=(Sg(e)-Sg(-e))/(2*e)
F=traceless_herm(g.force(U))
print('gauge force',num,np.einsum('msij,msji->',H,F).real)
# fermion
m=0.1
f=Fermion(lat,m,1e-13)
f.prep(U)
phi=f.refresh(rng)
def Sf(eps):
    f.prep(expm_ih(eps*H)@U); return f.action_force(phi,False)[0]
num=(Sf(e)-Sf(-e))/(2*e)
f.prep(U)
S,N=f.action_force(phi)
F=traceless_herm(N)
print('fermion force',num,np.einsum('msij,msji->',H,F).real)
# dense det check
V=lat.V
Dm=np.zeros((V*3,V*3),dtype=complex)
for s in range(V):
    for c in range(3):
        v=np.zeros((V,3),dtype=complex); v[s,c]=1
        Dm[:,s*3+c]=f.D(v).reshape(-1)
print('antiherm',np.abs(Dm+Dm.conj().T).max())
ld=np.linalg.slogdet(m*np.eye(V*3)+Dm)
ev=np.where(lat.even)[0]
idx=np.concatenate([[3*s+c for c in range(3)] for s in ev])
A=m*m*np.eye(V*3)-Dm@Dm
ld2=np.linalg.slogdet(A[np.ix_(idx,idx)])
print('det check',ld,ld2)
# timing
t=time.time(); 
for _ in range(100): f.D(phi)
print('D time',(time.time()-t)/100)
t=time.time(); x=f.cg(phi); print('cg',time.time()-t,f.cg_iters)
# HMC dH scaling
for Ns,nmd in [(0,10),(1,10)]:
    h=HMC(lat,6.0,Ns=Ns,m=0.1,nmd=nmd,tau=1.0,seed=3)
    t=time.time()
    for k in range(20):
        acc,dH=h.trajectory(thermal=True)
    print(Ns,'20 traj thermal',time.time()-t,h.g.plaq(h.U))
    t=time.time()
    for k in range(10):
        acc,dH=h.trajectory()
        print(acc,round(dH,3),round(h.g.plaq(h.U),4))
    print('10 traj',time.time()-t,getattr(h.f,'cg_iters',0))
