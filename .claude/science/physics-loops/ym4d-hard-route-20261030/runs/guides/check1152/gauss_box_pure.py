# GUIDE only (pure Python): checks the Section 14 Gaussian identities of row 1151 on small boxes.
import itertools, math, sys

def box(a):
    V = list(itertools.product(range(a[0]), range(a[1]), range(a[2])))
    idx = {v: i for i, v in enumerate(V)}
    E = []
    for v in V:
        for d in range(3):
            w = list(v); w[d] += 1; w = tuple(w)
            if w in idx:
                E.append((v, d))
    eidx = {e: i for i, e in enumerate(E)}
    P = []
    for v in V:
        for d1 in range(3):
            for d2 in range(d1 + 1, 3):
                w1 = list(v); w1[d1] += 1; w1 = tuple(w1)
                w2 = list(v); w2[d2] += 1; w2 = tuple(w2)
                if w1 in idx and w2 in idx:
                    P.append([(eidx[(v, d1)], 1), (eidx[(w1, d2)], 1), (eidx[(w2, d1)], -1), (eidx[(v, d2)], -1)])
    G = []  # gradient rows: edge -> (head, tail)
    for (v, d) in E:
        w = list(v); w[d] += 1; w = tuple(w)
        G.append((idx[w], idx[v]))
    return V, E, P, idx, eidx, G

def comb_tree(V, E, eidx):
    T = set()
    for (v, d) in E:
        if d == 2: T.add(eidx[(v, d)])
        elif d == 1 and v[2] == 0: T.add(eidx[(v, d)])
        elif d == 0 and v[1] == 0 and v[2] == 0: T.add(eidx[(v, d)])
    assert len(T) == len(V) - 1
    return T

def cholesky_logdet(Q):
    n = len(Q)
    A = [row[:] for row in Q]
    ld = 0.0
    for j in range(n):
        s = A[j][j] - sum(A[j][k] * A[j][k] for k in range(j))
        if s <= 0: raise ValueError("not positive definite at %d: %g" % (j, s))
        d = math.sqrt(s); A[j][j] = d; ld += 2 * math.log(d)
        Aj = A[j]
        for i in range(j + 1, n):
            Ai = A[i]
            Ai[j] = (Ai[j] - sum(Ai[k] * Aj[k] for k in range(j))) / d
    return ld

def gaussian_logdet(a, s):
    V, E, P, idx, eidx, G = box(a)
    T = comb_tree(V, E, eidx)
    free_sp = [i for i in range(len(E)) if i not in T]
    fsp = {ei: k for k, ei in enumerate(free_sp)}
    root = idx[(0, 0, 0)]
    free_v = [i for i in range(len(V)) if i != root]
    fv = {vi: k for k, vi in enumerate(free_v)}
    nsp, nv = len(free_sp), len(free_v)
    nper = nsp + nv
    dim = s * nper
    Q = [[0.0] * dim for _ in range(dim)]
    def add(row):
        items = list(row.items())
        for i, x in items:
            for j, y in items:
                Q[i][j] += x * y
    for t in range(s):
        for p in P:
            row = {}
            for ei, sg in p:
                if ei in fsp:
                    c = t * nper + fsp[ei]; row[c] = row.get(c, 0) + sg
            if row: add(row)
        for ei in range(len(E)):
            row = {}
            if ei in fsp:
                c1 = ((t + 1) % s) * nper + fsp[ei]; c0 = t * nper + fsp[ei]
                row[c1] = row.get(c1, 0) + 1; row[c0] = row.get(c0, 0) - 1
            h, tl = G[ei]
            if h != root:
                c = t * nper + nsp + fv[h]; row[c] = row.get(c, 0) - 1
            if tl != root:
                c = t * nper + nsp + fv[tl]; row[c] = row.get(c, 0) + 1
            if row: add(row)
    return cholesky_logdet(Q), dim

def mode_sum(a, m):
    tot = 0.0
    for q in itertools.product(*[range(x) for x in a]):
        k = sum(1 for x in q if x > 0)
        if k <= 1: continue
        lam = sum(4 * math.sin(math.pi * q[j] / (2 * a[j])) ** 2 for j in range(3))
        om = math.acosh(1 + lam / 2)
        x = math.exp(-m * om)
        tot += (k - 1) * math.log((1 + x) / (1 - x))
    return tot

for s in [1, 2, 3, 5, 8]:
    for w in [0.1, 0.7, 2.0]:
        lhs = sum(math.log(2 * math.cosh(w) - 2 * math.cos(2 * math.pi * k / s)) for k in range(s))
        rhs = s * w + 2 * math.log(1 - math.exp(-s * w))
        assert abs(lhs - rhs) < 1e-9
print("periodic determinant identity: OK")
for a in [(2, 2, 3), (2, 3, 3), (3, 3, 3)]:
    for m in [1, 2, 3]:
        ld1, d1 = gaussian_logdet(a, m)
        ld2, d2 = gaussian_logdet(a, 2 * m)
        assert d2 == 2 * d1
        lhs = -ld1 + 0.5 * ld2
        rhs = mode_sum(a, m)
        print("box", a, "m", m, " direct 2logG_m - logG_2m (one colour):", "%.10f" % lhs, "  analytic mode sum:", "%.10f" % rhs)
        sys.stdout.flush()
