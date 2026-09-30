"""T17 Test A: which events on a cluster keep N, P and L exactly, one record per site?

Configuration: occupied subset of cluster sites, content in axis unit vectors.
Invariants: P = sum c, L = sum x cross c (x = position in the cluster frame).
Class = same occupied set, same (P, L).  Any permutation inside a class keeps
N, P, L, and (unit speeds) kinetic energy.

We compare three event families, by union-find on the configurations of a cluster:
  bond    : two-record events on adjacent sites only (distance 1)
  pair    : two-record events on adjacent OR planar-diagonal pairs (distance 1, sqrt 2)
  full    : the whole class (any number of records changing at once)
and report how many configurations are moved at all by each family.
"""
import itertools, json, sys
from collections import defaultdict
import numpy as np

E3 = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
E2 = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def dist2(a, b):
    return sum((a[i]-b[i])**2 for i in range(3))

CLUSTERS = {
    'bond':      [(0,0,0),(1,0,0)],
    'diag2d':    [(0,0,0),(1,1,0)],
    'bodydiag':  [(0,0,0),(1,1,1)],
    'line3':     [(0,0,0),(1,0,0),(2,0,0)],
    'ltriple':   [(0,0,0),(1,0,0),(0,1,0)],
    'plaquette': [(0,0,0),(1,0,0),(0,1,0),(1,1,0)],
    'cube':      [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)],
}

class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb

def census_one(name, xs, contents, maxdist2_pair):
    out = []
    occ = list(range(len(xs)))
    if True:
        configs = list(itertools.product(contents, repeat=len(occ)))
        idx = {c: k for k, c in enumerate(configs)}
        # invariants
        def inv(cfg):
            P = (0,0,0); L = (0,0,0)
            for x, c in zip(xs, cfg):
                P = add(P, c); L = add(L, cross(x, c))
            return P, L
        classes = defaultdict(list)
        for k, c in enumerate(configs):
            classes[inv(c)].append(k)
        # families
        ufs = {'bond': UF(len(configs)), 'pair': UF(len(configs)), 'full': UF(len(configs))}
        for key, members in classes.items():
            for m in members[1:]:
                ufs['full'].union(members[0], m)
        # pair-level events
        for k, c in enumerate(configs):
            for a in range(len(occ)):
                for b in range(a+1, len(occ)):
                    d2 = dist2(xs[a], xs[b])
                    fams = []
                    if d2 == 1:
                        fams = ['bond', 'pair']
                    elif d2 <= maxdist2_pair:
                        fams = ['pair']
                    else:
                        continue
                    Pab = add(c[a], c[b]); Lab = add(cross(xs[a], c[a]), cross(xs[b], c[b]))
                    for u in contents:
                        for v in contents:
                            if add(u, v) == Pab and add(cross(xs[a], u), cross(xs[b], v)) == Lab:
                                c2 = list(c); c2[a] = u; c2[b] = v; c2 = tuple(c2)
                                for f in fams:
                                    ufs[f].union(k, idx[c2])
        def moved(uf):
            comp = defaultdict(int)
            for k in range(len(configs)):
                comp[uf.find(k)] += 1
            return sum(s for s in comp.values() if s > 1), sum(1 for s in comp.values() if s > 1), max(comp.values())
        res = {'cluster': name, 'occ': [list(x) for x in xs], 'N': len(occ), 'configs': len(configs),
               'classes': len(classes), 'classes_gt1': sum(1 for m in classes.values() if len(m) > 1),
               'max_class': max(len(m) for m in classes.values())}
        for f in ('bond', 'pair', 'full'):
            mv, nc, mx = moved(ufs[f])
            res[f] = {'configs_moved': mv, 'orbits_gt1': nc, 'max_orbit': mx}
        out.append(res)
    return out


def run():
    import time
    t0 = time.time()
    allres = []
    for name, sites in CLUSTERS.items():
        for cname, contents in (('3D', E3), ('2D', E2)):
            if cname == '2D' and any(s[2] != 0 for s in sites):
                continue
            n = len(sites)
            maxn = 4 if name == 'cube' else n
            for mask in range(1, 1 << n):
                k = bin(mask).count('1')
                if k < 2 or k > maxn:
                    continue
                xs = [sites[i] for i in range(n) if mask >> i & 1]
                for r in census_one(name, xs, contents, 2):
                    r['contents'] = cname
                    allres.append(r)
    json.dump(allres, open('A_results.json', 'w'))
    agg = defaultdict(lambda: {'subsets': 0, 'configs': 0, 'bond_moved': 0, 'pair_moved': 0, 'full_moved': 0,
                               'pair_gt_bond': 0, 'full_gt_pair': 0, 'max_orbit_full': 0})
    for r in allres:
        key = (r['cluster'], r['contents'], r['N'])
        a = agg[key]
        a['subsets'] += 1
        a['configs'] += r['configs']
        a['bond_moved'] += r['bond']['configs_moved']
        a['pair_moved'] += r['pair']['configs_moved']
        a['full_moved'] += r['full']['configs_moved']
        a['max_orbit_full'] = max(a['max_orbit_full'], r['full']['max_orbit'])
        if r['pair']['configs_moved'] > r['bond']['configs_moved']:
            a['pair_gt_bond'] += 1
        if r['full']['configs_moved'] > r['pair']['configs_moved'] or r['full']['orbits_gt1'] != r['pair']['orbits_gt1'] or r['full']['max_orbit'] != r['pair']['max_orbit']:
            a['full_gt_pair'] += 1
    print('cluster contents N | #occupancy-subsets configs | configs moved: bond pair full | #subsets pair>bond, full>pair | max full orbit')
    for key in sorted(agg):
        a = agg[key]
        print(key, a['subsets'], a['configs'], '|', a['bond_moved'], a['pair_moved'], a['full_moved'], '|',
              a['pair_gt_bond'], a['full_gt_pair'], '|', a['max_orbit_full'])
    print('time', round(time.time() - t0, 1), 's')

if __name__ == '__main__':
    run()
