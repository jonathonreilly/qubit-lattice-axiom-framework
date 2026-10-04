"""A54 c1b: translation-invariant version of c1 (uniform record background; B invariant under the
coarse translations).  Unknowns = translation orbits of unordered link pairs within range.
Usage: c1b_ti_scan.py L R2a,R2b,... [fermion|boson]"""
import signal, sys, time
signal.alarm(118)
from a54lib import *

L = int(sys.argv[1]); R2s = [int(t) for t in sys.argv[2].split(',')]
kind = sys.argv[3] if len(sys.argv) > 3 else 'fermion'
tor, recs, hops, dcol, loops, dp, Ddp = setup((L, L, L), 0, 'uniform')
n = tor.n; P = tor.P
if kind == 'boson':                     # translation-invariant bosonic control: B0 = fixed pattern, range^2 <= 4
    import random
    random.seed(3)
    pick = {}
    def okey(l, m):
        out = []
        for a, b in ((l, m), (m, l)):
            xa = tor.links[a]; xb = tor.links[b]
            typ = [k for k in range(3) if xa[k] % 2][0]
            off = tuple((xb[k] - xa[k]) % P[k] for k in range(3))
            out.append((typ, off))
        return min(out)
    B0 = [0] * n
    for l in range(n):
        for m in range(n):
            if l < m and link_d2(tor, l, m) <= 4:
                k = okey(l, m)
                if k not in pick: pick[k] = random.random() < 0.5
                if pick[k]:
                    B0[l] |= 1 << m; B0[m] |= 1 << l
    dcol = B0
    Ddp = []
    for m in dp:
        z = 0
        for l in bits_of(m): z ^= dcol[l]
        Ddp.append(z)
def orbit_key(l, m):
    out = []
    for a, b in ((l, m), (m, l)):
        xa = tor.links[a]; xb = tor.links[b]
        typ = [k for k in range(3) if xa[k] % 2][0]
        off = tuple((xb[k] - xa[k]) % P[k] for k in range(3))
        out.append((typ, off))
    return min(out)
origin_p = [k for k, pq in enumerate(tor.plaqs) if pq[0] == (0, 0, 0)]
D2 = {}
print("TI scan, torus %d^3, hops %s, uniform records" % (L, kind))
for R2 in R2s:
    t0 = time.time()
    keys = {}
    S = GF2()
    for p in origin_p:
        for q in range(len(dp)):
            if q == p: continue
            row = popc(dp[q] & Ddp[p]) & 1
            for l in bits_of(dp[q]):
                for m in bits_of(dp[p]):
                    if l == m: continue
                    if link_d2(tor, l, m) > R2: continue
                    k = orbit_key(l, m)
                    if k not in keys: keys[k] = len(keys) + 1
                    row ^= 1 << keys[k]
            if row: S.add(row)
    print("  R2 <= %3d: orbit unknowns %5d, equations %6d, rank %5d, inconsistent %4d -> %s (%.1f s)" % (
        R2, len(keys), S.neq, S.rank(), S.incons, 'SOLVABLE' if S.incons == 0 else 'no solution', time.time() - t0))
    sys.stdout.flush()
print("done")
