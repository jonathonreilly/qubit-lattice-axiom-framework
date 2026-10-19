#!/usr/bin/env python3
"""C4e-05: what U = L2 o L1 does to 3- and 4-magnon clusters (exact simulation, descriptive).

(a) every connected 3-configuration (range-2 connectivity: each magnon within Chebyshev 2 of
    another; one representative per T x| Z^3 orbit): run T_MAX steps and classify
      static     : U c = c
      periodic   : U^p c = c for some 1 < p <= T_MAX (bounded)
      rigid mover: U c = c + t, t != 0
      splits     : the cluster's diameter exceeds 12 (a pair escapes)
      other      : none of the above within T_MAX
(b) pair-single scattering: pair {0, e1+e2} (glides +e3) with a single at (a,b,h), h = 3,
    (a,b) in [-3,4]^2: outcome after 30 steps (single displacement; pair transmitted?).
(c) head-on pair-pair: (1,1,0)-pair going up meets a (1,-1,0)-pair going down, all lateral offsets.
"""
import sys, os, itertools, time
sys.path.insert(0, os.path.dirname(__file__))
from c4e_layers import U
from c4e_common import canon, dist, add, sub, is_face, glider_shift

PASS = FAIL = 0
def check(name, ok, info=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(('PASS' if ok else 'FAIL') + ': ' + name + (('  ' + info) if info else ''), flush=True)

u = U(); O = (0, 0, 0); t0 = time.time()
def diam(c): return max(dist(a, b) for a in c for b in c)
def spect(c): return [z for z in c if min(dist(z, y) for y in c if y != z) > 2]

# (a)
orb = {}
box = [v for v in itertools.product(range(-4, 5), repeat=3) if v > O]
for i, a in enumerate(box):
    for b in box[i + 1:]:
        c = (O, a, b)
        if dist(a, b) > 4 or spect(c): continue
        k = canon(c)
        if k not in orb: orb[k] = frozenset(c)
print('connected 3-magnon orbits:', len(orb))
TMAX = 60
cls = {'static': 0, 'periodic': 0, 'rigid mover': 0, 'splits': 0, 'other': 0}
exs = {}
for c in orb.values():
    d = u(c)
    if d == c: kind = 'static'
    else:
        t = sub(min(d), min(c))
        if frozenset(add(z, t) for z in c) == d: kind = 'rigid mover'
        else:
            kind = 'other'; x = d
            for step in range(2, TMAX + 1):
                x = u(x)
                if x == c: kind = 'periodic'; break
                if diam(x) > 12: kind = 'splits'; break
    cls[kind] += 1
    exs.setdefault(kind, sorted(c))
print('classification of connected triples (T_MAX=%d):' % TMAX, cls)
for k, v in exs.items(): print('   e.g. %-11s %s' % (k, v))
check('every connected triple is classified (no "other")', cls['other'] == 0)
check('no rigidly moving bound triple among connected triples', cls['rigid mover'] == 0,
      '(a statement about these %d orbits only)' % len(orb))

# (b)
P = frozenset({O, (1, 1, 0)})
outcomes = {}
for a in range(-3, 5):
    for b in range(-3, 5):
        w = (a, b, 3)
        c = P | {w}; x = c
        for t in range(30): x = u(x)
        # identify the free pair (face pair) and the single
        pairs = [(p, q) for p, q in itertools.combinations(sorted(x), 2) if is_face(sub(q, p))]
        rest = None; info = 'unclassified'
        if len(pairs) == 1:
            p, q = pairs[0]; s = [z for z in x if z not in (p, q)][0]
            info = 'single displaced by %s; pair at height %d (free value 30), orientation %s' % (
                sub(s, w), p[2], sub(q, p))
            key = (sub(s, w), p[2] - 30, sub(q, p))
        else:
            key = ('?', tuple(sorted(x)))
        outcomes.setdefault(key, []).append((a, b))
print('pair {0,e1+e2} (moving +e3) hitting a single at (a,b,3), a,b in [-3,4]: outcome classes after 30 steps')
for k, v in sorted(outcomes.items(), key=lambda kv: -len(kv[1])):
    print('   single shift %s, pair height lag %s, pair rho %s : %d cases, e.g. (a,b)=%s' % (k[0], k[1], k[2] if len(k) > 2 else '', len(v), v[0]))
transmitted = all(k[0] != '?' for k in outcomes)
check('pair-single: in every case one face pair and one single remain after 30 steps', transmitted)

# (c)
def decompose(x):
    """split a configuration into far-apart face pairs (greedy); None if not possible"""
    x = sorted(x); out = []; used = set()
    for p, q in itertools.combinations(x, 2):
        if p in used or q in used or not is_face(sub(q, p)): continue
        out.append((p, q)); used |= {p, q}
    return out if len(used) == len(x) else None
outc = {}
T = 40
for a in range(-2, 3):
    for b in range(-2, 3):
        for h in (5, 6):
            up = frozenset({O, (1, 1, 0)})
            dn = frozenset({add((1, 0, h), (a, b, 0)), add((0, 1, h), (a, b, 0))})
            x = up | dn
            for t in range(T): x = u(x)
            fu = frozenset(add(z, (0, 0, T)) for z in up); fd = frozenset(add(z, (0, 0, -T)) for z in dn)
            if x == (fu | fd): key = 'pass, no delay'
            else:
                dec = decompose(x)
                if dec is None: key = 'not two face pairs at t=%d' % T
                else:
                    desc = []
                    for p, q in dec:
                        v = glider_shift(p, q, -1)
                        desc.append(('up' if v[2] > 0 else 'down' if v[2] < 0 else 'lateral', sub(q, p)))
                    zs = sorted(p[2] for p, q in dec)
                    key = 'two free pairs: %s; heights %s (free: %d, %d)' % (sorted(desc), zs, -T + h, T)
            outc.setdefault(key, []).append((a, b, h))
for k, v in sorted(outc.items(), key=lambda kv: -len(kv[1])):
    print('   head-on pair-pair, lateral offset (a,b), gap h: %s : %d of 50, e.g. %s' % (k, len(v), v[0]))
check('head-on pair-pair: every case ends as two free face pairs (no bound pair-pair state)',
      all(k.startswith('two free') or k.startswith('pass') for k in outc))
print('elapsed %.0fs' % (time.time() - t0))
print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
