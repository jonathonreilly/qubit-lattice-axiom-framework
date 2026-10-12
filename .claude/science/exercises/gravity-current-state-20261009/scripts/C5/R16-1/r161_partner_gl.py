"""R16-1 (d): Q_W^P on Gauss-Legendre nodes. R13-1's partner formulas, unchanged, rewritten for general nodes/weights:
 - selectron_gl: two-complex-selectron photon coefficient (r131_photon_sqed.selectron: P_E = <G0^2/(16 eps^5)>,
   P_M = [chi(0) - chi(q)]/q^2, q = 2 pi s/Nref, s = 1, 2, 4, Richardson as there);
 - dE_partner_gl / dc_partner_gl: selectron-photino Yukawa loop (r131_electron_sqed.dE_partner / dc_partner).
Consistency: on uniform midpoint nodes both reproduce R13-1's functions."""
import sys; sys.path.insert(0, '.')
import numpy as np
from r85_box_qed_copy import deriv, plateau
from r131_electron_sqed import alpha, beta, PL, PR, he

def selectron_gl(law, nx, wx, ny, wy, Nref=128, ns=(1, 2, 4), dm2=0.0, chunk=8):
    KY, KZ = np.meshgrid(ny, ny, indexing='ij'); WYZ = np.outer(wy, wy)
    SY, WY, SZ, WZ = law.S(KY), law.W(KY), law.S(KZ), law.W(KZ)
    SpY, WpY = deriv(law.S, KY), deriv(law.W, KY)
    qs = [2 * np.pi * s / Nref for s in ns]
    PE = chi0 = 0.0; tot = {q: 0.0 for q in qs}
    for i0 in range(0, len(nx), chunk):
        kx = nx[i0:i0 + chunk][:, None, None]; wq = wx[i0:i0 + chunk][:, None, None] * WYZ[None]
        def M(sh): return law.m + law.W(kx + sh) + WY[None] + WZ[None]
        def eps(sh): return np.sqrt(law.S(kx + sh) ** 2 + SY[None] ** 2 + SZ[None] ** 2 + M(sh) ** 2 + dm2)
        e0, M0 = eps(0.0), M(0.0)
        G0 = 2 * SY[None] * SpY[None] + WpY[None] * 2 * M0
        PE += np.sum(wq * G0 ** 2 / e0 ** 5) / 16
        chi0 += np.sum(wq * G0 ** 2 / (4 * e0 ** 3))
        for q in qs:
            for sg in (+1, -1):
                e1 = eps(sg * q); G = 2 * SY[None] * SpY[None] + WpY[None] * (M0 + M(sg * q))
                tot[q] += 0.5 * np.sum(wq * G ** 2 / (2 * e0 * e1 * (e0 + e1)))
    V = (2 * np.pi) ** 3
    PE /= V; chi0 /= V
    PMs = [(chi0 - tot[q] / V) / q ** 2 for q in qs]
    r1 = (4 * PMs[0] - PMs[1]) / 3; r2 = (4 * PMs[1] - PMs[2]) / 3
    PM = (16 * r1 - r2) / 15
    return (PM - PE) / 2, PE

def dE_partner_gl(law, p, nx, wx, ny, wy, dm2=0.0, chunk=8):
    def Sg(q):
        rg = plateau(q, law.c1, law.c2); return rg * q + (1 - rg) * np.sin(q)
    QY, QZ = np.meshgrid(ny, ny, indexing='ij'); WYZ = np.outer(wy, wy)
    H = he(law, [p, 0.0, 0.0]); w, V = np.linalg.eigh(H); Pe = V[:, 2:] @ V[:, 2:].conj().T; Ep = w[-1]
    traces = []
    for Y in (beta @ PL, beta @ PR):
        Xm = Y @ Pe @ Y.conj().T
        traces.append((np.trace(Xm).real, [np.trace(alpha[j] @ Xm).real for j in range(3)], np.trace(beta @ Xm).real))
    gy, gz = Sg(QY), Sg(QZ); dy, dz = law.d(QY), law.d(QZ)
    Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
    tot = 0.0
    for i0 in range(0, len(nx), chunk):
        qx = nx[i0:i0 + chunk][:, None, None]; wq = wx[i0:i0 + chunk][:, None, None] * WYZ[None]
        gx, dx = Sg(qx), law.d(qx)
        Wl = np.sqrt(np.maximum(dx ** 2 - gx ** 2, 0) + np.maximum(dy ** 2 - gy ** 2, 0)[None] + np.maximum(dz ** 2 - gz ** 2, 0)[None])
        El = np.sqrt(gx ** 2 + gy[None] ** 2 + gz[None] ** 2 + Wl ** 2)
        kx = p - qx
        Ms = law.m + law.W(kx) + Wy[None] + Wz[None]
        eps = np.sqrt(law.S(kx) ** 2 + Sy[None] ** 2 + Sz[None] ** 2 + Ms ** 2 + dm2)
        for trX, ta, tb in traces:
            c = gx * ta[0] + gy[None] * ta[1] + gz[None] * ta[2] + Wl * tb
            tp = 0.5 * (trX + c / El); tm = 0.5 * (trX - c / El)
            tot += np.sum(wq * (tp / (2 * eps * (Ep - El - eps)) + tm / (2 * eps * (Ep + El + eps))))
    return Ep, tot / (2 * np.pi) ** 3 / 2

def dc_partner_gl(law, nx, wx, ny, wy, dm2=0.0):
    h = min(0.02, law.m / 8)
    E0, d0 = dE_partner_gl(law, 0.0, nx, wx, ny, wy, dm2)
    vals = []
    for hh in (h, 2 * h):
        Ep, d = dE_partner_gl(law, hh, nx, wx, ny, wy, dm2)
        vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2
