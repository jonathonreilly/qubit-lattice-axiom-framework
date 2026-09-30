"""Kill-check: are there flip components of the ice ensemble (same flux sector q=0) with larger <N_f> density than the
big component the attack sampled?  Generate ice states by directed-cycle reversals (changes components), then
run the attack's plaquette-flip MC from each and record the component's mean N_f."""
import numpy as np, sys
from numba import njit
from ice_flux_mc import seed_config, sweep, count_flippable, _xs, check_ice_and_flux
L=int(sys.argv[1]); ns=int(sys.argv[2]); nsw=int(sys.argv[3])
@njit
def outnbrs(s,L,x,y,z,k):
    # k-th outgoing link of vertex: returns (a, lx,ly,lz, nx,ny,nz)
    c=0
    for a in range(3):
        if s[a,x,y,z]==1:
            if c==k:
                nx,ny,nz=x,y,z
                if a==0: nx=(x+1)%L
                elif a==1: ny=(y+1)%L
                else: nz=(z+1)%L
                return a,x,y,z,nx,ny,nz
            c+=1
    for a in range(3):
        lx,ly,lz=x,y,z
        if a==0: lx=(x-1)%L
        elif a==1: ly=(y-1)%L
        else: lz=(z-1)%L
        if s[a,lx,ly,lz]==-1:
            if c==k: return a,lx,ly,lz,lx,ly,lz
            c+=1
    return -1,0,0,0,0,0,0
@njit
def loopmove(s,L,rng):
    r=_xs(rng)
    x=np.int64((r>>np.uint64(8))%np.uint64(L)); y=np.int64((r>>np.uint64(20))%np.uint64(L)); z=np.int64((r>>np.uint64(32))%np.uint64(L))
    seen=-np.ones((L,L,L),dtype=np.int64)
    path=np.zeros((4*L*L*L+2,4),dtype=np.int64)
    n=0
    while True:
        if seen[x,y,z]>=0:
            start=seen[x,y,z]; break
        seen[x,y,z]=n
        k=np.int64((_xs(rng)>>np.uint64(30))%np.uint64(3))
        a,lx,ly,lz,nx,ny,nz=outnbrs(s,L,x,y,z,k)
        # determine which vertex we are heading to: out-neighbour in the 6-neighbour sense
        # outnbrs returns link coordinates and the neighbour vertex reached following the arrow
        # for the 'incoming-reversed' branch the neighbour is (lx,ly,lz)
        path[n,0]=a;path[n,1]=lx;path[n,2]=ly;path[n,3]=lz
        n+=1
        x,y,z=nx,ny,nz
    for i in range(start,n):
        a,lx,ly,lz=path[i,0],path[i,1],path[i,2],path[i,3]
        s[a,lx,ly,lz]=-s[a,lx,ly,lz]
@njit
def one(L,seed,nloop,nsw,q):
    rng=np.empty(1,dtype=np.uint64); rng[0]=np.uint64(seed)*np.uint64(0x9E3779B97F4A7C15)+np.uint64(777)
    for _ in range(20): _xs(rng)
    s=seed_config(L,0)
    for _ in range(nloop):
        s2=s.copy(); loopmove(s2,L,rng)
        b,a0,a1,a2,dv=check_ice_and_flux(s2,L)
        if a0==0 and a1==0 and a2==0 and dv==0: s=s2
    # record flux & ice check, then flip-MC
    bad,w0,w1,w2,dev=check_ice_and_flux(s,L)
    n0=count_flippable(s,L)
    acc=0.0; cnt=0
    for i in range(nsw):
        sweep(s,L,rng)
        if i>=nsw//5:
            acc+=count_flippable(s,L); cnt+=1
    return bad,w0,w1,w2,dev,n0,acc/cnt
res=[]
for i in range(ns):
    r=one(L,i+1,200*L**3//8,nsw,0)
    res.append(r)
res=np.array(res)
print("ice violations",res[:,0].max())
sel=(res[:,1]==0)&(res[:,2]==0)&(res[:,3]==0)
print("q=0 states:",sel.sum(),"of",ns)
d=res[sel,6]/(3*L**3)
print("component mean densities: min %.5f max %.5f mean %.5f"%(d.min(),d.max(),d.mean()))
print(np.round(np.sort(d)[-10:],5)); print(np.round(np.sort(d)[:10],5))
