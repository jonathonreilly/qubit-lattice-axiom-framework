"""c36: session 20 (PROOF.md [S20]). Exact lift (A), critical branch + Schur complement on a d = 2 SU(2) model (B),
c35 C2 in exact rational arithmetic on Z^4 (C), level-1 trivial-background gap/decay by the Schur formula (D).
Criteria: checks/c36_criteria.md (written first). Usage: python3 c36_nah1.py A|B|C|D."""
import itertools
import os
import resource
import sys
import time
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20


# ======================================================================================================================
# common: SU(2)
SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
TAU = 1j * SIG / np.sqrt(2)          # orthonormal for -tr(XY)
I2 = np.eye(2, dtype=complex)


def su2_exp(x):
    x = np.asarray(x, float)
    th = np.linalg.norm(x, axis=-1) / np.sqrt(2)
    with np.errstate(invalid="ignore", divide="ignore"):
        nh = np.where(th[..., None] > 0, x / (np.sqrt(2) * np.where(th > 0, th, 1)[..., None]), 0.0)
    nsig = np.einsum("...a,aij->...ij", nh, SIG)
    return np.cos(th)[..., None, None] * np.eye(2) + 1j * np.sin(th)[..., None, None] * nsig


def dag(V):
    return np.conj(np.swapaxes(V, -1, -2))


def su2_coef(X):
    """coefficients of an su(2) matrix in the tau basis."""
    return np.array([-np.real(np.trace(TAU[a] @ X)) for a in range(3)])


def su2_log(V):
    """principal log of V in SU(2) (as a matrix)."""
    c = np.clip(np.real(np.trace(V)) / 2, -1, 1)
    th = np.arccos(c)
    if th < 1e-14:
        return 0.5 * (V - dag(V))
    return th / np.sin(th) * 0.5 * (V - dag(V))


def haar(rng, n):
    q = rng.standard_normal((n, 4)); q /= np.linalg.norm(q, axis=1)[:, None]
    return q[:, 0, None, None] * I2 + 1j * np.einsum("na,aij->nij", q[:, 1:], SIG)


def Adm(V):
    Vd = dag(V)
    return -np.real(np.einsum("aij,jk,bkl,li->ab", TAU, V, TAU, Vd))


# ======================================================================================================================
# common: lattice geometry on a torus (unwrapped steps, coordinates taken mod n when indexing)
class Lat:
    def __init__(self, d, L, T):
        self.d, self.L, self.T = d, L, T
        self.n = T * L
        self.sites = list(itertools.product(range(self.n), repeat=d))
        self.sidx = {s: i for i, s in enumerate(self.sites)}
        self.ns = len(self.sites); self.nl = self.ns * d
        self.blocks = list(itertools.product(range(T), repeat=d)); self.bidx = {X: i for i, X in enumerate(self.blocks)}
        self.nb = len(self.blocks)
        self.h = (L - 1) // 2
        self.orders = list(itertools.permutations(range(d)))

    def sid(self, x):
        return self.sidx[tuple(int(v) % self.n for v in x)]

    def lid(self, x, mu):
        return self.sid(x) * self.d + mu

    def centre(self, X):
        return tuple(self.L * Xi + self.h for Xi in X)

    def block_of(self, x):
        return tuple((int(v) % self.n) // self.L for v in x)

    def block_sites(self, X):
        return [tuple(self.L * Xi + yi for Xi, yi in zip(X, y)) for y in itertools.product(range(self.L), repeat=self.d)]


def axial_steps(c, y, order):
    x = list(c); out = []
    for mu in order:
        while x[mu] != y[mu]:
            if y[mu] > x[mu]:
                out.append((tuple(x), mu, +1)); x[mu] += 1
            else:
                xb = list(x); xb[mu] -= 1; out.append((tuple(xb), mu, -1)); x[mu] -= 1
    return out


def contour_steps(G, X, mu, order, y):
    cX = G.centre(X)
    Y = list(X); Y[mu] += 1; cY = G.centre(Y)
    st = axial_steps(cX, y, order)
    z = list(y)
    for _ in range(G.L):
        st.append((tuple(z), mu, +1)); z[mu] += 1
    back = axial_steps(cY, tuple(z), order)
    st += [(xb, nu, -s) for (xb, nu, s) in reversed(back)]
    return st


# ======================================================================================================================
# Part C: exact rational rows of O~_0 on Z^4
def part_C():
    t0 = time.time(); ok = {}
    d, L = 4, 3
    kap = Fraction(1)
    norm = Fraction(1, 24 * L ** d)
    orders = list(itertools.permutations(range(d)))
    h = (L - 1) // 2
    c0 = (h,) * d

    def bl(x):  # block of a Z^4 site
        return tuple(v // L for v in x)

    def add(dct, k, v):
        if v:
            nv = dct.get(k, 0) + v
            if nv:
                dct[k] = nv
            else:
                dct.pop(k, None)

    # slice template w (block at the origin), Q templates per direction
    wt = {}
    for y in itertools.product(range(L), repeat=d):
        for o in orders:
            for (xb, mu, s) in axial_steps(c0, y, o):
                wt[(xb, mu)] = wt.get((xb, mu), 0) + s
    w = {k: v * norm for k, v in wt.items() if v != 0}
    w2 = sum(v * v for v in w.values()); w1 = sum(abs(v) for v in w.values()); wmax = max(abs(v) for v in w.values())
    qt = []
    for mu in range(d):
        acc = {}
        for y in itertools.product(range(L), repeat=d):
            Gd = type("G", (), {})(); Gd.L = L
            Gd.centre = lambda X: tuple(L * Xi + h for Xi in X)
            for o in orders:
                for (xb, nu, s) in contour_steps(Gd, (0,) * d, mu, o, y):
                    acc[(xb, nu)] = acc.get((xb, nu), 0) + s
        qt.append({k: v * norm for k, v in acc.items() if v != 0})
    # inverse index of Q: for fine direction nu and residue class r = x mod L -> list of (mu, relpos, coef)
    qinv = {}
    for mu in range(d):
        for (xb, nu), v in qt[mu].items():
            r = tuple(c % L for c in xb)
            qinv.setdefault((nu, r), []).append((mu, xb, v))
    print(f"C: templates built: |w| = {len(w)}, |Q_mu| = {[len(q) for q in qt]}, w2 = {w2}  ({time.time()-t0:.1f} s)",
          flush=True)
    E = [tuple(int(i == j) for i in range(d)) for j in range(d)]

    def plus(x, mu, s=1):
        return tuple(x[i] + s * E[mu][i] for i in range(d))

    def Pi(v):
        out = dict(v)
        blocks = {}
        for (x, mu), a in v.items():
            if bl(x) == bl(plus(x, mu)):
                X = bl(x); key = (tuple(x[i] - L * X[i] for i in range(d)), mu)
                if key in w:
                    blocks[X] = blocks.get(X, 0) + w[key] * a
        for X, s in blocks.items():
            if s:
                for (xb, mu), wv in w.items():
                    add(out, (tuple(xb[i] + L * X[i] for i in range(d)), mu), -wv * s / w2)
        return out

    def dd(v):
        F = {}
        for (y, a), val in v.items():
            for mu in range(d):
                for nu in range(mu + 1, d):
                    if a == mu:
                        add(F, (y, mu, nu), val)                 # A_mu(x), x = y
                        add(F, (plus(y, nu, -1), mu, nu), -val)  # A_mu(x + e_nu)
                    if a == nu:
                        add(F, (plus(y, mu, -1), mu, nu), val)   # A_nu(x + e_mu)
                        add(F, (y, mu, nu), -val)                # A_nu(x)
        out = {}
        for (x, mu, nu), f in F.items():
            add(out, (x, mu), f); add(out, (plus(x, nu), mu), -f)
            add(out, (plus(x, mu), nu), f); add(out, (x, nu), -f)
        return out

    def QtQ(v):
        cv = {}
        for (x, nu), val in v.items():
            r = tuple(c % L for c in x)
            for (mu, xb, q) in qinv.get((nu, r), ()):
                X = tuple((x[i] - xb[i]) // L for i in range(d))
                add(cv, (X, mu), q * val)
        out = {}
        for (X, mu), cval in cv.items():
            for (xb, nu), q in qt[mu].items():
                add(out, (tuple(xb[i] + L * X[i] for i in range(d)), nu), q * cval)
        return out

    nB = L ** d - 1

    def fix(v):  # d0 P_res d0^T v
        f = {}
        for (x, mu), val in v.items():
            add(f, plus(x, mu), val); add(f, x, -val)       # (d0^T v)(s) = sum_mu v(s - e_mu, mu) - v(s, mu)
        # P_res per block
        byb = {}
        for s, val in f.items():
            byb.setdefault(bl(s), {})[s] = val
        g = {}
        for X, fs in byb.items():
            cX = tuple(L * X[i] + h for i in range(d))
            fs = dict(fs); fs.pop(cX, None)
            m = sum(fs.values())
            if m:
                for y in itertools.product(range(L), repeat=d):
                    s = tuple(L * X[i] + y[i] for i in range(d))
                    if s != cX:
                        add(fs, s, -m / nB)
            for s, val in fs.items():
                add(g, s, val)
        out = {}
        for s, val in g.items():
            for mu in range(d):
                add(out, (s, mu), -val); add(out, (plus(s, mu, -1), mu), val)   # (d0 g)(x, mu) = g(x+e_mu) - g(x)
        return out

    def O(v):
        out = dd(v)
        for k, val in QtQ(v).items():
            add(out, k, kap * val)
        for k, val in fix(v).items():
            add(out, k, val)
        return out

    def Ot(v):
        pv = Pi(v)
        out = Pi(O(pv))
        for k, val in v.items():
            add(out, k, val)
        for k, val in pv.items():
            add(out, k, -val)
        return out

    links0 = [(x, mu) for x in itertools.product(range(L), repeat=d) for mu in range(d)]
    rows = {}; rng_ok = True; Nmax = Fraction(0); M1max = Fraction(0); dmax = 0; nuw = Fraction(0)
    for j, b in enumerate(links0):
        r = Ot({b: Fraction(1)})
        rows[b] = r
        x0 = b[0]
        S = Fraction(0); S1 = Fraction(0)
        for (x, mu), val in r.items():
            if any(not (-1 <= v // L <= 1) for v in x):
                rng_ok = False
            dist = sum(abs(x[i] - x0[i]) for i in range(d))
            dmax = max(dmax, dist)
            S += abs(val); S1 += abs(val) * dist
        Nmax = max(Nmax, S); M1max = max(M1max, S1)
        # 1 - Pi row
        omp = {k: val for k, val in {b: Fraction(1)}.items()}
        pv = Pi({b: Fraction(1)})
        one_m = {}
        for k, val in omp.items():
            add(one_m, k, val)
        for k, val in pv.items():
            add(one_m, k, -val)
        nuw = max(nuw, sum(abs(v) for v in one_m.values()))
        if j % 27 == 0:
            print(f"  row {j}/324: nnz {len(r)}, running N = {float(Nmax):.6f}, M1 = {float(M1max):.6f}  "
                  f"({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)", flush=True)
    ok["C1"] = rng_ok and nuw == Fraction(30, 13) and dmax <= 20
    sym = all(rows[b].get(bp, 0) == rows[bp].get(b, 0) for b in links0 for bp in links0)
    ok["C2"] = sym
    Nf, M1f = float(Nmax), float(M1max)
    ok["C3"] = abs(Nf - 25.4760) <= 1e-5 * 25.4760 and abs(M1f - 41.0765) <= 1e-5 * 41.0765 and M1max <= Fraction(41077, 1000)
    gam0 = Fraction(1, 3500000) * Fraction(1, 2) / 9
    m = Fraction(193, 10 ** 12); m4 = Fraction(966, 10 ** 13)
    lhs = M1max * m * (1 + 40 * m); lhs4 = M1max * m4 * (1 + 40 * m4)
    ok["C4"] = lhs <= gam0 / 2 and 20 * m <= 1
    print(f"C1: range inside 3^4 blocks (exact zeros elsewhere): {rng_ok}; nu_w = {nuw}; max support distance {dmax}")
    print(f"C2: exact symmetry on the reference block: {sym}")
    print(f"C3: N_exact = {Nmax} = {Nf:.10f}; M1_exact = {M1max} = {M1f:.10f}  (c35 floats 25.4760, 41.0765)")
    print(f"C4: gamma_0/2 = {float(gam0/2):.10e}; M1*m*(1+40m) = {float(lhs):.10e} at m = 1.93e-10: {lhs <= gam0/2}; "
          f"at m_4 = 9.66e-11: M1*m4*(1+40m4) = {float(lhs4):.6e} <= gamma_0/4 = {float(gam0/4):.6e}: {lhs4 <= gam0/4}")
    for k in sorted(ok):
        print(k, "PASS" if ok[k] else "FAIL")
    print(f"Part C: {'PASS' if all(ok.values()) else 'FAIL'} (time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")



# ======================================================================================================================
# helpers for A and B (non-abelian, any d)
def path_prod(U, G, steps):
    P = I2.copy()
    for (xb, mu, s) in steps:
        b = G.lid(xb, mu)
        P = P @ (U[b] if s > 0 else dag(U[b]))
    return P


def lift(G, V):
    """exact lift U^(0)(V): 1 on block-interior links, V_(X, mu) on the crossing link of direction mu."""
    U = np.tile(I2, (G.nl, 1, 1))
    for x in G.sites:
        X = G.block_of(x)
        for mu in range(G.d):
            xp = list(x); xp[mu] += 1
            if G.block_of(xp) != X:
                U[G.lid(x, mu)] = V[G.bidx[X] * G.d + mu]
    return U


def coarse_plus(G, X, mu):
    Y = list(X); Y[mu] = (Y[mu] + 1) % G.T
    return tuple(Y)


def Mbar(G, U, X, mu):
    acc = np.zeros((2, 2), complex); n = 0
    for y in G.block_sites(X):
        for o in G.orders:
            acc += path_prod(U, G, contour_steps(G, X, mu, o, y)); n += 1
    return acc / n


def part_A():
    t0 = time.time(); ok = {}
    G = Lat(4, 3, 2); d = 4
    rng = np.random.default_rng(36001)
    nc = G.nb * d
    V = su2_exp(0.7 * rng.standard_normal((nc, 3)))
    g = haar(rng, G.nb)
    def gauge(V, g):
        W = V.copy()
        for iX, X in enumerate(G.blocks):
            for mu in range(d):
                W[iX * d + mu] = g[iX] @ V[iX * d + mu] @ dag(g[G.bidx[coarse_plus(G, X, mu)]])
        return W
    V = gauge(V, g)
    U = lift(G, V)
    eA1 = 0.0; eA4 = 0.0
    for iX, X in enumerate(G.blocks):
        for mu in range(d):
            Mb = Mbar(G, U, X, mu)
            eA1 = max(eA1, np.linalg.norm(Mb - V[iX * d + mu]))
            W0 = Mb / np.sqrt(np.linalg.det(Mb))
            eA4 = max(eA4, np.linalg.norm(su2_log(dag(V[iX * d + mu]) @ W0)))
    print(f"A1: max ||Mbar - V|| = {eA1:.2e}  ({time.time()-t0:.0f} s)", flush=True)
    eA2n = 0.0; eA2c = 0.0; ncorner = 0
    for x in G.sites:
        for mu in range(d):
            for nu in range(mu + 1, d):
                xm = list(x); xm[mu] += 1; xn = list(x); xn[nu] += 1
                Up = U[G.lid(x, mu)] @ U[G.lid(xm, nu)] @ dag(U[G.lid(xn, mu)]) @ dag(U[G.lid(x, nu)])
                if x[mu] % 3 == 2 and x[nu] % 3 == 2:
                    X = G.block_of(x); Xm = coarse_plus(G, X, mu); Xn = coarse_plus(G, X, nu)
                    VP = V[G.bidx[X] * d + mu] @ V[G.bidx[Xm] * d + nu] @ dag(V[G.bidx[Xn] * d + mu]) @ dag(V[G.bidx[X] * d + nu])
                    eA2c = max(eA2c, np.linalg.norm(Up - VP)); ncorner += 1
                else:
                    eA2n = max(eA2n, np.linalg.norm(Up - I2))
    g2 = haar(rng, G.nb)
    U2 = lift(G, gauge(V, g2))
    ghat = np.array([g2[G.bidx[G.block_of(x)]] for x in G.sites])
    eA3 = 0.0
    for x in G.sites:
        for mu in range(d):
            xp = list(x); xp[mu] += 1
            b = G.lid(x, mu)
            eA3 = max(eA3, np.linalg.norm(U2[b] - ghat[G.sid(x)] @ U[b] @ dag(ghat[G.sid(xp)])))
    ok["A1"] = eA1 <= 1e-12; ok["A2"] = eA2n <= 1e-12 and eA2c <= 1e-12; ok["A3"] = eA3 <= 1e-12; ok["A4"] = eA4 <= 1e-12
    print(f"A2: non-corner max ||U_p - 1|| = {eA2n:.2e}; corner ({ncorner}) max ||U_p - V_P|| = {eA2c:.2e}")
    print(f"A3: gauge covariance {eA3:.2e}; A4: max |rho_c| = {eA4:.2e}")
    for k in sorted(ok):
        print(k, "PASS" if ok[k] else "FAIL")
    print(f"Part A: {'PASS' if all(ok.values()) else 'FAIL'} (time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")


# ======================================================================================================================
# Part B: d = 2 SU(2) model
class Model2:
    def __init__(self, kappa=1.0):
        self.G = G = Lat(2, 3, 2); self.d = 2; self.kappa = kappa
        self.contours = []          # per coarse link: list of steps lists
        for iX, X in enumerate(G.blocks):
            for mu in range(2):
                self.contours.append([[(G.lid(xb, nu), s) for (xb, nu, s) in contour_steps(G, X, mu, o, y)]
                                      for y in G.block_sites(X) for o in G.orders])
        self.plaqs = []
        for x in G.sites:
            xm = list(x); xm[0] += 1; xn = list(x); xn[1] += 1
            self.plaqs.append([(G.lid(x, 0), 1), (G.lid(xm, 1), 1), (G.lid(xn, 0), -1), (G.lid(x, 1), -1)])
        self.nl = G.nl; self.nc = G.nb * 2

    @staticmethod
    def prod(U, st):
        P = I2.copy()
        for (b, s) in st:
            P = P @ (U[b] if s > 0 else dag(U[b]))
        return P

    def F(self, U, V):
        S = sum(np.real(np.trace(I2 - self.prod(U, st))) for st in self.plaqs)
        for c, cl in enumerate(self.contours):
            Mb = sum(self.prod(U, st) for st in cl) / len(cl)
            S += self.kappa * (2 * np.sqrt(np.real(np.linalg.det(Mb))) - np.real(np.trace(dag(V[c]) @ Mb)))
        return S

    @staticmethod
    def dpath(U, st, K, gU, w):
        """add w * d/de Re tr(K P) (left perturbations) into gU (nl, 3)."""
        Ws = [U[b] if s > 0 else dag(U[b]) for (b, s) in st]
        n = len(Ws)
        pre = [I2]
        for W in Ws:
            pre.append(pre[-1] @ W)
        suf = [I2] * (n + 1)
        for j in range(n - 1, -1, -1):
            suf[j] = Ws[j] @ suf[j + 1]
        for j, (b, s) in enumerate(st):
            if s > 0:
                Pr, Sf, sg = pre[j], suf[j], 1.0
            else:
                Pr, Sf, sg = pre[j + 1], suf[j + 1], -1.0
            Z = Sf @ K @ Pr
            for a in range(3):
                gU[b, a] += w * sg * np.real(np.trace(Z @ TAU[a]))

    def grad(self, U, V):
        gU = np.zeros((self.nl, 3)); gV = np.zeros((self.nc, 3))
        for st in self.plaqs:
            self.dpath(U, st, -I2, gU, 1.0)
        for c, cl in enumerate(self.contours):
            Mb = sum(self.prod(U, st) for st in cl) / len(cl)
            sd = np.sqrt(np.real(np.linalg.det(Mb)))
            K = sd * np.linalg.inv(Mb) - dag(V[c])
            for st in cl:
                self.dpath(U, st, K, gU, self.kappa / len(cl))
            for a in range(3):
                gV[c, a] = self.kappa * np.real(np.trace(Mb @ dag(V[c]) @ TAU[a]))
        return gU, gV

    def hess(self, U, V, h=1e-5):
        nA, nB = 3 * self.nl, 3 * self.nc
        H = np.zeros((nA + nB, nA + nB))
        for i in range(nA + nB):
            cols = []
            for sgn in (1, -1):
                U2, V2 = U.copy(), V.copy()
                if i < nA:
                    b, a = divmod(i, 3); U2[b] = su2_exp(sgn * h * np.eye(3)[a]) @ U[b]
                else:
                    c, a = divmod(i - nA, 3); V2[c] = su2_exp(sgn * h * np.eye(3)[a]) @ V[c]
                gU, gV = self.grad(U2, V2)
                cols.append(np.concatenate([gU.ravel(), gV.ravel()]))
            H[:, i] = (cols[0] - cols[1]) / (2 * h)
        return (H + H.T) / 2

    def gauge_ops(self, U):
        G = self.G; q = 3; norm = 1.0 / (len(G.orders) * G.L ** 2)
        AdU = np.array([Adm(u) for u in U])
        h = np.zeros((q * G.nb, q * G.nl)); M = np.zeros((q * G.nb, q * G.ns))
        for iX, X in enumerate(G.blocks):
            cX = G.centre(X)
            for y in G.block_sites(X):
                for o in G.orders:
                    Tm = np.eye(3)
                    for (xb, mu, s) in axial_steps(cX, y, o):
                        b = G.lid(xb, mu)
                        if s > 0:
                            h[q*iX:q*iX+q, q*b:q*b+q] += norm * Tm; Tm = Tm @ AdU[b]
                        else:
                            Tm = Tm @ AdU[b].T; h[q*iX:q*iX+q, q*b:q*b+q] += -norm * Tm
                    sy = G.sid(y)
                    M[q*iX:q*iX+q, q*sy:q*sy+q] += norm * Tm
        D = np.zeros((q * G.nl, q * G.ns))
        for x in G.sites:
            s_ = G.sid(x)
            for mu in range(2):
                b = s_ * 2 + mu; xp = list(x); xp[mu] += 1; sp_ = G.sid(xp)
                D[q*b:q*b+q, q*sp_:q*sp_+q] += AdU[b]; D[q*b:q*b+q, q*s_:q*s_+q] -= np.eye(3)
        mask = np.ones(q * G.ns)
        for X in G.blocks:
            sc = G.sid(G.centre(X)); mask[q*sc:q*sc+q] = 0
        Mm = M * mask[None, :]
        Pl = np.diag(mask)
        Pres = Pl - Mm.T @ np.linalg.solve(Mm @ Mm.T, Mm)
        Pi = np.eye(q * G.nl) - h.T @ np.linalg.solve(h @ h.T, h)
        return dict(h=h, D=D, Pres=Pres, Pi=Pi, mask=mask)

    @staticmethod
    def cov(HAA, ops, w=1.0):
        Pi = ops["Pi"]; n = Pi.shape[0]
        O = HAA + w * ops["D"] @ ops["Pres"] @ ops["D"].T
        Ot = Pi @ O @ Pi + (np.eye(n) - Pi)
        return Pi @ np.linalg.inv(Ot) @ Pi, Ot


def ad3(A):
    """ad_A in the tau basis: [A, tau_b] = sum_a (ad_A)_{ab} tau_a."""
    Am = np.einsum("a,aij->ij", A, TAU)
    return np.array([[su2_coef(Am @ TAU[b] - TAU[b] @ Am)[a] for b in range(3)] for a in range(3)])


def dexp(A):
    X = ad3(A); out = np.eye(3); term = np.eye(3)
    for k in range(1, 25):
        term = term @ X / (k + 1); out = out + term
    return out


def branch(m, V, tol=1e-13, maxit=200):
    U0 = lift(m.G, V)
    H0 = m.hess(U0, V)[:3 * m.nl, :3 * m.nl]
    ops0 = m.gauge_ops(U0)
    C0, _ = m.cov(H0, ops0)
    fix = ops0["D"] @ ops0["Pres"] @ ops0["D"].T
    A = np.zeros(3 * m.nl); hist = []
    for it in range(maxit):
        U = np.array([su2_exp(A[3*b:3*b+3]) @ U0[b] for b in range(m.nl)])
        gU, _ = m.grad(U, V)
        gch = np.concatenate([dexp(A[3*b:3*b+3]).T @ gU[b] for b in range(m.nl)])
        Gv = ops0["Pi"] @ (gch + fix @ A)
        r = np.linalg.norm(Gv); hist.append(r)
        if r <= tol:
            break
        A = A - C0 @ Gv
    U = np.array([su2_exp(A[3*b:3*b+3]) @ U0[b] for b in range(m.nl)])
    return U, A, U0, ops0, hist


def part_B():
    t0 = time.time(); ok = dict(B1=True, B2=True, B3=True)
    m = Model2(1.0); G = m.G
    rng = np.random.default_rng(36002)
    nA, nB = 3 * m.nl, 3 * m.nc
    for t in (0.05, 0.15):
        V = su2_exp(t * rng.standard_normal((m.nc, 3)))
        g = haar(rng, G.nb)
        for iX, X in enumerate(G.blocks):
            for mu in range(2):
                V[iX*2+mu] = g[iX] @ V[iX*2+mu] @ dag(g[G.bidx[coarse_plus(G, X, mu)]])
        U, A, U0, ops0, hist = branch(m, V)
        gU, gV = m.grad(U, V)
        fixres = np.linalg.norm(ops0["Pres"] @ ops0["D"].T @ A)
        hres = np.linalg.norm(ops0["h"] @ A)
        b1 = hist[-1] <= 1e-11 and np.abs(gU).max() <= 1e-9 and fixres <= 1e-9
        ok["B1"] &= b1
        print(f"B1 t={t}: iterations {len(hist)}, residuals {' '.join(f'{r:.1e}' for r in hist[:6])} ... {hist[-1]:.1e}; "
              f"max|grad_U F| at branch {np.abs(gU).max():.1e}; ||P_res D^* A*|| {fixres:.1e}; ||h A*|| {hres:.1e}; "
              f"max|A*| {np.abs(A).max():.3e}  ({time.time()-t0:.0f} s)", flush=True)
        H = m.hess(U, V)
        HAA, HAB, HBB = H[:nA, :nA], H[:nA, nA:], H[nA:, nA:]
        ops = m.gauge_ops(U)
        C, Ot = m.cov(HAA, ops)
        H1 = HBB - HAB.T @ C @ HAB
        C3, _ = m.cov(HAA, ops, w=3.0)
        H1w = HBB - HAB.T @ C3 @ HAB
        fixdep = np.abs(H1w - H1).max() / np.abs(H1).max()
        lam = rng.standard_normal(3 * G.ns) * ops["mask"]
        inv = np.linalg.norm(HAA @ (ops["D"] @ lam)) / np.linalg.norm(lam)
        ok["B3"] &= inv <= 1e-7 and fixdep <= 1e-8
        print(f"B3 t={t}: ||Hess(D lam)||/||lam|| = {inv:.1e}; fixing-weight dependence of the Schur result {fixdep:.1e}")

        def Ebr(Vs):
            # re-solve the branch at Vs from the branch at V, preconditioned by C (gauge-invariant value E^br)
            Us = U.copy(); gmax = np.inf
            for it in range(400):
                gs, _ = m.grad(Us, Vs); gmax = np.abs(gs).max()
                if gmax <= 1e-13:
                    break
                dl = -(C @ gs.ravel())
                Us = np.array([su2_exp(dl[3*bb:3*bb+3]) @ Us[bb] for bb in range(m.nl)])
            gres.append(gmax)
            return m.F(Us, Vs), gmax
        gres = []
        errs = []
        for k in range(6):
            Bd = rng.standard_normal((m.nc, 3)); Bd /= np.linalg.norm(Bd)
            def E_at(s):
                Vs = np.array([su2_exp(s * Bd[c]) @ V[c] for c in range(m.nc)])
                return Ebr(Vs)[0]
            def D4(hh):
                e = [E_at(j * hh) for j in (-2, -1, 0, 1, 2)]
                return (-e[0] + 16 * e[1] - 30 * e[2] + 16 * e[3] - e[4]) / (12 * hh * hh)
            d1, d2 = D4(1e-3), D4(5e-4)
            fd = (16 * d2 - d1) / 15
            sc = Bd.ravel() @ H1 @ Bd.ravel()
            errs.append(abs(fd - sc) / abs(sc))
        ok["B2"] &= max(errs) <= 1e-5
        print(f"B2 t={t}: relative errors FD vs Schur {' '.join(f'{e:.1e}' for e in errs)}; max re-solve gradient "
              f"{max(gres):.1e}  ({time.time()-t0:.0f} s)", flush=True)
        # B4 informational
        lmin0 = np.linalg.eigvalsh(Ot)[0]
        # level-1 gauge directions: coarse covariant derivative of V on the coarse torus
        Dc = np.zeros((nB, 3 * G.nb))
        for iX, X in enumerate(G.blocks):
            for mu in range(2):
                c = iX * 2 + mu; Y = G.bidx[coarse_plus(G, X, mu)]
                Dc[3*c:3*c+3, 3*Y:3*Y+3] += Adm(V[c]); Dc[3*c:3*c+3, 3*iX:3*iX+3] -= np.eye(3)
        Qg, _ = np.linalg.qr(Dc)
        rk = np.linalg.matrix_rank(Dc)
        Pc = np.eye(nB) - Qg[:, :rk] @ Qg[:, :rk].T
        ev = np.linalg.eigvalsh(Pc @ H1 @ Pc)
        nz = ev[np.abs(ev) > 1e-10]
        print(f"B4 t={t}: lambda_min(O~ at branch) = {lmin0:.6f}; Schur Hessian on the complement of coarse gauge directions: "
              f"min nonzero eigenvalue {nz.min() if len(nz) else float('nan'):.6f} (rank of gauge span {rk})")
    for k in sorted(ok):
        print(k, "PASS" if ok[k] else "FAIL")
    print(f"Part B: {'PASS' if all(ok.values()) else 'FAIL'} (time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")



# ======================================================================================================================
# Part D: level 1 at the trivial background (abelian), by the Schur formula in Bloch form
def part_D():
    import scipy.fft as sfft
    import c35_n5bg as C5
    t0 = time.time(); ok = {}
    L, d, kap = 3, 4, 1.0
    G = C5.Geo(4, 3, 3)
    op0 = C5.AbOp(G, kappa=kap)
    oploc = C5.AbOp(G, kappa=kap, a_ww=0.0)
    blk0 = [b for b in range(G.nl) if G.block_of_site(b // 4) == (0, 0, 0, 0)]
    nloc = len(blk0)
    E = np.zeros((G.nl, nloc)); E[blk0, np.arange(nloc)] = 1
    bsite = np.arange(G.nl) // 4
    Bk = G.coords[bsite] // L
    shift = np.where(Bk == 2, -1, Bk)
    bloc = {b: k for k, b in enumerate(blk0)}
    loc_of = np.zeros(G.nl, int)
    for b in range(G.nl):
        xl = tuple(G.coords[b // 4] % L); loc_of[b] = bloc[G.lid(xl, b % 4)]
    shifts = list(itertools.product((-1, 0, 1), repeat=4)); sidx = {sh: i for i, sh in enumerate(shifts)}
    sh_of = np.array([sidx[tuple(r)] for r in shift])
    S_arr = np.array(shifts, float)

    def build_As(cols):
        As = np.zeros((81, nloc, nloc))
        for j in range(G.nl):
            As[sh_of[j], :, loc_of[j]] += cols[j, :]
        return As
    As0 = build_As(op0.Ot(E)); Asl = build_As(oploc.Ot(E))
    PiE = op0.Pi(E)
    Pih = PiE[blk0, :]
    outside = np.abs(np.delete(PiE, blk0, axis=0)).max()
    del PiE
    # Q fibre: rows of the coarse links at coarse site 0
    iX0 = G.blocks.index((0, 0, 0, 0))
    Qc = op0.Q[iX0 * 4:(iX0 + 1) * 4, :].tocoo()
    Qs = np.zeros((81, 4, nloc))
    for r, c, v in zip(Qc.row, Qc.col, Qc.data):
        Qs[sh_of[c], r, loc_of[c]] += v
    # level-1 d*d symbol from the fine d*d rows at site 0 (unit cells = sites)
    dd = op0.dd.tocsr()
    ddS = {}
    for mu in range(4):
        row = dd.getrow(mu)
        for c, v in zip(row.indices, row.data):
            x = G.coords[c // 4]; sh = tuple(int(xi) if xi <= 1 else int(xi) - G.n for xi in x)
            ddS.setdefault(sh, np.zeros((4, 4)))[mu, c % 4] += v
    dsh = np.array(list(ddS.keys()), float); dmat = np.array(list(ddS.values()))
    print(f"D: fibres built (Pi outside block {outside:.1e}; {len(ddS)} d*d shifts)  ({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)",
          flush=True)
    # validation of the Bloch construction for O~_0 (as c35 C3) at one K
    K = 2 * np.pi * np.array([1, 2, 0, 1]) / 3
    Mk = np.tensordot(np.exp(1j * (S_arr @ K)), As0, axes=(0, 0)); Mk = (Mk + Mk.conj().T) / 2
    ew, vk = np.linalg.eigh(Mk); v = vk[:, 0]
    ext = v[loc_of] * np.exp(1j * (shift @ K))
    vres = np.linalg.norm(op0.Ot(ext.real) + 1j * op0.Ot(ext.imag) - ew[0] * ext) / np.linalg.norm(ext)
    qv = np.tensordot(np.exp(1j * (S_arr @ K)), Qs, axes=(0, 0)) @ v
    qfull = op0.Q @ ext
    qres = abs(np.linalg.norm(qfull[iX0 * 4:(iX0 + 1) * 4] - qv))
    print(f"D: Bloch validation O~_0 residual {vres:.1e}; Q fibre residual {qres:.1e}", flush=True)
    # H_1 on the level-1 momentum grid (2 pi / 12) Z^4
    n1 = 12
    H1 = np.zeros((n1,) * 4 + (4, 4), complex)
    onemPi = np.eye(nloc) - Pih
    done = np.zeros((n1,) * 4, bool)
    gauge_err = 0.0
    for idx in itertools.product(range(n1), repeat=4):
        if done[idx]:
            continue
        p = 2 * np.pi * np.array(idx) / n1
        ph = np.exp(1j * (S_arr @ p))
        Ok = np.tensordot(ph, As0, axes=(0, 0))
        Qk = np.tensordot(ph, Qs, axes=(0, 0))
        X = np.linalg.solve(Ok, Qk.conj().T)
        Hk = kap * np.eye(4) - kap * kap * (Qk @ X - Qk @ onemPi @ Qk.conj().T)
        Hk = (Hk + Hk.conj().T) / 2
        H1[idx] = Hk; done[idx] = True
        mi = tuple((-np.array(idx)) % n1)
        H1[mi] = Hk.conj(); done[mi] = True
    for idx in itertools.product(range(n1), repeat=4):
        p = 2 * np.pi * np.array(idx) / n1
        ddp = np.tensordot(np.exp(1j * (dsh @ p)), dmat, axes=(0, 0))
        if not any(idx):
            gauge_err = max(gauge_err, np.abs(H1[idx]).max()); continue
        w_, V_ = np.linalg.eigh((ddp + ddp.conj().T) / 2)
        gauge_err = max(gauge_err, np.linalg.norm(H1[idx] @ V_[:, 0]))
    ip = (6, 6, 6, 6)
    p = np.full(4, np.pi)
    ddp = np.real(np.tensordot(np.exp(1j * (dsh @ p)), dmat, axes=(0, 0)))
    w_, V_ = np.linalg.eigh((ddp + ddp.T) / 2)
    Bc = V_[:, 1:]
    A1 = Bc.conj().T @ (0.5 * H1[ip]) @ Bc; B1 = Bc.conj().T @ ddp @ Bc
    Lb = np.linalg.cholesky(B1); Li = np.linalg.inv(Lb)
    ratio = np.linalg.eigvalsh(Li @ A1 @ Li.conj().T)[0]
    ok["D1"] = gauge_err <= 1e-10 and abs(ratio - 0.030950) <= 1e-4 * 0.030950
    print(f"D1: max ||H_1(p) nu(p)|| = {gauge_err:.1e}; per-mode ratio at (pi,pi,pi,pi) = {ratio:.6f} (c31 E: 0.030950)  "
          f"({time.time()-t0:.0f} s)", flush=True)
    # level-1 operator fibres at level-2 momenta (2 pi / 4) Z^4
    n2 = 4
    pos = G.coords[np.array(blk0) // 4].astype(float); mu_of = np.array(blk0) % 4
    js = np.array(list(itertools.product(range(3), repeat=4)))
    O1 = np.zeros((n2,) * 4 + (nloc, nloc), np.complex64)
    gam1 = (np.inf, None); gam0 = (np.inf, None)
    for k2 in itertools.product(range(n2), repeat=4):
        K2 = 2 * np.pi * np.array(k2) / n2
        pidx = (np.array(k2)[None, :] + n2 * js) % n1
        pj = 2 * np.pi * pidx / n1
        Fm = np.exp(1j * (pj @ pos.T))                      # (81, 324)
        Hsel = H1[pidx[:, 0], pidx[:, 1], pidx[:, 2], pidx[:, 3]]  # (81, 4, 4)
        Hab = Hsel[:, mu_of][:, :, mu_of]                    # (81, 324, 324)
        Hf = np.zeros((nloc, nloc), complex)
        for jj in range(81):
            Hf += np.outer(Fm[jj], Fm[jj].conj()) * Hab[jj]
        Hf /= 81
        del Hab
        loc = np.tensordot(np.exp(1j * (S_arr @ K2)), Asl, axes=(0, 0))
        Ok1 = Pih @ Hf @ Pih + loc
        Ok1 = (Ok1 + Ok1.conj().T) / 2
        O1[k2] = Ok1
        l1 = np.linalg.eigvalsh(Ok1)[0]
        if l1 < gam1[0]:
            gam1 = (l1, k2)
        Ok0 = np.tensordot(np.exp(1j * (S_arr @ K2)), As0, axes=(0, 0)); Ok0 = (Ok0 + Ok0.conj().T) / 2
        l0 = np.linalg.eigvalsh(Ok0)[0]
        if l0 < gam0[0]:
            gam0 = (l0, k2)
    ok["D2"] = gam1[0] >= 1.29e-10
    print(f"D2: gamma_meas(1) = {gam1[0]:.6e} at K2 = (2pi/4){gam1[1]}; gamma_meas(0) (same grid) = {gam0[0]:.6e} at "
          f"(2pi/4){gam0[1]} (c35: 0.039849); ratio {gam1[0]/gam0[0]:.4f}; proven gamma_1 = 1.29e-10 (ratio "
          f"{gam1[0]/1.29e-10:.3e})  ({time.time()-t0:.0f} s, RSS {rss_mb():.0f} MB)", flush=True)
    # D3: real-space H_1 on the level-1 torus side 12
    Hr = np.fft.fftn(H1, axes=(0, 1, 2, 3)) / n1 ** 4     # H(r) = (1/N) sum_p H(p) e^{-i p r}
    prof = {}
    for r in itertools.product(range(n1), repeat=4):
        dist = sum(min(ri, n1 - ri) for ri in r)
        prof[dist] = max(prof.get(dist, 0.0), np.abs(Hr[r]).max())
    ds = sorted(prof)
    fitd = [dd_ for dd_ in ds if 2 <= dd_ <= 10]
    slope = np.polyfit(fitd, np.log([prof[x] for x in fitd]), 1)[0]
    print("D3: max |H_1(r)| by l1 distance: " + " ".join(f"{x}:{prof[x]:.2e}" for x in ds[:16]) +
          f"; fitted rate (r = 2..10) {-slope:.3f}", flush=True)
    del Hr
    # rows of O~_1 on the level-2 torus of side 4 (aliased) and of O~_0 (exact range)
    A0 = np.abs(As0)
    N0 = A0.sum((0, 2)).max()
    M0rows = np.zeros(nloc)
    for si in range(81):
        dist0 = np.abs(pos[None, :, :] + 3 * S_arr[si][None, None, :] - pos[:, None, :]).sum(-1)
        M0rows += (A0[si] * dist0).sum(1)
    M0 = M0rows.max()
    del A0, As0, Asl, op0, oploc, E, H1
    A1r = sfft.fftn(O1, axes=(0, 1, 2, 3), overwrite_x=True, workers=1) / n2 ** 4
    del O1
    N1 = 0.0; M1 = 0.0
    for S in itertools.product(range(n2), repeat=4):
        blkS = np.abs(A1r[S])                                       # (a, b) entries A(a, b + 3S)
        Sv = np.array([si if si <= n2 // 2 else si - n2 for si in S], float)
        tgt = pos[None, :, :] + 3 * Sv[None, None, :]
        dvec = np.abs(tgt - pos[:, None, :]) % (3 * n2)
        dist = np.minimum(dvec, 3 * n2 - dvec).sum(-1)
        if S == (0, 0, 0, 0):
            rowsN = blkS.sum(1); rowsM = (blkS * dist).sum(1)
        else:
            rowsN = rowsN + blkS.sum(1); rowsM = rowsM + (blkS * dist).sum(1)
    N1, M1 = rowsN.max(), rowsM.max()
    gam0p, gam1p = 1.5873e-8, 1.29e-10
    print(f"D3: level 0 rows (exact range): N_0 = {N0:.4f}, first moment {M0:.4f} (c35: 25.4760, 41.0765); "
          f"level 1 rows (torus side 12, aliased): N_0 = {N1:.4f}, first moment {M1:.4f}")
    print(f"D3: first-moment rates m ~ (gamma/2)/moment: level 0 {gam0p/2/M0:.3e} (proven gamma_0), level 1 {gam1p/2/M1:.3e} "
          f"(proven gamma_1); ratio {(gam1p/M1)/(gam0p/M0):.3e}")
    for k in sorted(ok):
        print(k, "PASS" if ok[k] else "FAIL")
    print(f"Part D: {'PASS' if all(ok.values()) else 'FAIL'} (time {time.time()-t0:.0f} s, peak RSS {rss_mb():.0f} MB)")


if __name__ == "__main__":
    part = sys.argv[1]
    {"A": part_A, "B": part_B, "C": part_C, "D": part_D}[part]()
