"""T-SPIRAL analysis: matching MCRG map R on spline surrogates; fixed points; linearised eigenvalues.
usage: python3 analysis.py file.npz [file2.npz ...]
Coordinates theta = (t, mu), t = tanh K. Fixed points: zeros of D(theta) = A_big(theta) - A_small(theta)
(equal final sizes). Jacobian T = pinv(W J_small) W J_big at theta*. Variants: S2/S5, matching level n.
"""
import sys
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.optimize import least_squares

SETS = {"S2": [0, 1], "S5": [0, 1, 2, 3, 4]}

def surrogates(tK, MU, M, E):
    sp = []
    for k in range(M.shape[-1]):
        z = M[..., k]
        s = float(np.sum(E[..., k] ** 2))
        sp.append(RectBivariateSpline(tK, MU, z, kx=3, ky=3, s=s))
    return sp

def ev(sp, th, idx, dx=0, dy=0):
    return np.array([float(sp[k].ev(th[0], th[1], dx=dx, dy=dy)) for k in idx])

def analyse(fn):
    Z = np.load(fn)
    tK, MU, d, b, nlev, S = Z["tK"], Z["MU"], int(Z["d"]), int(Z["b"]), int(Z["nlev"]), int(Z["S"])
    print(f"\n######## {fn}: d={d} b={b} L={int(Z['Lbig'])} S={S} levels={nlev}")
    # correlation-length diagnostic: largest r with C(r) > 0.01 on the fine big lattice; decay length from C(r)
    C = Z["C_big"]
    print("fine-lattice axis correlation C(r): r_max with C>0.02 [rows t, cols mu]")
    rmax = (C > 0.02).sum(-1)
    print("      mu: " + " ".join(f"{m:4.0f}" for m in MU))
    for i, t in enumerate(tK):
        print(f"t={t:4.2f}: " + " ".join(f"{v:4d}" for v in rmax[i]))
    out = []
    lo = np.array([tK[0], MU[0]]); hi = np.array([tK[-1], MU[-1]])
    for n in range(nlev):
        Mb, Eb = Z[f"big_n{n}_m"], Z[f"big_n{n}_e"]
        Ms, Es = Z[f"small_n{n}_m"], Z[f"small_n{n}_e"]
        spb, sps = surrogates(tK, MU, Mb, Eb), surrogates(tK, MU, Ms, Es)
        for sname, idx in SETS.items():
            sig = np.sqrt(np.median(Eb[..., idx] ** 2 + Es[..., idx] ** 2, axis=(0, 1)))
            W = 1.0 / sig
            def D(th):
                return W * (ev(spb, th, idx) - ev(sps, th, idx))
            def Rmap(th, start=None):
                tgt = ev(spb, th, idx)
                f = lambda p: W * (ev(sps, p, idx) - tgt)
                best = None
                for s0 in ([th] if start is None else [start]) + [np.array([0.5, 3.0]), np.array([0.9, 6.0])]:
                    r = least_squares(f, np.clip(s0, lo, hi), bounds=(lo, hi))
                    if best is None or r.cost < best.cost:
                        best = r
                return best.x, best.cost
            # flow table on a coarse grid
            if sname == "S5" or nlev == 1 or True:
                print(f"\n-- n={n} {sname}: flow R(theta) on coarse grid  (t, mu) -> (t', mu')   [boundary hits marked *]")
                for t in (0.2, 0.5, 0.8, 0.95):
                    row = []
                    for mu in (-2.0, 1.0, 4.0, 7.0):
                        p, c = Rmap(np.array([t, mu]))
                        flag = "*" if np.any(np.isclose(p, lo, atol=1e-3) | np.isclose(p, hi, atol=1e-3)) else " "
                        row.append(f"({t:.2f},{mu:+.0f})->({p[0]:.3f},{p[1]:+.2f}){flag}")
                    print("   " + "  ".join(row))
            if sname == "S2":
                # raw-grid test (no surrogate): significance of D for nn and plaquette at every grid point with t>0
                for k, nm in ((0, "nn"), (1, "plaq")):
                    Dr = (Mb[1:, :, k] - Ms[1:, :, k]) / np.sqrt(Eb[1:, :, k] ** 2 + Es[1:, :, k] ** 2)
                    print(f"-- n={n} raw D_{nm}/sigma over {Dr.size} grid points with t>0: max {Dr.max():+.1f}, "
                          f"min {Dr.min():+.1f}, points with D>-2sigma: {(Dr > -2).sum()} "
                          f"at (t,mu)={[(float(tK[1+i]), float(MU[j])) for i, j in zip(*np.where(Dr > -2))][:8]}")
            # census of eigenvalues of the local linearised map DR(theta) on interior grid points (not fixed points)
            ncx, ntot, minr = 0, 0, np.inf
            for t in tK[1:-1]:
                for mu in MU[1:-1]:
                    th = np.array([t, mu]); p, c = Rmap(th)
                    if np.any(np.isclose(p, lo, atol=1e-3) | np.isclose(p, hi, atol=1e-3)) or p[0] < 0.03:
                        continue
                    Jb = np.stack([ev(spb, th, idx, dx=1), ev(spb, th, idx, dy=1)], 1)
                    Js = np.stack([ev(sps, p, idx, dx=1), ev(sps, p, idx, dy=1)], 1)
                    T = np.linalg.lstsq(W[:, None] * Js, W[:, None] * Jb, rcond=None)[0]
                    e = np.linalg.eigvals(T); ntot += 1
                    if abs(e[0].imag) > 1e-9:
                        ncx += 1
                        y = np.log(e[0]) / np.log(b); minr = min(minr, abs(y.real) / abs(y.imag))
            print(f"-- n={n} {sname}: DR(theta) census (interior points whose image is interior): {ncx}/{ntot} complex; "
                  f"min Re/|Im| of ln(lam)/ln b among complex: {minr:.3g}")
            # fixed points: zeros of D from a seed grid, excluding the K=0 line
            fps = []
            for t0 in np.linspace(0.05, 0.95, 10):
                for m0 in np.linspace(-3, 9, 13):
                    r = least_squares(D, np.array([t0, m0]), bounds=(lo, hi))
                    th = r.x
                    chi = np.sqrt(2 * r.cost / len(idx))
                    if th[0] < 0.03 or chi > 2.0:
                        continue
                    if np.any(np.isclose(th, lo, atol=1e-3) | np.isclose(th, hi, atol=1e-3)):
                        continue
                    if any(np.linalg.norm((th - q[0]) / [0.05, 0.5]) < 1 for q in fps):
                        continue
                    fps.append((th, chi))
            # K=0 line eigenvalue (t direction): T_tt = (dA_big/dt)/(dA_small/dt) projected
            Jb0 = np.stack([ev(spb, np.array([0.0, 0.0]), idx, dx=1)], 1)
            Js0 = np.stack([ev(sps, np.array([0.0, 0.0]), idx, dx=1)], 1)
            lam0 = float(np.linalg.lstsq(W[:, None] * Js0, W[:, None] * Jb0, rcond=None)[0][0, 0])
            print(f"-- n={n} {sname}: K=0 line (fixed line, mu redundant there): t-eigenvalue {lam0:.3f} (real by construction)")
            if not fps:
                print(f"-- n={n} {sname}: NO interior fixed point (chi<=2, inside grid, t>=0.03)")
            for th, chi in fps:
                Jb = np.stack([ev(spb, th, idx, dx=1), ev(spb, th, idx, dy=1)], 1)
                Js = np.stack([ev(sps, th, idx, dx=1), ev(sps, th, idx, dy=1)], 1)
                T = np.linalg.lstsq(W[:, None] * Js, W[:, None] * Jb, rcond=None)[0]
                e = np.linalg.eigvals(T)
                ratio = abs(e[0].real) / abs(e[0].imag) if abs(e[0].imag) > 1e-9 else np.inf
                # note: RG eigenvalue lambda; spiral if complex pair. Re/Im quoted for log(lambda) (exponent y)
                y = np.log(e.astype(complex)) / np.log(b)
                ry = abs(y[0].real) / abs(y[0].imag) if abs(y[0].imag) > 1e-9 else np.inf
                print(f"-- n={n} {sname}: interior fixed point t={th[0]:.3f} (K={np.arctanh(th[0]):.3f}) mu={th[1]:+.2f} "
                      f"chi={chi:.2f}; eigenvalues {np.round(e,4)}; y=ln(lam)/ln b {np.round(y,4)}; Re/|Im| of y = {ry:.3g}")
                out.append((n, sname, th, e, ry))
    return out

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        analyse(fn)
