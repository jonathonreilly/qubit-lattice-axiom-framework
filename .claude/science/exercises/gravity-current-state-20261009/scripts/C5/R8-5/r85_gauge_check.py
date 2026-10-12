"""R8-5 gauge-parameter check of the electron speed in box QED (BQ).
Covariant gauge D_mn = [delta_mn - (1-xi) Dhat_m Dhat_n^*/(Q^2+lam^2)]/(Q^2+lam^2). Using the exact lattice WT identity
sum_m Dhat_m V_m(k+Q,k) = -ie[G^-1(k+Q) - G^-1(k)] and the longitudinal seagull, the xi-dependent part of Sigma is
   Sigma_xi(p) = -(1-xi) e^2 [ a I2 - a X(p) a ],  a = G^-1(p) = -i p0 + h(p),  X(p) = int G(p-Q)/(Q^2+lam^2)^2,
(derivation in R8-5_report.md section 4.3, "Gauge-parameter check"). a*I2 rescales Z0 and Z1 equally, so the speed's xi-dependence is
(1-xi) * [B^xi - A^xi] from +a X a; it must vanish as m -> 0 if the extraction is gauge independent.
k0 integral: int dk0/2pi (-ik0+E)^-1 ((p0-k0)^2+W^2)^-2 = s (2W + c)/(4 W^3 (W + c)^2), c = |E| - i s p0.
Reported: (B^xi - A^xi) * 16 pi^2 per (1-xi).
"""
import numpy as np, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from r85_box_qed import Law, kgrid1

def SX(law, N, lam, p0, px, chunk=16):
    """returns (S0, Vx): scalar part and alpha_x part of a X a at external (p0, px, 0, 0), averaged over BZ."""
    q1 = kgrid1(N)
    QY, QZ = np.meshgrid(q1, q1, indexing="ij")
    dy2, dz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
    a0 = -1j * p0
    ah = np.array([law.S(np.array(px)), 0.0, 0.0, law.m + law.W(np.array(px))])  # h(p) Clifford comps
    S0 = 0j; Vx = 0j
    for i0 in range(0, N, chunk):
        qx = q1[i0:i0 + chunk][:, None, None]
        W = np.sqrt(law.d(qx) ** 2 + dy2[None] + dz2[None] + lam ** 2)
        kx = px - qx
        h = [law.S(kx) + 0 * W, Sy[None] + 0 * W, Sz[None] + 0 * W, law.m + law.W(kx) + Wy[None] + Wz[None]]
        E = np.sqrt(sum(c ** 2 for c in h))
        f = {}
        for s in (+1, -1):
            c = E - 1j * s * p0
            f[s] = s * (2 * W + c) / (4 * W ** 3 * (W + c) ** 2)
        x0 = 0.5 * (f[1] + f[-1]); xs = 0.5 * (f[1] - f[-1])
        xv = [xs * hc / E for hc in h]
        ax = sum(ah[i] * xv[i] for i in range(4)); aa = float(np.dot(ah, ah))
        S0 += np.sum(a0 ** 2 * x0 + 2 * a0 * ax + x0 * aa)
        Vx += np.sum(a0 ** 2 * xv[0] + 2 * a0 * x0 * ah[0] + 2 * ax * ah[0] - aa * xv[0])
    return S0 / N ** 3, Vx / N ** 3

def dce_xi(law, N, lam, h=1e-3):
    A = 1j * (SX(law, N, lam, h, 0.0)[0] - SX(law, N, lam, -h, 0.0)[0]) / (2 * h)
    B = (SX(law, N, lam, 0.0, h)[1] - SX(law, N, lam, 0.0, -h)[1]) / (2 * h)
    return A, B

if __name__ == "__main__":
    U = 16 * np.pi ** 2
    for label, args in [("naive (F2 law)", (None, None, 0.0, None, None)), ("BQ S3 box", (2.0, 3.0, 1.0, 2.0, 3.0)),
                        ("BQ S1 box", (1.0, 2.0, 1.0, 1.0, 2.0))]:
        for (N, m) in [(96, 0.2), (128, 0.1), (192, 0.05), (288, 0.025)]:
            law = Law(*args, m, naive_photon=(args[0] is None))
            A, B = dce_xi(law, N, m)
            print(f"{label:16s} N={N} m=lam={m}:  A^xi*U={U*A.real:+.4f} (imag {A.imag:+.1e})  B^xi*U={U*B.real:+.4f}"
                  f"  (B^xi-A^xi)*U per (1-xi) = {U*(B-A).real:+.5f}", flush=True)
