# st55_2 -- exact one-step (V fixed) conditional Hessian at LCONV55's stripe vs the bare (joint-following) Hessian.
# Criteria: st55_2_criteria.md (sha256 ca8736af..., written 2026-10-29T05:47:31Z before this script).
# SU(2), d = 4, L = 3, fine torus side 6, V = 1. Plain python + fractions; no floats in any verdict.
from fractions import Fraction as F
from itertools import permutations, product
import sys, time

T0 = time.time()
def log(*a):
    print(*a, flush=True)

d = 4; L = 3; NS = 6
ORDERS = list(permutations(range(d)))
NCONT = len(ORDERS) * L ** d            # 1944
ROOT = (1, 1, 1, 1)
PL = [(m, n) for m in range(d) for n in range(m + 1, d)]
Z0 = F(0)
ONE = (F(1), Z0, Z0, Z0)

def qmul(p, q):
    a, b, c, dd = p; e, f, g, h = q
    return (a * e - b * f - c * g - dd * h,
            a * f + e * b - (c * h - dd * g),
            a * g + e * c - (dd * f - b * h),
            a * h + e * dd - (b * g - c * f))
def qconj(p):
    return (p[0], -p[1], -p[2], -p[3])
def qadd(p, q):
    return tuple(x + y for x, y in zip(p, q))
def qscal(p, s):
    return tuple(x * s for x in p)
def vq(v):
    return (Z0, v[0], v[1], v[2])
def Ad(U, v):
    r = qmul(qmul(U, vq(v)), qconj(U)); return (r[1], r[2], r[3])
def unit(k):
    return tuple(1 if i == k else 0 for i in range(d))
def add(a, b):
    return tuple(x + y for x, y in zip(a, b))
def scal(c, a):
    return tuple(c * x for x in a)
def wrap(x):
    return tuple(c % NS for c in x)

E3 = [(F(1), Z0, Z0), (Z0, F(1), Z0), (Z0, Z0, F(1))]

def stripe(tau):
    cb = (1 - tau * tau) / (1 + tau * tau); sb = 2 * tau / (1 + tau * tau)
    G = {0: (cb, Z0, Z0, sb), 1: ONE, 2: (cb, Z0, Z0, -sb)}      # exp(i a sigma_3), a = (beta, 0, -beta)
    def U(x, mu):
        if mu == 1:
            return G[x[0] % 3]
        return ONE
    return U, cb, sb

def axial_path(start, end, sigma):
    cur = list(start); steps = []
    for k in sigma:
        while cur[k] < end[k]:
            steps.append((tuple(cur), k, 1)); cur[k] += 1
        while cur[k] > end[k]:
            cur[k] -= 1; steps.append((tuple(cur), k, -1))
    return steps

CONTOURS = {}
for mu in range(d):
    cY = add(ROOT, scal(L, unit(mu)))
    lst = []
    for sigma in ORDERS:
        for y in product(range(L), repeat=d):
            p1 = axial_path(ROOT, y, sigma)
            p2 = [(add(y, scal(j, unit(mu))), mu, 1) for j in range(L)]
            p3f = axial_path(cY, add(y, scal(L, unit(mu))), sigma)
            p3 = [(s, k, -sg) for (s, k, sg) in reversed(p3f)]
            lst.append(p1 + p2 + p3)
    CONTOURS[mu] = lst

class Space:
    def __init__(self, dep):
        self.dep = tuple(dep)
        self.rs = list(product(range(3), repeat=len(dep)))
        self.ridx = {r: i for i, r in enumerate(self.rs)}
        self.nl = len(self.rs) * d          # link slots
        self.dim = self.nl * 3
        self.nw = F(NS ** d, 3 ** len(dep))   # links per slot (norm weight)
    def r(self, x):
        return tuple(x[i] % 3 for i in self.dep)
    def lslot(self, x, mu):
        return self.ridx[self.r(x)] * d + mu
    def sslot(self, x):
        return self.ridx[self.r(x)]

def zeros(n, m):
    return [[F(0)] * m for _ in range(n)]

def bare_hessian(sp, U):
    H = zeros(sp.dim, sp.dim)
    reps = []
    for r in sp.rs:
        x = [0] * d
        for i, c in zip(sp.dep, r):
            x[i] = c
        reps.append(tuple(x))
    for x in reps:
        for (m, n) in PL:
            links = [(x, m, 1), (add(x, unit(m)), n, 1), (add(x, unit(n)), m, -1), (x, n, -1)]
            F0 = []; slots = []
            for (s, k, sg) in links:
                Ub = U(wrap(s), k)
                F0.append(Ub if sg == 1 else qconj(Ub)); slots.append(sp.lslot(wrap(s), k))
            def X(j, e):
                s, k, sg = links[j]; Ub = U(wrap(s), k)
                return qmul(vq(e), Ub) if sg == 1 else qscal(qmul(qconj(Ub), vq(e)), -1)
            Up = F0[0]
            for j in range(1, 4):
                Up = qmul(Up, F0[j])
            up0 = Up[0]
            for j in range(4):
                for a in range(3):
                    H[slots[j] * 3 + a][slots[j] * 3 + a] += 2 * up0
            for i in range(4):
                for j in range(i + 1, 4):
                    for a in range(3):
                        Xi = X(i, E3[a])
                        for b in range(3):
                            Xj = X(j, E3[b])
                            prod_ = ONE
                            for k in range(4):
                                fac = Xi if k == i else (Xj if k == j else F0[k])
                                prod_ = qmul(prod_, fac)
                            val = -4 * prod_[0]
                            ia = slots[i] * 3 + a; jb = slots[j] * 3 + b
                            H[ia][jb] += val / 2
                            H[jb][ia] += val / 2
    w = sp.nw / 3 ** 0     # each rep stands for NS^4/3^|dep| plaquettes of each orientation
    return [[w * v for v in row] for row in H]

def kernel_data(sp, U):
    """returns r_mu (scalar M-bar) and L_mu (3 x dim) with a'_mu(v) = L_mu v (vector part of dM/dt), for coarse link (0,mu)"""
    out = {}
    for mu in range(d):
        Mbar = (Z0, Z0, Z0, Z0)
        Lm = [[F(0)] * sp.dim for _ in range(3)]
        for path in CONTOURS[mu]:
            F0 = []; info = []
            for (s, k, sg) in path:
                Ub = U(wrap(s), k)
                F0.append(Ub if sg == 1 else qconj(Ub)); info.append((wrap(s), k, sg, Ub))
            n = len(F0)
            pre = [ONE]
            for j in range(n):
                pre.append(qmul(pre[-1], F0[j]))
            suf = [ONE] * (n + 1)
            for j in reversed(range(n)):
                suf[j] = qmul(F0[j], suf[j + 1])
            Mbar = qadd(Mbar, pre[n])
            for j in range(n):
                s, k, sg, Ub = info[j]
                sl = sp.lslot(s, k)
                for a in range(3):
                    Xj = qmul(vq(E3[a]), Ub) if sg == 1 else qscal(qmul(qconj(Ub), vq(E3[a])), -1)
                    q = qmul(qmul(pre[j], Xj), suf[j + 1])
                    for c in range(3):
                        if q[c + 1] != 0:
                            Lm[c][sl * 3 + a] += q[c + 1] / NCONT
        Mbar = qscal(Mbar, F(1, NCONT))
        out[mu] = (Mbar, Lm)
    return out

def kernel_hessian(sp, kd):
    H = zeros(sp.dim, sp.dim)
    for mu in range(d):
        Mbar, Lm = kd[mu]
        r = Mbar[0]
        for c in range(3):
            row = Lm[c]
            nz = [(i, v) for i, v in enumerate(row) if v != 0]
            for i, vi in nz:
                for j, vj in nz:
                    H[i][j] += 16 * 2 * vi * vj / r
    return H

def gauge_matrix(sp, U):
    ns = len(sp.rs)
    G = zeros(sp.dim, ns * 3)
    for r in sp.rs:
        x = [0] * d
        for i, c in zip(sp.dep, r):
            x[i] = c
        x = tuple(x)
        for mu in range(d):
            ls = sp.lslot(x, mu)
            Ub = U(x, mu)
            s0 = sp.sslot(x); s1 = sp.sslot(wrap(add(x, unit(mu))))
            for a in range(3):
                # D_U lambda (x,mu) = lambda(x) - Ad_U lambda(x+e_mu)
                G[ls * 3 + a][s0 * 3 + a] += 1
                adv = [Ad(Ub, E3[b]) for b in range(3)]
                for b in range(3):
                    G[ls * 3 + a][s1 * 3 + b] -= adv[b][a]
    return G

def nullspace(Mrows, ncols):
    """exact basis of {v : M v = 0}, M given as a list of rows"""
    A = [row[:] for row in Mrows]
    piv = []; r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [vi - f * vr for vi, vr in zip(A[i], A[r])]
        piv.append(c); r += 1
        if r == len(A):
            break
    free = [c for c in range(ncols) if c not in set(piv)]
    basis = []
    for fcol in free:
        v = [F(0)] * ncols; v[fcol] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fcol]
        basis.append(v)
    return basis

def transpose(M):
    return [list(col) for col in zip(*M)]

def restrict(H, B):
    HB = [[sum(H[i][k] * b[k] for k in range(len(b)) if b[k] != 0) for b in B] for i in range(len(H))]
    return [[sum(B[p][i] * HB[i][q] for i in range(len(H)) if B[p][i] != 0) for q in range(len(B))] for p in range(len(B))]

def ldl_pd(M):
    n = len(M)
    Lm = [[F(0)] * n for _ in range(n)]; D = [F(0)] * n
    for j in range(n):
        s = M[j][j]
        for k in range(j):
            if Lm[j][k] != 0:
                s -= Lm[j][k] * Lm[j][k] * D[k]
        if s <= 0:
            return False
        D[j] = s
        for i in range(j + 1, n):
            t = M[i][j]
            for k in range(j):
                if Lm[i][k] != 0 and Lm[j][k] != 0:
                    t -= Lm[i][k] * Lm[j][k] * D[k]
            Lm[i][j] = t / s
    return True

def psd_rank(M):
    """exact symmetric elimination: returns (is_psd, rank)"""
    A = [row[:] for row in M]; n = len(A); rank = 0
    active = list(range(n))
    while active:
        # pick a positive diagonal pivot
        piv = None
        for i in active:
            if A[i][i] > 0:
                piv = i; break
        if piv is None:
            for i in active:
                if A[i][i] < 0:
                    return (False, rank)
                for j in active:
                    if A[i][j] != 0:
                        return (False, rank)
            return (True, rank)
        p = A[piv][piv]
        active.remove(piv); rank += 1
        for i in active:
            if A[i][piv] != 0:
                f = A[i][piv] / p
                for j in active:
                    if A[piv][j] != 0:
                        A[i][j] -= f * A[piv][j]
    return (True, rank)

def quad(H, v):
    return sum(v[i] * sum(H[i][j] * v[j] for j in range(len(v)) if v[j] != 0) for i in range(len(v)) if v[i] != 0)

def cert_lower(Hc, B, Gram, nw, lo=-2000, hi=2000):
    """largest k/1000 in [lo,hi]/1000 with B^T(H - lambda nw I)B PD (Gram = B^T B)"""
    HB = restrict(Hc, B)
    def ok(k):
        lam = F(k, 1000)
        M = [[HB[p][q] - lam * nw * Gram[p][q] for q in range(len(B))] for p in range(len(B))]
        return ldl_pd(M)
    if not ok(lo):
        return None
    a, b = lo, hi
    if ok(b):
        return F(b, 1000)
    while b - a > 1:
        m = (a + b) // 2
        if ok(m):
            a = m
        else:
            b = m
    return F(a, 1000)

def vC(sp, tau):
    v = [F(0)] * sp.dim
    for r in sp.rs:
        x = [0] * d
        for i, c in zip(sp.dep, r):
            x[i] = c
        x = tuple(x)
        s0 = sp.lslot(x, 0)
        for a in range(3):
            v[s0 * 3 + a] = F(1)
        if x[0] % 3 == 1:
            s1 = sp.lslot(x, 1)
            v[s1 * 3 + 0] = 4 * tau; v[s1 * 3 + 1] = -4 * tau
    return v

RES = {}
taus = [F(1, 50), F(1, 20), F(1, 10)]
for dep in [(0,), (0, 1)]:
    sp = Space(dep)
    log("\n=== subspace S_dep, dep =", dep, " dim =", sp.dim, " norm weight =", sp.nw, " t=%.1fs" % (time.time() - T0))
    for tau in [F(0)] + taus:
        U, cb, sb = stripe(tau)
        Hb = bare_hessian(sp, U)
        kd = kernel_data(sp, U)
        # G0 zero mismatch
        g0 = True
        for mu in range(d):
            Mbar = kd[mu][0]
            scalar = Mbar[1] == 0 and Mbar[2] == 0 and Mbar[3] == 0 and Mbar[0] > 0
            exp_r = (1 + 2 * (4 * cb ** 3 - 3 * cb)) / 3 if mu == 1 else F(1)
            g0 = g0 and scalar and Mbar[0] == exp_r
        Hk = kernel_hessian(sp, kd)
        G = gauge_matrix(sp, U)
        B = nullspace(transpose(G), sp.dim)        # H_red basis: G^T v = 0
        Gram = [[sum(x * y for x, y in zip(b1, b2)) for b2 in B] for b1 in B]
        vc = vC(sp, tau)
        horiz = all(sum(G[i][j] * vc[i] for i in range(sp.dim)) == 0 for j in range(len(G[0])))
        qb = quad(Hb, vc); qk = quad(Hk, vc); nv = sp.nw * sum(x * x for x in vc)
        tag = "tau=%s" % tau
        line = "%s dep=%s: G0 zero-mismatch %s; dim H_red = %d; v_C horizontal %s; RQ_bare(v_C) = %s ; RQ_ker(v_C, kappa=1) = %s" % (
            tag, dep, g0, len(B), horiz, str(qb / nv), str(qk / nv))
        log(line)
        RES[(dep, tau, 'g0')] = g0
        if dep == (0,) and tau != 0:
            s = 1 + tau * tau
            g1 = (qb == -27648 * tau * tau * (2 + 1 / (s * s))) and horiz
            RES[(dep, tau, 'g1')] = g1
            log("   G1 (= -27648 tau^2 (2 + s^-2) and v_C in H_red):", g1, "; G2 bare not PSD on H_red (v_C certifies):", qb < 0)
            RES[(dep, tau, 'g2')] = qb < 0
        for kap in ([F(1)] if not (dep == (0,) and tau == F(1, 20)) else [F(1), F(1, 10)]):
            Hc = [[Hb[i][j] + kap * Hk[i][j] for j in range(sp.dim)] for i in range(sp.dim)]
            pd = ldl_pd(restrict(Hc, B))
            lb = cert_lower(Hc, B, Gram, sp.nw) if pd else None
            log("   kappa_0 = %s : H_cond PD on H_red: %s ; certified lower bound on min RQ: %s ; RQ_cond(v_C) = %s" % (
                kap, pd, (str(lb) if lb is not None else "-"), str((qb + kap * qk) / nv)))
            RES[(dep, tau, 'pd', kap)] = pd
            RES[(dep, tau, 'qc', kap)] = qb + kap * qk
        if tau == 0:
            ps, rk = psd_rank(restrict(Hb, B))
            log("   C2 (tau=0): bare PSD on H_red: %s, rank %d of %d (kernel dim %d)" % (ps, rk, len(B), len(B) - rk))
            RES[(dep, 'c2')] = ps and rk < len(B) and RES[(dep, tau, 'pd', F(1))]
        log("   t=%.1fs" % (time.time() - T0))

ok = True
for dep in [(0,), (0, 1)]:
    for tau in [F(0)] + taus:
        ok = ok and RES[(dep, tau, 'g0')]
for tau in taus:
    ok = ok and RES[((0,), tau, 'g1')] and RES[((0,), tau, 'g2')]
for dep in [(0,), (0, 1)]:
    for tau in [F(1, 50), F(1, 20)]:
        ok = ok and RES[(dep, tau, 'pd', F(1))]
c1 = RES[((0,), F(1, 20), 'qc', F(1, 10))] < 0 and not RES[((0,), F(1, 20), 'pd', F(1, 10))]
c2 = RES[((0,), 'c2')] and RES[((0, 1), 'c2')]
log("\nC1 (kappa_0 = 1/10 at tau = 1/20 not PSD, v_C certifies) fired:", c1)
log("C2 (tau = 0: bare PSD with kernel, H_cond PD) holds on both subspaces:", c2)
log("report tau=1/10: H_cond PD on H_red(0):", RES[((0,), F(1, 10), 'pd', F(1))], "; on H_red(0,1):", RES[((0, 1), F(1, 10), 'pd', F(1))])
log("OVERALL:", "PASS" if (ok and c1 and c2) else "FAIL", " total %.1fs" % (time.time() - T0))
