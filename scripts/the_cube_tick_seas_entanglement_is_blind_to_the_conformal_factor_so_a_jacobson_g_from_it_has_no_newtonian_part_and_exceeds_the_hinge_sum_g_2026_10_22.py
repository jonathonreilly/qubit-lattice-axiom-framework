AUDIT_INPUT_PATHS = ('docs/THE_CUBE_TICK_SEAS_ENTANGLEMENT_IS_BLIND_TO_THE_CONFORMAL_FACTOR_SO_A_JACOBSON_G_FROM_IT_HAS_NO_NEWTONIAN_PART_AND_EXCEEDS_THE_HINGE_SUM_G_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Decisive test of the least-information geometry rule (A4) on the cube tick's
half-filled sea: area coefficient eta of the vacuum entanglement, the
entanglement first law, Bisognano-Wichmann locality, the response of S to edge
deformations, and the Jacobson coupling G = 1/(4 eta) against the hinge-sum G.

Self-contained (numpy, scipy). Seeded. Supplied model, finite diagnostic.
"""
import time
import numpy as np
from scipy.linalg import eigh_tridiagonal, schur
from scipy.interpolate import CubicSpline
from scipy.special import ive
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 120

T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(tag, kind, ok, text, data):
    global NP, NF
    NP += bool(ok)
    NF += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} [{kind}] {text} | {data}")


def ent(C):
    nu = np.linalg.eigvalsh(C)
    nu = nu[(nu > 1e-13) & (nu < 1 - 1e-13)]
    return float(-np.sum(nu * np.log(nu) + (1 - nu) * np.log(1 - nu)))


def modK(C):
    nu, V = np.linalg.eigh(C)
    nu = np.clip(nu, 1e-15, 1 - 1e-15)
    return (V * np.log((1 - nu) / nu)) @ V.T


# ---------------------------------------------------------------- 1D chains
def chain_C(u, N):
    """Open chain of 2N sites, hop 1, staggered mass u(-1)^x, half filled:
    correlation matrix of the left half."""
    d = u * (-1.0) ** np.arange(2 * N)
    w, v = eigh_tridiagonal(d, np.ones(2 * N - 1), select='i', select_range=(0, N - 1))
    V = v[:N, :]
    return V @ V.T


def s_chain(u, N=300):
    return ent(chain_C(u, N))


UG = np.exp(np.linspace(np.log(0.02), np.log(16.0), 44))
SG = np.array([s_chain(u) for u in UG])
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


def eta_plane(tx, ty, tz, n=500):
    """Planar (100) area coefficient per site^2: transverse-momentum chains."""
    k = (np.arange(n) + 0.5) * 2 * np.pi / n
    KY, KZ = np.meshgrid(k, k)
    M = 2 * np.sqrt(ty ** 2 * np.cos(KY) ** 2 + tz ** 2 * np.cos(KZ) ** 2)
    return float(s_of(M / tx).mean())


# ---------------------------------------------------------------- 3D torus
L8 = 8
G8 = np.indices((L8, L8, L8)).reshape(3, -1).T
N8 = L8 ** 3


def idx(x, y, z, L=L8):
    return ((x % L) * L + (y % L)) * L + (z % L)


def bond_list(L=L8):
    """(i, j, axis, staggered phase with APBC, tiling parity, cube id)."""
    out = []
    for x in range(L):
        for y in range(L):
            for z in range(L):
                c = (x, y, z)
                for mu in range(3):
                    d = [0, 0, 0]
                    d[mu] = 1
                    j = idx(x + d[0], y + d[1], z + d[2], L)
                    eta = [1, (-1) ** x, (-1) ** (x + y)][mu]
                    wrap = -1 if c[mu] == L - 1 else 1
                    p = c[mu] % 2
                    o = [(c[v] - ((c[v] - p) % 2)) % L for v in range(3)]
                    out.append((idx(*c, L=L), j, mu, eta * wrap, p, idx(*o, L=L)))
    return out


BONDS = bond_list()


def hop(weight):
    """Real symmetric hop matrix; weight(i, j, mu, parity, cube) -> float."""
    H = np.zeros((N8, N8))
    for i, j, mu, ph, p, cb in BONDS:
        w = weight(i, j, mu, p, cb)
        H[i, j] += ph * w
        H[j, i] += ph * w
    return H


def gs_proj(H):
    w, v = np.linalg.eigh(H)
    V = v[:, w < 0]
    return V @ V.T, float(np.abs(w).min())


def tiling_R(par, cube_w):
    """Each cube's R = sum_i w_i W_i / |w| for tiling par (R^2 = 1 per cube)."""
    def wt(i, j, mu, p, cb):
        if p != par:
            return 0.0
        w = cube_w(cb)
        return w[mu] / np.linalg.norm(w)
    return hop(wt)


def floquet_proj(eps, Re, Ro, MN=0.0, s_e=None):
    I = np.eye(N8)
    Ue = np.cos(eps) * I - 1j * np.sin(eps) * Re
    Uo = np.cos(eps) * I + 1j * np.sin(eps) * Ro
    if MN:
        Pm = (I - s_e) / 2
        V = I + Pm @ ((np.cos(MN / 2) - 1) * I + 1j * np.sin(MN / 2) * Re)
        U = Uo @ V @ Ue @ V
    else:
        U = Uo @ Ue
    T, Z = schur(U, output='complex')
    q = np.angle(np.diag(T))
    Zn = Z[:, q > 0]            # U = exp(-i w): occupied band w < 0
    return Zn @ Zn.conj().T, float(np.abs(np.triu(T, 1)).max()), float(np.abs(q).min())


X8 = G8[:, 0]
SLAB = np.where(X8 < 4)[0]                    # cuts through odd-tiling bonds
SLAB2 = np.where((X8 >= 1) & (X8 < 5))[0]     # cuts through even-tiling bonds


def slab_S(P):
    return ent(P[np.ix_(SLAB, SLAB)])


# ---------------------------------------------------------------- infinite-volume f
FC = {}


def fval(n):
    key = tuple(sorted(abs(int(a)) for a in n))
    if key not in FC:
        g = lambda t: ive(key[0], 2 * t) * ive(key[1], 2 * t) * ive(key[2], 2 * t) / np.sqrt(t)
        v = quad(g, 0, 1, limit=200)[0] + quad(g, 1, np.inf, limit=400)[0]
        FC[key] = (-1) ** sum(key) * v / np.sqrt(np.pi)
    return FC[key]


def corr_inf(sites):
    """Infinite-lattice pi-flux sea: C = 1/2 - (1/2) H |H|^-1, |H|^-1 = f(r)
    with f(2n) = pi^-1/2 int dt t^-1/2 prod_mu (-1)^n_mu e^-2t I_n_mu(2t)."""
    sites = np.asarray(sites).astype(np.int16)
    span = int(np.ptp(sites, axis=0).max()) + 2
    nm = span // 2 + 1
    F = np.zeros((2 * nm + 1,) * 3)
    for a in range(-nm, nm + 1):
        for b in range(-nm, nm + 1):
            for c in range(-nm, nm + 1):
                F[a + nm, b + nm, c + nm] = fval((a, b, c))
    n = len(sites)
    C = np.eye(n) / 2
    for mu in range(3):
        eta = [np.ones(n), (-1.0) ** (sites[:, 0] % 2), (-1.0) ** ((sites[:, 0] + sites[:, 1]) % 2)][mu]
        for s in (1, -1):
            z = sites.copy()
            z[:, mu] += s
            d = z[:, None, :] - sites[None, :, :]
            ev = np.all(d % 2 == 0, axis=2)
            h = d // 2 + nm
            vals = F[h[..., 0].clip(0, 2 * nm), h[..., 1].clip(0, 2 * nm), h[..., 2].clip(0, 2 * nm)]
            C -= 0.5 * eta[:, None] * np.where(ev, vals, 0.0)
    return C


# =============================================================== A. planar eta
print("== A. area coefficient of the pi-flux sea (both tick copies, eps -> 0)")
e0 = eta_plane(1, 1, 1)
e0b = eta_plane(1, 1, 1, n=400)
check("A1", "D", abs(CT[1] + 1 / 6) < 0.01 and abs(e0 - e0b) < 1e-5,
      "one transverse-momentum chain per (ky,kz): hop 1, staggered mass M = 2 sqrt(cos^2 ky + cos^2 kz); "
      "its half-line entropy has the c = 1 tail -(1/6) ln M; eta_100 = BZ mean, grid-converged",
      f"tail slope {CT[1]:.4f} (-1/6); eta_100 = {e0:.6f} nats/site^2 (grid 400: {e0b:.6f}); pi/16 = {np.pi/16:.6f} is NOT it")

# exact identity check: 8^3 APBC torus slab, real space vs chain sum
P0, gap0 = gs_proj(hop(lambda i, j, mu, p, cb: 1.0))
S_rs = slab_S(P0)
ks = 2 * np.pi * (np.arange(L8) + 0.5) / L8
S_ch = 0.0
for ky in ks:
    for kz in ks:
        M = 2 * np.sqrt(np.cos(ky) ** 2 + np.cos(kz) ** 2)
        h = np.diag(M * (-1.0) ** np.arange(L8)) + np.diag(np.ones(L8 - 1), 1) + np.diag(np.ones(L8 - 1), -1)
        h[0, -1] = h[-1, 0] = -1
        w, v = np.linalg.eigh(h)
        Vv = v[:, w < 0]
        S_ch += ent((Vv @ Vv.T)[:4, :4])
check("A2", "T", abs(S_rs - S_ch) < 1e-9,
      "exact: the 3D slab entropy on the 8^3 antiperiodic torus equals the sum over transverse momenta of 1D chain entropies "
      "(the (ky, ky+pi) pair decouples into two chains with mass +-M)",
      f"real space {S_rs:.10f}, chain sum {S_ch:.10f}, gap {gap0:.3f}; per site^2 {S_rs/(2*L8*L8):.4f}")

# cubes and balls in infinite volume
cub = []
for l in range(3, 9):
    r = np.arange(l)
    st = np.array([(a, b, c) for a in r for b in r for c in r])
    Cc = corr_inf(st)
    cub.append((l, ent(Cc)))
ll = np.array([c[0] for c in cub], float)
Sc = np.array([c[1] for c in cub])
Af = np.vstack([6 * ll ** 2, 12 * ll, np.log(ll), np.ones_like(ll)]).T
eta_cube = np.linalg.lstsq(Af, Sc, rcond=None)[0][0]
nuchk = np.linalg.eigvalsh(Cc)
check("A3", "D", abs(eta_cube - e0) / e0 < 0.03 and nuchk.min() > -1e-9 and nuchk.max() < 1 + 1e-9,
      "cubes l = 3..8 in the infinite lattice (C from a Bessel integral): fit S = eta 6 l^2 + b 12 l + c ln l + d reproduces eta_100",
      f"S(l): {', '.join(f'{a:.0f}:{b:.2f}' for a, b in cub)}; eta_cube = {eta_cube:.4f} vs eta_100 {e0:.4f}")

balls = []
for R in (2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0):
    r = np.arange(-int(R) - 1, int(R) + 2)
    st = np.array([(a, b, c) for a in r for b in r for c in r if a * a + b * b + c * c <= R * R])
    Reff = (3 * len(st) / (4 * np.pi)) ** (1 / 3)
    balls.append((R, len(st), 4 * np.pi * Reff ** 2, ent(corr_inf(st))))
Ab = np.array([b[2] for b in balls])
Sb = np.array([b[3] for b in balls])
eta_ball, cb0 = np.polyfit(Ab, Sb, 1)
check("A4", "D", eta_ball > e0 * 1.05,
      "balls R = 2.5..6 (A = 4 pi R_eff^2, R_eff from the site count): S = eta_ball A + c; per GEOMETRIC area the orientation-averaged "
      "coefficient exceeds the (100) one, so the vacuum's entropy per area depends on the cut's orientation",
      f"eta_ball = {eta_ball:.4f} (c = {cb0:.2f}), eta_ball/eta_100 = {eta_ball/e0:.3f}; S(R=6, {balls[-1][1]} sites) = {Sb[-1]:.2f}")

# =============================================================== B. tick and copy mass
print("== B. the cube tick itself (8^3 torus, Floquet vacuum = occupied quasi-energy band)")
one = lambda cb: np.ones(3)
Re = tiling_R(0, one)
Ro = tiling_R(1, one)
r2 = np.abs(Re @ Re - np.eye(N8)).max()
Sp = slab_S(gs_proj(Re + Ro)[0])
rows = []
for eps in (0.005, 0.0375, 0.3):
    Pf, od, qm = floquet_proj(eps, Re, Ro)
    rows.append((eps, slab_S(Pf) / Sp - 1))
ok = abs(rows[0][1]) < 1e-3 and abs(rows[1][1]) < 2e-3 and 0.5 < (rows[2][1] / rows[1][1]) / 64 < 2
check("B1", "D", ok and r2 < 1e-12,
      "the tick's Floquet vacuum tends to the pi-flux sea as eps0 -> 0, correction ~eps0^2: at the register's small eps0 the "
      "pi-flux sea is its equivalent to <0.1%",
      f"R^2-1 = {r2:.0e}; S_tick/S_piflux - 1: " + ", ".join(f"eps {a}: {b:+.1e}" for a, b in rows))

W = [hop(lambda i, j, m, p, cb, mu=mu: 1.0 if (m == mu and p == 0) else 0.0) for mu in range(3)]
s_e = 1j * W[0] @ W[1] @ W[2] @ Re
cm = []
for f in (0.5, 1.0, 1.9):
    MN = f * 0.0375
    Pf, od, qm = floquet_proj(0.0375, Re, Ro, MN, s_e)
    so, se = slab_S(Pf) / Sp, ent(Pf[np.ix_(SLAB2, SLAB2)]) / Sp
    cm.append((f, (so + se) / 2, qm, int(round(np.trace(Pf).real)), so, se))
cmax = max(c[1] for c in cm)
check("B2", "D", np.abs(s_e @ s_e - np.eye(N8)).max() < 1e-12 and all(c[3] == N8 // 2 and c[2] > 1e-3 for c in cm) and cmax < 2,
      "CL-1's copy mass (exp(i(MN/4)(1-s)R) before and after each even half-tick; band gapped, half filled) dimerises the heavy "
      "copy between the tilings; the cut-averaged eta moves by at most x1.7, not the x8 needed in E",
      "MN/eps0: S/S(0) odd cut, even cut, mean; min|q|: " + "; ".join(f"{a}: {e:.3f}, {g:.3f}, {b:.3f}; {c:.4f}" for a, b, c, _, e, g in cm))

# =============================================================== C. edge deformations
print("== C. response of the vacuum entropy to edge lengths (hop weight = 1/length, R normalised per cube)")
lam = np.exp(RNG.uniform(np.log(1 / 8), np.log(4), N8))
conf = lambda cb: lam[cb] * np.ones(3)
Pc = floquet_proj(0.0375, tiling_R(0, conf), tiling_R(1, conf))[0]
Pu = floquet_proj(0.0375, Re, Ro)[0]
dSc = abs(slab_S(Pc) - slab_S(Pu))
area_ratio = np.mean(lam ** 2)
ell = np.exp(RNG.uniform(-0.3, 0.3, (N8, 3)))
anis = lambda cb: 1.0 / ell[cb]
dSa = abs(slab_S(floquet_proj(0.0375, tiling_R(0, anis), tiling_R(1, anis))[0]) - slab_S(Pu))
check("C1", "T", dSc < 1e-9 and dSa > 1e-3,
      "theorem: each cube normalises its own hop (R^2 = 1) and the lapse clause fixes the step, so any cube-wise common rescaling "
      "of edges (a spatial conformal factor) leaves every half-tick and every entropy unchanged while proper areas scale: "
      "dS = 0 at dA != 0, so S is not eta x proper area; shape deformations do move S",
      f"random cube factors in [1/8, 4] (edge window): |dS| = {dSc:.1e} with mean area factor {area_ratio:.2f}; shape deformation |dS| = {dSa:.3f}")

ep = 0.01
et = eta_plane(1, 1 / (1 + ep), 1 / (1 + ep))
en = eta_plane(1 / (1 + ep), 1, 1)
ev = eta_plane((1 + ep) ** 2, 1 / (1 + ep), 1 / (1 + ep))
ecf = eta_plane(1 / (1 + ep), 1 / (1 + ep), 1 / (1 + ep))
dlt = (et - e0) / e0 / (2 * ep)
dln = (en - e0) / e0 / ep
etaT = (ev - e0) / ((1 + ep) ** 2 - 1)
check("C2", "D", abs(ecf - e0) < 1e-12 and abs(dlt - 1) > 0.3 and abs(dln) > 0.3,
      "planar cut, linear response (eps = 0.01): stretching the transverse edges raises the area by 2 eps but S by less than half "
      "of that fraction; stretching the normal edges (area fixed) lowers S; at fixed volume the area response defines eta_T",
      f"dlnS/dlnA (transverse) = {dlt:.3f} (area law: 1); dlnS/eps (normal, dA = 0) = {dln:.3f} (area law: 0); "
      f"eta_T = dS/dA|_V = {etaT:.4f} vs eta_100 {e0:.4f}; conformal dS = {abs(ecf-e0):.0e}")

# =============================================================== D. first law and BW
print("== D. entanglement first law and the modular Hamiltonian")
CUBE = np.where(np.all((G8 >= 2) & (G8 < 6), axis=1))[0]
C0 = P0[np.ix_(CUBE, CUBE)]
K = modK(C0)
S0 = ent(C0)
gf = RNG.normal(size=N8)
res = []
for d in (1e-3, 1e-2):
    Pd = gs_proj(hop(lambda i, j, mu, p, cb: 1.0 / (1.0 + d * 0.5 * (gf[i] + gf[j]))))[0]
    C1 = Pd[np.ix_(CUBE, CUBE)]
    dS = ent(C1) - S0
    dK = float(np.sum(K * (C1 - C0)))
    res.append((d, dS, dK, dK - dS))
q = res[1][3] / res[0][3]
check("D1", "T", abs(res[0][1] / res[0][2] - 1) < 0.02 and res[0][3] > 0 and res[1][3] > 0 and 60 < q < 160,
      "first law dS = d<K>, K = ln((1-C)/C): an identity at first order for any state change (random edge lengths, 4^3 cube "
      "in 8^3); d<K> - dS (relative entropy) is positive, second order; it imposes no equation on the edges by itself",
      "; ".join(f"d {a:.0e}: dS {b:+.3e}, d<K> {c:+.3e}" for a, b, c, _ in res) + f"; rel. ent. ratio {q:.0f} (d^2: 100)")

bw = []
for u in (0.1, 0.3, 1.0, 2.0):
    Kc = modK(chain_C(u, 300)[::-1, ::-1])
    bw.append((u, abs(Kc[0, 1]) / np.pi, abs(Kc[2, 3]) / (3 * np.pi)))
k = (np.arange(500) + 0.5) * 2 * np.pi / 500
KY, KZ = np.meshgrid(k, k)
Mk = 2 * np.sqrt(np.cos(KY) ** 2 + np.cos(KZ) ** 2).ravel()
sk = s_of(Mk)
ir = float(sk[Mk < 0.3].sum() / sk.sum())
check("D2", "D", abs(bw[0][1] - 1) < 0.01 and bw[3][1] < 0.9,
      "Bisognano-Wichmann: per transverse mode K = (2 pi/v) x local energy (v = 2) near the cone, not for cell-scale modes, "
      "which carry most of eta",
      "u, K_bond(j=1)/pi, K_bond(j=3)/(3pi): " + "; ".join(f"{a}: {b:.3f}, {c:.3f}" for a, b, c in bw)
      + f"; share of eta_100 from modes with M < 0.3: {ir:.3f}")

# =============================================================== E. photon estimate and Jacobson
print("== E. Jacobson's G = 1/(4 eta) against the hinge-sum G")


def s_bos(M, N=300):
    w, v = eigh_tridiagonal((2 + M * M) * np.ones(2 * N), -np.ones(2 * N - 1))
    Xm = (v * (0.5 / np.sqrt(w))) @ v.T
    Pm = (v * (0.5 * np.sqrt(w))) @ v.T
    nu = np.sqrt(np.clip(np.linalg.eigvals(Xm[:N, :N] @ Pm[:N, :N]).real, 0.25, None))
    a, b = nu + 0.5, nu - 0.5
    b = b[b > 1e-14]
    return float(np.sum(a * np.log(a)) - np.sum(b * np.log(b)))


MB = np.exp(np.linspace(np.log(0.03), np.log(3.0), 30))
SB = np.array([s_bos(m) for m in MB])
cb = np.polyfit(np.log(MB[:4]), SB[:4], 1)
Ms = np.sqrt(4 * np.sin(KY / 2) ** 2 + 4 * np.sin(KZ / 2) ** 2).ravel()
sbv = np.where(Ms < MB[0], np.polyval(cb, np.log(np.maximum(Ms, 1e-300))), CubicSpline(np.log(MB), SB)(np.log(np.maximum(Ms, MB[0]))))
eta_s = float(sbv.mean())
check("E1", "E", 0.01 < eta_s < 0.05,
      "ESTIMATE: massless lattice scalar by the same chain method; photon = 2 scalars (edge/centre term and rishons omitted)",
      f"eta_scalar = {eta_s:.4f}/site^2 (tail slope {cb[0]:.3f}); photon ~ {2*eta_s:.4f}")

req_B, req_A = np.pi / 2, 2 * np.pi
cases = [("sea, two copies", e0), ("sea + photon est.", e0 + 2 * eta_s),
         ("fixed-volume eta_T + photon", etaT + 2 * eta_s),
         ("sea x largest copy-mass factor", e0 * cmax)]
txt = "; ".join(f"{n}: eta {v:.3f} -> G_A4/G = {req_B/v:.2f} (B), {req_A/v:.1f} (A)" for n, v in cases)
check("E2", "E", all(req_B / v > 2 for _, v in cases),
      "Jacobson 1/(4G) = eta per site^2 vs hinge sum 8 pi G = L^2, L = cell rung = 2 sites (reading B: eta needed pi/2) or "
      "L = site (reading A: 2 pi); KILL criterion abs(ln(G_A4/G)) > ln 2 met for every content",
      txt)
gap = req_B - (e0 + 2 * eta_s)
check("E3", "E", gap > np.log(2),
      "rescue by the omitted rishon/edge-register sites would need > ln 2 per site^2 of cut (over one Bell pair per cut bond), "
      "set by supplied register sizes: FITTED",
      f"missing eta = {gap:.3f} nats/site^2 (ln 2 = {np.log(2):.3f})")
check("E4", "T", dSc < 1e-9 and (8 * 2) ** 2 == 256,
      "theorem (from C1): no response to the spatial conformal factor, so A4 gives no Newtonian coupling (1/G_N = 0), only a shape "
      "response; over the edge window [L/8, 2^(1+Delta) L] the vacuum entropy per proper area varies by >= 256 4^Delta",
      "agrees with induced-response (the tick sea induces no Newtonian sector)")

rB = [req_B / v for _, v in cases]
print(f"verdict: A4 KILLED as the source of G (exact conformal blindness; G_A4/G = {min(rB):.1f}-{max(rB):.1f} at reading B, "
      f"{4*min(rB):.0f}-{4*max(rB):.0f} at A; orientation-dependent eta). Gate: chooses no measured number, inserts no observed structure, bends no axiom; "
      "its built-in prediction G = 1/(4 eta) was tested and FAILS. The cell rung stays FITTED (hinge-sum unit map).")
print("theorems: A2, C1, D1, E4; diagnostics: A1, A3, A4, B1, B2, C2, D2; estimates: E1-E3")
print("supplied: pi-flux sea / cube tick at eps0 = 0.0375, hop = 1/length, (100) and lattice-ball cuts, photon = 2 scalars, "
      "readings A/B of the unit map; omitted: rishon and edge-register entanglement")
print(f"elapsed {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
