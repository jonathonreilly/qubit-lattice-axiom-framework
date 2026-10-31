#!/usr/bin/env python3
# cc55_checks.py -- COFUN_CC.md exact algebra checks.  Criteria: checks/cc55_criteria.md (written first).
# Exact arithmetic only (fractions.Fraction, ints). No numpy, no floats in any verdict. Independent construction:
# no code copied or imported from r55t, r55b, bb9, bb10, bb11, cf1.
import random, sys, time
from fractions import Fraction as Fr

L = 3          # block side
O = 1          # root offset (L-1)/2
T0 = time.time()
RESULTS = []

def report(tag, ok, msg):
    RESULTS.append((tag, ok))
    print(f"{tag}: {'PASS' if ok else 'FAIL'}  {msg}", flush=True)

def control(tag, fired, msg):
    RESULTS.append((tag, fired))
    print(f"{tag} control: {'FIRES' if fired else 'DOES NOT FIRE'}  {msg}", flush=True)

# ---------------- lattice primitives (d = 2) ----------------
def sid(N, a, b): return (a % N) * N + (b % N)
def lid(N, a, b, mu): return 2 * sid(N, a, b) + mu

def d0(lam, N):
    out = [0] * (2 * N * N)
    for a in range(N):
        for b in range(N):
            s = a * N + b
            out[2 * s] = lam[sid(N, a + 1, b)] - lam[s]
            out[2 * s + 1] = lam[sid(N, a, b + 1)] - lam[s]
    return out

def dstar1(j, N):   # adjoint of d0
    out = [0] * (N * N)
    for a in range(N):
        for b in range(N):
            s = a * N + b
            out[s] = (j[lid(N, a - 1, b, 0)] - j[2 * s]) + (j[lid(N, a, b - 1, 1)] - j[2 * s + 1])
    return out

def d1(A, N):
    out = [0] * (N * N)
    for a in range(N):
        for b in range(N):
            s = a * N + b
            out[s] = A[2 * s] + A[lid(N, a + 1, b, 1)] - A[lid(N, a, b + 1, 0)] - A[2 * s + 1]
    return out

def dstar2(Fm, N):  # transpose of d1
    out = [0] * (2 * N * N)
    for a in range(N):
        for b in range(N):
            s = a * N + b
            f = Fm[s]
            if f == 0:
                continue
            out[2 * s] += f
            out[lid(N, a + 1, b, 1)] += f
            out[lid(N, a, b + 1, 0)] -= f
            out[2 * s + 1] -= f
    return out

def ev(lam, Nf):
    Nc = Nf // L
    return [lam[sid(Nf, L * A + O, L * B + O)] for A in range(Nc) for B in range(Nc)]

def evT(f, Nc):
    Nf = Nc * L
    out = [0] * (Nf * Nf)
    for A in range(Nc):
        for B in range(Nc):
            out[sid(Nf, L * A + O, L * B + O)] = f[A * Nc + B]
    return out

def dot(u, v): return sum(x * y for x, y in zip(u, v))
def add(u, v): return [x + y for x, y in zip(u, v)]
def sub(u, v): return [x - y for x, y in zip(u, v)]
def scal(c, u): return [c * x for x in u]
def maxabs(u): return max((abs(x) for x in u), default=0)

# ---------------- averaging operators ----------------
def axial_path(Nf, c, y, order):
    co = {}
    z = [c[0], c[1]]
    for mu in order:
        while z[mu] != y[mu]:
            if y[mu] > z[mu]:
                l = lid(Nf, z[0], z[1], mu); co[l] = co.get(l, 0) + 1; z[mu] += 1
            else:
                z[mu] -= 1; l = lid(Nf, z[0], z[1], mu); co[l] = co.get(l, 0) - 1
    return co

def build_ops(Nf):
    """Root maps (orders 01, 10, avg), straight average and slice functionals, level Nf -> Nf/3."""
    Nc = Nf // L
    ninth = Fr(1, L * L)
    Q = {'01': [], '10': [], 'avg': []}
    H = {'01': [], '10': [], 'avg': []}
    Qs = []
    for A in range(Nc):
        for B in range(Nc):
            # slice functional h(X)
            for name, order in (('01', (0, 1)), ('10', (1, 0))):
                co = {}
                c = (L * A + O, L * B + O)
                for w0 in range(L):
                    for w1 in range(L):
                        y = (L * A + w0, L * B + w1)
                        for l, v in axial_path(Nf, c, y, order).items():
                            co[l] = co.get(l, 0) + v * ninth
                H[name].append({l: v for l, v in co.items() if v != 0})
            ha = {}
            for name in ('01', '10'):
                for l, v in H[name][-1].items():
                    ha[l] = ha.get(l, 0) + v / 2
            H['avg'].append({l: v for l, v in ha.items() if v != 0})
            for mu in range(2):
                e = (1, 0) if mu == 0 else (0, 1)
                c = (L * A + O, L * B + O)
                c2 = (c[0] + L * e[0], c[1] + L * e[1])
                # straight
                cs = {}
                for w0 in range(L):
                    for w1 in range(L):
                        y = (L * A + w0, L * B + w1)
                        for t in range(L):
                            l = lid(Nf, y[0] + t * e[0], y[1] + t * e[1], mu)
                            cs[l] = cs.get(l, 0) + ninth
                Qs.append(cs)
                for name, order in (('01', (0, 1)), ('10', (1, 0))):
                    co = {}
                    for w0 in range(L):
                        for w1 in range(L):
                            y = (L * A + w0, L * B + w1)
                            y2 = (y[0] + L * e[0], y[1] + L * e[1])
                            for l, v in axial_path(Nf, c, y, order).items():
                                co[l] = co.get(l, 0) + v * ninth
                            for t in range(L):
                                l = lid(Nf, y[0] + t * e[0], y[1] + t * e[1], mu)
                                co[l] = co.get(l, 0) + ninth
                            for l, v in axial_path(Nf, c2, y2, order).items():
                                co[l] = co.get(l, 0) - v * ninth
                    Q[name].append({l: v for l, v in co.items() if v != 0})
                qa = {}
                for name in ('01', '10'):
                    for l, v in Q[name][-1].items():
                        qa[l] = qa.get(l, 0) + v / 2
                Q['avg'].append({l: v for l, v in qa.items() if v != 0})
    return Q, Qs, H

def apply(op, v):        # op: list (output index) of dict(input index -> coeff)
    return [sum(c * v[i] for i, c in row.items()) for row in op]

def applyT(op, w, nin):
    out = [0] * nin
    for o, row in enumerate(op):
        wo = w[o]
        if wo == 0:
            continue
        for i, c in row.items():
            out[i] += c * wo
    return out

# ---------------- multi-level model ----------------
class Model:
    def __init__(self, k, T):
        self.k, self.T = k, T
        self.N = [T * L ** (k - i) for i in range(k + 1)]
        self.ops = [build_ops(self.N[i]) for i in range(k)]   # level i -> i+1
        self.kap = [Fr(i + 1) for i in range(k)]
    def nl(self, i): return 2 * self.N[i] ** 2
    def ns(self, i): return self.N[i] ** 2
    def Q(self, i, v, var='avg'): return apply(self.ops[i][0][var], v)
    def QT(self, i, w, var='avg'): return applyT(self.ops[i][0][var], w, self.nl(i))
    def Qstr(self, i, v): return apply(self.ops[i][1], v)
    def h(self, i, v, var='avg'): return apply(self.ops[i][2][var], v)
    def place0(self, f, l):          # ev^{(0->l)T}: level-l function -> level-0 function
        for i in range(l, 0, -1):
            f = evT(f, self.N[i])
        return f
    def root0(self, X):              # level-0 site of level-k root X=(A,B)
        k = self.k; s = L ** k; off = (s - 1) // 2
        return sid(self.N[0], s * X[0] + off, s * X[1] + off)
    def Rk(self, Dfun):
        """level-k function of root values; also report whether Dfun is root-supported"""
        T = self.T
        roots = {self.root0((A, B)): A * T + B for A in range(T) for B in range(T)}
        supported = all(v == 0 or z in roots for z, v in enumerate(Dfun))
        q = [Dfun[self.root0((A, B))] for A in range(T) for B in range(T)]
        return q, supported
    def Phi(self, l, j):             # block flux of a level-l 1-form to level k
        T = self.T; s = L ** (self.k - l); N = self.N[l]
        out = [0] * (2 * T * T)
        for A in range(T):
            for B in range(T):
                for mu in range(2):
                    acc = 0
                    for w in range(s):
                        if mu == 0:
                            Z = (s * A + s - 1, s * B + w)
                        else:
                            Z = (s * A + w, s * B + s - 1)
                        acc += j[lid(N, Z[0], Z[1], mu)]
                    out[2 * (A * T + B) + mu] = acc
        return out
    def blocksum(self, l, f):
        T = self.T; s = L ** (self.k - l); N = self.N[l]
        return [sum(f[sid(N, s * A + a, s * B + b)] for a in range(s) for b in range(s))
                for A in range(T) for B in range(T)]

# source = dict with lists G[l] (level-l 2-forms), j[l] (level-l 1-forms), s[l] (level-(l+1) 1-forms)
def zero_source(M):
    k = M.k
    return {'G': [[0] * M.ns(l) for l in range(k)], 'j': [[0] * M.nl(l) for l in range(k)],
            's': [[0] * M.nl(l + 1) for l in range(k)]}

def chain_coeffs(M, S, var='avg'):
    k = M.k; out = []
    for l in range(k):
        v = add(dstar2(S['G'][l], M.N[l]), S['j'][l])
        v = add(v, M.QT(l, S['s'][l], var))
        if l >= 1:
            v = sub(v, S['s'][l - 1])
        out.append(v)
    return out

def Dfun(M, coeffs):
    tot = [0] * M.ns(0)
    for l, v in enumerate(coeffs):
        tot = add(tot, M.place0(dstar1(v, M.N[l]), l))
    return tot

def residuals(M, x, xk, var='avg'):
    k = M.k
    return [sub(M.Q(l, x[l], var), x[l + 1] if l + 1 < k else xk) for l in range(k)]

def LS(M, S, x, var='avg'):          # linear source functional, x_k = 0
    k = M.k; r = residuals(M, x, [0] * M.nl(k), var)
    tot = 0
    for l in range(k):
        tot += dot(S['G'][l], d1(x[l], M.N[l])) + dot(S['j'][l], x[l]) + dot(S['s'][l], r[l])
    return tot

def Equad(M, x, xk, var='avg'):
    r = residuals(M, x, xk, var)
    F0 = d1(x[0], M.N[0])
    return Fr(1, 2) * dot(F0, F0) + sum(M.kap[l] / 2 * dot(r[l], r[l]) for l in range(M.k))

def path_level(M, l, start, mu, length):  # straight level-l path, +1 on links start + t e_mu
    j = [0] * M.nl(l); N = M.N[l]
    for t in range(length):
        z = (start[0] + t * (mu == 0), start[1] + t * (mu == 1))
        j[lid(N, z[0], z[1], mu)] += 1
    return j

def random_cc_source(M, rng, with_top=True, gens=('g1', 'g2', 'g3', 'g4', 'g5')):
    k = M.k; S = zero_source(M); T = M.T
    for l in range(k):
        N = M.N[l]
        if 'g1' in gens:
            S['G'][l] = [rng.randint(-3, 3) for _ in range(M.ns(l))]
        if 'g2' in gens and (l < k - 1 or with_top):
            S['s'][l] = [rng.randint(-3, 3) for _ in range(M.nl(l + 1))]
        if 'g5' in gens:
            S['j'][l] = add(S['j'][l], dstar2([rng.randint(-2, 2) for _ in range(M.ns(l))], N))
        if 'g3' in gens and l <= k - 2:
            for _ in range(3):
                Nn = M.N[l + 1]
                Y = (rng.randrange(Nn), rng.randrange(Nn)); mu = rng.randrange(2); c = rng.choice([-3, -2, -1, 1, 2, 3])
                p = (L * Y[0] + O, L * Y[1] + O)
                S['j'][l] = add(S['j'][l], scal(c, path_level(M, l, p, mu, L)))
                S['j'][l + 1][lid(Nn, Y[0], Y[1], mu)] -= c
        if 'g4' in gens and (l == 0 or l == k - 1 or rng.random() < 0.5):
            for _ in range(2):
                s = L ** (k - l); X = (rng.randrange(T), rng.randrange(T)); mu = rng.randrange(2)
                c = rng.choice([-3, -2, -1, 1, 2, 3])
                p = (s * X[0] + (s - 1) // 2, s * X[1] + (s - 1) // 2)
                S['j'][l] = add(S['j'][l], scal(c, path_level(M, l, p, mu, s)))
    return S

def flux_b(M, S, skip0=False):
    k = M.k; b = list(S['s'][k - 1])
    for l in range(k):
        if skip0 and l == 0:
            continue
        b = add(b, M.Phi(l, S['j'][l]))
    return b

def cS(M, S, with_s=True):
    k = M.k
    c = sum(Fr(L ** (k - l)) * maxabs(S['j'][l]) for l in range(k))
    return c + (maxabs(S['s'][k - 1]) if with_s else 0)

def decompose(M, S, var_sub='avg'):
    k = M.k; Sp = {'G': [list(g) for g in S['G']], 'j': [list(j) for j in S['j']], 's': [list(s) for s in S['s']]}
    bj = [0] * M.nl(k)
    for l in range(k):
        bj = add(bj, M.Phi(l, S['j'][l]))
    Sp['j'][k - 1] = sub(Sp['j'][k - 1], M.QT(k - 1, bj, var_sub))
    Sp['s'][k - 1] = [0] * M.nl(k)
    return Sp

def slot(M, S, which):
    Z = zero_source(M)
    if which == 'G': Z['G'] = S['G']
    if which == 'j': Z['j'] = S['j']
    if which == 's': Z['s'] = S['s']
    return Z

def rand_chain(M, rng):
    return [[rng.randint(-4, 4) for _ in range(M.nl(l))] for l in range(M.k)]

# ================= PART A =================
def partA(k, T, seed):
    print(f"--- Part A (k={k}, T={T}) ---", flush=True)
    rng = random.Random(seed)
    M = Model(k, T)
    # A1
    ok = True
    for i in range(k):
        Nf, Nc = M.N[i], M.N[i + 1]
        for _ in range(3):
            lam = [rng.randint(-5, 5) for _ in range(M.ns(i))]
            A = [rng.randint(-5, 5) for _ in range(M.nl(i))]
            for var in ('01', '10', 'avg'):
                if M.Q(i, d0(lam, Nf), var) != d0(ev(lam, Nf), Nc):
                    ok = False
                if M.Q(i, A, var) != sub(M.Qstr(i, A), d0(M.h(i, A, var), Nc)):
                    ok = False
    report(f"A1[k={k},T={T}]", ok, "root covariance Q d = d ev and Q = Q_str - d h, orders 01/10/avg")
    # A2
    ok = True
    for l in range(k):
        for _ in range(3):
            j = [rng.randint(-5, 5) for _ in range(M.nl(l))]
            if dstar1(M.Phi(l, j), M.N[k]) != M.blocksum(l, dstar1(j, M.N[l])):
                ok = False
            if maxabs(M.Phi(l, j)) > L ** (k - l) * maxabs(j):
                ok = False
    report(f"A2[k={k},T={T}]", ok, "d*_k Phi_l j = blocksum(d*_l j); |Phi_l j| <= 3^(k-l)|j|")
    # A3-A9
    srcs = [random_cc_source(M, rng) for _ in range(4)]
    okA3, okA4, okA5, okA6, okA8, okA9 = True, True, True, True, True, True
    anyq = False; c1 = False; c2 = False; c3 = False; c4 = False
    info = []
    for S in srcs:
        D = Dfun(M, chain_coeffs(M, S))
        q, supp = M.Rk(D)
        if not supp or sum(q) != 0:
            okA3 = False
        if any(v != 0 for v in q):
            anyq = True
        b = flux_b(M, S)
        if dstar1(b, M.N[k]) != q:
            okA4 = False
        if maxabs(b) > cS(M, S):
            okA4 = False
        info.append((maxabs(q), maxabs(b), cS(M, S)))
        bw = flux_b(M, S, skip0=True)
        if dstar1(bw, M.N[k]) != q:
            c1 = True
        Sp = decompose(M, S)
        Sp_bad = decompose(M, S, var_sub='01')
        for _ in range(8):
            x = rand_chain(M, rng)
            r = residuals(M, x, [0] * M.nl(k))
            if LS(M, S, x) != LS(M, Sp, x) + dot(b, r[k - 1]):
                okA5 = False
            if LS(M, S, x) != LS(M, Sp_bad, x) + dot(b, r[k - 1]):
                c2 = True
        # A6
        if any(v != 0 for v in Dfun(M, chain_coeffs(M, Sp))):
            okA6 = False
        for w in ('G', 'j', 's'):
            if any(v != 0 for v in Dfun(M, chain_coeffs(M, slot(M, Sp, w)))):
                okA6 = False
        # A8
        diffs = set(); diffs_bad = set()
        kap = M.kap[k - 1]; kap_bad = M.kap[k - 2] if k >= 2 else Fr(7)
        for _ in range(8):
            x = rand_chain(M, rng)
            r = residuals(M, x, [0] * M.nl(k))
            Esrc = Equad(M, x, [0] * M.nl(k)) - dot(b, r[k - 1])
            diffs.add(Esrc - Equad(M, x, [v / kap for v in b]))
            diffs_bad.add(Esrc - Equad(M, x, [v / kap_bad for v in b]))
        if diffs != {-dot(b, b) / (2 * kap)}:
            okA8 = False
        if len(diffs_bad) > 1:
            c3 = True
    report(f"A3[k={k},T={T}]", okA3 and anyq, f"all 4 sources (cc) (root-supported, total 0); some q != 0: {anyq}")
    report(f"A4[k={k},T={T}]", okA4, "d*b(S) = q exactly and max|b| <= c(S); (max|q|, max|b|, c(S)) = "
           + str([(str(a), str(bb), str(c)) for a, bb, c in info]))
    report(f"A5[k={k},T={T}]", okA5, "L_S(x) = L_S'(x) + <b, r_{k-1}(x)> on 32 (S,x) pairs")
    report(f"A6[k={k},T={T}]", okA6, "D(S') = D(S'^G) = D(S'^j) = D(S'^s) = 0 pointwise")
    # A7
    ok7 = True
    for _ in range(2):
        S = zero_source(M)
        S['s'][k - 1] = [rng.randint(-3, 3) for _ in range(M.nl(k))]
        D = Dfun(M, chain_coeffs(M, S))
        expect = M.place0(dstar1(S['s'][k - 1], M.N[k]), k)
        q, supp = M.Rk(D)
        if D != expect or not supp or sum(q) != 0 or all(v == 0 for v in D):
            ok7 = False
    report(f"A7[k={k},T={T}]", ok7, "top residual slot alone: D = ev^(0->k)T d* s_{k-1}, nonzero, root-supported, total 0")
    report(f"A8[k={k},T={T}]", okA8, "E_src(x; top residual source b) - E(x; B_k = b/kappa_{k-1}) = -||b||^2/(2 kappa_{k-1}) for all x")
    # A9
    ok9 = True
    for _ in range(8):
        x = rand_chain(M, rng)
        r = residuals(M, x, [0] * M.nl(k))
        Hx = []
        for l in range(k):
            if l == 0:
                v = add(dstar2(d1(x[0], M.N[0]), M.N[0]), scal(M.kap[0], M.QT(0, r[0])))
            else:
                v = sub(scal(M.kap[l], M.QT(l, r[l])), scal(M.kap[l - 1], r[l - 1]))
            Hx.append(v)
        lhs = Dfun(M, Hx)
        rhs = M.place0(scal(M.kap[k - 1], dstar1(r[k - 1], M.N[k])), k)
        if lhs != rhs:
            ok9 = False
        rhs_bad = M.place0(scal(M.kap[0] if k >= 2 else Fr(5), dstar1(r[k - 1], M.N[k])), k)
        if lhs != rhs_bad:
            c4 = True
    report(f"A9[k={k},T={T}]", ok9, "D(Hx) = kappa_{k-1} ev^(0->k)T d* r_{k-1}(x) for 8 random chains")
    control(f"C1[k={k},T={T}]", c1, "b with Phi_0 omitted: d*b != q")
    control(f"C2[k={k},T={T}]", c2, "A5 with Q^{01 T} in S' while the chain uses Q^avg: identity fails")
    control(f"C3[k={k},T={T}]", c3, "A8 with kappa_{k-2}: differences not constant")
    control(f"C4[k={k},T={T}]", c4, "A9 with kappa_0 in place of kappa_{k-1}: fails")
    S = zero_source(M); S['s'][k - 1][0] = 1
    b = flux_b(M, S)
    control(f"C5[k={k},T={T}]", maxabs(b) > cS(M, S, with_s=False), "bound without the max|s_{k-1}| term fails on s_{k-1} = delta_b")
    print(f"    (Part A k={k} T={T} done at {time.time() - T0:.1f}s)", flush=True)

# ================= PART B (k = 1, T = 3) =================
def solve_multi(Mat, rhss):
    n = len(Mat); m = len(rhss)
    A = [list(Mat[i]) + [r[i] for r in rhss] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            raise ValueError("singular reduced Hessian")
        A[col], A[piv] = A[piv], A[col]
        rowc = A[col]; inv = 1 / Fr(rowc[col])
        nz = [c for c in range(col, n + m) if rowc[c] != 0]
        for r in range(n):
            if r != col:
                f = A[r][col]
                if f != 0:
                    f = f * inv; rowr = A[r]
                    for c in nz:
                        rowr[c] -= f * rowc[c]
    return [[A[i][n + t] / A[i][i] for i in range(n)] for t in range(m)]

def partB(seed):
    print("--- Part B (k=1, T=3, exact solve) ---", flush=True)
    rng = random.Random(seed)
    M = Model(1, 3)
    N0, N1 = M.N[0], M.N[1]; n0 = M.nl(0); kap = M.kap[0]
    # axial tree gauge (order 01 from the root) in each level-1 block
    tree = set()
    for A in range(N1):
        for B in range(N1):
            c = (L * A + O, L * B + O)
            tree.add(lid(N0, c[0] - 1, c[1], 0)); tree.add(lid(N0, c[0], c[1], 0))
            for a in range(L * A, L * A + L):
                tree.add(lid(N0, a, c[1] - 1, 1)); tree.add(lid(N0, a, c[1], 1))
    U = [i for i in range(n0) if i not in tree]
    def Hop(x0, var):
        r0 = M.Q(0, x0, var)
        return add(dstar2(d1(x0, N0), N0), scal(kap, M.QT(0, r0, var)))
    Hred = {}
    for var in ('avg', '01', '10'):
        cols = {}
        for i in U:
            e = [0] * n0; e[i] = 1
            cols[i] = Hop(e, var)
        Hred[var] = [[cols[jj][ii] for jj in U] for ii in U]
    print(f"    reduced Hessians built ({len(U)} unknowns, {len(tree)} tree links) at {time.time() - T0:.1f}s", flush=True)
    def embed(z):
        x = [0] * n0
        for i, v in zip(U, z):
            x[i] = v
        return x
    def solve(var, rhs_list):
        return [embed(z) for z in solve_multi(Hred[var], [[rhs[i] for i in U] for rhs in rhs_list])]
    # sources
    srcs = [random_cc_source(M, rng, gens=('g1', 'g2', 'g4', 'g5')) for _ in range(3)]
    coeffs = [chain_coeffs(M, S)[0] for S in srcs]
    Sps = [decompose(M, S) for S in srcs]
    coeffsp = [chain_coeffs(M, Sp)[0] for Sp in Sps]
    bs = [flux_b(M, S) for S in srcs]
    data_rhs = [scal(kap, M.QT(0, [v / kap for v in b])) for b in bs]
    sol = solve('avg', coeffs + coeffsp + data_rhs)
    xs, xps, ys = sol[0:3], sol[3:6], sol[6:9]
    ok1 = all(Hop(x, 'avg') == c for x, c in zip(xs, coeffs)) and all(Hop(x, 'avg') == c for x, c in zip(xps, coeffsp))
    report("B1", ok1, "solved x satisfies Hx = S on all 162 links (sources S and S')")
    ok2 = True; qinfo = []
    for S, x, c in zip(srcs, xs, coeffs):
        q, supp = M.Rk(dstar1(c, N0))
        r0 = M.Q(0, x)
        if scal(kap, dstar1(r0, N1)) != q or all(v == 0 for v in q) or not supp:
            ok2 = False
        qinfo.append(str(maxabs(q)))
    report("B2", ok2, f"kappa_0 d* r_0(x) = q exactly at the critical point; max|q| per source = {qinfo}")
    ok3 = True
    for x, xp, y, b in zip(xs, xps, ys, bs):
        if d1(x, N0) != add(d1(xp, N0), d1(y, N0)):
            ok3 = False
        rd = sub(M.Q(0, y), [v / kap for v in b])
        if M.Q(0, x) != add(add(M.Q(0, xp), rd), [v / kap for v in b]):
            ok3 = False
    report("B3", ok3, "dx_0(S) = dx_0(S') + dy_0 and r_0(S) = r_0(S') + r_0(y) + b/kappa_0 exactly (3 sources)")
    # B4 h-independence of the data map
    data = [[rng.randint(-3, 3) for _ in range(M.nl(1))] for _ in range(2)] + [[v / kap for v in bs[0]]]
    outs = {}
    xs_var = {}
    for var in ('avg', '01', '10'):
        rhs = [scal(kap, M.QT(0, B, var)) for B in data]
        sols = solve(var, rhs)
        xs_var[var] = sols
        outs[var] = [(d1(x, N0), sub(M.Q(0, x, var), B)) for x, B in zip(sols, data)]
    ok4 = outs['avg'] == outs['01'] == outs['10']
    report("B4", ok4, "data minimisers with Q^avg, Q^01, Q^10: identical dx_0 and r_0 for 3 data (2 random, b/kappa_0)")
    xr = [rng.randint(-4, 4) for _ in range(n0)]
    Ediff = len({Equad(M, [xr], data[0], var) for var in ('avg', '01', '10')}) > 1
    xdiff = (xs_var['avg'] != xs_var['01']) or (xs_var['avg'] != xs_var['10'])
    control("C6", Ediff and xdiff, f"energies differ as functions: {Ediff}; gauge-fixed minimisers x_0 differ: {xdiff}")
    # B5 designed contrast
    S = zero_source(M)
    S['j'][0] = path_level(M, 0, (L * 1 + O, L * 1 + O), 0, L)
    rhs = chain_coeffs(M, S)[0]   # plain current only: chain-independent
    xa = solve('avg', [rhs])[0]; x1 = solve('01', [rhs])[0]
    differ = d1(xa, N0) != d1(x1, N0)
    print(f"B5 (informational contrast): root-charged plain current, chain Q^avg vs Q^01: dx_0 differ = {differ}", flush=True)
    print(f"    (Part B done at {time.time() - T0:.1f}s)", flush=True)

if __name__ == '__main__':
    partA(2, 3, 5501)
    partA(3, 2, 5502)
    partB(5503)
    allpass = all(ok for _, ok in RESULTS)
    print(f"VERDICT cc55: {'ALL PASS (all controls fired)' if allpass else 'SEE FAILS ABOVE'}  [{len(RESULTS)} items, {time.time() - T0:.1f}s]")
