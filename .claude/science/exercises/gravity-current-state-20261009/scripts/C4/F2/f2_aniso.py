"""F2: lattice QED with time ALSO on a lattice, anisotropy xi = a_s/a_t (a_s = 1).
xi = 1 is the hypercubic Z^4 block (W(B4) symmetry); xi -> infinity is continuous time (f2_ir.py).
Naive fermions in 4D (16 doublers; 4D staggered = 1/4 of the loop = 4 tastes), non-compact Wilson-type
photon, Feynman gauge, links in all four directions (temporal tadpole ~ a_t^2).
  fermion: Gamma_nu coefficient = sbar_nu(p)(1 - e^2 a_nu^2 <A_nu^2>/2) - e^2 int sbar_nu(q)(2 c_nu^2 - C)/den,
           sbar_0 = xi sin(q0/xi), c_0 = cos((p0+q0)/(2 xi)), khat_0 = 2 xi sin(k0/(2 xi)), q = p - k
           dc_f = a_x - a_0
  photon:  Pi_mn(k) = -e^2 c_m c_n int tr[S0(q) g_m S0(q+k) g_n] + delta_mn 4 e^2 a_m^2 int sbar_m^2/(Q^2+m^2)
           aE = Pi_xx(k0,0)/khat0^2, aB = Pi_yy(0,kx)/khat_x^2 (Richardson), dc_gamma = (aB-aE)/2
Usage: python f2_aniso.py
"""
import numpy as np, time

def bz(L, xi):
    ks = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    Lt = int(round(L * xi))
    k0s = ((np.arange(Lt) + 0.5) * 2 * np.pi / Lt - np.pi) * xi
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing="ij")
    return k0s, KX, KY, KZ, xi / (L ** 3 * Lt)   # measure: int d4k/(2pi)^4 = xi * mean

def fermion(L, xi, m, lam, h=1e-4):
    k0s, KX, KY, KZ, wgt = bz(L, xi)
    at = 1.0 / xi
    khs2 = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
    A2 = 0.0
    def coef_sum(p, nu):
        tot = 0.0
        for k0 in k0s:
            K2 = (2 * xi * np.sin(k0 / (2 * xi))) ** 2 + khs2 + lam ** 2
            q0 = p[0] - k0
            q = [p[1] - KX, p[2] - KY, p[3] - KZ]
            sb = [xi * np.sin(q0 / xi)] + [np.sin(x) for x in q]
            c = [np.cos((p[0] + q0) / (2 * xi))] + [np.cos((p[j + 1] + q[j]) / 2) for j in range(3)]
            C = c[0] ** 2 + c[1] ** 2 + c[2] ** 2 + c[3] ** 2
            den = (sb[0] ** 2 + sb[1] ** 2 + sb[2] ** 2 + sb[3] ** 2 + m ** 2) * K2
            tot += np.sum(sb[nu] * (2 * c[nu] ** 2 - C) / den)
        return tot * wgt
    for k0 in k0s:
        K2 = (2 * xi * np.sin(k0 / (2 * xi))) ** 2 + khs2 + lam ** 2
        A2 += np.sum(1 / K2)
    A2 *= wgt
    out = {}
    for nu, a_nu in ((0, at), (1, 1.0)):
        pp = np.zeros(4); pm = np.zeros(4); pp[nu] = h; pm[nu] = -h
        dI = (coef_sum(pp, nu) - coef_sum(pm, nu)) / (2 * h)
        out[nu] = -0.5 * a_nu ** 2 * A2 - dI
    return out[0], out[1], A2

def photon(L, xi, m, ks=(0.02, 0.04)):
    q0s, QX, QY, QZ, wgt = bz(L, xi)
    sx, sy, sz = np.sin(QX), np.sin(QY), np.sin(QZ)
    aEv = np.zeros(len(ks)); bub = np.zeros(len(ks)); tadx = tady = 0.0
    for q0 in q0s:
        s0 = xi * np.sin(q0 / xi)
        Q2 = s0 ** 2 + sx ** 2 + sy ** 2 + sz ** 2 + m ** 2
        tadx += 4 * np.sum(sx ** 2 / Q2); tady += 4 * np.sum(sy ** 2 / Q2)
        for i, k in enumerate(ks):
            # Pi_xx(k0=k, 0): Q' = Q with q0 -> q0+k ; c_x = cos(qx)
            s0p = xi * np.sin((q0 + k) / xi)
            Q2p = s0p ** 2 + sx ** 2 + sy ** 2 + sz ** 2 + m ** 2
            QQp = s0 * s0p + sx ** 2 + sy ** 2 + sz ** 2
            aEv[i] += np.sum(-4 * np.cos(QX) ** 2 * (-2 * sx ** 2 + QQp + m ** 2) / (Q2 * Q2p))
            # Pi_yy(0, kx=k): c_y = cos(qy)
            sxp = np.sin(QX + k)
            Q2b = s0 ** 2 + sxp ** 2 + sy ** 2 + sz ** 2 + m ** 2
            QQb = s0 ** 2 + sx * sxp + sy ** 2 + sz ** 2
            bub[i] += np.sum(-4 * np.cos(QY) ** 2 * (-2 * sy ** 2 + QQb + m ** 2) / (Q2 * Q2b))
    aEv *= wgt; bub *= wgt; tadx *= wgt; tady *= wgt
    vE = [(aEv[i] + tadx) / (2 * xi * np.sin(k / (2 * xi))) ** 2 for i, k in enumerate(ks)]
    vB = [(bub[i] + tady) / (2 * np.sin(k / 2)) ** 2 for i, k in enumerate(ks)]
    aE = (4 * vE[0] - vE[1]) / 3; aB = (4 * vB[0] - vB[1]) / 3
    wi = aEv[0] + tadx - (aEv[0] + tadx) * 0  # placeholder
    return aE, aB

if __name__ == "__main__":
    u = 16 * np.pi ** 2
    t0 = time.time()
    m, lam = 0.1, 0.2
    for L in (32, 48):
        for xi in (1.0, 2.0, 4.0, 8.0):
            a0, ax, A2 = fermion(L, xi, m, lam)
            aE, aB = photon(L, xi, m)
            dcf = u * (ax - a0); dcg_naive = u * (aB - aE) / 2
            print(f"L={L} xi={xi:3.1f} m={m} lam={lam}: dc_f*16pi^2={dcf:+.4f}  dc_gamma*16pi^2 per naive-4D={dcg_naive:+.4f} "
                  f"(per Dirac {dcg_naive/16:+.4f}; 4D staggered = 4 tastes {dcg_naive/4:+.4f})  "
                  f"Delta(stag 4 tastes) = {dcf - dcg_naive/4:+.4f}   [{time.time()-t0:.0f}s]", flush=True)
