"""R9-8: Wilson-line PATH dependence of the photon speed for the frame-rotated (non-separable) BQ-W law.
Same law as r98_frame_qed.py; only the gauge covariantisation of the off-axis hops differs:
  staircase (symmetrised over axis orders):  V_y(k+q xhat,k) = [d_y h(k) + d_y h(k+q xhat)]/2,   seagull(q,-q) = d_y^2 h(k)
  straight line (Terning/Mandelstam-type continuum path, A interpolated band-limited; valid in the photon box):
      V_y = int_0^1 ds d_y h(k + s q xhat),   seagull(q,-q) = int int ds dt d_y^2 h(k + (s-t) q xhat)
  P_M = [seagull(q) - chi_yy(q)]/d(q)^2 with seagull(0) = chi_yy(0) (f-sum, exact);  dc_gamma = (P_M - P_E)/2.
The two covariantisations differ by a gauge-invariant magnetic (flux) term: the path ambiguity of gauging a non-local kernel."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r98_frame_qed import LawW, comps_norm, dh, dot4, kgrid1, U

def d2h(law, kx, ky, kz, hstep=2e-3):
    f = lambda s: law.hW(kx, ky + s, kz)
    a, b, c, d, e = f(2 * hstep), f(hstep), f(0.0), f(-hstep), f(-2 * hstep)
    return tuple((-a[i] + 16 * b[i] - 30 * c[i] + 16 * d[i] - e[i]) / (12 * hstep ** 2) for i in range(4))

def run(law, N, qs=(0.02, 0.04), chunk=8):
    k1 = kgrid1(N); KY, KZ = np.meshgrid(k1, k1, indexing="ij")
    gs, gw = np.polynomial.legendre.leggauss(4); s01 = 0.5 * (gs + 1); w01 = 0.5 * gw
    # weight (1-u) on [0,1]: use 6-point GL and multiply
    us, uw = np.polynomial.legendre.leggauss(6); u01 = 0.5 * (us + 1); uw01 = 0.5 * uw * (1 - u01)
    acc = dict(PEw=0.0, chi0=0.0)
    accq = {q: dict(st=0.0, sl=0.0, dsea=0.0) for q in qs}
    for i0 in range(0, N, chunk):
        kx = k1[i0:i0 + chunk][:, None, None] + 0 * KY[None]; ky = KY[None] + 0 * kx; kz = KZ[None] + 0 * kx
        n, E = comps_norm(law.hW(kx, ky, kz)); x = dh(law, kx, ky, kz, 1)
        xn = dot4(x, n); x2 = dot4(x, x)
        acc["PEw"] += np.sum((x2 - xn ** 2) / (2 * E ** 3)); acc["chi0"] += np.sum(2 * (2 * x2 - 2 * xn ** 2) / (2 * E))
        y0 = d2h(law, kx, ky, kz)
        for q in qs:
            # seagull difference (straight): <-2 n . (Y(q) - d2h(k))>,  Y = int_0^1 (1-u)[f(u)+f(-u)] du
            Y = [0 * kx for _ in range(4)]
            for u, w in zip(u01, uw01):
                for sg in (+1, -1):
                    yy = d2h(law, kx + sg * u * q, ky, kz)
                    for i in range(4): Y[i] = Y[i] + w * yy[i]
            accq[q]["dsea"] += np.sum(-2 * dot4(n, tuple(Y[i] - y0[i] for i in range(4))))
            for sgn in (+1, -1):
                n2, E2 = comps_norm(law.hW(kx + sgn * q, ky, kz)); nn = dot4(n, n2)
                xq = dh(law, kx + sgn * q, ky, kz, 1)
                Xs = tuple(0.5 * (x[i] + xq[i]) for i in range(4))
                Xl = [0 * kx for _ in range(4)]
                for s, w in zip(s01, w01):
                    xs_ = dh(law, kx + sgn * s * q, ky, kz, 1)
                    for i in range(4): Xl[i] = Xl[i] + w * xs_[i]
                for key, X in (("st", Xs), ("sl", tuple(Xl))):
                    accq[q][key] += np.sum((dot4(X, X) * (1 + nn) - 2 * dot4(X, n) * dot4(X, n2)) / (E + E2))
    V = N ** 3; PEw = acc["PEw"] / V; chi0 = acc["chi0"] / V
    PMst, PMsl = [], []
    for q in qs:
        dq2 = law.d(np.array(q)) ** 2
        PMst.append((chi0 - accq[q]["st"] / V) / dq2)
        PMsl.append((chi0 + accq[q]["dsea"] / V - accq[q]["sl"] / V) / dq2)
    R = lambda a: (4 * a[0] - a[1]) / 3
    return PEw, R(PMst), R(PMsl)

if __name__ == "__main__":
    b1, b2, r, c1, c2 = [float(x) for x in sys.argv[1:6]]; N = int(sys.argv[6]); m = float(sys.argv[7])
    E1, E2 = float(sys.argv[8]), float(sys.argv[9])
    if E1 < 0: E1 = E2 = None
    law = LawW(b1, b2, r, c1, c2, m, E1, E2)
    PE, PMst, PMsl = run(law, N)
    print(f"paths b=({b1},{b2}) c=({c1},{c2}) E=({E1},{E2}) N={N} m={m} | P_E*U={U*PE:.4f} | staircase P_M*U={U*PMst:.4f}"
          f" dc_g*U={U*(PMst-PE)/2:+.4f} | straight P_M*U={U*PMsl:.4f} dc_g*U={U*(PMsl-PE)/2:+.4f}"
          f" | path shift of dc_g*U = {U*(PMsl-PMst)/2:+.4f}", flush=True)
