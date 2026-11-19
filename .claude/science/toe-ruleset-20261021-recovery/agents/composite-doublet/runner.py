#!/usr/bin/env python3
"""Can the Y = 1/2 doublet CL-3 would set be a fermion-pair composite of the rules' own dynamics?

Supplied model: one Weyl 16 of Spin(10) per family (Pati-Salam halves psi = (4,2,1), chi = (4b,1,2)), the register's
four-mode terms, the lattice cone E = 2 sqrt(sum sin^2(k_i/2)) (one cone, cell units a = 1), one-loop SM running.
Sections:
 A  pair channels (exact Clifford algebra): which four-mode terms hold a colourless Y = 1/2 doublet pair; vacuum alignment
 B  NJL gap equation on the lattice cone: critical coupling, O(1) coupling, tuning needed for m/M = 1e-17
 C  top-type condensation with measured couplings: compositeness (Pagels-Stokar, multi-channel), one-loop BHL running
 D  the scalar spectrum and electroweak fits against measurement
Finite diagnostics of supplied models; no physical identification.  Cited, not rederived: Bardeen-Hill-Lindner (1990),
Pagels-Stokar, Peskin vacuum alignment sign, the Peskin-Takeuchi heavy-doublet S, PDG values."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import null_space

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ---------------------------------------------------------------- A. Clifford algebra of Spin(10)
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1])
def kron(*a):
    out = np.array([[1.0 + 0j]])
    for x in a: out = np.kron(out, x)
    return out
G = []
for k in range(5):
    pre = [s3] * k; post = [s0] * (4 - k)
    G.append(kron(*pre, s1, *post)); G.append(kron(*pre, s2, *post))
G = [g.astype(complex) for g in G]
cliff = max(np.abs(G[a] @ G[b] + G[b] @ G[a] - 2 * (a == b) * np.eye(32)).max() for a in range(10) for b in range(10))
P = np.eye(32, dtype=complex)
for g in G: P = P @ g
G11 = P * (1j ** 5)                                  # (i)^5 G1..G10, squares to 1
if np.abs(G11 @ G11 - np.eye(32)).max() > 1e-12: G11 = -1j * G11 if np.abs((-1j * P) @ (-1j * P) - np.eye(32)).max() < 1e-12 else G11
w, U = np.linalg.eigh((G11 + G11.conj().T) / 2)
V = U[:, w > 0]                                     # the 16
Sig = {(i, j): 0.25j * (G[i] @ G[j] - G[j] @ G[i]) for i in range(10) for j in range(i + 1, 10)}
gen16 = {k: V.conj().T @ s @ V for k, s in Sig.items()}
# charge conjugation: try both products of five gammas; keep the one whose pairs c^T (C G_a) c land in 16 x 16
best = None
for idx in ([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]):
    C = np.eye(32, dtype=complex)
    for i in idx: C = C @ G[i]
    M = [V.T @ C @ G[a] @ V for a in range(10)]
    nrm = sum(np.abs(m).sum() for m in M)
    if best is None or nrm > best[0]: best = (nrm, C, M)
_, C, M = best
sym = max(np.abs(m - m.T).max() for m in M); uni = max(np.abs(m @ m.conj().T - np.eye(16)).max() for m in M)
# covariance: t^T M_c + M_c t = i(d_ac M_b - d_bc M_a) for t = Sigma_ab
cov = 0.0
for (a, b), t in gen16.items():
    for c in range(10):
        lhs = t.T @ M[c] + M[c] @ t
        rhs = 1j * ((a == c) * M[b] - (b == c) * M[a])
        cov = max(cov, min(np.abs(lhs - rhs).max(), np.abs(lhs + rhs).max()))
check('A1 [T] Cl(10) built (32 x 32); the 16 pair c^T M_a c with M_a = (C G_a)|16 is symmetric, unitary and a Spin(10) vector: '
      'the pair square g sum_a B_a B_a + h.c. has exactly one pair channel, the 10 (Hubbard-Stratonovich of a dN = 4 term holds '
      'only dN = 2 pair fields; no particle-hole channel exists)', cliff < 1e-12 and sym < 1e-12 and uni < 1e-12 and cov < 1e-12,
      f'clifford {cliff:.0e}, sym {sym:.0e}, unitary {uni:.0e}, covariance {cov:.0e}')

# Pati-Salam halves: so(4) chirality G7 G8 G9 G10 on the 16
Q4 = V.conj().T @ (G[6] @ G[7] @ G[8] @ G[9]) @ V
Q4 = Q4 / np.sqrt((Q4 @ Q4)[0, 0])
q, Uq = np.linalg.eigh((Q4 + Q4.conj().T) / 2)
Ppsi = Uq[:, q > 0]; Pchi = Uq[:, q < 0]
def blocks(m):
    return (np.abs(Ppsi.T @ m @ Ppsi).max(), np.abs(Ppsi.T @ m @ Pchi).max(), np.abs(Pchi.T @ m @ Pchi).max())
bd = [blocks(M[a]) for a in range(10)]
off_only = all(b[0] < 1e-12 and b[2] < 1e-12 and b[1] > 0.5 for b in bd[6:])
diag_only = all(b[1] < 1e-12 and (b[0] > 0.5 or b[2] > 0.5) for b in bd[:6])
check('A2 [T] the 10 splits as (6,1,1) + (1,2,2): the four so(4)-vector pairs M_7..M_10 join psi = (4,2,1) only to chi = (4b,1,2), '
      'the six so(6)-vector pairs join psi-psi and chi-chi only: the doublet channel is the psi chi (q u^c, q d^c, L e^c, L n^c) pair',
      off_only and diag_only and Ppsi.shape[1] == 8 == Pchi.shape[1],
      f'(psi psi, psi chi, chi chi) max |M_7| = {bd[6][0]:.0e}, {bd[6][1]:.2f}, {bd[6][2]:.0e}; |M_1| = {bd[0][0]:.2f}, {bd[0][1]:.0e}, {bd[0][2]:.2f}')

# colourless pair tensors in psi x psi, chi x chi, psi x chi (invariance under so(6))
so6 = [k for k in gen16 if k[0] < 6 and k[1] < 6]; so4 = [k for k in gen16 if k[0] >= 6]
def inv_dim(PA, PB, keys):
    rows = []
    for k in keys:
        tA = PA.conj().T @ gen16[k] @ PA; tB = PB.conj().T @ gen16[k] @ PB
        # pair c_A^T T c_B -> T' = tA^T T + T tB
        rows.append(np.kron(tA.T, np.eye(tB.shape[0])) + np.kron(np.eye(tA.shape[0]), tB.T))
    return null_space(np.vstack(rows)).shape[1]
d_pp, d_cc, d_pc = inv_dim(Ppsi, Ppsi, so6), inv_dim(Pchi, Pchi, so6), inv_dim(Ppsi, Pchi, so6)
check('A3 [T] colour (so(6) = SU(4)) singlet pairs: psi x psi 0, chi x chi 0, psi x chi 4 = (1,2,2): any four-mode term built '
      'inside one Pati-Salam half (the rung-1 tetrahedral top form, uude, uddn, which act inside one cell multiplet) has no '
      'colourless pair channel, so no Y = 1/2 doublet after any Fierz rearrangement', (d_pp, d_cc, d_pc) == (0, 0, 4),
      f'dims {d_pp}, {d_cc}, {d_pc}')

# quantum numbers of the channels in the vector representation
def L(i, j):
    m = np.zeros((10, 10), complex); m[i, j] = 1; m[j, i] = -1; return 1j * m
T3L = (L(6, 7) + L(8, 9)) / 2; T3R = (L(6, 7) - L(8, 9)) / 2; BL = (2 / 3) * (L(0, 1) + L(2, 3) + L(4, 5))
Y = T3R + BL / 2
Hs = T3L + 7.1 * T3R + 3.3 * BL                      # generic combination: joint eigenbasis
_, E = np.linalg.eigh(Hs)
qn = sorted({(round(float(np.real(E[:, i].conj() @ T3L @ E[:, i])), 6), round(float(np.real(E[:, i].conj() @ Y @ E[:, i])), 6),
              round(float(np.real(E[:, i].conj() @ BL @ E[:, i])), 6)) for i in range(10)})
dbl = [x for x in qn if abs(x[0]) == 0.5]; trip = [x for x in qn if x[0] == 0]
ok = sorted(dbl) == sorted([(-0.5, -0.5, 0.0), (-0.5, 0.5, 0.0), (0.5, -0.5, 0.0), (0.5, 0.5, 0.0)]) and \
     np.allclose(sorted({t[1] for t in trip}), [-1 / 3, 1 / 3], atol=1e-5) and sorted({round(t[0] + t[1], 6) for t in dbl}) == [-1.0, 0.0, 1.0]
check('A4 [T] (1,2,2): (T3L, Y) = (+-1/2, +-1/2), B - L = 0, Q = T3L + Y in {1, 0, 0, -1}: as a real 10 it is exactly one complex '
      'colourless doublet of hypercharge 1/2 with an EM-neutral direction; (6,1,1) is a colour-triplet pair with Y = -+1/3',
      ok, f'doublet (T3L, Y, B-L) {dbl}; triplet Y {sorted({t[1] for t in trip})}')

# vacuum alignment and the W_L / W_R mass matrix
Lv = [L(i, j) for i in range(10) for j in range(i + 1, 10) if (i < 6 and j < 6) or (i >= 6 and j >= 6)]
def cost(phi): return sum(np.linalg.norm(l @ phi) ** 2 for l in Lv)
e = np.eye(10)
c_d, c_t = cost(e[6]), cost(e[0])
rng = np.random.default_rng(7)
mix = [cost(np.cos(a) * e[6] + np.sin(a) * e[0]) for a in np.linspace(0, np.pi / 2, 7)]
TL = [(L(6, 7) + L(8, 9)) / 2, (L(6, 8) - L(7, 9)) / 2, (L(6, 9) + L(7, 8)) / 2]
TR = [(L(6, 7) - L(8, 9)) / 2, (L(6, 8) + L(7, 9)) / 2, (L(6, 9) - L(7, 8)) / 2]
alg = max(np.abs(TL[0] @ TL[1] - TL[1] @ TL[0] - 1j * TL[2]).max(), np.abs(TL[0] @ TR[1] - TR[1] @ TL[0]).max())
if alg > 1e-12:
    TL[2] = -TL[2]; TR[2] = -TR[2]
alg = max(np.abs(TL[0] @ TL[1] - TL[1] @ TL[0] - 1j * TL[2]).max(), np.abs(TL[0] @ TR[1] - TR[1] @ TL[0]).max())
zeros = []
for _ in range(5):
    gL, gR = rng.uniform(0.3, 1.5, 2)
    phi = rng.normal(size=10) * np.r_[np.zeros(6), np.ones(4)]; phi /= np.linalg.norm(phi)
    T = [gL * t for t in TL] + [gR * t for t in TR]
    M2 = np.real(np.array([[phi @ (a.conj().T @ b) @ phi for b in T] for a in T]))
    zeros.append(int(np.sum(np.linalg.eigvalsh((M2 + M2.T) / 2) < 1e-12)))
check('A5 [T] alignment: with equal Pati-Salam couplings the gauge mass-squared trace is 3 for a doublet-direction pair vev and '
      '5 for a triplet-direction one, rising monotonically between; gauge loops (positive Tr M^2, cited) align the 10 condensate '
      'onto the doublet. But a (1,2,2) vev always keeps SU(2)_L+R: for every g_L, g_R three link directions stay massless, '
      'so with SU(2)_R linked it gives massless charged links unless SU(2)_R is broken by a channel the pair square lacks',
      abs(c_d - 3) < 1e-12 and abs(c_t - 5) < 1e-12 and all(np.diff(mix) > -1e-12) and alg < 1e-12 and set(zeros) == {3},
      f'trace doublet {c_d:.3f}, triplet {c_t:.3f}; massless directions over 5 random (g_L, g_R, vev) {zeros}')

# ---------------------------------------------------------------- B. NJL gap equation on the lattice cone
def fib(n):
    i = np.arange(n) + 0.5; z = 1 - 2 * i / n; r = np.sqrt(1 - z * z); ph = np.pi * (1 + 5 ** 0.5) * i
    return np.c_[r * np.cos(ph), r * np.sin(ph), z]
DIR = fib(1600); RMAX = np.pi / np.abs(DIR).max(1)
xg, wg = np.polynomial.legendre.leggauss(240)
def radial(fun, lo):
    """(1/(2pi)^3) * integral over the Brillouin cube of fun(k, E0) in log-radial variables, exact cube boundary."""
    s_lo = np.log(lo); s_hi = np.log(RMAX)[:, None]
    s = s_lo + (s_hi - s_lo) * (xg[None, :] + 1) / 2; ws = (s_hi - s_lo) / 2 * wg[None, :]
    k = np.exp(s); kv = k[:, :, None] * DIR[:, None, :]
    E0 = 2 * np.sqrt((np.sin(kv / 2) ** 2).sum(-1))
    val = (fun(k, E0) * k ** 3 * ws).sum(1)
    return 4 * np.pi * val.mean() / (2 * np.pi) ** 3
I0 = radial(lambda k, E0: 1 / E0, 1e-9)
def I(m): return I0 - D(m)
def D(m): return radial(lambda k, E0: (1 / E0 - 1 / np.sqrt(E0 ** 2 + m * m)), m * 1e-7)
Rb = (3 / (4 * np.pi)) ** (1 / 3) * 2 * np.pi
I0_ball = 4 * np.pi * Rb ** 2 / 2 / (2 * np.pi) ** 3
I0_cont_cube = radial(lambda k, E0: 1 / k, 1e-9)
Nc = 3
Gc = 1 / (4 * Nc * I0)
check('B1 [F] gap equation m = 4 N_c G m I(m), I(m) = int_BZ d^3k/(2pi)^3 / sqrt(E0^2 + m^2) (4-component Dirac, mean field): '
      f'I0 = {I0:.5f} (the same cube with E0 = |k|: {I0_cont_cube:.5f}, ball of BZ volume: {I0_ball:.5f}); critical coupling '
      f'G_c = 1/(4 N_c I0) = {Gc:.4f} a^2 for N_c = 3, {3 * Gc:.4f} a^2 for N_c = 1', abs(I0_cont_cube - I0) / I0 < 0.5 and I0 > 0,
      f'angular nodes {len(DIR)}, radial nodes {len(xg)}')

def m_of_G(Gv):
    if 1 / Gv >= 4 * Nc * I0: return 0.0
    lo, hi = 1e-12, 50.0
    for _ in range(80):
        mid = np.sqrt(lo * hi)
        if 4 * Nc * I(mid) > 1 / Gv: lo = mid
        else: hi = mid
    return np.sqrt(lo * hi)
mG = {g: m_of_G(g) for g in (0.1, 0.5, 1.0, 2.0)}
check('B2 [F] with the supplied rule-size coupling G = O(1) a^2 the channel is above critical and the gap is cell-sized: '
      + ', '.join(f'G = {g}: m = {mG[g]:.3f}/a' for g in mG) + '; below G_c the light state stays massless: neither gives v/M ~ 1e-17',
      mG[0.1] == 0.0 and all(mG[g] > 0.1 for g in (0.5, 1.0, 2.0)), f'G_c = {Gc:.4f}')

ms = np.array([1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4])
dl = np.array([D(m) / I(m) for m in ms])          # (G - G_c)/G_c at which the gap is m
lead = ms ** 2 / (4 * np.pi ** 2 * I0)
Cfit = dl / lead - np.log(1 / ms)
ratio_cont = dl[-1] / (lead[-1] * np.log(1 / ms[-1]))
mt = 1e-17; d17 = mt ** 2 / (4 * np.pi ** 2 * I0) * (np.log(1 / mt) + Cfit[-1])
check('B3 [T/F] near criticality (G - G_c)/G_c = (m^2 / (4 pi^2 I0)) (ln(1/m) + C): the lattice fit settles '
      f'(C = {Cfit[-3]:.3f}, {Cfit[-2]:.3f}, {Cfit[-1]:.3f} at m = 1e-3, 3e-4 ...) so a gap m/M = 1e-17 needs '
      f'(G - G_c)/G_c = {d17:.1e}: quadratic sensitivity, the hierarchy restated as a tuning of the four-mode coefficient',
      abs(Cfit[-1] - Cfit[-2]) < 0.05 and 1e-34 < d17 < 1e-31, ' '.join(f'{m:.0e}:{d:.2e}' for m, d in zip(ms, dl)))

# ---------------------------------------------------------------- C. top-type condensation, measured inputs
MZ, v = 91.1876, 246.22
aS, ainv, s2w = 0.1180, 127.95, 0.2312
mt_pole, mH, mb, mtau, mc = 172.6, 125.1, 4.18, 1.777, 1.27
yt_meas = 0.936                                     # MSbar y_t(m_t), PDG-level
lam_meas = mH ** 2 / (2 * v ** 2)
e2 = 4 * np.pi / ainv
g2Z, gpZ, g3Z = np.sqrt(e2 / s2w), np.sqrt(e2 / (1 - s2w)), np.sqrt(4 * np.pi * aS)
b = np.array([41 / 6, -19 / 6, -7.0])
def gauge(mu):
    t = np.log(mu / MZ)
    g0 = np.array([gpZ, g2Z, g3Z])
    return 1 / np.sqrt(1 / g0 ** 2 - 2 * b * t / (16 * np.pi ** 2))
def rge(t, y):
    yt, lam = y; gp, g2, g3 = gauge(np.exp(t))
    k = 1 / (16 * np.pi ** 2)
    dy = k * yt * (4.5 * yt ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2 - 17 / 12 * gp ** 2)
    dl = k * (24 * lam ** 2 - 6 * yt ** 4 + 12 * lam * yt ** 2 - 3 * lam * (3 * g2 ** 2 + gp ** 2)
              + 3 / 8 * (2 * g2 ** 4 + (g2 ** 2 + gp ** 2) ** 2))
    return [dy, dl]
def bhl(Lam, y0=20.0, r=1.0):
    sol = solve_ivp(rge, [np.log(Lam), np.log(mt_pole)], [y0, r * y0 ** 2], rtol=1e-9, atol=1e-11, method='LSODA')
    return sol.y[0, -1], sol.y[1, -1]
# Pagels-Stokar (bubble, no gauge running)
def ps_m(Lam, w=1.0):
    lo, hi = 1e-3, 1e4
    for _ in range(100):
        m = np.sqrt(lo * hi)
        if w * 3 * m ** 2 * np.log(Lam ** 2 / m ** 2) / (4 * np.pi ** 2) > v ** 2: hi = m
        else: lo = m
    return m
Lams = [5e3, 1e6, 1e10, 1e15, 2.435e18]
rows = []
for Lam in Lams:
    yt, lam = bhl(Lam)
    rows.append((Lam, yt, yt * v / np.sqrt(2) * (1 + 4 * aS / (3 * np.pi)), np.sqrt(2 * max(lam, 0)) * v, 2 * ps_m(Lam)))
y_alt = [bhl(2.435e18, y0, r)[0] for y0, r in ((8.0, 1.0), (20.0, 0.5), (40.0, 2.0))]
spread = (max(y_alt) - min(y_alt)) / np.mean(y_alt)
print('   one-loop compositeness running (y_t, lambda -> large at Lambda), predicted vs measured y_t(m_t) = 0.936, m_t = 172.6, m_H = 125.1:')
for Lam, yt, mtp, mHp, mbub in rows:
    print(f'   Lambda = {Lam:8.1e} GeV: y_t(m_t) = {yt:.3f}, m_t ~ {mtp:5.0f} GeV, m_H ~ {mHp:5.0f} GeV (bubble 2m = {mbub:4.0f})')
check('C1 [E/M] BHL top condensation, measured gauge couplings: the infrared quasi-fixed point makes the prediction insensitive to '
      f'the boundary values (spread {spread:.1e}) and at every cutoff up to the cell y_t(m_t) >= {rows[-1][1]:.3f} vs 0.936, '
      f'm_t >= {rows[-1][2]:.0f} GeV vs 172.6 and m_H >= {rows[-1][3]:.0f} vs 125.1; a lower (coarse-rung) cutoff makes both worse',
      spread < 0.02 and all(r[1] > 1.05 * yt_meas for r in rows) and all(r[3] > 1.4 * mH for r in rows)
      and rows[0][2] > rows[-1][2], f'cutoffs {Lams[0]:.0e}..{Lams[-1]:.2e} GeV')

# multi-channel: sum_i N_ci m_i^2 ln(Lam^2/m_i^2) = 4 pi^2 v^2 (bubble)
Lam = 2.435e18
def mt_multi(ratios):
    lo, hi = 1e-3, 1e4
    for _ in range(100):
        m = np.sqrt(lo * hi)
        tot = sum(Nci * (m * rr) ** 2 * np.log(Lam ** 2 / (m * rr) ** 2) for Nci, rr in ratios)
        if tot > 4 * np.pi ** 2 * v ** 2: hi = m
        else: lo = m
    return m
m1 = mt_multi([(3, 1.0)])
mmeas = mt_multi([(3, 1.0), (3, mb / mt_pole), (1, mtau / mt_pole), (3, mc / mt_pole)])
meq = mt_multi([(3, 1.0), (3, 1.0), (1, 1.0)])
check('C2 [T/E] one composite doublet fed by several pairs: compositeness fixes sum_i N_ci m_i^2 ln(Lambda^2/m_i^2) = 4 pi^2 v^2, '
      f'so with the measured mass ratios the top takes {mmeas / m1:.5f} of its single-channel value; equal t, b, tau channels '
      f'(the open_gate note\'s H2) give {meq / m1:.3f} ~ sqrt(3/7) = {np.sqrt(3/7):.3f} (log shift), not 1/3, and force m_t = m_b = m_tau, which measurement excludes',
      abs(mmeas / m1 - 1) < 1e-3 and abs(meq / m1 - np.sqrt(3 / 7)) < 0.01, f'single {m1:.1f}, measured-ratio {mmeas:.1f}, equal {meq:.1f} GeV (bubble)')

# ---------------------------------------------------------------- D. scalar spectrum and fits
def mH_over_v(nDNc, Lam=2.435e18):
    lo, hi = 1e-3, 1e4
    for _ in range(100):
        m = np.sqrt(lo * hi)
        if nDNc * m ** 2 * np.log(Lam ** 2 / m ** 2) / (4 * np.pi ** 2) > v ** 2: hi = m
        else: lo = m
    return 2 * m / v, m
r_top, m_top_b = mH_over_v(3); r_mir, m_mir = mH_over_v(4)
check('D1 [E/M] the doublet channel holds one real scalar besides the three eaten modes: in the bubble it sits at 2 m_f, '
      f'm_H/v = {r_top:.3f} (top pair, cutoff at the cell) and {r_mir:.3f} (a whole mirror family, quark + lepton doublets, '
      f'm_f = {m_mir:.0f} GeV) vs measured 0.508; running raises it (C1). No light 125 GeV state without a further symmetry',
      r_top > 0.6 and r_mir > 0.6, f'top m_f {m_top_b:.0f} GeV')
S_mir = 4 / (6 * np.pi); S_meas, S_err = -0.05, 0.07
aS_v = 1 / (1 / aS + 7 / (2 * np.pi) * np.log(v / MZ)); a_c = np.pi / 4
check('D2 [E/M] the doublet made from the mirror family (the pair square\'s own channel) needs chiral mirror quarks and leptons '
      f'near v: S = 4/(6 pi) = {S_mir:.3f} vs {S_meas} +- {S_err} ({(S_mir - S_meas) / S_err:.1f} sigma), on top of LHC limits on '
      f'chiral extra families; colour alone cannot bind it: alpha_s(v) = {aS_v:.3f} vs ladder alpha_c = pi/(3 C_F) = {a_c:.3f}',
      (S_mir - S_meas) / S_err > 3 and aS_v < a_c / 5, 'heavy degenerate doublets, U = 0 fit')

print('theorems: A1-A5 (exact Clifford/so(10) algebra; A5 sign of the gauge-loop energy cited).  finite: B1-B2.  T/F: B3.')
print('estimates: C1-C2, D1-D2.  cited: BHL compositeness boundary, Pagels-Stokar, heavy-doublet S, PDG inputs.')
print('supplied: the 16 per family and its PS halves, the pair square and other four-mode terms as written in the register,')
print('  the mean-field (large-N) gap equation, the single-cone lattice band, G = O(1) a^2, one-loop SM running, cutoff = 1/a.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
