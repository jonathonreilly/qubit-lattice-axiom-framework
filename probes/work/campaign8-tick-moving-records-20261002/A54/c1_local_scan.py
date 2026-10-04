"""A54 c1: is there a bounded-range quadratic chi with chi X^{dp} chi = S_p on the charge-free sector?
GF(2) system (weakest local form, allows any Gauss/cocycle correction):
    <dq, (B + d) dp> = 0  for all plaquette pairs p < q,   B symmetric, B_lm = 0 unless |x_l - x_m|^2 <= R2.
Diagonal of B = 0 (+-1 chi) unless 'z4' (S gates allowed).
Usage: c1_local_scan.py Lx,Ly,Lz R2a,R2b,... [uniform|random] [fermion|boson|ferm+conj] [z4]"""
import signal, sys, time
signal.alarm(118)
from a54lib import *

shape = tuple(int(t) for t in sys.argv[1].split(','))
R2spec = sys.argv[2]
rk = sys.argv[3] if len(sys.argv) > 3 else 'uniform'
kind = sys.argv[4] if len(sys.argv) > 4 else 'fermion'
z4 = len(sys.argv) > 5 and sys.argv[5] == 'z4'
tor, recs, hops, dcol, loops, dp, Ddp = setup(shape, 0, rk, seed=11)
n = tor.n; NP = len(dp)
rank_of = {l: r for r, l in enumerate(sorted(range(n), key=lambda l: tor.links[l][::-1]))}
D2 = [[link_d2(tor, l, m) for m in range(n)] for l in range(n)]
if kind != 'fermion':
    # bosonic control: hops X_l Z^{B0 e_l} with B0 random symmetric, zero diagonal, range^2 <= 4
    rng = np.random.default_rng(5)
    B0 = [0] * n
    for l in range(n):
        for m in range(l + 1, n):
            if D2[l][m] <= 4 and rng.random() < 0.5:
                B0[l] |= 1 << m; B0[m] |= 1 << l
    dcol = B0 if kind == 'boson' else [a ^ b for a, b in zip(dcol, B0)]
    Ddp = []
    for m in dp:
        z = 0
        for l in bits_of(m):
            z ^= dcol[l]
        Ddp.append(z)
# sanity: d + d^T = D^T D  (fermion)  or 0 (boson)
viol = 0
for l in range(n):
    vl, _, wl, _ = tor.ends(l)
    for m in range(n):
        if m == l: continue
        vm, _, wm, _ = tor.ends(m)
        shared = len({vl, wl} & {vm, wm}) % 2
        want = 0 if kind == 'boson' else shared
        viol += (((dcol[l] >> m) & 1) ^ ((dcol[m] >> l) & 1)) != want
print("torus %s, records %s, hops %s%s: links %d, plaquettes %d; d + d^T check violations %d" % (
    shape, rk, kind, ' (Z4 chi allowed)' if z4 else '', n, NP, viol))
pl_of = plaqs_of_links(tor, dp)
R2s = sorted({D2[l][m] for l in range(n) for m in range(n) if l != m}) if R2spec == 'auto' else [int(t) for t in R2spec.split(',')]
for R2 in R2s:
    t0 = time.time()
    var = {}
    pairs = sorted(((max(rank_of[l], rank_of[m]), min(rank_of[l], rank_of[m]), l, m)
                    for l in range(n) for m in range(n) if (l < m and D2[l][m] <= R2) or (z4 and l == m)))
    for k, (_, _, l, m) in enumerate(pairs):
        var[(l, m)] = k + 1
    nb = {l: [m for m in range(n) if m != l and D2[l][m] <= R2] for l in range(n)}
    S = GF2(); maxneed = 0
    for p in range(NP):
        cand = set()
        for m in bits_of(dp[p]):
            for l in nb[m] + [m]:
                cand.update(pl_of[l])
        for l in bits_of(Ddp[p]):
            cand.update(pl_of[l])
        for q in cand:
            if q <= p: continue
            row = popc(dp[q] & Ddp[p]) & 1
            for l in bits_of(dp[q]):
                for m in bits_of(dp[p]):
                    key = (min(l, m), max(l, m))
                    k = var.get(key)
                    if k is not None:
                        row ^= 1 << k
            if row:
                S.add(row)
    # also the far equations: rhs must vanish where no unknown reaches (counted inside cand already)
    print("  R2 <= %2d: unknowns %6d, equations %6d, rank %6d, inconsistent rows %5d -> %s  (%.1f s)" % (
        R2, len(var), S.neq, S.rank(), S.incons, 'SOLVABLE' if S.incons == 0 else 'no solution', time.time() - t0))
    sys.stdout.flush()
    if R2spec == 'auto' and S.incons == 0:
        print('  threshold R2 = %d (torus max %d)' % (R2, max(R2s))); break
print("done")
