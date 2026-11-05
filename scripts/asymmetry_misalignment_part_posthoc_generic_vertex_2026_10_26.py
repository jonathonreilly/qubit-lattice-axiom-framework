#!/usr/bin/env python3
"""POST HOC (not pre-registered; disclosed): rerun the cross-talk scan with a generic cell-periodic 4x4 vertex
V(c) (all spinor structures, symmetrised to each sector's residual antiunitary) so that the Lorentz-scalar channel
has non-degenerate inter-family entries; purpose: test whether D2's non-decaying leak survives when J_tree != 0."""
import numpy as np, itertools
src = __import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_sector_crosstalk_2026_10_26.py').read_text().split("# ------------------------------------------------------------------ setup checks")[0]
exec(src)
def vert_profiles(rng, kind):
    V, Phi = {}, {}
    def cm(): return rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    Timg_v = lambda A: C_T.T @ A.conj() @ C_T
    if kind == 'up':
        for c in BITS:
            if c[0] == 0: V[c] = cm(); Phi[c] = herm(rng)
        for c in BITS:
            if c[0] == 1: cp = xor(c, (1, 0, 0)); V[c] = Timg_v(V[cp]); Phi[c] = T_img(Phi[cp])
    else:
        for c in BITS:
            A = cm(); V[c] = (A + Timg_v(A)) / 2; G = herm(rng); Phi[c] = (G + T_img(G)) / 2
    return fourier(V), fourier(Phi)
def yuk_v(sl, Vh, l):
    r = sl.rows(l); Y = np.zeros((3, 3), complex)
    for ia, a in enumerate(FAM):
        for ib, b in enumerate(FAM):
            Y[ia, ib] = scalar(sl.Z[a][r].T @ Vh[xor(XN[a], XN[b])] @ sl.Z[b][r])
    return Y
def dressed_v(sl, Vh, l, Phh, lp):
    r, rp = sl.rows(l), sl.rows(lp); dZ = {}
    for a in FAM:
        for K in BITS:
            v = np.zeros_like(sl.Z[a]); v[rp] = Phh[K] @ sl.Z[a][rp]; dZ[a, K] = sl.R[xor(XN[a], K)] @ v
    dY = np.zeros((3, 3), complex)
    for ia, a in enumerate(FAM):
        for ib, b in enumerate(FAM):
            B = sum(sl.Z[a][r].T @ Vh[xor(xor(XN[a], XN[b]), K)] @ dZ[b, K][r] + dZ[a, K][r].T @ Vh[xor(xor(XN[a], XN[b]), K)] @ sl.Z[b][r] for K in BITS)
            dY[ia, ib] = scalar(B)
    return dY
sl = Slab(40); rng = np.random.default_rng(31337); N = 12
DRv = [(vert_profiles(rng, 'up'), vert_profiles(rng, 'down')) for _ in range(N)]
t = lambda Y, dY: -np.imag(np.trace(np.linalg.solve(Y, dY)))
print("Delta | a(up shallow): sin th_tree  |J|/Jmax  d<-u   u<-d | b(down shallow): d<-u   u<-d")
for D in (0, 1, 2, 4, 8, 12, 18):
    rowa, rowb = [], []
    for (Vu, Pu), (Vd, Pd) in DRv:
        lu, ld = 1, 1 + D
        Yu, Yd = yuk_v(sl, Vu, lu), yuk_v(sl, Vd, ld)
        rowa.append((abs(np.sin(np.angle(np.linalg.det(Yu @ Yd)))), abs(jarlskog(Yu, Yd)), abs(t(Yd, dressed_v(sl, Vd, ld, Pu, lu))), abs(t(Yu, dressed_v(sl, Vu, lu, Pd, ld)))))
        lu, ld = 1 + D, 1
        Yu, Yd = yuk_v(sl, Vu, lu), yuk_v(sl, Vd, ld)
        rowb.append((abs(t(Yd, dressed_v(sl, Vd, ld, Pu, lu))), abs(t(Yu, dressed_v(sl, Vu, lu, Pd, ld)))))
    ma = np.median(np.array(rowa), axis=0); mxs = max(x[0] for x in rowa); mb = np.median(np.array(rowb), axis=0)
    print(f"{D:5d} | max {mxs:.1e}  {ma[1]:.2e}  {ma[2]:.1e}  {ma[3]:.1e} | {mb[0]:.1e}  {mb[1]:.1e}")
