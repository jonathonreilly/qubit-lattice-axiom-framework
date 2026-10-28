"""c37: the one-level curvature amplification K_curv at the trivial background, d = 4, L = 3 (PROOF.md [S21]).
Criteria: checks/c37_criteria.md (written first). Usage: python3 c37_kcurv.py A|B|C|D|E."""
import itertools
import os
import resource
import sys
import time

import numpy as np
import scipy.fft as sfft
import scipy.sparse as sp
import scipy.sparse.linalg as spl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c35_n5bg as C5  # noqa: E402

L, D4 = 3, 4
PLANES = [(m, n) for m in range(D4) for n in range(m + 1, D4)]
YS = [tuple(y) for y in np.array(list(itertools.product(range(L), repeat=D4)))[:, ::-1]]  # y with yidx = sum y_mu 3^mu
YIDX = {y: sum(int(y[m]) * L ** m for m in range(D4)) for y in YS}
NPL = len(YS) * len(PLANES)  # 486
T0 = time.time()


def rss_mb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e6 if sys.platform == "darwin" else r / 1e3


def say(s):
    print(f"{s}  ({time.time() - T0:.0f} s, RSS {rss_mb():.0f} MB)", flush=True)


# ======================================================================================================================
# level-0 Bloch fibres (unit cell = one block of 3^4 sites; 324 links, 486 plaquettes)
class Fib:
    def __init__(self, builds):
        G = C5.Geo(4, 3, 3)
        self.G = G
        blk0 = [b for b in range(G.nl) if G.block_of_site(b // 4) == (0, 0, 0, 0)]
        self.blk0 = blk0
        self.nloc = nloc = len(blk0)
        bloc = {b: k for k, b in enumerate(blk0)}
        self.lidx = lambda y, mu: bloc[G.lid(tuple(int(v) for v in y), mu)]
        bsite = np.arange(G.nl) // 4
        Bk = G.coords[bsite] // L
        shift = np.where(Bk == 2, -1, Bk)
        loc_of = np.zeros(G.nl, int)
        for b in range(G.nl):
            loc_of[b] = bloc[G.lid(tuple(G.coords[b // 4] % L), b % 4)]
        self.loc_of, self.shift = loc_of, shift
        shifts = list(itertools.product((-1, 0, 1), repeat=4))
        sidx = {s: i for i, s in enumerate(shifts)}
        self.sh_of = np.array([sidx[tuple(r)] for r in shift])
        self.S_arr = np.array(shifts, float)
        E = np.zeros((G.nl, nloc)); E[blk0, np.arange(nloc)] = 1
        self.As = {}
        op = None
        for name, (kap, aww) in builds.items():
            op = C5.AbOp(G, kappa=kap, a_ww=aww)
            cols = op.Ot(E)
            As = np.zeros((81, nloc, nloc))
            for j in range(G.nl):
                As[self.sh_of[j], :, loc_of[j]] += cols[j, :]
            self.As[name] = As.reshape(81, -1)
            del cols, As
        PiE = op.Pi(E)
        self.Pih = PiE[blk0, :].copy()
        self.onemPi = np.eye(nloc) - self.Pih
        del PiE
        iX0 = G.blocks.index((0, 0, 0, 0))
        Qc = op.Q[iX0 * 4:(iX0 + 1) * 4, :].tocoo()
        Qs = np.zeros((81, 4, nloc))
        for r, c, v in zip(Qc.row, Qc.col, Qc.data):
            Qs[self.sh_of[c], r, loc_of[c]] += v
        self.Qs = Qs.reshape(81, -1)
        self.op = op
        del E
        # d fibre data: local plaquette (yidx*6 + ip) -> local link, cell shift, sign
        rows, cols, shs, sgs = [], [], [], []
        for y in YS:
            for ip, (mu, nu) in enumerate(PLANES):
                pl = YIDX[y] * 6 + ip
                em = np.eye(D4, dtype=int)[mu]; en = np.eye(D4, dtype=int)[nu]
                for z, m, sg in ((np.array(y), mu, 1.0), (np.array(y) + em, nu, 1.0), (np.array(y) + en, mu, -1.0),
                                 (np.array(y), nu, -1.0)):
                    rows.append(pl); cols.append(self.lidx(z % L, m)); shs.append(z // L); sgs.append(sg)
        self.d_rows, self.d_cols = np.array(rows), np.array(cols)
        self.d_sh, self.d_sg = np.array(shs, float), np.array(sgs)
        iota = np.zeros((NPL, 6))
        J = np.zeros((nloc, 4))
        for y in YS:
            for ip, (mu, nu) in enumerate(PLANES):
                if y[mu] == L - 1 and y[nu] == L - 1:
                    iota[YIDX[y] * 6 + ip, ip] = 1.0
            for mu in range(D4):
                if y[mu] == L - 1:
                    J[self.lidx(y, mu), mu] = 1.0
        self.iota, self.J = iota, J

    def ph(self, K):
        return np.exp(1j * (self.S_arr @ K))

    def fib(self, A2, K, n1, n2):
        p = self.ph(K)
        return (p.real @ A2 + 1j * (p.imag @ A2)).reshape(n1, n2)

    def Ot(self, K, kap=1.0):
        M = self.fib(self.As["a"], K, self.nloc, self.nloc) + kap * self.fib(self.As["b"], K, self.nloc, self.nloc)
        return (M + M.conj().T) / 2

    def Q(self, K):
        return self.fib(self.Qs, K, 4, self.nloc)

    def d(self, K):
        M = np.zeros((NPL, self.nloc), complex)
        np.add.at(M, (self.d_rows, self.d_cols), self.d_sg * np.exp(1j * (self.d_sh @ K)))
        return M


def d1c(K):  # coarse curl fibre, 6 x 4
    M = np.zeros((6, 4), complex)
    for j, (mu, nu) in enumerate(PLANES):
        M[j, mu] += 1 - np.exp(1j * K[nu]); M[j, nu] += np.exp(1j * K[mu]) - 1
    return M


def d0c(K):  # coarse gradient fibre, 4 x 1
    return (np.exp(1j * K) - 1).reshape(4, 1)


def grid(T):
    return list(itertools.product(range(T), repeat=4))


def level0_hats(F, T, kap=1.0, want_x=False, cdt=np.complex64):
    """F1hat (T^4, 486, 6), rhohat (T^4, 4, 6) [, xhat (T^4, 324, 6), aphat (T^4, 324, 4)] of the trivial kernels."""
    shp = (T,) * 4
    F1h = np.zeros(shp + (NPL, 6), cdt); rh = np.zeros(shp + (4, 6), cdt)
    if want_x:
        xh = np.zeros(shp + (F.nloc, 6), np.complex64); aph = np.zeros(shp + (F.nloc, 4), np.complex64)
    done = np.zeros(shp, bool)
    for idx in grid(T):
        if done[idx]:
            continue
        K = 2 * np.pi * np.array(idx) / T
        Ok = F.Ot(K, kap); Dk = F.d(K); Qk = F.Q(K)
        rhs = np.hstack([Dk.conj().T @ F.iota, Qk.conj().T])
        X = np.linalg.solve(Ok, rhs)
        Cg = X - F.onemPi @ rhs
        x = -Cg[:, :6]
        vals = [F.iota + Dk @ x, Qk @ x]
        if want_x:
            vals += [x, kap * Cg[:, 6:]]
        mi = tuple((-np.array(idx)) % T)
        for arr, v in zip([F1h, rh] + ([xh, aph] if want_x else []), vals):
            arr[idx] = v; arr[mi] = v.conj()
        done[idx] = True; done[mi] = True
    return (F1h, rh, xh, aph) if want_x else (F1h, rh)


def kernel(hat, rdt=np.float32):
    """real-space torus kernel k(S)[r, c] = (1/T^4) sum_K hat(K) e^{-iK.S} (float32); returns (k, max |imag|)."""
    T = hat.shape[0]
    out = np.zeros(hat.shape, rdt); im = 0.0
    for c in range(hat.shape[-1]):
        kc = sfft.fftn(np.ascontiguousarray(hat[..., c]), axes=(0, 1, 2, 3), workers=1) / T ** 4
        im = max(im, float(np.abs(kc.imag).max())); out[..., c] = kc.real
        del kc
    return out, im


def kernel_stats(hat, dist=None):
    """streamed: per-row l1 sums, max |imag|, and (if dist) max |entry| by coarse distance and per-row mass at distance 0."""
    T = hat.shape[0]
    rs = np.zeros(hat.shape[-2]); im = 0.0
    prof = np.zeros(T // 2 + 1); m0 = np.zeros(hat.shape[-2])
    for c in range(hat.shape[-1]):
        kc = sfft.fftn(np.ascontiguousarray(hat[..., c]), axes=(0, 1, 2, 3), workers=1) / T ** 4
        im = max(im, float(np.abs(kc.imag).max()))
        a = np.abs(kc.real); del kc
        rs += a.sum(axis=(0, 1, 2, 3))
        if dist is not None:
            for r in range(T // 2 + 1):
                prof[r] = max(prof[r], float(a[dist == r].max()))
            m0 += a[dist == 0].sum(axis=0)
        del a
    return rs, im, prof, m0


def rowsums(k):
    return np.abs(k).sum(axis=(0, 1, 2, 3, 5))  # per row


def colsums(k):
    return np.abs(k).sum(axis=(0, 1, 2, 3, 4))  # per column


def tdist_inf(T):
    r = np.arange(T); r = np.minimum(r, T - r)
    return np.max(np.stack(np.meshgrid(r, r, r, r, indexing="ij")), 0)


def coarse_D(T):
    """coarse curl on the side-T torus, rows (S, plane), cols (S, mu), S raveled C-order."""
    n = T ** 4
    S = np.array(np.unravel_index(np.arange(n), (T,) * 4)).T
    rows, cols, vals = [], [], []
    for j, (mu, nu) in enumerate(PLANES):
        Sm = S.copy(); Sm[:, mu] = (Sm[:, mu] + 1) % T
        Sn = S.copy(); Sn[:, nu] = (Sn[:, nu] + 1) % T
        im_ = np.ravel_multi_index(Sm.T, (T,) * 4); in_ = np.ravel_multi_index(Sn.T, (T,) * 4)
        r = np.arange(n) * 6 + j
        for c, v in ((np.arange(n) * 4 + mu, 1.0), (im_ * 4 + nu, 1.0), (in_ * 4 + mu, -1.0), (np.arange(n) * 4 + nu, -1.0)):
            rows += list(r); cols += list(c); vals += [v] * n
    return sp.csr_matrix((vals, (rows, cols)), shape=(6 * n, 4 * n))


def lp_norm(obj, Dm, B):
    from scipy.optimize import linprog
    A = sp.vstack([Dm, -Dm]).tocsr()
    res = linprog(-obj, A_ub=A, b_ub=np.ones(A.shape[0]), bounds=(-B, B), method="highs")
    if res.status != 0:
        return float("nan")
    return -res.fun


# ======================================================================================================================
def part_A():
    ok = {}
    F = Fib({"a": (0.0, 1.0), "b": (1.0, 1.0)})
    F.As["b"] = F.As["b"] - F.As["a"]
    G, op = F.G, F.op  # op: kappa = 1
    say("A: fibres built")
    T = 3
    # real-space objects on the T = 3 torus (fine side 9)
    Dc = coarse_D(T)  # coarse ordering: raveled C-order over block coords
    nb = T ** 4
    # map Geo blocks (X tuples) -> raveled index
    bl_rav = np.array([np.ravel_multi_index(X, (T,) * 4) for X in G.blocks])
    # J in real space: coarse link (X, mu) -> fine links (L X + y, mu), y_mu = L - 1
    Jr = sp.lil_matrix((G.nl, nb * 4))
    for iX, X in enumerate(G.blocks):
        for y in YS:
            for mu in range(4):
                if y[mu] == L - 1:
                    Jr[G.lid(tuple(L * Xi + yi for Xi, yi in zip(X, y)), mu), bl_rav[iX] * 4 + mu] = 1.0
    Jr = Jr.tocsr()
    # Q rows ordered (Geo block index iX, mu) -> permute to raveled
    perm = np.zeros(nb * 4, int)
    for iX in range(nb):
        for mu in range(4):
            perm[bl_rav[iX] * 4 + mu] = iX * 4 + mu
    Qr = op.Q[perm, :]
    # iota in real space: coarse plaquette (Xrav, j) -> fine plaquettes (ip*ns + s)
    Ir = sp.lil_matrix((op.d1.shape[0], nb * 6))
    for iX, X in enumerate(G.blocks):
        for y in YS:
            for j, (mu, nu) in enumerate(PLANES):
                if y[mu] == L - 1 and y[nu] == L - 1:
                    s = G.sid(tuple(L * Xi + yi for Xi, yi in zip(X, y)))
                    Ir[j * G.ns + s, bl_rav[iX] * 6 + j] = 1.0
    Ir = Ir.tocsr()
    rng = np.random.default_rng(37)
    a = rng.standard_normal(nb * 4)
    e1 = np.abs(Qr @ (Jr @ a) - a).max()
    e2 = np.abs(op.d1 @ (Jr @ a) - Ir @ (Dc @ a)).max()
    ok["A1"] = e1 <= 1e-12 and e2 <= 1e-12
    say(f"A1: max|QJa - a| = {e1:.1e}; max|dJa - iota d_1 a| = {e2:.1e}")
    # A2: direct kernel columns vs Bloch
    lin = op.lin()
    F1h, rh = level0_hats(F, T, cdt=np.complex128)
    kF, _ = kernel(F1h, np.float64); kr, _ = kernel(rh, np.float64)
    errF = errr = 0.0; mxF = np.abs(kF).max(); mxr = np.abs(kr).max(); maxres = 0.0
    for j in range(6):
        delta = np.zeros(nb * 6); delta[j] = 1.0  # coarse plaquette (X = 0, plane j)
        f = Ir @ delta
        g = op.d1.T @ f
        y, info = spl.cg(lin, g, rtol=1e-13, maxiter=20000)
        res = np.linalg.norm(op.Ot(y) - g) / np.linalg.norm(g); maxres = max(maxres, res)
        x = -(y - (g - op.Pi(g)))
        F1 = f + op.d1 @ x
        rho = Qr @ x
        # compare: fine plaquette (ip, s) at cell R, local y -> Bloch kernel k(-R)[yidx*6+ip, j]
        for ip in range(6):
            for s in range(G.ns):
                xc = G.coords[s]; R = xc // L; yl = tuple(int(v) for v in xc % L)
                mR = tuple((-R) % T)
                errF = max(errF, abs(F1[ip * G.ns + s] - kF[mR + (YIDX[yl] * 6 + ip, j)]))
        for Sr in range(nb):
            R = np.array(np.unravel_index(Sr, (T,) * 4)); mR = tuple((-R) % T)
            for mu in range(4):
                errr = max(errr, abs(rho[Sr * 4 + mu] - kr[mR + (mu, j)]))
    ok["A2"] = maxres <= 1e-12 and errF <= 1e-8 * mxF and errr <= 1e-8 * mxr
    say(f"A2: CG rel. residual {maxres:.1e}; max|direct - Bloch| F_1 {errF:.1e} (max entry {mxF:.3f}), rho {errr:.1e} "
        f"(max entry {mxr:.3f})")
    # A3
    lo, hi = np.inf, -np.inf
    for _ in range(20):
        K = 2 * np.pi * rng.integers(0, 8, 4) / 8
        Ok = F.Ot(K); Dk = F.d(K)
        Cm = np.linalg.inv(Ok) - F.onemPi
        ev = np.linalg.eigvalsh(Dk @ Cm @ Dk.conj().T)
        lo, hi = min(lo, ev.min()), max(hi, ev.max())
    ok["A3"] = lo >= -1e-10 and hi <= 1 + 1e-10
    say(f"A3: eigenvalues of d C d^* over 20 random K: [{lo:.3e}, {1 - hi:.3e} below 1]")
    print(f"A: {'PASS' if all(ok.values()) else 'FAIL'} {ok}", flush=True)


def part_B():
    F = Fib({"a": (0.0, 1.0), "b": (1.0, 1.0)})
    F.As["b"] = F.As["b"] - F.As["a"]
    del F.op
    say("B: fibres built")
    res = {}
    for T in (6, 8, 10):
        F1h, rh = level0_hats(F, T)
        dist = tdist_inf(T)
        rsF, imF, prof, m0 = kernel_stats(F1h, dist); del F1h
        rsr, imr, profr, _ = kernel_stats(rh, dist); del rh
        Kp, Kr = rsF.max(), rsr.max()
        ip = int(rsF.argmax()); y = YS[ip // 6]
        res[T] = max(Kp, Kr)
        say(f"B T={T}: K_p = {Kp:.6f} (row: local site {y}, plane {PLANES[ip % 6]}; its l1 mass at coarse distance 0: "
            f"{m0[ip]:.4f}); K_rho = {Kr:.6f} (row mu = {int(rsr.argmax())}); K_curv = {res[T]:.6f}; max imag "
            f"{max(imF, imr):.1e}")
        say(f"B T={T}: decay profile max|K(p,P)| by coarse l^inf distance: " + ", ".join(f"{v:.2e}" for v in prof)
            + "; max|K_rho|: " + ", ".join(f"{v:.2e}" for v in profr))
    okB = res[10] < 1 and abs(res[10] - res[8]) <= 0.02
    print(f"B: {'PASS' if okB else 'FAIL'} K_curv(6, 8, 10) = {res[6]:.6f}, {res[8]:.6f}, {res[10]:.6f}", flush=True)


def part_C():
    F = Fib({"a": (0.0, 1.0), "b": (1.0, 1.0)})
    F.As["b"] = F.As["b"] - F.As["a"]
    del F.op
    say("C: fibres built")
    T = 10
    F1h, rh = level0_hats(F, T)
    Ks = [2 * np.pi * np.array(idx) / T for idx in grid(T)]
    d1h = np.array([d1c(K) for K in Ks]).reshape((T,) * 4 + (6, 4))
    rng = np.random.default_rng(370)
    cases = []
    a = np.zeros((T,) * 4 + (4,)); a[0, 0, 0, 0, 0] = 1.0; cases.append(("one coarse link", a))
    for s in range(3):
        cases.append((f"random seed {s}", rng.standard_normal((T,) * 4 + (4,))))
    a = np.zeros((T,) * 4 + (4,)); X1 = np.arange(T)
    a[..., 0] = np.sin(2 * np.pi * X1 / T)[None, :, None, None]; cases.append(("smooth sin", a))
    for lab, a in cases:
        at = sfft.fftn(a, axes=(0, 1, 2, 3), workers=1)
        Ft = np.einsum("...jm,...m->...j", d1h, at)
        FV = sfft.ifftn(Ft, axes=(0, 1, 2, 3), workers=1).real
        w = sfft.ifftn(np.einsum("...pj,...j->...p", F1h, Ft), axes=(0, 1, 2, 3), workers=1).real
        r = sfft.ifftn(np.einsum("...cj,...j->...c", rh, Ft), axes=(0, 1, 2, 3), workers=1).real
        eV = np.abs(FV).max()
        say(f"C1 {lab}: sup|F_V| = {eV:.3e}; sup|F_1|/sup|F_V| = {np.abs(w).max() / eV:.4f}; "
            f"sup|rho|/sup|F_V| = {np.abs(r).max() / eV:.4f}")
    del F1h, rh
    T = 6
    F1h, rh = level0_hats(F, T)
    Ks = [2 * np.pi * np.array(idx) / T for idx in grid(T)]
    d1h = np.array([d1c(K) for K in Ks]).reshape((T,) * 4 + (6, 4))
    kF, _ = kernel(F1h); kr, _ = kernel(rh)
    rsF = rowsums(kF); rsr = rowsums(kr)
    kA, _ = kernel(np.einsum("...pj,...jm->...pm", F1h, d1h).astype(np.complex64))
    kAr, _ = kernel(np.einsum("...cj,...jm->...cm", rh, d1h).astype(np.complex64))
    del F1h, rh
    Dm = coarse_D(T)
    top = np.argsort(-rsF)[:16]
    best = (0, None)
    for ip in top:
        obj = kA[..., ip, :].reshape(-1)
        v50 = lp_norm(obj, Dm, 50.0); v100 = lp_norm(obj, Dm, 100.0)
        if v50 > best[0]:
            best = (v50, ip)
        say(f"C2 F-row {ip} (site {YS[ip // 6]}, plane {PLANES[ip % 6]}): row sum {rsF[ip]:.5f}; exact norm (LP) "
            f"B=50 {v50:.5f}, B=100 {v100:.5f}")
    for mu in range(4):
        obj = kAr[..., mu, :].reshape(-1)
        v50 = lp_norm(obj, Dm, 50.0); v100 = lp_norm(obj, Dm, 100.0)
        say(f"C2 rho-row mu={mu}: row sum {rsr[mu]:.5f}; exact norm (LP) B=50 {v50:.5f}, B=100 {v100:.5f}")
    print(f"C: informational; max row sum K_p(6) = {rsF.max():.5f}, K_rho(6) = {rsr.max():.5f}; max LP over the "
          f"16 rows {best[0]:.5f}", flush=True)


def part_D():
    F = Fib({"a": (0.0, 1.0), "b": (1.0, 1.0)})
    F.As["b"] = F.As["b"] - F.As["a"]
    del F.op
    say("D: fibres built")
    T = 8
    for kap in (0.25, 4.0, 16.0):
        F1h, rh = level0_hats(F, T, kap)
        kF, _ = kernel(F1h); del F1h
        kr, _ = kernel(rh); del rh
        say(f"D1 kappa={kap}: K_p = {rowsums(kF).max():.6f}, K_rho = {rowsums(kr).max():.6f}")
        del kF, kr
    F1h, rh, xh, aph = level0_hats(F, T, 1.0, want_x=True)
    del F1h, rh
    kx, _ = kernel(xh); del xh
    ka, _ = kernel(aph); del aph
    KA = rowsums(kx).max()
    Zr = rowsums(ka).max(); Zc = colsums(ka).max()
    say(f"D2 kappa=1: K_A = {KA:.6f}; Z_row = {Zr:.6f}; Z_col = {Zc:.6f}; Z_col Z_row^2 = {Zc * Zr ** 2:.6f}; "
        f"(1 + Z_col) max(1, Z_row)^2 = {(1 + Zc) * max(1.0, Zr) ** 2:.6f}")
    print("D: informational", flush=True)


def part_E():
    F = Fib({"one": (1.0, 1.0), "loc": (1.0, 0.0)})
    del F.op
    say("E: fibres built")
    kap = 1.0
    nloc = F.nloc
    # H_1 on the level-1 grid (2 pi / 12) Z^4 (c36 D)
    n1 = 12
    H1 = np.zeros((n1,) * 4 + (4, 4), complex)
    done = np.zeros((n1,) * 4, bool)
    for idx in grid(n1):
        if done[idx]:
            continue
        p = 2 * np.pi * np.array(idx) / n1
        Ok = F.fib(F.As["one"], p, nloc, nloc); Ok = (Ok + Ok.conj().T) / 2
        Qk = F.Q(p)
        X = np.linalg.solve(Ok, Qk.conj().T)
        Hk = kap * np.eye(4) - kap * kap * (Qk @ X - Qk @ F.onemPi @ Qk.conj().T)
        Hk = (Hk + Hk.conj().T) / 2
        mi = tuple((-np.array(idx)) % n1)
        H1[idx] = Hk; H1[mi] = Hk.conj(); done[idx] = True; done[mi] = True
    say("E: H_1 grid built")
    # per-mode check (c36 D1)
    pp = np.full(4, np.pi); ddp = d1c(pp).conj().T @ d1c(pp)
    w_, V_ = np.linalg.eigh((ddp + ddp.conj().T) / 2); Bc = V_[:, 1:]
    A1 = Bc.conj().T @ (0.5 * H1[(6, 6, 6, 6)]) @ Bc; B1 = Bc.conj().T @ ddp @ Bc
    Li = np.linalg.inv(np.linalg.cholesky(B1))
    ratio = np.linalg.eigvalsh(Li @ A1 @ Li.conj().T)[0]
    pos = F.G.coords[np.array(F.blk0) // 4].astype(float); mu_of = np.array(F.blk0) % 4
    js = np.array(list(itertools.product(range(3), repeat=4)))
    n2 = 4
    shp = (n2,) * 4
    hats = {i: (np.zeros(shp + (NPL, 4), np.complex64), np.zeros(shp + (4, 4), np.complex64)) for i in (0, 1)}
    gerr = {0: 0.0, 1: 0.0}
    for k2 in grid(n2):
        K2 = 2 * np.pi * np.array(k2) / n2
        pidx = (np.array(k2)[None, :] + n2 * js) % n1
        Fm = np.exp(1j * ((2 * np.pi * pidx / n1) @ pos.T))
        Hsel = H1[pidx[:, 0], pidx[:, 1], pidx[:, 2], pidx[:, 3]]
        Hf = np.zeros((nloc, nloc), complex)
        for m in range(4):
            Im = np.where(mu_of == m)[0]
            for m2 in range(4):
                Im2 = np.where(mu_of == m2)[0]
                Hf[np.ix_(Im, Im2)] = Fm[:, Im].T @ (Hsel[:, m, m2][:, None] * Fm[:, Im2].conj()) / 81
        Dk = F.d(K2); Qk = F.Q(K2); d0 = d0c(K2)
        Oone = F.fib(F.As["one"], K2, nloc, nloc); Oone = (Oone + Oone.conj().T) / 2
        Oloc = F.fib(F.As["loc"], K2, nloc, nloc)
        O1 = F.Pih @ Hf @ F.Pih + Oloc; O1 = (O1 + O1.conj().T) / 2
        H0 = Dk.conj().T @ Dk
        for i, (Ok, Hk) in ((0, (Oone, H0)), (1, (O1, Hf))):
            rhs = Hk @ F.J
            Cg = np.linalg.solve(Ok, rhs) - F.onemPi @ rhs
            Am = Dk @ (F.J - Cg); Rm = -Qk @ Cg
            hats[i][0][k2] = Am; hats[i][1][k2] = Rm
            gerr[i] = max(gerr[i], np.linalg.norm(Am @ d0), np.linalg.norm(Rm @ d0))
    okE1 = max(gerr.values()) <= 1e-8 and abs(ratio - 0.030950) <= 1e-4 * 0.030950
    say(f"E1: gauge annihilation level 0 {gerr[0]:.1e}, level 1 {gerr[1]:.1e}; per-mode ratio {ratio:.6f} (c36 D1 0.030950)")
    if not okE1:
        print("E: E1 FAILED, no numbers reported", flush=True)
        return
    Dm = coarse_D(n2)
    for i in (0, 1):
        kA, imA = kernel(hats[i][0]); kR, imR = kernel(hats[i][1])
        vals = [lp_norm(kA[..., p, :].reshape(-1), Dm, 50.0) for p in range(NPL)]
        valr = [lp_norm(kR[..., c, :].reshape(-1), Dm, 50.0) for c in range(4)]
        vp = int(np.nanargmax(vals))
        say(f"E2 level {i} (torus side 4): exact K_p = {np.nanmax(vals):.5f} (row site {YS[vp // 6]}, plane "
            f"{PLANES[vp % 6]}); exact K_rho = {np.nanmax(valr):.5f}; nan count {int(np.isnan(vals).sum())}; max imag "
            f"{max(imA, imR):.1e}")
    print("E: informational (E1 holds)", flush=True)


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C, "D": part_D, "E": part_E}[sys.argv[1]]()
