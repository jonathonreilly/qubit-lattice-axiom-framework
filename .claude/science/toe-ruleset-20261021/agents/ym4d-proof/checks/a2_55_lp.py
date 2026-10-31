# a2_55_lp.py -- exact checks for ALIGN2_55 section 2 (hierarchical local-path alignment Lambda_LP; spline subdivision nesting).
# Criteria: a2_55_lp_criteria.md (incl. Amendment A1), written before this script. Fractions/ints only; stdout only.
from fractions import Fraction as F
import random, itertools

L = 3
S3 = {0: {0: F(1)}, 1: {-1: F(-5, 81), 0: F(60, 81), 1: F(30, 81), 2: F(-4, 81)},
      2: {-1: F(-4, 81), 0: F(30, 81), 1: F(60, 81), 2: F(-5, 81)}}
LIN = {0: {0: F(1)}, 1: {0: F(2, 3), 1: F(1, 3)}, 2: {0: F(1, 3), 1: F(2, 3)}}

def axial_steps(delta):
    steps = []
    for mu in (0, 1):
        sgn = 1 if delta[mu] > 0 else -1
        steps += [(mu, sgn)] * abs(delta[mu])
    return steps
def path_rel(r, o, steps_fn):
    # path from Y = 3*(I+o) to y = 3*I + r, returned as list of (rel_link_base, mu, sign) relative to y
    delta = (r[0] - 3*o[0], r[1] - 3*o[1])
    pos = (-delta[0], -delta[1])            # start Y relative to y
    out = []
    for (mu, sgn) in steps_fn(delta):
        if sgn > 0:
            out.append((pos, mu, 1)); pos = (pos[0] + (mu == 0), pos[1] + (mu == 1))
        else:
            pos = (pos[0] - (mu == 0), pos[1] - (mu == 1)); out.append((pos, mu, -1))
    assert pos == (0, 0)
    return out
def make_random_steps(seed):
    rng = random.Random(seed)
    cache = {}
    def fn(delta):
        if delta not in cache:
            st = axial_steps(delta); rng.shuffle(st); cache[delta] = st
        return list(cache[delta])
    return fn

class Model:
    def __init__(self, k, T, scheme=S3, steps_fn=axial_steps):
        self.k, self.T, self.sch = k, T, scheme
        self.N = [T * L**(k - l) for l in range(k + 1)]
        self.stencil = {}
        for r in itertools.product(range(3), repeat=2):
            lst = []
            for o0, w0 in scheme[r[0]].items():
                for o1, w1 in scheme[r[1]].items():
                    lst.append(((o0, o1), w0 * w1, path_rel(r, (o0, o1), steps_fn)))
            self.stencil[r] = lst
    def S0(self, l, v_coarse):   # level l+1 -> level l
        N = self.N[l]; Nc = self.N[l + 1]; out = {}
        for i in range(N):
            I, r0 = divmod(i, 3)
            for j in range(N):
                J, r1 = divmod(j, 3); s = F(0)
                for (o, w, _) in self.stencil[(r0, r1)]:
                    val = v_coarse.get(((I + o[0]) % Nc, (J + o[1]) % Nc))
                    if val: s += w * val
                if s: out[(i, j)] = s
        return out
    def M(self, l, xl):          # local path-average operator at level l (xl: dict link->value)
        N = self.N[l]; out = {}
        if not xl: return out
        for i in range(N):
            r0 = i % 3
            for j in range(N):
                r1 = j % 3
                if r0 == 0 and r1 == 0: continue
                s = F(0)
                for (o, w, path) in self.stencil[(r0, r1)]:
                    acc = F(0)
                    for (rel, mu, sg) in path:
                        val = xl.get((((i + rel[0]) % N, (j + rel[1]) % N), mu))
                        if val: acc += sg * val
                    if acc: s += w * acc
                if s: out[(i, j)] = s
        return out
    def Lam(self, x):            # returns list lam[l], l = 0..k
        lam = [None] * (self.k + 1); lam[self.k] = {}
        for l in range(self.k - 1, -1, -1):
            v = self.S0(l, lam[l + 1]); m = self.M(l, x[l])
            for key, val in m.items():
                v[key] = v.get(key, F(0)) - val
            lam[l] = {kk: vv for kk, vv in v.items() if vv != 0}
        return lam
    def Xi(self, nu):            # nu: dict on level-0 sites
        x = []
        for l in range(self.k):
            N, sc, N0 = self.N[l], L**l, self.N[0]; xl = {}
            for i in range(N):
                for j in range(N):
                    a = nu.get(((i*sc) % N0, (j*sc) % N0), F(0))
                    for mu in (0, 1):
                        b = nu.get((((i + (mu == 0))*sc) % N0, ((j + (mu == 1))*sc) % N0), F(0))
                        if b - a: xl[((i, j), mu)] = b - a
            x.append(xl)
        return x

def rnd(rng): return F(rng.randint(-9, 9), rng.randint(1, 6))
def random_nu(m, rng):
    N0, sk = m.N[0], L**m.k
    return {(i, j): rnd(rng) for i in range(N0) for j in range(N0) if not (i % sk == 0 and j % sk == 0)}
def random_chain(m, rng):
    return [{((i, j), mu): rnd(rng) for i in range(m.N[l]) for j in range(m.N[l]) for mu in (0, 1)} for l in range(m.k)]
def same(d1, d2): return {k: v for k, v in d1.items() if v} == {k: v for k, v in d2.items() if v}

results = {}
# ---------------- Part A ----------------
okA = {n: True for n in ('A1', 'A2', 'A3', 'A4', 'A1r')}
for k in (2, 3):
    m = Model(k, 4)
    for seed in (1, 2):
        rng = random.Random(1000*k + seed)
        nu = random_nu(m, rng)
        lam = m.Lam(m.Xi(nu))
        okA['A1'] &= same(lam[0], {kk: -vv for kk, vv in nu.items()})
        x = random_chain(m, rng); lam = m.Lam(x)
        for l in range(1, k):
            sc = L**l
            restr = {(i, j): lam[0].get(((i*sc), (j*sc)), F(0)) for i in range(m.N[l]) for j in range(m.N[l])}
            okA['A2'] &= same(restr, lam[l])
        mpert = rng.randrange(0, k)
        x2 = [dict(xl) for xl in x]
        for key in x2[mpert]: x2[mpert][key] += rnd(rng)
        lam2 = m.Lam(x2)
        for l in range(mpert + 1, k + 1): okA['A3'] &= same(lam[l], lam2[l])
        lq = k - 1; sc = L**lq
        q = {(i*sc, j*sc): rnd(rng) for i in range(m.N[lq]) for j in range(m.N[lq])}
        pair = lambda lm: sum(q[z] * lm.get(z, F(0)) for z in q)
        x3 = [dict(xl) for xl in x]
        for mm in range(0, lq):
            for key in x3[mm]: x3[mm][key] += rnd(rng)
        okA['A4'] &= (pair(lam[0]) == pair(m.Lam(x3)[0]))
    mr = Model(k, 4, steps_fn=make_random_steps(77 + k))
    rng = random.Random(5000 + k); nu = random_nu(mr, rng)
    okA['A1r'] &= same(mr.Lam(mr.Xi(nu))[0], {kk: -vv for kk, vv in nu.items()})
# A5 on T = 8
radii = {}
for k in (2, 3):
    m = Model(k, 8); mlev = k - 1
    x = [dict() for _ in range(k)]
    b0 = (m.N[mlev] // 2, m.N[mlev] // 2)
    x[mlev][(b0, 0)] = F(1)
    lam0 = m.Lam(x)[0]
    N0, sc = m.N[0], L**mlev
    base = (b0[0]*sc, b0[1]*sc)
    def tdist(a, b):
        return max(min((a[0]-b[0]) % N0, (b[0]-a[0]) % N0), min((a[1]-b[1]) % N0, (b[1]-a[1]) % N0))
    rad_own = max(tdist(z, base) for z, v in lam0.items() if v != 0)
    radii[k] = F(rad_own, L**k)            # coarse units
R_pred = 6 * F(1, L) * F(L, L - 1)         # 6 rho_m L/(L-1), rho_m = 1/L
okA['A5'] = all(r <= R_pred for r in radii.values())
for n in ('A1', 'A2', 'A3', 'A4', 'A1r'): print("Part A:", n, "PASS" if okA[n] else "FAIL")
print("Part A: A5 radii (coarse) k=2:", radii[2], " k=3:", radii[3], " bound:", R_pred, "->", "PASS" if okA['A5'] else "FAIL")

# ---------------- Part B ----------------
def field_affine(m, c, A):     # x^c_mu = c_mu + sum_nu A[mu][nu] * pos^c_nu at level 0, own x = rho_0 * x^c; pos^c = rho_0 * index
    rho = F(1, L**m.k); N = m.N[0]; x0 = {}
    for i in range(N):
        for j in range(N):
            for mu in (0, 1):
                x0[((i, j), mu)] = rho * (c[mu] + A[mu][0]*rho*i + A[mu][1]*rho*j)
    return x0
def field_quad(m, Q):          # x^c_mu = sum Q[mu] . (P0^2, P0 P1, P1^2), P = rho*index
    rho = F(1, L**m.k); N = m.N[0]; x0 = {}
    for i in range(N):
        for j in range(N):
            P0, P1 = rho*i, rho*j
            for mu in (0, 1):
                x0[((i, j), mu)] = rho * (Q[mu][0]*P0*P0 + Q[mu][1]*P0*P1 + Q[mu][2]*P1*P1)
    return x0
def window(m):
    N = m.N[0]; return [(i, j) for i in range(8, N - 9) for j in range(8, N - 9)]
cA, AA = (F(2, 3), F(-5, 7)), ((F(3, 2), F(-7, 5)), (F(11, 4), F(-2, 9)))
QQ = ((F(1), F(-3, 2), F(2, 5)), (F(-4, 3), F(5, 7), F(1, 2)))
def detail_max(m, x0, check_zero=False):
    mu = m.M(0, x0); w = window(m)
    vals = [abs(mu.get(z, F(0))) for z in w]
    return max(vals)
okB1 = True; quadmax = {}; quadmax_lin = {}
fire = {'CB1': False, 'CB2': False, 'CB3': False}
for k in (2, 3):
    m = Model(k, 4)
    okB1 &= (detail_max(m, field_affine(m, cA, AA)) == 0)
    quadmax[k] = detail_max(m, field_quad(m, QQ))
    ml = Model(k, 4, scheme=LIN)
    if detail_max(ml, field_affine(ml, cA, AA)) != 0: fire['CB1'] = True
    quadmax_lin[k] = detail_max(ml, field_quad(ml, QQ))
    mr = Model(k, 4, steps_fn=make_random_steps(99 + k))
    if detail_max(mr, field_affine(mr, cA, AA)) != 0: fire['CB2'] = True
ratio = quadmax[3] / quadmax[2] if quadmax[2] != 0 else None
okB2 = (quadmax[2] != 0) and (ratio == F(1, 27))
ratio_lin = quadmax_lin[3] / quadmax_lin[2] if quadmax_lin[2] != 0 else None
if ratio_lin != F(1, 27): fire['CB3'] = True
print("Part B: B1 (affine fields annihilated exactly, both depths):", "PASS" if okB1 else "FAIL")
print("Part B: B2 quadratic detail max k=2:", quadmax[2], " k=3:", quadmax[3], " ratio:", ratio, "->", "PASS" if okB2 else "FAIL")
print("Part B: linear-interp ratio (control CB3):", ratio_lin)
for kk, v in fire.items(): print("Part B control", kk, "FIRES" if v else "does NOT fire")

# ---------------- Part C ----------------
def B3(t):
    t = abs(t)
    if t >= 2: return F(0)
    if t >= 1: return (2 - t)**3 / 6
    return (4 - 6*t*t + 3*t**3) / 6
def Bper(t, M):
    s = F(0)
    for mm in range(-4, 5): s += B3(t - mm*M)
    return s
def matinv(A):
    n = len(A); Mx = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if Mx[r][c] != 0)
        Mx[c], Mx[p] = Mx[p], Mx[c]
        pv = Mx[c][c]; Mx[c] = [v / pv for v in Mx[c]]
        for r in range(n):
            if r != c and Mx[r][c] != 0:
                fct = Mx[r][c]; Mx[r] = [a - fct*b for a, b in zip(Mx[r], Mx[c])]
    return [row[n:] for row in Mx]
def det(A):
    n = len(A); Mx = [row[:] for row in A]; d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if Mx[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: Mx[c], Mx[p] = Mx[p], Mx[c]; d = -d
        d *= Mx[c][c]
        for r in range(c + 1, n):
            fct = Mx[r][c] / Mx[c][c]; Mx[r] = [a - fct*b for a, b in zip(Mx[r], Mx[c])]
    return d
def mm_(A, B): return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def spline_sub(Lf, M):
    C = [[Bper(F(i - j), M) for j in range(M)] for i in range(M)]
    E = [[Bper(F(i, Lf) - j, M) for j in range(M)] for i in range(Lf*M)]
    return mm_(E, matinv(C))
okC1 = okC2 = True
for (Lf, M) in ((3, 4), (5, 3), (3, 3)):
    S1 = spline_sub(Lf, M); S2 = spline_sub(Lf, Lf*M); Sdir = spline_sub(Lf*Lf, M)
    okC1 &= (mm_(S2, S1) == Sdir)
    okC2 &= all(S1[Lf*i] == [F(int(i == j)) for j in range(M)] for i in range(M))
    okC2 &= all(sum(row) == 1 for row in S1)
okC3 = all(det([[Bper(F(i - j), M) for j in range(M)] for i in range(M)]) != 0 for M in range(1, 9))
def dd_weights(tau):
    nodes = (-1, 0, 1, 2); w = {}
    for a in nodes:
        num = F(1); den = F(1)
        for b in nodes:
            if b != a: num *= (tau - b); den *= (a - b)
        w[a] = num / den
    return w
def dd_sub(Lf, M):
    S = [[F(0)]*M for _ in range(Lf*M)]
    for i in range(Lf*M):
        I, r = divmod(i, Lf)
        if r == 0: S[i][I % M] += 1; continue
        for a, wv in dd_weights(F(r, Lf)).items(): S[i][(I + a) % M] += wv
    return S
fireCC1 = (mm_(dd_sub(3, 18), dd_sub(3, 6)) != dd_sub(9, 6))
print("Part C: C1 (spline nesting S^(L)_{LM} S^(L)_M == S^(L^2)_M):", "PASS" if okC1 else "FAIL")
print("Part C: C2 (interpolatory, reproduces constants):", "PASS" if okC2 else "FAIL")
print("Part C: C3 (periodic collocation invertible, M = 1..8):", "PASS" if okC3 else "FAIL")
print("Part C control CC1 (DD3^2 != DD9):", "FIRES" if fireCC1 else "does NOT fire")
overall = all(okA.values()) and okB1 and okB2 and okC1 and okC2 and okC3 and all(fire.values()) and fireCC1
print("OVERALL:", "PASS" if overall else "FAIL")
