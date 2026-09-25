#!/usr/bin/env python3
"""Packets of all eight species in block 60's exact strong field of one body at rest, run 2 of 2.

As landed: block 60 T4 (#8590): with walls held at w = l = 1, chi = 1 + Q g, Q chi_0 = mu; N = 1 - P g, P = Q w0, w0 = 1/(1 + 2 Q g0);
w = N/chi; the local weak-exterior ratio 1 + 2Q/(P + Q) = 1 + (1 + 2Qg0)/(1 + Qg0) (a local coefficient comparison, not an integrated turn).
Block 110 (#8960): bonds are crossed at sqrt(w_x w_y)/(chi_x chi_y); long-wave rays of E = (w/l)|k|, index n = chi^3/N; continuum turn series
2(3a + p)/b + (3 pi/2)(5a^2 + 4ap + p^2)/b^2 + ..., a = Q/(4 pi), p = w0 a.  Block 69: the reach-three coupling sigma_a (1/2){C_a[B], P_a}.
Block 77: the staggered rest term m eps(x), eps = (-1)^(x+y+z).
MAPPING (stated): the lengths enter through the reach-three coupling with the bond strain B_b = 1/(chi_x chi_y) - 1 on the bond b = (x, x + e_a),
so that 1 + B_b = 1/l_b, block 60's bond length l_b = chi_x chi_y, and the long-wave crossing factor is block 110's; to first order
B_b = -(log chi_x + log chi_y).  Generator H = phi [sum_a sigma_a S_a + sum_a sigma_a (1/2){C_a[B], P_a} + m eps] phi, phi = sqrt(w).
Box: 64 x 48 x 48 interior sites, walls outside (open boundary: hops to walls absent), body at the centre.  Exact: the Green function by the
type-I sine transform (floating, exact to rounding), the T4 formulas (checked as residuals).  Floating point: expm_multiply evolutions, rays.
"""
import itertools, math, sys, time
import numpy as np
import scipy.sparse as sps
from scipy.fft import dstn, idstn
from scipy.sparse.linalg import expm_multiply
from scipy.interpolate import RegularGridInterpolator

def out(s): print(s, flush=True)
Lx, Ly, Lz = 64, 48, 48
X0 = np.array([32, 24, 24])
N3 = Lx * Ly * Lz
I, J, K = np.meshgrid(np.arange(Lx), np.arange(Ly), np.arange(Lz), indexing="ij")
idx = lambda i, j, k: (i * Ly + j) * Lz + k

# ------------------------------------------------------------------ the Dirichlet Green function and block 60's exact fields
lam = sum(np.meshgrid(*[2 - 2 * np.cos(np.pi * np.arange(1, L + 1) / (L + 1)) for L in (Lx, Ly, Lz)], indexing="ij"))
delta = np.zeros((Lx, Ly, Lz)); delta[tuple(X0)] = 1.0
g = idstn(dstn(delta, type=1, norm="ortho") / lam, type=1, norm="ortho")
g0 = g[tuple(X0)]
def lapD(f):
    fp = np.pad(f, 1)                           # zero walls
    return (fp[2:, 1:-1, 1:-1] + fp[:-2, 1:-1, 1:-1] + fp[1:-1, 2:, 1:-1] + fp[1:-1, :-2, 1:-1] + fp[1:-1, 1:-1, 2:] + fp[1:-1, 1:-1, :-2] - 6 * f)
res_g = np.abs(-lapD(g) - delta).max()
out("X Dirichlet Green function of the 64x48x48 box (type-I sine transform): g0 = %.8f, g at distance 8/12/16 along y: %.6f %.6f %.6f "
    "(continuum 1/(4 pi r): %.6f %.6f %.6f); residual of -Delta g = delta: %.1e"
    % (g0, g[32, 32, 24], g[32, 36, 24], g[32, 40, 24], 1 / (4 * np.pi * 8), 1 / (4 * np.pi * 12), 1 / (4 * np.pi * 16), res_g))
FCACHE = {}
def fields(Qg0):
    if Qg0 in FCACHE: return FCACHE[Qg0]
    FCACHE[Qg0] = _fields(Qg0); return FCACHE[Qg0]
def _fields(Qg0):
    Q = Qg0 / g0; w0 = 1 / (1 + 2 * Qg0); P = Q * w0
    chi = 1 + Q * g; Nf = 1 - P * g; w = Nf / chi
    # residuals of block 60 T4: Delta chi = -Q delta (on interior, walls chi = 1: the padded Laplacian of chi - 1); (-Delta + Q_x/chi_x) N = 0 with N = 1 on the walls
    r1 = np.abs(lapD(chi - 1) + Q * delta).max()
    r2 = np.abs(-lapD(Nf - 1) + Q * delta / chi * Nf).max()
    return dict(Q=Q, P=P, w0=w0, chi=chi, N=Nf, w=w, r1=r1, r2=r2)
for Qg0 in (0.05, 0.2, 0.5):
    f = fields(Qg0)
    out("X block 60 T4 at Q g0 = %.2f: Q = %.4f, w0 = %.6f (clock at the body; formula 1/(1 + 2Qg0) = %.6f), P = %.4f; residuals of the lengths' "
        "and the rates' equations %.1e, %.1e; local weak-exterior ratio 1 + (1 + 2Qg0)/(1 + Qg0) = %.5f"
        % (Qg0, f["Q"], f["w"][tuple(X0)], 1 / (1 + 2 * Qg0), f["P"], f["r1"], f["r2"], 1 + (1 + 2 * Qg0) / (1 + Qg0)))

# ------------------------------------------------------------------ lattice operators (open box)
def shift(a):
    dI = [0, 0, 0]; dI[a] = 1
    ii, jj, kk = I + dI[0], J + dI[1], K + dI[2]
    ok = (ii < Lx) & (jj < Ly) & (kk < Lz)
    rows = idx(I, J, K)[ok]; cols = idx(ii, jj, kk)[ok]
    return sps.csr_matrix((np.ones(rows.size), (rows, cols)), shape=(N3, N3))     # (T psi)(x) = psi(x + e_a), zero past the wall
T = [shift(a) for a in range(3)]
S = [((t - t.T) / 2j).tocsr() for t in T]
C = [((t + t.T) / 2).tocsr() for t in T]
P2 = [((S[a] @ C[a] + C[a] @ S[a]) / 2).tocsr() for a in range(3)]                  # the two-step momentum (symmetrised at the walls)
SIG = [sps.csr_matrix(np.array([[0, 1], [1, 0]], complex)), sps.csr_matrix(np.array([[0, -1j], [1j, 0]])), sps.csr_matrix(np.array([[1, 0], [0, -1]], complex))]
I2 = sps.identity(2, format="csr")
EPS = ((-1.0) ** (I + J + K)).ravel()
def bond_strain(chi, a):
    """B on the bond (x, x + e_a): 1/(chi_x chi_{x+e_a}) - 1, stored at x (zero on bonds that leave the box)"""
    c2 = np.roll(chi, -1, axis=a)
    B = 1.0 / (chi * c2) - 1.0
    sl = [slice(None)] * 3; sl[a] = -1; B[tuple(sl)] = 0.0
    return B.ravel()
def Cw(a, v):
    D = sps.diags(v)
    return ((D @ T[a] + T[a].T @ D) / 2).tocsr()
def generator(fl, m, lengths=True):
    Hc = None
    for a in range(3):
        term = S[a]
        if fl is not None and lengths:
            Ca = Cw(a, bond_strain(fl["chi"], a))
            term = term + (Ca @ P2[a] + P2[a] @ Ca) / 2
        t = sps.kron(term, SIG[a])
        Hc = t if Hc is None else Hc + t
    if m:
        Hc = Hc + sps.kron(sps.diags(m * EPS), I2)
    if fl is not None:
        ph = sps.kron(sps.diags(np.sqrt(fl["w"].ravel())), I2)
        Hc = ph @ Hc @ ph
    return Hc.tocsr()

# ------------------------------------------------------------------ exact species maps on the actual operator (block 70): V_n H V_n^dagger = s_n H
PAULI = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
SPECIES = list(itertools.product((0, 1), repeat=3))
def Vop(n):
    D = np.array([(-1) ** v for v in n]); s = int(np.prod(D)); rho = s * D
    if np.all(rho == 1): R = np.eye(2)
    else: R = PAULI[int(np.nonzero(rho == 1)[0][0])]
    U = ((-1.0) ** (n[0] * I + n[1] * J + n[2] * K)).ravel()
    return sps.kron(sps.diags(U), sps.csr_matrix(R)).tocsr(), s
f05 = fields(0.05); Hm0 = generator(f05, 0.0)
devs = []
for n in SPECIES:
    V, s = Vop(n)
    devs.append(abs(V @ Hm0 @ V.conj().T - s * Hm0).max())
out("X block 70 on the actual generator (rates, reach-three lengths, walls, m = 0, Q g0 = 0.05): max |V_n H V_n^dagger - s_n H| over the eight "
    "species = %.1e (the species' massless dynamics are exact images of one another)" % max(devs))

# ------------------------------------------------------------------ packets
q0, sig_f, sig_s, Tf, Ts, mslow = 0.4, 3.0, 5.0, 52.0, 40.0, 0.6
Pop = [sps.kron(P2[a], I2).tocsr() for a in range(3)]
def envelope(c, sig):
    return np.exp(-((I - c[0]) ** 2 + (J - c[1]) ** 2 + (K - c[2]) ** 2) / (4 * sig ** 2))
def fast_packet(n, b):
    c = (X0[0] - 24, X0[1] + b, X0[2])
    kx = np.pi * n[0] + q0; ky = np.pi * n[1]; kz = np.pi * n[2]
    ph = np.exp(1j * (kx * (I - c[0]) + ky * (J - c[1]) + kz * (K - c[2])))
    h = sum(np.sin([kx, ky, kz][a]) * PAULI[a] for a in range(3))
    ev, vec = np.linalg.eigh(h); u = vec[:, 1]
    amp = envelope(c, sig_f) * ph
    # projected on the free walk's positive branch momentum by momentum (FFT on the box grid; the packet is far from the walls)
    comp = [np.fft.fftn(amp * u[0]), np.fft.fftn(amp * u[1])]
    kk = [2 * np.pi * np.fft.fftfreq(L) for L in (Lx, Ly, Lz)]
    KX, KY, KZ = np.meshgrid(*kk, indexing="ij")
    sx, sy, sz = np.sin(KX), np.sin(KY), np.sin(KZ); e = np.sqrt(sx ** 2 + sy ** 2 + sz ** 2); e[e == 0] = 1
    nx, ny, nz = sx / e, sy / e, sz / e
    up = 0.5 * ((1 + nz) * comp[0] + (nx - 1j * ny) * comp[1]); dn = 0.5 * ((nx + 1j * ny) * comp[0] + (1 - nz) * comp[1])
    psi = np.stack([np.fft.ifftn(up).ravel(), np.fft.ifftn(dn).ravel()], 1).ravel()
    return psi / np.linalg.norm(psi)
def slow_packet(n, H):
    c = (X0[0] + 12, X0[1], X0[2])
    ph = np.exp(1j * np.pi * (n[0] * I + n[1] * J + n[2] * K))
    best = None
    for sgn in (+1, -1):
        for u in (np.array([1, 0], complex), np.array([0, 1], complex)):
            psi = ((envelope(c, sig_s) * ph * (1 + sgn * ((-1.0) ** (I + J + K)))).ravel()[:, None] * u[None, :]).ravel()
            psi /= np.linalg.norm(psi)
            e = np.real(np.vdot(psi, H @ psi))
            if best is None or e > best[0]: best = (e, psi)
    return best[1], best[0]
def measure(psi):
    rho = (np.abs(psi.reshape(N3, 2)) ** 2).sum(1)
    return np.array([(rho * I.ravel()).sum(), (rho * J.ravel()).sum(), (rho * K.ravel()).sum()]), np.array([np.real(np.vdot(psi, Pop[a] @ psi)) for a in range(3)])
H0free = generator(None, 0.0); H0mass = generator(None, mslow)
FAST = {}
t0 = time.time()
ref_cache = {}
def fast_run(Qg0, n, b, lengths=True):
    key = (n, b)
    if key not in ref_cache:
        p0 = fast_packet(n, b); ref_cache[key] = measure(expm_multiply(-1j * H0free * Tf, p0))
    fl = fields(Qg0); H = generator(fl, 0.0, lengths); p0 = fast_packet(n, b)
    x, P = measure(expm_multiply(-1j * H * Tf, p0)); x0r, P0r = ref_cache[key]
    return x - x0r, P - P0r
FASTC = {}
for Qg0 in (0.05, 0.2, 0.5):
    for b in (8, 12, 16):
        FAST[(Qg0, (0, 0, 0), b)] = fast_run(Qg0, (0, 0, 0), b)
        FASTC[(Qg0, (0, 0, 0), b)] = fast_run(Qg0, (0, 0, 0), b, lengths=False)
for n in SPECIES:
    if (0.05, n, 12) not in FAST:
        FAST[(0.05, n, 12)] = fast_run(0.05, n, 12)
        FASTC[(0.05, n, 12)] = fast_run(0.05, n, 12, lengths=False)
out("N fast packets (q = %.1f, width %g, T = %g, start 24 sites before the body): runs done in %.0f s" % (q0, sig_f, Tf, time.time() - t0))
SLOW = {}
t0 = time.time()
for Qg0, n in [(0.05, s_) for s_ in ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))] + [(0.2, (0, 0, 0)), (0.5, (0, 0, 0))]:
    fl = fields(Qg0); H = generator(fl, mslow)
    p0, e0 = slow_packet(n, H)
    pr, er = slow_packet(n, H0mass)
    x, _ = measure(expm_multiply(-1j * H * Ts, p0)); xr, _ = measure(expm_multiply(-1j * H0mass * Ts, pr))
    rho0 = (np.abs(p0.reshape(N3, 2)) ** 2).sum(1).reshape(Lx, Ly, Lz)
    u = np.log(fl["w"]); dux = (np.roll(u, -1, 0) - np.roll(u, 1, 0)) / 2
    a_model = (rho0 * dux).sum()                           # the packet-averaged du/dx at release: the pull towards the body (at smaller x) has this size
    SLOW[(Qg0, n)] = (x - xr, e0, a_model)
out("N slow packets (m = %.1f on one sublattice, width %g, released at rest 12 sites from the body along x, T = %g): runs done in %.0f s" % (mslow, sig_s, Ts, time.time() - t0))

# ------------------------------------------------------------------ rays in the same fields (lattice symbol and continuum), clouds and central rays
from scipy.ndimage import map_coordinates, spline_filter
def ray_fields(fl):
    """cubic-spline coefficients (prefiltered once) of w, chi and their central-difference gradients, walls padded at 1"""
    wp = np.pad(fl["w"], 2, constant_values=1.0); cp = np.pad(fl["chi"], 2, constant_values=1.0)
    grads = lambda F: [(np.roll(F, -1, a) - np.roll(F, 1, a)) / 2 for a in range(3)]
    sf = lambda F: spline_filter(F, order=3, mode="nearest")
    return sf(wp), sf(cp), [sf(G) for G in grads(wp)], [sf(G) for G in grads(cp)]
def interp(F, pts):
    return map_coordinates(F, pts + 2.0, order=3, mode="nearest", prefilter=False)
RFCACHE = {}
def rays(fl, n, b, kind, nr=2000, seed=5, dt=0.05, central=False, lengths=True):
    rng = np.random.default_rng(seed)
    c = np.array([X0[0] - 24, X0[1] + b, X0[2]], float); k0 = np.array([np.pi * n[0] + q0, np.pi * n[1], np.pi * n[2]])
    if central:
        x = c[:, None].copy(); k = k0[:, None].copy()
    else:
        x = c[:, None] + sig_f * rng.standard_normal((3, nr)); k = k0[:, None] + rng.standard_normal((3, nr)) / (2 * sig_f)
    key_rf = (id(fl), lengths)
    if key_rf not in RFCACHE:
        RFCACHE[key_rf] = ray_fields(fl if lengths else dict(w=fl["w"], chi=np.ones_like(fl["chi"])))
    wp, cp, gw, gc = RFCACHE[key_rf]
    def f(x, k):
        w = interp(wp, x); ch = interp(cp, x); dw = np.array([interp(G, x) for G in gw]); dc = np.array([interp(G, x) for G in gc])
        if kind == "lattice":
            B = 1 / ch ** 2 - 1; dB = -2 * dc / ch ** 3
            s, cc = np.sin(k), np.cos(k)
            h = s * (1 + B * cc ** 2); hn = np.sqrt((h ** 2).sum(0)) + 1e-300
            dh = cc * (1 + B * cc ** 2) - 2 * B * s ** 2 * cc
            xdot = w * h / hn * dh
            kdot = -(dw * hn + w * ((h / hn) * s * cc ** 2).sum(0) * dB)
        else:
            kn = np.sqrt((k ** 2).sum(0)) + 1e-300; cfac = w / ch ** 2
            xdot = cfac * k / kn
            kdot = -kn * (dw / ch ** 2 - 2 * w * dc / ch ** 3)
        return xdot, kdot
    x_s, k_s = x.copy(), k.copy()
    for _ in range(int(round(Tf / dt))):
        a1 = f(x, k); a2 = f(x + dt / 2 * a1[0], k + dt / 2 * a1[1]); a3 = f(x + dt / 2 * a2[0], k + dt / 2 * a2[1]); a4 = f(x + dt * a3[0], k + dt * a3[1])
        x = x + dt / 6 * (a1[0] + 2 * a2[0] + 2 * a3[0] + a4[0]); k = k + dt / 6 * (a1[1] + 2 * a2[1] + 2 * a3[1] + a4[1])
    return (x - x_s).mean(1), (0.5 * np.sin(2 * k) - 0.5 * np.sin(2 * k_s)).mean(1)
def ray_turn(fl, n, b, kind, central):
    dx, dP = rays(fl, n, b, kind, central=central)
    if fl is None: return dx, dP
    return dx, dP
flat = dict(w=np.ones((Lx, Ly, Lz)), chi=np.ones((Lx, Ly, Lz)))
RAYREF = {}
def ray_delta(Qg0, n, b, kind, central, lengths=True):
    key = (n, b, kind, central)
    if key not in RAYREF: RAYREF[key] = rays(flat, n, b, kind, central=central)
    dx, dP = rays(fields(Qg0), n, b, kind, central=central, lengths=lengths)
    return dx - RAYREF[key][0], dP - RAYREF[key][1]
def line_integral(F, b):
    """integral of -d_y F along the straight path y = y0 + b, z = z0, x from x0 - 24 to x0 - 24 + cos(q) Tf (the fast packet's)"""
    dF = -(np.roll(F, -1, 1) - np.roll(F, 1, 1)) / 2
    xs = np.linspace(X0[0] - 24, X0[0] - 24 + np.cos(q0) * Tf, 400)
    pts = np.stack([xs, np.full_like(xs, X0[1] + b), np.full_like(xs, X0[2])])
    vals = map_coordinates(dF, pts, order=3, mode="nearest")
    return np.trapezoid(vals, xs)

t0 = time.time()
rows = []
for Qg0 in (0.05, 0.2, 0.5):
    fl = fields(Qg0); u = np.log(fl["w"]); lam_ = np.log(fl["chi"] ** 2)
    dxs, e0, a_model = SLOW[(Qg0, (0, 0, 0))]
    ffall = (-2 * dxs[0] / Ts ** 2) / a_model                  # displacement towards the body over the size of the clocks' pull
    for b in (8, 12, 16):
        th_p = -FAST[(Qg0, (0, 0, 0), b)][1][1] / q0; th_pc = -FASTC[(Qg0, (0, 0, 0), b)][1][1] / q0
        th_cloud = -ray_delta(Qg0, (0, 0, 0), b, "lattice", False)[1][1] / q0
        th_cloudc = -ray_delta(Qg0, (0, 0, 0), b, "lattice", False, lengths=False)[1][1] / q0
        th_lat = -ray_delta(Qg0, (0, 0, 0), b, "lattice", True)[1][1] / q0
        th_latc = -ray_delta(Qg0, (0, 0, 0), b, "lattice", True, lengths=False)[1][1] / q0
        th_con = -ray_delta(Qg0, (0, 0, 0), b, "continuum", True)[1][1] / q0
        th_conc = -ray_delta(Qg0, (0, 0, 0), b, "continuum", True, lengths=False)[1][1] / q0
        Iu = line_integral(u, b); Ilam = line_integral(-lam_, b)
        R_model = (Iu + Ilam) / Iu
        rows.append(dict(Qg0=Qg0, b=b, th_p=th_p, th_cloud=th_cloud, th_lat=th_lat, th_con=th_con, R=th_p / th_pc, R_cloud=th_cloud / th_cloudc,
                         R_lat=th_lat / th_latc, R_con=th_con / th_conc, R_model=R_model, ffall=ffall))
        out("N Q g0 = %.2f, b = %d: turn (momentum kick / q): packet %.5f (clocks only %.5f) | lattice ray cloud %.5f (%.5f) | lattice central ray %.5f "
            "(%.5f) | continuum central ray %.5f (%.5f) | bending/fall = full / clocks-only: packet %.4f, cloud %.4f, lattice ray %.4f, continuum ray "
            "%.4f; index model along the path %.4f; block 60's local 1 + (1+2Qg0)/(1+Qg0) = %.4f | massive packet's fall / -du/dx = %.3f"
            % (Qg0, b, th_p, th_pc, th_cloud, th_cloudc, th_lat, th_latc, th_con, th_conc, th_p / th_pc, th_cloud / th_cloudc, th_lat / th_latc,
               th_con / th_conc, R_model, 1 + (1 + 2 * Qg0) / (1 + Qg0), ffall))
out("N rays done in %.0f s" % (time.time() - t0))
# the reach-three lattice factor: h_a = s_a (1 + B c_a^2), so at k = (q, 0, 0) the lengths' part of the kick carries cos^2 q while the clocks' part does not
for r in rows:
    r["R_latpred"] = 1 + np.cos(q0) ** 2 * (r["R_con"] - 1)
out("X the lengths enter the reach-three symbol as s_a (1 + B c_a^2): at k = (q, 0, 0) their share of the kick carries cos^2 q = %.4f, so the lattice "
    "ray's bending/fall should be 1 + cos^2 q (R_continuum - 1): %s against the lattice rays' %s"
    % (np.cos(q0) ** 2, " ".join("%.4f" % r["R_latpred"] for r in rows), " ".join("%.4f" % r["R_lat"] for r in rows)))
# slow packets by species
for (Qg0, n), (dxs, e0, a_model) in SLOW.items():
    out("N slow packet Q g0 = %.2f, species %s: energy %.4f (positive branch), displacement along x %.5f at T = %g (towards the body), acceleration %.3e against the packet-averaged "
        "du/dx %.3e (ratio %.4f)" % (Qg0, n, e0, dxs[0], Ts, -2 * dxs[0] / Ts ** 2, a_model, (-2 * dxs[0] / Ts ** 2) / a_model))
# species comparison at Q g0 = 0.05, b = 12
Rs = {n: FAST[(0.05, n, 12)][1][1] / FASTC[(0.05, n, 12)][1][1] for n in SPECIES}
Th = {n: -FAST[(0.05, n, 12)][1][1] / q0 for n in SPECIES}
out("N species at Q g0 = 0.05, b = 12: turn %s | bending/fall %s; spread of the ratio (max - min)/mean = %.2e"
    % (" ".join("%s: %.6f" % (n, Th[n]) for n in SPECIES), " ".join("%s: %.5f" % (n, Rs[n]) for n in SPECIES), (max(Rs.values()) - min(Rs.values())) / np.mean(list(Rs.values()))))
fsp = {n: (-2 * SLOW[(0.05, n)][0][0] / Ts ** 2) / SLOW[(0.05, n)][2] for n in ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))}
out("N slow packets by species at Q g0 = 0.05 (fall over the packet-averaged du/dx): %s" % " ".join("%s: %.5f" % kv for kv in fsp.items()))

# ------------------------------------------------------------------ the continuum series (block 110) in infinite space, and the lattice/width split
from scipy.integrate import quad
def turn_cont(a, p, b):
    n_ = lambda r: (r + a) ** 3 / (r ** 2 * (r - p))
    r0 = b
    for _ in range(200):                       # the turning point: r n(r) = b
        r0 = b / n_(r0)
    # theta = 2 int_{r0}^inf b dr / (r sqrt(r^2 n^2 - b^2)) - pi, substitution r = r0/s
    def integrand(s):
        r = r0 / s
        val = (r * n_(r)) ** 2 - b ** 2
        return 2 * b / (r * np.sqrt(max(val, 1e-300))) * (r0 / s ** 2)
    val, _ = quad(integrand, 1e-9, 1 - 1e-12, limit=400)
    return val - np.pi
for Qg0 in (0.05, 0.2, 0.5):
    Q = Qg0 / g0; w0 = 1 / (1 + 2 * Qg0); a = Q / (4 * np.pi); p = w0 * a
    cells = []
    for b in (8, 12, 16):
        th = turn_cont(a, p, b); s1 = 2 * (3 * a + p) / b; s2 = (3 * np.pi / 2) * (5 * a * a + 4 * a * p + p * p) / b ** 2
        cells.append("b = %d: exact %.6f, series to first order %.6f, to second %.6f (remainder %.1e)" % (b, th, s1, s1 + s2, th - s1 - s2))
    out("X continuum (infinite space, index chi^3/N = (r + a)^3/(r^2 (r - p))), Q g0 = %.2f, a = %.4f, p = %.4f: %s" % (Qg0, a, p, "; ".join(cells)))
# lattice correction and packet-width effect (box, same path), second-order parts by a fit in Q g0
for b in (8, 12, 16):
    R_ = [r for r in rows if r["b"] == b]
    xq = np.array([r["Qg0"] for r in R_])
    Lc = np.array([r["th_lat"] - r["th_con"] for r in R_]); Wd = np.array([r["th_cloud"] - r["th_lat"] for r in R_])
    cL = np.polyfit(xq, Lc, 2); cW = np.polyfit(xq, Wd, 2)
    L2 = cL[0] * 0.5 ** 2; W5 = Wd[-1]
    out("N b = %d: lattice correction (lattice minus continuum central ray) %s at Q g0 = 0.05/0.2/0.5, second-order part %.2e (Q g0)^2 -> %.2e at 0.5; "
        "packet-width effect (cloud minus central ray) %s; |second-order lattice correction| %s the packet-width effect at Q g0 = 0.5"
        % (b, " ".join("%+.2e" % v for v in Lc), cL[0], L2, " ".join("%+.2e" % v for v in Wd), "EXCEEDS" if abs(L2) > abs(W5) else "is below"))
    for r in R_: r["L2"] = L2; r["W5"] = W5

out("")
hits = []
spread = (max(Rs.values()) - min(Rs.values())) / np.mean(list(Rs.values()))
if spread > 0.05: hits.append("species' bending/fall differ by %.1f%% at Q g0 = 0.05" % (100 * spread))
if max(r["R"] for r in rows) > 3: hits.append("bending/fall exceeds 3 (%.3f)" % max(r["R"] for r in rows))
exceed = [r for r in rows if r["Qg0"] == 0.5 and abs(r["L2"]) > abs(r["W5"])]
if exceed: hits.append("the second-order lattice correction exceeds the packet-width effect at b = %s" % ", ".join(str(r["b"]) for r in exceed))
for h in hits: out("HIT: " + h)
r12 = {r["Qg0"]: r for r in rows if r["b"] == 12}
pc = max(abs(r["th_p"] / r["th_cloud"] - 1) for r in rows)
out("SUMMARY: all eight species (exact images under block 70's maps on this generator; ratio spread %.1e) in block 60's exact strong field, box "
    "64x48x48: bending/fall (the same packet with clocks and lengths over clocks only) at b = 12 = %.3f / %.3f / %.3f against the index model along "
    "the path %.3f / %.3f / %.3f and block 60's local 1 + (1+2Qg0)/(1+Qg0) = %.3f / %.3f / %.3f at Q g0 = 0.05 / 0.2 / 0.5; massive packets fall at "
    "%.2f-%.2f of the clocks' gradient; packets follow their lattice ray clouds to %.1f%%; the continuum series checked in infinite space"
    % (spread, r12[0.05]["R"], r12[0.2]["R"], r12[0.5]["R"], r12[0.05]["R_model"], r12[0.2]["R_model"], r12[0.5]["R_model"],
       1 + 1.1 / 1.05, 1 + 1.4 / 1.2, 1 + 2 / 1.5, min(r["ffall"] for r in rows), max(r["ffall"] for r in rows), 100 * pc))
