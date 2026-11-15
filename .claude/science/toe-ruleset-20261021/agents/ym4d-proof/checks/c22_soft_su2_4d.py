"""c22: SU(2), d = 4 one-step soft S4' minimiser (criteria: checks/c22_criteria.md, written before this script).

Fine torus 9^4, L = 3, coarse 3^4. Unit quaternions. E(U) = sum_p (1 - Re U_p) + kappa sum_c (|Mbar_c| - <V_c, Mbar_c>).
Usage: python3 c22_soft_su2_4d.py [smoke]
"""
import itertools
import resource
import sys
import time

import numpy as np

T0 = time.time()
NF, L, NC = 9, 3, 3
D = 4
NS = NF ** D
NL = D * NS          # fine links; index NL = identity dummy
KAPPA = 1.0
RNG = np.random.default_rng(20261027)


# ------------------------------------------------------------------ quaternions
def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
                     a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
                     a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
                     a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0], axis=-1)


def qconj(a):
    return a * np.array([1.0, -1.0, -1.0, -1.0])


def qexp(v):
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    s = np.where(n > 1e-300, np.sin(n) / np.where(n > 1e-300, n, 1.0), 1.0)
    return np.concatenate([np.cos(n), s * v], axis=-1)


def qlog(q):
    """half-angle log vector, |a| in [0, pi]."""
    v = q[..., 1:]
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    ang = np.arctan2(n, q[..., :1])
    return np.where(n > 1e-300, ang / np.where(n > 1e-300, n, 1.0), 1.0) * v


def Ad(q, xi):
    z = np.concatenate([np.zeros(xi.shape[:-1] + (1,)), xi], axis=-1)
    return qmul(qmul(q, z), qconj(q))[..., 1:]


# ------------------------------------------------------------------ geometry
def sidx(x):
    x = [c % NF for c in x]
    return ((x[0] * NF + x[1]) * NF + x[2]) * NF + x[3]


def lidx(x, mu):
    return mu * NS + sidx(x)


def path(a, b, order):
    out = []
    z = list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((lidx(z, c), 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1
                out.append((lidx(w, c), -1)); z[c] -= 1
    return out


def rev(p):
    return [(l, -s) for (l, s) in reversed(p)]


ORDERS = list(itertools.permutations(range(D)))
COARSE = list(itertools.product(range(NC), repeat=D))
CLINKS = [(X, mu) for mu in range(D) for X in COARSE]      # coarse link id = mu*81 + Xindex
CID = {c: i for i, c in enumerate(CLINKS)}
NCL = len(CLINKS)
NPER = len(ORDERS) * L ** D
MAXLEN = 11


def root(X):
    return tuple(L * X[i] + 1 for i in range(D))


def build_contours():
    lk = np.full((NCL * NPER, MAXLEN), NL, dtype=np.int64)
    sg = np.ones((NCL * NPER, MAXLEN), dtype=np.int8)
    st = np.zeros((NCL * NPER, MAXLEN), dtype=bool)      # straight-leg positions
    k = 0
    for (X, mu) in CLINKS:
        cX = root(X)
        cY = list(cX); cY[mu] += L
        for sig in ORDERS:
            for off in itertools.product((-1, 0, 1), repeat=D):
                y = [cX[i] + off[i] for i in range(D)]
                yL = list(y); yL[mu] += L
                p1 = path(cX, y, sig)
                s = [(lidx([y[i] + (j if i == mu else 0) for i in range(D)], mu), 1) for j in range(L)]
                p2 = rev(path(cY, yL, sig))
                seq = p1 + s + p2
                for m, (l_, s_) in enumerate(seq):
                    lk[k, m] = l_; sg[k, m] = s_
                for m in range(len(p1), len(p1) + L):
                    st[k, m] = True
                k += 1
    return lk, sg, st


def build_plaquettes():
    n = NS * 6
    lk = np.zeros((n, 4), dtype=np.int64); sg = np.ones((n, 4), dtype=np.int8)
    base = []; planes = []
    k = 0
    for x in itertools.product(range(NF), repeat=D):
        for (mu, nu) in itertools.combinations(range(D), 2):
            xm = list(x); xm[mu] += 1
            xn = list(x); xn[nu] += 1
            lk[k] = [lidx(x, mu), lidx(xm, nu), lidx(xn, mu), lidx(x, nu)]
            sg[k] = [1, 1, -1, -1]
            base.append(x); planes.append((mu, nu)); k += 1
    return lk, sg, base, planes


# ------------------------------------------------------------------ loop products and gradients
def factors(U, lk, sg):
    Ue = np.concatenate([U, np.array([[1.0, 0, 0, 0]])], axis=0)
    F = Ue[lk]
    neg = sg < 0
    F[neg] = qconj(F[neg])
    return F


def products(F):
    n = F.shape[1]
    P = np.empty((F.shape[0], n + 1, 4))
    P[:, 0] = [1.0, 0, 0, 0]
    for m in range(n):
        P[:, m + 1] = qmul(P[:, m], F[:, m])
    return P


def grad_from(F, P, G, lk, sg, mask=None):
    """Fine Lie gradient of sum_loops <G_loop, T_loop>; G: (nloops, 4)."""
    n = F.shape[1]
    g = np.zeros((NL + 1, 3))
    S = np.zeros((F.shape[0], 4)); S[:, 0] = 1.0           # suffix after position m
    for m in range(n - 1, -1, -1):
        Sfrom = qmul(F[:, m], S)
        plus = qmul(qmul(qconj(P[:, m]), G), qconj(Sfrom))[:, 1:]
        minus = -qmul(qmul(qconj(P[:, m + 1]), G), qconj(S))[:, 1:]
        c = np.where((sg[:, m] > 0)[:, None], plus, minus)
        if mask is not None:
            c = c * mask[:, m][:, None]
        for i in range(3):
            g[:, i] += np.bincount(lk[:, m], weights=c[:, i], minlength=NL + 1)
        S = Sfrom
    return g[:NL]


class Model:
    def __init__(self):
        t = time.time()
        self.clk, self.csg, self.cst = build_contours()
        self.plk, self.psg, self.pbase, self.pplanes = build_plaquettes()
        print(f"geometry: {self.clk.shape[0]} contours, {self.plk.shape[0]} plaquettes, {time.time() - t:.1f} s",
              flush=True)

    def evaluate(self, U, V, want_soft=False):
        F = factors(U, self.plk, self.psg)
        P = products(F)
        Tp = P[:, -1]
        EW = float(np.sum(1.0 - Tp[:, 0]))
        GW = np.zeros_like(Tp); GW[:, 0] = -1.0
        gW = grad_from(F, P, GW, self.plk, self.psg)
        del F, P
        F = factors(U, self.clk, self.csg)
        P = products(F)
        T = P[:, -1]
        Mb = T.reshape(NCL, NPER, 4).mean(axis=1)
        nM = np.linalg.norm(Mb, axis=1)
        ES = KAPPA * float(np.sum(nM - np.sum(V * Mb, axis=1)))
        Gc = KAPPA * (Mb / nM[:, None] - V) / NPER
        Gs = np.repeat(Gc, NPER, axis=0)
        gS = grad_from(F, P, Gs, self.clk, self.csg)
        out = {"E": EW + ES, "EW": EW, "ES": ES, "g": gW + gS, "Mb": Mb}
        if want_soft:
            out["J"] = gS
        return out


class FastModel(Model):
    """Same energy and gradient; the contour products are factorised as A[X,sigma,off] S[y,mu] A[Y,sigma,off]^-1."""

    def __init__(self):
        super().__init__()
        t = time.time()
        xid = {X: i for i, X in enumerate(COARSE)}
        offs = list(itertools.product((-1, 0, 1), repeat=D))
        self.nA = len(COARSE) * len(ORDERS) * len(offs)
        alk = np.full((self.nA, D), NL, dtype=np.int64); asg = np.ones((self.nA, D), dtype=np.int8)
        k = 0
        for X in COARSE:
            c = root(X)
            for sig in ORDERS:
                for off in offs:
                    y = [c[i] + off[i] for i in range(D)]
                    for m, (l_, s_) in enumerate(path(c, y, sig)):
                        alk[k, m] = l_; asg[k, m] = s_
                    k += 1
        self.alk, self.asg = alk, asg
        slk = np.zeros((NS * D, L), dtype=np.int64); ssg = np.ones((NS * D, L), dtype=np.int8)
        for x in itertools.product(range(NF), repeat=D):
            for mu in range(D):
                for j in range(L):
                    z = list(x); z[mu] += j
                    slk[mu * NS + sidx(x), j] = lidx(z, mu)
        self.slk, self.ssg = slk, ssg
        iA1 = np.zeros(NCL * NPER, dtype=np.int64); iA2 = np.zeros_like(iA1); iS = np.zeros_like(iA1)
        k = 0
        no, nf = len(ORDERS), len(offs)
        for (X, mu) in CLINKS:
            cX = root(X)
            Y = list(X); Y[mu] = (Y[mu] + 1) % NC
            for si in range(no):
                for oi, off in enumerate(offs):
                    iA1[k] = (xid[X] * no + si) * nf + oi
                    iA2[k] = (xid[tuple(Y)] * no + si) * nf + oi
                    y = [cX[i] + off[i] for i in range(D)]
                    iS[k] = mu * NS + sidx(y)
                    k += 1
        self.iA1, self.iA2, self.iS = iA1, iA2, iS
        print(f"fast factorisation: {self.nA} axial paths, {time.time() - t:.1f} s", flush=True)

    @staticmethod
    def _paths_forward(U, lk, sg):
        F = factors(U, lk, sg)
        return F, products(F)

    @staticmethod
    def _paths_backward(U, F, P, Tbar, lk, sg, Ubar):
        n = F.shape[1]
        S = np.zeros((F.shape[0], 4)); S[:, 0] = 1.0
        for m in range(n - 1, -1, -1):
            fbar = qmul(qmul(qconj(P[:, m]), Tbar), qconj(S))
            neg = sg[:, m] < 0
            fbar[neg] = qconj(fbar[neg])
            for i in range(4):
                Ubar[:, i] += np.bincount(lk[:, m], weights=fbar[:, i], minlength=NL + 1)
            S = qmul(F[:, m], S)

    def evaluate(self, U, V, want_soft=False):
        F = factors(U, self.plk, self.psg)
        P = products(F)
        Tp = P[:, -1]
        EW = float(np.sum(1.0 - Tp[:, 0]))
        GW = np.zeros_like(Tp); GW[:, 0] = -1.0
        gW = grad_from(F, P, GW, self.plk, self.psg)
        FA, PA = self._paths_forward(U, self.alk, self.asg)
        FS, PS = self._paths_forward(U, self.slk, self.ssg)
        A = PA[:, -1]; Sg = PS[:, -1]
        X1 = A[self.iA1]; Y1 = Sg[self.iS]; Z1 = qconj(A[self.iA2])
        XY = qmul(X1, Y1)
        T = qmul(XY, Z1)
        Mb = T.reshape(NCL, NPER, 4).mean(axis=1)
        nM = np.linalg.norm(Mb, axis=1)
        ES = KAPPA * float(np.sum(nM - np.sum(V * Mb, axis=1)))
        Gc = KAPPA * (Mb / nM[:, None] - V) / NPER
        G = np.repeat(Gc, NPER, axis=0)
        Xbar = qmul(G, qconj(qmul(Y1, Z1)))
        Ybar = qmul(qmul(qconj(X1), G), qconj(Z1))
        Zbar = qmul(qconj(XY), G)
        Abar = np.zeros((self.nA, 4)); Sbar = np.zeros((NS * D, 4))
        A2bar = qconj(Zbar)
        for i in range(4):
            Abar[:, i] = (np.bincount(self.iA1, weights=Xbar[:, i], minlength=self.nA)
                          + np.bincount(self.iA2, weights=A2bar[:, i], minlength=self.nA))
            Sbar[:, i] = np.bincount(self.iS, weights=Ybar[:, i], minlength=NS * D)
        Ubar = np.zeros((NL + 1, 4))
        self._paths_backward(U, FA, PA, Abar, self.alk, self.asg, Ubar)
        self._paths_backward(U, FS, PS, Sbar, self.slk, self.ssg, Ubar)
        gS = qmul(Ubar[:NL], qconj(U))[:, 1:]
        out = {"E": EW + ES, "EW": EW, "ES": ES, "g": gW + gS, "Mb": Mb}
        if want_soft:
            out["J"] = gS
        return out


def coarse_field():
    Xf = np.zeros((NCL, 3))
    for ci, (X, mu) in enumerate(CLINKS):
        for k in range(D):
            ph = 2 * np.pi * X[k] / NC
            Xf[ci] += 0.0
    A = RNG.normal(size=(D, 3, D)) / 2; B = RNG.normal(size=(D, 3, D)) / 2
    for ci, (X, mu) in enumerate(CLINKS):
        for k in range(D):
            ph = 2 * np.pi * X[k] / NC
            Xf[ci] += A[k, :, mu] * np.cos(ph) + B[k, :, mu] * np.sin(ph)
    return Xf


def start_config(V):
    U = np.zeros((NL, 4)); U[:, 0] = 1.0
    third = qexp(qlog(V) / L)
    for ci, (X, mu) in enumerate(CLINKS):
        cX = root(X)
        for j in range(L):
            x = list(cX); x[mu] += j
            U[lidx(x, mu)] = third[ci]
    return U


def coarse_gauge_D(V, Mb):
    GV = -KAPPA * qmul(Mb, qconj(V))[:, 1:]
    Dx = np.zeros((len(COARSE), 3))
    xid = {X: i for i, X in enumerate(COARSE)}
    for ci, (X, mu) in enumerate(CLINKS):
        Dx[xid[X]] += GV[ci]
        Y = list(X); Y[mu] = (Y[mu] + 1) % NC
        Dx[xid[tuple(Y)]] -= Ad(qconj(V[ci]), GV[ci])
    return Dx, GV


def lin_transpose(model, r, straight_only):
    g = np.zeros((NL + 1, 3))
    w = model.csg.astype(float) / NPER
    if straight_only:
        w = w * model.cst
    rr = np.repeat(r, NPER, axis=0)
    for m in range(MAXLEN):
        for i in range(3):
            g[:, i] += np.bincount(model.clk[:, m], weights=w[:, m] * rr[:, i], minlength=NL + 1)
    return g[:NL]


def axial_mask():
    A = np.zeros(NL, dtype=bool)
    for X in COARSE:
        c = root(X)
        for rho in range(D):
            A[lidx(c, rho)] = True
            w = list(c); w[rho] -= 1
            A[lidx(w, rho)] = True
    return A


def R_ax(J, A):
    n = np.linalg.norm(J, axis=1)
    return float(n[A].mean() / n[~A].mean())


def transporter(U, a, b):
    q = np.array([1.0, 0, 0, 0])
    for (l_, s_) in path(a, b, (0, 1, 2, 3)):
        f = U[l_] if s_ > 0 else qconj(U[l_])
        q = qmul(q, f)
    return q


def measure(model, U, V):
    F = factors(U, model.plk, model.psg)
    Tp = products(F)[:, -1]
    a = qlog(Tp)
    S = L ** 2 * float(np.max(np.linalg.norm(a, axis=1)))
    pid = {}
    for k, (x, pl) in enumerate(zip(model.pbase, model.pplanes)):
        pid[(tuple(x), pl)] = k
    eps3 = []
    for X in COARSE:
        c = root(X)
        cache = {}
        Phi = {pl: a[pid[(tuple(ci % NF for ci in c), pl)]] for pl in itertools.combinations(range(D), 2)}
        m = 0.0
        for off in itertools.product(range(-2, 2 + 1), repeat=D):
            x = [c[i] + off[i] for i in range(D)]
            for pl in itertools.combinations(range(D), 2):
                mu, nu = pl
                if off[mu] > 1 or off[nu] > 1:
                    continue
                key = tuple(x)
                if key not in cache:
                    cache[key] = transporter(U, c, x)
                T = cache[key]
                at = Ad(T, a[pid[(tuple(xi % NF for xi in x), pl)]])
                m = max(m, float(np.linalg.norm(at - Phi[pl])))
        eps3.append(m)
    O = L ** 2 * float(np.mean(eps3))
    epsV = []
    for ci, (X, mu) in enumerate(CLINKS):
        cX = root(X); cY = list(cX); cY[mu] += L
        Sc = transporter(U, cX, cY)
        epsV.append(float(np.linalg.norm(qlog(qmul(V[ci], qconj(Sc))))))
    return S, O, float(np.mean(epsV))


def minimise(model, V, U, maxit=6000, tol=1e-7):
    ev = model.evaluate(U, V)
    g = ev["g"]; g0 = np.linalg.norm(g)
    eta = 0.05; gprev = None; it = 0
    while it < maxit:
        gn = np.linalg.norm(g)
        if gn <= tol * g0:
            return U, ev, it, g0, gn, True
        if gprev is not None:
            s = -eta_prev * gprev
            y = g - gprev
            sy = float(np.sum(s * y))
            eta = float(np.sum(s * s)) / sy if sy > 0 else 0.05
            eta = min(max(eta, 1e-3), 5.0)
        Un = qmul(qexp(-eta * g), U)
        Un /= np.linalg.norm(Un, axis=1, keepdims=True)
        evn = model.evaluate(Un, V)
        if evn["E"] > ev["E"] + 1e-3 * abs(ev["E"]) + 1e-12:
            eta *= 0.25
            Un = qmul(qexp(-eta * g), U); Un /= np.linalg.norm(Un, axis=1, keepdims=True)
            evn = model.evaluate(Un, V)
        gprev, eta_prev = g, eta
        U, ev, g = Un, evn, evn["g"]
        it += 1
    return U, ev, it, g0, np.linalg.norm(g), False


def main():
    smoke = len(sys.argv) > 1 and sys.argv[1] == "smoke"
    model = FastModel()
    Xc = coarse_field()
    if smoke:
        V = qexp(0.2 * Xc)
        U = start_config(V)
        U = qmul(qexp(0.05 * RNG.normal(size=(NL, 3))), U)
        t = time.time(); ev = model.evaluate(U, V, want_soft=True); dt = time.time() - t
        print(f"smoke: one evaluation {dt:.2f} s, E = {ev['E']:.6f}")
        evs = Model.evaluate(model, U, V, want_soft=True)
        print(f"  fast vs direct evaluator: |dE| = {abs(ev['E'] - evs['E']):.2e}, max|dg| = {np.max(np.abs(ev['g'] - evs['g'])):.2e}, max|dJ| = {np.max(np.abs(ev['J'] - evs['J'])):.2e}")
        for trial in range(3):
            b = int(RNG.integers(NL)); xi = RNG.normal(size=3); h = 1e-6
            Up = U.copy(); Up[b] = qmul(qexp(h * xi), U[b])
            Um = U.copy(); Um[b] = qmul(qexp(-h * xi), U[b])
            fd = (model.evaluate(Up, V)["E"] - model.evaluate(Um, V)["E"]) / (2 * h)
            print(f"  grad check link {b}: analytic {float(ev['g'][b] @ xi):.8e}  fd {fd:.8e}")
        Dx, GV = coarse_gauge_D(V, ev["Mb"])
        J = ev["J"]
        fine = np.zeros_like(Dx)
        for i, X in enumerate(COARSE):
            c = root(X)
            for rho in range(D):
                fine[i] += J[lidx(c, rho)]
                w = list(c); w[rho] -= 1
                fine[i] -= Ad(qconj(U[lidx(w, rho)]), J[lidx(w, rho)])
        print(f"  Noether identity D(X) + fine root-gauge derivative of soft term: max {np.max(np.abs(Dx + fine)):.2e} "
              f"(scale {np.max(np.abs(Dx)):.2e})")
        print(f"  peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB, total {time.time() - T0:.1f} s")
        return
    A = axial_mask()
    rctrl = RNG.normal(size=(NCL, 3))
    Rroot = R_ax(lin_transpose(model, rctrl, False), A)
    Rstr = R_ax(lin_transpose(model, rctrl, True), A)
    ok = {}
    ok["V2"] = Rroot >= 1.5 * Rstr
    print(f"V2 control power: R_ax(Q_root^T r_ctrl) = {Rroot:.3f}, R_ax(Q_str^T r_ctrl) = {Rstr:.3f} -> "
          f"{'PASS' if ok['V2'] else 'FAIL'}", flush=True)
    res = {}
    conv = True; q1 = True; q2 = True
    for t in (0.02, 0.1, 0.2, 0.4):
        V = qexp(t * Xc)
        U0 = start_config(V)
        if t == 0.2:
            ev0 = model.evaluate(U0, V)
            D0, GV0 = coarse_gauge_D(V, ev0["Mb"])
            N1s = float(np.max(np.linalg.norm(D0, axis=1)) / np.max(np.linalg.norm(GV0, axis=1)))
            ok["V3"] = N1s >= 1e-2
            print(f"V3 start-config N1 (t=0.2) = {N1s:.3e} -> {'PASS' if ok['V3'] else 'FAIL'}", flush=True)
        tt = time.time()
        U, ev, it, g0, gn, cv = minimise(model, V, U0)
        ev = model.evaluate(U, V, want_soft=True)
        Dx, GV = coarse_gauge_D(V, ev["Mb"])
        N1 = float(np.max(np.linalg.norm(Dx, axis=1)) / np.max(np.linalg.norm(GV, axis=1)))
        RaxJ = R_ax(ev["J"], A)
        RaxS = R_ax(lin_transpose(model, GV, True), A)
        RaxR = R_ax(lin_transpose(model, GV, False), A)
        S, O, eV = measure(model, U, V)
        resid = float(np.mean(np.linalg.norm(qlog(qmul(qconj(V), ev["Mb"] / np.linalg.norm(ev["Mb"], axis=1,
                                                                                            keepdims=True))), axis=1)))
        res[t] = (S, O)
        conv &= cv; q1 &= N1 <= 1e-4
        if t <= 0.2:
            q2 &= RaxJ <= 1.25 * RaxS + 0.25
        print(f"t={t}: {'CONVERGED' if cv else 'NOT CONVERGED'} it={it} |g|/|g0|={gn / g0:.1e} E={ev['E']:.8e} "
              f"(EW {ev['EW']:.6e}, ES {ev['ES']:.6e}) {time.time() - tt:.0f} s", flush=True)
        print(f"   N1={N1:.2e}  R_ax(J)={RaxJ:.3f}  R_ax(Q_str^T r_min)={RaxS:.3f}  R_ax(Q_root^T r_min)={RaxR:.3f}")
        print(f"   S/t={S / t:.5f}  O/t={O / t:.5f}  mean eps_V/t={eV / t:.5f}  mean residual/t={resid / t:.5f}",
              flush=True)
    ok["V1"] = conv
    ok["Q1"] = q1
    ok["Q2"] = q2
    Sr, Or = res[0.02][0] / 0.02, res[0.02][1] / 0.02
    dev = {t: (abs(res[t][0] / t / Sr - 1), abs(res[t][1] / t / Or - 1)) for t in res}
    for t in (0.1, 0.2, 0.4):
        print(f"   dev_S({t}) = {dev[t][0]:.4f}  dev_O({t}) = {dev[t][1]:.4f}")
    ok["Q3"] = (dev[0.1][0] <= 0.3 and dev[0.1][1] <= 0.3 and dev[0.2][0] >= dev[0.1][0]
                and dev[0.2][1] >= dev[0.1][1])
    for k in ("V1", "V2", "V3", "Q1", "Q2", "Q3"):
        print(f"{k}: {'PASS' if ok[k] else 'FAIL'}")
    valid = ok["V1"] and ok["V2"] and ok["V3"]
    print(f"c22: {'VALID' if valid else 'INVALID'}; findings Q1 {ok['Q1']}, Q2 {ok['Q2']}, Q3 {ok['Q3']}; "
          f"time {time.time() - T0:.0f} s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB")


if __name__ == "__main__":
    main()
