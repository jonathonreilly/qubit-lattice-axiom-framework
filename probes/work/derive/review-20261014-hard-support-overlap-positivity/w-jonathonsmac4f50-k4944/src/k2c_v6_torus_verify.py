"""K2c follow-up V6 (PREREG.md): independent torus builder for the hard W-matched torus pool.
Antiperiodic-time torus, Lx = 2 periodic x, own site indexing; temporal link index ti -> ti+1 (mod Lt), ti = Lt-1 is the
wrap link t = T -> t = -T+1 (fermion sign -1). Crossing links: plane A (t = 0 -> 1) = (0, a1); plane B (t = T -> -T+1) =
(b0, b1). Every plaquette from links; admissible a1 and y = b1 - b0 from the explicit crossing plaquettes; b0 trapezoid."""
import numpy as np, sys, time
POOL = sys.argv[1] if len(sys.argv) > 1 else 'pool_K2c_wgsearch_hard_O_torus_Lt12_seed4412.npz'
d = np.load(POOL); U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]; k = len(U)
T = d['ux'].shape[1]; Lx = 2; Lt = 2 * T; N = 2 * Lx * Lt; M = 1.0; m = 0.05; delta = 0.6; DB = 0.55
def wrap(a): return (a + np.pi) % (2 * np.pi) - np.pi
gx = np.array([[0, 1], [1, 0]], complex); gt = np.array([[0, -1j], [1j, 0]]); I2 = np.eye(2)
def sidx(x, ti): return 2 * (ti + Lt * (x % Lx))           # ti = t + T - 1 in 0..Lt-1
def links(ua, ub, a1, b0, b1):
    UX = np.zeros((Lx, Lt)); UT = np.zeros((Lx, Lt))
    for t in range(1, T + 1):
        UX[:, t + T - 1] = ua['x'][t - 1]; UX[:, (1 - t) + T - 1] = ub['x'][t - 1]
    for t in range(1, T):
        UT[:, t + T - 1] = ua['t'][t - 1]; UT[:, (-t) + T - 1] = -ub['t'][t - 1]
    UT[:, T - 1] = [0.0, a1]; UT[:, Lt - 1] = [b0, b1]
    return UX, UT
def plaqs(UX, UT):   # row ti: plaquette between slices ti and ti+1 (mod Lt)
    return wrap(np.array([[UX[x, ti] + UT[(x + 1) % Lx, ti] - UX[x, (ti + 1) % Lt] - UT[x, ti] for x in range(Lx)] for ti in range(Lt)]))
def D_of(UX, UT):
    D = 2.0 * np.eye(N, dtype=complex)
    for x in range(Lx):
        for ti in range(Lt):
            a = sidx(x, ti); b = sidx(x + 1, ti); u = np.exp(1j * UX[x, ti])        # x periodic for fermions (torus convention)
            D[a:a+2, b:b+2] += -0.5 * (I2 - gx) * u; D[b:b+2, a:a+2] += -0.5 * (I2 + gx) * np.conj(u)
            b = sidx(x, (ti + 1) % Lt); u = (-1.0 if ti == Lt - 1 else 1.0) * np.exp(1j * UT[x, ti])
            D[a:a+2, b:b+2] += -0.5 * (I2 - gt) * u; D[b:b+2, a:a+2] += -0.5 * (I2 + gt) * np.conj(u)
    return D
G5 = np.kron(np.eye(N // 2), np.diag([1., -1.]))
def logdet(D, op):
    if op == 'W': s, l = np.linalg.slogdet(D + m * np.eye(N)); return l + np.log(complex(s)), np.inf
    X = D - M * np.eye(N); w, V = np.linalg.eigh(X.conj().T @ X)
    gap = np.abs(np.linalg.eigvalsh(G5 @ X)).min()
    Dov = np.eye(N) + X @ (V * (1 / np.sqrt(w))) @ V.conj().T
    s, l = np.linalg.slogdet((1 - m / 2) * Dov + m * np.eye(N)); return l + np.log(complex(s)), gap
def interval_affine(c_plus, c_minus):
    """set of z with |wrap(c_plus + z)| < delta and |wrap(c_minus - z)| < delta, as list of intervals within one period window."""
    I0 = (-delta - c_plus, delta - c_plus); out = []
    for kk in (-1, 0, 1):
        I1 = (c_minus - delta + 2 * np.pi * kk, c_minus + delta + 2 * np.pi * kk)
        lo, hi = max(I0[0], I1[0]), min(I0[1], I1[1])
        if hi > lo: out.append((lo, hi))
    return out
def domains(ua, ub):
    UX, UT = links(ua, ub, 0.0, 0.0, 0.0); P = plaqs(UX, UT)
    bulk = np.delete(P, [T - 1, Lt - 1], axis=0); assert np.all(np.abs(bulk) <= DB + 1e-12)
    # plane A row T-1: p0 = c + a1 (UT[1] enters +), p1 = c' - a1; plane B row Lt-1: p0 = c + b1 - b0, p1 = c' - (b1 - b0)
    A = interval_affine(P[T - 1, 0], P[T - 1, 1]); B = interval_affine(P[Lt - 1, 0], P[Lt - 1, 1])
    return A, B, np.abs(bulk).max()
# dense-scan check of the explicit domains (first 3 x 3 pairs), and orientation check: perturb a1, b1 and recompute plaquettes
scan = np.linspace(-np.pi, np.pi, 100001)[:-1]; err = 0; maxb = 0
for a in range(k):
    for b in range(k):
        Ad, Bd, mb = domains(U[a], U[b]); maxb = max(maxb, mb)
        if a < 3 and b < 3:
            for (row, dom, mk) in ((T - 1, Ad, lambda z: links(U[a], U[b], z, 0.0, 0.0)), (Lt - 1, Bd, lambda z: links(U[a], U[b], 0.0, 0.0, z))):
                ok = np.array([np.all(np.abs(plaqs(*mk(z))[row]) < delta) for z in scan[::50]])
                err = max(err, abs(ok.mean() * 2 * np.pi - sum(h - l for l, h in dom)))
print(f"# V6 pool {POOL}: k={k} Lt={Lt}; explicit max bulk |plaquette| {maxb:.4f}; domain length vs scan (step 2pi/2000) max diff {err:.1e}", flush=True)
def kernel(op, nA, nB, nw, pairs):
    xa, wa = np.polynomial.legendre.leggauss(nA); xb, wb = np.polynomial.legendre.leggauss(nB)
    bw = 2 * np.pi * np.arange(nw) / nw; L = {}; gmin = np.inf
    for (a, b) in pairs:
        Ad, Bd, _ = domains(U[a], U[b]); vals = []; ws = []
        for (la, ha) in Ad:
            for (lb, hb) in Bd:
                for ia in range(nA):
                    a1 = 0.5 * (ha - la) * xa[ia] + 0.5 * (ha + la)
                    for ib in range(nB):
                        y = 0.5 * (hb - lb) * xb[ib] + 0.5 * (hb + lb)
                        for b0 in bw:
                            v, g = logdet(D_of(*links(U[a], U[b], a1, b0, b0 + y)), op); vals.append(v); gmin = min(gmin, g)
                            ws.append(0.25 * (ha - la) * (hb - lb) * wa[ia] * wb[ib] * 2 * np.pi / nw)
        l = np.array(vals); w = np.array(ws); lm = l.real.max(); L[(a, b)] = lm + np.log(np.sum(w * np.exp(l - lm)) + 0j)
    return L, gmin
def to_Z(L):
    Lm = np.zeros((k, k), complex)
    for (a, b), v in L.items(): Lm[a, b] = v; Lm[b, a] = np.conj(v)
    dd = Lm.diagonal().real; return np.exp(Lm - 0.5 * (dd[:, None] + dd[None, :]))
t00 = time.time(); allp = [(a, b) for a in range(k) for b in range(a, k)]
for op in ('O', 'W'):
    L1, g1 = kernel(op, 6, 6, 4, allp); Z1 = to_Z(L1); ev = np.linalg.eigvalsh(0.5 * (Z1 + Z1.conj().T))
    print(f"V6 {op} (6,6,4): lam_min {ev[0]:+.5e} min/max {ev[0]/ev[-1]:+.4e} imag-diag max {max(abs(L1[(i,i)].imag) for i in range(k)):.1e}"
          + (f" min|eig H_W| {g1:.3f}" if op == 'O' else "") + f" [{time.time()-t00:.0f}s]", flush=True)
    rs = np.random.default_rng(7); sub = sorted({(int(min(p)), int(max(p))) for p in rs.integers(0, k, (14, 2)) if p[0] != p[1]})[:10]
    L2, _ = kernel(op, 8, 8, 6, sub + [(i, i) for i in range(k)])
    dd = np.array([L2[(i, i)].real for i in range(k)])
    ch = max(abs(np.exp(L2[p] - 0.5 * (dd[p[0]] + dd[p[1]])) - Z1[p]) for p in sub)
    print(f"V6 {op}: (6,6,4) -> (8,8,6) max change on {len(sub)} entries {ch:.1e} -> E = k x change = {k*ch:.1e} [{time.time()-t00:.0f}s]", flush=True)
print("done")
