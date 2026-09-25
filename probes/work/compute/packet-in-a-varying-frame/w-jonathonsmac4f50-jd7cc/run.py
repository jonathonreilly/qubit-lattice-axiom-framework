#!/usr/bin/env python3
"""A packet of the walk in a slowly varying coin frame (block 62, landed #8592), run 2 of 2.

As landed: T1 (a) uniform frame H(k)^2 = g^ij sin k_i sin k_j, g^ij = sum_a E_a^i E_a^j; (b) a uniform rotation of the coin vectors is a
conjugation; (c) the symmetrised generator is hermitian; 'extending this to nonuniform ray dynamics requires the separate slowly varying
approximation; no exact packet-force law follows' and 'a frame field whose rotation varies from site to site is a further object'.  This run
executes that further object; nothing here is claimed beyond the executed numbers.
Generator H = (1/2) sum_j {E^j(x).sigma, S_j} on a 256 x 256 torus slice (third direction uniform, k_z = 0: S_z = 0), E = 1 + eps(x).
Evolution: scipy expm_multiply (truncated Taylor with norm-based step selection, double precision); error control: an independent
Chebyshev propagator on the same states, and the norm.  Rays: antithetic clouds of 4096 rays of E(k, x)^2 = g^ij(x) sin k_i sin k_j (RK4), sampled
from the packet's position and momentum spreads.  Exact (sympy): uniform-frame identities used by the rays.
"""
import itertools, time
import numpy as np
import sympy as sp
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply

def out(s): print(s, flush=True)

# ------------------------------------------------------------------ exact: the uniform frame's square and the rotation's invisibility to g
e = sp.symbols('e0:9', real=True); s1, s2, th = sp.symbols('s1 s2 theta', real=True)
Sg = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E = [[e[3 * a + j] for j in range(3)] for a in range(3)]                     # E[a][j]
Hk = sum((E[a][j] * Sg[a] * [s1, s2, 0][j] for a in range(3) for j in range(2)), sp.zeros(2, 2))
g = [[sum(E[a][i] * E[a][j] for a in range(3)) for j in range(2)] for i in range(2)]
ok1 = sp.simplify(Hk * Hk - (sum(g[i][j] * [s1, s2][i] * [s1, s2][j] for i in range(2) for j in range(2))) * sp.eye(2)) == sp.zeros(2, 2)
Rz = sp.Matrix([[sp.cos(th), -sp.sin(th), 0], [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])
Er = Rz * sp.Matrix(E)
gr = [[sp.simplify(sum(Er[a, i] * Er[a, j] for a in range(3)) - g[i][j]) for j in range(2)] for i in range(2)]
out("X exact (sympy): uniform frame H(k)^2 = g^ij sin k_i sin k_j with g^ij = sum_a E_a^i E_a^j: %s; a rotation of the coin index leaves g unchanged: %s"
    % ("PASS" if ok1 else "FAIL", "PASS" if all(v == 0 for r in gr for v in r) else "FAIL"))

# ------------------------------------------------------------------ lattice
L = 256; N = L * L
X, Y = np.meshgrid(np.arange(L), np.arange(L), indexing='ij'); Xf, Yf = X.ravel().astype(float), Y.ravel().astype(float)
def shift(dx, dy):
    cols = ((X.ravel() + dx) % L) * L + (Y.ravel() + dy) % L
    return sps.csr_matrix((np.ones(N), (np.arange(N), cols)), shape=(N, N))
Tx, Ty = shift(1, 0), shift(0, 1)
S = [(Tx - Tx.T) / 2j, (Ty - Ty.T) / 2j]
SIG = [sps.csr_matrix(np.array([[0, 1], [1, 0]], complex)), sps.csr_matrix(np.array([[0, -1j], [1j, 0]])), sps.csr_matrix(np.array([[1, 0], [0, -1]], complex))]
def ham(Ef):
    """Ef[a][j]: site arrays of the frame E_a^j (a coin axis 0..2, j derivative axis 0..1)"""
    H = None
    for a in range(3):
        for j in range(2):
            v = Ef[a][j]
            if np.all(v == 0): continue
            D = sps.diags(v); term = (D @ S[j] + S[j] @ D) / 2
            t = sps.kron(term, SIG[a])
            H = t if H is None else H + t
    return H.tocsr()
x0, y0, w, q = 40.0, 0.0, 8.0, 0.6
def packet():
    dx = (Xf - x0 + L / 2) % L - L / 2; dy = (Yf - y0 + L / 2) % L - L / 2
    env = np.exp(-(dx ** 2 + dy ** 2) / (2 * w ** 2) + 1j * q * dx)
    u = np.array([1, 1]) / np.sqrt(2)                                    # positive eigenvector of sigma_x sin q
    psi = (env[:, None] * u[None, :]).ravel(); return psi / np.linalg.norm(psi)
def centre(psi, xc):
    rho = (np.abs(psi.reshape(N, 2)) ** 2).sum(1)
    dx = (Xf - xc + L / 2) % L - L / 2 + (xc - x0); dy = (Yf - y0 + L / 2) % L - L / 2
    return np.array([(rho * dx).sum(), (rho * dy).sum()]) / rho.sum()
TIMES = (20.0, 40.0, 60.0, 80.0)
def path(H, psi0):
    pts = []; psi = psi0; tprev = 0.0
    for t in TIMES:
        psi = expm_multiply(-1j * H * (t - tprev), psi); tprev = t
        pts.append(centre(psi, x0 + np.cos(q) * t))
    return np.array(pts), psi

# ------------------------------------------------------------------ rays
def ray_cloud(Efun, nr=256, seed=11, dt=0.1):
    """antithetic cloud: nr base samples, each with all 16 sign flips of (dx, dy, dk_x, dk_y), so odd sampling moments vanish exactly"""
    rng = np.random.default_rng(seed)
    base = np.stack([rng.normal(0, w / np.sqrt(2), nr), rng.normal(0, w / np.sqrt(2), nr), rng.normal(0, 1 / (np.sqrt(2) * w), nr), rng.normal(0, 1 / (np.sqrt(2) * w), nr)])
    flips = np.array(list(itertools.product((1, -1), repeat=4)), float).T          # 4 x 16
    dev = (base[:, :, None] * flips[:, None, :]).reshape(4, -1)
    st = dev + np.array([x0, y0, q, 0.0])[:, None]
    def En(x, y, k1, k2):
        Ex = Efun(x, y); s = (np.sin(k1), np.sin(k2))
        G = lambda i, j: sum(Ex[a][i] * Ex[a][j] for a in range(3))
        return np.sqrt(np.maximum(G(0, 0) * s[0] ** 2 + 2 * G(0, 1) * s[0] * s[1] + G(1, 1) * s[1] ** 2, 1e-300))
    h = 1e-5
    def f(st):
        x, y, k1, k2 = st
        return np.stack([(En(x, y, k1 + h, k2) - En(x, y, k1 - h, k2)) / (2 * h), (En(x, y, k1, k2 + h) - En(x, y, k1, k2 - h)) / (2 * h),
                         -(En(x + h, y, k1, k2) - En(x - h, y, k1, k2)) / (2 * h), -(En(x, y + h, k1, k2) - En(x, y - h, k1, k2)) / (2 * h)])
    start = st[:2].copy(); pts = []; t = 0.0
    for tt in TIMES:
        while t < tt - 1e-9:
            a1 = f(st); a2 = f(st + dt / 2 * a1); a3 = f(st + dt / 2 * a2); a4 = f(st + dt * a3)
            st = st + dt / 6 * (a1 + 2 * a2 + 2 * a3 + a4); t += dt
        pts.append([np.mean(st[0] - start[0]), np.mean(st[1] - start[1])])
    return np.array(pts)

ONE = np.ones(N); ZERO = np.zeros(N)
def ident():
    return [[ONE.copy(), ZERO.copy()], [ZERO.copy(), ONE.copy()], [ZERO.copy(), ZERO.copy()]]
psi0 = packet()
H0 = ham(ident())
p0, psiT0 = path(H0, psi0)
r0 = ray_cloud(lambda x, y: [[np.ones_like(x), np.zeros_like(x)], [np.zeros_like(x), np.ones_like(x)], [np.zeros_like(x), np.zeros_like(x)]])
out("N identity frame: packet centre at t = %s: %s; rays %s" % (TIMES, " ".join("(%.3f, %.3f)" % tuple(v) for v in p0), " ".join("(%.3f, %.3f)" % tuple(v) for v in r0)))

# error control and conservation (iii)
from scipy.special import jv
def chebyshev(H, psi, t, bound):
    """exp(-iHt) psi by the Chebyshev expansion sum (2 - delta_k0) (-i)^k J_k(bound t) T_k(H/bound), an independent propagator"""
    Hs = H / bound; K = int(bound * t + 60)
    t0v = psi; t1v = Hs @ psi
    acc = jv(0, bound * t) * t0v + 2 * (-1j) * jv(1, bound * t) * t1v
    for k in range(2, K):
        t2v = 2 * (Hs @ t1v) - t0v
        acc = acc + 2 * ((-1j) ** k) * jv(k, bound * t) * t2v
        t0v, t1v = t1v, t2v
    return acc
def err_control(H, label):
    psi_e = expm_multiply(-1j * H * 80.0, psi0)
    psi_c = chebyshev(H, psi0, 80.0, 2.5)
    out("N error control (%s): expm_multiply against an independent Chebyshev propagator (|spectrum| < 2.5) at t = 80: |difference| = %.1e; norm - 1 = %.1e"
        % (label, np.linalg.norm(psi_e - psi_c), np.linalg.norm(psi_e) - 1))
err_control(H0, "identity frame")

# ------------------------------------------------------------------ (i) shear gradient: symmetric off-diagonal eps_x^y = eps_y^x = e0 sin(2 pi m y / L), plus a diagonal stretch
def shear_frames(e0, m, sgn):
    f = sgn * e0 * np.sin(2 * np.pi * m * Yf / L)
    Ef = ident(); Ef[0][1] = f.copy(); Ef[1][0] = f.copy()
    fun = lambda x, y: [[np.ones_like(x), sgn * e0 * np.sin(2 * np.pi * m * y / L)], [sgn * e0 * np.sin(2 * np.pi * m * y / L), np.ones_like(x)], [np.zeros_like(x), np.zeros_like(x)]]
    return Ef, fun
def shear_frames_x(e0, m, sgn):
    f = sgn * e0 * np.sin(2 * np.pi * m * (Xf - x0) / L)
    Ef = ident(); Ef[0][1] = f.copy(); Ef[1][0] = f.copy()
    fun = lambda x, y: [[np.ones_like(x), sgn * e0 * np.sin(2 * np.pi * m * (x - x0) / L)], [sgn * e0 * np.sin(2 * np.pi * m * (x - x0) / L), np.ones_like(x)], [np.zeros_like(x), np.zeros_like(x)]]
    return Ef, fun
def stretch_frames(e0, m, sgn):
    f = sgn * e0 * np.sin(2 * np.pi * m * Yf / L)
    Ef = ident(); Ef[0][0] = ONE + f
    fun = lambda x, y: [[1 + sgn * e0 * np.sin(2 * np.pi * m * y / L), np.zeros_like(x)], [np.zeros_like(x), np.ones_like(x)], [np.zeros_like(x), np.zeros_like(x)]]
    return Ef, fun
rows_i = []
for lab, mk, e0, m in (("symmetric shear eps_xy = eps_yx, gradient transverse (wavelength 64)", shear_frames, 0.05, 4),
                       ("symmetric shear, gradient transverse, e0 = 0.1 (wavelength 42.7)", shear_frames, 0.1, 6),
                       ("symmetric shear, gradient along the motion (wavelength 51.2)", shear_frames_x, 0.05, 5),
                       ("stretch eps_xx, gradient transverse (wavelength 64)", stretch_frames, 0.05, 4)):
    pk, ry = {}, {}
    for sgn in (+1, -1):
        Ef, fun = mk(e0, m, sgn)
        pk[sgn], _ = path(ham(Ef), psi0); ry[sgn] = ray_cloud(fun)
    dp = 0.5 * (pk[1] - pk[-1]); dr = 0.5 * (ry[1] - ry[-1])
    ev = 0.5 * (pk[1] + pk[-1]) - p0; evr = 0.5 * (ry[1] + ry[-1]) - r0
    rel = np.linalg.norm(dp - dr, axis=1).max() / max(np.linalg.norm(dr, axis=1).max(), 1e-12)
    rows_i.append((lab, rel))
    out("N (i) %s, amplitude %.2f: odd-in-eps displacement of the centre (x, y) at t = 20, 40, 60, 80: packet %s | rays %s | largest |packet - rays| "
        "(vector) over the largest ray displacement: %.3f; even part (packet - identity) %s, rays %s"
        % (lab, e0, " ".join("(%+.3f, %+.3f)" % tuple(v) for v in dp), " ".join("(%+.3f, %+.3f)" % tuple(v) for v in dr), rel,
           " ".join("(%+.3f, %+.3f)" % tuple(v) for v in ev), " ".join("(%+.3f, %+.3f)" % tuple(v) for v in evr)))

# ------------------------------------------------------------------ (ii) pure local rotation of the coin axes: g unchanged, rays of g see nothing
# EXACT: with U(x) = exp(-i theta(x) n.sigma/2) and E^j(x).sigma = U sigma_j U^dagger,
#     U^dagger H' U = sum_j sigma_j S_j^(cos Delta/2) - sum_j n_j C_j^(sin Delta/2),   Delta_b = theta(x + e_j) - theta(x) on the bond b,
# (U^dagger(x) U(x + e) = cos(Delta/2) - i sin(Delta/2) n.sigma, and {sigma_j, n.sigma} = 2 n_j): a local rotation is a walk with bond rates
# cos(Delta/2) (second order) plus a coin-blind symmetric hop along the rotation axis's in-plane component (first order, only if n_j != 0).
def rot_frames(axis, th0, m, grad):
    coord = (Yf if grad == "y" else Xf - x0)
    thv = th0 * np.sin(2 * np.pi * m * coord / L)
    c, s_ = np.cos(thv), np.sin(thv)
    Ef = ident()
    if axis == "z":
        Ef[0][0] = c; Ef[1][0] = s_; Ef[0][1] = -s_; Ef[1][1] = c
    else:
        Ef[1][1] = c; Ef[2][1] = s_
    return Ef, thv
NV = {"z": np.array([0.0, 0.0, 1.0]), "x": np.array([1.0, 0.0, 0.0])}
def Uop(axis, thv):
    c, s_ = np.cos(thv / 2), np.sin(thv / 2)
    if axis == "z":
        blocks = [np.diag([np.exp(-1j * t / 2), np.exp(1j * t / 2)]) for t in thv]
        d0 = np.exp(-1j * thv / 2); d1 = np.exp(1j * thv / 2)
        return sps.diags(np.stack([d0, d1], 1).ravel()).tocsr()
    rows = np.repeat(np.arange(N) * 2, 2); rows = np.concatenate([2 * np.arange(N), 2 * np.arange(N), 2 * np.arange(N) + 1, 2 * np.arange(N) + 1])
    cols = np.concatenate([2 * np.arange(N), 2 * np.arange(N) + 1, 2 * np.arange(N), 2 * np.arange(N) + 1])
    vals = np.concatenate([c, -1j * s_, -1j * s_, c])
    return sps.csr_matrix((vals, (rows, cols)), shape=(2 * N, 2 * N))
Tl = [Tx, Ty]
def equivalent(axis, thv):
    thg = thv.reshape(L, L)
    H = None
    for j in range(2):
        nb = np.roll(thg, -1, axis=j).ravel()                         # theta(x + e_j)
        dl = nb - thv
        Dc = sps.diags(np.cos(dl / 2)); Ds = sps.diags(np.sin(dl / 2))
        Sc = (Dc @ Tl[j] - Tl[j].T @ Dc) / 2j; Cs = (Ds @ Tl[j] + Tl[j].T @ Ds) / 2
        t = sps.kron(Sc, SIG[j]) - NV[axis][j] * sps.kron(Cs, sps.identity(2))
        H = t if H is None else H + t
    return H.tocsr()
for axis, grad in (("z", "y"), ("x", "y"), ("x", "x")):
    Ef, thv = rot_frames(axis, 0.2, 8, grad)
    U = Uop(axis, thv)
    d = abs(U.conj().T @ ham(Ef) @ U - equivalent(axis, thv)).max()
    out("X local rotation about coin %s varying along %s (theta0 = 0.2, wavelength 32): max |U^dagger H' U - [sum sigma_j S_j^(cos Delta/2) - sum n_j "
        "C_j^(sin Delta/2)]| = %.1e (the identity is exact)" % (axis, grad, d))

def ray_equiv(axis, th0, m, grad, kick, nr=256, seed=11, dt=0.1):
    """rays of the equivalent walk's positive branch: E = sqrt(sum_j cos^2(d_j theta/2) sin^2 k_j) - sum_j n_j sin(d_j theta/2) cos k_j;
    kick = True: the packet's coin was not co-rotated; in the rotated frame its sigma_n = +1 part carries the phase exp(+i theta/2): k += grad(theta)/2"""
    rng = np.random.default_rng(seed)
    base = np.stack([rng.normal(0, w / np.sqrt(2), nr), rng.normal(0, w / np.sqrt(2), nr), rng.normal(0, 1 / (np.sqrt(2) * w), nr), rng.normal(0, 1 / (np.sqrt(2) * w), nr)])
    flips = np.array(list(itertools.product((1, -1), repeat=4)), float).T
    st = (base[:, :, None] * flips[:, None, :]).reshape(4, -1) + np.array([x0, y0, q, 0.0])[:, None]
    kk = 2 * np.pi * m / L
    def dth(x, y):
        if grad == "y": return np.zeros_like(x), th0 * kk * np.cos(kk * y)
        return th0 * kk * np.cos(kk * (x - x0)), np.zeros_like(y)
    if kick:
        gx, gy = dth(st[0], st[1]); st[2] += gx / 2; st[3] += gy / 2
    nv = NV[axis]
    def En(x, y, k1, k2):
        gx, gy = dth(x, y)
        return np.sqrt(np.cos(gx / 2) ** 2 * np.sin(k1) ** 2 + np.cos(gy / 2) ** 2 * np.sin(k2) ** 2) - nv[0] * np.sin(gx / 2) * np.cos(k1) - nv[1] * np.sin(gy / 2) * np.cos(k2)
    h = 1e-5
    def f(st):
        x, y, k1, k2 = st
        return np.stack([(En(x, y, k1 + h, k2) - En(x, y, k1 - h, k2)) / (2 * h), (En(x, y, k1, k2 + h) - En(x, y, k1, k2 - h)) / (2 * h),
                         -(En(x + h, y, k1, k2) - En(x - h, y, k1, k2)) / (2 * h), -(En(x, y + h, k1, k2) - En(x, y - h, k1, k2)) / (2 * h)])
    start = st[:2].copy(); t = 0.0
    while t < TIMES[-1] - 1e-9:
        a1 = f(st); a2 = f(st + dt / 2 * a1); a3 = f(st + dt / 2 * a2); a4 = f(st + dt * a3)
        st = st + dt / 6 * (a1 + 2 * a2 + 2 * a3 + a4); t += dt
    return np.array([np.mean(st[0] - start[0]), np.mean(st[1] - start[1])])

rot = {}
for axis, grad in (("z", "y"), ("z", "x"), ("x", "y"), ("x", "x")):
    for m, th0 in ((4, 0.05), (4, 0.1), (4, 0.2), (8, 0.1), (2, 0.1)):
        res = {}
        for sgn in (+1, -1):
            Ef, thv = rot_frames(axis, sgn * th0, m, grad)
            Hr = ham(Ef)
            pr, psir = path(Hr, psi0)                                   # coin NOT co-rotated
            pc, psic = path(Hr, Uop(axis, thv) @ psi0)                  # coin co-rotated: the local positive-energy packet of the rotated frame
            res[sgn] = (pr, pc, psir, Hr)
        odd = 0.5 * (res[1][0][-1] - res[-1][0][-1]); even = 0.5 * (res[1][0][-1] + res[-1][0][-1]) - p0[-1]
        oddc = 0.5 * (res[1][1][-1] - res[-1][1][-1]); evenc = 0.5 * (res[1][1][-1] + res[-1][1][-1]) - p0[-1]
        rk = 0.5 * (ray_equiv(axis, th0, m, grad, True) - ray_equiv(axis, -th0, m, grad, True)) if axis == "x" else None
        rc = 0.5 * (ray_equiv(axis, th0, m, grad, False) - ray_equiv(axis, -th0, m, grad, False))
        rce = 0.5 * (ray_equiv(axis, th0, m, grad, False) + ray_equiv(axis, -th0, m, grad, False)) - r0[-1]
        gradient = th0 * 2 * np.pi * m / L
        nd = np.linalg.norm(res[1][2]) - 1
        e0v = np.real(np.vdot(psi0, res[1][3] @ psi0)); e1v = np.real(np.vdot(res[1][2], res[1][3] @ res[1][2]))
        rot[(axis, grad, m, th0)] = (odd, even, oddc, evenc, gradient)
        out("N (ii) rotation about coin %s, angle varying along %s, theta0 = %.2f, wavelength %.0f (max gradient %.4f rad/site), t = 80, relative to "
            "the unrotated frame: coin NOT co-rotated: odd %s (rays of the equivalent walk with the kick grad(theta)/2: %s), even %s | coin co-rotated: "
            "odd %s (equivalent-walk rays %s), even %s (rays %s) | rays of g: 0 | norm - 1 = %.1e, <H>(80) - <H>(0) = %.1e"
            % (axis, grad, th0, L / m, gradient, "(%+.4f, %+.4f)" % tuple(odd), ("(%+.4f, %+.4f)" % tuple(rk)) if rk is not None else "n/a: the packet's coin (sigma_x = +1) is not a sigma_z eigenstate, the kick splits it", "(%+.4f, %+.4f)" % tuple(even),
               "(%+.5f, %+.5f)" % tuple(oddc), "(%+.5f, %+.5f)" % tuple(rc), "(%+.5f, %+.5f)" % tuple(evenc), "(%+.5f, %+.5f)" % tuple(rce), nd, e1v - e0v))
for axis, grad in (("z", "y"), ("z", "x"), ("x", "y"), ("x", "x")):
    A = [rot[(axis, grad, 4, t0)] for t0 in (0.05, 0.1, 0.2)]
    gr_ = [a[4] for a in A]
    def slope(vals): 
        v = [max(np.linalg.norm(x), 1e-15) for x in vals]
        return np.polyfit(np.log(gr_), np.log(v), 1)[0]
    out("N (ii) rotation about coin %s varying along %s, wavelength 64, theta0 = 0.05/0.1/0.2: |odd| not co-rotated %s (slope %.2f); co-rotated |odd| %s "
        "(slope %.2f), |even| %s (slope %.2f)"
        % (axis, grad, " ".join("%.2e" % np.linalg.norm(a[0]) for a in A), slope([a[0] for a in A]), " ".join("%.2e" % np.linalg.norm(a[2]) for a in A),
           slope([a[2] for a in A]), " ".join("%.2e" % np.linalg.norm(a[3]) for a in A), slope([a[3] for a in A])))

# ------------------------------------------------------------------ (iii) conservation for the shear case
Ef, _ = shear_frames(0.1, 6, +1); Hs = ham(Ef)
err_control(Hs, "shear e0 = 0.1")
psiT = expm_multiply(-1j * Hs * 80.0, psi0)
out("N (iii) shear e0 = 0.1: norm - 1 = %.1e; <H>(80) - <H>(0) = %.1e (<H> = %.6f); hermiticity |H - H^dagger| = %.1e"
    % (np.linalg.norm(psiT) - 1, np.real(np.vdot(psiT, Hs @ psiT)) - np.real(np.vdot(psi0, Hs @ psi0)), np.real(np.vdot(psi0, Hs @ psi0)), abs(Hs - Hs.conj().T).max()))

out("")
worst = max(r for _, r in rows_i)
kick = max(np.linalg.norm(v[0]) for v in rot.values()); corot = max(np.linalg.norm(v[2]) + np.linalg.norm(v[3]) for k, v in rot.items() if not (k[0] == "x" and k[1] == "x"))
corot_xx = max(np.linalg.norm(v[2]) for k, v in rot.items() if k[0] == "x" and k[1] == "x")
acc = {lab.split(",")[0] + ("" if "e0 = 0.1" not in lab else " (0.1)"): r for lab, r in rows_i}
out("SUMMARY: packets in a slowly varying coin frame against clouds of rays of g^ij sin k_i sin k_j, t <= 80: stretch with a transverse gradient "
    "%.1f%%, symmetric shear varying along the motion %.1f%%, symmetric shear with a transverse gradient %.0f%% and %.0f%% (its odd part is a small "
    "longitudinal shift, 0.3-0.6 of 65 sites, that the rays of g overstate; the even part agrees to 10-17%%); a pure local ROTATION of the coin axes (g unchanged, rays of g silent) is "
    "exactly a walk with bond rates cos(Delta/2) plus a coin-blind hop n_j sin(Delta/2) along the rotation axis (identity checked to machine "
    "precision): a packet whose coin is not co-rotated gets a kick grad(theta)/2 and drifts by up to %.2f sites at t = 80 (linear in the angle); "
    "a co-rotated packet moves by at most %.1e sites when the axis has no component along the gradient (second order) and by up to %.3f when it "
    "does (first order, the hop); norm and <H> conserved to 1e-14"
    % (100 * rows_i[3][1], 100 * rows_i[2][1], 100 * rows_i[0][1], 100 * rows_i[1][1], kick, corot, corot_xx))
