"""bb4: model checks for BFT_B.md session 4 (criteria: checks/bb4_criteria.md, written first).

(A) m = 0 regime of the walk factor (single box, sup norms).
(B) frame covariance of the local-torus construction (SU(2) covariant Laplacian, background given).
(C) hard-slice parametrix identity (abelian 1-form model, tent slice).
Model operators only; nothing here tests k-uniformity, lane A's norms or (CovLift).
"""
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

T0 = time.time()
SEED = 20261028
RESULTS = {}


def sig(t):
    t = np.asarray(t, float)
    return np.where(t <= 0, 1.0, np.where(t <= 0.5, 1 - 2 * t * t, np.where(t <= 1, 2 * (1 - t) ** 2, 0.0)))


def dist_iv(t, a, b, T):
    """distance on the circle R/TZ from t to the closed interval [a, b] (b - a < T)."""
    u = np.mod(np.asarray(t, float) - a, T)
    L = b - a
    return np.where(u <= L, 0.0, np.minimum(u - L, T - u))


def report(name, ok, msg):
    RESULTS[name] = bool(ok)
    print(f"{name} {'PASS' if ok else 'FAIL'}: {msg}")


# ---------------------------------------------------------------- (A)
def lap2d(n):
    N = n * n
    idx = np.arange(N).reshape(n, n)
    rows, cols, vals = [], [], []
    for sh in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nb = np.roll(idx, shift=(-sh[0], -sh[1]), axis=(0, 1))
        rows.append(idx.ravel()); cols.append(nb.ravel()); vals.append(-np.ones(N))
    rows.append(idx.ravel()); cols.append(idx.ravel()); vals.append(4 * np.ones(N))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))


def blockproj(n, b=3):
    N = n * n
    x, y = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    blk = ((x // b) * (n // b) + (y // b)).ravel()
    M = sp.csr_matrix((np.ones(N), (np.arange(N), blk)), shape=(N, (n // b) ** 2))
    return (M @ M.T) / float(b * b)  # block-average projector


def part_A():
    print("== (A) m = 0 regime ==")
    out = {}
    for model in ("A1", "A0"):
        out[model] = []
        for R in (6, 12, 18, 24, 30):
            Tw = 3 * int(np.ceil((3 * R + 14) / 3))
            N = Tw * Tw
            o = 3 * ((Tw - R) // 6)
            Lap = lap2d(Tw)
            x, y = np.meshgrid(np.arange(Tw), np.arange(Tw), indexing="ij")
            dx = dist_iv(x, o, o + R - 1, Tw); dy = dist_iv(y, o, o + R - 1, Tw)
            psi = (sig((dx - R / 2) / (R / 2)) * sig((dy - R / 2) / (R / 2))).ravel()
            inp = np.where(((dx <= 1) & (dy <= 1)).ravel())[0]
            F = np.zeros((N, len(inp))); F[inp, np.arange(len(inp))] = 1.0
            Psi = sp.diags(psi)
            if model == "A1":
                Lloc = (Lap + blockproj(Tw) / 9.0).tocsc()
                U = spla.splu(Lloc).solve(F)
            else:
                Lloc = Lap.tocsc()
                Lpin = Lap.tolil(); Lpin[0, 0] += 1.0
                lu = spla.splu(Lpin.tocsc())
                fbar = F.mean(axis=0)
                W = lu.solve(F - fbar)
                U = (W - W.mean(axis=0)) + fbar
            C = (Lloc @ Psi - Psi @ Lloc)
            G = np.abs(U).sum(axis=1).max()
            r = np.abs(C @ U).sum(axis=1).max()
            out[model].append((R, G, r))
            print(f"  {model} R={R:2d} T_W={Tw:3d} G_box={G:.4e} r_box={r:.4e} R*r={R * r:.4e}")
    a1 = out["A1"]; a0 = out["A0"]
    r6 = a1[0][2]; G6 = a1[0][1]
    ok1 = max(R * r for (R, G, r) in a1[1:]) <= 6 * r6 and max(G for (_, G, _) in a1) <= 2 * G6
    report("A-1", ok1, f"A1: max_(R>=12) R*r = {max(R * r for (R, G, r) in a1[1:]):.3e} vs 6*r(6) = {6 * r6:.3e}; "
           f"max G = {max(G for (_, G, _) in a1):.3e} vs 2*G(6) = {2 * G6:.3e}")
    ok2 = a0[-1][1] >= 4 * a0[0][1] and 30 * a0[-1][2] >= 2 * 6 * a0[0][2]
    report("A-2", ok2, f"A0: G(30)/G(6) = {a0[-1][1] / a0[0][1]:.3e}; 30 r(30)/(6 r(6)) = {30 * a0[-1][2] / (6 * a0[0][2]):.3e}")


# ---------------------------------------------------------------- (B)
PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)


def su2_from(a, scale):
    th = scale * np.linalg.norm(a, axis=-1)
    n = a / np.maximum(np.linalg.norm(a, axis=-1, keepdims=True), 1e-300)
    ns = np.einsum("...k,kij->...ij", n, PAULI)
    return np.cos(th)[..., None, None] * np.eye(2) + 1j * np.sin(th)[..., None, None] * ns


def haar_su2(rng, shape):
    q = rng.standard_normal(shape + (4,)); q /= np.linalg.norm(q, axis=-1, keepdims=True)
    ns = np.einsum("...k,kij->...ij", q[..., 1:], PAULI)
    return q[..., 0, None, None] * np.eye(2) + 1j * ns


def cov_lap(links, mu2):
    """links[n, n, 2, 2, 2] (x, y, direction, matrix). Operator on fields phi[n, n, 2], flattened (site*2 + colour)."""
    n = links.shape[0]
    idx = np.arange(n * n).reshape(n, n)
    rows, cols, vals = [], [], []
    for c in range(2):
        rows.append(2 * idx.ravel() + c); cols.append(2 * idx.ravel() + c); vals.append((4 + mu2) * np.ones(n * n, complex))
    for m in range(2):
        sh = (1, 0) if m == 0 else (0, 1)
        nb = np.roll(idx, shift=(-sh[0], -sh[1]), axis=(0, 1))
        Um = links[:, :, m]
        for a in range(2):
            for b in range(2):
                # -(U_m(x) phi(x+m))_a
                rows.append(2 * idx.ravel() + a); cols.append(2 * nb.ravel() + b); vals.append(-Um[:, :, a, b].ravel())
                # -(U_m(x-m)^dag phi(x-m))_a : row at nb (= x+m), column x, entry conj(U[b, a]) ... written from x+m side
                rows.append(2 * nb.ravel() + a); cols.append(2 * idx.ravel() + b); vals.append(-np.conj(Um[:, :, b, a]).ravel())
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * n * n, 2 * n * n))


def gauge_links(links, h):
    hp0 = np.roll(h, -1, axis=0); hp1 = np.roll(h, -1, axis=1)
    out = links.copy()
    hd = np.conj(np.swapaxes(h, -1, -2))
    out[:, :, 0] = hd @ links[:, :, 0] @ hp0
    out[:, :, 1] = hd @ links[:, :, 1] @ hp1
    return out


class BoxModelB:
    def __init__(self, links, frame, T=32, R=4, Mc=8, Tw=26, mu2=1.0):
        self.T, self.R, self.Mc, self.Tw = T, R, Mc, Tw
        self.links = links
        self.L = cov_lap(links, mu2).tocsc()
        self.boxes = []
        nb = T // R
        x, y = np.meshgrid(np.arange(T), np.arange(T), indexing="ij")
        for i in range(nb):
            for j in range(nb):
                a = (R * i, R * j)
                dx = dist_iv(x, a[0], a[0] + R - 1, T); dy = dist_iv(y, a[1], a[1] + R - 1, T)
                chi = ((dx == 0) & (dy == 0)).astype(float)  # sigma(d) at integer d: indicator
                psi = sig((dx - R / 2) / (R / 2)) * sig((dy - R / 2) / (R / 2))
                # frame region Omega: offsets 0..23, global = a - 10 + o
                W = 3 * R + 12
                og = np.arange(W)
                gx = (a[0] - (R + 6) + og) % T; gy = (a[1] - (R + 6) + og) % T
                g = np.zeros((W, W, 2, 2), complex)
                r0 = R + 6
                if frame:
                    g[r0, r0] = np.eye(2)
                    for o0 in range(r0, W - 1):
                        g[o0 + 1, r0] = np.conj(links[gx[o0], gy[r0], 0].T) @ g[o0, r0]
                    for o0 in range(r0, 0, -1):
                        g[o0 - 1, r0] = links[gx[o0 - 1], gy[r0], 0] @ g[o0, r0]
                    for o0 in range(W):
                        for o1 in range(r0, W - 1):
                            g[o0, o1 + 1] = np.conj(links[gx[o0], gy[o1], 1].T) @ g[o0, o1]
                        for o1 in range(r0, 0, -1):
                            g[o0, o1 - 1] = links[gx[o0], gy[o1 - 1], 1] @ g[o0, o1]
                else:
                    g[:, :] = np.eye(2)
                loc = np.zeros((Tw, Tw, 2, 2, 2), complex); loc[:] = np.eye(2)
                for m in range(2):
                    for o0 in range(W - (m == 0)):
                        for o1 in range(W - (m == 1)):
                            p0, p1 = (o0 + 1, o1) if m == 0 else (o0, o1 + 1)
                            Ug = links[gx[o0], gy[o1], m]
                            loc[o0, o1, m] = np.conj(g[o0, o1].T) @ Ug @ g[p0, p1]
                Lloc = cov_lap(loc, mu2).tocsc()
                lu = spla.splu(Lloc)
                psil = np.zeros((Tw, Tw)); psil[:W, :W] = psi[np.ix_(gx, gy)]
                Psil = sp.diags(np.repeat(psil.ravel(), 2))
                Cl = (Lloc @ Psil - Psil @ Lloc).tocsr()
                # inputs: box sites (chi = 1); P outputs: psi > 0; R outputs: d <= 5
                ins = [(o0, o1) for o0 in range(W) for o1 in range(W) if chi[gx[o0], gy[o1]] > 0]
                pouts = [(o0, o1) for o0 in range(W) for o1 in range(W) if psi[gx[o0], gy[o1]] > 0]
                routs = [(o0, o1) for o0 in range(W) for o1 in range(W)
                         if max(dx[gx[o0], gy[o1]], dy[gx[o0], gy[o1]]) <= R + 1]
                ncol = 2 * len(ins)
                F = np.zeros((2 * Tw * Tw, ncol), complex)
                for k, (o0, o1) in enumerate(ins):
                    gd = np.conj(g[o0, o1].T)  # frame source = g^dag y
                    for c in range(2):
                        F[2 * (o0 * Tw + o1):2 * (o0 * Tw + o1) + 2, 2 * k + c] = gd[:, c]
                Usol = lu.solve(F)
                Cu = Cl @ Usol
                Pm = np.zeros((2 * len(pouts), ncol), complex)
                for k, (o0, o1) in enumerate(pouts):
                    Pm[2 * k:2 * k + 2] = psil[o0, o1] * (g[o0, o1] @ Usol[2 * (o0 * Tw + o1):2 * (o0 * Tw + o1) + 2])
                Rm = np.zeros((2 * len(routs), ncol), complex)
                for k, (o0, o1) in enumerate(routs):
                    Rm[2 * k:2 * k + 2] = -(g[o0, o1] @ Cu[2 * (o0 * Tw + o1):2 * (o0 * Tw + o1) + 2])
                gidx = lambda lst: np.array([[2 * (gx[o0] * T + gy[o1]) + c for c in range(2)] for (o0, o1) in lst]).ravel()
                cube = ((a[0] // Mc) * (T // Mc) + (a[1] // Mc))
                self.boxes.append(dict(inp=gidx(ins), pout=gidx(pouts), rout=gidx(routs), P=Pm, R=Rm, cube=cube))

    def applyP(self, y, w=None):
        out = np.zeros_like(y)
        for bx in self.boxes:
            out[bx["pout"]] += bx["P"] @ y[bx["inp"]]
        return out

    def applyR(self, y):
        out = np.zeros_like(y)
        for bx in self.boxes:
            out[bx["rout"]] += bx["R"] @ y[bx["inp"]]
        return out


def cube_setup(T=32, Mc=8):
    nc = T // Mc
    x, y = np.meshgrid(np.arange(T), np.arange(T), indexing="ij")
    w0 = np.array([sig(dist_iv(np.arange(T), Mc * i, Mc * i + Mc - 1, T) / 2) for i in range(nc)])
    w0 = w0 / w0.sum(axis=0)
    eta = np.array([np.outer(w0[i], w0[j]).ravel() for i in range(nc) for j in range(nc)])  # (16, N)
    member = np.array([((x // Mc) * nc + (y // Mc)).ravel() == q for q in range(nc * nc)])
    bonds = []
    for qi in range(nc * nc):
        for qj in range(qi + 1, nc * nc):
            ai, bi = divmod(qi, nc); aj, bj = divmod(qj, nc)
            da = min((ai - aj) % nc, (aj - ai) % nc); db = min((bi - bj) % nc, (bj - bi) % nc)
            if max(da, db) == 1:
                bonds.append((qi, qj))
    return eta, member, bonds


def smat(svals, bonds, nq):
    S = np.eye(nq)
    for (q1, q2), s in zip(bonds, svals):
        S[q1, q2] = S[q2, q1] = s
    return S


def bond_energy(M, S, eta, member, j, lam, tol=1e-14):
    nq = S.shape[0]
    N2 = j.size
    eta2 = np.repeat(eta, 2, axis=1)  # (nq, 2N)

    def K(yc):  # yc (nq, 2N)
        z = S @ yc  # I(s)
        acc = z.copy(); w = z
        for _ in range(200):
            nw = np.zeros_like(w)
            for bx in M.boxes:
                rb = bx["R"] @ w[bx["cube"], bx["inp"]]
                for qp in np.nonzero(S[:, bx["cube"]])[0]:
                    nw[qp, bx["rout"]] += S[qp, bx["cube"]] * rb
            w = nw; acc += w
            if np.abs(w).max() <= 1e-17 * max(np.abs(acc).max(), 1e-300):
                break
        out = np.zeros_like(acc)
        for bx in M.boxes:
            pb = bx["P"] @ acc[bx["cube"], bx["inp"]]
            for qp in np.nonzero(S[:, bx["cube"]])[0]:
                out[qp, bx["pout"]] += S[qp, bx["cube"]] * pb
        return eta2 * out

    def nonlin(u):
        uu = u.reshape(-1, 2)
        return (lam * (np.abs(uu) ** 2).sum(axis=1, keepdims=True) * uu).ravel()

    A = np.zeros((nq, N2), complex)
    for it in range(100):
        views = S @ A
        yc = np.array([eta2[q] * (-j + nonlin(views[q])) for q in range(nq)])
        An = -K(yc)
        d = np.abs(An - A).max(); A = An
        if d <= tol * max(np.abs(A).max(), 1e-300):
            break
    views = S @ A
    E = 0.0
    for q in range(nq):
        mask2 = np.repeat(member[q], 2)
        u = views[q]
        uu = u.reshape(-1, 2)
        quart = ((np.abs(uu) ** 2).sum(axis=1) ** 2)[member[q]].sum()
        E += -0.5 * np.real(np.vdot(j[mask2], u[mask2])) - lam / 4 * quart
    return E, A, it


def part_B():
    print("== (B) frame covariance ==")
    rng = np.random.default_rng(SEED + 2)
    T, lam = 32, 0.05
    links = su2_from(rng.standard_normal((T, T, 2, 3)), 0.1)
    jv = (rng.standard_normal((T * T, 2)) + 1j * rng.standard_normal((T * T, 2))) * 0.3 / np.sqrt(2)
    j = jv.ravel()
    h = haar_su2(rng, (T, T))
    hl = h.reshape(-1, 2, 2)
    hd = np.conj(np.swapaxes(hl, -1, -2))
    act_hd = lambda v: np.einsum("sab,sb->sa", hd, v.reshape(-1, 2)).ravel()
    linksh = gauge_links(links, h)
    jh = act_hd(j)
    ys = [(rng.standard_normal(2 * T * T) + 1j * rng.standard_normal(2 * T * T)) for _ in range(4)]
    eta, member, bonds = cube_setup()
    svals = [rng.uniform(0, 1.2, len(bonds)) for _ in range(3)]
    q1, q2 = bonds[0]
    models = {}
    for frame in (True, False):
        for tag, lk in (("U", links), ("Uh", linksh)):
            t = time.time()
            models[(frame, tag)] = BoxModelB(lk, frame)
            print(f"  setup frame={frame} {tag}: {time.time() - t:.1f}s")
    # B-1
    worst = 0.0
    for key, M in models.items():
        for y in ys:
            res = M.L @ M.applyP(y) - (y - M.applyR(y))
            worst = max(worst, np.abs(res).max() / np.abs(y).max())
    report("B-1", worst <= 1e-10, f"max parametrix residual (frame & control, U & U^h) = {worst:.3e}")
    # B-2
    MU, MH = models[(True, "U")], models[(True, "Uh")]
    wp = wr = 0.0
    for bu, bh in zip(MU.boxes, MH.boxes):
        for y in ys:
            yb = y[bu["inp"]]
            yhb = act_hd(y)[bh["inp"]]
            Pu = np.zeros(2 * T * T, complex); Pu[bu["pout"]] = bu["P"] @ yb
            Ph = np.zeros(2 * T * T, complex); Ph[bh["pout"]] = bh["P"] @ yhb
            wp = max(wp, np.abs(Ph - act_hd(Pu)).max() / np.abs(Pu).max())
            Ru = np.zeros(2 * T * T, complex); Ru[bu["rout"]] = bu["R"] @ yb
            Rh = np.zeros(2 * T * T, complex); Rh[bh["rout"]] = bh["R"] @ yhb
            wr = max(wr, np.abs(Rh - act_hd(Ru)).max() / np.abs(Ru).max())
    report("B-2", max(wp, wr) <= 1e-10, f"covariance defect P_box {wp:.3e}, R_box {wr:.3e}")
    # B-3 walk inverse
    lu = spla.splu(MU.L)
    w3 = 0.0
    for y in ys:
        acc = y.copy(); w = y.copy()
        for _ in range(300):
            w = MU.applyR(w); acc += w
            if np.abs(w).max() < 1e-18 * np.abs(acc).max():
                break
        w3 = max(w3, np.abs(MU.applyP(acc) - lu.solve(y)).max() / np.abs(lu.solve(y)).max())
    report("B-3", w3 <= 1e-10, f"walk inverse vs L^-1, relative {w3:.3e}")
    # global solution and E(phi*) - E(0)
    phi = np.zeros_like(j)
    for _ in range(200):
        uu = phi.reshape(-1, 2)
        nl = (lam * (np.abs(uu) ** 2).sum(axis=1, keepdims=True) * uu).ravel()
        pn = lu.solve(j - nl)
        if np.abs(pn - phi).max() < 1e-16:
            phi = pn; break
        phi = pn
    uu = phi.reshape(-1, 2)
    Ephi = 0.5 * np.real(np.vdot(phi, MU.L @ phi)) + lam / 4 * ((np.abs(uu) ** 2).sum(axis=1) ** 2).sum() - np.real(np.vdot(j, phi))
    nq = len(eta)
    one = np.ones(len(bonds))
    out = {}
    for frame in (True, False):
        Mu, Mh = models[(frame, "U")], models[(frame, "Uh")]
        rows = []
        for sv in svals + [one]:
            S = smat(sv, bonds, nq)
            eu, _, itu = bond_energy(Mu, S, eta, member, j, lam)
            eh, _, ith = bond_energy(Mh, S, eta, member, jh, lam)
            rows.append((eu, eh))
        # two-cube polymer
        def RX(M, jj):
            vals = []
            for sb in (1.0, 0.0):
                sv = np.zeros(len(bonds)); sv[0] = sb
                S = smat(sv, bonds, nq)
                _, A, _ = bond_energy(M, S, eta, member, jj, lam)
                views = S @ A
                e = 0.0
                for q in (q1, q2):
                    mask2 = np.repeat(member[q], 2); u = views[q]; uu = u.reshape(-1, 2)
                    e += -0.5 * np.real(np.vdot(jj[mask2], u[mask2])) - lam / 4 * ((np.abs(uu) ** 2).sum(axis=1) ** 2)[member[q]].sum()
                vals.append(e)
            return vals[0] - vals[1]
        rxu, rxh = RX(Mu, j), RX(Mh, jh)
        out[frame] = (rows, rxu, rxh)
        print(f"  frame={frame}: dE(s) at U: " + ", ".join(f"{a:.10e}" for a, _ in rows)
              + f"; |dE(U^h)-dE(U)|: " + ", ".join(f"{abs(a - b):.2e}" for a, b in rows)
              + f"; R(X) = {rxu:.6e}, |dR| = {abs(rxu - rxh):.2e}")
    rows, rxu, rxh = out[True]
    inv = max(abs(a - b) / (1 + abs(a)) for a, b in rows)
    e1 = max(abs(out[f][0][-1][0] - (Ephi - 0.0)) / abs(Ephi) for f in (True, False))
    report("B-4", inv <= 1e-10 and e1 <= 1e-10, f"frame energy invariance {inv:.3e}; dE(1) vs E(phi*)-E(0) (both) {e1:.3e} (E = {Ephi:.10e})")
    report("B-5", abs(rxu - rxh) <= 1e-10 * (1 + abs(rxu)), f"frame two-cube polymer R(X) = {rxu:.6e}, defect {abs(rxu - rxh):.3e}")
    rows, rxu, rxh = out[False]
    ninv = max(abs(a - b) for a, b in rows[:-1])
    s1 = abs(rows[-1][0] - rows[-1][1]) / (1 + abs(rows[-1][0]))
    report("B-6", ninv >= 1e-6 and abs(rxu - rxh) >= 1e-8 and s1 <= 1e-10,
           f"control: max|dE(U^h)-dE(U)| at random s = {ninv:.3e}, |dR(X)| = {abs(rxu - rxh):.3e}, s=1 defect {s1:.3e}")


# ---------------------------------------------------------------- (C)
class SliceModel:
    def __init__(self, n, b=2):
        self.n, self.b = n, b
        ns = n * n; nl = 2 * ns
        self.ns, self.nl = ns, nl
        site = lambda x, y: (x % n) * n + (y % n)
        link = lambda x, y, m: 2 * site(x, y) + m
        self.site, self.link = site, link
        # d: sites -> links
        r, c, v = [], [], []
        for x in range(n):
            for y in range(n):
                for m in range(2):
                    xp, yp = (x + 1, y) if m == 0 else (x, y + 1)
                    r += [link(x, y, m)] * 2; c += [site(xp, yp), site(x, y)]; v += [1.0, -1.0]
        self.D = sp.csr_matrix((v, (r, c)), shape=(nl, ns))
        # curl
        r, c, v = [], [], []
        for x in range(n):
            for y in range(n):
                p = site(x, y)
                r += [p] * 4; c += [link(x, y, 0), link(x + 1, y, 1), link(x, y + 1, 0), link(x, y, 1)]; v += [1, 1, -1, -1]
        Kp = sp.csr_matrix((v, (r, c)), shape=(ns, nl))
        # root-to-root
        r, c, v = [], [], []
        k = 0
        for X0 in range(n // b):
            for X1 in range(n // b):
                for m in range(2):
                    cx, cy = b * X0, b * X1
                    for t in range(b):
                        px, py = (cx + t, cy) if m == 0 else (cx, cy + t)
                        r.append(k); c.append(link(px, py, m)); v.append(1.0)
                    k += 1
        Lam = sp.csr_matrix((v, (r, c)), shape=(k, nl))
        self.B = (Kp.T @ Kp + Lam.T @ Lam).tocsr()
        # tent slice
        r, c, v = [], [], []
        for x in range(n):
            for y in range(n):
                z = site(x, y)
                for X0 in range(n // b):
                    for X1 in range(n // b):
                        cx, cy = b * X0, b * X1
                        d0 = ((x - cx + n // 2) % n) - n // 2; d1 = ((y - cy + n // 2) % n) - n // 2
                        if abs(d0) >= b or abs(d1) >= b:
                            continue
                        chiX = (1 - abs(d0) / b) * (1 - abs(d1) / b)
                        for order in ((0, 1), (1, 0)):
                            px, py = cx, cy
                            for m in order:
                                dm = d0 if m == 0 else d1
                                for _ in range(abs(dm)):
                                    if dm > 0:
                                        r.append(z); c.append(link(px, py, m)); v.append(-0.5 * chiX)
                                        px, py = (px + 1, py) if m == 0 else (px, py + 1)
                                    else:
                                        px, py = (px - 1, py) if m == 0 else (px, py - 1)
                                        r.append(z); c.append(link(px, py, m)); v.append(+0.5 * chiX)
        self.Plam = sp.csr_matrix((v, (r, c)), shape=(ns, nl))
        self.Pi = (sp.identity(nl) + self.D @ self.Plam).tocsr()
        I = sp.identity(nl)
        A = self.Pi.T @ self.B @ self.Pi + (I - self.Pi).T @ (I - self.Pi)
        self.lu = spla.splu(A.tocsc())
        # link midpoints
        mx = np.zeros(nl); my = np.zeros(nl)
        for x in range(n):
            for y in range(n):
                for m in range(2):
                    l = link(x, y, m)
                    mx[l] = x + (0.5 if m == 0 else 0.0); my[l] = y + (0.5 if m == 1 else 0.0)
        self.mx, self.my = mx, my
        self.roots = np.array([site(b * X0, b * X1) for X0 in range(n // b) for X1 in range(n // b)])

    def slice_solve(self, yv):
        return self.Pi @ self.lu.solve(self.Pi.T @ yv)


def part_C():
    print("== (C) hard slice ==")
    rng = np.random.default_rng(SEED + 3)
    n, R, Tw = 60, 12, 56
    G = SliceModel(n); Lc = SliceModel(Tw)
    # C-1, C-2
    PP = G.Pi @ G.Pi - G.Pi
    c1a = np.abs(PP.data).max() if PP.nnz else 0.0
    c1b = c2 = 0.0
    for _ in range(3):
        lam = rng.standard_normal(G.ns); lam[G.roots] = 0.0
        dl = G.D @ lam
        c1b = max(c1b, np.abs(G.Pi @ dl).max() / np.abs(dl).max())
        c2 = max(c2, np.abs(G.B @ dl).max() / np.abs(dl).max())
    report("C-1", c1a <= 1e-12 and c1b <= 1e-12, f"max|Pi^2 - Pi| = {c1a:.3e}; max|Pi d lam|/max|d lam| = {c1b:.3e}")
    report("C-2", c2 <= 1e-12, f"max|B d lam|/max|d lam| = {c2:.3e}")
    nbx = n // R
    sh = 22

    def build(plateau, scale, use_pi=True):
        boxes = []
        for i in range(nbx):
            for jx in range(nbx):
                a0, a1 = R * i, R * jx
                d0 = dist_iv(G.mx, a0 - 0.5, a0 + R - 0.5, n); d1 = dist_iv(G.my, a1 - 0.5, a1 + R - 0.5, n)
                # chi partition: normalise over boxes per coordinate
                w0 = np.array([sig(dist_iv(G.mx, R * k - 0.5, R * k + R - 0.5, n)) for k in range(nbx)])
                w1 = np.array([sig(dist_iv(G.my, R * k - 0.5, R * k + R - 0.5, n)) for k in range(nbx)])
                chi = (sig(d0) / w0.sum(axis=0)) * (sig(d1) / w1.sum(axis=0))
                psi = sig((d0 - plateau) / scale) * sig((d1 - plateau) / scale)
                boxes.append(dict(a=(a0, a1), chi=chi, psi=psi))
        # global -> local link map (shift by sh - a, even)
        return boxes

    # precompute index maps
    gx = (np.arange(G.nl) // 2) // n; gy = (np.arange(G.nl) // 2) % n; gm = np.arange(G.nl) % 2

    def maps(a):
        lx = (gx - a[0] + sh) % n; ly = (gy - a[1] + sh) % n
        ok = (lx < Tw) & (ly < Tw)
        # only links whose distance to the box is <= 16 are transplanted (region inside the local torus, no wrap)
        d0 = dist_iv(G.mx, a[0] - 0.5, a[0] + R - 0.5, n); d1 = dist_iv(G.my, a[1] - 0.5, a[1] + R - 0.5, n)
        reg = ok & (np.maximum(d0, d1) <= 16)
        gl = np.nonzero(reg)[0]
        ll = 2 * (lx[gl] * Tw + ly[gl]) + gm[gl]
        return gl, ll

    def make_ops(plateau, scale, use_pi=True):
        boxes = build(plateau, scale)
        for bx in boxes:
            bx["gl"], bx["ll"] = maps(bx["a"])
            psil = np.zeros(Lc.nl); psil[bx["ll"]] = bx["psi"][bx["gl"]]
            bx["psil"] = psil

        def apply(y):
            Py = np.zeros(G.nl); Ry = np.zeros(G.nl)
            for bx in boxes:
                yt = np.zeros(Lc.nl); yt[bx["ll"]] = (bx["chi"] * y)[bx["gl"]]
                u = Lc.slice_solve(yt)
                cut = np.zeros(G.nl); cut[bx["gl"]] = (bx["psil"] * u)[bx["ll"]]
                Py += (G.Pi @ cut) if use_pi else cut
                C = Lc.B @ (bx["psil"] * u) - bx["psil"] * (Lc.B @ u)
                Ry[bx["gl"]] += -C[bx["ll"]]
            return Py, Ry
        return apply

    ys = [rng.standard_normal(G.nl) for _ in range(4)]
    apply = make_ops(R / 2, R / 2)
    c3 = c3s = 0.0
    for y in ys:
        Py, Ry = apply(y)
        c3 = max(c3, np.abs(G.Pi.T @ (G.B @ Py - (y - Ry))).max() / np.abs(y).max())
        c3s = max(c3s, np.abs(Py - G.Pi @ Py).max() / np.abs(Py).max())
    report("C-3", c3 <= 1e-10 and c3s <= 1e-12, f"slice identity residual {c3:.3e}; (1-Pi)P y {c3s:.3e}")
    y = ys[0]
    Rop = spla.LinearOperator((G.nl, G.nl), matvec=lambda v: v - apply(v)[1], dtype=float)
    z, info = spla.gmres(Rop, y, rtol=1e-13, atol=0.0, restart=200, maxiter=50)
    Pz, _ = apply(z)
    ug = G.slice_solve(y)
    c4 = np.abs(Pz - ug).max() / np.abs(ug).max()
    _, Rz = apply(z)
    print(f"  gmres info={info}, residual {np.abs(z - Rz - y).max():.3e}")
    report("C-4", c4 <= 1e-8, f"walk inverse vs slice inverse, relative {c4:.3e}")
    apply5 = make_ops(2.0, 10.0)
    c5 = 0.0
    for y in ys:
        Py, Ry = apply5(y)
        c5 = max(c5, np.abs(G.Pi.T @ (G.B @ Py - (y - Ry))).max() / np.abs(y).max())
    report("C-5", c5 >= 1e-6, f"small-plateau control: identity residual {c5:.3e} (predicted >= 1e-6)")
    apply6 = make_ops(R / 2, R / 2, use_pi=False)
    c6 = 0.0
    for yy in ys:
        Py, Ry = apply6(yy)
        c6 = max(c6, np.abs(G.Pi.T @ (G.B @ Py - (yy - Ry))).max() / np.abs(yy).max())
    P6z, _ = apply6(z)
    c6s = np.abs(P6z - G.Pi @ P6z).max() / np.abs(P6z).max()
    report("C-6", c6 <= 1e-10 and c6s >= 1e-6, f"no-Pi control: S-tested identity {c6:.3e}; (1-Pi)P'z relative {c6s:.3e}")


if __name__ == "__main__":
    part_A()
    print(f"  [t = {time.time() - T0:.1f}s]")
    part_C()
    print(f"  [t = {time.time() - T0:.1f}s]")
    part_B()
    print(f"  [t = {time.time() - T0:.1f}s]")
    allok = all(RESULTS.values()) and len(RESULTS) == 14
    print(f"VERDICT {'ALL PASS' if allok else 'NOT ALL PASS'} ({sum(RESULTS.values())}/{len(RESULTS)})")
