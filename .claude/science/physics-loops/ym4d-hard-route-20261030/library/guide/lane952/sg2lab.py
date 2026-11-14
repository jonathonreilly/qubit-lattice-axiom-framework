#!/usr/bin/env python3
"""lane952 (queue row 952, gap-sg2test-opus): GUIDE refutation test of (SG2) of row 950 (library/gap-sc-max.md 7.3-7.4).

SU(2) Wilson half-space slab in temporal gauge: slices t = 0..T, slice 0 frozen at the datum u, spatial plaquettes of
slice T at weight beta/2, temporal plaquettes <U_l(t), U_l(t+1)> at weight beta, spatial torus L^3. Links are unit
quaternions (w, x, y, z) = w + x i + y j + z k; <a, b> = Re(a b^*). First-step field E_l = Im(w_l u_l^*), w = slice 1.
Frame-only heat bath of row 950 7.4 (palindromic: parity 0, 1, 0), lagged moments E[X^(0) X^(n)].
Gauge-invariant proxies Y (functions of slices 1..T only) for Lemma LB of row 952 Section 1.3.
Compact U(1) variant with the same slab and observables (angles).
Written by Claude Opus 5.5 for row 952, rebuilt from row 950's text only (its scripts were not read).
GUIDE only: no statement of the proof chain rests on this code.
"""
import argparse, json, time, sys
import numpy as np

PI = np.pi

# ----------------------------------------------------------------------------------------------------------- quaternions
def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
                     a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
                     a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
                     a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0], axis=-1)

CONJ = np.array([1.0, -1.0, -1.0, -1.0])

def qc(a):
    return a * CONJ

def qexp_k(angle):
    """exp(angle k) as quaternion array, angle array."""
    angle = np.asarray(angle, dtype=float)
    out = np.zeros(angle.shape + (4,))
    out[..., 0] = np.cos(angle)
    out[..., 3] = np.sin(angle)
    return out

def sh(A, d, s):
    """value at x + s e_d; spatial axes are the three axes before the last one."""
    return np.roll(A, -s, axis=A.ndim - 4 + d)

def kp_a0(kappa, rng):
    """Kennedy-Pendleton: a0 with density prop. to sqrt(1-a0^2) exp(kappa a0) on [-1, 1]; kappa > 0 array."""
    out = np.empty(kappa.shape)
    flat_k = kappa.ravel()
    flat_o = out.ravel()
    todo = np.arange(flat_k.size)
    while todo.size:
        k = flat_k[todo]
        x1 = rng.random(todo.size); x2 = rng.random(todo.size); x3 = rng.random(todo.size); x4 = rng.random(todo.size)
        lam2 = -(np.log1p(-x1) + np.cos(2 * PI * x2) ** 2 * np.log1p(-x3)) / (2 * k)
        acc = x4 * x4 <= 1.0 - lam2
        flat_o[todo[acc]] = 1.0 - 2.0 * lam2[acc]
        todo = todo[~acc]
    return flat_o.reshape(kappa.shape)

def heatbath_su2(S, rng):
    """sample U with density prop. to exp(<U, S>) for staple array S (..., 4)."""
    kap = np.sqrt(np.sum(S * S, axis=-1))
    kap = np.maximum(kap, 1e-12)
    Sh = S / kap[..., None]
    a0 = kp_a0(kap, rng)
    v = rng.standard_normal(S.shape[:-1] + (3,))
    v /= np.sqrt(np.sum(v * v, axis=-1))[..., None]
    V = np.empty(S.shape)
    V[..., 0] = a0
    V[..., 1:] = v * np.sqrt(np.maximum(0.0, 1.0 - a0 * a0))[..., None]
    return qmul(V, Sh)

def random_su2(shape, rng):
    q = rng.standard_normal(shape + (4,))
    return q / np.sqrt(np.sum(q * q, axis=-1))[..., None]

# ----------------------------------------------------------------------------------------------------------- slices
def coords(L):
    x, y, z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
    return x, y, z

def eps_pattern(L):
    """tie mode of row 950 5.1: eps = (-1)^(x+y) on x-links, -(-1)^(x+y) on y-links, 0 on z-links."""
    x, y, z = coords(L)
    s = (-1.0) ** (x + y)
    return np.stack([s, -s, np.zeros_like(s)], axis=0)  # (3, L, L, L)

def eps_xyz(L):
    """tie mode of u_xyyz: (-1)^(x+y+z) (1, -1, 1) on (x, y, z) links."""
    x, y, z = coords(L)
    s_ = (-1.0) ** (x + y + z)
    return np.stack([s_, -s_, s_], axis=0)

def holonomy(Wd, d, L):
    """H(x) = w_d(x) w_d(x+d) ... w_d(x+(L-1)d)."""
    H = Wd.copy(); cur = Wd
    for _ in range(1, L):
        cur = sh(cur, d, 1)
        H = qmul(H, cur)
    return H

def proxy(W, L, plane, sgn, hdir):
    """gauge-invariant Y = sum_x c(x) Re(U_p(x) H(x)) / sqrt(L^3); plane (i, j), holonomy along hdir."""
    x, y, z = coords(L)
    c = (-1.0) ** (x + y) if sgn == "xy" else (-1.0) ** (x + y + z)
    i, j = plane
    Up = qmul(qmul(W[i], sh(W[j], i, 1)), qmul(qc(sh(W[i], j, 1)), qc(W[j])))
    H = holonomy(W[hdir], hdir, L)
    return float(np.sum(c * qmul(Up, H)[..., 0]) / np.sqrt(L ** 3))

def make_slice_su2(kind, L, phi=0.0, s=0.0, delta=0.0, vacfile=None):
    x, y, z = coords(L)
    u = np.zeros((3, L, L, L, 4)); u[..., 0] = 1.0
    if kind == "one":
        return u
    if kind in ("xy", "twist", "tilt", "interp", "pi", "pitwist", "xyyz", "xyyztwist", "xtwist"):
        u[1, ..., 0] = (-1.0) ** x                     # u_y = (-1)^x : flux -1 on xy plaquettes
    if kind in ("pi", "pitwist"):
        u[2, ..., 0] = (-1.0) ** (x + y)               # u_z = (-1)^(x+y): flux -1 on xz and yz too
    if kind in ("xyyz", "xyyztwist"):                  # u_z = (-1)^y: flux -1 on xy and yz, +1 on xz
        u[2, ..., 0] = (-1.0) ** y
    if kind == "xyyztwist":
        u[2] = qmul(u[2], qexp_k(np.full((L, L, L), phi / L)))
    if kind == "xtwist":                               # flat colour twist along x on u_xy
        u[0] = qexp_k(np.full((L, L, L), phi / L))
    if kind == "twist":                                # flat colour twist along z: z-links exp(delta k), delta = phi/L
        u[2] = qexp_k(np.full((L, L, L), phi / L))
    if kind == "pitwist":
        u[2] = qmul(u[2], qexp_k(np.full((L, L, L), phi / L)))
    if kind == "tilt":                                 # row 950 7.5 tilt along the pattern in colour 3
        e = eps_pattern(L)
        for i in (0, 1):
            u[i] = qmul(u[i], qexp_k(delta * e[i]))
    if kind == "interp":                               # u_xy (s=0) -> u_pi (s=1) via z-links exp(s pi [x+y odd] k)
        odd = ((x + y) % 2).astype(float)
        u[2] = qexp_k(s * PI * odd)
        if phi != 0.0:
            u[2] = qmul(u[2], qexp_k(np.full((L, L, L), phi / L)))
    if kind == "vac":
        u = np.load(vacfile)
    return u

def plaquettes(U):
    """Re of the three plaquette orientations of a slice U (3, L, L, L, 4): returns dict plane -> array."""
    out = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        P = qmul(qmul(U[i], sh(U[j], i, 1)), qmul(qc(sh(U[i], j, 1)), qc(U[j])))
        out[(i, j)] = P
    return out

# ----------------------------------------------------------------------------------------------------------- slab SU(2)
class SlabSU2:
    def __init__(self, u, beta, T, rng, start="cold", free_bottom=False):
        self.L = u.shape[1]; self.T = T; self.beta = beta; self.rng = rng
        self.free_bottom = free_bottom
        L = self.L
        self.U = np.empty((T + 1, 3, L, L, L, 4))
        for t in range(T + 1):
            self.U[t] = u
        if start == "hot":
            self.U[1:] = random_su2((T, 3, L, L, L), rng)
            if free_bottom:
                self.U[0] = random_su2((3, L, L, L), rng)
        x, y, z = coords(L)
        par = (x + y + z) % 2
        tt = np.arange(T + 1)[:, None, None, None]
        self.mask = [((par[None] + tt) % 2 == p) for p in (0, 1)]   # (T+1, L, L, L)
        t0 = 0 if free_bottom else 1
        for p in (0, 1):
            self.mask[p][:t0] = False
        w = np.full(T + 1, beta)
        w[T] = beta / 2
        if free_bottom:
            w[0] = beta / 2
        self.wsp = w[:, None, None, None, None]

    def staple(self, i):
        U = self.U; T = self.T; b = self.beta
        Ui = U[:, i]
        S = np.zeros_like(Ui)
        for j in range(3):
            if j == i:
                continue
            Uj = U[:, j]
            up = qmul(qmul(Uj, sh(Ui, j, 1)), qc(sh(Uj, i, 1)))
            Ujm = sh(Uj, j, -1)
            dn = qmul(qmul(qc(Ujm), sh(Ui, j, -1)), sh(Ujm, i, 1))
            S += up + dn
        S *= self.wsp
        S[1:] += b * Ui[:-1]          # temporal plaquette with slice t-1
        S[:-1] += b * Ui[1:]          # temporal plaquette with slice t+1
        return S

    def sweep(self):
        for i in range(3):
            for p in (0, 1):
                S = self.staple(i)
                m = self.mask[p]
                self.U[:, i][m] = heatbath_su2(S[m], self.rng)

    def E1(self, u):
        """first-step field Im(w u^*) of slice 1: (3, L, L, L, 3)."""
        return qmul(self.U[1], qc(u))[..., 1:]

# ----------------------------------------------------------------------------------------------------------- frame chain
def frame_staple(g, u, w):
    """F_x = sum_i [u_i(x) g_(x+i) w_i(x)^* + u_i(x-i)^* g_(x-i) w_i(x-i)]; weight exp(beta <g_x, F_x>)."""
    F = np.zeros_like(g)
    for i in range(3):
        F += qmul(qmul(u[i], sh(g, i, 1)), qc(w[i]))
        um = sh(u[i], i, -1); wm = sh(w[i], i, -1)
        F += qmul(qmul(qc(um), sh(g, i, -1)), wm)
    return F

def act(g, w):
    """(g.w)_l = g_x w_l g_(x+i)^*."""
    return np.stack([qmul(qmul(g, w[i]), qc(sh(g, i, 1))) for i in range(3)], axis=0)

def frame_chain(u, w, beta, lags, rng, keep_full=()):
    """run the palindromic frame heat bath from g = 1; return E^(n) mode data at each lag in lags (sorted)."""
    L = u.shape[1]
    g = np.zeros((L, L, L, 4)); g[..., 0] = 1.0
    x, y, z = coords(L)
    par = (x + y + z) % 2
    masks = [par == 0, par == 1]
    out = {}
    n = 0
    for target in lags:
        while n < target:
            for p in (0, 1, 0):
                F = beta * frame_staple(g, u, w)
                m = masks[p]
                g[m] = heatbath_su2(F[m], rng)
            n += 1
        out[target] = qmul(act(g, w), qc(u))[..., 1:]
    return out

# ----------------------------------------------------------------------------------------------------------- proxies
def zholonomy(Wz, L):
    H = Wz.copy()
    cur = Wz
    for _ in range(1, L):
        cur = sh(cur, 2, 1)
        H = qmul(H, cur)
    return H

# ----------------------------------------------------------------------------------------------------------- U(1)
class SlabU1:
    def __init__(self, u, beta, T, rng, start="cold"):
        self.L = u.shape[1]; self.T = T; self.beta = beta; self.rng = rng
        L = self.L
        self.A = np.empty((T + 1, 3, L, L, L))
        for t in range(T + 1):
            self.A[t] = u
        if start == "hot":
            self.A[1:] = rng.uniform(-PI, PI, (T, 3, L, L, L))
        x, y, z = coords(L)
        par = (x + y + z) % 2
        tt = np.arange(T + 1)[:, None, None, None]
        self.mask = [((par[None] + tt) % 2 == p) for p in (0, 1)]
        for p in (0, 1):
            self.mask[p][:1] = False
        w = np.full(T + 1, beta); w[T] = beta / 2
        self.wsp = w[:, None, None, None]

    def staple(self, i):
        A = self.A
        Ai = A[:, i]
        S = np.zeros(Ai.shape, dtype=complex)
        for j in range(3):
            if j == i:
                continue
            Aj = A[:, j]
            # plaquette (i,j) at x: A_i(x) + A_j(x+i) - A_i(x+j) - A_j(x); staple phase = A_j(x) + A_i(x+j) - A_j(x+i)
            up = Aj + sh1(Ai, j, 1) - sh1(Aj, i, 1)
            Ajm = sh1(Aj, j, -1)
            dn = -Ajm + sh1(Ai, j, -1) + sh1(Ajm, i, 1)
            S += np.exp(1j * up) + np.exp(1j * dn)
        S *= self.wsp
        S[1:] += self.beta * np.exp(1j * Ai[:-1])
        S[:-1] += self.beta * np.exp(1j * Ai[1:])
        return S

    def sweep(self):
        for i in range(3):
            for p in (0, 1):
                S = self.staple(i)
                m = self.mask[p]
                Sm = S[m]
                self.A[:, i][m] = self.rng.vonmises(np.angle(Sm), np.abs(Sm))

def sh1(A, d, s):
    return np.roll(A, -s, axis=A.ndim - 3 + d)

def frame_chain_u1(u, w, beta, lags, rng):
    L = u.shape[1]
    g = np.zeros((L, L, L))
    x, y, z = coords(L)
    par = (x + y + z) % 2
    masks = [par == 0, par == 1]
    out = {}
    n = 0
    for target in lags:
        while n < target:
            for p in (0, 1, 0):
                # weight exp(beta sum_l cos(u_l - g_x - w_l + g_(x+i)))
                F = np.zeros((L, L, L), dtype=complex)
                for i in range(3):
                    F += np.exp(1j * (u[i] - w[i] + sh1(g, i, 1)))           # cos(g_x - (u - w + g_(x+i)))
                    F += np.exp(1j * (sh1(w[i], i, -1) - sh1(u[i], i, -1) + sh1(g, i, -1)))
                F *= beta
                m = masks[p]
                g[m] = rng.vonmises(np.angle(F[m]), np.abs(F[m]))
            n += 1
        gw = np.stack([g + w[i] - sh1(g, i, 1) for i in range(3)], axis=0)
        out[target] = np.sin(gw - u)
    return out

# ----------------------------------------------------------------------------------------------------------- statistics
def blocks_mean(a, nb=8):
    a = np.asarray(a, dtype=float)
    n = (len(a) // nb) * nb
    if n == 0:
        return float(np.mean(a)) if len(a) else float("nan"), float("nan")
    b = a[:n].reshape(nb, -1).mean(axis=1)
    return float(b.mean()), float(b.std(ddof=1) / np.sqrt(nb))

def lb_split(Y, X):
    """Lemma LB with one regressor, raw moments (symmetric case): E_A[YX] E_B[YX] / E[Y^2], halves A, B."""
    Y = np.asarray(Y); X = np.asarray(X)
    n = len(Y) // 2
    a = np.mean(Y[:n] * X[:n]); b = np.mean(Y[n:2 * n] * X[n:2 * n])
    return float(a * b / np.mean(Y * Y)), float(np.mean(Y * X) ** 2 / np.mean(Y * Y))

# ----------------------------------------------------------------------------------------------------------- driver
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", default="su2")
    ap.add_argument("--slice", default="one")
    ap.add_argument("--phi", type=float, default=0.0)
    ap.add_argument("--s", type=float, default=0.0)
    ap.add_argument("--delta", type=float, default=0.0)
    ap.add_argument("--vacfile", default=None)
    ap.add_argument("--beta", type=float, default=2.3)
    ap.add_argument("--L", type=int, default=4)
    ap.add_argument("--T", type=int, default=6)
    ap.add_argument("--start", default="cold")
    ap.add_argument("--therm", type=int, default=500)
    ap.add_argument("--meas", type=int, default=2000)
    ap.add_argument("--every", type=int, default=1)
    ap.add_argument("--fevery", type=int, default=0, help="run a frame chain every fevery measurements (0: never)")
    ap.add_argument("--lags", default="0,1,2,4,8,16,32,64")
    ap.add_argument("--pca", type=int, default=0, help="1: keep full E^(0), E^(nmax) for split-sample PCA")
    ap.add_argument("--mode", default="xy", help="tie vector: xy (row 950) or xyz (u_xyyz)")
    ap.add_argument("--yplane", default="01")
    ap.add_argument("--ysign", default="xy")
    ap.add_argument("--ydir", type=int, default=2)
    ap.add_argument("--pca3", type=int, default=0, help="1: raw-moment PCA of the e_3 components of lim C_n")
    ap.add_argument("--raw", type=int, default=0, help="1: PCA with raw moments (symmetric slices)")
    ap.add_argument("--genvac", type=int, default=0, help="1: generate a vacuum slice from a free slab of T slices, save to --vacfile")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    L = a.L
    lags = sorted(set(int(v) for v in a.lags.split(",")))
    if a.mode == "xyz":
        eps = eps_xyz(L); norm = np.sqrt(3.0 * L ** 3)
    else:
        eps = eps_pattern(L); norm = np.sqrt(2.0 * L ** 3)
    t0 = time.time()
    res = {"args": vars(a)}
    if a.genvac:
        u0 = make_slice_su2("one", L)
        slab = SlabSU2(u0, a.beta, a.T, rng, start="hot", free_bottom=True)
        for _ in range(a.therm):
            slab.sweep()
        uv = slab.U[a.T // 2].copy()
        np.save(a.vacfile, uv)
        pl = plaquettes(uv)
        res["vac_plaq"] = {f"{k[0]}{k[1]}": float(np.mean(v[..., 0])) for k, v in pl.items()}
        res["seconds"] = time.time() - t0
        json.dump(res, open(a.out, "w"), indent=1); print(res); return
    if a.group == "su2":
        u = make_slice_su2(a.slice, L, phi=a.phi, s=a.s, delta=a.delta, vacfile=a.vacfile)
        pl = plaquettes(u)
        res["slice_plaq_re_mean"] = {f"{k[0]}{k[1]}": float(np.mean(v[..., 0])) for k, v in pl.items()}
        slab = SlabSU2(u, a.beta, a.T, rng, start=a.start)
        for _ in range(a.therm):
            slab.sweep()
        res["t_therm"] = time.time() - t0
        X0 = []; Y1 = []; Y2 = []; varc = []; Lam = np.zeros((L, L, L, 3, 3))
        lagX = {n: [] for n in lags}; lagX0 = []
        fullE0 = []; fullEn = []
        nmeas = 0
        for m in range(a.meas):
            for _ in range(a.every):
                slab.sweep()
            E = slab.E1(u)                               # (3, L, L, L, 3)
            Xa = np.einsum("ixyz,ixyza->a", eps, E) / norm
            X0.append(Xa)
            varc.append(float(np.mean(E * E)))
            Ek = np.fft.fftn(E, axes=(1, 2, 3))          # (3 dir, kx, ky, kz, 3 colour)
            Lam += np.einsum("ixyza,jxyza->xyzij", Ek, np.conj(Ek)).real
            if a.slice != "one" and a.slice != "vac":
                pln = (int(a.yplane[0]), int(a.yplane[1]))
                Y1.append(proxy(slab.U[1], L, pln, a.ysign, a.ydir))
                Y2.append(proxy(slab.U[2], L, pln, a.ysign, a.ydir))
            if a.fevery and (m % a.fevery == 0):
                fc = frame_chain(u, slab.U[1], a.beta, lags, rng)
                for n in lags:
                    lagX[n].append(np.einsum("ixyz,ixyza->a", eps, fc[n]) / norm)
                lagX0.append(Xa)
                if a.pca:
                    fullE0.append(E.ravel().copy()); fullEn.append(fc[lags[-1]].ravel().copy())
                if a.pca3:
                    fullE0.append(E[..., 2].ravel().copy()); fullEn.append(fc[lags[-1]][..., 2].ravel().copy())
            nmeas += 1
        X0 = np.array(X0)
        res["n_meas"] = nmeas
        res["percomp_var"] = blocks_mean(varc)
        Lam /= (3.0 * L ** 3 * nmeas)
        ev = np.linalg.eigvalsh(Lam)[..., -1]
        kmax = np.unravel_index(np.argmax(ev), ev.shape)
        res["lambda_max_k"] = float(ev.max()); res["k_of_max"] = [int(v) for v in kmax]
        res["lambda_k0"] = float(ev[0, 0, 0])
        # tie mode, temporal gauge: raw second moments per colour, and lambda_* = colour mean
        res["X0_raw2"] = [blocks_mean(X0[:, c] ** 2) for c in range(3)]
        res["X0_mean"] = [blocks_mean(X0[:, c]) for c in range(3)]
        res["lambda_star"] = blocks_mean(np.mean(X0 ** 2, axis=1))
        if Y1:
            Y1 = np.array(Y1); Y2 = np.array(Y2)
            res["Y1_mean"] = blocks_mean(Y1); res["Y1_raw2"] = blocks_mean(Y1 ** 2)
            res["Y1X3"] = blocks_mean(Y1 * X0[:, 2])
            res["LB_split_Y1"], res["LB_full_Y1"] = lb_split(Y1, X0[:, 2])
            # two regressors (Y1, Y2): c^T G^-1 c with raw moments
            Ym = np.stack([Y1, Y2], axis=1)
            G = Ym.T @ Ym / len(Y1); c = Ym.T @ X0[:, 2] / len(Y1)
            res["LB_Y1Y2"] = float(c @ np.linalg.solve(G, c))
        if lagX0:
            lagX0 = np.array(lagX0)
            res["n_frame"] = len(lagX0)
            for c in range(3):
                res[f"lag_X{c+1}"] = {str(n): blocks_mean(lagX0[:, c] * np.array(lagX[n])[:, c]) for n in lags}
            if (a.pca or a.pca3) and len(fullE0) >= 16:
                E0 = np.array(fullE0); En = np.array(fullEn)
                h = len(E0) // 2
                ctr = (lambda A: A) if (a.raw or a.pca3) else (lambda A: A - A.mean(0))
                def topvec(A0, An):
                    C = ctr(A0).T @ ctr(An) / len(A0)
                    C = 0.5 * (C + C.T)
                    w_, V_ = np.linalg.eigh(C)
                    return w_[-1], V_[:, -1]
                lamA, vA = topvec(E0[:h], En[:h])
                lamB, vB = topvec(E0[h:], En[h:])
                def quad(v, A0, An):
                    return float(np.mean((ctr(A0) @ v) * (ctr(An) @ v)))
                res["pca_insample_top"] = [float(lamA), float(lamB)]
                res["pca_split_top"] = [quad(vA, E0[h:], En[h:]), quad(vB, E0[:h], En[:h])]
                # top vector of the lag-0 covariance (temporal gauge) for reference
                C0 = ctr(E0).T @ ctr(E0) / len(E0)
                res["pca_C0_top_insample"] = float(np.linalg.eigvalsh(C0)[-1])
    else:
        x, y, z = coords(L)
        u = np.zeros((3, L, L, L))
        if a.slice in ("xy",):
            u[1] = PI * (x % 2)
        slab = SlabU1(u, a.beta, a.T, rng, start=a.start)
        for _ in range(a.therm):
            slab.sweep()
        X0 = []; Ys = []; lagX = {n: [] for n in lags}; lagX0 = []
        for m in range(a.meas):
            for _ in range(a.every):
                slab.sweep()
            E = np.sin(slab.A[1] - u)
            Xv = float(np.sum(eps * E) / norm)
            X0.append(Xv)
            W = slab.A[1]
            thp = W[0] + sh1(W[1], 0, 1) - sh1(W[0], 1, 1) - W[1]
            Ys.append(float(np.sum(((-1.0) ** (x + y)) * np.sin(thp)) / np.sqrt(L ** 3)))
            if a.fevery and (m % a.fevery == 0):
                fc = frame_chain_u1(u, slab.A[1], a.beta, lags, rng)
                for n in lags:
                    lagX[n].append(float(np.sum(eps * fc[n]) / norm))
                lagX0.append(Xv)
        X0 = np.array(X0); Ys = np.array(Ys)
        res["n_meas"] = len(X0)
        res["X0_raw2"] = blocks_mean(X0 ** 2); res["X0_mean"] = blocks_mean(X0)
        res["Y_raw2"] = blocks_mean(Ys ** 2); res["YX"] = blocks_mean(Ys * X0)
        res["LB_split_Y"], res["LB_full_Y"] = lb_split(Ys, X0)
        if lagX0:
            lagX0 = np.array(lagX0)
            res["n_frame"] = len(lagX0)
            res["lag_X"] = {str(n): blocks_mean(lagX0 * np.array(lagX[n])) for n in lags}
    res["seconds"] = time.time() - t0
    with open(a.out, "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: res[k] for k in res if k not in ("args",)}, indent=None)[:3000])

if __name__ == "__main__":
    main()
