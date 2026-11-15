# r55h_geo.py — exact shadow geometry checks for REVIEW55_HWPLD (criteria: checks/r55h_geo_criteria.md, written first).
# Pure Python ints/sets. No floats in verdicts. Seeded randomness only for sample selection.
import itertools, random, sys

T4 = list(itertools.product((-1, 0, 1), repeat=4))
CH4 = list(itertools.product((0, 1, 2), repeat=4))

def proj(X):
    return {(a // 3, b // 3, c // 3, d // 3) for (a, b, c, d) in X}

def N1(X):
    return {(a + t0, b + t1, c + t2, d + t3) for (a, b, c, d) in X for (t0, t1, t2, t3) in T4}

def Sig(X):
    return N1(proj(X))

def shnorm4(X, M):
    tot, cur = 0, set(X)
    for r in range(M + 1):
        tot += len(cur)
        cur = Sig(cur)
    return tot

def col(G):
    return {(3 * a + t0, 3 * b + t1, 3 * c + t2, 3 * d + t3) for (a, b, c, d) in G for (t0, t1, t2, t3) in CH4}

# ---------- 1D interval helpers (exact) ----------
def sig1(iv):
    lo, hi = iv
    return (lo // 3 - 1, hi // 3 + 1)

def size(iv):
    return iv[1] - iv[0] + 1

def union_size(a, b):
    inter = max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)
    return size(a) + size(b) - inter

out = []
def rec(s):
    out.append(s); print(s); sys.stdout.flush()

verdicts = {}

# ================= G-A : Proposition SH-neg =================
def E_direct(M):
    zeta = (3 ** (M + 1) - 1) // 2
    z = (zeta,) * 4
    y = (zeta + 8, zeta, zeta, zeta)
    return shnorm4({z, y}, M) - shnorm4({z}, M)

def E_product(M):
    zeta = (3 ** (M + 1) - 1) // 2
    A = (zeta, zeta)          # 1D shadow of zeta (coordinate 1 of z and coords 2-4 of both)
    B = (zeta + 8, zeta + 8)  # 1D shadow of eta = zeta + 8 (coordinate 1 of y)
    tot_P, tot_PY = 0, 0
    for r in range(M + 1):
        if r == 0:
            sP = 1; sPY = 2
        else:
            sP = size(A) ** 4
            sPY = union_size(A, B) * size(A) ** 3
        tot_P += sP; tot_PY += sPY
        A, B = sig1(A), sig1(B)
    return tot_PY - tot_P

ga1 = {M: E_direct(M) for M in range(2, 8)}
ga2 = {M: E_product(M) for M in range(2, 61)}
agree = all(ga1[M] == ga2[M] for M in ga1)
formula = all(ga2[M] == 27 * M + 55 for M in ga2) and all(ga1[M] == 27 * M + 55 for M in ga1)
rec("G-A1 direct 4D E(M), M=2..7: " + str(ga1))
rec("G-A2 product E(M) sample: " + str({M: ga2[M] for M in (2, 5, 10, 20, 29, 30, 45, 60)}))
rec("G-A direct==product on M=2..7: %s ; E(M)==27M+55 for all computed M: %s" % (agree, formula))
verdicts['G-A'] = 'PASS' if (agree and formula) else 'FAIL'

# G-A3: projections distance
M = 30
zeta = (3 ** (M + 1) - 1) // 2
eta = zeta + 8
d = []
pz, py = zeta, eta
for r in range(M + 1):
    d.append(py - pz)
    pz //= 3; py //= 3
rec("G-A3 d_r = pi^r(eta) - pi^r(zeta), r=0..30: " + str(d))
bad = [r for r in range(2, M + 1) if abs(d[r]) != 1]
ga3 = 'CONFIRMED' if not bad else 'REFUTED'
rec("G-A3 sentence 'the two projections stay at distance 1 for ever': %s (r in [2,M] with |d_r| != 1: first few %s, count %d)"
    % (ga3, bad[:5], len(bad)))
verdicts['G-A3'] = ga3

# ================= G-B : PLD depth-free Delta_sh =================
DELTA_SH = 3073361
def excess_direct(q, D):
    Q = (q,) * 4
    x = (3 * q,) * 4
    nx = shnorm4({x}, D + 1)      # levels k-1 .. k+D
    nQ = shnorm4({Q}, D)          # levels k .. k+D
    return nx - nQ

def excess_product(q, D):
    a = (3 * q, 3 * q)   # x_Q, level k-1
    b = (q, q)           # Q, level k
    nx = 0
    for r in range(D + 2):
        nx += size(a) ** 4
        a = sig1(a)
    nQ = 0
    for r in range(D + 1):
        nQ += size(b) ** 4
        b = sig1(b)
    return nx - nQ

def pos_test(D):     # q = 3*w, w = all-ones with D digits
    w = (3 ** D - 1) // 2
    return 3 * w

def pos_ctrl(D):     # q = w itself (control)
    return (3 ** D - 1) // 2

gb1 = {D: (excess_direct(pos_test(D), D), excess_product(pos_test(D), D)) for D in range(2, 8)}
rec("G-B1 test family direct vs product, D=2..7: " + str(gb1))
gb1_ok = all(v[0] == v[1] for v in gb1.values())
gb2 = {D: excess_product(pos_test(D), D) for D in range(2, 61)}
inc = [gb2[D + 1] - gb2[D] for D in range(10, 60)]
rec("G-B2 test family excess sample: " + str({D: gb2[D] for D in (2, 5, 10, 20, 40, 60)}))
rec("G-B2 per-level increments D=10..59: min %d max %d" % (min(inc), max(inc)))
Dbig = 20000
eb = excess_product(pos_test(Dbig), Dbig)
rec("G-B2 excess at D=%d: %d   vs 1+Delta_sh = %d" % (Dbig, eb, 1 + DELTA_SH))
refuted = (eb > 1 + DELTA_SH) or (min(inc) > 0)
verdicts['G-B'] = 'REFUTED (depth-free claim false)' if refuted else 'CONFIRMED (no counterexample in family)'
gb3 = {D: excess_product(pos_ctrl(D), D) for D in (2, 5, 10, 20, 40, 60)}
gb3big = excess_product(pos_ctrl(Dbig), Dbig)
rec("G-B3 control (q = all-ones) excess: %s ; at D=%d: %d" % (gb3, Dbig, gb3big))
verdicts['G-B3 control'] = 'bound holds' if (max(gb3.values()) <= 1 + DELTA_SH and gb3big <= 1 + DELTA_SH) else 'bound fails too'
verdicts['G-B1 product reduction'] = 'agrees' if gb1_ok else 'DISAGREES'

# ================= G-C : ring identities =================
rng = random.Random(55)
w6 = (3 ** 6 - 1) // 2
def rand_set(n, lo, hi, allones_frac=0.3):
    S = set()
    while len(S) < n:
        if rng.random() < allones_frac:
            base = rng.choice([w6, 3 * w6, w6 - 1, 3 * w6 + 2])
            S.add(tuple(base + rng.randint(-2, 2) for _ in range(4)))
        else:
            S.add(tuple(rng.randint(lo, hi) for _ in range(4)))
    return S

c1_viol = 0
for _ in range(200):
    G = rand_set(rng.randint(1, 6), -15, 15)
    if proj(N1(col(G))) != N1(G):
        c1_viol += 1
rec("G-C1 pi(N1(col Gamma)) == N1(Gamma): violations %d / 200" % c1_viol)
verdicts['G-C1'] = 'PASS' if c1_viol == 0 else 'FAIL'

c2_viol = 0; c4_viol = 0
max_open, max_closed = (0, 1), (0, 1)
Mc = 8
for _ in range(200):
    X = rand_set(rng.randint(1, 8), -40, 40)
    Z = N1(X)
    sx = [set(X)]
    for r in range(Mc):
        sx.append(Sig(sx[-1]))
    pz = [set(Z)]
    for r in range(Mc):
        pz.append(proj(pz[-1]))
    sz = [set(Z)]
    for r in range(Mc):
        sz.append(Sig(sz[-1]))
    for r in range(1, Mc + 1):
        if not pz[r] <= sx[r]:
            c2_viol += 1
        if len(sz[r]) > 16 * len(sx[r]):
            c4_viol += 1
    num_open = sum(len(pz[r]) for r in range(1, Mc + 1))
    den_open = sum(len(sx[r]) for r in range(1, Mc + 1))
    num_closed = len(Z) + num_open
    den_closed = sum(len(sx[r]) for r in range(0, Mc + 1))
    if num_open * max_open[1] > max_open[0] * den_open:
        max_open = (num_open, den_open)
    if num_closed * max_closed[1] > max_closed[0] * den_closed:
        max_closed = (num_closed, den_closed)
rec("G-C2 pi^r(N1 X) subset Sigma^r(X), r=1..8: violations %d" % c2_viol)
rec("G-C3 max open-ring count / sum_{r>=1}|Sigma^r X| = %d/%d = %.4f ; max closed-ring count / ||X||_sh = %d/%d = %.4f"
    % (max_open[0], max_open[1], max_open[0] / max_open[1], max_closed[0], max_closed[1], max_closed[0] / max_closed[1]))
rec("G-C4 |Sigma^r(N1 X)| <= 16|Sigma^r X|: violations %d" % c4_viol)
verdicts['G-C2'] = 'PASS' if c2_viol == 0 else 'FAIL'
verdicts['G-C4'] = 'PASS' if c4_viol == 0 else 'FAIL'

rec("VERDICTS: " + str(verdicts))
