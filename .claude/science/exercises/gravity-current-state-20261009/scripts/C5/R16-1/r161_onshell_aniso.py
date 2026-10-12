"""R16-1: R13-7's on-shell runner (r137_onshell.dE_onshell, formulas unchanged) on an anisotropic tensor grid:
q_x by Gauss-Legendre panels (nx nodes over [-pi, pi]), q_y, q_z midpoint (Np each). Needed for D1(r), whose
Wilson slab [b, pi-b] is only 0.34 wide at b = 1.4 (R13-7's uniform N = 64 grid puts ~3 points across it)."""
import numpy as np, sys
sys.path.insert(0, '.')
from r85_box_qed_copy import kgrid1
U = 16 * np.pi ** 2

def qx_nodes(npan=96, nper=8):
    x, w = np.polynomial.legendre.leggauss(nper)
    e = np.linspace(-np.pi, np.pi, npan + 1)
    a, b = e[:-1, None], e[1:, None]
    return (0.5 * (b - a) * x + 0.5 * (b + a)).ravel(), (0.5 * (b - a) * w).ravel()

def dE_onshell_aniso(law, Np, lam, ps, qxn, qxw, chunk=16):
    q1 = kgrid1(Np)
    QY, QZ = np.meshgrid(q1, q1, indexing='ij')
    dy2, dz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    out = {}
    for p in ps:
        Sp, Wp = law.S(np.array(p)), law.W(np.array(p))
        W0 = law.W(np.array(0.0))
        hp = np.array([Sp, 0.0, 0.0, law.m + Wp + 2 * W0])
        Ep = np.sqrt(hp @ hp); a = hp / Ep
        Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
        dly = (0.0 - Sy, W0 - Wy); dlz = (0.0 - Sz, W0 - Wz)
        acc = 0.0; tad = 0.0
        for i0 in range(0, len(qxn), chunk):
            qx = qxn[i0:i0 + chunk][:, None, None]; wq = qxw[i0:i0 + chunk][:, None, None]
            dx2 = law.d(qx) ** 2
            Wq = np.sqrt(dx2 + dy2[None] + dz2[None] + lam ** 2)
            kx = p - qx
            hk = [law.S(kx) + 0 * Wq, Sy[None] + 0 * Wq, Sz[None] + 0 * Wq,
                  law.m + law.W(kx) + Wy[None] + Wz[None] + 0 * Wq]
            Ek = np.sqrt(hk[0] ** 2 + hk[1] ** 2 + hk[2] ** 2 + hk[3] ** 2)
            b = [c / Ek for c in hk]
            ab = a[0] * b[0] + a[3] * b[3]
            dxa = Sp - law.S(kx); dxb = Wp - law.W(kx)
            for s in (+1, -1):
                d2 = dxa ** 2 + dxb ** 2
                db = dxa * b[0] + dxb * b[3]; da = dxa * a[0] + dxb * a[3]
                X = (d2 + s * (2 * db * da - d2 * ab)) / (2 * dx2)
                d2y = (dly[0] ** 2 + dly[1] ** 2)[None]
                dby = dly[0][None] * b[1] + dly[1][None] * b[3]; day = dly[1][None] * a[3]
                X = X + (d2y + s * (2 * dby * day - d2y * ab)) / (2 * dy2[None])
                d2z = (dlz[0] ** 2 + dlz[1] ** 2)[None]
                dbz = dlz[0][None] * b[2] + dlz[1][None] * b[3]; daz = dlz[1][None] * a[3]
                X = X + (d2z + s * (2 * dbz * daz - d2z * ab)) / (2 * dz2[None])
                X = X - (1 + s * ab) / 2
                acc += np.sum(wq * (-s * X / (2 * Wq * (Wq + Ek - s * Ep))))
            tx = a[0] * (law.S(p + qx) + law.S(p - qx) - 2 * Sp) + a[3] * (law.W(p + qx) + law.W(p - qx) - 2 * Wp)
            ty = a[3] * (law.W(QY) + law.W(-QY) - 2 * W0)[None]
            tz = a[3] * (law.W(QZ) + law.W(-QZ) - 2 * W0)[None]
            tad += np.sum(wq * (0.5 * (tx / dx2 + ty / dy2[None] + tz / dz2[None]) / (2 * Wq)))
        V = 2 * np.pi * Np ** 2
        out[p] = dict(Ep=Ep, dE=(acc + tad) / V, tad=tad / V)
    return out

def dce_aniso(law, Np, lam, qxn, qxw, h=0.02):
    """dc_e = (c_e^2 - 1)/2 (Richardson in p^2, steps h, 2h)."""
    r = dE_onshell_aniso(law, Np, lam, [0.0, h, 2 * h], qxn, qxw)
    F = {p: 2 * r[p]['Ep'] * r[p]['dE'] for p in r}
    D1 = (F[h] - F[0.0]) / h ** 2; D2 = (F[2 * h] - F[0.0]) / (4 * h ** 2)
    return ((4 * D1 - D2) / 3) / 2
