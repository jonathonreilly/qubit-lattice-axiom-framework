"""T17 Test B: spurious invariants of the L-conserving clause V* on an L x L torus (2D, four contents).

Events (all keep N and P; every one keeps the local L, by construction / Test A):
  S1  a record steps along its content into an empty site
  S2  target occupied by a parallel or antiparallel content: contents exchange
      (perpendicular target: blocked, no event -- this is what keeps L; the original clause exchanges)
  C'  plaquette-local class permutation: for every 2x2 plaquette, every re-assignment of the contents of
      the records in it that keeps (occupied sites, P_local, L_local)
Configuration graph -> connected components inside each (N, P) sector.
Variant flags: with_S2_perp (original clause: exchange for perpendicular targets too, breaks L),
               with_C (include C').
"""
import itertools, sys, time
from collections import defaultdict

Lx = int(sys.argv[1]) if len(sys.argv) > 1 else 4
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 4
E = [(1,0),(-1,0),(0,1),(0,-1)]   # contents 0..3
OPP = {0:1, 1:0, 2:3, 3:2}
NS = Lx*Lx

def site(x, y):
    return (x % Lx) + Lx * (y % Lx)

def xy(s):
    return s % Lx, s // Lx

def code(cfg):
    c = 0
    for s, k in cfg.items():
        c += (k+1) * (5 ** s)
    return c

def cross2(x, c):     # z-component of x cross c
    return x[0]*c[1] - x[1]*c[0]

PLAQ = []
for y in range(Lx):
    for x in range(Lx):
        PLAQ.append([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])
LOCAL = [(0,0),(1,0),(0,1),(1,1)]

def local_class_moves(occ_local, contents):
    """contents: tuple of content indices for occupied local sites (list of local coords). Return all other
    assignments with the same (P, Lz)."""
    P = [0,0]; Lz = 0
    for xyl, k in zip(occ_local, contents):
        P[0] += E[k][0]; P[1] += E[k][1]
        Lz += cross2(xyl, E[k])
    outs = []
    for cand in itertools.product(range(4), repeat=len(occ_local)):
        if cand == contents:
            continue
        P2 = [0,0]; L2 = 0
        for xyl, k in zip(occ_local, cand):
            P2[0] += E[k][0]; P2[1] += E[k][1]
            L2 += cross2(xyl, E[k])
        if P2 == P and L2 == Lz:
            outs.append(cand)
    return outs

_cache = {}
def moves_cached(occ_local, contents):
    key = (tuple(occ_local), contents)
    if key not in _cache:
        _cache[key] = local_class_moves(occ_local, contents)
    return _cache[key]

def neighbours(cfg, with_S2_perp, with_C):
    out = []
    for s, k in cfg.items():
        x, y = xy(s)
        t = site(x + E[k][0], y + E[k][1])
        if t not in cfg:
            n = dict(cfg); del n[s]; n[t] = k
            out.append(n)
        else:
            k2 = cfg[t]
            if k2 == k or k2 == OPP[k] or with_S2_perp:
                n = dict(cfg); n[s] = k2; n[t] = k
                out.append(n)
    if with_C:
        for pl in PLAQ:
            sites_g = [site(*p) for p in pl]
            occ = [i for i in range(4) if sites_g[i] in cfg]
            if len(occ) < 2:
                continue
            occ_local = [LOCAL[i] for i in occ]
            contents = tuple(cfg[sites_g[i]] for i in occ)
            for cand in moves_cached(occ_local, contents):
                n = dict(cfg)
                for i, kk in zip(occ, cand):
                    n[sites_g[i]] = kk
                out.append(n)
    return out

class UF:
    def __init__(self): self.p = {}
    def add(self, a): self.p.setdefault(a, a)
    def find(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]; a = p[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.p[ra] = rb

def run(N, with_S2_perp, with_C):
    uf = UF()
    cfgs = {}
    for occ in itertools.combinations(range(NS), N):
        for ks in itertools.product(range(4), repeat=N):
            cfg = dict(zip(occ, ks))
            c = code(cfg)
            uf.add(c); cfgs[c] = cfg
    for c, cfg in cfgs.items():
        for n in neighbours(cfg, with_S2_perp, with_C):
            uf.union(c, code(n))
    # sectors
    sect = defaultdict(lambda: defaultdict(list))
    for c, cfg in cfgs.items():
        P = [0,0]
        cnt = [0,0,0,0]
        for k in cfg.values():
            P[0] += E[k][0]; P[1] += E[k][1]; cnt[k] += 1
        sect[tuple(P)][uf.find(c)].append(tuple(cnt))
    return sect

def report(N, with_S2_perp, with_C):
    t0 = time.time()
    sect = run(N, with_S2_perp, with_C)
    tot_comp = sum(len(v) for v in sect.values())
    multi = {P: v for P, v in sect.items() if len(v) > 1}
    print(f'N={N} S2perp={with_S2_perp} C={with_C}: sectors(P)={len(sect)} components={tot_comp} '
          f'sectors_with_more_than_one_component={len(multi)}  ({time.time()-t0:.1f}s)')
    for P, v in sorted(multi.items())[:6]:
        sizes = sorted((len(m) for m in v.values()), reverse=True)
        # invariants: are x-mover / y-mover counts constant on each component?
        inv = []
        for m in v.values():
            xs = {c[0]+c[1] for c in m}; ys = {c[2]+c[3] for c in m}
            inv.append((sorted(xs), sorted(ys)))
        print('   P=', P, 'component sizes', sizes[:8], ' (x-mover-count, y-mover-count) per comp:', inv[:6])
    return sect

if __name__ == '__main__':
    print(f'torus {Lx}x{Lx}, N up to {NMAX}')
    for N in range(2, NMAX + 1):
        for flags in ((False, False), (False, True), (True, False), (True, True)):
            report(N, *flags)
