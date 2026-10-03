#!/usr/bin/env python3
"""A19 mediated registration (supplied toy, static-scatterer limit).

Ladder in Z^3: mover chain A and probe chain B side by side; rung pairs (A_x, B_x) carry a number-conserving pair
gate with theta = 0 and a |11> phase phi (inside the A10 S1 family).  With the mover held at site x during the
scattering, the probe (one excitation on B, Dirac round, mass m_p, momentum q < 0, coming from the right) evolves
as V_x.  A SHARP single-site record of the probe at site y then acts on the mover as the diagonal Kraus operator
      M_y(x) = <y| V_x |probe>,   sum_y |M_y(x)|^2 = 1  (unitarity)          [EXACT structure]
i.e. as a partial cut with modulus |M_y(x)| (coarse localisation, set by the probe packet) and phase arg M_y(x)
(a kick, set by the probe's momentum transfer).  Compared here with a direct sharp site cut on the mover.
"""
import numpy as np
from core1d import step, packet, vgroup, momentum_stats, PI


def probe_instrument(Mp, m_p, q, w_p, start_cell, xs, phi, T):
    """Return M[x_index, y_site] for defect sites xs (probe-chain site index = mover site index)."""
    X = len(xs)
    a0, b0 = packet(Mp, m_p, q, w_p, start_cell)
    a = np.repeat(a0[None], X, 0); b = np.repeat(b0[None], X, 0)
    rows = np.arange(X)
    ev = np.array([x % 2 == 0 for x in xs]); cells = np.array([x // 2 for x in xs])
    ph = np.exp(1j * phi)
    for t in range(T):
        a, b = step(a, b, m_p)
        a[rows[ev], cells[ev]] *= ph            # contact phase when the probe sits on the mover's site
        b[rows[~ev], cells[~ev]] *= ph
    Msite = np.empty((X, 2 * Mp), complex)
    Msite[:, 0::2] = a; Msite[:, 1::2] = b
    return Msite


def mover_state(Mm, m_A, K_A, w_A, c_cell):
    a, b = packet(Mm, m_A, K_A, w_A, c_cell)
    psi = np.empty(2 * Mm, complex); psi[0::2] = a; psi[1::2] = b
    return psi


def analyse(psi_sites, m_A):
    a, b = psi_sites[0::2][None], psi_sites[1::2][None]
    Km, Kv, plus = momentum_stats(a, b, m_A)
    P = np.abs(psi_sites) ** 2; P /= P.sum()
    x = np.arange(psi_sites.size) / 2.0
    mu = np.dot(P, x)
    return Km[0], np.sqrt(Kv[0]), plus[0], mu, np.sqrt(np.dot(P, (x - mu) ** 2))


Mp = 512                 # probe ring, cells
Mm = 512                 # mover ring, cells (same site indexing as the probe chain)
c_site = 512             # collision zone centre (site index)
m_A, K_A, w_A = 0.6, 1.0, 10.0
psiA = mover_state(Mm, m_A, K_A, w_A, c_site // 2)
K0m, sK0, plus0, mu0, sx0 = analyse(psiA, m_A)
print(f"mover before: K mean {K0m:+.4f}, K sd {sK0:.4f}, + band {plus0:.4f}, position sd {sx0:.2f} cells "
      f"(m_A={m_A}, K_A={K_A}, v={vgroup(K_A, m_A):.3f})")
xs = np.arange(c_site - 70, c_site + 71)       # mover sites where it has weight
wmask = np.zeros(2 * Mm, bool); wmask[xs] = True
print(f"  mover weight inside the defect window: {np.sum(np.abs(psiA[wmask])**2):.8f}")

# direct sharp site cut on the mover, for comparison (average over outcomes)
P = np.abs(psiA) ** 2
stats = []
for x in xs:
    if P[x] < 1e-12:
        continue
    cut = np.zeros_like(psiA); cut[x] = 1.0
    stats.append((P[x],) + analyse(cut, m_A))
st = np.array(stats); wsum = st[:, 0].sum()
print(f"direct sharp site cut: <K sd> {np.dot(st[:,0], st[:,2])/wsum:.4f} (uniform on the zone: {PI/np.sqrt(3):.4f}), "
      f"<+ band> {np.dot(st[:,0], st[:,3])/wsum:.4f}")

for (m_p, q, w_p, phi) in ((0.3, -0.1, 12.0, 0.6), (0.3, -0.05, 24.0, 0.6), (0.3, -0.1, 24.0, 0.6)):
    vp = vgroup(q, m_p)
    start = c_site // 2 + 40 + int(2 * w_p)
    T = int(2 * (start - c_site // 2) / abs(vp)) + 20
    M = probe_instrument(Mp, m_p, q, w_p, start, xs, phi, T)
    comp = np.abs(np.sum(np.abs(M) ** 2, axis=1) - 1).max()
    ys = np.arange(2 * Mp)
    refl = ys > c_site                           # probe registered right of the collision zone: reflected branch
    Prefl = np.sum(np.abs(M[:, refl]) ** 2, axis=1)
    # apply the instrument to the mover: outcome y -> psi'(x) = M_y(x) psi(x) on the window
    out = []
    for y in ys:
        k = M[:, y]
        new = np.zeros_like(psiA); new[xs] = k * psiA[xs]
        p = np.sum(np.abs(new) ** 2)
        if p < 1e-14:
            continue
        new /= np.sqrt(p)
        Km, sK, plus, mu, sx = analyse(new, m_A)
        out.append((y, p, Km, sK, plus, mu, sx))
    out = np.array(out)
    R = out[:, 0] > c_site
    def avg(col, sel):
        return np.dot(out[sel, 1], out[sel, col]) / out[sel, 1].sum()
    print(f"\nprobe m_p={m_p} q={q} (v={vp:+.3f}) w_p={w_p} cells, phi={phi}, T={T}: completeness |sum_y|M|^2-1| <= {comp:.1e}")
    print(f"  P(reflected) = {Prefl.mean():.4f} (range over mover sites {Prefl.min():.4f}..{Prefl.max():.4f}); "
          f"total outcome probability {out[:,1].sum():.6f}")
    print(f"  reflected-probe records: mover K mean {avg(2,R):+.4f} (shift {avg(2,R)-K0m:+.4f}; recoil 2q = {2*q:+.3f}), "
          f"K sd {avg(3,R):.4f}, + band {avg(4,R):.4f}, position sd {avg(6,R):.2f} cells")
    print(f"  transmitted-probe records: mover K mean {avg(2,~R):+.4f} (shift {avg(2,~R)-K0m:+.4f}), K sd {avg(3,~R):.4f}, "
          f"+ band {avg(4,~R):.4f}, position sd {avg(6,~R):.2f}")
    # structure of one reflected outcome: modulus width and phase slope of M_y(x)
    yb = int(out[R][np.argmax(out[R][:, 1]), 0])
    k = M[:, yb]; amp = np.abs(k) ** 2; amp /= amp.sum()
    xc = xs / 2.0; mu = np.dot(amp, xc); sd = np.sqrt(np.dot(amp, (xc - mu) ** 2))
    sel = amp > 0.2 * amp.max()
    ev = (xs % 2 == 0) & sel
    slope = np.polyfit(xc[ev], np.unwrap(np.angle(k[ev])), 1)[0]
    print(f"  most likely reflected record y={yb}: |M_y(x)|^2 profile sd {sd:.2f} cells (probe w_p={w_p}); "
          f"phase slope of M_y over mover cells {slope:+.4f} rad/cell (kick; 2|q| = {2*abs(q):.3f})")
