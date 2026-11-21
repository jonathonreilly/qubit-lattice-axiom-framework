# GUIDE only: check the period-2 line field with cuts on the torus (a, B).
import itertools, sys
from collections import deque
a, b1, b2, b3 = [int(v) for v in sys.argv[1].split(',')]
L = [a, b1, b2, b3]
def d_of(x):
    p = [c % 2 for c in x]
    if p[1] == p[2] == p[3]: return 0
    if p[0] == p[2] != p[3]: return 1
    if p[0] == p[3] != p[1]: return 2
    if p[0] == p[1] != p[2]: return 3
    raise Exception("not a partition")
sites = list(itertools.product(*[range(n) for n in L]))
def sh(x, mu, s=1):
    y = list(x); y[mu] = (y[mu] + s) % L[mu]; return tuple(y)
links = [(x, mu) for x in sites for mu in range(4)]
fixed = set()
cut = set()
for x in sites:
    mu = d_of(x)
    if (mu == 0 and x[0] == a - 1) or (mu > 0 and x[mu] == L[mu] - 1):
        cut.add((x, mu))
    else:
        fixed.add((x, mu))
# forest check: union-find on fixed links
par = {x: x for x in sites}
def find(x):
    while par[x] != x:
        par[x] = par[par[x]]; x = par[x]
    return x
cyc = 0
for (x, mu) in fixed:
    r1, r2 = find(x), find(sh(x, mu))
    if r1 == r2: cyc += 1
    else: par[r1] = r2
plaqs = []
for x in sites:
    for mu in range(4):
        for nu in range(mu + 1, 4):
            plaqs.append([(x, mu), (sh(x, nu), mu), (x, nu), (sh(x, mu), nu)])
bad = [p for p in plaqs if not any(l in cut for l in p) and sum(l in fixed for l in p) != 1]
D = set()
for (x, mu) in links:
    if (mu > 0 and x[0] in (0, a - 1)) or (mu == 0 and x[0] == a - 1): D.add((x, mu))
for p in plaqs:
    if any(l in cut and l[1] > 0 for l in p): D.update(p)
D.update(l for l in cut if l[1] > 0)
nbr = {}
for p in plaqs:
    free = [l for l in p if l not in fixed]
    for l in free:
        nbr.setdefault(l, set()).update(m for m in free if m != l)
degs = {}
for l in links:
    if l in fixed or l in D: continue
    degs[len(nbr.get(l, ()))] = degs.get(len(nbr.get(l, ())), 0) + 1
# distance from a mid-height plaquette (time j, spatial centre) to D through free links
j = a // 2
m = [n // 2 - 1 for n in L]
src = []
for mu in range(4):
    for nu in range(mu + 1, 4):
        base = [m[0], m[1], m[2], m[3]]; base[0] = j if (mu > 0) else j - 1
        x = tuple(base)
        p = [(x, mu), (sh(x, nu), mu), (x, nu), (sh(x, mu), nu)]
        src += [l for l in p if l not in fixed]
dist = {l: 0 for l in src}; dq = deque(src); dmin = None
while dq:
    l = dq.popleft()
    if l in D:
        dmin = dist[l]; break
    for k in nbr.get(l, ()):
        if k not in dist:
            dist[k] = dist[l] + 1; dq.append(k)
print("torus", L, "cycles in F:", cyc, "| imperfect plaquettes off cuts:", len(bad),
      "| degree histogram off D:", degs, "| BFS distance P->D:", dmin, "(claimed >=", j - 1, ")")
