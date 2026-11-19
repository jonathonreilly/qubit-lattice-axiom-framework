#!/usr/bin/env python3
"""hop-recheck: edge-register gravity results redone with the ADOPTED edge hop.

Edge register: values n = 0..2S, length l_rung (1 + n/2S); the domain-normalised raiser V has unit
matrix elements, so the edge hop is J (V + V^dag) (a tight-binding chain on the values).  Everything
else in CL-1/CL-3 reads the edges diagonally (phase, lapse, tick control).  Toys only; numpy/scipy.
"""
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

AUDIT_TIMEOUT_SEC = 120
t0 = time.time()
NP = NF = 0


def check(tag, ok, msg, det=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg} | {det}")


def hop(S):
    d = 2 * S + 1
    return sp.diags([np.ones(d - 1), np.ones(d - 1)], [1, -1], format="csr")


def kron(*ops):
    out = ops[0]
    for o in ops[1:]:
        out = sp.kron(out, o, format="csr")
    return out


# ---------------------------------------------------------------- A. sign and signature
print("== A. the hop sign and the Regge kinetic signature")
S, nm = 4, 8
d = 2 * S + 1; I = sp.identity(d); Im = sp.identity(nm)
n = np.arange(d) - S; N = sp.diags(n.astype(float))
a = sp.diags(np.sqrt(np.arange(1, nm)), -1, shape=(nm, nm), format="csr"); x = (a + a.T) / np.sqrt(2.0)
def joint(sgn):   # two edge registers + one matter mode; matter frequency and a hinge phase read the edges
    H = sgn * 0.7 * (kron(hop(S), I, Im) + kron(I, hop(S), Im))
    H = H + 0.3 * kron(N @ N, I, Im) + 0.2 * kron(I, N @ N, Im) - 0.25 * kron(N, N, Im)
    w = 1.0 + 0.1 * (np.add.outer(n, n)).ravel()
    H = H + sp.kron(sp.diags(w), (a.T @ a) + 0.5 * Im) + 0.3 * kron(N, I, x)
    return H.toarray()
Hp, Hm = joint(+1), joint(-1)
P1 = np.diag(np.kron(np.kron((-1.0) ** n, (-1.0) ** n), np.ones(nm)))
wp, wm = np.linalg.eigvalsh(Hp), np.linalg.eigvalsh(Hm)
def U(H):
    w, V = np.linalg.eigh(H); return (V * np.exp(-1j * w)) @ V.conj().T
du = abs(P1 @ U(Hp) @ P1 - U(Hm)).max()
check("T", abs(wp - wm).max() < 1e-10 and du < 1e-10,
      "A1 P = prod_e (-1)^{n_e} maps each register's hop to minus itself and commutes with every term that reads "
      "the edges diagonally, so the hop sign is a relabelling "
      "(edge momentum shifted by pi/h): 'sign opposite to matter's' is unobservable with one-register hops; "
      "ghost or normal is a property of the state (band top or bottom), not of the rule",
      f"joint spectrum diff {abs(wp-wm).max():.0e}, |P U(+) P - U(-)| {du:.0e}")

# DeWitt kinetic form h_ij h_ij - (tr h)^2 in the six-register basis (3 axis + 3 even face diagonals)
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)]
idx = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]
Mmap = np.zeros((6, 6))   # s_e = e^T gamma e  as linear map of the 6 metric components
for r, e in enumerate(E):
    for c, (i, j) in enumerate(idx):
        Mmap[r, c] = e[i] * e[j] * (1 if i == j else 2)
Gm = np.zeros((6, 6))     # DeWitt on (g_xx, g_yy, g_zz, g_xy, g_yz, g_xz)
for c, (i, j) in enumerate(idx):
    Gm[c, c] = 1.0 if i == j else 2.0
Gm[:3, :3] -= 1.0
Minv = np.linalg.inv(Mmap); Gs = Minv.T @ Gm @ Minv   # kinetic form in edge-squared-length rates
ev, evec = np.linalg.eigh(Gs)
neg = evec[:, ev < 0][:, 0]; s0 = np.array([1, 1, 1, 2, 2, 2.0]); s0 /= np.linalg.norm(s0)
offd = np.abs(Gs - np.diag(np.diag(Gs))).max() / np.abs(np.diag(Gs)).max()
check("T", (ev > 0).sum() == 5 and (ev < 0).sum() == 1 and offd > 0.1,
      "A2 the Regge (DeWitt) kinetic form in the six edge registers per site has signature (5+,1-); it is not "
      "diagonal in the edge basis, while one-register hops expanded about any band extremum give a diagonal "
      "form: the adopted hop cannot be the GR kinetic term; the sign of the ghost direction is carried only by two-register terms",
      f"eigs {ev.min():.2f}..{ev.max():.2f} (#neg {(ev<0).sum()}); |neg vec . uniform-scaling| "
      f"{abs(neg @ s0):.2f}; max offdiag/diag {offd:.2f}")
# realise the inverse form with single- and two-register hops: 1-cos(t_e +- t_f) gives (t_e +- t_f)^2/2
Ainv = np.linalg.inv(Gs); bplus = np.where(Ainv > 0, Ainv, 0); bminus = np.where(Ainv < 0, -Ainv, 0)
Q = np.zeros((6, 6))
for e in range(6):
    for f in range(e + 1, 6):
        for b, sg in ((bplus[e, f], 1), (bminus[e, f], -1)):
            v = np.zeros(6); v[e] = 1; v[f] = sg; Q += b * np.outer(v, v)
single = np.diag(Ainv) - np.diag(Q); Q += np.diag(single)
check("T", abs(Q - Ainv).max() < 1e-12 and (single < 0).any(),
      "A3 one-register hops J_e(V_e+V_e^dag) plus pair hops b_ef(V_e V_f + h.c.), c_ef(V_e V_f^dag + h.c.) reproduce "
      "the inverse DeWitt form exactly at quadratic order; under P_e every term containing V_e flips, so the "
      "products single_e x single_f x pair_ef are gauge invariant and carry the (5,1) signature",
      f"|Q - G^-1| {abs(Q-Ainv).max():.0e}; single-hop weights {np.round(single,2).tolist()}")

# ---------------------------------------------------------------- B. Newton limit and BMV on registers
print("== B. Newton limit and the BMV phase with hop registers (static, adiabatic)")
def chain_H(S, k0, kc, J=1.0, sgn=1, nreg=3):
    d = 2 * S + 1; I = sp.identity(d); N = sp.diags(np.arange(d) - S + 0.0)
    ops = lambda o, i: kron(*[o if j == i else I for j in range(nreg)])
    H = sum(sgn * J * ops(hop(S), i) for i in range(nreg))
    H = H + sum(0.5 * k0 * ops(N @ N, i) for i in range(nreg))
    for i in range(nreg - 1):
        Dn = ops(N, i) - ops(N, i + 1); H = H + 0.5 * kc * (Dn @ Dn)
    Kmat = k0 * np.eye(nreg) + kc * (2 * np.eye(nreg) - np.eye(nreg, k=1) - np.eye(nreg, k=-1))
    Kmat[0, 0] -= kc; Kmat[-1, -1] -= kc
    return H.tocsr(), [ops(N, i) for i in range(nreg)], Kmat
def chi(S, k0, kc, sgn=1):
    H, X, Km = chain_H(S, k0, kc, sgn=sgn)
    w, v = spl.eigsh(H, k=1, which="SA", tol=1e-13); g = v[:, 0]; e0 = w[0]
    A = (H - e0 * sp.identity(H.shape[0])).tocsc()
    nr = len(X); C = np.zeros((nr, nr))
    for j in range(nr):
        r = X[j] @ g; r = r - g * (g @ r)
        y = spl.minres(A + 1e-14 * sp.identity(H.shape[0]), r, rtol=1e-13)[0]; y -= g * (g @ y)
        for i in range(nr):
            C[i, j] = 2 * (X[i] @ g) @ y
    return C, np.linalg.inv(Km)
def bmv(C):  # A at reg 0|1, B at reg 1|2 (equal unit sources): entangling combination of static energies
    return C[0, 1] + C[1, 2] - C[0, 2] - C[1, 1]
rows = []
for sn_t in (0.5, 0.8, 1.2, 1.8):
    kc = 0.5 / sn_t ** 4; k0 = 0.2 * kc     # local harmonic sigma_n ~ sn_t
    S = int(max(4, np.ceil(4 * sn_t + 2)))
    Cp, Kinv = chi(S, k0, kc, +1); Cm, _ = chi(S, k0, kc, -1)
    rows.append((sn_t, S, bmv(Cp) / bmv(Kinv), abs(Cp - Cm).max() / abs(Cp).max(), Cp[0, 2] / Kinv[0, 2]))
check("D", rows[-1][2] > 0.999 and rows[0][2] < 0.9 and max(r[3] for r in rows) < 1e-6,
      "B1 three hop registers on a chain with a supplied Regge-like quadratic phase: the static response and the "
      "BMV entangling phase equal the harmonic (continuous-edge) values once the per-register zero-point spread "
      "sigma_n exceeds ~1 value; below it the integer values pin the edges and the response is suppressed; both "
      "hop signs give the same response (A1)",
      "sigma_n, S, phase ratio, sign diff, far-pair ratio: " + "; ".join(f"{r[0]}, {r[1]}, {r[2]:.4f}, {r[3]:.0e}, {r[4]:.4f}" for r in rows))
def e0_single(S, k, f, J=1.0):
    m = np.arange(2 * S + 1) - S
    return np.linalg.eigvalsh(np.diag(0.5 * k * (m - f) ** 2) - J * (np.eye(2 * S + 1, k=1) + np.eye(2 * S + 1, k=-1)))[0]
pins = []
for sn in (0.8, 1.0, 1.2, 1.4):
    k = 0.5 / sn ** 4; Sx = int(max(12, 10 * sn))
    A_ = (e0_single(Sx, k, 0.5) - e0_single(Sx, k, 0.0)) / 2; pins.append((sn, 4 * np.pi ** 2 * A_ / k))
sl = np.polyfit([p[0] ** 2 for p in pins], [np.log(p[1]) for p in pins], 1)[0]
inst = 16.0   # WKB around the theta circle: 4 sqrt(8/k) = 16 sigma_n^2
check("T", -20 < sl < -9,
      "B2 the pinning: a single register's ground energy depends on the offset f of the phase minimum from the "
      "value lattice as -A cos(2 pi f); in the theta (edge-momentum) picture A is the instanton around the "
      "theta circle, action 16 sigma_n^2, so the pinning stiffness k_pin/k ~ exp(-16 sigma_n^2) (prefactor "
      "a power of sigma_n); discreteness corrections to Newton and BMV are exponential in sigma_n^2",
      "k_pin/k at sigma_n " + ", ".join(f"{p[0]}: {p[1]:.1e}" for p in pins) + f"; local slope d ln/d sigma^2 {sl:.1f} (WKB -{inst:.0f} + prefactor)")
# window walls: per-register spread fixed in rung units (physical), S -> infinity
def chi_lr(S, k, J=1.0):   # exact static susceptibility / harmonic 1/k
    m = np.arange(2 * S + 1) - S
    Hs = np.diag(0.5 * k * m ** 2) - J * (np.eye(2 * S + 1, k=1) + np.eye(2 * S + 1, k=-1))
    w, V = np.linalg.eigh(Hs); mel = V.T @ (m * V[:, 0])
    return 2 * np.sum(mel[1:] ** 2 / (w[1:] - w[0])) * k
wall = {(s1, Sx): chi_lr(Sx, 0.5 / (s1 * Sx) ** 4) for s1 in (0.2, 0.3, 0.45) for Sx in (16, 32, 64, 128)}
check("D", abs(wall[(0.2, 128)] - 1) < 1e-3 and abs(wall[(0.45, 128)] - wall[(0.45, 64)]) < 0.03
      and wall[(0.45, 128)] < 0.5,
      "B3 the window: a register spans one factor of two in length, so the per-register zero-point spread is a "
      "fixed fraction s1 = sigma_n/S = 2 sigma_l/l_rung of the half-window; raising S at fixed s1 removes the "
      "value lattice but not the walls, and the response tends to an S-independent value below the harmonic "
      "one: the large-S limit is a box, not the harmonic limit, unless s1 <~ 0.2 (walls at >~ 5 sigma)",
      "chi/chi_harm at S = 16/32/64/128: " + "; ".join(f"s1 {s1}: " + "/".join(f"{wall[(s1, Sx)]:.3f}" for Sx in (16, 32, 64, 128)) for s1 in (0.2, 0.3, 0.45)))

# ---------------------------------------------------------------- C. vacuum standard with a hop register
print("== C. zero-point force and the vacuum standard on a hop register (edge-source B3 toy)")
def zp_toy(S, M=50.0, K=50.0, w0=2.0, sub=True, sgn=1, nmat=12, qmax=0.5):
    h = qmax / S; q = h * (np.arange(2 * S + 1) - S); J = 1.0 / (2 * M * h * h)
    Hq = -sgn * J * hop(S) + sp.diags(0.5 * K * q ** 2)
    m = np.arange(nmat); ad = np.diag(np.sqrt(m[1:]), -1)
    xo = (ad + ad.T) / np.sqrt(2 * w0); po = 1j * np.sqrt(w0 / 2) * (ad - ad.T)
    P2 = np.real(po @ po.T.conj()); X2 = xo @ xo; wq = w0 / (1 + q)
    H = sp.kron(Hq, sp.identity(nmat)) + sp.kron(sp.identity(2 * S + 1), sp.csr_matrix(P2 / 2))
    H = H + sp.kron(sp.diags(wq ** 2 / 2), sp.csr_matrix(X2))
    if sub:
        H = H - sp.kron(sp.diags(wq / 2), sp.identity(nmat))
    w, v = np.linalg.eigh(H.toarray()); g = v[:, 0]
    return K * np.sum(g ** 2 * np.kron(q, np.ones(nmat)))
res = []
for Sx in (2, 4, 8, 16, 40):
    Fr, Fs, Fg = zp_toy(Sx, sub=False), zp_toy(Sx), zp_toy(Sx, sgn=-1)
    res.append((Sx, 0.2 * Sx, Fr, Fs / Fr, abs(Fg - Fs)))
R_bo = (1 / 400.) / (1 + 1 / 400.)
check("D", abs(res[-1][3] / R_bo - 1) < 0.1 and max(r[4] for r in res) < 1e-10 and res[-1][2] > 0.95,
      "C1 the vacuum standard subtracts a function of the edge value only, so it cancels the matter zero-point "
      "force exactly for any edge kinetic term; the residual edge-motion term is the hop's: it matches the "
      "Born-Oppenheimer 1/(8M) once sigma_n >~ 2 and is the same for both hop signs; edge-source's 'harmonic' "
      "grid (81 points on +-0.5) IS this hop register at S = 40, normal sign",
      "S, sigma_n, raw force, residual ratio, sign diff: " + "; ".join(f"{r[0]}, {r[1]:.1f}, {r[2]:.3f}, {r[3]:.2e}, {r[4]:.0e}" for r in res)
      + f"; BO {R_bo:.2e}")

# ---------------------------------------------------------------- D. tensor zero point and the edge cone
print("== D. zero-point normalisation, the edge cone and Bloch turning")
dz = []
for sn in (1.0, 2.0, 4.0, 8.0):
    k = 0.5 / sn ** 4; Sx = int(6 * sn + 6); m = np.arange(2 * Sx + 1) - Sx
    H = np.diag(0.5 * k * m ** 2) - (np.eye(2 * Sx + 1, k=1) + np.eye(2 * Sx + 1, k=-1))
    w, V = np.linalg.eigh(H); g = V[:, 0]
    var = g ** 2 @ m ** 2; cth = g @ np.roll(g, 1) if False else g[1:] @ g[:-1]
    dz.append((sn, (1 - var / sn ** 2) * 16 * sn ** 2, (1 - cth) * 8 * sn ** 2))
check("T", abs(dz[-1][1] - 1) < 0.05 and abs(dz[-1][2] - 1) < 0.05,
      "D1 the cosine band: a register's zero-point variance is the harmonic one times 1 - 1/(16 sigma_n^2) and "
      "its dressed hop <cos theta> = 1 - 1/(8 sigma_n^2): the hop corrections are POWER laws in 1/S (not "
      "exponential), so the tensor seed P_t = 2H^2/(pi^2 M_P^2) holds with a relative correction O(1/sigma_n^2) "
      "and the edge kinetic weight is dressed by the vacuum's own momentum spread",
      "sigma_n, 16 s^2 (1-var/harm), 8 s^2 (1-<cos>): " + "; ".join(f"{z[0]}, {z[1]:.3f}, {z[2]:.3f}" for z in dz))
# lattice estimate of <theta^2> per register from all modes of a 3D massless field: <x^2><p^2> per site
L = 24; kk = 2 * np.pi * np.arange(L) / L
kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
w = 2 * np.sqrt(np.sin(kx / 2) ** 2 + np.sin(ky / 2) ** 2 + np.sin(kz / 2) ** 2); w[0, 0, 0] = np.inf
x2 = np.mean(1 / (2 * w)); w[0, 0, 0] = 0; p2 = np.mean(w / 2); cprime = 4 * x2 * p2
del kx, ky, kz, w
# <theta^2> = h^2 <p^2> = cprime / (4 sigma_n^2); edge cone shift dc/c = -<theta^2>/4 with a bare weight
dc_bound = 3e-15
sig_need = np.sqrt(cprime / (16 * dc_bound))
check("E", sig_need > 1e6,
      "D2 ESTIMATE: with the hop weight fixed bare by the rung length, the field's own zero-point momentum "
      "spread dresses the edge kinetic weight by exp(-<theta^2>/2) and moves the graviton cone off the "
      "matter (edge-metric) cone by dc/c = -c'/(16 sigma_n^2); GW170817 (|dc/c| < 3e-15) then needs "
      "sigma_n > ~4e6, S > ~1e7; fixing the weight self-consistently (dressed, as CL-3 fixes the link "
      "coefficients) removes the mean-field shift",
      f"per-site 4<x^2><p^2> on a 3D lattice c' = {cprime:.2f}; sigma_n needed {sig_need:.1e}; "
      f"S needed at sigma_n = 0.4 S: {sig_need/0.4:.1e}")
# graviton/Newton pinning mass and the S needed vs measurement
lr_eV = 1.0 / (np.sqrt(32 * np.pi) * 1.616e-35) * 1.973e-7   # 1/l_rung in eV (Lam = 4 -> l_rung^2 = 32 pi l_P^2)
bounds = {"LIGO m_g < 1.3e-23 eV": 1.3e-23, "BMV range > 1 mm": 1.973e-7 / 1e-3}
need = {k_: np.sqrt(np.log(lr_eV / v) / 8.0) for k_, v in bounds.items()}   # m a ~ exp(-8 sigma^2)
check("E", 3 < need["LIGO m_g < 1.3e-23 eV"] < 5,
      "D3 ESTIMATE: the pinning (B2) gives the long-wavelength edge field a mass m l_rung ~ exp(-8 sigma_n^2) "
      "(square root of the stiffness), so Newton's law and the BMV phase are those of continuous edges inside "
      "range 1/m; the measured graviton-mass bound needs sigma_n >~ 3.7, i.e. S >~ 10 at sigma_n ~ 0.4 S; "
      "the BMV phase itself is the GR value G m^2 t/(hbar d) = 0.79 rad up to exp(-16 sigma_n^2)",
      f"1/l_rung {lr_eV:.1e} eV; sigma_n needed: " + ", ".join(f"{k_} {v:.2f}" for k_, v in need.items()))
# Bloch turning of the volume mode (constant force on a cosine band)
Lam = 4.0
def bloch_ok(Sx, u, l=1.0):
    return Sx ** 2 / (9 * Lam ** 2 * l * u ** 2) >= 1.0   # Bloch amplitude 4J/F >= one window
Smin = [min(s for s in range(1, 200) if bloch_ok(s, u)) for u in (0.1, 0.5, 0.7)]
# quantum check: wide packet at the band top (ghost sector) under a constant force turns after T_B
Sx = 150; Jq = 1.0; Fq = 0.05; m = np.arange(2 * Sx + 1)
H = np.diag(Fq * m * 1.0) - Jq * (np.eye(2 * Sx + 1, k=1) + np.eye(2 * Sx + 1, k=-1))
wq, Vq = np.linalg.eigh(H); psi = np.exp(-(m - 80.0) ** 2 / (2 * 6.0 ** 2) + 1j * np.pi * m); psi /= np.linalg.norm(psi)
TB = 2 * np.pi / Fq; mean = []
for t in np.linspace(0, TB, 41):
    ph = Vq @ (np.exp(-1j * wq * t) * (Vq.conj().T @ psi)); mean.append(np.abs(ph) ** 2 @ m)
amp = max(mean) - min(mean)
check("T", abs(mean[-1] - mean[0]) < 0.5 and abs(amp - 4 * Jq / Fq) / (4 * Jq / Fq) < 0.15,
      "D4 on a register the volume mode's constant force gives Bloch motion: a packet in the ghost (band-top) "
      "sector moves up the potential, turns after an excursion 4J/F and returns at T_B = 2 pi/(F h); "
      "the Friedmann orbit of volume-mode B2 needs the excursion to exceed the window, S >= 12 u sqrt(l)",
      f"excursion {amp:.1f} vs 4J/F {4*Jq/Fq:.0f}, return |dn| {abs(mean[-1]-mean[0]):.2f}; S_min at u = .1/.5/.7: {Smin}")

print("theorems: A1-A3, B2, D1, D4; diagnostics: B1, B3, C1; estimates: D2, D3")
print("supplied: Regge-like quadratic phase (B), matter toy (C), sigma_n ~ 0.4 S, 3D lattice c', GW170817/LIGO bounds")
print(f"elapsed_seconds {time.time()-t0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
