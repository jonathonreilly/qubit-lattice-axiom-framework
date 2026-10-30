AUDIT_INPUT_PATHS = ('docs/A_CUBE_TICK_THAT_READS_ITS_OWN_LAPSE_AND_EDGES_IS_WEYL_BLIND_SO_ITS_VACUUM_ENTROPY_COUNTS_CUT_BONDS_NOT_PROPER_AREA_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Repair of M5 (vacuum entanglement maximal -> Einstein equations) by letting
the hop between neighbours be set by their proper separation, with no per-cube
renormalisation; tests whether the half-filled sea's entropy then tracks proper
area, computes Jacobson's G = 1/(4 eta) and the induced (Sakharov) static
couplings from the same sea, and lists what the repair costs the update law.

Self-contained (numpy, scipy). Seeded. Supplied model, finite diagnostic.
"""
import time
import itertools
import numpy as np
from scipy.linalg import eigh_tridiagonal, schur
from scipy.interpolate import CubicSpline

AUDIT_TIMEOUT_SEC = 120

T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0
EPS0 = 0.0375


def check(tag, kind, ok, text, data):
    global NP, NF
    NP += bool(ok)
    NF += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} [{kind}] {text} | {data}")


def ent(C):
    nu = np.linalg.eigvalsh(C)
    nu = nu[(nu > 1e-13) & (nu < 1 - 1e-13)]
    return float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)))


# ------------------------------------------------ Bloch tick (2x2x2 cell, k in site units)
CELL = list(itertools.product((0, 1), repeat=3))
CIX = {c: n for n, c in enumerate(CELL)}


def bloch(k, par):
    H = np.zeros((8, 8), complex)
    for c in CELL:
        for mu in range(3):
            if c[mu] != par:
                continue
            d = list(c)
            d[mu] = 1 - c[mu]
            ph = [1, (-1) ** c[0], (-1) ** (c[0] + c[1])][mu] / np.sqrt(3)
            f = np.exp(2j * k[mu]) if c[mu] == 1 else 1.0
            i, j = CIX[c], CIX[tuple(d)]
            H[j, i] += ph * f
            H[i, j] += ph * np.conj(f)
    return H


I8 = np.eye(8)


def utick(k, eps, mu=0.0):
    a, b = eps - mu / 2, eps + mu / 2
    return (np.cos(b) * I8 + 1j * np.sin(b) * bloch(k, 1)) @ (np.cos(a) * I8 - 1j * np.sin(a) * bloch(k, 0))


def qe(k, eps, mu=0.0):
    return np.sort(-np.angle(np.linalg.eigvals(utick(k, eps, mu))))


def vmax(eps):
    ks = np.linspace(-np.pi / 2, np.pi / 2, 241)
    v = 0.0
    for ky in np.linspace(0, np.pi / 2, 4):
        for kz in np.linspace(0, np.pi / 2, 4):
            b = np.array([qe((kx, ky, kz), eps) for kx in ks])
            v = max(v, float(np.abs(np.diff(b, axis=0)).max() / (ks[1] - ks[0])))
    return v


# ------------------------------------------------ 8^3 torus (cubes of both tilings)
L8 = 8
G8 = np.indices((L8, L8, L8)).reshape(3, -1).T
N8 = L8 ** 3


def idx(x, y, z, L=L8):
    return ((x % L) * L + (y % L)) * L + (z % L)


def origin(c, p, L=L8):
    return idx(*[(c[v] - ((c[v] - p) % 2)) % L for v in range(3)], L=L)


BONDS = []
for x, y, z in G8:
    c = (x, y, z)
    for mu in range(3):
        d = [0, 0, 0]
        d[mu] = 1
        ph = [1, (-1) ** x, (-1) ** (x + y)][mu] * (-1 if c[mu] == L8 - 1 else 1)
        p = c[mu] % 2
        BONDS.append((idx(*c), idx(x + d[0], y + d[1], z + d[2]), mu, ph, p, origin(c, p)))
CUBE_OF = np.array([[origin(tuple(g), p) for p in (0, 1)] for g in G8])   # site -> cube id per tiling


def hop(weight, par=None):
    H = np.zeros((N8, N8))
    for i, j, mu, ph, p, cb in BONDS:
        if par is not None and p != par:
            continue
        w = weight(mu, p, cb)
        H[i, j] += ph * w
        H[j, i] += ph * w
    return H


def floquet_cubes(eps_c):
    """Tick with a step per cube: each cube applies cos(eps_c) - i sin(eps_c) Rhat (Rhat^2 = 1)."""
    U = np.eye(N8, dtype=complex)
    for par, sgn in ((0, -1), (1, +1)):
        D = np.diag(np.cos(eps_c[CUBE_OF[:, par]]))
        R = hop(lambda mu, p, cb: np.sin(eps_c[cb]) / np.sqrt(3), par)
        U = (D + sgn * 1j * R) @ U
    T, Z = schur(U, output='complex')
    q = np.angle(np.diag(T))
    Zn = Z[:, q > 0]
    return Zn @ Zn.conj().T


def gs(H):
    w, v = np.linalg.eigh(H)
    V = v[:, w < 0]
    return V @ V.T


X8 = G8[:, 0]
SLAB = np.where(X8 < 4)[0]
CUT = [(cb) for i, j, mu, ph, p, cb in BONDS if mu == 0 and X8[i] in (3, 7)]


def slab_S(P):
    return ent(P[np.ix_(SLAB, SLAB)])


# ------------------------------------------------ chains (transverse-momentum decomposition)
def chain_C(u, N):
    d = u * (-1.0) ** np.arange(2 * N)
    w, v = eigh_tridiagonal(d, np.ones(2 * N - 1), select='i', select_range=(0, N - 1))
    V = v[:N, :]
    return V @ V.T


UG = np.exp(np.linspace(np.log(0.02), np.log(16.0), 44))
SG = np.array([ent(chain_C(u, 300)) for u in UG])
_A = np.vstack([np.ones(5), np.log(UG[:5]), UG[:5] ** 2 * np.log(UG[:5])]).T
CT = np.linalg.lstsq(_A, SG[:5], rcond=None)[0]
SPL = CubicSpline(np.log(UG), SG)


def s_of(u):
    u = np.asarray(u, float).ravel()
    out = np.empty_like(u)
    lo = u < UG[0]
    out[~lo] = SPL(np.log(u[~lo]))
    out[lo] = CT[0] + CT[1] * np.log(u[lo]) + CT[2] * u[lo] ** 2 * np.log(u[lo])
    return out


KK = (np.arange(400) + 0.5) * 2 * np.pi / 400
KY, KZ = np.meshgrid(KK, KK)


def eta_plane(tx, ty, tz, m=0.0):
    M = np.sqrt(4 * ty ** 2 * np.cos(KY) ** 2 + 4 * tz ** 2 * np.cos(KZ) ** 2 + m * m)
    return float(s_of(M / tx).mean())


# =============================================================== A. the repaired update
print("== A. hop = N/(proper length), no per-cube normalisation: what changes in the tick")
w = np.array([1 / 0.7, 1 / 1.3, 1 / 2.1])          # 1/l_i for one cube
Nl = np.sin(EPS0) / np.linalg.norm(w)               # CL-1 lapse clause: sqrt3 N rms(w) = N|w| = sin eps0
cub = [c for c in CELL]
Wm = []
for mu in range(3):
    Wc = np.zeros((8, 8))
    for c in cub:
        if c[mu] == 0:
            d = list(c)
            d[mu] = 1
            ph = [1, (-1) ** c[0], (-1) ** (c[0] + c[1])][mu]
            Wc[CIX[c], CIX[tuple(d)]] = Wc[CIX[tuple(d)], CIX[c]] = ph
    Wm.append(Wc)
Run = Nl * sum(w[m] * Wm[m] for m in range(3))
Rhat = sum(w[m] * Wm[m] for m in range(3)) / np.linalg.norm(w)
U_cl1 = np.cos(EPS0) * I8 - 1j * np.sin(EPS0) * Rhat
U_un = np.cos(EPS0) * I8 - 1j * Run
check("A1", "T", np.abs(Run @ Run - (Nl * np.linalg.norm(w)) ** 2 * I8).max() < 1e-15 and np.abs(U_cl1 - U_un).max() < 1e-15,
      "W_i anticommute, so the unnormalised hop N sum_i W_i/l_i squares to (N|w|)^2; with CL-1's lapse clause N|w| = sin eps0 the CL-1 "
      "cube unitary IS cos(eps0) - i N sum_i W_i/l_i: the per-cube normalisation is the lapse clause tying N to the edges",
      f"one cube, l = (0.7, 1.3, 2.1): |R_un^2 - sin^2 eps0| = {np.abs(Run@Run - np.sin(EPS0)**2*I8).max():.0e}, |U_CL1 - U_un| = {np.abs(U_cl1-U_un).max():.0e}")

vr = [(e, vmax(e) / (2 / np.sqrt(3) * np.sin(e))) for e in (0.0375, 0.3, 0.6, 1.0, 1.3)]
check("A2", "T", all(abs(r - 1) < 2e-3 for _, r in vr),
      "tick's max group velocity = (2/sqrt3) sin(eps) sites/tick at every step (Bloch): with the step read as sin(eps_c) = N_c|w_c| "
      "the cone is exact cube by cube for ANY lapse (variant R2, needs N|w| <= 1); step eps0 on the unnormalised hop (variant R1) "
      "scales light speed by sin(eps0|w|)/sin(eps0)",
      "v/((2/sqrt3) sin eps): " + ", ".join(f"{e}: {r:.5f}" for e, r in vr)
      + f"; R1 at edge l = 1/8: light speed x {np.sin(EPS0*8)/np.sin(EPS0):.2f}, at l = 4: x {np.sin(EPS0/4)/np.sin(EPS0):.3f}")

from scipy.optimize import minimize
ep_rows = []
for eps in (0.0375, 0.3, 0.6):
    for r in (0.5, 1.0):
        mu = r * eps
        f = lambda k: float(np.abs(qe(k, eps, mu)).min())
        res = minimize(f, np.zeros(3), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-15})
        h = 1e-3
        e1 = np.array([1.0, 0, 0])
        curv = (f(res.x + h * e1) + f(res.x - h * e1) - 2 * res.fun) / h ** 2
        ep_rows.append((eps, r, res.fun / mu, curv * res.fun / (2 / np.sqrt(3) * np.sin(eps)) ** 2 - (1 - r * r / 4)))
check("A3", "D", all(abs(a[2] - 1) < 1e-9 and 0.02 < a[3] / (a[0] * a[1]) ** 2 < 0.12 for a in ep_rows),
      "massive tick: rest phase = mu = mN per tick EXACTLY at every step (rest energy couples to the lapse universally); inertial "
      "factor 1 - (mu/eps)^2/4 plus a step-dependent remainder ~0.07 mu^2: species-dependent, negligible for observed m l",
      "eps, mu/eps: rest/mu - 1, inertial remainder: " + "; ".join(f"{a},{b}: {c-1:.0e}, {d:+.1e}" for a, b, c, d in ep_rows))

Nc = RNG.uniform(0.5, 1.0, N8)
lc = np.exp(RNG.uniform(np.log(1.0), np.log(4.0), N8))
sinb = lambda N_, l_: np.arcsin(np.sqrt(3) * N_ / l_ * np.sin(EPS0) / np.sqrt(3))   # sin eps_c = N_c |w_c| sin(eps0), |w| = sqrt3/l
P_base = floquet_cubes(sinb(Nc, lc))
Om = np.exp(RNG.uniform(np.log(1 / 8), np.log(4), N8))
P_weyl = floquet_cubes(sinb(Om * Nc, Om * lc))
lam = np.exp(RNG.uniform(np.log(1 / 2), np.log(2), N8))
P_sp = floquet_cubes(sinb(Nc, lam * lc))
dW = abs(slab_S(P_weyl) - slab_S(P_base))
dSp = abs(slab_S(P_sp) - slab_S(P_base))
check("A4", "T", dW < 1e-9 and dSp > 1e-3,
      "4D Weyl theorem: a cube reads only ratios of its own N and l_i, so (N, l) -> Omega (N, l) cube-wise leaves tick, vacuum and every "
      "entropy unchanged while proper areas scale by Omega^2; spatial-only rescaling at fixed N (the repair) moves S",
      f"8^3 Floquet, random cube N, l: Weyl factors in [1/8, 4]: |dS| = {dW:.1e}; spatial factors in [1/2, 2] at fixed N: |dS| = {dSp:.3f}")

# =============================================================== B. area-law tests
print("== B. does S track proper area under the repair?")
# B1 uniform spatial scaling at fixed N: static exact; Floquet tiny
H0 = hop(lambda mu, p, cb: 1.0)
S0 = slab_S(gs(H0))
S0c = slab_S(gs(H0 * 3.7))
Sf = [slab_S(floquet_cubes(np.full(N8, np.arcsin(np.sin(EPS0) / f)))) for f in (1.01, 1 / 1.01)]
dlnSA = (np.log(Sf[0]) - np.log(Sf[1])) / (2 * np.log(1.01 ** 2))
check("B1", "T", abs(S0c - S0) < 1e-10 and abs(dlnSA) < 1e-2,
      "uniform rescaling of all edges at fixed N: the static vacuum is exactly unchanged (ground state of c H = ground state of H); in the "
      "tick only the step moves (sin eps = N|w|), an O(eps^2) Floquet effect: dlnS/dlnA ~ 0, area law needs 1",
      f"static |dS| = {abs(S0c-S0):.0e}; tick at eps0 = {EPS0}: dlnS/dlnA = {dlnSA:+.1e}")

e0 = eta_plane(1, 1, 1)
ep = 0.01
dlt = (eta_plane(1, 1 / (1 + ep), 1 / (1 + ep)) - e0) / e0 / (2 * ep)
dln = (eta_plane(1 / (1 + ep), 1, 1) - e0) / e0 / ep
dcf = abs(eta_plane(1 / (1 + ep), 1 / (1 + ep), 1 / (1 + ep)) - e0)
check("B2", "D", dcf < 1e-12 and abs(dlt - 1) > 0.3 and abs(dln) > 0.3,
      "homogeneous strains (planar (100) cut, transverse-momentum chains): the repair and CL-1 give the SAME vacuum (only the overall "
      "hop scale differs), so the shape responses are unchanged: transverse stretch gives less than half the area-law response, "
      "normal stretch at fixed area moves S",
      f"eta_100 = {e0:.6f}; dlnS/dlnA transverse = {dlt:.3f} (area law 1); dlnS/eps normal, dA = 0: {dln:.3f} (area law 0)")

xs, ys = [], []
for t in range(10):
    lamc = np.exp(0.35 * RNG.normal(size=N8))
    S1 = slab_S(gs(hop(lambda mu, p, cb: 1.0 / lamc[cb])))
    A1 = np.sum(lamc[CUT] ** 2)
    xs.append(np.log(A1 / len(CUT)))
    ys.append(np.log(S1 / S0))
slope = np.polyfit(xs, ys, 1)[0]
check("B3", "D", abs(slope) < 0.5 and np.std(ys) > 1e-3,
      "random cube-wise edge factors (ln lambda ~ N(0, 0.35^2)) at fixed N, static 8^3: S moves, but ln S does not follow ln(proper "
      "cut area): the vacuum sees gradients of ln(N/l), not area",
      f"10 draws: regression slope dlnS/dlnA = {slope:+.3f} (area law 1); spread of ln S {np.std(ys):.3f}, of ln A {np.std(xs):.3f}")

Pm = gs(H0 + np.diag(0.7 * (-1.0) ** G8.sum(1)))
ks8 = 2 * np.pi * (np.arange(8) + 0.5) / 8
Sch = 0.0
for a in ks8:
    for b in ks8:
        M = np.sqrt(4 * np.cos(a) ** 2 + 4 * np.cos(b) ** 2 + 0.49)
        h = np.diag(M * (-1.0) ** np.arange(8)) + np.diag(np.ones(7), 1) + np.diag(np.ones(7), -1)
        h[0, -1] = h[-1, 0] = -1
        wv, vv = np.linalg.eigh(h)
        Vv = vv[:, wv < 0]
        Sch += ent((Vv @ Vv.T)[:4, :4])
etam = {m: eta_plane(1, 1, 1, m) for m in (0.25, 0.5, 1.0, 2.0)}
sl = {m: (np.log(eta_plane(1, 1, 1, m * 1.01)) - np.log(eta_plane(1, 1, 1, m / 1.01))) / (2 * np.log(1.01)) for m in (0.25, 0.5, 1.0)}
check("B4", "D", abs(slab_S(Pm) - Sch) < 1e-9 and all(v < 0 for v in sl.values()),
      "a mass is the only scale the sea can compare with l: with hop N/l and rest phase mN the vacuum depends on m l; staggered mass m "
      "enters the chains as sqrt(M^2 + m^2) (exact on 8^3); eta falls with m l, so at fixed N/l, dlnS/dlnA = (1/2) dln eta/dln(ml) < 0: "
      "the wrong sign for an area law",
      f"8^3 slab m = 0.7: 3D {slab_S(Pm):.8f} = chains {Sch:.8f}; eta(m): " + ", ".join(f"{m}: {v:.4f}" for m, v in etam.items())
      + "; dlnS/dlnA: " + ", ".join(f"{m}: {v/2:+.3f}" for m, v in sl.items()))

# =============================================================== C. G: Jacobson vs induced (static)
print("== C. G = 1/(4 eta) and the induced static couplings of the same sea")
reqB, reqA = np.pi / 2, 2 * np.pi
check("C1", "E", abs(e0 - 0.196645) < 2e-5,
      "Jacobson with the lattice cutoff: S = eta x (cut bonds), so in proper units eta_prop = eta/a^2 and G_J = a^2/(4 eta): constant in "
      "lattice units, varying as a^2 in proper units (x1024 across the edge window [1/8, 4]); unit map 8 pi G = L^2 with L = 2a (B) or a (A)",
      f"G_J = {1/(4*e0):.3f} a^2; G_J/G = {reqB/e0:.2f} (B), {reqA/e0:.1f} (A); per cell (2a)^2: eta = {4*e0:.3f}")

Lx, nk = 32, 8
Xc = np.arange(Lx)
kb = (np.arange(nk) + 0.5) * np.pi / nk


def Ebloch(phi, sig, m):
    """Static sea, x-dependent lapse e^phi and conformal factor e^sig (hop N/l), mass m N; 2x2 transverse Bloch cell."""
    n = 4 * Lx
    e = 0.0
    tx = np.exp((phi + np.roll(phi, -1)) / 2 - (sig + np.roll(sig, -1)) / 2)
    tt = np.exp(phi - sig)
    for ky in kb:
        for kz in kb:
            H = np.zeros((n, n), complex)
            for x in range(Lx):
                for y in (0, 1):
                    for z in (0, 1):
                        i = x * 4 + y * 2 + z
                        j = ((x + 1) % Lx) * 4 + y * 2 + z
                        ph = -tx[x] if x == Lx - 1 else tx[x]
                        H[j, i] += ph
                        H[i, j] += ph
                        j = x * 4 + (1 - y) * 2 + z
                        f = np.exp(2j * ky) if y == 1 else 1.0
                        H[j, i] += (-1) ** x * tt[x] * f
                        H[i, j] += (-1) ** x * tt[x] * np.conj(f)
                        j = x * 4 + y * 2 + (1 - z)
                        f = np.exp(2j * kz) if z == 1 else 1.0
                        H[j, i] += (-1) ** (x + y) * tt[x] * f
                        H[i, j] += (-1) ** (x + y) * tt[x] * np.conj(f)
                        H[i, i] += m * np.exp(phi[x]) * (-1) ** (x + y + z)
            wv = np.linalg.eigvalsh(H)
            e += wv[wv < 0].sum()
    return e / (nk * nk * n)


def quad_coeffs(m):
    z = np.zeros(Lx)
    e00 = Ebloch(z, z, m)
    s = 1e-3
    rows = []
    for nq in (1, 2, 3):
        q = 2 * np.pi * nq / Lx
        f = s * np.cos(q * Xc)
        d = lambda p, g: (Ebloch(p, g, m) + Ebloch(-p, -g, m) - 2 * e00) / s ** 2
        rows.append((q * q, d(z, f), d(f, z), d(f, f)))
    R = np.array(rows)
    ess, epp, eb = [np.polyfit(R[:, 0], R[:, i], 2)[1] for i in (1, 2, 3)]
    return ess, epp, eb - ess - epp


coef = {m: quad_coeffs(m) for m in (0.0, 0.5, 1.0)}
ess, epp, eps_ = coef[0.0]
A_, B_, C_ = -ess, -eps_, -epp
invGN0 = B_ * B_ / (2 * A_) - 2 * C_
alpha = B_ / 4
Mx = np.array([[2 * A_, B_], [B_, 2 * C_]])
check("C2", "T", abs(epp / ess - 1) < 1e-6 and abs(eps_ / ess + 2) < 1e-6 and abs(invGN0) < 1e-8 * abs(A_),
      "induced static action (Sakharov, same sea, E = -L): Weyl invariance forces (grad sigma)^2 : grad phi.grad sigma : (grad phi)^2 = "
      "1 : -2 : 1 (Einstein-Hilbert 2 : 4 : 0), so the field equations force rho = 0: NO Newtonian limit; N sqrt(h) R3 part: 1/(4G) = 4 pi alpha",
      f"Lx = {Lx}, 2x2 Bloch cell, nk = {nk}^2: e_ss {ess:.5f}, e_pp {epp:.5f}, e_ps {eps_:.5f}; 1/(4 pi G_N) = {invGN0:.0e}; "
      f"det = {np.linalg.det(Mx):.0e}; 4 pi alpha = {4*np.pi*alpha:.3f} vs eta {e0:.3f}")

Lc = 48
Xl = np.arange(Lc)
kc = (np.arange(24) + 0.5) * 2 * np.pi / 24
Mk = 2 * np.sqrt(np.cos(kc)[:, None] ** 2 + np.cos(kc)[None, :] ** 2).ravel()


def Echain(sig, scheme):
    s1, s2 = sig, np.roll(sig, -1)
    if scheme == 'exact':
        d = s2 - s1
        lb = np.where(np.abs(d) < 1e-14, np.exp(s1), (np.exp(s2) - np.exp(s1)) / np.where(np.abs(d) < 1e-14, 1, d))
    elif scheme == 'geometric':
        lb = np.exp((s1 + s2) / 2)
    else:
        lb = (np.exp(s1) + np.exp(s2)) / 2
    t = 1 / lb
    E = 0.0
    for M in Mk:
        h = np.diag(M * np.exp(-sig) * (-1.0) ** Xl) + np.diag(t[:-1], 1) + np.diag(t[:-1], -1)
        h[0, -1] = h[-1, 0] = -t[-1]
        wv = np.linalg.eigvalsh(h)
        E += wv[wv < 0].sum()
    return E / len(Mk) / Lc


sch = {}
for scheme in ('exact', 'geometric', 'arithmetic'):
    z = np.zeros(Lc)
    ez = Echain(z, scheme)
    R = []
    for nq in (1, 2, 3, 4):
        q = 2 * np.pi * nq / Lc
        f = 1e-3 * np.cos(q * Xl)
        R.append((q * q, (Echain(f, scheme) + Echain(-f, scheme) - 2 * ez) / 1e-6))
    R = np.array(R)
    sch[scheme] = 2 * np.pi * np.polyfit(R[:, 0], R[:, 1], 2)[1]
check("C3", "D", all(v > 0 for v in sch.values()) and max(sch.values()) / min(sch.values()) > 1.5,
      "how the hop reads a non-uniform edge (straight-edge proper length, geometric or arithmetic mean) moves the induced coefficient x2: "
      "a reading the rule must supply",
      "4 pi alpha = 2 pi e_ss (chains, Lx 48, 24^2 k): " + ", ".join(f"{k}: {v:.3f}" for k, v in sch.items())
      + f"; vs eta {e0:.3f}; G_alpha/G (B) = " + ", ".join(f"{reqB/v:.1f}" for v in sch.values()))

GN = {}
for m in (0.5, 1.0):
    a_, b_, c_ = coef[m]
    A2, B2, C2 = -a_, -c_, -b_
    GN[m] = 1 / (4 * np.pi * (B2 * B2 / (2 * A2) - 2 * C2))
check("C4", "E", all(v > 0 for v in GN.values()),
      "a mass (staggered, both copies; supplied) breaks Weyl invariance and induces a POSITIVE (attractive) static Newtonian coupling "
      "1/(4 pi G_N) = B^2/(2A) - 2C, weak: G_N far above the hinge-sum G",
      "m: G_N/a^2, G_N/G (B), (A): " + "; ".join(f"{m}: {v:.2f}, {v*2*np.pi:.0f}, {v*8*np.pi:.0f}" for m, v in GN.items()))

print("verdict: the repair (hop N/l with no lapse clause; step read from sin eps_c = N_c|w_c|) FAILS its target: S is exactly blind to the "
      "4D Weyl factor (A4), moves with ln(N/l) gradients only (B1-B3), and masses push it the wrong way (B4); S is eta x (cut bonds), "
      "not eta x proper area. Cost (A1-A3): the lapse becomes a free datum per cube; the cone and the EP survive.")
print("Sakharov: the massless sea induces no Newtonian limit (C2); masses induce a weak attractive one (C4). Jacobson's G_J = "
      f"{1/(4*e0):.2f} a^2 fixes nothing unless proper area per cut bond is one universal unit. Gate: no number chosen, no structure "
      "inserted, G not inserted; bends CL-1's lapse clause (no axiom); its built prediction (area law) FAILS.")
print("theorems: A1, A2, A4, B1, C2; diagnostics: A3, B2, B3, B4, C3; estimates: C1, C4")
print(f"elapsed {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
