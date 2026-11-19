# Second guide run for row 1160: (23) near f = 1 (tangent cone), and (10) toys with
# spread spectra. Pure Python. A guide only.
import math, random, itertools, sys
random.seed(1160)
E = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
def idx(bits): return sum(b << i for i, b in enumerate(bits))
star = {j: [i for i, e in enumerate(E) if j in e] for j in (1, 2, 3, 4)}
comp = {j: [i for i, e in enumerate(E) if j not in e] for j in (1, 2, 3, 4)}
cone = []
for j in (1, 2, 3, 4):
    for c in itertools.product((0, 1), repeat=3):
        for eta in itertools.product((0, 1), repeat=3):
            if eta == (0, 0, 0):
                continue
            vec = {}
            for t in itertools.product((0, 1), repeat=3):
                bits = [0] * 6
                for k, e in enumerate(comp[j]): bits[e] = c[k]
                for k, e in enumerate(star[j]): bits[e] = t[k]
                sgn = -1 if sum(x * y for x, y in zip(eta, t)) % 2 else 1
                vec[idx(bits)] = vec.get(idx(bits), 0) + sgn
            cone.append(list(vec.items()))
def Hvec(i):
    v = {}
    for t in itertools.product((0, 1), repeat=3):
        bits = [0] * 6
        for k, e in enumerate(star[i]): bits[e] = t[k]
        v[idx(bits)] = v.get(idx(bits), 0) + 8
    for B in range(64):
        v[B] = v.get(B, 0) - 1
    return list(v.items())
norm = [Hvec(i) for i in (1, 2, 3)]  # 8 H_i(d) - sum d <= 1
def lin(a, x): return sum(s * x[i] for i, s in a)
def lratio(d):
    den = max(lin(a, d) for a in norm)
    return (64 * (-min(d)) / den) if den > 1e-12 else None
# hit-and-run in {d : d(0)=0, cone >= 0, norm <= 1}; start at an interior point
y = 0.5
f = [y ** bin(B).count("1") for B in range(64)]
d = [x - 1 for x in f]       # f - 1 lies in the cone; scale it into the normalization
s0 = max(lin(a, d) for a in norm); d = [x / (2 * s0) for x in d]
best = 0.0; bestd = None
for st in range(30000):
    u = [0.0] + [random.gauss(0, 1) for _ in range(63)]
    lo, hi = -1e9, 1e9
    for a in cone:
        v = lin(a, d); s = lin(a, u)
        if s > 1e-14: lo = max(lo, -v / s)
        elif s < -1e-14: hi = min(hi, -v / s)
    for a in norm:
        v = 1 - lin(a, d); s = -lin(a, u)
        if s > 1e-14: lo = max(lo, -v / s)
        elif s < -1e-14: hi = min(hi, -v / s)
    if hi - lo < 1e-14 or hi > 1e8 or lo < -1e8:
        continue
    cands = [lo, hi, random.uniform(lo, hi)]
    if random.random() < 0.7:
        sc = []
        for lam in cands[:2]:
            g = [x + lam * w for x, w in zip(d, u)]
            r = lratio(g)
            sc.append((r if r is not None else -1, g))
        sc.sort(key=lambda z: z[0])
        cur = lratio(d) or -1
        d = sc[-1][1] if sc[-1][0] >= cur else [x + cands[2] * w for x, w in zip(d, u)]
    else:
        d = [x + cands[2] * w for x, w in zip(d, u)]
    r = lratio(d)
    if r is not None and r > best:
        best = r; bestd = d[:]
print("(23) tangent cone at f = 1: max of 64(-min d)/max_i(8H_i(d) - sum d) found = %.3f [claim <= 256]" % best)
if bestd:
    worst = min(range(64), key=lambda B: bestd[B])
    print("    worst B (edge bits 12,13,14,23,24,34) =", [(worst >> i) & 1 for i in range(6)],
          " max_i(8H_i - sum) =", round(max(lin(a, bestd) for a in norm), 4), " min d =", round(min(bestd), 4))
sys.stdout.flush()

# (10) toys with spread spectra
def matmul(A, B):
    n, m, l = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(l)] for i in range(n)]
G = list(itertools.product((0, 1), repeat=3))
def gadd(g, h): return tuple((x + y) % 2 for x, y in zip(g, h))
def toy(seed, h, d, eps):
    rnd = random.Random(seed); m = 2
    X = [(g, a) for g in G for a in range(m)]; ix = {x: i for i, x in enumerate(X)}; n = len(X)
    w = {}
    for k in G:
        for a in range(m):
            for b in range(a, m):
                base = 1.0 if (k == (0, 0, 0) and a == b) else 0.0
                w[(k, a, b)] = w[(k, b, a)] = base + eps * rnd.random()
    W = [[w[(gadd(x[0], yy[0]), x[1], yy[1])] for yy in X] for x in X]
    K = matmul(W, W)
    v = [1.0] * n
    for _ in range(2000):
        u = [sum(K[i][j] * v[j] for j in range(n)) for i in range(n)]
        lam = max(u); v = [x / lam for x in u]
    U = [[x / lam for x in row] for row in K]
    def mpow(A, t):
        R = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        for _ in range(t): R = matmul(R, A)
        return R
    def act(b, x): return ix[(gadd(b, X[x][0]), X[x][1])]
    def Zp(t):
        Ut = mpow(U, t); return sum(Ut[x][act(b, x)] for b in G for x in range(n)) / 8
    def Zfull(t):
        Ut = mpow(U, t); return sum(Ut[x][x] for x in range(n))
    T = 2 * (h + d); Ud = mpow(U, d)
    kd = [[sum(Ud[yy][act(b, x)] for b in G) / 8 for x in range(n)] for yy in range(n)]
    segs = list(itertools.product(range(n), repeat=h + 1))
    def segw(s): return math.prod(U[s[i]][s[i + 1]] for i in range(h))
    def orb(s): return min(tuple(act(b, x) for x in s) for b in G)
    orbs = sorted(set(orb(s) for s in segs)); oi = {o: i for i, o in enumerate(orbs)}
    J = [[0.0] * len(orbs) for _ in orbs]
    for s1 in segs:
        w1 = segw(s1); o1 = oi[orb(s1)]
        for s2 in segs:
            J[o1][oi[orb(s2)]] += w1 * Ud[s1[-1]][s2[0]] * segw(s2) * 8 * kd[s2[-1]][s1[0]]
    Zt = sum(map(sum, J)); J = [[x / Zt for x in row] for row in J]
    M = [[math.sqrt(x) for x in row] for row in J]
    MMt = matmul(M, [list(r) for r in zip(*M)])
    A = sum(x * x for row in MMt for x in row)
    return Zp(T) ** -2 * Zp(2 * d) ** -4, A, 1 / Zp(T), Zfull(T)
for seed, h, d, eps in ((5, 1, 1, 0.3), (6, 1, 2, 0.3), (7, 1, 1, 0.1), (8, 1, 2, 0.6)):
    lo, A, up, tr = toy(seed, h, d, eps)
    print("(10) toy seed %d h=%d d=%d eps=%.1f: lower %.6f <= A_obs %.6f <= 1/Z+(T) %.6f  (Tr U^T = %.4f)"
          % (seed, h, d, eps, lo, A, up, tr))
    sys.stdout.flush()
