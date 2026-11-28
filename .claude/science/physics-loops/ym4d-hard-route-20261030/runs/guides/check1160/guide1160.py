# Guide runs for the check of gap-solve8-astra62.md (row 1160). Pure Python.
# A guide only: nothing here is a proof step.
import math, random, itertools, sys

random.seed(20261119)

def jacobi_eig(A, tol=1e-13, maxsweep=200):
    n = len(A)
    a = [row[:] for row in A]
    for _ in range(maxsweep):
        off = sum(a[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                th = (a[q][q] - a[p][p]) / (2 * a[p][q])
                t = (1.0 if th >= 0 else -1.0) / (abs(th) + math.sqrt(th * th + 1))
                c = 1 / math.sqrt(t * t + 1); s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
    return sorted((a[i][i] for i in range(n)), reverse=True)

def matmul(A, B):
    n, m, l = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(l)] for i in range(n)]

G = list(itertools.product((0, 1), repeat=3))
def gadd(g, h): return tuple((x + y) % 2 for x, y in zip(g, h))
def chi(c, g): return -1 if sum(x * y for x, y in zip(c, g)) % 2 else 1

out = []
def say(s):
    out.append(s); print(s); sys.stdout.flush()

# ---------- (1): charged comparison on random Z_2^3-invariant positive kernels
def test_eq1(trials=400):
    worst = {1: 9.9, 2: 9.9, 3: 9.9, 10: 9.9}
    for tr in range(trials):
        m = random.choice([2, 3, 4, 5])
        mode = tr % 3
        w = {}
        for k in G:
            for a in range(m):
                for b in range(a, m):
                    if mode == 0:
                        v = random.random()
                    elif mode == 1:
                        v = random.random() ** 6
                    else:
                        v = (1.0 if k == (0, 0, 0) and a == b else 0.0) + 0.05 * random.random() ** 3
                    w[(k, a, b)] = w[(k, b, a)] = v
        sect = {}
        for c in G:
            Wc = [[sum(chi(c, k) * w[(k, a, b)] for k in G) for b in range(m)] for a in range(m)]
            mu = jacobi_eig(Wc)
            sect[c] = sorted((x * x for x in mu), reverse=True)  # K = W^2 >= 0
        lam0 = max(max(v) for v in sect.values())
        if abs(sect[(0, 0, 0)][0] - lam0) > 1e-9 * lam0:
            say("  vacuum not neutral?")
        neu = [x / lam0 for x in sect[(0, 0, 0)]]
        rho = neu[1]
        for c in G:
            if c == (0, 0, 0):
                continue
            lv = [x / lam0 for x in sect[c]]
            l2 = lv[1]
            for s in worst:
                if rho ** s < 1 - 1e-12:
                    r = (1 - l2 ** s) / (1 - rho ** s)
                    worst[s] = min(worst[s], r)
    return worst

w1 = test_eq1()
say("(1) min over random kernels of (1-lam_{chi,2}^s)/(1-rho^s) [must be >= 1/4]: "
    + ", ".join("s=%d: %.4f" % (s, v) for s, v in sorted(w1.items())))
# circle sharpness: lattice circle Z_{2N}, half-turn flip, heat-type kernel
vals = []
for N in (8, 32, 128):
    for h in (0.5, 0.05, 0.005):
        phi = lambda k: 1 - math.cos(math.pi * k / N)
        l1 = math.exp(-h * N * N * phi(1)); r2 = math.exp(-h * N * N * phi(2))
        vals.append((N, h, (1 - l1) / (1 - r2)))
say("(1) circle ratios (N, h, ratio): " + "; ".join("%d,%g,%.4f" % v for v in vals))

# ---------- (23): hit-and-run in the polytope of twist-ratio arrays
E = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
def idx(bits): return sum(b << i for i, b in enumerate(bits))
star = {j: [i for i, e in enumerate(E) if j in e] for j in (1, 2, 3, 4)}
comp = {j: [i for i, e in enumerate(E) if j not in e] for j in (1, 2, 3, 4)}
cons = []
for j in (1, 2, 3, 4):
    for c in itertools.product((0, 1), repeat=3):
        for eta in itertools.product((0, 1), repeat=3):
            vec = {}
            for t in itertools.product((0, 1), repeat=3):
                bits = [0] * 6
                for k, e in enumerate(comp[j]): bits[e] = c[k]
                for k, e in enumerate(star[j]): bits[e] = t[k]
                sgn = -1 if sum(x * y for x, y in zip(eta, t)) % 2 else 1
                vec[idx(bits)] = vec.get(idx(bits), 0) + sgn
            cons.append(list(vec.items()))
def cval(a, f): return sum(s * f[i] for i, s in a)
def Hzero(f, i):
    tot = 0.0
    for t in itertools.product((0, 1), repeat=3):
        bits = [0] * 6
        for k, e in enumerate(star[i]): bits[e] = t[k]
        tot += f[idx(bits)]
    return tot
def delta(f):
    S = sum(f)
    return max(8 * Hzero(f, i) / S - 1 for i in (1, 2, 3))
def ratio(f):
    d = delta(f); r = 1 - min(f)
    return (r / d if d > 1e-10 else (0.0 if r < 1e-10 else float('inf'))), d, r

def hit_and_run(steps=40000, greedy=0.5):
    y = 0.5
    f = [y ** bin(B).count("1") for B in range(64)]
    best = 0.0; worst_conv = -1.0; min19 = 1.0
    for st in range(steps):
        d = [0.0] + [random.gauss(0, 1) for _ in range(63)]
        lo, hi = -1e9, 1e9
        for a in cons:
            v = cval(a, f); s = cval(a, d)
            if s > 1e-14: lo = max(lo, -v / s)
            elif s < -1e-14: hi = min(hi, -v / s)
        if hi - lo < 1e-14:
            continue
        cand = []
        if random.random() < greedy:
            for lam in (lo, hi):
                g = [x + lam * dd for x, dd in zip(f, d)]
                cand.append((ratio(g)[0], g))
            cand.sort(key=lambda z: z[0])
            if cand[-1][0] >= ratio(f)[0] and cand[-1][0] != float('inf'):
                f = cand[-1][1]
            else:
                lam = random.uniform(lo, hi); f = [x + lam * dd for x, dd in zip(f, d)]
        else:
            lam = random.uniform(lo, hi); f = [x + lam * dd for x, dd in zip(f, d)]
        R, dl, r = ratio(f)
        if R != float('inf'):
            best = max(best, R)
        if r < 1:
            worst_conv = max(worst_conv, dl - r / (1 - r))
        # (19) in every frame: p_i(c) <= p_i(0)
        S = sum(f)
        for i in (1, 2, 3, 4):
            for c in itertools.product((0, 1), repeat=3):
                tot = 0.0
                for t in itertools.product((0, 1), repeat=3):
                    bits = [0] * 6
                    for k, e in enumerate(comp[i]): bits[e] = c[k]
                    for k, e in enumerate(star[i]): bits[e] = t[k]
                    tot += f[idx(bits)]
                min19 = min(min19, (Hzero(f, i) - tot) / S)
        if st % 5000 == 0:
            f = [y ** bin(B).count("1") for B in range(64)] if random.random() < 0.3 else f
    return best, worst_conv, min19, max(f), min(f)

best, wc, m19, fmax, fmin = hit_and_run(steps=6000)
say("(23) polytope walk: max (1-min f)/delta = %.3f [claim <= 256]; max of delta - r/(1-r) = %.2e [claim <= 0];"
    " min of p_i(0)-p_i(c) = %.2e [claim >= 0]; f range [%.3f, %.3f]" % (best, wc, m19, fmin, fmax))

# ---------- (34) on random finite joint laws
worst_a = -9; worst_b = -9
for tr in range(3000):
    k, l = random.choice([2, 3, 4]), random.choice([2, 3, 4])
    P = [[random.random() ** random.choice([1, 3, 8]) for _ in range(l)] for _ in range(k)]
    Z = sum(map(sum, P)); P = [[x / Z for x in row] for row in P]
    px = [sum(row) for row in P]; py = [sum(P[i][j] for i in range(k)) for j in range(l)]
    TV = 0.5 * sum(abs(P[i][j] - px[i] * py[j]) for i in range(k) for j in range(l))
    M = [[math.sqrt(x) for x in row] for row in P]
    MMt = matmul(M, [list(r) for r in zip(*M)])
    A = sum(x * x for row in MMt for x in row)
    worst_a = max(worst_a, TV - 3 * math.sqrt(max(0, 1 - A)))
    worst_b = max(worst_b, (1 - TV) ** 4 - A)
say("(34) max of TV - 3(1-A)^(1/2) = %.3e [claim <= 0]; max of (1-TV)^4 - A = %.3e [claim <= 0]" % (worst_a, worst_b))

# ---------- (10): toy mixed cylinder on X = G x {0,1}
def toy10(seed, h, d):
    rnd = random.Random(seed)
    m = 2
    X = [(g, a) for g in G for a in range(m)]
    ix = {x: i for i, x in enumerate(X)}
    w = {}
    for k in G:
        for a in range(m):
            for b in range(a, m):
                w[(k, a, b)] = w[(k, b, a)] = rnd.random() ** 2
    W = [[w[(gadd(x[0], y[0]), x[1], y[1])] for y in X] for x in X]
    K = matmul(W, W)
    # top eigenvalue by power iteration
    v = [1.0] * len(X)
    for _ in range(400):
        u = [sum(K[i][j] * v[j] for j in range(len(X))) for i in range(len(X))]
        lam = max(u); v = [x / lam for x in u]
    U = [[x / lam for x in row] for row in K]
    def mpow(A, t):
        R = [[1.0 if i == j else 0.0 for j in range(len(A))] for i in range(len(A))]
        for _ in range(t): R = matmul(R, A)
        return R
    def act(b, x): return ix[(gadd(b, X[x][0]), X[x][1])]
    def Zplus(t):
        Ut = mpow(U, t)
        return sum(Ut[x][act(b, x)] for b in G for x in range(len(X))) / 8
    T = 2 * (h + d)
    Ud = mpow(U, d)
    kd = [[sum(Ud[y][act(b, x)] for b in G) / 8 for x in range(len(X))] for y in range(len(X))]
    # joint law of the two segment orbits
    segs = list(itertools.product(range(len(X)), repeat=h + 1))
    def seg_w(s): return math.prod(U[s[i]][s[i + 1]] for i in range(h))
    def orb(s): return min(tuple(act(b, x) for x in s) for b in G)
    orbs = sorted(set(orb(s) for s in segs)); oi = {o: i for i, o in enumerate(orbs)}
    J = [[0.0] * len(orbs) for _ in orbs]
    for s1 in segs:
        w1 = seg_w(s1)
        for s2 in segs:
            J[oi[orb(s1)]][oi[orb(s2)]] += w1 * Ud[s1[-1]][s2[0]] * seg_w(s2) * 8 * kd[s2[-1]][s1[0]]
    Zt = sum(map(sum, J)); J = [[x / Zt for x in row] for row in J]
    M = [[math.sqrt(x) for x in row] for row in J]
    MMt = matmul(M, [list(r) for r in zip(*M)])
    A = sum(x * x for row in MMt for x in row)
    lower = Zplus(T) ** -2 * Zplus(2 * d) ** -4
    # two single slices T/2 apart, on the orbit quotient: A = Z+(2T)/Z+(T)^2
    Uh = mpow(U, T // 2)
    kh = [[sum(Uh[y][act(b, x)] for b in G) / 8 for x in range(len(X))] for y in range(len(X))]
    so = sorted(set(min(act(b, x) for b in G) for x in range(len(X)))); si = {o: i for i, o in enumerate(so)}
    J2 = [[0.0] * len(so) for _ in so]
    for x in range(len(X)):
        for y in range(len(X)):
            J2[si[min(act(b, x) for b in G)]][si[min(act(b, y) for b in G)]] += Uh[x][y] * kh[y][x]
    Z2 = sum(map(sum, J2)); J2 = [[q / Z2 for q in row] for row in J2]
    M2 = [[math.sqrt(q) for q in row] for row in J2]
    MM2 = matmul(M2, [list(r) for r in zip(*M2)])
    A2 = sum(q * q for row in MM2 for q in row)
    return A, lower, 1 / Zplus(T), A2, Zplus(2 * T) / Zplus(T) ** 2

for seed, h, d in ((1, 1, 2), (2, 1, 3), (3, 1, 1)):
    A, lo, up, A2, ex = toy10(seed, h, d)
    say("(10) toy seed %d h=%d d=%d: lower %.6f <= A_obs %.6f <= 1/Z+(T) %.6f; slice-pair A %.10f vs Z+(2T)/Z+(T)^2 %.10f"
        % (seed, h, d, lo, A, up, A2, ex))

# ---------- (28): plane lemma, maximize min_p eps_p prod h on a 3x3 periodic plane
def unit(v):
    s = math.sqrt(sum(x * x for x in v)); return [x / s for x in v]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
N = 3
dirs = ('+x', '-x', '+y', '-y')
def objective(L):
    vals = []
    for x in range(N):
        for y in range(N):
            c = [((x, y), '+x', '+y'), (((x + 1) % N, y), '-x', '+y'),
                 (((x + 1) % N, (y + 1) % N), '-x', '-y'), ((x, (y + 1) % N), '+x', '-y')]
            pr = 1.0
            for v, l1, l2 in c: pr *= dot(L[(v, l1)], L[(v, l2)])
            eps = -1.0 if (x, y) == (0, 0) else 1.0
            vals.append(eps * pr)
    return min(vals)
best28 = -9
for rs in range(60):
    L = {((x, y), dd): unit([random.gauss(0, 1) for _ in range(4)]) for x in range(N) for y in range(N) for dd in dirs}
    cur = objective(L); step = 0.5
    for it in range(4000):
        key = random.choice(list(L))
        old = L[key]
        L[key] = unit([o + step * random.gauss(0, 1) for o in old])
        new = objective(L)
        if new >= cur: cur = new
        else: L[key] = old
        if it % 1000 == 999: step *= 0.5
    best28 = max(best28, cur)
say("(28) plane lemma: best min_p eps_p prod h found = %.5f [claim <= 2^(-1/2) = %.5f]" % (best28, 2 ** -0.5))

# ---------- constants
say("constants: 1-cos(4pi/7)+20(1-cos(pi/7)) = %.4f (<4); cos(4 arccos(3/4)) = %.6f (=-31/32=%.6f);"
    " 223/32 = %.5f (<7); 16(-31/32)+20(3/4) = %.3f; 11/(3pi^2) = %.5f (1/3, 3/7, 1/2, 4/7 = %.4f %.4f %.4f %.4f);"
    " e^(-2pi) = %.6f vs 1/1650 = %.6f; 17*256 = %d"
    % (1 - math.cos(4 * math.pi / 7) + 20 * (1 - math.cos(math.pi / 7)), math.cos(4 * math.acos(0.75)), -31 / 32,
       223 / 32, 16 * (-31 / 32) + 15, 11 / (3 * math.pi ** 2), 1 / 3, 3 / 7, 1 / 2, 4 / 7,
       math.exp(-2 * math.pi), 1 / 1650, 17 * 256))
ok24 = all(2 * (1 - 4 * e) / (1 + e) ** 2 - 1 >= 1 - 12 * e - 1e-15 and (6 * e + e * e) / (1 + e) <= 6 * e + 1e-15
           for e in [i / 20000 for i in range(1, 1000)])
say("(24) scalar inequalities on eta in (0, 1/20): %s" % ok24)
