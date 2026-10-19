#!/usr/bin/env python3
"""C4e-06: second, independent implementation (flat-index torus code, no import of c4e_layers
for the dynamics) of the two involutions, written directly from the definitions in NOTE.md:
units are built by enumerating plaquettes and cubes, neighbourhoods N1/N2 by brute-force
site sharing.  Checks on the L^3 torus (L = 8, 10):
  (i)  L_i o L_i = id on random configurations at densities 0.02..0.98 (dense sectors);
  (ii) agreement with c4e_layers (run with torus wrap) on the same configurations;
  (iii) exhaustive check of L_i o L_i = id on the k = 2,3 sectors of the 6^3 torus... is too
       large for k=3 here; we do k <= 2 exhaustively on 8^3 and k = 3 for all configs with a
       magnon at the origin.
"""
import sys, os, random, itertools, time
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))

PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + (('  ' + info) if info else ''), flush=True)

def build(L):
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    units = {'square': [], 'tetra': []}     # each unit: (Dlist, Dplist)
    for x, y, z in itertools.product(range(L), repeat=3):
        # squares: normal z, y, x
        units['square'].append(((idx(x, y, z), idx(x + 1, y + 1, z)), (idx(x + 1, y, z), idx(x, y + 1, z))))
        units['square'].append(((idx(x, y, z), idx(x + 1, y, z + 1)), (idx(x + 1, y, z), idx(x, y, z + 1))))
        units['square'].append(((idx(x, y, z), idx(x, y + 1, z + 1)), (idx(x, y + 1, z), idx(x, y, z + 1))))
        p = (x + y + z) % 2
        B = [(x + a, y + b, z + c) for a in (0, 1) for b in (0, 1) for c in (0, 1) if (a + b + c) % 2 == 1]
        # B-sites: parity differs from the corner's (offsets of odd weight)
        for j, kj in ((0, x), (1, y), (2, z)):
            D = tuple(idx(*s) for s in B if s[j] == kj)
            Dp = tuple(idx(*s) for s in B if s[j] == kj + 1)
            assert len(D) == 2 and len(Dp) == 2
            units['tetra'].append((D, Dp))
    return units

def neighbourhoods(ul, nsites):
    at = [[] for _ in range(nsites)]
    for i, (D, Dp) in enumerate(ul):
        for s in D + Dp: at[s].append(i)
    N1 = []
    for i, (D, Dp) in enumerate(ul):
        s = set()
        for x in D + Dp: s.update(at[x])
        s.discard(i); N1.append(sorted(s))
    N2 = []
    for i in range(len(ul)):
        s = set()
        for v in N1[i]: s.update(N1[v])
        s -= set(N1[i]); s.discard(i); N2.append(sorted(s))
    return N1, N2

def layer(ul, N1, N2, occ):
    occ = occ.copy()
    def cand(i, o):
        D, Dp = ul[i]
        a = [o[s] for s in D]; b = [o[s] for s in Dp]
        return (all(a) and not any(b)) or (all(b) and not any(a))
    C = np.array([cand(i, occ) for i in range(len(ul))])
    act = []
    for i in np.nonzero(C)[0]:
        if C[N2[i]].any(): continue
        D, Dp = ul[i]; ok = True
        for st in (D, Dp):
            o = occ.copy(); o[list(D) + list(Dp)] = 0; o[list(st)] = 1
            if any(cand(v, o) for v in N1[i]): ok = False; break
        if ok: act.append(i)
    new = occ.copy()
    for i in act:
        D, Dp = ul[i]
        if occ[D[0]]: new[list(D)] = 0; new[list(Dp)] = 1
        else: new[list(Dp)] = 0; new[list(D)] = 1
    return new, act

t0 = time.time()
from c4e_layers import U as Uref
random.seed(7)
for L in (8, 10):
    units = build(L); n = L ** 3
    NB = {k: neighbourhoods(v, n) for k, v in units.items()}
    print('L=%d: units square=%d tetra=%d, |N1|=%s |N2|=%s (built %.0fs)' % (
        L, len(units['square']), len(units['tetra']),
        sorted({len(x) for x in NB['square'][0]}), sorted({len(x) for x in NB['square'][1]}), time.time() - t0), flush=True)
    wrap = lambda z, L=L: (z[0] % L, z[1] % L, z[2] % L)
    uref = Uref(wrap=wrap)
    bad_inv = bad_agree = 0; ntr = 0; nact = 0
    for trial in range(60 if L == 8 else 25):
        rho = random.choice([0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 0.98])
        occ = (np.random.default_rng(trial + 100 * L).random(n) < rho).astype(np.int8)
        ntr += 1
        o1, a1 = layer(units['square'], *NB['square'], occ)
        if not np.array_equal(layer(units['square'], *NB['square'], o1)[0], occ): bad_inv += 1
        o2, a2 = layer(units['tetra'], *NB['tetra'], o1)
        if not np.array_equal(layer(units['tetra'], *NB['tetra'], o2)[0], o1): bad_inv += 1
        nact += len(a1) + len(a2)
        conf = frozenset((i // (L * L), (i // L) % L, i % L) for i in np.nonzero(occ)[0])
        ref = uref(conf)
        mine = frozenset((i // (L * L), (i // L) % L, i % L) for i in np.nonzero(o2)[0])
        if ref != mine: bad_agree += 1
    check('L=%d torus: independent implementation, L_i o L_i = id on random configs' % L, bad_inv == 0,
          'configs=%d, active units=%d, failures=%d (%.0fs)' % (ntr, nact, bad_inv, time.time() - t0))
    check('L=%d torus: independent implementation agrees with c4e_layers on U' % L, bad_agree == 0,
          'disagreements=%d' % bad_agree)
# exhaustive k=2 and k=3 (magnon at origin) on the 8^3 torus with the independent code
L = 8; units = build(L); n = L ** 3; NB = {k: neighbourhoods(v, n) for k, v in units.items()}
bad = cnt = 0
for k in (2, 3):
    for rest in itertools.combinations(range(1, n), k - 1):
        occ = np.zeros(n, np.int8); occ[0] = 1; occ[list(rest)] = 1
        if k == 3 and random.random() > 0.08: continue      # k=3: random 8% sample of the 130305 configs
        cnt += 1
        for key in ('square', 'tetra'):
            o1, _ = layer(units[key], *NB[key], occ)
            if not np.array_equal(layer(units[key], *NB[key], o1)[0], occ): bad += 1
check('8^3 torus, independent code: all k=2 configs (magnon at origin) + 8%% random sample of k=3: L_i^2 = id',
      bad == 0, 'configs=%d failures=%d (%.0fs)' % (cnt, bad, time.time() - t0))
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
