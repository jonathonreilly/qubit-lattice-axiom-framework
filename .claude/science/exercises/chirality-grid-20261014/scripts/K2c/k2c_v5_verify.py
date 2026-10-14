"""K2c follow-up V5 (PREREG.md) on the W-matched hard pool (default pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz).
V5a: independent explicit-link builder (re-typed from K2 V1b), hard admissible set from explicit crossing plaquettes,
D_ov = 1 + X (X^dag X)^{-1/2}; GL n = 32 and 64; full k x k matrix (no symmetry filling).
V5b: W-jitter robustness with the main code (hard, GL 16/32)."""
import numpy as np, sys, time
POOL = sys.argv[1] if len(sys.argv) > 1 else 'pool_K2c_wsearch_hard_O_open_Lt12_seed1401.npz'
d = np.load(POOL); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]; k = len(U)
T = d['ux'].shape[1]; Lx = 2; Lt = 2 * T; N = 2 * Lx * Lt; M = 1.0; m = 0.05; delta = 0.6; DB = 0.55
def wrap(a): return (a + np.pi) % (2 * np.pi) - np.pi
gx = np.array([[0, 1], [1, 0]], complex); gt = np.array([[0, -1j], [1j, 0]])
def sidx(x, t): return 2 * ((t + T - 1) + Lt * (x % Lx))        # site ordering different from lat2d
def build_links(ua, ub, phi):
    UX = np.zeros((Lx, Lt)); UT = np.full((Lx, Lt), np.nan)
    for t in range(1, T + 1):
        UX[:, t + T - 1] = ua['x'][t - 1]; UX[:, (1 - t) + T - 1] = ub['x'][t - 1]
    for t in range(1, T):
        UT[:, t + T - 1] = ua['t'][t - 1]; UT[:, (-t) + T - 1] = -ub['t'][t - 1]
    UT[:, T - 1] = phi
    return UX, UT
def plaqs(UX, UT):
    return wrap(np.array([[UX[x, ti] + UT[(x + 1) % Lx, ti] - UX[x, ti + 1] - UT[x, ti] for x in range(Lx)] for ti in range(Lt - 1)]))
def DW(UX, UT):
    D = np.zeros((N, N), complex)
    for x in range(Lx):
        for ti in range(Lt):
            a = sidx(x, ti - T + 1); D[a:a+2, a:a+2] += 2 * np.eye(2)
            b = sidx(x + 1, ti - T + 1); u = (-1.0 if x == Lx - 1 else 1.0) * np.exp(1j * UX[x, ti])
            D[a:a+2, b:b+2] += -0.5 * (np.eye(2) - gx) * u; D[b:b+2, a:a+2] += -0.5 * (np.eye(2) + gx) * np.conj(u)
            if ti < Lt - 1:
                b = sidx(x, ti - T + 2); u = np.exp(1j * UT[x, ti])
                D[a:a+2, b:b+2] += -0.5 * (np.eye(2) - gt) * u; D[b:b+2, a:a+2] += -0.5 * (np.eye(2) + gt) * np.conj(u)
    return D
def logdet(D, op):
    if op == 'W': s, l = np.linalg.slogdet(D + m * np.eye(N)); return l + np.log(complex(s))
    X = D - M * np.eye(N); w, V = np.linalg.eigh(X.conj().T @ X)
    Dov = np.eye(N) + X @ (V * (1 / np.sqrt(w))) @ V.conj().T
    s, l = np.linalg.slogdet((1 - m / 2) * Dov + m * np.eye(N)); return l + np.log(complex(s))
def adm_pieces(ua, ub):
    UX, UT = build_links(ua, ub, np.zeros(Lx)); P0 = plaqs(UX, UT)
    bulk = np.delete(P0, T - 1, axis=0); assert np.all(np.abs(bulk) <= DB + 1e-12), np.abs(bulk).max()
    c0 = P0[T - 1, 0]; c1 = P0[T - 1, 1]          # crossing plaquettes at phi_1 = 0: p0 = c0 + phi_1, p1 = c1 - phi_1
    I0 = (-delta - c0, delta - c0); out = []
    for kk in (-1, 0, 1):
        I1 = (c1 - delta + 2 * np.pi * kk, c1 + delta + 2 * np.pi * kk)
        lo, hi = max(I0[0], I1[0]), min(I0[1], I1[1])
        if hi > lo: out.append((lo, hi))
    return out, np.abs(bulk).max()
t00 = time.time(); scan = np.linspace(-np.pi, np.pi, 200001)[:-1]; maxb = 0; scanerr = 0
for a in range(k):
    for b in range(k):
        pcs, mb = adm_pieces(U[a], U[b]); maxb = max(maxb, mb)
        if a < 3 and b < 3:                       # dense-scan check of the admissible set
            UX, UT = build_links(U[a], U[b], np.zeros(Lx)); P0 = plaqs(UX, UT)
            ok = (np.abs(wrap(P0[T-1, 0] + scan)) < delta) & (np.abs(wrap(P0[T-1, 1] - scan)) < delta)
            scanerr = max(scanerr, abs(ok.mean() * 2 * np.pi - sum(h - l for l, h in pcs)))
print(f"# V5a pool {POOL}: k={k} Lt={Lt}; explicit max bulk |plaquette| {maxb:.4f} (<= {DB}); admissible-set length vs dense scan max diff {scanerr:.1e}", flush=True)
res = {}
for op in ['O', 'W']:
    for n in (32, 64):
        xg, wg = np.polynomial.legendre.leggauss(n); L = np.zeros((k, k), complex); gmin = np.inf
        for a in range(k):
            for b in range(k):
                pcs, _ = adm_pieces(U[a], U[b]); vals = []; ws = []
                for (lo, hi) in pcs:
                    ph = 0.5 * (hi - lo) * xg + 0.5 * (hi + lo); ws.append(0.5 * (hi - lo) * wg)
                    for p in ph:
                        UX, UT = build_links(U[a], U[b], np.array([0.0, p])); D = DW(UX, UT)
                        if op == 'O':
                            H = np.kron(np.eye(N // 2), np.diag([1., -1.])) @ (D - M * np.eye(N)); gmin = min(gmin, np.abs(np.linalg.eigvalsh(H)).min())
                        vals.append(logdet(D, op))
                l = np.array(vals); w = np.concatenate(ws); lm = l.real.max(); L[a, b] = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
        dd = L.diagonal().real; Z = np.exp(L - 0.5 * (dd[:, None] + dd[None, :]))
        res[(op, n)] = Z
        ev = np.linalg.eigvalsh(0.5 * (Z + Z.conj().T))
        print(f"V5a {op} n={n}: lam_min {ev[0]:+.5e} min/max {ev[0]/ev[-1]:+.4e} symmetry defect {np.abs(Z - Z.conj().T).max():.1e}"
              + (f" min|eig H_W| {gmin:.3f}" if op == 'O' else "") + f" [{time.time()-t00:.0f}s]", flush=True)
    print(f"V5a {op}: n32 -> n64 max entry change {np.abs(res[(op, 64)] - res[(op, 32)]).max():.1e}", flush=True)
# V5b: W-jitter with the main code
from k2c_lib import Geom, full_kernel, lam
G = Geom(2, T, False, -1); rj = np.random.default_rng(55); xi = rj.uniform(-1, 1, k)
for eps in (1e-4, 1e-3, 1e-2, 3e-2, 1e-1):
    Uj = [{'x': u['x'] + 0.5 * (eps * xi[i] - u['x'][0].sum()), 't': u['t']} for i, u in enumerate(U)]
    out = []
    for op in ('O', 'W', 'PG'):
        Zl, g1 = full_kernel(G, Uj, 16, None, op, 'hard'); Zh, g2 = full_kernel(G, Uj, 32, None, op, 'hard')
        E = k * np.abs(Zh - Zl).max() + 1e-13; a_, b_, _ = lam(Zh); out.append(f"{op} lam_min {a_:+.3e} (E {E:.0e})")
    print(f"V5b eps={eps:g}: " + " | ".join(out) + f" [{time.time()-t00:.0f}s]", flush=True)
print("done")
