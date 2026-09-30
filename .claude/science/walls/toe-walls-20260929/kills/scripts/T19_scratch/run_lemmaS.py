"""Driver for Test A with independent verification of every SAT model."""
import sys, itertools, time, numpy as np
import sat_lemmaS as M

def verify(dims, r, model):
    n = 1
    for d in dims: n *= d
    coords = list(itertools.product(*[range(d) for d in dims]))
    idx = {c: i for i, c in enumerate(coords)}
    nmaj = 2 * n; ref = 0
    a = np.zeros((nmaj, 2 * n), dtype=np.uint8)
    for (u, q, t), val in model.items():
        if val: a[u, t * n + q] = 1
    # exact algebra: omega(a_u,a_v)=1 for all u!=v (both != ref); a_ref=0
    for u in range(nmaj):
        for v in range(u + 1, nmaj):
            w = int((a[u, :n] @ a[v, n:] + a[u, n:] @ a[v, :n]) % 2)
            want = 0 if (u == ref or v == ref) else 1
            assert w == want, (u, v, w)
    # bilinear images and their pairwise commutation must equal |{u,v} & {w,x}| mod 2 for all NN generators
    def img(u, v): return (a[u] ^ a[v])
    pairs = []
    for s, c in enumerate(coords):
        pairs.append((2 * s, 2 * s + 1))
        for ax in range(len(dims)):
            c2 = list(c); c2[ax] += 1; c2 = tuple(c2)
            if c2 in idx:
                tt = idx[c2]
                for i in (0, 1):
                    for j in (0, 1): pairs.append((2 * s + i, 2 * tt + j))
    maxr = 0
    for (u, v) in pairs:
        p = img(u, v)
        supp = [q for q in range(n) if p[q] or p[n + q]]
        cs = [coords[u // 2], coords[v // 2]]
        lo = [min(c[i] for c in cs) for i in range(len(dims))]; hi = [max(c[i] for c in cs) for i in range(len(dims))]
        for q in supp:
            d = max(max(lo[i] - coords[q][i], coords[q][i] - hi[i], 0) for i in range(len(dims)))
            maxr = max(maxr, d)
    for (u, v), (x, y) in itertools.combinations(pairs, 2):
        w = int((img(u, v)[:n] @ img(x, y)[n:] + img(u, v)[n:] @ img(x, y)[:n]) % 2)
        assert w == len({u, v} & {x, y}) % 2
    return maxr, len(pairs)

if __name__ == '__main__':
    cases = [tuple(map(int, s.split('x'))) for s in sys.argv[1].split(',')]
    rs = list(map(int, sys.argv[2].split(',')))
    for dims in cases:
        for r in rs:
            t0 = time.time()
            out = M.solve(dims, r)
            line = f"dims={'x'.join(map(str, dims))} r={r}: {out[0]}"
            if out[0] == 'SAT':
                maxr, npairs = verify(dims, r, out[3])
                line += f"  (verified: exact on {npairs} NN generators, achieved radius {maxr})"
            print(line + f"  [{time.time()-t0:.1f}s, vars={out[1]}, clauses={out[2]}]", flush=True)
