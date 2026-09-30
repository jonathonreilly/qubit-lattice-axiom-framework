import glob, math, random
import numpy as np
from analyze import load, summarize
S = summarize(load(glob.glob('runs/*.csv')))
def series(c, L):
    pts = sorted((k[1], v) for k, v in S.items() if k[0]==c and k[2]==1.0 and k[3]==2.0 and k[4]==L)
    return pts
def crossing(c, L1, L2, nboot=400, rng=random.Random(1)):
    a = {p:v for p,v in series(c,L1)}; b = {p:v for p,v in series(c,L2)}
    ps = sorted(set(a)&set(b))
    if len(ps) < 2: return None
    def cross(sampler):
        d = []
        for p in ps:
            qa = sampler(a[p]); qb = sampler(b[p]); d.append(qa-qb)   # Q(L1)-Q(L2): >0 in disordered? Q_small L larger
        # crossing of d through zero (sign change) with linear interpolation; pick the first sign change from the low-p side
        xs = []
        for i in range(len(ps)-1):
            if d[i]*d[i+1] < 0:
                xs.append(ps[i] + (ps[i+1]-ps[i])*d[i]/(d[i]-d[i+1]))
        return xs
    base = cross(lambda v: v['Q'])
    boots = []
    for _ in range(nboot):
        xs = cross(lambda v: rng.gauss(v['Q'], v['Q_se']))
        if xs: boots.append(xs[0])
    return base, (np.mean(boots), np.std(boots)) if boots else None
for c in 'UEAS':
    print('== clause', c)
    for L in (6,8,12,16):
        pts = series(c, L)
        if pts: print(' L=%d: '%L + ' '.join(f"p={p:g}:Q={v['Q']:.3f}" for p,v in pts))
    for (L1,L2) in [(6,8),(8,12),(12,16),(8,16)]:
        r = crossing(c, L1, L2)
        if r: print(f'  crossing L{L1}/L{L2}: first={r[0]}, boot(mean,sd)={r[1]}')
