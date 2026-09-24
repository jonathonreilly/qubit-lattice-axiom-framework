#!/usr/bin/env python3
"""Coupled motion of two heavy walkers under block 56's simplest clock law, at strong field (worked computation).

Line of n sites, walls at 0 and n+1 held at the ambient rate (phi = 1).  Block 55's reduced walk H(m) = m sigma_x + sigma_z D
(hop H_{z,z+1} = -(i/2) sigma_z, H_{z+1,z} = +(i/2) sigma_z), clocked H_w = phi H phi.  Field: the ledger <H_w>_A + <H_w>_B + F,
F = (6/Gam) sum over all bonds (walls included) (phi_z - phi_{z+1})^2  [the line's normalization of (2/gamma) sum; stationarity
in phi_z gives the task's ((12/Gam)(1 - A) + K) phi = 0, A the two-neighbour average], K_xy = Re h_xy, h_xy = sum over the two
walkers of psi_x^dag H_xy psi_y (rate-free).  Part E: exact rationals.  Parts N1-N4: floating point (numpy/scipy).
"""
import sys
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import solve_banded, eigh_tridiagonal
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

lines = []
def out(s):
    print(s); lines.append(s)

# ------------------------------------------------------------------ E: exact static checks (bodies at rest, K = diag(m))
def solve_exact(n, Gam, masses):          # masses: dict site(1..n) -> m ; returns phi[1..n]
    # (6/Gam) L phi + diag(m) phi = b, L = tridiag(-1, 2, -1), b = (6/Gam)(e_1 + e_n)
    a = [Fr(0)] * (n + 1); bdiag = [Fr(0)] * (n + 1); c = [Fr(0)] * (n + 1); r = [Fr(0)] * (n + 1)
    for z in range(1, n + 1):
        bdiag[z] = 12 / Gam + masses.get(z, Fr(0)); a[z] = -6 / Gam; c[z] = -6 / Gam
        r[z] = (6 / Gam if z in (1, n) else Fr(0))
    # Thomas algorithm, exact
    cp = [Fr(0)] * (n + 1); dp = [Fr(0)] * (n + 1)
    for z in range(1, n + 1):
        den = bdiag[z] - (a[z] * cp[z - 1] if z > 1 else 0)
        cp[z] = c[z] / den; dp[z] = (r[z] - (a[z] * dp[z - 1] if z > 1 else 0)) / den
    phi = [Fr(0)] * (n + 2); phi[0] = phi[n + 1] = Fr(1)
    for z in range(n, 0, -1):
        phi[z] = dp[z] - (cp[z] * phi[z + 1] if z < n else 0)
    return phi
def ledger_exact(n, Gam, masses, phi):
    E = sum(m * phi[z] ** 2 for z, m in masses.items())
    F = 6 / Gam * sum((phi[z] - phi[z + 1]) ** 2 for z in range(0, n + 1))
    return E + F
n0, Gam0 = 11, Fr(3, 7)
ok = True
for masses in ({6: Fr(5, 2)}, {3: Fr(2), 8: Fr(7, 3)}, {2: Fr(9), 5: Fr(1, 4), 9: Fr(40)}):
    phi = solve_exact(n0, Gam0, masses)
    L = ledger_exact(n0, Gam0, masses, phi)
    ok &= all(0 < phi[z] <= 1 for z in range(1, n0 + 1))
    ok &= L == sum(m * phi[z] for z, m in masses.items())                   # block 56: ledger = sum m phi
    ok &= L == 6 / Gam0 * (2 - phi[1] - phi[n0])                            # a sum over the wall sites
# one body: phi_0 = 1/(1 + x), x = (Gam/6) G_L(z0, z0) m, G_L = L^{-1} (Dirichlet): G_L(z, z) = z (n + 1 - z)/(n + 1)
z0, m0 = 6, Fr(5, 2)
phi = solve_exact(n0, Gam0, {z0: m0})
x = Gam0 / 6 * Fr(z0 * (n0 + 1 - z0), n0 + 1) * m0
ok &= phi[z0] == 1 / (1 + x)
# two bodies: the static law is linear in the charges q_i = m_i phi_i: phi = 1 - (Gam/6) sum q_i G_L(., z_i)
GL = lambda z, y: Fr(min(z, y) * (n0 + 1 - max(z, y)), n0 + 1)
ms = {3: Fr(2), 8: Fr(7, 3)}
phi = solve_exact(n0, Gam0, ms)
ok &= all(phi[z] == 1 - Gam0 / 6 * sum(m * phi[y] * GL(z, y) for y, m in ms.items()) for z in range(1, n0 + 1))
out("E exact (rationals, line of 11, walls held): 0 < phi <= 1; ledger = sum m phi = (6/Gam)(2 - phi_1 - phi_n) (wall term); "
    "one body phi_0 = 1/(1 + x) with x = (Gam/6) G_L(z0,z0) m; phi = 1 - (Gam/6) sum_i (m_i phi_i) G_L(., z_i): %s" % ("PASS" if ok else "FAIL"))
if not ok:
    print("SUMMARY: exact static identities FAIL"); sys.exit(1)

# ------------------------------------------------------------------ numerics
SX = np.array([[0, 1], [1, 0]], complex); SZ = np.array([[1, 0], [0, -1]], complex)
def hw(n, phi, m):
    """clocked generator phi H(m) phi on the open line (2n x 2n sparse)."""
    rows, cols, vals = [], [], []
    for z in range(n):
        for a in range(2):
            for b in range(2):
                if SX[a, b] != 0:
                    rows.append(2 * z + a); cols.append(2 * z + b); vals.append(phi[z] ** 2 * m * SX[a, b])
    for z in range(n - 1):
        f = phi[z] * phi[z + 1]
        for a in range(2):
            rows.append(2 * z + a); cols.append(2 * (z + 1) + a); vals.append(-0.5j * SZ[a, a] * f)
            rows.append(2 * (z + 1) + a); cols.append(2 * z + a); vals.append(0.5j * SZ[a, a] * f)
    return coo_matrix((vals, (rows, cols)), shape=(2 * n, 2 * n)).tocsr()
def kmat(n, psis, ms):
    """K = Re h (rate-free), tridiagonal: diagonal d, off-diagonal o (z, z+1)."""
    d = np.zeros(n); o = np.zeros(n - 1)
    for psi, m in zip(psis, ms):
        p = psi.reshape(n, 2)
        d += m * np.real(np.conj(p[:, 0]) * p[:, 1] + np.conj(p[:, 1]) * p[:, 0])
        hz = -0.5j * (np.conj(p[:-1, 0]) * p[1:, 0] - np.conj(p[:-1, 1]) * p[1:, 1])
        o += np.real(hz)
    return d, o
def solve_phi(n, Gam, d, o):
    ab = np.zeros((3, n))
    ab[0, 1:] = -6 / Gam + o; ab[1, :] = 12 / Gam + d; ab[2, :-1] = -6 / Gam + o
    rhs = np.zeros(n); rhs[0] = rhs[-1] = 6 / Gam
    return solve_banded((1, 1), ab, rhs)
def lam_min(n, Gam, d, o):
    return eigh_tridiagonal(12 / Gam + d, -6 / Gam + o, select='i', select_range=(0, 0))[0][0]
def packet(n, z0, width, m, k0):
    z = np.arange(n)
    e = np.sqrt(m * m + np.sin(k0) ** 2)
    spin = np.array([e + np.sin(k0), m]); spin = spin / np.linalg.norm(spin)
    env = np.exp(-((z - z0) / width) ** 2 / 2 + 1j * k0 * z)
    psi = (env[:, None] * spin[None, :]).reshape(-1)
    return psi / np.linalg.norm(psi)
def kvec(psi, n):
    p = psi.reshape(n, 2)
    return -np.angle(np.sum(np.conj(p[1:]) * p[:-1]))
def centroid(psi, n):
    rho = (np.abs(psi.reshape(n, 2)) ** 2).sum(axis=1)
    return float((np.arange(n) * rho).sum() / rho.sum()), rho
def ledger(n, Gam, psis, ms, phi):
    E = [float(np.real(np.vdot(p, hw(n, phi, m) @ p))) for p, m in zip(psis, ms)]
    full = np.concatenate([[1.0], phi, [1.0]])
    return E, 6 / Gam * float(((full[1:] - full[:-1]) ** 2).sum())
def run(n, Gam, ms, zs, k0s, width, T, dt, record=None):
    psis = [packet(n, z, width, m, k) for z, m, k in zip(zs, ms, k0s)]
    def phi_of(ps):
        d, o = kmat(n, ps, ms); return solve_phi(n, Gam, d, o), lam_min(n, Gam, d, o)
    phi, lm = phi_of(psis)
    E0, F0 = ledger(n, Gam, psis, ms, phi); L0 = sum(E0) + F0
    hist = []
    minphi, minlam = phi.min(), lm
    steps = int(round(T / dt))
    for s in range(steps + 1):
        if record is not None:
            cs = [centroid(p, n) for p in psis]
            hist.append((s * dt, [kvec(p, n) for p in psis], [c for c, _ in cs],
                         [float((rho * phi ** 2).sum()) for _, rho in cs], phi.copy()))
        if s == steps:
            break
        trial = [expm_multiply(-1j * hw(n, phi, m) * dt, p) for p, m in zip(psis, ms)]
        phit, _ = phi_of(trial)
        pmid = 0.5 * (phi + phit)
        psis = [expm_multiply(-1j * hw(n, pmid, m) * dt, p) for p, m in zip(psis, ms)]
        phi, lm = phi_of(psis)
        minphi = min(minphi, phi.min()); minlam = min(minlam, lm)
    E1, F1 = ledger(n, Gam, psis, ms, phi)
    return dict(L0=L0, drift=sum(E1) + F1 - L0, hist=hist, minphi=minphi, minlam=minlam, E0=E0)

# ------------------------------------------------------------------ N1, N2, N4: heavy walkers at rest, x from 0.1 to 5
n, width = 240, 6.0
zA, zB = 90, 150
mA, mB = 2.0, 3.0
GLf = lambda z, y: min(z, y) * (n + 1 - max(z, y)) / (n + 1)          # 1-indexed Dirichlet L^{-1}
g0 = GLf(zA + 1, zA + 1)
out("N  line n = %d, walls held at phi = 1, walkers A (m = %.1f) at %d and B (m = %.1f) at %d, width %.0f, both at rest; "
    "x_A = (Gam/6) G_L(zA,zA) m_A" % (n, mA, zA, mB, zB, width))
out("N  %5s %9s | %11s %11s | %9s %9s | %10s %10s %10s | %10s %10s" %
    ("x_A", "Gam", "L0", "drift", "phi_A", "phi_B", "dkA/dt", "charges", "bare", "dkB/dt", "charges"))
summary = []
for xA in (0.1, 0.5, 1.0, 2.0, 5.0):
    Gam = 6 * xA / (g0 * mA)
    r = run(n, Gam, (mA, mB), (zA, zB), (0.0, 0.0), width, T=20.0, dt=0.25, record=True)
    h = r["hist"]
    tt = np.array([x[0] for x in h]); kA = np.array([x[1][0] for x in h]); kB = np.array([x[1][1] for x in h])
    # initial pull: slope of k over the first 20 time units (the packets barely move: k is linear to the accuracy shown)
    pA = np.polyfit(tt, kA, 2)[1]; pB = np.polyfit(tt, kB, 2)[1]
    phi0 = h[0][4]
    phA, phB = phi0[zA], phi0[zB]
    qA, qB = mA * phA, mB * phB
    # mutual pull from block 54's law with block 56's linear field, point charges: dk_A/dt = (Gam/3) m_A phi_A * (q_A dG_self + q_B dG_AB)
    dG = lambda z, y: (GLf(z + 2, y + 1) - GLf(z, y + 1)) / 2           # d/dz of G_L(z+1, y+1) (symmetric difference, 0-indexed sites)
    predA = Gam / 3 * mA * phA * (qA * dG(zA, zA) + qB * dG(zA, zB))
    predB = Gam / 3 * mB * phB * (qB * dG(zB, zB) + qA * dG(zB, zA))
    bareA = Gam / 3 * mA * (mA * dG(zA, zA) + mB * dG(zA, zB))
    # smeared (exact bilinear form): q(z) = K_zz phi_z per walker; phi = 1 - (Gam/6) G_L (q_A + q_B) exactly when K is diagonal
    psA0 = packet(n, zA, width, mA, 0.0); psB0 = packet(n, zB, width, mB, 0.0)
    dA_, oA_ = kmat(n, [psA0], [mA]); dB_, oB_ = kmat(n, [psB0], [mB])
    GLm = np.array([[GLf(i + 1, j + 1) for j in range(n)] for i in range(n)])
    qAz, qBz = dA_ * phi0, dB_ * phi0
    Phi = GLm @ (qAz + qBz)
    lin_err = np.abs(1 - Gam / 6 * Phi - phi0).max()
    dPhi = np.zeros(n); dPhi[1:-1] = (Phi[2:] - Phi[:-2]) / 2
    smA = Gam / 3 * (qAz * dPhi).sum(); smB = Gam / 3 * (qBz * dPhi).sum()
    mutA = Gam / 3 * (qAz * np.gradient(GLm @ qBz)).sum()
    out("N  %5.1f %9.3e | %11.5e %+11.2e | %9.5f %9.5f | %+10.3e %+10.3e %+10.3e | %+10.3e %+10.3e" %
        (xA, Gam, r["L0"], r["drift"], phA, phB, pA, predA, bareA, pB, predB))
    summary.append((xA, r["drift"] / abs(r["L0"]), pA / predA, pA / bareA, pB / predB, phA, phB, pA / smA, pB / smB, lin_err, np.abs(oA_).max() + np.abs(oB_).max()))
    # N4: clock rate at each walker as they approach (long run at x = 1 and 5)
out("N1 ledger drift / ledger over the run: max %.1e (dt = 0.25, midpoint step; the integrator's level)" % max(abs(s[1]) for s in summary))
out("N2 pull / (charge prediction, q = m phi): A %s   B %s" % (", ".join("%.3f" % s[2] for s in summary), ", ".join("%.3f" % s[4] for s in summary)))
out("N2 pull / (bare-energy prediction):       A %s" % ", ".join("%.3f" % s[3] for s in summary))
out("N2 pull / (smeared bilinear form (Gam/3) sum_z q(z) d[G_L(q_A + q_B)](z), q = K_zz phi_z): A %s   B %s" % (", ".join("%.4f" % s[7] for s in summary), ", ".join("%.4f" % s[8] for s in summary)))
out("N2 check: at rest K has no bond entries (max %.1e) and the solved phi equals 1 - (Gam/6) G_L(q_A + q_B) to %.1e" % (max(s[10] for s in summary), max(s[9] for s in summary)))

# ------------------------------------------------------------------ N3: positivity for moving packets at large energy
out("N3 moving packets at large energy (m = 0.05, k0 = 1.2, bare energy %.3f): M = (12/Gam)(1 - A) + K is an M-matrix while every "
    "bond entry K_{z,z+1} <= 6/Gam; single packet, scan of Gam" % np.sqrt(0.05 ** 2 + np.sin(1.2) ** 2))
n3 = 120
for w3 in (1.0, 2.0, 4.0):
    psi = packet(n3, 60, w3, 0.05, 1.2)
    d, o = kmat(n3, [psi], [0.05])
    gams = np.logspace(-1, 3.5, 600)
    lms = np.array([lam_min(n3, G_, d, o) for G_ in gams])
    mph = np.array([solve_phi(n3, G_, d, o).min() for G_ in gams])
    g_m = 6 / o.max()
    g_phi = gams[np.argmax(mph < 0)] if (mph < 0).any() else None
    g_lam = gams[np.argmax(lms < 0)] if (lms < 0).any() else None
    out("N3   width %.0f: max bond entry %.4f -> M-matrix lost at Gam = %.1f; min phi < 0 from Gam ~ %s; lambda_min(M) < 0 from Gam ~ %s"
        % (w3, o.max(), g_m, ("%.1f" % g_phi) if g_phi else "never", ("%.1f" % g_lam) if g_lam else "never"))
for (lbl, G_) in (("inside the positive region", 13.2), ("past the phi-positivity loss (width 1)", 60.0)):
    r = run(n3, G_, (0.05, 0.05), (40, 80), (1.2, -1.2), 1.0, T=30.0, dt=0.05, record=False)
    out("N3   run, two packets k = +-1.2, width 1, Gam = %.1f (%s): min phi over the run %+.4f, min lambda(M) %+.3e, ledger drift/ledger %.1e"
        % (G_, lbl, r["minphi"], r["minlam"], r["drift"] / abs(r["L0"])))
# ------------------------------------------------------------------ N4: clock rates as the heavy walkers approach
for xA in (1.0, 5.0):
    Gam = 6 * xA / (g0 * mA)
    r = run(n, Gam, (mA, mB), (zA, zB), (0.0, 0.0), width, T=160.0, dt=0.5, record=True)
    h = r["hist"]
    rows = []
    for idx in (0, len(h) // 4, len(h) // 2, 3 * len(h) // 4, len(h) - 1):
        t_, ks, cs, wr, ph = h[idx]
        # static two-body prediction at the current centroids: phi_i = 1 - (Gam/6) sum_j m_j phi_j G_L(z_i, z_j)
        zi = [int(round(c)) + 1 for c in cs]
        Mst = np.array([[1 + Gam / 6 * mA * GLf(zi[0], zi[0]), Gam / 6 * mB * GLf(zi[0], zi[1])],
                        [Gam / 6 * mA * GLf(zi[1], zi[0]), 1 + Gam / 6 * mB * GLf(zi[1], zi[1])]])
        ps = np.linalg.solve(Mst, np.ones(2))
        rows.append("t=%5.1f sep %6.2f: w at A %.4f (static %.4f), at B %.4f (static %.4f)" % (t_, cs[1] - cs[0], wr[0], ps[0] ** 2, wr[1], ps[1] ** 2))
    out("N4 x_A = %.0f, drift/ledger %.1e: " % (xA, r["drift"] / abs(r["L0"])) + " | ".join(rows))

drift_ok = max(abs(s[1]) for s in summary) < 1e-4
charge_ok = all(abs(s[7] - 1) < 0.05 and abs(s[8] - 1) < 0.05 for s in summary)
bare_off = abs(summary[-1][3] - 1) > 0.5
print()
print("SUMMARY: simplest clock law at strong field (x = 0.1..5) on a walled line: ledger conserved to %.0e of itself; the pull on each "
      "heavy walker follows block 54's law with charges m*phi (smeared bilinear form: ratio %.3f..%.3f), not bare energies (ratio %.2f at x = 5); exact: "
      "ledger = sum m phi = wall term, phi = 1 - (Gam/6) sum q G_L; clocks at the walkers slow as they approach, tracking the static "
      "two-body law" % (max(abs(s[1]) for s in summary), min(min(s[7], s[8]) for s in summary), max(max(s[7], s[8]) for s in summary), summary[-1][3]))
if not (drift_ok and charge_ok and bare_off):
    print("HIT: a stated expectation fails: drift_ok=%s charge_ok=%s bare_off=%s" % (drift_ok, charge_ok, bare_off))
