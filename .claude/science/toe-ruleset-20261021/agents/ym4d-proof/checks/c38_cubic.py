"""c38: the signed cubic vertex of E_1^br at the trivial background against D^3 S_W (PROOF.md [S22]; the (H-C) artefact
test of REVIEW_S21). Criteria: checks/c38_criteria.md (written first). Usage: python3 c38_cubic.py A|B|C."""
import itertools
import os
import resource
import sys
import time

import numpy as np
import scipy.fft as sfft

L, D4 = 3, 4
PLANES = [(m, n) for m in range(D4) for n in range(m + 1, D4)]
YS = [tuple(int(v) for v in y) for y in np.array(list(itertools.product(range(L), repeat=D4)))[:, ::-1]]
YIDX = {y: sum(y[m] * L ** m for m in range(D4)) for y in YS}
NLOC, NPL = 324, 486
KAP = 1.0
EPS = np.zeros((3, 3, 3))
for (a, b, c), s in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
    EPS[a, b, c] = s
BRACKET = -np.sqrt(2.0)  # <X,[Y,Z]> = BRACKET * eps_abc x^a y^b z^c for TAU = i sigma / sqrt 2, <X,Y> = -tr XY
T0 = time.time()


def rss_mb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e6 if sys.platform == "darwin" else r / 1e3


def say(s):
    print(f"{s}  ({time.time() - T0:.0f} s, RSS {rss_mb():.0f} MB)", flush=True)


def lid(y, mu):
    return YIDX[tuple(int(v) for v in y)] * 4 + mu


def axial_steps(c, y, order):
    x = list(c); out = []
    for mu in order:
        while x[mu] != y[mu]:
            if y[mu] > x[mu]:
                out.append((tuple(x), mu, +1)); x[mu] += 1
            else:
                xb = list(x); xb[mu] -= 1; out.append((tuple(xb), mu, -1)); x[mu] -= 1
    return out


def contour_steps(mu, order, y):
    """S4' contour of the coarse link (0, mu): c_X -> y -> y + L e_mu -> c_{X + e_mu} (c36 contour_steps, unwrapped)."""
    cX = (1, 1, 1, 1)
    cY = list(cX); cY[mu] += L
    st = axial_steps(cX, y, order)
    z = list(y)
    for _ in range(L):
        st.append((tuple(z), mu, +1)); z[mu] += 1
    back = axial_steps(tuple(cY), tuple(z), order)
    st += [(xb, nu, -s) for (xb, nu, s) in reversed(back)]
    return st


def split(x):
    x = np.array(x)
    return x // L, x % L


class FineGeo:
    """level-0 unit cell (one block): plaquette link lists, contours, pair weights of the soft quadratic BCH term."""

    def __init__(self):
        pl_l = np.zeros((NPL, 4), int); pl_sh = np.zeros((NPL, 4, 4)); pl_sg = np.zeros((NPL, 4))
        for y in YS:
            for ip, (mu, nu) in enumerate(PLANES):
                q = YIDX[y] * 6 + ip
                em = np.eye(4, dtype=int)[mu]; en = np.eye(4, dtype=int)[nu]
                for i, (z, m, sg) in enumerate(((np.array(y), mu, 1.0), (np.array(y) + em, nu, 1.0),
                                                (np.array(y) + en, mu, -1.0), (np.array(y), nu, -1.0))):
                    cell, yl = split(z)
                    pl_l[q, i] = lid(yl, m); pl_sh[q, i] = cell; pl_sg[q, i] = sg
        self.pl_l, self.pl_sh, self.pl_sg = pl_l, pl_sh, pl_sg
        self.nl, self.npl, self.nc = NLOC, NPL, 4
        orders = list(itertools.permutations(range(4)))
        ncont = len(orders) * len(YS)
        self.ncont = ncont
        self.soft = []
        self.contours = []
        for mu in range(4):
            sup = {}; qw = {}; pw = {}
            conts = []
            for y in YS:
                for o in orders:
                    st = contour_steps(mu, o, y)
                    keys = []
                    for (xb, nu, s) in st:
                        cell, yl = split(xb)
                        k = (tuple(int(v) for v in cell), lid(yl, nu))
                        if k not in sup:
                            sup[k] = len(sup)
                        keys.append((sup[k], s))
                        qw[k] = qw.get(k, 0.0) + s / ncont
                    for i in range(len(keys)):
                        for j in range(i + 1, len(keys)):
                            ab = (keys[i][0], keys[j][0])
                            pw[ab] = pw.get(ab, 0.0) + 0.5 * keys[i][1] * keys[j][1] / ncont
                    conts.append([(kk, s) for (kk, s) in keys])
            na = len(sup)
            inv = [None] * na
            for k, a in sup.items():
                inv[a] = k
            sl = np.array([k[1] for k in inv]); ssh = np.array([k[0] for k in inv], float)
            W = np.zeros((na, na))
            for (a, b), v in pw.items():
                W[a, b] += v
            qa = np.zeros(na)
            for k, v in qw.items():
                qa[sup[k]] += v
            self.soft.append(dict(sl=sl, ssh=ssh, W=W, qa=qa, na=na))
            self.contours.append(conts)

    def d(self, K):
        M = np.zeros((NPL, NLOC), complex)
        ph = np.exp(1j * (self.pl_sh @ K))
        np.add.at(M, (np.repeat(np.arange(NPL), 4), self.pl_l.ravel()), (self.pl_sg * ph).ravel())
        return M

    def Q(self, K):
        M = np.zeros((4, NLOC), complex)
        for mu, s in enumerate(self.soft):
            np.add.at(M[mu], s["sl"], s["qa"] * np.exp(1j * (s["ssh"] @ K)))
        return M

    def fib(self, K, kap=KAP, full=False):
        Dk = self.d(K); Qk = self.Q(K)
        M = Dk.conj().T @ Dk + kap * Qk.conj().T @ Qk
        M = (M + M.conj().T) / 2
        w, V = np.linalg.eigh(M)
        keep = w > 1e-9 * w.max()
        Mp = (V[:, keep] / w[keep]) @ V[:, keep].conj().T
        U = kap * Mp @ Qk.conj().T
        A = Dk @ U
        R = Qk @ U - np.eye(4)
        H = A.conj().T @ A + kap * R.conj().T @ R
        res = np.abs(M @ U - kap * Qk.conj().T).max()
        out = dict(U=U, A=A, R=R, H=H, res=res)
        if full:
            out.update(D=Dk, Q=Qk)
        return out


class CoarseGeo:
    """coarse lattice, unit cell = one site (4 links, 6 plaquettes); the Wilson vertex with u = B."""

    def __init__(self):
        pl_l = np.zeros((6, 4), int); pl_sh = np.zeros((6, 4, 4)); pl_sg = np.zeros((6, 4))
        for ip, (mu, nu) in enumerate(PLANES):
            em = np.eye(4)[mu]; en = np.eye(4)[nu]
            for i, (z, m, sg) in enumerate(((0 * em, mu, 1.0), (em, nu, 1.0), (en, mu, -1.0), (0 * em, nu, -1.0))):
                pl_l[ip, i] = m; pl_sh[ip, i] = z; pl_sg[ip, i] = sg
        self.pl_l, self.pl_sh, self.pl_sg = pl_l, pl_sh, pl_sg
        self.nl, self.npl, self.nc = 4, 6, 4
        self.soft = []

    def d(self, K):
        M = np.zeros((6, 4), complex)
        ph = np.exp(1j * (self.pl_sh @ K))
        np.add.at(M, (np.repeat(np.arange(6), 4), self.pl_l.ravel()), (self.pl_sg * ph).ravel())
        return M

    def fib(self, K, kap=KAP, full=False):
        Dk = self.d(K); U = np.eye(4, dtype=complex)
        return dict(U=U, A=Dk @ U, R=np.zeros((4, 4), complex), H=Dk.conj().T @ Dk, D=Dk, res=0.0)


# ======================================================================================================================
# vertex pieces
def pair_w(geo):
    """w[q, i, j] = 1/2 sigma_i sigma_j for i < j (plaquette path order)."""
    w = np.zeros((geo.npl, 4, 4))
    for i in range(4):
        for j in range(i + 1, 4):
            w[:, i, j] = 0.5 * geo.pl_sg[:, i] * geo.pl_sg[:, j]
    return w


def leg_data(geo, f, K, dt=complex):
    """per-K leg arrays: UW (npl, 4, 4) [plaquette leg i, colourless direction], US list (na, 4)."""
    U = f["U"]
    UW = U[geo.pl_l] * np.exp(1j * (geo.pl_sh @ K))[..., None]
    US = [U[s["sl"]] * np.exp(1j * (s["ssh"] @ K))[:, None] for s in geo.soft]
    return UW.astype(dt), [u.astype(dt) for u in US]


def vertex_batch(geo, w, A1, R1, UW2, US2, UW3, US3, kap=KAP):
    """V[k, mu, nu, lam] for slot-2 leg data fixed (one K2) and batches over K3 (K1 = -K2 - K3 matching A1, R1 batches).
    A1 (n, npl, 4), R1 (n, 4, 4), UW2 (npl, 4, 4), US2 list (na, 4), UW3 (n, npl, 4, 4), US3 list (n, na, 4)."""
    Ypre = np.einsum("qij,qin->qjn", w, UW2)                  # sum_{i<j} w_ij U_i(K2)
    Z = np.einsum("qjn,kqjl->kqnl", Ypre, UW3)                # (n, npl, 4, 4)
    n = UW3.shape[0]
    VW = np.matmul(np.swapaxes(A1, 1, 2), Z.reshape(n, geo.npl, 16)).reshape(n, 4, 4, 4)
    VS = np.zeros_like(VW)
    for mu, s in enumerate(geo.soft):
        Y = US2[mu].T @ s["W"]                                # (4, na)
        S = np.matmul(Y[None], US3[mu])                       # (n, 4, 4)
        VS += kap * np.einsum("km,knl->kmnl", R1[:, mu, :], S)
    return VW, VS


def vertex_single(geo, K1, K2, K3):
    fs = [geo.fib(K) for K in (K1, K2, K3)]
    w = pair_w(geo)
    UW2, US2 = leg_data(geo, fs[1], K2)
    UW3, US3 = leg_data(geo, fs[2], K3)
    VW, VS = vertex_batch(geo, w, fs[0]["A"][None], fs[0]["R"][None], UW2, US2, UW3[None], [u[None] for u in US3])
    return VW[0], VS[0]


def antisym_single(geo, K1, K2, K3):
    """V_A[mu, nu, lam] at (K1, K2, K3): (1/6) sum over simultaneous permutations of (momentum, index) slots."""
    def V(a, b, c):
        vw, vs = vertex_single(geo, a, b, c)
        return vw + vs
    out = (V(K1, K2, K3) - V(K2, K1, K3).transpose(1, 0, 2) - V(K1, K3, K2).transpose(0, 2, 1)
           - V(K3, K2, K1).transpose(2, 1, 0) + V(K2, K3, K1).transpose(2, 0, 1) + V(K3, K1, K2).transpose(1, 2, 0)) / 6
    return out


# ======================================================================================================================
# torus pipeline
def grid_coords(T):
    return np.array(list(itertools.product(range(T), repeat=4)))


def torus_vertex(geo, T, dt=np.complex64):
    """Vst_W, Vst_S of shape (N*N, 4, 4, 4): index k2*N + k3 (slot-2 momentum K2, slot-3 K3, slot 1 K1 = -K2 - K3)."""
    kc = grid_coords(T); N = len(kc)
    strides = np.array([T ** 3, T ** 2, T, 1])
    Ks = 2 * np.pi * kc / T
    fibs = [geo.fib(K) for K in Ks]
    resmax = max(f["res"] for f in fibs)
    w = pair_w(geo)
    A = np.array([f["A"] for f in fibs]).astype(dt)
    R = np.array([f["R"] for f in fibs]).astype(dt)
    legs = [leg_data(geo, f, K, dt) for f, K in zip(fibs, Ks)]
    del fibs
    UW = np.array([lg[0] for lg in legs])
    US = [np.array([lg[1][mu] for lg in legs]) for mu in range(len(geo.soft))]
    del legs
    VstW = np.zeros((N * N, 4, 4, 4), dt); VstS = np.zeros((N * N, 4, 4, 4), dt)
    for k2 in range(N):
        k1 = ((-kc[k2][None, :] - kc) % T) @ strides
        vw, vs = vertex_batch(geo, w, A[k1], R[k1], UW[k2], [u[k2] for u in US], UW, US)
        VstW[k2 * N:(k2 + 1) * N] = vw; VstS[k2 * N:(k2 + 1) * N] = vs
    del UW, US, A, R
    return VstW, VstS, kc, resmax


def antisym_torus(Vsts, kc, T, dt=np.complex64):
    """V_A over the pair grid from one or a sum of stored vertices (index k2*N + k3)."""
    N = len(kc); strides = np.array([T ** 3, T ** 2, T, 1])
    VA = np.zeros((N * N, 4, 4, 4), dt)
    k3 = np.arange(N)

    def g(idx):
        out = Vsts[0][idx].copy()
        for V in Vsts[1:]:
            out += V[idx]
        return out
    for k2 in range(N):
        k1 = ((-kc[k2][None, :] - kc) % T) @ strides
        t1 = g(k2 * N + k3)
        t2 = g(k1 * N + k3).transpose(0, 2, 1, 3)
        t3 = g(k3 * N + k2).transpose(0, 1, 3, 2)
        t4 = g(k2 * N + k1).transpose(0, 3, 2, 1)
        t5 = g(k3 * N + k1).transpose(0, 3, 1, 2)
        t6 = g(k1 * N + k2).transpose(0, 2, 3, 1)
        VA[k2 * N:(k2 + 1) * N] = (t1 - t2 - t3 - t4 + t5 + t6) / 6
    return VA


def n3_from_VA(VA, T, keep_kernel=False):
    """N3 = max_mu sum_{R2,R3,nu,lam}|t_A(R2,R3)[mu,nu,lam]| with slot 1 at the origin; kernel t_A = fftn(V_A)/T^8."""
    acc = np.zeros(4); im = 0.0
    ker = np.zeros((T,) * 8 + (64,)) if keep_kernel else None
    for c in range(64):
        arr = np.ascontiguousarray(VA[:, c // 16, (c // 4) % 4, c % 4]).astype(np.complex128).reshape((T,) * 8)
        t = sfft.fftn(arr, axes=tuple(range(8)), workers=1) / T ** 8
        im = max(im, float(np.abs(t.imag).max()))
        acc[c // 16] += np.abs(t.real).sum()
        if keep_kernel:
            ker[..., c] = t.real
        del arr, t
    return acc.max(), acc, im, ker


# ======================================================================================================================
# real-space formula and exact actions (validation)
def su2_exp(x):
    x = np.asarray(x, float)
    th = np.linalg.norm(x, axis=-1) / np.sqrt(2)
    with np.errstate(invalid="ignore", divide="ignore"):
        nh = np.where(th[..., None] > 0, x / (np.sqrt(2) * np.where(th > 0, th, 1)[..., None]), 0.0)
    SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
    nsig = np.einsum("...a,aij->...ij", nh, SIG)
    return np.cos(th)[..., None, None] * np.eye(2) + 1j * np.sin(th)[..., None, None] * nsig


def dag(V):
    return np.conj(np.swapaxes(V, -1, -2))


class Torus:
    def __init__(self, geo, T):
        self.geo, self.T = geo, T
        self.kc = grid_coords(T); self.N = len(self.kc)

    def cell(self, S):
        S = np.asarray(S) % self.T
        return np.ravel_multi_index(tuple(S[..., m] for m in range(4)), (self.T,) * 4)

    def gl(self, sh, loc):
        """global link index of local link loc in cell S + sh, for all cells S: (N, ...)"""
        sh = np.asarray(sh); loc = np.asarray(loc)
        cells = self.cell(self.kc.reshape((self.N,) + (1,) * (sh.ndim - 1) + (4,)) + sh[None].astype(int))
        return cells * self.geo.nl + loc[None]


def field_u(geo, tor, B):
    """u = U-hat B in real space; B (N, 4, 3) coarse logs per cell; returns u (N*nl, 3)."""
    T = tor.T; N = tor.N
    Bh = sfft.fftn(B.reshape((T,) * 4 + (4, 3)), axes=(0, 1, 2, 3), workers=1).reshape(N, 4, 3)
    Ks = 2 * np.pi * tor.kc / T
    uh = np.array([geo.fib(K)["U"] @ Bh[k] for k, K in enumerate(Ks)])
    u = sfft.ifftn(uh.reshape((T,) * 4 + (geo.nl, 3)), axes=(0, 1, 2, 3), workers=1).reshape(N * geo.nl, 3)
    return u.real, float(np.abs(u.imag).max()), Bh


def cubic_formula(geo, tor, u, B):
    """E_3 by the real-space formula (bracket eps_abc): Wilson + soft parts."""
    gl = tor.gl(geo.pl_sh, geo.pl_l)                    # (N, npl, 4)
    uq = u[gl]                                            # (N, npl, 4, 3)
    du = np.einsum("qi,nqia->nqa", geo.pl_sg, uq)
    w = pair_w(geo)
    GW = np.zeros_like(du)
    for i in range(4):
        for j in range(i + 1, 4):
            GW += w[None, :, i, j, None] * np.cross(uq[:, :, i], uq[:, :, j])
    EW = float((du * GW).sum())
    ES = 0.0
    for mu, s in enumerate(geo.soft):
        g = tor.gl(s["ssh"], s["sl"])                     # (N, na)
        P = u[g]                                          # (N, na, 3)
        rho = np.einsum("a,nab->nb", s["qa"], P) - B[:, mu, :]
        Mde = np.einsum("nad,ab,nbe->nde", P, s["W"], P)
        Gam = np.einsum("cde,nde->nc", EPS, Mde)
        ES += KAP * float((rho * Gam).sum())
    return EW, ES


def exact_action(geo, tor, u, B, t):
    """exact SU(2) level-0 action G(t u, t B): Wilson + kappa sum_c (2 sqrt det Mbar - Re tr V^dag Mbar)."""
    U = su2_exp(t * u)
    gl = tor.gl(geo.pl_sh, geo.pl_l)
    P = np.broadcast_to(np.eye(2, dtype=complex), gl.shape[:2] + (2, 2)).copy()
    for i in range(4):
        Ui = U[gl[:, :, i]]
        P = P @ (Ui if geo.pl_sg[0, i] > 0 else dag(Ui))
    S = float(np.real(2 - np.trace(P, axis1=-2, axis2=-1)).sum())
    if not geo.soft:
        return S
    V = su2_exp(t * B)                                    # (N, 4, 2, 2)
    for mu, s in enumerate(geo.soft):
        g = tor.gl(s["ssh"], s["sl"])                     # (N, na)
        conts = geo.contours[mu]
        Mb = np.zeros((tor.N, 2, 2), complex)
        for cont in conts:
            Pc = np.broadcast_to(np.eye(2, dtype=complex), (tor.N, 2, 2)).copy()
            for (a, sg) in cont:
                Ua = U[g[:, a]]
                Pc = Pc @ (Ua if sg > 0 else dag(Ua))
            Mb += Pc
        Mb /= len(conts)
        det = np.real(np.linalg.det(Mb))
        S += KAP * float((2 * np.sqrt(det) - np.real(np.trace(dag(V[:, mu]) @ Mb, axis1=-2, axis2=-1))).sum())
    return S


def richardson_cubic(fun, t):
    f = lambda h: (fun(h) - fun(-h)) / (2 * h ** 3)
    return (4 * f(t) - f(2 * t)) / 3


def kernel_eval(ker, B, T):
    """sum_x sum_{R2,R3} t_A(R2,R3)[mu,nu,lam] eps_abc B^a_{x,mu} B^b_{x+R2,nu} B^c_{x+R3,lam}; B (T,T,T,T,4,3)."""
    tot = 0.0
    shifts = grid_coords(T)
    for R2 in shifts:
        B2 = np.roll(B, shift=tuple(-R2), axis=(0, 1, 2, 3))
        for R3 in shifts:
            B3 = np.roll(B, shift=tuple(-R3), axis=(0, 1, 2, 3))
            k = ker[tuple(R2) + tuple(R3)].reshape(4, 4, 4)
            cr = np.einsum("abc,xmb,xlc->xmla", EPS, B2.reshape(-1, 4, 3), B3.reshape(-1, 4, 3))  # (x, nu, lam, a)
            tot += float(np.einsum("mnl,xma,xnla->", k, B.reshape(-1, 4, 3), cr))
    return tot


def bloch_eval(VstW, VstS, Bh, kc, T):
    N = len(kc); strides = np.array([T ** 3, T ** 2, T, 1]); tot = 0.0
    for k2 in range(N):
        k1 = ((-kc[k2][None, :] - kc) % T) @ strides
        V = (VstW[k2 * N:(k2 + 1) * N] + VstS[k2 * N:(k2 + 1) * N]).astype(complex)
        tot += np.einsum("kmnl,abc,kma,nb,klc->", V, EPS, Bh[k1], Bh[k2], Bh)
    return tot / N ** 2


# ======================================================================================================================
def part_A():
    ok = {}
    geo = FineGeo(); cg = CoarseGeo()
    say(f"A: geometry built ({geo.ncont} contours per coarse link; soft supports {[s['na'] for s in geo.soft]})")
    # ---- A1: against c37's fibres
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import c37_kcurv as C7
    F = C7.Fib({"a": (0.0, 1.0), "b": (1.0, 1.0)})
    F.As["b"] = F.As["b"] - F.As["a"]
    perm = np.array([F.lidx(y, mu) for y in YS for mu in range(4)])  # my local index -> Fib's
    rng = np.random.default_rng(38)
    e = dict(res=0.0, d=0.0, Q=0.0, F1=0.0, rho=0.0, H=0.0, Hfac=0.0)
    for _ in range(12):
        K = 2 * np.pi * rng.integers(0, 5, 4) / 5
        f = geo.fib(K, full=True)
        e["res"] = max(e["res"], f["res"])
        e["d"] = max(e["d"], np.abs(F.d(K)[:, perm] - f["D"]).max())
        e["Q"] = max(e["Q"], np.abs(F.Q(K)[:, perm] - f["Q"]).max())
        Ok = F.Ot(K, KAP); Dk = F.d(K); Qk = F.Q(K)
        rhs = np.hstack([Dk.conj().T @ F.iota, Qk.conj().T])
        X = np.linalg.solve(Ok, rhs); Cg = X - F.onemPi @ rhs
        x = -Cg[:, :6]
        F1 = F.iota + Dk @ x; rho = Qk @ x
        d1 = C7.d1c(K)
        e["F1"] = max(e["F1"], np.abs(f["A"] - F1 @ d1).max())
        e["rho"] = max(e["rho"], np.abs(f["R"] - rho @ d1).max())
        Xq = np.linalg.solve(Ok, Qk.conj().T)
        H1 = KAP * np.eye(4) - KAP ** 2 * (Qk @ Xq - Qk @ F.onemPi @ Qk.conj().T)
        e["H"] = max(e["H"], np.abs(f["H"] - H1).max())
        e["Hfac"] = max(e["Hfac"], np.abs(f["H"] + KAP * rho @ d1).max())
    del F
    ok["A1"] = all(v <= 1e-9 for v in e.values())
    say("A1: " + ", ".join(f"{k} {v:.1e}" for k, v in e.items()))
    # ---- A2: coarse Wilson cubic, T = 3
    T = 3; tor = Torus(cg, T)
    B = rng.standard_normal((tor.N, 4, 3))
    EW, _ = cubic_formula(cg, tor, B.reshape(-1, 3), B)
    ex = richardson_cubic(lambda t: exact_action(cg, tor, B.reshape(-1, 3), B, t), 0.01)
    r2 = ex / (BRACKET * EW)
    VW, VS, kc, _ = torus_vertex(cg, T, np.complex128)
    VA = antisym_torus([VW, VS], kc, T, np.complex128)
    _, _, _, ker = n3_from_VA(VA, T, keep_kernel=True)
    EK = kernel_eval(ker, B.reshape((T,) * 4 + (4, 3)), T)
    ok["A2"] = abs(r2 - 1) <= 1e-5 and abs(EK / EW - 1) <= 1e-10
    say(f"A2: Wilson cubic formula {EW:.10e}; exact/(bracket*formula) = {r2:.10f}; kernel/formula - 1 = {EK / EW - 1:.1e}")
    # ---- A3: fine cubic incl. soft, T = 2
    T = 2; tor = Torus(geo, T)
    B = rng.standard_normal((tor.N, 4, 3))
    u, uim, Bh = field_u(geo, tor, B)
    EW, ES = cubic_formula(geo, tor, u, B)
    say(f"A3: formula E_3 = {EW + ES:.10e} (Wilson {EW:.6e}, soft {ES:.6e}); max imag of u {uim:.1e}")
    ex = richardson_cubic(lambda t: exact_action(geo, tor, u, B, t), 0.01)
    r3 = ex / (BRACKET * (EW + ES))
    VW, VS, kc, resm = torus_vertex(geo, T, np.complex128)
    EB = bloch_eval(VW, VS, Bh, kc, T)
    VA = antisym_torus([VW, VS], kc, T, np.complex128)
    _, _, _, ker = n3_from_VA(VA, T, keep_kernel=True)
    EK = kernel_eval(ker, B.reshape((T,) * 4 + (4, 3)), T)
    eB = abs(EB / (EW + ES) - 1); eK = abs(EK / (EW + ES) - 1)
    ok["A3"] = abs(r3 - 1) <= 1e-5 and eB <= 1e-8 and eK <= 1e-8
    say(f"A3: exact/(bracket*formula) = {r3:.10f}; Bloch-vertex sum/formula - 1 = {eB:.1e} (imag {abs(EB.imag):.1e}); "
        f"kernel/formula - 1 = {eK:.1e}; fibre residual {resm:.1e}")
    print(f"A: {'PASS' if all(ok.values()) else 'FAIL'} {ok}", flush=True)


def abs_bound(geo, T):
    """N3^abs: absolute values on every fine leg (Lemma E3-style counting), slots averaged as in the antisymmetrisation."""
    kc = grid_coords(T); Ks = 2 * np.pi * kc / T; N = len(kc)
    fibs = [geo.fib(K) for K in Ks]
    sh = (T,) * 4
    m = np.abs(sfft.ifftn(np.array([f["U"] for f in fibs]).reshape(sh + (geo.nl, 4)), axes=(0, 1, 2, 3), workers=1))
    a = np.abs(sfft.ifftn(np.array([f["A"] for f in fibs]).reshape(sh + (geo.npl, 4)), axes=(0, 1, 2, 3), workers=1))
    rr = np.abs(sfft.ifftn(np.array([f["R"] for f in fibs]).reshape(sh + (4, 4)), axes=(0, 1, 2, 3), workers=1))
    del fibs
    r = m.sum(axis=(0, 1, 2, 3, 5)); c = m.sum(axis=(0, 1, 2, 3))           # (nl,), (nl, 4)
    aq = a.sum(axis=(0, 1, 2, 3, 5)); ac = a.sum(axis=(0, 1, 2, 3))         # (npl,), (npl, 4)
    rhr = rr.sum(axis=(0, 1, 2, 3, 5)); rhc = rr.sum(axis=(0, 1, 2, 3))     # (4,), (4, 4)
    w = np.abs(pair_w(geo))
    rl = r[geo.pl_l]; cl = c[geo.pl_l]                                      # (npl, 4), (npl, 4, 4)
    g = np.einsum("qij,qi,qj->q", w, rl, rl)
    N1 = ac.T @ g
    N2 = np.einsum("q,qij,qin,qj->n", aq, w, cl, rl)
    N3 = np.einsum("q,qij,qi,qjn->n", aq, w, rl, cl)
    for mu, s in enumerate(geo.soft):
        W = np.abs(s["W"]); rs = r[s["sl"]]; cs = c[s["sl"]]
        N1 = N1 + KAP * rhc[mu, :] * float(rs @ W @ rs)
        N2 = N2 + KAP * rhr[mu] * (cs.T @ W @ rs)
        N3 = N3 + KAP * rhr[mu] * (rs @ W @ cs)
    return (N1.max() + N2.max() + N3.max()) / 3, N1.max(), N2.max(), N3.max()


def part_B():
    geo = FineGeo(); cg = CoarseGeo()
    say("B: geometry built")
    R3 = {}
    for T in (4, 5):
        VW, VS, kc, _ = torus_vertex(cg, T)
        VA = antisym_torus([VW, VS], kc, T)
        nW, _, imW, _ = n3_from_VA(VA, T)
        del VW, VS, VA
        VW, VS, kc, resm = torus_vertex(geo, T)
        say(f"B T={T}: vertex grid built (fibre residual {resm:.1e})")
        out = {}
        for lab, parts in (("Wilson part", [VW]), ("soft part", [VS]), ("total", [VW, VS])):
            VA = antisym_torus(parts, kc, T)
            out[lab] = n3_from_VA(VA, T)
            del VA
        del VW, VS
        nE, accE, imE, _ = out["total"]
        R3[T] = nE / nW
        nabs = abs_bound(geo, T)
        say(f"B T={T}: N3(T_W) = {nW:.6f}; N3(T_E) = {nE:.6f} (per slot-1 direction {np.round(accE, 6).tolist()}); "
            f"Wilson part {out['Wilson part'][0]:.6f}, soft part {out['soft part'][0]:.6f}; R_3 = {R3[T]:.6f}; "
            f"max imag {max(imW, imE):.1e}")
        say(f"B T={T}: absolute-leg bound N3^abs(T_E) = {nabs[0]:.4f} (slots {nabs[1]:.4f}, {nabs[2]:.4f}, {nabs[3]:.4f}); "
            f"N3^abs/N3(T_W) = {nabs[0] / nW:.4f}")
    okB = 0.1 <= R3[5] <= 10 and abs(R3[5] - R3[4]) <= 0.1 * R3[5]
    print(f"B: {'PASS' if okB else 'FAIL'} R_3(4) = {R3[4]:.6f}, R_3(5) = {R3[5]:.6f}", flush=True)


def part_C():
    geo = FineGeo(); cg = CoarseGeo()
    say("C: geometry built")
    k1 = np.array([1.0, 0.37, -0.52, 0.81]); k1 /= np.linalg.norm(k1)
    k2 = np.array([-0.44, 0.9, 0.23, -0.61]); k2 /= np.linalg.norm(k2)
    e1 = np.array([0.3, -0.7, 0.5, 0.2]); e2 = np.array([0.6, 0.1, -0.4, 0.8]); e3 = np.array([-0.5, 0.4, 0.9, -0.1])
    e = np.array([0.7, -0.2, 0.4, 0.55])
    for s in (0.1, 0.03, 0.01, 0.003):
        K1 = s * k1; K2 = s * k2; K3 = -K1 - K2
        vE = np.einsum("mnl,m,n,l->", antisym_single(geo, K1, K2, K3), e1, e2, e3)
        vW = np.einsum("mnl,m,n,l->", antisym_single(cg, K1, K2, K3), e1, e2, e3)
        c3 = vE / vW
        f = geo.fib(s * k1); fc = cg.fib(s * k1)
        c2 = np.real(e @ f["H"] @ e) / np.real(e @ fc["H"] @ e)
        say(f"C s={s}: c_3 = {c3.real:.6f} (imag {c3.imag:.1e}; V_A^W = {vW:.3e}); c_2 = {c2:.6f}; c_3 - c_2 = "
            f"{c3.real - c2:.2e}")
    print("C: informational", flush=True)


def part_D():
    """POST-HOC diagnostic (added after the B run, not a criterion): where the l1 mass of N3 sits on the torus. Mass of
    sum_{nu,lam}|t_A(R2,R3)[0,nu,lam]| binned by the shell s = max(|R2|_inf, |R3|_inf) (torus distances), T = 4, 5."""
    geo = FineGeo(); cg = CoarseGeo()
    for T in (4, 5):
        r = np.arange(T); r = np.minimum(r, T - r)
        g4 = np.max(np.stack(np.meshgrid(r, r, r, r, indexing="ij")), 0)
        shell = np.maximum(g4[(...,) + (None,) * 4], g4[(None,) * 4 + (...,)])
        for lab, gg in (("S_W", cg), ("E_1^br", geo)):
            VW, VS, kc, _ = torus_vertex(gg, T)
            VA = antisym_torus([VW, VS], kc, T)
            del VW, VS
            prof = np.zeros(T // 2 + 1)
            for c in range(16):
                arr = np.ascontiguousarray(VA[:, 0, c // 4, c % 4]).astype(np.complex128).reshape((T,) * 8)
                t = np.abs((sfft.fftn(arr, axes=tuple(range(8)), workers=1) / T ** 8).real)
                for sh in range(T // 2 + 1):
                    prof[sh] += t[shell == sh].sum()
            del VA
            say(f"D T={T} {lab}: N3 mass by shell max(|R2|,|R3|) = " + ", ".join(f"{v:.4f}" for v in prof)
                + f"; total {prof.sum():.4f}")
    print("D: post-hoc diagnostic", flush=True)


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C, "D": part_D}[sys.argv[1]]()
