"""c27: identities and constants of Proposition PG (physical gap), criteria checks/c27_criteria.md (written first)."""
import itertools
import resource
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
from scipy.sparse.linalg import lsmr

T0 = time.time()
rng = np.random.default_rng(20261027)


def rss():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


def axial(a, b, order):
    out = []; z = list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


class Geo:
    def __init__(self, d, T, n):
        self.d, self.T, self.n = d, T, n
        eps = 1.0 / n; self.eps = eps; N = n * T; self.N = N; NS = N ** d; self.NS = NS; NE = d * NS; self.NE = NE
        hn = (n - 1) // 2; self.hn = hn
        X = np.indices((N,) * d).reshape(d, -1).T; self.X = X
        sid = lambda x: np.ravel_multi_index(tuple(np.mod(x[..., i], N) for i in range(d)), (N,) * d)
        self.sid = sid
        E = np.eye(d, dtype=np.int64)
        r, c, v = [], [], []
        for mu in range(d):
            r += [mu * NS + np.arange(NS)] * 2; c += [sid(X + E[mu]), sid(X)]
            v += [np.full(NS, 1 / eps), np.full(NS, -1 / eps)]
        self.Gr = sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(NE, NS))
        coarse = np.indices((T,) * d).reshape(d, -1).T; self.coarse = coarse; Nc = len(coarse); self.Nc = Nc
        offs = np.indices((n,) * d).reshape(d, -1).T
        # block mean M, straight average Q_str, face flux F
        mr, mc = [], []
        for Xi, Xc in enumerate(coarse):
            mr.append(np.full(len(offs), Xi)); mc.append(sid(n * Xc + offs))
        self.Mm = sp.csr_matrix((np.full(Nc * len(offs), n ** -d), (np.concatenate(mr), np.concatenate(mc))), shape=(Nc, NS))
        qr, qc, qv, fr, fc = [], [], [], [], []
        for mu in range(d):
            for Xi, Xc in enumerate(coarse):
                base = n * Xc + offs
                for j in range(n):
                    qr.append(np.full(len(offs), mu * Nc + Xi)); qc.append(mu * NS + sid(base + j * E[mu]))
                top = base[offs[:, mu] == n - 1]
                fr.append(np.full(len(top), mu * Nc + Xi)); fc.append(mu * NS + sid(top))
        self.Qs = sp.csr_matrix((np.full(sum(len(a) for a in qr), eps * n ** -d), (np.concatenate(qr), np.concatenate(qc))),
                                shape=(d * Nc, NE))
        self.Fm = sp.csr_matrix((np.full(sum(len(a) for a in fr), eps ** (d - 1)), (np.concatenate(fr), np.concatenate(fc))),
                                shape=(d * Nc, NE))
        # S4' slice functional h
        orders = list(itertools.permutations(range(d))); wQ = 1.0 / (len(orders) * n ** d)
        hr, hc, hv = [], [], []
        for Xi, Xc in enumerate(coarse):
            cX = [n * Xc[i] + hn for i in range(d)]
            for sig in orders:
                for off in itertools.product(range(-hn, hn + 1), repeat=d):
                    y = [cX[i] + off[i] for i in range(d)]
                    for (z, cc, s_) in axial(cX, y, sig):
                        hr.append(Xi); hc.append(cc * NS + int(sid(np.array(z)))); hv.append(s_ * eps * wQ)
        self.H = sp.csr_matrix((hv, (hr, hc)), shape=(Nc, NE))
        self.roots = np.array([int(sid(n * Xc + hn)) for Xc in coarse])
        # coarse gradient
        cs = lambda Y: np.ravel_multi_index(tuple(np.mod(Y[..., i], T) for i in range(d)), (T,) * d)
        r, c, v = [], [], []
        for mu in range(d):
            r += [mu * Nc + np.arange(Nc)] * 2; c += [cs(coarse + E[mu]), cs(coarse)]; v += [np.ones(Nc), -np.ones(Nc)]
        self.Gc = sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(d * Nc, Nc))
        self.blk = np.empty(NS, dtype=np.int64)
        for Xi, Xc in enumerate(coarse):
            self.blk[sid(n * Xc + offs)] = Xi

    def n2(self, A):
        return self.eps ** self.d * float(A @ A)

    def comp_diff(self, A, mu, nu):
        d, NS = self.d, self.NS; E = np.eye(d, dtype=np.int64)
        a = A[mu * NS:(mu + 1) * NS]
        return (a[self.sid(self.X + E[nu])] - a) / self.eps

    def grad2(self, A):
        return sum(self.eps ** self.d * float(np.sum(self.comp_diff(A, m, v) ** 2)) for m in range(self.d) for v in range(self.d))


def curl2(g, A):
    # ||dA||^2 = ||grad A||^2 - ||d*A||^2 on the flat torus, with d* = Gr^T in eps^d-weighted inner products
    dstar = g.Gr.T @ A
    return g.grad2(A) - g.eps ** g.d * float(dstar @ dstar)


def hodge(g, A):
    psi = lsmr(g.Gr, A, atol=1e-15, btol=1e-15, maxiter=100000)[0]
    psi -= psi.mean()
    return psi, A - g.Gr @ psi


def project_H0(g, A):
    H = g.H.toarray()
    return A - H.T @ np.linalg.solve(H @ H.T, H @ A)


ok = {k: True for k in ("E1", "E2", "E3", "E4", "E5", "E6")}
I1 = 0.0


def run(d, T, n, dense):
    global I1
    tt = time.time(); g = Geo(d, T, n)
    # E1, E2
    A = rng.normal(size=g.NE)
    psi, Ac = hodge(g, A)
    Fc = g.Fm @ Ac
    e1 = float(np.max(np.abs(g.Gc.T @ Fc)) / np.max(np.abs(Fc)))
    ok["E1"] &= e1 <= 1e-10
    tests = {"random": A}
    k1 = np.zeros(g.NE)
    for mu in range(d):
        k1[mu * g.NS:(mu + 1) * g.NS] = np.cos(2 * np.pi * g.X[:, (mu + 1) % d] / g.N + mu) + np.sin(2 * np.pi * g.X[:, mu] / g.N)
    tests["smooth"] = k1
    tests["alternating"] = np.tile(((-1.0) ** g.X.sum(1)), d)
    e2 = 0.0
    for nm, B in tests.items():
        lhs = float(np.sum((g.Qs @ B - g.Fm @ B) ** 2))
        rhs = 4 * sum(g.eps ** d * float(np.sum(g.comp_diff(B, m, m) ** 2)) for m in range(d))
        e2 = max(e2, lhs / rhs)
    ok["E2"] &= e2 <= 1.0
    # E6
    C3 = C3_of(n)
    e6 = 0.0
    for nm, B in (("random", A), ("smooth", k1)):
        hB = g.H @ B
        for Xi in range(g.Nc):
            inb = g.blk == Xi
            nb = sum(g.eps ** d * float(np.sum(B[m * g.NS:(m + 1) * g.NS][inb] ** 2)) for m in range(d))
            gb = 0.0
            E = np.eye(d, dtype=np.int64)
            for m in range(d):
                for v in range(d):
                    nbr = g.sid(g.X + E[v]); both = inb & (g.blk[nbr] == Xi)
                    gb += g.eps ** d * float(np.sum(g.comp_diff(B, m, v)[both] ** 2))
            lhs = g.eps ** 2 * hB[Xi] ** 2
            rhs = 8 * g.eps ** 2 * nb + 8 * C3 * g.eps * gb
            e6 = max(e6, lhs / rhs)
    if d == 4:
        ok["E6"] &= e6 <= 1.0
    msg = f"d={d} T={T} n={n}: E1 {e1:.1e}  E2 max ratio {e2:.3f}  E6 max ratio {e6:.4f}"
    # E3 (dense)
    if dense:
        Cn = np.zeros((2 * g.Nc, g.NS))
        for Xi in range(g.Nc):
            Cn[Xi, g.roots[Xi]] = 1.0; Cn[g.Nc + Xi, g.blk == Xi] = 1.0
        Nul = sla.null_space(Cn)
        GN = (g.Gr @ Nul) * g.eps ** (d / 2)
        e3 = 0.0; e3b = 0.0
        lam = rng.normal(size=g.NS); lam[g.roots] = 0.0
        mprime = np.array([lam[g.blk == Xi].sum() for Xi in range(g.Nc)]) * n ** -d
        lam[g.roots] = mprime / (1 - n ** -d)
        cases = [project_H0(g, rng.normal(size=g.NE)), project_H0(g, k1), g.Gr @ lam,
                 project_H0(g, k1) + 0.3 * (g.Gr @ lam)]
        for A3 in cases:
            assert np.max(np.abs(g.H @ A3)) < 1e-9 * max(1.0, np.max(np.abs(A3)))
            x = A3 * g.eps ** (d / 2)
            c, *_ = np.linalg.lstsq(GN, -x, rcond=None)
            inf_orb = float(np.sum((x + GN @ c) ** 2))
            psi3, Ac3 = hodge(g, A3)
            r = psi3[g.roots]; m = g.Mm @ psi3
            e3b = max(e3b, float(np.max(np.abs((r - m) - g.H @ Ac3))) / max(np.max(np.abs(r - m)), 1e-300))
            phip, *_ = np.linalg.lstsq(Cn, np.concatenate([r, m * n ** d]), rcond=None)
            y = (g.Gr @ phip) * g.eps ** (d / 2)
            c2, *_ = np.linalg.lstsq(GN, -y, rcond=None)
            Erm = float(np.sum((y + GN @ c2) ** 2))
            pred = g.n2(Ac3) + Erm
            e3 = max(e3, abs(inf_orb - pred) / inf_orb)
            den = curl2(g, A3) + float(np.sum((g.Qs @ A3) ** 2))
            I1 = max(I1, inf_orb / den)
        ok["E3"] &= e3 <= 1e-8 and e3b <= 1e-10
        msg += f"  E3 rel {e3:.1e}, r-m=h(A_c) {e3b:.1e}"
    print(msg + f"  ({time.time() - tt:.0f} s, RSS {rss():.0f} MB)", flush=True)


_C3 = {}


def C3_of(n, all_sites=True):
    if n in _C3:
        return _C3[n]
    k = np.arange(n); s = np.arange(n)
    c = np.where(k == 0, 1.0 / n, 2.0 / n)
    a = c[:, None] * np.cos(np.pi * k[:, None] * (s[None, :] + 0.5) / n) ** 2          # (k, s)
    lam1 = 4 * np.sin(np.pi * k / (2 * n)) ** 2
    lam = lam1[:, None, None] + lam1[None, :, None] + lam1[None, None, :]
    lam[0, 0, 0] = np.inf
    inv = 1.0 / lam
    # G(s) = sum_k prod_i a(k_i, s_i) / lam_k, all s by tensor contraction
    G = np.einsum("abc,ai,bj,ck->ijk", inv, a, a, a, optimize=True)
    _C3[n] = float(G.max())
    return _C3[n]


# E4
c3s = [C3_of(n) for n in range(2, 25)]
ok["E4"] &= max(c3s) <= 14
print("E4 C_3(n), n = 2..24: " + " ".join(f"{x:.4f}" for x in c3s))
# E5 constants
worst_b = 0.0; worst_cb = 0.0; worst_g = 0.0
for n in range(3, 43, 2):
    s = np.sin(np.pi * np.arange(1, n + 1) / (n + 1))
    bn = (n / s.sum()) ** 4
    se = np.concatenate([[0.0], s, [0.0]])
    one_d_e = float(np.sum(np.diff(se) ** 2)); one_d_s = float(np.sum(s ** 2))
    Cb = (1.0 / n) ** 2 * 4 * bn ** 2 * one_d_e * one_d_s ** 3     # eps^{d-2} sum over bonds, d = 4
    worst_b = max(worst_b, bn / (np.pi / 2) ** 4); worst_cb = max(worst_cb, Cb / 163)
    if n <= 9:
        # gamma = (1_c - n^-4 beta)/(1 - n^-4 beta(c)) on the (n+2)^4 box, explicit
        prof = bn * np.einsum("i,j,k,l->ijkl", se, se, se, se)
        h = (n + 1) // 2
        gam = -n ** -4.0 * prof; gam[h, h, h, h] += 1.0; gam /= (1 - n ** -4.0 * prof[h, h, h, h])
        e = sum(float(np.sum(np.diff(gam, axis=ax) ** 2)) for ax in range(4)) * (1.0 / n) ** 2
        worst_g = max(worst_g, e / (20 * (1.0 / n) ** 2))
ok["E5"] &= worst_b <= 1 and worst_cb <= 1 and worst_g <= 1
print(f"E5 b_n/(pi/2)^4 max {worst_b:.4f}; C_beta/163 max {worst_cb:.4f}; ||d gamma||^2/(20 eps^2) max {worst_g:.4f}")
wI = 0.0; wD = 0.0
for (T, n) in ((2, 3), (3, 3), (2, 5)):
    g = Geo(4, T, n); d = 4
    for _ in range(3):
        m = rng.normal(size=g.Nc)
        mc = m.reshape((T,) * d)
        xi = (g.X - g.hn) / n; Y = np.floor(xi).astype(np.int64); t = xi - Y
        phi = np.zeros(g.NS)
        for a in itertools.product((0, 1), repeat=d):
            w = np.ones(g.NS)
            for i in range(d):
                w *= t[:, i] if a[i] else (1 - t[:, i])
            idx = tuple(np.mod(Y[:, i] + a[i], T) for i in range(d))
            phi += w * mc[idx]
        dcm = float(np.sum((g.Gc @ m) ** 2))
        dphi = g.eps ** d * float(np.sum((g.Gr @ phi) ** 2))
        delta = m - g.Mm @ phi
        wI = max(wI, dphi / (22 * dcm)); wD = max(wD, float(np.sum(delta ** 2)) / (216 * dcm))
ok["E5"] &= wI <= 1 and wD <= 1
print(f"E5 ||d phi~||^2/(22||d_c m||^2) max {wI:.4f}; sum delta^2/(216||d_c m||^2) max {wD:.4f}", flush=True)

for (d, T, n, dense) in ((4, 2, 3, True), (4, 2, 5, False), (2, 4, 3, True), (2, 4, 5, True), (2, 4, 7, True), (3, 3, 3, True)):
    run(d, T, n, dense)
print(f"I1 max inf_orbit/(||dA||^2 + ||QA||^2) over the tested A in H_0: {I1:.4f} (proven constant 3.5e6)")
for k, v in ok.items():
    print(f"{k}: {'PASS' if v else 'FAIL'}")
print(f"c27: time {time.time() - T0:.0f} s, peak RSS {rss():.0f} MB")
