#!/usr/bin/env python3
"""lane954 (FINISH row 954): GUIDE test of the two-slice Poincare ratio
    R_J(Phi) = Var_J(Phi) / E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ]
for gauge-invariant two-slice observables, SU(2) and compact U(1) Wilson, open time (no flux sectors).
Criteria are in library/gap-lsij-scale-opus.md Section 2, written before any run.
GUIDE only: a run can refute or guide, never prove.  Author: Claude Opus 5.5 (max), 2026-11-14.
Usage: python3 -I rj954.py --lib <path to liblgt954.dylib> --group su2 --L 4 --K 6 --beta 2.3 --nmeas 400
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import sys, time, json, argparse, ctypes, resource
import numpy as np

T0 = time.time()
RSS_CAP = 2.0e9


def rss():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        r *= 1024
    if r > RSS_CAP:
        raise SystemExit(f"peak RSS {r/1e9:.2f} GB above the 2 GB cap; stopping")
    return r


def log(*a):
    print(f"[{time.time()-T0:7.1f}s rss {rss()/1e6:5.0f}MB]", *a, flush=True)


# ------------------------------------------------------------------ quaternions, SU(2) convention
SGN = np.array([1., -1., -1., -1.])
E3D = np.array([0., 0., 0., -1.])          # e3^dagger: Re(W e3^dag) = sin(Theta) for U(1)-embedded W


def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + b0*a1 - (a2*b3 - a3*b2),
                     a0*b2 + b0*a2 - (a3*b1 - a1*b3),
                     a0*b3 + b0*a3 - (a1*b2 - a2*b1)], -1)


def qc(a):
    return a * SGN


def sh(f, o):
    """f(y + o) at y (spatial axes 0, 1, 2)."""
    return np.roll(f, (-o[0], -o[1], -o[2]), axis=(0, 1, 2))


def unsh(f, o):
    """value at y moves to y + o."""
    return np.roll(f, (o[0], o[1], o[2]), axis=(0, 1, 2))


def ev(d, n=1):
    o = [0, 0, 0]
    o[d] = n
    return tuple(o)


def add(*os_):
    return tuple(int(sum(o[i] for o in os_)) for i in range(3))


X_, W_ = 0, 1


# ------------------------------------------------------------------ loop shapes (base site y)
def plaq(s, i, j):
    return [(s, i, (0, 0, 0), 1), (s, j, ev(i), 1), (s, i, ev(j), 0), (s, j, (0, 0, 0), 0)]


def rect_long_i(s, i, j):
    return [(s, i, (0, 0, 0), 1), (s, i, ev(i), 1), (s, j, ev(i, 2), 1), (s, i, add(ev(i), ev(j)), 0),
            (s, i, ev(j), 0), (s, j, (0, 0, 0), 0)]


def sq2(s, i, j):
    return [(s, i, (0, 0, 0), 1), (s, i, ev(i), 1), (s, j, ev(i, 2), 1), (s, j, add(ev(i, 2), ev(j)), 1),
            (s, i, add(ev(i), ev(j, 2)), 0), (s, i, ev(j, 2), 0), (s, j, ev(j), 0), (s, j, (0, 0, 0), 0)]


def tplaq(i):
    return [(X_, i, (0, 0, 0), 1), (W_, i, (0, 0, 0), 0)]


def trect(i):
    return [(X_, i, (0, 0, 0), 1), (X_, i, ev(i), 1), (W_, i, ev(i), 0), (W_, i, (0, 0, 0), 0)]


PLANES = [(0, 1), (0, 2), (1, 2)]


def field_defs():
    """24 local fields, keyed by name -> list of loops (each a list of steps)."""
    F = {}
    for (i, j) in PLANES:
        p = frozenset((i, j))
        for s, nm in ((X_, "x"), (W_, "w")):
            F[("plaq", nm, p)] = [plaq(s, i, j)]
            F[("rect", nm, p)] = [rect_long_i(s, i, j), rect_long_i(s, j, i)]
            F[("sq2", nm, p)] = [sq2(s, i, j)]
    for i in range(3):
        F[("tpl", "xw", i)] = [tplaq(i)]
        F[("trect", "xw", i)] = [trect(i)]
    return F


def adapted_order(jr):
    """field keys in the order adapted to direction jr (cyclic relabelling is a lattice rotation)."""
    pl = [frozenset((jr, (jr+1) % 3)), frozenset((jr, (jr+2) % 3)), frozenset(((jr+1) % 3, (jr+2) % 3))]
    dr = [jr, (jr+1) % 3, (jr+2) % 3]
    keys = []
    for kind in ("plaq",):
        keys += [(kind, "x", p) for p in pl] + [(kind, "w", p) for p in pl]
    keys += [("tpl", "xw", i) for i in dr]
    for kind in ("rect", "sq2"):
        keys += [(kind, "x", p) for p in pl] + [(kind, "w", p) for p in pl]
    keys += [("trect", "xw", i) for i in dr]
    return keys


FIELDS = field_defs()


def eval_loop(links, steps, tail=None):
    """W(y) = product of the factors (times a constant tail), and per factor the Euclidean gradient of
    Re W(y) wrt that link variable, placed on the link's own site (unshifted by its offset)."""
    fac = []
    for (s, d, o, fw) in steps:
        f = sh(links[s][d], o)
        fac.append(f if fw else qc(f))
    if tail is not None:
        fac.append(np.broadcast_to(tail, fac[0].shape))
    n = len(fac)
    pre = [None]*(n+1)
    suf = [None]*(n+2)
    pre[1] = fac[0]
    for m in range(2, n+1):
        pre[m] = qmul(pre[m-1], fac[m-1])
    suf[n] = fac[n-1]
    for m in range(n-1, 0, -1):
        suf[m] = qmul(fac[m-1], suf[m+1])
    W = pre[n]
    out = []
    for m in range(1, len(steps)+1):
        if m == 1:
            rest = suf[2]
        elif m == n:
            rest = pre[n-1]
        else:
            rest = qmul(suf[m+1], pre[m-1])
        s, d, o, fw = steps[m-1]
        g = qc(rest) if fw else rest
        out.append((s, d, o, unsh(g, o)))
    return W, out


def strip_line(xi, wi, i):
    """strip loop (1/2) tr(P^x P^w^dag) with the FIXED base point y_i = 0 on each line (in SU(2) its value
    depends on the base point, so the own-site holonomy trick is not valid for it).  Returns the value per
    line (L, L) and the Euclidean gradients on the links x_i, w_i (arrays (L, L, L, 4))."""
    X = np.moveaxis(xi, i, 0)
    Wl = np.moveaxis(wi, i, 0)
    L = X.shape[0]
    one = np.zeros(X.shape[1:])
    one[..., 0] = 1.0

    def prefsuf(Z):
        A = [one]
        for n in range(1, L):
            A.append(qmul(A[-1], Z[n-1]))
        B = [None]*L
        B[L-1] = one
        for n in range(L-2, -1, -1):
            B[n] = qmul(Z[n+1], B[n+1])
        return A, B, qmul(A[L-1], Z[L-1])
    Ax, Bx, Qx = prefsuf(X)
    Aw, Bw, Qw = prefsuf(Wl)
    val = (Qx*Qw).sum(-1)
    gx = np.stack([qc(qmul(qmul(Bx[n], qc(Qw)), Ax[n])) for n in range(L)])
    gw = np.stack([qmul(qmul(qc(Aw[n]), Qx), qc(Bw[n])) for n in range(L)])
    return val, np.moveaxis(gx, 0, i), np.moveaxis(gw, 0, i)


class Meas:
    def __init__(self, L, group):
        self.L = L
        self.group = group
        y = np.indices((L, L, L))
        self.y = y
        self.kph = [np.exp(2j*np.pi*y[j]/L) for j in range(3)]          # e^{i k_min y_j}

    # ---------------------------------------------------------------- fields and their gradients
    def local(self, links):
        """for each field key and part ('c' = Re W, 's' = Re W e3^dag for U(1)): values F(y) and list of
        (s, d, o, gshift) gradient pieces (gshift indexed by the link site z; phase factor e^{-ik.o})."""
        parts = ("c", "s") if self.group == "u1" else ("c",)
        res = {}
        for key, loops in FIELDS.items():
            for part in parts:
                tail = E3D if part == "s" else None
                val = 0.0
                pieces = []
                for steps in loops:
                    W, gl = eval_loop(links, steps, tail)
                    val = val + W[..., 0]
                    pieces += gl
                res[(key, part)] = (val, pieces)
        return res

    def grad_k(self, pieces, kvec):
        """complex gradient array (2, 3, L, L, L, 4) of sum_y e^{ik.y} F(y); kvec integer 3-vector."""
        L = self.L
        G = np.zeros((2, 3, L, L, L, 4), complex if any(kvec) else float)
        for (s, d, o, g) in pieces:
            if any(kvec):
                G[s, d] += np.exp(-2j*np.pi*np.dot(kvec, o)/L)*g
            else:
                G[s, d] += g
        if any(kvec):
            ph = np.exp(2j*np.pi*(kvec[0]*self.y[0]+kvec[1]*self.y[1]+kvec[2]*self.y[2])/L)
            G *= ph[None, None, ..., None]
        return G

    def project(self, G, links):
        """tangent projection, G of shape (n, 2, 3, L, L, L, 4)."""
        for s in range(2):
            for d in range(3):
                u = links[s][d]
                G[:, s, d] -= (G[:, s, d]*u).sum(-1)[..., None]*u
        return G

    def winding(self, links):
        """per direction i: Q^x_i(y), Q^w_i(y) (holonomy starting at y) and the link gradients of Re Q."""
        L = self.L
        out = {}
        for i in range(3):
            for s in (X_, W_):
                u = links[s][i]
                Q = u.copy()
                for n in range(1, L):
                    Q = qmul(Q, sh(u, ev(i, n)))
                out[(s, i)] = Q
        return out

    # ---------------------------------------------------------------- one slice pair
    def measure(self, x, w):
        L = self.L
        links = {X_: x, W_: w}
        loc = self.local(links)
        win = self.winding(links)
        L2 = L*L
        R = {}
        if self.group == "su2":
            # ---- S0e: 24 local fields at k = 0 + 12 winding-even sums
            keys = adapted_order(0)
            vals, grads = [], []
            for kk in keys:
                v, pcs = loc[(kk, "c")]
                vals.append(v.sum())
                grads.append(self.grad_k(pcs, (0, 0, 0)))
            Mx, Mw, gMx, gMw = [], [], [], []
            for i in range(3):
                Qx, Qw = win[(X_, i)], win[(W_, i)]
                Px = Qx[..., 0]
                Pw = Qw[..., 0]
                gPx = qmul(qc(Qx), x[i])                       # grad of Re Q^x(y) wrt x_i(y)
                gPw = qmul(qc(Qw), w[i])
                st, g_st_x, g_st_w = strip_line(x[i], w[i], i)
                # line sums: every line counted L times when summing over all y; divide by L
                G = np.zeros((4, 2, 3, L, L, L, 4))
                G[0, X_, i] = g_st_x
                G[0, W_, i] = g_st_w
                G[1, X_, i] = Pw[..., None]*gPx                # grad of P^x P^w (per line)
                G[1, W_, i] = Px[..., None]*gPw
                G[2, X_, i] = 2*Px[..., None]*gPx
                G[3, W_, i] = 2*Pw[..., None]*gPw
                vals += [st.sum(), (Px*Pw).sum()/L, (Px**2).sum()/L, (Pw**2).sum()/L]
                grads += [G[0], G[1], G[2], G[3]]
                mx, mw = Px.sum()/(L*L2), Pw.sum()/(L*L2)
                gx = np.zeros((2, 3, L, L, L, 4))
                gw = np.zeros((2, 3, L, L, L, 4))
                gx[X_, i] = gPx/L2
                gw[W_, i] = gPw/L2
                Mx.append(mx)
                Mw.append(mw)
                gMx.append(gx)
                gMw.append(gw)
            Ga = self.project(np.array(grads), links)
            Xa = Ga.reshape(len(vals), -1)
            R["S0e"] = (np.array(vals), Xa @ Xa.T)
            if getattr(self, "debug", False):
                self.dbg = {"S0e": (np.array(vals), Xa.copy())}
            # ---- S0o: 8 odd polynomials in (M^x_i, M^w_i), averaged over i (3 copies)
            m2s, gs, m1s = 0, 0, 0
            for i in range(3):
                a, b, ga, gb = Mx[i], Mw[i], gMx[i], gMw[i]
                v = np.array([a, b, a**3, b**3, a*a*b, a*b*b, a**5, b**5])
                g = np.array([ga, gb, 3*a*a*ga, 3*b*b*gb, 2*a*b*ga + a*a*gb, b*b*ga + 2*a*b*gb, 5*a**4*ga, 5*b**4*gb])
                g = self.project(g, links).reshape(8, -1)
                if getattr(self, "debug", False) and i == 0:
                    self.dbg["S0o"] = (v.copy(), g.copy())
                m2s = m2s + np.outer(v, v)/3
                gs = gs + (g @ g.T)/3
            R["S0o"] = (None, m2s, gs)
            # ---- S1e: 24 local fields at k = k_min e_j, cos and sin parts, j-adapted labels (6 copies)
            m2s, gs = 0, 0
            for j in range(3):
                kv = [0, 0, 0]
                kv[j] = 1
                keys = adapted_order(j)
                vals, grads = [], []
                for kk in keys:
                    v, pcs = loc[(kk, "c")]
                    vals.append((v*self.kph[j]).sum())
                    grads.append(self.grad_k(pcs, kv))
                vals = np.array(vals)
                Gc = self.project(np.array(grads), links).reshape(len(keys), -1)
                if getattr(self, "debug", False) and j == 1:
                    self.dbg["S1e-re"] = (vals.real.copy(), Gc.real.copy())
                    self.dbg["S1e-im"] = (vals.imag.copy(), Gc.imag.copy())
                for part in (np.real, np.imag):
                    vv = part(vals)
                    XX = part(Gc)
                    m2s = m2s + np.outer(vv, vv)/6
                    gs = gs + (XX @ XX.T)/6
            R["S1e"] = (None, m2s, gs)
            # ---- S1o: winding line P_i at transverse momentum k_min e_j, (x, w); 12 copies of 2x2
            m2s, gs = 0, 0
            for i in range(3):
                Qx, Qw = win[(X_, i)], win[(W_, i)]
                Px, Pw = Qx[..., 0], Qw[..., 0]
                gPx = qmul(qc(Qx), x[i])
                gPw = qmul(qc(Qw), w[i])
                for j in range(3):
                    if j == i:
                        continue
                    ph = self.kph[j]
                    vals = np.array([(ph*Px).sum()/L, (ph*Pw).sum()/L])
                    G = np.zeros((2, 2, 3, L, L, L, 4), complex)
                    G[0, X_, i] = ph[..., None]*gPx
                    G[1, W_, i] = ph[..., None]*gPw
                    G = self.project(G, links).reshape(2, -1)
                    if getattr(self, "debug", False) and (i, j) == (2, 0):
                        self.dbg["S1o-re"] = (vals.real.copy(), G.real.copy())
                        self.dbg["S1o-im"] = (vals.imag.copy(), G.imag.copy())
                    for part in (np.real, np.imag):
                        vv = part(vals)
                        XX = part(G)
                        m2s = m2s + np.outer(vv, vv)/12
                        gs = gs + (XX @ XX.T)/12
            R["S1o"] = (None, m2s, gs)
            loc_stats = [loc[(("plaq", "x", frozenset((0, 1))), "c")][0].mean(),
                         loc[(("tpl", "xw", 0), "c")][0].mean(),
                         (loc[(("tpl", "xw", 0), "c")][0]**2).mean(),
                         np.mean([abs(m) for m in Mx]), np.mean([m*m for m in Mx]), np.mean([m**4 for m in Mx])]
        else:
            # ---- U(1): sectors U0c (cos fields k=0 + strip), U0s (sin fields k=0), U1c, U1s (k_min, 6 copies),
            #      U0w (charge-one winding sums, 3 copies)
            keys = adapted_order(0)
            for part, name in (("c", "U0c"), ("s", "U0s")):
                vals, grads = [], []
                for kk in keys:
                    v, pcs = loc[(kk, part)]
                    vals.append(v.sum())
                    grads.append(self.grad_k(pcs, (0, 0, 0)))
                if part == "c":
                    for i in range(3):
                        Qx, Qw = win[(X_, i)], win[(W_, i)]
                        st, gsx, gsw = strip_line(x[i], w[i], i)
                        G = np.zeros((2, 3, L, L, L, 4))
                        G[X_, i] = gsx
                        G[W_, i] = gsw
                        vals.append(st.sum())
                        grads.append(G)
                Ga = self.project(np.array(grads), links).reshape(len(vals), -1)
                R[name] = (np.array(vals), Ga @ Ga.T) if part == "c" else (None, np.outer(vals, vals), Ga @ Ga.T)
                if getattr(self, "debug", False):
                    self.dbg = getattr(self, "dbg", {})
                    self.dbg[name] = (np.array(vals), Ga.copy())
            for part, name in (("c", "U1c"), ("s", "U1s")):
                m2s, gs = 0, 0
                for j in range(3):
                    kv = [0, 0, 0]
                    kv[j] = 1
                    keys = adapted_order(j)
                    vals, grads = [], []
                    for kk in keys:
                        v, pcs = loc[(kk, part)]
                        vals.append((v*self.kph[j]).sum())
                        grads.append(self.grad_k(pcs, kv))
                    vals = np.array(vals)
                    Gc = self.project(np.array(grads), links).reshape(len(keys), -1)
                    if getattr(self, "debug", False) and j == 2:
                        self.dbg[name+"-re"] = (vals.real.copy(), Gc.real.copy())
                        self.dbg[name+"-im"] = (vals.imag.copy(), Gc.imag.copy())
                    for pp in (np.real, np.imag):
                        vv = pp(vals)
                        XX = pp(Gc)
                        m2s = m2s + np.outer(vv, vv)/6
                        gs = gs + (XX @ XX.T)/6
                R[name] = (None, m2s, gs)
            m2s, gs = 0, 0
            for i in range(3):
                Qx, Qw = win[(X_, i)], win[(W_, i)]
                vals = np.array([Qx[..., 0].sum(), (Qx*(-E3D)).sum(-1).sum(), Qw[..., 0].sum(), (Qw*(-E3D)).sum(-1).sum()])/L
                # (Qx*(-E3D)).sum(-1) = Q_3 = sin(Theta); gradients: Re Q -> qc(Q) u ; Re(Q e3^dag) -> e3 qc(Q) u
                e3 = np.array([0., 0., 0., 1.])
                G = np.zeros((4, 2, 3, L, L, L, 4))
                G[0, X_, i] = qmul(qc(Qx), x[i])
                G[1, X_, i] = qmul(qmul(np.broadcast_to(e3, Qx.shape), qc(Qx)), x[i])
                G[2, W_, i] = qmul(qc(Qw), w[i])
                G[3, W_, i] = qmul(qmul(np.broadcast_to(e3, Qw.shape), qc(Qw)), w[i])
                G = self.project(G, links).reshape(4, -1)
                if getattr(self, "debug", False) and i == 1:
                    self.dbg["U0w"] = (vals.copy(), G.copy())
                m2s = m2s + np.outer(vals, vals)/3
                gs = gs + (G @ G.T)/3
            R["U0w"] = (None, m2s, gs)
            loc_stats = [loc[(("plaq", "x", frozenset((0, 1))), "c")][0].mean(),
                         loc[(("tpl", "xw", 0), "c")][0].mean(),
                         (loc[(("tpl", "xw", 0), "c")][0]**2).mean(), 0.0, 0.0, 0.0]
        return R, np.array(loc_stats)


# ------------------------------------------------------------------ lattice driver
class Lattice:
    def __init__(self, lib, group, L, Nt, beta, seed):
        self.lib = lib
        self.group = group
        self.L, self.Nt, self.beta = L, Nt, beta
        V = L*L*L*Nt
        self.nf = np.zeros(V*4, np.int32)
        self.nb = np.zeros(V*4, np.int32)
        lib.build_nbr(L, Nt, self.nf.ctypes.data_as(ctypes.c_void_p), self.nb.ctypes.data_as(ctypes.c_void_p))
        self.st = np.zeros(4, np.uint64)
        lib.rng_seed(self.st.ctypes.data_as(ctypes.c_void_p), ctypes.c_uint64(seed))
        if group == "su2":
            self.U = np.zeros((Nt, L, L, L, 4, 4))
            self.U[..., 0] = 1.0
        else:
            self.A = np.zeros((Nt, L, L, L, 4))

    def sweep(self, n=1, nor=2):
        for _ in range(n):
            if self.group == "su2":
                self.lib.su2_sweep(self.U.ctypes.data_as(ctypes.c_void_p), self.nf.ctypes.data_as(ctypes.c_void_p),
                                   self.nb.ctypes.data_as(ctypes.c_void_p), self.L, self.Nt, ctypes.c_double(self.beta),
                                   nor, self.st.ctypes.data_as(ctypes.c_void_p))
            else:
                self.lib.u1_sweep(self.A.ctypes.data_as(ctypes.c_void_p), self.nf.ctypes.data_as(ctypes.c_void_p),
                                  self.nb.ctypes.data_as(ctypes.c_void_p), self.L, self.Nt, ctypes.c_double(self.beta),
                                  nor, self.st.ctypes.data_as(ctypes.c_void_p))

    def quat(self, t):
        """slice t as quaternion links, array axes (x0, x1, x2), shape (L, L, L, 4 mu, 4)."""
        if self.group == "su2":
            q = self.U[t]
        else:
            a = self.A[t]
            q = np.zeros(a.shape + (4,))
            q[..., 0] = np.cos(a)
            q[..., 3] = np.sin(a)
        return np.ascontiguousarray(q.transpose(2, 1, 0, 3, 4))

    def pair(self, t):
        """x = spatial links of slice t; w = slice t+1 transported by the temporal links of slice t."""
        a = self.quat(t)
        b = self.quat(t+1)
        U0 = a[..., 0, :]
        x = [a[..., d+1, :] for d in range(3)]
        w = [qmul(qmul(U0, b[..., d+1, :]), qc(sh(U0, ev(d)))) for d in range(3)]
        return x, w


def slice_series(lat, meas):
    """per slice t: SU(2): [sum of space-like plaquettes, M_0, M_1, M_2] (M_i = mean winding line);
    U(1): [sum cos plaquettes, B(k_min) for (j, plane containing j) x 6 (complex), M_0, M_1, M_2 (complex)]."""
    L = lat.L
    out = []
    for t in range(lat.Nt):
        q = lat.quat(t)
        x = [q[..., d+1, :] for d in range(3)]
        row = [0.0]
        Wp = {}
        for (i, j) in PLANES:
            W = qmul(qmul(x[i], sh(x[j], ev(i))), qmul(qc(sh(x[i], ev(j))), qc(x[j])))
            Wp[(i, j)] = W
            row[0] += W[..., 0].sum()
        if lat.group == "u1":
            for j in range(3):
                for (a, b) in PLANES:
                    if j in (a, b):
                        row.append((Wp[(a, b)][..., 3]*meas.kph[j]).sum())
        for i in range(3):
            Q = x[i].copy()
            for n in range(1, L):
                Q = qmul(Q, sh(x[i], ev(i, n)))
            row.append(Q[..., 0].sum()/L**3 + (1j*Q[..., 3].sum()/L**3 if lat.group == "u1" else 0))
        out.append(row)
    return np.array(out, complex if lat.group == "u1" else float)


def gap_analysis(ser, Nt, group, edge=2, tmax=6, nblk=20):
    """time correlators over the slab, both slices at distance >= edge from the ends; effective energies."""
    n = ser.shape[0]
    chans = {"plaq0": [0]}
    if group == "su2":
        chans["wind"] = [1, 2, 3]
    else:
        chans["Bkmin"] = list(range(1, 7))
        chans["wind"] = [7, 8, 9]

    def corr(sel):
        out = {}
        for nm, cols in chans.items():
            Z = ser[sel][:, :, cols]
            if nm == "plaq0":
                Z = Z - Z.mean(0, keepdims=True)
            cs = []
            for tau in range(tmax+1):
                ts = [t for t in range(edge, Nt-edge-tau)]
                v = np.mean([np.real(Z[:, t, :]*np.conj(Z[:, t+tau, :])).mean() for t in ts])
                cs.append(v)
            out[nm] = np.array(cs)
        return out
    full = corr(np.ones(n, bool))
    blocks = np.array_split(np.arange(n), nblk)
    jk = []
    for b in blocks:
        sel = np.ones(n, bool)
        sel[b] = False
        jk.append(corr(sel))
    res = {}
    for nm in chans:
        c = full[nm]
        with np.errstate(all="ignore"):
            e = np.log(c[:-1]/c[1:])
            ej = np.array([np.log(j[nm][:-1]/j[nm][1:]) for j in jk])
        nb = len(blocks)
        err = np.sqrt((nb-1)/nb*np.nansum((ej-np.nanmean(ej, 0))**2, 0))
        res[nm] = dict(C=c.tolist(), Eeff=e.tolist(), Eeff_err=err.tolist())
    return res


# ------------------------------------------------------------------ analysis
def top_gev(C, G, rel=1e-9):
    e, V = np.linalg.eigh(0.5*(G+G.T))
    keep = e > rel*e.max()
    B = V[:, keep]/np.sqrt(e[keep])
    M = B.T @ C @ B
    ew, ev_ = np.linalg.eigh(0.5*(M+M.T))
    vec = B @ ev_[:, -1]
    return ew[-1], vec


def sector_mats(data, sel):
    """data: dict sector -> (m1 array (n_cfg, n) or None, m2 (n_cfg, n, n), g (n_cfg, n, n))."""
    out = {}
    for name, (m1, m2, g) in data.items():
        M2 = m2[sel].mean(0)
        Gm = g[sel].mean(0)
        if m1 is not None:
            mu = m1[sel].mean(0)
            C = M2 - np.outer(mu, mu)
        else:
            C = M2
        out[name] = (C, Gm)
    return out


def analyse(data, nblk=20):
    n = next(iter(data.values()))[1].shape[0]
    full = sector_mats(data, np.ones(n, bool))
    res = {}
    blocks = np.array_split(np.arange(n), nblk)
    for name, (C, G) in full.items():
        top, vec = top_gev(C, G)
        diag = np.diag(C)/np.diag(G)
        jk_top, jk_diag = [], []
        for b in blocks:
            sel = np.ones(n, bool)
            sel[b] = False
            Cs, Gs = sector_mats({name: data[name]}, sel)[name]
            jk_top.append(top_gev(Cs, Gs)[0])
            jk_diag.append(np.diag(Cs)/np.diag(Gs))
        jk_top = np.array(jk_top)
        jk_diag = np.array(jk_diag)
        nb = len(blocks)
        err = np.sqrt((nb-1)/nb*((jk_top-jk_top.mean())**2).sum())
        derr = np.sqrt((nb-1)/nb*((jk_diag-jk_diag.mean(0))**2).sum(0))
        bc = nb*top-(nb-1)*jk_top.mean()
        res[name] = dict(top=float(top), err=float(err), top_bc=float(bc), diag=diag.tolist(), diag_err=derr.tolist(),
                         vec=(vec/np.abs(vec).max()).tolist())
    return res


def selftest(L=4, seed=1, eps=1e-5):
    """finite-difference check of the analytic tangent gradients of every k = 0 observable (S0e for SU(2);
    U0c and U0s for U(1)) on random links, along a random tangent field."""
    rng = np.random.default_rng(seed)
    for group in ("su2", "u1"):
        meas = Meas(L, group)
        meas.debug = True
        if group == "su2":
            x = [rng.normal(size=(L, L, L, 4)) for _ in range(3)]
            w = [rng.normal(size=(L, L, L, 4)) for _ in range(3)]
            x = [a/np.linalg.norm(a, axis=-1, keepdims=True) for a in x]
            w = [a/np.linalg.norm(a, axis=-1, keepdims=True) for a in w]
        else:
            def emb(th):
                q = np.zeros(th.shape + (4,))
                q[..., 0] = np.cos(th)
                q[..., 3] = np.sin(th)
                return q
            x = [emb(rng.uniform(-np.pi, np.pi, (L, L, L))) for _ in range(3)]
            w = [emb(rng.uniform(-np.pi, np.pi, (L, L, L))) for _ in range(3)]
        links = [x, w]
        z = []
        for sl in range(2):
            for d in range(3):
                u = links[sl][d]
                v = rng.normal(size=u.shape)
                if group == "u1":
                    v[..., 1:3] = 0.0
                v = v-(v*u).sum(-1, keepdims=True)*u
                z.append(v)
        Z = np.stack(z).reshape(2, 3, L, L, L, 4)

        def moved(e):
            out = [[None]*3, [None]*3]
            for sl in range(2):
                for d in range(3):
                    u, v = links[sl][d], Z[sl, d]
                    nv = np.linalg.norm(v, axis=-1, keepdims=True)
                    out[sl][d] = np.cos(e*nv)*u+np.sin(e*nv)*v/np.where(nv > 0, nv, 1)
            return out
        meas.measure(x, w)
        dbg = dict(meas.dbg)
        a1 = moved(eps)
        meas.measure(a1[0], a1[1])
        dp = dict(meas.dbg)
        a2 = moved(-eps)
        meas.measure(a2[0], a2[1])
        dm = dict(meas.dbg)
        for name, (v0, Xg) in dbg.items():
            fd = (dp[name][0]-dm[name][0])/(2*eps)
            an = Xg @ Z.reshape(-1)
            err = np.abs(fd-an).max()/max(1e-12, np.abs(an).max())
            print(f"selftest {group} {name}: n_obs {len(v0)}, max rel. error of directional derivative {err:.2e}",
                  "PASS" if err < 1e-5 else "FAIL", flush=True)


def main():
    if "--selftest" in sys.argv:
        selftest()
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", required=True)
    ap.add_argument("--group", choices=["su2", "u1"], default="su2")
    ap.add_argument("--L", type=int, default=4)
    ap.add_argument("--K", type=int, default=6)
    ap.add_argument("--m", type=int, default=1, help="2m+1 central pairs measured")
    ap.add_argument("--beta", type=float, default=2.3)
    ap.add_argument("--ntherm", type=int, default=200)
    ap.add_argument("--nsep", type=int, default=2)
    ap.add_argument("--nmeas", type=int, default=400)
    ap.add_argument("--nor", type=int, default=2)
    ap.add_argument("--seed", type=int, default=954)
    ap.add_argument("--out", default=None)
    ap.add_argument("--tmax", type=float, default=1e9, help="stop measuring after this many seconds")
    a = ap.parse_args()
    lib = ctypes.CDLL(a.lib)
    Nt = 2*a.K + 2 + 2*a.m
    lat = Lattice(lib, a.group, a.L, Nt, a.beta, a.seed)
    meas = Meas(a.L, a.group)
    log(f"group={a.group} L={a.L} K={a.K} m={a.m} Nt={Nt} beta={a.beta} ntherm={a.ntherm} nsep={a.nsep} nmeas={a.nmeas} nor={a.nor}")
    t1 = time.time()
    lat.sweep(a.ntherm, a.nor)
    log(f"thermalised, {(time.time()-t1)/max(a.ntherm,1)*1e3:.1f} ms per sweep")
    pairs = [a.K + j for j in range(2*a.m+1)]
    data = None
    series = []
    stats = []
    tm = 0.0
    tsw = 0.0
    nm = 0
    for r in range(a.nmeas):
        t1 = time.time()
        lat.sweep(a.nsep, a.nor)
        tsw += time.time()-t1
        t1 = time.time()
        acc = None
        st = 0
        for t in pairs:
            x, w = lat.pair(t)
            R, ls = meas.measure(x, w)
            st = st + ls/len(pairs)
            if acc is None:
                acc = {k: [None if v[0] is None else v[0]/len(pairs)] + [vv/len(pairs) for vv in v[1:]] for k, v in R.items()}
                for k, v in R.items():
                    if v[0] is not None:          # (vals, gram): store m1, m2, g
                        acc[k] = [v[0]/len(pairs), np.outer(v[0], v[0])/len(pairs), v[1]/len(pairs)]
            else:
                for k, v in R.items():
                    if v[0] is not None:
                        acc[k][0] = acc[k][0] + v[0]/len(pairs)
                        acc[k][1] = acc[k][1] + np.outer(v[0], v[0])/len(pairs)
                        acc[k][2] = acc[k][2] + v[1]/len(pairs)
                    else:
                        acc[k][1] = acc[k][1] + v[1]/len(pairs)
                        acc[k][2] = acc[k][2] + v[2]/len(pairs)
        tm += time.time()-t1
        if data is None:
            data = {k: [[] if v[0] is not None else None, [], []] for k, v in acc.items()}
        for k, v in acc.items():
            if v[0] is not None:
                data[k][0].append(v[0])
            data[k][1].append(v[1])
            data[k][2].append(v[2])
        stats.append(st)
        series.append(slice_series(lat, meas))
        nm += 1
        if (r+1) % max(1, a.nmeas//10) == 0:
            log(f"meas {r+1}/{a.nmeas}: sweep {tsw/nm*1e3:.0f} ms/meas, measure {tm/nm*1e3:.0f} ms/meas")
        if time.time()-T0 > a.tmax:
            log(f"time limit reached after {nm} measurements")
            break
    D = {k: (None if v[0] is None else np.array(v[0]), np.array(v[1]), np.array(v[2])) for k, v in data.items()}
    res = analyse(D)
    gaps = gap_analysis(np.array(series), Nt, a.group)
    stats = np.array(stats)
    ac = [np.corrcoef(D[k][1][:-1].reshape(nm-1, -1).sum(1), D[k][1][1:].reshape(nm-1, -1).sum(1))[0, 1] if nm > 3 else 0
          for k in D]
    out = dict(args=vars(a), nmeas=nm, Nt=Nt, stats_mean=stats.mean(0).tolist(), stats_err=(stats.std(0)/np.sqrt(nm)).tolist(),
               lag1_trace_m2=dict(zip(D.keys(), [float(c) for c in ac])), sectors=res, gaps=gaps,
               ms_per_sweep=tsw/nm/a.nsep*1e3, ms_per_meas=tm/nm*1e3, peak_rss_mb=rss()/1e6, wall_s=time.time()-T0)
    print(json.dumps({k: v for k, v in out.items() if k not in ("sectors", "gaps")}))
    for nm, g in gaps.items():
        print(f"  gap {nm:6s} Eeff(tau) " + " ".join(f"{e:.3f}+-{er:.3f}" for e, er in zip(g["Eeff"], g["Eeff_err"])))
    for name, r in res.items():
        print(f"  {name:4s} top {r['top']:.5f} +- {r['err']:.5f} (bias-corrected {r['top_bc']:.5f}); "
              f"max single {max(r['diag']):.5f}")
    if a.out:
        with open(a.out, "w") as f:
            json.dump(out, f)
    log("done")


if __name__ == "__main__":
    main()
