"""Clean pair test for a half-edge BKSF code under the on-site action mu_d -> mu_{Rd}, nu_d -> nu_{Rd}."""
import sys
exec(open('majhalf.py').read().split("if __name__ == '__main__':")[0])
orders = list(itertools.permutations(range(6)))
Hh = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
from collections import defaultdict
classes = defaultdict(list)
for o in orders: classes[Hh[o]].append(o)
eps1 = tuple([1] * 12)
def wrap(p): return tuple(((c + L // 2) % L) - L // 2 for c in p)
def clean_pair(G, labB, M, x, o, mlist, tab):
    Rx = tuple(int(c) for c in M @ np.array(x))
    lo = tuple(min(x[i], Rx[i]) - 1 for i in range(3)); hi = tuple(max(x[i], Rx[i]) + 1 for i in range(3))
    cols = np.array(sorted({6 * s_(p) + t for p in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]) for t in range(6)}))
    rows, rhs = [], []
    for g, lb in zip(G, labB):
        cg = np.concatenate([g[1][cols], g[0][cols]])
        if not cg.any(): continue
        rows.append(cg); rhs.append(1 if (lb is not None and wrap(lb) in (wrap(x), wrap(Rx))) else 0)
    A = np.concatenate([np.array(rows, np.uint8), np.array(rhs, np.uint8)[:, None]], 1); m, nn = A.shape[0], 2 * len(cols)
    piv, r = [], 0
    for c in range(nn):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0: continue
        pr = r + nz[0]; A[[r, pr]] = A[[pr, r]]; rr = np.flatnonzero(A[:, c]); rr = rr[rr != r]; A[rr] ^= A[r]; piv.append(c); r += 1
        if r == m: break
    if A[r:, -1].any(): return 'no S'
    sol = np.zeros(nn, np.uint8)
    for i, c in enumerate(piv): sol[c] = A[i, -1]
    Sx = np.zeros(n, np.uint8); Sz = np.zeros(n, np.uint8); Sx[cols] = sol[:len(cols)]; Sz[cols] = sol[len(cols):]
    S = [Sx, Sz, int(Sx.astype(int) @ Sz.astype(int)) % 4]
    T = rb.mulp(rb.dag(S), map_pauli(S, M, eps1, o, mlist, tab))
    f = rb.phase_in_group(G, T)
    return None if f is None else {0: 1, 2: -1}.get(f, 'imag')
res = Counter()
nclass = int(sys.argv[2]) if len(sys.argv) > 2 else 2
for h, ords in list(classes.items())[:nclass]:
    o = ords[0]; mlist, tab = site_table(o)
    for sec in ((0, 0, 0), (1, 1, 1)):
        G = gens(o, sec)
        labB = []
        for v in V:
            labB.append(v); labB += [None] * 6
        for M in O:
            kd = bk.kind(M)
            if kd not in ('C2axis', 'C2edge'): continue
            xs = [x for x in itertools.product(range(-2, 3), repeat=3) if 2 <= max(abs(x[i] - int(c)) for i, c in enumerate(M @ np.array(x))) <= 3][:2]
            for x in xs:
                res[(o, sec, kd, clean_pair(G, labB, M, x, o, mlist, tab))] += 1
        print(dict(res), flush=True)
print('FINAL', dict(res))
