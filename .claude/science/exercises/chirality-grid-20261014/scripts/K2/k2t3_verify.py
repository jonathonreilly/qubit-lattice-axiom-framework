"""Follow-up V1 (PREREG.md): bug hunt on K2-T3 G1p delta=0.6 sets 1, 2. Independent brute-force code path (V1b)."""
import numpy as np, sys, time
from lat2d import Geom, rand_half, kernel, mineig, wrap
G = Geom(2, 6, False, -1); delta = 0.6; s = 0.25; k = 8
rng = np.random.default_rng(262)
sets = [[rand_half(rng, G, s, delta) for _ in range(k)] for _ in range(3)]
# V1a
for si in [1, 2]:
    for op in ['O', 'W']:
        Z, g, im = kernel(G, sets[si], delta, 32, 'tri', op, sym=False)
        print(f"V1a set {si} op {op}: full-matrix min/max {mineig(Z):+.4e}, symmetry defect {np.abs(Z - Z.conj().T).max():.1e}, min|H_W| {g:.3f}")
sys.stdout.flush()
# V1b: independent builder. sites ordered s = (t + T - 1) + Lt * x (different from lat2d), spin inner.
Lx, T = 2, 6; Lt = 2 * T; N = 2 * Lx * Lt; M = 1.0; m = 0.05
gx = np.array([[0, 1], [1, 0]], complex); gt = np.array([[0, -1j], [1j, 0]]); g5 = np.diag([1., -1.]).astype(complex)
def sidx(x, t): return 2 * ((t + T - 1) + Lt * (x % Lx))
def build_links(ua, ub, phi):
    """returns UX[x, ti], UT[x, ti] angles (ti = t + T - 1), UT for t -> t+1 (last slice unused)."""
    UX = np.zeros((Lx, Lt)); UT = np.full((Lx, Lt), np.nan)
    for t in range(1, T + 1):
        UX[:, t + T - 1] = ua['x'][t - 1]; UX[:, (1 - t) + T - 1] = ub['x'][t - 1]
    for t in range(1, T):
        UT[:, t + T - 1] = ua['t'][t - 1]; UT[:, (-t) + T - 1] = -ub['t'][t - 1]
    UT[:, 0 + T - 1] = phi
    return UX, UT
def plaqs(UX, UT):
    P = []
    for ti in range(Lt - 1):
        for x in range(Lx):
            P.append(UX[x, ti] + UT[(x + 1) % Lx, ti] - UX[x, ti + 1] - UT[x, ti])
    return wrap(np.array(P)).reshape(Lt - 1, Lx)
def DW(UX, UT):
    D = np.zeros((N, N), complex)
    for x in range(Lx):
        for ti in range(Lt):
            a = sidx(x, ti - T + 1); D[a:a+2, a:a+2] += 2 * np.eye(2)
            b = sidx(x + 1, ti - T + 1); sg = -1.0 if x == Lx - 1 else 1.0
            u = sg * np.exp(1j * UX[x, ti])
            D[a:a+2, b:b+2] += -0.5 * (np.eye(2) - gx) * u; D[b:b+2, a:a+2] += -0.5 * (np.eye(2) + gx) * np.conj(u)
            if ti < Lt - 1:
                b = sidx(x, ti - T + 2); u = np.exp(1j * UT[x, ti])
                D[a:a+2, b:b+2] += -0.5 * (np.eye(2) - gt) * u; D[b:b+2, a:a+2] += -0.5 * (np.eye(2) + gt) * np.conj(u)
    return D
def logdet(D, op):
    if op == 'W': return np.linalg.slogdet(D + m * np.eye(N))
    X = D - M * np.eye(N); w, V = np.linalg.eigh(X.conj().T @ X)
    Dov = np.eye(N) + X @ (V * (1 / np.sqrt(w))) @ V.conj().T
    return np.linalg.slogdet((1 - m / 2) * Dov + m * np.eye(N))
def tri(d): return np.clip(1 - np.abs(d) / delta, 0, None)
for si in [1, 2]:
    U = sets[si]
    for Ngrid in [20000, 40000]:
        t0 = time.time(); res = {}
        grid = -np.pi + 2 * np.pi * np.arange(Ngrid) / Ngrid
        for op in ['O', 'W']:
            L = np.full((k, k), -np.inf); Mt = np.zeros((k, k), complex)
            for a in range(k):
                for b in range(k):
                    UX, UT = build_links(U[a], U[b], np.zeros(Lx))
                    bulk = plaqs(UX, UT); assert np.all(np.abs(np.delete(bulk, T - 1, axis=0)) < delta)
                    # crossing plaquettes for each grid phase phi_1 (phi_0 = 0)
                    c = UX[:, T - 1] - UX[:, T]          # Ux(x,0) - Ux(x,1)
                    p0 = wrap(c[0] + grid - 0.0); p1 = wrap(c[1] + 0.0 - grid)
                    wts = tri(p0) * tri(p1); sel = np.nonzero(wts > 0)[0]
                    if len(sel) == 0: continue
                    # D(phi) = Db + e^{i phi} F + e^{-i phi} B, components solved from three explicit builds (independent code path)
                    Ds = [DW(*build_links(U[a], U[b], np.array([0.0, ph]))) for ph in (0.0, np.pi / 2, np.pi)]
                    F = 0.25 * ((Ds[0] - Ds[2]) - 1j * (Ds[1] - (Ds[0] + Ds[2]) / 2) * 2); Bm = 0.5 * (Ds[0] - Ds[2]) - F
                    Db = 0.5 * (Ds[0] + Ds[2])
                    chk = DW(*build_links(U[a], U[b], np.array([0.0, 0.37])))
                    assert np.abs(Db + np.exp(0.37j) * F + np.exp(-0.37j) * Bm - chk).max() < 1e-12
                    lds = []
                    for c0 in range(0, len(sel), 256):
                        e = np.exp(1j * grid[sel[c0:c0+256]])
                        Dg = Db[None] + e[:, None, None] * F[None] + np.conj(e)[:, None, None] * Bm[None]
                        if op == 'W':
                            sg, ld = np.linalg.slogdet(Dg + m * np.eye(N)[None])
                        else:
                            X = Dg - M * np.eye(N)[None]; w, V = np.linalg.eigh(np.conj(np.swapaxes(X, 1, 2)) @ X)
                            Dov = np.eye(N)[None] + X @ (V * (1 / np.sqrt(w))[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
                            sg, ld = np.linalg.slogdet((1 - m / 2) * Dov + m * np.eye(N)[None])
                        lds.append(ld + np.log(sg.astype(complex)))
                    lds = np.concatenate(lds)
                    lm = lds.real.max()
                    L[a, b] = lm; Mt[a, b] = np.sum(wts[sel] * np.exp(lds - lm)) * (2 * np.pi / Ngrid)
            d = L.diagonal(); md = Mt.diagonal().real
            Z = np.where(np.isfinite(L), Mt * np.exp(L - 0.5 * (d[:, None] + d[None, :])), 0) / np.sqrt(np.outer(md, md))
            res[op] = (mineig(Z), np.abs(Z - Z.conj().T).max(), Z)
        print(f"V1b set {si} grid {Ngrid}: overlap min/max {res['O'][0]:+.4e} (sym defect {res['O'][1]:.1e}) | Wilson min/max {res['W'][0]:+.4e} | {time.time()-t0:.0f}s")
        sys.stdout.flush()
        if Ngrid == 20000: Z20 = res['O'][2]
    print(f"   grid change overlap max|dZ| {np.abs(res['O'][2] - Z20).max():.1e}")
print("done")
