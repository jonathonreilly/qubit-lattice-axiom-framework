#!/usr/bin/env python3
"""lane946 (FINISH row 946): GUIDE test of (FC)/(GC) for the SU(2) vacuum slice chain.

Estimates R(f) = E_nu |grad P f|^2 / E_nu |grad f|^2 by a frozen-slice Monte Carlo, using row 941's
(A3): grad_l P f(x) = beta Cov_{pi_x}(Proj_l w_l, f(w)).  Open time {0..2K}, middle slice K frozen,
forward and backward halves independent given x (E2), transported neighbour slices w, w' (E3).
Criteria are in library/gap-fctest-opus.md Step 2, written before any run.
GUIDE only: a run can refute or guide, never prove.  Author: Claude Opus 5.5 (max), 2026-11-14.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
           "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import sys, json, time, argparse, resource
import numpy as np
import scipy.sparse as ssp

RSS_CAP = 2.0e9
T_START = time.time()


def rss():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        r *= 1024
    if r > RSS_CAP:
        raise SystemExit(f"peak RSS {r/1e9:.2f} GB above the 2 GB cap; stopping")
    return r


def log(*a):
    print(f"[{time.time()-T_START:7.1f}s rss {rss()/1e6:6.0f}MB]", *a, flush=True)


# ---------------------------------------------------------------- quaternions (SU(2) = unit quaternions)
SGN = np.array([1., -1., -1., -1.])


def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    out = np.empty(np.broadcast_shapes(a.shape, b.shape))
    out[..., 0] = a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3
    out[..., 1] = a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2
    out[..., 2] = a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1
    out[..., 3] = a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0
    return out


def qconj(a):
    return a * SGN


def cmult(neg):
    """multiplier [1, s, s, s], s = -1 where neg (conjugation as a product)."""
    s = np.where(neg, -1.0, 1.0)
    m = np.ones(np.shape(neg) + (4,))
    m[..., 1:] = s[..., None]
    return m


# ---------------------------------------------------------------- spatial graphs
def spatial_box(L):
    ns = L ** 3

    def site(x, y, z):
        return (x % L) + L * ((y % L) + L * (z % L))
    coords = np.array([(x, y, z) for z in range(L) for y in range(L) for x in range(L)])
    links = []
    for s in range(ns):
        for mu in range(3):
            c = list(coords[s]); c[mu] += 1
            links.append((s, site(*c), mu))
    lk = lambda s, mu: 3 * s + mu
    plaqs, pinfo = [], []
    for s in range(ns):
        for o, (mu, nu) in enumerate([(0, 1), (0, 2), (1, 2)]):
            cm = list(coords[s]); cm[mu] += 1
            cn = list(coords[s]); cn[nu] += 1
            plaqs.append([(lk(s, mu), 1), (lk(site(*cm), nu), 1), (lk(site(*cn), mu), -1), (lk(s, nu), -1)])
            pinfo.append((s, o, mu, nu))
    lines, linfo = [], []
    for mu in range(3):
        for s in range(ns):
            if coords[s][mu] != 0:
                continue
            path = []
            for n in range(L):
                c = list(coords[s]); c[mu] = n
                path.append((lk(site(*c), mu), 1))
            lines.append(path); linfo.append((s, mu))
    return dict(kind="box", L=L, ns=ns, coords=coords, links=links, plaqs=plaqs, pinfo=pinfo,
                lines=lines, linfo=linfo, site=site)


def spatial_plaq():
    links = [(0, 1, 0), (1, 2, 1), (2, 3, 0), (3, 0, 1)]
    plaqs = [[(0, 1), (1, 1), (2, 1), (3, 1)]]
    return dict(kind="plaq", ns=4, links=links, plaqs=plaqs, pinfo=[(0, 0, 0, 1)], lines=[], linfo=[])


def spatial_cube():
    site = lambda x, y, z: x + 2 * y + 4 * z
    links, lidx = [], {}
    for z in (0, 1):
        for y in (0, 1):
            for x in (0, 1):
                c = (x, y, z)
                for mu in range(3):
                    if c[mu] == 0:
                        c2 = list(c); c2[mu] = 1
                        lidx[(site(*c), mu)] = len(links)
                        links.append((site(*c), site(*c2), mu))
    plaqs, pinfo = [], []
    for o, (mu, nu) in enumerate([(0, 1), (0, 2), (1, 2)]):
        rho = 3 - mu - nu
        for h in (0, 1):
            c = [0, 0, 0]; c[rho] = h
            s = site(*c)
            cm = list(c); cm[mu] = 1
            cn = list(c); cn[nu] = 1
            plaqs.append([(lidx[(s, mu)], 1), (lidx[(site(*cm), nu)], 1), (lidx[(site(*cn), mu)], -1),
                          (lidx[(s, nu)], -1)])
            pinfo.append((s, o, mu, nu))
    return dict(kind="cube", ns=8, links=links, plaqs=plaqs, pinfo=pinfo, lines=[], linfo=[])


# ---------------------------------------------------------------- 4D lattice, open time {0..2K}
class Lat4:
    def __init__(self, sp, K):
        self.sp, self.K = sp, K
        T = 2 * K + 1
        self.T = T
        nsl, ns = len(sp["links"]), sp["ns"]
        self.nsl, self.ns = nsl, ns
        self.nl = T * nsl + (T - 1) * ns
        self.la = np.array([l[0] for l in sp["links"]])
        self.lb = np.array([l[1] for l in sp["links"]])
        plaq = []
        for t in range(T):
            for P in sp["plaqs"]:
                plaq.append([(self.spi(t, j), sg) for (j, sg) in P])
        for t in range(T - 1):
            for j, (a, b, mu) in enumerate(sp["links"]):
                plaq.append([(self.spi(t, j), 1), (self.tmi(t, b), 1), (self.spi(t + 1, j), -1),
                             (self.tmi(t, a), -1)])
        self.plaq = plaq
        self.pidx = np.array([[l for (l, s) in P] for P in plaq])
        self.psg = np.array([[s for (l, s) in P] for P in plaq])
        inc = [[] for _ in range(self.nl)]
        for pi_, P in enumerate(plaq):
            ls = [l for (l, s) in P]
            assert len(set(ls)) == 4
            for k in range(4):
                inc[P[k][0]].append((pi_, k))
        mi = max(len(x) for x in inc)
        idx = np.zeros((self.nl, mi, 3), int)
        flg = np.zeros((self.nl, mi, 3), bool)
        sc = np.zeros((self.nl, mi), bool)
        val = np.zeros((self.nl, mi), bool)
        for l in range(self.nl):
            for j, (pi_, k) in enumerate(inc[l]):
                P = plaq[pi_]
                for m in range(3):
                    ll, sg = P[(k + 1 + m) % 4]
                    idx[l, j, m] = ll
                    flg[l, j, m] = sg < 0
                sc[l, j] = P[k][1] < 0
                val[l, j] = True
        self.idx, self.flg, self.sc, self.val = idx, flg, sc, val
        color = -np.ones(self.nl, int)
        for l in range(self.nl):
            used = set()
            for (pi_, k) in inc[l]:
                for (ll, s) in plaq[pi_]:
                    if ll != l and color[ll] >= 0:
                        used.add(color[ll])
            c = 0
            while c in used:
                c += 1
            color[l] = c
        self.color = color
        frozen = np.zeros(self.nl, bool)
        frozen[self.spi(K, 0):self.spi(K, 0) + nsl] = True
        self.frozen = frozen
        self.cls_all = [np.flatnonzero(color == c) for c in range(color.max() + 1)]
        self.cls_frz = [c[~frozen[c]] for c in self.cls_all]
        self.cls_frz = [c for c in self.cls_frz if c.size]
        self.tab_all = [self.table(c) for c in self.cls_all]
        self.tab_frz = [self.table(c) for c in self.cls_frz]

    def spi(self, t, j):
        return t * self.nsl + j

    def tmi(self, t, s):
        return self.T * self.nsl + t * self.ns + s

    def table(self, cls):
        idx = self.idx[cls]
        return dict(cls=cls, idx=idx, mult=cmult(self.flg[cls]), smult=cmult(self.sc[cls]),
                    val=self.val[cls].astype(float), sg=np.where(self.flg[cls], -1.0, 1.0),
                    sk=np.where(self.sc[cls], -1.0, 1.0), nv=self.val[cls].sum(1).astype(float))


# ---------------------------------------------------------------- SU(2) updates
def staples(U, tb):
    idx, mult, smult, val = tb["idx"], tb["mult"], tb["smult"], tb["val"]
    A = np.zeros((U.shape[0], idx.shape[0], 4))
    for j in range(idx.shape[1]):
        q1 = U[:, idx[:, j, 0]] * mult[:, j, 0]
        q2 = U[:, idx[:, j, 1]] * mult[:, j, 1]
        q3 = U[:, idx[:, j, 2]] * mult[:, j, 2]
        S = qmul(qmul(q1, q2), q3) * smult[:, j]
        A += S * val[:, j, None]
    return A


def sample_x(alpha, rng):
    """unit quaternions X with density prop. to exp(alpha X_0) w.r.t. Haar."""
    shp = alpha.shape
    a = alpha.ravel()
    x0 = np.empty_like(a)
    todo = np.arange(a.size)
    while todo.size:
        aa = a[todo]
        big = aa >= 1.0
        acc = np.zeros(todo.size, bool)
        v = np.empty(todo.size)
        if big.any():
            ab = aa[big]; nb = ab.size
            r1 = 1.0 - rng.random(nb); r2 = rng.random(nb); r3 = 1.0 - rng.random(nb); r4 = rng.random(nb)
            lam2 = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / (2 * ab)
            ib = np.flatnonzero(big)
            acc[ib] = r4 * r4 <= 1.0 - lam2
            v[ib] = 1.0 - 2.0 * lam2
        if (~big).any():
            asm = aa[~big]; nsm = asm.size
            g = rng.standard_normal((nsm, 4)); g /= np.linalg.norm(g, axis=1, keepdims=True)
            isml = np.flatnonzero(~big)
            acc[isml] = rng.random(nsm) <= np.exp(asm * (g[:, 0] - 1.0))
            v[isml] = g[:, 0]
        x0[todo[acc]] = v[acc]
        todo = todo[~acc]
    x0 = x0.reshape(shp)
    d = rng.standard_normal(shp + (3,))
    d /= np.linalg.norm(d, axis=-1, keepdims=True)
    r = np.sqrt(np.maximum(0.0, 1.0 - x0 * x0))
    return np.concatenate([x0[..., None], r[..., None] * d], axis=-1)


def hb_su2(U, tb, beta, rng):
    A = staples(U, tb)
    k = np.maximum(np.sqrt((A * A).sum(-1)), 1e-300)
    V = A / k[..., None]
    X = sample_x(beta * k, rng)
    U[:, tb["cls"]] = qmul(X, qconj(V))


def or_su2(U, tb):
    A = staples(U, tb)
    k = np.maximum(np.sqrt((A * A).sum(-1)), 1e-300)
    Vb = qconj(A / k[..., None])
    U[:, tb["cls"]] = qmul(qmul(Vb, qconj(U[:, tb["cls"]])), Vb)


def sweep_su2(U, tabs, beta, rng, nor=2):
    for tb in tabs:
        hb_su2(U, tb, beta, rng)
    for _ in range(nor):
        for tb in tabs:
            or_su2(U, tb)
    for tb in tabs:  # renormalise only updated links: the frozen slice x stays bit-exact
        c = tb["cls"]
        U[:, c] /= np.linalg.norm(U[:, c], axis=-1, keepdims=True)


# ---------------------------------------------------------------- non-compact U(1) (free photon)
def hb_u1(A, tb, beta, rng):
    r = (A[:, tb["idx"]] * tb["sg"]).sum(-1)
    tot = (r * tb["sk"] * tb["val"]).sum(-1)
    nv = tb["nv"]
    A[:, tb["cls"]] = -tot / nv + rng.standard_normal(tot.shape) / np.sqrt(beta * nv)


def sweep_u1(A, tabs, beta, rng):
    for tb in tabs:
        hb_u1(A, tb, beta, rng)


# ---------------------------------------------------------------- slices and loops
def slices_su2(lat, U):
    K, nsl = lat.K, lat.nsl
    x = U[:, K * nsl:(K + 1) * nsl]
    up = U[:, (K + 1) * nsl:(K + 2) * nsl]
    dn = U[:, (K - 1) * nsl:K * nsl]
    w = qmul(qmul(U[:, lat.tmi(K, lat.la)], up), qconj(U[:, lat.tmi(K, lat.lb)]))
    wp = qmul(qmul(qconj(U[:, lat.tmi(K - 1, lat.la)]), dn), U[:, lat.tmi(K - 1, lat.lb)])
    return x, w, wp


def slices_u1(lat, A):
    K, nsl = lat.K, lat.nsl
    x = A[:, K * nsl:(K + 1) * nsl]
    w = A[:, lat.tmi(K, lat.la)] + A[:, (K + 1) * nsl:(K + 2) * nsl] - A[:, lat.tmi(K, lat.lb)]
    wp = -A[:, lat.tmi(K - 1, lat.la)] + A[:, (K - 1) * nsl:K * nsl] + A[:, lat.tmi(K - 1, lat.lb)]
    return x, w, wp


def loop_prod(w, lidx, lmul):
    q = w[:, lidx] * lmul
    P = q[:, :, 0]
    for k in range(1, lidx.shape[1]):
        P = qmul(P, q[:, :, k])
    return P


def loop_grads(w, lidx, lneg, lmul):
    """tangent gradients of Re(loop) w.r.t. each of its links: (B, nloops, len, 4)."""
    q = w[:, lidx] * lmul
    n = lidx.shape[1]
    pre = [None] * n
    suf = [None] * n
    one = np.zeros(q.shape[:2] + (4,)); one[..., 0] = 1.0
    pre[0] = one
    for k in range(1, n):
        pre[k] = qmul(pre[k - 1], q[:, :, k - 1])
    suf[n - 1] = one
    for k in range(n - 2, -1, -1):
        suf[k] = qmul(q[:, :, k + 1], suf[k + 1])
    G = np.empty(q.shape)
    for k in range(n):
        Rk = qmul(suf[k], pre[k])
        g = np.where(lneg[None, :, k, None], Rk, qconj(Rk))
        wl = w[:, lidx[:, k]]
        G[:, :, k] = g - (g * wl).sum(-1, keepdims=True) * wl
    return G


def tau_int(series):
    """Sokal windowed integrated autocorrelation time; series (nchains, n)."""
    x = series - series.mean(1, keepdims=True)
    n = x.shape[1]
    c0 = (x * x).mean()
    if c0 <= 0:
        return 0.5
    tau = 0.5
    for t in range(1, n // 2):
        rho = (x[:, :-t] * x[:, t:]).mean() / c0
        tau += rho
        if t >= 6 * tau:
            break
    return float(tau)


def jack_ratio(num, den):
    """num, den: (B, ...) per independent chain sums -> ratio of totals and jackknife error."""
    B = num.shape[0]
    Nt, Dt = num.sum(0), den.sum(0)
    R = Nt / Dt
    Rj = np.array([(Nt - num[b]) / (Dt - den[b]) for b in range(B)])
    err = np.sqrt((B - 1) / B * ((Rj - Rj.mean(0)) ** 2).sum(0))
    return R, err


# ---------------------------------------------------------------- observables (SU(2) slices)
class ObsSU2:
    """base observables F(w) and output observables W F, with closed-form |grad f|^2 on x."""

    def __init__(self, sp, orient=None, ldir=None):
        self.sp = sp
        plaqs, pinfo = sp["plaqs"], sp["pinfo"]
        self.allp_idx = np.array([[l for l, s in P] for P in plaqs])
        self.allp_neg = np.array([[s < 0 for l, s in P] for P in plaqs])
        psel = np.array([i for i, pi in enumerate(pinfo) if orient is None or pi[1] in orient])
        self.psel = psel
        self.pidx, self.pneg = self.allp_idx[psel], self.allp_neg[psel]
        self.pmul = cmult(self.pneg)
        N1 = len(psel)
        lsel = np.array([i for i, li in enumerate(sp["linfo"]) if ldir is None or li[1] in ldir], int)
        self.lsel = lsel
        N2 = len(lsel)
        if N2:
            self.lidx = np.array([[l for l, s in sp["lines"][i]] for i in lsel])
            self.lneg = np.zeros(self.lidx.shape, bool)
            self.lmul = cmult(self.lneg)
        self.cube = sp["kind"] == "cube"
        blocks = [("c", N1), ("t3", N1), ("t10", N1), ("c3", N1)]
        if N2:
            blocks.append(("line", N2))
        if self.cube:
            blocks += [("mono3", 1), ("mono10", 1)]
        off, self.boff = 0, {}
        for name, n in blocks:
            self.boff[name] = (off, n); off += n
        self.NF = off
        rows, cols, vals, types = [], [], [], []
        nrow = 0

        def add_type(name, combos):
            nonlocal nrow
            r0 = nrow
            for cmb in combos:
                for (col, v) in cmb:
                    rows.append(nrow); cols.append(col); vals.append(v)
                nrow += 1
            types.append((name, r0, nrow))
        for name, n in blocks:
            o = self.boff[name][0]
            add_type(name, [[(o + i, 1.0)] for i in range(n)])
        if sp["kind"] == "box":
            L, site, coords = sp["L"], sp["site"], sp["coords"]
            gsel = {int(p): i for i, p in enumerate(psel)}
            oc = self.boff["c"][0]
            sq, self.sq_members = [], []
            for i, p in enumerate(psel):
                s, o, mu, nu = pinfo[p]
                c0 = coords[s]
                def P_at(dm, dn):
                    c = list(c0); c[mu] += dm; c[nu] += dn
                    return gsel[3 * site(*c) + o]
                m = [P_at(0, 0), P_at(1, 0), P_at(0, 1), P_at(1, 1)]
                self.sq_members.append(m)
                sq.append([(oc + j, 0.25) for j in m])
            add_type("sq2", sq)
            self.sq_members = np.array(self.sq_members)
            zm = []
            self.zm_groups = []
            for o in sorted(set(pinfo[p][1] for p in psel)):
                g = [i for i, p in enumerate(psel) if pinfo[p][1] == o]
                self.zm_groups.append(np.array(g))
                zm.append([(oc + j, 1.0) for j in g])
            add_type("zm", zm)
            if N2:
                ol = self.boff["line"][0]
                lmap = {(int(sp["linfo"][i][0]), int(sp["linfo"][i][1])): k for k, i in enumerate(lsel)}
                pat, self.pat_members, xs, self.xs_groups = [], [], [], []
                for k, i in enumerate(lsel):
                    s, mu = sp["linfo"][i]
                    nu, rho = [d for d in range(3) if d != mu]
                    mem = []
                    for dn, dr in ((0, 0), (1, 0), (0, 1), (1, 1)):
                        c = list(coords[s]); c[nu] += dn; c[rho] += dr
                        mem.append(lmap[(site(*c), mu)])
                    self.pat_members.append(mem)
                    pat.append([(ol + j, 0.25) for j in mem])
                add_type("patch", pat)
                self.pat_members = np.array(self.pat_members)
                for mu in sorted(set(sp["linfo"][i][1] for i in lsel)):
                    g = [k for k, i in enumerate(lsel) if sp["linfo"][i][1] == mu]
                    self.xs_groups.append(np.array(g))
                    xs.append([(ol + j, 1.0 / len(g)) for j in g])
                add_type("xsec", xs)
        self.W = ssp.csr_matrix((vals, (rows, cols)), shape=(nrow, self.NF))
        self.types = types

    def base(self, w):
        c = loop_prod(w, self.pidx, self.pmul)[..., 0]
        parts = [c, np.tanh(3 * c), np.tanh(10 * c), c ** 3]
        if len(self.lsel):
            parts.append(loop_prod(w, self.lidx, self.lmul)[..., 0])
        if self.cube:
            parts += [np.prod(np.tanh(3 * c), axis=1, keepdims=True),
                      np.prod(np.tanh(10 * c), axis=1, keepdims=True)]
        return np.concatenate(parts, axis=1)

    def den(self, x):
        """|grad f|^2 at the slice x for every output row; dict type -> (B, nrows)."""
        B = x.shape[0]
        c = loop_prod(x, self.pidx, self.pmul)[..., 0]
        g2 = 4.0 * (1.0 - c * c)
        out = {"c": g2, "t3": (3 / np.cosh(3 * c) ** 2) ** 2 * g2, "t10": (10 / np.cosh(10 * c) ** 2) ** 2 * g2,
               "c3": (3 * c * c) ** 2 * g2}
        need_G = self.sp["kind"] == "box" or self.cube
        if need_G:
            G = loop_grads(x, self.pidx, self.pneg, self.pmul)
        if self.sp["kind"] == "box":
            m = self.sq_members
            d = g2[:, m].sum(-1)
            pairs = ((0, 1, 1, 3), (0, 2, 2, 0), (1, 2, 3, 0), (2, 1, 3, 3))
            for (i, ki, j, kj) in pairs:
                d = d + 2.0 * (G[:, m[:, i], ki] * G[:, m[:, j], kj]).sum(-1)
            out["sq2"] = d / 16.0
            zz = []
            for g in self.zm_groups:
                acc = np.zeros((B, len(self.sp["links"]), 4))
                np.add.at(acc, (slice(None), self.pidx[g].ravel()), G[:, g].reshape(B, -1, 4))
                zz.append((acc * acc).sum((1, 2)))
            out["zm"] = np.stack(zz, 1)
            if len(self.lsel):
                L = self.sp["L"]
                f = loop_prod(x, self.lidx, self.lmul)[..., 0]
                gl = L * (1.0 - f * f)
                out["line"] = gl
                out["patch"] = gl[:, self.pat_members].sum(-1) / 16.0
                out["xsec"] = np.stack([gl[:, g].sum(-1) / len(g) ** 2 for g in self.xs_groups], 1)
        if self.cube:
            for kap in (3, 10):
                h = np.tanh(kap * c); hp = kap / np.cosh(kap * c) ** 2
                acc = np.zeros((B, len(self.sp["links"]), 4))
                for p in range(c.shape[1]):
                    wgt = hp[:, p] * np.prod(np.delete(h, p, axis=1), axis=1)
                    np.add.at(acc, (slice(None), self.pidx[p]), wgt[:, None, None] * G[:, p])
                out["mono%d" % kap] = (acc * acc).sum((1, 2))[:, None]
        return out


class Acc:
    def __init__(self, B, na, nf, nb=50):
        self.Sa = np.zeros((B, na)); self.Sf = np.zeros((B, nf)); self.Saf = np.zeros((B, na, nf))
        self.n, self.nb, self.ab, self.fb = 0, nb, [], []

    def add(self, a, f):
        self.ab.append(a); self.fb.append(f)
        if len(self.ab) >= self.nb:
            self.flush()

    def flush(self):
        if not self.ab:
            return
        A = np.stack(self.ab, 1); F = np.stack(self.fb, 1)
        self.Sa += A.sum(1); self.Sf += F.sum(1); self.Saf += np.matmul(A.transpose(0, 2, 1), F)
        self.n += A.shape[1]; self.ab, self.fb = [], []

    def cov(self):
        self.flush()
        n = self.n
        return self.Saf / n - (self.Sa / n)[:, :, None] * (self.Sf / n)[:, None, :]


def score_rows(W, CF, CB, beta):
    """S_row = beta^2 sum_(l,comp) (W C^F)_row . (W C^B)_row, per chain b."""
    out = []
    for b in range(CF.shape[0]):
        XF = W @ CF[b].T
        XB = W @ CB[b].T
        out.append(beta * beta * (XF * XB).sum(1))
    return np.array(out)


def make_geom(args):
    if args.geom == "box":
        return spatial_box(args.L)
    if args.geom == "plaq":
        return spatial_plaq()
    if args.geom == "cube":
        return spatial_cube()
    raise ValueError(args.geom)


def run_su2(args):
    sp = make_geom(args)
    lat = Lat4(sp, args.K)
    orient = None if args.orient == "all" else [int(c) for c in args.orient]
    ldir = None if args.orient == "all" else [int(c) for c in args.orient]
    ob = ObsSU2(sp, orient, ldir)
    B, beta, n, m = args.B, args.beta, args.n, args.m
    rng = np.random.default_rng(args.seed)
    log(f"su2 geom={args.geom} L={getattr(args,'L',None)} K={args.K} beta={beta} B={B} m={m} nsep={args.nsep} "
        f"n={n} nor={args.nor} links={lat.nl} colours={len(lat.cls_all)} NF={ob.NF} rows={ob.W.shape[0]}")
    U = np.zeros((B, lat.nl, 4)); U[..., 0] = 1.0
    for i in range(args.ntherm):
        sweep_su2(U, lat.tab_all, beta, rng, args.nor)
    log("thermalised; plaquette mean", float(loop_prod(U, lat.pidx, cmult(lat.psg < 0))[..., 0].mean()))
    nt = len(ob.types)
    num = np.zeros((B, m, nt)); den = np.zeros((B, m, nt))
    ser_c, ser_l, ser_a, ser_t10 = [], [], [], []
    na = lat.nsl * 4
    for r in range(m):
        for i in range(args.nsep):
            sweep_su2(U, lat.tab_all, beta, rng, args.nor)
        Ui = U.copy()
        x, _, _ = slices_su2(lat, Ui)
        dd = ob.den(x)
        aF, aB = Acc(B, na, ob.NF), Acc(B, na, ob.NF)
        sc, sl, sa, st = [], [], [], []
        for i in range(n):
            sweep_su2(Ui, lat.tab_frz, beta, rng, args.nor)
            _, w, wp = slices_su2(lat, Ui)
            a = w - (w * x).sum(-1, keepdims=True) * x
            ap = wp - (wp * x).sum(-1, keepdims=True) * x
            F, Fp = ob.base(w), ob.base(wp)
            aF.add(a.reshape(B, -1), F); aB.add(ap.reshape(B, -1), Fp)
            sc.append(F[:, 0]); sa.append(a[:, ob.pidx[0, 0]]); st.append(F[:, ob.boff["t10"][0]])
            if len(ob.lsel):
                sl.append(F[:, ob.boff["line"][0]])
        assert np.abs(Ui[:, lat.frozen] - U[:, lat.frozen]).max() == 0.0
        S = score_rows(ob.W, aF.cov(), aB.cov(), beta)
        for t, (name, r0, r1) in enumerate(ob.types):
            num[:, r, t] = S[:, r0:r1].mean(1)
            den[:, r, t] = dd[name].mean(1)
        ser_c.append(np.array(sc).T); ser_a.append(np.array(sa).transpose(1, 0, 2)); ser_t10.append(np.array(st).T)
        if sl:
            ser_l.append(np.array(sl).T)
        Rr = num[:, :r + 1].sum((0, 1)) / den[:, :r + 1].sum((0, 1))
        log(f"round {r+1}/{m}: " + " ".join(f"{nm}={Rr[t]:.4g}" for t, (nm, _, _) in enumerate(ob.types)))
    return finish(args, ob.types, num, den, ser_c, ser_a, ser_t10, ser_l)


def finish(args, types, num, den, ser_c, ser_a, ser_t10, ser_l, exact=None):
    R, err = jack_ratio(num.sum(1), den.sum(1))
    res = {"args": vars(args), "R": {}, "time_s": time.time() - T_START}
    sc = np.concatenate(ser_c, 0)
    sa = np.concatenate(ser_a, 0)
    tau = {"c_p0": tau_int(sc)}
    if ser_t10:
        tau["t10_p0"] = tau_int(np.concatenate(ser_t10, 0))
    if ser_l:
        tau["line0"] = tau_int(np.concatenate(ser_l, 0))
    if sa.ndim == 3:
        tau["a_l0_x_c_p0"] = max(tau_int(sa[:, :, k] * sc) for k in range(4))
    else:
        tau["a_l0_x_c_p0"] = tau_int(sa * sc)
    res["tau_inner"] = tau
    for t, (name, r0, r1) in enumerate(types):
        y = num[:, :, t]
        y1 = ((y[:, 1:] - y.mean(1, keepdims=True)) * (y[:, :-1] - y.mean(1, keepdims=True))).mean()
        y0 = ((y - y.mean(1, keepdims=True)) ** 2).mean()
        ent = {"R": float(R[t]), "err": float(err[t]), "num": float(num[:, :, t].mean()),
               "den": float(den[:, :, t].mean()), "outer_lag1": float(y1 / y0) if y0 > 0 else None}
        if exact is not None and name in exact:
            ent["exact"] = exact[name]
        res["R"][name] = ent
    os.makedirs(args.outdir, exist_ok=True)
    np.savez(os.path.join(args.outdir, args.tag + ".npz"), num=num, den=den,
             types=np.array([t[0] for t in types]))
    with open(os.path.join(args.outdir, args.tag + ".json"), "w") as fh:
        json.dump(res, fh, indent=1)
    log("RESULT " + args.tag)
    for name, e in res["R"].items():
        ex = f" exact={e['exact']:.5g}" if "exact" in e else ""
        log(f"  {name:7s} R={e['R']:.5g} +- {e['err']:.2g}  (num {e['num']:.4g}, den {e['den']:.4g}, "
            f"outer lag1 {e['outer_lag1']}){ex}")
    log("  tau_inner", tau)
    return res


# ---------------------------------------------------------------- free photon (calibration C1)
def photon_exact(sp):
    nsl, Np = len(sp["links"]), len(sp["plaqs"])
    D = np.zeros((Np, nsl))
    for p, P in enumerate(sp["plaqs"]):
        for (j, sg) in P:
            D[p, j] += sg
    ev, V = np.linalg.eigh(D.T @ D)
    ev = np.maximum(ev, 0.0)
    om = np.arccosh(1.0 + ev / 2.0)
    M = (V * np.exp(-om)) @ V.T
    return D, M


def run_photon(args):
    sp = spatial_box(args.L)
    lat = Lat4(sp, args.K)
    L = args.L
    D, M = photon_exact(sp)
    psel = np.array([i for i, pi in enumerate(sp["pinfo"]) if pi[1] == 0])
    Dsel = D[psel]
    N1 = len(psel)
    coords = sp["coords"]
    rows, types, exact, cvecs = [], [], {}, []
    for i in range(N1):
        g = np.zeros(N1); g[i] = 1.0; rows.append(g)
    types.append(("flux", 0, N1))
    for q in (1, 2):
        k = 2 * np.pi * q / L
        g = np.array([np.cos(k * coords[sp["pinfo"][p][0]][0]) for p in psel])
        r0 = len(rows); rows.append(g); types.append(("mode%d" % q, r0, r0 + 1))
    Wd = np.array(rows)
    C = Wd @ Dsel
    den_rows = (C * C).sum(1)
    MC = C @ M
    Rex = (MC * MC).sum(1) / den_rows
    for name, r0, r1 in types:
        exact[name] = float(Rex[r0:r1].mean())
    for q in (1, 2):
        k = 2 * np.pi * q / L
        om = np.arccosh(1 + 2 * np.sin(k / 2) ** 2)
        exact["mode%d_closed_form" % q] = float(np.exp(-2 * om))
    log("photon exact:", exact)
    W = ssp.csr_matrix(Wd)
    B, beta, n, m = args.B, args.beta, args.n, args.m
    rng = np.random.default_rng(args.seed)
    A = np.zeros((B, lat.nl))
    for i in range(args.ntherm):
        sweep_u1(A, lat.tab_all, beta, rng)
    nt = len(types)
    num = np.zeros((B, m, nt)); den = np.zeros((B, m, nt))
    ser_c, ser_a = [], []
    for r in range(m):
        for i in range(args.nsep):
            sweep_u1(A, lat.tab_all, beta, rng)
        Ai = A.copy()
        x, _, _ = slices_u1(lat, Ai)
        aF, aB = Acc(B, lat.nsl, N1), Acc(B, lat.nsl, N1)
        sc, sa = [], []
        for i in range(n):
            sweep_u1(Ai, lat.tab_frz, beta, rng)
            _, w, wp = slices_u1(lat, Ai)
            F, Fp = w @ Dsel.T, wp @ Dsel.T
            aF.add(w - x, F); aB.add(wp - x, Fp)
            sc.append(F[:, 0]); sa.append((w - x)[:, sp["plaqs"][psel[0]][0][0]])
        assert np.abs(Ai[:, lat.frozen] - A[:, lat.frozen]).max() == 0.0
        S = score_rows(W, aF.cov(), aB.cov(), beta)
        for t, (name, r0, r1) in enumerate(types):
            num[:, r, t] = S[:, r0:r1].mean(1)
            den[:, r, t] = den_rows[r0:r1].mean()
        ser_c.append(np.array(sc).T); ser_a.append(np.array(sa).T)
        Rr = num[:, :r + 1].sum((0, 1)) / den[:, :r + 1].sum((0, 1))
        log(f"round {r+1}/{m}: " + " ".join(f"{nm}={Rr[t]:.4g}" for t, (nm, _, _) in enumerate(types)))
    return finish(args, types, num, den, ser_c, ser_a, [], [], exact)


# ---------------------------------------------------------------- one-plaquette chain, exact (calibration C2)
def plaq_exact(beta, nchar=40, nq=800, M=24):
    from scipy.special import iv
    from scipy.linalg import eigh
    xg, wg = np.polynomial.legendre.leggauss(nq)
    th = (xg + 1) * np.pi / 2; wt = wg * np.pi / 2
    meas = (2 / np.pi) * np.sin(th) ** 2 * wt
    nn = np.arange(1, nchar + 1)
    s, co = np.sin(th), np.cos(th)
    chi = np.sin(np.outer(nn, th)) / s
    dchi = (nn[:, None] * np.cos(np.outer(nn, th)) * s - np.sin(np.outer(nn, th)) * co) / s ** 2
    ck = ((2 / beta) * iv(nn, beta)) ** 4
    E = np.exp(beta * co / 2)
    G = (chi * E * meas) @ chi.T
    Tm = G @ (ck[:, None] * G.T)
    ev, vec = np.linalg.eigh(Tm)
    lam0, lam1 = ev[-1], ev[-2]
    Om = vec[:, -1] @ chi
    if Om.mean() < 0:
        Om = -Om
    nu = Om ** 2 * meas; nu /= nu.sum()
    wv = chi @ (E * Om * meas)
    Dn, dDn = (ck * wv) @ chi, (ck * wv) @ dchi

    def dP(f):
        u = chi @ (E * Om * f * meas)
        N, dN = (ck * u) @ chi, (ck * u) @ dchi
        return (dN * Dn - N * dDn) / Dn ** 2

    def R(f, df):
        return float((nu * dP(f) ** 2).sum() / (nu * df ** 2).sum())
    out = {"beta": beta, "r1": float(lam1 / lam0), "r1sq": float((lam1 / lam0) ** 2),
           "R_c": R(co, -s), "R_t3": R(np.tanh(3 * co), -3 * s / np.cosh(3 * co) ** 2),
           "R_t10": R(np.tanh(10 * co), -10 * s / np.cosh(10 * co) ** 2), "R_c3": R(co ** 3, -3 * co ** 2 * s)}
    dPs = [dP(chi[mm]) for mm in range(1, M)]
    Am = np.array([[(nu * a * b).sum() for b in dPs] for a in dPs])
    Bm = np.array([[(nu * dchi[i] * dchi[j]).sum() for j in range(1, M)] for i in range(1, M)])
    out["theta_GC"] = float(eigh(Am, Bm, eigvals_only=True)[-1])
    out["plaq_mean_nu"] = float((nu * co).sum())
    return out


# ---------------------------------------------------------------- self-tests of the code pieces
def selftest():
    rng = np.random.default_rng(7)
    a, b, c = (rng.standard_normal((5, 4)) for _ in range(3))
    assert np.allclose(qmul(qmul(a, b), c), qmul(a, qmul(b, c)))
    u = a / np.linalg.norm(a, axis=1, keepdims=True)
    assert np.allclose(qmul(u, qconj(u)), [1, 0, 0, 0])
    assert np.allclose(np.linalg.norm(qmul(u, b), axis=1), np.linalg.norm(b, axis=1))
    log("quaternion algebra ok")
    # staples: action change = Re((U' - U) A) summed over one colour class
    for sp in (spatial_box(3), spatial_plaq(), spatial_cube()):
        lat = Lat4(sp, 2)
        U = rng.standard_normal((2, lat.nl, 4)); U /= np.linalg.norm(U, axis=-1, keepdims=True)
        pm = cmult(lat.psg < 0)
        S0 = loop_prod(U, lat.pidx, pm)[..., 0].sum(1)
        for tb in lat.tab_all[:3]:
            A = staples(U, tb)
            U2 = U.copy()
            Un = rng.standard_normal((2, tb["cls"].size, 4)); Un /= np.linalg.norm(Un, axis=-1, keepdims=True)
            U2[:, tb["cls"]] = Un
            S1 = loop_prod(U2, lat.pidx, pm)[..., 0].sum(1)
            pred = ((Un - U[:, tb["cls"]]) * qconj(A)).sum((-1, -2))
            assert np.allclose(S1 - S0, pred), (sp["kind"], S1 - S0, pred)
        # colour classes are independent sets
        for cl in lat.cls_all:
            s = set(cl.tolist())
            for P in lat.pidx:
                assert sum(int(l) in s for l in P) <= 1
        log(f"staples and colouring ok on {sp['kind']} (links {lat.nl}, colours {len(lat.cls_all)})")
    # u1 staples: conditional mean minimises the local action
    sp = spatial_box(3); lat = Lat4(sp, 2)
    Ar = rng.standard_normal((1, lat.nl))
    tb = lat.tab_all[0]
    r = (Ar[:, tb["idx"]] * tb["sg"]).sum(-1)
    mu = -(r * tb["sk"] * tb["val"]).sum(-1) / tb["nv"]

    def u1act(Av):
        fl = (Av[:, lat.pidx] * lat.psg).sum(-1)
        return (fl * fl).sum()
    A1 = Ar.copy(); A1[:, tb["cls"]] = mu
    for eps in (1e-3, -1e-3):
        A2 = A1.copy(); A2[:, tb["cls"]] += eps
        assert u1act(A2) > u1act(A1)
    log("u1 conditional mean ok")
    # transported slices (E3): <x_l, w_l> and <x_l, w'_l> are the timelike plaquettes at K and K-1
    for sp in (spatial_box(3), spatial_plaq(), spatial_cube()):
        lat = Lat4(sp, 2)
        U = rng.standard_normal((2, lat.nl, 4)); U /= np.linalg.norm(U, axis=-1, keepdims=True)
        x, w, wp = slices_su2(lat, U)
        nsp = len(sp["plaqs"]) * lat.T
        pm = cmult(lat.psg < 0)
        up = loop_prod(U, lat.pidx[nsp + lat.K * lat.nsl: nsp + (lat.K + 1) * lat.nsl],
                       pm[nsp + lat.K * lat.nsl: nsp + (lat.K + 1) * lat.nsl])[..., 0]
        dn = loop_prod(U, lat.pidx[nsp + (lat.K - 1) * lat.nsl: nsp + lat.K * lat.nsl],
                       pm[nsp + (lat.K - 1) * lat.nsl: nsp + lat.K * lat.nsl])[..., 0]
        assert np.allclose((x * w).sum(-1), up) and np.allclose((x * wp).sum(-1), dn)
        # gauge invariance of w under a random gauge transformation at times != K
        g = rng.standard_normal((2, lat.T, lat.ns, 4)); g /= np.linalg.norm(g, axis=-1, keepdims=True)
        g[:, lat.K] = np.array([1., 0, 0, 0])
        U2 = U.copy()
        for t in range(lat.T):
            sl = slice(t * lat.nsl, (t + 1) * lat.nsl)
            U2[:, sl] = qmul(qmul(g[:, t, lat.la], U[:, sl]), qconj(g[:, t, lat.lb]))
        for t in range(lat.T - 1):
            sl = slice(lat.tmi(t, 0), lat.tmi(t, 0) + lat.ns)
            U2[:, sl] = qmul(qmul(g[:, t], U[:, sl]), qconj(g[:, t + 1]))
        x2, w2, wp2 = slices_su2(lat, U2)
        assert np.allclose(x2, x) and np.allclose(w2, w) and np.allclose(wp2, wp)
    log("transported slices ok (timelike plaquettes; invariant under gauge maps off slice K)")
    # loop gradients by finite differences (right multiplication by exp(eps tau))
    sp = spatial_box(3)
    ob = ObsSU2(sp)
    w = rng.standard_normal((1, len(sp["links"]), 4)); w /= np.linalg.norm(w, axis=-1, keepdims=True)
    G = loop_grads(w, ob.pidx, ob.pneg, ob.pmul)
    c0 = loop_prod(w, ob.pidx, ob.pmul)[..., 0]
    eps = 1e-6
    for p in (0, 5, 17):
        for k in range(4):
            l = ob.pidx[p, k]
            for tau in ([0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]):
                tq = np.array(tau, float)
                w2 = w.copy(); w2[0, l] = qmul(w[0, l], np.cos(eps) * np.array([1., 0, 0, 0]) + np.sin(eps) * tq)
                fd = (loop_prod(w2, ob.pidx, ob.pmul)[0, p, 0] - c0[0, p]) / eps
                an = (G[0, p, k] * qmul(w[0, l], tq)).sum()
                assert abs(fd - an) < 1e-5, (p, k, fd, an)
            assert abs((G[0, p, k] ** 2).sum() - (1 - c0[0, p] ** 2)) < 1e-10
    log("loop gradients ok (finite differences, |grad_l Re W|^2 = 1 - Re W^2)")
    # dense check of den() for sq2 and zm against an explicit sum of per-link gradients
    d = ob.den(w)
    Gfull = np.zeros((len(ob.psel), len(sp["links"]), 4))
    for p in range(len(ob.psel)):
        for k in range(4):
            Gfull[p, ob.pidx[p, k]] += G[0, p, k]
    for i in (0, 7, 30):
        g = Gfull[ob.sq_members[i]].sum(0) / 4
        assert abs((g * g).sum() - d["sq2"][0, i]) < 1e-10
    for gi, grp in enumerate(ob.zm_groups):
        g = Gfull[grp].sum(0)
        assert abs((g * g).sum() - d["zm"][0, gi]) < 1e-9
    log("den() sq2 and zm agree with explicit gradient sums")
    # heat-bath sampler: E X0 = I_2(alpha)/I_1(alpha)
    from scipy.special import iv
    for al in (0.3, 2.0, 7.0):
        X = sample_x(np.full(200000, al), rng)
        e = X[:, 0].mean(); ex = iv(2, al) / iv(1, al)
        assert abs(e - ex) < 4 * X[:, 0].std() / np.sqrt(2e5), (al, e, ex)
        assert np.allclose(np.linalg.norm(X, axis=1), 1)
    log("sampler E X0 = I2/I1 ok")
    log("SELFTEST PASSED")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["selftest", "exact-plaq", "photon", "su2"])
    ap.add_argument("--geom", default="box")
    ap.add_argument("--L", type=int, default=4)
    ap.add_argument("--K", type=int, default=6)
    ap.add_argument("--beta", type=float, default=2.3)
    ap.add_argument("--B", type=int, default=16)
    ap.add_argument("--m", type=int, default=8)
    ap.add_argument("--nsep", type=int, default=10)
    ap.add_argument("--n", type=int, default=300)
    ap.add_argument("--ntherm", type=int, default=200)
    ap.add_argument("--nor", type=int, default=2)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--orient", default="all")
    ap.add_argument("--tag", default="run")
    ap.add_argument("--outdir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))
    args = ap.parse_args()
    if args.cmd == "selftest":
        selftest()
    elif args.cmd == "exact-plaq":
        print(json.dumps(plaq_exact(args.beta), indent=1))
    elif args.cmd == "photon":
        run_photon(args)
    else:
        run_su2(args)


if __name__ == "__main__":
    main()
