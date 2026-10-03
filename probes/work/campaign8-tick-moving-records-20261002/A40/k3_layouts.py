"""A40 k3: exhaust job layouts on the four roles (V, E, F, C) of A25's 2x2x2 layout (s = 0).
Supplied toy combinatorics.  Jobs: G (gravity content), L (light content), M (matter, may record).
Gravity forms (A25):  pair  = curl-split, content on V,E,F,C; lapse at V; shear h_ij at F
                      star  = (h,pi), content on V,F;  lapse at V; shear at F     (k2: hollow-star terms)
                      dual  = (h,pi) on the translate s+111: content on E,C; lapse at C; shear at E
Light forms:          link  = links on E, Gauss law at V (charges at V), plaquettes centred at F
                      dlink = links on F, Gauss law at C, plaquettes centred at E
                      ng-R  = non-gauge light (A39 (e) toy) on role R, no charge
Matter: any nonempty union of roles.
Coupling tests use real Z^3 sites: a matter hop is a pair of matter sites at Manhattan distance 1 or 2;
'X reach' = some single star (a site and its 6 neighbours) holds the hop's two ends and a site of role X.
"""
import itertools, signal
signal.alarm(28)
ROLES = ['V', 'E', 'F', 'C']
def role(y):
    w = sum(c % 2 for c in y)
    return ROLES[[0, 1, 2, 3].index(w)] if w in (0, 3) else ('E' if w == 1 else 'F')
NB = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
BOX = [y for y in itertools.product(range(-3, 4), repeat=3)]
def star(z):
    return [tuple(z[k] + d[k] for k in range(3)) for d in NB]

def man(a, b):
    return sum(abs(a[k] - b[k]) for k in range(3))

GRAV = {'pair': ({'V', 'E', 'F', 'C'}, 'V', 'F'), 'star': ({'V', 'F'}, 'V', 'F'), 'dual': ({'E', 'C'}, 'C', 'E')}
LIGHT = {'link': ({'E'}, 'V'), 'dlink': ({'F'}, 'C')}
for R in ROLES:
    LIGHT['ng-' + R] = ({R}, None)

def hops(M):
    # matter hops touching the origin cell, inside the box
    out = []
    base = [y for y in itertools.product((0, 1), repeat=3) if role(y) in M]
    for x in base:
        for y in BOX:
            if role(y) in M and 1 <= man(x, y) <= 2:
                out.append((x, y))
    return out

_cache = {}
def ok_hop(x, y, Xs):
    key = (tuple(c % 2 for c in x), tuple(y[k] - x[k] for k in range(3)), tuple(Xs))
    if key not in _cache:
        sx = set(star(x)); sy = set(star(y))
        cent = [z for z in sx if z in sy]          # stars holding both ends
        if SAME[0]:   # one common star must hold a site of every role in Xs
            _cache[key] = any(all(any(role(u) == X for u in star(z)) for X in Xs) for z in cent)
        else:         # each role in Xs in some common star (first-order split coupling)
            _cache[key] = all(any(any(role(u) == X for u in star(z)) for z in cent) for X in Xs)
    return _cache[key]
SAME = [False]

def reach(M, Xs):
    """True if the matter hops that pass the star test for every role in Xs connect every matter
    class of the cell to every other and to its own translates by 2e_x, 2e_y, 2e_z (3D-connected)."""
    sites = [y for y in itertools.product(range(-2, 4), repeat=3) if role(y) in M]
    S = set(sites)
    adj = {y: [] for y in sites}
    for x in sites:
        for d in itertools.product(range(-2, 3), repeat=3):
            m = sum(abs(c) for c in d)
            if 1 <= m <= 2:
                y = tuple(x[k] + d[k] for k in range(3))
                if y in S and ok_hop(x, y, Xs):
                    adj[x].append(y)
    base = [y for y in itertools.product((0, 1), repeat=3) if role(y) in M]
    start = base[0]
    seen = {start}; todo = [start]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); todo.append(v)
    need = base + [tuple(b[k] + 2 * (k == a) for k in range(3)) for b in base for a in range(3)]
    return all(t in seen for t in need)

rows = []
for gname, (gsup, lapse, shear) in GRAV.items():
    for lname, (lsup, gauss) in LIGHT.items():
        for k in range(1, 5):
            for M in itertools.combinations(ROLES, k):
                M = set(M)
                jobs = {R: ''.join(j for j, S in (('G', gsup), ('L', lsup), ('M', M)) if R in S) for R in ROLES}
                d10 = all(not ('M' in jobs[R] and len(jobs[R]) > 1) for R in ROLES)
                lg_share = any('G' in jobs[R] and 'L' in jobs[R] for R in ROLES)
                charged = gauss is not None and gauss in M
                hl = hops(M)
                lap = reach(M, [lapse])
                shr = reach(M, [lapse, shear])
                SAME[0] = True; _cache.clear()
                sho = reach(M, [lapse, shear])
                SAME[0] = False; _cache.clear()
                adj = any(man(x, y) == 1 for x, y in hl)
                buffers = [R for R in ROLES if jobs[R] == '']
                rows.append((gname, lname, ''.join(sorted(M, key=ROLES.index)), d10, lg_share, charged, lap, shr, adj,
                             jobs, buffers, sho))
print("combinations:", len(rows))
def show(r):
    g, l, m, d10, lg, ch, lap, shr, adj, jobs, buf, sho = r
    return (f"  grav={g:5s} light={l:6s} matter={m:5s} | D10 place-wise={d10!s:5s} light&grav share={lg!s:5s} "
            f"charged={ch!s:5s} lapse-reach={lap!s:5s} lapse,shear split={shr!s:5s} lapse+shear one star={sho!s:5s} matter-adjacent={adj!s:5s} | "
            f"jobs " + ' '.join(f"{R}:{jobs[R] or '-'}" for R in ROLES))
A = [r for r in rows if r[3] and r[5] and r[6]]
print("(1) place-wise D10 + charged matter + lapse reach:", len(A))
B = [r for r in rows if r[3] and r[5]]
print("(2) place-wise D10 + charged matter (no reach demand):", len(B))
for r in B: print(show(r))
C = [r for r in rows if r[3] and r[6] and r[7] and not r[4]]
print("(3) place-wise D10 + lapse and shear reach (split, first order) + light not sharing with gravity (any light form):", len(C))
for r in C: print(show(r))
Dd = [r for r in rows if r[5] and r[6] and r[7] and r[11] and not r[4]]
print("(4) charged + lapse and shear in one star + light not sharing with gravity, matter may share (factor-wise D10):", len(Dd))
for r in Dd: print(show(r))
E3 = [r for r in rows if r[3] and r[11] and not r[4]]
print("(3b) place-wise D10 + lapse and shear in ONE star with each hop (all-orders product) + light not sharing:", len(E3))
for r in E3: print(show(r))
print("(5) does any layout with gravity on a checkerboard (star/dual) and matter disjoint from gravity have",
      "adjacent matter places?",
      any(r[8] for r in rows if r[0] in ('star', 'dual') and not any('G' in r[9][R] and 'M' in r[9][R] for R in ROLES)))
