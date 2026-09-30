import sys, itertools
sys.argv = ['B','4','4']
import importlib.util
from collections import defaultdict
spec = importlib.util.spec_from_file_location('B', 'B_ergodic_2d.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
def lz_mod(cfg):
    L = 0
    for s, k in cfg.items():
        x, y = B.xy(s); c = B.E[k]; L += x*c[1] - y*c[0]
    return L % B.Lx
for N in (3, 4):
    uf = B.UF(); cfgs = {}
    for occ in itertools.combinations(range(B.NS), N):
        for ks in itertools.product(range(4), repeat=N):
            cfg = dict(zip(occ, ks)); c = B.code(cfg); uf.add(c); cfgs[c] = cfg
    for c, cfg in cfgs.items():
        for n in B.neighbours(cfg, False, True):
            uf.union(c, B.code(n))
    sec = defaultdict(lambda: defaultdict(int))
    for c, cfg in cfgs.items():
        P = [0,0]
        for k in cfg.values(): P[0] += B.E[k][0]; P[1] += B.E[k][1]
        sec[(tuple(P), lz_mod(cfg))][uf.find(c)] += 1
    fr = []
    for (P, L), v in sec.items():
        if abs(P[0]) == N or abs(P[1]) == N: continue     # skip all-aligned sectors
        tot = sum(v.values()); fr.append((max(v.values())/tot, P, L, len(v)))
    fr.sort()
    print(f'N={N}: generic (P,Lz mod 4) sectors {len(fr)}; largest-component fraction: min {fr[0][0]:.3f} (P={fr[0][1]}, L={fr[0][2]}), median {fr[len(fr)//2][0]:.3f}, max {fr[-1][0]:.3f}')
    tot_all = sum(sum(v.values()) for k, v in sec.items() if not (abs(k[0][0]) == N or abs(k[0][1]) == N))
    print('   states in generic sectors', tot_all, ' in largest components', sum(max(v.values()) for k, v in sec.items() if not (abs(k[0][0]) == N or abs(k[0][1]) == N)))
