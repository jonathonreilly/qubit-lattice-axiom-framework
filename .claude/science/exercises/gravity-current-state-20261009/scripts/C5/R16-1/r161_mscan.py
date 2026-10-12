"""R16-1 (c): Delta_lam(m) = dc_e(m) - dc_gamma(m) (x16pi^2) for D1(b=1.4, r=1/sqrt3), naive photon, lam = 0.05,
m in [0.005, 3] (+ large-m approach to the linear law), at three resolutions.
dc_e: R13-7's on-shell formulas (r161_onshell_aniso = r137_onshell.dE_onshell with general nodes), all three axes on
composite Gauss-Legendre panels adapted to the Wilson slab [b, pi-b] and to the photon IR region near q = 0.
dc_gamma: R10-1's refereed Theorem-D moment (r101_dirac_moment formulas, unchanged) on the same kind of panels.
Richardson step in p: h = min(0.02, m/8) (F(p) is analytic in p^2 only within |p| < m)."""
import sys, time; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law
from r85_box_qed_copy import deriv
U = 16 * np.pi ** 2

def axis_nodes(b, npp):
    """composite GL nodes on [-pi, pi]: IR panels near 0, box, Wilson slab, corner box."""
    w = np.pi - 2 * b
    pos = [0.0, 0.0125, 0.025, 0.05, 0.1, 0.2, 0.35, 0.55, 0.8, 1.05, b - 0.12, b] \
        + list(b + w * np.linspace(0, 1, 11)[1:]) + [np.pi - b + 0.25, np.pi - b + 0.6, np.pi - b + 1.0, np.pi]
    pos = np.unique(np.array([x for x in pos if 0 <= x <= np.pi]))
    edges = np.concatenate([-pos[::-1], pos[1:]])
    x, wt = np.polynomial.legendre.leggauss(npp)
    a, c = edges[:-1, None], edges[1:, None]
    return (0.5 * (c - a) * x + 0.5 * (c + a)).ravel(), (0.5 * (c - a) * wt).ravel()

def dE_onshell_gl(law, lam, ps, nx, wx, ny, wy, chunk=8):
    QY, QZ = np.meshgrid(ny, ny, indexing='ij'); WYZ = np.outer(wy, wy)
    dy2, dz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    out = {}
    for p in ps:
        Sp, Wp = law.S(np.array(p)), law.W(np.array(p)); W0 = law.W(np.array(0.0))
        hp = np.array([Sp, 0.0, 0.0, law.m + Wp + 2 * W0]); Ep = np.sqrt(hp @ hp); a = hp / Ep
        Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
        dly = (0.0 - Sy, W0 - Wy); dlz = (0.0 - Sz, W0 - Wz)
        acc = 0.0
        for i0 in range(0, len(nx), chunk):
            qx = nx[i0:i0 + chunk][:, None, None]; wq = wx[i0:i0 + chunk][:, None, None] * WYZ[None]
            dx2 = law.d(qx) ** 2
            Wq = np.sqrt(dx2 + dy2[None] + dz2[None] + lam ** 2)
            kx = p - qx
            hk = [law.S(kx) + 0 * Wq, Sy[None] + 0 * Wq, Sz[None] + 0 * Wq, law.m + law.W(kx) + Wy[None] + Wz[None] + 0 * Wq]
            Ek = np.sqrt(hk[0] ** 2 + hk[1] ** 2 + hk[2] ** 2 + hk[3] ** 2)
            bb = [c / Ek for c in hk]
            ab = a[0] * bb[0] + a[3] * bb[3]
            dxa = Sp - law.S(kx); dxb = Wp - law.W(kx)
            for s in (+1, -1):
                d2 = dxa ** 2 + dxb ** 2
                db = dxa * bb[0] + dxb * bb[3]; da = dxa * a[0] + dxb * a[3]
                X = (d2 + s * (2 * db * da - d2 * ab)) / (2 * dx2)
                d2y = (dly[0] ** 2 + dly[1] ** 2)[None]
                dby = dly[0][None] * bb[1] + dly[1][None] * bb[3]; day = dly[1][None] * a[3]
                X = X + (d2y + s * (2 * dby * day - d2y * ab)) / (2 * dy2[None])
                d2z = (dlz[0] ** 2 + dlz[1] ** 2)[None]
                dbz = dlz[0][None] * bb[2] + dlz[1][None] * bb[3]; daz = dlz[1][None] * a[3]
                X = X + (d2z + s * (2 * dbz * daz - d2z * ab)) / (2 * dz2[None])
                X = X - (1 + s * ab) / 2
                acc += np.sum(wq * (-s * X / (2 * Wq * (Wq + Ek - s * Ep))))
            tx = a[0] * (law.S(p + qx) + law.S(p - qx) - 2 * Sp) + a[3] * (law.W(p + qx) + law.W(p - qx) - 2 * Wp)
            ty = a[3] * (law.W(QY) + law.W(-QY) - 2 * W0)[None]
            tz = a[3] * (law.W(QZ) + law.W(-QZ) - 2 * W0)[None]
            acc += np.sum(wq * (0.5 * (tx / dx2 + ty / dy2[None] + tz / dz2[None]) / (2 * Wq)))
        out[p] = (Ep, acc / (2 * np.pi) ** 3)
    return out

def dce_gl(law, lam, nx, wx, ny, wy):
    h = min(0.02, law.m / 8)
    r = dE_onshell_gl(law, lam, [0.0, h, 2 * h], nx, wx, ny, wy)
    F = {p: 2 * r[p][0] * r[p][1] for p in r}
    D1 = (F[h] - F[0.0]) / h ** 2; D2 = (F[2 * h] - F[0.0]) / (4 * h ** 2)
    return ((4 * D1 - D2) / 3) / 2

def moment_gl(law, nx, wx, ny, wy, chunk=8):
    """R10-1 Theorem D moment <R_D> (formulas copied from r101_dirac_moment.moment), GL nodes."""
    KY, KZ = np.meshgrid(ny, ny, indexing='ij'); WYZ = np.outer(wy, wy)
    Sy, Wy, Sz, Wz = law.S(KY), law.W(KY), law.S(KZ), law.W(KZ)
    xy, xb = deriv(law.S, KY), deriv(law.W, KY)
    tot = 0.0
    for i0 in range(0, len(nx), chunk):
        kx = nx[i0:i0 + chunk][:, None, None]; wq = wx[i0:i0 + chunk][:, None, None] * WYZ[None]
        Sx, Wx = law.S(kx), law.W(kx)
        Sxp, Wxp = deriv(law.S, kx), deriv(law.W, kx)
        Sxpp, Wxpp = deriv(law.S, kx, 2), deriv(law.W, kx, 2)
        M = law.m + Wx + Wy[None] + Wz[None]
        E2 = Sx ** 2 + Sy[None] ** 2 + Sz[None] ** 2 + M ** 2; E = np.sqrt(E2)
        x2 = (xy ** 2 + xb ** 2)[None] + 0 * E
        X = xy[None] * Sy[None] + xb[None] * M
        a = Sxp ** 2 + Wxp ** 2 - 1 + 0 * E
        bq = Sx * Sxpp + M * Wxpp
        A = a + bq
        hhp = Sx * Sxp + M * Wxp
        c1 = xb[None] * Wxp; c2 = xb[None] * Wxpp
        R = a * x2 / (4 * E ** 3) - A * X ** 2 / (4 * E ** 5) - c1 * hhp * X / (2 * E ** 5) + c2 * X / (2 * E ** 3)
        tot += np.sum(wq * R)
    return tot / (2 * np.pi) ** 3

if __name__ == '__main__':
    lam = 0.05; b = 1.4; r = 1 / np.sqrt(3)
    levels = [(4, 3), (6, 4), (8, 5)] if len(sys.argv) < 2 else [tuple(int(x) for x in sys.argv[1].split(','))]
    ms = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.2, 1.6, 2.0, 2.5, 3.0, 6.4, 12.8, 25.6]
    t0 = time.time()
    print('D1(b=1.4, r=1/sqrt3), naive photon, lam=%.2f; columns: m | level (GL nodes/panel q_x, q_perp) | n_x, n_perp | dc_e*U | dc_gamma*U | Delta*U' % lam)
    for (lx, lp) in levels:
        nx, wx = axis_nodes(b, lx); ny, wy = axis_nodes(b, lp)
        for m in ms:
            law = D1Law(b, r, m)
            dce = dce_gl(law, lam, nx, wx, ny, wy) * U
            dcg = moment_gl(law, nx, wx, nx, wx) * U if len(nx) <= 220 else moment_gl(law, nx, wx, ny, wy) * U
            print('m=%7.3f | (%d,%d) | %d,%d | dc_e=%+10.4f | dc_g=%+10.4f | Delta=%+10.4f   [%.0fs]' % (m, lx, lp, len(nx), len(ny), dce, dcg, dce - dcg, time.time() - t0), flush=True)
