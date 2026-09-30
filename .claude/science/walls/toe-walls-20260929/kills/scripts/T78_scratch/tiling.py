"""Kill-check: find ice states that are a perfect plaquette tiling of the links (each link in exactly one chosen plaquette,
each chosen plaquette circulating) -> automatically ice, and every chosen plaquette is flippable => N_f >= 3L^3/4.
Then run the attack's flip-MC from that seed and compare <N_f>/(3L^3) with the attack's seed component (0.2597)."""
import numpy as np, sys, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
L=int(sys.argv[1]); nsamp=int(sys.argv[2]); burn=int(sys.argv[3])
def sh(v,a):
    w=list(v); w[a]=(w[a]+1)%L; return tuple(w)
plaqs=[]  # (a,b,x,y,z) links (a,v),(b,v+a),(a,v+b),(b,v)
for x in range(L):
  for y in range(L):
    for z in range(L):
      for a,b in ((0,1),(1,2),(0,2)):
        v=(x,y,z); va=sh(v,a); vb=sh(v,b)
        plaqs.append(((a,)+v,(b,)+va,(a,)+vb,(b,)+v))
cover={}
for i,p in enumerate(plaqs):
    for l in p: cover.setdefault(l,[]).append(i+1)
clauses=[]; top=len(plaqs)
for l,vs in cover.items():
    enc=CardEnc.equals(lits=vs,bound=1,top_id=top,encoding=EncType.pairwise)
    clauses+=enc.clauses; top=max(top,enc.nv)
s=Cadical153(bootstrap_with=clauses)
ok=s.solve()
print("exact plaquette tiling exists at L=%d:"%L,ok)
if not ok: sys.exit()
model=s.get_model(); chosen=[i for i in range(len(plaqs)) if model[i]>0]
print("plaquettes chosen",len(chosen),"expected",3*L**3//4)
# orient: link arrow s=+1 if from v to v+e_a. circulating: s1=s2=+1, s3=s4=-1 or all reversed
sarr=np.zeros((3,L,L,L),dtype=np.int8)
rng=np.random.default_rng(1)
for i in chosen:
    p=plaqs[i]; sg=rng.choice([1,-1])
    for k,l in enumerate(p):
        a,x,y,z=l
        sarr[a,x,y,z]= sg if k<2 else -sg
assert (sarr!=0).all()
from ice_flux_mc import check_ice_and_flux, count_flippable, sweep, flippable, _xs
print("ice violation",check_ice_and_flux(sarr,L)[0],"flux",check_ice_and_flux(sarr,L)[1:4],"N_f seed",count_flippable(sarr,L),"per site3L3",count_flippable(sarr,L)/(3*L**3))
import numba as nb
from numba import njit
@njit
def run(s,L,seed,burn,nsamp):
    rng=np.empty(1,dtype=np.uint64); rng[0]=np.uint64(seed)*np.uint64(0x9E3779B97F4A7C15)+np.uint64(12345)
    for _ in range(20): _xs(rng)
    out=np.zeros(nsamp)
    for _ in range(burn): sweep(s,L,rng)
    for k in range(nsamp):
        sweep(s,L,rng); out[k]=count_flippable(s,L)
    return out
o=run(sarr.copy(),L,5,burn,nsamp)
print("MC from tiling seed: <N_f>/(3L^3) =",o.mean()/(3*L**3),"+/-",o.std()/np.sqrt(nsamp),"first/last quarter",o[:nsamp//4].mean()/(3*L**3),o[-nsamp//4:].mean()/(3*L**3))
np.save("tiling_L%d.npy"%L,sarr)
