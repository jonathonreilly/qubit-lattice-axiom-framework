"""Kill-check K1 (independent code): does V* (the attack's L-conserving clause) keep 'energy flows as momentum'?

Energy of a record = 1 (unit speed), so the energy density is the occupancy n(x).  Its current is the rate-weighted
displacement of occupancy: J_tot(cfg) = sum over streaming moves (record steps into an EMPTY site) of the step vector.
Exchanges (pass-through) and class re-assignments move no occupancy, so they add nothing to J_tot.
P(cfg) = sum of contents (conserved by every event of V*).

Blocks 135-137 (walker): the member's identity  d^2 e/dt^2 = sum_ij dbar_i dbar_j Theta_ij  (Theta symmetric, local)
has a zero first moment on its right side, so it NEEDS   L J_tot = 0   (J_tot conserved), and 'energy flows as
momentum' means J_tot = P.  Both are the 'books' of blocks 136/137, and the classical clause's asymmetry
T^{0i} = (1-rho) T^{i0} is already in the 2026-09-21 wind-potential note (T3).

Clauses: 'vstar'  = attack's V* (perpendicular target blocked, antiparallel exchange, plaquette class events)
         'orig'   = 2026-09-20 clause streaming part (any occupied target exchanges contents) + same plaquette events
         'vstar_noC' = V* streaming only (no class events)
Independent implementation (own event generator, own class enumeration).
"""
import itertools, sys
from collections import defaultdict
import numpy as np

Lx = 5
E = [(1,0),(-1,0),(0,1),(0,-1)]
OPP = {0:1,1:0,2:3,3:2}
def sid(x,y): return (x % Lx) + Lx*(y % Lx)
def xy(s): return s % Lx, s // Lx

def cross2(p,c): return p[0]*c[1]-p[1]*c[0]
_cls = {}
def class_moves(local_pts, ks):
    key=(tuple(local_pts),ks)
    if key in _cls: return _cls[key]
    P=(sum(E[k][0] for k in ks), sum(E[k][1] for k in ks)); L=sum(cross2(p,E[k]) for p,k in zip(local_pts,ks))
    out=[]
    for cand in itertools.product(range(4), repeat=len(ks)):
        if cand==ks: continue
        P2=(sum(E[k][0] for k in cand), sum(E[k][1] for k in cand)); L2=sum(cross2(p,E[k]) for p,k in zip(local_pts,cand))
        if P2==P and L2==L: out.append(cand)
    _cls[key]=out; return out

def events(cfg, clause):
    """cfg: dict site->content.  returns list of (rate, newcfg, displacement_of_occupancy(vector))"""
    ev=[]
    for s,k in cfg.items():
        x,y=xy(s); t=sid(x+E[k][0], y+E[k][1])
        if t not in cfg:
            n=dict(cfg); del n[s]; n[t]=k; ev.append((1.0,n,E[k]))
        else:
            k2=cfg[t]
            if k2==k: continue                       # identical contents: exchange changes nothing
            if k2==OPP[k] or clause=='orig':
                n=dict(cfg); n[s]=k2; n[t]=k; ev.append((1.0,n,(0,0)))
    if clause in ('vstar','orig'):
        for y in range(Lx):
            for x in range(Lx):
                sites=[sid(x,y),sid(x+1,y),sid(x,y+1),sid(x+1,y+1)]; loc=[(0,0),(1,0),(0,1),(1,1)]
                occ=[i for i in range(4) if sites[i] in cfg]
                if len(occ)<2: continue
                ks=tuple(cfg[sites[i]] for i in occ)
                for cand in class_moves([loc[i] for i in occ], ks):
                    n=dict(cfg)
                    for i,kk in zip(occ,cand): n[sites[i]]=kk
                    ev.append((1.0,n,(0,0)))
    return ev

def Jtot(cfg, clause):
    j=np.zeros(2)
    for r,n,d in events(cfg,clause): j+=r*np.array(d)
    return j
def Ptot(cfg): return np.array([sum(E[k][0] for k in cfg.values()), sum(E[k][1] for k in cfg.values())],float)

def key(cfg): return tuple(sorted(cfg.items()))

def census(N, clause, nsample=None, seed=0):
    import random
    rnd=random.Random(seed)
    nJP=0; nLJ=0; tot=0; maxLJ=0
    sample=None
    def gen():
        if nsample is None:
            for occ in itertools.combinations(range(Lx*Lx), N):
                for ks in itertools.product(range(4), repeat=N):
                    yield occ,ks
        else:
            for _ in range(nsample):
                occ=tuple(sorted(rnd.sample(range(Lx*Lx),N))); ks=tuple(rnd.randrange(4) for _ in range(N))
                yield occ,ks
    for occ,ks in gen():
        cfg=dict(zip(occ,ks)); tot+=1
        J=Jtot(cfg,clause); P=Ptot(cfg)
        if np.abs(J-P).max()>1e-12: nJP+=1
        LJ=sum(r*(Jtot(n,clause)-J) for r,n,d in events(cfg,clause))
        if np.abs(LJ).max()>1e-12:
            nLJ+=1; maxLJ=max(maxLJ,np.abs(LJ).max())
            if sample is None: sample=(cfg,J,P,LJ)
    return tot,nJP,nLJ,maxLJ,sample

if __name__=='__main__':
    # explicit two-record example on a 6x6 torus: two co-moving neighbours
    cfg={sid(0,0):0, sid(1,0):0}
    for cl in ('vstar','orig'):
        J=Jtot(cfg,cl); P=Ptot(cfg)
        LJ=sum(r*(Jtot(n,cl)-J) for r,n,d in events(cfg,cl))
        print(f'[{cl}] two co-moving neighbours (e_x at (0,0),(1,0)): J_tot={J}, P={P}, L J_tot={LJ}')
    cfg={sid(0,0):0, sid(1,0):2}
    for cl in ('vstar','orig'):
        J=Jtot(cfg,cl); P=Ptot(cfg)
        LJ=sum(r*(Jtot(n,cl)-J) for r,n,d in events(cfg,cl))
        print(f'[{cl}] perpendicular neighbours (e_x at (0,0), e_y at (1,0)): J_tot={J}, P={P}, L J_tot={LJ}')
    for N,ns in ((2,None),(3,4000)):
        for cl in ('vstar','orig','vstar_noC'):
            tot,nJP,nLJ,mx,sm=census(N,cl,ns)
            print(f'N={N} clause={cl}: configs {tot}; J_tot != P in {nJP}; L J_tot != 0 in {nLJ} (max |L J| {mx})')
