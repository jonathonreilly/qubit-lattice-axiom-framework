"""Amended Test B (post-hoc, flagged): components per (N, P, Lz mod Ltorus) for V* and for the original clause."""
import sys, itertools, time
from collections import defaultdict
sys.argv = ['B', '4', '4']
import importlib.util
spec = importlib.util.spec_from_file_location('B', 'B_ergodic_2d.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)

def lz_mod(cfg):
    L = 0
    for s, k in cfg.items():
        x, y = B.xy(s)
        c = B.E[k]
        L += x * c[1] - y * c[0]
    return L % B.Lx

def run(N, s2perp, withC):
    uf = B.UF(); cfgs = {}
    for occ in itertools.combinations(range(B.NS), N):
        for ks in itertools.product(range(4), repeat=N):
            cfg = dict(zip(occ, ks)); c = B.code(cfg); uf.add(c); cfgs[c] = cfg
    viol = 0
    for c, cfg in cfgs.items():
        l0 = lz_mod(cfg)
        for n in B.neighbours(cfg, s2perp, withC):
            uf.union(c, B.code(n))
            if lz_mod(n) != l0: viol += 1
    comp = defaultdict(lambda: defaultdict(int))   # (P,L) -> root -> size
    for c, cfg in cfgs.items():
        P = [0,0]
        for k in cfg.values(): P[0] += B.E[k][0]; P[1] += B.E[k][1]
        comp[(tuple(P), lz_mod(cfg))][uf.find(c)] += 1
    return viol, comp

for N in (3, 4):
    for s2perp in (False, True):
        t0 = time.time()
        viol, comp = run(N, s2perp, True)
        ncomp = [len(v) for v in comp.values()]
        one = sum(1 for n in ncomp if n == 1)
        # is any component spread over several L mod 4 values? (compute by union over L keys)
        print(f'N={N} S2perp={s2perp}: Lz-mod-{B.Lx} changing events={viol}; (P,L) sectors={len(comp)}; '
              f'sectors with exactly 1 component={one}; max components in a sector={max(ncomp)}  ({time.time()-t0:.0f}s)')
        # generic sectors: exclude those with all-x or all-y movers (|P_x|==N or |P_y|==N)
        gen = [(k, v) for k, v in comp.items() if abs(k[0][0]) < N and abs(k[0][1]) < N]
        gen_one = sum(1 for k, v in gen if len(v) == 1)
        big_split = [(k, sorted(v.values(), reverse=True)[:4]) for k, v in gen if len(v) > 1][:5]
        print(f'    generic (not all-aligned) (P,L) sectors: {len(gen)}, with exactly 1 component: {gen_one}; examples with >1: {big_split}')
