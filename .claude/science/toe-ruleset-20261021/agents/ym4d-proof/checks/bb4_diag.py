"""bb4_diag: POST-HOC diagnostic, written after reading bb4.out (C-5 and B-6 FAILED as predictions).
Not a criterion; it does not change bb4's verdict. Imports bb4_models unchanged.
(D1) C-5 with plateau radii 0.5 and 1.0 (bb4 used 2.0): where does the slice identity start to fail?
(D2) B-6's frame-free control at mu^2 in {1, 0.25, 0.05}: size of the non-invariance of dE(s) and R(X), with the frame
     version alongside.
"""
import sys, os, time
import numpy as np
import scipy.sparse.linalg as spla
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bb4_models as M

T0 = time.time()


def d1():
    rng = np.random.default_rng(M.SEED + 3)
    n, R, Tw, sh = 60, 12, 56, 22
    G = M.SliceModel(n); Lc = M.SliceModel(Tw)
    gx = (np.arange(G.nl) // 2) // n; gy = (np.arange(G.nl) // 2) % n; gm = np.arange(G.nl) % 2
    nbx = n // R
    w0 = np.array([M.sig(M.dist_iv(G.mx, R * k - 0.5, R * k + R - 0.5, n)) for k in range(nbx)])
    w1 = np.array([M.sig(M.dist_iv(G.my, R * k - 0.5, R * k + R - 0.5, n)) for k in range(nbx)])
    ys = [rng.standard_normal(G.nl) for _ in range(4)]
    for plateau in (0.5, 1.0, 1.5, 2.0):
        boxes = []
        for i in range(nbx):
            for j in range(nbx):
                a = (R * i, R * j)
                d0 = M.dist_iv(G.mx, a[0] - 0.5, a[0] + R - 0.5, n); d1_ = M.dist_iv(G.my, a[1] - 0.5, a[1] + R - 0.5, n)
                chi = (M.sig(d0) / w0.sum(axis=0)) * (M.sig(d1_) / w1.sum(axis=0))
                psi = M.sig((d0 - plateau) / (12 - plateau)) * M.sig((d1_ - plateau) / (12 - plateau))
                lx = (gx - a[0] + sh) % n; ly = (gy - a[1] + sh) % n
                reg = (lx < Tw) & (ly < Tw) & (np.maximum(d0, d1_) <= 16)
                gl = np.nonzero(reg)[0]; ll = 2 * (lx[gl] * Tw + ly[gl]) + gm[gl]
                psil = np.zeros(Lc.nl); psil[ll] = psi[gl]
                boxes.append((chi, gl, ll, psil))
        worst = 0.0
        for y in ys:
            Py = np.zeros(G.nl); Ry = np.zeros(G.nl)
            for chi, gl, ll, psil in boxes:
                yt = np.zeros(Lc.nl); yt[ll] = (chi * y)[gl]
                u = Lc.slice_solve(yt)
                cut = np.zeros(G.nl); cut[gl] = (psil * u)[ll]
                Py += G.Pi @ cut
                C = Lc.B @ (psil * u) - psil * (Lc.B @ u)
                Ry[gl] += -C[ll]
            worst = max(worst, np.abs(G.Pi.T @ (G.B @ Py - (y - Ry))).max() / np.abs(y).max())
        print(f"D1 plateau {plateau:.1f} (scale {12 - plateau:.1f}): slice identity residual {worst:.3e}")
    # measured locality radius of Pi: max l-inf distance between a link midpoint and the links its row reads
    Pi = G.Pi.tocoo()
    dxm = np.abs(((G.mx[Pi.row] - G.mx[Pi.col] + n / 2) % n) - n / 2)
    dym = np.abs(((G.my[Pi.row] - G.my[Pi.col] + n / 2) % n) - n / 2)
    print(f"D1 measured radius of Pi (max l-inf midpoint distance over nonzero entries): {np.maximum(dxm, dym).max():.2f}")


def d2():
    rng = np.random.default_rng(M.SEED + 2)
    T, lam = 32, 0.05
    links = M.su2_from(rng.standard_normal((T, T, 2, 3)), 0.1)
    jv = (rng.standard_normal((T * T, 2)) + 1j * rng.standard_normal((T * T, 2))) * 0.3 / np.sqrt(2)
    j = jv.ravel()
    h = M.haar_su2(rng, (T, T))
    hd = np.conj(np.swapaxes(h.reshape(-1, 2, 2), -1, -2))
    jh = np.einsum("sab,sb->sa", hd, j.reshape(-1, 2)).ravel()
    linksh = M.gauge_links(links, h)
    _ = [rng.standard_normal(2 * T * T) for _ in range(8)]  # keep the stream aligned with bb4 part B (4 complex ys)
    eta, member, bonds = M.cube_setup()
    svals = [rng.uniform(0, 1.2, len(bonds)) for _ in range(3)]
    nq = len(eta)
    for mu2 in (1.0, 0.25, 0.05):
        line = []
        for frame in (True, False):
            Mu = M.BoxModelB(links, frame, mu2=mu2); Mh = M.BoxModelB(linksh, frame, mu2=mu2)
            dmax = 0.0
            for sv in svals:
                S = M.smat(sv, bonds, nq)
                eu, _, _ = M.bond_energy(Mu, S, eta, member, j, lam)
                eh, _, _ = M.bond_energy(Mh, S, eta, member, jh, lam)
                dmax = max(dmax, abs(eu - eh))
            line.append(f"{'frame' if frame else 'frame-free'} max|dE(U^h)-dE(U)| = {dmax:.3e}")
        print(f"D2 mu^2 = {mu2}: " + "; ".join(line))


if __name__ == "__main__":
    d1()
    print(f"  [t = {time.time() - T0:.1f}s]")
    d2()
    print(f"  [t = {time.time() - T0:.1f}s]")
