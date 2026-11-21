"""A1-A5 of CRITERIA.md. Reviewer's own computation of the tree coefficient."""
import sys, time
import numpy as np
from wnlib import *

rng = np.random.default_rng(20261031)
sig = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)


def expsu2(psi):
    r = np.linalg.norm(psi)
    return np.cos(r / 2) * np.eye(2) + 1j * (np.sinc(r / 2 / np.pi) / 2) * sum(psi[a] * sig[a] for a in range(3))


def Tfun(W1, W2, W3):
    return 0.5 * np.trace(W1 @ W2 @ W3).real - 0.5 * np.trace(W1 @ W3 @ W2).real


def A1():
    worst = 0
    wr = 0
    for _ in range(2000):
        ps = rng.normal(size=(3, 3)) * rng.uniform(0.1, 2)
        W = [expsu2(p) for p in ps]
        v = [np.array([(W[i] @ sig[a]).trace().imag / 2 for a in range(3)]) for i in range(3)]
        worst = max(worst, abs(Tfun(*W) - 2 * v[0] @ np.cross(v[1], v[2])))
        eps = 10 ** rng.uniform(-3, -0.7)
        ps = rng.normal(size=(3, 3)) * eps
        W = [expsu2(p) for p in ps]
        r = abs(Tfun(*W) - ps[0] @ np.cross(ps[1], ps[2]) / 4) / np.linalg.norm(ps) ** 5
        wr = max(wr, r)
    print(f"A1 |T-2v.vxv| worst {worst:.2e}; |T-psi^3/4|/|psi|^5 worst {wr:.3f}  {'PASS' if worst<1e-13 and wr<1 else 'FAIL'}")


CLAIM = {8: (0.39689, 0.21842, 0.61531), 16: (0.39686, 0.21881, 0.61568), 24: (0.39686, 0.21884, 0.61570), 32: (0.39686, 0.21884, 0.61570)}


def corner(T, d=4):
    x = (T // 2,) * d
    paths = [plaq(x, 0, 1), plaq(x, 1, 2), plaq(x, 2, 0)]
    Es = [green(current(p, T, d), T, d) for p in paths]
    kc = K_comp(paths, Es, T)
    kv = 12 * sumV(Es[0], Es[1], Es[2], T, d)
    return paths, Es, kc, kv


def A2(Ts):
    ok = True
    for T in Ts:
        t0 = time.time()
        _, _, kc, kv = corner(T)
        c = CLAIM[T]
        good = abs(kc - c[0]) < 2e-5 and abs(kv - c[1]) < 2e-5 and abs(kc + kv - c[2]) < 2e-5
        ok &= good
        print(f"A2 T={T}: K_comp {kc:.5f} K_vert {kv:.5f} K_total {kc+kv:.5f} (claimed {c}) {time.time()-t0:.1f}s {'ok' if good else 'DIFF'}")
    print("A2", "PASS" if ok else "FAIL")


def A3():
    T = 6
    d = 4
    paths, Es, kc, kv = corner(T)
    bad = 0
    moved = []
    for i in range(3):
        for trial in range(3):
            th = rng.normal(size=(T,) * d)
            E2 = list(Es)
            E2[i] = Es[i] + grad0(th, d)
            kc2 = K_comp(paths, E2, T)
            kv2 = 12 * sumV(E2[0], E2[1], E2[2], T, d)
            bad = max(bad, abs(kc2 + kv2 - kc - kv) / abs(kc + kv))
            moved.append(abs(kc2 - kc))
    # all three shifted at once: Prop 2.2 says each separately; test simultaneous as well
    E3 = [Es[i] + grad0(rng.normal(size=(T,) * d), d) for i in range(3)]
    kc3 = K_comp(paths, E3, T)
    kv3 = 12 * sumV(*E3, T, d)
    print(f"A3 worst rel change K_total {bad:.2e}; min move of K_comp {min(moved):.3f}; simultaneous {abs(kc3+kv3-kc-kv)/abs(kc+kv):.2e} {'PASS' if bad<1e-10 and min(moved)>1e-3 else 'FAIL'}")


# ---------- A4: first-principles tree by numerical minimisation with second-order jets
class J:
    __slots__ = ("f", "g", "H")

    def __init__(s, f, g, H):
        s.f, s.g, s.H = f, g, H

    def __add__(a, b):
        if isinstance(b, J):
            return J(a.f + b.f, a.g + b.g, a.H + b.H)
        return J(a.f + b, a.g, a.H)

    __radd__ = __add__

    def __neg__(a):
        return J(-a.f, -a.g, -a.H)

    def __sub__(a, b):
        return a + (-b)

    def __rsub__(a, b):
        return (-a) + b

    def __mul__(a, b):
        if isinstance(b, J):
            return J(a.f * b.f, a.f * b.g + b.f * a.g, a.f * b.H + b.f * a.H + np.outer(a.g, b.g) + np.outer(b.g, a.g))
        return J(a.f * b, a.g * b, a.H * b)

    __rmul__ = __mul__


def compose(u, f0, f1, f2):
    return J(f0, f1 * u.g, f1 * u.H + f2 * np.outer(u.g, u.g))


def ser(u, coef):
    f0 = sum(c * u ** i for i, c in enumerate(coef))
    f1 = sum(i * c * u ** (i - 1) for i, c in enumerate(coef) if i >= 1)
    f2 = sum(i * (i - 1) * c * u ** (i - 2) for i, c in enumerate(coef) if i >= 2)
    return f0, f1, f2


from math import factorial
CC = [(-1) ** i / (factorial(2 * i) * 4 ** i) for i in range(9)]            # cos(sqrt(u)/2)
SS = [(-1) ** i / (factorial(2 * i + 1) * 2 ** (2 * i + 1)) for i in range(9)]  # sin(sqrt(u)/2)/sqrt(u)
# 2 asin(sqrt(u))/sqrt(u) series
AS = [2 * factorial(2 * i) / (4 ** i * factorial(i) ** 2 * (2 * i + 1)) for i in range(9)]


def qmul(p, q):
    a, b, c, d = p
    e, f, g, h = q
    # q = w + i v.sigma : (w1,v1)(w2,v2) = (w1 w2 - v1.v2, w1 v2 + w2 v1 - v1 x v2)
    return [a * e - (b * f + c * g + d * h),
            a * f + e * b - (c * h - d * g),
            a * g + e * c - (d * f - b * h),
            a * h + e * d - (b * g - c * f)]


def qconj(q):
    return [q[0], -q[1], -q[2], -q[3]]


def Ulink(Aj):
    u = Aj[0] * Aj[0] + Aj[1] * Aj[1] + Aj[2] * Aj[2]
    c = compose(u, *ser(u.f, CC))
    s = compose(u, *ser(u.f, SS))
    return [c, s * Aj[0], s * Aj[1], s * Aj[2]]


def logq(q):
    u = q[1] * q[1] + q[2] * q[2] + q[3] * q[3]
    g = compose(u, *ser(u.f, AS))
    return [g * q[1], g * q[2], g * q[3]]


class Box:
    def __init__(self, n, d):
        self.n, self.d = n, d
        sites = [tuple(s) for s in np.ndindex(*(n,) * d)]
        self.links = [(x, mu) for x in sites for mu in range(d) if x[mu] + 1 < n]
        # comb tree: link along mu is in the tree if all coordinates after mu are 0
        self.tree = {(x, mu) for (x, mu) in self.links if all(x[nu] == 0 for nu in range(mu + 1, d))}
        self.free = [l for l in self.links if l not in self.tree]
        self.idx = {l: i for i, l in enumerate(self.free)}
        self.N = 3 * len(self.free)
        self.plaqs = [plaq(x, mu, nu) for x in sites for mu in range(d) for nu in range(mu + 1, d)
                      if x[mu] + 1 < n and x[nu] + 1 < n]
        # curl matrix on free links
        D = np.zeros((len(self.plaqs), len(self.free)))
        for p, path in enumerate(self.plaqs):
            for x, mu, s in path:
                if (x, mu) in self.idx:
                    D[p, self.idx[(x, mu)]] += s
        self.D = D
        self.c = np.linalg.inv(D.T @ D)

    def jets(self, A):
        N = self.N
        Z = np.zeros((N, N))
        U = {}
        for l in self.links:
            if l in self.idx:
                i = 3 * self.idx[l]
                comp = []
                for a in range(3):
                    g = np.zeros(N)
                    g[i + a] = 1
                    comp.append(J(A[i + a], g, Z.copy()))
                U[l] = Ulink(comp)
            else:
                g0 = np.zeros(N)
                U[l] = [J(1.0, g0.copy(), Z.copy())] + [J(0.0, g0.copy(), Z.copy()) for _ in range(3)]
        return U

    def holonomy(self, U, path):
        q = None
        for x, mu, s in path:
            u = U[(x, mu)]
            if s < 0:
                u = qconj(u)
            q = u if q is None else qmul(q, u)
        return q

    def objective(self, A, srcs):
        U = self.jets(A)
        F = J(0.0, np.zeros(self.N), np.zeros((self.N, self.N)))
        for path in self.plaqs:
            F = F + (1.0 - 1.0 * self.holonomy(U, path)[0]) * 1.0
        for path, tau in srcs:
            psi = logq(self.holonomy(U, path))
            for a in range(3):
                if tau[a] != 0:
                    F = F - tau[a] * psi[a]
        return F

    def minimise(self, srcs):
        A = np.zeros(self.N)
        for it in range(30):
            F = self.objective(A, srcs)
            step = np.linalg.solve(F.H, -F.g)
            A = A + step
            if np.linalg.norm(step) < 1e-14:
                break
        return self.objective(A, srcs).f

    def third(self, paths, h):
        eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
        tot = 0.0
        for (a, b, c), e in eps.items():
            acc = 0.0
            for s1 in (1, -1):
                for s2 in (1, -1):
                    for s3 in (1, -1):
                        t = [np.zeros(3) for _ in range(3)]
                        t[0][a] = s1 * h
                        t[1][b] = s2 * h
                        t[2][c] = s3 * h
                        srcs = [(paths[i], t[i]) for i in range(3)]
                        acc += s1 * s2 * s3 * (-self.minimise(srcs))
            tot += e * acc / (8 * h ** 3)
        return tot / 4

    def formula(self, paths):
        Es = []
        for p in paths:
            j = np.zeros(len(self.free))
            for x, mu, s in p:
                if (x, mu) in self.idx:
                    j[self.idx[(x, mu)]] += s
            Es.append(self.c @ j)
        def val(E, b):
            x, mu, s = b
            return s * E[self.idx[(x, mu)]] if (x, mu) in self.idx else 0.0
        def lev(path, E, F):
            e = [val(E, b) for b in path]
            f = [val(F, b) for b in path]
            return sum(e[s] * f[t] - e[t] * f[s] for s in range(len(e)) for t in range(s + 1, len(e)))
        kc = -12 * (lev(paths[0], Es[1], Es[2]) + lev(paths[1], Es[2], Es[0]) + lev(paths[2], Es[0], Es[1]))
        kv = 0.0
        for path in self.plaqs:
            inc = [[val(E, b) for b in path] for E in Es]
            P = [sum(i) for i in inc]
            for s in range(4):
                for t in range(s + 1, 4):
                    kv += np.linalg.det(np.array([[P[k], inc[k][s], inc[k][t]] for k in range(3)]))
        return kc, 12 * kv


def A4():
    for (n, d, base) in [(2, 3, (0, 0, 0)), (2, 4, (0, 0, 0, 0))]:
        t0 = time.time()
        B = Box(n, d)
        paths = [plaq(base, 0, 1), plaq(base, 1, 2), plaq(base, 2, 0)]
        kc, kv = B.formula(paths)
        w1 = B.third(paths, 0.04)
        w2 = B.third(paths, 0.02)
        rich = (4 * w2 - w1) / 3
        print(f"A4 box n={n} d={d} dof={B.N}: formula K_comp {kc:.6f} K_vert {kv:.6f} total {kc+kv:.6f}; min-tree h=.04 {w1:.6f} h=.02 {w2:.6f} Rich {rich:.6f}; rel diff {abs(rich-kc-kv)/abs(kc+kv):.1e} {'PASS' if abs(rich-kc-kv)<1e-3*abs(kc+kv) else 'FAIL'} ({time.time()-t0:.0f}s)", flush=True)


def A5():
    d = 2
    rows = []
    for T in (16, 32, 64):
        c = T // 2
        p1 = plaq((c, c), 0, 1)
        l2, e2 = line((c, c), 0, 3)
        p2 = lasso(l2, plaq(e2, 0, 1))
        l3, e3 = line((c, c), 1, 3)
        p3 = lasso(l3, plaq(e3, 0, 1))
        paths = [p1, p2, p3]
        Es = [green(current(p, T, d), T, d) for p in paths]
        kc = K_comp(paths, Es, T)
        kv = 12 * sumV(*Es, T, d)
        rows.append((T, kc, kv, kc + kv))
        print(f"A5 d=2 T={T}: K_comp {kc:.5f} K_vert {kv:.5f} K_total {kc+kv:.6f}")
    r1, r2 = rows[0][3] / rows[1][3], rows[1][3] / rows[2][3]
    print(f"A5 ratios {r1:.2f} {r2:.2f}, {'PASS' if 3 < r1 < 5 and 3 < r2 < 5 else 'CHECK'}")


if __name__ == "__main__":
    A1()
    A3()
    A2([8, 16, 24, 32] if "big" in sys.argv else [8, 16])
    A5()
    A4()
