"""A54 c2: the record-free core of Theorem L.  Gauss-parity-dressed hops t_l = X_l prod_{v in c_l} G_v on a
D-dimensional periodic corner lattice; demand exact fermionic commutation (anticommute iff exactly one
shared corner):  <dl, c_m> + <dm, c_l> = |dl cap dm| mod 2  for all links l != m.
Unknowns c_l(v) for corners v within distance^2 <= R2/4 of the link midpoint (doubled coordinates).
Prints the smallest range that admits a solution on each torus.  Usage: c2_gauss_core.py D L1,L2,..."""
import signal, sys, time, itertools
signal.alarm(118)
sys.path.insert(0, '.')
from a54lib import GF2

D = int(sys.argv[1]); sizes = [int(t) for t in sys.argv[2].split(',')]
for L in sizes:
    t0 = time.time()
    corners = list(itertools.product(range(L), repeat=D)); cid = {c: k for k, c in enumerate(corners)}
    links = []
    for c in corners:
        for a in range(D):
            w = list(c); w[a] = (w[a] + 1) % L
            links.append((cid[c], cid[tuple(w)], tuple(2 * x + (1 if k == a else 0) for k, x in enumerate(c))))
    n = len(links)
    def d2(x, y):                                   # doubled coordinates, period 2L
        s = 0
        for a, b in zip(x, y):
            t = abs(a - b) % (2 * L); t = min(t, 2 * L - t); s += t * t
        return s
    cdbl = [tuple(2 * x for x in c) for c in corners]
    allR2 = sorted({d2(links[l][2], cdbl[v]) for l in range(n) for v in range(len(corners))})
    found = None
    for R2 in allR2:
        var = {}
        order = sorted(((max(l, 0), v, l) for l in range(n) for v in range(len(corners))
                        if d2(links[l][2], cdbl[v]) <= R2))
        for k, (_, v, l) in enumerate(order):
            var[(l, v)] = k + 1
        S = GF2()
        for l in range(n):
            for m in range(l + 1, n):
                el = {links[l][0], links[l][1]}; em = {links[m][0], links[m][1]}
                row = (len(el & em) % 2) if len(el) == 2 and len(em) == 2 else 0
                for v in el:
                    k = var.get((m, v))
                    if k: row ^= 1 << k
                for v in em:
                    k = var.get((l, v))
                    if k: row ^= 1 << k
                if row: S.add(row)
        if S.incons == 0:
            found = R2; break
    print("D=%d torus L=%d: links %d; smallest range^2 (doubled units) admitting a solution: %s of max %d; "
          "unknowns there %d (%.1f s)" % (D, L, n, found, allR2[-1], len(var), time.time() - t0))
    sys.stdout.flush()
print("done")
